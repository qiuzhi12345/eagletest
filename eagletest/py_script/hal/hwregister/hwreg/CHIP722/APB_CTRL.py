from hal.common import *
from hal.hwregister.hwreg.CHIP722.addr_base import *
class APB_CTRL(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.APB_CTRL_SYSCLK_CONF = APB_CTRL_SYSCLK_CONF(self.channel, self.chipv)
        self.APB_CTRL_TICK_CONF = APB_CTRL_TICK_CONF(self.channel, self.chipv)
        self.APB_SARADC_CTRL = APB_SARADC_CTRL(self.channel, self.chipv)
        self.APB_SARADC_CTRL2 = APB_SARADC_CTRL2(self.channel, self.chipv)
        self.APB_SARADC_FSM = APB_SARADC_FSM(self.channel, self.chipv)
        self.APB_SARADC_FSM_WAIT = APB_SARADC_FSM_WAIT(self.channel, self.chipv)
        self.APB_SARADC_SAR1_STATUS = APB_SARADC_SAR1_STATUS(self.channel, self.chipv)
        self.APB_SARADC_SAR2_STATUS = APB_SARADC_SAR2_STATUS(self.channel, self.chipv)
        self.APB_SARADC_SAR1_PATT_TAB1 = APB_SARADC_SAR1_PATT_TAB1(self.channel, self.chipv)
        self.APB_SARADC_SAR1_PATT_TAB2 = APB_SARADC_SAR1_PATT_TAB2(self.channel, self.chipv)
        self.APB_SARADC_SAR1_PATT_TAB3 = APB_SARADC_SAR1_PATT_TAB3(self.channel, self.chipv)
        self.APB_SARADC_SAR1_PATT_TAB4 = APB_SARADC_SAR1_PATT_TAB4(self.channel, self.chipv)
        self.APB_SARADC_SAR2_PATT_TAB1 = APB_SARADC_SAR2_PATT_TAB1(self.channel, self.chipv)
        self.APB_SARADC_SAR2_PATT_TAB2 = APB_SARADC_SAR2_PATT_TAB2(self.channel, self.chipv)
        self.APB_SARADC_SAR2_PATT_TAB3 = APB_SARADC_SAR2_PATT_TAB3(self.channel, self.chipv)
        self.APB_SARADC_SAR2_PATT_TAB4 = APB_SARADC_SAR2_PATT_TAB4(self.channel, self.chipv)
        self.APB_ADC_ARB_CTRL = APB_ADC_ARB_CTRL(self.channel, self.chipv)
        self.APB_CTRL_CLK_OUT_EN = APB_CTRL_CLK_OUT_EN(self.channel, self.chipv)
        self.HOST_INF_SEL = HOST_INF_SEL(self.channel, self.chipv)
        self.EXT_MEM_PMS_LOCK = EXT_MEM_PMS_LOCK(self.channel, self.chipv)
        self.FLASH_ACE0_ATTR = FLASH_ACE0_ATTR(self.channel, self.chipv)
        self.FLASH_ACE1_ATTR = FLASH_ACE1_ATTR(self.channel, self.chipv)
        self.FLASH_ACE2_ATTR = FLASH_ACE2_ATTR(self.channel, self.chipv)
        self.FLASH_ACE3_ATTR = FLASH_ACE3_ATTR(self.channel, self.chipv)
        self.FLASH_ACE0_ADDR = FLASH_ACE0_ADDR(self.channel, self.chipv)
        self.FLASH_ACE1_ADDR = FLASH_ACE1_ADDR(self.channel, self.chipv)
        self.FLASH_ACE2_ADDR = FLASH_ACE2_ADDR(self.channel, self.chipv)
        self.FLASH_ACE3_ADDR = FLASH_ACE3_ADDR(self.channel, self.chipv)
        self.FLASH_ACE0_SIZE = FLASH_ACE0_SIZE(self.channel, self.chipv)
        self.FLASH_ACE1_SIZE = FLASH_ACE1_SIZE(self.channel, self.chipv)
        self.FLASH_ACE2_SIZE = FLASH_ACE2_SIZE(self.channel, self.chipv)
        self.FLASH_ACE3_SIZE = FLASH_ACE3_SIZE(self.channel, self.chipv)
        self.SRAM_ACE0_ATTR = SRAM_ACE0_ATTR(self.channel, self.chipv)
        self.SRAM_ACE1_ATTR = SRAM_ACE1_ATTR(self.channel, self.chipv)
        self.SRAM_ACE2_ATTR = SRAM_ACE2_ATTR(self.channel, self.chipv)
        self.SRAM_ACE3_ATTR = SRAM_ACE3_ATTR(self.channel, self.chipv)
        self.SRAM_ACE0_ADDR = SRAM_ACE0_ADDR(self.channel, self.chipv)
        self.SRAM_ACE1_ADDR = SRAM_ACE1_ADDR(self.channel, self.chipv)
        self.SRAM_ACE2_ADDR = SRAM_ACE2_ADDR(self.channel, self.chipv)
        self.SRAM_ACE3_ADDR = SRAM_ACE3_ADDR(self.channel, self.chipv)
        self.SRAM_ACE0_SIZE = SRAM_ACE0_SIZE(self.channel, self.chipv)
        self.SRAM_ACE1_SIZE = SRAM_ACE1_SIZE(self.channel, self.chipv)
        self.SRAM_ACE2_SIZE = SRAM_ACE2_SIZE(self.channel, self.chipv)
        self.SRAM_ACE3_SIZE = SRAM_ACE3_SIZE(self.channel, self.chipv)
        self.SPI0_PMS_CTRL = SPI0_PMS_CTRL(self.channel, self.chipv)
        self.SPI0_REJECT_ADDR = SPI0_REJECT_ADDR(self.channel, self.chipv)
        self.SPI1_PMS_CTRL = SPI1_PMS_CTRL(self.channel, self.chipv)
        self.SPI1_REJECT_ADDR = SPI1_REJECT_ADDR(self.channel, self.chipv)
        self.APB_CTRL_SDIO_CTRL = APB_CTRL_SDIO_CTRL(self.channel, self.chipv)
        self.REDCY_SIG0_REG = REDCY_SIG0_REG(self.channel, self.chipv)
        self.REDCY_SIG1_REG = REDCY_SIG1_REG(self.channel, self.chipv)
        self.WIFI_BB_CFG = WIFI_BB_CFG(self.channel, self.chipv)
        self.WIFI_BB_CFG_2 = WIFI_BB_CFG_2(self.channel, self.chipv)
        self.WIFI_CLK_EN = WIFI_CLK_EN(self.channel, self.chipv)
        self.WIFI_RST_EN = WIFI_RST_EN(self.channel, self.chipv)
        self.FRONT_END_MEM_PD = FRONT_END_MEM_PD(self.channel, self.chipv)
        self.APB_CTRL_DATE = APB_CTRL_DATE(self.channel, self.chipv)
class APB_CTRL_SYSCLK_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x0
        self.__apb_ctrl_soc_clk_sel_lsb = 14
        self.__apb_ctrl_soc_clk_sel_msb = 15
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
    def apb_ctrl_soc_clk_sel(self):
        return self.__MEM.rdm(self.__addr, self.__apb_ctrl_soc_clk_sel_msb, self.__apb_ctrl_soc_clk_sel_lsb)
    @apb_ctrl_soc_clk_sel.setter
    def apb_ctrl_soc_clk_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__apb_ctrl_soc_clk_sel_msb, self.__apb_ctrl_soc_clk_sel_lsb, value)

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
class APB_CTRL_TICK_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x4
        self.__apb_ctrl_tick_enable_lsb = 16
        self.__apb_ctrl_tick_enable_msb = 16
        self.__apb_ctrl_ck8m_tick_num_lsb = 8
        self.__apb_ctrl_ck8m_tick_num_msb = 15
        self.__apb_ctrl_xtal_tick_num_lsb = 0
        self.__apb_ctrl_xtal_tick_num_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def apb_ctrl_tick_enable(self):
        return self.__MEM.rdm(self.__addr, self.__apb_ctrl_tick_enable_msb, self.__apb_ctrl_tick_enable_lsb)
    @apb_ctrl_tick_enable.setter
    def apb_ctrl_tick_enable(self, value):
        return self.__MEM.wrm(self.__addr, self.__apb_ctrl_tick_enable_msb, self.__apb_ctrl_tick_enable_lsb, value)

    @property
    def apb_ctrl_ck8m_tick_num(self):
        return self.__MEM.rdm(self.__addr, self.__apb_ctrl_ck8m_tick_num_msb, self.__apb_ctrl_ck8m_tick_num_lsb)
    @apb_ctrl_ck8m_tick_num.setter
    def apb_ctrl_ck8m_tick_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__apb_ctrl_ck8m_tick_num_msb, self.__apb_ctrl_ck8m_tick_num_lsb, value)

    @property
    def apb_ctrl_xtal_tick_num(self):
        return self.__MEM.rdm(self.__addr, self.__apb_ctrl_xtal_tick_num_msb, self.__apb_ctrl_xtal_tick_num_lsb)
    @apb_ctrl_xtal_tick_num.setter
    def apb_ctrl_xtal_tick_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__apb_ctrl_xtal_tick_num_msb, self.__apb_ctrl_xtal_tick_num_lsb, value)
