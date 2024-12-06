import time
import re
import csv
import os, sys
import socket
import matplotlib.pyplot as plt
import pylab
import numpy as np
import pandas
import xlrd
from openpyxl import *
import subprocess
from baselib.test_channel import sock
from baselib.instrument import dm,tester
from baselib.instrument.spa import HP,Agilent
from hal.wifi_api import WIFIAPI
from rftest.rflib.wifi_lib import WIFILIB
from baselib.instrument.tester_serv.instrum_server import instru_server
from rftest.testcase.current.current_meas import RF_Curr
from hal.Init import HALS
from hal.common import *
from hal.common import MEM
from hal.hwregister.hwi2c.all import *
import rftest.rflib.rfglobal as rfglobal
from rftest.rflib.rfpll import rfpll
from rftest.rflib.rfcal import rfcal
from rftest.rflib.pbus import pbus
import rftest.rflib.wifi_instrum as wifi_instrum
from baselib.loglib.log_lib import *
import rftest.rflib.utility.iofunc as iofunc
from rftest.rflib.csv_report import csvreport
from rftest.testcase.rf_debug.pa_test import PA_OutPwr
from rftest.testcase.rf_debug.tx_gain_sweep import Sweep_TX_Gain

class I2C_SWEEP(object):

    def __init__(self,comport,chipv):

        self.comport = comport
        self.chipv = chipv
        self.wifiapi = WIFIAPI(self.comport,self.chipv)
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.pa_test =PA_OutPwr(self.comport,self.chipv)
        self.sweep_tx_gain = Sweep_TX_Gain(self.comport,self.chipv)
        self.mem = MEM(self.comport, self.chipv)
        self.i2c = HWI2C(self.comport,self.chipv)
        self.rfpll = rfpll(self.comport, self.chipv)
        self.rfcal = rfcal(self.comport, self.chipv)
        self.pbus = pbus(self.comport, self.chipv)
        self.curr_data_path = 'D:/chip/eagletest/py_script/rftest/rfdata/i2c_auto_data/'
        self.hals = HALS(self.comport,self.chipv)
        self.rf_curr = RF_Curr(self.comport,self.chipv)

    def force_power_rf(self,cable_lose=2, chan=1,freq=2412, rate = 'mcs7',cbw40=0, target_power = 13,target_pwr_dis =0,curr_en=0, se_en=0,max_pwr=25,  num=10, iqv_no=2,reset_flag=0,path=''):
        """
        :brief:
            test tx performance at a target power
        """
        if rate == 'mcs7':
            atten1 = 11  #13dBm
        elif rate == '1m':
            atten1 = -14 #19.5dBm
        else:
            atten1 = -12 #19

        dig_atten = 256-atten1
        iqv_num = 1
        tt_max = 3
        if target_pwr_dis == 1:
            tt_min = tt_max -1
        else:
            tt_min = 0

        for tt in range(tt_min,tt_max):
            if tt ==2:
                iqv_num = num
            logdebug('dig_atten=%d'%dig_atten)
            self.wifi.cmdstop()
            self.wifiapi.set_tx_dig_gain(1,int(dig_atten))

            rate_index=self.wifi.ratecheck(rate)
            [len_byte, delay] = self.wifi.get_length_delay_duty(rate,0.2)
            self.wifi.txout(rate_sym=rate, PackNum=0, PackLen =len_byte, cbw40=cbw40, ht_dup=0, backoff_qdb=0, frm_delay=delay)

            if reset_flag == 0:
                myiqv = tester.tester(freq, max_pwr, rate, wifi_instrum.test_para(rate), iqv_no,'measure', cable_lose, 10, 1,0,20)
                reset_flag = 1
            else:
                myiqv = tester.tester(freq, max_pwr, rate, wifi_instrum.test_para(rate), iqv_no,'measure', cable_lose, 10, 0,0,20)

            [pwr, freq_err, clk_err, evm, evm_std, evm_max, lo_leakage,iq_imb_amp,iq_imb_phase,evm_list] = wifi_instrum.iqv_avg(myiqv, 1,'false', -15)
            [freq_mask, mask_marg] =  [[],[]]
            if evm < -5:
                [pwr, freq_err, clk_err, evm, evm_std, evm_max,lo_leakage,iq_imb_amp,iq_imb_phase, evm_list] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false', -15)

                [freq_mask, mask_marg] =  wifi_instrum.spectrum_mask_flatness(myiqv, iqv_num, 99)
            else:
                break
            print "Power=%2.2f"%pwr
            if tt<(tt_max - 1):
                dig_atten -= (pwr - target_power)*4

        curr =[]
        if curr_en == 1:
            curr =self.rf_curr.measure_current(plot=0, sample_rate=0.0005,sample_num=512,maxvalue=0.8,labels='', hold=0, color='blue', title='%s'%(rate)+'_chan'+str(chan),path=path)
