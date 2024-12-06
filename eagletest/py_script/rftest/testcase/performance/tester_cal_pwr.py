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
import re
import serial
from hal.wifi_api import WIFIAPI
import rftest.rflib.wifi_instrum as wifi_instrum
from rftest.rflib.wifi_lib import WIFILIB
from rftest.rflib.csv_report import csvreport
from rftest.testcase.performance.wifi_txrx_test import WIFI_TXRX_TEST
from rftest.testcase.rf_debug.basic_test import BasicTest

class TESTER_CAL_PWR(object):

    def __init__(self,comport,chipv='ESP32'):
        self.comport = comport
        self.chipv = chipv
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.wifiapi = WIFIAPI(self.comport,self.chipv)
        self.txrx = WIFI_TXRX_TEST(self.comport,self.chipv)
        self.basic = BasicTest(self.comport,self.chipv)


    def WIFI_TX_PWR_CAL(self, cable_lose=2, rate='mcs7', target_pwr=13, iqv_no=1, iqv_num=10, name_str=""):
        """
        :test TX power and EVM
        :cable_lost:
        :channle: it is matrix [1,...]
        :data_rate: it is matrix ['mcs0',...]
        :iqv_no: 1-left port, 2-right port
        :iqv_num: iqview average number
        """
        self.comport.req_com("esp_en_reboot")

        title = 'channel, rate, offset,power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage(dB),iq_imb_amp(dB),iq_imb_phase(deg), evm_list\n'
        fname = self.wifi.get_filename('tester_cal_pwr_%s'%name_str, 'TX')
        csvreport1 = csvreport(fname, title)

        self.wifi.cmdstop()
        max_pwr = 25 - cable_lose

        self.wifi.txpacket(1, '54m', 0, 0, duty=0.1)
        test_para = wifi_instrum.test_para('54m')
        myiqv=tester.tester(2412, max_pwr, '54m', test_para, iqv_no,'measure', cable_lose, 10,1, 1,20)
        [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 1,'false')

        max_pwr = pwr + 12
        print "max_pwr=%f"%max_pwr

        tt_max = 4
        channel=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        self.wifi.save_init_print('tester_cal_pwr_%s_cal_mcs7'%name_str)
        for chan in channel:
            offset = 0
            for tt in range(0,tt_max):
                loginfo("rate=%s, channel=%d"%(rate, chan))
                self.wifi.cmdstop()
                cbw40m = self.wifi.rate2ht40(rate)

                self.wifi.txpacket(chan, rate, 0, cbw40m, backoff_qdb=0,duty=0.1)

                test_para = wifi_instrum.test_para(rate)
                if chan<=14:
                    freq = self.wifi.chan2freq(chan)
                else:
                    freq = chan

                myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0, 1,20)
                [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false')

                self.wifi.cmdstop()
                if tt < (tt_max - 1):
                    if abs(pwr - target_pwr) < 0.15 :
                        break
                    offset += int(round((pwr - target_pwr)*4))
                    if offset < 0:
                        offset = 256 + offset
                    self.comport.req_com("chan_power_correct_offset %d %d"%(chan,offset))

                    print chan,pwr,offset



            csvreport1.write_data([chan,rate,offset,pwr,evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase,evm_list])
            print [chan,rate,offset,pwr,evm,evm_std,evm_max]

        self.comport.req_com("wr_rf_cal_data")
        self.wifi.save_init_print('tester_cal_pwr_%s_cal_mcs7'%name_str)


    def TX_PWR_CAL_testcase(self,case=1,cable_lose=13.9,iqv_no=1,name_str=""):

        if case == 1:
            self.txrx.WIFI_TX_PWR_EVM(cable_lose=cable_lose, channel=[1,2,3,4,5,6,7,8,9,10,11,12,13,14], data_rate=['mcs7','1m'],iqv_no=iqv_no,iqv_num=10, force_txon=0,name_str=name_str+'_org')

            self.WIFI_TX_PWR_CAL(cable_lose=13.9, rate='mcs7', target_pwr=13, iqv_no=iqv_no, iqv_num=10, name_str=name_str+'_cal_mcs7')

            self.comport.req_com("test_rf_cal_level 1")
            self.wifi.save_init_print('tester_cal_pwr_%s_l1'%name_str)
            self.txrx.WIFI_TX_PWR_EVM(cable_lose=cable_lose, channel=[1,2,3,4,5,6,7,8,9,10,11,12,13,14], data_rate=['mcs7','1m'],iqv_no=iqv_no,iqv_num=10, force_txon=0,name_str=name_str+'_level1')

            self.comport.req_com("test_rf_cal_level 0")
            self.wifi.save_init_print('tester_cal_pwr_%s_l0'%name_str)
            self.txrx.WIFI_TX_PWR_EVM(cable_lose=cable_lose, channel=[1,2,3,4,5,6,7,8,9,10,11,12,13,14], data_rate=['mcs7','1m'],iqv_no=iqv_no,iqv_num=10, force_txon=0,name_str=name_str+'_level0')

        if case == 2:
            cable_lost_list=self.wifi.get_rx_cable_lost(iqv_unit_no=iqv_no, cable_att=30, chan_m=[1,2,3,4,5,6,7,8,9,10,11,12,13,14],noise_ref=-95.2)
            self.txrx.WIFI_TX_PWR_EVM_cable_list(cable_lose_list=cable_lost_list, channel=[1,2,3,4,5,6,7,8,9,10,11,12,13,14], data_rate=['mcs7','1m'],iqv_no=iqv_no,iqv_num=10, force_txon=0,name_str=name_str+'_org')

            self.comport.req_com("test_rf_cal_level 1")
            self.wifi.save_init_print('tester_cal_pwr_%s_l1'%name_str)
            self.txrx.WIFI_TX_PWR_EVM_cable_list(cable_lose_list=cable_lost_list, channel=[1,2,3,4,5,6,7,8,9,10,11,12,13,14], data_rate=['mcs7','1m'],iqv_no=iqv_no,iqv_num=10, force_txon=0,name_str=name_str+'_level1')

            self.comport.req_com("test_rf_cal_level 0")
            self.wifi.save_init_print('tester_cal_pwr_%s_l0'%name_str)
            self.txrx.WIFI_TX_PWR_EVM_cable_list(cable_lose_list=cable_lost_list, channel=[1,2,3,4,5,6,7,8,9,10,11,12,13,14], data_rate=['mcs7','1m'],iqv_no=iqv_no,iqv_num=10, force_txon=0,name_str=name_str+'_level0')
