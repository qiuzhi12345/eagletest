class RTC_BROWNOUT(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel

    def enable(self, enable = 1):
        '''
        :brief:
            enable rtc brownout
        :param:
            - enable: enable rtc brownout or not
        :return:
            no return
        '''
        return self.channel.req_com("rtc_brownout_enable %d"%(enable))

    def reset_enable(self, rst_en = 1):
        '''
        :brief:
            enable rtc brownout reset rtc function
        :param:
            - rst_en: enable reset rtc or not
        :return:
            no return
        '''
        return self.channel.req_com("rtc_brownout_reset_enable %d"%(rst_en))

    def pdrf_enable(self, pdrf_en = 1):
        '''
        :brief:
            enable rtc brownout powerdown rf function when voltage is low than thres
        :param:
            - pdrf_en: enable pd rf or not
        :return:
            no return
        '''
        return self.channel.req_com("rtc_brownout_pdrf_enable %d"%(pdrf_en))

    def close_flash_enable(self, clofla_en = 1):
        '''
        :brief:
            enable rtc brownout close flash function when voltage is low than thres
        :param:
            - clofla_en: enable close flash function or not
        :return:
            no return
        '''
        return self.channel.req_com("rtc_brownout_closeflash_enable %d"%(clofla_en))

    def thres_set(self, thres = 5):
        if self.chipv == "ESP32":
            '''
            :brief: set rtc brownout thres
            :param:
                - thres: it can be set 0~7, means different voltage thres.
            :return: no return
            '''
            return self.channel.req_com("rtc_brownout_thres_set %d"%(thres))
        else:
            pass

    def rst_count_set(self, rst_wait = 0x3ff):
        '''
        :brief: set rtc brownout reset rtc needing count
        :param:
            - rst_wait: 10 bits, when brownout count is more than rst_wait, reset rtc.
        :return: no return
        '''
        return self.channel.req_com("rtc_brownout_rst_wait_set %d"%(rst_wait))

    def int_enable(self, enable = 1):
        '''
        :brief: enable rtc brownout int
        :param:
            - enable: enable or not
        :return: no return
        '''
        return self.channel.req_com("rtc_brownout_int_enable %d"%(enable))

    def int_raw(self):
        '''
        :brief: get rtc brown out int raw status
        :param: no param
        :return: return int raw status
        '''
        return self.channel.req_com("get_rtc_brownout_int_raw")

    def int_sts(self):
        '''
        :brief: get rtc brown out int status
        :param: no param
        :return: return int status
        '''
        return self.channel.req_com("get_rtc_brownout_int_sts")

    def int_clr(self):
        '''
        :brief: clear rtc brown out interrupt
        :param: no param
        :return: no return
        '''
        return self.channel.req_com("clr_rtc_brownout_int")
    
    