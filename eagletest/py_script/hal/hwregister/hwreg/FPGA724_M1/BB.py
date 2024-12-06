from hal.common import *
from hal.hwregister.hwreg.FPGA724_M1.addr_base import *
class BB(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.BB_CTRL0 = BB_CTRL0(self.channel, self.chipv)
        self.BB_DIAG0 = BB_DIAG0(self.channel, self.chipv)
        self.BB_NRXRD1 = BB_NRXRD1(self.channel, self.chipv)
        self.DC_CTRL_0 = DC_CTRL_0(self.channel, self.chipv)
        self.TONE_CTRL_0 = TONE_CTRL_0(self.channel, self.chipv)
        self.TONE_CTRL_1 = TONE_CTRL_1(self.channel, self.chipv)
        self.TONE_CTRL_2 = TONE_CTRL_2(self.channel, self.chipv)
        self.TONE_CTRL_3 = TONE_CTRL_3(self.channel, self.chipv)
        self.TONE_CTRL_4 = TONE_CTRL_4(self.channel, self.chipv)
        self.TONE_CTRL_5 = TONE_CTRL_5(self.channel, self.chipv)
        self.BB_RESET = BB_RESET(self.channel, self.chipv)
        self.TONE_CTRL_6 = TONE_CTRL_6(self.channel, self.chipv)
        self.BB_FSM_CTRL = BB_FSM_CTRL(self.channel, self.chipv)
        self.DCDELTACONF0 = DCDELTACONF0(self.channel, self.chipv)
        self.DCDELTACONF1 = DCDELTACONF1(self.channel, self.chipv)
        self.BB_WDG_0 = BB_WDG_0(self.channel, self.chipv)
        self.BB_WDG_1 = BB_WDG_1(self.channel, self.chipv)
        self.BB_INT_ENA = BB_INT_ENA(self.channel, self.chipv)
        self.BB_INT_RAW = BB_INT_RAW(self.channel, self.chipv)
        self.BB_INT_ST = BB_INT_ST(self.channel, self.chipv)
        self.BB_INT_CLR = BB_INT_CLR(self.channel, self.chipv)
        self.BBPD_CTRL = BBPD_CTRL(self.channel, self.chipv)
        self.BB_CCA_CTRL_0 = BB_CCA_CTRL_0(self.channel, self.chipv)
        self.BB_CCA_CTRL_1 = BB_CCA_CTRL_1(self.channel, self.chipv)
        self.BB_CCA_CTRL_2 = BB_CCA_CTRL_2(self.channel, self.chipv)
        self.BB_CCA_CTRL_3 = BB_CCA_CTRL_3(self.channel, self.chipv)
        self.BB_NRXFDM_WDG = BB_NRXFDM_WDG(self.channel, self.chipv)
        self.BB_CTRL1 = BB_CTRL1(self.channel, self.chipv)
        self.BB_DC_RM_CONF0 = BB_DC_RM_CONF0(self.channel, self.chipv)
        self.BB_DC_RM_CONF1 = BB_DC_RM_CONF1(self.channel, self.chipv)
        self.DC_CTRL1 = DC_CTRL1(self.channel, self.chipv)
        self.DC_CTRL2 = DC_CTRL2(self.channel, self.chipv)
        self.BB_CLK_CONF = BB_CLK_CONF(self.channel, self.chipv)
        self.BB_STATE_CNT_CONF0 = BB_STATE_CNT_CONF0(self.channel, self.chipv)
        self.BB_STATE_CNT_CONF1 = BB_STATE_CNT_CONF1(self.channel, self.chipv)
        self.TONE_CTRL_7 = TONE_CTRL_7(self.channel, self.chipv)
        self.TONE_CTRL_8 = TONE_CTRL_8(self.channel, self.chipv)
        self.TONE_CTRL_9 = TONE_CTRL_9(self.channel, self.chipv)
        self.TONE_CTRL_10 = TONE_CTRL_10(self.channel, self.chipv)
        self.BB_STATE_CNT_CONF2 = BB_STATE_CNT_CONF2(self.channel, self.chipv)
        self.TONE_CTRL_11 = TONE_CTRL_11(self.channel, self.chipv)
        self.TONE_CTRL_12 = TONE_CTRL_12(self.channel, self.chipv)
        self.BB_NOUSE = BB_NOUSE(self.channel, self.chipv)
class BB_CTRL0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x0
        self.__reg_fft_clk_opt_lsb = 21
        self.__reg_fft_clk_opt_msb = 26
        self.__reg_dac_on_wait_lsb = 11
        self.__reg_dac_on_wait_msb = 20
        self.__reg_bb_mac_inf_path_lsb = 10
        self.__reg_bb_mac_inf_path_msb = 10
        self.__reg_rxcov_force_clk_lsb = 8
        self.__reg_rxcov_force_clk_msb = 8
        self.__reg_rxcov_ht40_force_clk_lsb = 7
        self.__reg_rxcov_ht40_force_clk_msb = 7
        self.__reg_ht20_cen_bcov_en_lsb = 6
        self.__reg_ht20_cen_bcov_en_msb = 6
        self.__reg_tx_top_clk_force_on_lsb = 3
        self.__reg_tx_top_clk_force_on_msb = 5
        self.__reg_fft_out_force_clk_lsb = 2
        self.__reg_fft_out_force_clk_msb = 2
        self.__reg_fft_force_clk_lsb = 1
        self.__reg_fft_force_clk_msb = 1
        self.__reg_ht40_bcov_en_lsb = 0
        self.__reg_ht40_bcov_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_fft_clk_opt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fft_clk_opt_msb, self.__reg_fft_clk_opt_lsb)
    @reg_fft_clk_opt.setter
    def reg_fft_clk_opt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fft_clk_opt_msb, self.__reg_fft_clk_opt_lsb, value)

    @property
    def reg_dac_on_wait(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dac_on_wait_msb, self.__reg_dac_on_wait_lsb)
    @reg_dac_on_wait.setter
    def reg_dac_on_wait(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dac_on_wait_msb, self.__reg_dac_on_wait_lsb, value)

    @property
    def reg_bb_mac_inf_path(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_mac_inf_path_msb, self.__reg_bb_mac_inf_path_lsb)
    @reg_bb_mac_inf_path.setter
    def reg_bb_mac_inf_path(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_mac_inf_path_msb, self.__reg_bb_mac_inf_path_lsb, value)

    @property
    def reg_rxcov_force_clk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxcov_force_clk_msb, self.__reg_rxcov_force_clk_lsb)
    @reg_rxcov_force_clk.setter
    def reg_rxcov_force_clk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxcov_force_clk_msb, self.__reg_rxcov_force_clk_lsb, value)

    @property
    def reg_rxcov_ht40_force_clk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxcov_ht40_force_clk_msb, self.__reg_rxcov_ht40_force_clk_lsb)
    @reg_rxcov_ht40_force_clk.setter
    def reg_rxcov_ht40_force_clk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxcov_ht40_force_clk_msb, self.__reg_rxcov_ht40_force_clk_lsb, value)

    @property
    def reg_ht20_cen_bcov_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ht20_cen_bcov_en_msb, self.__reg_ht20_cen_bcov_en_lsb)
    @reg_ht20_cen_bcov_en.setter
    def reg_ht20_cen_bcov_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ht20_cen_bcov_en_msb, self.__reg_ht20_cen_bcov_en_lsb, value)

    @property
    def reg_tx_top_clk_force_on(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_top_clk_force_on_msb, self.__reg_tx_top_clk_force_on_lsb)
    @reg_tx_top_clk_force_on.setter
    def reg_tx_top_clk_force_on(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_top_clk_force_on_msb, self.__reg_tx_top_clk_force_on_lsb, value)

    @property
    def reg_fft_out_force_clk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fft_out_force_clk_msb, self.__reg_fft_out_force_clk_lsb)
    @reg_fft_out_force_clk.setter
    def reg_fft_out_force_clk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fft_out_force_clk_msb, self.__reg_fft_out_force_clk_lsb, value)

    @property
    def reg_fft_force_clk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fft_force_clk_msb, self.__reg_fft_force_clk_lsb)
    @reg_fft_force_clk.setter
    def reg_fft_force_clk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fft_force_clk_msb, self.__reg_fft_force_clk_lsb, value)

    @property
    def reg_ht40_bcov_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ht40_bcov_en_msb, self.__reg_ht40_bcov_en_lsb)
    @reg_ht40_bcov_en.setter
    def reg_ht40_bcov_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ht40_bcov_en_msb, self.__reg_ht40_bcov_en_lsb, value)
class BB_DIAG0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x4
        self.__diag_hung_int_lsb = 31
        self.__diag_hung_int_msb = 31
        self.__reg_diag_mode_sel_lsb = 30
        self.__reg_diag_mode_sel_msb = 30
        self.__reg_diag_hung_int_clr_lsb = 29
        self.__reg_diag_hung_int_clr_msb = 29
        self.__reg_diag_hung_int_en_lsb = 28
        self.__reg_diag_hung_int_en_msb = 28
        self.__reg_diag_hung_cnt_lsb = 12
        self.__reg_diag_hung_cnt_msb = 27
        self.__reg_diag_st_lsb = 8
        self.__reg_diag_st_msb = 11
        self.__reg_diag_sel_1_lsb = 4
        self.__reg_diag_sel_1_msb = 7
        self.__reg_diag_sel_0_lsb = 0
        self.__reg_diag_sel_0_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def diag_hung_int(self):
        return self.__MEM.rdm(self.__addr, self.__diag_hung_int_msb, self.__diag_hung_int_lsb)
    @diag_hung_int.setter
    def diag_hung_int(self, value):
        return self.__MEM.wrm(self.__addr, self.__diag_hung_int_msb, self.__diag_hung_int_lsb, value)

    @property
    def reg_diag_mode_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_diag_mode_sel_msb, self.__reg_diag_mode_sel_lsb)
    @reg_diag_mode_sel.setter
    def reg_diag_mode_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_diag_mode_sel_msb, self.__reg_diag_mode_sel_lsb, value)

    @property
    def reg_diag_hung_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_diag_hung_int_clr_msb, self.__reg_diag_hung_int_clr_lsb)
    @reg_diag_hung_int_clr.setter
    def reg_diag_hung_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_diag_hung_int_clr_msb, self.__reg_diag_hung_int_clr_lsb, value)

    @property
    def reg_diag_hung_int_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_diag_hung_int_en_msb, self.__reg_diag_hung_int_en_lsb)
    @reg_diag_hung_int_en.setter
    def reg_diag_hung_int_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_diag_hung_int_en_msb, self.__reg_diag_hung_int_en_lsb, value)

    @property
    def reg_diag_hung_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_diag_hung_cnt_msb, self.__reg_diag_hung_cnt_lsb)
    @reg_diag_hung_cnt.setter
    def reg_diag_hung_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_diag_hung_cnt_msb, self.__reg_diag_hung_cnt_lsb, value)

    @property
    def reg_diag_st(self):
        return self.__MEM.rdm(self.__addr, self.__reg_diag_st_msb, self.__reg_diag_st_lsb)
    @reg_diag_st.setter
    def reg_diag_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_diag_st_msb, self.__reg_diag_st_lsb, value)

    @property
    def reg_diag_sel_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_diag_sel_1_msb, self.__reg_diag_sel_1_lsb)
    @reg_diag_sel_1.setter
    def reg_diag_sel_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_diag_sel_1_msb, self.__reg_diag_sel_1_lsb, value)

    @property
    def reg_diag_sel_0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_diag_sel_0_msb, self.__reg_diag_sel_0_lsb)
    @reg_diag_sel_0.setter
    def reg_diag_sel_0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_diag_sel_0_msb, self.__reg_diag_sel_0_lsb, value)
class BB_NRXRD1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x8
        self.__bb_status_lsb = 0
        self.__bb_status_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def bb_status(self):
        return self.__MEM.rdm(self.__addr, self.__bb_status_msb, self.__bb_status_lsb)
    @bb_status.setter
    def bb_status(self, value):
        return self.__MEM.wrm(self.__addr, self.__bb_status_msb, self.__bb_status_lsb, value)
class DC_CTRL_0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0xc
        self.__reg_dmd_in_80m_en_lsb = 20
        self.__reg_dmd_in_80m_en_msb = 20
        self.__reg_dc_shift_find_max_lsb = 17
        self.__reg_dc_shift_find_max_msb = 19
        self.__reg_dc_cnt_init_lsb = 13
        self.__reg_dc_cnt_init_msb = 16
        self.__reg_dc_shift_max_lsb = 10
        self.__reg_dc_shift_max_msb = 12
        self.__reg_dc_rm_en_lsb = 9
        self.__reg_dc_rm_en_msb = 9
        self.__reg_dc_max_lsb = 0
        self.__reg_dc_max_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_dmd_in_80m_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dmd_in_80m_en_msb, self.__reg_dmd_in_80m_en_lsb)
    @reg_dmd_in_80m_en.setter
    def reg_dmd_in_80m_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dmd_in_80m_en_msb, self.__reg_dmd_in_80m_en_lsb, value)

    @property
    def reg_dc_shift_find_max(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_shift_find_max_msb, self.__reg_dc_shift_find_max_lsb)
    @reg_dc_shift_find_max.setter
    def reg_dc_shift_find_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_shift_find_max_msb, self.__reg_dc_shift_find_max_lsb, value)

    @property
    def reg_dc_cnt_init(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_cnt_init_msb, self.__reg_dc_cnt_init_lsb)
    @reg_dc_cnt_init.setter
    def reg_dc_cnt_init(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_cnt_init_msb, self.__reg_dc_cnt_init_lsb, value)

    @property
    def reg_dc_shift_max(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_shift_max_msb, self.__reg_dc_shift_max_lsb)
    @reg_dc_shift_max.setter
    def reg_dc_shift_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_shift_max_msb, self.__reg_dc_shift_max_lsb, value)

    @property
    def reg_dc_rm_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_rm_en_msb, self.__reg_dc_rm_en_lsb)
    @reg_dc_rm_en.setter
    def reg_dc_rm_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_rm_en_msb, self.__reg_dc_rm_en_lsb, value)

    @property
    def reg_dc_max(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_max_msb, self.__reg_dc_max_lsb)
    @reg_dc_max.setter
    def reg_dc_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_max_msb, self.__reg_dc_max_lsb, value)
