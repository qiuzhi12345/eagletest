from hal.common import *
from hal.hwregister.hwreg.ESP32.addr_base import *
class RTC_CNTL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.RTC_OPTIONS0 = RTC_OPTIONS0(self.channel, self.chipv)
        self.RTC_SLP_TIMER0 = RTC_SLP_TIMER0(self.channel, self.chipv)
        self.RTC_SLP_TIMER1 = RTC_SLP_TIMER1(self.channel, self.chipv)
        self.RTC_TIME_UPDATE = RTC_TIME_UPDATE(self.channel, self.chipv)
        self.RTC_TIME0 = RTC_TIME0(self.channel, self.chipv)
        self.RTC_TIME1 = RTC_TIME1(self.channel, self.chipv)
        self.RTC_STATE0 = RTC_STATE0(self.channel, self.chipv)
        self.RTC_TIMER1 = RTC_TIMER1(self.channel, self.chipv)
        self.RTC_TIMER2 = RTC_TIMER2(self.channel, self.chipv)
        self.RTC_TIMER3 = RTC_TIMER3(self.channel, self.chipv)
        self.RTC_TIMER4 = RTC_TIMER4(self.channel, self.chipv)
        self.RTC_TIMER5 = RTC_TIMER5(self.channel, self.chipv)
        self.RTC_ANA_CONF = RTC_ANA_CONF(self.channel, self.chipv)
        self.RTC_RESET_STATE = RTC_RESET_STATE(self.channel, self.chipv)
        self.RTC_WAKEUP_STATE = RTC_WAKEUP_STATE(self.channel, self.chipv)
        self.INT_ENA_RTC = INT_ENA_RTC(self.channel, self.chipv)
        self.INT_RAW_RTC = INT_RAW_RTC(self.channel, self.chipv)
        self.INT_ST_RTC = INT_ST_RTC(self.channel, self.chipv)
        self.INT_CLR_RTC = INT_CLR_RTC(self.channel, self.chipv)
        self.RTC_STORE0 = RTC_STORE0(self.channel, self.chipv)
        self.RTC_STORE1 = RTC_STORE1(self.channel, self.chipv)
        self.RTC_STORE2 = RTC_STORE2(self.channel, self.chipv)
        self.RTC_STORE3 = RTC_STORE3(self.channel, self.chipv)
        self.RTC_EXT_XTL_CONF = RTC_EXT_XTL_CONF(self.channel, self.chipv)
        self.RTC_EXT_WAKEUP_CONF = RTC_EXT_WAKEUP_CONF(self.channel, self.chipv)
        self.RTC_SLP_REJECT_CONF = RTC_SLP_REJECT_CONF(self.channel, self.chipv)
        self.RTC_CPU_PERIOD_CONF = RTC_CPU_PERIOD_CONF(self.channel, self.chipv)
        self.RTC_SDIO_ACT_CONF = RTC_SDIO_ACT_CONF(self.channel, self.chipv)
        self.RTC_CLK_CONF = RTC_CLK_CONF(self.channel, self.chipv)
        self.RTC_SDIO_CONF = RTC_SDIO_CONF(self.channel, self.chipv)
        self.RTC_BIAS_CONF = RTC_BIAS_CONF(self.channel, self.chipv)
        self.RTC_REG = RTC_REG(self.channel, self.chipv)
        self.RTC_PWC = RTC_PWC(self.channel, self.chipv)
        self.DIG_PWC = DIG_PWC(self.channel, self.chipv)
        self.DIG_ISO = DIG_ISO(self.channel, self.chipv)
        self.RTC_WDTCONFIG0 = RTC_WDTCONFIG0(self.channel, self.chipv)
        self.RTC_WDTCONFIG1 = RTC_WDTCONFIG1(self.channel, self.chipv)
        self.RTC_WDTCONFIG2 = RTC_WDTCONFIG2(self.channel, self.chipv)
        self.RTC_WDTCONFIG3 = RTC_WDTCONFIG3(self.channel, self.chipv)
        self.RTC_WDTCONFIG4 = RTC_WDTCONFIG4(self.channel, self.chipv)
        self.RTC_WDTFEED = RTC_WDTFEED(self.channel, self.chipv)
        self.RTC_WDTWPROTECT = RTC_WDTWPROTECT(self.channel, self.chipv)
        self.RTC_TEST_MUX = RTC_TEST_MUX(self.channel, self.chipv)
        self.RTC_SW_CPU_STALL = RTC_SW_CPU_STALL(self.channel, self.chipv)
        self.RTC_STORE4 = RTC_STORE4(self.channel, self.chipv)
        self.RTC_STORE5 = RTC_STORE5(self.channel, self.chipv)
        self.RTC_STORE6 = RTC_STORE6(self.channel, self.chipv)
        self.RTC_STORE7 = RTC_STORE7(self.channel, self.chipv)
        self.RTC_DIAG0 = RTC_DIAG0(self.channel, self.chipv)
        self.RTC_DIAG1 = RTC_DIAG1(self.channel, self.chipv)
        self.RTC_HOLD_FORCE = RTC_HOLD_FORCE(self.channel, self.chipv)
        self.RTC_EXT_WAKEUP1 = RTC_EXT_WAKEUP1(self.channel, self.chipv)
        self.RTC_EXT_WAKEUP1_STATUS = RTC_EXT_WAKEUP1_STATUS(self.channel, self.chipv)
        self.RTC_BROWN_OUT = RTC_BROWN_OUT(self.channel, self.chipv)
        self.RTC_CNTL_DATE = RTC_CNTL_DATE(self.channel, self.chipv)
class RTC_OPTIONS0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x0
        self.__sw_sys_rst_lsb = 31
        self.__sw_sys_rst_msb = 31
        self.__reg_dg_wrap_force_norst_lsb = 30
        self.__reg_dg_wrap_force_norst_msb = 30
        self.__reg_dg_wrap_force_rst_lsb = 29
        self.__reg_dg_wrap_force_rst_msb = 29
        self.__reg_analog_force_noiso_lsb = 28
        self.__reg_analog_force_noiso_msb = 28
        self.__reg_pll_force_noiso_lsb = 27
        self.__reg_pll_force_noiso_msb = 27
        self.__reg_xtl_force_noiso_lsb = 26
        self.__reg_xtl_force_noiso_msb = 26
        self.__reg_analog_force_iso_lsb = 25
        self.__reg_analog_force_iso_msb = 25
        self.__reg_pll_force_iso_lsb = 24
        self.__reg_pll_force_iso_msb = 24
        self.__reg_xtl_force_iso_lsb = 23
        self.__reg_xtl_force_iso_msb = 23
        self.__reg_bias_core_force_pu_lsb = 22
        self.__reg_bias_core_force_pu_msb = 22
        self.__reg_bias_core_force_pd_lsb = 21
        self.__reg_bias_core_force_pd_msb = 21
        self.__reg_bias_core_folw_12m_lsb = 20
        self.__reg_bias_core_folw_12m_msb = 20
        self.__reg_bias_i2c_force_pu_lsb = 19
        self.__reg_bias_i2c_force_pu_msb = 19
        self.__reg_bias_i2c_force_pd_lsb = 18
        self.__reg_bias_i2c_force_pd_msb = 18
        self.__reg_bias_i2c_folw_12m_lsb = 17
        self.__reg_bias_i2c_folw_12m_msb = 17
        self.__reg_bias_force_nosleep_lsb = 16
        self.__reg_bias_force_nosleep_msb = 16
        self.__reg_bias_force_sleep_lsb = 15
        self.__reg_bias_force_sleep_msb = 15
        self.__reg_bias_sleep_folw_12m_lsb = 14
        self.__reg_bias_sleep_folw_12m_msb = 14
        self.__reg_xtl_force_pu_lsb = 13
        self.__reg_xtl_force_pu_msb = 13
        self.__reg_xtl_force_pd_lsb = 12
        self.__reg_xtl_force_pd_msb = 12
        self.__reg_bbpll_force_pu_lsb = 11
        self.__reg_bbpll_force_pu_msb = 11
        self.__reg_bbpll_force_pd_lsb = 10
        self.__reg_bbpll_force_pd_msb = 10
        self.__reg_bbpll_i2c_force_pu_lsb = 9
        self.__reg_bbpll_i2c_force_pu_msb = 9
        self.__reg_bbpll_i2c_force_pd_lsb = 8
        self.__reg_bbpll_i2c_force_pd_msb = 8
        self.__reg_bb_i2c_force_pu_lsb = 7
        self.__reg_bb_i2c_force_pu_msb = 7
        self.__reg_bb_i2c_force_pd_lsb = 6
        self.__reg_bb_i2c_force_pd_msb = 6
        self.__sw_procpu_rst_lsb = 5
        self.__sw_procpu_rst_msb = 5
        self.__sw_appcpu_rst_lsb = 4
        self.__sw_appcpu_rst_msb = 4
        self.__reg_sw_stall_procpu_c0_lsb = 2
        self.__reg_sw_stall_procpu_c0_msb = 3
        self.__reg_sw_stall_appcpu_c0_lsb = 0
        self.__reg_sw_stall_appcpu_c0_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sw_sys_rst(self):
        return self.__MEM.rdm(self.__addr, self.__sw_sys_rst_msb, self.__sw_sys_rst_lsb)
    @sw_sys_rst.setter
    def sw_sys_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__sw_sys_rst_msb, self.__sw_sys_rst_lsb, value)

    @property
    def reg_dg_wrap_force_norst(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dg_wrap_force_norst_msb, self.__reg_dg_wrap_force_norst_lsb)
    @reg_dg_wrap_force_norst.setter
    def reg_dg_wrap_force_norst(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dg_wrap_force_norst_msb, self.__reg_dg_wrap_force_norst_lsb, value)

    @property
    def reg_dg_wrap_force_rst(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dg_wrap_force_rst_msb, self.__reg_dg_wrap_force_rst_lsb)
    @reg_dg_wrap_force_rst.setter
    def reg_dg_wrap_force_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dg_wrap_force_rst_msb, self.__reg_dg_wrap_force_rst_lsb, value)

    @property
    def reg_analog_force_noiso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_analog_force_noiso_msb, self.__reg_analog_force_noiso_lsb)
    @reg_analog_force_noiso.setter
    def reg_analog_force_noiso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_analog_force_noiso_msb, self.__reg_analog_force_noiso_lsb, value)

    @property
    def reg_pll_force_noiso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pll_force_noiso_msb, self.__reg_pll_force_noiso_lsb)
    @reg_pll_force_noiso.setter
    def reg_pll_force_noiso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pll_force_noiso_msb, self.__reg_pll_force_noiso_lsb, value)

    @property
    def reg_xtl_force_noiso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xtl_force_noiso_msb, self.__reg_xtl_force_noiso_lsb)
    @reg_xtl_force_noiso.setter
    def reg_xtl_force_noiso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xtl_force_noiso_msb, self.__reg_xtl_force_noiso_lsb, value)

    @property
    def reg_analog_force_iso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_analog_force_iso_msb, self.__reg_analog_force_iso_lsb)
    @reg_analog_force_iso.setter
    def reg_analog_force_iso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_analog_force_iso_msb, self.__reg_analog_force_iso_lsb, value)

    @property
    def reg_pll_force_iso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pll_force_iso_msb, self.__reg_pll_force_iso_lsb)
    @reg_pll_force_iso.setter
    def reg_pll_force_iso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pll_force_iso_msb, self.__reg_pll_force_iso_lsb, value)

    @property
    def reg_xtl_force_iso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xtl_force_iso_msb, self.__reg_xtl_force_iso_lsb)
    @reg_xtl_force_iso.setter
    def reg_xtl_force_iso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xtl_force_iso_msb, self.__reg_xtl_force_iso_lsb, value)

    @property
    def reg_bias_core_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bias_core_force_pu_msb, self.__reg_bias_core_force_pu_lsb)
    @reg_bias_core_force_pu.setter
    def reg_bias_core_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bias_core_force_pu_msb, self.__reg_bias_core_force_pu_lsb, value)

    @property
    def reg_bias_core_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bias_core_force_pd_msb, self.__reg_bias_core_force_pd_lsb)
    @reg_bias_core_force_pd.setter
    def reg_bias_core_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bias_core_force_pd_msb, self.__reg_bias_core_force_pd_lsb, value)

    @property
    def reg_bias_core_folw_12m(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bias_core_folw_12m_msb, self.__reg_bias_core_folw_12m_lsb)
    @reg_bias_core_folw_12m.setter
    def reg_bias_core_folw_12m(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bias_core_folw_12m_msb, self.__reg_bias_core_folw_12m_lsb, value)

    @property
    def reg_bias_i2c_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bias_i2c_force_pu_msb, self.__reg_bias_i2c_force_pu_lsb)
    @reg_bias_i2c_force_pu.setter
    def reg_bias_i2c_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bias_i2c_force_pu_msb, self.__reg_bias_i2c_force_pu_lsb, value)

    @property
    def reg_bias_i2c_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bias_i2c_force_pd_msb, self.__reg_bias_i2c_force_pd_lsb)
    @reg_bias_i2c_force_pd.setter
    def reg_bias_i2c_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bias_i2c_force_pd_msb, self.__reg_bias_i2c_force_pd_lsb, value)

    @property
    def reg_bias_i2c_folw_12m(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bias_i2c_folw_12m_msb, self.__reg_bias_i2c_folw_12m_lsb)
    @reg_bias_i2c_folw_12m.setter
    def reg_bias_i2c_folw_12m(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bias_i2c_folw_12m_msb, self.__reg_bias_i2c_folw_12m_lsb, value)

    @property
    def reg_bias_force_nosleep(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bias_force_nosleep_msb, self.__reg_bias_force_nosleep_lsb)
    @reg_bias_force_nosleep.setter
    def reg_bias_force_nosleep(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bias_force_nosleep_msb, self.__reg_bias_force_nosleep_lsb, value)

    @property
    def reg_bias_force_sleep(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bias_force_sleep_msb, self.__reg_bias_force_sleep_lsb)
    @reg_bias_force_sleep.setter
    def reg_bias_force_sleep(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bias_force_sleep_msb, self.__reg_bias_force_sleep_lsb, value)

    @property
    def reg_bias_sleep_folw_12m(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bias_sleep_folw_12m_msb, self.__reg_bias_sleep_folw_12m_lsb)
    @reg_bias_sleep_folw_12m.setter
    def reg_bias_sleep_folw_12m(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bias_sleep_folw_12m_msb, self.__reg_bias_sleep_folw_12m_lsb, value)

    @property
    def reg_xtl_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xtl_force_pu_msb, self.__reg_xtl_force_pu_lsb)
    @reg_xtl_force_pu.setter
    def reg_xtl_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xtl_force_pu_msb, self.__reg_xtl_force_pu_lsb, value)

    @property
    def reg_xtl_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xtl_force_pd_msb, self.__reg_xtl_force_pd_lsb)
    @reg_xtl_force_pd.setter
    def reg_xtl_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xtl_force_pd_msb, self.__reg_xtl_force_pd_lsb, value)

    @property
    def reg_bbpll_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbpll_force_pu_msb, self.__reg_bbpll_force_pu_lsb)
    @reg_bbpll_force_pu.setter
    def reg_bbpll_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbpll_force_pu_msb, self.__reg_bbpll_force_pu_lsb, value)

    @property
    def reg_bbpll_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbpll_force_pd_msb, self.__reg_bbpll_force_pd_lsb)
    @reg_bbpll_force_pd.setter
    def reg_bbpll_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbpll_force_pd_msb, self.__reg_bbpll_force_pd_lsb, value)

    @property
    def reg_bbpll_i2c_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbpll_i2c_force_pu_msb, self.__reg_bbpll_i2c_force_pu_lsb)
    @reg_bbpll_i2c_force_pu.setter
    def reg_bbpll_i2c_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbpll_i2c_force_pu_msb, self.__reg_bbpll_i2c_force_pu_lsb, value)

    @property
    def reg_bbpll_i2c_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbpll_i2c_force_pd_msb, self.__reg_bbpll_i2c_force_pd_lsb)
    @reg_bbpll_i2c_force_pd.setter
    def reg_bbpll_i2c_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbpll_i2c_force_pd_msb, self.__reg_bbpll_i2c_force_pd_lsb, value)

    @property
    def reg_bb_i2c_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_i2c_force_pu_msb, self.__reg_bb_i2c_force_pu_lsb)
    @reg_bb_i2c_force_pu.setter
    def reg_bb_i2c_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_i2c_force_pu_msb, self.__reg_bb_i2c_force_pu_lsb, value)

    @property
    def reg_bb_i2c_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_i2c_force_pd_msb, self.__reg_bb_i2c_force_pd_lsb)
    @reg_bb_i2c_force_pd.setter
    def reg_bb_i2c_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_i2c_force_pd_msb, self.__reg_bb_i2c_force_pd_lsb, value)

    @property
    def sw_procpu_rst(self):
        return self.__MEM.rdm(self.__addr, self.__sw_procpu_rst_msb, self.__sw_procpu_rst_lsb)
    @sw_procpu_rst.setter
    def sw_procpu_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__sw_procpu_rst_msb, self.__sw_procpu_rst_lsb, value)

    @property
    def sw_appcpu_rst(self):
        return self.__MEM.rdm(self.__addr, self.__sw_appcpu_rst_msb, self.__sw_appcpu_rst_lsb)
    @sw_appcpu_rst.setter
    def sw_appcpu_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__sw_appcpu_rst_msb, self.__sw_appcpu_rst_lsb, value)

    @property
    def reg_sw_stall_procpu_c0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sw_stall_procpu_c0_msb, self.__reg_sw_stall_procpu_c0_lsb)
    @reg_sw_stall_procpu_c0.setter
    def reg_sw_stall_procpu_c0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sw_stall_procpu_c0_msb, self.__reg_sw_stall_procpu_c0_lsb, value)

    @property
    def reg_sw_stall_appcpu_c0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sw_stall_appcpu_c0_msb, self.__reg_sw_stall_appcpu_c0_lsb)
    @reg_sw_stall_appcpu_c0.setter
    def reg_sw_stall_appcpu_c0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sw_stall_appcpu_c0_msb, self.__reg_sw_stall_appcpu_c0_lsb, value)
