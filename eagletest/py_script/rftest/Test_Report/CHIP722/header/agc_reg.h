
#define AGCDC_CTRL1_REG (REG_AGC_BASE + 0x0000)
#define AGC_BB_DC_INT_INDEX 0x0000007F
#define AGC_BB_DC_INT_INDEX_S 16
#define AGC_DC_INT_CHK_EN (BIT(15))
#define AGC_DC_INT_CHK_EN_S 15
#define AGC_DC_INT_CHK_THR 0x000001FF
#define AGC_DC_INT_CHK_THR_S 6
#define AGC_DC_CTE_PROT_DOT8_EN (BIT(5))
#define AGC_DC_CTE_PROT_DOT8_EN_S 5
#define AGC_DC_MERGE_MULT 0x00000007
#define AGC_DC_MERGE_MULT_S 2
#define AGC_DC_MERGE_SHR 0x00000003
#define AGC_DC_MERGE_SHR_S 0

#define AGCDC_CTRL2_REG (REG_AGC_BASE + 0x0004)
#define AGC_COARSE_USE_MEMDC (BIT(31))
#define AGC_COARSE_USE_MEMDC_S 31
#define AGC_FINE_USE_MEMDC (BIT(30))
#define AGC_FINE_USE_MEMDC_S 30
#define AGC_STORE_DC_MERGE (BIT(29))
#define AGC_STORE_DC_MERGE_S 29
#define AGC_DCMEM_UPD_EN (BIT(28))
#define AGC_DCMEM_UPD_EN_S 28
#define AGC_HT2040_DCMEM_EN (BIT(27))
#define AGC_HT2040_DCMEM_EN_S 27
#define AGC_DC_MODE_HT40 0x00000003
#define AGC_DC_MODE_HT40_S 25
#define AGC_MODEM_DC_FINE_EN (BIT(24))
#define AGC_MODEM_DC_FINE_EN_S 24
#define AGC_MODEM_DC_FINE_EST_EN (BIT(23))
#define AGC_MODEM_DC_FINE_EST_EN_S 23
#define AGC_DC_FINE_MAX_LOOP 0x00000007
#define AGC_DC_FINE_MAX_LOOP_S 19
#define AGC_DC_COARSE_FORCE_MODE 0x00000003
#define AGC_DC_COARSE_FORCE_MODE_S 17
#define AGC_USE_DC_MEM_EN (BIT(16))
#define AGC_USE_DC_MEM_EN_S 16
#define AGC_DC_INIT_I 0x000000FF
#define AGC_DC_INIT_I_S 8
#define AGC_DC_INIT_Q 0x000000FF
#define AGC_DC_INIT_Q_S 0

#define AGCOFDM_CTRL1_REG (REG_AGC_BASE + 0x0008)
#define AGC_OCORR_THR2_2 0x000000FF
#define AGC_OCORR_THR2_2_S 24
#define AGC_OCORR_THR2 0x000000FF
#define AGC_OCORR_THR2_S 16
#define AGC_OCORR_THR1_2 0x000000FF
#define AGC_OCORR_THR1_2_S 8
#define AGC_OCORR_THR1 0x000000FF
#define AGC_OCORR_THR1_S 0

#define AGCOFDM_CTRL2_REG (REG_AGC_BASE + 0x000c)
#define AGC_PWR_VALID_CNT_INIT_2 0x0000000F
#define AGC_PWR_VALID_CNT_INIT_2_S 27
#define AGC_PWR_INBAND_THR 0x0000003F
#define AGC_PWR_INBAND_THR_S 21
#define AGC_CORR_DET_THR_2 0x0000003F
#define AGC_CORR_DET_THR_2_S 15
#define AGC_PWR_VALID_CNT_INIT 0x0000000F
#define AGC_PWR_VALID_CNT_INIT_S 11
#define AGC_CORR_DET_THR 0x0000001F
#define AGC_CORR_DET_THR_S 6
#define AGC_CORR_DET_CNT_MAX 0x0000003F
#define AGC_CORR_DET_CNT_MAX_S 0

#define AGCOFDM_CTRL3_REG (REG_AGC_BASE + 0x0010)
#define AGC_OCORR_GT_NOISE_THR_1 0x000001FF
#define AGC_OCORR_GT_NOISE_THR_1_S 23
#define AGC_PWR_FIR_GT_THR 0x000003FF
#define AGC_PWR_FIR_GT_THR_S 13
#define AGC_PWR_FIR_SURGE_THR 0x0000007F
#define AGC_PWR_FIR_SURGE_THR_S 6
#define AGC_PWR_INBAND_SURGE_THR 0x0000003F
#define AGC_PWR_INBAND_SURGE_THR_S 0

#define AGCOFDM_CTRL4_REG (REG_AGC_BASE + 0x0014)
#define AGC_OCORR_GT_NOISE_THR_2 0x000001FF
#define AGC_OCORR_GT_NOISE_THR_2_S 23
#define AGC_PWR_FIR_GT_THR_2 0x000003FF
#define AGC_PWR_FIR_GT_THR_2_S 13
#define AGC_PWR_FIR_SURGE_THR_2 0x0000007F
#define AGC_PWR_FIR_SURGE_THR_2_S 6
#define AGC_PWR_INBAND_SURGE_THR_2 0x0000003F
#define AGC_PWR_INBAND_SURGE_THR_2_S 0

#define AGCPWR_CTRL1_REG (REG_AGC_BASE + 0x0018)
#define AGC_NOISE_MIN_N_RST (BIT(31))
#define AGC_NOISE_MIN_N_RST_S 31
#define AGC_SIG_WEAK_MODE (BIT(30))
#define AGC_SIG_WEAK_MODE_S 30
#define AGC_RSSI_MODE (BIT(29))
#define AGC_RSSI_MODE_S 29
#define AGC_NOISE_AUTO_EN (BIT(28))
#define AGC_NOISE_AUTO_EN_S 28
#define AGC_RESET_NOISE (BIT(27))
#define AGC_RESET_NOISE_S 27
#define AGC_NOISE_WEAK_THR_EN (BIT(26))
#define AGC_NOISE_WEAK_THR_EN_S 26
#define AGC_NOISE_DONE_CLR (BIT(25))
#define AGC_NOISE_DONE_CLR_S 25
#define AGC_R_NOISE_DONE_RAW (BIT(24))
#define AGC_R_NOISE_DONE_RAW_S 24
#define AGC_NOISE_CAL (BIT(23))
#define AGC_NOISE_CAL_S 23
#define AGC_INIT_NOISEPWR 0x000000FF
#define AGC_INIT_NOISEPWR_S 15
#define AGC_NOISE_HW_FORCE 0x000003FF
#define AGC_NOISE_HW_FORCE_S 5
#define AGC_NOISE_HW_FORCE_EN (BIT(4))
#define AGC_NOISE_HW_FORCE_EN_S 4
#define AGC_NOISE_HW_UPD_EN (BIT(3))
#define AGC_NOISE_HW_UPD_EN_S 3
#define AGC_NOISE_CAL_TIME 0x00000007
#define AGC_NOISE_CAL_TIME_S 0

#define AGCPWR_CTRL2_REG (REG_AGC_BASE + 0x001c)
#define AGC_NOISE_WEAK_THR 0x000000FF
#define AGC_NOISE_WEAK_THR_S 24
#define AGC_RSSI_STRONG_THR 0x000000FF
#define AGC_RSSI_STRONG_THR_S 16
#define AGC_RSSI_MODECHECK_THR 0x000000FF
#define AGC_RSSI_MODECHECK_THR_S 8
#define AGC_SIG_WEAK_THR 0x000000FF
#define AGC_SIG_WEAK_THR_S 0

#define AGCPWR_CTRL3_REG (REG_AGC_BASE + 0x0020)
#define AGC_ADCSAT_RSTA_THR 0x0000003F
#define AGC_ADCSAT_RSTA_THR_S 26
#define AGC_ADC_SAT2_EN (BIT(25))
#define AGC_ADC_SAT2_EN_S 25
#define AGC_ADCSAT_SUM_THR2 0x0000001F
#define AGC_ADCSAT_SUM_THR2_S 20
#define AGC_ADCSAT_SUM_THR 0x0000003F
#define AGC_ADCSAT_SUM_THR_S 14
#define AGC_ADCSAT_COUNT_MAX 0x0000001F
#define AGC_ADCSAT_COUNT_MAX_S 9
#define AGC_ADCSAT_THR 0x000001FF
#define AGC_ADCSAT_THR_S 0

