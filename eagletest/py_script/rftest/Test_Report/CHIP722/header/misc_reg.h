
#define MISC_BITS_MISC_CTRL0_REG (REG_MISC_BASE + 0x0000)
#define MISC_BITS_MISC_CTRL0 0xFFFFFFFF
#define MISC_BITS_MISC_CTRL0_S 0

#define MISC_BITS_MISC_CTRL1_REG (REG_MISC_BASE + 0x0004)
#define MISC_BITS_MISC_CTRL1 0xFFFFFFFF
#define MISC_BITS_MISC_CTRL1_S 0

#define MISC_BITS_MISC_DATA0_REG (REG_MISC_BASE + 0x0008)
#define MISC_BITS_MISC_DATA0 0xFFFFFFFF
#define MISC_BITS_MISC_DATA0_S 0

#define MISC_BITS_MISC_CTRL2_REG (REG_MISC_BASE + 0x000c)
#define MISC_BITS_IQEST_CLK_FORCE_EN (BIT(30))
#define MISC_BITS_IQEST_CLK_FORCE_EN_S 30
#define MISC_BITS_MISCCLK_EN (BIT(29))
#define MISC_BITS_MISCCLK_EN_S 29
#define MISC_BITS_CMD_3WIRE_IN_LVDS (BIT(27))
#define MISC_BITS_CMD_3WIRE_IN_LVDS_S 27
#define MISC_BITS_CMD_STOP (BIT(26))
#define MISC_BITS_CMD_STOP_S 26
#define MISC_BITS_I2C_2WIRE_MODE (BIT(25))
#define MISC_BITS_I2C_2WIRE_MODE_S 25
#define MISC_BITS_CMD_3WIRE_MODE (BIT(24))
#define MISC_BITS_CMD_3WIRE_MODE_S 24
#define MISC_BITS_MUX_HALF_RATE (BIT(23))
#define MISC_BITS_MUX_HALF_RATE_S 23
#define MISC_BITS_APB_SW_MODE (BIT(18))
#define MISC_BITS_APB_SW_MODE_S 18
#define MISC_BITS_HOST_APB_ANA_DIG_EN (BIT(10))
#define MISC_BITS_HOST_APB_ANA_DIG_EN_S 10
#define MISC_BITS_HOST_I2C_MST_EN (BIT(9))
#define MISC_BITS_HOST_I2C_MST_EN_S 9
#define MISC_BITS_FORCE_BT_MODE_OFF (BIT(8))
#define MISC_BITS_FORCE_BT_MODE_OFF_S 8
#define MISC_BITS_FORCE_BT_MODE_ON (BIT(7))
#define MISC_BITS_FORCE_BT_MODE_ON_S 7
#define MISC_BITS_LVDS_ADC_DAC_ON (BIT(6))
#define MISC_BITS_LVDS_ADC_DAC_ON_S 6
#define MISC_BITS_PK_OE (BIT(5))
#define MISC_BITS_PK_OE_S 5
#define MISC_BITS_FORCE_DAC_OFF (BIT(4))
#define MISC_BITS_FORCE_DAC_OFF_S 4
#define MISC_BITS_FORCE_ADC_OFF (BIT(3))
#define MISC_BITS_FORCE_ADC_OFF_S 3
#define MISC_BITS_FORCE_DAC_ON (BIT(2))
#define MISC_BITS_FORCE_DAC_ON_S 2
#define MISC_BITS_FORCE_ADC_ON (BIT(1))
#define MISC_BITS_FORCE_ADC_ON_S 1
#define MISC_BITS_FORCE_APB_ON (BIT(0))
#define MISC_BITS_FORCE_APB_ON_S 0

