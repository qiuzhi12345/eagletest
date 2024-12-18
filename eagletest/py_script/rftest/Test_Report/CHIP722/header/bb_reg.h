
#define BB_CTRL0_REG (REG_BB_BASE + 0x0000)
#define BB_FFT_CLK_OPT 0x00000003
#define BB_FFT_CLK_OPT_S 21
#define BB_DAC_ON_WAIT 0x000003FF
#define BB_DAC_ON_WAIT_S 11
#define BB_MAC_INF_PATH (BIT(10))
#define BB_MAC_INF_PATH_S 10
#define BB_FPGA_HT2040_INS0 (BIT(9))
#define BB_FPGA_HT2040_INS0_S 9
#define BB_RXCOV_FORCE_CLK (BIT(8))
#define BB_RXCOV_FORCE_CLK_S 8
#define BB_RXCOV_HT40_FORCE_CLK (BIT(7))
#define BB_RXCOV_HT40_FORCE_CLK_S 7
#define BB_HT20_CEN_BCOV_EN (BIT(6))
#define BB_HT20_CEN_BCOV_EN_S 6
#define BB_TX_TOP_CLK_FORCE_ON 0x00000007
#define BB_TX_TOP_CLK_FORCE_ON_S 3
#define BB_FFT_OUT_FORCE_CLK (BIT(2))
#define BB_FFT_OUT_FORCE_CLK_S 2
#define BB_FFT_FORCE_CLK (BIT(1))
#define BB_FFT_FORCE_CLK_S 1
#define BB_HT40_BCOV_EN (BIT(0))
#define BB_HT40_BCOV_EN_S 0

#define BB_DIAG0_REG (REG_BB_BASE + 0x0004)
#define BB_DIAG_HUNG_INT (BIT(31))
#define BB_DIAG_HUNG_INT_S 31
#define BB_DIAG_MODE_SEL (BIT(30))
#define BB_DIAG_MODE_SEL_S 30
#define BB_DIAG_HUNG_INT_CLR (BIT(29))
#define BB_DIAG_HUNG_INT_CLR_S 29
#define BB_DIAG_HUNG_INT_EN (BIT(28))
#define BB_DIAG_HUNG_INT_EN_S 28
#define BB_DIAG_HUNG_CNT 0x0000FFFF
#define BB_DIAG_HUNG_CNT_S 12
#define BB_DIAG_ST 0x0000000F
#define BB_DIAG_ST_S 8
#define BB_DIAG_SEL_1 0x0000000F
#define BB_DIAG_SEL_1_S 4
#define BB_DIAG_SEL_0 0x0000000F
#define BB_DIAG_SEL_0_S 0

#define BB_NRXRD1_REG (REG_BB_BASE + 0x0008)
#define BB_STATUS 0xFFFFFFFF
#define BB_STATUS_S 0

#define BB_DC_CTRL_0_REG (REG_BB_BASE + 0x000c)
#define BB_DC_SHIFT_FIND_MAX 0x00000007
#define BB_DC_SHIFT_FIND_MAX_S 17
#define BB_DC_CNT_INIT 0x0000000F
#define BB_DC_CNT_INIT_S 13
#define BB_DC_SHIFT_MAX 0x00000007
#define BB_DC_SHIFT_MAX_S 10
#define BB_DC_RM_EN (BIT(9))
#define BB_DC_RM_EN_S 9
#define BB_DC_MAX 0x000001FF
#define BB_DC_MAX_S 0

#define BB_TONE_CTRL_0_REG (REG_BB_BASE + 0x0010)
#define BB_FFT_HTLTF_STOP_EN (BIT(31))
#define BB_FFT_HTLTF_STOP_EN_S 31
#define BB_FFT_TONE_GAIN_THR 0x0000007F
#define BB_FFT_TONE_GAIN_THR_S 24
#define BB_PHI_TONE_GAIN_THR 0x0000007F
#define BB_PHI_TONE_GAIN_THR_S 17
#define BB_AGC_TONE_GAIN_THR 0x0000007F
#define BB_AGC_TONE_GAIN_THR_S 10
#define BB_FFT_DC_RM_EN (BIT(9))
#define BB_FFT_DC_RM_EN_S 9
#define BB_FFT_TONE_RM_EN (BIT(8))
#define BB_FFT_TONE_RM_EN_S 8
#define BB_TONE_MAX 0x000000FF
#define BB_TONE_MAX_S 0

