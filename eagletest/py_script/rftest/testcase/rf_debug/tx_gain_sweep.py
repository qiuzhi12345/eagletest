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
from hal.rtc_debug import RTC_DEBUG
from hal.common import MEM
from hal.hwregister.hwi2c.all import HWI2C
from rftest.rflib.pbus import pbus
import rftest.rflib.rfglobal as rfglobal
from rftest.rflib.rfpll import rfpll
from rftest.rflib.rfcal import rfcal
import rftest.rflib.wifi_instrum as wifi_instrum
from baselib.loglib.log_lib import *
from rftest.rflib.saradc import SARADC
from rftest.rflib.csv_report import csvreport
rfglobal.iqv['evm_sorted'] = 0


#rftx_lst = [0xf,0x1f,0x2f,0x3f,0x4f,0x5f,0x6f,0x7f]
           #-9.75,-6.25,-3.75,-1.75,0,1.5,2.75
#bbgain_lst = [0x0,0x40,0x80,0xc0,0x100,0x140,0x20,0x60,0xa0,0xe0,0x120,0x160,0x30,0x70,0xb0,0xf0,0x130,0x170,0x38,0x78,0xb8,0xf8,0x138,0x178]
#             [0db, 1db, 2db, 3db, 4db, 5db , 6dB ,7dB, 8dB, 9db, 10db, 11db, 12db,13db,14db,15db,16db, 17dB,18dB,19db,20dB,21dB,22dB,23dB]

class Sweep_TX_Gain(object):

    def __init__(self,comport,chipv='ESP32'):

        self.comport = comport
        self.chipv = chipv
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.rtc_debug = RTC_DEBUG(self.comport,self.chipv)
        self.pbus = pbus(self.comport, self.chipv)
        self.mem = MEM(self.comport, self.chipv)
        self.rfcal = rfcal(self.comport, self.chipv)
        self.rfpll = rfpll(self.comport, self.chipv)
        self.hals = HALS(self.comport,self.chipv)
        self.saradc = SARADC(self.comport,self.chipv)
        self.wifiapi = WIFIAPI(self.comport,self.chipv)
        self.hwi2c = HWI2C(self.comport,self.chipv)




    def tx_gain_evm(self, cable_lose=2, channel=[1,14],iqv_no=1,iqv_num=10, rc_en=0,name_str=""):
        """
        :test TX power and EVM
        :cable_lost:
        :channle: it is matrix [1,...]
        :data_rate: it is matrix ['mcs0',...]
        :iqv_no: 1-left port, 2-right port
        :iqv_num: iqview average number
        """
        logsetlevel('I')

        title = 'pa_gain, filt_gain, dig_atten, channel, rate, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage(dB),iq_imb_amp(dB),iq_imb_phase(deg),evm_list\n'
        fname = self.wifi.get_filename('sweep_tx_gain', 'TX_GAIN_vs_EVM_%s'%name_str,'tx_gain_vs_evm')
        csvreport1 = csvreport(fname, title)

        self.wifi.cmdstop()
        max_pwr = 25 - cable_lose

        self.wifi.txpacket(1, '54m', 0, 0)
        test_para = wifi_instrum.test_para('54m')
        myiqv=tester.tester(2412, max_pwr, '54m', test_para, iqv_no,'measure', cable_lose, 10, 1, 1)
        [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 1,'false')

        max_pwr = pwr + 12
        print "max_pwr=%d"%max_pwr

        rate = 'mcs7'
        pa_gain_m = [0xf] #,0xf,0x1f,0x2f,0x3f,0x4f,0x5f,0x6f,0x7f]
        if rc_en==0:
            filt_gain_m = [0x20]
            #filt_gain_m = [0,0x80,0x100,0x20,0xa0,0x120,0x1a0,0x30]
            [txdci, txdcq] = [0, 0]
        else:
            filt_gain_m = [0]
            [txdci, txdcq] = self.rc_txdc_cal(cable_lose, iqv_no,num=12)

##        dig_atten_m = [24,20,16,8,4,0,-4,-8,-12,-16,-20,-24]
        dig_atten_m = [16,8,4,0,-4,-8,-12,-16]
        for chan in channel:
            for pa_gain in pa_gain_m:
                for filt_gain in filt_gain_m:
                    for dig_atten in dig_atten_m:

                        self.wifi.cmdstop()
                        cbw40m = self.wifi.rate2ht40(rate)
                        if chan<=14:
                            freq = self.wifi.chan2freq(chan)
                        else:
                            freq = chan
                        self.wifi.tx_rc_filter(rc_en, txdci, txdcq)
                        self.wifi.txp_force_gain(chan,rate, pa_gain, filt_gain, dig_atten)
