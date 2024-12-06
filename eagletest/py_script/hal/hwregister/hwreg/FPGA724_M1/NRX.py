from hal.common import *
from hal.hwregister.hwreg.FPGA724_M1.addr_base import *
class NRX(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.NRXSCALE = NRXSCALE(self.channel, self.chipv)
        self.NRXFTE = NRXFTE(self.channel, self.chipv)
        self.NRXTDM1 = NRXTDM1(self.channel, self.chipv)
        self.NRXMODE = NRXMODE(self.channel, self.chipv)
        self.NRXSPURV0 = NRXSPURV0(self.channel, self.chipv)
        self.NRXSPURV1 = NRXSPURV1(self.channel, self.chipv)
        self.NRXSPURV2 = NRXSPURV2(self.channel, self.chipv)
        self.NRXSPURV3 = NRXSPURV3(self.channel, self.chipv)
        self.NRXSPURV4 = NRXSPURV4(self.channel, self.chipv)
        self.NRXSPURV5 = NRXSPURV5(self.channel, self.chipv)
        self.NRXSPURV6 = NRXSPURV6(self.channel, self.chipv)
        self.NRXSPURV7 = NRXSPURV7(self.channel, self.chipv)
        self.NRXSPURFV1 = NRXSPURFV1(self.channel, self.chipv)
        self.NRXSPURFV2 = NRXSPURFV2(self.channel, self.chipv)
        self.NRXSPURC = NRXSPURC(self.channel, self.chipv)
        self.NRXFOE = NRXFOE(self.channel, self.chipv)
        self.NRXVIT = NRXVIT(self.channel, self.chipv)
        self.NRXFREQPARA = NRXFREQPARA(self.channel, self.chipv)
        self.NRXMODUSCALEAWGN0 = NRXMODUSCALEAWGN0(self.channel, self.chipv)
        self.NRXTEST0 = NRXTEST0(self.channel, self.chipv)
        self.NRXTEST1 = NRXTEST1(self.channel, self.chipv)
        self.NRXFDM1 = NRXFDM1(self.channel, self.chipv)
        self.NRXDEBUG = NRXDEBUG(self.channel, self.chipv)
        self.NRXCTE_CTRL0 = NRXCTE_CTRL0(self.channel, self.chipv)
        self.NRXCTE_CTRL1 = NRXCTE_CTRL1(self.channel, self.chipv)
        self.NRXCTE_CTRL2 = NRXCTE_CTRL2(self.channel, self.chipv)
        self.NRXCTE_CTRL3 = NRXCTE_CTRL3(self.channel, self.chipv)
        self.NRXFREQREG = NRXFREQREG(self.channel, self.chipv)
        self.BB_NRX_TEST = BB_NRX_TEST(self.channel, self.chipv)
        self.NRXPILOTCONF0 = NRXPILOTCONF0(self.channel, self.chipv)
        self.NRXPILOTCONF1 = NRXPILOTCONF1(self.channel, self.chipv)
        self.NRXPILOTCONF2 = NRXPILOTCONF2(self.channel, self.chipv)
        self.NRXPILOTCONF3 = NRXPILOTCONF3(self.channel, self.chipv)
        self.NRXCHAN_RATE_THR1 = NRXCHAN_RATE_THR1(self.channel, self.chipv)
        self.NRXCHAN_RATE_THR2 = NRXCHAN_RATE_THR2(self.channel, self.chipv)
        self.NRXLSIGEVM0 = NRXLSIGEVM0(self.channel, self.chipv)
        self.NRXLSIGEVM1 = NRXLSIGEVM1(self.channel, self.chipv)
        self.NRXSPURV8 = NRXSPURV8(self.channel, self.chipv)
        self.NRXPILOTCONF4 = NRXPILOTCONF4(self.channel, self.chipv)
        self.NRXPILOTCONF5 = NRXPILOTCONF5(self.channel, self.chipv)
        self.NRXPILOTCONF6 = NRXPILOTCONF6(self.channel, self.chipv)
        self.NRXPILOTCONF7 = NRXPILOTCONF7(self.channel, self.chipv)
        self.NRXPILOTCONF8 = NRXPILOTCONF8(self.channel, self.chipv)
        self.NRXTDM2 = NRXTDM2(self.channel, self.chipv)
        self.NRXCTE_CTRL4 = NRXCTE_CTRL4(self.channel, self.chipv)
        self.NRXCTE_CTRL5 = NRXCTE_CTRL5(self.channel, self.chipv)
        self.NRXPD_CTRL = NRXPD_CTRL(self.channel, self.chipv)
        self.NRXFTE1 = NRXFTE1(self.channel, self.chipv)
        self.NRXTDM3 = NRXTDM3(self.channel, self.chipv)
        self.NRXCTE_CTRL6 = NRXCTE_CTRL6(self.channel, self.chipv)
        self.NRXCTE_CTRL7 = NRXCTE_CTRL7(self.channel, self.chipv)
        self.NRXPILOTCONF9 = NRXPILOTCONF9(self.channel, self.chipv)
        self.NRXCLKGATE = NRXCLKGATE(self.channel, self.chipv)
        self.NRXPILOTCONF10 = NRXPILOTCONF10(self.channel, self.chipv)
        self.NRXPILOTCONF11 = NRXPILOTCONF11(self.channel, self.chipv)
        self.NRXCHANESTFILTCONF0 = NRXCHANESTFILTCONF0(self.channel, self.chipv)
        self.NRXCHANESTFILTCONF1 = NRXCHANESTFILTCONF1(self.channel, self.chipv)
        self.NRXFSM_DEBUG0 = NRXFSM_DEBUG0(self.channel, self.chipv)
        self.NRXCHANESTWEIGHTSELDOWN = NRXCHANESTWEIGHTSELDOWN(self.channel, self.chipv)
        self.NRXCHANESTWEIGHTSELUP = NRXCHANESTWEIGHTSELUP(self.channel, self.chipv)
        self.NRXCHANDUMP = NRXCHANDUMP(self.channel, self.chipv)
        self.NRXSIMDUG0 = NRXSIMDUG0(self.channel, self.chipv)
        self.NRXFFTSCALE = NRXFFTSCALE(self.channel, self.chipv)
        self.NRXSNRDEMAPTHR = NRXSNRDEMAPTHR(self.channel, self.chipv)
        self.NRXSOFTBITWIGHT = NRXSOFTBITWIGHT(self.channel, self.chipv)
        self.NRXCHANSELTHR0 = NRXCHANSELTHR0(self.channel, self.chipv)
        self.NRXTDM4 = NRXTDM4(self.channel, self.chipv)
        self.NRXFOEHTRANGE = NRXFOEHTRANGE(self.channel, self.chipv)
        self.NRXMODUSCALESTBC0 = NRXMODUSCALESTBC0(self.channel, self.chipv)
        self.NRXMODUSCALESTBC1 = NRXMODUSCALESTBC1(self.channel, self.chipv)
        self.NRXMODUSCALEAWGN1 = NRXMODUSCALEAWGN1(self.channel, self.chipv)
        self.NRXMODUSCALEMP0 = NRXMODUSCALEMP0(self.channel, self.chipv)
        self.NRXMODUSCALEMP1 = NRXMODUSCALEMP1(self.channel, self.chipv)
        self.NRXPOWMARGINSEL = NRXPOWMARGINSEL(self.channel, self.chipv)
        self.NRXFTM_CFG = NRXFTM_CFG(self.channel, self.chipv)
        self.NRXFTM_CFG2 = NRXFTM_CFG2(self.channel, self.chipv)
        self.NRXCHANSELTHR1 = NRXCHANSELTHR1(self.channel, self.chipv)
        self.NRXPILOTCONF12 = NRXPILOTCONF12(self.channel, self.chipv)
        self.NRXPILOTCONF13 = NRXPILOTCONF13(self.channel, self.chipv)
        self.NRXPILOTCONF14 = NRXPILOTCONF14(self.channel, self.chipv)
        self.NRXPILOTCONF15 = NRXPILOTCONF15(self.channel, self.chipv)
        self.NRXSIMDUG1 = NRXSIMDUG1(self.channel, self.chipv)
        self.NRXDATE = NRXDATE(self.channel, self.chipv)
class NRXSCALE(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x0
        self.__reg_fft_gain_opt_lsb = 28
        self.__reg_fft_gain_opt_msb = 28
        self.__reg_fft_scale_force_lsb = 20
        self.__reg_fft_scale_force_msb = 27
        self.__reg_fft_scale_force_en_lsb = 19
        self.__reg_fft_scale_force_en_msb = 19
        self.__reg_fft_scale_en_lsb = 18
        self.__reg_fft_scale_en_msb = 18
        self.__reg_fft_scale_tar_lsb = 8
        self.__reg_fft_scale_tar_msb = 17
        self.__reg_pwr_est_shift_change_en_lsb = 7
        self.__reg_pwr_est_shift_change_en_msb = 7
        self.__reg_rx_mod_mult_lsb = 4
        self.__reg_rx_mod_mult_msb = 6
        self.__reg_rx_mod_shr_lsb = 2
        self.__reg_rx_mod_shr_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_fft_gain_opt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fft_gain_opt_msb, self.__reg_fft_gain_opt_lsb)
    @reg_fft_gain_opt.setter
    def reg_fft_gain_opt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fft_gain_opt_msb, self.__reg_fft_gain_opt_lsb, value)

    @property
    def reg_fft_scale_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fft_scale_force_msb, self.__reg_fft_scale_force_lsb)
    @reg_fft_scale_force.setter
    def reg_fft_scale_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fft_scale_force_msb, self.__reg_fft_scale_force_lsb, value)

    @property
    def reg_fft_scale_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fft_scale_force_en_msb, self.__reg_fft_scale_force_en_lsb)
    @reg_fft_scale_force_en.setter
    def reg_fft_scale_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fft_scale_force_en_msb, self.__reg_fft_scale_force_en_lsb, value)

    @property
    def reg_fft_scale_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fft_scale_en_msb, self.__reg_fft_scale_en_lsb)
    @reg_fft_scale_en.setter
    def reg_fft_scale_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fft_scale_en_msb, self.__reg_fft_scale_en_lsb, value)

    @property
    def reg_fft_scale_tar(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fft_scale_tar_msb, self.__reg_fft_scale_tar_lsb)
    @reg_fft_scale_tar.setter
    def reg_fft_scale_tar(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fft_scale_tar_msb, self.__reg_fft_scale_tar_lsb, value)

    @property
    def reg_pwr_est_shift_change_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_est_shift_change_en_msb, self.__reg_pwr_est_shift_change_en_lsb)
    @reg_pwr_est_shift_change_en.setter
    def reg_pwr_est_shift_change_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_est_shift_change_en_msb, self.__reg_pwr_est_shift_change_en_lsb, value)

    @property
    def reg_rx_mod_mult(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_mod_mult_msb, self.__reg_rx_mod_mult_lsb)
    @reg_rx_mod_mult.setter
    def reg_rx_mod_mult(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_mod_mult_msb, self.__reg_rx_mod_mult_lsb, value)

    @property
    def reg_rx_mod_shr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_mod_shr_msb, self.__reg_rx_mod_shr_lsb)
    @reg_rx_mod_shr.setter
    def reg_rx_mod_shr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_mod_shr_msb, self.__reg_rx_mod_shr_lsb, value)
class NRXFTE(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x4
        self.__reg_fte_spur_mask_en_lsb = 31
        self.__reg_fte_spur_mask_en_msb = 31
        self.__reg_fte_data_rate_lsb = 28
        self.__reg_fte_data_rate_msb = 30
        self.__reg_fte_err_en_lsb = 27
        self.__reg_fte_err_en_msb = 27
        self.__reg_fte_max_lsb = 19
        self.__reg_fte_max_msb = 26
        self.__reg_fte_min_lsb = 12
        self.__reg_fte_min_msb = 18
        self.__reg_fte_err_mode_lsb = 11
        self.__reg_fte_err_mode_msb = 11
        self.__reg_nrx_fte_mode2_lsb = 10
        self.__reg_nrx_fte_mode2_msb = 10
        self.__reg_nrx_fte_en_lsb = 9
        self.__reg_nrx_fte_en_msb = 9
        self.__reg_fte_tar_backoff_lsb = 2
        self.__reg_fte_tar_backoff_msb = 8
        self.__reg_fte_htltf2_stbc_avg_en_lsb = 1
        self.__reg_fte_htltf2_stbc_avg_en_msb = 1
        self.__reg_fte_htltf_ext_lsb = 0
        self.__reg_fte_htltf_ext_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_fte_spur_mask_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fte_spur_mask_en_msb, self.__reg_fte_spur_mask_en_lsb)
    @reg_fte_spur_mask_en.setter
    def reg_fte_spur_mask_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fte_spur_mask_en_msb, self.__reg_fte_spur_mask_en_lsb, value)

    @property
    def reg_fte_data_rate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fte_data_rate_msb, self.__reg_fte_data_rate_lsb)
    @reg_fte_data_rate.setter
    def reg_fte_data_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fte_data_rate_msb, self.__reg_fte_data_rate_lsb, value)

    @property
    def reg_fte_err_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fte_err_en_msb, self.__reg_fte_err_en_lsb)
    @reg_fte_err_en.setter
    def reg_fte_err_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fte_err_en_msb, self.__reg_fte_err_en_lsb, value)

    @property
    def reg_fte_max(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fte_max_msb, self.__reg_fte_max_lsb)
    @reg_fte_max.setter
    def reg_fte_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fte_max_msb, self.__reg_fte_max_lsb, value)

    @property
    def reg_fte_min(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fte_min_msb, self.__reg_fte_min_lsb)
    @reg_fte_min.setter
    def reg_fte_min(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fte_min_msb, self.__reg_fte_min_lsb, value)

    @property
    def reg_fte_err_mode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fte_err_mode_msb, self.__reg_fte_err_mode_lsb)
    @reg_fte_err_mode.setter
    def reg_fte_err_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fte_err_mode_msb, self.__reg_fte_err_mode_lsb, value)

    @property
    def reg_nrx_fte_mode2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_nrx_fte_mode2_msb, self.__reg_nrx_fte_mode2_lsb)
    @reg_nrx_fte_mode2.setter
    def reg_nrx_fte_mode2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_nrx_fte_mode2_msb, self.__reg_nrx_fte_mode2_lsb, value)

    @property
    def reg_nrx_fte_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_nrx_fte_en_msb, self.__reg_nrx_fte_en_lsb)
    @reg_nrx_fte_en.setter
    def reg_nrx_fte_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_nrx_fte_en_msb, self.__reg_nrx_fte_en_lsb, value)

    @property
    def reg_fte_tar_backoff(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fte_tar_backoff_msb, self.__reg_fte_tar_backoff_lsb)
    @reg_fte_tar_backoff.setter
    def reg_fte_tar_backoff(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fte_tar_backoff_msb, self.__reg_fte_tar_backoff_lsb, value)

    @property
    def reg_fte_htltf2_stbc_avg_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fte_htltf2_stbc_avg_en_msb, self.__reg_fte_htltf2_stbc_avg_en_lsb)
    @reg_fte_htltf2_stbc_avg_en.setter
    def reg_fte_htltf2_stbc_avg_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fte_htltf2_stbc_avg_en_msb, self.__reg_fte_htltf2_stbc_avg_en_lsb, value)

    @property
    def reg_fte_htltf_ext(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fte_htltf_ext_msb, self.__reg_fte_htltf_ext_lsb)
    @reg_fte_htltf_ext.setter
    def reg_fte_htltf_ext(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fte_htltf_ext_msb, self.__reg_fte_htltf_ext_lsb, value)
class NRXTDM1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x8
        self.__reg_xcorr_en_end_t_lsb = 20
        self.__reg_xcorr_en_end_t_msb = 28
        self.__reg_foe_use_cte_lsb = 19
        self.__reg_foe_use_cte_msb = 19
        self.__reg_tdm_wait_end_lsb = 15
        self.__reg_tdm_wait_end_msb = 18
        self.__reg_xcorr_en_lsb = 14
        self.__reg_xcorr_en_msb = 14
        self.__reg_xcorr_find_thr2_lsb = 7
        self.__reg_xcorr_find_thr2_msb = 13
        self.__reg_xcorr_find_thr1_lsb = 0
        self.__reg_xcorr_find_thr1_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_xcorr_en_end_t(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_en_end_t_msb, self.__reg_xcorr_en_end_t_lsb)
    @reg_xcorr_en_end_t.setter
    def reg_xcorr_en_end_t(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_en_end_t_msb, self.__reg_xcorr_en_end_t_lsb, value)

    @property
    def reg_foe_use_cte(self):
        return self.__MEM.rdm(self.__addr, self.__reg_foe_use_cte_msb, self.__reg_foe_use_cte_lsb)
    @reg_foe_use_cte.setter
    def reg_foe_use_cte(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_foe_use_cte_msb, self.__reg_foe_use_cte_lsb, value)

    @property
    def reg_tdm_wait_end(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tdm_wait_end_msb, self.__reg_tdm_wait_end_lsb)
    @reg_tdm_wait_end.setter
    def reg_tdm_wait_end(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tdm_wait_end_msb, self.__reg_tdm_wait_end_lsb, value)

    @property
    def reg_xcorr_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_en_msb, self.__reg_xcorr_en_lsb)
    @reg_xcorr_en.setter
    def reg_xcorr_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_en_msb, self.__reg_xcorr_en_lsb, value)

    @property
    def reg_xcorr_find_thr2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_find_thr2_msb, self.__reg_xcorr_find_thr2_lsb)
    @reg_xcorr_find_thr2.setter
    def reg_xcorr_find_thr2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_find_thr2_msb, self.__reg_xcorr_find_thr2_lsb, value)

    @property
    def reg_xcorr_find_thr1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_find_thr1_msb, self.__reg_xcorr_find_thr1_lsb)
    @reg_xcorr_find_thr1.setter
    def reg_xcorr_find_thr1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_find_thr1_msb, self.__reg_xcorr_find_thr1_lsb, value)
class NRXMODE(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0xc
        self.__reg_cfo_start_3_lsb = 24
        self.__reg_cfo_start_3_msb = 31
        self.__reg_weight_pick_up_force_lsb = 22
        self.__reg_weight_pick_up_force_msb = 22
        self.__reg_weight_pick_down_force_lsb = 21
        self.__reg_weight_pick_down_force_msb = 21
        self.__reg_chan_interp_dep_sm_lsb = 20
        self.__reg_chan_interp_dep_sm_msb = 20
        self.__reg_cfo_start_2_lsb = 12
        self.__reg_cfo_start_2_msb = 19
        self.__reg_cfo_start_1_lsb = 4
        self.__reg_cfo_start_1_msb = 11
        self.__reg_htltf_sgi_retim_en_lsb = 3
        self.__reg_htltf_sgi_retim_en_msb = 3
        self.__reg_chan_spur_interp_en_lsb = 2
        self.__reg_chan_spur_interp_en_msb = 2
        self.__reg_ht20_data_40m_lsb = 1
        self.__reg_ht20_data_40m_msb = 1
        self.__reg_ht40_pri_up_lsb = 0
        self.__reg_ht40_pri_up_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_cfo_start_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cfo_start_3_msb, self.__reg_cfo_start_3_lsb)
    @reg_cfo_start_3.setter
    def reg_cfo_start_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cfo_start_3_msb, self.__reg_cfo_start_3_lsb, value)

    @property
    def reg_weight_pick_up_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_weight_pick_up_force_msb, self.__reg_weight_pick_up_force_lsb)
    @reg_weight_pick_up_force.setter
    def reg_weight_pick_up_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_weight_pick_up_force_msb, self.__reg_weight_pick_up_force_lsb, value)

    @property
    def reg_weight_pick_down_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_weight_pick_down_force_msb, self.__reg_weight_pick_down_force_lsb)
    @reg_weight_pick_down_force.setter
    def reg_weight_pick_down_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_weight_pick_down_force_msb, self.__reg_weight_pick_down_force_lsb, value)

    @property
    def reg_chan_interp_dep_sm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_interp_dep_sm_msb, self.__reg_chan_interp_dep_sm_lsb)
    @reg_chan_interp_dep_sm.setter
    def reg_chan_interp_dep_sm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_interp_dep_sm_msb, self.__reg_chan_interp_dep_sm_lsb, value)

    @property
    def reg_cfo_start_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cfo_start_2_msb, self.__reg_cfo_start_2_lsb)
    @reg_cfo_start_2.setter
    def reg_cfo_start_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cfo_start_2_msb, self.__reg_cfo_start_2_lsb, value)

    @property
    def reg_cfo_start_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cfo_start_1_msb, self.__reg_cfo_start_1_lsb)
    @reg_cfo_start_1.setter
    def reg_cfo_start_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cfo_start_1_msb, self.__reg_cfo_start_1_lsb, value)

    @property
    def reg_htltf_sgi_retim_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_htltf_sgi_retim_en_msb, self.__reg_htltf_sgi_retim_en_lsb)
    @reg_htltf_sgi_retim_en.setter
    def reg_htltf_sgi_retim_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_htltf_sgi_retim_en_msb, self.__reg_htltf_sgi_retim_en_lsb, value)

    @property
    def reg_chan_spur_interp_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_spur_interp_en_msb, self.__reg_chan_spur_interp_en_lsb)
    @reg_chan_spur_interp_en.setter
    def reg_chan_spur_interp_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_spur_interp_en_msb, self.__reg_chan_spur_interp_en_lsb, value)

    @property
    def reg_ht20_data_40m(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ht20_data_40m_msb, self.__reg_ht20_data_40m_lsb)
    @reg_ht20_data_40m.setter
    def reg_ht20_data_40m(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ht20_data_40m_msb, self.__reg_ht20_data_40m_lsb, value)

    @property
    def reg_ht40_pri_up(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ht40_pri_up_msb, self.__reg_ht40_pri_up_lsb)
    @reg_ht40_pri_up.setter
    def reg_ht40_pri_up(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ht40_pri_up_msb, self.__reg_ht40_pri_up_lsb, value)
