from hal.common import *
from hal.hwregister.hwreg.ESP32.addr_base import *
class DPORT(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.PRO_BOOT_REMAP_CTRL_REG = PRO_BOOT_REMAP_CTRL_REG(self.channel, self.chipv)
        self.APP_BOOT_REMAP_CTRL_REG = APP_BOOT_REMAP_CTRL_REG(self.channel, self.chipv)
        self.DPORT_ACCESS_CHECK = DPORT_ACCESS_CHECK(self.channel, self.chipv)
        self.PRO_DPORT_APB_MASK0 = PRO_DPORT_APB_MASK0(self.channel, self.chipv)
        self.PRO_DPORT_APB_MASK1 = PRO_DPORT_APB_MASK1(self.channel, self.chipv)
        self.APP_DPORT_APB_MASK0 = APP_DPORT_APB_MASK0(self.channel, self.chipv)
        self.APP_DPORT_APB_MASK1 = APP_DPORT_APB_MASK1(self.channel, self.chipv)
        self.PERI_CLK_EN = PERI_CLK_EN(self.channel, self.chipv)
        self.PERI_RST_EN = PERI_RST_EN(self.channel, self.chipv)
        self.WIFI_BB_CFG = WIFI_BB_CFG(self.channel, self.chipv)
        self.WIFI_BB_CFG_2 = WIFI_BB_CFG_2(self.channel, self.chipv)
        self.APPCPU_CTRL_REG_A = APPCPU_CTRL_REG_A(self.channel, self.chipv)
        self.APPCPU_CTRL_REG_B = APPCPU_CTRL_REG_B(self.channel, self.chipv)
        self.APPCPU_CTRL_REG_C = APPCPU_CTRL_REG_C(self.channel, self.chipv)
        self.APPCPU_CTRL_REG_D = APPCPU_CTRL_REG_D(self.channel, self.chipv)
        self.CPU_PER_CONF_REG = CPU_PER_CONF_REG(self.channel, self.chipv)
        self.PRO_CACHE_CTRL_REG = PRO_CACHE_CTRL_REG(self.channel, self.chipv)
        self.PRO_CACHE_CTRL1_REG = PRO_CACHE_CTRL1_REG(self.channel, self.chipv)
        self.PRO_CACHE_LOCK_0_ADDR_REG = PRO_CACHE_LOCK_0_ADDR_REG(self.channel, self.chipv)
        self.PRO_CACHE_LOCK_1_ADDR_REG = PRO_CACHE_LOCK_1_ADDR_REG(self.channel, self.chipv)
        self.PRO_CACHE_LOCK_2_ADDR_REG = PRO_CACHE_LOCK_2_ADDR_REG(self.channel, self.chipv)
        self.PRO_CACHE_LOCK_3_ADDR_REG = PRO_CACHE_LOCK_3_ADDR_REG(self.channel, self.chipv)
        self.APP_CACHE_CTRL_REG = APP_CACHE_CTRL_REG(self.channel, self.chipv)
        self.APP_CACHE_CTRL1_REG = APP_CACHE_CTRL1_REG(self.channel, self.chipv)
        self.APP_CACHE_LOCK_0_ADDR_REG = APP_CACHE_LOCK_0_ADDR_REG(self.channel, self.chipv)
        self.APP_CACHE_LOCK_1_ADDR_REG = APP_CACHE_LOCK_1_ADDR_REG(self.channel, self.chipv)
        self.APP_CACHE_LOCK_2_ADDR_REG = APP_CACHE_LOCK_2_ADDR_REG(self.channel, self.chipv)
        self.APP_CACHE_LOCK_3_ADDR_REG = APP_CACHE_LOCK_3_ADDR_REG(self.channel, self.chipv)
        self.TRACEMEM_MUX_MODE = TRACEMEM_MUX_MODE(self.channel, self.chipv)
        self.PRO_TRACEMEM_ENA = PRO_TRACEMEM_ENA(self.channel, self.chipv)
        self.APP_TRACEMEM_ENA = APP_TRACEMEM_ENA(self.channel, self.chipv)
        self.CACHE_MUX_MODE = CACHE_MUX_MODE(self.channel, self.chipv)
        self.IMMU_PAGE_MODE = IMMU_PAGE_MODE(self.channel, self.chipv)
        self.DMMU_PAGE_MODE = DMMU_PAGE_MODE(self.channel, self.chipv)
        self.ROM_MPU_ENA = ROM_MPU_ENA(self.channel, self.chipv)
        self.MEM_PD_MASK_REG = MEM_PD_MASK_REG(self.channel, self.chipv)
        self.ROM_PD_CTRL_REG = ROM_PD_CTRL_REG(self.channel, self.chipv)
        self.ROM_FO_CTRL_REG = ROM_FO_CTRL_REG(self.channel, self.chipv)
        self.SRAM_PD_CTRL_REG_0 = SRAM_PD_CTRL_REG_0(self.channel, self.chipv)
        self.SRAM_PD_CTRL_REG_1 = SRAM_PD_CTRL_REG_1(self.channel, self.chipv)
        self.SRAM_FO_CTRL_REG_0 = SRAM_FO_CTRL_REG_0(self.channel, self.chipv)
        self.SRAM_FO_CTRL_REG_1 = SRAM_FO_CTRL_REG_1(self.channel, self.chipv)
        self.IRAM_DRAM_AHB_SEL = IRAM_DRAM_AHB_SEL(self.channel, self.chipv)
        self.TAG_FO_CTRL_REG = TAG_FO_CTRL_REG(self.channel, self.chipv)
        self.AHB_LITE_MASK_REG = AHB_LITE_MASK_REG(self.channel, self.chipv)
        self.AHB_MPU_TABLE_0 = AHB_MPU_TABLE_0(self.channel, self.chipv)
        self.AHB_MPU_TABLE_1 = AHB_MPU_TABLE_1(self.channel, self.chipv)
        self.HOST_INF_SEL = HOST_INF_SEL(self.channel, self.chipv)
        self.PERIP_CLK_EN = PERIP_CLK_EN(self.channel, self.chipv)
        self.PERIP_RST_EN = PERIP_RST_EN(self.channel, self.chipv)
        self.SLAVE_SPI_CONFIG_REG = SLAVE_SPI_CONFIG_REG(self.channel, self.chipv)
        self.WIFI_CLK_EN = WIFI_CLK_EN(self.channel, self.chipv)
        self.WIFI_RST_EN = WIFI_RST_EN(self.channel, self.chipv)
        self.BT_LPCK_DIV_INT = BT_LPCK_DIV_INT(self.channel, self.chipv)
        self.BT_LPCK_DIV_FRAC = BT_LPCK_DIV_FRAC(self.channel, self.chipv)
        self.CPU_INTR_FROM_CPU_0_REG = CPU_INTR_FROM_CPU_0_REG(self.channel, self.chipv)
        self.CPU_INTR_FROM_CPU_1_REG = CPU_INTR_FROM_CPU_1_REG(self.channel, self.chipv)
        self.CPU_INTR_FROM_CPU_2_REG = CPU_INTR_FROM_CPU_2_REG(self.channel, self.chipv)
        self.CPU_INTR_FROM_CPU_3_REG = CPU_INTR_FROM_CPU_3_REG(self.channel, self.chipv)
        self.PRO_INTR_STATUS_REG_0 = PRO_INTR_STATUS_REG_0(self.channel, self.chipv)
        self.PRO_INTR_STATUS_REG_1 = PRO_INTR_STATUS_REG_1(self.channel, self.chipv)
        self.PRO_INTR_STATUS_REG_2 = PRO_INTR_STATUS_REG_2(self.channel, self.chipv)
        self.APP_INTR_STATUS_REG_0 = APP_INTR_STATUS_REG_0(self.channel, self.chipv)
        self.APP_INTR_STATUS_REG_1 = APP_INTR_STATUS_REG_1(self.channel, self.chipv)
        self.APP_INTR_STATUS_REG_2 = APP_INTR_STATUS_REG_2(self.channel, self.chipv)
        self.PRO_MAC_INTR_MAP_REG = PRO_MAC_INTR_MAP_REG(self.channel, self.chipv)
        self.PRO_MAC_NMI_MAP_REG = PRO_MAC_NMI_MAP_REG(self.channel, self.chipv)
        self.PRO_BB_INT_MAP_REG = PRO_BB_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_BT_MAC_INT_MAP_REG = PRO_BT_MAC_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_BT_BB_INT_MAP_REG = PRO_BT_BB_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_BT_BB_NMI_MAP_REG = PRO_BT_BB_NMI_MAP_REG(self.channel, self.chipv)
        self.PRO_RWBT_IRQ_MAP_REG = PRO_RWBT_IRQ_MAP_REG(self.channel, self.chipv)
        self.PRO_RWBLE_IRQ_MAP_REG = PRO_RWBLE_IRQ_MAP_REG(self.channel, self.chipv)
        self.PRO_RWBT_NMI_MAP_REG = PRO_RWBT_NMI_MAP_REG(self.channel, self.chipv)
        self.PRO_RWBLE_NMI_MAP_REG = PRO_RWBLE_NMI_MAP_REG(self.channel, self.chipv)
        self.PRO_SLC0_INTR_MAP_REG = PRO_SLC0_INTR_MAP_REG(self.channel, self.chipv)
        self.PRO_SLC1_INTR_MAP_REG = PRO_SLC1_INTR_MAP_REG(self.channel, self.chipv)
        self.PRO_UHCI0_INTR_MAP_REG = PRO_UHCI0_INTR_MAP_REG(self.channel, self.chipv)
        self.PRO_UHCI1_INTR_MAP_REG = PRO_UHCI1_INTR_MAP_REG(self.channel, self.chipv)
        self.PRO_TG_T0_LEVEL_INT_MAP_REG = PRO_TG_T0_LEVEL_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_TG_T1_LEVEL_INT_MAP_REG = PRO_TG_T1_LEVEL_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_TG_WDT_LEVEL_INT_MAP_REG = PRO_TG_WDT_LEVEL_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_TG_LACT_LEVEL_INT_MAP_REG = PRO_TG_LACT_LEVEL_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_TG1_T0_LEVEL_INT_MAP_REG = PRO_TG1_T0_LEVEL_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_TG1_T1_LEVEL_INT_MAP_REG = PRO_TG1_T1_LEVEL_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_TG1_WDT_LEVEL_INT_MAP_REG = PRO_TG1_WDT_LEVEL_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_TG1_LACT_LEVEL_INT_MAP_REG = PRO_TG1_LACT_LEVEL_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_GPIO_INTERRUPT_MAP_REG = PRO_GPIO_INTERRUPT_MAP_REG(self.channel, self.chipv)
        self.PRO_GPIO_INTERRUPT_NMI_MAP_REG = PRO_GPIO_INTERRUPT_NMI_MAP_REG(self.channel, self.chipv)
        self.PRO_CPU_INTR_FROM_CPU_0_MAP_REG = PRO_CPU_INTR_FROM_CPU_0_MAP_REG(self.channel, self.chipv)
        self.PRO_CPU_INTR_FROM_CPU_1_MAP_REG = PRO_CPU_INTR_FROM_CPU_1_MAP_REG(self.channel, self.chipv)
        self.PRO_CPU_INTR_FROM_CPU_2_MAP_REG = PRO_CPU_INTR_FROM_CPU_2_MAP_REG(self.channel, self.chipv)
        self.PRO_CPU_INTR_FROM_CPU_3_MAP_REG = PRO_CPU_INTR_FROM_CPU_3_MAP_REG(self.channel, self.chipv)
        self.PRO_SPI_INTR_0_MAP_REG = PRO_SPI_INTR_0_MAP_REG(self.channel, self.chipv)
        self.PRO_SPI_INTR_1_MAP_REG = PRO_SPI_INTR_1_MAP_REG(self.channel, self.chipv)
        self.PRO_SPI_INTR_2_MAP_REG = PRO_SPI_INTR_2_MAP_REG(self.channel, self.chipv)
        self.PRO_SPI_INTR_3_MAP_REG = PRO_SPI_INTR_3_MAP_REG(self.channel, self.chipv)
        self.PRO_I2S0_INT_MAP_REG = PRO_I2S0_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_I2S1_INT_MAP_REG = PRO_I2S1_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_UART_INTR_MAP_REG = PRO_UART_INTR_MAP_REG(self.channel, self.chipv)
        self.PRO_UART1_INTR_MAP_REG = PRO_UART1_INTR_MAP_REG(self.channel, self.chipv)
        self.PRO_UART2_INTR_MAP_REG = PRO_UART2_INTR_MAP_REG(self.channel, self.chipv)
        self.PRO_SDIO_HOST_INTERRUPT_MAP_REG = PRO_SDIO_HOST_INTERRUPT_MAP_REG(self.channel, self.chipv)
        self.PRO_EMAC_INT_MAP_REG = PRO_EMAC_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_PWM0_INTR_MAP_REG = PRO_PWM0_INTR_MAP_REG(self.channel, self.chipv)
        self.PRO_PWM1_INTR_MAP_REG = PRO_PWM1_INTR_MAP_REG(self.channel, self.chipv)
        self.PRO_PWM2_INTR_MAP_REG = PRO_PWM2_INTR_MAP_REG(self.channel, self.chipv)
        self.PRO_PWM3_INTR_MAP_REG = PRO_PWM3_INTR_MAP_REG(self.channel, self.chipv)
        self.PRO_LEDC_INT_MAP_REG = PRO_LEDC_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_EFUSE_INT_MAP_REG = PRO_EFUSE_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_CAN_INT_MAP_REG = PRO_CAN_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_RTC_CORE_INTR_MAP_REG = PRO_RTC_CORE_INTR_MAP_REG(self.channel, self.chipv)
        self.PRO_RMT_INTR_MAP_REG = PRO_RMT_INTR_MAP_REG(self.channel, self.chipv)
        self.PRO_PCNT_INTR_MAP_REG = PRO_PCNT_INTR_MAP_REG(self.channel, self.chipv)
        self.PRO_I2C_EXT0_INTR_MAP_REG = PRO_I2C_EXT0_INTR_MAP_REG(self.channel, self.chipv)
        self.PRO_I2C_EXT1_INTR_MAP_REG = PRO_I2C_EXT1_INTR_MAP_REG(self.channel, self.chipv)
        self.PRO_RSA_INTR_MAP_REG = PRO_RSA_INTR_MAP_REG(self.channel, self.chipv)
        self.PRO_SPI1_DMA_INT_MAP_REG = PRO_SPI1_DMA_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_SPI2_DMA_INT_MAP_REG = PRO_SPI2_DMA_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_SPI3_DMA_INT_MAP_REG = PRO_SPI3_DMA_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_WDG_INT_MAP_REG = PRO_WDG_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_TIMER_INT1_MAP_REG = PRO_TIMER_INT1_MAP_REG(self.channel, self.chipv)
        self.PRO_TIMER_INT2_MAP_REG = PRO_TIMER_INT2_MAP_REG(self.channel, self.chipv)
        self.PRO_TG_T0_EDGE_INT_MAP_REG = PRO_TG_T0_EDGE_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_TG_T1_EDGE_INT_MAP_REG = PRO_TG_T1_EDGE_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_TG_WDT_EDGE_INT_MAP_REG = PRO_TG_WDT_EDGE_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_TG_LACT_EDGE_INT_MAP_REG = PRO_TG_LACT_EDGE_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_TG1_T0_EDGE_INT_MAP_REG = PRO_TG1_T0_EDGE_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_TG1_T1_EDGE_INT_MAP_REG = PRO_TG1_T1_EDGE_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_TG1_WDT_EDGE_INT_MAP_REG = PRO_TG1_WDT_EDGE_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_TG1_LACT_EDGE_INT_MAP_REG = PRO_TG1_LACT_EDGE_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_MMU_IA_INT_MAP_REG = PRO_MMU_IA_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_MPU_IA_INT_MAP_REG = PRO_MPU_IA_INT_MAP_REG(self.channel, self.chipv)
        self.PRO_CACHE_IA_INT_MAP_REG = PRO_CACHE_IA_INT_MAP_REG(self.channel, self.chipv)
        self.APP_MAC_INTR_MAP_REG = APP_MAC_INTR_MAP_REG(self.channel, self.chipv)
        self.APP_MAC_NMI_MAP_REG = APP_MAC_NMI_MAP_REG(self.channel, self.chipv)
        self.APP_BB_INT_MAP_REG = APP_BB_INT_MAP_REG(self.channel, self.chipv)
        self.APP_BT_MAC_INT_MAP_REG = APP_BT_MAC_INT_MAP_REG(self.channel, self.chipv)
        self.APP_BT_BB_INT_MAP_REG = APP_BT_BB_INT_MAP_REG(self.channel, self.chipv)
        self.APP_BT_BB_NMI_MAP_REG = APP_BT_BB_NMI_MAP_REG(self.channel, self.chipv)
        self.APP_RWBT_IRQ_MAP_REG = APP_RWBT_IRQ_MAP_REG(self.channel, self.chipv)
        self.APP_RWBLE_IRQ_MAP_REG = APP_RWBLE_IRQ_MAP_REG(self.channel, self.chipv)
        self.APP_RWBT_NMI_MAP_REG = APP_RWBT_NMI_MAP_REG(self.channel, self.chipv)
        self.APP_RWBLE_NMI_MAP_REG = APP_RWBLE_NMI_MAP_REG(self.channel, self.chipv)
        self.APP_SLC0_INTR_MAP_REG = APP_SLC0_INTR_MAP_REG(self.channel, self.chipv)
        self.APP_SLC1_INTR_MAP_REG = APP_SLC1_INTR_MAP_REG(self.channel, self.chipv)
        self.APP_UHCI0_INTR_MAP_REG = APP_UHCI0_INTR_MAP_REG(self.channel, self.chipv)
        self.APP_UHCI1_INTR_MAP_REG = APP_UHCI1_INTR_MAP_REG(self.channel, self.chipv)
        self.APP_TG_T0_LEVEL_INT_MAP_REG = APP_TG_T0_LEVEL_INT_MAP_REG(self.channel, self.chipv)
        self.APP_TG_T1_LEVEL_INT_MAP_REG = APP_TG_T1_LEVEL_INT_MAP_REG(self.channel, self.chipv)
        self.APP_TG_WDT_LEVEL_INT_MAP_REG = APP_TG_WDT_LEVEL_INT_MAP_REG(self.channel, self.chipv)
        self.APP_TG_LACT_LEVEL_INT_MAP_REG = APP_TG_LACT_LEVEL_INT_MAP_REG(self.channel, self.chipv)
        self.APP_TG1_T0_LEVEL_INT_MAP_REG = APP_TG1_T0_LEVEL_INT_MAP_REG(self.channel, self.chipv)
        self.APP_TG1_T1_LEVEL_INT_MAP_REG = APP_TG1_T1_LEVEL_INT_MAP_REG(self.channel, self.chipv)
        self.APP_TG1_WDT_LEVEL_INT_MAP_REG = APP_TG1_WDT_LEVEL_INT_MAP_REG(self.channel, self.chipv)
        self.APP_TG1_LACT_LEVEL_INT_MAP_REG = APP_TG1_LACT_LEVEL_INT_MAP_REG(self.channel, self.chipv)
        self.APP_GPIO_INTERRUPT_MAP_REG = APP_GPIO_INTERRUPT_MAP_REG(self.channel, self.chipv)
        self.APP_GPIO_INTERRUPT_NMI_MAP_REG = APP_GPIO_INTERRUPT_NMI_MAP_REG(self.channel, self.chipv)
        self.APP_CPU_INTR_FROM_CPU_0_MAP_REG = APP_CPU_INTR_FROM_CPU_0_MAP_REG(self.channel, self.chipv)
        self.APP_CPU_INTR_FROM_CPU_1_MAP_REG = APP_CPU_INTR_FROM_CPU_1_MAP_REG(self.channel, self.chipv)
        self.APP_CPU_INTR_FROM_CPU_2_MAP_REG = APP_CPU_INTR_FROM_CPU_2_MAP_REG(self.channel, self.chipv)
        self.APP_CPU_INTR_FROM_CPU_3_MAP_REG = APP_CPU_INTR_FROM_CPU_3_MAP_REG(self.channel, self.chipv)
        self.APP_SPI_INTR_0_MAP_REG = APP_SPI_INTR_0_MAP_REG(self.channel, self.chipv)
        self.APP_SPI_INTR_1_MAP_REG = APP_SPI_INTR_1_MAP_REG(self.channel, self.chipv)
        self.APP_SPI_INTR_2_MAP_REG = APP_SPI_INTR_2_MAP_REG(self.channel, self.chipv)
        self.APP_SPI_INTR_3_MAP_REG = APP_SPI_INTR_3_MAP_REG(self.channel, self.chipv)
        self.APP_I2S0_INT_MAP_REG = APP_I2S0_INT_MAP_REG(self.channel, self.chipv)
        self.APP_I2S1_INT_MAP_REG = APP_I2S1_INT_MAP_REG(self.channel, self.chipv)
        self.APP_UART_INTR_MAP_REG = APP_UART_INTR_MAP_REG(self.channel, self.chipv)
        self.APP_UART1_INTR_MAP_REG = APP_UART1_INTR_MAP_REG(self.channel, self.chipv)
        self.APP_UART2_INTR_MAP_REG = APP_UART2_INTR_MAP_REG(self.channel, self.chipv)
        self.APP_SDIO_HOST_INTERRUPT_MAP_REG = APP_SDIO_HOST_INTERRUPT_MAP_REG(self.channel, self.chipv)
        self.APP_EMAC_INT_MAP_REG = APP_EMAC_INT_MAP_REG(self.channel, self.chipv)
        self.APP_PWM0_INTR_MAP_REG = APP_PWM0_INTR_MAP_REG(self.channel, self.chipv)
        self.APP_PWM1_INTR_MAP_REG = APP_PWM1_INTR_MAP_REG(self.channel, self.chipv)
        self.APP_PWM2_INTR_MAP_REG = APP_PWM2_INTR_MAP_REG(self.channel, self.chipv)
        self.APP_PWM3_INTR_MAP_REG = APP_PWM3_INTR_MAP_REG(self.channel, self.chipv)
        self.APP_LEDC_INT_MAP_REG = APP_LEDC_INT_MAP_REG(self.channel, self.chipv)
        self.APP_EFUSE_INT_MAP_REG = APP_EFUSE_INT_MAP_REG(self.channel, self.chipv)
        self.APP_CAN_INT_MAP_REG = APP_CAN_INT_MAP_REG(self.channel, self.chipv)
        self.APP_RTC_CORE_INTR_MAP_REG = APP_RTC_CORE_INTR_MAP_REG(self.channel, self.chipv)
        self.APP_RMT_INTR_MAP_REG = APP_RMT_INTR_MAP_REG(self.channel, self.chipv)
        self.APP_PCNT_INTR_MAP_REG = APP_PCNT_INTR_MAP_REG(self.channel, self.chipv)
        self.APP_I2C_EXT0_INTR_MAP_REG = APP_I2C_EXT0_INTR_MAP_REG(self.channel, self.chipv)
        self.APP_I2C_EXT1_INTR_MAP_REG = APP_I2C_EXT1_INTR_MAP_REG(self.channel, self.chipv)
        self.APP_RSA_INTR_MAP_REG = APP_RSA_INTR_MAP_REG(self.channel, self.chipv)
        self.APP_SPI1_DMA_INT_MAP_REG = APP_SPI1_DMA_INT_MAP_REG(self.channel, self.chipv)
        self.APP_SPI2_DMA_INT_MAP_REG = APP_SPI2_DMA_INT_MAP_REG(self.channel, self.chipv)
        self.APP_SPI3_DMA_INT_MAP_REG = APP_SPI3_DMA_INT_MAP_REG(self.channel, self.chipv)
        self.APP_WDG_INT_MAP_REG = APP_WDG_INT_MAP_REG(self.channel, self.chipv)
        self.APP_TIMER_INT1_MAP_REG = APP_TIMER_INT1_MAP_REG(self.channel, self.chipv)
        self.APP_TIMER_INT2_MAP_REG = APP_TIMER_INT2_MAP_REG(self.channel, self.chipv)
        self.APP_TG_T0_EDGE_INT_MAP_REG = APP_TG_T0_EDGE_INT_MAP_REG(self.channel, self.chipv)
        self.APP_TG_T1_EDGE_INT_MAP_REG = APP_TG_T1_EDGE_INT_MAP_REG(self.channel, self.chipv)
        self.APP_TG_WDT_EDGE_INT_MAP_REG = APP_TG_WDT_EDGE_INT_MAP_REG(self.channel, self.chipv)
        self.APP_TG_LACT_EDGE_INT_MAP_REG = APP_TG_LACT_EDGE_INT_MAP_REG(self.channel, self.chipv)
        self.APP_TG1_T0_EDGE_INT_MAP_REG = APP_TG1_T0_EDGE_INT_MAP_REG(self.channel, self.chipv)
        self.APP_TG1_T1_EDGE_INT_MAP_REG = APP_TG1_T1_EDGE_INT_MAP_REG(self.channel, self.chipv)
        self.APP_TG1_WDT_EDGE_INT_MAP_REG = APP_TG1_WDT_EDGE_INT_MAP_REG(self.channel, self.chipv)
        self.APP_TG1_LACT_EDGE_INT_MAP_REG = APP_TG1_LACT_EDGE_INT_MAP_REG(self.channel, self.chipv)
        self.APP_MMU_IA_INT_MAP_REG = APP_MMU_IA_INT_MAP_REG(self.channel, self.chipv)
        self.APP_MPU_IA_INT_MAP_REG = APP_MPU_IA_INT_MAP_REG(self.channel, self.chipv)
        self.APP_CACHE_IA_INT_MAP_REG = APP_CACHE_IA_INT_MAP_REG(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_UART = AHBLITE_MPU_TABLE_UART(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_SPI1 = AHBLITE_MPU_TABLE_SPI1(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_SPI0 = AHBLITE_MPU_TABLE_SPI0(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_GPIO = AHBLITE_MPU_TABLE_GPIO(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_FE2 = AHBLITE_MPU_TABLE_FE2(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_FE = AHBLITE_MPU_TABLE_FE(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_TIMER = AHBLITE_MPU_TABLE_TIMER(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_RTC = AHBLITE_MPU_TABLE_RTC(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_IO_MUX = AHBLITE_MPU_TABLE_IO_MUX(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_WDG = AHBLITE_MPU_TABLE_WDG(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_HINF = AHBLITE_MPU_TABLE_HINF(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_UHCI1 = AHBLITE_MPU_TABLE_UHCI1(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_MISC = AHBLITE_MPU_TABLE_MISC(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_I2C = AHBLITE_MPU_TABLE_I2C(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_I2S0 = AHBLITE_MPU_TABLE_I2S0(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_UART1 = AHBLITE_MPU_TABLE_UART1(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_BT = AHBLITE_MPU_TABLE_BT(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_BT_BUFFER = AHBLITE_MPU_TABLE_BT_BUFFER(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_I2C_EXT0 = AHBLITE_MPU_TABLE_I2C_EXT0(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_UHCI0 = AHBLITE_MPU_TABLE_UHCI0(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_SLCHOST = AHBLITE_MPU_TABLE_SLCHOST(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_RMT = AHBLITE_MPU_TABLE_RMT(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_PCNT = AHBLITE_MPU_TABLE_PCNT(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_SLC = AHBLITE_MPU_TABLE_SLC(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_LEDC = AHBLITE_MPU_TABLE_LEDC(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_EFUSE = AHBLITE_MPU_TABLE_EFUSE(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_SPI_ENCRYPT = AHBLITE_MPU_TABLE_SPI_ENCRYPT(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_BB = AHBLITE_MPU_TABLE_BB(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_PWM0 = AHBLITE_MPU_TABLE_PWM0(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_TIMERGROUP = AHBLITE_MPU_TABLE_TIMERGROUP(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_TIMERGROUP1 = AHBLITE_MPU_TABLE_TIMERGROUP1(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_SPI2 = AHBLITE_MPU_TABLE_SPI2(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_SPI3 = AHBLITE_MPU_TABLE_SPI3(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_APB_CTRL = AHBLITE_MPU_TABLE_APB_CTRL(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_I2C_EXT1 = AHBLITE_MPU_TABLE_I2C_EXT1(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_SDIO_HOST = AHBLITE_MPU_TABLE_SDIO_HOST(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_EMAC = AHBLITE_MPU_TABLE_EMAC(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_CAN = AHBLITE_MPU_TABLE_CAN(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_PWM1 = AHBLITE_MPU_TABLE_PWM1(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_I2S1 = AHBLITE_MPU_TABLE_I2S1(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_UART2 = AHBLITE_MPU_TABLE_UART2(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_PWM2 = AHBLITE_MPU_TABLE_PWM2(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_PWM3 = AHBLITE_MPU_TABLE_PWM3(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_RWBT = AHBLITE_MPU_TABLE_RWBT(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_BTMAC = AHBLITE_MPU_TABLE_BTMAC(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_WIFIMAC = AHBLITE_MPU_TABLE_WIFIMAC(self.channel, self.chipv)
        self.AHBLITE_MPU_TABLE_PWR = AHBLITE_MPU_TABLE_PWR(self.channel, self.chipv)
        self.MEM_ACCESS_DBUG0 = MEM_ACCESS_DBUG0(self.channel, self.chipv)
        self.MEM_ACCESS_DBUG1 = MEM_ACCESS_DBUG1(self.channel, self.chipv)
        self.PRO_DCACHE_DBUG_REG0 = PRO_DCACHE_DBUG_REG0(self.channel, self.chipv)
        self.PRO_DCACHE_DBUG_REG1 = PRO_DCACHE_DBUG_REG1(self.channel, self.chipv)
        self.PRO_DCACHE_DBUG_REG2 = PRO_DCACHE_DBUG_REG2(self.channel, self.chipv)
        self.PRO_DCACHE_DBUG_REG3 = PRO_DCACHE_DBUG_REG3(self.channel, self.chipv)
        self.PRO_DCACHE_DBUG_REG4 = PRO_DCACHE_DBUG_REG4(self.channel, self.chipv)
        self.PRO_DCACHE_DBUG_REG5 = PRO_DCACHE_DBUG_REG5(self.channel, self.chipv)
        self.PRO_DCACHE_DBUG_REG6 = PRO_DCACHE_DBUG_REG6(self.channel, self.chipv)
        self.PRO_DCACHE_DBUG_REG7 = PRO_DCACHE_DBUG_REG7(self.channel, self.chipv)
        self.PRO_DCACHE_DBUG_REG8 = PRO_DCACHE_DBUG_REG8(self.channel, self.chipv)
        self.PRO_DCACHE_DBUG_REG9 = PRO_DCACHE_DBUG_REG9(self.channel, self.chipv)
        self.APP_DCACHE_DBUG_REG0 = APP_DCACHE_DBUG_REG0(self.channel, self.chipv)
        self.APP_DCACHE_DBUG_REG1 = APP_DCACHE_DBUG_REG1(self.channel, self.chipv)
        self.APP_DCACHE_DBUG_REG2 = APP_DCACHE_DBUG_REG2(self.channel, self.chipv)
        self.APP_DCACHE_DBUG_REG3 = APP_DCACHE_DBUG_REG3(self.channel, self.chipv)
        self.APP_DCACHE_DBUG_REG4 = APP_DCACHE_DBUG_REG4(self.channel, self.chipv)
        self.APP_DCACHE_DBUG_REG5 = APP_DCACHE_DBUG_REG5(self.channel, self.chipv)
        self.APP_DCACHE_DBUG_REG6 = APP_DCACHE_DBUG_REG6(self.channel, self.chipv)
        self.APP_DCACHE_DBUG_REG7 = APP_DCACHE_DBUG_REG7(self.channel, self.chipv)
        self.APP_DCACHE_DBUG_REG8 = APP_DCACHE_DBUG_REG8(self.channel, self.chipv)
        self.APP_DCACHE_DBUG_REG9 = APP_DCACHE_DBUG_REG9(self.channel, self.chipv)
        self.PRO_CPU_RECORD_CTRL = PRO_CPU_RECORD_CTRL(self.channel, self.chipv)
        self.PRO_CPU_RECORD_STATUS = PRO_CPU_RECORD_STATUS(self.channel, self.chipv)
        self.PRO_CPU_RECORD_PID = PRO_CPU_RECORD_PID(self.channel, self.chipv)
        self.PRO_CPU_RECORD_PDEBUGINST = PRO_CPU_RECORD_PDEBUGINST(self.channel, self.chipv)
        self.PRO_CPU_RECORD_PDEBUGSTATUS = PRO_CPU_RECORD_PDEBUGSTATUS(self.channel, self.chipv)
        self.PRO_CPU_RECORD_PDEBUGDATA = PRO_CPU_RECORD_PDEBUGDATA(self.channel, self.chipv)
        self.PRO_CPU_RECORD_PDEBUGPC = PRO_CPU_RECORD_PDEBUGPC(self.channel, self.chipv)
        self.PRO_CPU_RECORD_PDEBUGLS0STAT = PRO_CPU_RECORD_PDEBUGLS0STAT(self.channel, self.chipv)
        self.PRO_CPU_RECORD_PDEBUGLS0ADDR = PRO_CPU_RECORD_PDEBUGLS0ADDR(self.channel, self.chipv)
        self.PRO_CPU_RECORD_PDEBUGLS0DATA = PRO_CPU_RECORD_PDEBUGLS0DATA(self.channel, self.chipv)
        self.APP_CPU_RECORD_CTRL = APP_CPU_RECORD_CTRL(self.channel, self.chipv)
        self.APP_CPU_RECORD_STATUS = APP_CPU_RECORD_STATUS(self.channel, self.chipv)
        self.APP_CPU_RECORD_PID = APP_CPU_RECORD_PID(self.channel, self.chipv)
        self.APP_CPU_RECORD_PDEBUGINST = APP_CPU_RECORD_PDEBUGINST(self.channel, self.chipv)
        self.APP_CPU_RECORD_PDEBUGSTATUS = APP_CPU_RECORD_PDEBUGSTATUS(self.channel, self.chipv)
        self.APP_CPU_RECORD_PDEBUGDATA = APP_CPU_RECORD_PDEBUGDATA(self.channel, self.chipv)
        self.APP_CPU_RECORD_PDEBUGPC = APP_CPU_RECORD_PDEBUGPC(self.channel, self.chipv)
        self.APP_CPU_RECORD_PDEBUGLS0STAT = APP_CPU_RECORD_PDEBUGLS0STAT(self.channel, self.chipv)
        self.APP_CPU_RECORD_PDEBUGLS0ADDR = APP_CPU_RECORD_PDEBUGLS0ADDR(self.channel, self.chipv)
        self.APP_CPU_RECORD_PDEBUGLS0DATA = APP_CPU_RECORD_PDEBUGLS0DATA(self.channel, self.chipv)
        self.RSA_PD_CTRL_REG = RSA_PD_CTRL_REG(self.channel, self.chipv)
        self.ROM_MPU_TABLE0 = ROM_MPU_TABLE0(self.channel, self.chipv)
        self.ROM_MPU_TABLE1 = ROM_MPU_TABLE1(self.channel, self.chipv)
        self.ROM_MPU_TABLE2 = ROM_MPU_TABLE2(self.channel, self.chipv)
        self.ROM_MPU_TABLE3 = ROM_MPU_TABLE3(self.channel, self.chipv)
        self.SHROM_MPU_TABLE0 = SHROM_MPU_TABLE0(self.channel, self.chipv)
        self.SHROM_MPU_TABLE1 = SHROM_MPU_TABLE1(self.channel, self.chipv)
        self.SHROM_MPU_TABLE2 = SHROM_MPU_TABLE2(self.channel, self.chipv)
        self.SHROM_MPU_TABLE3 = SHROM_MPU_TABLE3(self.channel, self.chipv)
        self.SHROM_MPU_TABLE4 = SHROM_MPU_TABLE4(self.channel, self.chipv)
        self.SHROM_MPU_TABLE5 = SHROM_MPU_TABLE5(self.channel, self.chipv)
        self.SHROM_MPU_TABLE6 = SHROM_MPU_TABLE6(self.channel, self.chipv)
        self.SHROM_MPU_TABLE7 = SHROM_MPU_TABLE7(self.channel, self.chipv)
        self.SHROM_MPU_TABLE8 = SHROM_MPU_TABLE8(self.channel, self.chipv)
        self.SHROM_MPU_TABLE9 = SHROM_MPU_TABLE9(self.channel, self.chipv)
        self.SHROM_MPU_TABLE10 = SHROM_MPU_TABLE10(self.channel, self.chipv)
        self.SHROM_MPU_TABLE11 = SHROM_MPU_TABLE11(self.channel, self.chipv)
        self.SHROM_MPU_TABLE12 = SHROM_MPU_TABLE12(self.channel, self.chipv)
        self.SHROM_MPU_TABLE13 = SHROM_MPU_TABLE13(self.channel, self.chipv)
        self.SHROM_MPU_TABLE14 = SHROM_MPU_TABLE14(self.channel, self.chipv)
        self.SHROM_MPU_TABLE15 = SHROM_MPU_TABLE15(self.channel, self.chipv)
        self.SHROM_MPU_TABLE16 = SHROM_MPU_TABLE16(self.channel, self.chipv)
        self.SHROM_MPU_TABLE17 = SHROM_MPU_TABLE17(self.channel, self.chipv)
        self.SHROM_MPU_TABLE18 = SHROM_MPU_TABLE18(self.channel, self.chipv)
        self.SHROM_MPU_TABLE19 = SHROM_MPU_TABLE19(self.channel, self.chipv)
        self.SHROM_MPU_TABLE20 = SHROM_MPU_TABLE20(self.channel, self.chipv)
        self.SHROM_MPU_TABLE21 = SHROM_MPU_TABLE21(self.channel, self.chipv)
        self.SHROM_MPU_TABLE22 = SHROM_MPU_TABLE22(self.channel, self.chipv)
        self.SHROM_MPU_TABLE23 = SHROM_MPU_TABLE23(self.channel, self.chipv)
        self.IMMU_TABLE0 = IMMU_TABLE0(self.channel, self.chipv)
        self.IMMU_TABLE1 = IMMU_TABLE1(self.channel, self.chipv)
        self.IMMU_TABLE2 = IMMU_TABLE2(self.channel, self.chipv)
        self.IMMU_TABLE3 = IMMU_TABLE3(self.channel, self.chipv)
        self.IMMU_TABLE4 = IMMU_TABLE4(self.channel, self.chipv)
        self.IMMU_TABLE5 = IMMU_TABLE5(self.channel, self.chipv)
        self.IMMU_TABLE6 = IMMU_TABLE6(self.channel, self.chipv)
        self.IMMU_TABLE7 = IMMU_TABLE7(self.channel, self.chipv)
        self.IMMU_TABLE8 = IMMU_TABLE8(self.channel, self.chipv)
        self.IMMU_TABLE9 = IMMU_TABLE9(self.channel, self.chipv)
        self.IMMU_TABLE10 = IMMU_TABLE10(self.channel, self.chipv)
        self.IMMU_TABLE11 = IMMU_TABLE11(self.channel, self.chipv)
        self.IMMU_TABLE12 = IMMU_TABLE12(self.channel, self.chipv)
        self.IMMU_TABLE13 = IMMU_TABLE13(self.channel, self.chipv)
        self.IMMU_TABLE14 = IMMU_TABLE14(self.channel, self.chipv)
        self.IMMU_TABLE15 = IMMU_TABLE15(self.channel, self.chipv)
        self.DMMU_TABLE0 = DMMU_TABLE0(self.channel, self.chipv)
        self.DMMU_TABLE1 = DMMU_TABLE1(self.channel, self.chipv)
        self.DMMU_TABLE2 = DMMU_TABLE2(self.channel, self.chipv)
        self.DMMU_TABLE3 = DMMU_TABLE3(self.channel, self.chipv)
        self.DMMU_TABLE4 = DMMU_TABLE4(self.channel, self.chipv)
        self.DMMU_TABLE5 = DMMU_TABLE5(self.channel, self.chipv)
        self.DMMU_TABLE6 = DMMU_TABLE6(self.channel, self.chipv)
        self.DMMU_TABLE7 = DMMU_TABLE7(self.channel, self.chipv)
        self.DMMU_TABLE8 = DMMU_TABLE8(self.channel, self.chipv)
        self.DMMU_TABLE9 = DMMU_TABLE9(self.channel, self.chipv)
        self.DMMU_TABLE10 = DMMU_TABLE10(self.channel, self.chipv)
        self.DMMU_TABLE11 = DMMU_TABLE11(self.channel, self.chipv)
        self.DMMU_TABLE12 = DMMU_TABLE12(self.channel, self.chipv)
        self.DMMU_TABLE13 = DMMU_TABLE13(self.channel, self.chipv)
        self.DMMU_TABLE14 = DMMU_TABLE14(self.channel, self.chipv)
        self.DMMU_TABLE15 = DMMU_TABLE15(self.channel, self.chipv)
        self.PRO_INTRUSION_CTRL = PRO_INTRUSION_CTRL(self.channel, self.chipv)
        self.PRO_INTRUSION_STATUS = PRO_INTRUSION_STATUS(self.channel, self.chipv)
        self.APP_INTRUSION_CTRL = APP_INTRUSION_CTRL(self.channel, self.chipv)
        self.APP_INTRUSION_STATUS = APP_INTRUSION_STATUS(self.channel, self.chipv)
        self.FRONT_END_MEM_PD = FRONT_END_MEM_PD(self.channel, self.chipv)
        self.MMU_IA_INT_EN = MMU_IA_INT_EN(self.channel, self.chipv)
        self.MPU_IA_INT_EN = MPU_IA_INT_EN(self.channel, self.chipv)
        self.CACHE_IA_INT_EN = CACHE_IA_INT_EN(self.channel, self.chipv)
        self.SECURE_BOOT_CTRL = SECURE_BOOT_CTRL(self.channel, self.chipv)
        self.SPI_DMA_CHAN_SEL = SPI_DMA_CHAN_SEL(self.channel, self.chipv)
        self.PRO_VECBASE_CTRL = PRO_VECBASE_CTRL(self.channel, self.chipv)
        self.PRO_VECBASE_SET = PRO_VECBASE_SET(self.channel, self.chipv)
        self.APP_VECBASE_CTRL = APP_VECBASE_CTRL(self.channel, self.chipv)
        self.APP_VECBASE_SET = APP_VECBASE_SET(self.channel, self.chipv)
        self.DPORT_REG_DATE = DPORT_REG_DATE(self.channel, self.chipv)
class PRO_BOOT_REMAP_CTRL_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x0
        self.__pro_boot_remap_lsb = 0
        self.__pro_boot_remap_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_boot_remap(self):
        return self.__MEM.rdm(self.__addr, self.__pro_boot_remap_msb, self.__pro_boot_remap_lsb)
    @pro_boot_remap.setter
    def pro_boot_remap(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_boot_remap_msb, self.__pro_boot_remap_lsb, value)
class APP_BOOT_REMAP_CTRL_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x4
        self.__app_boot_remap_lsb = 0
        self.__app_boot_remap_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_boot_remap(self):
        return self.__MEM.rdm(self.__addr, self.__app_boot_remap_msb, self.__app_boot_remap_lsb)
    @app_boot_remap.setter
    def app_boot_remap(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_boot_remap_msb, self.__app_boot_remap_lsb, value)
class DPORT_ACCESS_CHECK(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x8
        self.__dport_access_check_app_lsb = 8
        self.__dport_access_check_app_msb = 8
        self.__dport_access_check_pro_lsb = 0
        self.__dport_access_check_pro_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def dport_access_check_app(self):
        return self.__MEM.rdm(self.__addr, self.__dport_access_check_app_msb, self.__dport_access_check_app_lsb)
    @dport_access_check_app.setter
    def dport_access_check_app(self, value):
        return self.__MEM.wrm(self.__addr, self.__dport_access_check_app_msb, self.__dport_access_check_app_lsb, value)

    @property
    def dport_access_check_pro(self):
        return self.__MEM.rdm(self.__addr, self.__dport_access_check_pro_msb, self.__dport_access_check_pro_lsb)
    @dport_access_check_pro.setter
    def dport_access_check_pro(self, value):
        return self.__MEM.wrm(self.__addr, self.__dport_access_check_pro_msb, self.__dport_access_check_pro_lsb, value)
class PRO_DPORT_APB_MASK0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0xc
        self.__reg_prodport_apb_mask0_lsb = 0
        self.__reg_prodport_apb_mask0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_prodport_apb_mask0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_prodport_apb_mask0_msb, self.__reg_prodport_apb_mask0_lsb)
    @reg_prodport_apb_mask0.setter
    def reg_prodport_apb_mask0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_prodport_apb_mask0_msb, self.__reg_prodport_apb_mask0_lsb, value)
class PRO_DPORT_APB_MASK1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x10
        self.__reg_prodport_apb_mask1_lsb = 0
        self.__reg_prodport_apb_mask1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_prodport_apb_mask1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_prodport_apb_mask1_msb, self.__reg_prodport_apb_mask1_lsb)
    @reg_prodport_apb_mask1.setter
    def reg_prodport_apb_mask1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_prodport_apb_mask1_msb, self.__reg_prodport_apb_mask1_lsb, value)
class APP_DPORT_APB_MASK0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x14
        self.__reg_appdport_apb_mask0_lsb = 0
        self.__reg_appdport_apb_mask0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_appdport_apb_mask0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_appdport_apb_mask0_msb, self.__reg_appdport_apb_mask0_lsb)
    @reg_appdport_apb_mask0.setter
    def reg_appdport_apb_mask0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_appdport_apb_mask0_msb, self.__reg_appdport_apb_mask0_lsb, value)
class APP_DPORT_APB_MASK1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x18
        self.__reg_appdport_apb_mask1_lsb = 0
        self.__reg_appdport_apb_mask1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_appdport_apb_mask1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_appdport_apb_mask1_msb, self.__reg_appdport_apb_mask1_lsb)
    @reg_appdport_apb_mask1.setter
    def reg_appdport_apb_mask1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_appdport_apb_mask1_msb, self.__reg_appdport_apb_mask1_lsb, value)
class PERI_CLK_EN(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x1c
        self.__peri_clk_en_lsb = 0
        self.__peri_clk_en_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def peri_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__peri_clk_en_msb, self.__peri_clk_en_lsb)
    @peri_clk_en.setter
    def peri_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__peri_clk_en_msb, self.__peri_clk_en_lsb, value)
class PERI_RST_EN(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x20
        self.__peri_rst_en_lsb = 0
        self.__peri_rst_en_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def peri_rst_en(self):
        return self.__MEM.rdm(self.__addr, self.__peri_rst_en_msb, self.__peri_rst_en_lsb)
    @peri_rst_en.setter
    def peri_rst_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__peri_rst_en_msb, self.__peri_rst_en_lsb, value)
class WIFI_BB_CFG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x24
        self.__reg_wifi_bb_cfg_lsb = 0
        self.__reg_wifi_bb_cfg_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wifi_bb_cfg(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wifi_bb_cfg_msb, self.__reg_wifi_bb_cfg_lsb)
    @reg_wifi_bb_cfg.setter
    def reg_wifi_bb_cfg(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wifi_bb_cfg_msb, self.__reg_wifi_bb_cfg_lsb, value)
class WIFI_BB_CFG_2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x28
        self.__reg_wifi_bb_cfg_2_lsb = 0
        self.__reg_wifi_bb_cfg_2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wifi_bb_cfg_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wifi_bb_cfg_2_msb, self.__reg_wifi_bb_cfg_2_lsb)
    @reg_wifi_bb_cfg_2.setter
    def reg_wifi_bb_cfg_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wifi_bb_cfg_2_msb, self.__reg_wifi_bb_cfg_2_lsb, value)
class APPCPU_CTRL_REG_A(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x2c
        self.__reg_appcpu_resetting_lsb = 0
        self.__reg_appcpu_resetting_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_appcpu_resetting(self):
        return self.__MEM.rdm(self.__addr, self.__reg_appcpu_resetting_msb, self.__reg_appcpu_resetting_lsb)
    @reg_appcpu_resetting.setter
    def reg_appcpu_resetting(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_appcpu_resetting_msb, self.__reg_appcpu_resetting_lsb, value)
class APPCPU_CTRL_REG_B(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x30
        self.__reg_appcpu_clkgate_en_lsb = 0
        self.__reg_appcpu_clkgate_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_appcpu_clkgate_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_appcpu_clkgate_en_msb, self.__reg_appcpu_clkgate_en_lsb)
    @reg_appcpu_clkgate_en.setter
    def reg_appcpu_clkgate_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_appcpu_clkgate_en_msb, self.__reg_appcpu_clkgate_en_lsb, value)
class APPCPU_CTRL_REG_C(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x34
        self.__reg_appcpu_runstall_lsb = 0
        self.__reg_appcpu_runstall_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_appcpu_runstall(self):
        return self.__MEM.rdm(self.__addr, self.__reg_appcpu_runstall_msb, self.__reg_appcpu_runstall_lsb)
    @reg_appcpu_runstall.setter
    def reg_appcpu_runstall(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_appcpu_runstall_msb, self.__reg_appcpu_runstall_lsb, value)
class APPCPU_CTRL_REG_D(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x38
        self.__reg_appcpu_boot_addr_lsb = 0
        self.__reg_appcpu_boot_addr_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_appcpu_boot_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_appcpu_boot_addr_msb, self.__reg_appcpu_boot_addr_lsb)
    @reg_appcpu_boot_addr.setter
    def reg_appcpu_boot_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_appcpu_boot_addr_msb, self.__reg_appcpu_boot_addr_lsb, value)
class CPU_PER_CONF_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x3c
        self.__reg_fast_clk_rtc_sel_lsb = 3
        self.__reg_fast_clk_rtc_sel_msb = 3
        self.__reg_lowspeed_clk_sel_lsb = 2
        self.__reg_lowspeed_clk_sel_msb = 2
        self.__reg_cpuperiod_sel_lsb = 0
        self.__reg_cpuperiod_sel_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_fast_clk_rtc_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fast_clk_rtc_sel_msb, self.__reg_fast_clk_rtc_sel_lsb)
    @reg_fast_clk_rtc_sel.setter
    def reg_fast_clk_rtc_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fast_clk_rtc_sel_msb, self.__reg_fast_clk_rtc_sel_lsb, value)

    @property
    def reg_lowspeed_clk_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lowspeed_clk_sel_msb, self.__reg_lowspeed_clk_sel_lsb)
    @reg_lowspeed_clk_sel.setter
    def reg_lowspeed_clk_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lowspeed_clk_sel_msb, self.__reg_lowspeed_clk_sel_lsb, value)

    @property
    def reg_cpuperiod_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cpuperiod_sel_msb, self.__reg_cpuperiod_sel_lsb)
    @reg_cpuperiod_sel.setter
    def reg_cpuperiod_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cpuperiod_sel_msb, self.__reg_cpuperiod_sel_lsb, value)
class PRO_CACHE_CTRL_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x40
        self.__pro_dram_hl_lsb = 16
        self.__pro_dram_hl_msb = 16
        self.__slave_req_lsb = 15
        self.__slave_req_msb = 15
        self.__ahb_spi_req_lsb = 14
        self.__ahb_spi_req_msb = 14
        self.__pro_slave_req_lsb = 13
        self.__pro_slave_req_msb = 13
        self.__pro_ahb_spi_req_lsb = 12
        self.__pro_ahb_spi_req_msb = 12
        self.__pro_dram_split_lsb = 11
        self.__pro_dram_split_msb = 11
        self.__pro_single_iram_ena_lsb = 10
        self.__pro_single_iram_ena_msb = 10
        self.__pro_cache_lock_3_en_lsb = 9
        self.__pro_cache_lock_3_en_msb = 9
        self.__pro_cache_lock_2_en_lsb = 8
        self.__pro_cache_lock_2_en_msb = 8
        self.__pro_cache_lock_1_en_lsb = 7
        self.__pro_cache_lock_1_en_msb = 7
        self.__pro_cache_lock_0_en_lsb = 6
        self.__pro_cache_lock_0_en_msb = 6
        self.__pro_cache_flush_done_lsb = 5
        self.__pro_cache_flush_done_msb = 5
        self.__pro_cache_flush_ena_lsb = 4
        self.__pro_cache_flush_ena_msb = 4
        self.__pro_cache_enable_lsb = 3
        self.__pro_cache_enable_msb = 3
        self.__pro_cache_mode_lsb = 2
        self.__pro_cache_mode_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_dram_hl(self):
        return self.__MEM.rdm(self.__addr, self.__pro_dram_hl_msb, self.__pro_dram_hl_lsb)
    @pro_dram_hl.setter
    def pro_dram_hl(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_dram_hl_msb, self.__pro_dram_hl_lsb, value)

    @property
    def slave_req(self):
        return self.__MEM.rdm(self.__addr, self.__slave_req_msb, self.__slave_req_lsb)
    @slave_req.setter
    def slave_req(self, value):
        return self.__MEM.wrm(self.__addr, self.__slave_req_msb, self.__slave_req_lsb, value)

    @property
    def ahb_spi_req(self):
        return self.__MEM.rdm(self.__addr, self.__ahb_spi_req_msb, self.__ahb_spi_req_lsb)
    @ahb_spi_req.setter
    def ahb_spi_req(self, value):
        return self.__MEM.wrm(self.__addr, self.__ahb_spi_req_msb, self.__ahb_spi_req_lsb, value)

    @property
    def pro_slave_req(self):
        return self.__MEM.rdm(self.__addr, self.__pro_slave_req_msb, self.__pro_slave_req_lsb)
    @pro_slave_req.setter
    def pro_slave_req(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_slave_req_msb, self.__pro_slave_req_lsb, value)

    @property
    def pro_ahb_spi_req(self):
        return self.__MEM.rdm(self.__addr, self.__pro_ahb_spi_req_msb, self.__pro_ahb_spi_req_lsb)
    @pro_ahb_spi_req.setter
    def pro_ahb_spi_req(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_ahb_spi_req_msb, self.__pro_ahb_spi_req_lsb, value)

    @property
    def pro_dram_split(self):
        return self.__MEM.rdm(self.__addr, self.__pro_dram_split_msb, self.__pro_dram_split_lsb)
    @pro_dram_split.setter
    def pro_dram_split(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_dram_split_msb, self.__pro_dram_split_lsb, value)

    @property
    def pro_single_iram_ena(self):
        return self.__MEM.rdm(self.__addr, self.__pro_single_iram_ena_msb, self.__pro_single_iram_ena_lsb)
    @pro_single_iram_ena.setter
    def pro_single_iram_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_single_iram_ena_msb, self.__pro_single_iram_ena_lsb, value)

    @property
    def pro_cache_lock_3_en(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_lock_3_en_msb, self.__pro_cache_lock_3_en_lsb)
    @pro_cache_lock_3_en.setter
    def pro_cache_lock_3_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_lock_3_en_msb, self.__pro_cache_lock_3_en_lsb, value)

    @property
    def pro_cache_lock_2_en(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_lock_2_en_msb, self.__pro_cache_lock_2_en_lsb)
    @pro_cache_lock_2_en.setter
    def pro_cache_lock_2_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_lock_2_en_msb, self.__pro_cache_lock_2_en_lsb, value)

    @property
    def pro_cache_lock_1_en(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_lock_1_en_msb, self.__pro_cache_lock_1_en_lsb)
    @pro_cache_lock_1_en.setter
    def pro_cache_lock_1_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_lock_1_en_msb, self.__pro_cache_lock_1_en_lsb, value)

    @property
    def pro_cache_lock_0_en(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_lock_0_en_msb, self.__pro_cache_lock_0_en_lsb)
    @pro_cache_lock_0_en.setter
    def pro_cache_lock_0_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_lock_0_en_msb, self.__pro_cache_lock_0_en_lsb, value)

    @property
    def pro_cache_flush_done(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_flush_done_msb, self.__pro_cache_flush_done_lsb)
    @pro_cache_flush_done.setter
    def pro_cache_flush_done(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_flush_done_msb, self.__pro_cache_flush_done_lsb, value)

    @property
    def pro_cache_flush_ena(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_flush_ena_msb, self.__pro_cache_flush_ena_lsb)
    @pro_cache_flush_ena.setter
    def pro_cache_flush_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_flush_ena_msb, self.__pro_cache_flush_ena_lsb, value)

    @property
    def pro_cache_enable(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_enable_msb, self.__pro_cache_enable_lsb)
    @pro_cache_enable.setter
    def pro_cache_enable(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_enable_msb, self.__pro_cache_enable_lsb, value)

    @property
    def pro_cache_mode(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_mode_msb, self.__pro_cache_mode_lsb)
    @pro_cache_mode.setter
    def pro_cache_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_mode_msb, self.__pro_cache_mode_lsb, value)
class PRO_CACHE_CTRL1_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x44
        self.__pro_cache_mmu_ia_clr_lsb = 13
        self.__pro_cache_mmu_ia_clr_msb = 13
        self.__pro_cmmu_pd_lsb = 12
        self.__pro_cmmu_pd_msb = 12
        self.__pro_cmmu_force_on_lsb = 11
        self.__pro_cmmu_force_on_msb = 11
        self.__pro_cmmu_flash_page_mode_lsb = 9
        self.__pro_cmmu_flash_page_mode_msb = 10
        self.__pro_cmmu_sram_page_mode_lsb = 6
        self.__pro_cmmu_sram_page_mode_msb = 8
        self.__pro_cache_mask_opsdram_lsb = 5
        self.__pro_cache_mask_opsdram_msb = 5
        self.__pro_cache_mask_drom0_lsb = 4
        self.__pro_cache_mask_drom0_msb = 4
        self.__pro_cache_mask_dram1_lsb = 3
        self.__pro_cache_mask_dram1_msb = 3
        self.__pro_cache_mask_irom0_lsb = 2
        self.__pro_cache_mask_irom0_msb = 2
        self.__pro_cache_mask_iram1_lsb = 1
        self.__pro_cache_mask_iram1_msb = 1
        self.__pro_cache_mask_iram0_lsb = 0
        self.__pro_cache_mask_iram0_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_cache_mmu_ia_clr(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_mmu_ia_clr_msb, self.__pro_cache_mmu_ia_clr_lsb)
    @pro_cache_mmu_ia_clr.setter
    def pro_cache_mmu_ia_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_mmu_ia_clr_msb, self.__pro_cache_mmu_ia_clr_lsb, value)

    @property
    def pro_cmmu_pd(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cmmu_pd_msb, self.__pro_cmmu_pd_lsb)
    @pro_cmmu_pd.setter
    def pro_cmmu_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cmmu_pd_msb, self.__pro_cmmu_pd_lsb, value)

    @property
    def pro_cmmu_force_on(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cmmu_force_on_msb, self.__pro_cmmu_force_on_lsb)
    @pro_cmmu_force_on.setter
    def pro_cmmu_force_on(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cmmu_force_on_msb, self.__pro_cmmu_force_on_lsb, value)

    @property
    def pro_cmmu_flash_page_mode(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cmmu_flash_page_mode_msb, self.__pro_cmmu_flash_page_mode_lsb)
    @pro_cmmu_flash_page_mode.setter
    def pro_cmmu_flash_page_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cmmu_flash_page_mode_msb, self.__pro_cmmu_flash_page_mode_lsb, value)

    @property
    def pro_cmmu_sram_page_mode(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cmmu_sram_page_mode_msb, self.__pro_cmmu_sram_page_mode_lsb)
    @pro_cmmu_sram_page_mode.setter
    def pro_cmmu_sram_page_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cmmu_sram_page_mode_msb, self.__pro_cmmu_sram_page_mode_lsb, value)

    @property
    def pro_cache_mask_opsdram(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_mask_opsdram_msb, self.__pro_cache_mask_opsdram_lsb)
    @pro_cache_mask_opsdram.setter
    def pro_cache_mask_opsdram(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_mask_opsdram_msb, self.__pro_cache_mask_opsdram_lsb, value)

    @property
    def pro_cache_mask_drom0(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_mask_drom0_msb, self.__pro_cache_mask_drom0_lsb)
    @pro_cache_mask_drom0.setter
    def pro_cache_mask_drom0(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_mask_drom0_msb, self.__pro_cache_mask_drom0_lsb, value)

    @property
    def pro_cache_mask_dram1(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_mask_dram1_msb, self.__pro_cache_mask_dram1_lsb)
    @pro_cache_mask_dram1.setter
    def pro_cache_mask_dram1(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_mask_dram1_msb, self.__pro_cache_mask_dram1_lsb, value)

    @property
    def pro_cache_mask_irom0(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_mask_irom0_msb, self.__pro_cache_mask_irom0_lsb)
    @pro_cache_mask_irom0.setter
    def pro_cache_mask_irom0(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_mask_irom0_msb, self.__pro_cache_mask_irom0_lsb, value)

    @property
    def pro_cache_mask_iram1(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_mask_iram1_msb, self.__pro_cache_mask_iram1_lsb)
    @pro_cache_mask_iram1.setter
    def pro_cache_mask_iram1(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_mask_iram1_msb, self.__pro_cache_mask_iram1_lsb, value)

    @property
    def pro_cache_mask_iram0(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_mask_iram0_msb, self.__pro_cache_mask_iram0_lsb)
    @pro_cache_mask_iram0.setter
    def pro_cache_mask_iram0(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_mask_iram0_msb, self.__pro_cache_mask_iram0_lsb, value)
class PRO_CACHE_LOCK_0_ADDR_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x48
        self.__pro_cache_lock_0_addr_max_lsb = 18
        self.__pro_cache_lock_0_addr_max_msb = 21
        self.__pro_cache_lock_0_addr_min_lsb = 14
        self.__pro_cache_lock_0_addr_min_msb = 17
        self.__pro_cache_lock_0_addr_pre_lsb = 0
        self.__pro_cache_lock_0_addr_pre_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_cache_lock_0_addr_max(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_lock_0_addr_max_msb, self.__pro_cache_lock_0_addr_max_lsb)
    @pro_cache_lock_0_addr_max.setter
    def pro_cache_lock_0_addr_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_lock_0_addr_max_msb, self.__pro_cache_lock_0_addr_max_lsb, value)

    @property
    def pro_cache_lock_0_addr_min(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_lock_0_addr_min_msb, self.__pro_cache_lock_0_addr_min_lsb)
    @pro_cache_lock_0_addr_min.setter
    def pro_cache_lock_0_addr_min(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_lock_0_addr_min_msb, self.__pro_cache_lock_0_addr_min_lsb, value)

    @property
    def pro_cache_lock_0_addr_pre(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_lock_0_addr_pre_msb, self.__pro_cache_lock_0_addr_pre_lsb)
    @pro_cache_lock_0_addr_pre.setter
    def pro_cache_lock_0_addr_pre(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_lock_0_addr_pre_msb, self.__pro_cache_lock_0_addr_pre_lsb, value)
class PRO_CACHE_LOCK_1_ADDR_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x4c
        self.__pro_cache_lock_1_addr_max_lsb = 18
        self.__pro_cache_lock_1_addr_max_msb = 21
        self.__pro_cache_lock_1_addr_min_lsb = 14
        self.__pro_cache_lock_1_addr_min_msb = 17
        self.__pro_cache_lock_1_addr_pre_lsb = 0
        self.__pro_cache_lock_1_addr_pre_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_cache_lock_1_addr_max(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_lock_1_addr_max_msb, self.__pro_cache_lock_1_addr_max_lsb)
    @pro_cache_lock_1_addr_max.setter
    def pro_cache_lock_1_addr_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_lock_1_addr_max_msb, self.__pro_cache_lock_1_addr_max_lsb, value)

    @property
    def pro_cache_lock_1_addr_min(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_lock_1_addr_min_msb, self.__pro_cache_lock_1_addr_min_lsb)
    @pro_cache_lock_1_addr_min.setter
    def pro_cache_lock_1_addr_min(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_lock_1_addr_min_msb, self.__pro_cache_lock_1_addr_min_lsb, value)

    @property
    def pro_cache_lock_1_addr_pre(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_lock_1_addr_pre_msb, self.__pro_cache_lock_1_addr_pre_lsb)
    @pro_cache_lock_1_addr_pre.setter
    def pro_cache_lock_1_addr_pre(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_lock_1_addr_pre_msb, self.__pro_cache_lock_1_addr_pre_lsb, value)
class PRO_CACHE_LOCK_2_ADDR_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x50
        self.__pro_cache_lock_2_addr_max_lsb = 18
        self.__pro_cache_lock_2_addr_max_msb = 21
        self.__pro_cache_lock_2_addr_min_lsb = 14
        self.__pro_cache_lock_2_addr_min_msb = 17
        self.__pro_cache_lock_2_addr_pre_lsb = 0
        self.__pro_cache_lock_2_addr_pre_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_cache_lock_2_addr_max(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_lock_2_addr_max_msb, self.__pro_cache_lock_2_addr_max_lsb)
    @pro_cache_lock_2_addr_max.setter
    def pro_cache_lock_2_addr_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_lock_2_addr_max_msb, self.__pro_cache_lock_2_addr_max_lsb, value)

    @property
    def pro_cache_lock_2_addr_min(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_lock_2_addr_min_msb, self.__pro_cache_lock_2_addr_min_lsb)
    @pro_cache_lock_2_addr_min.setter
    def pro_cache_lock_2_addr_min(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_lock_2_addr_min_msb, self.__pro_cache_lock_2_addr_min_lsb, value)

    @property
    def pro_cache_lock_2_addr_pre(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_lock_2_addr_pre_msb, self.__pro_cache_lock_2_addr_pre_lsb)
    @pro_cache_lock_2_addr_pre.setter
    def pro_cache_lock_2_addr_pre(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_lock_2_addr_pre_msb, self.__pro_cache_lock_2_addr_pre_lsb, value)
class PRO_CACHE_LOCK_3_ADDR_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x54
        self.__pro_cache_lock_3_addr_max_lsb = 18
        self.__pro_cache_lock_3_addr_max_msb = 21
        self.__pro_cache_lock_3_addr_min_lsb = 14
        self.__pro_cache_lock_3_addr_min_msb = 17
        self.__pro_cache_lock_3_addr_pre_lsb = 0
        self.__pro_cache_lock_3_addr_pre_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_cache_lock_3_addr_max(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_lock_3_addr_max_msb, self.__pro_cache_lock_3_addr_max_lsb)
    @pro_cache_lock_3_addr_max.setter
    def pro_cache_lock_3_addr_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_lock_3_addr_max_msb, self.__pro_cache_lock_3_addr_max_lsb, value)

    @property
    def pro_cache_lock_3_addr_min(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_lock_3_addr_min_msb, self.__pro_cache_lock_3_addr_min_lsb)
    @pro_cache_lock_3_addr_min.setter
    def pro_cache_lock_3_addr_min(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_lock_3_addr_min_msb, self.__pro_cache_lock_3_addr_min_lsb, value)

    @property
    def pro_cache_lock_3_addr_pre(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_lock_3_addr_pre_msb, self.__pro_cache_lock_3_addr_pre_lsb)
    @pro_cache_lock_3_addr_pre.setter
    def pro_cache_lock_3_addr_pre(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_lock_3_addr_pre_msb, self.__pro_cache_lock_3_addr_pre_lsb, value)
class APP_CACHE_CTRL_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x58
        self.__app_dram_hl_lsb = 14
        self.__app_dram_hl_msb = 14
        self.__app_slave_req_lsb = 13
        self.__app_slave_req_msb = 13
        self.__app_ahb_spi_req_lsb = 12
        self.__app_ahb_spi_req_msb = 12
        self.__app_dram_split_lsb = 11
        self.__app_dram_split_msb = 11
        self.__app_single_iram_ena_lsb = 10
        self.__app_single_iram_ena_msb = 10
        self.__app_cache_lock_3_en_lsb = 9
        self.__app_cache_lock_3_en_msb = 9
        self.__app_cache_lock_2_en_lsb = 8
        self.__app_cache_lock_2_en_msb = 8
        self.__app_cache_lock_1_en_lsb = 7
        self.__app_cache_lock_1_en_msb = 7
        self.__app_cache_lock_0_en_lsb = 6
        self.__app_cache_lock_0_en_msb = 6
        self.__app_cache_flush_done_lsb = 5
        self.__app_cache_flush_done_msb = 5
        self.__app_cache_flush_ena_lsb = 4
        self.__app_cache_flush_ena_msb = 4
        self.__app_cache_enable_lsb = 3
        self.__app_cache_enable_msb = 3
        self.__app_cache_mode_lsb = 2
        self.__app_cache_mode_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_dram_hl(self):
        return self.__MEM.rdm(self.__addr, self.__app_dram_hl_msb, self.__app_dram_hl_lsb)
    @app_dram_hl.setter
    def app_dram_hl(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_dram_hl_msb, self.__app_dram_hl_lsb, value)

    @property
    def app_slave_req(self):
        return self.__MEM.rdm(self.__addr, self.__app_slave_req_msb, self.__app_slave_req_lsb)
    @app_slave_req.setter
    def app_slave_req(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_slave_req_msb, self.__app_slave_req_lsb, value)

    @property
    def app_ahb_spi_req(self):
        return self.__MEM.rdm(self.__addr, self.__app_ahb_spi_req_msb, self.__app_ahb_spi_req_lsb)
    @app_ahb_spi_req.setter
    def app_ahb_spi_req(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_ahb_spi_req_msb, self.__app_ahb_spi_req_lsb, value)

    @property
    def app_dram_split(self):
        return self.__MEM.rdm(self.__addr, self.__app_dram_split_msb, self.__app_dram_split_lsb)
    @app_dram_split.setter
    def app_dram_split(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_dram_split_msb, self.__app_dram_split_lsb, value)

    @property
    def app_single_iram_ena(self):
        return self.__MEM.rdm(self.__addr, self.__app_single_iram_ena_msb, self.__app_single_iram_ena_lsb)
    @app_single_iram_ena.setter
    def app_single_iram_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_single_iram_ena_msb, self.__app_single_iram_ena_lsb, value)

    @property
    def app_cache_lock_3_en(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_lock_3_en_msb, self.__app_cache_lock_3_en_lsb)
    @app_cache_lock_3_en.setter
    def app_cache_lock_3_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_lock_3_en_msb, self.__app_cache_lock_3_en_lsb, value)

    @property
    def app_cache_lock_2_en(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_lock_2_en_msb, self.__app_cache_lock_2_en_lsb)
    @app_cache_lock_2_en.setter
    def app_cache_lock_2_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_lock_2_en_msb, self.__app_cache_lock_2_en_lsb, value)

    @property
    def app_cache_lock_1_en(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_lock_1_en_msb, self.__app_cache_lock_1_en_lsb)
    @app_cache_lock_1_en.setter
    def app_cache_lock_1_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_lock_1_en_msb, self.__app_cache_lock_1_en_lsb, value)

    @property
    def app_cache_lock_0_en(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_lock_0_en_msb, self.__app_cache_lock_0_en_lsb)
    @app_cache_lock_0_en.setter
    def app_cache_lock_0_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_lock_0_en_msb, self.__app_cache_lock_0_en_lsb, value)

    @property
    def app_cache_flush_done(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_flush_done_msb, self.__app_cache_flush_done_lsb)
    @app_cache_flush_done.setter
    def app_cache_flush_done(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_flush_done_msb, self.__app_cache_flush_done_lsb, value)

    @property
    def app_cache_flush_ena(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_flush_ena_msb, self.__app_cache_flush_ena_lsb)
    @app_cache_flush_ena.setter
    def app_cache_flush_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_flush_ena_msb, self.__app_cache_flush_ena_lsb, value)

    @property
    def app_cache_enable(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_enable_msb, self.__app_cache_enable_lsb)
    @app_cache_enable.setter
    def app_cache_enable(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_enable_msb, self.__app_cache_enable_lsb, value)

    @property
    def app_cache_mode(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_mode_msb, self.__app_cache_mode_lsb)
    @app_cache_mode.setter
    def app_cache_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_mode_msb, self.__app_cache_mode_lsb, value)
class APP_CACHE_CTRL1_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x5c
        self.__app_cache_mmu_ia_clr_lsb = 13
        self.__app_cache_mmu_ia_clr_msb = 13
        self.__app_cmmu_pd_lsb = 12
        self.__app_cmmu_pd_msb = 12
        self.__app_cmmu_force_on_lsb = 11
        self.__app_cmmu_force_on_msb = 11
        self.__app_cmmu_flash_page_mode_lsb = 9
        self.__app_cmmu_flash_page_mode_msb = 10
        self.__app_cmmu_sram_page_mode_lsb = 6
        self.__app_cmmu_sram_page_mode_msb = 8
        self.__app_cache_mask_opsdram_lsb = 5
        self.__app_cache_mask_opsdram_msb = 5
        self.__app_cache_mask_drom0_lsb = 4
        self.__app_cache_mask_drom0_msb = 4
        self.__app_cache_mask_dram1_lsb = 3
        self.__app_cache_mask_dram1_msb = 3
        self.__app_cache_mask_irom0_lsb = 2
        self.__app_cache_mask_irom0_msb = 2
        self.__app_cache_mask_iram1_lsb = 1
        self.__app_cache_mask_iram1_msb = 1
        self.__app_cache_mask_iram0_lsb = 0
        self.__app_cache_mask_iram0_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_cache_mmu_ia_clr(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_mmu_ia_clr_msb, self.__app_cache_mmu_ia_clr_lsb)
    @app_cache_mmu_ia_clr.setter
    def app_cache_mmu_ia_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_mmu_ia_clr_msb, self.__app_cache_mmu_ia_clr_lsb, value)

    @property
    def app_cmmu_pd(self):
        return self.__MEM.rdm(self.__addr, self.__app_cmmu_pd_msb, self.__app_cmmu_pd_lsb)
    @app_cmmu_pd.setter
    def app_cmmu_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cmmu_pd_msb, self.__app_cmmu_pd_lsb, value)

    @property
    def app_cmmu_force_on(self):
        return self.__MEM.rdm(self.__addr, self.__app_cmmu_force_on_msb, self.__app_cmmu_force_on_lsb)
    @app_cmmu_force_on.setter
    def app_cmmu_force_on(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cmmu_force_on_msb, self.__app_cmmu_force_on_lsb, value)

    @property
    def app_cmmu_flash_page_mode(self):
        return self.__MEM.rdm(self.__addr, self.__app_cmmu_flash_page_mode_msb, self.__app_cmmu_flash_page_mode_lsb)
    @app_cmmu_flash_page_mode.setter
    def app_cmmu_flash_page_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cmmu_flash_page_mode_msb, self.__app_cmmu_flash_page_mode_lsb, value)

    @property
    def app_cmmu_sram_page_mode(self):
        return self.__MEM.rdm(self.__addr, self.__app_cmmu_sram_page_mode_msb, self.__app_cmmu_sram_page_mode_lsb)
    @app_cmmu_sram_page_mode.setter
    def app_cmmu_sram_page_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cmmu_sram_page_mode_msb, self.__app_cmmu_sram_page_mode_lsb, value)

    @property
    def app_cache_mask_opsdram(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_mask_opsdram_msb, self.__app_cache_mask_opsdram_lsb)
    @app_cache_mask_opsdram.setter
    def app_cache_mask_opsdram(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_mask_opsdram_msb, self.__app_cache_mask_opsdram_lsb, value)

    @property
    def app_cache_mask_drom0(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_mask_drom0_msb, self.__app_cache_mask_drom0_lsb)
    @app_cache_mask_drom0.setter
    def app_cache_mask_drom0(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_mask_drom0_msb, self.__app_cache_mask_drom0_lsb, value)

    @property
    def app_cache_mask_dram1(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_mask_dram1_msb, self.__app_cache_mask_dram1_lsb)
    @app_cache_mask_dram1.setter
    def app_cache_mask_dram1(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_mask_dram1_msb, self.__app_cache_mask_dram1_lsb, value)

    @property
    def app_cache_mask_irom0(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_mask_irom0_msb, self.__app_cache_mask_irom0_lsb)
    @app_cache_mask_irom0.setter
    def app_cache_mask_irom0(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_mask_irom0_msb, self.__app_cache_mask_irom0_lsb, value)

    @property
    def app_cache_mask_iram1(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_mask_iram1_msb, self.__app_cache_mask_iram1_lsb)
    @app_cache_mask_iram1.setter
    def app_cache_mask_iram1(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_mask_iram1_msb, self.__app_cache_mask_iram1_lsb, value)

    @property
    def app_cache_mask_iram0(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_mask_iram0_msb, self.__app_cache_mask_iram0_lsb)
    @app_cache_mask_iram0.setter
    def app_cache_mask_iram0(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_mask_iram0_msb, self.__app_cache_mask_iram0_lsb, value)
class APP_CACHE_LOCK_0_ADDR_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x60
        self.__app_cache_lock_0_addr_max_lsb = 18
        self.__app_cache_lock_0_addr_max_msb = 21
        self.__app_cache_lock_0_addr_min_lsb = 14
        self.__app_cache_lock_0_addr_min_msb = 17
        self.__app_cache_lock_0_addr_pre_lsb = 0
        self.__app_cache_lock_0_addr_pre_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_cache_lock_0_addr_max(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_lock_0_addr_max_msb, self.__app_cache_lock_0_addr_max_lsb)
    @app_cache_lock_0_addr_max.setter
    def app_cache_lock_0_addr_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_lock_0_addr_max_msb, self.__app_cache_lock_0_addr_max_lsb, value)

    @property
    def app_cache_lock_0_addr_min(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_lock_0_addr_min_msb, self.__app_cache_lock_0_addr_min_lsb)
    @app_cache_lock_0_addr_min.setter
    def app_cache_lock_0_addr_min(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_lock_0_addr_min_msb, self.__app_cache_lock_0_addr_min_lsb, value)

    @property
    def app_cache_lock_0_addr_pre(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_lock_0_addr_pre_msb, self.__app_cache_lock_0_addr_pre_lsb)
    @app_cache_lock_0_addr_pre.setter
    def app_cache_lock_0_addr_pre(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_lock_0_addr_pre_msb, self.__app_cache_lock_0_addr_pre_lsb, value)
class APP_CACHE_LOCK_1_ADDR_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x64
        self.__app_cache_lock_1_addr_max_lsb = 18
        self.__app_cache_lock_1_addr_max_msb = 21
        self.__app_cache_lock_1_addr_min_lsb = 14
        self.__app_cache_lock_1_addr_min_msb = 17
        self.__app_cache_lock_1_addr_pre_lsb = 0
        self.__app_cache_lock_1_addr_pre_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_cache_lock_1_addr_max(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_lock_1_addr_max_msb, self.__app_cache_lock_1_addr_max_lsb)
    @app_cache_lock_1_addr_max.setter
    def app_cache_lock_1_addr_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_lock_1_addr_max_msb, self.__app_cache_lock_1_addr_max_lsb, value)

    @property
    def app_cache_lock_1_addr_min(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_lock_1_addr_min_msb, self.__app_cache_lock_1_addr_min_lsb)
    @app_cache_lock_1_addr_min.setter
    def app_cache_lock_1_addr_min(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_lock_1_addr_min_msb, self.__app_cache_lock_1_addr_min_lsb, value)

    @property
    def app_cache_lock_1_addr_pre(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_lock_1_addr_pre_msb, self.__app_cache_lock_1_addr_pre_lsb)
    @app_cache_lock_1_addr_pre.setter
    def app_cache_lock_1_addr_pre(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_lock_1_addr_pre_msb, self.__app_cache_lock_1_addr_pre_lsb, value)
class APP_CACHE_LOCK_2_ADDR_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x68
        self.__app_cache_lock_2_addr_max_lsb = 18
        self.__app_cache_lock_2_addr_max_msb = 21
        self.__app_cache_lock_2_addr_min_lsb = 14
        self.__app_cache_lock_2_addr_min_msb = 17
        self.__app_cache_lock_2_addr_pre_lsb = 0
        self.__app_cache_lock_2_addr_pre_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_cache_lock_2_addr_max(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_lock_2_addr_max_msb, self.__app_cache_lock_2_addr_max_lsb)
    @app_cache_lock_2_addr_max.setter
    def app_cache_lock_2_addr_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_lock_2_addr_max_msb, self.__app_cache_lock_2_addr_max_lsb, value)

    @property
    def app_cache_lock_2_addr_min(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_lock_2_addr_min_msb, self.__app_cache_lock_2_addr_min_lsb)
    @app_cache_lock_2_addr_min.setter
    def app_cache_lock_2_addr_min(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_lock_2_addr_min_msb, self.__app_cache_lock_2_addr_min_lsb, value)

    @property
    def app_cache_lock_2_addr_pre(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_lock_2_addr_pre_msb, self.__app_cache_lock_2_addr_pre_lsb)
    @app_cache_lock_2_addr_pre.setter
    def app_cache_lock_2_addr_pre(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_lock_2_addr_pre_msb, self.__app_cache_lock_2_addr_pre_lsb, value)
class APP_CACHE_LOCK_3_ADDR_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x6c
        self.__app_cache_lock_3_addr_max_lsb = 18
        self.__app_cache_lock_3_addr_max_msb = 21
        self.__app_cache_lock_3_addr_min_lsb = 14
        self.__app_cache_lock_3_addr_min_msb = 17
        self.__app_cache_lock_3_addr_pre_lsb = 0
        self.__app_cache_lock_3_addr_pre_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_cache_lock_3_addr_max(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_lock_3_addr_max_msb, self.__app_cache_lock_3_addr_max_lsb)
    @app_cache_lock_3_addr_max.setter
    def app_cache_lock_3_addr_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_lock_3_addr_max_msb, self.__app_cache_lock_3_addr_max_lsb, value)

    @property
    def app_cache_lock_3_addr_min(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_lock_3_addr_min_msb, self.__app_cache_lock_3_addr_min_lsb)
    @app_cache_lock_3_addr_min.setter
    def app_cache_lock_3_addr_min(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_lock_3_addr_min_msb, self.__app_cache_lock_3_addr_min_lsb, value)

    @property
    def app_cache_lock_3_addr_pre(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_lock_3_addr_pre_msb, self.__app_cache_lock_3_addr_pre_lsb)
    @app_cache_lock_3_addr_pre.setter
    def app_cache_lock_3_addr_pre(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_lock_3_addr_pre_msb, self.__app_cache_lock_3_addr_pre_lsb, value)
class TRACEMEM_MUX_MODE(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x70
        self.__tracemem_mux_mode_lsb = 0
        self.__tracemem_mux_mode_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tracemem_mux_mode(self):
        return self.__MEM.rdm(self.__addr, self.__tracemem_mux_mode_msb, self.__tracemem_mux_mode_lsb)
    @tracemem_mux_mode.setter
    def tracemem_mux_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__tracemem_mux_mode_msb, self.__tracemem_mux_mode_lsb, value)
class PRO_TRACEMEM_ENA(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x74
        self.__pro_tracemem_ena_lsb = 0
        self.__pro_tracemem_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_tracemem_ena(self):
        return self.__MEM.rdm(self.__addr, self.__pro_tracemem_ena_msb, self.__pro_tracemem_ena_lsb)
    @pro_tracemem_ena.setter
    def pro_tracemem_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_tracemem_ena_msb, self.__pro_tracemem_ena_lsb, value)
class APP_TRACEMEM_ENA(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x78
        self.__app_tracemem_ena_lsb = 0
        self.__app_tracemem_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_tracemem_ena(self):
        return self.__MEM.rdm(self.__addr, self.__app_tracemem_ena_msb, self.__app_tracemem_ena_lsb)
    @app_tracemem_ena.setter
    def app_tracemem_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_tracemem_ena_msb, self.__app_tracemem_ena_lsb, value)
class CACHE_MUX_MODE(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x7c
        self.__cache_mux_mode_lsb = 0
        self.__cache_mux_mode_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def cache_mux_mode(self):
        return self.__MEM.rdm(self.__addr, self.__cache_mux_mode_msb, self.__cache_mux_mode_lsb)
    @cache_mux_mode.setter
    def cache_mux_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__cache_mux_mode_msb, self.__cache_mux_mode_lsb, value)
class IMMU_PAGE_MODE(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x80
        self.__immu_page_mode_lsb = 1
        self.__immu_page_mode_msb = 2
        self.__internal_sram_immu_ena_lsb = 0
        self.__internal_sram_immu_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def immu_page_mode(self):
        return self.__MEM.rdm(self.__addr, self.__immu_page_mode_msb, self.__immu_page_mode_lsb)
    @immu_page_mode.setter
    def immu_page_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__immu_page_mode_msb, self.__immu_page_mode_lsb, value)

    @property
    def internal_sram_immu_ena(self):
        return self.__MEM.rdm(self.__addr, self.__internal_sram_immu_ena_msb, self.__internal_sram_immu_ena_lsb)
    @internal_sram_immu_ena.setter
    def internal_sram_immu_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__internal_sram_immu_ena_msb, self.__internal_sram_immu_ena_lsb, value)
