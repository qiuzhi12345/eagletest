from baselib.test_channel.com import COM as com
from baselib.loglib.log_lib import *
from hal.Init import HALS
from rtclib.rtc import WAKEUP_REASON

class RTC_TIMER_TC_FUNC(object):
    def __init__(self, channel, chipv = "AUTO"):
        self.chip = HALS(channel, chipv)
        self.chipv = self.chip.chipv

    def tc000_rtc_timer_test(self):

        self.chip.rtc_timer.update_time()
        low1 = int(self.chip.rtc_timer.get_time_low())
        high1 = int(self.chip.rtc_timer.get_time_high())
        self.chip.rtc_timer.update_time()
        low2 = int(self.chip.rtc_timer.get_time_low())
        high2 = int(self.chip.rtc_timer.get_time_high())
        loginfo("low1: %d, high1: %d"%(low1, high1))  
        loginfo("low2:  %d, high2:  %d"%(low2, high2))
        if ((high1 == high2) and (low1 >= low2)) or (high1 > high2):
            return logfail()
        else:
            return logpass()

    def tc001_rtc_timer_valid_int_test(self):
        if self.chipv == "ESP32" or self.chipv == "CHIP722":
            fail_num = 0
            self.chip.rtc_timer.clr_valid_int()
            self.chip.rtc_timer.update_time()
            valid_int_raw0 = int(self.chip.rtc_timer.get_valid_int_raw_sts())
            if (1 != valid_int_raw0):
                fail_num += 1
                logerror("fail, valid_int_raw0: %d"%(valid_int_raw0))
            self.chip.rtc_timer.enable_valid_int(0)
            valid_int_sts0 = int(self.chip.rtc_timer.get_valid_int_sts())
            self.chip.rtc_timer.enable_valid_int(1)
            valid_int_sts1 = int(self.chip.rtc_timer.get_valid_int_sts())
            if (0 != valid_int_sts0) or (1 != valid_int_sts1):
                fail_num += 1
                logerror("fail, valid_int_sts0: %d, valid_int_sts1: %d\n"%(valid_int_sts0, valid_int_sts1))
            self.chip.rtc_timer.clr_valid_int()
            valid_int_raw1 = int(self.chip.rtc_timer.get_valid_int_raw_sts())
            valid_int_sts2 = int(self.chip.rtc_timer.get_valid_int_sts())
            if (0 != valid_int_raw1) or (0 != valid_int_sts2):
                fail_num += 1
                logerror("fail, valid_int_raw1: %d, valid_int_sts2: %d\n"%(valid_int_raw1, valid_int_sts2))
            if (0 != fail_num):
                return logfail()
            else:
                return logpass()

    def tc002_rtc_timer_int_test(self):
        fail_num = 0
        if self.chipv == "ESP32" or self.chipv == "CHIP722":
            self.chip.rtc_timer.enable_alarm(1)
            self.chip.rtc_timer.clr_int()
            time.sleep(1)
            raw0 = int(self.chip.rtc_timer.get_int_raw_sts())
            if (1 != raw0):
                fail_num += 1
                logerror("fail, raw0: %d\n"%(raw0))
            self.chip.rtc_timer.enable_int(0)
            sts0 = int(self.chip.rtc_timer.get_int_sts())
            self.chip.rtc_timer.enable_int(1)
            sts1 = int(self.chip.rtc_timer.get_int_sts())
            if (0 != sts0) or (1 != sts1):
                fail_num += 1
                logerror("fail, sts0: %d, sts1: %d"%(sts0, sts1))
            self.chip.rtc_timer.enable_alarm(0)
            self.chip.rtc_timer.clr_int()
            raw1 = int(self.chip.rtc_timer.get_int_raw_sts())
            sts2 = int(self.chip.rtc_timer.get_int_sts())
            if (0 != raw1) or (0 != sts2):
                fail_num += 1
                logerror("fail, raw1: %d, sts2: %d"%(raw1, sts2))
            if (0 != fail_num):
                return logfail()
            else:
                return logpass()
        else:
            self.chip.rtc_timer.enable_alarm(0)
            raw0 = int(self.chip.rtc_timer.get_int_raw_sts())
            self.chip.rtc_timer.enable_alarm(1)
            raw1 = int(self.chip.rtc_timer.get_int_raw_sts())
            self.chip.rtc_timer.clr_int()
            raw2 = int(self.chip.rtc_timer.get_int_raw_sts())
            self.chip.rtc_timer.enable_alarm(1)
            raw3 = int(self.chip.rtc_timer.get_int_raw_sts())
            if (0 != raw0) or (1 != raw1) or (0 != raw2) or (1 != raw3):
                logerror("raw0: %d, raw1: %d, raw2: %d, raw3: %d"%(raw0, raw1, raw2, raw3))
                return logfail()
            else:
                self.chip.rtc_timer.enable_int(0)
                sts0 = int(self.chip.rtc_timer.get_int_sts())
                self.chip.rtc_timer.enable_int(1)
                sts1 = int(self.chip.rtc_timer.get_int_sts())
                if (0 != sts0) or (1 != sts1):
                    logerror("sts0: %d, sts1: %d"%(sts0, sts1))
                    return logfail()
                self.chip.rtc_timer.clr_int()
                raw4 = int(self.chip.rtc_timer.get_int_raw_sts())
                sts2 = int(self.chip.rtc_timer.get_int_sts())
                if (0 != raw4) or (0 != sts2):
                    logerror("raw4: %d, sts2: %d"%(raw4, sts2))
                    return logfail()
                return logpass()

    def tc003_alarm_wakeup_test(self, slp_mode):
        self.chip.rtc_sleep.rtc_timer_wakeup(0, 0x1000)
        self.chip.rtc_sleep.sleep(slp_mode, 8, 0)
        time.sleep(1)
        wakeup_cause = int(self.chip.rtc_sleep.wakeup_cause())
        if (wakeup_cause == WAKEUP_REASON['TIMER_EXPIRE'].value):
            return logpass()
        else:
            return logfail()

    def tc004_sleep_time_test(self, dig_gpio = 6):
        #self.chip.rtc_debug.TOUCH_PAD7(0, 13, 3)#xtl_buf_wait, for c testcase
        #self.chip.rtc_debug.TOUCH_PAD10(0, 15, 1)#clk_8m_wait, for c testcase
        #self.chip.rtc_timer.rtc_slp_time_test(slow_clk_sel, sleep_time_us, dig_gpio)#for c testcase
        #return
        if self.chipv == "CHIP722" or self.chipv == "CHIP723":
            slow_clk_sel_list = [0, 1]
            sleep_time_us_list = [8000, 40000, 80000]
            max_error_value = 5
            fail_num = 0
            self.chip.rtc_clk.timegroup_timer0_enable()
            self.chip.rtc_clk.update_timergroup_timer0()
            time0_lo = int(self.chip.rtc_clk.read_timergroup_timer0_low())
            time0_hi = int(self.chip.rtc_clk.read_timergroup_timer0_high())
            time.sleep(1)
            self.chip.rtc_clk.update_timergroup_timer0()
            time1_lo = int(self.chip.rtc_clk.read_timergroup_timer0_low())
            time1_hi = int(self.chip.rtc_clk.read_timergroup_timer0_high())
            cur_freq1_lo = time1_lo - time0_lo
            cur_freq1_hi = time1_hi - time0_hi
            cpu_freq = 2 * (long(cur_freq1_hi << 32) + cur_freq1_lo) / 1000000
            loginfo("cpu_freq: %dM"%(cpu_freq))
            for slow_clk_sel in slow_clk_sel_list:
                for sleep_time_us in sleep_time_us_list:
                    if slow_clk_sel == 0:
                        period = int(self.chip.rtc_clk.get_clk_calibration(0))
                    elif slow_clk_sel == 1:
                        self.chip.rtc_clk.set_32k()
                        self.chip.rtc_clk.start_32k(1)
                        time.sleep(1)
                        period = int(self.chip.rtc_clk.get_clk_calibration(2))
                    elif slow_clk_sel == 2:
                        self.chip.rtc_clk.clk_8m_en(1, 1)
                        self.chip.HWREG.RTC_CNTL.RTC_CLK_CONF.reg_ck8m_force_pu = 1
                        time.sleep(1)
                        period = int(self.chip.rtc_clk.get_clk_calibration(1))
                    else:
                        logerror("wrong slow_clk_sel: %d"%(slow_clk_sel))
                        return
                    self.chip.rtc_clk.rtc_slow_clk_select(slow_clk_sel)
                    xtl_buf_wait_cycle = self.chip.HWREG.RTC_CNTL.RTC_TIMER1.xtl_buf_wait
                    cycle_str = self.chip.rtc_clk.conv_us_to_slowclk(sleep_time_us, period)
                    cycle_list = cycle_str.split(',')
                    low_slp = int(cycle_list[0])
                    high_slp = int(cycle_list[1])
                    self.chip.rtc_timer.xtl_off()
                    self.chip.rtc_sleep.rtc_timer_wakeup(high_slp, low_slp)
                    timeGP0 = self.chip.rtc_clk.read_timergroup_timer0()
                    time0 = time.time()
                    self.chip.rtc_sleep.sleep(0, 8, 0)
                    timeGP1 = self.chip.rtc_clk.read_timergroup_timer0()
                    time1 = time.time()
                    slp_time_ms = int(self.chip.rtc_timer.get_slp_time(period))/1000.0
                    pythonTime_ms = (time1 - time0) * 1000
                    timeGP0_list = timeGP0.split(',')
                    timeGP1_list = timeGP1.split(',')
                    timeGP_ms = 1000.0*(int(timeGP1_list[1]) - int(timeGP0_list[1]))/(cpu_freq*1024*1024)
                    xtl_buf_wait_ms = int(self.chip.rtc_clk.conv_slowclk_to_us(xtl_buf_wait_cycle, period))/1000.0
                    loginfo("pythonTime_ms: %f, timeGP_ms: %f, slp_time_ms: %f, xtl_buf_wait_ms: %f"%(pythonTime_ms, timeGP_ms, slp_time_ms, xtl_buf_wait_ms))
                    error = pythonTime_ms - (timeGP_ms + slp_time_ms + xtl_buf_wait_ms)
                    loginfo("error is : %f, abs(error): %f"%(error, abs(error)))
                    if abs(error) >= max_error_value:
                        logerror("error is: %f when slow_clk_sel[%d] and sleep_time_us[%d]"%(error, slow_clk_sel, sleep_time_us))
                        fail_num += 1
            if fail_num:
                return logfail()
            else:
                return logpass()
  
    def tc005_rtc_timer_int_handler_test(self, sleep_time_us):
        if self.chipv == "CHIP723":
            period = int(self.chip.rtc_clk.get_clk_calibration(0))
            cycle_str = self.chip.rtc_clk.conv_us_to_slowclk(sleep_time_us, period)
            cycle_list = cycle_str.split(',')
            low_slp = int(cycle_list[0])
            high_slp = int(cycle_list[1])
            print_str = self.chip.rtc_timer.rtc_timer_int_handler(high_slp, low_slp)
            if (print_str == "rtc_timer_int_handler_success"):
                return logpass()
            else:
                return logfail()