class APB_SARADC_CTRL(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x8
        self.__reg_saradc_xpd_sar_force_lsb = 27
        self.__reg_saradc_xpd_sar_force_msb = 28
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
    def reg_saradc_xpd_sar_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_xpd_sar_force_msb, self.__reg_saradc_xpd_sar_force_lsb)
    @reg_saradc_xpd_sar_force.setter
    def reg_saradc_xpd_sar_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_xpd_sar_force_msb, self.__reg_saradc_xpd_sar_force_lsb, value)

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
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0xc
        self.__reg_saradc_timer_en_lsb = 20
        self.__reg_saradc_timer_en_msb = 20
        self.__reg_saradc_timer_target_lsb = 12
        self.__reg_saradc_timer_target_msb = 19
        self.__reg_saradc_timer_sel_lsb = 11
        self.__reg_saradc_timer_sel_msb = 11
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
    def reg_saradc_timer_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_timer_en_msb, self.__reg_saradc_timer_en_lsb)
    @reg_saradc_timer_en.setter
    def reg_saradc_timer_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_timer_en_msb, self.__reg_saradc_timer_en_lsb, value)

    @property
    def reg_saradc_timer_target(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_timer_target_msb, self.__reg_saradc_timer_target_lsb)
    @reg_saradc_timer_target.setter
    def reg_saradc_timer_target(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_timer_target_msb, self.__reg_saradc_timer_target_lsb, value)

    @property
    def reg_saradc_timer_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_timer_sel_msb, self.__reg_saradc_timer_sel_lsb)
    @reg_saradc_timer_sel.setter
    def reg_saradc_timer_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_timer_sel_msb, self.__reg_saradc_timer_sel_lsb, value)

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
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x10
        self.__reg_saradc_sample_cycle_lsb = 24
        self.__reg_saradc_sample_cycle_msb = 31
        self.__reg_saradc_sample_num_lsb = 16
        self.__reg_saradc_sample_num_msb = 23
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
    def reg_saradc_sample_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_sample_num_msb, self.__reg_saradc_sample_num_lsb)
    @reg_saradc_sample_num.setter
    def reg_saradc_sample_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_sample_num_msb, self.__reg_saradc_sample_num_lsb, value)