#define MISC_BITS_MISC_TRAIN_CTRL0_REG (REG_MISC_BASE + 0x0010)
#define MISC_BITS_CATCH_DONE_CNT 0x0000000F
#define MISC_BITS_CATCH_DONE_CNT_S 28
#define MISC_BITS_R_IN_CATCH_DONE (BIT(27))
#define MISC_BITS_R_IN_CATCH_DONE_S 27
#define MISC_BITS_IN_FIFO_RESET (BIT(26))
#define MISC_BITS_IN_FIFO_RESET_S 26
#define MISC_BITS_IN_FIFO_EN (BIT(25))
#define MISC_BITS_IN_FIFO_EN_S 25
#define MISC_BITS_OUT_FIFO_RESET (BIT(24))
#define MISC_BITS_OUT_FIFO_RESET_S 24
#define MISC_BITS_OUT_FIFO_EN (BIT(23))
#define MISC_BITS_OUT_FIFO_EN_S 23
#define MISC_BITS_TRAIN_RX_SEL 0x00000003
#define MISC_BITS_TRAIN_RX_SEL_S 21
#define MISC_BITS_TRAIN_RX_BIT_SEL 0x0000001F
#define MISC_BITS_TRAIN_RX_BIT_SEL_S 16
#define MISC_BITS_TRAIN_RX_G_MODE (BIT(15))
#define MISC_BITS_TRAIN_RX_G_MODE_S 15
#define MISC_BITS_TRAIN_RX_CATCH_MODE 0x00000003
#define MISC_BITS_TRAIN_RX_CATCH_MODE_S 13
#define MISC_BITS_TRAIN_RX_EN (BIT(12))
#define MISC_BITS_TRAIN_RX_EN_S 12
#define MISC_BITS_TRAIN_TX_EN (BIT(11))
#define MISC_BITS_TRAIN_TX_EN_S 11
#define MISC_BITS_TRAIN_MODE 0x00000007
#define MISC_BITS_TRAIN_MODE_S 8
#define MISC_BITS_TRAIN_TX_PAT 0x000000FF
#define MISC_BITS_TRAIN_TX_PAT_S 0

#define MISC_BITS_MISC_TRAIN_CTRL1_REG (REG_MISC_BASE + 0x0014)
#define MISC_BITS_IN_CLK_G_LOCK (BIT(30))
#define MISC_BITS_IN_CLK_G_LOCK_S 30
#define MISC_BITS_OUT_CLK_G2 0x000003FF
#define MISC_BITS_OUT_CLK_G2_S 20
#define MISC_BITS_OUT_CLK_G1 0x000003FF
#define MISC_BITS_OUT_CLK_G1_S 10
#define MISC_BITS_OUT_CLK_G0 0x000003FF
#define MISC_BITS_OUT_CLK_G0_S 0

#define MISC_BITS_MISC_TRAIN_CTRL2_REG (REG_MISC_BASE + 0x0018)
#define MISC_BITS_OUT_CLK_G5 0x000003FF
#define MISC_BITS_OUT_CLK_G5_S 20
#define MISC_BITS_OUT_CLK_G4 0x000003FF
#define MISC_BITS_OUT_CLK_G4_S 10
#define MISC_BITS_OUT_CLK_G3 0x000003FF
#define MISC_BITS_OUT_CLK_G3_S 0

#define MISC_BITS_MISC_TRAIN_CTRL3_REG (REG_MISC_BASE + 0x001c)
#define MISC_BITS_R_RX_G_DONE (BIT(30))
#define MISC_BITS_R_RX_G_DONE_S 30
#define MISC_BITS_CLK_NOG_MAX 0x000003FF
#define MISC_BITS_CLK_NOG_MAX_S 20
#define MISC_BITS_OUT_CLK_G7 0x000003FF
#define MISC_BITS_OUT_CLK_G7_S 10
#define MISC_BITS_OUT_CLK_G6 0x000003FF
#define MISC_BITS_OUT_CLK_G6_S 0

#define MISC_BITS_MISC_TRAIN_CTRL4_REG (REG_MISC_BASE + 0x0020)
#define MISC_BITS_IN_CLK_G2 0x000003FF
#define MISC_BITS_IN_CLK_G2_S 20
#define MISC_BITS_IN_CLK_G1 0x000003FF
#define MISC_BITS_IN_CLK_G1_S 10
#define MISC_BITS_IN_CLK_G0 0x000003FF
#define MISC_BITS_IN_CLK_G0_S 0

#define MISC_BITS_MISC_TRAIN_CTRL5_REG (REG_MISC_BASE + 0x0024)
#define MISC_BITS_IN_CLK_G5 0x000003FF
#define MISC_BITS_IN_CLK_G5_S 20
#define MISC_BITS_IN_CLK_G4 0x000003FF
#define MISC_BITS_IN_CLK_G4_S 10
#define MISC_BITS_IN_CLK_G3 0x000003FF
#define MISC_BITS_IN_CLK_G3_S 0

