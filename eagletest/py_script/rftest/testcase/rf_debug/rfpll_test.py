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
from baselib.instrument.spa import HP,Agilent
from baselib.instrument import dm
from hal.rtc_debug import RTC_DEBUG
from rftest.rflib.rfcal import rfcal

from hal.adc import RTC_ADC2


rate_bps_dict = rfglobal.rate_bps_dict
sens_dict = rfglobal.sens_dict
rate_dict = rfglobal.ratedic
maxleve_dict = rfglobal.rx_maxlevel_dict


class RFPLL_TEST(object):

    def __init__(self,comport,chipv='ESP32', name_str=''):
        self.comport = comport
        self.chipv = chipv
        self.mem = MEM(self.comport,self.chipv)
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.wifiapi = WIFIAPI(self.comport,self.chipv)
        self.rfpll = rfpll(self.comport,self.chipv)
        self.rfcal = rfcal(self.comport,self.chipv)
        self.i2c = HWI2C(self.comport,self.chipv)
        self.pbus = pbus(self.comport,self.chipv)
        self.rtc_debug = RTC_DEBUG(self.comport,self.chipv)
        self.rtc_adc2 = RTC_ADC2(self.comport,self.chipv)
        self.name_str=name_str

    def rfpll_dac_evm(self, cable_lose=2, iqv_no=1,iqv_num=10,name_str=''):
        """
        :test TX power and EVM
        :cable_lost:
        :channle: it is matrix [1,...]
        :data_rate: it is matrix ['mcs0',...]
        :iqv_no: 1-left port, 2-right port
        :iqv_num: iqview average number
        """
        filetime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()));
        title = 'channel,rate,ir_dac_ext, ir_cap_ext, or_ampl, or_amph, ent_vco_bias_vol,ent_vco_bias_dm, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage(dB),iq_imb_amp(dB),iq_imb_phase(deg),evm_list\n'
        fname = self.wifi.get_filename('rfpll_dac_evm_%s'%name_str, 'rfpll_dac_evm_%s'%name_str)
        csvreport1 = csvreport(fname, title)

        self.wifiapi.pll_cap_track_en(0)
        self.wifiapi.txpwr_track_en(0,0,0)
        self.wifi.cmdstop()
        max_pwr = 25 - cable_lose

        rate = 'mcs7'
        backoff = 0
        for chan in [1]:
            cbw40m = self.wifi.rate2ht40(rate)
            test_para = wifi_instrum.test_para(rate)

            if chan<=14:
                freq = self.wifi.chan2freq(chan)
                self.wifiapi.rfchsel(chan, 0)
            else:
                freq = chan
                self.wifiapi.rfchsel(1,0)
                self.wifiapi.phy_set_freq(freq)

            if self.chipv == 'CHIP724':
                self.wifiapi.set_tx_gain(0x5e,0x20)
                self.wifiapi.set_tx_dig_gain(1,(256-10)) #256-bk
                self.wifi.i2c.bias.dreg_2p2 = 0

            [len_byte, frm_delay] = self.wifi.get_length_delay_duty(rate, 0.1, 500)
            self.wifi.txout(rate, 0, PackLen=len_byte, backoff_qdb=backoff, frm_delay=frm_delay)
            myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0, 0)
            for dac_ext in range(0,16):
                self.i2c.rfpll.ir_dac_ext = dac_ext
                self.wifiapi.pll_vol_cal()


                for i in range(0,1):
                    self.wifi.txout(rate, 0, PackLen=len_byte, backoff_qdb=backoff, frm_delay=frm_delay)

                    [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 1,'false', -15)
                    if evm < -5:
                        [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false', -15)

                    ir_cap_ext = self.i2c.rfpll.ir_cap_ext

                    ir_dac_ext = self.i2c.rfpll.ir_dac_ext
                    or_ampl = self.i2c.rfpll.or_ampl
                    or_amph = self.i2c.rfpll.or_amph
                    sar2_code = self.wifiapi.get_pll_vol()
                    vco_bias_vol = 0
                    vco_bias_dm = 0

                    csvreport1.write_data([chan, rate,ir_dac_ext, ir_cap_ext, or_ampl, or_amph, sar2_code,vco_bias_dm, pwr, evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase, evm_list])
                    print [chan,ir_dac_ext, ir_cap_ext, or_ampl, or_amph,sar2_code,vco_bias_dm, rate,pwr,evm,evm_std,evm_max]

    def rfpll_cap_evm(self, cable_lose=2, iqv_no=1,iqv_num=10, test_vol=0, name_str=''):
        """
        :test TX power and EVM
        :cable_lost:
        :channle: it is matrix [1,...]
        :data_rate: it is matrix ['mcs0',...]
        :iqv_no: 1-left port, 2-right port
        :iqv_num: iqview average number
        """
        filetime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()));
        title = 'channel,rate,ir_enx_cap,pll_cap_org,ir_cap_ext,or_pll_cap, or_capl, or_caph, test_num, cgm_code,ent_vco_bias_vol,ent_vco_bias_dm, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage(dB),iq_imb_amp(dB),iq_imb_phase(deg),evm_list\n'
        fname = self.wifi.get_filename('rfpll_cap_evm_%s'%name_str, 'rfpll_cap_evm_%s'%name_str)
        csvreport1 = csvreport(fname, title)

        rfglobal.iqv['evm_sorted'] = 1
        if test_vol==1:
            vv = dm.dm()

        self.wifiapi.pll_cap_track_en(0)
        self.wifiapi.txpwr_track_en(0,0,0)
        self.wifi.cmdstop()
        max_pwr = 25 - cable_lose

        rate = 'mcs7'
        backoff = 0
        for chan in range(1,15, 5): #[1,14]:
            cbw40m = self.wifi.rate2ht40(rate)
            test_para = wifi_instrum.test_para(rate)

            if chan<=14:
                freq = self.wifi.chan2freq(chan)
                self.wifiapi.rfchsel(chan, 0)
            else:
                freq = chan
                self.wifiapi.rfchsel(1,0)
                self.wifiapi.phy_set_freq(freq)
            if self.chipv == "CHIP724":
                self.wifiapi.set_tx_gain(0x5e, 0x20)
                self.wifiapi.set_tx_dig_gain(1,(256-12)) #256-bk

            elif self.chipv == "CHIP723":
                self.wifiapi.set_tx_gain(0x4f, 0x60)
                self.wifiapi.set_tx_dig_gain(1,(256-12)) #256-bk

            [len_byte, frm_delay] = self.wifi.get_length_delay_duty(rate, 0.2)
            self.wifi.txout(rate, 0, PackLen=len_byte, backoff_qdb=backoff, frm_delay=frm_delay)
            myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0, 0)

            pll_cap_org = self.i2c.rfpll.ir_cap_ext
            ir_enx_cap = self.i2c.rfpll.ir_enx_cap

            for cap_ext in range(pll_cap_org-2, pll_cap_org+4):
                self.i2c.rfpll.ir_cap_ext = cap_ext

                for i in range(0,1):
                    self.wifi.txout(rate, 0, PackLen=len_byte, backoff_qdb=backoff, frm_delay=frm_delay)

                    [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 1,'false', -15)
                    if evm < -5:
                        [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false', -15)

                    self.wifiapi.get_pll_vol()
                    ir_cap_ext = self.i2c.rfpll.ir_cap_ext
                    or_pll_cap = self.i2c.rfpll.or_pll_cap
                    or_capl = self.i2c.rfpll.or_capl
                    or_caph = self.i2c.rfpll.or_caph
                    self.i2c.rfpll.ent_vco_bias=1
                    self.i2c.rfpll.dtest=1

                    if self.chipv == "CHIP724":
                        sar2_code = self.wifiapi.get_sar2_vol(3)
                    else:
                        sar2_code = self.wifiapi.get_sar2_vol(2)
                    self.i2c.rfpll.ent_vco_bias=0
                    self.i2c.rfpll.dtest=0
                    self.i2c.bias.ent_cgm=1
                    self.i2c.bias.dtest=1
                    if self.chipv == "CHIP724":
                        cgm_code = self.wifiapi.get_sar2_vol(3)
                    else:
                        cgm_code = self.wifiapi.get_sar2_vol(2)

                    self.i2c.bias.ent_cgm=1
                    self.i2c.bias.dtest=1
                    ent_cgm_code = self.wifiapi.get_sar2_vol(3)
                    self.i2c.bias.ent_cgm=0
                    self.i2c.bias.dtest=0
                    vco_bias_vol = 0
                    vco_bias_dm = 0

                    if test_vol==1:
                        self.rtc_adc2.config()
                        self.rtc_adc2.set(pad = 1)
                        self.i2c.rfpll.ent_vco_bias=1
                        self.i2c.rfpll.dtest=1
                        self.rtc_debug.pull_internal_voltage(1)
##                        vco_bias_dm = vv.get_result('VDC')
                        self.mem.wrm(0x60008834, 31, 31, 0) # SAR2_RTC_force
                    csvreport1.write_data([chan, rate,ir_enx_cap, pll_cap_org, ir_cap_ext,or_pll_cap, or_capl, or_caph, i,cgm_code,sar2_code,vco_bias_dm, pwr, evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase, evm_list])
                    print [chan,ir_enx_cap,pll_cap_org,ir_cap_ext,or_pll_cap,or_capl, or_caph,cgm_code,sar2_code,vco_bias_dm, rate,pwr,evm,evm_std,evm_max]

##                self.i2c.rfpll.ir_cap_ext = pll_cap_org
##                return[j,ir_enx_cap,pll_cap_org,ir_cap_ext,or_pll_cap,or_capl, or_caph,cgm_code,sar2_code,vco_bias_dm, rate,pwr,evm,evm_std,evm_max]
            rfglobal.iqv['evm_sorted'] = 0

    def rfpll_cap_evm_target_pwr(self, cable_lose=2, iqv_no=1,iqv_num=10, test_vol=0, name_str=''):
        """
        :test TX power and EVM
        :cable_lost:
        :channle: it is matrix [1,...]
        :data_rate: it is matrix ['mcs0',...]
        :iqv_no: 1-left port, 2-right port
        :iqv_num: iqview average number
        """
        filetime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()));
        title = 'channel,rate,DREG, ir_enx_cap,pll_cap_org,ir_cap_ext,or_pll_cap, or_capl, or_caph, test_num, cgm_code,ent_vco_bias_vol,ent_vco_bias_dm, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage(dB),iq_imb_amp(dB),iq_imb_phase(deg),evm_list\n'
        fname = self.wifi.get_filename('rfpll_cap_evm_%s'%name_str, 'rfpll_cap_evm_%s'%name_str)
        csvreport1 = csvreport(fname, title)


        rfglobal.iqv['evm_sorted'] = 1
        if test_vol==1:
            vv = dm.dm()

        self.wifiapi.pll_cap_track_en(0)
        self.wifiapi.txpwr_track_en(0,0,0)
        self.wifi.cmdstop()
        max_pwr = 25 - cable_lose
        rate = 'mcs7'
        backoff = 0
        for chan in range(6,15, 14): #[1,14]:
            cbw40m = self.wifi.rate2ht40(rate)
            test_para = wifi_instrum.test_para(rate)

            if chan<=14:
                freq = self.wifi.chan2freq(chan)
                self.wifiapi.rfchsel(chan, 0)

            else:
                freq = chan
                self.wifiapi.rfchsel(1,0)
                self.wifiapi.phy_set_freq(freq)
