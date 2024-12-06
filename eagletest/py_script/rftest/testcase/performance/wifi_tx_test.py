######################################################################
## Pyphon Package
import time
import os
import math
import csv
import random
import time
import csv
import re
import serial
import numpy as np
import matplotlib.pyplot as plt

## User Custom Library
import baselib.test_channel.channel as     chn
import rftest.rflib.wifi_instrum    as     wifi_instrum
import rftest.rflib.utility.iofunc  as     iofunc
from   hal.common                   import MEM
from   hal.hwregister.hwi2c.all     import *
from   baselib.instrument           import *
from   baselib.instrument           import tester
from   rftest.rflib.rfpll           import rfpll
from   hal.wifi_api                 import WIFIAPI
from   rftest.rflib                 import rfglobal
from   rftest.rflib.wifi_lib        import WIFILIB
from   rftest.rflib.rfpll           import rfpll
from   rftest.rflib.csv_report      import csvreport
from   rftest.rflib.pbus            import pbus

#import wifilib.wifi as wifi
#import wifilib.mem as mem
#from loglib.log_lib import *
#from baselib.instrument import *
#from baselib.test_channel import *
#from rf_debug import *
#from rf_debug.utility import iofunc
#import testcase.tc008_rf_debug as rf_debug
#import testcase.tc002_agc_test as agc_test


