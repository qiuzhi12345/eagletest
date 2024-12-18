
#define NRXSCALE_REG (REG_NRX_BASE + 0x0000)
#define NRX_FFT_SCALE_FORCE 0x000000FF
#define NRX_FFT_SCALE_FORCE_S 20
#define NRX_FFT_SCALE_FORCE_EN (BIT(19))
#define NRX_FFT_SCALE_FORCE_EN_S 19
#define NRX_FFT_SCALE_EN (BIT(18))
#define NRX_FFT_SCALE_EN_S 18
#define NRX_FFT_SCALE_TAR 0x000003FF
#define NRX_FFT_SCALE_TAR_S 8
#define NRX_PWR_EST_SHIFT_CHANGE_EN (BIT(7))
#define NRX_PWR_EST_SHIFT_CHANGE_EN_S 7
#define NRX_RX_MOD_MULT 0x00000007
#define NRX_RX_MOD_MULT_S 4
#define NRX_RX_MOD_SHR 0x00000003
#define NRX_RX_MOD_SHR_S 2

#define NRXFTE_REG (REG_NRX_BASE + 0x0004)
#define NRX_FTE_SPUR_MASK_EN (BIT(31))
#define NRX_FTE_SPUR_MASK_EN_S 31
#define NRX_FTE_DATA_RATE 0x00000007
#define NRX_FTE_DATA_RATE_S 28
#define NRX_FTE_ERR_EN (BIT(27))
#define NRX_FTE_ERR_EN_S 27
#define NRX_FTE_MAX 0x000000FF
#define NRX_FTE_MAX_S 19
#define NRX_FTE_MIN 0x0000007F
#define NRX_FTE_MIN_S 12
#define NRX_FTE_ERR_MODE (BIT(11))
#define NRX_FTE_ERR_MODE_S 11
#define NRX_FTE_MODE2 (BIT(10))
#define NRX_FTE_MODE2_S 10
#define NRX_FTE_EN (BIT(9))
#define NRX_FTE_EN_S 9
#define NRX_FTE_TAR_BACKOFF 0x0000007F
#define NRX_FTE_TAR_BACKOFF_S 2
#define NRX_FTE_HTLTF_EXT (BIT(0))
#define NRX_FTE_HTLTF_EXT_S 0

#define NRXTDM1_REG (REG_NRX_BASE + 0x0008)
#define NRX_XCORR_EN_END_T 0x000001FF
#define NRX_XCORR_EN_END_T_S 20
#define NRX_FOE_USE_CTE (BIT(19))
#define NRX_FOE_USE_CTE_S 19
#define NRX_TDM_WAIT_END 0x0000000F
#define NRX_TDM_WAIT_END_S 15
#define NRX_XCORR_EN (BIT(14))
#define NRX_XCORR_EN_S 14
#define NRX_XCORR_FIND_THR2 0x0000007F
#define NRX_XCORR_FIND_THR2_S 7
#define NRX_XCORR_FIND_THR1 0x0000007F
#define NRX_XCORR_FIND_THR1_S 0

#define NRXMODE_REG (REG_NRX_BASE + 0x000c)
#define NRX_CFO_START_3 0x000000FF
#define NRX_CFO_START_3_S 24
#define NRX_WEIGHT_PICK_UP_FORCE (BIT(22))
#define NRX_WEIGHT_PICK_UP_FORCE_S 22
#define NRX_WEIGHT_PICK_DOWN_FORCE (BIT(21))
#define NRX_WEIGHT_PICK_DOWN_FORCE_S 21
#define NRX_CHAN_INTERP_DEP_SM (BIT(20))
#define NRX_CHAN_INTERP_DEP_SM_S 20
#define NRX_CFO_START_2 0x000000FF
#define NRX_CFO_START_2_S 12
#define NRX_CFO_START_1 0x000000FF
#define NRX_CFO_START_1_S 4
#define NRX_HTLTF_SGI_RETIM_EN (BIT(3))
#define NRX_HTLTF_SGI_RETIM_EN_S 3
#define NRX_CHAN_SPUR_INTERP_EN (BIT(2))
#define NRX_CHAN_SPUR_INTERP_EN_S 2
#define NRX_HT20_DATA_40M (BIT(1))
#define NRX_HT20_DATA_40M_S 1
#define NRX_HT40_PRI_UP (BIT(0))
#define NRX_HT40_PRI_UP_S 0

#define NRXSPURV0_REG (REG_NRX_BASE + 0x0010)
#define NRX_SPUR_VALUE0 0xFFFFFFFF
#define NRX_SPUR_VALUE0_S 0

#define NRXSPURV1_REG (REG_NRX_BASE + 0x0014)
#define NRX_SPUR_VALUE1 0xFFFFFFFF
#define NRX_SPUR_VALUE1_S 0

#define NRXSPURV2_REG (REG_NRX_BASE + 0x0018)
#define NRX_SPUR_VALUE2 0xFFFFFFFF
#define NRX_SPUR_VALUE2_S 0

#define NRXSPURV3_REG (REG_NRX_BASE + 0x001c)
#define NRX_SPUR_VALUE3 0xFFFFFFFF
#define NRX_SPUR_VALUE3_S 0

#define NRXSPURV4_REG (REG_NRX_BASE + 0x0020)
#define NRX_SPUR_VALUE4 0xFFFFFFFF
#define NRX_SPUR_VALUE4_S 0

#define NRXSPURV5_REG (REG_NRX_BASE + 0x0024)
#define NRX_SPUR_VALUE5 0xFFFFFFFF
#define NRX_SPUR_VALUE5_S 0