class DMMU_PAGE_MODE(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x84
        self.__dmmu_page_mode_lsb = 1
        self.__dmmu_page_mode_msb = 2
        self.__internal_sram_dmmu_ena_lsb = 0
        self.__internal_sram_dmmu_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def dmmu_page_mode(self):
        return self.__MEM.rdm(self.__addr, self.__dmmu_page_mode_msb, self.__dmmu_page_mode_lsb)
    @dmmu_page_mode.setter
    def dmmu_page_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__dmmu_page_mode_msb, self.__dmmu_page_mode_lsb, value)

    @property
    def internal_sram_dmmu_ena(self):
        return self.__MEM.rdm(self.__addr, self.__internal_sram_dmmu_ena_msb, self.__internal_sram_dmmu_ena_lsb)
    @internal_sram_dmmu_ena.setter
    def internal_sram_dmmu_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__internal_sram_dmmu_ena_msb, self.__internal_sram_dmmu_ena_lsb, value)
class ROM_MPU_ENA(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x88
        self.__app_rom_mpu_ena_lsb = 2
        self.__app_rom_mpu_ena_msb = 2
        self.__pro_rom_mpu_ena_lsb = 1
        self.__pro_rom_mpu_ena_msb = 1
        self.__share_rom_mpu_ena_lsb = 0
        self.__share_rom_mpu_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_rom_mpu_ena(self):
        return self.__MEM.rdm(self.__addr, self.__app_rom_mpu_ena_msb, self.__app_rom_mpu_ena_lsb)
    @app_rom_mpu_ena.setter
    def app_rom_mpu_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_rom_mpu_ena_msb, self.__app_rom_mpu_ena_lsb, value)

    @property
    def pro_rom_mpu_ena(self):
        return self.__MEM.rdm(self.__addr, self.__pro_rom_mpu_ena_msb, self.__pro_rom_mpu_ena_lsb)
    @pro_rom_mpu_ena.setter
    def pro_rom_mpu_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_rom_mpu_ena_msb, self.__pro_rom_mpu_ena_lsb, value)

    @property
    def share_rom_mpu_ena(self):
        return self.__MEM.rdm(self.__addr, self.__share_rom_mpu_ena_msb, self.__share_rom_mpu_ena_lsb)
    @share_rom_mpu_ena.setter
    def share_rom_mpu_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__share_rom_mpu_ena_msb, self.__share_rom_mpu_ena_lsb, value)
