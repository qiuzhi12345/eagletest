from hal.common import *
from hal.hwregister.hwreg.ESP32.addr_base import *
class MAC_PWR(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.MACCON_TIME = MACCON_TIME(self.channel, self.chipv)
        self.MACEMAC_TIMER_NS = MACEMAC_TIMER_NS(self.channel, self.chipv)
        self.MACEMAC_TIMER_S = MACEMAC_TIMER_S(self.channel, self.chipv)
        self.MACCON_TIME_SW = MACCON_TIME_SW(self.channel, self.chipv)
        self.MACTSF_TIME_FZ = MACTSF_TIME_FZ(self.channel, self.chipv)
        self.MACTSF0_TIME_LO = MACTSF0_TIME_LO(self.channel, self.chipv)
        self.MACTSF0_TIME_HI = MACTSF0_TIME_HI(self.channel, self.chipv)
        self.MACSLEEP_ST = MACSLEEP_ST(self.channel, self.chipv)
        self.MACSLEEP0_CONF = MACSLEEP0_CONF(self.channel, self.chipv)
        self.MACTSFSW0_LO = MACTSFSW0_LO(self.channel, self.chipv)
        self.MACTSFSW0_HI = MACTSFSW0_HI(self.channel, self.chipv)
        self.MACTBTTTAR0_LO = MACTBTTTAR0_LO(self.channel, self.chipv)
        self.MACTBTTTAR0_HI = MACTBTTTAR0_HI(self.channel, self.chipv)
        self.MACWAKETAR0_LO = MACWAKETAR0_LO(self.channel, self.chipv)
        self.MACWAKETAR0_HI = MACWAKETAR0_HI(self.channel, self.chipv)
        self.MACBEACTAR0_LO = MACBEACTAR0_LO(self.channel, self.chipv)
        self.MACBEACTAR0_HI = MACBEACTAR0_HI(self.channel, self.chipv)
        self.MACBEATAR0_LO = MACBEATAR0_LO(self.channel, self.chipv)
        self.MACBEATAR0_HI = MACBEATAR0_HI(self.channel, self.chipv)
        self.MACBEAINTER0 = MACBEAINTER0(self.channel, self.chipv)
        self.MACLISINTER0 = MACLISINTER0(self.channel, self.chipv)
        self.MACTSF1_TIME_LO = MACTSF1_TIME_LO(self.channel, self.chipv)
        self.MACTSF1_TIME_HI = MACTSF1_TIME_HI(self.channel, self.chipv)
        self.MACSLEEP1_CONF = MACSLEEP1_CONF(self.channel, self.chipv)
        self.MACTSFSW1_LO = MACTSFSW1_LO(self.channel, self.chipv)
        self.MACTSFSW1_HI = MACTSFSW1_HI(self.channel, self.chipv)
        self.MACTBTTTAR1_LO = MACTBTTTAR1_LO(self.channel, self.chipv)
        self.MACTBTTTAR1_HI = MACTBTTTAR1_HI(self.channel, self.chipv)
        self.MACWAKETAR1_LO = MACWAKETAR1_LO(self.channel, self.chipv)
        self.MACWAKETAR1_HI = MACWAKETAR1_HI(self.channel, self.chipv)
        self.MACBEACTAR1_LO = MACBEACTAR1_LO(self.channel, self.chipv)
        self.MACBEACTAR1_HI = MACBEACTAR1_HI(self.channel, self.chipv)
        self.MACBEATAR1_LO = MACBEATAR1_LO(self.channel, self.chipv)
        self.MACBEATAR1_HI = MACBEATAR1_HI(self.channel, self.chipv)
        self.MACBEAINTER1 = MACBEAINTER1(self.channel, self.chipv)
        self.MACLISINTER1 = MACLISINTER1(self.channel, self.chipv)
        self.MACTSF2_TIME_LO = MACTSF2_TIME_LO(self.channel, self.chipv)
        self.MACTSF2_TIME_HI = MACTSF2_TIME_HI(self.channel, self.chipv)
        self.MACSLEEP2_CONF = MACSLEEP2_CONF(self.channel, self.chipv)
        self.MACTSFSW2_LO = MACTSFSW2_LO(self.channel, self.chipv)
        self.MACTSFSW2_HI = MACTSFSW2_HI(self.channel, self.chipv)
        self.MACTBTTTAR2_LO = MACTBTTTAR2_LO(self.channel, self.chipv)
        self.MACTBTTTAR2_HI = MACTBTTTAR2_HI(self.channel, self.chipv)
        self.MACWAKETAR2_LO = MACWAKETAR2_LO(self.channel, self.chipv)
        self.MACWAKETAR2_HI = MACWAKETAR2_HI(self.channel, self.chipv)
        self.MACBEACTAR2_LO = MACBEACTAR2_LO(self.channel, self.chipv)
        self.MACBEACTAR2_HI = MACBEACTAR2_HI(self.channel, self.chipv)
        self.MACBEATAR2_LO = MACBEATAR2_LO(self.channel, self.chipv)
        self.MACBEATAR2_HI = MACBEATAR2_HI(self.channel, self.chipv)
        self.MACBEAINTER2 = MACBEAINTER2(self.channel, self.chipv)
        self.MACLISINTER2 = MACLISINTER2(self.channel, self.chipv)
        self.MACTSF3_TIME_LO = MACTSF3_TIME_LO(self.channel, self.chipv)
        self.MACTSF3_TIME_HI = MACTSF3_TIME_HI(self.channel, self.chipv)
        self.MACSLEEP3_CONF = MACSLEEP3_CONF(self.channel, self.chipv)
        self.MACTSFSW3_LO = MACTSFSW3_LO(self.channel, self.chipv)
        self.MACTSFSW3_HI = MACTSFSW3_HI(self.channel, self.chipv)
        self.MACTBTTTAR3_LO = MACTBTTTAR3_LO(self.channel, self.chipv)
        self.MACTBTTTAR3_HI = MACTBTTTAR3_HI(self.channel, self.chipv)
        self.MACWAKETAR3_LO = MACWAKETAR3_LO(self.channel, self.chipv)
        self.MACWAKETAR3_HI = MACWAKETAR3_HI(self.channel, self.chipv)
        self.MACBEACTAR3_LO = MACBEACTAR3_LO(self.channel, self.chipv)
        self.MACBEACTAR3_HI = MACBEACTAR3_HI(self.channel, self.chipv)
        self.MACBEATAR3_LO = MACBEATAR3_LO(self.channel, self.chipv)
        self.MACBEATAR3_HI = MACBEATAR3_HI(self.channel, self.chipv)
        self.MACBEAINTER3 = MACBEAINTER3(self.channel, self.chipv)
        self.MACLISINTER3 = MACLISINTER3(self.channel, self.chipv)
        self.MACRTC_CALI = MACRTC_CALI(self.channel, self.chipv)
        self.MACRTC_CALIVALUE = MACRTC_CALIVALUE(self.channel, self.chipv)
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
        self.MACPWRDATE = MACPWRDATE(self.channel, self.chipv)
class MACCON_TIME(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x0
        self.__contimer_lsb = 0
        self.__contimer_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def contimer(self):
        return self.__MEM.rdm(self.__addr, self.__contimer_msb, self.__contimer_lsb)
    @contimer.setter
    def contimer(self, value):
        return self.__MEM.wrm(self.__addr, self.__contimer_msb, self.__contimer_lsb, value)
class MACEMAC_TIMER_NS(object):
    def __init__(self, channel, chipv = "ESP32"):
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
    def __init__(self, channel, chipv = "ESP32"):
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
class MACCON_TIME_SW(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xc
        self.__reg_contimer_sw_lsb = 0
        self.__reg_contimer_sw_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_contimer_sw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_contimer_sw_msb, self.__reg_contimer_sw_lsb)
    @reg_contimer_sw.setter
    def reg_contimer_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_contimer_sw_msb, self.__reg_contimer_sw_lsb, value)
class MACTSF_TIME_FZ(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x10
        self.__reg_consw_wr_lsb = 10
        self.__reg_consw_wr_msb = 10
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
        self.__reg_contime_fz_lsb = 4
        self.__reg_contime_fz_msb = 4
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
    def reg_consw_wr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_consw_wr_msb, self.__reg_consw_wr_lsb)
    @reg_consw_wr.setter
    def reg_consw_wr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_consw_wr_msb, self.__reg_consw_wr_lsb, value)

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
    def reg_contime_fz(self):
        return self.__MEM.rdm(self.__addr, self.__reg_contime_fz_msb, self.__reg_contime_fz_lsb)
    @reg_contime_fz.setter
    def reg_contime_fz(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_contime_fz_msb, self.__reg_contime_fz_lsb, value)

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
    def __init__(self, channel, chipv = "ESP32"):
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
    def __init__(self, channel, chipv = "ESP32"):
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x1c
        self.__reg_con_upbyrtc_lsb = 24
        self.__reg_con_upbyrtc_msb = 24
        self.__reg_pwr_us_fix_lsb = 23
        self.__reg_pwr_us_fix_msb = 23
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
    def reg_con_upbyrtc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_con_upbyrtc_msb, self.__reg_con_upbyrtc_lsb)
    @reg_con_upbyrtc.setter
    def reg_con_upbyrtc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_con_upbyrtc_msb, self.__reg_con_upbyrtc_lsb, value)

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
    def __init__(self, channel, chipv = "ESP32"):
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
        self.__reg_wakeup_target0_valid_lsb = 26
        self.__reg_wakeup_target0_valid_msb = 26
        self.__reg_beacon_target0_valid_lsb = 25
        self.__reg_beacon_target0_valid_msb = 25
        self.__reg_beacon_target0_upbytsf_lsb = 24
        self.__reg_beacon_target0_upbytsf_msb = 24
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
    def reg_wakeup_target0_valid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wakeup_target0_valid_msb, self.__reg_wakeup_target0_valid_lsb)
    @reg_wakeup_target0_valid.setter
    def reg_wakeup_target0_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wakeup_target0_valid_msb, self.__reg_wakeup_target0_valid_lsb, value)

    @property
    def reg_beacon_target0_valid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacon_target0_valid_msb, self.__reg_beacon_target0_valid_lsb)
    @reg_beacon_target0_valid.setter
    def reg_beacon_target0_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacon_target0_valid_msb, self.__reg_beacon_target0_valid_lsb, value)

    @property
    def reg_beacon_target0_upbytsf(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacon_target0_upbytsf_msb, self.__reg_beacon_target0_upbytsf_lsb)
    @reg_beacon_target0_upbytsf.setter
    def reg_beacon_target0_upbytsf(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacon_target0_upbytsf_msb, self.__reg_beacon_target0_upbytsf_lsb, value)

    @property
    def reg_pwrclk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwrclk_en_msb, self.__reg_pwrclk_en_lsb)
    @reg_pwrclk_en.setter
    def reg_pwrclk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwrclk_en_msb, self.__reg_pwrclk_en_lsb, value)
