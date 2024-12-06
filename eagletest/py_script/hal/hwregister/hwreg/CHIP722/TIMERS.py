from hal.common import *
from hal.hwregister.hwreg.CHIP722.addr_base import *
class TIMERS(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.T0CONFIG = T0CONFIG(self.channel, self.chipv)
        self.T0LO = T0LO(self.channel, self.chipv)
        self.T0HI = T0HI(self.channel, self.chipv)
        self.T0UPDATE = T0UPDATE(self.channel, self.chipv)
        self.T0ALARMLO = T0ALARMLO(self.channel, self.chipv)
        self.T0ALARMHI = T0ALARMHI(self.channel, self.chipv)
        self.T0LOADLO = T0LOADLO(self.channel, self.chipv)
        self.T0LOADHI = T0LOADHI(self.channel, self.chipv)
        self.T0LOAD = T0LOAD(self.channel, self.chipv)
        self.T1CONFIG = T1CONFIG(self.channel, self.chipv)
        self.T1LO = T1LO(self.channel, self.chipv)
        self.T1HI = T1HI(self.channel, self.chipv)
        self.T1UPDATE = T1UPDATE(self.channel, self.chipv)
        self.T1ALARMLO = T1ALARMLO(self.channel, self.chipv)
        self.T1ALARMHI = T1ALARMHI(self.channel, self.chipv)
        self.T1LOADLO = T1LOADLO(self.channel, self.chipv)
        self.T1LOADHI = T1LOADHI(self.channel, self.chipv)
        self.T1LOAD = T1LOAD(self.channel, self.chipv)
        self.WDTCONFIG0 = WDTCONFIG0(self.channel, self.chipv)
        self.WDTCONFIG1 = WDTCONFIG1(self.channel, self.chipv)
        self.WDTCONFIG2 = WDTCONFIG2(self.channel, self.chipv)
        self.WDTCONFIG3 = WDTCONFIG3(self.channel, self.chipv)
        self.WDTCONFIG4 = WDTCONFIG4(self.channel, self.chipv)
        self.WDTCONFIG5 = WDTCONFIG5(self.channel, self.chipv)
        self.WDTFEED = WDTFEED(self.channel, self.chipv)
        self.WDTWPROTECT = WDTWPROTECT(self.channel, self.chipv)
        self.RTCCALICFG = RTCCALICFG(self.channel, self.chipv)
        self.RTCCALICFG1 = RTCCALICFG1(self.channel, self.chipv)
        self.LACTCONFIG = LACTCONFIG(self.channel, self.chipv)
        self.LACTRTC = LACTRTC(self.channel, self.chipv)
        self.LACTLO = LACTLO(self.channel, self.chipv)
        self.LACTHI = LACTHI(self.channel, self.chipv)
        self.LACTUPDATE = LACTUPDATE(self.channel, self.chipv)
        self.LACTALARMLO = LACTALARMLO(self.channel, self.chipv)
        self.LACTALARMHI = LACTALARMHI(self.channel, self.chipv)
        self.LACTLOADLO = LACTLOADLO(self.channel, self.chipv)
        self.LACTLOADHI = LACTLOADHI(self.channel, self.chipv)
        self.LACTLOAD = LACTLOAD(self.channel, self.chipv)
        self.INT_ENA_TIMERS = INT_ENA_TIMERS(self.channel, self.chipv)
        self.INT_RAW_TIMERS = INT_RAW_TIMERS(self.channel, self.chipv)
        self.INT_ST_TIMERS = INT_ST_TIMERS(self.channel, self.chipv)
        self.INT_CLR_TIMERS = INT_CLR_TIMERS(self.channel, self.chipv)
        self.RTCCALICFG2 = RTCCALICFG2(self.channel, self.chipv)
        self.NTIMERS_DATE = NTIMERS_DATE(self.channel, self.chipv)
        self.REGCLK = REGCLK(self.channel, self.chipv)
class T0CONFIG(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x0
        self.__reg_t0_en_lsb = 31
        self.__reg_t0_en_msb = 31
        self.__reg_t0_increase_lsb = 30
        self.__reg_t0_increase_msb = 30
        self.__reg_t0_autoreload_lsb = 29
        self.__reg_t0_autoreload_msb = 29
        self.__reg_t0_divider_lsb = 13
        self.__reg_t0_divider_msb = 28
        self.__reg_t0_edge_int_en_lsb = 12
        self.__reg_t0_edge_int_en_msb = 12
        self.__reg_t0_level_int_en_lsb = 11
        self.__reg_t0_level_int_en_msb = 11
        self.__reg_t0_alarm_en_lsb = 10
        self.__reg_t0_alarm_en_msb = 10
        self.__reg_t0_use_xtal_lsb = 9
        self.__reg_t0_use_xtal_msb = 9
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_t0_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_t0_en_msb, self.__reg_t0_en_lsb)
    @reg_t0_en.setter
    def reg_t0_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_t0_en_msb, self.__reg_t0_en_lsb, value)

    @property
    def reg_t0_increase(self):
        return self.__MEM.rdm(self.__addr, self.__reg_t0_increase_msb, self.__reg_t0_increase_lsb)
    @reg_t0_increase.setter
    def reg_t0_increase(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_t0_increase_msb, self.__reg_t0_increase_lsb, value)

    @property
    def reg_t0_autoreload(self):
        return self.__MEM.rdm(self.__addr, self.__reg_t0_autoreload_msb, self.__reg_t0_autoreload_lsb)
    @reg_t0_autoreload.setter
    def reg_t0_autoreload(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_t0_autoreload_msb, self.__reg_t0_autoreload_lsb, value)

    @property
    def reg_t0_divider(self):
        return self.__MEM.rdm(self.__addr, self.__reg_t0_divider_msb, self.__reg_t0_divider_lsb)
    @reg_t0_divider.setter
    def reg_t0_divider(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_t0_divider_msb, self.__reg_t0_divider_lsb, value)

    @property
    def reg_t0_edge_int_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_t0_edge_int_en_msb, self.__reg_t0_edge_int_en_lsb)
    @reg_t0_edge_int_en.setter
    def reg_t0_edge_int_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_t0_edge_int_en_msb, self.__reg_t0_edge_int_en_lsb, value)

    @property
    def reg_t0_level_int_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_t0_level_int_en_msb, self.__reg_t0_level_int_en_lsb)
    @reg_t0_level_int_en.setter
    def reg_t0_level_int_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_t0_level_int_en_msb, self.__reg_t0_level_int_en_lsb, value)

    @property
    def reg_t0_alarm_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_t0_alarm_en_msb, self.__reg_t0_alarm_en_lsb)
    @reg_t0_alarm_en.setter
    def reg_t0_alarm_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_t0_alarm_en_msb, self.__reg_t0_alarm_en_lsb, value)

    @property
    def reg_t0_use_xtal(self):
        return self.__MEM.rdm(self.__addr, self.__reg_t0_use_xtal_msb, self.__reg_t0_use_xtal_lsb)
    @reg_t0_use_xtal.setter
    def reg_t0_use_xtal(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_t0_use_xtal_msb, self.__reg_t0_use_xtal_lsb, value)
