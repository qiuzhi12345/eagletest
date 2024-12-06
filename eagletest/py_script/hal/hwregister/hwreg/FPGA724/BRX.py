from hal.common import *
from hal.hwregister.hwreg.FPGA724.addr_base import *
class BRX(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.BRXFSM_CNT = BRXFSM_CNT(self.channel, self.chipv)
        self.BRXBARK_CONF = BRXBARK_CONF(self.channel, self.chipv)
        self.BRXERR_CONF = BRXERR_CONF(self.channel, self.chipv)
        self.BRXDC_CONF = BRXDC_CONF(self.channel, self.chipv)
        self.BRXEQU_CONF = BRXEQU_CONF(self.channel, self.chipv)
        self.BRXEQU_TIM0 = BRXEQU_TIM0(self.channel, self.chipv)
        self.BRXEQU_TIM1 = BRXEQU_TIM1(self.channel, self.chipv)
        self.BRXEQU_TIM2 = BRXEQU_TIM2(self.channel, self.chipv)
        self.BRXEQU_TIM3 = BRXEQU_TIM3(self.channel, self.chipv)
        self.BRXPHASE_CONF = BRXPHASE_CONF(self.channel, self.chipv)
        self.BRXPHASE_TIM0 = BRXPHASE_TIM0(self.channel, self.chipv)
        self.BRXPHASE_TIM1 = BRXPHASE_TIM1(self.channel, self.chipv)
        self.BRXPHASE_TIM2 = BRXPHASE_TIM2(self.channel, self.chipv)
        self.BRXPHASE_TIM3 = BRXPHASE_TIM3(self.channel, self.chipv)
        self.BRXPHASE_EVM = BRXPHASE_EVM(self.channel, self.chipv)
        self.BRXFREQ_OFFSET = BRXFREQ_OFFSET(self.channel, self.chipv)
        self.BRXTIM_CONF = BRXTIM_CONF(self.channel, self.chipv)
        self.BRXTIM_READ_DATA = BRXTIM_READ_DATA(self.channel, self.chipv)
        self.BRXTIM_READ_HEAD = BRXTIM_READ_HEAD(self.channel, self.chipv)
        self.BRXSDF_CONF = BRXSDF_CONF(self.channel, self.chipv)
        self.BRXTIM_PPM_COM = BRXTIM_PPM_COM(self.channel, self.chipv)
        self.BRX_TEST = BRX_TEST(self.channel, self.chipv)
        self.BRX_CORR_5P5 = BRX_CORR_5P5(self.channel, self.chipv)
        self.BRXDUMP_CONF = BRXDUMP_CONF(self.channel, self.chipv)
        self.BRX_LR_SYNC = BRX_LR_SYNC(self.channel, self.chipv)
        self.BRX_LR_SDF = BRX_LR_SDF(self.channel, self.chipv)
        self.BRX_LR_HEAD = BRX_LR_HEAD(self.channel, self.chipv)
        self.BRX_LR_DET = BRX_LR_DET(self.channel, self.chipv)
        self.BRX_LR_CONF = BRX_LR_CONF(self.channel, self.chipv)
        self.BRX_LR_CONF1 = BRX_LR_CONF1(self.channel, self.chipv)
        self.BRX_LR_DET2 = BRX_LR_DET2(self.channel, self.chipv)
        self.BRX_LR_SYNC2 = BRX_LR_SYNC2(self.channel, self.chipv)
        self.BRX_LR_WD0 = BRX_LR_WD0(self.channel, self.chipv)
        self.BRX_LR_WD1 = BRX_LR_WD1(self.channel, self.chipv)
        self.BRX_LR_WD2 = BRX_LR_WD2(self.channel, self.chipv)
        self.BRX_LR_WD3 = BRX_LR_WD3(self.channel, self.chipv)
        self.BRXSDF_INV_CONF = BRXSDF_INV_CONF(self.channel, self.chipv)
        self.BRXSNR = BRXSNR(self.channel, self.chipv)
        self.BRXEQU_TIM0_LR = BRXEQU_TIM0_LR(self.channel, self.chipv)
        self.BRXDATE = BRXDATE(self.channel, self.chipv)
class BRXFSM_CNT(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x0
        self.__reg_brx_frcon_bcorr_lsb = 18
        self.__reg_brx_frcon_bcorr_msb = 18
        self.__reg_brx_frcon_fsm_lsb = 17
        self.__reg_brx_frcon_fsm_msb = 17
        self.__reg_brx_frcon_all_lsb = 16
        self.__reg_brx_frcon_all_msb = 16
        self.__reg_scorr_early_lsb = 12
        self.__reg_scorr_early_msb = 12
        self.__reg_bcorr_end_lsb = 6
        self.__reg_bcorr_end_msb = 11
        self.__reg_scorr_start_lsb = 0
        self.__reg_scorr_start_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_brx_frcon_bcorr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_brx_frcon_bcorr_msb, self.__reg_brx_frcon_bcorr_lsb)
    @reg_brx_frcon_bcorr.setter
    def reg_brx_frcon_bcorr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_brx_frcon_bcorr_msb, self.__reg_brx_frcon_bcorr_lsb, value)

    @property
    def reg_brx_frcon_fsm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_brx_frcon_fsm_msb, self.__reg_brx_frcon_fsm_lsb)
    @reg_brx_frcon_fsm.setter
    def reg_brx_frcon_fsm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_brx_frcon_fsm_msb, self.__reg_brx_frcon_fsm_lsb, value)

    @property
    def reg_brx_frcon_all(self):
        return self.__MEM.rdm(self.__addr, self.__reg_brx_frcon_all_msb, self.__reg_brx_frcon_all_lsb)
    @reg_brx_frcon_all.setter
    def reg_brx_frcon_all(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_brx_frcon_all_msb, self.__reg_brx_frcon_all_lsb, value)

    @property
    def reg_scorr_early(self):
        return self.__MEM.rdm(self.__addr, self.__reg_scorr_early_msb, self.__reg_scorr_early_lsb)
    @reg_scorr_early.setter
    def reg_scorr_early(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_scorr_early_msb, self.__reg_scorr_early_lsb, value)

    @property
    def reg_bcorr_end(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bcorr_end_msb, self.__reg_bcorr_end_lsb)
    @reg_bcorr_end.setter
    def reg_bcorr_end(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bcorr_end_msb, self.__reg_bcorr_end_lsb, value)

    @property
    def reg_scorr_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_scorr_start_msb, self.__reg_scorr_start_lsb)
    @reg_scorr_start.setter
    def reg_scorr_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_scorr_start_msb, self.__reg_scorr_start_lsb, value)