class TONE_CTRL_0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x10
        self.__reg_fft_htltf_stop_en_lsb = 31
        self.__reg_fft_htltf_stop_en_msb = 31
        self.__reg_fft_tone_gain_thr_lsb = 24
        self.__reg_fft_tone_gain_thr_msb = 30
        self.__reg_phi_tone_gain_thr_lsb = 17
        self.__reg_phi_tone_gain_thr_msb = 23
        self.__reg_agc_tone_gain_thr_lsb = 10
        self.__reg_agc_tone_gain_thr_msb = 16
        self.__reg_fft_dc_rm_en_lsb = 9
        self.__reg_fft_dc_rm_en_msb = 9
        self.__reg_fft_tone_rm_en_lsb = 8
        self.__reg_fft_tone_rm_en_msb = 8
        self.__reg_tone_max_lsb = 0
        self.__reg_tone_max_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_fft_htltf_stop_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fft_htltf_stop_en_msb, self.__reg_fft_htltf_stop_en_lsb)
    @reg_fft_htltf_stop_en.setter
    def reg_fft_htltf_stop_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fft_htltf_stop_en_msb, self.__reg_fft_htltf_stop_en_lsb, value)

    @property
    def reg_fft_tone_gain_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fft_tone_gain_thr_msb, self.__reg_fft_tone_gain_thr_lsb)
    @reg_fft_tone_gain_thr.setter
    def reg_fft_tone_gain_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fft_tone_gain_thr_msb, self.__reg_fft_tone_gain_thr_lsb, value)

    @property
    def reg_phi_tone_gain_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_phi_tone_gain_thr_msb, self.__reg_phi_tone_gain_thr_lsb)
    @reg_phi_tone_gain_thr.setter
    def reg_phi_tone_gain_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_phi_tone_gain_thr_msb, self.__reg_phi_tone_gain_thr_lsb, value)

    @property
    def reg_agc_tone_gain_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_tone_gain_thr_msb, self.__reg_agc_tone_gain_thr_lsb)
    @reg_agc_tone_gain_thr.setter
    def reg_agc_tone_gain_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_tone_gain_thr_msb, self.__reg_agc_tone_gain_thr_lsb, value)

    @property
    def reg_fft_dc_rm_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fft_dc_rm_en_msb, self.__reg_fft_dc_rm_en_lsb)
    @reg_fft_dc_rm_en.setter
    def reg_fft_dc_rm_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fft_dc_rm_en_msb, self.__reg_fft_dc_rm_en_lsb, value)

    @property
    def reg_fft_tone_rm_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fft_tone_rm_en_msb, self.__reg_fft_tone_rm_en_lsb)
    @reg_fft_tone_rm_en.setter
    def reg_fft_tone_rm_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fft_tone_rm_en_msb, self.__reg_fft_tone_rm_en_lsb, value)

    @property
    def reg_tone_max(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_max_msb, self.__reg_tone_max_lsb)
    @reg_tone_max.setter
    def reg_tone_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_max_msb, self.__reg_tone_max_lsb, value)
class TONE_CTRL_1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x14
        self.__reg_tone_shift_max_1_ht20_delta_lsb = 31
        self.__reg_tone_shift_max_1_ht20_delta_msb = 31
        self.__reg_tone_shift_max_1_fft_lsb = 28
        self.__reg_tone_shift_max_1_fft_msb = 30
        self.__reg_tone_shift_max_1_phi_lsb = 25
        self.__reg_tone_shift_max_1_phi_msb = 27
        self.__reg_tone_shift_max_1_agc_lsb = 22
        self.__reg_tone_shift_max_1_agc_msb = 24
        self.__reg_tone_fft_thr_1_lsb = 14
        self.__reg_tone_fft_thr_1_msb = 21
        self.__reg_tone_rm_en_1_lsb = 13
        self.__reg_tone_rm_en_1_msb = 13
        self.__reg_tone_est_coef_1_lsb = 0
        self.__reg_tone_est_coef_1_msb = 12
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tone_shift_max_1_ht20_delta(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_shift_max_1_ht20_delta_msb, self.__reg_tone_shift_max_1_ht20_delta_lsb)
    @reg_tone_shift_max_1_ht20_delta.setter
    def reg_tone_shift_max_1_ht20_delta(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_shift_max_1_ht20_delta_msb, self.__reg_tone_shift_max_1_ht20_delta_lsb, value)

    @property
    def reg_tone_shift_max_1_fft(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_shift_max_1_fft_msb, self.__reg_tone_shift_max_1_fft_lsb)
    @reg_tone_shift_max_1_fft.setter
    def reg_tone_shift_max_1_fft(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_shift_max_1_fft_msb, self.__reg_tone_shift_max_1_fft_lsb, value)

    @property
    def reg_tone_shift_max_1_phi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_shift_max_1_phi_msb, self.__reg_tone_shift_max_1_phi_lsb)
    @reg_tone_shift_max_1_phi.setter
    def reg_tone_shift_max_1_phi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_shift_max_1_phi_msb, self.__reg_tone_shift_max_1_phi_lsb, value)

    @property
    def reg_tone_shift_max_1_agc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_shift_max_1_agc_msb, self.__reg_tone_shift_max_1_agc_lsb)
    @reg_tone_shift_max_1_agc.setter
    def reg_tone_shift_max_1_agc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_shift_max_1_agc_msb, self.__reg_tone_shift_max_1_agc_lsb, value)

    @property
    def reg_tone_fft_thr_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_fft_thr_1_msb, self.__reg_tone_fft_thr_1_lsb)
    @reg_tone_fft_thr_1.setter
    def reg_tone_fft_thr_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_fft_thr_1_msb, self.__reg_tone_fft_thr_1_lsb, value)

    @property
    def reg_tone_rm_en_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_rm_en_1_msb, self.__reg_tone_rm_en_1_lsb)
    @reg_tone_rm_en_1.setter
    def reg_tone_rm_en_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_rm_en_1_msb, self.__reg_tone_rm_en_1_lsb, value)

    @property
    def reg_tone_est_coef_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_est_coef_1_msb, self.__reg_tone_est_coef_1_lsb)
    @reg_tone_est_coef_1.setter
    def reg_tone_est_coef_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_est_coef_1_msb, self.__reg_tone_est_coef_1_lsb, value)
class TONE_CTRL_2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x18
        self.__reg_tone_shift_max_2_ht20_delta_lsb = 31
        self.__reg_tone_shift_max_2_ht20_delta_msb = 31
        self.__reg_tone_shift_max_2_fft_lsb = 28
        self.__reg_tone_shift_max_2_fft_msb = 30
        self.__reg_tone_shift_max_2_phi_lsb = 25
        self.__reg_tone_shift_max_2_phi_msb = 27
        self.__reg_tone_shift_max_2_agc_lsb = 22
        self.__reg_tone_shift_max_2_agc_msb = 24
        self.__reg_tone_fft_thr_2_lsb = 14
        self.__reg_tone_fft_thr_2_msb = 21
        self.__reg_tone_rm_en_2_lsb = 13
        self.__reg_tone_rm_en_2_msb = 13
        self.__reg_tone_est_coef_2_lsb = 0
        self.__reg_tone_est_coef_2_msb = 12
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tone_shift_max_2_ht20_delta(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_shift_max_2_ht20_delta_msb, self.__reg_tone_shift_max_2_ht20_delta_lsb)
    @reg_tone_shift_max_2_ht20_delta.setter
    def reg_tone_shift_max_2_ht20_delta(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_shift_max_2_ht20_delta_msb, self.__reg_tone_shift_max_2_ht20_delta_lsb, value)

    @property
    def reg_tone_shift_max_2_fft(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_shift_max_2_fft_msb, self.__reg_tone_shift_max_2_fft_lsb)
    @reg_tone_shift_max_2_fft.setter
    def reg_tone_shift_max_2_fft(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_shift_max_2_fft_msb, self.__reg_tone_shift_max_2_fft_lsb, value)

    @property
    def reg_tone_shift_max_2_phi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_shift_max_2_phi_msb, self.__reg_tone_shift_max_2_phi_lsb)
    @reg_tone_shift_max_2_phi.setter
    def reg_tone_shift_max_2_phi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_shift_max_2_phi_msb, self.__reg_tone_shift_max_2_phi_lsb, value)

    @property
    def reg_tone_shift_max_2_agc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_shift_max_2_agc_msb, self.__reg_tone_shift_max_2_agc_lsb)
    @reg_tone_shift_max_2_agc.setter
    def reg_tone_shift_max_2_agc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_shift_max_2_agc_msb, self.__reg_tone_shift_max_2_agc_lsb, value)

    @property
    def reg_tone_fft_thr_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_fft_thr_2_msb, self.__reg_tone_fft_thr_2_lsb)
    @reg_tone_fft_thr_2.setter
    def reg_tone_fft_thr_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_fft_thr_2_msb, self.__reg_tone_fft_thr_2_lsb, value)

    @property
    def reg_tone_rm_en_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_rm_en_2_msb, self.__reg_tone_rm_en_2_lsb)
    @reg_tone_rm_en_2.setter
    def reg_tone_rm_en_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_rm_en_2_msb, self.__reg_tone_rm_en_2_lsb, value)

    @property
    def reg_tone_est_coef_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_est_coef_2_msb, self.__reg_tone_est_coef_2_lsb)
    @reg_tone_est_coef_2.setter
    def reg_tone_est_coef_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_est_coef_2_msb, self.__reg_tone_est_coef_2_lsb, value)
class TONE_CTRL_3(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x1c
        self.__reg_tone_shift_max_3_ht20_delta_lsb = 31
        self.__reg_tone_shift_max_3_ht20_delta_msb = 31
        self.__reg_tone_shift_max_3_fft_lsb = 28
        self.__reg_tone_shift_max_3_fft_msb = 30
        self.__reg_tone_shift_max_3_phi_lsb = 25
        self.__reg_tone_shift_max_3_phi_msb = 27
        self.__reg_tone_shift_max_3_agc_lsb = 22
        self.__reg_tone_shift_max_3_agc_msb = 24
        self.__reg_tone_fft_thr_3_lsb = 14
        self.__reg_tone_fft_thr_3_msb = 21
        self.__reg_tone_rm_en_3_lsb = 13
        self.__reg_tone_rm_en_3_msb = 13
        self.__reg_tone_est_coef_3_lsb = 0
        self.__reg_tone_est_coef_3_msb = 12
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tone_shift_max_3_ht20_delta(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_shift_max_3_ht20_delta_msb, self.__reg_tone_shift_max_3_ht20_delta_lsb)
    @reg_tone_shift_max_3_ht20_delta.setter
    def reg_tone_shift_max_3_ht20_delta(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_shift_max_3_ht20_delta_msb, self.__reg_tone_shift_max_3_ht20_delta_lsb, value)

    @property
    def reg_tone_shift_max_3_fft(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_shift_max_3_fft_msb, self.__reg_tone_shift_max_3_fft_lsb)
    @reg_tone_shift_max_3_fft.setter
    def reg_tone_shift_max_3_fft(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_shift_max_3_fft_msb, self.__reg_tone_shift_max_3_fft_lsb, value)

    @property
    def reg_tone_shift_max_3_phi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_shift_max_3_phi_msb, self.__reg_tone_shift_max_3_phi_lsb)
    @reg_tone_shift_max_3_phi.setter
    def reg_tone_shift_max_3_phi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_shift_max_3_phi_msb, self.__reg_tone_shift_max_3_phi_lsb, value)

    @property
    def reg_tone_shift_max_3_agc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_shift_max_3_agc_msb, self.__reg_tone_shift_max_3_agc_lsb)
    @reg_tone_shift_max_3_agc.setter
    def reg_tone_shift_max_3_agc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_shift_max_3_agc_msb, self.__reg_tone_shift_max_3_agc_lsb, value)

    @property
    def reg_tone_fft_thr_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_fft_thr_3_msb, self.__reg_tone_fft_thr_3_lsb)
    @reg_tone_fft_thr_3.setter
    def reg_tone_fft_thr_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_fft_thr_3_msb, self.__reg_tone_fft_thr_3_lsb, value)

    @property
    def reg_tone_rm_en_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_rm_en_3_msb, self.__reg_tone_rm_en_3_lsb)
    @reg_tone_rm_en_3.setter
    def reg_tone_rm_en_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_rm_en_3_msb, self.__reg_tone_rm_en_3_lsb, value)

    @property
    def reg_tone_est_coef_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_est_coef_3_msb, self.__reg_tone_est_coef_3_lsb)
    @reg_tone_est_coef_3.setter
    def reg_tone_est_coef_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_est_coef_3_msb, self.__reg_tone_est_coef_3_lsb, value)
