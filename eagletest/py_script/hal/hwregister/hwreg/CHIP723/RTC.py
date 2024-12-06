from hal.common import *
from hal.hwregister.hwreg.CHIP723.addr_base import *
class RTC(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.RTC_CTRL0 = RTC_CTRL0(self.channel, self.chipv)
        self.RTC_SLP = RTC_SLP(self.channel, self.chipv)
        self.RTC_CLP_CTRL = RTC_CLP_CTRL(self.channel, self.chipv)
        self.RTC_BUF_WAIT = RTC_BUF_WAIT(self.channel, self.chipv)
        self.RTC_ANA_CONF = RTC_ANA_CONF(self.channel, self.chipv)
        self.RTC_RESET_CAUSE = RTC_RESET_CAUSE(self.channel, self.chipv)
        self.RTC_WAKEUP_ENA = RTC_WAKEUP_ENA(self.channel, self.chipv)
        self.RTC_SLP_CNT = RTC_SLP_CNT(self.channel, self.chipv)
        self.RTC_INT_ENA = RTC_INT_ENA(self.channel, self.chipv)
        self.RTC_INT_CLR = RTC_INT_CLR(self.channel, self.chipv)
        self.RTC_INT_RAW = RTC_INT_RAW(self.channel, self.chipv)
        self.RTC_REMAIN0 = RTC_REMAIN0(self.channel, self.chipv)
        self.RTC_SCRATCH0 = RTC_SCRATCH0(self.channel, self.chipv)
        self.RTC_SCRATCH1 = RTC_SCRATCH1(self.channel, self.chipv)
        self.RTC_SCRATCH2 = RTC_SCRATCH2(self.channel, self.chipv)
        self.RTC_SCRATCH3 = RTC_SCRATCH3(self.channel, self.chipv)
        self.RTC_CPU_RAM_PD_EN = RTC_CPU_RAM_PD_EN(self.channel, self.chipv)
        self.RTC_PD_EN = RTC_PD_EN(self.channel, self.chipv)
        self.RTC_CPU_TIMER = RTC_CPU_TIMER(self.channel, self.chipv)
        self.RTC_SOC_TIMER = RTC_SOC_TIMER(self.channel, self.chipv)
        self.RTC_REMAIN1 = RTC_REMAIN1(self.channel, self.chipv)
        self.RTC_LOW_POWER_DIAG = RTC_LOW_POWER_DIAG(self.channel, self.chipv)
        self.RTC_CPU_RAM_FORCE_ISO = RTC_CPU_RAM_FORCE_ISO(self.channel, self.chipv)
        self.RTC_CPU_RAM_FORCE_NOISO = RTC_CPU_RAM_FORCE_NOISO(self.channel, self.chipv)
        self.RTC_CPU_RAM_FORCE_PU = RTC_CPU_RAM_FORCE_PU(self.channel, self.chipv)
        self.RTC_XTAL_EXT_CTR = RTC_XTAL_EXT_CTR(self.channel, self.chipv)
        self.RTC_GPIO_OUT_DATA = RTC_GPIO_OUT_DATA(self.channel, self.chipv)
        self.RTC_GPIO_ENABLE = RTC_GPIO_ENABLE(self.channel, self.chipv)
        self.RTC_GPIO_STATUS_INT = RTC_GPIO_STATUS_INT(self.channel, self.chipv)
        self.RTC_GPIO_IN_SYNC = RTC_GPIO_IN_SYNC(self.channel, self.chipv)
        self.RTC_GPIO_INT_TYPE = RTC_GPIO_INT_TYPE(self.channel, self.chipv)
        self.RTC_GPIO_WAKEUP = RTC_GPIO_WAKEUP(self.channel, self.chipv)
        self.RTC_EXT_WAKEUP = RTC_EXT_WAKEUP(self.channel, self.chipv)
        self.RTC_DEBUG_SEL = RTC_DEBUG_SEL(self.channel, self.chipv)
        self.RTC_PAD_XPD_DCDC = RTC_PAD_XPD_DCDC(self.channel, self.chipv)
        self.RTC_REMAIN2 = RTC_REMAIN2(self.channel, self.chipv)
        self.RTC_SLP_REJECT = RTC_SLP_REJECT(self.channel, self.chipv)
        self.RTC_CPU_RAM_FORCE_PD = RTC_CPU_RAM_FORCE_PD(self.channel, self.chipv)
        self.RTC_FORCE_PD = RTC_FORCE_PD(self.channel, self.chipv)
        self.RTC_CPU_PERIOD_SEL = RTC_CPU_PERIOD_SEL(self.channel, self.chipv)
        self.RTC_SDIO_ACT_DNUM = RTC_SDIO_ACT_DNUM(self.channel, self.chipv)
class RTC_CTRL0(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x0
        self.__sw_sys_rst_lsb = 31
        self.__sw_sys_rst_msb = 31
        self.__reg_pll_force_out_lsb = 24
        self.__reg_pll_force_out_msb = 24
        self.__reg_xpd_bg_sel_lsb = 23
        self.__reg_xpd_bg_sel_msb = 23
        self.__reg_dg_wrap_force_norst_lsb = 22
        self.__reg_dg_wrap_force_norst_msb = 22
        self.__reg_dg_wrap_force_rst_lsb = 21
        self.__reg_dg_wrap_force_rst_msb = 21
        self.__reg_analog_force_noiso_lsb = 20
        self.__reg_analog_force_noiso_msb = 20
        self.__reg_soc_pad_force_noiso_lsb = 19
        self.__reg_soc_pad_force_noiso_msb = 19
        self.__reg_pll_force_noiso_lsb = 16
        self.__reg_pll_force_noiso_msb = 16
        self.__reg_xtl_force_noiso_lsb = 15
        self.__reg_xtl_force_noiso_msb = 15
        self.__reg_bb_force_noiso_lsb = 14
        self.__reg_bb_force_noiso_msb = 14
        self.__reg_analog_force_iso_lsb = 13
        self.__reg_analog_force_iso_msb = 13
        self.__reg_soc_pad_force_iso_lsb = 12
        self.__reg_soc_pad_force_iso_msb = 12
        self.__reg_pll_force_iso_lsb = 9
        self.__reg_pll_force_iso_msb = 9
        self.__reg_xtl_force_iso_lsb = 8
        self.__reg_xtl_force_iso_msb = 8
        self.__reg_bb_force_iso_lsb = 7
        self.__reg_bb_force_iso_msb = 7
        self.__reg_bg_force_pu_lsb = 6
        self.__reg_bg_force_pu_msb = 6
        self.__reg_xtl_force_pu_lsb = 5
        self.__reg_xtl_force_pu_msb = 5
        self.__reg_pll_force_pu_lsb = 4
        self.__reg_pll_force_pu_msb = 4
        self.__reg_bb_force_pu_lsb = 3
        self.__reg_bb_force_pu_msb = 3
        self.__reg_soc_pad_force_pu_lsb = 1
        self.__reg_soc_pad_force_pu_msb = 1
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
    def reg_pll_force_out(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pll_force_out_msb, self.__reg_pll_force_out_lsb)
    @reg_pll_force_out.setter
    def reg_pll_force_out(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pll_force_out_msb, self.__reg_pll_force_out_lsb, value)

    @property
    def reg_xpd_bg_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xpd_bg_sel_msb, self.__reg_xpd_bg_sel_lsb)
    @reg_xpd_bg_sel.setter
    def reg_xpd_bg_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xpd_bg_sel_msb, self.__reg_xpd_bg_sel_lsb, value)

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
    def reg_soc_pad_force_noiso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_soc_pad_force_noiso_msb, self.__reg_soc_pad_force_noiso_lsb)
    @reg_soc_pad_force_noiso.setter
    def reg_soc_pad_force_noiso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_soc_pad_force_noiso_msb, self.__reg_soc_pad_force_noiso_lsb, value)

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
    def reg_bb_force_noiso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_force_noiso_msb, self.__reg_bb_force_noiso_lsb)
    @reg_bb_force_noiso.setter
    def reg_bb_force_noiso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_force_noiso_msb, self.__reg_bb_force_noiso_lsb, value)

    @property
    def reg_analog_force_iso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_analog_force_iso_msb, self.__reg_analog_force_iso_lsb)
    @reg_analog_force_iso.setter
    def reg_analog_force_iso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_analog_force_iso_msb, self.__reg_analog_force_iso_lsb, value)

    @property
    def reg_soc_pad_force_iso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_soc_pad_force_iso_msb, self.__reg_soc_pad_force_iso_lsb)
    @reg_soc_pad_force_iso.setter
    def reg_soc_pad_force_iso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_soc_pad_force_iso_msb, self.__reg_soc_pad_force_iso_lsb, value)

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
    def reg_bb_force_iso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_force_iso_msb, self.__reg_bb_force_iso_lsb)
    @reg_bb_force_iso.setter
    def reg_bb_force_iso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_force_iso_msb, self.__reg_bb_force_iso_lsb, value)

    @property
    def reg_bg_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bg_force_pu_msb, self.__reg_bg_force_pu_lsb)
    @reg_bg_force_pu.setter
    def reg_bg_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bg_force_pu_msb, self.__reg_bg_force_pu_lsb, value)

    @property
    def reg_xtl_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xtl_force_pu_msb, self.__reg_xtl_force_pu_lsb)
    @reg_xtl_force_pu.setter
    def reg_xtl_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xtl_force_pu_msb, self.__reg_xtl_force_pu_lsb, value)

    @property
    def reg_pll_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pll_force_pu_msb, self.__reg_pll_force_pu_lsb)
    @reg_pll_force_pu.setter
    def reg_pll_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pll_force_pu_msb, self.__reg_pll_force_pu_lsb, value)

    @property
    def reg_bb_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_force_pu_msb, self.__reg_bb_force_pu_lsb)
    @reg_bb_force_pu.setter
    def reg_bb_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_force_pu_msb, self.__reg_bb_force_pu_lsb, value)

    @property
    def reg_soc_pad_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_soc_pad_force_pu_msb, self.__reg_soc_pad_force_pu_lsb)
    @reg_soc_pad_force_pu.setter
    def reg_soc_pad_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_soc_pad_force_pu_msb, self.__reg_soc_pad_force_pu_lsb, value)