class MACTSFSW0_LO(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x24
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x28
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
class MACTBTTTAR0_LO(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x2c
        self.__reg_tbttstart_target0_lo_lsb = 0
        self.__reg_tbttstart_target0_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tbttstart_target0_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tbttstart_target0_lo_msb, self.__reg_tbttstart_target0_lo_lsb)
    @reg_tbttstart_target0_lo.setter
    def reg_tbttstart_target0_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tbttstart_target0_lo_msb, self.__reg_tbttstart_target0_lo_lsb, value)
class MACTBTTTAR0_HI(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x30
        self.__reg_tbttstart_target0_hi_lsb = 0
        self.__reg_tbttstart_target0_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tbttstart_target0_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tbttstart_target0_hi_msb, self.__reg_tbttstart_target0_hi_lsb)
    @reg_tbttstart_target0_hi.setter
    def reg_tbttstart_target0_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tbttstart_target0_hi_msb, self.__reg_tbttstart_target0_hi_lsb, value)
class MACWAKETAR0_LO(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x34
        self.__reg_wakeup_target0_lo_lsb = 0
        self.__reg_wakeup_target0_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wakeup_target0_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wakeup_target0_lo_msb, self.__reg_wakeup_target0_lo_lsb)
    @reg_wakeup_target0_lo.setter
    def reg_wakeup_target0_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wakeup_target0_lo_msb, self.__reg_wakeup_target0_lo_lsb, value)
