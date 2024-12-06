
#define RTC_I2C_SCL_LOW_REG (REG_RTC_I2C_BASE + 0x0000)
#define RTC_I2C_SCL_LOW_PERIOD_REG 0x000FFFFF
#define RTC_I2C_SCL_LOW_PERIOD_REG_S 0

#define RTC_I2C_CTRL_REG (REG_RTC_I2C_BASE + 0x0004)
#define RTC_I2C_I2CCLK_EN (BIT(31))
#define RTC_I2C_I2CCLK_EN_S 31
#define RTC_I2C_I2C_RESET (BIT(30))
#define RTC_I2C_I2C_RESET_S 30
#define RTC_I2C_RX_LSB_FIRST (BIT(5))
#define RTC_I2C_RX_LSB_FIRST_S 5
#define RTC_I2C_TX_LSB_FIRST (BIT(4))
#define RTC_I2C_TX_LSB_FIRST_S 4
#define RTC_I2C_TRANS_START (BIT(3))
#define RTC_I2C_TRANS_START_S 3
#define RTC_I2C_MS_MODE (BIT(2))
#define RTC_I2C_MS_MODE_S 2
#define RTC_I2C_SCL_FORCE_OUT (BIT(1))
#define RTC_I2C_SCL_FORCE_OUT_S 1
#define RTC_I2C_SDA_FORCE_OUT (BIT(0))
#define RTC_I2C_SDA_FORCE_OUT_S 0

#define RTC_I2C_STATUS_REG (REG_RTC_I2C_BASE + 0x0008)
#define RTC_I2C_SCL_STATE_LAST 0x00000007
#define RTC_I2C_SCL_STATE_LAST_S 28
#define RTC_I2C_SCL_MAIN_STATE_LAST 0x00000007
#define RTC_I2C_SCL_MAIN_STATE_LAST_S 24
#define RTC_I2C_SHIFT_REG 0x000000FF
#define RTC_I2C_SHIFT_REG_S 16
#define RTC_I2C_OP_CNT 0x00000003
#define RTC_I2C_OP_CNT_S 6
#define RTC_I2C_BYTE_TRANS (BIT(5))
#define RTC_I2C_BYTE_TRANS_S 5
#define RTC_I2C_SLAVE_ADDRESSED (BIT(4))
#define RTC_I2C_SLAVE_ADDRESSED_S 4
#define RTC_I2C_BUS_BUSY (BIT(3))
#define RTC_I2C_BUS_BUSY_S 3
#define RTC_I2C_ARB_LOST (BIT(2))
#define RTC_I2C_ARB_LOST_S 2
#define RTC_I2C_SLAVE_RW (BIT(1))
#define RTC_I2C_SLAVE_RW_S 1
#define RTC_I2C_ACK_REC (BIT(0))
#define RTC_I2C_ACK_REC_S 0

#define RTC_I2C_TO_REG (REG_RTC_I2C_BASE + 0x000c)
#define RTC_I2C_TIME_OUT_REG 0x000FFFFF
#define RTC_I2C_TIME_OUT_REG_S 0

#define RTC_I2C_SLAVE_ADDR_REG (REG_RTC_I2C_BASE + 0x0010)
#define RTC_I2C_ADDR_10BIT_EN (BIT(31))
#define RTC_I2C_ADDR_10BIT_EN_S 31
#define RTC_I2C_SLAVE_ADDR 0x00007FFF
#define RTC_I2C_SLAVE_ADDR_S 0

#define RTC_I2C_SCL_HIGH_REG (REG_RTC_I2C_BASE + 0x0014)
#define RTC_I2C_SCL_HIGH_PERIOD_REG 0x000FFFFF
#define RTC_I2C_SCL_HIGH_PERIOD_REG_S 0

#define RTC_I2C_SDA_DUTY_REG (REG_RTC_I2C_BASE + 0x0018)
#define RTC_I2C_SDA_DUTY_NUM 0x000FFFFF
#define RTC_I2C_SDA_DUTY_NUM_S 0

#define RTC_I2C_SCL_START_PERIOD_REG (REG_RTC_I2C_BASE + 0x001c)
#define RTC_I2C_SCL_START_PERIOD 0x000FFFFF
#define RTC_I2C_SCL_START_PERIOD_S 0