class RTC_SLP_TIMER0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x4
        self.__reg_slp_val_lo_lsb = 0
        self.__reg_slp_val_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_slp_val_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_slp_val_lo_msb, self.__reg_slp_val_lo_lsb)
    @reg_slp_val_lo.setter
    def reg_slp_val_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_slp_val_lo_msb, self.__reg_slp_val_lo_lsb, value)
class RTC_SLP_TIMER1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x8
        self.__reg_rtc_main_timer_alarm_en_lsb = 16
        self.__reg_rtc_main_timer_alarm_en_msb = 16
        self.__reg_slp_val_hi_lsb = 0
        self.__reg_slp_val_hi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rtc_main_timer_alarm_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_main_timer_alarm_en_msb, self.__reg_rtc_main_timer_alarm_en_lsb)
    @reg_rtc_main_timer_alarm_en.setter
    def reg_rtc_main_timer_alarm_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_main_timer_alarm_en_msb, self.__reg_rtc_main_timer_alarm_en_lsb, value)

    @property
    def reg_slp_val_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_slp_val_hi_msb, self.__reg_slp_val_hi_lsb)
    @reg_slp_val_hi.setter
    def reg_slp_val_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_slp_val_hi_msb, self.__reg_slp_val_hi_lsb, value)
class RTC_TIME_UPDATE(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0xc
        self.__rtc_time_update_lsb = 31
        self.__rtc_time_update_msb = 31
        self.__rtc_time_valid_lsb = 30
        self.__rtc_time_valid_msb = 30
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_time_update(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_time_update_msb, self.__rtc_time_update_lsb)
    @rtc_time_update.setter
    def rtc_time_update(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_time_update_msb, self.__rtc_time_update_lsb, value)
    @property
    def default_value(self):
        return 0x0

    @property
    def rtc_time_valid(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_time_valid_msb, self.__rtc_time_valid_lsb)
    @rtc_time_valid.setter
    def rtc_time_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_time_valid_msb, self.__rtc_time_valid_lsb, value)
class RTC_TIME0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x10
        self.__rtc_time_lo_lsb = 0
        self.__rtc_time_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_time_lo(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_time_lo_msb, self.__rtc_time_lo_lsb)
    @rtc_time_lo.setter
    def rtc_time_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_time_lo_msb, self.__rtc_time_lo_lsb, value)
class RTC_TIME1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x14
        self.__rtc_time_hi_lsb = 0
        self.__rtc_time_hi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_time_hi(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_time_hi_msb, self.__rtc_time_hi_lsb)
    @rtc_time_hi.setter
    def rtc_time_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_time_hi_msb, self.__rtc_time_hi_lsb, value)
class RTC_STATE0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x18
        self.__reg_sleep_en_lsb = 31
        self.__reg_sleep_en_msb = 31
        self.__slp_reject_lsb = 30
        self.__slp_reject_msb = 30
        self.__slp_wakeup_lsb = 29
        self.__slp_wakeup_msb = 29
        self.__sdio_active_ind_lsb = 28
        self.__sdio_active_ind_msb = 28
        self.__reg_sar_slp_timer_en_lsb = 24
        self.__reg_sar_slp_timer_en_msb = 24
        self.__reg_touch_slp_timer_en_lsb = 23
        self.__reg_touch_slp_timer_en_msb = 23
        self.__reg_apb2rtc_bridge_sel_lsb = 22
        self.__reg_apb2rtc_bridge_sel_msb = 22
        self.__reg_sar_wakeup_force_en_lsb = 21
        self.__reg_sar_wakeup_force_en_msb = 21
        self.__reg_touch_wakeup_force_en_lsb = 20
        self.__reg_touch_wakeup_force_en_msb = 20
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sleep_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sleep_en_msb, self.__reg_sleep_en_lsb)
    @reg_sleep_en.setter
    def reg_sleep_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sleep_en_msb, self.__reg_sleep_en_lsb, value)

    @property
    def slp_reject(self):
        return self.__MEM.rdm(self.__addr, self.__slp_reject_msb, self.__slp_reject_lsb)
    @slp_reject.setter
    def slp_reject(self, value):
        return self.__MEM.wrm(self.__addr, self.__slp_reject_msb, self.__slp_reject_lsb, value)

    @property
    def slp_wakeup(self):
        return self.__MEM.rdm(self.__addr, self.__slp_wakeup_msb, self.__slp_wakeup_lsb)
    @slp_wakeup.setter
    def slp_wakeup(self, value):
        return self.__MEM.wrm(self.__addr, self.__slp_wakeup_msb, self.__slp_wakeup_lsb, value)

    @property
    def sdio_active_ind(self):
        return self.__MEM.rdm(self.__addr, self.__sdio_active_ind_msb, self.__sdio_active_ind_lsb)
    @sdio_active_ind.setter
    def sdio_active_ind(self, value):
        return self.__MEM.wrm(self.__addr, self.__sdio_active_ind_msb, self.__sdio_active_ind_lsb, value)

    @property
    def reg_sar_slp_timer_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar_slp_timer_en_msb, self.__reg_sar_slp_timer_en_lsb)
    @reg_sar_slp_timer_en.setter
    def reg_sar_slp_timer_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar_slp_timer_en_msb, self.__reg_sar_slp_timer_en_lsb, value)

    @property
    def reg_touch_slp_timer_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_slp_timer_en_msb, self.__reg_touch_slp_timer_en_lsb)
    @reg_touch_slp_timer_en.setter
    def reg_touch_slp_timer_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_slp_timer_en_msb, self.__reg_touch_slp_timer_en_lsb, value)

    @property
    def reg_apb2rtc_bridge_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_apb2rtc_bridge_sel_msb, self.__reg_apb2rtc_bridge_sel_lsb)
    @reg_apb2rtc_bridge_sel.setter
    def reg_apb2rtc_bridge_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_apb2rtc_bridge_sel_msb, self.__reg_apb2rtc_bridge_sel_lsb, value)

    @property
    def reg_sar_wakeup_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar_wakeup_force_en_msb, self.__reg_sar_wakeup_force_en_lsb)
    @reg_sar_wakeup_force_en.setter
    def reg_sar_wakeup_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar_wakeup_force_en_msb, self.__reg_sar_wakeup_force_en_lsb, value)

    @property
    def reg_touch_wakeup_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_wakeup_force_en_msb, self.__reg_touch_wakeup_force_en_lsb)
    @reg_touch_wakeup_force_en.setter
    def reg_touch_wakeup_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_wakeup_force_en_msb, self.__reg_touch_wakeup_force_en_lsb, value)
class RTC_TIMER1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x1c
        self.__pll_buf_wait_lsb = 24
        self.__pll_buf_wait_msb = 31
        self.__xtl_buf_wait_lsb = 14
        self.__xtl_buf_wait_msb = 23
        self.__reg_ck12m_wait_lsb = 6
        self.__reg_ck12m_wait_msb = 13
        self.__reg_cpu_stall_wait_lsb = 1
        self.__reg_cpu_stall_wait_msb = 5
        self.__reg_cpu_stall_en_lsb = 0
        self.__reg_cpu_stall_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pll_buf_wait(self):
        return self.__MEM.rdm(self.__addr, self.__pll_buf_wait_msb, self.__pll_buf_wait_lsb)
    @pll_buf_wait.setter
    def pll_buf_wait(self, value):
        return self.__MEM.wrm(self.__addr, self.__pll_buf_wait_msb, self.__pll_buf_wait_lsb, value)

    @property
    def xtl_buf_wait(self):
        return self.__MEM.rdm(self.__addr, self.__xtl_buf_wait_msb, self.__xtl_buf_wait_lsb)
    @xtl_buf_wait.setter
    def xtl_buf_wait(self, value):
        return self.__MEM.wrm(self.__addr, self.__xtl_buf_wait_msb, self.__xtl_buf_wait_lsb, value)

    @property
    def reg_ck12m_wait(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ck12m_wait_msb, self.__reg_ck12m_wait_lsb)
    @reg_ck12m_wait.setter
    def reg_ck12m_wait(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ck12m_wait_msb, self.__reg_ck12m_wait_lsb, value)

    @property
    def reg_cpu_stall_wait(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cpu_stall_wait_msb, self.__reg_cpu_stall_wait_lsb)
    @reg_cpu_stall_wait.setter
    def reg_cpu_stall_wait(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cpu_stall_wait_msb, self.__reg_cpu_stall_wait_lsb, value)

    @property
    def reg_cpu_stall_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cpu_stall_en_msb, self.__reg_cpu_stall_en_lsb)
    @reg_cpu_stall_en.setter
    def reg_cpu_stall_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cpu_stall_en_msb, self.__reg_cpu_stall_en_lsb, value)
class RTC_TIMER2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x20
        self.__reg_min_time_ck12m_off_lsb = 24
        self.__reg_min_time_ck12m_off_msb = 31
        self.__reg_sar_touch_start_wait_lsb = 15
        self.__reg_sar_touch_start_wait_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_min_time_ck12m_off(self):
        return self.__MEM.rdm(self.__addr, self.__reg_min_time_ck12m_off_msb, self.__reg_min_time_ck12m_off_lsb)
    @reg_min_time_ck12m_off.setter
    def reg_min_time_ck12m_off(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_min_time_ck12m_off_msb, self.__reg_min_time_ck12m_off_lsb, value)

    @property
    def reg_sar_touch_start_wait(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar_touch_start_wait_msb, self.__reg_sar_touch_start_wait_lsb)
    @reg_sar_touch_start_wait.setter
    def reg_sar_touch_start_wait(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar_touch_start_wait_msb, self.__reg_sar_touch_start_wait_lsb, value)
class RTC_TIMER3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x24
        self.__reg_rom_ram_powerup_timer_lsb = 25
        self.__reg_rom_ram_powerup_timer_msb = 31
        self.__reg_rom_ram_wait_timer_lsb = 16
        self.__reg_rom_ram_wait_timer_msb = 24
        self.__reg_wifi_powerup_timer_lsb = 9
        self.__reg_wifi_powerup_timer_msb = 15
        self.__reg_wifi_wait_timer_lsb = 0
        self.__reg_wifi_wait_timer_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rom_ram_powerup_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rom_ram_powerup_timer_msb, self.__reg_rom_ram_powerup_timer_lsb)
    @reg_rom_ram_powerup_timer.setter
    def reg_rom_ram_powerup_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rom_ram_powerup_timer_msb, self.__reg_rom_ram_powerup_timer_lsb, value)

    @property
    def reg_rom_ram_wait_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rom_ram_wait_timer_msb, self.__reg_rom_ram_wait_timer_lsb)
    @reg_rom_ram_wait_timer.setter
    def reg_rom_ram_wait_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rom_ram_wait_timer_msb, self.__reg_rom_ram_wait_timer_lsb, value)

    @property
    def reg_wifi_powerup_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wifi_powerup_timer_msb, self.__reg_wifi_powerup_timer_lsb)
    @reg_wifi_powerup_timer.setter
    def reg_wifi_powerup_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wifi_powerup_timer_msb, self.__reg_wifi_powerup_timer_lsb, value)

    @property
    def reg_wifi_wait_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wifi_wait_timer_msb, self.__reg_wifi_wait_timer_lsb)
    @reg_wifi_wait_timer.setter
    def reg_wifi_wait_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wifi_wait_timer_msb, self.__reg_wifi_wait_timer_lsb, value)
class RTC_TIMER4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x28
        self.__reg_dg_wrap_powerup_timer_lsb = 25
        self.__reg_dg_wrap_powerup_timer_msb = 31
        self.__reg_dg_wrap_wait_timer_lsb = 16
        self.__reg_dg_wrap_wait_timer_msb = 24
        self.__reg_rtc_powerup_timer_lsb = 9
        self.__reg_rtc_powerup_timer_msb = 15
        self.__reg_rtc_wait_timer_lsb = 0
        self.__reg_rtc_wait_timer_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_dg_wrap_powerup_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dg_wrap_powerup_timer_msb, self.__reg_dg_wrap_powerup_timer_lsb)
    @reg_dg_wrap_powerup_timer.setter
    def reg_dg_wrap_powerup_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dg_wrap_powerup_timer_msb, self.__reg_dg_wrap_powerup_timer_lsb, value)

    @property
    def reg_dg_wrap_wait_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dg_wrap_wait_timer_msb, self.__reg_dg_wrap_wait_timer_lsb)
    @reg_dg_wrap_wait_timer.setter
    def reg_dg_wrap_wait_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dg_wrap_wait_timer_msb, self.__reg_dg_wrap_wait_timer_lsb, value)

    @property
    def reg_rtc_powerup_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_powerup_timer_msb, self.__reg_rtc_powerup_timer_lsb)
    @reg_rtc_powerup_timer.setter
    def reg_rtc_powerup_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_powerup_timer_msb, self.__reg_rtc_powerup_timer_lsb, value)

    @property
    def reg_rtc_wait_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_wait_timer_msb, self.__reg_rtc_wait_timer_lsb)
    @reg_rtc_wait_timer.setter
    def reg_rtc_wait_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_wait_timer_msb, self.__reg_rtc_wait_timer_lsb, value)
class RTC_TIMER5(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x2c
        self.__reg_rtcmem_powerup_timer_lsb = 25
        self.__reg_rtcmem_powerup_timer_msb = 31
        self.__reg_rtcmem_wait_timer_lsb = 16
        self.__reg_rtcmem_wait_timer_msb = 24
        self.__reg_min_slp_val_lsb = 8
        self.__reg_min_slp_val_msb = 15
        self.__reg_sar_subtimer_prediv_lsb = 0
        self.__reg_sar_subtimer_prediv_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rtcmem_powerup_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtcmem_powerup_timer_msb, self.__reg_rtcmem_powerup_timer_lsb)
    @reg_rtcmem_powerup_timer.setter
    def reg_rtcmem_powerup_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtcmem_powerup_timer_msb, self.__reg_rtcmem_powerup_timer_lsb, value)

    @property
    def reg_rtcmem_wait_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtcmem_wait_timer_msb, self.__reg_rtcmem_wait_timer_lsb)
    @reg_rtcmem_wait_timer.setter
    def reg_rtcmem_wait_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtcmem_wait_timer_msb, self.__reg_rtcmem_wait_timer_lsb, value)

    @property
    def reg_min_slp_val(self):
        return self.__MEM.rdm(self.__addr, self.__reg_min_slp_val_msb, self.__reg_min_slp_val_lsb)
    @reg_min_slp_val.setter
    def reg_min_slp_val(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_min_slp_val_msb, self.__reg_min_slp_val_lsb, value)

    @property
    def reg_sar_subtimer_prediv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar_subtimer_prediv_msb, self.__reg_sar_subtimer_prediv_lsb)
    @reg_sar_subtimer_prediv.setter
    def reg_sar_subtimer_prediv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar_subtimer_prediv_msb, self.__reg_sar_subtimer_prediv_lsb, value)
