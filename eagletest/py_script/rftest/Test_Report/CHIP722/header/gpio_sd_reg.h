
#define SIGMADELTA0_REG (REG_GPIO_SD_BASE + 0x0000)
#define SIGMADELTA_SD0_PRESCALE 0x000000FF
#define SIGMADELTA_SD0_PRESCALE_S 8
#define SIGMADELTA_SD0_IN 0x000000FF
#define SIGMADELTA_SD0_IN_S 0

#define SIGMADELTA1_REG (REG_GPIO_SD_BASE + 0x0004)
#define SIGMADELTA_SD1_PRESCALE 0x000000FF
#define SIGMADELTA_SD1_PRESCALE_S 8
#define SIGMADELTA_SD1_IN 0x000000FF
#define SIGMADELTA_SD1_IN_S 0

#define SIGMADELTA2_REG (REG_GPIO_SD_BASE + 0x0008)
#define SIGMADELTA_SD2_PRESCALE 0x000000FF
#define SIGMADELTA_SD2_PRESCALE_S 8
#define SIGMADELTA_SD2_IN 0x000000FF
#define SIGMADELTA_SD2_IN_S 0

#define SIGMADELTA3_REG (REG_GPIO_SD_BASE + 0x000c)
#define SIGMADELTA_SD3_PRESCALE 0x000000FF
#define SIGMADELTA_SD3_PRESCALE_S 8
#define SIGMADELTA_SD3_IN 0x000000FF
#define SIGMADELTA_SD3_IN_S 0

#define SIGMADELTA4_REG (REG_GPIO_SD_BASE + 0x0010)
#define SIGMADELTA_SD4_PRESCALE 0x000000FF
#define SIGMADELTA_SD4_PRESCALE_S 8
#define SIGMADELTA_SD4_IN 0x000000FF
#define SIGMADELTA_SD4_IN_S 0

#define SIGMADELTA5_REG (REG_GPIO_SD_BASE + 0x0014)
#define SIGMADELTA_SD5_PRESCALE 0x000000FF
#define SIGMADELTA_SD5_PRESCALE_S 8
#define SIGMADELTA_SD5_IN 0x000000FF
#define SIGMADELTA_SD5_IN_S 0

#define SIGMADELTA6_REG (REG_GPIO_SD_BASE + 0x0018)
#define SIGMADELTA_SD6_PRESCALE 0x000000FF
#define SIGMADELTA_SD6_PRESCALE_S 8
#define SIGMADELTA_SD6_IN 0x000000FF
#define SIGMADELTA_SD6_IN_S 0

#define SIGMADELTA7_REG (REG_GPIO_SD_BASE + 0x001c)
#define SIGMADELTA_SD7_PRESCALE 0x000000FF
#define SIGMADELTA_SD7_PRESCALE_S 8
#define SIGMADELTA_SD7_IN 0x000000FF
#define SIGMADELTA_SD7_IN_S 0

#define SIGMADELTA_CG_REG (REG_GPIO_SD_BASE + 0x0020)
#define SIGMADELTA_CLK_EN (BIT(31))
#define SIGMADELTA_CLK_EN_S 31

#define SIGMADELTA_MISC_REG (REG_GPIO_SD_BASE + 0x0024)
#define SIGMADELTA_SPI_SWAP (BIT(31))
#define SIGMADELTA_SPI_SWAP_S 31
#define SIGMADELTA_FUNCTION_CLK_EN (BIT(30))
#define SIGMADELTA_FUNCTION_CLK_EN_S 30

#define SIGMADELTA_VERSION_REG (REG_GPIO_SD_BASE + 0x0028)
#define SIGMADELTA_GPIO_SD_DATE 0x0FFFFFFF
#define SIGMADELTA_GPIO_SD_DATE_S 0
#define SIGMADELTA_GPIO_SD_DATE_VERSION 0x1802260
