from hal.common import *
from hal.hwregister.hwreg.CHIP723.addr_base import *
class SYSTEM(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.ROM_CTRL_0 = ROM_CTRL_0(self.channel, self.chipv)
        self.ROM_CTRL_1 = ROM_CTRL_1(self.channel, self.chipv)
        self.SRAM_CTRL_0 = SRAM_CTRL_0(self.channel, self.chipv)
        self.SRAM_CTRL_1 = SRAM_CTRL_1(self.channel, self.chipv)
        self.CPU_PERI_CLK_EN = CPU_PERI_CLK_EN(self.channel, self.chipv)
        self.CPU_PERI_RST_EN = CPU_PERI_RST_EN(self.channel, self.chipv)
        self.CPU_PER_CONF_REG = CPU_PER_CONF_REG(self.channel, self.chipv)
        self.JTAG_CTRL_0 = JTAG_CTRL_0(self.channel, self.chipv)
        self.JTAG_CTRL_1 = JTAG_CTRL_1(self.channel, self.chipv)
        self.JTAG_CTRL_2 = JTAG_CTRL_2(self.channel, self.chipv)
        self.JTAG_CTRL_3 = JTAG_CTRL_3(self.channel, self.chipv)
        self.JTAG_CTRL_4 = JTAG_CTRL_4(self.channel, self.chipv)
        self.JTAG_CTRL_5 = JTAG_CTRL_5(self.channel, self.chipv)
        self.JTAG_CTRL_6 = JTAG_CTRL_6(self.channel, self.chipv)
        self.JTAG_CTRL_7 = JTAG_CTRL_7(self.channel, self.chipv)
        self.MEM_PD_MASK_REG = MEM_PD_MASK_REG(self.channel, self.chipv)
        self.PERIP_CLK_EN0 = PERIP_CLK_EN0(self.channel, self.chipv)
        self.PERIP_CLK_EN1 = PERIP_CLK_EN1(self.channel, self.chipv)
        self.PERIP_RST_EN0 = PERIP_RST_EN0(self.channel, self.chipv)
        self.PERIP_RST_EN1 = PERIP_RST_EN1(self.channel, self.chipv)
        self.BT_LPCK_DIV_INT = BT_LPCK_DIV_INT(self.channel, self.chipv)
        self.BT_LPCK_DIV_FRAC = BT_LPCK_DIV_FRAC(self.channel, self.chipv)
        self.CPU_INTR_FROM_CPU_0_REG = CPU_INTR_FROM_CPU_0_REG(self.channel, self.chipv)
        self.CPU_INTR_FROM_CPU_1_REG = CPU_INTR_FROM_CPU_1_REG(self.channel, self.chipv)
        self.CPU_INTR_FROM_CPU_2_REG = CPU_INTR_FROM_CPU_2_REG(self.channel, self.chipv)
        self.CPU_INTR_FROM_CPU_3_REG = CPU_INTR_FROM_CPU_3_REG(self.channel, self.chipv)
        self.RSA_PD_CTRL_REG = RSA_PD_CTRL_REG(self.channel, self.chipv)
        self.BUSTOEXTMEM_ENA = BUSTOEXTMEM_ENA(self.channel, self.chipv)
        self.Cache_Control = Cache_Control(self.channel, self.chipv)
        self.External_Device_Encrypt_Decrypt_Control = External_Device_Encrypt_Decrypt_Control(self.channel, self.chipv)
        self.RTC_FASTMEM_CONFIG = RTC_FASTMEM_CONFIG(self.channel, self.chipv)
        self.RTC_FASTMEM_CRC = RTC_FASTMEM_CRC(self.channel, self.chipv)
        self.Redundant_ECO_Ctrl = Redundant_ECO_Ctrl(self.channel, self.chipv)
        self.CLOCK_GATE_REG = CLOCK_GATE_REG(self.channel, self.chipv)
        self.SRAM_CTRL_2 = SRAM_CTRL_2(self.channel, self.chipv)
        self.SYSCLK_CONF = SYSCLK_CONF(self.channel, self.chipv)
        self.SYSTEM_REG_DATE = SYSTEM_REG_DATE(self.channel, self.chipv)
class ROM_CTRL_0(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x0
        self.__rom_fo_lsb = 0
        self.__rom_fo_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rom_fo(self):
        return self.__MEM.rdm(self.__addr, self.__rom_fo_msb, self.__rom_fo_lsb)
    @rom_fo.setter
    def rom_fo(self, value):
        return self.__MEM.wrm(self.__addr, self.__rom_fo_msb, self.__rom_fo_lsb, value)
class ROM_CTRL_1(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x4
        self.__rom_force_pu_lsb = 2
        self.__rom_force_pu_msb = 3
        self.__rom_force_pd_lsb = 0
        self.__rom_force_pd_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rom_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__rom_force_pu_msb, self.__rom_force_pu_lsb)
    @rom_force_pu.setter
    def rom_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__rom_force_pu_msb, self.__rom_force_pu_lsb, value)

    @property
    def rom_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__rom_force_pd_msb, self.__rom_force_pd_lsb)
    @rom_force_pd.setter
    def rom_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__rom_force_pd_msb, self.__rom_force_pd_lsb, value)
class SRAM_CTRL_0(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x8
        self.__sram_fo_lsb = 0
        self.__sram_fo_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_fo(self):
        return self.__MEM.rdm(self.__addr, self.__sram_fo_msb, self.__sram_fo_lsb)
    @sram_fo.setter
    def sram_fo(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_fo_msb, self.__sram_fo_lsb, value)
class SRAM_CTRL_1(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0xc
        self.__sram_force_pd_lsb = 0
        self.__sram_force_pd_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__sram_force_pd_msb, self.__sram_force_pd_lsb)
    @sram_force_pd.setter
    def sram_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_force_pd_msb, self.__sram_force_pd_lsb, value)
