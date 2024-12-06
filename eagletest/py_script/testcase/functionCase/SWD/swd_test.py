# -- coding: utf-8 --
from baselib.test_channel.com import COM as com
from baselib.loglib.log_lib import *
from hal.Init import HALS
from rtclib.rtc import RESET_CAUSE
from baselib.instrument.eps import eps

class SWD_TC_FUNC(object):
    def __init__(self, channel, chipv = "AUTO"):
        self.chip = HALS(channel, chipv)
        self.chipv = self.chip.chipv

    def tc000_send_int_test(self):
        self.chip.swd.swd_init()
        self.chip.swd.swd_int_clr()
        while(1):
            raw = int(self.chip.swd.swd_int_raw_sts())
            time.sleep(0.1)
            if raw:
                break
        self.chip.swd.swd_int_enable(1)
        sts0 = int(self.chip.swd.swd_int_sts())
        self.chip.swd.swd_int_enable(0)
        raw1 = int(self.chip.swd.swd_int_raw_sts())
        sts1 = int(self.chip.swd.swd_int_sts())
        self.chip.swd.swd_int_clr()
        raw2 = int(self.chip.swd.swd_int_raw_sts())
        if (1 != sts0) or (1 != raw1) or (0 != sts1) or (0 != raw2):
            logerror("fail, sts0: %d, raw1: %d, sts1: %d, raw2: %d\n"%(sts0, raw1, sts1, raw2))
            return logfail()
        return logpass()

    def tc001_swd_stop_test(self):
        '''
        SWD disable会关闭超时计数器时钟，永远都不会产生中断；
        '''
        self.chip.swd.swd_init()
        self.chip.swd.swd_stop()
        i = 0
        while(1):
            raw = int(self.chip.swd.swd_int_raw_sts())
            loginfo("raw[%d]: %d"%(i, raw))
            i = i + 1
            time.sleep(0.1)

    def tc002_feed_swd_test(self):
        self.chip.swd.swd_init(auto_feed = 0)
        while(1):
            swd_feed_int = int(self.chip.swd.get_swd_feed_int())
            time.sleep(0.1)
            loginfo("swd_feed_int: %d"%(swd_feed_int))
            if (swd_feed_int):
                break
        self.chip.swd.swd_feed()
        if int(self.chip.swd.get_swd_feed_int()):
            return logfail()
        else:
            return logpass()

    def tc003_reset_rtc_test(self):
        self.chip.swd.swd_init(auto_feed = 0)
        rst_flag0 = int(self.chip.swd.get_swd_reset_flag())
        while(1):
            reset_cause_str = filter(str.isdigit, self.chip.rtc.rtc_reset_cause())
            try:
                reset_cause = int(reset_cause_str)
                if reset_cause == RESET_CAUSE['SUPER_WD_RST'].value:
                    break
            except:
                loginfo("reset_cause_str: %s"%(reset_cause_str))
            time.sleep(0.1)
        rst_flag1 = int(self.chip.swd.get_swd_reset_flag())
        self.chip.swd.clr_swd_reset_flag()
        rst_flag2 = int(self.chip.swd.get_swd_reset_flag())
        if (0 == rst_flag0) and (1 == rst_flag1) and (0 == rst_flag2) and (reset_cause == RESET_CAUSE['SUPER_WD_RST'].value):
            return logpass()
        else:
            logerror("reset_cause: %d, rst_flag0: %d, rst_flag1: %d, rst_flag2: %d"%(reset_cause, rst_flag0, rst_flag1, rst_flag2))
            return logfail()

    def tc004_lock_test(self):
        self.chip.swd.swd_init(auto_feed = 0)
        while(1):
            swd_feed_int1 = int(self.chip.swd.get_swd_feed_int())
            loginfo("swd_feed_int1: %d"%(swd_feed_int1))
            if (swd_feed_int1):
                break
        self.chip.swd.swd_lock()
        self.chip.swd.swd_feed()
        swd_feed_int2 = int(self.chip.swd.get_swd_feed_int())
        self.chip.swd.swd_unlock()
        self.chip.swd.swd_feed()
        swd_feed_int3 = int(self.chip.swd.get_swd_feed_int())
        if (1 == swd_feed_int2) and (0 == swd_feed_int3):
            return logpass()
        else:
            logerror("swd_feed_int2: %d, swd_feed_int3: %d"%(swd_feed_int2, swd_feed_int3))
            return logfail()

    def tc005_ultra_low_voltage_test(self):
        self.eps = eps()
        self.eps.pwr(3.3, 1)
        time.sleep(0.15)
        self.chip.swd.clr_swd_reset_flag()
        swd_reset_flag0 = int(self.chip.swd.get_swd_reset_flag())
        loginfo("swd_reset_flag0: %d"%(swd_reset_flag0))
        self.chip.swd.swd_init(auto_feed = 1)
        for i in range(30):
            vdd33_value = 3.2 - i * 0.1
            self.eps.pwr(vdd33_value, 1)
            time.sleep(0.15)
            swd_rst_flag_str = self.chip.swd.get_swd_reset_flag()
            if ('0' != swd_rst_flag_str):#reset
                loginfo("when swd reset happen, VDD3P3_RTC is: %s"%(vdd33_value))
                time.sleep(3)
                self.eps.pwr(3.3, 1)
                time.sleep(0.15)
                reset_cause = int(self.chip.rtc.rtc_reset_cause())
                if reset_cause != RESET_CAUSE['SUPER_WD_RST'].value:
                    logerror("wrong reset_cause: %d"%(reset_cause))
                    return logfail()
                break
        if (29 == i):
            logerror("swd can not reset")
            return
        #测试芯片什么时候挂死
        for j in range(30):
            value = vdd33_value - j * 0.1
            if value < 0:
                logerror("chip can work when VDD3P3_RTC value is 0")
                return
            self.eps.pwr(value, 1)
            time.sleep(0.15)
            self.chip.swd.get_swd_reset_flag()
            loginfo("chip is alive when VDD3P3_RTC value is: %s"%(value))
