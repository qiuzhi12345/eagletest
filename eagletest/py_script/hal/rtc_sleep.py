class RTC_SLEEP(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel

    def sleep(self, slp_mode, wakeup_opt, reject_opt, lslp = 0):
        '''
        :brief:
            start sleep
        :param:
            - slp_mode, 6 bits, when in deep sleep, set 0x3f
                - BIT0: RTC_SLEEP_PD_DIG;
                - BIT1: RTC_SLEEP_PD_RTC_RTC_PERIPH;
                - BIT2: RTC_SLEEP_PD_RTC_SLOW_MEM;
                - BIT3: RTC_SLEEP_PD_RTC_FAST_MEM;
                - BIT4: RTC_SLEEP_PD_RTC_MEM_FOLLOW_CPU;
                - BIT5: RTC_SLEEP_PD_VDDSDIO;
                - BIT6: RTC_SLEEP_PD_WIFI.
            - wakeup_opt: wakeup source:
                - bit0: rtc ext0 wakeup enable
                - bit1: rtc ext1 wakeup enable
                - bit2: rtc gpio wakeup enable
                - bit3: rtc timer wakeup enable
                - bit4: rtc sdio wakeup enable(light sleep only)
                - bit5: rtc mac wakeup enable(light sleep only)
                - bit6: rtc uart0 wakeup enable(light sleep only)
                - bit7: rtc uart1 wakeup enable(light sleep only)
                - bit8: rtc touch wakeup enable
                - bit9: rtc ulp wakeup enable
                - bit10: bt wakeup enable(light sleep only)
                - bit11: rtc cocpu wakeup enable(begin from chip722)
                - bit12: xtal32k dead wakeup enable(begin from chip722)
                - bit13: rtc cocpu trap wakeup enable(begin from chip722)
                - bit14: rtc usb wakeup enable(begin from chip722)
            - reject_opt: can not be as wakeup source
            - lslp: used to debug, default value set 0
        :return:
            return reject interrupt raw status(if in deep sleep mode, we never return value)
        '''
        if self.chipv == "ESP32":
            return self.channel.req_com("rtc_sleep %d %d %d"%(slp_mode, wakeup_opt, reject_opt))
        else:
            return self.channel.req_com("rtc_sleep %d %d %d %d"%(slp_mode, wakeup_opt, reject_opt, lslp))

    def special_sleep(self, slp_mode, wakeup_opt, reject_opt, lslp = 0):
        '''
        :brief:
            start sleep. compare to normal sleep api, this api add printf before goto sleep.
        :param:
            - slp_mode, 6 bits, when in deep sleep, set 0x3f
                - BIT0: RTC_SLEEP_PD_DIG;
                - BIT1: RTC_SLEEP_PD_RTC_RTC_PERIPH;
                - BIT2: RTC_SLEEP_PD_RTC_SLOW_MEM;
                - BIT3: RTC_SLEEP_PD_RTC_FAST_MEM;
                - BIT4: RTC_SLEEP_PD_RTC_MEM_FOLLOW_CPU;
                - BIT5: RTC_SLEEP_PD_VDDSDIO;
                - BIT6: RTC_SLEEP_PD_WIFI.
            - wakeup_opt: wakeup source:
                - bit0: rtc ext0 wakeup enable
                - bit1: rtc ext1 wakeup enable
                - bit2: rtc gpio wakeup enable(light sleep only)
                - bit3: rtc timer wakeup enable
                - bit4: rtc sdio wakeup enable(light sleep only)
                - bit5: rtc mac wakeup enable(light sleep only)
                - bit6: rtc uart0 wakeup enable(light sleep only)
                - bit7: rtc uart1 wakeup enable(light sleep only)
                - bit8: rtc touch wakeup enable
                - bit9: rtc ulp wakeup enable
                - bit10: bt wakeup enable(light sleep only)
                - bit11: rtc cocpu wakeup enable(begin from chip722)
                - bit12: xtal32k dead wakeup enable(begin from chip722)
                - bit13: rtc cocpu trap wakeup enable(begin from chip722)
                - bit14: rtc usb wakeup enable(begin from chip722)
            - lslp: set to 0(begin from chip722)
            - reject_opt: can not be as wakeup source
        :return:
            return reject interrupt raw status(if in deep sleep mode, we never return value)
        '''
        if self.chipv == "CHIP722":
            return self.channel.req_com("spe_sleep_forpython %d %d %d %d"%(slp_mode, wakeup_opt, reject_opt, lslp))
        else:
            return self.channel.req_com("spe_sleep_forpython %d %d %d"%(slp_mode, wakeup_opt, reject_opt))
    
    def wakeup_cause(self):
        '''
        :brief:
            start sleep
        :param:
            no param
        :return:
            return wakeup reason
        '''
        return self.channel.req_com("rtc_wakeup_cause")


    def rtc_timer_wakeup(self, cycle_hi, cycle_lo):
        '''
        :brief: set rtc timer to wakeup
        :param:
            - cycle_hi: sleep high 32 cycels
            - cycle_lo: sleep low 32 cycles
        :return: no return
        '''
        return self.channel.req_com("slp_cnt_wakeup %d %d"%(cycle_hi, cycle_lo))
