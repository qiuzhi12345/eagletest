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
import pylab as plt
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
from rftest.rflib.rfcal import rfcal

rate_bps_dict = rfglobal.rate_bps_dict
sens_dict = rfglobal.sens_dict
rate_dict = rfglobal.ratedic
maxleve_dict = rfglobal.rx_maxlevel_dict
rfglobal.iqv['evm_sorted'] = 0
##rfglobal.iqv_arg['auto_range']=0


class WIFI_TXRX_TEST(object):

    def __init__(self,comport,chipv='ESP32'):
        self.comport = comport
        self.chipv = chipv
        self.mem = MEM(self.comport,self.chipv)
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.wifiapi = WIFIAPI(self.comport,self.chipv)
        self.rfpll = rfpll(self.comport,self.chipv)
        self.i2c = HWI2C(self.comport,self.chipv)
        self.pbus = pbus(self.comport,self.chipv)
        self.rfcal = rfcal(self.comport,self.chipv)


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

    def WIFI_TX_PWR_EVM_freq_offset(self, cable_lose=2, channel=[1,14], data_rate=['mcs6','mcs7'],iqv_no=1,iqv_num=10, force_txon=0,name_str=""):
        """
        :test TX power and EVM
        :cable_lost:
        :channle: it is matrix [1,...]
        :data_rate: it is matrix ['mcs0',...]
        :iqv_no: 1-left port, 2-right port
        :iqv_num: iqview average number
        """
        rfglobal.iqv['evm_sorted'] = 0

        mask_marg_title = "lower4_marg, lower3_marg, lower2_marg, lower1_marg, upper1_marg, upper2_marg, upper3_marg, upper4_marg"
        title = 'channel, rate, freq_offset, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage(dB),iq_imb_amp(dB),iq_imb_phase(deg),%s, evm_list\n'%mask_marg_title
        fname = self.wifi.get_filename('wifi_txrx_test_%s'%name_str, 'TX')
        csvreport1 = csvreport(fname, title)

        self.wifi.cmdstop()
        max_pwr = 25 - cable_lose

        self.wifi.txpacket(1, '54m', 0, 0, duty=0.1)
        test_para = wifi_instrum.test_para('54m')
        myiqv=tester.tester(2412, max_pwr, '54m', test_para, iqv_no,'measure', cable_lose, 10, 1,1,20)
        [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 1,'false')

        max_pwr = pwr + 12
        print "max_pwr=%f"%max_pwr
        result = []
        for rate in data_rate:
            for chan in channel:
                loginfo("rate=%s, channel=%d"%(rate, chan))
                for freq_offset in range(-100,100,10):
                    if freq_offset<0:
                        freq_offset_s = freq_offset+655365
                    else:
                        freq_offset_s = freq_offset


                    self.wifi.cmdstop()
                    cbw40m = self.wifi.rate2ht40(rate)
                    self.wifi.rfchsel_offset_esp32(freq_offset_s)
                    if force_txon == 1:
                        self.wifi.tx_cbw40m_en(cbw40m)
                        self.wifi.esp_tx(chan, rate)
                    else:
                        self.wifi.txpacket(chan, rate, 0, cbw40m, backoff_qdb=0,duty=0.1)

                    test_para = wifi_instrum.test_para(rate)
                    if chan<=14:
                        freq = self.wifi.chan2freq(chan)
                    else:
                        freq = chan

                    myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0, 0,20)
                    [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false')
                    [freq_mask, mask_marg] =  wifi_instrum.spectrum_mask_flatness(myiqv, iqv_num, 99)
        ##                print [freq_mask, mask_marg]

                    self.wifi.cmdstop()

                    csvreport1.write_data([chan,rate,freq_offset,pwr,evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase, mask_marg, evm_list])
                    print [chan,rate,pwr,evm,evm_std,evm_max]


    def WIFI_TX_PWR_EVM_Radition(self, channel=[1,14], data_rate=['mcs6','mcs7'],iqv_no=1,iqv_num=10, force_txon=0,name_str=""):
        """
        :test TX power and EVM
        :cable_lost:
        :channle: it is matrix [1,...]
        :data_rate: it is matrix ['mcs0',...]
        :iqv_no: 1-left port, 2-right port
        :iqv_num: iqview average number
        """
        rfglobal.iqv['evm_sorted'] = 0

        mask_marg_title = "lower4_marg, lower3_marg, lower2_marg, lower1_marg, upper1_marg, upper2_marg, upper3_marg, upper4_marg"
        title = 'channel, rate,cable_lose, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage(dB),iq_imb_amp(dB),iq_imb_phase(deg),%s, evm_list\n'%mask_marg_title
        fname = self.wifi.get_filename('wifi_txrx_test_%s'%name_str, 'TX')
        csvreport1 = csvreport(fname, title)
        cable_lose_list= self.wifi.get_rx_cable_lost(iqv_no,channel)
        cable_lose=cable_lose_list[0]

        self.wifi.cmdstop()
        max_pwr = 25 - cable_lose

        self.wifi.txpacket(1, '54m', 0, 0, duty=0.1)
        test_para = wifi_instrum.test_para('54m')

        myiqv=tester.tester(2412, max_pwr, '54m', test_para, iqv_no,'measure', cable_lose, 10,1, 1,20)

        [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 1,'false')

##        max_pwr = pwr + 12
        print "max_pwr=%f"%max_pwr
        result = []
        for rate in data_rate:
            i = 0
            for chan in channel:
                cable_lose= cable_lose_list[i]
                i +=1
                loginfo("rate=%s, channel=%d,cable_lose=%2.2f"%(rate, chan,cable_lose))

                self.wifi.cmdstop()
                cbw40m = self.wifi.rate2ht40(rate)
                if force_txon == 1:
                    self.wifi.tx_cbw40m_en(cbw40m)
                    self.wifi.esp_tx(chan, rate)
                else:
                    self.wifi.txpacket(chan, rate, 0, cbw40m, backoff_qdb=0,duty=0.1)

                test_para = wifi_instrum.test_para(rate)
                if chan<=14:
                    freq = self.wifi.chan2freq(chan)
                else:
                    freq = chan

                myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0, 0,20)

                [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false')
                [freq_mask, mask_marg] =  wifi_instrum.spectrum_mask_flatness(myiqv, iqv_num, 99)
##                print [freq_mask, mask_marg]

                self.wifi.cmdstop()
##                self.wifi.cmdstop()
                or_pll_cap = self.i2c.rfpll.or_pll_cap
                or_pll_dac = self.i2c.rfpll.or_pll_dac
                ir_cap_ext = self.i2c.rfpll.ir_cap_ext
                ir_dac_ext = self.i2c.rfpll.ir_dac_ext

                result.append([chan,rate,pwr,evm, or_pll_cap, or_pll_dac, ir_cap_ext, ir_dac_ext])

                csvreport1.write_data([chan,rate,cable_lose,pwr,evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase, mask_marg, evm_list])
                print [chan,rate,pwr,evm,evm_std,evm_max]

        for data in result:
            print data

        if self.chipv=="ESP8266":
            gain_mis = self.i2c.dig_inf.tx_q_q_coff
            phase_mis = self.i2c.dig_inf.tx_q_i_coff
            print "gain_mis=%d, phase_mis=%d"%(gain_mis, phase_mis)

    def txpwr_track_test(self, cable_lose=2, channel=[1,14], data_rate=['mcs6','mcs7'],iqv_no=1,iqv_num=10, force_txon=0,name_str=""):
        """
        :test TX power and EVM
        :cable_lost:
        :channle: it is matrix [1,...]
        :data_rate: it is matrix ['mcs0',...]
        :iqv_no: 1-left port, 2-right port
        :iqv_num: iqview average number
        """
        title = 'channel, rate, pwr_track_en, fe_rate, mode, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage(dB),iq_imb_amp(dB),iq_imb_phase(deg),evm_list\n'
        fname = self.wifi.get_filename('wifi_txrx_test_%s'%name_str, 'TX')
        csvreport1 = csvreport(fname, title)

        self.wifi.cmdstop()
        max_pwr = 25 - cable_lose

        self.wifi.txpacket(1, '54m', 0, 0, duty=0.1)
        test_para = wifi_instrum.test_para('54m')
        myiqv=tester.tester(2412, max_pwr, '54m', test_para, iqv_no,'measure', cable_lose, 10,1,1,20)
        [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 1,'false')

##        max_pwr = pwr + 30
##        print "max_pwr=%f"%max_pwr
        result = []
        for i in range(2):
            if i==0:
                self.wifiapi.txpwr_track_en(0,0,0)
            else:
                self.wifiapi.txpwr_track_en(1,1,0)
            for rate in data_rate:
                for chan in channel:

                    loginfo("rate=%s, channel=%d,cable_lose=%2.2f"%(rate, chan,cable_lose))

                    self.wifi.cmdstop()
                    cbw40m = self.wifi.rate2ht40(rate)
                    if force_txon == 1:
                        self.wifi.tx_cbw40m_en(cbw40m)
                        self.wifi.esp_tx(chan, rate)
                    else:
                        self.wifi.txpacket(chan, rate, 0, cbw40m, backoff_qdb=0,duty=0.1)

                    if i>0:
                        time.sleep(2)

                    test_para = wifi_instrum.test_para(rate)
                    if chan<=14:
                        freq = self.wifi.chan2freq(chan)
                    else:
                        freq = chan

                    myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0,0,20)
                    [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false')
##                    [freq_mask, mask_marg] =  wifi_instrum.spectrum_mask_flatness(myiqv, iqv_num, 99)
    ##                print [freq_mask, mask_marg]

                    self.wifi.cmdstop()
    ##                self.wifi.cmdstop()
                    tx_rate = self.wifiapi.get_tx_rate()
                    track_rate = [tx_rate / 4, tx_rate & 0x3]
                    or_pll_cap = self.i2c.rfpll.or_pll_cap
                    or_pll_dac = self.i2c.rfpll.or_pll_dac
                    ir_cap_ext = self.i2c.rfpll.ir_cap_ext
                    ir_dac_ext = self.i2c.rfpll.ir_dac_ext

                    result.append([chan,rate,pwr,evm, or_pll_cap, or_pll_dac, ir_cap_ext, ir_dac_ext])

                    csvreport1.write_data([chan,rate,i, track_rate, pwr,evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase,evm_list])
                    print [chan,rate,track_rate,pwr,evm,evm_std,evm_max]

            for data in result:
                print data

    def WIFI_TX_PWR_EVM_HT40(self, cable_lose=2, channel=[1,14], data_rate=['mcs6','mcs7'],iqv_no=1,iqv_num=10, force_txon=0,name_str=""):
        """
        :test TX power and EVM
        :cable_lost:
        :channle: it is matrix [1,...]
        :data_rate: it is matrix ['mcs0',...]
        :iqv_no: 1-left port, 2-right port
        :iqv_num: iqview average number
        """
        rfglobal.iqv['evm_sorted'] = 0
        mask_marg_title = "lower4_marg, lower3_marg, lower2_marg, lower1_marg, upper1_marg, upper2_marg, upper3_marg, upper4_marg"
        title = 'channel,HT40_index,chan_test,rate, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage(dB),iq_imb_amp(dB),iq_imb_phase(deg),%s, evm_list\n'%mask_marg_title
        fname = self.wifi.get_filename('wifi_txrx_test_%s'%name_str, 'TX')
        csvreport1 = csvreport(fname, title)

        self.wifi.cmdstop()
        max_pwr = 25 - cable_lose

        self.wifi.txpacket(1, '54m', 0, 0, duty=0.1)
        test_para = wifi_instrum.test_para('54m')
        myiqv=tester.tester(2412, max_pwr, '54m', test_para, iqv_no,'measure', cable_lose, 10,1,1,20)
        [pwr, freq_err, clk_err, evm, evm_std, evm_max,lo_leakage,iq_imb_amp,iq_imb_phase,evm_list] = wifi_instrum.iqv_avg(myiqv, 1,'false')

##        max_pwr = pwr + 30
##        print "max_pwr=%f"%max_pwr
        result = []
        for rate in data_rate:
            for chan in channel:

                loginfo("rate=%s, channel=%d,cable_lose=%2.2f"%(rate, chan,cable_lose))

                self.wifi.cmdstop()
                cbw40m = self.wifi.rate2ht40(rate)
                if force_txon == 1:
                    self.wifi.tx_cbw40m_en(cbw40m)
                    self.wifi.esp_tx(chan, rate)
                else:
                    for ht40 in range(2,4):
                        self.wifiapi.cmdstop()
                        self.wifiapi.rfchsel(chan,ht40)
                        rate_index=self.wifi.ratecheck(rate)
                        [len_byte, delay] = self.wifi.get_length_delay_duty(rate,0.2)
                        self.wifi.txout(rate_sym=rate, PackNum=0, PackLen =len_byte, cbw40=cbw40m, ht_dup=0, backoff_qdb=0, frm_delay=delay)

                        test_para = wifi_instrum.test_para(rate)
                        if chan<=14:
                            freq = self.wifi.chan2freq(chan)

                        if  ht40 == 2:
                            freq -=10
                        elif ht40 == 3:
                            freq +=10
                        else:
                            freq = chan

                        myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0,0,20)
                        [pwr, freq_err, clk_err, evm, evm_std, evm_max, lo_leakage,iq_imb_amp,iq_imb_phase,evm_list] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false')
                        [freq_mask, mask_marg] =  wifi_instrum.spectrum_mask_flatness(myiqv, iqv_num, 99)
        ##                print [freq_mask, mask_marg]
                        if freq<2412 or freq >2472:
                            chan_test =freq
                        else:
                            chan_test = self.wifi.freq2chan(freq)

                        self.wifi.cmdstop()
                        or_pll_cap = self.i2c.rfpll.or_pll_cap
                        or_pll_dac = self.i2c.rfpll.or_pll_dac
                        ir_cap_ext = self.i2c.rfpll.ir_cap_ext
                        ir_dac_ext = self.i2c.rfpll.ir_dac_ext

                        result.append([chan,ht40,rate,pwr,evm, or_pll_cap, or_pll_dac, ir_cap_ext, ir_dac_ext])

                        csvreport1.write_data([chan,ht40,chan_test,rate,pwr,evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase, mask_marg, evm_list])
                        print [chan,ht40,chan_test,rate,pwr,evm,evm_std,evm_max]

        for data in result:
            print data


    def WIFI_TX_PWR_EVM(self, cable_lose=2, channel=[1,14], data_rate=['mcs6','mcs7'],iqv_no=1,iqv_num=10, force_txon=0,name_str=""):
        """
        :test TX power and EVM
        :cable_lost:
        :channle: it is matrix [1,...]
        :data_rate: it is matrix ['mcs0',...]
        :iqv_no: 1-left port, 2-right port
        :iqv_num: iqview average number
        """
        rfglobal.iqv['evm_sorted'] = 0
