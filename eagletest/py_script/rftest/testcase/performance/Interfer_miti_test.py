from rftest.rflib.wifi_lib import WIFILIB
from rftest.rflib import *
import re
import baselib.test_channel.channel as chn
from baselib.loglib.log_lib import *
from baselib.instrument import *
import numpy as np
import time
from baselib.test_channel import *
from baselib.instrument.tester_serv import *
import sys
from baselib.instrument import *
import csv
from rftest.rflib.csv_report import csvreport
from rftest.rflib import rfglobal
from baselib.instrument.tester_serv import wt200_serv
from rftest.testcase.performance.wifi_txrx_test import WIFI_TXRX_TEST
from baselib.instrument import tester
from baselib.instrument.spa import HP,Agilent

class Interfer_Test(object):
    def __init__(self,comport,chipv='ESP32'):
        self.comport = comport
        self.chipv = chipv
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.txrx_test = WIFI_TXRX_TEST(self.comport,self.chipv)

    def iq_open(self,name=''):
        if name == 'iqxel':
            iqxel_serv.init()
            iqxel_serv.open_instru('192.168.100.252')
            loginfo('iqxel is opened')
            return -99
        elif name == 'wt200':
            wt200_serv.init()
            result=wt200_serv.open_instru('192.168.100.242')
            res1 = result.split(',')
            res_ID_1 = int(res1[1],10)
            return res_ID_1

        elif name == 'wt208c':
            wt200_serv.init()
            result=wt200_serv.open_instru('192.168.100.250')
            res2 = result.split(',')
            res_ID_2 = int(res2[1],10)
            return res_ID_2

    def iq_close(self,name=''):
        if name == 'iqxel':
            iqxel_serv.close()
            iqxel_serv.term()
        elif name == 'wt200':
            wt200_serv.close()
            wt200_serv.term()
        elif name == 'wt208c':
            wt200_serv.close()
            wt200_serv.term()

    def iq_vsg_stop(self,name=''):
        if name == 'iqxel':
            iqxel_serv.txenable(0)
        elif name == 'wt200':
            wt200_serv.txenable(0)
        elif name == 'wt208c':
            wt200_serv.txenable(0)

    def iq_sigout(self,name='',rf_freqMhz=2412,pwr=-10,ex_att=1,data_rate='11m',frmcnt=1,iqv_no=1,wave_gap=100):
        if name == 'iqxel':
            iqxel_serv.setvsg(rf_freqMhz,pwr+ex_att,iqv_no)
            iqxel_serv.setrate(data_rate)
            iqxel_serv.txenable(1)
            iqxel_serv.txfrmcnt(frmcnt)
            loginfo('TX iqxel is ready!');
        elif name == 'wt200':
            wt200_serv.setvsg(rf_freqMhz,pwr+ex_att,iqv_no)
            wt200_serv.setrate(data_rate)
            wt200_serv.txenable(1)
            wt200_serv.txfrmcnt(frmcnt,wave_gap)
            loginfo('TX wt200 is ready!');
        elif name == 'wt208c':
            wt200_serv.setvsg(rf_freqMhz,pwr+ex_att,iqv_no)
            wt200_serv.setrate(data_rate)
            wt200_serv.txenable(1)
            wt200_serv.txfrmcnt(frmcnt,wave_gap)
            loginfo('TX wt208c is ready!');


    def rx_sens_immunity(self,iq_signal='iqxel',iq_interfere='wt208c',interferce_type = 'tone', lost_list=[11.5], pwr_interfere_step=1, pwr_signal_step=1, packnum=100, iqv_signal_no=1,iqv_interfere_no=1,Module_Name='ESP32_Testboard',Module_Num=''):

        '''
        iq_signal='iqxel' and iq_interfere='wt200': iqxel is signal source, wt200 is interfere source

        '''
        title = 'freq_interfere,pwr_interfere,rx_chan, rate, sens, sens_rssi, sens_find\n'
        fname = self.wifi.get_filename('rx_sens_immunity', 'RXSens_immunity')
        csvreport2 = csvreport(fname, title)

        #cable_lose = lost_list[0]
        cable_lose_signal = lost_list[0]
        cable_lose_interfere = lost_list[1]
        cur_rate = '6m'
        cbw40m = self.wifi.rate2ht40(cur_rate)
        self.wifi.cbw40m_en(cbw40m)

        res_sig = self.iq_open(iq_signal)
        if interferce_type == 'tone':
            chan_signal_list = [6]
            freq_interfere_list  = [2440]
            mytester=tester.tester(freq_interfere_list[0],-100,'tone',1,iqv_interfere_no,'cw',cable_lose_interfere,isreset=1)
        elif interferce_type =='AWGN_noise':
            chan_signal_list = [6]
            freq_interfere_list  = [2437]
            mytester=tester.tester(freq_interfere_list[0],-100,'AWGN_noise',1,iqv_interfere_no,'source',cable_lose_interfere,isreset=1)
        elif interferce_type =='OFDM_noise':
            chan_signal_list = [6]
            freq_interfere_list  = [2412,2432,2462]
            #res_inf = self.iq_open(iq_interfere)
            mytester=tester.tester(freq_interfere_list[0],-100,'6m',1,iqv_interfere_no,'source',cable_lose_interfere,isreset=1)
        elif interferce_type =='OFDM_duty100':
            chan_signal_list = [1,6,11]
            freq_interfere_list  = [2437]
            #res_inf = self.iq_open(iq_interfere)
            mytester=tester.tester(freq_interfere_list[0],-100,'6m_D100',1,iqv_interfere_no,'source',cable_lose_interfere,isreset=1)

        chan_l = len(chan_signal_list)
        for j in range(0,chan_l):
            channel_signal = chan_signal_list[j]
            freq_signal = self.wifi.chan2freq(channel_signal)
            freq_l = len(freq_interfere_list)
            for k in range(0,freq_l):
                start_pwr_interfere = pwr_interfere_vs_data_rate[cur_rate][0]
                stop_pwr_interfere = pwr_interfere_vs_data_rate[cur_rate][1]
                freq_interfere = freq_interfere_list[k]
                if interferce_type =='OFDM_duty100':
                    freq_interfere = freq_signal
                pwr_interfere = start_pwr_interfere

                while pwr_interfere <= stop_pwr_interfere:

            		if interferce_type =="tone":
            		  mytester.txenable(1)
            		  mytester.txcw(freq_interfere,pwr_interfere,iqv_interfere_no)
            		elif interferce_type =="OFDM_noise":
            		  #wt200_serv._connID = res_inf
            		  #self.iq_sigout(iq_interfere,freq_interfere,pwr_interfere,cable_lose,cur_rate,0,iqv_interfere_no)
            		  mytester.sigout_txfrmcnt(freq_interfere,pwr_interfere,cable_lose_interfere,'6m',0,iqv_interfere_no)
            		elif interferce_type =="OFDM_duty100":
            		  #wt200_serv._connID = res_inf
            		  #self.iq_sigout(iq_interfere,freq_interfere,pwr_interfere,cable_lose,'6m_D100',0,iqv_interfere_no)
            		  mytester.sigout_txfrmcnt(freq_interfere,pwr_interfere,cable_lose_interfere,'6m_D100',0,iqv_interfere_no)
            		elif interferce_type =="AWGN_noise":
            		  mytester.sigout(freq_interfere,pwr_interfere,cable_lose_interfere,'AWGN_noise',0,iqv_interfere_no) # IQVIEW
            		  mytester.trig_wave(1);
            		time.sleep(1)
            		perform_list2=[]
            		pwr_signal_min=pwr_signal_vs_data_rate[cur_rate][0]
            		pwr_signal_max=pwr_signal_vs_data_rate[cur_rate][1]
            		pwr_signal = pwr_signal_min
            		name_str = '%s_%s_%s_%s_interferce_%s_%s'%(channel_signal, cur_rate, pwr_signal_min, pwr_signal_max,freq_interfere,pwr_interfere)
            		title = 'freq_interfere,pwr_interfere,rx_chan, rfpwr, rxnum, rssi, gain, noise, err, fcs, freq,maxrssi,minrssi\n'
            		fname = self.wifi.get_filename('rx_sens_immunity', 'RX_%s'%name_str, 'rx_sens_immunity')
            		csvreport1 = csvreport(fname, title)

            		while pwr_signal <= pwr_signal_max:

                		self.wifi.esp_rx(channel_signal, cur_rate)
                		wt200_serv._connID = res_sig
                		self.iq_sigout(iq_signal,freq_signal,pwr_signal,cable_lose_signal,cur_rate,packnum,iqv_signal_no)

                		result_data = self.wifi.cmdstop()
                		self.iq_vsg_stop(iq_interfere)
                		self.iq_vsg_stop(iq_signal)

                		[DesirePackNum, gain, rssi, noise, err, err2, freqoff, rssi_min, rssi_max] = self.wifi.rxresult(result_data)

                		loginfo(result_data)
                		perform_list2.append((pwr_signal,DesirePackNum,rssi,noise,err,err2, freqoff))
                		csvreport1.write_data([freq_interfere,pwr_interfere,channel_signal,pwr_signal,DesirePackNum,rssi,gain,noise,err,err2, freqoff])
                		pwr_signal = pwr_signal + pwr_signal_step

                	[cur_sense, cur_sense_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find, perform_list2] = self.txrx_test.get_data_sens(packnum, perform_list2)
                	csvreport2.write_data([freq_interfere,pwr_interfere,channel_signal,cur_rate,cur_sense,cur_sense_rssi,cur_sense_find])
                	pwr_interfere=pwr_interfere+pwr_interfere_step
                mytester.gen_switch('OFF',iqv_interfere_no)





    def Interference_test(self,iq_signal='iqxel',iq_interfere='wt208c', interferce_type = '', lost_list=[11.5], pwr_interfere_step=1, pwr_signal_step=1, packnum=100, iqv_signal_no=1,iqv_interfere_no=1,Module_Name='ESP32_Testboard',Module_Num=''):

        '''
        iq_signal='iqxel' and iq_interfere='wt200': iqxel is signal source, wt200 is interfere source

        '''
        logsetlevel("D")

        cable_lose_signal = lost_list[0]
        cable_lose_interfere = lost_list[1]

        rate_list=['11m']
        chan_signal_list = [2]
        freq_interfere_list  = [2442]

        res_sig = self.iq_open(iq_signal)
        #mytester=tester.tester(freq_interfere_list[0],-40,'6m',1,iqv_interfere_no,'source',cable_lose_interfere,isreset=1)
        res_inf = self.iq_open(iq_interfere)

        for cur_rate in rate_list:
            cbw40m = self.wifi.rate2ht40(cur_rate)
            self.wifi.cbw40m_en(cbw40m)
            chan_signal_l = len(chan_signal_list)
            interfere_rate = cur_rate
            if interferce_type == "OFDM_noise":
                freq_interfere_list  = [2437,2462]
                interfere_rate = '6m'
            elif interferce_type == "BT_noise":
                freq_interfere_list  = [2427,2437,2462]
                interfere_rate = '1dh3-0101'

            for j in range(0,chan_signal_l):
                channel_signal = chan_signal_list[j]
                freq_signal = self.wifi.chan2freq(channel_signal)
                freq_inter_l = len(freq_interfere_list)
                for k in range(0,freq_inter_l):
                    freq_interfere = freq_interfere_list[k]


                    pwr_signal_min=pwr_signal_vs_data_rate[cur_rate][0]
                    pwr_signal_max=pwr_signal_vs_data_rate[cur_rate][1]
                    pwr_signal = pwr_signal_min


                    while pwr_signal <= pwr_signal_max:

                        start_pwr_interfere = pwr_interfere_vs_data_rate[cur_rate][0]
                        stop_pwr_interfere = pwr_interfere_vs_data_rate[cur_rate][1]
                        pwr_interfere = start_pwr_interfere


                        name_str = '%s_%s_interfere_%s_%s_%s_@signal_%s'%(channel_signal, cur_rate, freq_interfere,start_pwr_interfere, stop_pwr_interfere,pwr_signal)
                        title = 'freq_interfere,pwr_interfere,rx_chan, rfpwr, rxnum, rssi, gain, noise, err, fcs, freq,maxrssi,minrssi\n'
                        fname = self.wifi.get_filename('Interference_test', 'RX_%s'%name_str, '%s_Sig_%s_Interfer_%s_%s'%(Module_Name,cur_rate,interfere_rate,freq_interfere))
                        csvreport1 = csvreport(fname, title)
                        perform_list2=[]

                        while pwr_interfere <= stop_pwr_interfere:

                    		#mytester.sigout_txfrmcnt(freq_interfere,pwr_interfere,cable_lose_interfere,cur_rate,0,iqv_interfere_no)
                    		wt200_serv._connID = res_inf
                    		self.iq_sigout(iq_interfere,freq_interfere,pwr_interfere,cable_lose_interfere,interfere_rate,0,iqv_interfere_no)
                    		time.sleep(1)

                    		self.wifi.rfchsel(channel_signal,0)
                    		self.wifi.rxstart(cur_rate, 0, 41)

                    		wt200_serv._connID = res_sig
                    		self.iq_sigout(iq_signal,freq_signal,pwr_signal,cable_lose_signal,cur_rate,packnum,iqv_signal_no)

                    		result_data = self.wifi.cmdstop()
                    		print result_data
                    		self.iq_vsg_stop(iq_interfere)
                    		self.iq_vsg_stop(iq_signal)

                    		[DesirePackNum, gain, rssi, noise, err, err2, freqoff, rssi_min, rssi_max] = self.wifi.rxresult(result_data)

                    		loginfo(result_data)
                    		perform_list2.append((pwr_signal,DesirePackNum,rssi,noise,err,err2, freqoff))
                    		csvreport1.write_data([freq_interfere,pwr_interfere,channel_signal,pwr_signal,DesirePackNum,rssi,gain,noise,err,err2, freqoff])
                    		pwr_interfere=pwr_interfere+pwr_interfere_step

                        [cur_sense, cur_sense_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find, perform_list2] = self.txrx_test.get_data_sens(packnum, perform_list2)
                        pwr_signal = pwr_signal + pwr_signal_step
                    #mytester.gen_switch('OFF',iqv_interfere_no)
        self.iq_close(iq_signal)
        self.iq_close(iq_interfere)





    def wifi_block_test(self,iq_signal='iqxel', instr_interfer='sme', lost_list=[8,6.3], rate_list=['1m'], pwr_signal_step=1, packnum=100, iqv_signal_no=1,Module_Name='ESP32_Testboard',Module_Num=''):

        '''
        iq_signal='iqxel' and iq_interfere='wt200': iqxel is signal source, wt200 is interfere source

        '''
        logsetlevel("D")

        cable_lose_signal = lost_list[0]
        cable_lose_interfere = lost_list[1]

        chan_signal_list = [1,13]

        freq_interfere_list  = {
        '0':[2380,2504],
        '1':[2300,2330,2360,2524,2584,2674],
        }
        pwr_interfere = -34

        if iq_signal == 'iqview':
            mytester=tester.tester(2412,-40,'54m',1,iqv_signal_no,'source',cable_lose_signal,isreset=1);
        else:
            res_sig = self.iq_open(iq_signal)

        if instr_interfer == 'sme':
            mysig_gen = sme.sme();# signal generator!
        elif instr_interfer == 'HP':
            self.spa = HP('SG',cfreq=2400,rb=30,span=1,reflvl=-40);#rb and span
            HP_SG_Revise_Power = 0.7

        for cur_rate in rate_list:
            cbw40m = self.wifi.rate2ht40(cur_rate)
            self.wifi.cbw40m_en(cbw40m)
            for channel_signal in  chan_signal_list:
                freq_signal = self.wifi.chan2freq(channel_signal)
                for num in range(0,2):
                    if num == 0:
                        freq_interfere_lst = freq_interfere_list[str(0)]
                        pwr_signal_org =  -68
                    else:
                        freq_interfere_lst = freq_interfere_list[str(1)]
                        pwr_signal_org =  -74

                    for k in freq_interfere_list:
                        freq_interfere = k

                        pwr_signal_min=pwr_signal_org - 10
                        pwr_signal_max=pwr_signal_org + 10
                        pwr_signal = pwr_signal_min

                        name_str = '%s_%s_interfere_%s_%s_@signal_%s_%s'%(channel_signal, cur_rate, freq_interfere,pwr_interfere,pwr_signal_min,pwr_signal_max)
                        title = 'freq_interfere,pwr_interfere,rx_chan, rfpwr, rxnum, rssi, gain, noise, err, fcs, freq,maxrssi,minrssi\n'
                        fname = self.wifi.get_filename('Interference_test', 'RX_%s'%name_str, '%s_Sig_%s_Interfer_%s'%(Module_Name,cur_rate,freq_interfere))
                        csvreport1 = csvreport(fname, title)
                        perform_list2=[]

                        while pwr_signal <= pwr_signal_max:

                            if instr_interfer == 'sme':
                                mysig_gen.setfreq(freq_interfere*1e6)
                                mysig_gen.setpow(pwr_interfere+cable_lose_interfere)
                                mysig_gen.rfon()
                            elif instr_interfer == 'HP':
                                self.spa.set_cfreq(cfreq=freq_interfere*1e6)
                                self.spa.set_pwr(pwr_interfere+cable_lose_interfere+HP_SG_Revise_Power);

                            time.sleep(1)

                            self.wifi.rfchsel(channel_signal,0)
                            self.wifi.rxstart(cur_rate, 0, 41)

                            if iq_signal == 'iqview':
                                mytester.sigout_txfrmcnt(freq_signal,pwr_signal,cable_lose_signal,cur_rate,packnum,iqv_signal_no)
                            else:
                                wt200_serv._connID = res_sig
                                self.iq_sigout(iq_signal,freq_signal,pwr_signal,cable_lose_signal,cur_rate,packnum,iqv_signal_no)

                            result_data = self.wifi.cmdstop()
                            print result_data
                            self.iq_vsg_stop(iq_signal)

                            [DesirePackNum, gain, rssi, noise, err, err2, freqoff, rssi_min, rssi_max] = self.wifi.rxresult(result_data)

                            loginfo(result_data)
                            perform_list2.append((pwr_signal,DesirePackNum,rssi,noise,err,err2, freqoff))
                            csvreport1.write_data([freq_interfere,pwr_interfere,channel_signal,pwr_signal,DesirePackNum,rssi,gain,noise,err,err2, freqoff])

                            [cur_sense, cur_sense_rssi, cur_sense_find, cur_max, cur_max_rssi, cur_max_find, perform_list2] = self.txrx_test.get_data_sens(packnum, perform_list2)
                            pwr_signal = pwr_signal + pwr_signal_step
        if iq_signal == 'iqview':
            mytester.gen_switch('OFF',iqv_signal_no)
        else:
            self.iq_close(iq_signal)
        if instr_interfer == 'sme':
            mysig_gen.rfoff()
        elif instr_interfer == 'HP':
            self.spa.close()



    def test_case(self,case_flag=0,iq_signal='iqxel',iq_interfere='wt200', lost_list=[6.5,5], pwr_interfere_step=1, pwr_signal_step=5, packnum=500, iqv_signal_no=1,iqv_interfere_no=1,Module_Name='ESP32',Module_Num=''):


        if case_flag & (1<<0):
            self.Interference_test(iq_signal=iq_signal,iq_interfere=iq_interfere,interferce_type = '', lost_list=lost_list, pwr_interfere_step=pwr_interfere_step, pwr_signal_step=pwr_signal_step, packnum=packnum, iqv_signal_no=iqv_signal_no,iqv_interfere_no=iqv_interfere_no,Module_Name=Module_Name,Module_Num=Module_Num)
        if case_flag & (1<<1):
            self.Interference_test(iq_signal=iq_signal,iq_interfere=iq_interfere, interferce_type = 'BT_noise',lost_list=lost_list, pwr_interfere_step=pwr_interfere_step, pwr_signal_step=pwr_signal_step, packnum=packnum, iqv_signal_no=iqv_signal_no,iqv_interfere_no=iqv_interfere_no,Module_Name=Module_Name,Module_Num=Module_Num)
        if case_flag & (1<<2):
            self.Interference_test(iq_signal=iq_signal,iq_interfere=iq_interfere, interferce_type = 'OFDM_noise',lost_list=lost_list, pwr_interfere_step=pwr_interfere_step, pwr_signal_step=pwr_signal_step, packnum=packnum, iqv_signal_no=iqv_signal_no,iqv_interfere_no=iqv_interfere_no,Module_Name=Module_Name,Module_Num=Module_Num)

#  For  RX  sensitivity
pwr_interfere_vs_data_rate ={
'6m': [-110,-40],
}
pwr_signal_vs_data_rate ={
'6m': [-100,-25],
}



##pwr_interfere_vs_data_rate ={
##'6m': [-80,-10],
##'mcs7': [-60,-10],
##'11m': [-35,-35],
##}
##pwr_signal_vs_data_rate ={
##'6m': [-90,-10],
##'mcs7': [-70,-10],
##'11m': [-70,-70]
##}