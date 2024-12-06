from hal.common import *
from hal.hwregister.hwreg.FPGA724_M1.addr_base import *
class BB_TX(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.BBTXCONF = BBTXCONF(self.channel, self.chipv)
        self.BBTXANALOG_CTRL1 = BBTXANALOG_CTRL1(self.channel, self.chipv)
        self.BB_HT40_DUG = BB_HT40_DUG(self.channel, self.chipv)
        self.BB_HT40_DUG1 = BB_HT40_DUG1(self.channel, self.chipv)
        self.BB_IQ_MIS_CORR0 = BB_IQ_MIS_CORR0(self.channel, self.chipv)
        self.BB_IQ_MIS_CORR1 = BB_IQ_MIS_CORR1(self.channel, self.chipv)
        self.BB_IQ_MIS_CORR2 = BB_IQ_MIS_CORR2(self.channel, self.chipv)
        self.BB_IQ_MIS_CORR3 = BB_IQ_MIS_CORR3(self.channel, self.chipv)
        self.BB_IQ_MIS_CORR4 = BB_IQ_MIS_CORR4(self.channel, self.chipv)
        self.BB_IQ_MIS_CORR5 = BB_IQ_MIS_CORR5(self.channel, self.chipv)
        self.BB_IQ_MIS_CORR6 = BB_IQ_MIS_CORR6(self.channel, self.chipv)
        self.BB_IQ_MIS_CORR7 = BB_IQ_MIS_CORR7(self.channel, self.chipv)
        self.BB_IQ_MIS_CORR8 = BB_IQ_MIS_CORR8(self.channel, self.chipv)
        self.BB_IQ_MIS_CORR9 = BB_IQ_MIS_CORR9(self.channel, self.chipv)
        self.BB_IQ_MIS_CORR10 = BB_IQ_MIS_CORR10(self.channel, self.chipv)
        self.BB_IQ_MIS_CORR11 = BB_IQ_MIS_CORR11(self.channel, self.chipv)
        self.BB_IQ_MIS_CORR12 = BB_IQ_MIS_CORR12(self.channel, self.chipv)
        self.BB_IQ_MIS_CORR13 = BB_IQ_MIS_CORR13(self.channel, self.chipv)
        self.BB_IQ_MIS_CORR14 = BB_IQ_MIS_CORR14(self.channel, self.chipv)
        self.BB_IQ_MIS_CORR15 = BB_IQ_MIS_CORR15(self.channel, self.chipv)
        self.BB_TX_TEST = BB_TX_TEST(self.channel, self.chipv)
        self.BB_BTX_NOISE_I = BB_BTX_NOISE_I(self.channel, self.chipv)
        self.BB_BTX_NOISE_Q = BB_BTX_NOISE_Q(self.channel, self.chipv)
        self.BB_BTX_LR = BB_BTX_LR(self.channel, self.chipv)
        self.BB_BTX_LR_CONF = BB_BTX_LR_CONF(self.channel, self.chipv)
        self.BBTXDATE = BBTXDATE(self.channel, self.chipv)
class BBTXCONF(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_TX_BASE + 0x0
        self.__reg_stf_num_add_msb_lsb = 23
        self.__reg_stf_num_add_msb_msb = 25
        self.__reg_coef_sel_msb_lsb = 22
        self.__reg_coef_sel_msb_msb = 22
        self.__reg_ntx_contin_en_lsb = 21
        self.__reg_ntx_contin_en_msb = 21
        self.__reg_txpwr_ht2040_diff_lsb = 20
        self.__reg_txpwr_ht2040_diff_msb = 20
        self.__reg_txpwr_sys2040_diff_lsb = 19
        self.__reg_txpwr_sys2040_diff_msb = 19
        self.__reg_stf_num_add_lsb = 16
        self.__reg_stf_num_add_msb = 18
        self.__reg_tx_err_rst_val_lsb = 15
        self.__reg_tx_err_rst_val_msb = 15
        self.__reg_coef_sel_lsb = 13
        self.__reg_coef_sel_msb = 14
        self.__reg_init_phase_lsb = 11
        self.__reg_init_phase_msb = 12
        self.__reg_scrm_dis_lsb = 10
        self.__reg_scrm_dis_msb = 10
        self.__reg_ntx_window_lsb = 8
        self.__reg_ntx_window_msb = 9
        self.__reg_seed_load_lsb = 7
        self.__reg_seed_load_msb = 7
        self.__reg_seed_lsb = 0
        self.__reg_seed_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_stf_num_add_msb(self):
        return self.__MEM.rdm(self.__addr, self.__reg_stf_num_add_msb_msb, self.__reg_stf_num_add_msb_lsb)
    @reg_stf_num_add_msb.setter
    def reg_stf_num_add_msb(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_stf_num_add_msb_msb, self.__reg_stf_num_add_msb_lsb, value)

    @property
    def reg_coef_sel_msb(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coef_sel_msb_msb, self.__reg_coef_sel_msb_lsb)
    @reg_coef_sel_msb.setter
    def reg_coef_sel_msb(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coef_sel_msb_msb, self.__reg_coef_sel_msb_lsb, value)

    @property
    def reg_ntx_contin_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ntx_contin_en_msb, self.__reg_ntx_contin_en_lsb)
    @reg_ntx_contin_en.setter
    def reg_ntx_contin_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ntx_contin_en_msb, self.__reg_ntx_contin_en_lsb, value)

    @property
    def reg_txpwr_ht2040_diff(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txpwr_ht2040_diff_msb, self.__reg_txpwr_ht2040_diff_lsb)
    @reg_txpwr_ht2040_diff.setter
    def reg_txpwr_ht2040_diff(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txpwr_ht2040_diff_msb, self.__reg_txpwr_ht2040_diff_lsb, value)

    @property
    def reg_txpwr_sys2040_diff(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txpwr_sys2040_diff_msb, self.__reg_txpwr_sys2040_diff_lsb)
    @reg_txpwr_sys2040_diff.setter
    def reg_txpwr_sys2040_diff(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txpwr_sys2040_diff_msb, self.__reg_txpwr_sys2040_diff_lsb, value)

    @property
    def reg_stf_num_add(self):
        return self.__MEM.rdm(self.__addr, self.__reg_stf_num_add_msb, self.__reg_stf_num_add_lsb)
    @reg_stf_num_add.setter
    def reg_stf_num_add(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_stf_num_add_msb, self.__reg_stf_num_add_lsb, value)

    @property
    def reg_tx_err_rst_val(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_err_rst_val_msb, self.__reg_tx_err_rst_val_lsb)
    @reg_tx_err_rst_val.setter
    def reg_tx_err_rst_val(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_err_rst_val_msb, self.__reg_tx_err_rst_val_lsb, value)

    @property
    def reg_coef_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coef_sel_msb, self.__reg_coef_sel_lsb)
    @reg_coef_sel.setter
    def reg_coef_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coef_sel_msb, self.__reg_coef_sel_lsb, value)

    @property
    def reg_init_phase(self):
        return self.__MEM.rdm(self.__addr, self.__reg_init_phase_msb, self.__reg_init_phase_lsb)
    @reg_init_phase.setter
    def reg_init_phase(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_init_phase_msb, self.__reg_init_phase_lsb, value)

    @property
    def reg_scrm_dis(self):
        return self.__MEM.rdm(self.__addr, self.__reg_scrm_dis_msb, self.__reg_scrm_dis_lsb)
    @reg_scrm_dis.setter
    def reg_scrm_dis(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_scrm_dis_msb, self.__reg_scrm_dis_lsb, value)

    @property
    def reg_ntx_window(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ntx_window_msb, self.__reg_ntx_window_lsb)
    @reg_ntx_window.setter
    def reg_ntx_window(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ntx_window_msb, self.__reg_ntx_window_lsb, value)

    @property
    def reg_seed_load(self):
        return self.__MEM.rdm(self.__addr, self.__reg_seed_load_msb, self.__reg_seed_load_lsb)
    @reg_seed_load.setter
    def reg_seed_load(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_seed_load_msb, self.__reg_seed_load_lsb, value)

    @property
    def reg_seed(self):
        return self.__MEM.rdm(self.__addr, self.__reg_seed_msb, self.__reg_seed_lsb)
    @reg_seed.setter
    def reg_seed(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_seed_msb, self.__reg_seed_lsb, value)
