from hal.common import *
from hal.hwregister.hwreg.CHIP722.addr_base import *
class RTC_IO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.RTC_GPIO_OUT = RTC_GPIO_OUT(self.channel, self.chipv)
        self.RTC_GPIO_OUT_W1TS = RTC_GPIO_OUT_W1TS(self.channel, self.chipv)
        self.RTC_GPIO_OUT_W1TC = RTC_GPIO_OUT_W1TC(self.channel, self.chipv)
        self.RTC_GPIO_ENABLE = RTC_GPIO_ENABLE(self.channel, self.chipv)
        self.RTC_GPIO_ENABLE_W1TS = RTC_GPIO_ENABLE_W1TS(self.channel, self.chipv)
        self.RTC_GPIO_ENABLE_W1TC = RTC_GPIO_ENABLE_W1TC(self.channel, self.chipv)
        self.RTC_GPIO_STATUS = RTC_GPIO_STATUS(self.channel, self.chipv)
        self.RTC_GPIO_STATUS_W1TS = RTC_GPIO_STATUS_W1TS(self.channel, self.chipv)
        self.RTC_GPIO_STATUS_W1TC = RTC_GPIO_STATUS_W1TC(self.channel, self.chipv)
        self.RTC_GPIO_IN = RTC_GPIO_IN(self.channel, self.chipv)
        self.RTC_GPIO_PIN0 = RTC_GPIO_PIN0(self.channel, self.chipv)
        self.RTC_GPIO_PIN1 = RTC_GPIO_PIN1(self.channel, self.chipv)
        self.RTC_GPIO_PIN2 = RTC_GPIO_PIN2(self.channel, self.chipv)
        self.RTC_GPIO_PIN3 = RTC_GPIO_PIN3(self.channel, self.chipv)
        self.RTC_GPIO_PIN4 = RTC_GPIO_PIN4(self.channel, self.chipv)
        self.RTC_GPIO_PIN5 = RTC_GPIO_PIN5(self.channel, self.chipv)
        self.RTC_GPIO_PIN6 = RTC_GPIO_PIN6(self.channel, self.chipv)
        self.RTC_GPIO_PIN7 = RTC_GPIO_PIN7(self.channel, self.chipv)
        self.RTC_GPIO_PIN8 = RTC_GPIO_PIN8(self.channel, self.chipv)
        self.RTC_GPIO_PIN9 = RTC_GPIO_PIN9(self.channel, self.chipv)
        self.RTC_GPIO_PIN10 = RTC_GPIO_PIN10(self.channel, self.chipv)
        self.RTC_GPIO_PIN11 = RTC_GPIO_PIN11(self.channel, self.chipv)
        self.RTC_GPIO_PIN12 = RTC_GPIO_PIN12(self.channel, self.chipv)
        self.RTC_GPIO_PIN13 = RTC_GPIO_PIN13(self.channel, self.chipv)
        self.RTC_GPIO_PIN14 = RTC_GPIO_PIN14(self.channel, self.chipv)
        self.RTC_GPIO_PIN15 = RTC_GPIO_PIN15(self.channel, self.chipv)
        self.RTC_GPIO_PIN16 = RTC_GPIO_PIN16(self.channel, self.chipv)
        self.RTC_GPIO_PIN17 = RTC_GPIO_PIN17(self.channel, self.chipv)
        self.RTC_GPIO_PIN18 = RTC_GPIO_PIN18(self.channel, self.chipv)
        self.RTC_GPIO_PIN19 = RTC_GPIO_PIN19(self.channel, self.chipv)
        self.RTC_GPIO_PIN20 = RTC_GPIO_PIN20(self.channel, self.chipv)
        self.RTC_GPIO_PIN21 = RTC_GPIO_PIN21(self.channel, self.chipv)
        self.RTC_DEBUG_SEL = RTC_DEBUG_SEL(self.channel, self.chipv)
        self.TOUCH_PAD0 = TOUCH_PAD0(self.channel, self.chipv)
        self.TOUCH_PAD1 = TOUCH_PAD1(self.channel, self.chipv)
        self.TOUCH_PAD2 = TOUCH_PAD2(self.channel, self.chipv)
        self.TOUCH_PAD3 = TOUCH_PAD3(self.channel, self.chipv)
        self.TOUCH_PAD4 = TOUCH_PAD4(self.channel, self.chipv)
        self.TOUCH_PAD5 = TOUCH_PAD5(self.channel, self.chipv)
        self.TOUCH_PAD6 = TOUCH_PAD6(self.channel, self.chipv)
        self.TOUCH_PAD7 = TOUCH_PAD7(self.channel, self.chipv)
        self.TOUCH_PAD8 = TOUCH_PAD8(self.channel, self.chipv)
        self.TOUCH_PAD9 = TOUCH_PAD9(self.channel, self.chipv)
        self.TOUCH_PAD10 = TOUCH_PAD10(self.channel, self.chipv)
        self.TOUCH_PAD11 = TOUCH_PAD11(self.channel, self.chipv)
        self.TOUCH_PAD12 = TOUCH_PAD12(self.channel, self.chipv)
        self.TOUCH_PAD13 = TOUCH_PAD13(self.channel, self.chipv)
        self.TOUCH_PAD14 = TOUCH_PAD14(self.channel, self.chipv)
        self.XTAL_32P_PAD = XTAL_32P_PAD(self.channel, self.chipv)
        self.XTAL_32N_PAD = XTAL_32N_PAD(self.channel, self.chipv)
        self.PAD_DAC1 = PAD_DAC1(self.channel, self.chipv)
        self.PAD_DAC2 = PAD_DAC2(self.channel, self.chipv)
        self.RTC_PAD19 = RTC_PAD19(self.channel, self.chipv)
        self.RTC_PAD20 = RTC_PAD20(self.channel, self.chipv)
        self.RTC_PAD21 = RTC_PAD21(self.channel, self.chipv)
        self.EXT_WAKEUP0 = EXT_WAKEUP0(self.channel, self.chipv)
        self.XTL_EXT_CTR = XTL_EXT_CTR(self.channel, self.chipv)
        self.SAR_I2C_IO = SAR_I2C_IO(self.channel, self.chipv)
        self.RTC_IO_DATE = RTC_IO_DATE(self.channel, self.chipv)
class RTC_GPIO_OUT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x0
        self.__rtc_gpio_out_data_lsb = 10
        self.__rtc_gpio_out_data_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_gpio_out_data(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_gpio_out_data_msb, self.__rtc_gpio_out_data_lsb)
    @rtc_gpio_out_data.setter
    def rtc_gpio_out_data(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_gpio_out_data_msb, self.__rtc_gpio_out_data_lsb, value)
class RTC_GPIO_OUT_W1TS(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x4
        self.__rtc_gpio_out_data_w1ts_lsb = 10
        self.__rtc_gpio_out_data_w1ts_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_gpio_out_data_w1ts(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_gpio_out_data_w1ts_msb, self.__rtc_gpio_out_data_w1ts_lsb)
    @rtc_gpio_out_data_w1ts.setter
    def rtc_gpio_out_data_w1ts(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_gpio_out_data_w1ts_msb, self.__rtc_gpio_out_data_w1ts_lsb, value)
class RTC_GPIO_OUT_W1TC(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x8
        self.__rtc_gpio_out_data_w1tc_lsb = 10
        self.__rtc_gpio_out_data_w1tc_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_gpio_out_data_w1tc(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_gpio_out_data_w1tc_msb, self.__rtc_gpio_out_data_w1tc_lsb)
    @rtc_gpio_out_data_w1tc.setter
    def rtc_gpio_out_data_w1tc(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_gpio_out_data_w1tc_msb, self.__rtc_gpio_out_data_w1tc_lsb, value)
class RTC_GPIO_ENABLE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0xc
        self.__reg_rtc_gpio_enable_lsb = 10
        self.__reg_rtc_gpio_enable_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rtc_gpio_enable(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_gpio_enable_msb, self.__reg_rtc_gpio_enable_lsb)
    @reg_rtc_gpio_enable.setter
    def reg_rtc_gpio_enable(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_gpio_enable_msb, self.__reg_rtc_gpio_enable_lsb, value)
class RTC_GPIO_ENABLE_W1TS(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x10
        self.__reg_rtc_gpio_enable_w1ts_lsb = 10
        self.__reg_rtc_gpio_enable_w1ts_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rtc_gpio_enable_w1ts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_gpio_enable_w1ts_msb, self.__reg_rtc_gpio_enable_w1ts_lsb)
    @reg_rtc_gpio_enable_w1ts.setter
    def reg_rtc_gpio_enable_w1ts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_gpio_enable_w1ts_msb, self.__reg_rtc_gpio_enable_w1ts_lsb, value)
class RTC_GPIO_ENABLE_W1TC(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x14
        self.__reg_rtc_gpio_enable_w1tc_lsb = 10
        self.__reg_rtc_gpio_enable_w1tc_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rtc_gpio_enable_w1tc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_gpio_enable_w1tc_msb, self.__reg_rtc_gpio_enable_w1tc_lsb)
    @reg_rtc_gpio_enable_w1tc.setter
    def reg_rtc_gpio_enable_w1tc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_gpio_enable_w1tc_msb, self.__reg_rtc_gpio_enable_w1tc_lsb, value)
class RTC_GPIO_STATUS(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x18
        self.__rtc_gpio_status_int_lsb = 10
        self.__rtc_gpio_status_int_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_gpio_status_int(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_gpio_status_int_msb, self.__rtc_gpio_status_int_lsb)
    @rtc_gpio_status_int.setter
    def rtc_gpio_status_int(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_gpio_status_int_msb, self.__rtc_gpio_status_int_lsb, value)
class RTC_GPIO_STATUS_W1TS(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x1c
        self.__rtc_gpio_status_int_w1ts_lsb = 10
        self.__rtc_gpio_status_int_w1ts_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_gpio_status_int_w1ts(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_gpio_status_int_w1ts_msb, self.__rtc_gpio_status_int_w1ts_lsb)
    @rtc_gpio_status_int_w1ts.setter
    def rtc_gpio_status_int_w1ts(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_gpio_status_int_w1ts_msb, self.__rtc_gpio_status_int_w1ts_lsb, value)
class RTC_GPIO_STATUS_W1TC(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x20
        self.__rtc_gpio_status_int_w1tc_lsb = 10
        self.__rtc_gpio_status_int_w1tc_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_gpio_status_int_w1tc(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_gpio_status_int_w1tc_msb, self.__rtc_gpio_status_int_w1tc_lsb)
    @rtc_gpio_status_int_w1tc.setter
    def rtc_gpio_status_int_w1tc(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_gpio_status_int_w1tc_msb, self.__rtc_gpio_status_int_w1tc_lsb, value)
class RTC_GPIO_IN(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x24
        self.__rtc_gpio_in_next_lsb = 10
        self.__rtc_gpio_in_next_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_gpio_in_next(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_gpio_in_next_msb, self.__rtc_gpio_in_next_lsb)
    @rtc_gpio_in_next.setter
    def rtc_gpio_in_next(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_gpio_in_next_msb, self.__rtc_gpio_in_next_lsb, value)
class RTC_GPIO_PIN0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x28
        self.__RTC_GPIO_PIN0_WAKEUP_ENABLE_lsb = 10
        self.__RTC_GPIO_PIN0_WAKEUP_ENABLE_msb = 10
        self.__RTC_GPIO_PIN0_INT_TYPE_lsb = 7
        self.__RTC_GPIO_PIN0_INT_TYPE_msb = 9
        self.__RTC_GPIO_PIN0_PAD_DRIVER_lsb = 2
        self.__RTC_GPIO_PIN0_PAD_DRIVER_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def RTC_GPIO_PIN0_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN0_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN0_WAKEUP_ENABLE_lsb)
    @RTC_GPIO_PIN0_WAKEUP_ENABLE.setter
    def RTC_GPIO_PIN0_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN0_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN0_WAKEUP_ENABLE_lsb, value)

    @property
    def RTC_GPIO_PIN0_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN0_INT_TYPE_msb, self.__RTC_GPIO_PIN0_INT_TYPE_lsb)
    @RTC_GPIO_PIN0_INT_TYPE.setter
    def RTC_GPIO_PIN0_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN0_INT_TYPE_msb, self.__RTC_GPIO_PIN0_INT_TYPE_lsb, value)

    @property
    def RTC_GPIO_PIN0_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN0_PAD_DRIVER_msb, self.__RTC_GPIO_PIN0_PAD_DRIVER_lsb)
    @RTC_GPIO_PIN0_PAD_DRIVER.setter
    def RTC_GPIO_PIN0_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN0_PAD_DRIVER_msb, self.__RTC_GPIO_PIN0_PAD_DRIVER_lsb, value)
class RTC_GPIO_PIN1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x2c
        self.__RTC_GPIO_PIN1_WAKEUP_ENABLE_lsb = 10
        self.__RTC_GPIO_PIN1_WAKEUP_ENABLE_msb = 10
        self.__RTC_GPIO_PIN1_INT_TYPE_lsb = 7
        self.__RTC_GPIO_PIN1_INT_TYPE_msb = 9
        self.__RTC_GPIO_PIN1_PAD_DRIVER_lsb = 2
        self.__RTC_GPIO_PIN1_PAD_DRIVER_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def RTC_GPIO_PIN1_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN1_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN1_WAKEUP_ENABLE_lsb)
    @RTC_GPIO_PIN1_WAKEUP_ENABLE.setter
    def RTC_GPIO_PIN1_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN1_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN1_WAKEUP_ENABLE_lsb, value)

    @property
    def RTC_GPIO_PIN1_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN1_INT_TYPE_msb, self.__RTC_GPIO_PIN1_INT_TYPE_lsb)
    @RTC_GPIO_PIN1_INT_TYPE.setter
    def RTC_GPIO_PIN1_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN1_INT_TYPE_msb, self.__RTC_GPIO_PIN1_INT_TYPE_lsb, value)

    @property
    def RTC_GPIO_PIN1_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN1_PAD_DRIVER_msb, self.__RTC_GPIO_PIN1_PAD_DRIVER_lsb)
    @RTC_GPIO_PIN1_PAD_DRIVER.setter
    def RTC_GPIO_PIN1_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN1_PAD_DRIVER_msb, self.__RTC_GPIO_PIN1_PAD_DRIVER_lsb, value)
class RTC_GPIO_PIN2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x30
        self.__RTC_GPIO_PIN2_WAKEUP_ENABLE_lsb = 10
        self.__RTC_GPIO_PIN2_WAKEUP_ENABLE_msb = 10
        self.__RTC_GPIO_PIN2_INT_TYPE_lsb = 7
        self.__RTC_GPIO_PIN2_INT_TYPE_msb = 9
        self.__RTC_GPIO_PIN2_PAD_DRIVER_lsb = 2
        self.__RTC_GPIO_PIN2_PAD_DRIVER_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def RTC_GPIO_PIN2_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN2_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN2_WAKEUP_ENABLE_lsb)
    @RTC_GPIO_PIN2_WAKEUP_ENABLE.setter
    def RTC_GPIO_PIN2_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN2_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN2_WAKEUP_ENABLE_lsb, value)

    @property
    def RTC_GPIO_PIN2_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN2_INT_TYPE_msb, self.__RTC_GPIO_PIN2_INT_TYPE_lsb)
    @RTC_GPIO_PIN2_INT_TYPE.setter
    def RTC_GPIO_PIN2_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN2_INT_TYPE_msb, self.__RTC_GPIO_PIN2_INT_TYPE_lsb, value)

    @property
    def RTC_GPIO_PIN2_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN2_PAD_DRIVER_msb, self.__RTC_GPIO_PIN2_PAD_DRIVER_lsb)
    @RTC_GPIO_PIN2_PAD_DRIVER.setter
    def RTC_GPIO_PIN2_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN2_PAD_DRIVER_msb, self.__RTC_GPIO_PIN2_PAD_DRIVER_lsb, value)
class RTC_GPIO_PIN3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x34
        self.__RTC_GPIO_PIN3_WAKEUP_ENABLE_lsb = 10
        self.__RTC_GPIO_PIN3_WAKEUP_ENABLE_msb = 10
        self.__RTC_GPIO_PIN3_INT_TYPE_lsb = 7
        self.__RTC_GPIO_PIN3_INT_TYPE_msb = 9
        self.__RTC_GPIO_PIN3_PAD_DRIVER_lsb = 2
        self.__RTC_GPIO_PIN3_PAD_DRIVER_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def RTC_GPIO_PIN3_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN3_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN3_WAKEUP_ENABLE_lsb)
    @RTC_GPIO_PIN3_WAKEUP_ENABLE.setter
    def RTC_GPIO_PIN3_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN3_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN3_WAKEUP_ENABLE_lsb, value)

    @property
    def RTC_GPIO_PIN3_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN3_INT_TYPE_msb, self.__RTC_GPIO_PIN3_INT_TYPE_lsb)
    @RTC_GPIO_PIN3_INT_TYPE.setter
    def RTC_GPIO_PIN3_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN3_INT_TYPE_msb, self.__RTC_GPIO_PIN3_INT_TYPE_lsb, value)

    @property
    def RTC_GPIO_PIN3_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN3_PAD_DRIVER_msb, self.__RTC_GPIO_PIN3_PAD_DRIVER_lsb)
    @RTC_GPIO_PIN3_PAD_DRIVER.setter
    def RTC_GPIO_PIN3_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN3_PAD_DRIVER_msb, self.__RTC_GPIO_PIN3_PAD_DRIVER_lsb, value)
class RTC_GPIO_PIN4(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x38
        self.__RTC_GPIO_PIN4_WAKEUP_ENABLE_lsb = 10
        self.__RTC_GPIO_PIN4_WAKEUP_ENABLE_msb = 10
        self.__RTC_GPIO_PIN4_INT_TYPE_lsb = 7
        self.__RTC_GPIO_PIN4_INT_TYPE_msb = 9
        self.__RTC_GPIO_PIN4_PAD_DRIVER_lsb = 2
        self.__RTC_GPIO_PIN4_PAD_DRIVER_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def RTC_GPIO_PIN4_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN4_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN4_WAKEUP_ENABLE_lsb)
    @RTC_GPIO_PIN4_WAKEUP_ENABLE.setter
    def RTC_GPIO_PIN4_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN4_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN4_WAKEUP_ENABLE_lsb, value)

    @property
    def RTC_GPIO_PIN4_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN4_INT_TYPE_msb, self.__RTC_GPIO_PIN4_INT_TYPE_lsb)
    @RTC_GPIO_PIN4_INT_TYPE.setter
    def RTC_GPIO_PIN4_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN4_INT_TYPE_msb, self.__RTC_GPIO_PIN4_INT_TYPE_lsb, value)

    @property
    def RTC_GPIO_PIN4_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN4_PAD_DRIVER_msb, self.__RTC_GPIO_PIN4_PAD_DRIVER_lsb)
    @RTC_GPIO_PIN4_PAD_DRIVER.setter
    def RTC_GPIO_PIN4_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN4_PAD_DRIVER_msb, self.__RTC_GPIO_PIN4_PAD_DRIVER_lsb, value)
class RTC_GPIO_PIN5(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x3c
        self.__RTC_GPIO_PIN5_WAKEUP_ENABLE_lsb = 10
        self.__RTC_GPIO_PIN5_WAKEUP_ENABLE_msb = 10
        self.__RTC_GPIO_PIN5_INT_TYPE_lsb = 7
        self.__RTC_GPIO_PIN5_INT_TYPE_msb = 9
        self.__RTC_GPIO_PIN5_PAD_DRIVER_lsb = 2
        self.__RTC_GPIO_PIN5_PAD_DRIVER_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def RTC_GPIO_PIN5_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN5_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN5_WAKEUP_ENABLE_lsb)
    @RTC_GPIO_PIN5_WAKEUP_ENABLE.setter
    def RTC_GPIO_PIN5_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN5_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN5_WAKEUP_ENABLE_lsb, value)

    @property
    def RTC_GPIO_PIN5_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN5_INT_TYPE_msb, self.__RTC_GPIO_PIN5_INT_TYPE_lsb)
    @RTC_GPIO_PIN5_INT_TYPE.setter
    def RTC_GPIO_PIN5_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN5_INT_TYPE_msb, self.__RTC_GPIO_PIN5_INT_TYPE_lsb, value)

    @property
    def RTC_GPIO_PIN5_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN5_PAD_DRIVER_msb, self.__RTC_GPIO_PIN5_PAD_DRIVER_lsb)
    @RTC_GPIO_PIN5_PAD_DRIVER.setter
    def RTC_GPIO_PIN5_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN5_PAD_DRIVER_msb, self.__RTC_GPIO_PIN5_PAD_DRIVER_lsb, value)
