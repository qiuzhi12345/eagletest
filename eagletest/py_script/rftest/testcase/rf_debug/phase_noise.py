import baselib.test_channel.channel as chn
import baselib.test_channel.com as com
from baselib.instrument.tester_serv import *
from baselib.loglib.log_lib import *
import time
import csv
from baselib.plot import *
from baselib.instrument import *
from baselib.instrument import tester
import numpy as np
import pylab
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import re
import serial
from rftest.rflib.rfpll import rfpll
from hal.wifi_api import WIFIAPI
from rftest.rflib import rfglobal
import rftest.rflib.wifi_instrum as wifi_instrum
from rftest.rflib.wifi_lib import WIFILIB
from hal.common import MEM
from rftest.rflib.rfpll import rfpll
import rftest.rflib.utility.iofunc as iofunc
from rftest.rflib.csv_report import csvreport
from hal.hwregister.hwi2c.all import *
from rftest.rflib.pbus import pbus
from rftest.testcase.rf_debug.basic_test import BasicTest
from baselib.instrument.spa import HP,Agilent,phnoise
from baselib.instrument import dm
from hal.rtc_debug import RTC_DEBUG
from hal.adc import RTC_ADC2


rate_bps_dict = rfglobal.rate_bps_dict
sens_dict = rfglobal.sens_dict
rate_dict = rfglobal.ratedic
maxleve_dict = rfglobal.rx_maxlevel_dict


class PHASE_NOISE(object):

    def __init__(self,comport,chipv='ESP32', name_str=''):
        self.comport = comport
        self.chipv = chipv
        self.mem = MEM(self.comport,self.chipv)
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.wifiapi = WIFIAPI(self.comport,self.chipv)
        self.rfpll = rfpll(self.comport,self.chipv)
        self.i2c = HWI2C(self.comport,self.chipv)
        self.pbus = pbus(self.comport,self.chipv)
        self.rtc_debug = RTC_DEBUG(self.comport,self.chipv)
        self.rtc_adc2 = RTC_ADC2(self.comport,self.chipv)
        self.name_str=name_str
        self.curr_data_path='D:/chip/eagletest/py_script/rftest/rfdata/'

    def tester_init(self):
        self.tester=phnoise(mode=14,timeout=10,device="N9020A")

    def get_phase_noise_data(self,freq=0):
        self.tester_init()
        if freq!=0:
            self.tester.carrier_freq_set(freq=freq)
        #self.tester.restart()
        res=self.tester.get_result(trace=1)
        res_list=str(res).split(',')
        freq_offset_list=[]
        lplot=[]
        for i in range(len(res_list)/2):
            freq_offset_list.append(res_list[i*2])
            lplot.append(res_list[1+i*2])
        return [freq_offset_list,lplot]

    def data_ant(self,freq=2412,savecsv_en=1,plot_en=1,name_str=''):

        [freq_offset_list,lplot]=self.get_phase_noise_data(freq=freq)

        if savecsv_en!=0:
            filetime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()));
            title = 'freq_offset, lplot\n'
            fname = self.wifi.get_filename('phase_noise_test', 'phase_noise_test_%s'%name_str)
            csvreport1 = csvreport(fname, title)

            for i in range(len(freq_offset_list)):
                csvreport1.write_data([freq_offset_list[i],lplot[i]],float_num=6)

        freq_offset_list=map(eval,freq_offset_list)
        lplot=map(eval,lplot)
        if plot_en!=0:
            pylab.ion()
            pylab.figure(100)
            pylab.plot(freq_offset_list,lplot,linewidth=0.5,label='%s'%name_str)
            pylab.title("phase noise")
            pylab.xlabel('freq_offset(Hz)')
            pylab.ylabel('lplot(dBc)')
            pylab.xscale('log',nonposx='mask',subsx=[2,3,4,5,6,7,8,9])
            pylab.legend()
            pylab.grid(b=True,which='both',axis='both')
            ax=pylab.gca()
            ax.yaxis.set_major_locator(MultipleLocator(5))
            pylab.savefig(self.curr_data_path+"phase_noise_%s"%name_str)
            pylab.show()


    def phase_noise_test(self, chan=1,savecsv_en=1,plot_en=1,name_str=''):
        """

        """

##        self.wifiapi.pll_cap_track_en(0)
        self.wifi.cmdstop()
        self.wifi.rfchsel(chan,0)
        self.wifi.force_txon(1)
        self.wifi.txtone(1,0,60)
        freq=self.wifi.chan2freq(chan)
        self.data_ant(freq=freq,savecsv_en=savecsv_en,plot_en=plot_en,name_str=name_str)

        self.wifi.stoptone()
        self.wifi.force_txon(0)

