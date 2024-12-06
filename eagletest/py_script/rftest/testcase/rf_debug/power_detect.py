import time
import re
import csv
import os, sys
import matplotlib.pyplot as plt
import pylab
import numpy as np
from rftest.rflib.utility import mfunc
from baselib.instrument import dm,tester
from baselib.instrument.spa import HP,Agilent
from hal.wifi_api import WIFIAPI
from rftest.rflib.wifi_lib import WIFILIB
from hal.common import MEM
from hal.Init import HALS
from rftest.rflib.pbus import pbus as Pbus
from rftest.rflib.rfcal import rfcal
import rftest.rflib.rfglobal as rfglobal
from rftest.rflib.saradc import SARADC
from baselib.loglib.log_lib import *
from rftest.testcase.rf_debug.tx_gain_sweep import Sweep_TX_Gain
from rftest.rflib.csv_report import csvreport
from hal.hwregister.hwi2c.all import *
from hal.hwregister.hwpbus.all import *
import rftest.rflib.wifi_instrum as wifi_instrum
from baselib.instrument.awg import awg
from hal.adc import RTC_ADC2


rate_all = rfglobal.test_rate_all
rate_comm = rfglobal.test_rate_comm

class  PwrDet():

    def __init__(self,comport,chipv='ESP32'):
        self.comport = comport
        self.chipv = chipv
        self.wifiapi = WIFIAPI(self.comport,self.chipv)
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.mem = MEM(self.comport, self.chipv)
        self.pbus = Pbus(self.comport, self.chipv)
        self.hals = HALS(self.comport,self.chipv)
        self.rfcal = rfcal(self.comport, self.chipv)
        self.saradc = SARADC(self.comport,self.chipv)
        self.sweep_tx_gain = Sweep_TX_Gain(self.comport,self.chipv)
        self.i2c = HWI2C(self.comport,self.chipv)
        self.hwpbus = HWPBUS(self.comport,self.chipv)

    def tone_power_detector(self,backoff=-80,cable_lose=0,channel=[],name_str=''):# use spectrum analyzer

        '''
        :brief:
            comparison the power result between  Power detector and spectrum analyzer,
            adjust the offset of SARADC converting into power
        :param:
            - backoff   : the bacokff of tone
            - cable_lose: the lose of cable
        :return:
            csv report
        '''

        title = 'chan,backoff,det_pwr,SPA_pwr,diff(SPA_pwr-Det_pwr),Vdd33\n'
        fname = self.wifi.get_filename('sar_pwrdet_data', 'power_detector_%s'%(name_str))
        csvreport1 = csvreport(fname, title)

        device_spa = "N9020A" #"E4404B","N9020A"
        for chan in channel:
            cfreq =self.wifi.chan2freq(chan)
            if device_spa =="":
                SPA_Revise_Power = 2; #HP lose:2dB
                self.spa = HP('SA',cfreq=cfreq+5,rb=1,span=1,reflvl=20);#rb and span
            else:
                SPA_Revise_Power = 0.2;
                self.spa = Agilent('SA',cfreq=cfreq+5,rb=1,span=1,reflvl=20,device=device_spa);#rb and span
            self.spa.set_rb(30);

            self.wifi.rfchsel(chan,0)#1:40M,0:20M
            for i in range(backoff,0,2):
                if self.chipv=="CHIP723":
                    self.pbus.pbus_debugmode()
                    self.pbus.open_tx(0x5f,0x20)
                    self.rfcal.tos()
                    self.wifi.force_txon(1)
##                    self.pbus.pbus_wr('rftx1', 'en1', 0x7f)
##                    self.pbus.pbus_wr('bb', 'en1', 0x7c)
                    self.wifi.txtone(1, 5, i)
                    self.saradc.en_pwdet()
                    det_pwr = 0
                    for j in range(1,3):
                        det_pwr += float( self.saradc.sar_dout(8,pwr_dis=0,offset=17.5))
                    Vdd33 =  self.saradc.readvdd33()
                    self.wifi.txtone(1, 5, i)
                    SPA_pwr = self.spa.get_result('PEAK')[1]+SPA_Revise_Power+cable_lose
                    print "SPA_pwr=%2.2f"%SPA_pwr
                    self.wifi.txtone(0,5,i)