class CPU_PERI_CLK_EN(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x10
        self.__clk_en_dedicated_gpio_lsb = 7
        self.__clk_en_dedicated_gpio_msb = 7
        self.__clk_en_assist_debug_lsb = 6
        self.__clk_en_assist_debug_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def clk_en_dedicated_gpio(self):
        return self.__MEM.rdm(self.__addr, self.__clk_en_dedicated_gpio_msb, self.__clk_en_dedicated_gpio_lsb)
    @clk_en_dedicated_gpio.setter
    def clk_en_dedicated_gpio(self, value):
        return self.__MEM.wrm(self.__addr, self.__clk_en_dedicated_gpio_msb, self.__clk_en_dedicated_gpio_lsb, value)

    @property
    def clk_en_assist_debug(self):
        return self.__MEM.rdm(self.__addr, self.__clk_en_assist_debug_msb, self.__clk_en_assist_debug_lsb)
    @clk_en_assist_debug.setter
    def clk_en_assist_debug(self, value):
        return self.__MEM.wrm(self.__addr, self.__clk_en_assist_debug_msb, self.__clk_en_assist_debug_lsb, value)
class CPU_PERI_RST_EN(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x14
        self.__rst_en_dedicated_gpio_lsb = 7
        self.__rst_en_dedicated_gpio_msb = 7
        self.__rst_en_assist_debug_lsb = 6
        self.__rst_en_assist_debug_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rst_en_dedicated_gpio(self):
        return self.__MEM.rdm(self.__addr, self.__rst_en_dedicated_gpio_msb, self.__rst_en_dedicated_gpio_lsb)
    @rst_en_dedicated_gpio.setter
    def rst_en_dedicated_gpio(self, value):
        return self.__MEM.wrm(self.__addr, self.__rst_en_dedicated_gpio_msb, self.__rst_en_dedicated_gpio_lsb, value)

    @property
    def rst_en_assist_debug(self):
        return self.__MEM.rdm(self.__addr, self.__rst_en_assist_debug_msb, self.__rst_en_assist_debug_lsb)
    @rst_en_assist_debug.setter
    def rst_en_assist_debug(self, value):
        return self.__MEM.wrm(self.__addr, self.__rst_en_assist_debug_msb, self.__rst_en_assist_debug_lsb, value)
class CPU_PER_CONF_REG(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x18
        self.__reg_cpu_waiti_delay_num_lsb = 4
        self.__reg_cpu_waiti_delay_num_msb = 7
        self.__reg_cpu_wait_mode_force_on_lsb = 3
        self.__reg_cpu_wait_mode_force_on_msb = 3
        self.__reg_pll_freq_sel_lsb = 2
        self.__reg_pll_freq_sel_msb = 2
        self.__reg_cpuperiod_sel_lsb = 0
        self.__reg_cpuperiod_sel_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_cpu_waiti_delay_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cpu_waiti_delay_num_msb, self.__reg_cpu_waiti_delay_num_lsb)
    @reg_cpu_waiti_delay_num.setter
    def reg_cpu_waiti_delay_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cpu_waiti_delay_num_msb, self.__reg_cpu_waiti_delay_num_lsb, value)

    @property
    def reg_cpu_wait_mode_force_on(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cpu_wait_mode_force_on_msb, self.__reg_cpu_wait_mode_force_on_lsb)
    @reg_cpu_wait_mode_force_on.setter
    def reg_cpu_wait_mode_force_on(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cpu_wait_mode_force_on_msb, self.__reg_cpu_wait_mode_force_on_lsb, value)

    @property
    def reg_pll_freq_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pll_freq_sel_msb, self.__reg_pll_freq_sel_lsb)
    @reg_pll_freq_sel.setter
    def reg_pll_freq_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pll_freq_sel_msb, self.__reg_pll_freq_sel_lsb, value)

    @property
    def reg_cpuperiod_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cpuperiod_sel_msb, self.__reg_cpuperiod_sel_lsb)
    @reg_cpuperiod_sel.setter
    def reg_cpuperiod_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cpuperiod_sel_msb, self.__reg_cpuperiod_sel_lsb, value)