class BRXBARK_CONF(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x4
        self.__reg_lr_bcorr_pksrch_us_lsb = 16
        self.__reg_lr_bcorr_pksrch_us_msb = 21
        self.__reg_bcorr_above_thr_lsb = 12
        self.__reg_bcorr_above_thr_msb = 15
        self.__reg_bcorr_above_cnt_thr_lsb = 6
        self.__reg_bcorr_above_cnt_thr_msb = 11
        self.__reg_bcorr_pksrch_us_lsb = 0
        self.__reg_bcorr_pksrch_us_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_lr_bcorr_pksrch_us(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_bcorr_pksrch_us_msb, self.__reg_lr_bcorr_pksrch_us_lsb)
    @reg_lr_bcorr_pksrch_us.setter
    def reg_lr_bcorr_pksrch_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_bcorr_pksrch_us_msb, self.__reg_lr_bcorr_pksrch_us_lsb, value)

    @property
    def reg_bcorr_above_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bcorr_above_thr_msb, self.__reg_bcorr_above_thr_lsb)
    @reg_bcorr_above_thr.setter
    def reg_bcorr_above_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bcorr_above_thr_msb, self.__reg_bcorr_above_thr_lsb, value)

    @property
    def reg_bcorr_above_cnt_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bcorr_above_cnt_thr_msb, self.__reg_bcorr_above_cnt_thr_lsb)
    @reg_bcorr_above_cnt_thr.setter
    def reg_bcorr_above_cnt_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bcorr_above_cnt_thr_msb, self.__reg_bcorr_above_cnt_thr_lsb, value)

    @property
    def reg_bcorr_pksrch_us(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bcorr_pksrch_us_msb, self.__reg_bcorr_pksrch_us_lsb)
    @reg_bcorr_pksrch_us.setter
    def reg_bcorr_pksrch_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bcorr_pksrch_us_msb, self.__reg_bcorr_pksrch_us_lsb, value)
class BRXERR_CONF(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x8
        self.__reg_check_err_lsb = 18
        self.__reg_check_err_msb = 25
        self.__reg_check_lengthbit_lsb = 17
        self.__reg_check_lengthbit_msb = 17
        self.__reg_max_length_lsb = 0
        self.__reg_max_length_msb = 16
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_check_err(self):
        return self.__MEM.rdm(self.__addr, self.__reg_check_err_msb, self.__reg_check_err_lsb)
    @reg_check_err.setter
    def reg_check_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_check_err_msb, self.__reg_check_err_lsb, value)

    @property
    def reg_check_lengthbit(self):
        return self.__MEM.rdm(self.__addr, self.__reg_check_lengthbit_msb, self.__reg_check_lengthbit_lsb)
    @reg_check_lengthbit.setter
    def reg_check_lengthbit(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_check_lengthbit_msb, self.__reg_check_lengthbit_lsb, value)

    @property
    def reg_max_length(self):
        return self.__MEM.rdm(self.__addr, self.__reg_max_length_msb, self.__reg_max_length_lsb)
    @reg_max_length.setter
    def reg_max_length(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_max_length_msb, self.__reg_max_length_lsb, value)
class BRXDC_CONF(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0xc
        self.__reg_stop_dcest_lsb = 0
        self.__reg_stop_dcest_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_stop_dcest(self):
        return self.__MEM.rdm(self.__addr, self.__reg_stop_dcest_msb, self.__reg_stop_dcest_lsb)
    @reg_stop_dcest.setter
    def reg_stop_dcest(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_stop_dcest_msb, self.__reg_stop_dcest_lsb, value)
class BRXEQU_CONF(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x10
        self.__reg_equ_start_cnt_lsb = 16
        self.__reg_equ_start_cnt_msb = 23
        self.__reg_equ_max_shift_lsb = 12
        self.__reg_equ_max_shift_msb = 14
        self.__reg_equ_min_shift_lsb = 8
        self.__reg_equ_min_shift_msb = 10
        self.__reg_err_quant_thr_lsb = 5
        self.__reg_err_quant_thr_msb = 7
        self.__reg_equ_out_scale_lsb = 4
        self.__reg_equ_out_scale_msb = 4
        self.__reg_equ_ena_lsb = 0
        self.__reg_equ_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_equ_start_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_equ_start_cnt_msb, self.__reg_equ_start_cnt_lsb)
    @reg_equ_start_cnt.setter
    def reg_equ_start_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_equ_start_cnt_msb, self.__reg_equ_start_cnt_lsb, value)

    @property
    def reg_equ_max_shift(self):
        return self.__MEM.rdm(self.__addr, self.__reg_equ_max_shift_msb, self.__reg_equ_max_shift_lsb)
    @reg_equ_max_shift.setter
    def reg_equ_max_shift(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_equ_max_shift_msb, self.__reg_equ_max_shift_lsb, value)

    @property
    def reg_equ_min_shift(self):
        return self.__MEM.rdm(self.__addr, self.__reg_equ_min_shift_msb, self.__reg_equ_min_shift_lsb)
    @reg_equ_min_shift.setter
    def reg_equ_min_shift(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_equ_min_shift_msb, self.__reg_equ_min_shift_lsb, value)

    @property
    def reg_err_quant_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_err_quant_thr_msb, self.__reg_err_quant_thr_lsb)
    @reg_err_quant_thr.setter
    def reg_err_quant_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_err_quant_thr_msb, self.__reg_err_quant_thr_lsb, value)

    @property
    def reg_equ_out_scale(self):
        return self.__MEM.rdm(self.__addr, self.__reg_equ_out_scale_msb, self.__reg_equ_out_scale_lsb)
    @reg_equ_out_scale.setter
    def reg_equ_out_scale(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_equ_out_scale_msb, self.__reg_equ_out_scale_lsb, value)

    @property
    def reg_equ_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_equ_ena_msb, self.__reg_equ_ena_lsb)
    @reg_equ_ena.setter
    def reg_equ_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_equ_ena_msb, self.__reg_equ_ena_lsb, value)
class BRXEQU_TIM0(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x14
        self.__reg_equ_est_cnt_lsb = 16
        self.__reg_equ_est_cnt_msb = 27
        self.__reg_equ_bypass_cnt_lsb = 0
        self.__reg_equ_bypass_cnt_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_equ_est_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_equ_est_cnt_msb, self.__reg_equ_est_cnt_lsb)
    @reg_equ_est_cnt.setter
    def reg_equ_est_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_equ_est_cnt_msb, self.__reg_equ_est_cnt_lsb, value)

    @property
    def reg_equ_bypass_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_equ_bypass_cnt_msb, self.__reg_equ_bypass_cnt_lsb)
    @reg_equ_bypass_cnt.setter
    def reg_equ_bypass_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_equ_bypass_cnt_msb, self.__reg_equ_bypass_cnt_lsb, value)
class BRXEQU_TIM1(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x18
        self.__reg_equ_st2_cnt_lsb = 16
        self.__reg_equ_st2_cnt_msb = 27
        self.__reg_equ_st1_cnt_lsb = 0
        self.__reg_equ_st1_cnt_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_equ_st2_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_equ_st2_cnt_msb, self.__reg_equ_st2_cnt_lsb)
    @reg_equ_st2_cnt.setter
    def reg_equ_st2_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_equ_st2_cnt_msb, self.__reg_equ_st2_cnt_lsb, value)

    @property
    def reg_equ_st1_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_equ_st1_cnt_msb, self.__reg_equ_st1_cnt_lsb)
    @reg_equ_st1_cnt.setter
    def reg_equ_st1_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_equ_st1_cnt_msb, self.__reg_equ_st1_cnt_lsb, value)
