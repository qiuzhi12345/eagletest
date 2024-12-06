#include "stdlib.h"
#include "malloc.h"

#include "./common.h"
#include "./soc_base.h"
#include "./soc.h"

void wait_unless(unsigned int addr,unsigned num)
{
	while( READ_PERI_REG( addr ) != num )
		;	
}

void intsram_config(void)
{
	unsigned int begin_addr = 0x3ff14000;
	unsigned int end_addr   = 0x3ff1407f;
	unsigned int temp;
	unsigned int i;
	
	for(i = begin_addr;i < 0x3ff14040 ;i = i + 4 )
	{
		*(volatile unsigned int*) (i) = i>>2;
	}
	
	for(i = 0x3ff14040;i < end_addr ;i = i + 4 )
	{
	//	temp = *(volatile unsigned int*) (i);
		temp = (0x2<<4) | ((0xf-(i/4)) & 0xf);
		*(volatile unsigned int*) (i) = temp;
	}
}

#define PROCACHE_IMMU_ADDR_BASE ( (CPU_PERI_CACHE_CONFIG_BASE) + 0x00001000 )
#define PROCACHE_DMMU_ADDR_BASE ( (CPU_PERI_CACHE_CONFIG_BASE) + 0x00001400 )
 
#define PROCACHE_ITAG_ADDR_BASE ( (CPU_PERI_CACHE_CONFIG_BASE) + 0x00002000 )
#define PROCACHE_DTAG_ADDR_BASE ( (CPU_PERI_CACHE_CONFIG_BASE) + 0x00003000 )

#define IRAM0_START_ADDR         0x40072000
#define IRAM0_END_ADDR           0x403FFFFF
#define IRAM1_START_ADDR         0x40400000
#define IRAM1_END_ADDR           0x407FFFFF
#define IROM0_START_ADDR         0x40800000
#define IROM0_END_ADDR           0x40BFFFFF

#define IAHB0_START_ADDR         0x60400000
#define IAHB0_END_ADDR           0x607FFFFF
#define IAHB1_START_ADDR         0x60800000
#define IAHB1_END_ADDR           0x60BFFFFF

#define DROM0_START_ADDR         0x3F000000
#define DROM0_END_ADDR           0x3F3FFFFF
#define IAHB2_START_ADDR         0x60C00000
#define IAHB2_END_ADDR           0x60FFFFFF

#define DRAM1_START_ADDR         0x3F800000
#define DRAM1_END_ADDR           0x3FBFFFFF

#define DRAM0_START_ADDR         0x3FC00000
#define DRAM0_END_ADDR           0x3FF9DFFF
#define DAHB0_START_ADDR         0x61000000
#define DAHB0_END_ADDR           0x613FFFFF

#define DPORT_START_ADDR         0x3F400000
#define DPORT_END_ADDR           0x3F7FFFFF
#define DAHB1_START_ADDR         0x61400000
#define DAHB1_END_ADDR           0x617FFFFF

//#define D_DROM0_START_ADDR       0x3F000000
//#define D_DROM0_END_ADDR         0x3F3FFFFF
#define DAHB2_START_ADDR         0x61800000
#define DAHB2_END_ADDR           0x61BFFFFF

//cache mmu register file address
#define CACHE_IMMU_ADDRESS_BASE (PROCACHE_IMMU_ADDR_BASE)
#define CACHE_DMMU_ADDRESS_BASE (PROCACHE_DMMU_ADDR_BASE)
//virtual address, physical address check
#define ADDRESS_CHECK(addr,psize) (((addr) & (0xFFFF >>((64/(psize))-1))) != 0)
//CPU number check
#define CPU_NUMBER_CHECK(cpu_no)  (((cpu_no)<0) || ((cpu_no)>1))
//flash MMU edge check (flash size default : 16*1024 K)
#define MMU_EDGE_CHECK(mmu_val,num,psize) (((mmu_val) + (num)) > ((16*1024)/(psize)))

