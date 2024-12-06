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

class WIFI_TXRX_TEST(object):

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


    def get_rf_param(self, rf_setting='', instr=''):
        num = 0
        for name in rf_setting[0]:
            if name == instr:
                break
            num += 1

        param = []
        for rf_set in rf_setting:
            if rf_set[num] != instr and rf_set[num] != '':
                try:
                    param.append(int(rf_set[num],10))
                except:
                    param.append(rf_set[num])
        return param


    def get_rf_setting(self):
        """
        :load wifi setting file
        """
        data_path = "./rftest/test_script/"
        rf_setting_file = data_path+'wifi_test_setting.xlsx'
        info = iofunc.csv2dict(rf_setting_file, sheet='Test Info')
        temperature = info['Temperature']
        cable_lose = int(info['Cable loss'], 10)
        unit_no = int(info['Equipment Port'], 10)
        print 'cable_lose=%d, unit_no=%d, temperature=%s'%(cable_lose, unit_no, temperature)

        rf_setting = iofunc.csv2data(rf_setting_file, sheet='Test Setting',comment='#%')

        tx_channel = self.get_rf_param(rf_setting, instr='tx_channel')
        tx_rate = self.get_rf_param(rf_setting, instr='tx_rate')
        rx_channel = self.get_rf_param(rf_setting, instr='rx_channel')
        rx_rate = self.get_rf_param(rf_setting, instr='rx_rate')
        rxm_channel = self.get_rf_param(rf_setting, instr='rxm_channel')
        rxm_rate = self.get_rf_param(rf_setting, instr='rxm_rate')
        rxd_channel = self.get_rf_param(rf_setting, instr='rxd_channel')
        rxd_rate = self.get_rf_param(rf_setting, instr='rxd_rate')
        rxd_range = self.get_rf_param(rf_setting, instr='rxd_range')

        return [cable_lose, unit_no, temperature, tx_channel, tx_rate, rx_channel, rx_rate, rxm_channel, rxm_rate, rxd_channel, rxd_rate, rxd_range]

    def rc_txdc_cal(self, cable_lose=2, iqv_no=2,num=12):
        logsetlevel('E')
        rate = '11m'
        self.wifi.rfchsel(1)
        test_para = wifi_instrum.test_para(rate)
        myiqv=tester.tester(2412, 5, rate, test_para, iqv_no,'measure', cable_lose, 10, 1, 0)

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
                    self.wifi.txp_force_gain(2412, rate, 0xf, 0x30, 0)  ##max_power=5
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


    def rfpll_cap_test(self, cable_lose=2, iqv_no=1,iqv_num=10,name_str=''):
        """
        :test TX power and EVM
        :cable_lost:
        :channle: it is matrix [1,...]
        :data_rate: it is matrix ['mcs0',...]
        :iqv_no: 1-left port, 2-right port
        :iqv_num: iqview average number
        """
        logsetlevel('I')
        filetime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()));
        title = 'pa_gain, bb_gain, dig_atten,txdci,txdcq,txdci_f,txdcq_f,channel,rate, power, ir_enx_cap,ir_cap_ext,or_pll_cap,pll_dtest_code, pll_dtest_vol, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage(dB),iq_imb_amp(dB),iq_imb_phase(deg),evm_list\n'
        fname = self.wifi.get_filename('rfpll_cap_evm_test', 'rfpll_cap_evm_test_%s'%name_str)
        csvreport1 = csvreport(fname, title)

        self.wifi.cmdstop()
        max_pwr = 25 - cable_lose
##        self.wifi.txpacket(1, '54m', 0, 0)
##        test_para = wifi_instrum.test_para('54m')
##        myiqv=tester.tester(2412, max_pwr, '54m', test_para, iqv_no,'measure', cable_lose, 10, 1, 1)
##        [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 1,'false')
##        print [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase]
##
##        max_pwr = pwr + 12
##        print "max_pwr=%d"%max_pwr

        rate = '54m'