class JTAG_CTRL_0(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x1c
        self.__cancel_efuse_disable_jtag_temporary_0_lsb = 0
        self.__cancel_efuse_disable_jtag_temporary_0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def cancel_efuse_disable_jtag_temporary_0(self):
        return self.__MEM.rdm(self.__addr, self.__cancel_efuse_disable_jtag_temporary_0_msb, self.__cancel_efuse_disable_jtag_temporary_0_lsb)
    @cancel_efuse_disable_jtag_temporary_0.setter
    def cancel_efuse_disable_jtag_temporary_0(self, value):
        return self.__MEM.wrm(self.__addr, self.__cancel_efuse_disable_jtag_temporary_0_msb, self.__cancel_efuse_disable_jtag_temporary_0_lsb, value)
class JTAG_CTRL_1(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x20
        self.__cancel_efuse_disable_jtag_temporary_1_lsb = 0
        self.__cancel_efuse_disable_jtag_temporary_1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def cancel_efuse_disable_jtag_temporary_1(self):
        return self.__MEM.rdm(self.__addr, self.__cancel_efuse_disable_jtag_temporary_1_msb, self.__cancel_efuse_disable_jtag_temporary_1_lsb)
    @cancel_efuse_disable_jtag_temporary_1.setter
    def cancel_efuse_disable_jtag_temporary_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__cancel_efuse_disable_jtag_temporary_1_msb, self.__cancel_efuse_disable_jtag_temporary_1_lsb, value)
class JTAG_CTRL_2(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x24
        self.__cancel_efuse_disable_jtag_temporary_2_lsb = 0
        self.__cancel_efuse_disable_jtag_temporary_2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def cancel_efuse_disable_jtag_temporary_2(self):
        return self.__MEM.rdm(self.__addr, self.__cancel_efuse_disable_jtag_temporary_2_msb, self.__cancel_efuse_disable_jtag_temporary_2_lsb)
    @cancel_efuse_disable_jtag_temporary_2.setter
    def cancel_efuse_disable_jtag_temporary_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__cancel_efuse_disable_jtag_temporary_2_msb, self.__cancel_efuse_disable_jtag_temporary_2_lsb, value)
class JTAG_CTRL_3(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x28
        self.__cancel_efuse_disable_jtag_temporary_3_lsb = 0
        self.__cancel_efuse_disable_jtag_temporary_3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def cancel_efuse_disable_jtag_temporary_3(self):
        return self.__MEM.rdm(self.__addr, self.__cancel_efuse_disable_jtag_temporary_3_msb, self.__cancel_efuse_disable_jtag_temporary_3_lsb)
    @cancel_efuse_disable_jtag_temporary_3.setter
    def cancel_efuse_disable_jtag_temporary_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__cancel_efuse_disable_jtag_temporary_3_msb, self.__cancel_efuse_disable_jtag_temporary_3_lsb, value)
class JTAG_CTRL_4(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x2c
        self.__cancel_efuse_disable_jtag_temporary_4_lsb = 0
        self.__cancel_efuse_disable_jtag_temporary_4_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def cancel_efuse_disable_jtag_temporary_4(self):
        return self.__MEM.rdm(self.__addr, self.__cancel_efuse_disable_jtag_temporary_4_msb, self.__cancel_efuse_disable_jtag_temporary_4_lsb)
    @cancel_efuse_disable_jtag_temporary_4.setter
    def cancel_efuse_disable_jtag_temporary_4(self, value):
        return self.__MEM.wrm(self.__addr, self.__cancel_efuse_disable_jtag_temporary_4_msb, self.__cancel_efuse_disable_jtag_temporary_4_lsb, value)
class JTAG_CTRL_5(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x30
        self.__cancel_efuse_disable_jtag_temporary_5_lsb = 0
        self.__cancel_efuse_disable_jtag_temporary_5_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def cancel_efuse_disable_jtag_temporary_5(self):
        return self.__MEM.rdm(self.__addr, self.__cancel_efuse_disable_jtag_temporary_5_msb, self.__cancel_efuse_disable_jtag_temporary_5_lsb)
    @cancel_efuse_disable_jtag_temporary_5.setter
    def cancel_efuse_disable_jtag_temporary_5(self, value):
        return self.__MEM.wrm(self.__addr, self.__cancel_efuse_disable_jtag_temporary_5_msb, self.__cancel_efuse_disable_jtag_temporary_5_lsb, value)
class JTAG_CTRL_6(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x34
        self.__cancel_efuse_disable_jtag_temporary_6_lsb = 0
        self.__cancel_efuse_disable_jtag_temporary_6_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def cancel_efuse_disable_jtag_temporary_6(self):
        return self.__MEM.rdm(self.__addr, self.__cancel_efuse_disable_jtag_temporary_6_msb, self.__cancel_efuse_disable_jtag_temporary_6_lsb)
    @cancel_efuse_disable_jtag_temporary_6.setter
    def cancel_efuse_disable_jtag_temporary_6(self, value):
        return self.__MEM.wrm(self.__addr, self.__cancel_efuse_disable_jtag_temporary_6_msb, self.__cancel_efuse_disable_jtag_temporary_6_lsb, value)
class JTAG_CTRL_7(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x38
        self.__cancel_efuse_disable_jtag_temporary_7_lsb = 0
        self.__cancel_efuse_disable_jtag_temporary_7_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def cancel_efuse_disable_jtag_temporary_7(self):
        return self.__MEM.rdm(self.__addr, self.__cancel_efuse_disable_jtag_temporary_7_msb, self.__cancel_efuse_disable_jtag_temporary_7_lsb)
    @cancel_efuse_disable_jtag_temporary_7.setter
    def cancel_efuse_disable_jtag_temporary_7(self, value):
        return self.__MEM.wrm(self.__addr, self.__cancel_efuse_disable_jtag_temporary_7_msb, self.__cancel_efuse_disable_jtag_temporary_7_lsb, value)
class MEM_PD_MASK_REG(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x3c
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
class PERIP_CLK_EN0(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x40
        self.__spi4_clk_en_lsb = 31
        self.__spi4_clk_en_msb = 31
        self.__adc2_arb_clk_en_lsb = 30
        self.__adc2_arb_clk_en_msb = 30
        self.__systimer_clk_en_lsb = 29
        self.__systimer_clk_en_msb = 29
        self.__apb_saradc_clk_en_lsb = 28
        self.__apb_saradc_clk_en_msb = 28
        self.__spi3_dma_clk_en_lsb = 27
        self.__spi3_dma_clk_en_msb = 27
        self.__pwm3_clk_en_lsb = 26
        self.__pwm3_clk_en_msb = 26
        self.__pwm2_clk_en_lsb = 25
        self.__pwm2_clk_en_msb = 25
        self.__uart_mem_clk_en_lsb = 24
        self.__uart_mem_clk_en_msb = 24
        self.__usb_clk_en_lsb = 23
        self.__usb_clk_en_msb = 23
        self.__spi2_dma_clk_en_lsb = 22
        self.__spi2_dma_clk_en_msb = 22
        self.__i2s1_clk_en_lsb = 21
        self.__i2s1_clk_en_msb = 21
        self.__pwm1_clk_en_lsb = 20
        self.__pwm1_clk_en_msb = 20
        self.__can_clk_en_lsb = 19
        self.__can_clk_en_msb = 19
        self.__i2c_ext1_clk_en_lsb = 18
        self.__i2c_ext1_clk_en_msb = 18
        self.__pwm0_clk_en_lsb = 17
        self.__pwm0_clk_en_msb = 17
        self.__spi3_clk_en_lsb = 16
        self.__spi3_clk_en_msb = 16
        self.__timergroup1_clk_en_lsb = 15
        self.__timergroup1_clk_en_msb = 15
        self.__efuse_clk_en_lsb = 14
        self.__efuse_clk_en_msb = 14
        self.__timergroup_clk_en_lsb = 13
        self.__timergroup_clk_en_msb = 13
        self.__uhci1_clk_en_lsb = 12
        self.__uhci1_clk_en_msb = 12
        self.__ledc_clk_en_lsb = 11
        self.__ledc_clk_en_msb = 11
        self.__pcnt_clk_en_lsb = 10
        self.__pcnt_clk_en_msb = 10
        self.__rmt_clk_en_lsb = 9
        self.__rmt_clk_en_msb = 9
        self.__uhci0_clk_en_lsb = 8
        self.__uhci0_clk_en_msb = 8
        self.__i2c_ext0_clk_en_lsb = 7
        self.__i2c_ext0_clk_en_msb = 7
        self.__spi2_clk_en_lsb = 6
        self.__spi2_clk_en_msb = 6
        self.__uart1_clk_en_lsb = 5
        self.__uart1_clk_en_msb = 5
        self.__i2s0_clk_en_lsb = 4
        self.__i2s0_clk_en_msb = 4
        self.__wdg_clk_en_lsb = 3
        self.__wdg_clk_en_msb = 3
        self.__uart_clk_en_lsb = 2
        self.__uart_clk_en_msb = 2
        self.__spi01_clk_en_lsb = 1
        self.__spi01_clk_en_msb = 1
        self.__timers_clk_en_lsb = 0
        self.__timers_clk_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def spi4_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__spi4_clk_en_msb, self.__spi4_clk_en_lsb)
    @spi4_clk_en.setter
    def spi4_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi4_clk_en_msb, self.__spi4_clk_en_lsb, value)

    @property
    def adc2_arb_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__adc2_arb_clk_en_msb, self.__adc2_arb_clk_en_lsb)
    @adc2_arb_clk_en.setter
    def adc2_arb_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__adc2_arb_clk_en_msb, self.__adc2_arb_clk_en_lsb, value)

    @property
    def systimer_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__systimer_clk_en_msb, self.__systimer_clk_en_lsb)
    @systimer_clk_en.setter
    def systimer_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__systimer_clk_en_msb, self.__systimer_clk_en_lsb, value)

    @property
    def apb_saradc_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__apb_saradc_clk_en_msb, self.__apb_saradc_clk_en_lsb)
    @apb_saradc_clk_en.setter
    def apb_saradc_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__apb_saradc_clk_en_msb, self.__apb_saradc_clk_en_lsb, value)

    @property
    def spi3_dma_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__spi3_dma_clk_en_msb, self.__spi3_dma_clk_en_lsb)
    @spi3_dma_clk_en.setter
    def spi3_dma_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi3_dma_clk_en_msb, self.__spi3_dma_clk_en_lsb, value)

    @property
    def pwm3_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__pwm3_clk_en_msb, self.__pwm3_clk_en_lsb)
    @pwm3_clk_en.setter
    def pwm3_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__pwm3_clk_en_msb, self.__pwm3_clk_en_lsb, value)

    @property
    def pwm2_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__pwm2_clk_en_msb, self.__pwm2_clk_en_lsb)
    @pwm2_clk_en.setter
    def pwm2_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__pwm2_clk_en_msb, self.__pwm2_clk_en_lsb, value)

    @property
    def uart_mem_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__uart_mem_clk_en_msb, self.__uart_mem_clk_en_lsb)
    @uart_mem_clk_en.setter
    def uart_mem_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_mem_clk_en_msb, self.__uart_mem_clk_en_lsb, value)

    @property
    def usb_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__usb_clk_en_msb, self.__usb_clk_en_lsb)
    @usb_clk_en.setter
    def usb_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__usb_clk_en_msb, self.__usb_clk_en_lsb, value)

    @property
    def spi2_dma_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__spi2_dma_clk_en_msb, self.__spi2_dma_clk_en_lsb)
    @spi2_dma_clk_en.setter
    def spi2_dma_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi2_dma_clk_en_msb, self.__spi2_dma_clk_en_lsb, value)

    @property
    def i2s1_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__i2s1_clk_en_msb, self.__i2s1_clk_en_lsb)
    @i2s1_clk_en.setter
    def i2s1_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s1_clk_en_msb, self.__i2s1_clk_en_lsb, value)

    @property
    def pwm1_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__pwm1_clk_en_msb, self.__pwm1_clk_en_lsb)
    @pwm1_clk_en.setter
    def pwm1_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__pwm1_clk_en_msb, self.__pwm1_clk_en_lsb, value)

    @property
    def can_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__can_clk_en_msb, self.__can_clk_en_lsb)
    @can_clk_en.setter
    def can_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__can_clk_en_msb, self.__can_clk_en_lsb, value)

    @property
    def i2c_ext1_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__i2c_ext1_clk_en_msb, self.__i2c_ext1_clk_en_lsb)
    @i2c_ext1_clk_en.setter
    def i2c_ext1_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2c_ext1_clk_en_msb, self.__i2c_ext1_clk_en_lsb, value)

    @property
    def pwm0_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__pwm0_clk_en_msb, self.__pwm0_clk_en_lsb)
    @pwm0_clk_en.setter
    def pwm0_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__pwm0_clk_en_msb, self.__pwm0_clk_en_lsb, value)

    @property
    def spi3_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__spi3_clk_en_msb, self.__spi3_clk_en_lsb)
    @spi3_clk_en.setter
    def spi3_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi3_clk_en_msb, self.__spi3_clk_en_lsb, value)

    @property
    def timergroup1_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__timergroup1_clk_en_msb, self.__timergroup1_clk_en_lsb)
    @timergroup1_clk_en.setter
    def timergroup1_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__timergroup1_clk_en_msb, self.__timergroup1_clk_en_lsb, value)

    @property
    def efuse_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_clk_en_msb, self.__efuse_clk_en_lsb)
    @efuse_clk_en.setter
    def efuse_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_clk_en_msb, self.__efuse_clk_en_lsb, value)

    @property
    def timergroup_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__timergroup_clk_en_msb, self.__timergroup_clk_en_lsb)
    @timergroup_clk_en.setter
    def timergroup_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__timergroup_clk_en_msb, self.__timergroup_clk_en_lsb, value)

    @property
    def uhci1_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__uhci1_clk_en_msb, self.__uhci1_clk_en_lsb)
    @uhci1_clk_en.setter
    def uhci1_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__uhci1_clk_en_msb, self.__uhci1_clk_en_lsb, value)

    @property
    def ledc_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__ledc_clk_en_msb, self.__ledc_clk_en_lsb)
    @ledc_clk_en.setter
    def ledc_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__ledc_clk_en_msb, self.__ledc_clk_en_lsb, value)

    @property
    def pcnt_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__pcnt_clk_en_msb, self.__pcnt_clk_en_lsb)
    @pcnt_clk_en.setter
    def pcnt_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__pcnt_clk_en_msb, self.__pcnt_clk_en_lsb, value)

    @property
    def rmt_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__rmt_clk_en_msb, self.__rmt_clk_en_lsb)
    @rmt_clk_en.setter
    def rmt_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__rmt_clk_en_msb, self.__rmt_clk_en_lsb, value)

    @property
    def uhci0_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__uhci0_clk_en_msb, self.__uhci0_clk_en_lsb)
    @uhci0_clk_en.setter
    def uhci0_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__uhci0_clk_en_msb, self.__uhci0_clk_en_lsb, value)

    @property
    def i2c_ext0_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__i2c_ext0_clk_en_msb, self.__i2c_ext0_clk_en_lsb)
    @i2c_ext0_clk_en.setter
    def i2c_ext0_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2c_ext0_clk_en_msb, self.__i2c_ext0_clk_en_lsb, value)

    @property
    def spi2_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__spi2_clk_en_msb, self.__spi2_clk_en_lsb)
    @spi2_clk_en.setter
    def spi2_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi2_clk_en_msb, self.__spi2_clk_en_lsb, value)

    @property
    def uart1_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__uart1_clk_en_msb, self.__uart1_clk_en_lsb)
    @uart1_clk_en.setter
    def uart1_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart1_clk_en_msb, self.__uart1_clk_en_lsb, value)

    @property
    def i2s0_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__i2s0_clk_en_msb, self.__i2s0_clk_en_lsb)
    @i2s0_clk_en.setter
    def i2s0_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s0_clk_en_msb, self.__i2s0_clk_en_lsb, value)

    @property
    def wdg_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__wdg_clk_en_msb, self.__wdg_clk_en_lsb)
    @wdg_clk_en.setter
    def wdg_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__wdg_clk_en_msb, self.__wdg_clk_en_lsb, value)

    @property
    def uart_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__uart_clk_en_msb, self.__uart_clk_en_lsb)
    @uart_clk_en.setter
    def uart_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_clk_en_msb, self.__uart_clk_en_lsb, value)

    @property
    def spi01_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__spi01_clk_en_msb, self.__spi01_clk_en_lsb)
    @spi01_clk_en.setter
    def spi01_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi01_clk_en_msb, self.__spi01_clk_en_lsb, value)

    @property
    def timers_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__timers_clk_en_msb, self.__timers_clk_en_lsb)
    @timers_clk_en.setter
    def timers_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__timers_clk_en_msb, self.__timers_clk_en_lsb, value)