#define CACHE_IMMU_ENTRY_SIZE 256 
#define CACHE_DMMU_ENTRY_SIZE 128 
//===========================================
//  function :     mmu_init
//  description:   initial cache mmu,
//                 set mmu table invalid bit as invalid,
//		   if parameter is valid, write mmu,
//		   else not write;     
//  conditions:
//                 before set cache mmu, fuction should be called
//  inputs:
//                 NONE, 
//  output:        NONE
//===========================================
void mmu_init(void)
{
    unsigned int mmu_addr;
    unsigned int mmu_init_val;
    mmu_init_val = 0x8000;
    for ( mmu_addr = 0; mmu_addr < CACHE_IMMU_ENTRY_SIZE; mmu_addr++){
        *(volatile unsigned int *)((CACHE_IMMU_ADDRESS_BASE +  mmu_addr * 4)) = mmu_init_val;
    }
}
//===========================================
//  function :     cache_mmu_set
//  description:   set cache mmu, 
//                 set external memory bit to select flash or sram,
//                 set its invalid bit as valid,
//		   if parameter is valid, write mmu,
//		   else not write;     
//  conditions:
//                 before cache enable, fuction should be called
//  inputs:
//                 vaddr       is CPU port address , which should be aligned by psize
//                 paddr       is physical address , which should be aligned by psize
//                 psize       is page size of 
//                             flash , which is 64(KB),32(KB),16(KB)
//                             sram , which is 32(KB),16(KB),8(KB),4(KB),2(KB)
//                 num         is number of pages to be set, which is 0 ~ (memory size)/(page size)
//                 flash_sel   flash will be selected
//                 sram_sel    sram will be selected
//  output:        return code
//                 0 : mmu set success
//                 1 : vaddr or paddr is not aligned
//                 2 : vaddr is out of range 
//                 3 : psize error
//                 4 : mmu table to be written is out of range
//                 5 : no memory is selected
//==========================================================
unsigned int cache_mmu_set(unsigned int vaddr, unsigned int paddr, 
	                   short psize, short num, short flash_sel, short sram_sel)
{
    unsigned int mmu_addr=0;
    unsigned int mmu_table_val=0;
    unsigned int mask_m = 0;
    short i=0,j=0,Group=0;
    //address check
    if( (ADDRESS_CHECK(vaddr,psize)) || (ADDRESS_CHECK(paddr,psize)) ){
        return 1;
    }
    unsigned int ibus3_src = GET_PERI_REG_BITS(SENSITIVE_CACHE_SOURCE_1_REG,0x1,SENSITIVE_PRO_CACHE_I_SOURCE_PRO_DROM0_S);
    unsigned int dbus3_src = GET_PERI_REG_BITS(SENSITIVE_CACHE_SOURCE_1_REG,0x1,SENSITIVE_PRO_CACHE_D_SOURCE_PRO_DROM0_S);
    //
    if(vaddr >= IRAM0_START_ADDR && vaddr <= IRAM0_END_ADDR){
        Group = 1;
    } else if(vaddr >= IRAM1_START_ADDR && vaddr <= IRAM1_END_ADDR){
        Group = 2;
    } else if(vaddr >= IAHB0_START_ADDR && vaddr <= IAHB0_END_ADDR){
        Group = 2;
    } else if(vaddr >= IROM0_START_ADDR && vaddr <= IROM0_END_ADDR){
        Group = 3;
    } else if(vaddr >= IAHB1_START_ADDR && vaddr <= IAHB1_END_ADDR){
        Group = 3;
    } else if(vaddr >= DROM0_START_ADDR && vaddr <= DROM0_END_ADDR){ 
        Group = ibus3_src ? 4 : 8;
    } else if(vaddr >= IAHB2_START_ADDR && vaddr <= IAHB2_END_ADDR){
        Group = 4;
    } else if(vaddr >= DRAM0_START_ADDR && vaddr <= DRAM0_END_ADDR){
        Group = 5;
    } else if(vaddr >= DAHB0_START_ADDR && vaddr <= DAHB0_END_ADDR){
        Group = 5;
    } else if(vaddr >= DRAM1_START_ADDR && vaddr <= DRAM1_END_ADDR){
        Group = 6;
    } else if(vaddr >= DPORT_START_ADDR && vaddr <= DPORT_END_ADDR){
        Group = 7;
    } else if(vaddr >= DAHB1_START_ADDR && vaddr <= DAHB1_END_ADDR){
        Group = 7;
    } else if(vaddr >= DAHB2_START_ADDR && vaddr <= DAHB2_END_ADDR){
        Group = 8;
    } else {
        return 2;
    }
    //MMU egde check
    if(MMU_EDGE_CHECK(mmu_table_val,num,psize)){
        return 4;
    }
    //mmu value
    mmu_table_val = paddr >> 16;

    switch(Group){
        case 1: mmu_addr =   0 + ((vaddr & 0x3FFFFF) >> 16);
		break;      
	case 2: mmu_addr =  64 + ((vaddr & 0x3FFFFF) >> 16);
		break;
	case 3: mmu_addr = 128 + ((vaddr & 0x3FFFFF) >> 16);
		break;
	case 4: mmu_addr = 192 + ((vaddr & 0x3FFFFF) >> 16);
		break;
	case 5: mmu_addr = 256 + ((vaddr & 0x3FFFFF) >> 16);
		break;
	case 6: mmu_addr = 320 + ((vaddr & 0x3FFFFF) >> 16);
		break;
	case 7: mmu_addr = 384 + ((vaddr & 0x3FFFFF) >> 16);
		break;
	case 8: mmu_addr = 448 + ((vaddr & 0x3FFFFF) >> 16);
		break;
	default: break;
    }
    
    if(flash_sel){
        mask_m = (0x1<<15);
    }else if(sram_sel){
        mask_m = (0x1<<16);
    }else{
	return 5;
    }

    for ( i = 0; i < num; i++){
        WRITE_PERI_REG(CACHE_IMMU_ADDRESS_BASE + mmu_addr*4, ((mmu_table_val + i)&0x7fff)|(mask_m));
        mmu_addr++;
    }
    return 0;
}