#define BB_TONE_CTRL_1_REG (REG_BB_BASE + 0x0014)
#define BB_TONE_SHIFT_MAX_1_HT20_DELTA (BIT(31))
#define BB_TONE_SHIFT_MAX_1_HT20_DELTA_S 31
#define BB_TONE_SHIFT_MAX_1_FFT 0x00000007
#define BB_TONE_SHIFT_MAX_1_FFT_S 28
#define BB_TONE_SHIFT_MAX_1_PHI 0x00000007
#define BB_TONE_SHIFT_MAX_1_PHI_S 25
#define BB_TONE_SHIFT_MAX_1_AGC 0x00000007
#define BB_TONE_SHIFT_MAX_1_AGC_S 22
#define BB_TONE_FFT_THR_1 0x000000FF
#define BB_TONE_FFT_THR_1_S 14
#define BB_TONE_RM_EN_1 (BIT(13))
#define BB_TONE_RM_EN_1_S 13
#define BB_TONE_EST_COEF_1 0x00001FFF
#define BB_TONE_EST_COEF_1_S 0

#define BB_TONE_CTRL_2_REG (REG_BB_BASE + 0x0018)
#define BB_TONE_SHIFT_MAX_2_HT20_DELTA (BIT(31))
#define BB_TONE_SHIFT_MAX_2_HT20_DELTA_S 31
#define BB_TONE_SHIFT_MAX_2_FFT 0x00000007
#define BB_TONE_SHIFT_MAX_2_FFT_S 28
#define BB_TONE_SHIFT_MAX_2_PHI 0x00000007
#define BB_TONE_SHIFT_MAX_2_PHI_S 25
#define BB_TONE_SHIFT_MAX_2_AGC 0x00000007
#define BB_TONE_SHIFT_MAX_2_AGC_S 22
#define BB_TONE_FFT_THR_2 0x000000FF
#define BB_TONE_FFT_THR_2_S 14
#define BB_TONE_RM_EN_2 (BIT(13))
#define BB_TONE_RM_EN_2_S 13
#define BB_TONE_EST_COEF_2 0x00001FFF
#define BB_TONE_EST_COEF_2_S 0

#define BB_TONE_CTRL_3_REG (REG_BB_BASE + 0x001c)
#define BB_TONE_SHIFT_MAX_3_HT20_DELTA (BIT(31))
#define BB_TONE_SHIFT_MAX_3_HT20_DELTA_S 31
#define BB_TONE_SHIFT_MAX_3_FFT 0x00000007
#define BB_TONE_SHIFT_MAX_3_FFT_S 28
#define BB_TONE_SHIFT_MAX_3_PHI 0x00000007
#define BB_TONE_SHIFT_MAX_3_PHI_S 25
#define BB_TONE_SHIFT_MAX_3_AGC 0x00000007
#define BB_TONE_SHIFT_MAX_3_AGC_S 22
#define BB_TONE_FFT_THR_3 0x000000FF
#define BB_TONE_FFT_THR_3_S 14
#define BB_TONE_RM_EN_3 (BIT(13))
#define BB_TONE_RM_EN_3_S 13
#define BB_TONE_EST_COEF_3 0x00001FFF
#define BB_TONE_EST_COEF_3_S 0

#define BB_TONE_CTRL_4_REG (REG_BB_BASE + 0x0020)
#define BB_TONE_SHIFT_MAX_4_HT20_DELTA (BIT(31))
#define BB_TONE_SHIFT_MAX_4_HT20_DELTA_S 31
#define BB_TONE_SHIFT_MAX_4_FFT 0x00000007
#define BB_TONE_SHIFT_MAX_4_FFT_S 28
#define BB_TONE_SHIFT_MAX_4_PHI 0x00000007
#define BB_TONE_SHIFT_MAX_4_PHI_S 25
#define BB_TONE_SHIFT_MAX_4_AGC 0x00000007
#define BB_TONE_SHIFT_MAX_4_AGC_S 22
#define BB_TONE_FFT_THR_4 0x000000FF
#define BB_TONE_FFT_THR_4_S 14
#define BB_TONE_RM_EN_4 (BIT(13))
#define BB_TONE_RM_EN_4_S 13
#define BB_TONE_EST_COEF_4 0x00001FFF
#define BB_TONE_EST_COEF_4_S 0