class APB_SARADC_FSM_WAIT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x14
        self.__reg_saradc_standby_wait_lsb = 16
        self.__reg_saradc_standby_wait_msb = 23
        self.__reg_saradc_rstb_wait_lsb = 8
        self.__reg_saradc_rstb_wait_msb = 15
        self.__reg_saradc_xpd_wait_lsb = 0
        self.__reg_saradc_xpd_wait_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

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

    @property
    def reg_saradc_xpd_wait(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_xpd_wait_msb, self.__reg_saradc_xpd_wait_lsb)
    @reg_saradc_xpd_wait.setter
    def reg_saradc_xpd_wait(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_xpd_wait_msb, self.__reg_saradc_xpd_wait_lsb, value)
class APB_SARADC_SAR1_STATUS(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x18
        self.__reg_saradc_sar1_status_lsb = 0
        self.__reg_saradc_sar1_status_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_saradc_sar1_status(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_sar1_status_msb, self.__reg_saradc_sar1_status_lsb)
    @reg_saradc_sar1_status.setter
    def reg_saradc_sar1_status(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_sar1_status_msb, self.__reg_saradc_sar1_status_lsb, value)
class APB_SARADC_SAR2_STATUS(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x1c
        self.__reg_saradc_sar2_status_lsb = 0
        self.__reg_saradc_sar2_status_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_saradc_sar2_status(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_sar2_status_msb, self.__reg_saradc_sar2_status_lsb)
    @reg_saradc_sar2_status.setter
    def reg_saradc_sar2_status(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_sar2_status_msb, self.__reg_saradc_sar2_status_lsb, value)
class APB_SARADC_SAR1_PATT_TAB1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x20
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
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x24
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
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x28
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
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x2c
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
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x30
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
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x34
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
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x38
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
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x3c
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
class APB_ADC_ARB_CTRL(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x40
        self.__reg_adc_arb_fix_priority_lsb = 12
        self.__reg_adc_arb_fix_priority_msb = 12
        self.__reg_adc_arb_wifi_priority_lsb = 10
        self.__reg_adc_arb_wifi_priority_msb = 11
        self.__reg_adc_arb_rtc_priority_lsb = 8
        self.__reg_adc_arb_rtc_priority_msb = 9
        self.__reg_adc_arb_apb_priority_lsb = 6
        self.__reg_adc_arb_apb_priority_msb = 7
        self.__reg_adc_arb_grant_force_lsb = 5
        self.__reg_adc_arb_grant_force_msb = 5
        self.__reg_adc_arb_wifi_force_lsb = 4
        self.__reg_adc_arb_wifi_force_msb = 4
        self.__reg_adc_arb_rtc_force_lsb = 3
        self.__reg_adc_arb_rtc_force_msb = 3
        self.__reg_adc_arb_apb_force_lsb = 2
        self.__reg_adc_arb_apb_force_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_adc_arb_fix_priority(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_arb_fix_priority_msb, self.__reg_adc_arb_fix_priority_lsb)
    @reg_adc_arb_fix_priority.setter
    def reg_adc_arb_fix_priority(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_arb_fix_priority_msb, self.__reg_adc_arb_fix_priority_lsb, value)

    @property
    def reg_adc_arb_wifi_priority(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_arb_wifi_priority_msb, self.__reg_adc_arb_wifi_priority_lsb)
    @reg_adc_arb_wifi_priority.setter
    def reg_adc_arb_wifi_priority(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_arb_wifi_priority_msb, self.__reg_adc_arb_wifi_priority_lsb, value)

    @property
    def reg_adc_arb_rtc_priority(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_arb_rtc_priority_msb, self.__reg_adc_arb_rtc_priority_lsb)
    @reg_adc_arb_rtc_priority.setter
    def reg_adc_arb_rtc_priority(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_arb_rtc_priority_msb, self.__reg_adc_arb_rtc_priority_lsb, value)

    @property
    def reg_adc_arb_apb_priority(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_arb_apb_priority_msb, self.__reg_adc_arb_apb_priority_lsb)
    @reg_adc_arb_apb_priority.setter
    def reg_adc_arb_apb_priority(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_arb_apb_priority_msb, self.__reg_adc_arb_apb_priority_lsb, value)

    @property
    def reg_adc_arb_grant_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_arb_grant_force_msb, self.__reg_adc_arb_grant_force_lsb)
    @reg_adc_arb_grant_force.setter
    def reg_adc_arb_grant_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_arb_grant_force_msb, self.__reg_adc_arb_grant_force_lsb, value)

    @property
    def reg_adc_arb_wifi_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_arb_wifi_force_msb, self.__reg_adc_arb_wifi_force_lsb)
    @reg_adc_arb_wifi_force.setter
    def reg_adc_arb_wifi_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_arb_wifi_force_msb, self.__reg_adc_arb_wifi_force_lsb, value)

    @property
    def reg_adc_arb_rtc_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_arb_rtc_force_msb, self.__reg_adc_arb_rtc_force_lsb)
    @reg_adc_arb_rtc_force.setter
    def reg_adc_arb_rtc_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_arb_rtc_force_msb, self.__reg_adc_arb_rtc_force_lsb, value)

    @property
    def reg_adc_arb_apb_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_arb_apb_force_msb, self.__reg_adc_arb_apb_force_lsb)
    @reg_adc_arb_apb_force.setter
    def reg_adc_arb_apb_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_arb_apb_force_msb, self.__reg_adc_arb_apb_force_lsb, value)