//===========================================
//  function :     icache_lock_init
//  description:   enable lock function of icache,
//  conditions:    vaddr_min and vaddr_max are both from the same CPU port,
//                 instruction space between vaddr_min and vaddr_max will be locked in cache,
//                 the maximum of locked size is 16KB.
//                 before cache enable, the fuction should be called.
//  inputs:
//                 vaddr_min is CPU port address ,which is IRam0,IRam1,IRom0 and DRom0 port address
//                 vaddr_max is CPU port address ,which is IRam0,IRam1,IRom0 and DRom0 port address
//                 psize     is page size of flash, which is 64(KB),32(KB),16(KB)
//                 section   is the section number to be locked of cache.
//  output:        return code
//                 0 : lock function configured successfully
//                 1 : page size is error
//                 2 : virtual address is error 
//                 3 : the size to be locked is out of range
//===========================================
unsigned int icache_lock_init(unsigned int vaddr, unsigned int size,unsigned int section)
{
    unsigned int value = 0;
    unsigned int tag = 0;
    tag = vaddr;
    if(section == 0){
        value  = (       tag<<EXTMEM_PRO_ICACHE_LOCK0_ADDR_S);
        WRITE_PERI_REG(EXTMEM_PRO_ICACHE_LOCK0_ADDR_REG, value);
        WRITE_PERI_REG(EXTMEM_PRO_ICACHE_LOCK0_SIZE_REG, size);
        SET_PERI_REG_MASK(EXTMEM_PRO_ICACHE_CTRL_REG,EXTMEM_PRO_ICACHE_LOCK0_EN);
    }else if(section == 1){
        value  = (       tag<<EXTMEM_PRO_ICACHE_LOCK1_ADDR_S);
        WRITE_PERI_REG(EXTMEM_PRO_ICACHE_LOCK1_ADDR_REG, value);    
        WRITE_PERI_REG(EXTMEM_PRO_ICACHE_LOCK1_SIZE_REG, size);
        SET_PERI_REG_MASK(EXTMEM_PRO_ICACHE_CTRL_REG,EXTMEM_PRO_ICACHE_LOCK1_EN);
    }
    return 0;
}
//===========================================
//  function :     dcache_lock_init
//  description:   enable lock function of dcache,
//  conditions:    vaddr_min and vaddr_max are both from the same CPU port,
//                 data space between vaddr_min and vaddr_max will be locked in cache,
//                 the maximum of locked size is 16KB.
//                 before cache enable, the fuction should be called.
//  inputs:
//                 vaddr_min is CPU port address ,which is DRam1 port address
//                 vaddr_max is CPU port address ,which is DRam1 port address
//                 psize     is page size of flash, which is 32(KB),16(KB),8(KB),4(KB),2(KB)
//                 section   is the section number to be locked of cache.
//  output:        return code
//                 0 : lock function configured successfully
//                 1 : page size is error
//                 2 : virtual address is error 
//                 3 : the size to be locked is out of range
//===========================================
unsigned int dcache_lock_init(unsigned int vaddr, unsigned int size, unsigned int section)
{
    unsigned int value = 0;
    unsigned int tag = 0;
    tag = vaddr;
    if(section == 0){
        value  = (       tag<<EXTMEM_PRO_DCACHE_LOCK0_ADDR_S);
        WRITE_PERI_REG(EXTMEM_PRO_DCACHE_LOCK0_ADDR_REG, value);
        WRITE_PERI_REG(EXTMEM_PRO_DCACHE_LOCK0_SIZE_REG, size);
        SET_PERI_REG_MASK(EXTMEM_PRO_DCACHE_CTRL_REG,EXTMEM_PRO_DCACHE_LOCK0_EN);
    }else if(section == 1){
        value  = (       tag<<EXTMEM_PRO_DCACHE_LOCK1_ADDR_S);
        WRITE_PERI_REG(EXTMEM_PRO_DCACHE_LOCK1_ADDR_REG, value);    
        WRITE_PERI_REG(EXTMEM_PRO_DCACHE_LOCK1_SIZE_REG, size);
        SET_PERI_REG_MASK(EXTMEM_PRO_DCACHE_CTRL_REG,EXTMEM_PRO_DCACHE_LOCK1_EN);
    }
    return 0;
}