#define AGCPWR_CTRL5_REG (REG_AGC_BASE + 0x0024)
#define AGC_PWR_FIR2_CMP 0x0000001F
#define AGC_PWR_FIR2_CMP_S 27
#define AGC_COARSE_WEAK_THR 0x000000FF
#define AGC_COARSE_WEAK_THR_S 19
#define AGC_COARSE_WEAK_PROT (BIT(18))
#define AGC_COARSE_WEAK_PROT_S 18
#define AGC_PWR_LOW_THR 0x000001FF
#define AGC_PWR_LOW_THR_S 9
#define AGC_PWR_HIGH_THR 0x000001FF
#define AGC_PWR_HIGH_THR_S 0

#define AGCPWR_CTRL6_REG (REG_AGC_BASE + 0x0028)
#define AGC_PWR_DET_SEL (BIT(30))
#define AGC_PWR_DET_SEL_S 30
#define AGC_PWR_COARSE_SEL (BIT(29))
#define AGC_PWR_COARSE_SEL_S 29
#define AGC_PWR_FINE_SEL 0x00000003
#define AGC_PWR_FINE_SEL_S 27
#define AGC_PWR_FINE 0x000001FF
#define AGC_PWR_FINE_S 18
#define AGC_PWR_COARSE_LOW 0x000001FF
#define AGC_PWR_COARSE_LOW_S 9
#define AGC_PWR_COARSE_HIGH 0x000001FF
#define AGC_PWR_COARSE_HIGH_S 0

#define AGCPWR_CTRL7_REG (REG_AGC_BASE + 0x002c)
#define AGC_GAIN_FORCE 0x000000FF
#define AGC_GAIN_FORCE_S 24
#define AGC_GAIN_FORCE_EN (BIT(23))
#define AGC_GAIN_FORCE_EN_S 23
#define AGC_FAST_GAIN_SET (BIT(22))
#define AGC_FAST_GAIN_SET_S 22
#define AGC_MIN_GAIN 0x0000007F
#define AGC_MIN_GAIN_S 15
#define AGC_MAX_GAIN 0x0000007F
#define AGC_MAX_GAIN_S 8
#define AGC_RXGAIN_COMP 0x000000FF
#define AGC_RXGAIN_COMP_S 0

#define AGCFSM_CTRL1_REG (REG_AGC_BASE + 0x0030)
#define AGC_11N_GAIN_EN (BIT(31))
#define AGC_11N_GAIN_EN_S 31
#define AGC_11B_2ND_GAIN_EN (BIT(30))
#define AGC_11B_2ND_GAIN_EN_S 30
#define AGC_DIS (BIT(29))
#define AGC_DIS_S 29
#define AGC_START_DELAY 0x000003FF
#define AGC_START_DELAY_S 19
#define AGC_ANT_TIME 0x0000007F
#define AGC_ANT_TIME_S 11
#define AGC_RESTART_ST_EXT 0x00000003
#define AGC_RESTART_ST_EXT_S 9
#define AGC_RESET_SW (BIT(8))
#define AGC_RESET_SW_S 8
#define AGC_PWR_GO_DOWN_IND_EN (BIT(7))
#define AGC_PWR_GO_DOWN_IND_EN_S 7
#define AGC_RESTART_EN (BIT(6))
#define AGC_RESTART_EN_S 6
#define AGC_11B_EN (BIT(5))
#define AGC_11B_EN_S 5
#define AGC_11AB_EN (BIT(4))
#define AGC_11AB_EN_S 4
#define AGC_GAIN_TUNE_MIN 0x00000007
#define AGC_GAIN_TUNE_MIN_S 1
#define AGC_ADCSAT_HOLD (BIT(0))
#define AGC_ADCSAT_HOLD_S 0

#define AGCFSM_CTRL2_REG (REG_AGC_BASE + 0x0034)
#define AGC_ADC_DC_RM_TIME 0x0000007F
#define AGC_ADC_DC_RM_TIME_S 24
#define AGC_MODEM_TIME 0x0000007F
#define AGC_MODEM_TIME_S 16
#define AGC_MEASURE_TIME 0x0000007F
#define AGC_MEASURE_TIME_S 8
#define AGC_SETTLING_TIME 0x0000007F
#define AGC_SETTLING_TIME_S 0

#define AGCFSM_CTRL3_REG (REG_AGC_BASE + 0x0038)
#define AGC_DET_2_FINE_EN (BIT(31))
#define AGC_DET_2_FINE_EN_S 31
#define AGC_MODECHK_TIM_PROT (BIT(30))
#define AGC_MODECHK_TIM_PROT_S 30
#define AGC_GAIN_UPD_DIS (BIT(29))
#define AGC_GAIN_UPD_DIS_S 29
#define AGC_DONE_FORCE (BIT(28))
#define AGC_DONE_FORCE_S 28
#define AGC_FAST_CHECK (BIT(27))
#define AGC_FAST_CHECK_S 27
#define AGC_STRONG_CHECK (BIT(26))
#define AGC_STRONG_CHECK_S 26
#define AGC_PWR_CHECK_WAIT_COUNT 0x00000007
#define AGC_PWR_CHECK_WAIT_COUNT_S 23
#define AGC_FIR_DC_RM_TIME 0x0000007F
#define AGC_FIR_DC_RM_TIME_S 16
#define AGC_RX_END_TD_CLR (BIT(15))
#define AGC_RX_END_TD_CLR_S 15
#define AGC_MEASURE_DELAY_B 0x0000001F
#define AGC_MEASURE_DELAY_B_S 10
#define AGC_MEASURE_DELAY_A 0x0000001F
#define AGC_MEASURE_DELAY_A_S 5
#define AGC_MEASURE_DELAY_AB 0x0000001F
#define AGC_MEASURE_DELAY_AB_S 0

#define AGCMEM_CTRL1_REG (REG_AGC_BASE + 0x003c)
#define AGC_DCMEM_CLR (BIT(20))
#define AGC_DCMEM_CLR_S 20
#define AGC_DCMEM_FORCE_EN (BIT(19))
#define AGC_DCMEM_FORCE_EN_S 19
#define AGC_DCMEM_WEN (BIT(18))
#define AGC_DCMEM_WEN_S 18
#define AGC_DCMEM_REN (BIT(17))
#define AGC_DCMEM_REN_S 17
#define AGCMEM_WEN (BIT(16))
#define AGCMEM_WEN_S 16
#define AGCMEM_WADDR 0x000000FF
#define AGCMEM_WADDR_S 8
#define AGCMEM_WBE 0x000000FF
#define AGCMEM_WBE_S 0

#define AGCMEM_CTRL2_REG (REG_AGC_BASE + 0x0040)
#define AGCMEM_WDATA 0xFFFFFFFF
#define AGCMEM_WDATA_S 0

#define AGC11B_CTRL1_REG (REG_AGC_BASE + 0x0044)
#define AGC_DAGC_EN (BIT(25))
#define AGC_DAGC_EN_S 25
#define AGC_OFDM_CCK_JUDGE_THR 0x000001FF
#define AGC_OFDM_CCK_JUDGE_THR_S 16
#define AGC_BCORR_SNR_EN (BIT(15))
#define AGC_BCORR_SNR_EN_S 15
#define AGC_BCORR_LT_EXT (BIT(14))
#define AGC_BCORR_LT_EXT_S 14
#define AGC_BCORR_PWR_THR 0x0000003F
#define AGC_BCORR_PWR_THR_S 8
#define AGC_BCORR_SNR_THR 0x000000FF
#define AGC_BCORR_SNR_THR_S 0

#define AGC11B_CTRL2_REG (REG_AGC_BASE + 0x0048)
#define AGC_JUDGE_CNT 0x0000007F
#define AGC_JUDGE_CNT_S 8
#define AGC_PWR_11B_DESIRED 0x000000FF
#define AGC_PWR_11B_DESIRED_S 0

#define AGCRD1_REG (REG_AGC_BASE + 0x004c)
#define AGC_R_IN_NOISE_CAL (BIT(24))
#define AGC_R_IN_NOISE_CAL_S 24
#define AGC_R_ADCPWR_SW 0x000000FF
#define AGC_R_ADCPWR_SW_S 16
#define AGC_R_PWR_FIR2_SW 0x000000FF
#define AGC_R_PWR_FIR2_SW_S 8
#define AGC_R_PWR_FE_SW 0x000000FF
#define AGC_R_PWR_FE_SW_S 0

