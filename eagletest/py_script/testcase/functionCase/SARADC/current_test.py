from baselib.test_channel.com import COM as com
from baselib.loglib.log_lib import *
from hal.Init import HALS
from hal.hwregister.hwreg.ESP32.RTC_CNTL import *
from hal.hwregister.hwreg.ESP32.SARADC import *

from rtclib.rtc import ULP_PARAM
from rtclib.rtc import WAKEUP_ENABLE
from rtclib.rtc import WAKEUP_REASON
import time

class CURRENT_TC(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.channel = channel
        self.chipv = chipv
        self.chip = HALS(self.channel, self.chipv)
        self.rtc_option0 = RTC_OPTIONS0(self.channel, self.chipv)
        self.rtc_bias_conf = RTC_BIAS_CONF(self.channel, self.chipv)
        self.rtc_sar_reg = SAR_START_FORCE(self.channel, self.chipv)
        self.rtc_reg = RTC_REG(self.channel, self.chipv)
        self.rtc_diag = RTC_DIAG0(self.channel, self.chipv)

        
    def deep_sleep_dis_all(self,timer_hi=0, timer_lo=0xeffff):
        self.chip.rtc_sleep.set_rtc_timer_wakeup(timer_hi, timer_lo)
        self.chip.rtc_sleep.sleep(0x3f, 8, 0)
        
    def deep_sleep_en_ulp(self):
#        self.chip.rtc_sleep.set_rtc_timer_wakeup(0, 0xeffff)
      #  self.rtc_bias_conf.reg_dbg_atten = dbg
        self.rtc_option0.reg_bias_core_folw_12m = 0
        self.rtc_option0.reg_bias_i2c_folw_12m = 1
        self.rtc_option0.reg_bias_sleep_folw_12m = 0


        self.chip.ulp.init()
        self.chip.ulp.movi(0, 0)
        self.chip.ulp.blr(5, 0x81)
        #self.chip.ulp.wakeup()
        #self.chip.ulp.end()  
        self.chip.ulp.end()
        self.chip.ulp.start(1)
        self.chip.rtc_sleep.sleep(0x2b, 0x200, 0) 
        
        
    def deep_sleep_en_saradc(self):
       # self.rtc_bias_conf.reg_dbg_atten = dbg
        self.rtc_option0.reg_bias_core_folw_12m = 1
        self.rtc_option0.reg_bias_i2c_folw_12m = 1
        self.rtc_option0.reg_bias_sleep_folw_12m = 1
        self.chip.ulp.init()
        self.chip.ulp.meas_adc0(0, 0)
        self.chip.ulp.blr(5000, 0x81)
        #self.chip.ulp.wakeup()
        #self.chip.ulp.end()  
        self.chip.ulp.end()
        self.chip.ulp.start(1)
        self.chip.rtc_sleep.sleep(0x2b, 0x200, 0) 
        
        
    def rtc_ulp_adc(self):
        addr_sleep = self.chip.HWREG.RTC_CNTL.RTC_DIAG0._RTC_DIAG0__addr
        #self.chip.rtc_debug.TOUCH_PAD2(1, 9, 1)
        #self.chip.rtc_debug.PDAC2(1, 9, 4)
        #self.chip.rtc_debug.TOUCH_PAD0(1, 9, 0)
        self.chip.ulp.init()
        #self.chip.ulp.movi(ULP_PARAM['R0'].value, 0x1234)
        self.rtc_bias_conf.reg_dbg_atten = 3
        
        self.rtc_option0.reg_bias_core_folw_12m = 0
        self.rtc_option0.reg_bias_i2c_folw_12m = 0
        self.rtc_option0.reg_bias_sleep_folw_12m = 1
        self.chip.ulp.set_ulp_slp_time(208)
        self.chip.adc2_arb.rtc_force()
        self.chip.rtc_adc2.config()
        if self.chipv == "CHIP722":
            self.chip.adc2_arb.rtc_force()
        self.chip.rtc_adc2.set(pad = 8, ulp = True)
        self.chip.MEM.wr(ULP_PARAM['RTC_MEM_DATA'].value,0x1)
        
        #self.chip.ulp.movi(ULP_PARAM['R2'].value, 0)
        self.chip.ulp.movi(ULP_PARAM['R3'].value,0)
        self.chip.ulp.ldr(addr_sleep, 22, 22)
        self.chip.ulp.movr(ULP_PARAM['R2'].value,ULP_PARAM['R0'].value)
        self.chip.ulp.lshi(ULP_PARAM['R2'].value, ULP_PARAM['R2'].value, 12)
        self.chip.ulp.ldm(ULP_PARAM['R0'].value, ULP_PARAM['R3'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.meas_adc1(ULP_PARAM['R1'].value, 8)
        self.chip.ulp.addr(ULP_PARAM['R1'].value, ULP_PARAM['R1'].value, ULP_PARAM['R2'].value)
        self.chip.ulp.bhr(200, 2)      
        self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R0'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        #self.chip.ulp.stm(ULP_PARAM['R0'].value, ULP_PARAM['R0'].value ,ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.addi(ULP_PARAM['R0'].value, ULP_PARAM['R0'].value, 1)
        self.chip.ulp.stm(ULP_PARAM['R0'].value, ULP_PARAM['R3'].value ,ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        #self.chip.ulp.addi(ULP_PARAM['R2'].value, ULP_PARAM['R2'].value, 1)       
        #self.chip.ulp.movr(ULP_PARAM['R0'].value, ULP_PARAM['R2'].value)
        #self.chip.ulp.blr(100, 0x89)

        #self.chip.ulp.stm(ULP_PARAM['R0'].value, ULP_PARAM['R3'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.blr(100, 2)
        self.chip.ulp.wakeup()
        self.chip.ulp.end()
        self.chip.ulp.start(1)
        self.chip.rtc_sleep.sleep(0x2b, 0x200, 0)
        
        
    
        

        

        

        

        
        
        
        


        
        
        

        
        
