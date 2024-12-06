from hal.common import *
from hal.hwregister.hwreg.CHIP72.addr_base import *
class GPIO_SD(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.SIGMADELTA0 = SIGMADELTA0(self.channel, self.chipv)
        self.SIGMADELTA1 = SIGMADELTA1(self.channel, self.chipv)
        self.SIGMADELTA2 = SIGMADELTA2(self.channel, self.chipv)
        self.SIGMADELTA3 = SIGMADELTA3(self.channel, self.chipv)
        self.SIGMADELTA4 = SIGMADELTA4(self.channel, self.chipv)
        self.SIGMADELTA5 = SIGMADELTA5(self.channel, self.chipv)
        self.SIGMADELTA6 = SIGMADELTA6(self.channel, self.chipv)
        self.SIGMADELTA7 = SIGMADELTA7(self.channel, self.chipv)
        self.SIGMADELTA_CG = SIGMADELTA_CG(self.channel, self.chipv)
        self.SIGMADELTA_MISC = SIGMADELTA_MISC(self.channel, self.chipv)
        self.SIGMADELTA_VERSION = SIGMADELTA_VERSION(self.channel, self.chipv)
class SIGMADELTA0(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_SD_BASE + 0x0
        self.__reg_sd0_prescale_lsb = 8
        self.__reg_sd0_prescale_msb = 15
        self.__reg_sd0_in_lsb = 0
        self.__reg_sd0_in_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sd0_prescale(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sd0_prescale_msb, self.__reg_sd0_prescale_lsb)
    @reg_sd0_prescale.setter
    def reg_sd0_prescale(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sd0_prescale_msb, self.__reg_sd0_prescale_lsb, value)

    @property
    def reg_sd0_in(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sd0_in_msb, self.__reg_sd0_in_lsb)
    @reg_sd0_in.setter
    def reg_sd0_in(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sd0_in_msb, self.__reg_sd0_in_lsb, value)
class SIGMADELTA1(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_SD_BASE + 0x4
        self.__reg_sd1_prescale_lsb = 8
        self.__reg_sd1_prescale_msb = 15
        self.__reg_sd1_in_lsb = 0
        self.__reg_sd1_in_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sd1_prescale(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sd1_prescale_msb, self.__reg_sd1_prescale_lsb)
    @reg_sd1_prescale.setter
    def reg_sd1_prescale(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sd1_prescale_msb, self.__reg_sd1_prescale_lsb, value)

    @property
    def reg_sd1_in(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sd1_in_msb, self.__reg_sd1_in_lsb)
    @reg_sd1_in.setter
    def reg_sd1_in(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sd1_in_msb, self.__reg_sd1_in_lsb, value)
class SIGMADELTA2(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_SD_BASE + 0x8
        self.__reg_sd2_prescale_lsb = 8
        self.__reg_sd2_prescale_msb = 15
        self.__reg_sd2_in_lsb = 0
        self.__reg_sd2_in_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sd2_prescale(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sd2_prescale_msb, self.__reg_sd2_prescale_lsb)
    @reg_sd2_prescale.setter
    def reg_sd2_prescale(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sd2_prescale_msb, self.__reg_sd2_prescale_lsb, value)

    @property
    def reg_sd2_in(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sd2_in_msb, self.__reg_sd2_in_lsb)
    @reg_sd2_in.setter
    def reg_sd2_in(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sd2_in_msb, self.__reg_sd2_in_lsb, value)
class SIGMADELTA3(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_SD_BASE + 0xc
        self.__reg_sd3_prescale_lsb = 8
        self.__reg_sd3_prescale_msb = 15
        self.__reg_sd3_in_lsb = 0
        self.__reg_sd3_in_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sd3_prescale(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sd3_prescale_msb, self.__reg_sd3_prescale_lsb)
    @reg_sd3_prescale.setter
    def reg_sd3_prescale(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sd3_prescale_msb, self.__reg_sd3_prescale_lsb, value)

    @property
    def reg_sd3_in(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sd3_in_msb, self.__reg_sd3_in_lsb)
    @reg_sd3_in.setter
    def reg_sd3_in(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sd3_in_msb, self.__reg_sd3_in_lsb, value)
class SIGMADELTA4(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_SD_BASE + 0x10
        self.__reg_sd4_prescale_lsb = 8
        self.__reg_sd4_prescale_msb = 15
        self.__reg_sd4_in_lsb = 0
        self.__reg_sd4_in_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sd4_prescale(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sd4_prescale_msb, self.__reg_sd4_prescale_lsb)
    @reg_sd4_prescale.setter
    def reg_sd4_prescale(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sd4_prescale_msb, self.__reg_sd4_prescale_lsb, value)

    @property
    def reg_sd4_in(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sd4_in_msb, self.__reg_sd4_in_lsb)
    @reg_sd4_in.setter
    def reg_sd4_in(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sd4_in_msb, self.__reg_sd4_in_lsb, value)
class SIGMADELTA5(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_SD_BASE + 0x14
        self.__reg_sd5_prescale_lsb = 8
        self.__reg_sd5_prescale_msb = 15
        self.__reg_sd5_in_lsb = 0
        self.__reg_sd5_in_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sd5_prescale(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sd5_prescale_msb, self.__reg_sd5_prescale_lsb)
    @reg_sd5_prescale.setter
    def reg_sd5_prescale(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sd5_prescale_msb, self.__reg_sd5_prescale_lsb, value)

    @property
    def reg_sd5_in(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sd5_in_msb, self.__reg_sd5_in_lsb)
    @reg_sd5_in.setter
    def reg_sd5_in(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sd5_in_msb, self.__reg_sd5_in_lsb, value)
class SIGMADELTA6(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_SD_BASE + 0x18
        self.__reg_sd6_prescale_lsb = 8
        self.__reg_sd6_prescale_msb = 15
        self.__reg_sd6_in_lsb = 0
        self.__reg_sd6_in_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sd6_prescale(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sd6_prescale_msb, self.__reg_sd6_prescale_lsb)
    @reg_sd6_prescale.setter
    def reg_sd6_prescale(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sd6_prescale_msb, self.__reg_sd6_prescale_lsb, value)

    @property
    def reg_sd6_in(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sd6_in_msb, self.__reg_sd6_in_lsb)
    @reg_sd6_in.setter
    def reg_sd6_in(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sd6_in_msb, self.__reg_sd6_in_lsb, value)
class SIGMADELTA7(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_SD_BASE + 0x1c
        self.__reg_sd7_prescale_lsb = 8
        self.__reg_sd7_prescale_msb = 15
        self.__reg_sd7_in_lsb = 0
        self.__reg_sd7_in_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sd7_prescale(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sd7_prescale_msb, self.__reg_sd7_prescale_lsb)
    @reg_sd7_prescale.setter
    def reg_sd7_prescale(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sd7_prescale_msb, self.__reg_sd7_prescale_lsb, value)

    @property
    def reg_sd7_in(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sd7_in_msb, self.__reg_sd7_in_lsb)
    @reg_sd7_in.setter
    def reg_sd7_in(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sd7_in_msb, self.__reg_sd7_in_lsb, value)
class SIGMADELTA_CG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_SD_BASE + 0x20
        self.__reg_gpio_sd_clk_en_lsb = 31
        self.__reg_gpio_sd_clk_en_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_gpio_sd_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gpio_sd_clk_en_msb, self.__reg_gpio_sd_clk_en_lsb)
    @reg_gpio_sd_clk_en.setter
    def reg_gpio_sd_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gpio_sd_clk_en_msb, self.__reg_gpio_sd_clk_en_lsb, value)
class SIGMADELTA_MISC(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_SD_BASE + 0x24
        self.__reg_spi_swap_lsb = 31
        self.__reg_spi_swap_msb = 31
        self.__reg_sd_clk_en_lsb = 30
        self.__reg_sd_clk_en_msb = 30
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_spi_swap(self):
        return self.__MEM.rdm(self.__addr, self.__reg_spi_swap_msb, self.__reg_spi_swap_lsb)
    @reg_spi_swap.setter
    def reg_spi_swap(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_spi_swap_msb, self.__reg_spi_swap_lsb, value)

    @property
    def reg_sd_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sd_clk_en_msb, self.__reg_sd_clk_en_lsb)
    @reg_sd_clk_en.setter
    def reg_sd_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sd_clk_en_msb, self.__reg_sd_clk_en_lsb, value)
class SIGMADELTA_VERSION(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_SD_BASE + 0x28
        self.__reg_gpio_sd_date_lsb = 0
        self.__reg_gpio_sd_date_msb = 27
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_gpio_sd_date(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gpio_sd_date_msb, self.__reg_gpio_sd_date_lsb)
    @reg_gpio_sd_date.setter
    def reg_gpio_sd_date(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gpio_sd_date_msb, self.__reg_gpio_sd_date_lsb, value)
    @property
    def default_value(self):
        return 0x1704130