class RTC_SLP(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x4
        self.__slp_val_lsb = 0
        self.__slp_val_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def slp_val(self):
        return self.__MEM.rdm(self.__addr, self.__slp_val_msb, self.__slp_val_lsb)
    @slp_val.setter
    def slp_val(self, value):
        return self.__MEM.wrm(self.__addr, self.__slp_val_msb, self.__slp_val_lsb, value)
class RTC_CLP_CTRL(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x8
        self.__sdio_active_ind_lsb = 23
        self.__sdio_active_ind_msb = 23
        self.__slp_reject_lsb = 22
        self.__slp_reject_msb = 22
        self.__slp_wakeup_lsb = 21
        self.__slp_wakeup_msb = 21
        self.__reg_sleep_en_lsb = 20
        self.__reg_sleep_en_msb = 20
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sdio_active_ind(self):
        return self.__MEM.rdm(self.__addr, self.__sdio_active_ind_msb, self.__sdio_active_ind_lsb)
    @sdio_active_ind.setter
    def sdio_active_ind(self, value):
        return self.__MEM.wrm(self.__addr, self.__sdio_active_ind_msb, self.__sdio_active_ind_lsb, value)

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
    def reg_sleep_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sleep_en_msb, self.__reg_sleep_en_lsb)
    @reg_sleep_en.setter
    def reg_sleep_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sleep_en_msb, self.__reg_sleep_en_lsb, value)