class T0LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x4
        self.__t0_lo_lsb = 0
        self.__t0_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def t0_lo(self):
        return self.__MEM.rdm(self.__addr, self.__t0_lo_msb, self.__t0_lo_lsb)
    @t0_lo.setter
    def t0_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__t0_lo_msb, self.__t0_lo_lsb, value)
class T0HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x8
        self.__t0_hi_lsb = 0
        self.__t0_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def t0_hi(self):
        return self.__MEM.rdm(self.__addr, self.__t0_hi_msb, self.__t0_hi_lsb)
    @t0_hi.setter
    def t0_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__t0_hi_msb, self.__t0_hi_lsb, value)
class T0UPDATE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0xc
        self.__t0_update_lsb = 31
        self.__t0_update_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def t0_update(self):
        return self.__MEM.rdm(self.__addr, self.__t0_update_msb, self.__t0_update_lsb)
    @t0_update.setter
    def t0_update(self, value):
        return self.__MEM.wrm(self.__addr, self.__t0_update_msb, self.__t0_update_lsb, value)
    @property
    def default_value(self):
        return 0x0
class T0ALARMLO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x10
        self.__reg_t0_alarm_lo_lsb = 0
        self.__reg_t0_alarm_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_t0_alarm_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_t0_alarm_lo_msb, self.__reg_t0_alarm_lo_lsb)
    @reg_t0_alarm_lo.setter
    def reg_t0_alarm_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_t0_alarm_lo_msb, self.__reg_t0_alarm_lo_lsb, value)
class T0ALARMHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x14
        self.__reg_t0_alarm_hi_lsb = 0
        self.__reg_t0_alarm_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_t0_alarm_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_t0_alarm_hi_msb, self.__reg_t0_alarm_hi_lsb)
    @reg_t0_alarm_hi.setter
    def reg_t0_alarm_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_t0_alarm_hi_msb, self.__reg_t0_alarm_hi_lsb, value)
class T0LOADLO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x18
        self.__reg_t0_load_lo_lsb = 0
        self.__reg_t0_load_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_t0_load_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_t0_load_lo_msb, self.__reg_t0_load_lo_lsb)
    @reg_t0_load_lo.setter
    def reg_t0_load_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_t0_load_lo_msb, self.__reg_t0_load_lo_lsb, value)
class T0LOADHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x1c
        self.__reg_t0_load_hi_lsb = 0
        self.__reg_t0_load_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_t0_load_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_t0_load_hi_msb, self.__reg_t0_load_hi_lsb)
    @reg_t0_load_hi.setter
    def reg_t0_load_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_t0_load_hi_msb, self.__reg_t0_load_hi_lsb, value)