class TONE_CTRL_4(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x20
        self.__reg_tone_shift_max_4_ht20_delta_lsb = 31
        self.__reg_tone_shift_max_4_ht20_delta_msb = 31
        self.__reg_tone_shift_max_4_fft_lsb = 28
        self.__reg_tone_shift_max_4_fft_msb = 30
        self.__reg_tone_shift_max_4_phi_lsb = 25
        self.__reg_tone_shift_max_4_phi_msb = 27
        self.__reg_tone_shift_max_4_agc_lsb = 22
        self.__reg_tone_shift_max_4_agc_msb = 24
        self.__reg_tone_fft_thr_4_lsb = 14
        self.__reg_tone_fft_thr_4_msb = 21
        self.__reg_tone_rm_en_4_lsb = 13
        self.__reg_tone_rm_en_4_msb = 13
        self.__reg_tone_est_coef_4_lsb = 0
        self.__reg_tone_est_coef_4_msb = 12
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tone_shift_max_4_ht20_delta(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_shift_max_4_ht20_delta_msb, self.__reg_tone_shift_max_4_ht20_delta_lsb)
    @reg_tone_shift_max_4_ht20_delta.setter
    def reg_tone_shift_max_4_ht20_delta(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_shift_max_4_ht20_delta_msb, self.__reg_tone_shift_max_4_ht20_delta_lsb, value)

    @property
    def reg_tone_shift_max_4_fft(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_shift_max_4_fft_msb, self.__reg_tone_shift_max_4_fft_lsb)
    @reg_tone_shift_max_4_fft.setter
    def reg_tone_shift_max_4_fft(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_shift_max_4_fft_msb, self.__reg_tone_shift_max_4_fft_lsb, value)

    @property
    def reg_tone_shift_max_4_phi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_shift_max_4_phi_msb, self.__reg_tone_shift_max_4_phi_lsb)
    @reg_tone_shift_max_4_phi.setter
    def reg_tone_shift_max_4_phi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_shift_max_4_phi_msb, self.__reg_tone_shift_max_4_phi_lsb, value)

    @property
    def reg_tone_shift_max_4_agc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_shift_max_4_agc_msb, self.__reg_tone_shift_max_4_agc_lsb)
    @reg_tone_shift_max_4_agc.setter
    def reg_tone_shift_max_4_agc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_shift_max_4_agc_msb, self.__reg_tone_shift_max_4_agc_lsb, value)

    @property
    def reg_tone_fft_thr_4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_fft_thr_4_msb, self.__reg_tone_fft_thr_4_lsb)
    @reg_tone_fft_thr_4.setter
    def reg_tone_fft_thr_4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_fft_thr_4_msb, self.__reg_tone_fft_thr_4_lsb, value)

    @property
    def reg_tone_rm_en_4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_rm_en_4_msb, self.__reg_tone_rm_en_4_lsb)
    @reg_tone_rm_en_4.setter
    def reg_tone_rm_en_4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_rm_en_4_msb, self.__reg_tone_rm_en_4_lsb, value)

    @property
    def reg_tone_est_coef_4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_est_coef_4_msb, self.__reg_tone_est_coef_4_lsb)
    @reg_tone_est_coef_4.setter
    def reg_tone_est_coef_4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_est_coef_4_msb, self.__reg_tone_est_coef_4_lsb, value)
class TONE_CTRL_5(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x24
        self.__reg_dc_use_08us_lsb = 24
        self.__reg_dc_use_08us_msb = 25
        self.__reg_use_dc_coarse_en_lsb = 23
        self.__reg_use_dc_coarse_en_msb = 23
        self.__reg_use_dc_fine_en_lsb = 22
        self.__reg_use_dc_fine_en_msb = 22
        self.__reg_tone_swap_en_lsb = 21
        self.__reg_tone_swap_en_msb = 21
        self.__reg_tone_fft_latch_lsb = 20
        self.__reg_tone_fft_latch_msb = 20
        self.__reg_tone_sym_wait_lsb = 16
        self.__reg_tone_sym_wait_msb = 19
        self.__reg_tone_sym_wait_11n2nd_lsb = 12
        self.__reg_tone_sym_wait_11n2nd_msb = 15
        self.__reg_tone_sym_wait_en_lsb = 11
        self.__reg_tone_sym_wait_en_msb = 11
        self.__reg_11n_2nd_dis_dc_lsb = 10
        self.__reg_11n_2nd_dis_dc_msb = 10
        self.__reg_11n_2nd_dis_tone_lsb = 9
        self.__reg_11n_2nd_dis_tone_msb = 9
        self.__reg_tone_cnt_init_en_lsb = 8
        self.__reg_tone_cnt_init_en_msb = 8
        self.__reg_tone_cnt_init_lsb = 4
        self.__reg_tone_cnt_init_msb = 7
        self.__reg_tone_cnt_init_ht20_lsb = 0
        self.__reg_tone_cnt_init_ht20_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_dc_use_08us(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_use_08us_msb, self.__reg_dc_use_08us_lsb)
    @reg_dc_use_08us.setter
    def reg_dc_use_08us(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_use_08us_msb, self.__reg_dc_use_08us_lsb, value)

    @property
    def reg_use_dc_coarse_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_use_dc_coarse_en_msb, self.__reg_use_dc_coarse_en_lsb)
    @reg_use_dc_coarse_en.setter
    def reg_use_dc_coarse_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_use_dc_coarse_en_msb, self.__reg_use_dc_coarse_en_lsb, value)

    @property
    def reg_use_dc_fine_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_use_dc_fine_en_msb, self.__reg_use_dc_fine_en_lsb)
    @reg_use_dc_fine_en.setter
    def reg_use_dc_fine_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_use_dc_fine_en_msb, self.__reg_use_dc_fine_en_lsb, value)

    @property
    def reg_tone_swap_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_swap_en_msb, self.__reg_tone_swap_en_lsb)
    @reg_tone_swap_en.setter
    def reg_tone_swap_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_swap_en_msb, self.__reg_tone_swap_en_lsb, value)

    @property
    def reg_tone_fft_latch(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_fft_latch_msb, self.__reg_tone_fft_latch_lsb)
    @reg_tone_fft_latch.setter
    def reg_tone_fft_latch(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_fft_latch_msb, self.__reg_tone_fft_latch_lsb, value)

    @property
    def reg_tone_sym_wait(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_sym_wait_msb, self.__reg_tone_sym_wait_lsb)
    @reg_tone_sym_wait.setter
    def reg_tone_sym_wait(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_sym_wait_msb, self.__reg_tone_sym_wait_lsb, value)

    @property
    def reg_tone_sym_wait_11n2nd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_sym_wait_11n2nd_msb, self.__reg_tone_sym_wait_11n2nd_lsb)
    @reg_tone_sym_wait_11n2nd.setter
    def reg_tone_sym_wait_11n2nd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_sym_wait_11n2nd_msb, self.__reg_tone_sym_wait_11n2nd_lsb, value)

    @property
    def reg_tone_sym_wait_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_sym_wait_en_msb, self.__reg_tone_sym_wait_en_lsb)
    @reg_tone_sym_wait_en.setter
    def reg_tone_sym_wait_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_sym_wait_en_msb, self.__reg_tone_sym_wait_en_lsb, value)

    @property
    def reg_11n_2nd_dis_dc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_11n_2nd_dis_dc_msb, self.__reg_11n_2nd_dis_dc_lsb)
    @reg_11n_2nd_dis_dc.setter
    def reg_11n_2nd_dis_dc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_11n_2nd_dis_dc_msb, self.__reg_11n_2nd_dis_dc_lsb, value)

    @property
    def reg_11n_2nd_dis_tone(self):
        return self.__MEM.rdm(self.__addr, self.__reg_11n_2nd_dis_tone_msb, self.__reg_11n_2nd_dis_tone_lsb)
    @reg_11n_2nd_dis_tone.setter
    def reg_11n_2nd_dis_tone(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_11n_2nd_dis_tone_msb, self.__reg_11n_2nd_dis_tone_lsb, value)

    @property
    def reg_tone_cnt_init_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_cnt_init_en_msb, self.__reg_tone_cnt_init_en_lsb)
    @reg_tone_cnt_init_en.setter
    def reg_tone_cnt_init_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_cnt_init_en_msb, self.__reg_tone_cnt_init_en_lsb, value)

    @property
    def reg_tone_cnt_init(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_cnt_init_msb, self.__reg_tone_cnt_init_lsb)
    @reg_tone_cnt_init.setter
    def reg_tone_cnt_init(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_cnt_init_msb, self.__reg_tone_cnt_init_lsb, value)

    @property
    def reg_tone_cnt_init_ht20(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_cnt_init_ht20_msb, self.__reg_tone_cnt_init_ht20_lsb)
    @reg_tone_cnt_init_ht20.setter
    def reg_tone_cnt_init_ht20(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_cnt_init_ht20_msb, self.__reg_tone_cnt_init_ht20_lsb, value)
class BB_RESET(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x28
        self.__reg_bbclk_en_lsb = 15
        self.__reg_bbclk_en_msb = 15
        self.__reg_test8_rst_lsb = 14
        self.__reg_test8_rst_msb = 14
        self.__reg_test7_rst_lsb = 13
        self.__reg_test7_rst_msb = 13
        self.__reg_test6_rst_lsb = 12
        self.__reg_test6_rst_msb = 12
        self.__reg_test5_rst_lsb = 11
        self.__reg_test5_rst_msb = 11
        self.__reg_test4_rst_lsb = 10
        self.__reg_test4_rst_msb = 10
        self.__reg_test3_rst_lsb = 9
        self.__reg_test3_rst_msb = 9
        self.__reg_test2_rst_lsb = 8
        self.__reg_test2_rst_msb = 8
        self.__reg_test1_rst_lsb = 7
        self.__reg_test1_rst_msb = 7
        self.__reg_test0_rst_lsb = 6
        self.__reg_test0_rst_msb = 6
        self.__reg_brx_rst_lsb = 5
        self.__reg_brx_rst_msb = 5
        self.__reg_agc_rst_lsb = 4
        self.__reg_agc_rst_msb = 4
        self.__reg_tx_rst_lsb = 3
        self.__reg_tx_rst_msb = 3
        self.__reg_nrx_rst_lsb = 2
        self.__reg_nrx_rst_msb = 2
        self.__reg_fsm_rst_lsb = 1
        self.__reg_fsm_rst_msb = 1
        self.__reg_fft_rst_lsb = 0
        self.__reg_fft_rst_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bbclk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbclk_en_msb, self.__reg_bbclk_en_lsb)
    @reg_bbclk_en.setter
    def reg_bbclk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbclk_en_msb, self.__reg_bbclk_en_lsb, value)

    @property
    def reg_test8_rst(self):
        return self.__MEM.rdm(self.__addr, self.__reg_test8_rst_msb, self.__reg_test8_rst_lsb)
    @reg_test8_rst.setter
    def reg_test8_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_test8_rst_msb, self.__reg_test8_rst_lsb, value)

    @property
    def reg_test7_rst(self):
        return self.__MEM.rdm(self.__addr, self.__reg_test7_rst_msb, self.__reg_test7_rst_lsb)
    @reg_test7_rst.setter
    def reg_test7_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_test7_rst_msb, self.__reg_test7_rst_lsb, value)

    @property
    def reg_test6_rst(self):
        return self.__MEM.rdm(self.__addr, self.__reg_test6_rst_msb, self.__reg_test6_rst_lsb)
    @reg_test6_rst.setter
    def reg_test6_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_test6_rst_msb, self.__reg_test6_rst_lsb, value)

    @property
    def reg_test5_rst(self):
        return self.__MEM.rdm(self.__addr, self.__reg_test5_rst_msb, self.__reg_test5_rst_lsb)
    @reg_test5_rst.setter
    def reg_test5_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_test5_rst_msb, self.__reg_test5_rst_lsb, value)

    @property
    def reg_test4_rst(self):
        return self.__MEM.rdm(self.__addr, self.__reg_test4_rst_msb, self.__reg_test4_rst_lsb)
    @reg_test4_rst.setter
    def reg_test4_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_test4_rst_msb, self.__reg_test4_rst_lsb, value)

    @property
    def reg_test3_rst(self):
        return self.__MEM.rdm(self.__addr, self.__reg_test3_rst_msb, self.__reg_test3_rst_lsb)
    @reg_test3_rst.setter
    def reg_test3_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_test3_rst_msb, self.__reg_test3_rst_lsb, value)

    @property
    def reg_test2_rst(self):
        return self.__MEM.rdm(self.__addr, self.__reg_test2_rst_msb, self.__reg_test2_rst_lsb)
    @reg_test2_rst.setter
    def reg_test2_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_test2_rst_msb, self.__reg_test2_rst_lsb, value)

    @property
    def reg_test1_rst(self):
        return self.__MEM.rdm(self.__addr, self.__reg_test1_rst_msb, self.__reg_test1_rst_lsb)
    @reg_test1_rst.setter
    def reg_test1_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_test1_rst_msb, self.__reg_test1_rst_lsb, value)

    @property
    def reg_test0_rst(self):
        return self.__MEM.rdm(self.__addr, self.__reg_test0_rst_msb, self.__reg_test0_rst_lsb)
    @reg_test0_rst.setter
    def reg_test0_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_test0_rst_msb, self.__reg_test0_rst_lsb, value)

    @property
    def reg_brx_rst(self):
        return self.__MEM.rdm(self.__addr, self.__reg_brx_rst_msb, self.__reg_brx_rst_lsb)
    @reg_brx_rst.setter
    def reg_brx_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_brx_rst_msb, self.__reg_brx_rst_lsb, value)

    @property
    def reg_agc_rst(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_rst_msb, self.__reg_agc_rst_lsb)
    @reg_agc_rst.setter
    def reg_agc_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_rst_msb, self.__reg_agc_rst_lsb, value)

    @property
    def reg_tx_rst(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_rst_msb, self.__reg_tx_rst_lsb)
    @reg_tx_rst.setter
    def reg_tx_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_rst_msb, self.__reg_tx_rst_lsb, value)

    @property
    def reg_nrx_rst(self):
        return self.__MEM.rdm(self.__addr, self.__reg_nrx_rst_msb, self.__reg_nrx_rst_lsb)
    @reg_nrx_rst.setter
    def reg_nrx_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_nrx_rst_msb, self.__reg_nrx_rst_lsb, value)

    @property
    def reg_fsm_rst(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fsm_rst_msb, self.__reg_fsm_rst_lsb)
    @reg_fsm_rst.setter
    def reg_fsm_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fsm_rst_msb, self.__reg_fsm_rst_lsb, value)

    @property
    def reg_fft_rst(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fft_rst_msb, self.__reg_fft_rst_lsb)
    @reg_fft_rst.setter
    def reg_fft_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fft_rst_msb, self.__reg_fft_rst_lsb, value)
