from baselib.test_channel.com import COM as com
from baselib.loglib.log_lib import *
from hal.Init import HALS
from rtclib.rtc import RESET_CAUSE 

class RTC_WDT_TC_FUNC(object):
    def __init__(self, channel, chipv = "AUTO"):
        self.chip = HALS(channel, chipv)
        self.chipv = self.chip.chipv

    def tc000_send_int_test(self):
        fail_num = 0
        self.chip.rtc_wdt.wdt_unlock()
        clr_raw_sts = int(self.chip.rtc_wdt.wdt_int_clr())
        if (clr_raw_sts):
            logerror("fail, clr_sts0: %d\n"%(clr_raw_sts))
            fail_num += 1
        self.chip.rtc_wdt.wdt_stg_hold_len(0, 0xffff)
        self.chip.rtc_wdt.wdt_stg_act(0, 1)
        self.chip.rtc_wdt.wdt_init()
        if self.chipv == "ESP32":
            time.sleep(1)
        else:
            time.sleep(2.5)
        raw_sts1 = int(self.chip.rtc_wdt.wdt_int_raw_sts())
        if not raw_sts1:
            logerror("fail, raw_sts1: %d\n"%(raw_sts1))
            fail_num += 1
        else:
            self.chip.rtc_wdt.wdt_int_enable(1)
            sts0 = int(self.chip.rtc_wdt.wdt_int_sts())
            self.chip.rtc_wdt.wdt_int_enable(0)
            sts1 = int(self.chip.rtc_wdt.wdt_int_sts())
            if (1 != sts0) or (0 != sts1):
                logerror("fail, sts0: %d, sts1: %d\n"%(sts0, sts1)) 
                fail_num += 1
        if not fail_num:
            return logpass()
        else:
            return logfail()
       
    def tc001_reset_cpu_test(self):
        self.chip.rtc_wdt.wdt_unlock()
        self.chip.rtc_wdt.wdt_stg_hold_len(0, 0xffff)
        loginfo("tc001_reset_cpu_test begin\n")
        self.chip.rtc_wdt.wdt_stg_act(0, 2)
        self.chip.rtc_wdt.wdt_init()
        if self.chipv == "ESP32":
            time.sleep(1)
        else:
            time.sleep(3.5)
        reset_cause = int(self.chip.rtc.rtc_reset_cause())
        loginfo("reset_cause: %d\n"%(reset_cause))
        if (reset_cause == RESET_CAUSE['RTCWDT_CPU_RESET'].value):
            return logpass()
        else:
            return logfail()
       
    def tc002_reset_system_test(self):
        self.chip.rtc_wdt.wdt_unlock()
        self.chip.rtc_wdt.wdt_stg_hold_len(0, 0xffff)
        self.chip.rtc_wdt.wdt_stg_act(0, 3)
        self.chip.rtc_wdt.wdt_init()
        if self.chipv == "ESP32":
            time.sleep(1)
        else:
            time.sleep(3.5)
        reset_cause = int(self.chip.rtc.rtc_reset_cause())
        loginfo("reset_cause: %d\n"%(reset_cause))
        if (reset_cause == RESET_CAUSE['RTCWDT_SYS_RESET'].value):
            return logpass()
        else:
            return logfail()
    
    def tc003_reset_rtc_test(self):
        self.chip.rtc_wdt.wdt_unlock()
        self.chip.rtc_wdt.wdt_stg_hold_len(0, 0xffff)
        self.chip.rtc_wdt.wdt_stg_act(0, 4)
        self.chip.rtc_wdt.wdt_init()
        if self.chipv == "ESP32":
            time.sleep(1)
        else:
            time.sleep(3.5)
        reset_cause = int(self.chip.rtc.rtc_reset_cause())
        loginfo("reset_cause: %d\n"%(reset_cause))
        if (reset_cause == RESET_CAUSE['RTCWDT_RTC_RESET'].value):
            return logpass()
        else:
            return logfail()
    
    def tc004_feed_wdt_test(self):
        self.chip.rtc_wdt.wdt_unlock()
        self.chip.rtc_wdt.wdt_stg_hold_len(0, 0xffff)#about 8ms
        self.chip.rtc_wdt.wdt_stg_act(0, 3)
        self.chip.rtc_wdt.wdt_init()
        default_reset_value = int(self.chip.rtc.rtc_reset_cause())
        for i in range(100):
            time.sleep(0.05)
            self.chip.rtc_wdt.wdt_feed()
            i +=1
        reset_cause1 = int(self.chip.rtc.rtc_reset_cause())
        if self.chipv == "ESP32":
            time.sleep(1)
        else:
            time.sleep(3.5)
        reset_cause2 = int(self.chip.rtc.rtc_reset_cause())
        loginfo("default_reset_value: %d, reset_cause1 when feed wdt: %d, reset_cause2 when no feed wdt: %d\n"%(default_reset_value, reset_cause1, reset_cause2))
        if self.chipv == "ESP32":
            if (RESET_CAUSE['RTCWDT_SYS_RESET'].value == reset_cause2) and ((RESET_CAUSE['POWERON_RESET'].value == default_reset_value) or (RESET_CAUSE['RTCWDT_RTC_RESET'].value == default_reset_value))\
                    and ((RESET_CAUSE['POWERON_RESET'].value == reset_cause1) or (RESET_CAUSE['RTCWDT_RTC_RESET'].value == reset_cause1)):
                return logpass()
            else:
                return logfail()
        else:
            if (RESET_CAUSE['RTCWDT_SYS_RESET'].value != reset_cause2) or (RESET_CAUSE['POWERON_RESET'].value != default_reset_value) or (RESET_CAUSE['POWERON_RESET'].value != reset_cause1):
                return logfail()
            else:
                return logpass()

    def tc005_lock_test(self):
        default_reset_cause = int(self.chip.rtc.rtc_reset_cause())
        self.chip.rtc_wdt.wdt_unlock()
        self.chip.rtc_wdt.wdt_lock()
        self.chip.rtc_wdt.wdt_stg_hold_len(0, 0xff)
        self.chip.rtc_wdt.wdt_stg_act(0, 3)
        self.chip.rtc_wdt.wdt_init()
        if self.chipv == "CHIP722":
            time.sleep(3.5)
        else:
            time.sleep(1)
        reset_cause = int(self.chip.rtc.rtc_reset_cause())
        loginfo("reset_cause: %d\n"%(reset_cause))
        if ((default_reset_cause == RESET_CAUSE['POWERON_RESET'].value) and (reset_cause == RESET_CAUSE['RTCWDT_SYS_RESET'].value)):
            return logfail()
        else:
            return logpass()

    def tc006_reset_chip_test(self):
        if self.chipv == "CHIP722" or self.chipv == "CHIP723":
            self.chip.rtc_wdt.wdt_unlock()
            self.chip.rtc_wdt.wdt_stg_hold_len(0, 0xffff)
            self.chip.rtc_wdt.wdt_stg_act(0, 5)
            self.chip.rtc_wdt.wdt_init()
            time.sleep(3.5)
            reset_cause = int(self.chip.rtc.rtc_reset_cause())
            loginfo("reset_cause: %d\n"%(reset_cause))
            if (reset_cause == RESET_CAUSE['POWERON_RESET'].value):
                return logpass()
            else:
                return logfail()
        else:
            logerror("This type of chip has no the function of reset chip")
            return logpass()
        