class PERIP_CLK_EN1(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x44
        self.__crypto_dma_clk_en_lsb = 6
        self.__crypto_dma_clk_en_msb = 6
        self.__crypto_hmac_clk_en_lsb = 5
        self.__crypto_hmac_clk_en_msb = 5
        self.__crypto_ds_clk_en_lsb = 4
        self.__crypto_ds_clk_en_msb = 4
        self.__crypto_rsa_clk_en_lsb = 3
        self.__crypto_rsa_clk_en_msb = 3
        self.__crypto_sha_clk_en_lsb = 2
        self.__crypto_sha_clk_en_msb = 2
        self.__crypto_aes_clk_en_lsb = 1
        self.__crypto_aes_clk_en_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def crypto_dma_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__crypto_dma_clk_en_msb, self.__crypto_dma_clk_en_lsb)
    @crypto_dma_clk_en.setter
    def crypto_dma_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__crypto_dma_clk_en_msb, self.__crypto_dma_clk_en_lsb, value)

    @property
    def crypto_hmac_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__crypto_hmac_clk_en_msb, self.__crypto_hmac_clk_en_lsb)
    @crypto_hmac_clk_en.setter
    def crypto_hmac_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__crypto_hmac_clk_en_msb, self.__crypto_hmac_clk_en_lsb, value)

    @property
    def crypto_ds_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__crypto_ds_clk_en_msb, self.__crypto_ds_clk_en_lsb)
    @crypto_ds_clk_en.setter
    def crypto_ds_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__crypto_ds_clk_en_msb, self.__crypto_ds_clk_en_lsb, value)

    @property
    def crypto_rsa_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__crypto_rsa_clk_en_msb, self.__crypto_rsa_clk_en_lsb)
    @crypto_rsa_clk_en.setter
    def crypto_rsa_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__crypto_rsa_clk_en_msb, self.__crypto_rsa_clk_en_lsb, value)

    @property
    def crypto_sha_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__crypto_sha_clk_en_msb, self.__crypto_sha_clk_en_lsb)
    @crypto_sha_clk_en.setter
    def crypto_sha_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__crypto_sha_clk_en_msb, self.__crypto_sha_clk_en_lsb, value)

    @property
    def crypto_aes_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__crypto_aes_clk_en_msb, self.__crypto_aes_clk_en_lsb)
    @crypto_aes_clk_en.setter
    def crypto_aes_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__crypto_aes_clk_en_msb, self.__crypto_aes_clk_en_lsb, value)