##                    self.pbus.pbus_wr('rftx1', 'en1', 0x0)
##                    self.pbus.pbus_wr('bb', 'en1', 0x0)
                    diff = det_pwr/2-SPA_pwr
                    csvreport1.write_data([i,float(det_pwr/2),SPA_pwr,diff,Vdd33])

                elif self.chipv =="CHIP724":
                    self.wifi.force_txon(1)
                    self.wifi.txtone(1, 5, i)
                    SPA_pwr = self.spa.get_result('PEAK')[1]+SPA_Revise_Power+cable_lose
                    self.wifi.txtone(0,5,i)
                    det_pwr=self.wifiapi.test_txtone_pwr(-i,loop_num=1,mode=1,step=128)
                    diff = float(det_pwr)/16-SPA_pwr
                    time.sleep(3)
                    csvreport1.write_data([chan,i,float(det_pwr)/16,SPA_pwr,diff])


    def packet_power_detector(self, cable_lose=2, channel=[1], data_rate=['mcs7'], num=10, iqv_no=2,name_str=''):# use WIFI insturment

        title = 'rftx,bbgain,dig_gain,channel,rate,power,evm,evm_sta,evm_max,freq_error(KHz),syclk_error(ppm),,,,detpwr\n'
        fname = self.wifi.get_filename('sar_pwrdet_data', 'packet_detector_%s'%name_str)
        csvreport1 = csvreport(fname, title)

        chan = channel[0]
        target_power = 0
        rate = data_rate[0]
        max_pwr = 25 - cable_lose
        reset_flag = 0
        logdebug("rate=%s,channel=%d"%(rate,chan))
        freq = self.wifi.chan2freq(chan)
        self.wifiapi.txpwr_track_en(1,0,0)
        self.wifiapi.pll_cap_track_en(0)
        for i in range(50,-50,-1):
            dig_gain = i
            rfgain = 0x4f
            bbgain = 0x140
            print rfgain
            w_str = ''
            sar_out = []

            w_str = self.sweep_tx_gain.force_gain_rf(cable_lose=cable_lose, chan=chan, rate=rate, target_power=target_power, rfgain=rfgain, bbgain=bbgain, dig_atten=dig_gain, max_pwr=max_pwr,  num=num, iqv_no=iqv_no,reset_flag=reset_flag,target_pwr_dis=1)
            detpwr = self.wifiapi.packet_pwdet_out()
            for i in range(0,8):
                data = self.mem.rd(0x6000e080+i*4)
                sar_out.append(data)
            reset_flag = 1

            csvreport1.write_data(list(w_str.split(","))+[int(detpwr)/16.0,sar_out])


    def tone_pwdet(self, instr=''):
        title = 'atten, reg, reg_data, pwr, pwr_f, sar_code0,sar_code1,sar_code2,sar_code3,sar_code4,sar_code5,sar_code6,sar_code7\n'
        fname = self.wifi.get_filename('tone_pwdet', 'tone_pwdet_%s'%instr)
        csvreport1 = csvreport(fname, title)

        block = 'rftx'
        i2c_regdict = self.wifi.i2c_regdict_get()
        regdict = i2c_regdict[block]
        for ctrl_name in regdict:
            [addr, msb, lsb] = regdict[ctrl_name][0:3]
            bits = msb-lsb+1
            step = bits-1
            if step <2:
                step = 1
            code_org = self.wifi.i2c_ric(block, ctrl_name)
            for reg_data in range(0, 2**(bits), step):
                self.wifi.i2c_wic(block, ctrl_name, reg_data)
                for atten in range(110,105, -1):
                    pwr = self.wifi.test_txtone_pwr(atten,2,mode=1,step=64)
                    pwr_f = int(pwr)/32.0
                    sar_out = []
                    for i in range(0,8):
                        data = 4095-self.mem.rd(0x6000e080+i*4)
                        sar_out.append(data)
                    csvreport1.write_data([atten, ctrl_name, reg_data, pwr, pwr_f, sar_out])
                self.wifi.i2c_wic(block, ctrl_name, code_org)


    def tone_pwdet_sar(self, instr=''):
        title = 'atten, pwr, pwr_f, sar_code0,sar_code1,sar_code2,sar_code3,sar_code4,sar_code5,sar_code6,sar_code7\n'
        fname = self.wifi.get_filename('tone_pwdet', 'tone_pwdet_%s'%(instr))
        csvreport1 = csvreport(fname, title)

        self.wifi.rfchsel(14,0)#1:40M,0:20M

##        self.pbus.pbus_debugmode()
##        self.pbus.open_tx(0x5f,0x120)
##
##        if lb_en==1:
####            self.hwpbus.RFRX1.EN1 = 0x105
####            self.hwpbus.RFTX1.EN1 = 0x7f
####            self.hwpbus.BB1.EN1   = 0x1f9
####            self.i2c.bbtop.enlb    = 1
####            self.i2c.rfrx.LB_MODE  = 1
##            self.i2c.rftx.LB_EN    = 1
##            self.i2c.rftx.LB_EN_IQ = 1
##            self.i2c.rftx.LB_GCT   = 1
##            self.rfcal.tos()
##            self.wifiapi.rxdc_cal()
##        else:
##            self.i2c.bbtop.enlb    = 0
##            self.i2c.rfrx.LB_MODE  = 0
##            self.i2c.rftx.LB_EN    = 0
##            self.i2c.rftx.LB_EN_IQ = 0
##            self.i2c.rftx.LB_GCT   = 0
##            self.rfcal.tos()

        self.wifi.force_txon(1)

        for atten in range(120,0, -8):
            pwr = self.wifiapi.meas_tone_pwr_db(atten, 64)
            sar_out = []
            for i in range(0,8):
                data = 4095-self.mem.rd(0x6000e080+i*4)
                sar_out.append(data)
            pwr_f = int(pwr)/8.0
            csvreport1.write_data([atten, pwr, pwr_f, sar_out])
        self.wifi.force_txon(0)


    def tone_pwdet_spa(self, cable_lose=2, instr=''):
        title = 'atten, pwr, pwr_f, spa_pwr, sar_code0,sar_code1,sar_code2,sar_code3,sar_code4,sar_code5,sar_code6,sar_code7\n'
        fname = self.wifi.get_filename('tone_pwdet', 'tone_pwdet_%s'%(instr))
        csvreport1 = csvreport(fname, title)

        chan = 1
        chan_freq = 2412+5
        tone_step = 128
        device_spa = "N9020A" #"E4404B","N9020A"
        if device_spa =="":
            SPA_Revise_Power = 2; #HP lose:2dB
            self.spa = HP('SA',cfreq=chan_freq,rb=1,span=1,reflvl=20);#rb and span
        else:
            SPA_Revise_Power = 0.2;
            self.spa = Agilent('SA',cfreq=chan_freq,rb=1,span=1,reflvl=20,device=device_spa);#rb and span
        self.spa.set_rb(30);

        self.wifiapi.pll_cap_track_en(0)
        self.wifiapi.txpwr_track_en(0,0,0)

        self.wifi.rfchsel(chan,0)#1:40M,0:20M
        self.wifiapi.set_tx_gain(0x5f, 0xa0)