##            if self.chipv == "CHIP724":
            for j in range(7,16,8):
##                    self.i2c.bias.dreg_2p2 = j
##                self.i2c.bias.cp1p6_dreg = j
                self.i2c.bias.cp1p2_dreg = j
                self.wifiapi.pll_vol_cal()

                [iq_amp,iq_phase] = self.rfcal.txiq_cal(cable_lose=cable_lose,iqv_no=iqv_no)

                tt_min = 0
                tt_max = 2
                target_power = 13
                dig_atten =12
                self.wifiapi.rfchsel(chan, 0)

                for tt in range(tt_min,tt_max):
                    if tt == (tt_max -1):
                        iqv_num = 10
                    loginfo('dig_atten=%d'%dig_atten)
                    if self.chipv=="CHIP723":
                        self.wifiapi.set_tx_gain(0x4f, 0x60)
                    if self.chipv =="CHIP724":
                        self.wifiapi.set_tx_gain(0x5e, 0x20)

                    self.wifiapi.set_tx_dig_gain(1,(256-12)) #256-bk

                    self.wifi.cmdstop()
                    cbw40m = self.wifi.rate2ht40(rate)

                    [len_byte, frm_delay] = self.wifi.get_length_delay_duty(rate,0.2)
                    self.wifi.txout(rate_sym=rate, PackNum=0, PackLen =len_byte, cbw40=cbw40m, ht_dup=0, backoff_qdb=0, frm_delay=frm_delay)
                    myiqv = tester.tester(freq, max_pwr, rate, wifi_instrum.test_para(rate), iqv_no,'measure', cable_lose, 10, 0,1,20)
                    wifi_instrum.iqv_avg(myiqv, 10,'false')

                    self.wifi.cmdstop()
                    iqv = rfglobal.iqv
                    pwr = iqv['pwr']
                    print 'power=%2.2f'%pwr
                    if tt < (tt_max - 1):
                        dig_atten += (pwr - target_power)*4

                self.wifiapi.set_tx_dig_gain(1,(256-dig_atten)) #256-bk
                self.wifi.txiq_set(1,iq_amp,iq_phase)
                pll_cap_org = self.i2c.rfpll.ir_cap_ext
                ir_enx_cap = self.i2c.rfpll.ir_enx_cap
                [len_byte, frm_delay] = self.wifi.get_length_delay_duty(rate,0.2)
                for cap_ext in range(pll_cap_org-2, pll_cap_org+8):
                    self.i2c.rfpll.ir_cap_ext = cap_ext


                    for i in range(0,1):

                        self.wifi.txout(rate, 0, PackLen=len_byte, backoff_qdb=backoff, frm_delay=frm_delay)

                        [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 1,'false', -15)
                        if evm < -5:
                            [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false', -15)

                        self.wifiapi.get_pll_vol()
                        ir_cap_ext = self.i2c.rfpll.ir_cap_ext
                        or_pll_cap = self.i2c.rfpll.or_pll_cap
                        or_capl = self.i2c.rfpll.or_capl
                        or_caph = self.i2c.rfpll.or_caph
                        self.i2c.rfpll.ent_vco_bias=1
                        self.i2c.rfpll.dtest=1

                        if self.chipv == "CHIP724":
                            sar2_code = self.wifiapi.get_sar2_vol(3)
                        else:
                            sar2_code = self.wifiapi.get_sar2_vol(2)
                        self.i2c.rfpll.ent_vco_bias=0
                        self.i2c.rfpll.dtest=0

                        self.i2c.bias.ent_cgm=1
                        self.i2c.bias.dtest=1
                        if self.chipv == "CHIP724":
                            cgm_code = self.wifiapi.get_sar2_vol(3)
                        else:
                            cgm_code = self.wifiapi.get_sar2_vol(2)
                        self.i2c.bias.ent_cgm=0
                        self.i2c.bias.dtest=0
                        vco_bias_vol = 0
                        vco_bias_dm = 0

                        if test_vol==1:
                            self.rtc_adc2.config()
                            self.rtc_adc2.set(pad = 1)
                            self.i2c.rfpll.ent_vco_bias=1
                            self.i2c.rfpll.dtest=1
                            self.rtc_debug.pull_internal_voltage(1)
                            vco_bias_dm = vv.get_result('VDC')
                            self.mem.wrm(0x60008834, 31, 31, 0) # SAR2_RTC_force

                        csvreport1.write_data([chan, rate,j,ir_enx_cap, pll_cap_org, ir_cap_ext,or_pll_cap, or_capl, or_caph, i,cgm_code,sar2_code,vco_bias_dm, pwr, evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase, evm_list])
                        print [chan,j,ir_enx_cap,pll_cap_org,ir_cap_ext,or_pll_cap,or_capl, or_caph,cgm_code,sar2_code,vco_bias_dm, rate,pwr,evm,evm_std,evm_max]

            rfglobal.iqv['evm_sorted'] = 0

    def rfpll_dac_evm_target_pwr(self, cable_lose=2, iqv_no=1,iqv_num=10, test_vol=0, name_str=''):
        """
        :test TX power and EVM
        :cable_lost:
        :channle: it is matrix [1,...]
        :data_rate: it is matrix ['mcs0',...]
        :iqv_no: 1-left port, 2-right port
        :iqv_num: iqview average number
        """
        filetime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()));
        title = 'channel,rate,DREG_Val, ir_dac_ext,ir_cap_ext,or_pll_cap, or_capl, or_caph, test_num, cgm_code,ent_vco_bias_vol,ent_vco_bias_dm, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage(dB),iq_imb_amp(dB),iq_imb_phase(deg),evm_list\n'
        fname = self.wifi.get_filename('rfpll_cap_evm_%s'%name_str, 'rfpll_cap_evm_%s'%name_str)
        csvreport1 = csvreport(fname, title)


        rfglobal.iqv['evm_sorted'] = 1
        if test_vol==1:
            vv = dm.dm()

        self.wifiapi.pll_cap_track_en(0)
        self.wifiapi.txpwr_track_en(0,0,0)
        self.wifi.cmdstop()
        max_pwr = 25 - cable_lose
        rate = 'mcs7'
        backoff = 0
        for chan in range(1,15, 14): #[1,14]:
            cbw40m = self.wifi.rate2ht40(rate)
            test_para = wifi_instrum.test_para(rate)

            if chan<=14:
                freq = self.wifi.chan2freq(chan)
                self.wifiapi.rfchsel(chan, 0)

            else:
                freq = chan
                self.wifiapi.rfchsel(1,0)
                self.wifiapi.phy_set_freq(freq)