class BRXEQU_TIM2(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x1c
        self.__reg_equ_st4_cnt_lsb = 16
        self.__reg_equ_st4_cnt_msb = 27
        self.__reg_equ_st3_cnt_lsb = 0
        self.__reg_equ_st3_cnt_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_equ_st4_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_equ_st4_cnt_msb, self.__reg_equ_st4_cnt_lsb)
    @reg_equ_st4_cnt.setter
    def reg_equ_st4_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_equ_st4_cnt_msb, self.__reg_equ_st4_cnt_lsb, value)

    @property
    def reg_equ_st3_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_equ_st3_cnt_msb, self.__reg_equ_st3_cnt_lsb)
    @reg_equ_st3_cnt.setter
    def reg_equ_st3_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_equ_st3_cnt_msb, self.__reg_equ_st3_cnt_lsb, value)
class BRXEQU_TIM3(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x20
        self.__reg_equ_st6_cnt_lsb = 16
        self.__reg_equ_st6_cnt_msb = 27
        self.__reg_equ_st5_cnt_lsb = 0
        self.__reg_equ_st5_cnt_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_equ_st6_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_equ_st6_cnt_msb, self.__reg_equ_st6_cnt_lsb)
    @reg_equ_st6_cnt.setter
    def reg_equ_st6_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_equ_st6_cnt_msb, self.__reg_equ_st6_cnt_lsb, value)

    @property
    def reg_equ_st5_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_equ_st5_cnt_msb, self.__reg_equ_st5_cnt_lsb)
    @reg_equ_st5_cnt.setter
    def reg_equ_st5_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_equ_st5_cnt_msb, self.__reg_equ_st5_cnt_lsb, value)
class BRXPHASE_CONF(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x24
        self.__reg_phase_comp_mode_lsb = 28
        self.__reg_phase_comp_mode_msb = 29
        self.__reg_freq_shift_lsb = 24
        self.__reg_freq_shift_msb = 25
        self.__reg_phase_start_cnt_lsb = 16
        self.__reg_phase_start_cnt_msb = 23
        self.__reg_phase_cck_adj_lsb = 14
        self.__reg_phase_cck_adj_msb = 15
        self.__reg_phase_qsk_adj_lsb = 12
        self.__reg_phase_qsk_adj_msb = 13
        self.__reg_phase_max_shift_lsb = 8
        self.__reg_phase_max_shift_msb = 10
        self.__reg_phase_min_shift_lsb = 4
        self.__reg_phase_min_shift_msb = 6
        self.__reg_max_freq_lsb = 2
        self.__reg_max_freq_msb = 3
        self.__reg_dis_trace_freq_lsb = 1
        self.__reg_dis_trace_freq_msb = 1
        self.__reg_dis_coarse_freq_lsb = 0
        self.__reg_dis_coarse_freq_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_phase_comp_mode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_phase_comp_mode_msb, self.__reg_phase_comp_mode_lsb)
    @reg_phase_comp_mode.setter
    def reg_phase_comp_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_phase_comp_mode_msb, self.__reg_phase_comp_mode_lsb, value)

    @property
    def reg_freq_shift(self):
        return self.__MEM.rdm(self.__addr, self.__reg_freq_shift_msb, self.__reg_freq_shift_lsb)
    @reg_freq_shift.setter
    def reg_freq_shift(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_freq_shift_msb, self.__reg_freq_shift_lsb, value)

    @property
    def reg_phase_start_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_phase_start_cnt_msb, self.__reg_phase_start_cnt_lsb)
    @reg_phase_start_cnt.setter
    def reg_phase_start_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_phase_start_cnt_msb, self.__reg_phase_start_cnt_lsb, value)

    @property
    def reg_phase_cck_adj(self):
        return self.__MEM.rdm(self.__addr, self.__reg_phase_cck_adj_msb, self.__reg_phase_cck_adj_lsb)
    @reg_phase_cck_adj.setter
    def reg_phase_cck_adj(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_phase_cck_adj_msb, self.__reg_phase_cck_adj_lsb, value)

    @property
    def reg_phase_qsk_adj(self):
        return self.__MEM.rdm(self.__addr, self.__reg_phase_qsk_adj_msb, self.__reg_phase_qsk_adj_lsb)
    @reg_phase_qsk_adj.setter
    def reg_phase_qsk_adj(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_phase_qsk_adj_msb, self.__reg_phase_qsk_adj_lsb, value)

    @property
    def reg_phase_max_shift(self):
        return self.__MEM.rdm(self.__addr, self.__reg_phase_max_shift_msb, self.__reg_phase_max_shift_lsb)
    @reg_phase_max_shift.setter
    def reg_phase_max_shift(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_phase_max_shift_msb, self.__reg_phase_max_shift_lsb, value)

    @property
    def reg_phase_min_shift(self):
        return self.__MEM.rdm(self.__addr, self.__reg_phase_min_shift_msb, self.__reg_phase_min_shift_lsb)
    @reg_phase_min_shift.setter
    def reg_phase_min_shift(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_phase_min_shift_msb, self.__reg_phase_min_shift_lsb, value)

    @property
    def reg_max_freq(self):
        return self.__MEM.rdm(self.__addr, self.__reg_max_freq_msb, self.__reg_max_freq_lsb)
    @reg_max_freq.setter
    def reg_max_freq(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_max_freq_msb, self.__reg_max_freq_lsb, value)

    @property
    def reg_dis_trace_freq(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dis_trace_freq_msb, self.__reg_dis_trace_freq_lsb)
    @reg_dis_trace_freq.setter
    def reg_dis_trace_freq(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dis_trace_freq_msb, self.__reg_dis_trace_freq_lsb, value)

    @property
    def reg_dis_coarse_freq(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dis_coarse_freq_msb, self.__reg_dis_coarse_freq_lsb)
    @reg_dis_coarse_freq.setter
    def reg_dis_coarse_freq(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dis_coarse_freq_msb, self.__reg_dis_coarse_freq_lsb, value)
class BRXPHASE_TIM0(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x28
        self.__reg_phase_st2_cnt_lsb = 16
        self.__reg_phase_st2_cnt_msb = 27
        self.__reg_phase_st1_cnt_lsb = 0
        self.__reg_phase_st1_cnt_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_phase_st2_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_phase_st2_cnt_msb, self.__reg_phase_st2_cnt_lsb)
    @reg_phase_st2_cnt.setter
    def reg_phase_st2_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_phase_st2_cnt_msb, self.__reg_phase_st2_cnt_lsb, value)

    @property
    def reg_phase_st1_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_phase_st1_cnt_msb, self.__reg_phase_st1_cnt_lsb)
    @reg_phase_st1_cnt.setter
    def reg_phase_st1_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_phase_st1_cnt_msb, self.__reg_phase_st1_cnt_lsb, value)
