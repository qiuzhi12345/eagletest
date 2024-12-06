
#define RMT_CH0DATA_REG (REG_RMT_BASE + 0x0000)

#define RMT_CH1DATA_REG (REG_RMT_BASE + 0x0004)

#define RMT_CH2DATA_REG (REG_RMT_BASE + 0x0008)

#define RMT_CH3DATA_REG (REG_RMT_BASE + 0x000c)

#define RMT_CH0CONF0_REG (REG_RMT_BASE + 0x0010)
#define RMT_CLK_EN (BIT(31))
#define RMT_CLK_EN_S 31
#define RMT_MEM_PD (BIT(30))
#define RMT_MEM_PD_S 30
#define RMT_CARRIER_OUT_LV_CH0 (BIT(29))
#define RMT_CARRIER_OUT_LV_CH0_S 29
#define RMT_CARRIER_EN_CH0 (BIT(28))
#define RMT_CARRIER_EN_CH0_S 28
#define RMT_MEM_SIZE_CH0 0x00000007
#define RMT_MEM_SIZE_CH0_S 24
#define RMT_IDLE_THRES_CH0 0x0000FFFF
#define RMT_IDLE_THRES_CH0_S 8
#define RMT_DIV_CNT_CH0 0x000000FF
#define RMT_DIV_CNT_CH0_S 0

#define RMT_CH0CONF1_REG (REG_RMT_BASE + 0x0014)
#define RMT_TX_STOP_CH0 (BIT(20))
#define RMT_TX_STOP_CH0_S 20
#define RMT_IDLE_OUT_EN_CH0 (BIT(19))
#define RMT_IDLE_OUT_EN_CH0_S 19
#define RMT_IDLE_OUT_LV_CH0 (BIT(18))
#define RMT_IDLE_OUT_LV_CH0_S 18
#define RMT_REF_ALWAYS_ON_CH0 (BIT(17))
#define RMT_REF_ALWAYS_ON_CH0_S 17
#define RMT_RX_FILTER_THRES_CH0 0x000000FF
#define RMT_RX_FILTER_THRES_CH0_S 8
#define RMT_RX_FILTER_EN_CH0 (BIT(7))
#define RMT_RX_FILTER_EN_CH0_S 7
#define RMT_TX_CONTI_MODE_CH0 (BIT(6))
#define RMT_TX_CONTI_MODE_CH0_S 6
#define RMT_MEM_OWNER_CH0 (BIT(5))
#define RMT_MEM_OWNER_CH0_S 5
#define RMT_APB_MEM_RST_CH0 (BIT(4))
#define RMT_APB_MEM_RST_CH0_S 4
#define RMT_MEM_RD_RST_CH0 (BIT(3))
#define RMT_MEM_RD_RST_CH0_S 3
#define RMT_MEM_WR_RST_CH0 (BIT(2))
#define RMT_MEM_WR_RST_CH0_S 2
#define RMT_RX_EN_CH0 (BIT(1))
#define RMT_RX_EN_CH0_S 1
#define RMT_TX_START_CH0 (BIT(0))
#define RMT_TX_START_CH0_S 0

#define RMT_CH1CONF0_REG (REG_RMT_BASE + 0x0018)
#define RMT_CARRIER_OUT_LV_CH1 (BIT(29))
#define RMT_CARRIER_OUT_LV_CH1_S 29
#define RMT_CARRIER_EN_CH1 (BIT(28))
#define RMT_CARRIER_EN_CH1_S 28
#define RMT_MEM_SIZE_CH1 0x00000007
#define RMT_MEM_SIZE_CH1_S 24
#define RMT_IDLE_THRES_CH1 0x0000FFFF
#define RMT_IDLE_THRES_CH1_S 8
#define RMT_DIV_CNT_CH1 0x000000FF
#define RMT_DIV_CNT_CH1_S 0