#define AGCRD2_REG (REG_AGC_BASE + 0x0050)
#define AGC_RX_END_TD (BIT(30))
#define AGC_RX_END_TD_S 30
#define AGC_DCMEM_RDATA 0x000FFFFF
#define AGC_DCMEM_RDATA_S 10
#define AGC_NOISE_RSSI_SW 0x000003FF
#define AGC_NOISE_RSSI_SW_S 0

#define AGCOFDM_CTRL5_REG (REG_AGC_BASE + 0x0054)
#define AGC_USE_SELF_CORR_2 (BIT(31))
#define AGC_USE_SELF_CORR_2_S 31
#define AGC_CORR_DET_CNT_MAX_2 0x0000007F
#define AGC_CORR_DET_CNT_MAX_2_S 24
#define AGC_QUICK_OFDM_THR 0x000000FF
#define AGC_QUICK_OFDM_THR_S 16
#define AGC_QUICK_OFDM_EN (BIT(15))
#define AGC_QUICK_OFDM_EN_S 15
#define AGC_WEEK_RSSI_SC_THR_2 0x000000FF
#define AGC_WEEK_RSSI_SC_THR_2_S 7
#define AGC_CORR_START_CNT 0x0000007F
#define AGC_CORR_START_CNT_S 0

#define AGCPWR_CTRL8_REG (REG_AGC_BASE + 0x0058)
#define AGC_PWR_FINE_ADC 0x000001FF
#define AGC_PWR_FINE_ADC_S 22
#define AGC_ADCSAT_RSTA_EN_BT (BIT(21))
#define AGC_ADCSAT_RSTA_EN_BT_S 21
#define AGC_ADCSAT_RSTA_EN_11B (BIT(20))
#define AGC_ADCSAT_RSTA_EN_11B_S 20
#define AGC_ADCSAT_RSTA_EN (BIT(19))
#define AGC_ADCSAT_RSTA_EN_S 19
#define AGC_PWR_FINE_QUICK 0x000001FF
#define AGC_PWR_FINE_QUICK_S 10
#define AGC_QUICK_TUNE_EN (BIT(9))
#define AGC_QUICK_TUNE_EN_S 9
#define AGC_QUICK_TUNE_THR 0x000001FF
#define AGC_QUICK_TUNE_THR_S 0

#define AGCGAIN_CTRL_1_REG (REG_AGC_BASE + 0x005c)
#define AGC_DIS_RFAGC_SAT (BIT(29))
#define AGC_DIS_RFAGC_SAT_S 29
#define AGC_RFAGC_FSM_RST_EN (BIT(28))
#define AGC_RFAGC_FSM_RST_EN_S 28
#define AGC_RFAGC_EN_BT (BIT(27))
#define AGC_RFAGC_EN_BT_S 27
#define AGC_RFAGC_EN (BIT(26))
#define AGC_RFAGC_EN_S 26
#define AGC_RFAGC_EXIT_UPD_GAIN (BIT(25))
#define AGC_RFAGC_EXIT_UPD_GAIN_S 25
#define AGC_RFAGC_RSTB_AUTO_EN (BIT(24))
#define AGC_RFAGC_RSTB_AUTO_EN_S 24
#define AGC_RFAGC_RSTB_INV (BIT(23))
#define AGC_RFAGC_RSTB_INV_S 23
#define AGC_RFAGC_LNA_SAT_INV (BIT(22))
#define AGC_RFAGC_LNA_SAT_INV_S 22
#define AGC_RFAGC_VGA_SAT_INV (BIT(21))
#define AGC_RFAGC_VGA_SAT_INV_S 21
#define AGC_CHK_GAIN_MIN (BIT(20))
#define AGC_CHK_GAIN_MIN_S 20
#define AGC_RFAGC_EXIT_RST_ANA (BIT(19))
#define AGC_RFAGC_EXIT_RST_ANA_S 19
#define AGC_RF_AGC_TO_MAX 0x0007FFFF
#define AGC_RF_AGC_TO_MAX_S 0

#define AGCGAIN_CTRL_2_REG (REG_AGC_BASE + 0x0060)
#define AGC_GAIN_GT_4_BT 0x0000007F
#define AGC_GAIN_GT_4_BT_S 24
#define AGC_GAIN_GT_3_BT 0x0000007F
#define AGC_GAIN_GT_3_BT_S 16
#define AGC_GAIN_GT_2_BT 0x0000007F
#define AGC_GAIN_GT_2_BT_S 8
#define AGC_GAIN_GT_1_BT 0x0000007F
#define AGC_GAIN_GT_1_BT_S 0

#define AGCGAIN_CTRL_3_REG (REG_AGC_BASE + 0x0064)
#define AGC_GAIN_GT_4 0x0000007F
#define AGC_GAIN_GT_4_S 24
#define AGC_GAIN_GT_3 0x0000007F
#define AGC_GAIN_GT_3_S 16
#define AGC_GAIN_GT_2 0x0000007F
#define AGC_GAIN_GT_2_S 8
#define AGC_GAIN_GT_1 0x0000007F
#define AGC_GAIN_GT_1_S 0

#define AGCPKDET_CTRL_0_REG (REG_AGC_BASE + 0x0068)
#define AGC_PKDET_CTRL 0xFFFFFFFF
#define AGC_PKDET_CTRL_S 0

#define AGCRD9_REG (REG_AGC_BASE + 0x006c)
#define AGC_R_FINE_GAIN_SAT (BIT(24))
#define AGC_R_FINE_GAIN_SAT_S 24
#define AGC_R_RX_GAIN_2ND_SW 0x000000FF
#define AGC_R_RX_GAIN_2ND_SW_S 16
#define AGC_R_SIGRSSI_SW 0x000000FF
#define AGC_R_SIGRSSI_SW_S 8
#define AGC_R_RX_GAIN_SW 0x000000FF
#define AGC_R_RX_GAIN_SW_S 0

#define AGCOFDM_CTRL6_REG (REG_AGC_BASE + 0x0070)
#define AGC_WEEK_RSSI_CFO_THR 0x000000FF
#define AGC_WEEK_RSSI_CFO_THR_S 24
#define AGC_WEEK_RSSI_SC_THR 0x000000FF
#define AGC_WEEK_RSSI_SC_THR_S 16
#define AGC_OCORR_LT_RSSI_THR_2 0x000000FF
#define AGC_OCORR_LT_RSSI_THR_2_S 8
#define AGC_WEEK_RSSI_XC_THR 0x000000FF
#define AGC_WEEK_RSSI_XC_THR_S 0

#define AGCFSM_CTRL4_REG (REG_AGC_BASE + 0x0074)
#define AGC_RX11N_HBW_THR 0x00000007
#define AGC_RX11N_HBW_THR_S 28
#define AGC_RSSI_WEAK_11A_LATCH (BIT(27))
#define AGC_RSSI_WEAK_11A_LATCH_S 27
#define AGC_RSSI_WEAK_LATCH (BIT(26))
#define AGC_RSSI_WEAK_LATCH_S 26
#define AGC_RSSI_WEAK_ANT_OPT_11A (BIT(25))
#define AGC_RSSI_WEAK_ANT_OPT_11A_S 25
#define AGC_RSSI_WEAK_ANT_OPT (BIT(24))
#define AGC_RSSI_WEAK_ANT_OPT_S 24
#define AGC_FIND_DIS_RSSI_UPD (BIT(23))
#define AGC_FIND_DIS_RSSI_UPD_S 23
#define AGC_FORCE_CCA_SEC (BIT(22))
#define AGC_FORCE_CCA_SEC_S 22
#define AGC_FORCE_CCA_SEC_EN (BIT(21))
#define AGC_FORCE_CCA_SEC_EN_S 21
#define AGC_FORCE_CCA (BIT(20))
#define AGC_FORCE_CCA_S 20
#define AGC_FORCE_CCA_EN (BIT(19))
#define AGC_FORCE_CCA_EN_S 19
#define AGC_DIS_CCA (BIT(18))
#define AGC_DIS_CCA_S 18
#define AGC_GAIN_TUNE_MAX 0x00000007
#define AGC_GAIN_TUNE_MAX_S 15
#define AGC_2ND_USE_INIT_DC (BIT(14))
#define AGC_2ND_USE_INIT_DC_S 14
#define AGC_CHAN_MERGE_DIS (BIT(13))
#define AGC_CHAN_MERGE_DIS_S 13
#define AGC_CORR_DIS (BIT(12))
#define AGC_CORR_DIS_S 12
#define AGC_FINE_2ND_CNT 0x00000007
#define AGC_FINE_2ND_CNT_S 9
#define AGC_PWR_VOTE_1ST (BIT(8))
#define AGC_PWR_VOTE_1ST_S 8
#define AGC_GAIN_SAME_EN (BIT(7))
#define AGC_GAIN_SAME_EN_S 7
#define AGC_SETTLING_2_TIME 0x0000007F
#define AGC_SETTLING_2_TIME_S 0