##        rfglobal.iqv_arg['auto_range']=0
        mask_marg_title = "lower4_marg, lower3_marg, lower2_marg, lower1_marg, upper1_marg, upper2_marg, upper3_marg, upper4_marg"
        title = 'channel, rate, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage(dB),iq_imb_amp(dB),iq_imb_phase(deg),%s, evm_list\n'%mask_marg_title
        fname = self.wifi.get_filename('wifi_txrx_test_%s'%name_str, 'TX')
        csvreport1 = csvreport(fname, title)

        self.wifi.cmdstop()
        max_pwr = 25 - cable_lose

        self.wifi.txpacket(1, '54m', 0, 0, duty=0.1)
        test_para = wifi_instrum.test_para('54m')
        myiqv=tester.tester(2412, max_pwr, '54m', test_para, iqv_no,'measure', cable_lose, 10,1,1,20)
        [pwr, freq_err, clk_err, evm, evm_std, evm_max,lo_leakage,iq_imb_amp,iq_imb_phase, evm_list] = wifi_instrum.iqv_avg(myiqv, 1,'false')

##        max_pwr = pwr + 30
##        print "max_pwr=%f"%max_pwr
        result = []
##        for i in range (0,11):
        self.wifi.save_init_print('wifi_txrx_test_%s'%name_str)
        for rate in data_rate:
            for chan in channel:

                loginfo("rate=%s, channel=%d,cable_lose=%2.2f"%(rate, chan,cable_lose))

                self.wifi.cmdstop()
                cbw40m = self.wifi.rate2ht40(rate)
                if force_txon == 1:

                    self.wifi.tx_cbw40m_en(cbw40m)
                    self.wifi.esp_tx(chan, rate)
                else:
                    self.wifi.txpacket(chan, rate, 0, cbw40m, backoff_qdb=0,duty=0.1)

                test_para = wifi_instrum.test_para(rate)
                if chan<=14:
                    freq = self.wifi.chan2freq(chan)
                else:
                    freq = chan

                myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0,0,20)
                [pwr, freq_err, clk_err, evm, evm_std, evm_max, lo_leakage,iq_imb_amp,iq_imb_phase,evm_list] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false')
                [freq_mask, mask_marg] =  wifi_instrum.spectrum_mask_flatness(myiqv, iqv_num, 99)