class RTC_BUF_WAIT(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0xc
        self.__pll_buf_wait_lsb = 12
        self.__pll_buf_wait_msb = 19
        self.__xtl_buf_wait_lsb = 0
        self.__xtl_buf_wait_msb = 9
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
class RTC_ANA_CONF(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x10
        self.__rtc_ana_conf_tmp_lsb = 25
        self.__rtc_ana_conf_tmp_msb = 31
        self.__reg_core_work_vol_lsb = 4
        self.__reg_core_work_vol_msb = 7
        self.__reg_core_slp_vol_lsb = 0
        self.__reg_core_slp_vol_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_ana_conf_tmp(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_ana_conf_tmp_msb, self.__rtc_ana_conf_tmp_lsb)
    @rtc_ana_conf_tmp.setter
    def rtc_ana_conf_tmp(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_ana_conf_tmp_msb, self.__rtc_ana_conf_tmp_lsb, value)

    @property
    def reg_core_work_vol(self):
        return self.__MEM.rdm(self.__addr, self.__reg_core_work_vol_msb, self.__reg_core_work_vol_lsb)
    @reg_core_work_vol.setter
    def reg_core_work_vol(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_core_work_vol_msb, self.__reg_core_work_vol_lsb, value)

    @property
    def reg_core_slp_vol(self):
        return self.__MEM.rdm(self.__addr, self.__reg_core_slp_vol_msb, self.__reg_core_slp_vol_lsb)
    @reg_core_slp_vol.setter
    def reg_core_slp_vol(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_core_slp_vol_msb, self.__reg_core_slp_vol_lsb, value)
class RTC_RESET_CAUSE(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x14
        self.__reset_cause_lsb = 0
        self.__reset_cause_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reset_cause(self):
        return self.__MEM.rdm(self.__addr, self.__reset_cause_msb, self.__reset_cause_lsb)
    @reset_cause.setter
    def reset_cause(self, value):
        return self.__MEM.wrm(self.__addr, self.__reset_cause_msb, self.__reset_cause_lsb, value)
class RTC_WAKEUP_ENA(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x18
        self.__wakeup_cause_lsb = 8
        self.__wakeup_cause_msb = 15
        self.__reg_rtc_wakeup_ena_lsb = 0
        self.__reg_rtc_wakeup_ena_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def wakeup_cause(self):
        return self.__MEM.rdm(self.__addr, self.__wakeup_cause_msb, self.__wakeup_cause_lsb)
    @wakeup_cause.setter
    def wakeup_cause(self, value):
        return self.__MEM.wrm(self.__addr, self.__wakeup_cause_msb, self.__wakeup_cause_lsb, value)

    @property
    def reg_rtc_wakeup_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_wakeup_ena_msb, self.__reg_rtc_wakeup_ena_lsb)
    @reg_rtc_wakeup_ena.setter
    def reg_rtc_wakeup_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_wakeup_ena_msb, self.__reg_rtc_wakeup_ena_lsb, value)
class RTC_SLP_CNT(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x1c
        self.__slp_cnt_val_lsb = 0
        self.__slp_cnt_val_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def slp_cnt_val(self):
        return self.__MEM.rdm(self.__addr, self.__slp_cnt_val_msb, self.__slp_cnt_val_lsb)
    @slp_cnt_val.setter
    def slp_cnt_val(self, value):
        return self.__MEM.wrm(self.__addr, self.__slp_cnt_val_msb, self.__slp_cnt_val_lsb, value)
class RTC_INT_ENA(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x20
        self.__rtc_core_int_ena_lsb = 0
        self.__rtc_core_int_ena_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_core_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_core_int_ena_msb, self.__rtc_core_int_ena_lsb)
    @rtc_core_int_ena.setter
    def rtc_core_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_core_int_ena_msb, self.__rtc_core_int_ena_lsb, value)
class RTC_INT_CLR(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x24
        self.__rtc_core_int_clr_lsb = 0
        self.__rtc_core_int_clr_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_core_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_core_int_clr_msb, self.__rtc_core_int_clr_lsb)
    @rtc_core_int_clr.setter
    def rtc_core_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_core_int_clr_msb, self.__rtc_core_int_clr_lsb, value)
class RTC_INT_RAW(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x28
        self.__rtc_core_int_raw_lsb = 0
        self.__rtc_core_int_raw_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_core_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_core_int_raw_msb, self.__rtc_core_int_raw_lsb)
    @rtc_core_int_raw.setter
    def rtc_core_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_core_int_raw_msb, self.__rtc_core_int_raw_lsb, value)