#define AGCRD3_REG (REG_AGC_BASE + 0x0078)
#define AGC_BB_DIAG_0 0x0000FFFF
#define AGC_BB_DIAG_0_S 16
#define AGC_STATE 0x0000000F
#define AGC_STATE_S 8
#define AGC_RX_GAIN 0x000000FF
#define AGC_RX_GAIN_S 0

#define AGCBT_CTRL0_REG (REG_AGC_BASE + 0x007c)
#define AGC_BT_GAIN_MIN_RESTART_EN (BIT(31))
#define AGC_BT_GAIN_MIN_RESTART_EN_S 31
#define AGC_BT_GAIN_MAX_RESTART_EN (BIT(30))
#define AGC_BT_GAIN_MAX_RESTART_EN_S 30
#define AGC_BT_RXPWR_CMP_SEL 0x00000003
#define AGC_BT_RXPWR_CMP_SEL_S 28
#define AGC_BT_RXPWR_VAR_THR 0x0000000F
#define AGC_BT_RXPWR_VAR_THR_S 24
#define AGC_BT_RSSI_THR 0x000000FF
#define AGC_BT_RSSI_THR_S 16
#define AGC_BT_PWDET_V_CNT 0x000000FF
#define AGC_BT_PWDET_V_CNT_S 8
#define AGC_BT_PWDET_S_CNT 0x000000FF
#define AGC_BT_PWDET_S_CNT_S 0

#define AGCBT_CTRL1_REG (REG_AGC_BASE + 0x0080)
#define AGC_GAIN_TUNE_MIN_BT 0x00000007
#define AGC_GAIN_TUNE_MIN_BT_S 29
#define AGC_BT_PWR_OFS 0x0000003F
#define AGC_BT_PWR_OFS_S 23
#define AGC_PWR_FINE_2ND_OFS_BT 0x0000003F
#define AGC_PWR_FINE_2ND_OFS_BT_S 17
#define AGC_PWR_FINE_1ST_BT 0x000001FF
#define AGC_PWR_FINE_1ST_BT_S 8
#define AGC_FORCE_BT_MODE 0x00000003
#define AGC_FORCE_BT_MODE_S 6
#define AGC_BT_RXPWR_CHK_S 0x0000001F
#define AGC_BT_RXPWR_CHK_S_S 1
#define AGC_FORCE_BB_OFF (BIT(0))
#define AGC_FORCE_BB_OFF_S 0

#define AGCBT_CTRL2_REG (REG_AGC_BASE + 0x0084)
#define AGC_BT_GAIN_MAXMIN_RECORRECT_EN (BIT(31))
#define AGC_BT_GAIN_MAXMIN_RECORRECT_EN_S 31
#define AGC_PWR_FINE_RECORRECT_INF_BT (BIT(30))
#define AGC_PWR_FINE_RECORRECT_INF_BT_S 30
#define AGC_PWR_RESTART_REF_SEL_BT (BIT(29))
#define AGC_PWR_RESTART_REF_SEL_BT_S 29
#define AGC_PWR_FINE_RECORRECT_EN_LE (BIT(28))
#define AGC_PWR_FINE_RECORRECT_EN_LE_S 28
#define AGC_PWR_FINE_RECORRECT_EN_BT (BIT(27))
#define AGC_PWR_FINE_RECORRECT_EN_BT_S 27
#define AGC_PWR_FINE_RECORRECT_THR_BT 0x0000001F
#define AGC_PWR_FINE_RECORRECT_THR_BT_S 22
#define AGC_PWR_RISEDROP_BT_ERROR_EN (BIT(21))
#define AGC_PWR_RISEDROP_BT_ERROR_EN_S 21
#define AGC_PWR_DROP_THR_BT_ERROR 0x0000003F
#define AGC_PWR_DROP_THR_BT_ERROR_S 15
#define AGC_PWR_RESTART_THR_BT_ERROR 0x0000003F
#define AGC_PWR_RESTART_THR_BT_ERROR_S 9
#define AGC_BT_PWR_FINE_ADC 0x000001FF
#define AGC_BT_PWR_FINE_ADC_S 0

#define AGCHT2040_SCALE_REG (REG_AGC_BASE + 0x0088)
#define AGC_HT2040_SCALE_EN (BIT(8))
#define AGC_HT2040_SCALE_EN_S 8
#define AGC_HT2040_SCALE 0x000000FF
#define AGC_HT2040_SCALE_S 0

#define AGCRD4_REG (REG_AGC_BASE + 0x008c)
#define AGC_R_GAIN_MAX_PKD_BT_CUR 0x0000007F
#define AGC_R_GAIN_MAX_PKD_BT_CUR_S 19
#define AGC_R_GAIN_MAX_PKD_CUR 0x0000007F
#define AGC_R_GAIN_MAX_PKD_CUR_S 12
#define AGC_NOISE_RSSI 0x00000FFF
#define AGC_NOISE_RSSI_S 0

#define AGCPWR_CTRL9_REG (REG_AGC_BASE + 0x0090)
#define AGC_PWR_DROP_THR_BT 0x0000003F
#define AGC_PWR_DROP_THR_BT_S 26
#define AGC_PWR_RESTART_THR_BT 0x0000003F
#define AGC_PWR_RESTART_THR_BT_S 20
#define AGC_PWR_DROP_THR_11B 0x0000001F
#define AGC_PWR_DROP_THR_11B_S 15
#define AGC_PWR_RESTART_THR_11B 0x0000001F
#define AGC_PWR_RESTART_THR_11B_S 10
#define AGC_PWR_DROP_THR 0x0000001F
#define AGC_PWR_DROP_THR_S 5
#define AGC_PWR_RESTART_THR 0x0000001F
#define AGC_PWR_RESTART_THR_S 0

#define AGCGAIN_CTRL_4_REG (REG_AGC_BASE + 0x0094)
#define AGC_RCV_EXIT_EN (BIT(31))
#define AGC_RCV_EXIT_EN_S 31
#define AGC_MDCHK_EXIT_EN 0x00000007
#define AGC_MDCHK_EXIT_EN_S 28
#define AGC_FINE_EXIT_EN 0x00000007
#define AGC_FINE_EXIT_EN_S 25
#define AGC_INIT_USE_FINE (BIT(24))
#define AGC_INIT_USE_FINE_S 24
#define AGC_PWR_LT_GAIN_OPT (BIT(23))
#define AGC_PWR_LT_GAIN_OPT_S 23
#define AGC_PWR_LT_GAIN_JUMP 0x0000007F
#define AGC_PWR_LT_GAIN_JUMP_S 16
#define AGC_INIT_GAIN_OFS 0x0000007F
#define AGC_INIT_GAIN_OFS_S 9
#define AGC_INIT_GAIN 0x0000007F
#define AGC_INIT_GAIN_S 2
#define AGC_INIT_SET_EN (BIT(1))
#define AGC_INIT_SET_EN_S 1
#define AGC_INIT_GAIN_EN (BIT(0))
#define AGC_INIT_GAIN_EN_S 0

#define AGCRD5_REG (REG_AGC_BASE + 0x0098)
#define AGC_DIAG_AGC_1 0xFFFFFFFF
#define AGC_DIAG_AGC_1_S 0

#define AGCRD6_REG (REG_AGC_BASE + 0x009c)
#define AGC_DIAG_AGC_2 0xFFFFFFFF
#define AGC_DIAG_AGC_2_S 0

#define AGCPWR_CTRL10_REG (REG_AGC_BASE + 0x00a0)
#define AGC_RXGAIN_COMP_HT2040 0x000000FF
#define AGC_RXGAIN_COMP_HT2040_S 24
#define AGC_RESTART_GT_THR 0x000000FF
#define AGC_RESTART_GT_THR_S 16
#define AGC_PWR_TOO_LT_GAIN_JUMP 0x0000007F
#define AGC_PWR_TOO_LT_GAIN_JUMP_S 9
#define AGC_PWR_TOO_LOW_THR 0x000001FF
#define AGC_PWR_TOO_LOW_THR_S 0

