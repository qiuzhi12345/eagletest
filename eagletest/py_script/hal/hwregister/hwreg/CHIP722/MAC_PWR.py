from hal.common import *
from hal.hwregister.hwreg.CHIP722.addr_base import *
class MAC_PWR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.MACTIME = MACTIME(self.channel, self.chipv)
        self.MACEMAC_TIMER_NS = MACEMAC_TIMER_NS(self.channel, self.chipv)
        self.MACEMAC_TIMER_S = MACEMAC_TIMER_S(self.channel, self.chipv)
        self.MACTIME_SW = MACTIME_SW(self.channel, self.chipv)
        self.MACTSF_TIME_FZ = MACTSF_TIME_FZ(self.channel, self.chipv)
        self.MACTSF0_TIME_LO = MACTSF0_TIME_LO(self.channel, self.chipv)
        self.MACTSF0_TIME_HI = MACTSF0_TIME_HI(self.channel, self.chipv)
        self.MACSLEEP_ST = MACSLEEP_ST(self.channel, self.chipv)
        self.MACSLEEP0_CONF = MACSLEEP0_CONF(self.channel, self.chipv)
        self.MACTSF0_ACTIVE = MACTSF0_ACTIVE(self.channel, self.chipv)
        self.MACTSFSW0_LO = MACTSFSW0_LO(self.channel, self.chipv)
        self.MACTSFSW0_HI = MACTSFSW0_HI(self.channel, self.chipv)
        self.MACBEACTAR0_LO = MACBEACTAR0_LO(self.channel, self.chipv)
        self.MACBEACTAR0_HI = MACBEACTAR0_HI(self.channel, self.chipv)
        self.MACBEATAR0_LO = MACBEATAR0_LO(self.channel, self.chipv)
        self.MACBEATAR0_HI = MACBEATAR0_HI(self.channel, self.chipv)
        self.MACBEA_CUR_TAR0 = MACBEA_CUR_TAR0(self.channel, self.chipv)
        self.MACBEAINTER0 = MACBEAINTER0(self.channel, self.chipv)
        self.MACTSF1_TIME_LO = MACTSF1_TIME_LO(self.channel, self.chipv)
        self.MACTSF1_TIME_HI = MACTSF1_TIME_HI(self.channel, self.chipv)
        self.MACSLEEP1_CONF = MACSLEEP1_CONF(self.channel, self.chipv)
        self.MACTSF1_ACTIVE = MACTSF1_ACTIVE(self.channel, self.chipv)
        self.MACTSFSW1_LO = MACTSFSW1_LO(self.channel, self.chipv)
        self.MACTSFSW1_HI = MACTSFSW1_HI(self.channel, self.chipv)
        self.MACBEACTAR1_LO = MACBEACTAR1_LO(self.channel, self.chipv)
        self.MACBEACTAR1_HI = MACBEACTAR1_HI(self.channel, self.chipv)
        self.MACBEATAR1_LO = MACBEATAR1_LO(self.channel, self.chipv)
        self.MACBEATAR1_HI = MACBEATAR1_HI(self.channel, self.chipv)
        self.MACBEA_CUR_TAR1 = MACBEA_CUR_TAR1(self.channel, self.chipv)
        self.MACBEAINTER1 = MACBEAINTER1(self.channel, self.chipv)
        self.MACTSF2_TIME_LO = MACTSF2_TIME_LO(self.channel, self.chipv)
        self.MACTSF2_TIME_HI = MACTSF2_TIME_HI(self.channel, self.chipv)
        self.MACSLEEP2_CONF = MACSLEEP2_CONF(self.channel, self.chipv)
        self.MACTSF2_ACTIVE = MACTSF2_ACTIVE(self.channel, self.chipv)
        self.MACTSFSW2_LO = MACTSFSW2_LO(self.channel, self.chipv)
        self.MACTSFSW2_HI = MACTSFSW2_HI(self.channel, self.chipv)
        self.MACBEACTAR2_LO = MACBEACTAR2_LO(self.channel, self.chipv)
        self.MACBEACTAR2_HI = MACBEACTAR2_HI(self.channel, self.chipv)
        self.MACBEATAR2_LO = MACBEATAR2_LO(self.channel, self.chipv)
        self.MACBEATAR2_HI = MACBEATAR2_HI(self.channel, self.chipv)
        self.MACBEA_CUR_TAR2 = MACBEA_CUR_TAR2(self.channel, self.chipv)
        self.MACBEAINTER2 = MACBEAINTER2(self.channel, self.chipv)
        self.MACTSF3_TIME_LO = MACTSF3_TIME_LO(self.channel, self.chipv)
        self.MACTSF3_TIME_HI = MACTSF3_TIME_HI(self.channel, self.chipv)
        self.MACSLEEP3_CONF = MACSLEEP3_CONF(self.channel, self.chipv)
        self.MACTSF3_ACTIVE = MACTSF3_ACTIVE(self.channel, self.chipv)
        self.MACTSFSW3_LO = MACTSFSW3_LO(self.channel, self.chipv)
        self.MACTSFSW3_HI = MACTSFSW3_HI(self.channel, self.chipv)
        self.MACBEACTAR3_LO = MACBEACTAR3_LO(self.channel, self.chipv)
        self.MACBEACTAR3_HI = MACBEACTAR3_HI(self.channel, self.chipv)
        self.MACBEATAR3_LO = MACBEATAR3_LO(self.channel, self.chipv)
        self.MACBEATAR3_HI = MACBEATAR3_HI(self.channel, self.chipv)
        self.MACBEA_CUR_TAR3 = MACBEA_CUR_TAR3(self.channel, self.chipv)
        self.MACBEAINTER3 = MACBEAINTER3(self.channel, self.chipv)
        self.MACRTC_CALISW = MACRTC_CALISW(self.channel, self.chipv)
        self.MACTSF0TIMER_ENA = MACTSF0TIMER_ENA(self.channel, self.chipv)
        self.MACTSF0_TIMER_LO = MACTSF0_TIMER_LO(self.channel, self.chipv)
        self.MACTSF0_TIMER_HI = MACTSF0_TIMER_HI(self.channel, self.chipv)
        self.MACTSF1TIMER_ENA = MACTSF1TIMER_ENA(self.channel, self.chipv)
        self.MACTSF1_TIMER_LO = MACTSF1_TIMER_LO(self.channel, self.chipv)
        self.MACTSF1_TIMER_HI = MACTSF1_TIMER_HI(self.channel, self.chipv)
        self.MACTSF2TIMER_ENA = MACTSF2TIMER_ENA(self.channel, self.chipv)
        self.MACTSF2_TIMER_LO = MACTSF2_TIMER_LO(self.channel, self.chipv)
        self.MACTSF2_TIMER_HI = MACTSF2_TIMER_HI(self.channel, self.chipv)
        self.MACTSF3TIMER_ENA = MACTSF3TIMER_ENA(self.channel, self.chipv)
        self.MACTSF3_TIMER_LO = MACTSF3_TIMER_LO(self.channel, self.chipv)
        self.MACTSF3_TIMER_HI = MACTSF3_TIMER_HI(self.channel, self.chipv)
        self.MACRND = MACRND(self.channel, self.chipv)
        self.MACRXBEA_TO = MACRXBEA_TO(self.channel, self.chipv)
        self.MACRWBT_COEX_CONF = MACRWBT_COEX_CONF(self.channel, self.chipv)
        self.MACRWBT_COEX_PTI = MACRWBT_COEX_PTI(self.channel, self.chipv)
        self.MACRWBT_COEX_WAIT0 = MACRWBT_COEX_WAIT0(self.channel, self.chipv)
        self.MACRWBT_COEX_WAIT1 = MACRWBT_COEX_WAIT1(self.channel, self.chipv)
        self.MACRWBT_COEX_DYNAMIC_PRIORITY = MACRWBT_COEX_DYNAMIC_PRIORITY(self.channel, self.chipv)
        self.MACRWBT_COEX_GPIO_SEL = MACRWBT_COEX_GPIO_SEL(self.channel, self.chipv)
        self.MACRWBT_COEX_TIMER0_CONF0 = MACRWBT_COEX_TIMER0_CONF0(self.channel, self.chipv)
        self.MACRWBT_COEX_TIMER0_CONF1 = MACRWBT_COEX_TIMER0_CONF1(self.channel, self.chipv)
        self.MACRWBT_COEX_TIMER1_CONF0 = MACRWBT_COEX_TIMER1_CONF0(self.channel, self.chipv)
        self.MACRWBT_COEX_TIMER1_CONF1 = MACRWBT_COEX_TIMER1_CONF1(self.channel, self.chipv)
        self.MACRWBT_COEX_TIMER2_CONF0 = MACRWBT_COEX_TIMER2_CONF0(self.channel, self.chipv)
        self.MACRWBT_COEX_TIMER2_CONF1 = MACRWBT_COEX_TIMER2_CONF1(self.channel, self.chipv)
        self.MACRWBT_COEX_TIMER3_CONF0 = MACRWBT_COEX_TIMER3_CONF0(self.channel, self.chipv)
        self.MACRWBT_COEX_TIMER3_CONF1 = MACRWBT_COEX_TIMER3_CONF1(self.channel, self.chipv)
        self.MACRWBT_COEX_TIMER4_CONF0 = MACRWBT_COEX_TIMER4_CONF0(self.channel, self.chipv)
        self.MACRWBT_COEX_TIMER4_CONF1 = MACRWBT_COEX_TIMER4_CONF1(self.channel, self.chipv)
        self.MACRWBT_COEX_TIMER5_CONF0 = MACRWBT_COEX_TIMER5_CONF0(self.channel, self.chipv)
        self.MACRWBT_COEX_TIMER5_CONF1 = MACRWBT_COEX_TIMER5_CONF1(self.channel, self.chipv)
        self.MACRWBT_COEX_TIMER6_CONF0 = MACRWBT_COEX_TIMER6_CONF0(self.channel, self.chipv)
        self.MACRWBT_COEX_TIMER6_CONF1 = MACRWBT_COEX_TIMER6_CONF1(self.channel, self.chipv)
        self.MACRWBT_COEX_TIMER7_CONF0 = MACRWBT_COEX_TIMER7_CONF0(self.channel, self.chipv)
        self.MACRWBT_COEX_TIMER7_CONF1 = MACRWBT_COEX_TIMER7_CONF1(self.channel, self.chipv)
        self.MACRWBT_COEX_TIMER8_CONF0 = MACRWBT_COEX_TIMER8_CONF0(self.channel, self.chipv)
        self.MACRWBT_COEX_TIMER8_CONF1 = MACRWBT_COEX_TIMER8_CONF1(self.channel, self.chipv)
        self.MACRWBT_COEX_TIMER9_CONF0 = MACRWBT_COEX_TIMER9_CONF0(self.channel, self.chipv)
        self.MACRWBT_COEX_TIMER9_CONF1 = MACRWBT_COEX_TIMER9_CONF1(self.channel, self.chipv)
        self.MACRWBT_COEX_TIMER10_CONF0 = MACRWBT_COEX_TIMER10_CONF0(self.channel, self.chipv)
        self.MACRWBT_COEX_TIMER10_CONF1 = MACRWBT_COEX_TIMER10_CONF1(self.channel, self.chipv)
        self.MACRWBT_COEX_TIMER11_CONF0 = MACRWBT_COEX_TIMER11_CONF0(self.channel, self.chipv)
        self.MACRWBT_COEX_TIMER11_CONF1 = MACRWBT_COEX_TIMER11_CONF1(self.channel, self.chipv)
        self.MACRWBT_COEX_TIMER_END_ST = MACRWBT_COEX_TIMER_END_ST(self.channel, self.chipv)
        self.MACRWBT_COEX_TIMER_END_CLR = MACRWBT_COEX_TIMER_END_CLR(self.channel, self.chipv)
        self.INT_ENA_MACPWR = INT_ENA_MACPWR(self.channel, self.chipv)
        self.INT_RAW_MACPWR = INT_RAW_MACPWR(self.channel, self.chipv)
        self.INT_ST_MACPWR = INT_ST_MACPWR(self.channel, self.chipv)
        self.INT_CLR_MACPWR = INT_CLR_MACPWR(self.channel, self.chipv)
        self.MACCO_EXTERN_CONF0 = MACCO_EXTERN_CONF0(self.channel, self.chipv)
        self.MACCO_EXTERN_CONF1 = MACCO_EXTERN_CONF1(self.channel, self.chipv)
        self.MACPWRDATE = MACPWRDATE(self.channel, self.chipv)
class MACTIME(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x0
        self.__reg_mactime_lsb = 0
        self.__reg_mactime_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_mactime(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mactime_msb, self.__reg_mactime_lsb)
    @reg_mactime.setter
    def reg_mactime(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mactime_msb, self.__reg_mactime_lsb, value)
class MACEMAC_TIMER_NS(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x4
        self.__emactimer_ns_lsb = 0
        self.__emactimer_ns_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def emactimer_ns(self):
        return self.__MEM.rdm(self.__addr, self.__emactimer_ns_msb, self.__emactimer_ns_lsb)
    @emactimer_ns.setter
    def emactimer_ns(self, value):
        return self.__MEM.wrm(self.__addr, self.__emactimer_ns_msb, self.__emactimer_ns_lsb, value)
class MACEMAC_TIMER_S(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x8
        self.__emactimer_s_lsb = 0
        self.__emactimer_s_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def emactimer_s(self):
        return self.__MEM.rdm(self.__addr, self.__emactimer_s_msb, self.__emactimer_s_lsb)
    @emactimer_s.setter
    def emactimer_s(self, value):
        return self.__MEM.wrm(self.__addr, self.__emactimer_s_msb, self.__emactimer_s_lsb, value)
class MACTIME_SW(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xc
        self.__reg_mactime_sw_lsb = 0
        self.__reg_mactime_sw_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_mactime_sw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mactime_sw_msb, self.__reg_mactime_sw_lsb)
    @reg_mactime_sw.setter
    def reg_mactime_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mactime_sw_msb, self.__reg_mactime_sw_lsb, value)
class MACTSF_TIME_FZ(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x10
        self.__reg_macsw_wr_lsb = 10
        self.__reg_macsw_wr_msb = 10
        self.__reg_tsf3sw_wr_lsb = 9
        self.__reg_tsf3sw_wr_msb = 9
        self.__reg_tsf2sw_wr_lsb = 8
        self.__reg_tsf2sw_wr_msb = 8
        self.__reg_tsf1sw_wr_lsb = 7
        self.__reg_tsf1sw_wr_msb = 7
        self.__reg_tsf0sw_wr_lsb = 6
        self.__reg_tsf0sw_wr_msb = 6
        self.__reg_emactime_fz_lsb = 5
        self.__reg_emactime_fz_msb = 5
        self.__reg_tsf3time_fz_lsb = 3
        self.__reg_tsf3time_fz_msb = 3
        self.__reg_tsf2time_fz_lsb = 2
        self.__reg_tsf2time_fz_msb = 2
        self.__reg_tsf1time_fz_lsb = 1
        self.__reg_tsf1time_fz_msb = 1
        self.__reg_tsf0time_fz_lsb = 0
        self.__reg_tsf0time_fz_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macsw_wr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macsw_wr_msb, self.__reg_macsw_wr_lsb)
    @reg_macsw_wr.setter
    def reg_macsw_wr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macsw_wr_msb, self.__reg_macsw_wr_lsb, value)

    @property
    def reg_tsf3sw_wr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf3sw_wr_msb, self.__reg_tsf3sw_wr_lsb)
    @reg_tsf3sw_wr.setter
    def reg_tsf3sw_wr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf3sw_wr_msb, self.__reg_tsf3sw_wr_lsb, value)

    @property
    def reg_tsf2sw_wr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf2sw_wr_msb, self.__reg_tsf2sw_wr_lsb)
    @reg_tsf2sw_wr.setter
    def reg_tsf2sw_wr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf2sw_wr_msb, self.__reg_tsf2sw_wr_lsb, value)

    @property
    def reg_tsf1sw_wr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf1sw_wr_msb, self.__reg_tsf1sw_wr_lsb)
    @reg_tsf1sw_wr.setter
    def reg_tsf1sw_wr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf1sw_wr_msb, self.__reg_tsf1sw_wr_lsb, value)

    @property
    def reg_tsf0sw_wr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf0sw_wr_msb, self.__reg_tsf0sw_wr_lsb)
    @reg_tsf0sw_wr.setter
    def reg_tsf0sw_wr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf0sw_wr_msb, self.__reg_tsf0sw_wr_lsb, value)

    @property
    def reg_emactime_fz(self):
        return self.__MEM.rdm(self.__addr, self.__reg_emactime_fz_msb, self.__reg_emactime_fz_lsb)
    @reg_emactime_fz.setter
    def reg_emactime_fz(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_emactime_fz_msb, self.__reg_emactime_fz_lsb, value)

    @property
    def reg_tsf3time_fz(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf3time_fz_msb, self.__reg_tsf3time_fz_lsb)
    @reg_tsf3time_fz.setter
    def reg_tsf3time_fz(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf3time_fz_msb, self.__reg_tsf3time_fz_lsb, value)

    @property
    def reg_tsf2time_fz(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf2time_fz_msb, self.__reg_tsf2time_fz_lsb)
    @reg_tsf2time_fz.setter
    def reg_tsf2time_fz(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf2time_fz_msb, self.__reg_tsf2time_fz_lsb, value)

    @property
    def reg_tsf1time_fz(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf1time_fz_msb, self.__reg_tsf1time_fz_lsb)
    @reg_tsf1time_fz.setter
    def reg_tsf1time_fz(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf1time_fz_msb, self.__reg_tsf1time_fz_lsb, value)

    @property
    def reg_tsf0time_fz(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf0time_fz_msb, self.__reg_tsf0time_fz_lsb)
    @reg_tsf0time_fz.setter
    def reg_tsf0time_fz(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf0time_fz_msb, self.__reg_tsf0time_fz_lsb, value)
