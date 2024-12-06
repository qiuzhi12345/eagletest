class POWER(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel

    def ldo_debug(self, select, adc2_channel, enable = True, is_rtc = True):
        '''
        :brief:
            debug internal ldo, include rtc_ldo & adc_vref & digital_ldo, pull internal ldo voltage to adc2_channel pad.
        :param:
            - adc2_channel: which pad internal ldo connected to
            - enable: enable ldo debug or not
        for ESP32:
            - select: select which to debug
                - 0: rtc internal voltage
                - 1: adc2_vref
                - 2: digital internal voltage
        for CHIP722:
            if is_rtc == 1:
                select:             0           1           2            3
                voltage(TEST_MUX): vdd_rtc    vref_sar1    vdd_dig       vcm
            if is_rtc ==0:
                select:             0           1        2            3
                voltage(TEST_MUX): vref_sar2   rp       vp           vn
        :return:
            no return
        '''
        if self.chipv == "ESP32":
            return self.channel.req_com("ldo_debug %d %d %d"%(enable, select, adc2_channel))
        else:
            return self.channel.req_com("ldo_debug %d %d %d %d"%(enable, select, adc2_channel, is_rtc))
    
    def vdd33_read(self, filter = 1):
        '''
        :brief:
            read power voltage
        :param:
            no
        :return:
            no return
        '''
        return self.channel.req_com("read_vdd33 %d"%(filter))

    def open_rf(self):
        '''
        :brief:
            open rf
        :param:
            no
        :return:
            no return
        '''
        if self.chipv == "CHIP722":
            return self.channel.req_com("open_rf")

    def close_rf(self):
        '''
        :brief:
            close rf
        :param:
            no
        :return:
            no return
        '''
        if self.chipv == "CHIP722":
            return self.channel.req_com("close_rf")
    
    def deepsleep_cur(self, dbg, slp_mode, ana2_pd = 7, wakeup_opt = 8, slp_time = 0xfffffff):
        '''
        :brief:
            deepsleep current configuration.
        :param:
            - dbg: in CHIP722, it can be set to 0~15, in ESP32 can be set to 0~3;
            - slp_mode
                - 0x71: MEM_PU & PERI_PU
                - 0x7d: MEM_PD & PERI_PU
                - 0x7f: MEM_PD & PERI_PD
            - ana2_pd: set to 7 in Chip722
        :return:
            no return
        '''
        if self.chipv == "ESP32":
            return  self.channel.req_com("deepsleep_current %d %d %d %d"%(dbg, slp_mode, wakeup_opt, slp_time), 1)
        elif self.chipv == "CHIP722":
            return  self.channel.req_com("deepsleep_current %d %d %d"%(dbg, slp_mode, ana2_pd), 1)
        else:
            return  self.channel.req_com("deepsleep_current %d %d"%(dbg, slp_mode), 1)

    def lightsleep_cur(self, dbg_slp, dig_dbias, slp_mode, wakeup_opt = 8, slp_time = 0xfffffff, pd_rom_ram_cache = 1, xtal_fpu = 0, pll_320m_fpu = 0, pll_480m_fpu = 0, apll_fpu = 0, pull_ldo = 0, mem_fpu = 0, rtc_dbias = 0, pd_cur_slp = 1, biasslp_slp = 1):
        '''
        :brief:
            lightsleep current configuration.
        :param:
            - dbg
            - dig_dbias: dig_dbias_slp
            - slp_mode: sleep mode
            - pd_rom_ram_cache: power down rom, ram, cache
            - xtal_fpu: force power up xtal
            - pll_320m_fpu: force power up 320M PLL
            - pll_480m_fpu: force power up 480M PLL
            - apll_fpu: force power up APLL
            - pull_ldo:
             - 1: pull ldo
             - 0: not pull ldo
        :return:
            no return
        '''
        if self.chipv == "ESP32":
            return self.channel.req_com("lightsleep_current %d %d %d %d %d %d %d %d %d %d"%(dbg_slp, dig_dbias, slp_mode, wakeup_opt, slp_time, xtal_fpu, pll_320m_fpu, pll_480m_fpu, apll_fpu, mem_fpu, rtc_dbias), 1)
        elif self.chipv == "CHIP722":
            return self.channel.req_com("lightsleep_current %d %d %d %d %d %d %d %d %d %d %d %d"%(dbg_slp, dig_dbias, slp_mode, wakeup_opt, slp_time, pd_rom_ram_cache, xtal_fpu, pll_320m_fpu, pll_480m_fpu, apll_fpu, pull_ldo, rtc_dbias), 1)
        else:
            return self.channel.req_com("lightsleep_current %d %d %d %d %d %d %d %d %d %d %d %d %d %d"%(dbg_slp, dig_dbias, slp_mode, wakeup_opt, slp_time, pd_rom_ram_cache, xtal_fpu, pll_320m_fpu, pll_480m_fpu, apll_fpu, pull_ldo, rtc_dbias, pd_cur_slp, biasslp_slp), 1)

    def modemsleep_cur(self, close_phy = 1, cpu_freq = 1, wifi_pd = 0, wifi_clkgating = 0, peri_clkgating = 0, cpu_waiti = 0, cpu_keeprun = 0, use_cache = 0, rtc_dbias = 4, dig_dbias = 4):
        '''
        :brief:
            modemsleep current configuration.
        :param:
            - close_phy: 1: close phy, 0: not close.
            - cpu_freq:
                - 3: 240M (pll_480M)
                - 2: 160M (pll_480M)
                - 1: 80M (pll_480M)
                - 0: XTAL (xtal: main)
                - 7: 20M (CHIP722)
                - 8: 10M (CHIP722)
                - 9: 2M (CHIP722)
            - wifi_pd: wifi force pd.
            - wifi_clkgating: wifi clock gating
            - peri_clkgating: peri clock gating
            - cpu_waiti: cpu wait interrupt
            - cpu_keeprun: cpu keep run, GPIO0 need connected to GND.
            - use_cache: use cache when value is 1. GPIO1 must connected to high.
            - rtc_dbias: rtc_dbias_wak
            - dig_dbias: dig_dbias_wak.
        :return:
            no return
        '''
        if self.chipv == "ESP32":
            return self.channel.req_com("modemsleep_current %d %d %d %d %d %d %d %d %d"%(close_phy, cpu_freq, wifi_pd, wifi_clkgating, peri_clkgating, cpu_waiti, cpu_keeprun, rtc_dbias, dig_dbias), 1)
        else:
            return self.channel.req_com("modemsleep_current %d %d %d %d %d %d %d %d %d %d"%(close_phy, cpu_freq, wifi_pd, wifi_clkgating, peri_clkgating, cpu_waiti, cpu_keeprun, use_cache, rtc_dbias, dig_dbias), 1)

    def sleep_cur_config(self, pd_cur_slp = 1, pd_cur_monitor = 1, biasslp_slp = 1, biasslp_monitor = 1, dbg_slp = 15, dbg_monitor = 0):
        '''
        :brief:
            configurations used before lightsleep or deepsleep, valid from chip722_m1
        '''
        return self.channel.req_com("rtc_sleep_bias_init %d %d %d %d %d %d"%(pd_cur_slp, pd_cur_monitor, biasslp_slp, biasslp_monitor, dbg_slp, dbg_monitor))
