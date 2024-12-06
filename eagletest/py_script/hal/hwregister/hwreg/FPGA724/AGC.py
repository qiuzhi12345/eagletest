from hal.common import *
from hal.hwregister.hwreg.FPGA724.addr_base import *
class AGC(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.AGCDC_CTRL1 = AGCDC_CTRL1(self.channel, self.chipv)
        self.AGCDC_CTRL2 = AGCDC_CTRL2(self.channel, self.chipv)
        self.AGCOFDM_CTRL1 = AGCOFDM_CTRL1(self.channel, self.chipv)
        self.AGCOFDM_CTRL2 = AGCOFDM_CTRL2(self.channel, self.chipv)
        self.AGCOFDM_CTRL3 = AGCOFDM_CTRL3(self.channel, self.chipv)
        self.AGCOFDM_CTRL4 = AGCOFDM_CTRL4(self.channel, self.chipv)
        self.AGCPWR_CTRL1 = AGCPWR_CTRL1(self.channel, self.chipv)
        self.AGCPWR_CTRL2 = AGCPWR_CTRL2(self.channel, self.chipv)
        self.AGCPWR_CTRL3 = AGCPWR_CTRL3(self.channel, self.chipv)
        self.AGCPWR_CTRL5 = AGCPWR_CTRL5(self.channel, self.chipv)
        self.AGCPWR_CTRL6 = AGCPWR_CTRL6(self.channel, self.chipv)
        self.AGCPWR_CTRL7 = AGCPWR_CTRL7(self.channel, self.chipv)
        self.AGCFSM_CTRL1 = AGCFSM_CTRL1(self.channel, self.chipv)
        self.AGCFSM_CTRL2 = AGCFSM_CTRL2(self.channel, self.chipv)
        self.AGCFSM_CTRL3 = AGCFSM_CTRL3(self.channel, self.chipv)
        self.AGCMEM_CTRL1 = AGCMEM_CTRL1(self.channel, self.chipv)
        self.AGCMEM_CTRL2 = AGCMEM_CTRL2(self.channel, self.chipv)
        self.AGC11B_CTRL1 = AGC11B_CTRL1(self.channel, self.chipv)
        self.AGC11B_CTRL2 = AGC11B_CTRL2(self.channel, self.chipv)
        self.AGCRD1 = AGCRD1(self.channel, self.chipv)
        self.AGCRD2 = AGCRD2(self.channel, self.chipv)
        self.AGCOFDM_CTRL5 = AGCOFDM_CTRL5(self.channel, self.chipv)
        self.AGCPWR_CTRL8 = AGCPWR_CTRL8(self.channel, self.chipv)
        self.AGCGAIN_CTRL_1 = AGCGAIN_CTRL_1(self.channel, self.chipv)
        self.AGCGAIN_CTRL_2 = AGCGAIN_CTRL_2(self.channel, self.chipv)
        self.AGCGAIN_CTRL_3 = AGCGAIN_CTRL_3(self.channel, self.chipv)
        self.AGCPKDET_CTRL_0 = AGCPKDET_CTRL_0(self.channel, self.chipv)
        self.AGCRD9 = AGCRD9(self.channel, self.chipv)
        self.AGCOFDM_CTRL6 = AGCOFDM_CTRL6(self.channel, self.chipv)
        self.AGCFSM_CTRL4 = AGCFSM_CTRL4(self.channel, self.chipv)
        self.AGCRD3 = AGCRD3(self.channel, self.chipv)
        self.AGCBT_CTRL0 = AGCBT_CTRL0(self.channel, self.chipv)
        self.AGCBT_CTRL1 = AGCBT_CTRL1(self.channel, self.chipv)
        self.AGCBT_CTRL2 = AGCBT_CTRL2(self.channel, self.chipv)
        self.AGCHT2040_SCALE = AGCHT2040_SCALE(self.channel, self.chipv)
        self.AGCRD4 = AGCRD4(self.channel, self.chipv)
        self.AGCPWR_CTRL9 = AGCPWR_CTRL9(self.channel, self.chipv)
        self.AGCGAIN_CTRL_4 = AGCGAIN_CTRL_4(self.channel, self.chipv)
        self.AGCRD5 = AGCRD5(self.channel, self.chipv)
        self.AGCRD6 = AGCRD6(self.channel, self.chipv)
        self.AGCPWR_CTRL10 = AGCPWR_CTRL10(self.channel, self.chipv)
        self.AGCGAIN_CTRL_5 = AGCGAIN_CTRL_5(self.channel, self.chipv)
        self.AGCSEC_CTRL0 = AGCSEC_CTRL0(self.channel, self.chipv)
        self.AGCPWR_CTRL11 = AGCPWR_CTRL11(self.channel, self.chipv)
        self.AGCPWR_CTRL12 = AGCPWR_CTRL12(self.channel, self.chipv)
        self.AGCPWR_CTRL13 = AGCPWR_CTRL13(self.channel, self.chipv)
        self.AGCTEST_CTRL = AGCTEST_CTRL(self.channel, self.chipv)
        self.AGCOFDM_CTRL7 = AGCOFDM_CTRL7(self.channel, self.chipv)
        self.AGCRD7 = AGCRD7(self.channel, self.chipv)
        self.AGCOFDM_CTRL8 = AGCOFDM_CTRL8(self.channel, self.chipv)
        self.AGCOFDM_CTRL9 = AGCOFDM_CTRL9(self.channel, self.chipv)
        self.AGCOFDM_CTRL10 = AGCOFDM_CTRL10(self.channel, self.chipv)
        self.AGCBT_CTRL3 = AGCBT_CTRL3(self.channel, self.chipv)
        self.AGCOFDM_CTRL12 = AGCOFDM_CTRL12(self.channel, self.chipv)
        self.AGCPWR_CTRL14 = AGCPWR_CTRL14(self.channel, self.chipv)
        self.AGCCCA_CTRL0 = AGCCCA_CTRL0(self.channel, self.chipv)
        self.AGCGAIN_CTRL_6 = AGCGAIN_CTRL_6(self.channel, self.chipv)
        self.AGCGAIN_CTRL_7 = AGCGAIN_CTRL_7(self.channel, self.chipv)
        self.AGCCHAN_BW = AGCCHAN_BW(self.channel, self.chipv)
        self.AGCOFDM_CTRL11 = AGCOFDM_CTRL11(self.channel, self.chipv)
        self.AGCPWR_CTRL15 = AGCPWR_CTRL15(self.channel, self.chipv)
        self.AGCFSM_CTRL5 = AGCFSM_CTRL5(self.channel, self.chipv)
        self.AGCPWR_CTRL16 = AGCPWR_CTRL16(self.channel, self.chipv)
        self.AGCPWR_CTRL17 = AGCPWR_CTRL17(self.channel, self.chipv)
        self.AGCRD8 = AGCRD8(self.channel, self.chipv)
        self.AGCPWR_CTRL18 = AGCPWR_CTRL18(self.channel, self.chipv)
        self.AGCOFDM_CTRL13 = AGCOFDM_CTRL13(self.channel, self.chipv)
        self.AGCPWR_CTRL19 = AGCPWR_CTRL19(self.channel, self.chipv)
        self.AGCGAIN_CTRL_8 = AGCGAIN_CTRL_8(self.channel, self.chipv)
        self.AGCGAIN_CTRL_9 = AGCGAIN_CTRL_9(self.channel, self.chipv)
        self.AGCGAIN_CTRL_10 = AGCGAIN_CTRL_10(self.channel, self.chipv)
        self.AGCANT_CTRL1 = AGCANT_CTRL1(self.channel, self.chipv)
        self.AGCANT_CTRL2 = AGCANT_CTRL2(self.channel, self.chipv)
        self.AGC11B_CTRL3 = AGC11B_CTRL3(self.channel, self.chipv)
        self.AGCPWR_CTRL20 = AGCPWR_CTRL20(self.channel, self.chipv)
        self.AGCPWR_CTRL21 = AGCPWR_CTRL21(self.channel, self.chipv)
        self.AGCPWR_CTRL22 = AGCPWR_CTRL22(self.channel, self.chipv)
        self.AGCPWR_CTRL23 = AGCPWR_CTRL23(self.channel, self.chipv)
        self.AGCPWR_CTRL24 = AGCPWR_CTRL24(self.channel, self.chipv)
        self.AGCPWR_CTRL25 = AGCPWR_CTRL25(self.channel, self.chipv)
        self.AGCPWR_CTRL26 = AGCPWR_CTRL26(self.channel, self.chipv)
        self.AGCBT_CTRL4 = AGCBT_CTRL4(self.channel, self.chipv)
        self.AGCBT_CTRL5 = AGCBT_CTRL5(self.channel, self.chipv)
        self.AGCFINEGAIN_CTRL = AGCFINEGAIN_CTRL(self.channel, self.chipv)
        self.AGCRESTART_CTRL = AGCRESTART_CTRL(self.channel, self.chipv)
        self.AGCFSM_CTRL6 = AGCFSM_CTRL6(self.channel, self.chipv)
        self.AGCFSM_CTRL7 = AGCFSM_CTRL7(self.channel, self.chipv)
        self.AGCPD_CTRL = AGCPD_CTRL(self.channel, self.chipv)
        self.AGC_WSCAN_CTRL = AGC_WSCAN_CTRL(self.channel, self.chipv)
        self.AGCRD10 = AGCRD10(self.channel, self.chipv)
        self.AGCRD11 = AGCRD11(self.channel, self.chipv)
        self.AGCRD12 = AGCRD12(self.channel, self.chipv)
        self.AGCRD13 = AGCRD13(self.channel, self.chipv)
        self.AGCRD14 = AGCRD14(self.channel, self.chipv)
        self.AGCRD15 = AGCRD15(self.channel, self.chipv)
        self.AGCRD16 = AGCRD16(self.channel, self.chipv)
        self.AGCRD17 = AGCRD17(self.channel, self.chipv)
        self.AGCRD18 = AGCRD18(self.channel, self.chipv)
        self.AGCRD19 = AGCRD19(self.channel, self.chipv)
        self.AGCRD20 = AGCRD20(self.channel, self.chipv)
        self.AGCRD21 = AGCRD21(self.channel, self.chipv)
        self.AGCPWR_CTRL27 = AGCPWR_CTRL27(self.channel, self.chipv)
        self.AGCPWR_CTRL28 = AGCPWR_CTRL28(self.channel, self.chipv)
        self.AGCBT_CTRL6 = AGCBT_CTRL6(self.channel, self.chipv)
        self.AGCBT_CTRL7 = AGCBT_CTRL7(self.channel, self.chipv)
        self.AGCGAIN_CTRL_11 = AGCGAIN_CTRL_11(self.channel, self.chipv)
        self.AGCFSM_CTRL8 = AGCFSM_CTRL8(self.channel, self.chipv)
        self.AGCNOUSE = AGCNOUSE(self.channel, self.chipv)
class AGCDC_CTRL1(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x0
        self.__bb_dc_int_index_lsb = 16
        self.__bb_dc_int_index_msb = 22
        self.__reg_dc_int_chk_en_lsb = 15
        self.__reg_dc_int_chk_en_msb = 15
        self.__reg_dc_int_chk_thr_lsb = 6
        self.__reg_dc_int_chk_thr_msb = 14
        self.__reg_dc_cte_prot_dot8_en_lsb = 5
        self.__reg_dc_cte_prot_dot8_en_msb = 5
        self.__reg_dc_merge_mult_lsb = 2
        self.__reg_dc_merge_mult_msb = 4
        self.__reg_dc_merge_shr_lsb = 0
        self.__reg_dc_merge_shr_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def bb_dc_int_index(self):
        return self.__MEM.rdm(self.__addr, self.__bb_dc_int_index_msb, self.__bb_dc_int_index_lsb)
    @bb_dc_int_index.setter
    def bb_dc_int_index(self, value):
        return self.__MEM.wrm(self.__addr, self.__bb_dc_int_index_msb, self.__bb_dc_int_index_lsb, value)

    @property
    def reg_dc_int_chk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_int_chk_en_msb, self.__reg_dc_int_chk_en_lsb)
    @reg_dc_int_chk_en.setter
    def reg_dc_int_chk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_int_chk_en_msb, self.__reg_dc_int_chk_en_lsb, value)

    @property
    def reg_dc_int_chk_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_int_chk_thr_msb, self.__reg_dc_int_chk_thr_lsb)
    @reg_dc_int_chk_thr.setter
    def reg_dc_int_chk_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_int_chk_thr_msb, self.__reg_dc_int_chk_thr_lsb, value)

    @property
    def reg_dc_cte_prot_dot8_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_cte_prot_dot8_en_msb, self.__reg_dc_cte_prot_dot8_en_lsb)
    @reg_dc_cte_prot_dot8_en.setter
    def reg_dc_cte_prot_dot8_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_cte_prot_dot8_en_msb, self.__reg_dc_cte_prot_dot8_en_lsb, value)

    @property
    def reg_dc_merge_mult(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_merge_mult_msb, self.__reg_dc_merge_mult_lsb)
    @reg_dc_merge_mult.setter
    def reg_dc_merge_mult(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_merge_mult_msb, self.__reg_dc_merge_mult_lsb, value)

    @property
    def reg_dc_merge_shr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_merge_shr_msb, self.__reg_dc_merge_shr_lsb)
    @reg_dc_merge_shr.setter
    def reg_dc_merge_shr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_merge_shr_msb, self.__reg_dc_merge_shr_lsb, value)
class AGCDC_CTRL2(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x4
        self.__reg_coarse_use_memdc_lsb = 31
        self.__reg_coarse_use_memdc_msb = 31
        self.__reg_fine_use_memdc_lsb = 30
        self.__reg_fine_use_memdc_msb = 30
        self.__reg_store_dc_merge_lsb = 29
        self.__reg_store_dc_merge_msb = 29
        self.__reg_agc_dcmem_upd_en_lsb = 28
        self.__reg_agc_dcmem_upd_en_msb = 28
        self.__reg_ht2040_dcmem_en_lsb = 27
        self.__reg_ht2040_dcmem_en_msb = 27
        self.__reg_dc_mode_ht40_lsb = 25
        self.__reg_dc_mode_ht40_msb = 26
        self.__reg_modem_dc_fine_en_lsb = 24
        self.__reg_modem_dc_fine_en_msb = 24
        self.__reg_modem_dc_fine_est_en_lsb = 23
        self.__reg_modem_dc_fine_est_en_msb = 23
        self.__reg_dc_fine_max_loop_lsb = 19
        self.__reg_dc_fine_max_loop_msb = 21
        self.__reg_dc_coarse_force_mode_lsb = 17
        self.__reg_dc_coarse_force_mode_msb = 18
        self.__reg_use_dc_mem_en_lsb = 16
        self.__reg_use_dc_mem_en_msb = 16
        self.__reg_dc_init_i_lsb = 8
        self.__reg_dc_init_i_msb = 15
        self.__reg_dc_init_q_lsb = 0
        self.__reg_dc_init_q_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_coarse_use_memdc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coarse_use_memdc_msb, self.__reg_coarse_use_memdc_lsb)
    @reg_coarse_use_memdc.setter
    def reg_coarse_use_memdc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coarse_use_memdc_msb, self.__reg_coarse_use_memdc_lsb, value)

    @property
    def reg_fine_use_memdc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fine_use_memdc_msb, self.__reg_fine_use_memdc_lsb)
    @reg_fine_use_memdc.setter
    def reg_fine_use_memdc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fine_use_memdc_msb, self.__reg_fine_use_memdc_lsb, value)

    @property
    def reg_store_dc_merge(self):
        return self.__MEM.rdm(self.__addr, self.__reg_store_dc_merge_msb, self.__reg_store_dc_merge_lsb)
    @reg_store_dc_merge.setter
    def reg_store_dc_merge(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_store_dc_merge_msb, self.__reg_store_dc_merge_lsb, value)

    @property
    def reg_agc_dcmem_upd_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_dcmem_upd_en_msb, self.__reg_agc_dcmem_upd_en_lsb)
    @reg_agc_dcmem_upd_en.setter
    def reg_agc_dcmem_upd_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_dcmem_upd_en_msb, self.__reg_agc_dcmem_upd_en_lsb, value)

    @property
    def reg_ht2040_dcmem_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ht2040_dcmem_en_msb, self.__reg_ht2040_dcmem_en_lsb)
    @reg_ht2040_dcmem_en.setter
    def reg_ht2040_dcmem_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ht2040_dcmem_en_msb, self.__reg_ht2040_dcmem_en_lsb, value)

    @property
    def reg_dc_mode_ht40(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_mode_ht40_msb, self.__reg_dc_mode_ht40_lsb)
    @reg_dc_mode_ht40.setter
    def reg_dc_mode_ht40(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_mode_ht40_msb, self.__reg_dc_mode_ht40_lsb, value)

    @property
    def reg_modem_dc_fine_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_modem_dc_fine_en_msb, self.__reg_modem_dc_fine_en_lsb)
    @reg_modem_dc_fine_en.setter
    def reg_modem_dc_fine_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_modem_dc_fine_en_msb, self.__reg_modem_dc_fine_en_lsb, value)

    @property
    def reg_modem_dc_fine_est_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_modem_dc_fine_est_en_msb, self.__reg_modem_dc_fine_est_en_lsb)
    @reg_modem_dc_fine_est_en.setter
    def reg_modem_dc_fine_est_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_modem_dc_fine_est_en_msb, self.__reg_modem_dc_fine_est_en_lsb, value)

    @property
    def reg_dc_fine_max_loop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_fine_max_loop_msb, self.__reg_dc_fine_max_loop_lsb)
    @reg_dc_fine_max_loop.setter
    def reg_dc_fine_max_loop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_fine_max_loop_msb, self.__reg_dc_fine_max_loop_lsb, value)

    @property
    def reg_dc_coarse_force_mode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_coarse_force_mode_msb, self.__reg_dc_coarse_force_mode_lsb)
    @reg_dc_coarse_force_mode.setter
    def reg_dc_coarse_force_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_coarse_force_mode_msb, self.__reg_dc_coarse_force_mode_lsb, value)

    @property
    def reg_use_dc_mem_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_use_dc_mem_en_msb, self.__reg_use_dc_mem_en_lsb)
    @reg_use_dc_mem_en.setter
    def reg_use_dc_mem_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_use_dc_mem_en_msb, self.__reg_use_dc_mem_en_lsb, value)

    @property
    def reg_dc_init_i(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_init_i_msb, self.__reg_dc_init_i_lsb)
    @reg_dc_init_i.setter
    def reg_dc_init_i(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_init_i_msb, self.__reg_dc_init_i_lsb, value)

    @property
    def reg_dc_init_q(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_init_q_msb, self.__reg_dc_init_q_lsb)
    @reg_dc_init_q.setter
    def reg_dc_init_q(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_init_q_msb, self.__reg_dc_init_q_lsb, value)
class AGCOFDM_CTRL1(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x8
        self.__reg_agc_ocorr_thr2_2_lsb = 24
        self.__reg_agc_ocorr_thr2_2_msb = 31
        self.__reg_agc_ocorr_thr2_lsb = 16
        self.__reg_agc_ocorr_thr2_msb = 23
        self.__reg_agc_ocorr_thr1_2_lsb = 8
        self.__reg_agc_ocorr_thr1_2_msb = 15
        self.__reg_agc_ocorr_thr1_lsb = 0
        self.__reg_agc_ocorr_thr1_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_agc_ocorr_thr2_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_ocorr_thr2_2_msb, self.__reg_agc_ocorr_thr2_2_lsb)
    @reg_agc_ocorr_thr2_2.setter
    def reg_agc_ocorr_thr2_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_ocorr_thr2_2_msb, self.__reg_agc_ocorr_thr2_2_lsb, value)

    @property
    def reg_agc_ocorr_thr2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_ocorr_thr2_msb, self.__reg_agc_ocorr_thr2_lsb)
    @reg_agc_ocorr_thr2.setter
    def reg_agc_ocorr_thr2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_ocorr_thr2_msb, self.__reg_agc_ocorr_thr2_lsb, value)

    @property
    def reg_agc_ocorr_thr1_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_ocorr_thr1_2_msb, self.__reg_agc_ocorr_thr1_2_lsb)
    @reg_agc_ocorr_thr1_2.setter
    def reg_agc_ocorr_thr1_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_ocorr_thr1_2_msb, self.__reg_agc_ocorr_thr1_2_lsb, value)

    @property
    def reg_agc_ocorr_thr1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_ocorr_thr1_msb, self.__reg_agc_ocorr_thr1_lsb)
    @reg_agc_ocorr_thr1.setter
    def reg_agc_ocorr_thr1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_ocorr_thr1_msb, self.__reg_agc_ocorr_thr1_lsb, value)
class AGCOFDM_CTRL2(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0xc
        self.__reg_pwr_valid_cnt_init_2_lsb = 27
        self.__reg_pwr_valid_cnt_init_2_msb = 30
        self.__reg_pwr_inband_thr_lsb = 21
        self.__reg_pwr_inband_thr_msb = 26
        self.__reg_corr_det_thr_2_lsb = 15
        self.__reg_corr_det_thr_2_msb = 20
        self.__reg_pwr_valid_cnt_init_lsb = 11
        self.__reg_pwr_valid_cnt_init_msb = 14
        self.__reg_corr_det_thr_lsb = 6
        self.__reg_corr_det_thr_msb = 10
        self.__reg_corr_det_cnt_max_lsb = 0
        self.__reg_corr_det_cnt_max_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_pwr_valid_cnt_init_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_valid_cnt_init_2_msb, self.__reg_pwr_valid_cnt_init_2_lsb)
    @reg_pwr_valid_cnt_init_2.setter
    def reg_pwr_valid_cnt_init_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_valid_cnt_init_2_msb, self.__reg_pwr_valid_cnt_init_2_lsb, value)

    @property
    def reg_pwr_inband_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_inband_thr_msb, self.__reg_pwr_inband_thr_lsb)
    @reg_pwr_inband_thr.setter
    def reg_pwr_inband_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_inband_thr_msb, self.__reg_pwr_inband_thr_lsb, value)

    @property
    def reg_corr_det_thr_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_det_thr_2_msb, self.__reg_corr_det_thr_2_lsb)
    @reg_corr_det_thr_2.setter
    def reg_corr_det_thr_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_det_thr_2_msb, self.__reg_corr_det_thr_2_lsb, value)

    @property
    def reg_pwr_valid_cnt_init(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_valid_cnt_init_msb, self.__reg_pwr_valid_cnt_init_lsb)
    @reg_pwr_valid_cnt_init.setter
    def reg_pwr_valid_cnt_init(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_valid_cnt_init_msb, self.__reg_pwr_valid_cnt_init_lsb, value)

    @property
    def reg_corr_det_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_det_thr_msb, self.__reg_corr_det_thr_lsb)
    @reg_corr_det_thr.setter
    def reg_corr_det_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_det_thr_msb, self.__reg_corr_det_thr_lsb, value)

    @property
    def reg_corr_det_cnt_max(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_det_cnt_max_msb, self.__reg_corr_det_cnt_max_lsb)
    @reg_corr_det_cnt_max.setter
    def reg_corr_det_cnt_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_det_cnt_max_msb, self.__reg_corr_det_cnt_max_lsb, value)
class AGCOFDM_CTRL3(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x10
        self.__reg_ocorr_gt_noise_thr_1_lsb = 23
        self.__reg_ocorr_gt_noise_thr_1_msb = 31
        self.__reg_pwr_fir_gt_thr_lsb = 13
        self.__reg_pwr_fir_gt_thr_msb = 22
        self.__reg_pwr_fir_surge_thr_lsb = 6
        self.__reg_pwr_fir_surge_thr_msb = 12
        self.__reg_pwr_inband_surge_thr_lsb = 0
        self.__reg_pwr_inband_surge_thr_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ocorr_gt_noise_thr_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ocorr_gt_noise_thr_1_msb, self.__reg_ocorr_gt_noise_thr_1_lsb)
    @reg_ocorr_gt_noise_thr_1.setter
    def reg_ocorr_gt_noise_thr_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ocorr_gt_noise_thr_1_msb, self.__reg_ocorr_gt_noise_thr_1_lsb, value)

    @property
    def reg_pwr_fir_gt_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fir_gt_thr_msb, self.__reg_pwr_fir_gt_thr_lsb)
    @reg_pwr_fir_gt_thr.setter
    def reg_pwr_fir_gt_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fir_gt_thr_msb, self.__reg_pwr_fir_gt_thr_lsb, value)

    @property
    def reg_pwr_fir_surge_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fir_surge_thr_msb, self.__reg_pwr_fir_surge_thr_lsb)
    @reg_pwr_fir_surge_thr.setter
    def reg_pwr_fir_surge_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fir_surge_thr_msb, self.__reg_pwr_fir_surge_thr_lsb, value)

    @property
    def reg_pwr_inband_surge_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_inband_surge_thr_msb, self.__reg_pwr_inband_surge_thr_lsb)
    @reg_pwr_inband_surge_thr.setter
    def reg_pwr_inband_surge_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_inband_surge_thr_msb, self.__reg_pwr_inband_surge_thr_lsb, value)
class AGCOFDM_CTRL4(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x14
        self.__reg_ocorr_gt_noise_thr_2_lsb = 23
        self.__reg_ocorr_gt_noise_thr_2_msb = 31
        self.__reg_pwr_fir_gt_thr_2_lsb = 13
        self.__reg_pwr_fir_gt_thr_2_msb = 22
        self.__reg_pwr_fir_surge_thr_2_lsb = 6
        self.__reg_pwr_fir_surge_thr_2_msb = 12
        self.__reg_pwr_inband_surge_thr_2_lsb = 0
        self.__reg_pwr_inband_surge_thr_2_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ocorr_gt_noise_thr_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ocorr_gt_noise_thr_2_msb, self.__reg_ocorr_gt_noise_thr_2_lsb)
    @reg_ocorr_gt_noise_thr_2.setter
    def reg_ocorr_gt_noise_thr_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ocorr_gt_noise_thr_2_msb, self.__reg_ocorr_gt_noise_thr_2_lsb, value)

    @property
    def reg_pwr_fir_gt_thr_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fir_gt_thr_2_msb, self.__reg_pwr_fir_gt_thr_2_lsb)
    @reg_pwr_fir_gt_thr_2.setter
    def reg_pwr_fir_gt_thr_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fir_gt_thr_2_msb, self.__reg_pwr_fir_gt_thr_2_lsb, value)

    @property
    def reg_pwr_fir_surge_thr_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fir_surge_thr_2_msb, self.__reg_pwr_fir_surge_thr_2_lsb)
    @reg_pwr_fir_surge_thr_2.setter
    def reg_pwr_fir_surge_thr_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fir_surge_thr_2_msb, self.__reg_pwr_fir_surge_thr_2_lsb, value)

    @property
    def reg_pwr_inband_surge_thr_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_inband_surge_thr_2_msb, self.__reg_pwr_inband_surge_thr_2_lsb)
    @reg_pwr_inband_surge_thr_2.setter
    def reg_pwr_inband_surge_thr_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_inband_surge_thr_2_msb, self.__reg_pwr_inband_surge_thr_2_lsb, value)