##        self.wifi.cmdstop()
        w_str=[chan,rate,pwr,evm,evm_std,evm_max,freq_err,clk_err,lo_leakage,iq_imb_amp,iq_imb_phase,evm_list,mask_marg]

        return [w_str,int(256-dig_atten-atten1),curr]


    def i2c_EVM_MASK(self, cable_lose=2, channel=[1], sheetnamelist=['rftx'], curr_en=0, mask_en=0,  num=10, iqv_no=2):

        '''
        :brief:
            sweep i2c table, and use WIFI Insturment to test EVM and mask at a target power, find the best configuration of i2c
        :param:
            - cable_lose    : the lose of cable
            - channel       : 1~14
            - sheetnamelist : the sheet name in i2c table under test
            - curr_en       : enable current test
            - mask_en       : enable mask test
            - num           : user-defined
            - iqv_no        : 1 - left ; 2- right
        :return:
            csv report

        '''
        logsetlevel("I")
        if self.chipv == "CHIP724":
            i2c_table = self.curr_data_path+'/' +'chip724_sweep_i2c_reg_oktorun_simple.xlsm'
        if self.chipv == "CHIP723":
             i2c_table = self.curr_data_path+'/' +'chip723_sweep_i2c_reg_oktorun_simple.xlsm'
        if self.chipv == "CHIP722":
             i2c_table = self.curr_data_path+'/' +'chip722_sweep_i2c_reg_oktorun.xlsm'
        if self.chipv =="ESP32":
            i2c_table =  self.curr_data_path+'/' +"sweep_i2c_reg_new_test.xlsx"
        if self.chipv == "ESP8266":
            i2c_table =  self.curr_data_path+'/' +"esp8266_sweep_i2c_reg_new_test.xlsx"

        rfglobal.iqv['evm_sorted'] = 1

        workbook=xlrd.open_workbook(i2c_table)
        if sheetnamelist==[]:
            sheetnamelist=workbook.sheet_names()
        print sheetnamelist
        for sname in sheetnamelist:
            block=sname.encode('utf-8')
            i2c_regdict =pandas.read_excel(i2c_table,sheetname=block)

            title = 'i2c_ctrl_name, i2c_addr, msb, lsb, i2c_data_default, i2c_data, backoff_qdb, channel, rate, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage,iq_gain(dB),iq_phase(deg),'
            fname = self.wifi.get_filename('i2c_auto_data', 'TX_EVM_Test_i2c_block_%s'%(block), 'TX_EVM_Test_i2c_block')

            for chan in channel:
##            chan = channel[0]
                if mask_en == 1:
                    target_power = 18
                    rate = 'mcs0'
                else:
                    target_power = 13
                    rate ='mcs7'
                evm_lst_str =''
                for i in range(0,num,1):
                  evm_lst_str+= 'evm_%d,'%(i)
                title +=evm_lst_str
    ##            title +='lower4_freq,lower3_freq,lower2_freq,lower1_freq, upper1_freq,upper2_freq,upper3_freq, upper4_freq,'
                title +='lower4_marg,lower3_marg,lower2_marg,lower1_marg, upper1_marg,upper2_marg,upper3_marg, upper4_marg,'
                if  curr_en == 1:
                        title +='curr_pwr_1m, curr_max,curr_min,curr_avg,'
                csvreport1 = csvreport(fname, title+'\n')
##                chan = channel[0]
                reset_flag = 0
                max_pwr = 25-cable_lose

                loginfo("rate=%s, channel=%d"%(rate, chan))
                self.wifi.cmdstop()
                cbw40m = self.wifi.rate2ht40(rate)
                freq = self.wifi.chan2freq(chan)
                if self.chipv == "CHIP722":
                    self.wifiapi.rfchsel(chan,cbw40m*2)
                    self.wifiapi.set_tx_gain(0x5f, 0xa0)
                    #self.PA_reg_wr()
                elif self.chipv == "CHIP723":
                    self.wifi.rfchsel(1,0)
                    self.PA_reg_wr()
                    self.wifiapi.set_tx_gain(0x5f, 0x20)
                elif self.chipv == "CHIP724":
                    self.wifi.rfchsel(chan,0)
                    self.wifiapi.set_tx_gain(0x5e, 0x20)
                    self.wifiapi.set_tx_dig_gain(1,(256-12)) #256-bk
                else:
                    self.wifiapi.rfchsel(chan,cbw40m)

                for index in i2c_regdict.index:
                    data_wr_lst=[]
                    evm_lst=[]
                    backoff_lst=[]
                    addr=i2c_regdict.loc[index]["#addr"]
                    msb=i2c_regdict.loc[index]["msb"]
                    lsb=i2c_regdict.loc[index]["lsb"]
                    print "ctrl_name",i2c_regdict.loc[index]["ctrl_name"],i2c_regdict.loc[index]["ctrl_name"].split("[")[0]
                    ctrl_name=str(i2c_regdict.loc[index]["ctrl_name"].split("[")[0])
                    data_rd=self.wifi.i2c_ric(block, ctrl_name)
                    loginfo('data_rd=%d'%data_rd)
                    data_max = int(2**(msb-lsb+1))
                    step = int((data_max-1)/16)+1
                    print "data_max,step",data_max,step
                    for data_wr in range(0, data_max,step):
                        self.wifi.cmdstop()
                        self.wifi.i2c_wic(block, ctrl_name, data_wr)
                        w_str3 = []
                        w_str2 = self.force_power_rf(cable_lose=cable_lose, chan=chan, freq=freq,cbw40=cbw40m, rate =rate, target_power=target_power, target_pwr_dis =0,curr_en=0, max_pwr=max_pwr,  num=num, iqv_no=iqv_no,reset_flag=reset_flag,path=fname)
                        if curr_en == 1:
                            a = self.force_power_rf(cable_lose=cable_lose, chan=chan, freq=freq,cbw40=cbw40m, rate ='1m', target_power=19.5, target_pwr_dis =0,curr_en=curr_en, max_pwr=max_pwr,  num=1, iqv_no=iqv_no,reset_flag=0,path=fname)
                            pwr_1m = a[0][2]
                            curr = a[2]
                            w_str3 = [pwr_1m, curr[0],curr[1],curr[2]]

                        w_str =[ctrl_name, addr, msb, lsb, data_rd, data_wr,w_str2[1]]
                        data_wr_lst.append(data_wr)
                        evm_lst.append(w_str2[0][3])
                        backoff_lst.append(w_str2[1])


                        csvreport1.write_data(w_str+w_str2[0]+w_str3)


                    pylab.figure(200)
                    pylab.title("TX_EVM&Backoff_%s_%s"%(ctrl_name,rate))
                    pylab.subplot(1,2,1)
                    pylab.plot(data_wr_lst,evm_lst,label='%s'%(ctrl_name))

                    pylab.subplot(1,2,2)
                    pylab.plot(data_wr_lst,backoff_lst,label='%s'%(ctrl_name))
                    pylab.legend()
                    pylab.grid()
                    plt.savefig(self.curr_data_path+'/'+'pic'+'/'+'Tx_EVM&Power_%s_%s.png'%(ctrl_name,rate))
                    plt.close()

                    self.wifi.i2c_wic(block, ctrl_name, data_rd)

        rfglobal.iqv['evm_sorted'] = 0


    def i2c_EVM_MASK_SE(self, cable_lose=2, channel=[1], sheetnamelist=['rftx'], curr_en=0, mask_en=0,  se_en=0, plt_en=0,num=10, iqv_no=2):

        '''
        :brief:
            sweep i2c table, and use WIFI Insturment to test EVM and mask at a target power, find the best configuration of i2c
        :param:
            - cable_lose    : the lose of cable
            - channel       : 1~14
            - sheetnamelist : the sheet name in i2c table under test
            - curr_en       : enable current test
            - mask_en       : enable mask test
            - num           : user-defined
            - iqv_no        : 1 - left ; 2- right
        :return:
            csv report

        '''
        if self.chipv == "CHIP722":
             i2c_table = self.curr_data_path+'/' +'chip722_sweep_i2c_reg_oktorun.xlsm'
        if self.chipv =="ESP32":
            i2c_table =  self.curr_data_path+'/' +"sweep_i2c_reg_new_test.xlsx"

        rfglobal.iqv['evm_sorted'] = 1

        workbook=xlrd.open_workbook(i2c_table)
        if sheetnamelist==[]:
            sheetnamelist=workbook.sheet_names()
        print sheetnamelist
        for sname in sheetnamelist:
            block=sname.encode('utf-8')
            i2c_regdict =pandas.read_excel(i2c_table,sheetname=block)

            title = 'i2c_ctrl_name, i2c_addr, msb, lsb, i2c_data_default, i2c_data, backoff_qdb, channel, rate, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),'
            fname = self.wifi.get_filename('i2c_auto_data', 'TX_EVM_Test_i2c_block_%s'%(block), 'TX_EVM_Test_i2c_block')

            chan = channel[0]
            if mask_en == 1:
                target_power = 18
                rate = 'mcs0'
            else:
                target_power = 13
                rate ='mcs7'

            evm_lst_str =''
            for i in range(0,num,1):
              evm_lst_str+= 'evm_%d,'%(i)
            title +=evm_lst_str
