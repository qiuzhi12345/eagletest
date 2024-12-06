from hal.common import *
from hal.hwregister.hwreg.ESP32.addr_base import *
class APB_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.APB_CTRL_SYSCLK_CONF = APB_CTRL_SYSCLK_CONF(self.channel, self.chipv)
        self.APB_CTRL_XTAL_TICK_CONF = APB_CTRL_XTAL_TICK_CONF(self.channel, self.chipv)
        self.APB_CTRL_PLL_TICK_CONF = APB_CTRL_PLL_TICK_CONF(self.channel, self.chipv)
        self.APB_CTRL_CK8M_TICK_CONF = APB_CTRL_CK8M_TICK_CONF(self.channel, self.chipv)
        self.APB_SARADC_CTRL = APB_SARADC_CTRL(self.channel, self.chipv)
        self.APB_SARADC_CTRL2 = APB_SARADC_CTRL2(self.channel, self.chipv)
        self.APB_SARADC_FSM = APB_SARADC_FSM(self.channel, self.chipv)
        self.APB_SARADC_SAR1_PATT_TAB1 = APB_SARADC_SAR1_PATT_TAB1(self.channel, self.chipv)
        self.APB_SARADC_SAR1_PATT_TAB2 = APB_SARADC_SAR1_PATT_TAB2(self.channel, self.chipv)
        self.APB_SARADC_SAR1_PATT_TAB3 = APB_SARADC_SAR1_PATT_TAB3(self.channel, self.chipv)
        self.APB_SARADC_SAR1_PATT_TAB4 = APB_SARADC_SAR1_PATT_TAB4(self.channel, self.chipv)
        self.APB_SARADC_SAR2_PATT_TAB1 = APB_SARADC_SAR2_PATT_TAB1(self.channel, self.chipv)
        self.APB_SARADC_SAR2_PATT_TAB2 = APB_SARADC_SAR2_PATT_TAB2(self.channel, self.chipv)
        self.APB_SARADC_SAR2_PATT_TAB3 = APB_SARADC_SAR2_PATT_TAB3(self.channel, self.chipv)
        self.APB_SARADC_SAR2_PATT_TAB4 = APB_SARADC_SAR2_PATT_TAB4(self.channel, self.chipv)
        self.APB_CTRL_APLL_TICK_CONF = APB_CTRL_APLL_TICK_CONF(self.channel, self.chipv)
        self.APB_CTRL_DATE = APB_CTRL_DATE(self.channel, self.chipv)
class APB_CTRL_SYSCLK_CONF(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x0
        self.__apb_ctrl_quick_clk_chng_lsb = 13
        self.__apb_ctrl_quick_clk_chng_msb = 13
        self.__apb_ctrl_rst_tick_cnt_lsb = 12
        self.__apb_ctrl_rst_tick_cnt_msb = 12
        self.__reg_clk_en_lsb = 11
        self.__reg_clk_en_msb = 11
        self.__apb_ctrl_clk_320m_en_lsb = 10
        self.__apb_ctrl_clk_320m_en_msb = 10
        self.__apb_ctrl_pre_div_cnt_lsb = 0
        self.__apb_ctrl_pre_div_cnt_msb = 9
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def apb_ctrl_quick_clk_chng(self):
        return self.__MEM.rdm(self.__addr, self.__apb_ctrl_quick_clk_chng_msb, self.__apb_ctrl_quick_clk_chng_lsb)
    @apb_ctrl_quick_clk_chng.setter
    def apb_ctrl_quick_clk_chng(self, value):
        return self.__MEM.wrm(self.__addr, self.__apb_ctrl_quick_clk_chng_msb, self.__apb_ctrl_quick_clk_chng_lsb, value)

    @property
    def apb_ctrl_rst_tick_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__apb_ctrl_rst_tick_cnt_msb, self.__apb_ctrl_rst_tick_cnt_lsb)
    @apb_ctrl_rst_tick_cnt.setter
    def apb_ctrl_rst_tick_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__apb_ctrl_rst_tick_cnt_msb, self.__apb_ctrl_rst_tick_cnt_lsb, value)

    @property
    def reg_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk_en_msb, self.__reg_clk_en_lsb)
    @reg_clk_en.setter
    def reg_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk_en_msb, self.__reg_clk_en_lsb, value)

    @property
    def apb_ctrl_clk_320m_en(self):
        return self.__MEM.rdm(self.__addr, self.__apb_ctrl_clk_320m_en_msb, self.__apb_ctrl_clk_320m_en_lsb)
    @apb_ctrl_clk_320m_en.setter
    def apb_ctrl_clk_320m_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__apb_ctrl_clk_320m_en_msb, self.__apb_ctrl_clk_320m_en_lsb, value)

    @property
    def apb_ctrl_pre_div_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__apb_ctrl_pre_div_cnt_msb, self.__apb_ctrl_pre_div_cnt_lsb)
    @apb_ctrl_pre_div_cnt.setter
    def apb_ctrl_pre_div_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__apb_ctrl_pre_div_cnt_msb, self.__apb_ctrl_pre_div_cnt_lsb, value)
