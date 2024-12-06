class RTC_WDT(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        
    def wdt_init(self, cpu_reset_len = 7, sys_reset_len = 7, chip_reset_width = 7):
        '''
        :brief:
            watch dog timer init
        :param:
            cpu_reset_len: cycles to reset cpu;
            sys_reset_len: cycles to reset system;
            chip_reset_width: pulse width to reset chip, used begin from CHIP722.
        :return:
            no return
        '''
        if self.chipv == "CHIP722":
            return self.channel.req_com("wdt_init %d %d %d"%(cpu_reset_len, sys_reset_len, chip_reset_width))
        else:
            return self.channel.req_com("wdt_init %d %d"%(cpu_reset_len, sys_reset_len))
    
    def wdt_feed(self):
        '''
        :brief:
            feed watch dog
        :param:
            no param
        :return:
            no return
        '''
        return self.channel.req_com("wdt_feed")
    
    def wdt_stg_hold_len(self, stage, cycle):
        '''
        :brief:
            set hold length for stage[0~3]
        :param:
            - stage: [0~3], which stage to set;
            - cycle: length value
        :return:
            no return
        '''
        return self.channel.req_com("wdt_stg_hold_len %d %d"%(stage, cycle))
    
    def wdt_stg_act(self, stage, act):
        '''
        :brief:
            set action value[0~4] for certain stage[0~3]
        :param:
            - stage: [0~3], which stage to set;
            - act: action value when wdt arrived:
                - 0: do nothing;
                - 1: send int;
                - 2: reset cpu;
                - 3: reset system;
                - 4: reset RTC(include system & rtc)
                - 5: reset chip(begin from CHIP722)
        :return:
            no return
        '''
        return self.channel.req_com("wdt_stg_act %d %d"%(stage, act))
    
    def wdt_flashboot_enable(self, enable):
        '''
        :brief:
            enable wdt or disable wdt when flash boot
        :param:
            enable:
                - 0: disable;
                - 1: enable
        :return:
            no return
        ''' 
        return self.channel.req_com("wdt_flashboot_enable %d"%(enable))
    
    def wdt_int_enable(self, enable):
        '''
        :brief:
            enable or disable wdt interrupt
        :param:
            enable:
                - 0: disable;
                - 1: enable
        :return:
            no return
        ''' 
        return self.channel.req_com("wdt_int_enable %d"%(enable))
    
    def wdt_int_raw_sts(self):
        '''
        :brief:
            wdt interrupt raw status
        :param:
            no param
        :return:
            raw status value
        ''' 
        return self.channel.req_com("wdt_int_raw_sts")
    
    def wdt_int_sts(self):
        '''
        :brief:
            wdt interrupt status
        :param:
            no param
        :return:
            status value
        ''' 
        return self.channel.req_com("wdt_int_sts")

    def wdt_int_clr(self):
        '''
        :brief:
            clear wdt interrupt
        :param:
            no param
        :return:
            no return
        ''' 
        return self.channel.req_com("wdt_int_clr")
    
    def wdt_stop(self):
        '''
        :brief:
            stop wdt
        :param:
            no param
        :return:
            no return
        ''' 
        return self.channel.req_com("wdt_stop")

    def wdt_lock(self):
        '''
        :brief:
            lock rtc wdt
        :param:
            no param
        :return:
            no return
        '''
        return self.channel.req_com("wdt_lock")

    def wdt_unlock(self):
        '''
        :brief:
            unlock rtc wdt
        :param:
            no param
        :return:
            no return
        '''
        return self.channel.req_com("wdt_unlock")