class RTC_REMAIN0(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x2c
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)
class RTC_SCRATCH0(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x30
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
class RTC_SCRATCH1(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x34
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
class RTC_SCRATCH2(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x38
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
class RTC_SCRATCH3(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x3c
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
class RTC_CPU_RAM_PD_EN(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x40
        self.__reg_cpu_ram_pd_en_lsb = 0
        self.__reg_cpu_ram_pd_en_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_cpu_ram_pd_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cpu_ram_pd_en_msb, self.__reg_cpu_ram_pd_en_lsb)
    @reg_cpu_ram_pd_en.setter
    def reg_cpu_ram_pd_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cpu_ram_pd_en_msb, self.__reg_cpu_ram_pd_en_lsb, value)
class RTC_PD_EN(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x44
        self.__reg_soc_pad_pd_en_lsb = 5
        self.__reg_soc_pad_pd_en_msb = 5
        self.__reg_bb_pd_en_lsb = 2
        self.__reg_bb_pd_en_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_soc_pad_pd_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_soc_pad_pd_en_msb, self.__reg_soc_pad_pd_en_lsb)
    @reg_soc_pad_pd_en.setter
    def reg_soc_pad_pd_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_soc_pad_pd_en_msb, self.__reg_soc_pad_pd_en_lsb, value)

    @property
    def reg_bb_pd_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_pd_en_msb, self.__reg_bb_pd_en_lsb)
    @reg_bb_pd_en.setter
    def reg_bb_pd_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_pd_en_msb, self.__reg_bb_pd_en_lsb, value)