class APB_CTRL_CLK_OUT_EN(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x44
        self.__reg_clk_xtal_oen_lsb = 10
        self.__reg_clk_xtal_oen_msb = 10
        self.__reg_clk40x_bb_oen_lsb = 9
        self.__reg_clk40x_bb_oen_msb = 9
        self.__reg_clk_dac_cpu_oen_lsb = 8
        self.__reg_clk_dac_cpu_oen_msb = 8
        self.__reg_clk_adc_inf_oen_lsb = 7
        self.__reg_clk_adc_inf_oen_msb = 7
        self.__reg_clk_320m_oen_lsb = 6
        self.__reg_clk_320m_oen_msb = 6
        self.__reg_clk160_oen_lsb = 5
        self.__reg_clk160_oen_msb = 5
        self.__reg_clk80_oen_lsb = 4
        self.__reg_clk80_oen_msb = 4
        self.__reg_clk_bb_oen_lsb = 3
        self.__reg_clk_bb_oen_msb = 3
        self.__reg_clk44_oen_lsb = 2
        self.__reg_clk44_oen_msb = 2
        self.__reg_clk22_oen_lsb = 1
        self.__reg_clk22_oen_msb = 1
        self.__reg_clk20_oen_lsb = 0
        self.__reg_clk20_oen_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_clk_xtal_oen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk_xtal_oen_msb, self.__reg_clk_xtal_oen_lsb)
    @reg_clk_xtal_oen.setter
    def reg_clk_xtal_oen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk_xtal_oen_msb, self.__reg_clk_xtal_oen_lsb, value)

    @property
    def reg_clk40x_bb_oen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk40x_bb_oen_msb, self.__reg_clk40x_bb_oen_lsb)
    @reg_clk40x_bb_oen.setter
    def reg_clk40x_bb_oen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk40x_bb_oen_msb, self.__reg_clk40x_bb_oen_lsb, value)

    @property
    def reg_clk_dac_cpu_oen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk_dac_cpu_oen_msb, self.__reg_clk_dac_cpu_oen_lsb)
    @reg_clk_dac_cpu_oen.setter
    def reg_clk_dac_cpu_oen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk_dac_cpu_oen_msb, self.__reg_clk_dac_cpu_oen_lsb, value)

    @property
    def reg_clk_adc_inf_oen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk_adc_inf_oen_msb, self.__reg_clk_adc_inf_oen_lsb)
    @reg_clk_adc_inf_oen.setter
    def reg_clk_adc_inf_oen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk_adc_inf_oen_msb, self.__reg_clk_adc_inf_oen_lsb, value)

    @property
    def reg_clk_320m_oen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk_320m_oen_msb, self.__reg_clk_320m_oen_lsb)
    @reg_clk_320m_oen.setter
    def reg_clk_320m_oen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk_320m_oen_msb, self.__reg_clk_320m_oen_lsb, value)

    @property
    def reg_clk160_oen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk160_oen_msb, self.__reg_clk160_oen_lsb)
    @reg_clk160_oen.setter
    def reg_clk160_oen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk160_oen_msb, self.__reg_clk160_oen_lsb, value)

    @property
    def reg_clk80_oen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk80_oen_msb, self.__reg_clk80_oen_lsb)
    @reg_clk80_oen.setter
    def reg_clk80_oen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk80_oen_msb, self.__reg_clk80_oen_lsb, value)

    @property
    def reg_clk_bb_oen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk_bb_oen_msb, self.__reg_clk_bb_oen_lsb)
    @reg_clk_bb_oen.setter
    def reg_clk_bb_oen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk_bb_oen_msb, self.__reg_clk_bb_oen_lsb, value)

    @property
    def reg_clk44_oen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk44_oen_msb, self.__reg_clk44_oen_lsb)
    @reg_clk44_oen.setter
    def reg_clk44_oen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk44_oen_msb, self.__reg_clk44_oen_lsb, value)

    @property
    def reg_clk22_oen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk22_oen_msb, self.__reg_clk22_oen_lsb)
    @reg_clk22_oen.setter
    def reg_clk22_oen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk22_oen_msb, self.__reg_clk22_oen_lsb, value)

    @property
    def reg_clk20_oen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk20_oen_msb, self.__reg_clk20_oen_lsb)
    @reg_clk20_oen.setter
    def reg_clk20_oen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk20_oen_msb, self.__reg_clk20_oen_lsb, value)