class T0LOAD(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x20
        self.__t0_load_lsb = 0
        self.__t0_load_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def t0_load(self):
        return self.__MEM.rdm(self.__addr, self.__t0_load_msb, self.__t0_load_lsb)
    @t0_load.setter
    def t0_load(self, value):
        return self.__MEM.wrm(self.__addr, self.__t0_load_msb, self.__t0_load_lsb, value)
class T1CONFIG(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x24
        self.__reg_t1_en_lsb = 31
        self.__reg_t1_en_msb = 31
        self.__reg_t1_increase_lsb = 30
        self.__reg_t1_increase_msb = 30
        self.__reg_t1_autoreload_lsb = 29
        self.__reg_t1_autoreload_msb = 29
        self.__reg_t1_divider_lsb = 13
        self.__reg_t1_divider_msb = 28
        self.__reg_t1_edge_int_en_lsb = 12
        self.__reg_t1_edge_int_en_msb = 12
        self.__reg_t1_level_int_en_lsb = 11
        self.__reg_t1_level_int_en_msb = 11
        self.__reg_t1_alarm_en_lsb = 10
        self.__reg_t1_alarm_en_msb = 10
        self.__reg_t1_use_xtal_lsb = 9
        self.__reg_t1_use_xtal_msb = 9
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_t1_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_t1_en_msb, self.__reg_t1_en_lsb)
    @reg_t1_en.setter
    def reg_t1_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_t1_en_msb, self.__reg_t1_en_lsb, value)

    @property
    def reg_t1_increase(self):
        return self.__MEM.rdm(self.__addr, self.__reg_t1_increase_msb, self.__reg_t1_increase_lsb)
    @reg_t1_increase.setter
    def reg_t1_increase(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_t1_increase_msb, self.__reg_t1_increase_lsb, value)

    @property
    def reg_t1_autoreload(self):
        return self.__MEM.rdm(self.__addr, self.__reg_t1_autoreload_msb, self.__reg_t1_autoreload_lsb)
    @reg_t1_autoreload.setter
    def reg_t1_autoreload(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_t1_autoreload_msb, self.__reg_t1_autoreload_lsb, value)

    @property
    def reg_t1_divider(self):
        return self.__MEM.rdm(self.__addr, self.__reg_t1_divider_msb, self.__reg_t1_divider_lsb)
    @reg_t1_divider.setter
    def reg_t1_divider(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_t1_divider_msb, self.__reg_t1_divider_lsb, value)

    @property
    def reg_t1_edge_int_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_t1_edge_int_en_msb, self.__reg_t1_edge_int_en_lsb)
    @reg_t1_edge_int_en.setter
    def reg_t1_edge_int_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_t1_edge_int_en_msb, self.__reg_t1_edge_int_en_lsb, value)

    @property
    def reg_t1_level_int_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_t1_level_int_en_msb, self.__reg_t1_level_int_en_lsb)
    @reg_t1_level_int_en.setter
    def reg_t1_level_int_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_t1_level_int_en_msb, self.__reg_t1_level_int_en_lsb, value)

    @property
    def reg_t1_alarm_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_t1_alarm_en_msb, self.__reg_t1_alarm_en_lsb)
    @reg_t1_alarm_en.setter
    def reg_t1_alarm_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_t1_alarm_en_msb, self.__reg_t1_alarm_en_lsb, value)

    @property
    def reg_t1_use_xtal(self):
        return self.__MEM.rdm(self.__addr, self.__reg_t1_use_xtal_msb, self.__reg_t1_use_xtal_lsb)
    @reg_t1_use_xtal.setter
    def reg_t1_use_xtal(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_t1_use_xtal_msb, self.__reg_t1_use_xtal_lsb, value)
class T1LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x28
        self.__t1_lo_lsb = 0
        self.__t1_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def t1_lo(self):
        return self.__MEM.rdm(self.__addr, self.__t1_lo_msb, self.__t1_lo_lsb)
    @t1_lo.setter
    def t1_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__t1_lo_msb, self.__t1_lo_lsb, value)
class T1HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x2c
        self.__t1_hi_lsb = 0
        self.__t1_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def t1_hi(self):
        return self.__MEM.rdm(self.__addr, self.__t1_hi_msb, self.__t1_hi_lsb)
    @t1_hi.setter
    def t1_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__t1_hi_msb, self.__t1_hi_lsb, value)
class T1UPDATE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x30
        self.__t1_update_lsb = 31
        self.__t1_update_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def t1_update(self):
        return self.__MEM.rdm(self.__addr, self.__t1_update_msb, self.__t1_update_lsb)
    @t1_update.setter
    def t1_update(self, value):
        return self.__MEM.wrm(self.__addr, self.__t1_update_msb, self.__t1_update_lsb, value)
    @property
    def default_value(self):
        return 0x0
class T1ALARMLO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x34
        self.__reg_t1_alarm_lo_lsb = 0
        self.__reg_t1_alarm_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_t1_alarm_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_t1_alarm_lo_msb, self.__reg_t1_alarm_lo_lsb)
    @reg_t1_alarm_lo.setter
    def reg_t1_alarm_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_t1_alarm_lo_msb, self.__reg_t1_alarm_lo_lsb, value)
class T1ALARMHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x38
        self.__reg_t1_alarm_hi_lsb = 0
        self.__reg_t1_alarm_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_t1_alarm_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_t1_alarm_hi_msb, self.__reg_t1_alarm_hi_lsb)
    @reg_t1_alarm_hi.setter
    def reg_t1_alarm_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_t1_alarm_hi_msb, self.__reg_t1_alarm_hi_lsb, value)
class T1LOADLO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x3c
        self.__reg_t1_load_lo_lsb = 0
        self.__reg_t1_load_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_t1_load_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_t1_load_lo_msb, self.__reg_t1_load_lo_lsb)
    @reg_t1_load_lo.setter
    def reg_t1_load_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_t1_load_lo_msb, self.__reg_t1_load_lo_lsb, value)