class NRXSPURV0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x10
        self.__reg_spur_value0_lsb = 0
        self.__reg_spur_value0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_spur_value0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_spur_value0_msb, self.__reg_spur_value0_lsb)
    @reg_spur_value0.setter
    def reg_spur_value0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_spur_value0_msb, self.__reg_spur_value0_lsb, value)
class NRXSPURV1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x14
        self.__reg_spur_value1_lsb = 0
        self.__reg_spur_value1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_spur_value1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_spur_value1_msb, self.__reg_spur_value1_lsb)
    @reg_spur_value1.setter
    def reg_spur_value1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_spur_value1_msb, self.__reg_spur_value1_lsb, value)
class NRXSPURV2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x18
        self.__reg_spur_value2_lsb = 0
        self.__reg_spur_value2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_spur_value2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_spur_value2_msb, self.__reg_spur_value2_lsb)
    @reg_spur_value2.setter
    def reg_spur_value2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_spur_value2_msb, self.__reg_spur_value2_lsb, value)
class NRXSPURV3(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x1c
        self.__reg_spur_value3_lsb = 0
        self.__reg_spur_value3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_spur_value3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_spur_value3_msb, self.__reg_spur_value3_lsb)
    @reg_spur_value3.setter
    def reg_spur_value3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_spur_value3_msb, self.__reg_spur_value3_lsb, value)
class NRXSPURV4(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x20
        self.__reg_spur_value4_lsb = 0
        self.__reg_spur_value4_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_spur_value4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_spur_value4_msb, self.__reg_spur_value4_lsb)
    @reg_spur_value4.setter
    def reg_spur_value4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_spur_value4_msb, self.__reg_spur_value4_lsb, value)
class NRXSPURV5(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x24
        self.__reg_spur_value5_lsb = 0
        self.__reg_spur_value5_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_spur_value5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_spur_value5_msb, self.__reg_spur_value5_lsb)
    @reg_spur_value5.setter
    def reg_spur_value5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_spur_value5_msb, self.__reg_spur_value5_lsb, value)
class NRXSPURV6(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x28
        self.__reg_spur_value6_lsb = 0
        self.__reg_spur_value6_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_spur_value6(self):
        return self.__MEM.rdm(self.__addr, self.__reg_spur_value6_msb, self.__reg_spur_value6_lsb)
    @reg_spur_value6.setter
    def reg_spur_value6(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_spur_value6_msb, self.__reg_spur_value6_lsb, value)
class NRXSPURV7(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x2c
        self.__reg_spur_value7_lsb = 0
        self.__reg_spur_value7_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_spur_value7(self):
        return self.__MEM.rdm(self.__addr, self.__reg_spur_value7_msb, self.__reg_spur_value7_lsb)
    @reg_spur_value7.setter
    def reg_spur_value7(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_spur_value7_msb, self.__reg_spur_value7_lsb, value)
class NRXSPURFV1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x30
        self.__reg_spur_float_value1_lsb = 0
        self.__reg_spur_float_value1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_spur_float_value1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_spur_float_value1_msb, self.__reg_spur_float_value1_lsb)
    @reg_spur_float_value1.setter
    def reg_spur_float_value1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_spur_float_value1_msb, self.__reg_spur_float_value1_lsb, value)
class NRXSPURFV2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x34
        self.__reg_spur_float_value2_lsb = 0
        self.__reg_spur_float_value2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_spur_float_value2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_spur_float_value2_msb, self.__reg_spur_float_value2_lsb)
    @reg_spur_float_value2.setter
    def reg_spur_float_value2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_spur_float_value2_msb, self.__reg_spur_float_value2_lsb, value)
class NRXSPURC(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x38
        self.__reg_spur_value_en_lsb = 4
        self.__reg_spur_value_en_msb = 4
        self.__reg_spur_float_pst_lsb = 1
        self.__reg_spur_float_pst_msb = 3
        self.__reg_spur_float_en_lsb = 0
        self.__reg_spur_float_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_spur_value_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_spur_value_en_msb, self.__reg_spur_value_en_lsb)
    @reg_spur_value_en.setter
    def reg_spur_value_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_spur_value_en_msb, self.__reg_spur_value_en_lsb, value)

    @property
    def reg_spur_float_pst(self):
        return self.__MEM.rdm(self.__addr, self.__reg_spur_float_pst_msb, self.__reg_spur_float_pst_lsb)
    @reg_spur_float_pst.setter
    def reg_spur_float_pst(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_spur_float_pst_msb, self.__reg_spur_float_pst_lsb, value)

    @property
    def reg_spur_float_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_spur_float_en_msb, self.__reg_spur_float_en_lsb)
    @reg_spur_float_en.setter
    def reg_spur_float_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_spur_float_en_msb, self.__reg_spur_float_en_lsb, value)
class NRXFOE(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x3c
        self.__reg_cfo_cal_num_2_lsb = 23
        self.__reg_cfo_cal_num_2_msb = 31
        self.__reg_cfo_cal_num_1_lsb = 14
        self.__reg_cfo_cal_num_1_msb = 22
        self.__reg_foe_force_lsb = 1
        self.__reg_foe_force_msb = 13
        self.__reg_foe_force_en_lsb = 0
        self.__reg_foe_force_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_cfo_cal_num_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cfo_cal_num_2_msb, self.__reg_cfo_cal_num_2_lsb)
    @reg_cfo_cal_num_2.setter
    def reg_cfo_cal_num_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cfo_cal_num_2_msb, self.__reg_cfo_cal_num_2_lsb, value)

    @property
    def reg_cfo_cal_num_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cfo_cal_num_1_msb, self.__reg_cfo_cal_num_1_lsb)
    @reg_cfo_cal_num_1.setter
    def reg_cfo_cal_num_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cfo_cal_num_1_msb, self.__reg_cfo_cal_num_1_lsb, value)

    @property
    def reg_foe_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_foe_force_msb, self.__reg_foe_force_lsb)
    @reg_foe_force.setter
    def reg_foe_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_foe_force_msb, self.__reg_foe_force_lsb, value)

    @property
    def reg_foe_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_foe_force_en_msb, self.__reg_foe_force_en_lsb)
    @reg_foe_force_en.setter
    def reg_foe_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_foe_force_en_msb, self.__reg_foe_force_en_lsb, value)
class NRXVIT(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x40
        self.__reg_clk80_en_lsb = 1
        self.__reg_clk80_en_msb = 1
        self.__reg_clk_force_vit_lsb = 0
        self.__reg_clk_force_vit_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_clk80_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk80_en_msb, self.__reg_clk80_en_lsb)
    @reg_clk80_en.setter
    def reg_clk80_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk80_en_msb, self.__reg_clk80_en_lsb, value)

    @property
    def reg_clk_force_vit(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk_force_vit_msb, self.__reg_clk_force_vit_lsb)
    @reg_clk_force_vit.setter
    def reg_clk_force_vit(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk_force_vit_msb, self.__reg_clk_force_vit_lsb, value)
class NRXFREQPARA(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x48
        self.__fs_vs_f_para_shift_lsb = 24
        self.__fs_vs_f_para_shift_msb = 28
        self.__fs_vs_f_para_lsb = 0
        self.__fs_vs_f_para_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def fs_vs_f_para_shift(self):
        return self.__MEM.rdm(self.__addr, self.__fs_vs_f_para_shift_msb, self.__fs_vs_f_para_shift_lsb)
    @fs_vs_f_para_shift.setter
    def fs_vs_f_para_shift(self, value):
        return self.__MEM.wrm(self.__addr, self.__fs_vs_f_para_shift_msb, self.__fs_vs_f_para_shift_lsb, value)

    @property
    def fs_vs_f_para(self):
        return self.__MEM.rdm(self.__addr, self.__fs_vs_f_para_msb, self.__fs_vs_f_para_lsb)
    @fs_vs_f_para.setter
    def fs_vs_f_para(self, value):
        return self.__MEM.wrm(self.__addr, self.__fs_vs_f_para_msb, self.__fs_vs_f_para_lsb, value)
class NRXMODUSCALEAWGN0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x4c
        self.__reg_mcs3_scale_lsb = 24
        self.__reg_mcs3_scale_msb = 31
        self.__reg_mcs2_scale_lsb = 16
        self.__reg_mcs2_scale_msb = 23
        self.__reg_mcs1_scale_lsb = 8
        self.__reg_mcs1_scale_msb = 15
        self.__reg_mcs0_scale_lsb = 0
        self.__reg_mcs0_scale_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_mcs3_scale(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mcs3_scale_msb, self.__reg_mcs3_scale_lsb)
    @reg_mcs3_scale.setter
    def reg_mcs3_scale(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mcs3_scale_msb, self.__reg_mcs3_scale_lsb, value)

    @property
    def reg_mcs2_scale(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mcs2_scale_msb, self.__reg_mcs2_scale_lsb)
    @reg_mcs2_scale.setter
    def reg_mcs2_scale(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mcs2_scale_msb, self.__reg_mcs2_scale_lsb, value)

    @property
    def reg_mcs1_scale(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mcs1_scale_msb, self.__reg_mcs1_scale_lsb)
    @reg_mcs1_scale.setter
    def reg_mcs1_scale(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mcs1_scale_msb, self.__reg_mcs1_scale_lsb, value)

    @property
    def reg_mcs0_scale(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mcs0_scale_msb, self.__reg_mcs0_scale_lsb)
    @reg_mcs0_scale.setter
    def reg_mcs0_scale(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mcs0_scale_msb, self.__reg_mcs0_scale_lsb, value)
class NRXTEST0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x50
        self.__reg_com_pha_force_lsb = 1
        self.__reg_com_pha_force_msb = 21
        self.__reg_com_pha_force_en_lsb = 0
        self.__reg_com_pha_force_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_com_pha_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_com_pha_force_msb, self.__reg_com_pha_force_lsb)
    @reg_com_pha_force.setter
    def reg_com_pha_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_com_pha_force_msb, self.__reg_com_pha_force_lsb, value)

    @property
    def reg_com_pha_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_com_pha_force_en_msb, self.__reg_com_pha_force_en_lsb)
    @reg_com_pha_force_en.setter
    def reg_com_pha_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_com_pha_force_en_msb, self.__reg_com_pha_force_en_lsb, value)
class NRXTEST1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x54
        self.__reg_slope_force_lsb = 1
        self.__reg_slope_force_msb = 21
        self.__reg_slope_force_en_lsb = 0
        self.__reg_slope_force_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_slope_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_slope_force_msb, self.__reg_slope_force_lsb)
    @reg_slope_force.setter
    def reg_slope_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_slope_force_msb, self.__reg_slope_force_lsb, value)

    @property
    def reg_slope_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_slope_force_en_msb, self.__reg_slope_force_en_lsb)
    @reg_slope_force_en.setter
    def reg_slope_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_slope_force_en_msb, self.__reg_slope_force_en_lsb, value)
class NRXFDM1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x58
        self.__reg_vht_det_en_lsb = 19
        self.__reg_vht_det_en_msb = 19
        self.__reg_vht_notsupported_en_lsb = 18
        self.__reg_vht_notsupported_en_msb = 18
        self.__reg_dup_del_pwr_en_lsb = 17
        self.__reg_dup_del_pwr_en_msb = 17
        self.__reg_dup_del_pwr_thr_lsb = 12
        self.__reg_dup_del_pwr_thr_msb = 16
        self.__reg_fft_done_end_en_lsb = 11
        self.__reg_fft_done_end_en_msb = 11
        self.__fft_ltf_start_pos_pulse_lsb = 10
        self.__fft_ltf_start_pos_pulse_msb = 10
        self.__reg_fdm_wait_end_lsb = 0
        self.__reg_fdm_wait_end_msb = 9
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_vht_det_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_vht_det_en_msb, self.__reg_vht_det_en_lsb)
    @reg_vht_det_en.setter
    def reg_vht_det_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_vht_det_en_msb, self.__reg_vht_det_en_lsb, value)

    @property
    def reg_vht_notsupported_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_vht_notsupported_en_msb, self.__reg_vht_notsupported_en_lsb)
    @reg_vht_notsupported_en.setter
    def reg_vht_notsupported_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_vht_notsupported_en_msb, self.__reg_vht_notsupported_en_lsb, value)

    @property
    def reg_dup_del_pwr_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dup_del_pwr_en_msb, self.__reg_dup_del_pwr_en_lsb)
    @reg_dup_del_pwr_en.setter
    def reg_dup_del_pwr_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dup_del_pwr_en_msb, self.__reg_dup_del_pwr_en_lsb, value)

    @property
    def reg_dup_del_pwr_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dup_del_pwr_thr_msb, self.__reg_dup_del_pwr_thr_lsb)
    @reg_dup_del_pwr_thr.setter
    def reg_dup_del_pwr_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dup_del_pwr_thr_msb, self.__reg_dup_del_pwr_thr_lsb, value)

    @property
    def reg_fft_done_end_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fft_done_end_en_msb, self.__reg_fft_done_end_en_lsb)
    @reg_fft_done_end_en.setter
    def reg_fft_done_end_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fft_done_end_en_msb, self.__reg_fft_done_end_en_lsb, value)

    @property
    def fft_ltf_start_pos_pulse(self):
        return self.__MEM.rdm(self.__addr, self.__fft_ltf_start_pos_pulse_msb, self.__fft_ltf_start_pos_pulse_lsb)
    @fft_ltf_start_pos_pulse.setter
    def fft_ltf_start_pos_pulse(self, value):
        return self.__MEM.wrm(self.__addr, self.__fft_ltf_start_pos_pulse_msb, self.__fft_ltf_start_pos_pulse_lsb, value)

    @property
    def reg_fdm_wait_end(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fdm_wait_end_msb, self.__reg_fdm_wait_end_lsb)
    @reg_fdm_wait_end.setter
    def reg_fdm_wait_end(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fdm_wait_end_msb, self.__reg_fdm_wait_end_lsb, value)
class NRXDEBUG(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x5c
        self.__fdm_wait_for_end_lsb = 31
        self.__fdm_wait_for_end_msb = 31
        self.__rf_freq_offset_phi_valid_lsb = 30
        self.__rf_freq_offset_phi_valid_msb = 30
        self.__rf_freq_offset_phi_lsb = 15
        self.__rf_freq_offset_phi_msb = 29
        self.__fte_offset_lsb = 8
        self.__fte_offset_msb = 14
        self.__fte_offset_valid_lsb = 7
        self.__fte_offset_valid_msb = 7
        self.__equal_start_lsb = 6
        self.__equal_start_msb = 6
        self.__test_p1_lsb = 5
        self.__test_p1_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def fdm_wait_for_end(self):
        return self.__MEM.rdm(self.__addr, self.__fdm_wait_for_end_msb, self.__fdm_wait_for_end_lsb)
    @fdm_wait_for_end.setter
    def fdm_wait_for_end(self, value):
        return self.__MEM.wrm(self.__addr, self.__fdm_wait_for_end_msb, self.__fdm_wait_for_end_lsb, value)

    @property
    def rf_freq_offset_phi_valid(self):
        return self.__MEM.rdm(self.__addr, self.__rf_freq_offset_phi_valid_msb, self.__rf_freq_offset_phi_valid_lsb)
    @rf_freq_offset_phi_valid.setter
    def rf_freq_offset_phi_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__rf_freq_offset_phi_valid_msb, self.__rf_freq_offset_phi_valid_lsb, value)

    @property
    def rf_freq_offset_phi(self):
        return self.__MEM.rdm(self.__addr, self.__rf_freq_offset_phi_msb, self.__rf_freq_offset_phi_lsb)
    @rf_freq_offset_phi.setter
    def rf_freq_offset_phi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rf_freq_offset_phi_msb, self.__rf_freq_offset_phi_lsb, value)

    @property
    def fte_offset(self):
        return self.__MEM.rdm(self.__addr, self.__fte_offset_msb, self.__fte_offset_lsb)
    @fte_offset.setter
    def fte_offset(self, value):
        return self.__MEM.wrm(self.__addr, self.__fte_offset_msb, self.__fte_offset_lsb, value)

    @property
    def fte_offset_valid(self):
        return self.__MEM.rdm(self.__addr, self.__fte_offset_valid_msb, self.__fte_offset_valid_lsb)
    @fte_offset_valid.setter
    def fte_offset_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__fte_offset_valid_msb, self.__fte_offset_valid_lsb, value)

    @property
    def equal_start(self):
        return self.__MEM.rdm(self.__addr, self.__equal_start_msb, self.__equal_start_lsb)
    @equal_start.setter
    def equal_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__equal_start_msb, self.__equal_start_lsb, value)

    @property
    def test_p1(self):
        return self.__MEM.rdm(self.__addr, self.__test_p1_msb, self.__test_p1_lsb)
    @test_p1.setter
    def test_p1(self, value):
        return self.__MEM.wrm(self.__addr, self.__test_p1_msb, self.__test_p1_lsb, value)
class NRXCTE_CTRL0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x78
        self.__reg_xcorr_gi_win_h_lsb = 27
        self.__reg_xcorr_gi_win_h_msb = 31
        self.__reg_xcorr_gi_win_l_lsb = 22
        self.__reg_xcorr_gi_win_l_msb = 26
        self.__reg_xcorr_win_h_lsb = 17
        self.__reg_xcorr_win_h_msb = 21
        self.__reg_xcorr_win_l_lsb = 12
        self.__reg_xcorr_win_l_msb = 16
        self.__reg_xcorr_cte_to_lsb = 6
        self.__reg_xcorr_cte_to_msb = 11
        self.__reg_cte_pk_offset_lsb = 0
        self.__reg_cte_pk_offset_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_xcorr_gi_win_h(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_gi_win_h_msb, self.__reg_xcorr_gi_win_h_lsb)
    @reg_xcorr_gi_win_h.setter
    def reg_xcorr_gi_win_h(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_gi_win_h_msb, self.__reg_xcorr_gi_win_h_lsb, value)

    @property
    def reg_xcorr_gi_win_l(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_gi_win_l_msb, self.__reg_xcorr_gi_win_l_lsb)
    @reg_xcorr_gi_win_l.setter
    def reg_xcorr_gi_win_l(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_gi_win_l_msb, self.__reg_xcorr_gi_win_l_lsb, value)

    @property
    def reg_xcorr_win_h(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_win_h_msb, self.__reg_xcorr_win_h_lsb)
    @reg_xcorr_win_h.setter
    def reg_xcorr_win_h(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_win_h_msb, self.__reg_xcorr_win_h_lsb, value)

    @property
    def reg_xcorr_win_l(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_win_l_msb, self.__reg_xcorr_win_l_lsb)
    @reg_xcorr_win_l.setter
    def reg_xcorr_win_l(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_win_l_msb, self.__reg_xcorr_win_l_lsb, value)

    @property
    def reg_xcorr_cte_to(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_cte_to_msb, self.__reg_xcorr_cte_to_lsb)
    @reg_xcorr_cte_to.setter
    def reg_xcorr_cte_to(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_cte_to_msb, self.__reg_xcorr_cte_to_lsb, value)

    @property
    def reg_cte_pk_offset(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cte_pk_offset_msb, self.__reg_cte_pk_offset_lsb)
    @reg_cte_pk_offset.setter
    def reg_cte_pk_offset(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cte_pk_offset_msb, self.__reg_cte_pk_offset_lsb, value)