class RTC_ANA_CONF(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x30
        self.__reg_pll_i2c_pu_lsb = 31
        self.__reg_pll_i2c_pu_msb = 31
        self.__reg_ckgen_i2c_pu_lsb = 30
        self.__reg_ckgen_i2c_pu_msb = 30
        self.__reg_rfrx_pbus_pu_lsb = 28
        self.__reg_rfrx_pbus_pu_msb = 28
        self.__reg_txrf_i2c_pu_lsb = 27
        self.__reg_txrf_i2c_pu_msb = 27
        self.__reg_pvtmon_pu_lsb = 26
        self.__reg_pvtmon_pu_msb = 26
        self.__reg_bbpll_cal_slp_start_lsb = 25
        self.__reg_bbpll_cal_slp_start_msb = 25
        self.__reg_plla_force_pu_lsb = 24
        self.__reg_plla_force_pu_msb = 24
        self.__reg_plla_force_pd_lsb = 23
        self.__reg_plla_force_pd_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_pll_i2c_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pll_i2c_pu_msb, self.__reg_pll_i2c_pu_lsb)
    @reg_pll_i2c_pu.setter
    def reg_pll_i2c_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pll_i2c_pu_msb, self.__reg_pll_i2c_pu_lsb, value)

    @property
    def reg_ckgen_i2c_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ckgen_i2c_pu_msb, self.__reg_ckgen_i2c_pu_lsb)
    @reg_ckgen_i2c_pu.setter
    def reg_ckgen_i2c_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ckgen_i2c_pu_msb, self.__reg_ckgen_i2c_pu_lsb, value)

    @property
    def reg_rfrx_pbus_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rfrx_pbus_pu_msb, self.__reg_rfrx_pbus_pu_lsb)
    @reg_rfrx_pbus_pu.setter
    def reg_rfrx_pbus_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rfrx_pbus_pu_msb, self.__reg_rfrx_pbus_pu_lsb, value)

    @property
    def reg_txrf_i2c_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrf_i2c_pu_msb, self.__reg_txrf_i2c_pu_lsb)
    @reg_txrf_i2c_pu.setter
    def reg_txrf_i2c_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrf_i2c_pu_msb, self.__reg_txrf_i2c_pu_lsb, value)

    @property
    def reg_pvtmon_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pvtmon_pu_msb, self.__reg_pvtmon_pu_lsb)
    @reg_pvtmon_pu.setter
    def reg_pvtmon_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pvtmon_pu_msb, self.__reg_pvtmon_pu_lsb, value)

    @property
    def reg_bbpll_cal_slp_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbpll_cal_slp_start_msb, self.__reg_bbpll_cal_slp_start_lsb)
    @reg_bbpll_cal_slp_start.setter
    def reg_bbpll_cal_slp_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbpll_cal_slp_start_msb, self.__reg_bbpll_cal_slp_start_lsb, value)

    @property
    def reg_plla_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_plla_force_pu_msb, self.__reg_plla_force_pu_lsb)
    @reg_plla_force_pu.setter
    def reg_plla_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_plla_force_pu_msb, self.__reg_plla_force_pu_lsb, value)

    @property
    def reg_plla_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_plla_force_pd_msb, self.__reg_plla_force_pd_lsb)
    @reg_plla_force_pd.setter
    def reg_plla_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_plla_force_pd_msb, self.__reg_plla_force_pd_lsb, value)
class RTC_RESET_STATE(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x34
        self.__procpu_stat_vector_sel_lsb = 13
        self.__procpu_stat_vector_sel_msb = 13
        self.__appcpu_stat_vector_sel_lsb = 12
        self.__appcpu_stat_vector_sel_msb = 12
        self.__reset_cause_appcpu_lsb = 6
        self.__reset_cause_appcpu_msb = 11
        self.__reset_cause_procpu_lsb = 0
        self.__reset_cause_procpu_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def procpu_stat_vector_sel(self):
        return self.__MEM.rdm(self.__addr, self.__procpu_stat_vector_sel_msb, self.__procpu_stat_vector_sel_lsb)
    @procpu_stat_vector_sel.setter
    def procpu_stat_vector_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__procpu_stat_vector_sel_msb, self.__procpu_stat_vector_sel_lsb, value)

    @property
    def appcpu_stat_vector_sel(self):
        return self.__MEM.rdm(self.__addr, self.__appcpu_stat_vector_sel_msb, self.__appcpu_stat_vector_sel_lsb)
    @appcpu_stat_vector_sel.setter
    def appcpu_stat_vector_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__appcpu_stat_vector_sel_msb, self.__appcpu_stat_vector_sel_lsb, value)

    @property
    def reset_cause_appcpu(self):
        return self.__MEM.rdm(self.__addr, self.__reset_cause_appcpu_msb, self.__reset_cause_appcpu_lsb)
    @reset_cause_appcpu.setter
    def reset_cause_appcpu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reset_cause_appcpu_msb, self.__reset_cause_appcpu_lsb, value)

    @property
    def reset_cause_procpu(self):
        return self.__MEM.rdm(self.__addr, self.__reset_cause_procpu_msb, self.__reset_cause_procpu_lsb)
    @reset_cause_procpu.setter
    def reset_cause_procpu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reset_cause_procpu_msb, self.__reset_cause_procpu_lsb, value)
class RTC_WAKEUP_STATE(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x38
        self.__reg_gpio_wakeup_filter_lsb = 22
        self.__reg_gpio_wakeup_filter_msb = 22
        self.__reg_rtc_wakeup_ena_lsb = 11
        self.__reg_rtc_wakeup_ena_msb = 21
        self.__wakeup_cause_lsb = 0
        self.__wakeup_cause_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_gpio_wakeup_filter(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gpio_wakeup_filter_msb, self.__reg_gpio_wakeup_filter_lsb)
    @reg_gpio_wakeup_filter.setter
    def reg_gpio_wakeup_filter(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gpio_wakeup_filter_msb, self.__reg_gpio_wakeup_filter_lsb, value)

    @property
    def reg_rtc_wakeup_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_wakeup_ena_msb, self.__reg_rtc_wakeup_ena_lsb)
    @reg_rtc_wakeup_ena.setter
    def reg_rtc_wakeup_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_wakeup_ena_msb, self.__reg_rtc_wakeup_ena_lsb, value)

    @property
    def wakeup_cause(self):
        return self.__MEM.rdm(self.__addr, self.__wakeup_cause_msb, self.__wakeup_cause_lsb)
    @wakeup_cause.setter
    def wakeup_cause(self, value):
        return self.__MEM.wrm(self.__addr, self.__wakeup_cause_msb, self.__wakeup_cause_lsb, value)
class INT_ENA_RTC(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x3c
        self.__rtc_main_timer_int_ena_lsb = 8
        self.__rtc_main_timer_int_ena_msb = 8
        self.__rtc_brown_out_int_ena_lsb = 7
        self.__rtc_brown_out_int_ena_msb = 7
        self.__rtc_touch_int_ena_lsb = 6
        self.__rtc_touch_int_ena_msb = 6
        self.__rtc_sar_int_ena_lsb = 5
        self.__rtc_sar_int_ena_msb = 5
        self.__rtc_time_valid_int_ena_lsb = 4
        self.__rtc_time_valid_int_ena_msb = 4
        self.__rtc_wdt_int_ena_lsb = 3
        self.__rtc_wdt_int_ena_msb = 3
        self.__sdio_idle_int_ena_lsb = 2
        self.__sdio_idle_int_ena_msb = 2
        self.__slp_reject_int_ena_lsb = 1
        self.__slp_reject_int_ena_msb = 1
        self.__slp_wakeup_int_ena_lsb = 0
        self.__slp_wakeup_int_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_main_timer_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_main_timer_int_ena_msb, self.__rtc_main_timer_int_ena_lsb)
    @rtc_main_timer_int_ena.setter
    def rtc_main_timer_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_main_timer_int_ena_msb, self.__rtc_main_timer_int_ena_lsb, value)

    @property
    def rtc_brown_out_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_brown_out_int_ena_msb, self.__rtc_brown_out_int_ena_lsb)
    @rtc_brown_out_int_ena.setter
    def rtc_brown_out_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_brown_out_int_ena_msb, self.__rtc_brown_out_int_ena_lsb, value)

    @property
    def rtc_touch_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_touch_int_ena_msb, self.__rtc_touch_int_ena_lsb)
    @rtc_touch_int_ena.setter
    def rtc_touch_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_touch_int_ena_msb, self.__rtc_touch_int_ena_lsb, value)

    @property
    def rtc_sar_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_sar_int_ena_msb, self.__rtc_sar_int_ena_lsb)
    @rtc_sar_int_ena.setter
    def rtc_sar_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_sar_int_ena_msb, self.__rtc_sar_int_ena_lsb, value)

    @property
    def rtc_time_valid_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_time_valid_int_ena_msb, self.__rtc_time_valid_int_ena_lsb)
    @rtc_time_valid_int_ena.setter
    def rtc_time_valid_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_time_valid_int_ena_msb, self.__rtc_time_valid_int_ena_lsb, value)

    @property
    def rtc_wdt_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_wdt_int_ena_msb, self.__rtc_wdt_int_ena_lsb)
    @rtc_wdt_int_ena.setter
    def rtc_wdt_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_wdt_int_ena_msb, self.__rtc_wdt_int_ena_lsb, value)

    @property
    def sdio_idle_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__sdio_idle_int_ena_msb, self.__sdio_idle_int_ena_lsb)
    @sdio_idle_int_ena.setter
    def sdio_idle_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__sdio_idle_int_ena_msb, self.__sdio_idle_int_ena_lsb, value)

    @property
    def slp_reject_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__slp_reject_int_ena_msb, self.__slp_reject_int_ena_lsb)
    @slp_reject_int_ena.setter
    def slp_reject_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__slp_reject_int_ena_msb, self.__slp_reject_int_ena_lsb, value)

    @property
    def slp_wakeup_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__slp_wakeup_int_ena_msb, self.__slp_wakeup_int_ena_lsb)
    @slp_wakeup_int_ena.setter
    def slp_wakeup_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__slp_wakeup_int_ena_msb, self.__slp_wakeup_int_ena_lsb, value)
class INT_RAW_RTC(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x40
        self.__rtc_main_timer_int_raw_lsb = 8
        self.__rtc_main_timer_int_raw_msb = 8
        self.__rtc_brown_out_int_raw_lsb = 7
        self.__rtc_brown_out_int_raw_msb = 7
        self.__rtc_touch_int_raw_lsb = 6
        self.__rtc_touch_int_raw_msb = 6
        self.__rtc_sar_int_raw_lsb = 5
        self.__rtc_sar_int_raw_msb = 5
        self.__rtc_time_valid_int_raw_lsb = 4
        self.__rtc_time_valid_int_raw_msb = 4
        self.__rtc_wdt_int_raw_lsb = 3
        self.__rtc_wdt_int_raw_msb = 3
        self.__sdio_idle_int_raw_lsb = 2
        self.__sdio_idle_int_raw_msb = 2
        self.__slp_reject_int_raw_lsb = 1
        self.__slp_reject_int_raw_msb = 1
        self.__slp_wakeup_int_raw_lsb = 0
        self.__slp_wakeup_int_raw_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_main_timer_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_main_timer_int_raw_msb, self.__rtc_main_timer_int_raw_lsb)
    @rtc_main_timer_int_raw.setter
    def rtc_main_timer_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_main_timer_int_raw_msb, self.__rtc_main_timer_int_raw_lsb, value)

    @property
    def rtc_brown_out_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_brown_out_int_raw_msb, self.__rtc_brown_out_int_raw_lsb)
    @rtc_brown_out_int_raw.setter
    def rtc_brown_out_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_brown_out_int_raw_msb, self.__rtc_brown_out_int_raw_lsb, value)

    @property
    def rtc_touch_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_touch_int_raw_msb, self.__rtc_touch_int_raw_lsb)
    @rtc_touch_int_raw.setter
    def rtc_touch_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_touch_int_raw_msb, self.__rtc_touch_int_raw_lsb, value)

    @property
    def rtc_sar_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_sar_int_raw_msb, self.__rtc_sar_int_raw_lsb)
    @rtc_sar_int_raw.setter
    def rtc_sar_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_sar_int_raw_msb, self.__rtc_sar_int_raw_lsb, value)

    @property
    def rtc_time_valid_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_time_valid_int_raw_msb, self.__rtc_time_valid_int_raw_lsb)
    @rtc_time_valid_int_raw.setter
    def rtc_time_valid_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_time_valid_int_raw_msb, self.__rtc_time_valid_int_raw_lsb, value)

    @property
    def rtc_wdt_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_wdt_int_raw_msb, self.__rtc_wdt_int_raw_lsb)
    @rtc_wdt_int_raw.setter
    def rtc_wdt_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_wdt_int_raw_msb, self.__rtc_wdt_int_raw_lsb, value)

    @property
    def sdio_idle_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__sdio_idle_int_raw_msb, self.__sdio_idle_int_raw_lsb)
    @sdio_idle_int_raw.setter
    def sdio_idle_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__sdio_idle_int_raw_msb, self.__sdio_idle_int_raw_lsb, value)

    @property
    def slp_reject_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__slp_reject_int_raw_msb, self.__slp_reject_int_raw_lsb)
    @slp_reject_int_raw.setter
    def slp_reject_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__slp_reject_int_raw_msb, self.__slp_reject_int_raw_lsb, value)

    @property
    def slp_wakeup_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__slp_wakeup_int_raw_msb, self.__slp_wakeup_int_raw_lsb)
    @slp_wakeup_int_raw.setter
    def slp_wakeup_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__slp_wakeup_int_raw_msb, self.__slp_wakeup_int_raw_lsb, value)
class INT_ST_RTC(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x44
        self.__rtc_main_timer_int_st_lsb = 8
        self.__rtc_main_timer_int_st_msb = 8
        self.__rtc_brown_out_int_st_lsb = 7
        self.__rtc_brown_out_int_st_msb = 7
        self.__rtc_touch_int_st_lsb = 6
        self.__rtc_touch_int_st_msb = 6
        self.__rtc_sar_int_st_lsb = 5
        self.__rtc_sar_int_st_msb = 5
        self.__rtc_time_valid_int_st_lsb = 4
        self.__rtc_time_valid_int_st_msb = 4
        self.__rtc_wdt_int_st_lsb = 3
        self.__rtc_wdt_int_st_msb = 3
        self.__sdio_idle_int_st_lsb = 2
        self.__sdio_idle_int_st_msb = 2
        self.__slp_reject_int_st_lsb = 1
        self.__slp_reject_int_st_msb = 1
        self.__slp_wakeup_int_st_lsb = 0
        self.__slp_wakeup_int_st_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_main_timer_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_main_timer_int_st_msb, self.__rtc_main_timer_int_st_lsb)
    @rtc_main_timer_int_st.setter
    def rtc_main_timer_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_main_timer_int_st_msb, self.__rtc_main_timer_int_st_lsb, value)

    @property
    def rtc_brown_out_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_brown_out_int_st_msb, self.__rtc_brown_out_int_st_lsb)
    @rtc_brown_out_int_st.setter
    def rtc_brown_out_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_brown_out_int_st_msb, self.__rtc_brown_out_int_st_lsb, value)

    @property
    def rtc_touch_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_touch_int_st_msb, self.__rtc_touch_int_st_lsb)
    @rtc_touch_int_st.setter
    def rtc_touch_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_touch_int_st_msb, self.__rtc_touch_int_st_lsb, value)

    @property
    def rtc_sar_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_sar_int_st_msb, self.__rtc_sar_int_st_lsb)
    @rtc_sar_int_st.setter
    def rtc_sar_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_sar_int_st_msb, self.__rtc_sar_int_st_lsb, value)

    @property
    def rtc_time_valid_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_time_valid_int_st_msb, self.__rtc_time_valid_int_st_lsb)
    @rtc_time_valid_int_st.setter
    def rtc_time_valid_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_time_valid_int_st_msb, self.__rtc_time_valid_int_st_lsb, value)

    @property
    def rtc_wdt_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_wdt_int_st_msb, self.__rtc_wdt_int_st_lsb)
    @rtc_wdt_int_st.setter
    def rtc_wdt_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_wdt_int_st_msb, self.__rtc_wdt_int_st_lsb, value)

    @property
    def sdio_idle_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__sdio_idle_int_st_msb, self.__sdio_idle_int_st_lsb)
    @sdio_idle_int_st.setter
    def sdio_idle_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__sdio_idle_int_st_msb, self.__sdio_idle_int_st_lsb, value)

    @property
    def slp_reject_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__slp_reject_int_st_msb, self.__slp_reject_int_st_lsb)
    @slp_reject_int_st.setter
    def slp_reject_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__slp_reject_int_st_msb, self.__slp_reject_int_st_lsb, value)

    @property
    def slp_wakeup_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__slp_wakeup_int_st_msb, self.__slp_wakeup_int_st_lsb)
    @slp_wakeup_int_st.setter
    def slp_wakeup_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__slp_wakeup_int_st_msb, self.__slp_wakeup_int_st_lsb, value)