class T1LOADHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x40
        self.__reg_t1_load_hi_lsb = 0
        self.__reg_t1_load_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_t1_load_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_t1_load_hi_msb, self.__reg_t1_load_hi_lsb)
    @reg_t1_load_hi.setter
    def reg_t1_load_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_t1_load_hi_msb, self.__reg_t1_load_hi_lsb, value)
class T1LOAD(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x44
        self.__t1_load_lsb = 0
        self.__t1_load_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def t1_load(self):
        return self.__MEM.rdm(self.__addr, self.__t1_load_msb, self.__t1_load_lsb)
    @t1_load.setter
    def t1_load(self, value):
        return self.__MEM.wrm(self.__addr, self.__t1_load_msb, self.__t1_load_lsb, value)
class WDTCONFIG0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x48
        self.__reg_wdt_en_lsb = 31
        self.__reg_wdt_en_msb = 31
        self.__reg_wdt_stg0_lsb = 29
        self.__reg_wdt_stg0_msb = 30
        self.__reg_wdt_stg1_lsb = 27
        self.__reg_wdt_stg1_msb = 28
        self.__reg_wdt_stg2_lsb = 25
        self.__reg_wdt_stg2_msb = 26
        self.__reg_wdt_stg3_lsb = 23
        self.__reg_wdt_stg3_msb = 24
        self.__reg_wdt_edge_int_en_lsb = 22
        self.__reg_wdt_edge_int_en_msb = 22
        self.__reg_wdt_level_int_en_lsb = 21
        self.__reg_wdt_level_int_en_msb = 21
        self.__reg_wdt_cpu_reset_length_lsb = 18
        self.__reg_wdt_cpu_reset_length_msb = 20
        self.__reg_wdt_sys_reset_length_lsb = 15
        self.__reg_wdt_sys_reset_length_msb = 17
        self.__reg_wdt_flashboot_mod_en_lsb = 14
        self.__reg_wdt_flashboot_mod_en_msb = 14
        self.__reg_wdt_procpu_reset_en_lsb = 13
        self.__reg_wdt_procpu_reset_en_msb = 13
        self.__reg_wdt_appcpu_reset_en_lsb = 12
        self.__reg_wdt_appcpu_reset_en_msb = 12
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wdt_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wdt_en_msb, self.__reg_wdt_en_lsb)
    @reg_wdt_en.setter
    def reg_wdt_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wdt_en_msb, self.__reg_wdt_en_lsb, value)

    @property
    def reg_wdt_stg0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wdt_stg0_msb, self.__reg_wdt_stg0_lsb)
    @reg_wdt_stg0.setter
    def reg_wdt_stg0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wdt_stg0_msb, self.__reg_wdt_stg0_lsb, value)

    @property
    def reg_wdt_stg1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wdt_stg1_msb, self.__reg_wdt_stg1_lsb)
    @reg_wdt_stg1.setter
    def reg_wdt_stg1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wdt_stg1_msb, self.__reg_wdt_stg1_lsb, value)

    @property
    def reg_wdt_stg2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wdt_stg2_msb, self.__reg_wdt_stg2_lsb)
    @reg_wdt_stg2.setter
    def reg_wdt_stg2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wdt_stg2_msb, self.__reg_wdt_stg2_lsb, value)

    @property
    def reg_wdt_stg3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wdt_stg3_msb, self.__reg_wdt_stg3_lsb)
    @reg_wdt_stg3.setter
    def reg_wdt_stg3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wdt_stg3_msb, self.__reg_wdt_stg3_lsb, value)

    @property
    def reg_wdt_edge_int_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wdt_edge_int_en_msb, self.__reg_wdt_edge_int_en_lsb)
    @reg_wdt_edge_int_en.setter
    def reg_wdt_edge_int_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wdt_edge_int_en_msb, self.__reg_wdt_edge_int_en_lsb, value)

    @property
    def reg_wdt_level_int_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wdt_level_int_en_msb, self.__reg_wdt_level_int_en_lsb)
    @reg_wdt_level_int_en.setter
    def reg_wdt_level_int_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wdt_level_int_en_msb, self.__reg_wdt_level_int_en_lsb, value)

    @property
    def reg_wdt_cpu_reset_length(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wdt_cpu_reset_length_msb, self.__reg_wdt_cpu_reset_length_lsb)
    @reg_wdt_cpu_reset_length.setter
    def reg_wdt_cpu_reset_length(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wdt_cpu_reset_length_msb, self.__reg_wdt_cpu_reset_length_lsb, value)

    @property
    def reg_wdt_sys_reset_length(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wdt_sys_reset_length_msb, self.__reg_wdt_sys_reset_length_lsb)
    @reg_wdt_sys_reset_length.setter
    def reg_wdt_sys_reset_length(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wdt_sys_reset_length_msb, self.__reg_wdt_sys_reset_length_lsb, value)

    @property
    def reg_wdt_flashboot_mod_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wdt_flashboot_mod_en_msb, self.__reg_wdt_flashboot_mod_en_lsb)
    @reg_wdt_flashboot_mod_en.setter
    def reg_wdt_flashboot_mod_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wdt_flashboot_mod_en_msb, self.__reg_wdt_flashboot_mod_en_lsb, value)

    @property
    def reg_wdt_procpu_reset_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wdt_procpu_reset_en_msb, self.__reg_wdt_procpu_reset_en_lsb)
    @reg_wdt_procpu_reset_en.setter
    def reg_wdt_procpu_reset_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wdt_procpu_reset_en_msb, self.__reg_wdt_procpu_reset_en_lsb, value)

    @property
    def reg_wdt_appcpu_reset_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wdt_appcpu_reset_en_msb, self.__reg_wdt_appcpu_reset_en_lsb)
    @reg_wdt_appcpu_reset_en.setter
    def reg_wdt_appcpu_reset_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wdt_appcpu_reset_en_msb, self.__reg_wdt_appcpu_reset_en_lsb, value)