class NRXCTE_CTRL1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x7c
        self.__reg_cfo_use_cte_pre08_lsb = 31
        self.__reg_cfo_use_cte_pre08_msb = 31
        self.__reg_sc_det_thr_lsb = 27
        self.__reg_sc_det_thr_msb = 30
        self.__reg_sc_rise_to_lsb = 18
        self.__reg_sc_rise_to_msb = 26
        self.__reg_sc_fall_to_lsb = 9
        self.__reg_sc_fall_to_msb = 17
        self.__reg_sc_det_timer_lsb = 0
        self.__reg_sc_det_timer_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_cfo_use_cte_pre08(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cfo_use_cte_pre08_msb, self.__reg_cfo_use_cte_pre08_lsb)
    @reg_cfo_use_cte_pre08.setter
    def reg_cfo_use_cte_pre08(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cfo_use_cte_pre08_msb, self.__reg_cfo_use_cte_pre08_lsb, value)

    @property
    def reg_sc_det_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sc_det_thr_msb, self.__reg_sc_det_thr_lsb)
    @reg_sc_det_thr.setter
    def reg_sc_det_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sc_det_thr_msb, self.__reg_sc_det_thr_lsb, value)

    @property
    def reg_sc_rise_to(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sc_rise_to_msb, self.__reg_sc_rise_to_lsb)
    @reg_sc_rise_to.setter
    def reg_sc_rise_to(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sc_rise_to_msb, self.__reg_sc_rise_to_lsb, value)

    @property
    def reg_sc_fall_to(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sc_fall_to_msb, self.__reg_sc_fall_to_lsb)
    @reg_sc_fall_to.setter
    def reg_sc_fall_to(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sc_fall_to_msb, self.__reg_sc_fall_to_lsb, value)

    @property
    def reg_sc_det_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sc_det_timer_msb, self.__reg_sc_det_timer_lsb)
    @reg_sc_det_timer.setter
    def reg_sc_det_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sc_det_timer_msb, self.__reg_sc_det_timer_lsb, value)
class NRXCTE_CTRL2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x80
        self.__reg_cte_mode_lsb = 30
        self.__reg_cte_mode_msb = 31
        self.__reg_cte_gi2_wait_1_lsb = 24
        self.__reg_cte_gi2_wait_1_msb = 29
        self.__reg_xcorr_pk_shr_1_lsb = 20
        self.__reg_xcorr_pk_shr_1_msb = 23
        self.__reg_xcorr_pk_mult_1_lsb = 14
        self.__reg_xcorr_pk_mult_1_msb = 19
        self.__reg_sc_end_thr_1_lsb = 7
        self.__reg_sc_end_thr_1_msb = 13
        self.__reg_sc_coef_1_lsb = 0
        self.__reg_sc_coef_1_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_cte_mode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cte_mode_msb, self.__reg_cte_mode_lsb)
    @reg_cte_mode.setter
    def reg_cte_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cte_mode_msb, self.__reg_cte_mode_lsb, value)

    @property
    def reg_cte_gi2_wait_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cte_gi2_wait_1_msb, self.__reg_cte_gi2_wait_1_lsb)
    @reg_cte_gi2_wait_1.setter
    def reg_cte_gi2_wait_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cte_gi2_wait_1_msb, self.__reg_cte_gi2_wait_1_lsb, value)

    @property
    def reg_xcorr_pk_shr_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_pk_shr_1_msb, self.__reg_xcorr_pk_shr_1_lsb)
    @reg_xcorr_pk_shr_1.setter
    def reg_xcorr_pk_shr_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_pk_shr_1_msb, self.__reg_xcorr_pk_shr_1_lsb, value)

    @property
    def reg_xcorr_pk_mult_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_pk_mult_1_msb, self.__reg_xcorr_pk_mult_1_lsb)
    @reg_xcorr_pk_mult_1.setter
    def reg_xcorr_pk_mult_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_pk_mult_1_msb, self.__reg_xcorr_pk_mult_1_lsb, value)

    @property
    def reg_sc_end_thr_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sc_end_thr_1_msb, self.__reg_sc_end_thr_1_lsb)
    @reg_sc_end_thr_1.setter
    def reg_sc_end_thr_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sc_end_thr_1_msb, self.__reg_sc_end_thr_1_lsb, value)

    @property
    def reg_sc_coef_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sc_coef_1_msb, self.__reg_sc_coef_1_lsb)
    @reg_sc_coef_1.setter
    def reg_sc_coef_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sc_coef_1_msb, self.__reg_sc_coef_1_lsb, value)
class NRXCTE_CTRL3(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x84
        self.__reg_cte_gi2_wait_2_lsb = 24
        self.__reg_cte_gi2_wait_2_msb = 29
        self.__reg_xcorr_pk_shr_2_lsb = 20
        self.__reg_xcorr_pk_shr_2_msb = 23
        self.__reg_xcorr_pk_mult_2_lsb = 14
        self.__reg_xcorr_pk_mult_2_msb = 19
        self.__reg_sc_end_thr_2_lsb = 7
        self.__reg_sc_end_thr_2_msb = 13
        self.__reg_sc_coef_2_lsb = 0
        self.__reg_sc_coef_2_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_cte_gi2_wait_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cte_gi2_wait_2_msb, self.__reg_cte_gi2_wait_2_lsb)
    @reg_cte_gi2_wait_2.setter
    def reg_cte_gi2_wait_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cte_gi2_wait_2_msb, self.__reg_cte_gi2_wait_2_lsb, value)

    @property
    def reg_xcorr_pk_shr_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_pk_shr_2_msb, self.__reg_xcorr_pk_shr_2_lsb)
    @reg_xcorr_pk_shr_2.setter
    def reg_xcorr_pk_shr_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_pk_shr_2_msb, self.__reg_xcorr_pk_shr_2_lsb, value)

    @property
    def reg_xcorr_pk_mult_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_pk_mult_2_msb, self.__reg_xcorr_pk_mult_2_lsb)
    @reg_xcorr_pk_mult_2.setter
    def reg_xcorr_pk_mult_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_pk_mult_2_msb, self.__reg_xcorr_pk_mult_2_lsb, value)

    @property
    def reg_sc_end_thr_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sc_end_thr_2_msb, self.__reg_sc_end_thr_2_lsb)
    @reg_sc_end_thr_2.setter
    def reg_sc_end_thr_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sc_end_thr_2_msb, self.__reg_sc_end_thr_2_lsb, value)

    @property
    def reg_sc_coef_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sc_coef_2_msb, self.__reg_sc_coef_2_lsb)
    @reg_sc_coef_2.setter
    def reg_sc_coef_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sc_coef_2_msb, self.__reg_sc_coef_2_lsb, value)
class NRXFREQREG(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x88
        self.__reg_timing_jump_en_lsb = 21
        self.__reg_timing_jump_en_msb = 21
        self.__jump_num_lsb = 15
        self.__jump_num_msb = 20
        self.__delta_phase_reg_lsb = 0
        self.__delta_phase_reg_msb = 14
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_timing_jump_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_timing_jump_en_msb, self.__reg_timing_jump_en_lsb)
    @reg_timing_jump_en.setter
    def reg_timing_jump_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_timing_jump_en_msb, self.__reg_timing_jump_en_lsb, value)

    @property
    def jump_num(self):
        return self.__MEM.rdm(self.__addr, self.__jump_num_msb, self.__jump_num_lsb)
    @jump_num.setter
    def jump_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__jump_num_msb, self.__jump_num_lsb, value)

    @property
    def delta_phase_reg(self):
        return self.__MEM.rdm(self.__addr, self.__delta_phase_reg_msb, self.__delta_phase_reg_lsb)
    @delta_phase_reg.setter
    def delta_phase_reg(self, value):
        return self.__MEM.wrm(self.__addr, self.__delta_phase_reg_msb, self.__delta_phase_reg_lsb, value)
class BB_NRX_TEST(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x8c
        self.__reg_nrxclk_en_lsb = 0
        self.__reg_nrxclk_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_nrxclk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_nrxclk_en_msb, self.__reg_nrxclk_en_lsb)
    @reg_nrxclk_en.setter
    def reg_nrxclk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_nrxclk_en_msb, self.__reg_nrxclk_en_lsb, value)
class NRXPILOTCONF0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x90
        self.__reg_k_shift6_lsb = 20
        self.__reg_k_shift6_msb = 22
        self.__reg_k_shift5_lsb = 16
        self.__reg_k_shift5_msb = 18
        self.__reg_k_shift4_lsb = 12
        self.__reg_k_shift4_msb = 14
        self.__reg_k_shift3_lsb = 8
        self.__reg_k_shift3_msb = 10
        self.__reg_k_shift2_lsb = 4
        self.__reg_k_shift2_msb = 6
        self.__reg_k_shift1_lsb = 0
        self.__reg_k_shift1_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_k_shift6(self):
        return self.__MEM.rdm(self.__addr, self.__reg_k_shift6_msb, self.__reg_k_shift6_lsb)
    @reg_k_shift6.setter
    def reg_k_shift6(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_k_shift6_msb, self.__reg_k_shift6_lsb, value)

    @property
    def reg_k_shift5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_k_shift5_msb, self.__reg_k_shift5_lsb)
    @reg_k_shift5.setter
    def reg_k_shift5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_k_shift5_msb, self.__reg_k_shift5_lsb, value)

    @property
    def reg_k_shift4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_k_shift4_msb, self.__reg_k_shift4_lsb)
    @reg_k_shift4.setter
    def reg_k_shift4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_k_shift4_msb, self.__reg_k_shift4_lsb, value)

    @property
    def reg_k_shift3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_k_shift3_msb, self.__reg_k_shift3_lsb)
    @reg_k_shift3.setter
    def reg_k_shift3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_k_shift3_msb, self.__reg_k_shift3_lsb, value)

    @property
    def reg_k_shift2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_k_shift2_msb, self.__reg_k_shift2_lsb)
    @reg_k_shift2.setter
    def reg_k_shift2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_k_shift2_msb, self.__reg_k_shift2_lsb, value)

    @property
    def reg_k_shift1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_k_shift1_msb, self.__reg_k_shift1_lsb)
    @reg_k_shift1.setter
    def reg_k_shift1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_k_shift1_msb, self.__reg_k_shift1_lsb, value)
class NRXPILOTCONF1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x94
        self.__reg_a_shift6_lsb = 20
        self.__reg_a_shift6_msb = 22
        self.__reg_a_shift5_lsb = 16
        self.__reg_a_shift5_msb = 18
        self.__reg_a_shift4_lsb = 12
        self.__reg_a_shift4_msb = 14
        self.__reg_a_shift3_lsb = 8
        self.__reg_a_shift3_msb = 10
        self.__reg_a_shift2_lsb = 4
        self.__reg_a_shift2_msb = 6
        self.__reg_a_shift1_lsb = 0
        self.__reg_a_shift1_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_a_shift6(self):
        return self.__MEM.rdm(self.__addr, self.__reg_a_shift6_msb, self.__reg_a_shift6_lsb)
    @reg_a_shift6.setter
    def reg_a_shift6(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_a_shift6_msb, self.__reg_a_shift6_lsb, value)

    @property
    def reg_a_shift5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_a_shift5_msb, self.__reg_a_shift5_lsb)
    @reg_a_shift5.setter
    def reg_a_shift5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_a_shift5_msb, self.__reg_a_shift5_lsb, value)

    @property
    def reg_a_shift4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_a_shift4_msb, self.__reg_a_shift4_lsb)
    @reg_a_shift4.setter
    def reg_a_shift4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_a_shift4_msb, self.__reg_a_shift4_lsb, value)

    @property
    def reg_a_shift3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_a_shift3_msb, self.__reg_a_shift3_lsb)
    @reg_a_shift3.setter
    def reg_a_shift3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_a_shift3_msb, self.__reg_a_shift3_lsb, value)

    @property
    def reg_a_shift2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_a_shift2_msb, self.__reg_a_shift2_lsb)
    @reg_a_shift2.setter
    def reg_a_shift2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_a_shift2_msb, self.__reg_a_shift2_lsb, value)

    @property
    def reg_a_shift1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_a_shift1_msb, self.__reg_a_shift1_lsb)
    @reg_a_shift1.setter
    def reg_a_shift1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_a_shift1_msb, self.__reg_a_shift1_lsb, value)
class NRXPILOTCONF2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x98
        self.__reg_phi_fine_fix_en_lsb = 27
        self.__reg_phi_fine_fix_en_msb = 27
        self.__reg_phi_fine_fix_lsb = 12
        self.__reg_phi_fine_fix_msb = 26
        self.__reg_slope_fix_lsb = 0
        self.__reg_slope_fix_msb = 9
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_phi_fine_fix_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_phi_fine_fix_en_msb, self.__reg_phi_fine_fix_en_lsb)
    @reg_phi_fine_fix_en.setter
    def reg_phi_fine_fix_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_phi_fine_fix_en_msb, self.__reg_phi_fine_fix_en_lsb, value)

    @property
    def reg_phi_fine_fix(self):
        return self.__MEM.rdm(self.__addr, self.__reg_phi_fine_fix_msb, self.__reg_phi_fine_fix_lsb)
    @reg_phi_fine_fix.setter
    def reg_phi_fine_fix(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_phi_fine_fix_msb, self.__reg_phi_fine_fix_lsb, value)

    @property
    def reg_slope_fix(self):
        return self.__MEM.rdm(self.__addr, self.__reg_slope_fix_msb, self.__reg_slope_fix_lsb)
    @reg_slope_fix.setter
    def reg_slope_fix(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_slope_fix_msb, self.__reg_slope_fix_lsb, value)
class NRXPILOTCONF3(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x9c
        self.__reg_f_shift6_lsb = 20
        self.__reg_f_shift6_msb = 22
        self.__reg_f_shift5_lsb = 16
        self.__reg_f_shift5_msb = 18
        self.__reg_f_shift4_lsb = 12
        self.__reg_f_shift4_msb = 14
        self.__reg_f_shift3_lsb = 8
        self.__reg_f_shift3_msb = 10
        self.__reg_f_shift2_lsb = 4
        self.__reg_f_shift2_msb = 6
        self.__reg_f_shift1_lsb = 0
        self.__reg_f_shift1_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_f_shift6(self):
        return self.__MEM.rdm(self.__addr, self.__reg_f_shift6_msb, self.__reg_f_shift6_lsb)
    @reg_f_shift6.setter
    def reg_f_shift6(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_f_shift6_msb, self.__reg_f_shift6_lsb, value)

    @property
    def reg_f_shift5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_f_shift5_msb, self.__reg_f_shift5_lsb)
    @reg_f_shift5.setter
    def reg_f_shift5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_f_shift5_msb, self.__reg_f_shift5_lsb, value)

    @property
    def reg_f_shift4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_f_shift4_msb, self.__reg_f_shift4_lsb)
    @reg_f_shift4.setter
    def reg_f_shift4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_f_shift4_msb, self.__reg_f_shift4_lsb, value)

    @property
    def reg_f_shift3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_f_shift3_msb, self.__reg_f_shift3_lsb)
    @reg_f_shift3.setter
    def reg_f_shift3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_f_shift3_msb, self.__reg_f_shift3_lsb, value)

    @property
    def reg_f_shift2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_f_shift2_msb, self.__reg_f_shift2_lsb)
    @reg_f_shift2.setter
    def reg_f_shift2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_f_shift2_msb, self.__reg_f_shift2_lsb, value)

    @property
    def reg_f_shift1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_f_shift1_msb, self.__reg_f_shift1_lsb)
    @reg_f_shift1.setter
    def reg_f_shift1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_f_shift1_msb, self.__reg_f_shift1_lsb, value)
class NRXCHAN_RATE_THR1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0xa0
        self.__reg_chan_rate_thr_mcs4_lsb = 24
        self.__reg_chan_rate_thr_mcs4_msb = 31
        self.__reg_chan_rate_thr_mcs5_lsb = 16
        self.__reg_chan_rate_thr_mcs5_msb = 23
        self.__reg_chan_rate_thr_mcs6_lsb = 8
        self.__reg_chan_rate_thr_mcs6_msb = 15
        self.__reg_chan_rate_thr_mcs7_lsb = 0
        self.__reg_chan_rate_thr_mcs7_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_chan_rate_thr_mcs4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_rate_thr_mcs4_msb, self.__reg_chan_rate_thr_mcs4_lsb)
    @reg_chan_rate_thr_mcs4.setter
    def reg_chan_rate_thr_mcs4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_rate_thr_mcs4_msb, self.__reg_chan_rate_thr_mcs4_lsb, value)

    @property
    def reg_chan_rate_thr_mcs5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_rate_thr_mcs5_msb, self.__reg_chan_rate_thr_mcs5_lsb)
    @reg_chan_rate_thr_mcs5.setter
    def reg_chan_rate_thr_mcs5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_rate_thr_mcs5_msb, self.__reg_chan_rate_thr_mcs5_lsb, value)

    @property
    def reg_chan_rate_thr_mcs6(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_rate_thr_mcs6_msb, self.__reg_chan_rate_thr_mcs6_lsb)
    @reg_chan_rate_thr_mcs6.setter
    def reg_chan_rate_thr_mcs6(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_rate_thr_mcs6_msb, self.__reg_chan_rate_thr_mcs6_lsb, value)

    @property
    def reg_chan_rate_thr_mcs7(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_rate_thr_mcs7_msb, self.__reg_chan_rate_thr_mcs7_lsb)
    @reg_chan_rate_thr_mcs7.setter
    def reg_chan_rate_thr_mcs7(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_rate_thr_mcs7_msb, self.__reg_chan_rate_thr_mcs7_lsb, value)
class NRXCHAN_RATE_THR2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0xa4
        self.__reg_fte_data_rate_en_lsb = 24
        self.__reg_fte_data_rate_en_msb = 24
        self.__reg_chan_rate_thr_mcs1_lsb = 16
        self.__reg_chan_rate_thr_mcs1_msb = 23
        self.__reg_chan_rate_thr_mcs2_lsb = 8
        self.__reg_chan_rate_thr_mcs2_msb = 15
        self.__reg_chan_rate_thr_mcs3_lsb = 0
        self.__reg_chan_rate_thr_mcs3_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_fte_data_rate_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fte_data_rate_en_msb, self.__reg_fte_data_rate_en_lsb)
    @reg_fte_data_rate_en.setter
    def reg_fte_data_rate_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fte_data_rate_en_msb, self.__reg_fte_data_rate_en_lsb, value)

    @property
    def reg_chan_rate_thr_mcs1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_rate_thr_mcs1_msb, self.__reg_chan_rate_thr_mcs1_lsb)
    @reg_chan_rate_thr_mcs1.setter
    def reg_chan_rate_thr_mcs1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_rate_thr_mcs1_msb, self.__reg_chan_rate_thr_mcs1_lsb, value)

    @property
    def reg_chan_rate_thr_mcs2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_rate_thr_mcs2_msb, self.__reg_chan_rate_thr_mcs2_lsb)
    @reg_chan_rate_thr_mcs2.setter
    def reg_chan_rate_thr_mcs2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_rate_thr_mcs2_msb, self.__reg_chan_rate_thr_mcs2_lsb, value)

    @property
    def reg_chan_rate_thr_mcs3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_rate_thr_mcs3_msb, self.__reg_chan_rate_thr_mcs3_lsb)
    @reg_chan_rate_thr_mcs3.setter
    def reg_chan_rate_thr_mcs3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_rate_thr_mcs3_msb, self.__reg_chan_rate_thr_mcs3_lsb, value)