class TONE_CTRL_6(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x2c
        self.__reg_tone_est_fb_en_4_lsb = 26
        self.__reg_tone_est_fb_en_4_msb = 26
        self.__reg_tone_est_fb_out_en_4_lsb = 25
        self.__reg_tone_est_fb_out_en_4_msb = 25
        self.__reg_tone_est_fb_en_3_lsb = 24
        self.__reg_tone_est_fb_en_3_msb = 24
        self.__reg_tone_est_fb_out_en_3_lsb = 23
        self.__reg_tone_est_fb_out_en_3_msb = 23
        self.__reg_tone_est_fb_en_2_lsb = 22
        self.__reg_tone_est_fb_en_2_msb = 22
        self.__reg_tone_est_fb_out_en_2_lsb = 21
        self.__reg_tone_est_fb_out_en_2_msb = 21
        self.__reg_tone_est_fb_en_1_lsb = 20
        self.__reg_tone_est_fb_en_1_msb = 20
        self.__reg_tone_est_fb_out_en_1_lsb = 19
        self.__reg_tone_est_fb_out_en_1_msb = 19
        self.__reg_tone_est_coef_4_lsb_lsb = 16
        self.__reg_tone_est_coef_4_lsb_msb = 18
        self.__reg_tone_est_coef_3_lsb_lsb = 13
        self.__reg_tone_est_coef_3_lsb_msb = 15
        self.__reg_tone_est_coef_2_lsb_lsb = 10
        self.__reg_tone_est_coef_2_lsb_msb = 12
        self.__reg_tone_est_coef_1_lsb_lsb = 7
        self.__reg_tone_est_coef_1_lsb_msb = 9
        self.__reg_demod_tone_gain_thr_lsb = 0
        self.__reg_demod_tone_gain_thr_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tone_est_fb_en_4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_est_fb_en_4_msb, self.__reg_tone_est_fb_en_4_lsb)
    @reg_tone_est_fb_en_4.setter
    def reg_tone_est_fb_en_4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_est_fb_en_4_msb, self.__reg_tone_est_fb_en_4_lsb, value)

    @property
    def reg_tone_est_fb_out_en_4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_est_fb_out_en_4_msb, self.__reg_tone_est_fb_out_en_4_lsb)
    @reg_tone_est_fb_out_en_4.setter
    def reg_tone_est_fb_out_en_4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_est_fb_out_en_4_msb, self.__reg_tone_est_fb_out_en_4_lsb, value)

    @property
    def reg_tone_est_fb_en_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_est_fb_en_3_msb, self.__reg_tone_est_fb_en_3_lsb)
    @reg_tone_est_fb_en_3.setter
    def reg_tone_est_fb_en_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_est_fb_en_3_msb, self.__reg_tone_est_fb_en_3_lsb, value)

    @property
    def reg_tone_est_fb_out_en_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_est_fb_out_en_3_msb, self.__reg_tone_est_fb_out_en_3_lsb)
    @reg_tone_est_fb_out_en_3.setter
    def reg_tone_est_fb_out_en_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_est_fb_out_en_3_msb, self.__reg_tone_est_fb_out_en_3_lsb, value)

    @property
    def reg_tone_est_fb_en_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_est_fb_en_2_msb, self.__reg_tone_est_fb_en_2_lsb)
    @reg_tone_est_fb_en_2.setter
    def reg_tone_est_fb_en_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_est_fb_en_2_msb, self.__reg_tone_est_fb_en_2_lsb, value)

    @property
    def reg_tone_est_fb_out_en_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_est_fb_out_en_2_msb, self.__reg_tone_est_fb_out_en_2_lsb)
    @reg_tone_est_fb_out_en_2.setter
    def reg_tone_est_fb_out_en_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_est_fb_out_en_2_msb, self.__reg_tone_est_fb_out_en_2_lsb, value)

    @property
    def reg_tone_est_fb_en_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_est_fb_en_1_msb, self.__reg_tone_est_fb_en_1_lsb)
    @reg_tone_est_fb_en_1.setter
    def reg_tone_est_fb_en_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_est_fb_en_1_msb, self.__reg_tone_est_fb_en_1_lsb, value)

    @property
    def reg_tone_est_fb_out_en_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_est_fb_out_en_1_msb, self.__reg_tone_est_fb_out_en_1_lsb)
    @reg_tone_est_fb_out_en_1.setter
    def reg_tone_est_fb_out_en_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_est_fb_out_en_1_msb, self.__reg_tone_est_fb_out_en_1_lsb, value)

    @property
    def reg_tone_est_coef_4_lsb(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_est_coef_4_lsb_msb, self.__reg_tone_est_coef_4_lsb_lsb)
    @reg_tone_est_coef_4_lsb.setter
    def reg_tone_est_coef_4_lsb(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_est_coef_4_lsb_msb, self.__reg_tone_est_coef_4_lsb_lsb, value)

    @property
    def reg_tone_est_coef_3_lsb(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_est_coef_3_lsb_msb, self.__reg_tone_est_coef_3_lsb_lsb)
    @reg_tone_est_coef_3_lsb.setter
    def reg_tone_est_coef_3_lsb(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_est_coef_3_lsb_msb, self.__reg_tone_est_coef_3_lsb_lsb, value)

    @property
    def reg_tone_est_coef_2_lsb(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_est_coef_2_lsb_msb, self.__reg_tone_est_coef_2_lsb_lsb)
    @reg_tone_est_coef_2_lsb.setter
    def reg_tone_est_coef_2_lsb(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_est_coef_2_lsb_msb, self.__reg_tone_est_coef_2_lsb_lsb, value)

    @property
    def reg_tone_est_coef_1_lsb(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_est_coef_1_lsb_msb, self.__reg_tone_est_coef_1_lsb_lsb)
    @reg_tone_est_coef_1_lsb.setter
    def reg_tone_est_coef_1_lsb(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_est_coef_1_lsb_msb, self.__reg_tone_est_coef_1_lsb_lsb, value)

    @property
    def reg_demod_tone_gain_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_demod_tone_gain_thr_msb, self.__reg_demod_tone_gain_thr_lsb)
    @reg_demod_tone_gain_thr.setter
    def reg_demod_tone_gain_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_demod_tone_gain_thr_msb, self.__reg_demod_tone_gain_thr_lsb, value)
class BB_FSM_CTRL(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x30
        self.__reg_agc_err_exit_en_lsb = 10
        self.__reg_agc_err_exit_en_msb = 10
        self.__reg_tx_wait_delay_lsb = 0
        self.__reg_tx_wait_delay_msb = 9
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_agc_err_exit_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_err_exit_en_msb, self.__reg_agc_err_exit_en_lsb)
    @reg_agc_err_exit_en.setter
    def reg_agc_err_exit_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_err_exit_en_msb, self.__reg_agc_err_exit_en_lsb, value)

    @property
    def reg_tx_wait_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_wait_delay_msb, self.__reg_tx_wait_delay_lsb)
    @reg_tx_wait_delay.setter
    def reg_tx_wait_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_wait_delay_msb, self.__reg_tx_wait_delay_lsb, value)
class DCDELTACONF0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x34
        self.__reg_dc_est_clk_force_lsb = 24
        self.__reg_dc_est_clk_force_msb = 24
        self.__reg_dc_est_sel_lsb = 22
        self.__reg_dc_est_sel_msb = 23
        self.__reg_dc_corr_clk_sel_lsb = 20
        self.__reg_dc_corr_clk_sel_msb = 21
        self.__reg_dc_delay_cnt_lsb = 8
        self.__reg_dc_delay_cnt_msb = 19
        self.__reg_dc_corr_delay_cycle_lsb = 0
        self.__reg_dc_corr_delay_cycle_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_dc_est_clk_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_est_clk_force_msb, self.__reg_dc_est_clk_force_lsb)
    @reg_dc_est_clk_force.setter
    def reg_dc_est_clk_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_est_clk_force_msb, self.__reg_dc_est_clk_force_lsb, value)

    @property
    def reg_dc_est_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_est_sel_msb, self.__reg_dc_est_sel_lsb)
    @reg_dc_est_sel.setter
    def reg_dc_est_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_est_sel_msb, self.__reg_dc_est_sel_lsb, value)

    @property
    def reg_dc_corr_clk_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_corr_clk_sel_msb, self.__reg_dc_corr_clk_sel_lsb)
    @reg_dc_corr_clk_sel.setter
    def reg_dc_corr_clk_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_corr_clk_sel_msb, self.__reg_dc_corr_clk_sel_lsb, value)

    @property
    def reg_dc_delay_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_delay_cnt_msb, self.__reg_dc_delay_cnt_lsb)
    @reg_dc_delay_cnt.setter
    def reg_dc_delay_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_delay_cnt_msb, self.__reg_dc_delay_cnt_lsb, value)

    @property
    def reg_dc_corr_delay_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_corr_delay_cycle_msb, self.__reg_dc_corr_delay_cycle_lsb)
    @reg_dc_corr_delay_cycle.setter
    def reg_dc_corr_delay_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_corr_delay_cycle_msb, self.__reg_dc_corr_delay_cycle_lsb, value)
class DCDELTACONF1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x38
        self.__reg_dc_est_corr_en_force_lsb = 27
        self.__reg_dc_est_corr_en_force_msb = 27
        self.__reg_dc_est_corr_en_lsb = 26
        self.__reg_dc_est_corr_en_msb = 26
        self.__phi_delta_est_done_lsb = 25
        self.__phi_delta_est_done_msb = 25
        self.__phi_delta_est_lsb = 12
        self.__phi_delta_est_msb = 24
        self.__reg_dc_est_corr_len_lsb = 0
        self.__reg_dc_est_corr_len_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_dc_est_corr_en_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_est_corr_en_force_msb, self.__reg_dc_est_corr_en_force_lsb)
    @reg_dc_est_corr_en_force.setter
    def reg_dc_est_corr_en_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_est_corr_en_force_msb, self.__reg_dc_est_corr_en_force_lsb, value)

    @property
    def reg_dc_est_corr_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_est_corr_en_msb, self.__reg_dc_est_corr_en_lsb)
    @reg_dc_est_corr_en.setter
    def reg_dc_est_corr_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_est_corr_en_msb, self.__reg_dc_est_corr_en_lsb, value)

    @property
    def phi_delta_est_done(self):
        return self.__MEM.rdm(self.__addr, self.__phi_delta_est_done_msb, self.__phi_delta_est_done_lsb)
    @phi_delta_est_done.setter
    def phi_delta_est_done(self, value):
        return self.__MEM.wrm(self.__addr, self.__phi_delta_est_done_msb, self.__phi_delta_est_done_lsb, value)

    @property
    def phi_delta_est(self):
        return self.__MEM.rdm(self.__addr, self.__phi_delta_est_msb, self.__phi_delta_est_lsb)
    @phi_delta_est.setter
    def phi_delta_est(self, value):
        return self.__MEM.wrm(self.__addr, self.__phi_delta_est_msb, self.__phi_delta_est_lsb, value)

    @property
    def reg_dc_est_corr_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_est_corr_len_msb, self.__reg_dc_est_corr_len_lsb)
    @reg_dc_est_corr_len.setter
    def reg_dc_est_corr_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_est_corr_len_msb, self.__reg_dc_est_corr_len_lsb, value)