class MACWAKETAR0_HI(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x38
        self.__reg_wakeup_target0_hi_lsb = 0
        self.__reg_wakeup_target0_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wakeup_target0_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wakeup_target0_hi_msb, self.__reg_wakeup_target0_hi_lsb)
    @reg_wakeup_target0_hi.setter
    def reg_wakeup_target0_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wakeup_target0_hi_msb, self.__reg_wakeup_target0_hi_lsb, value)
class MACBEACTAR0_LO(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x3c
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x40
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x44
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x48
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
class MACBEAINTER0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x4c
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
class MACLISINTER0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x50
        self.__reg_listen_interval0_tu_lsb = 0
        self.__reg_listen_interval0_tu_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_listen_interval0_tu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_listen_interval0_tu_msb, self.__reg_listen_interval0_tu_lsb)
    @reg_listen_interval0_tu.setter
    def reg_listen_interval0_tu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_listen_interval0_tu_msb, self.__reg_listen_interval0_tu_lsb, value)
class MACTSF1_TIME_LO(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x54
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x58
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x5c
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
        self.__reg_wakeup_target1_valid_lsb = 26
        self.__reg_wakeup_target1_valid_msb = 26
        self.__reg_beacon_target1_valid_lsb = 25
        self.__reg_beacon_target1_valid_msb = 25
        self.__reg_beacon_target1_upbytsf_lsb = 24
        self.__reg_beacon_target1_upbytsf_msb = 24
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
    def reg_wakeup_target1_valid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wakeup_target1_valid_msb, self.__reg_wakeup_target1_valid_lsb)
    @reg_wakeup_target1_valid.setter
    def reg_wakeup_target1_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wakeup_target1_valid_msb, self.__reg_wakeup_target1_valid_lsb, value)

    @property
    def reg_beacon_target1_valid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacon_target1_valid_msb, self.__reg_beacon_target1_valid_lsb)
    @reg_beacon_target1_valid.setter
    def reg_beacon_target1_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacon_target1_valid_msb, self.__reg_beacon_target1_valid_lsb, value)

    @property
    def reg_beacon_target1_upbytsf(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacon_target1_upbytsf_msb, self.__reg_beacon_target1_upbytsf_lsb)
    @reg_beacon_target1_upbytsf.setter
    def reg_beacon_target1_upbytsf(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacon_target1_upbytsf_msb, self.__reg_beacon_target1_upbytsf_lsb, value)