class BBTXANALOG_CTRL1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_TX_BASE + 0x4
        self.__reg_loop_back_en_lsb = 31
        self.__reg_loop_back_en_msb = 31
        self.__reg_spur_db_cfg_lsb = 20
        self.__reg_spur_db_cfg_msb = 27
        self.__reg_rssi_cfg_lsb = 12
        self.__reg_rssi_cfg_msb = 19
        self.__reg_tx_shr_lsb = 0
        self.__reg_tx_shr_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_loop_back_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_loop_back_en_msb, self.__reg_loop_back_en_lsb)
    @reg_loop_back_en.setter
    def reg_loop_back_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_loop_back_en_msb, self.__reg_loop_back_en_lsb, value)

    @property
    def reg_spur_db_cfg(self):
        return self.__MEM.rdm(self.__addr, self.__reg_spur_db_cfg_msb, self.__reg_spur_db_cfg_lsb)
    @reg_spur_db_cfg.setter
    def reg_spur_db_cfg(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_spur_db_cfg_msb, self.__reg_spur_db_cfg_lsb, value)

    @property
    def reg_rssi_cfg(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rssi_cfg_msb, self.__reg_rssi_cfg_lsb)
    @reg_rssi_cfg.setter
    def reg_rssi_cfg(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rssi_cfg_msb, self.__reg_rssi_cfg_lsb, value)

    @property
    def reg_tx_shr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_shr_msb, self.__reg_tx_shr_lsb)
    @reg_tx_shr.setter
    def reg_tx_shr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_shr_msb, self.__reg_tx_shr_lsb, value)