class WDTCONFIG1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x4c
        self.__reg_wdt_clk_prescale_lsb = 16
        self.__reg_wdt_clk_prescale_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wdt_clk_prescale(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wdt_clk_prescale_msb, self.__reg_wdt_clk_prescale_lsb)
    @reg_wdt_clk_prescale.setter
    def reg_wdt_clk_prescale(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wdt_clk_prescale_msb, self.__reg_wdt_clk_prescale_lsb, value)
class WDTCONFIG2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x50
        self.__reg_wdt_stg0_hold_lsb = 0
        self.__reg_wdt_stg0_hold_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wdt_stg0_hold(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wdt_stg0_hold_msb, self.__reg_wdt_stg0_hold_lsb)
    @reg_wdt_stg0_hold.setter
    def reg_wdt_stg0_hold(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wdt_stg0_hold_msb, self.__reg_wdt_stg0_hold_lsb, value)
class WDTCONFIG3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x54
        self.__reg_wdt_stg1_hold_lsb = 0
        self.__reg_wdt_stg1_hold_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wdt_stg1_hold(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wdt_stg1_hold_msb, self.__reg_wdt_stg1_hold_lsb)
    @reg_wdt_stg1_hold.setter
    def reg_wdt_stg1_hold(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wdt_stg1_hold_msb, self.__reg_wdt_stg1_hold_lsb, value)
class WDTCONFIG4(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x58
        self.__reg_wdt_stg2_hold_lsb = 0
        self.__reg_wdt_stg2_hold_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wdt_stg2_hold(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wdt_stg2_hold_msb, self.__reg_wdt_stg2_hold_lsb)
    @reg_wdt_stg2_hold.setter
    def reg_wdt_stg2_hold(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wdt_stg2_hold_msb, self.__reg_wdt_stg2_hold_lsb, value)
class WDTCONFIG5(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x5c
        self.__reg_wdt_stg3_hold_lsb = 0
        self.__reg_wdt_stg3_hold_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wdt_stg3_hold(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wdt_stg3_hold_msb, self.__reg_wdt_stg3_hold_lsb)
    @reg_wdt_stg3_hold.setter
    def reg_wdt_stg3_hold(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wdt_stg3_hold_msb, self.__reg_wdt_stg3_hold_lsb, value)
class WDTFEED(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x60
        self.__wdt_feed_lsb = 0
        self.__wdt_feed_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def wdt_feed(self):
        return self.__MEM.rdm(self.__addr, self.__wdt_feed_msb, self.__wdt_feed_lsb)
    @wdt_feed.setter
    def wdt_feed(self, value):
        return self.__MEM.wrm(self.__addr, self.__wdt_feed_msb, self.__wdt_feed_lsb, value)
class WDTWPROTECT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x64
        self.__reg_wdt_wkey_lsb = 0
        self.__reg_wdt_wkey_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wdt_wkey(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wdt_wkey_msb, self.__reg_wdt_wkey_lsb)
    @reg_wdt_wkey.setter
    def reg_wdt_wkey(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wdt_wkey_msb, self.__reg_wdt_wkey_lsb, value)
class RTCCALICFG(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x68
        self.__reg_rtc_cali_start_lsb = 31
        self.__reg_rtc_cali_start_msb = 31
        self.__reg_rtc_cali_max_lsb = 16
        self.__reg_rtc_cali_max_msb = 30
        self.__rtc_cali_rdy_lsb = 15
        self.__rtc_cali_rdy_msb = 15
        self.__reg_rtc_cali_clk_sel_lsb = 13
        self.__reg_rtc_cali_clk_sel_msb = 14
        self.__reg_rtc_cali_start_cycling_lsb = 12
        self.__reg_rtc_cali_start_cycling_msb = 12
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rtc_cali_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_cali_start_msb, self.__reg_rtc_cali_start_lsb)
    @reg_rtc_cali_start.setter
    def reg_rtc_cali_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_cali_start_msb, self.__reg_rtc_cali_start_lsb, value)

    @property
    def reg_rtc_cali_max(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_cali_max_msb, self.__reg_rtc_cali_max_lsb)
    @reg_rtc_cali_max.setter
    def reg_rtc_cali_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_cali_max_msb, self.__reg_rtc_cali_max_lsb, value)

    @property
    def rtc_cali_rdy(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_cali_rdy_msb, self.__rtc_cali_rdy_lsb)
    @rtc_cali_rdy.setter
    def rtc_cali_rdy(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_cali_rdy_msb, self.__rtc_cali_rdy_lsb, value)

    @property
    def reg_rtc_cali_clk_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_cali_clk_sel_msb, self.__reg_rtc_cali_clk_sel_lsb)
    @reg_rtc_cali_clk_sel.setter
    def reg_rtc_cali_clk_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_cali_clk_sel_msb, self.__reg_rtc_cali_clk_sel_lsb, value)

    @property
    def reg_rtc_cali_start_cycling(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_cali_start_cycling_msb, self.__reg_rtc_cali_start_cycling_lsb)
    @reg_rtc_cali_start_cycling.setter
    def reg_rtc_cali_start_cycling(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_cali_start_cycling_msb, self.__reg_rtc_cali_start_cycling_lsb, value)