#define NRXSPURV6_REG (REG_NRX_BASE + 0x0028)
#define NRX_SPUR_VALUE6 0xFFFFFFFF
#define NRX_SPUR_VALUE6_S 0

#define NRXSPURV7_REG (REG_NRX_BASE + 0x002c)
#define NRX_SPUR_VALUE7 0xFFFFFFFF
#define NRX_SPUR_VALUE7_S 0

#define NRXSPURFV1_REG (REG_NRX_BASE + 0x0030)
#define NRX_SPUR_FLOAT_VALUE1 0xFFFFFFFF
#define NRX_SPUR_FLOAT_VALUE1_S 0

#define NRXSPURFV2_REG (REG_NRX_BASE + 0x0034)
#define NRX_SPUR_FLOAT_VALUE2 0xFFFFFFFF
#define NRX_SPUR_FLOAT_VALUE2_S 0

#define NRXSPURC_REG (REG_NRX_BASE + 0x0038)
#define NRX_SPUR_VALUE_EN (BIT(4))
#define NRX_SPUR_VALUE_EN_S 4
#define NRX_SPUR_FLOAT_PST 0x00000007
#define NRX_SPUR_FLOAT_PST_S 1
#define NRX_SPUR_FLOAT_EN (BIT(0))
#define NRX_SPUR_FLOAT_EN_S 0

#define NRXFOE_REG (REG_NRX_BASE + 0x003c)
#define NRX_CFO_CAL_NUM_2 0x000001FF
#define NRX_CFO_CAL_NUM_2_S 23
#define NRX_CFO_CAL_NUM_1 0x000001FF
#define NRX_CFO_CAL_NUM_1_S 14
#define NRX_FOE_FORCE 0x00001FFF
#define NRX_FOE_FORCE_S 1
#define NRX_FOE_FORCE_EN (BIT(0))
#define NRX_FOE_FORCE_EN_S 0

#define NRXVIT_REG (REG_NRX_BASE + 0x0040)
#define NRX_CLK80_EN (BIT(1))
#define NRX_CLK80_EN_S 1
#define NRX_CLK_FORCE_VIT (BIT(0))
#define NRX_CLK_FORCE_VIT_S 0

#define NRXFREQPARA_REG (REG_NRX_BASE + 0x0048)
#define NRX_FS_VS_F_PARA_SHIFT 0x0000001F
#define NRX_FS_VS_F_PARA_SHIFT_S 24
#define NRX_FS_VS_F_PARA 0x00FFFFFF
#define NRX_FS_VS_F_PARA_S 0

#define NRXMODUSCALE_REG (REG_NRX_BASE + 0x004c)
#define NRX_64QAM_SCALE 0x000000FF
#define NRX_64QAM_SCALE_S 24
#define NRX_16QAM_SCALE 0x000000FF
#define NRX_16QAM_SCALE_S 16
#define NRX_QPSK_SCALE 0x000000FF
#define NRX_QPSK_SCALE_S 8
#define NRX_BPSK_SCALE 0x000000FF
#define NRX_BPSK_SCALE_S 0

#define NRXTEST0_REG (REG_NRX_BASE + 0x0050)
#define NRX_COM_PHA_FORCE 0x001FFFFF
#define NRX_COM_PHA_FORCE_S 1
#define NRX_COM_PHA_FORCE_EN (BIT(0))
#define NRX_COM_PHA_FORCE_EN_S 0

#define NRXTEST1_REG (REG_NRX_BASE + 0x0054)
#define NRX_SLOPE_FORCE 0x001FFFFF
#define NRX_SLOPE_FORCE_S 1
#define NRX_SLOPE_FORCE_EN (BIT(0))
#define NRX_SLOPE_FORCE_EN_S 0

#define NRXFDM1_REG (REG_NRX_BASE + 0x0058)
#define NRX_VHT_NOTSUPPORTED_EN (BIT(18))
#define NRX_VHT_NOTSUPPORTED_EN_S 18
#define NRX_DUP_DEL_PWR_EN (BIT(17))
#define NRX_DUP_DEL_PWR_EN_S 17
#define NRX_DUP_DEL_PWR_THR 0x0000001F
#define NRX_DUP_DEL_PWR_THR_S 12
#define NRX_FFT_DONE_END_EN (BIT(11))
#define NRX_FFT_DONE_END_EN_S 11
#define NRX_FFT_LTF_START_POS_PULSE (BIT(10))
#define NRX_FFT_LTF_START_POS_PULSE_S 10
#define NRX_FDM_WAIT_END 0x000003FF
#define NRX_FDM_WAIT_END_S 0

#define NRXDEBUG_REG (REG_NRX_BASE + 0x005c)
#define NRX_FDM_WAIT_FOR_END (BIT(31))
#define NRX_FDM_WAIT_FOR_END_S 31
#define NRX_RF_FREQ_OFFSET_PHI_VALID (BIT(30))
#define NRX_RF_FREQ_OFFSET_PHI_VALID_S 30
#define NRX_RF_FREQ_OFFSET_PHI 0x00007FFF
#define NRX_RF_FREQ_OFFSET_PHI_S 15
#define NRX_FTE_OFFSET 0x0000007F
#define NRX_FTE_OFFSET_S 8
#define NRX_FTE_OFFSET_VALID (BIT(7))
#define NRX_FTE_OFFSET_VALID_S 7
#define NRX_EQUAL_START (BIT(6))
#define NRX_EQUAL_START_S 6
#define NRX_TEST_P1 (BIT(5))
#define NRX_TEST_P1_S 5

#define NRXPILOTERR0_REG (REG_NRX_BASE + 0x0060)
#define NRX_PILOT_PH_ERR0 0x001FFFFF
#define NRX_PILOT_PH_ERR0_S 0