class RTC_CPU_TIMER(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x48
        self.__reg_cpu_ram_powerup_timer_lsb = 25
        self.__reg_cpu_ram_powerup_timer_msb = 31
        self.__reg_cpu_ram_wait_timer_lsb = 16
        self.__reg_cpu_ram_wait_timer_msb = 24
        self.__reg_bb_powerup_timer_lsb = 9
        self.__reg_bb_powerup_timer_msb = 15
        self.__reg_bb_wait_timer_lsb = 0
        self.__reg_bb_wait_timer_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_cpu_ram_powerup_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cpu_ram_powerup_timer_msb, self.__reg_cpu_ram_powerup_timer_lsb)
    @reg_cpu_ram_powerup_timer.setter
    def reg_cpu_ram_powerup_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cpu_ram_powerup_timer_msb, self.__reg_cpu_ram_powerup_timer_lsb, value)

    @property
    def reg_cpu_ram_wait_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cpu_ram_wait_timer_msb, self.__reg_cpu_ram_wait_timer_lsb)
    @reg_cpu_ram_wait_timer.setter
    def reg_cpu_ram_wait_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cpu_ram_wait_timer_msb, self.__reg_cpu_ram_wait_timer_lsb, value)

    @property
    def reg_bb_powerup_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_powerup_timer_msb, self.__reg_bb_powerup_timer_lsb)
    @reg_bb_powerup_timer.setter
    def reg_bb_powerup_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_powerup_timer_msb, self.__reg_bb_powerup_timer_lsb, value)

    @property
    def reg_bb_wait_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_wait_timer_msb, self.__reg_bb_wait_timer_lsb)
    @reg_bb_wait_timer.setter
    def reg_bb_wait_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_wait_timer_msb, self.__reg_bb_wait_timer_lsb, value)
class RTC_SOC_TIMER(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x4c
        self.__reg_soc_pad_powerup_timer_lsb = 25
        self.__reg_soc_pad_powerup_timer_msb = 31
        self.__reg_soc_pad_wait_timer_lsb = 16
        self.__reg_soc_pad_wait_timer_msb = 24
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_soc_pad_powerup_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_soc_pad_powerup_timer_msb, self.__reg_soc_pad_powerup_timer_lsb)
    @reg_soc_pad_powerup_timer.setter
    def reg_soc_pad_powerup_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_soc_pad_powerup_timer_msb, self.__reg_soc_pad_powerup_timer_lsb, value)

    @property
    def reg_soc_pad_wait_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_soc_pad_wait_timer_msb, self.__reg_soc_pad_wait_timer_lsb)
    @reg_soc_pad_wait_timer.setter
    def reg_soc_pad_wait_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_soc_pad_wait_timer_msb, self.__reg_soc_pad_wait_timer_lsb, value)
class RTC_REMAIN1(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x50
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)
class RTC_LOW_POWER_DIAG(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x54
        self.__rtc_low_power_diag_lsb = 0
        self.__rtc_low_power_diag_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_low_power_diag(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_low_power_diag_msb, self.__rtc_low_power_diag_lsb)
    @rtc_low_power_diag.setter
    def rtc_low_power_diag(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_low_power_diag_msb, self.__rtc_low_power_diag_lsb, value)
class RTC_CPU_RAM_FORCE_ISO(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x58
        self.__reg_cpu_ram_force_iso_lsb = 0
        self.__reg_cpu_ram_force_iso_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_cpu_ram_force_iso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cpu_ram_force_iso_msb, self.__reg_cpu_ram_force_iso_lsb)
    @reg_cpu_ram_force_iso.setter
    def reg_cpu_ram_force_iso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cpu_ram_force_iso_msb, self.__reg_cpu_ram_force_iso_lsb, value)
class RTC_CPU_RAM_FORCE_NOISO(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x5c
        self.__reg_cpu_ram_force_noiso_lsb = 0
        self.__reg_cpu_ram_force_noiso_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_cpu_ram_force_noiso(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cpu_ram_force_noiso_msb, self.__reg_cpu_ram_force_noiso_lsb)
    @reg_cpu_ram_force_noiso.setter
    def reg_cpu_ram_force_noiso(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cpu_ram_force_noiso_msb, self.__reg_cpu_ram_force_noiso_lsb, value)
class RTC_CPU_RAM_FORCE_PU(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x60
        self.__reg_cpu_ram_force_pu_lsb = 0
        self.__reg_cpu_ram_force_pu_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_cpu_ram_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cpu_ram_force_pu_msb, self.__reg_cpu_ram_force_pu_lsb)
    @reg_cpu_ram_force_pu.setter
    def reg_cpu_ram_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cpu_ram_force_pu_msb, self.__reg_cpu_ram_force_pu_lsb, value)