class AGCPWR_CTRL1(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x18
        self.__reg_noise_min_n_rst_lsb = 31
        self.__reg_noise_min_n_rst_msb = 31
        self.__reg_sig_weak_mode_lsb = 30
        self.__reg_sig_weak_mode_msb = 30
        self.__reg_rssi_mode_lsb = 29
        self.__reg_rssi_mode_msb = 29
        self.__reg_agc_noise_auto_en_lsb = 28
        self.__reg_agc_noise_auto_en_msb = 28
        self.__reg_agc_reset_noise_lsb = 27
        self.__reg_agc_reset_noise_msb = 27
        self.__reg_noise_weak_thr_en_lsb = 26
        self.__reg_noise_weak_thr_en_msb = 26
        self.__reg_noise_done_clr_lsb = 25
        self.__reg_noise_done_clr_msb = 25
        self.__r_noise_done_raw_lsb = 24
        self.__r_noise_done_raw_msb = 24
        self.__reg_noise_cal_lsb = 23
        self.__reg_noise_cal_msb = 23
        self.__reg_init_noisepwr_lsb = 15
        self.__reg_init_noisepwr_msb = 22
        self.__reg_noise_hw_force_lsb = 5
        self.__reg_noise_hw_force_msb = 14
        self.__reg_noise_hw_force_en_lsb = 4
        self.__reg_noise_hw_force_en_msb = 4
        self.__reg_noise_hw_upd_en_lsb = 3
        self.__reg_noise_hw_upd_en_msb = 3
        self.__reg_noise_cal_time_lsb = 0
        self.__reg_noise_cal_time_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_noise_min_n_rst(self):
        return self.__MEM.rdm(self.__addr, self.__reg_noise_min_n_rst_msb, self.__reg_noise_min_n_rst_lsb)
    @reg_noise_min_n_rst.setter
    def reg_noise_min_n_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_noise_min_n_rst_msb, self.__reg_noise_min_n_rst_lsb, value)

    @property
    def reg_sig_weak_mode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sig_weak_mode_msb, self.__reg_sig_weak_mode_lsb)
    @reg_sig_weak_mode.setter
    def reg_sig_weak_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sig_weak_mode_msb, self.__reg_sig_weak_mode_lsb, value)

    @property
    def reg_rssi_mode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rssi_mode_msb, self.__reg_rssi_mode_lsb)
    @reg_rssi_mode.setter
    def reg_rssi_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rssi_mode_msb, self.__reg_rssi_mode_lsb, value)

    @property
    def reg_agc_noise_auto_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_noise_auto_en_msb, self.__reg_agc_noise_auto_en_lsb)
    @reg_agc_noise_auto_en.setter
    def reg_agc_noise_auto_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_noise_auto_en_msb, self.__reg_agc_noise_auto_en_lsb, value)

    @property
    def reg_agc_reset_noise(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_reset_noise_msb, self.__reg_agc_reset_noise_lsb)
    @reg_agc_reset_noise.setter
    def reg_agc_reset_noise(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_reset_noise_msb, self.__reg_agc_reset_noise_lsb, value)

    @property
    def reg_noise_weak_thr_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_noise_weak_thr_en_msb, self.__reg_noise_weak_thr_en_lsb)
    @reg_noise_weak_thr_en.setter
    def reg_noise_weak_thr_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_noise_weak_thr_en_msb, self.__reg_noise_weak_thr_en_lsb, value)

    @property
    def reg_noise_done_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_noise_done_clr_msb, self.__reg_noise_done_clr_lsb)
    @reg_noise_done_clr.setter
    def reg_noise_done_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_noise_done_clr_msb, self.__reg_noise_done_clr_lsb, value)

    @property
    def r_noise_done_raw(self):
        return self.__MEM.rdm(self.__addr, self.__r_noise_done_raw_msb, self.__r_noise_done_raw_lsb)
    @r_noise_done_raw.setter
    def r_noise_done_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_noise_done_raw_msb, self.__r_noise_done_raw_lsb, value)

    @property
    def reg_noise_cal(self):
        return self.__MEM.rdm(self.__addr, self.__reg_noise_cal_msb, self.__reg_noise_cal_lsb)
    @reg_noise_cal.setter
    def reg_noise_cal(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_noise_cal_msb, self.__reg_noise_cal_lsb, value)

    @property
    def reg_init_noisepwr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_init_noisepwr_msb, self.__reg_init_noisepwr_lsb)
    @reg_init_noisepwr.setter
    def reg_init_noisepwr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_init_noisepwr_msb, self.__reg_init_noisepwr_lsb, value)

    @property
    def reg_noise_hw_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_noise_hw_force_msb, self.__reg_noise_hw_force_lsb)
    @reg_noise_hw_force.setter
    def reg_noise_hw_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_noise_hw_force_msb, self.__reg_noise_hw_force_lsb, value)

    @property
    def reg_noise_hw_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_noise_hw_force_en_msb, self.__reg_noise_hw_force_en_lsb)
    @reg_noise_hw_force_en.setter
    def reg_noise_hw_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_noise_hw_force_en_msb, self.__reg_noise_hw_force_en_lsb, value)

    @property
    def reg_noise_hw_upd_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_noise_hw_upd_en_msb, self.__reg_noise_hw_upd_en_lsb)
    @reg_noise_hw_upd_en.setter
    def reg_noise_hw_upd_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_noise_hw_upd_en_msb, self.__reg_noise_hw_upd_en_lsb, value)

    @property
    def reg_noise_cal_time(self):
        return self.__MEM.rdm(self.__addr, self.__reg_noise_cal_time_msb, self.__reg_noise_cal_time_lsb)
    @reg_noise_cal_time.setter
    def reg_noise_cal_time(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_noise_cal_time_msb, self.__reg_noise_cal_time_lsb, value)
class AGCPWR_CTRL2(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x1c
        self.__reg_noise_weak_thr_lsb = 24
        self.__reg_noise_weak_thr_msb = 31
        self.__reg_rssi_strong_thr_lsb = 16
        self.__reg_rssi_strong_thr_msb = 23
        self.__reg_rssi_modecheck_thr_lsb = 8
        self.__reg_rssi_modecheck_thr_msb = 15
        self.__reg_sig_weak_thr_lsb = 0
        self.__reg_sig_weak_thr_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_noise_weak_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_noise_weak_thr_msb, self.__reg_noise_weak_thr_lsb)
    @reg_noise_weak_thr.setter
    def reg_noise_weak_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_noise_weak_thr_msb, self.__reg_noise_weak_thr_lsb, value)

    @property
    def reg_rssi_strong_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rssi_strong_thr_msb, self.__reg_rssi_strong_thr_lsb)
    @reg_rssi_strong_thr.setter
    def reg_rssi_strong_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rssi_strong_thr_msb, self.__reg_rssi_strong_thr_lsb, value)

    @property
    def reg_rssi_modecheck_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rssi_modecheck_thr_msb, self.__reg_rssi_modecheck_thr_lsb)
    @reg_rssi_modecheck_thr.setter
    def reg_rssi_modecheck_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rssi_modecheck_thr_msb, self.__reg_rssi_modecheck_thr_lsb, value)

    @property
    def reg_sig_weak_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sig_weak_thr_msb, self.__reg_sig_weak_thr_lsb)
    @reg_sig_weak_thr.setter
    def reg_sig_weak_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sig_weak_thr_msb, self.__reg_sig_weak_thr_lsb, value)
class AGCPWR_CTRL3(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x20
        self.__reg_adcsat_rsta_thr_lsb = 26
        self.__reg_adcsat_rsta_thr_msb = 31
        self.__reg_adc_sat2_en_lsb = 25
        self.__reg_adc_sat2_en_msb = 25
        self.__reg_adcsat_sum_thr2_lsb = 20
        self.__reg_adcsat_sum_thr2_msb = 24
        self.__reg_adcsat_sum_thr_lsb = 14
        self.__reg_adcsat_sum_thr_msb = 19
        self.__reg_adcsat_count_max_lsb = 9
        self.__reg_adcsat_count_max_msb = 13
        self.__reg_adcsat_thr_lsb = 0
        self.__reg_adcsat_thr_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_adcsat_rsta_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcsat_rsta_thr_msb, self.__reg_adcsat_rsta_thr_lsb)
    @reg_adcsat_rsta_thr.setter
    def reg_adcsat_rsta_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcsat_rsta_thr_msb, self.__reg_adcsat_rsta_thr_lsb, value)

    @property
    def reg_adc_sat2_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_sat2_en_msb, self.__reg_adc_sat2_en_lsb)
    @reg_adc_sat2_en.setter
    def reg_adc_sat2_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_sat2_en_msb, self.__reg_adc_sat2_en_lsb, value)

    @property
    def reg_adcsat_sum_thr2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcsat_sum_thr2_msb, self.__reg_adcsat_sum_thr2_lsb)
    @reg_adcsat_sum_thr2.setter
    def reg_adcsat_sum_thr2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcsat_sum_thr2_msb, self.__reg_adcsat_sum_thr2_lsb, value)

    @property
    def reg_adcsat_sum_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcsat_sum_thr_msb, self.__reg_adcsat_sum_thr_lsb)
    @reg_adcsat_sum_thr.setter
    def reg_adcsat_sum_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcsat_sum_thr_msb, self.__reg_adcsat_sum_thr_lsb, value)

    @property
    def reg_adcsat_count_max(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcsat_count_max_msb, self.__reg_adcsat_count_max_lsb)
    @reg_adcsat_count_max.setter
    def reg_adcsat_count_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcsat_count_max_msb, self.__reg_adcsat_count_max_lsb, value)

    @property
    def reg_adcsat_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcsat_thr_msb, self.__reg_adcsat_thr_lsb)
    @reg_adcsat_thr.setter
    def reg_adcsat_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcsat_thr_msb, self.__reg_adcsat_thr_lsb, value)
class AGCPWR_CTRL5(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x24
        self.__reg_pwr_fir2_cmp_lsb = 27
        self.__reg_pwr_fir2_cmp_msb = 31
        self.__reg_coarse_weak_thr_lsb = 19
        self.__reg_coarse_weak_thr_msb = 26
        self.__reg_coarse_weak_prot_lsb = 18
        self.__reg_coarse_weak_prot_msb = 18
        self.__reg_pwr_low_thr_lsb = 9
        self.__reg_pwr_low_thr_msb = 17
        self.__reg_pwr_high_thr_lsb = 0
        self.__reg_pwr_high_thr_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_pwr_fir2_cmp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fir2_cmp_msb, self.__reg_pwr_fir2_cmp_lsb)
    @reg_pwr_fir2_cmp.setter
    def reg_pwr_fir2_cmp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fir2_cmp_msb, self.__reg_pwr_fir2_cmp_lsb, value)

    @property
    def reg_coarse_weak_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coarse_weak_thr_msb, self.__reg_coarse_weak_thr_lsb)
    @reg_coarse_weak_thr.setter
    def reg_coarse_weak_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coarse_weak_thr_msb, self.__reg_coarse_weak_thr_lsb, value)

    @property
    def reg_coarse_weak_prot(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coarse_weak_prot_msb, self.__reg_coarse_weak_prot_lsb)
    @reg_coarse_weak_prot.setter
    def reg_coarse_weak_prot(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coarse_weak_prot_msb, self.__reg_coarse_weak_prot_lsb, value)

    @property
    def reg_pwr_low_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_low_thr_msb, self.__reg_pwr_low_thr_lsb)
    @reg_pwr_low_thr.setter
    def reg_pwr_low_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_low_thr_msb, self.__reg_pwr_low_thr_lsb, value)

    @property
    def reg_pwr_high_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_high_thr_msb, self.__reg_pwr_high_thr_lsb)
    @reg_pwr_high_thr.setter
    def reg_pwr_high_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_high_thr_msb, self.__reg_pwr_high_thr_lsb, value)
class AGCPWR_CTRL6(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x28
        self.__reg_pwr_det_sel_lsb = 30
        self.__reg_pwr_det_sel_msb = 30
        self.__reg_pwr_coarse_sel_lsb = 29
        self.__reg_pwr_coarse_sel_msb = 29
        self.__reg_pwr_fine_sel_lsb = 27
        self.__reg_pwr_fine_sel_msb = 28
        self.__reg_pwr_fine_lsb = 18
        self.__reg_pwr_fine_msb = 26
        self.__reg_pwr_coarse_low_lsb = 9
        self.__reg_pwr_coarse_low_msb = 17
        self.__reg_pwr_coarse_high_lsb = 0
        self.__reg_pwr_coarse_high_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_pwr_det_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_det_sel_msb, self.__reg_pwr_det_sel_lsb)
    @reg_pwr_det_sel.setter
    def reg_pwr_det_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_det_sel_msb, self.__reg_pwr_det_sel_lsb, value)

    @property
    def reg_pwr_coarse_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_coarse_sel_msb, self.__reg_pwr_coarse_sel_lsb)
    @reg_pwr_coarse_sel.setter
    def reg_pwr_coarse_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_coarse_sel_msb, self.__reg_pwr_coarse_sel_lsb, value)

    @property
    def reg_pwr_fine_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_sel_msb, self.__reg_pwr_fine_sel_lsb)
    @reg_pwr_fine_sel.setter
    def reg_pwr_fine_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_sel_msb, self.__reg_pwr_fine_sel_lsb, value)

    @property
    def reg_pwr_fine(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_msb, self.__reg_pwr_fine_lsb)
    @reg_pwr_fine.setter
    def reg_pwr_fine(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_msb, self.__reg_pwr_fine_lsb, value)

    @property
    def reg_pwr_coarse_low(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_coarse_low_msb, self.__reg_pwr_coarse_low_lsb)
    @reg_pwr_coarse_low.setter
    def reg_pwr_coarse_low(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_coarse_low_msb, self.__reg_pwr_coarse_low_lsb, value)

    @property
    def reg_pwr_coarse_high(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_coarse_high_msb, self.__reg_pwr_coarse_high_lsb)
    @reg_pwr_coarse_high.setter
    def reg_pwr_coarse_high(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_coarse_high_msb, self.__reg_pwr_coarse_high_lsb, value)
class AGCPWR_CTRL7(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x2c
        self.__reg_gain_force_lsb = 24
        self.__reg_gain_force_msb = 31
        self.__reg_gain_force_en_lsb = 23
        self.__reg_gain_force_en_msb = 23
        self.__reg_fast_gain_set_lsb = 22
        self.__reg_fast_gain_set_msb = 22
        self.__reg_min_gain_lsb = 15
        self.__reg_min_gain_msb = 21
        self.__reg_max_gain_lsb = 8
        self.__reg_max_gain_msb = 14
        self.__reg_rxgain_comp_lsb = 0
        self.__reg_rxgain_comp_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_gain_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_force_msb, self.__reg_gain_force_lsb)
    @reg_gain_force.setter
    def reg_gain_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_force_msb, self.__reg_gain_force_lsb, value)

    @property
    def reg_gain_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_force_en_msb, self.__reg_gain_force_en_lsb)
    @reg_gain_force_en.setter
    def reg_gain_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_force_en_msb, self.__reg_gain_force_en_lsb, value)

    @property
    def reg_fast_gain_set(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fast_gain_set_msb, self.__reg_fast_gain_set_lsb)
    @reg_fast_gain_set.setter
    def reg_fast_gain_set(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fast_gain_set_msb, self.__reg_fast_gain_set_lsb, value)

    @property
    def reg_min_gain(self):
        return self.__MEM.rdm(self.__addr, self.__reg_min_gain_msb, self.__reg_min_gain_lsb)
    @reg_min_gain.setter
    def reg_min_gain(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_min_gain_msb, self.__reg_min_gain_lsb, value)

    @property
    def reg_max_gain(self):
        return self.__MEM.rdm(self.__addr, self.__reg_max_gain_msb, self.__reg_max_gain_lsb)
    @reg_max_gain.setter
    def reg_max_gain(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_max_gain_msb, self.__reg_max_gain_lsb, value)

    @property
    def reg_rxgain_comp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxgain_comp_msb, self.__reg_rxgain_comp_lsb)
    @reg_rxgain_comp.setter
    def reg_rxgain_comp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxgain_comp_msb, self.__reg_rxgain_comp_lsb, value)
class AGCFSM_CTRL1(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x30
        self.__reg_11n_gain_en_lsb = 31
        self.__reg_11n_gain_en_msb = 31
        self.__reg_11b_2nd_gain_en_lsb = 30
        self.__reg_11b_2nd_gain_en_msb = 30
        self.__reg_agc_dis_lsb = 29
        self.__reg_agc_dis_msb = 29
        self.__reg_agc_start_delay_lsb = 19
        self.__reg_agc_start_delay_msb = 28
        self.__reg_ant_time_lsb = 11
        self.__reg_ant_time_msb = 17
        self.__reg_restart_st_ext_lsb = 9
        self.__reg_restart_st_ext_msb = 10
        self.__reg_agc_reset_sw_lsb = 8
        self.__reg_agc_reset_sw_msb = 8
        self.__reg_pwr_go_down_ind_en_lsb = 7
        self.__reg_pwr_go_down_ind_en_msb = 7
        self.__reg_agc_restart_en_lsb = 6
        self.__reg_agc_restart_en_msb = 6
        self.__reg_11b_en_lsb = 5
        self.__reg_11b_en_msb = 5
        self.__reg_11a_en_lsb = 4
        self.__reg_11a_en_msb = 4
        self.__reg_gain_tune_min_lsb = 1
        self.__reg_gain_tune_min_msb = 3
        self.__reg_adcsat_hold_lsb = 0
        self.__reg_adcsat_hold_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_11n_gain_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_11n_gain_en_msb, self.__reg_11n_gain_en_lsb)
    @reg_11n_gain_en.setter
    def reg_11n_gain_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_11n_gain_en_msb, self.__reg_11n_gain_en_lsb, value)

    @property
    def reg_11b_2nd_gain_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_11b_2nd_gain_en_msb, self.__reg_11b_2nd_gain_en_lsb)
    @reg_11b_2nd_gain_en.setter
    def reg_11b_2nd_gain_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_11b_2nd_gain_en_msb, self.__reg_11b_2nd_gain_en_lsb, value)

    @property
    def reg_agc_dis(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_dis_msb, self.__reg_agc_dis_lsb)
    @reg_agc_dis.setter
    def reg_agc_dis(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_dis_msb, self.__reg_agc_dis_lsb, value)

    @property
    def reg_agc_start_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_start_delay_msb, self.__reg_agc_start_delay_lsb)
    @reg_agc_start_delay.setter
    def reg_agc_start_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_start_delay_msb, self.__reg_agc_start_delay_lsb, value)

    @property
    def reg_ant_time(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ant_time_msb, self.__reg_ant_time_lsb)
    @reg_ant_time.setter
    def reg_ant_time(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ant_time_msb, self.__reg_ant_time_lsb, value)

    @property
    def reg_restart_st_ext(self):
        return self.__MEM.rdm(self.__addr, self.__reg_restart_st_ext_msb, self.__reg_restart_st_ext_lsb)
    @reg_restart_st_ext.setter
    def reg_restart_st_ext(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_restart_st_ext_msb, self.__reg_restart_st_ext_lsb, value)

    @property
    def reg_agc_reset_sw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_reset_sw_msb, self.__reg_agc_reset_sw_lsb)
    @reg_agc_reset_sw.setter
    def reg_agc_reset_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_reset_sw_msb, self.__reg_agc_reset_sw_lsb, value)

    @property
    def reg_pwr_go_down_ind_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_go_down_ind_en_msb, self.__reg_pwr_go_down_ind_en_lsb)
    @reg_pwr_go_down_ind_en.setter
    def reg_pwr_go_down_ind_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_go_down_ind_en_msb, self.__reg_pwr_go_down_ind_en_lsb, value)

    @property
    def reg_agc_restart_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_restart_en_msb, self.__reg_agc_restart_en_lsb)
    @reg_agc_restart_en.setter
    def reg_agc_restart_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_restart_en_msb, self.__reg_agc_restart_en_lsb, value)

    @property
    def reg_11b_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_11b_en_msb, self.__reg_11b_en_lsb)
    @reg_11b_en.setter
    def reg_11b_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_11b_en_msb, self.__reg_11b_en_lsb, value)

    @property
    def reg_11a_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_11a_en_msb, self.__reg_11a_en_lsb)
    @reg_11a_en.setter
    def reg_11a_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_11a_en_msb, self.__reg_11a_en_lsb, value)

    @property
    def reg_gain_tune_min(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_tune_min_msb, self.__reg_gain_tune_min_lsb)
    @reg_gain_tune_min.setter
    def reg_gain_tune_min(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_tune_min_msb, self.__reg_gain_tune_min_lsb, value)

    @property
    def reg_adcsat_hold(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcsat_hold_msb, self.__reg_adcsat_hold_lsb)
    @reg_adcsat_hold.setter
    def reg_adcsat_hold(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcsat_hold_msb, self.__reg_adcsat_hold_lsb, value)
class AGCFSM_CTRL2(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x34
        self.__reg_adc_dc_rm_time_lsb = 24
        self.__reg_adc_dc_rm_time_msb = 30
        self.__reg_modem_time_lsb = 16
        self.__reg_modem_time_msb = 22
        self.__reg_measure_time_lsb = 8
        self.__reg_measure_time_msb = 14
        self.__reg_settling_time_lsb = 0
        self.__reg_settling_time_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_adc_dc_rm_time(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_dc_rm_time_msb, self.__reg_adc_dc_rm_time_lsb)
    @reg_adc_dc_rm_time.setter
    def reg_adc_dc_rm_time(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_dc_rm_time_msb, self.__reg_adc_dc_rm_time_lsb, value)

    @property
    def reg_modem_time(self):
        return self.__MEM.rdm(self.__addr, self.__reg_modem_time_msb, self.__reg_modem_time_lsb)
    @reg_modem_time.setter
    def reg_modem_time(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_modem_time_msb, self.__reg_modem_time_lsb, value)

    @property
    def reg_measure_time(self):
        return self.__MEM.rdm(self.__addr, self.__reg_measure_time_msb, self.__reg_measure_time_lsb)
    @reg_measure_time.setter
    def reg_measure_time(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_measure_time_msb, self.__reg_measure_time_lsb, value)

    @property
    def reg_settling_time(self):
        return self.__MEM.rdm(self.__addr, self.__reg_settling_time_msb, self.__reg_settling_time_lsb)
    @reg_settling_time.setter
    def reg_settling_time(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_settling_time_msb, self.__reg_settling_time_lsb, value)
class AGCFSM_CTRL3(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x38
        self.__reg_det_2_fine_en_lsb = 31
        self.__reg_det_2_fine_en_msb = 31
        self.__reg_modechk_tim_prot_lsb = 30
        self.__reg_modechk_tim_prot_msb = 30
        self.__reg_gain_upd_dis_lsb = 29
        self.__reg_gain_upd_dis_msb = 29
        self.__reg_agc_done_force_lsb = 28
        self.__reg_agc_done_force_msb = 28
        self.__reg_fast_check_lsb = 27
        self.__reg_fast_check_msb = 27
        self.__reg_strong_check_lsb = 26
        self.__reg_strong_check_msb = 26
        self.__reg_pwr_check_wait_count_lsb = 23
        self.__reg_pwr_check_wait_count_msb = 25
        self.__reg_fir_dc_rm_time_lsb = 16
        self.__reg_fir_dc_rm_time_msb = 22
        self.__reg_rx_end_td_clr_lsb = 15
        self.__reg_rx_end_td_clr_msb = 15
        self.__reg_measure_delay_b_lsb = 10
        self.__reg_measure_delay_b_msb = 14
        self.__reg_measure_delay_a_lsb = 5
        self.__reg_measure_delay_a_msb = 9
        self.__reg_measure_delay_ab_lsb = 0
        self.__reg_measure_delay_ab_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_det_2_fine_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_det_2_fine_en_msb, self.__reg_det_2_fine_en_lsb)
    @reg_det_2_fine_en.setter
    def reg_det_2_fine_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_det_2_fine_en_msb, self.__reg_det_2_fine_en_lsb, value)

    @property
    def reg_modechk_tim_prot(self):
        return self.__MEM.rdm(self.__addr, self.__reg_modechk_tim_prot_msb, self.__reg_modechk_tim_prot_lsb)
    @reg_modechk_tim_prot.setter
    def reg_modechk_tim_prot(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_modechk_tim_prot_msb, self.__reg_modechk_tim_prot_lsb, value)

    @property
    def reg_gain_upd_dis(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_upd_dis_msb, self.__reg_gain_upd_dis_lsb)
    @reg_gain_upd_dis.setter
    def reg_gain_upd_dis(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_upd_dis_msb, self.__reg_gain_upd_dis_lsb, value)

    @property
    def reg_agc_done_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_done_force_msb, self.__reg_agc_done_force_lsb)
    @reg_agc_done_force.setter
    def reg_agc_done_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_done_force_msb, self.__reg_agc_done_force_lsb, value)

    @property
    def reg_fast_check(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fast_check_msb, self.__reg_fast_check_lsb)
    @reg_fast_check.setter
    def reg_fast_check(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fast_check_msb, self.__reg_fast_check_lsb, value)

    @property
    def reg_strong_check(self):
        return self.__MEM.rdm(self.__addr, self.__reg_strong_check_msb, self.__reg_strong_check_lsb)
    @reg_strong_check.setter
    def reg_strong_check(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_strong_check_msb, self.__reg_strong_check_lsb, value)

    @property
    def reg_pwr_check_wait_count(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_check_wait_count_msb, self.__reg_pwr_check_wait_count_lsb)
    @reg_pwr_check_wait_count.setter
    def reg_pwr_check_wait_count(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_check_wait_count_msb, self.__reg_pwr_check_wait_count_lsb, value)

    @property
    def reg_fir_dc_rm_time(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fir_dc_rm_time_msb, self.__reg_fir_dc_rm_time_lsb)
    @reg_fir_dc_rm_time.setter
    def reg_fir_dc_rm_time(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fir_dc_rm_time_msb, self.__reg_fir_dc_rm_time_lsb, value)

    @property
    def reg_rx_end_td_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_end_td_clr_msb, self.__reg_rx_end_td_clr_lsb)
    @reg_rx_end_td_clr.setter
    def reg_rx_end_td_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_end_td_clr_msb, self.__reg_rx_end_td_clr_lsb, value)

    @property
    def reg_measure_delay_b(self):
        return self.__MEM.rdm(self.__addr, self.__reg_measure_delay_b_msb, self.__reg_measure_delay_b_lsb)
    @reg_measure_delay_b.setter
    def reg_measure_delay_b(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_measure_delay_b_msb, self.__reg_measure_delay_b_lsb, value)

    @property
    def reg_measure_delay_a(self):
        return self.__MEM.rdm(self.__addr, self.__reg_measure_delay_a_msb, self.__reg_measure_delay_a_lsb)
    @reg_measure_delay_a.setter
    def reg_measure_delay_a(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_measure_delay_a_msb, self.__reg_measure_delay_a_lsb, value)

    @property
    def reg_measure_delay_ab(self):
        return self.__MEM.rdm(self.__addr, self.__reg_measure_delay_ab_msb, self.__reg_measure_delay_ab_lsb)
    @reg_measure_delay_ab.setter
    def reg_measure_delay_ab(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_measure_delay_ab_msb, self.__reg_measure_delay_ab_lsb, value)
class AGCMEM_CTRL1(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x3c
        self.__reg_agc_dcmem_clr_lsb = 20
        self.__reg_agc_dcmem_clr_msb = 20
        self.__reg_agc_dcmem_force_en_lsb = 19
        self.__reg_agc_dcmem_force_en_msb = 19
        self.__reg_agc_dcmem_wen_lsb = 18
        self.__reg_agc_dcmem_wen_msb = 18
        self.__reg_agc_dcmem_ren_lsb = 17
        self.__reg_agc_dcmem_ren_msb = 17
        self.__reg_agcmem_wen_lsb = 16
        self.__reg_agcmem_wen_msb = 16
        self.__reg_agcmem_waddr_lsb = 8
        self.__reg_agcmem_waddr_msb = 15
        self.__reg_agcmem_wbe_lsb = 0
        self.__reg_agcmem_wbe_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_agc_dcmem_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_dcmem_clr_msb, self.__reg_agc_dcmem_clr_lsb)
    @reg_agc_dcmem_clr.setter
    def reg_agc_dcmem_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_dcmem_clr_msb, self.__reg_agc_dcmem_clr_lsb, value)

    @property
    def reg_agc_dcmem_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_dcmem_force_en_msb, self.__reg_agc_dcmem_force_en_lsb)
    @reg_agc_dcmem_force_en.setter
    def reg_agc_dcmem_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_dcmem_force_en_msb, self.__reg_agc_dcmem_force_en_lsb, value)

    @property
    def reg_agc_dcmem_wen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_dcmem_wen_msb, self.__reg_agc_dcmem_wen_lsb)
    @reg_agc_dcmem_wen.setter
    def reg_agc_dcmem_wen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_dcmem_wen_msb, self.__reg_agc_dcmem_wen_lsb, value)

    @property
    def reg_agc_dcmem_ren(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_dcmem_ren_msb, self.__reg_agc_dcmem_ren_lsb)
    @reg_agc_dcmem_ren.setter
    def reg_agc_dcmem_ren(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_dcmem_ren_msb, self.__reg_agc_dcmem_ren_lsb, value)

    @property
    def reg_agcmem_wen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agcmem_wen_msb, self.__reg_agcmem_wen_lsb)
    @reg_agcmem_wen.setter
    def reg_agcmem_wen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agcmem_wen_msb, self.__reg_agcmem_wen_lsb, value)

    @property
    def reg_agcmem_waddr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agcmem_waddr_msb, self.__reg_agcmem_waddr_lsb)
    @reg_agcmem_waddr.setter
    def reg_agcmem_waddr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agcmem_waddr_msb, self.__reg_agcmem_waddr_lsb, value)

    @property
    def reg_agcmem_wbe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agcmem_wbe_msb, self.__reg_agcmem_wbe_lsb)
    @reg_agcmem_wbe.setter
    def reg_agcmem_wbe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agcmem_wbe_msb, self.__reg_agcmem_wbe_lsb, value)
