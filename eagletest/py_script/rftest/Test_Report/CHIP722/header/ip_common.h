
#ifndef IP_COMMON

	#define IP_COMMON

	#include <xtensa/hal.h>
	#include <xtensa/config/core.h>
	#include <xtensa/config/system.h>
	#include "./diag_utils.h"


	// bus;

	#define BUS_IRAM0_BASE			(0x40000000)

	#define BUS_IRAM1_BASE			(0x40400000)

	#define BUS_IROM0_BASE			(0x40800000)

	#define BUS_DRAM0_BASE			(0x3ff80000)

	#define BUS_DRAM1_BASE			(0x3f800000)

	#define BUS_DROM0_BASE			(0x3f400000)

	#define BUS_DPORT_BASE			(0x3fe00000)
	#define BUS_DPORT_CPU_PERI_BASE		( (BUS_DPORT_BASE) + (0x000c0000) )
	#define BUS_DPORT_APB_PERI_BASE		( (BUS_DPORT_BASE) + (0x00000000) )

	#define BUS_AHB_0_BASE			(0x50000000)
	#define BUS_AHB_1_BASE			(0x60000000)
	#define BUS_AHB_APB_PERI_BASE		( (BUS_AHB_1_BASE) + (0x00000000) )


	// cpu_peripheral;

	#define CPU_PERI_BASE			(BUS_DPORT_CPU_PERI_BASE)

	#define CPU_PERI_SYSTEM_REG_BASE	( (CPU_PERI_BASE) + (0x00000000) )
	#define CPU_PERI_SENSITIVE_REG_BASE	( (CPU_PERI_BASE) + (0x00001000) )
	#define CPU_PERI_INTERRUPT_REG_BASE	( (CPU_PERI_BASE) + (0x00002000) )
	#define CPU_PERI_DMA_COPY_BASE		( (CPU_PERI_BASE) + (0x00003000) )
	#define CPU_PERI_CACHE_CONFIG_BASE	( (CPU_PERI_BASE) + (0x00004000) )
	#define CPU_PERI_AES			( (CPU_PERI_BASE) + (0x00008000) )
	#define CPU_PERI_SHA			( (CPU_PERI_BASE) + (0x00009000) )
	#define CPU_PERI_RSA			( (CPU_PERI_BASE) + (0x0000a000) )
	#define CPU_PERI_SECURE_BOOT		( (CPU_PERI_BASE) + (0x0000b000) )
	#define CPU_PERI_HMAC			( (CPU_PERI_BASE) + (0x0000c000) )
	#define CPU_PERI_DIGITAL_SIGNATURE	( (CPU_PERI_BASE) + (0x0000d000) )
	#define CPU_PERI_ASSIST_DEBUG		( (CPU_PERI_BASE) + (0x0000e000) )
	#define CPU_PERI_DEDICATED_GPIO		( (CPU_PERI_BASE) + (0x0000f000) )
	#define CPU_PERI_INTRUSION		( (CPU_PERI_BASE) + (0x00010000) )

	#define REG_DPORT_BASE			(CPU_PERI_SYSTEM_REG_BASE)
	#define REG_SYSTEM_BASE			(CPU_PERI_SYSTEM_REG_BASE)
	#define REG_SENSITIVE_BASE		(CPU_PERI_SENSITIVE_REG_BASE)
	#define REG_INTERRUPT_BASE		(CPU_PERI_INTERRUPT_REG_BASE)


	// apb_peripheral;

	#ifdef APB_PERI_USE_DPORT
		#define APB_PERI_BASE BUS_DPORT_APB_PERI_BASE
	#else
		#define APB_PERI_BASE BUS_AHB_APB_PERI_BASE
	#endif

	#define REG_SPI_MEM_BASE( i ) ( \
		( (i) == 0 ) ?		( (APB_PERI_BASE) + (0x00003000) ) : \
		( (i) == 1 ) ?		( (APB_PERI_BASE) + (0x00002000) ) : \
		( (i) == 4 ) ?		( (APB_PERI_BASE) + (0x00036000) ) : \
		( (i) == 5 ) ?		( (APB_PERI_BASE) + (0x00037000) ) : \
		0 \
	)
	// 0 : g0spi_0 : 0x1000;
	// 1 : g0spi_1 : 0x1000;
	// 4 : g1spi_0 : 0x1000;
	// 5 : g1spi_1 : 0x1000;

	#define REG_SPI_BASE( i ) ( \
		( (i) == 2 ) ?		( (APB_PERI_BASE) + (0x00024000) ) : \
		( (i) == 3 ) ?		( (APB_PERI_BASE) + (0x00025000) ) : \
		0 \
	)
	// 2 : spi_2 : 0x1000;
	// 3 : spi_3 : 0x1000;

	#define REG_RMT_BASE		( (APB_PERI_BASE) + (0x00016000) )
	// rmt : 0x1000;
	
	#define REG_I2C_EXT_BASE( i ) ( \
		( (i) == 0 ) ?		( (APB_PERI_BASE) + (0x00013000) ) : \
		( (i) == 1 ) ?		( (APB_PERI_BASE) + (0x00027000) ) : \
		0 \
	)
	// i2c_ext0 : 0x1000;
	// i2c_ext1 : 0x1000;

	#define REG_PCNT_BASE		( (APB_PERI_BASE) + (0x00017000) ) 
	// pcnt : 0x1000;
	
	#define REG_LEDC_BASE		( (APB_PERI_BASE) + (0x00019000) )
	// ledc : 0x1000;
	
	#define REG_I2S_BASE( i ) ( \
		( (i) == 0 ) ?		( (APB_PERI_BASE) + (0x0000f000) ) : \
		( (i) == 1 ) ?		( (APB_PERI_BASE) + (0x0002d000) ) : \
		0 \
	)
	// i2s0 : 0x1000;
	// i2s1 : 0x1000;

	#define REG_UHCI_BASE(i) ( \
		( (i) == 0 ) ?		( (APB_PERI_BASE) + (0x00014000) ) : \
		( (i) == 1 ) ?		( (APB_PERI_BASE) + (0x0000c000) ) : \
		0 \
	)
	// uhci0 : 0x1000;
	// uhci1 : 0x1000;
		
	#define REG_UART_BASE( i ) (\
		( (i) == 0 ) ?		( (APB_PERI_BASE) + (0x00000000) ) : \
		( (i) == 1 ) ?		( (APB_PERI_BASE) + (0x00010000) ) : \
		( (i) == 2 ) ?		( (APB_PERI_BASE) + (0x0002e000) ) : \
		0 \
	)
	// uart  : 0x1000;
	// uart1 : 0x1000;
	// uart2 : 0x1000;
	
	#define DR_REG_CAN_BASE		( (APB_PERI_BASE) + (0x0002b000) )
	// can : 0x1000;

	#define REG_SLCHOST_BASE	( (APB_PERI_BASE) + (0x00015000) ) 
	// slchost : 0x1000;

	#define REG_SLC_BASE		( (APB_PERI_BASE) + (0x00018000) ) 
	// slc : 0x1000;

	#define PWM_REGISTER_BASE( i ) ( \
		( (i) == 0 ) ?		( (APB_PERI_BASE) + (0x0001e000) ) : \
		( (i) == 1 ) ?		( (APB_PERI_BASE) + (0x0002c000) ) : \
		0 \
	)
	// 0 : pwm0 : 0x1000;
	// 1 : pwm1 : 0x1000;

	#define MCPWM_REGISTER_BASE( i ) ( \
		( (i) == 0 ) ?		( (APB_PERI_BASE) + (0x0002f000) ) : \
		( (i) == 1 ) ?		( (APB_PERI_BASE) + (0x00030000) ) : \
		0 \
	)
	// 0 : pwm2 : 0x1000;
	// 1 : pwm3 : 0x1000;

	#define REG_TIMERS_BASE( i ) ( \
		( (i) == 0 ) ?		( (APB_PERI_BASE) + (0x0001f000) ) : \
		( (i) == 1 ) ?		( (APB_PERI_BASE) + (0x00020000) ) : \
		0 \
	)
	// 0 : timergroup  : 0x1000;
	// 1 : timergroup1 : 0x1000;

	#define REG_HINF_BASE		( (APB_PERI_BASE) + (0x0000b000) ) 
	// hinf : 0x1000;

	#define REG_EFUSE_BASE		( (APB_PERI_BASE) + (0x0001a000) )
	// efuse : 0x1000;

	#define RTC_SLOWMEM_BASE	( (APB_PERI_BASE) + (0x00021000) )
	// rtc_slowmem : 0x2000;


	// other;

	#define REG_WDEVBT_BASE  0x60032000
	#define REG_WDEVLE_BASE  0x60032400
	#define REG_WDEV_BASE  0x60033000
	#define REG_WDEVRX_BASE  0x60033000
	#define REG_WDEVTX_BASE  0x60033400
	#define REG_WDEVSEC_BASE  0x60033800
	#define REG_WDEVSCH_BASE  0x60033c00
	#define REG_WDEVTXQMEM_BASE  0x60034000
	#define REG_WDEVPWR_BASE  0x60035000

	#define apb_int_offset 0x60000200
	#define cpu_to_share_ram_offset 0x3ffc0000

	#define apb_sp2_offset 0x60000b00
	#define apb_bb_offset 0x60000000
	//#define apb_bbtx_offset 0x60008400
	//#define apb_bbagc_offset 0x60008000
	//#define apb_bbbrx_offset 0x60008800
	//#define apb_bbnrx_offset 0x60008c00
	#define REG_AGC_BASE  0x6001C000
	#define REG_BBTX_BASE 0x6001C400
	#define REG_BRX_BASE  0x6001C800
	#define REG_NRX_BASE  0x6001CC00
	#define REG_BB_BASE   0x6001D000
	#define REG_MISC_BASE 0x6000D000
	#define REG_I2C_BASE  0x6000E000
	#define REG_I2C_MST_BASE  0x6000E000

	#define REG_SYSTIMER_BASE 0x60023000
	#define REG_APB_CTRL_BASE 0x60026000

	#define REG_GPIO_BASE        0x60004000
	#define REG_GPIO_SD_BASE	0x60004f00
	#define REG_FE2_BASE         0x60005000
	#define REG_FE_BASE          0x60006000

	#define REG_IO_MUX_BASE      0x60009000

	#define REG_BT_BASE          0x60011000
	#define REG_BT_V2_BASE	     0x60011000
	#define REG_BT_BUFFER_BASE   0x60012000

	#define REG_IO_MUX_BASE 0x60009000
	#define REG_RTCCNTL_BASE 0x60008000
	#define REG_RTCIO_BASE 0x60008400
	#define REG_RTCANA_CNTL_BASE 0x60008800
	#define REG_SAR_BASE  0x60008800
	#define REG_RTC_I2C_BASE 0x60008c00
	#define REG_RTCSAR_I2C_BASE 0x60008c00
	#define REG_PWM_BASE 0x6001E000
	#define REG_PWM_BASE 0x6001E000

	//=========================
	#define WRITE_PERI_REG(addr, val)        (*((volatile U32*)(addr))) = (U32)(val)
	#define READ_PERI_REG(addr)              (*(volatile U32*)(addr))
	#define CLEAR_PERI_REG_MASK(reg, mask)   WRITE_PERI_REG((reg), ((READ_PERI_REG(reg))&(~(mask))))
	#define SET_PERI_REG_MASK(reg, mask)     WRITE_PERI_REG((reg), ((READ_PERI_REG(reg))|(mask)))
	#define GET_PERI_REG_MASK(reg, mask)     ((READ_PERI_REG(reg))&(mask))
	#define SET_PERI_REG_BITS(reg, bit_map, value, shift) (WRITE_PERI_REG((reg), ((READ_PERI_REG(reg))&(~((bit_map)<<(shift))))|((value&bit_map)<<(shift))))
	#define GET_PERI_REG_BITS(reg, bit_map, shift)    ((READ_PERI_REG(reg))&((bit_map)<<(shift)))>>shift
	//function

	#define __ATTRIB_ALIGN(x)         __attribute__ ((aligned((x))))

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

	typedef unsigned long  U32,u32;
	typedef unsigned char  U8,u8;
	typedef unsigned short int  U16,u16;

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

