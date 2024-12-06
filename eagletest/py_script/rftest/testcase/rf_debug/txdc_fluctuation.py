import time
import re
import csv
import os, sys
import matplotlib.pyplot as plt
import pylab
import numpy as np
from baselib.instrument import dm,tester
from baselib.instrument.spa import HP,Agilent
from rftest.rflib.wifi_lib import WIFILIB
from hal.wifi_api import WIFIAPI
from hal.Init import HALS
from hal.common import MEM
from rftest.rflib.pbus import pbus
import rftest.rflib.rfglobal as rfglobal
from rftest.rflib.rfpll import rfpll
from rftest.rflib.rfcal import rfcal
import rftest.rflib.wifi_instrum as wifi_instrum
from baselib.loglib.log_lib import *
from rftest.rflib.saradc import SARADC
from rftest.rflib.csv_report import csvreport

##rftx_lst = [0x3f]
rftx_lst = [0x1f, 0x2f,0x3f,0x4f,0x5f,0x6f,0x7f]
           #-9.75,-6.25,-3.75,-1.75,0,1.5,2.75
##rftx_lst = [0x0, 0x1,0x2,0x3,0x4,0x8,0xc,0x10,0x20,0x30,0x40,0x50,0x60,0x70]

##bbgain_lst = [0x0,0x40,0x80,0xc0,0x100,0x140,0x20,0x60,0xa0,0xe0,0x120,0x160,0x30,0x70,0xb0,0xf0,0x130,0x170,0x38,0x78,0xb8,0xf8,0x138,0x178]
##             #[0db, 1db, 2db, 3db, 4db, 5db , 6dB ,7dB, 8dB, 9db, 10db, 11db, 12db,13db,14db,15db,16db, 17dB,18dB,19db,20dB,21dB,22dB,23dB]

##bbgain_lst = [0x0,0x40,0x80,0xc0,0x100,0x140,0x20,0x60,0xa0,0xe0,0x120,0x160,0x30,0x70,0xb0,0xf0,0x130]
##             #[0db, 1db, 2db, 3db, 4db, 5db , 6dB ,7dB, 8dB, 9db, 10db, 11db,12db,13db,14db,15db,16db]
bbgain_lst = [0xa0]
             #[8db]


class TXDC_fluctuation(object):

    def __init__(self,comport,chipv='ESP32'):

        self.comport = comport
        self.chipv = chipv
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.pbus = pbus(self.comport, self.chipv)
        self.mem = MEM(self.comport, self.chipv)
        self.rfcal = rfcal(self.comport, self.chipv)
        self.rfpll = rfpll(self.comport, self.chipv)
        self.hals = HALS(self.comport,self.chipv)
        self.saradc = SARADC(self.comport,self.chipv)
        self.wifiapi = WIFIAPI(self.comport,self.chipv)

    def txdc_fluctation_gain_sweep(self,cfreq=2440,PA_gain_list=[0x7f,0x5f,0x3f,0x1f],filter_gain_list=[0x40,0x10,0xc0,0x20,0xa0,0xe0,0x120,0x30,0x130],board_no="chip722A",device_spa="N9020A"):

        title = 'freq,TX RF gain,TX filter gian,max_pwr,min_pwr,TXDC fluctation\n'
        fname = self.wifi.get_filename('TXDC_fluctuation', 'txdc_fluctation_gain_sweep_%s'%(board_no))
        csvreport1 = csvreport(fname, title)

        if device_spa =="":
            self.spa = HP('SA',cfreq);
        else:
            self.spa = Agilent('SA',cfreq,device=device_spa);
        self.spa.set_param(cfreq,span=10,rb=30,vb=30)
        self.spa.trace_detector(1,"NORM")
        self.rfpll.set_freq(cfreq)
        self.pbus.pbus_debugmode()
        self.pbus.open_tx(0x5f,0x120)
        self.rfcal.tos()
        self.mem.wrm(0x600060a0, 17, 16, 3)#tx clock force
        for filter_gain in filter_gain_list:
            for pa_gain in PA_gain_list:
                self.pbus.open_tx(pa_gain,filter_gain)
                self.rfcal.tos()
                self.spa.trace_detector(1,"NORM")
                self.spa.trace_maxhold(1)
                time.sleep(50)
                txdc_freq_max,txdc_power_max=self.spa.pk_detect()
                self.spa.trace_detector(1,"NORM")
                self.spa.trace_minhold(1)
                time.sleep(50)
                txdc_freq_min,txdc_power_min=self.spa.pk_detect()
                txdc_power_delta=txdc_power_max-txdc_power_min
                csvreport1.write_data([cfreq,hex(pa_gain),hex(filter_gain),txdc_power_max,txdc_power_min,txdc_power_delta])


    def TX_noise_3200MHz(self,cfreq,rf_gain_list=[0x1f,0x3f,0x5f,0x7f],filter_gian_list=[0x40,0x100,0x20,0x120,0x130,0x138],board_no="chip722A",device_spa="N9020A"):

        title = 'freq,ir_dac_ext,TX RF gain,TX filter gian,TX digital gain ,800MHz noise(dBm),1600MHz noise(dBm),3200MHz noise(dBm),TX tone power(dB)\n'
        fname = self.wifi.get_filename('TX_noise_3200MHz', 'TX_noise_3200MHz_gain_sweep_%s'%(board_no))
        csvreport1 = csvreport(fname, title)

        if device_spa =="":
            self.spa = HP('SA',cfreq);
        else:
            self.spa = Agilent('SA',cfreq,device=device_spa);

        self.spa.set_param(cfreq,span=1,rb=10,vb=30)
        self.rfpll.set_freq(cfreq)
        self.pbus.pbus_debugmode()
        self.hals.HWI2C.rfpll.ir_enx_dac=1
        for i in range(0,16):
            self.hals.HWI2C.rfpll.ir_dac_ext=i
            self.rfpll.restart_cal()
            for rf_gain in rf_gain_list:
                for filter_gain in filter_gian_list:
                    self.pbus.open_tx(rf_gain,filter_gain)
                    self.rfcal.tos()
                    self.mem.wrm(0x600060a0, 17, 16, 3)#tx clock force
                    for digital_gain in range(0,120,20):
                        self.wifi.txtone(1,0,digital_gain)
                        self.spa.set_cfreq(cfreq)
                        self.spa.set_reflvl(30)
                        freq_noise0,power_noise0=self.spa.pk_detect()
                        self.spa.set_param(cfreq/3,span=1,rb=10,vb=30)
                        self.spa.set_reflvl(0)
                        freq_noise1,power_noise1=self.spa.pk_detect()
                        self.spa.set_cfreq(2*cfreq/3)
                        freq_noise2,power_noise2=self.spa.pk_detect()
                        self.spa.set_cfreq(4*cfreq/3)
                        freq_noise3,power_noise3=self.spa.pk_detect()
                        self.wifi.stoptone()
                        csvreport1.write_data([cfreq,i,hex(rf_gain),hex(filter_gain),digital_gain,power_noise1,power_noise2,power_noise3,power_noise0])