class RTC_XTAL_EXT_CTR(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x64
        self.__reg_xtl_ext_ctr_en_lsb = 1
        self.__reg_xtl_ext_ctr_en_msb = 1
        self.__reg_xtl_ext_ctr_lv_lsb = 0
        self.__reg_xtl_ext_ctr_lv_msb = 0
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
class RTC_GPIO_OUT_DATA(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x68
        self.__rtc_gpio_out_data_lsb = 0
        self.__rtc_gpio_out_data_msb = 1
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
class RTC_GPIO_ENABLE(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x74
        self.__reg_rtc_gpio_enable_lsb = 0
        self.__reg_rtc_gpio_enable_msb = 1
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
class RTC_GPIO_STATUS_INT(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x80
        self.__rtc_gpio_status_int_lsb = 0
        self.__rtc_gpio_status_int_msb = 1
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
class RTC_GPIO_IN_SYNC(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x8c
        self.__rtc_gpio1_in_sync_1_lsb = 1
        self.__rtc_gpio1_in_sync_1_msb = 1
        self.__rtc_gpio0_in_sync_1_lsb = 0
        self.__rtc_gpio0_in_sync_1_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_gpio1_in_sync_1(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_gpio1_in_sync_1_msb, self.__rtc_gpio1_in_sync_1_lsb)
    @rtc_gpio1_in_sync_1.setter
    def rtc_gpio1_in_sync_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_gpio1_in_sync_1_msb, self.__rtc_gpio1_in_sync_1_lsb, value)

    @property
    def rtc_gpio0_in_sync_1(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_gpio0_in_sync_1_msb, self.__rtc_gpio0_in_sync_1_lsb)
    @rtc_gpio0_in_sync_1.setter
    def rtc_gpio0_in_sync_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_gpio0_in_sync_1_msb, self.__rtc_gpio0_in_sync_1_lsb, value)
class RTC_GPIO_INT_TYPE(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x90
        self.__reg_rtc_gpio1_int_type_lsb = 8
        self.__reg_rtc_gpio1_int_type_msb = 10
        self.__reg_rtc_gpio0_int_type_lsb = 4
        self.__reg_rtc_gpio0_int_type_msb = 6
        self.__reg_rtc_gpio_pad_driver_lsb = 0
        self.__reg_rtc_gpio_pad_driver_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rtc_gpio1_int_type(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_gpio1_int_type_msb, self.__reg_rtc_gpio1_int_type_lsb)
    @reg_rtc_gpio1_int_type.setter
    def reg_rtc_gpio1_int_type(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_gpio1_int_type_msb, self.__reg_rtc_gpio1_int_type_lsb, value)

    @property
    def reg_rtc_gpio0_int_type(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_gpio0_int_type_msb, self.__reg_rtc_gpio0_int_type_lsb)
    @reg_rtc_gpio0_int_type.setter
    def reg_rtc_gpio0_int_type(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_gpio0_int_type_msb, self.__reg_rtc_gpio0_int_type_lsb, value)

    @property
    def reg_rtc_gpio_pad_driver(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_gpio_pad_driver_msb, self.__reg_rtc_gpio_pad_driver_lsb)
    @reg_rtc_gpio_pad_driver.setter
    def reg_rtc_gpio_pad_driver(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_gpio_pad_driver_msb, self.__reg_rtc_gpio_pad_driver_lsb, value)
class RTC_GPIO_WAKEUP(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x94
        self.__reg_rtc_gpio1_wakeup_lv_lsb = 3
        self.__reg_rtc_gpio1_wakeup_lv_msb = 3
        self.__reg_rtc_gpio1_wakeup_en_lsb = 2
        self.__reg_rtc_gpio1_wakeup_en_msb = 2
        self.__reg_rtc_gpio0_wakeup_lv_lsb = 1
        self.__reg_rtc_gpio0_wakeup_lv_msb = 1
        self.__reg_rtc_gpio0_wakeup_en_lsb = 0
        self.__reg_rtc_gpio0_wakeup_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rtc_gpio1_wakeup_lv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_gpio1_wakeup_lv_msb, self.__reg_rtc_gpio1_wakeup_lv_lsb)
    @reg_rtc_gpio1_wakeup_lv.setter
    def reg_rtc_gpio1_wakeup_lv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_gpio1_wakeup_lv_msb, self.__reg_rtc_gpio1_wakeup_lv_lsb, value)

    @property
    def reg_rtc_gpio1_wakeup_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_gpio1_wakeup_en_msb, self.__reg_rtc_gpio1_wakeup_en_lsb)
    @reg_rtc_gpio1_wakeup_en.setter
    def reg_rtc_gpio1_wakeup_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_gpio1_wakeup_en_msb, self.__reg_rtc_gpio1_wakeup_en_lsb, value)

    @property
    def reg_rtc_gpio0_wakeup_lv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_gpio0_wakeup_lv_msb, self.__reg_rtc_gpio0_wakeup_lv_lsb)
    @reg_rtc_gpio0_wakeup_lv.setter
    def reg_rtc_gpio0_wakeup_lv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_gpio0_wakeup_lv_msb, self.__reg_rtc_gpio0_wakeup_lv_lsb, value)

    @property
    def reg_rtc_gpio0_wakeup_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtc_gpio0_wakeup_en_msb, self.__reg_rtc_gpio0_wakeup_en_lsb)
    @reg_rtc_gpio0_wakeup_en.setter
    def reg_rtc_gpio0_wakeup_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtc_gpio0_wakeup_en_msb, self.__reg_rtc_gpio0_wakeup_en_lsb, value)