class MEM_PD_MASK_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x8c
        self.__lslp_mem_pd_mask_lsb = 0
        self.__lslp_mem_pd_mask_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def lslp_mem_pd_mask(self):
        return self.__MEM.rdm(self.__addr, self.__lslp_mem_pd_mask_msb, self.__lslp_mem_pd_mask_lsb)
    @lslp_mem_pd_mask.setter
    def lslp_mem_pd_mask(self, value):
        return self.__MEM.wrm(self.__addr, self.__lslp_mem_pd_mask_msb, self.__lslp_mem_pd_mask_lsb, value)
class ROM_PD_CTRL_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x90
        self.__share_rom_pd_lsb = 2
        self.__share_rom_pd_msb = 7
        self.__app_rom_pd_lsb = 1
        self.__app_rom_pd_msb = 1
        self.__pro_rom_pd_lsb = 0
        self.__pro_rom_pd_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def share_rom_pd(self):
        return self.__MEM.rdm(self.__addr, self.__share_rom_pd_msb, self.__share_rom_pd_lsb)
    @share_rom_pd.setter
    def share_rom_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__share_rom_pd_msb, self.__share_rom_pd_lsb, value)

    @property
    def app_rom_pd(self):
        return self.__MEM.rdm(self.__addr, self.__app_rom_pd_msb, self.__app_rom_pd_lsb)
    @app_rom_pd.setter
    def app_rom_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_rom_pd_msb, self.__app_rom_pd_lsb, value)

    @property
    def pro_rom_pd(self):
        return self.__MEM.rdm(self.__addr, self.__pro_rom_pd_msb, self.__pro_rom_pd_lsb)
    @pro_rom_pd.setter
    def pro_rom_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_rom_pd_msb, self.__pro_rom_pd_lsb, value)
class ROM_FO_CTRL_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x94
        self.__share_rom_fo_lsb = 2
        self.__share_rom_fo_msb = 7
        self.__app_rom_fo_lsb = 1
        self.__app_rom_fo_msb = 1
        self.__pro_rom_fo_lsb = 0
        self.__pro_rom_fo_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def share_rom_fo(self):
        return self.__MEM.rdm(self.__addr, self.__share_rom_fo_msb, self.__share_rom_fo_lsb)
    @share_rom_fo.setter
    def share_rom_fo(self, value):
        return self.__MEM.wrm(self.__addr, self.__share_rom_fo_msb, self.__share_rom_fo_lsb, value)

    @property
    def app_rom_fo(self):
        return self.__MEM.rdm(self.__addr, self.__app_rom_fo_msb, self.__app_rom_fo_lsb)
    @app_rom_fo.setter
    def app_rom_fo(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_rom_fo_msb, self.__app_rom_fo_lsb, value)

    @property
    def pro_rom_fo(self):
        return self.__MEM.rdm(self.__addr, self.__pro_rom_fo_msb, self.__pro_rom_fo_lsb)
    @pro_rom_fo.setter
    def pro_rom_fo(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_rom_fo_msb, self.__pro_rom_fo_lsb, value)
class SRAM_PD_CTRL_REG_0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x98
        self.__sram_pd_0_lsb = 0
        self.__sram_pd_0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_pd_0(self):
        return self.__MEM.rdm(self.__addr, self.__sram_pd_0_msb, self.__sram_pd_0_lsb)
    @sram_pd_0.setter
    def sram_pd_0(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_pd_0_msb, self.__sram_pd_0_lsb, value)
class SRAM_PD_CTRL_REG_1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x9c
        self.__sram_pd_1_lsb = 0
        self.__sram_pd_1_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_pd_1(self):
        return self.__MEM.rdm(self.__addr, self.__sram_pd_1_msb, self.__sram_pd_1_lsb)
    @sram_pd_1.setter
    def sram_pd_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_pd_1_msb, self.__sram_pd_1_lsb, value)
class SRAM_FO_CTRL_REG_0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0xa0
        self.__sram_fo_0_lsb = 0
        self.__sram_fo_0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_fo_0(self):
        return self.__MEM.rdm(self.__addr, self.__sram_fo_0_msb, self.__sram_fo_0_lsb)
    @sram_fo_0.setter
    def sram_fo_0(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_fo_0_msb, self.__sram_fo_0_lsb, value)
class SRAM_FO_CTRL_REG_1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0xa4
        self.__sram_fo_1_lsb = 0
        self.__sram_fo_1_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_fo_1(self):
        return self.__MEM.rdm(self.__addr, self.__sram_fo_1_msb, self.__sram_fo_1_lsb)
    @sram_fo_1.setter
    def sram_fo_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_fo_1_msb, self.__sram_fo_1_lsb, value)
class IRAM_DRAM_AHB_SEL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0xa8
        self.__mac_dump_mode_lsb = 5
        self.__mac_dump_mode_msb = 6
        self.__mask_ahb_lsb = 4
        self.__mask_ahb_msb = 4
        self.__mask_app_dram_lsb = 3
        self.__mask_app_dram_msb = 3
        self.__mask_pro_dram_lsb = 2
        self.__mask_pro_dram_msb = 2
        self.__mask_app_iram_lsb = 1
        self.__mask_app_iram_msb = 1
        self.__mask_pro_iram_lsb = 0
        self.__mask_pro_iram_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def mac_dump_mode(self):
        return self.__MEM.rdm(self.__addr, self.__mac_dump_mode_msb, self.__mac_dump_mode_lsb)
    @mac_dump_mode.setter
    def mac_dump_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__mac_dump_mode_msb, self.__mac_dump_mode_lsb, value)

    @property
    def mask_ahb(self):
        return self.__MEM.rdm(self.__addr, self.__mask_ahb_msb, self.__mask_ahb_lsb)
    @mask_ahb.setter
    def mask_ahb(self, value):
        return self.__MEM.wrm(self.__addr, self.__mask_ahb_msb, self.__mask_ahb_lsb, value)

    @property
    def mask_app_dram(self):
        return self.__MEM.rdm(self.__addr, self.__mask_app_dram_msb, self.__mask_app_dram_lsb)
    @mask_app_dram.setter
    def mask_app_dram(self, value):
        return self.__MEM.wrm(self.__addr, self.__mask_app_dram_msb, self.__mask_app_dram_lsb, value)

    @property
    def mask_pro_dram(self):
        return self.__MEM.rdm(self.__addr, self.__mask_pro_dram_msb, self.__mask_pro_dram_lsb)
    @mask_pro_dram.setter
    def mask_pro_dram(self, value):
        return self.__MEM.wrm(self.__addr, self.__mask_pro_dram_msb, self.__mask_pro_dram_lsb, value)

    @property
    def mask_app_iram(self):
        return self.__MEM.rdm(self.__addr, self.__mask_app_iram_msb, self.__mask_app_iram_lsb)
    @mask_app_iram.setter
    def mask_app_iram(self, value):
        return self.__MEM.wrm(self.__addr, self.__mask_app_iram_msb, self.__mask_app_iram_lsb, value)

    @property
    def mask_pro_iram(self):
        return self.__MEM.rdm(self.__addr, self.__mask_pro_iram_msb, self.__mask_pro_iram_lsb)
    @mask_pro_iram.setter
    def mask_pro_iram(self, value):
        return self.__MEM.wrm(self.__addr, self.__mask_pro_iram_msb, self.__mask_pro_iram_lsb, value)
class TAG_FO_CTRL_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0xac
        self.__app_cache_tag_pd_lsb = 9
        self.__app_cache_tag_pd_msb = 9
        self.__app_cache_tag_force_on_lsb = 8
        self.__app_cache_tag_force_on_msb = 8
        self.__pro_cache_tag_pd_lsb = 1
        self.__pro_cache_tag_pd_msb = 1
        self.__pro_cache_tag_force_on_lsb = 0
        self.__pro_cache_tag_force_on_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_cache_tag_pd(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_tag_pd_msb, self.__app_cache_tag_pd_lsb)
    @app_cache_tag_pd.setter
    def app_cache_tag_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_tag_pd_msb, self.__app_cache_tag_pd_lsb, value)

    @property
    def app_cache_tag_force_on(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_tag_force_on_msb, self.__app_cache_tag_force_on_lsb)
    @app_cache_tag_force_on.setter
    def app_cache_tag_force_on(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_tag_force_on_msb, self.__app_cache_tag_force_on_lsb, value)

    @property
    def pro_cache_tag_pd(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_tag_pd_msb, self.__pro_cache_tag_pd_lsb)
    @pro_cache_tag_pd.setter
    def pro_cache_tag_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_tag_pd_msb, self.__pro_cache_tag_pd_lsb, value)

    @property
    def pro_cache_tag_force_on(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_tag_force_on_msb, self.__pro_cache_tag_force_on_lsb)
    @pro_cache_tag_force_on.setter
    def pro_cache_tag_force_on(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_tag_force_on_msb, self.__pro_cache_tag_force_on_lsb, value)
class AHB_LITE_MASK_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0xb0
        self.__ahb_lite_sdhost_pid_reg_lsb = 11
        self.__ahb_lite_sdhost_pid_reg_msb = 13
        self.__ahb_lite_mask_appdport_lsb = 10
        self.__ahb_lite_mask_appdport_msb = 10
        self.__ahb_lite_mask_prodport_lsb = 9
        self.__ahb_lite_mask_prodport_msb = 9
        self.__ahb_lite_mask_sdio_lsb = 8
        self.__ahb_lite_mask_sdio_msb = 8
        self.__ahb_lite_mask_app_lsb = 4
        self.__ahb_lite_mask_app_msb = 4
        self.__ahb_lite_mask_pro_lsb = 0
        self.__ahb_lite_mask_pro_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def ahb_lite_sdhost_pid_reg(self):
        return self.__MEM.rdm(self.__addr, self.__ahb_lite_sdhost_pid_reg_msb, self.__ahb_lite_sdhost_pid_reg_lsb)
    @ahb_lite_sdhost_pid_reg.setter
    def ahb_lite_sdhost_pid_reg(self, value):
        return self.__MEM.wrm(self.__addr, self.__ahb_lite_sdhost_pid_reg_msb, self.__ahb_lite_sdhost_pid_reg_lsb, value)

    @property
    def ahb_lite_mask_appdport(self):
        return self.__MEM.rdm(self.__addr, self.__ahb_lite_mask_appdport_msb, self.__ahb_lite_mask_appdport_lsb)
    @ahb_lite_mask_appdport.setter
    def ahb_lite_mask_appdport(self, value):
        return self.__MEM.wrm(self.__addr, self.__ahb_lite_mask_appdport_msb, self.__ahb_lite_mask_appdport_lsb, value)

    @property
    def ahb_lite_mask_prodport(self):
        return self.__MEM.rdm(self.__addr, self.__ahb_lite_mask_prodport_msb, self.__ahb_lite_mask_prodport_lsb)
    @ahb_lite_mask_prodport.setter
    def ahb_lite_mask_prodport(self, value):
        return self.__MEM.wrm(self.__addr, self.__ahb_lite_mask_prodport_msb, self.__ahb_lite_mask_prodport_lsb, value)

    @property
    def ahb_lite_mask_sdio(self):
        return self.__MEM.rdm(self.__addr, self.__ahb_lite_mask_sdio_msb, self.__ahb_lite_mask_sdio_lsb)
    @ahb_lite_mask_sdio.setter
    def ahb_lite_mask_sdio(self, value):
        return self.__MEM.wrm(self.__addr, self.__ahb_lite_mask_sdio_msb, self.__ahb_lite_mask_sdio_lsb, value)

    @property
    def ahb_lite_mask_app(self):
        return self.__MEM.rdm(self.__addr, self.__ahb_lite_mask_app_msb, self.__ahb_lite_mask_app_lsb)
    @ahb_lite_mask_app.setter
    def ahb_lite_mask_app(self, value):
        return self.__MEM.wrm(self.__addr, self.__ahb_lite_mask_app_msb, self.__ahb_lite_mask_app_lsb, value)

    @property
    def ahb_lite_mask_pro(self):
        return self.__MEM.rdm(self.__addr, self.__ahb_lite_mask_pro_msb, self.__ahb_lite_mask_pro_lsb)
    @ahb_lite_mask_pro.setter
    def ahb_lite_mask_pro(self, value):
        return self.__MEM.wrm(self.__addr, self.__ahb_lite_mask_pro_msb, self.__ahb_lite_mask_pro_lsb, value)