##        self.rfpll.pll_cap_cal_init()

        base = BasicTest(self.comport,self.chipv)

        pa_gain = 0x5f
        bb_gain = 0x20
        self.wifiapi.set_tx_gain(pa_gain, bb_gain)

        self.wifi.force_txon(1)
        [rfrx1, rftx1, rftx2, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2] = self.pbus.all_pbus()
        self.wifi.force_txon(0)

        target_power = 10
        self.wifi.rfchsel(1, 0)
        self.wifi.txp_force_gain(2412, rate, pa_gain, bb_gain, 8)
        evm = -30
        for chan in range(1,4):
##            print kk
##            chan = 1
            cbw40m = self.wifi.rate2ht40(rate)
            test_para = wifi_instrum.test_para(rate)
            if chan<=14:
                freq = self.wifi.chan2freq(chan)
            else:
                freq = chan

            dig_atten = 8

##            if(evm<-28):
            self.wifi.rfchsel(chan, cbw40m)
##                print 'set chan %2.2f'%evm
##            if(evm<-28):
##            self.wifi.txp_force_gain(2412, rate, pa_gain, bb_gain, dig_atten)
##            else:
            self.wifi.txout(rate)
            myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0, 1)

##            for i in range(0,1):
####                if(evm<-28):
####                    self.wifi.txp_force_gain(2412, rate, pa_gain, bb_gain, dig_atten)
####                else:
##                self.wifi.txout(rate)
##                [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 1,'false', -15)
##                sub_pwr = pwr - target_power
##                delta = int(sub_pwr*4)
##                print [i, dig_atten, pwr, sub_pwr, evm]
##
##                if sub_pwr>0.5:
##                    dig_atten += delta
##                    if dig_atten > 24:
##                        dig_atten = 24
##                        break
##                elif sub_pwr<-0.5:
##                    dig_atten += delta
##                    if dig_atten < 0:
##                        dig_atten = 0
##                        break
##                else:
##                    break

            pll_cap_org = self.i2c.rfpll.ir_cap_ext
            ir_enx_cap = self.i2c.rfpll.ir_enx_cap
            for cap_ext in range(pll_cap_org-3, pll_cap_org+5):
                self.i2c.rfpll.ir_cap_ext = cap_ext

                [pll_dtest_code, pll_dtest_vol] = self.rfpll.get_pll_vol()
                or_pll_cap = self.i2c.rfpll.or_pll_cap

