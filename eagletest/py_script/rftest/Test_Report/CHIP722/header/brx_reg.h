
#define BRXFSM_CNT_REG (REG_BRX_BASE + 0x0000)
#define BRX_FRCON_BCORR (BIT(18))
#define BRX_FRCON_BCORR_S 18
#define BRX_FRCON_FSM (BIT(17))
#define BRX_FRCON_FSM_S 17
#define BRX_FRCON_ALL (BIT(16))
#define BRX_FRCON_ALL_S 16
#define BRX_SCORR_EARLY (BIT(12))
#define BRX_SCORR_EARLY_S 12
#define BRX_BCORR_END 0x0000003F
#define BRX_BCORR_END_S 6
#define BRX_SCORR_START 0x0000003F
#define BRX_SCORR_START_S 0

#define BRXBARK_CONF_REG (REG_BRX_BASE + 0x0004)
#define BRX_LR_BCORR_PKSRCH_US 0x0000003F
#define BRX_LR_BCORR_PKSRCH_US_S 16
#define BRX_BCORR_ABOVE_THR 0x0000000F
#define BRX_BCORR_ABOVE_THR_S 12
#define BRX_BCORR_ABOVE_CNT_THR 0x0000003F
#define BRX_BCORR_ABOVE_CNT_THR_S 6
#define BRX_BCORR_PKSRCH_US 0x0000003F
#define BRX_BCORR_PKSRCH_US_S 0

#define BRXERR_CONF_REG (REG_BRX_BASE + 0x0008)
#define BRX_CHECK_ERR 0x000000FF
#define BRX_CHECK_ERR_S 18
#define BRX_CHECK_LENGTHBIT (BIT(17))
#define BRX_CHECK_LENGTHBIT_S 17
#define BRX_MAX_LENGTH 0x0001FFFF
#define BRX_MAX_LENGTH_S 0

#define BRXDC_CONF_REG (REG_BRX_BASE + 0x000C)
#define BRX_STOP_DCEST 0x00000003
#define BRX_STOP_DCEST_S 0

#define BRXEQU_CONF_REG (REG_BRX_BASE + 0x0010)
#define BRX_EQU_START_CNT 0x000000FF
#define BRX_EQU_START_CNT_S 16
#define BRX_EQU_MAX_SHIFT 0x00000007
#define BRX_EQU_MAX_SHIFT_S 12
#define BRX_EQU_MIN_SHIFT 0x00000007
#define BRX_EQU_MIN_SHIFT_S 8
#define BRX_ERR_QUANT_THR 0x00000007
#define BRX_ERR_QUANT_THR_S 5
#define BRX_EQU_OUT_SCALE (BIT(4))
#define BRX_EQU_OUT_SCALE_S 4
#define BRX_EQU_ENA (BIT(0))
#define BRX_EQU_ENA_S 0

#define BRXEQU_TIM0_REG (REG_BRX_BASE + 0x0014)
#define BRX_EQU_EST_CNT 0x00000FFF
#define BRX_EQU_EST_CNT_S 16
#define BRX_EQU_BYPASS_CNT 0x00000FFF
#define BRX_EQU_BYPASS_CNT_S 0

#define BRXEQU_TIM1_REG (REG_BRX_BASE + 0x0018)
#define BRX_EQU_ST2_CNT 0x00000FFF
#define BRX_EQU_ST2_CNT_S 16
#define BRX_EQU_ST1_CNT 0x00000FFF
#define BRX_EQU_ST1_CNT_S 0

#define BRXEQU_TIM2_REG (REG_BRX_BASE + 0x001C)
#define BRX_EQU_ST4_CNT 0x00000FFF
#define BRX_EQU_ST4_CNT_S 16
#define BRX_EQU_ST3_CNT 0x00000FFF
#define BRX_EQU_ST3_CNT_S 0

#define BRXEQU_TIM3_REG (REG_BRX_BASE + 0x0020)
#define BRX_EQU_ST6_CNT 0x00000FFF
#define BRX_EQU_ST6_CNT_S 16
#define BRX_EQU_ST5_CNT 0x00000FFF
#define BRX_EQU_ST5_CNT_S 0

