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

rate_bps_dict = rfglobal.rate_bps_dict
sens_dict = rfglobal.sens_dict
rate_dict = rfglobal.ratedic
maxleve_dict = rfglobal.rx_maxlevel_dict

class WIFI_Feature_Case(object):

    def __init__(self,comport,chipv='ESP32', name_str=''):
        self.comport = comport
        self.chipv = chipv
        self.mem = MEM(self.comport,self.chipv)
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.wifiapi = WIFIAPI(self.comport,self.chipv)
        self.rfpll = rfpll(self.comport,self.chipv)
        self.i2c = HWI2C(self.comport,self.chipv)
        self.pbus = pbus(self.comport,self.chipv)
        self.name_str=name_str
        #self.mac = self.wifi.read_mac()


    def TX_Length_Test(self, cable_lose=2, iqv_no=1,iqv_num=10):
        """
        :test TX power and EVM
        :cable_lost:
        :channle: it is matrix [1,...]
        :data_rate: it is matrix ['mcs0',...]
        :iqv_no: 1-left port, 2-right port
        :iqv_num: iqview average number
        """
        channel=[14]

##        length_m = [100, 1024, 4095, 12095]

        data_rate=['mcs7']
        length_m = [50, 55, 60, 70, 98, 99, 100, 101, 102, 200]

        title = 'channel, cbw40, short_gi, rate, Pocket_length, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage(dB),iq_imb_amp(dB),iq_imb_phase(deg), evm_list\n'
        fname = self.wifi.get_filename('WIFI_Feature_Case', 'TX_Length_Test')
        csvreport1 = csvreport(fname, title)

        self.wifiapi.pll_cap_track_en(1)

        max_pwr = 25 - cable_lose

        self.wifi.txpacket(1, '54m', 0, 0)
        test_para = wifi_instrum.test_para('54m')
        myiqv=tester.tester(2412, max_pwr, '54m', test_para, iqv_no,'measure', cable_lose, 10, 1)
        [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 1,'false')
        max_pwr = pwr + 12
        print "max_pwr=%d"%max_pwr

        for rate in data_rate:
            for chan in channel:

                rate_index=self.wifi.ratecheck(rate)
                cbw40 = self.wifi.rate2ht40(rate)
                short_gi = self.wifi.rate2shortGI(rate)
                test_para = wifi_instrum.test_para(rate)

                if chan<=14:
                    freq = self.wifi.chan2freq(chan)
                    self.wifi.rfchsel(chan, cbw40*2)
                else:
                    freq = chan
                    self.wifi.rfchsel(14, cbw40*2)
                    self.rfpll.set_freq(freq)

##                self.i2c.rfpll.ir_enx_cap=0
##                self.i2c.rfpll.ir_enx_dac=0

##                for length in length_m:
                for length in range(50, 300, 5):

                    if rate_index < 16 and length > 4095:
                        break

                    [len_byte, delay_us] = self.wifi.get_length_delay_duty(rate, duty=0.3, length=length)
                    if delay_us > 100000:
                        delay_us = 100000
                    loginfo("rate=%s, channel=%d, length=%d, delay_us=%d"%(rate, chan, len_byte, delay_us))

