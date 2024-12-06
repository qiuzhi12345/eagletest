# -- coding: utf-8 --
class TSEN(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel

    def config(self, xpd_wait = 5, clk_gate = 1, clk_inv = 0, clk_div = 3, data_inv = 0, ulp = 0, xpd_force = 0, dac = 15, div_chop = 2):
        '''
        :brief:
            configure temperature sensor.
        :param:
            - xpd_wait: 12bits, cycles between power up temperature sensor and reset it;
            - clk_gate: 1bit, clock gating temperature sensor when it is power down;
            - clk_inv: 1bit, invert temperature sensor clock;
            - clk_div: 8bits, clock divide factor for temperature sensor clock, must set > 1;
            - data_inv: 1bit, invert data received from temperature sensor;
            - ulp: control by ulp or software;
            - xpd_force: begin use from chip722, 2bits:
              - when 3, force tsen xpd open,;
              - when 2, force tsen xpd close;
              - when 0 or 1, tsen_cntl control tsen xpd open or close.
            - dac: begin use from chip722, 4bits, can set to follow values:
             - 测量温度范围为50~125时，dac为5；
             - 测量温度范围为20~100时，dac为13或者7；
             - 测量温度范围为-10~80时，dac;为15；
             - 测量温度范围为-30~50时，dac为11或14；
             - 测量温度范围为-40~20时，DAC为10.
            - div_chop： begin use from chip722, 2bits， only analog use.
        :return:
            no return
        '''
        if self.chipv == "ESP32":
            return self.channel.req_com("tmp_sens_config %d %d %d %d %d %d"%(xpd_wait, clk_gate, clk_inv, clk_div, data_inv, ulp))
        else:
            return self.channel.req_com("tmp_sens_config %d %d %d %d %d %d %d %d %d"%(xpd_wait, clk_gate, clk_inv, clk_div, data_inv, ulp, xpd_force, dac, div_chop))

    def read(self):
        '''
        :brief:
            read temperature data.
        :param:
            no param
        :return:
            return temp data.
        '''
        return self.channel.req_com("tmp_read")

    def int_enable(self, enable = 1):
        '''
        :brief:
            enable tsen interrupt
        :param:
            - enable: 1 or 0, enable or not, default value is 1.
        :return:
            no return
        '''
        if self.chipv == "CHIP722" or self.chipv == "CHIP723":
            return self.channel.req_com("tsen_int_enable %d"%(enable))

    def rtc_int_raw(self):
        '''
        :brief:
            get tsen int raw status in rtc int sts
        :param:
            no param
        :return:
            return raw
        '''
        if self.chipv == "CHIP722" or self.chipv == "CHIP723":
            return self.channel.req_com("rtc_int_raw_tsen")

    def rtc_int_enable(self):
        '''
        :brief:
            enable tsen int in rtc int
        :param:
            no param
        :return:
            return mask status
        '''
        if self.chipv == "CHIP722" or self.chipv == "CHIP723":
            return self.channel.req_com("rtc_int_enable_tsen")

    def rtc_int_sts(self):
        '''
        :brief:
            get tsen int mask status in rtc int sts
        :param:
            no param
        :return:
            return mask status
        '''
        if self.chipv == "CHIP722" or self.chipv == "CHIP723":
            return self.channel.req_com("rtc_int_sts_tsen")

    def rtc_int_clr(self):
        '''
        :brief:
            clear tsen interrupt in rtc int
        :param:
            no param
        :return:
            no return
        '''
        if self.chipv == "CHIP722" or self.chipv == "CHIP723":
            return self.channel.req_com("rtc_int_clr_tsen")

    def close(self):
        '''
        :brief:
            close temperature sensor to make it not work.
        :param:
            no param
        :return:
            no return
        '''
        return self.channel.req_com("tsen_close")