##                print [freq_mask, mask_marg]

                self.wifi.cmdstop()

                or_pll_cap = self.i2c.rfpll.or_pll_cap
                or_pll_dac = self.i2c.rfpll.or_pll_dac
                ir_cap_ext = self.i2c.rfpll.ir_cap_ext
                ir_dac_ext = self.i2c.rfpll.ir_dac_ext

                result.append([chan,rate,pwr,evm, or_pll_cap, or_pll_dac, ir_cap_ext, ir_dac_ext])

                csvreport1.write_data([chan,rate,pwr,evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase, mask_marg, evm_list])
                print [chan,rate,pwr,evm,evm_std,evm_max]

        for data in result:
            print data

        if self.chipv=="ESP8266":
            gain_mis = self.i2c.dig_inf.tx_q_q_coff
            phase_mis = self.i2c.dig_inf.tx_q_i_coff
            print "gain_mis=%d, phase_mis=%d"%(gain_mis, phase_mis)

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

                myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0,1,20)
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

                myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0,1,20)
                [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_min, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false')

                self.wifi.cmdstop()

                csvreport1.write_data([chan,rate, pwr, pocket_len, evm,evm_max,evm_min, evm_std, evm_list])
                print [chan,rate,pocket_len, pwr,evm,evm_max,evm_min,evm_std, evm_list]


    def WIFI_TX_CLIP_MASK(self, cable_lose=2, channel=[1], data_rate=['mcs0'], pa_gain=0x5f, bb_gain=0x30, dig_atten=5, target_power=18, iqv_no=1, iqv_num=10):
        """
        :test TX power and EVM
        :cable_lost:
        :channle: it is matrix [1,...]
        :data_rate: it is matrix ['mcs0',...]
        :iqv_no: 1-left port, 2-right port
        :iqv_num: iqview average number
        """
        freq_marg_title = "lower4_freq, lower3_freq, lower2_freq, lower1_freq, upper1_freq, upper2_freq, upper3_freq, upper4_freq"
        mask_marg_title = "lower4_marg, lower3_marg, lower2_marg, lower1_marg, upper1_marg, upper2_marg, upper3_marg, upper4_marg"
        title = 'channel, rate, clip_val, clip_comp, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage(dB),iq_imb_amp(dB),iq_imb_phase(deg),%s,%s,evm_list\n'%(freq_marg_title,mask_marg_title)
        fname = self.wifi.get_filename('wifi_txrx_test', 'CLIP_MASK')
        csvreport1 = csvreport(fname, title)

        self.wifi.cmdstop()
        max_pwr = 25 - cable_lose

        self.wifi.txpacket(1, '54m', 0, 0)
        test_para = wifi_instrum.test_para('54m')
        myiqv=tester.tester(2412, max_pwr, '54m', test_para, iqv_no,'measure', cable_lose, 10, 1)
        [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 1,'false')

        max_pwr = pwr + 12
        print "max_pwr=%d"%max_pwr
        clip_comp = 0
        for rate in data_rate:
            for chan in channel:
                loginfo("rate=%s, channel=%d"%(rate, chan))

                self.wifi.cmdstop()
                cbw40m = self.wifi.rate2ht40(rate)
                self.wifi.rfchsel(chan,cbw40m*2)
                self.wifiapi.pll_cap_track_en(1)
                self.wifiapi.set_tx_gain(pa_gain,bb_gain)
                self.wifiapi.set_tx_dig_gain(1,256-dig_atten)
                self.wifi.txout(rate, PackNum=0, PackLen=500, cbw40=cbw40m, ht_dup=0, backoff_qdb=0, frm_delay=1500)

                max_pwr = 25-cable_lose
                test_para = wifi_instrum.test_para(rate)
                freq = self.wifi.chan2freq(chan)

                for val in range(-20,60,4):
                    clip_val = val-dig_atten
                    if clip_val < 0:
                        clip_val = 256 + clip_val
                    for tt in range(0,3):
                        print '%d'%tt,clip_val,clip_comp,self.mem.rdm(0x60006000,9,2)

                        self.wifi.dig_gain_clip(clip_val,clip_comp)
                        self.wifi.txout(rate, PackNum=0, PackLen=500, cbw40=cbw40m, ht_dup=0, backoff_qdb=0, frm_delay=1500)
                        myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0, 1,20)
                        [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false')
                        if tt < 3:
                            delta = int((pwr - target_power)*4)
                            if (delta < 1 ) & (delta > -1):
                                break
                            clip_comp -= delta


                    [freq_mask, mask_marg] = wifi_instrum.spectrum_mask_flatness(myiqv, iqv_num, 99)

                    self.wifi.cmdstop()

                    csvreport1.write_data([chan,rate,clip_val,clip_comp,pwr,evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase, freq_mask, mask_marg, evm_list])
                    print [chan,rate,clip_val,clip_comp,pwr,evm,evm_std,evm_max,freq_err,clk_err,lo_leakage,iq_imb_amp,iq_imb_phase, freq_mask, mask_marg, evm_list]





    #*************************************************************#
    #*****************wifi rx *****************#
    #*********************************************************************#

    def get_data_sens(self, packnum, perform_list):
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


    def get_rx_data(self, perform_list):
        suc_num = []
        rx_rssi = []
        for data in perform_list:
            suc_num.append(data[1])
            rx_rssi.append(data[0])
        return [suc_num, rx_rssi]

    def WIFI_RX_per(self, cable_lose=13,rx_chan=11,tx_chan=11, rx_rate='mcs6', minpwr=-80, maxpwr=-30,pwr_step =1, packnum=100, iqv_no=1,name_str='', break_en=0, maxlevel_en=0, ht40_index=0):
        """
        :test RX performance
        """
        print_err_code = 0
        rssi_data_base_en = 0
        rssi_data_base = 0

        logsetlevel("I")

        self.wifi.cmdstop()
        self.wifiapi.rssi_min_max_print()
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

        if rx_rate=="test":
            ratenum = rate_dict["mcs6"]
            cbw40m = self.wifi.rate2ht40("mcs6")

        else:
            ratenum = rate_dict[rx_rate]
            cbw40m = self.wifi.rate2ht40(rx_rate)

        if ht40_index == 2:
            tx_freq -= 10
        elif ht40_index == 3:
            tx_freq += 10
        elif cbw40m==1 and ratenum < 0x10:
            tx_freq -= 10

        name_str_local = '%s_%s_%s_%s_%s_%s'%(rx_chan, tx_freq, rx_rate, minpwr, maxpwr,name_str)
        if rssi_data_base == 1:
            title = 'rx_chan, ht40_index, tx_freq, rfpwr, rxnum, rssi, gain, noise, err, fcs, freq, rssi_min, rssi_max,rssi_base_p5,rssi_base_p4,rssi_base_p3,rssi_base_p2,rssi_base_p1,rssi_base_n0,rssi_base_n1,rssi_base_n2,rssi_base_n3,rssi_base_n4,rssi_base_n5\n'
        else:
            title = 'rx_chan, ht40_index, tx_freq, rfpwr, rxnum, rssi, gain, noise, err, fcs, freq, rssi_min, rssi_max\n'
        fname = self.wifi.get_filename('wifi_txrx_test_%s'%name_str, 'RX_%s'%name_str_local, 'rx')
        csvreport1 = csvreport(fname, title)

        perform_list=[]

        rfpwr= minpwr

        loginfo('\nscan %s rx now!'%rx_rate)

        mytester.sigout(tx_freq,rfpwr,cable_lose,rx_rate,packnum,iqv_no)
        sens=minpwr+20
        sens_rssi=minpwr+20

        if rx_chan<15:
            if ht40_index == 0:
                ht40_index = cbw40m*2
            self.wifi.rfchsel(rx_chan, ht40_index)

        else:
            if ht40_index == 0:
                ht40_index = cbw40m*2
            self.wifi.rfchsel(14, ht40_index)
            self.rfpll.set_freq(tx_chan)

        while rfpwr<=maxpwr:
            loginfo("rfpwr=%d"%rfpwr)
            mytester.sigout(tx_freq,rfpwr,cable_lose,rx_rate,packnum,iqv_no)
            if rssi_data_base_en == 1:
                rssi_data_base = 256 + rfpwr

            if rx_rate=="test":
                self.wifi.rxstart("mcs7", print_err_code,rssi_data_base)
                #wifi.esp_rx(rx_chan, rx_rate)
            else:
                self.wifi.rxstart(rx_rate, print_err_code,rssi_data_base)

            mytester.trig_wave(iqv_no);
            time.sleep(0.1)
            result_data = self.wifi.cmdstop(print_err=print_err_code)

            if rssi_data_base_en == 1:
                [DesirePackNum, gain, rssi, noise, err, err2,freqoff, rssi_min, rssi_max,rssi_base_p5,rssi_base_p4,rssi_base_p3,rssi_base_p2,rssi_base_p1,rssi_base_n0,rssi_base_n1,rssi_base_n2,rssi_base_n3,rssi_base_n4,rssi_base_n5] = self.wifi.rxresult(result_data)
            else:
                [DesirePackNum, gain, rssi, noise, err, err2,freqoff, rssi_min, rssi_max] = self.wifi.rxresult(result_data)
            perform_list.append((rfpwr,DesirePackNum,rssi,gain,noise,err,err2));
            loginfo(result_data)
            if rssi_data_base_en == 1:
                csvreport1.write_data([rx_chan,ht40_index,tx_freq,rfpwr,DesirePackNum,rssi,gain,noise,err,err2,freqoff, rssi_min, rssi_max,rssi_base_p5,rssi_base_p4,rssi_base_p3,rssi_base_p2,rssi_base_p1,rssi_base_n0,rssi_base_n1,rssi_base_n2,rssi_base_n3,rssi_base_n4,rssi_base_n5])
            else:
                csvreport1.write_data([rx_chan,ht40_index,tx_freq,rfpwr,DesirePackNum,rssi,gain,noise,err,err2,freqoff, rssi_min, rssi_max])
            if print_err_code==1:
                result_data = result_data.replace('#', '\n')
                csvreport1.write_string(result_data)

            rfpwr=rfpwr+pwr_step

            mytester.set_pwr(rfpwr,0,iqv_no,'source');

            if break_en==1:
                if maxlevel_en==1 and DesirePackNum <= 10:
                    break
                elif maxlevel_en==0 and DesirePackNum >= 100:
                    break

        [cur_sense, cur_sense_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find, perform_list] = self.get_data_sens(packnum, perform_list)

        mytester.gen_switch('OFF',iqv_no);

        logsetlevel("D")

        return [cur_sense, cur_sense_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find, perform_list];


    def WIFI_RX_per_freq_offset(self, cable_lose=13,rx_chan=11,tx_chan=11, rx_rate='mcs6', minpwr=-80, maxpwr=-30,pwr_step =1, packnum=100, iqv_no=1,name_str=''):
        """
        :test RX performance
        """
        print_err_code = 0

##        logsetlevel("I")

        name_str_local = '%s_%s_%s_%s_%s'%(rx_chan, rx_rate, minpwr, maxpwr,name_str)
        title = 'rx_chan, rfpwr,freq_offset, rxnum, rssi, gain, noise, err, fcs, freq, rssi_min, rssi_max\n'
        fname = self.wifi.get_filename('wifi_txrx_test_%s'%name_str, 'RX_%s'%name_str_local, 'rx')
        csvreport1 = csvreport(fname, title)

        self.wifi.cmdstop()
        self.wifiapi.rssi_min_max_print()
        for freq_offset in range (-100,110,10):
            if freq_offset<0:
                freq_offset_s = freq_offset+655365
##                freq_offset_s = freq_offset+655360
            else:
                freq_offset_s = freq_offset
            loginfo(freq_offset)
            self.wifi.rfchsel_offset_esp32(freq_offset)


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

            if rx_rate=="test":
                ratenum = rate_dict["mcs7"]
                cbw40m = self.wifi.rate2ht40("mcs7")

            else:
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

            while rfpwr<=maxpwr:
                mytester.sigout(tx_freq,rfpwr,cable_lose,rx_rate,packnum,iqv_no)
                if rx_rate=="test":
                    self.wifi.rxstart("mcs7", print_err_code)
        ##            wifi.esp_rx(rx_chan, rx_rate)
                else:
                    self.wifi.rxstart(rx_rate, print_err_code)
                mytester.trig_wave(iqv_no);
                time.sleep(0.1)
                result_data = self.wifi.cmdstop()

                [DesirePackNum, gain, rssi, noise, err, err2,freqoff, rssi_min, rssi_max] = self.wifi.rxresult(result_data)

                perform_list.append((rfpwr,freq_offset,DesirePackNum,rssi,gain,noise,err,err2));
                loginfo(result_data)
                csvreport1.write_data([rx_chan,rfpwr,freq_offset,DesirePackNum,rssi,gain,noise,err,err2, rssi_min, rssi_max])

                if print_err_code==1:
                    result_data = result_data.replace('#', '\n')
                    csvreport1.write_string(result_data)

                rfpwr=rfpwr+pwr_step;
                mytester.set_pwr(rfpwr,0,iqv_no,'source');

        [cur_sense, cur_sense_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find, perform_list] = self.get_data_sens(packnum, perform_list)

        mytester.gen_switch('OFF',iqv_no);

##        logsetlevel("D")

        return [cur_sense, cur_sense_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find, perform_list];


    def WIFI_RX_sens(self, cable_lose=13, chan_in=[1], data_rate=['mcs7'],packnum=100,loop_num=1,iqv_no=1,name_str=''):
        title = 'test_number,rate,'
        for chan in chan_in:
            title += 'sens chan%d,'%chan
        for chan in chan_in:
            title += 'sens_rssi chan%d,'%chan
        title += '\n'

        fname = self.wifi.get_filename('wifi_txrx_test_%s'%name_str, 'RXSens_%s'%name_str)
        csvreport2 = csvreport(fname, title)

        for loop in range(1,loop_num+1):
            plt.figure()
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
                    minpwr = rate_sens - 2
                    maxpwr = rate_sens + 10
                    loginfo('minpwr=%d, maxpwr=%d'%(minpwr,maxpwr))

                    [cur_sens, cur_sens_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find,per_list] = self.WIFI_RX_per(cable_lose,rx_chan,tx_chan,cur_rate,minpwr,maxpwr,1,packnum,iqv_no,name_str, 1)

                    cur_sens_list.append(cur_sens)
                    cur_sens_rssi_list.append(cur_sens_rssi)
                csvreport2.write_data([loop,cur_rate,cur_sens_list,cur_sens_rssi_list])

                plt.plot(chan_in,cur_sens_list,label='%s'%(cur_rate))

            self.show_figure(xlabel='Channel', ylabel='RX Sensitivity(dBm)', ylim=[-110, -60], fname=fname)

    def show_figure(self, xlabel='', ylabel='', ylim=[0,100], fname=''):
        filetime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend(loc=4)
        plt.ylim(ylim[0], ylim[1])
        plt.grid()
        title = fname.split('/')
        title = title[-1]+'_%s'%filetime
        plt.title(title)
        figname =fname+'_%s.png'%filetime
        plt.savefig(figname)
##        plt.show()


    def WIFI_RX_maxlevel(self, cable_lose=13, chan_in=[1], data_rate=['mcs7'], iqv_no=1,name_str=''):
        title = 'rate,'
        for chan in chan_in:
            title += 'max_level chan%d,'%chan
        for chan in chan_in:
            title += 'max_rssi chan%d,'%chan
        title += '\n'

        fname = self.wifi.get_filename('wifi_txrx_test_%s'%name_str, 'RXMaxLevel_%s'%name_str)
        csvreport2 = csvreport(fname, title)

        packnum=100

        for cur_rate in data_rate:
            maxlevel = maxleve_dict[cur_rate]
            minpwr = -10 #maxlevel - 10
            maxpwr = 5  #maxlevel + 5
            loginfo('minpwr=%d, maxpwr=%d'%(minpwr,maxpwr))
            max_level = []
            max_level_rssi = []
            for i in range(0, len(chan_in)):
                chan_no = chan_in[i]
                rx_chan = chan_no
                tx_chan = chan_no

                loginfo('chan=%d'%chan_no)

                [cur_sens, cur_sens_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find,per_list] = self.WIFI_RX_per(cable_lose,rx_chan,tx_chan,cur_rate,minpwr,maxpwr,1,packnum,iqv_no,name_str,1,1)
                max_level.append(cur_max)
                max_level_rssi.append(cur_max_rssi)
            csvreport2.write_data([cur_rate, max_level, max_level_rssi])

            plt.plot(chan_in,max_level,label='%s'%(cur_rate))

        self.show_figure(xlabel='Channel', ylabel='RX MAX Level (dBm)', ylim=[-30, 20], fname=fname)


    def WIFI_RX_range(self,cable_lose=2, chan_in=[1], data_rate=['mcs7'], rx_range=[], iqv_no=1, plot_en=1,name_str=''):

        title = 'channel, rate,minpwr, maxpwr, sens, sens_rssi, sens_find, cur_max, cur_max_rssi, cur_max_find\n'
        fname = self.wifi.get_filename('wifi_txrx_test_%s'%name_str, 'RXRange_%s'%name_str)
        csvreport2 = csvreport(fname, title)
        packnum=100

        for i in range(0, len(chan_in)):
            for j in range(0,len(data_rate)):
                cur_rate = data_rate[j]
                chan_no = chan_in[i]
                rx_chan = chan_no
                tx_chan = chan_no
                print rx_range
                if rx_range==[]:
                    rate_sens = sens_dict[cur_rate]
                    print cur_rate
                    print rate_sens
                    minpwr = rate_sens - 2
                    maxpwr = 0
                else:
                    rssi_range = rx_range[j]
                    rssi_range = rssi_range.replace('[','').replace(']','')
                    rssi_range = rssi_range.split(',')
                    print rssi_range
                    minpwr = int(rssi_range[0], 10)
                    maxpwr = int(rssi_range[1], 10)

                print 'minpwr=%d, maxpwr=%d'%(minpwr,maxpwr)
                print 'chan=%d'%chan_no

                [cur_sens, cur_sens_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find,per_list] = self.WIFI_RX_per(cable_lose,rx_chan,tx_chan,cur_rate,minpwr,maxpwr,1,packnum,iqv_no,name_str)

                csvreport2.write_data([chan_no,cur_rate,minpwr,maxpwr,cur_sens, cur_sens_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find])

                [suc_num, rx_rssi] = self.get_rx_data(per_list)

##                label = 'chan%d,%s'%(chan_no,cur_rate)
##                plot1 = plt.plot(rx_rssi,suc_num, label=label)
##
##        self.show_figure(xlabel='RX RSSI', ylabel='RX Success Rate %', ylim=[-10,110], fname=fname)..


    def WIFI_HT40_RX_range(self, cable_lose=13, chan_in=[1], data_rate=['mcs7'], rx_range_max= 0, iqv_no=1, plot_en=1,name_str=''):

        title = 'channel,ht40_index,rx_chan,rate,minpwr, maxpwr, sens, sens_rssi, sens_find, cur_max, cur_max_rssi, cur_max_find\n'
        fname = self.wifi.get_filename('wifi_txrx_test_%s'%name_str, 'HT40_RXRange_%s'%name_str)
        csvreport2 = csvreport(fname, title)
        packnum=100

        for i in range(0, len(chan_in)):
            for j in range( 0,len(data_rate)):
                cur_rate = data_rate[j]
                chan_no = chan_in[i]
                rx_chan = chan_no
                tx_chan = chan_no
                freq = self.wifi.chan2freq(tx_chan)

                rate_sens = sens_dict[cur_rate]
                print cur_rate
                print rate_sens
##                minpwr = rate_sens - 2
                minpwr = -30
                maxpwr = rx_range_max

                print 'minpwr=%d, maxpwr=%d'%(minpwr,maxpwr)
                print 'chan=%d'%chan_no
                for ht40_index in range(2,3):
                    if ht40_index == 2:
                        freq -=10;
                    if ht40_index ==3:
                        freq+= 10;
                    if freq < 2412 or  freq > 2472:
                        chan_test = freq
                    else:
                        chan_test = self.wifi.freq2chan(freq)

                    [cur_sens, cur_sens_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find,per_list] = self.WIFI_RX_per(cable_lose,rx_chan,tx_chan,cur_rate,minpwr,maxpwr,1,packnum,iqv_no,name_str,ht40_index=ht40_index)

                    csvreport2.write_data([chan_no,ht40_index,chan_test,cur_rate,minpwr,maxpwr,cur_sens, cur_sens_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find])

                    [suc_num, rx_rssi] = self.get_rx_data(per_list)

    def WIFI_RX_range_Radition(self, chan_in=[1], data_rate=['mcs7'], rx_range=[], iqv_no=1, plot_en=1,name_str=''):

            title = 'channel, rate,minpwr, maxpwr, sens, sens_rssi, sens_find, cur_max, cur_max_rssi, cur_max_find\n'
            fname = self.wifi.get_filename('wifi_txrx_test_%s'%name_str, 'RXRange_%s'%name_str)
            csvreport2 = csvreport(fname, title)
            packnum=100
            cable_list = self.wifi.get_rx_cable_lost(iqv_no,chan_in)
            for i in range(0, len(chan_in)):
                for j in range(0,len(data_rate)):
                    cur_rate = data_rate[j]
                    chan_no = chan_in[i]
                    rx_chan = chan_no
                    tx_chan = chan_no
                    print rx_range
                    cable_lose=cable_list[i-1]
                    loginfo("rate=%s, channel=%d,cable_lose=%2.2f"%(cur_rate, chan_no,cable_lose))
                    if rx_range==[]:
                        rate_sens = sens_dict[cur_rate]
                        print cur_rate
                        print rate_sens
                        minpwr = rate_sens - 2
                        maxpwr = 0
                    else:
                        rssi_range = rx_range[j]
                        rssi_range = rssi_range.replace('[','').replace(']','')
                        rssi_range = rssi_range.split(',')
                        print rssi_range
                        minpwr = int(rssi_range[0], 10)
                        maxpwr = int(rssi_range[1], 10)

                    print 'minpwr=%d, maxpwr=%d'%(minpwr,maxpwr)
                    print 'chan=%d'%chan_no

                    [cur_sens, cur_sens_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find,per_list] = self.WIFI_RX_per(cable_lose,rx_chan,tx_chan,cur_rate,minpwr,maxpwr,1,packnum,iqv_no,name_str)

                    csvreport2.write_data([chan_no,cur_rate,minpwr,maxpwr,cur_sens, cur_sens_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find])

                    [suc_num, rx_rssi] = self.get_rx_data(per_list)

    def FLASH_TEST(self,iqv_no=2,clk=[1,2,4],div=[0,1,2,3],mode=[0,1,2]):
        '''
        clk:
            1:80M, 2,40M, 4 ,20M;
        div:
            0,1,2,3 flash driver, 0: the lest,  1: the most
        mode:
            0: 2 SPI Lins,
            1: 4 SPI Lines
        '''
        cable_list=self.wifi.get_rx_cable_lost(iqv_unit_no=iqv_no, cable_att=30, chan_m=[1,2,3,4,5,6,7,8,9,10,11,12,13,14],noise_ref=-95.2)
        for ck in clk:
            for dv in div:
                for mo in mode:
                    loginfo(("ck=%d,dv=%d,mo=%d")%(ck,dv,mo))
                    self.wifiapi.flash_test_init(ck,dv,mo)
                    self.WIFI_RX_range_Radition(cable_list=cable_list,chan_in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14], data_rate=['mcs7','1m'], rx_range=['[-73, -50]','[-98,-50]'], iqv_no=iqv_no,plot_en=0,name_str='clk=%d_div=%d,mo=%d'%(ck,dv,mo))
                    self.WIFI_TX_PWR_EVM_Radition(cable_lose_list=cable_list, channel=[1,2,3,4,5,6,7,8,9,10,11,12,13,14], data_rate=['mcs7','1m'],iqv_no=iqv_no,iqv_num=20, force_txon=0,name_str='clk=%d_div=%d,mo=%d'%(ck,dv,mo))
        self.wifiapi.flash_test_enable(0)
        self.WIFI_RX_range_Radition(cable_list=cable_list,chan_in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14], data_rate=['mcs7','1m'], rx_range=['[-73, -50]','[-98,-50]'], iqv_no=iqv_no,plot_en=0,name_str='flash_off')
        self.WIFI_TX_PWR_EVM_Radition(cable_lose_list=cable_list, channel=[1,2,3,4,5,6,7,8,9,10,11,12,13,14], data_rate=['mcs7','1m'],iqv_no=iqv_no,iqv_num=20, force_txon=0,name_str='flash_off')

    def WIFI_RX_range_filter_gain(self, cable_lose=13, chan_in=[1], data_rate=['mcs7'], rx_range=['[-60, -20]'], filter_dcap_range=range(15,65), rxgain_range=range(35,60), iqv_no=1,name_str=''):

        title = 'channel, rate, minpwr, maxpwr, filter_dcap, rxgian, sens, sens_rssi, sens_find, cur_max, cur_max_rssi, cur_max_find\n'
        fname = self.wifi.get_filename('%s'%name_str, 'RX_range_filter_gain_%s'%name_str)
        csvreport2 = csvreport(fname, title)