##            title +='lower4_freq,lower3_freq,lower2_freq,lower1_freq, upper1_freq,upper2_freq,upper3_freq, upper4_freq,'
            title +='lower4_marg,lower3_marg,lower2_marg,lower1_marg, upper1_marg,upper2_marg,upper3_marg, upper4_marg,'
            if  curr_en == 1:
                title +='curr_pwr_1m, curr_max,curr_min,curr_avg,'

            if se_en==1:
                title +='SE_4.8GHz, SE_9.6GHz'
                self.spa = Agilent('SA',2412,device="N9020A")
                self.spa.set_param(9747,span=50,rb=100,vb=300)

            csvreport1 = csvreport(fname, title+'\n')
            chan = channel[0]
            reset_flag = 0
            max_pwr = 25-cable_lose
            loginfo("rate=%s, channel=%d"%(rate, chan))
            self.wifi.cmdstop()
            cbw40m = self.wifi.rate2ht40(rate)
            freq = self.wifi.chan2freq(chan)
            if self.chipv == "CHIP722":
                self.wifiapi.rfchsel(chan,cbw40m*2)
                self.wifiapi.set_tx_gain(0x5f, 0xa0)
                #self.PA_reg_wr()
            else:
                self.wifiapi.rfchsel(chan,cbw40m)

            for index in i2c_regdict.index:
                data_wr_lst=[]
                evm_lst=[]
                backoff_lst=[]
                addr=i2c_regdict.loc[index]["#addr"]
                msb=i2c_regdict.loc[index]["msb"]
                lsb=i2c_regdict.loc[index]["lsb"]
                print "ctrl_name",i2c_regdict.loc[index]["ctrl_name"],i2c_regdict.loc[index]["ctrl_name"].split("[")[0]
                ctrl_name=str(i2c_regdict.loc[index]["ctrl_name"].split("[")[0])
                data_rd=self.wifi.i2c_ric(block, ctrl_name)
                loginfo('data_rd=%d'%data_rd)
                data_max = int(2**(msb-lsb+1))
                step = int((data_max-1)/16)+1
                print "data_max,step",data_max,step
                for data_wr in range(0, data_max,step):
                    self.wifi.cmdstop()
                    self.wifi.i2c_wic(block, ctrl_name, data_wr)
                    w_str3 = []
                    w_str4=[]
                    w_str2 = self.force_power_rf(cable_lose=cable_lose, chan=chan, freq=freq,cbw40=cbw40m, rate =rate, target_power=target_power, target_pwr_dis =0,curr_en=0,max_pwr=max_pwr,  num=num, iqv_no=iqv_no,reset_flag=reset_flag,path=fname)
                    if curr_en == 1:
                        a = self.force_power_rf(cable_lose=cable_lose, chan=chan, freq=freq,cbw40=cbw40m, rate ='1m', target_power=19.5, target_pwr_dis =0,curr_en=curr_en, max_pwr=max_pwr,  num=1, iqv_no=iqv_no,reset_flag=0,path=fname)
                        pwr_1m = a[0][2]
                        curr = a[2]
                        w_str3 = [pwr_1m, curr[0],curr[1],curr[2]]

                    if se_en==1:
                        self.wifi.cmdstop()
                        self.force_power_rf(cable_lose=cable_lose, chan=chan, freq=freq,cbw40=cbw40m, rate ='1m', target_power=19.5, target_pwr_dis =0,curr_en=curr_en, max_pwr=max_pwr,  num=1, iqv_no=iqv_no,reset_flag=0,path=fname)
                        time.sleep(1)
                        self.spa.set_cfreq(2*freq)
