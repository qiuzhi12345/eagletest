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
from hal.common import MEM
from rftest.rflib.pbus import pbus
import rftest.rflib.rfglobal as rfglobal
from rftest.rflib.rfpll import rfpll
from rftest.rflib.rfcal import rfcal
import rftest.rflib.wifi_instrum as wifi_instrum
from baselib.loglib.log_lib import *
from rftest.rflib.saradc import SARADC
from rftest.rflib.csv_report import csvreport
#from rftest.testcase.rf_debug.i2c_sweep import I2C_SWEEP

rftx_lst = [0x5f]
#rftx_lst = [0x1f, 0x2f,0x3f,0x4f,0x5f,0x6f,0x7f]
           #-9.75,-6.25,-3.75,-1.75,0,1.5,2.75
##rftx_lst = [0x0, 0x1,0x2,0x3,0x4,0x8,0xc,0x10,0x20,0x30,0x40,0x50,0x60,0x70]

##bbgain_lst = [0x0,0x40,0x80,0xc0,0x100,0x140,0x20,0x60,0xa0,0xe0,0x120,0x160,0x30,0x70,0xb0,0xf0,0x130,0x170,0x38,0x78,0xb8,0xf8,0x138,0x178]
##             #[0db, 1db, 2db, 3db, 4db, 5db , 6dB ,7dB, 8dB, 9db, 10db, 11db, 12db,13db,14db,15db,16db, 17dB,18dB,19db,20dB,21dB,22dB,23dB]

##bbgain_lst = [0x0,0x40,0x80,0xc0,0x100,0x140,0x20,0x60,0xa0,0xe0,0x120,0x160,0x30,0x70,0xb0,0xf0,0x130]
##             #[0db, 1db, 2db, 3db, 4db, 5db , 6dB ,7dB, 8dB, 9db, 10db, 11db,12db,13db,14db,15db,16db]
bbgain_lst = [0x120]
             #[8db]


class Sweep_TX_Gain(object):

    def __init__(self,comport,chipv='ESP32'):

        self.comport = comport
        self.chipv = chipv
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.pbus = pbus(self.comport, self.chipv)
        self.mem = MEM(self.comport, self.chipv)
        self.rfcal = rfcal(self.comport, self.chipv)
        self.rfpll = rfpll(self.comport, self.chipv)
        self.hals = HALS(self.comport,self.chipv)
        self.saradc = SARADC(self.comport,self.chipv)
        self.wifiapi = WIFIAPI(self.comport,self.chipv)


    def force_tx_gain_init(self, freq=2412,rate='mcs7',pa_gain=0x5f,bb_gain=0x120,dig_atten=12):
        self.wifiapi.cmdstop()
        cbw40m = self.wifi.rate2ht40(rate)

        if self.chipv == "CHIP722":
            self.rfpll.set_freq(freq)

##            freq = 2412
##            self.rfpll.set_freq(freq)
##            self.pbus.pbus_debugmode()
##            self.pbus.open_tx(pa_gain, bb_gain)
##            self.rfcal.tos()
##            self.wifi.force_txon(1)

           # setting for evm, better 1dB
            self.wifi.i2c_wic('rfpll','lf_hbw',0) # default 1
            self.wifi.i2c_wic('rfpll','ir_ext_dchgp',7) # default 7
            self.wifi.i2c_wic('bias','cp1p6_dreg',0) #default 2

##            self.wifi.i2c_wic('rftx','TMX2G_CCT_LOAD',7)#default 7
            self.wifi.i2c_wic('rftx','TMX2G_RCT_LOAD',1)