class RTC_GPIO_PIN6(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x40
        self.__RTC_GPIO_PIN6_WAKEUP_ENABLE_lsb = 10
        self.__RTC_GPIO_PIN6_WAKEUP_ENABLE_msb = 10
        self.__RTC_GPIO_PIN6_INT_TYPE_lsb = 7
        self.__RTC_GPIO_PIN6_INT_TYPE_msb = 9
        self.__RTC_GPIO_PIN6_PAD_DRIVER_lsb = 2
        self.__RTC_GPIO_PIN6_PAD_DRIVER_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def RTC_GPIO_PIN6_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN6_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN6_WAKEUP_ENABLE_lsb)
    @RTC_GPIO_PIN6_WAKEUP_ENABLE.setter
    def RTC_GPIO_PIN6_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN6_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN6_WAKEUP_ENABLE_lsb, value)

    @property
    def RTC_GPIO_PIN6_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN6_INT_TYPE_msb, self.__RTC_GPIO_PIN6_INT_TYPE_lsb)
    @RTC_GPIO_PIN6_INT_TYPE.setter
    def RTC_GPIO_PIN6_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN6_INT_TYPE_msb, self.__RTC_GPIO_PIN6_INT_TYPE_lsb, value)

    @property
    def RTC_GPIO_PIN6_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN6_PAD_DRIVER_msb, self.__RTC_GPIO_PIN6_PAD_DRIVER_lsb)
    @RTC_GPIO_PIN6_PAD_DRIVER.setter
    def RTC_GPIO_PIN6_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN6_PAD_DRIVER_msb, self.__RTC_GPIO_PIN6_PAD_DRIVER_lsb, value)
class RTC_GPIO_PIN7(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x44
        self.__RTC_GPIO_PIN7_WAKEUP_ENABLE_lsb = 10
        self.__RTC_GPIO_PIN7_WAKEUP_ENABLE_msb = 10
        self.__RTC_GPIO_PIN7_INT_TYPE_lsb = 7
        self.__RTC_GPIO_PIN7_INT_TYPE_msb = 9
        self.__RTC_GPIO_PIN7_PAD_DRIVER_lsb = 2
        self.__RTC_GPIO_PIN7_PAD_DRIVER_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def RTC_GPIO_PIN7_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN7_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN7_WAKEUP_ENABLE_lsb)
    @RTC_GPIO_PIN7_WAKEUP_ENABLE.setter
    def RTC_GPIO_PIN7_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN7_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN7_WAKEUP_ENABLE_lsb, value)

    @property
    def RTC_GPIO_PIN7_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN7_INT_TYPE_msb, self.__RTC_GPIO_PIN7_INT_TYPE_lsb)
    @RTC_GPIO_PIN7_INT_TYPE.setter
    def RTC_GPIO_PIN7_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN7_INT_TYPE_msb, self.__RTC_GPIO_PIN7_INT_TYPE_lsb, value)

    @property
    def RTC_GPIO_PIN7_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN7_PAD_DRIVER_msb, self.__RTC_GPIO_PIN7_PAD_DRIVER_lsb)
    @RTC_GPIO_PIN7_PAD_DRIVER.setter
    def RTC_GPIO_PIN7_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN7_PAD_DRIVER_msb, self.__RTC_GPIO_PIN7_PAD_DRIVER_lsb, value)
class RTC_GPIO_PIN8(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x48
        self.__RTC_GPIO_PIN8_WAKEUP_ENABLE_lsb = 10
        self.__RTC_GPIO_PIN8_WAKEUP_ENABLE_msb = 10
        self.__RTC_GPIO_PIN8_INT_TYPE_lsb = 7
        self.__RTC_GPIO_PIN8_INT_TYPE_msb = 9
        self.__RTC_GPIO_PIN8_PAD_DRIVER_lsb = 2
        self.__RTC_GPIO_PIN8_PAD_DRIVER_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def RTC_GPIO_PIN8_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN8_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN8_WAKEUP_ENABLE_lsb)
    @RTC_GPIO_PIN8_WAKEUP_ENABLE.setter
    def RTC_GPIO_PIN8_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN8_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN8_WAKEUP_ENABLE_lsb, value)

    @property
    def RTC_GPIO_PIN8_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN8_INT_TYPE_msb, self.__RTC_GPIO_PIN8_INT_TYPE_lsb)
    @RTC_GPIO_PIN8_INT_TYPE.setter
    def RTC_GPIO_PIN8_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN8_INT_TYPE_msb, self.__RTC_GPIO_PIN8_INT_TYPE_lsb, value)

    @property
    def RTC_GPIO_PIN8_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN8_PAD_DRIVER_msb, self.__RTC_GPIO_PIN8_PAD_DRIVER_lsb)
    @RTC_GPIO_PIN8_PAD_DRIVER.setter
    def RTC_GPIO_PIN8_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN8_PAD_DRIVER_msb, self.__RTC_GPIO_PIN8_PAD_DRIVER_lsb, value)
class RTC_GPIO_PIN9(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x4c
        self.__RTC_GPIO_PIN9_WAKEUP_ENABLE_lsb = 10
        self.__RTC_GPIO_PIN9_WAKEUP_ENABLE_msb = 10
        self.__RTC_GPIO_PIN9_INT_TYPE_lsb = 7
        self.__RTC_GPIO_PIN9_INT_TYPE_msb = 9
        self.__RTC_GPIO_PIN9_PAD_DRIVER_lsb = 2
        self.__RTC_GPIO_PIN9_PAD_DRIVER_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def RTC_GPIO_PIN9_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN9_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN9_WAKEUP_ENABLE_lsb)
    @RTC_GPIO_PIN9_WAKEUP_ENABLE.setter
    def RTC_GPIO_PIN9_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN9_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN9_WAKEUP_ENABLE_lsb, value)

    @property
    def RTC_GPIO_PIN9_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN9_INT_TYPE_msb, self.__RTC_GPIO_PIN9_INT_TYPE_lsb)
    @RTC_GPIO_PIN9_INT_TYPE.setter
    def RTC_GPIO_PIN9_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN9_INT_TYPE_msb, self.__RTC_GPIO_PIN9_INT_TYPE_lsb, value)

    @property
    def RTC_GPIO_PIN9_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN9_PAD_DRIVER_msb, self.__RTC_GPIO_PIN9_PAD_DRIVER_lsb)
    @RTC_GPIO_PIN9_PAD_DRIVER.setter
    def RTC_GPIO_PIN9_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN9_PAD_DRIVER_msb, self.__RTC_GPIO_PIN9_PAD_DRIVER_lsb, value)
class RTC_GPIO_PIN10(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x50
        self.__RTC_GPIO_PIN10_WAKEUP_ENABLE_lsb = 10
        self.__RTC_GPIO_PIN10_WAKEUP_ENABLE_msb = 10
        self.__RTC_GPIO_PIN10_INT_TYPE_lsb = 7
        self.__RTC_GPIO_PIN10_INT_TYPE_msb = 9
        self.__RTC_GPIO_PIN10_PAD_DRIVER_lsb = 2
        self.__RTC_GPIO_PIN10_PAD_DRIVER_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def RTC_GPIO_PIN10_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN10_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN10_WAKEUP_ENABLE_lsb)
    @RTC_GPIO_PIN10_WAKEUP_ENABLE.setter
    def RTC_GPIO_PIN10_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN10_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN10_WAKEUP_ENABLE_lsb, value)

    @property
    def RTC_GPIO_PIN10_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN10_INT_TYPE_msb, self.__RTC_GPIO_PIN10_INT_TYPE_lsb)
    @RTC_GPIO_PIN10_INT_TYPE.setter
    def RTC_GPIO_PIN10_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN10_INT_TYPE_msb, self.__RTC_GPIO_PIN10_INT_TYPE_lsb, value)

    @property
    def RTC_GPIO_PIN10_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN10_PAD_DRIVER_msb, self.__RTC_GPIO_PIN10_PAD_DRIVER_lsb)
    @RTC_GPIO_PIN10_PAD_DRIVER.setter
    def RTC_GPIO_PIN10_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN10_PAD_DRIVER_msb, self.__RTC_GPIO_PIN10_PAD_DRIVER_lsb, value)
class RTC_GPIO_PIN11(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x54
        self.__RTC_GPIO_PIN11_WAKEUP_ENABLE_lsb = 10
        self.__RTC_GPIO_PIN11_WAKEUP_ENABLE_msb = 10
        self.__RTC_GPIO_PIN11_INT_TYPE_lsb = 7
        self.__RTC_GPIO_PIN11_INT_TYPE_msb = 9
        self.__RTC_GPIO_PIN11_PAD_DRIVER_lsb = 2
        self.__RTC_GPIO_PIN11_PAD_DRIVER_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def RTC_GPIO_PIN11_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN11_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN11_WAKEUP_ENABLE_lsb)
    @RTC_GPIO_PIN11_WAKEUP_ENABLE.setter
    def RTC_GPIO_PIN11_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN11_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN11_WAKEUP_ENABLE_lsb, value)

    @property
    def RTC_GPIO_PIN11_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN11_INT_TYPE_msb, self.__RTC_GPIO_PIN11_INT_TYPE_lsb)
    @RTC_GPIO_PIN11_INT_TYPE.setter
    def RTC_GPIO_PIN11_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN11_INT_TYPE_msb, self.__RTC_GPIO_PIN11_INT_TYPE_lsb, value)

    @property
    def RTC_GPIO_PIN11_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN11_PAD_DRIVER_msb, self.__RTC_GPIO_PIN11_PAD_DRIVER_lsb)
    @RTC_GPIO_PIN11_PAD_DRIVER.setter
    def RTC_GPIO_PIN11_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN11_PAD_DRIVER_msb, self.__RTC_GPIO_PIN11_PAD_DRIVER_lsb, value)
class RTC_GPIO_PIN12(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x58
        self.__RTC_GPIO_PIN12_WAKEUP_ENABLE_lsb = 10
        self.__RTC_GPIO_PIN12_WAKEUP_ENABLE_msb = 10
        self.__RTC_GPIO_PIN12_INT_TYPE_lsb = 7
        self.__RTC_GPIO_PIN12_INT_TYPE_msb = 9
        self.__RTC_GPIO_PIN12_PAD_DRIVER_lsb = 2
        self.__RTC_GPIO_PIN12_PAD_DRIVER_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def RTC_GPIO_PIN12_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN12_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN12_WAKEUP_ENABLE_lsb)
    @RTC_GPIO_PIN12_WAKEUP_ENABLE.setter
    def RTC_GPIO_PIN12_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN12_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN12_WAKEUP_ENABLE_lsb, value)

    @property
    def RTC_GPIO_PIN12_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN12_INT_TYPE_msb, self.__RTC_GPIO_PIN12_INT_TYPE_lsb)
    @RTC_GPIO_PIN12_INT_TYPE.setter
    def RTC_GPIO_PIN12_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN12_INT_TYPE_msb, self.__RTC_GPIO_PIN12_INT_TYPE_lsb, value)

    @property
    def RTC_GPIO_PIN12_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN12_PAD_DRIVER_msb, self.__RTC_GPIO_PIN12_PAD_DRIVER_lsb)
    @RTC_GPIO_PIN12_PAD_DRIVER.setter
    def RTC_GPIO_PIN12_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN12_PAD_DRIVER_msb, self.__RTC_GPIO_PIN12_PAD_DRIVER_lsb, value)
class RTC_GPIO_PIN13(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x5c
        self.__RTC_GPIO_PIN13_WAKEUP_ENABLE_lsb = 10
        self.__RTC_GPIO_PIN13_WAKEUP_ENABLE_msb = 10
        self.__RTC_GPIO_PIN13_INT_TYPE_lsb = 7
        self.__RTC_GPIO_PIN13_INT_TYPE_msb = 9
        self.__RTC_GPIO_PIN13_PAD_DRIVER_lsb = 2
        self.__RTC_GPIO_PIN13_PAD_DRIVER_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def RTC_GPIO_PIN13_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN13_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN13_WAKEUP_ENABLE_lsb)
    @RTC_GPIO_PIN13_WAKEUP_ENABLE.setter
    def RTC_GPIO_PIN13_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN13_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN13_WAKEUP_ENABLE_lsb, value)

    @property
    def RTC_GPIO_PIN13_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN13_INT_TYPE_msb, self.__RTC_GPIO_PIN13_INT_TYPE_lsb)
    @RTC_GPIO_PIN13_INT_TYPE.setter
    def RTC_GPIO_PIN13_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN13_INT_TYPE_msb, self.__RTC_GPIO_PIN13_INT_TYPE_lsb, value)

    @property
    def RTC_GPIO_PIN13_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN13_PAD_DRIVER_msb, self.__RTC_GPIO_PIN13_PAD_DRIVER_lsb)
    @RTC_GPIO_PIN13_PAD_DRIVER.setter
    def RTC_GPIO_PIN13_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN13_PAD_DRIVER_msb, self.__RTC_GPIO_PIN13_PAD_DRIVER_lsb, value)
class RTC_GPIO_PIN14(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x60
        self.__RTC_GPIO_PIN14_WAKEUP_ENABLE_lsb = 10
        self.__RTC_GPIO_PIN14_WAKEUP_ENABLE_msb = 10
        self.__RTC_GPIO_PIN14_INT_TYPE_lsb = 7
        self.__RTC_GPIO_PIN14_INT_TYPE_msb = 9
        self.__RTC_GPIO_PIN14_PAD_DRIVER_lsb = 2
        self.__RTC_GPIO_PIN14_PAD_DRIVER_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def RTC_GPIO_PIN14_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN14_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN14_WAKEUP_ENABLE_lsb)
    @RTC_GPIO_PIN14_WAKEUP_ENABLE.setter
    def RTC_GPIO_PIN14_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN14_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN14_WAKEUP_ENABLE_lsb, value)

    @property
    def RTC_GPIO_PIN14_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN14_INT_TYPE_msb, self.__RTC_GPIO_PIN14_INT_TYPE_lsb)
    @RTC_GPIO_PIN14_INT_TYPE.setter
    def RTC_GPIO_PIN14_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN14_INT_TYPE_msb, self.__RTC_GPIO_PIN14_INT_TYPE_lsb, value)

    @property
    def RTC_GPIO_PIN14_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN14_PAD_DRIVER_msb, self.__RTC_GPIO_PIN14_PAD_DRIVER_lsb)
    @RTC_GPIO_PIN14_PAD_DRIVER.setter
    def RTC_GPIO_PIN14_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN14_PAD_DRIVER_msb, self.__RTC_GPIO_PIN14_PAD_DRIVER_lsb, value)
class RTC_GPIO_PIN15(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x64
        self.__RTC_GPIO_PIN15_WAKEUP_ENABLE_lsb = 10
        self.__RTC_GPIO_PIN15_WAKEUP_ENABLE_msb = 10
        self.__RTC_GPIO_PIN15_INT_TYPE_lsb = 7
        self.__RTC_GPIO_PIN15_INT_TYPE_msb = 9
        self.__RTC_GPIO_PIN15_PAD_DRIVER_lsb = 2
        self.__RTC_GPIO_PIN15_PAD_DRIVER_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def RTC_GPIO_PIN15_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN15_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN15_WAKEUP_ENABLE_lsb)
    @RTC_GPIO_PIN15_WAKEUP_ENABLE.setter
    def RTC_GPIO_PIN15_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN15_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN15_WAKEUP_ENABLE_lsb, value)

    @property
    def RTC_GPIO_PIN15_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN15_INT_TYPE_msb, self.__RTC_GPIO_PIN15_INT_TYPE_lsb)
    @RTC_GPIO_PIN15_INT_TYPE.setter
    def RTC_GPIO_PIN15_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN15_INT_TYPE_msb, self.__RTC_GPIO_PIN15_INT_TYPE_lsb, value)

    @property
    def RTC_GPIO_PIN15_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN15_PAD_DRIVER_msb, self.__RTC_GPIO_PIN15_PAD_DRIVER_lsb)
    @RTC_GPIO_PIN15_PAD_DRIVER.setter
    def RTC_GPIO_PIN15_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN15_PAD_DRIVER_msb, self.__RTC_GPIO_PIN15_PAD_DRIVER_lsb, value)
class RTC_GPIO_PIN16(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x68
        self.__RTC_GPIO_PIN16_WAKEUP_ENABLE_lsb = 10
        self.__RTC_GPIO_PIN16_WAKEUP_ENABLE_msb = 10
        self.__RTC_GPIO_PIN16_INT_TYPE_lsb = 7
        self.__RTC_GPIO_PIN16_INT_TYPE_msb = 9
        self.__RTC_GPIO_PIN16_PAD_DRIVER_lsb = 2
        self.__RTC_GPIO_PIN16_PAD_DRIVER_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def RTC_GPIO_PIN16_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN16_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN16_WAKEUP_ENABLE_lsb)
    @RTC_GPIO_PIN16_WAKEUP_ENABLE.setter
    def RTC_GPIO_PIN16_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN16_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN16_WAKEUP_ENABLE_lsb, value)

    @property
    def RTC_GPIO_PIN16_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN16_INT_TYPE_msb, self.__RTC_GPIO_PIN16_INT_TYPE_lsb)
    @RTC_GPIO_PIN16_INT_TYPE.setter
    def RTC_GPIO_PIN16_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN16_INT_TYPE_msb, self.__RTC_GPIO_PIN16_INT_TYPE_lsb, value)

    @property
    def RTC_GPIO_PIN16_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN16_PAD_DRIVER_msb, self.__RTC_GPIO_PIN16_PAD_DRIVER_lsb)
    @RTC_GPIO_PIN16_PAD_DRIVER.setter
    def RTC_GPIO_PIN16_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN16_PAD_DRIVER_msb, self.__RTC_GPIO_PIN16_PAD_DRIVER_lsb, value)
class RTC_GPIO_PIN17(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x6c
        self.__RTC_GPIO_PIN17_WAKEUP_ENABLE_lsb = 10
        self.__RTC_GPIO_PIN17_WAKEUP_ENABLE_msb = 10
        self.__RTC_GPIO_PIN17_INT_TYPE_lsb = 7
        self.__RTC_GPIO_PIN17_INT_TYPE_msb = 9
        self.__RTC_GPIO_PIN17_PAD_DRIVER_lsb = 2
        self.__RTC_GPIO_PIN17_PAD_DRIVER_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def RTC_GPIO_PIN17_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN17_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN17_WAKEUP_ENABLE_lsb)
    @RTC_GPIO_PIN17_WAKEUP_ENABLE.setter
    def RTC_GPIO_PIN17_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN17_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN17_WAKEUP_ENABLE_lsb, value)

    @property
    def RTC_GPIO_PIN17_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN17_INT_TYPE_msb, self.__RTC_GPIO_PIN17_INT_TYPE_lsb)
    @RTC_GPIO_PIN17_INT_TYPE.setter
    def RTC_GPIO_PIN17_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN17_INT_TYPE_msb, self.__RTC_GPIO_PIN17_INT_TYPE_lsb, value)

    @property
    def RTC_GPIO_PIN17_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN17_PAD_DRIVER_msb, self.__RTC_GPIO_PIN17_PAD_DRIVER_lsb)
    @RTC_GPIO_PIN17_PAD_DRIVER.setter
    def RTC_GPIO_PIN17_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN17_PAD_DRIVER_msb, self.__RTC_GPIO_PIN17_PAD_DRIVER_lsb, value)
class RTC_GPIO_PIN18(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x70
        self.__RTC_GPIO_PIN18_WAKEUP_ENABLE_lsb = 10
        self.__RTC_GPIO_PIN18_WAKEUP_ENABLE_msb = 10
        self.__RTC_GPIO_PIN18_INT_TYPE_lsb = 7
        self.__RTC_GPIO_PIN18_INT_TYPE_msb = 9
        self.__RTC_GPIO_PIN18_PAD_DRIVER_lsb = 2
        self.__RTC_GPIO_PIN18_PAD_DRIVER_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def RTC_GPIO_PIN18_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN18_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN18_WAKEUP_ENABLE_lsb)
    @RTC_GPIO_PIN18_WAKEUP_ENABLE.setter
    def RTC_GPIO_PIN18_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN18_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN18_WAKEUP_ENABLE_lsb, value)

    @property
    def RTC_GPIO_PIN18_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN18_INT_TYPE_msb, self.__RTC_GPIO_PIN18_INT_TYPE_lsb)
    @RTC_GPIO_PIN18_INT_TYPE.setter
    def RTC_GPIO_PIN18_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN18_INT_TYPE_msb, self.__RTC_GPIO_PIN18_INT_TYPE_lsb, value)

    @property
    def RTC_GPIO_PIN18_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN18_PAD_DRIVER_msb, self.__RTC_GPIO_PIN18_PAD_DRIVER_lsb)
    @RTC_GPIO_PIN18_PAD_DRIVER.setter
    def RTC_GPIO_PIN18_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN18_PAD_DRIVER_msb, self.__RTC_GPIO_PIN18_PAD_DRIVER_lsb, value)