##                    self.mem.wrm(0x6000e040, 6, 6, 0)  #pll cal start
##                    self.mem.wrm(0x6000e040, 6, 6, 1)  #pll cal start
                    self.wifi.txout(rate, PackNum=0, PackLen=len_byte, cbw40=cbw40, frm_delay=delay_us)

                    myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0, 1)
                    [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false')

##                    self.wifi.cmdstop()

                    csvreport1.write_data([chan,cbw40,short_gi,rate,len_byte,pwr,evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase, evm_list])
                    print [chan,rate,pwr,evm,evm_std,evm_max,freq_err,clk_err,lo_leakage,iq_imb_amp,iq_imb_phase, evm_list]


    def esp8266_freq_offset_test(self, cable_lose=2, iqv_no=1, name_str=''):

        channel=14
        data_rate='mcs7'
        iqv_num = 2

        title = 'byte112, byte113, chan_offset, freq_offset, freq_error(kHz), meas_error, channel, rate, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage(dB),iq_imb_amp(dB),iq_imb_phase(deg)\n'
        fname = self.wifi.get_filename('freq_offset_test_%s'%name_str, 'freq_offset_test')
        csvreport1 = csvreport(fname, title)

        max_pwr = 25 - cable_lose

        self.wifiapi.wifi_init_8266(0, 0)
        self.wifi.txpacket(1, data_rate, 0, 0, duty=0.1)
        test_para = wifi_instrum.test_para(data_rate)
        myiqv=tester.tester(2412, max_pwr, data_rate, test_para, iqv_no,'measure', cable_lose, 10, 1)
        [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 1,'false')
        freq_offset_init = freq_err
        max_pwr = pwr + 12

        freq_offset_set = []
        freq_offset_meas = []
        for byte112 in [0,1,3,5,7,9]:
            for byte113 in [4, -4]:
                for chan_offset in [20, -20]:

                    if byte112 == 0:
                        freq_offset = freq_offset_init
                    elif byte112 == 1:
                        freq_offset = freq_offset_init+chan_offset
                    elif byte112 == 3:
                        if chan_offset < 0:
                            freq_offset = freq_offset_init+chan_offset
                        else:
                            freq_offset = freq_offset_init
                    elif byte112 == 5:
                        freq_offset = freq_offset_init+byte113*8
                    elif byte112 == 7:
                        if byte113 < 0:
                            freq_offset = freq_offset_init+byte113*8
                        else:
                            freq_offset = freq_offset_init
                    elif byte112 == 9:
                        freq_offset = freq_offset_init + byte113*8+chan_offset

                    self.wifiapi.wifi_init_8266(byte112, byte113)
                    self.wifiapi.rfchsel_offset(channel, chan_offset)

                    self.wifi.txpacket(channel, data_rate, 0, 0, duty=0.1)

                    test_para = wifi_instrum.test_para(data_rate)
                    freq = self.wifi.chan2freq(channel)

                    myiqv=tester.tester(freq, max_pwr, data_rate, test_para, iqv_no,'measure', cable_lose, 10, 0, 1)
                    [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false')
                    self.wifi.cmdstop()

                    csvreport1.write_data([byte112, byte113, chan_offset, freq_offset, freq_err, freq_offset-freq_err, channel,data_rate,pwr,evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase])
                    print [byte112, byte113, chan_offset, channel,data_rate,pwr,evm,evm_std,evm_max,freq_err]

                    freq_offset_set.append(freq_offset)
                    freq_offset_meas.append(freq_err)

    def fcc_limit_test(self,cable_lose=2, iqv_no=1, iqv_num=2, name_str=''):
        title = 'chan, rate, backoff, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage(dB),iq_imb_amp(dB),iq_imb_phase(deg)\n'
        fname = self.wifi.get_filename('fcc_limit_test_%s'%name_str, 'fcc_limit_test')
        csvreport1 = csvreport(fname, title)
        logsetlevel('I')
        chan_m = range(1,14,5)
        rate_m = rfglobal.test_rate_comm

        for rate in rate_m:
            rate_index=self.wifi.ratecheck(rate)
            cbw40 = self.wifi.rate2ht40(rate)

            for chan in chan_m:
                if cbw40==1 and (chan < 3 or chan > 11):
                    continue

                test_para = wifi_instrum.test_para(rate)
                freq = self.wifi.chan2freq(chan)
                self.wifi.txout(rate, 0, 500, cbw40=cbw40, frm_delay=2000)
                myiqv=tester.tester(freq, 25, rate, test_para, iqv_no,'measure', cable_lose, 10, 0, 1)

                for backoff in range(0,11,2):
                    self.wifi.fcc_limit_set(chan=chan, cbw40=cbw40, rate_index=rate_index, backoff_db=backoff)
                    self.wifi.rfchsel(chan, cbw40*2)
                    self.wifi.txout(rate, 0, 500, cbw40=cbw40, frm_delay=2000)

                    [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false')
                    self.wifi.cmdstop()

                    csvreport1.write_data([chan, rate, backoff,pwr,evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase])
                    loginfo([chan, rate, backoff,pwr,evm])


    def wifi_tx_rate_test(self, cable_lose=2,iqv_no=1,iqv_num=10, name_str=""):
        """
        :test TX power and EVM
        :cable_lost:
        :iqv_no: 1-left port, 2-right port
        :iqv_num: iqview average number
        """
        title = 'chan, chan_config, cbw40,ht_dup,freq,rate, rate_fe, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage(dB),iq_imb_amp(dB),iq_imb_phase(deg),evm_list\n'
        fname = self.wifi.get_filename('wifi_tx_rate_test_%s'%name_str, 'wifi_tx_rate_test_%s'%name_str)
        csvreport1 = csvreport(fname, title)

        logsetlevel("I")
        self.wifi.cmdstop()
        max_pwr = 25 - cable_lose

        self.wifi.txpacket(1, '54m', 0, 0, duty=0.1)
        test_para = wifi_instrum.test_para('54m')
        myiqv=tester.tester(2412, max_pwr, '54m', test_para, iqv_no,'measure', cable_lose, 10,1,1,20)
        [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 1,'false')

        self.wifi.txpwr_track_en(1,1,0)

        chan = 3
        result = []
        for rate in rate_all:
            if rate[-2:]=='40':
                break
            for chan_config in range(0,6):
                rate_index=self.wifi.ratecheck(rate)
                print [chan_config,rate_index]
                if chan_config==5:
                    if rate_index >= 16:
                        cbw40 = 1
                        ht_dup = 0
                    else:
                        break
                elif chan_config==4:
                    if rate_index >= 8 and rate_index<16:
                        cbw40 = 0
                        ht_dup = 1
                    else:
                        continue
                else:
                    cbw40 = 0
                    ht_dup = 0

                freq = self.wifi.chan2freq(chan)
                if chan_config==2:
                    freq -= 10
                elif chan_config==3 or chan_config==4:
                    freq += 10

                if chan_config > 3:
                    chan_config = 3
                self.wifiapi.rfchsel(chan,chan_config)

                self.wifi.txout(rate, 0, 500, cbw40=cbw40, ht_dup=ht_dup, backoff_qdb=0, frm_delay=1500)

                test_para = wifi_instrum.test_para(rate)
                myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0,0,20)
                [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false')
                self.wifi.cmdstop()
                rate_fe = self.wifiapi.get_tx_rate()

                csvreport1.write_data([chan,chan_config,cbw40,ht_dup,freq,rate,rate_fe,pwr,evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase, evm_list])
                loginfo([chan,chan_config,cbw40,ht_dup,freq,rate,rate_fe,pwr,evm])


