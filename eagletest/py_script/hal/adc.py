# -- coding: utf-8 --
class RTC_ADC1(object):
    
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel

    def xpd_enable(self, enable = 1):
        return self.channel.req_com("xpd_sar_enable %d"%(enable))

    def config(self, amp_wait = 10, bit_width = 3, clk_gate = True, data_inv = False, sample_cycle = 2, sample_num = 0, init_code_msb = 0x3f, init_code_lsb = 0):
        '''
        :brief:
            set global parameter for each rtc adc1 channel
        :param:
            - amp_wait: wait cycle between adc xpd and start.
            - bit_width: 
                - Before CHIP723: resolution, bit width of SAR ADC1, 00:for 9-bit, 01:for 10-bit, 10:for 11-bit, 11: for 12-bit.
                - From CHIP723: delete it, data width is 13-bit.
            - clk_gate: 1: clock gating SARADC sensor when it is idle; 0: no clock gating.
            - data_inv: 
                - Before CHIP723, need invert SAR ADC1 data received from ADC1 sensor;
                - From CHIP723, don't invert.
            - sample_cycle: how many cycles that ADC controller need to receive data form ADC1 sensor.
            - sample_num: how many times ADC convertion need to exercise every time ADC controller is triggered.
        :return:
            no return
        '''
        if self.chipv == "ESP8266":
            pass
        elif self.chipv == "ESP32" or self.chipv == "CHIP722":
            return self.channel.req_com("rtc_adc1_config %d %d %d %d %d %d"%(amp_wait, bit_width, clk_gate, data_inv, sample_cycle, sample_num))
        else:
            return self.channel.req_com("rtc_adc1_config %d %d %d %d %d %d %d"%(amp_wait, clk_gate, data_inv, sample_cycle, sample_num, init_code_msb, init_code_lsb))

    def set(self, atten = 3, pad = 0, ulp = False):
        '''
        :brief:
            single config for adc1 channel
        :param:
            - atten: attenuation, it can be set 0~3.
            - pad: which rtc adc1 channel will be set.
        :return:
            no return
        '''
        if self.chipv == "ESP8266":
            pass
        else:
            return self.channel.req_com("rtc_adc1_init %d %d %d"%(atten, pad, ulp))

    def read(self, filter_en = 1):
        '''
        :brief:
            rtc adc1 data
                - From CHIP723, adc data is 13-bit.
                - Before CHIP723, depend on bit-width: 00:for 9-bit, 01:for 10-bit, 10:for 11-bit, 11: for 12-bit.
        :param:
            no param.
        :return:
            return sample result
        '''
        if self.chipv == "ESP8266":
            from hal.common import I2C
            from hal.common import MEM
            self.__i2c = I2C(self.channel, self.chipv)
            self.__mem = MEM(self.channel, self.chipv)
            self.__i2c.i2c_wrm(0x6c, 2, 0, 5, 5, 1)
            self.__mem.setmask(0x60000D5c,0x200000)
            self.__mem.clrmask(0x60000D5c,0x800000)
            #force en
            self.__mem.clrmask(0x60000D50,0x2)
            self.__mem.setmask(0x60000D50,0x2)
            e=[1,2,3,4,5,6,7,8]
            sar_out = ''
            sar_out_temp = 0
            for i in range(0,8):
                c=self.__mem.rd(0x60000D80+i*4)&0xfff
                e[i] = 2048-c
                sar_out += '%d,'%e[i]
                sar_out_temp+=e[i]
            self.__i2c.i2c_wrm(0x6c, 2, 0, 5, 5, 1)   # select Test MUX
            return sar_out_temp/8.0
        else:
            return self.channel.req_com("rtc_adc1_read %d"%(filter_en))

    def sar1_dref(self,sar1_dref):
        if self.chipv == "CHIP722":
            return self.channel.req_com("set_saradc1_dref %d"%(sar1_dref))