class AGCMEM_CTRL2(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x40
        self.__reg_agcmem_wdata_lsb = 0
        self.__reg_agcmem_wdata_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_agcmem_wdata(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agcmem_wdata_msb, self.__reg_agcmem_wdata_lsb)
    @reg_agcmem_wdata.setter
    def reg_agcmem_wdata(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agcmem_wdata_msb, self.__reg_agcmem_wdata_lsb, value)
class AGC11B_CTRL1(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x44
        self.__reg_dagc_en_lsb = 25
        self.__reg_dagc_en_msb = 25
        self.__reg_ofdm_cck_judge_thr_lsb = 16
        self.__reg_ofdm_cck_judge_thr_msb = 24
        self.__reg_bcorr_snr_en_lsb = 15
        self.__reg_bcorr_snr_en_msb = 15
        self.__reg_bcorr_lt_ext_lsb = 14
        self.__reg_bcorr_lt_ext_msb = 14
        self.__reg_bcorr_pwr_thr_lsb = 8
        self.__reg_bcorr_pwr_thr_msb = 13
        self.__reg_bcorr_snr_thr_lsb = 0
        self.__reg_bcorr_snr_thr_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_dagc_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dagc_en_msb, self.__reg_dagc_en_lsb)
    @reg_dagc_en.setter
    def reg_dagc_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dagc_en_msb, self.__reg_dagc_en_lsb, value)

    @property
    def reg_ofdm_cck_judge_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ofdm_cck_judge_thr_msb, self.__reg_ofdm_cck_judge_thr_lsb)
    @reg_ofdm_cck_judge_thr.setter
    def reg_ofdm_cck_judge_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ofdm_cck_judge_thr_msb, self.__reg_ofdm_cck_judge_thr_lsb, value)

    @property
    def reg_bcorr_snr_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bcorr_snr_en_msb, self.__reg_bcorr_snr_en_lsb)
    @reg_bcorr_snr_en.setter
    def reg_bcorr_snr_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bcorr_snr_en_msb, self.__reg_bcorr_snr_en_lsb, value)

    @property
    def reg_bcorr_lt_ext(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bcorr_lt_ext_msb, self.__reg_bcorr_lt_ext_lsb)
    @reg_bcorr_lt_ext.setter
    def reg_bcorr_lt_ext(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bcorr_lt_ext_msb, self.__reg_bcorr_lt_ext_lsb, value)

    @property
    def reg_bcorr_pwr_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bcorr_pwr_thr_msb, self.__reg_bcorr_pwr_thr_lsb)
    @reg_bcorr_pwr_thr.setter
    def reg_bcorr_pwr_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bcorr_pwr_thr_msb, self.__reg_bcorr_pwr_thr_lsb, value)

    @property
    def reg_bcorr_snr_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bcorr_snr_thr_msb, self.__reg_bcorr_snr_thr_lsb)
    @reg_bcorr_snr_thr.setter
    def reg_bcorr_snr_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bcorr_snr_thr_msb, self.__reg_bcorr_snr_thr_lsb, value)
class AGC11B_CTRL2(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x48
        self.__reg_judge_cnt_lsb = 8
        self.__reg_judge_cnt_msb = 14
        self.__reg_pwr_11b_desired_lsb = 0
        self.__reg_pwr_11b_desired_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_judge_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_judge_cnt_msb, self.__reg_judge_cnt_lsb)
    @reg_judge_cnt.setter
    def reg_judge_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_judge_cnt_msb, self.__reg_judge_cnt_lsb, value)

    @property
    def reg_pwr_11b_desired(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_11b_desired_msb, self.__reg_pwr_11b_desired_lsb)
    @reg_pwr_11b_desired.setter
    def reg_pwr_11b_desired(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_11b_desired_msb, self.__reg_pwr_11b_desired_lsb, value)
class AGCRD1(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x4c
        self.__r_in_noise_cal_lsb = 24
        self.__r_in_noise_cal_msb = 24
        self.__r_adcpwr_sw_lsb = 16
        self.__r_adcpwr_sw_msb = 23
        self.__r_pwr_fir2_sw_lsb = 8
        self.__r_pwr_fir2_sw_msb = 15
        self.__r_pwr_fe_sw_lsb = 0
        self.__r_pwr_fe_sw_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def r_in_noise_cal(self):
        return self.__MEM.rdm(self.__addr, self.__r_in_noise_cal_msb, self.__r_in_noise_cal_lsb)
    @r_in_noise_cal.setter
    def r_in_noise_cal(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_in_noise_cal_msb, self.__r_in_noise_cal_lsb, value)

    @property
    def r_adcpwr_sw(self):
        return self.__MEM.rdm(self.__addr, self.__r_adcpwr_sw_msb, self.__r_adcpwr_sw_lsb)
    @r_adcpwr_sw.setter
    def r_adcpwr_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_adcpwr_sw_msb, self.__r_adcpwr_sw_lsb, value)

    @property
    def r_pwr_fir2_sw(self):
        return self.__MEM.rdm(self.__addr, self.__r_pwr_fir2_sw_msb, self.__r_pwr_fir2_sw_lsb)
    @r_pwr_fir2_sw.setter
    def r_pwr_fir2_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_pwr_fir2_sw_msb, self.__r_pwr_fir2_sw_lsb, value)

    @property
    def r_pwr_fe_sw(self):
        return self.__MEM.rdm(self.__addr, self.__r_pwr_fe_sw_msb, self.__r_pwr_fe_sw_lsb)
    @r_pwr_fe_sw.setter
    def r_pwr_fe_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_pwr_fe_sw_msb, self.__r_pwr_fe_sw_lsb, value)
class AGCRD2(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x50
        self.__rx_end_td_lsb = 30
        self.__rx_end_td_msb = 30
        self.__agc_dcmem_rdata_lsb = 10
        self.__agc_dcmem_rdata_msb = 29
        self.__noise_rssi_sw_lsb = 0
        self.__noise_rssi_sw_msb = 9
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rx_end_td(self):
        return self.__MEM.rdm(self.__addr, self.__rx_end_td_msb, self.__rx_end_td_lsb)
    @rx_end_td.setter
    def rx_end_td(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_end_td_msb, self.__rx_end_td_lsb, value)

    @property
    def agc_dcmem_rdata(self):
        return self.__MEM.rdm(self.__addr, self.__agc_dcmem_rdata_msb, self.__agc_dcmem_rdata_lsb)
    @agc_dcmem_rdata.setter
    def agc_dcmem_rdata(self, value):
        return self.__MEM.wrm(self.__addr, self.__agc_dcmem_rdata_msb, self.__agc_dcmem_rdata_lsb, value)

    @property
    def noise_rssi_sw(self):
        return self.__MEM.rdm(self.__addr, self.__noise_rssi_sw_msb, self.__noise_rssi_sw_lsb)
    @noise_rssi_sw.setter
    def noise_rssi_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__noise_rssi_sw_msb, self.__noise_rssi_sw_lsb, value)
class AGCOFDM_CTRL5(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x54
        self.__reg_use_self_corr_2_lsb = 31
        self.__reg_use_self_corr_2_msb = 31
        self.__reg_corr_det_cnt_max_2_lsb = 24
        self.__reg_corr_det_cnt_max_2_msb = 30
        self.__reg_quick_ofdm_thr_lsb = 16
        self.__reg_quick_ofdm_thr_msb = 23
        self.__reg_quick_ofdm_en_lsb = 15
        self.__reg_quick_ofdm_en_msb = 15
        self.__reg_week_rssi_sc_thr_2_lsb = 7
        self.__reg_week_rssi_sc_thr_2_msb = 14
        self.__reg_corr_start_cnt_lsb = 0
        self.__reg_corr_start_cnt_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_use_self_corr_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_use_self_corr_2_msb, self.__reg_use_self_corr_2_lsb)
    @reg_use_self_corr_2.setter
    def reg_use_self_corr_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_use_self_corr_2_msb, self.__reg_use_self_corr_2_lsb, value)

    @property
    def reg_corr_det_cnt_max_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_det_cnt_max_2_msb, self.__reg_corr_det_cnt_max_2_lsb)
    @reg_corr_det_cnt_max_2.setter
    def reg_corr_det_cnt_max_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_det_cnt_max_2_msb, self.__reg_corr_det_cnt_max_2_lsb, value)

    @property
    def reg_quick_ofdm_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_quick_ofdm_thr_msb, self.__reg_quick_ofdm_thr_lsb)
    @reg_quick_ofdm_thr.setter
    def reg_quick_ofdm_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_quick_ofdm_thr_msb, self.__reg_quick_ofdm_thr_lsb, value)

    @property
    def reg_quick_ofdm_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_quick_ofdm_en_msb, self.__reg_quick_ofdm_en_lsb)
    @reg_quick_ofdm_en.setter
    def reg_quick_ofdm_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_quick_ofdm_en_msb, self.__reg_quick_ofdm_en_lsb, value)

    @property
    def reg_week_rssi_sc_thr_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_week_rssi_sc_thr_2_msb, self.__reg_week_rssi_sc_thr_2_lsb)
    @reg_week_rssi_sc_thr_2.setter
    def reg_week_rssi_sc_thr_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_week_rssi_sc_thr_2_msb, self.__reg_week_rssi_sc_thr_2_lsb, value)

    @property
    def reg_corr_start_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_start_cnt_msb, self.__reg_corr_start_cnt_lsb)
    @reg_corr_start_cnt.setter
    def reg_corr_start_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_start_cnt_msb, self.__reg_corr_start_cnt_lsb, value)
class AGCPWR_CTRL8(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x58
        self.__reg_adcsat_dis_filt_lsb = 31
        self.__reg_adcsat_dis_filt_msb = 31
        self.__reg_pwr_fine_adc_lsb = 22
        self.__reg_pwr_fine_adc_msb = 30
        self.__reg_adcsat_rsta_en_bt_lsb = 21
        self.__reg_adcsat_rsta_en_bt_msb = 21
        self.__reg_adcsat_rsta_en_11b_lsb = 20
        self.__reg_adcsat_rsta_en_11b_msb = 20
        self.__reg_adcsat_rsta_en_lsb = 19
        self.__reg_adcsat_rsta_en_msb = 19
        self.__reg_pwr_fine_quick_lsb = 10
        self.__reg_pwr_fine_quick_msb = 18
        self.__reg_quick_tune_en_lsb = 9
        self.__reg_quick_tune_en_msb = 9
        self.__reg_quick_tune_thr_lsb = 0
        self.__reg_quick_tune_thr_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_adcsat_dis_filt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcsat_dis_filt_msb, self.__reg_adcsat_dis_filt_lsb)
    @reg_adcsat_dis_filt.setter
    def reg_adcsat_dis_filt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcsat_dis_filt_msb, self.__reg_adcsat_dis_filt_lsb, value)

    @property
    def reg_pwr_fine_adc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_adc_msb, self.__reg_pwr_fine_adc_lsb)
    @reg_pwr_fine_adc.setter
    def reg_pwr_fine_adc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_adc_msb, self.__reg_pwr_fine_adc_lsb, value)

    @property
    def reg_adcsat_rsta_en_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcsat_rsta_en_bt_msb, self.__reg_adcsat_rsta_en_bt_lsb)
    @reg_adcsat_rsta_en_bt.setter
    def reg_adcsat_rsta_en_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcsat_rsta_en_bt_msb, self.__reg_adcsat_rsta_en_bt_lsb, value)

    @property
    def reg_adcsat_rsta_en_11b(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcsat_rsta_en_11b_msb, self.__reg_adcsat_rsta_en_11b_lsb)
    @reg_adcsat_rsta_en_11b.setter
    def reg_adcsat_rsta_en_11b(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcsat_rsta_en_11b_msb, self.__reg_adcsat_rsta_en_11b_lsb, value)

    @property
    def reg_adcsat_rsta_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcsat_rsta_en_msb, self.__reg_adcsat_rsta_en_lsb)
    @reg_adcsat_rsta_en.setter
    def reg_adcsat_rsta_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcsat_rsta_en_msb, self.__reg_adcsat_rsta_en_lsb, value)

    @property
    def reg_pwr_fine_quick(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_quick_msb, self.__reg_pwr_fine_quick_lsb)
    @reg_pwr_fine_quick.setter
    def reg_pwr_fine_quick(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_quick_msb, self.__reg_pwr_fine_quick_lsb, value)

    @property
    def reg_quick_tune_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_quick_tune_en_msb, self.__reg_quick_tune_en_lsb)
    @reg_quick_tune_en.setter
    def reg_quick_tune_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_quick_tune_en_msb, self.__reg_quick_tune_en_lsb, value)

    @property
    def reg_quick_tune_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_quick_tune_thr_msb, self.__reg_quick_tune_thr_lsb)
    @reg_quick_tune_thr.setter
    def reg_quick_tune_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_quick_tune_thr_msb, self.__reg_quick_tune_thr_lsb, value)
class AGCGAIN_CTRL_1(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x5c
        self.__reg_dis_rfagc_sat_lsb = 29
        self.__reg_dis_rfagc_sat_msb = 29
        self.__reg_rfagc_fsm_rst_en_lsb = 28
        self.__reg_rfagc_fsm_rst_en_msb = 28
        self.__reg_rfagc_en_bt_lsb = 27
        self.__reg_rfagc_en_bt_msb = 27
        self.__reg_rfagc_en_lsb = 26
        self.__reg_rfagc_en_msb = 26
        self.__reg_rfagc_exit_upd_gain_lsb = 25
        self.__reg_rfagc_exit_upd_gain_msb = 25
        self.__reg_rfagc_rstb_auto_en_lsb = 24
        self.__reg_rfagc_rstb_auto_en_msb = 24
        self.__reg_rfagc_rstb_inv_lsb = 23
        self.__reg_rfagc_rstb_inv_msb = 23
        self.__reg_rfagc_lna_sat_inv_lsb = 22
        self.__reg_rfagc_lna_sat_inv_msb = 22
        self.__reg_rfagc_vga_sat_inv_lsb = 21
        self.__reg_rfagc_vga_sat_inv_msb = 21
        self.__reg_chk_gain_min_lsb = 20
        self.__reg_chk_gain_min_msb = 20
        self.__reg_rfagc_exit_rst_ana_lsb = 19
        self.__reg_rfagc_exit_rst_ana_msb = 19
        self.__reg_rf_agc_to_max_lsb = 0
        self.__reg_rf_agc_to_max_msb = 18
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_dis_rfagc_sat(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dis_rfagc_sat_msb, self.__reg_dis_rfagc_sat_lsb)
    @reg_dis_rfagc_sat.setter
    def reg_dis_rfagc_sat(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dis_rfagc_sat_msb, self.__reg_dis_rfagc_sat_lsb, value)

    @property
    def reg_rfagc_fsm_rst_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rfagc_fsm_rst_en_msb, self.__reg_rfagc_fsm_rst_en_lsb)
    @reg_rfagc_fsm_rst_en.setter
    def reg_rfagc_fsm_rst_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rfagc_fsm_rst_en_msb, self.__reg_rfagc_fsm_rst_en_lsb, value)

    @property
    def reg_rfagc_en_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rfagc_en_bt_msb, self.__reg_rfagc_en_bt_lsb)
    @reg_rfagc_en_bt.setter
    def reg_rfagc_en_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rfagc_en_bt_msb, self.__reg_rfagc_en_bt_lsb, value)

    @property
    def reg_rfagc_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rfagc_en_msb, self.__reg_rfagc_en_lsb)
    @reg_rfagc_en.setter
    def reg_rfagc_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rfagc_en_msb, self.__reg_rfagc_en_lsb, value)

    @property
    def reg_rfagc_exit_upd_gain(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rfagc_exit_upd_gain_msb, self.__reg_rfagc_exit_upd_gain_lsb)
    @reg_rfagc_exit_upd_gain.setter
    def reg_rfagc_exit_upd_gain(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rfagc_exit_upd_gain_msb, self.__reg_rfagc_exit_upd_gain_lsb, value)

    @property
    def reg_rfagc_rstb_auto_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rfagc_rstb_auto_en_msb, self.__reg_rfagc_rstb_auto_en_lsb)
    @reg_rfagc_rstb_auto_en.setter
    def reg_rfagc_rstb_auto_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rfagc_rstb_auto_en_msb, self.__reg_rfagc_rstb_auto_en_lsb, value)

    @property
    def reg_rfagc_rstb_inv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rfagc_rstb_inv_msb, self.__reg_rfagc_rstb_inv_lsb)
    @reg_rfagc_rstb_inv.setter
    def reg_rfagc_rstb_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rfagc_rstb_inv_msb, self.__reg_rfagc_rstb_inv_lsb, value)

    @property
    def reg_rfagc_lna_sat_inv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rfagc_lna_sat_inv_msb, self.__reg_rfagc_lna_sat_inv_lsb)
    @reg_rfagc_lna_sat_inv.setter
    def reg_rfagc_lna_sat_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rfagc_lna_sat_inv_msb, self.__reg_rfagc_lna_sat_inv_lsb, value)

    @property
    def reg_rfagc_vga_sat_inv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rfagc_vga_sat_inv_msb, self.__reg_rfagc_vga_sat_inv_lsb)
    @reg_rfagc_vga_sat_inv.setter
    def reg_rfagc_vga_sat_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rfagc_vga_sat_inv_msb, self.__reg_rfagc_vga_sat_inv_lsb, value)

    @property
    def reg_chk_gain_min(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chk_gain_min_msb, self.__reg_chk_gain_min_lsb)
    @reg_chk_gain_min.setter
    def reg_chk_gain_min(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chk_gain_min_msb, self.__reg_chk_gain_min_lsb, value)

    @property
    def reg_rfagc_exit_rst_ana(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rfagc_exit_rst_ana_msb, self.__reg_rfagc_exit_rst_ana_lsb)
    @reg_rfagc_exit_rst_ana.setter
    def reg_rfagc_exit_rst_ana(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rfagc_exit_rst_ana_msb, self.__reg_rfagc_exit_rst_ana_lsb, value)

    @property
    def reg_rf_agc_to_max(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rf_agc_to_max_msb, self.__reg_rf_agc_to_max_lsb)
    @reg_rf_agc_to_max.setter
    def reg_rf_agc_to_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rf_agc_to_max_msb, self.__reg_rf_agc_to_max_lsb, value)
class AGCGAIN_CTRL_2(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x60
        self.__reg_gain_gt_4_bt_lsb = 24
        self.__reg_gain_gt_4_bt_msb = 30
        self.__reg_gain_gt_3_bt_lsb = 16
        self.__reg_gain_gt_3_bt_msb = 22
        self.__reg_gain_gt_2_bt_lsb = 8
        self.__reg_gain_gt_2_bt_msb = 14
        self.__reg_gain_gt_1_bt_lsb = 0
        self.__reg_gain_gt_1_bt_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_gain_gt_4_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_gt_4_bt_msb, self.__reg_gain_gt_4_bt_lsb)
    @reg_gain_gt_4_bt.setter
    def reg_gain_gt_4_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_gt_4_bt_msb, self.__reg_gain_gt_4_bt_lsb, value)

    @property
    def reg_gain_gt_3_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_gt_3_bt_msb, self.__reg_gain_gt_3_bt_lsb)
    @reg_gain_gt_3_bt.setter
    def reg_gain_gt_3_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_gt_3_bt_msb, self.__reg_gain_gt_3_bt_lsb, value)

    @property
    def reg_gain_gt_2_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_gt_2_bt_msb, self.__reg_gain_gt_2_bt_lsb)
    @reg_gain_gt_2_bt.setter
    def reg_gain_gt_2_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_gt_2_bt_msb, self.__reg_gain_gt_2_bt_lsb, value)

    @property
    def reg_gain_gt_1_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_gt_1_bt_msb, self.__reg_gain_gt_1_bt_lsb)
    @reg_gain_gt_1_bt.setter
    def reg_gain_gt_1_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_gt_1_bt_msb, self.__reg_gain_gt_1_bt_lsb, value)
class AGCGAIN_CTRL_3(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x64
        self.__reg_gain_gt_4_lsb = 24
        self.__reg_gain_gt_4_msb = 30
        self.__reg_gain_gt_3_lsb = 16
        self.__reg_gain_gt_3_msb = 22
        self.__reg_gain_gt_2_lsb = 8
        self.__reg_gain_gt_2_msb = 14
        self.__reg_gain_gt_1_lsb = 0
        self.__reg_gain_gt_1_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_gain_gt_4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_gt_4_msb, self.__reg_gain_gt_4_lsb)
    @reg_gain_gt_4.setter
    def reg_gain_gt_4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_gt_4_msb, self.__reg_gain_gt_4_lsb, value)

    @property
    def reg_gain_gt_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_gt_3_msb, self.__reg_gain_gt_3_lsb)
    @reg_gain_gt_3.setter
    def reg_gain_gt_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_gt_3_msb, self.__reg_gain_gt_3_lsb, value)

    @property
    def reg_gain_gt_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_gt_2_msb, self.__reg_gain_gt_2_lsb)
    @reg_gain_gt_2.setter
    def reg_gain_gt_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_gt_2_msb, self.__reg_gain_gt_2_lsb, value)

    @property
    def reg_gain_gt_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_gt_1_msb, self.__reg_gain_gt_1_lsb)
    @reg_gain_gt_1.setter
    def reg_gain_gt_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_gt_1_msb, self.__reg_gain_gt_1_lsb, value)
class AGCPKDET_CTRL_0(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x68
        self.__reg_pkdet_ctrl_lsb = 0
        self.__reg_pkdet_ctrl_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_pkdet_ctrl(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pkdet_ctrl_msb, self.__reg_pkdet_ctrl_lsb)
    @reg_pkdet_ctrl.setter
    def reg_pkdet_ctrl(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pkdet_ctrl_msb, self.__reg_pkdet_ctrl_lsb, value)
class AGCRD9(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x6c
        self.__r_fine_gain_sat_lsb = 24
        self.__r_fine_gain_sat_msb = 24
        self.__r_rx_gain_2nd_sw_lsb = 16
        self.__r_rx_gain_2nd_sw_msb = 23
        self.__r_sigrssi_sw_lsb = 8
        self.__r_sigrssi_sw_msb = 15
        self.__r_rx_gain_sw_lsb = 0
        self.__r_rx_gain_sw_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def r_fine_gain_sat(self):
        return self.__MEM.rdm(self.__addr, self.__r_fine_gain_sat_msb, self.__r_fine_gain_sat_lsb)
    @r_fine_gain_sat.setter
    def r_fine_gain_sat(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_fine_gain_sat_msb, self.__r_fine_gain_sat_lsb, value)

    @property
    def r_rx_gain_2nd_sw(self):
        return self.__MEM.rdm(self.__addr, self.__r_rx_gain_2nd_sw_msb, self.__r_rx_gain_2nd_sw_lsb)
    @r_rx_gain_2nd_sw.setter
    def r_rx_gain_2nd_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_rx_gain_2nd_sw_msb, self.__r_rx_gain_2nd_sw_lsb, value)

    @property
    def r_sigrssi_sw(self):
        return self.__MEM.rdm(self.__addr, self.__r_sigrssi_sw_msb, self.__r_sigrssi_sw_lsb)
    @r_sigrssi_sw.setter
    def r_sigrssi_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_sigrssi_sw_msb, self.__r_sigrssi_sw_lsb, value)

    @property
    def r_rx_gain_sw(self):
        return self.__MEM.rdm(self.__addr, self.__r_rx_gain_sw_msb, self.__r_rx_gain_sw_lsb)
    @r_rx_gain_sw.setter
    def r_rx_gain_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_rx_gain_sw_msb, self.__r_rx_gain_sw_lsb, value)
class AGCOFDM_CTRL6(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x70
        self.__reg_week_rssi_cfo_thr_lsb = 24
        self.__reg_week_rssi_cfo_thr_msb = 31
        self.__reg_week_rssi_sc_thr_lsb = 16
        self.__reg_week_rssi_sc_thr_msb = 23
        self.__reg_ocorr_lt_rssi_thr_2_lsb = 8
        self.__reg_ocorr_lt_rssi_thr_2_msb = 15
        self.__reg_week_rssi_xc_thr_lsb = 0
        self.__reg_week_rssi_xc_thr_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_week_rssi_cfo_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_week_rssi_cfo_thr_msb, self.__reg_week_rssi_cfo_thr_lsb)
    @reg_week_rssi_cfo_thr.setter
    def reg_week_rssi_cfo_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_week_rssi_cfo_thr_msb, self.__reg_week_rssi_cfo_thr_lsb, value)

    @property
    def reg_week_rssi_sc_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_week_rssi_sc_thr_msb, self.__reg_week_rssi_sc_thr_lsb)
    @reg_week_rssi_sc_thr.setter
    def reg_week_rssi_sc_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_week_rssi_sc_thr_msb, self.__reg_week_rssi_sc_thr_lsb, value)

    @property
    def reg_ocorr_lt_rssi_thr_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ocorr_lt_rssi_thr_2_msb, self.__reg_ocorr_lt_rssi_thr_2_lsb)
    @reg_ocorr_lt_rssi_thr_2.setter
    def reg_ocorr_lt_rssi_thr_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ocorr_lt_rssi_thr_2_msb, self.__reg_ocorr_lt_rssi_thr_2_lsb, value)

    @property
    def reg_week_rssi_xc_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_week_rssi_xc_thr_msb, self.__reg_week_rssi_xc_thr_lsb)
    @reg_week_rssi_xc_thr.setter
    def reg_week_rssi_xc_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_week_rssi_xc_thr_msb, self.__reg_week_rssi_xc_thr_lsb, value)
class AGCFSM_CTRL4(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x74
        self.__reg_rx11n_hbw_thr_lsb = 28
        self.__reg_rx11n_hbw_thr_msb = 30
        self.__reg_rssi_weak_11a_latch_lsb = 27
        self.__reg_rssi_weak_11a_latch_msb = 27
        self.__reg_rssi_weak_latch_lsb = 26
        self.__reg_rssi_weak_latch_msb = 26
        self.__reg_rssi_weak_ant_opt_11a_lsb = 25
        self.__reg_rssi_weak_ant_opt_11a_msb = 25
        self.__reg_rssi_weak_ant_opt_lsb = 24
        self.__reg_rssi_weak_ant_opt_msb = 24
        self.__reg_find_dis_rssi_upd_lsb = 23
        self.__reg_find_dis_rssi_upd_msb = 23
        self.__reg_force_cca_sec_lsb = 22
        self.__reg_force_cca_sec_msb = 22
        self.__reg_force_cca_sec_en_lsb = 21
        self.__reg_force_cca_sec_en_msb = 21
        self.__reg_force_cca_lsb = 20
        self.__reg_force_cca_msb = 20
        self.__reg_force_cca_en_lsb = 19
        self.__reg_force_cca_en_msb = 19
        self.__reg_agc_dis_cca_lsb = 18
        self.__reg_agc_dis_cca_msb = 18
        self.__reg_gain_tune_max_lsb = 15
        self.__reg_gain_tune_max_msb = 17
        self.__reg_2nd_use_init_dc_lsb = 14
        self.__reg_2nd_use_init_dc_msb = 14
        self.__reg_chan_merge_dis_lsb = 13
        self.__reg_chan_merge_dis_msb = 13
        self.__reg_agc_corr_dis_lsb = 12
        self.__reg_agc_corr_dis_msb = 12
        self.__reg_fine_2nd_cnt_lsb = 9
        self.__reg_fine_2nd_cnt_msb = 11
        self.__reg_pwr_vote_1st_lsb = 8
        self.__reg_pwr_vote_1st_msb = 8
        self.__reg_gain_same_en_lsb = 7
        self.__reg_gain_same_en_msb = 7
        self.__reg_settling_2_time_lsb = 0
        self.__reg_settling_2_time_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rx11n_hbw_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx11n_hbw_thr_msb, self.__reg_rx11n_hbw_thr_lsb)
    @reg_rx11n_hbw_thr.setter
    def reg_rx11n_hbw_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx11n_hbw_thr_msb, self.__reg_rx11n_hbw_thr_lsb, value)

    @property
    def reg_rssi_weak_11a_latch(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rssi_weak_11a_latch_msb, self.__reg_rssi_weak_11a_latch_lsb)
    @reg_rssi_weak_11a_latch.setter
    def reg_rssi_weak_11a_latch(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rssi_weak_11a_latch_msb, self.__reg_rssi_weak_11a_latch_lsb, value)

    @property
    def reg_rssi_weak_latch(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rssi_weak_latch_msb, self.__reg_rssi_weak_latch_lsb)
    @reg_rssi_weak_latch.setter
    def reg_rssi_weak_latch(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rssi_weak_latch_msb, self.__reg_rssi_weak_latch_lsb, value)

    @property
    def reg_rssi_weak_ant_opt_11a(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rssi_weak_ant_opt_11a_msb, self.__reg_rssi_weak_ant_opt_11a_lsb)
    @reg_rssi_weak_ant_opt_11a.setter
    def reg_rssi_weak_ant_opt_11a(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rssi_weak_ant_opt_11a_msb, self.__reg_rssi_weak_ant_opt_11a_lsb, value)

    @property
    def reg_rssi_weak_ant_opt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rssi_weak_ant_opt_msb, self.__reg_rssi_weak_ant_opt_lsb)
    @reg_rssi_weak_ant_opt.setter
    def reg_rssi_weak_ant_opt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rssi_weak_ant_opt_msb, self.__reg_rssi_weak_ant_opt_lsb, value)

    @property
    def reg_find_dis_rssi_upd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_find_dis_rssi_upd_msb, self.__reg_find_dis_rssi_upd_lsb)
    @reg_find_dis_rssi_upd.setter
    def reg_find_dis_rssi_upd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_find_dis_rssi_upd_msb, self.__reg_find_dis_rssi_upd_lsb, value)

    @property
    def reg_force_cca_sec(self):
        return self.__MEM.rdm(self.__addr, self.__reg_force_cca_sec_msb, self.__reg_force_cca_sec_lsb)
    @reg_force_cca_sec.setter
    def reg_force_cca_sec(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_force_cca_sec_msb, self.__reg_force_cca_sec_lsb, value)

    @property
    def reg_force_cca_sec_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_force_cca_sec_en_msb, self.__reg_force_cca_sec_en_lsb)
    @reg_force_cca_sec_en.setter
    def reg_force_cca_sec_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_force_cca_sec_en_msb, self.__reg_force_cca_sec_en_lsb, value)

    @property
    def reg_force_cca(self):
        return self.__MEM.rdm(self.__addr, self.__reg_force_cca_msb, self.__reg_force_cca_lsb)
    @reg_force_cca.setter
    def reg_force_cca(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_force_cca_msb, self.__reg_force_cca_lsb, value)

    @property
    def reg_force_cca_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_force_cca_en_msb, self.__reg_force_cca_en_lsb)
    @reg_force_cca_en.setter
    def reg_force_cca_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_force_cca_en_msb, self.__reg_force_cca_en_lsb, value)

    @property
    def reg_agc_dis_cca(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_dis_cca_msb, self.__reg_agc_dis_cca_lsb)
    @reg_agc_dis_cca.setter
    def reg_agc_dis_cca(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_dis_cca_msb, self.__reg_agc_dis_cca_lsb, value)

    @property
    def reg_gain_tune_max(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_tune_max_msb, self.__reg_gain_tune_max_lsb)
    @reg_gain_tune_max.setter
    def reg_gain_tune_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_tune_max_msb, self.__reg_gain_tune_max_lsb, value)

    @property
    def reg_2nd_use_init_dc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_2nd_use_init_dc_msb, self.__reg_2nd_use_init_dc_lsb)
    @reg_2nd_use_init_dc.setter
    def reg_2nd_use_init_dc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_2nd_use_init_dc_msb, self.__reg_2nd_use_init_dc_lsb, value)

    @property
    def reg_chan_merge_dis(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chan_merge_dis_msb, self.__reg_chan_merge_dis_lsb)
    @reg_chan_merge_dis.setter
    def reg_chan_merge_dis(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chan_merge_dis_msb, self.__reg_chan_merge_dis_lsb, value)

    @property
    def reg_agc_corr_dis(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_corr_dis_msb, self.__reg_agc_corr_dis_lsb)
    @reg_agc_corr_dis.setter
    def reg_agc_corr_dis(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_corr_dis_msb, self.__reg_agc_corr_dis_lsb, value)

    @property
    def reg_fine_2nd_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fine_2nd_cnt_msb, self.__reg_fine_2nd_cnt_lsb)
    @reg_fine_2nd_cnt.setter
    def reg_fine_2nd_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fine_2nd_cnt_msb, self.__reg_fine_2nd_cnt_lsb, value)

    @property
    def reg_pwr_vote_1st(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_vote_1st_msb, self.__reg_pwr_vote_1st_lsb)
    @reg_pwr_vote_1st.setter
    def reg_pwr_vote_1st(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_vote_1st_msb, self.__reg_pwr_vote_1st_lsb, value)

    @property
    def reg_gain_same_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_same_en_msb, self.__reg_gain_same_en_lsb)
    @reg_gain_same_en.setter
    def reg_gain_same_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_same_en_msb, self.__reg_gain_same_en_lsb, value)

    @property
    def reg_settling_2_time(self):
        return self.__MEM.rdm(self.__addr, self.__reg_settling_2_time_msb, self.__reg_settling_2_time_lsb)
    @reg_settling_2_time.setter
    def reg_settling_2_time(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_settling_2_time_msb, self.__reg_settling_2_time_lsb, value)