class HOST_INF_SEL(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x48
        self.__spi_prior_lsb = 13
        self.__spi_prior_msb = 13
        self.__spi1_hold_lsb = 9
        self.__spi1_hold_msb = 9
        self.__spi0_hold_lsb = 8
        self.__spi0_hold_msb = 8
        self.__peri_io_swap_lsb = 0
        self.__peri_io_swap_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def spi_prior(self):
        return self.__MEM.rdm(self.__addr, self.__spi_prior_msb, self.__spi_prior_lsb)
    @spi_prior.setter
    def spi_prior(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi_prior_msb, self.__spi_prior_lsb, value)

    @property
    def spi1_hold(self):
        return self.__MEM.rdm(self.__addr, self.__spi1_hold_msb, self.__spi1_hold_lsb)
    @spi1_hold.setter
    def spi1_hold(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi1_hold_msb, self.__spi1_hold_lsb, value)

    @property
    def spi0_hold(self):
        return self.__MEM.rdm(self.__addr, self.__spi0_hold_msb, self.__spi0_hold_lsb)
    @spi0_hold.setter
    def spi0_hold(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi0_hold_msb, self.__spi0_hold_lsb, value)

    @property
    def peri_io_swap(self):
        return self.__MEM.rdm(self.__addr, self.__peri_io_swap_msb, self.__peri_io_swap_lsb)
    @peri_io_swap.setter
    def peri_io_swap(self, value):
        return self.__MEM.wrm(self.__addr, self.__peri_io_swap_msb, self.__peri_io_swap_lsb, value)
class EXT_MEM_PMS_LOCK(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x4c
        self.__ext_mem_pms_lock_lsb = 0
        self.__ext_mem_pms_lock_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def ext_mem_pms_lock(self):
        return self.__MEM.rdm(self.__addr, self.__ext_mem_pms_lock_msb, self.__ext_mem_pms_lock_lsb)
    @ext_mem_pms_lock.setter
    def ext_mem_pms_lock(self, value):
        return self.__MEM.wrm(self.__addr, self.__ext_mem_pms_lock_msb, self.__ext_mem_pms_lock_lsb, value)
class FLASH_ACE0_ATTR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x50
        self.__flash_ace0_attr_lsb = 0
        self.__flash_ace0_attr_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def flash_ace0_attr(self):
        return self.__MEM.rdm(self.__addr, self.__flash_ace0_attr_msb, self.__flash_ace0_attr_lsb)
    @flash_ace0_attr.setter
    def flash_ace0_attr(self, value):
        return self.__MEM.wrm(self.__addr, self.__flash_ace0_attr_msb, self.__flash_ace0_attr_lsb, value)
class FLASH_ACE1_ATTR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x54
        self.__flash_ace1_attr_lsb = 0
        self.__flash_ace1_attr_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def flash_ace1_attr(self):
        return self.__MEM.rdm(self.__addr, self.__flash_ace1_attr_msb, self.__flash_ace1_attr_lsb)
    @flash_ace1_attr.setter
    def flash_ace1_attr(self, value):
        return self.__MEM.wrm(self.__addr, self.__flash_ace1_attr_msb, self.__flash_ace1_attr_lsb, value)
class FLASH_ACE2_ATTR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x58
        self.__flash_ace2_attr_lsb = 0
        self.__flash_ace2_attr_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def flash_ace2_attr(self):
        return self.__MEM.rdm(self.__addr, self.__flash_ace2_attr_msb, self.__flash_ace2_attr_lsb)
    @flash_ace2_attr.setter
    def flash_ace2_attr(self, value):
        return self.__MEM.wrm(self.__addr, self.__flash_ace2_attr_msb, self.__flash_ace2_attr_lsb, value)
class FLASH_ACE3_ATTR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x5c
        self.__flash_ace3_attr_lsb = 0
        self.__flash_ace3_attr_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def flash_ace3_attr(self):
        return self.__MEM.rdm(self.__addr, self.__flash_ace3_attr_msb, self.__flash_ace3_attr_lsb)
    @flash_ace3_attr.setter
    def flash_ace3_attr(self, value):
        return self.__MEM.wrm(self.__addr, self.__flash_ace3_attr_msb, self.__flash_ace3_attr_lsb, value)
class FLASH_ACE0_ADDR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x60
        self.__flash_ace0_addr_s_lsb = 0
        self.__flash_ace0_addr_s_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def flash_ace0_addr_s(self):
        return self.__MEM.rdm(self.__addr, self.__flash_ace0_addr_s_msb, self.__flash_ace0_addr_s_lsb)
    @flash_ace0_addr_s.setter
    def flash_ace0_addr_s(self, value):
        return self.__MEM.wrm(self.__addr, self.__flash_ace0_addr_s_msb, self.__flash_ace0_addr_s_lsb, value)
class FLASH_ACE1_ADDR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x64
        self.__flash_ace1_addr_s_lsb = 0
        self.__flash_ace1_addr_s_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def flash_ace1_addr_s(self):
        return self.__MEM.rdm(self.__addr, self.__flash_ace1_addr_s_msb, self.__flash_ace1_addr_s_lsb)
    @flash_ace1_addr_s.setter
    def flash_ace1_addr_s(self, value):
        return self.__MEM.wrm(self.__addr, self.__flash_ace1_addr_s_msb, self.__flash_ace1_addr_s_lsb, value)
class FLASH_ACE2_ADDR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x68
        self.__flash_ace2_addr_s_lsb = 0
        self.__flash_ace2_addr_s_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def flash_ace2_addr_s(self):
        return self.__MEM.rdm(self.__addr, self.__flash_ace2_addr_s_msb, self.__flash_ace2_addr_s_lsb)
    @flash_ace2_addr_s.setter
    def flash_ace2_addr_s(self, value):
        return self.__MEM.wrm(self.__addr, self.__flash_ace2_addr_s_msb, self.__flash_ace2_addr_s_lsb, value)
class FLASH_ACE3_ADDR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x6c
        self.__flash_ace3_addr_s_lsb = 0
        self.__flash_ace3_addr_s_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def flash_ace3_addr_s(self):
        return self.__MEM.rdm(self.__addr, self.__flash_ace3_addr_s_msb, self.__flash_ace3_addr_s_lsb)
    @flash_ace3_addr_s.setter
    def flash_ace3_addr_s(self, value):
        return self.__MEM.wrm(self.__addr, self.__flash_ace3_addr_s_msb, self.__flash_ace3_addr_s_lsb, value)
class FLASH_ACE0_SIZE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x70
        self.__flash_ace0_size_lsb = 0
        self.__flash_ace0_size_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def flash_ace0_size(self):
        return self.__MEM.rdm(self.__addr, self.__flash_ace0_size_msb, self.__flash_ace0_size_lsb)
    @flash_ace0_size.setter
    def flash_ace0_size(self, value):
        return self.__MEM.wrm(self.__addr, self.__flash_ace0_size_msb, self.__flash_ace0_size_lsb, value)
class FLASH_ACE1_SIZE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x74
        self.__flash_ace1_size_lsb = 0
        self.__flash_ace1_size_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def flash_ace1_size(self):
        return self.__MEM.rdm(self.__addr, self.__flash_ace1_size_msb, self.__flash_ace1_size_lsb)
    @flash_ace1_size.setter
    def flash_ace1_size(self, value):
        return self.__MEM.wrm(self.__addr, self.__flash_ace1_size_msb, self.__flash_ace1_size_lsb, value)
class FLASH_ACE2_SIZE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x78
        self.__flash_ace2_size_lsb = 0
        self.__flash_ace2_size_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def flash_ace2_size(self):
        return self.__MEM.rdm(self.__addr, self.__flash_ace2_size_msb, self.__flash_ace2_size_lsb)
    @flash_ace2_size.setter
    def flash_ace2_size(self, value):
        return self.__MEM.wrm(self.__addr, self.__flash_ace2_size_msb, self.__flash_ace2_size_lsb, value)
class FLASH_ACE3_SIZE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x7c
        self.__flash_ace3_size_lsb = 0
        self.__flash_ace3_size_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def flash_ace3_size(self):
        return self.__MEM.rdm(self.__addr, self.__flash_ace3_size_msb, self.__flash_ace3_size_lsb)
    @flash_ace3_size.setter
    def flash_ace3_size(self, value):
        return self.__MEM.wrm(self.__addr, self.__flash_ace3_size_msb, self.__flash_ace3_size_lsb, value)
class SRAM_ACE0_ATTR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x80
        self.__sram_ace0_attr_lsb = 0
        self.__sram_ace0_attr_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_ace0_attr(self):
        return self.__MEM.rdm(self.__addr, self.__sram_ace0_attr_msb, self.__sram_ace0_attr_lsb)
    @sram_ace0_attr.setter
    def sram_ace0_attr(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_ace0_attr_msb, self.__sram_ace0_attr_lsb, value)
class SRAM_ACE1_ATTR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x84
        self.__sram_ace1_attr_lsb = 0
        self.__sram_ace1_attr_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_ace1_attr(self):
        return self.__MEM.rdm(self.__addr, self.__sram_ace1_attr_msb, self.__sram_ace1_attr_lsb)
    @sram_ace1_attr.setter
    def sram_ace1_attr(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_ace1_attr_msb, self.__sram_ace1_attr_lsb, value)
class SRAM_ACE2_ATTR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x88
        self.__sram_ace2_attr_lsb = 0
        self.__sram_ace2_attr_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_ace2_attr(self):
        return self.__MEM.rdm(self.__addr, self.__sram_ace2_attr_msb, self.__sram_ace2_attr_lsb)
    @sram_ace2_attr.setter
    def sram_ace2_attr(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_ace2_attr_msb, self.__sram_ace2_attr_lsb, value)
class SRAM_ACE3_ATTR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x8c
        self.__sram_ace3_attr_lsb = 0
        self.__sram_ace3_attr_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_ace3_attr(self):
        return self.__MEM.rdm(self.__addr, self.__sram_ace3_attr_msb, self.__sram_ace3_attr_lsb)
    @sram_ace3_attr.setter
    def sram_ace3_attr(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_ace3_attr_msb, self.__sram_ace3_attr_lsb, value)
class SRAM_ACE0_ADDR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x90
        self.__sram_ace0_addr_s_lsb = 0
        self.__sram_ace0_addr_s_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_ace0_addr_s(self):
        return self.__MEM.rdm(self.__addr, self.__sram_ace0_addr_s_msb, self.__sram_ace0_addr_s_lsb)
    @sram_ace0_addr_s.setter
    def sram_ace0_addr_s(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_ace0_addr_s_msb, self.__sram_ace0_addr_s_lsb, value)
class SRAM_ACE1_ADDR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x94
        self.__sram_ace1_addr_s_lsb = 0
        self.__sram_ace1_addr_s_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_ace1_addr_s(self):
        return self.__MEM.rdm(self.__addr, self.__sram_ace1_addr_s_msb, self.__sram_ace1_addr_s_lsb)
    @sram_ace1_addr_s.setter
    def sram_ace1_addr_s(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_ace1_addr_s_msb, self.__sram_ace1_addr_s_lsb, value)
class SRAM_ACE2_ADDR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x98
        self.__sram_ace2_addr_s_lsb = 0
        self.__sram_ace2_addr_s_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_ace2_addr_s(self):
        return self.__MEM.rdm(self.__addr, self.__sram_ace2_addr_s_msb, self.__sram_ace2_addr_s_lsb)
    @sram_ace2_addr_s.setter
    def sram_ace2_addr_s(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_ace2_addr_s_msb, self.__sram_ace2_addr_s_lsb, value)
class SRAM_ACE3_ADDR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x9c
        self.__sram_ace3_addr_s_lsb = 0
        self.__sram_ace3_addr_s_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_ace3_addr_s(self):
        return self.__MEM.rdm(self.__addr, self.__sram_ace3_addr_s_msb, self.__sram_ace3_addr_s_lsb)
    @sram_ace3_addr_s.setter
    def sram_ace3_addr_s(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_ace3_addr_s_msb, self.__sram_ace3_addr_s_lsb, value)
class SRAM_ACE0_SIZE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0xa0
        self.__sram_ace0_size_lsb = 0
        self.__sram_ace0_size_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_ace0_size(self):
        return self.__MEM.rdm(self.__addr, self.__sram_ace0_size_msb, self.__sram_ace0_size_lsb)
    @sram_ace0_size.setter
    def sram_ace0_size(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_ace0_size_msb, self.__sram_ace0_size_lsb, value)
class SRAM_ACE1_SIZE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0xa4
        self.__sram_ace1_size_lsb = 0
        self.__sram_ace1_size_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_ace1_size(self):
        return self.__MEM.rdm(self.__addr, self.__sram_ace1_size_msb, self.__sram_ace1_size_lsb)
    @sram_ace1_size.setter
    def sram_ace1_size(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_ace1_size_msb, self.__sram_ace1_size_lsb, value)
class SRAM_ACE2_SIZE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0xa8
        self.__sram_ace2_size_lsb = 0
        self.__sram_ace2_size_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_ace2_size(self):
        return self.__MEM.rdm(self.__addr, self.__sram_ace2_size_msb, self.__sram_ace2_size_lsb)
    @sram_ace2_size.setter
    def sram_ace2_size(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_ace2_size_msb, self.__sram_ace2_size_lsb, value)
class SRAM_ACE3_SIZE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0xac
        self.__sram_ace3_size_lsb = 0
        self.__sram_ace3_size_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_ace3_size(self):
        return self.__MEM.rdm(self.__addr, self.__sram_ace3_size_msb, self.__sram_ace3_size_lsb)
    @sram_ace3_size.setter
    def sram_ace3_size(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_ace3_size_msb, self.__sram_ace3_size_lsb, value)
class SPI0_PMS_CTRL(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0xb0
        self.__spi0_reject_cde_lsb = 2
        self.__spi0_reject_cde_msb = 6
        self.__spi0_reject_clr_lsb = 1
        self.__spi0_reject_clr_msb = 1
        self.__spi0_reject_int_lsb = 0
        self.__spi0_reject_int_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def spi0_reject_cde(self):
        return self.__MEM.rdm(self.__addr, self.__spi0_reject_cde_msb, self.__spi0_reject_cde_lsb)
    @spi0_reject_cde.setter
    def spi0_reject_cde(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi0_reject_cde_msb, self.__spi0_reject_cde_lsb, value)

    @property
    def spi0_reject_clr(self):
        return self.__MEM.rdm(self.__addr, self.__spi0_reject_clr_msb, self.__spi0_reject_clr_lsb)
    @spi0_reject_clr.setter
    def spi0_reject_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi0_reject_clr_msb, self.__spi0_reject_clr_lsb, value)

    @property
    def spi0_reject_int(self):
        return self.__MEM.rdm(self.__addr, self.__spi0_reject_int_msb, self.__spi0_reject_int_lsb)
    @spi0_reject_int.setter
    def spi0_reject_int(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi0_reject_int_msb, self.__spi0_reject_int_lsb, value)
class SPI0_REJECT_ADDR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0xb4
        self.__spi0_reject_addr_lsb = 0
        self.__spi0_reject_addr_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def spi0_reject_addr(self):
        return self.__MEM.rdm(self.__addr, self.__spi0_reject_addr_msb, self.__spi0_reject_addr_lsb)
    @spi0_reject_addr.setter
    def spi0_reject_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi0_reject_addr_msb, self.__spi0_reject_addr_lsb, value)
class SPI1_PMS_CTRL(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0xb8
        self.__spi1_reject_cde_lsb = 2
        self.__spi1_reject_cde_msb = 6
        self.__spi1_reject_clr_lsb = 1
        self.__spi1_reject_clr_msb = 1
        self.__spi1_reject_int_lsb = 0
        self.__spi1_reject_int_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def spi1_reject_cde(self):
        return self.__MEM.rdm(self.__addr, self.__spi1_reject_cde_msb, self.__spi1_reject_cde_lsb)
    @spi1_reject_cde.setter
    def spi1_reject_cde(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi1_reject_cde_msb, self.__spi1_reject_cde_lsb, value)

    @property
    def spi1_reject_clr(self):
        return self.__MEM.rdm(self.__addr, self.__spi1_reject_clr_msb, self.__spi1_reject_clr_lsb)
    @spi1_reject_clr.setter
    def spi1_reject_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi1_reject_clr_msb, self.__spi1_reject_clr_lsb, value)

    @property
    def spi1_reject_int(self):
        return self.__MEM.rdm(self.__addr, self.__spi1_reject_int_msb, self.__spi1_reject_int_lsb)
    @spi1_reject_int.setter
    def spi1_reject_int(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi1_reject_int_msb, self.__spi1_reject_int_lsb, value)
class SPI1_REJECT_ADDR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0xbc
        self.__spi1_reject_addr_lsb = 0
        self.__spi1_reject_addr_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def spi1_reject_addr(self):
        return self.__MEM.rdm(self.__addr, self.__spi1_reject_addr_msb, self.__spi1_reject_addr_lsb)
    @spi1_reject_addr.setter
    def spi1_reject_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi1_reject_addr_msb, self.__spi1_reject_addr_lsb, value)