class BB_HT40_DUG(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_TX_BASE + 0x8
        self.__reg_spur_en_lsb = 26
        self.__reg_spur_en_msb = 26
        self.__reg_spur_freq_lsb = 16
        self.__reg_spur_freq_msb = 25
        self.__reg_packet_num_lsb = 12
        self.__reg_packet_num_msb = 15
        self.__reg_packet_gain_lsb = 4
        self.__reg_packet_gain_msb = 11
        self.__reg_packet_rate_lsb = 0
        self.__reg_packet_rate_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_spur_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_spur_en_msb, self.__reg_spur_en_lsb)
    @reg_spur_en.setter
    def reg_spur_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_spur_en_msb, self.__reg_spur_en_lsb, value)

    @property
    def reg_spur_freq(self):
        return self.__MEM.rdm(self.__addr, self.__reg_spur_freq_msb, self.__reg_spur_freq_lsb)
    @reg_spur_freq.setter
    def reg_spur_freq(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_spur_freq_msb, self.__reg_spur_freq_lsb, value)

    @property
    def reg_packet_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_packet_num_msb, self.__reg_packet_num_lsb)
    @reg_packet_num.setter
    def reg_packet_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_packet_num_msb, self.__reg_packet_num_lsb, value)

    @property
    def reg_packet_gain(self):
        return self.__MEM.rdm(self.__addr, self.__reg_packet_gain_msb, self.__reg_packet_gain_lsb)
    @reg_packet_gain.setter
    def reg_packet_gain(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_packet_gain_msb, self.__reg_packet_gain_lsb, value)

    @property
    def reg_packet_rate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_packet_rate_msb, self.__reg_packet_rate_lsb)
    @reg_packet_rate.setter
    def reg_packet_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_packet_rate_msb, self.__reg_packet_rate_lsb, value)
class BB_HT40_DUG1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_TX_BASE + 0xc
        self.__reg_packet_cbw_lsb = 24
        self.__reg_packet_cbw_msb = 24
        self.__reg_packet_len_lsb = 8
        self.__reg_packet_len_msb = 23
        self.__reg_packet_idle_time_lsb = 0
        self.__reg_packet_idle_time_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_packet_cbw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_packet_cbw_msb, self.__reg_packet_cbw_lsb)
    @reg_packet_cbw.setter
    def reg_packet_cbw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_packet_cbw_msb, self.__reg_packet_cbw_lsb, value)

    @property
    def reg_packet_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_packet_len_msb, self.__reg_packet_len_lsb)
    @reg_packet_len.setter
    def reg_packet_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_packet_len_msb, self.__reg_packet_len_lsb, value)

    @property
    def reg_packet_idle_time(self):
        return self.__MEM.rdm(self.__addr, self.__reg_packet_idle_time_msb, self.__reg_packet_idle_time_lsb)
    @reg_packet_idle_time.setter
    def reg_packet_idle_time(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_packet_idle_time_msb, self.__reg_packet_idle_time_lsb, value)
class BB_IQ_MIS_CORR0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_TX_BASE + 0x10
        self.__reg_iq_mis_coef1_lsb = 16
        self.__reg_iq_mis_coef1_msb = 26
        self.__reg_tx_iqam_x2_lsb = 12
        self.__reg_tx_iqam_x2_msb = 12
        self.__reg_tx_iq_mis_corr_en_lsb = 11
        self.__reg_tx_iq_mis_corr_en_msb = 11
        self.__reg_iq_mis_coef0_lsb = 0
        self.__reg_iq_mis_coef0_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_iq_mis_coef1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef1_msb, self.__reg_iq_mis_coef1_lsb)
    @reg_iq_mis_coef1.setter
    def reg_iq_mis_coef1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef1_msb, self.__reg_iq_mis_coef1_lsb, value)

    @property
    def reg_tx_iqam_x2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_iqam_x2_msb, self.__reg_tx_iqam_x2_lsb)
    @reg_tx_iqam_x2.setter
    def reg_tx_iqam_x2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_iqam_x2_msb, self.__reg_tx_iqam_x2_lsb, value)

    @property
    def reg_tx_iq_mis_corr_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_iq_mis_corr_en_msb, self.__reg_tx_iq_mis_corr_en_lsb)
    @reg_tx_iq_mis_corr_en.setter
    def reg_tx_iq_mis_corr_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_iq_mis_corr_en_msb, self.__reg_tx_iq_mis_corr_en_lsb, value)

    @property
    def reg_iq_mis_coef0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef0_msb, self.__reg_iq_mis_coef0_lsb)
    @reg_iq_mis_coef0.setter
    def reg_iq_mis_coef0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef0_msb, self.__reg_iq_mis_coef0_lsb, value)
