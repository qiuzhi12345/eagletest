from baselib.test_channel.com import COM as com
from baselib.loglib.log_lib import *
from hal.Init import HALS

class CLOCK_TC_FUNC(object):
    def __init__(self, channel, chipv = "AUTO"):
        self.chip = HALS(channel, chipv)
        self.chipv = self.chip.chipv

    def tc000_cpu_freq_test(self): 
        sleepTime = 5
        fail_num = 0
        self.chip.rtc_clk.set_cpu_freq(1)
        self.chip.rtc_clk.timegroup_timer0_enable()
        self.chip.rtc_clk.update_timergroup_timer0()
        time0_lo = int(self.chip.rtc_clk.read_timergroup_timer0_low())
        time0_hi = int(self.chip.rtc_clk.read_timergroup_timer0_high())
        time.sleep(sleepTime)
        self.chip.rtc_clk.update_timergroup_timer0()
        time1_lo = int(self.chip.rtc_clk.read_timergroup_timer0_low())
        time1_hi = int(self.chip.rtc_clk.read_timergroup_timer0_high())
        cur_freq1_lo = time1_lo - time0_lo
        cur_freq1_hi = time1_hi - time0_hi
        cpu_freq0 = 2 * (long(cur_freq1_hi << 32) + cur_freq1_lo) / (1000000 * sleepTime)
        if 80 != cpu_freq0:
            fail_num += 1
            logerror("cur_cpu_freq1_lo: %d, cur_cpu_freq1_hi: %d, cpu_freq0: %dM\n"%(cur_freq1_lo, cur_freq1_hi, cpu_freq0))
        self.chip.rtc_clk.set_cpu_freq(0)
        self.chip.rtc_clk.update_timergroup_timer0()
        time2_lo = int(self.chip.rtc_clk.read_timergroup_timer0_low())
        time2_hi = int(self.chip.rtc_clk.read_timergroup_timer0_high())
        time.sleep(sleepTime)
        self.chip.rtc_clk.update_timergroup_timer0()
        time3_lo = int(self.chip.rtc_clk.read_timergroup_timer0_low())
        time3_hi = int(self.chip.rtc_clk.read_timergroup_timer0_high())
        set_freq_lo0 = time3_lo - time2_lo
        set_freq_hi0 = time3_hi - time2_hi
        cpu_freq1 = 2 *(long(set_freq_hi0 << 32) + set_freq_lo0) / (1000000 * sleepTime)
        if 40 != cpu_freq1:
            fail_num += 1
            logerror("set_freq_lo0: %d, set_freq_hi0: %d, cpu_freq1: %dM\n"%(set_freq_lo0, set_freq_hi0, cpu_freq1))
        self.chip.rtc_clk.set_cpu_freq(4)
        self.chip.rtc_clk.update_timergroup_timer0()
        time4_lo = int(self.chip.rtc_clk.read_timergroup_timer0_low())
        time4_hi = int(self.chip.rtc_clk.read_timergroup_timer0_high())
        time.sleep(sleepTime)
        self.chip.rtc_clk.update_timergroup_timer0()
        time5_lo = int(self.chip.rtc_clk.read_timergroup_timer0_low())
        time5_hi = int(self.chip.rtc_clk.read_timergroup_timer0_high())
        set_freq_lo1 = time5_lo - time4_lo
        set_freq_hi1 = time5_hi - time4_hi
        cpu_freq2 = 2* (long(set_freq_hi1 << 32) + set_freq_lo1) / (1000000 * sleepTime)
        self.chip.rtc_clk.set_cpu_freq(1)
        if 2 != cpu_freq2:
            fail_num += 1
            logerror("set_freq_lo1: %d, set_freq_hi1: %d, cpu_freq2: %dM\n"%(set_freq_lo1, cur_freq1_hi, cpu_freq2))
        if fail_num:
            return logfail()
        else:
            return logpass()

    def tc001_rtc_cal_32k_test(self):
        period1 = int(self.chip.rtc_clk.get_clk_calibration(2))
        if self.chipv == "ESP32":
            self.chip.rtc_clk.set_32k(dac = 1, dres = 3, dbias = 0)
            self.chip.rtc_clk.help_starting_32k()
        else:
            self.chip.rtc_clk.set_32k()
        self.chip.rtc_clk.start_32k(1)
        time.sleep(1)
        try:
            period2 = int(self.chip.rtc_clk.get_clk_calibration(2))
            loginfo("32k disable period: 0x%x, enable period: 0x%x"%(period1, period2))
            # 1000000 / (period2 >> 19)
            freq = (1000000 << 19) / period2
            loginfo("32k freq: %d"%(freq))
            #error is within 2/10000
            if (0 == period1) and ((freq >= 32761) and (freq <= 32775)):
                return logpass()
            else:
                return logfail()
        except:
            logerror("x32k period is 0")
            return logfail()

    def tc002_rtc_cal_8MD256_test(self):
        period1 = int(self.chip.rtc_clk.get_clk_calibration(1))
        self.chip.rtc_clk.clk_8m_en(1, 1)
        period2 = int(self.chip.rtc_clk.get_clk_calibration(1))
        loginfo("8M D256 disable period: 0x%x, enable period: 0x%x"%(period1, period2))
        # 1000000 / (period2 >> 19)
        freq = (1000000 << 19) / period2
        loginfo("8M D256 freq: %d"%(freq))
        if (self.chipv == "ESP32"): 
            if (0 == period1) and ((freq >= 28515) and (freq <= 36329)):
                return logpass()
        else:
            if (0 == period1) and ((freq >= 30625) and (freq <= 33437)):
                return logpass()

    def tc003_rtc_cal_150k_test(self):
        period = int(self.chip.rtc_clk.get_clk_calibration(0))
        # 1000000 / (period >> 19)
        freq = (1000000 << 19) / period
        loginfo("150k freq: %d"%(freq))
        if (freq >= 140000) and (freq <= 170000):
            return logpass()
        else:
            return logfail()

    def tc004_8MD256_disable_timeout_test(self):
        self.chip.rtc_clk.clk_8m_en(clk_8m_en = 1, d256_en = 1)
        period1 = int(self.chip.rtc_clk.get_clk_calibration(1))
        if self.chipv == "ESP32":
            self.chip.rtc_clk.clk_8m_en(clk_8m_en = 1, d256_en = 0)
        else:
            self.chip.rtc_clk.clk_8m_en(clk_8m_en = 0, d256_en = 0)
        period2 = int(self.chip.rtc_clk.get_clk_calibration(1))
        loginfo("enable period: 0x%x, disable period: 0x%x"%(period1, period2))
        if (0 != period1) and (0 == period2):
            return logpass()
        else:
            return logfail()

    def tc005_32k_disable_timeout_test(self):
        if self.chipv == "ESP32":
            self.chip.rtc_clk.set_32k(dac = 1, dres = 3, dbias = 0)
            self.chip.rtc_clk.help_starting_32k()
        else:
            self.chip.rtc_clk.set_32k()
        self.chip.rtc_clk.start_32k(1)
        time.sleep(1)
        period1 = int(self.chip.rtc_clk.get_clk_calibration(2))
        self.chip.rtc_clk.start_32k(0)
        period2 = int(self.chip.rtc_clk.get_clk_calibration(2))
        loginfo("enable period: 0x%x, disable period: 0x%x"%(period1, period2))
        if (0 != period1) and (0 == period2):
            return logpass()
        else:
            return logfail()

    def tc006_x32k_help_work_test(self):
        if self.chipv == "ESP32":
            self.chip.rtc_clk.set_32k(dac = 1, dres = 3, dbias = 0)
        else:
            self.chip.rtc_clk.set_32k()
        self.chip.rtc_clk.start_32k(1)
        time1 = time.time()
        while(1):
            period = int(self.chip.rtc_clk.get_clk_calibration(2))
            if period:
                break
        time2 = time.time()
        delayTime1 = time2 - time1
        self.chip.rtc_clk.start_32k(0)
        period = int(self.chip.rtc_clk.get_clk_calibration(2))
        if period:
            return logfail()
        self.chip.rtc_clk.help_starting_32k()
        self.chip.rtc_clk.start_32k(1)
        time3 = time.time()
        while(1):
            period = int(self.chip.rtc_clk.get_clk_calibration(2))
            if period:
                break
        time4 = time.time()
        delayTime2 = time4 - time3
        loginfo("delayTime2: %f, delayTime1: %f"%(delayTime2, delayTime1))
        if delayTime2 < delayTime1:
            return logpass()
        else:
            return logfail()

    def tc007_rtc_cal_thres_timeout_test(self):
        return logpass()

    def tc008_rtc_cal_period_test(self):
        return logpass()
        
    def tc009_x32k_startup_time_scan(self, dbuf_list = [0, 1], dac_list = [0, 1, 2, 3, 4, 5, 6, 7], dres_list = [0, 1, 2, 3, 4, 5, 6, 7]):
        '''
        this testcase is only used for chip722
        '''
        from baselib.loglib.log_csv import csvreport as csvreport
        self.log = csvreport('/x32k_scan_startup_time/%s' % time.strftime('%y_%m_%d'))
        for dbuf in dbuf_list:
            for dac in dac_list:
                for dres in dres_list:
                    time_str = self.chip.rtc_clk.x32k_startup_time(dbuf, dac, dres, dac)
                    times = filter(str.isdigit, time_str)
                    self.log.write_value('dbuf%d_dac%d_dres%d_dgm%d' % (dbuf, dac, dres, dac), times)
                    loginfo(times)
                    self.chip.rtc_clk.start_32k(0)
                    self.chip.rtc_wdt.wdt_unlock()
                    self.chip.rtc_wdt.wdt_stg_hold_len(0, 0xffff)
                    self.chip.rtc_wdt.wdt_stg_act(0, 5)
                    self.chip.rtc_wdt.wdt_init()
                    time.sleep(4)
                    self.chip.rtc_wdt.wdt_stop()
        self.log.flush_line()