#define RMT_CH1CONF1_REG (REG_RMT_BASE + 0x001c)
#define RMT_TX_STOP_CH1 (BIT(20))
#define RMT_TX_STOP_CH1_S 20
#define RMT_IDLE_OUT_EN_CH1 (BIT(19))
#define RMT_IDLE_OUT_EN_CH1_S 19
#define RMT_IDLE_OUT_LV_CH1 (BIT(18))
#define RMT_IDLE_OUT_LV_CH1_S 18
#define RMT_REF_ALWAYS_ON_CH1 (BIT(17))
#define RMT_REF_ALWAYS_ON_CH1_S 17
#define RMT_RX_FILTER_THRES_CH1 0x000000FF
#define RMT_RX_FILTER_THRES_CH1_S 8
#define RMT_RX_FILTER_EN_CH1 (BIT(7))
#define RMT_RX_FILTER_EN_CH1_S 7
#define RMT_TX_CONTI_MODE_CH1 (BIT(6))
#define RMT_TX_CONTI_MODE_CH1_S 6
#define RMT_MEM_OWNER_CH1 (BIT(5))
#define RMT_MEM_OWNER_CH1_S 5
#define RMT_APB_MEM_RST_CH1 (BIT(4))
#define RMT_APB_MEM_RST_CH1_S 4
#define RMT_MEM_RD_RST_CH1 (BIT(3))
#define RMT_MEM_RD_RST_CH1_S 3
#define RMT_MEM_WR_RST_CH1 (BIT(2))
#define RMT_MEM_WR_RST_CH1_S 2
#define RMT_RX_EN_CH1 (BIT(1))
#define RMT_RX_EN_CH1_S 1
#define RMT_TX_START_CH1 (BIT(0))
#define RMT_TX_START_CH1_S 0

#define RMT_CH2CONF0_REG (REG_RMT_BASE + 0x0020)
#define RMT_CARRIER_OUT_LV_CH2 (BIT(29))
#define RMT_CARRIER_OUT_LV_CH2_S 29
#define RMT_CARRIER_EN_CH2 (BIT(28))
#define RMT_CARRIER_EN_CH2_S 28
#define RMT_MEM_SIZE_CH2 0x00000007
#define RMT_MEM_SIZE_CH2_S 24
#define RMT_IDLE_THRES_CH2 0x0000FFFF
#define RMT_IDLE_THRES_CH2_S 8
#define RMT_DIV_CNT_CH2 0x000000FF
#define RMT_DIV_CNT_CH2_S 0

#define RMT_CH2CONF1_REG (REG_RMT_BASE + 0x0024)
#define RMT_TX_STOP_CH2 (BIT(20))
#define RMT_TX_STOP_CH2_S 20
#define RMT_IDLE_OUT_EN_CH2 (BIT(19))
#define RMT_IDLE_OUT_EN_CH2_S 19
#define RMT_IDLE_OUT_LV_CH2 (BIT(18))
#define RMT_IDLE_OUT_LV_CH2_S 18
#define RMT_REF_ALWAYS_ON_CH2 (BIT(17))
#define RMT_REF_ALWAYS_ON_CH2_S 17
#define RMT_RX_FILTER_THRES_CH2 0x000000FF
#define RMT_RX_FILTER_THRES_CH2_S 8
#define RMT_RX_FILTER_EN_CH2 (BIT(7))
#define RMT_RX_FILTER_EN_CH2_S 7
#define RMT_TX_CONTI_MODE_CH2 (BIT(6))
#define RMT_TX_CONTI_MODE_CH2_S 6
#define RMT_MEM_OWNER_CH2 (BIT(5))
#define RMT_MEM_OWNER_CH2_S 5
#define RMT_APB_MEM_RST_CH2 (BIT(4))
#define RMT_APB_MEM_RST_CH2_S 4
#define RMT_MEM_RD_RST_CH2 (BIT(3))
#define RMT_MEM_RD_RST_CH2_S 3
#define RMT_MEM_WR_RST_CH2 (BIT(2))
#define RMT_MEM_WR_RST_CH2_S 2
#define RMT_RX_EN_CH2 (BIT(1))
#define RMT_RX_EN_CH2_S 1
#define RMT_TX_START_CH2 (BIT(0))
#define RMT_TX_START_CH2_S 0

#define RMT_CH3CONF0_REG (REG_RMT_BASE + 0x0028)
#define RMT_CARRIER_OUT_LV_CH3 (BIT(29))
#define RMT_CARRIER_OUT_LV_CH3_S 29
#define RMT_CARRIER_EN_CH3 (BIT(28))
#define RMT_CARRIER_EN_CH3_S 28
#define RMT_MEM_SIZE_CH3 0x00000007
#define RMT_MEM_SIZE_CH3_S 24
#define RMT_IDLE_THRES_CH3 0x0000FFFF
#define RMT_IDLE_THRES_CH3_S 8
#define RMT_DIV_CNT_CH3 0x000000FF
#define RMT_DIV_CNT_CH3_S 0