class BB_IQ_MIS_CORR1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_TX_BASE + 0x14
        self.__reg_iq_mis_coef3_lsb = 16
        self.__reg_iq_mis_coef3_msb = 26
        self.__reg_iq_mis_coef2_lsb = 0
        self.__reg_iq_mis_coef2_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_iq_mis_coef3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef3_msb, self.__reg_iq_mis_coef3_lsb)
    @reg_iq_mis_coef3.setter
    def reg_iq_mis_coef3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef3_msb, self.__reg_iq_mis_coef3_lsb, value)

    @property
    def reg_iq_mis_coef2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef2_msb, self.__reg_iq_mis_coef2_lsb)
    @reg_iq_mis_coef2.setter
    def reg_iq_mis_coef2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef2_msb, self.__reg_iq_mis_coef2_lsb, value)
class BB_IQ_MIS_CORR2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_TX_BASE + 0x18
        self.__reg_iq_mis_coef5_lsb = 16
        self.__reg_iq_mis_coef5_msb = 26
        self.__reg_iq_mis_coef4_lsb = 0
        self.__reg_iq_mis_coef4_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_iq_mis_coef5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef5_msb, self.__reg_iq_mis_coef5_lsb)
    @reg_iq_mis_coef5.setter
    def reg_iq_mis_coef5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef5_msb, self.__reg_iq_mis_coef5_lsb, value)

    @property
    def reg_iq_mis_coef4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef4_msb, self.__reg_iq_mis_coef4_lsb)
    @reg_iq_mis_coef4.setter
    def reg_iq_mis_coef4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef4_msb, self.__reg_iq_mis_coef4_lsb, value)