#define NRXPILOTERR1_REG (REG_NRX_BASE + 0x0064)
#define NRX_PILOT_PH_ERR1 0x001FFFFF
#define NRX_PILOT_PH_ERR1_S 0

#define NRXPILOTERR2_REG (REG_NRX_BASE + 0x0068)
#define NRX_PILOT_PH_ERR2 0x001FFFFF
#define NRX_PILOT_PH_ERR2_S 0

#define NRXPILOTERR3_REG (REG_NRX_BASE + 0x006c)
#define NRX_PILOT_PH_ERR3 0x001FFFFF
#define NRX_PILOT_PH_ERR3_S 0

#define NRXPILOTERR4_REG (REG_NRX_BASE + 0x0070)
#define NRX_PILOT_PH_ERR4 0x001FFFFF
#define NRX_PILOT_PH_ERR4_S 0

#define NRXPILOTERR5_REG (REG_NRX_BASE + 0x0074)
#define NRX_PILOT_PH_ERR5 0x001FFFFF
#define NRX_PILOT_PH_ERR5_S 0

#define NRXCTE_CTRL0_REG (REG_NRX_BASE + 0x0078)
#define NRX_XCORR_GI_WIN_H 0x0000001F
#define NRX_XCORR_GI_WIN_H_S 27
#define NRX_XCORR_GI_WIN_L 0x0000001F
#define NRX_XCORR_GI_WIN_L_S 22
#define NRX_XCORR_WIN_H 0x0000001F
#define NRX_XCORR_WIN_H_S 17
#define NRX_XCORR_WIN_L 0x0000001F
#define NRX_XCORR_WIN_L_S 12
#define NRX_XCORR_CTE_TO 0x0000003F
#define NRX_XCORR_CTE_TO_S 6
#define NRX_CTE_PK_OFFSET 0x0000003F
#define NRX_CTE_PK_OFFSET_S 0

#define NRXCTE_CTRL1_REG (REG_NRX_BASE + 0x007c)
#define NRX_CFO_USE_CTE_PRE08 (BIT(31))
#define NRX_CFO_USE_CTE_PRE08_S 31
#define NRX_SC_DET_THR 0x0000000F
#define NRX_SC_DET_THR_S 27
#define NRX_SC_RISE_TO 0x000001FF
#define NRX_SC_RISE_TO_S 18
#define NRX_SC_FALL_TO 0x000001FF
#define NRX_SC_FALL_TO_S 9
#define NRX_SC_DET_TIMER 0x000001FF
#define NRX_SC_DET_TIMER_S 0

#define NRXCTE_CTRL2_REG (REG_NRX_BASE + 0x0080)
#define NRX_CTE_MODE 0x00000003
#define NRX_CTE_MODE_S 30
#define NRX_CTE_GI2_WAIT_1 0x0000003F
#define NRX_CTE_GI2_WAIT_1_S 24
#define NRX_XCORR_PK_SHR_1 0x0000000F
#define NRX_XCORR_PK_SHR_1_S 20
#define NRX_XCORR_PK_MULT_1 0x0000003F
#define NRX_XCORR_PK_MULT_1_S 14
#define NRX_SC_END_THR_1 0x0000007F
#define NRX_SC_END_THR_1_S 7
#define NRX_SC_COEF_1 0x0000007F
#define NRX_SC_COEF_1_S 0

#define NRXCTE_CTRL3_REG (REG_NRX_BASE + 0x0084)
#define NRX_CTE_GI2_WAIT_2 0x0000003F
#define NRX_CTE_GI2_WAIT_2_S 24
#define NRX_XCORR_PK_SHR_2 0x0000000F
#define NRX_XCORR_PK_SHR_2_S 20
#define NRX_XCORR_PK_MULT_2 0x0000003F
#define NRX_XCORR_PK_MULT_2_S 14
#define NRX_SC_END_THR_2 0x0000007F
#define NRX_SC_END_THR_2_S 7
#define NRX_SC_COEF_2 0x0000007F
#define NRX_SC_COEF_2_S 0

#define NRXFREQREG_REG (REG_NRX_BASE + 0x0088)
#define NRX_TIMING_JUMP_EN (BIT(21))
#define NRX_TIMING_JUMP_EN_S 21
#define NRX_JUMP_NUM 0x0000003F
#define NRX_JUMP_NUM_S 15
#define NRX_DELTA_PHASE_REG 0x00007FFF
#define NRX_DELTA_PHASE_REG_S 0

#define NRX_BB_NRX_TEST_REG (REG_NRX_BASE + 0x008c)
#define NRXCLK_EN (BIT(0))
#define NRXCLK_EN_S 0

#define NRXPILOTCONF0_REG (REG_NRX_BASE + 0x0090)
#define NRX_SYM_MAX_NUM 0x000000FF
#define NRX_SYM_MAX_NUM_S 24
#define NRX_K_SHIFT6 0x00000007
#define NRX_K_SHIFT6_S 20
#define NRX_K_SHIFT5 0x00000007
#define NRX_K_SHIFT5_S 16
#define NRX_K_SHIFT4 0x00000007
#define NRX_K_SHIFT4_S 12
#define NRX_K_SHIFT3 0x00000007
#define NRX_K_SHIFT3_S 8
#define NRX_K_SHIFT2 0x00000007
#define NRX_K_SHIFT2_S 4
#define NRX_K_SHIFT1 0x00000007
#define NRX_K_SHIFT1_S 0