class NRXLSIGEVM0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0xa8
        self.__reg_sum_imag_evm_lsb = 16
        self.__reg_sum_imag_evm_msb = 31
        self.__reg_sum_real_evm_lsb = 0
        self.__reg_sum_real_evm_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sum_imag_evm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sum_imag_evm_msb, self.__reg_sum_imag_evm_lsb)
    @reg_sum_imag_evm.setter
    def reg_sum_imag_evm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sum_imag_evm_msb, self.__reg_sum_imag_evm_lsb, value)

    @property
    def reg_sum_real_evm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sum_real_evm_msb, self.__reg_sum_real_evm_lsb)
    @reg_sum_real_evm.setter
    def reg_sum_real_evm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sum_real_evm_msb, self.__reg_sum_real_evm_lsb, value)
class NRXLSIGEVM1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0xac
        self.__reg_evm_est_shift_en_lsb = 16
        self.__reg_evm_est_shift_en_msb = 16
        self.__reg_evm_est_shift_lsb = 12
        self.__reg_evm_est_shift_msb = 15
        self.__reg_imag_evm_est_lsb = 6
        self.__reg_imag_evm_est_msb = 11
        self.__reg_real_evm_est_lsb = 0
        self.__reg_real_evm_est_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_evm_est_shift_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_evm_est_shift_en_msb, self.__reg_evm_est_shift_en_lsb)
    @reg_evm_est_shift_en.setter
    def reg_evm_est_shift_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_evm_est_shift_en_msb, self.__reg_evm_est_shift_en_lsb, value)

    @property
    def reg_evm_est_shift(self):
        return self.__MEM.rdm(self.__addr, self.__reg_evm_est_shift_msb, self.__reg_evm_est_shift_lsb)
    @reg_evm_est_shift.setter
    def reg_evm_est_shift(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_evm_est_shift_msb, self.__reg_evm_est_shift_lsb, value)

    @property
    def reg_imag_evm_est(self):
        return self.__MEM.rdm(self.__addr, self.__reg_imag_evm_est_msb, self.__reg_imag_evm_est_lsb)
    @reg_imag_evm_est.setter
    def reg_imag_evm_est(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_imag_evm_est_msb, self.__reg_imag_evm_est_lsb, value)

    @property
    def reg_real_evm_est(self):
        return self.__MEM.rdm(self.__addr, self.__reg_real_evm_est_msb, self.__reg_real_evm_est_lsb)
    @reg_real_evm_est.setter
    def reg_real_evm_est(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_real_evm_est_msb, self.__reg_real_evm_est_lsb, value)
class NRXSPURV8(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0xb0
        self.__reg_spur_value8_lsb = 0
        self.__reg_spur_value8_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_spur_value8(self):
        return self.__MEM.rdm(self.__addr, self.__reg_spur_value8_msb, self.__reg_spur_value8_lsb)
    @reg_spur_value8.setter
    def reg_spur_value8(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_spur_value8_msb, self.__reg_spur_value8_lsb, value)
class NRXPILOTCONF4(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0xb4
        self.__reg_sig_chan_est_en_lsb = 15
        self.__reg_sig_chan_est_en_msb = 15
        self.__reg_htltf_comp_dep_sm_lsb = 14
        self.__reg_htltf_comp_dep_sm_msb = 14
        self.__reg_htltf_comp_en_lsb = 13
        self.__reg_htltf_comp_en_msb = 13
        self.__reg_htltf_comp_sel_lsb = 12
        self.__reg_htltf_comp_sel_msb = 12
        self.__ph_err_reg_rshift_lsb = 8
        self.__ph_err_reg_rshift_msb = 11
        self.__delta_phase_reg_shift_lsb = 4
        self.__delta_phase_reg_shift_msb = 7
        self.__common_phase_f_shift_reg_shift_lsb = 0
        self.__common_phase_f_shift_reg_shift_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sig_chan_est_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sig_chan_est_en_msb, self.__reg_sig_chan_est_en_lsb)
    @reg_sig_chan_est_en.setter
    def reg_sig_chan_est_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sig_chan_est_en_msb, self.__reg_sig_chan_est_en_lsb, value)

    @property
    def reg_htltf_comp_dep_sm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_htltf_comp_dep_sm_msb, self.__reg_htltf_comp_dep_sm_lsb)
    @reg_htltf_comp_dep_sm.setter
    def reg_htltf_comp_dep_sm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_htltf_comp_dep_sm_msb, self.__reg_htltf_comp_dep_sm_lsb, value)

    @property
    def reg_htltf_comp_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_htltf_comp_en_msb, self.__reg_htltf_comp_en_lsb)
    @reg_htltf_comp_en.setter
    def reg_htltf_comp_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_htltf_comp_en_msb, self.__reg_htltf_comp_en_lsb, value)

    @property
    def reg_htltf_comp_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_htltf_comp_sel_msb, self.__reg_htltf_comp_sel_lsb)
    @reg_htltf_comp_sel.setter
    def reg_htltf_comp_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_htltf_comp_sel_msb, self.__reg_htltf_comp_sel_lsb, value)

    @property
    def ph_err_reg_rshift(self):
        return self.__MEM.rdm(self.__addr, self.__ph_err_reg_rshift_msb, self.__ph_err_reg_rshift_lsb)
    @ph_err_reg_rshift.setter
    def ph_err_reg_rshift(self, value):
        return self.__MEM.wrm(self.__addr, self.__ph_err_reg_rshift_msb, self.__ph_err_reg_rshift_lsb, value)

    @property
    def delta_phase_reg_shift(self):
        return self.__MEM.rdm(self.__addr, self.__delta_phase_reg_shift_msb, self.__delta_phase_reg_shift_lsb)
    @delta_phase_reg_shift.setter
    def delta_phase_reg_shift(self, value):
        return self.__MEM.wrm(self.__addr, self.__delta_phase_reg_shift_msb, self.__delta_phase_reg_shift_lsb, value)

    @property
    def common_phase_f_shift_reg_shift(self):
        return self.__MEM.rdm(self.__addr, self.__common_phase_f_shift_reg_shift_msb, self.__common_phase_f_shift_reg_shift_lsb)
    @common_phase_f_shift_reg_shift.setter
    def common_phase_f_shift_reg_shift(self, value):
        return self.__MEM.wrm(self.__addr, self.__common_phase_f_shift_reg_shift_msb, self.__common_phase_f_shift_reg_shift_lsb, value)
class NRXPILOTCONF5(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0xb8
        self.__reg_mac_dug_inf_mod_lsb = 29
        self.__reg_mac_dug_inf_mod_msb = 31
        self.__common_ph_err_abs_reg_lsb = 8
        self.__common_ph_err_abs_reg_msb = 28
        self.__common_ph_err_abs_reg_kb_lsb = 0
        self.__common_ph_err_abs_reg_kb_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_mac_dug_inf_mod(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mac_dug_inf_mod_msb, self.__reg_mac_dug_inf_mod_lsb)
    @reg_mac_dug_inf_mod.setter
    def reg_mac_dug_inf_mod(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mac_dug_inf_mod_msb, self.__reg_mac_dug_inf_mod_lsb, value)

    @property
    def common_ph_err_abs_reg(self):
        return self.__MEM.rdm(self.__addr, self.__common_ph_err_abs_reg_msb, self.__common_ph_err_abs_reg_lsb)
    @common_ph_err_abs_reg.setter
    def common_ph_err_abs_reg(self, value):
        return self.__MEM.wrm(self.__addr, self.__common_ph_err_abs_reg_msb, self.__common_ph_err_abs_reg_lsb, value)

    @property
    def common_ph_err_abs_reg_kb(self):
        return self.__MEM.rdm(self.__addr, self.__common_ph_err_abs_reg_kb_msb, self.__common_ph_err_abs_reg_kb_lsb)
    @common_ph_err_abs_reg_kb.setter
    def common_ph_err_abs_reg_kb(self, value):
        return self.__MEM.wrm(self.__addr, self.__common_ph_err_abs_reg_kb_msb, self.__common_ph_err_abs_reg_kb_lsb, value)
class NRXPILOTCONF6(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0xbc
        self.__common_phase_f_shift_reg_lsb = 0
        self.__common_phase_f_shift_reg_msb = 26
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def common_phase_f_shift_reg(self):
        return self.__MEM.rdm(self.__addr, self.__common_phase_f_shift_reg_msb, self.__common_phase_f_shift_reg_lsb)
    @common_phase_f_shift_reg.setter
    def common_phase_f_shift_reg(self, value):
        return self.__MEM.wrm(self.__addr, self.__common_phase_f_shift_reg_msb, self.__common_phase_f_shift_reg_lsb, value)
class NRXPILOTCONF7(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0xc0
        self.__reg_data_pilot_tk_en_lsb = 21
        self.__reg_data_pilot_tk_en_msb = 21
        self.__reg_pilot_pwr_track_en_lsb = 20
        self.__reg_pilot_pwr_track_en_msb = 20
        self.__reg_pilot_pwr_init_avg_num_lsb = 16
        self.__reg_pilot_pwr_init_avg_num_msb = 19
        self.__reg_foe_pilot_tk_cmp_en_lsb = 15
        self.__reg_foe_pilot_tk_cmp_en_msb = 15
        self.__freq_offset_tot_reg_lsb = 0
        self.__freq_offset_tot_reg_msb = 14
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_data_pilot_tk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_data_pilot_tk_en_msb, self.__reg_data_pilot_tk_en_lsb)
    @reg_data_pilot_tk_en.setter
    def reg_data_pilot_tk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_data_pilot_tk_en_msb, self.__reg_data_pilot_tk_en_lsb, value)

    @property
    def reg_pilot_pwr_track_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pilot_pwr_track_en_msb, self.__reg_pilot_pwr_track_en_lsb)
    @reg_pilot_pwr_track_en.setter
    def reg_pilot_pwr_track_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pilot_pwr_track_en_msb, self.__reg_pilot_pwr_track_en_lsb, value)

    @property
    def reg_pilot_pwr_init_avg_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pilot_pwr_init_avg_num_msb, self.__reg_pilot_pwr_init_avg_num_lsb)
    @reg_pilot_pwr_init_avg_num.setter
    def reg_pilot_pwr_init_avg_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pilot_pwr_init_avg_num_msb, self.__reg_pilot_pwr_init_avg_num_lsb, value)

    @property
    def reg_foe_pilot_tk_cmp_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_foe_pilot_tk_cmp_en_msb, self.__reg_foe_pilot_tk_cmp_en_lsb)
    @reg_foe_pilot_tk_cmp_en.setter
    def reg_foe_pilot_tk_cmp_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_foe_pilot_tk_cmp_en_msb, self.__reg_foe_pilot_tk_cmp_en_lsb, value)

    @property
    def freq_offset_tot_reg(self):
        return self.__MEM.rdm(self.__addr, self.__freq_offset_tot_reg_msb, self.__freq_offset_tot_reg_lsb)
    @freq_offset_tot_reg.setter
    def freq_offset_tot_reg(self, value):
        return self.__MEM.wrm(self.__addr, self.__freq_offset_tot_reg_msb, self.__freq_offset_tot_reg_lsb, value)
class NRXPILOTCONF8(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0xc4
        self.__freq_offset_tot_reg_kb_lsb = 14
        self.__freq_offset_tot_reg_kb_msb = 19
        self.__delta_phase_reg_kb_lsb = 8
        self.__delta_phase_reg_kb_msb = 13
        self.__common_phase_reg_kb_lsb = 0
        self.__common_phase_reg_kb_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def freq_offset_tot_reg_kb(self):
        return self.__MEM.rdm(self.__addr, self.__freq_offset_tot_reg_kb_msb, self.__freq_offset_tot_reg_kb_lsb)
    @freq_offset_tot_reg_kb.setter
    def freq_offset_tot_reg_kb(self, value):
        return self.__MEM.wrm(self.__addr, self.__freq_offset_tot_reg_kb_msb, self.__freq_offset_tot_reg_kb_lsb, value)

    @property
    def delta_phase_reg_kb(self):
        return self.__MEM.rdm(self.__addr, self.__delta_phase_reg_kb_msb, self.__delta_phase_reg_kb_lsb)
    @delta_phase_reg_kb.setter
    def delta_phase_reg_kb(self, value):
        return self.__MEM.wrm(self.__addr, self.__delta_phase_reg_kb_msb, self.__delta_phase_reg_kb_lsb, value)

    @property
    def common_phase_reg_kb(self):
        return self.__MEM.rdm(self.__addr, self.__common_phase_reg_kb_msb, self.__common_phase_reg_kb_lsb)
    @common_phase_reg_kb.setter
    def common_phase_reg_kb(self, value):
        return self.__MEM.wrm(self.__addr, self.__common_phase_reg_kb_msb, self.__common_phase_reg_kb_lsb, value)
class NRXTDM2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0xc8
        self.__reg_tdm_1st_chk_wait_lsb = 23
        self.__reg_tdm_1st_chk_wait_msb = 31
        self.__reg_xcorr_agc_gt_ext_2_lsb = 22
        self.__reg_xcorr_agc_gt_ext_2_msb = 22
        self.__reg_xcorr_agc_gt_ext_lsb = 21
        self.__reg_xcorr_agc_gt_ext_msb = 21
        self.__reg_xcorr_det_agc_mode_2_lsb = 20
        self.__reg_xcorr_det_agc_mode_2_msb = 20
        self.__reg_xcorr_det_agc_mode_lsb = 19
        self.__reg_xcorr_det_agc_mode_msb = 19
        self.__reg_xcorr_agc_pre64_en_2_lsb = 18
        self.__reg_xcorr_agc_pre64_en_2_msb = 18
        self.__reg_xcorr_agc_pre64_en_lsb = 17
        self.__reg_xcorr_agc_pre64_en_msb = 17
        self.__reg_xcorr_agc_2th_ext_lsb = 16
        self.__reg_xcorr_agc_2th_ext_msb = 16
        self.__reg_xcorr_agc_2th_en_2_lsb = 15
        self.__reg_xcorr_agc_2th_en_2_msb = 15
        self.__reg_xcorr_agc_2th_en_lsb = 14
        self.__reg_xcorr_agc_2th_en_msb = 14
        self.__reg_xcorr_agc_thr2_lsb = 7
        self.__reg_xcorr_agc_thr2_msb = 13
        self.__reg_xcorr_agc_thr1_lsb = 0
        self.__reg_xcorr_agc_thr1_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tdm_1st_chk_wait(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tdm_1st_chk_wait_msb, self.__reg_tdm_1st_chk_wait_lsb)
    @reg_tdm_1st_chk_wait.setter
    def reg_tdm_1st_chk_wait(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tdm_1st_chk_wait_msb, self.__reg_tdm_1st_chk_wait_lsb, value)

    @property
    def reg_xcorr_agc_gt_ext_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_agc_gt_ext_2_msb, self.__reg_xcorr_agc_gt_ext_2_lsb)
    @reg_xcorr_agc_gt_ext_2.setter
    def reg_xcorr_agc_gt_ext_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_agc_gt_ext_2_msb, self.__reg_xcorr_agc_gt_ext_2_lsb, value)

    @property
    def reg_xcorr_agc_gt_ext(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_agc_gt_ext_msb, self.__reg_xcorr_agc_gt_ext_lsb)
    @reg_xcorr_agc_gt_ext.setter
    def reg_xcorr_agc_gt_ext(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_agc_gt_ext_msb, self.__reg_xcorr_agc_gt_ext_lsb, value)

    @property
    def reg_xcorr_det_agc_mode_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_det_agc_mode_2_msb, self.__reg_xcorr_det_agc_mode_2_lsb)
    @reg_xcorr_det_agc_mode_2.setter
    def reg_xcorr_det_agc_mode_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_det_agc_mode_2_msb, self.__reg_xcorr_det_agc_mode_2_lsb, value)

    @property
    def reg_xcorr_det_agc_mode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_det_agc_mode_msb, self.__reg_xcorr_det_agc_mode_lsb)
    @reg_xcorr_det_agc_mode.setter
    def reg_xcorr_det_agc_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_det_agc_mode_msb, self.__reg_xcorr_det_agc_mode_lsb, value)

    @property
    def reg_xcorr_agc_pre64_en_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_agc_pre64_en_2_msb, self.__reg_xcorr_agc_pre64_en_2_lsb)
    @reg_xcorr_agc_pre64_en_2.setter
    def reg_xcorr_agc_pre64_en_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_agc_pre64_en_2_msb, self.__reg_xcorr_agc_pre64_en_2_lsb, value)

    @property
    def reg_xcorr_agc_pre64_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_agc_pre64_en_msb, self.__reg_xcorr_agc_pre64_en_lsb)
    @reg_xcorr_agc_pre64_en.setter
    def reg_xcorr_agc_pre64_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_agc_pre64_en_msb, self.__reg_xcorr_agc_pre64_en_lsb, value)

    @property
    def reg_xcorr_agc_2th_ext(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_agc_2th_ext_msb, self.__reg_xcorr_agc_2th_ext_lsb)
    @reg_xcorr_agc_2th_ext.setter
    def reg_xcorr_agc_2th_ext(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_agc_2th_ext_msb, self.__reg_xcorr_agc_2th_ext_lsb, value)

    @property
    def reg_xcorr_agc_2th_en_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_agc_2th_en_2_msb, self.__reg_xcorr_agc_2th_en_2_lsb)
    @reg_xcorr_agc_2th_en_2.setter
    def reg_xcorr_agc_2th_en_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_agc_2th_en_2_msb, self.__reg_xcorr_agc_2th_en_2_lsb, value)

    @property
    def reg_xcorr_agc_2th_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_agc_2th_en_msb, self.__reg_xcorr_agc_2th_en_lsb)
    @reg_xcorr_agc_2th_en.setter
    def reg_xcorr_agc_2th_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_agc_2th_en_msb, self.__reg_xcorr_agc_2th_en_lsb, value)

    @property
    def reg_xcorr_agc_thr2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_agc_thr2_msb, self.__reg_xcorr_agc_thr2_lsb)
    @reg_xcorr_agc_thr2.setter
    def reg_xcorr_agc_thr2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_agc_thr2_msb, self.__reg_xcorr_agc_thr2_lsb, value)

    @property
    def reg_xcorr_agc_thr1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_agc_thr1_msb, self.__reg_xcorr_agc_thr1_lsb)
    @reg_xcorr_agc_thr1.setter
    def reg_xcorr_agc_thr1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_agc_thr1_msb, self.__reg_xcorr_agc_thr1_lsb, value)