class BB_IQ_MIS_CORR3(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_TX_BASE + 0x1c
        self.__reg_iq_mis_coef7_lsb = 16
        self.__reg_iq_mis_coef7_msb = 26
        self.__reg_iq_mis_coef6_lsb = 0
        self.__reg_iq_mis_coef6_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_iq_mis_coef7(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef7_msb, self.__reg_iq_mis_coef7_lsb)
    @reg_iq_mis_coef7.setter
    def reg_iq_mis_coef7(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef7_msb, self.__reg_iq_mis_coef7_lsb, value)

    @property
    def reg_iq_mis_coef6(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef6_msb, self.__reg_iq_mis_coef6_lsb)
    @reg_iq_mis_coef6.setter
    def reg_iq_mis_coef6(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef6_msb, self.__reg_iq_mis_coef6_lsb, value)
class BB_IQ_MIS_CORR4(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_TX_BASE + 0x20
        self.__reg_iq_mis_coef9_lsb = 16
        self.__reg_iq_mis_coef9_msb = 26
        self.__reg_iq_mis_coef8_lsb = 0
        self.__reg_iq_mis_coef8_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_iq_mis_coef9(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef9_msb, self.__reg_iq_mis_coef9_lsb)
    @reg_iq_mis_coef9.setter
    def reg_iq_mis_coef9(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef9_msb, self.__reg_iq_mis_coef9_lsb, value)

    @property
    def reg_iq_mis_coef8(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef8_msb, self.__reg_iq_mis_coef8_lsb)
    @reg_iq_mis_coef8.setter
    def reg_iq_mis_coef8(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef8_msb, self.__reg_iq_mis_coef8_lsb, value)
class BB_IQ_MIS_CORR5(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_TX_BASE + 0x24
        self.__reg_iq_mis_coef11_lsb = 16
        self.__reg_iq_mis_coef11_msb = 26
        self.__reg_iq_mis_coef10_lsb = 0
        self.__reg_iq_mis_coef10_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_iq_mis_coef11(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef11_msb, self.__reg_iq_mis_coef11_lsb)
    @reg_iq_mis_coef11.setter
    def reg_iq_mis_coef11(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef11_msb, self.__reg_iq_mis_coef11_lsb, value)

    @property
    def reg_iq_mis_coef10(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef10_msb, self.__reg_iq_mis_coef10_lsb)
    @reg_iq_mis_coef10.setter
    def reg_iq_mis_coef10(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef10_msb, self.__reg_iq_mis_coef10_lsb, value)
class BB_IQ_MIS_CORR6(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_TX_BASE + 0x28
        self.__reg_iq_mis_coef13_lsb = 16
        self.__reg_iq_mis_coef13_msb = 26
        self.__reg_iq_mis_coef12_lsb = 0
        self.__reg_iq_mis_coef12_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_iq_mis_coef13(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef13_msb, self.__reg_iq_mis_coef13_lsb)
    @reg_iq_mis_coef13.setter
    def reg_iq_mis_coef13(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef13_msb, self.__reg_iq_mis_coef13_lsb, value)

    @property
    def reg_iq_mis_coef12(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef12_msb, self.__reg_iq_mis_coef12_lsb)
    @reg_iq_mis_coef12.setter
    def reg_iq_mis_coef12(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef12_msb, self.__reg_iq_mis_coef12_lsb, value)
class BB_IQ_MIS_CORR7(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_TX_BASE + 0x2c
        self.__reg_iq_mis_coef15_lsb = 16
        self.__reg_iq_mis_coef15_msb = 26
        self.__reg_iq_mis_coef14_lsb = 0
        self.__reg_iq_mis_coef14_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_iq_mis_coef15(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef15_msb, self.__reg_iq_mis_coef15_lsb)
    @reg_iq_mis_coef15.setter
    def reg_iq_mis_coef15(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef15_msb, self.__reg_iq_mis_coef15_lsb, value)

    @property
    def reg_iq_mis_coef14(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef14_msb, self.__reg_iq_mis_coef14_lsb)
    @reg_iq_mis_coef14.setter
    def reg_iq_mis_coef14(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef14_msb, self.__reg_iq_mis_coef14_lsb, value)
class BB_IQ_MIS_CORR8(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_TX_BASE + 0x30
        self.__reg_iq_mis_coef17_lsb = 16
        self.__reg_iq_mis_coef17_msb = 26
        self.__reg_iq_mis_coef16_lsb = 0
        self.__reg_iq_mis_coef16_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_iq_mis_coef17(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef17_msb, self.__reg_iq_mis_coef17_lsb)
    @reg_iq_mis_coef17.setter
    def reg_iq_mis_coef17(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef17_msb, self.__reg_iq_mis_coef17_lsb, value)

    @property
    def reg_iq_mis_coef16(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef16_msb, self.__reg_iq_mis_coef16_lsb)
    @reg_iq_mis_coef16.setter
    def reg_iq_mis_coef16(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef16_msb, self.__reg_iq_mis_coef16_lsb, value)
class BB_IQ_MIS_CORR9(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_TX_BASE + 0x34
        self.__reg_iq_mis_coef19_lsb = 16
        self.__reg_iq_mis_coef19_msb = 26
        self.__reg_iq_mis_coef18_lsb = 0
        self.__reg_iq_mis_coef18_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_iq_mis_coef19(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef19_msb, self.__reg_iq_mis_coef19_lsb)
    @reg_iq_mis_coef19.setter
    def reg_iq_mis_coef19(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef19_msb, self.__reg_iq_mis_coef19_lsb, value)

    @property
    def reg_iq_mis_coef18(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef18_msb, self.__reg_iq_mis_coef18_lsb)
    @reg_iq_mis_coef18.setter
    def reg_iq_mis_coef18(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef18_msb, self.__reg_iq_mis_coef18_lsb, value)
class BB_IQ_MIS_CORR10(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_TX_BASE + 0x38
        self.__reg_iq_mis_coef21_lsb = 16
        self.__reg_iq_mis_coef21_msb = 26
        self.__reg_iq_mis_coef20_lsb = 0
        self.__reg_iq_mis_coef20_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_iq_mis_coef21(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef21_msb, self.__reg_iq_mis_coef21_lsb)
    @reg_iq_mis_coef21.setter
    def reg_iq_mis_coef21(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef21_msb, self.__reg_iq_mis_coef21_lsb, value)

    @property
    def reg_iq_mis_coef20(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef20_msb, self.__reg_iq_mis_coef20_lsb)
    @reg_iq_mis_coef20.setter
    def reg_iq_mis_coef20(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef20_msb, self.__reg_iq_mis_coef20_lsb, value)
class BB_IQ_MIS_CORR11(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_TX_BASE + 0x3c
        self.__reg_iq_mis_coef23_lsb = 16
        self.__reg_iq_mis_coef23_msb = 26
        self.__reg_iq_mis_coef22_lsb = 0
        self.__reg_iq_mis_coef22_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_iq_mis_coef23(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef23_msb, self.__reg_iq_mis_coef23_lsb)
    @reg_iq_mis_coef23.setter
    def reg_iq_mis_coef23(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef23_msb, self.__reg_iq_mis_coef23_lsb, value)

    @property
    def reg_iq_mis_coef22(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef22_msb, self.__reg_iq_mis_coef22_lsb)
    @reg_iq_mis_coef22.setter
    def reg_iq_mis_coef22(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef22_msb, self.__reg_iq_mis_coef22_lsb, value)
class BB_IQ_MIS_CORR12(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_TX_BASE + 0x40
        self.__reg_iq_mis_coef25_lsb = 16
        self.__reg_iq_mis_coef25_msb = 26
        self.__reg_iq_mis_coef24_lsb = 0
        self.__reg_iq_mis_coef24_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_iq_mis_coef25(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef25_msb, self.__reg_iq_mis_coef25_lsb)
    @reg_iq_mis_coef25.setter
    def reg_iq_mis_coef25(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef25_msb, self.__reg_iq_mis_coef25_lsb, value)

    @property
    def reg_iq_mis_coef24(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef24_msb, self.__reg_iq_mis_coef24_lsb)
    @reg_iq_mis_coef24.setter
    def reg_iq_mis_coef24(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef24_msb, self.__reg_iq_mis_coef24_lsb, value)
class BB_IQ_MIS_CORR13(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_TX_BASE + 0x44
        self.__reg_iq_mis_coef27_lsb = 16
        self.__reg_iq_mis_coef27_msb = 26
        self.__reg_iq_mis_coef26_lsb = 0
        self.__reg_iq_mis_coef26_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_iq_mis_coef27(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef27_msb, self.__reg_iq_mis_coef27_lsb)
    @reg_iq_mis_coef27.setter
    def reg_iq_mis_coef27(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef27_msb, self.__reg_iq_mis_coef27_lsb, value)

    @property
    def reg_iq_mis_coef26(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef26_msb, self.__reg_iq_mis_coef26_lsb)
    @reg_iq_mis_coef26.setter
    def reg_iq_mis_coef26(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef26_msb, self.__reg_iq_mis_coef26_lsb, value)
class BB_IQ_MIS_CORR14(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_TX_BASE + 0x48
        self.__reg_iq_mis_coef29_lsb = 16
        self.__reg_iq_mis_coef29_msb = 26
        self.__reg_iq_mis_coef28_lsb = 0
        self.__reg_iq_mis_coef28_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_iq_mis_coef29(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef29_msb, self.__reg_iq_mis_coef29_lsb)
    @reg_iq_mis_coef29.setter
    def reg_iq_mis_coef29(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef29_msb, self.__reg_iq_mis_coef29_lsb, value)

    @property
    def reg_iq_mis_coef28(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef28_msb, self.__reg_iq_mis_coef28_lsb)
    @reg_iq_mis_coef28.setter
    def reg_iq_mis_coef28(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef28_msb, self.__reg_iq_mis_coef28_lsb, value)
class BB_IQ_MIS_CORR15(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_TX_BASE + 0x4c
        self.__reg_iq_mis_coef31_lsb = 16
        self.__reg_iq_mis_coef31_msb = 26
        self.__reg_iq_mis_coef30_lsb = 0
        self.__reg_iq_mis_coef30_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_iq_mis_coef31(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef31_msb, self.__reg_iq_mis_coef31_lsb)
    @reg_iq_mis_coef31.setter
    def reg_iq_mis_coef31(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef31_msb, self.__reg_iq_mis_coef31_lsb, value)

    @property
    def reg_iq_mis_coef30(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_mis_coef30_msb, self.__reg_iq_mis_coef30_lsb)
    @reg_iq_mis_coef30.setter
    def reg_iq_mis_coef30(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_mis_coef30_msb, self.__reg_iq_mis_coef30_lsb, value)
class BB_TX_TEST(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_TX_BASE + 0x50
        self.__reg_bbtx_clkgate6_en_lsb = 6
        self.__reg_bbtx_clkgate6_en_msb = 6
        self.__reg_bbtx_clkgate5_en_lsb = 5
        self.__reg_bbtx_clkgate5_en_msb = 5
        self.__reg_bbtx_clkgate4_en_lsb = 4
        self.__reg_bbtx_clkgate4_en_msb = 4
        self.__reg_bbtx_clkgate3_en_lsb = 3
        self.__reg_bbtx_clkgate3_en_msb = 3
        self.__reg_bbtx_clkgate2_en_lsb = 2
        self.__reg_bbtx_clkgate2_en_msb = 2
        self.__reg_bbtx_clkgate1_en_lsb = 1
        self.__reg_bbtx_clkgate1_en_msb = 1
        self.__reg_bbtxclk_en_lsb = 0
        self.__reg_bbtxclk_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bbtx_clkgate6_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbtx_clkgate6_en_msb, self.__reg_bbtx_clkgate6_en_lsb)
    @reg_bbtx_clkgate6_en.setter
    def reg_bbtx_clkgate6_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbtx_clkgate6_en_msb, self.__reg_bbtx_clkgate6_en_lsb, value)

    @property
    def reg_bbtx_clkgate5_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbtx_clkgate5_en_msb, self.__reg_bbtx_clkgate5_en_lsb)
    @reg_bbtx_clkgate5_en.setter
    def reg_bbtx_clkgate5_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbtx_clkgate5_en_msb, self.__reg_bbtx_clkgate5_en_lsb, value)

    @property
    def reg_bbtx_clkgate4_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbtx_clkgate4_en_msb, self.__reg_bbtx_clkgate4_en_lsb)
    @reg_bbtx_clkgate4_en.setter
    def reg_bbtx_clkgate4_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbtx_clkgate4_en_msb, self.__reg_bbtx_clkgate4_en_lsb, value)

    @property
    def reg_bbtx_clkgate3_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbtx_clkgate3_en_msb, self.__reg_bbtx_clkgate3_en_lsb)
    @reg_bbtx_clkgate3_en.setter
    def reg_bbtx_clkgate3_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbtx_clkgate3_en_msb, self.__reg_bbtx_clkgate3_en_lsb, value)

    @property
    def reg_bbtx_clkgate2_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbtx_clkgate2_en_msb, self.__reg_bbtx_clkgate2_en_lsb)
    @reg_bbtx_clkgate2_en.setter
    def reg_bbtx_clkgate2_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbtx_clkgate2_en_msb, self.__reg_bbtx_clkgate2_en_lsb, value)

    @property
    def reg_bbtx_clkgate1_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbtx_clkgate1_en_msb, self.__reg_bbtx_clkgate1_en_lsb)
    @reg_bbtx_clkgate1_en.setter
    def reg_bbtx_clkgate1_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbtx_clkgate1_en_msb, self.__reg_bbtx_clkgate1_en_lsb, value)

    @property
    def reg_bbtxclk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbtxclk_en_msb, self.__reg_bbtxclk_en_lsb)
    @reg_bbtxclk_en.setter
    def reg_bbtxclk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbtxclk_en_msb, self.__reg_bbtxclk_en_lsb, value)