#define NRXPILOTCONF1_REG (REG_NRX_BASE + 0x0094)
#define NRX_A_SHIFT6 0x00000007
#define NRX_A_SHIFT6_S 20
#define NRX_A_SHIFT5 0x00000007
#define NRX_A_SHIFT5_S 16
#define NRX_A_SHIFT4 0x00000007
#define NRX_A_SHIFT4_S 12
#define NRX_A_SHIFT3 0x00000007
#define NRX_A_SHIFT3_S 8
#define NRX_A_SHIFT2 0x00000007
#define NRX_A_SHIFT2_S 4
#define NRX_A_SHIFT1 0x00000007
#define NRX_A_SHIFT1_S 0

#define NRXPILOTCONF2_REG (REG_NRX_BASE + 0x0098)
#define NRX_PHI_FINE_FIX_EN (BIT(27))
#define NRX_PHI_FINE_FIX_EN_S 27
#define NRX_PHI_FINE_FIX 0x00007FFF
#define NRX_PHI_FINE_FIX_S 12
#define NRX_SLOPE_FIX 0x000003FF
#define NRX_SLOPE_FIX_S 0

#define NRXPILOTCONF3_REG (REG_NRX_BASE + 0x009c)
#define NRX_F_SHIFT6 0x00000007
#define NRX_F_SHIFT6_S 20
#define NRX_F_SHIFT5 0x00000007
#define NRX_F_SHIFT5_S 16
#define NRX_F_SHIFT4 0x00000007
#define NRX_F_SHIFT4_S 12
#define NRX_F_SHIFT3 0x00000007
#define NRX_F_SHIFT3_S 8
#define NRX_F_SHIFT2 0x00000007
#define NRX_F_SHIFT2_S 4
#define NRX_F_SHIFT1 0x00000007
#define NRX_F_SHIFT1_S 0

#define NRXCHAN_RATE_THR1_REG (REG_NRX_BASE + 0x00a0)
#define NRX_CHAN_RATE_THR_MCS4 0x000000FF
#define NRX_CHAN_RATE_THR_MCS4_S 24
#define NRX_CHAN_RATE_THR_MCS5 0x000000FF
#define NRX_CHAN_RATE_THR_MCS5_S 16
#define NRX_CHAN_RATE_THR_MCS6 0x000000FF
#define NRX_CHAN_RATE_THR_MCS6_S 8
#define NRX_CHAN_RATE_THR_MCS7 0x000000FF
#define NRX_CHAN_RATE_THR_MCS7_S 0

#define NRXCHAN_RATE_THR2_REG (REG_NRX_BASE + 0x00a4)
#define NRX_FTE_DATA_RATE_EN (BIT(24))
#define NRX_FTE_DATA_RATE_EN_S 24
#define NRX_CHAN_RATE_THR_MCS1 0x000000FF
#define NRX_CHAN_RATE_THR_MCS1_S 16
#define NRX_CHAN_RATE_THR_MCS2 0x000000FF
#define NRX_CHAN_RATE_THR_MCS2_S 8
#define NRX_CHAN_RATE_THR_MCS3 0x000000FF
#define NRX_CHAN_RATE_THR_MCS3_S 0

#define NRXLSIGEVM0_REG (REG_NRX_BASE + 0x00a8)
#define NRX_SUM_IMAG_EVM 0x0000FFFF
#define NRX_SUM_IMAG_EVM_S 16
#define NRX_SUM_REAL_EVM 0x0000FFFF
#define NRX_SUM_REAL_EVM_S 0

#define NRXLSIGEVM1_REG (REG_NRX_BASE + 0x00ac)
#define NRX_EVM_EST_SHIFT_EN (BIT(16))
#define NRX_EVM_EST_SHIFT_EN_S 16
#define NRX_EVM_EST_SHIFT 0x0000000F
#define NRX_EVM_EST_SHIFT_S 12
#define NRX_IMAG_EVM_EST 0x0000003F
#define NRX_IMAG_EVM_EST_S 6
#define NRX_REAL_EVM_EST 0x0000003F
#define NRX_REAL_EVM_EST_S 0

#define NRXSPURV8_REG (REG_NRX_BASE + 0x00b0)
#define NRX_SPUR_VALUE8 0xFFFFFFFF
#define NRX_SPUR_VALUE8_S 0

#define NRXPILOTCONF4_REG (REG_NRX_BASE + 0x00b4)
#define NRX_SIG_CHAN_EST_EN (BIT(15))
#define NRX_SIG_CHAN_EST_EN_S 15
#define NRX_HTLTF_COMP_DEP_SM (BIT(14))
#define NRX_HTLTF_COMP_DEP_SM_S 14
#define NRX_HTLTF_COMP_EN (BIT(13))
#define NRX_HTLTF_COMP_EN_S 13
#define NRX_HTLTF_COMP_SEL (BIT(12))
#define NRX_HTLTF_COMP_SEL_S 12
#define NRX_PH_ERR_RSHIFT 0x0000000F
#define NRX_PH_ERR_RSHIFT_S 8
#define NRX_DELTA_PHASE_SHIFT 0x0000000F
#define NRX_DELTA_PHASE_SHIFT_S 4
#define NRX_COMMON_PHASE_F_SHIFT_SHIFT 0x0000000F
#define NRX_COMMON_PHASE_F_SHIFT_SHIFT_S 0

#define NRXPILOTCONF5_REG (REG_NRX_BASE + 0x00b8)
#define NRX_MAC_DUG_INF_MOD 0x00000007
#define NRX_MAC_DUG_INF_MOD_S 29
#define NRX_COMMON_PH_ERR_ABS_REG 0x001FFFFF
#define NRX_COMMON_PH_ERR_ABS_REG_S 8
#define NRX_COMMON_PH_ERR_ABS_KB 0x000000FF
#define NRX_COMMON_PH_ERR_ABS_KB_S 0