##                        self.wifi.txpacket(chan, rate, 0, cbw40m)
##                        self.wifi.force_tx_gain_init(chan, rate, pa_gain, filt_gain, dig_atten)
                        test_para = wifi_instrum.test_para(rate)
                        myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0, 0,20)
                        [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false', -15)
                        loginfo("rate=%s, pa_gain=0x%x, filt_gain=0x%x, dig_atten=%d, channel=%d,power=%2.2f,evm=%2.2f"%(rate,pa_gain, filt_gain, dig_atten,chan,pwr, evm))
                        csvreport1.write_data([hex(pa_gain), hex(filt_gain), dig_atten,chan,rate,pwr,evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase, evm_list])
                        print [chan,rate,pwr,evm,evm_std,evm_max,freq_err,clk_err,lo_leakage,iq_imb_amp,iq_imb_phase, evm_list]

                    if pwr>16:
                        break

        logsetlevel('D')

    def rc_txdc_cal(self, cable_lose=2, iqv_no=2,num=12):
        logsetlevel('E')
        rate = '11m'
        self.wifi.rfchsel(1)
        test_para = wifi_instrum.test_para(rate)
        myiqv=tester.tester(2412, 5, rate, test_para, iqv_no,'measure', cable_lose, 10, 1, 0,20)

        txdci = -(num/2*10)
        txdcq = 0

        for fine in range(0,2):
            if fine==0:
                step=10
            else:
                step=2

            if fine == 1:
                txdci -= (num/2*step)

            for iq in range(0, 2):

                lo_m = []
                txdc_m = []
                if iq==0:
                    txdc = txdci
                else:
                    txdc = txdcq

                for i in range(0,num):
                    self.wifi.tx_rc_filter(1, txdci,txdcq)
                    self.wifi.txp_force_gain(1, rate, 0xf, 0x30, 0)  ##max_power=5
                    [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 1,'false')
                    lo_m.append(lo_leakage)
                    txdc_m.append(txdc)
                    print 'i=%d: txdci=%d, txdcq=%d, lo=%2.2f, step=%d'%(i,txdci, txdcq,lo_leakage, step)

##                    if i>0 and lo_leakage > lo_old:
##                        break

                    txdc += step
                    if iq==0:
                        txdci = txdc
                    else:
                        txdcq = txdc

                    lo_old = lo_leakage

                lo_min = min(lo_m)
                txdc = txdc_m[lo_m.index(lo_min)]
                print lo_m
                print txdc_m
                print "lo_min=%2.2f, txdc=%d"%(lo_min, txdc)

                if iq==0:
                    txdci = txdc
                    if fine==0:
                        txdcq =  -(num/2*step)
                    else:
                        txdcq -= (num/2*step)
                else:
                    txdcq = txdc
        logsetlevel('I')
        return [txdci, txdcq]



    def tx_gain_fast_test(self, cable_lose=2, channel=[1], iqv_no=1,iqv_num=10,name_str=''):
        """
        :test TX power and EVM
        :cable_lost:
        :channle: it is matrix [1,...]
        :data_rate: it is matrix ['mcs0',...]
        :iqv_no: 1-left port, 2-right port
        :iqv_num: iqview average number
        """
        logsetlevel('D')
        rfglobal.iqv['evm_sorted'] = 1
        title = 'pa_gain, bb_gain, dig_atten, txdci,txdcq,txdci_f,txdcq_f,channel, rate, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage(dB),iq_imb_amp(dB),iq_imb_phase(deg),evm_list\n'
        fname = self.wifi.get_filename('sweep_tx_gain', 'tx_gain_fast_test_%s'%name_str)
        csvreport1 = csvreport(fname, title)

        self.wifi.cmdstop()
        max_pwr = 25 - cable_lose

        self.wifi.txpacket(1, '54m', 0, 0)
        test_para = wifi_instrum.test_para('54m')
        myiqv=tester.tester(2412, max_pwr, '54m', test_para, iqv_no,'measure', cable_lose, 10, 1, 1,20)
        [pwr, freq_err, clk_err, evm, evm_std, evm_max, lo_leakage,iq_imb_amp,iq_imb_phase,evm_list] = wifi_instrum.iqv_avg(myiqv, 1,'false')

        max_pwr = pwr + 12
        print "max_pwr=%d"%max_pwr

        rate = 'mcs7'
        chan = channel[0]
        pa_gain_m = [0x0,0x1,0x2,0x3,0x4,0x8,0xc,0x10,0x20,0x30,0x40,0x50,0x60,0x70,0xf,0x1f,0x2f,0x3f,0x4f,0x5f,0x6f,0x7f]
        bb_gain_m = [0x0,0x40,0x80,0xc0,0x100,0x140,0x20,0x60,0xa0,0xe0,0x120,0x160,0x30,0x70,0xb0,0xf0,0x130]
        dig_atten = 12

        for i in range(0,2):
##            for gain in range(0,128):
##                if i ==0:
##                    pa_gain = gain
##                    bb_gain = 0x0
            if i==0:
                gain_m = pa_gain_m
            else:
                gain_m = bb_gain_m

            for gain in gain_m:
                if i ==0:
                    pa_gain = gain
                    bb_gain = 0x20
                else:
                    pa_gain = 0x3f
                    bb_gain = gain

                cbw40m = self.wifi.rate2ht40(rate)
                print "dddd"
                self.wifi.tx_rc_filter(0, 0, 0)
                result = self.wifiapi.set_tx_gain(pa_gain, bb_gain)
                result = result.split(',')
                txdco = result[3:7]

                self.wifi.txp_force_gain(2412, rate, pa_gain, bb_gain, dig_atten)
                self.wifi.txpacket(chan, rate, 0, cbw40m)

                test_para = wifi_instrum.test_para(rate)
                if chan<=14:
                    freq = self.wifi.chan2freq(chan)
                else:
                    freq = chan

                myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0, 1,20)
                [pwr, freq_err, clk_err, evm, evm_std, evm_max, lo_leakage,iq_imb_amp,iq_imb_phase,evm_list] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false', -15)

                loginfo("rate=%s, pa_gain=0x%x, bb_gain=0x%x, dig_atten=%d, channel=%d,power=%2.2f,evm=%2.2f"%(rate,pa_gain, bb_gain, dig_atten,chan,pwr, evm))
                csvreport1.write_data([hex(pa_gain), hex(bb_gain), dig_atten, txdco, chan,rate,pwr,evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase, evm_list])
                print [chan,rate,pwr,evm,evm_std,evm_max,freq_err,clk_err,lo_leakage,iq_imb_amp,iq_imb_phase, evm_list]

        logsetlevel('D')
        rfglobal.iqv['evm_sorted'] = 0

    def tx_dig_gain_sweep(self, cable_lose=2, channel=[1], iqv_no=1,iqv_num=10):
        """
        :test TX power and EVM
        :cable_lost:
        :channle: it is matrix [1,...]
        :data_rate: it is matrix ['mcs0',...]
        :iqv_no: 1-left port, 2-right port
        :iqv_num: iqview average number
        """
        logsetlevel('I')

        title = 'pa_gain, bb_gain, dig_atten, channel, rate, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage(dB),iq_imb_amp(dB),iq_imb_phase(deg),evm_list\n'
        fname = self.wifi.get_filename('sweep_tx_gain', 'tx_dig_gain_sweep')
        csvreport1 = csvreport(fname, title)

        self.wifi.cmdstop()
        max_pwr = 25 - cable_lose

        self.wifi.txpacket(1, '54m', 0, 0)
        test_para = wifi_instrum.test_para('54m')
        myiqv=tester.tester(2412, max_pwr, '54m', test_para, iqv_no,'measure', cable_lose, 10, 1, 1,20)
        [pwr, freq_err, clk_err, evm, evm_std, evm_max, lo_leakage,iq_imb_amp,iq_imb_phase,evm_list] = wifi_instrum.iqv_avg(myiqv, 1,'false')

        max_pwr = pwr + 12
        print "max_pwr=%d"%max_pwr

        rate = 'mcs7'
        chan = channel[0]
        pa_gain_m = [0x1f]
        bb_gain_m = [0x100]

        for pa_gain in pa_gain_m:
            for bb_gain in bb_gain_m:
                for dig_atten in range(60,-40,-2):

                        cbw40m = self.wifi.rate2ht40(rate)

                        self.wifi.tx_rc_filter(0, 0, 0)
                        self.wifi.txp_force_gain(2412, rate, pa_gain, bb_gain, dig_atten)
                        self.wifi.txpacket(chan, rate, 0, cbw40m)

                        test_para = wifi_instrum.test_para(rate)
                        if chan<=14:
                            freq = self.wifi.chan2freq(chan)
                        else:
                            freq = chan

                        myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0, 1,20)
                        [pwr, freq_err, clk_err, evm, evm_std, evm_max,lo_leakage,iq_imb_amp,iq_imb_phase,evm_list] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false', -15)
                        loginfo("rate=%s, pa_gain=0x%x, bb_gain=0x%x, dig_atten=%d, channel=%d,power=%2.2f,evm=%2.2f"%(rate,pa_gain, bb_gain, dig_atten,chan,pwr, evm))
                        csvreport1.write_data([hex(pa_gain), hex(bb_gain), dig_atten,chan,rate,pwr,evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase, evm_list])
                        print [chan,rate,pwr,evm,evm_std,evm_max,freq_err,clk_err,lo_leakage,iq_imb_amp,iq_imb_phase, evm_list]

        logsetlevel('D')



    def tx_gain_table_sweep(self, cable_lose=2, channel=[1], iqv_no=1,iqv_num=10):
        """
        :test TX power and EVM
        :cable_lost:
        :channle: it is matrix [1,...]
        :data_rate: it is matrix ['mcs0',...]
        :iqv_no: 1-left port, 2-right port
        :iqv_num: iqview average number
        """
        logsetlevel('I')

        title = 'pa_gain, bb_gain, dig_atten, channel, rate, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage(dB),iq_imb_amp(dB),iq_imb_phase(deg),evm_list\n'
        fname = self.wifi.get_filename('sweep_tx_gain', 'tx_gain_table')
        csvreport1 = csvreport(fname, title)

        self.wifi.cmdstop()
        max_pwr = 25 - cable_lose

        self.wifi.txpacket(1, 'mcs7', 0, 0)
        test_para = wifi_instrum.test_para('54m')
        myiqv=tester.tester(2412, max_pwr, '54m', test_para, iqv_no,'measure', cable_lose, 10, 1, 1,20)
        [pwr, freq_err, clk_err, evm, evm_std, evm_max, lo_leakage,iq_imb_amp,iq_imb_phase,evm_list] = wifi_instrum.iqv_avg(myiqv, 1,'false')

        max_pwr = pwr + 12
        print "max_pwr=%d"%max_pwr

        rate = 'mcs7'
        chan = channel[0]
        pa_gain_m = [0xf,0x1f,0x2f,0x3f,0x4f,0x5f,0x6f,0x7f]

        bb_gain_m = [0x0,0x40,0x80,0xc0,0x100,0x140,0x20,0x60,0xa0,0xe0,0x120,0x160,0x30,0x70,0xb0]

        for pa_gain in pa_gain_m:
            for bb_gain in bb_gain_m:
                for dig_atten in range(24,-24,-4):

                        cbw40m = self.wifi.rate2ht40(rate)

                        self.wifi.tx_rc_filter(0, 0, 0)
                        self.wifi.txp_force_gain(2412, rate, pa_gain, bb_gain, dig_atten)
                        self.wifi.txpacket(chan, rate, 0, cbw40m)

                        test_para = wifi_instrum.test_para(rate)
                        if chan<=14:
                            freq = self.wifi.chan2freq(chan)
                        else:
                            freq = chan

                        myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0, 1,20)
                        [pwr, freq_err, clk_err, evm, evm_std, evm_max, lo_leakage,iq_imb_amp,iq_imb_phase,evm_list] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false', -15)
                        loginfo("rate=%s, pa_gain=0x%x, bb_gain=0x%x, dig_atten=%d, channel=%d,power=%2.2f,evm=%2.2f"%(rate,pa_gain, bb_gain, dig_atten,chan,pwr, evm))
                        csvreport1.write_data([hex(pa_gain), hex(bb_gain), dig_atten,chan,rate,pwr,evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase, evm_list])
                        print [chan,rate,pwr,evm,evm_std,evm_max,freq_err,clk_err,lo_leakage,iq_imb_amp,iq_imb_phase, evm_list]

        logsetlevel('D')


    def tx_gain_target_pwr_sweep(self, cable_lose=2, channel=[1], iqv_no=1,iqv_num=10):

        title = 'rftx,bbgain,dig_atten,channel,rate, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),evm_list\n'
        fname = self.wifi.get_filename('tx_gain_target_pwr_sweep', 'tx_gain_target_pwr_sweep')
        csvreport1 = csvreport(fname, title)

        rfglobal.iqv['evm_sorted'] = 1

        max_pwr = 25-cable_lose
        reset_flag = 0

        rate = 'mcs7'
        chan = channel[0]