class BRXPHASE_TIM1(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x2c
        self.__reg_phase_st4_cnt_lsb = 16
        self.__reg_phase_st4_cnt_msb = 27
        self.__reg_phase_st3_cnt_lsb = 0
        self.__reg_phase_st3_cnt_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_phase_st4_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_phase_st4_cnt_msb, self.__reg_phase_st4_cnt_lsb)
    @reg_phase_st4_cnt.setter
    def reg_phase_st4_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_phase_st4_cnt_msb, self.__reg_phase_st4_cnt_lsb, value)

    @property
    def reg_phase_st3_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_phase_st3_cnt_msb, self.__reg_phase_st3_cnt_lsb)
    @reg_phase_st3_cnt.setter
    def reg_phase_st3_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_phase_st3_cnt_msb, self.__reg_phase_st3_cnt_lsb, value)
class BRXPHASE_TIM2(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x30
        self.__reg_phase_st6_cnt_lsb = 16
        self.__reg_phase_st6_cnt_msb = 27
        self.__reg_phase_st5_cnt_lsb = 0
        self.__reg_phase_st5_cnt_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_phase_st6_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_phase_st6_cnt_msb, self.__reg_phase_st6_cnt_lsb)
    @reg_phase_st6_cnt.setter
    def reg_phase_st6_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_phase_st6_cnt_msb, self.__reg_phase_st6_cnt_lsb, value)

    @property
    def reg_phase_st5_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_phase_st5_cnt_msb, self.__reg_phase_st5_cnt_lsb)
    @reg_phase_st5_cnt.setter
    def reg_phase_st5_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_phase_st5_cnt_msb, self.__reg_phase_st5_cnt_lsb, value)
class BRXPHASE_TIM3(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x34
        self.__reg_phase_st7_cnt_lsb = 0
        self.__reg_phase_st7_cnt_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_phase_st7_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_phase_st7_cnt_msb, self.__reg_phase_st7_cnt_lsb)
    @reg_phase_st7_cnt.setter
    def reg_phase_st7_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_phase_st7_cnt_msb, self.__reg_phase_st7_cnt_lsb, value)
class BRXPHASE_EVM(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x38
        self.__phase_evm_head_lsb = 16
        self.__phase_evm_head_msb = 31
        self.__phase_evm_data_lsb = 0
        self.__phase_evm_data_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def phase_evm_head(self):
        return self.__MEM.rdm(self.__addr, self.__phase_evm_head_msb, self.__phase_evm_head_lsb)
    @phase_evm_head.setter
    def phase_evm_head(self, value):
        return self.__MEM.wrm(self.__addr, self.__phase_evm_head_msb, self.__phase_evm_head_lsb, value)

    @property
    def phase_evm_data(self):
        return self.__MEM.rdm(self.__addr, self.__phase_evm_data_msb, self.__phase_evm_data_lsb)
    @phase_evm_data.setter
    def phase_evm_data(self, value):
        return self.__MEM.wrm(self.__addr, self.__phase_evm_data_msb, self.__phase_evm_data_lsb, value)
class BRXFREQ_OFFSET(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x3c
        self.__freq_offset_head_lsb = 16
        self.__freq_offset_head_msb = 31
        self.__freq_offset_data_lsb = 0
        self.__freq_offset_data_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def freq_offset_head(self):
        return self.__MEM.rdm(self.__addr, self.__freq_offset_head_msb, self.__freq_offset_head_lsb)
    @freq_offset_head.setter
    def freq_offset_head(self, value):
        return self.__MEM.wrm(self.__addr, self.__freq_offset_head_msb, self.__freq_offset_head_lsb, value)

    @property
    def freq_offset_data(self):
        return self.__MEM.rdm(self.__addr, self.__freq_offset_data_msb, self.__freq_offset_data_lsb)
    @freq_offset_data.setter
    def freq_offset_data(self, value):
        return self.__MEM.wrm(self.__addr, self.__freq_offset_data_msb, self.__freq_offset_data_lsb, value)
class BRXTIM_CONF(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x40
        self.__reg_tim_start_cnt_lsb = 20
        self.__reg_tim_start_cnt_msb = 31
        self.__reg_tim_coeff_lsb = 12
        self.__reg_tim_coeff_msb = 18
        self.__reg_tdelta_shift_lsb = 8
        self.__reg_tdelta_shift_msb = 9
        self.__reg_ppm_shift_lsb = 6
        self.__reg_ppm_shift_msb = 7
        self.__reg_check_lock_lsb = 4
        self.__reg_check_lock_msb = 5
        self.__reg_head_lock_lsb = 3
        self.__reg_head_lock_msb = 3
        self.__reg_dis_trace_tdelta_lsb = 2
        self.__reg_dis_trace_tdelta_msb = 2
        self.__reg_dis_trace_ppm_lsb = 1
        self.__reg_dis_trace_ppm_msb = 1
        self.__reg_dis_coarse_ppm_lsb = 0
        self.__reg_dis_coarse_ppm_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tim_start_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tim_start_cnt_msb, self.__reg_tim_start_cnt_lsb)
    @reg_tim_start_cnt.setter
    def reg_tim_start_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tim_start_cnt_msb, self.__reg_tim_start_cnt_lsb, value)

    @property
    def reg_tim_coeff(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tim_coeff_msb, self.__reg_tim_coeff_lsb)
    @reg_tim_coeff.setter
    def reg_tim_coeff(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tim_coeff_msb, self.__reg_tim_coeff_lsb, value)

    @property
    def reg_tdelta_shift(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tdelta_shift_msb, self.__reg_tdelta_shift_lsb)
    @reg_tdelta_shift.setter
    def reg_tdelta_shift(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tdelta_shift_msb, self.__reg_tdelta_shift_lsb, value)

    @property
    def reg_ppm_shift(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ppm_shift_msb, self.__reg_ppm_shift_lsb)
    @reg_ppm_shift.setter
    def reg_ppm_shift(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ppm_shift_msb, self.__reg_ppm_shift_lsb, value)

    @property
    def reg_check_lock(self):
        return self.__MEM.rdm(self.__addr, self.__reg_check_lock_msb, self.__reg_check_lock_lsb)
    @reg_check_lock.setter
    def reg_check_lock(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_check_lock_msb, self.__reg_check_lock_lsb, value)

    @property
    def reg_head_lock(self):
        return self.__MEM.rdm(self.__addr, self.__reg_head_lock_msb, self.__reg_head_lock_lsb)
    @reg_head_lock.setter
    def reg_head_lock(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_head_lock_msb, self.__reg_head_lock_lsb, value)

    @property
    def reg_dis_trace_tdelta(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dis_trace_tdelta_msb, self.__reg_dis_trace_tdelta_lsb)
    @reg_dis_trace_tdelta.setter
    def reg_dis_trace_tdelta(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dis_trace_tdelta_msb, self.__reg_dis_trace_tdelta_lsb, value)

    @property
    def reg_dis_trace_ppm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dis_trace_ppm_msb, self.__reg_dis_trace_ppm_lsb)
    @reg_dis_trace_ppm.setter
    def reg_dis_trace_ppm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dis_trace_ppm_msb, self.__reg_dis_trace_ppm_lsb, value)

    @property
    def reg_dis_coarse_ppm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dis_coarse_ppm_msb, self.__reg_dis_coarse_ppm_lsb)
    @reg_dis_coarse_ppm.setter
    def reg_dis_coarse_ppm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dis_coarse_ppm_msb, self.__reg_dis_coarse_ppm_lsb, value)
