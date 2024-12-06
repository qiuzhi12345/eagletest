#define SLP_OE (BIT(0))
#define SLP_SEL (BIT(1))
#define SLP_PD (BIT(2))
#define SLP_PU (BIT(3))
#define SLP_IE (BIT(4))
#define SLP_DRV 0x3
#define SLP_DRV_S 5
#define FUN_PD (BIT(7))
#define FUN_PU (BIT(8))
#define FUN_IE (BIT(9))
#define FUN_DRV 0x3
#define FUN_DRV_S 10
#define MCU_SEL 0x7
#define MCU_SEL_S 12

#define PIN_PULLUP_DIS(PIN_NAME)                 CLEAR_PERI_REG_MASK(PIN_NAME, FUN_PU)
#define PIN_PULLUP_EN(PIN_NAME)                  SET_PERI_REG_MASK(PIN_NAME, FUN_PU)
#define PIN_PULLDWN_DIS(PIN_NAME)             CLEAR_PERI_REG_MASK(PIN_NAME, FUN_PD)
#define PIN_PULLDWN_EN(PIN_NAME)              SET_PERI_REG_MASK(PIN_NAME, FUN_PD)
#define PIN_FUNC_SELECT(PIN_NAME, FUNC)      do { CLEAR_PERI_REG_MASK(PIN_NAME, (MCU_SEL)<<MCU_SEL_S); \
                                                  SET_PERI_REG_MASK  (PIN_NAME, (FUNC)<<MCU_SEL_S); } while(0)

#define PIN_CTRL                          (REG_IO_MUX_BASE +0x00)
#define CLK_OUT3                                    0xf
#define CLK_OUT3_S                                  8
#define CLK_OUT2                                    0xf
#define CLK_OUT2_S                                  4
#define CLK_OUT1                                    0xf
#define CLK_OUT1_S                                  0

#define PERIPHS_IO_MUX_GPIO0_U            (REG_IO_MUX_BASE +0x04)
#define FUNC_GPIO0_GPIO0                            1
#define FUNC_GPIO0_GPIO0_0                          0

#define PERIPHS_IO_MUX_GPIO1_U            (REG_IO_MUX_BASE +0x08)
#define FUNC_GPIO1_GPIO1                            1
#define FUNC_GPIO1_GPIO1_0                          0

#define PERIPHS_IO_MUX_GPIO2_U            (REG_IO_MUX_BASE +0x0c)
#define FUNC_GPIO2_GPIO2                            1
#define FUNC_GPIO2_GPIO2_0                          0

#define PERIPHS_IO_MUX_GPIO3_U            (REG_IO_MUX_BASE +0x10)
#define FUNC_GPIO3_GPIO3                            1
#define FUNC_GPIO3_GPIO3_0                          0

#define PERIPHS_IO_MUX_GPIO4_U            (REG_IO_MUX_BASE +0x14)
#define FUNC_GPIO4_GPIO4                            1
#define FUNC_GPIO4_GPIO4_0                          0

#define PERIPHS_IO_MUX_GPIO5_U            (REG_IO_MUX_BASE +0x18)
#define FUNC_GPIO5_GPIO5                            1
#define FUNC_GPIO5_GPIO5_0                          0

#define PERIPHS_IO_MUX_GPIO6_U            (REG_IO_MUX_BASE +0x1c)
#define FUNC_GPIO6_GPIO6                            1
#define FUNC_GPIO6_GPIO6_0                          0

#define PERIPHS_IO_MUX_GPIO7_U            (REG_IO_MUX_BASE +0x20)
#define FUNC_GPIO7_GPIO7                            1
#define FUNC_GPIO7_GPIO7_0                          0

#define PERIPHS_IO_MUX_GPIO8_U            (REG_IO_MUX_BASE +0x24)
#define FUNC_GPIO8_SUBSPICS1                        3
#define FUNC_GPIO8_GPIO8                            1
#define FUNC_GPIO8_GPIO8_0                          0

#define PERIPHS_IO_MUX_GPIO9_U            (REG_IO_MUX_BASE +0x28)
#define FUNC_GPIO9_SUBSPIHD                         3
#define FUNC_GPIO9_FSPIHD                           2
#define FUNC_GPIO9_GPIO9                            1
#define FUNC_GPIO9_SD_DATA2                         0

#define PERIPHS_IO_MUX_GPIO10_U           (REG_IO_MUX_BASE +0x2c)
#define FUNC_GPIO10_SUBSPICS0                       3
#define FUNC_GPIO10_FSPICS0                         2
#define FUNC_GPIO10_GPIO10                          1
#define FUNC_GPIO10_SD_DATA3                        0