##            if self.chipv == "CHIP724":
            for j in range(0,16,2):
                self.i2c.bias.dreg_2p2 = j
##                self.i2c.bias.cp1p6_dreg = j
                self.i2c.bias.cp1p2_dreg = 7
##                self.wifiapi.pll_vol_cal()

                [iq_amp,iq_phase] = self.rfcal.txiq_cal(cable_lose=cable_lose,iqv_no=iqv_no)
##            if self.chipv == "CHIP723":
##                for j in range(0,16,7):
##                    self.i2c.bias.cp1p6_dreg = j
##                    self.wifiapi.pll_vol_cal()
                tt_min = 0
                tt_max = 2
                target_power = 13
                dig_atten =12
                for tt in range(tt_min,tt_max):
                    if tt == (tt_max -1):
                        iqv_num = 10
                    loginfo('dig_atten=%d'%dig_atten)
                    self.wifi.rfchsel(chan,0)
                    if self.chipv=="CHIP723":
                        self.wifiapi.set_tx_gain(0x4f, 0x60)
                    if self.chipv =="CHIP724":
                        self.wifiapi.set_tx_gain(0x5e, 0x20)

                    self.wifiapi.set_tx_dig_gain(1,(256-12)) #256-bk

                    self.wifi.cmdstop()
                    cbw40m = self.wifi.rate2ht40(rate)

                    [len_byte, frm_delay] = self.wifi.get_length_delay_duty(rate,0.2)
                    self.wifi.txout(rate_sym=rate, PackNum=0, PackLen =len_byte, cbw40=cbw40m, ht_dup=0, backoff_qdb=0, frm_delay=frm_delay)
                    myiqv = tester.tester(freq, max_pwr, rate, wifi_instrum.test_para(rate), iqv_no,'measure', cable_lose, 10, 0,0,20)
                    wifi_instrum.iqv_avg(myiqv, 10,'false')

                    self.wifi.cmdstop()
                    iqv = rfglobal.iqv
                    pwr = iqv['pwr']
                    print 'power=%2.2f'%pwr
                    if tt < (tt_max - 1):
                        dig_atten += (pwr - target_power)*4

                self.wifiapi.set_tx_dig_gain(1,(256-dig_atten)) #256-bk
                self.wifi.txiq_set(1,iq_amp,iq_phase)
                [len_byte, frm_delay] = self.wifi.get_length_delay_duty(rate,0.2)
                for dac_ext in range(0,16,1):
                    self.i2c.rfpll.ir_dac_ext = dac_ext
                    self.wifiapi.pll_vol_cal()

                    for i in range(0,1):

                        self.wifi.txout(rate, 0, PackLen=len_byte, backoff_qdb=backoff, frm_delay=frm_delay)

                        [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 1,'false', -15)
                        if evm < -5:
                            [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false', -15)

                        self.wifiapi.get_pll_vol()
                        ir_cap_ext = self.i2c.rfpll.ir_cap_ext
                        ir_dac_ext = self.i2c.rfpll.ir_dac_ext
                        or_capl = self.i2c.rfpll.or_capl
                        or_caph = self.i2c.rfpll.or_caph
                        self.i2c.rfpll.ent_vco_bias=1
                        self.i2c.rfpll.dtest=1

                        if self.chipv == "CHIP724":
                            sar2_code = self.wifiapi.get_sar2_vol(3)
                        else:
                            sar2_code = self.wifiapi.get_sar2_vol(2)
                        self.i2c.rfpll.ent_vco_bias=0
                        self.i2c.rfpll.dtest=0

                        self.i2c.bias.ent_cgm=1
                        self.i2c.bias.dtest=1
                        if self.chipv == "CHIP724":
                            cgm_code = self.wifiapi.get_sar2_vol(3)
                        else:
                            cgm_code = self.wifiapi.get_sar2_vol(2)
                        self.i2c.bias.ent_cgm=0
                        self.i2c.bias.dtest=0
                        vco_bias_vol = 0
                        vco_bias_dm = 0

                        if test_vol==1:
                            self.rtc_adc2.config()
                            self.rtc_adc2.set(pad = 1)
                            self.i2c.rfpll.ent_vco_bias=1
                            self.i2c.rfpll.dtest=1
                            self.rtc_debug.pull_internal_voltage(1)
                            vco_bias_dm = vv.get_result('VDC')
                            self.mem.wrm(0x60008834, 31, 31, 0) # SAR2_RTC_force

                        csvreport1.write_data([chan, rate,j, ir_dac_ext, ir_cap_ext, or_capl, or_caph, i,cgm_code,sar2_code,vco_bias_dm, pwr, evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase, evm_list])
                        print [chan,j,ir_dac_ext,ir_cap_ext,or_capl, or_caph,cgm_code,sar2_code,vco_bias_dm, rate,pwr,evm,evm_std,evm_max]

            rfglobal.iqv['evm_sorted'] = 0



    def get_cal_time(self, result):
        result = result.split(',')
        cal_time = 0
        index = 0
        if len(result) > 50:
            data_first = int(result[2])
            time1 = int(result[-1])/50.0 # resd i2c 50 times
            for i in range(3, 50):
                if (int(result[i]) != data_first):
                    index = i-2
                    cal_time = index*time1
                    break

        return [index,cal_time]

    def rfpll_cal_time(self, name_str=''):
        num_str = ''
        for i in range(1, 50):
            num_str+='%d,'%i
        title = 'index,cal_time,,chan_freq/or_pll_cap,%s\n'%num_str
        fname = self.wifi.get_filename('rfpll_cal_time_%s'%name_str, 'rfpll_cal_time_%s'%name_str)
        csvreport1 = csvreport(fname, title)
        time_max = 0
        for chan_freq in range(12, 73, 5):
            result = self.wifiapi.rfpll_cal_time(chan_freq, 1)
            [index,cal_time] = self.get_cal_time(result)
            if cal_time > time_max:
                time_max = cal_time
            csvreport1.write_string('%d,%2.2f,'%(index,cal_time)+result)
            result = self.wifiapi.rfpll_cal_time(chan_freq, 0)
            result = result.split('\n')
            for result_1 in result:
                if result_1 != '':
                    [index,cal_time] = self.get_cal_time(result_1)
                    if cal_time > time_max:
                        time_max = cal_time
                    csvreport1.write_string('%d,%2.2f,'%(index,cal_time)+result_1+'\n')
        csvreport1.write_string("cal_time_max=%2.2f\n"%time_max)


    def rfpll_cap_evm_unlock(self, cable_lose=2, iqv_no=1,iqv_num=10,dm_en=1,name_str=''):
        """
        :test TX power and EVM
        :cable_lost:
        :channle: it is matrix [1,...]
        :data_rate: it is matrix ['mcs0',...]
        :iqv_no: 1-left port, 2-right port
        :iqv_num: iqview average number
        """
        filetime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()));
        title = 'channel,rate, ir_enx_cap,ir_cap_ext,or_pll_cap, meas_vol,ent_vco_bias_vol, sar2_code, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage(dB),iq_imb_amp(dB),iq_imb_phase(deg),evm_list\n'
        fname = self.wifi.get_filename('rfpll_cap_evm_unlock_%s'%name_str, 'rfpll_cap_evm_unlock_%s'%name_str)
        csvreport1 = csvreport(fname, title)

        if dm_en==1:
            self.mydm = dm.dm()
            self.i2c.rfpll.ent_vco_bias = 1
            self.i2c.rfpll.dtest=1
            self.rtc_debug.pull_internal_voltage(1)

        self.wifiapi.pll_cap_track_en(0)
        self.wifi.cmdstop()
        max_pwr = 25 - cable_lose

        rate = 'mcs7'
        backoff = 0
        for chan in [1,11]:
            cbw40m = self.wifi.rate2ht40(rate)
            test_para = wifi_instrum.test_para(rate)

            if chan<=14:
                freq = self.wifi.chan2freq(chan)
                self.wifiapi.rfchsel(chan, 0)
            else:
                freq = chan
                self.wifiapi.rfchsel(1,0)
                self.rfpll.set_freq(freq)

            [len_byte, frm_delay] = self.wifi.get_length_delay_duty(rate, 0.1, 500)
            self.wifi.txout(rate, 0, PackLen=len_byte, backoff_qdb=backoff, frm_delay=frm_delay)
            myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0, 0)