#define RMT_CH3CONF1_REG (REG_RMT_BASE + 0x002c)
#define RMT_TX_STOP_CH3 (BIT(20))
#define RMT_TX_STOP_CH3_S 20
#define RMT_IDLE_OUT_EN_CH3 (BIT(19))
#define RMT_IDLE_OUT_EN_CH3_S 19
#define RMT_IDLE_OUT_LV_CH3 (BIT(18))
#define RMT_IDLE_OUT_LV_CH3_S 18
#define RMT_REF_ALWAYS_ON_CH3 (BIT(17))
#define RMT_REF_ALWAYS_ON_CH3_S 17
#define RMT_RX_FILTER_THRES_CH3 0x000000FF
#define RMT_RX_FILTER_THRES_CH3_S 8
#define RMT_RX_FILTER_EN_CH3 (BIT(7))
#define RMT_RX_FILTER_EN_CH3_S 7
#define RMT_TX_CONTI_MODE_CH3 (BIT(6))
#define RMT_TX_CONTI_MODE_CH3_S 6
#define RMT_MEM_OWNER_CH3 (BIT(5))
#define RMT_MEM_OWNER_CH3_S 5
#define RMT_APB_MEM_RST_CH3 (BIT(4))
#define RMT_APB_MEM_RST_CH3_S 4
#define RMT_MEM_RD_RST_CH3 (BIT(3))
#define RMT_MEM_RD_RST_CH3_S 3
#define RMT_MEM_WR_RST_CH3 (BIT(2))
#define RMT_MEM_WR_RST_CH3_S 2
#define RMT_RX_EN_CH3 (BIT(1))
#define RMT_RX_EN_CH3_S 1
#define RMT_TX_START_CH3 (BIT(0))
#define RMT_TX_START_CH3_S 0

#define RMT_CH0STATUS_REG (REG_RMT_BASE + 0x0030)
#define RMT_APB_MEM_RD_ERR_CH0 (BIT(27))
#define RMT_APB_MEM_RD_ERR_CH0_S 27
#define RMT_APB_MEM_WR_ERR_CH0 (BIT(26))
#define RMT_APB_MEM_WR_ERR_CH0_S 26
#define RMT_MEM_EMPTY_CH0 (BIT(25))
#define RMT_MEM_EMPTY_CH0_S 25
#define RMT_MEM_FULL_CH0 (BIT(24))
#define RMT_MEM_FULL_CH0_S 24
#define RMT_MEM_OWNER_ERR_CH0 (BIT(23))
#define RMT_MEM_OWNER_ERR_CH0_S 23
#define RMT_STATE_CH0 0x00000007
#define RMT_STATE_CH0_S 20
#define RMT_MEM_RADDR_EX_CH0 0x000001FF
#define RMT_MEM_RADDR_EX_CH0_S 10
#define RMT_MEM_WADDR_EX_CH0 0x000001FF
#define RMT_MEM_WADDR_EX_CH0_S 0

#define RMT_CH1STATUS_REG (REG_RMT_BASE + 0x0034)
#define RMT_APB_MEM_RD_ERR_CH1 (BIT(27))
#define RMT_APB_MEM_RD_ERR_CH1_S 27
#define RMT_APB_MEM_WR_ERR_CH1 (BIT(26))
#define RMT_APB_MEM_WR_ERR_CH1_S 26
#define RMT_MEM_EMPTY_CH1 (BIT(25))
#define RMT_MEM_EMPTY_CH1_S 25
#define RMT_MEM_FULL_CH1 (BIT(24))
#define RMT_MEM_FULL_CH1_S 24
#define RMT_MEM_OWNER_ERR_CH1 (BIT(23))
#define RMT_MEM_OWNER_ERR_CH1_S 23
#define RMT_STATE_CH1 0x00000007
#define RMT_STATE_CH1_S 20
#define RMT_MEM_RADDR_EX_CH1 0x000001FF
#define RMT_MEM_RADDR_EX_CH1_S 10
#define RMT_MEM_WADDR_EX_CH1 0x000001FF
#define RMT_MEM_WADDR_EX_CH1_S 0