#define BB_TONE_CTRL_5_REG (REG_BB_BASE + 0x0024)
#define BB_DC_USE_08US 0x00000003
#define BB_DC_USE_08US_S 24
#define BB_USE_DC_COARSE_EN (BIT(23))
#define BB_USE_DC_COARSE_EN_S 23
#define BB_USE_DC_FINE_EN (BIT(22))
#define BB_USE_DC_FINE_EN_S 22
#define BB_TONE_SWAP_EN (BIT(21))
#define BB_TONE_SWAP_EN_S 21
#define BB_TONE_FFT_LATCH (BIT(20))
#define BB_TONE_FFT_LATCH_S 20
#define BB_TONE_SYM_WAIT 0x0000000F
#define BB_TONE_SYM_WAIT_S 16
#define BB_TONE_SYM_WAIT_11N2ND 0x0000000F
#define BB_TONE_SYM_WAIT_11N2ND_S 12
#define BB_TONE_SYM_WAIT_EN (BIT(11))
#define BB_TONE_SYM_WAIT_EN_S 11
#define BB_11N_2ND_DIS_DC (BIT(10))
#define BB_11N_2ND_DIS_DC_S 10
#define BB_11N_2ND_DIS_TONE (BIT(9))
#define BB_11N_2ND_DIS_TONE_S 9
#define BB_TONE_CNT_INIT_EN (BIT(8))
#define BB_TONE_CNT_INIT_EN_S 8
#define BB_TONE_CNT_INIT 0x0000000F
#define BB_TONE_CNT_INIT_S 4
#define BB_TONE_CNT_INIT_HT20 0x0000000F
#define BB_TONE_CNT_INIT_HT20_S 0

#define BB_RESET_REG (REG_BB_BASE + 0x0028)
#define BBCLK_EN (BIT(15))
#define BBCLK_EN_S 15
#define BB_TEST8_RST (BIT(14))
#define BB_TEST8_RST_S 14
#define BB_TEST7_RST (BIT(13))
#define BB_TEST7_RST_S 13
#define BB_TEST6_RST (BIT(12))
#define BB_TEST6_RST_S 12
#define BB_TEST5_RST (BIT(11))
#define BB_TEST5_RST_S 11
#define BB_TEST4_RST (BIT(10))
#define BB_TEST4_RST_S 10
#define BB_TEST3_RST (BIT(9))
#define BB_TEST3_RST_S 9
#define BB_TEST2_RST (BIT(8))
#define BB_TEST2_RST_S 8
#define BB_TEST1_RST (BIT(7))
#define BB_TEST1_RST_S 7
#define BB_TEST0_RST (BIT(6))
#define BB_TEST0_RST_S 6
#define BB_BRX_RST (BIT(5))
#define BB_BRX_RST_S 5
#define BB_AGC_RST (BIT(4))
#define BB_AGC_RST_S 4
#define BB_TX_RST (BIT(3))
#define BB_TX_RST_S 3
#define BB_NRX_RST (BIT(2))
#define BB_NRX_RST_S 2
#define BB_FSM_RST (BIT(1))
#define BB_FSM_RST_S 1
#define BB_FFT_RST (BIT(0))
#define BB_FFT_RST_S 0

#define BB_TONE_CTRL_6_REG (REG_BB_BASE + 0x002c)
#define BB_TONE_EST_FB_EN_4 (BIT(26))
#define BB_TONE_EST_FB_EN_4_S 26
#define BB_TONE_EST_FB_OUT_EN_4 (BIT(25))
#define BB_TONE_EST_FB_OUT_EN_4_S 25
#define BB_TONE_EST_FB_EN_3 (BIT(24))
#define BB_TONE_EST_FB_EN_3_S 24
#define BB_TONE_EST_FB_OUT_EN_3 (BIT(23))
#define BB_TONE_EST_FB_OUT_EN_3_S 23
#define BB_TONE_EST_FB_EN_2 (BIT(22))
#define BB_TONE_EST_FB_EN_2_S 22
#define BB_TONE_EST_FB_OUT_EN_2 (BIT(21))
#define BB_TONE_EST_FB_OUT_EN_2_S 21
#define BB_TONE_EST_FB_EN_1 (BIT(20))
#define BB_TONE_EST_FB_EN_1_S 20
#define BB_TONE_EST_FB_OUT_EN_1 (BIT(19))
#define BB_TONE_EST_FB_OUT_EN_1_S 19
#define BB_TONE_EST_COEF_4_LSB 0x00000007
#define BB_TONE_EST_COEF_4_LSB_S 16
#define BB_TONE_EST_COEF_3_LSB 0x00000007
#define BB_TONE_EST_COEF_3_LSB_S 13
#define BB_TONE_EST_COEF_2_LSB 0x00000007
#define BB_TONE_EST_COEF_2_LSB_S 10
#define BB_TONE_EST_COEF_1_LSB 0x00000007
#define BB_TONE_EST_COEF_1_LSB_S 7
#define BB_DEMOD_TONE_GAIN_THR 0x0000007F
#define BB_DEMOD_TONE_GAIN_THR_S 0