class RTCCALICFG1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x6c
        self.__rtc_cali_value_lsb = 7
        self.__rtc_cali_value_msb = 31
        self.__rtc_cali_cycling_data_vld_lsb = 0
        self.__rtc_cali_cycling_data_vld_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_cali_value(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_cali_value_msb, self.__rtc_cali_value_lsb)
    @rtc_cali_value.setter
    def rtc_cali_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_cali_value_msb, self.__rtc_cali_value_lsb, value)

    @property
    def rtc_cali_cycling_data_vld(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_cali_cycling_data_vld_msb, self.__rtc_cali_cycling_data_vld_lsb)
    @rtc_cali_cycling_data_vld.setter
    def rtc_cali_cycling_data_vld(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_cali_cycling_data_vld_msb, self.__rtc_cali_cycling_data_vld_lsb, value)
class LACTCONFIG(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x70
        self.__reg_lact_en_lsb = 31
        self.__reg_lact_en_msb = 31
        self.__reg_lact_increase_lsb = 30
        self.__reg_lact_increase_msb = 30
        self.__reg_lact_autoreload_lsb = 29
        self.__reg_lact_autoreload_msb = 29
        self.__reg_lact_divider_lsb = 13
        self.__reg_lact_divider_msb = 28
        self.__reg_lact_edge_int_en_lsb = 12
        self.__reg_lact_edge_int_en_msb = 12
        self.__reg_lact_level_int_en_lsb = 11
        self.__reg_lact_level_int_en_msb = 11
        self.__reg_lact_alarm_en_lsb = 10
        self.__reg_lact_alarm_en_msb = 10
        self.__reg_lact_lac_en_lsb = 9
        self.__reg_lact_lac_en_msb = 9
        self.__reg_lact_cpst_en_lsb = 8
        self.__reg_lact_cpst_en_msb = 8
        self.__reg_lact_rtc_only_lsb = 7
        self.__reg_lact_rtc_only_msb = 7
        self.__reg_lact_use_reftick_lsb = 6
        self.__reg_lact_use_reftick_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_lact_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lact_en_msb, self.__reg_lact_en_lsb)
    @reg_lact_en.setter
    def reg_lact_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lact_en_msb, self.__reg_lact_en_lsb, value)

    @property
    def reg_lact_increase(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lact_increase_msb, self.__reg_lact_increase_lsb)
    @reg_lact_increase.setter
    def reg_lact_increase(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lact_increase_msb, self.__reg_lact_increase_lsb, value)

    @property
    def reg_lact_autoreload(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lact_autoreload_msb, self.__reg_lact_autoreload_lsb)
    @reg_lact_autoreload.setter
    def reg_lact_autoreload(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lact_autoreload_msb, self.__reg_lact_autoreload_lsb, value)

    @property
    def reg_lact_divider(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lact_divider_msb, self.__reg_lact_divider_lsb)
    @reg_lact_divider.setter
    def reg_lact_divider(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lact_divider_msb, self.__reg_lact_divider_lsb, value)

    @property
    def reg_lact_edge_int_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lact_edge_int_en_msb, self.__reg_lact_edge_int_en_lsb)
    @reg_lact_edge_int_en.setter
    def reg_lact_edge_int_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lact_edge_int_en_msb, self.__reg_lact_edge_int_en_lsb, value)

    @property
    def reg_lact_level_int_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lact_level_int_en_msb, self.__reg_lact_level_int_en_lsb)
    @reg_lact_level_int_en.setter
    def reg_lact_level_int_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lact_level_int_en_msb, self.__reg_lact_level_int_en_lsb, value)

    @property
    def reg_lact_alarm_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lact_alarm_en_msb, self.__reg_lact_alarm_en_lsb)
    @reg_lact_alarm_en.setter
    def reg_lact_alarm_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lact_alarm_en_msb, self.__reg_lact_alarm_en_lsb, value)

    @property
    def reg_lact_lac_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lact_lac_en_msb, self.__reg_lact_lac_en_lsb)
    @reg_lact_lac_en.setter
    def reg_lact_lac_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lact_lac_en_msb, self.__reg_lact_lac_en_lsb, value)

    @property
    def reg_lact_cpst_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lact_cpst_en_msb, self.__reg_lact_cpst_en_lsb)
    @reg_lact_cpst_en.setter
    def reg_lact_cpst_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lact_cpst_en_msb, self.__reg_lact_cpst_en_lsb, value)

    @property
    def reg_lact_rtc_only(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lact_rtc_only_msb, self.__reg_lact_rtc_only_lsb)
    @reg_lact_rtc_only.setter
    def reg_lact_rtc_only(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lact_rtc_only_msb, self.__reg_lact_rtc_only_lsb, value)

    @property
    def reg_lact_use_reftick(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lact_use_reftick_msb, self.__reg_lact_use_reftick_lsb)
    @reg_lact_use_reftick.setter
    def reg_lact_use_reftick(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lact_use_reftick_msb, self.__reg_lact_use_reftick_lsb, value)