class AGCRD3(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x78
        self.__bb_diag_0_lsb = 16
        self.__bb_diag_0_msb = 31
        self.__agc_state_lsb = 8
        self.__agc_state_msb = 11
        self.__rx_gain_lsb = 0
        self.__rx_gain_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def bb_diag_0(self):
        return self.__MEM.rdm(self.__addr, self.__bb_diag_0_msb, self.__bb_diag_0_lsb)
    @bb_diag_0.setter
    def bb_diag_0(self, value):
        return self.__MEM.wrm(self.__addr, self.__bb_diag_0_msb, self.__bb_diag_0_lsb, value)

    @property
    def agc_state(self):
        return self.__MEM.rdm(self.__addr, self.__agc_state_msb, self.__agc_state_lsb)
    @agc_state.setter
    def agc_state(self, value):
        return self.__MEM.wrm(self.__addr, self.__agc_state_msb, self.__agc_state_lsb, value)

    @property
    def rx_gain(self):
        return self.__MEM.rdm(self.__addr, self.__rx_gain_msb, self.__rx_gain_lsb)
    @rx_gain.setter
    def rx_gain(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_gain_msb, self.__rx_gain_lsb, value)
class AGCBT_CTRL0(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x7c
        self.__reg_bt_gain_min_restart_en_lsb = 31
        self.__reg_bt_gain_min_restart_en_msb = 31
        self.__reg_bt_gain_max_restart_en_lsb = 30
        self.__reg_bt_gain_max_restart_en_msb = 30
        self.__reg_bt_rxpwr_cmp_sel_lsb = 28
        self.__reg_bt_rxpwr_cmp_sel_msb = 29
        self.__reg_bt_rxpwr_var_thr_lsb = 24
        self.__reg_bt_rxpwr_var_thr_msb = 27
        self.__reg_bt_rssi_thr_lsb = 16
        self.__reg_bt_rssi_thr_msb = 23
        self.__reg_bt_pwdet_v_cnt_lsb = 8
        self.__reg_bt_pwdet_v_cnt_msb = 15
        self.__reg_bt_pwdet_s_cnt_lsb = 0
        self.__reg_bt_pwdet_s_cnt_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bt_gain_min_restart_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bt_gain_min_restart_en_msb, self.__reg_bt_gain_min_restart_en_lsb)
    @reg_bt_gain_min_restart_en.setter
    def reg_bt_gain_min_restart_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bt_gain_min_restart_en_msb, self.__reg_bt_gain_min_restart_en_lsb, value)

    @property
    def reg_bt_gain_max_restart_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bt_gain_max_restart_en_msb, self.__reg_bt_gain_max_restart_en_lsb)
    @reg_bt_gain_max_restart_en.setter
    def reg_bt_gain_max_restart_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bt_gain_max_restart_en_msb, self.__reg_bt_gain_max_restart_en_lsb, value)

    @property
    def reg_bt_rxpwr_cmp_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bt_rxpwr_cmp_sel_msb, self.__reg_bt_rxpwr_cmp_sel_lsb)
    @reg_bt_rxpwr_cmp_sel.setter
    def reg_bt_rxpwr_cmp_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bt_rxpwr_cmp_sel_msb, self.__reg_bt_rxpwr_cmp_sel_lsb, value)

    @property
    def reg_bt_rxpwr_var_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bt_rxpwr_var_thr_msb, self.__reg_bt_rxpwr_var_thr_lsb)
    @reg_bt_rxpwr_var_thr.setter
    def reg_bt_rxpwr_var_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bt_rxpwr_var_thr_msb, self.__reg_bt_rxpwr_var_thr_lsb, value)

    @property
    def reg_bt_rssi_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bt_rssi_thr_msb, self.__reg_bt_rssi_thr_lsb)
    @reg_bt_rssi_thr.setter
    def reg_bt_rssi_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bt_rssi_thr_msb, self.__reg_bt_rssi_thr_lsb, value)

    @property
    def reg_bt_pwdet_v_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bt_pwdet_v_cnt_msb, self.__reg_bt_pwdet_v_cnt_lsb)
    @reg_bt_pwdet_v_cnt.setter
    def reg_bt_pwdet_v_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bt_pwdet_v_cnt_msb, self.__reg_bt_pwdet_v_cnt_lsb, value)

    @property
    def reg_bt_pwdet_s_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bt_pwdet_s_cnt_msb, self.__reg_bt_pwdet_s_cnt_lsb)
    @reg_bt_pwdet_s_cnt.setter
    def reg_bt_pwdet_s_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bt_pwdet_s_cnt_msb, self.__reg_bt_pwdet_s_cnt_lsb, value)
class AGCBT_CTRL1(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x80
        self.__reg_gain_tune_min_bt_lsb = 29
        self.__reg_gain_tune_min_bt_msb = 31
        self.__reg_bt_pwr_ofs_lsb = 23
        self.__reg_bt_pwr_ofs_msb = 28
        self.__reg_pwr_fine_2nd_ofs_bt_lsb = 17
        self.__reg_pwr_fine_2nd_ofs_bt_msb = 22
        self.__reg_pwr_fine_1st_bt_lsb = 8
        self.__reg_pwr_fine_1st_bt_msb = 16
        self.__reg_force_bt_mode_lsb = 6
        self.__reg_force_bt_mode_msb = 7
        self.__reg_bt_rxpwr_chk_s_lsb = 1
        self.__reg_bt_rxpwr_chk_s_msb = 5
        self.__reg_force_bb_off_lsb = 0
        self.__reg_force_bb_off_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_gain_tune_min_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_tune_min_bt_msb, self.__reg_gain_tune_min_bt_lsb)
    @reg_gain_tune_min_bt.setter
    def reg_gain_tune_min_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_tune_min_bt_msb, self.__reg_gain_tune_min_bt_lsb, value)

    @property
    def reg_bt_pwr_ofs(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bt_pwr_ofs_msb, self.__reg_bt_pwr_ofs_lsb)
    @reg_bt_pwr_ofs.setter
    def reg_bt_pwr_ofs(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bt_pwr_ofs_msb, self.__reg_bt_pwr_ofs_lsb, value)

    @property
    def reg_pwr_fine_2nd_ofs_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_2nd_ofs_bt_msb, self.__reg_pwr_fine_2nd_ofs_bt_lsb)
    @reg_pwr_fine_2nd_ofs_bt.setter
    def reg_pwr_fine_2nd_ofs_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_2nd_ofs_bt_msb, self.__reg_pwr_fine_2nd_ofs_bt_lsb, value)

    @property
    def reg_pwr_fine_1st_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_1st_bt_msb, self.__reg_pwr_fine_1st_bt_lsb)
    @reg_pwr_fine_1st_bt.setter
    def reg_pwr_fine_1st_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_1st_bt_msb, self.__reg_pwr_fine_1st_bt_lsb, value)

    @property
    def reg_force_bt_mode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_force_bt_mode_msb, self.__reg_force_bt_mode_lsb)
    @reg_force_bt_mode.setter
    def reg_force_bt_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_force_bt_mode_msb, self.__reg_force_bt_mode_lsb, value)

    @property
    def reg_bt_rxpwr_chk_s(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bt_rxpwr_chk_s_msb, self.__reg_bt_rxpwr_chk_s_lsb)
    @reg_bt_rxpwr_chk_s.setter
    def reg_bt_rxpwr_chk_s(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bt_rxpwr_chk_s_msb, self.__reg_bt_rxpwr_chk_s_lsb, value)

    @property
    def reg_force_bb_off(self):
        return self.__MEM.rdm(self.__addr, self.__reg_force_bb_off_msb, self.__reg_force_bb_off_lsb)
    @reg_force_bb_off.setter
    def reg_force_bb_off(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_force_bb_off_msb, self.__reg_force_bb_off_lsb, value)
class AGCBT_CTRL2(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x84
        self.__reg_bt_gain_maxmin_recorrect_en_lsb = 31
        self.__reg_bt_gain_maxmin_recorrect_en_msb = 31
        self.__reg_pwr_fine_recorrect_inf_bt_lsb = 30
        self.__reg_pwr_fine_recorrect_inf_bt_msb = 30
        self.__reg_pwr_restart_ref_sel_bt_lsb = 29
        self.__reg_pwr_restart_ref_sel_bt_msb = 29
        self.__reg_pwr_fine_recorrect_en_le_lsb = 28
        self.__reg_pwr_fine_recorrect_en_le_msb = 28
        self.__reg_pwr_fine_recorrect_en_bt_lsb = 27
        self.__reg_pwr_fine_recorrect_en_bt_msb = 27
        self.__reg_pwr_fine_recorrect_thr_bt_lsb = 22
        self.__reg_pwr_fine_recorrect_thr_bt_msb = 26
        self.__reg_pwr_risedrop_bt_error_en_lsb = 21
        self.__reg_pwr_risedrop_bt_error_en_msb = 21
        self.__reg_pwr_drop_thr_bt_error_lsb = 15
        self.__reg_pwr_drop_thr_bt_error_msb = 20
        self.__reg_pwr_restart_thr_bt_error_lsb = 9
        self.__reg_pwr_restart_thr_bt_error_msb = 14
        self.__reg_bt_pwr_fine_adc_lsb = 0
        self.__reg_bt_pwr_fine_adc_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bt_gain_maxmin_recorrect_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bt_gain_maxmin_recorrect_en_msb, self.__reg_bt_gain_maxmin_recorrect_en_lsb)
    @reg_bt_gain_maxmin_recorrect_en.setter
    def reg_bt_gain_maxmin_recorrect_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bt_gain_maxmin_recorrect_en_msb, self.__reg_bt_gain_maxmin_recorrect_en_lsb, value)

    @property
    def reg_pwr_fine_recorrect_inf_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_recorrect_inf_bt_msb, self.__reg_pwr_fine_recorrect_inf_bt_lsb)
    @reg_pwr_fine_recorrect_inf_bt.setter
    def reg_pwr_fine_recorrect_inf_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_recorrect_inf_bt_msb, self.__reg_pwr_fine_recorrect_inf_bt_lsb, value)

    @property
    def reg_pwr_restart_ref_sel_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_restart_ref_sel_bt_msb, self.__reg_pwr_restart_ref_sel_bt_lsb)
    @reg_pwr_restart_ref_sel_bt.setter
    def reg_pwr_restart_ref_sel_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_restart_ref_sel_bt_msb, self.__reg_pwr_restart_ref_sel_bt_lsb, value)

    @property
    def reg_pwr_fine_recorrect_en_le(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_recorrect_en_le_msb, self.__reg_pwr_fine_recorrect_en_le_lsb)
    @reg_pwr_fine_recorrect_en_le.setter
    def reg_pwr_fine_recorrect_en_le(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_recorrect_en_le_msb, self.__reg_pwr_fine_recorrect_en_le_lsb, value)

    @property
    def reg_pwr_fine_recorrect_en_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_recorrect_en_bt_msb, self.__reg_pwr_fine_recorrect_en_bt_lsb)
    @reg_pwr_fine_recorrect_en_bt.setter
    def reg_pwr_fine_recorrect_en_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_recorrect_en_bt_msb, self.__reg_pwr_fine_recorrect_en_bt_lsb, value)

    @property
    def reg_pwr_fine_recorrect_thr_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_recorrect_thr_bt_msb, self.__reg_pwr_fine_recorrect_thr_bt_lsb)
    @reg_pwr_fine_recorrect_thr_bt.setter
    def reg_pwr_fine_recorrect_thr_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_recorrect_thr_bt_msb, self.__reg_pwr_fine_recorrect_thr_bt_lsb, value)

    @property
    def reg_pwr_risedrop_bt_error_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_risedrop_bt_error_en_msb, self.__reg_pwr_risedrop_bt_error_en_lsb)
    @reg_pwr_risedrop_bt_error_en.setter
    def reg_pwr_risedrop_bt_error_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_risedrop_bt_error_en_msb, self.__reg_pwr_risedrop_bt_error_en_lsb, value)

    @property
    def reg_pwr_drop_thr_bt_error(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_drop_thr_bt_error_msb, self.__reg_pwr_drop_thr_bt_error_lsb)
    @reg_pwr_drop_thr_bt_error.setter
    def reg_pwr_drop_thr_bt_error(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_drop_thr_bt_error_msb, self.__reg_pwr_drop_thr_bt_error_lsb, value)

    @property
    def reg_pwr_restart_thr_bt_error(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_restart_thr_bt_error_msb, self.__reg_pwr_restart_thr_bt_error_lsb)
    @reg_pwr_restart_thr_bt_error.setter
    def reg_pwr_restart_thr_bt_error(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_restart_thr_bt_error_msb, self.__reg_pwr_restart_thr_bt_error_lsb, value)

    @property
    def reg_bt_pwr_fine_adc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bt_pwr_fine_adc_msb, self.__reg_bt_pwr_fine_adc_lsb)
    @reg_bt_pwr_fine_adc.setter
    def reg_bt_pwr_fine_adc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bt_pwr_fine_adc_msb, self.__reg_bt_pwr_fine_adc_lsb, value)
class AGCHT2040_SCALE(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x88
        self.__reg_ht2040_scale_en_lsb = 8
        self.__reg_ht2040_scale_en_msb = 8
        self.__reg_agc_ht2040_scale_lsb = 0
        self.__reg_agc_ht2040_scale_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ht2040_scale_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ht2040_scale_en_msb, self.__reg_ht2040_scale_en_lsb)
    @reg_ht2040_scale_en.setter
    def reg_ht2040_scale_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ht2040_scale_en_msb, self.__reg_ht2040_scale_en_lsb, value)

    @property
    def reg_agc_ht2040_scale(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_ht2040_scale_msb, self.__reg_agc_ht2040_scale_lsb)
    @reg_agc_ht2040_scale.setter
    def reg_agc_ht2040_scale(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_ht2040_scale_msb, self.__reg_agc_ht2040_scale_lsb, value)
class AGCRD4(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x8c
        self.__r_gain_max_pkd_bt_cur_lsb = 19
        self.__r_gain_max_pkd_bt_cur_msb = 25
        self.__r_gain_max_pkd_cur_lsb = 12
        self.__r_gain_max_pkd_cur_msb = 18
        self.__noise_rssi_lsb = 0
        self.__noise_rssi_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def r_gain_max_pkd_bt_cur(self):
        return self.__MEM.rdm(self.__addr, self.__r_gain_max_pkd_bt_cur_msb, self.__r_gain_max_pkd_bt_cur_lsb)
    @r_gain_max_pkd_bt_cur.setter
    def r_gain_max_pkd_bt_cur(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_gain_max_pkd_bt_cur_msb, self.__r_gain_max_pkd_bt_cur_lsb, value)

    @property
    def r_gain_max_pkd_cur(self):
        return self.__MEM.rdm(self.__addr, self.__r_gain_max_pkd_cur_msb, self.__r_gain_max_pkd_cur_lsb)
    @r_gain_max_pkd_cur.setter
    def r_gain_max_pkd_cur(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_gain_max_pkd_cur_msb, self.__r_gain_max_pkd_cur_lsb, value)

    @property
    def noise_rssi(self):
        return self.__MEM.rdm(self.__addr, self.__noise_rssi_msb, self.__noise_rssi_lsb)
    @noise_rssi.setter
    def noise_rssi(self, value):
        return self.__MEM.wrm(self.__addr, self.__noise_rssi_msb, self.__noise_rssi_lsb, value)
class AGCPWR_CTRL9(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x90
        self.__reg_pwr_drop_thr_bt_lsb = 26
        self.__reg_pwr_drop_thr_bt_msb = 31
        self.__reg_pwr_restart_thr_bt_lsb = 20
        self.__reg_pwr_restart_thr_bt_msb = 25
        self.__reg_pwr_drop_thr_11b_lsb = 15
        self.__reg_pwr_drop_thr_11b_msb = 19
        self.__reg_pwr_restart_thr_11b_lsb = 10
        self.__reg_pwr_restart_thr_11b_msb = 14
        self.__reg_pwr_drop_thr_lsb = 5
        self.__reg_pwr_drop_thr_msb = 9
        self.__reg_pwr_restart_thr_lsb = 0
        self.__reg_pwr_restart_thr_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_pwr_drop_thr_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_drop_thr_bt_msb, self.__reg_pwr_drop_thr_bt_lsb)
    @reg_pwr_drop_thr_bt.setter
    def reg_pwr_drop_thr_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_drop_thr_bt_msb, self.__reg_pwr_drop_thr_bt_lsb, value)

    @property
    def reg_pwr_restart_thr_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_restart_thr_bt_msb, self.__reg_pwr_restart_thr_bt_lsb)
    @reg_pwr_restart_thr_bt.setter
    def reg_pwr_restart_thr_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_restart_thr_bt_msb, self.__reg_pwr_restart_thr_bt_lsb, value)

    @property
    def reg_pwr_drop_thr_11b(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_drop_thr_11b_msb, self.__reg_pwr_drop_thr_11b_lsb)
    @reg_pwr_drop_thr_11b.setter
    def reg_pwr_drop_thr_11b(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_drop_thr_11b_msb, self.__reg_pwr_drop_thr_11b_lsb, value)

    @property
    def reg_pwr_restart_thr_11b(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_restart_thr_11b_msb, self.__reg_pwr_restart_thr_11b_lsb)
    @reg_pwr_restart_thr_11b.setter
    def reg_pwr_restart_thr_11b(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_restart_thr_11b_msb, self.__reg_pwr_restart_thr_11b_lsb, value)

    @property
    def reg_pwr_drop_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_drop_thr_msb, self.__reg_pwr_drop_thr_lsb)
    @reg_pwr_drop_thr.setter
    def reg_pwr_drop_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_drop_thr_msb, self.__reg_pwr_drop_thr_lsb, value)

    @property
    def reg_pwr_restart_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_restart_thr_msb, self.__reg_pwr_restart_thr_lsb)
    @reg_pwr_restart_thr.setter
    def reg_pwr_restart_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_restart_thr_msb, self.__reg_pwr_restart_thr_lsb, value)
class AGCGAIN_CTRL_4(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x94
        self.__reg_rcv_exit_en_lsb = 31
        self.__reg_rcv_exit_en_msb = 31
        self.__reg_mdchk_exit_en_lsb = 28
        self.__reg_mdchk_exit_en_msb = 30
        self.__reg_fine_exit_en_lsb = 25
        self.__reg_fine_exit_en_msb = 27
        self.__reg_init_use_fine_lsb = 24
        self.__reg_init_use_fine_msb = 24
        self.__reg_pwr_lt_gain_opt_lsb = 23
        self.__reg_pwr_lt_gain_opt_msb = 23
        self.__reg_pwr_lt_gain_jump_lsb = 16
        self.__reg_pwr_lt_gain_jump_msb = 22
        self.__reg_init_gain_ofs_lsb = 9
        self.__reg_init_gain_ofs_msb = 15
        self.__reg_init_gain_lsb = 2
        self.__reg_init_gain_msb = 8
        self.__reg_init_set_en_lsb = 1
        self.__reg_init_set_en_msb = 1
        self.__reg_init_gain_en_lsb = 0
        self.__reg_init_gain_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rcv_exit_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rcv_exit_en_msb, self.__reg_rcv_exit_en_lsb)
    @reg_rcv_exit_en.setter
    def reg_rcv_exit_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rcv_exit_en_msb, self.__reg_rcv_exit_en_lsb, value)

    @property
    def reg_mdchk_exit_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mdchk_exit_en_msb, self.__reg_mdchk_exit_en_lsb)
    @reg_mdchk_exit_en.setter
    def reg_mdchk_exit_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mdchk_exit_en_msb, self.__reg_mdchk_exit_en_lsb, value)

    @property
    def reg_fine_exit_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fine_exit_en_msb, self.__reg_fine_exit_en_lsb)
    @reg_fine_exit_en.setter
    def reg_fine_exit_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fine_exit_en_msb, self.__reg_fine_exit_en_lsb, value)

    @property
    def reg_init_use_fine(self):
        return self.__MEM.rdm(self.__addr, self.__reg_init_use_fine_msb, self.__reg_init_use_fine_lsb)
    @reg_init_use_fine.setter
    def reg_init_use_fine(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_init_use_fine_msb, self.__reg_init_use_fine_lsb, value)

    @property
    def reg_pwr_lt_gain_opt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_lt_gain_opt_msb, self.__reg_pwr_lt_gain_opt_lsb)
    @reg_pwr_lt_gain_opt.setter
    def reg_pwr_lt_gain_opt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_lt_gain_opt_msb, self.__reg_pwr_lt_gain_opt_lsb, value)

    @property
    def reg_pwr_lt_gain_jump(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_lt_gain_jump_msb, self.__reg_pwr_lt_gain_jump_lsb)
    @reg_pwr_lt_gain_jump.setter
    def reg_pwr_lt_gain_jump(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_lt_gain_jump_msb, self.__reg_pwr_lt_gain_jump_lsb, value)

    @property
    def reg_init_gain_ofs(self):
        return self.__MEM.rdm(self.__addr, self.__reg_init_gain_ofs_msb, self.__reg_init_gain_ofs_lsb)
    @reg_init_gain_ofs.setter
    def reg_init_gain_ofs(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_init_gain_ofs_msb, self.__reg_init_gain_ofs_lsb, value)

    @property
    def reg_init_gain(self):
        return self.__MEM.rdm(self.__addr, self.__reg_init_gain_msb, self.__reg_init_gain_lsb)
    @reg_init_gain.setter
    def reg_init_gain(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_init_gain_msb, self.__reg_init_gain_lsb, value)

    @property
    def reg_init_set_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_init_set_en_msb, self.__reg_init_set_en_lsb)
    @reg_init_set_en.setter
    def reg_init_set_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_init_set_en_msb, self.__reg_init_set_en_lsb, value)

    @property
    def reg_init_gain_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_init_gain_en_msb, self.__reg_init_gain_en_lsb)
    @reg_init_gain_en.setter
    def reg_init_gain_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_init_gain_en_msb, self.__reg_init_gain_en_lsb, value)
class AGCRD5(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x98
        self.__bb_rx_frame_lsb = 20
        self.__bb_rx_frame_msb = 20
        self.__agc_debug_0_lsb = 0
        self.__agc_debug_0_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def bb_rx_frame(self):
        return self.__MEM.rdm(self.__addr, self.__bb_rx_frame_msb, self.__bb_rx_frame_lsb)
    @bb_rx_frame.setter
    def bb_rx_frame(self, value):
        return self.__MEM.wrm(self.__addr, self.__bb_rx_frame_msb, self.__bb_rx_frame_lsb, value)

    @property
    def agc_debug_0(self):
        return self.__MEM.rdm(self.__addr, self.__agc_debug_0_msb, self.__agc_debug_0_lsb)
    @agc_debug_0.setter
    def agc_debug_0(self, value):
        return self.__MEM.wrm(self.__addr, self.__agc_debug_0_msb, self.__agc_debug_0_lsb, value)
class AGCRD6(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x9c
        self.__agc_debug_1_lsb = 0
        self.__agc_debug_1_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def agc_debug_1(self):
        return self.__MEM.rdm(self.__addr, self.__agc_debug_1_msb, self.__agc_debug_1_lsb)
    @agc_debug_1.setter
    def agc_debug_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__agc_debug_1_msb, self.__agc_debug_1_lsb, value)
class AGCPWR_CTRL10(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0xa0
        self.__reg_rxgain_comp_ht2040_lsb = 24
        self.__reg_rxgain_comp_ht2040_msb = 31
        self.__reg_restart_gt_thr_lsb = 16
        self.__reg_restart_gt_thr_msb = 23
        self.__reg_pwr_too_lt_gain_jump_lsb = 9
        self.__reg_pwr_too_lt_gain_jump_msb = 15
        self.__reg_pwr_too_low_thr_lsb = 0
        self.__reg_pwr_too_low_thr_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxgain_comp_ht2040(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxgain_comp_ht2040_msb, self.__reg_rxgain_comp_ht2040_lsb)
    @reg_rxgain_comp_ht2040.setter
    def reg_rxgain_comp_ht2040(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxgain_comp_ht2040_msb, self.__reg_rxgain_comp_ht2040_lsb, value)

    @property
    def reg_restart_gt_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_restart_gt_thr_msb, self.__reg_restart_gt_thr_lsb)
    @reg_restart_gt_thr.setter
    def reg_restart_gt_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_restart_gt_thr_msb, self.__reg_restart_gt_thr_lsb, value)

    @property
    def reg_pwr_too_lt_gain_jump(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_too_lt_gain_jump_msb, self.__reg_pwr_too_lt_gain_jump_lsb)
    @reg_pwr_too_lt_gain_jump.setter
    def reg_pwr_too_lt_gain_jump(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_too_lt_gain_jump_msb, self.__reg_pwr_too_lt_gain_jump_lsb, value)

    @property
    def reg_pwr_too_low_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_too_low_thr_msb, self.__reg_pwr_too_low_thr_lsb)
    @reg_pwr_too_low_thr.setter
    def reg_pwr_too_low_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_too_low_thr_msb, self.__reg_pwr_too_low_thr_lsb, value)