class APB_CTRL_XTAL_TICK_CONF(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x4
        self.__apb_ctrl_xtal_tick_num_lsb = 0
        self.__apb_ctrl_xtal_tick_num_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def apb_ctrl_xtal_tick_num(self):
        return self.__MEM.rdm(self.__addr, self.__apb_ctrl_xtal_tick_num_msb, self.__apb_ctrl_xtal_tick_num_lsb)
    @apb_ctrl_xtal_tick_num.setter
    def apb_ctrl_xtal_tick_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__apb_ctrl_xtal_tick_num_msb, self.__apb_ctrl_xtal_tick_num_lsb, value)
class APB_CTRL_PLL_TICK_CONF(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x8
        self.__apb_ctrl_pll_tick_num_lsb = 0
        self.__apb_ctrl_pll_tick_num_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def apb_ctrl_pll_tick_num(self):
        return self.__MEM.rdm(self.__addr, self.__apb_ctrl_pll_tick_num_msb, self.__apb_ctrl_pll_tick_num_lsb)
    @apb_ctrl_pll_tick_num.setter
    def apb_ctrl_pll_tick_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__apb_ctrl_pll_tick_num_msb, self.__apb_ctrl_pll_tick_num_lsb, value)
class APB_CTRL_CK8M_TICK_CONF(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0xc
        self.__apb_ctrl_ck8m_tick_num_lsb = 0
        self.__apb_ctrl_ck8m_tick_num_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def apb_ctrl_ck8m_tick_num(self):
        return self.__MEM.rdm(self.__addr, self.__apb_ctrl_ck8m_tick_num_msb, self.__apb_ctrl_ck8m_tick_num_lsb)
    @apb_ctrl_ck8m_tick_num.setter
    def apb_ctrl_ck8m_tick_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__apb_ctrl_ck8m_tick_num_msb, self.__apb_ctrl_ck8m_tick_num_lsb, value)