class PERIP_RST_EN0(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x48
        self.__spi4_rst_lsb = 31
        self.__spi4_rst_msb = 31
        self.__adc2_arb_rst_lsb = 30
        self.__adc2_arb_rst_msb = 30
        self.__systimer_rst_lsb = 29
        self.__systimer_rst_msb = 29
        self.__apb_saradc_rst_lsb = 28
        self.__apb_saradc_rst_msb = 28
        self.__spi3_dma_rst_lsb = 27
        self.__spi3_dma_rst_msb = 27
        self.__pwm3_rst_lsb = 26
        self.__pwm3_rst_msb = 26
        self.__pwm2_rst_lsb = 25
        self.__pwm2_rst_msb = 25
        self.__uart_mem_rst_lsb = 24
        self.__uart_mem_rst_msb = 24
        self.__usb_rst_lsb = 23
        self.__usb_rst_msb = 23
        self.__spi2_dma_rst_lsb = 22
        self.__spi2_dma_rst_msb = 22
        self.__i2s1_rst_lsb = 21
        self.__i2s1_rst_msb = 21
        self.__pwm1_rst_lsb = 20
        self.__pwm1_rst_msb = 20
        self.__can_rst_lsb = 19
        self.__can_rst_msb = 19
        self.__i2c_ext1_rst_lsb = 18
        self.__i2c_ext1_rst_msb = 18
        self.__pwm0_rst_lsb = 17
        self.__pwm0_rst_msb = 17
        self.__spi3_rst_lsb = 16
        self.__spi3_rst_msb = 16
        self.__timergroup1_rst_lsb = 15
        self.__timergroup1_rst_msb = 15
        self.__efuse_rst_lsb = 14
        self.__efuse_rst_msb = 14
        self.__timergroup_rst_lsb = 13
        self.__timergroup_rst_msb = 13
        self.__uhci1_rst_lsb = 12
        self.__uhci1_rst_msb = 12
        self.__ledc_rst_lsb = 11
        self.__ledc_rst_msb = 11
        self.__pcnt_rst_lsb = 10
        self.__pcnt_rst_msb = 10
        self.__rmt_rst_lsb = 9
        self.__rmt_rst_msb = 9
        self.__uhci0_rst_lsb = 8
        self.__uhci0_rst_msb = 8
        self.__i2c_ext0_rst_lsb = 7
        self.__i2c_ext0_rst_msb = 7
        self.__spi2_rst_lsb = 6
        self.__spi2_rst_msb = 6
        self.__uart1_rst_lsb = 5
        self.__uart1_rst_msb = 5
        self.__i2s0_rst_lsb = 4
        self.__i2s0_rst_msb = 4
        self.__wdg_rst_lsb = 3
        self.__wdg_rst_msb = 3
        self.__uart_rst_lsb = 2
        self.__uart_rst_msb = 2
        self.__spi01_rst_lsb = 1
        self.__spi01_rst_msb = 1
        self.__timers_rst_lsb = 0
        self.__timers_rst_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def spi4_rst(self):
        return self.__MEM.rdm(self.__addr, self.__spi4_rst_msb, self.__spi4_rst_lsb)
    @spi4_rst.setter
    def spi4_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi4_rst_msb, self.__spi4_rst_lsb, value)

    @property
    def adc2_arb_rst(self):
        return self.__MEM.rdm(self.__addr, self.__adc2_arb_rst_msb, self.__adc2_arb_rst_lsb)
    @adc2_arb_rst.setter
    def adc2_arb_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__adc2_arb_rst_msb, self.__adc2_arb_rst_lsb, value)

    @property
    def systimer_rst(self):
        return self.__MEM.rdm(self.__addr, self.__systimer_rst_msb, self.__systimer_rst_lsb)
    @systimer_rst.setter
    def systimer_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__systimer_rst_msb, self.__systimer_rst_lsb, value)

    @property
    def apb_saradc_rst(self):
        return self.__MEM.rdm(self.__addr, self.__apb_saradc_rst_msb, self.__apb_saradc_rst_lsb)
    @apb_saradc_rst.setter
    def apb_saradc_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__apb_saradc_rst_msb, self.__apb_saradc_rst_lsb, value)

    @property
    def spi3_dma_rst(self):
        return self.__MEM.rdm(self.__addr, self.__spi3_dma_rst_msb, self.__spi3_dma_rst_lsb)
    @spi3_dma_rst.setter
    def spi3_dma_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi3_dma_rst_msb, self.__spi3_dma_rst_lsb, value)

    @property
    def pwm3_rst(self):
        return self.__MEM.rdm(self.__addr, self.__pwm3_rst_msb, self.__pwm3_rst_lsb)
    @pwm3_rst.setter
    def pwm3_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__pwm3_rst_msb, self.__pwm3_rst_lsb, value)

    @property
    def pwm2_rst(self):
        return self.__MEM.rdm(self.__addr, self.__pwm2_rst_msb, self.__pwm2_rst_lsb)
    @pwm2_rst.setter
    def pwm2_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__pwm2_rst_msb, self.__pwm2_rst_lsb, value)

    @property
    def uart_mem_rst(self):
        return self.__MEM.rdm(self.__addr, self.__uart_mem_rst_msb, self.__uart_mem_rst_lsb)
    @uart_mem_rst.setter
    def uart_mem_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_mem_rst_msb, self.__uart_mem_rst_lsb, value)

    @property
    def usb_rst(self):
        return self.__MEM.rdm(self.__addr, self.__usb_rst_msb, self.__usb_rst_lsb)
    @usb_rst.setter
    def usb_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__usb_rst_msb, self.__usb_rst_lsb, value)

    @property
    def spi2_dma_rst(self):
        return self.__MEM.rdm(self.__addr, self.__spi2_dma_rst_msb, self.__spi2_dma_rst_lsb)
    @spi2_dma_rst.setter
    def spi2_dma_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi2_dma_rst_msb, self.__spi2_dma_rst_lsb, value)

    @property
    def i2s1_rst(self):
        return self.__MEM.rdm(self.__addr, self.__i2s1_rst_msb, self.__i2s1_rst_lsb)
    @i2s1_rst.setter
    def i2s1_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s1_rst_msb, self.__i2s1_rst_lsb, value)

    @property
    def pwm1_rst(self):
        return self.__MEM.rdm(self.__addr, self.__pwm1_rst_msb, self.__pwm1_rst_lsb)
    @pwm1_rst.setter
    def pwm1_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__pwm1_rst_msb, self.__pwm1_rst_lsb, value)

    @property
    def can_rst(self):
        return self.__MEM.rdm(self.__addr, self.__can_rst_msb, self.__can_rst_lsb)
    @can_rst.setter
    def can_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__can_rst_msb, self.__can_rst_lsb, value)

    @property
    def i2c_ext1_rst(self):
        return self.__MEM.rdm(self.__addr, self.__i2c_ext1_rst_msb, self.__i2c_ext1_rst_lsb)
    @i2c_ext1_rst.setter
    def i2c_ext1_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2c_ext1_rst_msb, self.__i2c_ext1_rst_lsb, value)

    @property
    def pwm0_rst(self):
        return self.__MEM.rdm(self.__addr, self.__pwm0_rst_msb, self.__pwm0_rst_lsb)
    @pwm0_rst.setter
    def pwm0_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__pwm0_rst_msb, self.__pwm0_rst_lsb, value)

    @property
    def spi3_rst(self):
        return self.__MEM.rdm(self.__addr, self.__spi3_rst_msb, self.__spi3_rst_lsb)
    @spi3_rst.setter
    def spi3_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi3_rst_msb, self.__spi3_rst_lsb, value)

    @property
    def timergroup1_rst(self):
        return self.__MEM.rdm(self.__addr, self.__timergroup1_rst_msb, self.__timergroup1_rst_lsb)
    @timergroup1_rst.setter
    def timergroup1_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__timergroup1_rst_msb, self.__timergroup1_rst_lsb, value)

    @property
    def efuse_rst(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_rst_msb, self.__efuse_rst_lsb)
    @efuse_rst.setter
    def efuse_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_rst_msb, self.__efuse_rst_lsb, value)

    @property
    def timergroup_rst(self):
        return self.__MEM.rdm(self.__addr, self.__timergroup_rst_msb, self.__timergroup_rst_lsb)
    @timergroup_rst.setter
    def timergroup_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__timergroup_rst_msb, self.__timergroup_rst_lsb, value)

    @property
    def uhci1_rst(self):
        return self.__MEM.rdm(self.__addr, self.__uhci1_rst_msb, self.__uhci1_rst_lsb)
    @uhci1_rst.setter
    def uhci1_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__uhci1_rst_msb, self.__uhci1_rst_lsb, value)

    @property
    def ledc_rst(self):
        return self.__MEM.rdm(self.__addr, self.__ledc_rst_msb, self.__ledc_rst_lsb)
    @ledc_rst.setter
    def ledc_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__ledc_rst_msb, self.__ledc_rst_lsb, value)

    @property
    def pcnt_rst(self):
        return self.__MEM.rdm(self.__addr, self.__pcnt_rst_msb, self.__pcnt_rst_lsb)
    @pcnt_rst.setter
    def pcnt_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__pcnt_rst_msb, self.__pcnt_rst_lsb, value)

    @property
    def rmt_rst(self):
        return self.__MEM.rdm(self.__addr, self.__rmt_rst_msb, self.__rmt_rst_lsb)
    @rmt_rst.setter
    def rmt_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__rmt_rst_msb, self.__rmt_rst_lsb, value)

    @property
    def uhci0_rst(self):
        return self.__MEM.rdm(self.__addr, self.__uhci0_rst_msb, self.__uhci0_rst_lsb)
    @uhci0_rst.setter
    def uhci0_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__uhci0_rst_msb, self.__uhci0_rst_lsb, value)

    @property
    def i2c_ext0_rst(self):
        return self.__MEM.rdm(self.__addr, self.__i2c_ext0_rst_msb, self.__i2c_ext0_rst_lsb)
    @i2c_ext0_rst.setter
    def i2c_ext0_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2c_ext0_rst_msb, self.__i2c_ext0_rst_lsb, value)

    @property
    def spi2_rst(self):
        return self.__MEM.rdm(self.__addr, self.__spi2_rst_msb, self.__spi2_rst_lsb)
    @spi2_rst.setter
    def spi2_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi2_rst_msb, self.__spi2_rst_lsb, value)

    @property
    def uart1_rst(self):
        return self.__MEM.rdm(self.__addr, self.__uart1_rst_msb, self.__uart1_rst_lsb)
    @uart1_rst.setter
    def uart1_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart1_rst_msb, self.__uart1_rst_lsb, value)

    @property
    def i2s0_rst(self):
        return self.__MEM.rdm(self.__addr, self.__i2s0_rst_msb, self.__i2s0_rst_lsb)
    @i2s0_rst.setter
    def i2s0_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s0_rst_msb, self.__i2s0_rst_lsb, value)

    @property
    def wdg_rst(self):
        return self.__MEM.rdm(self.__addr, self.__wdg_rst_msb, self.__wdg_rst_lsb)
    @wdg_rst.setter
    def wdg_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__wdg_rst_msb, self.__wdg_rst_lsb, value)

    @property
    def uart_rst(self):
        return self.__MEM.rdm(self.__addr, self.__uart_rst_msb, self.__uart_rst_lsb)
    @uart_rst.setter
    def uart_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_rst_msb, self.__uart_rst_lsb, value)

    @property
    def spi01_rst(self):
        return self.__MEM.rdm(self.__addr, self.__spi01_rst_msb, self.__spi01_rst_lsb)
    @spi01_rst.setter
    def spi01_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi01_rst_msb, self.__spi01_rst_lsb, value)

    @property
    def timers_rst(self):
        return self.__MEM.rdm(self.__addr, self.__timers_rst_msb, self.__timers_rst_lsb)
    @timers_rst.setter
    def timers_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__timers_rst_msb, self.__timers_rst_lsb, value)