##        target_pwr_m = [12,13,14,15,16,17,18,19,20]
        target_pwr_m = [8,9,10,11,12,13]
##        pa_gain_m =[0x1f,0x2f,0x3f,0x4f,0x5f,0x6f,0x7f]
##        pa_gain_m =[0x1e,0x2e,0x3e,0x4e,0x5e,0x6e,0x7e]
        pa_gain_m =[0x2e,0x3e,0x4e,0x5e]
##        bb_gain_m = [0x0,0x40,0x80,0xc0,0x100,0x140,0x20,0x60,0xa0,0xe0,0x120,0x160,0x30,0x70,0xb0,]
        bb_gain_m = [0x0,0x40,0x80,0xc0,0x100,0x140,0x20,0x60,0xa0,0xe0]
        dig_atten = 0
        #[0x10,0x20,0x30,0x40,0x50,0x60,0x70,0x71,0x72,0x73,0x74,0x78,0x7c]
##        pa_gain_m = [0xf,0x1f,0x2f,0x3f,0x4f,0x5f,0x6f,0x7f]
##        bb_gain_m = [0x0]
##        dig_atten = 16

        for target_pwr in target_pwr_m:
            if target_pwr >= 18:
                rate = 'mcs0'
            for pa_gain in pa_gain_m:
                for bb_gain in bb_gain_m:
                    w_str = self.force_gain_rf(cable_lose=cable_lose, chan=chan, rate=rate, target_power=target_pwr, rfgain=pa_gain, bbgain=bb_gain, dig_atten=dig_atten, max_pwr=max_pwr, num=iqv_num, iqv_no=iqv_no,reset_flag=reset_flag,target_pwr_dis=0,evm_list_en=1)
                    reset_flag = 1
                    csvreport1.write_data(list(w_str.split(",")))

        rfglobal.iqv['evm_sorted'] = 0


    def sweep_tx_gain_tone(self,cable_lose=2, target_pwr_dis=0,board_no=''):

        '''
        :brief:
            sweep PA gain and BB gain ,and use spectrum analyizer to test the tone power
        :param:
            - cable_lose    : the lose of cable
            - target_pwr_dis:
                            0 : disable the adjustment of the attentuation
                            1 : adjust the attentuation of tone to make the tone power reach a target value
            - board_no      : the number of test board
        :return:
            csv report
        '''

        title = 'freq,rftx,bbgian,SPA_pwr,sarpwr,power\n'
        fname = self.wifi.get_filename('sweep_tx_gain', 'Test_tx_gain_tone_%s'%(board_no))
        csvreport1 = csvreport(fname, title)

        freq_sweep = 2437
        tone_freq = 3
        target_tone = 13
        device_spa = "" #"E4404B","N9020A"

        if device_spa =="":
            SPA_Revise_Power = 1.87; #HP lose:1.87dB
            self.spa = HP('SA',cfreq=freq_sweep+tone_freq,rb=1,span=1,reflvl=20);#rb and span
        else:
            self.spa = Agilent('SA',cfreq=freq_sweep+tone_freq,rb=1,span=1,reflvl=20,device=device_spa);#rb and span
            SPA_Revise_Power = 0;
        self.spa.set_rb(30);

        self.rfpll.set_freq(freq_sweep,40)
        self.pbus.pbus_debugmode()
        self.pbus.open_tx()
        self.pbus.set_dco(256,256,256,256)

        for yy0 in range(0,len(rftx_lst)):
            for kk0 in range(0,len(bbgain_lst)):
                power_sweep = -50
                rfgain = rftx_lst[yy0]
                bbgain = bbgain_lst[kk0]
                self.pbus.pbus_wr('rftx2','en1',rfgain);# Set Filter Gain
                self.pbus.pbus_wr('bb','en2',bbgain);# Set PA Gain
                self.rfcal.tos()
                self.mem.wrm(0x600060a0, 17, 16, 3) #force tx on
                tt_max = 5
                if target_pwr_dis == 1:
                    tt_min = tt_max - 1
                else:
                    tt_min = 0
                for tt in range(tt_min,tt_max):
                    self.wifi.txtone(1, tone_freq, power_sweep)
                    time.sleep(1)
                    SPA_pwr = self.spa.get_result('PEAK')[1]+SPA_Revise_Power+cable_lose
                    sarpwr= self.saradc.sar_dout(8, signal='tone', pwr_dis=0);
                    self.wifi.txtone(0, tone_freq, power_sweep)
                    if tt < (tt_max-1):
                        power_sweep += int((target_tone-SPA_pwr)*4)

                csvreport1.write_data([(freq_sweep+tone_freq),hex(rfgain),bbgain,SPA_pwr,sarpwr,power_sweep])



    def fixed_gain_matching(self,cable_lose=2, channel=[1], data_rate=['mcs7'],target_pwr_dis_m =[1,0], iqv_num=10, iqv_no=2, board_no='',recal=0):
        """
        :brief:
            test tx performance at fixed gian, pa_gain=0x5f, bb_gain=0x120
        :param:
            - cable_lose    : the lose of cable
            - channel       : 1~14
            - data_rate     : high data rate for EVM ,low data rate for mask
            - iqv_num           : user-defined
            - target_pwr_dis:
                            0 : disable the adjustment of the digital gain
                            1 : adjust the digital gain to make the packet power reach a target value
            - iqv_no        : 1 - left ; 2- right
            - board_no      : the number of test board
        :return:
            csv report
        """
        title = 'rftx,bbgain,dig_atten,pll_cap_org,better_ir_cap,channel,rate, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),iq_gain,iq_phase,evm_list\n'
        fname = self.wifi.get_filename('sweep_tx_gain', 'Fixed_tx_gain_EVM_%s'%(board_no),'tx_matching')
        csvreport1 = csvreport(fname, title)
        rfglobal.iqv['evm_sorted'] =1

        if self.chipv == "CHIP723" or self.chipv == "CHIP724" :
            target_power ={
                "mcs7": 13 ,
                "54m": 15,
                "mcs0": 18,
                "6m":18,
                '11m':19.5,
                "1m":19.5,
                "mcs0_40": 18,
                "mcs7_40":13.5
            }
        else:
            target_power ={
                "mcs7": 13.5 ,
                "54m": 15,
                "mcs0": 18,
                "6m":18,
                '11m':19.5,
                "1m":19.5,
                "mcs0_40": 18,
                "mcs7_40":13
            }

        max_pwr = 25-cable_lose
        reset_flag = 0
        dig_gain = {

        "mcs0": -8 ,
        "mcs1": -8 ,
        "mcs2": -8 ,
        "mcs3": -2 ,
        "mcs4": -2 ,
        "mcs5":  4 ,
        "mcs6":  6 ,
        "mcs7": 12 ,
        "mcs0_40": -8 ,
        "mcs1_40": -6 ,
        "mcs2_40": -6 ,
        "mcs3_40": -2 ,
        "mcs4_40": -2 ,
        "mcs5_40":  4 ,
        "mcs6_40":  8 ,
        "mcs7_40": 10 ,
        "6m":  -8,
        "9m":  -6,
        "12m": -6,
        "18m": -6,
        "24m": -2,
        "36m": -2,
        "48m": 4,
        "54m": 6,
        "1m": -18 ,
        "2m": -18 ,
        "5.5m": -18,
        "11m":-18
        }
        if self.chipv =="CHIP724":
            rfgain=0x5e
            bbgain=0x20
        elif self.chipv =="CHIP723":
            rfgain=0x5e
            bbgain=0xa0
        elif self.chipv =="CHIP722":
            rfgain=0x5f
            bbgain=0xa0
        else:
            rfgain=0x5f
            bbgain=0x120

        w_str_t = ''