class AGCGAIN_CTRL_5(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0xa4
        self.__reg_min_gain_bt_lsb = 22
        self.__reg_min_gain_bt_msb = 28
        self.__reg_max_gain_bt_lsb = 15
        self.__reg_max_gain_bt_msb = 21
        self.__reg_search_fail_tune_lsb = 14
        self.__reg_search_fail_tune_msb = 14
        self.__reg_max_gain_lt_lsb = 7
        self.__reg_max_gain_lt_msb = 13
        self.__reg_max_gain_too_lt_lsb = 0
        self.__reg_max_gain_too_lt_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_min_gain_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_min_gain_bt_msb, self.__reg_min_gain_bt_lsb)
    @reg_min_gain_bt.setter
    def reg_min_gain_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_min_gain_bt_msb, self.__reg_min_gain_bt_lsb, value)

    @property
    def reg_max_gain_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_max_gain_bt_msb, self.__reg_max_gain_bt_lsb)
    @reg_max_gain_bt.setter
    def reg_max_gain_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_max_gain_bt_msb, self.__reg_max_gain_bt_lsb, value)

    @property
    def reg_search_fail_tune(self):
        return self.__MEM.rdm(self.__addr, self.__reg_search_fail_tune_msb, self.__reg_search_fail_tune_lsb)
    @reg_search_fail_tune.setter
    def reg_search_fail_tune(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_search_fail_tune_msb, self.__reg_search_fail_tune_lsb, value)

    @property
    def reg_max_gain_lt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_max_gain_lt_msb, self.__reg_max_gain_lt_lsb)
    @reg_max_gain_lt.setter
    def reg_max_gain_lt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_max_gain_lt_msb, self.__reg_max_gain_lt_lsb, value)

    @property
    def reg_max_gain_too_lt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_max_gain_too_lt_msb, self.__reg_max_gain_too_lt_lsb)
    @reg_max_gain_too_lt.setter
    def reg_max_gain_too_lt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_max_gain_too_lt_msb, self.__reg_max_gain_too_lt_lsb, value)
class AGCSEC_CTRL0(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0xa8
        self.__reg_pwr_sec_gt_thr_lsb = 8
        self.__reg_pwr_sec_gt_thr_msb = 13
        self.__reg_sig_weak_sec_thr_lsb = 0
        self.__reg_sig_weak_sec_thr_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_pwr_sec_gt_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_sec_gt_thr_msb, self.__reg_pwr_sec_gt_thr_lsb)
    @reg_pwr_sec_gt_thr.setter
    def reg_pwr_sec_gt_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_sec_gt_thr_msb, self.__reg_pwr_sec_gt_thr_lsb, value)

    @property
    def reg_sig_weak_sec_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sig_weak_sec_thr_msb, self.__reg_sig_weak_sec_thr_lsb)
    @reg_sig_weak_sec_thr.setter
    def reg_sig_weak_sec_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sig_weak_sec_thr_msb, self.__reg_sig_weak_sec_thr_lsb, value)
class AGCPWR_CTRL11(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0xac
        self.__reg_rest_fine_pwr_sel_lsb = 27
        self.__reg_rest_fine_pwr_sel_msb = 28
        self.__reg_pwr_fine_mcs2_lsb = 18
        self.__reg_pwr_fine_mcs2_msb = 26
        self.__reg_pwr_fine_mcs1_lsb = 9
        self.__reg_pwr_fine_mcs1_msb = 17
        self.__reg_pwr_fine_mcs0_lsb = 0
        self.__reg_pwr_fine_mcs0_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rest_fine_pwr_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rest_fine_pwr_sel_msb, self.__reg_rest_fine_pwr_sel_lsb)
    @reg_rest_fine_pwr_sel.setter
    def reg_rest_fine_pwr_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rest_fine_pwr_sel_msb, self.__reg_rest_fine_pwr_sel_lsb, value)

    @property
    def reg_pwr_fine_mcs2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_mcs2_msb, self.__reg_pwr_fine_mcs2_lsb)
    @reg_pwr_fine_mcs2.setter
    def reg_pwr_fine_mcs2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_mcs2_msb, self.__reg_pwr_fine_mcs2_lsb, value)

    @property
    def reg_pwr_fine_mcs1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_mcs1_msb, self.__reg_pwr_fine_mcs1_lsb)
    @reg_pwr_fine_mcs1.setter
    def reg_pwr_fine_mcs1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_mcs1_msb, self.__reg_pwr_fine_mcs1_lsb, value)

    @property
    def reg_pwr_fine_mcs0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_mcs0_msb, self.__reg_pwr_fine_mcs0_lsb)
    @reg_pwr_fine_mcs0.setter
    def reg_pwr_fine_mcs0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_mcs0_msb, self.__reg_pwr_fine_mcs0_lsb, value)
class AGCPWR_CTRL12(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0xb0
        self.__reg_pwr_fine_mcs5_lsb = 18
        self.__reg_pwr_fine_mcs5_msb = 26
        self.__reg_pwr_fine_mcs4_lsb = 9
        self.__reg_pwr_fine_mcs4_msb = 17
        self.__reg_pwr_fine_mcs3_lsb = 0
        self.__reg_pwr_fine_mcs3_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_pwr_fine_mcs5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_mcs5_msb, self.__reg_pwr_fine_mcs5_lsb)
    @reg_pwr_fine_mcs5.setter
    def reg_pwr_fine_mcs5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_mcs5_msb, self.__reg_pwr_fine_mcs5_lsb, value)

    @property
    def reg_pwr_fine_mcs4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_mcs4_msb, self.__reg_pwr_fine_mcs4_lsb)
    @reg_pwr_fine_mcs4.setter
    def reg_pwr_fine_mcs4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_mcs4_msb, self.__reg_pwr_fine_mcs4_lsb, value)

    @property
    def reg_pwr_fine_mcs3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_mcs3_msb, self.__reg_pwr_fine_mcs3_lsb)
    @reg_pwr_fine_mcs3.setter
    def reg_pwr_fine_mcs3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_mcs3_msb, self.__reg_pwr_fine_mcs3_lsb, value)
class AGCPWR_CTRL13(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0xb4
        self.__reg_pwr_chg_sel_lsb = 31
        self.__reg_pwr_chg_sel_msb = 31
        self.__reg_pwr_fe2_tonerm_en_lsb = 30
        self.__reg_pwr_fe2_tonerm_en_msb = 30
        self.__reg_pwr_fe_dcrm_en_lsb = 29
        self.__reg_pwr_fe_dcrm_en_msb = 29
        self.__reg_pwr_fine_sel_fe_lsb = 28
        self.__reg_pwr_fine_sel_fe_msb = 28
        self.__reg_pwr_coarse_sel_fe_lsb = 27
        self.__reg_pwr_coarse_sel_fe_msb = 27
        self.__reg_pwr_coarse_adc_lsb = 18
        self.__reg_pwr_coarse_adc_msb = 26
        self.__reg_pwr_fine_mcs7_lsb = 9
        self.__reg_pwr_fine_mcs7_msb = 17
        self.__reg_pwr_fine_mcs6_lsb = 0
        self.__reg_pwr_fine_mcs6_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_pwr_chg_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_chg_sel_msb, self.__reg_pwr_chg_sel_lsb)
    @reg_pwr_chg_sel.setter
    def reg_pwr_chg_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_chg_sel_msb, self.__reg_pwr_chg_sel_lsb, value)

    @property
    def reg_pwr_fe2_tonerm_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fe2_tonerm_en_msb, self.__reg_pwr_fe2_tonerm_en_lsb)
    @reg_pwr_fe2_tonerm_en.setter
    def reg_pwr_fe2_tonerm_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fe2_tonerm_en_msb, self.__reg_pwr_fe2_tonerm_en_lsb, value)

    @property
    def reg_pwr_fe_dcrm_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fe_dcrm_en_msb, self.__reg_pwr_fe_dcrm_en_lsb)
    @reg_pwr_fe_dcrm_en.setter
    def reg_pwr_fe_dcrm_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fe_dcrm_en_msb, self.__reg_pwr_fe_dcrm_en_lsb, value)

    @property
    def reg_pwr_fine_sel_fe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_sel_fe_msb, self.__reg_pwr_fine_sel_fe_lsb)
    @reg_pwr_fine_sel_fe.setter
    def reg_pwr_fine_sel_fe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_sel_fe_msb, self.__reg_pwr_fine_sel_fe_lsb, value)

    @property
    def reg_pwr_coarse_sel_fe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_coarse_sel_fe_msb, self.__reg_pwr_coarse_sel_fe_lsb)
    @reg_pwr_coarse_sel_fe.setter
    def reg_pwr_coarse_sel_fe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_coarse_sel_fe_msb, self.__reg_pwr_coarse_sel_fe_lsb, value)

    @property
    def reg_pwr_coarse_adc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_coarse_adc_msb, self.__reg_pwr_coarse_adc_lsb)
    @reg_pwr_coarse_adc.setter
    def reg_pwr_coarse_adc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_coarse_adc_msb, self.__reg_pwr_coarse_adc_lsb, value)

    @property
    def reg_pwr_fine_mcs7(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_mcs7_msb, self.__reg_pwr_fine_mcs7_lsb)
    @reg_pwr_fine_mcs7.setter
    def reg_pwr_fine_mcs7(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_mcs7_msb, self.__reg_pwr_fine_mcs7_lsb, value)

    @property
    def reg_pwr_fine_mcs6(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_mcs6_msb, self.__reg_pwr_fine_mcs6_lsb)
    @reg_pwr_fine_mcs6.setter
    def reg_pwr_fine_mcs6(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_mcs6_msb, self.__reg_pwr_fine_mcs6_lsb, value)
class AGCTEST_CTRL(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0xb8
        self.__reg_corr_force_clk_lsb = 16
        self.__reg_corr_force_clk_msb = 16
        self.__reg_corr_ht40_force_clk_lsb = 15
        self.__reg_corr_ht40_force_clk_msb = 15
        self.__reg_agc_force_clk_lsb = 14
        self.__reg_agc_force_clk_msb = 14
        self.__reg_11b_force_clk_lsb = 13
        self.__reg_11b_force_clk_msb = 13
        self.__reg_filt_att1db_en_sec_lsb = 12
        self.__reg_filt_att1db_en_sec_msb = 12
        self.__reg_filt_att1db_en_lsb = 11
        self.__reg_filt_att1db_en_msb = 11
        self.__reg_agcclk_en_lsb = 10
        self.__reg_agcclk_en_msb = 10
        self.__reg_test_ctrl_lsb = 0
        self.__reg_test_ctrl_msb = 9
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_corr_force_clk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_force_clk_msb, self.__reg_corr_force_clk_lsb)
    @reg_corr_force_clk.setter
    def reg_corr_force_clk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_force_clk_msb, self.__reg_corr_force_clk_lsb, value)

    @property
    def reg_corr_ht40_force_clk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_ht40_force_clk_msb, self.__reg_corr_ht40_force_clk_lsb)
    @reg_corr_ht40_force_clk.setter
    def reg_corr_ht40_force_clk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_ht40_force_clk_msb, self.__reg_corr_ht40_force_clk_lsb, value)

    @property
    def reg_agc_force_clk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_force_clk_msb, self.__reg_agc_force_clk_lsb)
    @reg_agc_force_clk.setter
    def reg_agc_force_clk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_force_clk_msb, self.__reg_agc_force_clk_lsb, value)

    @property
    def reg_11b_force_clk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_11b_force_clk_msb, self.__reg_11b_force_clk_lsb)
    @reg_11b_force_clk.setter
    def reg_11b_force_clk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_11b_force_clk_msb, self.__reg_11b_force_clk_lsb, value)

    @property
    def reg_filt_att1db_en_sec(self):
        return self.__MEM.rdm(self.__addr, self.__reg_filt_att1db_en_sec_msb, self.__reg_filt_att1db_en_sec_lsb)
    @reg_filt_att1db_en_sec.setter
    def reg_filt_att1db_en_sec(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_filt_att1db_en_sec_msb, self.__reg_filt_att1db_en_sec_lsb, value)

    @property
    def reg_filt_att1db_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_filt_att1db_en_msb, self.__reg_filt_att1db_en_lsb)
    @reg_filt_att1db_en.setter
    def reg_filt_att1db_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_filt_att1db_en_msb, self.__reg_filt_att1db_en_lsb, value)

    @property
    def reg_agcclk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agcclk_en_msb, self.__reg_agcclk_en_lsb)
    @reg_agcclk_en.setter
    def reg_agcclk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agcclk_en_msb, self.__reg_agcclk_en_lsb, value)

    @property
    def reg_test_ctrl(self):
        return self.__MEM.rdm(self.__addr, self.__reg_test_ctrl_msb, self.__reg_test_ctrl_lsb)
    @reg_test_ctrl.setter
    def reg_test_ctrl(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_test_ctrl_msb, self.__reg_test_ctrl_lsb, value)
class AGCOFDM_CTRL7(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0xbc
        self.__reg_corr_val_after_gain_3_en_lsb = 26
        self.__reg_corr_val_after_gain_3_en_msb = 26
        self.__reg_corr_val_after_gain_2_en_lsb = 25
        self.__reg_corr_val_after_gain_2_en_msb = 25
        self.__reg_corr_val_after_gain_en_lsb = 24
        self.__reg_corr_val_after_gain_en_msb = 24
        self.__reg_corr_val_after_gain_3_lsb = 16
        self.__reg_corr_val_after_gain_3_msb = 23
        self.__reg_corr_val_after_gain_2_lsb = 8
        self.__reg_corr_val_after_gain_2_msb = 15
        self.__reg_corr_val_after_gain_lsb = 0
        self.__reg_corr_val_after_gain_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_corr_val_after_gain_3_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_val_after_gain_3_en_msb, self.__reg_corr_val_after_gain_3_en_lsb)
    @reg_corr_val_after_gain_3_en.setter
    def reg_corr_val_after_gain_3_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_val_after_gain_3_en_msb, self.__reg_corr_val_after_gain_3_en_lsb, value)

    @property
    def reg_corr_val_after_gain_2_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_val_after_gain_2_en_msb, self.__reg_corr_val_after_gain_2_en_lsb)
    @reg_corr_val_after_gain_2_en.setter
    def reg_corr_val_after_gain_2_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_val_after_gain_2_en_msb, self.__reg_corr_val_after_gain_2_en_lsb, value)

    @property
    def reg_corr_val_after_gain_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_val_after_gain_en_msb, self.__reg_corr_val_after_gain_en_lsb)
    @reg_corr_val_after_gain_en.setter
    def reg_corr_val_after_gain_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_val_after_gain_en_msb, self.__reg_corr_val_after_gain_en_lsb, value)

    @property
    def reg_corr_val_after_gain_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_val_after_gain_3_msb, self.__reg_corr_val_after_gain_3_lsb)
    @reg_corr_val_after_gain_3.setter
    def reg_corr_val_after_gain_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_val_after_gain_3_msb, self.__reg_corr_val_after_gain_3_lsb, value)

    @property
    def reg_corr_val_after_gain_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_val_after_gain_2_msb, self.__reg_corr_val_after_gain_2_lsb)
    @reg_corr_val_after_gain_2.setter
    def reg_corr_val_after_gain_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_val_after_gain_2_msb, self.__reg_corr_val_after_gain_2_lsb, value)

    @property
    def reg_corr_val_after_gain(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_val_after_gain_msb, self.__reg_corr_val_after_gain_lsb)
    @reg_corr_val_after_gain.setter
    def reg_corr_val_after_gain(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_val_after_gain_msb, self.__reg_corr_val_after_gain_lsb, value)
class AGCRD7(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0xc0
        self.__agc_debug_2_lsb = 0
        self.__agc_debug_2_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def agc_debug_2(self):
        return self.__MEM.rdm(self.__addr, self.__agc_debug_2_msb, self.__agc_debug_2_lsb)
    @agc_debug_2.setter
    def agc_debug_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__agc_debug_2_msb, self.__agc_debug_2_lsb, value)
class AGCOFDM_CTRL8(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0xc4
        self.__reg_corr_pwr_rise_chk_lsb = 30
        self.__reg_corr_pwr_rise_chk_msb = 30
        self.__reg_corr_pwr_rise_chk_2_lsb = 29
        self.__reg_corr_pwr_rise_chk_2_msb = 29
        self.__reg_corr_use_xcorr_lsb = 28
        self.__reg_corr_use_xcorr_msb = 28
        self.__reg_corr_use_xcorr_2_lsb = 27
        self.__reg_corr_use_xcorr_2_msb = 27
        self.__reg_pwr_valid_cnt_init_3_lsb = 23
        self.__reg_pwr_valid_cnt_init_3_msb = 26
        self.__reg_pwr_fir_gt_thr_3_lsb = 13
        self.__reg_pwr_fir_gt_thr_3_msb = 22
        self.__reg_pwr_fir_surge_thr_3_lsb = 6
        self.__reg_pwr_fir_surge_thr_3_msb = 12
        self.__reg_pwr_inband_surge_thr_3_lsb = 0
        self.__reg_pwr_inband_surge_thr_3_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_corr_pwr_rise_chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_pwr_rise_chk_msb, self.__reg_corr_pwr_rise_chk_lsb)
    @reg_corr_pwr_rise_chk.setter
    def reg_corr_pwr_rise_chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_pwr_rise_chk_msb, self.__reg_corr_pwr_rise_chk_lsb, value)

    @property
    def reg_corr_pwr_rise_chk_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_pwr_rise_chk_2_msb, self.__reg_corr_pwr_rise_chk_2_lsb)
    @reg_corr_pwr_rise_chk_2.setter
    def reg_corr_pwr_rise_chk_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_pwr_rise_chk_2_msb, self.__reg_corr_pwr_rise_chk_2_lsb, value)

    @property
    def reg_corr_use_xcorr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_use_xcorr_msb, self.__reg_corr_use_xcorr_lsb)
    @reg_corr_use_xcorr.setter
    def reg_corr_use_xcorr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_use_xcorr_msb, self.__reg_corr_use_xcorr_lsb, value)

    @property
    def reg_corr_use_xcorr_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_use_xcorr_2_msb, self.__reg_corr_use_xcorr_2_lsb)
    @reg_corr_use_xcorr_2.setter
    def reg_corr_use_xcorr_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_use_xcorr_2_msb, self.__reg_corr_use_xcorr_2_lsb, value)

    @property
    def reg_pwr_valid_cnt_init_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_valid_cnt_init_3_msb, self.__reg_pwr_valid_cnt_init_3_lsb)
    @reg_pwr_valid_cnt_init_3.setter
    def reg_pwr_valid_cnt_init_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_valid_cnt_init_3_msb, self.__reg_pwr_valid_cnt_init_3_lsb, value)

    @property
    def reg_pwr_fir_gt_thr_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fir_gt_thr_3_msb, self.__reg_pwr_fir_gt_thr_3_lsb)
    @reg_pwr_fir_gt_thr_3.setter
    def reg_pwr_fir_gt_thr_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fir_gt_thr_3_msb, self.__reg_pwr_fir_gt_thr_3_lsb, value)

    @property
    def reg_pwr_fir_surge_thr_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fir_surge_thr_3_msb, self.__reg_pwr_fir_surge_thr_3_lsb)
    @reg_pwr_fir_surge_thr_3.setter
    def reg_pwr_fir_surge_thr_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fir_surge_thr_3_msb, self.__reg_pwr_fir_surge_thr_3_lsb, value)

    @property
    def reg_pwr_inband_surge_thr_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_inband_surge_thr_3_msb, self.__reg_pwr_inband_surge_thr_3_lsb)
    @reg_pwr_inband_surge_thr_3.setter
    def reg_pwr_inband_surge_thr_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_inband_surge_thr_3_msb, self.__reg_pwr_inband_surge_thr_3_lsb, value)
class AGCOFDM_CTRL9(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0xc8
        self.__reg_pwr_fir_gt_noise_thr_lsb = 24
        self.__reg_pwr_fir_gt_noise_thr_msb = 31
        self.__reg_pwr_fir_gt_noise_thr_2_lsb = 16
        self.__reg_pwr_fir_gt_noise_thr_2_msb = 23
        self.__reg_pwr_fir_gt_noise_thr_3_lsb = 8
        self.__reg_pwr_fir_gt_noise_thr_3_msb = 15
        self.__reg_ocorr_gt_noise_thr_vote_lsb = 0
        self.__reg_ocorr_gt_noise_thr_vote_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_pwr_fir_gt_noise_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fir_gt_noise_thr_msb, self.__reg_pwr_fir_gt_noise_thr_lsb)
    @reg_pwr_fir_gt_noise_thr.setter
    def reg_pwr_fir_gt_noise_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fir_gt_noise_thr_msb, self.__reg_pwr_fir_gt_noise_thr_lsb, value)

    @property
    def reg_pwr_fir_gt_noise_thr_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fir_gt_noise_thr_2_msb, self.__reg_pwr_fir_gt_noise_thr_2_lsb)
    @reg_pwr_fir_gt_noise_thr_2.setter
    def reg_pwr_fir_gt_noise_thr_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fir_gt_noise_thr_2_msb, self.__reg_pwr_fir_gt_noise_thr_2_lsb, value)

    @property
    def reg_pwr_fir_gt_noise_thr_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fir_gt_noise_thr_3_msb, self.__reg_pwr_fir_gt_noise_thr_3_lsb)
    @reg_pwr_fir_gt_noise_thr_3.setter
    def reg_pwr_fir_gt_noise_thr_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fir_gt_noise_thr_3_msb, self.__reg_pwr_fir_gt_noise_thr_3_lsb, value)

    @property
    def reg_ocorr_gt_noise_thr_vote(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ocorr_gt_noise_thr_vote_msb, self.__reg_ocorr_gt_noise_thr_vote_lsb)
    @reg_ocorr_gt_noise_thr_vote.setter
    def reg_ocorr_gt_noise_thr_vote(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ocorr_gt_noise_thr_vote_msb, self.__reg_ocorr_gt_noise_thr_vote_lsb, value)
class AGCOFDM_CTRL10(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0xcc
        self.__reg_xcorr_snr_thr_en_1_lsb = 31
        self.__reg_xcorr_snr_thr_en_1_msb = 31
        self.__reg_xcorr_snr_thr_en_2_lsb = 30
        self.__reg_xcorr_snr_thr_en_2_msb = 30
        self.__reg_gain_fir_gt_thr_3_lsb = 20
        self.__reg_gain_fir_gt_thr_3_msb = 29
        self.__reg_gain_fir_gt_thr_2_lsb = 10
        self.__reg_gain_fir_gt_thr_2_msb = 19
        self.__reg_gain_fir_gt_thr_1_lsb = 0
        self.__reg_gain_fir_gt_thr_1_msb = 9
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_xcorr_snr_thr_en_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_snr_thr_en_1_msb, self.__reg_xcorr_snr_thr_en_1_lsb)
    @reg_xcorr_snr_thr_en_1.setter
    def reg_xcorr_snr_thr_en_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_snr_thr_en_1_msb, self.__reg_xcorr_snr_thr_en_1_lsb, value)

    @property
    def reg_xcorr_snr_thr_en_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_snr_thr_en_2_msb, self.__reg_xcorr_snr_thr_en_2_lsb)
    @reg_xcorr_snr_thr_en_2.setter
    def reg_xcorr_snr_thr_en_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_snr_thr_en_2_msb, self.__reg_xcorr_snr_thr_en_2_lsb, value)

    @property
    def reg_gain_fir_gt_thr_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_fir_gt_thr_3_msb, self.__reg_gain_fir_gt_thr_3_lsb)
    @reg_gain_fir_gt_thr_3.setter
    def reg_gain_fir_gt_thr_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_fir_gt_thr_3_msb, self.__reg_gain_fir_gt_thr_3_lsb, value)

    @property
    def reg_gain_fir_gt_thr_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_fir_gt_thr_2_msb, self.__reg_gain_fir_gt_thr_2_lsb)
    @reg_gain_fir_gt_thr_2.setter
    def reg_gain_fir_gt_thr_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_fir_gt_thr_2_msb, self.__reg_gain_fir_gt_thr_2_lsb, value)

    @property
    def reg_gain_fir_gt_thr_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_fir_gt_thr_1_msb, self.__reg_gain_fir_gt_thr_1_lsb)
    @reg_gain_fir_gt_thr_1.setter
    def reg_gain_fir_gt_thr_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_fir_gt_thr_1_msb, self.__reg_gain_fir_gt_thr_1_lsb, value)
class AGCBT_CTRL3(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0xd0
        self.__reg_bt_gain_offset_lsb = 17
        self.__reg_bt_gain_offset_msb = 24
        self.__reg_rxgain_comp_bt_lsb = 9
        self.__reg_rxgain_comp_bt_msb = 16
        self.__reg_pwr_fine_1st_le_lsb = 0
        self.__reg_pwr_fine_1st_le_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bt_gain_offset(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bt_gain_offset_msb, self.__reg_bt_gain_offset_lsb)
    @reg_bt_gain_offset.setter
    def reg_bt_gain_offset(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bt_gain_offset_msb, self.__reg_bt_gain_offset_lsb, value)

    @property
    def reg_rxgain_comp_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxgain_comp_bt_msb, self.__reg_rxgain_comp_bt_lsb)
    @reg_rxgain_comp_bt.setter
    def reg_rxgain_comp_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxgain_comp_bt_msb, self.__reg_rxgain_comp_bt_lsb, value)

    @property
    def reg_pwr_fine_1st_le(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_1st_le_msb, self.__reg_pwr_fine_1st_le_lsb)
    @reg_pwr_fine_1st_le.setter
    def reg_pwr_fine_1st_le(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_1st_le_msb, self.__reg_pwr_fine_1st_le_lsb, value)
class AGCOFDM_CTRL12(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0xd4
        self.__reg_corr_lg_ppm_lsb = 26
        self.__reg_corr_lg_ppm_msb = 26
        self.__reg_corr_lg_ppm_2_lsb = 25
        self.__reg_corr_lg_ppm_2_msb = 25
        self.__reg_corr_ptg_en2_lsb = 24
        self.__reg_corr_ptg_en2_msb = 24
        self.__reg_corr_ptg_thr_lsb = 20
        self.__reg_corr_ptg_thr_msb = 23
        self.__reg_corr_ptg_max_lsb = 16
        self.__reg_corr_ptg_max_msb = 19
        self.__reg_corr_ptg_en1_lsb = 15
        self.__reg_corr_ptg_en1_msb = 15
        self.__reg_corr_start_cnt_2_lsb = 8
        self.__reg_corr_start_cnt_2_msb = 14
        self.__reg_week_rssi_xc_thr_2_lsb = 0
        self.__reg_week_rssi_xc_thr_2_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_corr_lg_ppm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_lg_ppm_msb, self.__reg_corr_lg_ppm_lsb)
    @reg_corr_lg_ppm.setter
    def reg_corr_lg_ppm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_lg_ppm_msb, self.__reg_corr_lg_ppm_lsb, value)

    @property
    def reg_corr_lg_ppm_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_lg_ppm_2_msb, self.__reg_corr_lg_ppm_2_lsb)
    @reg_corr_lg_ppm_2.setter
    def reg_corr_lg_ppm_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_lg_ppm_2_msb, self.__reg_corr_lg_ppm_2_lsb, value)

    @property
    def reg_corr_ptg_en2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_ptg_en2_msb, self.__reg_corr_ptg_en2_lsb)
    @reg_corr_ptg_en2.setter
    def reg_corr_ptg_en2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_ptg_en2_msb, self.__reg_corr_ptg_en2_lsb, value)

    @property
    def reg_corr_ptg_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_ptg_thr_msb, self.__reg_corr_ptg_thr_lsb)
    @reg_corr_ptg_thr.setter
    def reg_corr_ptg_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_ptg_thr_msb, self.__reg_corr_ptg_thr_lsb, value)

    @property
    def reg_corr_ptg_max(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_ptg_max_msb, self.__reg_corr_ptg_max_lsb)
    @reg_corr_ptg_max.setter
    def reg_corr_ptg_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_ptg_max_msb, self.__reg_corr_ptg_max_lsb, value)

    @property
    def reg_corr_ptg_en1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_ptg_en1_msb, self.__reg_corr_ptg_en1_lsb)
    @reg_corr_ptg_en1.setter
    def reg_corr_ptg_en1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_ptg_en1_msb, self.__reg_corr_ptg_en1_lsb, value)

    @property
    def reg_corr_start_cnt_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_start_cnt_2_msb, self.__reg_corr_start_cnt_2_lsb)
    @reg_corr_start_cnt_2.setter
    def reg_corr_start_cnt_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_start_cnt_2_msb, self.__reg_corr_start_cnt_2_lsb, value)

    @property
    def reg_week_rssi_xc_thr_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_week_rssi_xc_thr_2_msb, self.__reg_week_rssi_xc_thr_2_lsb)
    @reg_week_rssi_xc_thr_2.setter
    def reg_week_rssi_xc_thr_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_week_rssi_xc_thr_2_msb, self.__reg_week_rssi_xc_thr_2_lsb, value)