class NRXCTE_CTRL4(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0xcc
        self.__reg_sc_end_thr_3_lsb = 25
        self.__reg_sc_end_thr_3_msb = 31
        self.__reg_sc_coef_3_lsb = 18
        self.__reg_sc_coef_3_msb = 24
        self.__reg_scorr_fall_sum_thr_3_lsb = 15
        self.__reg_scorr_fall_sum_thr_3_msb = 17
        self.__reg_scorr_fall_chk_num_3_lsb = 12
        self.__reg_scorr_fall_chk_num_3_msb = 14
        self.__reg_scorr_fall_sum_thr_2_lsb = 9
        self.__reg_scorr_fall_sum_thr_2_msb = 11
        self.__reg_scorr_fall_chk_num_2_lsb = 6
        self.__reg_scorr_fall_chk_num_2_msb = 8
        self.__reg_scorr_fall_sum_thr_1_lsb = 3
        self.__reg_scorr_fall_sum_thr_1_msb = 5
        self.__reg_scorr_fall_chk_num_1_lsb = 0
        self.__reg_scorr_fall_chk_num_1_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sc_end_thr_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sc_end_thr_3_msb, self.__reg_sc_end_thr_3_lsb)
    @reg_sc_end_thr_3.setter
    def reg_sc_end_thr_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sc_end_thr_3_msb, self.__reg_sc_end_thr_3_lsb, value)

    @property
    def reg_sc_coef_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sc_coef_3_msb, self.__reg_sc_coef_3_lsb)
    @reg_sc_coef_3.setter
    def reg_sc_coef_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sc_coef_3_msb, self.__reg_sc_coef_3_lsb, value)

    @property
    def reg_scorr_fall_sum_thr_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_scorr_fall_sum_thr_3_msb, self.__reg_scorr_fall_sum_thr_3_lsb)
    @reg_scorr_fall_sum_thr_3.setter
    def reg_scorr_fall_sum_thr_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_scorr_fall_sum_thr_3_msb, self.__reg_scorr_fall_sum_thr_3_lsb, value)

    @property
    def reg_scorr_fall_chk_num_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_scorr_fall_chk_num_3_msb, self.__reg_scorr_fall_chk_num_3_lsb)
    @reg_scorr_fall_chk_num_3.setter
    def reg_scorr_fall_chk_num_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_scorr_fall_chk_num_3_msb, self.__reg_scorr_fall_chk_num_3_lsb, value)

    @property
    def reg_scorr_fall_sum_thr_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_scorr_fall_sum_thr_2_msb, self.__reg_scorr_fall_sum_thr_2_lsb)
    @reg_scorr_fall_sum_thr_2.setter
    def reg_scorr_fall_sum_thr_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_scorr_fall_sum_thr_2_msb, self.__reg_scorr_fall_sum_thr_2_lsb, value)

    @property
    def reg_scorr_fall_chk_num_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_scorr_fall_chk_num_2_msb, self.__reg_scorr_fall_chk_num_2_lsb)
    @reg_scorr_fall_chk_num_2.setter
    def reg_scorr_fall_chk_num_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_scorr_fall_chk_num_2_msb, self.__reg_scorr_fall_chk_num_2_lsb, value)

    @property
    def reg_scorr_fall_sum_thr_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_scorr_fall_sum_thr_1_msb, self.__reg_scorr_fall_sum_thr_1_lsb)
    @reg_scorr_fall_sum_thr_1.setter
    def reg_scorr_fall_sum_thr_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_scorr_fall_sum_thr_1_msb, self.__reg_scorr_fall_sum_thr_1_lsb, value)

    @property
    def reg_scorr_fall_chk_num_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_scorr_fall_chk_num_1_msb, self.__reg_scorr_fall_chk_num_1_lsb)
    @reg_scorr_fall_chk_num_1.setter
    def reg_scorr_fall_chk_num_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_scorr_fall_chk_num_1_msb, self.__reg_scorr_fall_chk_num_1_lsb, value)
class NRXCTE_CTRL5(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0xd0
        self.__r_cte_typ_mrc_lsb = 28
        self.__r_cte_typ_mrc_msb = 30
        self.__reg_cte_mrc_en_lsb = 27
        self.__reg_cte_mrc_en_msb = 27
        self.__reg_cte_xcorr_loss_prot_lsb = 26
        self.__reg_cte_xcorr_loss_prot_msb = 26
        self.__reg_sc_end_thr_xcorr_lsb = 19
        self.__reg_sc_end_thr_xcorr_msb = 25
        self.__reg_xcorr_gi_pk_shr_lsb = 15
        self.__reg_xcorr_gi_pk_shr_msb = 18
        self.__reg_xcorr_gi_pk_mult_lsb = 9
        self.__reg_xcorr_gi_pk_mult_msb = 14
        self.__reg_cte_xcorr_gi_en_weak_lsb = 8
        self.__reg_cte_xcorr_gi_en_weak_msb = 8
        self.__reg_cte_xcorr_gi_en_force_lsb = 7
        self.__reg_cte_xcorr_gi_en_force_msb = 7
        self.__reg_sc_end_thr_gi_lsb = 0
        self.__reg_sc_end_thr_gi_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def r_cte_typ_mrc(self):
        return self.__MEM.rdm(self.__addr, self.__r_cte_typ_mrc_msb, self.__r_cte_typ_mrc_lsb)
    @r_cte_typ_mrc.setter
    def r_cte_typ_mrc(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_cte_typ_mrc_msb, self.__r_cte_typ_mrc_lsb, value)

    @property
    def reg_cte_mrc_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cte_mrc_en_msb, self.__reg_cte_mrc_en_lsb)
    @reg_cte_mrc_en.setter
    def reg_cte_mrc_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cte_mrc_en_msb, self.__reg_cte_mrc_en_lsb, value)

    @property
    def reg_cte_xcorr_loss_prot(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cte_xcorr_loss_prot_msb, self.__reg_cte_xcorr_loss_prot_lsb)
    @reg_cte_xcorr_loss_prot.setter
    def reg_cte_xcorr_loss_prot(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cte_xcorr_loss_prot_msb, self.__reg_cte_xcorr_loss_prot_lsb, value)

    @property
    def reg_sc_end_thr_xcorr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sc_end_thr_xcorr_msb, self.__reg_sc_end_thr_xcorr_lsb)
    @reg_sc_end_thr_xcorr.setter
    def reg_sc_end_thr_xcorr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sc_end_thr_xcorr_msb, self.__reg_sc_end_thr_xcorr_lsb, value)

    @property
    def reg_xcorr_gi_pk_shr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_gi_pk_shr_msb, self.__reg_xcorr_gi_pk_shr_lsb)
    @reg_xcorr_gi_pk_shr.setter
    def reg_xcorr_gi_pk_shr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_gi_pk_shr_msb, self.__reg_xcorr_gi_pk_shr_lsb, value)

    @property
    def reg_xcorr_gi_pk_mult(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_gi_pk_mult_msb, self.__reg_xcorr_gi_pk_mult_lsb)
    @reg_xcorr_gi_pk_mult.setter
    def reg_xcorr_gi_pk_mult(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_gi_pk_mult_msb, self.__reg_xcorr_gi_pk_mult_lsb, value)

    @property
    def reg_cte_xcorr_gi_en_weak(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cte_xcorr_gi_en_weak_msb, self.__reg_cte_xcorr_gi_en_weak_lsb)
    @reg_cte_xcorr_gi_en_weak.setter
    def reg_cte_xcorr_gi_en_weak(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cte_xcorr_gi_en_weak_msb, self.__reg_cte_xcorr_gi_en_weak_lsb, value)

    @property
    def reg_cte_xcorr_gi_en_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cte_xcorr_gi_en_force_msb, self.__reg_cte_xcorr_gi_en_force_lsb)
    @reg_cte_xcorr_gi_en_force.setter
    def reg_cte_xcorr_gi_en_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cte_xcorr_gi_en_force_msb, self.__reg_cte_xcorr_gi_en_force_lsb, value)

    @property
    def reg_sc_end_thr_gi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sc_end_thr_gi_msb, self.__reg_sc_end_thr_gi_lsb)
    @reg_sc_end_thr_gi.setter
    def reg_sc_end_thr_gi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sc_end_thr_gi_msb, self.__reg_sc_end_thr_gi_lsb, value)
class NRXPD_CTRL(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0xd4
        self.__reg_tdm_corr_force_pu_lsb = 9
        self.__reg_tdm_corr_force_pu_msb = 9
        self.__reg_tdm_corr_force_pd_lsb = 8
        self.__reg_tdm_corr_force_pd_msb = 8
        self.__reg_chan_est_force_pu_lsb = 7
        self.__reg_chan_est_force_pu_msb = 7
        self.__reg_chan_est_force_pd_lsb = 6
        self.__reg_chan_est_force_pd_msb = 6
        self.__reg_rx_rot_force_pu_lsb = 5
        self.__reg_rx_rot_force_pu_msb = 5
        self.__reg_rx_rot_force_pd_lsb = 4
        self.__reg_rx_rot_force_pd_msb = 4
        self.__reg_vit_force_pu_lsb = 3
        self.__reg_vit_force_pu_msb = 3
        self.__reg_vit_force_pd_lsb = 2
        self.__reg_vit_force_pd_msb = 2
        self.__reg_demap_force_pu_lsb = 1
        self.__reg_demap_force_pu_msb = 1
        self.__reg_demap_force_pd_lsb = 0
        self.__reg_demap_force_pd_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tdm_corr_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tdm_corr_force_pu_msb, self.__reg_tdm_corr_force_pu_lsb)
    @reg_tdm_corr_force_pu.setter
    def reg_tdm_corr_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tdm_corr_force_pu_msb, self.__reg_tdm_corr_force_pu_lsb, value)

    @property
    def reg_tdm_corr_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tdm_corr_force_pd_msb, self.__reg_tdm_corr_force_pd_lsb)
    @reg_tdm_corr_force_pd.setter
    def reg_tdm_corr_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tdm_corr_force_pd_msb, self.__reg_tdm_corr_force_pd_lsb, value)

    @property
    def reg_chan_est_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_est_force_pu_msb, self.__reg_chan_est_force_pu_lsb)
    @reg_chan_est_force_pu.setter
    def reg_chan_est_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_est_force_pu_msb, self.__reg_chan_est_force_pu_lsb, value)

    @property
    def reg_chan_est_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_est_force_pd_msb, self.__reg_chan_est_force_pd_lsb)
    @reg_chan_est_force_pd.setter
    def reg_chan_est_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_est_force_pd_msb, self.__reg_chan_est_force_pd_lsb, value)

    @property
    def reg_rx_rot_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_rot_force_pu_msb, self.__reg_rx_rot_force_pu_lsb)
    @reg_rx_rot_force_pu.setter
    def reg_rx_rot_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_rot_force_pu_msb, self.__reg_rx_rot_force_pu_lsb, value)

    @property
    def reg_rx_rot_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_rot_force_pd_msb, self.__reg_rx_rot_force_pd_lsb)
    @reg_rx_rot_force_pd.setter
    def reg_rx_rot_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_rot_force_pd_msb, self.__reg_rx_rot_force_pd_lsb, value)

    @property
    def reg_vit_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_vit_force_pu_msb, self.__reg_vit_force_pu_lsb)
    @reg_vit_force_pu.setter
    def reg_vit_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_vit_force_pu_msb, self.__reg_vit_force_pu_lsb, value)

    @property
    def reg_vit_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_vit_force_pd_msb, self.__reg_vit_force_pd_lsb)
    @reg_vit_force_pd.setter
    def reg_vit_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_vit_force_pd_msb, self.__reg_vit_force_pd_lsb, value)

    @property
    def reg_demap_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_demap_force_pu_msb, self.__reg_demap_force_pu_lsb)
    @reg_demap_force_pu.setter
    def reg_demap_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_demap_force_pu_msb, self.__reg_demap_force_pu_lsb, value)

    @property
    def reg_demap_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_demap_force_pd_msb, self.__reg_demap_force_pd_lsb)
    @reg_demap_force_pd.setter
    def reg_demap_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_demap_force_pd_msb, self.__reg_demap_force_pd_lsb, value)
class NRXFTE1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0xd8
        self.__reg_non_gi_rot_nonstbc_en_lsb = 15
        self.__reg_non_gi_rot_nonstbc_en_msb = 15
        self.__reg_non_gi_rot_stbc_en_lsb = 14
        self.__reg_non_gi_rot_stbc_en_msb = 14
        self.__reg_fte_tar_backoff_stbc_comp_lsb = 7
        self.__reg_fte_tar_backoff_stbc_comp_msb = 13
        self.__reg_fte_tar_backoff_sgi_comp_lsb = 0
        self.__reg_fte_tar_backoff_sgi_comp_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_non_gi_rot_nonstbc_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_non_gi_rot_nonstbc_en_msb, self.__reg_non_gi_rot_nonstbc_en_lsb)
    @reg_non_gi_rot_nonstbc_en.setter
    def reg_non_gi_rot_nonstbc_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_non_gi_rot_nonstbc_en_msb, self.__reg_non_gi_rot_nonstbc_en_lsb, value)

    @property
    def reg_non_gi_rot_stbc_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_non_gi_rot_stbc_en_msb, self.__reg_non_gi_rot_stbc_en_lsb)
    @reg_non_gi_rot_stbc_en.setter
    def reg_non_gi_rot_stbc_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_non_gi_rot_stbc_en_msb, self.__reg_non_gi_rot_stbc_en_lsb, value)

    @property
    def reg_fte_tar_backoff_stbc_comp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fte_tar_backoff_stbc_comp_msb, self.__reg_fte_tar_backoff_stbc_comp_lsb)
    @reg_fte_tar_backoff_stbc_comp.setter
    def reg_fte_tar_backoff_stbc_comp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fte_tar_backoff_stbc_comp_msb, self.__reg_fte_tar_backoff_stbc_comp_lsb, value)

    @property
    def reg_fte_tar_backoff_sgi_comp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fte_tar_backoff_sgi_comp_msb, self.__reg_fte_tar_backoff_sgi_comp_lsb)
    @reg_fte_tar_backoff_sgi_comp.setter
    def reg_fte_tar_backoff_sgi_comp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fte_tar_backoff_sgi_comp_msb, self.__reg_fte_tar_backoff_sgi_comp_lsb, value)
class NRXTDM3(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0xdc
        self.__reg_xcorr_pk_shr_3_lsb = 22
        self.__reg_xcorr_pk_shr_3_msb = 25
        self.__reg_xcorr_pk_mult_3_lsb = 16
        self.__reg_xcorr_pk_mult_3_msb = 21
        self.__reg_xcorr_agc_pre64_en_3_lsb = 15
        self.__reg_xcorr_agc_pre64_en_3_msb = 15
        self.__reg_xcorr_agc_2th_en_3_lsb = 14
        self.__reg_xcorr_agc_2th_en_3_msb = 14
        self.__reg_xcorr_find_thr3_lsb = 7
        self.__reg_xcorr_find_thr3_msb = 13
        self.__reg_xcorr_agc_thr3_lsb = 0
        self.__reg_xcorr_agc_thr3_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_xcorr_pk_shr_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_pk_shr_3_msb, self.__reg_xcorr_pk_shr_3_lsb)
    @reg_xcorr_pk_shr_3.setter
    def reg_xcorr_pk_shr_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_pk_shr_3_msb, self.__reg_xcorr_pk_shr_3_lsb, value)

    @property
    def reg_xcorr_pk_mult_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_pk_mult_3_msb, self.__reg_xcorr_pk_mult_3_lsb)
    @reg_xcorr_pk_mult_3.setter
    def reg_xcorr_pk_mult_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_pk_mult_3_msb, self.__reg_xcorr_pk_mult_3_lsb, value)

    @property
    def reg_xcorr_agc_pre64_en_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_agc_pre64_en_3_msb, self.__reg_xcorr_agc_pre64_en_3_lsb)
    @reg_xcorr_agc_pre64_en_3.setter
    def reg_xcorr_agc_pre64_en_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_agc_pre64_en_3_msb, self.__reg_xcorr_agc_pre64_en_3_lsb, value)

    @property
    def reg_xcorr_agc_2th_en_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_agc_2th_en_3_msb, self.__reg_xcorr_agc_2th_en_3_lsb)
    @reg_xcorr_agc_2th_en_3.setter
    def reg_xcorr_agc_2th_en_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_agc_2th_en_3_msb, self.__reg_xcorr_agc_2th_en_3_lsb, value)

    @property
    def reg_xcorr_find_thr3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_find_thr3_msb, self.__reg_xcorr_find_thr3_lsb)
    @reg_xcorr_find_thr3.setter
    def reg_xcorr_find_thr3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_find_thr3_msb, self.__reg_xcorr_find_thr3_lsb, value)

    @property
    def reg_xcorr_agc_thr3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_agc_thr3_msb, self.__reg_xcorr_agc_thr3_lsb)
    @reg_xcorr_agc_thr3.setter
    def reg_xcorr_agc_thr3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_agc_thr3_msb, self.__reg_xcorr_agc_thr3_lsb, value)
class NRXCTE_CTRL6(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0xe0
        self.__reg_sc_end_thr_foe_en_lsb = 25
        self.__reg_sc_end_thr_foe_en_msb = 25
        self.__reg_sc_end_thr_foe_lsb = 18
        self.__reg_sc_end_thr_foe_msb = 24
        self.__reg_scorr_foe_fall_sum_thr_3_lsb = 15
        self.__reg_scorr_foe_fall_sum_thr_3_msb = 17
        self.__reg_scorr_foe_fall_chk_num_3_lsb = 12
        self.__reg_scorr_foe_fall_chk_num_3_msb = 14
        self.__reg_scorr_foe_fall_sum_thr_2_lsb = 9
        self.__reg_scorr_foe_fall_sum_thr_2_msb = 11
        self.__reg_scorr_foe_fall_chk_num_2_lsb = 6
        self.__reg_scorr_foe_fall_chk_num_2_msb = 8
        self.__reg_scorr_foe_fall_sum_thr_1_lsb = 3
        self.__reg_scorr_foe_fall_sum_thr_1_msb = 5
        self.__reg_scorr_foe_fall_chk_num_1_lsb = 0
        self.__reg_scorr_foe_fall_chk_num_1_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sc_end_thr_foe_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sc_end_thr_foe_en_msb, self.__reg_sc_end_thr_foe_en_lsb)
    @reg_sc_end_thr_foe_en.setter
    def reg_sc_end_thr_foe_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sc_end_thr_foe_en_msb, self.__reg_sc_end_thr_foe_en_lsb, value)

    @property
    def reg_sc_end_thr_foe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sc_end_thr_foe_msb, self.__reg_sc_end_thr_foe_lsb)
    @reg_sc_end_thr_foe.setter
    def reg_sc_end_thr_foe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sc_end_thr_foe_msb, self.__reg_sc_end_thr_foe_lsb, value)

    @property
    def reg_scorr_foe_fall_sum_thr_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_scorr_foe_fall_sum_thr_3_msb, self.__reg_scorr_foe_fall_sum_thr_3_lsb)
    @reg_scorr_foe_fall_sum_thr_3.setter
    def reg_scorr_foe_fall_sum_thr_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_scorr_foe_fall_sum_thr_3_msb, self.__reg_scorr_foe_fall_sum_thr_3_lsb, value)

    @property
    def reg_scorr_foe_fall_chk_num_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_scorr_foe_fall_chk_num_3_msb, self.__reg_scorr_foe_fall_chk_num_3_lsb)
    @reg_scorr_foe_fall_chk_num_3.setter
    def reg_scorr_foe_fall_chk_num_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_scorr_foe_fall_chk_num_3_msb, self.__reg_scorr_foe_fall_chk_num_3_lsb, value)

    @property
    def reg_scorr_foe_fall_sum_thr_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_scorr_foe_fall_sum_thr_2_msb, self.__reg_scorr_foe_fall_sum_thr_2_lsb)
    @reg_scorr_foe_fall_sum_thr_2.setter
    def reg_scorr_foe_fall_sum_thr_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_scorr_foe_fall_sum_thr_2_msb, self.__reg_scorr_foe_fall_sum_thr_2_lsb, value)

    @property
    def reg_scorr_foe_fall_chk_num_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_scorr_foe_fall_chk_num_2_msb, self.__reg_scorr_foe_fall_chk_num_2_lsb)
    @reg_scorr_foe_fall_chk_num_2.setter
    def reg_scorr_foe_fall_chk_num_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_scorr_foe_fall_chk_num_2_msb, self.__reg_scorr_foe_fall_chk_num_2_lsb, value)

    @property
    def reg_scorr_foe_fall_sum_thr_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_scorr_foe_fall_sum_thr_1_msb, self.__reg_scorr_foe_fall_sum_thr_1_lsb)
    @reg_scorr_foe_fall_sum_thr_1.setter
    def reg_scorr_foe_fall_sum_thr_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_scorr_foe_fall_sum_thr_1_msb, self.__reg_scorr_foe_fall_sum_thr_1_lsb, value)

    @property
    def reg_scorr_foe_fall_chk_num_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_scorr_foe_fall_chk_num_1_msb, self.__reg_scorr_foe_fall_chk_num_1_lsb)
    @reg_scorr_foe_fall_chk_num_1.setter
    def reg_scorr_foe_fall_chk_num_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_scorr_foe_fall_chk_num_1_msb, self.__reg_scorr_foe_fall_chk_num_1_lsb, value)