##        case = 0
##
##        if case == 0:
##            self.wifi.i2c_wic('rftx','PA2G_ICT_STG0_CGM',2),
##            self.wifi.i2c_wic('rftx','PA2G_ICT_STG1',8),
##            self.wifi.i2c_wic('rftx','PA2G_ICT_STG1_CGM',10),
##            self.wifi.i2c_wic('rftx','PA2G_ICT_STG2',10),
##        if case == 1:
##            self.wifi.i2c_wic('rftx','PA2G_ICT_STG0_CGM',2),
##            self.wifi.i2c_wic('rftx','PA2G_ICT_STG1',8),
##            self.wifi.i2c_wic('rftx','PA2G_ICT_STG1_CGM',10),
##            self.wifi.i2c_wic('rftx','PA2G_ICT_STG2',4),
##        elif case == 2:
##            self.wifi.i2c_wic('rftx','PA2G_ICT_STG0_CGM',1),
##            self.wifi.i2c_wic('rftx','PA2G_ICT_STG1',8),
##            self.wifi.i2c_wic('rftx','PA2G_ICT_STG1_CGM',12),
##            self.wifi.i2c_wic('rftx','PA2G_ICT_STG2',10),
##        elif case == 3:
##            self.wifi.i2c_wic('rftx','PA2G_ICT_STG0_CGM',1),
##            self.wifi.i2c_wic('rftx','PA2G_ICT_STG1',8),
##            self.wifi.i2c_wic('rftx','PA2G_ICT_STG1_CGM',12),
##            self.wifi.i2c_wic('rftx','PA2G_ICT_STG2',4),


        for chan in channel:
            for rate in data_rate:
                for target_pwr_dis in target_pwr_dis_m:

##                    self.wifi.txiq_set(1,0,-9)
                    if recal==0:
                        w_str = self.force_gain_rf(cable_lose=cable_lose, chan=chan, rate=rate, target_power=target_power[rate], rfgain=rfgain, bbgain=bbgain, dig_atten=dig_gain[rate], max_pwr=max_pwr, num=iqv_num, iqv_no=iqv_no,reset_flag=reset_flag,target_pwr_dis=target_pwr_dis,evm_list_en=1)
                    else:
                        w_str = self.force_gain_rf_rfpll_cal(cable_lose=cable_lose, chan=chan, rate=rate, target_power=target_power[rate], rfgain=rfgain, bbgain=bbgain, dig_atten=dig_gain[rate], max_pwr=max_pwr, num=iqv_num, iqv_no=iqv_no,reset_flag=reset_flag,target_pwr_dis=target_pwr_dis,evm_list_en=1)

                    reset_flag = 1
##                    a1 = self.wifi.i2c_ric('rftx','PA2G_ICT_STG0_CGM'),
##                    b1 = self.wifi.i2c_ric('rftx','PA2G_ICT_STG1'),
##                    c1 = self.wifi.i2c_ric('rftx','PA2G_ICT_STG1_CGM'),
##                    d1 = self.wifi.i2c_ric('rftx','PA2G_ICT_STG2'),

                    csvreport1.write_data(list(w_str.split(","))) #+[a1,b1,c1,d1]))

        rfglobal.iqv['evm_sorted'] = 0

    def fix_gain_rate_sweep(self,cable_lose=2, channel=[1], data_rate=['mcs7'], iqv_num=10, target_pwr_dis=0,iqv_no=2, board_no=''):
        """
        :brief:
            sweep PA gain and BB gain with adjusting digital gain to reach a target power ,and use WIFI Insturment to
            test EVM or mask, find the gain combination which satisfy EVM and mask
        :param:
            - cable_lose    : the lose of cable
            - channel       : 1~14
            - data_rate     : high data rate for EVM ,low data rate for mask
            - num           : user-defined
            - target_pwr_dis:
                            0 : disable the adjustment of the digital gain
                            1 : adjust the digital gain to make the packet power reach a target value
            - iqv_no        : 1 - left ; 2- right
            - board_no      : the number of test board
        :return:
            csv report
       """
        logsetlevel('I')

        title = 'pa_gain, bb_gain, dig_atten,channel, rate, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage(dB),iq_imb_amp(dB),iq_imb_phase(deg),evm_list\n'
        fname = self.wifi.get_filename('sweep_tx_gain', 'fix_gain_rate_sweep%s'%board_no)
        csvreport1 = csvreport(fname, title)

        self.wifi.cmdstop()
        max_pwr = 25 - cable_lose

        self.wifi.txpacket(1, '54m', 0, 0)
        test_para = wifi_instrum.test_para('54m')
        myiqv=tester.tester(2412, max_pwr, '54m', test_para, iqv_no,'measure', cable_lose, 10, 1, 1)
        [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 1,'false')

        max_pwr = pwr + 12
        print "max_pwr=%d"%max_pwr

        dig_gain = {
        "mcs0": -6 ,
        "mcs1": -6 ,
        "mcs2": -6 ,
        "mcs3": -2 ,
        "mcs4": -2 ,
        "mcs5":  4 ,
        "mcs6":  8 ,
        "mcs7": 12 ,
        "mcs0_40": -6 ,
        "mcs1_40": -6 ,
        "mcs2_40": -6 ,
        "mcs3_40": -2 ,
        "mcs4_40": -2 ,
        "mcs5_40":  4 ,
        "mcs6_40":  8 ,
        "mcs7_40": 12 ,
        "6m":  -6,
        "9m":  -6,
        "12m": -6,
        "18m": -6,
        "24m": -2,
        "36m": -2,
        "48m": 4,
        "54m": 8,
        "1m": -16 ,
        "2m": -16 ,
        "5.5m": -16,
        "11m":-16
}
        if self.chipv == 'CHIP724':
            pa_gain = 0x4e
            bb_gain = 0xa0
        else:
            pa_gain = 0x5f
            bb_gain = 0x20

        reset_flag = 0

        for rate in data_rate:
            for chan in channel:

                cbw40m = self.wifi.rate2ht40(rate)
                self.wifi.tx_rc_filter(0, 0, 0)
                result = self.wifiapi.set_tx_gain(pa_gain, bb_gain)


                dig_atten = dig_gain[rate]
                self.wifi.txp_force_gain(2412, rate, pa_gain, bb_gain, dig_atten)
                self.wifi.txpacket(chan, rate, 0, cbw40m)