class MACTSF0_TIME_LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x14
        self.__tsftime0_lo_lsb = 0
        self.__tsftime0_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tsftime0_lo(self):
        return self.__MEM.rdm(self.__addr, self.__tsftime0_lo_msb, self.__tsftime0_lo_lsb)
    @tsftime0_lo.setter
    def tsftime0_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsftime0_lo_msb, self.__tsftime0_lo_lsb, value)
class MACTSF0_TIME_HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x18
        self.__tsftime0_hi_lsb = 0
        self.__tsftime0_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tsftime0_hi(self):
        return self.__MEM.rdm(self.__addr, self.__tsftime0_hi_msb, self.__tsftime0_hi_lsb)
    @tsftime0_hi.setter
    def tsftime0_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsftime0_hi_msb, self.__tsftime0_hi_lsb, value)
class MACSLEEP_ST(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x1c
        self.__reg_mac_upbyrtc_lsb = 25
        self.__reg_mac_upbyrtc_msb = 25
        self.__reg_pwr_us_fix_lsb = 23
        self.__reg_pwr_us_fix_msb = 24
        self.__reg_digclk_div_lsb = 16
        self.__reg_digclk_div_msb = 22
        self.__reg_wakeup_early_lsb = 0
        self.__reg_wakeup_early_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_mac_upbyrtc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mac_upbyrtc_msb, self.__reg_mac_upbyrtc_lsb)
    @reg_mac_upbyrtc.setter
    def reg_mac_upbyrtc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mac_upbyrtc_msb, self.__reg_mac_upbyrtc_lsb, value)

    @property
    def reg_pwr_us_fix(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_us_fix_msb, self.__reg_pwr_us_fix_lsb)
    @reg_pwr_us_fix.setter
    def reg_pwr_us_fix(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_us_fix_msb, self.__reg_pwr_us_fix_lsb, value)

    @property
    def reg_digclk_div(self):
        return self.__MEM.rdm(self.__addr, self.__reg_digclk_div_msb, self.__reg_digclk_div_lsb)
    @reg_digclk_div.setter
    def reg_digclk_div(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_digclk_div_msb, self.__reg_digclk_div_lsb, value)

    @property
    def reg_wakeup_early(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wakeup_early_msb, self.__reg_wakeup_early_lsb)
    @reg_wakeup_early.setter
    def reg_wakeup_early(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wakeup_early_msb, self.__reg_wakeup_early_lsb, value)
class MACSLEEP0_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x20
        self.__reg_tsfup0_ena_lsb = 31
        self.__reg_tsfup0_ena_msb = 31
        self.__reg_txbeacon0_ena_lsb = 30
        self.__reg_txbeacon0_ena_msb = 30
        self.__reg_wakeup0_ena_lsb = 29
        self.__reg_wakeup0_ena_msb = 29
        self.__reg_tsf0rtcup_ena_lsb = 28
        self.__reg_tsf0rtcup_ena_msb = 28
        self.__reg_tsf0hwup_ena_lsb = 27
        self.__reg_tsf0hwup_ena_msb = 27
        self.__reg_beacon_target0_valid_lsb = 25
        self.__reg_beacon_target0_valid_msb = 25
        self.__reg_pwrclk_en_lsb = 23
        self.__reg_pwrclk_en_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tsfup0_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsfup0_ena_msb, self.__reg_tsfup0_ena_lsb)
    @reg_tsfup0_ena.setter
    def reg_tsfup0_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsfup0_ena_msb, self.__reg_tsfup0_ena_lsb, value)

    @property
    def reg_txbeacon0_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txbeacon0_ena_msb, self.__reg_txbeacon0_ena_lsb)
    @reg_txbeacon0_ena.setter
    def reg_txbeacon0_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txbeacon0_ena_msb, self.__reg_txbeacon0_ena_lsb, value)

    @property
    def reg_wakeup0_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wakeup0_ena_msb, self.__reg_wakeup0_ena_lsb)
    @reg_wakeup0_ena.setter
    def reg_wakeup0_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wakeup0_ena_msb, self.__reg_wakeup0_ena_lsb, value)

    @property
    def reg_tsf0rtcup_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf0rtcup_ena_msb, self.__reg_tsf0rtcup_ena_lsb)
    @reg_tsf0rtcup_ena.setter
    def reg_tsf0rtcup_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf0rtcup_ena_msb, self.__reg_tsf0rtcup_ena_lsb, value)

    @property
    def reg_tsf0hwup_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf0hwup_ena_msb, self.__reg_tsf0hwup_ena_lsb)
    @reg_tsf0hwup_ena.setter
    def reg_tsf0hwup_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf0hwup_ena_msb, self.__reg_tsf0hwup_ena_lsb, value)

    @property
    def reg_beacon_target0_valid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacon_target0_valid_msb, self.__reg_beacon_target0_valid_lsb)
    @reg_beacon_target0_valid.setter
    def reg_beacon_target0_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacon_target0_valid_msb, self.__reg_beacon_target0_valid_lsb, value)

    @property
    def reg_pwrclk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwrclk_en_msb, self.__reg_pwrclk_en_lsb)
    @reg_pwrclk_en.setter
    def reg_pwrclk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwrclk_en_msb, self.__reg_pwrclk_en_lsb, value)
class MACTSF0_ACTIVE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x24
        self.__tsf0_active_st_lsb = 1
        self.__tsf0_active_st_msb = 1
        self.__reg_tsf0_active_clr_lsb = 0
        self.__reg_tsf0_active_clr_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tsf0_active_st(self):
        return self.__MEM.rdm(self.__addr, self.__tsf0_active_st_msb, self.__tsf0_active_st_lsb)
    @tsf0_active_st.setter
    def tsf0_active_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsf0_active_st_msb, self.__tsf0_active_st_lsb, value)

    @property
    def reg_tsf0_active_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf0_active_clr_msb, self.__reg_tsf0_active_clr_lsb)
    @reg_tsf0_active_clr.setter
    def reg_tsf0_active_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf0_active_clr_msb, self.__reg_tsf0_active_clr_lsb, value)
class MACTSFSW0_LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x28
        self.__reg_tsfupsw0_lo_lsb = 0
        self.__reg_tsfupsw0_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tsfupsw0_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsfupsw0_lo_msb, self.__reg_tsfupsw0_lo_lsb)
    @reg_tsfupsw0_lo.setter
    def reg_tsfupsw0_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsfupsw0_lo_msb, self.__reg_tsfupsw0_lo_lsb, value)
class MACTSFSW0_HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x2c
        self.__reg_tsfupsw0_hi_lsb = 0
        self.__reg_tsfupsw0_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tsfupsw0_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsfupsw0_hi_msb, self.__reg_tsfupsw0_hi_lsb)
    @reg_tsfupsw0_hi.setter
    def reg_tsfupsw0_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsfupsw0_hi_msb, self.__reg_tsfupsw0_hi_lsb, value)
class MACBEACTAR0_LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x30
        self.__reg_beacstart_target0_lo_lsb = 0
        self.__reg_beacstart_target0_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_beacstart_target0_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacstart_target0_lo_msb, self.__reg_beacstart_target0_lo_lsb)
    @reg_beacstart_target0_lo.setter
    def reg_beacstart_target0_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacstart_target0_lo_msb, self.__reg_beacstart_target0_lo_lsb, value)
class MACBEACTAR0_HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x34
        self.__reg_beacstart_target0_hi_lsb = 0
        self.__reg_beacstart_target0_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_beacstart_target0_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacstart_target0_hi_msb, self.__reg_beacstart_target0_hi_lsb)
    @reg_beacstart_target0_hi.setter
    def reg_beacstart_target0_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacstart_target0_hi_msb, self.__reg_beacstart_target0_hi_lsb, value)
class MACBEATAR0_LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x38
        self.__reg_beacon_target0_lo_lsb = 0
        self.__reg_beacon_target0_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_beacon_target0_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacon_target0_lo_msb, self.__reg_beacon_target0_lo_lsb)
    @reg_beacon_target0_lo.setter
    def reg_beacon_target0_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacon_target0_lo_msb, self.__reg_beacon_target0_lo_lsb, value)
class MACBEATAR0_HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x3c
        self.__reg_beacon_target0_hi_lsb = 0
        self.__reg_beacon_target0_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_beacon_target0_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacon_target0_hi_msb, self.__reg_beacon_target0_hi_lsb)
    @reg_beacon_target0_hi.setter
    def reg_beacon_target0_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacon_target0_hi_msb, self.__reg_beacon_target0_hi_lsb, value)
class MACBEA_CUR_TAR0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x40
        self.__beacon_cur_tar0_lsb = 0
        self.__beacon_cur_tar0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def beacon_cur_tar0(self):
        return self.__MEM.rdm(self.__addr, self.__beacon_cur_tar0_msb, self.__beacon_cur_tar0_lsb)
    @beacon_cur_tar0.setter
    def beacon_cur_tar0(self, value):
        return self.__MEM.wrm(self.__addr, self.__beacon_cur_tar0_msb, self.__beacon_cur_tar0_lsb, value)
class MACBEAINTER0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x44
        self.__reg_tbtt0_early_time_lsb = 16
        self.__reg_tbtt0_early_time_msb = 31
        self.__reg_tbtt0_lsb = 0
        self.__reg_tbtt0_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tbtt0_early_time(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tbtt0_early_time_msb, self.__reg_tbtt0_early_time_lsb)
    @reg_tbtt0_early_time.setter
    def reg_tbtt0_early_time(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tbtt0_early_time_msb, self.__reg_tbtt0_early_time_lsb, value)

    @property
    def reg_tbtt0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tbtt0_msb, self.__reg_tbtt0_lsb)
    @reg_tbtt0.setter
    def reg_tbtt0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tbtt0_msb, self.__reg_tbtt0_lsb, value)
class MACTSF1_TIME_LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x48
        self.__tsftime1_lo_lsb = 0
        self.__tsftime1_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tsftime1_lo(self):
        return self.__MEM.rdm(self.__addr, self.__tsftime1_lo_msb, self.__tsftime1_lo_lsb)
    @tsftime1_lo.setter
    def tsftime1_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsftime1_lo_msb, self.__tsftime1_lo_lsb, value)
class MACTSF1_TIME_HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x4c
        self.__tsftime1_hi_lsb = 0
        self.__tsftime1_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tsftime1_hi(self):
        return self.__MEM.rdm(self.__addr, self.__tsftime1_hi_msb, self.__tsftime1_hi_lsb)
    @tsftime1_hi.setter
    def tsftime1_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsftime1_hi_msb, self.__tsftime1_hi_lsb, value)
class MACSLEEP1_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x50
        self.__reg_tsfup1_ena_lsb = 31
        self.__reg_tsfup1_ena_msb = 31
        self.__reg_txbeacon1_ena_lsb = 30
        self.__reg_txbeacon1_ena_msb = 30
        self.__reg_wakeup1_ena_lsb = 29
        self.__reg_wakeup1_ena_msb = 29
        self.__reg_tsf1rtcup_ena_lsb = 28
        self.__reg_tsf1rtcup_ena_msb = 28
        self.__reg_tsf1hwup_ena_lsb = 27
        self.__reg_tsf1hwup_ena_msb = 27
        self.__reg_beacon_target1_valid_lsb = 25
        self.__reg_beacon_target1_valid_msb = 25
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tsfup1_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsfup1_ena_msb, self.__reg_tsfup1_ena_lsb)
    @reg_tsfup1_ena.setter
    def reg_tsfup1_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsfup1_ena_msb, self.__reg_tsfup1_ena_lsb, value)

    @property
    def reg_txbeacon1_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txbeacon1_ena_msb, self.__reg_txbeacon1_ena_lsb)
    @reg_txbeacon1_ena.setter
    def reg_txbeacon1_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txbeacon1_ena_msb, self.__reg_txbeacon1_ena_lsb, value)

    @property
    def reg_wakeup1_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wakeup1_ena_msb, self.__reg_wakeup1_ena_lsb)
    @reg_wakeup1_ena.setter
    def reg_wakeup1_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wakeup1_ena_msb, self.__reg_wakeup1_ena_lsb, value)

    @property
    def reg_tsf1rtcup_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf1rtcup_ena_msb, self.__reg_tsf1rtcup_ena_lsb)
    @reg_tsf1rtcup_ena.setter
    def reg_tsf1rtcup_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf1rtcup_ena_msb, self.__reg_tsf1rtcup_ena_lsb, value)

    @property
    def reg_tsf1hwup_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf1hwup_ena_msb, self.__reg_tsf1hwup_ena_lsb)
    @reg_tsf1hwup_ena.setter
    def reg_tsf1hwup_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf1hwup_ena_msb, self.__reg_tsf1hwup_ena_lsb, value)

    @property
    def reg_beacon_target1_valid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacon_target1_valid_msb, self.__reg_beacon_target1_valid_lsb)
    @reg_beacon_target1_valid.setter
    def reg_beacon_target1_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacon_target1_valid_msb, self.__reg_beacon_target1_valid_lsb, value)
class MACTSF1_ACTIVE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x54
        self.__tsf1_active_st_lsb = 1
        self.__tsf1_active_st_msb = 1
        self.__reg_tsf1_active_clr_lsb = 0
        self.__reg_tsf1_active_clr_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tsf1_active_st(self):
        return self.__MEM.rdm(self.__addr, self.__tsf1_active_st_msb, self.__tsf1_active_st_lsb)
    @tsf1_active_st.setter
    def tsf1_active_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsf1_active_st_msb, self.__tsf1_active_st_lsb, value)

    @property
    def reg_tsf1_active_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf1_active_clr_msb, self.__reg_tsf1_active_clr_lsb)
    @reg_tsf1_active_clr.setter
    def reg_tsf1_active_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf1_active_clr_msb, self.__reg_tsf1_active_clr_lsb, value)
class MACTSFSW1_LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x58
        self.__reg_tsfupsw1_lo_lsb = 0
        self.__reg_tsfupsw1_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tsfupsw1_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsfupsw1_lo_msb, self.__reg_tsfupsw1_lo_lsb)
    @reg_tsfupsw1_lo.setter
    def reg_tsfupsw1_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsfupsw1_lo_msb, self.__reg_tsfupsw1_lo_lsb, value)