#define BB_FSM_CTRL_REG (REG_BB_BASE + 0x0030)
#define BB_AGC_ERR_EXIT_EN (BIT(10))
#define BB_AGC_ERR_EXIT_EN_S 10
#define BB_TX_WAIT_DELAY 0x000003FF
#define BB_TX_WAIT_DELAY_S 0

#define BB_DCDELTACONF0_REG (REG_BB_BASE + 0x0034)
#define BB_DC_EST_CLK_FORCE (BIT(24))
#define BB_DC_EST_CLK_FORCE_S 24
#define BB_DC_EST_SEL 0x00000003
#define BB_DC_EST_SEL_S 22
#define BB_DC_CORR_CLK_SEL 0x00000003
#define BB_DC_CORR_CLK_SEL_S 20
#define BB_DC_DELAY_CNT 0x00000FFF
#define BB_DC_DELAY_CNT_S 8
#define BB_DC_CORR_DELAY_CYCLE 0x000000FF
#define BB_DC_CORR_DELAY_CYCLE_S 0

#define BB_DCDELTACONF1_REG (REG_BB_BASE + 0x0038)
#define BB_DC_EST_CORR_EN_FORCE (BIT(27))
#define BB_DC_EST_CORR_EN_FORCE_S 27
#define BB_DC_EST_CORR_EN (BIT(26))
#define BB_DC_EST_CORR_EN_S 26
#define BB_PHI_DELTA_EST_DONE (BIT(25))
#define BB_PHI_DELTA_EST_DONE_S 25
#define BB_PHI_DELTA_EST 0x00001FFF
#define BB_PHI_DELTA_EST_S 12
#define BB_DC_EST_CORR_LEN 0x00000FFF
#define BB_DC_EST_CORR_LEN_S 0

#define BB_WDG_0_REG (REG_BB_BASE + 0x003c)
#define BB_WDG_BUSY_CHK (BIT(31))
#define BB_WDG_BUSY_CHK_S 31
#define BB_WDG_SRCH_CHK (BIT(30))
#define BB_WDG_SRCH_CHK_S 30
#define BB_WDG_MAX_BUSY 0x00003FFF
#define BB_WDG_MAX_BUSY_S 16
#define BB_WDG_MAX_SRCH 0x0000FFFF
#define BB_WDG_MAX_SRCH_S 0

#define BB_WDG_1_REG (REG_BB_BASE + 0x0040)
#define BB_WDG_RST_EN (BIT(31))
#define BB_WDG_RST_EN_S 31
#define BB_WDG_INT_EN (BIT(30))
#define BB_WDG_INT_EN_S 30
#define BB_WDG_CLR (BIT(29))
#define BB_WDG_CLR_S 29
#define BB_R_BB_WDG_FLAG (BIT(28))
#define BB_R_BB_WDG_FLAG_S 28
#define BB_R_BB_WDG_STATUS 0x0FFFFFFF
#define BB_R_BB_WDG_STATUS_S 0

#define BB_INT_ENA_REG (REG_BB_BASE + 0x0044)
#define BB_TIMER_INT_ENA (BIT(2))
#define BB_TIMER_INT_ENA_S 2
#define BB_DC_INT_ENA (BIT(1))
#define BB_DC_INT_ENA_S 1
#define BB_NOISE_INT_ENA (BIT(0))
#define BB_NOISE_INT_ENA_S 0