##                self.wifi.txout_new(txchan=chan,rate_sym=rate,PackNum=0,time_us=500,duty=0.5,backoff_qdb=0) ## For Current Test

                test_para = wifi_instrum.test_para(rate)
                if chan<=14:
                    freq = self.wifi.chan2freq(chan)
                else:
                    freq = chan

                myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0, 1)
                [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false', -15)
                loginfo("rate=%s, pa_gain=0x%x, bb_gain=0x%x, dig_atten=%d, channel=%d,power=%2.2f,evm=%2.2f"%(rate,pa_gain, bb_gain, dig_atten,chan,pwr, evm))
                csvreport1.write_data([hex(pa_gain), hex(bb_gain), dig_atten, chan,rate,pwr,evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase, evm_list])
                print [chan,rate,pwr,evm,evm_std,evm_max,freq_err,clk_err,lo_leakage,iq_imb_amp,iq_imb_phase, evm_list]

        logsetlevel('D')

    def force_gain_rf_rfpll_cal(self,cable_lose=2, chan=1, rate = 'mcs7',target_power = 13, rfgain = 0x5f, bbgain = 0x120, dig_atten = 12, max_pwr=25,  num=10, iqv_no=2,reset_flag=0, target_pwr_dis=0, evm_list_en=0):
        '''
        :brief:
            test tx performance at fixed gian
        '''
        rfglobal.iqv['evm_sorted'] =1
        if chan<=14:
            freq = self.wifi.chan2freq(chan)
        else:
            freq = chan
        iqv_num = 1
        tt_max = 3
        if target_pwr_dis == 1:
            tt_min = tt_max -1
        else:
            tt_min = 0
        for tt in range(tt_min,tt_max):
            if tt == (tt_max -1):
                iqv_num = num
            logdebug('dig_atten=%d'%dig_atten)
            self.wifi.cmdstop()
            cbw40m = self.wifi.rate2ht40(rate)
            [tx_gain,tx_phase]= self.rfcal.txiq_cal(cable_lose,iqv_no)
            self.wifiapi.cmdstop()
            cbw40m = self.wifi.rate2ht40(rate)
            self.wifiapi.rfchsel(chan,cbw40m)
            if cbw40m == 1:
                self.wifi.i2c.bbtop.filter_wftx0_dcap_lq=15
                self.wifi.i2c.bbtop.filter_wftx0_dcap_hq=15
            self.wifiapi.set_tx_gain(rfgain, bbgain)
            self.wifiapi.set_tx_dig_gain(1,(256-dig_atten)) #256-bk
            self.wifi.txiq_set(1,tx_gain,tx_phase)
            self.wifi.i2c.rftx.PA2G_CCT_STG1=11
            pll_cap_org = self.wifi.i2c.rfpll.ir_cap_ext
            ir_enx_cap = self.wifi.i2c.rfpll.ir_enx_cap
            print "default_cap=%d"%pll_cap_org
            better_ir_cap =0
            better_cap_find=0
            [len_byte, delay] = self.wifi.get_length_delay_duty(rate,0.2)
            myiqv=tester.tester(freq, max_pwr, rate, wifi_instrum.test_para(rate), iqv_no,'measure', cable_lose, 10, 0, 0)
            for cap_ext in range(pll_cap_org-4, pll_cap_org+8):
                self.wifi.i2c.rfpll.ir_cap_ext = cap_ext

                for i in range(0,1):
                    self.wifi.txout(rate, 0, PackLen=len_byte, backoff_qdb=0, frm_delay=delay)

                    [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 1,'false', -15)
                    if evm < -5:
                        [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false', -15)

                    ir_cap_ext = self.wifi.i2c.rfpll.ir_cap_ext
                    or_pll_cap = self.wifi.i2c.rfpll.or_pll_cap
                    or_capl = self.wifi.i2c.rfpll.or_capl
                    or_caph = self.wifi.i2c.rfpll.or_caph
                    sar2_code = self.wifiapi.get_pll_vol()
                    vco_bias_vol = 0
                    vco_bias_dm = 0
##                    sar2_code_lst.append(sar2_code)
                    if better_cap_find==0:
                        if sar2_code >=7500:

                            better_ir_cap=cap_ext-1
                            better_cap_find =1
                        else:
                            better_ir_cap=cap_ext
                            better_cap_find=0

            self.wifi.i2c.rfpll.ir_cap_ext =better_ir_cap

            time.sleep(0.2)
##            self.best_register_wr()
            [len_byte, delay] = self.wifi.get_length_delay_duty(rate,0.2)
            self.wifi.txout(rate_sym=rate, PackNum=0, PackLen =len_byte, cbw40=cbw40m, ht_dup=0, backoff_qdb=0, frm_delay=delay)
##            self.wifi.txpacket(chan, rate, 0, cbw40m)

            if reset_flag == 0:
                myiqv = tester.tester(freq, max_pwr, rate, wifi_instrum.test_para(rate), iqv_no,'measure', cable_lose, 10, 1,0,20)
                reset_flag = 1
            else:
                myiqv = tester.tester(freq, max_pwr, rate, wifi_instrum.test_para(rate), iqv_no,'measure', cable_lose, 10, 0,0,20)

            wifi_instrum.iqv_avg(myiqv, iqv_num,'false')
            if rate in('1m','11m'):
                [freq_mask,marg] = wifi_instrum.spectrum_mask_flatness(myiqv, iqv_num, 3)
            elif rate in ('6m','mcs0','mcs0_40'):
                [freq_mask,marg] = wifi_instrum.spectrum_mask_flatness(myiqv, iqv_num, 99)
            self.wifi.cmdstop()
            iqv = rfglobal.iqv
            evm = iqv['evm_raw']
            evm_std = iqv['evm_std']
            evm_max = iqv['evm_max']
            pwr = iqv['pwr']
            freq_err = iqv['freq_err']
            clk_err = iqv['clk_err']
            iq_imb_amp = iqv['iqamp']
            iq_imb_phase = iqv ['iqphase']
            if tt < (tt_max - 1):
                dig_atten += (pwr - target_power)*4

        w_str = ''
        w_str += "%s, 0x%x ,%d, %d,%d,%d,%s,%2.2f,%2.2f,%2.2f,%2.2f,%2.2f,%2.2f,%2.2f,%2.2f,"%(hex(rfgain),bbgain,dig_atten,pll_cap_org,better_ir_cap,freq,str(rate),pwr,evm,evm_std,evm_max,freq_err,clk_err,iq_imb_amp,iq_imb_phase)
        if evm_list_en == 1:
            for evm_i in iqv['evm_list']:
                w_str += '%s,'%(evm_i)
        if rate in('1m','2m','5.5m''11m','6m','9m','12m','18m','mcs0','mcs0_40','mcs1','mcs2','mcs1_40','mcs2_40'):
            for n in range(0,8):
                w_str += '%s'%freq_mask[n]+','+'%s'%marg[n]+','
        print hex(rfgain),hex(bbgain),dig_atten,pll_cap_org,better_ir_cap,chan,str(rate),pwr,evm,evm_std,evm_max,freq_err,clk_err
        return w_str
        rfglobal.iqv['evm_sorted'] =0


    def force_gain_rf(self,cable_lose=2, chan=1, rate = 'mcs7',target_power = 13, rfgain = 0x5f, bbgain = 0x120, dig_atten = 12, max_pwr=25,  num=10, iqv_no=2,reset_flag=0, target_pwr_dis=0, evm_list_en=0):
        '''
        :brief:
            test tx performance at fixed gian
        '''
        rfglobal.iqv['evm_sorted'] =1
        if chan<=14:
            freq = self.wifi.chan2freq(chan)
        else:
            freq = chan
        iqv_num = 1
        tt_max = 3
        if target_pwr_dis == 1:
            tt_min = tt_max -1
        else:
            tt_min = 0
        for tt in range(tt_min,tt_max):
            if tt == (tt_max -1):
                iqv_num = num
            logdebug('dig_atten=%d'%dig_atten)
            self.wifi.cmdstop()
            cbw40m = self.wifi.rate2ht40(rate)

            if self.chipv=="CHIP724":
##                [txiq_gain,txiq_phase] = self.rfcal.txiq_cal(cable_lose,iqv_no)
                self.wifiapi.rfchsel(chan,cbw40m)
                self.wifiapi.set_tx_gain(rfgain, bbgain)
                self.wifiapi.set_tx_dig_gain(1,(256-dig_atten)) #256-bk
##                self.wifi.txiq_set(1,txiq_gain,txiq_phase)
##                self.best_register_wr()


            else:
                self.wifi.txp_force_gain(chan,rate,rfgain,bbgain,int(dig_atten))
            time.sleep(0.2)

            [len_byte, delay] = self.wifi.get_length_delay_duty(rate,0.2)
            self.wifi.txout(rate_sym=rate, PackNum=0, PackLen =len_byte, cbw40=cbw40m, ht_dup=0, backoff_qdb=0, frm_delay=delay)
##            self.wifi.txpacket(chan, rate, 0, cbw40m)

            if reset_flag == 0:
                myiqv = tester.tester(freq, max_pwr, rate, wifi_instrum.test_para(rate), iqv_no,'measure', cable_lose, 10, 1,0,20)
                reset_flag = 1
            else:
                myiqv = tester.tester(freq, max_pwr, rate, wifi_instrum.test_para(rate), iqv_no,'measure', cable_lose, 10, 0,0,20)

            wifi_instrum.iqv_avg(myiqv, iqv_num,'false')
            if rate in('1m','11m'):
                [freq_mask,marg] = wifi_instrum.spectrum_mask_flatness(myiqv, iqv_num, 3)
            elif rate in ('6m','mcs0','mcs0_40'):
                [freq_mask,marg] = wifi_instrum.spectrum_mask_flatness(myiqv, iqv_num, 99)
            self.wifi.cmdstop()
            iqv = rfglobal.iqv
            evm = iqv['evm_raw']
            evm_std = iqv['evm_std']
            evm_max = iqv['evm_max']
            pwr = iqv['pwr']
            freq_err = iqv['freq_err']
            clk_err = iqv['clk_err']
            iq_imb_amp = iqv['iqamp']
            iq_imb_phase = iqv ['iqphase']
            if tt < (tt_max - 1):
                dig_atten += (pwr - target_power)*4

        w_str = ''
        w_str += "%s, 0x%x ,%d, %d,%d,%d,%s,%2.2f,%2.2f,%2.2f,%2.2f,%2.2f,%2.2f,%2.2f,%2.2f,"%(hex(rfgain),bbgain,dig_atten,1,1,freq,str(rate),pwr,evm,evm_std,evm_max,freq_err,clk_err,iq_imb_amp,iq_imb_phase)
        if evm_list_en == 1:
            for evm_i in iqv['evm_list']:
                w_str += '%s,'%(evm_i)
        if rate in('1m','2m','5.5m''11m','6m','9m','12m','18m','mcs0','mcs0_40','mcs1','mcs2','mcs1_40','mcs2_40'):
            for n in range(0,8):
                w_str += '%s'%freq_mask[n]+','+'%s'%marg[n]+','
        print hex(rfgain),hex(bbgain),dig_atten,chan,str(rate),pwr,evm,evm_std,evm_max,freq_err,clk_err
        print self.wifi.i2c.rfpll.ir_cap_ext
        return w_str


    def best_register_wr(self):
##        self.wifi.i2c.rfpll.ir_en_pll_mon=0  #1
##        self.wifi.i2c.rfpll.ir_sel_fcnt_cal=0 #0
##        self.wifi.i2c.rfpll.ir_ext_dchgp=4 #7
##        self.wifi.i2c.rfpll.enb_open_lf=1#0
##        self.wifi.i2c.rfpll.dlref=3 #3
##        self.wifi.i2c.rfpll.dhref=3 #3
##        self.wifi.i2c.rfpll.bst_sf=0 #0
##        self.wifi.i2c.rfpll.ir_acal_delay=0 #8
##        self.wifi.i2c.bias_marlin3.cgm_bias=3#2
##        self.wifi.i2c.bias_marlin3.dres12k=2#7
##        self.wifi.i2c.bias_marlin3.rc_dvref=3#2
##        self.wifi.i2c.rfpll.ir_dac_ext = 8
##        self.wifiapi.pll_vol_cal()
##        self.wifi.i2c.rftx.PA2G_ICT_STG1=8 # 8
##        self.wifi.i2c.rftx.TMX2G_CCT_LOAD=11
##        self.wifi.i2c.rftx.PA2G_CCT_STG1=11
##        self.wifi.i2c.rftx.PA2G_CCT_STG2=11
##        self.wifi.i2c.rfpll.lf_hbw=1 #1
        self.wifi.i2c.bias.dref2p2=0
  ##        self.wifi.i2c.bias.cp1p2_reg=7
##        self.wifi.i2c.rftx.PA2G_ICT_STG0=8 #default 8  6
##        self.wifi.i2c.rftx.PA2G_ICT_STG0_CGM=2   #default 2 better 7
####        self.wifi.i2c.rftx.PA2G_ICT_STG1=8  #deafult 8
##        self.wifi.i2c.rftx.PA2G_ICT_STG2=10  #deafult 10 better 0
####        self.wifi.i2c.rftx.PA2G_VCT_CSC_STG0=10 #default 10 better 8
####        self.wifi.i2c.rftx.PA2G_VCT_CSC_STG1=4 #default 4 better 5
####        self.wifi.i2c.rftx.PA2G_VCT_CSC_STG2=7 #default 10
##        self.wifi.i2c.rfpll.or_dvco_kvco=0             # default 0, better 3
##        self.wifi.i2c.rfpll.bst_sf = 0
##        self.wifi.i2c.rfpll.ir_amplf_open=7 #default 7, better 0
##        self.wifi.i2c.rfpll.ir_amplf_close=0
##        self.wifi.i2c.rftx.LB_GCT=0

    def flash_test(self,cable_lose=33,iqv_no=2,clk=[1,2,4],div=[0,1,2,3]):
        for ck in clk:
            for dv in div:
                loginfo(("ck=%d,dv=%d")%(ck,dv))
                self.wifiapi.flash_test_init(ck,dv)
                self.sweep_tx_gain_EVM(cable_lose=cable_lose, channel=[1,2,3,4,5,6,7,8,9,10,11,12,13,14], data_rate=['mcs7'], num=10, target_pwr_dis=1,iqv_no=iqv_no, board_no='')
        self.wifiapi.flash_test_enable(0)
        self.sweep_tx_gain_EVM(cable_lose=cable_lose, channel=[1,2,3,4,5,6,7,8,9,10,11,12,13,14], data_rate=['mcs7'], num=10, target_pwr_dis=1,iqv_no=iqv_no, board_no='')