class INT_CLR_RTC(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x48
        self.__rtc_main_timer_int_clr_lsb = 8
        self.__rtc_main_timer_int_clr_msb = 8
        self.__rtc_brown_out_int_clr_lsb = 7
        self.__rtc_brown_out_int_clr_msb = 7
        self.__rtc_touch_int_clr_lsb = 6
        self.__rtc_touch_int_clr_msb = 6
        self.__rtc_sar_int_clr_lsb = 5
        self.__rtc_sar_int_clr_msb = 5
        self.__rtc_time_valid_int_clr_lsb = 4
        self.__rtc_time_valid_int_clr_msb = 4
        self.__rtc_wdt_int_clr_lsb = 3
        self.__rtc_wdt_int_clr_msb = 3
        self.__sdio_idle_int_clr_lsb = 2
        self.__sdio_idle_int_clr_msb = 2
        self.__slp_reject_int_clr_lsb = 1
        self.__slp_reject_int_clr_msb = 1
        self.__slp_wakeup_int_clr_lsb = 0
        self.__slp_wakeup_int_clr_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_main_timer_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_main_timer_int_clr_msb, self.__rtc_main_timer_int_clr_lsb)
    @rtc_main_timer_int_clr.setter
    def rtc_main_timer_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_main_timer_int_clr_msb, self.__rtc_main_timer_int_clr_lsb, value)

    @property
    def rtc_brown_out_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_brown_out_int_clr_msb, self.__rtc_brown_out_int_clr_lsb)
    @rtc_brown_out_int_clr.setter
    def rtc_brown_out_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_brown_out_int_clr_msb, self.__rtc_brown_out_int_clr_lsb, value)

    @property
    def rtc_touch_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_touch_int_clr_msb, self.__rtc_touch_int_clr_lsb)
    @rtc_touch_int_clr.setter
    def rtc_touch_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_touch_int_clr_msb, self.__rtc_touch_int_clr_lsb, value)

    @property
    def rtc_sar_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_sar_int_clr_msb, self.__rtc_sar_int_clr_lsb)
    @rtc_sar_int_clr.setter
    def rtc_sar_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_sar_int_clr_msb, self.__rtc_sar_int_clr_lsb, value)

    @property
    def rtc_time_valid_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_time_valid_int_clr_msb, self.__rtc_time_valid_int_clr_lsb)
    @rtc_time_valid_int_clr.setter
    def rtc_time_valid_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_time_valid_int_clr_msb, self.__rtc_time_valid_int_clr_lsb, value)

    @property
    def rtc_wdt_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_wdt_int_clr_msb, self.__rtc_wdt_int_clr_lsb)
    @rtc_wdt_int_clr.setter
    def rtc_wdt_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_wdt_int_clr_msb, self.__rtc_wdt_int_clr_lsb, value)

    @property
    def sdio_idle_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__sdio_idle_int_clr_msb, self.__sdio_idle_int_clr_lsb)
    @sdio_idle_int_clr.setter
    def sdio_idle_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__sdio_idle_int_clr_msb, self.__sdio_idle_int_clr_lsb, value)

    @property
    def slp_reject_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__slp_reject_int_clr_msb, self.__slp_reject_int_clr_lsb)
    @slp_reject_int_clr.setter
    def slp_reject_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__slp_reject_int_clr_msb, self.__slp_reject_int_clr_lsb, value)

    @property
    def slp_wakeup_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__slp_wakeup_int_clr_msb, self.__slp_wakeup_int_clr_lsb)
    @slp_wakeup_int_clr.setter
    def slp_wakeup_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__slp_wakeup_int_clr_msb, self.__slp_wakeup_int_clr_lsb, value)
class RTC_STORE0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x4c
        self.__rtc_scratch0_lsb = 0
        self.__rtc_scratch0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_scratch0(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_scratch0_msb, self.__rtc_scratch0_lsb)
    @rtc_scratch0.setter
    def rtc_scratch0(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_scratch0_msb, self.__rtc_scratch0_lsb, value)
class RTC_STORE1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x50
        self.__rtc_scratch1_lsb = 0
        self.__rtc_scratch1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_scratch1(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_scratch1_msb, self.__rtc_scratch1_lsb)
    @rtc_scratch1.setter
    def rtc_scratch1(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_scratch1_msb, self.__rtc_scratch1_lsb, value)
class RTC_STORE2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x54
        self.__rtc_scratch2_lsb = 0
        self.__rtc_scratch2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_scratch2(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_scratch2_msb, self.__rtc_scratch2_lsb)
    @rtc_scratch2.setter
    def rtc_scratch2(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_scratch2_msb, self.__rtc_scratch2_lsb, value)
class RTC_STORE3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x58
        self.__rtc_scratch3_lsb = 0
        self.__rtc_scratch3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_scratch3(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_scratch3_msb, self.__rtc_scratch3_lsb)
    @rtc_scratch3.setter
    def rtc_scratch3(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_scratch3_msb, self.__rtc_scratch3_lsb, value)
class RTC_EXT_XTL_CONF(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x5c
        self.__reg_xtl_ext_ctr_en_lsb = 31
        self.__reg_xtl_ext_ctr_en_msb = 31
        self.__reg_xtl_ext_ctr_lv_lsb = 30
        self.__reg_xtl_ext_ctr_lv_msb = 30
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_xtl_ext_ctr_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xtl_ext_ctr_en_msb, self.__reg_xtl_ext_ctr_en_lsb)
    @reg_xtl_ext_ctr_en.setter
    def reg_xtl_ext_ctr_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xtl_ext_ctr_en_msb, self.__reg_xtl_ext_ctr_en_lsb, value)

    @property
    def reg_xtl_ext_ctr_lv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xtl_ext_ctr_lv_msb, self.__reg_xtl_ext_ctr_lv_lsb)
    @reg_xtl_ext_ctr_lv.setter
    def reg_xtl_ext_ctr_lv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xtl_ext_ctr_lv_msb, self.__reg_xtl_ext_ctr_lv_lsb, value)
class RTC_EXT_WAKEUP_CONF(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x60
        self.__reg_ext_wakeup1_lv_lsb = 31
        self.__reg_ext_wakeup1_lv_msb = 31
        self.__reg_ext_wakeup0_lv_lsb = 30
        self.__reg_ext_wakeup0_lv_msb = 30
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ext_wakeup1_lv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ext_wakeup1_lv_msb, self.__reg_ext_wakeup1_lv_lsb)
    @reg_ext_wakeup1_lv.setter
    def reg_ext_wakeup1_lv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ext_wakeup1_lv_msb, self.__reg_ext_wakeup1_lv_lsb, value)

    @property
    def reg_ext_wakeup0_lv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ext_wakeup0_lv_msb, self.__reg_ext_wakeup0_lv_lsb)
    @reg_ext_wakeup0_lv.setter
    def reg_ext_wakeup0_lv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ext_wakeup0_lv_msb, self.__reg_ext_wakeup0_lv_lsb, value)
class RTC_SLP_REJECT_CONF(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x64
        self.__reject_cause_lsb = 28
        self.__reject_cause_msb = 31
        self.__reg_deep_slp_reject_en_lsb = 27
        self.__reg_deep_slp_reject_en_msb = 27
        self.__reg_light_slp_reject_en_lsb = 26
        self.__reg_light_slp_reject_en_msb = 26
        self.__reg_sdio_reject_en_lsb = 25
        self.__reg_sdio_reject_en_msb = 25
        self.__reg_gpio_reject_en_lsb = 24
        self.__reg_gpio_reject_en_msb = 24
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reject_cause(self):
        return self.__MEM.rdm(self.__addr, self.__reject_cause_msb, self.__reject_cause_lsb)
    @reject_cause.setter
    def reject_cause(self, value):
        return self.__MEM.wrm(self.__addr, self.__reject_cause_msb, self.__reject_cause_lsb, value)

    @property
    def reg_deep_slp_reject_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_deep_slp_reject_en_msb, self.__reg_deep_slp_reject_en_lsb)
    @reg_deep_slp_reject_en.setter
    def reg_deep_slp_reject_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_deep_slp_reject_en_msb, self.__reg_deep_slp_reject_en_lsb, value)

    @property
    def reg_light_slp_reject_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_light_slp_reject_en_msb, self.__reg_light_slp_reject_en_lsb)
    @reg_light_slp_reject_en.setter
    def reg_light_slp_reject_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_light_slp_reject_en_msb, self.__reg_light_slp_reject_en_lsb, value)

    @property
    def reg_sdio_reject_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sdio_reject_en_msb, self.__reg_sdio_reject_en_lsb)
    @reg_sdio_reject_en.setter
    def reg_sdio_reject_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sdio_reject_en_msb, self.__reg_sdio_reject_en_lsb, value)

    @property
    def reg_gpio_reject_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gpio_reject_en_msb, self.__reg_gpio_reject_en_lsb)
    @reg_gpio_reject_en.setter
    def reg_gpio_reject_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gpio_reject_en_msb, self.__reg_gpio_reject_en_lsb, value)
class RTC_CPU_PERIOD_CONF(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x68
        self.__reg_rtc_cpuperiod_sel_lsb = 30
        self.__reg_rtc_cpuperiod_sel_msb = 31
        self.__reg_rtc_cpusel_conf_lsb = 29
        self.__reg_rtc_cpusel_conf_msb = 29
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rtc_cpuperiod_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_cpuperiod_sel_msb, self.__reg_rtc_cpuperiod_sel_lsb)
    @reg_rtc_cpuperiod_sel.setter
    def reg_rtc_cpuperiod_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_cpuperiod_sel_msb, self.__reg_rtc_cpuperiod_sel_lsb, value)

    @property
    def reg_rtc_cpusel_conf(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_cpusel_conf_msb, self.__reg_rtc_cpusel_conf_lsb)
    @reg_rtc_cpusel_conf.setter
    def reg_rtc_cpusel_conf(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_cpusel_conf_msb, self.__reg_rtc_cpusel_conf_lsb, value)
class RTC_SDIO_ACT_CONF(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x6c
        self.__reg_sdio_act_dnum_lsb = 22
        self.__reg_sdio_act_dnum_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sdio_act_dnum(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sdio_act_dnum_msb, self.__reg_sdio_act_dnum_lsb)
    @reg_sdio_act_dnum.setter
    def reg_sdio_act_dnum(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sdio_act_dnum_msb, self.__reg_sdio_act_dnum_lsb, value)
class RTC_CLK_CONF(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x70
        self.__reg_ana_clk_rtc_sel_lsb = 30
        self.__reg_ana_clk_rtc_sel_msb = 31
        self.__reg_fast_clk_rtc_sel_lsb = 29
        self.__reg_fast_clk_rtc_sel_msb = 29
        self.__reg_soc_clk_sel_lsb = 27
        self.__reg_soc_clk_sel_msb = 28
        self.__reg_ck12m_force_pu_lsb = 26
        self.__reg_ck12m_force_pu_msb = 26
        self.__reg_ck12m_force_pd_lsb = 25
        self.__reg_ck12m_force_pd_msb = 25
        self.__reg_ck12m_dfreq_lsb = 17
        self.__reg_ck12m_dfreq_msb = 24
        self.__reg_ck12m_force_nogating_lsb = 16
        self.__reg_ck12m_force_nogating_msb = 16
        self.__reg_xtal_force_nogating_lsb = 15
        self.__reg_xtal_force_nogating_msb = 15
        self.__reg_ck12m_div_sel_lsb = 12
        self.__reg_ck12m_div_sel_msb = 14
        self.__reg_ck12m_dfreq_force_lsb = 11
        self.__reg_ck12m_dfreq_force_msb = 11
        self.__reg_dig_clk12m_en_lsb = 10
        self.__reg_dig_clk12m_en_msb = 10
        self.__reg_dig_clk12m_d256_en_lsb = 9
        self.__reg_dig_clk12m_d256_en_msb = 9
        self.__reg_dig_xtal32k_en_lsb = 8
        self.__reg_dig_xtal32k_en_msb = 8
        self.__reg_enb_ck12m_div_lsb = 7
        self.__reg_enb_ck12m_div_msb = 7
        self.__reg_enb_ck12m_lsb = 6
        self.__reg_enb_ck12m_msb = 6
        self.__reg_ck12m_div_lsb = 4
        self.__reg_ck12m_div_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ana_clk_rtc_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ana_clk_rtc_sel_msb, self.__reg_ana_clk_rtc_sel_lsb)
    @reg_ana_clk_rtc_sel.setter
    def reg_ana_clk_rtc_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ana_clk_rtc_sel_msb, self.__reg_ana_clk_rtc_sel_lsb, value)

    @property
    def reg_fast_clk_rtc_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fast_clk_rtc_sel_msb, self.__reg_fast_clk_rtc_sel_lsb)
    @reg_fast_clk_rtc_sel.setter
    def reg_fast_clk_rtc_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fast_clk_rtc_sel_msb, self.__reg_fast_clk_rtc_sel_lsb, value)

    @property
    def reg_soc_clk_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_soc_clk_sel_msb, self.__reg_soc_clk_sel_lsb)
    @reg_soc_clk_sel.setter
    def reg_soc_clk_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_soc_clk_sel_msb, self.__reg_soc_clk_sel_lsb, value)

    @property
    def reg_ck12m_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ck12m_force_pu_msb, self.__reg_ck12m_force_pu_lsb)
    @reg_ck12m_force_pu.setter
    def reg_ck12m_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ck12m_force_pu_msb, self.__reg_ck12m_force_pu_lsb, value)

    @property
    def reg_ck12m_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ck12m_force_pd_msb, self.__reg_ck12m_force_pd_lsb)
    @reg_ck12m_force_pd.setter
    def reg_ck12m_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ck12m_force_pd_msb, self.__reg_ck12m_force_pd_lsb, value)

    @property
    def reg_ck12m_dfreq(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ck12m_dfreq_msb, self.__reg_ck12m_dfreq_lsb)
    @reg_ck12m_dfreq.setter
    def reg_ck12m_dfreq(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ck12m_dfreq_msb, self.__reg_ck12m_dfreq_lsb, value)

    @property
    def reg_ck12m_force_nogating(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ck12m_force_nogating_msb, self.__reg_ck12m_force_nogating_lsb)
    @reg_ck12m_force_nogating.setter
    def reg_ck12m_force_nogating(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ck12m_force_nogating_msb, self.__reg_ck12m_force_nogating_lsb, value)

    @property
    def reg_xtal_force_nogating(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xtal_force_nogating_msb, self.__reg_xtal_force_nogating_lsb)
    @reg_xtal_force_nogating.setter
    def reg_xtal_force_nogating(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xtal_force_nogating_msb, self.__reg_xtal_force_nogating_lsb, value)

    @property
    def reg_ck12m_div_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ck12m_div_sel_msb, self.__reg_ck12m_div_sel_lsb)
    @reg_ck12m_div_sel.setter
    def reg_ck12m_div_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ck12m_div_sel_msb, self.__reg_ck12m_div_sel_lsb, value)

    @property
    def reg_ck12m_dfreq_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ck12m_dfreq_force_msb, self.__reg_ck12m_dfreq_force_lsb)
    @reg_ck12m_dfreq_force.setter
    def reg_ck12m_dfreq_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ck12m_dfreq_force_msb, self.__reg_ck12m_dfreq_force_lsb, value)

    @property
    def reg_dig_clk12m_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dig_clk12m_en_msb, self.__reg_dig_clk12m_en_lsb)
    @reg_dig_clk12m_en.setter
    def reg_dig_clk12m_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dig_clk12m_en_msb, self.__reg_dig_clk12m_en_lsb, value)

    @property
    def reg_dig_clk12m_d256_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dig_clk12m_d256_en_msb, self.__reg_dig_clk12m_d256_en_lsb)
    @reg_dig_clk12m_d256_en.setter
    def reg_dig_clk12m_d256_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dig_clk12m_d256_en_msb, self.__reg_dig_clk12m_d256_en_lsb, value)

    @property
    def reg_dig_xtal32k_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dig_xtal32k_en_msb, self.__reg_dig_xtal32k_en_lsb)
    @reg_dig_xtal32k_en.setter
    def reg_dig_xtal32k_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dig_xtal32k_en_msb, self.__reg_dig_xtal32k_en_lsb, value)

    @property
    def reg_enb_ck12m_div(self):
        return self.__MEM.rdm(self.__addr, self.__reg_enb_ck12m_div_msb, self.__reg_enb_ck12m_div_lsb)
    @reg_enb_ck12m_div.setter
    def reg_enb_ck12m_div(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_enb_ck12m_div_msb, self.__reg_enb_ck12m_div_lsb, value)

    @property
    def reg_enb_ck12m(self):
        return self.__MEM.rdm(self.__addr, self.__reg_enb_ck12m_msb, self.__reg_enb_ck12m_lsb)
    @reg_enb_ck12m.setter
    def reg_enb_ck12m(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_enb_ck12m_msb, self.__reg_enb_ck12m_lsb, value)

    @property
    def reg_ck12m_div(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ck12m_div_msb, self.__reg_ck12m_div_lsb)
    @reg_ck12m_div.setter
    def reg_ck12m_div(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ck12m_div_msb, self.__reg_ck12m_div_lsb, value)