class BB_WDG_0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x3c
        self.__reg_bb_wdg_busy_chk_lsb = 31
        self.__reg_bb_wdg_busy_chk_msb = 31
        self.__reg_bb_wdg_srch_chk_lsb = 30
        self.__reg_bb_wdg_srch_chk_msb = 30
        self.__reg_bb_wdg_max_busy_lsb = 16
        self.__reg_bb_wdg_max_busy_msb = 29
        self.__reg_bb_wdg_max_srch_lsb = 0
        self.__reg_bb_wdg_max_srch_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bb_wdg_busy_chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_wdg_busy_chk_msb, self.__reg_bb_wdg_busy_chk_lsb)
    @reg_bb_wdg_busy_chk.setter
    def reg_bb_wdg_busy_chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_wdg_busy_chk_msb, self.__reg_bb_wdg_busy_chk_lsb, value)

    @property
    def reg_bb_wdg_srch_chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_wdg_srch_chk_msb, self.__reg_bb_wdg_srch_chk_lsb)
    @reg_bb_wdg_srch_chk.setter
    def reg_bb_wdg_srch_chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_wdg_srch_chk_msb, self.__reg_bb_wdg_srch_chk_lsb, value)

    @property
    def reg_bb_wdg_max_busy(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_wdg_max_busy_msb, self.__reg_bb_wdg_max_busy_lsb)
    @reg_bb_wdg_max_busy.setter
    def reg_bb_wdg_max_busy(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_wdg_max_busy_msb, self.__reg_bb_wdg_max_busy_lsb, value)

    @property
    def reg_bb_wdg_max_srch(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_wdg_max_srch_msb, self.__reg_bb_wdg_max_srch_lsb)
    @reg_bb_wdg_max_srch.setter
    def reg_bb_wdg_max_srch(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_wdg_max_srch_msb, self.__reg_bb_wdg_max_srch_lsb, value)
class BB_WDG_1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x40
        self.__reg_bb_wdg_rst_en_lsb = 31
        self.__reg_bb_wdg_rst_en_msb = 31
        self.__reg_bb_wdg_int_en_lsb = 30
        self.__reg_bb_wdg_int_en_msb = 30
        self.__reg_bb_wdg_clr_lsb = 29
        self.__reg_bb_wdg_clr_msb = 29
        self.__r_bb_wdg_flag_lsb = 28
        self.__r_bb_wdg_flag_msb = 28
        self.__r_bb_wdg_status_lsb = 0
        self.__r_bb_wdg_status_msb = 27
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bb_wdg_rst_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_wdg_rst_en_msb, self.__reg_bb_wdg_rst_en_lsb)
    @reg_bb_wdg_rst_en.setter
    def reg_bb_wdg_rst_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_wdg_rst_en_msb, self.__reg_bb_wdg_rst_en_lsb, value)

    @property
    def reg_bb_wdg_int_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_wdg_int_en_msb, self.__reg_bb_wdg_int_en_lsb)
    @reg_bb_wdg_int_en.setter
    def reg_bb_wdg_int_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_wdg_int_en_msb, self.__reg_bb_wdg_int_en_lsb, value)

    @property
    def reg_bb_wdg_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_wdg_clr_msb, self.__reg_bb_wdg_clr_lsb)
    @reg_bb_wdg_clr.setter
    def reg_bb_wdg_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_wdg_clr_msb, self.__reg_bb_wdg_clr_lsb, value)

    @property
    def r_bb_wdg_flag(self):
        return self.__MEM.rdm(self.__addr, self.__r_bb_wdg_flag_msb, self.__r_bb_wdg_flag_lsb)
    @r_bb_wdg_flag.setter
    def r_bb_wdg_flag(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_bb_wdg_flag_msb, self.__r_bb_wdg_flag_lsb, value)

    @property
    def r_bb_wdg_status(self):
        return self.__MEM.rdm(self.__addr, self.__r_bb_wdg_status_msb, self.__r_bb_wdg_status_lsb)
    @r_bb_wdg_status.setter
    def r_bb_wdg_status(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_bb_wdg_status_msb, self.__r_bb_wdg_status_lsb, value)
class BB_INT_ENA(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x44
        self.__tone_est_fft_done_int_ena_lsb = 5
        self.__tone_est_fft_done_int_ena_msb = 5
        self.__tone_est_req_int_ena_lsb = 4
        self.__tone_est_req_int_ena_msb = 4
        self.__tone_est_auto_done_int_ena_lsb = 3
        self.__tone_est_auto_done_int_ena_msb = 3
        self.__bb_timer_int_ena_lsb = 2
        self.__bb_timer_int_ena_msb = 2
        self.__dc_int_ena_lsb = 1
        self.__dc_int_ena_msb = 1
        self.__noise_int_ena_lsb = 0
        self.__noise_int_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tone_est_fft_done_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__tone_est_fft_done_int_ena_msb, self.__tone_est_fft_done_int_ena_lsb)
    @tone_est_fft_done_int_ena.setter
    def tone_est_fft_done_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__tone_est_fft_done_int_ena_msb, self.__tone_est_fft_done_int_ena_lsb, value)

    @property
    def tone_est_req_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__tone_est_req_int_ena_msb, self.__tone_est_req_int_ena_lsb)
    @tone_est_req_int_ena.setter
    def tone_est_req_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__tone_est_req_int_ena_msb, self.__tone_est_req_int_ena_lsb, value)

    @property
    def tone_est_auto_done_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__tone_est_auto_done_int_ena_msb, self.__tone_est_auto_done_int_ena_lsb)
    @tone_est_auto_done_int_ena.setter
    def tone_est_auto_done_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__tone_est_auto_done_int_ena_msb, self.__tone_est_auto_done_int_ena_lsb, value)

    @property
    def bb_timer_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__bb_timer_int_ena_msb, self.__bb_timer_int_ena_lsb)
    @bb_timer_int_ena.setter
    def bb_timer_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__bb_timer_int_ena_msb, self.__bb_timer_int_ena_lsb, value)

    @property
    def dc_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__dc_int_ena_msb, self.__dc_int_ena_lsb)
    @dc_int_ena.setter
    def dc_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__dc_int_ena_msb, self.__dc_int_ena_lsb, value)

    @property
    def noise_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__noise_int_ena_msb, self.__noise_int_ena_lsb)
    @noise_int_ena.setter
    def noise_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__noise_int_ena_msb, self.__noise_int_ena_lsb, value)
class BB_INT_RAW(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x48
        self.__tone_est_fft_done_int_raw_lsb = 5
        self.__tone_est_fft_done_int_raw_msb = 5
        self.__tone_est_req_int_raw_lsb = 4
        self.__tone_est_req_int_raw_msb = 4
        self.__tone_est_auto_done_int_raw_lsb = 3
        self.__tone_est_auto_done_int_raw_msb = 3
        self.__bb_timer_int_raw_lsb = 2
        self.__bb_timer_int_raw_msb = 2
        self.__dc_int_raw_lsb = 1
        self.__dc_int_raw_msb = 1
        self.__noise_int_raw_lsb = 0
        self.__noise_int_raw_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tone_est_fft_done_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__tone_est_fft_done_int_raw_msb, self.__tone_est_fft_done_int_raw_lsb)
    @tone_est_fft_done_int_raw.setter
    def tone_est_fft_done_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__tone_est_fft_done_int_raw_msb, self.__tone_est_fft_done_int_raw_lsb, value)

    @property
    def tone_est_req_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__tone_est_req_int_raw_msb, self.__tone_est_req_int_raw_lsb)
    @tone_est_req_int_raw.setter
    def tone_est_req_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__tone_est_req_int_raw_msb, self.__tone_est_req_int_raw_lsb, value)

    @property
    def tone_est_auto_done_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__tone_est_auto_done_int_raw_msb, self.__tone_est_auto_done_int_raw_lsb)
    @tone_est_auto_done_int_raw.setter
    def tone_est_auto_done_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__tone_est_auto_done_int_raw_msb, self.__tone_est_auto_done_int_raw_lsb, value)

    @property
    def bb_timer_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__bb_timer_int_raw_msb, self.__bb_timer_int_raw_lsb)
    @bb_timer_int_raw.setter
    def bb_timer_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__bb_timer_int_raw_msb, self.__bb_timer_int_raw_lsb, value)

    @property
    def dc_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__dc_int_raw_msb, self.__dc_int_raw_lsb)
    @dc_int_raw.setter
    def dc_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__dc_int_raw_msb, self.__dc_int_raw_lsb, value)

    @property
    def noise_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__noise_int_raw_msb, self.__noise_int_raw_lsb)
    @noise_int_raw.setter
    def noise_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__noise_int_raw_msb, self.__noise_int_raw_lsb, value)
class BB_INT_ST(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x4c
        self.__tone_est_fft_done_int_st_lsb = 5
        self.__tone_est_fft_done_int_st_msb = 5
        self.__tone_est_req_int_st_lsb = 4
        self.__tone_est_req_int_st_msb = 4
        self.__tone_est_auto_done_int_st_lsb = 3
        self.__tone_est_auto_done_int_st_msb = 3
        self.__bb_timer_int_st_lsb = 2
        self.__bb_timer_int_st_msb = 2
        self.__dc_int_st_lsb = 1
        self.__dc_int_st_msb = 1
        self.__noise_int_st_lsb = 0
        self.__noise_int_st_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tone_est_fft_done_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__tone_est_fft_done_int_st_msb, self.__tone_est_fft_done_int_st_lsb)
    @tone_est_fft_done_int_st.setter
    def tone_est_fft_done_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__tone_est_fft_done_int_st_msb, self.__tone_est_fft_done_int_st_lsb, value)

    @property
    def tone_est_req_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__tone_est_req_int_st_msb, self.__tone_est_req_int_st_lsb)
    @tone_est_req_int_st.setter
    def tone_est_req_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__tone_est_req_int_st_msb, self.__tone_est_req_int_st_lsb, value)

    @property
    def tone_est_auto_done_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__tone_est_auto_done_int_st_msb, self.__tone_est_auto_done_int_st_lsb)
    @tone_est_auto_done_int_st.setter
    def tone_est_auto_done_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__tone_est_auto_done_int_st_msb, self.__tone_est_auto_done_int_st_lsb, value)

    @property
    def bb_timer_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__bb_timer_int_st_msb, self.__bb_timer_int_st_lsb)
    @bb_timer_int_st.setter
    def bb_timer_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__bb_timer_int_st_msb, self.__bb_timer_int_st_lsb, value)

    @property
    def dc_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__dc_int_st_msb, self.__dc_int_st_lsb)
    @dc_int_st.setter
    def dc_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__dc_int_st_msb, self.__dc_int_st_lsb, value)

    @property
    def noise_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__noise_int_st_msb, self.__noise_int_st_lsb)
    @noise_int_st.setter
    def noise_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__noise_int_st_msb, self.__noise_int_st_lsb, value)
class BB_INT_CLR(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x50
        self.__tone_est_fft_done_int_clr_lsb = 5
        self.__tone_est_fft_done_int_clr_msb = 5
        self.__tone_est_req_int_clr_lsb = 4
        self.__tone_est_req_int_clr_msb = 4
        self.__tone_est_auto_done_int_clr_lsb = 3
        self.__tone_est_auto_done_int_clr_msb = 3
        self.__bb_timer_int_clr_lsb = 2
        self.__bb_timer_int_clr_msb = 2
        self.__dc_int_clr_lsb = 1
        self.__dc_int_clr_msb = 1
        self.__noise_int_clr_lsb = 0
        self.__noise_int_clr_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tone_est_fft_done_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__tone_est_fft_done_int_clr_msb, self.__tone_est_fft_done_int_clr_lsb)
    @tone_est_fft_done_int_clr.setter
    def tone_est_fft_done_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__tone_est_fft_done_int_clr_msb, self.__tone_est_fft_done_int_clr_lsb, value)

    @property
    def tone_est_req_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__tone_est_req_int_clr_msb, self.__tone_est_req_int_clr_lsb)
    @tone_est_req_int_clr.setter
    def tone_est_req_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__tone_est_req_int_clr_msb, self.__tone_est_req_int_clr_lsb, value)

    @property
    def tone_est_auto_done_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__tone_est_auto_done_int_clr_msb, self.__tone_est_auto_done_int_clr_lsb)
    @tone_est_auto_done_int_clr.setter
    def tone_est_auto_done_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__tone_est_auto_done_int_clr_msb, self.__tone_est_auto_done_int_clr_lsb, value)

    @property
    def bb_timer_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__bb_timer_int_clr_msb, self.__bb_timer_int_clr_lsb)
    @bb_timer_int_clr.setter
    def bb_timer_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__bb_timer_int_clr_msb, self.__bb_timer_int_clr_lsb, value)

    @property
    def dc_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__dc_int_clr_msb, self.__dc_int_clr_lsb)
    @dc_int_clr.setter
    def dc_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__dc_int_clr_msb, self.__dc_int_clr_lsb, value)

    @property
    def noise_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__noise_int_clr_msb, self.__noise_int_clr_lsb)
    @noise_int_clr.setter
    def noise_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__noise_int_clr_msb, self.__noise_int_clr_lsb, value)
