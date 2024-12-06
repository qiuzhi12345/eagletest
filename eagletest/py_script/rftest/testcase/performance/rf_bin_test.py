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
from rftest.rflib import rfglobal
import rftest.rflib.wifi_instrum as wifi_instrum
import rftest.rflib.bt_instrum as bt_instrum
from rftest.rflib.wifi_lib import WIFILIB
from rftest.rflib. saradc import SARADC
from hal.common import MEM
from rftest.rflib.rfpll import rfpll
import rftest.rflib.utility.iofunc as iofunc
from rftest.rflib.csv_report import csvreport
from hal.bt_api import *
from rftest.testcase.performance.wifi_txrx_test import WIFI_TXRX_TEST
from rftest.testcase.performance.bt_auto_test import BtAutoTest
from rftest.testcase.performance.wifi_auto_test import WiFiAutoTest
from rftest.rflib.csv_report import csvreport
from rftest.testcase.performance import data_summary
from rftest.testcase.performance.tx_ack_test import ACK_Test
from hal.wifi_api import WIFIAPI

rate_bps_dict = rfglobal.rate_bps_dict
sens_dict = rfglobal.sens_dict
rate_dict = rfglobal.ratedic
drate2name = bt_instrum.drate2name
name2drate = bt_instrum.name2drate
DH2name = bt_instrum.DH2name
name2DH = bt_instrum.name2DH
dtype2name = bt_instrum.dtype2name
name2dtype = bt_instrum.name2dtype


#-----------------------------------------------

# *********test case list*********#
# tx_contin_en
# esp_tx
# wifitxout
# esp_rx
# tx_cbw40m_en
# wifi_txtone
# bt_txtone
# RF_init_sel
# txpwr_track_en

# cmdstop-done

#*******additional functon*******#
#check mac : esp_chk_mac
#write mac : esp_set_mac
#esp_origin_mac

#esp_en_reboot
#GPIO_test

#-----------------------------------------------