class MACTSFSW1_HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x5c
        self.__reg_tsfupsw1_hi_lsb = 0
        self.__reg_tsfupsw1_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tsfupsw1_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsfupsw1_hi_msb, self.__reg_tsfupsw1_hi_lsb)
    @reg_tsfupsw1_hi.setter
    def reg_tsfupsw1_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsfupsw1_hi_msb, self.__reg_tsfupsw1_hi_lsb, value)
class MACBEACTAR1_LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x60
        self.__reg_beacstart_target1_lo_lsb = 0
        self.__reg_beacstart_target1_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_beacstart_target1_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacstart_target1_lo_msb, self.__reg_beacstart_target1_lo_lsb)
    @reg_beacstart_target1_lo.setter
    def reg_beacstart_target1_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacstart_target1_lo_msb, self.__reg_beacstart_target1_lo_lsb, value)
class MACBEACTAR1_HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x64
        self.__reg_beacstart_target1_hi_lsb = 0
        self.__reg_beacstart_target1_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_beacstart_target1_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacstart_target1_hi_msb, self.__reg_beacstart_target1_hi_lsb)
    @reg_beacstart_target1_hi.setter
    def reg_beacstart_target1_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacstart_target1_hi_msb, self.__reg_beacstart_target1_hi_lsb, value)
class MACBEATAR1_LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x68
        self.__reg_beacon_target1_lo_lsb = 0
        self.__reg_beacon_target1_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_beacon_target1_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacon_target1_lo_msb, self.__reg_beacon_target1_lo_lsb)
    @reg_beacon_target1_lo.setter
    def reg_beacon_target1_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacon_target1_lo_msb, self.__reg_beacon_target1_lo_lsb, value)
class MACBEATAR1_HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x6c
        self.__reg_beacon_target1_hi_lsb = 0
        self.__reg_beacon_target1_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_beacon_target1_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacon_target1_hi_msb, self.__reg_beacon_target1_hi_lsb)
    @reg_beacon_target1_hi.setter
    def reg_beacon_target1_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacon_target1_hi_msb, self.__reg_beacon_target1_hi_lsb, value)
class MACBEA_CUR_TAR1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x70
        self.__beacon_cur_tar1_lsb = 0
        self.__beacon_cur_tar1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def beacon_cur_tar1(self):
        return self.__MEM.rdm(self.__addr, self.__beacon_cur_tar1_msb, self.__beacon_cur_tar1_lsb)
    @beacon_cur_tar1.setter
    def beacon_cur_tar1(self, value):
        return self.__MEM.wrm(self.__addr, self.__beacon_cur_tar1_msb, self.__beacon_cur_tar1_lsb, value)
class MACBEAINTER1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x74
        self.__reg_tbtt1_early_time_lsb = 16
        self.__reg_tbtt1_early_time_msb = 31
        self.__reg_tbtt1_lsb = 0
        self.__reg_tbtt1_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tbtt1_early_time(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tbtt1_early_time_msb, self.__reg_tbtt1_early_time_lsb)
    @reg_tbtt1_early_time.setter
    def reg_tbtt1_early_time(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tbtt1_early_time_msb, self.__reg_tbtt1_early_time_lsb, value)

    @property
    def reg_tbtt1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tbtt1_msb, self.__reg_tbtt1_lsb)
    @reg_tbtt1.setter
    def reg_tbtt1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tbtt1_msb, self.__reg_tbtt1_lsb, value)
class MACTSF2_TIME_LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x78
        self.__tsftime2_lo_lsb = 0
        self.__tsftime2_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tsftime2_lo(self):
        return self.__MEM.rdm(self.__addr, self.__tsftime2_lo_msb, self.__tsftime2_lo_lsb)
    @tsftime2_lo.setter
    def tsftime2_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsftime2_lo_msb, self.__tsftime2_lo_lsb, value)
class MACTSF2_TIME_HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x7c
        self.__tsftime2_hi_lsb = 0
        self.__tsftime2_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tsftime2_hi(self):
        return self.__MEM.rdm(self.__addr, self.__tsftime2_hi_msb, self.__tsftime2_hi_lsb)
    @tsftime2_hi.setter
    def tsftime2_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsftime2_hi_msb, self.__tsftime2_hi_lsb, value)
class MACSLEEP2_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x80
        self.__reg_tsfup2_ena_lsb = 31
        self.__reg_tsfup2_ena_msb = 31
        self.__reg_txbeacon2_ena_lsb = 30
        self.__reg_txbeacon2_ena_msb = 30
        self.__reg_wakeup2_ena_lsb = 29
        self.__reg_wakeup2_ena_msb = 29
        self.__reg_tsf2rtcup_ena_lsb = 28
        self.__reg_tsf2rtcup_ena_msb = 28
        self.__reg_tsf2hwup_ena_lsb = 27
        self.__reg_tsf2hwup_ena_msb = 27
        self.__reg_beacon_target2_valid_lsb = 25
        self.__reg_beacon_target2_valid_msb = 25
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tsfup2_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsfup2_ena_msb, self.__reg_tsfup2_ena_lsb)
    @reg_tsfup2_ena.setter
    def reg_tsfup2_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsfup2_ena_msb, self.__reg_tsfup2_ena_lsb, value)

    @property
    def reg_txbeacon2_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txbeacon2_ena_msb, self.__reg_txbeacon2_ena_lsb)
    @reg_txbeacon2_ena.setter
    def reg_txbeacon2_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txbeacon2_ena_msb, self.__reg_txbeacon2_ena_lsb, value)

    @property
    def reg_wakeup2_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wakeup2_ena_msb, self.__reg_wakeup2_ena_lsb)
    @reg_wakeup2_ena.setter
    def reg_wakeup2_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wakeup2_ena_msb, self.__reg_wakeup2_ena_lsb, value)

    @property
    def reg_tsf2rtcup_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf2rtcup_ena_msb, self.__reg_tsf2rtcup_ena_lsb)
    @reg_tsf2rtcup_ena.setter
    def reg_tsf2rtcup_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf2rtcup_ena_msb, self.__reg_tsf2rtcup_ena_lsb, value)

    @property
    def reg_tsf2hwup_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf2hwup_ena_msb, self.__reg_tsf2hwup_ena_lsb)
    @reg_tsf2hwup_ena.setter
    def reg_tsf2hwup_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf2hwup_ena_msb, self.__reg_tsf2hwup_ena_lsb, value)

    @property
    def reg_beacon_target2_valid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacon_target2_valid_msb, self.__reg_beacon_target2_valid_lsb)
    @reg_beacon_target2_valid.setter
    def reg_beacon_target2_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacon_target2_valid_msb, self.__reg_beacon_target2_valid_lsb, value)
class MACTSF2_ACTIVE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x84
        self.__tsf2_active_st_lsb = 1
        self.__tsf2_active_st_msb = 1
        self.__reg_tsf2_active_clr_lsb = 0
        self.__reg_tsf2_active_clr_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tsf2_active_st(self):
        return self.__MEM.rdm(self.__addr, self.__tsf2_active_st_msb, self.__tsf2_active_st_lsb)
    @tsf2_active_st.setter
    def tsf2_active_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsf2_active_st_msb, self.__tsf2_active_st_lsb, value)

    @property
    def reg_tsf2_active_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf2_active_clr_msb, self.__reg_tsf2_active_clr_lsb)
    @reg_tsf2_active_clr.setter
    def reg_tsf2_active_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf2_active_clr_msb, self.__reg_tsf2_active_clr_lsb, value)
class MACTSFSW2_LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x88
        self.__reg_tsfupsw2_lo_lsb = 0
        self.__reg_tsfupsw2_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tsfupsw2_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsfupsw2_lo_msb, self.__reg_tsfupsw2_lo_lsb)
    @reg_tsfupsw2_lo.setter
    def reg_tsfupsw2_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsfupsw2_lo_msb, self.__reg_tsfupsw2_lo_lsb, value)
class MACTSFSW2_HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x8c
        self.__reg_tsfupsw2_hi_lsb = 0
        self.__reg_tsfupsw2_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tsfupsw2_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsfupsw2_hi_msb, self.__reg_tsfupsw2_hi_lsb)
    @reg_tsfupsw2_hi.setter
    def reg_tsfupsw2_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsfupsw2_hi_msb, self.__reg_tsfupsw2_hi_lsb, value)
class MACBEACTAR2_LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x90
        self.__reg_beacstart_target2_lo_lsb = 0
        self.__reg_beacstart_target2_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_beacstart_target2_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacstart_target2_lo_msb, self.__reg_beacstart_target2_lo_lsb)
    @reg_beacstart_target2_lo.setter
    def reg_beacstart_target2_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacstart_target2_lo_msb, self.__reg_beacstart_target2_lo_lsb, value)
class MACBEACTAR2_HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x94
        self.__reg_beacstart_target2_hi_lsb = 0
        self.__reg_beacstart_target2_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_beacstart_target2_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacstart_target2_hi_msb, self.__reg_beacstart_target2_hi_lsb)
    @reg_beacstart_target2_hi.setter
    def reg_beacstart_target2_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacstart_target2_hi_msb, self.__reg_beacstart_target2_hi_lsb, value)
class MACBEATAR2_LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x98
        self.__reg_beacon_target2_lo_lsb = 0
        self.__reg_beacon_target2_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_beacon_target2_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacon_target2_lo_msb, self.__reg_beacon_target2_lo_lsb)
    @reg_beacon_target2_lo.setter
    def reg_beacon_target2_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacon_target2_lo_msb, self.__reg_beacon_target2_lo_lsb, value)
class MACBEATAR2_HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x9c
        self.__reg_beacon_target2_hi_lsb = 0
        self.__reg_beacon_target2_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_beacon_target2_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacon_target2_hi_msb, self.__reg_beacon_target2_hi_lsb)
    @reg_beacon_target2_hi.setter
    def reg_beacon_target2_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacon_target2_hi_msb, self.__reg_beacon_target2_hi_lsb, value)
class MACBEA_CUR_TAR2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xa0
        self.__beacon_cur_tar2_lsb = 0
        self.__beacon_cur_tar2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def beacon_cur_tar2(self):
        return self.__MEM.rdm(self.__addr, self.__beacon_cur_tar2_msb, self.__beacon_cur_tar2_lsb)
    @beacon_cur_tar2.setter
    def beacon_cur_tar2(self, value):
        return self.__MEM.wrm(self.__addr, self.__beacon_cur_tar2_msb, self.__beacon_cur_tar2_lsb, value)
class MACBEAINTER2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xa4
        self.__reg_tbtt2_early_time_lsb = 16
        self.__reg_tbtt2_early_time_msb = 31
        self.__reg_tbtt2_lsb = 0
        self.__reg_tbtt2_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tbtt2_early_time(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tbtt2_early_time_msb, self.__reg_tbtt2_early_time_lsb)
    @reg_tbtt2_early_time.setter
    def reg_tbtt2_early_time(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tbtt2_early_time_msb, self.__reg_tbtt2_early_time_lsb, value)

    @property
    def reg_tbtt2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tbtt2_msb, self.__reg_tbtt2_lsb)
    @reg_tbtt2.setter
    def reg_tbtt2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tbtt2_msb, self.__reg_tbtt2_lsb, value)
class MACTSF3_TIME_LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xa8
        self.__tsftime3_lo_lsb = 0
        self.__tsftime3_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tsftime3_lo(self):
        return self.__MEM.rdm(self.__addr, self.__tsftime3_lo_msb, self.__tsftime3_lo_lsb)
    @tsftime3_lo.setter
    def tsftime3_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsftime3_lo_msb, self.__tsftime3_lo_lsb, value)
class MACTSF3_TIME_HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xac
        self.__tsftime3_hi_lsb = 0
        self.__tsftime3_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tsftime3_hi(self):
        return self.__MEM.rdm(self.__addr, self.__tsftime3_hi_msb, self.__tsftime3_hi_lsb)
    @tsftime3_hi.setter
    def tsftime3_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsftime3_hi_msb, self.__tsftime3_hi_lsb, value)
class MACSLEEP3_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xb0
        self.__reg_tsfup3_ena_lsb = 31
        self.__reg_tsfup3_ena_msb = 31
        self.__reg_txbeacon3_ena_lsb = 30
        self.__reg_txbeacon3_ena_msb = 30
        self.__reg_wakeup3_ena_lsb = 29
        self.__reg_wakeup3_ena_msb = 29
        self.__reg_tsf3rtcup_ena_lsb = 28
        self.__reg_tsf3rtcup_ena_msb = 28
        self.__reg_tsf3hwup_ena_lsb = 27
        self.__reg_tsf3hwup_ena_msb = 27
        self.__reg_beacon_target3_valid_lsb = 25
        self.__reg_beacon_target3_valid_msb = 25
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tsfup3_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsfup3_ena_msb, self.__reg_tsfup3_ena_lsb)
    @reg_tsfup3_ena.setter
    def reg_tsfup3_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsfup3_ena_msb, self.__reg_tsfup3_ena_lsb, value)

    @property
    def reg_txbeacon3_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txbeacon3_ena_msb, self.__reg_txbeacon3_ena_lsb)
    @reg_txbeacon3_ena.setter
    def reg_txbeacon3_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txbeacon3_ena_msb, self.__reg_txbeacon3_ena_lsb, value)

    @property
    def reg_wakeup3_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wakeup3_ena_msb, self.__reg_wakeup3_ena_lsb)
    @reg_wakeup3_ena.setter
    def reg_wakeup3_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wakeup3_ena_msb, self.__reg_wakeup3_ena_lsb, value)

    @property
    def reg_tsf3rtcup_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf3rtcup_ena_msb, self.__reg_tsf3rtcup_ena_lsb)
    @reg_tsf3rtcup_ena.setter
    def reg_tsf3rtcup_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf3rtcup_ena_msb, self.__reg_tsf3rtcup_ena_lsb, value)

    @property
    def reg_tsf3hwup_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf3hwup_ena_msb, self.__reg_tsf3hwup_ena_lsb)
    @reg_tsf3hwup_ena.setter
    def reg_tsf3hwup_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf3hwup_ena_msb, self.__reg_tsf3hwup_ena_lsb, value)

    @property
    def reg_beacon_target3_valid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacon_target3_valid_msb, self.__reg_beacon_target3_valid_lsb)
    @reg_beacon_target3_valid.setter
    def reg_beacon_target3_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacon_target3_valid_msb, self.__reg_beacon_target3_valid_lsb, value)
class MACTSF3_ACTIVE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xb4
        self.__tsf3_active_st_lsb = 1
        self.__tsf3_active_st_msb = 1
        self.__reg_tsf3_active_clr_lsb = 0
        self.__reg_tsf3_active_clr_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tsf3_active_st(self):
        return self.__MEM.rdm(self.__addr, self.__tsf3_active_st_msb, self.__tsf3_active_st_lsb)
    @tsf3_active_st.setter
    def tsf3_active_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsf3_active_st_msb, self.__tsf3_active_st_lsb, value)

    @property
    def reg_tsf3_active_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf3_active_clr_msb, self.__reg_tsf3_active_clr_lsb)
    @reg_tsf3_active_clr.setter
    def reg_tsf3_active_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf3_active_clr_msb, self.__reg_tsf3_active_clr_lsb, value)
class MACTSFSW3_LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xb8
        self.__reg_tsfupsw3_lo_lsb = 0
        self.__reg_tsfupsw3_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tsfupsw3_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsfupsw3_lo_msb, self.__reg_tsfupsw3_lo_lsb)
    @reg_tsfupsw3_lo.setter
    def reg_tsfupsw3_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsfupsw3_lo_msb, self.__reg_tsfupsw3_lo_lsb, value)
class MACTSFSW3_HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xbc
        self.__reg_tsfupsw3_hi_lsb = 0
        self.__reg_tsfupsw3_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tsfupsw3_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsfupsw3_hi_msb, self.__reg_tsfupsw3_hi_lsb)
    @reg_tsfupsw3_hi.setter
    def reg_tsfupsw3_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsfupsw3_hi_msb, self.__reg_tsfupsw3_hi_lsb, value)