#define BRXPHASE_CONF_REG (REG_BRX_BASE + 0x0024)
#define BRX_PHASE_COMP_MODE 0x00000003
#define BRX_PHASE_COMP_MODE_S 28
#define BRX_FREQ_SHIFT 0x00000003
#define BRX_FREQ_SHIFT_S 24
#define BRX_PHASE_START_CNT 0x000000FF
#define BRX_PHASE_START_CNT_S 16
#define BRX_PHASE_CCK_ADJ 0x00000003
#define BRX_PHASE_CCK_ADJ_S 14
#define BRX_PHASE_QSK_ADJ 0x00000003
#define BRX_PHASE_QSK_ADJ_S 12
#define BRX_PHASE_MAX_SHIFT 0x00000007
#define BRX_PHASE_MAX_SHIFT_S 8
#define BRX_PHASE_MIN_SHIFT 0x00000007
#define BRX_PHASE_MIN_SHIFT_S 4
#define BRX_MAX_FREQ 0x00000003
#define BRX_MAX_FREQ_S 2
#define BRX_DIS_TRACE_FREQ (BIT(1))
#define BRX_DIS_TRACE_FREQ_S 1
#define BRX_DIS_COARSE_FREQ (BIT(0))
#define BRX_DIS_COARSE_FREQ_S 0

#define BRXPHASE_TIM0_REG (REG_BRX_BASE + 0x0028)
#define BRX_PHASE_ST2_CNT 0x00000FFF
#define BRX_PHASE_ST2_CNT_S 16
#define BRX_PHASE_ST1_CNT 0x00000FFF
#define BRX_PHASE_ST1_CNT_S 0

#define BRXPHASE_TIM1_REG (REG_BRX_BASE + 0x002C)
#define BRX_PHASE_ST4_CNT 0x00000FFF
#define BRX_PHASE_ST4_CNT_S 16
#define BRX_PHASE_ST3_CNT 0x00000FFF
#define BRX_PHASE_ST3_CNT_S 0

#define BRXPHASE_TIM2_REG (REG_BRX_BASE + 0x0030)
#define BRX_PHASE_ST6_CNT 0x00000FFF
#define BRX_PHASE_ST6_CNT_S 16
#define BRX_PHASE_ST5_CNT 0x00000FFF
#define BRX_PHASE_ST5_CNT_S 0

#define BRXPHASE_TIM3_REG (REG_BRX_BASE + 0x0034)
#define BRX_PHASE_ST7_CNT 0x00000FFF
#define BRX_PHASE_ST7_CNT_S 0

#define BRXPHASE_EVM_REG (REG_BRX_BASE + 0x0038)
#define BRX_PHASE_EVM_HEAD 0x0000FFFF
#define BRX_PHASE_EVM_HEAD_S 16
#define BRX_PHASE_EVM_DATA 0x0000FFFF
#define BRX_PHASE_EVM_DATA_S 0

#define BRXFREQ_OFFSET_REG (REG_BRX_BASE + 0x003C)
#define BRX_FREQ_OFFSET_HEAD 0x0000FFFF
#define BRX_FREQ_OFFSET_HEAD_S 16
#define BRX_FREQ_OFFSET_DATA 0x0000FFFF
#define BRX_FREQ_OFFSET_DATA_S 0

#define BRXTIM_CONF_REG (REG_BRX_BASE + 0x0040)
#define BRX_TIM_START_CNT 0x00000FFF
#define BRX_TIM_START_CNT_S 20
#define BRX_TIM_COEFF 0x0000007F
#define BRX_TIM_COEFF_S 12
#define BRX_TDELTA_SHIFT 0x00000003
#define BRX_TDELTA_SHIFT_S 8
#define BRX_PPM_SHIFT 0x00000003
#define BRX_PPM_SHIFT_S 6
#define BRX_CHECK_LOCK 0x00000003
#define BRX_CHECK_LOCK_S 4
#define BRX_HEAD_LOCK (BIT(3))
#define BRX_HEAD_LOCK_S 3
#define BRX_DIS_TRACE_TDELTA (BIT(2))
#define BRX_DIS_TRACE_TDELTA_S 2
#define BRX_DIS_TRACE_PPM (BIT(1))
#define BRX_DIS_TRACE_PPM_S 1
#define BRX_DIS_COARSE_PPM (BIT(0))
#define BRX_DIS_COARSE_PPM_S 0

#define BRXTIM_READ_DATA_REG (REG_BRX_BASE + 0x0044)
#define BRX_TIM_PPM_DATA 0x00003FFF
#define BRX_TIM_PPM_DATA_S 18
#define BRX_TIM_PTR_DATA 0x0001FFFF
#define BRX_TIM_PTR_DATA_S 0

#define BRXTIM_READ_HEAD_REG (REG_BRX_BASE + 0x0048)
#define BRX_TIM_PPM_HEAD 0x00003FFF
#define BRX_TIM_PPM_HEAD_S 18
#define BRX_TIM_PTR_HEAD 0x0001FFFF
#define BRX_TIM_PTR_HEAD_S 0