##                        time.sleep(3)
                        result=self.spa.pk_search()
                        se_sec=result[0][1]
                        time.sleep(1)
                        self.spa.set_cfreq(4*freq)
##                        time.sleep(3)
                        result=self.spa.pk_search()
                        se_fth=result[0][1]
                        w_str4=[se_sec,se_fth]
                        print w_str4

                    w_str =[ctrl_name, addr, msb, lsb, data_rd, data_wr,w_str2[1]]
                    data_wr_lst.append(data_wr)
                    evm_lst.append(w_str2[0][3])
                    backoff_lst.append(w_str2[1])

                    csvreport1.write_data(w_str+w_str2[0]+w_str3+w_str4)

                if plt_en==1:
                    pylab.figure(200)
                    pylab.title("TX_EVM&Backoff_%s_%s"%(ctrl_name,rate))
                    pylab.subplot(1,2,1)
                    pylab.plot(data_wr_lst,evm_lst,label='%s'%(ctrl_name))

                    pylab.subplot(1,2,2)
                    pylab.plot(data_wr_lst,backoff_lst,label='%s'%(ctrl_name))
                    pylab.legend()
                    pylab.grid()
                    plt.savefig(self.curr_data_path+'/'+'pic'+'/'+'Tx_EVM&Power_%s_%s.png'%(ctrl_name,rate))
                    plt.close()

                self.wifi.i2c_wic(block, ctrl_name, data_rd)

        rfglobal.iqv['evm_sorted'] = 0


    def PA_reg_rd(self):

        print 'or_dvco_kvco',self.wifi.i2c_ric('rfpll','or_dvco_kvco') # default 1

        print 'lf_hbw',self.wifi.i2c_ric('rfpll','lf_hbw') # default 1
        print 'ir_ext_dchgp',self.wifi.i2c_ric('rfpll','ir_ext_dchgp') # default 7
        print 'cp1p6_dreg',self.wifi.i2c_ric('bias','cp1p6_dreg') #default 2

        print 'TMX2G_CCT_LOAD', self.wifi.i2c_ric('rftx','TMX2G_CCT_LOAD')

        print 'TMX2G_RCT_LOAD', self.wifi.i2c_ric('rftx','TMX2G_RCT_LOAD')
        print 'PA2G_CCT_STG1', self.wifi.i2c_ric('rftx','PA2G_CCT_STG1')
        print 'PA2G_CCT_STG2', self.wifi.i2c_ric('rftx','PA2G_CCT_STG2')

        print 'PA2G_ICT_STG0', self.wifi.i2c_ric('rftx','PA2G_ICT_STG0')
        print 'PA2G_ICT_STG0_CGM',self.wifi.i2c_ric('rftx','PA2G_ICT_STG0_CGM')
        print 'PA2G_ICT_STG1',self.wifi.i2c_ric('rftx','PA2G_ICT_STG1')
        if self.chipv == "CHIP722":
            print 'PA2G_ICT_STG1_CGM',self.wifi.i2c_ric('rftx','PA2G_ICT_STG1_CGM')
        print 'PA2G_ICT_STG2', self.wifi.i2c_ric('rftx','PA2G_ICT_STG2')

        print 'PA2G_CCT2F_STG0', self.wifi.i2c_ric('rftx','PA2G_CCT2F_STG0')

        print 'PA2G_MCT_CLASSB',self.wifi.i2c_ric('rftx','PA2G_MCT_CLASSB')
        print 'PA2G_RCT_STG2', self.wifi.i2c_ric('rftx','PA2G_RCT_STG2')

        print 'PA2G_STG1_SEL_ICGM',self.wifi.i2c_ric('rftx','PA2G_STG1_SEL_ICGM')
        if self.chipv == "CHIP722":
            print 'PA2G_STG1_SEL_ICGM_N',self.wifi.i2c_ric('rftx','PA2G_STG1_SEL_ICGM_N')
        elif self.chipv == "ESP32":
            print 'PA2G_STG0_SEL_ICGM_N',self.wifi.i2c_ric('rftx','PA2G_STG0_SEL_ICGM_N')

        print 'PA2G_VCT_CSC_STG0',self.wifi.i2c_ric('rftx','PA2G_VCT_CSC_STG0')
        print 'PA2G_VCT_CSC_STG1',self.wifi.i2c_ric('rftx','PA2G_VCT_CSC_STG1')
        print 'PA2G_VCT_CSC_STG2',self.wifi.i2c_ric('rftx','PA2G_VCT_CSC_STG2')
        if self.chipv == "CHIP722":
            print 'SPARE_TX',self.wifi.i2c_ric('rftx','SPARE_TX')


    def PA_reg_wr(self):

        # setting for evm, better 1dB
##        self.wifi.i2c_wic('rfpll','or_dvco_kvco',0)
##        self.wifi.i2c_wic('rfpll','lf_hbw',0) # default 1
##        self.wifi.i2c_wic('rfpll','ir_ext_dchgp',7) # default 7
##        self.wifi.i2c_wic('bias','cp1p6_dreg',7) #default 2
##
##
        self.wifi.i2c_wic('rftx','TMX2G_CCT_LOAD',11) # 3
        self.wifi.i2c_wic('rftx','TMX2G_RCT_LOAD',1) # 6
        self.wifi.i2c_wic('rftx','PA2G_CCT_STG1',11)  # 7
        self.wifi.i2c_wic('rftx','PA2G_CCT_STG2',4)  # 1