class AHB_MPU_TABLE_0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0xb4
        self.__ahb_access_grant_0_lsb = 0
        self.__ahb_access_grant_0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def ahb_access_grant_0(self):
        return self.__MEM.rdm(self.__addr, self.__ahb_access_grant_0_msb, self.__ahb_access_grant_0_lsb)
    @ahb_access_grant_0.setter
    def ahb_access_grant_0(self, value):
        return self.__MEM.wrm(self.__addr, self.__ahb_access_grant_0_msb, self.__ahb_access_grant_0_lsb, value)
class AHB_MPU_TABLE_1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0xb8
        self.__ahb_access_grant_1_lsb = 0
        self.__ahb_access_grant_1_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def ahb_access_grant_1(self):
        return self.__MEM.rdm(self.__addr, self.__ahb_access_grant_1_msb, self.__ahb_access_grant_1_lsb)
    @ahb_access_grant_1.setter
    def ahb_access_grant_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__ahb_access_grant_1_msb, self.__ahb_access_grant_1_lsb, value)
class HOST_INF_SEL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0xbc
        self.__link_device_sel_lsb = 8
        self.__link_device_sel_msb = 15
        self.__peri_io_swap_lsb = 0
        self.__peri_io_swap_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def link_device_sel(self):
        return self.__MEM.rdm(self.__addr, self.__link_device_sel_msb, self.__link_device_sel_lsb)
    @link_device_sel.setter
    def link_device_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__link_device_sel_msb, self.__link_device_sel_lsb, value)

    @property
    def peri_io_swap(self):
        return self.__MEM.rdm(self.__addr, self.__peri_io_swap_msb, self.__peri_io_swap_lsb)
    @peri_io_swap.setter
    def peri_io_swap(self, value):
        return self.__MEM.wrm(self.__addr, self.__peri_io_swap_msb, self.__peri_io_swap_lsb, value)
class PERIP_CLK_EN(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0xc0
        self.__reg_perip_clk_en_lsb = 0
        self.__reg_perip_clk_en_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_perip_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_perip_clk_en_msb, self.__reg_perip_clk_en_lsb)
    @reg_perip_clk_en.setter
    def reg_perip_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_perip_clk_en_msb, self.__reg_perip_clk_en_lsb, value)
class PERIP_RST_EN(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0xc4
        self.__reg_perip_rst_lsb = 0
        self.__reg_perip_rst_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_perip_rst(self):
        return self.__MEM.rdm(self.__addr, self.__reg_perip_rst_msb, self.__reg_perip_rst_lsb)
    @reg_perip_rst.setter
    def reg_perip_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_perip_rst_msb, self.__reg_perip_rst_lsb, value)
class SLAVE_SPI_CONFIG_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0xc8
        self.__reg_spi_decrypt_enable_lsb = 12
        self.__reg_spi_decrypt_enable_msb = 12
        self.__reg_spi_encrypt_enable_lsb = 8
        self.__reg_spi_encrypt_enable_msb = 8
        self.__slave_spi_mask_app_lsb = 4
        self.__slave_spi_mask_app_msb = 4
        self.__slave_spi_mask_pro_lsb = 0
        self.__slave_spi_mask_pro_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_spi_decrypt_enable(self):
        return self.__MEM.rdm(self.__addr, self.__reg_spi_decrypt_enable_msb, self.__reg_spi_decrypt_enable_lsb)
    @reg_spi_decrypt_enable.setter
    def reg_spi_decrypt_enable(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_spi_decrypt_enable_msb, self.__reg_spi_decrypt_enable_lsb, value)

    @property
    def reg_spi_encrypt_enable(self):
        return self.__MEM.rdm(self.__addr, self.__reg_spi_encrypt_enable_msb, self.__reg_spi_encrypt_enable_lsb)
    @reg_spi_encrypt_enable.setter
    def reg_spi_encrypt_enable(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_spi_encrypt_enable_msb, self.__reg_spi_encrypt_enable_lsb, value)

    @property
    def slave_spi_mask_app(self):
        return self.__MEM.rdm(self.__addr, self.__slave_spi_mask_app_msb, self.__slave_spi_mask_app_lsb)
    @slave_spi_mask_app.setter
    def slave_spi_mask_app(self, value):
        return self.__MEM.wrm(self.__addr, self.__slave_spi_mask_app_msb, self.__slave_spi_mask_app_lsb, value)

    @property
    def slave_spi_mask_pro(self):
        return self.__MEM.rdm(self.__addr, self.__slave_spi_mask_pro_msb, self.__slave_spi_mask_pro_lsb)
    @slave_spi_mask_pro.setter
    def slave_spi_mask_pro(self, value):
        return self.__MEM.wrm(self.__addr, self.__slave_spi_mask_pro_msb, self.__slave_spi_mask_pro_lsb, value)
class WIFI_CLK_EN(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0xcc
        self.__reg_wifi_clk_en_lsb = 0
        self.__reg_wifi_clk_en_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wifi_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wifi_clk_en_msb, self.__reg_wifi_clk_en_lsb)
    @reg_wifi_clk_en.setter
    def reg_wifi_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wifi_clk_en_msb, self.__reg_wifi_clk_en_lsb, value)
class WIFI_RST_EN(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0xd0
        self.__reg_wifi_rst_lsb = 0
        self.__reg_wifi_rst_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wifi_rst(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wifi_rst_msb, self.__reg_wifi_rst_lsb)
    @reg_wifi_rst.setter
    def reg_wifi_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wifi_rst_msb, self.__reg_wifi_rst_lsb, value)
class BT_LPCK_DIV_INT(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0xd4
        self.__reg_btextwakeup_req_lsb = 12
        self.__reg_btextwakeup_req_msb = 12
        self.__reg_bt_lpck_div_num_lsb = 0
        self.__reg_bt_lpck_div_num_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_btextwakeup_req(self):
        return self.__MEM.rdm(self.__addr, self.__reg_btextwakeup_req_msb, self.__reg_btextwakeup_req_lsb)
    @reg_btextwakeup_req.setter
    def reg_btextwakeup_req(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_btextwakeup_req_msb, self.__reg_btextwakeup_req_lsb, value)

    @property
    def reg_bt_lpck_div_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bt_lpck_div_num_msb, self.__reg_bt_lpck_div_num_lsb)
    @reg_bt_lpck_div_num.setter
    def reg_bt_lpck_div_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bt_lpck_div_num_msb, self.__reg_bt_lpck_div_num_lsb, value)
class BT_LPCK_DIV_FRAC(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0xd8
        self.__reg_lpclk_sel_xtal32k_lsb = 27
        self.__reg_lpclk_sel_xtal32k_msb = 27
        self.__reg_lpclk_sel_xtal_lsb = 26
        self.__reg_lpclk_sel_xtal_msb = 26
        self.__reg_lpclk_sel_8m_lsb = 25
        self.__reg_lpclk_sel_8m_msb = 25
        self.__reg_lpclk_sel_rtc_slow_lsb = 24
        self.__reg_lpclk_sel_rtc_slow_msb = 24
        self.__reg_bt_lpck_div_a_lsb = 12
        self.__reg_bt_lpck_div_a_msb = 23
        self.__reg_bt_lpck_div_b_lsb = 0
        self.__reg_bt_lpck_div_b_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_lpclk_sel_xtal32k(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lpclk_sel_xtal32k_msb, self.__reg_lpclk_sel_xtal32k_lsb)
    @reg_lpclk_sel_xtal32k.setter
    def reg_lpclk_sel_xtal32k(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lpclk_sel_xtal32k_msb, self.__reg_lpclk_sel_xtal32k_lsb, value)

    @property
    def reg_lpclk_sel_xtal(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lpclk_sel_xtal_msb, self.__reg_lpclk_sel_xtal_lsb)
    @reg_lpclk_sel_xtal.setter
    def reg_lpclk_sel_xtal(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lpclk_sel_xtal_msb, self.__reg_lpclk_sel_xtal_lsb, value)

    @property
    def reg_lpclk_sel_8m(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lpclk_sel_8m_msb, self.__reg_lpclk_sel_8m_lsb)
    @reg_lpclk_sel_8m.setter
    def reg_lpclk_sel_8m(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lpclk_sel_8m_msb, self.__reg_lpclk_sel_8m_lsb, value)

    @property
    def reg_lpclk_sel_rtc_slow(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lpclk_sel_rtc_slow_msb, self.__reg_lpclk_sel_rtc_slow_lsb)
    @reg_lpclk_sel_rtc_slow.setter
    def reg_lpclk_sel_rtc_slow(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lpclk_sel_rtc_slow_msb, self.__reg_lpclk_sel_rtc_slow_lsb, value)

    @property
    def reg_bt_lpck_div_a(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bt_lpck_div_a_msb, self.__reg_bt_lpck_div_a_lsb)
    @reg_bt_lpck_div_a.setter
    def reg_bt_lpck_div_a(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bt_lpck_div_a_msb, self.__reg_bt_lpck_div_a_lsb, value)

    @property
    def reg_bt_lpck_div_b(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bt_lpck_div_b_msb, self.__reg_bt_lpck_div_b_lsb)
    @reg_bt_lpck_div_b.setter
    def reg_bt_lpck_div_b(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bt_lpck_div_b_msb, self.__reg_bt_lpck_div_b_lsb, value)
class CPU_INTR_FROM_CPU_0_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0xdc
        self.__cpu_intr_from_cpu_0_lsb = 0
        self.__cpu_intr_from_cpu_0_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def cpu_intr_from_cpu_0(self):
        return self.__MEM.rdm(self.__addr, self.__cpu_intr_from_cpu_0_msb, self.__cpu_intr_from_cpu_0_lsb)
    @cpu_intr_from_cpu_0.setter
    def cpu_intr_from_cpu_0(self, value):
        return self.__MEM.wrm(self.__addr, self.__cpu_intr_from_cpu_0_msb, self.__cpu_intr_from_cpu_0_lsb, value)
class CPU_INTR_FROM_CPU_1_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0xe0
        self.__cpu_intr_from_cpu_1_lsb = 0
        self.__cpu_intr_from_cpu_1_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def cpu_intr_from_cpu_1(self):
        return self.__MEM.rdm(self.__addr, self.__cpu_intr_from_cpu_1_msb, self.__cpu_intr_from_cpu_1_lsb)
    @cpu_intr_from_cpu_1.setter
    def cpu_intr_from_cpu_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__cpu_intr_from_cpu_1_msb, self.__cpu_intr_from_cpu_1_lsb, value)
class CPU_INTR_FROM_CPU_2_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0xe4
        self.__cpu_intr_from_cpu_2_lsb = 0
        self.__cpu_intr_from_cpu_2_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def cpu_intr_from_cpu_2(self):
        return self.__MEM.rdm(self.__addr, self.__cpu_intr_from_cpu_2_msb, self.__cpu_intr_from_cpu_2_lsb)
    @cpu_intr_from_cpu_2.setter
    def cpu_intr_from_cpu_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__cpu_intr_from_cpu_2_msb, self.__cpu_intr_from_cpu_2_lsb, value)
class CPU_INTR_FROM_CPU_3_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0xe8
        self.__cpu_intr_from_cpu_3_lsb = 0
        self.__cpu_intr_from_cpu_3_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def cpu_intr_from_cpu_3(self):
        return self.__MEM.rdm(self.__addr, self.__cpu_intr_from_cpu_3_msb, self.__cpu_intr_from_cpu_3_lsb)
    @cpu_intr_from_cpu_3.setter
    def cpu_intr_from_cpu_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__cpu_intr_from_cpu_3_msb, self.__cpu_intr_from_cpu_3_lsb, value)
class PRO_INTR_STATUS_REG_0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0xec
        self.__pro_intr_status_0_lsb = 0
        self.__pro_intr_status_0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_intr_status_0(self):
        return self.__MEM.rdm(self.__addr, self.__pro_intr_status_0_msb, self.__pro_intr_status_0_lsb)
    @pro_intr_status_0.setter
    def pro_intr_status_0(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_intr_status_0_msb, self.__pro_intr_status_0_lsb, value)
class PRO_INTR_STATUS_REG_1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0xf0
        self.__pro_intr_status_1_lsb = 0
        self.__pro_intr_status_1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_intr_status_1(self):
        return self.__MEM.rdm(self.__addr, self.__pro_intr_status_1_msb, self.__pro_intr_status_1_lsb)
    @pro_intr_status_1.setter
    def pro_intr_status_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_intr_status_1_msb, self.__pro_intr_status_1_lsb, value)
class PRO_INTR_STATUS_REG_2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0xf4
        self.__pro_intr_status_2_lsb = 0
        self.__pro_intr_status_2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_intr_status_2(self):
        return self.__MEM.rdm(self.__addr, self.__pro_intr_status_2_msb, self.__pro_intr_status_2_lsb)
    @pro_intr_status_2.setter
    def pro_intr_status_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_intr_status_2_msb, self.__pro_intr_status_2_lsb, value)
class APP_INTR_STATUS_REG_0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0xf8
        self.__app_intr_status_0_lsb = 0
        self.__app_intr_status_0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_intr_status_0(self):
        return self.__MEM.rdm(self.__addr, self.__app_intr_status_0_msb, self.__app_intr_status_0_lsb)
    @app_intr_status_0.setter
    def app_intr_status_0(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_intr_status_0_msb, self.__app_intr_status_0_lsb, value)
class APP_INTR_STATUS_REG_1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0xfc
        self.__app_intr_status_1_lsb = 0
        self.__app_intr_status_1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_intr_status_1(self):
        return self.__MEM.rdm(self.__addr, self.__app_intr_status_1_msb, self.__app_intr_status_1_lsb)
    @app_intr_status_1.setter
    def app_intr_status_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_intr_status_1_msb, self.__app_intr_status_1_lsb, value)
class APP_INTR_STATUS_REG_2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x100
        self.__app_intr_status_2_lsb = 0
        self.__app_intr_status_2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_intr_status_2(self):
        return self.__MEM.rdm(self.__addr, self.__app_intr_status_2_msb, self.__app_intr_status_2_lsb)
    @app_intr_status_2.setter
    def app_intr_status_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_intr_status_2_msb, self.__app_intr_status_2_lsb, value)
class PRO_MAC_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x104
        self.__pro_mac_intr_map_lsb = 0
        self.__pro_mac_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_mac_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_mac_intr_map_msb, self.__pro_mac_intr_map_lsb)
    @pro_mac_intr_map.setter
    def pro_mac_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_mac_intr_map_msb, self.__pro_mac_intr_map_lsb, value)
class PRO_MAC_NMI_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x108
        self.__pro_mac_nmi_map_lsb = 0
        self.__pro_mac_nmi_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_mac_nmi_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_mac_nmi_map_msb, self.__pro_mac_nmi_map_lsb)
    @pro_mac_nmi_map.setter
    def pro_mac_nmi_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_mac_nmi_map_msb, self.__pro_mac_nmi_map_lsb, value)
class PRO_BB_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x10c
        self.__pro_bb_int_map_lsb = 0
        self.__pro_bb_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_bb_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_bb_int_map_msb, self.__pro_bb_int_map_lsb)
    @pro_bb_int_map.setter
    def pro_bb_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_bb_int_map_msb, self.__pro_bb_int_map_lsb, value)
class PRO_BT_MAC_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x110
        self.__pro_bt_mac_int_map_lsb = 0
        self.__pro_bt_mac_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_bt_mac_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_bt_mac_int_map_msb, self.__pro_bt_mac_int_map_lsb)
    @pro_bt_mac_int_map.setter
    def pro_bt_mac_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_bt_mac_int_map_msb, self.__pro_bt_mac_int_map_lsb, value)
class PRO_BT_BB_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x114
        self.__pro_bt_bb_int_map_lsb = 0
        self.__pro_bt_bb_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_bt_bb_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_bt_bb_int_map_msb, self.__pro_bt_bb_int_map_lsb)
    @pro_bt_bb_int_map.setter
    def pro_bt_bb_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_bt_bb_int_map_msb, self.__pro_bt_bb_int_map_lsb, value)
class PRO_BT_BB_NMI_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x118
        self.__pro_bt_bb_nmi_map_lsb = 0
        self.__pro_bt_bb_nmi_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_bt_bb_nmi_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_bt_bb_nmi_map_msb, self.__pro_bt_bb_nmi_map_lsb)
    @pro_bt_bb_nmi_map.setter
    def pro_bt_bb_nmi_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_bt_bb_nmi_map_msb, self.__pro_bt_bb_nmi_map_lsb, value)
class PRO_RWBT_IRQ_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x11c
        self.__pro_rwbt_irq_map_lsb = 0
        self.__pro_rwbt_irq_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_rwbt_irq_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_rwbt_irq_map_msb, self.__pro_rwbt_irq_map_lsb)
    @pro_rwbt_irq_map.setter
    def pro_rwbt_irq_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_rwbt_irq_map_msb, self.__pro_rwbt_irq_map_lsb, value)
class PRO_RWBLE_IRQ_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x120
        self.__pro_rwble_irq_map_lsb = 0
        self.__pro_rwble_irq_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_rwble_irq_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_rwble_irq_map_msb, self.__pro_rwble_irq_map_lsb)
    @pro_rwble_irq_map.setter
    def pro_rwble_irq_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_rwble_irq_map_msb, self.__pro_rwble_irq_map_lsb, value)
class PRO_RWBT_NMI_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x124
        self.__pro_rwbt_nmi_map_lsb = 0
        self.__pro_rwbt_nmi_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_rwbt_nmi_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_rwbt_nmi_map_msb, self.__pro_rwbt_nmi_map_lsb)
    @pro_rwbt_nmi_map.setter
    def pro_rwbt_nmi_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_rwbt_nmi_map_msb, self.__pro_rwbt_nmi_map_lsb, value)
class PRO_RWBLE_NMI_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x128
        self.__pro_rwble_nmi_map_lsb = 0
        self.__pro_rwble_nmi_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_rwble_nmi_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_rwble_nmi_map_msb, self.__pro_rwble_nmi_map_lsb)
    @pro_rwble_nmi_map.setter
    def pro_rwble_nmi_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_rwble_nmi_map_msb, self.__pro_rwble_nmi_map_lsb, value)
class PRO_SLC0_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x12c
        self.__pro_slc0_intr_map_lsb = 0
        self.__pro_slc0_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_slc0_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_slc0_intr_map_msb, self.__pro_slc0_intr_map_lsb)
    @pro_slc0_intr_map.setter
    def pro_slc0_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_slc0_intr_map_msb, self.__pro_slc0_intr_map_lsb, value)
class PRO_SLC1_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x130
        self.__pro_slc1_intr_map_lsb = 0
        self.__pro_slc1_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_slc1_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_slc1_intr_map_msb, self.__pro_slc1_intr_map_lsb)
    @pro_slc1_intr_map.setter
    def pro_slc1_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_slc1_intr_map_msb, self.__pro_slc1_intr_map_lsb, value)
class PRO_UHCI0_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x134
        self.__pro_uhci0_intr_map_lsb = 0
        self.__pro_uhci0_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_uhci0_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_uhci0_intr_map_msb, self.__pro_uhci0_intr_map_lsb)
    @pro_uhci0_intr_map.setter
    def pro_uhci0_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_uhci0_intr_map_msb, self.__pro_uhci0_intr_map_lsb, value)
class PRO_UHCI1_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x138
        self.__pro_uhci1_intr_map_lsb = 0
        self.__pro_uhci1_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_uhci1_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_uhci1_intr_map_msb, self.__pro_uhci1_intr_map_lsb)
    @pro_uhci1_intr_map.setter
    def pro_uhci1_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_uhci1_intr_map_msb, self.__pro_uhci1_intr_map_lsb, value)
class PRO_TG_T0_LEVEL_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x13c
        self.__pro_tg_t0_level_int_map_lsb = 0
        self.__pro_tg_t0_level_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_tg_t0_level_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_tg_t0_level_int_map_msb, self.__pro_tg_t0_level_int_map_lsb)
    @pro_tg_t0_level_int_map.setter
    def pro_tg_t0_level_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_tg_t0_level_int_map_msb, self.__pro_tg_t0_level_int_map_lsb, value)
class PRO_TG_T1_LEVEL_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x140
        self.__pro_tg_t1_level_int_map_lsb = 0
        self.__pro_tg_t1_level_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_tg_t1_level_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_tg_t1_level_int_map_msb, self.__pro_tg_t1_level_int_map_lsb)
    @pro_tg_t1_level_int_map.setter
    def pro_tg_t1_level_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_tg_t1_level_int_map_msb, self.__pro_tg_t1_level_int_map_lsb, value)
class PRO_TG_WDT_LEVEL_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x144
        self.__pro_tg_wdt_level_int_map_lsb = 0
        self.__pro_tg_wdt_level_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_tg_wdt_level_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_tg_wdt_level_int_map_msb, self.__pro_tg_wdt_level_int_map_lsb)
    @pro_tg_wdt_level_int_map.setter
    def pro_tg_wdt_level_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_tg_wdt_level_int_map_msb, self.__pro_tg_wdt_level_int_map_lsb, value)
class PRO_TG_LACT_LEVEL_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x148
        self.__pro_tg_lact_level_int_map_lsb = 0
        self.__pro_tg_lact_level_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_tg_lact_level_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_tg_lact_level_int_map_msb, self.__pro_tg_lact_level_int_map_lsb)
    @pro_tg_lact_level_int_map.setter
    def pro_tg_lact_level_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_tg_lact_level_int_map_msb, self.__pro_tg_lact_level_int_map_lsb, value)
class PRO_TG1_T0_LEVEL_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x14c
        self.__pro_tg1_t0_level_int_map_lsb = 0
        self.__pro_tg1_t0_level_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_tg1_t0_level_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_tg1_t0_level_int_map_msb, self.__pro_tg1_t0_level_int_map_lsb)
    @pro_tg1_t0_level_int_map.setter
    def pro_tg1_t0_level_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_tg1_t0_level_int_map_msb, self.__pro_tg1_t0_level_int_map_lsb, value)
class PRO_TG1_T1_LEVEL_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x150
        self.__pro_tg1_t1_level_int_map_lsb = 0
        self.__pro_tg1_t1_level_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_tg1_t1_level_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_tg1_t1_level_int_map_msb, self.__pro_tg1_t1_level_int_map_lsb)
    @pro_tg1_t1_level_int_map.setter
    def pro_tg1_t1_level_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_tg1_t1_level_int_map_msb, self.__pro_tg1_t1_level_int_map_lsb, value)
class PRO_TG1_WDT_LEVEL_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x154
        self.__pro_tg1_wdt_level_int_map_lsb = 0
        self.__pro_tg1_wdt_level_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_tg1_wdt_level_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_tg1_wdt_level_int_map_msb, self.__pro_tg1_wdt_level_int_map_lsb)
    @pro_tg1_wdt_level_int_map.setter
    def pro_tg1_wdt_level_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_tg1_wdt_level_int_map_msb, self.__pro_tg1_wdt_level_int_map_lsb, value)
class PRO_TG1_LACT_LEVEL_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x158
        self.__pro_tg1_lact_level_int_map_lsb = 0
        self.__pro_tg1_lact_level_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_tg1_lact_level_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_tg1_lact_level_int_map_msb, self.__pro_tg1_lact_level_int_map_lsb)
    @pro_tg1_lact_level_int_map.setter
    def pro_tg1_lact_level_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_tg1_lact_level_int_map_msb, self.__pro_tg1_lact_level_int_map_lsb, value)
class PRO_GPIO_INTERRUPT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x15c
        self.__pro_gpio_interrupt_pro_map_lsb = 0
        self.__pro_gpio_interrupt_pro_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_gpio_interrupt_pro_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_gpio_interrupt_pro_map_msb, self.__pro_gpio_interrupt_pro_map_lsb)
    @pro_gpio_interrupt_pro_map.setter
    def pro_gpio_interrupt_pro_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_gpio_interrupt_pro_map_msb, self.__pro_gpio_interrupt_pro_map_lsb, value)
class PRO_GPIO_INTERRUPT_NMI_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x160
        self.__pro_gpio_interrupt_pro_nmi_map_lsb = 0
        self.__pro_gpio_interrupt_pro_nmi_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_gpio_interrupt_pro_nmi_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_gpio_interrupt_pro_nmi_map_msb, self.__pro_gpio_interrupt_pro_nmi_map_lsb)
    @pro_gpio_interrupt_pro_nmi_map.setter
    def pro_gpio_interrupt_pro_nmi_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_gpio_interrupt_pro_nmi_map_msb, self.__pro_gpio_interrupt_pro_nmi_map_lsb, value)
class PRO_CPU_INTR_FROM_CPU_0_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x164
        self.__pro_cpu_intr_from_cpu_0_map_lsb = 0
        self.__pro_cpu_intr_from_cpu_0_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_cpu_intr_from_cpu_0_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cpu_intr_from_cpu_0_map_msb, self.__pro_cpu_intr_from_cpu_0_map_lsb)
    @pro_cpu_intr_from_cpu_0_map.setter
    def pro_cpu_intr_from_cpu_0_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cpu_intr_from_cpu_0_map_msb, self.__pro_cpu_intr_from_cpu_0_map_lsb, value)
class PRO_CPU_INTR_FROM_CPU_1_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x168
        self.__pro_cpu_intr_from_cpu_1_map_lsb = 0
        self.__pro_cpu_intr_from_cpu_1_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_cpu_intr_from_cpu_1_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cpu_intr_from_cpu_1_map_msb, self.__pro_cpu_intr_from_cpu_1_map_lsb)
    @pro_cpu_intr_from_cpu_1_map.setter
    def pro_cpu_intr_from_cpu_1_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cpu_intr_from_cpu_1_map_msb, self.__pro_cpu_intr_from_cpu_1_map_lsb, value)
class PRO_CPU_INTR_FROM_CPU_2_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x16c
        self.__pro_cpu_intr_from_cpu_2_map_lsb = 0
        self.__pro_cpu_intr_from_cpu_2_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_cpu_intr_from_cpu_2_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cpu_intr_from_cpu_2_map_msb, self.__pro_cpu_intr_from_cpu_2_map_lsb)
    @pro_cpu_intr_from_cpu_2_map.setter
    def pro_cpu_intr_from_cpu_2_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cpu_intr_from_cpu_2_map_msb, self.__pro_cpu_intr_from_cpu_2_map_lsb, value)
class PRO_CPU_INTR_FROM_CPU_3_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x170
        self.__pro_cpu_intr_from_cpu_3_map_lsb = 0
        self.__pro_cpu_intr_from_cpu_3_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_cpu_intr_from_cpu_3_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cpu_intr_from_cpu_3_map_msb, self.__pro_cpu_intr_from_cpu_3_map_lsb)
    @pro_cpu_intr_from_cpu_3_map.setter
    def pro_cpu_intr_from_cpu_3_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cpu_intr_from_cpu_3_map_msb, self.__pro_cpu_intr_from_cpu_3_map_lsb, value)
class PRO_SPI_INTR_0_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x174
        self.__pro_spi_intr_0_map_lsb = 0
        self.__pro_spi_intr_0_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_spi_intr_0_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_spi_intr_0_map_msb, self.__pro_spi_intr_0_map_lsb)
    @pro_spi_intr_0_map.setter
    def pro_spi_intr_0_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_spi_intr_0_map_msb, self.__pro_spi_intr_0_map_lsb, value)
class PRO_SPI_INTR_1_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x178
        self.__pro_spi_intr_1_map_lsb = 0
        self.__pro_spi_intr_1_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_spi_intr_1_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_spi_intr_1_map_msb, self.__pro_spi_intr_1_map_lsb)
    @pro_spi_intr_1_map.setter
    def pro_spi_intr_1_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_spi_intr_1_map_msb, self.__pro_spi_intr_1_map_lsb, value)
class PRO_SPI_INTR_2_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x17c
        self.__pro_spi_intr_2_map_lsb = 0
        self.__pro_spi_intr_2_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_spi_intr_2_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_spi_intr_2_map_msb, self.__pro_spi_intr_2_map_lsb)
    @pro_spi_intr_2_map.setter
    def pro_spi_intr_2_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_spi_intr_2_map_msb, self.__pro_spi_intr_2_map_lsb, value)
class PRO_SPI_INTR_3_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x180
        self.__pro_spi_intr_3_map_lsb = 0
        self.__pro_spi_intr_3_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_spi_intr_3_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_spi_intr_3_map_msb, self.__pro_spi_intr_3_map_lsb)
    @pro_spi_intr_3_map.setter
    def pro_spi_intr_3_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_spi_intr_3_map_msb, self.__pro_spi_intr_3_map_lsb, value)
class PRO_I2S0_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x184
        self.__pro_i2s0_int_map_lsb = 0
        self.__pro_i2s0_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_i2s0_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_i2s0_int_map_msb, self.__pro_i2s0_int_map_lsb)
    @pro_i2s0_int_map.setter
    def pro_i2s0_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_i2s0_int_map_msb, self.__pro_i2s0_int_map_lsb, value)
class PRO_I2S1_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x188
        self.__pro_i2s1_int_map_lsb = 0
        self.__pro_i2s1_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_i2s1_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_i2s1_int_map_msb, self.__pro_i2s1_int_map_lsb)
    @pro_i2s1_int_map.setter
    def pro_i2s1_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_i2s1_int_map_msb, self.__pro_i2s1_int_map_lsb, value)
class PRO_UART_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x18c
        self.__pro_uart_intr_map_lsb = 0
        self.__pro_uart_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_uart_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_uart_intr_map_msb, self.__pro_uart_intr_map_lsb)
    @pro_uart_intr_map.setter
    def pro_uart_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_uart_intr_map_msb, self.__pro_uart_intr_map_lsb, value)
class PRO_UART1_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x190
        self.__pro_uart1_intr_map_lsb = 0
        self.__pro_uart1_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_uart1_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_uart1_intr_map_msb, self.__pro_uart1_intr_map_lsb)
    @pro_uart1_intr_map.setter
    def pro_uart1_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_uart1_intr_map_msb, self.__pro_uart1_intr_map_lsb, value)
class PRO_UART2_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x194
        self.__pro_uart2_intr_map_lsb = 0
        self.__pro_uart2_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_uart2_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_uart2_intr_map_msb, self.__pro_uart2_intr_map_lsb)
    @pro_uart2_intr_map.setter
    def pro_uart2_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_uart2_intr_map_msb, self.__pro_uart2_intr_map_lsb, value)
class PRO_SDIO_HOST_INTERRUPT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x198
        self.__pro_sdio_host_interrupt_map_lsb = 0
        self.__pro_sdio_host_interrupt_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_sdio_host_interrupt_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_sdio_host_interrupt_map_msb, self.__pro_sdio_host_interrupt_map_lsb)
    @pro_sdio_host_interrupt_map.setter
    def pro_sdio_host_interrupt_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_sdio_host_interrupt_map_msb, self.__pro_sdio_host_interrupt_map_lsb, value)
class PRO_EMAC_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x19c
        self.__pro_emac_int_map_lsb = 0
        self.__pro_emac_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_emac_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_emac_int_map_msb, self.__pro_emac_int_map_lsb)
    @pro_emac_int_map.setter
    def pro_emac_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_emac_int_map_msb, self.__pro_emac_int_map_lsb, value)
class PRO_PWM0_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x1a0
        self.__pro_pwm0_intr_map_lsb = 0
        self.__pro_pwm0_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_pwm0_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_pwm0_intr_map_msb, self.__pro_pwm0_intr_map_lsb)
    @pro_pwm0_intr_map.setter
    def pro_pwm0_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_pwm0_intr_map_msb, self.__pro_pwm0_intr_map_lsb, value)
class PRO_PWM1_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x1a4
        self.__pro_pwm1_intr_map_lsb = 0
        self.__pro_pwm1_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_pwm1_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_pwm1_intr_map_msb, self.__pro_pwm1_intr_map_lsb)
    @pro_pwm1_intr_map.setter
    def pro_pwm1_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_pwm1_intr_map_msb, self.__pro_pwm1_intr_map_lsb, value)
class PRO_PWM2_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x1a8
        self.__pro_pwm2_intr_map_lsb = 0
        self.__pro_pwm2_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_pwm2_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_pwm2_intr_map_msb, self.__pro_pwm2_intr_map_lsb)
    @pro_pwm2_intr_map.setter
    def pro_pwm2_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_pwm2_intr_map_msb, self.__pro_pwm2_intr_map_lsb, value)
