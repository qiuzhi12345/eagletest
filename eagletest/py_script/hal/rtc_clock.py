# -- coding: utf-8 --
class RTC_CLK(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel

    def set_32k(self, dac = 3, dres = 3, dbias = 3, dgm = 3, dbuf = 1):
        '''
        set rtc 32k parameter
        for ESP32, referance config is: dac = 1, dres = 3, dbias = 0
        For CHIP722, referance config is: dac = 3, dres = 3, dgm = 3, dbuf = 1
        :dac:
            - before chip722: can set [0~3];
            - chip722: can set [0~0x3f]
        :dres:
            - before chip722: can set [0~3]
            - chip722: can set [0~7]
        :dbias:
            - before chip722: can set [0~3]
        :dgm:
            - chip722: can set [0~7], must same as dac
        :dbuf:
            - chip722: can set [0~1]
        :return:
            - no return
        ''' 
        if self.chipv == "ESP32":
            return self.channel.req_com("rtc_clk_32k_set %d %d %d"%(dac, dres, dbias))
        else:
            return self.channel.req_com("x32k_set %d %d %d %d"%(dac, dres, dgm, dbuf))

    def start_32k(self, enable = 1):
        '''
        enable rtc 32k clock
        
        :enable:
            - 0: disable 32k clock
            - 1: enable 32k clock
        :return:
            -no return
        '''
        if self.chipv == "ESP32":
            return self.channel.req_com("rtc_clk_32k_enable %d"%(enable))
        else:
            return self.channel.req_com("x32k_enable %d"%(enable))

    def help_starting_32k(self, div_num = 1, diva = 4, divb = 1, delay = 0, ext_dac = 1):
        '''
        帮助并加速 xtal 32k起振,C code中默认用40M帮助起振， div_num + divb/diva = f_lp_source / 32 = 40M / 32 = 1 + 1/4， 所以div_num为1， divb为1， diva为4.
        :div_num: 帮助起振的时钟，分频为32k的整数配置部分， 12bits;
        :diva： 帮助起振的时钟，分频为32k的小数配置部分分母， 12bits;
        :divb： 帮助起振的时钟，分频为32k的小数配置部分分子， 12bits;
        :delay: lp_clk默认打开8M，将其切换到40M时可能需要加delay才能成功，单位为微秒;
        :ext_dac: external dac value, can set [0~7], can not use begin chip722.
        :return: no return
        '''
        if self.chipv == "ESP32":
            return self.channel.req_com("rtc_clk_32k_ext_dac_set %d"%(ext_dac))
        else:
            pass
            #return self.channel.req_com("x32k_start_help %d %d %d %d"%(div_num, diva, divb, delay))

    def x32k_startup_time(self, dbuf, dac, dres, dgm):
        '''
        get rtc 32k startup time
        :enable:
        :dac:
            - before chip722: can set [0~3];
            - chip722: can set [0~0x3f]
        :dres:
            - before chip722: can set [0~3]
            - chip722: can set [0~7]
        :dgm:
            - chip722: can set [0~7], must same as dac
        :dbuf:
            - chip722: can set [0~1]
        :return:
            - return startup time
        '''
        return self.channel.req_com("get_xtal_startup_time %d %d %d %d"%(dbuf, dac, dres, dgm))

    def clk_8m_en(self, clk_8m_en = 1, d256_en = 1):
        '''
        enable 8m rtc clk and enable freq div(256) or not
          
        :clk_8m_en: enable 8m or not 
        :d256_en: enable freq_div or not
        :return:
            - no return
        ''' 
        return self.channel.req_com("rtc_clk_8m_enable %d %d"%(clk_8m_en, d256_en))
    
    def apll_en(self, enable, sdm0, sdm1, smd2, o_div):
        '''
        enable or disable APLL and set APLL's parameter
               output frequency is given by the formula:
               apll_freq = xtal_freq * (4 + sdm2 + sdm1/256 + sdm0/65536)/(o_div + 2) * 2)
               
        :enable: enable or disable APLL 
        :sdm0: frequency adjustment parameter,can set[0~255]
        :sdm1: frequency adjustment parameter,can set[0~255]
        :sdm2: frequency adjustment parameter,can set[0~63]
        :o_div: frequency divider, can set[0~31]
        :return:
            - no return
        ''' 
        return self.channel.req_com("rtc_clk_apll_enable %d %d %d %d %d"%(enable, sdm0, sdm1, smd2, o_div))
    
    def clk_32k_en_flag(self):
        '''
        the flag of 32k enable or not

        :return: return the flag:  
           
                - 0: disable
                - 1: enable
        ''' 
        return self.channel.req_com("rtc_clk_32k_enabled")    
    
    def clk_8m_en_flag(self):
        '''
        the flag of 8m enable or not
        
        :return: return the flag
          
                - 0: disable
                - 1: enable
        ''' 
        return self.channel.req_com("rtc_clk_8m_enabled")        
    
    def clk_8md256_en_flag(self):
        '''
        the flag of 8md256 enable or not
        
        :return: return the flag
        
               - 0: disable
               - 1: enable
        ''' 
        return self.channel.req_com("rtc_clk_8md256_enabled")  
    
    def rtc_slow_clk_select(self, slow_freq):
        '''
        select slow clk
        
        :slow_freq: the num of slow clk
         
                - 0: RTC_SLOW_FREQ_RTC 150K  
                - 1: 32K_XTAL
                - 2: 8MD256
        :return: 
             - no return
        ''' 
        return self.channel.req_com("rtc_clk_slow_freq_set %d"%(slow_freq))
    
    def rtc_fast_clk_select(self, fast_freq):
        '''
        select fast clk
        
        :fast_freq: the num of fast clk 
        
                - 0: RTC_FAST_FREQ_XTAL/D4  
                - 1: RTC_FAST_FREQ_8M
        :return:
             - no return
        ''' 
        return self.channel.req_com("rtc_clk_fast_freq_set %d"%(fast_freq))
  
    def set_cpu_freq(self, cpu_freq):
        '''
        set freq_cpu by full implementation, used to set frequency at first time after power up
           
        :cpu_freq: 
               - 0: XTAL (xtal: main)
               - 1: 80M (pll_480M)
               - 2: 160M (pll_480M)
               - 3: 240M (pll_480M)
               - 4: 2M (xtal:div)
               - 5: 80M (pll_320M, added from CHIP722)
               - 6: 160M (pll_320M, added from CHIP722)
        :return:
             - no return
        ''' 
        return self.channel.req_com("rtc_set_cpu_freq %d"%(cpu_freq))
    
    def set_cpu_freq_fast(self, cpu_freq):
        '''
        switch to one of frequencies when cpu is working
         
        :cpu_freq : 
               - 0: XTAL (xtal: main)
               - 1: 80M (pll_320M)
               - 2: 160M (pll_320M)
               - 3: 240M (pll_480M)
               - 4: 2M (xtal:div)
               - 5: 80M (pll_320M, added from CHIP722)
               - 6: 160M (pll_320M, added from CHIP722)
        :return:
             - no return
        ''' 
        return self.channel.req_com("rtc_clk_cpu_freq_set_fast %d"%(cpu_freq))
    
    def get_cpu_freq(self):
        '''
        get frequency in which cpu is working
          
        :return: return current frequency: 
               - 0: XTAL (xtal: main)
               - 1: 80M (pll_320M)
               - 2: 160M (pll_320M)
               - 3: 240M (pll_480M)
               - 4: 2M (xtal:div)
               - 5: 80M (pll_320M, added from CHIP722)
               - 6: 160M (pll_320M, added from CHIP722)
        ''' 
        return self.channel.req_com("rtc_clk_cpu_freq_get")
    
    def trans_cpu_freq_value(self, cpu_freq):
        '''
        transform cpu_freq to its value
        
        :cpu_freq: 
               - 0: XTAL (xtal: main)
               - 1: 80M (pll_320M)
               - 2: 160M (pll_320M)
               - 3: 240M (pll_480M)
               - 4: 2M (xtal:div)
               - 5: 80M (pll_320M, added from CHIP722)
               - 6: 160M (pll_320M, added from CHIP722)
        :return: 
             -return the value of frequency 
        ''' 
        return self.channel.req_com("rtc_clk_cpu_freq_value %d"%(cpu_freq))
         
    def get_xtal_freq(self):
        '''
        get frequency in which xtal is working
        
        :return: return current frequency:
        
               - 0: XTAL_FREQ_AUTO
               - 40: !< 40MHz XTAL
               - 26: !< 26MHz XTAL
               - 24: !< 24MHz XTAL
        ''' 
        return self.channel.req_com("rtc_clk_xtal_freq_get")

    def timegroup_timer0_enable(self):
        '''
        enable time group timer0

        :return: no return
        '''
        return self.channel.req_com("timegroup_timer0_en")

    def update_timergroup_timer0(self):
        '''
        update time group timer0

        :return: no return
        '''
        return self.channel.req_com("update_timer0")

    def read_timergroup_timer0_low(self):
        '''
        read time group timer0 low 32 bits

        :return: return timer0 low 32 bits value
        '''
        return self.channel.req_com("read_timer0_lo")
    
    def read_timergroup_timer0_high(self):
        '''
        read time group timer0 high 32 bits

        :return: return timer0 high 32 bits value
        '''
        return self.channel.req_com("read_timer0_hi")

    def read_timergroup_timer0(self):
        '''
        read time group timer0

        :return: return timer0 value
        '''
        return self.channel.req_com("read_GPtimer")

    def get_clk_calibration(self, cal_clk, slow_clk_cycles = 128):
        '''
        get rtc clock period
        :cal_clk: can set to be 0, 1, 2.
            - 0: RTC_CAL_RTC_MUX
              - ESP32 & before chips: rtc slow clock selected, it may be 150K or 32K or 8MD256, default 150k when chip reset;
              - CHIP722: 150K
            - 1: RTC_CAL_8MD256
            - 2: RTC_CAL_32K_XTAL
        :slow_clk_cycles:
            - slow clock cycles
        :return:
            return period
        '''
        return self.channel.req_com("rtc_clk_cal %d %d"%(cal_clk, slow_clk_cycles))

    def conv_us_to_slowclk(self, time_in_us, period):
        '''
        convert time interval from microseconds to SLOW_CLK cycles
        :time_in_us: Time interval in microseconds, 64bits
        :period: Period of slow clock in microseconds,Q13.19 fixed point format
        :return:
             - lowcycle(low 32bit) & highcycle(high 16bit)
        '''
        return self.channel.req_com("rtc_time_us_to_slowclk %d %d"%(time_in_us, period))

    def conv_slowclk_to_us(self, rtc_cycles, period):
        '''
        calculate test time
        :rtc_cycle: the number of period in rtc slow time
        :period: Period of slow clock in microseconds,Q13.19 fixed point format
        :return:
             - return test time in microseconds
        '''
        return self.channel.req_com("rtc_time_slowclk_to_us %d %d"%(rtc_cycles, period))

    def get_clk_cal_ratio(self, cal_clk, slow_clk_cycles = 128):
        '''
        measure ratio between XTAL frequency and RTC slow clock frequency
        :cal_clk:
               - 0: RTC_CAL_RTC_MUX
               - 1: RTC_CAL_8MD256
               - 2: RTC_CAL_32K_XTAL
        :slow_clk_cycles: slow clock cycles
        :return:
             - return average slow clock period in microseconds, Q13.19 fixed point format
               or 0 if calibration has timed out
        '''
        return self.channel.req_com("rtc_clk_cal_ratio %d %d"%(cal_clk, slow_clk_cycles))