class BB_BTX_NOISE_I(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_TX_BASE + 0x54
        self.__btx_bkn_scale_i_lsb = 19
        self.__btx_bkn_scale_i_msb = 19
        self.__btx_bkn_num_i_lsb = 15
        self.__btx_bkn_num_i_msb = 18
        self.__btx_bkn_thn_i_lsb = 8
        self.__btx_bkn_thn_i_msb = 14
        self.__btx_bkn_seed_i_lsb = 1
        self.__btx_bkn_seed_i_msb = 7
        self.__btx_bkn_enable_lsb = 0
        self.__btx_bkn_enable_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def btx_bkn_scale_i(self):
        return self.__MEM.rdm(self.__addr, self.__btx_bkn_scale_i_msb, self.__btx_bkn_scale_i_lsb)
    @btx_bkn_scale_i.setter
    def btx_bkn_scale_i(self, value):
        return self.__MEM.wrm(self.__addr, self.__btx_bkn_scale_i_msb, self.__btx_bkn_scale_i_lsb, value)

    @property
    def btx_bkn_num_i(self):
        return self.__MEM.rdm(self.__addr, self.__btx_bkn_num_i_msb, self.__btx_bkn_num_i_lsb)
    @btx_bkn_num_i.setter
    def btx_bkn_num_i(self, value):
        return self.__MEM.wrm(self.__addr, self.__btx_bkn_num_i_msb, self.__btx_bkn_num_i_lsb, value)

    @property
    def btx_bkn_thn_i(self):
        return self.__MEM.rdm(self.__addr, self.__btx_bkn_thn_i_msb, self.__btx_bkn_thn_i_lsb)
    @btx_bkn_thn_i.setter
    def btx_bkn_thn_i(self, value):
        return self.__MEM.wrm(self.__addr, self.__btx_bkn_thn_i_msb, self.__btx_bkn_thn_i_lsb, value)

    @property
    def btx_bkn_seed_i(self):
        return self.__MEM.rdm(self.__addr, self.__btx_bkn_seed_i_msb, self.__btx_bkn_seed_i_lsb)
    @btx_bkn_seed_i.setter
    def btx_bkn_seed_i(self, value):
        return self.__MEM.wrm(self.__addr, self.__btx_bkn_seed_i_msb, self.__btx_bkn_seed_i_lsb, value)

    @property
    def btx_bkn_enable(self):
        return self.__MEM.rdm(self.__addr, self.__btx_bkn_enable_msb, self.__btx_bkn_enable_lsb)
    @btx_bkn_enable.setter
    def btx_bkn_enable(self, value):
        return self.__MEM.wrm(self.__addr, self.__btx_bkn_enable_msb, self.__btx_bkn_enable_lsb, value)
class BB_BTX_NOISE_Q(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_TX_BASE + 0x58
        self.__reg_btx_infinite_lsb = 20
        self.__reg_btx_infinite_msb = 20
        self.__btx_bkn_scale_q_lsb = 19
        self.__btx_bkn_scale_q_msb = 19
        self.__btx_bkn_num_q_lsb = 15
        self.__btx_bkn_num_q_msb = 18
        self.__btx_bkn_thn_q_lsb = 8
        self.__btx_bkn_thn_q_msb = 14
        self.__btx_bkn_seed_q_lsb = 1
        self.__btx_bkn_seed_q_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_btx_infinite(self):
        return self.__MEM.rdm(self.__addr, self.__reg_btx_infinite_msb, self.__reg_btx_infinite_lsb)
    @reg_btx_infinite.setter
    def reg_btx_infinite(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_btx_infinite_msb, self.__reg_btx_infinite_lsb, value)

    @property
    def btx_bkn_scale_q(self):
        return self.__MEM.rdm(self.__addr, self.__btx_bkn_scale_q_msb, self.__btx_bkn_scale_q_lsb)
    @btx_bkn_scale_q.setter
    def btx_bkn_scale_q(self, value):
        return self.__MEM.wrm(self.__addr, self.__btx_bkn_scale_q_msb, self.__btx_bkn_scale_q_lsb, value)

    @property
    def btx_bkn_num_q(self):
        return self.__MEM.rdm(self.__addr, self.__btx_bkn_num_q_msb, self.__btx_bkn_num_q_lsb)
    @btx_bkn_num_q.setter
    def btx_bkn_num_q(self, value):
        return self.__MEM.wrm(self.__addr, self.__btx_bkn_num_q_msb, self.__btx_bkn_num_q_lsb, value)

    @property
    def btx_bkn_thn_q(self):
        return self.__MEM.rdm(self.__addr, self.__btx_bkn_thn_q_msb, self.__btx_bkn_thn_q_lsb)
    @btx_bkn_thn_q.setter
    def btx_bkn_thn_q(self, value):
        return self.__MEM.wrm(self.__addr, self.__btx_bkn_thn_q_msb, self.__btx_bkn_thn_q_lsb, value)

    @property
    def btx_bkn_seed_q(self):
        return self.__MEM.rdm(self.__addr, self.__btx_bkn_seed_q_msb, self.__btx_bkn_seed_q_lsb)
    @btx_bkn_seed_q.setter
    def btx_bkn_seed_q(self, value):
        return self.__MEM.wrm(self.__addr, self.__btx_bkn_seed_q_msb, self.__btx_bkn_seed_q_lsb, value)
class BB_BTX_LR(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_TX_BASE + 0x5c
        self.__reg_lr_pre_conf_lsb = 16
        self.__reg_lr_pre_conf_msb = 23
        self.__reg_lr_short_pre_len_lsb = 8
        self.__reg_lr_short_pre_len_msb = 13
        self.__reg_lr_pre_len_lsb = 0
        self.__reg_lr_pre_len_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_lr_pre_conf(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_pre_conf_msb, self.__reg_lr_pre_conf_lsb)
    @reg_lr_pre_conf.setter
    def reg_lr_pre_conf(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_pre_conf_msb, self.__reg_lr_pre_conf_lsb, value)

    @property
    def reg_lr_short_pre_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_short_pre_len_msb, self.__reg_lr_short_pre_len_lsb)
    @reg_lr_short_pre_len.setter
    def reg_lr_short_pre_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_short_pre_len_msb, self.__reg_lr_short_pre_len_lsb, value)

    @property
    def reg_lr_pre_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_pre_len_msb, self.__reg_lr_pre_len_lsb)
    @reg_lr_pre_len.setter
    def reg_lr_pre_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_pre_len_msb, self.__reg_lr_pre_len_lsb, value)