class APB_SARADC_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x10
        self.__reg_saradc_data_to_i2s_lsb = 26
        self.__reg_saradc_data_to_i2s_msb = 26
        self.__reg_saradc_data_sar_sel_lsb = 25
        self.__reg_saradc_data_sar_sel_msb = 25
        self.__reg_saradc_sar2_patt_p_clear_lsb = 24
        self.__reg_saradc_sar2_patt_p_clear_msb = 24
        self.__reg_saradc_sar1_patt_p_clear_lsb = 23
        self.__reg_saradc_sar1_patt_p_clear_msb = 23
        self.__reg_saradc_sar2_patt_len_lsb = 19
        self.__reg_saradc_sar2_patt_len_msb = 22
        self.__reg_saradc_sar1_patt_len_lsb = 15
        self.__reg_saradc_sar1_patt_len_msb = 18
        self.__reg_saradc_sar_clk_div_lsb = 7
        self.__reg_saradc_sar_clk_div_msb = 14
        self.__reg_saradc_sar_clk_gated_lsb = 6
        self.__reg_saradc_sar_clk_gated_msb = 6
        self.__reg_saradc_sar_sel_lsb = 5
        self.__reg_saradc_sar_sel_msb = 5
        self.__reg_saradc_work_mode_lsb = 3
        self.__reg_saradc_work_mode_msb = 4
        self.__reg_saradc_sar2_mux_lsb = 2
        self.__reg_saradc_sar2_mux_msb = 2
        self.__reg_saradc_start_lsb = 1
        self.__reg_saradc_start_msb = 1
        self.__reg_saradc_start_force_lsb = 0
        self.__reg_saradc_start_force_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_saradc_data_to_i2s(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_data_to_i2s_msb, self.__reg_saradc_data_to_i2s_lsb)
    @reg_saradc_data_to_i2s.setter
    def reg_saradc_data_to_i2s(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_data_to_i2s_msb, self.__reg_saradc_data_to_i2s_lsb, value)

    @property
    def reg_saradc_data_sar_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_data_sar_sel_msb, self.__reg_saradc_data_sar_sel_lsb)
    @reg_saradc_data_sar_sel.setter
    def reg_saradc_data_sar_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_data_sar_sel_msb, self.__reg_saradc_data_sar_sel_lsb, value)

    @property
    def reg_saradc_sar2_patt_p_clear(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_sar2_patt_p_clear_msb, self.__reg_saradc_sar2_patt_p_clear_lsb)
    @reg_saradc_sar2_patt_p_clear.setter
    def reg_saradc_sar2_patt_p_clear(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_sar2_patt_p_clear_msb, self.__reg_saradc_sar2_patt_p_clear_lsb, value)

    @property
    def reg_saradc_sar1_patt_p_clear(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_sar1_patt_p_clear_msb, self.__reg_saradc_sar1_patt_p_clear_lsb)
    @reg_saradc_sar1_patt_p_clear.setter
    def reg_saradc_sar1_patt_p_clear(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_sar1_patt_p_clear_msb, self.__reg_saradc_sar1_patt_p_clear_lsb, value)

    @property
    def reg_saradc_sar2_patt_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_sar2_patt_len_msb, self.__reg_saradc_sar2_patt_len_lsb)
    @reg_saradc_sar2_patt_len.setter
    def reg_saradc_sar2_patt_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_sar2_patt_len_msb, self.__reg_saradc_sar2_patt_len_lsb, value)

    @property
    def reg_saradc_sar1_patt_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_sar1_patt_len_msb, self.__reg_saradc_sar1_patt_len_lsb)
    @reg_saradc_sar1_patt_len.setter
    def reg_saradc_sar1_patt_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_sar1_patt_len_msb, self.__reg_saradc_sar1_patt_len_lsb, value)

    @property
    def reg_saradc_sar_clk_div(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_sar_clk_div_msb, self.__reg_saradc_sar_clk_div_lsb)
    @reg_saradc_sar_clk_div.setter
    def reg_saradc_sar_clk_div(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_sar_clk_div_msb, self.__reg_saradc_sar_clk_div_lsb, value)

    @property
    def reg_saradc_sar_clk_gated(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_sar_clk_gated_msb, self.__reg_saradc_sar_clk_gated_lsb)
    @reg_saradc_sar_clk_gated.setter
    def reg_saradc_sar_clk_gated(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_sar_clk_gated_msb, self.__reg_saradc_sar_clk_gated_lsb, value)

    @property
    def reg_saradc_sar_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_sar_sel_msb, self.__reg_saradc_sar_sel_lsb)
    @reg_saradc_sar_sel.setter
    def reg_saradc_sar_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_sar_sel_msb, self.__reg_saradc_sar_sel_lsb, value)

    @property
    def reg_saradc_work_mode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_work_mode_msb, self.__reg_saradc_work_mode_lsb)
    @reg_saradc_work_mode.setter
    def reg_saradc_work_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_work_mode_msb, self.__reg_saradc_work_mode_lsb, value)

    @property
    def reg_saradc_sar2_mux(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_sar2_mux_msb, self.__reg_saradc_sar2_mux_lsb)
    @reg_saradc_sar2_mux.setter
    def reg_saradc_sar2_mux(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_sar2_mux_msb, self.__reg_saradc_sar2_mux_lsb, value)

    @property
    def reg_saradc_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_start_msb, self.__reg_saradc_start_lsb)
    @reg_saradc_start.setter
    def reg_saradc_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_start_msb, self.__reg_saradc_start_lsb, value)

    @property
    def reg_saradc_start_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_start_force_msb, self.__reg_saradc_start_force_lsb)
    @reg_saradc_start_force.setter
    def reg_saradc_start_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_start_force_msb, self.__reg_saradc_start_force_lsb, value)