class PERIP_RST_EN1(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x4c
        self.__crypto_dma_rst_lsb = 6
        self.__crypto_dma_rst_msb = 6
        self.__crypto_hmac_rst_lsb = 5
        self.__crypto_hmac_rst_msb = 5
        self.__crypto_ds_rst_lsb = 4
        self.__crypto_ds_rst_msb = 4
        self.__crypto_rsa_rst_lsb = 3
        self.__crypto_rsa_rst_msb = 3
        self.__crypto_sha_rst_lsb = 2
        self.__crypto_sha_rst_msb = 2
        self.__crypto_aes_rst_lsb = 1
        self.__crypto_aes_rst_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def crypto_dma_rst(self):
        return self.__MEM.rdm(self.__addr, self.__crypto_dma_rst_msb, self.__crypto_dma_rst_lsb)
    @crypto_dma_rst.setter
    def crypto_dma_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__crypto_dma_rst_msb, self.__crypto_dma_rst_lsb, value)

    @property
    def crypto_hmac_rst(self):
        return self.__MEM.rdm(self.__addr, self.__crypto_hmac_rst_msb, self.__crypto_hmac_rst_lsb)
    @crypto_hmac_rst.setter
    def crypto_hmac_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__crypto_hmac_rst_msb, self.__crypto_hmac_rst_lsb, value)

    @property
    def crypto_ds_rst(self):
        return self.__MEM.rdm(self.__addr, self.__crypto_ds_rst_msb, self.__crypto_ds_rst_lsb)
    @crypto_ds_rst.setter
    def crypto_ds_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__crypto_ds_rst_msb, self.__crypto_ds_rst_lsb, value)

    @property
    def crypto_rsa_rst(self):
        return self.__MEM.rdm(self.__addr, self.__crypto_rsa_rst_msb, self.__crypto_rsa_rst_lsb)
    @crypto_rsa_rst.setter
    def crypto_rsa_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__crypto_rsa_rst_msb, self.__crypto_rsa_rst_lsb, value)

    @property
    def crypto_sha_rst(self):
        return self.__MEM.rdm(self.__addr, self.__crypto_sha_rst_msb, self.__crypto_sha_rst_lsb)
    @crypto_sha_rst.setter
    def crypto_sha_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__crypto_sha_rst_msb, self.__crypto_sha_rst_lsb, value)

    @property
    def crypto_aes_rst(self):
        return self.__MEM.rdm(self.__addr, self.__crypto_aes_rst_msb, self.__crypto_aes_rst_lsb)
    @crypto_aes_rst.setter
    def crypto_aes_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__crypto_aes_rst_msb, self.__crypto_aes_rst_lsb, value)