##        self.wifi.i2c_wic('bias','dres12k',14)
##        self.wifi.i2c_wic('bias','cgm_bias',3)
##        self.wifi.i2c_wic('rftx','PA2G_ICT_STG0',11)  # 8
##        self.wifi.i2c_wic('rftx','PA2G_ICT_STG0_CGM',0) #10
##
        self.wifi.i2c_wic('rftx','PA2G_ICT_STG1',8)     #6
##        self.wifi.i2c_wic('rftx','PA2G_ICT_STG1_CGM',10) #0
##
##        self.wifi.i2c_wic('rftx','PA2G_ICT_STG2',10)    # 8
##        self.wifi.i2c_wic('rftx','PA2G_CCT2F_STG0',0)   # 0
##
##        self.wifi.i2c_wic('rftx','PA2G_MCT_CLASSB',0)   # 0
##        self.wifi.i2c_wic('rftx','PA2G_RCT_STG2',0)     # 7
##
##        self.wifi.i2c_wic('rftx','PA2G_STG1_SEL_ICGM',1)   # 0
##        self.wifi.i2c_wic('rftx','PA2G_STG1_SEL_ICGM_N',1) # 1
##
##        self.wifi.i2c_wic('rftx','PA2G_VCT_CSC_STG0',10)  # 11
##        self.wifi.i2c_wic('rftx','PA2G_VCT_CSC_STG1',4)  # 5
##        self.wifi.i2c_wic('rftx','PA2G_VCT_CSC_STG2',10) # 4
##        self.wifi.i2c_wic('rftx','SPARE_TX',5)        # 7
##
##        self.wifi.i2c_wic('xtal','ir_xtal_dac_enx',1)
##        self.wifi.i2c_wic('rfpll','ir_enx_dchgp',1)



    def combi2c_EVM_MASK(self, cable_lose=2, channel=[1], sheetnamelist=['rftx'], curr_en=0, mask_en=0, target_pwr_dis=0, num=10, iqv_no=2):

        '''
        :brief:
            sweep the key i2c registers by combined way, and use WIFI Insturment to test EVM and mask, find the best combination configuration of i2c
        :param:
            - cable_lose    : the lose of cable
            - channel       : 1~14
            - sheetnamelist : the sheet name in i2c table under test
            - curr_en       : enable current test
            - mask_en       : enable mask test
            - num           : user-defined
            - iqv_no        : 1 - left ; 2- right
        :return:
            csv report
        '''


        i2c_table =  self.curr_data_path+'/' +'chip722_sweep_i2c_reg_oktorun.xlsm'
        #i2c_list = self.pa_test.i2c_table2list(sheetnamelist=sheetnamelist,step_auto=0,i2c_table=i2c_table)

        i2c_list = [
##            ['rfpll','ir_en_pll_mon','0:1:2'], #1
##            ['rfpll','ir_sel_fcnt_cal','0:1:2'],#0
##            ['rfpll','ir_ext_dchgp', '0:4:8'],#7
##            ['rfpll','enb_open_lf', '0:1:2'],#0
##            ['rfpll','dlref','0:3:4'],#3
##            ['rfpll','dhref','0:3:4'],#3
##            ['rfpll','bst_sf','0:1:2'],#0
##            ['rfpll','ir_acal_delay', '0:4:9'],#8
##            ['bias','cgm_bias','0:1:3'],#3
##            ['bias_marlin3','dres12k','2:1:4'],#7
##            ['bias_marlin3','rc_dvref','0:1:4'],#2
##            ['rftx','TMX2G_CCT_LOAD','14:2:16'],
##            ['rftx','TMX2G_RCT_LOAD','1:1:2'],
##            ['rftx','PA2G_CCT_STG1','14:2:16'],
####            ['rftx','PA2G_CCT_STG2','4:2:8'],
##            ['rftx','PA2G_ICT_STG0','6:2:12'],  # 3
            ['rftx','PA2G_ICT_STG0_CGM','0:1:4'],  # 4
            ['rftx','PA2G_ICT_STG1','6:1:9'],  # 3
            ['rftx','PA2G_ICT_STG1_CGM','8:2:15'], # 4
##            ['rftx','PA2G_STG1_SEL_ICGM','0:1:2'], # 0
##            ['rftx','PA2G_STG1_SEL_ICGM_N','0:1:2'], # 1
            ['rftx','PA2G_VCT_CSC_STG0','8:2:15'], # 4
##            ['rftx','PA2G_VCT_CSC_STG1','2:2:8'], # 3
##            ['rftx','PA2G_VCT_CSC_STG2','0:11:16'], # 8
##            #['rftx','PA2G_ICT_BIAS_PMOS','0:2:16'],
##            ['rftx','PA2G_RCT_STG2','0:1:8'],
##            ['rftx','PA2G_CCT_STG2','0:1:16'],
##            ['rftx','PA2G_MCT_CLASSB','0:2:4'],
        ]

        title ='channel, rate, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),'

        if mask_en == 1:
            target_power = 18
            rate = 'mcs0'
        else:
            target_power = 13
            rate ='mcs7'

        evm_lst_str =''
        rfglobal.iqv['evm_sorted'] = 1
        for i in range(0,num,1):
          evm_lst_str+= 'evm_%d,'%(i)
        title +=evm_lst_str