class APB_SARADC_CTRL2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x14
        self.__reg_saradc_sar2_inv_lsb = 10
        self.__reg_saradc_sar2_inv_msb = 10
        self.__reg_saradc_sar1_inv_lsb = 9
        self.__reg_saradc_sar1_inv_msb = 9
        self.__reg_saradc_max_meas_num_lsb = 1
        self.__reg_saradc_max_meas_num_msb = 8
        self.__reg_saradc_meas_num_limit_lsb = 0
        self.__reg_saradc_meas_num_limit_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_saradc_sar2_inv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_sar2_inv_msb, self.__reg_saradc_sar2_inv_lsb)
    @reg_saradc_sar2_inv.setter
    def reg_saradc_sar2_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_sar2_inv_msb, self.__reg_saradc_sar2_inv_lsb, value)

    @property
    def reg_saradc_sar1_inv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_sar1_inv_msb, self.__reg_saradc_sar1_inv_lsb)
    @reg_saradc_sar1_inv.setter
    def reg_saradc_sar1_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_sar1_inv_msb, self.__reg_saradc_sar1_inv_lsb, value)

    @property
    def reg_saradc_max_meas_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_max_meas_num_msb, self.__reg_saradc_max_meas_num_lsb)
    @reg_saradc_max_meas_num.setter
    def reg_saradc_max_meas_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_max_meas_num_msb, self.__reg_saradc_max_meas_num_lsb, value)

    @property
    def reg_saradc_meas_num_limit(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_meas_num_limit_msb, self.__reg_saradc_meas_num_limit_lsb)
    @reg_saradc_meas_num_limit.setter
    def reg_saradc_meas_num_limit(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_meas_num_limit_msb, self.__reg_saradc_meas_num_limit_lsb, value)
class APB_SARADC_FSM(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x18
        self.__reg_saradc_sample_cycle_lsb = 24
        self.__reg_saradc_sample_cycle_msb = 31
        self.__reg_saradc_start_wait_lsb = 16
        self.__reg_saradc_start_wait_msb = 23
        self.__reg_saradc_standby_wait_lsb = 8
        self.__reg_saradc_standby_wait_msb = 15
        self.__reg_saradc_rstb_wait_lsb = 0
        self.__reg_saradc_rstb_wait_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_saradc_sample_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_sample_cycle_msb, self.__reg_saradc_sample_cycle_lsb)
    @reg_saradc_sample_cycle.setter
    def reg_saradc_sample_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_sample_cycle_msb, self.__reg_saradc_sample_cycle_lsb, value)

    @property
    def reg_saradc_start_wait(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_start_wait_msb, self.__reg_saradc_start_wait_lsb)
    @reg_saradc_start_wait.setter
    def reg_saradc_start_wait(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_start_wait_msb, self.__reg_saradc_start_wait_lsb, value)

    @property
    def reg_saradc_standby_wait(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_standby_wait_msb, self.__reg_saradc_standby_wait_lsb)
    @reg_saradc_standby_wait.setter
    def reg_saradc_standby_wait(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_standby_wait_msb, self.__reg_saradc_standby_wait_lsb, value)

    @property
    def reg_saradc_rstb_wait(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_rstb_wait_msb, self.__reg_saradc_rstb_wait_lsb)
    @reg_saradc_rstb_wait.setter
    def reg_saradc_rstb_wait(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_rstb_wait_msb, self.__reg_saradc_rstb_wait_lsb, value)
class APB_SARADC_SAR1_PATT_TAB1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x1c
        self.__reg_saradc_sar1_patt_tab1_lsb = 0
        self.__reg_saradc_sar1_patt_tab1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_saradc_sar1_patt_tab1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_sar1_patt_tab1_msb, self.__reg_saradc_sar1_patt_tab1_lsb)
    @reg_saradc_sar1_patt_tab1.setter
    def reg_saradc_sar1_patt_tab1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_sar1_patt_tab1_msb, self.__reg_saradc_sar1_patt_tab1_lsb, value)
class APB_SARADC_SAR1_PATT_TAB2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x20
        self.__reg_saradc_sar1_patt_tab2_lsb = 0
        self.__reg_saradc_sar1_patt_tab2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_saradc_sar1_patt_tab2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_sar1_patt_tab2_msb, self.__reg_saradc_sar1_patt_tab2_lsb)
    @reg_saradc_sar1_patt_tab2.setter
    def reg_saradc_sar1_patt_tab2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_sar1_patt_tab2_msb, self.__reg_saradc_sar1_patt_tab2_lsb, value)
