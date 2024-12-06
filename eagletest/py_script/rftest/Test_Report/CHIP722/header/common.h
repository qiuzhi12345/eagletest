#ifndef COMMON_H
#define COMMON_H


#if !defined (DIAG_UTILS_H_INCLUDED)
#define DIAG_UTILS_H_INCLUDED
// If you change this define, you must also change the plusarg "+DVMagicExit" 
// sent to the simulator
#define MAGIC_DIAG_EXIT XSHAL_SIMIO_BYPASS_VADDR
#endif
#define PRINT_LINE printline(__FILE__,__FUNCTION__,__LINE__)
#define CHECK_LINE(value,ref) checkline(value,ref,__FUNCTION__, __FILE__,__LINE__)

#define __ATTRIB_ALIGN(x)         __attribute__ ((aligned((x))))

int strlen (const char *str);

// Exit status
int set_diag_status(int stat);

// Place-holder routines
int diag_pass();
int diag_fail();

int pass(const char *msg);
int fail(const char *msg);

int Check (unsigned int address, unsigned int value, unsigned int mask);
int CheckU8 (unsigned char* AddressPtr, unsigned int value, unsigned int mask);

void printline(const char *file_name,const char *func_name,unsigned int line);
void checkline(unsigned int value,unsigned int ref,const char *file_name,const char *func_name,unsigned int line);

void err_print(const char * info_msg);
void printinfo(const char * info_msg,unsigned int value);
void ets_print(const char * info_msg,unsigned int value);

#define BIT(x) (0x1 << (x))

typedef unsigned long  U32,u32;
typedef unsigned char  U8,u8;
typedef unsigned short int  U16,u16;

//=========================
#define WRITE_PERI_REG(addr, val)        (*((volatile U32*)(addr))) = (U32)(val)
#define READ_PERI_REG(addr)              (*(volatile U32*)(addr))
#define CLEAR_PERI_REG_MASK(reg, mask)   WRITE_PERI_REG((reg), ((READ_PERI_REG(reg))&(~(mask))))
#define SET_PERI_REG_MASK(reg, mask)     WRITE_PERI_REG((reg), ((READ_PERI_REG(reg))|(mask)))
#define GET_PERI_REG_MASK(reg, mask)     ((READ_PERI_REG(reg))&(mask))
#define SET_PERI_REG_BITS(reg, bit_map, value, shift) (WRITE_PERI_REG((reg), ((READ_PERI_REG(reg))&(~((bit_map)<<(shift))))|((value&bit_map)<<(shift))))
#define GET_PERI_REG_BITS(reg, bit_map, shift)    ((READ_PERI_REG(reg))&((bit_map)<<(shift)))>>shift
//function

inline void mac_write(unsigned int addr, unsigned int value)
{
   *(volatile unsigned int*)(addr) = value;
}

inline void mac_write_byte(unsigned int addr, unsigned char value)
{
   *(volatile unsigned char*)(addr) = value;
}

inline void mac_write_halfword(unsigned int addr, unsigned short value)
{
   *(volatile unsigned short*)(addr) = value;
}

inline unsigned int mac_read(unsigned int addr)
{
   unsigned int value;
   value = *(volatile unsigned int*)(addr);
   return value;
}

inline unsigned char mac_read_byte(unsigned int addr)
{
   unsigned char value;
   value = *(volatile unsigned char*)(addr);
   return value;
}

inline unsigned short mac_read_halfword(unsigned int addr)
{
   unsigned short value;
   value = *(volatile unsigned short*)(addr);
   return value;
}

// (/ 300.0 64)
#define CPU_SPEED 5

void delay_ns(unsigned int n_ns)
{
   volatile unsigned int i = (n_ns * CPU_SPEED) >> 10;  //cpu instruction speed: 8M/s
   while(i--){};
}

void delay_us(unsigned int n_us)
{
  volatile unsigned int i = n_us * CPU_SPEED;  //cpu instruction speed: 16M/s
  while(i--){};
}


#endif