class RTC_ADC2(object):
    
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel

    def config(self, bit_width = 3, clk_gate = True, data_inv = False, sample_cycle = 2, sample_num = 0, clk_div = 2, init_code_msb = 0x3f, init_code_lsb = 0):
        '''
        :brief:
            set global parameter for each rtc adc2 channel
        :param:
            - bit_width: resolution, bit width of SAR ADC2, 00:for 9-bit, 01:for 10-bit, 10:for 11-bit, 11: for 12-bit.
            - clk_gate: 1: clock gating SARADC sensor when it is idle; 0: no clock gating.
            - data_inv: 
                - Before CHIP723, need invert SAR ADC2 data received from ADC2 sensor;
                - From CHIP723, don't invert.
            - sample_cycle: how many cycles that ADC controller need to receive data form ADC2 sensor.
            - sample_num: how many times ADC convertion need to exercise every time ADC controller is triggered.
        :return:
            no return
        '''
        if self.chipv == "ESP32":
            return self.channel.req_com("rtc_adc2_config %d %d %d %d %d"%(bit_width, clk_gate, data_inv, sample_cycle, sample_num))
        elif self.chipv == "CHIP722":
            return self.channel.req_com("rtc_adc2_config %d %d %d %d %d %d"%(bit_width, clk_gate, data_inv, sample_cycle, sample_num, clk_div))
        else:
            return self.channel.req_com("rtc_adc2_config %d %d %d %d %d %d %d"%(clk_gate, data_inv, sample_cycle, sample_num, clk_div, init_code_msb, init_code_lsb))

    def set(self, atten = 3, pad = 0, ulp = False, test_pad_en = 0):
        '''
        :brief:
            - single config for adc2 channel
        :param:
            - atten: attenuation, it can be set 0~3.
            - pad: which rtc adc2 channel will be set.
            - test_pad_en: only used to debug internal vdd3.3v.
        :return:
            - no return
        '''
        if self.chipv == "ESP8266":
            pass
        else:
            return self.channel.req_com("rtc_adc2_init %d %d %d %d"%(atten, pad, ulp, test_pad_en))

    def read(self, filter_en = 1):
        '''
        :brief:
            read rtc adc2 sample result
        :param:
            no param.
        :return:
            return sample result
        '''
        return self.channel.req_com("rtc_adc2_read %d"%(filter_en))
        
    def sar2_dref(self,sar2_dref):
        if self.chipv == "CHIP722":
            return self.channel.req_com("set_saradc2_dref %d"%(sar2_dref))

