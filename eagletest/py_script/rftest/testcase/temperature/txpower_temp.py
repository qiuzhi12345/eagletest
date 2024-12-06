#-------------------------------------------------------------------------------
# Name:        TXPower VS Temperature
# Purpose:
#
# Author:      QZ
#
# Created:     17/12/2018
# Copyright:   (c) Test 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time
import re
import csv
import os, sys
import matplotlib.pyplot as plt
import pylab
import numpy as np
from baselib.loglib.log_lib import *
from baselib.test_channel.com import COM as com
from baselib.instrument.spa import HP,Agilent
from rftest.rflib.wifi_lib import WIFILIB
from hal.Init import HALS
from hal.common import *
from hal.common import MEM
from rftest.rflib.pbus import pbus
from rftest.rflib.rfpll import rfpll
from rftest.rflib.rfcal import rfcal
import rftest.rflib.rfglobal as rfglobal
import rftest.rflib.wifi_instrum as rftx

class TXPower_spa(object):
    def __init__(self,comport,chipv="ESP32"):
        self.comport=channel
        self.chipv=chipv
        self.wifi = WIFILIB(self.comport,self.chipv)
        ##self.wifitx = WIFITX(self.comport,self.chipv)
        ##self.wifirx = WIFIRX(self.comport,self.chipv)
        self.mem=MEM(self.comport,self.chipv)
        self.pbus = pbus(self.comport, self.chipv)
        self.rfcal = rfcal(self.comport, self.chipv)
        self.rfpll = rfpll(self.comport, self.chipv)

    def spa_sel(self,instrument="HP"):
        if instrument=="HP":
            self.tester=HP()

        else:
            self.tester=Agilent()

    def get_txpower(self,freq=2440,atten=40,Gain_Filter=0x120,Gain_PA=0x5f):
        self.tester.reset()
        self.tester.set_param(cfreq=freq,span=10,rb=100,vb=30)
        self.rfpll.set_freq(freq)
        self.pbus.pbus_debugmode()
        self.pbus.open_tx()
        self.pbus.pbus_wr('bb','en2',Gain_Filter);# Set Filter Gain
        self.pbus.pbus_wr('rftx2','en1',Gain_PA);# Set Filter Gain
        self.rfcal.tos()
        self.mem.wrm(0x600060a0,17,16,0x3)
        self.wifi.txtone(1,0,atten)
        result=self.tester.pk_detect()
        self.wifi.stoptone()
        self.rflib.pbus.open_rx()
        self.rflib.pbus.pbus_workmode()
        return result

class test01_txpower_temp(object):
    def __init__(self,channel_list=[],chipv="ESP32"):
        chanlist=[]
        self.com_list=channel_list
        for num in range(len(channel_list)):
            chan="com(%d)"%channel_list[num]
            chanlist.append(eval(chan))
        self.comport_list = chanlist
        self.chipv = chipv
        self.curr_data_path = 'D:/chip/eagletest/rfdata/txpower_temp_data/'

    def _test_txp_temp(self,freq=2440,atten=0,Gain_Filter=0x120,Gain_PA=0x5f,instru="HP",temp=25):
        txplist=[]
        Test_state = 'This Test was developed for txpower_temperature Test';
        # CSV Table Generate
        filetime = time.strftime('_%Y%m%d_%H%M%S',time.localtime(time.time()));
        folder = self.curr_data_path + 'TXPower_temp_Test_%s'%filetime;
        data_path = folder +'/'
        os.mkdir(folder)

        with open(data_path+'TXPower_temp_Test_%s.csv'%filetime, 'ab+') as f:
            f_csv=csv.writer(f)
            f_csv.writerow(['Test Introduction : %s'%Test_state])
            headers=['temperature','com_num','chip_id','freq_set','atten','Gain_Filter','Gain_PA','freq_meas','txpower']
            f_csv.writerow(headers)
            while 1:
                for i in range(len(self.comport_list)):
                    channel=self.comport_list[i]
                    loginfo("test com: com%d"%self.com_list[i])
                    _tester=TXPower_spa(channel)
                    chip_id=CHIP_ID(channel,self.chipv).chip_mac()
                    _tester.spa_sel(instru)
                    for atten in range(0,41,4):
                        loginfo("com%d set para:freq= %d,atten= %d,Gain_Filter= 0x%x,Gain_PA= 0x%x,temp= %d"%(self.com_list[i],freq,atten,Gain_Filter,Gain_PA,temp))
                        (freq_meas,txp)=_tester.get_txpower(freq,atten,Gain_Filter,Gain_PA)
                        f_csv.writerow([temp,self.com_list[i],chip_id,freq,atten,hex(Gain_Filter),hex(Gain_PA),freq_meas,txp])
                        txplist.append((freq_meas,txp))
                #return txplist
                input_str=raw_input("please input present temperature:")
                print input_str
                if input_str=="quit":
                    break
                else:
                    temp=int(input_str)





