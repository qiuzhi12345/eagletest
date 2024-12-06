# -- coding: utf-8 --
class GPIO(object):
    """docstring for GPIO"""
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel

    def rtc_gpio_in_enable(self, rtc_in_no, enable = 1):
        '''
        :brief:
            rtc gpio input enable
        :param:
            - rtc_in_no: rtc gpio number;
            - enable: enable or not;
        :return:
            no return
        '''
        self.channel.req_com("rtc_gpio_in_enable %d %d"%(rtc_in_no, enable))

    def rtc_gpio_out(self, rtc_out_no, out_value, drv = 2):
        '''
        :brief:
            rtc gpio output value
        :param:
            - 1.rtc_out_no: rtc gpio number;
            - 2.out_value: can be either 1 or 0;
            - 3.drv: default value is 2, it can be set to 0,1,2,3.
        :return:
            no return
        '''
        self.channel.req_com("rtc_gpio_out %d %d %d"%(rtc_out_no, out_value, drv))

    def rtc_gpio_in(self, rtc_in_no):
        '''
        :brief:
            rtc gpio input value
        :param:
            rtc_in_no: rtc gpio number.
        :return:
            return value of rtc_in_no input
        '''
        return self.channel.req_com("rtc_gpio_in %d" %(rtc_in_no))

    def rtc_gpio_pu(self, rtc_out_no, pu):
        '''
        :brief:
            rtc gpio force power up.
        :param:
            - rtc_out_no: rtc gpio number.
            - pu:
                - 1: force power up
                - 0: no force power up.
        :return:
            no return
        '''
        return self.channel.req_com("rtc_gpio_pu %d %d" %(rtc_out_no, pu))

    def rtc_gpio_pd(self, rtc_out_no, pd):
        '''
        :brief:
            rtc gpio force power down.
        :param:
            - rtc_out_no: rtc gpio number.
            - pd:
                - 1: force power down
                - 0: no force power down.
        :return:
             no return
        '''
        return self.channel.req_com("rtc_gpio_pd %d %d" %(rtc_out_no, pd))

    def rtc_gpio_hold(self, rtc_out_no, hold = 1):
        '''
        :brief:
            rtc gpio hold, when hold, no matter what output, the output value is equal to the output value before hold.
        :param:
            - rtc_out_no: rtc gpio number.
            - hold:
                - 1: hold
                - 0: not hold.
        :return:
            no return
        '''
        return self.channel.req_com("rtc_gpio_hold %d %d" %(rtc_out_no, hold))

    def dig_gpio_out(self, dig_out_no, out_value, drv = 2):
        '''
        :brief:
            dig gpio output value
        :param:
            - 1.dig_out_no: dig gpio number;
            - 2.out_value: can be either 1 or 0
            - 3.drv: default value is 2, it can be set to 0,1,2,3.
        :return:
            no return
        '''
        self.channel.req_com("dig_gpio_out %d %d %d"%(dig_out_no, out_value, drv))

    def dig_gpio_in(self, dig_in_no):
        '''
        :brief:
            dig gpio input value
        :param:
            dig_in_no: dig gpio number.
        :return:
            value of dig_in_no input
        '''
        return self.channel.req_com("dig_gpio_in %d" %(dig_in_no))

    def dig_gpio_pu(self, dig_out_no, pu):
        '''
        :brief:
            dig gpio force power up.
        :param:
            - dig_out_no: dig gpio number.
            - pu:
                - 1: force power up
                - 0: no force power up.
        :return:
            no return
        '''
        return self.channel.req_com("dig_gpio_pu %d %d" %(dig_out_no, pu))

    def dig_gpio_pd(self, dig_out_no, pd):
        '''
        :brief:
            dig gpio force power down.
        :param:
            - dig_out_no: dig gpio number.
            - pd:
                - 1: force power down
                - 0: no force power down.
        :return:
            no return
        '''
        return self.channel.req_com("dig_gpio_pd %d %d" %(dig_out_no, pd))

    def dig_gpio_hold(self, dig_out_no, hold):
        '''
        :brief:
            dig gpio hold, when hold, no matter what output, the output value is equal to the output value before hold.
        :param:
            - dig_out_no: dig gpio number.
            - hold:
                - 1: hold
                - 0: not hold.
        :return:
            no return
        '''
        return self.channel.req_com("dig_gpio_hold %d %d" %(dig_out_no, hold))

    #need to test
    def rtc_gpio_drv(self, rtc_out_no, drv):
        '''
        :brief:
            set rtc gpio drv value, which can be set to 0,1,2,3
        :param:
            - rtc_out_no: rtc gpio number.
            - drv: dev value
        :return:
            no return
        '''
        return self.channel.req_com("rtc_gpio_drv %d %d" %(rtc_out_no, drv))

    def rtc_gpio_hang_up(self, rtc_out_no):
        '''
        :brief:
            rtc gpio hang up, when hang up, output disable, input disable, not pu, not pd.
        :param:
            rtc_out_no: to be hang up rtc gpio number.
        :return:
            no return
        '''
        return self.channel.req_com("rtc_gpio_hang_up %d" %(rtc_out_no))

    def rtc_gpio_mux_sel(self, gpio_no, mux_sel):
        '''
        :brief:
            when gpio_no can be as rtc_gpio or dig_gpio, we need select its function
        :param:
            mux_sel: 
                - 0: mux_sel_dig
                - 1: mux_sel_rtc
        :return:
            no return
        '''
        return self.channel.req_com("rtc_gpio_mux_sel %d %d" %(gpio_no, mux_sel))

    def dig_gpio_drv(self, dig_out_no, drv):

        '''
        :brief:
            set dig gpio drv value, which can be set to 0,1,2,3
        :param:
            - dig_out_no: dig gpio number.
            - drv: drv value
        :return:
            no return
        '''
        return self.channel.req_com("dig_gpio_drv %d %d" %(dig_out_no, drv))

    def dig_gpio_hang_up(self, dig_out_no):
        '''
        :brief:
            dig gpio hang up, when hang up, output disable, input disable, not pu, not pd
        :param:
            dig_out_no: to be hang up dig gpio number.
        :return:
            no return
        '''
        return self.channel.req_com("dig_gpio_hang_up %d" %(dig_out_no))

    def rtc_gpio_wakeup_enable(self, rtc_in_no, lvl = 5):
        '''
        @brief: rtc gpio wakeup enable
        @param:
            - rtc_in_no: which rtc pad used to wakeup;
            - lvl:
                - 0: 关闭;
                - 1: 上升沿触发中断；
                - 2: 下降沿触发；
                - 3: 任意沿触发；
                - 4: 低电平触发；
                - 5: 高电平触发
        @return - no return
        '''
        return self.channel.req_com("rtc_gpio_wakeup_enable %d %d"%( rtc_in_no, lvl))

    def ext1_wakeup_enable(self, rtc_in_no, lvl = 1):
        '''
        @brief: rtc gpio wakeup enable
        @param:
            - rtc_in_no: which rtc pad used to wakeup;
            - lvl:
                - 0: 低电平唤醒;
                - 1: 高电平唤醒；
        @return - no return
        '''
        return self.channel.req_com("ext1_wakeup_enable %d %d"%( rtc_in_no, lvl))

    def rtc_gpio_slp_in_enable(self, rtc_gpio_no, enable = 1):
        '''
        :brief:
            enable or disable rtc_gpio when in sleep
        :param:
            - enable: enable or not
        :return:
            no return
        '''
        return self.channel.req_com("rtc_gpio_slp_in_enable %d %d"%(rtc_gpio_no, enable))

    def rtc_gpio_pd_xtal_enable(self, rtc_gpio_no, lv = 0):
        '''
        :brief: rtc gpio wakeup pd xtal enable.
        :param:
            - rtc_gpio_no: which rtc pad used to pd xtal;
            - lv: set 1, if rtc_gpio_no get low value, pd xtal; set 0, if rtc_gpio_no get high value, pd xtal.
        :return:
            no return
        '''
        if self.chipv == "CHIP722":
            return self.channel.req_com("rtc_gpio_pd_xtal_enable %d %d" %(rtc_gpio_no, lv))
        else:
            pass

    def rtc_gpio_hangup_all(self):
        '''
        :brief:
            hangup all rtc gpio pads.
        :param:
            no param
        :return:
            no return
        '''
        return self.channel.req_com("all_rtc_gpio_hang_up")

    def dig_gpio_hangup_all(self, no_hangup_pad = 100, useUart = 1):
        '''
        :brief:
            hangup all digital gpio pads except no_hangup_pad pad and uart pad if useUart equal 1.
        :param:
            - no_hangup_pad: which pad will not hangup;
            - useUart: hangup uart or not.If 1, uart pad will not hangup, print will be valid, otherwise uart pad will hangup and print will be unvalid.
        :return:
            no return
        '''
        return self.channel.req_com("all_dig_gpio_hang_up %d %d"%(no_hangup_pad, useUart))