#define AGCGAIN_CTRL_5_REG (REG_AGC_BASE + 0x00a4)
#define AGC_MIN_GAIN_BT 0x0000007F
#define AGC_MIN_GAIN_BT_S 22
#define AGC_MAX_GAIN_BT 0x0000007F
#define AGC_MAX_GAIN_BT_S 15
#define AGC_SEARCH_FAIL_TUNE (BIT(14))
#define AGC_SEARCH_FAIL_TUNE_S 14
#define AGC_MAX_GAIN_LT 0x0000007F
#define AGC_MAX_GAIN_LT_S 7
#define AGC_MAX_GAIN_TOO_LT 0x0000007F
#define AGC_MAX_GAIN_TOO_LT_S 0

#define AGCSEC_CTRL0_REG (REG_AGC_BASE + 0x00a8)
#define AGC_PWR_SEC_GT_THR 0x0000003F
#define AGC_PWR_SEC_GT_THR_S 8
#define AGC_SIG_WEAK_SEC_THR 0x000000FF
#define AGC_SIG_WEAK_SEC_THR_S 0

#define AGCPWR_CTRL11_REG (REG_AGC_BASE + 0x00ac)
#define AGC_REST_FINE_PWR_SEL 0x00000003
#define AGC_REST_FINE_PWR_SEL_S 27
#define AGC_PWR_FINE_MCS2 0x000001FF
#define AGC_PWR_FINE_MCS2_S 18
#define AGC_PWR_FINE_MCS1 0x000001FF
#define AGC_PWR_FINE_MCS1_S 9
#define AGC_PWR_FINE_MCS0 0x000001FF
#define AGC_PWR_FINE_MCS0_S 0

#define AGCPWR_CTRL12_REG (REG_AGC_BASE + 0x00b0)
#define AGC_PWR_FINE_MCS5 0x000001FF
#define AGC_PWR_FINE_MCS5_S 18
#define AGC_PWR_FINE_MCS4 0x000001FF
#define AGC_PWR_FINE_MCS4_S 9
#define AGC_PWR_FINE_MCS3 0x000001FF
#define AGC_PWR_FINE_MCS3_S 0

#define AGCPWR_CTRL13_REG (REG_AGC_BASE + 0x00b4)
#define AGC_PWR_FE2_TONERM_EN (BIT(30))
#define AGC_PWR_FE2_TONERM_EN_S 30
#define AGC_PWR_FE_DCRM_EN (BIT(29))
#define AGC_PWR_FE_DCRM_EN_S 29
#define AGC_PWR_FINE_SEL_FE (BIT(28))
#define AGC_PWR_FINE_SEL_FE_S 28
#define AGC_PWR_COARSE_SEL_FE (BIT(27))
#define AGC_PWR_COARSE_SEL_FE_S 27
#define AGC_PWR_COARSE_ADC 0x000001FF
#define AGC_PWR_COARSE_ADC_S 18
#define AGC_PWR_FINE_MCS7 0x000001FF
#define AGC_PWR_FINE_MCS7_S 9
#define AGC_PWR_FINE_MCS6 0x000001FF
#define AGC_PWR_FINE_MCS6_S 0

#define AGCTEST_CTRL_REG (REG_AGC_BASE + 0x00b8)
#define AGC_CORR_FORCE_CLK (BIT(16))
#define AGC_CORR_FORCE_CLK_S 16
#define AGC_CORR_HT40_FORCE_CLK (BIT(15))
#define AGC_CORR_HT40_FORCE_CLK_S 15
#define AGC_FORCE_CLK (BIT(14))
#define AGC_FORCE_CLK_S 14
#define AGC_11B_FORCE_CLK (BIT(13))
#define AGC_11B_FORCE_CLK_S 13
#define AGC_FILT_ATT1DB_EN_SEC (BIT(12))
#define AGC_FILT_ATT1DB_EN_SEC_S 12
#define AGC_FILT_ATT1DB_EN (BIT(11))
#define AGC_FILT_ATT1DB_EN_S 11
#define AGCCLK_EN (BIT(10))
#define AGCCLK_EN_S 10
#define AGC_TEST_CTRL 0x000003FF
#define AGC_TEST_CTRL_S 0

#define AGCOFDM_CTRL7_REG (REG_AGC_BASE + 0x00bc)
#define AGC_CORR_VAL_AFTER_GAIN_3_EN (BIT(26))
#define AGC_CORR_VAL_AFTER_GAIN_3_EN_S 26
#define AGC_CORR_VAL_AFTER_GAIN_2_EN (BIT(25))
#define AGC_CORR_VAL_AFTER_GAIN_2_EN_S 25
#define AGC_CORR_VAL_AFTER_GAIN_EN (BIT(24))
#define AGC_CORR_VAL_AFTER_GAIN_EN_S 24
#define AGC_CORR_VAL_AFTER_GAIN_3 0x000000FF
#define AGC_CORR_VAL_AFTER_GAIN_3_S 16
#define AGC_CORR_VAL_AFTER_GAIN_2 0x000000FF
#define AGC_CORR_VAL_AFTER_GAIN_2_S 8
#define AGC_CORR_VAL_AFTER_GAIN 0x000000FF
#define AGC_CORR_VAL_AFTER_GAIN_S 0

#define AGCRD7_REG (REG_AGC_BASE + 0x00c0)
#define AGC_DIAG_AGC_3 0xFFFFFFFF
#define AGC_DIAG_AGC_3_S 0

#define AGCOFDM_CTRL8_REG (REG_AGC_BASE + 0x00c4)
#define AGC_CORR_PWR_RISE_CHK (BIT(30))
#define AGC_CORR_PWR_RISE_CHK_S 30
#define AGC_CORR_PWR_RISE_CHK_2 (BIT(29))
#define AGC_CORR_PWR_RISE_CHK_2_S 29
#define AGC_CORR_USE_XCORR (BIT(28))
#define AGC_CORR_USE_XCORR_S 28
#define AGC_CORR_USE_XCORR_2 (BIT(27))
#define AGC_CORR_USE_XCORR_2_S 27
#define AGC_PWR_VALID_CNT_INIT_3 0x0000000F
#define AGC_PWR_VALID_CNT_INIT_3_S 23
#define AGC_PWR_FIR_GT_THR_3 0x000003FF
#define AGC_PWR_FIR_GT_THR_3_S 13
#define AGC_PWR_FIR_SURGE_THR_3 0x0000007F
#define AGC_PWR_FIR_SURGE_THR_3_S 6
#define AGC_PWR_INBAND_SURGE_THR_3 0x0000003F
#define AGC_PWR_INBAND_SURGE_THR_3_S 0

#define AGCOFDM_CTRL9_REG (REG_AGC_BASE + 0x00c8)
#define AGC_PWR_FIR_GT_NOISE_THR 0x000000FF
#define AGC_PWR_FIR_GT_NOISE_THR_S 24
#define AGC_PWR_FIR_GT_NOISE_THR_2 0x000000FF
#define AGC_PWR_FIR_GT_NOISE_THR_2_S 16
#define AGC_PWR_FIR_GT_NOISE_THR_3 0x000000FF
#define AGC_PWR_FIR_GT_NOISE_THR_3_S 8
#define AGC_OCORR_GT_NOISE_THR_VOTE 0x000000FF
#define AGC_OCORR_GT_NOISE_THR_VOTE_S 0

#define AGCOFDM_CTRL10_REG (REG_AGC_BASE + 0x00cc)
#define AGC_XCORR_SNR_THR_EN_1 (BIT(31))
#define AGC_XCORR_SNR_THR_EN_1_S 31
#define AGC_XCORR_SNR_THR_EN_2 (BIT(30))
#define AGC_XCORR_SNR_THR_EN_2_S 30
#define AGC_GAIN_FIR_GT_THR_3 0x000003FF
#define AGC_GAIN_FIR_GT_THR_3_S 20
#define AGC_GAIN_FIR_GT_THR_2 0x000003FF
#define AGC_GAIN_FIR_GT_THR_2_S 10
#define AGC_GAIN_FIR_GT_THR_1 0x000003FF
#define AGC_GAIN_FIR_GT_THR_1_S 0

#define AGCBT_CTRL3_REG (REG_AGC_BASE + 0x00d0)
#define AGC_BT_GAIN_OFFSET 0x000000FF
#define AGC_BT_GAIN_OFFSET_S 17
#define AGC_RXGAIN_COMP_BT 0x000000FF
#define AGC_RXGAIN_COMP_BT_S 9
#define AGC_PWR_FINE_1ST_LE 0x000001FF
#define AGC_PWR_FINE_1ST_LE_S 0