class RTC_GPIO_PIN19(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x74
        self.__RTC_GPIO_PIN19_WAKEUP_ENABLE_lsb = 10
        self.__RTC_GPIO_PIN19_WAKEUP_ENABLE_msb = 10
        self.__RTC_GPIO_PIN19_INT_TYPE_lsb = 7
        self.__RTC_GPIO_PIN19_INT_TYPE_msb = 9
        self.__RTC_GPIO_PIN19_PAD_DRIVER_lsb = 2
        self.__RTC_GPIO_PIN19_PAD_DRIVER_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def RTC_GPIO_PIN19_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN19_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN19_WAKEUP_ENABLE_lsb)
    @RTC_GPIO_PIN19_WAKEUP_ENABLE.setter
    def RTC_GPIO_PIN19_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN19_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN19_WAKEUP_ENABLE_lsb, value)

    @property
    def RTC_GPIO_PIN19_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN19_INT_TYPE_msb, self.__RTC_GPIO_PIN19_INT_TYPE_lsb)
    @RTC_GPIO_PIN19_INT_TYPE.setter
    def RTC_GPIO_PIN19_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN19_INT_TYPE_msb, self.__RTC_GPIO_PIN19_INT_TYPE_lsb, value)

    @property
    def RTC_GPIO_PIN19_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN19_PAD_DRIVER_msb, self.__RTC_GPIO_PIN19_PAD_DRIVER_lsb)
    @RTC_GPIO_PIN19_PAD_DRIVER.setter
    def RTC_GPIO_PIN19_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN19_PAD_DRIVER_msb, self.__RTC_GPIO_PIN19_PAD_DRIVER_lsb, value)
class RTC_GPIO_PIN20(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x78
        self.__RTC_GPIO_PIN20_WAKEUP_ENABLE_lsb = 10
        self.__RTC_GPIO_PIN20_WAKEUP_ENABLE_msb = 10
        self.__RTC_GPIO_PIN20_INT_TYPE_lsb = 7
        self.__RTC_GPIO_PIN20_INT_TYPE_msb = 9
        self.__RTC_GPIO_PIN20_PAD_DRIVER_lsb = 2
        self.__RTC_GPIO_PIN20_PAD_DRIVER_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def RTC_GPIO_PIN20_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN20_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN20_WAKEUP_ENABLE_lsb)
    @RTC_GPIO_PIN20_WAKEUP_ENABLE.setter
    def RTC_GPIO_PIN20_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN20_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN20_WAKEUP_ENABLE_lsb, value)

    @property
    def RTC_GPIO_PIN20_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN20_INT_TYPE_msb, self.__RTC_GPIO_PIN20_INT_TYPE_lsb)
    @RTC_GPIO_PIN20_INT_TYPE.setter
    def RTC_GPIO_PIN20_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN20_INT_TYPE_msb, self.__RTC_GPIO_PIN20_INT_TYPE_lsb, value)

    @property
    def RTC_GPIO_PIN20_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN20_PAD_DRIVER_msb, self.__RTC_GPIO_PIN20_PAD_DRIVER_lsb)
    @RTC_GPIO_PIN20_PAD_DRIVER.setter
    def RTC_GPIO_PIN20_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN20_PAD_DRIVER_msb, self.__RTC_GPIO_PIN20_PAD_DRIVER_lsb, value)
class RTC_GPIO_PIN21(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x7c
        self.__RTC_GPIO_PIN21_WAKEUP_ENABLE_lsb = 10
        self.__RTC_GPIO_PIN21_WAKEUP_ENABLE_msb = 10
        self.__RTC_GPIO_PIN21_INT_TYPE_lsb = 7
        self.__RTC_GPIO_PIN21_INT_TYPE_msb = 9
        self.__RTC_GPIO_PIN21_PAD_DRIVER_lsb = 2
        self.__RTC_GPIO_PIN21_PAD_DRIVER_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def RTC_GPIO_PIN21_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN21_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN21_WAKEUP_ENABLE_lsb)
    @RTC_GPIO_PIN21_WAKEUP_ENABLE.setter
    def RTC_GPIO_PIN21_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN21_WAKEUP_ENABLE_msb, self.__RTC_GPIO_PIN21_WAKEUP_ENABLE_lsb, value)

    @property
    def RTC_GPIO_PIN21_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN21_INT_TYPE_msb, self.__RTC_GPIO_PIN21_INT_TYPE_lsb)
    @RTC_GPIO_PIN21_INT_TYPE.setter
    def RTC_GPIO_PIN21_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN21_INT_TYPE_msb, self.__RTC_GPIO_PIN21_INT_TYPE_lsb, value)

    @property
    def RTC_GPIO_PIN21_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__RTC_GPIO_PIN21_PAD_DRIVER_msb, self.__RTC_GPIO_PIN21_PAD_DRIVER_lsb)
    @RTC_GPIO_PIN21_PAD_DRIVER.setter
    def RTC_GPIO_PIN21_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__RTC_GPIO_PIN21_PAD_DRIVER_msb, self.__RTC_GPIO_PIN21_PAD_DRIVER_lsb, value)
class RTC_DEBUG_SEL(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x80
        self.__reg_rtc_debug_12m_no_gating_lsb = 25
        self.__reg_rtc_debug_12m_no_gating_msb = 25
        self.__reg_rtc_debug_sel4_lsb = 20
        self.__reg_rtc_debug_sel4_msb = 24
        self.__reg_rtc_debug_sel3_lsb = 15
        self.__reg_rtc_debug_sel3_msb = 19
        self.__reg_rtc_debug_sel2_lsb = 10
        self.__reg_rtc_debug_sel2_msb = 14
        self.__reg_rtc_debug_sel1_lsb = 5
        self.__reg_rtc_debug_sel1_msb = 9
        self.__reg_rtc_debug_sel0_lsb = 0
        self.__reg_rtc_debug_sel0_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rtc_debug_12m_no_gating(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_debug_12m_no_gating_msb, self.__reg_rtc_debug_12m_no_gating_lsb)
    @reg_rtc_debug_12m_no_gating.setter
    def reg_rtc_debug_12m_no_gating(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_debug_12m_no_gating_msb, self.__reg_rtc_debug_12m_no_gating_lsb, value)

    @property
    def reg_rtc_debug_sel4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_debug_sel4_msb, self.__reg_rtc_debug_sel4_lsb)
    @reg_rtc_debug_sel4.setter
    def reg_rtc_debug_sel4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_debug_sel4_msb, self.__reg_rtc_debug_sel4_lsb, value)

    @property
    def reg_rtc_debug_sel3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_debug_sel3_msb, self.__reg_rtc_debug_sel3_lsb)
    @reg_rtc_debug_sel3.setter
    def reg_rtc_debug_sel3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_debug_sel3_msb, self.__reg_rtc_debug_sel3_lsb, value)

    @property
    def reg_rtc_debug_sel2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_debug_sel2_msb, self.__reg_rtc_debug_sel2_lsb)
    @reg_rtc_debug_sel2.setter
    def reg_rtc_debug_sel2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_debug_sel2_msb, self.__reg_rtc_debug_sel2_lsb, value)

    @property
    def reg_rtc_debug_sel1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_debug_sel1_msb, self.__reg_rtc_debug_sel1_lsb)
    @reg_rtc_debug_sel1.setter
    def reg_rtc_debug_sel1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_debug_sel1_msb, self.__reg_rtc_debug_sel1_lsb, value)

    @property
    def reg_rtc_debug_sel0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_debug_sel0_msb, self.__reg_rtc_debug_sel0_lsb)
    @reg_rtc_debug_sel0.setter
    def reg_rtc_debug_sel0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_debug_sel0_msb, self.__reg_rtc_debug_sel0_lsb, value)
class TOUCH_PAD0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x84
        self.__reg_touch_pad0_drv_lsb = 29
        self.__reg_touch_pad0_drv_msb = 30
        self.__reg_touch_pad0_rde_lsb = 28
        self.__reg_touch_pad0_rde_msb = 28
        self.__reg_touch_pad0_rue_lsb = 27
        self.__reg_touch_pad0_rue_msb = 27
        self.__reg_touch_pad0_dac_lsb = 23
        self.__reg_touch_pad0_dac_msb = 25
        self.__reg_touch_pad0_start_lsb = 22
        self.__reg_touch_pad0_start_msb = 22
        self.__reg_touch_pad0_tie_opt_lsb = 21
        self.__reg_touch_pad0_tie_opt_msb = 21
        self.__reg_touch_pad0_xpd_lsb = 20
        self.__reg_touch_pad0_xpd_msb = 20
        self.__reg_touch_pad0_mux_sel_lsb = 19
        self.__reg_touch_pad0_mux_sel_msb = 19
        self.__reg_touch_pad0_fun_sel_lsb = 17
        self.__reg_touch_pad0_fun_sel_msb = 18
        self.__reg_touch_pad0_slp_sel_lsb = 16
        self.__reg_touch_pad0_slp_sel_msb = 16
        self.__reg_touch_pad0_slp_ie_lsb = 15
        self.__reg_touch_pad0_slp_ie_msb = 15
        self.__reg_touch_pad0_slp_oe_lsb = 14
        self.__reg_touch_pad0_slp_oe_msb = 14
        self.__reg_touch_pad0_fun_ie_lsb = 13
        self.__reg_touch_pad0_fun_ie_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_pad0_drv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad0_drv_msb, self.__reg_touch_pad0_drv_lsb)
    @reg_touch_pad0_drv.setter
    def reg_touch_pad0_drv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad0_drv_msb, self.__reg_touch_pad0_drv_lsb, value)

    @property
    def reg_touch_pad0_rde(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad0_rde_msb, self.__reg_touch_pad0_rde_lsb)
    @reg_touch_pad0_rde.setter
    def reg_touch_pad0_rde(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad0_rde_msb, self.__reg_touch_pad0_rde_lsb, value)

    @property
    def reg_touch_pad0_rue(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad0_rue_msb, self.__reg_touch_pad0_rue_lsb)
    @reg_touch_pad0_rue.setter
    def reg_touch_pad0_rue(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad0_rue_msb, self.__reg_touch_pad0_rue_lsb, value)

    @property
    def reg_touch_pad0_dac(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad0_dac_msb, self.__reg_touch_pad0_dac_lsb)
    @reg_touch_pad0_dac.setter
    def reg_touch_pad0_dac(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad0_dac_msb, self.__reg_touch_pad0_dac_lsb, value)

    @property
    def reg_touch_pad0_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad0_start_msb, self.__reg_touch_pad0_start_lsb)
    @reg_touch_pad0_start.setter
    def reg_touch_pad0_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad0_start_msb, self.__reg_touch_pad0_start_lsb, value)

    @property
    def reg_touch_pad0_tie_opt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad0_tie_opt_msb, self.__reg_touch_pad0_tie_opt_lsb)
    @reg_touch_pad0_tie_opt.setter
    def reg_touch_pad0_tie_opt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad0_tie_opt_msb, self.__reg_touch_pad0_tie_opt_lsb, value)

    @property
    def reg_touch_pad0_xpd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad0_xpd_msb, self.__reg_touch_pad0_xpd_lsb)
    @reg_touch_pad0_xpd.setter
    def reg_touch_pad0_xpd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad0_xpd_msb, self.__reg_touch_pad0_xpd_lsb, value)

    @property
    def reg_touch_pad0_mux_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad0_mux_sel_msb, self.__reg_touch_pad0_mux_sel_lsb)
    @reg_touch_pad0_mux_sel.setter
    def reg_touch_pad0_mux_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad0_mux_sel_msb, self.__reg_touch_pad0_mux_sel_lsb, value)

    @property
    def reg_touch_pad0_fun_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad0_fun_sel_msb, self.__reg_touch_pad0_fun_sel_lsb)
    @reg_touch_pad0_fun_sel.setter
    def reg_touch_pad0_fun_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad0_fun_sel_msb, self.__reg_touch_pad0_fun_sel_lsb, value)

    @property
    def reg_touch_pad0_slp_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad0_slp_sel_msb, self.__reg_touch_pad0_slp_sel_lsb)
    @reg_touch_pad0_slp_sel.setter
    def reg_touch_pad0_slp_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad0_slp_sel_msb, self.__reg_touch_pad0_slp_sel_lsb, value)

    @property
    def reg_touch_pad0_slp_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad0_slp_ie_msb, self.__reg_touch_pad0_slp_ie_lsb)
    @reg_touch_pad0_slp_ie.setter
    def reg_touch_pad0_slp_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad0_slp_ie_msb, self.__reg_touch_pad0_slp_ie_lsb, value)

    @property
    def reg_touch_pad0_slp_oe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad0_slp_oe_msb, self.__reg_touch_pad0_slp_oe_lsb)
    @reg_touch_pad0_slp_oe.setter
    def reg_touch_pad0_slp_oe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad0_slp_oe_msb, self.__reg_touch_pad0_slp_oe_lsb, value)

    @property
    def reg_touch_pad0_fun_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad0_fun_ie_msb, self.__reg_touch_pad0_fun_ie_lsb)
    @reg_touch_pad0_fun_ie.setter
    def reg_touch_pad0_fun_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad0_fun_ie_msb, self.__reg_touch_pad0_fun_ie_lsb, value)
class TOUCH_PAD1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x88
        self.__reg_touch_pad1_drv_lsb = 29
        self.__reg_touch_pad1_drv_msb = 30
        self.__reg_touch_pad1_rde_lsb = 28
        self.__reg_touch_pad1_rde_msb = 28
        self.__reg_touch_pad1_rue_lsb = 27
        self.__reg_touch_pad1_rue_msb = 27
        self.__reg_touch_pad1_dac_lsb = 23
        self.__reg_touch_pad1_dac_msb = 25
        self.__reg_touch_pad1_start_lsb = 22
        self.__reg_touch_pad1_start_msb = 22
        self.__reg_touch_pad1_tie_opt_lsb = 21
        self.__reg_touch_pad1_tie_opt_msb = 21
        self.__reg_touch_pad1_xpd_lsb = 20
        self.__reg_touch_pad1_xpd_msb = 20
        self.__reg_touch_pad1_mux_sel_lsb = 19
        self.__reg_touch_pad1_mux_sel_msb = 19
        self.__reg_touch_pad1_fun_sel_lsb = 17
        self.__reg_touch_pad1_fun_sel_msb = 18
        self.__reg_touch_pad1_slp_sel_lsb = 16
        self.__reg_touch_pad1_slp_sel_msb = 16
        self.__reg_touch_pad1_slp_ie_lsb = 15
        self.__reg_touch_pad1_slp_ie_msb = 15
        self.__reg_touch_pad1_slp_oe_lsb = 14
        self.__reg_touch_pad1_slp_oe_msb = 14
        self.__reg_touch_pad1_fun_ie_lsb = 13
        self.__reg_touch_pad1_fun_ie_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_pad1_drv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad1_drv_msb, self.__reg_touch_pad1_drv_lsb)
    @reg_touch_pad1_drv.setter
    def reg_touch_pad1_drv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad1_drv_msb, self.__reg_touch_pad1_drv_lsb, value)

    @property
    def reg_touch_pad1_rde(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad1_rde_msb, self.__reg_touch_pad1_rde_lsb)
    @reg_touch_pad1_rde.setter
    def reg_touch_pad1_rde(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad1_rde_msb, self.__reg_touch_pad1_rde_lsb, value)

    @property
    def reg_touch_pad1_rue(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad1_rue_msb, self.__reg_touch_pad1_rue_lsb)
    @reg_touch_pad1_rue.setter
    def reg_touch_pad1_rue(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad1_rue_msb, self.__reg_touch_pad1_rue_lsb, value)

    @property
    def reg_touch_pad1_dac(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad1_dac_msb, self.__reg_touch_pad1_dac_lsb)
    @reg_touch_pad1_dac.setter
    def reg_touch_pad1_dac(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad1_dac_msb, self.__reg_touch_pad1_dac_lsb, value)

    @property
    def reg_touch_pad1_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad1_start_msb, self.__reg_touch_pad1_start_lsb)
    @reg_touch_pad1_start.setter
    def reg_touch_pad1_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad1_start_msb, self.__reg_touch_pad1_start_lsb, value)

    @property
    def reg_touch_pad1_tie_opt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad1_tie_opt_msb, self.__reg_touch_pad1_tie_opt_lsb)
    @reg_touch_pad1_tie_opt.setter
    def reg_touch_pad1_tie_opt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad1_tie_opt_msb, self.__reg_touch_pad1_tie_opt_lsb, value)

    @property
    def reg_touch_pad1_xpd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad1_xpd_msb, self.__reg_touch_pad1_xpd_lsb)
    @reg_touch_pad1_xpd.setter
    def reg_touch_pad1_xpd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad1_xpd_msb, self.__reg_touch_pad1_xpd_lsb, value)

    @property
    def reg_touch_pad1_mux_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad1_mux_sel_msb, self.__reg_touch_pad1_mux_sel_lsb)
    @reg_touch_pad1_mux_sel.setter
    def reg_touch_pad1_mux_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad1_mux_sel_msb, self.__reg_touch_pad1_mux_sel_lsb, value)

    @property
    def reg_touch_pad1_fun_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad1_fun_sel_msb, self.__reg_touch_pad1_fun_sel_lsb)
    @reg_touch_pad1_fun_sel.setter
    def reg_touch_pad1_fun_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad1_fun_sel_msb, self.__reg_touch_pad1_fun_sel_lsb, value)

    @property
    def reg_touch_pad1_slp_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad1_slp_sel_msb, self.__reg_touch_pad1_slp_sel_lsb)
    @reg_touch_pad1_slp_sel.setter
    def reg_touch_pad1_slp_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad1_slp_sel_msb, self.__reg_touch_pad1_slp_sel_lsb, value)

    @property
    def reg_touch_pad1_slp_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad1_slp_ie_msb, self.__reg_touch_pad1_slp_ie_lsb)
    @reg_touch_pad1_slp_ie.setter
    def reg_touch_pad1_slp_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad1_slp_ie_msb, self.__reg_touch_pad1_slp_ie_lsb, value)

    @property
    def reg_touch_pad1_slp_oe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad1_slp_oe_msb, self.__reg_touch_pad1_slp_oe_lsb)
    @reg_touch_pad1_slp_oe.setter
    def reg_touch_pad1_slp_oe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad1_slp_oe_msb, self.__reg_touch_pad1_slp_oe_lsb, value)

    @property
    def reg_touch_pad1_fun_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad1_fun_ie_msb, self.__reg_touch_pad1_fun_ie_lsb)
    @reg_touch_pad1_fun_ie.setter
    def reg_touch_pad1_fun_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad1_fun_ie_msb, self.__reg_touch_pad1_fun_ie_lsb, value)