class WIFI_TX_TEST(object):
    def __init__(self,comport,chipv='ESP32'):
        self.comport = comport
        self.chipv = chipv
        self.mem = MEM(self.comport,self.chipv)
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.wifiapi = WIFIAPI(self.comport,self.chipv)
        self.rfpll = rfpll(self.comport,self.chipv)
        self.i2c = HWI2C(self.comport,self.chipv)
        self.pbus = pbus(self.comport,self.chipv)

    ######################################################################
    def bssbw_wififormat_chansel_check (self,bss_bw,wifi_format,chan_sel):
        bssbw_list=[5,10,20,40]
        result1=True
        result2=True

        if (bss_bw == 5) | (bss_bw == 10):
            wififormat_list=['nht']
        elif (bss_bw == 20):
            wififormat_list=['ht','nht']
        elif (bss_bw == 40):
            wififormat_list=['ht','nht','dup']
        else:
            print("Error: bss_bw argument error! Only following values available:\n%s"%bssbw_list)
            result1=False
            result2=False

        if result1 != False:
            if wifi_format == 'all':
                result1=wififormat_list
            elif wifi_format in wififormat_list:
                result1=[wifi_format]
            else:
                print("Error: wifi_format argument error! When bss_bw=%d only following values available:\n%s"%(bss_bw,wififormat_list))
                result1=False
                result2=False

            if (bss_bw == 40):
                if (wifi_format=='ht'):
                    chansel_list=['up','down','cen','all']
                    chansel_num_list=[1,2,3]
                elif(wifi_format=='nht'):
                    chansel_list=['up','down','cen','all']
                    chansel_num_list=[2,3]
                else:
                    chansel_list=['cen','all']
                    chansel_num_list=[1]
            else:
                chansel_list=['cen','all']
                chansel_num_list=[0]

        if result2 != False:
            if chan_sel == 'all':
                result2=chansel_num_list
            elif chan_sel in chansel_list:
                if (bss_bw == 40):
                    if (wifi_format == 'ht'):
                        if chan_sel == 'up':
                            result2=[3]
                        elif chan_sel == 'down':
                            result2=[2]
                        else:
                            result2=[1]
                    elif (wifi_format == 'nht'):
                        if chan_sel == 'up':
                            result2=[3]
                        else:
                            result2=[2]
                    else:
                        result2=[1]
                else:
                    result2=[0]
            else:
                result2=False
                print("Error: chan_sel argument error! When bss_bw=%s, wifi_format=%s, only following values available:\n%s"%(bss_bw,wifi_format,chansel_list))

        return result1, result2

    ######################################################################
    def iqvchan_check (self,iqv_chan):
        iqvchan_list=[1,2]

        if iqv_chan in iqvchan_list:
            result=True
        else:
            result=False
            print("Error: iqv_chan argument error, only following values available: %s"%iqvchan_list)

        return result

    ######################################################################
    def rfchan_check (self,channel,bss_bw):
        if bss_bw == 40:
            chan_list = range(3,13)
        else:
            chan_list = range(1,15)

        result = True
        for chan in channel:
            if chan not in chan_list:
                print("Error: channel argument error! When bss_bw=%d only following values available:\n%s"%(bss_bw,chan_list))
                result = False
                break

        return result

    ######################################################################
    def datalen_check (self,data_len,wifi_format):
        maxlen_dic={
        'ht'  : 2**16-1,
        'nht' : 2**12-1,
        'dup' : 2**12-1}

        minlen=5
        if len(wifi_format) > 1:
            maxlen=2**12-1
        else:
            maxlen=maxlen_dic[wifi_format[0]]

        if len(data_len) == 1:
        	if (data_len[0] < minlen) | (data_len[0] > maxlen):
        	    result=False
        	    print("Error: data_len should be in range [%d,%d]"%(minlen,maxlen))
        	else:
        	    result=data_len
        elif len(data_len) == 2:
        	if data_len[0] > data_len[1]:
        	    result=False
        	    print("Error: data_len[0] should be less than or equal to data_len[1]")
           	elif (data_len[0] < minlen) | (data_len[1] > maxlen):
        	    result=False
        	    print("Error: data_len should be in range [%d,%d]"%(minlen,maxlen))
        	elif data_len[0] == data_len[1]:
        	    result=data_len
        	else:
        	    result=range(data_len[0],data_len[1]+1)
        elif len(data_len) == 3:
        	if data_len[0] > data_len[1]:
        	    result=False
        	    print("Error: data_len[0] should be less than or equal to data_len[1]")
           	elif (data_len[0] < minlen) | (data_len[1] > maxlen):
        	    result=False
        	    print("Error: data_len should be in range [%d,%d]"%(minlen,maxlen))
        	elif data_len[2] > (data_len[1]-data_len[0]+1):
        	    result=False
        	    print("Error: data_len[2] should be less than or equal to data_len[1]-data_len[0]+1")
        	elif data_len[2] == (data_len[1]-data_len[0]+1):
        	    result=range(data_len[0],data_len[1]+1)
        	else:
        	    result=sorted(random.sample(range(data_len[0],data_len[1]+1),data_len[2]))
        elif len(data_len) >= 4:
        	data_len=sorted(data_len)
           	if (data_len[0] < minlen) | (data_len[-1] > maxlen):
        	    result=False
        	    print("Error: data_len should be in range [%d,%d]"%(minlen,maxlen))
        	else:
        	    result=data_len

        return result

    ######################################################################
    def bssbw_wififormat_rate_check (self,bss_bw,wifi_format,rate):
        if (bss_bw in [20,40]) & (wifi_format == 'all') & (rate != ['all']):
            result=False
            rate_list=['all']
            print("Error: rate_sym argument error! When wifi_format=%s, only following values available: 'all'"%wifi_format)
        else:
            result=True

        return result

    ######################################################################
    def cbw_check(self,cbw_ls,bss_bw,wifi_format,chan_sel):
        if bss_bw == 40:
            if wifi_format == 'ht':
                if (chan_sel == 'up') | (chan_sel == 'down'):
                    cbw_list=[0]
                else:
                    cbw_list=[0,1]
            elif wifi_format == 'dup':
                cbw_list=[1]
            else:
                cbw_list=[0]
        else:
            cbw_list=[0]
        for i in cbw_ls:
            if i in cbw_list:
                result = True
            else:
                result = False
                print("Error: cbw argument error! When bss_bw=%d, wifi_format=%s, chan_sel=%s, only following values available:\n%s"%(bss_bw,wifi_format,chan_sel,cbw_list))

        return result

    ######################################################################
    def shortgi_check(self,wifi_format,short_gi):
        if (wifi_format != 'ht') & (short_gi):
            result = False
            print("Error: short_gi argument error! When wifi_format=%s, only following values available: 0"%wifi_format)
        else:
            result = True

        return result

    ######################################################################
    def rate_gen (self,rate,bss_bw,wifi_format,cbw):
        if bss_bw in [20,40]:
            if (wifi_format == 'ht'):
                if (cbw == 1):
                    rate_list=['mcs0','mcs1','mcs2','mcs3','mcs4','mcs5','mcs6','mcs7','mcs32']
                else:
                    rate_list=['mcs0','mcs1','mcs2','mcs3','mcs4','mcs5','mcs6','mcs7']
            else:
                if (wifi_format == 'dup'):
                    rate_list=['6m','9m','12m','18m','24m','36m','48m','54m']
                else:
                    rate_list=['lr_0_0.125m','lr_1_0.25m','lr_2_0.5m','lr_3_0.25m','lr_4_0.5m','lr_5_1m','lr_6_0.25m','lr_7_0.5m','1m','2ml','2ms','5.5ml','5.5ms','11ml','11ms','6m','9m','12m','18m','24m','36m','48m','54m']
        elif bss_bw == 10:
            rate_list=['3m_10','4.5m_10','6m_10','9m_10','12m_10','18m_10','24m_10','27m_10']
        else:
            rate_list=['1.5m_5','2.25m_5','3m_5','4.5m_5','6m_5','9m_5','12m_5','13.5m_5']

        if (len(rate) == 1) & (rate == ['all']):
            result = rate_list;
        else:
            result=[]
            for rate_var in rate:
                if rate_var in rate_list:
                    result.append(rate_var)
                else:
                    result = False
                    print("Error: rate_sym argument error! When bss_bw=%d and wifi_format=%s, only following values available:\n%s"%(bss_bw,wifi_format,rate_list))
                    break

        return result

    ######################################################################
    def chansel_num_gen (self,bss_bw,wifi_format,cbw,chan_sel):
        if (chan_sel == 'all'):
            if (wifi_format == 'ht'):
                if bss_bw == 40:
                    if cbw == 1:
                        result = [2]
                    else:
                        result = [1,2,3]
                else:
                    result = [0]
            elif (wifi_format == 'dup'):
                result = [2]
            elif (wifi_format == 'nht'):
                if (bss_bw == 40):
                    result = [1,2,3]
                else:
                    result = [0]
            else:
                result = [1]
        elif (chan_sel == 'cen'):
            if bss_bw == 40:
                if cbw == 1:
                    result = [2]
                else:
                    result = [1]
            else:
                result = [0]
        elif (chan_sel == 'up'):
            result = [3]
        else:
            result = [2]

        return result

    ######################################################################
    def get_chan_freq(self,chan=1,wifi_format='ht',chansel_num=1,cbw=0):
        if chan==14:
            freq = 2484
        else:
            freq = 2412 + 5*(chan-1)
        if (chansel_num == 0) | (chansel_num == 1):
            result = freq
        elif (chansel_num == 2) | (chansel_num == 3):
            if cbw == 1:
                if wifi_format == 'dup':
                    result = freq-10
                else:
                    result = freq
            else:
                result = freq+(chansel_num-2.5)*20
        else:
            result = freq

        return result

    ######################################################################
    def SampleTime_Gen(self,bss_bw,cbw,wifi_format,rate,short_gi,data_len):
        rate_ht40_dic={ 'mcs0'        : 13.5,
                        'mcs1'        : 27,
                        'mcs2'        : 40.5,
                        'mcs3'        : 54,
                        'mcs4'        : 81,
                        'mcs5'        : 108,
                        'mcs6'        : 121.5,
                        'mcs7'        : 135,
                        'mcs32'       : 6}
        rate_ht20_dic={ 'mcs0'        : 6.5,
                        'mcs1'        : 13,
                        'mcs2'        : 19.5,
                        'mcs3'        : 26,
                        'mcs4'        : 39,
                        'mcs5'        : 52,
                        'mcs6'        : 58.5,
                        'mcs7'        : 65}
        rate_nht20_dic={
                        'lr_0_0.125m' : 0.125,
                        'lr_1_0.25m'  : 0.25,
                        'lr_2_0.5m'   : 0.5,
                        'lr_3_0.25m'  : 0.25,
                        'lr_4_0.5m'   : 0.5,
                        'lr_5_1m'     : 1,
                        'lr_6_0.25m'  : 0.25,
                        'lr_7_0.5m'   : 0.5,
                        '1m'          : 1,
                        '2m'          : 2,
                        '2ms'         : 2,
                        '2ml'         : 2,
                        '5.5m'        : 5.5,
                        '5.5ms'       : 5.5,
                        '5.5ml'       : 5.5,
                        '11m'         : 11,
                        '11ms'        : 11,
                        '11ml'        : 11,
                        '6m'          : 6,
                        '9m'          : 9,
                        '12m'         : 12,
                        '18m'         : 18,
                        '24m'         : 24,
                        '36m'         : 36,
                        '48m'         : 48,
                        '54m'         : 54}
        rate_nht10_dic={'3m_10'       : 3,
                        '4.5m_10'     : 4.5,
                        '6m_10'       : 6,
                        '9m_10'       : 9,
                        '12m_10'      : 12,
                        '18m_10'      : 18,
                        '24m_10'      : 24,
                        '27m_10'      : 27}
        rate_nht5_dic= {'1.5m_5'      : 1.5,
                        '2.25m_5'     : 2.25,
                        '3m_5'        : 3,
                        '4.5m_5'      : 4.5,
                        '6m_5'        : 6,
                        '9m_5'        : 9,
                        '12m_5'       : 12,
                        '13.5m_5'     : 13.5}
        sym_len_dic= {40 : 4.0,
                      20 : 4.0,
                      10 : 8.0,
                      5  : 16.0}
        pream_sym_num_dic= {'ht'  : 9,
                            'nht' : 5,
                            'dup' : 5}
        if bss_bw==40:
            if wifi_format == 'ht':
                if cbw == 1:
                    rate_mbps_dic = rate_ht40_dic
                else:
                    rate_mbps_dic = rate_ht20_dic
            else:
                rate_mbps_dic = rate_nht20_dic
        elif bss_bw == 20:
            if wifi_format == 'ht':
                rate_mbps_dic = rate_ht20_dic
            else:
                rate_mbps_dic = rate_nht20_dic
        elif bss_bw == 10:
            rate_mbps_dic = rate_nht10_dic
        else:
            rate_mbps_dic = rate_nht5_dic

        if rate in ['lr_0_0.125m','lr_1_0.25m','lr_2_0.5m','lr_3_0.25m','lr_4_0.5m','lr_5_1m','lr_6_0.25m','lr_7_0.5m','1m','2ml','2ms','5.5ml','5.5ms','11ml','11ms']:
            packet_time_len = 192 + math.ceil(data_len*8.0/rate_mbps_dic[rate])
            print("Info: packet time length is %2.1fus"%packet_time_len)
            result = packet_time_len + 8 + 32
        else:
            data_sym_num = math.ceil(data_len*8.0/rate_mbps_dic[rate]/sym_len_dic[bss_bw])
            if (wifi_format == 'ht') & (short_gi == 1):
                packet_time_len = pream_sym_num_dic[wifi_format]*sym_len_dic[bss_bw] + data_sym_num*sym_len_dic[bss_bw]*0.9
            else:
                packet_time_len = (pream_sym_num_dic[wifi_format] + data_sym_num)*sym_len_dic[bss_bw]
            print("Info: data symbol number is %d, packet time length is %2.1fus"%(data_sym_num,packet_time_len))
            result = math.ceil(packet_time_len + 5*sym_len_dic[bss_bw])

        return result

    ######################################################################
    def txtest (self, logpath='wifi_tx',iqv_chan=1, iqv_num=1, cable_loss=3, channel=[3,4], bss_bw=40, cbw=[0], wifi_format='all', chan_sel='all', rate_sym=['all'], data_len=[1024,1024,1], short_gi=0, loop_num=10, backoff_qdb=0, frm_delay=1000, dis_cca=1, para_set='default', only_check=0, verbose=0):
        """
        --channel     : [1~14]
        --bss_bw      : 5, 10, 20, 40
        --wifi_format : 'ht', 'nht', 'dup', 'all'
        --chan_sel    : 'up', 'down', 'cen', 'all'
        --rate_sym    : 'mcs0'~'mcs7','mcs32','6m','9m','12m','18m','24m','36m','48m','54m'
        --iqv_chan    : 1-left port, 2-right port
        --para_set    : 'default', 'normal', 'better', 'best'
        --only_check  : only check the arguments, and run the empty frame
        --
          bss_bw    wifi_format
          5         'all': 'nht'
          10        'all': 'nht'
          20        'all': 'nht', 'ht
          40        'all': 'nht', 'ht', 'dup'
        """

        #### argument checking
        ##create log dir
        if False==os.path.exists('./log/%s'%logpath):
           try:
             os.makedirs(r'./log/%s'%logpath)
           except:
             logerror("Error: create directory %s failed!"%logpath)
             return False
        if cable_loss < 0:
            print("Error: the value of cable_loss should be nonnegative")
            return False
        (wififormat_list,chansel_num_list)=self.bssbw_wififormat_chansel_check(bss_bw,wifi_format,chan_sel)
        #print wififormat_list,chansel_num_list
        if wififormat_list == False:
            return False
        if chansel_num_list == False:
            return False
        if self.rfchan_check(channel,bss_bw) == False:
            return False
        if self.bssbw_wififormat_rate_check(bss_bw,wifi_format,rate_sym) == False:
            return False
        if self.iqvchan_check(iqv_chan) == False:
            return False

        datalen_list=self.datalen_check(data_len,wififormat_list)
        if datalen_list == False:
            return False

        #### open test report for writing
        date_stamp=time.strftime('%Y-%m%d-%H%M%S', time.localtime())
        test_report='./rftest/log/wifi_tx/wifitx_%sm_%s_%s.csv' %(bss_bw, wifi_format, date_stamp)
        print("Info: test report file is %s"%test_report)
        fid=open(test_report, 'w')
        #fid.write('channel, power(dbm), freq_error(kHz), clk_error(ppm), evm(dB), cbw(MHz), rate(Mbps), length, MCS, CRC\n')
        if only_check != 1:
            fid.write('wifi_format, cbw, ht_dup, chan_sel, rate, fe_rate, data_len, short_gi, rf_chan, freq_tx, backoff(dB), cable_loss(dB), power(dbm), evm(dB), freq_error(kHz), data_rate(Mbps), psdu_len(Bytes), psdu_crc\n')
        else:
            fid.write('wifi_format, cbw, ht_dup, chan_sel, rate, data_len, short_gi, rf_chan, freq_tx, backoff(dB), cable_loss(dB)\n')
        fid.close()

        #### set arguments for IQx instrument
        #sock.open(IQV_server)
        #logsetlevel('ERROR')
        #iqv_num = 1 # iqv_num: iqview average number
        ext_atten = cable_loss
        max_pwr = 25-ext_atten

        ## AmplitudeTracking,FullPacketChannelEst,frequencyCorr
        if para_set=='default':
            test_para_11n=['EWC','nxn',1,1,0,1,0,'auto_detect','ltf']        #default
            test_para_11ag=['sym_by_sym','raw_long','on','long_train','off']  #default
        elif para_set=='normal':
            test_para_11n=['EWC','nxn',1,1,1,1,0,'auto_detect','ltf_sig']    #normal
            test_para_11ag=['sym_by_sym','raw_long','on','long_train','on']   #normal
        elif para_set=='better':
            test_para_11n=['EWC','nxn',1,1,1,1,0,'auto_detect','full']       #better
            test_para_11ag=['sym_by_sym','2nd_ord','on','long_train','on']    #better
        elif para_set=='best':
            test_para_11n=['EWC','nxn',1,1,1,1,1,'auto_detect','full']       #best
            test_para_11ag=['sym_by_sym','raw_full','on','full_packet','on']  #best
        else:
            print("Error: para_set argument error, allowed values are default, normal, better, best")
            return False

        test_para_11b=['7_taps','off','std_tx_gac']   #default

        #get MAX power
        #chan = channel[0]
        #max_pwr = 25-ext_atten#get_iqv_max_power(chan, 'mcs7', test_para_11n, ext_atten, iqv_chan)
        #print "test max_pwr: ",max_pwr

        w_str = ''
        data = []
        time_start=time.time()

        #### start test
        for chan in channel:
            for wifi_format in wififormat_list:
        	    ## set arguments for wifi-tx couverage test
                print "wififormat_list=%s"%wififormat_list
                if self.shortgi_check(wifi_format,short_gi) == False:
                    return False

                if wifi_format=='ht':
                    ht_dup=0
                    test_para = test_para_11n
                else:
                    if bss_bw == 10:
                        test_para = test_para_11ag + ['half']
                    elif bss_bw == 5:
                        test_para = test_para_11ag + ['quar']
                    else:
                        test_para = test_para_11ag
                    if wifi_format=='dup':
                        ht_dup=1
                    else:
                        ht_dup=0

                if False == self.cbw_check(cbw,bss_bw,wifi_format,chan_sel):
                    return False
                for cbw_var in cbw:
                    chansel_num_list=self.chansel_num_gen(bss_bw,wifi_format,cbw_var,chan_sel)
                    for chansel_num in chansel_num_list:
                        rate_list=self.rate_gen(rate_sym,bss_bw,wifi_format,cbw_var)
                        if rate_list == False:
                            return False
                        for rate in rate_list:
                            freq = self.get_chan_freq(chan,wifi_format,chansel_num,cbw_var)
                            if wifi_format=='ht':
                                test_para = test_para_11n
                            else:
                                if bss_bw == 10:
                                    test_para = test_para_11ag + ['half']
                                elif bss_bw == 5:
                                    test_para = test_para_11ag + ['quar']
                                else:
                                    if rate in ['lr_0_0.125m','lr_1_0.25m','lr_2_0.5m','lr_3_0.25m','lr_4_0.5m','lr_5_1m','lr_6_0.25m','lr_7_0.5m','1m','2ml','2ms','5.5ml','5.5ms','11ml','11ms']:
                                        test_para = test_para_11b
                                    else:
                                        test_para = test_para_11ag
                            if only_check != 1:
                                print(self.wifi.cmdstop())
                                print(self.wifi.rfchsel(chan,chansel_num))
                            for data_len in datalen_list:
                                fid=open(test_report, 'a')
                                SampleTime_us = math.ceil(self.SampleTime_Gen(bss_bw,cbw_var,wifi_format,rate,short_gi,data_len))
                                if only_check != 1:
                                    print "gain: %d"%(self.mem.rd(0x60000560)&0xff)
                                    self.wifi.txtest(rate, 0, data_len, cbw_var, ht_dup, short_gi, backoff_qdb, frm_delay, dis_cca)
                                    fe_tx_rate=self.wifiapi.get_tx_rate()
                                    self.wifi.txtest(rate, 0, data_len, cbw_var, ht_dup, short_gi, backoff_qdb, frm_delay, dis_cca)
                                    #self.wifi.txtest(rate_sym=rate, PackNum=0, PackLen=data_len, cbw=cbw_var, ht_dup=ht_dup, short_gi=short_gi, backoff_qdb=backoff_qdb, frm_delay=frm_delay, dis_cca=dis_cca)
                                    u0 = time.time()
                                    myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_chan,'measure', ext_atten, 10, 1)
                                    print 'tester:%2.2f'%(time.time()-u0)
                                    for i in range(0,loop_num):
                                        u0 = time.time()
                                        wifi_instrum.iqv_avg(myiqv, iqv_num, SampleTime_us=SampleTime_us)
                                        print 'get:%2.2f'%(time.time()-u0)
                                        iqv = rfglobal.iqv
                                        print iqv
                                        evm = iqv['evm_raw']
                                        pwr = iqv['pwr']+(backoff_qdb/4)
                                        freq_err = iqv['freq_err']
                                        clk_err = iqv['clk_err']
                                        data_rate = iqv['data_rate']
                                        psdu_len = int(float(iqv['psdu_len']))
                                        if int(float(iqv['psdu_crc'])) == 1 :
                                            psdu_crc='passed'
                                        else:
                                            psdu_crc='failed'
                                        w_str = '%s'%wifi_format+','+'%d'%cbw_var+','+'%d'%ht_dup+','+'%d'%+chansel_num+','+'%s'%rate+','+'0x%x'%fe_tx_rate+','+'%d'%data_len+','+'%d'%short_gi+','+'%d'%chan+','+'%d'%freq+','+'%2.2f'%(backoff_qdb/4.0)+','+'%2.1f'%ext_atten+','+'%2.2f'%iqv['pwr']+','+'%2.2f'%iqv['evm_raw']+','+'%2.2f'%freq_err+','+'%s'%data_rate+','+'%d'%psdu_len+','+'%s'%psdu_crc+','+'\n'
                                        fid.write(w_str)
                                        if (verbose ==1):
                                            data.append(['rate=%s'%rate, 'channel=%d'%chan, 'power=%2.2fdBm'%pwr, 'evm=%2.2fdB'%evm, 'freq_error=%2.2fkhz'%freq_err, 'clk_error=%2.2fppm'%(clk_err), 'data_rate=%sMbps'%(data_rate), 'psdu_len=%d'%(psdu_len), 'psdu_crc=%s'%(psdu_crc)])
                                    self.wifi.cmdstop()
                                else:
                                    w_str = '%s'%wifi_format+','+'%d'%cbw_var+','+'%d'%ht_dup+','+'%d'%+chansel_num+','+'%s'%rate+','+'%d'%data_len+','+'%d'%short_gi+','+'%d'%chan+','+'%d'%freq+','+'%2.2f'%(backoff_qdb/4.0)+'\n'
                                    fid.write(w_str)
                                fid.close()

        if (only_check != 1) & (verbose == 1):
            print '\n\n-----RFTX Test Result-----\n'
            for item in data:
                print item
                print '\n\n--------------------------\n'

        time_end=time.time()
        run_time=time_end-time_start
        print "Running time is: %s seconds"%run_time

