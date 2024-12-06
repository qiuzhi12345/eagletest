from baselib.test_channel.com import COM as com
from baselib.loglib.log_lib import *
from hal.Init import HALS
from rtclib.rtc import RESET_CAUSE
from baselib.instrument.eps import eps

class RTC_BROWNOUT_TC_FUNC(object):
    def __init__(self, channel, chipv = "AUTO"):
        self.chip = HALS(channel, chipv)
        self.chipv = self.chip.chipv

    def tc000_close_rf_test(self):
        '''
        test current.
        '''
        self.eps = eps()
        self.eps.pwr(3.3, 1)
        time.sleep(0.5)
        self.chip.rtc_debug.TOUCH_PAD2(0, 31, 0)
        if self.chipv == "ESP32":
            self.chip.rtc_clk.set_cpu_freq(1)
            self.chip.wifimac.mac_init()
        elif self.chipv == "CHIP722":

            self.chip.power.open_rf()
            time.sleep(1)
            self.chip.rtc_clk.set_cpu_freq(5)
        self.chip.rtc_brownout.enable(1)
        if self.chipv == "CHIP722":
            self.chip.HWI2C.ulp.dbrown_out_thres = 7
        else:
            self.chip.rtc_brownout.thres_set(7)
        self.chip.rtc_brownout.pdrf_enable(1)
        for i in range(15):
            vdd33_value = 3.3 - i * 0.1
            self.eps.pwr(vdd33_value, 1)
            time.sleep(1)

    def tc001_int_test(self, thres):
        '''
        thres set from 0 to 7, record brownout voltage
        '''
        self.eps = eps()
        self.eps.pwr(3.3, 1)
        time.sleep(1)
        self.chip.rtc_debug.TOUCH_PAD2(0, 31, 0)
        self.chip.rtc_brownout.int_clr()
        raw0 = int(self.chip.rtc_brownout.int_raw())
        if raw0:
            logerror("wrong, brownout int generate when vdd voltage is 3.3v")
            return logfail()
        self.chip.rtc_brownout.enable(1)
        self.chip.rtc_brownout.reset_enable(0)
        self.chip.rtc_brownout.int_enable(0)
        if self.chipv == "CHIP722":
            self.chip.HWI2C.ulp.dbrown_out_thres = thres
        else:
            self.chip.rtc_brownout.thres_set(thres)
        for i in range(15):
            vdd33_value = 3.2 - i * 0.1
            self.eps.pwr(vdd33_value, 1)
            time.sleep(1)
            raw1 = int(self.chip.rtc_brownout.int_raw())
            if raw1:
                loginfo("brownout int generage when vdd value is: %.1f"%(vdd33_value))
                break
        if raw1:
            sts1 = int(self.chip.rtc_brownout.int_sts())
            self.chip.rtc_brownout.int_enable(1)
            sts2 = int(self.chip.rtc_brownout.int_sts())
            raw2 = int(self.chip.rtc_brownout.int_clr())
            if (0 == sts1) and (1 == sts2) and (0 == raw2):
                return logpass()
            else:
                logerror("sts1: %d, sts2: %d, raw2: %d"%(sts1, sts2, raw2))
                return logfail()
        else:
            return logfail()

    def tc002_reset_rtc_test(self, thres):
        '''
        thres set from 0 to 7, record brownout voltage
        '''
        self.eps = eps()
        self.eps.pwr(3.3, 1)
        time.sleep(0.5)
        if self.chipv == "CHIP722":
            self.chip.rtc_debug.TOUCH_PAD5(0, 0, 3)#pull out RROWNOUT_DET signal
        loginfo("begin pull debug signal")
        default_reset_cause = int(self.chip.rtc.rtc_reset_cause())
        if (RESET_CAUSE['RTCWDT_BROWN_OUT_RESET'].value == default_reset_cause):
            logerror("wrong default_reset_cause: 0x%x"%(default_reset_cause))
            return
        self.chip.rtc_brownout.enable(enable = 1)
        self.chip.rtc_brownout.reset_enable(rst_en = 1)
        self.chip.rtc_brownout.int_enable(1)
        if self.chipv == "CHIP722":
            self.chip.HWI2C.ulp.dbrown_out_thres = thres
        else:
            self.chip.rtc_brownout.thres_set(thres)
        for i in range(15):
            vdd33_value = 3.2 - i * 0.1
            self.eps.pwr(vdd33_value, 1)
            time.sleep(0.5)
            try:
                reset_cause = int(self.chip.rtc.rtc_reset_cause())
            except:
                time.sleep(3)
                self.chip.rtc.rtc_reset_cause()#sometimes when reset chip, it did not succeed the first time, so add this code.
                reset_cause = int(self.chip.rtc.rtc_reset_cause())
            if reset_cause == RESET_CAUSE['RTCWDT_BROWN_OUT_RESET'].value:
                break;
        if (reset_cause == RESET_CAUSE['RTCWDT_BROWN_OUT_RESET'].value):
            logpass()
        else:
            logfail()

    def tc003_close_flash_test(self):
        '''
        test current.
        '''
        self.eps = eps()
        self.eps.pwr(3.3, 1)
        self.chip.rtc_brownout.enable(1)
        if self.chipv == "CHIP722":
            self.chip.HWI2C.ulp.dbrown_out_thres = 7
        else:
            self.chip.rtc_brownout.thres_set(7)
        self.chip.rtc_brownout.close_flash_enable(1)
        for i in range(15):
            vdd33_value = 3.3 - i * 0.1
            self.eps.pwr(vdd33_value, 1)
            time.sleep(2)
        return logpass()

    def tc004_start_chip_lowest_voltage(self):
        return logpass()

    def tc005_int_thres_test(self):
        return logpass()

    def tc006_reset_thres_test(self):
        return logpass()