class LACTRTC(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x74
        self.__reg_lact_rtc_step_len_lsb = 6
        self.__reg_lact_rtc_step_len_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_lact_rtc_step_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lact_rtc_step_len_msb, self.__reg_lact_rtc_step_len_lsb)
    @reg_lact_rtc_step_len.setter
    def reg_lact_rtc_step_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lact_rtc_step_len_msb, self.__reg_lact_rtc_step_len_lsb, value)
class LACTLO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x78
        self.__lact_lo_lsb = 0
        self.__lact_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def lact_lo(self):
        return self.__MEM.rdm(self.__addr, self.__lact_lo_msb, self.__lact_lo_lsb)
    @lact_lo.setter
    def lact_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__lact_lo_msb, self.__lact_lo_lsb, value)
class LACTHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x7c
        self.__lact_hi_lsb = 0
        self.__lact_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def lact_hi(self):
        return self.__MEM.rdm(self.__addr, self.__lact_hi_msb, self.__lact_hi_lsb)
    @lact_hi.setter
    def lact_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__lact_hi_msb, self.__lact_hi_lsb, value)
class LACTUPDATE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x80
        self.__lact_update_lsb = 0
        self.__lact_update_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def lact_update(self):
        return self.__MEM.rdm(self.__addr, self.__lact_update_msb, self.__lact_update_lsb)
    @lact_update.setter
    def lact_update(self, value):
        return self.__MEM.wrm(self.__addr, self.__lact_update_msb, self.__lact_update_lsb, value)
    @property
    def default_value(self):
        return 0x0
class LACTALARMLO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x84
        self.__reg_lact_alarm_lo_lsb = 0
        self.__reg_lact_alarm_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_lact_alarm_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lact_alarm_lo_msb, self.__reg_lact_alarm_lo_lsb)
    @reg_lact_alarm_lo.setter
    def reg_lact_alarm_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lact_alarm_lo_msb, self.__reg_lact_alarm_lo_lsb, value)
class LACTALARMHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x88
        self.__reg_lact_alarm_hi_lsb = 0
        self.__reg_lact_alarm_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_lact_alarm_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lact_alarm_hi_msb, self.__reg_lact_alarm_hi_lsb)
    @reg_lact_alarm_hi.setter
    def reg_lact_alarm_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lact_alarm_hi_msb, self.__reg_lact_alarm_hi_lsb, value)
class LACTLOADLO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x8c
        self.__reg_lact_load_lo_lsb = 0
        self.__reg_lact_load_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_lact_load_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lact_load_lo_msb, self.__reg_lact_load_lo_lsb)
    @reg_lact_load_lo.setter
    def reg_lact_load_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lact_load_lo_msb, self.__reg_lact_load_lo_lsb, value)
class LACTLOADHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x90
        self.__reg_lact_load_hi_lsb = 0
        self.__reg_lact_load_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_lact_load_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lact_load_hi_msb, self.__reg_lact_load_hi_lsb)
    @reg_lact_load_hi.setter
    def reg_lact_load_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lact_load_hi_msb, self.__reg_lact_load_hi_lsb, value)
class LACTLOAD(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x94
        self.__lact_load_lsb = 0
        self.__lact_load_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def lact_load(self):
        return self.__MEM.rdm(self.__addr, self.__lact_load_msb, self.__lact_load_lsb)
    @lact_load.setter
    def lact_load(self, value):
        return self.__MEM.wrm(self.__addr, self.__lact_load_msb, self.__lact_load_lsb, value)
class INT_ENA_TIMERS(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x98
        self.__lact_int_ena_lsb = 3
        self.__lact_int_ena_msb = 3
        self.__wdt_int_ena_lsb = 2
        self.__wdt_int_ena_msb = 2
        self.__t1_int_ena_lsb = 1
        self.__t1_int_ena_msb = 1
        self.__t0_int_ena_lsb = 0
        self.__t0_int_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def lact_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__lact_int_ena_msb, self.__lact_int_ena_lsb)
    @lact_int_ena.setter
    def lact_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__lact_int_ena_msb, self.__lact_int_ena_lsb, value)

    @property
    def wdt_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__wdt_int_ena_msb, self.__wdt_int_ena_lsb)
    @wdt_int_ena.setter
    def wdt_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__wdt_int_ena_msb, self.__wdt_int_ena_lsb, value)

    @property
    def t1_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__t1_int_ena_msb, self.__t1_int_ena_lsb)
    @t1_int_ena.setter
    def t1_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__t1_int_ena_msb, self.__t1_int_ena_lsb, value)

    @property
    def t0_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__t0_int_ena_msb, self.__t0_int_ena_lsb)
    @t0_int_ena.setter
    def t0_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__t0_int_ena_msb, self.__t0_int_ena_lsb, value)