class RTC_EXT_WAKEUP(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x98
        self.__reg_ext_wakeup1_lv_lsb = 1
        self.__reg_ext_wakeup1_lv_msb = 1
        self.__reg_ext_wakeup0_lv_lsb = 0
        self.__reg_ext_wakeup0_lv_msb = 0
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
class RTC_DEBUG_SEL(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0x9c
        self.__reg_rtc_debug_sel1_lsb = 8
        self.__reg_rtc_debug_sel1_msb = 12
        self.__reg_rtc_debug_sel0_lsb = 0
        self.__reg_rtc_debug_sel0_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

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
class RTC_PAD_XPD_DCDC(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0xa0
        self.__reg_pad_xpd_dcdc_sel_2_lsb = 6
        self.__reg_pad_xpd_dcdc_sel_2_msb = 6
        self.__reg_pad_xpd_dcdc_slp_pd_lsb = 5
        self.__reg_pad_xpd_dcdc_slp_pd_msb = 5
        self.__reg_pad_xpd_dcdc_slp_pu_lsb = 4
        self.__reg_pad_xpd_dcdc_slp_pu_msb = 4
        self.__reg_pad_xpd_dcdc_fuc_pd_lsb = 3
        self.__reg_pad_xpd_dcdc_fuc_pd_msb = 3
        self.__reg_pad_xpd_dcdc_fuc_pu_lsb = 2
        self.__reg_pad_xpd_dcdc_fuc_pu_msb = 2
        self.__reg_pad_xpd_dcdc_sel_lsb = 0
        self.__reg_pad_xpd_dcdc_sel_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_pad_xpd_dcdc_sel_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pad_xpd_dcdc_sel_2_msb, self.__reg_pad_xpd_dcdc_sel_2_lsb)
    @reg_pad_xpd_dcdc_sel_2.setter
    def reg_pad_xpd_dcdc_sel_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pad_xpd_dcdc_sel_2_msb, self.__reg_pad_xpd_dcdc_sel_2_lsb, value)

    @property
    def reg_pad_xpd_dcdc_slp_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pad_xpd_dcdc_slp_pd_msb, self.__reg_pad_xpd_dcdc_slp_pd_lsb)
    @reg_pad_xpd_dcdc_slp_pd.setter
    def reg_pad_xpd_dcdc_slp_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pad_xpd_dcdc_slp_pd_msb, self.__reg_pad_xpd_dcdc_slp_pd_lsb, value)

    @property
    def reg_pad_xpd_dcdc_slp_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pad_xpd_dcdc_slp_pu_msb, self.__reg_pad_xpd_dcdc_slp_pu_lsb)
    @reg_pad_xpd_dcdc_slp_pu.setter
    def reg_pad_xpd_dcdc_slp_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pad_xpd_dcdc_slp_pu_msb, self.__reg_pad_xpd_dcdc_slp_pu_lsb, value)

    @property
    def reg_pad_xpd_dcdc_fuc_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pad_xpd_dcdc_fuc_pd_msb, self.__reg_pad_xpd_dcdc_fuc_pd_lsb)
    @reg_pad_xpd_dcdc_fuc_pd.setter
    def reg_pad_xpd_dcdc_fuc_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pad_xpd_dcdc_fuc_pd_msb, self.__reg_pad_xpd_dcdc_fuc_pd_lsb, value)

    @property
    def reg_pad_xpd_dcdc_fuc_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pad_xpd_dcdc_fuc_pu_msb, self.__reg_pad_xpd_dcdc_fuc_pu_lsb)
    @reg_pad_xpd_dcdc_fuc_pu.setter
    def reg_pad_xpd_dcdc_fuc_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pad_xpd_dcdc_fuc_pu_msb, self.__reg_pad_xpd_dcdc_fuc_pu_lsb, value)

    @property
    def reg_pad_xpd_dcdc_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pad_xpd_dcdc_sel_msb, self.__reg_pad_xpd_dcdc_sel_lsb)
    @reg_pad_xpd_dcdc_sel.setter
    def reg_pad_xpd_dcdc_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pad_xpd_dcdc_sel_msb, self.__reg_pad_xpd_dcdc_sel_lsb, value)