##        self.i2c.sar.sar2_init_code_msb = 5
        self.i2c.rfpll.ir_enx_cap=0
        self.i2c.rfpll.ir_enx_dac=0
        self.wifi.force_txon(1)
        for atten in range(120,0, -1):
            self.wifi.txtone_step(1, tone_step, atten)

##            self.mem.wrm(0x6000e040, 6, 6, 0)  #pll cal start
##            self.mem.wrm(0x6000e040, 6, 6, 1)  #pll cal start
            SPA_pwr = self.spa.get_result('PEAK')[1]+SPA_Revise_Power+cable_lose
            pwr = self.wifiapi.meas_tone_pwr_db(atten, tone_step)
            sar_out = []
            for i in range(0,8):
                data = self.mem.rd(0x6000e080+i*4)
                sar_out.append(data)
            pwr_f = int(pwr)/8.0
            csvreport1.write_data([atten, pwr, pwr_f, SPA_pwr, sar_out, self.i2c.sar.sar2_init_code_msb])
        self.wifi.force_txon(0)
##        self.i2c.sar.sar2_init_code_msb = 3

    def tone_pwdet_reg(self, cable_lose=2, ctrl_name='', max_data=4, instr=''):
        title = 'atten, %s,pwr, pwr_f, spa_pwr, sar_code0,sar_code1,sar_code2,sar_code3,sar_code4,sar_code5,sar_code6,sar_code7\n'%ctrl_name
        fname = self.wifi.get_filename('tone_pwdet', 'tone_pwdet_%s_%s'%(instr, ctrl_name))
        csvreport1 = csvreport(fname, title)

        chan = 14
        chan_freq = 2484+5
        tone_step = 128
        device_spa = "E4404B" #"E4404B","N9020A"
        if device_spa =="":
            SPA_Revise_Power = 2; #HP lose:2dB
            self.spa = HP('SA',cfreq=chan_freq,rb=1,span=1,reflvl=20);#rb and span
        else:
            SPA_Revise_Power = 0.2;
            self.spa = Agilent('SA',cfreq=chan_freq,rb=1,span=1,reflvl=20,device=device_spa);#rb and span
        self.spa.set_rb(30);

        self.wifi.rfchsel(chan,0)#1:40M,0:20M
        self.wifiapi.set_tx_gain(0x5f, 0x120)
        block = 'rftx'
        self.i2c.rfpll.ir_enx_cap=0
        self.i2c.rfpll.ir_enx_dac=0
        code_org = self.wifi.i2c_ric(block, ctrl_name)
        for reg_data in range(0, max_data):
            self.wifi.i2c_wic(block, ctrl_name, reg_data)

            for atten in range(128,-7, -8):
                self.wifi.force_txon(1)
                self.wifi.txtone_step(1, tone_step, atten)
                self.mem.wrm(0x6000e040, 6, 6, 0)  #pll cal start
                self.mem.wrm(0x6000e040, 6, 6, 1)  #pll cal start
                SPA_pwr = self.spa.get_result('PEAK')[1]+SPA_Revise_Power+cable_lose
                pwr = self.wifiapi.meas_tone_pwr_db(atten, tone_step)
                self.wifi.force_txon(0)
                sar_out = []
                for i in range(0,8):
                    data = 4095-self.mem.rd(0x6000e080+i*4)
                    sar_out.append(data)
                pwr_f = int(pwr)/8.0
                csvreport1.write_data([atten, reg_data,pwr, pwr_f, SPA_pwr, sar_out])


    def tone_pwdet_delay(self, instr=''):
        title = 'atten, state3_delay, pwr, pwr_f, sar_code0,sar_code1,sar_code2,sar_code3,sar_code4,sar_code5,sar_code6,sar_code7\n'
        fname = self.wifi.get_filename('tone_pwdet', 'tone_pwdet_%s'%(instr))
        csvreport1 = csvreport(fname, title)

        self.wifi.rfchsel(14,0)#1:40M,0:20M

        for delay in range(0,0x2f,2):
            self.mem.wrm(0x6000e054, 15, 8, delay)