class BBPD_CTRL(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x54
        self.__reg_fft_force_pu_lsb = 3
        self.__reg_fft_force_pu_msb = 3
        self.__reg_fft_force_pd_lsb = 2
        self.__reg_fft_force_pd_msb = 2
        self.__reg_dc_est_force_pu_lsb = 1
        self.__reg_dc_est_force_pu_msb = 1
        self.__reg_dc_est_force_pd_lsb = 0
        self.__reg_dc_est_force_pd_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_fft_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fft_force_pu_msb, self.__reg_fft_force_pu_lsb)
    @reg_fft_force_pu.setter
    def reg_fft_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fft_force_pu_msb, self.__reg_fft_force_pu_lsb, value)

    @property
    def reg_fft_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fft_force_pd_msb, self.__reg_fft_force_pd_lsb)
    @reg_fft_force_pd.setter
    def reg_fft_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fft_force_pd_msb, self.__reg_fft_force_pd_lsb, value)

    @property
    def reg_dc_est_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_est_force_pu_msb, self.__reg_dc_est_force_pu_lsb)
    @reg_dc_est_force_pu.setter
    def reg_dc_est_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_est_force_pu_msb, self.__reg_dc_est_force_pu_lsb, value)

    @property
    def reg_dc_est_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_est_force_pd_msb, self.__reg_dc_est_force_pd_lsb)
    @reg_dc_est_force_pd.setter
    def reg_dc_est_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_est_force_pd_msb, self.__reg_dc_est_force_pd_lsb, value)
class BB_CCA_CTRL_0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x58
        self.__reg_cca_cnt_pri_car_lsb = 31
        self.__reg_cca_cnt_pri_car_msb = 31
        self.__reg_cca_cnt_sec_car_lsb = 30
        self.__reg_cca_cnt_sec_car_msb = 30
        self.__reg_cca_cnt_txrx_lsb = 29
        self.__reg_cca_cnt_txrx_msb = 29
        self.__reg_cca_timer_clr_lsb = 28
        self.__reg_cca_timer_clr_msb = 28
        self.__reg_bb_timer_clr_lsb = 27
        self.__reg_bb_timer_clr_msb = 27
        self.__reg_bb_timer_max_lsb = 0
        self.__reg_bb_timer_max_msb = 26
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_cca_cnt_pri_car(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cca_cnt_pri_car_msb, self.__reg_cca_cnt_pri_car_lsb)
    @reg_cca_cnt_pri_car.setter
    def reg_cca_cnt_pri_car(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cca_cnt_pri_car_msb, self.__reg_cca_cnt_pri_car_lsb, value)

    @property
    def reg_cca_cnt_sec_car(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cca_cnt_sec_car_msb, self.__reg_cca_cnt_sec_car_lsb)
    @reg_cca_cnt_sec_car.setter
    def reg_cca_cnt_sec_car(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cca_cnt_sec_car_msb, self.__reg_cca_cnt_sec_car_lsb, value)

    @property
    def reg_cca_cnt_txrx(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cca_cnt_txrx_msb, self.__reg_cca_cnt_txrx_lsb)
    @reg_cca_cnt_txrx.setter
    def reg_cca_cnt_txrx(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cca_cnt_txrx_msb, self.__reg_cca_cnt_txrx_lsb, value)

    @property
    def reg_cca_timer_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cca_timer_clr_msb, self.__reg_cca_timer_clr_lsb)
    @reg_cca_timer_clr.setter
    def reg_cca_timer_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cca_timer_clr_msb, self.__reg_cca_timer_clr_lsb, value)

    @property
    def reg_bb_timer_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_timer_clr_msb, self.__reg_bb_timer_clr_lsb)
    @reg_bb_timer_clr.setter
    def reg_bb_timer_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_timer_clr_msb, self.__reg_bb_timer_clr_lsb, value)

    @property
    def reg_bb_timer_max(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_timer_max_msb, self.__reg_bb_timer_max_lsb)
    @reg_bb_timer_max.setter
    def reg_bb_timer_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_timer_max_msb, self.__reg_bb_timer_max_lsb, value)
class BB_CCA_CTRL_1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x5c
        self.__bb_timer_done_lsb = 27
        self.__bb_timer_done_msb = 27
        self.__bb_timer_lsb = 0
        self.__bb_timer_msb = 26
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def bb_timer_done(self):
        return self.__MEM.rdm(self.__addr, self.__bb_timer_done_msb, self.__bb_timer_done_lsb)
    @bb_timer_done.setter
    def bb_timer_done(self, value):
        return self.__MEM.wrm(self.__addr, self.__bb_timer_done_msb, self.__bb_timer_done_lsb, value)

    @property
    def bb_timer(self):
        return self.__MEM.rdm(self.__addr, self.__bb_timer_msb, self.__bb_timer_lsb)
    @bb_timer.setter
    def bb_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__bb_timer_msb, self.__bb_timer_lsb, value)
class BB_CCA_CTRL_2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x60
        self.__cca_cnt_lsb = 0
        self.__cca_cnt_msb = 26
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def cca_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__cca_cnt_msb, self.__cca_cnt_lsb)
    @cca_cnt.setter
    def cca_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__cca_cnt_msb, self.__cca_cnt_lsb, value)
class BB_CCA_CTRL_3(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x64
        self.__cca_sec_cnt_lsb = 0
        self.__cca_sec_cnt_msb = 26
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def cca_sec_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__cca_sec_cnt_msb, self.__cca_sec_cnt_lsb)
    @cca_sec_cnt.setter
    def cca_sec_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__cca_sec_cnt_msb, self.__cca_sec_cnt_lsb, value)
class BB_NRXFDM_WDG(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x68
        self.__fdm_wdg_int_lsb = 28
        self.__fdm_wdg_int_msb = 28
        self.__fdm_wdg_int_cnt_lsb = 16
        self.__fdm_wdg_int_cnt_msb = 27
        self.__reg_fdm_wdg_int_en_lsb = 15
        self.__reg_fdm_wdg_int_en_msb = 15
        self.__reg_fdm_wdg_int_cnt_clr_lsb = 14
        self.__reg_fdm_wdg_int_cnt_clr_msb = 14
        self.__reg_fdm_wdg_clr_lsb = 13
        self.__reg_fdm_wdg_clr_msb = 13
        self.__reg_fdm_wdg_rst_en_lsb = 12
        self.__reg_fdm_wdg_rst_en_msb = 12
        self.__reg_fdm_wdg_en_lsb = 11
        self.__reg_fdm_wdg_en_msb = 11
        self.__reg_fdm_wdg_cnt_lsb = 0
        self.__reg_fdm_wdg_cnt_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def fdm_wdg_int(self):
        return self.__MEM.rdm(self.__addr, self.__fdm_wdg_int_msb, self.__fdm_wdg_int_lsb)
    @fdm_wdg_int.setter
    def fdm_wdg_int(self, value):
        return self.__MEM.wrm(self.__addr, self.__fdm_wdg_int_msb, self.__fdm_wdg_int_lsb, value)

    @property
    def fdm_wdg_int_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__fdm_wdg_int_cnt_msb, self.__fdm_wdg_int_cnt_lsb)
    @fdm_wdg_int_cnt.setter
    def fdm_wdg_int_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__fdm_wdg_int_cnt_msb, self.__fdm_wdg_int_cnt_lsb, value)

    @property
    def reg_fdm_wdg_int_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fdm_wdg_int_en_msb, self.__reg_fdm_wdg_int_en_lsb)
    @reg_fdm_wdg_int_en.setter
    def reg_fdm_wdg_int_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fdm_wdg_int_en_msb, self.__reg_fdm_wdg_int_en_lsb, value)

    @property
    def reg_fdm_wdg_int_cnt_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fdm_wdg_int_cnt_clr_msb, self.__reg_fdm_wdg_int_cnt_clr_lsb)
    @reg_fdm_wdg_int_cnt_clr.setter
    def reg_fdm_wdg_int_cnt_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fdm_wdg_int_cnt_clr_msb, self.__reg_fdm_wdg_int_cnt_clr_lsb, value)

    @property
    def reg_fdm_wdg_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fdm_wdg_clr_msb, self.__reg_fdm_wdg_clr_lsb)
    @reg_fdm_wdg_clr.setter
    def reg_fdm_wdg_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fdm_wdg_clr_msb, self.__reg_fdm_wdg_clr_lsb, value)

    @property
    def reg_fdm_wdg_rst_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fdm_wdg_rst_en_msb, self.__reg_fdm_wdg_rst_en_lsb)
    @reg_fdm_wdg_rst_en.setter
    def reg_fdm_wdg_rst_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fdm_wdg_rst_en_msb, self.__reg_fdm_wdg_rst_en_lsb, value)

    @property
    def reg_fdm_wdg_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fdm_wdg_en_msb, self.__reg_fdm_wdg_en_lsb)
    @reg_fdm_wdg_en.setter
    def reg_fdm_wdg_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fdm_wdg_en_msb, self.__reg_fdm_wdg_en_lsb, value)

    @property
    def reg_fdm_wdg_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fdm_wdg_cnt_msb, self.__reg_fdm_wdg_cnt_lsb)
    @reg_fdm_wdg_cnt.setter
    def reg_fdm_wdg_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fdm_wdg_cnt_msb, self.__reg_fdm_wdg_cnt_lsb, value)
class BB_CTRL1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x6c
        self.__reg_btx_start_wait_lsb = 20
        self.__reg_btx_start_wait_msb = 29
        self.__reg_ntx_ht2040_start_wait_lsb = 10
        self.__reg_ntx_ht2040_start_wait_msb = 19
        self.__reg_ntx_start_wait_lsb = 0
        self.__reg_ntx_start_wait_msb = 9
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_btx_start_wait(self):
        return self.__MEM.rdm(self.__addr, self.__reg_btx_start_wait_msb, self.__reg_btx_start_wait_lsb)
    @reg_btx_start_wait.setter
    def reg_btx_start_wait(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_btx_start_wait_msb, self.__reg_btx_start_wait_lsb, value)

    @property
    def reg_ntx_ht2040_start_wait(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ntx_ht2040_start_wait_msb, self.__reg_ntx_ht2040_start_wait_lsb)
    @reg_ntx_ht2040_start_wait.setter
    def reg_ntx_ht2040_start_wait(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ntx_ht2040_start_wait_msb, self.__reg_ntx_ht2040_start_wait_lsb, value)

    @property
    def reg_ntx_start_wait(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ntx_start_wait_msb, self.__reg_ntx_start_wait_lsb)
    @reg_ntx_start_wait.setter
    def reg_ntx_start_wait(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ntx_start_wait_msb, self.__reg_ntx_start_wait_lsb, value)
class BB_DC_RM_CONF0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x70
        self.__reg_use_stf_dc_calc_fo_min_thr_lsb = 24
        self.__reg_use_stf_dc_calc_fo_min_thr_msb = 31
        self.__reg_use_stf_dc_calc_snr_min_thr_lsb = 16
        self.__reg_use_stf_dc_calc_snr_min_thr_msb = 23
        self.__reg_use_stf_dc_1p6sum_snr_min_thr_lsb = 8
        self.__reg_use_stf_dc_1p6sum_snr_min_thr_msb = 15
        self.__reg_use_stf_dc_1p6sum_fo_max_thr_lsb = 0
        self.__reg_use_stf_dc_1p6sum_fo_max_thr_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_use_stf_dc_calc_fo_min_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_use_stf_dc_calc_fo_min_thr_msb, self.__reg_use_stf_dc_calc_fo_min_thr_lsb)
    @reg_use_stf_dc_calc_fo_min_thr.setter
    def reg_use_stf_dc_calc_fo_min_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_use_stf_dc_calc_fo_min_thr_msb, self.__reg_use_stf_dc_calc_fo_min_thr_lsb, value)

    @property
    def reg_use_stf_dc_calc_snr_min_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_use_stf_dc_calc_snr_min_thr_msb, self.__reg_use_stf_dc_calc_snr_min_thr_lsb)
    @reg_use_stf_dc_calc_snr_min_thr.setter
    def reg_use_stf_dc_calc_snr_min_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_use_stf_dc_calc_snr_min_thr_msb, self.__reg_use_stf_dc_calc_snr_min_thr_lsb, value)

    @property
    def reg_use_stf_dc_1p6sum_snr_min_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_use_stf_dc_1p6sum_snr_min_thr_msb, self.__reg_use_stf_dc_1p6sum_snr_min_thr_lsb)
    @reg_use_stf_dc_1p6sum_snr_min_thr.setter
    def reg_use_stf_dc_1p6sum_snr_min_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_use_stf_dc_1p6sum_snr_min_thr_msb, self.__reg_use_stf_dc_1p6sum_snr_min_thr_lsb, value)

    @property
    def reg_use_stf_dc_1p6sum_fo_max_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_use_stf_dc_1p6sum_fo_max_thr_msb, self.__reg_use_stf_dc_1p6sum_fo_max_thr_lsb)
    @reg_use_stf_dc_1p6sum_fo_max_thr.setter
    def reg_use_stf_dc_1p6sum_fo_max_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_use_stf_dc_1p6sum_fo_max_thr_msb, self.__reg_use_stf_dc_1p6sum_fo_max_thr_lsb, value)