#define BRXSDF_CONF_REG (REG_BRX_BASE + 0x004C)
#define BRX_SHORT_SFD_BITWIDTH 0x0000001F
#define BRX_SHORT_SFD_BITWIDTH_S 20
#define BRX_LONG_SFD_BITWIDTH 0x0000001F
#define BRX_LONG_SFD_BITWIDTH_S 12
#define BRX_SFD_SEARCH_US 0x00000FFF
#define BRX_SFD_SEARCH_US_S 0

#define BRXTIM_PPM_COM_REG (REG_BRX_BASE + 0x0050)
#define BRX_TIM_CORRECT_PTR 0x0000003F
#define BRX_TIM_CORRECT_PTR_S 9
#define BRX_TIM_PPM_CORRECT 0x000001FF
#define BRX_TIM_PPM_CORRECT_S 0

#define BRX_TEST_REG (REG_BRX_BASE + 0x0054)
#define BRXCLK_EN (BIT(0))
#define BRXCLK_EN_S 0

#define BRX_CORR_5P5_REG (REG_BRX_BASE + 0x0058)
#define BRX_CORR_5P5_EN (BIT(16))
#define BRX_CORR_5P5_EN_S 16
#define BRX_CORR_THRES1 0x000000FF
#define BRX_CORR_THRES1_S 8
#define BRX_CORR_THRES2 0x000000FF
#define BRX_CORR_THRES2_S 0

#define BRXDUMP_CONF_REG (REG_BRX_BASE + 0x005c)
#define BRX_MAC_INF_SEL 0x0000000F
#define BRX_MAC_INF_SEL_S 0

#define BRX_LR_SYNC_REG (REG_BRX_BASE + 0x0060)
#define BRX_LR_STATE_END_US 0x0000003F
#define BRX_LR_STATE_END_US_S 24
#define BRX_LR_STATE_START_US 0x0000003F
#define BRX_LR_STATE_START_US_S 16
#define BRX_LR_STATE_THR 0x0000000F
#define BRX_LR_STATE_THR_S 12
#define BRX_LR_PEAK_ENABLE (BIT(11))
#define BRX_LR_PEAK_ENABLE_S 11
#define BRX_LR_ENABLE (BIT(10))
#define BRX_LR_ENABLE_S 10
#define BRX_LR_BCORR_ABOVE_CNT_THR 0x0000003F
#define BRX_LR_BCORR_ABOVE_CNT_THR_S 4
#define BRX_LR_BCORR_ABOVE_THR 0x0000000F
#define BRX_LR_BCORR_ABOVE_THR_S 0

#define BRX_LR_SDF_REG (REG_BRX_BASE + 0x0064)
#define BRX_LR_SFD_SEARCH_US 0x00000FFF
#define BRX_LR_SFD_SEARCH_US_S 16
#define BRX_LR_SFD_VALUE 0x0000FFFF
#define BRX_LR_SFD_VALUE_S 0

#define BRX_LR_HEAD_REG (REG_BRX_BASE + 0x0068)
#define BRX_LR_HEADX2X4_THR 0x0000000F
#define BRX_LR_HEADX2X4_THR_S 16
#define BRX_LR_HEADX2_THR 0x0000000F
#define BRX_LR_HEADX2_THR_S 12
#define BRX_LR_HEADX4_THR 0x0000000F
#define BRX_LR_HEADX4_THR_S 8
#define BRX_LR_HEADX1X2_THR 0x0000000F
#define BRX_LR_HEADX1X2_THR_S 4
#define BRX_LR_HEADX1X4_THR 0x0000000F
#define BRX_LR_HEADX1X4_THR_S 0

#define BRX_LR_DET_REG (REG_BRX_BASE + 0x006C)
#define BRX_BCORR_SHIFT 0x00000007
#define BRX_BCORR_SHIFT_S 20
#define BRX_LR_SCORR_US 0x0000000F
#define BRX_LR_SCORR_US_S 16
#define BRX_LR_ABOVE_WIN 0x00000007
#define BRX_LR_ABOVE_WIN_S 12
#define BRX_LR_ABOVE_CNT_ENABLE (BIT(7))
#define BRX_LR_ABOVE_CNT_ENABLE_S 7
#define BRX_LR_ABOVE_CNT 0x00000007
#define BRX_LR_ABOVE_CNT_S 4
#define BRX_LR_ABOVE_US_ENABLE (BIT(7))
#define BRX_LR_ABOVE_US_ENABLE_S 7
#define BRX_LR_ABOVE_US 0x00000007
#define BRX_LR_ABOVE_US_S 4
#define BRX_LR_MAX_CNT_THR 0x00000007
#define BRX_LR_MAX_CNT_THR_S 0

#define BRX_LR_CONF_REG (REG_BRX_BASE + 0x0070)
#define BRX_LR_ABOVE_CONF 0xFFFFFFFF
#define BRX_LR_ABOVE_CONF_S 0