#define MISC_BITS_MISC_TRAIN_CTRL6_REG (REG_MISC_BASE + 0x0028)
#define MISC_BITS_IN_CLK_G7 0x000003FF
#define MISC_BITS_IN_CLK_G7_S 10
#define MISC_BITS_IN_CLK_G6 0x000003FF
#define MISC_BITS_IN_CLK_G6_S 0

#define MISC_BITS_TRAIN_RX_DATA_H_REG (REG_MISC_BASE + 0x002c)
#define MISC_BITS_TRAIN_RX_DATA_H 0xFFFFFFFF
#define MISC_BITS_TRAIN_RX_DATA_H_S 0

#define MISC_BITS_TRAIN_RX_DATA_L_REG (REG_MISC_BASE + 0x0030)
#define MISC_BITS_TRAIN_RX_DATA_L 0xFFFFFFFF
#define MISC_BITS_TRAIN_RX_DATA_L_S 0

#define MISC_BITS_TRAIN_RX_G_LATCH0_REG (REG_MISC_BASE + 0x0034)
#define MISC_BITS_RXG_CNT_LATCH_2 0x000003FF
#define MISC_BITS_RXG_CNT_LATCH_2_S 20
#define MISC_BITS_RXG_CNT_LATCH_1 0x000003FF
#define MISC_BITS_RXG_CNT_LATCH_1_S 10
#define MISC_BITS_RXG_CNT_LATCH_0 0x000003FF
#define MISC_BITS_RXG_CNT_LATCH_0_S 0

#define MISC_BITS_TRAIN_RX_G_LATCH1_REG (REG_MISC_BASE + 0x0038)
#define MISC_BITS_RXG_CNT_LATCH_5 0x000003FF
#define MISC_BITS_RXG_CNT_LATCH_5_S 20
#define MISC_BITS_RXG_CNT_LATCH_4 0x000003FF
#define MISC_BITS_RXG_CNT_LATCH_4_S 10
#define MISC_BITS_RXG_CNT_LATCH_3 0x000003FF
#define MISC_BITS_RXG_CNT_LATCH_3_S 0

#define MISC_BITS_TRAIN_RX_G_LATCH2_REG (REG_MISC_BASE + 0x003C)
#define MISC_BITS_RXG_CNT_LATCH_7 0x000003FF
#define MISC_BITS_RXG_CNT_LATCH_7_S 10
#define MISC_BITS_RXG_CNT_LATCH_6 0x000003FF
#define MISC_BITS_RXG_CNT_LATCH_6_S 0

#define MISC_BITS_MISC_TEST_CTRL0_REG (REG_MISC_BASE + 0x0040)
#define MISC_BITS_HOST_MUX_ST_DUMP (BIT(11))
#define MISC_BITS_HOST_MUX_ST_DUMP_S 11
#define MISC_BITS_RX_DATA_MODE (BIT(10))
#define MISC_BITS_RX_DATA_MODE_S 10
#define MISC_BITS_TX_DATA_MODE (BIT(9))
#define MISC_BITS_TX_DATA_MODE_S 9
#define MISC_BITS_SLV_TEST_5_SIM_EN (BIT(8))
#define MISC_BITS_SLV_TEST_5_SIM_EN_S 8
#define MISC_BITS_SLV_TEST_4_SIM_EN (BIT(7))
#define MISC_BITS_SLV_TEST_4_SIM_EN_S 7
#define MISC_BITS_SLV_TEST_3_SIM_EN (BIT(6))
#define MISC_BITS_SLV_TEST_3_SIM_EN_S 6
#define MISC_BITS_SLV_TEST_2_SIM_EN (BIT(5))
#define MISC_BITS_SLV_TEST_2_SIM_EN_S 5
#define MISC_BITS_SLV_TEST_1_SIM_EN (BIT(4))
#define MISC_BITS_SLV_TEST_1_SIM_EN_S 4
#define MISC_BITS_SLV_TEST_0_SIM_EN (BIT(3))
#define MISC_BITS_SLV_TEST_0_SIM_EN_S 3
#define MISC_BITS_SLV_RXCAL_SIM_EN (BIT(2))
#define MISC_BITS_SLV_RXCAL_SIM_EN_S 2
#define MISC_BITS_SLV_TXCAL_SIM_EN (BIT(1))
#define MISC_BITS_SLV_TXCAL_SIM_EN_S 1
#define MISC_BITS_GATE_SIM_EN (BIT(0))
#define MISC_BITS_GATE_SIM_EN_S 0