class BB_BTX_LR_CONF(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_TX_BASE + 0x60
        self.__reg_lr_rate_sdf_lsb = 16
        self.__reg_lr_rate_sdf_msb = 31
        self.__reg_lr_rate_conf_lsb = 0
        self.__reg_lr_rate_conf_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_lr_rate_sdf(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_rate_sdf_msb, self.__reg_lr_rate_sdf_lsb)
    @reg_lr_rate_sdf.setter
    def reg_lr_rate_sdf(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_rate_sdf_msb, self.__reg_lr_rate_sdf_lsb, value)

    @property
    def reg_lr_rate_conf(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_rate_conf_msb, self.__reg_lr_rate_conf_lsb)
    @reg_lr_rate_conf.setter
    def reg_lr_rate_conf(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_rate_conf_msb, self.__reg_lr_rate_conf_lsb, value)
class BBTXDATE(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BB_TX_BASE + 0x3fc
        self.__reg_bbtx_date_lsb = 0
        self.__reg_bbtx_date_msb = 27
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bbtx_date(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbtx_date_msb, self.__reg_bbtx_date_lsb)
    @reg_bbtx_date.setter
    def reg_bbtx_date(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbtx_date_msb, self.__reg_bbtx_date_lsb, value)
    @property
    def default_value(self):
        return 0x1804080