##                if(evm<-28):
##                    self.wifi.txp_force_gain(2412, rate, pa_gain, bb_gain, dig_atten)
##                else:
                self.wifi.txout(rate)
                [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false', -15)
                ir_cap_ext = self.i2c.rfpll.ir_cap_ext
                csvreport1.write_data([hex(rftx2), hex(bb2), dig_atten, dcoi1, dcoq1, dcoi2, dcoq2, chan, rate,pwr, ir_enx_cap,ir_cap_ext,or_pll_cap,pll_dtest_code, pll_dtest_vol,evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase, evm_list])
                print [chan,ir_enx_cap,ir_cap_ext,or_pll_cap,pll_dtest_code, pll_dtest_vol, rate,pwr,evm,evm_std,evm_max]
##                if pll_dtest_vol>1.3:
##                    break

##            base.i2c_table_read("%d_%s"%(kk,filetime))

        logsetlevel('D')


    def tx_gain_fast_test(self, cable_lose=2, channel=[1], iqv_no=1,iqv_num=10,name_str=''):
        """
        :test TX power and EVM
        :cable_lost:
        :channle: it is matrix [1,...]
        :data_rate: it is matrix ['mcs0',...]
        :iqv_no: 1-left port, 2-right port
        :iqv_num: iqview average number
        """
        logsetlevel('I')

        title = 'pa_gain, bb_gain, dig_atten, txdci,txdcq,txdci_f,txdcq_f,channel, rate, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage(dB),iq_imb_amp(dB),iq_imb_phase(deg),evm_list\n'
        fname = self.wifi.get_filename('tx_gain_fast_test', 'tx_gain_fast_test_%s'%name_str)
        csvreport1 = csvreport(fname, title)

        self.wifi.cmdstop()
        max_pwr = 25 - cable_lose

        self.wifi.txpacket(1, '54m', 0, 0)
        test_para = wifi_instrum.test_para('54m')
        myiqv=tester.tester(2412, max_pwr, '54m', test_para, iqv_no,'measure', cable_lose, 10, 1, 1)
        [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 1,'false')

        max_pwr = pwr + 12
        print "max_pwr=%d"%max_pwr

        rate = '54m'
        chan = channel[0]
        pa_gain_m = [0x0,0x1,0x3,0x7,0xf,0x1f,0x2f,0x3f,0x5f,0x7f]
        bb_gain_m = [0,0x80,0x100,0x20,0xa0,0x120,0x30]
        dig_atten = 12

        for i in range(0,2):
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

                myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0, 1)
                [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false', -15)
                loginfo("rate=%s, pa_gain=0x%x, bb_gain=0x%x, dig_atten=%d, channel=%d,power=%2.2f,evm=%2.2f"%(rate,pa_gain, bb_gain, dig_atten,chan,pwr, evm))
                csvreport1.write_data([hex(pa_gain), hex(bb_gain), dig_atten, txdco, chan,rate,pwr,evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase, evm_list])
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
        fname = self.wifi.get_filename('tx_gain_table', 'tx_gain_table')
        csvreport1 = csvreport(fname, title)

        self.wifi.cmdstop()
        max_pwr = 25 - cable_lose

        self.wifi.txpacket(1, '54m', 0, 0)
        test_para = wifi_instrum.test_para('54m')
        myiqv=tester.tester(2412, max_pwr, '54m', test_para, iqv_no,'measure', cable_lose, 10, 1, 1)
        [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 1,'false')

        max_pwr = pwr + 12
        print "max_pwr=%d"%max_pwr

        rate = '54m'
        chan = channel[0]
        pa_gain_m = [0x1f,0x2f,0x3f,0x5f,0x7f]

        bb_gain_m = [0,0x80,0x100,0x20,0xa0,0x120,0x30]

        for pa_gain in pa_gain_m:
            for bb_gain in bb_gain_m:
                for dig_atten in range(28,-24,-4):

                        cbw40m = self.wifi.rate2ht40(rate)

                        self.wifi.tx_rc_filter(0, 0, 0)
                        self.wifi.txp_force_gain(2412, rate, pa_gain, bb_gain, dig_atten)
                        self.wifi.txpacket(chan, rate, 0, cbw40m)

                        test_para = wifi_instrum.test_para(rate)
                        if chan<=14:
                            freq = self.wifi.chan2freq(chan)
                        else:
                            freq = chan

                        myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0, 1)
                        [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false', -15)
                        loginfo("rate=%s, pa_gain=0x%x, bb_gain=0x%x, dig_atten=%d, channel=%d,power=%2.2f,evm=%2.2f"%(rate,pa_gain, bb_gain, dig_atten,chan,pwr, evm))
                        csvreport1.write_data([hex(pa_gain), hex(bb_gain), dig_atten,chan,rate,pwr,evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase, evm_list])
                        print [chan,rate,pwr,evm,evm_std,evm_max,freq_err,clk_err,lo_leakage,iq_imb_amp,iq_imb_phase, evm_list]

        logsetlevel('D')



    def tx_gain_evm(self, cable_lose=2, channel=[1,14], iqv_no=1,iqv_num=10, rc_en=0,name_str=""):
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
        fname = self.wifi.get_filename('wifi_txrx_test', 'TX_%S'%name_str)
        csvreport1 = csvreport(fname, title)

        self.wifi.cmdstop()
        max_pwr = 25 - cable_lose

        self.wifi.txpacket(1, '54m', 0, 0)
        test_para = wifi_instrum.test_para('54m')
        myiqv=tester.tester(2412, max_pwr, '54m', test_para, iqv_no,'measure', cable_lose, 10, 1, 1)
        [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 1,'false')

        max_pwr = pwr + 12
        print "max_pwr=%d"%max_pwr

        rate = '54m'
        pa_gain_m = [0xf] #,0xf,0x1f,0x2f,0x3f,0x4f,0x5f,0x6f,0x7f]
        if rc_en==0:
            filt_gain_m = [0,0x80,0x100,0x20,0xa0,0x120,0x1a0,0x30]
            [txdci, txdcq] = [0, 0]
        else:
            filt_gain_m = [0]
            [txdci, txdcq] = self.rc_txdc_cal(cable_lose, iqv_no,num=12)

        dig_atten_m = [24,20,16,8,4,0,-4,-8,-12,-16,-20,-24]

        for pa_gain in pa_gain_m:
            for filt_gain in filt_gain_m:
                for dig_atten in dig_atten_m:
                    for chan in channel:
                        self.wifi.cmdstop()
                        cbw40m = self.wifi.rate2ht40(rate)

                        self.wifi.tx_rc_filter(rc_en, txdci, txdcq)
                        self.wifi.txp_force_gain(2412, rate, pa_gain, filt_gain, dig_atten)
                        self.wifi.txpacket(chan, rate, 0, cbw40m)


                        test_para = wifi_instrum.test_para(rate)
                        if chan<=14:
                            freq = self.wifi.chan2freq(chan)
                        else:
                            freq = chan

                        myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0, 1)
                        [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false', -15)
                        loginfo("rate=%s, pa_gain=0x%x, filt_gain=0x%x, dig_atten=%d, channel=%d,power=%2.2f,evm=%2.2f"%(rate,pa_gain, filt_gain, dig_atten,chan,pwr, evm))
                        csvreport1.write_data([hex(pa_gain), hex(filt_gain), dig_atten,chan,rate,pwr,evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase, evm_list])
                        print [chan,rate,pwr,evm,evm_std,evm_max,freq_err,clk_err,lo_leakage,iq_imb_amp,iq_imb_phase, evm_list]

                    if pwr>16:
                        break

        logsetlevel('D')

    def WIFI_TX_PWR_EVM(self, cable_lose=2, channel=[1,14], data_rate=['mcs6','mcs7'],iqv_no=1,iqv_num=10, force_txon=0,name_str=""):
        """
        :test TX power and EVM
        :cable_lost:
        :channle: it is matrix [1,...]
        :data_rate: it is matrix ['mcs0',...]
        :iqv_no: 1-left port, 2-right port
        :iqv_num: iqview average number
        """

        mask_marg_title = "lower4_marg, lower3_marg, lower2_marg, lower1_marg, upper1_marg, upper2_marg, upper3_marg, upper4_marg"
        title = 'channel, rate, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage(dB),iq_imb_amp(dB),iq_imb_phase(deg),%s, evm_list\n'%mask_marg_title
        fname = self.wifi.get_filename('wifi_txrx_test_%s'%self.name_str, 'TX')
        csvreport1 = csvreport(fname, title)

        self.wifi.cmdstop()
        max_pwr = 25 - cable_lose

        self.wifi.txpacket(1, '54m', 0, 0)
        test_para = wifi_instrum.test_para('54m')
        myiqv=tester.tester(2412, max_pwr, '54m', test_para, iqv_no,'measure', cable_lose, 10, 1)
        [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 1,'false')

        max_pwr = pwr + 12
        print "max_pwr=%d"%max_pwr

        for rate in data_rate:
            for chan in channel:
                loginfo("rate=%s, channel=%d"%(rate, chan))

                self.wifi.cmdstop()
                cbw40m = self.wifi.rate2ht40(rate)
                if force_txon == 1:
                    self.wifi.tx_cbw40m_en(cbw40m)
                    self.wifi.esp_tx(chan, rate)
                else:
                    self.wifi.txpacket(chan, rate, 0, cbw40m)

                test_para = wifi_instrum.test_para(rate)
                if chan<=14:
                    freq = self.wifi.chan2freq(chan)
                else:
                    freq = chan

                myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0, 1)
                [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false')
                [freq_mask, mask_marg] = wifi_instrum.spectrum_mask_flatness(myiqv, iqv_num, 99)
                print [freq_mask, mask_marg]

                self.wifi.cmdstop()

                csvreport1.write_data([chan,rate,pwr,evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase, mask_marg, evm_list])
                print [chan,rate,pwr,evm,evm_std,evm_max,freq_err,clk_err,lo_leakage,iq_imb_amp,iq_imb_phase, mask_marg, evm_list]


    def WIFI_EVM_DEBUG(self, cable_lose=2, iqv_no=1, len_max = 20, iqv_num=100):
        """
        :test TX power and EVM
        :cable_lost:
        :channle: it is matrix [1,...]
        :data_rate: it is matrix ['mcs0',...]
        :iqv_no: 1-left port, 2-right port
        :iqv_num: iqview average number
        """

        chan = 1
        data_rate = ['mcs7', '54m', 'mcs6', '48m']
        title = 'channel, rate, power, pocket_len, rand_seed, evm, evm_max,evm_min,evm_std,evm_list\n'
        fname = self.wifi.get_filename('wifi_txrx_test', 'EVM_DEBUG')
        csvreport1 = csvreport(fname, title)

        self.wifi.cmdstop()

        self.wifi.rfchsel(chan,0)
        self.wifiapi.set_tx_gain(0x2f, 0x120)
        self.wifiapi.set_tx_dig_gain(1,(256-28)) #256-bk

        for rate in data_rate:
            for rand_seed in range(0, 100, 1):
                self.mem.wrm(0x6001c400, 6, 0, rand_seed)
                pocket_len = 195
                loginfo("rate=%s, len=%d"%(rate, pocket_len))

                self.wifi.cmdstop()
                self.wifi.txout(rate, 0, pocket_len, backoff_qdb=20)

                max_pwr = 25-cable_lose
                test_para = wifi_instrum.test_para(rate)
                freq = self.wifi.chan2freq(chan)

                myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0)
                [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_min, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false')

                self.wifi.cmdstop()

                csvreport1.write_data([chan,rate, pwr, pocket_len, rand_seed, evm,evm_max,evm_min, evm_std, evm_list])
                print [chan,rate,pocket_len, rand_seed, pwr,evm,evm_max,evm_min,evm_std, evm_list]


    def WIFI_EVM_DEBUG_len(self, cable_lose=2, iqv_no=1, len_max = 20, iqv_num=100):
        """
        :test TX power and EVM
        :cable_lost:
        :channle: it is matrix [1,...]
        :data_rate: it is matrix ['mcs0',...]
        :iqv_no: 1-left port, 2-right port
        :iqv_num: iqview average number
        """

        chan = 1
        data_rate = ['mcs7', '54m', 'mcs6', '48m']
        title = 'channel, rate, power, pocket_len, evm, evm_max,evm_min,evm_std,evm_list\n'
        fname = self.wifi.get_filename('wifi_txrx_test', 'EVM_DEBUG')
        csvreport1 = csvreport(fname, title)

        self.wifi.cmdstop()

        self.wifi.rfchsel(chan,0)
        self.wifiapi.set_tx_gain(0x2f, 0x120)
        self.wifiapi.set_tx_dig_gain(1,(256-28)) #256-bk

        for rate in data_rate:
            for pocket_len in range(10, 60, 2):
                self.mem.wrm(0x6001c400, 6, 0, 0x25)
##                pocket_len = 195
                loginfo("rate=%s, len=%d"%(rate, pocket_len))

                self.wifi.cmdstop()
                self.wifi.txout(rate, 0, pocket_len, backoff_qdb=20)

                max_pwr = 25-cable_lose
                test_para = wifi_instrum.test_para(rate)
                freq = self.wifi.chan2freq(chan)

                myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0)
                [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_min, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false')

                self.wifi.cmdstop()

                csvreport1.write_data([chan,rate, pwr, pocket_len, evm,evm_max,evm_min, evm_std, evm_list])
                print [chan,rate,pocket_len, pwr,evm,evm_max,evm_min,evm_std, evm_list]


    #*************************************************************#
    #*****************wifi rx *****************#
    #*********************************************************************#

    def get_data_sens(self, packnum, perform_list):
    #**************creat log***************#

        cur_sense=0
        cur_sense_rssi=0
        cur_sense_find=0
        cur_max=0
        cur_max_rssi=0
        cur_max_find=0
        cur_max_start = 0
        fail=0
        cur_err=0
        cur_err_fcs=0

        for data in perform_list:
            loginfo(data)
            if cur_sense_find==0:
                if data[1]>=(packnum*0.9):
                    cur_sense=data[0]
                    cur_sense_rssi=data[2]
                    cur_err=data[4]
                    cur_err_fcs = data[5]
                    cur_sense_find=1
                else:
                    cur_sense=data[0]
                    cur_sense_rssi=data[2]
                    cur_err=data[4]
                    cur_err_fcs = data[5]
                    cur_sense_find=0
            if cur_max_find==0:
                if cur_max_start==0:
                    if data[1]>=(packnum*0.95):
                        cur_max_start=1
                else:
                    if data[1]<(packnum*0.9):
                        cur_max_find=1
                    else:
                        cur_max=data[0]
                        cur_max_rssi=data[2]
                        cur_max_find=0
        return [cur_sense, cur_sense_rssi/10.0, cur_sense_find, cur_max, cur_max_rssi/10.0, cur_max_find, perform_list]


    def WIFI_RX_per(self, cable_lose=13,rx_chan=11,tx_chan=11, rx_rate='mcs6', minpwr=-80, maxpwr=-30,pwr_step =1, packnum=100, iqv_no=1,filter_dcap=40):
        """
        :test RX performance
        """
        logsetlevel("I")

        name_str = '%s_%s_%s_%s_%s'%(rx_chan, rx_rate, minpwr, maxpwr,filter_dcap)
        title = 'rx_chan, rfpwr, rxnum, rssi, gain, noise, err, fcs, freq\n'
        fname = self.wifi.get_filename('wifi_txrx_test_%s'%self.name_str, 'RX_%s'%name_str, 'wifitest_rx')
        csvreport1 = csvreport(fname, title)

        self.wifi.cmdstop()

        if tx_chan<15:
           tx_freq=self.wifi.chan2freq(tx_chan)
        else:
           tx_freq=tx_chan

        if rx_chan<15:
           rx_freq=self.wifi.chan2freq(rx_chan)
        else:
           rx_freq=rx_chan
        loginfo('tx chan cfg: %d %d'%(tx_chan,tx_freq))
        loginfo('rx chan cfg: %d %d'%(rx_chan,rx_freq))

        mytester=tester.tester(tx_freq,-40,'1m',1,iqv_no,'source',cable_lose,isreset=1)

        ratenum = rate_dict[rx_rate]
        cbw40m = self.wifi.rate2ht40(rx_rate)

        if cbw40m==1 and ratenum < 0x10:
            tx_freq -= 10

        perform_list=[]
        rfpwr= minpwr
        loginfo('\nscan %s rx now!'%rx_rate)

        mytester.sigout(tx_freq,rfpwr,cable_lose,rx_rate,packnum,iqv_no)
        sens=minpwr+20
        sens_rssi=minpwr+20

        if rx_chan<15:
            self.wifi.rfchsel(rx_chan, cbw40m*2)
        else:
            self.wifi.rfchsel(14, cbw40m*2)
            self.rfpll.set_freq(tx_chan)
        self.i2c.bbtop.filter_wifirx0_dcap_lq=filter_dcap
        self.i2c.bbtop.filter_wifirx0_dcap_hq=filter_dcap
        self.i2c.bbtop.filter_wifirx1_dcap_lq=filter_dcap
        self.i2c.bbtop.filter_wifirx1_dcap_hq=filter_dcap
        self.i2c.bbtop.filter_wifirx2_dcap_lq=filter_dcap
        self.i2c.bbtop.filter_wifirx2_dcap_hq=filter_dcap
        self.i2c.bbtop.filter_wifirx3_dcap_lq=filter_dcap
        self.i2c.bbtop.filter_wifirx3_dcap_hq=filter_dcap
        print "filter_dacp=%s"%filter_dcap
        while rfpwr<=maxpwr:
            mytester.sigout(tx_freq,rfpwr,cable_lose,rx_rate,packnum,iqv_no)

            self.wifi.rxstart(rx_rate)
##            wifi.esp_rx(rx_chan, rx_rate)
            mytester.trig_wave(iqv_no);
            time.sleep(0.1)
            result_data = self.wifi.cmdstop()

            [DesirePackNum, gain, rssi, noise, err, err2, freqoff] = self.wifi.rxresult(result_data)

            perform_list.append((rfpwr,DesirePackNum,rssi,gain,noise,err,err2, freqoff));
            loginfo(result_data)
            csvreport1.write_data([rx_chan,rfpwr,DesirePackNum,rssi,gain,noise,err,err2, freqoff])

            rfpwr=rfpwr+pwr_step;
            mytester.set_pwr(rfpwr,0,iqv_no,'source');

        [cur_sense, cur_sense_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find, perform_list] = self.get_data_sens(packnum, perform_list)

        mytester.gen_switch('OFF',iqv_no);

        logsetlevel("D")

        return [cur_sense, cur_sense_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find, perform_list];


    def WIFI_RX_sens(self, cable_lose=13, chan_in=[1], data_rate=['mcs7'],packnum=100,loop_num=1,iqv_no=1,name_str=""):

        title = 'test_number,channel, rate, sens, sens_rssi, sens_find\n'
        fname = self.wifi.get_filename('wifi_txrx_test_%s'%self.name_str, 'RXSens')
        csvreport2 = csvreport(fname, title)

        for loop in range(1,loop_num+1):
            for cur_rate in data_rate:
                cur_sens_list=[]
                cur_sens_rssi_list=[]
                for i in range(0, len(chan_in)):
                    chan_no = chan_in[i]
                    rx_chan = chan_no
                    tx_chan = chan_no

                    loginfo('chan=%d'%chan_no)
                    loginfo("loop=%d"%loop)
                    ratenum = rate_dict[cur_rate]
                    rate_sens = sens_dict[cur_rate]
                    minpwr = rate_sens - 1
                    maxpwr = rate_sens + 6
                    loginfo('minpwr=%d, maxpwr=%d'%(minpwr,maxpwr))

                    [cur_sens, cur_sens_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find,per_list] = self.WIFI_RX_per(cable_lose,rx_chan,tx_chan,cur_rate,minpwr,maxpwr,1,packnum,iqv_no)

                    csvreport2.write_data([loop,chan_no,cur_rate,cur_sens,cur_sens_rssi,cur_sense_find])

                    cur_sens_list.append(cur_sens)
                    cur_sens_rssi_list.append(cur_sens_rssi)

                pylab.ion()
                pylab.figure(100)
                pylab.plot(chan_in,cur_sens_list,label='rx_rate=%s,test_number=%d'%(cur_rate,loop))
                pylab.xlabel('channel')
                pylab.ylabel('sensitivity(dBm)')
                pylab.legend()
                pylab.grid()
                pylab.show()

                pylab.figure(101)
                pylab.plot(chan_in,cur_sens_rssi_list,label='rx_rate=%s,test_number=%d'%(cur_rate,loop))
                pylab.xlabel('channel')
                pylab.ylabel('rssi(dBm)')
                pylab.legend()
                pylab.grid()
                pylab.show()
    def WIFI_RX_maxlevel(self, cable_lose=13, chan_in=[1], data_rate=['mcs7'], iqv_no=1,name_str=""):

        title = 'channel, rate, cur_max, cur_max_rssi, cur_max_find\n'
        fname = self.wifi.get_filename('wifi_txrx_test_%s'%self.name_str, 'RXMaxLevel')
        csvreport2 = csvreport(fname, title)

        packnum=100

        for cur_rate in data_rate:

            maxlevel = maxleve_dict[cur_rate]
            minpwr = maxlevel -10
            maxpwr = maxlevel + 3
            loginfo('minpwr=%d, maxpwr=%d'%(minpwr,maxpwr))

            for i in range(0, len(chan_in)):
                chan_no = chan_in[i]
                rx_chan = chan_no
                tx_chan = chan_no

                loginfo('chan=%d'%chan_no)

                [cur_sens, cur_sens_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find,per_list] = self.WIFI_RX_per(cable_lose,rx_chan,tx_chan,cur_rate,minpwr,maxpwr,1,packnum,iqv_no)
                csvreport2.write_data([chan_no,cur_rate,cur_max, cur_max_rssi, cur_max_find])


    def WIFI_RX_range(self, cable_lose=13, chan_in=[1], data_rate=['mcs7'], rx_range=['[-60, -20]'], iqv_no=1,name_str=""):

        title = 'channel, rate, minpwr, maxpwr, sens, sens_rssi, sens_find, cur_max, cur_max_rssi, cur_max_find\n'
        fname = self.wifi.get_filename('wifi_txrx_test_%s'%self.name_str, 'RXRange')
        csvreport2 = csvreport(fname, title)

        packnum=100

        for i in range(0, len(chan_in)):
            for j in range(0,len(data_rate)):
                cur_rate = data_rate[j]
                chan_no = chan_in[i]
                rx_chan = chan_no
                tx_chan = chan_no
                rssi_range = rx_range[j]
                rssi_range = rssi_range.replace('[','').replace(']','')
                rssi_range = rssi_range.split(',')
                print rx_range
                print rssi_range
                minpwr = int(rssi_range[0], 10)
                maxpwr = int(rssi_range[1], 10)
                rate_sens = sens_dict[cur_rate]

                print 'minpwr=%d, maxpwr=%d'%(minpwr,maxpwr)

                print 'chan=%d'%chan_no

                [cur_sens, cur_sens_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find,per_list] = self.WIFI_RX_per(cable_lose,rx_chan,tx_chan,cur_rate,minpwr,maxpwr,1,packnum,iqv_no)

                csvreport2.write_data([chan_no,cur_rate,minpwr,maxpwr,cur_sens, cur_sens_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find])

    def WIFI_RX_range_filter_gain(self, cable_lose=13, chan_in=[1], data_rate=['mcs7'], rx_range=['[-60, -20]'], iqv_no=1,name_str=""):

        title = 'channel, rate, minpwr, maxpwr, filter_dcap, rxgian, sens, sens_rssi, sens_find, cur_max, cur_max_rssi, cur_max_find\n'
        fname = self.wifi.get_filename('wifi_txrx_test_%s'%self.name_str, 'WIFI_RX_range_filter_gain')
        csvreport2 = csvreport(fname, title)

        packnum=100

        for i in range(0, len(chan_in)):
            for j in range(0,len(data_rate)):
                cur_rate = data_rate[j]
                chan_no = chan_in[i]
                rx_chan = chan_no
                tx_chan = chan_no
                rssi_range = rx_range[j]
                rssi_range = rssi_range.replace('[','').replace(']','')
                rssi_range = rssi_range.split(',')
                print rx_range
                print rssi_range
                minpwr = int(rssi_range[0], 10)
                maxpwr = int(rssi_range[1], 10)
                rate_sens = sens_dict[cur_rate]

                print 'minpwr=%d, maxpwr=%d'%(minpwr,maxpwr)

                print 'chan=%d'%chan_no
                self.wifiapi.wifi_filtbw_set(1,1)
                for filter_dcap in range(15,65):
                    for rxgain in range(35,60):
                        self.wifi.rx_force_gain(1,rxgain)

                        [cur_sens, cur_sens_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find,per_list] = self.WIFI_RX_per(cable_lose,rx_chan,tx_chan,cur_rate,minpwr,maxpwr,1,packnum,iqv_no,filter_dcap)

                        csvreport2.write_data([chan_no,cur_rate,minpwr,maxpwr, filter_dcap, rxgain, cur_sens, cur_sens_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find])

    def wifi_test(self, test_flag=0xf,temp_vol=""):
        # load RF setting
        self.wifi.cmdstop()
        [cable_lose, unit_no, temperature, tx_channel, tx_rate, rx_channel, rx_rate, rxm_channel, rxm_rate, rxd_channel, rxd_rate, rxd_range] = self.get_rf_setting()

        # RF test list

        self.wifi.save_init_print('wifi_txrx_test_%s'%self.name_str)

        if (test_flag & 0x1) > 0:
            self.WIFI_TX_PWR_EVM(cable_lose=cable_lose, channel=tx_channel, data_rate=tx_rate, iqv_no=unit_no, iqv_num=10,name_str=temp_vol)

        if (test_flag & 0x2) > 0:
            self.WIFI_RX_sens(cable_lose=cable_lose, chan_in=rx_channel, data_rate=rx_rate,iqv_no=unit_no,name_str=temp_vol)

        if (test_flag & 0x4) > 0:
            self.WIFI_RX_maxlevel(cable_lose=cable_lose, chan_in=rxm_channel,data_rate=rxm_rate,iqv_no=unit_no,name_str=temp_vol)

        if (test_flag & 0x8) > 0:
            self.WIFI_RX_range(cable_lose=cable_lose, chan_in=rxd_channel, data_rate=rxd_rate, rx_range=rxd_range, iqv_no=unit_no,name_str=temp_vol)
