void dcache_unlock(unsigned int vaddr, unsigned size)
{
    WRITE_PERI_REG(EXTMEM_PRO_DCACHE_MEM_SYNC0_REG,vaddr);
    SET_PERI_REG_BITS(EXTMEM_PRO_DCACHE_MEM_SYNC1_REG,EXTMEM_PRO_DCACHE_MEMSYNC_SIZE,size,EXTMEM_PRO_DCACHE_MEMSYNC_SIZE_S);
    SET_PERI_REG_MASK(EXTMEM_PRO_DCACHE_CTRL_REG,EXTMEM_PRO_DCACHE_UNLOCK_ENA);
    while(GET_PERI_REG_MASK(EXTMEM_PRO_DCACHE_CTRL_REG,EXTMEM_PRO_DCACHE_UNLOCK_DONE)==0);
}

void icache_unlock(unsigned int vaddr, unsigned size)
{
    WRITE_PERI_REG(EXTMEM_PRO_ICACHE_MEM_SYNC0_REG,vaddr);
    SET_PERI_REG_BITS(EXTMEM_PRO_ICACHE_MEM_SYNC1_REG,EXTMEM_PRO_ICACHE_MEMSYNC_SIZE,size,EXTMEM_PRO_ICACHE_MEMSYNC_SIZE_S);
    SET_PERI_REG_MASK(EXTMEM_PRO_ICACHE_CTRL_REG,EXTMEM_PRO_ICACHE_UNLOCK_ENA);
    while(GET_PERI_REG_MASK(EXTMEM_PRO_ICACHE_CTRL_REG,EXTMEM_PRO_ICACHE_UNLOCK_DONE)==0);
}

void icache_way_mode(unsigned int mode)
{
        SET_PERI_REG_BITS(EXTMEM_PRO_ICACHE_CTRL_REG,0x1,0x1,EXTMEM_PRO_ICACHE_ENABLE_S);
        SET_PERI_REG_BITS(EXTMEM_PRO_ICACHE_CTRL_REG,0x1,mode,EXTMEM_PRO_ICACHE_MODE_S);
}
void dcache_way_mode(unsigned int mode)
{
        SET_PERI_REG_BITS(EXTMEM_PRO_DCACHE_CTRL_REG,0x1,0x1,EXTMEM_PRO_DCACHE_ENABLE_S);
        SET_PERI_REG_BITS(EXTMEM_PRO_DCACHE_CTRL_REG,0x1,mode,EXTMEM_PRO_DCACHE_MODE_S);
}

typedef struct node{
	unsigned int	chainlink_header;
	void * 		buf_ptr;
	struct node * 	chainlink_next_ptr;
} chain;

typedef chain *pchain;

void link_insert(void * head, void * link)
{
	pchain p;
	p = (pchain) head;
	while(NULL != p->chainlink_next_ptr)
	{
		p = p->chainlink_next_ptr;
	}
	p->chainlink_next_ptr = (pchain) link;
}

void link_init(void *head,int *buf_ptr,unsigned int buf_length)
{
	unsigned int i;
	pchain p;
        p = (pchain)head;
	p->chainlink_header = ((1<<31)|(1<<30)|(0<<29)|(0<<28)|((buf_length)<<12)|(buf_length));
	//p->chainlink_header = ((1<<31)|(1<<30)|(0<<29)|(0<<28)|(buf_length<<12)|(0x100));
	p->buf_ptr = buf_ptr;
	p->chainlink_next_ptr = NULL;
}

void link_tail_set(pchain head)
{
	pchain p;
	p = head;
	while(NULL != p->chainlink_next_ptr)
	{
		p = p->chainlink_next_ptr;
	}
	p->chainlink_header = (p->chainlink_header)|(0x40000000);
}

void link_connect(void * head, void * tail)
{
	pchain p1,p2;
	p1 = (pchain) head;
	p2 = (pchain) tail;
	p1->chainlink_next_ptr = p2;
	p2->chainlink_next_ptr = p1;
}

unsigned int crc32(unsigned int *data,unsigned int size)
{
	unsigned int i = 0,j=0,crc = 0xFFFFFFFF,table_value=0;
	unsigned int  crc_table[256];
	char     data_temp = 0;
	for(i = 0; i< 256;i++){
		table_value = i;
		for(j = 0;j<8;j++){
			if(table_value&1){
				table_value = (table_value>>1)^(0xEDB88320);
			}else{
				table_value = (table_value>>1);
			}
		}
		crc_table[i] = table_value;
	}
	for (i = 0;i < size;i++){
		for(j = 0;j < 4;j++){
		    data_temp = (char)(data[i]>>(j*8));
		    printinfo("data_temp = \n",data_temp);
		    crc = crc_table[(crc^data_temp)&0xff] ^ (crc>>8);
		}
	}
	return crc;
}

