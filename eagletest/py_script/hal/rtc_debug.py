class RTC_DEBUG(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel

    def PDAC1(self,is_sensor, row , bitnum):
        '''
        :brief:
        :param:
        :return: - no return
        '''
        return self.channel.req_com("PDAC1_DEBUG_CFG %d %d %d"%(is_sensor, row, bitnum))

    def PDAC2(self,is_sensor, row , bitnum):
        '''
        :brief:
        :param:
        :return: - no return
        '''
        return self.channel.req_com("PDAC2_DEBUG_CFG %d %d %d"%(is_sensor, row, bitnum))

    def X32P(self,is_sensor, row , bitnum):
        '''
        :brief:
        :param:
        :return: - no return
        '''
        return self.channel.req_com("X32P_DEBUG_CFG %d %d %d"%(is_sensor, row, bitnum))

    def X32N(self,is_sensor, row , bitnum):
        '''
        :brief:
        :param:
        :return: - no return
        '''
        return self.channel.req_com("X32N_DEBUG_CFG %d %d %d"%(is_sensor, row, bitnum))

    def TOUCH_PAD0(self,is_sensor, row , bitnum):
        '''
        :brief:
        :param:
        :return: - no return
        '''
        return self.channel.req_com("TOUCH_PAD0_DEBUG_CFG %d %d %d"%(is_sensor, row, bitnum))

    def TOUCH_PAD1(self,is_sensor, row , bitnum):
        '''
        :brief:
        :param:
        :return: - no return
        '''
        return self.channel.req_com("TOUCH_PAD1_DEBUG_CFG %d %d %d"%(is_sensor, row, bitnum))

    def TOUCH_PAD2(self,is_sensor, row , bitnum):
        '''
        :brief:
        :param:
        :return: - no return
        '''
        return self.channel.req_com("TOUCH_PAD2_DEBUG_CFG %d %d %d"%(is_sensor, row, bitnum))

    def TOUCH_PAD3(self,is_sensor, row , bitnum):
        '''
        :brief:
        :param:
        :return: - no return
        '''
        return self.channel.req_com("TOUCH_PAD3_DEBUG_CFG %d %d %d"%(is_sensor, row, bitnum))
    def TOUCH_PAD4(self,is_sensor, row , bitnum):
        '''
        :brief:
        :param:
        :return: - no return
        '''
        return self.channel.req_com("TOUCH_PAD4_DEBUG_CFG %d %d %d"%(is_sensor, row, bitnum))

    def TOUCH_PAD5(self,is_sensor, row , bitnum):
        '''
        :brief:
        :param:
        :return: - no return
        '''
        return self.channel.req_com("TOUCH_PAD5_DEBUG_CFG %d %d %d"%(is_sensor, row, bitnum))

    def TOUCH_PAD6(self,is_sensor, row , bitnum):
        '''
        :brief:
        :param:
        :return: - no return
        '''
        return self.channel.req_com("TOUCH_PAD6_DEBUG_CFG %d %d %d"%(is_sensor, row, bitnum))

    def TOUCH_PAD7(self,is_sensor, row , bitnum):
        '''
        :brief:
        :param:
        :return: - no return
        '''
        return self.channel.req_com("TOUCH_PAD7_DEBUG_CFG %d %d %d"%(is_sensor, row, bitnum))

    def TOUCH_PAD8(self,is_sensor, row , bitnum):
        '''
        :brief:
        :param:
        :return: - no return
        '''
        if self.chipv == "CHIP722":
            return self.channel.req_com("TOUCH_PAD8_DEBUG_CFG %d %d %d"%(is_sensor, row, bitnum))
        else:
            pass

    def TOUCH_PAD9(self,is_sensor, row , bitnum):
        '''
        :brief:
        :param:
        :return: - no return
        '''
        if self.chipv == "CHIP722":
            return self.channel.req_com("TOUCH_PAD9_DEBUG_CFG %d %d %d"%(is_sensor, row, bitnum))
        else:
            pass

    def TOUCH_PAD10(self,is_sensor, row , bitnum):
        '''
        :brief:
        :param:
        :return: - no return
        '''
        if self.chipv == "CHIP722":
            return self.channel.req_com("TOUCH_PAD10_DEBUG_CFG %d %d %d"%(is_sensor, row, bitnum))
        else:
            pass

    def TOUCH_PAD11(self,is_sensor, row , bitnum):
        '''
        :brief:
        :param:
        :return: - no return
        '''
        if self.chipv == "CHIP722":
            return self.channel.req_com("TOUCH_PAD11_DEBUG_CFG %d %d %d"%(is_sensor, row, bitnum))
        else:
            pass

    def TOUCH_PAD12(self,is_sensor, row , bitnum):
        '''
        :brief:
        :param:
        :return: - no return
        '''
        if self.chipv == "CHIP722":
            return self.channel.req_com("TOUCH_PAD12_DEBUG_CFG %d %d %d"%(is_sensor, row, bitnum))
        else:
            pass

    def TOUCH_PAD13(self,is_sensor, row , bitnum):
        '''
        :brief:
        :param:
        :return: - no return
        '''
        if self.chipv == "CHIP722":
            return self.channel.req_com("TOUCH_PAD13_DEBUG_CFG %d %d %d"%(is_sensor, row, bitnum))
        else:
            pass

    def TOUCH_PAD14(self,is_sensor, row , bitnum):
        '''
        :brief:
        :param:
        :return: - no return
        '''
        if self.chipv == "CHIP722":
            return self.channel.req_com("TOUCH_PAD14_DEBUG_CFG %d %d %d"%(is_sensor, row, bitnum))
        else:
            pass

    def RTC_PAD19(self,is_sensor, row , bitnum):
        '''
        :brief:
        :param:
        :return: - no return
        '''
        if self.chipv == "CHIP722":
            return self.channel.req_com("RTC_PAD19_DEBUG_CFG %d %d %d"%(is_sensor, row, bitnum))
        else:
            pass

    def RTC_PAD20(self,is_sensor, row , bitnum):
        '''
        :brief:
        :param:
        :return: - no return
        '''
        if self.chipv == "CHIP722":
            return self.channel.req_com("RTC_PAD20_DEBUG_CFG %d %d %d"%(is_sensor, row, bitnum))
        else:
            pass

    def CLK(self, row , clk_out_num, clk_gate):
        '''
        :brief:
        :param:
        :return: - no return
        '''
        return self.channel.req_com("CLK_OUT_DEBUG_CFG %d %d %d"%(row, clk_out_num, clk_gate))

    def increasement_flag(self, initial):
        '''
        :brief:
        :param:
        :return: - no return
        '''
        return self.channel.req_com("increasement_flag %d"%(initial))

    def apll_en(self):
        '''
        :brief:
        :param:
        :return: - no return
        '''
        return self.channel.req_com("apll_en")

    def gpio_pulse(self, rtc_gpio_no, delay_us, drv = 3, mode = 0):
        '''
        :brief:
        :param:
        :return: - no return
        '''
        return self.channel.req_com("gpio_pulse %d %d %d %d"%(rtc_gpio_no, drv, delay_us, mode))

    def pull_internal_voltage(self,channel):
        '''
        :brief: set pad for TEST_MUX
        :param:
                channel: SAR2_CHANNEL
        :return: - no return
        '''
        if self.chipv == "CHIP722" or 'CHIP723':
            return self.channel.req_com("pull_internal_voltage %d"%(channel))
        else:
            pass

    def set_test_mux(self,is_rtc,test_mux):
        '''
        :brief: connect internal voltage to TEST_MUX
        :param:
                                    is_rtc == 1 :
                                    test_mux             0           1           2            3
                voltage(TEST_MUX) =                   vdd_rtc     vref_sar1    vdd_dig       vcm
                                    is_rtc ==0 :
                                    test_mux             0           1           2            3
                voltage(TEST_MUX) =                   vref_sar2     rp          vp           vn
        :return: - no return
        '''
        if self.chipv == "CHIP722":
            return self.channel.req_com("rtc_test_mux_meas %d %d"%(is_rtc,test_mux))
        else:
            pass