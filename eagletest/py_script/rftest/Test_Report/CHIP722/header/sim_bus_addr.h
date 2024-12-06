
#define ADDR_IRAM0_ROM_0	(0x40000000)
#define ADDR_IRAM0_ROM_1	(0x40010000)
#define ADDR_IRAM0_ROM_2	(0x40020000)
#define ADDR_IRAM0_ROM_3	(0x40030000)
#define ADDR_IRAM0_ROM_4	(0x40040000)
#define ADDR_IRAM0_RTCFAST	(0x40050000)
#define ADDR_IRAM0_SRAM_0	(0x40052000)
#define ADDR_IRAM0_SRAM_1	(0x40054000)
#define ADDR_IRAM0_SRAM_2	(0x40056000)
#define ADDR_IRAM0_SRAM_3	(0x40058000)
#define ADDR_IRAM0_SRAM_4	(0x4005c000)
#define ADDR_IRAM0_SRAM_5	(0x40060000)
#define ADDR_IRAM0_SRAM_6	(0x40064000)
#define ADDR_IRAM0_SRAM_7	(0x40068000)
#define ADDR_IRAM0_SRAM_8	(0x4006c000)
#define ADDR_IRAM0_SRAM_9	(0x40070000)
#define ADDR_IRAM0_SRAM_10	(0x40074000)
#define ADDR_IRAM0_SRAM_11	(0x40078000)
#define ADDR_IRAM0_SRAM_12	(0x4007c000)
#define ADDR_IRAM0_SRAM_13	(0x40080000)
#define ADDR_IRAM0_SRAM_14	(0x40084000)
#define ADDR_IRAM0_SRAM_15	(0x40088000)
#define ADDR_IRAM0_SRAM_16	(0x4008c000)
#define ADDR_IRAM0_SRAM_17	(0x40090000)
#define ADDR_IRAM0_SRAM_18	(0x40094000)
#define ADDR_IRAM0_SRAM_19	(0x40098000)
#define ADDR_IRAM0_SRAM_20	(0x4009c000)
#define ADDR_IRAM0_SRAM_21	(0x400a0000)
#define ADDR_IRAM0_SRAM_22	(0x400a4000)
#define ADDR_IRAM0_SRAM_23	(0x400a8000)
#define ADDR_IRAM0_SRAM_24	(0x400ac000)
#define ADDR_IRAM0_SRAM_25	(0x400b0000)
#define ADDR_IRAM0_SRAM_26	(0x400b4000)
#define ADDR_IRAM0_SRAM_27	(0x400b8000)
#define ADDR_IRAM0_SRAM_28	(0x400bc000)
#define ADDR_IRAM0_CACHE	(0x400c0000)

#define LEN_IRAM0_ROM		(0x10000)
#define LEN_IRAM0_RTCFAST	(0x2000)
#define LEN_IRAM0_SRAM_0_2	(0x2000)
#define LEN_IRAM0_SRAM_3_28	(0x4000)
#define LEN_IRAM0_CACHE		(0x340000)


#define ADDR_IRAM1_CACHE	(0x40400000)

#define LEN_IRAM1_CACHE		(0x400000)


#define ADDR_IROM0_CACHE	(0x40800000)

#define LEN_IROM0_CACHE		(0x400000)


#define ADDR_DRAM0_ROM_4	(0x3ff80000)
#define ADDR_DRAM0_RTCFAST	(0x3ff90000)
#define ADDR_DRAM0_SRAM_0	(0x3ff92000) 
#define ADDR_DRAM0_SRAM_1	(0x3ff94000) 
#define ADDR_DRAM0_SRAM_2	(0x3ff96000) 
#define ADDR_DRAM0_SRAM_3	(0x3ff98000) 
#define ADDR_DRAM0_SRAM_4	(0x3ff9c000) 
#define ADDR_DRAM0_SRAM_5	(0x3ffa0000) 
#define ADDR_DRAM0_SRAM_6	(0x3ffa4000) 
#define ADDR_DRAM0_SRAM_7	(0x3ffa8000) 
#define ADDR_DRAM0_SRAM_8	(0x3ffac000) 
#define ADDR_DRAM0_SRAM_9	(0x3ffb0000) 
#define ADDR_DRAM0_SRAM_10	(0x3ffb4000) 
#define ADDR_DRAM0_SRAM_11	(0x3ffb8000) 
#define ADDR_DRAM0_SRAM_12	(0x3ffbc000) 
#define ADDR_DRAM0_SRAM_13	(0x3ffc0000) 
#define ADDR_DRAM0_SRAM_14	(0x3ffc4000) 
#define ADDR_DRAM0_SRAM_15	(0x3ffc8000) 
#define ADDR_DRAM0_SRAM_16	(0x3ffcc000) 
#define ADDR_DRAM0_SRAM_17	(0x3ffd0000) 
#define ADDR_DRAM0_SRAM_18	(0x3ffd4000) 
#define ADDR_DRAM0_SRAM_19	(0x3ffd8000) 
#define ADDR_DRAM0_SRAM_20	(0x3ffdc000) 
#define ADDR_DRAM0_SRAM_21	(0x3ffe0000) 
#define ADDR_DRAM0_SRAM_22	(0x3ffe4000) 
#define ADDR_DRAM0_SRAM_23	(0x3ffe8000) 
#define ADDR_DRAM0_SRAM_24	(0x3ffec000) 
#define ADDR_DRAM0_SRAM_25	(0x3fff0000) 
#define ADDR_DRAM0_SRAM_26	(0x3fff4000) 
#define ADDR_DRAM0_SRAM_27	(0x3fff8000) 
#define ADDR_DRAM0_SRAM_28	(0x3fffc000) 

#define LEN_DRAM0_RTCFAST	(0x2000)
#define LEN_DRAM0_SRAM_0_2	(0x2000)
#define LEN_DRAM0_SRAM_3_28	(0x4000)


#define ADDR_DRAM1_CACHE	(0x3f800000)

#define LEN_DRAM1_CACHE		(0x400000)


#define ADDR_DROM0_CACHE	(0x3f400000)

#define LEN_DROM0_CACHE		(0x400000)


#define ADDR_DPORT_CPU		(0x3ff00000)
#define ADDR_DPORT_APB		(0x3ff40000)
#define ADDR_DPORT_RTCSLOW	(0x3ff61000)

#define LEN_DPORT_CPU		(0x400000)
#define LEN_DPORT_APP		(0x400000)
#define LEN_DPORT_RTCSLOW	(0x2000)


#define ADDR_AHB_RTCSLOW_0	(0x50000000)
#define ADDR_AHB_RTCSLOW_1	(0x60021000)

#define LEN_AHB_RTCSLOW		(0x2000)



#define CPU_PERIPHERAL_AES			(0x3ff08000)
#define CPU_PERIPHERAL_SHA			(0x3ff09000)
#define CPU_PERIPHERAL_RSA			(0x3ff0a000)
#define CPU_PERIPHERAL_SECURE_BOOT		(0x3ff0b000)
#define CPU_PERIPHERAL_HMAC			(0x3ff0c000)
#define CPU_PERIPHERAL_DIGITAL_SIGNATURE	(0x3ff0d000)
#define CPU_PERIPHERAL_ASSIST_DEBUG		(0x3ff0e000)
#define CPU_PERIPHERAL_DEDICATED_GPIO		(0x3ff0f000)
#define CPU_PERIPHERAL_INTRUSION		(0x3ff10000)