class NRXCTE_CTRL7(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0xe4
        self.__reg_ltf_foe_end_cnt_lsb = 24
        self.__reg_ltf_foe_end_cnt_msb = 30
        self.__reg_demod_sig_mrc_dis_lsb = 23
        self.__reg_demod_sig_mrc_dis_msb = 23
        self.__reg_demod_mrc_en_lsb = 22
        self.__reg_demod_mrc_en_msb = 22
        self.__reg_scorr_cmp_shr_lsb = 20
        self.__reg_scorr_cmp_shr_msb = 21
        self.__reg_cte_sec_gt_thr_lsb = 16
        self.__reg_cte_sec_gt_thr_msb = 19
        self.__reg_cte_mrc_xcorr_en_lsb = 15
        self.__reg_cte_mrc_xcorr_en_msb = 15
        self.__reg_cte_mrc_xcorr_mask_lsb = 0
        self.__reg_cte_mrc_xcorr_mask_msb = 14
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ltf_foe_end_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ltf_foe_end_cnt_msb, self.__reg_ltf_foe_end_cnt_lsb)
    @reg_ltf_foe_end_cnt.setter
    def reg_ltf_foe_end_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ltf_foe_end_cnt_msb, self.__reg_ltf_foe_end_cnt_lsb, value)

    @property
    def reg_demod_sig_mrc_dis(self):
        return self.__MEM.rdm(self.__addr, self.__reg_demod_sig_mrc_dis_msb, self.__reg_demod_sig_mrc_dis_lsb)
    @reg_demod_sig_mrc_dis.setter
    def reg_demod_sig_mrc_dis(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_demod_sig_mrc_dis_msb, self.__reg_demod_sig_mrc_dis_lsb, value)

    @property
    def reg_demod_mrc_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_demod_mrc_en_msb, self.__reg_demod_mrc_en_lsb)
    @reg_demod_mrc_en.setter
    def reg_demod_mrc_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_demod_mrc_en_msb, self.__reg_demod_mrc_en_lsb, value)

    @property
    def reg_scorr_cmp_shr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_scorr_cmp_shr_msb, self.__reg_scorr_cmp_shr_lsb)
    @reg_scorr_cmp_shr.setter
    def reg_scorr_cmp_shr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_scorr_cmp_shr_msb, self.__reg_scorr_cmp_shr_lsb, value)

    @property
    def reg_cte_sec_gt_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cte_sec_gt_thr_msb, self.__reg_cte_sec_gt_thr_lsb)
    @reg_cte_sec_gt_thr.setter
    def reg_cte_sec_gt_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cte_sec_gt_thr_msb, self.__reg_cte_sec_gt_thr_lsb, value)

    @property
    def reg_cte_mrc_xcorr_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cte_mrc_xcorr_en_msb, self.__reg_cte_mrc_xcorr_en_lsb)
    @reg_cte_mrc_xcorr_en.setter
    def reg_cte_mrc_xcorr_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cte_mrc_xcorr_en_msb, self.__reg_cte_mrc_xcorr_en_lsb, value)

    @property
    def reg_cte_mrc_xcorr_mask(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cte_mrc_xcorr_mask_msb, self.__reg_cte_mrc_xcorr_mask_lsb)
    @reg_cte_mrc_xcorr_mask.setter
    def reg_cte_mrc_xcorr_mask(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cte_mrc_xcorr_mask_msb, self.__reg_cte_mrc_xcorr_mask_lsb, value)
class NRXPILOTCONF9(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0xe8
        self.__reg_foe_delta_phi_thr_down_lsb = 0
        self.__reg_foe_delta_phi_thr_down_msb = 14
        self.__reg_foe_delta_phi_thr_up_lsb = 0
        self.__reg_foe_delta_phi_thr_up_msb = 14
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_foe_delta_phi_thr_down(self):
        return self.__MEM.rdm(self.__addr, self.__reg_foe_delta_phi_thr_down_msb, self.__reg_foe_delta_phi_thr_down_lsb)
    @reg_foe_delta_phi_thr_down.setter
    def reg_foe_delta_phi_thr_down(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_foe_delta_phi_thr_down_msb, self.__reg_foe_delta_phi_thr_down_lsb, value)

    @property
    def reg_foe_delta_phi_thr_up(self):
        return self.__MEM.rdm(self.__addr, self.__reg_foe_delta_phi_thr_up_msb, self.__reg_foe_delta_phi_thr_up_lsb)
    @reg_foe_delta_phi_thr_up.setter
    def reg_foe_delta_phi_thr_up(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_foe_delta_phi_thr_up_msb, self.__reg_foe_delta_phi_thr_up_lsb, value)
class NRXCLKGATE(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0xec
        self.__reg_ftm_force_clk_lsb = 9
        self.__reg_ftm_force_clk_msb = 9
        self.__reg_nrx_clk_opt_dis_lsb = 8
        self.__reg_nrx_clk_opt_dis_msb = 8
        self.__reg_corr_find_force_clk_lsb = 7
        self.__reg_corr_find_force_clk_msb = 7
        self.__reg_spur_gen_force_clk_lsb = 6
        self.__reg_spur_gen_force_clk_msb = 6
        self.__reg_fte_force_clk_lsb = 5
        self.__reg_fte_force_clk_msb = 5
        self.__reg_demod_force_clk_lsb = 4
        self.__reg_demod_force_clk_msb = 4
        self.__reg_corr_force_clk_lsb = 3
        self.__reg_corr_force_clk_msb = 3
        self.__reg_rx_rot_force_clk_lsb = 2
        self.__reg_rx_rot_force_clk_msb = 2
        self.__reg_chan_est_force_clk_lsb = 1
        self.__reg_chan_est_force_clk_msb = 1
        self.__reg_equ_force_clk_lsb = 0
        self.__reg_equ_force_clk_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ftm_force_clk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ftm_force_clk_msb, self.__reg_ftm_force_clk_lsb)
    @reg_ftm_force_clk.setter
    def reg_ftm_force_clk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ftm_force_clk_msb, self.__reg_ftm_force_clk_lsb, value)

    @property
    def reg_nrx_clk_opt_dis(self):
        return self.__MEM.rdm(self.__addr, self.__reg_nrx_clk_opt_dis_msb, self.__reg_nrx_clk_opt_dis_lsb)
    @reg_nrx_clk_opt_dis.setter
    def reg_nrx_clk_opt_dis(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_nrx_clk_opt_dis_msb, self.__reg_nrx_clk_opt_dis_lsb, value)

    @property
    def reg_corr_find_force_clk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_find_force_clk_msb, self.__reg_corr_find_force_clk_lsb)
    @reg_corr_find_force_clk.setter
    def reg_corr_find_force_clk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_find_force_clk_msb, self.__reg_corr_find_force_clk_lsb, value)

    @property
    def reg_spur_gen_force_clk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_spur_gen_force_clk_msb, self.__reg_spur_gen_force_clk_lsb)
    @reg_spur_gen_force_clk.setter
    def reg_spur_gen_force_clk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_spur_gen_force_clk_msb, self.__reg_spur_gen_force_clk_lsb, value)

    @property
    def reg_fte_force_clk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fte_force_clk_msb, self.__reg_fte_force_clk_lsb)
    @reg_fte_force_clk.setter
    def reg_fte_force_clk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fte_force_clk_msb, self.__reg_fte_force_clk_lsb, value)

    @property
    def reg_demod_force_clk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_demod_force_clk_msb, self.__reg_demod_force_clk_lsb)
    @reg_demod_force_clk.setter
    def reg_demod_force_clk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_demod_force_clk_msb, self.__reg_demod_force_clk_lsb, value)

    @property
    def reg_corr_force_clk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_force_clk_msb, self.__reg_corr_force_clk_lsb)
    @reg_corr_force_clk.setter
    def reg_corr_force_clk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_force_clk_msb, self.__reg_corr_force_clk_lsb, value)

    @property
    def reg_rx_rot_force_clk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_rot_force_clk_msb, self.__reg_rx_rot_force_clk_lsb)
    @reg_rx_rot_force_clk.setter
    def reg_rx_rot_force_clk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_rot_force_clk_msb, self.__reg_rx_rot_force_clk_lsb, value)

    @property
    def reg_chan_est_force_clk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_est_force_clk_msb, self.__reg_chan_est_force_clk_lsb)
    @reg_chan_est_force_clk.setter
    def reg_chan_est_force_clk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_est_force_clk_msb, self.__reg_chan_est_force_clk_lsb, value)

    @property
    def reg_equ_force_clk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_equ_force_clk_msb, self.__reg_equ_force_clk_lsb)
    @reg_equ_force_clk.setter
    def reg_equ_force_clk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_equ_force_clk_msb, self.__reg_equ_force_clk_lsb, value)
class NRXPILOTCONF10(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0xf0
        self.__reg_chan_rot_force_en_lsb = 21
        self.__reg_chan_rot_force_en_msb = 21
        self.__reg_chan_rot_slope_force_lsb = 0
        self.__reg_chan_rot_slope_force_msb = 20
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_chan_rot_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_rot_force_en_msb, self.__reg_chan_rot_force_en_lsb)
    @reg_chan_rot_force_en.setter
    def reg_chan_rot_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_rot_force_en_msb, self.__reg_chan_rot_force_en_lsb, value)

    @property
    def reg_chan_rot_slope_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_rot_slope_force_msb, self.__reg_chan_rot_slope_force_lsb)
    @reg_chan_rot_slope_force.setter
    def reg_chan_rot_slope_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_rot_slope_force_msb, self.__reg_chan_rot_slope_force_lsb, value)
class NRXPILOTCONF11(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0xf4
        self.__reg_chan_rot_com_pha_force_lsb = 0
        self.__reg_chan_rot_com_pha_force_msb = 20
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_chan_rot_com_pha_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_rot_com_pha_force_msb, self.__reg_chan_rot_com_pha_force_lsb)
    @reg_chan_rot_com_pha_force.setter
    def reg_chan_rot_com_pha_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_rot_com_pha_force_msb, self.__reg_chan_rot_com_pha_force_lsb, value)
class NRXCHANESTFILTCONF0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0xf8
        self.__reg_num_gt_ChAcorrThres_lsb = 24
        self.__reg_num_gt_ChAcorrThres_msb = 29
        self.__reg_CoA_dB_Thres1_lsb = 16
        self.__reg_CoA_dB_Thres1_msb = 23
        self.__reg_CoA_dB_Thres0_lsb = 8
        self.__reg_CoA_dB_Thres0_msb = 15
        self.__reg_ChAcorrThres_lsb = 0
        self.__reg_ChAcorrThres_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_num_gt_ChAcorrThres(self):
        return self.__MEM.rdm(self.__addr, self.__reg_num_gt_ChAcorrThres_msb, self.__reg_num_gt_ChAcorrThres_lsb)
    @reg_num_gt_ChAcorrThres.setter
    def reg_num_gt_ChAcorrThres(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_num_gt_ChAcorrThres_msb, self.__reg_num_gt_ChAcorrThres_lsb, value)

    @property
    def reg_CoA_dB_Thres1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_CoA_dB_Thres1_msb, self.__reg_CoA_dB_Thres1_lsb)
    @reg_CoA_dB_Thres1.setter
    def reg_CoA_dB_Thres1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_CoA_dB_Thres1_msb, self.__reg_CoA_dB_Thres1_lsb, value)

    @property
    def reg_CoA_dB_Thres0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_CoA_dB_Thres0_msb, self.__reg_CoA_dB_Thres0_lsb)
    @reg_CoA_dB_Thres0.setter
    def reg_CoA_dB_Thres0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_CoA_dB_Thres0_msb, self.__reg_CoA_dB_Thres0_lsb, value)

    @property
    def reg_ChAcorrThres(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ChAcorrThres_msb, self.__reg_ChAcorrThres_lsb)
    @reg_ChAcorrThres.setter
    def reg_ChAcorrThres(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ChAcorrThres_msb, self.__reg_ChAcorrThres_lsb, value)
class NRXCHANESTFILTCONF1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0xfc
        self.__reg_force_chan_filt_sel_en_lsb = 31
        self.__reg_force_chan_filt_sel_en_msb = 31
        self.__reg_force_chan_filt_sel_lsb = 28
        self.__reg_force_chan_filt_sel_msb = 30
        self.__reg_num_ChCcorr_pk_lsb = 24
        self.__reg_num_ChCcorr_pk_msb = 27
        self.__reg_ChCcorrThresVec2_lsb = 16
        self.__reg_ChCcorrThresVec2_msb = 23
        self.__reg_ChCcorrThresVec1_lsb = 8
        self.__reg_ChCcorrThresVec1_msb = 15
        self.__reg_ChCcorrThresVec0_lsb = 0
        self.__reg_ChCcorrThresVec0_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_force_chan_filt_sel_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_force_chan_filt_sel_en_msb, self.__reg_force_chan_filt_sel_en_lsb)
    @reg_force_chan_filt_sel_en.setter
    def reg_force_chan_filt_sel_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_force_chan_filt_sel_en_msb, self.__reg_force_chan_filt_sel_en_lsb, value)

    @property
    def reg_force_chan_filt_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_force_chan_filt_sel_msb, self.__reg_force_chan_filt_sel_lsb)
    @reg_force_chan_filt_sel.setter
    def reg_force_chan_filt_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_force_chan_filt_sel_msb, self.__reg_force_chan_filt_sel_lsb, value)

    @property
    def reg_num_ChCcorr_pk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_num_ChCcorr_pk_msb, self.__reg_num_ChCcorr_pk_lsb)
    @reg_num_ChCcorr_pk.setter
    def reg_num_ChCcorr_pk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_num_ChCcorr_pk_msb, self.__reg_num_ChCcorr_pk_lsb, value)

    @property
    def reg_ChCcorrThresVec2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ChCcorrThresVec2_msb, self.__reg_ChCcorrThresVec2_lsb)
    @reg_ChCcorrThresVec2.setter
    def reg_ChCcorrThresVec2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ChCcorrThresVec2_msb, self.__reg_ChCcorrThresVec2_lsb, value)

    @property
    def reg_ChCcorrThresVec1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ChCcorrThresVec1_msb, self.__reg_ChCcorrThresVec1_lsb)
    @reg_ChCcorrThresVec1.setter
    def reg_ChCcorrThresVec1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ChCcorrThresVec1_msb, self.__reg_ChCcorrThresVec1_lsb, value)

    @property
    def reg_ChCcorrThresVec0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ChCcorrThresVec0_msb, self.__reg_ChCcorrThresVec0_lsb)
    @reg_ChCcorrThresVec0.setter
    def reg_ChCcorrThresVec0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ChCcorrThresVec0_msb, self.__reg_ChCcorrThresVec0_lsb, value)
class NRXFSM_DEBUG0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x100
        self.__reg_ht_rate_pre_en_lsb = 11
        self.__reg_ht_rate_pre_en_msb = 11
        self.__reg_fsm_lsym_max_lsb = 0
        self.__reg_fsm_lsym_max_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ht_rate_pre_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ht_rate_pre_en_msb, self.__reg_ht_rate_pre_en_lsb)
    @reg_ht_rate_pre_en.setter
    def reg_ht_rate_pre_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ht_rate_pre_en_msb, self.__reg_ht_rate_pre_en_lsb, value)

    @property
    def reg_fsm_lsym_max(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fsm_lsym_max_msb, self.__reg_fsm_lsym_max_lsb)
    @reg_fsm_lsym_max.setter
    def reg_fsm_lsym_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fsm_lsym_max_msb, self.__reg_fsm_lsym_max_lsb, value)
class NRXCHANESTWEIGHTSELDOWN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x104
        self.__reg_weight_sel_down_smoothing_stbc_wide_lsb = 28
        self.__reg_weight_sel_down_smoothing_stbc_wide_msb = 30
        self.__reg_weight_sel_down_smoothing_stbc_narrow_lsb = 24
        self.__reg_weight_sel_down_smoothing_stbc_narrow_msb = 26
        self.__reg_weight_sel_down_smoothing_nonstbc_wide_lsb = 20
        self.__reg_weight_sel_down_smoothing_nonstbc_wide_msb = 22
        self.__reg_weight_sel_down_smoothing_nonstbc_narrow_lsb = 16
        self.__reg_weight_sel_down_smoothing_nonstbc_narrow_msb = 18
        self.__reg_weight_sel_down_nonsmoothing_stbc_lsb = 12
        self.__reg_weight_sel_down_nonsmoothing_stbc_msb = 14
        self.__reg_weight_sel_down_nonsmoothing_nonstbc_lsb = 8
        self.__reg_weight_sel_down_nonsmoothing_nonstbc_msb = 10
        self.__reg_weight_sel_down_xsmoothing_lsb = 4
        self.__reg_weight_sel_down_xsmoothing_msb = 6
        self.__reg_weight_sel_down_force_lsb = 0
        self.__reg_weight_sel_down_force_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_weight_sel_down_smoothing_stbc_wide(self):
        return self.__MEM.rdm(self.__addr, self.__reg_weight_sel_down_smoothing_stbc_wide_msb, self.__reg_weight_sel_down_smoothing_stbc_wide_lsb)
    @reg_weight_sel_down_smoothing_stbc_wide.setter
    def reg_weight_sel_down_smoothing_stbc_wide(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_weight_sel_down_smoothing_stbc_wide_msb, self.__reg_weight_sel_down_smoothing_stbc_wide_lsb, value)

    @property
    def reg_weight_sel_down_smoothing_stbc_narrow(self):
        return self.__MEM.rdm(self.__addr, self.__reg_weight_sel_down_smoothing_stbc_narrow_msb, self.__reg_weight_sel_down_smoothing_stbc_narrow_lsb)
    @reg_weight_sel_down_smoothing_stbc_narrow.setter
    def reg_weight_sel_down_smoothing_stbc_narrow(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_weight_sel_down_smoothing_stbc_narrow_msb, self.__reg_weight_sel_down_smoothing_stbc_narrow_lsb, value)

    @property
    def reg_weight_sel_down_smoothing_nonstbc_wide(self):
        return self.__MEM.rdm(self.__addr, self.__reg_weight_sel_down_smoothing_nonstbc_wide_msb, self.__reg_weight_sel_down_smoothing_nonstbc_wide_lsb)
    @reg_weight_sel_down_smoothing_nonstbc_wide.setter
    def reg_weight_sel_down_smoothing_nonstbc_wide(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_weight_sel_down_smoothing_nonstbc_wide_msb, self.__reg_weight_sel_down_smoothing_nonstbc_wide_lsb, value)

    @property
    def reg_weight_sel_down_smoothing_nonstbc_narrow(self):
        return self.__MEM.rdm(self.__addr, self.__reg_weight_sel_down_smoothing_nonstbc_narrow_msb, self.__reg_weight_sel_down_smoothing_nonstbc_narrow_lsb)
    @reg_weight_sel_down_smoothing_nonstbc_narrow.setter
    def reg_weight_sel_down_smoothing_nonstbc_narrow(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_weight_sel_down_smoothing_nonstbc_narrow_msb, self.__reg_weight_sel_down_smoothing_nonstbc_narrow_lsb, value)

    @property
    def reg_weight_sel_down_nonsmoothing_stbc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_weight_sel_down_nonsmoothing_stbc_msb, self.__reg_weight_sel_down_nonsmoothing_stbc_lsb)
    @reg_weight_sel_down_nonsmoothing_stbc.setter
    def reg_weight_sel_down_nonsmoothing_stbc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_weight_sel_down_nonsmoothing_stbc_msb, self.__reg_weight_sel_down_nonsmoothing_stbc_lsb, value)

    @property
    def reg_weight_sel_down_nonsmoothing_nonstbc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_weight_sel_down_nonsmoothing_nonstbc_msb, self.__reg_weight_sel_down_nonsmoothing_nonstbc_lsb)
    @reg_weight_sel_down_nonsmoothing_nonstbc.setter
    def reg_weight_sel_down_nonsmoothing_nonstbc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_weight_sel_down_nonsmoothing_nonstbc_msb, self.__reg_weight_sel_down_nonsmoothing_nonstbc_lsb, value)

    @property
    def reg_weight_sel_down_xsmoothing(self):
        return self.__MEM.rdm(self.__addr, self.__reg_weight_sel_down_xsmoothing_msb, self.__reg_weight_sel_down_xsmoothing_lsb)
    @reg_weight_sel_down_xsmoothing.setter
    def reg_weight_sel_down_xsmoothing(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_weight_sel_down_xsmoothing_msb, self.__reg_weight_sel_down_xsmoothing_lsb, value)

    @property
    def reg_weight_sel_down_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_weight_sel_down_force_msb, self.__reg_weight_sel_down_force_lsb)
    @reg_weight_sel_down_force.setter
    def reg_weight_sel_down_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_weight_sel_down_force_msb, self.__reg_weight_sel_down_force_lsb, value)