#define RTC_I2C_SCL_STOP_PERIOD_REG (REG_RTC_I2C_BASE + 0x0020)
#define RTC_I2C_SCL_STOP_PERIOD 0x000FFFFF
#define RTC_I2C_SCL_STOP_PERIOD_S 0

#define RTC_I2C_INT_CLR_REG (REG_RTC_I2C_BASE + 0x0024)
#define RTC_I2C_DETECT_START_INT_CLR (BIT(8))
#define RTC_I2C_DETECT_START_INT_CLR_S 8
#define RTC_I2C_TX_DATA_INT_CLR (BIT(7))
#define RTC_I2C_TX_DATA_INT_CLR_S 7
#define RTC_I2C_RX_DATA_INT_CLR (BIT(6))
#define RTC_I2C_RX_DATA_INT_CLR_S 6
#define RTC_I2C_ACK_ERR_INT_CLR (BIT(5))
#define RTC_I2C_ACK_ERR_INT_CLR_S 5
#define RTC_I2C_TIME_OUT_INT_CLR (BIT(4))
#define RTC_I2C_TIME_OUT_INT_CLR_S 4
#define RTC_I2C_TRANS_COMPLETE_INT_CLR (BIT(3))
#define RTC_I2C_TRANS_COMPLETE_INT_CLR_S 3
#define RTC_I2C_MASTER_TRAN_COMP_INT_CLR (BIT(2))
#define RTC_I2C_MASTER_TRAN_COMP_INT_CLR_S 2
#define RTC_I2C_ARBITRATION_LOST_INT_CLR (BIT(1))
#define RTC_I2C_ARBITRATION_LOST_INT_CLR_S 1
#define RTC_I2C_SLAVE_TRAN_COMP_INT_CLR (BIT(0))
#define RTC_I2C_SLAVE_TRAN_COMP_INT_CLR_S 0

#define RTC_I2C_INT_RAW_REG (REG_RTC_I2C_BASE + 0x0028)
#define RTC_I2C_DETECT_START_INT_RAW (BIT(8))
#define RTC_I2C_DETECT_START_INT_RAW_S 8
#define RTC_I2C_TX_DATA_INT_RAW (BIT(7))
#define RTC_I2C_TX_DATA_INT_RAW_S 7
#define RTC_I2C_RX_DATA_INT_RAW (BIT(6))
#define RTC_I2C_RX_DATA_INT_RAW_S 6
#define RTC_I2C_ACK_ERR_INT_RAW (BIT(5))
#define RTC_I2C_ACK_ERR_INT_RAW_S 5
#define RTC_I2C_TIME_OUT_INT_RAW (BIT(4))
#define RTC_I2C_TIME_OUT_INT_RAW_S 4
#define RTC_I2C_TRANS_COMPLETE_INT_RAW (BIT(3))
#define RTC_I2C_TRANS_COMPLETE_INT_RAW_S 3
#define RTC_I2C_MASTER_TRAN_COMP_INT_RAW (BIT(2))
#define RTC_I2C_MASTER_TRAN_COMP_INT_RAW_S 2
#define RTC_I2C_ARBITRATION_LOST_INT_RAW (BIT(1))
#define RTC_I2C_ARBITRATION_LOST_INT_RAW_S 1
#define RTC_I2C_SLAVE_TRAN_COMP_INT_RAW (BIT(0))
#define RTC_I2C_SLAVE_TRAN_COMP_INT_RAW_S 0

#define RTC_I2C_INT_ST_REG (REG_RTC_I2C_BASE + 0x002c)
#define RTC_I2C_DETECT_START_INT_ST (BIT(8))
#define RTC_I2C_DETECT_START_INT_ST_S 8
#define RTC_I2C_TX_DATA_INT_ST (BIT(7))
#define RTC_I2C_TX_DATA_INT_ST_S 7
#define RTC_I2C_RX_DATA_INT_ST (BIT(6))
#define RTC_I2C_RX_DATA_INT_ST_S 6
#define RTC_I2C_ACK_ERR_INT_ST (BIT(5))
#define RTC_I2C_ACK_ERR_INT_ST_S 5
#define RTC_I2C_TIME_OUT_INT_ST (BIT(4))
#define RTC_I2C_TIME_OUT_INT_ST_S 4
#define RTC_I2C_TRANS_COMPLETE_INT_ST (BIT(3))
#define RTC_I2C_TRANS_COMPLETE_INT_ST_S 3
#define RTC_I2C_MASTER_TRAN_COMP_INT_ST (BIT(2))
#define RTC_I2C_MASTER_TRAN_COMP_INT_ST_S 2
#define RTC_I2C_ARBITRATION_LOST_INT_ST (BIT(1))
#define RTC_I2C_ARBITRATION_LOST_INT_ST_S 1
#define RTC_I2C_SLAVE_TRAN_COMP_INT_ST (BIT(0))
#define RTC_I2C_SLAVE_TRAN_COMP_INT_ST_S 0