class PRO_PWM3_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x1ac
        self.__pro_pwm3_intr_map_lsb = 0
        self.__pro_pwm3_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_pwm3_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_pwm3_intr_map_msb, self.__pro_pwm3_intr_map_lsb)
    @pro_pwm3_intr_map.setter
    def pro_pwm3_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_pwm3_intr_map_msb, self.__pro_pwm3_intr_map_lsb, value)
class PRO_LEDC_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x1b0
        self.__pro_ledc_int_map_lsb = 0
        self.__pro_ledc_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_ledc_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_ledc_int_map_msb, self.__pro_ledc_int_map_lsb)
    @pro_ledc_int_map.setter
    def pro_ledc_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_ledc_int_map_msb, self.__pro_ledc_int_map_lsb, value)
class PRO_EFUSE_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x1b4
        self.__pro_efuse_int_map_lsb = 0
        self.__pro_efuse_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_efuse_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_efuse_int_map_msb, self.__pro_efuse_int_map_lsb)
    @pro_efuse_int_map.setter
    def pro_efuse_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_efuse_int_map_msb, self.__pro_efuse_int_map_lsb, value)
class PRO_CAN_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x1b8
        self.__pro_can_int_map_lsb = 0
        self.__pro_can_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_can_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_can_int_map_msb, self.__pro_can_int_map_lsb)
    @pro_can_int_map.setter
    def pro_can_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_can_int_map_msb, self.__pro_can_int_map_lsb, value)
class PRO_RTC_CORE_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x1bc
        self.__pro_rtc_core_intr_map_lsb = 0
        self.__pro_rtc_core_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_rtc_core_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_rtc_core_intr_map_msb, self.__pro_rtc_core_intr_map_lsb)
    @pro_rtc_core_intr_map.setter
    def pro_rtc_core_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_rtc_core_intr_map_msb, self.__pro_rtc_core_intr_map_lsb, value)
class PRO_RMT_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x1c0
        self.__pro_rmt_intr_map_lsb = 0
        self.__pro_rmt_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_rmt_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_rmt_intr_map_msb, self.__pro_rmt_intr_map_lsb)
    @pro_rmt_intr_map.setter
    def pro_rmt_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_rmt_intr_map_msb, self.__pro_rmt_intr_map_lsb, value)
class PRO_PCNT_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x1c4
        self.__pro_pcnt_intr_map_lsb = 0
        self.__pro_pcnt_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_pcnt_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_pcnt_intr_map_msb, self.__pro_pcnt_intr_map_lsb)
    @pro_pcnt_intr_map.setter
    def pro_pcnt_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_pcnt_intr_map_msb, self.__pro_pcnt_intr_map_lsb, value)
class PRO_I2C_EXT0_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x1c8
        self.__pro_i2c_ext0_intr_map_lsb = 0
        self.__pro_i2c_ext0_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_i2c_ext0_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_i2c_ext0_intr_map_msb, self.__pro_i2c_ext0_intr_map_lsb)
    @pro_i2c_ext0_intr_map.setter
    def pro_i2c_ext0_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_i2c_ext0_intr_map_msb, self.__pro_i2c_ext0_intr_map_lsb, value)
class PRO_I2C_EXT1_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x1cc
        self.__pro_i2c_ext1_intr_map_lsb = 0
        self.__pro_i2c_ext1_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_i2c_ext1_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_i2c_ext1_intr_map_msb, self.__pro_i2c_ext1_intr_map_lsb)
    @pro_i2c_ext1_intr_map.setter
    def pro_i2c_ext1_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_i2c_ext1_intr_map_msb, self.__pro_i2c_ext1_intr_map_lsb, value)
class PRO_RSA_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x1d0
        self.__pro_rsa_intr_map_lsb = 0
        self.__pro_rsa_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_rsa_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_rsa_intr_map_msb, self.__pro_rsa_intr_map_lsb)
    @pro_rsa_intr_map.setter
    def pro_rsa_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_rsa_intr_map_msb, self.__pro_rsa_intr_map_lsb, value)
class PRO_SPI1_DMA_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x1d4
        self.__pro_spi1_dma_int_map_lsb = 0
        self.__pro_spi1_dma_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_spi1_dma_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_spi1_dma_int_map_msb, self.__pro_spi1_dma_int_map_lsb)
    @pro_spi1_dma_int_map.setter
    def pro_spi1_dma_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_spi1_dma_int_map_msb, self.__pro_spi1_dma_int_map_lsb, value)
class PRO_SPI2_DMA_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x1d8
        self.__pro_spi2_dma_int_map_lsb = 0
        self.__pro_spi2_dma_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_spi2_dma_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_spi2_dma_int_map_msb, self.__pro_spi2_dma_int_map_lsb)
    @pro_spi2_dma_int_map.setter
    def pro_spi2_dma_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_spi2_dma_int_map_msb, self.__pro_spi2_dma_int_map_lsb, value)
class PRO_SPI3_DMA_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x1dc
        self.__pro_spi3_dma_int_map_lsb = 0
        self.__pro_spi3_dma_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_spi3_dma_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_spi3_dma_int_map_msb, self.__pro_spi3_dma_int_map_lsb)
    @pro_spi3_dma_int_map.setter
    def pro_spi3_dma_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_spi3_dma_int_map_msb, self.__pro_spi3_dma_int_map_lsb, value)
class PRO_WDG_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x1e0
        self.__pro_wdg_int_map_lsb = 0
        self.__pro_wdg_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_wdg_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_wdg_int_map_msb, self.__pro_wdg_int_map_lsb)
    @pro_wdg_int_map.setter
    def pro_wdg_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_wdg_int_map_msb, self.__pro_wdg_int_map_lsb, value)
class PRO_TIMER_INT1_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x1e4
        self.__pro_timer_int1_map_lsb = 0
        self.__pro_timer_int1_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_timer_int1_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_timer_int1_map_msb, self.__pro_timer_int1_map_lsb)
    @pro_timer_int1_map.setter
    def pro_timer_int1_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_timer_int1_map_msb, self.__pro_timer_int1_map_lsb, value)
class PRO_TIMER_INT2_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x1e8
        self.__pro_timer_int2_map_lsb = 0
        self.__pro_timer_int2_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_timer_int2_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_timer_int2_map_msb, self.__pro_timer_int2_map_lsb)
    @pro_timer_int2_map.setter
    def pro_timer_int2_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_timer_int2_map_msb, self.__pro_timer_int2_map_lsb, value)
class PRO_TG_T0_EDGE_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x1ec
        self.__pro_tg_t0_edge_int_map_lsb = 0
        self.__pro_tg_t0_edge_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_tg_t0_edge_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_tg_t0_edge_int_map_msb, self.__pro_tg_t0_edge_int_map_lsb)
    @pro_tg_t0_edge_int_map.setter
    def pro_tg_t0_edge_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_tg_t0_edge_int_map_msb, self.__pro_tg_t0_edge_int_map_lsb, value)
class PRO_TG_T1_EDGE_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x1f0
        self.__pro_tg_t1_edge_int_map_lsb = 0
        self.__pro_tg_t1_edge_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_tg_t1_edge_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_tg_t1_edge_int_map_msb, self.__pro_tg_t1_edge_int_map_lsb)
    @pro_tg_t1_edge_int_map.setter
    def pro_tg_t1_edge_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_tg_t1_edge_int_map_msb, self.__pro_tg_t1_edge_int_map_lsb, value)
class PRO_TG_WDT_EDGE_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x1f4
        self.__pro_tg_wdt_edge_int_map_lsb = 0
        self.__pro_tg_wdt_edge_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_tg_wdt_edge_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_tg_wdt_edge_int_map_msb, self.__pro_tg_wdt_edge_int_map_lsb)
    @pro_tg_wdt_edge_int_map.setter
    def pro_tg_wdt_edge_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_tg_wdt_edge_int_map_msb, self.__pro_tg_wdt_edge_int_map_lsb, value)
class PRO_TG_LACT_EDGE_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x1f8
        self.__pro_tg_lact_edge_int_map_lsb = 0
        self.__pro_tg_lact_edge_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_tg_lact_edge_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_tg_lact_edge_int_map_msb, self.__pro_tg_lact_edge_int_map_lsb)
    @pro_tg_lact_edge_int_map.setter
    def pro_tg_lact_edge_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_tg_lact_edge_int_map_msb, self.__pro_tg_lact_edge_int_map_lsb, value)
class PRO_TG1_T0_EDGE_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x1fc
        self.__pro_tg1_t0_edge_int_map_lsb = 0
        self.__pro_tg1_t0_edge_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_tg1_t0_edge_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_tg1_t0_edge_int_map_msb, self.__pro_tg1_t0_edge_int_map_lsb)
    @pro_tg1_t0_edge_int_map.setter
    def pro_tg1_t0_edge_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_tg1_t0_edge_int_map_msb, self.__pro_tg1_t0_edge_int_map_lsb, value)
class PRO_TG1_T1_EDGE_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x200
        self.__pro_tg1_t1_edge_int_map_lsb = 0
        self.__pro_tg1_t1_edge_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_tg1_t1_edge_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_tg1_t1_edge_int_map_msb, self.__pro_tg1_t1_edge_int_map_lsb)
    @pro_tg1_t1_edge_int_map.setter
    def pro_tg1_t1_edge_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_tg1_t1_edge_int_map_msb, self.__pro_tg1_t1_edge_int_map_lsb, value)
class PRO_TG1_WDT_EDGE_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x204
        self.__pro_tg1_wdt_edge_int_map_lsb = 0
        self.__pro_tg1_wdt_edge_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_tg1_wdt_edge_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_tg1_wdt_edge_int_map_msb, self.__pro_tg1_wdt_edge_int_map_lsb)
    @pro_tg1_wdt_edge_int_map.setter
    def pro_tg1_wdt_edge_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_tg1_wdt_edge_int_map_msb, self.__pro_tg1_wdt_edge_int_map_lsb, value)
class PRO_TG1_LACT_EDGE_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x208
        self.__pro_tg1_lact_edge_int_map_lsb = 0
        self.__pro_tg1_lact_edge_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_tg1_lact_edge_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_tg1_lact_edge_int_map_msb, self.__pro_tg1_lact_edge_int_map_lsb)
    @pro_tg1_lact_edge_int_map.setter
    def pro_tg1_lact_edge_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_tg1_lact_edge_int_map_msb, self.__pro_tg1_lact_edge_int_map_lsb, value)
class PRO_MMU_IA_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x20c
        self.__pro_mmu_ia_int_map_lsb = 0
        self.__pro_mmu_ia_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_mmu_ia_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_mmu_ia_int_map_msb, self.__pro_mmu_ia_int_map_lsb)
    @pro_mmu_ia_int_map.setter
    def pro_mmu_ia_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_mmu_ia_int_map_msb, self.__pro_mmu_ia_int_map_lsb, value)
class PRO_MPU_IA_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x210
        self.__pro_mpu_ia_int_map_lsb = 0
        self.__pro_mpu_ia_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_mpu_ia_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_mpu_ia_int_map_msb, self.__pro_mpu_ia_int_map_lsb)
    @pro_mpu_ia_int_map.setter
    def pro_mpu_ia_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_mpu_ia_int_map_msb, self.__pro_mpu_ia_int_map_lsb, value)
class PRO_CACHE_IA_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x214
        self.__pro_cache_ia_int_map_lsb = 0
        self.__pro_cache_ia_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_cache_ia_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_ia_int_map_msb, self.__pro_cache_ia_int_map_lsb)
    @pro_cache_ia_int_map.setter
    def pro_cache_ia_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_ia_int_map_msb, self.__pro_cache_ia_int_map_lsb, value)
class APP_MAC_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x218
        self.__app_mac_intr_map_lsb = 0
        self.__app_mac_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_mac_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_mac_intr_map_msb, self.__app_mac_intr_map_lsb)
    @app_mac_intr_map.setter
    def app_mac_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_mac_intr_map_msb, self.__app_mac_intr_map_lsb, value)
class APP_MAC_NMI_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x21c
        self.__app_mac_nmi_map_lsb = 0
        self.__app_mac_nmi_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_mac_nmi_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_mac_nmi_map_msb, self.__app_mac_nmi_map_lsb)
    @app_mac_nmi_map.setter
    def app_mac_nmi_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_mac_nmi_map_msb, self.__app_mac_nmi_map_lsb, value)
class APP_BB_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x220
        self.__app_bb_int_map_lsb = 0
        self.__app_bb_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_bb_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_bb_int_map_msb, self.__app_bb_int_map_lsb)
    @app_bb_int_map.setter
    def app_bb_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_bb_int_map_msb, self.__app_bb_int_map_lsb, value)
class APP_BT_MAC_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x224
        self.__app_bt_mac_int_map_lsb = 0
        self.__app_bt_mac_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_bt_mac_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_bt_mac_int_map_msb, self.__app_bt_mac_int_map_lsb)
    @app_bt_mac_int_map.setter
    def app_bt_mac_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_bt_mac_int_map_msb, self.__app_bt_mac_int_map_lsb, value)
class APP_BT_BB_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x228
        self.__app_bt_bb_int_map_lsb = 0
        self.__app_bt_bb_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_bt_bb_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_bt_bb_int_map_msb, self.__app_bt_bb_int_map_lsb)
    @app_bt_bb_int_map.setter
    def app_bt_bb_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_bt_bb_int_map_msb, self.__app_bt_bb_int_map_lsb, value)
class APP_BT_BB_NMI_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x22c
        self.__app_bt_bb_nmi_map_lsb = 0
        self.__app_bt_bb_nmi_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_bt_bb_nmi_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_bt_bb_nmi_map_msb, self.__app_bt_bb_nmi_map_lsb)
    @app_bt_bb_nmi_map.setter
    def app_bt_bb_nmi_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_bt_bb_nmi_map_msb, self.__app_bt_bb_nmi_map_lsb, value)
class APP_RWBT_IRQ_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x230
        self.__app_rwbt_irq_map_lsb = 0
        self.__app_rwbt_irq_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_rwbt_irq_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_rwbt_irq_map_msb, self.__app_rwbt_irq_map_lsb)
    @app_rwbt_irq_map.setter
    def app_rwbt_irq_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_rwbt_irq_map_msb, self.__app_rwbt_irq_map_lsb, value)
class APP_RWBLE_IRQ_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x234
        self.__app_rwble_irq_map_lsb = 0
        self.__app_rwble_irq_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_rwble_irq_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_rwble_irq_map_msb, self.__app_rwble_irq_map_lsb)
    @app_rwble_irq_map.setter
    def app_rwble_irq_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_rwble_irq_map_msb, self.__app_rwble_irq_map_lsb, value)
class APP_RWBT_NMI_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x238
        self.__app_rwbt_nmi_map_lsb = 0
        self.__app_rwbt_nmi_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_rwbt_nmi_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_rwbt_nmi_map_msb, self.__app_rwbt_nmi_map_lsb)
    @app_rwbt_nmi_map.setter
    def app_rwbt_nmi_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_rwbt_nmi_map_msb, self.__app_rwbt_nmi_map_lsb, value)
class APP_RWBLE_NMI_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x23c
        self.__app_rwble_nmi_map_lsb = 0
        self.__app_rwble_nmi_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_rwble_nmi_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_rwble_nmi_map_msb, self.__app_rwble_nmi_map_lsb)
    @app_rwble_nmi_map.setter
    def app_rwble_nmi_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_rwble_nmi_map_msb, self.__app_rwble_nmi_map_lsb, value)
class APP_SLC0_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x240
        self.__app_slc0_intr_map_lsb = 0
        self.__app_slc0_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_slc0_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_slc0_intr_map_msb, self.__app_slc0_intr_map_lsb)
    @app_slc0_intr_map.setter
    def app_slc0_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_slc0_intr_map_msb, self.__app_slc0_intr_map_lsb, value)
class APP_SLC1_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x244
        self.__app_slc1_intr_map_lsb = 0
        self.__app_slc1_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_slc1_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_slc1_intr_map_msb, self.__app_slc1_intr_map_lsb)
    @app_slc1_intr_map.setter
    def app_slc1_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_slc1_intr_map_msb, self.__app_slc1_intr_map_lsb, value)
class APP_UHCI0_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x248
        self.__app_uhci0_intr_map_lsb = 0
        self.__app_uhci0_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_uhci0_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_uhci0_intr_map_msb, self.__app_uhci0_intr_map_lsb)
    @app_uhci0_intr_map.setter
    def app_uhci0_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_uhci0_intr_map_msb, self.__app_uhci0_intr_map_lsb, value)
class APP_UHCI1_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x24c
        self.__app_uhci1_intr_map_lsb = 0
        self.__app_uhci1_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_uhci1_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_uhci1_intr_map_msb, self.__app_uhci1_intr_map_lsb)
    @app_uhci1_intr_map.setter
    def app_uhci1_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_uhci1_intr_map_msb, self.__app_uhci1_intr_map_lsb, value)
class APP_TG_T0_LEVEL_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x250
        self.__app_tg_t0_level_int_map_lsb = 0
        self.__app_tg_t0_level_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_tg_t0_level_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_tg_t0_level_int_map_msb, self.__app_tg_t0_level_int_map_lsb)
    @app_tg_t0_level_int_map.setter
    def app_tg_t0_level_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_tg_t0_level_int_map_msb, self.__app_tg_t0_level_int_map_lsb, value)
class APP_TG_T1_LEVEL_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x254
        self.__app_tg_t1_level_int_map_lsb = 0
        self.__app_tg_t1_level_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_tg_t1_level_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_tg_t1_level_int_map_msb, self.__app_tg_t1_level_int_map_lsb)
    @app_tg_t1_level_int_map.setter
    def app_tg_t1_level_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_tg_t1_level_int_map_msb, self.__app_tg_t1_level_int_map_lsb, value)
class APP_TG_WDT_LEVEL_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x258
        self.__app_tg_wdt_level_int_map_lsb = 0
        self.__app_tg_wdt_level_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_tg_wdt_level_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_tg_wdt_level_int_map_msb, self.__app_tg_wdt_level_int_map_lsb)
    @app_tg_wdt_level_int_map.setter
    def app_tg_wdt_level_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_tg_wdt_level_int_map_msb, self.__app_tg_wdt_level_int_map_lsb, value)
class APP_TG_LACT_LEVEL_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x25c
        self.__app_tg_lact_level_int_map_lsb = 0
        self.__app_tg_lact_level_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_tg_lact_level_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_tg_lact_level_int_map_msb, self.__app_tg_lact_level_int_map_lsb)
    @app_tg_lact_level_int_map.setter
    def app_tg_lact_level_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_tg_lact_level_int_map_msb, self.__app_tg_lact_level_int_map_lsb, value)
class APP_TG1_T0_LEVEL_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x260
        self.__app_tg1_t0_level_int_map_lsb = 0
        self.__app_tg1_t0_level_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_tg1_t0_level_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_tg1_t0_level_int_map_msb, self.__app_tg1_t0_level_int_map_lsb)
    @app_tg1_t0_level_int_map.setter
    def app_tg1_t0_level_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_tg1_t0_level_int_map_msb, self.__app_tg1_t0_level_int_map_lsb, value)
class APP_TG1_T1_LEVEL_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x264
        self.__app_tg1_t1_level_int_map_lsb = 0
        self.__app_tg1_t1_level_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_tg1_t1_level_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_tg1_t1_level_int_map_msb, self.__app_tg1_t1_level_int_map_lsb)
    @app_tg1_t1_level_int_map.setter
    def app_tg1_t1_level_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_tg1_t1_level_int_map_msb, self.__app_tg1_t1_level_int_map_lsb, value)
class APP_TG1_WDT_LEVEL_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x268
        self.__app_tg1_wdt_level_int_map_lsb = 0
        self.__app_tg1_wdt_level_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_tg1_wdt_level_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_tg1_wdt_level_int_map_msb, self.__app_tg1_wdt_level_int_map_lsb)
    @app_tg1_wdt_level_int_map.setter
    def app_tg1_wdt_level_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_tg1_wdt_level_int_map_msb, self.__app_tg1_wdt_level_int_map_lsb, value)
class APP_TG1_LACT_LEVEL_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x26c
        self.__app_tg1_lact_level_int_map_lsb = 0
        self.__app_tg1_lact_level_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_tg1_lact_level_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_tg1_lact_level_int_map_msb, self.__app_tg1_lact_level_int_map_lsb)
    @app_tg1_lact_level_int_map.setter
    def app_tg1_lact_level_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_tg1_lact_level_int_map_msb, self.__app_tg1_lact_level_int_map_lsb, value)
class APP_GPIO_INTERRUPT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x270
        self.__app_gpio_interrupt_app_map_lsb = 0
        self.__app_gpio_interrupt_app_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_gpio_interrupt_app_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_gpio_interrupt_app_map_msb, self.__app_gpio_interrupt_app_map_lsb)
    @app_gpio_interrupt_app_map.setter
    def app_gpio_interrupt_app_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_gpio_interrupt_app_map_msb, self.__app_gpio_interrupt_app_map_lsb, value)
class APP_GPIO_INTERRUPT_NMI_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x274
        self.__app_gpio_interrupt_app_nmi_map_lsb = 0
        self.__app_gpio_interrupt_app_nmi_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_gpio_interrupt_app_nmi_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_gpio_interrupt_app_nmi_map_msb, self.__app_gpio_interrupt_app_nmi_map_lsb)
    @app_gpio_interrupt_app_nmi_map.setter
    def app_gpio_interrupt_app_nmi_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_gpio_interrupt_app_nmi_map_msb, self.__app_gpio_interrupt_app_nmi_map_lsb, value)
class APP_CPU_INTR_FROM_CPU_0_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x278
        self.__app_cpu_intr_from_cpu_0_map_lsb = 0
        self.__app_cpu_intr_from_cpu_0_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_cpu_intr_from_cpu_0_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_cpu_intr_from_cpu_0_map_msb, self.__app_cpu_intr_from_cpu_0_map_lsb)
    @app_cpu_intr_from_cpu_0_map.setter
    def app_cpu_intr_from_cpu_0_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cpu_intr_from_cpu_0_map_msb, self.__app_cpu_intr_from_cpu_0_map_lsb, value)
class APP_CPU_INTR_FROM_CPU_1_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x27c
        self.__app_cpu_intr_from_cpu_1_map_lsb = 0
        self.__app_cpu_intr_from_cpu_1_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_cpu_intr_from_cpu_1_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_cpu_intr_from_cpu_1_map_msb, self.__app_cpu_intr_from_cpu_1_map_lsb)
    @app_cpu_intr_from_cpu_1_map.setter
    def app_cpu_intr_from_cpu_1_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cpu_intr_from_cpu_1_map_msb, self.__app_cpu_intr_from_cpu_1_map_lsb, value)
class APP_CPU_INTR_FROM_CPU_2_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x280
        self.__app_cpu_intr_from_cpu_2_map_lsb = 0
        self.__app_cpu_intr_from_cpu_2_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_cpu_intr_from_cpu_2_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_cpu_intr_from_cpu_2_map_msb, self.__app_cpu_intr_from_cpu_2_map_lsb)
    @app_cpu_intr_from_cpu_2_map.setter
    def app_cpu_intr_from_cpu_2_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cpu_intr_from_cpu_2_map_msb, self.__app_cpu_intr_from_cpu_2_map_lsb, value)
class APP_CPU_INTR_FROM_CPU_3_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x284
        self.__app_cpu_intr_from_cpu_3_map_lsb = 0
        self.__app_cpu_intr_from_cpu_3_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_cpu_intr_from_cpu_3_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_cpu_intr_from_cpu_3_map_msb, self.__app_cpu_intr_from_cpu_3_map_lsb)
    @app_cpu_intr_from_cpu_3_map.setter
    def app_cpu_intr_from_cpu_3_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cpu_intr_from_cpu_3_map_msb, self.__app_cpu_intr_from_cpu_3_map_lsb, value)
class APP_SPI_INTR_0_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x288
        self.__app_spi_intr_0_map_lsb = 0
        self.__app_spi_intr_0_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_spi_intr_0_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_spi_intr_0_map_msb, self.__app_spi_intr_0_map_lsb)
    @app_spi_intr_0_map.setter
    def app_spi_intr_0_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_spi_intr_0_map_msb, self.__app_spi_intr_0_map_lsb, value)
class APP_SPI_INTR_1_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x28c
        self.__app_spi_intr_1_map_lsb = 0
        self.__app_spi_intr_1_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_spi_intr_1_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_spi_intr_1_map_msb, self.__app_spi_intr_1_map_lsb)
    @app_spi_intr_1_map.setter
    def app_spi_intr_1_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_spi_intr_1_map_msb, self.__app_spi_intr_1_map_lsb, value)
class APP_SPI_INTR_2_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x290
        self.__app_spi_intr_2_map_lsb = 0
        self.__app_spi_intr_2_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_spi_intr_2_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_spi_intr_2_map_msb, self.__app_spi_intr_2_map_lsb)
    @app_spi_intr_2_map.setter
    def app_spi_intr_2_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_spi_intr_2_map_msb, self.__app_spi_intr_2_map_lsb, value)
class APP_SPI_INTR_3_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x294
        self.__app_spi_intr_3_map_lsb = 0
        self.__app_spi_intr_3_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_spi_intr_3_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_spi_intr_3_map_msb, self.__app_spi_intr_3_map_lsb)
    @app_spi_intr_3_map.setter
    def app_spi_intr_3_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_spi_intr_3_map_msb, self.__app_spi_intr_3_map_lsb, value)
class APP_I2S0_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x298
        self.__app_i2s0_int_map_lsb = 0
        self.__app_i2s0_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_i2s0_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_i2s0_int_map_msb, self.__app_i2s0_int_map_lsb)
    @app_i2s0_int_map.setter
    def app_i2s0_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_i2s0_int_map_msb, self.__app_i2s0_int_map_lsb, value)
class APP_I2S1_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x29c
        self.__app_i2s1_int_map_lsb = 0
        self.__app_i2s1_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_i2s1_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_i2s1_int_map_msb, self.__app_i2s1_int_map_lsb)
    @app_i2s1_int_map.setter
    def app_i2s1_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_i2s1_int_map_msb, self.__app_i2s1_int_map_lsb, value)
class APP_UART_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x2a0
        self.__app_uart_intr_map_lsb = 0
        self.__app_uart_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_uart_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_uart_intr_map_msb, self.__app_uart_intr_map_lsb)
    @app_uart_intr_map.setter
    def app_uart_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_uart_intr_map_msb, self.__app_uart_intr_map_lsb, value)
class APP_UART1_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x2a4
        self.__app_uart1_intr_map_lsb = 0
        self.__app_uart1_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_uart1_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_uart1_intr_map_msb, self.__app_uart1_intr_map_lsb)
    @app_uart1_intr_map.setter
    def app_uart1_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_uart1_intr_map_msb, self.__app_uart1_intr_map_lsb, value)
class APP_UART2_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x2a8
        self.__app_uart2_intr_map_lsb = 0
        self.__app_uart2_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_uart2_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_uart2_intr_map_msb, self.__app_uart2_intr_map_lsb)
    @app_uart2_intr_map.setter
    def app_uart2_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_uart2_intr_map_msb, self.__app_uart2_intr_map_lsb, value)
class APP_SDIO_HOST_INTERRUPT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x2ac
        self.__app_sdio_host_interrupt_map_lsb = 0
        self.__app_sdio_host_interrupt_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_sdio_host_interrupt_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_sdio_host_interrupt_map_msb, self.__app_sdio_host_interrupt_map_lsb)
    @app_sdio_host_interrupt_map.setter
    def app_sdio_host_interrupt_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_sdio_host_interrupt_map_msb, self.__app_sdio_host_interrupt_map_lsb, value)
class APP_EMAC_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x2b0
        self.__app_emac_int_map_lsb = 0
        self.__app_emac_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_emac_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_emac_int_map_msb, self.__app_emac_int_map_lsb)
    @app_emac_int_map.setter
    def app_emac_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_emac_int_map_msb, self.__app_emac_int_map_lsb, value)
class APP_PWM0_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x2b4
        self.__app_pwm0_intr_map_lsb = 0
        self.__app_pwm0_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_pwm0_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_pwm0_intr_map_msb, self.__app_pwm0_intr_map_lsb)
    @app_pwm0_intr_map.setter
    def app_pwm0_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_pwm0_intr_map_msb, self.__app_pwm0_intr_map_lsb, value)
class APP_PWM1_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x2b8
        self.__app_pwm1_intr_map_lsb = 0
        self.__app_pwm1_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_pwm1_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_pwm1_intr_map_msb, self.__app_pwm1_intr_map_lsb)
    @app_pwm1_intr_map.setter
    def app_pwm1_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_pwm1_intr_map_msb, self.__app_pwm1_intr_map_lsb, value)
class APP_PWM2_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x2bc
        self.__app_pwm2_intr_map_lsb = 0
        self.__app_pwm2_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_pwm2_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_pwm2_intr_map_msb, self.__app_pwm2_intr_map_lsb)
    @app_pwm2_intr_map.setter
    def app_pwm2_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_pwm2_intr_map_msb, self.__app_pwm2_intr_map_lsb, value)
class APP_PWM3_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x2c0
        self.__app_pwm3_intr_map_lsb = 0
        self.__app_pwm3_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_pwm3_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_pwm3_intr_map_msb, self.__app_pwm3_intr_map_lsb)
    @app_pwm3_intr_map.setter
    def app_pwm3_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_pwm3_intr_map_msb, self.__app_pwm3_intr_map_lsb, value)
class APP_LEDC_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x2c4
        self.__app_ledc_int_map_lsb = 0
        self.__app_ledc_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_ledc_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_ledc_int_map_msb, self.__app_ledc_int_map_lsb)
    @app_ledc_int_map.setter
    def app_ledc_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_ledc_int_map_msb, self.__app_ledc_int_map_lsb, value)
class APP_EFUSE_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x2c8
        self.__app_efuse_int_map_lsb = 0
        self.__app_efuse_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_efuse_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_efuse_int_map_msb, self.__app_efuse_int_map_lsb)
    @app_efuse_int_map.setter
    def app_efuse_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_efuse_int_map_msb, self.__app_efuse_int_map_lsb, value)
class APP_CAN_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x2cc
        self.__app_can_int_map_lsb = 0
        self.__app_can_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_can_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_can_int_map_msb, self.__app_can_int_map_lsb)
    @app_can_int_map.setter
    def app_can_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_can_int_map_msb, self.__app_can_int_map_lsb, value)
class APP_RTC_CORE_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x2d0
        self.__app_rtc_core_intr_map_lsb = 0
        self.__app_rtc_core_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_rtc_core_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_rtc_core_intr_map_msb, self.__app_rtc_core_intr_map_lsb)
    @app_rtc_core_intr_map.setter
    def app_rtc_core_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_rtc_core_intr_map_msb, self.__app_rtc_core_intr_map_lsb, value)
class APP_RMT_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x2d4
        self.__app_rmt_intr_map_lsb = 0
        self.__app_rmt_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_rmt_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_rmt_intr_map_msb, self.__app_rmt_intr_map_lsb)
    @app_rmt_intr_map.setter
    def app_rmt_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_rmt_intr_map_msb, self.__app_rmt_intr_map_lsb, value)
class APP_PCNT_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x2d8
        self.__app_pcnt_intr_map_lsb = 0
        self.__app_pcnt_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_pcnt_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_pcnt_intr_map_msb, self.__app_pcnt_intr_map_lsb)
    @app_pcnt_intr_map.setter
    def app_pcnt_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_pcnt_intr_map_msb, self.__app_pcnt_intr_map_lsb, value)
class APP_I2C_EXT0_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x2dc
        self.__app_i2c_ext0_intr_map_lsb = 0
        self.__app_i2c_ext0_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_i2c_ext0_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_i2c_ext0_intr_map_msb, self.__app_i2c_ext0_intr_map_lsb)
    @app_i2c_ext0_intr_map.setter
    def app_i2c_ext0_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_i2c_ext0_intr_map_msb, self.__app_i2c_ext0_intr_map_lsb, value)
class APP_I2C_EXT1_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x2e0
        self.__app_i2c_ext1_intr_map_lsb = 0
        self.__app_i2c_ext1_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_i2c_ext1_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_i2c_ext1_intr_map_msb, self.__app_i2c_ext1_intr_map_lsb)
    @app_i2c_ext1_intr_map.setter
    def app_i2c_ext1_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_i2c_ext1_intr_map_msb, self.__app_i2c_ext1_intr_map_lsb, value)
class APP_RSA_INTR_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x2e4
        self.__app_rsa_intr_map_lsb = 0
        self.__app_rsa_intr_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_rsa_intr_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_rsa_intr_map_msb, self.__app_rsa_intr_map_lsb)
    @app_rsa_intr_map.setter
    def app_rsa_intr_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_rsa_intr_map_msb, self.__app_rsa_intr_map_lsb, value)
class APP_SPI1_DMA_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x2e8
        self.__app_spi1_dma_int_map_lsb = 0
        self.__app_spi1_dma_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_spi1_dma_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_spi1_dma_int_map_msb, self.__app_spi1_dma_int_map_lsb)
    @app_spi1_dma_int_map.setter
    def app_spi1_dma_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_spi1_dma_int_map_msb, self.__app_spi1_dma_int_map_lsb, value)