class APB_SARADC_SAR1_PATT_TAB3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x24
        self.__reg_saradc_sar1_patt_tab3_lsb = 0
        self.__reg_saradc_sar1_patt_tab3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_saradc_sar1_patt_tab3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_sar1_patt_tab3_msb, self.__reg_saradc_sar1_patt_tab3_lsb)
    @reg_saradc_sar1_patt_tab3.setter
    def reg_saradc_sar1_patt_tab3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_sar1_patt_tab3_msb, self.__reg_saradc_sar1_patt_tab3_lsb, value)
class APB_SARADC_SAR1_PATT_TAB4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x28
        self.__reg_saradc_sar1_patt_tab4_lsb = 0
        self.__reg_saradc_sar1_patt_tab4_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_saradc_sar1_patt_tab4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_sar1_patt_tab4_msb, self.__reg_saradc_sar1_patt_tab4_lsb)
    @reg_saradc_sar1_patt_tab4.setter
    def reg_saradc_sar1_patt_tab4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_sar1_patt_tab4_msb, self.__reg_saradc_sar1_patt_tab4_lsb, value)
class APB_SARADC_SAR2_PATT_TAB1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x2c
        self.__reg_saradc_sar2_patt_tab1_lsb = 0
        self.__reg_saradc_sar2_patt_tab1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_saradc_sar2_patt_tab1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_sar2_patt_tab1_msb, self.__reg_saradc_sar2_patt_tab1_lsb)
    @reg_saradc_sar2_patt_tab1.setter
    def reg_saradc_sar2_patt_tab1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_sar2_patt_tab1_msb, self.__reg_saradc_sar2_patt_tab1_lsb, value)
class APB_SARADC_SAR2_PATT_TAB2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x30
        self.__reg_saradc_sar2_patt_tab2_lsb = 0
        self.__reg_saradc_sar2_patt_tab2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_saradc_sar2_patt_tab2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_sar2_patt_tab2_msb, self.__reg_saradc_sar2_patt_tab2_lsb)
    @reg_saradc_sar2_patt_tab2.setter
    def reg_saradc_sar2_patt_tab2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_sar2_patt_tab2_msb, self.__reg_saradc_sar2_patt_tab2_lsb, value)
class APB_SARADC_SAR2_PATT_TAB3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x34
        self.__reg_saradc_sar2_patt_tab3_lsb = 0
        self.__reg_saradc_sar2_patt_tab3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_saradc_sar2_patt_tab3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_sar2_patt_tab3_msb, self.__reg_saradc_sar2_patt_tab3_lsb)
    @reg_saradc_sar2_patt_tab3.setter
    def reg_saradc_sar2_patt_tab3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_sar2_patt_tab3_msb, self.__reg_saradc_sar2_patt_tab3_lsb, value)
class APB_SARADC_SAR2_PATT_TAB4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x38
        self.__reg_saradc_sar2_patt_tab4_lsb = 0
        self.__reg_saradc_sar2_patt_tab4_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_saradc_sar2_patt_tab4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_sar2_patt_tab4_msb, self.__reg_saradc_sar2_patt_tab4_lsb)
    @reg_saradc_sar2_patt_tab4.setter
    def reg_saradc_sar2_patt_tab4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_sar2_patt_tab4_msb, self.__reg_saradc_sar2_patt_tab4_lsb, value)
class APB_CTRL_APLL_TICK_CONF(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x3c
        self.__apb_ctrl_apll_tick_num_lsb = 0
        self.__apb_ctrl_apll_tick_num_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def apb_ctrl_apll_tick_num(self):
        return self.__MEM.rdm(self.__addr, self.__apb_ctrl_apll_tick_num_msb, self.__apb_ctrl_apll_tick_num_lsb)
    @apb_ctrl_apll_tick_num.setter
    def apb_ctrl_apll_tick_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__apb_ctrl_apll_tick_num_msb, self.__apb_ctrl_apll_tick_num_lsb, value)
class APB_CTRL_DATE(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x7c
        self.__apb_ctrl_date_lsb = 0
        self.__apb_ctrl_date_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def apb_ctrl_date(self):
        return self.__MEM.rdm(self.__addr, self.__apb_ctrl_date_msb, self.__apb_ctrl_date_lsb)
    @apb_ctrl_date.setter
    def apb_ctrl_date(self, value):
        return self.__MEM.wrm(self.__addr, self.__apb_ctrl_date_msb, self.__apb_ctrl_date_lsb, value)
    @property
    def default_value(self):
        return 0x16042000 