#define RTC_I2C_INT_ENA_REG (REG_RTC_I2C_BASE + 0x0030)
#define RTC_I2C_DETECT_START_INT_ENA (BIT(8))
#define RTC_I2C_DETECT_START_INT_ENA_S 8
#define RTC_I2C_TX_DATA_INT_ENA (BIT(7))
#define RTC_I2C_TX_DATA_INT_ENA_S 7
#define RTC_I2C_RX_DATA_INT_ENA (BIT(6))
#define RTC_I2C_RX_DATA_INT_ENA_S 6
#define RTC_I2C_ACK_ERR_INT_ENA (BIT(5))
#define RTC_I2C_ACK_ERR_INT_ENA_S 5
#define RTC_I2C_TIME_OUT_INT_ENA (BIT(4))
#define RTC_I2C_TIME_OUT_INT_ENA_S 4
#define RTC_I2C_TRANS_COMPLETE_INT_ENA (BIT(3))
#define RTC_I2C_TRANS_COMPLETE_INT_ENA_S 3
#define RTC_I2C_MASTER_TRAN_COMP_INT_ENA (BIT(2))
#define RTC_I2C_MASTER_TRAN_COMP_INT_ENA_S 2
#define RTC_I2C_ARBITRATION_LOST_INT_ENA (BIT(1))
#define RTC_I2C_ARBITRATION_LOST_INT_ENA_S 1
#define RTC_I2C_SLAVE_TRAN_COMP_INT_ENA (BIT(0))
#define RTC_I2C_SLAVE_TRAN_COMP_INT_ENA_S 0

#define RTC_I2C_DATA_REG (REG_RTC_I2C_BASE + 0x0034)
#define RTC_I2C_I2C_DONE (BIT(31))
#define RTC_I2C_I2C_DONE_S 31
#define RTC_I2C_SLAVE_TX_DATA 0x000000FF
#define RTC_I2C_SLAVE_TX_DATA_S 8
#define RTC_I2C_I2C_RDATA 0x000000FF
#define RTC_I2C_I2C_RDATA_S 0

#define RTC_I2C_CMD0_REG (REG_RTC_I2C_BASE + 0x0038)
#define RTC_I2C_COMMAND0_DONE (BIT(31))
#define RTC_I2C_COMMAND0_DONE_S 31
#define RTC_I2C_COMMAND0 0x00003FFF
#define RTC_I2C_COMMAND0_S 0

#define RTC_I2C_CMD1_REG (REG_RTC_I2C_BASE + 0x003c)
#define RTC_I2C_COMMAND1_DONE (BIT(31))
#define RTC_I2C_COMMAND1_DONE_S 31
#define RTC_I2C_COMMAND1 0x00003FFF
#define RTC_I2C_COMMAND1_S 0

#define RTC_I2C_CMD2_REG (REG_RTC_I2C_BASE + 0x0040)
#define RTC_I2C_COMMAND2_DONE (BIT(31))
#define RTC_I2C_COMMAND2_DONE_S 31
#define RTC_I2C_COMMAND2 0x00003FFF
#define RTC_I2C_COMMAND2_S 0

#define RTC_I2C_CMD3_REG (REG_RTC_I2C_BASE + 0x0044)
#define RTC_I2C_COMMAND3_DONE (BIT(31))
#define RTC_I2C_COMMAND3_DONE_S 31
#define RTC_I2C_COMMAND3 0x00003FFF
#define RTC_I2C_COMMAND3_S 0

#define RTC_I2C_CMD4_REG (REG_RTC_I2C_BASE + 0x0048)
#define RTC_I2C_COMMAND4_DONE (BIT(31))
#define RTC_I2C_COMMAND4_DONE_S 31
#define RTC_I2C_COMMAND4 0x00003FFF
#define RTC_I2C_COMMAND4_S 0