#define MISC_BITS_HOST_MUX_STATE_REG (REG_MISC_BASE + 0x0044)
#define MISC_BITS_DATA_MUX_STATUS 0xFFFFFFFF
#define MISC_BITS_DATA_MUX_STATUS_S 0

#define MISC_BITS_LVDS_CTRL0_REG (REG_MISC_BASE + 0x0048)
#define MISC_BITS_PHYTX_INV 0x0000000F
#define MISC_BITS_PHYTX_INV_S 28
#define MISC_BITS_PHYTX_EDGE 0x0000000F
#define MISC_BITS_PHYTX_EDGE_S 24
#define MISC_BITS_PHYTX_START (BIT(23))
#define MISC_BITS_PHYTX_START_S 23
#define MISC_BITS_PHYTX_START_CNT 0x0000001F
#define MISC_BITS_PHYTX_START_CNT_S 18
#define MISC_BITS_TEST_ERR_DISP (BIT(17))
#define MISC_BITS_TEST_ERR_DISP_S 17
#define MISC_BITS_LVDS_DIR2DIG (BIT(16))
#define MISC_BITS_LVDS_DIR2DIG_S 16
#define MISC_BITS_PHYRX_INV 0x0000000F
#define MISC_BITS_PHYRX_INV_S 12
#define MISC_BITS_PHYRX_EDGE 0x0000000F
#define MISC_BITS_PHYRX_EDGE_S 8
#define MISC_BITS_PHYRX_START (BIT(7))
#define MISC_BITS_PHYRX_START_S 7
#define MISC_BITS_PHYRX_START_CNT 0x0000001F
#define MISC_BITS_PHYRX_START_CNT_S 2
#define MISC_BITS_PHYRX_EN_CDET (BIT(1))
#define MISC_BITS_PHYRX_EN_CDET_S 1
#define MISC_BITS_PHYRX_SET_DISP (BIT(0))
#define MISC_BITS_PHYRX_SET_DISP_S 0

#define MISC_BITS_LVDS_CTRL1_REG (REG_MISC_BASE + 0x004c)
#define MISC_BITS_PHYRX_STATUS 0xFFFFFFFF
#define MISC_BITS_PHYRX_STATUS_S 0

#define MISC_BITS_LVDS_CTRL2_REG (REG_MISC_BASE + 0x0050)
#define MISC_BITS_PHYTX_MODE 0x00000007
#define MISC_BITS_PHYTX_MODE_S 27
#define MISC_BITS_PHYRX_MODE 0x00000007
#define MISC_BITS_PHYRX_MODE_S 24
#define MISC_BITS_SERDES_RX_SLEEPB (BIT(23))
#define MISC_BITS_SERDES_RX_SLEEPB_S 23
#define MISC_BITS_SERDES_XPD_TX (BIT(22))
#define MISC_BITS_SERDES_XPD_TX_S 22
#define MISC_BITS_SERDES_XPD_TX_BIAS (BIT(21))
#define MISC_BITS_SERDES_XPD_TX_BIAS_S 21
#define MISC_BITS_SERDES_XPD_PLL (BIT(20))
#define MISC_BITS_SERDES_XPD_PLL_S 20
#define MISC_BITS_SERDES_GPD (BIT(19))
#define MISC_BITS_SERDES_GPD_S 19
#define MISC_BITS_SERDES_RX_PAUSE (BIT(18))
#define MISC_BITS_SERDES_RX_PAUSE_S 18
#define MISC_BITS_SERDES_RX_LOCKDETEN (BIT(17))
#define MISC_BITS_SERDES_RX_LOCKDETEN_S 17
#define MISC_BITS_SERDES_PLL_I_STOP (BIT(16))
#define MISC_BITS_SERDES_PLL_I_STOP_S 16
#define MISC_BITS_SERDES_RX_LOCK 0x0000000F
#define MISC_BITS_SERDES_RX_LOCK_S 12
#define MISC_BITS_SERDES_RX_DET_OUT 0x0000000F
#define MISC_BITS_SERDES_RX_DET_OUT_S 8
#define MISC_BITS_SERDES_CTRL 0x000000FF
#define MISC_BITS_SERDES_CTRL_S 0

