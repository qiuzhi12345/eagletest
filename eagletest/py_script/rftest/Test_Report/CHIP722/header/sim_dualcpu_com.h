/*
 * sim_dualcpu_com.h
 *
 *  Created on: Mar 16, 2016
 *      Author: qgu
 */

#ifndef SIM_DUALCPU_COM_H_
#define SIM_DUALCPU_COM_H_


// sections define
#define FUNC_SEC_INTER_MEM_POOL0 	__attribute__((section(".iram0_sram_0.text")))
#define FUNC_SEC_INTER_MEM_POOL3 	__attribute__((section(".iram0_sram_3.text")))
#define FUNC_SEC_INTER_MEM_POOL4 	__attribute__((section(".iram0_sram_4.text")))
#define FUNC_SEC_INTER_MEM_POOL5 	__attribute__((section(".iram0_sram_5.text")))
#define FUNC_SEC_INTER_MEM_POOL6 	__attribute__((section(".iram0_sram_6.text")))
#define FUNC_SEC_INTER_MEM_POOL7 	__attribute__((section(".iram0_sram_7.text")))
#define FUNC_SEC_FLASH			__attribute__((section(".iram0_1.text")))

FUNC_SEC_INTER_MEM_POOL0 int pool0_test(){
	int a, b, c, d;
	a = 0x1234;
	b = 0x5678;
	c = 0xabcd;
	d = 0xdead;
	a = a ^ b ^ c ^ d;
	b = a ^ b ^ c ^ d;
	c = a ^ b ^ c ^ d;
	d = a ^ b ^ c ^ d;
	a = a ^ b ^ c ^ d;
	b = a ^ b ^ c ^ d;
	c = a ^ b ^ c ^ d;
	d = a ^ b ^ c ^ d;
	return d;
}

FUNC_SEC_INTER_MEM_POOL3 int pool3_test(){
	int a, b, c, d;
	a = 0x1234;
	b = 0x5678;
	c = 0xabcd;
	d = 0xdead;
	a = a ^ b ^ c ^ d;
	b = a ^ b ^ c ^ d;
	c = a ^ b ^ c ^ d;
	d = a ^ b ^ c ^ d;
	a = a ^ b ^ c ^ d;
	b = a ^ b ^ c ^ d;
	c = a ^ b ^ c ^ d;
	d = a ^ b ^ c ^ d;
	return d;
}

FUNC_SEC_INTER_MEM_POOL4 int pool4_test(){
	int a, b, c, d;
	a = 0x1234;
	b = 0x5678;
	c = 0xabcd;
	d = 0xdead;
	a = a ^ b ^ c ^ d;
	b = a ^ b ^ c ^ d;
	c = a ^ b ^ c ^ d;
	d = a ^ b ^ c ^ d;
	a = a ^ b ^ c ^ d;
	b = a ^ b ^ c ^ d;
	c = a ^ b ^ c ^ d;
	d = a ^ b ^ c ^ d;
	return d;
}

FUNC_SEC_INTER_MEM_POOL5 int pool5_test(){
	int a, b, c, d;
	a = 0x1234;
	b = 0x5678;
	c = 0xabcd;
	d = 0xdead;
	a = a ^ b ^ c ^ d;
	b = a ^ b ^ c ^ d;
	c = a ^ b ^ c ^ d;
	d = a ^ b ^ c ^ d;
	a = a ^ b ^ c ^ d;
	b = a ^ b ^ c ^ d;
	c = a ^ b ^ c ^ d;
	d = a ^ b ^ c ^ d;
	return d;
}

FUNC_SEC_INTER_MEM_POOL6 int pool6_test(){
	int a, b, c, d;
	a = 0x1234;
	b = 0x5678;
	c = 0xabcd;
	d = 0xdead;
	a = a ^ b ^ c ^ d;
	b = a ^ b ^ c ^ d;
	c = a ^ b ^ c ^ d;
	d = a ^ b ^ c ^ d;
	a = a ^ b ^ c ^ d;
	b = a ^ b ^ c ^ d;
	c = a ^ b ^ c ^ d;
	d = a ^ b ^ c ^ d;
	return d;
}

FUNC_SEC_INTER_MEM_POOL7 int pool7_test(){
	int a, b, c, d;
	a = 0x1234;
	b = 0x5678;
	c = 0xabcd;
	d = 0xdead;
	a = a ^ b ^ c ^ d;
	b = a ^ b ^ c ^ d;
	c = a ^ b ^ c ^ d;
	d = a ^ b ^ c ^ d;
	a = a ^ b ^ c ^ d;
	b = a ^ b ^ c ^ d;
	c = a ^ b ^ c ^ d;
	d = a ^ b ^ c ^ d;
	return d;
}


FUNC_SEC_FLASH int dcache_read(unsigned int start_addr_d,unsigned int addr_offset_d,\
			       unsigned int data_len,unsigned int read_num)
{
	unsigned int j,error,temp;
	error = 0;
	for( j=0;j<(data_len<<2);j=j+4 ) {
	        temp = start_addr_d+addr_offset_d+j;
		if( READ_PERI_REG( temp ) != (temp) ) {
			error = 1;
			return error;
		}
	}
	return error;
}

FUNC_SEC_FLASH int dcache_write(unsigned int start_addr_d,unsigned int addr_offset_d,\
				unsigned int data_len,unsigned int *data_buffer,\
				unsigned int read_num)
{
	unsigned int j,k,error;
	unsigned int tmp[16],ii;
	error = 0;
	for( j=0;j<(data_len<<2);j=j+4 ) {
		WRITE_PERI_REG(( start_addr_d+addr_offset_d+j ),data_buffer[j>>2]);
	}
	dcache_flush(0,1);
	dcache_invalidate(0,1);
	for( k=0;k<(data_len<<2);k=k+4 ) {
		tmp[k>>2] = READ_PERI_REG( start_addr_d+addr_offset_d+k );
		if( tmp[k>>2] != data_buffer[k>>2] ) {
			error = 1;
		        for(ii=0;ii<=(k>>2);ii++){
				printinfo("databuffer;",data_buffer[ii]);
				printinfo("data;\n",tmp[ii]);
			}
			return error;
		}
	}
	return error;
}

#endif /* SIM_DUALCPU_INMEM_FUNCS_H_ */