class BT_LPCK_DIV_INT(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x50
        self.__reg_bt_lpck_div_num_lsb = 0
        self.__reg_bt_lpck_div_num_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bt_lpck_div_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bt_lpck_div_num_msb, self.__reg_bt_lpck_div_num_lsb)
    @reg_bt_lpck_div_num.setter
    def reg_bt_lpck_div_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bt_lpck_div_num_msb, self.__reg_bt_lpck_div_num_lsb, value)
class BT_LPCK_DIV_FRAC(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x54
        self.__reg_lpclk_rtc_en_lsb = 28
        self.__reg_lpclk_rtc_en_msb = 28
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
    def reg_lpclk_rtc_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lpclk_rtc_en_msb, self.__reg_lpclk_rtc_en_lsb)
    @reg_lpclk_rtc_en.setter
    def reg_lpclk_rtc_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lpclk_rtc_en_msb, self.__reg_lpclk_rtc_en_lsb, value)

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
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x58
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
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x5c
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
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x60
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
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x64
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
class RSA_PD_CTRL_REG(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x68
        self.__rsa_mem_force_pd_lsb = 2
        self.__rsa_mem_force_pd_msb = 2
        self.__rsa_mem_force_pu_lsb = 1
        self.__rsa_mem_force_pu_msb = 1
        self.__rsa_mem_pd_lsb = 0
        self.__rsa_mem_pd_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rsa_mem_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__rsa_mem_force_pd_msb, self.__rsa_mem_force_pd_lsb)
    @rsa_mem_force_pd.setter
    def rsa_mem_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__rsa_mem_force_pd_msb, self.__rsa_mem_force_pd_lsb, value)

    @property
    def rsa_mem_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__rsa_mem_force_pu_msb, self.__rsa_mem_force_pu_lsb)
    @rsa_mem_force_pu.setter
    def rsa_mem_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__rsa_mem_force_pu_msb, self.__rsa_mem_force_pu_lsb, value)

    @property
    def rsa_mem_pd(self):
        return self.__MEM.rdm(self.__addr, self.__rsa_mem_pd_msb, self.__rsa_mem_pd_lsb)
    @rsa_mem_pd.setter
    def rsa_mem_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__rsa_mem_pd_msb, self.__rsa_mem_pd_lsb, value)
class BUSTOEXTMEM_ENA(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x6c
        self.__bustoextmem_ena_lsb = 0
        self.__bustoextmem_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def bustoextmem_ena(self):
        return self.__MEM.rdm(self.__addr, self.__bustoextmem_ena_msb, self.__bustoextmem_ena_lsb)
    @bustoextmem_ena.setter
    def bustoextmem_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__bustoextmem_ena_msb, self.__bustoextmem_ena_lsb, value)
class Cache_Control(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x70
        self.__pro_cache_reset_lsb = 2
        self.__pro_cache_reset_msb = 2
        self.__pro_dcache_clk_on_lsb = 1
        self.__pro_dcache_clk_on_msb = 1
        self.__pro_icache_clk_on_lsb = 0
        self.__pro_icache_clk_on_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pro_cache_reset(self):
        return self.__MEM.rdm(self.__addr, self.__pro_cache_reset_msb, self.__pro_cache_reset_lsb)
    @pro_cache_reset.setter
    def pro_cache_reset(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_cache_reset_msb, self.__pro_cache_reset_lsb, value)

    @property
    def pro_dcache_clk_on(self):
        return self.__MEM.rdm(self.__addr, self.__pro_dcache_clk_on_msb, self.__pro_dcache_clk_on_lsb)
    @pro_dcache_clk_on.setter
    def pro_dcache_clk_on(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_dcache_clk_on_msb, self.__pro_dcache_clk_on_lsb, value)

    @property
    def pro_icache_clk_on(self):
        return self.__MEM.rdm(self.__addr, self.__pro_icache_clk_on_msb, self.__pro_icache_clk_on_lsb)
    @pro_icache_clk_on.setter
    def pro_icache_clk_on(self, value):
        return self.__MEM.wrm(self.__addr, self.__pro_icache_clk_on_msb, self.__pro_icache_clk_on_lsb, value)
class External_Device_Encrypt_Decrypt_Control(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x74
        self.__enable_download_manual_encrypt_lsb = 3
        self.__enable_download_manual_encrypt_msb = 3
        self.__enable_download_G0CB_decrypt_lsb = 2
        self.__enable_download_G0CB_decrypt_msb = 2
        self.__enable_download_DB_encrypt_lsb = 1
        self.__enable_download_DB_encrypt_msb = 1
        self.__enable_spi_manual_encrypt_lsb = 0
        self.__enable_spi_manual_encrypt_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def enable_download_manual_encrypt(self):
        return self.__MEM.rdm(self.__addr, self.__enable_download_manual_encrypt_msb, self.__enable_download_manual_encrypt_lsb)
    @enable_download_manual_encrypt.setter
    def enable_download_manual_encrypt(self, value):
        return self.__MEM.wrm(self.__addr, self.__enable_download_manual_encrypt_msb, self.__enable_download_manual_encrypt_lsb, value)

    @property
    def enable_download_G0CB_decrypt(self):
        return self.__MEM.rdm(self.__addr, self.__enable_download_G0CB_decrypt_msb, self.__enable_download_G0CB_decrypt_lsb)
    @enable_download_G0CB_decrypt.setter
    def enable_download_G0CB_decrypt(self, value):
        return self.__MEM.wrm(self.__addr, self.__enable_download_G0CB_decrypt_msb, self.__enable_download_G0CB_decrypt_lsb, value)

    @property
    def enable_download_DB_encrypt(self):
        return self.__MEM.rdm(self.__addr, self.__enable_download_DB_encrypt_msb, self.__enable_download_DB_encrypt_lsb)
    @enable_download_DB_encrypt.setter
    def enable_download_DB_encrypt(self, value):
        return self.__MEM.wrm(self.__addr, self.__enable_download_DB_encrypt_msb, self.__enable_download_DB_encrypt_lsb, value)

    @property
    def enable_spi_manual_encrypt(self):
        return self.__MEM.rdm(self.__addr, self.__enable_spi_manual_encrypt_msb, self.__enable_spi_manual_encrypt_lsb)
    @enable_spi_manual_encrypt.setter
    def enable_spi_manual_encrypt(self, value):
        return self.__MEM.wrm(self.__addr, self.__enable_spi_manual_encrypt_msb, self.__enable_spi_manual_encrypt_lsb, value)
class RTC_FASTMEM_CONFIG(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x78
        self.__rtc_mem_crc_finish_lsb = 31
        self.__rtc_mem_crc_finish_msb = 31
        self.__reg_rtc_mem_crc_len_lsb = 20
        self.__reg_rtc_mem_crc_len_msb = 30
        self.__reg_rtc_mem_crc_addr_lsb = 9
        self.__reg_rtc_mem_crc_addr_msb = 19
        self.__reg_rtc_mem_crc_start_lsb = 8
        self.__reg_rtc_mem_crc_start_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_mem_crc_finish(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_mem_crc_finish_msb, self.__rtc_mem_crc_finish_lsb)
    @rtc_mem_crc_finish.setter
    def rtc_mem_crc_finish(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_mem_crc_finish_msb, self.__rtc_mem_crc_finish_lsb, value)

    @property
    def reg_rtc_mem_crc_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_mem_crc_len_msb, self.__reg_rtc_mem_crc_len_lsb)
    @reg_rtc_mem_crc_len.setter
    def reg_rtc_mem_crc_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_mem_crc_len_msb, self.__reg_rtc_mem_crc_len_lsb, value)

    @property
    def reg_rtc_mem_crc_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_mem_crc_addr_msb, self.__reg_rtc_mem_crc_addr_lsb)
    @reg_rtc_mem_crc_addr.setter
    def reg_rtc_mem_crc_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_mem_crc_addr_msb, self.__reg_rtc_mem_crc_addr_lsb, value)

    @property
    def reg_rtc_mem_crc_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_mem_crc_start_msb, self.__reg_rtc_mem_crc_start_lsb)
    @reg_rtc_mem_crc_start.setter
    def reg_rtc_mem_crc_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_mem_crc_start_msb, self.__reg_rtc_mem_crc_start_lsb, value)