##        packnum=100

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
                for filter_dcap in filter_dcap_range:
                    for rxgain in rxgain_range:
                        self.wifi.rx_force_gain(1,rxgain)

                        [cur_sens, cur_sens_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find,per_list] = self.WIFI_RX_per(cable_lose,rx_chan,tx_chan,cur_rate,minpwr,maxpwr,1,packnum,iqv_no,filter_dcap)

                        csvreport2.write_data([chan_no,cur_rate,minpwr,maxpwr, filter_dcap, rxgain, cur_sens, cur_sens_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find])



    def WIFI_RX_range_rxiq(self, cable_lose=13, chan_in=[1], data_rate=['mcs7'], rx_range=['[-60, -20]'], iq_amp=range(-7,32), iq_phase=range(-4,16), iqv_no=1,name_str=''):

        title = 'channel, rate, minpwr, maxpwr, iq_amp, iq_phase, rxgian, sens, sens_rssi, sens_find, cur_max, cur_max_rssi, cur_max_find\n'
        fname = self.wifi.get_filename('%s'%name_str, 'RX_range_rxiq_%s'%name_str)
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

                for amp in iq_amp:
                    #for phase in iq_phase:
                    self.wifi.rxiq_set(1,amp,-4)

                    [cur_sens, cur_sens_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find,per_list] = self.WIFI_RX_per(cable_lose,rx_chan,tx_chan,cur_rate,minpwr,maxpwr,1,packnum,iqv_no,'Amp_'+str(amp))

                    csvreport2.write_data([chan_no,cur_rate,minpwr,maxpwr, amp, -4, cur_sens, cur_sens_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find])





    def wifi_test(self, test_flag=0xf, cable_lose_in=0, unit_no_in=0, name_str=''):
        # load RF setting

        self.wifi.cmdstop()
        [cable_lose, unit_no, temperature, tx_channel, tx_rate, rx_channel, rx_rate, rxm_channel, rxm_rate, rxd_channel, rxd_rate, rxd_range] = self.get_rf_setting()

        if cable_lose_in>0:
            cable_lose = cable_lose_in

        if unit_no_in>0:
            unit_no = unit_no_in

        # RF test list
        self.wifi.save_init_print('wifi_txrx_test_%s'%name_str)


        if (test_flag & 0x1) > 0:
            for i in range(0,11):

                self.WIFI_TX_PWR_EVM(cable_lose=cable_lose, channel=tx_channel, data_rate=tx_rate, iqv_no=unit_no, iqv_num=150,force_txon=0,name_str="wifitxout_%s"%name_str)
