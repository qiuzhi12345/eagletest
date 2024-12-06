# -- coding: utf-8 --
from baselib.test_channel.com import COM as com
from baselib.loglib.log_lib import *
from hal.Init import HALS
from rtclib.rtc import ULP_PARAM
from rtclib.rtc import WAKEUP_ENABLE
from rtclib.rtc import WAKEUP_REASON
from rtclib.rtc import TSEN_LIB

class TSEN_TC_FUNC(object):
    def __init__(self, channel, chipv = "AUTO"):
        self.chip = HALS(channel, chipv)
        self.chipv = self.chip.chipv
        self.tsen_lib = TSEN_LIB(channel, self.chipv)

    def tc000_tsen_read_normalspeed(self):
        self.chip.rtc_clk.set_cpu_freq(1)
        self.chip.tsen.config()
        while(1):
            time.sleep(0.5)
            data = int(self.chip.tsen.read(), 16)
            loginfo("tmp data: 0x%x"%(data))

    def tc001_tsen_read_lowspeed(self):
        self.chip.tsen.config()
        time.sleep(1)
        data1 = int(self.chip.tsen.read(), 16)
        self.chip.rtc_clk.set_cpu_freq(4)
        time.sleep(2)
        data2 = int(self.chip.tsen.read(), 16)
        loginfo("data1: 0x%x, data2: 0x%x"%(data1, data2))
        if data2 <= data1:
            return logpass()
        else:
            return logfail()
        
    def tc002_tsen_read_deepsleep(self):
        self.chip.tsen.config()
        time.sleep(1)
        data1 = int(self.chip.tsen.read(), 16)
        self.tsen_lib.tsen_deepsleep_read(1)
        data2 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
        loginfo("data1: 0x%x, data2: 0x%x"%(data1, data2))
        if abs(data2 - data1) <= 2:
            return logpass()
        else:
            return logfail()

    def tc003_tsen_read_lightsleep(self):
        self.chip.tsen.config()
        time.sleep(1)
        data1 = int(self.chip.tsen.read(), 16)
        self.tsen_lib.tsen_lightsleep_read(1)
        data2 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
        loginfo("data1: 0x%x, data2: 0x%x"%(data1, data2))
        if abs(data2 - data1) <= 2:
            return logpass()
        else:
            return logfail()

    def tc004_tsen_read_wifiinit(self):
        self.chip.tsen.config()
        time.sleep(1)
        data1 = int(self.chip.tsen.read(), 16)
        self.chip.wifimac.mac_init()
        time.sleep(2)
        data2 = int(self.chip.tsen.read(), 16)
        loginfo("data1: 0x%x, data2: 0x%x"%(data1, data2))
        if data2 >= data1:
            return logpass()
        else:
            return logfail()

    def tc005_tsen_ulp_read_normalspeed(self):
        self.chip.rtc_clk.set_cpu_freq(1)
        self.chip.tsen.config(ulp = 1)
        self.chip.ulp.init()
        self.chip.ulp.movi(ULP_PARAM['R1'].value, 0)
        self.chip.ulp.tsens(ULP_PARAM['R2'].value, 10000)
        self.chip.ulp.stm(ULP_PARAM['R2'].value, ULP_PARAM['R1'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.end()
        self.chip.ulp.start(0)
        data = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
        loginfo("ulp read tmp: 0x%x\n"%(data))

    def tc006_tsen_close_test(self):
        '''给芯片加热或冷却时芯片温度值保持不变则验证成功'''
        self.chip.tsen.config()
        self.chip.tsen.close()
        while(1):
            time.sleep(0.5)
            data = int(self.chip.tsen.read(), 16)
            loginfo("tmp data: 0x%x"%(data))

    def tc007_tmp_value_test(self):
        tsen_min_value = 15
        tsen_max_value = 40
        if self.chipv == "CHIP722" or self.chipv == "CHIP723":
            offset = 0
            self.chip.tsen.config()
            time.sleep(1)
            data = int(self.chip.tsen.read(), 16)
            tmp = 0.4386 * data - 27.88 * offset - 20.52
            loginfo("data: 0x%x, tmp: %d"%(data, tmp))
            if tmp > tsen_min_value and tmp < tsen_max_value:
                return logpass()
            else:
                return logfail()

    def tc008_tsen_int_test(self):
        if self.chipv == "CHIP722" or self.chipv == "CHIP723":
            self.chip.tsen.config()
            self.chip.tsen.rtc_int_clr()
            self.chip.tsen.int_enable(0)
            while(1):
                data = int(self.chip.tsen.read(), 16)
                if data:
                    break
            raw0 = int(self.chip.tsen.rtc_int_raw())
            self.chip.tsen.rtc_int_clr()
            self.chip.tsen.int_enable(1)
            while(1):
                data = int(self.chip.tsen.read(), 16)
                if data:
                    break
            raw1 = int(self.chip.tsen.rtc_int_raw())
            self.chip.tsen.rtc_int_clr()
            raw2 = int(self.chip.tsen.rtc_int_raw())
            if (0 != raw0) or (1 != raw1) or (0 != raw2):
                loginfo("raw0: %d, raw1: %d, raw2: %d"%(raw0, raw1, raw2))
                return logfail()
            else:
                return logpass()