class NRXCHANESTWEIGHTSELUP(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x108
        self.__reg_weight_sel_up_smoothing_stbc_wide_lsb = 28
        self.__reg_weight_sel_up_smoothing_stbc_wide_msb = 30
        self.__reg_weight_sel_up_smoothing_stbc_narrow_lsb = 24
        self.__reg_weight_sel_up_smoothing_stbc_narrow_msb = 26
        self.__reg_weight_sel_up_smoothing_nonstbc_wide_lsb = 20
        self.__reg_weight_sel_up_smoothing_nonstbc_wide_msb = 22
        self.__reg_weight_sel_up_smoothing_nonstbc_narrow_lsb = 16
        self.__reg_weight_sel_up_smoothing_nonstbc_narrow_msb = 18
        self.__reg_weight_sel_up_nonsmoothing_stbc_lsb = 12
        self.__reg_weight_sel_up_nonsmoothing_stbc_msb = 14
        self.__reg_weight_sel_up_nonsmoothing_nonstbc_lsb = 8
        self.__reg_weight_sel_up_nonsmoothing_nonstbc_msb = 10
        self.__reg_weight_sel_up_xsmoothing_lsb = 4
        self.__reg_weight_sel_up_xsmoothing_msb = 6
        self.__reg_weight_sel_up_force_lsb = 0
        self.__reg_weight_sel_up_force_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_weight_sel_up_smoothing_stbc_wide(self):
        return self.__MEM.rdm(self.__addr, self.__reg_weight_sel_up_smoothing_stbc_wide_msb, self.__reg_weight_sel_up_smoothing_stbc_wide_lsb)
    @reg_weight_sel_up_smoothing_stbc_wide.setter
    def reg_weight_sel_up_smoothing_stbc_wide(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_weight_sel_up_smoothing_stbc_wide_msb, self.__reg_weight_sel_up_smoothing_stbc_wide_lsb, value)

    @property
    def reg_weight_sel_up_smoothing_stbc_narrow(self):
        return self.__MEM.rdm(self.__addr, self.__reg_weight_sel_up_smoothing_stbc_narrow_msb, self.__reg_weight_sel_up_smoothing_stbc_narrow_lsb)
    @reg_weight_sel_up_smoothing_stbc_narrow.setter
    def reg_weight_sel_up_smoothing_stbc_narrow(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_weight_sel_up_smoothing_stbc_narrow_msb, self.__reg_weight_sel_up_smoothing_stbc_narrow_lsb, value)

    @property
    def reg_weight_sel_up_smoothing_nonstbc_wide(self):
        return self.__MEM.rdm(self.__addr, self.__reg_weight_sel_up_smoothing_nonstbc_wide_msb, self.__reg_weight_sel_up_smoothing_nonstbc_wide_lsb)
    @reg_weight_sel_up_smoothing_nonstbc_wide.setter
    def reg_weight_sel_up_smoothing_nonstbc_wide(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_weight_sel_up_smoothing_nonstbc_wide_msb, self.__reg_weight_sel_up_smoothing_nonstbc_wide_lsb, value)

    @property
    def reg_weight_sel_up_smoothing_nonstbc_narrow(self):
        return self.__MEM.rdm(self.__addr, self.__reg_weight_sel_up_smoothing_nonstbc_narrow_msb, self.__reg_weight_sel_up_smoothing_nonstbc_narrow_lsb)
    @reg_weight_sel_up_smoothing_nonstbc_narrow.setter
    def reg_weight_sel_up_smoothing_nonstbc_narrow(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_weight_sel_up_smoothing_nonstbc_narrow_msb, self.__reg_weight_sel_up_smoothing_nonstbc_narrow_lsb, value)

    @property
    def reg_weight_sel_up_nonsmoothing_stbc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_weight_sel_up_nonsmoothing_stbc_msb, self.__reg_weight_sel_up_nonsmoothing_stbc_lsb)
    @reg_weight_sel_up_nonsmoothing_stbc.setter
    def reg_weight_sel_up_nonsmoothing_stbc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_weight_sel_up_nonsmoothing_stbc_msb, self.__reg_weight_sel_up_nonsmoothing_stbc_lsb, value)

    @property
    def reg_weight_sel_up_nonsmoothing_nonstbc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_weight_sel_up_nonsmoothing_nonstbc_msb, self.__reg_weight_sel_up_nonsmoothing_nonstbc_lsb)
    @reg_weight_sel_up_nonsmoothing_nonstbc.setter
    def reg_weight_sel_up_nonsmoothing_nonstbc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_weight_sel_up_nonsmoothing_nonstbc_msb, self.__reg_weight_sel_up_nonsmoothing_nonstbc_lsb, value)

    @property
    def reg_weight_sel_up_xsmoothing(self):
        return self.__MEM.rdm(self.__addr, self.__reg_weight_sel_up_xsmoothing_msb, self.__reg_weight_sel_up_xsmoothing_lsb)
    @reg_weight_sel_up_xsmoothing.setter
    def reg_weight_sel_up_xsmoothing(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_weight_sel_up_xsmoothing_msb, self.__reg_weight_sel_up_xsmoothing_lsb, value)

    @property
    def reg_weight_sel_up_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_weight_sel_up_force_msb, self.__reg_weight_sel_up_force_lsb)
    @reg_weight_sel_up_force.setter
    def reg_weight_sel_up_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_weight_sel_up_force_msb, self.__reg_weight_sel_up_force_lsb, value)
class NRXCHANDUMP(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x10c
        self.__reg_chan_dump_bypass_test_lsb = 11
        self.__reg_chan_dump_bypass_test_msb = 11
        self.__reg_chan_fft_out_dump_en_lsb = 10
        self.__reg_chan_fft_out_dump_en_msb = 10
        self.__reg_fte_offset_non_avg_en_lsb = 9
        self.__reg_fte_offset_non_avg_en_msb = 9
        self.__reg_fft_htltf_start_pos_pulse_en_lsb = 8
        self.__reg_fft_htltf_start_pos_pulse_en_msb = 8
        self.__reg_chan_dump_shift_force_lsb = 4
        self.__reg_chan_dump_shift_force_msb = 7
        self.__reg_chan_dump_shift_force_en_lsb = 3
        self.__reg_chan_dump_shift_force_en_msb = 3
        self.__reg_chan_stbcltf2_dump_en_lsb = 2
        self.__reg_chan_stbcltf2_dump_en_msb = 2
        self.__reg_chan_lltf_dump_en_lsb = 1
        self.__reg_chan_lltf_dump_en_msb = 1
        self.__reg_chan_htltf_dump_en_lsb = 0
        self.__reg_chan_htltf_dump_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_chan_dump_bypass_test(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_dump_bypass_test_msb, self.__reg_chan_dump_bypass_test_lsb)
    @reg_chan_dump_bypass_test.setter
    def reg_chan_dump_bypass_test(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_dump_bypass_test_msb, self.__reg_chan_dump_bypass_test_lsb, value)

    @property
    def reg_chan_fft_out_dump_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_fft_out_dump_en_msb, self.__reg_chan_fft_out_dump_en_lsb)
    @reg_chan_fft_out_dump_en.setter
    def reg_chan_fft_out_dump_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_fft_out_dump_en_msb, self.__reg_chan_fft_out_dump_en_lsb, value)

    @property
    def reg_fte_offset_non_avg_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fte_offset_non_avg_en_msb, self.__reg_fte_offset_non_avg_en_lsb)
    @reg_fte_offset_non_avg_en.setter
    def reg_fte_offset_non_avg_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fte_offset_non_avg_en_msb, self.__reg_fte_offset_non_avg_en_lsb, value)

    @property
    def reg_fft_htltf_start_pos_pulse_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fft_htltf_start_pos_pulse_en_msb, self.__reg_fft_htltf_start_pos_pulse_en_lsb)
    @reg_fft_htltf_start_pos_pulse_en.setter
    def reg_fft_htltf_start_pos_pulse_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fft_htltf_start_pos_pulse_en_msb, self.__reg_fft_htltf_start_pos_pulse_en_lsb, value)

    @property
    def reg_chan_dump_shift_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_dump_shift_force_msb, self.__reg_chan_dump_shift_force_lsb)
    @reg_chan_dump_shift_force.setter
    def reg_chan_dump_shift_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_dump_shift_force_msb, self.__reg_chan_dump_shift_force_lsb, value)

    @property
    def reg_chan_dump_shift_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_dump_shift_force_en_msb, self.__reg_chan_dump_shift_force_en_lsb)
    @reg_chan_dump_shift_force_en.setter
    def reg_chan_dump_shift_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_dump_shift_force_en_msb, self.__reg_chan_dump_shift_force_en_lsb, value)

    @property
    def reg_chan_stbcltf2_dump_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_stbcltf2_dump_en_msb, self.__reg_chan_stbcltf2_dump_en_lsb)
    @reg_chan_stbcltf2_dump_en.setter
    def reg_chan_stbcltf2_dump_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_stbcltf2_dump_en_msb, self.__reg_chan_stbcltf2_dump_en_lsb, value)

    @property
    def reg_chan_lltf_dump_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_lltf_dump_en_msb, self.__reg_chan_lltf_dump_en_lsb)
    @reg_chan_lltf_dump_en.setter
    def reg_chan_lltf_dump_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_lltf_dump_en_msb, self.__reg_chan_lltf_dump_en_lsb, value)

    @property
    def reg_chan_htltf_dump_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_htltf_dump_en_msb, self.__reg_chan_htltf_dump_en_lsb)
    @reg_chan_htltf_dump_en.setter
    def reg_chan_htltf_dump_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_htltf_dump_en_msb, self.__reg_chan_htltf_dump_en_lsb, value)
class NRXSIMDUG0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x110
        self.__reg_rxstart_time_cycle_lsb = 0
        self.__reg_rxstart_time_cycle_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxstart_time_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxstart_time_cycle_msb, self.__reg_rxstart_time_cycle_lsb)
    @reg_rxstart_time_cycle.setter
    def reg_rxstart_time_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxstart_time_cycle_msb, self.__reg_rxstart_time_cycle_lsb, value)
class NRXFFTSCALE(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x114
        self.__reg_modu_scale_en_lsb = 9
        self.__reg_modu_scale_en_msb = 9
        self.__reg_modu_snr_thr_en_lsb = 8
        self.__reg_modu_snr_thr_en_msb = 8
        self.__reg_fft_scale_lsb = 0
        self.__reg_fft_scale_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_modu_scale_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_modu_scale_en_msb, self.__reg_modu_scale_en_lsb)
    @reg_modu_scale_en.setter
    def reg_modu_scale_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_modu_scale_en_msb, self.__reg_modu_scale_en_lsb, value)

    @property
    def reg_modu_snr_thr_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_modu_snr_thr_en_msb, self.__reg_modu_snr_thr_en_lsb)
    @reg_modu_snr_thr_en.setter
    def reg_modu_snr_thr_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_modu_snr_thr_en_msb, self.__reg_modu_snr_thr_en_lsb, value)

    @property
    def reg_fft_scale(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fft_scale_msb, self.__reg_fft_scale_lsb)
    @reg_fft_scale.setter
    def reg_fft_scale(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fft_scale_msb, self.__reg_fft_scale_lsb, value)
class NRXSNRDEMAPTHR(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x118
        self.__reg_snr_64qam_thr_lsb = 24
        self.__reg_snr_64qam_thr_msb = 31
        self.__reg_snr_16qam_thr_lsb = 16
        self.__reg_snr_16qam_thr_msb = 23
        self.__reg_snr_qpsk_thr_lsb = 8
        self.__reg_snr_qpsk_thr_msb = 15
        self.__reg_snr_bpsk_thr_lsb = 0
        self.__reg_snr_bpsk_thr_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_snr_64qam_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_snr_64qam_thr_msb, self.__reg_snr_64qam_thr_lsb)
    @reg_snr_64qam_thr.setter
    def reg_snr_64qam_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_snr_64qam_thr_msb, self.__reg_snr_64qam_thr_lsb, value)

    @property
    def reg_snr_16qam_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_snr_16qam_thr_msb, self.__reg_snr_16qam_thr_lsb)
    @reg_snr_16qam_thr.setter
    def reg_snr_16qam_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_snr_16qam_thr_msb, self.__reg_snr_16qam_thr_lsb, value)

    @property
    def reg_snr_qpsk_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_snr_qpsk_thr_msb, self.__reg_snr_qpsk_thr_lsb)
    @reg_snr_qpsk_thr.setter
    def reg_snr_qpsk_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_snr_qpsk_thr_msb, self.__reg_snr_qpsk_thr_lsb, value)

    @property
    def reg_snr_bpsk_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_snr_bpsk_thr_msb, self.__reg_snr_bpsk_thr_lsb)
    @reg_snr_bpsk_thr.setter
    def reg_snr_bpsk_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_snr_bpsk_thr_msb, self.__reg_snr_bpsk_thr_lsb, value)
class NRXSOFTBITWIGHT(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x11c
        self.__reg_bit_wight_shift_en_lsb = 6
        self.__reg_bit_wight_shift_en_msb = 6
        self.__reg_bit2_wight_shift_lsb = 4
        self.__reg_bit2_wight_shift_msb = 5
        self.__reg_bit1_wight_shift_lsb = 2
        self.__reg_bit1_wight_shift_msb = 3
        self.__reg_bit0_wight_shift_lsb = 0
        self.__reg_bit0_wight_shift_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bit_wight_shift_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bit_wight_shift_en_msb, self.__reg_bit_wight_shift_en_lsb)
    @reg_bit_wight_shift_en.setter
    def reg_bit_wight_shift_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bit_wight_shift_en_msb, self.__reg_bit_wight_shift_en_lsb, value)

    @property
    def reg_bit2_wight_shift(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bit2_wight_shift_msb, self.__reg_bit2_wight_shift_lsb)
    @reg_bit2_wight_shift.setter
    def reg_bit2_wight_shift(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bit2_wight_shift_msb, self.__reg_bit2_wight_shift_lsb, value)

    @property
    def reg_bit1_wight_shift(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bit1_wight_shift_msb, self.__reg_bit1_wight_shift_lsb)
    @reg_bit1_wight_shift.setter
    def reg_bit1_wight_shift(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bit1_wight_shift_msb, self.__reg_bit1_wight_shift_lsb, value)

    @property
    def reg_bit0_wight_shift(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bit0_wight_shift_msb, self.__reg_bit0_wight_shift_lsb)
    @reg_bit0_wight_shift.setter
    def reg_bit0_wight_shift(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bit0_wight_shift_msb, self.__reg_bit0_wight_shift_lsb, value)
class NRXCHANSELTHR0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x120
        self.__reg_chan_sel_awgn_lsb = 25
        self.__reg_chan_sel_awgn_msb = 27
        self.__reg_ceupdate_mcs0_4_en_lsb = 24
        self.__reg_ceupdate_mcs0_4_en_msb = 24
        self.__reg_ceupdate_mcs0_4_snr_thr_lsb = 16
        self.__reg_ceupdate_mcs0_4_snr_thr_msb = 23
        self.__reg_chan_sel_awgn_thr_lsb = 0
        self.__reg_chan_sel_awgn_thr_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_chan_sel_awgn(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_sel_awgn_msb, self.__reg_chan_sel_awgn_lsb)
    @reg_chan_sel_awgn.setter
    def reg_chan_sel_awgn(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_sel_awgn_msb, self.__reg_chan_sel_awgn_lsb, value)

    @property
    def reg_ceupdate_mcs0_4_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ceupdate_mcs0_4_en_msb, self.__reg_ceupdate_mcs0_4_en_lsb)
    @reg_ceupdate_mcs0_4_en.setter
    def reg_ceupdate_mcs0_4_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ceupdate_mcs0_4_en_msb, self.__reg_ceupdate_mcs0_4_en_lsb, value)

    @property
    def reg_ceupdate_mcs0_4_snr_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ceupdate_mcs0_4_snr_thr_msb, self.__reg_ceupdate_mcs0_4_snr_thr_lsb)
    @reg_ceupdate_mcs0_4_snr_thr.setter
    def reg_ceupdate_mcs0_4_snr_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ceupdate_mcs0_4_snr_thr_msb, self.__reg_ceupdate_mcs0_4_snr_thr_lsb, value)

    @property
    def reg_chan_sel_awgn_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_sel_awgn_thr_msb, self.__reg_chan_sel_awgn_thr_lsb)
    @reg_chan_sel_awgn_thr.setter
    def reg_chan_sel_awgn_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_sel_awgn_thr_msb, self.__reg_chan_sel_awgn_thr_lsb, value)
class NRXTDM4(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x124
        self.__reg_cte_dly_lsb = 8
        self.__reg_cte_dly_msb = 11
        self.__reg_agc_xcorr_start_lsb = 0
        self.__reg_agc_xcorr_start_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_cte_dly(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cte_dly_msb, self.__reg_cte_dly_lsb)
    @reg_cte_dly.setter
    def reg_cte_dly(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cte_dly_msb, self.__reg_cte_dly_lsb, value)

    @property
    def reg_agc_xcorr_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_xcorr_start_msb, self.__reg_agc_xcorr_start_lsb)
    @reg_agc_xcorr_start.setter
    def reg_agc_xcorr_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_xcorr_start_msb, self.__reg_agc_xcorr_start_lsb, value)
class NRXFOEHTRANGE(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x128
        self.__reg_foe_htstf_on_lsb = 16
        self.__reg_foe_htstf_on_msb = 16
        self.__reg_foe_htstf_end_lsb = 8
        self.__reg_foe_htstf_end_msb = 15
        self.__reg_foe_htstf_start_lsb = 0
        self.__reg_foe_htstf_start_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_foe_htstf_on(self):
        return self.__MEM.rdm(self.__addr, self.__reg_foe_htstf_on_msb, self.__reg_foe_htstf_on_lsb)
    @reg_foe_htstf_on.setter
    def reg_foe_htstf_on(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_foe_htstf_on_msb, self.__reg_foe_htstf_on_lsb, value)

    @property
    def reg_foe_htstf_end(self):
        return self.__MEM.rdm(self.__addr, self.__reg_foe_htstf_end_msb, self.__reg_foe_htstf_end_lsb)
    @reg_foe_htstf_end.setter
    def reg_foe_htstf_end(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_foe_htstf_end_msb, self.__reg_foe_htstf_end_lsb, value)

    @property
    def reg_foe_htstf_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_foe_htstf_start_msb, self.__reg_foe_htstf_start_lsb)
    @reg_foe_htstf_start.setter
    def reg_foe_htstf_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_foe_htstf_start_msb, self.__reg_foe_htstf_start_lsb, value)
class NRXMODUSCALESTBC0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x12c
        self.__reg_mcs3_scale_stbc_lsb = 24
        self.__reg_mcs3_scale_stbc_msb = 31
        self.__reg_mcs2_scale_stbc_lsb = 16
        self.__reg_mcs2_scale_stbc_msb = 23
        self.__reg_mcs1_scale_stbc_lsb = 8
        self.__reg_mcs1_scale_stbc_msb = 15
        self.__reg_mcs0_scale_stbc_lsb = 0
        self.__reg_mcs0_scale_stbc_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_mcs3_scale_stbc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mcs3_scale_stbc_msb, self.__reg_mcs3_scale_stbc_lsb)
    @reg_mcs3_scale_stbc.setter
    def reg_mcs3_scale_stbc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mcs3_scale_stbc_msb, self.__reg_mcs3_scale_stbc_lsb, value)

    @property
    def reg_mcs2_scale_stbc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mcs2_scale_stbc_msb, self.__reg_mcs2_scale_stbc_lsb)
    @reg_mcs2_scale_stbc.setter
    def reg_mcs2_scale_stbc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mcs2_scale_stbc_msb, self.__reg_mcs2_scale_stbc_lsb, value)

    @property
    def reg_mcs1_scale_stbc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mcs1_scale_stbc_msb, self.__reg_mcs1_scale_stbc_lsb)
    @reg_mcs1_scale_stbc.setter
    def reg_mcs1_scale_stbc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mcs1_scale_stbc_msb, self.__reg_mcs1_scale_stbc_lsb, value)

    @property
    def reg_mcs0_scale_stbc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mcs0_scale_stbc_msb, self.__reg_mcs0_scale_stbc_lsb)
    @reg_mcs0_scale_stbc.setter
    def reg_mcs0_scale_stbc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mcs0_scale_stbc_msb, self.__reg_mcs0_scale_stbc_lsb, value)