class APP_SPI2_DMA_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x2ec
        self.__app_spi2_dma_int_map_lsb = 0
        self.__app_spi2_dma_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_spi2_dma_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_spi2_dma_int_map_msb, self.__app_spi2_dma_int_map_lsb)
    @app_spi2_dma_int_map.setter
    def app_spi2_dma_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_spi2_dma_int_map_msb, self.__app_spi2_dma_int_map_lsb, value)
class APP_SPI3_DMA_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x2f0
        self.__app_spi3_dma_int_map_lsb = 0
        self.__app_spi3_dma_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_spi3_dma_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_spi3_dma_int_map_msb, self.__app_spi3_dma_int_map_lsb)
    @app_spi3_dma_int_map.setter
    def app_spi3_dma_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_spi3_dma_int_map_msb, self.__app_spi3_dma_int_map_lsb, value)
class APP_WDG_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x2f4
        self.__app_wdg_int_map_lsb = 0
        self.__app_wdg_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_wdg_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_wdg_int_map_msb, self.__app_wdg_int_map_lsb)
    @app_wdg_int_map.setter
    def app_wdg_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_wdg_int_map_msb, self.__app_wdg_int_map_lsb, value)
class APP_TIMER_INT1_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x2f8
        self.__app_timer_int1_map_lsb = 0
        self.__app_timer_int1_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_timer_int1_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_timer_int1_map_msb, self.__app_timer_int1_map_lsb)
    @app_timer_int1_map.setter
    def app_timer_int1_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_timer_int1_map_msb, self.__app_timer_int1_map_lsb, value)
class APP_TIMER_INT2_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x2fc
        self.__app_timer_int2_map_lsb = 0
        self.__app_timer_int2_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_timer_int2_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_timer_int2_map_msb, self.__app_timer_int2_map_lsb)
    @app_timer_int2_map.setter
    def app_timer_int2_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_timer_int2_map_msb, self.__app_timer_int2_map_lsb, value)
class APP_TG_T0_EDGE_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x300
        self.__app_tg_t0_edge_int_map_lsb = 0
        self.__app_tg_t0_edge_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_tg_t0_edge_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_tg_t0_edge_int_map_msb, self.__app_tg_t0_edge_int_map_lsb)
    @app_tg_t0_edge_int_map.setter
    def app_tg_t0_edge_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_tg_t0_edge_int_map_msb, self.__app_tg_t0_edge_int_map_lsb, value)
class APP_TG_T1_EDGE_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x304
        self.__app_tg_t1_edge_int_map_lsb = 0
        self.__app_tg_t1_edge_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_tg_t1_edge_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_tg_t1_edge_int_map_msb, self.__app_tg_t1_edge_int_map_lsb)
    @app_tg_t1_edge_int_map.setter
    def app_tg_t1_edge_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_tg_t1_edge_int_map_msb, self.__app_tg_t1_edge_int_map_lsb, value)
class APP_TG_WDT_EDGE_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x308
        self.__app_tg_wdt_edge_int_map_lsb = 0
        self.__app_tg_wdt_edge_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_tg_wdt_edge_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_tg_wdt_edge_int_map_msb, self.__app_tg_wdt_edge_int_map_lsb)
    @app_tg_wdt_edge_int_map.setter
    def app_tg_wdt_edge_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_tg_wdt_edge_int_map_msb, self.__app_tg_wdt_edge_int_map_lsb, value)
class APP_TG_LACT_EDGE_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x30c
        self.__app_tg_lact_edge_int_map_lsb = 0
        self.__app_tg_lact_edge_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_tg_lact_edge_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_tg_lact_edge_int_map_msb, self.__app_tg_lact_edge_int_map_lsb)
    @app_tg_lact_edge_int_map.setter
    def app_tg_lact_edge_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_tg_lact_edge_int_map_msb, self.__app_tg_lact_edge_int_map_lsb, value)
class APP_TG1_T0_EDGE_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x310
        self.__app_tg1_t0_edge_int_map_lsb = 0
        self.__app_tg1_t0_edge_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_tg1_t0_edge_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_tg1_t0_edge_int_map_msb, self.__app_tg1_t0_edge_int_map_lsb)
    @app_tg1_t0_edge_int_map.setter
    def app_tg1_t0_edge_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_tg1_t0_edge_int_map_msb, self.__app_tg1_t0_edge_int_map_lsb, value)
class APP_TG1_T1_EDGE_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x314
        self.__app_tg1_t1_edge_int_map_lsb = 0
        self.__app_tg1_t1_edge_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_tg1_t1_edge_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_tg1_t1_edge_int_map_msb, self.__app_tg1_t1_edge_int_map_lsb)
    @app_tg1_t1_edge_int_map.setter
    def app_tg1_t1_edge_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_tg1_t1_edge_int_map_msb, self.__app_tg1_t1_edge_int_map_lsb, value)
class APP_TG1_WDT_EDGE_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x318
        self.__app_tg1_wdt_edge_int_map_lsb = 0
        self.__app_tg1_wdt_edge_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_tg1_wdt_edge_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_tg1_wdt_edge_int_map_msb, self.__app_tg1_wdt_edge_int_map_lsb)
    @app_tg1_wdt_edge_int_map.setter
    def app_tg1_wdt_edge_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_tg1_wdt_edge_int_map_msb, self.__app_tg1_wdt_edge_int_map_lsb, value)
class APP_TG1_LACT_EDGE_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x31c
        self.__app_tg1_lact_edge_int_map_lsb = 0
        self.__app_tg1_lact_edge_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_tg1_lact_edge_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_tg1_lact_edge_int_map_msb, self.__app_tg1_lact_edge_int_map_lsb)
    @app_tg1_lact_edge_int_map.setter
    def app_tg1_lact_edge_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_tg1_lact_edge_int_map_msb, self.__app_tg1_lact_edge_int_map_lsb, value)
class APP_MMU_IA_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x320
        self.__app_mmu_ia_int_map_lsb = 0
        self.__app_mmu_ia_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_mmu_ia_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_mmu_ia_int_map_msb, self.__app_mmu_ia_int_map_lsb)
    @app_mmu_ia_int_map.setter
    def app_mmu_ia_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_mmu_ia_int_map_msb, self.__app_mmu_ia_int_map_lsb, value)
class APP_MPU_IA_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x324
        self.__app_mpu_ia_int_map_lsb = 0
        self.__app_mpu_ia_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_mpu_ia_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_mpu_ia_int_map_msb, self.__app_mpu_ia_int_map_lsb)
    @app_mpu_ia_int_map.setter
    def app_mpu_ia_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_mpu_ia_int_map_msb, self.__app_mpu_ia_int_map_lsb, value)
class APP_CACHE_IA_INT_MAP_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x328
        self.__app_cache_ia_int_map_lsb = 0
        self.__app_cache_ia_int_map_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_cache_ia_int_map(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_ia_int_map_msb, self.__app_cache_ia_int_map_lsb)
    @app_cache_ia_int_map.setter
    def app_cache_ia_int_map(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_ia_int_map_msb, self.__app_cache_ia_int_map_lsb, value)
class AHBLITE_MPU_TABLE_UART(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x32c
        self.__uart_access_grant_config_lsb = 0
        self.__uart_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def uart_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__uart_access_grant_config_msb, self.__uart_access_grant_config_lsb)
    @uart_access_grant_config.setter
    def uart_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_access_grant_config_msb, self.__uart_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_SPI1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x330
        self.__spi1_access_grant_config_lsb = 0
        self.__spi1_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def spi1_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__spi1_access_grant_config_msb, self.__spi1_access_grant_config_lsb)
    @spi1_access_grant_config.setter
    def spi1_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi1_access_grant_config_msb, self.__spi1_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_SPI0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x334
        self.__spi0_access_grant_config_lsb = 0
        self.__spi0_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def spi0_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__spi0_access_grant_config_msb, self.__spi0_access_grant_config_lsb)
    @spi0_access_grant_config.setter
    def spi0_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi0_access_grant_config_msb, self.__spi0_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_GPIO(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x338
        self.__gpio_access_grant_config_lsb = 0
        self.__gpio_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def gpio_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__gpio_access_grant_config_msb, self.__gpio_access_grant_config_lsb)
    @gpio_access_grant_config.setter
    def gpio_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__gpio_access_grant_config_msb, self.__gpio_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_FE2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x33c
        self.__fe2_access_grant_config_lsb = 0
        self.__fe2_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def fe2_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__fe2_access_grant_config_msb, self.__fe2_access_grant_config_lsb)
    @fe2_access_grant_config.setter
    def fe2_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__fe2_access_grant_config_msb, self.__fe2_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_FE(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x340
        self.__fe_access_grant_config_lsb = 0
        self.__fe_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def fe_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__fe_access_grant_config_msb, self.__fe_access_grant_config_lsb)
    @fe_access_grant_config.setter
    def fe_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__fe_access_grant_config_msb, self.__fe_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_TIMER(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x344
        self.__timer_access_grant_config_lsb = 0
        self.__timer_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def timer_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__timer_access_grant_config_msb, self.__timer_access_grant_config_lsb)
    @timer_access_grant_config.setter
    def timer_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__timer_access_grant_config_msb, self.__timer_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_RTC(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x348
        self.__rtc_access_grant_config_lsb = 0
        self.__rtc_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_access_grant_config_msb, self.__rtc_access_grant_config_lsb)
    @rtc_access_grant_config.setter
    def rtc_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_access_grant_config_msb, self.__rtc_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_IO_MUX(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x34c
        self.__iomux_access_grant_config_lsb = 0
        self.__iomux_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def iomux_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__iomux_access_grant_config_msb, self.__iomux_access_grant_config_lsb)
    @iomux_access_grant_config.setter
    def iomux_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__iomux_access_grant_config_msb, self.__iomux_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_WDG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x350
        self.__wdg_access_grant_config_lsb = 0
        self.__wdg_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def wdg_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__wdg_access_grant_config_msb, self.__wdg_access_grant_config_lsb)
    @wdg_access_grant_config.setter
    def wdg_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__wdg_access_grant_config_msb, self.__wdg_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_HINF(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x354
        self.__hinf_access_grant_config_lsb = 0
        self.__hinf_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def hinf_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__hinf_access_grant_config_msb, self.__hinf_access_grant_config_lsb)
    @hinf_access_grant_config.setter
    def hinf_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__hinf_access_grant_config_msb, self.__hinf_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_UHCI1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x358
        self.__uhci1_access_grant_config_lsb = 0
        self.__uhci1_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def uhci1_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__uhci1_access_grant_config_msb, self.__uhci1_access_grant_config_lsb)
    @uhci1_access_grant_config.setter
    def uhci1_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__uhci1_access_grant_config_msb, self.__uhci1_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_MISC(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x35c
        self.__misc_access_grant_config_lsb = 0
        self.__misc_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def misc_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__misc_access_grant_config_msb, self.__misc_access_grant_config_lsb)
    @misc_access_grant_config.setter
    def misc_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__misc_access_grant_config_msb, self.__misc_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_I2C(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x360
        self.__i2c_access_grant_config_lsb = 0
        self.__i2c_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2c_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__i2c_access_grant_config_msb, self.__i2c_access_grant_config_lsb)
    @i2c_access_grant_config.setter
    def i2c_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2c_access_grant_config_msb, self.__i2c_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_I2S0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x364
        self.__i2s0_access_grant_config_lsb = 0
        self.__i2s0_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s0_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__i2s0_access_grant_config_msb, self.__i2s0_access_grant_config_lsb)
    @i2s0_access_grant_config.setter
    def i2s0_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s0_access_grant_config_msb, self.__i2s0_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_UART1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x368
        self.__uart1_access_grant_config_lsb = 0
        self.__uart1_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def uart1_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__uart1_access_grant_config_msb, self.__uart1_access_grant_config_lsb)
    @uart1_access_grant_config.setter
    def uart1_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart1_access_grant_config_msb, self.__uart1_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_BT(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x36c
        self.__bt_access_grant_config_lsb = 0
        self.__bt_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def bt_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__bt_access_grant_config_msb, self.__bt_access_grant_config_lsb)
    @bt_access_grant_config.setter
    def bt_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__bt_access_grant_config_msb, self.__bt_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_BT_BUFFER(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x370
        self.__btbuffer_access_grant_config_lsb = 0
        self.__btbuffer_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def btbuffer_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__btbuffer_access_grant_config_msb, self.__btbuffer_access_grant_config_lsb)
    @btbuffer_access_grant_config.setter
    def btbuffer_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__btbuffer_access_grant_config_msb, self.__btbuffer_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_I2C_EXT0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x374
        self.__i2cext0_access_grant_config_lsb = 0
        self.__i2cext0_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2cext0_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__i2cext0_access_grant_config_msb, self.__i2cext0_access_grant_config_lsb)
    @i2cext0_access_grant_config.setter
    def i2cext0_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2cext0_access_grant_config_msb, self.__i2cext0_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_UHCI0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x378
        self.__uhci0_access_grant_config_lsb = 0
        self.__uhci0_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def uhci0_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__uhci0_access_grant_config_msb, self.__uhci0_access_grant_config_lsb)
    @uhci0_access_grant_config.setter
    def uhci0_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__uhci0_access_grant_config_msb, self.__uhci0_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_SLCHOST(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x37c
        self.__slchost_access_grant_config_lsb = 0
        self.__slchost_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def slchost_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__slchost_access_grant_config_msb, self.__slchost_access_grant_config_lsb)
    @slchost_access_grant_config.setter
    def slchost_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__slchost_access_grant_config_msb, self.__slchost_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_RMT(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x380
        self.__rmt_access_grant_config_lsb = 0
        self.__rmt_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rmt_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__rmt_access_grant_config_msb, self.__rmt_access_grant_config_lsb)
    @rmt_access_grant_config.setter
    def rmt_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__rmt_access_grant_config_msb, self.__rmt_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_PCNT(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x384
        self.__pcnt_access_grant_config_lsb = 0
        self.__pcnt_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pcnt_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__pcnt_access_grant_config_msb, self.__pcnt_access_grant_config_lsb)
    @pcnt_access_grant_config.setter
    def pcnt_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__pcnt_access_grant_config_msb, self.__pcnt_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_SLC(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x388
        self.__slc_access_grant_config_lsb = 0
        self.__slc_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def slc_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__slc_access_grant_config_msb, self.__slc_access_grant_config_lsb)
    @slc_access_grant_config.setter
    def slc_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__slc_access_grant_config_msb, self.__slc_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_LEDC(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x38c
        self.__ledc_access_grant_config_lsb = 0
        self.__ledc_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def ledc_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__ledc_access_grant_config_msb, self.__ledc_access_grant_config_lsb)
    @ledc_access_grant_config.setter
    def ledc_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__ledc_access_grant_config_msb, self.__ledc_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_EFUSE(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x390
        self.__efuse_access_grant_config_lsb = 0
        self.__efuse_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_access_grant_config_msb, self.__efuse_access_grant_config_lsb)
    @efuse_access_grant_config.setter
    def efuse_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_access_grant_config_msb, self.__efuse_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_SPI_ENCRYPT(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x394
        self.__spi_encrypy_access_grant_config_lsb = 0
        self.__spi_encrypy_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def spi_encrypy_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__spi_encrypy_access_grant_config_msb, self.__spi_encrypy_access_grant_config_lsb)
    @spi_encrypy_access_grant_config.setter
    def spi_encrypy_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi_encrypy_access_grant_config_msb, self.__spi_encrypy_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_BB(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x398
        self.__bb_access_grant_config_lsb = 0
        self.__bb_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def bb_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__bb_access_grant_config_msb, self.__bb_access_grant_config_lsb)
    @bb_access_grant_config.setter
    def bb_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__bb_access_grant_config_msb, self.__bb_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_PWM0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x39c
        self.__pwm0_access_grant_config_lsb = 0
        self.__pwm0_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pwm0_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__pwm0_access_grant_config_msb, self.__pwm0_access_grant_config_lsb)
    @pwm0_access_grant_config.setter
    def pwm0_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__pwm0_access_grant_config_msb, self.__pwm0_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_TIMERGROUP(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x3a0
        self.__timergroup_access_grant_config_lsb = 0
        self.__timergroup_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def timergroup_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__timergroup_access_grant_config_msb, self.__timergroup_access_grant_config_lsb)
    @timergroup_access_grant_config.setter
    def timergroup_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__timergroup_access_grant_config_msb, self.__timergroup_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_TIMERGROUP1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x3a4
        self.__timergroup1_access_grant_config_lsb = 0
        self.__timergroup1_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def timergroup1_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__timergroup1_access_grant_config_msb, self.__timergroup1_access_grant_config_lsb)
    @timergroup1_access_grant_config.setter
    def timergroup1_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__timergroup1_access_grant_config_msb, self.__timergroup1_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_SPI2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x3a8
        self.__spi2_access_grant_config_lsb = 0
        self.__spi2_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def spi2_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__spi2_access_grant_config_msb, self.__spi2_access_grant_config_lsb)
    @spi2_access_grant_config.setter
    def spi2_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi2_access_grant_config_msb, self.__spi2_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_SPI3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x3ac
        self.__spi3_access_grant_config_lsb = 0
        self.__spi3_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def spi3_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__spi3_access_grant_config_msb, self.__spi3_access_grant_config_lsb)
    @spi3_access_grant_config.setter
    def spi3_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi3_access_grant_config_msb, self.__spi3_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_APB_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x3b0
        self.__apbctrl_access_grant_config_lsb = 0
        self.__apbctrl_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def apbctrl_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__apbctrl_access_grant_config_msb, self.__apbctrl_access_grant_config_lsb)
    @apbctrl_access_grant_config.setter
    def apbctrl_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__apbctrl_access_grant_config_msb, self.__apbctrl_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_I2C_EXT1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x3b4
        self.__i2cext1_access_grant_config_lsb = 0
        self.__i2cext1_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2cext1_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__i2cext1_access_grant_config_msb, self.__i2cext1_access_grant_config_lsb)
    @i2cext1_access_grant_config.setter
    def i2cext1_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2cext1_access_grant_config_msb, self.__i2cext1_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_SDIO_HOST(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x3b8
        self.__sdiohost_access_grant_config_lsb = 0
        self.__sdiohost_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sdiohost_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__sdiohost_access_grant_config_msb, self.__sdiohost_access_grant_config_lsb)
    @sdiohost_access_grant_config.setter
    def sdiohost_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__sdiohost_access_grant_config_msb, self.__sdiohost_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_EMAC(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x3bc
        self.__emac_access_grant_config_lsb = 0
        self.__emac_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def emac_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__emac_access_grant_config_msb, self.__emac_access_grant_config_lsb)
    @emac_access_grant_config.setter
    def emac_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__emac_access_grant_config_msb, self.__emac_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_CAN(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x3c0
        self.__can_access_grant_config_lsb = 0
        self.__can_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def can_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__can_access_grant_config_msb, self.__can_access_grant_config_lsb)
    @can_access_grant_config.setter
    def can_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__can_access_grant_config_msb, self.__can_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_PWM1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x3c4
        self.__pwm1_access_grant_config_lsb = 0
        self.__pwm1_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pwm1_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__pwm1_access_grant_config_msb, self.__pwm1_access_grant_config_lsb)
    @pwm1_access_grant_config.setter
    def pwm1_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__pwm1_access_grant_config_msb, self.__pwm1_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_I2S1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x3c8
        self.__i2s1_access_grant_config_lsb = 0
        self.__i2s1_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s1_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__i2s1_access_grant_config_msb, self.__i2s1_access_grant_config_lsb)
    @i2s1_access_grant_config.setter
    def i2s1_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s1_access_grant_config_msb, self.__i2s1_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_UART2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x3cc
        self.__uart2_access_grant_config_lsb = 0
        self.__uart2_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def uart2_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__uart2_access_grant_config_msb, self.__uart2_access_grant_config_lsb)
    @uart2_access_grant_config.setter
    def uart2_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart2_access_grant_config_msb, self.__uart2_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_PWM2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x3d0
        self.__pwm2_access_grant_config_lsb = 0
        self.__pwm2_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pwm2_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__pwm2_access_grant_config_msb, self.__pwm2_access_grant_config_lsb)
    @pwm2_access_grant_config.setter
    def pwm2_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__pwm2_access_grant_config_msb, self.__pwm2_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_PWM3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x3d4
        self.__pwm3_access_grant_config_lsb = 0
        self.__pwm3_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pwm3_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__pwm3_access_grant_config_msb, self.__pwm3_access_grant_config_lsb)
    @pwm3_access_grant_config.setter
    def pwm3_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__pwm3_access_grant_config_msb, self.__pwm3_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_RWBT(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x3d8
        self.__rwbt_access_grant_config_lsb = 0
        self.__rwbt_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rwbt_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__rwbt_access_grant_config_msb, self.__rwbt_access_grant_config_lsb)
    @rwbt_access_grant_config.setter
    def rwbt_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__rwbt_access_grant_config_msb, self.__rwbt_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_BTMAC(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x3dc
        self.__btmac_access_grant_config_lsb = 0
        self.__btmac_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def btmac_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__btmac_access_grant_config_msb, self.__btmac_access_grant_config_lsb)
    @btmac_access_grant_config.setter
    def btmac_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__btmac_access_grant_config_msb, self.__btmac_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_WIFIMAC(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x3e0
        self.__wifimac_access_grant_config_lsb = 0
        self.__wifimac_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def wifimac_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__wifimac_access_grant_config_msb, self.__wifimac_access_grant_config_lsb)
    @wifimac_access_grant_config.setter
    def wifimac_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__wifimac_access_grant_config_msb, self.__wifimac_access_grant_config_lsb, value)
class AHBLITE_MPU_TABLE_PWR(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x3e4
        self.__pwr_access_grant_config_lsb = 0
        self.__pwr_access_grant_config_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pwr_access_grant_config(self):
        return self.__MEM.rdm(self.__addr, self.__pwr_access_grant_config_msb, self.__pwr_access_grant_config_lsb)
    @pwr_access_grant_config.setter
    def pwr_access_grant_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__pwr_access_grant_config_msb, self.__pwr_access_grant_config_lsb, value)
class MEM_ACCESS_DBUG0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x3e8
        self.__internal_sram_mmu_multi_hit_lsb = 26
        self.__internal_sram_mmu_multi_hit_msb = 29
        self.__internal_sram_ia_lsb = 14
        self.__internal_sram_ia_msb = 25
        self.__internal_sram_mmu_ad_lsb = 10
        self.__internal_sram_mmu_ad_msb = 13
        self.__share_rom_ia_lsb = 6
        self.__share_rom_ia_msb = 9
        self.__share_rom_mpu_ad_lsb = 4
        self.__share_rom_mpu_ad_msb = 5
        self.__app_rom_ia_lsb = 3
        self.__app_rom_ia_msb = 3
        self.__app_rom_mpu_ad_lsb = 2
        self.__app_rom_mpu_ad_msb = 2
        self.__pro_rom_ia_lsb = 1
        self.__pro_rom_ia_msb = 1
        self.__pro_rom_mpu_ad_lsb = 0
        self.__pro_rom_mpu_ad_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def internal_sram_mmu_multi_hit(self):
        return self.__MEM.rdm(self.__addr, self.__internal_sram_mmu_multi_hit_msb, self.__internal_sram_mmu_multi_hit_lsb)
    @internal_sram_mmu_multi_hit.setter
    def internal_sram_mmu_multi_hit(self, value):
        return self.__MEM.wrm(self.__addr, self.__internal_sram_mmu_multi_hit_msb, self.__internal_sram_mmu_multi_hit_lsb, value)

    @property
    def internal_sram_ia(self):
        return self.__MEM.rdm(self.__addr, self.__internal_sram_ia_msb, self.__internal_sram_ia_lsb)
    @internal_sram_ia.setter
    def internal_sram_ia(self, value):
        return self.__MEM.wrm(self.__addr, self.__internal_sram_ia_msb, self.__internal_sram_ia_lsb, value)

    @property
    def internal_sram_mmu_ad(self):
        return self.__MEM.rdm(self.__addr, self.__internal_sram_mmu_ad_msb, self.__internal_sram_mmu_ad_lsb)
    @internal_sram_mmu_ad.setter
    def internal_sram_mmu_ad(self, value):
        return self.__MEM.wrm(self.__addr, self.__internal_sram_mmu_ad_msb, self.__internal_sram_mmu_ad_lsb, value)

    @property
    def share_rom_ia(self):
        return self.__MEM.rdm(self.__addr, self.__share_rom_ia_msb, self.__share_rom_ia_lsb)
    @share_rom_ia.setter
    def share_rom_ia(self, value):
        return self.__MEM.wrm(self.__addr, self.__share_rom_ia_msb, self.__share_rom_ia_lsb, value)

    @property
    def share_rom_mpu_ad(self):
        return self.__MEM.rdm(self.__addr, self.__share_rom_mpu_ad_msb, self.__share_rom_mpu_ad_lsb)
    @share_rom_mpu_ad.setter
    def share_rom_mpu_ad(self, value):
        return self.__MEM.wrm(self.__addr, self.__share_rom_mpu_ad_msb, self.__share_rom_mpu_ad_lsb, value)

    @property
    def app_rom_ia(self):
        return self.__MEM.rdm(self.__addr, self.__app_rom_ia_msb, self.__app_rom_ia_lsb)
    @app_rom_ia.setter
    def app_rom_ia(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_rom_ia_msb, self.__app_rom_ia_lsb, value)

    @property
    def app_rom_mpu_ad(self):
        return self.__MEM.rdm(self.__addr, self.__app_rom_mpu_ad_msb, self.__app_rom_mpu_ad_lsb)
    @app_rom_mpu_ad.setter
    def app_rom_mpu_ad(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_rom_mpu_ad_msb, self.__app_rom_mpu_ad_lsb, value)

    @property
    def pro_rom_ia(self):
        return self.__MEM.rdm(self.__addr, self.__pro_rom_ia_msb, self.__pro_rom_ia_lsb)
    @pro_rom_ia.setter
    def pro_rom_ia(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_rom_ia_msb, self.__pro_rom_ia_lsb, value)

    @property
    def pro_rom_mpu_ad(self):
        return self.__MEM.rdm(self.__addr, self.__pro_rom_mpu_ad_msb, self.__pro_rom_mpu_ad_lsb)
    @pro_rom_mpu_ad.setter
    def pro_rom_mpu_ad(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_rom_mpu_ad_msb, self.__pro_rom_mpu_ad_lsb, value)
class MEM_ACCESS_DBUG1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x3ec
        self.__ahblite_ia_lsb = 10
        self.__ahblite_ia_msb = 10
        self.__ahblite_access_deny_lsb = 9
        self.__ahblite_access_deny_msb = 9
        self.__ahb_access_deny_lsb = 8
        self.__ahb_access_deny_msb = 8
        self.__dport_pidgen_ia_lsb = 6
        self.__dport_pidgen_ia_msb = 7
        self.__dport_arb_ia_lsb = 4
        self.__dport_arb_ia_msb = 5
        self.__internal_sram_mmu_miss_lsb = 0
        self.__internal_sram_mmu_miss_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def ahblite_ia(self):
        return self.__MEM.rdm(self.__addr, self.__ahblite_ia_msb, self.__ahblite_ia_lsb)
    @ahblite_ia.setter
    def ahblite_ia(self, value):
        return self.__MEM.wrm(self.__addr, self.__ahblite_ia_msb, self.__ahblite_ia_lsb, value)

    @property
    def ahblite_access_deny(self):
        return self.__MEM.rdm(self.__addr, self.__ahblite_access_deny_msb, self.__ahblite_access_deny_lsb)
    @ahblite_access_deny.setter
    def ahblite_access_deny(self, value):
        return self.__MEM.wrm(self.__addr, self.__ahblite_access_deny_msb, self.__ahblite_access_deny_lsb, value)

    @property
    def ahb_access_deny(self):
        return self.__MEM.rdm(self.__addr, self.__ahb_access_deny_msb, self.__ahb_access_deny_lsb)
    @ahb_access_deny.setter
    def ahb_access_deny(self, value):
        return self.__MEM.wrm(self.__addr, self.__ahb_access_deny_msb, self.__ahb_access_deny_lsb, value)

    @property
    def dport_pidgen_ia(self):
        return self.__MEM.rdm(self.__addr, self.__dport_pidgen_ia_msb, self.__dport_pidgen_ia_lsb)
    @dport_pidgen_ia.setter
    def dport_pidgen_ia(self, value):
        return self.__MEM.wrm(self.__addr, self.__dport_pidgen_ia_msb, self.__dport_pidgen_ia_lsb, value)

    @property
    def dport_arb_ia(self):
        return self.__MEM.rdm(self.__addr, self.__dport_arb_ia_msb, self.__dport_arb_ia_lsb)
    @dport_arb_ia.setter
    def dport_arb_ia(self, value):
        return self.__MEM.wrm(self.__addr, self.__dport_arb_ia_msb, self.__dport_arb_ia_lsb, value)

    @property
    def internal_sram_mmu_miss(self):
        return self.__MEM.rdm(self.__addr, self.__internal_sram_mmu_miss_msb, self.__internal_sram_mmu_miss_lsb)
    @internal_sram_mmu_miss.setter
    def internal_sram_mmu_miss(self, value):
        return self.__MEM.wrm(self.__addr, self.__internal_sram_mmu_miss_msb, self.__internal_sram_mmu_miss_lsb, value)
class PRO_DCACHE_DBUG_REG0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x3f0
        self.__pro_rx_end_lsb = 23
        self.__pro_rx_end_msb = 23
        self.__pro_slave_wdata_v_lsb = 22
        self.__pro_slave_wdata_v_msb = 22
        self.__pro_slave_wr_lsb = 21
        self.__pro_slave_wr_msb = 21
        self.__pro_tx_end_lsb = 20
        self.__pro_tx_end_msb = 20
        self.__pro_wr_bak_to_read_lsb = 19
        self.__pro_wr_bak_to_read_msb = 19
        self.__pro_cache_state_lsb = 7
        self.__pro_cache_state_msb = 18
        self.__pro_cache_ia_lsb = 1
        self.__pro_cache_ia_msb = 6
        self.__pro_cache_mmu_ia_lsb = 0
        self.__pro_cache_mmu_ia_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_rx_end(self):
        return self.__MEM.rdm(self.__addr, self.__pro_rx_end_msb, self.__pro_rx_end_lsb)
    @pro_rx_end.setter
    def pro_rx_end(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_rx_end_msb, self.__pro_rx_end_lsb, value)

    @property
    def pro_slave_wdata_v(self):
        return self.__MEM.rdm(self.__addr, self.__pro_slave_wdata_v_msb, self.__pro_slave_wdata_v_lsb)
    @pro_slave_wdata_v.setter
    def pro_slave_wdata_v(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_slave_wdata_v_msb, self.__pro_slave_wdata_v_lsb, value)

    @property
    def pro_slave_wr(self):
        return self.__MEM.rdm(self.__addr, self.__pro_slave_wr_msb, self.__pro_slave_wr_lsb)
    @pro_slave_wr.setter
    def pro_slave_wr(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_slave_wr_msb, self.__pro_slave_wr_lsb, value)

    @property
    def pro_tx_end(self):
        return self.__MEM.rdm(self.__addr, self.__pro_tx_end_msb, self.__pro_tx_end_lsb)
    @pro_tx_end.setter
    def pro_tx_end(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_tx_end_msb, self.__pro_tx_end_lsb, value)

    @property
    def pro_wr_bak_to_read(self):
        return self.__MEM.rdm(self.__addr, self.__pro_wr_bak_to_read_msb, self.__pro_wr_bak_to_read_lsb)
    @pro_wr_bak_to_read.setter
    def pro_wr_bak_to_read(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_wr_bak_to_read_msb, self.__pro_wr_bak_to_read_lsb, value)

    @property
    def pro_cache_state(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_state_msb, self.__pro_cache_state_lsb)
    @pro_cache_state.setter
    def pro_cache_state(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_state_msb, self.__pro_cache_state_lsb, value)

    @property
    def pro_cache_ia(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_ia_msb, self.__pro_cache_ia_lsb)
    @pro_cache_ia.setter
    def pro_cache_ia(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_ia_msb, self.__pro_cache_ia_lsb, value)

    @property
    def pro_cache_mmu_ia(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_mmu_ia_msb, self.__pro_cache_mmu_ia_lsb)
    @pro_cache_mmu_ia.setter
    def pro_cache_mmu_ia(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_mmu_ia_msb, self.__pro_cache_mmu_ia_lsb, value)
class PRO_DCACHE_DBUG_REG1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x3f4
        self.__pro_ctag_ram_rdata_lsb = 0
        self.__pro_ctag_ram_rdata_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_ctag_ram_rdata(self):
        return self.__MEM.rdm(self.__addr, self.__pro_ctag_ram_rdata_msb, self.__pro_ctag_ram_rdata_lsb)
    @pro_ctag_ram_rdata.setter
    def pro_ctag_ram_rdata(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_ctag_ram_rdata_msb, self.__pro_ctag_ram_rdata_lsb, value)