#define AGCOFDM_CTRL12_REG (REG_AGC_BASE + 0x00d4)
#define AGC_CORR_LG_PPM (BIT(26))
#define AGC_CORR_LG_PPM_S 26
#define AGC_CORR_LG_PPM_2 (BIT(25))
#define AGC_CORR_LG_PPM_2_S 25
#define AGC_CORR_PTG_EN2 (BIT(24))
#define AGC_CORR_PTG_EN2_S 24
#define AGC_CORR_PTG_THR 0x0000000F
#define AGC_CORR_PTG_THR_S 20
#define AGC_CORR_PTG_MAX 0x0000000F
#define AGC_CORR_PTG_MAX_S 16
#define AGC_CORR_PTG_EN1 (BIT(15))
#define AGC_CORR_PTG_EN1_S 15
#define AGC_CORR_START_CNT_2 0x0000007F
#define AGC_CORR_START_CNT_2_S 8
#define AGC_WEEK_RSSI_XC_THR_2 0x000000FF
#define AGC_WEEK_RSSI_XC_THR_2_S 0

#define AGCPWR_CTRL14_REG (REG_AGC_BASE + 0x00d8)
#define AGC_ADCSAT_THR_RST 0x000001FF
#define AGC_ADCSAT_THR_RST_S 20
#define AGC_PWR_GT_FE_CHK (BIT(19))
#define AGC_PWR_GT_FE_CHK_S 19
#define AGC_PWR_LT_FE_CHK (BIT(18))
#define AGC_PWR_LT_FE_CHK_S 18
#define AGC_PWR_FE_HIGH_THR 0x000001FF
#define AGC_PWR_FE_HIGH_THR_S 9
#define AGC_PWR_COARSE_INIT 0x000001FF
#define AGC_PWR_COARSE_INIT_S 0

#define AGCCCA_CTRL0_REG (REG_AGC_BASE + 0x00dc)
#define AGC_CCA_THR_SEC 0x0000000F
#define AGC_CCA_THR_SEC_S 12
#define AGC_CCA_DLY_LEN_SEC 0x0000000F
#define AGC_CCA_DLY_LEN_SEC_S 8
#define AGC_CCA_THR 0x0000000F
#define AGC_CCA_THR_S 4
#define AGC_CCA_DLY_LEN 0x0000000F
#define AGC_CCA_DLY_LEN_S 0

#define AGCGAIN_CTRL_6_REG (REG_AGC_BASE + 0x00e0)
#define AGC_RSSI_2ND_11N_MCS3 0x000000FF
#define AGC_RSSI_2ND_11N_MCS3_S 24
#define AGC_RSSI_2ND_11N_MCS2 0x000000FF
#define AGC_RSSI_2ND_11N_MCS2_S 16
#define AGC_RSSI_2ND_11N_MCS1 0x000000FF
#define AGC_RSSI_2ND_11N_MCS1_S 8
#define AGC_RSSI_2ND_11N_MCS0 0x000000FF
#define AGC_RSSI_2ND_11N_MCS0_S 0

#define AGCGAIN_CTRL_7_REG (REG_AGC_BASE + 0x00e4)
#define AGC_RSSI_2ND_11N_MCS7 0x000000FF
#define AGC_RSSI_2ND_11N_MCS7_S 24
#define AGC_RSSI_2ND_11N_MCS6 0x000000FF
#define AGC_RSSI_2ND_11N_MCS6_S 16
#define AGC_RSSI_2ND_11N_MCS5 0x000000FF
#define AGC_RSSI_2ND_11N_MCS5_S 8
#define AGC_RSSI_2ND_11N_MCS4 0x000000FF
#define AGC_RSSI_2ND_11N_MCS4_S 0

#define AGCCHAN_BW_REG (REG_AGC_BASE + 0x00e8)
#define AGC_CHBW_MULT_THR 0x00000007
#define AGC_CHBW_MULT_THR_S 27
#define AGC_CHBW_SHIFT_THR 0x00000007
#define AGC_CHBW_SHIFT_THR_S 24
#define AGC_CHANBW_CORR_THR_2 0x000000FF
#define AGC_CHANBW_CORR_THR_2_S 16
#define AGC_CHANBW_CORR_THR_1 0x000000FF
#define AGC_CHANBW_CORR_THR_1_S 8
#define AGC_WEEK_RSSI_CHANBW_THR 0x000000FF
#define AGC_WEEK_RSSI_CHANBW_THR_S 0

#define AGCOFDM_CTRL11_REG (REG_AGC_BASE + 0x00ec)
#define AGC_PWR_FIR_STAB_THR_SPUR 0x0000007F
#define AGC_PWR_FIR_STAB_THR_SPUR_S 25
#define AGC_PWR_STAB_SEL (BIT(24))
#define AGC_PWR_STAB_SEL_S 24
#define AGC_PWR_STAB_1_CHK (BIT(23))
#define AGC_PWR_STAB_1_CHK_S 23
#define AGC_PWR_STAB_2_CHK (BIT(22))
#define AGC_PWR_STAB_2_CHK_S 22
#define AGC_PWR_STAB_3_CHK (BIT(21))
#define AGC_PWR_STAB_3_CHK_S 21
#define AGC_PWR_FIR_STAB_THR_3 0x0000007F
#define AGC_PWR_FIR_STAB_THR_3_S 14
#define AGC_PWR_FIR_STAB_THR_2 0x0000007F
#define AGC_PWR_FIR_STAB_THR_2_S 7
#define AGC_PWR_FIR_STAB_THR_1 0x0000007F
#define AGC_PWR_FIR_STAB_THR_1_S 0

#define AGCPWR_CTRL15_REG (REG_AGC_BASE + 0x00f0)
#define AGC_XCORR_SNR_THR_H 0x000001FF
#define AGC_XCORR_SNR_THR_H_S 23
#define AGC_XCORR_SNR_THR_L 0x000001FF
#define AGC_XCORR_SNR_THR_L_S 14
#define AGC_PWR_RSTA_CHK_TONE (BIT(13))
#define AGC_PWR_RSTA_CHK_TONE_S 13
#define AGC_PWR_RESTART_ADD 0x0000001F
#define AGC_PWR_RESTART_ADD_S 8
#define AGC_WEEK_RSSI_RSTA_THR 0x000000FF
#define AGC_WEEK_RSSI_RSTA_THR_S 0

#define AGCFSM_CTRL5_REG (REG_AGC_BASE + 0x00f4)
#define AGC_ST_WAIT_CNT 0x00000007
#define AGC_ST_WAIT_CNT_S 29
#define AGC_PWR_SEC_ANTI_ENG (BIT(28))
#define AGC_PWR_SEC_ANTI_ENG_S 28
#define AGC_PWR_SEC_ANTI_SCORR (BIT(27))
#define AGC_PWR_SEC_ANTI_SCORR_S 27
#define AGC_PWR_SEC_ANTI_THR 0x000000FF
#define AGC_PWR_SEC_ANTI_THR_S 19
#define AGC_RIFS_CNT_START 0x000001FF
#define AGC_RIFS_CNT_START_S 10
#define AGC_RIFS_CNT_INIT 0x000001FF
#define AGC_RIFS_CNT_INIT_S 1
#define AGC_RIFS_MODE_EN (BIT(0))
#define AGC_RIFS_MODE_EN_S 0

#define AGCPWR_CTRL16_REG (REG_AGC_BASE + 0x00f8)
#define AGC_FINE_PWR_NUM 0x00000007
#define AGC_FINE_PWR_NUM_S 29
#define AGC_PWR_FINE_LT_HT2040 (BIT(28))
#define AGC_PWR_FINE_LT_HT2040_S 28
#define AGC_PWR_FINE_LT_HT20 (BIT(27))
#define AGC_PWR_FINE_LT_HT20_S 27
#define AGC_PWR_LT_FE_CHK_GT_THR 0x000001FF
#define AGC_PWR_LT_FE_CHK_GT_THR_S 18
#define AGC_PWR_COARSE_PRI_LOW 0x000001FF
#define AGC_PWR_COARSE_PRI_LOW_S 9
#define AGC_PWR_LOW_PRI_THR 0x000001FF
#define AGC_PWR_LOW_PRI_THR_S 0