#define NRXPILOTCONF6_REG (REG_NRX_BASE + 0x00bc)
#define NRX_COMMON_PHASE_F_SHIFT_REG 0x07FFFFFF
#define NRX_COMMON_PHASE_F_SHIFT_REG_S 0

#define NRXPILOTCONF7_REG (REG_NRX_BASE + 0x00c0)
#define NRX_DATA_PILOT_TK_EN (BIT(21))
#define NRX_DATA_PILOT_TK_EN_S 21
#define NRX_PILOT_PWR_TRACK_EN (BIT(20))
#define NRX_PILOT_PWR_TRACK_EN_S 20
#define NRX_PILOT_PWR_INIT_AVG_NUM 0x0000000F
#define NRX_PILOT_PWR_INIT_AVG_NUM_S 16
#define NRX_FOE_PILOT_TK_CMP_EN (BIT(15))
#define NRX_FOE_PILOT_TK_CMP_EN_S 15
#define NRX_FREQ_OFFSET_TOT_REG 0x00007FFF
#define NRX_FREQ_OFFSET_TOT_REG_S 0

#define NRXPILOTCONF8_REG (REG_NRX_BASE + 0x00c4)
#define NRX_FREQ_OFFSET_TOT_KB 0x0000003F
#define NRX_FREQ_OFFSET_TOT_KB_S 14
#define NRX_DELTA_PHASE_KB 0x0000003F
#define NRX_DELTA_PHASE_KB_S 8
#define NRX_COMMON_PHASE_KB 0x000000FF
#define NRX_COMMON_PHASE_KB_S 0

#define NRXTDM2_REG (REG_NRX_BASE + 0x00c8)
#define NRX_TDM_1ST_CHK_WAIT 0x000001FF
#define NRX_TDM_1ST_CHK_WAIT_S 23
#define NRX_XCORR_AGC_GT_EXT_2 (BIT(22))
#define NRX_XCORR_AGC_GT_EXT_2_S 22
#define NRX_XCORR_AGC_GT_EXT (BIT(21))
#define NRX_XCORR_AGC_GT_EXT_S 21
#define NRX_XCORR_DET_AGC_MODE_2 (BIT(20))
#define NRX_XCORR_DET_AGC_MODE_2_S 20
#define NRX_XCORR_DET_AGC_MODE (BIT(19))
#define NRX_XCORR_DET_AGC_MODE_S 19
#define NRX_XCORR_AGC_PRE64_EN_2 (BIT(18))
#define NRX_XCORR_AGC_PRE64_EN_2_S 18
#define NRX_XCORR_AGC_PRE64_EN (BIT(17))
#define NRX_XCORR_AGC_PRE64_EN_S 17
#define NRX_XCORR_AGC_2TH_EXT (BIT(16))
#define NRX_XCORR_AGC_2TH_EXT_S 16
#define NRX_XCORR_AGC_2TH_EN_2 (BIT(15))
#define NRX_XCORR_AGC_2TH_EN_2_S 15
#define NRX_XCORR_AGC_2TH_EN (BIT(14))
#define NRX_XCORR_AGC_2TH_EN_S 14
#define NRX_XCORR_AGC_THR2 0x0000007F
#define NRX_XCORR_AGC_THR2_S 7
#define NRX_XCORR_AGC_THR1 0x0000007F
#define NRX_XCORR_AGC_THR1_S 0

#define NRXCTE_CTRL4_REG (REG_NRX_BASE + 0x00cc)
#define NRX_SC_END_THR_3 0x0000007F
#define NRX_SC_END_THR_3_S 25
#define NRX_SC_COEF_3 0x0000007F
#define NRX_SC_COEF_3_S 18
#define NRX_SCORR_FALL_SUM_THR_3 0x00000007
#define NRX_SCORR_FALL_SUM_THR_3_S 15
#define NRX_SCORR_FALL_CHK_NUM_3 0x00000007
#define NRX_SCORR_FALL_CHK_NUM_3_S 12
#define NRX_SCORR_FALL_SUM_THR_2 0x00000007
#define NRX_SCORR_FALL_SUM_THR_2_S 9
#define NRX_SCORR_FALL_CHK_NUM_2 0x00000007
#define NRX_SCORR_FALL_CHK_NUM_2_S 6
#define NRX_SCORR_FALL_SUM_THR_1 0x00000007
#define NRX_SCORR_FALL_SUM_THR_1_S 3
#define NRX_SCORR_FALL_CHK_NUM_1 0x00000007
#define NRX_SCORR_FALL_CHK_NUM_1_S 0

#define NRXCTE_CTRL5_REG (REG_NRX_BASE + 0x00d0)
#define NRX_R_CTE_TYP_MRC 0x00000007
#define NRX_R_CTE_TYP_MRC_S 28
#define NRX_CTE_MRC_EN (BIT(27))
#define NRX_CTE_MRC_EN_S 27
#define NRX_CTE_XCORR_LOSS_PROT (BIT(26))
#define NRX_CTE_XCORR_LOSS_PROT_S 26
#define NRX_SC_END_THR_XCORR 0x0000007F
#define NRX_SC_END_THR_XCORR_S 19
#define NRX_XCORR_GI_PK_SHR 0x0000000F
#define NRX_XCORR_GI_PK_SHR_S 15
#define NRX_XCORR_GI_PK_MULT 0x0000003F
#define NRX_XCORR_GI_PK_MULT_S 9
#define NRX_CTE_XCORR_GI_EN_WEAK (BIT(8))
#define NRX_CTE_XCORR_GI_EN_WEAK_S 8
#define NRX_CTE_XCORR_GI_EN_FORCE (BIT(7))
#define NRX_CTE_XCORR_GI_EN_FORCE_S 7
#define NRX_SC_END_THR_GI 0x0000007F
#define NRX_SC_END_THR_GI_S 0

