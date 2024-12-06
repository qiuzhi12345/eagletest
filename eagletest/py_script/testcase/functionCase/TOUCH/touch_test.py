from baselib.test_channel.com import COM as com
from baselib.loglib.log_lib import *
from hal.Init import HALS
from rtclib.rtc import WAKEUP_ENABLE
from rtclib.rtc import WAKEUP_REASON

class TOUCH_TC_FUNC(object):
    def __init__(self, channel, chipv = "AUTO"):
        self.chip = HALS(channel, chipv)
        self.chipv = self.chip.chipv

    def tc000_meas_en_test(self):
        touch_list = [0, 2 , 3, 4, 5, 6, 7, 8, 9]
        fail_num = 0
        self.chip.touch.touch_global_init()
        self.chip.touch.touch_clr_meas_en()
        for touch_no in touch_list:
            value1, value2 = 0, 0
            thres = 0
            meas_en = 0
            self.chip.touch.touch_init(touch_no)
            value1 = int(self.chip.touch.touch_read(touch_no))
            self.chip.touch.set_thres(touch_no, value1 / 2)
            thres =  int(self.chip.touch.get_thres(touch_no))
            loginfo("touch_no %d read_value: %d, thres is: %d"%(touch_no, value1, thres))
            while(1):
                time.sleep(1)
                touch_value = int(self.chip.touch.touch_read(touch_no))
                loginfo("touch_value: %d"%(touch_value))
                if touch_value < thres:
                    break
            meas_en = self.chip.touch.get_meas_en(touch_no)
            value2 = int(self.chip.touch.touch_read(touch_no))
            loginfo("value2: %d\n"%(value2))
            if (0 == meas_en):
                fail_num += 1
                logerror("touch_no: %d, meas_en: %d\n"%(touch_no, meas_en))
        if not fail_num:
            return logpass()
        else:
            return logfail()

    def tc001_int_test(self):
        touch_list = [0, 2, 3, 4, 5, 6, 7, 8, 9]
        fail_num = 0
        self.chip.touch.touch_global_init()
        for touch_no in touch_list:
            raw_sts0, raw_sts1, sts0, sts1, sts2 = 0, 0, 0
            value, thres= 0, 0
            self.chip.touch.touch_init(touch_no)
            self.chip.touch.clr_int()
            value = int(self.chip.touch.touch_read(touch_no))
            self.chip.touch.set_thres(touch_no, value / 2)
            thres =  int(self.chip.touch.get_thres(touch_no))
            loginfo("touch_no %d, read_value: %d, thres is: %d"%(touch_no, value, thres))
            while(1):
                time.sleep(1)
                touch_value = int(self.chip.touch.touch_read(touch_no))
                loginfo("touch_value: %d"%(touch_value))
                if touch_value < thres:
                    break
            raw_sts0 = int(self.chip.touch.get_int_raw_sts())
            if not raw_sts0:
                fail_num += 1
                logerror("fail, raw_sts0: %d when touch_no: %d"%(raw_sts0, touch_no))
            self.chip.touch.enable_int(0)
            sts0 = int(self.chip.touch.get_int_sts())
            self.chip.touch.enable_int(1)
            sts1 = int(self.chip.touch.get_int_sts())
            if sts0 or (not sts1):
                fail_num += 1
                logerror("fail, sts0: %d, sts1: %d, when touch_no: %d"%(sts0, sts1, touch_no))
            self.chip.touch.clr_int()
            raw_sts1 = int(self.chip.touch.get_int_raw_sts())
            sts2 = int(self.chip.touch.get_int_sts())
            if raw_sts1 or sts2:
                fail_num += 1
                logerror("fail, raw_sts1: %d, sts2: %d, when touch_no: %d"%(raw_sts1, sts2, touch_no))
        if not fail_num:
            return logpass()
        else:
            return logfail()

    def tc002_wakeup_test(self):
        touch_no = 0
        self.chip.touch.touch_global_init()
        self.chip.touch.touch_init(touch_no)
        value_str = self.chip.touch.touch_read(touch_no)
        value = int(value_str)
        self.chip.touch.set_thres(touch_no, value / 2)
        thres =  int(self.chip.touch.get_thres(touch_no))
        loginfo("touch_no %d: read_value: %d, thres is: %d"%(touch_no, value, thres))
        self.chip.touch.enable_int(1)
        self.chip.touch.enable_period_timer()
        self.chip.rtc_sleep.sleep(0x3f, WAKEUP_ENABLE['TOUCH_TRIG_EN'].value, 0)
        time.sleep(1)
        wakeup_cause = int(self.chip.rtc_sleep.wakeup_cause())
        if (wakeup_cause == WAKEUP_REASON['TOUCH_TRIG'].value):
            return logpass()
        else:
            return logfail()