class AGCPWR_CTRL14(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0xd8
        self.__reg_adcsat_thr_rst_lsb = 20
        self.__reg_adcsat_thr_rst_msb = 28
        self.__reg_pwr_gt_fe_chk_lsb = 19
        self.__reg_pwr_gt_fe_chk_msb = 19
        self.__reg_pwr_lt_fe_chk_lsb = 18
        self.__reg_pwr_lt_fe_chk_msb = 18
        self.__reg_pwr_fe_high_thr_lsb = 9
        self.__reg_pwr_fe_high_thr_msb = 17
        self.__reg_pwr_coarse_init_lsb = 0
        self.__reg_pwr_coarse_init_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_adcsat_thr_rst(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcsat_thr_rst_msb, self.__reg_adcsat_thr_rst_lsb)
    @reg_adcsat_thr_rst.setter
    def reg_adcsat_thr_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcsat_thr_rst_msb, self.__reg_adcsat_thr_rst_lsb, value)

    @property
    def reg_pwr_gt_fe_chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_gt_fe_chk_msb, self.__reg_pwr_gt_fe_chk_lsb)
    @reg_pwr_gt_fe_chk.setter
    def reg_pwr_gt_fe_chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_gt_fe_chk_msb, self.__reg_pwr_gt_fe_chk_lsb, value)

    @property
    def reg_pwr_lt_fe_chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_lt_fe_chk_msb, self.__reg_pwr_lt_fe_chk_lsb)
    @reg_pwr_lt_fe_chk.setter
    def reg_pwr_lt_fe_chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_lt_fe_chk_msb, self.__reg_pwr_lt_fe_chk_lsb, value)

    @property
    def reg_pwr_fe_high_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fe_high_thr_msb, self.__reg_pwr_fe_high_thr_lsb)
    @reg_pwr_fe_high_thr.setter
    def reg_pwr_fe_high_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fe_high_thr_msb, self.__reg_pwr_fe_high_thr_lsb, value)

    @property
    def reg_pwr_coarse_init(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_coarse_init_msb, self.__reg_pwr_coarse_init_lsb)
    @reg_pwr_coarse_init.setter
    def reg_pwr_coarse_init(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_coarse_init_msb, self.__reg_pwr_coarse_init_lsb, value)
class AGCCCA_CTRL0(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0xdc
        self.__reg_cca_thr_sec_lsb = 12
        self.__reg_cca_thr_sec_msb = 15
        self.__reg_cca_dly_len_sec_lsb = 8
        self.__reg_cca_dly_len_sec_msb = 11
        self.__reg_cca_thr_lsb = 4
        self.__reg_cca_thr_msb = 7
        self.__reg_cca_dly_len_lsb = 0
        self.__reg_cca_dly_len_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_cca_thr_sec(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cca_thr_sec_msb, self.__reg_cca_thr_sec_lsb)
    @reg_cca_thr_sec.setter
    def reg_cca_thr_sec(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cca_thr_sec_msb, self.__reg_cca_thr_sec_lsb, value)

    @property
    def reg_cca_dly_len_sec(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cca_dly_len_sec_msb, self.__reg_cca_dly_len_sec_lsb)
    @reg_cca_dly_len_sec.setter
    def reg_cca_dly_len_sec(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cca_dly_len_sec_msb, self.__reg_cca_dly_len_sec_lsb, value)

    @property
    def reg_cca_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cca_thr_msb, self.__reg_cca_thr_lsb)
    @reg_cca_thr.setter
    def reg_cca_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cca_thr_msb, self.__reg_cca_thr_lsb, value)

    @property
    def reg_cca_dly_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cca_dly_len_msb, self.__reg_cca_dly_len_lsb)
    @reg_cca_dly_len.setter
    def reg_cca_dly_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cca_dly_len_msb, self.__reg_cca_dly_len_lsb, value)
class AGCGAIN_CTRL_6(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0xe0
        self.__reg_rssi_2nd_11n_mcs3_lsb = 24
        self.__reg_rssi_2nd_11n_mcs3_msb = 31
        self.__reg_rssi_2nd_11n_mcs2_lsb = 16
        self.__reg_rssi_2nd_11n_mcs2_msb = 23
        self.__reg_rssi_2nd_11n_mcs1_lsb = 8
        self.__reg_rssi_2nd_11n_mcs1_msb = 15
        self.__reg_rssi_2nd_11n_mcs0_lsb = 0
        self.__reg_rssi_2nd_11n_mcs0_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rssi_2nd_11n_mcs3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rssi_2nd_11n_mcs3_msb, self.__reg_rssi_2nd_11n_mcs3_lsb)
    @reg_rssi_2nd_11n_mcs3.setter
    def reg_rssi_2nd_11n_mcs3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rssi_2nd_11n_mcs3_msb, self.__reg_rssi_2nd_11n_mcs3_lsb, value)

    @property
    def reg_rssi_2nd_11n_mcs2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rssi_2nd_11n_mcs2_msb, self.__reg_rssi_2nd_11n_mcs2_lsb)
    @reg_rssi_2nd_11n_mcs2.setter
    def reg_rssi_2nd_11n_mcs2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rssi_2nd_11n_mcs2_msb, self.__reg_rssi_2nd_11n_mcs2_lsb, value)

    @property
    def reg_rssi_2nd_11n_mcs1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rssi_2nd_11n_mcs1_msb, self.__reg_rssi_2nd_11n_mcs1_lsb)
    @reg_rssi_2nd_11n_mcs1.setter
    def reg_rssi_2nd_11n_mcs1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rssi_2nd_11n_mcs1_msb, self.__reg_rssi_2nd_11n_mcs1_lsb, value)

    @property
    def reg_rssi_2nd_11n_mcs0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rssi_2nd_11n_mcs0_msb, self.__reg_rssi_2nd_11n_mcs0_lsb)
    @reg_rssi_2nd_11n_mcs0.setter
    def reg_rssi_2nd_11n_mcs0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rssi_2nd_11n_mcs0_msb, self.__reg_rssi_2nd_11n_mcs0_lsb, value)
class AGCGAIN_CTRL_7(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0xe4
        self.__reg_rssi_2nd_11n_mcs7_lsb = 24
        self.__reg_rssi_2nd_11n_mcs7_msb = 31
        self.__reg_rssi_2nd_11n_mcs6_lsb = 16
        self.__reg_rssi_2nd_11n_mcs6_msb = 23
        self.__reg_rssi_2nd_11n_mcs5_lsb = 8
        self.__reg_rssi_2nd_11n_mcs5_msb = 15
        self.__reg_rssi_2nd_11n_mcs4_lsb = 0
        self.__reg_rssi_2nd_11n_mcs4_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rssi_2nd_11n_mcs7(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rssi_2nd_11n_mcs7_msb, self.__reg_rssi_2nd_11n_mcs7_lsb)
    @reg_rssi_2nd_11n_mcs7.setter
    def reg_rssi_2nd_11n_mcs7(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rssi_2nd_11n_mcs7_msb, self.__reg_rssi_2nd_11n_mcs7_lsb, value)

    @property
    def reg_rssi_2nd_11n_mcs6(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rssi_2nd_11n_mcs6_msb, self.__reg_rssi_2nd_11n_mcs6_lsb)
    @reg_rssi_2nd_11n_mcs6.setter
    def reg_rssi_2nd_11n_mcs6(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rssi_2nd_11n_mcs6_msb, self.__reg_rssi_2nd_11n_mcs6_lsb, value)

    @property
    def reg_rssi_2nd_11n_mcs5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rssi_2nd_11n_mcs5_msb, self.__reg_rssi_2nd_11n_mcs5_lsb)
    @reg_rssi_2nd_11n_mcs5.setter
    def reg_rssi_2nd_11n_mcs5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rssi_2nd_11n_mcs5_msb, self.__reg_rssi_2nd_11n_mcs5_lsb, value)

    @property
    def reg_rssi_2nd_11n_mcs4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rssi_2nd_11n_mcs4_msb, self.__reg_rssi_2nd_11n_mcs4_lsb)
    @reg_rssi_2nd_11n_mcs4.setter
    def reg_rssi_2nd_11n_mcs4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rssi_2nd_11n_mcs4_msb, self.__reg_rssi_2nd_11n_mcs4_lsb, value)
class AGCCHAN_BW(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0xe8
        self.__reg_chbw_mult_thr_lsb = 27
        self.__reg_chbw_mult_thr_msb = 29
        self.__reg_chbw_shift_thr_lsb = 24
        self.__reg_chbw_shift_thr_msb = 26
        self.__reg_chanbw_corr_thr_2_lsb = 16
        self.__reg_chanbw_corr_thr_2_msb = 23
        self.__reg_chanbw_corr_thr_1_lsb = 8
        self.__reg_chanbw_corr_thr_1_msb = 15
        self.__reg_week_rssi_chanbw_thr_lsb = 0
        self.__reg_week_rssi_chanbw_thr_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_chbw_mult_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chbw_mult_thr_msb, self.__reg_chbw_mult_thr_lsb)
    @reg_chbw_mult_thr.setter
    def reg_chbw_mult_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chbw_mult_thr_msb, self.__reg_chbw_mult_thr_lsb, value)

    @property
    def reg_chbw_shift_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chbw_shift_thr_msb, self.__reg_chbw_shift_thr_lsb)
    @reg_chbw_shift_thr.setter
    def reg_chbw_shift_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chbw_shift_thr_msb, self.__reg_chbw_shift_thr_lsb, value)

    @property
    def reg_chanbw_corr_thr_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chanbw_corr_thr_2_msb, self.__reg_chanbw_corr_thr_2_lsb)
    @reg_chanbw_corr_thr_2.setter
    def reg_chanbw_corr_thr_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chanbw_corr_thr_2_msb, self.__reg_chanbw_corr_thr_2_lsb, value)

    @property
    def reg_chanbw_corr_thr_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chanbw_corr_thr_1_msb, self.__reg_chanbw_corr_thr_1_lsb)
    @reg_chanbw_corr_thr_1.setter
    def reg_chanbw_corr_thr_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chanbw_corr_thr_1_msb, self.__reg_chanbw_corr_thr_1_lsb, value)

    @property
    def reg_week_rssi_chanbw_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_week_rssi_chanbw_thr_msb, self.__reg_week_rssi_chanbw_thr_lsb)
    @reg_week_rssi_chanbw_thr.setter
    def reg_week_rssi_chanbw_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_week_rssi_chanbw_thr_msb, self.__reg_week_rssi_chanbw_thr_lsb, value)
class AGCOFDM_CTRL11(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0xec
        self.__reg_pwr_fir_stab_thr_spur_lsb = 25
        self.__reg_pwr_fir_stab_thr_spur_msb = 31
        self.__reg_pwr_stab_sel_lsb = 24
        self.__reg_pwr_stab_sel_msb = 24
        self.__reg_pwr_stab_1_chk_lsb = 23
        self.__reg_pwr_stab_1_chk_msb = 23
        self.__reg_pwr_stab_2_chk_lsb = 22
        self.__reg_pwr_stab_2_chk_msb = 22
        self.__reg_pwr_stab_3_chk_lsb = 21
        self.__reg_pwr_stab_3_chk_msb = 21
        self.__reg_pwr_fir_stab_thr_3_lsb = 14
        self.__reg_pwr_fir_stab_thr_3_msb = 20
        self.__reg_pwr_fir_stab_thr_2_lsb = 7
        self.__reg_pwr_fir_stab_thr_2_msb = 13
        self.__reg_pwr_fir_stab_thr_1_lsb = 0
        self.__reg_pwr_fir_stab_thr_1_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_pwr_fir_stab_thr_spur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fir_stab_thr_spur_msb, self.__reg_pwr_fir_stab_thr_spur_lsb)
    @reg_pwr_fir_stab_thr_spur.setter
    def reg_pwr_fir_stab_thr_spur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fir_stab_thr_spur_msb, self.__reg_pwr_fir_stab_thr_spur_lsb, value)

    @property
    def reg_pwr_stab_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_stab_sel_msb, self.__reg_pwr_stab_sel_lsb)
    @reg_pwr_stab_sel.setter
    def reg_pwr_stab_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_stab_sel_msb, self.__reg_pwr_stab_sel_lsb, value)

    @property
    def reg_pwr_stab_1_chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_stab_1_chk_msb, self.__reg_pwr_stab_1_chk_lsb)
    @reg_pwr_stab_1_chk.setter
    def reg_pwr_stab_1_chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_stab_1_chk_msb, self.__reg_pwr_stab_1_chk_lsb, value)

    @property
    def reg_pwr_stab_2_chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_stab_2_chk_msb, self.__reg_pwr_stab_2_chk_lsb)
    @reg_pwr_stab_2_chk.setter
    def reg_pwr_stab_2_chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_stab_2_chk_msb, self.__reg_pwr_stab_2_chk_lsb, value)

    @property
    def reg_pwr_stab_3_chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_stab_3_chk_msb, self.__reg_pwr_stab_3_chk_lsb)
    @reg_pwr_stab_3_chk.setter
    def reg_pwr_stab_3_chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_stab_3_chk_msb, self.__reg_pwr_stab_3_chk_lsb, value)

    @property
    def reg_pwr_fir_stab_thr_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fir_stab_thr_3_msb, self.__reg_pwr_fir_stab_thr_3_lsb)
    @reg_pwr_fir_stab_thr_3.setter
    def reg_pwr_fir_stab_thr_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fir_stab_thr_3_msb, self.__reg_pwr_fir_stab_thr_3_lsb, value)

    @property
    def reg_pwr_fir_stab_thr_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fir_stab_thr_2_msb, self.__reg_pwr_fir_stab_thr_2_lsb)
    @reg_pwr_fir_stab_thr_2.setter
    def reg_pwr_fir_stab_thr_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fir_stab_thr_2_msb, self.__reg_pwr_fir_stab_thr_2_lsb, value)

    @property
    def reg_pwr_fir_stab_thr_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fir_stab_thr_1_msb, self.__reg_pwr_fir_stab_thr_1_lsb)
    @reg_pwr_fir_stab_thr_1.setter
    def reg_pwr_fir_stab_thr_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fir_stab_thr_1_msb, self.__reg_pwr_fir_stab_thr_1_lsb, value)
class AGCPWR_CTRL15(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0xf0
        self.__reg_xcorr_snr_thr_h_lsb = 23
        self.__reg_xcorr_snr_thr_h_msb = 31
        self.__reg_xcorr_snr_thr_l_lsb = 14
        self.__reg_xcorr_snr_thr_l_msb = 22
        self.__reg_pwr_rsta_chk_tone_lsb = 13
        self.__reg_pwr_rsta_chk_tone_msb = 13
        self.__reg_pwr_restart_add_lsb = 8
        self.__reg_pwr_restart_add_msb = 12
        self.__reg_week_rssi_rsta_thr_lsb = 0
        self.__reg_week_rssi_rsta_thr_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_xcorr_snr_thr_h(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_snr_thr_h_msb, self.__reg_xcorr_snr_thr_h_lsb)
    @reg_xcorr_snr_thr_h.setter
    def reg_xcorr_snr_thr_h(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_snr_thr_h_msb, self.__reg_xcorr_snr_thr_h_lsb, value)

    @property
    def reg_xcorr_snr_thr_l(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xcorr_snr_thr_l_msb, self.__reg_xcorr_snr_thr_l_lsb)
    @reg_xcorr_snr_thr_l.setter
    def reg_xcorr_snr_thr_l(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xcorr_snr_thr_l_msb, self.__reg_xcorr_snr_thr_l_lsb, value)

    @property
    def reg_pwr_rsta_chk_tone(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_rsta_chk_tone_msb, self.__reg_pwr_rsta_chk_tone_lsb)
    @reg_pwr_rsta_chk_tone.setter
    def reg_pwr_rsta_chk_tone(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_rsta_chk_tone_msb, self.__reg_pwr_rsta_chk_tone_lsb, value)

    @property
    def reg_pwr_restart_add(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_restart_add_msb, self.__reg_pwr_restart_add_lsb)
    @reg_pwr_restart_add.setter
    def reg_pwr_restart_add(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_restart_add_msb, self.__reg_pwr_restart_add_lsb, value)

    @property
    def reg_week_rssi_rsta_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_week_rssi_rsta_thr_msb, self.__reg_week_rssi_rsta_thr_lsb)
    @reg_week_rssi_rsta_thr.setter
    def reg_week_rssi_rsta_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_week_rssi_rsta_thr_msb, self.__reg_week_rssi_rsta_thr_lsb, value)
class AGCFSM_CTRL5(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0xf4
        self.__reg_st_wait_cnt_lsb = 29
        self.__reg_st_wait_cnt_msb = 31
        self.__reg_pwr_sec_anti_eng_lsb = 28
        self.__reg_pwr_sec_anti_eng_msb = 28
        self.__reg_pwr_sec_anti_scorr_lsb = 27
        self.__reg_pwr_sec_anti_scorr_msb = 27
        self.__reg_pwr_sec_anti_thr_lsb = 19
        self.__reg_pwr_sec_anti_thr_msb = 26
        self.__reg_rifs_cnt_start_lsb = 10
        self.__reg_rifs_cnt_start_msb = 18
        self.__reg_rifs_cnt_init_lsb = 1
        self.__reg_rifs_cnt_init_msb = 9
        self.__reg_rifs_mode_en_lsb = 0
        self.__reg_rifs_mode_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_st_wait_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_st_wait_cnt_msb, self.__reg_st_wait_cnt_lsb)
    @reg_st_wait_cnt.setter
    def reg_st_wait_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_st_wait_cnt_msb, self.__reg_st_wait_cnt_lsb, value)

    @property
    def reg_pwr_sec_anti_eng(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_sec_anti_eng_msb, self.__reg_pwr_sec_anti_eng_lsb)
    @reg_pwr_sec_anti_eng.setter
    def reg_pwr_sec_anti_eng(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_sec_anti_eng_msb, self.__reg_pwr_sec_anti_eng_lsb, value)

    @property
    def reg_pwr_sec_anti_scorr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_sec_anti_scorr_msb, self.__reg_pwr_sec_anti_scorr_lsb)
    @reg_pwr_sec_anti_scorr.setter
    def reg_pwr_sec_anti_scorr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_sec_anti_scorr_msb, self.__reg_pwr_sec_anti_scorr_lsb, value)

    @property
    def reg_pwr_sec_anti_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_sec_anti_thr_msb, self.__reg_pwr_sec_anti_thr_lsb)
    @reg_pwr_sec_anti_thr.setter
    def reg_pwr_sec_anti_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_sec_anti_thr_msb, self.__reg_pwr_sec_anti_thr_lsb, value)

    @property
    def reg_rifs_cnt_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rifs_cnt_start_msb, self.__reg_rifs_cnt_start_lsb)
    @reg_rifs_cnt_start.setter
    def reg_rifs_cnt_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rifs_cnt_start_msb, self.__reg_rifs_cnt_start_lsb, value)

    @property
    def reg_rifs_cnt_init(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rifs_cnt_init_msb, self.__reg_rifs_cnt_init_lsb)
    @reg_rifs_cnt_init.setter
    def reg_rifs_cnt_init(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rifs_cnt_init_msb, self.__reg_rifs_cnt_init_lsb, value)

    @property
    def reg_rifs_mode_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rifs_mode_en_msb, self.__reg_rifs_mode_en_lsb)
    @reg_rifs_mode_en.setter
    def reg_rifs_mode_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rifs_mode_en_msb, self.__reg_rifs_mode_en_lsb, value)
class AGCPWR_CTRL16(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0xf8
        self.__reg_fine_pwr_num_lsb = 29
        self.__reg_fine_pwr_num_msb = 31
        self.__reg_pwr_fine_lt_ht2040_lsb = 28
        self.__reg_pwr_fine_lt_ht2040_msb = 28
        self.__reg_pwr_fine_lt_ht20_lsb = 27
        self.__reg_pwr_fine_lt_ht20_msb = 27
        self.__reg_pwr_lt_fe_chk_gt_thr_lsb = 18
        self.__reg_pwr_lt_fe_chk_gt_thr_msb = 26
        self.__reg_pwr_coarse_pri_low_lsb = 9
        self.__reg_pwr_coarse_pri_low_msb = 17
        self.__reg_pwr_low_pri_thr_lsb = 0
        self.__reg_pwr_low_pri_thr_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_fine_pwr_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fine_pwr_num_msb, self.__reg_fine_pwr_num_lsb)
    @reg_fine_pwr_num.setter
    def reg_fine_pwr_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fine_pwr_num_msb, self.__reg_fine_pwr_num_lsb, value)

    @property
    def reg_pwr_fine_lt_ht2040(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_lt_ht2040_msb, self.__reg_pwr_fine_lt_ht2040_lsb)
    @reg_pwr_fine_lt_ht2040.setter
    def reg_pwr_fine_lt_ht2040(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_lt_ht2040_msb, self.__reg_pwr_fine_lt_ht2040_lsb, value)

    @property
    def reg_pwr_fine_lt_ht20(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_lt_ht20_msb, self.__reg_pwr_fine_lt_ht20_lsb)
    @reg_pwr_fine_lt_ht20.setter
    def reg_pwr_fine_lt_ht20(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_lt_ht20_msb, self.__reg_pwr_fine_lt_ht20_lsb, value)

    @property
    def reg_pwr_lt_fe_chk_gt_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_lt_fe_chk_gt_thr_msb, self.__reg_pwr_lt_fe_chk_gt_thr_lsb)
    @reg_pwr_lt_fe_chk_gt_thr.setter
    def reg_pwr_lt_fe_chk_gt_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_lt_fe_chk_gt_thr_msb, self.__reg_pwr_lt_fe_chk_gt_thr_lsb, value)

    @property
    def reg_pwr_coarse_pri_low(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_coarse_pri_low_msb, self.__reg_pwr_coarse_pri_low_lsb)
    @reg_pwr_coarse_pri_low.setter
    def reg_pwr_coarse_pri_low(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_coarse_pri_low_msb, self.__reg_pwr_coarse_pri_low_lsb, value)

    @property
    def reg_pwr_low_pri_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_low_pri_thr_msb, self.__reg_pwr_low_pri_thr_lsb)
    @reg_pwr_low_pri_thr.setter
    def reg_pwr_low_pri_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_low_pri_thr_msb, self.__reg_pwr_low_pri_thr_lsb, value)
class AGCPWR_CTRL17(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0xfc
        self.__reg_pwr_fine_lt_bt_lsb = 28
        self.__reg_pwr_fine_lt_bt_msb = 28
        self.__reg_pwr_lt_fe_chk_bt_lsb = 27
        self.__reg_pwr_lt_fe_chk_bt_msb = 27
        self.__reg_pwr_lt_fe_chk_gt_thr_bt_lsb = 18
        self.__reg_pwr_lt_fe_chk_gt_thr_bt_msb = 26
        self.__reg_pwr_coarse_pri_low_bt_lsb = 9
        self.__reg_pwr_coarse_pri_low_bt_msb = 17
        self.__reg_pwr_low_pri_thr_bt_lsb = 0
        self.__reg_pwr_low_pri_thr_bt_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_pwr_fine_lt_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_lt_bt_msb, self.__reg_pwr_fine_lt_bt_lsb)
    @reg_pwr_fine_lt_bt.setter
    def reg_pwr_fine_lt_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_lt_bt_msb, self.__reg_pwr_fine_lt_bt_lsb, value)

    @property
    def reg_pwr_lt_fe_chk_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_lt_fe_chk_bt_msb, self.__reg_pwr_lt_fe_chk_bt_lsb)
    @reg_pwr_lt_fe_chk_bt.setter
    def reg_pwr_lt_fe_chk_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_lt_fe_chk_bt_msb, self.__reg_pwr_lt_fe_chk_bt_lsb, value)

    @property
    def reg_pwr_lt_fe_chk_gt_thr_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_lt_fe_chk_gt_thr_bt_msb, self.__reg_pwr_lt_fe_chk_gt_thr_bt_lsb)
    @reg_pwr_lt_fe_chk_gt_thr_bt.setter
    def reg_pwr_lt_fe_chk_gt_thr_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_lt_fe_chk_gt_thr_bt_msb, self.__reg_pwr_lt_fe_chk_gt_thr_bt_lsb, value)

    @property
    def reg_pwr_coarse_pri_low_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_coarse_pri_low_bt_msb, self.__reg_pwr_coarse_pri_low_bt_lsb)
    @reg_pwr_coarse_pri_low_bt.setter
    def reg_pwr_coarse_pri_low_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_coarse_pri_low_bt_msb, self.__reg_pwr_coarse_pri_low_bt_lsb, value)

    @property
    def reg_pwr_low_pri_thr_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_low_pri_thr_bt_msb, self.__reg_pwr_low_pri_thr_bt_lsb)
    @reg_pwr_low_pri_thr_bt.setter
    def reg_pwr_low_pri_thr_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_low_pri_thr_bt_msb, self.__reg_pwr_low_pri_thr_bt_lsb, value)
class AGCRD8(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x100
        self.__agc_debug_3_lsb = 0
        self.__agc_debug_3_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def agc_debug_3(self):
        return self.__MEM.rdm(self.__addr, self.__agc_debug_3_msb, self.__agc_debug_3_lsb)
    @agc_debug_3.setter
    def agc_debug_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__agc_debug_3_msb, self.__agc_debug_3_lsb, value)
class AGCPWR_CTRL18(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x104
        self.__reg_pwr_ht40_chk_thr_lsb = 24
        self.__reg_pwr_ht40_chk_thr_msb = 31
        self.__reg_ht40_rssi_chk_thr_lsb = 16
        self.__reg_ht40_rssi_chk_thr_msb = 23
        self.__reg_pwr_ht40_chk_en_lsb = 15
        self.__reg_pwr_ht40_chk_en_msb = 15
        self.__reg_gain_ht40_en_lsb = 14
        self.__reg_gain_ht40_en_msb = 14
        self.__reg_pwr_ht40_en_lsb = 13
        self.__reg_pwr_ht40_en_msb = 13
        self.__reg_pwr_fine_gain_sel_lsb = 11
        self.__reg_pwr_fine_gain_sel_msb = 12
        self.__reg_pwr_fine_2nd_11b_lsb = 0
        self.__reg_pwr_fine_2nd_11b_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_pwr_ht40_chk_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_ht40_chk_thr_msb, self.__reg_pwr_ht40_chk_thr_lsb)
    @reg_pwr_ht40_chk_thr.setter
    def reg_pwr_ht40_chk_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_ht40_chk_thr_msb, self.__reg_pwr_ht40_chk_thr_lsb, value)

    @property
    def reg_ht40_rssi_chk_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ht40_rssi_chk_thr_msb, self.__reg_ht40_rssi_chk_thr_lsb)
    @reg_ht40_rssi_chk_thr.setter
    def reg_ht40_rssi_chk_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ht40_rssi_chk_thr_msb, self.__reg_ht40_rssi_chk_thr_lsb, value)

    @property
    def reg_pwr_ht40_chk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_ht40_chk_en_msb, self.__reg_pwr_ht40_chk_en_lsb)
    @reg_pwr_ht40_chk_en.setter
    def reg_pwr_ht40_chk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_ht40_chk_en_msb, self.__reg_pwr_ht40_chk_en_lsb, value)

    @property
    def reg_gain_ht40_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_ht40_en_msb, self.__reg_gain_ht40_en_lsb)
    @reg_gain_ht40_en.setter
    def reg_gain_ht40_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_ht40_en_msb, self.__reg_gain_ht40_en_lsb, value)

    @property
    def reg_pwr_ht40_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_ht40_en_msb, self.__reg_pwr_ht40_en_lsb)
    @reg_pwr_ht40_en.setter
    def reg_pwr_ht40_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_ht40_en_msb, self.__reg_pwr_ht40_en_lsb, value)

    @property
    def reg_pwr_fine_gain_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_gain_sel_msb, self.__reg_pwr_fine_gain_sel_lsb)
    @reg_pwr_fine_gain_sel.setter
    def reg_pwr_fine_gain_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_gain_sel_msb, self.__reg_pwr_fine_gain_sel_lsb, value)

    @property
    def reg_pwr_fine_2nd_11b(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_2nd_11b_msb, self.__reg_pwr_fine_2nd_11b_lsb)
    @reg_pwr_fine_2nd_11b.setter
    def reg_pwr_fine_2nd_11b(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_2nd_11b_msb, self.__reg_pwr_fine_2nd_11b_lsb, value)
class AGCOFDM_CTRL13(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x108
        self.__reg_agc_ocorr_thr4_lsb = 24
        self.__reg_agc_ocorr_thr4_msb = 31
        self.__reg_corr_det_cnt_max_4_lsb = 16
        self.__reg_corr_det_cnt_max_4_msb = 22
        self.__reg_corr_det_thr_4_lsb = 10
        self.__reg_corr_det_thr_4_msb = 15
        self.__reg_corr_use_xcorr_gt_2_lsb = 9
        self.__reg_corr_use_xcorr_gt_2_msb = 9
        self.__reg_corr_use_xcorr_gt_lsb = 8
        self.__reg_corr_use_xcorr_gt_msb = 8
        self.__reg_week_rssi_gi_thr_lsb = 0
        self.__reg_week_rssi_gi_thr_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_agc_ocorr_thr4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_ocorr_thr4_msb, self.__reg_agc_ocorr_thr4_lsb)
    @reg_agc_ocorr_thr4.setter
    def reg_agc_ocorr_thr4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_ocorr_thr4_msb, self.__reg_agc_ocorr_thr4_lsb, value)

    @property
    def reg_corr_det_cnt_max_4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_det_cnt_max_4_msb, self.__reg_corr_det_cnt_max_4_lsb)
    @reg_corr_det_cnt_max_4.setter
    def reg_corr_det_cnt_max_4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_det_cnt_max_4_msb, self.__reg_corr_det_cnt_max_4_lsb, value)

    @property
    def reg_corr_det_thr_4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_det_thr_4_msb, self.__reg_corr_det_thr_4_lsb)
    @reg_corr_det_thr_4.setter
    def reg_corr_det_thr_4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_det_thr_4_msb, self.__reg_corr_det_thr_4_lsb, value)

    @property
    def reg_corr_use_xcorr_gt_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_use_xcorr_gt_2_msb, self.__reg_corr_use_xcorr_gt_2_lsb)
    @reg_corr_use_xcorr_gt_2.setter
    def reg_corr_use_xcorr_gt_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_use_xcorr_gt_2_msb, self.__reg_corr_use_xcorr_gt_2_lsb, value)

    @property
    def reg_corr_use_xcorr_gt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_use_xcorr_gt_msb, self.__reg_corr_use_xcorr_gt_lsb)
    @reg_corr_use_xcorr_gt.setter
    def reg_corr_use_xcorr_gt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_use_xcorr_gt_msb, self.__reg_corr_use_xcorr_gt_lsb, value)

    @property
    def reg_week_rssi_gi_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_week_rssi_gi_thr_msb, self.__reg_week_rssi_gi_thr_lsb)
    @reg_week_rssi_gi_thr.setter
    def reg_week_rssi_gi_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_week_rssi_gi_thr_msb, self.__reg_week_rssi_gi_thr_lsb, value)