# ######################################################################
# def spur_test(chan=6,min_pwr=-96,max_pwr=-80,step=2,cable_loss=8,log_suf='_1'):
#     """
#     --chan        : rf channel number, [0~14]
#     --min_pwr     : maximum spur power, [-100~-20], 1dB
#     --max_pwr     : maximum spur power, [-100~-20], 1dB
#     --step        : step of spur power, [-100~-20], 1dB
#     """
#
#     if max_pwr < min_pwr:
# 	print('Error: max_pwr must be greater or equal to min_pwr\n')
# 	return False
#
#     path='d:/chip/.running'
#     index=1
#     for pwr in range(min_pwr-step*(1-index),max_pwr+step,step):
# 	file_exist = os.path.exists(path)
# 	if index == 0:
# 	    suf_0='_bssbw40_nht20-11b_nospur%s'%log_suf
# 	    suf_1='_bssbw40_nht20-11g_nospur%s'%log_suf
# 	    suf_2='_bssbw40_ht20_nospur%s'%log_suf
# 	    suf_3='_bssbw40_ht40_nospur%s'%log_suf
# 	else:
# 	    suf_0='_bssbw40_nht20-11b_spur%ddbm%s'%(pwr,log_suf)
# 	    suf_1='_bssbw40_nht20-11g_spur%ddbm%s'%(pwr,log_suf)
# 	    suf_2='_bssbw40_ht20_spur%ddbm%s'%(pwr,log_suf)
# 	    suf_3='_bssbw40_ht40_spur%ddbm%s'%(pwr,log_suf)
# 	while True:
# 	    if file_exist == True:
# 		date_stamp=time.strftime('%Y-%m%d-%H%M%S', time.localtime())
# 		print('log_suf= %s, time= %s\n'%(suf_0,date_stamp))
# 		print('log_suf= %s, time= %s\n'%(suf_1,date_stamp))
# 		print('log_suf= %s, time= %s\n'%(suf_2,date_stamp))
# 		print('log_suf= %s, time= %s\n'%(suf_3,date_stamp))
# 		time.sleep(1)
#                 rf_debug.rxagcscan_test(log_type=2,logpath='wifi_rx',log_suf=suf_0,instru='iqv',unit_no=0,rx_chan=chan,sub_chan_cfg=1,tx_chan=chan,minpwr=-100,maxpwr=-50,packnum=100,cable_lose=cable_loss,board_id='fpga',rxgain_force_en=0,rxgain_force=20,set_chan=1,c_set_chan_en=1,freq_offset=0,rx_ratelst=['1m','2ml','5.5ml','11ml'])
# 		rf_debug.rxagcscan_test(log_type=2,logpath='wifi_rx',log_suf=suf_1,instru='iqv',unit_no=0,rx_chan=chan,sub_chan_cfg=1,tx_chan=chan,minpwr=-95,maxpwr=-45,packnum=100,cable_lose=cable_loss,board_id='fpga',rxgain_force_en=0,rxgain_force=20,set_chan=1,c_set_chan_en=1,freq_offset=0,rx_ratelst=['6m','9m','12m','18m','24m','36m','48m','54m'])
# 		rf_debug.rxagcscan_test(log_type=2,logpath='wifi_rx',log_suf=suf_2,instru='iqv',unit_no=0,rx_chan=chan,sub_chan_cfg=1,tx_chan=chan,minpwr=-95,maxpwr=-45,packnum=100,cable_lose=cable_loss,board_id='fpga',rxgain_force_en=0,rxgain_force=20,set_chan=1,c_set_chan_en=1,freq_offset=0,rx_ratelst=['mcs0','mcs1','mcs2','mcs3','mcs4','mcs5','mcs6','mcs7'])
# 		rf_debug.rxagcscan_test(log_type=2,logpath='wifi_rx',log_suf=suf_3,instru='iqv',unit_no=0,rx_chan=chan,sub_chan_cfg=3,tx_chan=chan,minpwr=-90,maxpwr=-40,packnum=100,cable_lose=cable_loss,board_id='fpga',rxgain_force_en=0,rxgain_force=20,set_chan=1,c_set_chan_en=1,freq_offset=0,rx_ratelst=['mcs0_40','mcs1_40','mcs2_40','mcs3_40','mcs4_40','mcs5_40','mcs6_40','mcs7_40'])
# 		os.rmdir(path)
# 		break
# 	    else:
# 		time.sleep(1)
# 		file_exist = os.path.exists(path)
# 	index+=1
#
######################################################################
#def timesync_test(chan=6,min_pwr=-96,max_pwr=-80,step=2,cable_loss=8,log_suf='_1'):
#    """
#    --chan        : rf channel number, [0~14]
#    --min_pwr     : maximum spur power, [-100~-20], 1dB
#    --max_pwr     : maximum spur power, [-100~-20], 1dB
#    --step        : step of spur power, [-100~-20], 1dB
#    """
