#define BB_INT_RAW_REG (REG_BB_BASE + 0x0048)
#define BB_TIMER_INT_RAW (BIT(2))
#define BB_TIMER_INT_RAW_S 2
#define BB_DC_INT_RAW (BIT(1))
#define BB_DC_INT_RAW_S 1
#define BB_NOISE_INT_RAW (BIT(0))
#define BB_NOISE_INT_RAW_S 0

#define BB_INT_ST_REG (REG_BB_BASE + 0x004c)
#define BB_TIMER_INT_ST (BIT(2))
#define BB_TIMER_INT_ST_S 2
#define BB_DC_INT_ST (BIT(1))
#define BB_DC_INT_ST_S 1
#define BB_NOISE_INT_ST (BIT(0))
#define BB_NOISE_INT_ST_S 0

#define BB_INT_CLR_REG (REG_BB_BASE + 0x0050)
#define BB_TIMER_INT_CLR (BIT(2))
#define BB_TIMER_INT_CLR_S 2
#define BB_DC_INT_CLR (BIT(1))
#define BB_DC_INT_CLR_S 1
#define BB_NOISE_INT_CLR (BIT(0))
#define BB_NOISE_INT_CLR_S 0

#define BBPD_CTRL_REG (REG_BB_BASE + 0x0054)
#define BB_FFT_FORCE_PU (BIT(3))
#define BB_FFT_FORCE_PU_S 3
#define BB_FFT_FORCE_PD (BIT(2))
#define BB_FFT_FORCE_PD_S 2
#define BB_DC_EST_FORCE_PU (BIT(1))
#define BB_DC_EST_FORCE_PU_S 1
#define BB_DC_EST_FORCE_PD (BIT(0))
#define BB_DC_EST_FORCE_PD_S 0

#define BB_CCA_CTRL_0_REG (REG_BB_BASE + 0x0058)
#define BB_CCA_CNT_PRI_CAR (BIT(31))
#define BB_CCA_CNT_PRI_CAR_S 31
#define BB_CCA_CNT_SEC_CAR (BIT(30))
#define BB_CCA_CNT_SEC_CAR_S 30
#define BB_CCA_CNT_TXRX (BIT(29))
#define BB_CCA_CNT_TXRX_S 29
#define BB_CCA_TIMER_CLR (BIT(28))
#define BB_CCA_TIMER_CLR_S 28
#define BB_TIMER_CLR (BIT(27))
#define BB_TIMER_CLR_S 27
#define BB_TIMER_MAX 0x07FFFFFF
#define BB_TIMER_MAX_S 0

#define BB_CCA_CTRL_1_REG (REG_BB_BASE + 0x005c)
#define BB_TIMER_DONE (BIT(27))
#define BB_TIMER_DONE_S 27
#define BB_TIMER 0x07FFFFFF
#define BB_TIMER_S 0

#define BB_CCA_CTRL_2_REG (REG_BB_BASE + 0x0060)
#define BB_CCA_CNT 0x07FFFFFF
#define BB_CCA_CNT_S 0

#define BB_CCA_CTRL_3_REG (REG_BB_BASE + 0x0064)
#define BB_CCA_SEC_CNT 0x07FFFFFF
#define BB_CCA_SEC_CNT_S 0

#define BB_NRXFDM_WDG_REG (REG_BB_BASE + 0x0068)
#define BB_FDM_WDG_INT (BIT(28))
#define BB_FDM_WDG_INT_S 28
#define BB_FDM_WDG_INT_CNT 0x00000FFF
#define BB_FDM_WDG_INT_CNT_S 16
#define BB_FDM_WDG_INT_EN (BIT(15))
#define BB_FDM_WDG_INT_EN_S 15
#define BB_FDM_WDG_INT_CNT_CLR (BIT(14))
#define BB_FDM_WDG_INT_CNT_CLR_S 14
#define BB_FDM_WDG_CLR (BIT(13))
#define BB_FDM_WDG_CLR_S 13
#define BB_FDM_WDG_RST_EN (BIT(12))
#define BB_FDM_WDG_RST_EN_S 12
#define BB_FDM_WDG_EN (BIT(11))
#define BB_FDM_WDG_EN_S 11
#define BB_FDM_WDG_CNT 0x000007FF
#define BB_FDM_WDG_CNT_S 0