class RTC_FASTMEM_CRC(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x7c
        self.__rtc_mem_crc_res_lsb = 0
        self.__rtc_mem_crc_res_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_mem_crc_res(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_mem_crc_res_msb, self.__rtc_mem_crc_res_lsb)
    @rtc_mem_crc_res.setter
    def rtc_mem_crc_res(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_mem_crc_res_msb, self.__rtc_mem_crc_res_lsb, value)
class Redundant_ECO_Ctrl(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x80
        self.__Redundant_ECO_result_lsb = 1
        self.__Redundant_ECO_result_msb = 1
        self.__Redundant_ECO_drive_lsb = 0
        self.__Redundant_ECO_drive_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def Redundant_ECO_result(self):
        return self.__MEM.rdm(self.__addr, self.__Redundant_ECO_result_msb, self.__Redundant_ECO_result_lsb)
    @Redundant_ECO_result.setter
    def Redundant_ECO_result(self, value):
        return self.__MEM.wrm(self.__addr, self.__Redundant_ECO_result_msb, self.__Redundant_ECO_result_lsb, value)

    @property
    def Redundant_ECO_drive(self):
        return self.__MEM.rdm(self.__addr, self.__Redundant_ECO_drive_msb, self.__Redundant_ECO_drive_lsb)
    @Redundant_ECO_drive.setter
    def Redundant_ECO_drive(self, value):
        return self.__MEM.wrm(self.__addr, self.__Redundant_ECO_drive_msb, self.__Redundant_ECO_drive_lsb, value)
class CLOCK_GATE_REG(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x84
        self.__reg_clk_en_lsb = 0
        self.__reg_clk_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk_en_msb, self.__reg_clk_en_lsb)
    @reg_clk_en.setter
    def reg_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk_en_msb, self.__reg_clk_en_lsb, value)
class SRAM_CTRL_2(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x88
        self.__sram_force_pu_lsb = 0
        self.__sram_force_pu_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__sram_force_pu_msb, self.__sram_force_pu_lsb)
    @sram_force_pu.setter
    def sram_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_force_pu_msb, self.__sram_force_pu_lsb, value)
class SYSCLK_CONF(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0x8c
        self.__clk_div_en_lsb = 19
        self.__clk_div_en_msb = 19
        self.__clk_xtal_freq_lsb = 12
        self.__clk_xtal_freq_msb = 18
        self.__reg_soc_clk_sel_lsb = 10
        self.__reg_soc_clk_sel_msb = 11
        self.__reg_pre_div_cnt_lsb = 0
        self.__reg_pre_div_cnt_msb = 9
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def clk_div_en(self):
        return self.__MEM.rdm(self.__addr, self.__clk_div_en_msb, self.__clk_div_en_lsb)
    @clk_div_en.setter
    def clk_div_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__clk_div_en_msb, self.__clk_div_en_lsb, value)

    @property
    def clk_xtal_freq(self):
        return self.__MEM.rdm(self.__addr, self.__clk_xtal_freq_msb, self.__clk_xtal_freq_lsb)
    @clk_xtal_freq.setter
    def clk_xtal_freq(self, value):
        return self.__MEM.wrm(self.__addr, self.__clk_xtal_freq_msb, self.__clk_xtal_freq_lsb, value)

    @property
    def reg_soc_clk_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_soc_clk_sel_msb, self.__reg_soc_clk_sel_lsb)
    @reg_soc_clk_sel.setter
    def reg_soc_clk_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_soc_clk_sel_msb, self.__reg_soc_clk_sel_lsb, value)

    @property
    def reg_pre_div_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pre_div_cnt_msb, self.__reg_pre_div_cnt_lsb)
    @reg_pre_div_cnt.setter
    def reg_pre_div_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pre_div_cnt_msb, self.__reg_pre_div_cnt_lsb, value)
class SYSTEM_REG_DATE(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SYSTEM_BASE + 0xffc
        self.__system_reg_date_lsb = 0
        self.__system_reg_date_msb = 27
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def system_reg_date(self):
        return self.__MEM.rdm(self.__addr, self.__system_reg_date_msb, self.__system_reg_date_lsb)
    @system_reg_date.setter
    def system_reg_date(self, value):
        return self.__MEM.wrm(self.__addr, self.__system_reg_date_msb, self.__system_reg_date_lsb, value)
    @property
    def default_value(self):
        return 0x1908020