#define MISC_BITS_LVDS_CTRL3_REG (REG_MISC_BASE + 0x0054)
#define MISC_BITS_PHYTX_MB0_SEL 0x0000001F
#define MISC_BITS_PHYTX_MB0_SEL_S 25
#define MISC_BITS_PHYTX_MB1_SEL 0x0000001F
#define MISC_BITS_PHYTX_MB1_SEL_S 20
#define MISC_BITS_PHYTX_MB2_SEL 0x0000001F
#define MISC_BITS_PHYTX_MB2_SEL_S 15
#define MISC_BITS_PHYTX_MB3_SEL 0x0000001F
#define MISC_BITS_PHYTX_MB3_SEL_S 10
#define MISC_BITS_PHYRX_MB0_SEL 0x0000001F
#define MISC_BITS_PHYRX_MB0_SEL_S 5
#define MISC_BITS_PHYRX_MB1_SEL 0x0000001F
#define MISC_BITS_PHYRX_MB1_SEL_S 0

#define MISC_BITS_LVDS_CTRL4_REG (REG_MISC_BASE + 0x0058)
#define MISC_BITS_PHYRX_OUT_EDGE_SEL 0x00000003
#define MISC_BITS_PHYRX_OUT_EDGE_SEL_S 28
#define MISC_BITS_PHYRX_MB2_SEL 0x0000001F
#define MISC_BITS_PHYRX_MB2_SEL_S 23
#define MISC_BITS_PHYRX_MB3_SEL 0x0000001F
#define MISC_BITS_PHYRX_MB3_SEL_S 18
#define MISC_BITS_PHYTX_FREQ_SEL (BIT(17))
#define MISC_BITS_PHYTX_FREQ_SEL_S 17
#define MISC_BITS_PHYTX_DET_MODE (BIT(16))
#define MISC_BITS_PHYTX_DET_MODE_S 16
#define MISC_BITS_PHYRX_8B_ORDER 0x0000000F
#define MISC_BITS_PHYRX_8B_ORDER_S 12
#define MISC_BITS_PHYRX_10B_ORDER 0x0000000F
#define MISC_BITS_PHYRX_10B_ORDER_S 8
#define MISC_BITS_PHYRX_LANE_SEL 0x000000FF
#define MISC_BITS_PHYRX_LANE_SEL_S 0

#define MISC_BITS_LVDS_CTRL5_REG (REG_MISC_BASE + 0x005c)
#define MISC_BITS_SLVHOST_TRAIN_SEL 0x000000FF
#define MISC_BITS_SLVHOST_TRAIN_SEL_S 24
#define MISC_BITS_PHYRX_EN_ARB 0x0000000F
#define MISC_BITS_PHYRX_EN_ARB_S 20
#define MISC_BITS_PHYRX_EDGE_SEL 0x00000003
#define MISC_BITS_PHYRX_EDGE_SEL_S 18
#define MISC_BITS_PHYTX_IN_EDGE_SEL 0x00000003
#define MISC_BITS_PHYTX_IN_EDGE_SEL_S 16
#define MISC_BITS_PHYTX_8B_ORDER 0x0000000F
#define MISC_BITS_PHYTX_8B_ORDER_S 12
#define MISC_BITS_PHYTX_10B_ORDER 0x0000000F
#define MISC_BITS_PHYTX_10B_ORDER_S 8
#define MISC_BITS_PHYTX_LANE_SEL 0x000000FF
#define MISC_BITS_PHYTX_LANE_SEL_S 0

#define MISC_BITS_MISC_CTRL3_REG (REG_MISC_BASE + 0x0060)
#define MISC_BITS_FE_PSEL_EN (BIT(30))
#define MISC_BITS_FE_PSEL_EN_S 30
#define MISC_BITS_SLV_ON2TX_DEL 0x0000003F
#define MISC_BITS_SLV_ON2TX_DEL_S 24
#define MISC_BITS_MODE_SW_DEL 0x0000003F
#define MISC_BITS_MODE_SW_DEL_S 18
#define MISC_BITS_OUT2IN_DV 0x0000003F
#define MISC_BITS_OUT2IN_DV_S 12
#define MISC_BITS_OUT2IN_DEL 0x0000003F
#define MISC_BITS_OUT2IN_DEL_S 6
#define MISC_BITS_SLV_RX2OFF_DEL 0x0000003F
#define MISC_BITS_SLV_RX2OFF_DEL_S 0