##            if chan==1:
##                cap_start = 120
##            else:
##                cap_start = 120 #cap_last + 5

            if self.chipv=='CHIP722':
                cap_start = 100
                cap_end = 0
            elif self.chipv=='ESP32':
                cap_start = 160
                cap_end = 60

            cap_last = 0
            evm0_num = 0
            for cap_ext in range(cap_start, cap_end, -1):
                self.i2c.rfpll.ir_cap_ext = cap_ext

                self.wifi.txout(rate, 0, PackLen=len_byte, backoff_qdb=backoff, frm_delay=frm_delay)

                [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 2,'false', -15)
                if evm < -28:
                    [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 20,'false', -15)
                ir_cap_ext = self.i2c.rfpll.ir_cap_ext
                ir_enx_cap = self.i2c.rfpll.ir_enx_cap
                or_pll_cap = self.i2c.rfpll.or_pll_cap
                [sar2_code, vco_bias_vol] = self.rfpll.get_pll_vol()

                if dm_en==1:
                    meas_vol=self.mydm.get_result("VDC",data_type = 'MAX')

                else:
                    meas_vol=0

                csvreport1.write_data([chan, rate, ir_enx_cap,ir_cap_ext,or_pll_cap, meas_vol,vco_bias_vol, sar2_code, pwr, evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase, evm_list])
                print [chan,ir_enx_cap,ir_cap_ext,or_pll_cap,meas_vol,vco_bias_vol, sar2_code,rate,pwr,evm,evm_std,evm_max]