class PRO_DCACHE_DBUG_REG2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x3f8
        self.__pro_cache_vaddr_lsb = 0
        self.__pro_cache_vaddr_msb = 26
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_cache_vaddr(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_vaddr_msb, self.__pro_cache_vaddr_lsb)
    @pro_cache_vaddr.setter
    def pro_cache_vaddr(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_vaddr_msb, self.__pro_cache_vaddr_lsb, value)
class PRO_DCACHE_DBUG_REG3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x3fc
        self.__pro_cache_iram0_pid_error_lsb = 15
        self.__pro_cache_iram0_pid_error_msb = 15
        self.__pro_cpu_disabled_cache_ia_lsb = 9
        self.__pro_cpu_disabled_cache_ia_msb = 14
        self.__pro_mmu_rdata_lsb = 0
        self.__pro_mmu_rdata_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_cache_iram0_pid_error(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_iram0_pid_error_msb, self.__pro_cache_iram0_pid_error_lsb)
    @pro_cache_iram0_pid_error.setter
    def pro_cache_iram0_pid_error(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_iram0_pid_error_msb, self.__pro_cache_iram0_pid_error_lsb, value)

    @property
    def pro_cpu_disabled_cache_ia(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cpu_disabled_cache_ia_msb, self.__pro_cpu_disabled_cache_ia_lsb)
    @pro_cpu_disabled_cache_ia.setter
    def pro_cpu_disabled_cache_ia(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cpu_disabled_cache_ia_msb, self.__pro_cpu_disabled_cache_ia_lsb, value)

    @property
    def pro_mmu_rdata(self):
        return self.__MEM.rdm(self.__addr, self.__pro_mmu_rdata_msb, self.__pro_mmu_rdata_lsb)
    @pro_mmu_rdata.setter
    def pro_mmu_rdata(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_mmu_rdata_msb, self.__pro_mmu_rdata_lsb, value)
class PRO_DCACHE_DBUG_REG4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x400
        self.__pro_reg_DRam1Addr0_ia_lsb = 0
        self.__pro_reg_DRam1Addr0_ia_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_reg_DRam1Addr0_ia(self):
        return self.__MEM.rdm(self.__addr, self.__pro_reg_DRam1Addr0_ia_msb, self.__pro_reg_DRam1Addr0_ia_lsb)
    @pro_reg_DRam1Addr0_ia.setter
    def pro_reg_DRam1Addr0_ia(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_reg_DRam1Addr0_ia_msb, self.__pro_reg_DRam1Addr0_ia_lsb, value)