#define NRXPD_CTRL_REG (REG_NRX_BASE + 0x00d4)
#define NRX_CHAN_EST_FORCE_PU (BIT(7))
#define NRX_CHAN_EST_FORCE_PU_S 7
#define NRX_CHAN_EST_FORCE_PD (BIT(6))
#define NRX_CHAN_EST_FORCE_PD_S 6
#define NRX_RX_ROT_FORCE_PU (BIT(5))
#define NRX_RX_ROT_FORCE_PU_S 5
#define NRX_RX_ROT_FORCE_PD (BIT(4))
#define NRX_RX_ROT_FORCE_PD_S 4
#define NRX_VIT_FORCE_PU (BIT(3))
#define NRX_VIT_FORCE_PU_S 3
#define NRX_VIT_FORCE_PD (BIT(2))
#define NRX_VIT_FORCE_PD_S 2
#define NRX_DEMAP_FORCE_PU (BIT(1))
#define NRX_DEMAP_FORCE_PU_S 1
#define NRX_DEMAP_FORCE_PD (BIT(0))
#define NRX_DEMAP_FORCE_PD_S 0

#define NRXFTE1_REG (REG_NRX_BASE + 0x00d8)
#define NRX_FTE_TAR_BACKOFF_STBC_COMP 0x0000007F
#define NRX_FTE_TAR_BACKOFF_STBC_COMP_S 7
#define NRX_FTE_TAR_BACKOFF_SGI_COMP 0x0000007F
#define NRX_FTE_TAR_BACKOFF_SGI_COMP_S 0

#define NRXTDM3_REG (REG_NRX_BASE + 0x00dc)
#define NRX_XCORR_PK_SHR_3 0x0000000F
#define NRX_XCORR_PK_SHR_3_S 22
#define NRX_XCORR_PK_MULT_3 0x0000003F
#define NRX_XCORR_PK_MULT_3_S 16
#define NRX_XCORR_AGC_PRE64_EN_3 (BIT(15))
#define NRX_XCORR_AGC_PRE64_EN_3_S 15
#define NRX_XCORR_AGC_2TH_EN_3 (BIT(14))
#define NRX_XCORR_AGC_2TH_EN_3_S 14
#define NRX_XCORR_FIND_THR3 0x0000007F
#define NRX_XCORR_FIND_THR3_S 7
#define NRX_XCORR_AGC_THR3 0x0000007F
#define NRX_XCORR_AGC_THR3_S 0

#define NRXCTE_CTRL6_REG (REG_NRX_BASE + 0x00e0)
#define NRX_SC_END_THR_FOE_EN (BIT(25))
#define NRX_SC_END_THR_FOE_EN_S 25
#define NRX_SC_END_THR_FOE 0x0000007F
#define NRX_SC_END_THR_FOE_S 18
#define NRX_SCORR_FOE_FALL_SUM_THR_3 0x00000007
#define NRX_SCORR_FOE_FALL_SUM_THR_3_S 15
#define NRX_SCORR_FOE_FALL_CHK_NUM_3 0x00000007
#define NRX_SCORR_FOE_FALL_CHK_NUM_3_S 12
#define NRX_SCORR_FOE_FALL_SUM_THR_2 0x00000007
#define NRX_SCORR_FOE_FALL_SUM_THR_2_S 9
#define NRX_SCORR_FOE_FALL_CHK_NUM_2 0x00000007
#define NRX_SCORR_FOE_FALL_CHK_NUM_2_S 6
#define NRX_SCORR_FOE_FALL_SUM_THR_1 0x00000007
#define NRX_SCORR_FOE_FALL_SUM_THR_1_S 3
#define NRX_SCORR_FOE_FALL_CHK_NUM_1 0x00000007
#define NRX_SCORR_FOE_FALL_CHK_NUM_1_S 0

#define NRXCTE_CTRL7_REG (REG_NRX_BASE + 0x00e4)
#define NRX_LTF_FOE_END_CNT 0x0000007F
#define NRX_LTF_FOE_END_CNT_S 24
#define NRX_DEMOD_SIG_MRC_DIS (BIT(23))
#define NRX_DEMOD_SIG_MRC_DIS_S 23
#define NRX_DEMOD_MRC_EN (BIT(22))
#define NRX_DEMOD_MRC_EN_S 22
#define NRX_SCORR_CMP_SHR 0x00000003
#define NRX_SCORR_CMP_SHR_S 20
#define NRX_CTE_SEC_GT_THR 0x0000000F
#define NRX_CTE_SEC_GT_THR_S 16
#define NRX_CTE_MRC_XCORR_EN (BIT(15))
#define NRX_CTE_MRC_XCORR_EN_S 15
#define NRX_CTE_MRC_XCORR_MASK 0x00007FFF
#define NRX_CTE_MRC_XCORR_MASK_S 0

#define NRXPILOTCONF9_REG (REG_NRX_BASE + 0x00e8)
#define NRX_FOE_DELTA_PHI_THR_DOWN 0x00007FFF
#define NRX_FOE_DELTA_PHI_THR_DOWN_S 0
#define NRX_FOE_DELTA_PHI_THR_UP 0x00007FFF
#define NRX_FOE_DELTA_PHI_THR_UP_S 0

