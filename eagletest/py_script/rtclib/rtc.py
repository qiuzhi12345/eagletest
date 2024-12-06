import sys
from enum import Enum
from baselib.loglib.log_lib import *
from hal.Init import HALS

class RESET_CAUSE(Enum):
    NO_MEAN = 0
    POWERON_RESET = 1    # vbat power on reset
    SW_RESET = 3         # software reset digital core
    OWDT_RESET = 4       # legacy watch dog reset digital core
    DEEPSLEEP_RESET = 5  # deep sleep reset digital core
    SDIO_RESET = 6       # reset by slc module, reset digital core
    TG0WDT_SYS_RESET = 7 # Timer Group0 Watch Dog reset digital core
    TG1WDT_SYS_RESET = 8 # Timer Group1 Watch Dog reset digital core
    RTCWDT_SYS_RESET = 9 # RTC Watch Dog reset digital core
    INTRUSION_RESET = 10 # Intrusion tested to reset CPU
    TGWDT_CPU_RESET = 11 # Time Group Reset CPU 
    SW_CPU_RESET = 12    # Software reset CPU
    RTCWDT_CPU_RESET = 13        # RTC Watch Dog Reset CPU
    EXT_CPU_RESET = 14           # for APP CPU, reseted by PRO CPU
    RTCWDT_BROWN_OUT_RESET = 15  # Reset when the vdd voltage is not stable
    RTCWDT_RTC_RESET = 16        # RTC Watch Dog reset digital core and RTC module.
    SUPER_WD_RST = 18 # swd reset chip, delete from CHIP723


class WAKEUP_REASON(Enum):
    NO_SLEEP = 0
    EXT_EVENT0_TRIG = 1 #BIT0
    EXT_EVENT1_TRIG = 2 #BIT1
    GPIO_TRIG = 4       #BIT2
    TIMER_EXPIRE = 8    #BIT3
    SDIO_TRIG = 0x10      #BIT4
    MAC_TRIG = 0x20       #BIT5
    UART0_TRIG = 0x40     #BIT6
    UART1_TRIG = 0x80    #BIT7
    TOUCH_TRIG = 0x100    #BIT8
    SAR_TRIG = 0x200      #BIT9
    BT_TRIG = 0x400      #BIT10
    COCPU_TRIG = 0x800    #BIT11
    X32K_DEAD_TRIG = 0x1000    #BIT12
    COCPU_TRAP_TRIG = 0x2000   #BIT13
    USB_TRIG= 0x4000    #BIT14
    TOUCH_TIMEOUT_TRIG = 0x8000 #BIT15
    BROWN_OUT_TRIG = 0x10000    #BIT16


class WAKEUP_ENABLE(Enum):
    DISEN_WAKEUP = 0
    EXT_EVENT0_TRIG_EN = 1 #BIT0
    EXT_EVENT1_TRIG_EN = 2 #BIT1
    GPIO_TRIG_EN = 4       #BIT2
    TIMER_EXPIRE_EN = 8    #BIT3
    SDIO_TRIG_EN = 0x10      #BIT4
    MAC_TRIG_EN = 0x20       #BIT5
    UART0_TRIG_EN = 0x40     #BIT6
    UART1_TRIG_EN = 0x80    #BIT7
    TOUCH_TRIG_EN = 0x100    #BIT8
    SAR_TRIG_EN = 0x200      #BIT9
    BT_TRIG_EN = 0x400      #BIT10
    COCPU_TRIG_EN = 0x800    #BIT11
    X32K_DEAD_TRIG_EN = 0x1000    #BIT12
    COCPU_TRAP_TRIG_EN = 0x2000   #BIT13
    USB_TRIG_EN = 0x4000    #BIT14
    TOUCH_TIMEOUT_EN = 0x8000   #BIT15
    BROWN_OUT_EN = 0x10000      #BIT16


class ULP_PARAM(Enum):
    R0, R1, R2, R3 = 0, 1, 2, 3
    RTC_MEM_BASE = 0x60021000
    RTC_MEM_DATA_OFFSET = 512
    RTC_MEM_DATA = RTC_MEM_BASE + RTC_MEM_DATA_OFFSET * 4