class RTC_SDIO_CONF(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x74
        self.__reg_xpd_sdio_reg_lsb = 31
        self.__reg_xpd_sdio_reg_msb = 31
        self.__reg_drefh_sdio_lsb = 29
        self.__reg_drefh_sdio_msb = 30
        self.__reg_drefm_sdio_lsb = 27
        self.__reg_drefm_sdio_msb = 28
        self.__reg_drefl_sdio_lsb = 25
        self.__reg_drefl_sdio_msb = 26
        self.__reg1p8_ready_lsb = 24
        self.__reg1p8_ready_msb = 24
        self.__reg_sdio_tieh_lsb = 23
        self.__reg_sdio_tieh_msb = 23
        self.__reg_sdio_force_lsb = 22
        self.__reg_sdio_force_msb = 22
        self.__reg_sdio_reg_pd_en_lsb = 21
        self.__reg_sdio_reg_pd_en_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_xpd_sdio_reg(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xpd_sdio_reg_msb, self.__reg_xpd_sdio_reg_lsb)
    @reg_xpd_sdio_reg.setter
    def reg_xpd_sdio_reg(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xpd_sdio_reg_msb, self.__reg_xpd_sdio_reg_lsb, value)

    @property
    def reg_drefh_sdio(self):
        return self.__MEM.rdm(self.__addr, self.__reg_drefh_sdio_msb, self.__reg_drefh_sdio_lsb)
    @reg_drefh_sdio.setter
    def reg_drefh_sdio(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_drefh_sdio_msb, self.__reg_drefh_sdio_lsb, value)

    @property
    def reg_drefm_sdio(self):
        return self.__MEM.rdm(self.__addr, self.__reg_drefm_sdio_msb, self.__reg_drefm_sdio_lsb)
    @reg_drefm_sdio.setter
    def reg_drefm_sdio(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_drefm_sdio_msb, self.__reg_drefm_sdio_lsb, value)

    @property
    def reg_drefl_sdio(self):
        return self.__MEM.rdm(self.__addr, self.__reg_drefl_sdio_msb, self.__reg_drefl_sdio_lsb)
    @reg_drefl_sdio.setter
    def reg_drefl_sdio(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_drefl_sdio_msb, self.__reg_drefl_sdio_lsb, value)

    @property
    def reg1p8_ready(self):
        return self.__MEM.rdm(self.__addr, self.__reg1p8_ready_msb, self.__reg1p8_ready_lsb)
    @reg1p8_ready.setter
    def reg1p8_ready(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg1p8_ready_msb, self.__reg1p8_ready_lsb, value)

    @property
    def reg_sdio_tieh(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sdio_tieh_msb, self.__reg_sdio_tieh_lsb)
    @reg_sdio_tieh.setter
    def reg_sdio_tieh(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sdio_tieh_msb, self.__reg_sdio_tieh_lsb, value)

    @property
    def reg_sdio_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sdio_force_msb, self.__reg_sdio_force_lsb)
    @reg_sdio_force.setter
    def reg_sdio_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sdio_force_msb, self.__reg_sdio_force_lsb, value)

    @property
    def reg_sdio_reg_pd_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sdio_reg_pd_en_msb, self.__reg_sdio_reg_pd_en_lsb)
    @reg_sdio_reg_pd_en.setter
    def reg_sdio_reg_pd_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sdio_reg_pd_en_msb, self.__reg_sdio_reg_pd_en_lsb, value)
class RTC_BIAS_CONF(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x78
        self.__reg_rst_bias_i2c_lsb = 31
        self.__reg_rst_bias_i2c_msb = 31
        self.__reg_dec_heartbeat_width_lsb = 30
        self.__reg_dec_heartbeat_width_msb = 30
        self.__reg_inc_heartbeat_period_lsb = 29
        self.__reg_inc_heartbeat_period_msb = 29
        self.__reg_dec_heartbeat_period_lsb = 28
        self.__reg_dec_heartbeat_period_msb = 28
        self.__reg_inc_heartbeat_refresh_lsb = 27
        self.__reg_inc_heartbeat_refresh_msb = 27
        self.__reg_enb_sck_xtal_lsb = 26
        self.__reg_enb_sck_xtal_msb = 26
        self.__reg_dbg_atten_lsb = 24
        self.__reg_dbg_atten_msb = 25
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rst_bias_i2c(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rst_bias_i2c_msb, self.__reg_rst_bias_i2c_lsb)
    @reg_rst_bias_i2c.setter
    def reg_rst_bias_i2c(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rst_bias_i2c_msb, self.__reg_rst_bias_i2c_lsb, value)

    @property
    def reg_dec_heartbeat_width(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dec_heartbeat_width_msb, self.__reg_dec_heartbeat_width_lsb)
    @reg_dec_heartbeat_width.setter
    def reg_dec_heartbeat_width(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dec_heartbeat_width_msb, self.__reg_dec_heartbeat_width_lsb, value)

    @property
    def reg_inc_heartbeat_period(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inc_heartbeat_period_msb, self.__reg_inc_heartbeat_period_lsb)
    @reg_inc_heartbeat_period.setter
    def reg_inc_heartbeat_period(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inc_heartbeat_period_msb, self.__reg_inc_heartbeat_period_lsb, value)

    @property
    def reg_dec_heartbeat_period(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dec_heartbeat_period_msb, self.__reg_dec_heartbeat_period_lsb)
    @reg_dec_heartbeat_period.setter
    def reg_dec_heartbeat_period(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dec_heartbeat_period_msb, self.__reg_dec_heartbeat_period_lsb, value)

    @property
    def reg_inc_heartbeat_refresh(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inc_heartbeat_refresh_msb, self.__reg_inc_heartbeat_refresh_lsb)
    @reg_inc_heartbeat_refresh.setter
    def reg_inc_heartbeat_refresh(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inc_heartbeat_refresh_msb, self.__reg_inc_heartbeat_refresh_lsb, value)

    @property
    def reg_enb_sck_xtal(self):
        return self.__MEM.rdm(self.__addr, self.__reg_enb_sck_xtal_msb, self.__reg_enb_sck_xtal_lsb)
    @reg_enb_sck_xtal.setter
    def reg_enb_sck_xtal(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_enb_sck_xtal_msb, self.__reg_enb_sck_xtal_lsb, value)

    @property
    def reg_dbg_atten(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dbg_atten_msb, self.__reg_dbg_atten_lsb)
    @reg_dbg_atten.setter
    def reg_dbg_atten(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dbg_atten_msb, self.__reg_dbg_atten_lsb, value)
class RTC_REG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x7c
        self.__reg_rtc_reg_force_pu_lsb = 31
        self.__reg_rtc_reg_force_pu_msb = 31
        self.__reg_rtc_reg_force_pd_lsb = 30
        self.__reg_rtc_reg_force_pd_msb = 30
        self.__reg_rtc_dboost_force_pu_lsb = 29
        self.__reg_rtc_dboost_force_pu_msb = 29
        self.__reg_rtc_dboost_force_pd_lsb = 28
        self.__reg_rtc_dboost_force_pd_msb = 28
        self.__reg_rtc_dbias_wak_lsb = 25
        self.__reg_rtc_dbias_wak_msb = 27
        self.__reg_rtc_dbias_slp_lsb = 22
        self.__reg_rtc_dbias_slp_msb = 24
        self.__reg_sck_dcap_lsb = 14
        self.__reg_sck_dcap_msb = 21
        self.__reg_dig_reg_dbias_wak_lsb = 11
        self.__reg_dig_reg_dbias_wak_msb = 13
        self.__reg_dig_reg_dbias_slp_lsb = 8
        self.__reg_dig_reg_dbias_slp_msb = 10
        self.__reg_sck_dcap_force_lsb = 7
        self.__reg_sck_dcap_force_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rtc_reg_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_reg_force_pu_msb, self.__reg_rtc_reg_force_pu_lsb)
    @reg_rtc_reg_force_pu.setter
    def reg_rtc_reg_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_reg_force_pu_msb, self.__reg_rtc_reg_force_pu_lsb, value)

    @property
    def reg_rtc_reg_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_reg_force_pd_msb, self.__reg_rtc_reg_force_pd_lsb)
    @reg_rtc_reg_force_pd.setter
    def reg_rtc_reg_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_reg_force_pd_msb, self.__reg_rtc_reg_force_pd_lsb, value)

    @property
    def reg_rtc_dboost_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_dboost_force_pu_msb, self.__reg_rtc_dboost_force_pu_lsb)
    @reg_rtc_dboost_force_pu.setter
    def reg_rtc_dboost_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_dboost_force_pu_msb, self.__reg_rtc_dboost_force_pu_lsb, value)

    @property
    def reg_rtc_dboost_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_dboost_force_pd_msb, self.__reg_rtc_dboost_force_pd_lsb)
    @reg_rtc_dboost_force_pd.setter
    def reg_rtc_dboost_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_dboost_force_pd_msb, self.__reg_rtc_dboost_force_pd_lsb, value)

    @property
    def reg_rtc_dbias_wak(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_dbias_wak_msb, self.__reg_rtc_dbias_wak_lsb)
    @reg_rtc_dbias_wak.setter
    def reg_rtc_dbias_wak(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_dbias_wak_msb, self.__reg_rtc_dbias_wak_lsb, value)

    @property
    def reg_rtc_dbias_slp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_dbias_slp_msb, self.__reg_rtc_dbias_slp_lsb)
    @reg_rtc_dbias_slp.setter
    def reg_rtc_dbias_slp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_dbias_slp_msb, self.__reg_rtc_dbias_slp_lsb, value)

    @property
    def reg_sck_dcap(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sck_dcap_msb, self.__reg_sck_dcap_lsb)
    @reg_sck_dcap.setter
    def reg_sck_dcap(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sck_dcap_msb, self.__reg_sck_dcap_lsb, value)

    @property
    def reg_dig_reg_dbias_wak(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dig_reg_dbias_wak_msb, self.__reg_dig_reg_dbias_wak_lsb)
    @reg_dig_reg_dbias_wak.setter
    def reg_dig_reg_dbias_wak(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dig_reg_dbias_wak_msb, self.__reg_dig_reg_dbias_wak_lsb, value)

    @property
    def reg_dig_reg_dbias_slp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dig_reg_dbias_slp_msb, self.__reg_dig_reg_dbias_slp_lsb)
    @reg_dig_reg_dbias_slp.setter
    def reg_dig_reg_dbias_slp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dig_reg_dbias_slp_msb, self.__reg_dig_reg_dbias_slp_lsb, value)

    @property
    def reg_sck_dcap_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sck_dcap_force_msb, self.__reg_sck_dcap_force_lsb)
    @reg_sck_dcap_force.setter
    def reg_sck_dcap_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sck_dcap_force_msb, self.__reg_sck_dcap_force_lsb, value)