class BRXTIM_READ_DATA(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x44
        self.__tim_ppm_data_lsb = 18
        self.__tim_ppm_data_msb = 31
        self.__tim_ptr_data_lsb = 0
        self.__tim_ptr_data_msb = 16
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tim_ppm_data(self):
        return self.__MEM.rdm(self.__addr, self.__tim_ppm_data_msb, self.__tim_ppm_data_lsb)
    @tim_ppm_data.setter
    def tim_ppm_data(self, value):
        return self.__MEM.wrm(self.__addr, self.__tim_ppm_data_msb, self.__tim_ppm_data_lsb, value)

    @property
    def tim_ptr_data(self):
        return self.__MEM.rdm(self.__addr, self.__tim_ptr_data_msb, self.__tim_ptr_data_lsb)
    @tim_ptr_data.setter
    def tim_ptr_data(self, value):
        return self.__MEM.wrm(self.__addr, self.__tim_ptr_data_msb, self.__tim_ptr_data_lsb, value)
class BRXTIM_READ_HEAD(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x48
        self.__tim_ppm_head_lsb = 18
        self.__tim_ppm_head_msb = 31
        self.__tim_ptr_head_lsb = 0
        self.__tim_ptr_head_msb = 16
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tim_ppm_head(self):
        return self.__MEM.rdm(self.__addr, self.__tim_ppm_head_msb, self.__tim_ppm_head_lsb)
    @tim_ppm_head.setter
    def tim_ppm_head(self, value):
        return self.__MEM.wrm(self.__addr, self.__tim_ppm_head_msb, self.__tim_ppm_head_lsb, value)

    @property
    def tim_ptr_head(self):
        return self.__MEM.rdm(self.__addr, self.__tim_ptr_head_msb, self.__tim_ptr_head_lsb)
    @tim_ptr_head.setter
    def tim_ptr_head(self, value):
        return self.__MEM.wrm(self.__addr, self.__tim_ptr_head_msb, self.__tim_ptr_head_lsb, value)
class BRXSDF_CONF(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x4c
        self.__reg_short_sfd_bitwidth_lsb = 20
        self.__reg_short_sfd_bitwidth_msb = 24
        self.__reg_long_sfd_bitwidth_lsb = 12
        self.__reg_long_sfd_bitwidth_msb = 16
        self.__reg_sfd_search_us_lsb = 0
        self.__reg_sfd_search_us_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_short_sfd_bitwidth(self):
        return self.__MEM.rdm(self.__addr, self.__reg_short_sfd_bitwidth_msb, self.__reg_short_sfd_bitwidth_lsb)
    @reg_short_sfd_bitwidth.setter
    def reg_short_sfd_bitwidth(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_short_sfd_bitwidth_msb, self.__reg_short_sfd_bitwidth_lsb, value)

    @property
    def reg_long_sfd_bitwidth(self):
        return self.__MEM.rdm(self.__addr, self.__reg_long_sfd_bitwidth_msb, self.__reg_long_sfd_bitwidth_lsb)
    @reg_long_sfd_bitwidth.setter
    def reg_long_sfd_bitwidth(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_long_sfd_bitwidth_msb, self.__reg_long_sfd_bitwidth_lsb, value)

    @property
    def reg_sfd_search_us(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sfd_search_us_msb, self.__reg_sfd_search_us_lsb)
    @reg_sfd_search_us.setter
    def reg_sfd_search_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sfd_search_us_msb, self.__reg_sfd_search_us_lsb, value)
class BRXTIM_PPM_COM(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x50
        self.__reg_tim_correct_ptr_lsb = 9
        self.__reg_tim_correct_ptr_msb = 14
        self.__reg_tim_ppm_correct_lsb = 0
        self.__reg_tim_ppm_correct_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tim_correct_ptr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tim_correct_ptr_msb, self.__reg_tim_correct_ptr_lsb)
    @reg_tim_correct_ptr.setter
    def reg_tim_correct_ptr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tim_correct_ptr_msb, self.__reg_tim_correct_ptr_lsb, value)

    @property
    def reg_tim_ppm_correct(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tim_ppm_correct_msb, self.__reg_tim_ppm_correct_lsb)
    @reg_tim_ppm_correct.setter
    def reg_tim_ppm_correct(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tim_ppm_correct_msb, self.__reg_tim_ppm_correct_lsb, value)
class BRX_TEST(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x54
        self.__reg_brxclk_en_lsb = 0
        self.__reg_brxclk_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_brxclk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_brxclk_en_msb, self.__reg_brxclk_en_lsb)
    @reg_brxclk_en.setter
    def reg_brxclk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_brxclk_en_msb, self.__reg_brxclk_en_lsb, value)
class BRX_CORR_5P5(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x58
        self.__reg_corr_5p5_en_lsb = 16
        self.__reg_corr_5p5_en_msb = 16
        self.__reg_corr_thres1_lsb = 8
        self.__reg_corr_thres1_msb = 15
        self.__reg_corr_thres2_lsb = 0
        self.__reg_corr_thres2_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_corr_5p5_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_5p5_en_msb, self.__reg_corr_5p5_en_lsb)
    @reg_corr_5p5_en.setter
    def reg_corr_5p5_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_5p5_en_msb, self.__reg_corr_5p5_en_lsb, value)

    @property
    def reg_corr_thres1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_thres1_msb, self.__reg_corr_thres1_lsb)
    @reg_corr_thres1.setter
    def reg_corr_thres1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_thres1_msb, self.__reg_corr_thres1_lsb, value)

    @property
    def reg_corr_thres2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_corr_thres2_msb, self.__reg_corr_thres2_lsb)
    @reg_corr_thres2.setter
    def reg_corr_thres2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_corr_thres2_msb, self.__reg_corr_thres2_lsb, value)
class BRXDUMP_CONF(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x5c
        self.__reg_brx_mac_inf_sel_lsb = 0
        self.__reg_brx_mac_inf_sel_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_brx_mac_inf_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_brx_mac_inf_sel_msb, self.__reg_brx_mac_inf_sel_lsb)
    @reg_brx_mac_inf_sel.setter
    def reg_brx_mac_inf_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_brx_mac_inf_sel_msb, self.__reg_brx_mac_inf_sel_lsb, value)