#define RTC_I2C_CMD5_REG (REG_RTC_I2C_BASE + 0x004c)
#define RTC_I2C_COMMAND5_DONE (BIT(31))
#define RTC_I2C_COMMAND5_DONE_S 31
#define RTC_I2C_COMMAND5 0x00003FFF
#define RTC_I2C_COMMAND5_S 0

#define RTC_I2C_CMD6_REG (REG_RTC_I2C_BASE + 0x0050)
#define RTC_I2C_COMMAND6_DONE (BIT(31))
#define RTC_I2C_COMMAND6_DONE_S 31
#define RTC_I2C_COMMAND6 0x00003FFF
#define RTC_I2C_COMMAND6_S 0

#define RTC_I2C_CMD7_REG (REG_RTC_I2C_BASE + 0x0054)
#define RTC_I2C_COMMAND7_DONE (BIT(31))
#define RTC_I2C_COMMAND7_DONE_S 31
#define RTC_I2C_COMMAND7 0x00003FFF
#define RTC_I2C_COMMAND7_S 0

#define RTC_I2C_CMD8_REG (REG_RTC_I2C_BASE + 0x0058)
#define RTC_I2C_COMMAND8_DONE (BIT(31))
#define RTC_I2C_COMMAND8_DONE_S 31
#define RTC_I2C_COMMAND8 0x00003FFF
#define RTC_I2C_COMMAND8_S 0

#define RTC_I2C_CMD9_REG (REG_RTC_I2C_BASE + 0x005c)
#define RTC_I2C_COMMAND9_DONE (BIT(31))
#define RTC_I2C_COMMAND9_DONE_S 31
#define RTC_I2C_COMMAND9 0x00003FFF
#define RTC_I2C_COMMAND9_S 0

#define RTC_I2C_CMD10_REG (REG_RTC_I2C_BASE + 0x0060)
#define RTC_I2C_COMMAND10_DONE (BIT(31))
#define RTC_I2C_COMMAND10_DONE_S 31
#define RTC_I2C_COMMAND10 0x00003FFF
#define RTC_I2C_COMMAND10_S 0

#define RTC_I2C_CMD11_REG (REG_RTC_I2C_BASE + 0x0064)
#define RTC_I2C_COMMAND11_DONE (BIT(31))
#define RTC_I2C_COMMAND11_DONE_S 31
#define RTC_I2C_COMMAND11 0x00003FFF
#define RTC_I2C_COMMAND11_S 0

#define RTC_I2C_CMD12_REG (REG_RTC_I2C_BASE + 0x0068)
#define RTC_I2C_COMMAND12_DONE (BIT(31))
#define RTC_I2C_COMMAND12_DONE_S 31
#define RTC_I2C_COMMAND12 0x00003FFF
#define RTC_I2C_COMMAND12_S 0

#define RTC_I2C_CMD13_REG (REG_RTC_I2C_BASE + 0x006c)
#define RTC_I2C_COMMAND13_DONE (BIT(31))
#define RTC_I2C_COMMAND13_DONE_S 31
#define RTC_I2C_COMMAND13 0x00003FFF
#define RTC_I2C_COMMAND13_S 0

#define RTC_I2C_CMD14_REG (REG_RTC_I2C_BASE + 0x0070)
#define RTC_I2C_COMMAND14_DONE (BIT(31))
#define RTC_I2C_COMMAND14_DONE_S 31
#define RTC_I2C_COMMAND14 0x00003FFF
#define RTC_I2C_COMMAND14_S 0

#define RTC_I2C_CMD15_REG (REG_RTC_I2C_BASE + 0x0074)
#define RTC_I2C_COMMAND15_DONE (BIT(31))
#define RTC_I2C_COMMAND15_DONE_S 31
#define RTC_I2C_COMMAND15 0x00003FFF
#define RTC_I2C_COMMAND15_S 0

#define RTC_I2C_DATE_REG (REG_RTC_I2C_BASE + 0x00FC)
#define RTC_I2C_I2C_DATE 0x0FFFFFFF
#define RTC_I2C_I2C_DATE_S 0
#define RTC_I2C_I2C_DATE_VERSION 0x1711170