#define MISC_BITS_MISC_FE_IQ_EST_CTRL_0_REG (REG_MISC_BASE + 0x0070)
#define MISC_BITS_IQ_EST_DONE (BIT(31))
#define MISC_BITS_IQ_EST_DONE_S 31
#define MISC_BITS_IQ_EST_CTRL_0 0x7FFFFFFF
#define MISC_BITS_IQ_EST_CTRL_0_S 0

#define MISC_BITS_MISC_FE_IQ_EST_CTRL_1_REG (REG_MISC_BASE + 0x0074)
#define MISC_BITS_IQ_EST_SSEA_DONE (BIT(31))
#define MISC_BITS_IQ_EST_SSEA_DONE_S 31
#define MISC_BITS_IQ_EST_SSEA_OVERFLOWA (BIT(30))
#define MISC_BITS_IQ_EST_SSEA_OVERFLOWA_S 30
#define MISC_BITS_IQ_EST_SSEA_OVERFLOWM (BIT(29))
#define MISC_BITS_IQ_EST_SSEA_OVERFLOWM_S 29
#define MISC_BITS_IQ_EST_CTRL_1 0x1FFFFFFF
#define MISC_BITS_IQ_EST_CTRL_1_S 0

#define MISC_BITS_MISC_FE_IQ_RESULT1_REG (REG_MISC_BASE + 0x0078)
#define MISC_BITS_IQ_EST_MULT_II 0xFFFFFFFF
#define MISC_BITS_IQ_EST_MULT_II_S 0

#define MISC_BITS_MISC_FE_IQ_RESULT2_REG (REG_MISC_BASE + 0x007c)
#define MISC_BITS_IQ_EST_MULT_IQ 0xFFFFFFFF
#define MISC_BITS_IQ_EST_MULT_IQ_S 0

#define MISC_BITS_MISC_FE_IQ_RESULT3_REG (REG_MISC_BASE + 0x0080)
#define MISC_BITS_IQ_EST_MULT_QI 0xFFFFFFFF
#define MISC_BITS_IQ_EST_MULT_QI_S 0

#define MISC_BITS_MISC_FE_IQ_RESULT4_REG (REG_MISC_BASE + 0x0084)
#define MISC_BITS_IQ_EST_MULT_QQ 0xFFFFFFFF
#define MISC_BITS_IQ_EST_MULT_QQ_S 0

#define MISC_BITS_MISC_FE_IQ_RESULT_2_1_REG (REG_MISC_BASE + 0x0088)
#define MISC_BITS_IQ_EST_MULT2_II 0xFFFFFFFF
#define MISC_BITS_IQ_EST_MULT2_II_S 0

#define MISC_BITS_MISC_FE_IQ_RESULT_2_2_REG (REG_MISC_BASE + 0x008c)
#define MISC_BITS_IQ_EST_MULT2_IQ 0xFFFFFFFF
#define MISC_BITS_IQ_EST_MULT2_IQ_S 0

#define MISC_BITS_MISC_FE_IQ_RESULT_2_3_REG (REG_MISC_BASE + 0x0090)
#define MISC_BITS_IQ_EST_MULT2_QI 0xFFFFFFFF
#define MISC_BITS_IQ_EST_MULT2_QI_S 0

#define MISC_BITS_MISC_FE_IQ_RESULT_2_4_REG (REG_MISC_BASE + 0x0094)
#define MISC_BITS_IQ_EST_MULT2_QQ 0xFFFFFFFF
#define MISC_BITS_IQ_EST_MULT2_QQ_S 0

#define MISC_BITS_MISC_FE_IQ_RESULT_DC_I_REG (REG_MISC_BASE + 0x0098)
#define MISC_BITS_IQ_EST_MULT_DC_I 0xFFFFFFFF
#define MISC_BITS_IQ_EST_MULT_DC_I_S 0

#define MISC_BITS_MISC_FE_IQ_RESULT_DC_Q_REG (REG_MISC_BASE + 0x009c)
#define MISC_BITS_IQ_EST_MULT_DC_Q 0xFFFFFFFF
#define MISC_BITS_IQ_EST_MULT_DC_Q_S 0

#define MISC_BITS_MISC_FE_IQ_RESULT_PWR_REG (REG_MISC_BASE + 0x00a0)
#define MISC_BITS_IQ_EST_MULT_PWR 0xFFFFFFFF
#define MISC_BITS_IQ_EST_MULT_PWR_S 0

#define MISC_BITS_MISC_FE_IQ_RESULT_PWR_I_REG (REG_MISC_BASE + 0x00a4)
#define MISC_BITS_IQ_EST_MULT_PWR_I 0xFFFFFFFF
#define MISC_BITS_IQ_EST_MULT_PWR_I_S 0

