import time
import csv
import os
import sys
import re
import matplotlib.pyplot as plt
import pylab
from baselib.loglib.log_lib import *
from rftest.rflib.csv_report import csvreport
from rftest.rflib.wifi_lib import WIFILIB
from hal.wifi_api import WIFIAPI
from hal.rtc_sleep import RTC_SLEEP
from hal.Init import HALS
from rftest.rflib import rfglobal
from rftest.testcase.rf_debug.packets_test import Packet_Test
rate_dict = rfglobal.ratedic
sens_dict = rfglobal.sens_dict
class ACK_Test(object):

    def __init__(self, comport, chipv = "ESP32"):

        self.comport = comport
        self.chipv = chipv
        self.wifiapi = WIFIAPI(self.comport,self.chipv)
        self.hals = HALS(self.comport,self.chipv)
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.sleep = RTC_SLEEP(self.comport, self.chipv)
        self.packet_test = Packet_Test(self.comport, self.chipv)

    def tx_ack_test(self,ap_addr0=0x0,ap_addr1=0x0,tx_rate=0x10,tx_num=100):

        result_data = self.wifiapi.tx_ack_test(ap_addr0,ap_addr1,tx_rate,tx_num,100,1,3,0)
        result=str.split(result_data)
        flag = str(result[-11])
        tx_num = int(result[-9])
        ack_num = int(result[-7])
        rssi = float(result[-5])/10
        rssi_max = int(result[-3])
        rssi_min = int(result[-1])
        return [flag,tx_num,ack_num,rssi,rssi_max,rssi_min]

    def sleep_proc(self, sleep_mode=0x40):
        loginfo('sleep')
        self.sleep.rtc_timer_wakeup(0, 0x50000)
        self.sleep.sleep(sleep_mode, 8, 0)
        loginfo('wake up')

    def ack_test_case(self,comp_atten=14,chan=1,sleep_mode_en=0,sleep_mode=0x40,data_rate=['1m'],tx_num=100):
        #sleep_mode : 0x40 -- light sleep; 0x3f -- deep_sleep
        logsetlevel('D')
        title = 'rx_chan,tx_rate, flag,tx_num,ack_num,rssi,rssi_max,rssi_min,atten_set,atten\n'
        fname = self.wifi.get_filename('ack_test_data',  'ack_test')
        csvreport1 = csvreport(fname, title)

##        ap_addr0 = 0xA8178980
##        ap_addr1 = 0x6B06

        ap_addr0 = 0x44353ac8
        ap_addr1 = 0x8865
        res = -99
        for cur_rate in data_rate:

            cbw40m = self.wifi.rate2ht40(cur_rate)
            ratenum = self.wifi.ratecheck(cur_rate)
            if cbw40m == 1:
                if chan <3: chan = 3
                elif chan>11: chan = 11
            self.wifi.rfchsel(chan,cbw40m*2)

            if sleep_mode_en ==1:
                self.sleep_proc(sleep_mode)
                if sleep_mode == 0x40:
                    self.hals.rtc_clk.set_cpu_freq(5)
                    self.wifiapi.rftest_init()
                time.sleep(1)
                self.wifi.rfchsel(chan,cbw40m*2)
            sens_target = sens_dict[cur_rate]

            atten = 0
            res = self.packet_test.set_att(atten,comp_atten)

            self.wifiapi.cbw40m_en(cbw40m)
            [flag,tx_num,ack_num,rssi,rssi_max,rssi_min] = self.tx_ack_test(ap_addr0,ap_addr1,ratenum,tx_num)
            loginfo('first,aten_set:%s,%d,cur_rate=%s,flag=%s,tx_num=%d,ack_num=%d,rssi=%2.1f,rssi_max=%d,rssi_min=%d'%(res,atten,cur_rate,flag,tx_num,ack_num,rssi,rssi_max,rssi_min))

            set_atten = int(rssi - sens_target)
            loginfo( 'rssi:%2.1f set_atten:%d'%(rssi,set_atten))

            for att_offset in range(6,-15,-1):
                atten = att_offset+set_atten
                res = self.packet_test.set_att(atten,comp_atten)

                [flag,tx_num,ack_num,rssi,rssi_max,rssi_min] = self.tx_ack_test(ap_addr0,ap_addr1,ratenum,tx_num)
                loginfo('aten_set:%s,%d,cur_rate=%s,flag=%s,tx_num=%d,ack_num=%d,rssi=%2.1f,rssi_max=%d,rssi_min=%d'%(res,atten,cur_rate,flag,tx_num,ack_num,rssi,rssi_max,rssi_min))
                csvreport1.write_data([chan,str(cur_rate),flag,tx_num,ack_num,rssi,rssi_max,rssi_min,res,atten])



    def wifi_ack_test_case(self,comp_atten=14,chan=1,test_mode=0,data_rate=['1m']):
        #test_mode :
        # 0 : normal mode
        # 1 : set channel
        # 2 : modem sleep
        # 3 : light sleep WIFP_NO_PD
        # 4 : light sleep WIFP_PD
        # 5 : bt coex //ESP32

        logsetlevel('D')
        title = 'rx_chan,tx_rate, flag,tx_num,ack_num,rssi,res,atten\n'
        fname = self.wifi.get_filename('ack_test_data',  'ack_test')
        csvreport1 = csvreport(fname, title)
##
##        ap_addr0 = 0xA8178980
##        ap_addr1 = 0x6B06

##        ap_addr0 = 0x44353ac8   #C8:3A:35:44:65:88
##        ap_addr1 = 0x8865