#define NRXCLKGATE_REG (REG_NRX_BASE + 0x00ec)
#define NRX_DEMOD_FORCE_CLK (BIT(4))
#define NRX_DEMOD_FORCE_CLK_S 4
#define NRX_TDM_CORR_FORCE_CLK (BIT(3))
#define NRX_TDM_CORR_FORCE_CLK_S 3
#define NRX_RX_ROT_FORCE_CLK (BIT(2))
#define NRX_RX_ROT_FORCE_CLK_S 2
#define NRX_CHAN_EST_FORCE_CLK (BIT(1))
#define NRX_CHAN_EST_FORCE_CLK_S 1
#define NRX_EQU_FORCE_CLK (BIT(0))
#define NRX_EQU_FORCE_CLK_S 0

#define NRXPILOTCONF10_REG (REG_NRX_BASE + 0x00f0)
#define NRX_CHAN_ROT_FORCE_EN (BIT(21))
#define NRX_CHAN_ROT_FORCE_EN_S 21
#define NRX_CHAN_ROT_SLOPE_FORCE 0x001FFFFF
#define NRX_CHAN_ROT_SLOPE_FORCE_S 0

#define NRXPILOTCONF11_REG (REG_NRX_BASE + 0x00f4)
#define NRX_CHAN_ROT_COM_PHA_FORCE 0x001FFFFF
#define NRX_CHAN_ROT_COM_PHA_FORCE_S 0

#define NRXCHANESTFILTCONF0_REG (REG_NRX_BASE + 0x00f8)
#define NRX_NUM_GT_CHACORRTHRES 0x0000003F
#define NRX_NUM_GT_CHACORRTHRES_S 24
#define NRX_COA_DB_THRES1 0x000000FF
#define NRX_COA_DB_THRES1_S 16
#define NRX_COA_DB_THRES0 0x000000FF
#define NRX_COA_DB_THRES0_S 8
#define NRX_CHACORRTHRES 0x000000FF
#define NRX_CHACORRTHRES_S 0

#define NRXCHANESTFILTCONF1_REG (REG_NRX_BASE + 0x00fc)
#define NRX_FORCE_CHAN_FILT_SEL_EN (BIT(31))
#define NRX_FORCE_CHAN_FILT_SEL_EN_S 31
#define NRX_FORCE_CHAN_FILT_SEL 0x00000007
#define NRX_FORCE_CHAN_FILT_SEL_S 28
#define NRX_NUM_CHCCORR_PK 0x0000000F
#define NRX_NUM_CHCCORR_PK_S 24
#define NRX_CHCCORRTHRESVEC2 0x000000FF
#define NRX_CHCCORRTHRESVEC2_S 16
#define NRX_CHCCORRTHRESVEC1 0x000000FF
#define NRX_CHCCORRTHRESVEC1_S 8
#define NRX_CHCCORRTHRESVEC0 0x000000FF
#define NRX_CHCCORRTHRESVEC0_S 0

#define NRXFSM_DEBUG0_REG (REG_NRX_BASE + 0x0100)
#define NRX_HT_RATE_PRE_EN (BIT(11))
#define NRX_HT_RATE_PRE_EN_S 11
#define NRX_FSM_LSYM_MAX 0x000007FF
#define NRX_FSM_LSYM_MAX_S 0

#define NRXCHANESTWEIGHTSELDOWN_REG (REG_NRX_BASE + 0x0104)
#define NRX_WEIGHT_SEL_DOWN_SMOOTHING_STBC_WIDE 0x00000007
#define NRX_WEIGHT_SEL_DOWN_SMOOTHING_STBC_WIDE_S 28
#define NRX_WEIGHT_SEL_DOWN_SMOOTHING_STBC_NARROW 0x00000007
#define NRX_WEIGHT_SEL_DOWN_SMOOTHING_STBC_NARROW_S 24
#define NRX_WEIGHT_SEL_DOWN_SMOOTHING_NONSTBC_WIDE 0x00000007
#define NRX_WEIGHT_SEL_DOWN_SMOOTHING_NONSTBC_WIDE_S 20
#define NRX_WEIGHT_SEL_DOWN_SMOOTHING_NONSTBC_NARROW 0x00000007
#define NRX_WEIGHT_SEL_DOWN_SMOOTHING_NONSTBC_NARROW_S 16
#define NRX_WEIGHT_SEL_DOWN_NONSMOOTHING_STBC 0x00000007
#define NRX_WEIGHT_SEL_DOWN_NONSMOOTHING_STBC_S 12
#define NRX_WEIGHT_SEL_DOWN_NONSMOOTHING_NONSTBC 0x00000007
#define NRX_WEIGHT_SEL_DOWN_NONSMOOTHING_NONSTBC_S 8
#define NRX_WEIGHT_SEL_DOWN_XSMOOTHING 0x00000007
#define NRX_WEIGHT_SEL_DOWN_XSMOOTHING_S 4
#define NRX_WEIGHT_SEL_DOWN_FORCE 0x00000007
#define NRX_WEIGHT_SEL_DOWN_FORCE_S 0

#define NRXCHANESTWEIGHTSELUP_REG (REG_NRX_BASE + 0x0108)
#define NRX_WEIGHT_SEL_UP_SMOOTHING_STBC_WIDE 0x00000007
#define NRX_WEIGHT_SEL_UP_SMOOTHING_STBC_WIDE_S 28
#define NRX_WEIGHT_SEL_UP_SMOOTHING_STBC_NARROW 0x00000007
#define NRX_WEIGHT_SEL_UP_SMOOTHING_STBC_NARROW_S 24
#define NRX_WEIGHT_SEL_UP_SMOOTHING_NONSTBC_WIDE 0x00000007
#define NRX_WEIGHT_SEL_UP_SMOOTHING_NONSTBC_WIDE_S 20
#define NRX_WEIGHT_SEL_UP_SMOOTHING_NONSTBC_NARROW 0x00000007
#define NRX_WEIGHT_SEL_UP_SMOOTHING_NONSTBC_NARROW_S 16
#define NRX_WEIGHT_SEL_UP_NONSMOOTHING_STBC 0x00000007
#define NRX_WEIGHT_SEL_UP_NONSMOOTHING_STBC_S 12
#define NRX_WEIGHT_SEL_UP_NONSMOOTHING_NONSTBC 0x00000007
#define NRX_WEIGHT_SEL_UP_NONSMOOTHING_NONSTBC_S 8
#define NRX_WEIGHT_SEL_UP_XSMOOTHING 0x00000007
#define NRX_WEIGHT_SEL_UP_XSMOOTHING_S 4
#define NRX_WEIGHT_SEL_UP_FORCE 0x00000007
#define NRX_WEIGHT_SEL_UP_FORCE_S 0