class TSEN_LIB(object):
    def __init__(self, channel, chipv = "AUTO"):
        self.chip = HALS(channel, chipv)
        self.chipv = self.chip.chipv

    def tsen_2m_read(self, times):
        data_list = []
        self.chip.rtc_clk.set_cpu_freq(4)
        self.chip.tsen.config()
        for i in range(times):
            data = int(self.chip.tsen.read(), 16)
            data_list.append(data)
            time.sleep(0.01)
        return data_list

    def tsen_80m_read(self, times):
        data_list = []
        self.chip.rtc_clk.set_cpu_freq(1)
        self.chip.tsen.config()
        for i in range(times):
            data = int(self.chip.tsen.read(), 16)
            data_list.append(data)
            time.sleep(0.01)
        return data_list

    def tsen_wifiinit_read(self, times):
        data_list = []
        self.chip.rtc_clk.set_cpu_freq(1)
        self.chip.wifimac.mac_init()
        self.chip.tsen.config()
        for i in range(times):
            data = int(self.chip.tsen.read(), 16)
            data_list.append(data)
            time.sleep(0.01)
        return data_list

    def tsen_lightsleep_read(self, times):
        if self.chipv == "ESP32":
            lowpower_state_addr = self.chip.HWREG.RTC_CNTL.RTC_DIAG0._RTC_DIAG0__addr
        else:
            lowpower_state_addr = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__addr
            lowpower_state_lsb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_lsb
            lowpower_state_msb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_msb
            tsen_ctrl2_addr = self.chip.HWREG.SARADC.SAR_TSENS_CTRL2._SAR_TSENS_CTRL2__addr
            tsen_reset_lsb = self.chip.HWREG.SARADC.SAR_TSENS_CTRL2._SAR_TSENS_CTRL2__reg_tsens_reset_lsb
            tsen_reset_msb = self.chip.HWREG.SARADC.SAR_TSENS_CTRL2._SAR_TSENS_CTRL2__reg_tsens_reset_msb
        if self.chipv == "CHIP723":
            self.chip.HWREG.RTC_CNTL.RTC_ANA_CONF.reg_sar_i2c_force_pu = 1
        self.chip.rtc_clk.set_cpu_freq(1)
        self.chip.tsen.config(ulp = 1)
        self.chip.ulp.init()
        if self.chipv == "ESP32":
            self.chip.ulp.ldr(lowpower_state_addr, 19, 19)
            self.chip.ulp.blr(1, 8)
            self.chip.ulp.movr(ULP_PARAM['R0'].value, ULP_PARAM['R1'].value)
            self.chip.ulp.bhr(times, 5)
        elif self.chipv == "CHIP722":
            self.chip.ulp.ldr(lowpower_state_addr, lowpower_state_msb, lowpower_state_lsb)
            self.chip.ulp.blr(1, 10)
            self.chip.ulp.movr(ULP_PARAM['R0'].value, ULP_PARAM['R1'].value)
            self.chip.ulp.bhr(times, 7)
        else:
            self.chip.ulp.ldr(lowpower_state_addr, lowpower_state_msb, lowpower_state_lsb)
            self.chip.ulp.blr(1, 8)
            self.chip.ulp.movr(ULP_PARAM['R0'].value, ULP_PARAM['R1'].value)
            self.chip.ulp.bhr(times, 5)
        self.chip.ulp.tsens(ULP_PARAM['R2'].value, 10000)
        self.chip.ulp.stm(ULP_PARAM['R2'].value, ULP_PARAM['R1'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.addi(ULP_PARAM['R1'].value, ULP_PARAM['R1'].value, 1)
        if self.chipv == "CHIP722":
            self.chip.ulp.str(tsen_ctrl2_addr, tsen_reset_msb, tsen_reset_lsb, 1)
            self.chip.ulp.str(tsen_ctrl2_addr, tsen_reset_msb, tsen_reset_lsb, 0)
        self.chip.ulp.jmpi(2)
        self.chip.ulp.wakeup()
        self.chip.ulp.end()
        self.chip.ulp.start(1)
        self.chip.rtc_sleep.sleep(0, WAKEUP_ENABLE['SAR_TRIG_EN'].value, 0)
        time.sleep(1)
        wakeup_cause = int(self.chip.rtc_sleep.wakeup_cause())
        if (wakeup_cause == WAKEUP_REASON['SAR_TRIG'].value):
            return ULP_PARAM['RTC_MEM_DATA'].value
        else:
            logerror("wrong wakeup_cause: %d"%(wakeup_cause))
            sys.exit(-1)

    def tsen_deepsleep_read(self, times):
        if self.chipv == "ESP32":
            lowpower_state_addr = self.chip.HWREG.RTC_CNTL.RTC_DIAG0._RTC_DIAG0__addr
            slp_timer_en_addr = self.chip.HWREG.RTC_CNTL.RTC_STATE0._RTC_STATE0__addr
            slp_timer_en_lsb = self.chip.HWREG.RTC_CNTL.RTC_STATE0._RTC_STATE0__reg_sar_slp_timer_en_lsb
            slp_timer_en_msb = self.chip.HWREG.RTC_CNTL.RTC_STATE0._RTC_STATE0__reg_sar_slp_timer_en_msb
        else:
            lowpower_state_addr = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__addr
            lowpower_state_lsb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_lsb
            lowpower_state_msb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_msb
            tsen_ctrl2_addr = self.chip.HWREG.SARADC.SAR_TSENS_CTRL2._SAR_TSENS_CTRL2__addr
            tsen_reset_lsb = self.chip.HWREG.SARADC.SAR_TSENS_CTRL2._SAR_TSENS_CTRL2__reg_tsens_reset_lsb
            tsen_reset_msb = self.chip.HWREG.SARADC.SAR_TSENS_CTRL2._SAR_TSENS_CTRL2__reg_tsens_reset_msb
            slp_timer_en_addr = self.chip.HWREG.RTC_CNTL.RTC_ULP_CP_TIMER._RTC_ULP_CP_TIMER__addr
            slp_timer_en_lsb = self.chip.HWREG.RTC_CNTL.RTC_ULP_CP_TIMER._RTC_ULP_CP_TIMER__reg_ulp_cp_slp_timer_en_lsb
            slp_timer_en_msb = self.chip.HWREG.RTC_CNTL.RTC_ULP_CP_TIMER._RTC_ULP_CP_TIMER__reg_ulp_cp_slp_timer_en_msb
            rtc_timer2_addr = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__addr
            touch_start_wait_lsb = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__reg_ulpcp_touch_start_wait_lsb
            touch_start_wait_msb = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__reg_ulpcp_touch_start_wait_msb
            self.chip.MEM.wrm(rtc_timer2_addr, touch_start_wait_msb, touch_start_wait_lsb, 0x1ff)#default_value 16
        if self.chipv == "CHIP723":
            self.chip.HWREG.RTC_CNTL.RTC_ANA_CONF.reg_sar_i2c_force_pu = 1
        self.chip.rtc_clk.set_cpu_freq(1)
        self.chip.tsen.config(ulp = 1)
        self.chip.ulp.init()
        if self.chipv == "ESP32":
            self.chip.ulp.ldr(lowpower_state_addr, 19, 19)
            self.chip.ulp.blr(1, 9)
            self.chip.ulp.movr(ULP_PARAM['R0'].value, ULP_PARAM['R1'].value)
            self.chip.ulp.bhr(times, 5)
        elif self.chipv == "CHIP722":
            self.chip.ulp.ldr(lowpower_state_addr, lowpower_state_msb, lowpower_state_lsb)
            self.chip.ulp.blr(1, 11)
            self.chip.ulp.movr(ULP_PARAM['R0'].value, ULP_PARAM['R1'].value)
            self.chip.ulp.bhr(times, 7)
        else:
            self.chip.ulp.ldr(lowpower_state_addr, lowpower_state_msb, lowpower_state_lsb)
            self.chip.ulp.blr(1, 9)
            self.chip.ulp.movr(ULP_PARAM['R0'].value, ULP_PARAM['R1'].value)
            self.chip.ulp.bhr(times, 5)
        self.chip.ulp.tsens(ULP_PARAM['R2'].value, 10000)
        self.chip.ulp.stm(ULP_PARAM['R2'].value, ULP_PARAM['R1'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.addi(ULP_PARAM['R1'].value, ULP_PARAM['R1'].value, 1)
        if self.chipv == "CHIP722":
            self.chip.ulp.str(tsen_ctrl2_addr, tsen_reset_msb, tsen_reset_lsb, 1)
            self.chip.ulp.str(tsen_ctrl2_addr, tsen_reset_msb, tsen_reset_lsb, 0)
        self.chip.ulp.jmpi(2)
        self.chip.ulp.wakeup()
        self.chip.ulp.str(slp_timer_en_addr, slp_timer_en_msb, slp_timer_en_lsb, 0)
        self.chip.ulp.end()
        self.chip.ulp.start(1)
        self.chip.rtc_sleep.sleep(1, WAKEUP_ENABLE['SAR_TRIG_EN'].value, 0)
        time.sleep(1)
        wakeup_cause = int(self.chip.rtc_sleep.wakeup_cause())
        if (wakeup_cause == WAKEUP_REASON['SAR_TRIG'].value):
            return ULP_PARAM['RTC_MEM_DATA'].value
        else:
            logerror("wrong wakeup_cause: %d"%(wakeup_cause))
            sys.exit(-1)

class ADC_LIB(object):
    def __init__(self, channel, chipv = "AUTO"):
        self.chip = HALS(channel, chipv)
        self.chipv = self.chip.chipv

    def adc1_lightsleep_read(self, adc1_channel, times, atten_value):
        if self.chipv == "ESP32":
            lowpower_state_addr = self.chip.HWREG.RTC_CNTL.RTC_DIAG0._RTC_DIAG0__addr
        else:
            lowpower_state_addr = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__addr
            lowpower_state_lsb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_lsb
            lowpower_state_msb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_msb
        self.chip.rtc_adc1.config()
        self.chip.rtc_adc1.set(pad = adc1_channel, ulp = True, atten = atten_value)
        self.chip.ulp.init()
        if self.chipv == "CHIP722":
            self.chip.ulp.ldr(lowpower_state_addr, lowpower_state_msb, lowpower_state_lsb)
        else:
            self.chip.ulp.ldr(lowpower_state_addr, 19, 19)
        self.chip.ulp.blr(1, 8)
        self.chip.ulp.movr(ULP_PARAM['R0'].value, ULP_PARAM['R1'].value)
        self.chip.ulp.bhr(times, 5)
        if self.chipv == "CHIP722":
            self.chip.ulp.meas_adc0(ULP_PARAM['R2'].value, adc1_channel)
        else:
            self.chip.ulp.meas_adc0(ULP_PARAM['R2'].value, adc1_channel + 1)
        self.chip.ulp.stm(ULP_PARAM['R2'].value, ULP_PARAM['R1'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.addi(ULP_PARAM['R1'].value, ULP_PARAM['R1'].value, 1)
        self.chip.ulp.jmpi(2)
        self.chip.ulp.wakeup()
        self.chip.ulp.end()
        self.chip.ulp.start(1)
        self.chip.rtc_sleep.sleep(0, WAKEUP_ENABLE['SAR_TRIG_EN'].value, 0)
        time.sleep(2)
        wakeup_cause = int(self.chip.rtc_sleep.wakeup_cause())
        if (wakeup_cause == WAKEUP_REASON['SAR_TRIG'].value):
            return ULP_PARAM['RTC_MEM_DATA'].value
        else:
            logerror("wrong wakeup_cause: %d"%(wakeup_cause))
            sys.exit(-1)

    def adc1_deepsleep_read(self, adc1_channel, times, atten_value):
        if self.chipv == "ESP32":
            lowpower_state_addr = self.chip.HWREG.RTC_CNTL.RTC_DIAG0._RTC_DIAG0__addr
        else:
            lowpower_state_addr = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__addr
            lowpower_state_lsb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_lsb
            lowpower_state_msb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_msb
            rtc_timer2_addr = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__addr
            touch_start_wait_lsb = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__reg_ulpcp_touch_start_wait_lsb
            touch_start_wait_msb = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__reg_ulpcp_touch_start_wait_msb
            self.chip.MEM.wrm(rtc_timer2_addr, touch_start_wait_msb, touch_start_wait_lsb, 0x1ff)#default_value 16
        self.chip.rtc_adc1.config()
        self.chip.rtc_adc1.set(pad = adc1_channel, ulp = True, atten = atten_value)
        self.chip.ulp.init()
        if self.chipv == "CHIP722":
            self.chip.ulp.ldr(lowpower_state_addr, lowpower_state_msb, lowpower_state_lsb)
        else:
            self.chip.ulp.ldr(lowpower_state_addr, 19, 19)
        self.chip.ulp.blr(1, 8)
        self.chip.ulp.movr(ULP_PARAM['R0'].value, ULP_PARAM['R1'].value)
        self.chip.ulp.bhr(times, 5)
        if self.chipv == "CHIP722":
            self.chip.ulp.meas_adc0(ULP_PARAM['R2'].value, adc1_channel)
        else:
            self.chip.ulp.meas_adc0(ULP_PARAM['R2'].value, adc1_channel + 1)
        self.chip.ulp.stm(ULP_PARAM['R2'].value, ULP_PARAM['R1'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.addi(ULP_PARAM['R1'].value, ULP_PARAM['R1'].value, 1)
        self.chip.ulp.jmpi(2)
        self.chip.ulp.wakeup()
        self.chip.ulp.end()
        self.chip.ulp.start(1)
        self.chip.rtc_sleep.sleep(1, WAKEUP_ENABLE['SAR_TRIG_EN'].value, 0)
        time.sleep(2)
        wakeup_cause = int(self.chip.rtc_sleep.wakeup_cause())
        if (wakeup_cause == WAKEUP_REASON['SAR_TRIG'].value):
            return ULP_PARAM['RTC_MEM_DATA'].value
        else:
            logerror("wrong wakeup_cause: %d"%(wakeup_cause))
            sys.exit(-1)

    def adc2_lightsleep_read(self, adc2_channel, times, atten_value):
        if self.chipv == "ESP32":
            lowpower_state_addr = self.chip.HWREG.RTC_CNTL.RTC_DIAG0._RTC_DIAG0__addr
        else:
            lowpower_state_addr = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__addr
            lowpower_state_lsb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_lsb
            lowpower_state_msb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_msb
            sar_meas2_mux_addr = self.chip.HWREG.SARADC.SAR_MEAS2_MUX._SAR_MEAS2_MUX__addr
            rtc_force_lsb = self.chip.HWREG.SARADC.SAR_MEAS2_MUX._SAR_MEAS2_MUX__reg_sar2_rtc_force_lsb
            rtc_force_msb = self.chip.HWREG.SARADC.SAR_MEAS2_MUX._SAR_MEAS2_MUX__reg_sar2_rtc_force_msb
        self.chip.rtc_adc2.config()
        self.chip.rtc_adc2.set(pad = adc2_channel, ulp = True, atten = atten_value)
        #if self.chipv == "CHIP722":
        #    self.chip.adc2_arb.rtc_force()
        self.chip.ulp.init()
        if self.chipv == "CHIP722":
            self.chip.ulp.ldr(lowpower_state_addr, lowpower_state_msb, lowpower_state_lsb)
        else:
            self.chip.ulp.ldr(lowpower_state_addr, 19, 19)
        self.chip.ulp.blr(1, 9)
        if self.chipv == "CHIP722":
            self.chip.ulp.str(sar_meas2_mux_addr, rtc_force_msb, rtc_force_lsb, 1)
        self.chip.ulp.movr(ULP_PARAM['R0'].value, ULP_PARAM['R1'].value)
        self.chip.ulp.bhr(times, 5)
        if self.chipv == "CHIP722":
            self.chip.ulp.meas_adc1(ULP_PARAM['R2'].value, adc2_channel)
        else:
            self.chip.ulp.meas_adc1(ULP_PARAM['R2'].value, adc2_channel + 1)
        self.chip.ulp.stm(ULP_PARAM['R2'].value, ULP_PARAM['R1'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.addi(ULP_PARAM['R1'].value, ULP_PARAM['R1'].value, 1)
        self.chip.ulp.jmpi(2)
        self.chip.ulp.wakeup()
        self.chip.ulp.end()
        self.chip.ulp.start(1)
        self.chip.rtc_sleep.sleep(0, WAKEUP_ENABLE['SAR_TRIG_EN'].value, 0)
        time.sleep(2)
        wakeup_cause = int(self.chip.rtc_sleep.wakeup_cause())
        if (wakeup_cause == WAKEUP_REASON['SAR_TRIG'].value):
            return ULP_PARAM['RTC_MEM_DATA'].value
        else:
            logerror("wrong wakeup_cause: %d"%(wakeup_cause))
            sys.exit(-1)

    def adc2_deepsleep_read(self, adc2_channel, times, atten_value):
        if self.chipv == "ESP32":
            lowpower_state_addr = self.chip.HWREG.RTC_CNTL.RTC_DIAG0._RTC_DIAG0__addr
        else:
            lowpower_state_addr = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__addr
            lowpower_state_lsb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_lsb
            lowpower_state_msb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_msb
            sar_meas2_mux_addr = self.chip.HWREG.SARADC.SAR_MEAS2_MUX._SAR_MEAS2_MUX__addr
            rtc_force_lsb = self.chip.HWREG.SARADC.SAR_MEAS2_MUX._SAR_MEAS2_MUX__reg_sar2_rtc_force_lsb
            rtc_force_msb = self.chip.HWREG.SARADC.SAR_MEAS2_MUX._SAR_MEAS2_MUX__reg_sar2_rtc_force_msb
        self.chip.rtc_adc2.config()
        self.chip.rtc_adc2.set(pad = adc2_channel, ulp = True, atten = atten_value)
        #if self.chipv == "CHIP722":
        #    self.chip.adc2_arb.rtc_force()
        self.chip.ulp.init()
        if self.chipv == "CHIP722":
            self.chip.ulp.ldr(lowpower_state_addr, lowpower_state_msb, lowpower_state_lsb)
        else:
            self.chip.ulp.ldr(lowpower_state_addr, 19, 19)
        self.chip.ulp.blr(1, 9)
        if self.chipv == "CHIP722":
            self.chip.ulp.str(sar_meas2_mux_addr, rtc_force_msb, rtc_force_lsb, 1)
        self.chip.ulp.movr(ULP_PARAM['R0'].value, ULP_PARAM['R1'].value)
        self.chip.ulp.bhr(times, 5)
        if self.chipv == "CHIP722":
            self.chip.ulp.meas_adc1(ULP_PARAM['R2'].value, adc2_channel)
        else:
            self.chip.ulp.meas_adc1(ULP_PARAM['R2'].value, adc2_channel + 1)
        self.chip.ulp.stm(ULP_PARAM['R2'].value, ULP_PARAM['R1'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.addi(ULP_PARAM['R1'].value, ULP_PARAM['R1'].value, 1)
        self.chip.ulp.jmpi(2)
        self.chip.ulp.wakeup()
        self.chip.ulp.end()
        self.chip.ulp.start(1)
        self.chip.rtc_sleep.sleep(1, WAKEUP_ENABLE['SAR_TRIG_EN'].value, 0)
        time.sleep(2)
        wakeup_cause = int(self.chip.rtc_sleep.wakeup_cause())
        if (wakeup_cause == WAKEUP_REASON['SAR_TRIG'].value):
            return ULP_PARAM['RTC_MEM_DATA'].value
        else:
            logerror("wrong wakeup_cause: %d"%(wakeup_cause))
            sys.exit(-1)