class RF_Bin_Test(WIFI_TXRX_TEST,BtAutoTest):
    def __init__(self,comport,chipv='ESP32'):
        self.comport = comport
        self.chipv = chipv
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.wifiapi = WIFIAPI(self.comport,self.chipv)
        self.bt = BTAPI(self.comport,self.chipv)
        self.mem = MEM(self.comport,self.chipv)
        self.saradc = SARADC(self.comport,self.chipv)
        self.txrx = WIFI_TXRX_TEST(self.comport,self.chipv)
        self.ack_test = ACK_Test(self.comport,self.chipv)
        self.bt_test=BtAutoTest(self.comport,self.chipv)
        self.rf_bt_autotest_data = "D:/chip/eagletest/py_script/rftest/rfdata/rf_bin_test/bt_data/"
        self.folder = 'rf_bin_test'
        self.wifi_txrx_data = "D:/chip/eagletest/py_script/rftest/rfdata/rf_bin_test/wifi_data/"
        self.rf_wifi_autotest_data = "D:/chip/eagletest/py_script/rftest/rfdata/rf_bin_test/wifi_data/"
        self.txrx_data = "D:/chip/eagletest/py_script/rftest/rfdata/rf_bin_test/wifi_data/"
        self.ack_test ="D:/chip/eagletest/py_script/rftest/rfdata/rf_bin_test/wifi_data/Ack_Test_data"

    def tx_continue_en(self):

        self.wifi.tx_contin_en(0)
        self.wifi.tx_contin_en(1)

    def wifi_tx_tone(self,en=1,channel=[1,6,11],backoff=0,name_str=""):

        title ='chan,backoff,det_pwr\n'
        fname = self.wifi.get_filename(self.folder,'wifi_tx_tone_pwrdet_sar_test_%s'%name_str)
        csvreport1 =csvreport(fname, title)
        for chan in channel:
            for etten in range (backoff,40,4):
                self.wifi.wifiscwout(en=en,chan=chan,backoff=etten)
                self.saradc.en_pwdet(signal='tone')
                det_pwr = self.saradc.sar_dout(num=8, signal='tone', pwr_dis=0, offset=19)
                csvreport1.write_data([chan,etten,det_pwr])

    def bt_tx_tone(self,en=1,channel=[1,39,78],backoff=0,name_str=""):

        title ='chan,backoff,det_pwr\n'
        fname = self.wifi.get_filename(self.folder,'BT_tx_tone_pwrdet_sar_test_%s'%name_str)
        csvreport1 =csvreport(fname, title)
        for chan in channel:
            for etten in range (backoff,40,4):
                self.bt.bt_tx_tone(en=en, chan=chan,backoff=etten)
                self.saradc.en_pwdet(signal='tone')
                det_pwr = self.saradc.sar_dout(num=8, signal='tone', pwr_dis=0, offset=8)
                csvreport1.write_data([chan,etten,det_pwr])

    def txpwr_track_en(self,track_en=0,correct_en=0,print_en=0):

        self.wifi.txpwr_track_en(0,0,0)
        self.wifi.txpwr_track_en(1,0,0)

    def RF_init_sel(self, en=1,addr=0x0):

        cmdstr = "RF_init_sel %d %d"%(en,addr)
        return self.channel.req_com("RF_init_sel %d %d"%(en,addr))

    def backoff_verify(self,cable_lose=2,rate_list=['1m','11m'],channel=[1,7,13],iqv_no=2):

        title = 'rate,chan, backoff, power,evm,evm_std,evm_max,evm_list,freq_err, clk_err\n'
        fname = self.wifi.get_filename(self.folder,'Backoff_verify_test_data')
        csvreport1 = csvreport(fname,title)
        self.wifi.cmdstop()
        max_pwr = 25 - cable_lose
        backoff=0

        print "max_pwr=%f"%max_pwr

        for rate in rate_list:
            for chan in channel:
                for backoff in range(0,46,4):
                    print "rate=%s,chan=%d,backoff=%d"%(rate,chan,backoff)

                    self.wifi.txpacket(txchan=chan,rate_sym=rate, PackNum=0, cbw40=0, ht_dup=0, backoff_qdb=backoff, duty=0.1)
                    test_para = wifi_instrum.test_para(rate)
                    if chan<=14:
                        freq = self.wifi.chan2freq(chan)
                    else:
                        freq = chan

                    myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0, 1)
                    [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 10,'false')
                    [freq_mask, mask_marg] =  wifi_instrum.spectrum_mask_flatness(myiqv, 10, 99)
                    self.wifi.save_init_print()
                    print [pwr,evm]
                    csvreport1.write_data([chan,rate,backoff,pwr,evm,evm_std,evm_max,evm_list,freq_err, clk_err])

    def loop_test(self,loop_time=20):
        for loop in range (1, loop_time+1):
            self.backoff_verify(cable_lose=5.3,rate_list=['6m','54m','mcs0','mcs7'],channel=[1,6,11],iqv_no=2)

    def delays_vs_evm(self,cable_lose=12,channel=[],rate_dict=[],iqv_no=2,name_str=""):

        rfglobal.iqv['evm_sorted'] = 0
        mask_marg_title = "lower4_marg, lower3_marg, lower2_marg, lower1_marg, upper1_marg, upper2_marg, upper3_marg, upper4_marg"
        title = 'channel, rate,delay, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage(dB),iq_imb_amp(dB),iq_imb_phase(deg),%s, evm_list\n'%mask_marg_title
        fname = self.wifi.get_filename('wifi_txrx_test_%s'%name_str, 'TX')
        csvreport1 = csvreport(fname, title)

        self.wifi.cmdstop()
        max_pwr = 25 - cable_lose

        self.wifi.txpacket(1, '54m', 0, 0, duty=0.1)
        test_para = wifi_instrum.test_para('54m')
        myiqv=tester.tester(2412, max_pwr, '54m', test_para, iqv_no,'measure', cable_lose, 10,1,1,20)
        [pwr, freq_err, clk_err, evm, evm_std, evm_max,lo_leakage,iq_imb_amp,iq_imb_phase, evm_list] = wifi_instrum.iqv_avg(myiqv, 1,'false')

        self.wifi.save_init_print('wifi_txrx_test_%s'%name_str)

        for rate in rate_dict:
            for chan in channel:

                loginfo("rate=%s, channel=%d,cable_lose=%2.2f"%(rate, chan,cable_lose))

                self.wifi.cmdstop()
