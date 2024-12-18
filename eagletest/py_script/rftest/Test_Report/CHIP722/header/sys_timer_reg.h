
#define SYSTIMER_CONF_REG (REG_SYSTIMER_BASE + 0x0000)
#define SYSTIMER_CLK_EN (BIT(31))
#define SYSTIMER_CLK_EN_S 31
#define SYSTIMER_CLK_FO (BIT(0))
#define SYSTIMER_CLK_FO_S 0

#define SYSTIMER_LOAD_REG (REG_SYSTIMER_BASE + 0x0004)
#define SYSTIMER_TIMER_LOAD (BIT(31))
#define SYSTIMER_TIMER_LOAD_S 31

#define SYSTIMER_LOAD_HI_REG (REG_SYSTIMER_BASE + 0x0008)
#define SYSTIMER_TIMER_LOAD_HI 0xFFFFFFFF
#define SYSTIMER_TIMER_LOAD_HI_S 0

#define SYSTIMER_LOAD_LO_REG (REG_SYSTIMER_BASE + 0x000C)
#define SYSTIMER_TIMER_LOAD_LO 0xFFFFFFFF
#define SYSTIMER_TIMER_LOAD_LO_S 0

#define SYSTIMER_STEP_REG (REG_SYSTIMER_BASE + 0x0010)
#define SYSTIMER_TIMER_PLL_STEP 0x000003FF
#define SYSTIMER_TIMER_PLL_STEP_S 10
#define SYSTIMER_TIMER_XTAL_STEP 0x000003FF
#define SYSTIMER_TIMER_XTAL_STEP_S 0

#define SYSTIMER_TARGET0_HI_REG (REG_SYSTIMER_BASE + 0x0014)
#define SYSTIMER_TIMER_TARGET0_HI 0xFFFFFFFF
#define SYSTIMER_TIMER_TARGET0_HI_S 0

#define SYSTIMER_TARGET0_LO_REG (REG_SYSTIMER_BASE + 0x0018)
#define SYSTIMER_TIMER_TARGET0_LO 0xFFFFFFFF
#define SYSTIMER_TIMER_TARGET0_LO_S 0

#define SYSTIMER_TARGET1_HI_REG (REG_SYSTIMER_BASE + 0x001C)
#define SYSTIMER_TIMER_TARGET1_HI 0xFFFFFFFF
#define SYSTIMER_TIMER_TARGET1_HI_S 0

#define SYSTIMER_TARGET1_LO_REG (REG_SYSTIMER_BASE + 0x0020)
#define SYSTIMER_TIMER_TARGET1_LO 0xFFFFFFFF
#define SYSTIMER_TIMER_TARGET1_LO_S 0

#define SYSTIMER_TARGET2_HI_REG (REG_SYSTIMER_BASE + 0x0024)
#define SYSTIMER_TIMER_TARGET2_HI 0xFFFFFFFF
#define SYSTIMER_TIMER_TARGET2_HI_S 0

#define SYSTIMER_TARGET2_LO_REG (REG_SYSTIMER_BASE + 0x0028)
#define SYSTIMER_TIMER_TARGET2_LO 0xFFFFFFFF
#define SYSTIMER_TIMER_TARGET2_LO_S 0

#define SYSTIMER_TARGET0_CONF_REG (REG_SYSTIMER_BASE + 0x002C)
#define SYSTIMER_TARGET0_WORK_EN (BIT(31))
#define SYSTIMER_TARGET0_WORK_EN_S 31
#define SYSTIMER_TARGET0_PERIOD_MODE (BIT(30))
#define SYSTIMER_TARGET0_PERIOD_MODE_S 30
#define SYSTIMER_TARGET0_PERIOD 0x3FFFFFFF
#define SYSTIMER_TARGET0_PERIOD_S 0

#define SYSTIMER_TARGET1_CONF_REG (REG_SYSTIMER_BASE + 0x0030)
#define SYSTIMER_TARGET1_WORK_EN (BIT(31))
#define SYSTIMER_TARGET1_WORK_EN_S 31
#define SYSTIMER_TARGET1_PERIOD_MODE (BIT(30))
#define SYSTIMER_TARGET1_PERIOD_MODE_S 30
#define SYSTIMER_TARGET1_PERIOD 0x3FFFFFFF
#define SYSTIMER_TARGET1_PERIOD_S 0

#define SYSTIMER_TARGET2_CONF_REG (REG_SYSTIMER_BASE + 0x0034)
#define SYSTIMER_TARGET2_WORK_EN (BIT(31))
#define SYSTIMER_TARGET2_WORK_EN_S 31
#define SYSTIMER_TARGET2_PERIOD_MODE (BIT(30))
#define SYSTIMER_TARGET2_PERIOD_MODE_S 30
#define SYSTIMER_TARGET2_PERIOD 0x3FFFFFFF
#define SYSTIMER_TARGET2_PERIOD_S 0

#define SYSTIMER_UPDATE_REG (REG_SYSTIMER_BASE + 0x0038)
#define SYSTIMER_TIMER_UPDATE (BIT(31))
#define SYSTIMER_TIMER_UPDATE_S 31
#define SYSTIMER_TIMER_VALUE_VALID (BIT(30))
#define SYSTIMER_TIMER_VALUE_VALID_S 30

#define SYSTIMER_VALUE_HI_REG (REG_SYSTIMER_BASE + 0x003C)
#define SYSTIMER_TIMER_VALUE_HI 0xFFFFFFFF
#define SYSTIMER_TIMER_VALUE_HI_S 0

#define SYSTIMER_VALUE_LO_REG (REG_SYSTIMER_BASE + 0x0040)
#define SYSTIMER_TIMER_VALUE_LO 0xFFFFFFFF
#define SYSTIMER_TIMER_VALUE_LO_S 0

#define SYSTIMER_INT_ENA_REG (REG_SYSTIMER_BASE + 0x0044)
#define SYSTIMER_INT2_ENA (BIT(2))
#define SYSTIMER_INT2_ENA_S 2
#define SYSTIMER_INT1_ENA (BIT(1))
#define SYSTIMER_INT1_ENA_S 1
#define SYSTIMER_INT0_ENA (BIT(0))
#define SYSTIMER_INT0_ENA_S 0

#define SYSTIMER_INT_RAW_REG (REG_SYSTIMER_BASE + 0x0048)
#define SYSTIMER_INT2_RAW (BIT(2))
#define SYSTIMER_INT2_RAW_S 2
#define SYSTIMER_INT1_RAW (BIT(1))
#define SYSTIMER_INT1_RAW_S 1
#define SYSTIMER_INT0_RAW (BIT(0))
#define SYSTIMER_INT0_RAW_S 0

#define SYSTIMER_INT_CLR_REG (REG_SYSTIMER_BASE + 0x004C)
#define SYSTIMER_INT2_CLR (BIT(2))
#define SYSTIMER_INT2_CLR_S 2
#define SYSTIMER_INT1_CLR (BIT(1))
#define SYSTIMER_INT1_CLR_S 1
#define SYSTIMER_INT0_CLR (BIT(0))
#define SYSTIMER_INT0_CLR_S 0

#define SYSTIMER_DATE_REG (REG_SYSTIMER_BASE + 0x00fc)
#define SYSTIMER_DATE 0xFFFFFFFF
#define SYSTIMER_DATE_S 0
#define SYSTIMER_DATE_VERSION 0x1807160