class AGCPWR_CTRL19(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x10c
        self.__reg_pwr_chg_err_rcv_gt_thr_lsb = 24
        self.__reg_pwr_chg_err_rcv_gt_thr_msb = 31
        self.__reg_pwr_chg_err_rcv_lt_thr_lsb = 16
        self.__reg_pwr_chg_err_rcv_lt_thr_msb = 23
        self.__reg_pwr_chg_err_gt_thr_lsb = 8
        self.__reg_pwr_chg_err_gt_thr_msb = 15
        self.__reg_pwr_chg_err_lt_thr_lsb = 0
        self.__reg_pwr_chg_err_lt_thr_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_pwr_chg_err_rcv_gt_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_chg_err_rcv_gt_thr_msb, self.__reg_pwr_chg_err_rcv_gt_thr_lsb)
    @reg_pwr_chg_err_rcv_gt_thr.setter
    def reg_pwr_chg_err_rcv_gt_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_chg_err_rcv_gt_thr_msb, self.__reg_pwr_chg_err_rcv_gt_thr_lsb, value)

    @property
    def reg_pwr_chg_err_rcv_lt_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_chg_err_rcv_lt_thr_msb, self.__reg_pwr_chg_err_rcv_lt_thr_lsb)
    @reg_pwr_chg_err_rcv_lt_thr.setter
    def reg_pwr_chg_err_rcv_lt_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_chg_err_rcv_lt_thr_msb, self.__reg_pwr_chg_err_rcv_lt_thr_lsb, value)

    @property
    def reg_pwr_chg_err_gt_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_chg_err_gt_thr_msb, self.__reg_pwr_chg_err_gt_thr_lsb)
    @reg_pwr_chg_err_gt_thr.setter
    def reg_pwr_chg_err_gt_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_chg_err_gt_thr_msb, self.__reg_pwr_chg_err_gt_thr_lsb, value)

    @property
    def reg_pwr_chg_err_lt_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_chg_err_lt_thr_msb, self.__reg_pwr_chg_err_lt_thr_lsb)
    @reg_pwr_chg_err_lt_thr.setter
    def reg_pwr_chg_err_lt_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_chg_err_lt_thr_msb, self.__reg_pwr_chg_err_lt_thr_lsb, value)
class AGCGAIN_CTRL_8(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x110
        self.__reg_gain_gt_4_max_bt_lsb = 24
        self.__reg_gain_gt_4_max_bt_msb = 30
        self.__reg_gain_gt_3_max_bt_lsb = 16
        self.__reg_gain_gt_3_max_bt_msb = 22
        self.__reg_gain_gt_2_max_bt_lsb = 8
        self.__reg_gain_gt_2_max_bt_msb = 14
        self.__reg_gain_gt_1_max_bt_lsb = 0
        self.__reg_gain_gt_1_max_bt_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_gain_gt_4_max_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_gt_4_max_bt_msb, self.__reg_gain_gt_4_max_bt_lsb)
    @reg_gain_gt_4_max_bt.setter
    def reg_gain_gt_4_max_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_gt_4_max_bt_msb, self.__reg_gain_gt_4_max_bt_lsb, value)

    @property
    def reg_gain_gt_3_max_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_gt_3_max_bt_msb, self.__reg_gain_gt_3_max_bt_lsb)
    @reg_gain_gt_3_max_bt.setter
    def reg_gain_gt_3_max_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_gt_3_max_bt_msb, self.__reg_gain_gt_3_max_bt_lsb, value)

    @property
    def reg_gain_gt_2_max_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_gt_2_max_bt_msb, self.__reg_gain_gt_2_max_bt_lsb)
    @reg_gain_gt_2_max_bt.setter
    def reg_gain_gt_2_max_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_gt_2_max_bt_msb, self.__reg_gain_gt_2_max_bt_lsb, value)

    @property
    def reg_gain_gt_1_max_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_gt_1_max_bt_msb, self.__reg_gain_gt_1_max_bt_lsb)
    @reg_gain_gt_1_max_bt.setter
    def reg_gain_gt_1_max_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_gt_1_max_bt_msb, self.__reg_gain_gt_1_max_bt_lsb, value)
class AGCGAIN_CTRL_9(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x114
        self.__reg_gain_gt_4_max_lsb = 24
        self.__reg_gain_gt_4_max_msb = 30
        self.__reg_gain_gt_3_max_lsb = 16
        self.__reg_gain_gt_3_max_msb = 22
        self.__reg_gain_gt_2_max_lsb = 8
        self.__reg_gain_gt_2_max_msb = 14
        self.__reg_gain_gt_1_max_lsb = 0
        self.__reg_gain_gt_1_max_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_gain_gt_4_max(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_gt_4_max_msb, self.__reg_gain_gt_4_max_lsb)
    @reg_gain_gt_4_max.setter
    def reg_gain_gt_4_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_gt_4_max_msb, self.__reg_gain_gt_4_max_lsb, value)

    @property
    def reg_gain_gt_3_max(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_gt_3_max_msb, self.__reg_gain_gt_3_max_lsb)
    @reg_gain_gt_3_max.setter
    def reg_gain_gt_3_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_gt_3_max_msb, self.__reg_gain_gt_3_max_lsb, value)

    @property
    def reg_gain_gt_2_max(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_gt_2_max_msb, self.__reg_gain_gt_2_max_lsb)
    @reg_gain_gt_2_max.setter
    def reg_gain_gt_2_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_gt_2_max_msb, self.__reg_gain_gt_2_max_lsb, value)

    @property
    def reg_gain_gt_1_max(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_gt_1_max_msb, self.__reg_gain_gt_1_max_lsb)
    @reg_gain_gt_1_max.setter
    def reg_gain_gt_1_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_gt_1_max_msb, self.__reg_gain_gt_1_max_lsb, value)
class AGCGAIN_CTRL_10(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x118
        self.__reg_quickdrop_gain_thr_lsb = 24
        self.__reg_quickdrop_gain_thr_msb = 31
        self.__reg_quickdrop_no_pkd2_lsb = 16
        self.__reg_quickdrop_no_pkd2_msb = 23
        self.__reg_quickdrop_pkd_lsb = 8
        self.__reg_quickdrop_pkd_msb = 15
        self.__reg_quickdrop_no_pkd_lsb = 0
        self.__reg_quickdrop_no_pkd_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_quickdrop_gain_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_quickdrop_gain_thr_msb, self.__reg_quickdrop_gain_thr_lsb)
    @reg_quickdrop_gain_thr.setter
    def reg_quickdrop_gain_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_quickdrop_gain_thr_msb, self.__reg_quickdrop_gain_thr_lsb, value)

    @property
    def reg_quickdrop_no_pkd2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_quickdrop_no_pkd2_msb, self.__reg_quickdrop_no_pkd2_lsb)
    @reg_quickdrop_no_pkd2.setter
    def reg_quickdrop_no_pkd2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_quickdrop_no_pkd2_msb, self.__reg_quickdrop_no_pkd2_lsb, value)

    @property
    def reg_quickdrop_pkd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_quickdrop_pkd_msb, self.__reg_quickdrop_pkd_lsb)
    @reg_quickdrop_pkd.setter
    def reg_quickdrop_pkd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_quickdrop_pkd_msb, self.__reg_quickdrop_pkd_lsb, value)

    @property
    def reg_quickdrop_no_pkd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_quickdrop_no_pkd_msb, self.__reg_quickdrop_no_pkd_lsb)
    @reg_quickdrop_no_pkd.setter
    def reg_quickdrop_no_pkd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_quickdrop_no_pkd_msb, self.__reg_quickdrop_no_pkd_lsb, value)
class AGCANT_CTRL1(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x11c
        self.__reg_ant_dc_rm_time_lsb = 16
        self.__reg_ant_dc_rm_time_msb = 22
        self.__reg_ant_mac_en_lsb = 15
        self.__reg_ant_mac_en_msb = 15
        self.__reg_ant_rst_en_lsb = 14
        self.__reg_ant_rst_en_msb = 14
        self.__reg_ant_11b_back_lsb = 13
        self.__reg_ant_11b_back_msb = 13
        self.__reg_ant_cur_force_en_lsb = 12
        self.__reg_ant_cur_force_en_msb = 12
        self.__reg_ant_cur_force_lsb = 11
        self.__reg_ant_cur_force_msb = 11
        self.__reg_gain_ant1_comp_lsb = 4
        self.__reg_gain_ant1_comp_msb = 10
        self.__reg_ant_chk_bt_lsb = 3
        self.__reg_ant_chk_bt_msb = 3
        self.__reg_ant_chk_ofdm2_lsb = 2
        self.__reg_ant_chk_ofdm2_msb = 2
        self.__reg_ant_chk_cck_lsb = 1
        self.__reg_ant_chk_cck_msb = 1
        self.__reg_ant_chk_ofdm_lsb = 0
        self.__reg_ant_chk_ofdm_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ant_dc_rm_time(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ant_dc_rm_time_msb, self.__reg_ant_dc_rm_time_lsb)
    @reg_ant_dc_rm_time.setter
    def reg_ant_dc_rm_time(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ant_dc_rm_time_msb, self.__reg_ant_dc_rm_time_lsb, value)

    @property
    def reg_ant_mac_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ant_mac_en_msb, self.__reg_ant_mac_en_lsb)
    @reg_ant_mac_en.setter
    def reg_ant_mac_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ant_mac_en_msb, self.__reg_ant_mac_en_lsb, value)

    @property
    def reg_ant_rst_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ant_rst_en_msb, self.__reg_ant_rst_en_lsb)
    @reg_ant_rst_en.setter
    def reg_ant_rst_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ant_rst_en_msb, self.__reg_ant_rst_en_lsb, value)

    @property
    def reg_ant_11b_back(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ant_11b_back_msb, self.__reg_ant_11b_back_lsb)
    @reg_ant_11b_back.setter
    def reg_ant_11b_back(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ant_11b_back_msb, self.__reg_ant_11b_back_lsb, value)

    @property
    def reg_ant_cur_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ant_cur_force_en_msb, self.__reg_ant_cur_force_en_lsb)
    @reg_ant_cur_force_en.setter
    def reg_ant_cur_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ant_cur_force_en_msb, self.__reg_ant_cur_force_en_lsb, value)

    @property
    def reg_ant_cur_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ant_cur_force_msb, self.__reg_ant_cur_force_lsb)
    @reg_ant_cur_force.setter
    def reg_ant_cur_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ant_cur_force_msb, self.__reg_ant_cur_force_lsb, value)

    @property
    def reg_gain_ant1_comp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_ant1_comp_msb, self.__reg_gain_ant1_comp_lsb)
    @reg_gain_ant1_comp.setter
    def reg_gain_ant1_comp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_ant1_comp_msb, self.__reg_gain_ant1_comp_lsb, value)

    @property
    def reg_ant_chk_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ant_chk_bt_msb, self.__reg_ant_chk_bt_lsb)
    @reg_ant_chk_bt.setter
    def reg_ant_chk_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ant_chk_bt_msb, self.__reg_ant_chk_bt_lsb, value)

    @property
    def reg_ant_chk_ofdm2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ant_chk_ofdm2_msb, self.__reg_ant_chk_ofdm2_lsb)
    @reg_ant_chk_ofdm2.setter
    def reg_ant_chk_ofdm2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ant_chk_ofdm2_msb, self.__reg_ant_chk_ofdm2_lsb, value)

    @property
    def reg_ant_chk_cck(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ant_chk_cck_msb, self.__reg_ant_chk_cck_lsb)
    @reg_ant_chk_cck.setter
    def reg_ant_chk_cck(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ant_chk_cck_msb, self.__reg_ant_chk_cck_lsb, value)

    @property
    def reg_ant_chk_ofdm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ant_chk_ofdm_msb, self.__reg_ant_chk_ofdm_lsb)
    @reg_ant_chk_ofdm.setter
    def reg_ant_chk_ofdm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ant_chk_ofdm_msb, self.__reg_ant_chk_ofdm_lsb, value)
class AGCANT_CTRL2(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x120
        self.__reg_rssi_ant_bt_thr_lsb = 24
        self.__reg_rssi_ant_bt_thr_msb = 31
        self.__reg_rssi_ant_ofdm2_thr_lsb = 16
        self.__reg_rssi_ant_ofdm2_thr_msb = 23
        self.__reg_rssi_ant_cck_thr_lsb = 8
        self.__reg_rssi_ant_cck_thr_msb = 15
        self.__reg_rssi_ant_ofdm_thr_lsb = 0
        self.__reg_rssi_ant_ofdm_thr_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rssi_ant_bt_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rssi_ant_bt_thr_msb, self.__reg_rssi_ant_bt_thr_lsb)
    @reg_rssi_ant_bt_thr.setter
    def reg_rssi_ant_bt_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rssi_ant_bt_thr_msb, self.__reg_rssi_ant_bt_thr_lsb, value)

    @property
    def reg_rssi_ant_ofdm2_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rssi_ant_ofdm2_thr_msb, self.__reg_rssi_ant_ofdm2_thr_lsb)
    @reg_rssi_ant_ofdm2_thr.setter
    def reg_rssi_ant_ofdm2_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rssi_ant_ofdm2_thr_msb, self.__reg_rssi_ant_ofdm2_thr_lsb, value)

    @property
    def reg_rssi_ant_cck_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rssi_ant_cck_thr_msb, self.__reg_rssi_ant_cck_thr_lsb)
    @reg_rssi_ant_cck_thr.setter
    def reg_rssi_ant_cck_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rssi_ant_cck_thr_msb, self.__reg_rssi_ant_cck_thr_lsb, value)

    @property
    def reg_rssi_ant_ofdm_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rssi_ant_ofdm_thr_msb, self.__reg_rssi_ant_ofdm_thr_lsb)
    @reg_rssi_ant_ofdm_thr.setter
    def reg_rssi_ant_ofdm_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rssi_ant_ofdm_thr_msb, self.__reg_rssi_ant_ofdm_thr_lsb, value)
class AGC11B_CTRL3(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x124
        self.__reg_rssi_2nd_11b_thr_lsb = 24
        self.__reg_rssi_2nd_11b_thr_msb = 31
        self.__reg_bcorr_snr_thr_strong_lsb = 16
        self.__reg_bcorr_snr_thr_strong_msb = 23
        self.__reg_bcorr_pwr_1s_thr_lsb = 10
        self.__reg_bcorr_pwr_1s_thr_msb = 15
        self.__reg_bcorr_pwr_thr_strong_lsb = 4
        self.__reg_bcorr_pwr_thr_strong_msb = 9
        self.__reg_bcorr_lt_ext_cnt_lsb = 0
        self.__reg_bcorr_lt_ext_cnt_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rssi_2nd_11b_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rssi_2nd_11b_thr_msb, self.__reg_rssi_2nd_11b_thr_lsb)
    @reg_rssi_2nd_11b_thr.setter
    def reg_rssi_2nd_11b_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rssi_2nd_11b_thr_msb, self.__reg_rssi_2nd_11b_thr_lsb, value)

    @property
    def reg_bcorr_snr_thr_strong(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bcorr_snr_thr_strong_msb, self.__reg_bcorr_snr_thr_strong_lsb)
    @reg_bcorr_snr_thr_strong.setter
    def reg_bcorr_snr_thr_strong(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bcorr_snr_thr_strong_msb, self.__reg_bcorr_snr_thr_strong_lsb, value)

    @property
    def reg_bcorr_pwr_1s_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bcorr_pwr_1s_thr_msb, self.__reg_bcorr_pwr_1s_thr_lsb)
    @reg_bcorr_pwr_1s_thr.setter
    def reg_bcorr_pwr_1s_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bcorr_pwr_1s_thr_msb, self.__reg_bcorr_pwr_1s_thr_lsb, value)

    @property
    def reg_bcorr_pwr_thr_strong(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bcorr_pwr_thr_strong_msb, self.__reg_bcorr_pwr_thr_strong_lsb)
    @reg_bcorr_pwr_thr_strong.setter
    def reg_bcorr_pwr_thr_strong(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bcorr_pwr_thr_strong_msb, self.__reg_bcorr_pwr_thr_strong_lsb, value)

    @property
    def reg_bcorr_lt_ext_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bcorr_lt_ext_cnt_msb, self.__reg_bcorr_lt_ext_cnt_lsb)
    @reg_bcorr_lt_ext_cnt.setter
    def reg_bcorr_lt_ext_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bcorr_lt_ext_cnt_msb, self.__reg_bcorr_lt_ext_cnt_lsb, value)
class AGCPWR_CTRL20(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x128
        self.__reg_agv_noise_fsdb_min_lsb = 24
        self.__reg_agv_noise_fsdb_min_msb = 31
        self.__r_cal_count_lsb = 12
        self.__r_cal_count_msb = 23
        self.__r_rssi_min_lsb = 0
        self.__r_rssi_min_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_agv_noise_fsdb_min(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agv_noise_fsdb_min_msb, self.__reg_agv_noise_fsdb_min_lsb)
    @reg_agv_noise_fsdb_min.setter
    def reg_agv_noise_fsdb_min(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agv_noise_fsdb_min_msb, self.__reg_agv_noise_fsdb_min_lsb, value)

    @property
    def r_cal_count(self):
        return self.__MEM.rdm(self.__addr, self.__r_cal_count_msb, self.__r_cal_count_lsb)
    @r_cal_count.setter
    def r_cal_count(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_cal_count_msb, self.__r_cal_count_lsb, value)

    @property
    def r_rssi_min(self):
        return self.__MEM.rdm(self.__addr, self.__r_rssi_min_msb, self.__r_rssi_min_lsb)
    @r_rssi_min.setter
    def r_rssi_min(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_rssi_min_msb, self.__r_rssi_min_lsb, value)
class AGCPWR_CTRL21(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x12c
        self.__reg_noise_hold_lsb = 25
        self.__reg_noise_hold_msb = 25
        self.__reg_noise_load_lsb = 24
        self.__reg_noise_load_msb = 24
        self.__reg_cal_count_load_lsb = 12
        self.__reg_cal_count_load_msb = 23
        self.__reg_rssi_min_load_lsb = 0
        self.__reg_rssi_min_load_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_noise_hold(self):
        return self.__MEM.rdm(self.__addr, self.__reg_noise_hold_msb, self.__reg_noise_hold_lsb)
    @reg_noise_hold.setter
    def reg_noise_hold(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_noise_hold_msb, self.__reg_noise_hold_lsb, value)

    @property
    def reg_noise_load(self):
        return self.__MEM.rdm(self.__addr, self.__reg_noise_load_msb, self.__reg_noise_load_lsb)
    @reg_noise_load.setter
    def reg_noise_load(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_noise_load_msb, self.__reg_noise_load_lsb, value)

    @property
    def reg_cal_count_load(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cal_count_load_msb, self.__reg_cal_count_load_lsb)
    @reg_cal_count_load.setter
    def reg_cal_count_load(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cal_count_load_msb, self.__reg_cal_count_load_lsb, value)

    @property
    def reg_rssi_min_load(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rssi_min_load_msb, self.__reg_rssi_min_load_lsb)
    @reg_rssi_min_load.setter
    def reg_rssi_min_load(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rssi_min_load_msb, self.__reg_rssi_min_load_lsb, value)
class AGCPWR_CTRL22(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x130
        self.__reg_rc_filter_noise_en_lsb = 26
        self.__reg_rc_filter_noise_en_msb = 26
        self.__reg_load_noise_rc_init_lsb = 24
        self.__reg_load_noise_rc_init_msb = 24
        self.__reg_noise_rc_init_lsb = 0
        self.__reg_noise_rc_init_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rc_filter_noise_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rc_filter_noise_en_msb, self.__reg_rc_filter_noise_en_lsb)
    @reg_rc_filter_noise_en.setter
    def reg_rc_filter_noise_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rc_filter_noise_en_msb, self.__reg_rc_filter_noise_en_lsb, value)

    @property
    def reg_load_noise_rc_init(self):
        return self.__MEM.rdm(self.__addr, self.__reg_load_noise_rc_init_msb, self.__reg_load_noise_rc_init_lsb)
    @reg_load_noise_rc_init.setter
    def reg_load_noise_rc_init(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_load_noise_rc_init_msb, self.__reg_load_noise_rc_init_lsb, value)

    @property
    def reg_noise_rc_init(self):
        return self.__MEM.rdm(self.__addr, self.__reg_noise_rc_init_msb, self.__reg_noise_rc_init_lsb)
    @reg_noise_rc_init.setter
    def reg_noise_rc_init(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_noise_rc_init_msb, self.__reg_noise_rc_init_lsb, value)
class AGCPWR_CTRL23(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x134
        self.__reg_rc_shift_max_lsb = 24
        self.__reg_rc_shift_max_msb = 26
        self.__reg_noise_rc_in_min_lsb = 12
        self.__reg_noise_rc_in_min_msb = 23
        self.__reg_noise_rc_in_max_lsb = 0
        self.__reg_noise_rc_in_max_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rc_shift_max(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rc_shift_max_msb, self.__reg_rc_shift_max_lsb)
    @reg_rc_shift_max.setter
    def reg_rc_shift_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rc_shift_max_msb, self.__reg_rc_shift_max_lsb, value)

    @property
    def reg_noise_rc_in_min(self):
        return self.__MEM.rdm(self.__addr, self.__reg_noise_rc_in_min_msb, self.__reg_noise_rc_in_min_lsb)
    @reg_noise_rc_in_min.setter
    def reg_noise_rc_in_min(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_noise_rc_in_min_msb, self.__reg_noise_rc_in_min_lsb, value)

    @property
    def reg_noise_rc_in_max(self):
        return self.__MEM.rdm(self.__addr, self.__reg_noise_rc_in_max_msb, self.__reg_noise_rc_in_max_lsb)
    @reg_noise_rc_in_max.setter
    def reg_noise_rc_in_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_noise_rc_in_max_msb, self.__reg_noise_rc_in_max_lsb, value)
class AGCPWR_CTRL24(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x138
        self.__reg_noise_rc_out_lsb = 12
        self.__reg_noise_rc_out_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_noise_rc_out(self):
        return self.__MEM.rdm(self.__addr, self.__reg_noise_rc_out_msb, self.__reg_noise_rc_out_lsb)
    @reg_noise_rc_out.setter
    def reg_noise_rc_out(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_noise_rc_out_msb, self.__reg_noise_rc_out_lsb, value)
class AGCPWR_CTRL25(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x13c
        self.__reg_max_gain_sch_lsb = 18
        self.__reg_max_gain_sch_msb = 24
        self.__reg_pwr_fe_high_find_thr_lsb = 9
        self.__reg_pwr_fe_high_find_thr_msb = 17
        self.__reg_pwr_high_find_thr_lsb = 0
        self.__reg_pwr_high_find_thr_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_max_gain_sch(self):
        return self.__MEM.rdm(self.__addr, self.__reg_max_gain_sch_msb, self.__reg_max_gain_sch_lsb)
    @reg_max_gain_sch.setter
    def reg_max_gain_sch(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_max_gain_sch_msb, self.__reg_max_gain_sch_lsb, value)

    @property
    def reg_pwr_fe_high_find_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fe_high_find_thr_msb, self.__reg_pwr_fe_high_find_thr_lsb)
    @reg_pwr_fe_high_find_thr.setter
    def reg_pwr_fe_high_find_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fe_high_find_thr_msb, self.__reg_pwr_fe_high_find_thr_lsb, value)

    @property
    def reg_pwr_high_find_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_high_find_thr_msb, self.__reg_pwr_high_find_thr_lsb)
    @reg_pwr_high_find_thr.setter
    def reg_pwr_high_find_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_high_find_thr_msb, self.__reg_pwr_high_find_thr_lsb, value)
class AGCPWR_CTRL26(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x140
        self.__reg_rst_pwrtrk_win_lsb = 26
        self.__reg_rst_pwrtrk_win_msb = 26
        self.__reg_restart_pwr_coarse_lsb = 17
        self.__reg_restart_pwr_coarse_msb = 25
        self.__reg_pwr_ant_delta_thr_lsb = 9
        self.__reg_pwr_ant_delta_thr_msb = 16
        self.__reg_pwr_ant_sw_lsb = 0
        self.__reg_pwr_ant_sw_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rst_pwrtrk_win(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rst_pwrtrk_win_msb, self.__reg_rst_pwrtrk_win_lsb)
    @reg_rst_pwrtrk_win.setter
    def reg_rst_pwrtrk_win(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rst_pwrtrk_win_msb, self.__reg_rst_pwrtrk_win_lsb, value)

    @property
    def reg_restart_pwr_coarse(self):
        return self.__MEM.rdm(self.__addr, self.__reg_restart_pwr_coarse_msb, self.__reg_restart_pwr_coarse_lsb)
    @reg_restart_pwr_coarse.setter
    def reg_restart_pwr_coarse(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_restart_pwr_coarse_msb, self.__reg_restart_pwr_coarse_lsb, value)

    @property
    def reg_pwr_ant_delta_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_ant_delta_thr_msb, self.__reg_pwr_ant_delta_thr_lsb)
    @reg_pwr_ant_delta_thr.setter
    def reg_pwr_ant_delta_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_ant_delta_thr_msb, self.__reg_pwr_ant_delta_thr_lsb, value)

    @property
    def reg_pwr_ant_sw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_ant_sw_msb, self.__reg_pwr_ant_sw_lsb)
    @reg_pwr_ant_sw.setter
    def reg_pwr_ant_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_ant_sw_msb, self.__reg_pwr_ant_sw_lsb, value)
class AGCBT_CTRL4(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x144
        self.__reg_pwr_fine_2nd_ofs_bt_lt_lsb = 18
        self.__reg_pwr_fine_2nd_ofs_bt_lt_msb = 23
        self.__reg_pwr_fine_1st_le_lt_lsb = 9
        self.__reg_pwr_fine_1st_le_lt_msb = 17
        self.__reg_pwr_fine_1st_bt_lt_lsb = 0
        self.__reg_pwr_fine_1st_bt_lt_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_pwr_fine_2nd_ofs_bt_lt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_2nd_ofs_bt_lt_msb, self.__reg_pwr_fine_2nd_ofs_bt_lt_lsb)
    @reg_pwr_fine_2nd_ofs_bt_lt.setter
    def reg_pwr_fine_2nd_ofs_bt_lt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_2nd_ofs_bt_lt_msb, self.__reg_pwr_fine_2nd_ofs_bt_lt_lsb, value)

    @property
    def reg_pwr_fine_1st_le_lt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_1st_le_lt_msb, self.__reg_pwr_fine_1st_le_lt_lsb)
    @reg_pwr_fine_1st_le_lt.setter
    def reg_pwr_fine_1st_le_lt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_1st_le_lt_msb, self.__reg_pwr_fine_1st_le_lt_lsb, value)

    @property
    def reg_pwr_fine_1st_bt_lt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_1st_bt_lt_msb, self.__reg_pwr_fine_1st_bt_lt_lsb)
    @reg_pwr_fine_1st_bt_lt.setter
    def reg_pwr_fine_1st_bt_lt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_1st_bt_lt_msb, self.__reg_pwr_fine_1st_bt_lt_lsb, value)
class AGCBT_CTRL5(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x148
        self.__reg_pwr_le_coded_thr_lsb = 16
        self.__reg_pwr_le_coded_thr_msb = 23
        self.__reg_pwr_le_thr_lsb = 8
        self.__reg_pwr_le_thr_msb = 15
        self.__reg_pwr_bt_thr_lsb = 0
        self.__reg_pwr_bt_thr_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_pwr_le_coded_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_le_coded_thr_msb, self.__reg_pwr_le_coded_thr_lsb)
    @reg_pwr_le_coded_thr.setter
    def reg_pwr_le_coded_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_le_coded_thr_msb, self.__reg_pwr_le_coded_thr_lsb, value)

    @property
    def reg_pwr_le_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_le_thr_msb, self.__reg_pwr_le_thr_lsb)
    @reg_pwr_le_thr.setter
    def reg_pwr_le_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_le_thr_msb, self.__reg_pwr_le_thr_lsb, value)

    @property
    def reg_pwr_bt_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_bt_thr_msb, self.__reg_pwr_bt_thr_lsb)
    @reg_pwr_bt_thr.setter
    def reg_pwr_bt_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_bt_thr_msb, self.__reg_pwr_bt_thr_lsb, value)
