void icache_enable_32k_pro(unsigned int mode,unsigned int flash_psize)
{
	// no mask, no segm en, no flash segm, no force on;
        SET_PERI_REG_BITS(EXTMEM_PRO_ICACHE_CTRL_REG,0x1,mode,EXTMEM_PRO_ICACHE_MODE_S);
        SET_PERI_REG_BITS(EXTMEM_PRO_ICACHE_CTRL_REG,0x1,0x1,EXTMEM_PRO_ICACHE_ENABLE_S);
}
void dcache_enable_32k_pro(unsigned int mode,unsigned int sram_psize)
{
	// no mask, no segm en, no flash segm, no force on;
        SET_PERI_REG_BITS(EXTMEM_PRO_DCACHE_CTRL_REG,0x1,mode,EXTMEM_PRO_DCACHE_MODE_S);
        SET_PERI_REG_BITS(EXTMEM_PRO_DCACHE_CTRL_REG,0x1,0x1,EXTMEM_PRO_DCACHE_ENABLE_S);
}

void cache_flush_pro(void)
{ 
	unsigned int temp;
	temp = READ_PERI_REG( EXTMEM_PRO_DCACHE_CTRL_REG );
	WRITE_PERI_REG( EXTMEM_PRO_DCACHE_CTRL_REG, temp & 0xffffffef );
	WRITE_PERI_REG( EXTMEM_PRO_DCACHE_CTRL_REG, temp | 0x00000010 ); // cache flush;
	while( ( READ_PERI_REG( EXTMEM_PRO_DCACHE_CTRL_REG ) & 0x00000020 ) != 0x00000020 ) {
	} 						// wait cache flush done;
}

void spi_mask( unsigned int mask_pro, unsigned int mask_app )
{
}


void spi_crypt( unsigned int enable )
{
}

void pro_write_dram(unsigned int addr, unsigned int data)
{
	*(volatile unsigned int *)(0x3fffff20) = addr;
	__asm__ __volatile__ (
				"MOVI	    a2,0	  \n"
				"WSR 	    a2,SCOMPARE1  \n" 
				"ISYNC 			  \n" 
				"MOV        a3,%0	  \n" 
				"L32R 	    a2,%1         \n" 
				"S32C1I     a3,a2,%2	  \n"
				:
				: "a" (data),"i"(0x3fffff20), "i"(0)
	    		     );
}