##            self.mem.wrm(0x6000e054, 23, 16, delay)
            for atten in range(120,121):
                for i in range(10):
                    self.wifi.force_txon(1)
                    pwr = self.wifiapi.meas_tone_pwr_db(atten, 64)
                    self.wifi.force_txon(0)
                    time.sleep(0.01)
                    sar_out = []
                    for i in range(0,8):
                        data = 4095-self.mem.rd(0x6000e080+i*4)
                        sar_out.append(data)
                    pwr_f = int(pwr)/8.0
                    csvreport1.write_data([atten, delay, pwr, pwr_f, sar_out])

    def sar_dout_read(self, csvreport1='', backoff_in=0, rate=0, pwdet_code=0, tone_en=0, instr=''):
        backoff = backoff_in
        if backoff < 0:
            backoff = 256+backoff

        self.mem.wrm(0x6000e05c, 15, 0, pwdet_code)
        for i in range(0,4):
            if tone_en==1:
                self.wifiapi.test_txtone_pwr(backoff+42,1,mode=1,step=128)
            else:
                self.wifiapi.set_tx_dig_gain(1,(256-backoff_in)) #256-bk
                self.wifiapi.txstart(rate,4,10, frm_delay=3000)
            data = []
            for k in range(8):
                data.append(self.mem.rd(0x6000e080+k*4))
            loginfo(tone_en,rate,backoff_in,data)
            if csvreport1 != '':
                csvreport1.write_data([tone_en,rate,backoff_in, hex(pwdet_code), instr, data])

    def pwdet_sar_dout(self, instr=''):
        title = 'tone_en,rate, backoff, pwdet_code, atten,sar_code0,sar_code1,sar_code2,sar_code3,sar_code4,sar_code5,sar_code6,sar_code7\n'
        fname = self.wifi.get_filename('pwdet_sar_dout', 'tone_pwdet_atten')
        csvreport1 = csvreport(fname, title)

        self.i2c.sar.sar2_smp_count = 2
        self.wifiapi.txpwr_track_en(1,0,0)
        self.wifiapi.pll_cap_track_en(0)

        self.mem.wrm(0x6000e060, 4, 3, 1)  #pwdet sar atten

        self.mem.wrm(0x6000e050, 4, 2,6) #pwdet sar num

        self.sar_init_code(1400)
        self.wifi.txout('mcs7', 4, PackLen=200)

        self.sar_dout_read(csvreport1, backoff_in=24, rate=0x0, pwdet_code=0x0160, tone_en=1)
        self.sar_dout_read(csvreport1, backoff_in=24, rate=0x0, pwdet_code=0x0165, tone_en=1)

        for atten in range(0,4):
            self.mem.wrm(0x6000e060, 4, 3, atten)  #pwdet sar atten
            for backoff in range(-20,20):
                for rate in [0x0, 0x10, 0xff]:
                    if rate==0xff:
                        tone_en = 1
                    else:
                        tone_en = 0
                    self.sar_dout_read(csvreport1, backoff_in=backoff, rate=rate, pwdet_code=0x016a, tone_en=tone_en, instr='%d'%atten)


    def sar_init_code(self, init_code=0):
        self.i2c.sar.sar2_init_code_lsb = init_code&0xff
        self.i2c.sar.sar2_init_code_msb = init_code>>8

    def pwdet_sar_init_code(self, instr=''):
        title = 'rate, backoff, pwdet_code, init_code, sar_code0,sar_code1,sar_code2,sar_code3,sar_code4,sar_code5,sar_code6,sar_code7\n'
        fname = self.wifi.get_filename('pwdet_sar_dout', 'pwdet_sar_init_code_%s'%(instr))
        csvreport1 = csvreport(fname, title)

        self.mem.wrm(0x6000e050, 4, 2,6)

        self.wifiapi.txpwr_track_en(1,0,0)
        self.wifiapi.pll_cap_track_en(0)

        self.wifi.txout('mcs7', 4, PackLen=200)

        for i in range(4):
            backoff = -12 + i*12
            rate = 0x0
            for init_code in range(0,4000,100):
                self.sar_init_code(init_code)
                self.sar_dout_read(csvreport1, backoff_in=backoff, rate=0x0, pwdet_code=0x016a, instr=init_code)

    def pwdet_state_set(self, wr=0, state_stage=0, state=0):
        if wr==1:
            if state_stage ==0:
                self.mem.wrm(0x6000e060,23,16, state) #state0
            elif state_stage ==1:
                self.mem.wrm(0x6000e054, 7, 0, state) #state1
            elif state_stage ==2:
                self.mem.wrm(0x6000e054,15, 8, state) #state2
            elif state_stage ==3:
                self.mem.wrm(0x6000e054,23,16, state)  #state3
            elif state_stage ==4:
                self.mem.wrm(0x6000e058, 7, 0, state) # state4
            elif state_stage ==5:
                self.mem.wrm(0x6000e058,15, 8, state) #state5
            elif state_stage ==6:
                self.mem.wrm(0x6000e058,23,16, state) #state6
            else:
                return 0

        if state_stage ==0:
            data = self.mem.rdm(0x6000e060,23,16) #state0
        elif state_stage ==1:
            data = self.mem.rdm(0x6000e054, 7, 0) #state1
        elif state_stage ==2:
            data = self.mem.rdm(0x6000e054,15, 8) #state2
        elif state_stage ==3:
            data = self.mem.rdm(0x6000e054,23,16)  #state3
        elif state_stage ==4:
            data = self.mem.rdm(0x6000e058, 7, 0) # state4
        elif state_stage ==5:
            data = self.mem.rdm(0x6000e058,15, 8) #state5
        elif state_stage ==6:
            data = self.mem.rdm(0x6000e058,23,16) #state6
        else:
            data = 0
        return data

    def pwdet_sar_state(self, instr=''):
        title = 'state_stage,state_org,state,rate,i,pwr_std mcs7,pwr_std 11m,pwr_std 11ms,pwr_mean mcs7,pwr_mean 11m,pwr_mean 11ms,pwr_max,,,pwr_min\n'
        fname = self.wifi.get_filename('pwdet_sar_state', 'pwdet_sar_state_%s'%(instr))
        csvreport1 = csvreport(fname, title)

        self.wifiapi.txpwr_track_en(0,0,0)
        self.wifiapi.pll_cap_track_en(0)