class MACTSFSW1_LO(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x60
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x64
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
class MACTBTTTAR1_LO(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x68
        self.__reg_tbttstart_target1_lo_lsb = 0
        self.__reg_tbttstart_target1_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tbttstart_target1_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tbttstart_target1_lo_msb, self.__reg_tbttstart_target1_lo_lsb)
    @reg_tbttstart_target1_lo.setter
    def reg_tbttstart_target1_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tbttstart_target1_lo_msb, self.__reg_tbttstart_target1_lo_lsb, value)
class MACTBTTTAR1_HI(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x6c
        self.__reg_tbttstart_target1_hi_lsb = 0
        self.__reg_tbttstart_target1_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tbttstart_target1_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tbttstart_target1_hi_msb, self.__reg_tbttstart_target1_hi_lsb)
    @reg_tbttstart_target1_hi.setter
    def reg_tbttstart_target1_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tbttstart_target1_hi_msb, self.__reg_tbttstart_target1_hi_lsb, value)
class MACWAKETAR1_LO(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x70
        self.__reg_wakeup_target1_lo_lsb = 0
        self.__reg_wakeup_target1_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wakeup_target1_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wakeup_target1_lo_msb, self.__reg_wakeup_target1_lo_lsb)
    @reg_wakeup_target1_lo.setter
    def reg_wakeup_target1_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wakeup_target1_lo_msb, self.__reg_wakeup_target1_lo_lsb, value)