class RTC_REMAIN2(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0xa4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)
class RTC_SLP_REJECT(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0xa8
        self.__reject_cause_lsb = 8
        self.__reject_cause_msb = 11
        self.__reg_rtcclk_en_lsb = 2
        self.__reg_rtcclk_en_msb = 2
        self.__reg_deep_slp_reject_en_lsb = 1
        self.__reg_deep_slp_reject_en_msb = 1
        self.__reg_light_slp_reject_en_lsb = 0
        self.__reg_light_slp_reject_en_msb = 0
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
    def reg_rtcclk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rtcclk_en_msb, self.__reg_rtcclk_en_lsb)
    @reg_rtcclk_en.setter
    def reg_rtcclk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rtcclk_en_msb, self.__reg_rtcclk_en_lsb, value)

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
class RTC_CPU_RAM_FORCE_PD(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0xac
        self.__reg_cpu_ram_force_pd_lsb = 0
        self.__reg_cpu_ram_force_pd_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_cpu_ram_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cpu_ram_force_pd_msb, self.__reg_cpu_ram_force_pd_lsb)
    @reg_cpu_ram_force_pd.setter
    def reg_cpu_ram_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cpu_ram_force_pd_msb, self.__reg_cpu_ram_force_pd_lsb, value)
class RTC_FORCE_PD(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0xb0
        self.__reg_bg_force_pd_lsb = 6
        self.__reg_bg_force_pd_msb = 6
        self.__reg_xtl_force_pd_lsb = 5
        self.__reg_xtl_force_pd_msb = 5
        self.__reg_pll_force_pd_lsb = 4
        self.__reg_pll_force_pd_msb = 4
        self.__reg_bb_force_pd_lsb = 3
        self.__reg_bb_force_pd_msb = 3
        self.__reg_soc_pad_force_pd_lsb = 1
        self.__reg_soc_pad_force_pd_msb = 1
        self.__reg_DRam1_force_pd_lsb = 0
        self.__reg_DRam1_force_pd_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bg_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bg_force_pd_msb, self.__reg_bg_force_pd_lsb)
    @reg_bg_force_pd.setter
    def reg_bg_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bg_force_pd_msb, self.__reg_bg_force_pd_lsb, value)

    @property
    def reg_xtl_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xtl_force_pd_msb, self.__reg_xtl_force_pd_lsb)
    @reg_xtl_force_pd.setter
    def reg_xtl_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xtl_force_pd_msb, self.__reg_xtl_force_pd_lsb, value)

    @property
    def reg_pll_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pll_force_pd_msb, self.__reg_pll_force_pd_lsb)
    @reg_pll_force_pd.setter
    def reg_pll_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pll_force_pd_msb, self.__reg_pll_force_pd_lsb, value)

    @property
    def reg_bb_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_force_pd_msb, self.__reg_bb_force_pd_lsb)
    @reg_bb_force_pd.setter
    def reg_bb_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_force_pd_msb, self.__reg_bb_force_pd_lsb, value)

    @property
    def reg_soc_pad_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_soc_pad_force_pd_msb, self.__reg_soc_pad_force_pd_lsb)
    @reg_soc_pad_force_pd.setter
    def reg_soc_pad_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_soc_pad_force_pd_msb, self.__reg_soc_pad_force_pd_lsb, value)

    @property
    def reg_DRam1_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_DRam1_force_pd_msb, self.__reg_DRam1_force_pd_lsb)
    @reg_DRam1_force_pd.setter
    def reg_DRam1_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_DRam1_force_pd_msb, self.__reg_DRam1_force_pd_lsb, value)
class RTC_CPU_PERIOD_SEL(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0xb4
        self.__reg_rtc_cpuperiod_sel_lsb = 1
        self.__reg_rtc_cpuperiod_sel_msb = 1
        self.__reg_rtc_cpusel_conf_lsb = 0
        self.__reg_rtc_cpusel_conf_msb = 0
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
class RTC_SDIO_ACT_DNUM(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = RTC_BASE + 0xbc
        self.__reg_sdio_act_dnum_lsb = 0
        self.__reg_sdio_act_dnum_msb = 9
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