class BRX_LR_SYNC(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x60
        self.__reg_lr_state_end_us_lsb = 24
        self.__reg_lr_state_end_us_msb = 29
        self.__reg_lr_state_start_us_lsb = 16
        self.__reg_lr_state_start_us_msb = 21
        self.__reg_lr_state_thr_lsb = 12
        self.__reg_lr_state_thr_msb = 15
        self.__reg_lr_peak_enable_lsb = 11
        self.__reg_lr_peak_enable_msb = 11
        self.__reg_lr_enable_lsb = 10
        self.__reg_lr_enable_msb = 10
        self.__reg_lr_bcorr_above_cnt_thr_lsb = 4
        self.__reg_lr_bcorr_above_cnt_thr_msb = 9
        self.__reg_lr_bcorr_above_thr_lsb = 0
        self.__reg_lr_bcorr_above_thr_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_lr_state_end_us(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_state_end_us_msb, self.__reg_lr_state_end_us_lsb)
    @reg_lr_state_end_us.setter
    def reg_lr_state_end_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_state_end_us_msb, self.__reg_lr_state_end_us_lsb, value)

    @property
    def reg_lr_state_start_us(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_state_start_us_msb, self.__reg_lr_state_start_us_lsb)
    @reg_lr_state_start_us.setter
    def reg_lr_state_start_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_state_start_us_msb, self.__reg_lr_state_start_us_lsb, value)

    @property
    def reg_lr_state_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_state_thr_msb, self.__reg_lr_state_thr_lsb)
    @reg_lr_state_thr.setter
    def reg_lr_state_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_state_thr_msb, self.__reg_lr_state_thr_lsb, value)

    @property
    def reg_lr_peak_enable(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_peak_enable_msb, self.__reg_lr_peak_enable_lsb)
    @reg_lr_peak_enable.setter
    def reg_lr_peak_enable(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_peak_enable_msb, self.__reg_lr_peak_enable_lsb, value)

    @property
    def reg_lr_enable(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_enable_msb, self.__reg_lr_enable_lsb)
    @reg_lr_enable.setter
    def reg_lr_enable(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_enable_msb, self.__reg_lr_enable_lsb, value)

    @property
    def reg_lr_bcorr_above_cnt_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_bcorr_above_cnt_thr_msb, self.__reg_lr_bcorr_above_cnt_thr_lsb)
    @reg_lr_bcorr_above_cnt_thr.setter
    def reg_lr_bcorr_above_cnt_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_bcorr_above_cnt_thr_msb, self.__reg_lr_bcorr_above_cnt_thr_lsb, value)

    @property
    def reg_lr_bcorr_above_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_bcorr_above_thr_msb, self.__reg_lr_bcorr_above_thr_lsb)
    @reg_lr_bcorr_above_thr.setter
    def reg_lr_bcorr_above_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_bcorr_above_thr_msb, self.__reg_lr_bcorr_above_thr_lsb, value)
class BRX_LR_SDF(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x64
        self.__reg_lr_sfd_search_us_lsb = 16
        self.__reg_lr_sfd_search_us_msb = 27
        self.__reg_lr_sfd_value_lsb = 0
        self.__reg_lr_sfd_value_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_lr_sfd_search_us(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_sfd_search_us_msb, self.__reg_lr_sfd_search_us_lsb)
    @reg_lr_sfd_search_us.setter
    def reg_lr_sfd_search_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_sfd_search_us_msb, self.__reg_lr_sfd_search_us_lsb, value)

    @property
    def reg_lr_sfd_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_sfd_value_msb, self.__reg_lr_sfd_value_lsb)
    @reg_lr_sfd_value.setter
    def reg_lr_sfd_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_sfd_value_msb, self.__reg_lr_sfd_value_lsb, value)
class BRX_LR_HEAD(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x68
        self.__reg_lr_headx2x4_thr_lsb = 16
        self.__reg_lr_headx2x4_thr_msb = 19
        self.__reg_lr_headx2_thr_lsb = 12
        self.__reg_lr_headx2_thr_msb = 15
        self.__reg_lr_headx4_thr_lsb = 8
        self.__reg_lr_headx4_thr_msb = 11
        self.__reg_lr_headx1x2_thr_lsb = 4
        self.__reg_lr_headx1x2_thr_msb = 7
        self.__reg_lr_headx1x4_thr_lsb = 0
        self.__reg_lr_headx1x4_thr_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_lr_headx2x4_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_headx2x4_thr_msb, self.__reg_lr_headx2x4_thr_lsb)
    @reg_lr_headx2x4_thr.setter
    def reg_lr_headx2x4_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_headx2x4_thr_msb, self.__reg_lr_headx2x4_thr_lsb, value)

    @property
    def reg_lr_headx2_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_headx2_thr_msb, self.__reg_lr_headx2_thr_lsb)
    @reg_lr_headx2_thr.setter
    def reg_lr_headx2_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_headx2_thr_msb, self.__reg_lr_headx2_thr_lsb, value)

    @property
    def reg_lr_headx4_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_headx4_thr_msb, self.__reg_lr_headx4_thr_lsb)
    @reg_lr_headx4_thr.setter
    def reg_lr_headx4_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_headx4_thr_msb, self.__reg_lr_headx4_thr_lsb, value)

    @property
    def reg_lr_headx1x2_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_headx1x2_thr_msb, self.__reg_lr_headx1x2_thr_lsb)
    @reg_lr_headx1x2_thr.setter
    def reg_lr_headx1x2_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_headx1x2_thr_msb, self.__reg_lr_headx1x2_thr_lsb, value)

    @property
    def reg_lr_headx1x4_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_headx1x4_thr_msb, self.__reg_lr_headx1x4_thr_lsb)
    @reg_lr_headx1x4_thr.setter
    def reg_lr_headx1x4_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_headx1x4_thr_msb, self.__reg_lr_headx1x4_thr_lsb, value)
class BRX_LR_DET(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x6c
        self.__reg_bcorr_shift_lsb = 20
        self.__reg_bcorr_shift_msb = 22
        self.__reg_lr_scorr_us_lsb = 16
        self.__reg_lr_scorr_us_msb = 19
        self.__reg_lr_above_win_lsb = 12
        self.__reg_lr_above_win_msb = 14
        self.__reg_lr_above_cnt_enable_lsb = 7
        self.__reg_lr_above_cnt_enable_msb = 7
        self.__reg_lr_above_cnt_lsb = 4
        self.__reg_lr_above_cnt_msb = 6
        self.__reg_lr_above_us_enable_lsb = 7
        self.__reg_lr_above_us_enable_msb = 7
        self.__reg_lr_above_us_lsb = 4
        self.__reg_lr_above_us_msb = 6
        self.__reg_lr_max_cnt_thr_lsb = 0
        self.__reg_lr_max_cnt_thr_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bcorr_shift(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bcorr_shift_msb, self.__reg_bcorr_shift_lsb)
    @reg_bcorr_shift.setter
    def reg_bcorr_shift(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bcorr_shift_msb, self.__reg_bcorr_shift_lsb, value)

    @property
    def reg_lr_scorr_us(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_scorr_us_msb, self.__reg_lr_scorr_us_lsb)
    @reg_lr_scorr_us.setter
    def reg_lr_scorr_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_scorr_us_msb, self.__reg_lr_scorr_us_lsb, value)

    @property
    def reg_lr_above_win(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_above_win_msb, self.__reg_lr_above_win_lsb)
    @reg_lr_above_win.setter
    def reg_lr_above_win(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_above_win_msb, self.__reg_lr_above_win_lsb, value)

    @property
    def reg_lr_above_cnt_enable(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_above_cnt_enable_msb, self.__reg_lr_above_cnt_enable_lsb)
    @reg_lr_above_cnt_enable.setter
    def reg_lr_above_cnt_enable(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_above_cnt_enable_msb, self.__reg_lr_above_cnt_enable_lsb, value)

    @property
    def reg_lr_above_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_above_cnt_msb, self.__reg_lr_above_cnt_lsb)
    @reg_lr_above_cnt.setter
    def reg_lr_above_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_above_cnt_msb, self.__reg_lr_above_cnt_lsb, value)

    @property
    def reg_lr_above_us_enable(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_above_us_enable_msb, self.__reg_lr_above_us_enable_lsb)
    @reg_lr_above_us_enable.setter
    def reg_lr_above_us_enable(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_above_us_enable_msb, self.__reg_lr_above_us_enable_lsb, value)

    @property
    def reg_lr_above_us(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_above_us_msb, self.__reg_lr_above_us_lsb)
    @reg_lr_above_us.setter
    def reg_lr_above_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_above_us_msb, self.__reg_lr_above_us_lsb, value)

    @property
    def reg_lr_max_cnt_thr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_max_cnt_thr_msb, self.__reg_lr_max_cnt_thr_lsb)
    @reg_lr_max_cnt_thr.setter
    def reg_lr_max_cnt_thr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_max_cnt_thr_msb, self.__reg_lr_max_cnt_thr_lsb, value)