class MACWAKETAR1_HI(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x74
        self.__reg_wakeup_target1_hi_lsb = 0
        self.__reg_wakeup_target1_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wakeup_target1_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wakeup_target1_hi_msb, self.__reg_wakeup_target1_hi_lsb)
    @reg_wakeup_target1_hi.setter
    def reg_wakeup_target1_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wakeup_target1_hi_msb, self.__reg_wakeup_target1_hi_lsb, value)
class MACBEACTAR1_LO(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x78
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x7c
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x80
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x84
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
class MACBEAINTER1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x88
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
class MACLISINTER1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x8c
        self.__reg_listen_interval1_tu_lsb = 0
        self.__reg_listen_interval1_tu_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_listen_interval1_tu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_listen_interval1_tu_msb, self.__reg_listen_interval1_tu_lsb)
    @reg_listen_interval1_tu.setter
    def reg_listen_interval1_tu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_listen_interval1_tu_msb, self.__reg_listen_interval1_tu_lsb, value)
class MACTSF2_TIME_LO(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x90
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x94
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x98
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
        self.__reg_wakeup_target2_valid_lsb = 26
        self.__reg_wakeup_target2_valid_msb = 26
        self.__reg_beacon_target2_valid_lsb = 25
        self.__reg_beacon_target2_valid_msb = 25
        self.__reg_beacon_target2_upbytsf_lsb = 24
        self.__reg_beacon_target2_upbytsf_msb = 24
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
    def reg_wakeup_target2_valid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wakeup_target2_valid_msb, self.__reg_wakeup_target2_valid_lsb)
    @reg_wakeup_target2_valid.setter
    def reg_wakeup_target2_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wakeup_target2_valid_msb, self.__reg_wakeup_target2_valid_lsb, value)

    @property
    def reg_beacon_target2_valid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacon_target2_valid_msb, self.__reg_beacon_target2_valid_lsb)
    @reg_beacon_target2_valid.setter
    def reg_beacon_target2_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacon_target2_valid_msb, self.__reg_beacon_target2_valid_lsb, value)

    @property
    def reg_beacon_target2_upbytsf(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacon_target2_upbytsf_msb, self.__reg_beacon_target2_upbytsf_lsb)
    @reg_beacon_target2_upbytsf.setter
    def reg_beacon_target2_upbytsf(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacon_target2_upbytsf_msb, self.__reg_beacon_target2_upbytsf_lsb, value)
class MACTSFSW2_LO(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x9c
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xa0
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
class MACTBTTTAR2_LO(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xa4
        self.__reg_tbttstart_target2_lo_lsb = 0
        self.__reg_tbttstart_target2_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tbttstart_target2_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tbttstart_target2_lo_msb, self.__reg_tbttstart_target2_lo_lsb)
    @reg_tbttstart_target2_lo.setter
    def reg_tbttstart_target2_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tbttstart_target2_lo_msb, self.__reg_tbttstart_target2_lo_lsb, value)
class MACTBTTTAR2_HI(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xa8
        self.__reg_tbttstart_target2_hi_lsb = 0
        self.__reg_tbttstart_target2_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tbttstart_target2_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tbttstart_target2_hi_msb, self.__reg_tbttstart_target2_hi_lsb)
    @reg_tbttstart_target2_hi.setter
    def reg_tbttstart_target2_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tbttstart_target2_hi_msb, self.__reg_tbttstart_target2_hi_lsb, value)
class MACWAKETAR2_LO(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xac
        self.__reg_wakeup_target2_lo_lsb = 0
        self.__reg_wakeup_target2_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wakeup_target2_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wakeup_target2_lo_msb, self.__reg_wakeup_target2_lo_lsb)
    @reg_wakeup_target2_lo.setter
    def reg_wakeup_target2_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wakeup_target2_lo_msb, self.__reg_wakeup_target2_lo_lsb, value)
