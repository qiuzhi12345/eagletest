void cache_enable_32k_app(unsigned int mode,unsigned int flash_psize,unsigned int sram_psize)
{
	// no mask, no segm en, no flash segm, no force on;
	unsigned int temp;
	temp = READ_PERI_REG( DPORT_APP_CACHE_CTRL_REG );
	temp |= (0x000000B|(mode<< DPORT_APP_CACHE_MODE_S));
	WRITE_PERI_REG( DPORT_APP_CACHE_CTRL_REG, temp);
        SET_PERI_REG_BITS(DPORT_APP_CACHE_CTRL1_REG,DPORT_APP_CMMU_FLASH_PAGE_MODE,\
	                  flash_psize,DPORT_APP_CMMU_FLASH_PAGE_MODE_S);
	SET_PERI_REG_BITS(DPORT_APP_CACHE_CTRL1_REG,DPORT_APP_CMMU_SRAM_PAGE_MODE,\
	                  sram_psize,DPORT_APP_CMMU_SRAM_PAGE_MODE_S);//
}

void cache_flush_app(void)
{ 
	unsigned int temp;
	temp = READ_PERI_REG( DPORT_APP_CACHE_CTRL_REG );
	WRITE_PERI_REG( DPORT_APP_CACHE_CTRL_REG, temp & 0xffffffdf );
	WRITE_PERI_REG( DPORT_APP_CACHE_CTRL_REG, temp | 0x00000020 ); // cache flush;
	while( ( READ_PERI_REG( DPORT_APP_CACHE_CTRL_REG ) & 0x00000040 ) != 0x00000040 ) {
		;
	} 						// wait cache flush done;
}

void cache_lock_en_app( unsigned int en_0, unsigned int en_1 )
{
	unsigned int temp;

	temp = READ_PERI_REG( DPORT_APP_CACHE_CTRL_REG );
	temp = temp & ~0x000000c0;
	
	WRITE_PERI_REG( DPORT_APP_CACHE_CTRL_REG, temp | (en_0%2)<<6 | (en_1%2)<<7 );
}

void app_cache_mmu_flash_table_init(void)
{
	unsigned int mmu_start_addr = 0x3ff12120;
	unsigned int mmu_end_addr   = 0x3ff12200;
	unsigned int i;
	for (i = 0;i<(mmu_end_addr-mmu_start_addr);i++)
	{
		WRITE_PERI_REG(mmu_start_addr+(i<<2),0x0);
	}
}

void app_cache_mmu_sram_table_init(void)
{
	unsigned int mmu_start_addr = 0x3ff13200;
	unsigned int mmu_end_addr   = 0x3ff13400;
	unsigned int i;
	for (i = 0;i<(mmu_end_addr-mmu_start_addr);i++)
	{
		WRITE_PERI_REG(mmu_start_addr+(i<<2),i);
	}
}

void app_write_dram(unsigned int addr, unsigned int data)
{
	*(volatile unsigned int *)(0x3fffff00) = addr;
	__asm__ __volatile__ (
				"MOVI	    a2,0	  \n"
				"WSR 	    a2,SCOMPARE1  \n" 
				"ISYNC 			  \n" 
				"MOV        a3,%0	  \n" 
				"L32R 	    a2,%1         \n" 
				"S32C1I     a3,a2,%2	  \n"
				:
				: "a" (data),"i"(0x3fffff00), "i"(0)
	    		     );
}