class MACBEACTAR3_LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xc0
        self.__reg_beacstart_target3_lo_lsb = 0
        self.__reg_beacstart_target3_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_beacstart_target3_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacstart_target3_lo_msb, self.__reg_beacstart_target3_lo_lsb)
    @reg_beacstart_target3_lo.setter
    def reg_beacstart_target3_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacstart_target3_lo_msb, self.__reg_beacstart_target3_lo_lsb, value)
class MACBEACTAR3_HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xc4
        self.__reg_beacstart_target3_hi_lsb = 0
        self.__reg_beacstart_target3_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_beacstart_target3_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacstart_target3_hi_msb, self.__reg_beacstart_target3_hi_lsb)
    @reg_beacstart_target3_hi.setter
    def reg_beacstart_target3_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacstart_target3_hi_msb, self.__reg_beacstart_target3_hi_lsb, value)
class MACBEATAR3_LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xc8
        self.__reg_beacon_target3_lo_lsb = 0
        self.__reg_beacon_target3_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_beacon_target3_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacon_target3_lo_msb, self.__reg_beacon_target3_lo_lsb)
    @reg_beacon_target3_lo.setter
    def reg_beacon_target3_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacon_target3_lo_msb, self.__reg_beacon_target3_lo_lsb, value)
class MACBEATAR3_HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xcc
        self.__reg_beacon_target3_hi_lsb = 0
        self.__reg_beacon_target3_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_beacon_target3_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacon_target3_hi_msb, self.__reg_beacon_target3_hi_lsb)
    @reg_beacon_target3_hi.setter
    def reg_beacon_target3_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacon_target3_hi_msb, self.__reg_beacon_target3_hi_lsb, value)
class MACBEA_CUR_TAR3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xd0
        self.__beacon_cur_tar3_lsb = 0
        self.__beacon_cur_tar3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def beacon_cur_tar3(self):
        return self.__MEM.rdm(self.__addr, self.__beacon_cur_tar3_msb, self.__beacon_cur_tar3_lsb)
    @beacon_cur_tar3.setter
    def beacon_cur_tar3(self, value):
        return self.__MEM.wrm(self.__addr, self.__beacon_cur_tar3_msb, self.__beacon_cur_tar3_lsb, value)
class MACBEAINTER3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xd4
        self.__reg_tbtt3_early_time_lsb = 16
        self.__reg_tbtt3_early_time_msb = 31
        self.__reg_tbtt3_lsb = 0
        self.__reg_tbtt3_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tbtt3_early_time(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tbtt3_early_time_msb, self.__reg_tbtt3_early_time_lsb)
    @reg_tbtt3_early_time.setter
    def reg_tbtt3_early_time(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tbtt3_early_time_msb, self.__reg_tbtt3_early_time_lsb, value)

    @property
    def reg_tbtt3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tbtt3_msb, self.__reg_tbtt3_lsb)
    @reg_tbtt3.setter
    def reg_tbtt3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tbtt3_msb, self.__reg_tbtt3_lsb, value)
class MACRTC_CALISW(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xd8
        self.__reg_calisw_value_lsb = 0
        self.__reg_calisw_value_msb = 17
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_calisw_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_calisw_value_msb, self.__reg_calisw_value_lsb)
    @reg_calisw_value.setter
    def reg_calisw_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_calisw_value_msb, self.__reg_calisw_value_lsb, value)
class MACTSF0TIMER_ENA(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xdc
        self.__reg_tsf0timer_ena_lsb = 31
        self.__reg_tsf0timer_ena_msb = 31
        self.__reg_tsf0timer_wakeup_ena_lsb = 30
        self.__reg_tsf0timer_wakeup_ena_msb = 30
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tsf0timer_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf0timer_ena_msb, self.__reg_tsf0timer_ena_lsb)
    @reg_tsf0timer_ena.setter
    def reg_tsf0timer_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf0timer_ena_msb, self.__reg_tsf0timer_ena_lsb, value)

    @property
    def reg_tsf0timer_wakeup_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf0timer_wakeup_ena_msb, self.__reg_tsf0timer_wakeup_ena_lsb)
    @reg_tsf0timer_wakeup_ena.setter
    def reg_tsf0timer_wakeup_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf0timer_wakeup_ena_msb, self.__reg_tsf0timer_wakeup_ena_lsb, value)
class MACTSF0_TIMER_LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xe0
        self.__reg_tsf0timer_lo_lsb = 0
        self.__reg_tsf0timer_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tsf0timer_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf0timer_lo_msb, self.__reg_tsf0timer_lo_lsb)
    @reg_tsf0timer_lo.setter
    def reg_tsf0timer_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf0timer_lo_msb, self.__reg_tsf0timer_lo_lsb, value)
class MACTSF0_TIMER_HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xe4
        self.__reg_tsf0timer_hi_lsb = 0
        self.__reg_tsf0timer_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tsf0timer_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf0timer_hi_msb, self.__reg_tsf0timer_hi_lsb)
    @reg_tsf0timer_hi.setter
    def reg_tsf0timer_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf0timer_hi_msb, self.__reg_tsf0timer_hi_lsb, value)
class MACTSF1TIMER_ENA(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xe8
        self.__reg_tsf1timer_ena_lsb = 31
        self.__reg_tsf1timer_ena_msb = 31
        self.__reg_tsf1timer_wakeup_ena_lsb = 30
        self.__reg_tsf1timer_wakeup_ena_msb = 30
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tsf1timer_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf1timer_ena_msb, self.__reg_tsf1timer_ena_lsb)
    @reg_tsf1timer_ena.setter
    def reg_tsf1timer_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf1timer_ena_msb, self.__reg_tsf1timer_ena_lsb, value)

    @property
    def reg_tsf1timer_wakeup_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf1timer_wakeup_ena_msb, self.__reg_tsf1timer_wakeup_ena_lsb)
    @reg_tsf1timer_wakeup_ena.setter
    def reg_tsf1timer_wakeup_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf1timer_wakeup_ena_msb, self.__reg_tsf1timer_wakeup_ena_lsb, value)
class MACTSF1_TIMER_LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xec
        self.__reg_tsf1timer_lo_lsb = 0
        self.__reg_tsf1timer_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tsf1timer_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf1timer_lo_msb, self.__reg_tsf1timer_lo_lsb)
    @reg_tsf1timer_lo.setter
    def reg_tsf1timer_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf1timer_lo_msb, self.__reg_tsf1timer_lo_lsb, value)
class MACTSF1_TIMER_HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xf0
        self.__reg_tsf1timer_hi_lsb = 0
        self.__reg_tsf1timer_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tsf1timer_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf1timer_hi_msb, self.__reg_tsf1timer_hi_lsb)
    @reg_tsf1timer_hi.setter
    def reg_tsf1timer_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf1timer_hi_msb, self.__reg_tsf1timer_hi_lsb, value)
class MACTSF2TIMER_ENA(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xf4
        self.__reg_tsf2timer_ena_lsb = 31
        self.__reg_tsf2timer_ena_msb = 31
        self.__reg_tsf2timer_wakeup_ena_lsb = 30
        self.__reg_tsf2timer_wakeup_ena_msb = 30
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tsf2timer_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf2timer_ena_msb, self.__reg_tsf2timer_ena_lsb)
    @reg_tsf2timer_ena.setter
    def reg_tsf2timer_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf2timer_ena_msb, self.__reg_tsf2timer_ena_lsb, value)

    @property
    def reg_tsf2timer_wakeup_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf2timer_wakeup_ena_msb, self.__reg_tsf2timer_wakeup_ena_lsb)
    @reg_tsf2timer_wakeup_ena.setter
    def reg_tsf2timer_wakeup_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf2timer_wakeup_ena_msb, self.__reg_tsf2timer_wakeup_ena_lsb, value)
class MACTSF2_TIMER_LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xf8
        self.__reg_tsf2timer_lo_lsb = 0
        self.__reg_tsf2timer_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tsf2timer_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf2timer_lo_msb, self.__reg_tsf2timer_lo_lsb)
    @reg_tsf2timer_lo.setter
    def reg_tsf2timer_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf2timer_lo_msb, self.__reg_tsf2timer_lo_lsb, value)
class MACTSF2_TIMER_HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xfc
        self.__reg_tsf2timer_hi_lsb = 0
        self.__reg_tsf2timer_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tsf2timer_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf2timer_hi_msb, self.__reg_tsf2timer_hi_lsb)
    @reg_tsf2timer_hi.setter
    def reg_tsf2timer_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf2timer_hi_msb, self.__reg_tsf2timer_hi_lsb, value)
class MACTSF3TIMER_ENA(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x100
        self.__reg_tsf3timer_ena_lsb = 31
        self.__reg_tsf3timer_ena_msb = 31
        self.__reg_tsf3timer_wakeup_ena_lsb = 30
        self.__reg_tsf3timer_wakeup_ena_msb = 30
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tsf3timer_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf3timer_ena_msb, self.__reg_tsf3timer_ena_lsb)
    @reg_tsf3timer_ena.setter
    def reg_tsf3timer_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf3timer_ena_msb, self.__reg_tsf3timer_ena_lsb, value)

    @property
    def reg_tsf3timer_wakeup_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf3timer_wakeup_ena_msb, self.__reg_tsf3timer_wakeup_ena_lsb)
    @reg_tsf3timer_wakeup_ena.setter
    def reg_tsf3timer_wakeup_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf3timer_wakeup_ena_msb, self.__reg_tsf3timer_wakeup_ena_lsb, value)
class MACTSF3_TIMER_LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x104
        self.__reg_tsf3timer_lo_lsb = 0
        self.__reg_tsf3timer_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tsf3timer_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf3timer_lo_msb, self.__reg_tsf3timer_lo_lsb)
    @reg_tsf3timer_lo.setter
    def reg_tsf3timer_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf3timer_lo_msb, self.__reg_tsf3timer_lo_lsb, value)
class MACTSF3_TIMER_HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x108
        self.__reg_tsf3timer_hi_lsb = 0
        self.__reg_tsf3timer_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tsf3timer_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsf3timer_hi_msb, self.__reg_tsf3timer_hi_lsb)
    @reg_tsf3timer_hi.setter
    def reg_tsf3timer_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsf3timer_hi_msb, self.__reg_tsf3timer_hi_lsb, value)
class MACRND(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x10c
        self.__mac_rnd_data_lsb = 0
        self.__mac_rnd_data_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def mac_rnd_data(self):
        return self.__MEM.rdm(self.__addr, self.__mac_rnd_data_msb, self.__mac_rnd_data_lsb)
    @mac_rnd_data.setter
    def mac_rnd_data(self, value):
        return self.__MEM.wrm(self.__addr, self.__mac_rnd_data_msb, self.__mac_rnd_data_lsb, value)
class MACRXBEA_TO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x110
        self.__reg_rxbeacontimout_lsb = 0
        self.__reg_rxbeacontimout_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxbeacontimout(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxbeacontimout_msb, self.__reg_rxbeacontimout_lsb)
    @reg_rxbeacontimout.setter
    def reg_rxbeacontimout(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxbeacontimout_msb, self.__reg_rxbeacontimout_lsb, value)
class MACRWBT_COEX_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x114
        self.__reg_rw_nbt_prio_ble_lsb = 30
        self.__reg_rw_nbt_prio_ble_msb = 31
        self.__reg_rw_bt_prio_sel_lsb = 24
        self.__reg_rw_bt_prio_sel_msb = 27
        self.__reg_freq_hop_timer_lsb = 8
        self.__reg_freq_hop_timer_msb = 19
        self.__reg_wlanat_inv_lsb = 3
        self.__reg_wlanat_inv_msb = 3
        self.__reg_freq_hop_busy_ena_lsb = 1
        self.__reg_freq_hop_busy_ena_msb = 1
        self.__reg_rw_bt_coex_en_lsb = 0
        self.__reg_rw_bt_coex_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rw_nbt_prio_ble(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rw_nbt_prio_ble_msb, self.__reg_rw_nbt_prio_ble_lsb)
    @reg_rw_nbt_prio_ble.setter
    def reg_rw_nbt_prio_ble(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rw_nbt_prio_ble_msb, self.__reg_rw_nbt_prio_ble_lsb, value)

    @property
    def reg_rw_bt_prio_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rw_bt_prio_sel_msb, self.__reg_rw_bt_prio_sel_lsb)
    @reg_rw_bt_prio_sel.setter
    def reg_rw_bt_prio_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rw_bt_prio_sel_msb, self.__reg_rw_bt_prio_sel_lsb, value)

    @property
    def reg_freq_hop_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_freq_hop_timer_msb, self.__reg_freq_hop_timer_lsb)
    @reg_freq_hop_timer.setter
    def reg_freq_hop_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_freq_hop_timer_msb, self.__reg_freq_hop_timer_lsb, value)

    @property
    def reg_wlanat_inv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wlanat_inv_msb, self.__reg_wlanat_inv_lsb)
    @reg_wlanat_inv.setter
    def reg_wlanat_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wlanat_inv_msb, self.__reg_wlanat_inv_lsb, value)

    @property
    def reg_freq_hop_busy_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_freq_hop_busy_ena_msb, self.__reg_freq_hop_busy_ena_lsb)
    @reg_freq_hop_busy_ena.setter
    def reg_freq_hop_busy_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_freq_hop_busy_ena_msb, self.__reg_freq_hop_busy_ena_lsb, value)

    @property
    def reg_rw_bt_coex_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rw_bt_coex_en_msb, self.__reg_rw_bt_coex_en_lsb)
    @reg_rw_bt_coex_en.setter
    def reg_rw_bt_coex_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rw_bt_coex_en_msb, self.__reg_rw_bt_coex_en_lsb, value)
class MACRWBT_COEX_PTI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x118
        self.__reg_wlan_rxbeacon3_pti_lsb = 24
        self.__reg_wlan_rxbeacon3_pti_msb = 27
        self.__reg_wlan_rxbeacon2_pti_lsb = 20
        self.__reg_wlan_rxbeacon2_pti_msb = 23
        self.__reg_wlan_rxbeacon1_pti_lsb = 16
        self.__reg_wlan_rxbeacon1_pti_msb = 19
        self.__reg_wlan_rxbeacon0_pti_lsb = 12
        self.__reg_wlan_rxbeacon0_pti_msb = 15
        self.__reg_wlan_rx_pti_lsb = 4
        self.__reg_wlan_rx_pti_msb = 7
        self.__extern_get_lsb = 3
        self.__extern_get_msb = 3
        self.__wlan_get_lsb = 2
        self.__wlan_get_msb = 2
        self.__wlan_rwbt_ant_sel_lsb = 1
        self.__wlan_rwbt_ant_sel_msb = 1
        self.__rw_bt_get_lsb = 0
        self.__rw_bt_get_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wlan_rxbeacon3_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wlan_rxbeacon3_pti_msb, self.__reg_wlan_rxbeacon3_pti_lsb)
    @reg_wlan_rxbeacon3_pti.setter
    def reg_wlan_rxbeacon3_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wlan_rxbeacon3_pti_msb, self.__reg_wlan_rxbeacon3_pti_lsb, value)

    @property
    def reg_wlan_rxbeacon2_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wlan_rxbeacon2_pti_msb, self.__reg_wlan_rxbeacon2_pti_lsb)
    @reg_wlan_rxbeacon2_pti.setter
    def reg_wlan_rxbeacon2_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wlan_rxbeacon2_pti_msb, self.__reg_wlan_rxbeacon2_pti_lsb, value)

    @property
    def reg_wlan_rxbeacon1_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wlan_rxbeacon1_pti_msb, self.__reg_wlan_rxbeacon1_pti_lsb)
    @reg_wlan_rxbeacon1_pti.setter
    def reg_wlan_rxbeacon1_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wlan_rxbeacon1_pti_msb, self.__reg_wlan_rxbeacon1_pti_lsb, value)

    @property
    def reg_wlan_rxbeacon0_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wlan_rxbeacon0_pti_msb, self.__reg_wlan_rxbeacon0_pti_lsb)
    @reg_wlan_rxbeacon0_pti.setter
    def reg_wlan_rxbeacon0_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wlan_rxbeacon0_pti_msb, self.__reg_wlan_rxbeacon0_pti_lsb, value)

    @property
    def reg_wlan_rx_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wlan_rx_pti_msb, self.__reg_wlan_rx_pti_lsb)
    @reg_wlan_rx_pti.setter
    def reg_wlan_rx_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wlan_rx_pti_msb, self.__reg_wlan_rx_pti_lsb, value)

    @property
    def extern_get(self):
        return self.__MEM.rdm(self.__addr, self.__extern_get_msb, self.__extern_get_lsb)
    @extern_get.setter
    def extern_get(self, value):
        return self.__MEM.wrm(self.__addr, self.__extern_get_msb, self.__extern_get_lsb, value)

    @property
    def wlan_get(self):
        return self.__MEM.rdm(self.__addr, self.__wlan_get_msb, self.__wlan_get_lsb)
    @wlan_get.setter
    def wlan_get(self, value):
        return self.__MEM.wrm(self.__addr, self.__wlan_get_msb, self.__wlan_get_lsb, value)

    @property
    def wlan_rwbt_ant_sel(self):
        return self.__MEM.rdm(self.__addr, self.__wlan_rwbt_ant_sel_msb, self.__wlan_rwbt_ant_sel_lsb)
    @wlan_rwbt_ant_sel.setter
    def wlan_rwbt_ant_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__wlan_rwbt_ant_sel_msb, self.__wlan_rwbt_ant_sel_lsb, value)

    @property
    def rw_bt_get(self):
        return self.__MEM.rdm(self.__addr, self.__rw_bt_get_msb, self.__rw_bt_get_lsb)
    @rw_bt_get.setter
    def rw_bt_get(self, value):
        return self.__MEM.wrm(self.__addr, self.__rw_bt_get_msb, self.__rw_bt_get_lsb, value)