class MACWAKETAR2_HI(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xb0
        self.__reg_wakeup_target2_hi_lsb = 0
        self.__reg_wakeup_target2_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wakeup_target2_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wakeup_target2_hi_msb, self.__reg_wakeup_target2_hi_lsb)
    @reg_wakeup_target2_hi.setter
    def reg_wakeup_target2_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wakeup_target2_hi_msb, self.__reg_wakeup_target2_hi_lsb, value)
class MACBEACTAR2_LO(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xb4
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xb8
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xbc
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xc0
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
class MACBEAINTER2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xc4
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
class MACLISINTER2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xc8
        self.__reg_listen_interval2_tu_lsb = 0
        self.__reg_listen_interval2_tu_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_listen_interval2_tu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_listen_interval2_tu_msb, self.__reg_listen_interval2_tu_lsb)
    @reg_listen_interval2_tu.setter
    def reg_listen_interval2_tu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_listen_interval2_tu_msb, self.__reg_listen_interval2_tu_lsb, value)
class MACTSF3_TIME_LO(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xcc
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xd0
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xd4
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
        self.__reg_wakeup_target3_valid_lsb = 26
        self.__reg_wakeup_target3_valid_msb = 26
        self.__reg_beacon_target3_valid_lsb = 25
        self.__reg_beacon_target3_valid_msb = 25
        self.__reg_beacon_target3_upbytsf_lsb = 24
        self.__reg_beacon_target3_upbytsf_msb = 24
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
    def reg_wakeup_target3_valid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wakeup_target3_valid_msb, self.__reg_wakeup_target3_valid_lsb)
    @reg_wakeup_target3_valid.setter
    def reg_wakeup_target3_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wakeup_target3_valid_msb, self.__reg_wakeup_target3_valid_lsb, value)

    @property
    def reg_beacon_target3_valid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacon_target3_valid_msb, self.__reg_beacon_target3_valid_lsb)
    @reg_beacon_target3_valid.setter
    def reg_beacon_target3_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacon_target3_valid_msb, self.__reg_beacon_target3_valid_lsb, value)

    @property
    def reg_beacon_target3_upbytsf(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacon_target3_upbytsf_msb, self.__reg_beacon_target3_upbytsf_lsb)
    @reg_beacon_target3_upbytsf.setter
    def reg_beacon_target3_upbytsf(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacon_target3_upbytsf_msb, self.__reg_beacon_target3_upbytsf_lsb, value)
class MACTSFSW3_LO(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xd8
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xdc
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
class MACTBTTTAR3_LO(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xe0
        self.__reg_tbttstart_target3_lo_lsb = 0
        self.__reg_tbttstart_target3_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tbttstart_target3_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tbttstart_target3_lo_msb, self.__reg_tbttstart_target3_lo_lsb)
    @reg_tbttstart_target3_lo.setter
    def reg_tbttstart_target3_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tbttstart_target3_lo_msb, self.__reg_tbttstart_target3_lo_lsb, value)
class MACTBTTTAR3_HI(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xe4
        self.__reg_tbttstart_target3_hi_lsb = 0
        self.__reg_tbttstart_target3_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tbttstart_target3_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tbttstart_target3_hi_msb, self.__reg_tbttstart_target3_hi_lsb)
    @reg_tbttstart_target3_hi.setter
    def reg_tbttstart_target3_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tbttstart_target3_hi_msb, self.__reg_tbttstart_target3_hi_lsb, value)
class MACWAKETAR3_LO(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xe8
        self.__reg_wakeup_target3_lo_lsb = 0
        self.__reg_wakeup_target3_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wakeup_target3_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wakeup_target3_lo_msb, self.__reg_wakeup_target3_lo_lsb)
    @reg_wakeup_target3_lo.setter
    def reg_wakeup_target3_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wakeup_target3_lo_msb, self.__reg_wakeup_target3_lo_lsb, value)