class DIG_ADC(object):
        
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel

    def config(self, data_to_i2s = 1, work_mod = 0, sample_cycle = 2, clk_div = 2, clk_gate = 1, rst_wait = 8, standby_wait = 0, start_wait = 8,  num_limit = 1):
        '''
        :brief:
            set global parameter for dig adc1&adc2.
        :param:
            - data_to_i2s: i2s receive data from adc or not, can set to [0, 1]
            - work_mod: two digital adc controller work single or double at the same time or alter, 00:single, 01:double, 10:alter, can set to [0~2].
            - sample_cycle: cycles between DIG ADC controller start ADC sensor and beginning to receive data from sensor, can set to [0~0xff].
            - clk_div: clock divider factor for ADC sensor clock, can set to [0~0xff].
            - clk_gate: 1: clock gating SARADC sensor when it is idle, 0: no clock gating.
            - rst_wait: the time that ADC sensor need to reset, can set to [0~0xff].
            - standby_wait: the time that ADC controller wait next sample_start signal, if the time is over, clock gating the ADC sensor, can set to [0~0xff].
            - start_wait: the time that ADC sensor can work in normal after sample_start signal, can set to [0~0xff].
            - num_limit: meas_num enable, can set to [0~1], 1: enable meas_num, 0: disable meas_num.
        :return:
            no return
        '''
        if self.chipv == "ESP8266":
            pass
        else:
            return self.channel.req_com("dig_adc_config %d %d %d %d %d %d %d %d %d"%(data_to_i2s, work_mod, sample_cycle, clk_div, clk_gate, rst_wait, standby_wait,start_wait, num_limit))

    def set_adc1(self, max_meas_num = 16 , sar1_patt_len = 15, sar1_inv = 1, table1 = 0xffffffff, table2 = 0xffffffff, table3 = 0xffffffff, table4 = 0xffffffff):
        '''
        :brief:
            single config for dig adc1 controller.
        :param:
            - max_meas_num: maximum times for DIG controller to do ADC measurement.
            - sar1_patt_len: the number of order in table.
            - sar1_inv: invert data received from ADC1 sensor or not.
            - table1: No.0 ~ 3 order, length of each order is one BYTE,such as {chan[3:0], bit_width[1:0], atten[1:0]}.
            - table2: No.4 ~ 7 order, length of each order is one BYTE,such as {chan[3:0], bit_width[1:0], atten[1:0]}.
            - table3: No.8 ~ 11 order, length of each order is one BYTE,such as {chan[3:0], bit_width[1:0], atten[1:0]}.
            - table4: No.12 ~15 order, length of each order is one BYTE,such as {chan[3:0], bit_width[1:0], atten[1:0]}.
        :return:
            no return
        '''
        if self.chipv == "ESP8266":
            pass
        else:
            return self.channel.req_com("dig_adc1_init %d %d %d %d %d %d %d"%(max_meas_num , sar1_patt_len, sar1_inv, table1, table2, table3, table4))

    def set_adc2(self, max_meas_num = 16 , sar2_patt_len = 15, sar2_inv = 1, table1 = 0xffffffff, table2 = 0xffffffff, table3 = 0xffffffff, table4 = 0xffffffff):
        '''
        :brief:
            single config for dig adc2 controller.
        :param:
            - max_meas_num: maximum times for DIG controller to do ADC measurement.
            - sar2_patt_len: the number of order in table.
            - sar2_inv: invert data received from ADC2 sensor or not.
            - table1: No.0 ~ 3 order, length of each order is one BYTE,such as {chan[3:0], bit_width[1:0], atten[1:0]}.
            - table2: No.4 ~ 7 order, length of each order is one BYTE,such as {chan[3:0], bit_width[1:0], atten[1:0]}.
            - table3: No.8 ~ 11 order, length of each order is one BYTE,such as {chan[3:0], bit_width[1:0], atten[1:0]}.
            - table4: No.12 ~15 order, length of each order is one BYTE,such as {chan[3:0], bit_width[1:0], atten[1:0]}.
        :return:
            no return
        '''
        if self.chipv == "ESP8266":
            pass
        else:
            return self.channel.req_com("dig_adc2_init %d %d %d %d %d %d %d"%(max_meas_num , sar2_patt_len, sar2_inv, table1, table2, table3, table4))

    def i2s(self, i2s_rx_bck_div_num = 0x3f, fifo_mode = 1):
        '''
        :brief:
            config i2s parameter
        :param:
            - i2s_rx_bck_div_num: controll the rate of i2s read adc data
            - fifo_mode:
                - 0: 16bit double channel, used in digital adc double mode or alternate mode.
                - 1: 16bit single channel, used in digital adc single mode.
        :return:
            no return
        '''
        if self.chipv == "ESP8266":
            pass
        else:
            return self.channel.req_com("i2s_config %d %d"%(i2s_rx_bck_div_num, fifo_mode))

    def read(self, rx_eof_num = 32, i2s_trigger = 1, trigger_delay = 1, isprint = 0):
        '''
        :brief:
            trigger i2s or reg_force start to drive adc sample data,and reveive data to DMA_BUF.
        :param:
            - rx_eof_num: reveive the number of data ,rx_eof_num = max_meas_num / 2.
            - i2s_trigger: use i2s_drive ,otherwise use reg force.
            - trigger_delay: drive gap when use reg force.
            - isprint: printf DMA_BUF enable
        :return:
            return DMA_BUF's address
        '''
        if self.chipv == "ESP8266":
            pass
        else:
            return self.channel.req_com("dig_adc_read %d %d %d %d"%(rx_eof_num, i2s_trigger, trigger_delay, isprint))

    def test_pad_select(self, enable = 1):
        '''
        :brief:
            enable internal vdd3.3 debug
        :param:
            - enable: enable or not.
        :return:
            no return
        '''
        if self.chipv == "ESP8266":
            pass
        else:
            return self.channel.req_com("test_pad_select %d"%(enable))

    def debug(self, debug_bit_sel, sar_debug_bit_sel, pdac1_func_sel, rtc_gpio_no):
        '''
        :brief:
            trigger i2s or reg_force start to drive adc sample data,and reveive data to DMA_BUF.
        :param:
            - rx_eof_num: reveive the number of data ,rx_eof_num = meas_num / 2.
            - i2s_trigger: use i2s_drive ,otherwise use reg force.
            - trigger_delay: drive gap when use reg force.
            - isprint: printf DMA_BUF enable
        :return:
            return DMA_BUF's address
        '''
        if self.chipv == "ESP8266":
            pass
        else:
            return self.channel.req_com("saradc_debug %d %d %d %d"%(debug_bit_sel, sar_debug_bit_sel, pdac1_func_sel, rtc_gpio_no))

    def dig_adc_timer_en(self, enable = 1, cycle = 128):
        '''
        :brief:
            enable digital adc timer, only used in test adc2 arbiter.
        :param:
            - enable: 使能timer触发adc.
            - cycle: timer触发的目标计数值.
        :return:
            no return
        '''
        if self.chipv == "CHIP722":
            return self.channel.req_com("dig_adc_timer_en %d %d"%(enable, cycle))

    def dig_adc2_start_sts(self):
        '''
        :brief:
            dig_adc2 timer方式，读取start中断，如果该值为１表明可以开始digital采样
        :param:　无
        :return:
            return　digital adc2 start status by timer mode.
        '''
        if self.chipv == "CHIP722":
            return self.channel.req_com("dig_adc2_start_status")