class RTC_PWC(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x80
        self.__reg_rtc_pd_en_lsb = 20
        self.__reg_rtc_pd_en_msb = 20
        self.__reg_rtc_force_pu_lsb = 19
        self.__reg_rtc_force_pu_msb = 19
        self.__reg_rtc_force_pd_lsb = 18
        self.__reg_rtc_force_pd_msb = 18
        self.__reg_rtc_slowmem_pd_en_lsb = 17
        self.__reg_rtc_slowmem_pd_en_msb = 17
        self.__reg_rtc_slowmem_force_pu_lsb = 16
        self.__reg_rtc_slowmem_force_pu_msb = 16
        self.__reg_rtc_slowmem_force_pd_lsb = 15
        self.__reg_rtc_slowmem_force_pd_msb = 15
        self.__reg_rtc_fastmem_pd_en_lsb = 14
        self.__reg_rtc_fastmem_pd_en_msb = 14
        self.__reg_rtc_fastmem_force_pu_lsb = 13
        self.__reg_rtc_fastmem_force_pu_msb = 13
        self.__reg_rtc_fastmem_force_pd_lsb = 12
        self.__reg_rtc_fastmem_force_pd_msb = 12
        self.__reg_rtc_slowmem_force_lpu_lsb = 11
        self.__reg_rtc_slowmem_force_lpu_msb = 11
        self.__reg_rtc_slowmem_force_lpd_lsb = 10
        self.__reg_rtc_slowmem_force_lpd_msb = 10
        self.__reg_rtc_slowmem_folw_cpu_lsb = 9
        self.__reg_rtc_slowmem_folw_cpu_msb = 9
        self.__reg_rtc_fastmem_force_lpu_lsb = 8
        self.__reg_rtc_fastmem_force_lpu_msb = 8
        self.__reg_rtc_fastmem_force_lpd_lsb = 7
        self.__reg_rtc_fastmem_force_lpd_msb = 7
        self.__reg_rtc_fastmem_folw_cpu_lsb = 6
        self.__reg_rtc_fastmem_folw_cpu_msb = 6
        self.__reg_rtc_force_noiso_lsb = 5
        self.__reg_rtc_force_noiso_msb = 5
        self.__reg_rtc_force_iso_lsb = 4
        self.__reg_rtc_force_iso_msb = 4
        self.__reg_rtc_slowmem_force_iso_lsb = 3
        self.__reg_rtc_slowmem_force_iso_msb = 3
        self.__reg_rtc_slowmem_force_noiso_lsb = 2
        self.__reg_rtc_slowmem_force_noiso_msb = 2
        self.__reg_rtc_fastmem_force_iso_lsb = 1
        self.__reg_rtc_fastmem_force_iso_msb = 1
        self.__reg_rtc_fastmem_force_noiso_lsb = 0
        self.__reg_rtc_fastmem_force_noiso_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rtc_pd_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_pd_en_msb, self.__reg_rtc_pd_en_lsb)
    @reg_rtc_pd_en.setter
    def reg_rtc_pd_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_pd_en_msb, self.__reg_rtc_pd_en_lsb, value)

    @property
    def reg_rtc_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_force_pu_msb, self.__reg_rtc_force_pu_lsb)
    @reg_rtc_force_pu.setter
    def reg_rtc_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_force_pu_msb, self.__reg_rtc_force_pu_lsb, value)

    @property
    def reg_rtc_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_force_pd_msb, self.__reg_rtc_force_pd_lsb)
    @reg_rtc_force_pd.setter
    def reg_rtc_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_force_pd_msb, self.__reg_rtc_force_pd_lsb, value)

    @property
    def reg_rtc_slowmem_pd_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_slowmem_pd_en_msb, self.__reg_rtc_slowmem_pd_en_lsb)
    @reg_rtc_slowmem_pd_en.setter
    def reg_rtc_slowmem_pd_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_slowmem_pd_en_msb, self.__reg_rtc_slowmem_pd_en_lsb, value)

    @property
    def reg_rtc_slowmem_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_slowmem_force_pu_msb, self.__reg_rtc_slowmem_force_pu_lsb)
    @reg_rtc_slowmem_force_pu.setter
    def reg_rtc_slowmem_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_slowmem_force_pu_msb, self.__reg_rtc_slowmem_force_pu_lsb, value)

    @property
    def reg_rtc_slowmem_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_slowmem_force_pd_msb, self.__reg_rtc_slowmem_force_pd_lsb)
    @reg_rtc_slowmem_force_pd.setter
    def reg_rtc_slowmem_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_slowmem_force_pd_msb, self.__reg_rtc_slowmem_force_pd_lsb, value)

    @property
    def reg_rtc_fastmem_pd_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_fastmem_pd_en_msb, self.__reg_rtc_fastmem_pd_en_lsb)
    @reg_rtc_fastmem_pd_en.setter
    def reg_rtc_fastmem_pd_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_fastmem_pd_en_msb, self.__reg_rtc_fastmem_pd_en_lsb, value)

    @property
    def reg_rtc_fastmem_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_fastmem_force_pu_msb, self.__reg_rtc_fastmem_force_pu_lsb)
    @reg_rtc_fastmem_force_pu.setter
    def reg_rtc_fastmem_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_fastmem_force_pu_msb, self.__reg_rtc_fastmem_force_pu_lsb, value)

    @property
    def reg_rtc_fastmem_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_fastmem_force_pd_msb, self.__reg_rtc_fastmem_force_pd_lsb)
    @reg_rtc_fastmem_force_pd.setter
    def reg_rtc_fastmem_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_fastmem_force_pd_msb, self.__reg_rtc_fastmem_force_pd_lsb, value)

    @property
    def reg_rtc_slowmem_force_lpu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_slowmem_force_lpu_msb, self.__reg_rtc_slowmem_force_lpu_lsb)
    @reg_rtc_slowmem_force_lpu.setter
    def reg_rtc_slowmem_force_lpu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_slowmem_force_lpu_msb, self.__reg_rtc_slowmem_force_lpu_lsb, value)

    @property
    def reg_rtc_slowmem_force_lpd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_slowmem_force_lpd_msb, self.__reg_rtc_slowmem_force_lpd_lsb)
    @reg_rtc_slowmem_force_lpd.setter
    def reg_rtc_slowmem_force_lpd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_slowmem_force_lpd_msb, self.__reg_rtc_slowmem_force_lpd_lsb, value)

    @property
    def reg_rtc_slowmem_folw_cpu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_slowmem_folw_cpu_msb, self.__reg_rtc_slowmem_folw_cpu_lsb)
    @reg_rtc_slowmem_folw_cpu.setter
    def reg_rtc_slowmem_folw_cpu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_slowmem_folw_cpu_msb, self.__reg_rtc_slowmem_folw_cpu_lsb, value)

    @property
    def reg_rtc_fastmem_force_lpu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_fastmem_force_lpu_msb, self.__reg_rtc_fastmem_force_lpu_lsb)
    @reg_rtc_fastmem_force_lpu.setter
    def reg_rtc_fastmem_force_lpu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_fastmem_force_lpu_msb, self.__reg_rtc_fastmem_force_lpu_lsb, value)

    @property
    def reg_rtc_fastmem_force_lpd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_fastmem_force_lpd_msb, self.__reg_rtc_fastmem_force_lpd_lsb)
    @reg_rtc_fastmem_force_lpd.setter
    def reg_rtc_fastmem_force_lpd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_fastmem_force_lpd_msb, self.__reg_rtc_fastmem_force_lpd_lsb, value)

    @property
    def reg_rtc_fastmem_folw_cpu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_fastmem_folw_cpu_msb, self.__reg_rtc_fastmem_folw_cpu_lsb)
    @reg_rtc_fastmem_folw_cpu.setter
    def reg_rtc_fastmem_folw_cpu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_fastmem_folw_cpu_msb, self.__reg_rtc_fastmem_folw_cpu_lsb, value)

    @property
    def reg_rtc_force_noiso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_force_noiso_msb, self.__reg_rtc_force_noiso_lsb)
    @reg_rtc_force_noiso.setter
    def reg_rtc_force_noiso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_force_noiso_msb, self.__reg_rtc_force_noiso_lsb, value)

    @property
    def reg_rtc_force_iso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_force_iso_msb, self.__reg_rtc_force_iso_lsb)
    @reg_rtc_force_iso.setter
    def reg_rtc_force_iso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_force_iso_msb, self.__reg_rtc_force_iso_lsb, value)

    @property
    def reg_rtc_slowmem_force_iso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_slowmem_force_iso_msb, self.__reg_rtc_slowmem_force_iso_lsb)
    @reg_rtc_slowmem_force_iso.setter
    def reg_rtc_slowmem_force_iso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_slowmem_force_iso_msb, self.__reg_rtc_slowmem_force_iso_lsb, value)

    @property
    def reg_rtc_slowmem_force_noiso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_slowmem_force_noiso_msb, self.__reg_rtc_slowmem_force_noiso_lsb)
    @reg_rtc_slowmem_force_noiso.setter
    def reg_rtc_slowmem_force_noiso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_slowmem_force_noiso_msb, self.__reg_rtc_slowmem_force_noiso_lsb, value)

    @property
    def reg_rtc_fastmem_force_iso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_fastmem_force_iso_msb, self.__reg_rtc_fastmem_force_iso_lsb)
    @reg_rtc_fastmem_force_iso.setter
    def reg_rtc_fastmem_force_iso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_fastmem_force_iso_msb, self.__reg_rtc_fastmem_force_iso_lsb, value)

    @property
    def reg_rtc_fastmem_force_noiso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_fastmem_force_noiso_msb, self.__reg_rtc_fastmem_force_noiso_lsb)
    @reg_rtc_fastmem_force_noiso.setter
    def reg_rtc_fastmem_force_noiso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_fastmem_force_noiso_msb, self.__reg_rtc_fastmem_force_noiso_lsb, value)
class DIG_PWC(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x84
        self.__reg_dg_wrap_pd_en_lsb = 31
        self.__reg_dg_wrap_pd_en_msb = 31
        self.__reg_wifi_pd_en_lsb = 30
        self.__reg_wifi_pd_en_msb = 30
        self.__reg_inter_ram4_pd_en_lsb = 29
        self.__reg_inter_ram4_pd_en_msb = 29
        self.__reg_inter_ram3_pd_en_lsb = 28
        self.__reg_inter_ram3_pd_en_msb = 28
        self.__reg_inter_ram2_pd_en_lsb = 27
        self.__reg_inter_ram2_pd_en_msb = 27
        self.__reg_inter_ram1_pd_en_lsb = 26
        self.__reg_inter_ram1_pd_en_msb = 26
        self.__reg_inter_ram0_pd_en_lsb = 25
        self.__reg_inter_ram0_pd_en_msb = 25
        self.__reg_rom0_pd_en_lsb = 24
        self.__reg_rom0_pd_en_msb = 24
        self.__reg_dg_wrap_force_pu_lsb = 20
        self.__reg_dg_wrap_force_pu_msb = 20
        self.__reg_dg_wrap_force_pd_lsb = 19
        self.__reg_dg_wrap_force_pd_msb = 19
        self.__reg_wifi_force_pu_lsb = 18
        self.__reg_wifi_force_pu_msb = 18
        self.__reg_wifi_force_pd_lsb = 17
        self.__reg_wifi_force_pd_msb = 17
        self.__reg_inter_ram4_force_pu_lsb = 16
        self.__reg_inter_ram4_force_pu_msb = 16
        self.__reg_inter_ram4_force_pd_lsb = 15
        self.__reg_inter_ram4_force_pd_msb = 15
        self.__reg_inter_ram3_force_pu_lsb = 14
        self.__reg_inter_ram3_force_pu_msb = 14
        self.__reg_inter_ram3_force_pd_lsb = 13
        self.__reg_inter_ram3_force_pd_msb = 13
        self.__reg_inter_ram2_force_pu_lsb = 12
        self.__reg_inter_ram2_force_pu_msb = 12
        self.__reg_inter_ram2_force_pd_lsb = 11
        self.__reg_inter_ram2_force_pd_msb = 11
        self.__reg_inter_ram1_force_pu_lsb = 10
        self.__reg_inter_ram1_force_pu_msb = 10
        self.__reg_inter_ram1_force_pd_lsb = 9
        self.__reg_inter_ram1_force_pd_msb = 9
        self.__reg_inter_ram0_force_pu_lsb = 8
        self.__reg_inter_ram0_force_pu_msb = 8
        self.__reg_inter_ram0_force_pd_lsb = 7
        self.__reg_inter_ram0_force_pd_msb = 7
        self.__reg_rom0_force_pu_lsb = 6
        self.__reg_rom0_force_pu_msb = 6
        self.__reg_rom0_force_pd_lsb = 5
        self.__reg_rom0_force_pd_msb = 5
        self.__reg_lslp_mem_force_pu_lsb = 4
        self.__reg_lslp_mem_force_pu_msb = 4
        self.__reg_lslp_mem_force_pd_lsb = 3
        self.__reg_lslp_mem_force_pd_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_dg_wrap_pd_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dg_wrap_pd_en_msb, self.__reg_dg_wrap_pd_en_lsb)
    @reg_dg_wrap_pd_en.setter
    def reg_dg_wrap_pd_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dg_wrap_pd_en_msb, self.__reg_dg_wrap_pd_en_lsb, value)

    @property
    def reg_wifi_pd_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wifi_pd_en_msb, self.__reg_wifi_pd_en_lsb)
    @reg_wifi_pd_en.setter
    def reg_wifi_pd_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wifi_pd_en_msb, self.__reg_wifi_pd_en_lsb, value)

    @property
    def reg_inter_ram4_pd_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inter_ram4_pd_en_msb, self.__reg_inter_ram4_pd_en_lsb)
    @reg_inter_ram4_pd_en.setter
    def reg_inter_ram4_pd_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inter_ram4_pd_en_msb, self.__reg_inter_ram4_pd_en_lsb, value)

    @property
    def reg_inter_ram3_pd_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inter_ram3_pd_en_msb, self.__reg_inter_ram3_pd_en_lsb)
    @reg_inter_ram3_pd_en.setter
    def reg_inter_ram3_pd_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inter_ram3_pd_en_msb, self.__reg_inter_ram3_pd_en_lsb, value)

    @property
    def reg_inter_ram2_pd_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inter_ram2_pd_en_msb, self.__reg_inter_ram2_pd_en_lsb)
    @reg_inter_ram2_pd_en.setter
    def reg_inter_ram2_pd_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inter_ram2_pd_en_msb, self.__reg_inter_ram2_pd_en_lsb, value)

    @property
    def reg_inter_ram1_pd_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inter_ram1_pd_en_msb, self.__reg_inter_ram1_pd_en_lsb)
    @reg_inter_ram1_pd_en.setter
    def reg_inter_ram1_pd_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inter_ram1_pd_en_msb, self.__reg_inter_ram1_pd_en_lsb, value)

    @property
    def reg_inter_ram0_pd_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inter_ram0_pd_en_msb, self.__reg_inter_ram0_pd_en_lsb)
    @reg_inter_ram0_pd_en.setter
    def reg_inter_ram0_pd_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inter_ram0_pd_en_msb, self.__reg_inter_ram0_pd_en_lsb, value)

    @property
    def reg_rom0_pd_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rom0_pd_en_msb, self.__reg_rom0_pd_en_lsb)
    @reg_rom0_pd_en.setter
    def reg_rom0_pd_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rom0_pd_en_msb, self.__reg_rom0_pd_en_lsb, value)

    @property
    def reg_dg_wrap_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dg_wrap_force_pu_msb, self.__reg_dg_wrap_force_pu_lsb)
    @reg_dg_wrap_force_pu.setter
    def reg_dg_wrap_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dg_wrap_force_pu_msb, self.__reg_dg_wrap_force_pu_lsb, value)

    @property
    def reg_dg_wrap_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dg_wrap_force_pd_msb, self.__reg_dg_wrap_force_pd_lsb)
    @reg_dg_wrap_force_pd.setter
    def reg_dg_wrap_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dg_wrap_force_pd_msb, self.__reg_dg_wrap_force_pd_lsb, value)

    @property
    def reg_wifi_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wifi_force_pu_msb, self.__reg_wifi_force_pu_lsb)
    @reg_wifi_force_pu.setter
    def reg_wifi_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wifi_force_pu_msb, self.__reg_wifi_force_pu_lsb, value)

    @property
    def reg_wifi_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wifi_force_pd_msb, self.__reg_wifi_force_pd_lsb)
    @reg_wifi_force_pd.setter
    def reg_wifi_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wifi_force_pd_msb, self.__reg_wifi_force_pd_lsb, value)

    @property
    def reg_inter_ram4_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inter_ram4_force_pu_msb, self.__reg_inter_ram4_force_pu_lsb)
    @reg_inter_ram4_force_pu.setter
    def reg_inter_ram4_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inter_ram4_force_pu_msb, self.__reg_inter_ram4_force_pu_lsb, value)

    @property
    def reg_inter_ram4_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inter_ram4_force_pd_msb, self.__reg_inter_ram4_force_pd_lsb)
    @reg_inter_ram4_force_pd.setter
    def reg_inter_ram4_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inter_ram4_force_pd_msb, self.__reg_inter_ram4_force_pd_lsb, value)

    @property
    def reg_inter_ram3_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inter_ram3_force_pu_msb, self.__reg_inter_ram3_force_pu_lsb)
    @reg_inter_ram3_force_pu.setter
    def reg_inter_ram3_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inter_ram3_force_pu_msb, self.__reg_inter_ram3_force_pu_lsb, value)

    @property
    def reg_inter_ram3_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inter_ram3_force_pd_msb, self.__reg_inter_ram3_force_pd_lsb)
    @reg_inter_ram3_force_pd.setter
    def reg_inter_ram3_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inter_ram3_force_pd_msb, self.__reg_inter_ram3_force_pd_lsb, value)

    @property
    def reg_inter_ram2_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inter_ram2_force_pu_msb, self.__reg_inter_ram2_force_pu_lsb)
    @reg_inter_ram2_force_pu.setter
    def reg_inter_ram2_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inter_ram2_force_pu_msb, self.__reg_inter_ram2_force_pu_lsb, value)

    @property
    def reg_inter_ram2_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inter_ram2_force_pd_msb, self.__reg_inter_ram2_force_pd_lsb)
    @reg_inter_ram2_force_pd.setter
    def reg_inter_ram2_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inter_ram2_force_pd_msb, self.__reg_inter_ram2_force_pd_lsb, value)

    @property
    def reg_inter_ram1_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inter_ram1_force_pu_msb, self.__reg_inter_ram1_force_pu_lsb)
    @reg_inter_ram1_force_pu.setter
    def reg_inter_ram1_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inter_ram1_force_pu_msb, self.__reg_inter_ram1_force_pu_lsb, value)

    @property
    def reg_inter_ram1_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inter_ram1_force_pd_msb, self.__reg_inter_ram1_force_pd_lsb)
    @reg_inter_ram1_force_pd.setter
    def reg_inter_ram1_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inter_ram1_force_pd_msb, self.__reg_inter_ram1_force_pd_lsb, value)

    @property
    def reg_inter_ram0_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inter_ram0_force_pu_msb, self.__reg_inter_ram0_force_pu_lsb)
    @reg_inter_ram0_force_pu.setter
    def reg_inter_ram0_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inter_ram0_force_pu_msb, self.__reg_inter_ram0_force_pu_lsb, value)

    @property
    def reg_inter_ram0_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inter_ram0_force_pd_msb, self.__reg_inter_ram0_force_pd_lsb)
    @reg_inter_ram0_force_pd.setter
    def reg_inter_ram0_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inter_ram0_force_pd_msb, self.__reg_inter_ram0_force_pd_lsb, value)

    @property
    def reg_rom0_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rom0_force_pu_msb, self.__reg_rom0_force_pu_lsb)
    @reg_rom0_force_pu.setter
    def reg_rom0_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rom0_force_pu_msb, self.__reg_rom0_force_pu_lsb, value)

    @property
    def reg_rom0_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rom0_force_pd_msb, self.__reg_rom0_force_pd_lsb)
    @reg_rom0_force_pd.setter
    def reg_rom0_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rom0_force_pd_msb, self.__reg_rom0_force_pd_lsb, value)

    @property
    def reg_lslp_mem_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lslp_mem_force_pu_msb, self.__reg_lslp_mem_force_pu_lsb)
    @reg_lslp_mem_force_pu.setter
    def reg_lslp_mem_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lslp_mem_force_pu_msb, self.__reg_lslp_mem_force_pu_lsb, value)

    @property
    def reg_lslp_mem_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lslp_mem_force_pd_msb, self.__reg_lslp_mem_force_pd_lsb)
    @reg_lslp_mem_force_pd.setter
    def reg_lslp_mem_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lslp_mem_force_pd_msb, self.__reg_lslp_mem_force_pd_lsb, value)