##        ap_addr0 = 0x3FA50574
##        ap_addr1 = 0x41EC

##        ap_addr0 = 0xce34fe18
##        ap_addr1 = 0x8924

        ap_addr0 = 0x03020100 # 00:01:02:03:04:05 CMW500
        ap_addr1 = 0x0504

        tx_length = 100
        backoff = 1
        delay_ms = 0
        tx_num=100
        test_num_0 = 1
        test_num_loop = 1
        res = -99
        for cur_rate in data_rate:
            atten = 0
            cbw40m = self.wifi.rate2ht40(cur_rate)
            ratenum = self.wifi.ratecheck(cur_rate)
            sens_target = sens_dict[cur_rate]
            if cur_rate == 'mcs0':
                sens_target = sens_dict['6m']
            elif cur_rate == 'mcs7'or cur_rate == '54m':
                sens_target = sens_dict['24m']
            if cbw40m == 1:
                if chan <3: chan = 3
                elif chan>11: chan = 11
            self.wifi.rfchsel(chan,cbw40m*2)
            self.wifiapi.cbw40m_en(cbw40m)

            res = self.packet_test.set_att(atten,comp_atten)

            test_result = self.wifiapi.wifi_ack_test(ap_addr0,ap_addr1,ratenum,tx_length,chan,cbw40m*2,tx_num,test_num_0, backoff ,test_mode, delay_ms)

            result = test_result.split(',')
            ack_num = int(result[-2-test_num_0*2-2])
            rssi = float(result[-2-test_num_0-1])/10
            ack_mask = str(result[-2])


            loginfo('first,atten_set:%s,%d,cur_rate=%s,tx_num=%d,ack_mask=%s ,ack_num=%d,rssi=%2.1f'%(res,atten,cur_rate,tx_num,ack_mask ,ack_num,rssi))

            set_atten = int(rssi - sens_target)
            loginfo( 'rssi:%2.1f set_atten:%d'%(rssi,set_atten))
##
            for att_offset in range(16,-10,-1):
                atten = att_offset+set_atten
                res = self.packet_test.set_att(atten,comp_atten)

                test_result = self.wifiapi.wifi_ack_test(ap_addr0,ap_addr1,ratenum,tx_length,chan,cbw40m*2,tx_num,test_num_loop, backoff ,test_mode, delay_ms)
                result = test_result.split(',')
                ack_num = int(result[-2-test_num_0*2-2])
                rssi = float(result[-2-test_num_0-1])/10
                ack_mask = str(result[-2])

                loginfo('atten_set:%s,%d,cur_rate=%s,tx_num=%d,ack_mask=%s ,ack_num=%d,rssi=%2.1f'%(res,atten,cur_rate,tx_num,ack_mask ,ack_num,rssi))
                csvreport1.write_data([chan,str(cur_rate),ack_mask,tx_num,ack_num,rssi,res,atten])


    def coex_mode_test(self):
        ap_mac1 = 0x44353ac8
        ap_mac2 = 0x8865
        rate = 0x17
        pocket_len = 100
        num = 32
        backoff = 1
        loop_num = 4
        test_num = 10
        title = 'coex_mode, mode_str, loop_num, tx_num, ack_num, ack_mask, rssi, test_result\n'
        fname = self.wifi.get_filename('ack_test_data',  'coex_ack_test')
        csvreport1 = csvreport(fname, title)

        self.wifi.rfchsel(10, 0)
        self.wifiapi.tx_ack_test(ap_mac1, ap_mac2, rate, num, pocket_len,backoff)
        for coex_mode in range(0,7):
            mode_str = self.wifiapi.coex_test(coex_mode)
            time.sleep(0.5)
            for i in range(0, loop_num):
                test_result = self.wifiapi.wifi_ack_test(num, test_num)
                result = test_result.split(',')
                ack_num = result[1]
                ack_mask = result[1+test_num*2+2]
                rssi = result[1+test_num+1]
                csvreport1.write_data([coex_mode, mode_str, i, num, ack_num, ack_mask, rssi, test_result])

    def sleep_mode_test(self):
        ap_mac1 = 0x44353ac8
        ap_mac2 = 0x8865
        rate = 0x17
        pocket_len = 100
        pocket_num = 32
        backoff = 1
        loop_num = 10
        test_num = 10
        title = 'test_mode, mode_str, loop_num, tx_num, ack_num, ack_mask, rssi, test_result\n'
        fname = self.wifi.get_filename('ack_test_data',  'sleep_ack_test')
        csvreport1 = csvreport(fname, title)

        self.wifi.rfchsel(10, 0)
        self.wifiapi.tx_ack_test(ap_mac1, ap_mac2, rate, pocket_num, pocket_len,backoff)
        for test_mode in range(0,4):
            if test_mode==0:
                mode_str = 'set_channel'
            elif test_mode==1:
                mode_str = 'modem_sleep'
            elif test_mode==2:
                mode_str = 'light_sleep NO WIFI_PD'
            else:
                mode_str = 'light_sleep WIFI_PD'
            for i in range(0, loop_num):
                test_result = self.wifiapi.wifi_ack_test(pocket_num, test_num, test_mode=test_mode+1)
                result = test_result.split(',')
                ack_num = result[1]
                ack_mask = result[1+test_num*2+2]
                rssi = result[1+test_num+1]
                csvreport1.write_data([test_mode, mode_str, i, pocket_num, ack_num, ack_mask, rssi, test_result])

