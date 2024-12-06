class RTC_TIMER(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        
    def update_time(self):
        '''
        :brief:
            update rtc time
        :param:
            no param
        :return:
            no return
        '''
        return self.channel.req_com("update_rtc_time")
    
    def enable_valid_int(self, enable):
        '''
        :brief:
            enable rtc timer valid interrupt
        :param:
            enable:
                - 1: enable valid int;
                - 0: disable valid int
        :return:
            no return
        '''
        if self.chipv == "ESP32" or self.chipv == "CHIP722":
            return self.channel.req_com("rtc_time_valid_int_enable %d"%(enable))
    
    def get_valid_int_raw_sts(self):
        '''
        :brief:
            get rtc timer valid interrupt raw status
        :param:
            no param
        :return:
            return raw status
        '''
        if self.chipv == "ESP32" or self.chipv == "CHIP722":
            return self.channel.req_com("rtc_time_valid_int_raw_sts")
    
    def get_valid_int_sts(self):
        '''
        :brief:
            get rtc timer valid interrupt status
        :param:
            no param
        :return:
            return status
        '''
        if self.chipv == "ESP32" or self.chipv == "CHIP722":
            return self.channel.req_com("rtc_time_valid_int_sts")
    
    def clr_valid_int(self):
        '''
        :brief:
            clear rtc timer valid interrupt
        :param:
            no param
        :return:
            no return
        '''
        if self.chipv == "ESP32" or self.chipv == "CHIP722":
            return self.channel.req_com("rtc_time_valid_int_clr")
    
    def get_valid_value(self):
        '''
        :brief:
            get rtc timer valid value
        :param:
            no param
        :return:
            return valid value
        '''
        if self.chipv == "ESP32" or self.chipv == "CHIP722":
            return self.channel.req_com("rtc_time_valid_value")
    
    def enable_alarm(self, enable):
        '''
        :brief:
            enable rtc timer alarm
        :param:
            enable:
                - 1: enable valid int;
                - 0: disable valid int
        :return:
            no return
        '''
        return self.channel.req_com("rtc_time_alarm_enable %d"%(enable))
    
    def get_time_low(self):
        '''
        :brief:
            get rtc timer low 32 bits value
        :param:
            no param
        :return:
            return rtc timer low 32 bits value
        '''
        return self.channel.req_com("get_rtc_time_low")
    
    def get_time_high(self):
        '''
        :brief:
            get rtc timer high 32 bits value
        :param:
            no param
        :return:
            return rtc timer high 32 bits value
        '''
        return self.channel.req_com("get_rtc_time_high")

    def set_alarm_time_low(self, low_value):
        '''
        :brief:
            set rtc sleep timer low 32 bits value
        :param:
            low_value: value to set
        :return:
            no return
        '''
        return self.channel.req_com("set_rtc_alarm_time_low %d"%(low_value))

    def set_alarm_time_high(self, high_value):
        '''
        :brief:
            set rtc sleep timer high 32 bits value
        :param:
            high_value: value to set
        :return:
            no return
        '''
        return self.channel.req_com("set_rtc_alarm_time_low %d"%(high_value))

    def enable_int(self, enable):
        '''
        :brief:
            enable rtc timer interrupt
        return
        :param:
            enable:
                - 1: enable int;
                - 0: disable int
        :return:
            no return
        '''
        return self.channel.req_com("rtc_time_int_enable %d"%(enable))
    
    def get_int_raw_sts(self):
        '''
        :brief:
            get rtc timer interrupt raw status
        :param:
            no param
        :return:
            return raw status
        '''
        return self.channel.req_com("rtc_time_int_raw_sts")
    
    def get_int_sts(self):
        '''
        :brief:
            get rtc timer interrupt status
        :param:
            no param
        :return:
            return status
        '''
        return self.channel.req_com("rtc_time_int_sts")
    
    def clr_int(self):
        '''
        :brief:
            clear rtc timer interrupt
        :param:
            no param
        :return:
            no return
        '''
        return self.channel.req_com("rtc_time_int_clr")

    def xtl_off(self, enable = 1):
        '''
        :brief:
            begin from CHIP722.
            when enable, rtc_timer0 store time after sleep, rtc_timer1 store time before sleep;
            when disable, rtc_timer0 store rtc time, rtc_timer1 is invalid.
        :param:
            enable or not
        :return:
            no return
        '''
        if self.chipv == "CHIP722":
            return self.channel.req_com("xtl_off %d"%(enable))

    def get_time1_low(self):
        '''
        :brief:
            get rtc timer low 32 bits value before sleep when xtl is off
        :param:
            no param
        :return:
            return rtc timer low 32 bits value
        '''
        return self.channel.req_com("get_rtc_time1_low")

    def get_time1_high(self):
        '''
        :brief:
            get rtc timer high 16 bits value before sleep when xtl is off
        :param:
            no param
        :return:
            return rtc timer high 16 bits value
        '''
        return self.channel.req_com("get_rtc_time1_high")

    def get_slp_time(self, period):
        '''
        :brief:
            get rtc sleep value
        :param:
            period: rtc slow clock period
        :return:
            return rtc sleep timer value
        '''
        return self.channel.req_com("rtc_slp_time %d"%(period))

    def rtc_slp_time_test(self, slow_clk_sel, slp_time_us, dig_gpio):
        '''
        :brief:
            get rtc sleep value
        :param:
            - slow_clk_sel
                - 0: RTC_SLOW_FREQ_RTC 150K
                - 1: 32K_XTAL
                - 2: 8MD256
            - slp_time_us: sleep time
            - dig_gpio: which digital gpio to connected to detect sleep time
        :return:
            return rtc sleep timer value
        '''
        return self.channel.req_com("rtc_slp_time_testcase %d %d %d"%(slow_clk_sel, slp_time_us, dig_gpio))
    
    def rtc_timer_int_handler(self, slp_cycles_hi, slp_cycles_low):
        '''
        :brief: test if rtc_timer handler ok or not.
        :param:
            - slp_cycles_low: rtc timer sleep time low 32bit
            - slp_cycles_high: rtc timer sleep time high 16bit
        :return: no return
        '''
        if self.chipv == "CHIP722" or self.chipv == "CHIP723":
            return self.channel.req_com("rtc_timer_int_handler_set %d %d"%(slp_cycles_hi, slp_cycles_low))