##        self.wifi.txon_delay(paon_delay=156, btx_wait=125, ntx_wait=158, ntx40_wait=173, stf_num=0)
        self.mem.wrm(0x6000e060,23,16, 50) #state0
        self.mem.wrm(0x6000e054, 7, 0, 15) #state1
        self.mem.wrm(0x6000e054,15, 8, 15) #state2
        self.mem.wrm(0x6000e054,23,16, 15)  #state3
        self.mem.wrm(0x6000e058, 7, 0, 255) # state4
        self.mem.wrm(0x6000e058,15, 8, 23) #state5
        self.mem.wrm(0x6000e058,23,16, 255) #state6

        for state_stage in range(0,7):
##            self.wifi.sar_delay_set(wr=1)  #set default delay
            state_org = self.pwdet_state_set(wr=0, state_stage=state_stage, state=0)
##            state_org = self.mem.rdm(0x6000e058,23,16)
            for state in range(3,256,2):
                self.mem.wrm(0x6000e058,23,16, state) #state6
                state_now = self.mem.rdm(0x6000e058,23,16)
                pwr_std = []
                pwr_mean = []
                pwr_max = []
                pwr_min = []
                for rate in ['mcs7','11m','11ms']:
                    power_list = []
                    for i in range(0,8):
                        self.wifi.txout(rate, 2, 100)
                        pwdet_power = float(self.wifiapi.packet_pwdet_out())/16
                        power_list.append(pwdet_power)
                    pwr_std.append(np.std(power_list))
                    pwr_max.append(np.max(power_list))
                    pwr_min.append(np.min(power_list))
                    pwr_mean.append(np.mean(power_list))
                csvreport1.write_data([state_stage,state_org,state_now,rate,i,pwr_std,pwr_mean,pwr_max,pwr_min])
                loginfo(state_stage,state_org,state_now,rate,i,pwr_std,pwr_mean,pwr_max,pwr_min)


    def pocket_power_linear(self, cable_lose=0, iqv_no=1, iqv_num=1, name_str=''):

        rate_m = ['1m', 'mcs0']

        chan_m = [1,14]

        title = 'channel,rate,tone_en,dig_atten,i,pwdet_power,power,power-pwdet,evm,sar_dout\n'
        fname = self.wifi.get_filename('pocket_power_linear_%s'%name_str, 'pocket_power_linear_%s'%(name_str))
        csvreport1 = csvreport(fname, title)

        self.wifiapi.txpwr_track_en(1,0,0)
        self.wifiapi.pll_cap_track_en(0)