#define PERIPHS_IO_MUX_GPIO11_U           (REG_IO_MUX_BASE +0x30)
#define FUNC_GPIO11_SUBSPID                         3
#define FUNC_GPIO11_FSPID                           2
#define FUNC_GPIO11_GPIO11                          1
#define FUNC_GPIO11_SD_CMD                          0

#define PERIPHS_IO_MUX_GPIO12_U           (REG_IO_MUX_BASE +0x34)
#define FUNC_GPIO12_SUBSPICLK                       3
#define FUNC_GPIO12_FSPICLK                         2
#define FUNC_GPIO12_GPIO12                          1
#define FUNC_GPIO12_SD_CLK                          0

#define PERIPHS_IO_MUX_GPIO13_U           (REG_IO_MUX_BASE +0x38)
#define FUNC_GPIO13_SUBSPIQ                         3
#define FUNC_GPIO13_FSPIQ                           2
#define FUNC_GPIO13_GPIO13                          1
#define FUNC_GPIO13_SD_DATA0                        0

#define PERIPHS_IO_MUX_GPIO14_U           (REG_IO_MUX_BASE +0x3c)
#define FUNC_GPIO14_SUBSPIWP                        3
#define FUNC_GPIO14_FSPIWP                          2
#define FUNC_GPIO14_GPIO14                          1
#define FUNC_GPIO14_SD_DATA1                        0

#define PERIPHS_IO_MUX_XTAL_32K_P_U       (REG_IO_MUX_BASE +0x40)
#define FUNC_XTAL_32K_P_U0RTS                       2
#define FUNC_XTAL_32K_P_GPIO15                      1
#define FUNC_XTAL_32K_P_GPIO15_0                    0

#define PERIPHS_IO_MUX_XTAL_32K_N_U       (REG_IO_MUX_BASE +0x44)
#define FUNC_XTAL_32K_N_U0CTS                       2
#define FUNC_XTAL_32K_N_GPIO16                      1
#define FUNC_XTAL_32K_N_GPIO16_0                    0

#define PERIPHS_IO_MUX_DAC_1_U            (REG_IO_MUX_BASE +0x48)
#define FUNC_DAC_1_U1TXD                            2
#define FUNC_DAC_1_GPIO17                           1
#define FUNC_DAC_1_GPIO17_0                         0

#define PERIPHS_IO_MUX_DAC_2_U            (REG_IO_MUX_BASE +0x4c)
#define FUNC_DAC_2_CLK_OUT3                         3
#define FUNC_DAC_2_U1RXD                            2
#define FUNC_DAC_2_GPIO18                           1
#define FUNC_DAC_2_GPIO18_0                         0

#define PERIPHS_IO_MUX_GPIO19_U           (REG_IO_MUX_BASE +0x50)
#define FUNC_GPIO19_CLK_OUT2                        3
#define FUNC_GPIO19_U1RTS                           2
#define FUNC_GPIO19_GPIO19                          1
#define FUNC_GPIO19_GPIO19_0                        0

#define PERIPHS_IO_MUX_GPIO20_U           (REG_IO_MUX_BASE +0x54)
#define FUNC_GPIO20_CLK_OUT1                        3
#define FUNC_GPIO20_U1CTS                           2
#define FUNC_GPIO20_GPIO20                          1
#define FUNC_GPIO20_GPIO20_0                        0

#define PERIPHS_IO_MUX_GPIO21_U           (REG_IO_MUX_BASE +0x58)
#define FUNC_GPIO21_GPIO21                          1
#define FUNC_GPIO21_GPIO21_0                        0

#define PERIPHS_IO_MUX_SPICS1_U           (REG_IO_MUX_BASE +0x6c)
#define FUNC_SPICS1_GPIO26                          1
#define FUNC_SPICS1_SPICS1                          0

#define PERIPHS_IO_MUX_SPIHD_U            (REG_IO_MUX_BASE +0x70)
#define FUNC_SPIHD_GPIO27                           1
#define FUNC_SPIHD_SPIHD                            0

#define PERIPHS_IO_MUX_SPIWP_U            (REG_IO_MUX_BASE +0x74)
#define FUNC_SPIWP_GPIO28                           1
#define FUNC_SPIWP_SPIWP                            0

#define PERIPHS_IO_MUX_SPICS0_U           (REG_IO_MUX_BASE +0x78)
#define FUNC_SPICS0_GPIO29                          1
#define FUNC_SPICS0_SPICS0                          0

#define PERIPHS_IO_MUX_SPICLK_U           (REG_IO_MUX_BASE +0x7c)
#define FUNC_SPICLK_GPIO30                          1
#define FUNC_SPICLK_SPICLK                          0

#define PERIPHS_IO_MUX_SPIQ_U             (REG_IO_MUX_BASE +0x80)
#define FUNC_SPIQ_GPIO31                            1
#define FUNC_SPIQ_SPIQ                              0

