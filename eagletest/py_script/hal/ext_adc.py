class EXT_ADC(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel

    def cfg_adsadc(self, addr, mode, cfg_data):
        '''
        :brief:
            configuration of ESP chip for control of external ADC device (ADS1115)
        :param:
            - addr: 8-bit, i2c address of ads1115 
            - mode : configuration register address
                - 1: config register
                - 2: lo_thresh register
                - 3: hi_thresh register
            - cfg_data: 
                :mode=1:
                    - 0: continuous conversion(MUX=6,PGA=1,DR=860,MODE=0,COMP_QUE=3)
                    - 1: single-shot acquisition(MUX=6, PGA=1, DR=860, MODE=1,COMP_QUE=3)
                    - else: configure according to the table 8 in ads1115.pdf, if COMP_QUE bits<3, 
                        lo_thresh register(mode=2) and hi_thresh register(mode=3) should be configured
                :mode=2:
                    cfg_data is the value of lo_thresh register
                :mode=3:
                    cfg_data is the value of hi_thresh register
        :return:
            no return
        '''
        return self.channel.req_com("cfg_adsadc 0x%x %d 0x%x"%(addr, mode, cfg_data))

    def pre_rd_adsadc(self, addr, reg_addr):
        '''
        :breif:
            pre-configuration of reading ads1115. For any read operation, commands to execute should be
            first "pre_rd_adsadc" and then "esp_rd_adsadc".
        :param:
            - addr: 8-bit, i2c address of ads1115 
            - reg_addr: sub-address of slave
                - 0: conversion register
                - 1: config register
                - 2: lo_thres register
                - 3: hi_thres register
        :return:
            no return
        '''
        return self.channel.req_com("pre_rd_adsadc 0x%x %d"%(addr, reg_addr))

    def esp_rd_adsadc(self, addr, reg_addr):
        '''
        :breif:
            read data out from ads1115. For any read operation, commands to execute should be
            first "pre_rd_adsadc" and then "esp_rd_adsadc".
        :param:
            - addr: 8-bit, i2c address of ads1115 
            - reg_addr: sub-address of slave
                - 0: conversion register
                - 1: config register
                - 2: lo_thres register
                - 3: hi_thres register
        :return:
            return the result of ads1115 acquisition
        '''
        return self.channel.req_com("esp_rd_adsadc 0x%x %d"%(addr, reg_addr))