class APB_CTRL_SDIO_CTRL(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0xc0
        self.__reg_sdio_win_access_en_lsb = 0
        self.__reg_sdio_win_access_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sdio_win_access_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sdio_win_access_en_msb, self.__reg_sdio_win_access_en_lsb)
    @reg_sdio_win_access_en.setter
    def reg_sdio_win_access_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sdio_win_access_en_msb, self.__reg_sdio_win_access_en_lsb, value)
class REDCY_SIG0_REG(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0xc4
        self.__redcy_andor_lsb = 31
        self.__redcy_andor_msb = 31
        self.__redcy_sig0_lsb = 0
        self.__redcy_sig0_msb = 30
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def redcy_andor(self):
        return self.__MEM.rdm(self.__addr, self.__redcy_andor_msb, self.__redcy_andor_lsb)
    @redcy_andor.setter
    def redcy_andor(self, value):
        return self.__MEM.wrm(self.__addr, self.__redcy_andor_msb, self.__redcy_andor_lsb, value)

    @property
    def redcy_sig0(self):
        return self.__MEM.rdm(self.__addr, self.__redcy_sig0_msb, self.__redcy_sig0_lsb)
    @redcy_sig0.setter
    def redcy_sig0(self, value):
        return self.__MEM.wrm(self.__addr, self.__redcy_sig0_msb, self.__redcy_sig0_lsb, value)
class REDCY_SIG1_REG(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0xc8
        self.__redcy_nandor_lsb = 31
        self.__redcy_nandor_msb = 31
        self.__redcy_sig1_lsb = 0
        self.__redcy_sig1_msb = 30
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def redcy_nandor(self):
        return self.__MEM.rdm(self.__addr, self.__redcy_nandor_msb, self.__redcy_nandor_lsb)
    @redcy_nandor.setter
    def redcy_nandor(self, value):
        return self.__MEM.wrm(self.__addr, self.__redcy_nandor_msb, self.__redcy_nandor_lsb, value)

    @property
    def redcy_sig1(self):
        return self.__MEM.rdm(self.__addr, self.__redcy_sig1_msb, self.__redcy_sig1_lsb)
    @redcy_sig1.setter
    def redcy_sig1(self, value):
        return self.__MEM.wrm(self.__addr, self.__redcy_sig1_msb, self.__redcy_sig1_lsb, value)
class WIFI_BB_CFG(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0xcc
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
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0xd0
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
class WIFI_CLK_EN(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0xd4
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
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0xd8
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
class FRONT_END_MEM_PD(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0xdc
        self.__reg_dc_mem_force_pd_lsb = 5
        self.__reg_dc_mem_force_pd_msb = 5
        self.__reg_dc_mem_force_pu_lsb = 4
        self.__reg_dc_mem_force_pu_msb = 4
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
    def reg_dc_mem_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_mem_force_pd_msb, self.__reg_dc_mem_force_pd_lsb)
    @reg_dc_mem_force_pd.setter
    def reg_dc_mem_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_mem_force_pd_msb, self.__reg_dc_mem_force_pd_lsb, value)

    @property
    def reg_dc_mem_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_mem_force_pu_msb, self.__reg_dc_mem_force_pu_lsb)
    @reg_dc_mem_force_pu.setter
    def reg_dc_mem_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_mem_force_pu_msb, self.__reg_dc_mem_force_pu_lsb, value)

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
class APB_CTRL_DATE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x3fc
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
        return 0x18102500