class BB_DC_RM_CONF1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x74
        self.__reg_use_ltf_dc_calc_fo_min_thr_lsb = 19
        self.__reg_use_ltf_dc_calc_fo_min_thr_msb = 26
        self.__reg_use_ltf_dc_calc_snr_min_thr_lsb = 11
        self.__reg_use_ltf_dc_calc_snr_min_thr_msb = 18
        self.__reg_use_dc_ltf_calc_en_lsb = 10
        self.__reg_use_dc_ltf_calc_en_msb = 10
        self.__reg_use_dc_htstf_en_lsb = 9
        self.__reg_use_dc_htstf_en_msb = 9
        self.__reg_use_dc_coarse_calc_en_lsb = 8
        self.__reg_use_dc_coarse_calc_en_msb = 8
        self.__reg_use_ltf_dc_est_fo_max_thr_lsb = 0
        self.__reg_use_ltf_dc_est_fo_max_thr_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_use_ltf_dc_calc_fo_min_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_use_ltf_dc_calc_fo_min_thr_msb, self.__reg_use_ltf_dc_calc_fo_min_thr_lsb)
    @reg_use_ltf_dc_calc_fo_min_thr.setter
    def reg_use_ltf_dc_calc_fo_min_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_use_ltf_dc_calc_fo_min_thr_msb, self.__reg_use_ltf_dc_calc_fo_min_thr_lsb, value)

    @property
    def reg_use_ltf_dc_calc_snr_min_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_use_ltf_dc_calc_snr_min_thr_msb, self.__reg_use_ltf_dc_calc_snr_min_thr_lsb)
    @reg_use_ltf_dc_calc_snr_min_thr.setter
    def reg_use_ltf_dc_calc_snr_min_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_use_ltf_dc_calc_snr_min_thr_msb, self.__reg_use_ltf_dc_calc_snr_min_thr_lsb, value)

    @property
    def reg_use_dc_ltf_calc_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_use_dc_ltf_calc_en_msb, self.__reg_use_dc_ltf_calc_en_lsb)
    @reg_use_dc_ltf_calc_en.setter
    def reg_use_dc_ltf_calc_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_use_dc_ltf_calc_en_msb, self.__reg_use_dc_ltf_calc_en_lsb, value)

    @property
    def reg_use_dc_htstf_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_use_dc_htstf_en_msb, self.__reg_use_dc_htstf_en_lsb)
    @reg_use_dc_htstf_en.setter
    def reg_use_dc_htstf_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_use_dc_htstf_en_msb, self.__reg_use_dc_htstf_en_lsb, value)

    @property
    def reg_use_dc_coarse_calc_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_use_dc_coarse_calc_en_msb, self.__reg_use_dc_coarse_calc_en_lsb)
    @reg_use_dc_coarse_calc_en.setter
    def reg_use_dc_coarse_calc_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_use_dc_coarse_calc_en_msb, self.__reg_use_dc_coarse_calc_en_lsb, value)

    @property
    def reg_use_ltf_dc_est_fo_max_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_use_ltf_dc_est_fo_max_thr_msb, self.__reg_use_ltf_dc_est_fo_max_thr_lsb)
    @reg_use_ltf_dc_est_fo_max_thr.setter
    def reg_use_ltf_dc_est_fo_max_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_use_ltf_dc_est_fo_max_thr_msb, self.__reg_use_ltf_dc_est_fo_max_thr_lsb, value)
class DC_CTRL1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x78
        self.__reg_loop_cnt_min_shift4_lsb = 24
        self.__reg_loop_cnt_min_shift4_msb = 31
        self.__reg_loop_cnt_min_shift3_lsb = 16
        self.__reg_loop_cnt_min_shift3_msb = 23
        self.__reg_loop_cnt_min_shift2_lsb = 8
        self.__reg_loop_cnt_min_shift2_msb = 15
        self.__reg_loop_cnt_min_shift1_lsb = 0
        self.__reg_loop_cnt_min_shift1_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_loop_cnt_min_shift4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_loop_cnt_min_shift4_msb, self.__reg_loop_cnt_min_shift4_lsb)
    @reg_loop_cnt_min_shift4.setter
    def reg_loop_cnt_min_shift4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_loop_cnt_min_shift4_msb, self.__reg_loop_cnt_min_shift4_lsb, value)

    @property
    def reg_loop_cnt_min_shift3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_loop_cnt_min_shift3_msb, self.__reg_loop_cnt_min_shift3_lsb)
    @reg_loop_cnt_min_shift3.setter
    def reg_loop_cnt_min_shift3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_loop_cnt_min_shift3_msb, self.__reg_loop_cnt_min_shift3_lsb, value)

    @property
    def reg_loop_cnt_min_shift2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_loop_cnt_min_shift2_msb, self.__reg_loop_cnt_min_shift2_lsb)
    @reg_loop_cnt_min_shift2.setter
    def reg_loop_cnt_min_shift2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_loop_cnt_min_shift2_msb, self.__reg_loop_cnt_min_shift2_lsb, value)

    @property
    def reg_loop_cnt_min_shift1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_loop_cnt_min_shift1_msb, self.__reg_loop_cnt_min_shift1_lsb)
    @reg_loop_cnt_min_shift1.setter
    def reg_loop_cnt_min_shift1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_loop_cnt_min_shift1_msb, self.__reg_loop_cnt_min_shift1_lsb, value)
class DC_CTRL2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x7c
        self.__reg_loop_cnt_min_shift7_lsb = 16
        self.__reg_loop_cnt_min_shift7_msb = 23
        self.__reg_loop_cnt_min_shift6_lsb = 8
        self.__reg_loop_cnt_min_shift6_msb = 15
        self.__reg_loop_cnt_min_shift5_lsb = 0
        self.__reg_loop_cnt_min_shift5_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_loop_cnt_min_shift7(self):
        return self.__MEM.rdm(self.__addr, self.__reg_loop_cnt_min_shift7_msb, self.__reg_loop_cnt_min_shift7_lsb)
    @reg_loop_cnt_min_shift7.setter
    def reg_loop_cnt_min_shift7(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_loop_cnt_min_shift7_msb, self.__reg_loop_cnt_min_shift7_lsb, value)

    @property
    def reg_loop_cnt_min_shift6(self):
        return self.__MEM.rdm(self.__addr, self.__reg_loop_cnt_min_shift6_msb, self.__reg_loop_cnt_min_shift6_lsb)
    @reg_loop_cnt_min_shift6.setter
    def reg_loop_cnt_min_shift6(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_loop_cnt_min_shift6_msb, self.__reg_loop_cnt_min_shift6_lsb, value)

    @property
    def reg_loop_cnt_min_shift5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_loop_cnt_min_shift5_msb, self.__reg_loop_cnt_min_shift5_lsb)
    @reg_loop_cnt_min_shift5.setter
    def reg_loop_cnt_min_shift5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_loop_cnt_min_shift5_msb, self.__reg_loop_cnt_min_shift5_lsb, value)
class BB_CLK_CONF(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x80
        self.__reg_tone_delta_clk_fen_lsb = 14
        self.__reg_tone_delta_clk_fen_msb = 14
        self.__reg_tone4_clk_fen_lsb = 13
        self.__reg_tone4_clk_fen_msb = 13
        self.__reg_tone3_clk_fen_lsb = 12
        self.__reg_tone3_clk_fen_msb = 12
        self.__reg_tone2_clk_fen_lsb = 11
        self.__reg_tone2_clk_fen_msb = 11
        self.__reg_tone1_clk_fen_lsb = 10
        self.__reg_tone1_clk_fen_msb = 10
        self.__reg_bbclk_160m_fen_lsb = 9
        self.__reg_bbclk_160m_fen_msb = 9
        self.__reg_bbclk_80m_fen_lsb = 8
        self.__reg_bbclk_80m_fen_msb = 8
        self.__reg_bbclk_40m_fen_lsb = 7
        self.__reg_bbclk_40m_fen_msb = 7
        self.__reg_bbclk_80x_fen_lsb = 6
        self.__reg_bbclk_80x_fen_msb = 6
        self.__reg_bbclk_40x_fen_lsb = 5
        self.__reg_bbclk_40x_fen_msb = 5
        self.__reg_bbclk_160m_dmd_fen_lsb = 4
        self.__reg_bbclk_160m_dmd_fen_msb = 4
        self.__reg_bbclk_80m_dmd_fen_lsb = 3
        self.__reg_bbclk_80m_dmd_fen_msb = 3
        self.__reg_bbclk_44m_fen_lsb = 2
        self.__reg_bbclk_44m_fen_msb = 2
        self.__reg_bbct_clk80x_fen_lsb = 1
        self.__reg_bbct_clk80x_fen_msb = 1
        self.__reg_bbct_clk40x_fen_lsb = 0
        self.__reg_bbct_clk40x_fen_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tone_delta_clk_fen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_delta_clk_fen_msb, self.__reg_tone_delta_clk_fen_lsb)
    @reg_tone_delta_clk_fen.setter
    def reg_tone_delta_clk_fen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_delta_clk_fen_msb, self.__reg_tone_delta_clk_fen_lsb, value)

    @property
    def reg_tone4_clk_fen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone4_clk_fen_msb, self.__reg_tone4_clk_fen_lsb)
    @reg_tone4_clk_fen.setter
    def reg_tone4_clk_fen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone4_clk_fen_msb, self.__reg_tone4_clk_fen_lsb, value)

    @property
    def reg_tone3_clk_fen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone3_clk_fen_msb, self.__reg_tone3_clk_fen_lsb)
    @reg_tone3_clk_fen.setter
    def reg_tone3_clk_fen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone3_clk_fen_msb, self.__reg_tone3_clk_fen_lsb, value)

    @property
    def reg_tone2_clk_fen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone2_clk_fen_msb, self.__reg_tone2_clk_fen_lsb)
    @reg_tone2_clk_fen.setter
    def reg_tone2_clk_fen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone2_clk_fen_msb, self.__reg_tone2_clk_fen_lsb, value)

    @property
    def reg_tone1_clk_fen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone1_clk_fen_msb, self.__reg_tone1_clk_fen_lsb)
    @reg_tone1_clk_fen.setter
    def reg_tone1_clk_fen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone1_clk_fen_msb, self.__reg_tone1_clk_fen_lsb, value)

    @property
    def reg_bbclk_160m_fen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbclk_160m_fen_msb, self.__reg_bbclk_160m_fen_lsb)
    @reg_bbclk_160m_fen.setter
    def reg_bbclk_160m_fen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbclk_160m_fen_msb, self.__reg_bbclk_160m_fen_lsb, value)

    @property
    def reg_bbclk_80m_fen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbclk_80m_fen_msb, self.__reg_bbclk_80m_fen_lsb)
    @reg_bbclk_80m_fen.setter
    def reg_bbclk_80m_fen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbclk_80m_fen_msb, self.__reg_bbclk_80m_fen_lsb, value)

    @property
    def reg_bbclk_40m_fen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbclk_40m_fen_msb, self.__reg_bbclk_40m_fen_lsb)
    @reg_bbclk_40m_fen.setter
    def reg_bbclk_40m_fen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbclk_40m_fen_msb, self.__reg_bbclk_40m_fen_lsb, value)

    @property
    def reg_bbclk_80x_fen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbclk_80x_fen_msb, self.__reg_bbclk_80x_fen_lsb)
    @reg_bbclk_80x_fen.setter
    def reg_bbclk_80x_fen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbclk_80x_fen_msb, self.__reg_bbclk_80x_fen_lsb, value)

    @property
    def reg_bbclk_40x_fen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbclk_40x_fen_msb, self.__reg_bbclk_40x_fen_lsb)
    @reg_bbclk_40x_fen.setter
    def reg_bbclk_40x_fen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbclk_40x_fen_msb, self.__reg_bbclk_40x_fen_lsb, value)

    @property
    def reg_bbclk_160m_dmd_fen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbclk_160m_dmd_fen_msb, self.__reg_bbclk_160m_dmd_fen_lsb)
    @reg_bbclk_160m_dmd_fen.setter
    def reg_bbclk_160m_dmd_fen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbclk_160m_dmd_fen_msb, self.__reg_bbclk_160m_dmd_fen_lsb, value)

    @property
    def reg_bbclk_80m_dmd_fen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbclk_80m_dmd_fen_msb, self.__reg_bbclk_80m_dmd_fen_lsb)
    @reg_bbclk_80m_dmd_fen.setter
    def reg_bbclk_80m_dmd_fen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbclk_80m_dmd_fen_msb, self.__reg_bbclk_80m_dmd_fen_lsb, value)

    @property
    def reg_bbclk_44m_fen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbclk_44m_fen_msb, self.__reg_bbclk_44m_fen_lsb)
    @reg_bbclk_44m_fen.setter
    def reg_bbclk_44m_fen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbclk_44m_fen_msb, self.__reg_bbclk_44m_fen_lsb, value)

    @property
    def reg_bbct_clk80x_fen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbct_clk80x_fen_msb, self.__reg_bbct_clk80x_fen_lsb)
    @reg_bbct_clk80x_fen.setter
    def reg_bbct_clk80x_fen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbct_clk80x_fen_msb, self.__reg_bbct_clk80x_fen_lsb, value)

    @property
    def reg_bbct_clk40x_fen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbct_clk40x_fen_msb, self.__reg_bbct_clk40x_fen_lsb)
    @reg_bbct_clk40x_fen.setter
    def reg_bbct_clk40x_fen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbct_clk40x_fen_msb, self.__reg_bbct_clk40x_fen_lsb, value)