#define AGCPWR_CTRL17_REG (REG_AGC_BASE + 0x00fc)
#define AGC_PWR_FINE_LT_BT (BIT(28))
#define AGC_PWR_FINE_LT_BT_S 28
#define AGC_PWR_LT_FE_CHK_BT (BIT(27))
#define AGC_PWR_LT_FE_CHK_BT_S 27
#define AGC_PWR_LT_FE_CHK_GT_THR_BT 0x000001FF
#define AGC_PWR_LT_FE_CHK_GT_THR_BT_S 18
#define AGC_PWR_COARSE_PRI_LOW_BT 0x000001FF
#define AGC_PWR_COARSE_PRI_LOW_BT_S 9
#define AGC_PWR_LOW_PRI_THR_BT 0x000001FF
#define AGC_PWR_LOW_PRI_THR_BT_S 0

#define AGCRD8_REG (REG_AGC_BASE + 0x0100)
#define AGC_DIAG_AGC_4 0xFFFFFFFF
#define AGC_DIAG_AGC_4_S 0

#define AGCPWR_CTRL18_REG (REG_AGC_BASE + 0x0104)
#define AGC_PWR_HT40_CHK_THR 0x000000FF
#define AGC_PWR_HT40_CHK_THR_S 24
#define AGC_HT40_RSSI_CHK_THR 0x000000FF
#define AGC_HT40_RSSI_CHK_THR_S 16
#define AGC_PWR_HT40_CHK_EN (BIT(15))
#define AGC_PWR_HT40_CHK_EN_S 15
#define AGC_GAIN_HT40_EN (BIT(14))
#define AGC_GAIN_HT40_EN_S 14
#define AGC_PWR_FINE_2ND_11B 0x000001FF
#define AGC_PWR_FINE_2ND_11B_S 0

#define AGCOFDM_CTRL13_REG (REG_AGC_BASE + 0x0108)
#define AGC_OCORR_THR4 0x000000FF
#define AGC_OCORR_THR4_S 24
#define AGC_CORR_DET_CNT_MAX_4 0x0000007F
#define AGC_CORR_DET_CNT_MAX_4_S 16
#define AGC_CORR_DET_THR_4 0x0000003F
#define AGC_CORR_DET_THR_4_S 10
#define AGC_CORR_USE_XCORR_GT_2 (BIT(9))
#define AGC_CORR_USE_XCORR_GT_2_S 9
#define AGC_CORR_USE_XCORR_GT (BIT(8))
#define AGC_CORR_USE_XCORR_GT_S 8
#define AGC_WEEK_RSSI_GI_THR 0x000000FF
#define AGC_WEEK_RSSI_GI_THR_S 0

#define AGCPWR_CTRL19_REG (REG_AGC_BASE + 0x010c)
#define AGC_PWR_CHG_ERR_RCV_GT_THR 0x000000FF
#define AGC_PWR_CHG_ERR_RCV_GT_THR_S 24
#define AGC_PWR_CHG_ERR_RCV_LT_THR 0x000000FF
#define AGC_PWR_CHG_ERR_RCV_LT_THR_S 16
#define AGC_PWR_CHG_ERR_GT_THR 0x000000FF
#define AGC_PWR_CHG_ERR_GT_THR_S 8
#define AGC_PWR_CHG_ERR_LT_THR 0x000000FF
#define AGC_PWR_CHG_ERR_LT_THR_S 0

#define AGCGAIN_CTRL_8_REG (REG_AGC_BASE + 0x0110)
#define AGC_GAIN_GT_4_MAX_BT 0x0000007F
#define AGC_GAIN_GT_4_MAX_BT_S 24
#define AGC_GAIN_GT_3_MAX_BT 0x0000007F
#define AGC_GAIN_GT_3_MAX_BT_S 16
#define AGC_GAIN_GT_2_MAX_BT 0x0000007F
#define AGC_GAIN_GT_2_MAX_BT_S 8
#define AGC_GAIN_GT_1_MAX_BT 0x0000007F
#define AGC_GAIN_GT_1_MAX_BT_S 0

#define AGCGAIN_CTRL_9_REG (REG_AGC_BASE + 0x0114)
#define AGC_GAIN_GT_4_MAX 0x0000007F
#define AGC_GAIN_GT_4_MAX_S 24
#define AGC_GAIN_GT_3_MAX 0x0000007F
#define AGC_GAIN_GT_3_MAX_S 16
#define AGC_GAIN_GT_2_MAX 0x0000007F
#define AGC_GAIN_GT_2_MAX_S 8
#define AGC_GAIN_GT_1_MAX 0x0000007F
#define AGC_GAIN_GT_1_MAX_S 0

#define AGCGAIN_CTRL_10_REG (REG_AGC_BASE + 0x0118)
#define AGC_QUICKDROP_GAIN_THR 0x000000FF
#define AGC_QUICKDROP_GAIN_THR_S 24
#define AGC_QUICKDROP_NO_PKD2 0x000000FF
#define AGC_QUICKDROP_NO_PKD2_S 16
#define AGC_QUICKDROP_PKD 0x000000FF
#define AGC_QUICKDROP_PKD_S 8
#define AGC_QUICKDROP_NO_PKD 0x000000FF
#define AGC_QUICKDROP_NO_PKD_S 0

#define AGCANT_CTRL1_REG (REG_AGC_BASE + 0x011c)
#define AGC_ANT_DC_RM_TIME 0x0000007F
#define AGC_ANT_DC_RM_TIME_S 16
#define AGC_ANT_MAC_EN (BIT(15))
#define AGC_ANT_MAC_EN_S 15
#define AGC_ANT_RST_EN (BIT(14))
#define AGC_ANT_RST_EN_S 14
#define AGC_ANT_11B_BACK (BIT(13))
#define AGC_ANT_11B_BACK_S 13
#define AGC_ANT_CUR_FORCE_EN (BIT(12))
#define AGC_ANT_CUR_FORCE_EN_S 12
#define AGC_ANT_CUR_FORCE (BIT(11))
#define AGC_ANT_CUR_FORCE_S 11
#define AGC_GAIN_ANT1_COMP 0x0000007F
#define AGC_GAIN_ANT1_COMP_S 4
#define AGC_ANT_CHK_BT (BIT(3))
#define AGC_ANT_CHK_BT_S 3
#define AGC_ANT_CHK_OFDM2 (BIT(2))
#define AGC_ANT_CHK_OFDM2_S 2
#define AGC_ANT_CHK_CCK (BIT(1))
#define AGC_ANT_CHK_CCK_S 1
#define AGC_ANT_CHK_OFDM (BIT(0))
#define AGC_ANT_CHK_OFDM_S 0

#define AGCANT_CTRL2_REG (REG_AGC_BASE + 0x0120)
#define AGC_RSSI_ANT_BT_THR 0x000000FF
#define AGC_RSSI_ANT_BT_THR_S 24
#define AGC_RSSI_ANT_OFDM2_THR 0x000000FF
#define AGC_RSSI_ANT_OFDM2_THR_S 16
#define AGC_RSSI_ANT_CCK_THR 0x000000FF
#define AGC_RSSI_ANT_CCK_THR_S 8
#define AGC_RSSI_ANT_OFDM_THR 0x000000FF
#define AGC_RSSI_ANT_OFDM_THR_S 0

#define AGC11B_CTRL3_REG (REG_AGC_BASE + 0x0124)
#define AGC_RSSI_2ND_11B_THR 0x000000FF
#define AGC_RSSI_2ND_11B_THR_S 24
#define AGC_BCORR_SNR_THR_STRONG 0x000000FF
#define AGC_BCORR_SNR_THR_STRONG_S 16
#define AGC_BCORR_PWR_1S_THR 0x0000003F
#define AGC_BCORR_PWR_1S_THR_S 10
#define AGC_BCORR_PWR_THR_STRONG 0x0000003F
#define AGC_BCORR_PWR_THR_STRONG_S 4
#define AGC_BCORR_LT_EXT_CNT 0x0000000F
#define AGC_BCORR_LT_EXT_CNT_S 0

#define AGCPWR_CTRL20_REG (REG_AGC_BASE + 0x0128)
#define AGC_AGV_NOISE_FSDB_MIN 0x000000FF
#define AGC_AGV_NOISE_FSDB_MIN_S 24
#define AGC_R_CAL_COUNT 0x00000FFF
#define AGC_R_CAL_COUNT_S 12
#define AGC_R_RSSI_MIN 0x00000FFF
#define AGC_R_RSSI_MIN_S 0