class MACWAKETAR3_HI(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xec
        self.__reg_wakeup_target3_hi_lsb = 0
        self.__reg_wakeup_target3_hi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wakeup_target3_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wakeup_target3_hi_msb, self.__reg_wakeup_target3_hi_lsb)
    @reg_wakeup_target3_hi.setter
    def reg_wakeup_target3_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wakeup_target3_hi_msb, self.__reg_wakeup_target3_hi_lsb, value)
class MACBEACTAR3_LO(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xf0
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xf4
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xf8
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0xfc
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
class MACBEAINTER3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x100
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
class MACLISINTER3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x104
        self.__reg_listen_interval3_tu_lsb = 0
        self.__reg_listen_interval3_tu_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_listen_interval3_tu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_listen_interval3_tu_msb, self.__reg_listen_interval3_tu_lsb)
    @reg_listen_interval3_tu.setter
    def reg_listen_interval3_tu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_listen_interval3_tu_msb, self.__reg_listen_interval3_tu_lsb, value)
class MACRTC_CALI(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x108
        self.__reg_rtccali_auto_ena_lsb = 31
        self.__reg_rtccali_auto_ena_msb = 31
        self.__reg_rtccali_start_lsb = 30
        self.__reg_rtccali_start_msb = 30
        self.__reg_rtccali_max_lsb = 0
        self.__reg_rtccali_max_msb = 12
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rtccali_auto_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtccali_auto_ena_msb, self.__reg_rtccali_auto_ena_lsb)
    @reg_rtccali_auto_ena.setter
    def reg_rtccali_auto_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtccali_auto_ena_msb, self.__reg_rtccali_auto_ena_lsb, value)

    @property
    def reg_rtccali_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtccali_start_msb, self.__reg_rtccali_start_lsb)
    @reg_rtccali_start.setter
    def reg_rtccali_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtccali_start_msb, self.__reg_rtccali_start_lsb, value)

    @property
    def reg_rtccali_max(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtccali_max_msb, self.__reg_rtccali_max_lsb)
    @reg_rtccali_max.setter
    def reg_rtccali_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtccali_max_msb, self.__reg_rtccali_max_lsb, value)
class MACRTC_CALIVALUE(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x10c
        self.__rtccali_rdy_lsb = 31
        self.__rtccali_rdy_msb = 31
        self.__cali_value_lsb = 0
        self.__cali_value_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtccali_rdy(self):
        return self.__MEM.rdm(self.__addr, self.__rtccali_rdy_msb, self.__rtccali_rdy_lsb)
    @rtccali_rdy.setter
    def rtccali_rdy(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtccali_rdy_msb, self.__rtccali_rdy_lsb, value)

    @property
    def cali_value(self):
        return self.__MEM.rdm(self.__addr, self.__cali_value_msb, self.__cali_value_lsb)
    @cali_value.setter
    def cali_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__cali_value_msb, self.__cali_value_lsb, value)
class MACRTC_CALISW(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x110
        self.__reg_calisw_ena_lsb = 31
        self.__reg_calisw_ena_msb = 31
        self.__reg_calisw_value_lsb = 0
        self.__reg_calisw_value_msb = 17
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_calisw_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_calisw_ena_msb, self.__reg_calisw_ena_lsb)
    @reg_calisw_ena.setter
    def reg_calisw_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_calisw_ena_msb, self.__reg_calisw_ena_lsb, value)

    @property
    def reg_calisw_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_calisw_value_msb, self.__reg_calisw_value_lsb)
    @reg_calisw_value.setter
    def reg_calisw_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_calisw_value_msb, self.__reg_calisw_value_lsb, value)
class MACTSF0TIMER_ENA(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x114
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x118
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x11c
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x120
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x124
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x128
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x12c
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x130
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x134
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x138
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x13c
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x140
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x144
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_PWR_BASE + 0x148
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
class MACPWRDATE(object):
    def __init__(self, channel, chipv = "ESP32"):
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
        return 0x1604141
