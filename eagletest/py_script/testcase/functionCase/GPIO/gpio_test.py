from baselib.loglib.log_lib import *
from hal.Init import HALS
from rtclib.rtc import WAKEUP_ENABLE
from rtclib.rtc import WAKEUP_REASON

class GPIO_TC_FUNC(object):
    def __init__(self, channel, chipv = "AUTO"):
        self.chip = HALS(channel, chipv)
        self.chipv = self.chip.chipv
  
    def tc000_rtc_gpio_test(self, channel):
        '''
        ESP32:
            test rtc_gpio_no[6~17] can both be as input gpio and output gpio.
            need two device: devece1, device2, rtc_gpio_no[n] in device1 connected to
            rtc_gpio_no[n] in device2, n from 6->17.
        CHIP722: rtc_gpio_no[0~21]
        '''
        chip1 = HALS(channel)
        if self.chipv == "ESP32":
            '''
            In ESP32:
            1) no rtc gpio pad 8, 9 in test board
            2) rtc gpio pad 6, 11, 12, 15 should not connected to other board, otherwise chip can not power up for CI test.
            '''
            #rtc_gpio_no_list = range(6, 18)
            rtc_gpio_no_list = [7, 10, 13, 14, 16, 17]
        else:
            rtc_gpio_no_list = range(22)
        self.chip.gpio.rtc_gpio_hangup_all()
        chip1.gpio.rtc_gpio_hangup_all()
        fail_num = 0
        for out_value in range(2):
            for rtc_out_no in rtc_gpio_no_list:
                in_value = 0
                rtc_in_no = rtc_out_no
                chip1.gpio.rtc_gpio_out(rtc_out_no, out_value)
                in_value = int(self.chip.gpio.rtc_gpio_in(rtc_in_no))
                if (in_value != out_value):
                    logerror("error, rtc_out_no: %d, in_value:%d, out_value: %d\n"%(rtc_out_no, in_value, out_value))
                    fail_num += 1
            if fail_num:
                logerror("fail_num is: %d when out_value = %d\n"%(fail_num, out_value))
        if not fail_num:
            return logpass()
        else:
            return logfail()
    
    def tc001_only_in_rtc_gpio_test(self):
        if self.chipv == "ESP32":
            '''
            test rtc_gpio_no[0~5] can only as input gpio. RTC_GPIO_NO[0~5] connected to RTC_GPIO_NO[12~17], RTC_GPIO_NO[12~17] are as out_put no,
            output VALUE, if RTC_GPIO_NO[0~5] in_put value is equal VALUE, test pass.
            '''
            #rtc_gpio_in_no_list =  range(6), rtc_gpio_out_no_list = range(12, 18)
            rtc_gpio_in_no_list =  [0,  1,  2,  4,  5]
            rtc_gpio_out_no_list = [12, 13, 14, 16, 17]
            fail_num = 0
            for out_value in range(2):
                for i in range(len(rtc_gpio_in_no_list)):
                    in_value = 0
                    self.chip.gpio.rtc_gpio_out(rtc_gpio_out_no_list[i], out_value)
                    in_value = int(self.chip.gpio.rtc_gpio_in(rtc_gpio_in_no_list[i]))
                    if (in_value != out_value):
                        logerror("in_value: %d, out_value: %d, rtc_gpio_in_no: %d, rtc_gpio_out_no: %d\n"%(in_value, out_value, rtc_gpio_in_no_list[i], rtc_gpio_out_no_list[i]))
                        fail_num += 1
                if fail_num:
                    logerror("fail_num is: %d when out_value = %d\n"%(fail_num, out_value))
            if not fail_num:
                return logpass()
            else:
                return logfail()

    def tc002_dig_gpio_test(self, channel):
        '''
        test dig_gpio_no[0~23,25~27, 32~33] can both be as input gpio and output gpio.
        need two device: devece1, device2, dig_gpio_no[n] in device1 connected to
        dig_gpio_no[n] in device2, n from 0->23 or 25~27 or 32~33.
        CHIP722: dig_gpio_no: 0~21, 26~45
        '''
        chip1 = HALS(channel)
        if self.chipv == "ESP32":
            '''
            In ESP32:
            1) no pad 20, 32, 32 in test board
            2) pad 0, 1, 2, 3, 6, 8, 10, 11, 12, 25 should not connected to other board, otherwise chip can not power up for CI test.
            3) pad 7 should not connected to other board, otherwise chip can not auto-detected flash size.
            '''
            #dig_gpio_no_list = range(24) + range(25, 28) + range(32, 34)
            dig_gpio_no_list = range(13, 20) + [4, 5, 9, 21, 22, 23] + range(26, 28)
        else:
            dig_gpio_no_list = range(22) + range(26, 46)
        self.chip.gpio.dig_gpio_hangup_all()
        chip1.gpio.dig_gpio_hangup_all()
        fail_num = 0
        for out_value in range(2):
            for dig_out_no in dig_gpio_no_list:
                in_value = 0
                dig_in_no = dig_out_no
                chip1.gpio.dig_gpio_out(dig_out_no, out_value)
                in_value = int(self.chip.gpio.dig_gpio_in(dig_in_no))
                if (in_value != out_value):
                    logerror("error, dig_out_no: %d, in_value:%d, out_value: %d\n"%(dig_out_no, in_value, out_value))
                    fail_num += 1
            if fail_num:
                logerror("fail_num is: %d when out_value = %d\n"%(fail_num, out_value))
        if not fail_num:
            return logpass()
        else:
            return logfail()

    def tc003_only_in_dig_gpio_test(self):
        '''test dig_gpio_in_no can only as input gpio. dig_gpio_in_no connected
            to dig_gpio_out_no, dig_gpio_out_no are as out_put no, output VALUE,
            if dig_gpio_in_no input value is equal VALUE, test pass.
        '''
        if self.chipv == "ESP32":
            #dig_gpio_in_no_list =  range(34, 40)
            #dig_gpio_out_no_list = [14, 27, 2, 15, 13, 12]
            dig_gpio_in_no_list =  [34, 35, 36, 37, 38]
            dig_gpio_out_no_list = [14, 27, 2, 15, 13]
        else:
            dig_gpio_in_no_list =  [46]
            dig_gpio_out_no_list = [18]
        fail_num = 0
        for out_value in range(2):
            for i in range(len(dig_gpio_in_no_list)):
                in_value = 0
                self.chip.gpio.dig_gpio_out(dig_gpio_out_no_list[i], out_value)
                in_value = int(self.chip.gpio.dig_gpio_in(dig_gpio_in_no_list[i]))
                if (in_value != out_value):
                    logerror("in_value: %d, out_value: %d, dig_gpio_in_no: %d, dig_gpio_out_no: %d\n"%(in_value, out_value, dig_gpio_in_no_list[i], dig_gpio_out_no_list[i]))
                    fail_num += 1
            if fail_num:
                logerror("fail_num is: %d when out_value = %d\n"%(fail_num, out_value))
        if not fail_num:
            return logpass()
        else:
            return logfail()

    def tc004_rtc_gpio_pu_test(self, channel):
        chip1 = HALS(channel)
        if self.chipv == "ESP32":
            '''
            In ESP32:
            1) no rtc gpio pad 8, 9 in test board
            2) rtc gpio pad 6, 11, 12, 15 should not connected to other board, otherwise chip can not power up for CI test.
            '''
            #rtc_gpio_no_list = range(6, 18)
            rtc_gpio_no_list = [7, 10, 13, 14, 16, 17]
        else:
            rtc_gpio_no_list = range(22)
        self.chip.gpio.rtc_gpio_hangup_all()
        chip1.gpio.rtc_gpio_hangup_all()
        fail_num = 0
        for rtc_out_no in rtc_gpio_no_list:
            in_value = 0
            rtc_in_no = rtc_out_no
            self.chip.gpio.rtc_gpio_pu(rtc_out_no, 1)
            in_value = int(chip1.gpio.rtc_gpio_in(rtc_in_no))
            if (1 != in_value):
                logerror("rtc_out_no: %d, in_value:%d\n"%(rtc_out_no, in_value))
                fail_num += 1
        if fail_num:
            logerror("fail_num: %d"%(fail_num))
            return logfail()
        else:
            return logpass()

    def tc005_dig_gpio_pu_test(self, channel):
        '''dig_gpio_out_no need connected to dig_gpio_in_no'''
        chip1 = HALS(channel)
        if self.chipv == "ESP32":
            '''
            In ESP32:
            1) no rtc gpio pad 8, 9 in test board
            2) rtc gpio pad 6, 11, 12, 15 should not connected to other board, otherwise chip can not power up for CI test.
            '''
            #rtc_gpio_no_list = range(6, 18)
            dig_gpio_no_list = range(13, 20) + [4, 5, 9, 21, 22, 23] + range(26, 28)
        else:
            dig_gpio_no_list = range(22) + range(26, 46)
        self.chip.gpio.dig_gpio_hangup_all()
        chip1.gpio.dig_gpio_hangup_all()
        fail_num = 0
        for dig_out_no in dig_gpio_no_list:
            in_value = 0
            dig_in_no = dig_out_no
            self.chip.gpio.dig_gpio_pu(dig_out_no, 1)
            in_value = int(chip1.gpio.dig_gpio_in(dig_in_no))
            if (1 != in_value):
                logerror("dig_out_no: %d, in_value:%d\n"%(dig_out_no, in_value))
                fail_num += 1
        if fail_num:
            logerror("fail_num: %d"%(fail_num))
            return logfail()
        else:
            return logpass()

    def tc006_rtc_gpio_pd_test(self, channel):
        '''rtc_gpio_out_no need connected to rtc_gpio_in_no'''
        chip1 = HALS(channel)
        if self.chipv == "ESP32":
            '''
            In ESP32:
            1) no rtc gpio pad 8, 9 in test board
            2) rtc gpio pad 6, 11, 12, 15 should not connected to other board, otherwise chip can not power up for CI test.
            '''
            #rtc_gpio_no_list = range(6, 18)
            rtc_gpio_no_list = [7, 10, 13, 14, 16, 17]
        else:
            rtc_gpio_no_list = range(22)
        self.chip.gpio.rtc_gpio_hangup_all()
        chip1.gpio.rtc_gpio_hangup_all()
        fail_num = 0
        for rtc_out_no in rtc_gpio_no_list:
            in_value = 0
            rtc_in_no = rtc_out_no
            self.chip.gpio.rtc_gpio_pd(rtc_out_no, 1)
            in_value = int(chip1.gpio.rtc_gpio_in(rtc_in_no))
            if (0 != in_value):
                logerror("rtc_out_no: %d, in_value:%d\n"%(rtc_out_no, in_value))
                fail_num += 1
        if fail_num:
            logerror("fail_num: %d"%(fail_num))
            return logfail()
        else:
            return logpass()
    
    def tc007_dig_gpio_pd_test(self, channel):
        '''dig_gpio_out_no need connected to dig_gpio_in_no'''
        chip1 = HALS(channel)
        if self.chipv == "ESP32":
            '''
            In ESP32:
            1) no rtc gpio pad 8, 9 in test board
            2) rtc gpio pad 6, 11, 12, 15 should not connected to other board, otherwise chip can not power up for CI test.
            '''
            #rtc_gpio_no_list = range(6, 18)
            dig_gpio_no_list = range(13, 20) + [4, 5, 9, 21, 22, 23] + range(26, 28)
        else:
            dig_gpio_no_list = range(22) + range(26, 46)
        self.chip.gpio.dig_gpio_hangup_all()
        chip1.gpio.dig_gpio_hangup_all()
        fail_num = 0
        for dig_out_no in dig_gpio_no_list:
            in_value = 0
            dig_in_no = dig_out_no
            self.chip.gpio.dig_gpio_pd(dig_out_no, 1)
            in_value = int(chip1.gpio.dig_gpio_in(dig_in_no))
            if (0 != in_value):
                logerror("dig_out_no: %d, in_value:%d\n"%(dig_out_no, in_value))
                fail_num += 1
        if fail_num:
            logerror("fail_num: %d"%(fail_num))
            return logfail()
        else:
            return logpass()

    def tc008_rtc_gpio_hold_test(self, channel):
        '''rtc_gpio_out_no need connected to rtc_gpio_in_no'''
        chip1 = HALS(channel)
        if self.chipv == "ESP32":
            '''
            In ESP32:
            1) no rtc gpio pad 8, 9 in test board
            2) rtc gpio pad 6, 11, 12, 15 should not connected to other board, otherwise chip can not power up for CI test.
            '''
            #rtc_gpio_no_list = range(6, 18)
            rtc_gpio_no_list = [7, 10, 13, 14, 16, 17]
        else:
            rtc_gpio_no_list = range(22)
        self.chip.gpio.rtc_gpio_hangup_all()
        chip1.gpio.rtc_gpio_hangup_all()
        fail_num = 0
        for rtc_out_no in rtc_gpio_no_list:
            out_value1, out_value2 = 1, 0
            rtc_in_no = rtc_out_no
            self.chip.gpio.rtc_gpio_out(rtc_out_no, out_value1)
            self.chip.gpio.rtc_gpio_hold(rtc_out_no, 1)
            self.chip.gpio.rtc_gpio_out(rtc_out_no, out_value2)
            in_value2 = int(chip1.gpio.rtc_gpio_in(rtc_in_no))
            if(out_value1 != in_value2):
                logerror("rtc_out_no: %d, out_value1: %d, in_value2: %d\n"%(rtc_out_no, out_value1, in_value2))
                fail_num += 1
        if fail_num:
            logerror("fail_num: %d"%(fail_num))
            return logfail()
        else:
            return logpass()
    
    def tc009_dig_gpio_hold_test(self, channel):
        '''dig_gpio_out_no need connected to dig_gpio_in_no'''
        chip1 = HALS(channel)
        if self.chipv == "ESP32":
            '''
            In ESP32:
            1) no rtc gpio pad 8, 9 in test board
            2) rtc gpio pad 6, 11, 12, 15 should not connected to other board, otherwise chip can not power up for CI test.
            '''
            #rtc_gpio_no_list = range(6, 18)
            dig_gpio_no_list = range(13, 20) + [4, 5, 9, 21, 22, 23] + range(26, 28)
        else:
            dig_gpio_no_list = range(22) + range(26, 46)
        self.chip.gpio.dig_gpio_hangup_all()
        chip1.gpio.dig_gpio_hangup_all()
        fail_num = 0
        for dig_out_no in dig_gpio_no_list:
            out_value1, out_value2 = 1, 0
            dig_in_no = dig_out_no
            self.chip.gpio.dig_gpio_out(dig_out_no, out_value1)
            self.chip.gpio.dig_gpio_hold(dig_out_no, 1)
            self.chip.gpio.dig_gpio_out(dig_out_no, out_value2)
            in_value2 = int(chip1.gpio.dig_gpio_in(dig_in_no))
            if(out_value1 != in_value2):
                logerror("dig_out_no: %d, out_value1: %d, in_value2: %d\n"%(dig_out_no, out_value1, in_value2))
                fail_num += 1
        if fail_num:
            logerror("fail_num: %d"%(fail_num))
            return logfail()
        else:
            return logpass()

    def tc010_rtc_gpio_hold_insleep_test(self):
        '''
        rtc_gpio_out_no need connected to rtc_gpio_in_no
        before sleep, rtc_gpio_out_no output 0, then hold, then output 1 when in sleep, wakeup.  
        '''
        rtc_gpio_in_no =  6
        rtc_gpio_out_no = 7
        out_value1 = 0
        rtc_gpio_out_w1ts = self.chip.HWREG.RTC_IO.RTC_GPIO_OUT_W1TS._RTC_GPIO_OUT_W1TS__addr
        rtc_gpio_out_data_w1ts_lsb = self.chip.HWREG.RTC_IO.RTC_GPIO_OUT_W1TS._RTC_GPIO_OUT_W1TS__rtc_gpio_out_data_w1ts_lsb + rtc_gpio_out_no
        rtc_gpio_out_data_w1ts_msb = self.chip.HWREG.RTC_IO.RTC_GPIO_OUT_W1TS._RTC_GPIO_OUT_W1TS__rtc_gpio_out_data_w1ts_lsb + rtc_gpio_out_no
        if self.chipv == "ESP32":
            lowpower_state_addr = self.chip.HWREG.RTC_CNTL.RTC_DIAG0._RTC_DIAG0__addr
        else:
            lowpower_state_addr = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__addr
            lowpower_state_lsb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_lsb
            lowpower_state_msb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_msb
        self.chip.ulp.init()
        if self.chipv == "ESP32":
            self.chip.ulp.ldr(lowpower_state_addr, 19, 19)
        else:
            self.chip.ulp.ldr(lowpower_state_addr, lowpower_state_msb, lowpower_state_lsb)
        self.chip.ulp.blr(1, 3)
        self.chip.ulp.str(rtc_gpio_out_w1ts, rtc_gpio_out_data_w1ts_msb, rtc_gpio_out_data_w1ts_lsb, 1)#rtc_gpio_out(rtc_gpio_no, 1)
        self.chip.ulp.wakeup()
        self.chip.ulp.end()
        self.chip.ulp.start(1)
        self.chip.gpio.rtc_gpio_out(rtc_gpio_out_no, out_value1)
        in_value1 = int(self.chip.gpio.rtc_gpio_in(rtc_gpio_in_no))
        self.chip.gpio.rtc_gpio_hold(rtc_gpio_out_no, 1)
        self.chip.rtc_sleep.sleep(1, WAKEUP_REASON['SAR_TRIG'].value, 0)
        time.sleep(1)
        in_value2 = int(self.chip.gpio.rtc_gpio_in(rtc_gpio_in_no))
        loginfo("in_value1: %d, in_value2: %d\n"%(in_value1, in_value2))
        if(out_value1 != in_value2):
            return logfail()
        else:
            return logpass()

    def tc011_rtc_gpio_wakeup_test(self, rtc_gpio_no):
        wakeup_cause0 = int(self.chip.rtc_sleep.wakeup_cause())
        self.chip.gpio.rtc_gpio_wakeup_enable(rtc_gpio_no, 1)
        self.chip.gpio.rtc_gpio_hang_up(rtc_gpio_no)
        self.chip.gpio.rtc_gpio_in_enable(rtc_gpio_no)
        self.chip.gpio.rtc_gpio_hold(rtc_gpio_no)
        self.chip.rtc_sleep.sleep(0x7d, WAKEUP_ENABLE['GPIO_TRIG_EN'].value, 0)
        time.sleep(1)
        wakeup_cause1 = int(self.chip.rtc_sleep.wakeup_cause())
        if self.chipv == "CHIP722" or self.chipv == "CHIP723":
            self.chip.rtc_wdt.wdt_unlock()
            self.chip.rtc_wdt.wdt_stg_hold_len(0, 0xffff)
            self.chip.rtc_wdt.wdt_stg_act(0, 5)
            self.chip.rtc_wdt.wdt_init()
            time.sleep(2)
        self.chip.gpio.rtc_gpio_wakeup_enable(rtc_gpio_no, 2)
        self.chip.gpio.rtc_gpio_hang_up(rtc_gpio_no)
        self.chip.gpio.rtc_gpio_in_enable(rtc_gpio_no)
        self.chip.gpio.rtc_gpio_hold(rtc_gpio_no)
        self.chip.rtc_sleep.sleep(0x7d, WAKEUP_ENABLE['GPIO_TRIG_EN'].value, 0)
        time.sleep(1)
        wakeup_cause2 = int(self.chip.rtc_sleep.wakeup_cause())
        if self.chipv == "CHIP722" or self.chipv == "CHIP723":
            self.chip.rtc_wdt.wdt_unlock()
            self.chip.rtc_wdt.wdt_stg_hold_len(0, 0xffff)
            self.chip.rtc_wdt.wdt_stg_act(0, 5)
            self.chip.rtc_wdt.wdt_init()
            time.sleep(2)
        self.chip.gpio.rtc_gpio_wakeup_enable(rtc_gpio_no, 3)
        self.chip.gpio.rtc_gpio_hang_up(rtc_gpio_no)
        self.chip.gpio.rtc_gpio_in_enable(rtc_gpio_no)
        self.chip.gpio.rtc_gpio_hold(rtc_gpio_no)
        self.chip.rtc_sleep.sleep(0x7d, WAKEUP_ENABLE['GPIO_TRIG_EN'].value, 0)
        time.sleep(1)
        wakeup_cause3 = int(self.chip.rtc_sleep.wakeup_cause())
        if self.chipv == "CHIP722" or self.chipv == "CHIP723":
            self.chip.rtc_wdt.wdt_unlock()
            self.chip.rtc_wdt.wdt_stg_hold_len(0, 0xffff)
            self.chip.rtc_wdt.wdt_stg_act(0, 5)
            self.chip.rtc_wdt.wdt_init()
            time.sleep(2)
        self.chip.gpio.rtc_gpio_wakeup_enable(rtc_gpio_no, 4)
        self.chip.gpio.rtc_gpio_hang_up(rtc_gpio_no)
        self.chip.gpio.rtc_gpio_in_enable(rtc_gpio_no)
        self.chip.gpio.rtc_gpio_hold(rtc_gpio_no)
        self.chip.rtc_sleep.sleep(0x7d, WAKEUP_ENABLE['GPIO_TRIG_EN'].value, 0)
        time.sleep(1)
        wakeup_cause4 = int(self.chip.rtc_sleep.wakeup_cause())
        if self.chipv == "CHIP722" or self.chipv == "CHIP723":
            self.chip.rtc_wdt.wdt_unlock()
            self.chip.rtc_wdt.wdt_stg_hold_len(0, 0xffff)
            self.chip.rtc_wdt.wdt_stg_act(0, 5)
            self.chip.rtc_wdt.wdt_init()
            time.sleep(2)
        self.chip.gpio.rtc_gpio_wakeup_enable(rtc_gpio_no, 5)
        self.chip.gpio.rtc_gpio_hang_up(rtc_gpio_no)
        self.chip.gpio.rtc_gpio_in_enable(rtc_gpio_no)
        self.chip.gpio.rtc_gpio_hold(rtc_gpio_no)
        self.chip.rtc_sleep.sleep(0x7d, WAKEUP_ENABLE['GPIO_TRIG_EN'].value, 0)
        time.sleep(1)
        wakeup_cause5 = int(self.chip.rtc_sleep.wakeup_cause())
        loginfo("wakeup_cause0:%d, wakeup_cause1:%d, wakeup_cause2:%d, wakeup_cause3:%d, wakeup_cause4:%d, wakeup_cause5:%d"%(wakeup_cause0, wakeup_cause1, wakeup_cause2, wakeup_cause3, wakeup_cause4, wakeup_cause5))
        if (0 == wakeup_cause0) and (wakeup_cause1 == WAKEUP_REASON['GPIO_TRIG'].value) and (wakeup_cause2 == WAKEUP_REASON['GPIO_TRIG'].value) and (wakeup_cause3 == WAKEUP_REASON['GPIO_TRIG'].value) \
            and (wakeup_cause4 == WAKEUP_REASON['GPIO_TRIG'].value) and (wakeup_cause5 == WAKEUP_REASON['GPIO_TRIG'].value):
            return logpass()
        else:
            return logfail()

    def tc012_ext1_wakeup_test(self, rtc_gpio_no):
        '''rtc_in_no need to connect to high level by default, then low, then high'''
        self.chip.gpio.rtc_gpio_hang_up(rtc_gpio_no)
        self.chip.gpio.rtc_gpio_in_enable(rtc_gpio_no)
        self.chip.gpio.rtc_gpio_hold(rtc_gpio_no)
        self.chip.gpio.ext1_wakeup_enable(rtc_gpio_no, 0)
        self.chip.rtc_sleep.sleep(0x7f, WAKEUP_ENABLE['EXT_EVENT1_TRIG_EN'].value, 0)
        time.sleep(1)
        wakeup_cause1 = int(self.chip.rtc_sleep.wakeup_cause())
        if self.chipv == "CHIP722" or self.chipv == "CHIP723":
            self.chip.rtc_wdt.wdt_unlock()
            self.chip.rtc_wdt.wdt_stg_hold_len(0, 0xffff)
            self.chip.rtc_wdt.wdt_stg_act(0, 5)
            self.chip.rtc_wdt.wdt_init()
            time.sleep(2)
        self.chip.gpio.rtc_gpio_hang_up(rtc_gpio_no)
        self.chip.gpio.rtc_gpio_in_enable(rtc_gpio_no)
        self.chip.gpio.rtc_gpio_hold(rtc_gpio_no)
        self.chip.gpio.ext1_wakeup_enable(rtc_gpio_no, 1)
        self.chip.rtc_sleep.sleep(0x7f, WAKEUP_ENABLE['EXT_EVENT1_TRIG_EN'].value, 0)
        time.sleep(1)
        wakeup_cause2 = int(self.chip.rtc_sleep.wakeup_cause())
        if (wakeup_cause1 == WAKEUP_REASON['EXT_EVENT1_TRIG'].value) and (wakeup_cause2 == WAKEUP_REASON['EXT_EVENT1_TRIG'].value):
            return logpass()
        else:
            return logfail()

    def tc013_rtc_gpio_pd_xtal_test(self):
        self.chip.rtc_debug.CLK(5, 1)#clk_out_num set to 1 means clock signal strapping to gpio20 in CHIP722
        rtc_in_no = 3
        self.chip.gpio.rtc_gpio_pd_xtal_enable(rtc_in_no, 0)
        self.chip.HWREG.RTC_CNTL.RTC_OPTIONS0.reg_xtl_force_pu = 0
        time.sleep(5)
        in_value = int(self.chip.gpio.rtc_gpio_in(rtc_in_no))
        loginfo("in_value: %d"%(in_value))







    def tc004_2_rtc_gpio_pu_test(self, rtc_gpio_out_no):
        '''rtc_gpio_out_no need connected to rtc_gpio_in_no'''
        rtc_gpio_in_no =  4
        self.chip.gpio.rtc_gpio_hang_up(rtc_gpio_out_no)
        self.chip.gpio.rtc_gpio_pu(rtc_gpio_out_no, 1)
        in_value = int(self.chip.gpio.rtc_gpio_in(rtc_gpio_in_no))
        loginfo("in_value: %d\n"%(in_value))
        if (1 != in_value):
            return logfail()
        else:
            return logpass()

    def tc005_2_dig_gpio_pu_test(self, dig_gpio_out_no):
        '''dig_gpio_out_no need connected to dig_gpio_in_no'''
        dig_gpio_in_no =  4
        self.chip.gpio.dig_gpio_hang_up(dig_gpio_out_no)
        self.chip.gpio.dig_gpio_pu(dig_gpio_out_no, 1)
        in_value = int(self.chip.gpio.dig_gpio_in(dig_gpio_in_no))
        loginfo("in_value: %d\n"%(in_value))
        if (1 != in_value):
            return logfail()
        else:
            return logpass()

    def tc006_2_rtc_gpio_pd_test(self, rtc_gpio_out_no):
        '''rtc_gpio_out_no need connected to rtc_gpio_in_no'''
        rtc_gpio_in_no =  4
        self.chip.gpio.rtc_gpio_hang_up(rtc_gpio_out_no)
        self.chip.gpio.rtc_gpio_pd(rtc_gpio_out_no, 1)
        in_value = int(self.chip.gpio.rtc_gpio_in(rtc_gpio_in_no))
        loginfo("in_value: %d\n"%(in_value))
        if (0 != in_value):
            return logfail()
        else:
            return logpass()

    def tc007_2_dig_gpio_pd_test(self, dig_gpio_out_no):
        '''dig_gpio_out_no need connected to dig_gpio_in_no'''
        dig_gpio_in_no =  4
        self.chip.gpio.dig_gpio_hang_up(dig_gpio_out_no)
        self.chip.gpio.dig_gpio_pd(dig_gpio_out_no, 1)
        in_value = int(self.chip.gpio.dig_gpio_in(dig_gpio_in_no))
        loginfo("in_value: %d\n"%(in_value))
        if (0 != in_value):
            return logfail()
        else:
            return logpass()
        
    def tc008_2_rtc_gpio_hold_test(self, rtc_gpio_out_no):
        '''rtc_gpio_out_no need connected to dig_gpio_in_no'''
        rtc_gpio_in_no =  4
        out_value1, out_value2 = 1, 0
        self.chip.gpio.rtc_gpio_hang_up(rtc_gpio_out_no)
        self.chip.gpio.rtc_gpio_out(rtc_gpio_out_no, out_value1)
        in_value1 = int(self.chip.gpio.rtc_gpio_in(rtc_gpio_in_no))
        loginfo("in_value1: %d\n"%(in_value1))
        self.chip.gpio.rtc_gpio_hold(rtc_gpio_out_no, 1)
        self.chip.gpio.rtc_gpio_out(rtc_gpio_out_no, out_value2)
        in_value2 = int(self.chip.gpio.rtc_gpio_in(rtc_gpio_in_no))
        loginfo("in_value2: %d\n"%(in_value2))
        if(out_value1 != in_value2):
            return logfail()
        else:
            return logpass()

    def tc009_2_dig_gpio_hold_test(self, dig_gpio_out_no):
        '''dig_gpio_out_no need connected to dig_gpio_in_no'''
        dig_gpio_in_no =  4
        out_value1, out_value2 = 1, 0
        self.chip.gpio.dig_gpio_hang_up(dig_gpio_out_no)
        self.chip.gpio.dig_gpio_out(dig_gpio_out_no, out_value1)
        in_value1 = int(self.chip.gpio.dig_gpio_in(dig_gpio_in_no))
        loginfo("in_value1: %d\n"%(in_value1))
        self.chip.gpio.dig_gpio_hold(dig_gpio_out_no, 1)
        self.chip.gpio.dig_gpio_out(dig_gpio_out_no, out_value2)
        in_value2 = int(self.chip.gpio.dig_gpio_in(dig_gpio_in_no))
        loginfo("in_value2: %d\n"%(in_value2))
        if(out_value1 != in_value2):
            return logfail()
        else:
            return logpass()