#define AGCPWR_CTRL21_REG (REG_AGC_BASE + 0x012c)
#define AGC_NOISE_HOLD (BIT(25))
#define AGC_NOISE_HOLD_S 25
#define AGC_NOISE_LOAD (BIT(24))
#define AGC_NOISE_LOAD_S 24
#define AGC_CAL_COUNT_LOAD 0x00000FFF
#define AGC_CAL_COUNT_LOAD_S 12
#define AGC_RSSI_MIN_LOAD 0x00000FFF
#define AGC_RSSI_MIN_LOAD_S 0

#define AGCPWR_CTRL22_REG (REG_AGC_BASE + 0x0130)
#define AGC_RC_FILTER_NOISE_EN (BIT(26))
#define AGC_RC_FILTER_NOISE_EN_S 26
#define AGC_LOAD_NOISE_RC_INIT (BIT(24))
#define AGC_LOAD_NOISE_RC_INIT_S 24
#define AGC_NOISE_RC_INIT 0x00000FFF
#define AGC_NOISE_RC_INIT_S 0

#define AGCPWR_CTRL23_REG (REG_AGC_BASE + 0x0134)
#define AGC_RC_SHIFT_MAX 0x00000007
#define AGC_RC_SHIFT_MAX_S 24
#define AGC_NOISE_RC_IN_MIN 0x00000FFF
#define AGC_NOISE_RC_IN_MIN_S 12
#define AGC_NOISE_RC_IN_MAX 0x00000FFF
#define AGC_NOISE_RC_IN_MAX_S 0

#define AGCPWR_CTRL24_REG (REG_AGC_BASE + 0x0138)
#define AGC_NOISE_RC_OUT 0x00000FFF
#define AGC_NOISE_RC_OUT_S 12

#define AGCPWR_CTRL25_REG (REG_AGC_BASE + 0x013c)
#define AGC_MAX_GAIN_SCH 0x0000007F
#define AGC_MAX_GAIN_SCH_S 18
#define AGC_PWR_FE_HIGH_FIND_THR 0x000001FF
#define AGC_PWR_FE_HIGH_FIND_THR_S 9
#define AGC_PWR_HIGH_FIND_THR 0x000001FF
#define AGC_PWR_HIGH_FIND_THR_S 0

#define AGCPWR_CTRL26_REG (REG_AGC_BASE + 0x0140)
#define AGC_RST_PWRTRK_WIN (BIT(26))
#define AGC_RST_PWRTRK_WIN_S 26
#define AGC_RESTART_PWR_COARSE 0x000001FF
#define AGC_RESTART_PWR_COARSE_S 17
#define AGC_PWR_ANT_DELTA_THR 0x000000FF
#define AGC_PWR_ANT_DELTA_THR_S 9
#define AGC_PWR_ANT_SW 0x000001FF
#define AGC_PWR_ANT_SW_S 0

#define AGCBT_CTRL4_REG (REG_AGC_BASE + 0x0144)
#define AGC_PWR_FINE_2ND_OFS_BT_LT 0x0000003F
#define AGC_PWR_FINE_2ND_OFS_BT_LT_S 18
#define AGC_PWR_FINE_1ST_LE_LT 0x000001FF
#define AGC_PWR_FINE_1ST_LE_LT_S 9
#define AGC_PWR_FINE_1ST_BT_LT 0x000001FF
#define AGC_PWR_FINE_1ST_BT_LT_S 0

#define AGCBT_CTRL5_REG (REG_AGC_BASE + 0x0148)
#define AGC_PWR_LE_CODED_THR 0x000000FF
#define AGC_PWR_LE_CODED_THR_S 16
#define AGC_PWR_LE_THR 0x000000FF
#define AGC_PWR_LE_THR_S 8
#define AGC_PWR_BT_THR 0x000000FF
#define AGC_PWR_BT_THR_S 0

#define AGCFINEGAIN_CTRL_REG (REG_AGC_BASE + 0x014c)
#define AGC_RSSI_ANT_OFDM_LOW_THR 0x000000FF
#define AGC_RSSI_ANT_OFDM_LOW_THR_S 17
#define AGC_FINE_GAIN_OFFSET 0x000001FF
#define AGC_FINE_GAIN_OFFSET_S 8
#define AGC_FINE_RSSI_THR 0x000000FF
#define AGC_FINE_RSSI_THR_S 0

#define AGCRESTART_CTRL_REG (REG_AGC_BASE + 0x0150)
#define AGC_PWR_FINE_LATCH_THR 0x000001FF
#define AGC_PWR_FINE_LATCH_THR_S 20
#define AGC_REST_CNT_END 0x000000FF
#define AGC_REST_CNT_END_S 12
#define AGC_REST_QKDET_EN (BIT(11))
#define AGC_REST_QKDET_EN_S 11
#define AGC_CORR_DET_CNT_MAX_REST 0x0000003F
#define AGC_CORR_DET_CNT_MAX_REST_S 5
#define AGC_CORR_DET_THR_REST 0x0000001F
#define AGC_CORR_DET_THR_REST_S 0

#define AGCFSM_CTRL6_REG (REG_AGC_BASE + 0x0154)
#define AGC_RSSI_LATCH_SEL (BIT(30))
#define AGC_RSSI_LATCH_SEL_S 30
#define AGC_PWR_ERR_LT_GAIN_SEL (BIT(29))
#define AGC_PWR_ERR_LT_GAIN_SEL_S 29
#define AGC_PWR_ERR_LT_COARSE 0x000001FF
#define AGC_PWR_ERR_LT_COARSE_S 20
#define AGC_MIN_GAIN_EXT 0x0000007F
#define AGC_MIN_GAIN_EXT_S 13
#define AGC_PWR_HIGH_THR_ADD 0x000001FF
#define AGC_PWR_HIGH_THR_ADD_S 4
#define AGC_INIT_WCNT 0x0000000F
#define AGC_INIT_WCNT_S 0

#define AGCFSM_CTRL7_REG (REG_AGC_BASE + 0x0158)
#define AGC_ST_WAIT_EXIT_EN 0x00000003
#define AGC_ST_WAIT_EXIT_EN_S 7
#define AGC_ADC_VALID_TIME 0x0000007F
#define AGC_ADC_VALID_TIME_S 0

#define AGCPWR_CTRL27_REG (REG_AGC_BASE + 0x01a0)
#define AGC_LE_CODED_RSSI_THR 0x000000FF
#define AGC_LE_CODED_RSSI_THR_S 21
#define AGC_LE_CODED_RXPWR_VAR_THR 0x0000000F
#define AGC_LE_CODED_RXPWR_VAR_THR_S 17
#define AGC_PWR_FINE_RECORRECT_THR_LE_CODED 0x0000001F
#define AGC_PWR_FINE_RECORRECT_THR_LE_CODED_S 12
#define AGC_PWR_DROP_THR_LE_CODED 0x0000003F
#define AGC_PWR_DROP_THR_LE_CODED_S 6
#define AGC_PWR_RESTART_THR_LE_CODED 0x0000003F
#define AGC_PWR_RESTART_THR_LE_CODED_S 0

#define AGCBT_CTRL6_REG (REG_AGC_BASE + 0x01a4)
#define AGC_FLAG_PWR_OK_EN_BT (BIT(18))
#define AGC_FLAG_PWR_OK_EN_BT_S 18
#define AGC_PWR_FINE_1ST_LE_CODED_LT 0x000001FF
#define AGC_PWR_FINE_1ST_LE_CODED_LT_S 9
#define AGC_PWR_FINE_1ST_LE_CODED 0x000001FF
#define AGC_PWR_FINE_1ST_LE_CODED_S 0

#define AGCBT_CTRL7_REG (REG_AGC_BASE + 0x01a8)
#define AGC_ADCSAT_RSTA_THR_BT 0x0000003F
#define AGC_ADCSAT_RSTA_THR_BT_S 26
#define AGC_ADC_SAT2_EN_BT (BIT(25))
#define AGC_ADC_SAT2_EN_BT_S 25
#define AGC_ADCSAT_SUM_THR2_BT 0x0000001F
#define AGC_ADCSAT_SUM_THR2_BT_S 20
#define AGC_ADCSAT_SUM_THR_BT 0x0000003F
#define AGC_ADCSAT_SUM_THR_BT_S 14
#define AGC_ADCSAT_COUNT_MAX_BT 0x0000001F
#define AGC_ADCSAT_COUNT_MAX_BT_S 9
#define AGC_ADCSAT_THR_BT 0x000001FF
#define AGC_ADCSAT_THR_BT_S 0

#define AGCNOUSE_REG (REG_AGC_BASE + 0x03fc)
#define AGC_DATE 0x0FFFFFFF
#define AGC_DATE_S 0
#define AGC_DATE_VERSION 0x1904270