class DIG_ISO(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x88
        self.__reg_dg_wrap_force_noiso_lsb = 31
        self.__reg_dg_wrap_force_noiso_msb = 31
        self.__reg_dg_wrap_force_iso_lsb = 30
        self.__reg_dg_wrap_force_iso_msb = 30
        self.__reg_wifi_force_noiso_lsb = 29
        self.__reg_wifi_force_noiso_msb = 29
        self.__reg_wifi_force_iso_lsb = 28
        self.__reg_wifi_force_iso_msb = 28
        self.__reg_inter_ram4_force_noiso_lsb = 27
        self.__reg_inter_ram4_force_noiso_msb = 27
        self.__reg_inter_ram4_force_iso_lsb = 26
        self.__reg_inter_ram4_force_iso_msb = 26
        self.__reg_inter_ram3_force_noiso_lsb = 25
        self.__reg_inter_ram3_force_noiso_msb = 25
        self.__reg_inter_ram3_force_iso_lsb = 24
        self.__reg_inter_ram3_force_iso_msb = 24
        self.__reg_inter_ram2_force_noiso_lsb = 23
        self.__reg_inter_ram2_force_noiso_msb = 23
        self.__reg_inter_ram2_force_iso_lsb = 22
        self.__reg_inter_ram2_force_iso_msb = 22
        self.__reg_inter_ram1_force_noiso_lsb = 21
        self.__reg_inter_ram1_force_noiso_msb = 21
        self.__reg_inter_ram1_force_iso_lsb = 20
        self.__reg_inter_ram1_force_iso_msb = 20
        self.__reg_inter_ram0_force_noiso_lsb = 19
        self.__reg_inter_ram0_force_noiso_msb = 19
        self.__reg_inter_ram0_force_iso_lsb = 18
        self.__reg_inter_ram0_force_iso_msb = 18
        self.__reg_rom0_force_noiso_lsb = 17
        self.__reg_rom0_force_noiso_msb = 17
        self.__reg_rom0_force_iso_lsb = 16
        self.__reg_rom0_force_iso_msb = 16
        self.__reg_dg_pad_force_hold_lsb = 15
        self.__reg_dg_pad_force_hold_msb = 15
        self.__reg_dg_pad_force_unhold_lsb = 14
        self.__reg_dg_pad_force_unhold_msb = 14
        self.__reg_dg_pad_force_iso_lsb = 13
        self.__reg_dg_pad_force_iso_msb = 13
        self.__reg_dg_pad_force_noiso_lsb = 12
        self.__reg_dg_pad_force_noiso_msb = 12
        self.__reg_dg_pad_autohold_en_lsb = 11
        self.__reg_dg_pad_autohold_en_msb = 11
        self.__clr_dg_pad_autohold_lsb = 10
        self.__clr_dg_pad_autohold_msb = 10
        self.__dg_pad_autohold_lsb = 9
        self.__dg_pad_autohold_msb = 9
        self.__reg_dig_iso_force_on_lsb = 8
        self.__reg_dig_iso_force_on_msb = 8
        self.__reg_dig_iso_force_off_lsb = 7
        self.__reg_dig_iso_force_off_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_dg_wrap_force_noiso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dg_wrap_force_noiso_msb, self.__reg_dg_wrap_force_noiso_lsb)
    @reg_dg_wrap_force_noiso.setter
    def reg_dg_wrap_force_noiso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dg_wrap_force_noiso_msb, self.__reg_dg_wrap_force_noiso_lsb, value)

    @property
    def reg_dg_wrap_force_iso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dg_wrap_force_iso_msb, self.__reg_dg_wrap_force_iso_lsb)
    @reg_dg_wrap_force_iso.setter
    def reg_dg_wrap_force_iso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dg_wrap_force_iso_msb, self.__reg_dg_wrap_force_iso_lsb, value)

    @property
    def reg_wifi_force_noiso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wifi_force_noiso_msb, self.__reg_wifi_force_noiso_lsb)
    @reg_wifi_force_noiso.setter
    def reg_wifi_force_noiso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wifi_force_noiso_msb, self.__reg_wifi_force_noiso_lsb, value)

    @property
    def reg_wifi_force_iso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wifi_force_iso_msb, self.__reg_wifi_force_iso_lsb)
    @reg_wifi_force_iso.setter
    def reg_wifi_force_iso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wifi_force_iso_msb, self.__reg_wifi_force_iso_lsb, value)

    @property
    def reg_inter_ram4_force_noiso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inter_ram4_force_noiso_msb, self.__reg_inter_ram4_force_noiso_lsb)
    @reg_inter_ram4_force_noiso.setter
    def reg_inter_ram4_force_noiso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inter_ram4_force_noiso_msb, self.__reg_inter_ram4_force_noiso_lsb, value)

    @property
    def reg_inter_ram4_force_iso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inter_ram4_force_iso_msb, self.__reg_inter_ram4_force_iso_lsb)
    @reg_inter_ram4_force_iso.setter
    def reg_inter_ram4_force_iso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inter_ram4_force_iso_msb, self.__reg_inter_ram4_force_iso_lsb, value)

    @property
    def reg_inter_ram3_force_noiso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inter_ram3_force_noiso_msb, self.__reg_inter_ram3_force_noiso_lsb)
    @reg_inter_ram3_force_noiso.setter
    def reg_inter_ram3_force_noiso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inter_ram3_force_noiso_msb, self.__reg_inter_ram3_force_noiso_lsb, value)

    @property
    def reg_inter_ram3_force_iso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inter_ram3_force_iso_msb, self.__reg_inter_ram3_force_iso_lsb)
    @reg_inter_ram3_force_iso.setter
    def reg_inter_ram3_force_iso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inter_ram3_force_iso_msb, self.__reg_inter_ram3_force_iso_lsb, value)

    @property
    def reg_inter_ram2_force_noiso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inter_ram2_force_noiso_msb, self.__reg_inter_ram2_force_noiso_lsb)
    @reg_inter_ram2_force_noiso.setter
    def reg_inter_ram2_force_noiso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inter_ram2_force_noiso_msb, self.__reg_inter_ram2_force_noiso_lsb, value)

    @property
    def reg_inter_ram2_force_iso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inter_ram2_force_iso_msb, self.__reg_inter_ram2_force_iso_lsb)
    @reg_inter_ram2_force_iso.setter
    def reg_inter_ram2_force_iso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inter_ram2_force_iso_msb, self.__reg_inter_ram2_force_iso_lsb, value)

    @property
    def reg_inter_ram1_force_noiso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inter_ram1_force_noiso_msb, self.__reg_inter_ram1_force_noiso_lsb)
    @reg_inter_ram1_force_noiso.setter
    def reg_inter_ram1_force_noiso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inter_ram1_force_noiso_msb, self.__reg_inter_ram1_force_noiso_lsb, value)

    @property
    def reg_inter_ram1_force_iso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inter_ram1_force_iso_msb, self.__reg_inter_ram1_force_iso_lsb)
    @reg_inter_ram1_force_iso.setter
    def reg_inter_ram1_force_iso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inter_ram1_force_iso_msb, self.__reg_inter_ram1_force_iso_lsb, value)

    @property
    def reg_inter_ram0_force_noiso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inter_ram0_force_noiso_msb, self.__reg_inter_ram0_force_noiso_lsb)
    @reg_inter_ram0_force_noiso.setter
    def reg_inter_ram0_force_noiso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inter_ram0_force_noiso_msb, self.__reg_inter_ram0_force_noiso_lsb, value)

    @property
    def reg_inter_ram0_force_iso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inter_ram0_force_iso_msb, self.__reg_inter_ram0_force_iso_lsb)
    @reg_inter_ram0_force_iso.setter
    def reg_inter_ram0_force_iso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inter_ram0_force_iso_msb, self.__reg_inter_ram0_force_iso_lsb, value)

    @property
    def reg_rom0_force_noiso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rom0_force_noiso_msb, self.__reg_rom0_force_noiso_lsb)
    @reg_rom0_force_noiso.setter
    def reg_rom0_force_noiso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rom0_force_noiso_msb, self.__reg_rom0_force_noiso_lsb, value)

    @property
    def reg_rom0_force_iso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rom0_force_iso_msb, self.__reg_rom0_force_iso_lsb)
    @reg_rom0_force_iso.setter
    def reg_rom0_force_iso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rom0_force_iso_msb, self.__reg_rom0_force_iso_lsb, value)

    @property
    def reg_dg_pad_force_hold(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dg_pad_force_hold_msb, self.__reg_dg_pad_force_hold_lsb)
    @reg_dg_pad_force_hold.setter
    def reg_dg_pad_force_hold(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dg_pad_force_hold_msb, self.__reg_dg_pad_force_hold_lsb, value)

    @property
    def reg_dg_pad_force_unhold(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dg_pad_force_unhold_msb, self.__reg_dg_pad_force_unhold_lsb)
    @reg_dg_pad_force_unhold.setter
    def reg_dg_pad_force_unhold(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dg_pad_force_unhold_msb, self.__reg_dg_pad_force_unhold_lsb, value)

    @property
    def reg_dg_pad_force_iso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dg_pad_force_iso_msb, self.__reg_dg_pad_force_iso_lsb)
    @reg_dg_pad_force_iso.setter
    def reg_dg_pad_force_iso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dg_pad_force_iso_msb, self.__reg_dg_pad_force_iso_lsb, value)

    @property
    def reg_dg_pad_force_noiso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dg_pad_force_noiso_msb, self.__reg_dg_pad_force_noiso_lsb)
    @reg_dg_pad_force_noiso.setter
    def reg_dg_pad_force_noiso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dg_pad_force_noiso_msb, self.__reg_dg_pad_force_noiso_lsb, value)

    @property
    def reg_dg_pad_autohold_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dg_pad_autohold_en_msb, self.__reg_dg_pad_autohold_en_lsb)
    @reg_dg_pad_autohold_en.setter
    def reg_dg_pad_autohold_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dg_pad_autohold_en_msb, self.__reg_dg_pad_autohold_en_lsb, value)

    @property
    def clr_dg_pad_autohold(self):
        return self.__MEM.rdm(self.__addr, self.__clr_dg_pad_autohold_msb, self.__clr_dg_pad_autohold_lsb)
    @clr_dg_pad_autohold.setter
    def clr_dg_pad_autohold(self, value):
        return self.__MEM.wrm(self.__addr, self.__clr_dg_pad_autohold_msb, self.__clr_dg_pad_autohold_lsb, value)

    @property
    def dg_pad_autohold(self):
        return self.__MEM.rdm(self.__addr, self.__dg_pad_autohold_msb, self.__dg_pad_autohold_lsb)
    @dg_pad_autohold.setter
    def dg_pad_autohold(self, value):
        return self.__MEM.wrm(self.__addr, self.__dg_pad_autohold_msb, self.__dg_pad_autohold_lsb, value)

    @property
    def reg_dig_iso_force_on(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dig_iso_force_on_msb, self.__reg_dig_iso_force_on_lsb)
    @reg_dig_iso_force_on.setter
    def reg_dig_iso_force_on(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dig_iso_force_on_msb, self.__reg_dig_iso_force_on_lsb, value)

    @property
    def reg_dig_iso_force_off(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dig_iso_force_off_msb, self.__reg_dig_iso_force_off_lsb)
    @reg_dig_iso_force_off.setter
    def reg_dig_iso_force_off(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dig_iso_force_off_msb, self.__reg_dig_iso_force_off_lsb, value)
class RTC_WDTCONFIG0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x8c
        self.__reg_wdt_en_lsb = 31
        self.__reg_wdt_en_msb = 31
        self.__reg_wdt_stg0_lsb = 28
        self.__reg_wdt_stg0_msb = 30
        self.__reg_wdt_stg1_lsb = 25
        self.__reg_wdt_stg1_msb = 27
        self.__reg_wdt_stg2_lsb = 22
        self.__reg_wdt_stg2_msb = 24
        self.__reg_wdt_stg3_lsb = 19
        self.__reg_wdt_stg3_msb = 21
        self.__reg_wdt_edge_int_en_lsb = 18
        self.__reg_wdt_edge_int_en_msb = 18
        self.__reg_wdt_level_int_en_lsb = 17
        self.__reg_wdt_level_int_en_msb = 17
        self.__reg_wdt_cpu_reset_length_lsb = 14
        self.__reg_wdt_cpu_reset_length_msb = 16
        self.__reg_wdt_sys_reset_length_lsb = 11
        self.__reg_wdt_sys_reset_length_msb = 13
        self.__reg_wdt_flashboot_mod_en_lsb = 10
        self.__reg_wdt_flashboot_mod_en_msb = 10
        self.__reg_wdt_procpu_reset_en_lsb = 9
        self.__reg_wdt_procpu_reset_en_msb = 9
        self.__reg_wdt_appcpu_reset_en_lsb = 8
        self.__reg_wdt_appcpu_reset_en_msb = 8
        self.__reg_wdt_pause_in_slp_lsb = 7
        self.__reg_wdt_pause_in_slp_msb = 7
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

    @property
    def reg_wdt_pause_in_slp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wdt_pause_in_slp_msb, self.__reg_wdt_pause_in_slp_lsb)
    @reg_wdt_pause_in_slp.setter
    def reg_wdt_pause_in_slp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wdt_pause_in_slp_msb, self.__reg_wdt_pause_in_slp_lsb, value)
class RTC_WDTCONFIG1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x90
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
class RTC_WDTCONFIG2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x94
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
class RTC_WDTCONFIG3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x98
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
class RTC_WDTCONFIG4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x9c
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
class RTC_WDTFEED(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0xa0
        self.__rtc_wdt_feed_lsb = 31
        self.__rtc_wdt_feed_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_wdt_feed(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_wdt_feed_msb, self.__rtc_wdt_feed_lsb)
    @rtc_wdt_feed.setter
    def rtc_wdt_feed(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_wdt_feed_msb, self.__rtc_wdt_feed_lsb, value)
class RTC_WDTWPROTECT(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0xa4
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
class RTC_TEST_MUX(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0xa8
        self.__reg_dtest_rtc_lsb = 30
        self.__reg_dtest_rtc_msb = 31
        self.__reg_ent_rtc_lsb = 29
        self.__reg_ent_rtc_msb = 29
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_dtest_rtc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dtest_rtc_msb, self.__reg_dtest_rtc_lsb)
    @reg_dtest_rtc.setter
    def reg_dtest_rtc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dtest_rtc_msb, self.__reg_dtest_rtc_lsb, value)

    @property
    def reg_ent_rtc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ent_rtc_msb, self.__reg_ent_rtc_lsb)
    @reg_ent_rtc.setter
    def reg_ent_rtc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ent_rtc_msb, self.__reg_ent_rtc_lsb, value)