class NRXMODUSCALESTBC1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x130
        self.__reg_mcs7_scale_stbc_lsb = 24
        self.__reg_mcs7_scale_stbc_msb = 31
        self.__reg_mcs6_scale_stbc_lsb = 16
        self.__reg_mcs6_scale_stbc_msb = 23
        self.__reg_mcs5_scale_stbc_lsb = 8
        self.__reg_mcs5_scale_stbc_msb = 15
        self.__reg_mcs4_scale_stbc_lsb = 0
        self.__reg_mcs4_scale_stbc_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_mcs7_scale_stbc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mcs7_scale_stbc_msb, self.__reg_mcs7_scale_stbc_lsb)
    @reg_mcs7_scale_stbc.setter
    def reg_mcs7_scale_stbc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mcs7_scale_stbc_msb, self.__reg_mcs7_scale_stbc_lsb, value)

    @property
    def reg_mcs6_scale_stbc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mcs6_scale_stbc_msb, self.__reg_mcs6_scale_stbc_lsb)
    @reg_mcs6_scale_stbc.setter
    def reg_mcs6_scale_stbc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mcs6_scale_stbc_msb, self.__reg_mcs6_scale_stbc_lsb, value)

    @property
    def reg_mcs5_scale_stbc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mcs5_scale_stbc_msb, self.__reg_mcs5_scale_stbc_lsb)
    @reg_mcs5_scale_stbc.setter
    def reg_mcs5_scale_stbc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mcs5_scale_stbc_msb, self.__reg_mcs5_scale_stbc_lsb, value)

    @property
    def reg_mcs4_scale_stbc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mcs4_scale_stbc_msb, self.__reg_mcs4_scale_stbc_lsb)
    @reg_mcs4_scale_stbc.setter
    def reg_mcs4_scale_stbc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mcs4_scale_stbc_msb, self.__reg_mcs4_scale_stbc_lsb, value)
class NRXMODUSCALEAWGN1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x134
        self.__reg_mcs7_scale_lsb = 24
        self.__reg_mcs7_scale_msb = 31
        self.__reg_mcs6_scale_lsb = 16
        self.__reg_mcs6_scale_msb = 23
        self.__reg_mcs5_scale_lsb = 8
        self.__reg_mcs5_scale_msb = 15
        self.__reg_mcs4_scale_lsb = 0
        self.__reg_mcs4_scale_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_mcs7_scale(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mcs7_scale_msb, self.__reg_mcs7_scale_lsb)
    @reg_mcs7_scale.setter
    def reg_mcs7_scale(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mcs7_scale_msb, self.__reg_mcs7_scale_lsb, value)

    @property
    def reg_mcs6_scale(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mcs6_scale_msb, self.__reg_mcs6_scale_lsb)
    @reg_mcs6_scale.setter
    def reg_mcs6_scale(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mcs6_scale_msb, self.__reg_mcs6_scale_lsb, value)

    @property
    def reg_mcs5_scale(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mcs5_scale_msb, self.__reg_mcs5_scale_lsb)
    @reg_mcs5_scale.setter
    def reg_mcs5_scale(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mcs5_scale_msb, self.__reg_mcs5_scale_lsb, value)

    @property
    def reg_mcs4_scale(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mcs4_scale_msb, self.__reg_mcs4_scale_lsb)
    @reg_mcs4_scale.setter
    def reg_mcs4_scale(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mcs4_scale_msb, self.__reg_mcs4_scale_lsb, value)
class NRXMODUSCALEMP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x138
        self.__reg_mcs3_scale_mp_lsb = 24
        self.__reg_mcs3_scale_mp_msb = 31
        self.__reg_mcs2_scale_mp_lsb = 16
        self.__reg_mcs2_scale_mp_msb = 23
        self.__reg_mcs1_scale_mp_lsb = 8
        self.__reg_mcs1_scale_mp_msb = 15
        self.__reg_mcs0_scale_mp_lsb = 0
        self.__reg_mcs0_scale_mp_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_mcs3_scale_mp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mcs3_scale_mp_msb, self.__reg_mcs3_scale_mp_lsb)
    @reg_mcs3_scale_mp.setter
    def reg_mcs3_scale_mp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mcs3_scale_mp_msb, self.__reg_mcs3_scale_mp_lsb, value)

    @property
    def reg_mcs2_scale_mp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mcs2_scale_mp_msb, self.__reg_mcs2_scale_mp_lsb)
    @reg_mcs2_scale_mp.setter
    def reg_mcs2_scale_mp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mcs2_scale_mp_msb, self.__reg_mcs2_scale_mp_lsb, value)

    @property
    def reg_mcs1_scale_mp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mcs1_scale_mp_msb, self.__reg_mcs1_scale_mp_lsb)
    @reg_mcs1_scale_mp.setter
    def reg_mcs1_scale_mp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mcs1_scale_mp_msb, self.__reg_mcs1_scale_mp_lsb, value)

    @property
    def reg_mcs0_scale_mp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mcs0_scale_mp_msb, self.__reg_mcs0_scale_mp_lsb)
    @reg_mcs0_scale_mp.setter
    def reg_mcs0_scale_mp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mcs0_scale_mp_msb, self.__reg_mcs0_scale_mp_lsb, value)
class NRXMODUSCALEMP1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x13c
        self.__reg_mcs7_scale_mp_lsb = 24
        self.__reg_mcs7_scale_mp_msb = 31
        self.__reg_mcs6_scale_mp_lsb = 16
        self.__reg_mcs6_scale_mp_msb = 23
        self.__reg_mcs5_scale_mp_lsb = 8
        self.__reg_mcs5_scale_mp_msb = 15
        self.__reg_mcs4_scale_mp_lsb = 0
        self.__reg_mcs4_scale_mp_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_mcs7_scale_mp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mcs7_scale_mp_msb, self.__reg_mcs7_scale_mp_lsb)
    @reg_mcs7_scale_mp.setter
    def reg_mcs7_scale_mp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mcs7_scale_mp_msb, self.__reg_mcs7_scale_mp_lsb, value)

    @property
    def reg_mcs6_scale_mp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mcs6_scale_mp_msb, self.__reg_mcs6_scale_mp_lsb)
    @reg_mcs6_scale_mp.setter
    def reg_mcs6_scale_mp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mcs6_scale_mp_msb, self.__reg_mcs6_scale_mp_lsb, value)

    @property
    def reg_mcs5_scale_mp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mcs5_scale_mp_msb, self.__reg_mcs5_scale_mp_lsb)
    @reg_mcs5_scale_mp.setter
    def reg_mcs5_scale_mp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mcs5_scale_mp_msb, self.__reg_mcs5_scale_mp_lsb, value)

    @property
    def reg_mcs4_scale_mp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mcs4_scale_mp_msb, self.__reg_mcs4_scale_mp_lsb)
    @reg_mcs4_scale_mp.setter
    def reg_mcs4_scale_mp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mcs4_scale_mp_msb, self.__reg_mcs4_scale_mp_lsb, value)
class NRXPOWMARGINSEL(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x140
        self.__reg_powmargin_awgn_mp_sel_force_lsb = 17
        self.__reg_powmargin_awgn_mp_sel_force_msb = 17
        self.__reg_powmargin_awgn_mp_sel_force_en_lsb = 16
        self.__reg_powmargin_awgn_mp_sel_force_en_msb = 16
        self.__reg_powmargin_sel_awgn_rssi_thr_lsb = 8
        self.__reg_powmargin_sel_awgn_rssi_thr_msb = 15
        self.__reg_powmargin_sel_awgn_delta_thr_lsb = 0
        self.__reg_powmargin_sel_awgn_delta_thr_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_powmargin_awgn_mp_sel_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_powmargin_awgn_mp_sel_force_msb, self.__reg_powmargin_awgn_mp_sel_force_lsb)
    @reg_powmargin_awgn_mp_sel_force.setter
    def reg_powmargin_awgn_mp_sel_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_powmargin_awgn_mp_sel_force_msb, self.__reg_powmargin_awgn_mp_sel_force_lsb, value)

    @property
    def reg_powmargin_awgn_mp_sel_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_powmargin_awgn_mp_sel_force_en_msb, self.__reg_powmargin_awgn_mp_sel_force_en_lsb)
    @reg_powmargin_awgn_mp_sel_force_en.setter
    def reg_powmargin_awgn_mp_sel_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_powmargin_awgn_mp_sel_force_en_msb, self.__reg_powmargin_awgn_mp_sel_force_en_lsb, value)

    @property
    def reg_powmargin_sel_awgn_rssi_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_powmargin_sel_awgn_rssi_thr_msb, self.__reg_powmargin_sel_awgn_rssi_thr_lsb)
    @reg_powmargin_sel_awgn_rssi_thr.setter
    def reg_powmargin_sel_awgn_rssi_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_powmargin_sel_awgn_rssi_thr_msb, self.__reg_powmargin_sel_awgn_rssi_thr_lsb, value)

    @property
    def reg_powmargin_sel_awgn_delta_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_powmargin_sel_awgn_delta_thr_msb, self.__reg_powmargin_sel_awgn_delta_thr_lsb)
    @reg_powmargin_sel_awgn_delta_thr.setter
    def reg_powmargin_sel_awgn_delta_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_powmargin_sel_awgn_delta_thr_msb, self.__reg_powmargin_sel_awgn_delta_thr_lsb, value)
class NRXFTM_CFG(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x144
        self.__reg_ftm_cal_en_lsb = 30
        self.__reg_ftm_cal_en_msb = 30
        self.__reg_ftm_cnt_max3_lsb = 20
        self.__reg_ftm_cnt_max3_msb = 29
        self.__reg_ftm_cnt_max2_lsb = 10
        self.__reg_ftm_cnt_max2_msb = 19
        self.__reg_ftm_cnt_max1_lsb = 0
        self.__reg_ftm_cnt_max1_msb = 9
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ftm_cal_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ftm_cal_en_msb, self.__reg_ftm_cal_en_lsb)
    @reg_ftm_cal_en.setter
    def reg_ftm_cal_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ftm_cal_en_msb, self.__reg_ftm_cal_en_lsb, value)

    @property
    def reg_ftm_cnt_max3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ftm_cnt_max3_msb, self.__reg_ftm_cnt_max3_lsb)
    @reg_ftm_cnt_max3.setter
    def reg_ftm_cnt_max3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ftm_cnt_max3_msb, self.__reg_ftm_cnt_max3_lsb, value)

    @property
    def reg_ftm_cnt_max2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ftm_cnt_max2_msb, self.__reg_ftm_cnt_max2_lsb)
    @reg_ftm_cnt_max2.setter
    def reg_ftm_cnt_max2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ftm_cnt_max2_msb, self.__reg_ftm_cnt_max2_lsb, value)

    @property
    def reg_ftm_cnt_max1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ftm_cnt_max1_msb, self.__reg_ftm_cnt_max1_lsb)
    @reg_ftm_cnt_max1.setter
    def reg_ftm_cnt_max1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ftm_cnt_max1_msb, self.__reg_ftm_cnt_max1_lsb, value)
class NRXFTM_CFG2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x148
        self.__reg_ftm_cnt_mask3_lsb = 20
        self.__reg_ftm_cnt_mask3_msb = 29
        self.__reg_ftm_cnt_mask2_lsb = 10
        self.__reg_ftm_cnt_mask2_msb = 19
        self.__reg_ftm_cnt_mask1_lsb = 0
        self.__reg_ftm_cnt_mask1_msb = 9
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ftm_cnt_mask3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ftm_cnt_mask3_msb, self.__reg_ftm_cnt_mask3_lsb)
    @reg_ftm_cnt_mask3.setter
    def reg_ftm_cnt_mask3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ftm_cnt_mask3_msb, self.__reg_ftm_cnt_mask3_lsb, value)

    @property
    def reg_ftm_cnt_mask2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ftm_cnt_mask2_msb, self.__reg_ftm_cnt_mask2_lsb)
    @reg_ftm_cnt_mask2.setter
    def reg_ftm_cnt_mask2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ftm_cnt_mask2_msb, self.__reg_ftm_cnt_mask2_lsb, value)

    @property
    def reg_ftm_cnt_mask1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ftm_cnt_mask1_msb, self.__reg_ftm_cnt_mask1_lsb)
    @reg_ftm_cnt_mask1.setter
    def reg_ftm_cnt_mask1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ftm_cnt_mask1_msb, self.__reg_ftm_cnt_mask1_lsb, value)
class NRXCHANSELTHR1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x14c
        self.__reg_chan_filter_off_thr_nonstbc_lsb = 8
        self.__reg_chan_filter_off_thr_nonstbc_msb = 15
        self.__reg_chan_filter_off_thr_stbc_lsb = 0
        self.__reg_chan_filter_off_thr_stbc_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_chan_filter_off_thr_nonstbc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_filter_off_thr_nonstbc_msb, self.__reg_chan_filter_off_thr_nonstbc_lsb)
    @reg_chan_filter_off_thr_nonstbc.setter
    def reg_chan_filter_off_thr_nonstbc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_filter_off_thr_nonstbc_msb, self.__reg_chan_filter_off_thr_nonstbc_lsb, value)

    @property
    def reg_chan_filter_off_thr_stbc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_filter_off_thr_stbc_msb, self.__reg_chan_filter_off_thr_stbc_lsb)
    @reg_chan_filter_off_thr_stbc.setter
    def reg_chan_filter_off_thr_stbc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_filter_off_thr_stbc_msb, self.__reg_chan_filter_off_thr_stbc_lsb, value)
class NRXPILOTCONF12(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x150
        self.__reg_a1_shift6_lsb = 20
        self.__reg_a1_shift6_msb = 22
        self.__reg_a1_shift5_lsb = 16
        self.__reg_a1_shift5_msb = 18
        self.__reg_a1_shift4_lsb = 12
        self.__reg_a1_shift4_msb = 14
        self.__reg_a1_shift3_lsb = 8
        self.__reg_a1_shift3_msb = 10
        self.__reg_a1_shift2_lsb = 4
        self.__reg_a1_shift2_msb = 6
        self.__reg_a1_shift1_lsb = 0
        self.__reg_a1_shift1_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_a1_shift6(self):
        return self.__MEM.rdm(self.__addr, self.__reg_a1_shift6_msb, self.__reg_a1_shift6_lsb)
    @reg_a1_shift6.setter
    def reg_a1_shift6(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_a1_shift6_msb, self.__reg_a1_shift6_lsb, value)

    @property
    def reg_a1_shift5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_a1_shift5_msb, self.__reg_a1_shift5_lsb)
    @reg_a1_shift5.setter
    def reg_a1_shift5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_a1_shift5_msb, self.__reg_a1_shift5_lsb, value)

    @property
    def reg_a1_shift4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_a1_shift4_msb, self.__reg_a1_shift4_lsb)
    @reg_a1_shift4.setter
    def reg_a1_shift4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_a1_shift4_msb, self.__reg_a1_shift4_lsb, value)

    @property
    def reg_a1_shift3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_a1_shift3_msb, self.__reg_a1_shift3_lsb)
    @reg_a1_shift3.setter
    def reg_a1_shift3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_a1_shift3_msb, self.__reg_a1_shift3_lsb, value)

    @property
    def reg_a1_shift2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_a1_shift2_msb, self.__reg_a1_shift2_lsb)
    @reg_a1_shift2.setter
    def reg_a1_shift2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_a1_shift2_msb, self.__reg_a1_shift2_lsb, value)

    @property
    def reg_a1_shift1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_a1_shift1_msb, self.__reg_a1_shift1_lsb)
    @reg_a1_shift1.setter
    def reg_a1_shift1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_a1_shift1_msb, self.__reg_a1_shift1_lsb, value)
class NRXPILOTCONF13(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x154
        self.__reg_a2_shift6_lsb = 20
        self.__reg_a2_shift6_msb = 22
        self.__reg_a2_shift5_lsb = 16
        self.__reg_a2_shift5_msb = 18
        self.__reg_a2_shift4_lsb = 12
        self.__reg_a2_shift4_msb = 14
        self.__reg_a2_shift3_lsb = 8
        self.__reg_a2_shift3_msb = 10
        self.__reg_a2_shift2_lsb = 4
        self.__reg_a2_shift2_msb = 6
        self.__reg_a2_shift1_lsb = 0
        self.__reg_a2_shift1_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_a2_shift6(self):
        return self.__MEM.rdm(self.__addr, self.__reg_a2_shift6_msb, self.__reg_a2_shift6_lsb)
    @reg_a2_shift6.setter
    def reg_a2_shift6(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_a2_shift6_msb, self.__reg_a2_shift6_lsb, value)

    @property
    def reg_a2_shift5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_a2_shift5_msb, self.__reg_a2_shift5_lsb)
    @reg_a2_shift5.setter
    def reg_a2_shift5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_a2_shift5_msb, self.__reg_a2_shift5_lsb, value)

    @property
    def reg_a2_shift4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_a2_shift4_msb, self.__reg_a2_shift4_lsb)
    @reg_a2_shift4.setter
    def reg_a2_shift4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_a2_shift4_msb, self.__reg_a2_shift4_lsb, value)

    @property
    def reg_a2_shift3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_a2_shift3_msb, self.__reg_a2_shift3_lsb)
    @reg_a2_shift3.setter
    def reg_a2_shift3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_a2_shift3_msb, self.__reg_a2_shift3_lsb, value)

    @property
    def reg_a2_shift2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_a2_shift2_msb, self.__reg_a2_shift2_lsb)
    @reg_a2_shift2.setter
    def reg_a2_shift2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_a2_shift2_msb, self.__reg_a2_shift2_lsb, value)

    @property
    def reg_a2_shift1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_a2_shift1_msb, self.__reg_a2_shift1_lsb)
    @reg_a2_shift1.setter
    def reg_a2_shift1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_a2_shift1_msb, self.__reg_a2_shift1_lsb, value)
class NRXPILOTCONF14(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x158
        self.__reg_sym_max_num2_lsb = 16
        self.__reg_sym_max_num2_msb = 31
        self.__reg_sym_max_num1_lsb = 0
        self.__reg_sym_max_num1_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sym_max_num2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sym_max_num2_msb, self.__reg_sym_max_num2_lsb)
    @reg_sym_max_num2.setter
    def reg_sym_max_num2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sym_max_num2_msb, self.__reg_sym_max_num2_lsb, value)

    @property
    def reg_sym_max_num1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sym_max_num1_msb, self.__reg_sym_max_num1_lsb)
    @reg_sym_max_num1.setter
    def reg_sym_max_num1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sym_max_num1_msb, self.__reg_sym_max_num1_lsb, value)
class NRXPILOTCONF15(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x15c
        self.__reg_sym_max_num4_lsb = 16
        self.__reg_sym_max_num4_msb = 31
        self.__reg_sym_max_num3_lsb = 0
        self.__reg_sym_max_num3_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sym_max_num4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sym_max_num4_msb, self.__reg_sym_max_num4_lsb)
    @reg_sym_max_num4.setter
    def reg_sym_max_num4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sym_max_num4_msb, self.__reg_sym_max_num4_lsb, value)

    @property
    def reg_sym_max_num3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sym_max_num3_msb, self.__reg_sym_max_num3_lsb)
    @reg_sym_max_num3.setter
    def reg_sym_max_num3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sym_max_num3_msb, self.__reg_sym_max_num3_lsb, value)
class NRXSIMDUG1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x3f8
        self.__reg_rxstart_time_lsb = 0
        self.__reg_rxstart_time_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxstart_time(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxstart_time_msb, self.__reg_rxstart_time_lsb)
    @reg_rxstart_time.setter
    def reg_rxstart_time(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxstart_time_msb, self.__reg_rxstart_time_lsb, value)
class NRXDATE(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = NRX_BASE + 0x3fc
        self.__reg_nrx_date_lsb = 0
        self.__reg_nrx_date_msb = 27
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_nrx_date(self):
        return self.__MEM.rdm(self.__addr, self.__reg_nrx_date_msb, self.__reg_nrx_date_lsb)
    @reg_nrx_date.setter
    def reg_nrx_date(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_nrx_date_msb, self.__reg_nrx_date_lsb, value)
    @property
    def default_value(self):
        return 0x1912031
