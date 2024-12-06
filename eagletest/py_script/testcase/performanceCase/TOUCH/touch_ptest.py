from baselib.loglib.log_lib import *
from hal.Init import HALS
from hal.common import CHIP_ID
from baselib.instrument import awg
from baselib.tc_platform.common import *
from baselib.tc_platform.tc_platform import *
from baselib.test_channel.com import COM
import re
import scipy.optimize as opt
import matplotlib.pyplot as plt
import pandas as pd
import time

class TouchPtest(object):
    '''
    Used for Touch Function Performance Verfication
    There is 10 touch pad available in ESP32, below is 
    0:GPIO4; 1:GPIO0; 2:GPIO2; 3:MTDO; 4:MTCK; 5:MTDI; 6:MTMS; 7:GPIO27; 8:32K_XN; 9:32K_XP 

    For TOUCH tripping threshold level configuration:
    Use touch_global_init command under hal/touch to setup
    Use below equation to calculate touch tripping voltage level
    - Vrefh = 2.4 + 0.1*drefh - 0.5*(3-drange)
    - Vrefl = 0.5 + 0.1*drefl
    '''
    def __init__(self, channel, chipv = "AUTO"):
        self.chip = HALS(channel, chipv)
        self.channel = self.chip.channel
        self.chipv = self.chip.chipv


    def touch_anaTest_init(self,touch_no,dac=7,tie_opt=0):
        '''
        :brief:
            choose pad to be tested but also sets parameter
        :param:
            - touch_no: which touch pad to be tested
            - dac:      pull up & down current level
            - tie_opt:  pulse initial voltage level
        '''
        self.chip.touch.touch_init(touch_no,dac=dac)
        self.chip.HWREG.SARADC.SAR_TOUCH_CTRL2.reg_touch_start_fsm_en = 0
        self.chip.HWREG.RTC_IO.TOUCH_CFG.reg_touch_xpd_bias           = 1
        setattr(getattr(self.chip.HWREG.RTC_IO,'TOUCH_PAD%s'%touch_no),'reg_touch_pad%s_tie_opt'%touch_no,tie_opt)
        setattr(getattr(self.chip.HWREG.RTC_IO,'TOUCH_PAD%s'%touch_no),'reg_touch_pad%s_rue'%touch_no,0)
        setattr(getattr(self.chip.HWREG.RTC_IO,'TOUCH_PAD%s'%touch_no),'reg_touch_pad%s_rde'%touch_no,0)
        setattr(getattr(self.chip.HWREG.RTC_IO,'TOUCH_PAD%s'%touch_no),'reg_touch_pad%s_xpd'%touch_no,1)

    def touch_anaTest_start(self,touch_no,start =1):
        '''
        :brief:
            Used to start or stop pad touch sensor function, constant pulsing
        '''
        setattr(getattr(self.chip.HWREG.RTC_IO,'TOUCH_PAD%s'%touch_no),'reg_touch_pad%s_start'%touch_no,start)


    #Need Scope test Voltage and digital multimeter testCurrnet
    def scan_touch(self, drefh_ls=range(4), drefl_ls=range(4),drange_ls=range(4),touch_no_ls = [0,1], opt_ls = [0,1], dac_ls = range(8)):
        for drefh in drefh_ls:
            for drefl in drefl_ls:
                for drange in drange_ls:                    
                    self.chip.touch.touch_global_init(drefh,drefl,drange)
                    for t_no in touch_no_ls:
                        for tie_opt in opt_ls:
                            for dac in dac_ls:
                                print "drefh,drefl,drange,t_no, tie_opt, dac"
                                print drefh,drefl,drange,t_no, tie_opt, dac
                                raw_input('Config Scope to "Signal Trig Acquire Mode"')
                                self.touch_anaTest_init(t_no, dac, tie_opt)
                                self.touch_anaTest_start(t_no, 1)
                                raw_input('makesure waveform saved!')
                                self.touch_anaTest_start(t_no, 0)
    