#define RMT_CH2STATUS_REG (REG_RMT_BASE + 0x0038)
#define RMT_APB_MEM_RD_ERR_CH2 (BIT(27))
#define RMT_APB_MEM_RD_ERR_CH2_S 27
#define RMT_APB_MEM_WR_ERR_CH2 (BIT(26))
#define RMT_APB_MEM_WR_ERR_CH2_S 26
#define RMT_MEM_EMPTY_CH2 (BIT(25))
#define RMT_MEM_EMPTY_CH2_S 25
#define RMT_MEM_FULL_CH2 (BIT(24))
#define RMT_MEM_FULL_CH2_S 24
#define RMT_MEM_OWNER_ERR_CH2 (BIT(23))
#define RMT_MEM_OWNER_ERR_CH2_S 23
#define RMT_STATE_CH2 0x00000007
#define RMT_STATE_CH2_S 20
#define RMT_MEM_RADDR_EX_CH2 0x000001FF
#define RMT_MEM_RADDR_EX_CH2_S 10
#define RMT_MEM_WADDR_EX_CH2 0x000001FF
#define RMT_MEM_WADDR_EX_CH2_S 0

#define RMT_CH3STATUS_REG (REG_RMT_BASE + 0x003c)
#define RMT_APB_MEM_RD_ERR_CH3 (BIT(27))
#define RMT_APB_MEM_RD_ERR_CH3_S 27
#define RMT_APB_MEM_WR_ERR_CH3 (BIT(26))
#define RMT_APB_MEM_WR_ERR_CH3_S 26
#define RMT_MEM_EMPTY_CH3 (BIT(25))
#define RMT_MEM_EMPTY_CH3_S 25
#define RMT_MEM_FULL_CH3 (BIT(24))
#define RMT_MEM_FULL_CH3_S 24
#define RMT_MEM_OWNER_ERR_CH3 (BIT(23))
#define RMT_MEM_OWNER_ERR_CH3_S 23
#define RMT_STATE_CH3 0x00000007
#define RMT_STATE_CH3_S 20
#define RMT_MEM_RADDR_EX_CH3 0x000001FF
#define RMT_MEM_RADDR_EX_CH3_S 10
#define RMT_MEM_WADDR_EX_CH3 0x000001FF
#define RMT_MEM_WADDR_EX_CH3_S 0

#define RMT_CH0ADDR_REG (REG_RMT_BASE + 0x0040)
#define RMT_APB_MEM_RADDR_CH0 0x000001FF
#define RMT_APB_MEM_RADDR_CH0_S 10
#define RMT_APB_MEM_WADDR_CH0 0x000001FF
#define RMT_APB_MEM_WADDR_CH0_S 0

#define RMT_CH1ADDR_REG (REG_RMT_BASE + 0x0044)
#define RMT_APB_MEM_RADDR_CH1 0x000001FF
#define RMT_APB_MEM_RADDR_CH1_S 10
#define RMT_APB_MEM_WADDR_CH1 0x000001FF
#define RMT_APB_MEM_WADDR_CH1_S 0

#define RMT_CH2ADDR_REG (REG_RMT_BASE + 0x0048)
#define RMT_APB_MEM_RADDR_CH2 0x000001FF
#define RMT_APB_MEM_RADDR_CH2_S 10
#define RMT_APB_MEM_WADDR_CH2 0x000001FF
#define RMT_APB_MEM_WADDR_CH2_S 0

#define RMT_CH3ADDR_REG (REG_RMT_BASE + 0x004c)
#define RMT_APB_MEM_RADDR_CH3 0x000001FF
#define RMT_APB_MEM_RADDR_CH3_S 10
#define RMT_APB_MEM_WADDR_CH3 0x000001FF
#define RMT_APB_MEM_WADDR_CH3_S 0