class RTC_SW_CPU_STALL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0xac
        self.__reg_sw_stall_procpu_c1_lsb = 26
        self.__reg_sw_stall_procpu_c1_msb = 31
        self.__reg_sw_stall_appcpu_c1_lsb = 20
        self.__reg_sw_stall_appcpu_c1_msb = 25
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sw_stall_procpu_c1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sw_stall_procpu_c1_msb, self.__reg_sw_stall_procpu_c1_lsb)
    @reg_sw_stall_procpu_c1.setter
    def reg_sw_stall_procpu_c1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sw_stall_procpu_c1_msb, self.__reg_sw_stall_procpu_c1_lsb, value)

    @property
    def reg_sw_stall_appcpu_c1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sw_stall_appcpu_c1_msb, self.__reg_sw_stall_appcpu_c1_lsb)
    @reg_sw_stall_appcpu_c1.setter
    def reg_sw_stall_appcpu_c1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sw_stall_appcpu_c1_msb, self.__reg_sw_stall_appcpu_c1_lsb, value)
class RTC_STORE4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0xb0
        self.__rtc_scratch4_lsb = 0
        self.__rtc_scratch4_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_scratch4(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_scratch4_msb, self.__rtc_scratch4_lsb)
    @rtc_scratch4.setter
    def rtc_scratch4(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_scratch4_msb, self.__rtc_scratch4_lsb, value)
class RTC_STORE5(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0xb4
        self.__rtc_scratch5_lsb = 0
        self.__rtc_scratch5_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_scratch5(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_scratch5_msb, self.__rtc_scratch5_lsb)
    @rtc_scratch5.setter
    def rtc_scratch5(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_scratch5_msb, self.__rtc_scratch5_lsb, value)
class RTC_STORE6(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0xb8
        self.__rtc_scratch6_lsb = 0
        self.__rtc_scratch6_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_scratch6(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_scratch6_msb, self.__rtc_scratch6_lsb)
    @rtc_scratch6.setter
    def rtc_scratch6(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_scratch6_msb, self.__rtc_scratch6_lsb, value)
class RTC_STORE7(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0xbc
        self.__rtc_scratch7_lsb = 0
        self.__rtc_scratch7_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_scratch7(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_scratch7_msb, self.__rtc_scratch7_lsb)
    @rtc_scratch7.setter
    def rtc_scratch7(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_scratch7_msb, self.__rtc_scratch7_lsb, value)
class RTC_DIAG0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0xc0
        self.__rtc_low_power_diag0_lsb = 0
        self.__rtc_low_power_diag0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_low_power_diag0(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_low_power_diag0_msb, self.__rtc_low_power_diag0_lsb)
    @rtc_low_power_diag0.setter
    def rtc_low_power_diag0(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_low_power_diag0_msb, self.__rtc_low_power_diag0_lsb, value)
class RTC_DIAG1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0xc4
        self.__rtc_low_power_diag1_lsb = 0
        self.__rtc_low_power_diag1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_low_power_diag1(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_low_power_diag1_msb, self.__rtc_low_power_diag1_lsb)
    @rtc_low_power_diag1.setter
    def rtc_low_power_diag1(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_low_power_diag1_msb, self.__rtc_low_power_diag1_lsb, value)
class RTC_HOLD_FORCE(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0xc8
        self.__reg_x32n_hold_force_lsb = 17
        self.__reg_x32n_hold_force_msb = 17
        self.__reg_x32p_hold_force_lsb = 16
        self.__reg_x32p_hold_force_msb = 16
        self.__reg_touch_pad7_hold_force_lsb = 15
        self.__reg_touch_pad7_hold_force_msb = 15
        self.__reg_touch_pad6_hold_force_lsb = 14
        self.__reg_touch_pad6_hold_force_msb = 14
        self.__reg_touch_pad5_hold_force_lsb = 13
        self.__reg_touch_pad5_hold_force_msb = 13
        self.__reg_touch_pad4_hold_force_lsb = 12
        self.__reg_touch_pad4_hold_force_msb = 12
        self.__reg_touch_pad3_hold_force_lsb = 11
        self.__reg_touch_pad3_hold_force_msb = 11
        self.__reg_touch_pad2_hold_force_lsb = 10
        self.__reg_touch_pad2_hold_force_msb = 10
        self.__reg_touch_pad1_hold_force_lsb = 9
        self.__reg_touch_pad1_hold_force_msb = 9
        self.__reg_touch_pad0_hold_force_lsb = 8
        self.__reg_touch_pad0_hold_force_msb = 8
        self.__reg_sense4_hold_force_lsb = 7
        self.__reg_sense4_hold_force_msb = 7
        self.__reg_sense3_hold_force_lsb = 6
        self.__reg_sense3_hold_force_msb = 6
        self.__reg_sense2_hold_force_lsb = 5
        self.__reg_sense2_hold_force_msb = 5
        self.__reg_sense1_hold_force_lsb = 4
        self.__reg_sense1_hold_force_msb = 4
        self.__reg_pdac2_hold_force_lsb = 3
        self.__reg_pdac2_hold_force_msb = 3
        self.__reg_pdac1_hold_force_lsb = 2
        self.__reg_pdac1_hold_force_msb = 2
        self.__reg_adc2_hold_force_lsb = 1
        self.__reg_adc2_hold_force_msb = 1
        self.__reg_adc1_hold_force_lsb = 0
        self.__reg_adc1_hold_force_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_x32n_hold_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_x32n_hold_force_msb, self.__reg_x32n_hold_force_lsb)
    @reg_x32n_hold_force.setter
    def reg_x32n_hold_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_x32n_hold_force_msb, self.__reg_x32n_hold_force_lsb, value)

    @property
    def reg_x32p_hold_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_x32p_hold_force_msb, self.__reg_x32p_hold_force_lsb)
    @reg_x32p_hold_force.setter
    def reg_x32p_hold_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_x32p_hold_force_msb, self.__reg_x32p_hold_force_lsb, value)

    @property
    def reg_touch_pad7_hold_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad7_hold_force_msb, self.__reg_touch_pad7_hold_force_lsb)
    @reg_touch_pad7_hold_force.setter
    def reg_touch_pad7_hold_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad7_hold_force_msb, self.__reg_touch_pad7_hold_force_lsb, value)

    @property
    def reg_touch_pad6_hold_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad6_hold_force_msb, self.__reg_touch_pad6_hold_force_lsb)
    @reg_touch_pad6_hold_force.setter
    def reg_touch_pad6_hold_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad6_hold_force_msb, self.__reg_touch_pad6_hold_force_lsb, value)

    @property
    def reg_touch_pad5_hold_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad5_hold_force_msb, self.__reg_touch_pad5_hold_force_lsb)
    @reg_touch_pad5_hold_force.setter
    def reg_touch_pad5_hold_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad5_hold_force_msb, self.__reg_touch_pad5_hold_force_lsb, value)

    @property
    def reg_touch_pad4_hold_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad4_hold_force_msb, self.__reg_touch_pad4_hold_force_lsb)
    @reg_touch_pad4_hold_force.setter
    def reg_touch_pad4_hold_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad4_hold_force_msb, self.__reg_touch_pad4_hold_force_lsb, value)

    @property
    def reg_touch_pad3_hold_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad3_hold_force_msb, self.__reg_touch_pad3_hold_force_lsb)
    @reg_touch_pad3_hold_force.setter
    def reg_touch_pad3_hold_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad3_hold_force_msb, self.__reg_touch_pad3_hold_force_lsb, value)

    @property
    def reg_touch_pad2_hold_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad2_hold_force_msb, self.__reg_touch_pad2_hold_force_lsb)
    @reg_touch_pad2_hold_force.setter
    def reg_touch_pad2_hold_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad2_hold_force_msb, self.__reg_touch_pad2_hold_force_lsb, value)

    @property
    def reg_touch_pad1_hold_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad1_hold_force_msb, self.__reg_touch_pad1_hold_force_lsb)
    @reg_touch_pad1_hold_force.setter
    def reg_touch_pad1_hold_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad1_hold_force_msb, self.__reg_touch_pad1_hold_force_lsb, value)

    @property
    def reg_touch_pad0_hold_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad0_hold_force_msb, self.__reg_touch_pad0_hold_force_lsb)
    @reg_touch_pad0_hold_force.setter
    def reg_touch_pad0_hold_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad0_hold_force_msb, self.__reg_touch_pad0_hold_force_lsb, value)

    @property
    def reg_sense4_hold_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sense4_hold_force_msb, self.__reg_sense4_hold_force_lsb)
    @reg_sense4_hold_force.setter
    def reg_sense4_hold_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sense4_hold_force_msb, self.__reg_sense4_hold_force_lsb, value)

    @property
    def reg_sense3_hold_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sense3_hold_force_msb, self.__reg_sense3_hold_force_lsb)
    @reg_sense3_hold_force.setter
    def reg_sense3_hold_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sense3_hold_force_msb, self.__reg_sense3_hold_force_lsb, value)

    @property
    def reg_sense2_hold_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sense2_hold_force_msb, self.__reg_sense2_hold_force_lsb)
    @reg_sense2_hold_force.setter
    def reg_sense2_hold_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sense2_hold_force_msb, self.__reg_sense2_hold_force_lsb, value)

    @property
    def reg_sense1_hold_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sense1_hold_force_msb, self.__reg_sense1_hold_force_lsb)
    @reg_sense1_hold_force.setter
    def reg_sense1_hold_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sense1_hold_force_msb, self.__reg_sense1_hold_force_lsb, value)

    @property
    def reg_pdac2_hold_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdac2_hold_force_msb, self.__reg_pdac2_hold_force_lsb)
    @reg_pdac2_hold_force.setter
    def reg_pdac2_hold_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdac2_hold_force_msb, self.__reg_pdac2_hold_force_lsb, value)

    @property
    def reg_pdac1_hold_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdac1_hold_force_msb, self.__reg_pdac1_hold_force_lsb)
    @reg_pdac1_hold_force.setter
    def reg_pdac1_hold_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdac1_hold_force_msb, self.__reg_pdac1_hold_force_lsb, value)

    @property
    def reg_adc2_hold_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc2_hold_force_msb, self.__reg_adc2_hold_force_lsb)
    @reg_adc2_hold_force.setter
    def reg_adc2_hold_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc2_hold_force_msb, self.__reg_adc2_hold_force_lsb, value)

    @property
    def reg_adc1_hold_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc1_hold_force_msb, self.__reg_adc1_hold_force_lsb)
    @reg_adc1_hold_force.setter
    def reg_adc1_hold_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc1_hold_force_msb, self.__reg_adc1_hold_force_lsb, value)
class RTC_EXT_WAKEUP1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0xcc
        self.__reg_ext_wakeup1_status_clr_lsb = 18
        self.__reg_ext_wakeup1_status_clr_msb = 18
        self.__reg_ext_wakeup1_sel_lsb = 0
        self.__reg_ext_wakeup1_sel_msb = 17
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ext_wakeup1_status_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ext_wakeup1_status_clr_msb, self.__reg_ext_wakeup1_status_clr_lsb)
    @reg_ext_wakeup1_status_clr.setter
    def reg_ext_wakeup1_status_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ext_wakeup1_status_clr_msb, self.__reg_ext_wakeup1_status_clr_lsb, value)

    @property
    def reg_ext_wakeup1_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ext_wakeup1_sel_msb, self.__reg_ext_wakeup1_sel_lsb)
    @reg_ext_wakeup1_sel.setter
    def reg_ext_wakeup1_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ext_wakeup1_sel_msb, self.__reg_ext_wakeup1_sel_lsb, value)
class RTC_EXT_WAKEUP1_STATUS(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0xd0
        self.__reg_ext_wakeup1_status_lsb = 0
        self.__reg_ext_wakeup1_status_msb = 17
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ext_wakeup1_status(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ext_wakeup1_status_msb, self.__reg_ext_wakeup1_status_lsb)
    @reg_ext_wakeup1_status.setter
    def reg_ext_wakeup1_status(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ext_wakeup1_status_msb, self.__reg_ext_wakeup1_status_lsb, value)
class RTC_BROWN_OUT(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0xd4
        self.__rtc_brown_out_det_lsb = 31
        self.__rtc_brown_out_det_msb = 31
        self.__reg_brown_out_ena_lsb = 30
        self.__reg_brown_out_ena_msb = 30
        self.__reg_dbrown_out_thres_lsb = 27
        self.__reg_dbrown_out_thres_msb = 29
        self.__reg_brown_out_rst_ena_lsb = 26
        self.__reg_brown_out_rst_ena_msb = 26
        self.__reg_brown_out_rst_wait_lsb = 16
        self.__reg_brown_out_rst_wait_msb = 25
        self.__reg_brown_out_pd_rf_ena_lsb = 15
        self.__reg_brown_out_pd_rf_ena_msb = 15
        self.__reg_brown_out_close_flash_ena_lsb = 14
        self.__reg_brown_out_close_flash_ena_msb = 14
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_brown_out_det(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_brown_out_det_msb, self.__rtc_brown_out_det_lsb)
    @rtc_brown_out_det.setter
    def rtc_brown_out_det(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_brown_out_det_msb, self.__rtc_brown_out_det_lsb, value)

    @property
    def reg_brown_out_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_brown_out_ena_msb, self.__reg_brown_out_ena_lsb)
    @reg_brown_out_ena.setter
    def reg_brown_out_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_brown_out_ena_msb, self.__reg_brown_out_ena_lsb, value)

    @property
    def reg_dbrown_out_thres(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dbrown_out_thres_msb, self.__reg_dbrown_out_thres_lsb)
    @reg_dbrown_out_thres.setter
    def reg_dbrown_out_thres(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dbrown_out_thres_msb, self.__reg_dbrown_out_thres_lsb, value)

    @property
    def reg_brown_out_rst_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_brown_out_rst_ena_msb, self.__reg_brown_out_rst_ena_lsb)
    @reg_brown_out_rst_ena.setter
    def reg_brown_out_rst_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_brown_out_rst_ena_msb, self.__reg_brown_out_rst_ena_lsb, value)

    @property
    def reg_brown_out_rst_wait(self):
        return self.__MEM.rdm(self.__addr, self.__reg_brown_out_rst_wait_msb, self.__reg_brown_out_rst_wait_lsb)
    @reg_brown_out_rst_wait.setter
    def reg_brown_out_rst_wait(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_brown_out_rst_wait_msb, self.__reg_brown_out_rst_wait_lsb, value)

    @property
    def reg_brown_out_pd_rf_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_brown_out_pd_rf_ena_msb, self.__reg_brown_out_pd_rf_ena_lsb)
    @reg_brown_out_pd_rf_ena.setter
    def reg_brown_out_pd_rf_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_brown_out_pd_rf_ena_msb, self.__reg_brown_out_pd_rf_ena_lsb, value)

    @property
    def reg_brown_out_close_flash_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_brown_out_close_flash_ena_msb, self.__reg_brown_out_close_flash_ena_lsb)
    @reg_brown_out_close_flash_ena.setter
    def reg_brown_out_close_flash_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_brown_out_close_flash_ena_msb, self.__reg_brown_out_close_flash_ena_lsb, value)
class RTC_CNTL_DATE(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_CNTL_BASE + 0x13c
        self.__rtc_cntl_date_lsb = 0
        self.__rtc_cntl_date_msb = 27
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_cntl_date(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_cntl_date_msb, self.__rtc_cntl_date_lsb)
    @rtc_cntl_date.setter
    def rtc_cntl_date(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_cntl_date_msb, self.__rtc_cntl_date_lsb, value)
    @property
    def default_value(self):
        return 0x1604280