class AGCFINEGAIN_CTRL(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x14c
        self.__reg_htstf_cnt_lsb = 25
        self.__reg_htstf_cnt_msb = 30
        self.__reg_rssi_ant_ofdm_low_thr_lsb = 17
        self.__reg_rssi_ant_ofdm_low_thr_msb = 24
        self.__reg_fine_gain_offset_lsb = 8
        self.__reg_fine_gain_offset_msb = 16
        self.__reg_fine_rssi_thr_lsb = 0
        self.__reg_fine_rssi_thr_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_htstf_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_htstf_cnt_msb, self.__reg_htstf_cnt_lsb)
    @reg_htstf_cnt.setter
    def reg_htstf_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_htstf_cnt_msb, self.__reg_htstf_cnt_lsb, value)

    @property
    def reg_rssi_ant_ofdm_low_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rssi_ant_ofdm_low_thr_msb, self.__reg_rssi_ant_ofdm_low_thr_lsb)
    @reg_rssi_ant_ofdm_low_thr.setter
    def reg_rssi_ant_ofdm_low_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rssi_ant_ofdm_low_thr_msb, self.__reg_rssi_ant_ofdm_low_thr_lsb, value)

    @property
    def reg_fine_gain_offset(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fine_gain_offset_msb, self.__reg_fine_gain_offset_lsb)
    @reg_fine_gain_offset.setter
    def reg_fine_gain_offset(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fine_gain_offset_msb, self.__reg_fine_gain_offset_lsb, value)

    @property
    def reg_fine_rssi_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fine_rssi_thr_msb, self.__reg_fine_rssi_thr_lsb)
    @reg_fine_rssi_thr.setter
    def reg_fine_rssi_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fine_rssi_thr_msb, self.__reg_fine_rssi_thr_lsb, value)
class AGCRESTART_CTRL(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x150
        self.__reg_pwr_fine_latch_thr_lsb = 20
        self.__reg_pwr_fine_latch_thr_msb = 28
        self.__reg_rest_cnt_end_lsb = 12
        self.__reg_rest_cnt_end_msb = 19
        self.__reg_rest_qkdet_en_lsb = 11
        self.__reg_rest_qkdet_en_msb = 11
        self.__reg_corr_det_cnt_max_rest_lsb = 5
        self.__reg_corr_det_cnt_max_rest_msb = 10
        self.__reg_corr_det_thr_rest_lsb = 0
        self.__reg_corr_det_thr_rest_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_pwr_fine_latch_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_latch_thr_msb, self.__reg_pwr_fine_latch_thr_lsb)
    @reg_pwr_fine_latch_thr.setter
    def reg_pwr_fine_latch_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_latch_thr_msb, self.__reg_pwr_fine_latch_thr_lsb, value)

    @property
    def reg_rest_cnt_end(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rest_cnt_end_msb, self.__reg_rest_cnt_end_lsb)
    @reg_rest_cnt_end.setter
    def reg_rest_cnt_end(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rest_cnt_end_msb, self.__reg_rest_cnt_end_lsb, value)

    @property
    def reg_rest_qkdet_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rest_qkdet_en_msb, self.__reg_rest_qkdet_en_lsb)
    @reg_rest_qkdet_en.setter
    def reg_rest_qkdet_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rest_qkdet_en_msb, self.__reg_rest_qkdet_en_lsb, value)

    @property
    def reg_corr_det_cnt_max_rest(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_det_cnt_max_rest_msb, self.__reg_corr_det_cnt_max_rest_lsb)
    @reg_corr_det_cnt_max_rest.setter
    def reg_corr_det_cnt_max_rest(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_det_cnt_max_rest_msb, self.__reg_corr_det_cnt_max_rest_lsb, value)

    @property
    def reg_corr_det_thr_rest(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_det_thr_rest_msb, self.__reg_corr_det_thr_rest_lsb)
    @reg_corr_det_thr_rest.setter
    def reg_corr_det_thr_rest(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_det_thr_rest_msb, self.__reg_corr_det_thr_rest_lsb, value)
class AGCFSM_CTRL6(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x154
        self.__reg_hpwr_coarse_gain_fast_lsb = 31
        self.__reg_hpwr_coarse_gain_fast_msb = 31
        self.__reg_rssi_latch_sel_lsb = 30
        self.__reg_rssi_latch_sel_msb = 30
        self.__reg_pwr_err_lt_gain_sel_lsb = 29
        self.__reg_pwr_err_lt_gain_sel_msb = 29
        self.__reg_pwr_err_lt_coarse_lsb = 20
        self.__reg_pwr_err_lt_coarse_msb = 28
        self.__reg_min_gain_ext_lsb = 13
        self.__reg_min_gain_ext_msb = 19
        self.__reg_pwr_high_thr_add_lsb = 4
        self.__reg_pwr_high_thr_add_msb = 12
        self.__reg_agc_init_wcnt_lsb = 0
        self.__reg_agc_init_wcnt_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_hpwr_coarse_gain_fast(self):
        return self.__MEM.rdm(self.__addr, self.__reg_hpwr_coarse_gain_fast_msb, self.__reg_hpwr_coarse_gain_fast_lsb)
    @reg_hpwr_coarse_gain_fast.setter
    def reg_hpwr_coarse_gain_fast(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_hpwr_coarse_gain_fast_msb, self.__reg_hpwr_coarse_gain_fast_lsb, value)

    @property
    def reg_rssi_latch_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rssi_latch_sel_msb, self.__reg_rssi_latch_sel_lsb)
    @reg_rssi_latch_sel.setter
    def reg_rssi_latch_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rssi_latch_sel_msb, self.__reg_rssi_latch_sel_lsb, value)

    @property
    def reg_pwr_err_lt_gain_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_err_lt_gain_sel_msb, self.__reg_pwr_err_lt_gain_sel_lsb)
    @reg_pwr_err_lt_gain_sel.setter
    def reg_pwr_err_lt_gain_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_err_lt_gain_sel_msb, self.__reg_pwr_err_lt_gain_sel_lsb, value)

    @property
    def reg_pwr_err_lt_coarse(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_err_lt_coarse_msb, self.__reg_pwr_err_lt_coarse_lsb)
    @reg_pwr_err_lt_coarse.setter
    def reg_pwr_err_lt_coarse(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_err_lt_coarse_msb, self.__reg_pwr_err_lt_coarse_lsb, value)

    @property
    def reg_min_gain_ext(self):
        return self.__MEM.rdm(self.__addr, self.__reg_min_gain_ext_msb, self.__reg_min_gain_ext_lsb)
    @reg_min_gain_ext.setter
    def reg_min_gain_ext(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_min_gain_ext_msb, self.__reg_min_gain_ext_lsb, value)

    @property
    def reg_pwr_high_thr_add(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_high_thr_add_msb, self.__reg_pwr_high_thr_add_lsb)
    @reg_pwr_high_thr_add.setter
    def reg_pwr_high_thr_add(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_high_thr_add_msb, self.__reg_pwr_high_thr_add_lsb, value)

    @property
    def reg_agc_init_wcnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_init_wcnt_msb, self.__reg_agc_init_wcnt_lsb)
    @reg_agc_init_wcnt.setter
    def reg_agc_init_wcnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_init_wcnt_msb, self.__reg_agc_init_wcnt_lsb, value)
class AGCFSM_CTRL7(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x158
        self.__reg_agc_start_delay_err_lsb = 19
        self.__reg_agc_start_delay_err_msb = 28
        self.__reg_agc_start_delay_txend_lsb = 9
        self.__reg_agc_start_delay_txend_msb = 18
        self.__reg_st_wait_exit_en_lsb = 7
        self.__reg_st_wait_exit_en_msb = 8
        self.__reg_adc_valid_time_lsb = 0
        self.__reg_adc_valid_time_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_agc_start_delay_err(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_start_delay_err_msb, self.__reg_agc_start_delay_err_lsb)
    @reg_agc_start_delay_err.setter
    def reg_agc_start_delay_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_start_delay_err_msb, self.__reg_agc_start_delay_err_lsb, value)

    @property
    def reg_agc_start_delay_txend(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_start_delay_txend_msb, self.__reg_agc_start_delay_txend_lsb)
    @reg_agc_start_delay_txend.setter
    def reg_agc_start_delay_txend(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_start_delay_txend_msb, self.__reg_agc_start_delay_txend_lsb, value)

    @property
    def reg_st_wait_exit_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_st_wait_exit_en_msb, self.__reg_st_wait_exit_en_lsb)
    @reg_st_wait_exit_en.setter
    def reg_st_wait_exit_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_st_wait_exit_en_msb, self.__reg_st_wait_exit_en_lsb, value)

    @property
    def reg_adc_valid_time(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_valid_time_msb, self.__reg_adc_valid_time_lsb)
    @reg_adc_valid_time.setter
    def reg_adc_valid_time(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_valid_time_msb, self.__reg_adc_valid_time_lsb, value)
class AGCPD_CTRL(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x15c
        self.__reg_agc_pwr_force_pu_lsb = 1
        self.__reg_agc_pwr_force_pu_msb = 1
        self.__reg_agc_pwr_force_pd_lsb = 0
        self.__reg_agc_pwr_force_pd_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_agc_pwr_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_pwr_force_pu_msb, self.__reg_agc_pwr_force_pu_lsb)
    @reg_agc_pwr_force_pu.setter
    def reg_agc_pwr_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_pwr_force_pu_msb, self.__reg_agc_pwr_force_pu_lsb, value)

    @property
    def reg_agc_pwr_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_pwr_force_pd_msb, self.__reg_agc_pwr_force_pd_lsb)
    @reg_agc_pwr_force_pd.setter
    def reg_agc_pwr_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_pwr_force_pd_msb, self.__reg_agc_pwr_force_pd_lsb, value)
class AGC_WSCAN_CTRL(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x160
        self.__reg_wscan_en_lsb = 0
        self.__reg_wscan_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wscan_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wscan_en_msb, self.__reg_wscan_en_lsb)
    @reg_wscan_en.setter
    def reg_wscan_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wscan_en_msb, self.__reg_wscan_en_lsb, value)
class AGCRD10(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x164
        self.__agc_debug_4_lsb = 0
        self.__agc_debug_4_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def agc_debug_4(self):
        return self.__MEM.rdm(self.__addr, self.__agc_debug_4_msb, self.__agc_debug_4_lsb)
    @agc_debug_4.setter
    def agc_debug_4(self, value):
        return self.__MEM.wrm(self.__addr, self.__agc_debug_4_msb, self.__agc_debug_4_lsb, value)
class AGCRD11(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x168
        self.__agc_debug_5_lsb = 0
        self.__agc_debug_5_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def agc_debug_5(self):
        return self.__MEM.rdm(self.__addr, self.__agc_debug_5_msb, self.__agc_debug_5_lsb)
    @agc_debug_5.setter
    def agc_debug_5(self, value):
        return self.__MEM.wrm(self.__addr, self.__agc_debug_5_msb, self.__agc_debug_5_lsb, value)
class AGCRD12(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x16c
        self.__agc_debug_6_lsb = 0
        self.__agc_debug_6_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def agc_debug_6(self):
        return self.__MEM.rdm(self.__addr, self.__agc_debug_6_msb, self.__agc_debug_6_lsb)
    @agc_debug_6.setter
    def agc_debug_6(self, value):
        return self.__MEM.wrm(self.__addr, self.__agc_debug_6_msb, self.__agc_debug_6_lsb, value)
class AGCRD13(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x170
        self.__agc_debug_7_lsb = 0
        self.__agc_debug_7_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def agc_debug_7(self):
        return self.__MEM.rdm(self.__addr, self.__agc_debug_7_msb, self.__agc_debug_7_lsb)
    @agc_debug_7.setter
    def agc_debug_7(self, value):
        return self.__MEM.wrm(self.__addr, self.__agc_debug_7_msb, self.__agc_debug_7_lsb, value)
class AGCRD14(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x174
        self.__agc_debug_8_lsb = 0
        self.__agc_debug_8_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def agc_debug_8(self):
        return self.__MEM.rdm(self.__addr, self.__agc_debug_8_msb, self.__agc_debug_8_lsb)
    @agc_debug_8.setter
    def agc_debug_8(self, value):
        return self.__MEM.wrm(self.__addr, self.__agc_debug_8_msb, self.__agc_debug_8_lsb, value)
class AGCRD15(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x178
        self.__agc_debug_9_lsb = 0
        self.__agc_debug_9_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def agc_debug_9(self):
        return self.__MEM.rdm(self.__addr, self.__agc_debug_9_msb, self.__agc_debug_9_lsb)
    @agc_debug_9.setter
    def agc_debug_9(self, value):
        return self.__MEM.wrm(self.__addr, self.__agc_debug_9_msb, self.__agc_debug_9_lsb, value)
class AGCRD16(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x17c
        self.__agc_debug_10_lsb = 0
        self.__agc_debug_10_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def agc_debug_10(self):
        return self.__MEM.rdm(self.__addr, self.__agc_debug_10_msb, self.__agc_debug_10_lsb)
    @agc_debug_10.setter
    def agc_debug_10(self, value):
        return self.__MEM.wrm(self.__addr, self.__agc_debug_10_msb, self.__agc_debug_10_lsb, value)
class AGCRD17(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x180
        self.__agc_debug_11_lsb = 0
        self.__agc_debug_11_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def agc_debug_11(self):
        return self.__MEM.rdm(self.__addr, self.__agc_debug_11_msb, self.__agc_debug_11_lsb)
    @agc_debug_11.setter
    def agc_debug_11(self, value):
        return self.__MEM.wrm(self.__addr, self.__agc_debug_11_msb, self.__agc_debug_11_lsb, value)
class AGCRD18(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x184
        self.__agc_debug_12_lsb = 0
        self.__agc_debug_12_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def agc_debug_12(self):
        return self.__MEM.rdm(self.__addr, self.__agc_debug_12_msb, self.__agc_debug_12_lsb)
    @agc_debug_12.setter
    def agc_debug_12(self, value):
        return self.__MEM.wrm(self.__addr, self.__agc_debug_12_msb, self.__agc_debug_12_lsb, value)
class AGCRD19(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x188
        self.__agc_debug_13_lsb = 0
        self.__agc_debug_13_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def agc_debug_13(self):
        return self.__MEM.rdm(self.__addr, self.__agc_debug_13_msb, self.__agc_debug_13_lsb)
    @agc_debug_13.setter
    def agc_debug_13(self, value):
        return self.__MEM.wrm(self.__addr, self.__agc_debug_13_msb, self.__agc_debug_13_lsb, value)
class AGCRD20(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x18c
        self.__agc_debug_14_lsb = 0
        self.__agc_debug_14_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def agc_debug_14(self):
        return self.__MEM.rdm(self.__addr, self.__agc_debug_14_msb, self.__agc_debug_14_lsb)
    @agc_debug_14.setter
    def agc_debug_14(self, value):
        return self.__MEM.wrm(self.__addr, self.__agc_debug_14_msb, self.__agc_debug_14_lsb, value)
class AGCRD21(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x190
        self.__agc_debug_15_lsb = 0
        self.__agc_debug_15_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def agc_debug_15(self):
        return self.__MEM.rdm(self.__addr, self.__agc_debug_15_msb, self.__agc_debug_15_lsb)
    @agc_debug_15.setter
    def agc_debug_15(self, value):
        return self.__MEM.wrm(self.__addr, self.__agc_debug_15_msb, self.__agc_debug_15_lsb, value)
class AGCPWR_CTRL27(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x194
        self.__reg_stbc_pwr_chg_err_lt_thr_lsb = 24
        self.__reg_stbc_pwr_chg_err_lt_thr_msb = 31
        self.__reg_stbc_pwr_chg_err_gt_thr_lsb = 16
        self.__reg_stbc_pwr_chg_err_gt_thr_msb = 23
        self.__reg_adcsat_stbc_rsta_thr_lsb = 10
        self.__reg_adcsat_stbc_rsta_thr_msb = 15
        self.__reg_stbc_pwr_drop_thr_lsb = 5
        self.__reg_stbc_pwr_drop_thr_msb = 9
        self.__reg_stbc_pwr_restart_thr_lsb = 0
        self.__reg_stbc_pwr_restart_thr_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_stbc_pwr_chg_err_lt_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_stbc_pwr_chg_err_lt_thr_msb, self.__reg_stbc_pwr_chg_err_lt_thr_lsb)
    @reg_stbc_pwr_chg_err_lt_thr.setter
    def reg_stbc_pwr_chg_err_lt_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_stbc_pwr_chg_err_lt_thr_msb, self.__reg_stbc_pwr_chg_err_lt_thr_lsb, value)

    @property
    def reg_stbc_pwr_chg_err_gt_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_stbc_pwr_chg_err_gt_thr_msb, self.__reg_stbc_pwr_chg_err_gt_thr_lsb)
    @reg_stbc_pwr_chg_err_gt_thr.setter
    def reg_stbc_pwr_chg_err_gt_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_stbc_pwr_chg_err_gt_thr_msb, self.__reg_stbc_pwr_chg_err_gt_thr_lsb, value)

    @property
    def reg_adcsat_stbc_rsta_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcsat_stbc_rsta_thr_msb, self.__reg_adcsat_stbc_rsta_thr_lsb)
    @reg_adcsat_stbc_rsta_thr.setter
    def reg_adcsat_stbc_rsta_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcsat_stbc_rsta_thr_msb, self.__reg_adcsat_stbc_rsta_thr_lsb, value)

    @property
    def reg_stbc_pwr_drop_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_stbc_pwr_drop_thr_msb, self.__reg_stbc_pwr_drop_thr_lsb)
    @reg_stbc_pwr_drop_thr.setter
    def reg_stbc_pwr_drop_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_stbc_pwr_drop_thr_msb, self.__reg_stbc_pwr_drop_thr_lsb, value)

    @property
    def reg_stbc_pwr_restart_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_stbc_pwr_restart_thr_msb, self.__reg_stbc_pwr_restart_thr_lsb)
    @reg_stbc_pwr_restart_thr.setter
    def reg_stbc_pwr_restart_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_stbc_pwr_restart_thr_msb, self.__reg_stbc_pwr_restart_thr_lsb, value)
class AGCPWR_CTRL28(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x1a0
        self.__reg_pwr_fine_recorrect_le_coded_en_lsb = 29
        self.__reg_pwr_fine_recorrect_le_coded_en_msb = 29
        self.__reg_le_coded_rssi_thr_lsb = 21
        self.__reg_le_coded_rssi_thr_msb = 28
        self.__reg_le_coded_rxpwr_var_thr_lsb = 17
        self.__reg_le_coded_rxpwr_var_thr_msb = 20
        self.__reg_pwr_fine_recorrect_thr_le_coded_lsb = 12
        self.__reg_pwr_fine_recorrect_thr_le_coded_msb = 16
        self.__reg_pwr_drop_thr_le_coded_lsb = 6
        self.__reg_pwr_drop_thr_le_coded_msb = 11
        self.__reg_pwr_restart_thr_le_coded_lsb = 0
        self.__reg_pwr_restart_thr_le_coded_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_pwr_fine_recorrect_le_coded_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_recorrect_le_coded_en_msb, self.__reg_pwr_fine_recorrect_le_coded_en_lsb)
    @reg_pwr_fine_recorrect_le_coded_en.setter
    def reg_pwr_fine_recorrect_le_coded_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_recorrect_le_coded_en_msb, self.__reg_pwr_fine_recorrect_le_coded_en_lsb, value)

    @property
    def reg_le_coded_rssi_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_le_coded_rssi_thr_msb, self.__reg_le_coded_rssi_thr_lsb)
    @reg_le_coded_rssi_thr.setter
    def reg_le_coded_rssi_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_le_coded_rssi_thr_msb, self.__reg_le_coded_rssi_thr_lsb, value)

    @property
    def reg_le_coded_rxpwr_var_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_le_coded_rxpwr_var_thr_msb, self.__reg_le_coded_rxpwr_var_thr_lsb)
    @reg_le_coded_rxpwr_var_thr.setter
    def reg_le_coded_rxpwr_var_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_le_coded_rxpwr_var_thr_msb, self.__reg_le_coded_rxpwr_var_thr_lsb, value)

    @property
    def reg_pwr_fine_recorrect_thr_le_coded(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_recorrect_thr_le_coded_msb, self.__reg_pwr_fine_recorrect_thr_le_coded_lsb)
    @reg_pwr_fine_recorrect_thr_le_coded.setter
    def reg_pwr_fine_recorrect_thr_le_coded(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_recorrect_thr_le_coded_msb, self.__reg_pwr_fine_recorrect_thr_le_coded_lsb, value)

    @property
    def reg_pwr_drop_thr_le_coded(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_drop_thr_le_coded_msb, self.__reg_pwr_drop_thr_le_coded_lsb)
    @reg_pwr_drop_thr_le_coded.setter
    def reg_pwr_drop_thr_le_coded(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_drop_thr_le_coded_msb, self.__reg_pwr_drop_thr_le_coded_lsb, value)

    @property
    def reg_pwr_restart_thr_le_coded(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_restart_thr_le_coded_msb, self.__reg_pwr_restart_thr_le_coded_lsb)
    @reg_pwr_restart_thr_le_coded.setter
    def reg_pwr_restart_thr_le_coded(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_restart_thr_le_coded_msb, self.__reg_pwr_restart_thr_le_coded_lsb, value)
class AGCBT_CTRL6(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x1a4
        self.__reg_sat_rsta_trig_bt_en_lsb = 26
        self.__reg_sat_rsta_trig_bt_en_msb = 26
        self.__reg_init_gain_bt_lsb = 19
        self.__reg_init_gain_bt_msb = 25
        self.__reg_flag_pwr_ok_en_bt_lsb = 18
        self.__reg_flag_pwr_ok_en_bt_msb = 18
        self.__reg_pwr_fine_1st_le_coded_lt_lsb = 9
        self.__reg_pwr_fine_1st_le_coded_lt_msb = 17
        self.__reg_pwr_fine_1st_le_coded_lsb = 0
        self.__reg_pwr_fine_1st_le_coded_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sat_rsta_trig_bt_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sat_rsta_trig_bt_en_msb, self.__reg_sat_rsta_trig_bt_en_lsb)
    @reg_sat_rsta_trig_bt_en.setter
    def reg_sat_rsta_trig_bt_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sat_rsta_trig_bt_en_msb, self.__reg_sat_rsta_trig_bt_en_lsb, value)

    @property
    def reg_init_gain_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_init_gain_bt_msb, self.__reg_init_gain_bt_lsb)
    @reg_init_gain_bt.setter
    def reg_init_gain_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_init_gain_bt_msb, self.__reg_init_gain_bt_lsb, value)

    @property
    def reg_flag_pwr_ok_en_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_flag_pwr_ok_en_bt_msb, self.__reg_flag_pwr_ok_en_bt_lsb)
    @reg_flag_pwr_ok_en_bt.setter
    def reg_flag_pwr_ok_en_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_flag_pwr_ok_en_bt_msb, self.__reg_flag_pwr_ok_en_bt_lsb, value)

    @property
    def reg_pwr_fine_1st_le_coded_lt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_1st_le_coded_lt_msb, self.__reg_pwr_fine_1st_le_coded_lt_lsb)
    @reg_pwr_fine_1st_le_coded_lt.setter
    def reg_pwr_fine_1st_le_coded_lt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_1st_le_coded_lt_msb, self.__reg_pwr_fine_1st_le_coded_lt_lsb, value)

    @property
    def reg_pwr_fine_1st_le_coded(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwr_fine_1st_le_coded_msb, self.__reg_pwr_fine_1st_le_coded_lsb)
    @reg_pwr_fine_1st_le_coded.setter
    def reg_pwr_fine_1st_le_coded(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwr_fine_1st_le_coded_msb, self.__reg_pwr_fine_1st_le_coded_lsb, value)
class AGCBT_CTRL7(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x1a8
        self.__reg_adcsat_rsta_thr_bt_lsb = 26
        self.__reg_adcsat_rsta_thr_bt_msb = 31
        self.__reg_adc_sat2_en_bt_lsb = 25
        self.__reg_adc_sat2_en_bt_msb = 25
        self.__reg_adcsat_sum_thr2_bt_lsb = 20
        self.__reg_adcsat_sum_thr2_bt_msb = 24
        self.__reg_adcsat_sum_thr_bt_lsb = 14
        self.__reg_adcsat_sum_thr_bt_msb = 19
        self.__reg_adcsat_count_max_bt_lsb = 9
        self.__reg_adcsat_count_max_bt_msb = 13
        self.__reg_adcsat_thr_bt_lsb = 0
        self.__reg_adcsat_thr_bt_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_adcsat_rsta_thr_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcsat_rsta_thr_bt_msb, self.__reg_adcsat_rsta_thr_bt_lsb)
    @reg_adcsat_rsta_thr_bt.setter
    def reg_adcsat_rsta_thr_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcsat_rsta_thr_bt_msb, self.__reg_adcsat_rsta_thr_bt_lsb, value)

    @property
    def reg_adc_sat2_en_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_sat2_en_bt_msb, self.__reg_adc_sat2_en_bt_lsb)
    @reg_adc_sat2_en_bt.setter
    def reg_adc_sat2_en_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_sat2_en_bt_msb, self.__reg_adc_sat2_en_bt_lsb, value)

    @property
    def reg_adcsat_sum_thr2_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcsat_sum_thr2_bt_msb, self.__reg_adcsat_sum_thr2_bt_lsb)
    @reg_adcsat_sum_thr2_bt.setter
    def reg_adcsat_sum_thr2_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcsat_sum_thr2_bt_msb, self.__reg_adcsat_sum_thr2_bt_lsb, value)

    @property
    def reg_adcsat_sum_thr_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcsat_sum_thr_bt_msb, self.__reg_adcsat_sum_thr_bt_lsb)
    @reg_adcsat_sum_thr_bt.setter
    def reg_adcsat_sum_thr_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcsat_sum_thr_bt_msb, self.__reg_adcsat_sum_thr_bt_lsb, value)

    @property
    def reg_adcsat_count_max_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcsat_count_max_bt_msb, self.__reg_adcsat_count_max_bt_lsb)
    @reg_adcsat_count_max_bt.setter
    def reg_adcsat_count_max_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcsat_count_max_bt_msb, self.__reg_adcsat_count_max_bt_lsb, value)

    @property
    def reg_adcsat_thr_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcsat_thr_bt_msb, self.__reg_adcsat_thr_bt_lsb)
    @reg_adcsat_thr_bt.setter
    def reg_adcsat_thr_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcsat_thr_bt_msb, self.__reg_adcsat_thr_bt_lsb, value)
class AGCGAIN_CTRL_11(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x1ac
        self.__reg_max_gain_bt_sch_lsb = 0
        self.__reg_max_gain_bt_sch_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_max_gain_bt_sch(self):
        return self.__MEM.rdm(self.__addr, self.__reg_max_gain_bt_sch_msb, self.__reg_max_gain_bt_sch_lsb)
    @reg_max_gain_bt_sch.setter
    def reg_max_gain_bt_sch(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_max_gain_bt_sch_msb, self.__reg_max_gain_bt_sch_lsb, value)
class AGCFSM_CTRL8(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x1b0
        self.__reg_adc_valid_time_bt_lsb = 14
        self.__reg_adc_valid_time_bt_msb = 20
        self.__reg_settling_time_fine_bt_lsb = 7
        self.__reg_settling_time_fine_bt_msb = 13
        self.__reg_settling_time_coarse_bt_lsb = 0
        self.__reg_settling_time_coarse_bt_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_adc_valid_time_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_valid_time_bt_msb, self.__reg_adc_valid_time_bt_lsb)
    @reg_adc_valid_time_bt.setter
    def reg_adc_valid_time_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_valid_time_bt_msb, self.__reg_adc_valid_time_bt_lsb, value)

    @property
    def reg_settling_time_fine_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_settling_time_fine_bt_msb, self.__reg_settling_time_fine_bt_lsb)
    @reg_settling_time_fine_bt.setter
    def reg_settling_time_fine_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_settling_time_fine_bt_msb, self.__reg_settling_time_fine_bt_lsb, value)

    @property
    def reg_settling_time_coarse_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_settling_time_coarse_bt_msb, self.__reg_settling_time_coarse_bt_lsb)
    @reg_settling_time_coarse_bt.setter
    def reg_settling_time_coarse_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_settling_time_coarse_bt_msb, self.__reg_settling_time_coarse_bt_lsb, value)
class AGCNOUSE(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = AGC_BASE + 0x3fc
        self.__reg_agc_date_lsb = 0
        self.__reg_agc_date_msb = 27
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_agc_date(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_date_msb, self.__reg_agc_date_lsb)
    @reg_agc_date.setter
    def reg_agc_date(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_date_msb, self.__reg_agc_date_lsb, value)
    @property
    def default_value(self):
        return 0x1910141