class MACRWBT_COEX_WAIT0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x11c
        self.__reg_wlan_ant_sel_tail_wait_lsb = 16
        self.__reg_wlan_ant_sel_tail_wait_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wlan_ant_sel_tail_wait(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wlan_ant_sel_tail_wait_msb, self.__reg_wlan_ant_sel_tail_wait_lsb)
    @reg_wlan_ant_sel_tail_wait.setter
    def reg_wlan_ant_sel_tail_wait(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wlan_ant_sel_tail_wait_msb, self.__reg_wlan_ant_sel_tail_wait_lsb, value)
class MACRWBT_COEX_WAIT1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x120
        self.__reg_wlan_ant_sel_head_wait_lsb = 16
        self.__reg_wlan_ant_sel_head_wait_msb = 31
        self.__reg_mac_refuse_time_lsb = 0
        self.__reg_mac_refuse_time_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wlan_ant_sel_head_wait(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wlan_ant_sel_head_wait_msb, self.__reg_wlan_ant_sel_head_wait_lsb)
    @reg_wlan_ant_sel_head_wait.setter
    def reg_wlan_ant_sel_head_wait(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wlan_ant_sel_head_wait_msb, self.__reg_wlan_ant_sel_head_wait_lsb, value)

    @property
    def reg_mac_refuse_time(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mac_refuse_time_msb, self.__reg_mac_refuse_time_lsb)
    @reg_mac_refuse_time.setter
    def reg_mac_refuse_time(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mac_refuse_time_msb, self.__reg_mac_refuse_time_lsb, value)
class MACRWBT_COEX_DYNAMIC_PRIORITY(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x124
        self.__reg_bt_dynamic_prio_en_lsb = 31
        self.__reg_bt_dynamic_prio_en_msb = 31
        self.__reg_bt_dynamic_prio_lsb = 27
        self.__reg_bt_dynamic_prio_msb = 30
        self.__reg_wlan_dynamic_prio_en_lsb = 26
        self.__reg_wlan_dynamic_prio_en_msb = 26
        self.__reg_wlan_dynamic_prio_lsb = 22
        self.__reg_wlan_dynamic_prio_msb = 25
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bt_dynamic_prio_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bt_dynamic_prio_en_msb, self.__reg_bt_dynamic_prio_en_lsb)
    @reg_bt_dynamic_prio_en.setter
    def reg_bt_dynamic_prio_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bt_dynamic_prio_en_msb, self.__reg_bt_dynamic_prio_en_lsb, value)

    @property
    def reg_bt_dynamic_prio(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bt_dynamic_prio_msb, self.__reg_bt_dynamic_prio_lsb)
    @reg_bt_dynamic_prio.setter
    def reg_bt_dynamic_prio(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bt_dynamic_prio_msb, self.__reg_bt_dynamic_prio_lsb, value)

    @property
    def reg_wlan_dynamic_prio_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wlan_dynamic_prio_en_msb, self.__reg_wlan_dynamic_prio_en_lsb)
    @reg_wlan_dynamic_prio_en.setter
    def reg_wlan_dynamic_prio_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wlan_dynamic_prio_en_msb, self.__reg_wlan_dynamic_prio_en_lsb, value)

    @property
    def reg_wlan_dynamic_prio(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wlan_dynamic_prio_msb, self.__reg_wlan_dynamic_prio_lsb)
    @reg_wlan_dynamic_prio.setter
    def reg_wlan_dynamic_prio(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wlan_dynamic_prio_msb, self.__reg_wlan_dynamic_prio_lsb, value)
class MACRWBT_COEX_GPIO_SEL(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x128
        self.__reg_freq_hop_busy_lsb = 30
        self.__reg_freq_hop_busy_msb = 31
        self.__reg_gpio_bt_priority_sel_lsb = 6
        self.__reg_gpio_bt_priority_sel_msb = 8
        self.__reg_gpio_bt_active_sel_lsb = 3
        self.__reg_gpio_bt_active_sel_msb = 5
        self.__reg_gpio_wlan_active_sel_lsb = 0
        self.__reg_gpio_wlan_active_sel_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_freq_hop_busy(self):
        return self.__MEM.rdm(self.__addr, self.__reg_freq_hop_busy_msb, self.__reg_freq_hop_busy_lsb)
    @reg_freq_hop_busy.setter
    def reg_freq_hop_busy(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_freq_hop_busy_msb, self.__reg_freq_hop_busy_lsb, value)

    @property
    def reg_gpio_bt_priority_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gpio_bt_priority_sel_msb, self.__reg_gpio_bt_priority_sel_lsb)
    @reg_gpio_bt_priority_sel.setter
    def reg_gpio_bt_priority_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gpio_bt_priority_sel_msb, self.__reg_gpio_bt_priority_sel_lsb, value)

    @property
    def reg_gpio_bt_active_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gpio_bt_active_sel_msb, self.__reg_gpio_bt_active_sel_lsb)
    @reg_gpio_bt_active_sel.setter
    def reg_gpio_bt_active_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gpio_bt_active_sel_msb, self.__reg_gpio_bt_active_sel_lsb, value)

    @property
    def reg_gpio_wlan_active_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gpio_wlan_active_sel_msb, self.__reg_gpio_wlan_active_sel_lsb)
    @reg_gpio_wlan_active_sel.setter
    def reg_gpio_wlan_active_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gpio_wlan_active_sel_msb, self.__reg_gpio_wlan_active_sel_lsb, value)
class MACRWBT_COEX_TIMER0_CONF0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x12c
        self.__reg_coex_timer0_ena_lsb = 31
        self.__reg_coex_timer0_ena_msb = 31
        self.__reg_coex_timer0_src_lsb = 30
        self.__reg_coex_timer0_src_msb = 30
        self.__reg_coex_timer0_fh_lsb = 28
        self.__reg_coex_timer0_fh_msb = 28
        self.__reg_coex_timer0_pti_lsb = 24
        self.__reg_coex_timer0_pti_msb = 27
        self.__reg_coex_timer0_len_lsb = 0
        self.__reg_coex_timer0_len_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_coex_timer0_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer0_ena_msb, self.__reg_coex_timer0_ena_lsb)
    @reg_coex_timer0_ena.setter
    def reg_coex_timer0_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer0_ena_msb, self.__reg_coex_timer0_ena_lsb, value)

    @property
    def reg_coex_timer0_src(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer0_src_msb, self.__reg_coex_timer0_src_lsb)
    @reg_coex_timer0_src.setter
    def reg_coex_timer0_src(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer0_src_msb, self.__reg_coex_timer0_src_lsb, value)

    @property
    def reg_coex_timer0_fh(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer0_fh_msb, self.__reg_coex_timer0_fh_lsb)
    @reg_coex_timer0_fh.setter
    def reg_coex_timer0_fh(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer0_fh_msb, self.__reg_coex_timer0_fh_lsb, value)

    @property
    def reg_coex_timer0_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer0_pti_msb, self.__reg_coex_timer0_pti_lsb)
    @reg_coex_timer0_pti.setter
    def reg_coex_timer0_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer0_pti_msb, self.__reg_coex_timer0_pti_lsb, value)

    @property
    def reg_coex_timer0_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer0_len_msb, self.__reg_coex_timer0_len_lsb)
    @reg_coex_timer0_len.setter
    def reg_coex_timer0_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer0_len_msb, self.__reg_coex_timer0_len_lsb, value)
class MACRWBT_COEX_TIMER0_CONF1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x130
        self.__reg_coex_timer0_start_lsb = 0
        self.__reg_coex_timer0_start_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_coex_timer0_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer0_start_msb, self.__reg_coex_timer0_start_lsb)
    @reg_coex_timer0_start.setter
    def reg_coex_timer0_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer0_start_msb, self.__reg_coex_timer0_start_lsb, value)
class MACRWBT_COEX_TIMER1_CONF0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x134
        self.__reg_coex_timer1_ena_lsb = 31
        self.__reg_coex_timer1_ena_msb = 31
        self.__reg_coex_timer1_src_lsb = 30
        self.__reg_coex_timer1_src_msb = 30
        self.__reg_coex_timer1_fh_lsb = 28
        self.__reg_coex_timer1_fh_msb = 28
        self.__reg_coex_timer1_pti_lsb = 24
        self.__reg_coex_timer1_pti_msb = 27
        self.__reg_coex_timer1_len_lsb = 0
        self.__reg_coex_timer1_len_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_coex_timer1_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer1_ena_msb, self.__reg_coex_timer1_ena_lsb)
    @reg_coex_timer1_ena.setter
    def reg_coex_timer1_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer1_ena_msb, self.__reg_coex_timer1_ena_lsb, value)

    @property
    def reg_coex_timer1_src(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer1_src_msb, self.__reg_coex_timer1_src_lsb)
    @reg_coex_timer1_src.setter
    def reg_coex_timer1_src(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer1_src_msb, self.__reg_coex_timer1_src_lsb, value)

    @property
    def reg_coex_timer1_fh(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer1_fh_msb, self.__reg_coex_timer1_fh_lsb)
    @reg_coex_timer1_fh.setter
    def reg_coex_timer1_fh(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer1_fh_msb, self.__reg_coex_timer1_fh_lsb, value)

    @property
    def reg_coex_timer1_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer1_pti_msb, self.__reg_coex_timer1_pti_lsb)
    @reg_coex_timer1_pti.setter
    def reg_coex_timer1_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer1_pti_msb, self.__reg_coex_timer1_pti_lsb, value)

    @property
    def reg_coex_timer1_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer1_len_msb, self.__reg_coex_timer1_len_lsb)
    @reg_coex_timer1_len.setter
    def reg_coex_timer1_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer1_len_msb, self.__reg_coex_timer1_len_lsb, value)
class MACRWBT_COEX_TIMER1_CONF1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x138
        self.__reg_coex_timer1_start_lsb = 0
        self.__reg_coex_timer1_start_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_coex_timer1_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer1_start_msb, self.__reg_coex_timer1_start_lsb)
    @reg_coex_timer1_start.setter
    def reg_coex_timer1_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer1_start_msb, self.__reg_coex_timer1_start_lsb, value)
class MACRWBT_COEX_TIMER2_CONF0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x13c
        self.__reg_coex_timer2_ena_lsb = 31
        self.__reg_coex_timer2_ena_msb = 31
        self.__reg_coex_timer2_src_lsb = 30
        self.__reg_coex_timer2_src_msb = 30
        self.__reg_coex_timer2_fh_lsb = 28
        self.__reg_coex_timer2_fh_msb = 28
        self.__reg_coex_timer2_pti_lsb = 24
        self.__reg_coex_timer2_pti_msb = 27
        self.__reg_coex_timer2_len_lsb = 0
        self.__reg_coex_timer2_len_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_coex_timer2_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer2_ena_msb, self.__reg_coex_timer2_ena_lsb)
    @reg_coex_timer2_ena.setter
    def reg_coex_timer2_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer2_ena_msb, self.__reg_coex_timer2_ena_lsb, value)

    @property
    def reg_coex_timer2_src(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer2_src_msb, self.__reg_coex_timer2_src_lsb)
    @reg_coex_timer2_src.setter
    def reg_coex_timer2_src(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer2_src_msb, self.__reg_coex_timer2_src_lsb, value)

    @property
    def reg_coex_timer2_fh(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer2_fh_msb, self.__reg_coex_timer2_fh_lsb)
    @reg_coex_timer2_fh.setter
    def reg_coex_timer2_fh(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer2_fh_msb, self.__reg_coex_timer2_fh_lsb, value)

    @property
    def reg_coex_timer2_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer2_pti_msb, self.__reg_coex_timer2_pti_lsb)
    @reg_coex_timer2_pti.setter
    def reg_coex_timer2_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer2_pti_msb, self.__reg_coex_timer2_pti_lsb, value)

    @property
    def reg_coex_timer2_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer2_len_msb, self.__reg_coex_timer2_len_lsb)
    @reg_coex_timer2_len.setter
    def reg_coex_timer2_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer2_len_msb, self.__reg_coex_timer2_len_lsb, value)
class MACRWBT_COEX_TIMER2_CONF1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x140
        self.__reg_coex_timer2_start_lsb = 0
        self.__reg_coex_timer2_start_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_coex_timer2_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer2_start_msb, self.__reg_coex_timer2_start_lsb)
    @reg_coex_timer2_start.setter
    def reg_coex_timer2_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer2_start_msb, self.__reg_coex_timer2_start_lsb, value)
class MACRWBT_COEX_TIMER3_CONF0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x144
        self.__reg_coex_timer3_ena_lsb = 31
        self.__reg_coex_timer3_ena_msb = 31
        self.__reg_coex_timer3_src_lsb = 30
        self.__reg_coex_timer3_src_msb = 30
        self.__reg_coex_timer3_fh_lsb = 28
        self.__reg_coex_timer3_fh_msb = 28
        self.__reg_coex_timer3_pti_lsb = 24
        self.__reg_coex_timer3_pti_msb = 27
        self.__reg_coex_timer3_len_lsb = 0
        self.__reg_coex_timer3_len_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_coex_timer3_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer3_ena_msb, self.__reg_coex_timer3_ena_lsb)
    @reg_coex_timer3_ena.setter
    def reg_coex_timer3_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer3_ena_msb, self.__reg_coex_timer3_ena_lsb, value)

    @property
    def reg_coex_timer3_src(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer3_src_msb, self.__reg_coex_timer3_src_lsb)
    @reg_coex_timer3_src.setter
    def reg_coex_timer3_src(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer3_src_msb, self.__reg_coex_timer3_src_lsb, value)

    @property
    def reg_coex_timer3_fh(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer3_fh_msb, self.__reg_coex_timer3_fh_lsb)
    @reg_coex_timer3_fh.setter
    def reg_coex_timer3_fh(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer3_fh_msb, self.__reg_coex_timer3_fh_lsb, value)

    @property
    def reg_coex_timer3_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer3_pti_msb, self.__reg_coex_timer3_pti_lsb)
    @reg_coex_timer3_pti.setter
    def reg_coex_timer3_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer3_pti_msb, self.__reg_coex_timer3_pti_lsb, value)

    @property
    def reg_coex_timer3_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer3_len_msb, self.__reg_coex_timer3_len_lsb)
    @reg_coex_timer3_len.setter
    def reg_coex_timer3_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer3_len_msb, self.__reg_coex_timer3_len_lsb, value)