##                if evm < -30:
##                    cap_last = self.i2c.rfpll.ir_cap_ext
##
##                if cap_last>0 and evm > -1:
##                    evm0_num += 1
##
##                if evm0_num>5:
##                    break

##            if cap_last==0:
##                cap_last = 60


    def rfpll_cap_noise(self,device_spa="N9020A",name_str=""):
        '''
        :brief: rfpll or_pll_cap and or_pll_dac sweep
        :param: - no param
        :output file: ./rftest/rfdata/rfpll_sweep
        '''
        title = 'channel,ir_cap_enx, ir_cap_ext, or_pll_cap, ent_vco_bias_vol, tone_frequency, tone_power, frequency1(+40m),power1(+40m), frequency2(+40m), power2(-40m)\n'
        fname = self.wifi.get_filename('rfpll_cap_noise_%s'%name_str, 'rfpll_cap_noise_%s'%name_str)
        csvreport1=csvreport(fname, title)
        if device_spa =="":
            self.spa = HP('SA',2412);
        else:
            self.spa = Agilent('SA',2412,device=device_spa);


        self.wifiapi.pll_cap_track_en(0)
        self.wifi.force_txon(1)
        self.wifi.txtone(1,0, 40)

        for chan in[14]:

            self.wifiapi.rfchsel(chan, 0)

            for cap_ext in range(50, -1, -1):

                self.i2c.rfpll.ir_cap_ext = cap_ext

                self.spa.set_param(2400,span=900,rb=100,vb=300)
                time.sleep(0.2)
                result=self.spa.pk_search()
                tone_freq=result[0][0]
                tone_pwr=result[0][1]

                self.spa.set_param(tone_freq,span=10,rb=10, vb=10)
                time.sleep(0.2)
                result1=self.spa.pk_search()
                tone_freq1=result1[0][0]
                tone_pwr1=result1[0][1]

                self.spa.set_param(tone_freq+40,span=10,rb=10, vb=10)
                time.sleep(0.2)
                result1=self.spa.pk_search()
                tone_freq2=result1[0][0]
                tone_pwr2=result1[0][1]

                self.spa.set_param(tone_freq-40,span=5,rb=10, vb=10)
                time.sleep(0.2)
                result1=self.spa.pk_search()
                tone_freq3=result1[0][0]
                tone_pwr3=result1[0][1]

                [sar2_code, vco_bias_vol] = self.rfpll.get_pll_vol()

                csvreport1.write_data([chan, self.i2c.rfpll.ir_enx_cap, self.i2c.rfpll.ir_cap_ext,self.i2c.rfpll.or_pll_cap,vco_bias_vol, tone_freq1,tone_pwr1, tone_freq2,tone_pwr2,tone_freq3, tone_pwr3], float_num=4)


    def rfpll_sweep(self, freq_start=2000, freq_end=3000, freq_step=1,name_str=""):
        '''
        :brief: rfpll or_pll_cap and or_pll_dac sweep
        :param: - no param
        :output file: ./rftest/rfdata/rfpll_sweep
        '''
        title = 'frequency, or_pll_cap,or_pll_dac, dsdm_23_16, dsdm_15_8, dsdm_7_0\n'
        fname = self.wifi.get_filename('rfpll_sweep_%s'%name_str, 'rfpll_sweep_%s'%name_str)
        csvreport1=csvreport(fname, title)

        self.wifi.i2c_wic('rfpll', 'ir_enx_dac', 0)
        self.wifi.i2c_wic('rfpll', 'ir_enx_cap', 0)
        for freq in range(freq_start, freq_end, freq_step):
            self.rfpll.set_freq(freq)
            or_pll_cap = self.wifi.i2c_ric('rfpll', 'or_pll_cap')
            or_pll_dac = self.wifi.i2c_ric('rfpll', 'or_pll_dac')
            dsdm_23_16 = self.wifi.i2c_ric('rfpll_sdm', 'dsdm_23_16')
            dsdm_15_8  = self.wifi.i2c_ric('rfpll_sdm', 'dsdm_15_8')
            dsdm_7_0   = self.wifi.i2c_ric('rfpll_sdm', 'dsdm_7_0')
            csvreport1.write_data([freq, or_pll_cap, or_pll_dac, dsdm_23_16, dsdm_15_8, dsdm_7_0])


    def rfpll_open_cap(self,device_spa="N9020A",name_str=""):
        '''
        :brief: rfpll or_pll_cap and or_pll_dac sweep
        :param: - no param
        :output file: ./rftest/rfdata/rfpll_sweep
        '''
        title = 'ir_cap_enx, ir_cap_ext, tone_freq,tone_pwr,tone_freq1,tone_pwr1\n'
        fname = self.wifi.get_filename('rfpll_sweep_%s'%name_str, 'rfpll_sweep_%s'%name_str)
        csvreport1=csvreport(fname, title)
        if device_spa =="":
            self.spa = HP('SA',2412);
        else:
            self.spa = Agilent('SA',2412,device=device_spa);


        self.rfpll.set_freq(2000)
        self.i2c.rfpll.ir_enx_cap = 1
        self.wifi.force_txon(1)
        self.wifi.txtone(1,0, 70)
        for cap_ext in range(0, 192):
            self.spa.set_param(2400,span=900,rb=100,vb=300)
            self.i2c.rfpll.ir_cap_ext = cap_ext
            time.sleep(1)
            result=self.spa.pk_search()
            tone_freq=result[0][0]
            tone_pwr=result[0][1]
            self.spa.set_param(tone_freq,span=5,rb=3,vb=10)
            time.sleep(1)
            result1=self.spa.pk_search()
            tone_freq1=result1[0][0]
            tone_pwr1=result1[0][1]
            csvreport1.write_data([1, cap_ext,tone_freq,tone_pwr,tone_freq1,tone_pwr1], float_num=4)

    def rfpll_ent_vol(self):
        title = 'ent_vco, ent_vco_bias, dtest, pll_cap, atten,vol_code\n'
        fname = self.wifi.get_filename('rfpll_ent_vol', 'rfpll_ent_vol')
        csvreport1=csvreport(fname, title)
        logsetlevel('I')
        cap_org = self.i2c.rfpll.ir_cap_ext
        for i in range(2):
            for dtest in range(4):
                for cap in range(cap_org-5, cap_org+5):
                    self.i2c.rfpll.ir_cap_ext = cap
                    if i==0:
                        self.i2c.rfpll.ent_vco_bias=1
                        self.i2c.rfpll.ent_vco=0
                    else:
                        self.i2c.rfpll.ent_vco_bias=0
                        self.i2c.rfpll.ent_vco=1
                    self.i2c.rfpll.dtest=dtest
                    for atten in range(4):
                        sar2_code = self.wifiapi.get_sar2_vol(atten)
                        csvreport1.write_data([self.i2c.rfpll.ent_vco,self.i2c.rfpll.ent_vco_bias,
                            self.i2c.rfpll.dtest,self.i2c.rfpll.ir_cap_ext,atten,sar2_code])
                        loginfo([self.i2c.rfpll.ent_vco,self.i2c.rfpll.ent_vco_bias,
                            self.i2c.rfpll.dtest,self.i2c.rfpll.ir_cap_ext,atten,sar2_code])
        self.i2c.rfpll.ent_vco_bias=0
        self.i2c.rfpll.ent_vco=0
        self.i2c.rfpll.dtest=0
        self.i2c.rfpll.ir_cap_ext = cap_org