##            self.wifi.i2c_wic('rftx','PA2G_CCT_STG1',7)#default 7
##            self.wifi.i2c_wic('rftx','PA2G_CCT_STG2',15)#default 0
            self.wifi.i2c_wic('rftx','PA2G_ICT_STG0',8)
            self.wifi.i2c_wic('rftx','PA2G_ICT_STG0_CGM',3)

            self.wifi.i2c_wic('rftx','PA2G_ICT_STG1',4)#default 4
            self.wifi.i2c_wic('rftx','PA2G_ICT_STG1_CGM',9)

            self.wifi.i2c_wic('rftx','PA2G_ICT_STG2',10)#default 10
            self.wifi.i2c_wic('rftx','PA2G_CCT2F_STG0',0)

            self.wifi.i2c_wic('rftx','PA2G_MCT_CLASSB',0)
            self.wifi.i2c_wic('rftx','PA2G_RCT_STG2',0)

            self.wifi.i2c_wic('rftx','PA2G_STG1_SEL_ICGM',0)
            self.wifi.i2c_wic('rftx','PA2G_STG1_SEL_ICGM_N',1)

            self.wifi.i2c_wic('rftx','PA2G_VCT_CSC_STG0',8)
            self.wifi.i2c_wic('rftx','PA2G_VCT_CSC_STG1',4)
            self.wifi.i2c_wic('rftx','PA2G_VCT_CSC_STG2',10)
            self.wifi.i2c_wic('rftx','SPARE_TX',5)