class MACRWBT_COEX_TIMER3_CONF1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x148
        self.__reg_coex_timer3_start_lsb = 0
        self.__reg_coex_timer3_start_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_coex_timer3_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer3_start_msb, self.__reg_coex_timer3_start_lsb)
    @reg_coex_timer3_start.setter
    def reg_coex_timer3_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer3_start_msb, self.__reg_coex_timer3_start_lsb, value)
class MACRWBT_COEX_TIMER4_CONF0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x14c
        self.__reg_coex_timer4_ena_lsb = 31
        self.__reg_coex_timer4_ena_msb = 31
        self.__reg_coex_timer4_src_lsb = 30
        self.__reg_coex_timer4_src_msb = 30
        self.__reg_coex_timer4_fh_lsb = 28
        self.__reg_coex_timer4_fh_msb = 28
        self.__reg_coex_timer4_pti_lsb = 24
        self.__reg_coex_timer4_pti_msb = 27
        self.__reg_coex_timer4_len_lsb = 0
        self.__reg_coex_timer4_len_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_coex_timer4_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer4_ena_msb, self.__reg_coex_timer4_ena_lsb)
    @reg_coex_timer4_ena.setter
    def reg_coex_timer4_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer4_ena_msb, self.__reg_coex_timer4_ena_lsb, value)

    @property
    def reg_coex_timer4_src(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer4_src_msb, self.__reg_coex_timer4_src_lsb)
    @reg_coex_timer4_src.setter
    def reg_coex_timer4_src(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer4_src_msb, self.__reg_coex_timer4_src_lsb, value)

    @property
    def reg_coex_timer4_fh(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer4_fh_msb, self.__reg_coex_timer4_fh_lsb)
    @reg_coex_timer4_fh.setter
    def reg_coex_timer4_fh(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer4_fh_msb, self.__reg_coex_timer4_fh_lsb, value)

    @property
    def reg_coex_timer4_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer4_pti_msb, self.__reg_coex_timer4_pti_lsb)
    @reg_coex_timer4_pti.setter
    def reg_coex_timer4_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer4_pti_msb, self.__reg_coex_timer4_pti_lsb, value)

    @property
    def reg_coex_timer4_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer4_len_msb, self.__reg_coex_timer4_len_lsb)
    @reg_coex_timer4_len.setter
    def reg_coex_timer4_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer4_len_msb, self.__reg_coex_timer4_len_lsb, value)
class MACRWBT_COEX_TIMER4_CONF1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x150
        self.__reg_coex_timer4_start_lsb = 0
        self.__reg_coex_timer4_start_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_coex_timer4_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer4_start_msb, self.__reg_coex_timer4_start_lsb)
    @reg_coex_timer4_start.setter
    def reg_coex_timer4_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer4_start_msb, self.__reg_coex_timer4_start_lsb, value)
class MACRWBT_COEX_TIMER5_CONF0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x154
        self.__reg_coex_timer5_ena_lsb = 31
        self.__reg_coex_timer5_ena_msb = 31
        self.__reg_coex_timer5_src_lsb = 30
        self.__reg_coex_timer5_src_msb = 30
        self.__reg_coex_timer5_fh_lsb = 28
        self.__reg_coex_timer5_fh_msb = 28
        self.__reg_coex_timer5_pti_lsb = 24
        self.__reg_coex_timer5_pti_msb = 27
        self.__reg_coex_timer5_len_lsb = 0
        self.__reg_coex_timer5_len_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_coex_timer5_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer5_ena_msb, self.__reg_coex_timer5_ena_lsb)
    @reg_coex_timer5_ena.setter
    def reg_coex_timer5_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer5_ena_msb, self.__reg_coex_timer5_ena_lsb, value)

    @property
    def reg_coex_timer5_src(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer5_src_msb, self.__reg_coex_timer5_src_lsb)
    @reg_coex_timer5_src.setter
    def reg_coex_timer5_src(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer5_src_msb, self.__reg_coex_timer5_src_lsb, value)

    @property
    def reg_coex_timer5_fh(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer5_fh_msb, self.__reg_coex_timer5_fh_lsb)
    @reg_coex_timer5_fh.setter
    def reg_coex_timer5_fh(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer5_fh_msb, self.__reg_coex_timer5_fh_lsb, value)

    @property
    def reg_coex_timer5_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer5_pti_msb, self.__reg_coex_timer5_pti_lsb)
    @reg_coex_timer5_pti.setter
    def reg_coex_timer5_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer5_pti_msb, self.__reg_coex_timer5_pti_lsb, value)

    @property
    def reg_coex_timer5_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer5_len_msb, self.__reg_coex_timer5_len_lsb)
    @reg_coex_timer5_len.setter
    def reg_coex_timer5_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer5_len_msb, self.__reg_coex_timer5_len_lsb, value)
class MACRWBT_COEX_TIMER5_CONF1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x158
        self.__reg_coex_timer5_start_lsb = 0
        self.__reg_coex_timer5_start_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_coex_timer5_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer5_start_msb, self.__reg_coex_timer5_start_lsb)
    @reg_coex_timer5_start.setter
    def reg_coex_timer5_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer5_start_msb, self.__reg_coex_timer5_start_lsb, value)
class MACRWBT_COEX_TIMER6_CONF0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x15c
        self.__reg_coex_timer6_ena_lsb = 31
        self.__reg_coex_timer6_ena_msb = 31
        self.__reg_coex_timer6_src_lsb = 30
        self.__reg_coex_timer6_src_msb = 30
        self.__reg_coex_timer6_fh_lsb = 28
        self.__reg_coex_timer6_fh_msb = 28
        self.__reg_coex_timer6_pti_lsb = 24
        self.__reg_coex_timer6_pti_msb = 27
        self.__reg_coex_timer6_len_lsb = 0
        self.__reg_coex_timer6_len_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_coex_timer6_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer6_ena_msb, self.__reg_coex_timer6_ena_lsb)
    @reg_coex_timer6_ena.setter
    def reg_coex_timer6_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer6_ena_msb, self.__reg_coex_timer6_ena_lsb, value)

    @property
    def reg_coex_timer6_src(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer6_src_msb, self.__reg_coex_timer6_src_lsb)
    @reg_coex_timer6_src.setter
    def reg_coex_timer6_src(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer6_src_msb, self.__reg_coex_timer6_src_lsb, value)

    @property
    def reg_coex_timer6_fh(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer6_fh_msb, self.__reg_coex_timer6_fh_lsb)
    @reg_coex_timer6_fh.setter
    def reg_coex_timer6_fh(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer6_fh_msb, self.__reg_coex_timer6_fh_lsb, value)

    @property
    def reg_coex_timer6_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer6_pti_msb, self.__reg_coex_timer6_pti_lsb)
    @reg_coex_timer6_pti.setter
    def reg_coex_timer6_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer6_pti_msb, self.__reg_coex_timer6_pti_lsb, value)

    @property
    def reg_coex_timer6_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer6_len_msb, self.__reg_coex_timer6_len_lsb)
    @reg_coex_timer6_len.setter
    def reg_coex_timer6_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer6_len_msb, self.__reg_coex_timer6_len_lsb, value)
class MACRWBT_COEX_TIMER6_CONF1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x160
        self.__reg_coex_timer6_start_lsb = 0
        self.__reg_coex_timer6_start_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_coex_timer6_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer6_start_msb, self.__reg_coex_timer6_start_lsb)
    @reg_coex_timer6_start.setter
    def reg_coex_timer6_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer6_start_msb, self.__reg_coex_timer6_start_lsb, value)
class MACRWBT_COEX_TIMER7_CONF0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x164
        self.__reg_coex_timer7_ena_lsb = 31
        self.__reg_coex_timer7_ena_msb = 31
        self.__reg_coex_timer7_src_lsb = 30
        self.__reg_coex_timer7_src_msb = 30
        self.__reg_coex_timer7_fh_lsb = 28
        self.__reg_coex_timer7_fh_msb = 28
        self.__reg_coex_timer7_pti_lsb = 24
        self.__reg_coex_timer7_pti_msb = 27
        self.__reg_coex_timer7_len_lsb = 0
        self.__reg_coex_timer7_len_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_coex_timer7_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer7_ena_msb, self.__reg_coex_timer7_ena_lsb)
    @reg_coex_timer7_ena.setter
    def reg_coex_timer7_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer7_ena_msb, self.__reg_coex_timer7_ena_lsb, value)

    @property
    def reg_coex_timer7_src(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer7_src_msb, self.__reg_coex_timer7_src_lsb)
    @reg_coex_timer7_src.setter
    def reg_coex_timer7_src(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer7_src_msb, self.__reg_coex_timer7_src_lsb, value)

    @property
    def reg_coex_timer7_fh(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer7_fh_msb, self.__reg_coex_timer7_fh_lsb)
    @reg_coex_timer7_fh.setter
    def reg_coex_timer7_fh(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer7_fh_msb, self.__reg_coex_timer7_fh_lsb, value)

    @property
    def reg_coex_timer7_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer7_pti_msb, self.__reg_coex_timer7_pti_lsb)
    @reg_coex_timer7_pti.setter
    def reg_coex_timer7_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer7_pti_msb, self.__reg_coex_timer7_pti_lsb, value)

    @property
    def reg_coex_timer7_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer7_len_msb, self.__reg_coex_timer7_len_lsb)
    @reg_coex_timer7_len.setter
    def reg_coex_timer7_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer7_len_msb, self.__reg_coex_timer7_len_lsb, value)
class MACRWBT_COEX_TIMER7_CONF1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x168
        self.__reg_coex_timer7_start_lsb = 0
        self.__reg_coex_timer7_start_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_coex_timer7_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer7_start_msb, self.__reg_coex_timer7_start_lsb)
    @reg_coex_timer7_start.setter
    def reg_coex_timer7_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer7_start_msb, self.__reg_coex_timer7_start_lsb, value)
class MACRWBT_COEX_TIMER8_CONF0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x16c
        self.__reg_coex_timer8_ena_lsb = 31
        self.__reg_coex_timer8_ena_msb = 31
        self.__reg_coex_timer8_src_lsb = 30
        self.__reg_coex_timer8_src_msb = 30
        self.__reg_coex_timer8_fh_lsb = 28
        self.__reg_coex_timer8_fh_msb = 28
        self.__reg_coex_timer8_pti_lsb = 24
        self.__reg_coex_timer8_pti_msb = 27
        self.__reg_coex_timer8_len_lsb = 0
        self.__reg_coex_timer8_len_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_coex_timer8_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer8_ena_msb, self.__reg_coex_timer8_ena_lsb)
    @reg_coex_timer8_ena.setter
    def reg_coex_timer8_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer8_ena_msb, self.__reg_coex_timer8_ena_lsb, value)

    @property
    def reg_coex_timer8_src(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer8_src_msb, self.__reg_coex_timer8_src_lsb)
    @reg_coex_timer8_src.setter
    def reg_coex_timer8_src(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer8_src_msb, self.__reg_coex_timer8_src_lsb, value)

    @property
    def reg_coex_timer8_fh(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer8_fh_msb, self.__reg_coex_timer8_fh_lsb)
    @reg_coex_timer8_fh.setter
    def reg_coex_timer8_fh(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer8_fh_msb, self.__reg_coex_timer8_fh_lsb, value)

    @property
    def reg_coex_timer8_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer8_pti_msb, self.__reg_coex_timer8_pti_lsb)
    @reg_coex_timer8_pti.setter
    def reg_coex_timer8_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer8_pti_msb, self.__reg_coex_timer8_pti_lsb, value)

    @property
    def reg_coex_timer8_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer8_len_msb, self.__reg_coex_timer8_len_lsb)
    @reg_coex_timer8_len.setter
    def reg_coex_timer8_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer8_len_msb, self.__reg_coex_timer8_len_lsb, value)
class MACRWBT_COEX_TIMER8_CONF1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x170
        self.__reg_coex_timer8_start_lsb = 0
        self.__reg_coex_timer8_start_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_coex_timer8_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer8_start_msb, self.__reg_coex_timer8_start_lsb)
    @reg_coex_timer8_start.setter
    def reg_coex_timer8_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer8_start_msb, self.__reg_coex_timer8_start_lsb, value)
class MACRWBT_COEX_TIMER9_CONF0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x174
        self.__reg_coex_timer9_ena_lsb = 31
        self.__reg_coex_timer9_ena_msb = 31
        self.__reg_coex_timer9_src_lsb = 30
        self.__reg_coex_timer9_src_msb = 30
        self.__reg_coex_timer9_fh_lsb = 28
        self.__reg_coex_timer9_fh_msb = 28
        self.__reg_coex_timer9_pti_lsb = 24
        self.__reg_coex_timer9_pti_msb = 27
        self.__reg_coex_timer9_len_lsb = 0
        self.__reg_coex_timer9_len_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_coex_timer9_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer9_ena_msb, self.__reg_coex_timer9_ena_lsb)
    @reg_coex_timer9_ena.setter
    def reg_coex_timer9_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer9_ena_msb, self.__reg_coex_timer9_ena_lsb, value)

    @property
    def reg_coex_timer9_src(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer9_src_msb, self.__reg_coex_timer9_src_lsb)
    @reg_coex_timer9_src.setter
    def reg_coex_timer9_src(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer9_src_msb, self.__reg_coex_timer9_src_lsb, value)

    @property
    def reg_coex_timer9_fh(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer9_fh_msb, self.__reg_coex_timer9_fh_lsb)
    @reg_coex_timer9_fh.setter
    def reg_coex_timer9_fh(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer9_fh_msb, self.__reg_coex_timer9_fh_lsb, value)

    @property
    def reg_coex_timer9_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer9_pti_msb, self.__reg_coex_timer9_pti_lsb)
    @reg_coex_timer9_pti.setter
    def reg_coex_timer9_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer9_pti_msb, self.__reg_coex_timer9_pti_lsb, value)

    @property
    def reg_coex_timer9_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer9_len_msb, self.__reg_coex_timer9_len_lsb)
    @reg_coex_timer9_len.setter
    def reg_coex_timer9_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer9_len_msb, self.__reg_coex_timer9_len_lsb, value)
class MACRWBT_COEX_TIMER9_CONF1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x178
        self.__reg_coex_timer9_start_lsb = 0
        self.__reg_coex_timer9_start_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_coex_timer9_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer9_start_msb, self.__reg_coex_timer9_start_lsb)
    @reg_coex_timer9_start.setter
    def reg_coex_timer9_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer9_start_msb, self.__reg_coex_timer9_start_lsb, value)
class MACRWBT_COEX_TIMER10_CONF0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x17c
        self.__reg_coex_timer10_ena_lsb = 31
        self.__reg_coex_timer10_ena_msb = 31
        self.__reg_coex_timer10_src_lsb = 30
        self.__reg_coex_timer10_src_msb = 30
        self.__reg_coex_timer10_fh_lsb = 28
        self.__reg_coex_timer10_fh_msb = 28
        self.__reg_coex_timer10_pti_lsb = 24
        self.__reg_coex_timer10_pti_msb = 27
        self.__reg_coex_timer10_len_lsb = 0
        self.__reg_coex_timer10_len_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_coex_timer10_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer10_ena_msb, self.__reg_coex_timer10_ena_lsb)
    @reg_coex_timer10_ena.setter
    def reg_coex_timer10_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer10_ena_msb, self.__reg_coex_timer10_ena_lsb, value)

    @property
    def reg_coex_timer10_src(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer10_src_msb, self.__reg_coex_timer10_src_lsb)
    @reg_coex_timer10_src.setter
    def reg_coex_timer10_src(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer10_src_msb, self.__reg_coex_timer10_src_lsb, value)

    @property
    def reg_coex_timer10_fh(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer10_fh_msb, self.__reg_coex_timer10_fh_lsb)
    @reg_coex_timer10_fh.setter
    def reg_coex_timer10_fh(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer10_fh_msb, self.__reg_coex_timer10_fh_lsb, value)

    @property
    def reg_coex_timer10_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer10_pti_msb, self.__reg_coex_timer10_pti_lsb)
    @reg_coex_timer10_pti.setter
    def reg_coex_timer10_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer10_pti_msb, self.__reg_coex_timer10_pti_lsb, value)

    @property
    def reg_coex_timer10_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer10_len_msb, self.__reg_coex_timer10_len_lsb)
    @reg_coex_timer10_len.setter
    def reg_coex_timer10_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer10_len_msb, self.__reg_coex_timer10_len_lsb, value)
