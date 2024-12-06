import time
import csv
import os
import serial
import re
import matplotlib.pyplot as plt
import pylab
from baselib.loglib.log_lib import *
from hal.Init import HALS
from baselib.test_channel.com import COM as com
from baselib.instrument import tester
from rftest.rflib.wifi_lib import WIFILIB
import rftest.rflib.wifi_instrum as wifi_instrum

class Iperf_Test(object):

    def __init__(self, comport, chipv = "ESP32"):

        self.comport = comport
        self.chipv = chipv
        self.wifi = WIFILIB(self.comport,self.chipv)


    def test_iperf(self, comp_sta=5,inter_freq=[2437,2462],step=5, cable_lose=0,iqv=1):

        filetime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()));
        filename = self.wifi.get_filename('test_iperf', 'test_iperf')
        file_w = '%s_%s.log'%(filename, filetime)
        f=open(file_w, 'a')
        logsetlevel('D')

        mytester=tester.tester(2437,-90,'1m',1,iqv,'source',cable_lose,isreset=1)
        loginfo("mytester init")

        chip_sta = HALS(com(comp_sta),"ESP32")
        self.comport.req_com("restart")
        time.sleep(4)
        self.comport.req_com("ap chenling")

        loginfo("ap ok")
        for freq in inter_freq:
            for inter_pwr in range(-60,-10, step):
                f=open(file_w, 'a')
                f.write("\n\n")

                chip_sta.channel.req_com("restart")
                time.sleep(10)
                result_scan = chip_sta.channel.req_com("scan", endstr= 'sta scan done')
                chip_sta.channel.req_com("sta chenling")
                chip_sta.channel.req_com("iperf -s -u")

                loginfo("sta ok")
                wifi_instrum.instru_tx_signal(source='6m', tx_freq=freq,tx_pwr=inter_pwr, tx_rate='6m', packnum=0,cable_lose=cable_lose,iqv_no=iqv)
                self.comport.req_com("iperf -c 192.168.4.2 -t 60 -u")
                result_sta =  chip_sta.channel.req_com("", endstr= 'iperf exit')
                while re.findall(r'(sta disconnect, reconnect...)',result_sta,re.M)!=[]: break
                result_ap =  self.comport.req_com("", endstr= 'iperf exit')
                f.write("sta, freq:%d, inter_pwr:%d\n"%(freq,inter_pwr))
                f.write(result_scan)
                f.write(result_sta)
                f.write("\n\n")
                f.write("ap, freq:%d, inter_pwr:%d\n"%(freq,inter_pwr))
                f.write(result_ap)
                f.close()