##            self.WIFI_TX_PWR_EVM(cable_lose=cable_lose, channel=tx_channel, data_rate=tx_rate, iqv_no=unit_no, iqv_num=50,force_txon=1,name_str="esp_tx_%s"%name_str)

        if (test_flag & 0x2) > 0:
            self.WIFI_RX_sens(cable_lose=cable_lose, chan_in=rx_channel, data_rate=rx_rate,iqv_no=unit_no,name_str=name_str)

        if (test_flag & 0x4) > 0:
            self.WIFI_RX_maxlevel(cable_lose=cable_lose, chan_in=rxm_channel,data_rate=rxm_rate,iqv_no=unit_no,name_str=name_str)

        if (test_flag & 0x8) > 0:
            self.WIFI_RX_range(cable_lose=cable_lose, chan_in=rxd_channel, data_rate=rxd_rate, rx_range=rxd_range, iqv_no=unit_no,name_str=name_str)


    def rx_test_tmp(self):
        logsetlevel("D")
        self.wifiapi.rxstart(0x17)
        wifi_instrum.instru_tx_signal(tx_pwr=-40, tx_rate='mcs7', cable_lose=10, iqv_no=2)
        self.wifi.cmdstop()

    def Wifi_test_uart_issue(self,cable_lose=0,iqv_no=0,name_str=''):
        self.wifiapi.uart_test_enable(0)
##
        self.wifi_test(test_flag=1, cable_lose_in=cable_lose, unit_no_in=iqv_no, name_str=name_str + '_uart_off')
        self.wifi_test(test_flag=8,cable_lose_in=cable_lose, unit_no_in=iqv_no, name_str=name_str + '_uart_off')

        self.wifiapi.uart_test_enable(1)
        self.wifi_test(test_flag=1, cable_lose_in=cable_lose, unit_no_in=iqv_no, name_str=name_str + '_uart_on')
        self.wifi_test(test_flag=8, cable_lose_in=cable_lose, unit_no_in=iqv_no, name_str=name_str + '_uart_on')