class PRO_DCACHE_DBUG_REG5(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x404
        self.__pro_reg_DRom0Addr0_ia_lsb = 0
        self.__pro_reg_DRom0Addr0_ia_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_reg_DRom0Addr0_ia(self):
        return self.__MEM.rdm(self.__addr, self.__pro_reg_DRom0Addr0_ia_msb, self.__pro_reg_DRom0Addr0_ia_lsb)
    @pro_reg_DRom0Addr0_ia.setter
    def pro_reg_DRom0Addr0_ia(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_reg_DRom0Addr0_ia_msb, self.__pro_reg_DRom0Addr0_ia_lsb, value)
class PRO_DCACHE_DBUG_REG6(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x408
        self.__pro_reg_IRam0Addr_ia_lsb = 0
        self.__pro_reg_IRam0Addr_ia_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_reg_IRam0Addr_ia(self):
        return self.__MEM.rdm(self.__addr, self.__pro_reg_IRam0Addr_ia_msb, self.__pro_reg_IRam0Addr_ia_lsb)
    @pro_reg_IRam0Addr_ia.setter
    def pro_reg_IRam0Addr_ia(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_reg_IRam0Addr_ia_msb, self.__pro_reg_IRam0Addr_ia_lsb, value)
class PRO_DCACHE_DBUG_REG7(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x40c
        self.__pro_reg_IRam1Addr_ia_lsb = 0
        self.__pro_reg_IRam1Addr_ia_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_reg_IRam1Addr_ia(self):
        return self.__MEM.rdm(self.__addr, self.__pro_reg_IRam1Addr_ia_msb, self.__pro_reg_IRam1Addr_ia_lsb)
    @pro_reg_IRam1Addr_ia.setter
    def pro_reg_IRam1Addr_ia(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_reg_IRam1Addr_ia_msb, self.__pro_reg_IRam1Addr_ia_lsb, value)
class PRO_DCACHE_DBUG_REG8(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x410
        self.__pro_reg_IRom0Addr_ia_lsb = 0
        self.__pro_reg_IRom0Addr_ia_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_reg_IRom0Addr_ia(self):
        return self.__MEM.rdm(self.__addr, self.__pro_reg_IRom0Addr_ia_msb, self.__pro_reg_IRom0Addr_ia_lsb)
    @pro_reg_IRom0Addr_ia.setter
    def pro_reg_IRom0Addr_ia(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_reg_IRom0Addr_ia_msb, self.__pro_reg_IRom0Addr_ia_lsb, value)
class PRO_DCACHE_DBUG_REG9(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x414
        self.__pro_reg_opsDRamAddr_ia_lsb = 0
        self.__pro_reg_opsDRamAddr_ia_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_reg_opsDRamAddr_ia(self):
        return self.__MEM.rdm(self.__addr, self.__pro_reg_opsDRamAddr_ia_msb, self.__pro_reg_opsDRamAddr_ia_lsb)
    @pro_reg_opsDRamAddr_ia.setter
    def pro_reg_opsDRamAddr_ia(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_reg_opsDRamAddr_ia_msb, self.__pro_reg_opsDRamAddr_ia_lsb, value)
class APP_DCACHE_DBUG_REG0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x418
        self.__app_rx_end_lsb = 23
        self.__app_rx_end_msb = 23
        self.__app_slave_wdata_v_lsb = 22
        self.__app_slave_wdata_v_msb = 22
        self.__app_slave_wr_lsb = 21
        self.__app_slave_wr_msb = 21
        self.__app_tx_end_lsb = 20
        self.__app_tx_end_msb = 20
        self.__app_wr_bak_to_read_lsb = 19
        self.__app_wr_bak_to_read_msb = 19
        self.__app_cache_state_lsb = 7
        self.__app_cache_state_msb = 18
        self.__app_cache_ia_lsb = 1
        self.__app_cache_ia_msb = 6
        self.__app_cache_mmu_ia_lsb = 0
        self.__app_cache_mmu_ia_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_rx_end(self):
        return self.__MEM.rdm(self.__addr, self.__app_rx_end_msb, self.__app_rx_end_lsb)
    @app_rx_end.setter
    def app_rx_end(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_rx_end_msb, self.__app_rx_end_lsb, value)

    @property
    def app_slave_wdata_v(self):
        return self.__MEM.rdm(self.__addr, self.__app_slave_wdata_v_msb, self.__app_slave_wdata_v_lsb)
    @app_slave_wdata_v.setter
    def app_slave_wdata_v(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_slave_wdata_v_msb, self.__app_slave_wdata_v_lsb, value)

    @property
    def app_slave_wr(self):
        return self.__MEM.rdm(self.__addr, self.__app_slave_wr_msb, self.__app_slave_wr_lsb)
    @app_slave_wr.setter
    def app_slave_wr(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_slave_wr_msb, self.__app_slave_wr_lsb, value)

    @property
    def app_tx_end(self):
        return self.__MEM.rdm(self.__addr, self.__app_tx_end_msb, self.__app_tx_end_lsb)
    @app_tx_end.setter
    def app_tx_end(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_tx_end_msb, self.__app_tx_end_lsb, value)

    @property
    def app_wr_bak_to_read(self):
        return self.__MEM.rdm(self.__addr, self.__app_wr_bak_to_read_msb, self.__app_wr_bak_to_read_lsb)
    @app_wr_bak_to_read.setter
    def app_wr_bak_to_read(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_wr_bak_to_read_msb, self.__app_wr_bak_to_read_lsb, value)

    @property
    def app_cache_state(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_state_msb, self.__app_cache_state_lsb)
    @app_cache_state.setter
    def app_cache_state(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_state_msb, self.__app_cache_state_lsb, value)

    @property
    def app_cache_ia(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_ia_msb, self.__app_cache_ia_lsb)
    @app_cache_ia.setter
    def app_cache_ia(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_ia_msb, self.__app_cache_ia_lsb, value)

    @property
    def app_cache_mmu_ia(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_mmu_ia_msb, self.__app_cache_mmu_ia_lsb)
    @app_cache_mmu_ia.setter
    def app_cache_mmu_ia(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_mmu_ia_msb, self.__app_cache_mmu_ia_lsb, value)
class APP_DCACHE_DBUG_REG1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x41c
        self.__app_ctag_ram_rdata_lsb = 0
        self.__app_ctag_ram_rdata_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_ctag_ram_rdata(self):
        return self.__MEM.rdm(self.__addr, self.__app_ctag_ram_rdata_msb, self.__app_ctag_ram_rdata_lsb)
    @app_ctag_ram_rdata.setter
    def app_ctag_ram_rdata(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_ctag_ram_rdata_msb, self.__app_ctag_ram_rdata_lsb, value)
class APP_DCACHE_DBUG_REG2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x420
        self.__app_cache_vaddr_lsb = 0
        self.__app_cache_vaddr_msb = 26
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_cache_vaddr(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_vaddr_msb, self.__app_cache_vaddr_lsb)
    @app_cache_vaddr.setter
    def app_cache_vaddr(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_vaddr_msb, self.__app_cache_vaddr_lsb, value)
class APP_DCACHE_DBUG_REG3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x424
        self.__app_cache_iram0_pid_error_lsb = 15
        self.__app_cache_iram0_pid_error_msb = 15
        self.__app_cpu_disabled_cache_ia_lsb = 9
        self.__app_cpu_disabled_cache_ia_msb = 14
        self.__app_mmu_rdata_lsb = 0
        self.__app_mmu_rdata_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_cache_iram0_pid_error(self):
        return self.__MEM.rdm(self.__addr, self.__app_cache_iram0_pid_error_msb, self.__app_cache_iram0_pid_error_lsb)
    @app_cache_iram0_pid_error.setter
    def app_cache_iram0_pid_error(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cache_iram0_pid_error_msb, self.__app_cache_iram0_pid_error_lsb, value)

    @property
    def app_cpu_disabled_cache_ia(self):
        return self.__MEM.rdm(self.__addr, self.__app_cpu_disabled_cache_ia_msb, self.__app_cpu_disabled_cache_ia_lsb)
    @app_cpu_disabled_cache_ia.setter
    def app_cpu_disabled_cache_ia(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cpu_disabled_cache_ia_msb, self.__app_cpu_disabled_cache_ia_lsb, value)

    @property
    def app_mmu_rdata(self):
        return self.__MEM.rdm(self.__addr, self.__app_mmu_rdata_msb, self.__app_mmu_rdata_lsb)
    @app_mmu_rdata.setter
    def app_mmu_rdata(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_mmu_rdata_msb, self.__app_mmu_rdata_lsb, value)
class APP_DCACHE_DBUG_REG4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x428
        self.__app_reg_DRam1Addr0_ia_lsb = 0
        self.__app_reg_DRam1Addr0_ia_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_reg_DRam1Addr0_ia(self):
        return self.__MEM.rdm(self.__addr, self.__app_reg_DRam1Addr0_ia_msb, self.__app_reg_DRam1Addr0_ia_lsb)
    @app_reg_DRam1Addr0_ia.setter
    def app_reg_DRam1Addr0_ia(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_reg_DRam1Addr0_ia_msb, self.__app_reg_DRam1Addr0_ia_lsb, value)
class APP_DCACHE_DBUG_REG5(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x42c
        self.__app_reg_DRom0Addr0_ia_lsb = 0
        self.__app_reg_DRom0Addr0_ia_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_reg_DRom0Addr0_ia(self):
        return self.__MEM.rdm(self.__addr, self.__app_reg_DRom0Addr0_ia_msb, self.__app_reg_DRom0Addr0_ia_lsb)
    @app_reg_DRom0Addr0_ia.setter
    def app_reg_DRom0Addr0_ia(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_reg_DRom0Addr0_ia_msb, self.__app_reg_DRom0Addr0_ia_lsb, value)
class APP_DCACHE_DBUG_REG6(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x430
        self.__app_reg_IRam0Addr_ia_lsb = 0
        self.__app_reg_IRam0Addr_ia_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_reg_IRam0Addr_ia(self):
        return self.__MEM.rdm(self.__addr, self.__app_reg_IRam0Addr_ia_msb, self.__app_reg_IRam0Addr_ia_lsb)
    @app_reg_IRam0Addr_ia.setter
    def app_reg_IRam0Addr_ia(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_reg_IRam0Addr_ia_msb, self.__app_reg_IRam0Addr_ia_lsb, value)
class APP_DCACHE_DBUG_REG7(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x434
        self.__app_reg_IRam1Addr_ia_lsb = 0
        self.__app_reg_IRam1Addr_ia_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_reg_IRam1Addr_ia(self):
        return self.__MEM.rdm(self.__addr, self.__app_reg_IRam1Addr_ia_msb, self.__app_reg_IRam1Addr_ia_lsb)
    @app_reg_IRam1Addr_ia.setter
    def app_reg_IRam1Addr_ia(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_reg_IRam1Addr_ia_msb, self.__app_reg_IRam1Addr_ia_lsb, value)
class APP_DCACHE_DBUG_REG8(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x438
        self.__app_reg_IRom0Addr_ia_lsb = 0
        self.__app_reg_IRom0Addr_ia_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_reg_IRom0Addr_ia(self):
        return self.__MEM.rdm(self.__addr, self.__app_reg_IRom0Addr_ia_msb, self.__app_reg_IRom0Addr_ia_lsb)
    @app_reg_IRom0Addr_ia.setter
    def app_reg_IRom0Addr_ia(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_reg_IRom0Addr_ia_msb, self.__app_reg_IRom0Addr_ia_lsb, value)
class APP_DCACHE_DBUG_REG9(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x43c
        self.__app_reg_opsDRamAddr_ia_lsb = 0
        self.__app_reg_opsDRamAddr_ia_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_reg_opsDRamAddr_ia(self):
        return self.__MEM.rdm(self.__addr, self.__app_reg_opsDRamAddr_ia_msb, self.__app_reg_opsDRamAddr_ia_lsb)
    @app_reg_opsDRamAddr_ia.setter
    def app_reg_opsDRamAddr_ia(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_reg_opsDRamAddr_ia_msb, self.__app_reg_opsDRamAddr_ia_lsb, value)
class PRO_CPU_RECORD_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x440
        self.__reg_pro_cpu_pdebug_enable_lsb = 8
        self.__reg_pro_cpu_pdebug_enable_msb = 8
        self.__reg_pro_cpu_record_disable_lsb = 4
        self.__reg_pro_cpu_record_disable_msb = 4
        self.__reg_pro_cpu_record_enable_lsb = 0
        self.__reg_pro_cpu_record_enable_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_pro_cpu_pdebug_enable(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pro_cpu_pdebug_enable_msb, self.__reg_pro_cpu_pdebug_enable_lsb)
    @reg_pro_cpu_pdebug_enable.setter
    def reg_pro_cpu_pdebug_enable(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pro_cpu_pdebug_enable_msb, self.__reg_pro_cpu_pdebug_enable_lsb, value)

    @property
    def reg_pro_cpu_record_disable(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pro_cpu_record_disable_msb, self.__reg_pro_cpu_record_disable_lsb)
    @reg_pro_cpu_record_disable.setter
    def reg_pro_cpu_record_disable(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pro_cpu_record_disable_msb, self.__reg_pro_cpu_record_disable_lsb, value)

    @property
    def reg_pro_cpu_record_enable(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pro_cpu_record_enable_msb, self.__reg_pro_cpu_record_enable_lsb)
    @reg_pro_cpu_record_enable.setter
    def reg_pro_cpu_record_enable(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pro_cpu_record_enable_msb, self.__reg_pro_cpu_record_enable_lsb, value)
class PRO_CPU_RECORD_STATUS(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x444
        self.__pro_cpu_recording_lsb = 0
        self.__pro_cpu_recording_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_cpu_recording(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cpu_recording_msb, self.__pro_cpu_recording_lsb)
    @pro_cpu_recording.setter
    def pro_cpu_recording(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cpu_recording_msb, self.__pro_cpu_recording_lsb, value)
class PRO_CPU_RECORD_PID(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x448
        self.__record_pro_pid_lsb = 0
        self.__record_pro_pid_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def record_pro_pid(self):
        return self.__MEM.rdm(self.__addr, self.__record_pro_pid_msb, self.__record_pro_pid_lsb)
    @record_pro_pid.setter
    def record_pro_pid(self, value):
        return self.__MEM.wrm(self.__addr, self.__record_pro_pid_msb, self.__record_pro_pid_lsb, value)
class PRO_CPU_RECORD_PDEBUGINST(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x44c
        self.__record_pro_pdebuginst_lsb = 0
        self.__record_pro_pdebuginst_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def record_pro_pdebuginst(self):
        return self.__MEM.rdm(self.__addr, self.__record_pro_pdebuginst_msb, self.__record_pro_pdebuginst_lsb)
    @record_pro_pdebuginst.setter
    def record_pro_pdebuginst(self, value):
        return self.__MEM.wrm(self.__addr, self.__record_pro_pdebuginst_msb, self.__record_pro_pdebuginst_lsb, value)
class PRO_CPU_RECORD_PDEBUGSTATUS(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x450
        self.__record_pro_pdebugstatus_lsb = 0
        self.__record_pro_pdebugstatus_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def record_pro_pdebugstatus(self):
        return self.__MEM.rdm(self.__addr, self.__record_pro_pdebugstatus_msb, self.__record_pro_pdebugstatus_lsb)
    @record_pro_pdebugstatus.setter
    def record_pro_pdebugstatus(self, value):
        return self.__MEM.wrm(self.__addr, self.__record_pro_pdebugstatus_msb, self.__record_pro_pdebugstatus_lsb, value)
class PRO_CPU_RECORD_PDEBUGDATA(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x454
        self.__record_pro_pdebugdata_lsb = 0
        self.__record_pro_pdebugdata_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def record_pro_pdebugdata(self):
        return self.__MEM.rdm(self.__addr, self.__record_pro_pdebugdata_msb, self.__record_pro_pdebugdata_lsb)
    @record_pro_pdebugdata.setter
    def record_pro_pdebugdata(self, value):
        return self.__MEM.wrm(self.__addr, self.__record_pro_pdebugdata_msb, self.__record_pro_pdebugdata_lsb, value)
class PRO_CPU_RECORD_PDEBUGPC(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x458
        self.__record_pro_pdebugpc_lsb = 0
        self.__record_pro_pdebugpc_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def record_pro_pdebugpc(self):
        return self.__MEM.rdm(self.__addr, self.__record_pro_pdebugpc_msb, self.__record_pro_pdebugpc_lsb)
    @record_pro_pdebugpc.setter
    def record_pro_pdebugpc(self, value):
        return self.__MEM.wrm(self.__addr, self.__record_pro_pdebugpc_msb, self.__record_pro_pdebugpc_lsb, value)
class PRO_CPU_RECORD_PDEBUGLS0STAT(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x45c
        self.__record_pro_pdebugls0stat_lsb = 0
        self.__record_pro_pdebugls0stat_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def record_pro_pdebugls0stat(self):
        return self.__MEM.rdm(self.__addr, self.__record_pro_pdebugls0stat_msb, self.__record_pro_pdebugls0stat_lsb)
    @record_pro_pdebugls0stat.setter
    def record_pro_pdebugls0stat(self, value):
        return self.__MEM.wrm(self.__addr, self.__record_pro_pdebugls0stat_msb, self.__record_pro_pdebugls0stat_lsb, value)
class PRO_CPU_RECORD_PDEBUGLS0ADDR(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x460
        self.__record_pro_pdebugls0addr_lsb = 0
        self.__record_pro_pdebugls0addr_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def record_pro_pdebugls0addr(self):
        return self.__MEM.rdm(self.__addr, self.__record_pro_pdebugls0addr_msb, self.__record_pro_pdebugls0addr_lsb)
    @record_pro_pdebugls0addr.setter
    def record_pro_pdebugls0addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__record_pro_pdebugls0addr_msb, self.__record_pro_pdebugls0addr_lsb, value)
class PRO_CPU_RECORD_PDEBUGLS0DATA(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x464
        self.__record_pro_pdebugls0data_lsb = 0
        self.__record_pro_pdebugls0data_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def record_pro_pdebugls0data(self):
        return self.__MEM.rdm(self.__addr, self.__record_pro_pdebugls0data_msb, self.__record_pro_pdebugls0data_lsb)
    @record_pro_pdebugls0data.setter
    def record_pro_pdebugls0data(self, value):
        return self.__MEM.wrm(self.__addr, self.__record_pro_pdebugls0data_msb, self.__record_pro_pdebugls0data_lsb, value)
class APP_CPU_RECORD_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x468
        self.__reg_app_cpu_pdebug_enable_lsb = 8
        self.__reg_app_cpu_pdebug_enable_msb = 8
        self.__reg_app_cpu_record_disable_lsb = 4
        self.__reg_app_cpu_record_disable_msb = 4
        self.__reg_app_cpu_record_enable_lsb = 0
        self.__reg_app_cpu_record_enable_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_app_cpu_pdebug_enable(self):
        return self.__MEM.rdm(self.__addr, self.__reg_app_cpu_pdebug_enable_msb, self.__reg_app_cpu_pdebug_enable_lsb)
    @reg_app_cpu_pdebug_enable.setter
    def reg_app_cpu_pdebug_enable(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_app_cpu_pdebug_enable_msb, self.__reg_app_cpu_pdebug_enable_lsb, value)

    @property
    def reg_app_cpu_record_disable(self):
        return self.__MEM.rdm(self.__addr, self.__reg_app_cpu_record_disable_msb, self.__reg_app_cpu_record_disable_lsb)
    @reg_app_cpu_record_disable.setter
    def reg_app_cpu_record_disable(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_app_cpu_record_disable_msb, self.__reg_app_cpu_record_disable_lsb, value)

    @property
    def reg_app_cpu_record_enable(self):
        return self.__MEM.rdm(self.__addr, self.__reg_app_cpu_record_enable_msb, self.__reg_app_cpu_record_enable_lsb)
    @reg_app_cpu_record_enable.setter
    def reg_app_cpu_record_enable(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_app_cpu_record_enable_msb, self.__reg_app_cpu_record_enable_lsb, value)
class APP_CPU_RECORD_STATUS(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x46c
        self.__app_cpu_recording_lsb = 0
        self.__app_cpu_recording_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_cpu_recording(self):
        return self.__MEM.rdm(self.__addr, self.__app_cpu_recording_msb, self.__app_cpu_recording_lsb)
    @app_cpu_recording.setter
    def app_cpu_recording(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_cpu_recording_msb, self.__app_cpu_recording_lsb, value)
class APP_CPU_RECORD_PID(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x470
        self.__record_app_pid_lsb = 0
        self.__record_app_pid_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def record_app_pid(self):
        return self.__MEM.rdm(self.__addr, self.__record_app_pid_msb, self.__record_app_pid_lsb)
    @record_app_pid.setter
    def record_app_pid(self, value):
        return self.__MEM.wrm(self.__addr, self.__record_app_pid_msb, self.__record_app_pid_lsb, value)
class APP_CPU_RECORD_PDEBUGINST(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x474
        self.__record_app_pdebuginst_lsb = 0
        self.__record_app_pdebuginst_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def record_app_pdebuginst(self):
        return self.__MEM.rdm(self.__addr, self.__record_app_pdebuginst_msb, self.__record_app_pdebuginst_lsb)
    @record_app_pdebuginst.setter
    def record_app_pdebuginst(self, value):
        return self.__MEM.wrm(self.__addr, self.__record_app_pdebuginst_msb, self.__record_app_pdebuginst_lsb, value)
class APP_CPU_RECORD_PDEBUGSTATUS(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x478
        self.__record_app_pdebugstatus_lsb = 0
        self.__record_app_pdebugstatus_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def record_app_pdebugstatus(self):
        return self.__MEM.rdm(self.__addr, self.__record_app_pdebugstatus_msb, self.__record_app_pdebugstatus_lsb)
    @record_app_pdebugstatus.setter
    def record_app_pdebugstatus(self, value):
        return self.__MEM.wrm(self.__addr, self.__record_app_pdebugstatus_msb, self.__record_app_pdebugstatus_lsb, value)
class APP_CPU_RECORD_PDEBUGDATA(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x47c
        self.__record_app_pdebugdata_lsb = 0
        self.__record_app_pdebugdata_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def record_app_pdebugdata(self):
        return self.__MEM.rdm(self.__addr, self.__record_app_pdebugdata_msb, self.__record_app_pdebugdata_lsb)
    @record_app_pdebugdata.setter
    def record_app_pdebugdata(self, value):
        return self.__MEM.wrm(self.__addr, self.__record_app_pdebugdata_msb, self.__record_app_pdebugdata_lsb, value)
class APP_CPU_RECORD_PDEBUGPC(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x480
        self.__record_app_pdebugpc_lsb = 0
        self.__record_app_pdebugpc_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def record_app_pdebugpc(self):
        return self.__MEM.rdm(self.__addr, self.__record_app_pdebugpc_msb, self.__record_app_pdebugpc_lsb)
    @record_app_pdebugpc.setter
    def record_app_pdebugpc(self, value):
        return self.__MEM.wrm(self.__addr, self.__record_app_pdebugpc_msb, self.__record_app_pdebugpc_lsb, value)
class APP_CPU_RECORD_PDEBUGLS0STAT(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x484
        self.__record_app_pdebugls0stat_lsb = 0
        self.__record_app_pdebugls0stat_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def record_app_pdebugls0stat(self):
        return self.__MEM.rdm(self.__addr, self.__record_app_pdebugls0stat_msb, self.__record_app_pdebugls0stat_lsb)
    @record_app_pdebugls0stat.setter
    def record_app_pdebugls0stat(self, value):
        return self.__MEM.wrm(self.__addr, self.__record_app_pdebugls0stat_msb, self.__record_app_pdebugls0stat_lsb, value)
class APP_CPU_RECORD_PDEBUGLS0ADDR(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x488
        self.__record_app_pdebugls0addr_lsb = 0
        self.__record_app_pdebugls0addr_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def record_app_pdebugls0addr(self):
        return self.__MEM.rdm(self.__addr, self.__record_app_pdebugls0addr_msb, self.__record_app_pdebugls0addr_lsb)
    @record_app_pdebugls0addr.setter
    def record_app_pdebugls0addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__record_app_pdebugls0addr_msb, self.__record_app_pdebugls0addr_lsb, value)
class APP_CPU_RECORD_PDEBUGLS0DATA(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x48c
        self.__record_app_pdebugls0data_lsb = 0
        self.__record_app_pdebugls0data_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def record_app_pdebugls0data(self):
        return self.__MEM.rdm(self.__addr, self.__record_app_pdebugls0data_msb, self.__record_app_pdebugls0data_lsb)
    @record_app_pdebugls0data.setter
    def record_app_pdebugls0data(self, value):
        return self.__MEM.wrm(self.__addr, self.__record_app_pdebugls0data_msb, self.__record_app_pdebugls0data_lsb, value)
class RSA_PD_CTRL_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x490
        self.__rsa_pd_lsb = 0
        self.__rsa_pd_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rsa_pd(self):
        return self.__MEM.rdm(self.__addr, self.__rsa_pd_msb, self.__rsa_pd_lsb)
    @rsa_pd.setter
    def rsa_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__rsa_pd_msb, self.__rsa_pd_lsb, value)
class ROM_MPU_TABLE0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x494
        self.__rom_mpu_table0_lsb = 0
        self.__rom_mpu_table0_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rom_mpu_table0(self):
        return self.__MEM.rdm(self.__addr, self.__rom_mpu_table0_msb, self.__rom_mpu_table0_lsb)
    @rom_mpu_table0.setter
    def rom_mpu_table0(self, value):
        return self.__MEM.wrm(self.__addr, self.__rom_mpu_table0_msb, self.__rom_mpu_table0_lsb, value)
class ROM_MPU_TABLE1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x498
        self.__rom_mpu_table1_lsb = 0
        self.__rom_mpu_table1_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rom_mpu_table1(self):
        return self.__MEM.rdm(self.__addr, self.__rom_mpu_table1_msb, self.__rom_mpu_table1_lsb)
    @rom_mpu_table1.setter
    def rom_mpu_table1(self, value):
        return self.__MEM.wrm(self.__addr, self.__rom_mpu_table1_msb, self.__rom_mpu_table1_lsb, value)
class ROM_MPU_TABLE2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x49c
        self.__rom_mpu_table2_lsb = 0
        self.__rom_mpu_table2_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rom_mpu_table2(self):
        return self.__MEM.rdm(self.__addr, self.__rom_mpu_table2_msb, self.__rom_mpu_table2_lsb)
    @rom_mpu_table2.setter
    def rom_mpu_table2(self, value):
        return self.__MEM.wrm(self.__addr, self.__rom_mpu_table2_msb, self.__rom_mpu_table2_lsb, value)
class ROM_MPU_TABLE3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x4a0
        self.__rom_mpu_table3_lsb = 0
        self.__rom_mpu_table3_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rom_mpu_table3(self):
        return self.__MEM.rdm(self.__addr, self.__rom_mpu_table3_msb, self.__rom_mpu_table3_lsb)
    @rom_mpu_table3.setter
    def rom_mpu_table3(self, value):
        return self.__MEM.wrm(self.__addr, self.__rom_mpu_table3_msb, self.__rom_mpu_table3_lsb, value)
class SHROM_MPU_TABLE0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x4a4
        self.__shrom_mpu_table0_lsb = 0
        self.__shrom_mpu_table0_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def shrom_mpu_table0(self):
        return self.__MEM.rdm(self.__addr, self.__shrom_mpu_table0_msb, self.__shrom_mpu_table0_lsb)
    @shrom_mpu_table0.setter
    def shrom_mpu_table0(self, value):
        return self.__MEM.wrm(self.__addr, self.__shrom_mpu_table0_msb, self.__shrom_mpu_table0_lsb, value)
class SHROM_MPU_TABLE1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x4a8
        self.__shrom_mpu_table1_lsb = 0
        self.__shrom_mpu_table1_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def shrom_mpu_table1(self):
        return self.__MEM.rdm(self.__addr, self.__shrom_mpu_table1_msb, self.__shrom_mpu_table1_lsb)
    @shrom_mpu_table1.setter
    def shrom_mpu_table1(self, value):
        return self.__MEM.wrm(self.__addr, self.__shrom_mpu_table1_msb, self.__shrom_mpu_table1_lsb, value)
class SHROM_MPU_TABLE2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x4ac
        self.__shrom_mpu_table2_lsb = 0
        self.__shrom_mpu_table2_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def shrom_mpu_table2(self):
        return self.__MEM.rdm(self.__addr, self.__shrom_mpu_table2_msb, self.__shrom_mpu_table2_lsb)
    @shrom_mpu_table2.setter
    def shrom_mpu_table2(self, value):
        return self.__MEM.wrm(self.__addr, self.__shrom_mpu_table2_msb, self.__shrom_mpu_table2_lsb, value)
class SHROM_MPU_TABLE3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x4b0
        self.__shrom_mpu_table3_lsb = 0
        self.__shrom_mpu_table3_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def shrom_mpu_table3(self):
        return self.__MEM.rdm(self.__addr, self.__shrom_mpu_table3_msb, self.__shrom_mpu_table3_lsb)
    @shrom_mpu_table3.setter
    def shrom_mpu_table3(self, value):
        return self.__MEM.wrm(self.__addr, self.__shrom_mpu_table3_msb, self.__shrom_mpu_table3_lsb, value)
class SHROM_MPU_TABLE4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x4b4
        self.__shrom_mpu_table4_lsb = 0
        self.__shrom_mpu_table4_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def shrom_mpu_table4(self):
        return self.__MEM.rdm(self.__addr, self.__shrom_mpu_table4_msb, self.__shrom_mpu_table4_lsb)
    @shrom_mpu_table4.setter
    def shrom_mpu_table4(self, value):
        return self.__MEM.wrm(self.__addr, self.__shrom_mpu_table4_msb, self.__shrom_mpu_table4_lsb, value)
class SHROM_MPU_TABLE5(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x4b8
        self.__shrom_mpu_table5_lsb = 0
        self.__shrom_mpu_table5_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def shrom_mpu_table5(self):
        return self.__MEM.rdm(self.__addr, self.__shrom_mpu_table5_msb, self.__shrom_mpu_table5_lsb)
    @shrom_mpu_table5.setter
    def shrom_mpu_table5(self, value):
        return self.__MEM.wrm(self.__addr, self.__shrom_mpu_table5_msb, self.__shrom_mpu_table5_lsb, value)
class SHROM_MPU_TABLE6(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x4bc
        self.__shrom_mpu_table6_lsb = 0
        self.__shrom_mpu_table6_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def shrom_mpu_table6(self):
        return self.__MEM.rdm(self.__addr, self.__shrom_mpu_table6_msb, self.__shrom_mpu_table6_lsb)
    @shrom_mpu_table6.setter
    def shrom_mpu_table6(self, value):
        return self.__MEM.wrm(self.__addr, self.__shrom_mpu_table6_msb, self.__shrom_mpu_table6_lsb, value)
class SHROM_MPU_TABLE7(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x4c0
        self.__shrom_mpu_table7_lsb = 0
        self.__shrom_mpu_table7_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def shrom_mpu_table7(self):
        return self.__MEM.rdm(self.__addr, self.__shrom_mpu_table7_msb, self.__shrom_mpu_table7_lsb)
    @shrom_mpu_table7.setter
    def shrom_mpu_table7(self, value):
        return self.__MEM.wrm(self.__addr, self.__shrom_mpu_table7_msb, self.__shrom_mpu_table7_lsb, value)
class SHROM_MPU_TABLE8(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x4c4
        self.__shrom_mpu_table8_lsb = 0
        self.__shrom_mpu_table8_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def shrom_mpu_table8(self):
        return self.__MEM.rdm(self.__addr, self.__shrom_mpu_table8_msb, self.__shrom_mpu_table8_lsb)
    @shrom_mpu_table8.setter
    def shrom_mpu_table8(self, value):
        return self.__MEM.wrm(self.__addr, self.__shrom_mpu_table8_msb, self.__shrom_mpu_table8_lsb, value)
class SHROM_MPU_TABLE9(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x4c8
        self.__shrom_mpu_table9_lsb = 0
        self.__shrom_mpu_table9_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def shrom_mpu_table9(self):
        return self.__MEM.rdm(self.__addr, self.__shrom_mpu_table9_msb, self.__shrom_mpu_table9_lsb)
    @shrom_mpu_table9.setter
    def shrom_mpu_table9(self, value):
        return self.__MEM.wrm(self.__addr, self.__shrom_mpu_table9_msb, self.__shrom_mpu_table9_lsb, value)
class SHROM_MPU_TABLE10(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x4cc
        self.__shrom_mpu_table10_lsb = 0
        self.__shrom_mpu_table10_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def shrom_mpu_table10(self):
        return self.__MEM.rdm(self.__addr, self.__shrom_mpu_table10_msb, self.__shrom_mpu_table10_lsb)
    @shrom_mpu_table10.setter
    def shrom_mpu_table10(self, value):
        return self.__MEM.wrm(self.__addr, self.__shrom_mpu_table10_msb, self.__shrom_mpu_table10_lsb, value)
class SHROM_MPU_TABLE11(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x4d0
        self.__shrom_mpu_table11_lsb = 0
        self.__shrom_mpu_table11_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def shrom_mpu_table11(self):
        return self.__MEM.rdm(self.__addr, self.__shrom_mpu_table11_msb, self.__shrom_mpu_table11_lsb)
    @shrom_mpu_table11.setter
    def shrom_mpu_table11(self, value):
        return self.__MEM.wrm(self.__addr, self.__shrom_mpu_table11_msb, self.__shrom_mpu_table11_lsb, value)
class SHROM_MPU_TABLE12(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x4d4
        self.__shrom_mpu_table12_lsb = 0
        self.__shrom_mpu_table12_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def shrom_mpu_table12(self):
        return self.__MEM.rdm(self.__addr, self.__shrom_mpu_table12_msb, self.__shrom_mpu_table12_lsb)
    @shrom_mpu_table12.setter
    def shrom_mpu_table12(self, value):
        return self.__MEM.wrm(self.__addr, self.__shrom_mpu_table12_msb, self.__shrom_mpu_table12_lsb, value)
class SHROM_MPU_TABLE13(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x4d8
        self.__shrom_mpu_table13_lsb = 0
        self.__shrom_mpu_table13_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def shrom_mpu_table13(self):
        return self.__MEM.rdm(self.__addr, self.__shrom_mpu_table13_msb, self.__shrom_mpu_table13_lsb)
    @shrom_mpu_table13.setter
    def shrom_mpu_table13(self, value):
        return self.__MEM.wrm(self.__addr, self.__shrom_mpu_table13_msb, self.__shrom_mpu_table13_lsb, value)
class SHROM_MPU_TABLE14(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x4dc
        self.__shrom_mpu_table14_lsb = 0
        self.__shrom_mpu_table14_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def shrom_mpu_table14(self):
        return self.__MEM.rdm(self.__addr, self.__shrom_mpu_table14_msb, self.__shrom_mpu_table14_lsb)
    @shrom_mpu_table14.setter
    def shrom_mpu_table14(self, value):
        return self.__MEM.wrm(self.__addr, self.__shrom_mpu_table14_msb, self.__shrom_mpu_table14_lsb, value)
class SHROM_MPU_TABLE15(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x4e0
        self.__shrom_mpu_table15_lsb = 0
        self.__shrom_mpu_table15_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def shrom_mpu_table15(self):
        return self.__MEM.rdm(self.__addr, self.__shrom_mpu_table15_msb, self.__shrom_mpu_table15_lsb)
    @shrom_mpu_table15.setter
    def shrom_mpu_table15(self, value):
        return self.__MEM.wrm(self.__addr, self.__shrom_mpu_table15_msb, self.__shrom_mpu_table15_lsb, value)
class SHROM_MPU_TABLE16(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x4e4
        self.__shrom_mpu_table16_lsb = 0
        self.__shrom_mpu_table16_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def shrom_mpu_table16(self):
        return self.__MEM.rdm(self.__addr, self.__shrom_mpu_table16_msb, self.__shrom_mpu_table16_lsb)
    @shrom_mpu_table16.setter
    def shrom_mpu_table16(self, value):
        return self.__MEM.wrm(self.__addr, self.__shrom_mpu_table16_msb, self.__shrom_mpu_table16_lsb, value)
class SHROM_MPU_TABLE17(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x4e8
        self.__shrom_mpu_table17_lsb = 0
        self.__shrom_mpu_table17_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def shrom_mpu_table17(self):
        return self.__MEM.rdm(self.__addr, self.__shrom_mpu_table17_msb, self.__shrom_mpu_table17_lsb)
    @shrom_mpu_table17.setter
    def shrom_mpu_table17(self, value):
        return self.__MEM.wrm(self.__addr, self.__shrom_mpu_table17_msb, self.__shrom_mpu_table17_lsb, value)
class SHROM_MPU_TABLE18(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x4ec
        self.__shrom_mpu_table18_lsb = 0
        self.__shrom_mpu_table18_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def shrom_mpu_table18(self):
        return self.__MEM.rdm(self.__addr, self.__shrom_mpu_table18_msb, self.__shrom_mpu_table18_lsb)
    @shrom_mpu_table18.setter
    def shrom_mpu_table18(self, value):
        return self.__MEM.wrm(self.__addr, self.__shrom_mpu_table18_msb, self.__shrom_mpu_table18_lsb, value)
class SHROM_MPU_TABLE19(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x4f0
        self.__shrom_mpu_table19_lsb = 0
        self.__shrom_mpu_table19_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def shrom_mpu_table19(self):
        return self.__MEM.rdm(self.__addr, self.__shrom_mpu_table19_msb, self.__shrom_mpu_table19_lsb)
    @shrom_mpu_table19.setter
    def shrom_mpu_table19(self, value):
        return self.__MEM.wrm(self.__addr, self.__shrom_mpu_table19_msb, self.__shrom_mpu_table19_lsb, value)
class SHROM_MPU_TABLE20(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x4f4
        self.__shrom_mpu_table20_lsb = 0
        self.__shrom_mpu_table20_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def shrom_mpu_table20(self):
        return self.__MEM.rdm(self.__addr, self.__shrom_mpu_table20_msb, self.__shrom_mpu_table20_lsb)
    @shrom_mpu_table20.setter
    def shrom_mpu_table20(self, value):
        return self.__MEM.wrm(self.__addr, self.__shrom_mpu_table20_msb, self.__shrom_mpu_table20_lsb, value)
class SHROM_MPU_TABLE21(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x4f8
        self.__shrom_mpu_table21_lsb = 0
        self.__shrom_mpu_table21_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def shrom_mpu_table21(self):
        return self.__MEM.rdm(self.__addr, self.__shrom_mpu_table21_msb, self.__shrom_mpu_table21_lsb)
    @shrom_mpu_table21.setter
    def shrom_mpu_table21(self, value):
        return self.__MEM.wrm(self.__addr, self.__shrom_mpu_table21_msb, self.__shrom_mpu_table21_lsb, value)
class SHROM_MPU_TABLE22(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x4fc
        self.__shrom_mpu_table22_lsb = 0
        self.__shrom_mpu_table22_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def shrom_mpu_table22(self):
        return self.__MEM.rdm(self.__addr, self.__shrom_mpu_table22_msb, self.__shrom_mpu_table22_lsb)
    @shrom_mpu_table22.setter
    def shrom_mpu_table22(self, value):
        return self.__MEM.wrm(self.__addr, self.__shrom_mpu_table22_msb, self.__shrom_mpu_table22_lsb, value)
class SHROM_MPU_TABLE23(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x500
        self.__shrom_mpu_table23_lsb = 0
        self.__shrom_mpu_table23_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def shrom_mpu_table23(self):
        return self.__MEM.rdm(self.__addr, self.__shrom_mpu_table23_msb, self.__shrom_mpu_table23_lsb)
    @shrom_mpu_table23.setter
    def shrom_mpu_table23(self, value):
        return self.__MEM.wrm(self.__addr, self.__shrom_mpu_table23_msb, self.__shrom_mpu_table23_lsb, value)
class IMMU_TABLE0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x504
        self.__immu_table0_lsb = 0
        self.__immu_table0_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def immu_table0(self):
        return self.__MEM.rdm(self.__addr, self.__immu_table0_msb, self.__immu_table0_lsb)
    @immu_table0.setter
    def immu_table0(self, value):
        return self.__MEM.wrm(self.__addr, self.__immu_table0_msb, self.__immu_table0_lsb, value)
class IMMU_TABLE1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x508
        self.__immu_table1_lsb = 0
        self.__immu_table1_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def immu_table1(self):
        return self.__MEM.rdm(self.__addr, self.__immu_table1_msb, self.__immu_table1_lsb)
    @immu_table1.setter
    def immu_table1(self, value):
        return self.__MEM.wrm(self.__addr, self.__immu_table1_msb, self.__immu_table1_lsb, value)
class IMMU_TABLE2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x50c
        self.__immu_table2_lsb = 0
        self.__immu_table2_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def immu_table2(self):
        return self.__MEM.rdm(self.__addr, self.__immu_table2_msb, self.__immu_table2_lsb)
    @immu_table2.setter
    def immu_table2(self, value):
        return self.__MEM.wrm(self.__addr, self.__immu_table2_msb, self.__immu_table2_lsb, value)
class IMMU_TABLE3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x510
        self.__immu_table3_lsb = 0
        self.__immu_table3_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def immu_table3(self):
        return self.__MEM.rdm(self.__addr, self.__immu_table3_msb, self.__immu_table3_lsb)
    @immu_table3.setter
    def immu_table3(self, value):
        return self.__MEM.wrm(self.__addr, self.__immu_table3_msb, self.__immu_table3_lsb, value)
class IMMU_TABLE4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x514
        self.__immu_table4_lsb = 0
        self.__immu_table4_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def immu_table4(self):
        return self.__MEM.rdm(self.__addr, self.__immu_table4_msb, self.__immu_table4_lsb)
    @immu_table4.setter
    def immu_table4(self, value):
        return self.__MEM.wrm(self.__addr, self.__immu_table4_msb, self.__immu_table4_lsb, value)
class IMMU_TABLE5(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x518
        self.__immu_table5_lsb = 0
        self.__immu_table5_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def immu_table5(self):
        return self.__MEM.rdm(self.__addr, self.__immu_table5_msb, self.__immu_table5_lsb)
    @immu_table5.setter
    def immu_table5(self, value):
        return self.__MEM.wrm(self.__addr, self.__immu_table5_msb, self.__immu_table5_lsb, value)
class IMMU_TABLE6(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x51c
        self.__immu_table6_lsb = 0
        self.__immu_table6_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def immu_table6(self):
        return self.__MEM.rdm(self.__addr, self.__immu_table6_msb, self.__immu_table6_lsb)
    @immu_table6.setter
    def immu_table6(self, value):
        return self.__MEM.wrm(self.__addr, self.__immu_table6_msb, self.__immu_table6_lsb, value)
class IMMU_TABLE7(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x520
        self.__immu_table7_lsb = 0
        self.__immu_table7_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def immu_table7(self):
        return self.__MEM.rdm(self.__addr, self.__immu_table7_msb, self.__immu_table7_lsb)
    @immu_table7.setter
    def immu_table7(self, value):
        return self.__MEM.wrm(self.__addr, self.__immu_table7_msb, self.__immu_table7_lsb, value)
class IMMU_TABLE8(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x524
        self.__immu_table8_lsb = 0
        self.__immu_table8_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def immu_table8(self):
        return self.__MEM.rdm(self.__addr, self.__immu_table8_msb, self.__immu_table8_lsb)
    @immu_table8.setter
    def immu_table8(self, value):
        return self.__MEM.wrm(self.__addr, self.__immu_table8_msb, self.__immu_table8_lsb, value)
class IMMU_TABLE9(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x528
        self.__immu_table9_lsb = 0
        self.__immu_table9_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def immu_table9(self):
        return self.__MEM.rdm(self.__addr, self.__immu_table9_msb, self.__immu_table9_lsb)
    @immu_table9.setter
    def immu_table9(self, value):
        return self.__MEM.wrm(self.__addr, self.__immu_table9_msb, self.__immu_table9_lsb, value)
class IMMU_TABLE10(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x52c
        self.__immu_table10_lsb = 0
        self.__immu_table10_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def immu_table10(self):
        return self.__MEM.rdm(self.__addr, self.__immu_table10_msb, self.__immu_table10_lsb)
    @immu_table10.setter
    def immu_table10(self, value):
        return self.__MEM.wrm(self.__addr, self.__immu_table10_msb, self.__immu_table10_lsb, value)
class IMMU_TABLE11(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x530
        self.__immu_table11_lsb = 0
        self.__immu_table11_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def immu_table11(self):
        return self.__MEM.rdm(self.__addr, self.__immu_table11_msb, self.__immu_table11_lsb)
    @immu_table11.setter
    def immu_table11(self, value):
        return self.__MEM.wrm(self.__addr, self.__immu_table11_msb, self.__immu_table11_lsb, value)
class IMMU_TABLE12(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x534
        self.__immu_table12_lsb = 0
        self.__immu_table12_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def immu_table12(self):
        return self.__MEM.rdm(self.__addr, self.__immu_table12_msb, self.__immu_table12_lsb)
    @immu_table12.setter
    def immu_table12(self, value):
        return self.__MEM.wrm(self.__addr, self.__immu_table12_msb, self.__immu_table12_lsb, value)
class IMMU_TABLE13(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x538
        self.__immu_table13_lsb = 0
        self.__immu_table13_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def immu_table13(self):
        return self.__MEM.rdm(self.__addr, self.__immu_table13_msb, self.__immu_table13_lsb)
    @immu_table13.setter
    def immu_table13(self, value):
        return self.__MEM.wrm(self.__addr, self.__immu_table13_msb, self.__immu_table13_lsb, value)
class IMMU_TABLE14(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x53c
        self.__immu_table14_lsb = 0
        self.__immu_table14_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def immu_table14(self):
        return self.__MEM.rdm(self.__addr, self.__immu_table14_msb, self.__immu_table14_lsb)
    @immu_table14.setter
    def immu_table14(self, value):
        return self.__MEM.wrm(self.__addr, self.__immu_table14_msb, self.__immu_table14_lsb, value)
class IMMU_TABLE15(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x540
        self.__immu_table15_lsb = 0
        self.__immu_table15_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def immu_table15(self):
        return self.__MEM.rdm(self.__addr, self.__immu_table15_msb, self.__immu_table15_lsb)
    @immu_table15.setter
    def immu_table15(self, value):
        return self.__MEM.wrm(self.__addr, self.__immu_table15_msb, self.__immu_table15_lsb, value)
class DMMU_TABLE0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x544
        self.__dmmu_table0_lsb = 0
        self.__dmmu_table0_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def dmmu_table0(self):
        return self.__MEM.rdm(self.__addr, self.__dmmu_table0_msb, self.__dmmu_table0_lsb)
    @dmmu_table0.setter
    def dmmu_table0(self, value):
        return self.__MEM.wrm(self.__addr, self.__dmmu_table0_msb, self.__dmmu_table0_lsb, value)
class DMMU_TABLE1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x548
        self.__dmmu_table1_lsb = 0
        self.__dmmu_table1_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def dmmu_table1(self):
        return self.__MEM.rdm(self.__addr, self.__dmmu_table1_msb, self.__dmmu_table1_lsb)
    @dmmu_table1.setter
    def dmmu_table1(self, value):
        return self.__MEM.wrm(self.__addr, self.__dmmu_table1_msb, self.__dmmu_table1_lsb, value)
class DMMU_TABLE2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x54c
        self.__dmmu_table2_lsb = 0
        self.__dmmu_table2_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def dmmu_table2(self):
        return self.__MEM.rdm(self.__addr, self.__dmmu_table2_msb, self.__dmmu_table2_lsb)
    @dmmu_table2.setter
    def dmmu_table2(self, value):
        return self.__MEM.wrm(self.__addr, self.__dmmu_table2_msb, self.__dmmu_table2_lsb, value)
class DMMU_TABLE3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x550
        self.__dmmu_table3_lsb = 0
        self.__dmmu_table3_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def dmmu_table3(self):
        return self.__MEM.rdm(self.__addr, self.__dmmu_table3_msb, self.__dmmu_table3_lsb)
    @dmmu_table3.setter
    def dmmu_table3(self, value):
        return self.__MEM.wrm(self.__addr, self.__dmmu_table3_msb, self.__dmmu_table3_lsb, value)
class DMMU_TABLE4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x554
        self.__dmmu_table4_lsb = 0
        self.__dmmu_table4_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def dmmu_table4(self):
        return self.__MEM.rdm(self.__addr, self.__dmmu_table4_msb, self.__dmmu_table4_lsb)
    @dmmu_table4.setter
    def dmmu_table4(self, value):
        return self.__MEM.wrm(self.__addr, self.__dmmu_table4_msb, self.__dmmu_table4_lsb, value)
class DMMU_TABLE5(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x558
        self.__dmmu_table5_lsb = 0
        self.__dmmu_table5_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def dmmu_table5(self):
        return self.__MEM.rdm(self.__addr, self.__dmmu_table5_msb, self.__dmmu_table5_lsb)
    @dmmu_table5.setter
    def dmmu_table5(self, value):
        return self.__MEM.wrm(self.__addr, self.__dmmu_table5_msb, self.__dmmu_table5_lsb, value)
class DMMU_TABLE6(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x55c
        self.__dmmu_table6_lsb = 0
        self.__dmmu_table6_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def dmmu_table6(self):
        return self.__MEM.rdm(self.__addr, self.__dmmu_table6_msb, self.__dmmu_table6_lsb)
    @dmmu_table6.setter
    def dmmu_table6(self, value):
        return self.__MEM.wrm(self.__addr, self.__dmmu_table6_msb, self.__dmmu_table6_lsb, value)
class DMMU_TABLE7(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x560
        self.__dmmu_table7_lsb = 0
        self.__dmmu_table7_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def dmmu_table7(self):
        return self.__MEM.rdm(self.__addr, self.__dmmu_table7_msb, self.__dmmu_table7_lsb)
    @dmmu_table7.setter
    def dmmu_table7(self, value):
        return self.__MEM.wrm(self.__addr, self.__dmmu_table7_msb, self.__dmmu_table7_lsb, value)
class DMMU_TABLE8(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x564
        self.__dmmu_table8_lsb = 0
        self.__dmmu_table8_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def dmmu_table8(self):
        return self.__MEM.rdm(self.__addr, self.__dmmu_table8_msb, self.__dmmu_table8_lsb)
    @dmmu_table8.setter
    def dmmu_table8(self, value):
        return self.__MEM.wrm(self.__addr, self.__dmmu_table8_msb, self.__dmmu_table8_lsb, value)
class DMMU_TABLE9(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x568
        self.__dmmu_table9_lsb = 0
        self.__dmmu_table9_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def dmmu_table9(self):
        return self.__MEM.rdm(self.__addr, self.__dmmu_table9_msb, self.__dmmu_table9_lsb)
    @dmmu_table9.setter
    def dmmu_table9(self, value):
        return self.__MEM.wrm(self.__addr, self.__dmmu_table9_msb, self.__dmmu_table9_lsb, value)
class DMMU_TABLE10(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x56c
        self.__dmmu_table10_lsb = 0
        self.__dmmu_table10_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def dmmu_table10(self):
        return self.__MEM.rdm(self.__addr, self.__dmmu_table10_msb, self.__dmmu_table10_lsb)
    @dmmu_table10.setter
    def dmmu_table10(self, value):
        return self.__MEM.wrm(self.__addr, self.__dmmu_table10_msb, self.__dmmu_table10_lsb, value)
class DMMU_TABLE11(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x570
        self.__dmmu_table11_lsb = 0
        self.__dmmu_table11_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def dmmu_table11(self):
        return self.__MEM.rdm(self.__addr, self.__dmmu_table11_msb, self.__dmmu_table11_lsb)
    @dmmu_table11.setter
    def dmmu_table11(self, value):
        return self.__MEM.wrm(self.__addr, self.__dmmu_table11_msb, self.__dmmu_table11_lsb, value)
class DMMU_TABLE12(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x574
        self.__dmmu_table12_lsb = 0
        self.__dmmu_table12_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def dmmu_table12(self):
        return self.__MEM.rdm(self.__addr, self.__dmmu_table12_msb, self.__dmmu_table12_lsb)
    @dmmu_table12.setter
    def dmmu_table12(self, value):
        return self.__MEM.wrm(self.__addr, self.__dmmu_table12_msb, self.__dmmu_table12_lsb, value)
class DMMU_TABLE13(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x578
        self.__dmmu_table13_lsb = 0
        self.__dmmu_table13_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def dmmu_table13(self):
        return self.__MEM.rdm(self.__addr, self.__dmmu_table13_msb, self.__dmmu_table13_lsb)
    @dmmu_table13.setter
    def dmmu_table13(self, value):
        return self.__MEM.wrm(self.__addr, self.__dmmu_table13_msb, self.__dmmu_table13_lsb, value)
class DMMU_TABLE14(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x57c
        self.__dmmu_table14_lsb = 0
        self.__dmmu_table14_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def dmmu_table14(self):
        return self.__MEM.rdm(self.__addr, self.__dmmu_table14_msb, self.__dmmu_table14_lsb)
    @dmmu_table14.setter
    def dmmu_table14(self, value):
        return self.__MEM.wrm(self.__addr, self.__dmmu_table14_msb, self.__dmmu_table14_lsb, value)
class DMMU_TABLE15(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x580
        self.__dmmu_table15_lsb = 0
        self.__dmmu_table15_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def dmmu_table15(self):
        return self.__MEM.rdm(self.__addr, self.__dmmu_table15_msb, self.__dmmu_table15_lsb)
    @dmmu_table15.setter
    def dmmu_table15(self, value):
        return self.__MEM.wrm(self.__addr, self.__dmmu_table15_msb, self.__dmmu_table15_lsb, value)
class PRO_INTRUSION_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x584
        self.__pro_intrusion_record_reset_n_lsb = 0
        self.__pro_intrusion_record_reset_n_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_intrusion_record_reset_n(self):
        return self.__MEM.rdm(self.__addr, self.__pro_intrusion_record_reset_n_msb, self.__pro_intrusion_record_reset_n_lsb)
    @pro_intrusion_record_reset_n.setter
    def pro_intrusion_record_reset_n(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_intrusion_record_reset_n_msb, self.__pro_intrusion_record_reset_n_lsb, value)
class PRO_INTRUSION_STATUS(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x588
        self.__pro_intrusion_record_lsb = 0
        self.__pro_intrusion_record_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_intrusion_record(self):
        return self.__MEM.rdm(self.__addr, self.__pro_intrusion_record_msb, self.__pro_intrusion_record_lsb)
    @pro_intrusion_record.setter
    def pro_intrusion_record(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_intrusion_record_msb, self.__pro_intrusion_record_lsb, value)
class APP_INTRUSION_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x58c
        self.__app_intrusion_record_reset_n_lsb = 0
        self.__app_intrusion_record_reset_n_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_intrusion_record_reset_n(self):
        return self.__MEM.rdm(self.__addr, self.__app_intrusion_record_reset_n_msb, self.__app_intrusion_record_reset_n_lsb)
    @app_intrusion_record_reset_n.setter
    def app_intrusion_record_reset_n(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_intrusion_record_reset_n_msb, self.__app_intrusion_record_reset_n_lsb, value)
class APP_INTRUSION_STATUS(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x590
        self.__app_intrusion_record_lsb = 0
        self.__app_intrusion_record_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_intrusion_record(self):
        return self.__MEM.rdm(self.__addr, self.__app_intrusion_record_msb, self.__app_intrusion_record_lsb)
    @app_intrusion_record.setter
    def app_intrusion_record(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_intrusion_record_msb, self.__app_intrusion_record_lsb, value)
class FRONT_END_MEM_PD(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x594
        self.__reg_pbus_mem_force_pd_lsb = 3
        self.__reg_pbus_mem_force_pd_msb = 3
        self.__reg_pbus_mem_force_pu_lsb = 2
        self.__reg_pbus_mem_force_pu_msb = 2
        self.__reg_agc_mem_force_pd_lsb = 1
        self.__reg_agc_mem_force_pd_msb = 1
        self.__reg_agc_mem_force_pu_lsb = 0
        self.__reg_agc_mem_force_pu_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_pbus_mem_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pbus_mem_force_pd_msb, self.__reg_pbus_mem_force_pd_lsb)
    @reg_pbus_mem_force_pd.setter
    def reg_pbus_mem_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pbus_mem_force_pd_msb, self.__reg_pbus_mem_force_pd_lsb, value)

    @property
    def reg_pbus_mem_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pbus_mem_force_pu_msb, self.__reg_pbus_mem_force_pu_lsb)
    @reg_pbus_mem_force_pu.setter
    def reg_pbus_mem_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pbus_mem_force_pu_msb, self.__reg_pbus_mem_force_pu_lsb, value)

    @property
    def reg_agc_mem_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_mem_force_pd_msb, self.__reg_agc_mem_force_pd_lsb)
    @reg_agc_mem_force_pd.setter
    def reg_agc_mem_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_mem_force_pd_msb, self.__reg_agc_mem_force_pd_lsb, value)

    @property
    def reg_agc_mem_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_mem_force_pu_msb, self.__reg_agc_mem_force_pu_lsb)
    @reg_agc_mem_force_pu.setter
    def reg_agc_mem_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_mem_force_pu_msb, self.__reg_agc_mem_force_pu_lsb, value)
class MMU_IA_INT_EN(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x598
        self.__mmu_ia_int_en_lsb = 0
        self.__mmu_ia_int_en_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def mmu_ia_int_en(self):
        return self.__MEM.rdm(self.__addr, self.__mmu_ia_int_en_msb, self.__mmu_ia_int_en_lsb)
    @mmu_ia_int_en.setter
    def mmu_ia_int_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__mmu_ia_int_en_msb, self.__mmu_ia_int_en_lsb, value)
class MPU_IA_INT_EN(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x59c
        self.__mpu_ia_int_en_lsb = 0
        self.__mpu_ia_int_en_msb = 16
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def mpu_ia_int_en(self):
        return self.__MEM.rdm(self.__addr, self.__mpu_ia_int_en_msb, self.__mpu_ia_int_en_lsb)
    @mpu_ia_int_en.setter
    def mpu_ia_int_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__mpu_ia_int_en_msb, self.__mpu_ia_int_en_lsb, value)
class CACHE_IA_INT_EN(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x5a0
        self.__cache_ia_int_en_lsb = 0
        self.__cache_ia_int_en_msb = 27
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def cache_ia_int_en(self):
        return self.__MEM.rdm(self.__addr, self.__cache_ia_int_en_msb, self.__cache_ia_int_en_lsb)
    @cache_ia_int_en.setter
    def cache_ia_int_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__cache_ia_int_en_msb, self.__cache_ia_int_en_lsb, value)
class SECURE_BOOT_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x5a4
        self.__sw_bootloader_sel_lsb = 0
        self.__sw_bootloader_sel_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sw_bootloader_sel(self):
        return self.__MEM.rdm(self.__addr, self.__sw_bootloader_sel_msb, self.__sw_bootloader_sel_lsb)
    @sw_bootloader_sel.setter
    def sw_bootloader_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__sw_bootloader_sel_msb, self.__sw_bootloader_sel_lsb, value)
class SPI_DMA_CHAN_SEL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x5a8
        self.__SPI3_DMA_CHAN_SEL_lsb = 4
        self.__SPI3_DMA_CHAN_SEL_msb = 5
        self.__SPI2_DMA_CHAN_SEL_lsb = 2
        self.__SPI2_DMA_CHAN_SEL_msb = 3
        self.__SPI1_DMA_CHAN_SEL_lsb = 0
        self.__SPI1_DMA_CHAN_SEL_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def SPI3_DMA_CHAN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__SPI3_DMA_CHAN_SEL_msb, self.__SPI3_DMA_CHAN_SEL_lsb)
    @SPI3_DMA_CHAN_SEL.setter
    def SPI3_DMA_CHAN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__SPI3_DMA_CHAN_SEL_msb, self.__SPI3_DMA_CHAN_SEL_lsb, value)

    @property
    def SPI2_DMA_CHAN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__SPI2_DMA_CHAN_SEL_msb, self.__SPI2_DMA_CHAN_SEL_lsb)
    @SPI2_DMA_CHAN_SEL.setter
    def SPI2_DMA_CHAN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__SPI2_DMA_CHAN_SEL_msb, self.__SPI2_DMA_CHAN_SEL_lsb, value)

    @property
    def SPI1_DMA_CHAN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__SPI1_DMA_CHAN_SEL_msb, self.__SPI1_DMA_CHAN_SEL_lsb)
    @SPI1_DMA_CHAN_SEL.setter
    def SPI1_DMA_CHAN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__SPI1_DMA_CHAN_SEL_msb, self.__SPI1_DMA_CHAN_SEL_lsb, value)
class PRO_VECBASE_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x5ac
        self.__pro_out_vecbase_sel_lsb = 0
        self.__pro_out_vecbase_sel_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_out_vecbase_sel(self):
        return self.__MEM.rdm(self.__addr, self.__pro_out_vecbase_sel_msb, self.__pro_out_vecbase_sel_lsb)
    @pro_out_vecbase_sel.setter
    def pro_out_vecbase_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_out_vecbase_sel_msb, self.__pro_out_vecbase_sel_lsb, value)
class PRO_VECBASE_SET(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x5b0
        self.__pro_out_vecbase_reg_lsb = 0
        self.__pro_out_vecbase_reg_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_out_vecbase_reg(self):
        return self.__MEM.rdm(self.__addr, self.__pro_out_vecbase_reg_msb, self.__pro_out_vecbase_reg_lsb)
    @pro_out_vecbase_reg.setter
    def pro_out_vecbase_reg(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_out_vecbase_reg_msb, self.__pro_out_vecbase_reg_lsb, value)
class APP_VECBASE_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x5b4
        self.__app_out_vecbase_sel_lsb = 0
        self.__app_out_vecbase_sel_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_out_vecbase_sel(self):
        return self.__MEM.rdm(self.__addr, self.__app_out_vecbase_sel_msb, self.__app_out_vecbase_sel_lsb)
    @app_out_vecbase_sel.setter
    def app_out_vecbase_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_out_vecbase_sel_msb, self.__app_out_vecbase_sel_lsb, value)
class APP_VECBASE_SET(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0x5b8
        self.__app_out_vecbase_reg_lsb = 0
        self.__app_out_vecbase_reg_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def app_out_vecbase_reg(self):
        return self.__MEM.rdm(self.__addr, self.__app_out_vecbase_reg_msb, self.__app_out_vecbase_reg_lsb)
    @app_out_vecbase_reg.setter
    def app_out_vecbase_reg(self, value):
        return self.__MEM.wrm(self.__addr, self.__app_out_vecbase_reg_msb, self.__app_out_vecbase_reg_lsb, value)
class DPORT_REG_DATE(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = DPORT_BASE + 0xffc
        self.__dport_reg_date_lsb = 0
        self.__dport_reg_date_msb = 27
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def dport_reg_date(self):
        return self.__MEM.rdm(self.__addr, self.__dport_reg_date_msb, self.__dport_reg_date_lsb)
    @dport_reg_date.setter
    def dport_reg_date(self, value):
        return self.__MEM.wrm(self.__addr, self.__dport_reg_date_msb, self.__dport_reg_date_lsb, value)
    @property
    def default_value(self):
        return 0x1605190