#define RMT_INT_RAW_REG (REG_RMT_BASE + 0x0050)
#define RMT_CH3_TX_LOOP_INT_RAW (BIT(19))
#define RMT_CH3_TX_LOOP_INT_RAW_S 19
#define RMT_CH2_TX_LOOP_INT_RAW (BIT(18))
#define RMT_CH2_TX_LOOP_INT_RAW_S 18
#define RMT_CH1_TX_LOOP_INT_RAW (BIT(17))
#define RMT_CH1_TX_LOOP_INT_RAW_S 17
#define RMT_CH0_TX_LOOP_INT_RAW (BIT(16))
#define RMT_CH0_TX_LOOP_INT_RAW_S 16
#define RMT_CH3_TX_THR_EVENT_INT_RAW (BIT(15))
#define RMT_CH3_TX_THR_EVENT_INT_RAW_S 15
#define RMT_CH2_TX_THR_EVENT_INT_RAW (BIT(14))
#define RMT_CH2_TX_THR_EVENT_INT_RAW_S 14
#define RMT_CH1_TX_THR_EVENT_INT_RAW (BIT(13))
#define RMT_CH1_TX_THR_EVENT_INT_RAW_S 13
#define RMT_CH0_TX_THR_EVENT_INT_RAW (BIT(12))
#define RMT_CH0_TX_THR_EVENT_INT_RAW_S 12
#define RMT_CH3_ERR_INT_RAW (BIT(11))
#define RMT_CH3_ERR_INT_RAW_S 11
#define RMT_CH3_RX_END_INT_RAW (BIT(10))
#define RMT_CH3_RX_END_INT_RAW_S 10
#define RMT_CH3_TX_END_INT_RAW (BIT(9))
#define RMT_CH3_TX_END_INT_RAW_S 9
#define RMT_CH2_ERR_INT_RAW (BIT(8))
#define RMT_CH2_ERR_INT_RAW_S 8
#define RMT_CH2_RX_END_INT_RAW (BIT(7))
#define RMT_CH2_RX_END_INT_RAW_S 7
#define RMT_CH2_TX_END_INT_RAW (BIT(6))
#define RMT_CH2_TX_END_INT_RAW_S 6
#define RMT_CH1_ERR_INT_RAW (BIT(5))
#define RMT_CH1_ERR_INT_RAW_S 5
#define RMT_CH1_RX_END_INT_RAW (BIT(4))
#define RMT_CH1_RX_END_INT_RAW_S 4
#define RMT_CH1_TX_END_INT_RAW (BIT(3))
#define RMT_CH1_TX_END_INT_RAW_S 3
#define RMT_CH0_ERR_INT_RAW (BIT(2))
#define RMT_CH0_ERR_INT_RAW_S 2
#define RMT_CH0_RX_END_INT_RAW (BIT(1))
#define RMT_CH0_RX_END_INT_RAW_S 1
#define RMT_CH0_TX_END_INT_RAW (BIT(0))
#define RMT_CH0_TX_END_INT_RAW_S 0

#define RMT_INT_ST_REG (REG_RMT_BASE + 0x0054)
#define RMT_CH3_TX_LOOP_INT_ST (BIT(19))
#define RMT_CH3_TX_LOOP_INT_ST_S 19
#define RMT_CH2_TX_LOOP_INT_ST (BIT(18))
#define RMT_CH2_TX_LOOP_INT_ST_S 18
#define RMT_CH1_TX_LOOP_INT_ST (BIT(17))
#define RMT_CH1_TX_LOOP_INT_ST_S 17
#define RMT_CH0_TX_LOOP_INT_ST (BIT(16))
#define RMT_CH0_TX_LOOP_INT_ST_S 16
#define RMT_CH3_TX_THR_EVENT_INT_ST (BIT(15))
#define RMT_CH3_TX_THR_EVENT_INT_ST_S 15
#define RMT_CH2_TX_THR_EVENT_INT_ST (BIT(14))
#define RMT_CH2_TX_THR_EVENT_INT_ST_S 14
#define RMT_CH1_TX_THR_EVENT_INT_ST (BIT(13))
#define RMT_CH1_TX_THR_EVENT_INT_ST_S 13
#define RMT_CH0_TX_THR_EVENT_INT_ST (BIT(12))
#define RMT_CH0_TX_THR_EVENT_INT_ST_S 12
#define RMT_CH3_ERR_INT_ST (BIT(11))
#define RMT_CH3_ERR_INT_ST_S 11
#define RMT_CH3_RX_END_INT_ST (BIT(10))
#define RMT_CH3_RX_END_INT_ST_S 10
#define RMT_CH3_TX_END_INT_ST (BIT(9))
#define RMT_CH3_TX_END_INT_ST_S 9
#define RMT_CH2_ERR_INT_ST (BIT(8))
#define RMT_CH2_ERR_INT_ST_S 8
#define RMT_CH2_RX_END_INT_ST (BIT(7))
#define RMT_CH2_RX_END_INT_ST_S 7
#define RMT_CH2_TX_END_INT_ST (BIT(6))
#define RMT_CH2_TX_END_INT_ST_S 6
#define RMT_CH1_ERR_INT_ST (BIT(5))
#define RMT_CH1_ERR_INT_ST_S 5
#define RMT_CH1_RX_END_INT_ST (BIT(4))
#define RMT_CH1_RX_END_INT_ST_S 4
#define RMT_CH1_TX_END_INT_ST (BIT(3))
#define RMT_CH1_TX_END_INT_ST_S 3
#define RMT_CH0_ERR_INT_ST (BIT(2))
#define RMT_CH0_ERR_INT_ST_S 2
#define RMT_CH0_RX_END_INT_ST (BIT(1))
#define RMT_CH0_RX_END_INT_ST_S 1
#define RMT_CH0_TX_END_INT_ST (BIT(0))
#define RMT_CH0_TX_END_INT_ST_S 0