class TOUCH_PAD2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x8c
        self.__reg_touch_pad2_drv_lsb = 29
        self.__reg_touch_pad2_drv_msb = 30
        self.__reg_touch_pad2_rde_lsb = 28
        self.__reg_touch_pad2_rde_msb = 28
        self.__reg_touch_pad2_rue_lsb = 27
        self.__reg_touch_pad2_rue_msb = 27
        self.__reg_touch_pad2_dac_lsb = 23
        self.__reg_touch_pad2_dac_msb = 25
        self.__reg_touch_pad2_start_lsb = 22
        self.__reg_touch_pad2_start_msb = 22
        self.__reg_touch_pad2_tie_opt_lsb = 21
        self.__reg_touch_pad2_tie_opt_msb = 21
        self.__reg_touch_pad2_xpd_lsb = 20
        self.__reg_touch_pad2_xpd_msb = 20
        self.__reg_touch_pad2_mux_sel_lsb = 19
        self.__reg_touch_pad2_mux_sel_msb = 19
        self.__reg_touch_pad2_fun_sel_lsb = 17
        self.__reg_touch_pad2_fun_sel_msb = 18
        self.__reg_touch_pad2_slp_sel_lsb = 16
        self.__reg_touch_pad2_slp_sel_msb = 16
        self.__reg_touch_pad2_slp_ie_lsb = 15
        self.__reg_touch_pad2_slp_ie_msb = 15
        self.__reg_touch_pad2_slp_oe_lsb = 14
        self.__reg_touch_pad2_slp_oe_msb = 14
        self.__reg_touch_pad2_fun_ie_lsb = 13
        self.__reg_touch_pad2_fun_ie_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_pad2_drv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad2_drv_msb, self.__reg_touch_pad2_drv_lsb)
    @reg_touch_pad2_drv.setter
    def reg_touch_pad2_drv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad2_drv_msb, self.__reg_touch_pad2_drv_lsb, value)

    @property
    def reg_touch_pad2_rde(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad2_rde_msb, self.__reg_touch_pad2_rde_lsb)
    @reg_touch_pad2_rde.setter
    def reg_touch_pad2_rde(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad2_rde_msb, self.__reg_touch_pad2_rde_lsb, value)

    @property
    def reg_touch_pad2_rue(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad2_rue_msb, self.__reg_touch_pad2_rue_lsb)
    @reg_touch_pad2_rue.setter
    def reg_touch_pad2_rue(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad2_rue_msb, self.__reg_touch_pad2_rue_lsb, value)

    @property
    def reg_touch_pad2_dac(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad2_dac_msb, self.__reg_touch_pad2_dac_lsb)
    @reg_touch_pad2_dac.setter
    def reg_touch_pad2_dac(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad2_dac_msb, self.__reg_touch_pad2_dac_lsb, value)

    @property
    def reg_touch_pad2_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad2_start_msb, self.__reg_touch_pad2_start_lsb)
    @reg_touch_pad2_start.setter
    def reg_touch_pad2_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad2_start_msb, self.__reg_touch_pad2_start_lsb, value)

    @property
    def reg_touch_pad2_tie_opt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad2_tie_opt_msb, self.__reg_touch_pad2_tie_opt_lsb)
    @reg_touch_pad2_tie_opt.setter
    def reg_touch_pad2_tie_opt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad2_tie_opt_msb, self.__reg_touch_pad2_tie_opt_lsb, value)

    @property
    def reg_touch_pad2_xpd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad2_xpd_msb, self.__reg_touch_pad2_xpd_lsb)
    @reg_touch_pad2_xpd.setter
    def reg_touch_pad2_xpd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad2_xpd_msb, self.__reg_touch_pad2_xpd_lsb, value)

    @property
    def reg_touch_pad2_mux_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad2_mux_sel_msb, self.__reg_touch_pad2_mux_sel_lsb)
    @reg_touch_pad2_mux_sel.setter
    def reg_touch_pad2_mux_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad2_mux_sel_msb, self.__reg_touch_pad2_mux_sel_lsb, value)

    @property
    def reg_touch_pad2_fun_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad2_fun_sel_msb, self.__reg_touch_pad2_fun_sel_lsb)
    @reg_touch_pad2_fun_sel.setter
    def reg_touch_pad2_fun_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad2_fun_sel_msb, self.__reg_touch_pad2_fun_sel_lsb, value)

    @property
    def reg_touch_pad2_slp_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad2_slp_sel_msb, self.__reg_touch_pad2_slp_sel_lsb)
    @reg_touch_pad2_slp_sel.setter
    def reg_touch_pad2_slp_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad2_slp_sel_msb, self.__reg_touch_pad2_slp_sel_lsb, value)

    @property
    def reg_touch_pad2_slp_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad2_slp_ie_msb, self.__reg_touch_pad2_slp_ie_lsb)
    @reg_touch_pad2_slp_ie.setter
    def reg_touch_pad2_slp_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad2_slp_ie_msb, self.__reg_touch_pad2_slp_ie_lsb, value)

    @property
    def reg_touch_pad2_slp_oe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad2_slp_oe_msb, self.__reg_touch_pad2_slp_oe_lsb)
    @reg_touch_pad2_slp_oe.setter
    def reg_touch_pad2_slp_oe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad2_slp_oe_msb, self.__reg_touch_pad2_slp_oe_lsb, value)

    @property
    def reg_touch_pad2_fun_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad2_fun_ie_msb, self.__reg_touch_pad2_fun_ie_lsb)
    @reg_touch_pad2_fun_ie.setter
    def reg_touch_pad2_fun_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad2_fun_ie_msb, self.__reg_touch_pad2_fun_ie_lsb, value)
class TOUCH_PAD3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x90
        self.__reg_touch_pad3_drv_lsb = 29
        self.__reg_touch_pad3_drv_msb = 30
        self.__reg_touch_pad3_rde_lsb = 28
        self.__reg_touch_pad3_rde_msb = 28
        self.__reg_touch_pad3_rue_lsb = 27
        self.__reg_touch_pad3_rue_msb = 27
        self.__reg_touch_pad3_dac_lsb = 23
        self.__reg_touch_pad3_dac_msb = 25
        self.__reg_touch_pad3_start_lsb = 22
        self.__reg_touch_pad3_start_msb = 22
        self.__reg_touch_pad3_tie_opt_lsb = 21
        self.__reg_touch_pad3_tie_opt_msb = 21
        self.__reg_touch_pad3_xpd_lsb = 20
        self.__reg_touch_pad3_xpd_msb = 20
        self.__reg_touch_pad3_mux_sel_lsb = 19
        self.__reg_touch_pad3_mux_sel_msb = 19
        self.__reg_touch_pad3_fun_sel_lsb = 17
        self.__reg_touch_pad3_fun_sel_msb = 18
        self.__reg_touch_pad3_slp_sel_lsb = 16
        self.__reg_touch_pad3_slp_sel_msb = 16
        self.__reg_touch_pad3_slp_ie_lsb = 15
        self.__reg_touch_pad3_slp_ie_msb = 15
        self.__reg_touch_pad3_slp_oe_lsb = 14
        self.__reg_touch_pad3_slp_oe_msb = 14
        self.__reg_touch_pad3_fun_ie_lsb = 13
        self.__reg_touch_pad3_fun_ie_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_pad3_drv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad3_drv_msb, self.__reg_touch_pad3_drv_lsb)
    @reg_touch_pad3_drv.setter
    def reg_touch_pad3_drv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad3_drv_msb, self.__reg_touch_pad3_drv_lsb, value)

    @property
    def reg_touch_pad3_rde(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad3_rde_msb, self.__reg_touch_pad3_rde_lsb)
    @reg_touch_pad3_rde.setter
    def reg_touch_pad3_rde(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad3_rde_msb, self.__reg_touch_pad3_rde_lsb, value)

    @property
    def reg_touch_pad3_rue(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad3_rue_msb, self.__reg_touch_pad3_rue_lsb)
    @reg_touch_pad3_rue.setter
    def reg_touch_pad3_rue(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad3_rue_msb, self.__reg_touch_pad3_rue_lsb, value)

    @property
    def reg_touch_pad3_dac(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad3_dac_msb, self.__reg_touch_pad3_dac_lsb)
    @reg_touch_pad3_dac.setter
    def reg_touch_pad3_dac(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad3_dac_msb, self.__reg_touch_pad3_dac_lsb, value)

    @property
    def reg_touch_pad3_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad3_start_msb, self.__reg_touch_pad3_start_lsb)
    @reg_touch_pad3_start.setter
    def reg_touch_pad3_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad3_start_msb, self.__reg_touch_pad3_start_lsb, value)

    @property
    def reg_touch_pad3_tie_opt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad3_tie_opt_msb, self.__reg_touch_pad3_tie_opt_lsb)
    @reg_touch_pad3_tie_opt.setter
    def reg_touch_pad3_tie_opt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad3_tie_opt_msb, self.__reg_touch_pad3_tie_opt_lsb, value)

    @property
    def reg_touch_pad3_xpd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad3_xpd_msb, self.__reg_touch_pad3_xpd_lsb)
    @reg_touch_pad3_xpd.setter
    def reg_touch_pad3_xpd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad3_xpd_msb, self.__reg_touch_pad3_xpd_lsb, value)

    @property
    def reg_touch_pad3_mux_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad3_mux_sel_msb, self.__reg_touch_pad3_mux_sel_lsb)
    @reg_touch_pad3_mux_sel.setter
    def reg_touch_pad3_mux_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad3_mux_sel_msb, self.__reg_touch_pad3_mux_sel_lsb, value)

    @property
    def reg_touch_pad3_fun_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad3_fun_sel_msb, self.__reg_touch_pad3_fun_sel_lsb)
    @reg_touch_pad3_fun_sel.setter
    def reg_touch_pad3_fun_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad3_fun_sel_msb, self.__reg_touch_pad3_fun_sel_lsb, value)

    @property
    def reg_touch_pad3_slp_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad3_slp_sel_msb, self.__reg_touch_pad3_slp_sel_lsb)
    @reg_touch_pad3_slp_sel.setter
    def reg_touch_pad3_slp_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad3_slp_sel_msb, self.__reg_touch_pad3_slp_sel_lsb, value)

    @property
    def reg_touch_pad3_slp_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad3_slp_ie_msb, self.__reg_touch_pad3_slp_ie_lsb)
    @reg_touch_pad3_slp_ie.setter
    def reg_touch_pad3_slp_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad3_slp_ie_msb, self.__reg_touch_pad3_slp_ie_lsb, value)

    @property
    def reg_touch_pad3_slp_oe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad3_slp_oe_msb, self.__reg_touch_pad3_slp_oe_lsb)
    @reg_touch_pad3_slp_oe.setter
    def reg_touch_pad3_slp_oe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad3_slp_oe_msb, self.__reg_touch_pad3_slp_oe_lsb, value)

    @property
    def reg_touch_pad3_fun_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad3_fun_ie_msb, self.__reg_touch_pad3_fun_ie_lsb)
    @reg_touch_pad3_fun_ie.setter
    def reg_touch_pad3_fun_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad3_fun_ie_msb, self.__reg_touch_pad3_fun_ie_lsb, value)
class TOUCH_PAD4(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x94
        self.__reg_touch_pad4_drv_lsb = 29
        self.__reg_touch_pad4_drv_msb = 30
        self.__reg_touch_pad4_rde_lsb = 28
        self.__reg_touch_pad4_rde_msb = 28
        self.__reg_touch_pad4_rue_lsb = 27
        self.__reg_touch_pad4_rue_msb = 27
        self.__reg_touch_pad4_dac_lsb = 23
        self.__reg_touch_pad4_dac_msb = 25
        self.__reg_touch_pad4_start_lsb = 22
        self.__reg_touch_pad4_start_msb = 22
        self.__reg_touch_pad4_tie_opt_lsb = 21
        self.__reg_touch_pad4_tie_opt_msb = 21
        self.__reg_touch_pad4_xpd_lsb = 20
        self.__reg_touch_pad4_xpd_msb = 20
        self.__reg_touch_pad4_mux_sel_lsb = 19
        self.__reg_touch_pad4_mux_sel_msb = 19
        self.__reg_touch_pad4_fun_sel_lsb = 17
        self.__reg_touch_pad4_fun_sel_msb = 18
        self.__reg_touch_pad4_slp_sel_lsb = 16
        self.__reg_touch_pad4_slp_sel_msb = 16
        self.__reg_touch_pad4_slp_ie_lsb = 15
        self.__reg_touch_pad4_slp_ie_msb = 15
        self.__reg_touch_pad4_slp_oe_lsb = 14
        self.__reg_touch_pad4_slp_oe_msb = 14
        self.__reg_touch_pad4_fun_ie_lsb = 13
        self.__reg_touch_pad4_fun_ie_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_pad4_drv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad4_drv_msb, self.__reg_touch_pad4_drv_lsb)
    @reg_touch_pad4_drv.setter
    def reg_touch_pad4_drv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad4_drv_msb, self.__reg_touch_pad4_drv_lsb, value)

    @property
    def reg_touch_pad4_rde(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad4_rde_msb, self.__reg_touch_pad4_rde_lsb)
    @reg_touch_pad4_rde.setter
    def reg_touch_pad4_rde(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad4_rde_msb, self.__reg_touch_pad4_rde_lsb, value)

    @property
    def reg_touch_pad4_rue(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad4_rue_msb, self.__reg_touch_pad4_rue_lsb)
    @reg_touch_pad4_rue.setter
    def reg_touch_pad4_rue(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad4_rue_msb, self.__reg_touch_pad4_rue_lsb, value)

    @property
    def reg_touch_pad4_dac(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad4_dac_msb, self.__reg_touch_pad4_dac_lsb)
    @reg_touch_pad4_dac.setter
    def reg_touch_pad4_dac(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad4_dac_msb, self.__reg_touch_pad4_dac_lsb, value)

    @property
    def reg_touch_pad4_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad4_start_msb, self.__reg_touch_pad4_start_lsb)
    @reg_touch_pad4_start.setter
    def reg_touch_pad4_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad4_start_msb, self.__reg_touch_pad4_start_lsb, value)

    @property
    def reg_touch_pad4_tie_opt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad4_tie_opt_msb, self.__reg_touch_pad4_tie_opt_lsb)
    @reg_touch_pad4_tie_opt.setter
    def reg_touch_pad4_tie_opt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad4_tie_opt_msb, self.__reg_touch_pad4_tie_opt_lsb, value)

    @property
    def reg_touch_pad4_xpd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad4_xpd_msb, self.__reg_touch_pad4_xpd_lsb)
    @reg_touch_pad4_xpd.setter
    def reg_touch_pad4_xpd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad4_xpd_msb, self.__reg_touch_pad4_xpd_lsb, value)

    @property
    def reg_touch_pad4_mux_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad4_mux_sel_msb, self.__reg_touch_pad4_mux_sel_lsb)
    @reg_touch_pad4_mux_sel.setter
    def reg_touch_pad4_mux_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad4_mux_sel_msb, self.__reg_touch_pad4_mux_sel_lsb, value)

    @property
    def reg_touch_pad4_fun_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad4_fun_sel_msb, self.__reg_touch_pad4_fun_sel_lsb)
    @reg_touch_pad4_fun_sel.setter
    def reg_touch_pad4_fun_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad4_fun_sel_msb, self.__reg_touch_pad4_fun_sel_lsb, value)

    @property
    def reg_touch_pad4_slp_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad4_slp_sel_msb, self.__reg_touch_pad4_slp_sel_lsb)
    @reg_touch_pad4_slp_sel.setter
    def reg_touch_pad4_slp_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad4_slp_sel_msb, self.__reg_touch_pad4_slp_sel_lsb, value)

    @property
    def reg_touch_pad4_slp_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad4_slp_ie_msb, self.__reg_touch_pad4_slp_ie_lsb)
    @reg_touch_pad4_slp_ie.setter
    def reg_touch_pad4_slp_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad4_slp_ie_msb, self.__reg_touch_pad4_slp_ie_lsb, value)

    @property
    def reg_touch_pad4_slp_oe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad4_slp_oe_msb, self.__reg_touch_pad4_slp_oe_lsb)
    @reg_touch_pad4_slp_oe.setter
    def reg_touch_pad4_slp_oe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad4_slp_oe_msb, self.__reg_touch_pad4_slp_oe_lsb, value)

    @property
    def reg_touch_pad4_fun_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad4_fun_ie_msb, self.__reg_touch_pad4_fun_ie_lsb)
    @reg_touch_pad4_fun_ie.setter
    def reg_touch_pad4_fun_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad4_fun_ie_msb, self.__reg_touch_pad4_fun_ie_lsb, value)
class TOUCH_PAD5(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x98
        self.__reg_touch_pad5_drv_lsb = 29
        self.__reg_touch_pad5_drv_msb = 30
        self.__reg_touch_pad5_rde_lsb = 28
        self.__reg_touch_pad5_rde_msb = 28
        self.__reg_touch_pad5_rue_lsb = 27
        self.__reg_touch_pad5_rue_msb = 27
        self.__reg_touch_pad5_dac_lsb = 23
        self.__reg_touch_pad5_dac_msb = 25
        self.__reg_touch_pad5_start_lsb = 22
        self.__reg_touch_pad5_start_msb = 22
        self.__reg_touch_pad5_tie_opt_lsb = 21
        self.__reg_touch_pad5_tie_opt_msb = 21
        self.__reg_touch_pad5_xpd_lsb = 20
        self.__reg_touch_pad5_xpd_msb = 20
        self.__reg_touch_pad5_mux_sel_lsb = 19
        self.__reg_touch_pad5_mux_sel_msb = 19
        self.__reg_touch_pad5_fun_sel_lsb = 17
        self.__reg_touch_pad5_fun_sel_msb = 18
        self.__reg_touch_pad5_slp_sel_lsb = 16
        self.__reg_touch_pad5_slp_sel_msb = 16
        self.__reg_touch_pad5_slp_ie_lsb = 15
        self.__reg_touch_pad5_slp_ie_msb = 15
        self.__reg_touch_pad5_slp_oe_lsb = 14
        self.__reg_touch_pad5_slp_oe_msb = 14
        self.__reg_touch_pad5_fun_ie_lsb = 13
        self.__reg_touch_pad5_fun_ie_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_pad5_drv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad5_drv_msb, self.__reg_touch_pad5_drv_lsb)
    @reg_touch_pad5_drv.setter
    def reg_touch_pad5_drv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad5_drv_msb, self.__reg_touch_pad5_drv_lsb, value)

    @property
    def reg_touch_pad5_rde(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad5_rde_msb, self.__reg_touch_pad5_rde_lsb)
    @reg_touch_pad5_rde.setter
    def reg_touch_pad5_rde(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad5_rde_msb, self.__reg_touch_pad5_rde_lsb, value)

    @property
    def reg_touch_pad5_rue(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad5_rue_msb, self.__reg_touch_pad5_rue_lsb)
    @reg_touch_pad5_rue.setter
    def reg_touch_pad5_rue(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad5_rue_msb, self.__reg_touch_pad5_rue_lsb, value)

    @property
    def reg_touch_pad5_dac(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad5_dac_msb, self.__reg_touch_pad5_dac_lsb)
    @reg_touch_pad5_dac.setter
    def reg_touch_pad5_dac(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad5_dac_msb, self.__reg_touch_pad5_dac_lsb, value)

    @property
    def reg_touch_pad5_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad5_start_msb, self.__reg_touch_pad5_start_lsb)
    @reg_touch_pad5_start.setter
    def reg_touch_pad5_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad5_start_msb, self.__reg_touch_pad5_start_lsb, value)

    @property
    def reg_touch_pad5_tie_opt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad5_tie_opt_msb, self.__reg_touch_pad5_tie_opt_lsb)
    @reg_touch_pad5_tie_opt.setter
    def reg_touch_pad5_tie_opt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad5_tie_opt_msb, self.__reg_touch_pad5_tie_opt_lsb, value)

    @property
    def reg_touch_pad5_xpd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad5_xpd_msb, self.__reg_touch_pad5_xpd_lsb)
    @reg_touch_pad5_xpd.setter
    def reg_touch_pad5_xpd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad5_xpd_msb, self.__reg_touch_pad5_xpd_lsb, value)

    @property
    def reg_touch_pad5_mux_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad5_mux_sel_msb, self.__reg_touch_pad5_mux_sel_lsb)
    @reg_touch_pad5_mux_sel.setter
    def reg_touch_pad5_mux_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad5_mux_sel_msb, self.__reg_touch_pad5_mux_sel_lsb, value)

    @property
    def reg_touch_pad5_fun_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad5_fun_sel_msb, self.__reg_touch_pad5_fun_sel_lsb)
    @reg_touch_pad5_fun_sel.setter
    def reg_touch_pad5_fun_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad5_fun_sel_msb, self.__reg_touch_pad5_fun_sel_lsb, value)

    @property
    def reg_touch_pad5_slp_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad5_slp_sel_msb, self.__reg_touch_pad5_slp_sel_lsb)
    @reg_touch_pad5_slp_sel.setter
    def reg_touch_pad5_slp_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad5_slp_sel_msb, self.__reg_touch_pad5_slp_sel_lsb, value)

    @property
    def reg_touch_pad5_slp_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad5_slp_ie_msb, self.__reg_touch_pad5_slp_ie_lsb)
    @reg_touch_pad5_slp_ie.setter
    def reg_touch_pad5_slp_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad5_slp_ie_msb, self.__reg_touch_pad5_slp_ie_lsb, value)

    @property
    def reg_touch_pad5_slp_oe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad5_slp_oe_msb, self.__reg_touch_pad5_slp_oe_lsb)
    @reg_touch_pad5_slp_oe.setter
    def reg_touch_pad5_slp_oe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad5_slp_oe_msb, self.__reg_touch_pad5_slp_oe_lsb, value)

    @property
    def reg_touch_pad5_fun_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad5_fun_ie_msb, self.__reg_touch_pad5_fun_ie_lsb)
    @reg_touch_pad5_fun_ie.setter
    def reg_touch_pad5_fun_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad5_fun_ie_msb, self.__reg_touch_pad5_fun_ie_lsb, value)
