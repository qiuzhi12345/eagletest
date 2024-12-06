from rftest.rflib.wifi_lib import WIFILIB
from rftest.rflib import *
import baselib.test_channel.channel as chn
from baselib.loglib.log_lib import *
from baselib.instrument import *
from math import *
import time
from baselib.test_channel import *
from baselib.instrument.tester_serv import *
from baselib.instrument import tester
from rftest.rflib.csv_report import csvreport
import sys
from baselib.instrument import *
import csv
import xlwt
import xlrd
import os
from rftest.testcase.performance.wifi_txrx_test import WIFI_TXRX_TEST
from rftest.rflib import rfglobal

sens_dict = rfglobal.sens_dict
rx_maxlevel_dict =rfglobal.rx_maxlevel_dict

data_rate_vs_iq_mode_dic={
    '11b':['1m','2m','5.5m','11m'],
    '11a':['1m','11m','6m','54m','mcs0','mcs7','mcs0_40','mcs7_40'],

    '11g':['18m','24m','36m','48m','54m'],
    '11n_20':['mcs7','mcs6','mcs5','mcs4','mcs3','mcs2','mcs1','mcs0'],
    '11n_40':['mcs0_40','mcs1_40','mcs2_40','mcs3_40','mcs4_40','mcs5_40','mcs6_40','mcs7_40'],
##    '11n':['mcs4_40','mcs5_40','mcs6_40','mcs7_40']
    '11n':['mcs7']

}


class RxFreqTol(object):
    def __init__(self,comport,chipv='ESP32'):
        self.comport = comport
        self.chipv = chipv
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.wifi_txrx_test = WIFI_TXRX_TEST(self.comport,self.chipv)



    def rf_freq_tol_test(self,lost_list=[11.5],tx_chan=[14],pwr_step =2,iq_mode=['11b'],packnum=100,iqv_no=1):



        title1 ='Channel, Rate, Rx_Pwr(dBm), offset_freq(khz),DesirePackNum, gain, Rssi, Noise, err, err2, freqoff,rssi_min, rssi_max\n'
        fname1 = self.wifi.get_filename('rf_rxfreqtol_data', 'RX_Frequency_Tolerence_Test','rx_scan_result')
        file1 = csvreport(fname1, title1)

        title2 = 'chan_no,subrate,rx_pwr,cur_min_freq, cur_min_find, cur_max_freq, cur_max_find,cur_max_start\n'
        fname2 = self.wifi.get_filename('rf_rxfreqtol_data', 'RX_Frequency_Tolerence_Test_freqRange','rx_freqRange_result')
        file2 = csvreport(fname2, title2)

        time.sleep(0.5)
        offset_freq = 0
        self.wifi.cmdstop()
        cable_lose = lost_list[0]
        chan_no=tx_chan[0]

        for m in iq_mode:
            data_rate=data_rate_vs_iq_mode_dic[m]
            rate_l = len(data_rate)
            for i in range(0,rate_l):
    			subrate = data_rate[i]
##    			cbw40m = self.wifi.rate2ht40(subrate)
##    			logdebug("cbw40m=%d"%(cbw40m))
    			chan_l = len(tx_chan)
    			logdebug("subrate=%s, channel=%d"%(subrate, chan_no))
    			for j in range(0,chan_l):
        			chan_no=tx_chan[0]
    				freq=self.wifi.chan2freq(chan_no)
    				perform_list=[]

    				rate_sens = sens_dict[subrate]
    				rate_max = rx_maxlevel_dict[subrate]
    				minpwr = rate_sens
    				maxpwr = -20
##    				minpwr = rate_max-10
##    				maxpwr = rate_max
##    				minpwr = -72
##    				maxpwr = -71
    				rfpwr= minpwr
    				loginfo('minpwr=%d, maxpwr=%d'%(minpwr,maxpwr))
    				while rfpwr<=maxpwr:
    				    for offset_freq in range (-650,650,10):
    				        rate= subrate+'_offset'+'_%d'%offset_freq+'khz'
    				        loginfo("rate=%s, channel=%d"%(rate, chan_no))

##    				        cbw40m = self.wifi.rate2ht40(subrate)
    				        cbw40m = 2
    				        self.wifi.tx_cbw40m_en(cbw40m)
    				        self.wifi.rfchsel(chan_no, cbw40m)
    				        if cbw40m == 2:
    				            freq-=10
    				        elif cbw40==3:
    				            freq+=10
            ##    			self.wifi.esp_rx(chan_no, subrate)
    				        mytester=tester.tester(freq,-50,rate,1,iqv_no,'source',cable_lose,isreset=0)
    				        mytester.sigout(freq,rfpwr,cable_lose,rate,packnum,iqv_no)
    				        mytester.trig_wave(iqv_no)
    				        self.wifi.rxstart(subrate)
    				        time.sleep(0.1)

    				        result_data= self.wifi.cmdstop()



    				        [DesirePackNum, gain, Rssi, Noise, err, err2, freqoff,rssi_min, rssi_max] = self.wifi.rxresult(result_data)
    				        perform_list.append((rfpwr,offset_freq,DesirePackNum, gain,Rssi,Noise,err,err2, freqoff))

    				        mytester.gen_switch('OFF',iqv_no)
    				        file1.write_data([chan_no,subrate,rfpwr,offset_freq,DesirePackNum, gain, Rssi, Noise, err, err2, freqoff,rssi_min, rssi_max])
    				        [cur_min_freq, cur_min_find, cur_max_freq, cur_max_find, cur_max_start,perform_list] = self.get_data_sens(packnum, perform_list)
    				    file2.write_data([chan_no,subrate,rfpwr,cur_min_freq, cur_min_find, cur_max_freq, cur_max_find,cur_max_start,])
    				    rfpwr=rfpwr+pwr_step;
    				    print rfpwr
    				    mytester.set_pwr(rfpwr,0,iqv_no,'source');

    def get_data_sens(self, packnum, perform_list):
    #**************creat log***************#

        cur_min_find = 0
        cur_max_freq = 0
        cur_max_find = 0
        cur_max_start = 0
        cur_min_freq=0

        for data in perform_list:
            loginfo(data)
            if cur_min_find==0:
                if data[2]>=(packnum*0.9):
                    cur_min_freq=data[1]
                    cur_min_find=1
                else:
                    cur_min_freq=data[1]
                    cur_min_find=0

            if cur_max_find==0:
                if cur_max_start == 0:
                    if data[2]>=(packnum*0.95):
                            cur_max_start=1
                elif cur_max_start == 1:
                    if data[2]<(packnum*0.9):
                        cur_max_freq=data[1]
                        cur_max_find=1
                    else:
                        cur_max_freq=data[1]
                        cur_max_find=0
        return [ cur_min_freq,cur_min_find, cur_max_freq,cur_max_find,cur_max_start, perform_list]