#define PERIPHS_IO_MUX_SPID_U             (REG_IO_MUX_BASE +0x84)
#define FUNC_SPID_GPIO32                            1
#define FUNC_SPID_SPID                              0

#define PERIPHS_IO_MUX_GPIO33_U           (REG_IO_MUX_BASE +0x88)
#define FUNC_GPIO33_SUBSPIHD                        3
#define FUNC_GPIO33_SD_DATA2                        2
#define FUNC_GPIO33_GPIO33                          1
#define FUNC_GPIO33_FSPIHD                          0

#define PERIPHS_IO_MUX_GPIO34_U           (REG_IO_MUX_BASE +0x8c)
#define FUNC_GPIO34_SUBSPICS0                       3
#define FUNC_GPIO34_SD_DATA3                        2
#define FUNC_GPIO34_GPIO34                          1
#define FUNC_GPIO34_FSPICS0                         0

#define PERIPHS_IO_MUX_GPIO35_U           (REG_IO_MUX_BASE +0x90)
#define FUNC_GPIO35_SUBSPID                         3
#define FUNC_GPIO35_SD_CMD                          2
#define FUNC_GPIO35_GPIO35                          1
#define FUNC_GPIO35_FSPID                           0

#define PERIPHS_IO_MUX_GPIO36_U           (REG_IO_MUX_BASE +0x94)
#define FUNC_GPIO36_SUBSPICLK                       3
#define FUNC_GPIO36_SD_CLK                          2
#define FUNC_GPIO36_GPIO36                          1
#define FUNC_GPIO36_FSPICLK                         0

#define PERIPHS_IO_MUX_GPIO37_U           (REG_IO_MUX_BASE +0x98)
#define FUNC_GPIO37_SUBSPIQ                         3
#define FUNC_GPIO37_SD_DATA0                        2
#define FUNC_GPIO37_GPIO37                          1
#define FUNC_GPIO37_FSPIQ                           0

#define PERIPHS_IO_MUX_GPIO38_U           (REG_IO_MUX_BASE +0x9c)
#define FUNC_GPIO38_SUBSPIWP                        3
#define FUNC_GPIO38_SD_DATA1                        2
#define FUNC_GPIO38_GPIO38                          1
#define FUNC_GPIO38_FSPIWP                          0

#define PERIPHS_IO_MUX_MTCK_U             (REG_IO_MUX_BASE +0xa0)
#define FUNC_MTCK_SUBSPICS1                         3
#define FUNC_MTCK_CLK_OUT3                          2
#define FUNC_MTCK_GPIO39                            1
#define FUNC_MTCK_MTCK                              0

#define PERIPHS_IO_MUX_MTDO_U             (REG_IO_MUX_BASE +0xa4)
#define FUNC_MTDO_CLK_OUT2                          2
#define FUNC_MTDO_GPIO40                            1
#define FUNC_MTDO_MTDO                              0

#define PERIPHS_IO_MUX_MTDI_U             (REG_IO_MUX_BASE +0xa8)
#define FUNC_MTDI_CLK_OUT1                          2
#define FUNC_MTDI_GPIO41                            1
#define FUNC_MTDI_MTDI                              0

#define PERIPHS_IO_MUX_MTMS_U             (REG_IO_MUX_BASE +0xac)
#define FUNC_MTMS_GPIO42                            1
#define FUNC_MTMS_MTMS                              0

#define PERIPHS_IO_MUX_U0TXD_U            (REG_IO_MUX_BASE +0xb0)
#define FUNC_U0TXD_CLK_OUT1                         2
#define FUNC_U0TXD_GPIO43                           1
#define FUNC_U0TXD_U0TXD                            0

#define PERIPHS_IO_MUX_U0RXD_U            (REG_IO_MUX_BASE +0xb4)
#define FUNC_U0RXD_CLK_OUT2                         2
#define FUNC_U0RXD_GPIO44                           1
#define FUNC_U0RXD_U0RXD                            0

#define PERIPHS_IO_MUX_GPIO45_U           (REG_IO_MUX_BASE +0xb8)
#define FUNC_GPIO45_GPIO45                          1
#define FUNC_GPIO45_GPIO45_0                        0

#define PERIPHS_IO_MUX_GPIO46_U           (REG_IO_MUX_BASE +0xbc)
#define FUNC_GPIO46_GPIO46                          1
#define FUNC_GPIO46_GPIO46_0                        0

#define IO_MUX_DATE_REG (REG_IO_MUX_BASE + 0xfc)
#define IO_MUX_DATE 0xFFFFFFFF
#define IO_MUX_DATE_S 0
#define IO_MUX_DATE_VERSION 0x1809060