#define RMT_INT_ENA_REG (REG_RMT_BASE + 0x0058)
#define RMT_CH3_TX_LOOP_INT_ENA (BIT(19))
#define RMT_CH3_TX_LOOP_INT_ENA_S 19
#define RMT_CH2_TX_LOOP_INT_ENA (BIT(18))
#define RMT_CH2_TX_LOOP_INT_ENA_S 18
#define RMT_CH1_TX_LOOP_INT_ENA (BIT(17))
#define RMT_CH1_TX_LOOP_INT_ENA_S 17
#define RMT_CH0_TX_LOOP_INT_ENA (BIT(16))
#define RMT_CH0_TX_LOOP_INT_ENA_S 16
#define RMT_CH3_TX_THR_EVENT_INT_ENA (BIT(15))
#define RMT_CH3_TX_THR_EVENT_INT_ENA_S 15
#define RMT_CH2_TX_THR_EVENT_INT_ENA (BIT(14))
#define RMT_CH2_TX_THR_EVENT_INT_ENA_S 14
#define RMT_CH1_TX_THR_EVENT_INT_ENA (BIT(13))
#define RMT_CH1_TX_THR_EVENT_INT_ENA_S 13
#define RMT_CH0_TX_THR_EVENT_INT_ENA (BIT(12))
#define RMT_CH0_TX_THR_EVENT_INT_ENA_S 12
#define RMT_CH3_ERR_INT_ENA (BIT(11))
#define RMT_CH3_ERR_INT_ENA_S 11
#define RMT_CH3_RX_END_INT_ENA (BIT(10))
#define RMT_CH3_RX_END_INT_ENA_S 10
#define RMT_CH3_TX_END_INT_ENA (BIT(9))
#define RMT_CH3_TX_END_INT_ENA_S 9
#define RMT_CH2_ERR_INT_ENA (BIT(8))
#define RMT_CH2_ERR_INT_ENA_S 8
#define RMT_CH2_RX_END_INT_ENA (BIT(7))
#define RMT_CH2_RX_END_INT_ENA_S 7
#define RMT_CH2_TX_END_INT_ENA (BIT(6))
#define RMT_CH2_TX_END_INT_ENA_S 6
#define RMT_CH1_ERR_INT_ENA (BIT(5))
#define RMT_CH1_ERR_INT_ENA_S 5
#define RMT_CH1_RX_END_INT_ENA (BIT(4))
#define RMT_CH1_RX_END_INT_ENA_S 4
#define RMT_CH1_TX_END_INT_ENA (BIT(3))
#define RMT_CH1_TX_END_INT_ENA_S 3
#define RMT_CH0_ERR_INT_ENA (BIT(2))
#define RMT_CH0_ERR_INT_ENA_S 2
#define RMT_CH0_RX_END_INT_ENA (BIT(1))
#define RMT_CH0_RX_END_INT_ENA_S 1
#define RMT_CH0_TX_END_INT_ENA (BIT(0))
#define RMT_CH0_TX_END_INT_ENA_S 0