class INT_RAW_TIMERS(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0x9c
        self.__lact_int_raw_lsb = 3
        self.__lact_int_raw_msb = 3
        self.__wdt_int_raw_lsb = 2
        self.__wdt_int_raw_msb = 2
        self.__t1_int_raw_lsb = 1
        self.__t1_int_raw_msb = 1
        self.__t0_int_raw_lsb = 0
        self.__t0_int_raw_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def lact_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__lact_int_raw_msb, self.__lact_int_raw_lsb)
    @lact_int_raw.setter
    def lact_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__lact_int_raw_msb, self.__lact_int_raw_lsb, value)

    @property
    def wdt_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__wdt_int_raw_msb, self.__wdt_int_raw_lsb)
    @wdt_int_raw.setter
    def wdt_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__wdt_int_raw_msb, self.__wdt_int_raw_lsb, value)

    @property
    def t1_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__t1_int_raw_msb, self.__t1_int_raw_lsb)
    @t1_int_raw.setter
    def t1_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__t1_int_raw_msb, self.__t1_int_raw_lsb, value)

    @property
    def t0_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__t0_int_raw_msb, self.__t0_int_raw_lsb)
    @t0_int_raw.setter
    def t0_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__t0_int_raw_msb, self.__t0_int_raw_lsb, value)
class INT_ST_TIMERS(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0xa0
        self.__lact_int_st_lsb = 3
        self.__lact_int_st_msb = 3
        self.__wdt_int_st_lsb = 2
        self.__wdt_int_st_msb = 2
        self.__t1_int_st_lsb = 1
        self.__t1_int_st_msb = 1
        self.__t0_int_st_lsb = 0
        self.__t0_int_st_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def lact_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__lact_int_st_msb, self.__lact_int_st_lsb)
    @lact_int_st.setter
    def lact_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__lact_int_st_msb, self.__lact_int_st_lsb, value)

    @property
    def wdt_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__wdt_int_st_msb, self.__wdt_int_st_lsb)
    @wdt_int_st.setter
    def wdt_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__wdt_int_st_msb, self.__wdt_int_st_lsb, value)

    @property
    def t1_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__t1_int_st_msb, self.__t1_int_st_lsb)
    @t1_int_st.setter
    def t1_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__t1_int_st_msb, self.__t1_int_st_lsb, value)

    @property
    def t0_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__t0_int_st_msb, self.__t0_int_st_lsb)
    @t0_int_st.setter
    def t0_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__t0_int_st_msb, self.__t0_int_st_lsb, value)
class INT_CLR_TIMERS(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0xa4
        self.__lact_int_clr_lsb = 3
        self.__lact_int_clr_msb = 3
        self.__wdt_int_clr_lsb = 2
        self.__wdt_int_clr_msb = 2
        self.__t1_int_clr_lsb = 1
        self.__t1_int_clr_msb = 1
        self.__t0_int_clr_lsb = 0
        self.__t0_int_clr_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def lact_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__lact_int_clr_msb, self.__lact_int_clr_lsb)
    @lact_int_clr.setter
    def lact_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__lact_int_clr_msb, self.__lact_int_clr_lsb, value)

    @property
    def wdt_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__wdt_int_clr_msb, self.__wdt_int_clr_lsb)
    @wdt_int_clr.setter
    def wdt_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__wdt_int_clr_msb, self.__wdt_int_clr_lsb, value)

    @property
    def t1_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__t1_int_clr_msb, self.__t1_int_clr_lsb)
    @t1_int_clr.setter
    def t1_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__t1_int_clr_msb, self.__t1_int_clr_lsb, value)

    @property
    def t0_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__t0_int_clr_msb, self.__t0_int_clr_lsb)
    @t0_int_clr.setter
    def t0_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__t0_int_clr_msb, self.__t0_int_clr_lsb, value)
class RTCCALICFG2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0xa8
        self.__reg_rtc_cali_timeout_thres_lsb = 7
        self.__reg_rtc_cali_timeout_thres_msb = 31
        self.__reg_rtc_cali_timeout_rst_cnt_lsb = 3
        self.__reg_rtc_cali_timeout_rst_cnt_msb = 6
        self.__rtc_cali_timeout_lsb = 0
        self.__rtc_cali_timeout_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rtc_cali_timeout_thres(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_cali_timeout_thres_msb, self.__reg_rtc_cali_timeout_thres_lsb)
    @reg_rtc_cali_timeout_thres.setter
    def reg_rtc_cali_timeout_thres(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_cali_timeout_thres_msb, self.__reg_rtc_cali_timeout_thres_lsb, value)

    @property
    def reg_rtc_cali_timeout_rst_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_cali_timeout_rst_cnt_msb, self.__reg_rtc_cali_timeout_rst_cnt_lsb)
    @reg_rtc_cali_timeout_rst_cnt.setter
    def reg_rtc_cali_timeout_rst_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_cali_timeout_rst_cnt_msb, self.__reg_rtc_cali_timeout_rst_cnt_lsb, value)

    @property
    def rtc_cali_timeout(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_cali_timeout_msb, self.__rtc_cali_timeout_lsb)
    @rtc_cali_timeout.setter
    def rtc_cali_timeout(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_cali_timeout_msb, self.__rtc_cali_timeout_lsb, value)
class NTIMERS_DATE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0xf8
        self.__reg_ntimers_date_lsb = 0
        self.__reg_ntimers_date_msb = 27
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ntimers_date(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ntimers_date_msb, self.__reg_ntimers_date_lsb)
    @reg_ntimers_date.setter
    def reg_ntimers_date(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ntimers_date_msb, self.__reg_ntimers_date_lsb, value)
    @property
    def default_value(self):
        return 0x1810190
class REGCLK(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = TIMERS_BASE + 0xfc
        self.__reg_clk_en_lsb = 31
        self.__reg_clk_en_msb = 31
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