class BRX_LR_CONF(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x70
        self.__reg_lr_above_conf_lsb = 0
        self.__reg_lr_above_conf_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_lr_above_conf(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_above_conf_msb, self.__reg_lr_above_conf_lsb)
    @reg_lr_above_conf.setter
    def reg_lr_above_conf(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_above_conf_msb, self.__reg_lr_above_conf_lsb, value)
class BRX_LR_CONF1(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x74
        self.__reg_lr_above_conf1_lsb = 0
        self.__reg_lr_above_conf1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_lr_above_conf1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_above_conf1_msb, self.__reg_lr_above_conf1_lsb)
    @reg_lr_above_conf1.setter
    def reg_lr_above_conf1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_above_conf1_msb, self.__reg_lr_above_conf1_lsb, value)
class BRX_LR_DET2(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x78
        self.__reg_bcorr_shift2_lsb = 20
        self.__reg_bcorr_shift2_msb = 22
        self.__reg_lr_scorr_us2_lsb = 16
        self.__reg_lr_scorr_us2_msb = 19
        self.__reg_lr_above_win2_lsb = 12
        self.__reg_lr_above_win2_msb = 14
        self.__reg_lr_above_cnt_enable2_lsb = 7
        self.__reg_lr_above_cnt_enable2_msb = 7
        self.__reg_lr_above_cnt2_lsb = 4
        self.__reg_lr_above_cnt2_msb = 6
        self.__reg_lr_above_us_enable2_lsb = 7
        self.__reg_lr_above_us_enable2_msb = 7
        self.__reg_lr_above_us2_lsb = 4
        self.__reg_lr_above_us2_msb = 6
        self.__reg_lr_max_cnt_thr2_lsb = 0
        self.__reg_lr_max_cnt_thr2_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bcorr_shift2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bcorr_shift2_msb, self.__reg_bcorr_shift2_lsb)
    @reg_bcorr_shift2.setter
    def reg_bcorr_shift2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bcorr_shift2_msb, self.__reg_bcorr_shift2_lsb, value)

    @property
    def reg_lr_scorr_us2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_scorr_us2_msb, self.__reg_lr_scorr_us2_lsb)
    @reg_lr_scorr_us2.setter
    def reg_lr_scorr_us2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_scorr_us2_msb, self.__reg_lr_scorr_us2_lsb, value)

    @property
    def reg_lr_above_win2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_above_win2_msb, self.__reg_lr_above_win2_lsb)
    @reg_lr_above_win2.setter
    def reg_lr_above_win2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_above_win2_msb, self.__reg_lr_above_win2_lsb, value)

    @property
    def reg_lr_above_cnt_enable2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_above_cnt_enable2_msb, self.__reg_lr_above_cnt_enable2_lsb)
    @reg_lr_above_cnt_enable2.setter
    def reg_lr_above_cnt_enable2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_above_cnt_enable2_msb, self.__reg_lr_above_cnt_enable2_lsb, value)

    @property
    def reg_lr_above_cnt2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_above_cnt2_msb, self.__reg_lr_above_cnt2_lsb)
    @reg_lr_above_cnt2.setter
    def reg_lr_above_cnt2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_above_cnt2_msb, self.__reg_lr_above_cnt2_lsb, value)

    @property
    def reg_lr_above_us_enable2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_above_us_enable2_msb, self.__reg_lr_above_us_enable2_lsb)
    @reg_lr_above_us_enable2.setter
    def reg_lr_above_us_enable2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_above_us_enable2_msb, self.__reg_lr_above_us_enable2_lsb, value)

    @property
    def reg_lr_above_us2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_above_us2_msb, self.__reg_lr_above_us2_lsb)
    @reg_lr_above_us2.setter
    def reg_lr_above_us2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_above_us2_msb, self.__reg_lr_above_us2_lsb, value)

    @property
    def reg_lr_max_cnt_thr2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_max_cnt_thr2_msb, self.__reg_lr_max_cnt_thr2_lsb)
    @reg_lr_max_cnt_thr2.setter
    def reg_lr_max_cnt_thr2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_max_cnt_thr2_msb, self.__reg_lr_max_cnt_thr2_lsb, value)
class BRX_LR_SYNC2(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x7c
        self.__reg_lr_state_end_us2_lsb = 24
        self.__reg_lr_state_end_us2_msb = 29
        self.__reg_lr_state_start_us2_lsb = 16
        self.__reg_lr_state_start_us2_msb = 21
        self.__reg_lr_state_thr2_lsb = 12
        self.__reg_lr_state_thr2_msb = 15
        self.__reg_lr_peak_enable2_lsb = 11
        self.__reg_lr_peak_enable2_msb = 11
        self.__reg_lr_bcorr_above_cnt_thr2_lsb = 4
        self.__reg_lr_bcorr_above_cnt_thr2_msb = 9
        self.__reg_lr_bcorr_above_thr2_lsb = 0
        self.__reg_lr_bcorr_above_thr2_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_lr_state_end_us2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_state_end_us2_msb, self.__reg_lr_state_end_us2_lsb)
    @reg_lr_state_end_us2.setter
    def reg_lr_state_end_us2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_state_end_us2_msb, self.__reg_lr_state_end_us2_lsb, value)

    @property
    def reg_lr_state_start_us2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_state_start_us2_msb, self.__reg_lr_state_start_us2_lsb)
    @reg_lr_state_start_us2.setter
    def reg_lr_state_start_us2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_state_start_us2_msb, self.__reg_lr_state_start_us2_lsb, value)

    @property
    def reg_lr_state_thr2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_state_thr2_msb, self.__reg_lr_state_thr2_lsb)
    @reg_lr_state_thr2.setter
    def reg_lr_state_thr2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_state_thr2_msb, self.__reg_lr_state_thr2_lsb, value)

    @property
    def reg_lr_peak_enable2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_peak_enable2_msb, self.__reg_lr_peak_enable2_lsb)
    @reg_lr_peak_enable2.setter
    def reg_lr_peak_enable2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_peak_enable2_msb, self.__reg_lr_peak_enable2_lsb, value)

    @property
    def reg_lr_bcorr_above_cnt_thr2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_bcorr_above_cnt_thr2_msb, self.__reg_lr_bcorr_above_cnt_thr2_lsb)
    @reg_lr_bcorr_above_cnt_thr2.setter
    def reg_lr_bcorr_above_cnt_thr2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_bcorr_above_cnt_thr2_msb, self.__reg_lr_bcorr_above_cnt_thr2_lsb, value)

    @property
    def reg_lr_bcorr_above_thr2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_bcorr_above_thr2_msb, self.__reg_lr_bcorr_above_thr2_lsb)
    @reg_lr_bcorr_above_thr2.setter
    def reg_lr_bcorr_above_thr2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_bcorr_above_thr2_msb, self.__reg_lr_bcorr_above_thr2_lsb, value)