class MACRWBT_COEX_TIMER10_CONF1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x180
        self.__reg_coex_timer10_start_lsb = 0
        self.__reg_coex_timer10_start_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_coex_timer10_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer10_start_msb, self.__reg_coex_timer10_start_lsb)
    @reg_coex_timer10_start.setter
    def reg_coex_timer10_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer10_start_msb, self.__reg_coex_timer10_start_lsb, value)
class MACRWBT_COEX_TIMER11_CONF0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x184
        self.__reg_coex_timer11_ena_lsb = 31
        self.__reg_coex_timer11_ena_msb = 31
        self.__reg_coex_timer11_src_lsb = 30
        self.__reg_coex_timer11_src_msb = 30
        self.__reg_coex_timer11_fh_lsb = 28
        self.__reg_coex_timer11_fh_msb = 28
        self.__reg_coex_timer11_pti_lsb = 24
        self.__reg_coex_timer11_pti_msb = 27
        self.__reg_coex_timer11_len_lsb = 0
        self.__reg_coex_timer11_len_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_coex_timer11_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer11_ena_msb, self.__reg_coex_timer11_ena_lsb)
    @reg_coex_timer11_ena.setter
    def reg_coex_timer11_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer11_ena_msb, self.__reg_coex_timer11_ena_lsb, value)

    @property
    def reg_coex_timer11_src(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer11_src_msb, self.__reg_coex_timer11_src_lsb)
    @reg_coex_timer11_src.setter
    def reg_coex_timer11_src(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer11_src_msb, self.__reg_coex_timer11_src_lsb, value)

    @property
    def reg_coex_timer11_fh(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer11_fh_msb, self.__reg_coex_timer11_fh_lsb)
    @reg_coex_timer11_fh.setter
    def reg_coex_timer11_fh(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer11_fh_msb, self.__reg_coex_timer11_fh_lsb, value)

    @property
    def reg_coex_timer11_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer11_pti_msb, self.__reg_coex_timer11_pti_lsb)
    @reg_coex_timer11_pti.setter
    def reg_coex_timer11_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer11_pti_msb, self.__reg_coex_timer11_pti_lsb, value)

    @property
    def reg_coex_timer11_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer11_len_msb, self.__reg_coex_timer11_len_lsb)
    @reg_coex_timer11_len.setter
    def reg_coex_timer11_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer11_len_msb, self.__reg_coex_timer11_len_lsb, value)
class MACRWBT_COEX_TIMER11_CONF1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x188
        self.__reg_coex_timer11_start_lsb = 0
        self.__reg_coex_timer11_start_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_coex_timer11_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer11_start_msb, self.__reg_coex_timer11_start_lsb)
    @reg_coex_timer11_start.setter
    def reg_coex_timer11_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer11_start_msb, self.__reg_coex_timer11_start_lsb, value)
class MACRWBT_COEX_TIMER_END_ST(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x18c
        self.__coex_timer11_end_st_lsb = 11
        self.__coex_timer11_end_st_msb = 11
        self.__coex_timer10_end_st_lsb = 10
        self.__coex_timer10_end_st_msb = 10
        self.__coex_timer9_end_st_lsb = 9
        self.__coex_timer9_end_st_msb = 9
        self.__coex_timer8_end_st_lsb = 8
        self.__coex_timer8_end_st_msb = 8
        self.__coex_timer7_end_st_lsb = 7
        self.__coex_timer7_end_st_msb = 7
        self.__coex_timer6_end_st_lsb = 6
        self.__coex_timer6_end_st_msb = 6
        self.__coex_timer5_end_st_lsb = 5
        self.__coex_timer5_end_st_msb = 5
        self.__coex_timer4_end_st_lsb = 4
        self.__coex_timer4_end_st_msb = 4
        self.__coex_timer3_end_st_lsb = 3
        self.__coex_timer3_end_st_msb = 3
        self.__coex_timer2_end_st_lsb = 2
        self.__coex_timer2_end_st_msb = 2
        self.__coex_timer1_end_st_lsb = 1
        self.__coex_timer1_end_st_msb = 1
        self.__coex_timer0_end_st_lsb = 0
        self.__coex_timer0_end_st_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def coex_timer11_end_st(self):
        return self.__MEM.rdm(self.__addr, self.__coex_timer11_end_st_msb, self.__coex_timer11_end_st_lsb)
    @coex_timer11_end_st.setter
    def coex_timer11_end_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__coex_timer11_end_st_msb, self.__coex_timer11_end_st_lsb, value)

    @property
    def coex_timer10_end_st(self):
        return self.__MEM.rdm(self.__addr, self.__coex_timer10_end_st_msb, self.__coex_timer10_end_st_lsb)
    @coex_timer10_end_st.setter
    def coex_timer10_end_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__coex_timer10_end_st_msb, self.__coex_timer10_end_st_lsb, value)

    @property
    def coex_timer9_end_st(self):
        return self.__MEM.rdm(self.__addr, self.__coex_timer9_end_st_msb, self.__coex_timer9_end_st_lsb)
    @coex_timer9_end_st.setter
    def coex_timer9_end_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__coex_timer9_end_st_msb, self.__coex_timer9_end_st_lsb, value)

    @property
    def coex_timer8_end_st(self):
        return self.__MEM.rdm(self.__addr, self.__coex_timer8_end_st_msb, self.__coex_timer8_end_st_lsb)
    @coex_timer8_end_st.setter
    def coex_timer8_end_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__coex_timer8_end_st_msb, self.__coex_timer8_end_st_lsb, value)

    @property
    def coex_timer7_end_st(self):
        return self.__MEM.rdm(self.__addr, self.__coex_timer7_end_st_msb, self.__coex_timer7_end_st_lsb)
    @coex_timer7_end_st.setter
    def coex_timer7_end_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__coex_timer7_end_st_msb, self.__coex_timer7_end_st_lsb, value)

    @property
    def coex_timer6_end_st(self):
        return self.__MEM.rdm(self.__addr, self.__coex_timer6_end_st_msb, self.__coex_timer6_end_st_lsb)
    @coex_timer6_end_st.setter
    def coex_timer6_end_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__coex_timer6_end_st_msb, self.__coex_timer6_end_st_lsb, value)

    @property
    def coex_timer5_end_st(self):
        return self.__MEM.rdm(self.__addr, self.__coex_timer5_end_st_msb, self.__coex_timer5_end_st_lsb)
    @coex_timer5_end_st.setter
    def coex_timer5_end_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__coex_timer5_end_st_msb, self.__coex_timer5_end_st_lsb, value)

    @property
    def coex_timer4_end_st(self):
        return self.__MEM.rdm(self.__addr, self.__coex_timer4_end_st_msb, self.__coex_timer4_end_st_lsb)
    @coex_timer4_end_st.setter
    def coex_timer4_end_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__coex_timer4_end_st_msb, self.__coex_timer4_end_st_lsb, value)

    @property
    def coex_timer3_end_st(self):
        return self.__MEM.rdm(self.__addr, self.__coex_timer3_end_st_msb, self.__coex_timer3_end_st_lsb)
    @coex_timer3_end_st.setter
    def coex_timer3_end_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__coex_timer3_end_st_msb, self.__coex_timer3_end_st_lsb, value)

    @property
    def coex_timer2_end_st(self):
        return self.__MEM.rdm(self.__addr, self.__coex_timer2_end_st_msb, self.__coex_timer2_end_st_lsb)
    @coex_timer2_end_st.setter
    def coex_timer2_end_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__coex_timer2_end_st_msb, self.__coex_timer2_end_st_lsb, value)

    @property
    def coex_timer1_end_st(self):
        return self.__MEM.rdm(self.__addr, self.__coex_timer1_end_st_msb, self.__coex_timer1_end_st_lsb)
    @coex_timer1_end_st.setter
    def coex_timer1_end_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__coex_timer1_end_st_msb, self.__coex_timer1_end_st_lsb, value)

    @property
    def coex_timer0_end_st(self):
        return self.__MEM.rdm(self.__addr, self.__coex_timer0_end_st_msb, self.__coex_timer0_end_st_lsb)
    @coex_timer0_end_st.setter
    def coex_timer0_end_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__coex_timer0_end_st_msb, self.__coex_timer0_end_st_lsb, value)
class MACRWBT_COEX_TIMER_END_CLR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x190
        self.__reg_coex_timer11_end_clr_lsb = 11
        self.__reg_coex_timer11_end_clr_msb = 11
        self.__reg_coex_timer10_end_clr_lsb = 10
        self.__reg_coex_timer10_end_clr_msb = 10
        self.__reg_coex_timer9_end_clr_lsb = 9
        self.__reg_coex_timer9_end_clr_msb = 9
        self.__reg_coex_timer8_end_clr_lsb = 8
        self.__reg_coex_timer8_end_clr_msb = 8
        self.__reg_coex_timer7_end_clr_lsb = 7
        self.__reg_coex_timer7_end_clr_msb = 7
        self.__reg_coex_timer6_end_clr_lsb = 6
        self.__reg_coex_timer6_end_clr_msb = 6
        self.__reg_coex_timer5_end_clr_lsb = 5
        self.__reg_coex_timer5_end_clr_msb = 5
        self.__reg_coex_timer4_end_clr_lsb = 4
        self.__reg_coex_timer4_end_clr_msb = 4
        self.__reg_coex_timer3_end_clr_lsb = 3
        self.__reg_coex_timer3_end_clr_msb = 3
        self.__reg_coex_timer2_end_clr_lsb = 2
        self.__reg_coex_timer2_end_clr_msb = 2
        self.__reg_coex_timer1_end_clr_lsb = 1
        self.__reg_coex_timer1_end_clr_msb = 1
        self.__reg_coex_timer0_end_clr_lsb = 0
        self.__reg_coex_timer0_end_clr_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_coex_timer11_end_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer11_end_clr_msb, self.__reg_coex_timer11_end_clr_lsb)
    @reg_coex_timer11_end_clr.setter
    def reg_coex_timer11_end_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer11_end_clr_msb, self.__reg_coex_timer11_end_clr_lsb, value)

    @property
    def reg_coex_timer10_end_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer10_end_clr_msb, self.__reg_coex_timer10_end_clr_lsb)
    @reg_coex_timer10_end_clr.setter
    def reg_coex_timer10_end_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer10_end_clr_msb, self.__reg_coex_timer10_end_clr_lsb, value)

    @property
    def reg_coex_timer9_end_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer9_end_clr_msb, self.__reg_coex_timer9_end_clr_lsb)
    @reg_coex_timer9_end_clr.setter
    def reg_coex_timer9_end_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer9_end_clr_msb, self.__reg_coex_timer9_end_clr_lsb, value)

    @property
    def reg_coex_timer8_end_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer8_end_clr_msb, self.__reg_coex_timer8_end_clr_lsb)
    @reg_coex_timer8_end_clr.setter
    def reg_coex_timer8_end_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer8_end_clr_msb, self.__reg_coex_timer8_end_clr_lsb, value)

    @property
    def reg_coex_timer7_end_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer7_end_clr_msb, self.__reg_coex_timer7_end_clr_lsb)
    @reg_coex_timer7_end_clr.setter
    def reg_coex_timer7_end_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer7_end_clr_msb, self.__reg_coex_timer7_end_clr_lsb, value)

    @property
    def reg_coex_timer6_end_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer6_end_clr_msb, self.__reg_coex_timer6_end_clr_lsb)
    @reg_coex_timer6_end_clr.setter
    def reg_coex_timer6_end_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer6_end_clr_msb, self.__reg_coex_timer6_end_clr_lsb, value)

    @property
    def reg_coex_timer5_end_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer5_end_clr_msb, self.__reg_coex_timer5_end_clr_lsb)
    @reg_coex_timer5_end_clr.setter
    def reg_coex_timer5_end_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer5_end_clr_msb, self.__reg_coex_timer5_end_clr_lsb, value)

    @property
    def reg_coex_timer4_end_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer4_end_clr_msb, self.__reg_coex_timer4_end_clr_lsb)
    @reg_coex_timer4_end_clr.setter
    def reg_coex_timer4_end_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer4_end_clr_msb, self.__reg_coex_timer4_end_clr_lsb, value)

    @property
    def reg_coex_timer3_end_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer3_end_clr_msb, self.__reg_coex_timer3_end_clr_lsb)
    @reg_coex_timer3_end_clr.setter
    def reg_coex_timer3_end_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer3_end_clr_msb, self.__reg_coex_timer3_end_clr_lsb, value)

    @property
    def reg_coex_timer2_end_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer2_end_clr_msb, self.__reg_coex_timer2_end_clr_lsb)
    @reg_coex_timer2_end_clr.setter
    def reg_coex_timer2_end_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer2_end_clr_msb, self.__reg_coex_timer2_end_clr_lsb, value)

    @property
    def reg_coex_timer1_end_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer1_end_clr_msb, self.__reg_coex_timer1_end_clr_lsb)
    @reg_coex_timer1_end_clr.setter
    def reg_coex_timer1_end_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer1_end_clr_msb, self.__reg_coex_timer1_end_clr_lsb, value)

    @property
    def reg_coex_timer0_end_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coex_timer0_end_clr_msb, self.__reg_coex_timer0_end_clr_lsb)
    @reg_coex_timer0_end_clr.setter
    def reg_coex_timer0_end_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coex_timer0_end_clr_msb, self.__reg_coex_timer0_end_clr_lsb, value)
class INT_ENA_MACPWR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x194
        self.__tsf0_reach_int_ena_lsb = 8
        self.__tsf0_reach_int_ena_msb = 8
        self.__tsf1_reach_int_ena_lsb = 7
        self.__tsf1_reach_int_ena_msb = 7
        self.__tsf2_reach_int_ena_lsb = 6
        self.__tsf2_reach_int_ena_msb = 6
        self.__tsf3_reach_int_ena_lsb = 5
        self.__tsf3_reach_int_ena_msb = 5
        self.__tbtt0_int_ena_lsb = 4
        self.__tbtt0_int_ena_msb = 4
        self.__tbtt1_int_ena_lsb = 3
        self.__tbtt1_int_ena_msb = 3
        self.__tbtt2_int_ena_lsb = 2
        self.__tbtt2_int_ena_msb = 2
        self.__tbtt3_int_ena_lsb = 1
        self.__tbtt3_int_ena_msb = 1
        self.__coex_timer_end_int_ena_lsb = 0
        self.__coex_timer_end_int_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tsf0_reach_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__tsf0_reach_int_ena_msb, self.__tsf0_reach_int_ena_lsb)
    @tsf0_reach_int_ena.setter
    def tsf0_reach_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsf0_reach_int_ena_msb, self.__tsf0_reach_int_ena_lsb, value)

    @property
    def tsf1_reach_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__tsf1_reach_int_ena_msb, self.__tsf1_reach_int_ena_lsb)
    @tsf1_reach_int_ena.setter
    def tsf1_reach_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsf1_reach_int_ena_msb, self.__tsf1_reach_int_ena_lsb, value)

    @property
    def tsf2_reach_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__tsf2_reach_int_ena_msb, self.__tsf2_reach_int_ena_lsb)
    @tsf2_reach_int_ena.setter
    def tsf2_reach_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsf2_reach_int_ena_msb, self.__tsf2_reach_int_ena_lsb, value)

    @property
    def tsf3_reach_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__tsf3_reach_int_ena_msb, self.__tsf3_reach_int_ena_lsb)
    @tsf3_reach_int_ena.setter
    def tsf3_reach_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsf3_reach_int_ena_msb, self.__tsf3_reach_int_ena_lsb, value)

    @property
    def tbtt0_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__tbtt0_int_ena_msb, self.__tbtt0_int_ena_lsb)
    @tbtt0_int_ena.setter
    def tbtt0_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__tbtt0_int_ena_msb, self.__tbtt0_int_ena_lsb, value)

    @property
    def tbtt1_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__tbtt1_int_ena_msb, self.__tbtt1_int_ena_lsb)
    @tbtt1_int_ena.setter
    def tbtt1_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__tbtt1_int_ena_msb, self.__tbtt1_int_ena_lsb, value)

    @property
    def tbtt2_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__tbtt2_int_ena_msb, self.__tbtt2_int_ena_lsb)
    @tbtt2_int_ena.setter
    def tbtt2_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__tbtt2_int_ena_msb, self.__tbtt2_int_ena_lsb, value)

    @property
    def tbtt3_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__tbtt3_int_ena_msb, self.__tbtt3_int_ena_lsb)
    @tbtt3_int_ena.setter
    def tbtt3_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__tbtt3_int_ena_msb, self.__tbtt3_int_ena_lsb, value)

    @property
    def coex_timer_end_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__coex_timer_end_int_ena_msb, self.__coex_timer_end_int_ena_lsb)
    @coex_timer_end_int_ena.setter
    def coex_timer_end_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__coex_timer_end_int_ena_msb, self.__coex_timer_end_int_ena_lsb, value)