class BB_STATE_CNT_CONF0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x84
        self.__reg_bb_cnt_rx_err_restart_tar_lsb = 20
        self.__reg_bb_cnt_rx_err_restart_tar_msb = 29
        self.__reg_bb_cnt_agc_reset_tar_lsb = 10
        self.__reg_bb_cnt_agc_reset_tar_msb = 19
        self.__reg_bb_cnt_tx_tar_lsb = 0
        self.__reg_bb_cnt_tx_tar_msb = 9
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bb_cnt_rx_err_restart_tar(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_cnt_rx_err_restart_tar_msb, self.__reg_bb_cnt_rx_err_restart_tar_lsb)
    @reg_bb_cnt_rx_err_restart_tar.setter
    def reg_bb_cnt_rx_err_restart_tar(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_cnt_rx_err_restart_tar_msb, self.__reg_bb_cnt_rx_err_restart_tar_lsb, value)

    @property
    def reg_bb_cnt_agc_reset_tar(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_cnt_agc_reset_tar_msb, self.__reg_bb_cnt_agc_reset_tar_lsb)
    @reg_bb_cnt_agc_reset_tar.setter
    def reg_bb_cnt_agc_reset_tar(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_cnt_agc_reset_tar_msb, self.__reg_bb_cnt_agc_reset_tar_lsb, value)

    @property
    def reg_bb_cnt_tx_tar(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_cnt_tx_tar_msb, self.__reg_bb_cnt_tx_tar_lsb)
    @reg_bb_cnt_tx_tar.setter
    def reg_bb_cnt_tx_tar(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_cnt_tx_tar_msb, self.__reg_bb_cnt_tx_tar_lsb, value)
class BB_STATE_CNT_CONF1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x88
        self.__reg_bb_cnt_err_tar_lsb = 20
        self.__reg_bb_cnt_err_tar_msb = 29
        self.__reg_bb_cnt_rx_en_tar_lsb = 10
        self.__reg_bb_cnt_rx_en_tar_msb = 19
        self.__reg_bb_cnt_rifs_tar_lsb = 0
        self.__reg_bb_cnt_rifs_tar_msb = 9
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bb_cnt_err_tar(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_cnt_err_tar_msb, self.__reg_bb_cnt_err_tar_lsb)
    @reg_bb_cnt_err_tar.setter
    def reg_bb_cnt_err_tar(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_cnt_err_tar_msb, self.__reg_bb_cnt_err_tar_lsb, value)

    @property
    def reg_bb_cnt_rx_en_tar(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_cnt_rx_en_tar_msb, self.__reg_bb_cnt_rx_en_tar_lsb)
    @reg_bb_cnt_rx_en_tar.setter
    def reg_bb_cnt_rx_en_tar(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_cnt_rx_en_tar_msb, self.__reg_bb_cnt_rx_en_tar_lsb, value)

    @property
    def reg_bb_cnt_rifs_tar(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_cnt_rifs_tar_msb, self.__reg_bb_cnt_rifs_tar_lsb)
    @reg_bb_cnt_rifs_tar.setter
    def reg_bb_cnt_rifs_tar(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_cnt_rifs_tar_msb, self.__reg_bb_cnt_rifs_tar_lsb, value)
class TONE_CTRL_7(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x8c
        self.__reg_tone_est_fft_en_lsb = 31
        self.__reg_tone_est_fft_en_msb = 31
        self.__reg_tone_est_auto_covg_en_lsb = 30
        self.__reg_tone_est_auto_covg_en_msb = 30
        self.__reg_phi_delta_est_shift_lsb = 28
        self.__reg_phi_delta_est_shift_msb = 29
        self.__reg_phi_delta_est_abs_max_lsb = 20
        self.__reg_phi_delta_est_abs_max_msb = 27
        self.__reg_tone_est_auto_cnt_tar_lsb = 16
        self.__reg_tone_est_auto_cnt_tar_msb = 19
        self.__tone_est_coef_lsb = 0
        self.__tone_est_coef_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tone_est_fft_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_est_fft_en_msb, self.__reg_tone_est_fft_en_lsb)
    @reg_tone_est_fft_en.setter
    def reg_tone_est_fft_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_est_fft_en_msb, self.__reg_tone_est_fft_en_lsb, value)

    @property
    def reg_tone_est_auto_covg_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_est_auto_covg_en_msb, self.__reg_tone_est_auto_covg_en_lsb)
    @reg_tone_est_auto_covg_en.setter
    def reg_tone_est_auto_covg_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_est_auto_covg_en_msb, self.__reg_tone_est_auto_covg_en_lsb, value)

    @property
    def reg_phi_delta_est_shift(self):
        return self.__MEM.rdm(self.__addr, self.__reg_phi_delta_est_shift_msb, self.__reg_phi_delta_est_shift_lsb)
    @reg_phi_delta_est_shift.setter
    def reg_phi_delta_est_shift(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_phi_delta_est_shift_msb, self.__reg_phi_delta_est_shift_lsb, value)

    @property
    def reg_phi_delta_est_abs_max(self):
        return self.__MEM.rdm(self.__addr, self.__reg_phi_delta_est_abs_max_msb, self.__reg_phi_delta_est_abs_max_lsb)
    @reg_phi_delta_est_abs_max.setter
    def reg_phi_delta_est_abs_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_phi_delta_est_abs_max_msb, self.__reg_phi_delta_est_abs_max_lsb, value)

    @property
    def reg_tone_est_auto_cnt_tar(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_est_auto_cnt_tar_msb, self.__reg_tone_est_auto_cnt_tar_lsb)
    @reg_tone_est_auto_cnt_tar.setter
    def reg_tone_est_auto_cnt_tar(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_est_auto_cnt_tar_msb, self.__reg_tone_est_auto_cnt_tar_lsb, value)

    @property
    def tone_est_coef(self):
        return self.__MEM.rdm(self.__addr, self.__tone_est_coef_msb, self.__tone_est_coef_lsb)
    @tone_est_coef.setter
    def tone_est_coef(self, value):
        return self.__MEM.wrm(self.__addr, self.__tone_est_coef_msb, self.__tone_est_coef_lsb, value)
class TONE_CTRL_8(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x90
        self.__fft_out_data_lsb = 8
        self.__fft_out_data_msb = 31
        self.__reg_fft_out_addr_lsb = 0
        self.__reg_fft_out_addr_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def fft_out_data(self):
        return self.__MEM.rdm(self.__addr, self.__fft_out_data_msb, self.__fft_out_data_lsb)
    @fft_out_data.setter
    def fft_out_data(self, value):
        return self.__MEM.wrm(self.__addr, self.__fft_out_data_msb, self.__fft_out_data_lsb, value)

    @property
    def reg_fft_out_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fft_out_addr_msb, self.__reg_fft_out_addr_lsb)
    @reg_fft_out_addr.setter
    def reg_fft_out_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fft_out_addr_msb, self.__reg_fft_out_addr_lsb, value)
class TONE_CTRL_9(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x94
        self.__reg_fft_out_addr_val_lsb = 16
        self.__reg_fft_out_addr_val_msb = 16
        self.__reg_tone_est_req_err1_lsb = 8
        self.__reg_tone_est_req_err1_msb = 15
        self.__reg_tone_est_req_err0_lsb = 0
        self.__reg_tone_est_req_err0_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_fft_out_addr_val(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fft_out_addr_val_msb, self.__reg_fft_out_addr_val_lsb)
    @reg_fft_out_addr_val.setter
    def reg_fft_out_addr_val(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fft_out_addr_val_msb, self.__reg_fft_out_addr_val_lsb, value)

    @property
    def reg_tone_est_req_err1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_est_req_err1_msb, self.__reg_tone_est_req_err1_lsb)
    @reg_tone_est_req_err1.setter
    def reg_tone_est_req_err1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_est_req_err1_msb, self.__reg_tone_est_req_err1_lsb, value)

    @property
    def reg_tone_est_req_err0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_est_req_err0_msb, self.__reg_tone_est_req_err0_lsb)
    @reg_tone_est_req_err0.setter
    def reg_tone_est_req_err0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_est_req_err0_msb, self.__reg_tone_est_req_err0_lsb, value)
class TONE_CTRL_10(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x98
        self.__reg_tone_est_req_err_det_num_lsb = 24
        self.__reg_tone_est_req_err_det_num_msb = 31
        self.__reg_tone_est_req_err_det_len_lsb = 0
        self.__reg_tone_est_req_err_det_len_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tone_est_req_err_det_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_est_req_err_det_num_msb, self.__reg_tone_est_req_err_det_num_lsb)
    @reg_tone_est_req_err_det_num.setter
    def reg_tone_est_req_err_det_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_est_req_err_det_num_msb, self.__reg_tone_est_req_err_det_num_lsb, value)

    @property
    def reg_tone_est_req_err_det_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tone_est_req_err_det_len_msb, self.__reg_tone_est_req_err_det_len_lsb)
    @reg_tone_est_req_err_det_len.setter
    def reg_tone_est_req_err_det_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tone_est_req_err_det_len_msb, self.__reg_tone_est_req_err_det_len_lsb, value)
class BB_STATE_CNT_CONF2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x9c
        self.__reg_bb_cnt_txend_tar_lsb = 0
        self.__reg_bb_cnt_txend_tar_msb = 9
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bb_cnt_txend_tar(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_cnt_txend_tar_msb, self.__reg_bb_cnt_txend_tar_lsb)
    @reg_bb_cnt_txend_tar.setter
    def reg_bb_cnt_txend_tar(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_cnt_txend_tar_msb, self.__reg_bb_cnt_txend_tar_lsb, value)
class TONE_CTRL_11(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0xa0
        self.__reg_te_loop_cnt_thr4_lsb = 24
        self.__reg_te_loop_cnt_thr4_msb = 31
        self.__reg_te_loop_cnt_thr3_lsb = 16
        self.__reg_te_loop_cnt_thr3_msb = 23
        self.__reg_te_loop_cnt_thr2_lsb = 8
        self.__reg_te_loop_cnt_thr2_msb = 15
        self.__reg_te_loop_cnt_thr1_lsb = 0
        self.__reg_te_loop_cnt_thr1_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_te_loop_cnt_thr4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_te_loop_cnt_thr4_msb, self.__reg_te_loop_cnt_thr4_lsb)
    @reg_te_loop_cnt_thr4.setter
    def reg_te_loop_cnt_thr4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_te_loop_cnt_thr4_msb, self.__reg_te_loop_cnt_thr4_lsb, value)

    @property
    def reg_te_loop_cnt_thr3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_te_loop_cnt_thr3_msb, self.__reg_te_loop_cnt_thr3_lsb)
    @reg_te_loop_cnt_thr3.setter
    def reg_te_loop_cnt_thr3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_te_loop_cnt_thr3_msb, self.__reg_te_loop_cnt_thr3_lsb, value)

    @property
    def reg_te_loop_cnt_thr2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_te_loop_cnt_thr2_msb, self.__reg_te_loop_cnt_thr2_lsb)
    @reg_te_loop_cnt_thr2.setter
    def reg_te_loop_cnt_thr2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_te_loop_cnt_thr2_msb, self.__reg_te_loop_cnt_thr2_lsb, value)

    @property
    def reg_te_loop_cnt_thr1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_te_loop_cnt_thr1_msb, self.__reg_te_loop_cnt_thr1_lsb)
    @reg_te_loop_cnt_thr1.setter
    def reg_te_loop_cnt_thr1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_te_loop_cnt_thr1_msb, self.__reg_te_loop_cnt_thr1_lsb, value)
class TONE_CTRL_12(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0xa4
        self.__reg_te_loop_cnt_thr7_lsb = 16
        self.__reg_te_loop_cnt_thr7_msb = 23
        self.__reg_te_loop_cnt_thr6_lsb = 8
        self.__reg_te_loop_cnt_thr6_msb = 15
        self.__reg_te_loop_cnt_thr5_lsb = 0
        self.__reg_te_loop_cnt_thr5_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_te_loop_cnt_thr7(self):
        return self.__MEM.rdm(self.__addr, self.__reg_te_loop_cnt_thr7_msb, self.__reg_te_loop_cnt_thr7_lsb)
    @reg_te_loop_cnt_thr7.setter
    def reg_te_loop_cnt_thr7(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_te_loop_cnt_thr7_msb, self.__reg_te_loop_cnt_thr7_lsb, value)

    @property
    def reg_te_loop_cnt_thr6(self):
        return self.__MEM.rdm(self.__addr, self.__reg_te_loop_cnt_thr6_msb, self.__reg_te_loop_cnt_thr6_lsb)
    @reg_te_loop_cnt_thr6.setter
    def reg_te_loop_cnt_thr6(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_te_loop_cnt_thr6_msb, self.__reg_te_loop_cnt_thr6_lsb, value)

    @property
    def reg_te_loop_cnt_thr5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_te_loop_cnt_thr5_msb, self.__reg_te_loop_cnt_thr5_lsb)
    @reg_te_loop_cnt_thr5.setter
    def reg_te_loop_cnt_thr5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_te_loop_cnt_thr5_msb, self.__reg_te_loop_cnt_thr5_lsb, value)
class BB_NOUSE(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_BASE + 0x3fc
        self.__reg_bb_date_lsb = 0
        self.__reg_bb_date_msb = 27
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bb_date(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_date_msb, self.__reg_bb_date_lsb)
    @reg_bb_date.setter
    def reg_bb_date(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_date_msb, self.__reg_bb_date_lsb, value)
    @property
    def default_value(self):
        return 0x1910140