#define NRXCHANDUMP_REG (REG_NRX_BASE + 0x010c)
#define NRX_CHAN_DUMP_BYPASS_TEST (BIT(11))
#define NRX_CHAN_DUMP_BYPASS_TEST_S 11
#define NRX_CHAN_FFT_OUT_DUMP_EN (BIT(10))
#define NRX_CHAN_FFT_OUT_DUMP_EN_S 10
#define NRX_FTE_OFFSET_NON_AVG_EN (BIT(9))
#define NRX_FTE_OFFSET_NON_AVG_EN_S 9
#define NRX_FFT_HTLTF_START_POS_PULSE_EN (BIT(8))
#define NRX_FFT_HTLTF_START_POS_PULSE_EN_S 8
#define NRX_CHAN_DUMP_SHIFT_FORCE 0x0000000F
#define NRX_CHAN_DUMP_SHIFT_FORCE_S 4
#define NRX_CHAN_DUMP_SHIFT_FORCE_EN (BIT(3))
#define NRX_CHAN_DUMP_SHIFT_FORCE_EN_S 3
#define NRX_CHAN_STBCLTF2_DUMP_EN (BIT(2))
#define NRX_CHAN_STBCLTF2_DUMP_EN_S 2
#define NRX_CHAN_LLTF_DUMP_EN (BIT(1))
#define NRX_CHAN_LLTF_DUMP_EN_S 1
#define NRX_CHAN_HTLTF_DUMP_EN (BIT(0))
#define NRX_CHAN_HTLTF_DUMP_EN_S 0

#define NRXSIMDUG0_REG (REG_NRX_BASE + 0x0110)
#define NRX_RXSTART_TIME_CYCLE 0x0000007F
#define NRX_RXSTART_TIME_CYCLE_S 0

#define NRXFFTSCALE_REG (REG_NRX_BASE + 0x0114)
#define NRX_MODU_SCALE_EN (BIT(9))
#define NRX_MODU_SCALE_EN_S 9
#define NRX_MODU_SNR_THR_EN (BIT(8))
#define NRX_MODU_SNR_THR_EN_S 8
#define NRX_FFT_SCALE 0x000000FF
#define NRX_FFT_SCALE_S 0

#define NRXSNRDEMAPTHR_REG (REG_NRX_BASE + 0x0118)
#define NRX_SNR_64QAM_THR 0x000000FF
#define NRX_SNR_64QAM_THR_S 24
#define NRX_SNR_16QAM_THR 0x000000FF
#define NRX_SNR_16QAM_THR_S 16
#define NRX_SNR_QPSK_THR 0x000000FF
#define NRX_SNR_QPSK_THR_S 8
#define NRX_SNR_BPSK_THR 0x000000FF
#define NRX_SNR_BPSK_THR_S 0

#define NRXSOFTBITWIGHT_REG (REG_NRX_BASE + 0x011c)
#define NRX_BIT_WIGHT_SHIFT_EN (BIT(6))
#define NRX_BIT_WIGHT_SHIFT_EN_S 6
#define NRX_BIT2_WIGHT_SHIFT 0x00000003
#define NRX_BIT2_WIGHT_SHIFT_S 4
#define NRX_BIT1_WIGHT_SHIFT 0x00000003
#define NRX_BIT1_WIGHT_SHIFT_S 2
#define NRX_BIT0_WIGHT_SHIFT 0x00000003
#define NRX_BIT0_WIGHT_SHIFT_S 0

#define NRXCHANSELTHR_REG (REG_NRX_BASE + 0x0120)
#define NRX_CHAN_FILTER_OFF_THR 0x000000FF
#define NRX_CHAN_FILTER_OFF_THR_S 8
#define NRX_CHAN_SEL_AWGN_THR 0x000000FF
#define NRX_CHAN_SEL_AWGN_THR_S 0

#define NRXTDM4_REG (REG_NRX_BASE + 0x0124)
#define NRX_CTE_DLY 0x0000000F
#define NRX_CTE_DLY_S 8
#define NRX_AGC_XCORR_START 0x000000FF
#define NRX_AGC_XCORR_START_S 0

#define NRXFOEHTRANGE_REG (REG_NRX_BASE + 0x0128)
#define NRX_FOE_HTSTF_ON (BIT(16))
#define NRX_FOE_HTSTF_ON_S 16
#define NRX_FOE_HTSTF_END 0x000000FF
#define NRX_FOE_HTSTF_END_S 8
#define NRX_FOE_HTSTF_START 0x000000FF
#define NRX_FOE_HTSTF_START_S 0

#define NRXSIMDUG1_REG (REG_NRX_BASE + 0x03F8)
#define NRX_RXSTART_TIME 0xFFFFFFFF
#define NRX_RXSTART_TIME_S 0

#define NRXDATE_REG (REG_NRX_BASE + 0x03FC)
#define NRX_DATE 0x0FFFFFFF
#define NRX_DATE_S 0
#define NRX_DATE_VERSION 0x1808271