##        title +='lower4_freq,lower3_freq,lower2_freq,lower1_freq, upper1_freq,upper2_freq,upper3_freq, upper4_freq,'
        title +='lower4_marg,lower3_marg,lower2_marg,lower1_marg, upper1_marg,upper2_marg,upper3_marg, upper4_marg,'
        title +='backoff_qdb,'
        if  curr_en == 1:
                title +='curr_pwr_1m, curr_max,curr_min,curr_avg,'

        for header1 in  i2c_list:
            [block,ctrl_name,sweep_start,sweep_stop,sweep_step]=self.pa_test.get_sweep_cmd(header1);
            title +='%s,'%(ctrl_name);

        fname = self.wifi.get_filename('i2c_auto_data', 'TX_EVM_Test_combi2c_block')
        csvreport1 = csvreport(fname, title+'\n')

        chan = channel[0]
        reset_flag = 0
        loop = 0
        max_pwr = 25-cable_lose
        logdebug("rate=%s, channel=%d"%(rate, chan))
        self.wifi.cmdstop()
        cbw40m = self.wifi.rate2ht40(rate)
        self.wifiapi.rfchsel(chan,cbw40m)
        freq = self.wifi.chan2freq(chan)
        if self.chipv == "CHIP722":
                self.wifiapi.rfchsel(chan,cbw40m*2)
                self.wifiapi.set_tx_gain(0x5f, 0xa0)
        elif  self.chipv == "CHIP723":
                self.wifi.rfchsel(1,0)
##                self.PA_reg_wr()
                self.wifiapi.set_tx_gain(0x5f, 0x20)
        else:
                self.wifiapi.rfchsel(chan,cbw40m)

        sweep_list = self.comb_i2clist(i2c_list)

        logdebug(sweep_list,len(sweep_list))
        for y in range(0,len(sweep_list),1):
            self.wifi.cmdstop()
            if isinstance(sweep_list[y][0],list):
                for list1 in sweep_list[y]:
                    self.wifi.i2c_wic(list1[0],list1[1],int(list1[2]))
            else:
                self.wifi.i2c_wic(sweep_list[y][0],sweep_list[y][1],int(sweep_list[y][2]))
            w_str3 = []
            w_str2 = self.force_power_rf(cable_lose=cable_lose, chan=chan, freq=freq,cbw40=cbw40m, rate =rate, target_power=target_power,target_pwr_dis=target_pwr_dis,  curr_en=0, max_pwr=max_pwr,  num=num, iqv_no=iqv_no,reset_flag=reset_flag,path=fname)
            if curr_en == 1:
                a = self.force_power_rf(cable_lose=cable_lose, chan=chan, freq=freq,cbw40=cbw40m, rate ='1m', target_power=19.5, target_pwr_dis =0, curr_en=curr_en, max_pwr=max_pwr,  num=1, iqv_no=iqv_no,reset_flag=0,path=fname)
                pwr_1m = a[0][2]
                curr = a[2]
                w_str3 = [pwr_1m, curr[0],curr[1],curr[2]]
            w_str = []
            if isinstance(sweep_list[y][0],list):
                for list1 in sweep_list[y]:
                    w_str.append(self.wifi.i2c_ric(list1[0],list1[1]))
            else:
                 w_str.append(self.wifi.i2c_ric(sweep_list[y][0],sweep_list[y][1]))
            print w_str

            csvreport1.write_data(w_str2[0]+[w_str2[1]]+w_str3+w_str)
        rfglobal.iqv['evm_sorted'] = 0


    def comb_array(self,array1=[['a1','a2',0],['a1','a2',1]],array2=[['x1','x2',0],['x1','x2',1]]):

        comb_array = []
        list1 = []
        for list1 in array1:
            for list2 in array2:
                #print 1111,list1,list2
                if len(list1)>1 and  not isinstance(list1[0],str) :
                    comb_array.append(list1 +[list2])
                else:
                    comb_array.append([list1,list2])
        return comb_array


    def comb_i2clist(self,sweep_list1=[]):

        cmd_list_all=[]
        cmd_list_all_comb = []

        for list1 in  sweep_list1:
            cmd_sweep_param_list = []
            cmd_list = self.pa_test.get_sweep_cmd(list1)
            for kk0 in range(cmd_list[2], cmd_list[3],  cmd_list[4]):
                cmd_sweep_param_list.append ([cmd_list[0], cmd_list[1], kk0])
            cmd_list_all.append(cmd_sweep_param_list)
        #logdebug(cmd_list_all)
        cmd_list_all_comb = cmd_list_all[0];
        for kk0 in range(1,len(cmd_list_all)):
            cmd_list_all_comb = self.comb_array(cmd_list_all_comb,cmd_list_all[kk0])

        return cmd_list_all_comb


    def read_i2creg_all(self):
        filetime = time.strftime('_%Y%m%d_%H%M%S',time.localtime(time.time()));
        chip_id=CHIP_ID(self.comport,self.chipv).chip_mac()
        folder = "d:/chip/eagletest/rfdata/"+'read_i2creg_all_'+chip_id+filetime
        data_path = folder+'/'
        isexist=os.path.exists(folder)
        if not isexist:
            os.makedirs(folder)

        i2c_table = "./hal/hwregister/hwi2c/%s/csv/i2c_table.xlsm"%self.chipv
        sheetnamelist=("rftx","rfrx","bias","xtal","rfpll")
        for sname in sheetnamelist:
            block=sname.encode('utf-8')
            i2c_regdict =pandas.read_excel(i2c_table,sheetname=block)
            with open(data_path+'read_i2creg_%s_%s.csv'%(block,filetime),'w') as i2c_evm_file:
                i2c_evm_file.write('i2c_addr, msb, lsb, i2c_ctrl_name, rw, i2c_data_default\n')
                w_str = ''
                for index in i2c_regdict.index:
                    addr=i2c_regdict.loc[index]["#addr"]
                    msb=i2c_regdict.loc[index]["msb"]
                    lsb=i2c_regdict.loc[index]["lsb"]
                    ctrl_name=i2c_regdict.loc[index]["ctrl_name"].split("[")[0]
                    rw=i2c_regdict.loc[index]["rw"]
                    #block=str.upper(block)
                    data_rd_str="self.hals.HWI2C.%s.%s"%(block,ctrl_name)
                    data_rd=eval(data_rd_str)
                    logdebug('data_rd=%d'%data_rd)

                    w_str += "%d, %d, %d, %s,%s, %d\n"%( addr, msb, lsb,ctrl_name,rw, data_rd)
                i2c_evm_file.write(w_str)

    def read_i2creg_all_loop(self,loop,i2c_table_out="d:/chip/eagletest/rfdata/i2c_table.xlsm"):
        if self.chipv=="ESP8266":
            sheetnamelist=("bias","bbpll","bbtx","bbrx","rftx","rfrx","saradc","xtal","rfpll","ckgen","rfpll_sdm","dig_fe","dig_inf")
        if self.chipv=="ESP32":
            sheetnamelist=("bias","bbpll","bbtop","rftx","rfrx","saradc","xtal","rfpll","ckgen","rfpll_sdm","dig_fe","apll")

        i2c_regdict_wr_list=[]
        for sname in sheetnamelist:
            block=sname.encode('utf-8')
            i2c_regdict =pandas.read_excel(i2c_table_out,sheetname=block)
            i2c_regdict_wr=pandas.DataFrame(i2c_regdict)
            i2c_regdict_wr_list.append([block,i2c_regdict_wr])