##        self.wifi.sar_delay_set(wr=1, state4=100, sar_delay=40, atten=3)

        self.wifi.save_init_print('pocket_power_linear_%s'%name_str, name_str)

        max_pwr = 25 - cable_lose
        result = []

        for rate in rate_m:
            for chan in chan_m:
                self.wifi.rfchsel(chan)
                test_para = wifi_instrum.test_para(rate)
                if chan<=14:
                    freq = self.wifi.chan2freq(chan)
                else:
                    freq = chan
                myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0,0,20)

                for backoff in range(48, -24, -2):
                    cbw40m = self.wifi.rate2ht40(rate)

                    self.wifiapi.set_tx_dig_gain(1,(256-backoff)) #256-bk
                    self.wifi.txout(rate, 0, 100)

                    [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false')

                    rate_index=self.wifi.ratecheck(rate)

                    for i in range(4):
                        if i<2:
                            tone_en = 0
                            power_sum = 0
                            for k in range(0,4):
                                self.wifi.txout(rate, 1, 100, frm_delay=5000)
                                power_sum += float(self.wifiapi.packet_pwdet_out())
                            pwdet_power = power_sum/(16*4)
                            pocket_pwr = pwdet_power
                        else:
                            tone_en = 1
                            if rate_index < 8:
                                tone_comp = 42 + 3
                            else:
                                tone_comp = 42
                            pwdet_power = float(self.wifiapi.test_txtone_pwr(backoff+tone_comp, 1, 1, 128))/16
                            tone_pwr = pwdet_power
                        sar_dout = []
                        for k in range(8):
                            sar_dout.append(self.mem.rd(0x6000e080+k*4))

                        csvreport1.write_data([chan,rate,tone_en,backoff,i,pwdet_power,pwr, pwr-pwdet_power,evm,sar_dout])
                    print [chan,rate,backoff,tone_pwr,pocket_pwr,pwr,evm]

    def pocket_power_test(self, cable_lose=0, iqv_no=1, iqv_num=1, name_str=''):

        chan_m = [14]

        title = 'channel,rate,rate_index,i,pwdet_power,power,power-pwdet,evm,sar_dout\n'
        fname = self.wifi.get_filename('pocket_power_test_%s'%name_str, 'pocket_power_test_%s'%(name_str))
        csvreport1 = csvreport(fname, title)

        self.wifiapi.txpwr_track_en(1,0,0)
        self.wifiapi.pll_cap_track_en(0)
        self.mem.wrm(0x6000e054,23,16, 63)  #state3
        self.wifi.save_init_print('pocket_power_test_%s'%name_str, name_str)

        max_pwr = 25 - cable_lose
        result = []

        for rate in rate_all:
            for chan in chan_m:
                cbw40m = self.wifi.rate2ht40(rate)
                self.wifi.rfchsel(chan, cbw40m*2)
                test_para = wifi_instrum.test_para(rate)
                if chan<=14:
                    freq = self.wifi.chan2freq(chan)
                else:
                    freq = chan
                rate_index=self.wifi.ratecheck(rate)

                myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0,0,20)
                self.wifi.txout(rate, 0, 100, cbw40=cbw40m,frm_delay=5000)
                [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false')

                for i in range(4):
                    power_sum = 0
                    for k in range(0,4):
                        self.wifi.txout(rate, 1, 100, frm_delay=5000)
                        power_sum += float(self.wifiapi.packet_pwdet_out(rate_index))
                    pwdet_power = power_sum/(16*4)
                    sar_dout = self.mem.rd(0x6000e080)

                    csvreport1.write_data([chan,rate,rate_index,i,pwdet_power,pwr, pwr-pwdet_power,evm,sar_dout])
                    print [chan,rate,rate_index,pwdet_power,pwr,evm]


    def pwdet_track_test(self, name_str=''):
        title = 'rate,chan,i,sar_dout,pwdet_power,pocket\n'
        fname = self.wifi.get_filename('pwdet_track_test_%s'%name_str, 'pwdet_track_test_%s'%name_str)
        csvreport1 = csvreport(fname, title)

        self.wifi.save_init_print('pwdet_track_test_%s'%name_str, name_str)

        self.wifiapi.txpwr_track_en(1,0,1)
        self.wifiapi.pll_cap_track_en(0)

        self.wifi.txout('mcs0', 1, 100)

        for chan in range(14,15, 4):
            for rate in range(0,24,1):
                i = 0
                while (1):
                    result = self.wifiapi.txstart_over(rate,1,frm_delay=6000)
##                    result = self.wifiapi.txstart(rate,1,frm_delay=6000)
                    pwdet_power = float(self.wifiapi.packet_pwdet_out(rate))/16
                    sar_dout = self.mem.rd(0x6000e080)
                    if len(result.split(',')) == 24:
                        csvreport1.write_data([rate,chan,i,sar_dout,pwdet_power,result])
                        loginfo(rate,chan,i,sar_dout,pwdet_power,result)
                        i = i+1
                        if i==16:
                            break


    def pwdet_stable_test(self, cable_lose=11.1,iqv_no=1,name_str=''):
        title = 'rate,chan,i,pwdet_power, pwr, sar_dout, evm\n'
        fname = self.wifi.get_filename('pwdet_stable_test_%s'%name_str, 'pwdet_stable_test_%s'%name_str)
        csvreport1 = csvreport(fname, title)

        self.wifi.save_init_print('pwdet_stable_test_%s'%name_str, name_str)
        self.wifiapi.txpwr_track_en(1,0,0)
        self.wifiapi.pll_cap_track_en(0)

        rate_m = ['1m','mcs0','mcs7']
        for rate in rate_m:
            for chan in[1,6,11,14]:
                self.wifi.rfchsel(chan)
                test_para = wifi_instrum.test_para(rate)
                if chan<=14:
                    freq = self.wifi.chan2freq(chan)
                else:
                    freq = chan
                myiqv=tester.tester(freq, 25, rate, test_para, iqv_no,'measure', cable_lose, 10, 0,0,20)

                for i in range(1):
                    self.wifi.txout(rate, 0, 100)
                    [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 1,'false')

                    pwdet_power = float(self.wifiapi.packet_pwdet_out())/16
                    sar_dout = self.mem.rd(0x6000e080)
                    csvreport1.write_data([rate,chan,i,pwdet_power, pwr, sar_dout, evm])
                    loginfo(rate,chan,i,pwdet_power, pwr, sar_dout, evm)

    def txcap_pwr_test(self, cable_lose=11.1,iqv_no=1,name_str=''):
        title = 'rate,chan,cap_reg, cap_data, pwr, evm\n'
        fname = self.wifi.get_filename('txcap_pwr_test_%s'%name_str, 'txcap_pwr_test_%s'%name_str)
        csvreport1 = csvreport(fname, title)

        txcap_reg = ['TMX2G_CCT_LOAD', 'PA2G_CCT_STG1', 'PA2G_CCT_STG2']
        rate_m = ['6m']
        for rate in rate_m:
            for chan in[14]:
                self.wifi.rfchsel(chan)
                test_para = wifi_instrum.test_para(rate)
                if chan<=14:
                    freq = self.wifi.chan2freq(chan)
                else:
                    freq = chan
                myiqv=tester.tester(freq, 25, rate, test_para, iqv_no,'measure', cable_lose, 10, 0,0,20)

                for cap_reg in txcap_reg:
                    self.wifi.rfchsel(chan)
                    for cap_data in range(0,16):
                        self.wifi.i2c_wic('rftx', cap_reg, cap_data)
                        reg_data = self.wifi.i2c_ric('rftx', cap_reg)
                        self.wifi.txout(rate, 0, 100)
                        [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, 1,'false')
                        csvreport1.write_data([rate,chan,cap_reg, reg_data, pwr, evm])
                        loginfo(rate,chan,cap_reg, reg_data, pwr, evm)


    def test_cct_reg(self, cable_lose=0, iqv_no=1, iqv_num=1, name_str=''):

        title = 'chan,rate,PA2G_CCT_STG1,dig_atten,pwr,evm,sar_dout\n'
        fname = self.wifi.get_filename('test_cct_reg_%s'%name_str, 'test_cct_reg_%s'%(name_str))
        csvreport1 = csvreport(fname, title)

        self.wifiapi.txpwr_track_en(1,0,0)
        self.wifiapi.pll_cap_track_en(0)

        self.wifi.save_init_print('test_cct_reg_%s'%name_str, name_str)

        max_pwr = 25 - cable_lose
        result = []

        rate = 'mcs7'
        chan = 14
        self.wifi.rfchsel(chan)

        test_para = wifi_instrum.test_para(rate)
        if chan<=14:
            freq = self.wifi.chan2freq(chan)
        else:
            freq = chan
        myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 0,0,20)

        for data in range(16):
            self.i2c.rftx.PA2G_CCT_STG1=data
            for backoff in range(24, -12, -4):
                cbw40m = self.wifi.rate2ht40(rate)

                self.wifiapi.set_tx_dig_gain(1,(256-backoff)) #256-bk
                self.wifi.txout(rate, 0, 100)

                [pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false')

                rate_index=self.wifi.ratecheck(rate)
                self.wifi.txout(rate, 1, 100, frm_delay=5000)
                pwdet_power = float(self.wifiapi.packet_pwdet_out())

                sar_dout = []
                for k in range(8):
                    sar_dout.append(self.mem.rd(0x6000e080+k*4))

                PA2G_CCT_STG1 = self.i2c.rftx.PA2G_CCT_STG1

                csvreport1.write_data([chan,rate,PA2G_CCT_STG1, backoff,pwr,evm,sar_dout[0]])
                print [chan,rate,PA2G_CCT_STG1, backoff,pwr,evm,sar_dout[0]]

    def test_pwdet_reg(self, name_str=''):

        title = 'chan,rate,reg,reg_org,reg_data,same_num,dig_atten,sar_code,sar_dout0,sar_dout1,sar_dout2,sar_dout3,sar_dout4,sar_dout5,sar_dout6,sar_dout7\n'
        fname = self.wifi.get_filename('test_pwdet_code_%s'%name_str, 'test_pwdet_code_%s'%(name_str))
        csvreport1 = csvreport(fname, title)

##        self.wifiapi.txpwr_track_en(1,0,0)
##        self.wifiapi.pll_cap_track_en(0)

##        self.wifi.save_init_print('test_pwdet_code_%s'%name_str, name_str)

        rate = 'mcs7'
        chan = 14
##        self.wifi.rfchsel(chan)
##        reg_m = {
##            'cp1p6_dreg': ['bias', 16],
##            'cp1p2_dreg': ['bias', 16],
##            'cp1p1_pvt_reg': ['bias', 16],
##            'dreg_2p2': ['bias', 16]
##        }
        reg_m = {'PA2G_CCT_STG1': ['rftx', 16]}
##        reg_m = {
##            'TMX2G_CCT_LOAD': ['rftx', 16],
##            'TMX2G_RCT_LOAD': ['rftx', 8],
##            'PA2G_CCT_STG1': ['rftx', 16],
##            'PA2G_CCT_STG2': ['rftx', 16],
##            'PA2G_ICT_STG0': ['rftx', 16],
##            'PA2G_ICT_STG0_CGM': ['rftx', 16],
##            'PA2G_ICT_STG1': ['rftx', 16],
##            'PA2G_ICT_STG1_CGM': ['rftx', 16],
##            'PA2G_ICT_STG2': ['rftx', 16],
##            'PA2G_CCT2F_STG0': ['rftx', 16],
##            'PA2G_MCT_CLASSB': ['rftx', 4],
##            'PA2G_RCT_STG2': ['rftx', 8],
##            'PA2G_VCT_CSC_STG0': ['rftx', 16],
##            'PA2G_VCT_CSC_STG1': ['rftx', 16],
##            'PA2G_VCT_CSC_STG2': ['rftx', 16],
##            'PA2G_PKDET_EN': ['rftx', 8],
##            'PWDET_VTH_TUNE': ['rftx', 16],
##            'PWDET_ICT_OUTPUT': ['rftx', 4],
##            'PWDET_VCT_REF': ['rftx', 4]
##            }
        self.mem.wrm(0x6000e050, 4, 2,6); #sample_num)
        for reg in reg_m:
            temp = reg_m[reg]
            max_data = temp[1]
            block = temp[0]
            reg_org = self.wifi.i2c_ric(block, reg)
            for data in range(11,12):
                self.wifi.i2c_wic(block, reg, data)
                same_num = 0
                code_old = 0
                for backoff in range(60, 0, -1):
                    cbw40m = self.wifi.rate2ht40(rate)

                    if self.chipv=="CHIP724":
                        self.wifi.force_txon(1)
                        self.wifi.txtone(1, 5, backoff)
                        self.wifiapi.get_power_db()
                        self.wifi.force_txon(0)
                    else:
                        self.wifi.test_txtone_pwr(backoff, 1,1,128)

                    sar_dout = []
                    for k in range(8):
                        sar_dout.append(self.mem.rd(0x6000e080+k*4))

                    code_old = sar_dout[0]
                    reg_rd = self.wifi.i2c_ric(block, reg)

                    csvreport1.write_data([chan,rate,reg,reg_org,reg_rd,same_num,backoff,hex(sar_dout[0]),sar_dout])
                    print [chan,rate,reg,reg_org,reg_rd,same_num,backoff,hex(sar_dout[0]),sar_dout]

            self.wifi.i2c_wic(block, reg, reg_org)

    def get_pwdet_sar_code(self,freq_step=128,atten=100):
        if self.chipv=="CHIP724":
            self.wifi.force_txon(1)
            self.wifi.txtone_step(0, freq_step, atten)
            self.wifiapi.get_power_db()
            rtc_sar_code = int(self.mem.rd(0x60008830)&0xffff)
            self.wifi.force_txon(0)
        else:
            self.wifiapi.test_txtone_pwr(atten,1,1,step=freq_step)
            rtc_sar_code = []
            for k in range(2):
                rtc_sar_code.append(self.mem.rd(0x6000e080+k*4))

        return rtc_sar_code

    def test_pwdet_code(self, bt_mode=0, name_str=''):

        title = 'chan,rate,dig_atten,dc_code,ref_code,sig_code,power,temp_code\n'
        fname = self.wifi.get_filename('test_pwdet_code', 'test_pwdet_code_%s_%s'%(bt_mode,name_str))
        csvreport1 = csvreport(fname, title)

        rate = 'mcs7'
        chan = 14
        logsetlevel('I')
##        self.mem.wrm(0x6000e050, 4, 2,6); #sample_num)
##        self.mem.wrm(0x6000e050, 15,8, 2) #sar clk div
        if bt_mode==1:
##            self.wifi.bt_mode_force(1)
            freq = 24
        else:
##            self.wifi.bt_mode_force(0)
            freq = 128

        self.mem.wrm(0x6000e05c, 15,0, 0x160) #dc
        dc_code = self.get_pwdet_sar_code(freq,80)
        self.mem.wrm(0x6000e05c, 15,0, 0x165) #ref
        ref_code = self.get_pwdet_sar_code(freq,80)
        self.mem.wrm(0x6000e05c, 15,0, 0x16a) #sig
        power_init = 9.5 #60 is 11dbm

        for backoff in range(120, 0, -1):
            cbw40m = self.wifi.rate2ht40(rate)
            power = power_init+(60-backoff)*0.25
            sig_code = self.get_pwdet_sar_code(freq,backoff)
            temp_code = self.wifiapi.temp_read()

            csvreport1.write_data([chan,rate,backoff,dc_code,ref_code,sig_code,power,temp_code])
            print [chan,rate,backoff,dc_code,ref_code,sig_code,power,temp_code]


    def test_vdd33(self,rtc_en=0):
        title = 'vdd33_in, rtc_en, atten, num,sar_code,sar_dout0,sar_dout1,sar_dout2,sar_dout3,sar_dout4,sar_dout5,sar_dout6,sar_dout7\n'
        fname = self.wifi.get_filename('test_vdd33', 'test_vdd33_%s'%(rtc_en))
        csvreport1 = csvreport(fname, title)
        logsetlevel('I')
        self.awg = awg()

        self.pbus.pbus_debugmode()
##        code = self.wifiapi.get_sar2_vol(2) #do init reg

        if rtc_en==1:
             self.rtc_sar2_init(2)

        for i in range(0,40):
            vdd33 = 2.0 + i*0.05
            self.awg.appl('DC',0,0,vdd33)

            self.pbus.pbus_wr('rftx1', 'en1', 2)
            self.i2c.rftx.TE_PWDET=1

            for atten in range(0,4,1):
                for j in range(4):
                    sar_dout = []
                    if rtc_en==1:
                        self.rtc_sar2_set_atten(atten)
                        code =self.rtc_sar2_read()
                        for k in range(8):
                            sar_dout.append(self.rtc_sar2_read())
                    else:
##                        self.mem.wrm(0x6000e05c, 19,19, 1) #en test
##                        self.mem.wrm(0x6000e060, 4,3, atten) #atten
##                        self.mem.wrm(0x6000e05c, 23,23, 0) #use PKDET
##                        self.mem.wrm(0x6000e05c, 21,21, 1) #use TEMP
##                        code = self.wifiapi.read_sar2_code()
                        code = self.wifiapi.get_sar2_vol(atten)
                        for k in range(8):
                            sar_dout.append(self.mem.rd(0x6000e080+k*4))
                    csvreport1.write_data([vdd33,rtc_en, atten,j,code,sar_dout])
                    loginfo([vdd33,rtc_en, atten,j,code,sar_dout])

        self.i2c.rftx.TE_PWDET=0
        self.pbus.pbus_debugmode()

    def rtc_sar2_set_atten(self, atten=0):
        self.adc2.set(atten=atten, pad=0, test_pad_en=1)
        self.mem.wrm(0x60008830,30,19,0) #en pad

    def rtc_sar2_read(self):
        return self.adc2.read(0)

    def rtc_sar2_init(self, atten=2):
        self.pbus.pbus_debugmode()
        self.pbus.pbus_wr('rftx1', 'en1', 2)
        self.i2c.rftx.TE_PWDET=1
        self.adc2 = RTC_ADC2(self.comport, self.chipv)
        self.adc2.config()
        self.wifi.sar2_init_code(1400)
        self.rtc_sar2_set_atten(atten)
        return self.adc2.read(0)

    def test_vdd33_new(self,instr=''):
        title = 'vdd33_in, atten, num,phy_sar_code,rtc_sar_code,sar_dout0,sar_dout1\n'
        fname = self.wifi.get_filename('test_vdd33', 'test_vdd33_%s'%instr)
        csvreport1 = csvreport(fname, title)
        logsetlevel('I')
        self.awg = awg()

##        self.mem.wrm(0x6000e050, 15,8, 2) #sar clk div
##        self.mem.wrm(0x6000e050, 4, 2,1) #sar num

        for i in range(0,40):
            vdd33 = 2.0 + i*0.05
            self.awg.appl('DC',0,0,vdd33)
            time.sleep(0.1)

            for atten in range(0,4,1):
                for j in range(2):
                    sar_dout = []
                    code = self.wifiapi.test_phy_vdd33(atten, clk_div=1)
                    for k in range(2):
                        sar_dout.append(self.mem.rd(0x6000e080+k*4))
                    csvreport1.write_data([vdd33, atten,j,code,sar_dout])
                    loginfo([vdd33, atten,j,code,sar_dout])