#define BB_CTRL1_REG (REG_BB_BASE + 0x006c)
#define BB_BTX_START_WAIT 0x000003FF
#define BB_BTX_START_WAIT_S 20
#define BB_NTX_HT2040_START_WAIT 0x000003FF
#define BB_NTX_HT2040_START_WAIT_S 10
#define BB_NTX_START_WAIT 0x000003FF
#define BB_NTX_START_WAIT_S 0

#define BB_DC_RM_CONF0_REG (REG_BB_BASE + 0x0070)
#define BB_USE_STF_DC_CALC_FO_MIN_THR 0x000000FF
#define BB_USE_STF_DC_CALC_FO_MIN_THR_S 24
#define BB_USE_STF_DC_CALC_SNR_MIN_THR 0x000000FF
#define BB_USE_STF_DC_CALC_SNR_MIN_THR_S 16
#define BB_USE_STF_DC_1P6SUM_SNR_MIN_THR 0x000000FF
#define BB_USE_STF_DC_1P6SUM_SNR_MIN_THR_S 8
#define BB_USE_STF_DC_1P6SUM_FO_MAX_THR 0x000000FF
#define BB_USE_STF_DC_1P6SUM_FO_MAX_THR_S 0

#define BB_DC_RM_CONF1_REG (REG_BB_BASE + 0x0074)
#define BB_USE_DC_HTSTF_EN (BIT(9))
#define BB_USE_DC_HTSTF_EN_S 9
#define BB_USE_DC_COARSE_CALC_EN (BIT(8))
#define BB_USE_DC_COARSE_CALC_EN_S 8
#define BB_USE_LTF_DC_EST_FO_MAX_THR 0x000000FF
#define BB_USE_LTF_DC_EST_FO_MAX_THR_S 0

#define BB_DC_CTRL1_REG (REG_BB_BASE + 0x0078)
#define BB_LOOP_CNT_MIN_SHIFT4 0x000000FF
#define BB_LOOP_CNT_MIN_SHIFT4_S 24
#define BB_LOOP_CNT_MIN_SHIFT3 0x000000FF
#define BB_LOOP_CNT_MIN_SHIFT3_S 16
#define BB_LOOP_CNT_MIN_SHIFT2 0x000000FF
#define BB_LOOP_CNT_MIN_SHIFT2_S 8
#define BB_LOOP_CNT_MIN_SHIFT1 0x000000FF
#define BB_LOOP_CNT_MIN_SHIFT1_S 0

#define BB_DC_CTRL2_REG (REG_BB_BASE + 0x007c)
#define BB_LOOP_CNT_MIN_SHIFT7 0x000000FF
#define BB_LOOP_CNT_MIN_SHIFT7_S 16
#define BB_LOOP_CNT_MIN_SHIFT6 0x000000FF
#define BB_LOOP_CNT_MIN_SHIFT6_S 8
#define BB_LOOP_CNT_MIN_SHIFT5 0x000000FF
#define BB_LOOP_CNT_MIN_SHIFT5_S 0

#define BB_CLK_CONF_REG (REG_BB_BASE + 0x0080)
#define BB_CLK80X_EN_FORCE_ON (BIT(1))
#define BB_CLK80X_EN_FORCE_ON_S 1
#define BB_CLK40X_EN_FORCE_ON (BIT(0))
#define BB_CLK40X_EN_FORCE_ON_S 0

#define BB_STATE_CNT_CONF0_REG (REG_BB_BASE + 0x0084)
#define BB_CNT_RX_ERR_RESTART_TAR 0x000003FF
#define BB_CNT_RX_ERR_RESTART_TAR_S 20
#define BB_CNT_AGC_RESET_TAR 0x000003FF
#define BB_CNT_AGC_RESET_TAR_S 10
#define BB_CNT_TX_TAR 0x000003FF
#define BB_CNT_TX_TAR_S 0

#define BB_STATE_CNT_CONF1_REG (REG_BB_BASE + 0x0088)
#define BB_CNT_RX_EN_TAR 0x000003FF
#define BB_CNT_RX_EN_TAR_S 10
#define BB_CNT_RIFS_TAR 0x000003FF
#define BB_CNT_RIFS_TAR_S 0

#define BB_NOUSE_REG (REG_BB_BASE + 0x03FC)
#define BB_DATE 0x0FFFFFFF
#define BB_DATE_S 0
#define BB_DATE_VERSION 0x1809260