##            print i2c_regdict_wr_list
        column=str(loop)
            #print i2c_regdict
        for i in range(0,len(i2c_regdict_wr_list)):
##                print i2c_regdict_wr_list[i][1]
            data_rd_list=[]
            for index in i2c_regdict_wr_list[i][1].index:
                ctrl_name=i2c_regdict_wr_list[i][1].loc[index]["ctrl_name"].split("[")[0]
                block=str.upper(i2c_regdict_wr_list[i][0])
                data_rd_str="self.hals.HWI2C.%s.%s"%(block,ctrl_name)
                data_rd=eval(data_rd_str)
                logdebug('data_rd=%d'%data_rd)
                data_rd_list.append(data_rd)
            writer=pandas.ExcelWriter(i2c_table_out)
            book=load_workbook(i2c_table_out)
            writer.book=book
            writer.sheets=dict((ws.title,ws) for ws in book.worksheets)
            data_wr=pandas.DataFrame(i2c_regdict_wr_list[i][1])
            data_wr[column]=data_rd_list
##                print data_wr
            data_wr.to_excel(writer,str.lower(block),index=False)
            writer.save()

    def tx_read_allreg(self,chan,rate_sym, PackNum=1,loop_num=5,i2c_table_out="d:/chip/eagletest/rfdata/i2c_table.xlsm"):
        self.wifi.rfchsel(chan)
        for loop in range(0,loop_num):
            self.wifi.txout(rate_sym, PackNum)
            self.wifi.cmdstop()
            self.read_i2creg_all_loop(loop,i2c_table_out)