#define RMT_INT_CLR_REG (REG_RMT_BASE + 0x005c)
#define RMT_CH3_TX_LOOP_INT_CLR (BIT(19))
#define RMT_CH3_TX_LOOP_INT_CLR_S 19
#define RMT_CH2_TX_LOOP_INT_CLR (BIT(18))
#define RMT_CH2_TX_LOOP_INT_CLR_S 18
#define RMT_CH1_TX_LOOP_INT_CLR (BIT(17))
#define RMT_CH1_TX_LOOP_INT_CLR_S 17
#define RMT_CH0_TX_LOOP_INT_CLR (BIT(16))
#define RMT_CH0_TX_LOOP_INT_CLR_S 16
#define RMT_CH3_TX_THR_EVENT_INT_CLR (BIT(15))
#define RMT_CH3_TX_THR_EVENT_INT_CLR_S 15
#define RMT_CH2_TX_THR_EVENT_INT_CLR (BIT(14))
#define RMT_CH2_TX_THR_EVENT_INT_CLR_S 14
#define RMT_CH1_TX_THR_EVENT_INT_CLR (BIT(13))
#define RMT_CH1_TX_THR_EVENT_INT_CLR_S 13
#define RMT_CH0_TX_THR_EVENT_INT_CLR (BIT(12))
#define RMT_CH0_TX_THR_EVENT_INT_CLR_S 12
#define RMT_CH3_ERR_INT_CLR (BIT(11))
#define RMT_CH3_ERR_INT_CLR_S 11
#define RMT_CH3_RX_END_INT_CLR (BIT(10))
#define RMT_CH3_RX_END_INT_CLR_S 10
#define RMT_CH3_TX_END_INT_CLR (BIT(9))
#define RMT_CH3_TX_END_INT_CLR_S 9
#define RMT_CH2_ERR_INT_CLR (BIT(8))
#define RMT_CH2_ERR_INT_CLR_S 8
#define RMT_CH2_RX_END_INT_CLR (BIT(7))
#define RMT_CH2_RX_END_INT_CLR_S 7
#define RMT_CH2_TX_END_INT_CLR (BIT(6))
#define RMT_CH2_TX_END_INT_CLR_S 6
#define RMT_CH1_ERR_INT_CLR (BIT(5))
#define RMT_CH1_ERR_INT_CLR_S 5
#define RMT_CH1_RX_END_INT_CLR (BIT(4))
#define RMT_CH1_RX_END_INT_CLR_S 4
#define RMT_CH1_TX_END_INT_CLR (BIT(3))
#define RMT_CH1_TX_END_INT_CLR_S 3
#define RMT_CH0_ERR_INT_CLR (BIT(2))
#define RMT_CH0_ERR_INT_CLR_S 2
#define RMT_CH0_RX_END_INT_CLR (BIT(1))
#define RMT_CH0_RX_END_INT_CLR_S 1
#define RMT_CH0_TX_END_INT_CLR (BIT(0))
#define RMT_CH0_TX_END_INT_CLR_S 0

#define RMT_CH0CARRIER_DUTY_REG (REG_RMT_BASE + 0x0060)
#define RMT_CARRIER_HIGH_CH0 0x0000FFFF
#define RMT_CARRIER_HIGH_CH0_S 16
#define RMT_CARRIER_LOW_CH0 0x0000FFFF
#define RMT_CARRIER_LOW_CH0_S 0

#define RMT_CH1CARRIER_DUTY_REG (REG_RMT_BASE + 0x0064)
#define RMT_CARRIER_HIGH_CH1 0x0000FFFF
#define RMT_CARRIER_HIGH_CH1_S 16
#define RMT_CARRIER_LOW_CH1 0x0000FFFF
#define RMT_CARRIER_LOW_CH1_S 0

#define RMT_CH2CARRIER_DUTY_REG (REG_RMT_BASE + 0x0068)
#define RMT_CARRIER_HIGH_CH2 0x0000FFFF
#define RMT_CARRIER_HIGH_CH2_S 16
#define RMT_CARRIER_LOW_CH2 0x0000FFFF
#define RMT_CARRIER_LOW_CH2_S 0

#define RMT_CH3CARRIER_DUTY_REG (REG_RMT_BASE + 0x006c)
#define RMT_CARRIER_HIGH_CH3 0x0000FFFF
#define RMT_CARRIER_HIGH_CH3_S 16
#define RMT_CARRIER_LOW_CH3 0x0000FFFF
#define RMT_CARRIER_LOW_CH3_S 0