class TOUCH_PAD6(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x9c
        self.__reg_touch_pad6_drv_lsb = 29
        self.__reg_touch_pad6_drv_msb = 30
        self.__reg_touch_pad6_rde_lsb = 28
        self.__reg_touch_pad6_rde_msb = 28
        self.__reg_touch_pad6_rue_lsb = 27
        self.__reg_touch_pad6_rue_msb = 27
        self.__reg_touch_pad6_dac_lsb = 23
        self.__reg_touch_pad6_dac_msb = 25
        self.__reg_touch_pad6_start_lsb = 22
        self.__reg_touch_pad6_start_msb = 22
        self.__reg_touch_pad6_tie_opt_lsb = 21
        self.__reg_touch_pad6_tie_opt_msb = 21
        self.__reg_touch_pad6_xpd_lsb = 20
        self.__reg_touch_pad6_xpd_msb = 20
        self.__reg_touch_pad6_mux_sel_lsb = 19
        self.__reg_touch_pad6_mux_sel_msb = 19
        self.__reg_touch_pad6_fun_sel_lsb = 17
        self.__reg_touch_pad6_fun_sel_msb = 18
        self.__reg_touch_pad6_slp_sel_lsb = 16
        self.__reg_touch_pad6_slp_sel_msb = 16
        self.__reg_touch_pad6_slp_ie_lsb = 15
        self.__reg_touch_pad6_slp_ie_msb = 15
        self.__reg_touch_pad6_slp_oe_lsb = 14
        self.__reg_touch_pad6_slp_oe_msb = 14
        self.__reg_touch_pad6_fun_ie_lsb = 13
        self.__reg_touch_pad6_fun_ie_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_pad6_drv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad6_drv_msb, self.__reg_touch_pad6_drv_lsb)
    @reg_touch_pad6_drv.setter
    def reg_touch_pad6_drv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad6_drv_msb, self.__reg_touch_pad6_drv_lsb, value)

    @property
    def reg_touch_pad6_rde(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad6_rde_msb, self.__reg_touch_pad6_rde_lsb)
    @reg_touch_pad6_rde.setter
    def reg_touch_pad6_rde(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad6_rde_msb, self.__reg_touch_pad6_rde_lsb, value)

    @property
    def reg_touch_pad6_rue(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad6_rue_msb, self.__reg_touch_pad6_rue_lsb)
    @reg_touch_pad6_rue.setter
    def reg_touch_pad6_rue(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad6_rue_msb, self.__reg_touch_pad6_rue_lsb, value)

    @property
    def reg_touch_pad6_dac(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad6_dac_msb, self.__reg_touch_pad6_dac_lsb)
    @reg_touch_pad6_dac.setter
    def reg_touch_pad6_dac(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad6_dac_msb, self.__reg_touch_pad6_dac_lsb, value)

    @property
    def reg_touch_pad6_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad6_start_msb, self.__reg_touch_pad6_start_lsb)
    @reg_touch_pad6_start.setter
    def reg_touch_pad6_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad6_start_msb, self.__reg_touch_pad6_start_lsb, value)

    @property
    def reg_touch_pad6_tie_opt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad6_tie_opt_msb, self.__reg_touch_pad6_tie_opt_lsb)
    @reg_touch_pad6_tie_opt.setter
    def reg_touch_pad6_tie_opt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad6_tie_opt_msb, self.__reg_touch_pad6_tie_opt_lsb, value)

    @property
    def reg_touch_pad6_xpd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad6_xpd_msb, self.__reg_touch_pad6_xpd_lsb)
    @reg_touch_pad6_xpd.setter
    def reg_touch_pad6_xpd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad6_xpd_msb, self.__reg_touch_pad6_xpd_lsb, value)

    @property
    def reg_touch_pad6_mux_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad6_mux_sel_msb, self.__reg_touch_pad6_mux_sel_lsb)
    @reg_touch_pad6_mux_sel.setter
    def reg_touch_pad6_mux_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad6_mux_sel_msb, self.__reg_touch_pad6_mux_sel_lsb, value)

    @property
    def reg_touch_pad6_fun_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad6_fun_sel_msb, self.__reg_touch_pad6_fun_sel_lsb)
    @reg_touch_pad6_fun_sel.setter
    def reg_touch_pad6_fun_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad6_fun_sel_msb, self.__reg_touch_pad6_fun_sel_lsb, value)

    @property
    def reg_touch_pad6_slp_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad6_slp_sel_msb, self.__reg_touch_pad6_slp_sel_lsb)
    @reg_touch_pad6_slp_sel.setter
    def reg_touch_pad6_slp_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad6_slp_sel_msb, self.__reg_touch_pad6_slp_sel_lsb, value)

    @property
    def reg_touch_pad6_slp_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad6_slp_ie_msb, self.__reg_touch_pad6_slp_ie_lsb)
    @reg_touch_pad6_slp_ie.setter
    def reg_touch_pad6_slp_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad6_slp_ie_msb, self.__reg_touch_pad6_slp_ie_lsb, value)

    @property
    def reg_touch_pad6_slp_oe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad6_slp_oe_msb, self.__reg_touch_pad6_slp_oe_lsb)
    @reg_touch_pad6_slp_oe.setter
    def reg_touch_pad6_slp_oe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad6_slp_oe_msb, self.__reg_touch_pad6_slp_oe_lsb, value)

    @property
    def reg_touch_pad6_fun_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad6_fun_ie_msb, self.__reg_touch_pad6_fun_ie_lsb)
    @reg_touch_pad6_fun_ie.setter
    def reg_touch_pad6_fun_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad6_fun_ie_msb, self.__reg_touch_pad6_fun_ie_lsb, value)
class TOUCH_PAD7(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0xa0
        self.__reg_touch_pad7_drv_lsb = 29
        self.__reg_touch_pad7_drv_msb = 30
        self.__reg_touch_pad7_rde_lsb = 28
        self.__reg_touch_pad7_rde_msb = 28
        self.__reg_touch_pad7_rue_lsb = 27
        self.__reg_touch_pad7_rue_msb = 27
        self.__reg_touch_pad7_dac_lsb = 23
        self.__reg_touch_pad7_dac_msb = 25
        self.__reg_touch_pad7_start_lsb = 22
        self.__reg_touch_pad7_start_msb = 22
        self.__reg_touch_pad7_tie_opt_lsb = 21
        self.__reg_touch_pad7_tie_opt_msb = 21
        self.__reg_touch_pad7_xpd_lsb = 20
        self.__reg_touch_pad7_xpd_msb = 20
        self.__reg_touch_pad7_mux_sel_lsb = 19
        self.__reg_touch_pad7_mux_sel_msb = 19
        self.__reg_touch_pad7_fun_sel_lsb = 17
        self.__reg_touch_pad7_fun_sel_msb = 18
        self.__reg_touch_pad7_slp_sel_lsb = 16
        self.__reg_touch_pad7_slp_sel_msb = 16
        self.__reg_touch_pad7_slp_ie_lsb = 15
        self.__reg_touch_pad7_slp_ie_msb = 15
        self.__reg_touch_pad7_slp_oe_lsb = 14
        self.__reg_touch_pad7_slp_oe_msb = 14
        self.__reg_touch_pad7_fun_ie_lsb = 13
        self.__reg_touch_pad7_fun_ie_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_pad7_drv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad7_drv_msb, self.__reg_touch_pad7_drv_lsb)
    @reg_touch_pad7_drv.setter
    def reg_touch_pad7_drv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad7_drv_msb, self.__reg_touch_pad7_drv_lsb, value)

    @property
    def reg_touch_pad7_rde(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad7_rde_msb, self.__reg_touch_pad7_rde_lsb)
    @reg_touch_pad7_rde.setter
    def reg_touch_pad7_rde(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad7_rde_msb, self.__reg_touch_pad7_rde_lsb, value)

    @property
    def reg_touch_pad7_rue(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad7_rue_msb, self.__reg_touch_pad7_rue_lsb)
    @reg_touch_pad7_rue.setter
    def reg_touch_pad7_rue(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad7_rue_msb, self.__reg_touch_pad7_rue_lsb, value)

    @property
    def reg_touch_pad7_dac(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad7_dac_msb, self.__reg_touch_pad7_dac_lsb)
    @reg_touch_pad7_dac.setter
    def reg_touch_pad7_dac(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad7_dac_msb, self.__reg_touch_pad7_dac_lsb, value)

    @property
    def reg_touch_pad7_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad7_start_msb, self.__reg_touch_pad7_start_lsb)
    @reg_touch_pad7_start.setter
    def reg_touch_pad7_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad7_start_msb, self.__reg_touch_pad7_start_lsb, value)

    @property
    def reg_touch_pad7_tie_opt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad7_tie_opt_msb, self.__reg_touch_pad7_tie_opt_lsb)
    @reg_touch_pad7_tie_opt.setter
    def reg_touch_pad7_tie_opt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad7_tie_opt_msb, self.__reg_touch_pad7_tie_opt_lsb, value)

    @property
    def reg_touch_pad7_xpd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad7_xpd_msb, self.__reg_touch_pad7_xpd_lsb)
    @reg_touch_pad7_xpd.setter
    def reg_touch_pad7_xpd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad7_xpd_msb, self.__reg_touch_pad7_xpd_lsb, value)

    @property
    def reg_touch_pad7_mux_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad7_mux_sel_msb, self.__reg_touch_pad7_mux_sel_lsb)
    @reg_touch_pad7_mux_sel.setter
    def reg_touch_pad7_mux_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad7_mux_sel_msb, self.__reg_touch_pad7_mux_sel_lsb, value)

    @property
    def reg_touch_pad7_fun_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad7_fun_sel_msb, self.__reg_touch_pad7_fun_sel_lsb)
    @reg_touch_pad7_fun_sel.setter
    def reg_touch_pad7_fun_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad7_fun_sel_msb, self.__reg_touch_pad7_fun_sel_lsb, value)

    @property
    def reg_touch_pad7_slp_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad7_slp_sel_msb, self.__reg_touch_pad7_slp_sel_lsb)
    @reg_touch_pad7_slp_sel.setter
    def reg_touch_pad7_slp_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad7_slp_sel_msb, self.__reg_touch_pad7_slp_sel_lsb, value)

    @property
    def reg_touch_pad7_slp_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad7_slp_ie_msb, self.__reg_touch_pad7_slp_ie_lsb)
    @reg_touch_pad7_slp_ie.setter
    def reg_touch_pad7_slp_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad7_slp_ie_msb, self.__reg_touch_pad7_slp_ie_lsb, value)

    @property
    def reg_touch_pad7_slp_oe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad7_slp_oe_msb, self.__reg_touch_pad7_slp_oe_lsb)
    @reg_touch_pad7_slp_oe.setter
    def reg_touch_pad7_slp_oe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad7_slp_oe_msb, self.__reg_touch_pad7_slp_oe_lsb, value)

    @property
    def reg_touch_pad7_fun_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad7_fun_ie_msb, self.__reg_touch_pad7_fun_ie_lsb)
    @reg_touch_pad7_fun_ie.setter
    def reg_touch_pad7_fun_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad7_fun_ie_msb, self.__reg_touch_pad7_fun_ie_lsb, value)
class TOUCH_PAD8(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0xa4
        self.__reg_touch_pad8_drv_lsb = 29
        self.__reg_touch_pad8_drv_msb = 30
        self.__reg_touch_pad8_rde_lsb = 28
        self.__reg_touch_pad8_rde_msb = 28
        self.__reg_touch_pad8_rue_lsb = 27
        self.__reg_touch_pad8_rue_msb = 27
        self.__reg_touch_pad8_dac_lsb = 23
        self.__reg_touch_pad8_dac_msb = 25
        self.__reg_touch_pad8_start_lsb = 22
        self.__reg_touch_pad8_start_msb = 22
        self.__reg_touch_pad8_tie_opt_lsb = 21
        self.__reg_touch_pad8_tie_opt_msb = 21
        self.__reg_touch_pad8_xpd_lsb = 20
        self.__reg_touch_pad8_xpd_msb = 20
        self.__reg_touch_pad8_mux_sel_lsb = 19
        self.__reg_touch_pad8_mux_sel_msb = 19
        self.__reg_touch_pad8_fun_sel_lsb = 17
        self.__reg_touch_pad8_fun_sel_msb = 18
        self.__reg_touch_pad8_slp_sel_lsb = 16
        self.__reg_touch_pad8_slp_sel_msb = 16
        self.__reg_touch_pad8_slp_ie_lsb = 15
        self.__reg_touch_pad8_slp_ie_msb = 15
        self.__reg_touch_pad8_slp_oe_lsb = 14
        self.__reg_touch_pad8_slp_oe_msb = 14
        self.__reg_touch_pad8_fun_ie_lsb = 13
        self.__reg_touch_pad8_fun_ie_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_pad8_drv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad8_drv_msb, self.__reg_touch_pad8_drv_lsb)
    @reg_touch_pad8_drv.setter
    def reg_touch_pad8_drv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad8_drv_msb, self.__reg_touch_pad8_drv_lsb, value)

    @property
    def reg_touch_pad8_rde(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad8_rde_msb, self.__reg_touch_pad8_rde_lsb)
    @reg_touch_pad8_rde.setter
    def reg_touch_pad8_rde(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad8_rde_msb, self.__reg_touch_pad8_rde_lsb, value)

    @property
    def reg_touch_pad8_rue(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad8_rue_msb, self.__reg_touch_pad8_rue_lsb)
    @reg_touch_pad8_rue.setter
    def reg_touch_pad8_rue(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad8_rue_msb, self.__reg_touch_pad8_rue_lsb, value)

    @property
    def reg_touch_pad8_dac(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad8_dac_msb, self.__reg_touch_pad8_dac_lsb)
    @reg_touch_pad8_dac.setter
    def reg_touch_pad8_dac(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad8_dac_msb, self.__reg_touch_pad8_dac_lsb, value)

    @property
    def reg_touch_pad8_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad8_start_msb, self.__reg_touch_pad8_start_lsb)
    @reg_touch_pad8_start.setter
    def reg_touch_pad8_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad8_start_msb, self.__reg_touch_pad8_start_lsb, value)

    @property
    def reg_touch_pad8_tie_opt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad8_tie_opt_msb, self.__reg_touch_pad8_tie_opt_lsb)
    @reg_touch_pad8_tie_opt.setter
    def reg_touch_pad8_tie_opt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad8_tie_opt_msb, self.__reg_touch_pad8_tie_opt_lsb, value)

    @property
    def reg_touch_pad8_xpd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad8_xpd_msb, self.__reg_touch_pad8_xpd_lsb)
    @reg_touch_pad8_xpd.setter
    def reg_touch_pad8_xpd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad8_xpd_msb, self.__reg_touch_pad8_xpd_lsb, value)

    @property
    def reg_touch_pad8_mux_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad8_mux_sel_msb, self.__reg_touch_pad8_mux_sel_lsb)
    @reg_touch_pad8_mux_sel.setter
    def reg_touch_pad8_mux_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad8_mux_sel_msb, self.__reg_touch_pad8_mux_sel_lsb, value)

    @property
    def reg_touch_pad8_fun_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad8_fun_sel_msb, self.__reg_touch_pad8_fun_sel_lsb)
    @reg_touch_pad8_fun_sel.setter
    def reg_touch_pad8_fun_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad8_fun_sel_msb, self.__reg_touch_pad8_fun_sel_lsb, value)

    @property
    def reg_touch_pad8_slp_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad8_slp_sel_msb, self.__reg_touch_pad8_slp_sel_lsb)
    @reg_touch_pad8_slp_sel.setter
    def reg_touch_pad8_slp_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad8_slp_sel_msb, self.__reg_touch_pad8_slp_sel_lsb, value)

    @property
    def reg_touch_pad8_slp_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad8_slp_ie_msb, self.__reg_touch_pad8_slp_ie_lsb)
    @reg_touch_pad8_slp_ie.setter
    def reg_touch_pad8_slp_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad8_slp_ie_msb, self.__reg_touch_pad8_slp_ie_lsb, value)

    @property
    def reg_touch_pad8_slp_oe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad8_slp_oe_msb, self.__reg_touch_pad8_slp_oe_lsb)
    @reg_touch_pad8_slp_oe.setter
    def reg_touch_pad8_slp_oe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad8_slp_oe_msb, self.__reg_touch_pad8_slp_oe_lsb, value)

    @property
    def reg_touch_pad8_fun_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad8_fun_ie_msb, self.__reg_touch_pad8_fun_ie_lsb)
    @reg_touch_pad8_fun_ie.setter
    def reg_touch_pad8_fun_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad8_fun_ie_msb, self.__reg_touch_pad8_fun_ie_lsb, value)
class TOUCH_PAD9(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0xa8
        self.__reg_touch_pad9_drv_lsb = 29
        self.__reg_touch_pad9_drv_msb = 30
        self.__reg_touch_pad9_rde_lsb = 28
        self.__reg_touch_pad9_rde_msb = 28
        self.__reg_touch_pad9_rue_lsb = 27
        self.__reg_touch_pad9_rue_msb = 27
        self.__reg_touch_pad9_dac_lsb = 23
        self.__reg_touch_pad9_dac_msb = 25
        self.__reg_touch_pad9_start_lsb = 22
        self.__reg_touch_pad9_start_msb = 22
        self.__reg_touch_pad9_tie_opt_lsb = 21
        self.__reg_touch_pad9_tie_opt_msb = 21
        self.__reg_touch_pad9_xpd_lsb = 20
        self.__reg_touch_pad9_xpd_msb = 20
        self.__reg_touch_pad9_mux_sel_lsb = 19
        self.__reg_touch_pad9_mux_sel_msb = 19
        self.__reg_touch_pad9_fun_sel_lsb = 17
        self.__reg_touch_pad9_fun_sel_msb = 18
        self.__reg_touch_pad9_slp_sel_lsb = 16
        self.__reg_touch_pad9_slp_sel_msb = 16
        self.__reg_touch_pad9_slp_ie_lsb = 15
        self.__reg_touch_pad9_slp_ie_msb = 15
        self.__reg_touch_pad9_slp_oe_lsb = 14
        self.__reg_touch_pad9_slp_oe_msb = 14
        self.__reg_touch_pad9_fun_ie_lsb = 13
        self.__reg_touch_pad9_fun_ie_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_pad9_drv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad9_drv_msb, self.__reg_touch_pad9_drv_lsb)
    @reg_touch_pad9_drv.setter
    def reg_touch_pad9_drv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad9_drv_msb, self.__reg_touch_pad9_drv_lsb, value)

    @property
    def reg_touch_pad9_rde(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad9_rde_msb, self.__reg_touch_pad9_rde_lsb)
    @reg_touch_pad9_rde.setter
    def reg_touch_pad9_rde(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad9_rde_msb, self.__reg_touch_pad9_rde_lsb, value)

    @property
    def reg_touch_pad9_rue(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad9_rue_msb, self.__reg_touch_pad9_rue_lsb)
    @reg_touch_pad9_rue.setter
    def reg_touch_pad9_rue(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad9_rue_msb, self.__reg_touch_pad9_rue_lsb, value)

    @property
    def reg_touch_pad9_dac(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad9_dac_msb, self.__reg_touch_pad9_dac_lsb)
    @reg_touch_pad9_dac.setter
    def reg_touch_pad9_dac(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad9_dac_msb, self.__reg_touch_pad9_dac_lsb, value)

    @property
    def reg_touch_pad9_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad9_start_msb, self.__reg_touch_pad9_start_lsb)
    @reg_touch_pad9_start.setter
    def reg_touch_pad9_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad9_start_msb, self.__reg_touch_pad9_start_lsb, value)

    @property
    def reg_touch_pad9_tie_opt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad9_tie_opt_msb, self.__reg_touch_pad9_tie_opt_lsb)
    @reg_touch_pad9_tie_opt.setter
    def reg_touch_pad9_tie_opt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad9_tie_opt_msb, self.__reg_touch_pad9_tie_opt_lsb, value)

    @property
    def reg_touch_pad9_xpd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad9_xpd_msb, self.__reg_touch_pad9_xpd_lsb)
    @reg_touch_pad9_xpd.setter
    def reg_touch_pad9_xpd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad9_xpd_msb, self.__reg_touch_pad9_xpd_lsb, value)

    @property
    def reg_touch_pad9_mux_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad9_mux_sel_msb, self.__reg_touch_pad9_mux_sel_lsb)
    @reg_touch_pad9_mux_sel.setter
    def reg_touch_pad9_mux_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad9_mux_sel_msb, self.__reg_touch_pad9_mux_sel_lsb, value)

    @property
    def reg_touch_pad9_fun_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad9_fun_sel_msb, self.__reg_touch_pad9_fun_sel_lsb)
    @reg_touch_pad9_fun_sel.setter
    def reg_touch_pad9_fun_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad9_fun_sel_msb, self.__reg_touch_pad9_fun_sel_lsb, value)

    @property
    def reg_touch_pad9_slp_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad9_slp_sel_msb, self.__reg_touch_pad9_slp_sel_lsb)
    @reg_touch_pad9_slp_sel.setter
    def reg_touch_pad9_slp_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad9_slp_sel_msb, self.__reg_touch_pad9_slp_sel_lsb, value)

    @property
    def reg_touch_pad9_slp_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad9_slp_ie_msb, self.__reg_touch_pad9_slp_ie_lsb)
    @reg_touch_pad9_slp_ie.setter
    def reg_touch_pad9_slp_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad9_slp_ie_msb, self.__reg_touch_pad9_slp_ie_lsb, value)

    @property
    def reg_touch_pad9_slp_oe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad9_slp_oe_msb, self.__reg_touch_pad9_slp_oe_lsb)
    @reg_touch_pad9_slp_oe.setter
    def reg_touch_pad9_slp_oe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad9_slp_oe_msb, self.__reg_touch_pad9_slp_oe_lsb, value)

    @property
    def reg_touch_pad9_fun_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad9_fun_ie_msb, self.__reg_touch_pad9_fun_ie_lsb)
    @reg_touch_pad9_fun_ie.setter
    def reg_touch_pad9_fun_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad9_fun_ie_msb, self.__reg_touch_pad9_fun_ie_lsb, value)