##                cbw40m = self.wifi.rate2ht40(rate)
##                self.wifi.tx_cbw40m_en(cbw40m)
                for delay in range(100,500,2):
                    result=[]
                    if type(rate) == str:
                        rate_num = self.wifi.ratecheck(rate)
                        print rate_num
                    result =self.wifiapi.esp_tx(chan, rate_num,0)
                    print result

                    result_m = result.split(",")
                    length = result_m[3].split("=")
                    length_m =int(length[1],10)
                    print [rate_num, length_m]
                    self.wifiapi.RF_init_sel(0)
                    print self.wifiapi.RF_init_sel
                    self.wifiapi.esp_tx_debug(chan,rate_num,0,length_m,delay)

                    test_para = wifi_instrum.test_para(rate)
                    if chan<=14:
                        freq = self.wifi.chan2freq(chan)
                    else:
                        freq = chan

                    myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0,1,20)
                    [pwr, freq_err, clk_err, evm, evm_std, evm_max, lo_leakage,iq_imb_amp,iq_imb_phase,evm_list] = wifi_instrum.iqv_avg(myiqv, 20,'false')
                    [freq_mask, mask_marg] =  wifi_instrum.spectrum_mask_flatness(myiqv, 20, 99)


                    self.wifi.cmdstop()
                    csvreport1.write_data([chan,rate,delay,pwr,evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase, mask_marg, evm_list])
                    print [chan,rate,delay,pwr,evm,evm_std,evm_max]

            for data in result:
                print data


    def test_case(self,sel=0xf,cable_lose=2,iqv_no=2,name_str=""):

        self.wifi.save_init_print(self.folder)

        if (sel & 0x1) > 0:
            self.bt_test.bt_test_case(2)

        if (sel & 0x2) > 0:
            self.txrx.WIFI_TX_PWR_EVM(cable_lose=cable_lose, channel=[1,3,5,7,9,11,13], data_rate=['mcs7','mcs0','mcs7_40','mcs0_40','54m','6m','11m','1m'],iqv_no=iqv_no,iqv_num=20, force_txon=0,name_str=name_str)  # wifi_txout
            self.txrx.WIFI_TX_PWR_EVM(cable_lose=cable_lose, channel=[1,3,5,7,9,11,13], data_rate=['mcs7','mcs0','mcs7_40','mcs0_40','54m','6m','11m','1m'],iqv_no=iqv_no,iqv_num=20, force_txon=1,name_str=name_str)  # esp_tx
            self.txrx.WIFI_RX_sens(cable_lose=cable_lose, chan_in=[1,3,5,7,9,11,13], data_rate=['mcs7','mcs0','mcs7_40','mcs0_40','54m','6m','11m','1m'],packnum=100,loop_num=1,iqv_no=iqv_no,name_str=name_str)
            self.txrx.WIFI_RX_maxlevel(cable_lose=cable_lose, chan_in=[1,3,5,7,9,11,13],  data_rate=['mcs7','mcs0','mcs7_40','mcs0_40','54m','6m','11m','1m'], iqv_no=iqv_no,name_str=name_str)

        if (sel & 0x4) >0:
            self.wifi_tx_tone(en=1,channel=[1,6,11],backoff=0,name_str=name_str)
#
        if (sel & 0x8)>0:
            self.bt_tx_tone(en=1,channel=[1,39,78],backoff=0,name_str=name_str)
#Backoff_Verify

        if (sel & 0x10)>0:
            self.backoff_verify(cable_lose=cable_lose,rate='54m',channel=[1],iqv_no=iqv_no)

#ACK Test
        if (sel & 0x20)>0:
            self.ack_test.wifi_ack_test_case(comp_atten=14,chan=1,test_mode=0,data_rate=['1m'])


##        if(self & 0x16)>0:

##            self.txpwr_track_en()
##            self.tx_continue_en()