##
##
##
##
##    def i2c_EVM_default_rftx_setting(self):
##        self.wifi.i2c_wic('rftx', 'TMX2G_CCT_LOAD', 15)
##        self.wifi.i2c_wic('rftx','TMX2G_RCT_LOAD',6)
##        self.wifi.i2c_wic('rftx','PA2G_CCT_STG1',7)
##        self.wifi.i2c_wic('rftx','PA2G_CCT_STG2',3)
##        self.wifi.i2c_wic('rftx','PA2G_ICT_STG0',8)
##        self.wifi.i2c_wic('rftx','PA2G_ICT_STG0_CGM',10)
##        self.wifi.i2c_wic('rftx','PA2G_ICT_STG1',6)
##        self.wifi.i2c_wic('rftx','PA2G_ICT_BIAS_PMOS',0)
##        self.wifi.i2c_wic('rftx','PA2G_ICT_STG2',8)
##        self.wifi.i2c_wic('rftx','PA2G_CCT2F_STG0',0)
##        self.wifi.i2c_wic('rftx','PA2G_MCT_CLASSB',0)
##        self.wifi.i2c_wic('rftx','PA2G_RCT_STG2',7)
##        self.wifi.i2c_wic('rftx','PA2G_STG1_SEL_ICGM',0)
##        self.wifi.i2c_wic('rftx','PA2G_STG0_SEL_ICGM_N',1)
##        self.wifi.i2c_wic('rftx','PA2G_VCT_CSC_STG0',11)
##        self.wifi.i2c_wic('rftx','PA2G_VCT_CSC_STG1',5)
##        self.wifi.i2c_wic('rftx','PA2G_VCT_CSC_STG2',4)
##        self.wifi.i2c_wic('rftx','PA2G_PKDET_EN',0)
##        self.wifi.i2c_wic('rftx','PWDET_VTH_TUNE',4)
##        self.wifi.i2c_wic('rftx','PWDET_ICT_OUTPUT',3)
##        self.wifi.i2c_wic('rftx','PWDET_VCT_REF',1)
##        self.wifi.i2c_wic('rftx','PA2G_CCT2F_STG0_GATE',7)
##
##    def i2c_EVM_better_rftx_setting(self):
####        self.wifi.i2c_wic('rftx', 'TMX2G_CCT_LOAD', 1)  #default is 15
##
##        self.wifi.i2c_wic('rftx','TMX2G_RCT_LOAD',7)   #default is 6
##        self.wifi.i2c_wic('rftx','PA2G_CCT_STG1',0)#default is 7
####        self.wifi.i2c_wic('rftx','PA2G_CCT_STG2',1)#default is 3
####        self.wifi.i2c_wic('rftx','PA2G_ICT_STG0',8)#default is 8
####        self.wifi.i2c_wic('rftx','PA2G_ICT_STG0_CGM',10)#default is 10
##        self.wifi.i2c_wic('rftx','PA2G_ICT_STG1',7)#default is 6
####        self.wifi.i2c_wic('rftx','PA2G_ICT_BIAS_PMOS',1)#default is 0
##        self.wifi.i2c_wic('rftx','PA2G_ICT_STG2',15)#default is 8
####        self.wifi.i2c_wic('rftx','PA2G_CCT2F_STG0',15)#default is 0
####        self.wifi.i2c_wic('rftx','PA2G_MCT_CLASSB',0)#default is 0
####        self.wifi.i2c_wic('rftx','PA2G_RCT_STG2',4)#default is 7
####        self.wifi.i2c_wic('rftx','PA2G_STG1_SEL_ICGM',0)#default is 0
####        self.wifi.i2c_wic('rftx','PA2G_STG0_SEL_ICGM_N',1)#default is 1
####        self.wifi.i2c_wic('rftx','PA2G_VCT_CSC_STG0',13)#default is 11
####        self.wifi.i2c_wic('rftx','PA2G_VCT_CSC_STG1',1)#default is 5
####        self.wifi.i2c_wic('rftx','PA2G_VCT_CSC_STG2',4)#default is 4
####        self.wifi.i2c_wic('rftx','PA2G_PKDET_EN',4)#default is 4
####        self.wifi.i2c_wic('rftx','PWDET_VTH_TUNE',15)#default is 4
####        self.wifi.i2c_wic('rftx','PWDET_ICT_OUTPUT',2)#default is 3
####        self.wifi.i2c_wic('rftx','PWDET_VCT_REF',1)#default is 1
####        self.wifi.i2c_wic('rftx','PA2G_CCT2F_STG0_GATE',6)#default is 7
####       self.wifi.i2c_wic('rftx','TE_PA2G',1)#default is 0
##
##    def tx_test(self, cable_lose=2, channel=[1], num=10,mask_en=0, iqv_no=2,sel=0,setting=''):
##
##        filetime = time.strftime('_%Y%m%d_%H%M%S',time.localtime(time.time()));
##        folder = self.curr_data_path+'TX_EVM_Test_%s_%s'%(filetime,setting)
##        data_path = folder+'/'
##        os.mkdir(folder)
##        with open(data_path+'TX_EVM_Test_%s_%s.csv'%(filetime,setting),'ab+') as file1:
##                file1.write('backoff, channel, rate, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),')
##                chan = channel[0]
##                if mask_en == 1:
##                    target_power = 19
##                    rate = 'mcs0'
##                    evm_list_en = 0
##                    file1.write('lower4_freq,lower4_marg, lower3_freq, lower3_marg, lower2_freq, lower2_marg, lower1_freq,lower1_marg, upper1_freq, upper1_marg,upper2_freq,upper2_marg, upper3_freq, upper3_marg, upper4_freq,upper4_marg,')
##                else:
##                    target_power = 13
##                    rate ='mcs7'
##                    evm_list_en = 1
##                    evm_lst_str =''
##                    for i in range(0,num,1):
##                      evm_lst_str+= 'evm_list_%d,'%(i)
##                    file1.write(evm_lst_str)
##                file1.write('\n')
##                chan = channel[0]
##                reset_flag = 0
##                loop = 0
##                max_pwr = 25-cable_lose
##                logdebug("rate=%s, channel=%d"%(rate, chan))
##                self.wifi.cmdstop()
##                cbw40m = self.wifi.rate2ht40(rate)
##                self.wifiapi.rfchsel(chan,cbw40m)
##                freq = self.wifi.chan2freq(chan)
##                [len_byte, delay] = self.wifi.get_length_delay_duty(self.wifi.ratecheck(rate),0.2)
##                if sel==1:
##
##                    logdebug("-------")
##                    self.i2c_EVM_better_rftx_setting()
###                    self.i2c_EVM_better_bias_setting()
##                    logdebug("-------")
##                elif sel == 0:
##                    logdebug("-------")
##                    self.i2c_EVM_default_rftx_setting()
##                    self.i2c_EVM_default_bias_setting()
##                    logdebug("-------")
##
##                w_str1 = ''
##                w_str1 = self.force_power_rf(cable_lose=cable_lose, chan=chan, freq=freq,cbw40=cbw40m, rate =rate, len_byte=len_byte, delay=delay, target_power=target_power, evm_list_en = evm_list_en, max_pwr=max_pwr,  num=num, iqv_no=iqv_no,reset_flag=reset_flag)
##                print w_str1[0]
##                w_str2=''
##                w_str2 = '%d,'%(w_str1[1])
##                print w_str2
####                self.wifi.txout(rate_sym='mcs7', PackNum=0, PackLen =len_byte, cbw40=0, ht_dup=0, backoff_qdb=w_str[1], frm_delay=delay)
##                file1.write(w_str2 + w_str1[0]+'\n')
##
##    def i2c_EVM_default_bias_setting(self):
##        self.wifi.i2c_wic('bias', 'cp1p6_dreg', 2)
####        self.wifi.i2c_wic('bias', 'cgm_bias', 2)
####        self.wifi.i2c_wic('bias', 'dres12k', 8)
####        self.wifi.i2c_wic('bias', 'rc_div', 11)
####        self.wifi.i2c_wic('bias', 'rc_chg_count', 2)
####        self.wifi.i2c_wic('bias', 'cp1p1_pvt_reg', 2)
##
##    def i2c_EVM_better_bias_setting(self):
##        self.wifi.i2c_wic('bias', 'cp1p6_dreg', 0)
####        self.wifi.i2c_wic('bias', 'cgm_bias', 3)
####        self.wifi.i2c_wic('bias', 'dres12k', 11)
####        self.wifi.i2c_wic('bias', 'rc_div', 5)
####        self.wifi.i2c_wic('bias', 'rc_chg_count', 10)
####        self.wifi.i2c_wic('bias', 'cp1p1_pvt_reg',3)