class TOUCH_PAD10(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0xac
        self.__reg_touch_pad10_drv_lsb = 29
        self.__reg_touch_pad10_drv_msb = 30
        self.__reg_touch_pad10_rde_lsb = 28
        self.__reg_touch_pad10_rde_msb = 28
        self.__reg_touch_pad10_rue_lsb = 27
        self.__reg_touch_pad10_rue_msb = 27
        self.__reg_touch_pad10_dac_lsb = 23
        self.__reg_touch_pad10_dac_msb = 25
        self.__reg_touch_pad10_start_lsb = 22
        self.__reg_touch_pad10_start_msb = 22
        self.__reg_touch_pad10_tie_opt_lsb = 21
        self.__reg_touch_pad10_tie_opt_msb = 21
        self.__reg_touch_pad10_xpd_lsb = 20
        self.__reg_touch_pad10_xpd_msb = 20
        self.__reg_touch_pad10_mux_sel_lsb = 19
        self.__reg_touch_pad10_mux_sel_msb = 19
        self.__reg_touch_pad10_fun_sel_lsb = 17
        self.__reg_touch_pad10_fun_sel_msb = 18
        self.__reg_touch_pad10_slp_sel_lsb = 16
        self.__reg_touch_pad10_slp_sel_msb = 16
        self.__reg_touch_pad10_slp_ie_lsb = 15
        self.__reg_touch_pad10_slp_ie_msb = 15
        self.__reg_touch_pad10_slp_oe_lsb = 14
        self.__reg_touch_pad10_slp_oe_msb = 14
        self.__reg_touch_pad10_fun_ie_lsb = 13
        self.__reg_touch_pad10_fun_ie_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_pad10_drv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad10_drv_msb, self.__reg_touch_pad10_drv_lsb)
    @reg_touch_pad10_drv.setter
    def reg_touch_pad10_drv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad10_drv_msb, self.__reg_touch_pad10_drv_lsb, value)

    @property
    def reg_touch_pad10_rde(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad10_rde_msb, self.__reg_touch_pad10_rde_lsb)
    @reg_touch_pad10_rde.setter
    def reg_touch_pad10_rde(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad10_rde_msb, self.__reg_touch_pad10_rde_lsb, value)

    @property
    def reg_touch_pad10_rue(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad10_rue_msb, self.__reg_touch_pad10_rue_lsb)
    @reg_touch_pad10_rue.setter
    def reg_touch_pad10_rue(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad10_rue_msb, self.__reg_touch_pad10_rue_lsb, value)

    @property
    def reg_touch_pad10_dac(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad10_dac_msb, self.__reg_touch_pad10_dac_lsb)
    @reg_touch_pad10_dac.setter
    def reg_touch_pad10_dac(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad10_dac_msb, self.__reg_touch_pad10_dac_lsb, value)

    @property
    def reg_touch_pad10_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad10_start_msb, self.__reg_touch_pad10_start_lsb)
    @reg_touch_pad10_start.setter
    def reg_touch_pad10_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad10_start_msb, self.__reg_touch_pad10_start_lsb, value)

    @property
    def reg_touch_pad10_tie_opt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad10_tie_opt_msb, self.__reg_touch_pad10_tie_opt_lsb)
    @reg_touch_pad10_tie_opt.setter
    def reg_touch_pad10_tie_opt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad10_tie_opt_msb, self.__reg_touch_pad10_tie_opt_lsb, value)

    @property
    def reg_touch_pad10_xpd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad10_xpd_msb, self.__reg_touch_pad10_xpd_lsb)
    @reg_touch_pad10_xpd.setter
    def reg_touch_pad10_xpd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad10_xpd_msb, self.__reg_touch_pad10_xpd_lsb, value)

    @property
    def reg_touch_pad10_mux_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad10_mux_sel_msb, self.__reg_touch_pad10_mux_sel_lsb)
    @reg_touch_pad10_mux_sel.setter
    def reg_touch_pad10_mux_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad10_mux_sel_msb, self.__reg_touch_pad10_mux_sel_lsb, value)

    @property
    def reg_touch_pad10_fun_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad10_fun_sel_msb, self.__reg_touch_pad10_fun_sel_lsb)
    @reg_touch_pad10_fun_sel.setter
    def reg_touch_pad10_fun_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad10_fun_sel_msb, self.__reg_touch_pad10_fun_sel_lsb, value)

    @property
    def reg_touch_pad10_slp_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad10_slp_sel_msb, self.__reg_touch_pad10_slp_sel_lsb)
    @reg_touch_pad10_slp_sel.setter
    def reg_touch_pad10_slp_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad10_slp_sel_msb, self.__reg_touch_pad10_slp_sel_lsb, value)

    @property
    def reg_touch_pad10_slp_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad10_slp_ie_msb, self.__reg_touch_pad10_slp_ie_lsb)
    @reg_touch_pad10_slp_ie.setter
    def reg_touch_pad10_slp_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad10_slp_ie_msb, self.__reg_touch_pad10_slp_ie_lsb, value)

    @property
    def reg_touch_pad10_slp_oe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad10_slp_oe_msb, self.__reg_touch_pad10_slp_oe_lsb)
    @reg_touch_pad10_slp_oe.setter
    def reg_touch_pad10_slp_oe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad10_slp_oe_msb, self.__reg_touch_pad10_slp_oe_lsb, value)

    @property
    def reg_touch_pad10_fun_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad10_fun_ie_msb, self.__reg_touch_pad10_fun_ie_lsb)
    @reg_touch_pad10_fun_ie.setter
    def reg_touch_pad10_fun_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad10_fun_ie_msb, self.__reg_touch_pad10_fun_ie_lsb, value)
class TOUCH_PAD11(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0xb0
        self.__reg_touch_pad11_drv_lsb = 29
        self.__reg_touch_pad11_drv_msb = 30
        self.__reg_touch_pad11_rde_lsb = 28
        self.__reg_touch_pad11_rde_msb = 28
        self.__reg_touch_pad11_rue_lsb = 27
        self.__reg_touch_pad11_rue_msb = 27
        self.__reg_touch_pad11_dac_lsb = 23
        self.__reg_touch_pad11_dac_msb = 25
        self.__reg_touch_pad11_start_lsb = 22
        self.__reg_touch_pad11_start_msb = 22
        self.__reg_touch_pad11_tie_opt_lsb = 21
        self.__reg_touch_pad11_tie_opt_msb = 21
        self.__reg_touch_pad11_xpd_lsb = 20
        self.__reg_touch_pad11_xpd_msb = 20
        self.__reg_touch_pad11_mux_sel_lsb = 19
        self.__reg_touch_pad11_mux_sel_msb = 19
        self.__reg_touch_pad11_fun_sel_lsb = 17
        self.__reg_touch_pad11_fun_sel_msb = 18
        self.__reg_touch_pad11_slp_sel_lsb = 16
        self.__reg_touch_pad11_slp_sel_msb = 16
        self.__reg_touch_pad11_slp_ie_lsb = 15
        self.__reg_touch_pad11_slp_ie_msb = 15
        self.__reg_touch_pad11_slp_oe_lsb = 14
        self.__reg_touch_pad11_slp_oe_msb = 14
        self.__reg_touch_pad11_fun_ie_lsb = 13
        self.__reg_touch_pad11_fun_ie_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_pad11_drv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad11_drv_msb, self.__reg_touch_pad11_drv_lsb)
    @reg_touch_pad11_drv.setter
    def reg_touch_pad11_drv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad11_drv_msb, self.__reg_touch_pad11_drv_lsb, value)

    @property
    def reg_touch_pad11_rde(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad11_rde_msb, self.__reg_touch_pad11_rde_lsb)
    @reg_touch_pad11_rde.setter
    def reg_touch_pad11_rde(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad11_rde_msb, self.__reg_touch_pad11_rde_lsb, value)

    @property
    def reg_touch_pad11_rue(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad11_rue_msb, self.__reg_touch_pad11_rue_lsb)
    @reg_touch_pad11_rue.setter
    def reg_touch_pad11_rue(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad11_rue_msb, self.__reg_touch_pad11_rue_lsb, value)

    @property
    def reg_touch_pad11_dac(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad11_dac_msb, self.__reg_touch_pad11_dac_lsb)
    @reg_touch_pad11_dac.setter
    def reg_touch_pad11_dac(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad11_dac_msb, self.__reg_touch_pad11_dac_lsb, value)

    @property
    def reg_touch_pad11_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad11_start_msb, self.__reg_touch_pad11_start_lsb)
    @reg_touch_pad11_start.setter
    def reg_touch_pad11_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad11_start_msb, self.__reg_touch_pad11_start_lsb, value)

    @property
    def reg_touch_pad11_tie_opt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad11_tie_opt_msb, self.__reg_touch_pad11_tie_opt_lsb)
    @reg_touch_pad11_tie_opt.setter
    def reg_touch_pad11_tie_opt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad11_tie_opt_msb, self.__reg_touch_pad11_tie_opt_lsb, value)

    @property
    def reg_touch_pad11_xpd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad11_xpd_msb, self.__reg_touch_pad11_xpd_lsb)
    @reg_touch_pad11_xpd.setter
    def reg_touch_pad11_xpd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad11_xpd_msb, self.__reg_touch_pad11_xpd_lsb, value)

    @property
    def reg_touch_pad11_mux_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad11_mux_sel_msb, self.__reg_touch_pad11_mux_sel_lsb)
    @reg_touch_pad11_mux_sel.setter
    def reg_touch_pad11_mux_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad11_mux_sel_msb, self.__reg_touch_pad11_mux_sel_lsb, value)

    @property
    def reg_touch_pad11_fun_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad11_fun_sel_msb, self.__reg_touch_pad11_fun_sel_lsb)
    @reg_touch_pad11_fun_sel.setter
    def reg_touch_pad11_fun_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad11_fun_sel_msb, self.__reg_touch_pad11_fun_sel_lsb, value)

    @property
    def reg_touch_pad11_slp_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad11_slp_sel_msb, self.__reg_touch_pad11_slp_sel_lsb)
    @reg_touch_pad11_slp_sel.setter
    def reg_touch_pad11_slp_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad11_slp_sel_msb, self.__reg_touch_pad11_slp_sel_lsb, value)

    @property
    def reg_touch_pad11_slp_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad11_slp_ie_msb, self.__reg_touch_pad11_slp_ie_lsb)
    @reg_touch_pad11_slp_ie.setter
    def reg_touch_pad11_slp_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad11_slp_ie_msb, self.__reg_touch_pad11_slp_ie_lsb, value)

    @property
    def reg_touch_pad11_slp_oe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad11_slp_oe_msb, self.__reg_touch_pad11_slp_oe_lsb)
    @reg_touch_pad11_slp_oe.setter
    def reg_touch_pad11_slp_oe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad11_slp_oe_msb, self.__reg_touch_pad11_slp_oe_lsb, value)

    @property
    def reg_touch_pad11_fun_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad11_fun_ie_msb, self.__reg_touch_pad11_fun_ie_lsb)
    @reg_touch_pad11_fun_ie.setter
    def reg_touch_pad11_fun_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad11_fun_ie_msb, self.__reg_touch_pad11_fun_ie_lsb, value)
class TOUCH_PAD12(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0xb4
        self.__reg_touch_pad12_drv_lsb = 29
        self.__reg_touch_pad12_drv_msb = 30
        self.__reg_touch_pad12_rde_lsb = 28
        self.__reg_touch_pad12_rde_msb = 28
        self.__reg_touch_pad12_rue_lsb = 27
        self.__reg_touch_pad12_rue_msb = 27
        self.__reg_touch_pad12_dac_lsb = 23
        self.__reg_touch_pad12_dac_msb = 25
        self.__reg_touch_pad12_start_lsb = 22
        self.__reg_touch_pad12_start_msb = 22
        self.__reg_touch_pad12_tie_opt_lsb = 21
        self.__reg_touch_pad12_tie_opt_msb = 21
        self.__reg_touch_pad12_xpd_lsb = 20
        self.__reg_touch_pad12_xpd_msb = 20
        self.__reg_touch_pad12_mux_sel_lsb = 19
        self.__reg_touch_pad12_mux_sel_msb = 19
        self.__reg_touch_pad12_fun_sel_lsb = 17
        self.__reg_touch_pad12_fun_sel_msb = 18
        self.__reg_touch_pad12_slp_sel_lsb = 16
        self.__reg_touch_pad12_slp_sel_msb = 16
        self.__reg_touch_pad12_slp_ie_lsb = 15
        self.__reg_touch_pad12_slp_ie_msb = 15
        self.__reg_touch_pad12_slp_oe_lsb = 14
        self.__reg_touch_pad12_slp_oe_msb = 14
        self.__reg_touch_pad12_fun_ie_lsb = 13
        self.__reg_touch_pad12_fun_ie_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_pad12_drv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad12_drv_msb, self.__reg_touch_pad12_drv_lsb)
    @reg_touch_pad12_drv.setter
    def reg_touch_pad12_drv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad12_drv_msb, self.__reg_touch_pad12_drv_lsb, value)

    @property
    def reg_touch_pad12_rde(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad12_rde_msb, self.__reg_touch_pad12_rde_lsb)
    @reg_touch_pad12_rde.setter
    def reg_touch_pad12_rde(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad12_rde_msb, self.__reg_touch_pad12_rde_lsb, value)

    @property
    def reg_touch_pad12_rue(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad12_rue_msb, self.__reg_touch_pad12_rue_lsb)
    @reg_touch_pad12_rue.setter
    def reg_touch_pad12_rue(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad12_rue_msb, self.__reg_touch_pad12_rue_lsb, value)

    @property
    def reg_touch_pad12_dac(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad12_dac_msb, self.__reg_touch_pad12_dac_lsb)
    @reg_touch_pad12_dac.setter
    def reg_touch_pad12_dac(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad12_dac_msb, self.__reg_touch_pad12_dac_lsb, value)

    @property
    def reg_touch_pad12_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad12_start_msb, self.__reg_touch_pad12_start_lsb)
    @reg_touch_pad12_start.setter
    def reg_touch_pad12_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad12_start_msb, self.__reg_touch_pad12_start_lsb, value)

    @property
    def reg_touch_pad12_tie_opt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad12_tie_opt_msb, self.__reg_touch_pad12_tie_opt_lsb)
    @reg_touch_pad12_tie_opt.setter
    def reg_touch_pad12_tie_opt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad12_tie_opt_msb, self.__reg_touch_pad12_tie_opt_lsb, value)

    @property
    def reg_touch_pad12_xpd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad12_xpd_msb, self.__reg_touch_pad12_xpd_lsb)
    @reg_touch_pad12_xpd.setter
    def reg_touch_pad12_xpd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad12_xpd_msb, self.__reg_touch_pad12_xpd_lsb, value)

    @property
    def reg_touch_pad12_mux_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad12_mux_sel_msb, self.__reg_touch_pad12_mux_sel_lsb)
    @reg_touch_pad12_mux_sel.setter
    def reg_touch_pad12_mux_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad12_mux_sel_msb, self.__reg_touch_pad12_mux_sel_lsb, value)

    @property
    def reg_touch_pad12_fun_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad12_fun_sel_msb, self.__reg_touch_pad12_fun_sel_lsb)
    @reg_touch_pad12_fun_sel.setter
    def reg_touch_pad12_fun_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad12_fun_sel_msb, self.__reg_touch_pad12_fun_sel_lsb, value)

    @property
    def reg_touch_pad12_slp_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad12_slp_sel_msb, self.__reg_touch_pad12_slp_sel_lsb)
    @reg_touch_pad12_slp_sel.setter
    def reg_touch_pad12_slp_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad12_slp_sel_msb, self.__reg_touch_pad12_slp_sel_lsb, value)

    @property
    def reg_touch_pad12_slp_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad12_slp_ie_msb, self.__reg_touch_pad12_slp_ie_lsb)
    @reg_touch_pad12_slp_ie.setter
    def reg_touch_pad12_slp_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad12_slp_ie_msb, self.__reg_touch_pad12_slp_ie_lsb, value)

    @property
    def reg_touch_pad12_slp_oe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad12_slp_oe_msb, self.__reg_touch_pad12_slp_oe_lsb)
    @reg_touch_pad12_slp_oe.setter
    def reg_touch_pad12_slp_oe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad12_slp_oe_msb, self.__reg_touch_pad12_slp_oe_lsb, value)

    @property
    def reg_touch_pad12_fun_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad12_fun_ie_msb, self.__reg_touch_pad12_fun_ie_lsb)
    @reg_touch_pad12_fun_ie.setter
    def reg_touch_pad12_fun_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad12_fun_ie_msb, self.__reg_touch_pad12_fun_ie_lsb, value)