#define MISC_BITS_MISC_FE_IQ_RESULT_PWR_Q_REG (REG_MISC_BASE + 0x00a8)
#define MISC_BITS_IQ_EST_MULT_PWR_Q 0xFFFFFFFF
#define MISC_BITS_IQ_EST_MULT_PWR_Q_S 0

#define MISC_BITS_MISC_FE_IQ_RESULT_PWR_IQ_REG (REG_MISC_BASE + 0x00ac)
#define MISC_BITS_IQ_EST_MULT_PWR_IQ 0xFFFFFFFF
#define MISC_BITS_IQ_EST_MULT_PWR_IQ_S 0

#define MISC_BITS_MISC_FE_IQ_SSEA_CORR1_REG (REG_MISC_BASE + 0x00b0)
#define MISC_BITS_IQ_EST_SSEA_CORR1 0xFFFFFFFF
#define MISC_BITS_IQ_EST_SSEA_CORR1_S 0

#define MISC_BITS_MISC_FE_IQ_SSEA_CORR1_CONJ_REG (REG_MISC_BASE + 0x00b4)
#define MISC_BITS_IQ_EST_SSEA_CORR1_CONJ 0xFFFFFFFF
#define MISC_BITS_IQ_EST_SSEA_CORR1_CONJ_S 0

#define MISC_BITS_MISC_FE_IQ_SSEA_CORR2_REG (REG_MISC_BASE + 0x00b8)
#define MISC_BITS_IQ_EST_SSEA_CORR2 0xFFFFFFFF
#define MISC_BITS_IQ_EST_SSEA_CORR2_S 0

#define MISC_BITS_MISC_FE_IQ_SSEA_CORR2_CONJ_REG (REG_MISC_BASE + 0x00bc)
#define MISC_BITS_IQ_EST_SSEA_CORR2_CONJ 0xFFFFFFFF
#define MISC_BITS_IQ_EST_SSEA_CORR2_CONJ_S 0

#define MISC_BITS_MISC_FE_IQ_SSEA_DC_REG (REG_MISC_BASE + 0x00c0)
#define MISC_BITS_IQ_EST_SSEA_DC 0xFFFFFFFF
#define MISC_BITS_IQ_EST_SSEA_DC_S 0

#define MISC_BITS_MISC_FE_IQ_SSEA_POWER_REG (REG_MISC_BASE + 0x00c4)
#define MISC_BITS_IQ_EST_SSEA_POWER 0xFFFFFFFF
#define MISC_BITS_IQ_EST_SSEA_POWER_S 0

#define MISC_BITS_MISC_DUMP_REG (REG_MISC_BASE + 0x00c8)
#define MISC_BITS_DMEM_RD_ST_DIV2 0x00003FFF
#define MISC_BITS_DMEM_RD_ST_DIV2_S 18
#define MISC_BITS_DMEM_WR_DONE (BIT(17))
#define MISC_BITS_DMEM_WR_DONE_S 17
#define MISC_BITS_DMEM_RD_EN (BIT(16))
#define MISC_BITS_DMEM_RD_EN_S 16
#define MISC_BITS_DMEM_WR_EN (BIT(15))
#define MISC_BITS_DMEM_WR_EN_S 15
#define MISC_BITS_DMEM_WR_NUM 0x00007FFF
#define MISC_BITS_DMEM_WR_NUM_S 0

#define MISC_BITS_MISC_DUMP_RD_REG (REG_MISC_BASE + 0x00f0)

#define MISC_BITS_TX_TEST_CTRL0_REG (REG_MISC_BASE + 0x00f4)
#define MISC_BITS_TX_TEST_CTRL0 0xFFFFFFFF
#define MISC_BITS_TX_TEST_CTRL0_S 0

#define MISC_BITS_MISC_NOUSE_1_REG (REG_MISC_BASE + 0x00f8)
#define MISC_BITS_MISC_NOUSE_1 0xFFFFFFFF
#define MISC_BITS_MISC_NOUSE_1_S 0

#define MISC_BITS_MISC_NOUSE_0_REG (REG_MISC_BASE + 0x00fc)
#define MISC_BITS_MISC_NOUSE_0 0xFFFFFFFF
#define MISC_BITS_MISC_NOUSE_0_S 0