class BRX_LR_WD0(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x80
        self.__reg_lr_sfd_wd0_lsb = 0
        self.__reg_lr_sfd_wd0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_lr_sfd_wd0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_sfd_wd0_msb, self.__reg_lr_sfd_wd0_lsb)
    @reg_lr_sfd_wd0.setter
    def reg_lr_sfd_wd0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_sfd_wd0_msb, self.__reg_lr_sfd_wd0_lsb, value)
class BRX_LR_WD1(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x84
        self.__reg_lr_sfd_wd1_lsb = 0
        self.__reg_lr_sfd_wd1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_lr_sfd_wd1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_sfd_wd1_msb, self.__reg_lr_sfd_wd1_lsb)
    @reg_lr_sfd_wd1.setter
    def reg_lr_sfd_wd1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_sfd_wd1_msb, self.__reg_lr_sfd_wd1_lsb, value)
class BRX_LR_WD2(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x88
        self.__reg_lr_sfd_wd2_lsb = 0
        self.__reg_lr_sfd_wd2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_lr_sfd_wd2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_sfd_wd2_msb, self.__reg_lr_sfd_wd2_lsb)
    @reg_lr_sfd_wd2.setter
    def reg_lr_sfd_wd2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_sfd_wd2_msb, self.__reg_lr_sfd_wd2_lsb, value)
class BRX_LR_WD3(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x8c
        self.__reg_lr_sfd_wd3_lsb = 0
        self.__reg_lr_sfd_wd3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_lr_sfd_wd3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lr_sfd_wd3_msb, self.__reg_lr_sfd_wd3_lsb)
    @reg_lr_sfd_wd3.setter
    def reg_lr_sfd_wd3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lr_sfd_wd3_msb, self.__reg_lr_sfd_wd3_lsb, value)
class BRXSDF_INV_CONF(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x90
        self.__reg_inv_short_sfd_bitwidth_lsb = 20
        self.__reg_inv_short_sfd_bitwidth_msb = 24
        self.__reg_inv_long_sfd_bitwidth_lsb = 12
        self.__reg_inv_long_sfd_bitwidth_msb = 16
        self.__reg_inv_short_sfd_enable_lsb = 1
        self.__reg_inv_short_sfd_enable_msb = 1
        self.__reg_inv_long_sfd_enable_lsb = 0
        self.__reg_inv_long_sfd_enable_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_inv_short_sfd_bitwidth(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inv_short_sfd_bitwidth_msb, self.__reg_inv_short_sfd_bitwidth_lsb)
    @reg_inv_short_sfd_bitwidth.setter
    def reg_inv_short_sfd_bitwidth(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inv_short_sfd_bitwidth_msb, self.__reg_inv_short_sfd_bitwidth_lsb, value)

    @property
    def reg_inv_long_sfd_bitwidth(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inv_long_sfd_bitwidth_msb, self.__reg_inv_long_sfd_bitwidth_lsb)
    @reg_inv_long_sfd_bitwidth.setter
    def reg_inv_long_sfd_bitwidth(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inv_long_sfd_bitwidth_msb, self.__reg_inv_long_sfd_bitwidth_lsb, value)

    @property
    def reg_inv_short_sfd_enable(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inv_short_sfd_enable_msb, self.__reg_inv_short_sfd_enable_lsb)
    @reg_inv_short_sfd_enable.setter
    def reg_inv_short_sfd_enable(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inv_short_sfd_enable_msb, self.__reg_inv_short_sfd_enable_lsb, value)

    @property
    def reg_inv_long_sfd_enable(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inv_long_sfd_enable_msb, self.__reg_inv_long_sfd_enable_lsb)
    @reg_inv_long_sfd_enable.setter
    def reg_inv_long_sfd_enable(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inv_long_sfd_enable_msb, self.__reg_inv_long_sfd_enable_lsb, value)
class BRXSNR(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x94
        self.__bcorr_snr_lsb = 0
        self.__bcorr_snr_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def bcorr_snr(self):
        return self.__MEM.rdm(self.__addr, self.__bcorr_snr_msb, self.__bcorr_snr_lsb)
    @bcorr_snr.setter
    def bcorr_snr(self, value):
        return self.__MEM.wrm(self.__addr, self.__bcorr_snr_msb, self.__bcorr_snr_lsb, value)
class BRXEQU_TIM0_LR(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x98
        self.__reg_equ_est_cnt_lr_lsb = 16
        self.__reg_equ_est_cnt_lr_msb = 27
        self.__reg_equ_bypass_wait_lr_lsb = 15
        self.__reg_equ_bypass_wait_lr_msb = 15
        self.__reg_equ_bypass_cnt_lr_lsb = 0
        self.__reg_equ_bypass_cnt_lr_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_equ_est_cnt_lr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_equ_est_cnt_lr_msb, self.__reg_equ_est_cnt_lr_lsb)
    @reg_equ_est_cnt_lr.setter
    def reg_equ_est_cnt_lr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_equ_est_cnt_lr_msb, self.__reg_equ_est_cnt_lr_lsb, value)

    @property
    def reg_equ_bypass_wait_lr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_equ_bypass_wait_lr_msb, self.__reg_equ_bypass_wait_lr_lsb)
    @reg_equ_bypass_wait_lr.setter
    def reg_equ_bypass_wait_lr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_equ_bypass_wait_lr_msb, self.__reg_equ_bypass_wait_lr_lsb, value)

    @property
    def reg_equ_bypass_cnt_lr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_equ_bypass_cnt_lr_msb, self.__reg_equ_bypass_cnt_lr_lsb)
    @reg_equ_bypass_cnt_lr.setter
    def reg_equ_bypass_cnt_lr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_equ_bypass_cnt_lr_msb, self.__reg_equ_bypass_cnt_lr_lsb, value)
class BRXDATE(object):
    def __init__(self, channel, chipv = "FPGA724"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = BRX_BASE + 0x384
        self.__reg_brx_date_lsb = 0
        self.__reg_brx_date_msb = 27
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_brx_date(self):
        return self.__MEM.rdm(self.__addr, self.__reg_brx_date_msb, self.__reg_brx_date_lsb)
    @reg_brx_date.setter
    def reg_brx_date(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_brx_date_msb, self.__reg_brx_date_lsb, value)
    @property
    def default_value(self):
        return 0x1604281