class TOUCH_PAD13(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0xb8
        self.__reg_touch_pad13_drv_lsb = 29
        self.__reg_touch_pad13_drv_msb = 30
        self.__reg_touch_pad13_rde_lsb = 28
        self.__reg_touch_pad13_rde_msb = 28
        self.__reg_touch_pad13_rue_lsb = 27
        self.__reg_touch_pad13_rue_msb = 27
        self.__reg_touch_pad13_dac_lsb = 23
        self.__reg_touch_pad13_dac_msb = 25
        self.__reg_touch_pad13_start_lsb = 22
        self.__reg_touch_pad13_start_msb = 22
        self.__reg_touch_pad13_tie_opt_lsb = 21
        self.__reg_touch_pad13_tie_opt_msb = 21
        self.__reg_touch_pad13_xpd_lsb = 20
        self.__reg_touch_pad13_xpd_msb = 20
        self.__reg_touch_pad13_mux_sel_lsb = 19
        self.__reg_touch_pad13_mux_sel_msb = 19
        self.__reg_touch_pad13_fun_sel_lsb = 17
        self.__reg_touch_pad13_fun_sel_msb = 18
        self.__reg_touch_pad13_slp_sel_lsb = 16
        self.__reg_touch_pad13_slp_sel_msb = 16
        self.__reg_touch_pad13_slp_ie_lsb = 15
        self.__reg_touch_pad13_slp_ie_msb = 15
        self.__reg_touch_pad13_slp_oe_lsb = 14
        self.__reg_touch_pad13_slp_oe_msb = 14
        self.__reg_touch_pad13_fun_ie_lsb = 13
        self.__reg_touch_pad13_fun_ie_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_pad13_drv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad13_drv_msb, self.__reg_touch_pad13_drv_lsb)
    @reg_touch_pad13_drv.setter
    def reg_touch_pad13_drv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad13_drv_msb, self.__reg_touch_pad13_drv_lsb, value)

    @property
    def reg_touch_pad13_rde(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad13_rde_msb, self.__reg_touch_pad13_rde_lsb)
    @reg_touch_pad13_rde.setter
    def reg_touch_pad13_rde(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad13_rde_msb, self.__reg_touch_pad13_rde_lsb, value)

    @property
    def reg_touch_pad13_rue(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad13_rue_msb, self.__reg_touch_pad13_rue_lsb)
    @reg_touch_pad13_rue.setter
    def reg_touch_pad13_rue(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad13_rue_msb, self.__reg_touch_pad13_rue_lsb, value)

    @property
    def reg_touch_pad13_dac(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad13_dac_msb, self.__reg_touch_pad13_dac_lsb)
    @reg_touch_pad13_dac.setter
    def reg_touch_pad13_dac(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad13_dac_msb, self.__reg_touch_pad13_dac_lsb, value)

    @property
    def reg_touch_pad13_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad13_start_msb, self.__reg_touch_pad13_start_lsb)
    @reg_touch_pad13_start.setter
    def reg_touch_pad13_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad13_start_msb, self.__reg_touch_pad13_start_lsb, value)

    @property
    def reg_touch_pad13_tie_opt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad13_tie_opt_msb, self.__reg_touch_pad13_tie_opt_lsb)
    @reg_touch_pad13_tie_opt.setter
    def reg_touch_pad13_tie_opt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad13_tie_opt_msb, self.__reg_touch_pad13_tie_opt_lsb, value)

    @property
    def reg_touch_pad13_xpd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad13_xpd_msb, self.__reg_touch_pad13_xpd_lsb)
    @reg_touch_pad13_xpd.setter
    def reg_touch_pad13_xpd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad13_xpd_msb, self.__reg_touch_pad13_xpd_lsb, value)

    @property
    def reg_touch_pad13_mux_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad13_mux_sel_msb, self.__reg_touch_pad13_mux_sel_lsb)
    @reg_touch_pad13_mux_sel.setter
    def reg_touch_pad13_mux_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad13_mux_sel_msb, self.__reg_touch_pad13_mux_sel_lsb, value)

    @property
    def reg_touch_pad13_fun_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad13_fun_sel_msb, self.__reg_touch_pad13_fun_sel_lsb)
    @reg_touch_pad13_fun_sel.setter
    def reg_touch_pad13_fun_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad13_fun_sel_msb, self.__reg_touch_pad13_fun_sel_lsb, value)

    @property
    def reg_touch_pad13_slp_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad13_slp_sel_msb, self.__reg_touch_pad13_slp_sel_lsb)
    @reg_touch_pad13_slp_sel.setter
    def reg_touch_pad13_slp_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad13_slp_sel_msb, self.__reg_touch_pad13_slp_sel_lsb, value)

    @property
    def reg_touch_pad13_slp_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad13_slp_ie_msb, self.__reg_touch_pad13_slp_ie_lsb)
    @reg_touch_pad13_slp_ie.setter
    def reg_touch_pad13_slp_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad13_slp_ie_msb, self.__reg_touch_pad13_slp_ie_lsb, value)

    @property
    def reg_touch_pad13_slp_oe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad13_slp_oe_msb, self.__reg_touch_pad13_slp_oe_lsb)
    @reg_touch_pad13_slp_oe.setter
    def reg_touch_pad13_slp_oe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad13_slp_oe_msb, self.__reg_touch_pad13_slp_oe_lsb, value)

    @property
    def reg_touch_pad13_fun_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad13_fun_ie_msb, self.__reg_touch_pad13_fun_ie_lsb)
    @reg_touch_pad13_fun_ie.setter
    def reg_touch_pad13_fun_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad13_fun_ie_msb, self.__reg_touch_pad13_fun_ie_lsb, value)
class TOUCH_PAD14(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0xbc
        self.__reg_touch_pad14_drv_lsb = 29
        self.__reg_touch_pad14_drv_msb = 30
        self.__reg_touch_pad14_rde_lsb = 28
        self.__reg_touch_pad14_rde_msb = 28
        self.__reg_touch_pad14_rue_lsb = 27
        self.__reg_touch_pad14_rue_msb = 27
        self.__reg_touch_pad14_dac_lsb = 23
        self.__reg_touch_pad14_dac_msb = 25
        self.__reg_touch_pad14_start_lsb = 22
        self.__reg_touch_pad14_start_msb = 22
        self.__reg_touch_pad14_tie_opt_lsb = 21
        self.__reg_touch_pad14_tie_opt_msb = 21
        self.__reg_touch_pad14_xpd_lsb = 20
        self.__reg_touch_pad14_xpd_msb = 20
        self.__reg_touch_pad14_mux_sel_lsb = 19
        self.__reg_touch_pad14_mux_sel_msb = 19
        self.__reg_touch_pad14_fun_sel_lsb = 17
        self.__reg_touch_pad14_fun_sel_msb = 18
        self.__reg_touch_pad14_slp_sel_lsb = 16
        self.__reg_touch_pad14_slp_sel_msb = 16
        self.__reg_touch_pad14_slp_ie_lsb = 15
        self.__reg_touch_pad14_slp_ie_msb = 15
        self.__reg_touch_pad14_slp_oe_lsb = 14
        self.__reg_touch_pad14_slp_oe_msb = 14
        self.__reg_touch_pad14_fun_ie_lsb = 13
        self.__reg_touch_pad14_fun_ie_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_pad14_drv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad14_drv_msb, self.__reg_touch_pad14_drv_lsb)
    @reg_touch_pad14_drv.setter
    def reg_touch_pad14_drv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad14_drv_msb, self.__reg_touch_pad14_drv_lsb, value)

    @property
    def reg_touch_pad14_rde(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad14_rde_msb, self.__reg_touch_pad14_rde_lsb)
    @reg_touch_pad14_rde.setter
    def reg_touch_pad14_rde(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad14_rde_msb, self.__reg_touch_pad14_rde_lsb, value)

    @property
    def reg_touch_pad14_rue(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad14_rue_msb, self.__reg_touch_pad14_rue_lsb)
    @reg_touch_pad14_rue.setter
    def reg_touch_pad14_rue(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad14_rue_msb, self.__reg_touch_pad14_rue_lsb, value)

    @property
    def reg_touch_pad14_dac(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad14_dac_msb, self.__reg_touch_pad14_dac_lsb)
    @reg_touch_pad14_dac.setter
    def reg_touch_pad14_dac(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad14_dac_msb, self.__reg_touch_pad14_dac_lsb, value)

    @property
    def reg_touch_pad14_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad14_start_msb, self.__reg_touch_pad14_start_lsb)
    @reg_touch_pad14_start.setter
    def reg_touch_pad14_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad14_start_msb, self.__reg_touch_pad14_start_lsb, value)

    @property
    def reg_touch_pad14_tie_opt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad14_tie_opt_msb, self.__reg_touch_pad14_tie_opt_lsb)
    @reg_touch_pad14_tie_opt.setter
    def reg_touch_pad14_tie_opt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad14_tie_opt_msb, self.__reg_touch_pad14_tie_opt_lsb, value)

    @property
    def reg_touch_pad14_xpd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad14_xpd_msb, self.__reg_touch_pad14_xpd_lsb)
    @reg_touch_pad14_xpd.setter
    def reg_touch_pad14_xpd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad14_xpd_msb, self.__reg_touch_pad14_xpd_lsb, value)

    @property
    def reg_touch_pad14_mux_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad14_mux_sel_msb, self.__reg_touch_pad14_mux_sel_lsb)
    @reg_touch_pad14_mux_sel.setter
    def reg_touch_pad14_mux_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad14_mux_sel_msb, self.__reg_touch_pad14_mux_sel_lsb, value)

    @property
    def reg_touch_pad14_fun_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad14_fun_sel_msb, self.__reg_touch_pad14_fun_sel_lsb)
    @reg_touch_pad14_fun_sel.setter
    def reg_touch_pad14_fun_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad14_fun_sel_msb, self.__reg_touch_pad14_fun_sel_lsb, value)

    @property
    def reg_touch_pad14_slp_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad14_slp_sel_msb, self.__reg_touch_pad14_slp_sel_lsb)
    @reg_touch_pad14_slp_sel.setter
    def reg_touch_pad14_slp_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad14_slp_sel_msb, self.__reg_touch_pad14_slp_sel_lsb, value)

    @property
    def reg_touch_pad14_slp_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad14_slp_ie_msb, self.__reg_touch_pad14_slp_ie_lsb)
    @reg_touch_pad14_slp_ie.setter
    def reg_touch_pad14_slp_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad14_slp_ie_msb, self.__reg_touch_pad14_slp_ie_lsb, value)

    @property
    def reg_touch_pad14_slp_oe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad14_slp_oe_msb, self.__reg_touch_pad14_slp_oe_lsb)
    @reg_touch_pad14_slp_oe.setter
    def reg_touch_pad14_slp_oe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad14_slp_oe_msb, self.__reg_touch_pad14_slp_oe_lsb, value)

    @property
    def reg_touch_pad14_fun_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad14_fun_ie_msb, self.__reg_touch_pad14_fun_ie_lsb)
    @reg_touch_pad14_fun_ie.setter
    def reg_touch_pad14_fun_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad14_fun_ie_msb, self.__reg_touch_pad14_fun_ie_lsb, value)
class XTAL_32P_PAD(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0xc0
        self.__reg_x32p_drv_lsb = 29
        self.__reg_x32p_drv_msb = 30
        self.__reg_x32p_rde_lsb = 28
        self.__reg_x32p_rde_msb = 28
        self.__reg_x32p_rue_lsb = 27
        self.__reg_x32p_rue_msb = 27
        self.__reg_x32p_mux_sel_lsb = 19
        self.__reg_x32p_mux_sel_msb = 19
        self.__reg_x32p_fun_sel_lsb = 17
        self.__reg_x32p_fun_sel_msb = 18
        self.__reg_x32p_slp_sel_lsb = 16
        self.__reg_x32p_slp_sel_msb = 16
        self.__reg_x32p_slp_ie_lsb = 15
        self.__reg_x32p_slp_ie_msb = 15
        self.__reg_x32p_slp_oe_lsb = 14
        self.__reg_x32p_slp_oe_msb = 14
        self.__reg_x32p_fun_ie_lsb = 13
        self.__reg_x32p_fun_ie_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_x32p_drv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_x32p_drv_msb, self.__reg_x32p_drv_lsb)
    @reg_x32p_drv.setter
    def reg_x32p_drv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_x32p_drv_msb, self.__reg_x32p_drv_lsb, value)

    @property
    def reg_x32p_rde(self):
        return self.__MEM.rdm(self.__addr, self.__reg_x32p_rde_msb, self.__reg_x32p_rde_lsb)
    @reg_x32p_rde.setter
    def reg_x32p_rde(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_x32p_rde_msb, self.__reg_x32p_rde_lsb, value)

    @property
    def reg_x32p_rue(self):
        return self.__MEM.rdm(self.__addr, self.__reg_x32p_rue_msb, self.__reg_x32p_rue_lsb)
    @reg_x32p_rue.setter
    def reg_x32p_rue(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_x32p_rue_msb, self.__reg_x32p_rue_lsb, value)

    @property
    def reg_x32p_mux_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_x32p_mux_sel_msb, self.__reg_x32p_mux_sel_lsb)
    @reg_x32p_mux_sel.setter
    def reg_x32p_mux_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_x32p_mux_sel_msb, self.__reg_x32p_mux_sel_lsb, value)

    @property
    def reg_x32p_fun_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_x32p_fun_sel_msb, self.__reg_x32p_fun_sel_lsb)
    @reg_x32p_fun_sel.setter
    def reg_x32p_fun_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_x32p_fun_sel_msb, self.__reg_x32p_fun_sel_lsb, value)

    @property
    def reg_x32p_slp_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_x32p_slp_sel_msb, self.__reg_x32p_slp_sel_lsb)
    @reg_x32p_slp_sel.setter
    def reg_x32p_slp_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_x32p_slp_sel_msb, self.__reg_x32p_slp_sel_lsb, value)

    @property
    def reg_x32p_slp_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_x32p_slp_ie_msb, self.__reg_x32p_slp_ie_lsb)
    @reg_x32p_slp_ie.setter
    def reg_x32p_slp_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_x32p_slp_ie_msb, self.__reg_x32p_slp_ie_lsb, value)

    @property
    def reg_x32p_slp_oe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_x32p_slp_oe_msb, self.__reg_x32p_slp_oe_lsb)
    @reg_x32p_slp_oe.setter
    def reg_x32p_slp_oe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_x32p_slp_oe_msb, self.__reg_x32p_slp_oe_lsb, value)

    @property
    def reg_x32p_fun_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_x32p_fun_ie_msb, self.__reg_x32p_fun_ie_lsb)
    @reg_x32p_fun_ie.setter
    def reg_x32p_fun_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_x32p_fun_ie_msb, self.__reg_x32p_fun_ie_lsb, value)
class XTAL_32N_PAD(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0xc4
        self.__reg_x32n_drv_lsb = 29
        self.__reg_x32n_drv_msb = 30
        self.__reg_x32n_rde_lsb = 28
        self.__reg_x32n_rde_msb = 28
        self.__reg_x32n_rue_lsb = 27
        self.__reg_x32n_rue_msb = 27
        self.__reg_x32n_mux_sel_lsb = 19
        self.__reg_x32n_mux_sel_msb = 19
        self.__reg_x32n_fun_sel_lsb = 17
        self.__reg_x32n_fun_sel_msb = 18
        self.__reg_x32n_slp_sel_lsb = 16
        self.__reg_x32n_slp_sel_msb = 16
        self.__reg_x32n_slp_ie_lsb = 15
        self.__reg_x32n_slp_ie_msb = 15
        self.__reg_x32n_slp_oe_lsb = 14
        self.__reg_x32n_slp_oe_msb = 14
        self.__reg_x32n_fun_ie_lsb = 13
        self.__reg_x32n_fun_ie_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_x32n_drv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_x32n_drv_msb, self.__reg_x32n_drv_lsb)
    @reg_x32n_drv.setter
    def reg_x32n_drv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_x32n_drv_msb, self.__reg_x32n_drv_lsb, value)

    @property
    def reg_x32n_rde(self):
        return self.__MEM.rdm(self.__addr, self.__reg_x32n_rde_msb, self.__reg_x32n_rde_lsb)
    @reg_x32n_rde.setter
    def reg_x32n_rde(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_x32n_rde_msb, self.__reg_x32n_rde_lsb, value)

    @property
    def reg_x32n_rue(self):
        return self.__MEM.rdm(self.__addr, self.__reg_x32n_rue_msb, self.__reg_x32n_rue_lsb)
    @reg_x32n_rue.setter
    def reg_x32n_rue(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_x32n_rue_msb, self.__reg_x32n_rue_lsb, value)

    @property
    def reg_x32n_mux_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_x32n_mux_sel_msb, self.__reg_x32n_mux_sel_lsb)
    @reg_x32n_mux_sel.setter
    def reg_x32n_mux_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_x32n_mux_sel_msb, self.__reg_x32n_mux_sel_lsb, value)

    @property
    def reg_x32n_fun_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_x32n_fun_sel_msb, self.__reg_x32n_fun_sel_lsb)
    @reg_x32n_fun_sel.setter
    def reg_x32n_fun_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_x32n_fun_sel_msb, self.__reg_x32n_fun_sel_lsb, value)

    @property
    def reg_x32n_slp_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_x32n_slp_sel_msb, self.__reg_x32n_slp_sel_lsb)
    @reg_x32n_slp_sel.setter
    def reg_x32n_slp_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_x32n_slp_sel_msb, self.__reg_x32n_slp_sel_lsb, value)

    @property
    def reg_x32n_slp_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_x32n_slp_ie_msb, self.__reg_x32n_slp_ie_lsb)
    @reg_x32n_slp_ie.setter
    def reg_x32n_slp_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_x32n_slp_ie_msb, self.__reg_x32n_slp_ie_lsb, value)

    @property
    def reg_x32n_slp_oe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_x32n_slp_oe_msb, self.__reg_x32n_slp_oe_lsb)
    @reg_x32n_slp_oe.setter
    def reg_x32n_slp_oe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_x32n_slp_oe_msb, self.__reg_x32n_slp_oe_lsb, value)

    @property
    def reg_x32n_fun_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_x32n_fun_ie_msb, self.__reg_x32n_fun_ie_lsb)
    @reg_x32n_fun_ie.setter
    def reg_x32n_fun_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_x32n_fun_ie_msb, self.__reg_x32n_fun_ie_lsb, value)
class PAD_DAC1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0xc8
        self.__reg_pdac1_drv_lsb = 29
        self.__reg_pdac1_drv_msb = 30
        self.__reg_pdac1_rde_lsb = 28
        self.__reg_pdac1_rde_msb = 28
        self.__reg_pdac1_rue_lsb = 27
        self.__reg_pdac1_rue_msb = 27
        self.__reg_pdac1_mux_sel_lsb = 19
        self.__reg_pdac1_mux_sel_msb = 19
        self.__reg_pdac1_fun_sel_lsb = 17
        self.__reg_pdac1_fun_sel_msb = 18
        self.__reg_pdac1_slp_sel_lsb = 16
        self.__reg_pdac1_slp_sel_msb = 16
        self.__reg_pdac1_slp_ie_lsb = 15
        self.__reg_pdac1_slp_ie_msb = 15
        self.__reg_pdac1_slp_oe_lsb = 14
        self.__reg_pdac1_slp_oe_msb = 14
        self.__reg_pdac1_fun_ie_lsb = 13
        self.__reg_pdac1_fun_ie_msb = 13
        self.__reg_pdac1_dac_xpd_force_lsb = 12
        self.__reg_pdac1_dac_xpd_force_msb = 12
        self.__reg_pdac1_xpd_dac_lsb = 11
        self.__reg_pdac1_xpd_dac_msb = 11
        self.__reg_pdac1_dac_lsb = 3
        self.__reg_pdac1_dac_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_pdac1_drv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdac1_drv_msb, self.__reg_pdac1_drv_lsb)
    @reg_pdac1_drv.setter
    def reg_pdac1_drv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdac1_drv_msb, self.__reg_pdac1_drv_lsb, value)

    @property
    def reg_pdac1_rde(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdac1_rde_msb, self.__reg_pdac1_rde_lsb)
    @reg_pdac1_rde.setter
    def reg_pdac1_rde(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdac1_rde_msb, self.__reg_pdac1_rde_lsb, value)

    @property
    def reg_pdac1_rue(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdac1_rue_msb, self.__reg_pdac1_rue_lsb)
    @reg_pdac1_rue.setter
    def reg_pdac1_rue(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdac1_rue_msb, self.__reg_pdac1_rue_lsb, value)

    @property
    def reg_pdac1_mux_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdac1_mux_sel_msb, self.__reg_pdac1_mux_sel_lsb)
    @reg_pdac1_mux_sel.setter
    def reg_pdac1_mux_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdac1_mux_sel_msb, self.__reg_pdac1_mux_sel_lsb, value)

    @property
    def reg_pdac1_fun_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdac1_fun_sel_msb, self.__reg_pdac1_fun_sel_lsb)
    @reg_pdac1_fun_sel.setter
    def reg_pdac1_fun_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdac1_fun_sel_msb, self.__reg_pdac1_fun_sel_lsb, value)

    @property
    def reg_pdac1_slp_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdac1_slp_sel_msb, self.__reg_pdac1_slp_sel_lsb)
    @reg_pdac1_slp_sel.setter
    def reg_pdac1_slp_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdac1_slp_sel_msb, self.__reg_pdac1_slp_sel_lsb, value)

    @property
    def reg_pdac1_slp_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdac1_slp_ie_msb, self.__reg_pdac1_slp_ie_lsb)
    @reg_pdac1_slp_ie.setter
    def reg_pdac1_slp_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdac1_slp_ie_msb, self.__reg_pdac1_slp_ie_lsb, value)

    @property
    def reg_pdac1_slp_oe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdac1_slp_oe_msb, self.__reg_pdac1_slp_oe_lsb)
    @reg_pdac1_slp_oe.setter
    def reg_pdac1_slp_oe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdac1_slp_oe_msb, self.__reg_pdac1_slp_oe_lsb, value)

    @property
    def reg_pdac1_fun_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdac1_fun_ie_msb, self.__reg_pdac1_fun_ie_lsb)
    @reg_pdac1_fun_ie.setter
    def reg_pdac1_fun_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdac1_fun_ie_msb, self.__reg_pdac1_fun_ie_lsb, value)

    @property
    def reg_pdac1_dac_xpd_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdac1_dac_xpd_force_msb, self.__reg_pdac1_dac_xpd_force_lsb)
    @reg_pdac1_dac_xpd_force.setter
    def reg_pdac1_dac_xpd_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdac1_dac_xpd_force_msb, self.__reg_pdac1_dac_xpd_force_lsb, value)

    @property
    def reg_pdac1_xpd_dac(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdac1_xpd_dac_msb, self.__reg_pdac1_xpd_dac_lsb)
    @reg_pdac1_xpd_dac.setter
    def reg_pdac1_xpd_dac(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdac1_xpd_dac_msb, self.__reg_pdac1_xpd_dac_lsb, value)

    @property
    def reg_pdac1_dac(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdac1_dac_msb, self.__reg_pdac1_dac_lsb)
    @reg_pdac1_dac.setter
    def reg_pdac1_dac(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdac1_dac_msb, self.__reg_pdac1_dac_lsb, value)