class ADC2_ARB(object):

    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel

    def rtc_force(self):
        '''
        :brief:
            仲裁器工作在digital_power_domain，在deep_sleep下仲裁器无法工作；为了满足deep_sleep模式下RTC控制器能够正常工作，需要设置SAR2_RTC_FORCE为1，将SARADC1直接授权给RTC控制器
        :param: no param
        :return: no return
        '''
        if self.chipv == "CHIP722":
            return self.channel.req_com("saradc2_rtc_force")
        else:
            pass

    def config(self, grant_force = 0, rtc_force = 0, dig_force = 0, wifi_force = 0, fix_pri = 0, rtc_pri = 0, dig_pri = 0, wifi_pri = 0):
        '''
        :brief:
            配置adc2仲裁参数
        :param:
         - grant_force: 屏蔽仲裁器，１: 屏蔽，仲裁器无效，0: 不屏蔽，仲裁器有效；
         - rtc_force:　仲裁器屏蔽时，是否将使用权授权给rtc，１:　授权，0: 禁止授权；
         - dig_force:　仲裁器屏蔽时，是否将使用权授权给digital，1: 授权，0: 禁止授权；
         - wifi_force:　仲裁器屏蔽时，是否将使用权授权给wifi，1: 授权，0: 禁止授权；
         - fix_pri: 仲裁时，优先级是否固定，1: 固定，　0: 不固定。
         - rtc_pri: rtc控制器的仲裁优先级，值越大优先级越高，范围为[0~2]；
         - dig_pri: digital控制器的仲裁优先级，值越大优先级越高，范围为[0~2]；
         - wifi_pri: wifi控制器的仲裁优先级，值越大优先级越高，范围为[0~2]；
        :return:
        '''
        if self.chipv == "CHIP722":
            return self.channel.req_com("adc2arb_config %d %d %d %d %d %d %d %d"%(grant_force, rtc_force, dig_force, wifi_force, fix_pri, rtc_pri, dig_pri, wifi_pri))
        else:
            pass

    def get_vdd33(self, sample_num = 0):
        '''
        :brief:
            仅用于arbiter测试中。
        :param: sample_num最大值为７．
        :return: vdd33数值
        '''
        if self.chipv == "CHIP722":
            return self.channel.req_com("dbg_get_vdd33 %d"%(sample_num))
        else:
            pass