#define BRX_LR_CONF1_REG (REG_BRX_BASE + 0x0074)
#define BRX_LR_ABOVE_CONF1 0xFFFFFFFF
#define BRX_LR_ABOVE_CONF1_S 0

#define BRX_LR_DET2_REG (REG_BRX_BASE + 0x0078)
#define BRX_BCORR_SHIFT2 0x00000007
#define BRX_BCORR_SHIFT2_S 20
#define BRX_LR_SCORR_US2 0x0000000F
#define BRX_LR_SCORR_US2_S 16
#define BRX_LR_ABOVE_WIN2 0x00000007
#define BRX_LR_ABOVE_WIN2_S 12
#define BRX_LR_ABOVE_CNT_ENABLE2 (BIT(7))
#define BRX_LR_ABOVE_CNT_ENABLE2_S 7
#define BRX_LR_ABOVE_CNT2 0x00000007
#define BRX_LR_ABOVE_CNT2_S 4
#define BRX_LR_ABOVE_US_ENABLE2 (BIT(7))
#define BRX_LR_ABOVE_US_ENABLE2_S 7
#define BRX_LR_ABOVE_US2 0x00000007
#define BRX_LR_ABOVE_US2_S 4
#define BRX_LR_MAX_CNT_THR2 0x00000007
#define BRX_LR_MAX_CNT_THR2_S 0

#define BRX_LR_SYNC2_REG (REG_BRX_BASE + 0x007C)
#define BRX_LR_STATE_END_US2 0x0000003F
#define BRX_LR_STATE_END_US2_S 24
#define BRX_LR_STATE_START_US2 0x0000003F
#define BRX_LR_STATE_START_US2_S 16
#define BRX_LR_STATE_THR2 0x0000000F
#define BRX_LR_STATE_THR2_S 12
#define BRX_LR_PEAK_ENABLE2 (BIT(11))
#define BRX_LR_PEAK_ENABLE2_S 11
#define BRX_LR_BCORR_ABOVE_CNT_THR2 0x0000003F
#define BRX_LR_BCORR_ABOVE_CNT_THR2_S 4
#define BRX_LR_BCORR_ABOVE_THR2 0x0000000F
#define BRX_LR_BCORR_ABOVE_THR2_S 0

#define BRX_LR_WD0_REG (REG_BRX_BASE + 0x0080)
#define BRX_LR_SFD_WD0 0xFFFFFFFF
#define BRX_LR_SFD_WD0_S 0

#define BRX_LR_WD1_REG (REG_BRX_BASE + 0x0084)
#define BRX_LR_SFD_WD1 0xFFFFFFFF
#define BRX_LR_SFD_WD1_S 0

#define BRX_LR_WD2_REG (REG_BRX_BASE + 0x0088)
#define BRX_LR_SFD_WD2 0xFFFFFFFF
#define BRX_LR_SFD_WD2_S 0

#define BRX_LR_WD3_REG (REG_BRX_BASE + 0x008C)
#define BRX_LR_SFD_WD3 0xFFFFFFFF
#define BRX_LR_SFD_WD3_S 0

#define BRXSDF_INV_CONF_REG (REG_BRX_BASE + 0x0090)
#define BRX_INV_SHORT_SFD_BITWIDTH 0x0000001F
#define BRX_INV_SHORT_SFD_BITWIDTH_S 20
#define BRX_INV_LONG_SFD_BITWIDTH 0x0000001F
#define BRX_INV_LONG_SFD_BITWIDTH_S 12
#define BRX_INV_SHORT_SFD_ENABLE (BIT(1))
#define BRX_INV_SHORT_SFD_ENABLE_S 1
#define BRX_INV_LONG_SFD_ENABLE (BIT(0))
#define BRX_INV_LONG_SFD_ENABLE_S 0

#define BRXSNR_REG (REG_BRX_BASE + 0x0094)
#define BRX_BCORR_SNR 0x000000FF
#define BRX_BCORR_SNR_S 0

#define BRXEQU_TIM0_LR_REG (REG_BRX_BASE + 0x0098)
#define BRX_EQU_EST_CNT_LR 0x00000FFF
#define BRX_EQU_EST_CNT_LR_S 16
#define BRX_EQU_BYPASS_WAIT_LR (BIT(15))
#define BRX_EQU_BYPASS_WAIT_LR_S 15
#define BRX_EQU_BYPASS_CNT_LR 0x00000FFF
#define BRX_EQU_BYPASS_CNT_LR_S 0

#define BRXDATE_REG (REG_BRX_BASE + 0x0384)
#define BRX_DATE 0x0FFFFFFF
#define BRX_DATE_S 0
#define BRX_DATE_VERSION 0x1604281