class PAD_DAC2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0xcc
        self.__reg_pdac2_drv_lsb = 29
        self.__reg_pdac2_drv_msb = 30
        self.__reg_pdac2_rde_lsb = 28
        self.__reg_pdac2_rde_msb = 28
        self.__reg_pdac2_rue_lsb = 27
        self.__reg_pdac2_rue_msb = 27
        self.__reg_pdac2_mux_sel_lsb = 19
        self.__reg_pdac2_mux_sel_msb = 19
        self.__reg_pdac2_fun_sel_lsb = 17
        self.__reg_pdac2_fun_sel_msb = 18
        self.__reg_pdac2_slp_sel_lsb = 16
        self.__reg_pdac2_slp_sel_msb = 16
        self.__reg_pdac2_slp_ie_lsb = 15
        self.__reg_pdac2_slp_ie_msb = 15
        self.__reg_pdac2_slp_oe_lsb = 14
        self.__reg_pdac2_slp_oe_msb = 14
        self.__reg_pdac2_fun_ie_lsb = 13
        self.__reg_pdac2_fun_ie_msb = 13
        self.__reg_pdac2_dac_xpd_force_lsb = 12
        self.__reg_pdac2_dac_xpd_force_msb = 12
        self.__reg_pdac2_xpd_dac_lsb = 11
        self.__reg_pdac2_xpd_dac_msb = 11
        self.__reg_pdac2_dac_lsb = 3
        self.__reg_pdac2_dac_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_pdac2_drv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdac2_drv_msb, self.__reg_pdac2_drv_lsb)
    @reg_pdac2_drv.setter
    def reg_pdac2_drv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdac2_drv_msb, self.__reg_pdac2_drv_lsb, value)

    @property
    def reg_pdac2_rde(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdac2_rde_msb, self.__reg_pdac2_rde_lsb)
    @reg_pdac2_rde.setter
    def reg_pdac2_rde(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdac2_rde_msb, self.__reg_pdac2_rde_lsb, value)

    @property
    def reg_pdac2_rue(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdac2_rue_msb, self.__reg_pdac2_rue_lsb)
    @reg_pdac2_rue.setter
    def reg_pdac2_rue(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdac2_rue_msb, self.__reg_pdac2_rue_lsb, value)

    @property
    def reg_pdac2_mux_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdac2_mux_sel_msb, self.__reg_pdac2_mux_sel_lsb)
    @reg_pdac2_mux_sel.setter
    def reg_pdac2_mux_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdac2_mux_sel_msb, self.__reg_pdac2_mux_sel_lsb, value)

    @property
    def reg_pdac2_fun_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdac2_fun_sel_msb, self.__reg_pdac2_fun_sel_lsb)
    @reg_pdac2_fun_sel.setter
    def reg_pdac2_fun_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdac2_fun_sel_msb, self.__reg_pdac2_fun_sel_lsb, value)

    @property
    def reg_pdac2_slp_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdac2_slp_sel_msb, self.__reg_pdac2_slp_sel_lsb)
    @reg_pdac2_slp_sel.setter
    def reg_pdac2_slp_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdac2_slp_sel_msb, self.__reg_pdac2_slp_sel_lsb, value)

    @property
    def reg_pdac2_slp_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdac2_slp_ie_msb, self.__reg_pdac2_slp_ie_lsb)
    @reg_pdac2_slp_ie.setter
    def reg_pdac2_slp_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdac2_slp_ie_msb, self.__reg_pdac2_slp_ie_lsb, value)

    @property
    def reg_pdac2_slp_oe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdac2_slp_oe_msb, self.__reg_pdac2_slp_oe_lsb)
    @reg_pdac2_slp_oe.setter
    def reg_pdac2_slp_oe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdac2_slp_oe_msb, self.__reg_pdac2_slp_oe_lsb, value)

    @property
    def reg_pdac2_fun_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdac2_fun_ie_msb, self.__reg_pdac2_fun_ie_lsb)
    @reg_pdac2_fun_ie.setter
    def reg_pdac2_fun_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdac2_fun_ie_msb, self.__reg_pdac2_fun_ie_lsb, value)

    @property
    def reg_pdac2_dac_xpd_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdac2_dac_xpd_force_msb, self.__reg_pdac2_dac_xpd_force_lsb)
    @reg_pdac2_dac_xpd_force.setter
    def reg_pdac2_dac_xpd_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdac2_dac_xpd_force_msb, self.__reg_pdac2_dac_xpd_force_lsb, value)

    @property
    def reg_pdac2_xpd_dac(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdac2_xpd_dac_msb, self.__reg_pdac2_xpd_dac_lsb)
    @reg_pdac2_xpd_dac.setter
    def reg_pdac2_xpd_dac(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdac2_xpd_dac_msb, self.__reg_pdac2_xpd_dac_lsb, value)

    @property
    def reg_pdac2_dac(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdac2_dac_msb, self.__reg_pdac2_dac_lsb)
    @reg_pdac2_dac.setter
    def reg_pdac2_dac(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdac2_dac_msb, self.__reg_pdac2_dac_lsb, value)
class RTC_PAD19(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0xd0
        self.__reg_rtc_pad19_drv_lsb = 29
        self.__reg_rtc_pad19_drv_msb = 30
        self.__reg_rtc_pad19_rde_lsb = 28
        self.__reg_rtc_pad19_rde_msb = 28
        self.__reg_rtc_pad19_rue_lsb = 27
        self.__reg_rtc_pad19_rue_msb = 27
        self.__reg_rtc_pad19_mux_sel_lsb = 19
        self.__reg_rtc_pad19_mux_sel_msb = 19
        self.__reg_rtc_pad19_fun_sel_lsb = 17
        self.__reg_rtc_pad19_fun_sel_msb = 18
        self.__reg_rtc_pad19_slp_sel_lsb = 16
        self.__reg_rtc_pad19_slp_sel_msb = 16
        self.__reg_rtc_pad19_slp_ie_lsb = 15
        self.__reg_rtc_pad19_slp_ie_msb = 15
        self.__reg_rtc_pad19_slp_oe_lsb = 14
        self.__reg_rtc_pad19_slp_oe_msb = 14
        self.__reg_rtc_pad19_fun_ie_lsb = 13
        self.__reg_rtc_pad19_fun_ie_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rtc_pad19_drv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad19_drv_msb, self.__reg_rtc_pad19_drv_lsb)
    @reg_rtc_pad19_drv.setter
    def reg_rtc_pad19_drv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad19_drv_msb, self.__reg_rtc_pad19_drv_lsb, value)

    @property
    def reg_rtc_pad19_rde(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad19_rde_msb, self.__reg_rtc_pad19_rde_lsb)
    @reg_rtc_pad19_rde.setter
    def reg_rtc_pad19_rde(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad19_rde_msb, self.__reg_rtc_pad19_rde_lsb, value)

    @property
    def reg_rtc_pad19_rue(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad19_rue_msb, self.__reg_rtc_pad19_rue_lsb)
    @reg_rtc_pad19_rue.setter
    def reg_rtc_pad19_rue(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad19_rue_msb, self.__reg_rtc_pad19_rue_lsb, value)

    @property
    def reg_rtc_pad19_mux_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad19_mux_sel_msb, self.__reg_rtc_pad19_mux_sel_lsb)
    @reg_rtc_pad19_mux_sel.setter
    def reg_rtc_pad19_mux_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad19_mux_sel_msb, self.__reg_rtc_pad19_mux_sel_lsb, value)

    @property
    def reg_rtc_pad19_fun_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad19_fun_sel_msb, self.__reg_rtc_pad19_fun_sel_lsb)
    @reg_rtc_pad19_fun_sel.setter
    def reg_rtc_pad19_fun_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad19_fun_sel_msb, self.__reg_rtc_pad19_fun_sel_lsb, value)

    @property
    def reg_rtc_pad19_slp_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad19_slp_sel_msb, self.__reg_rtc_pad19_slp_sel_lsb)
    @reg_rtc_pad19_slp_sel.setter
    def reg_rtc_pad19_slp_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad19_slp_sel_msb, self.__reg_rtc_pad19_slp_sel_lsb, value)

    @property
    def reg_rtc_pad19_slp_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad19_slp_ie_msb, self.__reg_rtc_pad19_slp_ie_lsb)
    @reg_rtc_pad19_slp_ie.setter
    def reg_rtc_pad19_slp_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad19_slp_ie_msb, self.__reg_rtc_pad19_slp_ie_lsb, value)

    @property
    def reg_rtc_pad19_slp_oe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad19_slp_oe_msb, self.__reg_rtc_pad19_slp_oe_lsb)
    @reg_rtc_pad19_slp_oe.setter
    def reg_rtc_pad19_slp_oe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad19_slp_oe_msb, self.__reg_rtc_pad19_slp_oe_lsb, value)

    @property
    def reg_rtc_pad19_fun_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad19_fun_ie_msb, self.__reg_rtc_pad19_fun_ie_lsb)
    @reg_rtc_pad19_fun_ie.setter
    def reg_rtc_pad19_fun_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad19_fun_ie_msb, self.__reg_rtc_pad19_fun_ie_lsb, value)
class RTC_PAD20(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0xd4
        self.__reg_rtc_pad20_drv_lsb = 29
        self.__reg_rtc_pad20_drv_msb = 30
        self.__reg_rtc_pad20_rde_lsb = 28
        self.__reg_rtc_pad20_rde_msb = 28
        self.__reg_rtc_pad20_rue_lsb = 27
        self.__reg_rtc_pad20_rue_msb = 27
        self.__reg_rtc_pad20_mux_sel_lsb = 19
        self.__reg_rtc_pad20_mux_sel_msb = 19
        self.__reg_rtc_pad20_fun_sel_lsb = 17
        self.__reg_rtc_pad20_fun_sel_msb = 18
        self.__reg_rtc_pad20_slp_sel_lsb = 16
        self.__reg_rtc_pad20_slp_sel_msb = 16
        self.__reg_rtc_pad20_slp_ie_lsb = 15
        self.__reg_rtc_pad20_slp_ie_msb = 15
        self.__reg_rtc_pad20_slp_oe_lsb = 14
        self.__reg_rtc_pad20_slp_oe_msb = 14
        self.__reg_rtc_pad20_fun_ie_lsb = 13
        self.__reg_rtc_pad20_fun_ie_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rtc_pad20_drv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad20_drv_msb, self.__reg_rtc_pad20_drv_lsb)
    @reg_rtc_pad20_drv.setter
    def reg_rtc_pad20_drv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad20_drv_msb, self.__reg_rtc_pad20_drv_lsb, value)

    @property
    def reg_rtc_pad20_rde(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad20_rde_msb, self.__reg_rtc_pad20_rde_lsb)
    @reg_rtc_pad20_rde.setter
    def reg_rtc_pad20_rde(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad20_rde_msb, self.__reg_rtc_pad20_rde_lsb, value)

    @property
    def reg_rtc_pad20_rue(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad20_rue_msb, self.__reg_rtc_pad20_rue_lsb)
    @reg_rtc_pad20_rue.setter
    def reg_rtc_pad20_rue(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad20_rue_msb, self.__reg_rtc_pad20_rue_lsb, value)

    @property
    def reg_rtc_pad20_mux_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad20_mux_sel_msb, self.__reg_rtc_pad20_mux_sel_lsb)
    @reg_rtc_pad20_mux_sel.setter
    def reg_rtc_pad20_mux_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad20_mux_sel_msb, self.__reg_rtc_pad20_mux_sel_lsb, value)

    @property
    def reg_rtc_pad20_fun_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad20_fun_sel_msb, self.__reg_rtc_pad20_fun_sel_lsb)
    @reg_rtc_pad20_fun_sel.setter
    def reg_rtc_pad20_fun_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad20_fun_sel_msb, self.__reg_rtc_pad20_fun_sel_lsb, value)

    @property
    def reg_rtc_pad20_slp_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad20_slp_sel_msb, self.__reg_rtc_pad20_slp_sel_lsb)
    @reg_rtc_pad20_slp_sel.setter
    def reg_rtc_pad20_slp_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad20_slp_sel_msb, self.__reg_rtc_pad20_slp_sel_lsb, value)

    @property
    def reg_rtc_pad20_slp_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad20_slp_ie_msb, self.__reg_rtc_pad20_slp_ie_lsb)
    @reg_rtc_pad20_slp_ie.setter
    def reg_rtc_pad20_slp_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad20_slp_ie_msb, self.__reg_rtc_pad20_slp_ie_lsb, value)

    @property
    def reg_rtc_pad20_slp_oe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad20_slp_oe_msb, self.__reg_rtc_pad20_slp_oe_lsb)
    @reg_rtc_pad20_slp_oe.setter
    def reg_rtc_pad20_slp_oe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad20_slp_oe_msb, self.__reg_rtc_pad20_slp_oe_lsb, value)

    @property
    def reg_rtc_pad20_fun_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad20_fun_ie_msb, self.__reg_rtc_pad20_fun_ie_lsb)
    @reg_rtc_pad20_fun_ie.setter
    def reg_rtc_pad20_fun_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad20_fun_ie_msb, self.__reg_rtc_pad20_fun_ie_lsb, value)
class RTC_PAD21(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0xd8
        self.__reg_rtc_pad21_drv_lsb = 29
        self.__reg_rtc_pad21_drv_msb = 30
        self.__reg_rtc_pad21_rde_lsb = 28
        self.__reg_rtc_pad21_rde_msb = 28
        self.__reg_rtc_pad21_rue_lsb = 27
        self.__reg_rtc_pad21_rue_msb = 27
        self.__reg_rtc_pad21_mux_sel_lsb = 19
        self.__reg_rtc_pad21_mux_sel_msb = 19
        self.__reg_rtc_pad21_fun_sel_lsb = 17
        self.__reg_rtc_pad21_fun_sel_msb = 18
        self.__reg_rtc_pad21_slp_sel_lsb = 16
        self.__reg_rtc_pad21_slp_sel_msb = 16
        self.__reg_rtc_pad21_slp_ie_lsb = 15
        self.__reg_rtc_pad21_slp_ie_msb = 15
        self.__reg_rtc_pad21_slp_oe_lsb = 14
        self.__reg_rtc_pad21_slp_oe_msb = 14
        self.__reg_rtc_pad21_fun_ie_lsb = 13
        self.__reg_rtc_pad21_fun_ie_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rtc_pad21_drv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad21_drv_msb, self.__reg_rtc_pad21_drv_lsb)
    @reg_rtc_pad21_drv.setter
    def reg_rtc_pad21_drv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad21_drv_msb, self.__reg_rtc_pad21_drv_lsb, value)

    @property
    def reg_rtc_pad21_rde(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad21_rde_msb, self.__reg_rtc_pad21_rde_lsb)
    @reg_rtc_pad21_rde.setter
    def reg_rtc_pad21_rde(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad21_rde_msb, self.__reg_rtc_pad21_rde_lsb, value)

    @property
    def reg_rtc_pad21_rue(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad21_rue_msb, self.__reg_rtc_pad21_rue_lsb)
    @reg_rtc_pad21_rue.setter
    def reg_rtc_pad21_rue(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad21_rue_msb, self.__reg_rtc_pad21_rue_lsb, value)

    @property
    def reg_rtc_pad21_mux_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad21_mux_sel_msb, self.__reg_rtc_pad21_mux_sel_lsb)
    @reg_rtc_pad21_mux_sel.setter
    def reg_rtc_pad21_mux_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad21_mux_sel_msb, self.__reg_rtc_pad21_mux_sel_lsb, value)

    @property
    def reg_rtc_pad21_fun_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad21_fun_sel_msb, self.__reg_rtc_pad21_fun_sel_lsb)
    @reg_rtc_pad21_fun_sel.setter
    def reg_rtc_pad21_fun_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad21_fun_sel_msb, self.__reg_rtc_pad21_fun_sel_lsb, value)

    @property
    def reg_rtc_pad21_slp_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad21_slp_sel_msb, self.__reg_rtc_pad21_slp_sel_lsb)
    @reg_rtc_pad21_slp_sel.setter
    def reg_rtc_pad21_slp_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad21_slp_sel_msb, self.__reg_rtc_pad21_slp_sel_lsb, value)

    @property
    def reg_rtc_pad21_slp_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad21_slp_ie_msb, self.__reg_rtc_pad21_slp_ie_lsb)
    @reg_rtc_pad21_slp_ie.setter
    def reg_rtc_pad21_slp_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad21_slp_ie_msb, self.__reg_rtc_pad21_slp_ie_lsb, value)

    @property
    def reg_rtc_pad21_slp_oe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad21_slp_oe_msb, self.__reg_rtc_pad21_slp_oe_lsb)
    @reg_rtc_pad21_slp_oe.setter
    def reg_rtc_pad21_slp_oe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad21_slp_oe_msb, self.__reg_rtc_pad21_slp_oe_lsb, value)

    @property
    def reg_rtc_pad21_fun_ie(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pad21_fun_ie_msb, self.__reg_rtc_pad21_fun_ie_lsb)
    @reg_rtc_pad21_fun_ie.setter
    def reg_rtc_pad21_fun_ie(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pad21_fun_ie_msb, self.__reg_rtc_pad21_fun_ie_lsb, value)
class EXT_WAKEUP0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0xdc
        self.__reg_ext_wakeup0_sel_lsb = 27
        self.__reg_ext_wakeup0_sel_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ext_wakeup0_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ext_wakeup0_sel_msb, self.__reg_ext_wakeup0_sel_lsb)
    @reg_ext_wakeup0_sel.setter
    def reg_ext_wakeup0_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ext_wakeup0_sel_msb, self.__reg_ext_wakeup0_sel_lsb, value)
class XTL_EXT_CTR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0xe0
        self.__reg_xtl_ext_ctr_sel_lsb = 27
        self.__reg_xtl_ext_ctr_sel_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_xtl_ext_ctr_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xtl_ext_ctr_sel_msb, self.__reg_xtl_ext_ctr_sel_lsb)
    @reg_xtl_ext_ctr_sel.setter
    def reg_xtl_ext_ctr_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xtl_ext_ctr_sel_msb, self.__reg_xtl_ext_ctr_sel_lsb, value)
class SAR_I2C_IO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0xe4
        self.__reg_sar_i2c_sda_sel_lsb = 30
        self.__reg_sar_i2c_sda_sel_msb = 31
        self.__reg_sar_i2c_scl_sel_lsb = 28
        self.__reg_sar_i2c_scl_sel_msb = 29
        self.__reg_sar_debug_bit_sel_lsb = 23
        self.__reg_sar_debug_bit_sel_msb = 27
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sar_i2c_sda_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar_i2c_sda_sel_msb, self.__reg_sar_i2c_sda_sel_lsb)
    @reg_sar_i2c_sda_sel.setter
    def reg_sar_i2c_sda_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar_i2c_sda_sel_msb, self.__reg_sar_i2c_sda_sel_lsb, value)

    @property
    def reg_sar_i2c_scl_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar_i2c_scl_sel_msb, self.__reg_sar_i2c_scl_sel_lsb)
    @reg_sar_i2c_scl_sel.setter
    def reg_sar_i2c_scl_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar_i2c_scl_sel_msb, self.__reg_sar_i2c_scl_sel_lsb, value)

    @property
    def reg_sar_debug_bit_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar_debug_bit_sel_msb, self.__reg_sar_debug_bit_sel_lsb)
    @reg_sar_debug_bit_sel.setter
    def reg_sar_debug_bit_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar_debug_bit_sel_msb, self.__reg_sar_debug_bit_sel_lsb, value)
class RTC_IO_DATE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_IO_BASE + 0x1fc
        self.__rtc_io_date_lsb = 0
        self.__rtc_io_date_msb = 27
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_io_date(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_io_date_msb, self.__rtc_io_date_lsb)
    @rtc_io_date.setter
    def rtc_io_date(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_io_date_msb, self.__rtc_io_date_lsb, value)
    @property
    def default_value(self):
        return 0x1808030