#define RMT_CH0_TX_LIM_REG (REG_RMT_BASE + 0x0070)
#define RMT_LOOP_COUNT_RESET_CH0 (BIT(20))
#define RMT_LOOP_COUNT_RESET_CH0_S 20
#define RMT_TX_LOOP_CNT_EN_CH0 (BIT(19))
#define RMT_TX_LOOP_CNT_EN_CH0_S 19
#define RMT_TX_LOOP_NUM_CH0 0x000003FF
#define RMT_TX_LOOP_NUM_CH0_S 9
#define RMT_TX_LIM_CH0 0x000001FF
#define RMT_TX_LIM_CH0_S 0

#define RMT_CH1_TX_LIM_REG (REG_RMT_BASE + 0x0074)
#define RMT_LOOP_COUNT_RESET_CH1 (BIT(20))
#define RMT_LOOP_COUNT_RESET_CH1_S 20
#define RMT_TX_LOOP_CNT_EN_CH1 (BIT(19))
#define RMT_TX_LOOP_CNT_EN_CH1_S 19
#define RMT_TX_LOOP_NUM_CH1 0x000003FF
#define RMT_TX_LOOP_NUM_CH1_S 9
#define RMT_TX_LIM_CH1 0x000001FF
#define RMT_TX_LIM_CH1_S 0

#define RMT_CH2_TX_LIM_REG (REG_RMT_BASE + 0x0078)
#define RMT_LOOP_COUNT_RESET_CH2 (BIT(20))
#define RMT_LOOP_COUNT_RESET_CH2_S 20
#define RMT_TX_LOOP_CNT_EN_CH2 (BIT(19))
#define RMT_TX_LOOP_CNT_EN_CH2_S 19
#define RMT_TX_LOOP_NUM_CH2 0x000003FF
#define RMT_TX_LOOP_NUM_CH2_S 9
#define RMT_TX_LIM_CH2 0x000001FF
#define RMT_TX_LIM_CH2_S 0

#define RMT_CH3_TX_LIM_REG (REG_RMT_BASE + 0x007c)
#define RMT_LOOP_COUNT_RESET_CH3 (BIT(20))
#define RMT_LOOP_COUNT_RESET_CH3_S 20
#define RMT_TX_LOOP_CNT_EN_CH3 (BIT(19))
#define RMT_TX_LOOP_CNT_EN_CH3_S 19
#define RMT_TX_LOOP_NUM_CH3 0x000003FF
#define RMT_TX_LOOP_NUM_CH3_S 9
#define RMT_TX_LIM_CH3 0x000001FF
#define RMT_TX_LIM_CH3_S 0

#define RMT_APB_CONF_REG (REG_RMT_BASE + 0x0080)
#define RMT_MEM_TX_WRAP_EN (BIT(1))
#define RMT_MEM_TX_WRAP_EN_S 1
#define RMT_APB_FIFO_MASK (BIT(0))
#define RMT_APB_FIFO_MASK_S 0

#define RMT_TX_SIM_REG (REG_RMT_BASE + 0x0084)
#define RMT_TX_SIM_EN (BIT(4))
#define RMT_TX_SIM_EN_S 4
#define RMT_TX_SIM_CH3 (BIT(3))
#define RMT_TX_SIM_CH3_S 3
#define RMT_TX_SIM_CH2 (BIT(2))
#define RMT_TX_SIM_CH2_S 2
#define RMT_TX_SIM_CH1 (BIT(1))
#define RMT_TX_SIM_CH1_S 1
#define RMT_TX_SIM_CH0 (BIT(0))
#define RMT_TX_SIM_CH0_S 0

#define RMT_REF_CNT_RST_REG (REG_RMT_BASE + 0x0088)
#define RMT_REF_CNT_RST_CH3 (BIT(3))
#define RMT_REF_CNT_RST_CH3_S 3
#define RMT_REF_CNT_RST_CH2 (BIT(2))
#define RMT_REF_CNT_RST_CH2_S 2
#define RMT_REF_CNT_RST_CH1 (BIT(1))
#define RMT_REF_CNT_RST_CH1_S 1
#define RMT_REF_CNT_RST_CH0 (BIT(0))
#define RMT_REF_CNT_RST_CH0_S 0

#define RMT_DATE_REG (REG_RMT_BASE + 0x0fc)
#define RMT_DATE 0xFFFFFFFF
#define RMT_DATE_S 0
#define RMT_DATE_VERSION 0x18072600