class INT_RAW_MACPWR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x198
        self.__tsf0_reach_int_raw_lsb = 8
        self.__tsf0_reach_int_raw_msb = 8
        self.__tsf1_reach_int_raw_lsb = 7
        self.__tsf1_reach_int_raw_msb = 7
        self.__tsf2_reach_int_raw_lsb = 6
        self.__tsf2_reach_int_raw_msb = 6
        self.__tsf3_reach_int_raw_lsb = 5
        self.__tsf3_reach_int_raw_msb = 5
        self.__tbtt0_int_raw_lsb = 4
        self.__tbtt0_int_raw_msb = 4
        self.__tbtt1_int_raw_lsb = 3
        self.__tbtt1_int_raw_msb = 3
        self.__tbtt2_int_raw_lsb = 2
        self.__tbtt2_int_raw_msb = 2
        self.__tbtt3_int_raw_lsb = 1
        self.__tbtt3_int_raw_msb = 1
        self.__coex_timer_end_int_raw_lsb = 0
        self.__coex_timer_end_int_raw_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tsf0_reach_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__tsf0_reach_int_raw_msb, self.__tsf0_reach_int_raw_lsb)
    @tsf0_reach_int_raw.setter
    def tsf0_reach_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsf0_reach_int_raw_msb, self.__tsf0_reach_int_raw_lsb, value)

    @property
    def tsf1_reach_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__tsf1_reach_int_raw_msb, self.__tsf1_reach_int_raw_lsb)
    @tsf1_reach_int_raw.setter
    def tsf1_reach_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsf1_reach_int_raw_msb, self.__tsf1_reach_int_raw_lsb, value)

    @property
    def tsf2_reach_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__tsf2_reach_int_raw_msb, self.__tsf2_reach_int_raw_lsb)
    @tsf2_reach_int_raw.setter
    def tsf2_reach_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsf2_reach_int_raw_msb, self.__tsf2_reach_int_raw_lsb, value)

    @property
    def tsf3_reach_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__tsf3_reach_int_raw_msb, self.__tsf3_reach_int_raw_lsb)
    @tsf3_reach_int_raw.setter
    def tsf3_reach_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsf3_reach_int_raw_msb, self.__tsf3_reach_int_raw_lsb, value)

    @property
    def tbtt0_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__tbtt0_int_raw_msb, self.__tbtt0_int_raw_lsb)
    @tbtt0_int_raw.setter
    def tbtt0_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__tbtt0_int_raw_msb, self.__tbtt0_int_raw_lsb, value)

    @property
    def tbtt1_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__tbtt1_int_raw_msb, self.__tbtt1_int_raw_lsb)
    @tbtt1_int_raw.setter
    def tbtt1_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__tbtt1_int_raw_msb, self.__tbtt1_int_raw_lsb, value)

    @property
    def tbtt2_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__tbtt2_int_raw_msb, self.__tbtt2_int_raw_lsb)
    @tbtt2_int_raw.setter
    def tbtt2_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__tbtt2_int_raw_msb, self.__tbtt2_int_raw_lsb, value)

    @property
    def tbtt3_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__tbtt3_int_raw_msb, self.__tbtt3_int_raw_lsb)
    @tbtt3_int_raw.setter
    def tbtt3_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__tbtt3_int_raw_msb, self.__tbtt3_int_raw_lsb, value)

    @property
    def coex_timer_end_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__coex_timer_end_int_raw_msb, self.__coex_timer_end_int_raw_lsb)
    @coex_timer_end_int_raw.setter
    def coex_timer_end_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__coex_timer_end_int_raw_msb, self.__coex_timer_end_int_raw_lsb, value)
class INT_ST_MACPWR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x19c
        self.__tsf0_reach_int_st_lsb = 8
        self.__tsf0_reach_int_st_msb = 8
        self.__tsf1_reach_int_st_lsb = 7
        self.__tsf1_reach_int_st_msb = 7
        self.__tsf2_reach_int_st_lsb = 6
        self.__tsf2_reach_int_st_msb = 6
        self.__tsf3_reach_int_st_lsb = 5
        self.__tsf3_reach_int_st_msb = 5
        self.__tbtt0_int_st_lsb = 4
        self.__tbtt0_int_st_msb = 4
        self.__tbtt1_int_st_lsb = 3
        self.__tbtt1_int_st_msb = 3
        self.__tbtt2_int_st_lsb = 2
        self.__tbtt2_int_st_msb = 2
        self.__tbtt3_int_st_lsb = 1
        self.__tbtt3_int_st_msb = 1
        self.__coex_timer_end_int_st_lsb = 0
        self.__coex_timer_end_int_st_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tsf0_reach_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__tsf0_reach_int_st_msb, self.__tsf0_reach_int_st_lsb)
    @tsf0_reach_int_st.setter
    def tsf0_reach_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsf0_reach_int_st_msb, self.__tsf0_reach_int_st_lsb, value)

    @property
    def tsf1_reach_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__tsf1_reach_int_st_msb, self.__tsf1_reach_int_st_lsb)
    @tsf1_reach_int_st.setter
    def tsf1_reach_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsf1_reach_int_st_msb, self.__tsf1_reach_int_st_lsb, value)

    @property
    def tsf2_reach_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__tsf2_reach_int_st_msb, self.__tsf2_reach_int_st_lsb)
    @tsf2_reach_int_st.setter
    def tsf2_reach_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsf2_reach_int_st_msb, self.__tsf2_reach_int_st_lsb, value)

    @property
    def tsf3_reach_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__tsf3_reach_int_st_msb, self.__tsf3_reach_int_st_lsb)
    @tsf3_reach_int_st.setter
    def tsf3_reach_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsf3_reach_int_st_msb, self.__tsf3_reach_int_st_lsb, value)

    @property
    def tbtt0_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__tbtt0_int_st_msb, self.__tbtt0_int_st_lsb)
    @tbtt0_int_st.setter
    def tbtt0_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__tbtt0_int_st_msb, self.__tbtt0_int_st_lsb, value)

    @property
    def tbtt1_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__tbtt1_int_st_msb, self.__tbtt1_int_st_lsb)
    @tbtt1_int_st.setter
    def tbtt1_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__tbtt1_int_st_msb, self.__tbtt1_int_st_lsb, value)

    @property
    def tbtt2_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__tbtt2_int_st_msb, self.__tbtt2_int_st_lsb)
    @tbtt2_int_st.setter
    def tbtt2_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__tbtt2_int_st_msb, self.__tbtt2_int_st_lsb, value)

    @property
    def tbtt3_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__tbtt3_int_st_msb, self.__tbtt3_int_st_lsb)
    @tbtt3_int_st.setter
    def tbtt3_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__tbtt3_int_st_msb, self.__tbtt3_int_st_lsb, value)

    @property
    def coex_timer_end_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__coex_timer_end_int_st_msb, self.__coex_timer_end_int_st_lsb)
    @coex_timer_end_int_st.setter
    def coex_timer_end_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__coex_timer_end_int_st_msb, self.__coex_timer_end_int_st_lsb, value)
class INT_CLR_MACPWR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x1a0
        self.__tsf0_reach_int_clr_lsb = 8
        self.__tsf0_reach_int_clr_msb = 8
        self.__tsf1_reach_int_clr_lsb = 7
        self.__tsf1_reach_int_clr_msb = 7
        self.__tsf2_reach_int_clr_lsb = 6
        self.__tsf2_reach_int_clr_msb = 6
        self.__tsf3_reach_int_clr_lsb = 5
        self.__tsf3_reach_int_clr_msb = 5
        self.__tbtt0_int_clr_lsb = 4
        self.__tbtt0_int_clr_msb = 4
        self.__tbtt1_int_clr_lsb = 3
        self.__tbtt1_int_clr_msb = 3
        self.__tbtt2_int_clr_lsb = 2
        self.__tbtt2_int_clr_msb = 2
        self.__tbtt3_int_clr_lsb = 1
        self.__tbtt3_int_clr_msb = 1
        self.__coex_timer_end_int_clr_lsb = 0
        self.__coex_timer_end_int_clr_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tsf0_reach_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__tsf0_reach_int_clr_msb, self.__tsf0_reach_int_clr_lsb)
    @tsf0_reach_int_clr.setter
    def tsf0_reach_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsf0_reach_int_clr_msb, self.__tsf0_reach_int_clr_lsb, value)

    @property
    def tsf1_reach_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__tsf1_reach_int_clr_msb, self.__tsf1_reach_int_clr_lsb)
    @tsf1_reach_int_clr.setter
    def tsf1_reach_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsf1_reach_int_clr_msb, self.__tsf1_reach_int_clr_lsb, value)

    @property
    def tsf2_reach_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__tsf2_reach_int_clr_msb, self.__tsf2_reach_int_clr_lsb)
    @tsf2_reach_int_clr.setter
    def tsf2_reach_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsf2_reach_int_clr_msb, self.__tsf2_reach_int_clr_lsb, value)

    @property
    def tsf3_reach_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__tsf3_reach_int_clr_msb, self.__tsf3_reach_int_clr_lsb)
    @tsf3_reach_int_clr.setter
    def tsf3_reach_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__tsf3_reach_int_clr_msb, self.__tsf3_reach_int_clr_lsb, value)

    @property
    def tbtt0_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__tbtt0_int_clr_msb, self.__tbtt0_int_clr_lsb)
    @tbtt0_int_clr.setter
    def tbtt0_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__tbtt0_int_clr_msb, self.__tbtt0_int_clr_lsb, value)

    @property
    def tbtt1_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__tbtt1_int_clr_msb, self.__tbtt1_int_clr_lsb)
    @tbtt1_int_clr.setter
    def tbtt1_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__tbtt1_int_clr_msb, self.__tbtt1_int_clr_lsb, value)

    @property
    def tbtt2_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__tbtt2_int_clr_msb, self.__tbtt2_int_clr_lsb)
    @tbtt2_int_clr.setter
    def tbtt2_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__tbtt2_int_clr_msb, self.__tbtt2_int_clr_lsb, value)

    @property
    def tbtt3_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__tbtt3_int_clr_msb, self.__tbtt3_int_clr_lsb)
    @tbtt3_int_clr.setter
    def tbtt3_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__tbtt3_int_clr_msb, self.__tbtt3_int_clr_lsb, value)

    @property
    def coex_timer_end_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__coex_timer_end_int_clr_msb, self.__coex_timer_end_int_clr_lsb)
    @coex_timer_end_int_clr.setter
    def coex_timer_end_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__coex_timer_end_int_clr_msb, self.__coex_timer_end_int_clr_lsb, value)
class MACCO_EXTERN_CONF0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x1a4
        self.__reg_extern_in0_pti_lsb = 28
        self.__reg_extern_in0_pti_msb = 31
        self.__reg_extern_in1_pti_lsb = 24
        self.__reg_extern_in1_pti_msb = 27
        self.__reg_extern_in2_pti_lsb = 20
        self.__reg_extern_in2_pti_msb = 23
        self.__reg_extern_in3_pti_lsb = 16
        self.__reg_extern_in3_pti_msb = 19
        self.__reg_extern_out0_pti_lsb = 12
        self.__reg_extern_out0_pti_msb = 15
        self.__reg_extern_out1_pti_lsb = 8
        self.__reg_extern_out1_pti_msb = 11
        self.__reg_extern_out2_pti_lsb = 4
        self.__reg_extern_out2_pti_msb = 7
        self.__reg_extern_out3_pti_lsb = 0
        self.__reg_extern_out3_pti_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_extern_in0_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_extern_in0_pti_msb, self.__reg_extern_in0_pti_lsb)
    @reg_extern_in0_pti.setter
    def reg_extern_in0_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_extern_in0_pti_msb, self.__reg_extern_in0_pti_lsb, value)

    @property
    def reg_extern_in1_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_extern_in1_pti_msb, self.__reg_extern_in1_pti_lsb)
    @reg_extern_in1_pti.setter
    def reg_extern_in1_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_extern_in1_pti_msb, self.__reg_extern_in1_pti_lsb, value)

    @property
    def reg_extern_in2_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_extern_in2_pti_msb, self.__reg_extern_in2_pti_lsb)
    @reg_extern_in2_pti.setter
    def reg_extern_in2_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_extern_in2_pti_msb, self.__reg_extern_in2_pti_lsb, value)

    @property
    def reg_extern_in3_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_extern_in3_pti_msb, self.__reg_extern_in3_pti_lsb)
    @reg_extern_in3_pti.setter
    def reg_extern_in3_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_extern_in3_pti_msb, self.__reg_extern_in3_pti_lsb, value)

    @property
    def reg_extern_out0_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_extern_out0_pti_msb, self.__reg_extern_out0_pti_lsb)
    @reg_extern_out0_pti.setter
    def reg_extern_out0_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_extern_out0_pti_msb, self.__reg_extern_out0_pti_lsb, value)

    @property
    def reg_extern_out1_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_extern_out1_pti_msb, self.__reg_extern_out1_pti_lsb)
    @reg_extern_out1_pti.setter
    def reg_extern_out1_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_extern_out1_pti_msb, self.__reg_extern_out1_pti_lsb, value)

    @property
    def reg_extern_out2_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_extern_out2_pti_msb, self.__reg_extern_out2_pti_lsb)
    @reg_extern_out2_pti.setter
    def reg_extern_out2_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_extern_out2_pti_msb, self.__reg_extern_out2_pti_lsb, value)

    @property
    def reg_extern_out3_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_extern_out3_pti_msb, self.__reg_extern_out3_pti_lsb)
    @reg_extern_out3_pti.setter
    def reg_extern_out3_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_extern_out3_pti_msb, self.__reg_extern_out3_pti_lsb, value)
class MACCO_EXTERN_CONF1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x1a8
        self.__reg_extern_ant_follow_wlan_lsb = 0
        self.__reg_extern_ant_follow_wlan_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_extern_ant_follow_wlan(self):
        return self.__MEM.rdm(self.__addr, self.__reg_extern_ant_follow_wlan_msb, self.__reg_extern_ant_follow_wlan_lsb)
    @reg_extern_ant_follow_wlan.setter
    def reg_extern_ant_follow_wlan(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_extern_ant_follow_wlan_msb, self.__reg_extern_ant_follow_wlan_lsb, value)
class MACPWRDATE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x3f8
        self.__reg_macpwr_date_lsb = 0
        self.__reg_macpwr_date_msb = 27
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macpwr_date(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macpwr_date_msb, self.__reg_macpwr_date_lsb)
    @reg_macpwr_date.setter
    def reg_macpwr_date(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macpwr_date_msb, self.__reg_macpwr_date_lsb, value)
    @property
    def default_value(self):
        return 0x1810260