##            self.wifi.i2c_wic('ckgen','sel_rx',0)#default 1
##            self.wifi.i2c_wic('xtal','ir_xtal_dac_enx',)#default 0
##            self.wifi.i2c_wic('xtal','ir_xtal_dac_ext',8)#default 8
##            for i in range(4):
##                for hl in ['h','l']:
##                    self.wifi.i2c_wic('bbtop','filter_wifitx%d_dcap_%sq'%(i,hl),40)
##            self.wifi.i2c_wic('bbtop','filter_wifitx0_dcap_hq',40)
##            self.wifi.i2c_wic('bbtop','filter_wifitx0_dcap_lq',40)


        else:
            self.wifiapi.rfchsel(chan,cbw40m)
            self.wifiapi.set_tx_gain(pa_gain, bb_gain)

        cbw40m = self.wifi.rate2ht40(rate)
        self.wifiapi.set_tx_gain(pa_gain, bb_gain)
        self.wifiapi.set_tx_dig_gain(1,(256-dig_atten)) #256-bk
        self.mem.wrm(0x600060a0,11,8, 0xe)
        self.mem.wrm(0x600060a0,11,8, 0x0)
        self.mem.wrm(0x600060a0,11,8, 0xe)
        self.mem.wrm(0x600060a0,11,8, 0x0)
        rate_index=self.wifi.ratecheck(rate)
        [len_byte, delay] = self.wifi.get_length_delay_duty(rate_index,0.2)
        self.wifi.txout(rate_sym=rate, PackNum=0, PackLen =len_byte, cbw40=cbw40m, ht_dup=0, backoff_qdb=0, frm_delay=delay)


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


    def sweep_tx_gain_EVM(self,cable_lose=2, channel=[1], data_rate=['mcs7'], num=10, target_pwr_dis=0,iqv_no=2, board_no='',evm_list_en=0):

        '''
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
        '''

        title = 'rftx,bbgain,dig_atten,channel,rate, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),'
        fname = self.wifi.get_filename('sweep_tx_gain', 'Test_tx_gain_EVM_%s'%(board_no))
        csvreport1 = csvreport(fname, title+'\n')

        for rate in data_rate:
            for chan in channel:

                if rate == 'mcs0':
                    target_power = 19
                else:
                    if self.chipv =="CHIP722":
                        target_power = 13
                    else:
                        target_power = 13
                    evm_list_en = 1
                    if evm_list_en == 1:
                        evm_lst_str =''
                        for i in range(0,num,1):
                          evm_lst_str+= 'evm_list_%d,'%(i)
                        title +=evm_lst_str
                max_pwr = 25-cable_lose
                reset_flag = 0
                logdebug("rate=%s, channel=%d"%(rate, chan))
                if self.chipv =="CHIP722":
                    freq = self.wifi.chan2freq(chan)
                    self.rfpll.set_freq(freq)
                else:
                    freq = self.wifi.chan2freq(chans)

                for yy0 in range(0,len(rftx_lst)):
                    rfgain = rftx_lst[yy0]
                    for kk0 in range(0,len(bbgain_lst)):
                        bbgain = bbgain_lst[kk0]
                        mcs7_atten1 = 12
                        w_str = ''
                        w_str = self.force_gain_rf(cable_lose=cable_lose, chan=chan, freq=freq, rate=rate, target_power=target_power, rfgain=rfgain, bbgain=bbgain, mcs7_atten1=mcs7_atten1, max_pwr=max_pwr,  num=num, iqv_no=iqv_no,reset_flag=reset_flag,target_pwr_dis=target_pwr_dis,evm_list_en=evm_list_en)

                        reset_flag = 1
                        csvreport1.write_data(list(w_str.split(",")))


    def sweep_dig_gain(self, cable_lose=2, channel=[1], data_rate=['mcs7'], num=10, iqv_no=2, board_no=''):

        '''
        :brief:
            sweep digital gain with fixed PA and BB gain, and use WIFI Insturment to test power and EVM,
            find the range of digital gain without affecting EVM
        :param:
            - cable_lose    : the lose of cable
            - channel       : 1~14
            - data_rate     : mcs7
            - num           : user-defined
            - iqv_no        : 1 - left ; 2- right
            - board_no      : the number of test board
        :return:
            csv report
        '''

        title = 'rftx,bbgain,dig_gain,channel,rate,power,evm,evm_sta,evm_max,freq_error(KHz),syclk_error(ppm)\n'
        fname = self.wifi.get_filename('sweep_tx_gain', 'Test_sweep_digital_gain_%s'%(board_no))
        csvreport1 = csvreport(fname, title)

        chan = channel[0]
        target_power = 0
        rate = data_rate[0]
        max_pwr = 25 - cable_lose
        reset_flag = 0
        logdebug("rate=%s,channel=%d"%(rate,chan))
        if self.chipv =="CHIP722":
            freq = self.wifi.chan2freq(chan)
            self.rfpll.set_freq(freq)
        else:
            freq = self.wifi.chan2freq(chan)

        for i in range(-50,50,2):
            dig_gain = i
            rfgain = 0x3f
            bbgain = 0x20
            print rfgain
            w_str = ''
            w_str = self.force_gain_rf(cable_lose=cable_lose, chan=chan, freq=freq, rate=rate, target_power=target_power, rfgain=rfgain, bbgain=bbgain, mcs7_atten1=dig_gain, max_pwr=max_pwr,  num=num, iqv_no=iqv_no,reset_flag=reset_flag,target_pwr_dis=1)
            reset_flag = 1

            csvreport1.write_data(list(w_str.split(",")))

    def fixed_tx_gain_EVM(self,cable_lose=2, channel=[1], data_rate=['mcs7'], num=10, target_pwr_dis=0,iqv_no=2, board_no=''):

        '''
        :brief:
            test tx performance at fixed gian, pa_gain=0x5f, bb_gain=0x120
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
        '''


        title = 'rftx,bbgain,dig_atten,channel,rate, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm)\n'

        fname = self.wifi.get_filename('sweep_tx_gain', 'Fixed_tx_gain_EVM_%s'%(board_no))
        csvreport1 = csvreport(fname, title)

        chan = channel[0]
        rate = data_rate[0] #'mcs7'
        target_power = 13
        max_pwr = 25-cable_lose
        reset_flag = 0
        logdebug("rate=%s, channel=%d"%(rate, chan))
        freq = self.wifi.chan2freq(chan)

        w_str = self.force_gain_rf(cable_lose=cable_lose, chan=chan, freq=freq, rate=rate, target_power=target_power, rfgain=0x5f, bbgain=0x120, mcs7_atten1=12, max_pwr=max_pwr,  num=num, iqv_no=iqv_no,reset_flag=reset_flag,target_pwr_dis=target_pwr_dis)

        reset_flag = 1
        csvreport1.write_data(list(w_str.split(",")))

    def force_gain_rf(self,cable_lose=2, chan=1, freq=2412, rate = 'mcs7',target_power = 13, rfgain = 0x5f, bbgain = 0x120, mcs7_atten1 = 12, max_pwr=25,  num=10, iqv_no=2,reset_flag=0, target_pwr_dis=0, evm_list_en=0):
        '''
        :brief:
            test tx performance at fixed gian
        '''
        dig_atten = mcs7_atten1
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

            self.force_tx_gain_init(freq,rate,rfgain,bbgain,int(dig_atten))

            if reset_flag == 0:
                myiqv = tester.tester(freq, max_pwr, rate, wifi_instrum.test_para(rate), iqv_no,'measure', cable_lose, 10, 0,1)
                reset_flag = 1
            else:
                myiqv = tester.tester(freq, max_pwr, rate, wifi_instrum.test_para(rate), iqv_no,'measure', cable_lose, 10, 0,1)

            wifi_instrum.iqv_avg(myiqv, iqv_num,'false')
            if rate in('1m','11m'):
                wifi_instrum.spectrum_mask_flatness(myiqv, iqv_num, 3)
                iqv_mask_flatness = rfglobal.iqv_mask_flatness
            elif rate in ('6m','mcs0','mcs0_40'):
                wifi_instrum.spectrum_mask_flatness(myiqv, iqv_num, 99)
                iqv_mask_flatness = rfglobal.iqv_mask_flatness
            self.wifi.cmdstop()
            iqv = rfglobal.iqv
            evm = iqv['evm_raw']
            evm_std = iqv['evm_std']
            evm_max = iqv['evm_max']
            pwr = iqv['pwr']
            freq_err = iqv['freq_err']
            clk_err = iqv['clk_err']
            if tt < (tt_max - 1):
                dig_atten += (pwr - target_power)*4

        w_str = ''
        w_str += "%s, 0x%x ,%d, %d,%s,%2.2f,%2.2f,%2.2f,%2.2f,%2.2f,%2.2f,"%(hex(rfgain),bbgain,dig_atten,chan,str(rate),pwr,evm,evm_std,evm_max,freq_err,clk_err)
        if evm_list_en == 1:
            for evm_i in iqv['evm_list']:
                w_str += '%s,'%(evm_i)
        if rate in('1m','11m'):
            freq_mask = [0,0,iqv_mask_flatness['lower2_freq_11b'],iqv_mask_flatness['lower1_freq_11b'],iqv_mask_flatness['upper1_freq_11b'],iqv_mask_flatness['upper2_freq_11b'],0,0]
            marg =      [0,0,iqv_mask_flatness['lower2_marg_11b'],iqv_mask_flatness['lower1_marg_11b'],iqv_mask_flatness['upper1_marg_11b'],iqv_mask_flatness['upper2_marg_11b'],0,0]
            for n in range(0,8):
                w_str += '%s'%freq_mask[n]+','+'%s'%marg[n]+','
        elif rate in ('6m','mcs0','mcs0_40'):
            freq_mask = [iqv_mask_flatness['lower4_freq'],iqv_mask_flatness['lower3_freq'],iqv_mask_flatness['lower2_freq'],iqv_mask_flatness['lower1_freq'],iqv_mask_flatness['upper1_freq'],iqv_mask_flatness['upper2_freq'],iqv_mask_flatness['upper3_freq'],iqv_mask_flatness['upper4_freq']]
            marg =      [iqv_mask_flatness['lower4_marg'],iqv_mask_flatness['lower3_marg'],iqv_mask_flatness['lower2_marg'],iqv_mask_flatness['lower1_marg'],iqv_mask_flatness['upper1_marg'],iqv_mask_flatness['upper2_marg'],iqv_mask_flatness['upper3_marg'],iqv_mask_flatness['upper4_marg']]
            for n in range(0,8):
                w_str += '%s'%freq_mask[n]+','+'%s'%marg[n]+','
        print hex(rfgain),hex(bbgain),dig_atten,chan,str(rate),pwr,evm,evm_std,evm_max,freq_err,clk_err
        return w_str

