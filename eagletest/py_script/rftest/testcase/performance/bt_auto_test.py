from rftest.rflib.wifi_lib import WIFILIB
from hal.bt_api import BTAPI
from hal.common import MEM
import win32com
import win32com.client
from win32com.client import Dispatch, constants, gencache
from docx import Document
import re
import baselib.test_channel.channel as chn
from baselib.loglib.log_lib import *
from baselib.plot import *
from baselib.instrument import *
import numpy as np
import scipy
from math import *
from shutil import copy
import time
import csv
import pylab
import matplotlib.pyplot as plt
from baselib.test_channel import *
import xlrd
from baselib.instrument.tester_serv import *
import sys
import random
from baselib.plot import mfunc
from baselib.instrument import *
from rftest.rflib import *
from baselib.instrument import tester
from rftest.rflib import bt_instrum
from rftest.rflib.csv_report import csvreport
import os
from hal.common import MEM
from rftest.testcase.performance.Interfer_miti_test import Interfer_Test
rate_bps_dict = rfglobal. rate_bps_dict
drate2name = bt_instrum.drate2name
name2drate = bt_instrum.name2drate
DH2name = bt_instrum.DH2name
name2DH = bt_instrum.name2DH
dtype2name = bt_instrum.dtype2name
name2dtype = bt_instrum.name2dtype

global test_case_information



class BtAutoTest(object):

    def __init__(self,comport,chipv='ESP32'):
        self.comport = comport
        self.chipv = chipv
        self.bt = BTAPI(self.comport,self.chipv)
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.mem = MEM(self.comport,self.chipv)
        self.interfer_test = Interfer_Test(self.comport,self.chipv)
        self.rf_bt_autotest_data = "D:/chip/eagletest/py_script/rftest/rfdata/bt_auto_data/"
        self.folder = 'bt_auto_data'

#-##############-----BT Transmitter---------############-#

    def BT_TX_PWR_EVM(self,cable_loss=1.5,pwr_level=[0,8], channel=[0,78],rate_lst = ['1M_DH1_1010'],iqv_no=1, iqv_num=10,file_w='BT_TX'):
        """
        --iqv_no: 1-left port, 2-right port
        --iqv_num: iqview average number
        """
        '''
        BT_rate :    1 : 1M;   2 : 2M:  3 : 3M
        DH_type :    1 : DH1;  3 : DH3; 5 : DH5
        data_type :  0 : 1010; 1 : 00001111; 2 : prbs9
        chan : BT tx channel set (0 to 78)
        '''
        maxpwracpfreq_title ='Lower_freq1,lower_freq2,lower_freq3,upper_freq3,upper_freq2,upper_freq3,'
        maxpweracpmargin_title = 'lower_margin1,lower_margin2,lower_margin3,upper_margin3,upper_margin2,upper_margin1,'

        title = 'rate, channel, power_level,power(dbm),Init Freq Err(kHz),deltaF1Avg(kHz), deltaF2Max(kHz), deltaF2Avg(kHz), bandwidth20dB(kHz),OMEGA_I(kHz),OMEGA_O(kHz),OMEGA_IO(kHz), DEVM Average,DEVM Peak,EdrprobEVM99pass(%),EdrEVMvalid,EdrPowDiffdB(dB),'
        title += maxpwracpfreq_title + maxpweracpmargin_title +'\n'
        fname = self.wifi.get_filename(self.folder+'/'+file_w,'BT_tx_pwr_evm_%s'%(rate_lst[0]),'TX')
        fw1=csvreport(fname,title)

        max_pwr = 18 - cable_loss
        self.bt.fcc_bt_tx(pwr_level=8,FH_en=0,tx_chan=0,rate=1,DH=1,datatype=0)
        myiqv=tester.tester(2402, max_pwr, '1M_DH1_1010', [1,'All'], iqv_no,'measure', cable_loss, 10, 1, 1, 150)

        for rate_name in rate_lst:
            [LE_EN,data_rate,DH_type,data_type] = bt_instrum.name2rate(rate_name)
            drate = data_rate
            DH = DH_type
            dtype = data_type
            for pwr_lev in pwr_level:
                max_pwr =-12+6+pwr_lev*3-cable_loss
                for chan in  channel:
                    freq = 2402+chan

                    self.wifi.cmdstop()
                    loginfo("pwr_level=%d, channel=%d, freq=%d, data_rate=%d, DH_type=%d, data_type=%d,"%(pwr_lev, chan, freq, drate, DH, dtype))

                    self.bt.fcc_bt_tx(pwr_lev, 0, chan, drate, DH, dtype)
                    myiqv=tester.tester(freq, max_pwr, rate_name, [drate,'All'], iqv_no,'measure', cable_loss, 10, 0, 1, 150)

                    [tx_result]=bt_instrum.iqv_bt_avg(rate_name,myiqv,iqv_num)
                    [maxPowerAcpFreqHz,maxPowerAcpDbm] = bt_instrum.max_Power_Acp(myiqv,iqv_num)
                    fw1.write_data([rate_name,freq,pwr_lev,tx_result,maxPowerAcpFreqHz,maxPowerAcpDbm])




    def LE_TX_PWR_EVM(self,cable_loss=1.5,pwr_level=[0,8], channel=[0,39],rate_lst=['LE_1M_1010'],iqv_no=1, iqv_num=10,file_w='LE_TX'):
        """
        --iqv_no: 1-left port, 2-right port
        --iqv_num: iqview average number
        """
        '''
        LE_rate : 0 : 1M;   1 : 2M:  2 : 125K   3 : 500
        tx_chan : BT tx channel set (0 to 39)
        '''
        maxpwracpfreq_title ='Lower_freq1,lower_freq2,lower_freq3,upper_freq3,upper_freq2,upper_freq3'
        maxpweracpmargin_title = 'lower_margin1,lower_margin2,lower_margin3,upper_margin3,upper_margin2,upper_margin1'

        title = 'rate, channel, power_level,power(dbm),Init Freq Err(kHz),deltaF1Avg(kHz), deltaF2Max(kHz), deltaF2Avg(kHz),pwr_le_pk(dBm),%s,%s\n'%(maxpwracpfreq_title,maxpweracpmargin_title)
        fname = self.wifi.get_filename(self.folder+'/'+file_w,'LE_tx_pwr_evm_%s'%(rate_lst[0]),'TX')
        fw1 = csvreport(fname,title)

        max_pwr = 18 - cable_loss

        self.bt.fcc_le_tx(8, 0, 250, 2, 0)
        myiqv=tester.tester(2402, max_pwr, 'LE_1M_prbs9', [0,'All'], iqv_no,'measure', cable_loss, 10, 1, 1, 150)

        for rate_name in rate_lst:
            [LE_EN,data_rate,DH_type,data_type] = bt_instrum.name2rate(rate_name)
            drate = data_rate
            DH = DH_type
            dtype = data_type
            for pwr_lev in pwr_level:
                max_pwr =-12+6+pwr_lev*3-cable_loss
                for chan in  channel:
                    freq = 2402+chan*2

                    self.wifi.cmdstop()
                    loginfo("pwr_level=%d, channel=%d, freq=%d, data_rate=%d, data_type=%d,"%(pwr_lev, chan, freq, drate, dtype))

                    self.bt.fcc_le_tx(pwr_lev, chan, 250, dtype, drate)
                    myiqv=tester.tester(freq, max_pwr, rate_name, [0,'All'], iqv_no,'measure', cable_loss, 10, 0, 1, 150)

                    [tx_result]=bt_instrum.iqv_bt_avg(rate_name,myiqv,iqv_num)
                    [maxPowerAcpFreqHz,maxPowerAcpDbm] = bt_instrum.max_Power_Acp(myiqv,iqv_num)
                    fw1.write_data([rate_name,freq,pwr_lev,tx_result,maxPowerAcpFreqHz,maxPowerAcpDbm])



    def BT_TX_PWR_EVM_freq_offset(self,cable_loss=1.5,pwr_level=[0,8], channel=[0,78],rate_lst = ['1M_DH1_1010'],iqv_no=1, iqv_num=10,file_w='BT_TX'):
        """
        --iqv_no: 1-left port, 2-right port
        --iqv_num: iqview average number
        """
        '''
        BT_rate :    1 : 1M;   2 : 2M:  3 : 3M
        DH_type :    1 : DH1;  3 : DH3; 5 : DH5
        data_type :  0 : 1010; 1 : 00001111; 2 : prbs9
        chan : BT tx channel set (0 to 78)
        '''
        maxpwracpfreq_title ='Lower_freq1,lower_freq2,lower_freq3,upper_freq3,upper_freq2,upper_freq3,'
        maxpweracpmargin_title = 'lower_margin1,lower_margin2,lower_margin3,upper_margin3,upper_margin2,upper_margin1,'

        title = 'rate, channel, power_level,power(dbm),Init Freq Err(kHz),deltaF1Avg(kHz), deltaF2Max(kHz), deltaF2Avg(kHz), bandwidth20dB(kHz),OMEGA_I(kHz),OMEGA_O(kHz),OMEGA_IO(kHz), DEVM Average,DEVM Peak,EdrprobEVM99pass(%),EdrEVMvalid,EdrPowDiffdB(dB),'
        title += maxpwracpfreq_title + maxpweracpmargin_title +'\n'
        fname = self.wifi.get_filename(self.folder+'/'+file_w,'BT_tx_pwr_evm_%s'%(rate_lst[0]),'TX')
        fw1 = csvreport(fname,title)

        max_pwr = 18 - cable_loss
        self.bt.fcc_bt_tx(pwr_level=8,FH_en=0,tx_chan=0,rate=1,DH=1,datatype=0)
        myiqv=tester.tester(2402, max_pwr, '1M_DH1_1010', [1,'All'], iqv_no,'measure', cable_loss, 10, 1, 1, 150)

        for rate_name in rate_lst:
            [LE_EN,data_rate,DH_type,data_type] = bt_instrum.name2rate(rate_name)
            drate = data_rate
            DH = DH_type
            dtype = data_type
            for pwr_lev in pwr_level:
                max_pwr =-12+6+pwr_lev*3-cable_loss
                for chan in  channel:
                    freq = 2402+chan
                    for freq_offset in range(-100,130,10):
                        if freq_offset<0:
                            freq_offset1= freq_offset + 655365

                            self.wifi.cmdstop()
                            loginfo("pwr_level=%d, channel=%d, freq=%d, data_rate=%d, DH_type=%d, data_type=%d,"%(pwr_lev, chan, freq, drate, DH, dtype))

                            self.wifi.rfchsel_offset_esp32(freq_offset1)
                            self.bt.fcc_bt_tx(pwr_lev, 0, chan, drate, DH, dtype)
                            myiqv=tester.tester(freq, max_pwr, rate_name, [drate,'All'], iqv_no,'measure', cable_loss, 10, 0, 1, 150)

                            [tx_result]=bt_instrum.iqv_bt_avg(rate_name,myiqv,iqv_num)
                            [maxPowerAcpFreqHz,maxPowerAcpDbm] = bt_instrum.max_Power_Acp(myiqv,iqv_num)
                            fw1.write_data([rate_name,freq,pwr_lev,freq_offset,tx_result,maxPowerAcpFreqHz,maxPowerAcpDbm])



    def LE_TX_PWR_EVM_freq_offset(self,cable_loss=1.5,pwr_level=[0,8], channel=[0,39],rate_lst=['LE_1M_1010'],iqv_no=1, iqv_num=10, file_w='LE_TX'):
        """
        --iqv_no: 1-left port, 2-right port
        --iqv_num: iqview average number
        """
        '''
        LE_rate : 0 : 1M;   1 : 2M:  2 : 125K   3 : 500
        tx_chan : BT tx channel set (0 to 39)
        '''
        maxpwracpfreq_title ='Lower_freq1,lower_freq2,lower_freq3,upper_freq3,upper_freq2,upper_freq3'
        maxpweracpmargin_title = 'lower_margin1,lower_margin2,lower_margin3,upper_margin3,upper_margin2,upper_margin1'

        title = 'rate, channel, power_level,freq_offset,power(dbm),Init Freq Err(kHz),deltaF1Avg(kHz), deltaF2Max(kHz), deltaF2Avg(kHz),pwr_le_pk(dBm),%s,%s\n'%(maxpwracpfreq_title,maxpweracpmargin_title)
        fname = self.wifi.get_filename(self.folder+'/'+file_w,'LE_tx_pwr_evm_%s'%(rate_lst[0]),'TX')
        fw1 = csvreport(fname,title)

        max_pwr = 18 - cable_loss

        self.bt.fcc_le_tx(8, 0, 250, 2, 0)
        myiqv=tester.tester(2402, max_pwr, 'LE_1M_prbs9', [0,'All'], iqv_no,'measure', cable_loss, 10, 1, 1, 150)

        for rate_name in rate_lst:
            [LE_EN,data_rate,DH_type,data_type] = bt_instrum.name2rate(rate_name)
            drate = data_rate
            DH = DH_type
            dtype = data_type
            for pwr_lev in pwr_level:
                max_pwr =-12+6+pwr_lev*3-cable_loss
                for chan in  channel:
                    freq = 2402+chan*2
                    for freq_offset in range(-100,130,10):
                        if freq_offset<0:
                            freq_offset1= freq_offset + 655365

                        self.wifi.cmdstop()
                        loginfo("pwr_level=%d, channel=%d, freq=%d, data_rate=%d, data_type=%d,"%(pwr_lev, chan, freq, drate, dtype))
                        self.wifi.rfchsel_offset_esp32(freq_offset1)
                        self.bt.fcc_le_tx(pwr_lev, chan, 250, dtype, drate)
                        myiqv=tester.tester(freq, max_pwr, rate_name, [0,'All'], iqv_no,'measure', cable_loss, 10, 0, 1, 150)

                        [tx_result]=bt_instrum.iqv_bt_avg(rate_name,myiqv,iqv_num)
                        [maxPowerAcpFreqHz,maxPowerAcpDbm] = bt_instrum.max_Power_Acp(myiqv,iqv_num)
                        fw1.write_data([rate_name,freq,pwr_lev,freq_offset,tx_result,maxPowerAcpFreqHz,maxPowerAcpDbm])





    def BT_TX_PWR_EVM_A2(self,cable_loss=1.5,pwr_level=[0,8], channel=[0,78],rate_name = '1M_DH1_1010',iqv_no=1, iqv_num=10, report_en=0, doc='', select='', file_w='TX_A2'):
        """
        --iqv_no: 1-left port, 2-right port
        --iqv_num: iqview average number
        """
        [LE_EN,data_rate,DH_type,data_type] =bt_instrum.name2rate(rate_name)

        title0 = 'rate, channel, power_level,power(dbm),Init Freq Err(kHz),deltaF1Avg(kHz), deltaF2Max(kHz), deltaF2Avg(kHz),'
        if LE_EN==1:
            title = title0 + 'pwr_le_pk(dBm)\n'
            fname = self.wifi.get_filename(self.folder+'/'+file_w,'LE_tx_pwr_evm_'+rate_name,'TX')
            f1 = csvreport(fname,title)
        else:
            title = title0 + 'bandwidth20dB(kHz),OMEGA_I(kHz),OMEGA_O(kHz),OMEGA_IO(kHz), DEVM Average,DEVM Peak,EdrprobEVM99pass(%),EdrEVMvalid,EdrPowDiffdB(dB)\n'
            fname = self.wifi.get_filename(self.folder+'/'+file_w,'BR_tx_pwr_evm_'+rate_name,'TX')
            f2 = csvreport(fname,title)

        path = self.rf_bt_autotest_data +'/'+file_w
        if not os.path.exists(path):
            os.makedirs(path)
        if not os.path.exists(path+'/'+'pic'):
            os.makedirs(path+'/'+'pic')

        w_str = ''
        data = []; chan_lst=[]; freq_lst=[]; power_lst=[]; Init_Freq_Err_lst=[]; deltaF2Max_lst=[]; deltaF2Avg_lst=[]; deltaF1Avg_lst=[]; bandwidth20dB_lst = [];
        OMEGA_I_lst = []; OMEGA_O_lst = []; OMEGA_IO_lst = []; EdrEVMAv_lst = []; EdrEVMpk_lst = []; EdrprobEVM99pass_lst = []; EdrPowDiffdB_lst = []; EdrEVMvalid_lst = [];
        pass_flag = 1
        reset_flag = 0

        max_pwr = 18 - cable_loss
        self.bt.fcc_le_tx(8, 0, 250, 2, 0)
        myiqv=tester.tester(2402, max_pwr, 'LE_1M_prbs9', [0,'All'], iqv_no,'measure', cable_loss, 10, 1, 1, 150)

        if report_en == 1:
            table = doc.Tables[table_vs_TX_rate_dic[rate_name]]
            row_len = len(table.Rows)
            col_len = len(table.Columns)
            for i in range(0,row_len):
                table.Cell(i,1).Select()
                param = select.Text.encode('unicode-escape').decode('string_escape')
                if re.match(r'Pass/Fail',param,re.M)!=None:
                    row_param = i
            select0 = table.Cell(2,2).Select()
            select.TypeText(rate_name)

        drate = data_rate
        DH = DH_type
        dtype = data_type

        for pwr_lev in pwr_level:
            max_pwr =-12+6+pwr_lev*3-cable_loss
            for j in range(0,len(channel)):
                chan = int(channel[j])
                if LE_EN == 0:
                    freq = 2402+chan
                    self.wifi.cmdstop()
                    loginfo("pwr_level=%d, channel=%d, freq=%d, data_rate=%d,DH_type=%d, data_type=%d,"%(pwr_lev, chan, freq,drate, DH, dtype))

                    self.bt.fcc_bt_tx(pwr_lev, 0, chan, drate, DH, dtype)
                    myiqv=tester.tester(freq, max_pwr, rate_name, [drate,'All'], iqv_no,'measure', cable_loss, 10, 0, 1, 150)
                else:
                    freq = 2402+chan*2
                    self.wifi.cmdstop()
                    loginfo("pwr_level=%d, channel=%d, freq=%d, data_rate=%d, data_type=%d,"%(pwr_lev, chan, freq, drate, dtype))

                    self.bt.fcc_le_tx(pwr_lev, chan, 250, dtype)
                    myiqv=tester.tester(freq, max_pwr, rate_name, [0,'All'], iqv_no,'measure', cable_loss, 10, 0, 1, 150)

                [tx_result] = bt_instrum.iqv_bt_avg(rate_name,myiqv,iqv_num)
                loginfo(tx_result)
                if LE_EN==1 :
                    f1.write_data([rate_name,freq,pwr_lev,tx_result])
                else:
                    f2.write_data([rate_name,freq,pwr_lev,tx_result])

                if report_en == 1:
                    iqv = rfglobal.iqv
                    power = [0,'']; Init_Freq_Err = [0,'']; deltaF1Avg =  [0,'']; deltaF2Max =  [0,'']; deltaF2Avg =  [0,'']; pwr_le_pk = [0,'']; OMEGA_I = [0,''];
                    OMEGA_O = [0,'']; OMEGA_IO = [0,'']; EdrEVMAv = [0,'']; EdrEVMpk = [0,'']; EdrprobEVM99pass = [0,'']; EdrPowDiffdB = [0,'']; EdrEVMvalid = [0,'']; bandwidth20dB = [0,''];
                    res_flag = ''
                    rf_list=[chan,freq]

                    if  (LE_EN == 1) :
                        [power[0],Init_Freq_Err[0],deltaF1Avg[0],deltaF2Max[0],deltaF2Avg[0],pwr_le_pk[0]] = tx_result
                    else :
                        [power[0],Init_Freq_Err[0],deltaF1Avg[0],deltaF2Max[0],deltaF2Avg[0],bandwidth20dB[0],OMEGA_I[0],OMEGA_O[0],OMEGA_IO[0],EdrEVMAv[0],EdrEVMpk[0],EdrprobEVM99pass[0],EdrEVMvalid[0],EdrPowDiffdB[0]] = tx_result

                    power[1] = (pwr_lev*3-15)<=power[0] and (pwr_lev*3-9)>=power[0]

                    chan_lst.append(chan)
                    freq_lst.append(freq)
                    power_lst.append(power[0])
                    rf_list.append(power)

                    if LE_EN == 1 :
                        Init_Freq_Err[1] = (Init_Freq_Err[0] >= BT_param_th_dict['LE_Init_Freq_Err'][0]) and (Init_Freq_Err[0] <= BT_param_th_dict['LE_Init_Freq_Err'][1])
                        rf_list.append(Init_Freq_Err)
                        Init_Freq_Err_lst.append(Init_Freq_Err[0])

                        if deltaF1Avg[0] != '/':
                            deltaF1Avg[1] = (deltaF1Avg[0] >= BT_param_th_dict['LE_deltaF1Avg'][0]) and (deltaF1Avg[0] <= BT_param_th_dict['LE_deltaF1Avg'][1])
                            rf_list.append(deltaF1Avg)
                            deltaF1Avg_lst.append(deltaF1Avg[0])

                        if deltaF2Max[0] != '/' and deltaF2Avg[0] != '/':
                            deltaF2Max[1] = (deltaF2Max[0] >= BT_param_th_dict['LE_deltaF2Max'][0]) and (deltaF2Max[0] <= BT_param_th_dict['LE_deltaF2Max'][1])
                            deltaF2Avg[1] = (deltaF2Avg[0] >= BT_param_th_dict['LE_deltaF2Avg'][0]) and (deltaF2Avg[0] <= BT_param_th_dict['LE_deltaF2Avg'][1])
                            rf_list.extend([deltaF2Max,deltaF2Avg])
                            deltaF2Max_lst.append(deltaF2Max[0])
                            deltaF2Avg_lst.append(deltaF2Avg[0])

                    else:
                        Init_Freq_Err[1] = (Init_Freq_Err[0] >= BT_param_th_dict['Init_Freq_Err'][0]) and (Init_Freq_Err[0] <= BT_param_th_dict['Init_Freq_Err'][1])
                        rf_list.append(Init_Freq_Err)
                        Init_Freq_Err_lst.append(Init_Freq_Err[0])

                        if deltaF1Avg[0] != '/':
                            deltaF1Avg[1] = (deltaF1Avg[0] >= BT_param_th_dict['deltaF1Avg'][0]) and (deltaF1Avg[0] <= BT_param_th_dict['deltaF1Avg'][1])
                            rf_list.append(deltaF1Avg)
                            deltaF1Avg_lst.append(deltaF1Avg[0])

                        if deltaF2Max[0] != '/' and deltaF2Avg[0] != '/':
                            deltaF2Max[1] = (deltaF2Max[0] >= BT_param_th_dict['deltaF2Max'][0]) and (deltaF2Max[0] <= BT_param_th_dict['deltaF2Max'][1])
                            deltaF2Avg[1] = (deltaF2Avg[0] >= BT_param_th_dict['deltaF2Avg'][0]) and (deltaF2Avg[0] <= BT_param_th_dict['deltaF2Avg'][1])
                            rf_list.extend([deltaF2Max,deltaF2Avg])
                            deltaF2Max_lst.append(deltaF2Max[0])
                            deltaF2Avg_lst.append(deltaF2Avg[0])

                        if OMEGA_I[0] != '/' and OMEGA_O[1] != '/' :
                            OMEGA_I[1] = (OMEGA_I[0] >= BT_param_th_dict['OMEGA_I'][0]) and (OMEGA_I[0] <= BT_param_th_dict['OMEGA_I'][1])
                            OMEGA_O[1] = (OMEGA_O[0] >= BT_param_th_dict['OMEGA_O'][0]) and (OMEGA_O[0] <= BT_param_th_dict['OMEGA_O'][1])
                            OMEGA_IO[1] = (OMEGA_IO[0] >= BT_param_th_dict['OMEGA_IO'][0]) and (OMEGA_IO[0] <= BT_param_th_dict['OMEGA_IO'][1])
                            EdrEVMAv[1] = (EdrEVMAv[0] >= BT_param_th_dict['3M_DEVM_Average(%)'][0]) and (EdrEVMAv[0] <= BT_param_th_dict['3M_DEVM_Average(%)'][1])
                            EdrEVMpk[1] = (EdrEVMpk[0] >= BT_param_th_dict['3M_DEVM_Peak(%)'][0]) and (EdrEVMpk[0] <= BT_param_th_dict['3M_DEVM_Peak(%)'][1])
                            EdrprobEVM99pass[1] = (EdrprobEVM99pass[0] >= BT_param_th_dict['3M_EdrprobEVM99pas'][0]) and (EdrprobEVM99pass[0] <= BT_param_th_dict['3M_EdrprobEVM99pas'][1])
                            EdrPowDiffdB[1] = (EdrPowDiffdB[0] >= BT_param_th_dict['EdrPowDiffdB'][0]) and (EdrPowDiffdB[0] <= BT_param_th_dict['EdrPowDiffdB'][1])
                            rf_list.extend([OMEGA_I,OMEGA_O,OMEGA_IO,EdrEVMAv,EdrEVMpk,EdrprobEVM99pass,EdrPowDiffdB])
                            OMEGA_I_lst.append(OMEGA_I[0])
                            OMEGA_O_lst.append(OMEGA_O[0])
                            OMEGA_IO_lst.append(OMEGA_IO[0])
                            EdrEVMAv_lst.append(EdrEVMAv[0])
                            EdrEVMpk_lst.append(EdrEVMpk[0])
                            EdrprobEVM99pass_lst.append(EdrprobEVM99pass[0])
                            EdrPowDiffdB_lst.append(EdrPowDiffdB[0])
                        if bandwidth20dB[0] != '/':
                            bandwidth20dB[1] = (bandwidth20dB[0] >= BT_param_th_dict['bandwidth20dB'][0]) and (bandwidth20dB[0] <= BT_param_th_dict['bandwidth20dB'][1])
                            rf_list.append(bandwidth20dB)
                            bandwidth20dB_lst.append(bandwidth20dB[0])

                    for i in range(2,len(rf_list)):
                        if rf_list[i][1] :
                            res_flag = 'pass'
                        else:
                            res_flag = 'fail'
                    rf_list.append(res_flag)
                    print rf_list

                    col = j+2
                    for row in range(3,row_param+1):
                    	select1 = table.Cell(row,col).Select()
                    	select.Font.Bold = False
                    	select.Font.Italic = False
                    	select.Font.ColorIndex = 1
                        if row>= 5 and row<=(row_param-1):
                            #print '**********',rf_list[row-3][1]
                            if (not rf_list[row-3][1]):
                                select.Font.Bold = True
                                select.Font.ColorIndex = 5
                            select.TypeText('%2.2f'%rf_list[row-3][0])
                        else:
                            if re.match(r'fail',str(rf_list[row-3]),re.M)!=None:
                                select.Font.Bold = True
                                select.Font.ColorIndex = 5
                            select.TypeText(rf_list[row-3])
                    table.Cell(row_param,col).Select()
                    res_param = select.Text.encode('unicode-escape').decode('string_escape')
                    if re.match(r'pass',res_param,re.M)!=None:
                        pass_flag = pass_flag & 1
                    else:
                        pass_flag = 0

        print '\n\n--------------------------\n'

        if report_en ==1:
            if pass_flag==1:
                table.Cell(row_len,2).Select()
                select.Font.Bold = True
                select.TypeText(rate_name+' meets the test requirements')
            else:
                table.Cell(row_len,2).Select()
                select.Font.Bold = True
                select.Font.ColorIndex = 5
                select.TypeText(rate_name+' does not meet the test requirements')

            pylab.figure(100)
            pylab.title("loss=%s"%cable_loss)
            pylab.plot(chan_lst,power_lst,label='pwr_%s'%(rate_name))
            pylab.legend()
            pylab.grid()
            plt.savefig(path+'/'+'pic'+'/'+'bt_pwr_%s.png'%(rate_name));
            plt.close()

            pylab.figure(100)
            pylab.title("loss=%s"%cable_loss)
            pylab.plot(chan_lst,Init_Freq_Err_lst,label='Init_Freq_Err_%s'%(rate_name))
            pylab.legend()
            pylab.grid()
            plt.savefig(path+'/'+'pic'+'/'+'bt_Init_Freq_Err_%s.png'%(rate_name));
            plt.close()

            if  (LE_EN == 1 and dtype == 0) :

                pylab.figure(100)
                pylab.title("loss=%s"%cable_loss)
                pylab.plot(chan_lst,deltaF2Max_lst,label='deltaF2Max_%s'%(rate_name))
                pylab.legend()
                pylab.grid()
                plt.savefig(path+'/'+'pic'+'/'+'bt_deltaF2Max_%s.png'%(rate_name));
                plt.close()

                pylab.figure(100)
                pylab.title("loss=%s"%cable_loss)
                pylab.plot(chan_lst,deltaF2Avg_lst,label='deltaF2Avg_%s'%(rate_name))
                pylab.legend()
                pylab.grid()
                plt.savefig(path+'/'+'pic'+'/'+'bt_deltaF2Avg_%s_pwr.png'%(rate_name));
                plt.close()

            elif  (LE_EN == 1 and dtype == 1):

                pylab.figure(100)
                pylab.title("loss=%s"%cable_loss)
                pylab.plot(chan_lst,deltaF1Avg_lst,label='deltaF1Avg_%s'%(rate_name))
                pylab.legend()
                pylab.grid()
                plt.savefig(path+'/'+'pic'+'/'+'bt_deltaF1Avg_%s.png'%(rate_name));
                plt.close()

            elif (drate ==1 and dtype == 0) :
                pylab.figure(100)
                pylab.title("loss=%s"%cable_loss)
                pylab.plot(chan_lst,deltaF2Max_lst,label='deltaF2Max_%s'%(rate_name))
                pylab.legend()
                pylab.grid()
                plt.savefig(path+'/'+'pic'+'/'+'bt_deltaF2Max_%s.png'%(rate_name));
                plt.close()

                pylab.figure(100)
                pylab.title("loss=%s"%cable_loss)
                pylab.plot(chan_lst,deltaF2Avg_lst,label='deltaF2Avg_%s'%(rate_name))
                pylab.legend()
                pylab.grid()
                plt.savefig(path+'/'+'pic'+'/'+'bt_deltaF2Avg_%s_pwr.png'%(rate_name));
                plt.close()

            elif (drate ==1 and dtype == 1) :
                pylab.figure(100)
                pylab.title("loss=%s"%cable_loss)
                pylab.plot(chan_lst,deltaF1Avg_lst,label='deltaF1Avg_%s'%(rate_name))
                pylab.legend()
                pylab.grid()
                plt.savefig(path+'/'+'pic'+'/'+'bt_deltaF1Avg_%s.png'%(rate_name));
                plt.close()

            elif (drate ==1 and dtype == 2) :
                pylab.figure(100)
                pylab.title("loss=%s"%cable_loss)
                pylab.plot(chan_lst,bandwidth20dB_lst,label='bandwidth20dB_%s'%(rate_name))
                pylab.legend()
                pylab.grid()
                plt.savefig(path+'/'+'pic'+'/'+'bt_bandwidth20dB_%s.png'%(rate_name));
                plt.close()

            elif drate == 2 or drate == 3:

                pylab.figure(100)
                pylab.title("loss=%s"%cable_loss)
                pylab.plot(chan_lst,EdrEVMAv_lst,label='EdrEVMAv_%s'%(rate_name))
                pylab.legend()
                pylab.grid()
                plt.savefig(path+'/'+'pic'+'/'+'bt_EdrEVMAv_%s.png'%(rate_name));
                plt.close()

                pylab.figure(100)
                pylab.title("loss=%s"%cable_loss)
                pylab.plot(chan_lst,EdrEVMpk_lst,label='EdrEVMpk_%s'%(rate_name))
                pylab.legend()
                pylab.grid()
                plt.savefig(path+'/'+'pic'+'/'+'bt_EdrEVMpk_%s.png'%(rate_name));
                plt.close()

                pylab.figure(100)
                pylab.title("loss=%s"%cable_loss)
                pylab.plot(chan_lst,EdrPowDiffdB_lst,label='EdrPowDiffdB_%s'%(rate_name))
                pylab.legend()
                pylab.grid()
                plt.savefig(path+'/'+'pic'+'/'+'bt_EdrPowDiffdB_%s.png'%(rate_name));
                plt.close()

            if rate_name == '1M_DH5_1010' or rate_name == 'LE_1M_1010':
                select1= table.Cell(10,2).Select()
                select.InlineShapes.AddPicture(path+'/'+'pic'+'/'+'bt_pwr_%s.png'%(rate_name))

                select2= table.Cell(11,2).Select()
                select.InlineShapes.AddPicture(path+'/'+'pic'+'/'+'bt_Init_Freq_Err_%s.png'%(rate_name))

                select3= table.Cell(12,2).Select()
                select.InlineShapes.AddPicture(path+'/'+'pic'+'/'+'bt_deltaF2Max_%s.png'%(rate_name))

                select4= table.Cell(13,2).Select()
                select.InlineShapes.AddPicture(path+'/'+'pic'+'/'+'bt_deltaF2Avg_%s_pwr.png'%(rate_name))

            elif rate_name == '1M_DH5_00001111' or rate_name == 'LE_1M_00001111':
                select1= table.Cell(9,2).Select()
                select.InlineShapes.AddPicture(path+'/'+'pic'+'/'+'bt_pwr_%s.png'%(rate_name))

                select2= table.Cell(10,2).Select()
                select.InlineShapes.AddPicture(path+'/'+'pic'+'/'+'bt_Init_Freq_Err_%s.png'%(rate_name))

                select3= table.Cell(11,2).Select()
                select.InlineShapes.AddPicture(path+'/'+'pic'+'/'+'bt_deltaF1Avg_%s.png'%(rate_name))

            elif rate_name == '1M_DH5_prbs9':
                select1= table.Cell(9,2).Select()
                select.InlineShapes.AddPicture(path+'/'+'pic'+'/'+'bt_pwr_%s.png'%(rate_name))

                select2= table.Cell(10,2).Select()
                select.InlineShapes.AddPicture(path+'/'+'pic'+'/'+'bt_Init_Freq_Err_%s.png'%(rate_name))

                select3= table.Cell(11,2).Select()
                select.InlineShapes.AddPicture(path+'/'+'pic'+'/'+'bt_bandwidth20dB_%s.png'%(rate_name))

            elif rate_name == 'LE_1M_prbs9':
                select1= table.Cell(8,2).Select()
                select.InlineShapes.AddPicture(path+'/'+'pic'+'/'+'bt_pwr_%s.png'%(rate_name))

                select2= table.Cell(9,2).Select()
                select.InlineShapes.AddPicture(path+'/'+'pic'+'/'+'bt_Init_Freq_Err_%s.png'%(rate_name))

            else:
                select1= table.Cell(15,2).Select()
                select.InlineShapes.AddPicture(path+'/'+'pic'+'/'+'bt_pwr_%s.png'%(rate_name))

                select2= table.Cell(16,2).Select()
                select.InlineShapes.AddPicture(path+'/'+'pic'+'/'+'bt_Init_Freq_Err_%s.png'%(rate_name))

                select3= table.Cell(17,2).Select()
                select.InlineShapes.AddPicture(path+'/'+'pic'+'/'+'bt_EdrEVMAv_%s.png'%(rate_name))

                select4= table.Cell(18,2).Select()
                select.InlineShapes.AddPicture(path+'/'+'pic'+'/'+'bt_EdrEVMpk_%s.png'%(rate_name))

                select5= table.Cell(19,2).Select()
                select.InlineShapes.AddPicture(path+'/'+'pic'+'/'+'bt_EdrPowDiffdB_%s.png'%(rate_name))

        return pass_flag


    #************************BT rx*********************#


    def rw_le_rx_per_test(self,framecnt=1000,ratename='LE_prbs9',rate=0,pwrdBm=-15,freq=2472, cable_loss=0, iqv_no=1, syncw=0x0,mytester='', rssireq=0):

        chan=(freq-2402)/2
        if chan==0:
            fi=37
        elif chan==12:
            fi=38
        elif chan==39:
            fi=39
        elif chan<=11:
            fi=chan-1
        elif chan<=38:
            fi=chan-2
        self.wifi.cmdstop()

        if mytester=='iqxel' or mytester=='wt200' or mytester=='wt208c':
            if rssireq == 1:
                self.bt.rw_le_rx_per_rssi(rx_chan=fi, syncw=syncw, rate=rate)
            else:
                self.bt.rw_le_rx_per(rx_chan=fi, syncw=syncw, rate=rate)
            self.interfer_test.iq_sigout(mytester,freq,pwrdBm,cable_loss,ratename,framecnt,iqv_no)
        else:
            mytester=tester.tester(freq,-40,ratename,1,iqv_no,'source',cable_loss,10,0);
            mytester.sigout(freq,pwrdBm,cable_loss,ratename,framecnt,iqv_no)
            if rssireq == 1:
                self.bt.rw_le_rx_per_rssi(rx_chan=fi, syncw=syncw, rate=rate)
            else:
                self.bt.rw_le_rx_per(rx_chan=fi, syncw=syncw, rate=rate)
            mytester.trig_wave(iqv_no);
            mytester.txenable(0)

        result=self.wifi.cmdstop()
        result=result.split()
        totalp=int(result[0],16)

        cp=int(result[1],16)
        PER=1-(float(cp)/framecnt)

        type_ep=int(result[2],16)
        len_ep=int(result[3],16)
        crc_ep=int(result[4],16)
        mic_ep=int(result[5],16)
        sn_ep=int(result[6],16)
        nesn_ep=int(result[7],16)
        time_ep=int(result[8],16)
        priv_ep=int(result[9],16)

        gainmax=0
        gainmin=0
        rssimax=0
        rssimin=0

        if self.chipv=='ESP32':
            pwr_ib=int(result[20],16)
            pwr_fb=int(result[21],16)
            gain=int(result[22],16)
            if(totalp!=0):
                pwr_ib=0-(float(pwr_ib)/totalp)
                pwr_fb=0-(float(pwr_fb)/totalp)
                gain=float(gain)/totalp

            RSSI = pwr_ib - gain
            pwr_ibm_w_ep=int(result[11],16)
            pwr_fbm_w_ep=int(result[12],16)

            pwr_r_free_w_ep=int(result[13],16)
            pwr_r_ac_w_ep=int(result[14],16)
            pwr_r_pac_w_ep=int(result[15],16)
            pwr_d_free_w_ep=int(result[16],16)
            pwr_d_ac_w_ep=int(result[17],16)
            pwr_d_pac_w_ep=int(result[18],16)

            if rssireq == 1:
                gainmax=int(result[24],10)
                gainmin=int(result[25],10)
                rssimax=int(result[26],10)
                rssimin=int(result[27],10)

        else:
            total_rssi=int(result[11],10)
            total_inband=int(result[12],10)
            total_fullband=int(result[13],10)
            total_gain=int(result[14],16)
            if (crc_ep+cp) >0 :
                RSSI = float(total_rssi)/(crc_ep+cp)
                pwr_ib = float(total_inband)/(crc_ep+cp)
                pwr_fb = float(total_fullband)/(crc_ep+cp)
                gain=float(total_gain)/(crc_ep+cp)
            else:
                RSSI=0
                pwr_ib =0
                pwr_fb =0
                gain=0
            pwr_ibm_w_ep=0
            pwr_fbm_w_ep=0
            pwr_r_free_w_ep=0
            pwr_r_ac_w_ep=0
            pwr_r_pac_w_ep=0
            pwr_d_free_w_ep=0
            pwr_d_ac_w_ep=0
            pwr_d_pac_w_ep=0
            if rssireq == 1:
                gainmax=int(result[16],10)
                gainmin=int(result[17],10)
                rssimax=int(result[18],10)
                rssimin=int(result[19],10)

        return [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
        pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, type_ep, len_ep, crc_ep,
        mic_ep, sn_ep, nesn_ep,time_ep,priv_ep, gainmax, gainmin, rssimax, rssimin
        ]

    def rw_le_rx_per_sweep(self,per_limit=0.2,framecnt=1000,rate_name='LE_1M_prbs9', rate=0, pwrdBm_start=-70,pwrdBm_end=-50, step=1,channel=[0], file_w='LE_RX',cable_loss=0, iqv_no=1, report_en=0, doc='', select='',syncw=0x71764129,max_sens_sel=0, rssireq=0):

        if max_sens_sel == 0:
            title = 'rate,chan, freq, sens(dBm), sens_rssi(dbm),PER,BER\n'
            fname = self.wifi.get_filename(self.folder+'/'+file_w,'bt_rx_sens_'+rate_name,'RX_Sens')
            csvreport1 = csvreport(fname, title)
        else:
            title = 'rate,chan, freq, max_input(dBm), sens_rssi(dbm),PER\n'
            fname = self.wifi.get_filename(self.folder+'/'+file_w,'bt_rx_max_input_'+rate_name,'RX_Sens')
            csvreport1 = csvreport(fname, title)

        if rssireq==1:
            title1 ='Rate,Channel,TX power,TX pac,RX pac,RX correct pac,PER,fail,AER, PER RX pac, RSSI, inband, fullband, gain, gainmax, gainmin, rssimax, rssimin\n'
        else:
            title1 ='Rate,Channel,TX power,TX pac,RX pac,RX correct pac,PER,fail,AER, PER RX pac, RSSI, inband, fullband, gain\n'
        fname1 = self.wifi.get_filename(self.folder+'/'+file_w,"pwr%d_%d_"%(pwrdBm_start, pwrdBm_end)+rate_name,'RX_Scan')

        csvreport2 = csvreport(fname1, title1)

        path = self.rf_bt_autotest_data +'/'+file_w
        if not os.path.exists(path):
            os.makedirs(path)
        if not os.path.exists(path+'/'+'pic'):
            os.makedirs(path+'/'+'pic')

        freq_lst = np.array(channel)*2+2402
        print 'freq_ls' ,freq_lst
        framecnt_est=framecnt

        freqlst = []; ratelst = []; PERlst = []; senslst = []; rssilst =[]; chanlst = []; passlst = [];
        pass_flag = 1

        if report_en == 1:
            table = doc.Tables[table_vs_RX_rate_dic[rate_name]]
            row_len = len(table.Rows)
            col_len = len(table.Columns)
            for i in range(0,row_len):
                table.Cell(i,1).Select()
                param = select.Text.encode('unicode-escape').decode('string_escape')
                if re.match(r'Pass/Fail',param,re.M)!=None:
                    row_param = i
            select0 = table.Cell(2,2).Select()
            select.TypeText(rate_name)

        mytester=tester.tester(2402,-40,rate_name,1,iqv_no,'source',cable_loss,10,0)

        for i in range(0,len(freq_lst)):
            chan = channel[i]
            freq = freq_lst[i]
            pwrdBm=pwrdBm_start
            cur_sense_find=0
            cur_max_find = 0
            res_lst=[]
            while pwrdBm<=pwrdBm_end:
                [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
                pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, type_ep, len_ep, crc_ep,
                mic_ep, sn_ep, nesn_ep, time_ep, priv_ep,
                gainmax, gainmin, rssimax, rssimin]=self.rw_le_rx_per_test(framecnt=framecnt,ratename=rate_name,rate=rate,pwrdBm=pwrdBm, freq=freq, cable_loss=cable_loss, iqv_no=iqv_no, syncw=syncw,mytester =mytester,rssireq=rssireq)

##                if totalp >= framecnt+10 :
##                    [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
##                    pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, type_ep, len_ep, crc_ep,
##                    mic_ep, sn_ep, nesn_ep,time_ep,priv_ep]=self.rw_le_rx_per_test(framecnt=framecnt,ratename=rate_name,pwrdBm=pwrdBm, freq=freq, cable_loss=cable_loss, iqv_no=iqv_no, syncw=syncw,mytester =mytester)

                PER=1-(float(cp)/framecnt_est)

                if PER >= per_limit:
                    fail=1
                else:
                    fail=0
                AER=1-(float(totalp)/framecnt_est)
                PER_RX_pac=1

                if totalp != 0:
                    PER_RX_pac=1-(float(cp)/totalp)

                if rssireq==1:
                    csvreport2.write_data([rate_name,chan,pwrdBm,framecnt_est,totalp,cp,PER,fail,AER,PER_RX_pac,RSSI,pwr_ib,pwr_fb,gain,gainmax,gainmin,rssimax,rssimin])
                else:
                    csvreport2.write_data([rate_name,chan,pwrdBm,framecnt_est,totalp,cp,PER,fail,AER,PER_RX_pac,RSSI,pwr_ib,pwr_fb,gain])

                loginfo([rate_name,chan,pwrdBm,framecnt_est,totalp,cp,PER,fail, int(RSSI),int(pwr_ib),int(pwr_fb),gain])
                if max_sens_sel == 0 and cur_sense_find==0:
                    if PER < per_limit:
                        res_lst = [chan, freq,pwrdBm,RSSI,PER*100]
                        cur_sense_find=1
                    else:
                        res_lst = [chan, freq,pwrdBm,RSSI,PER*100]
                        cur_sense_find=0
                if max_sens_sel == 1 and cur_max_find == 0:
                    if PER > per_limit:
                        res_lst = [chan, freq,pwrdBm,RSSI,PER*100]
                        cur_max_find=1
                    else:
                        res_lst = [chan, freq,pwrdBm,RSSI,PER*100]
                        cur_max_find=0

                pwrdBm=pwrdBm+step

            res_flag = ''
            if report_en ==1:
                if res_lst[2] <=BT_param_th_dict[rate_name+'_rssi']:
                    res_flag = 'pass'
                else:
                    res_flag = 'fail'
                res_lst.append(res_flag)
                col = i+2
                for row in range(3,row_len-1):
                    select1 = table.Cell(row,col).Select()
                    select.Font.Bold = False
                    select.Font.Italic = False
                    select.Font.ColorIndex = 1
                    if row>= 5 and row<=(row_param-1):
                        if  res_flag == 'fail':
                            select.Font.Bold = True
                            select.Font.ColorIndex = 5
                        select.TypeText('%2.2f'%res_lst[row-3])
                    else:
                        if  res_flag == 'fail':
                            select.Font.Bold = True
                            select.Font.ColorIndex = 5
                        select.TypeText(res_lst[row-3])

                table.Cell(row_param,col).Select()
                res_param = select.Text.encode('unicode-escape').decode('string_escape')
                if re.match(r'pass',res_param,re.M)!=None:
                    pass_flag = pass_flag & 1
                else:
                    pass_flag = 0

            passlst.append(pass_flag)
            chanlst.append(res_lst[0])
            freqlst.append(res_lst[1])
            senslst.append(res_lst[2])
            rssilst.append(res_lst[3])
            PERlst.append(res_lst[4])
            csvreport1.write_data([rate_name,res_lst[0],res_lst[1],res_lst[2],res_lst[3],res_lst[4]])
##
        pylab.figure(100)
        pylab.title("loss=%s"%cable_loss)
        pylab.plot(freqlst,senslst,label='sens_%s'%(rate_name))
        pylab.legend()
        pylab.grid()
        plt.savefig(path+'/'+'pic'+'/'+'bt_sens_%s.png'%(rate_name));
        plt.close()
        if report_en ==1:
            if pass_flag ==1:
                table.Cell(row_len,2).Select()
                select.Font.Bold = True
                select.TypeText(rate_name+' meets the test requirements')
            else:
                table.Cell(row_len,2).Select()
                select.Font.Bold = True
                select.Font.ColorIndex = 5
                select.TypeText(rate_name+' does not meet the test requirements')

            select1= table.Cell(9,2).Select()
            select.InlineShapes.AddPicture(path+'/'+'pic'+'/'+'bt_sens_%s.png'%(rate_name))

        return pass_flag


    def rw_le_rx_per_sweep_freq_offset(self,per_limit=0.2,framecnt=1000,rate_name='LE_prbs9',pwrdBm_start=-70,pwrdBm_end=-50, step=1,channel=[0,1,2], file_w = '../bt_rx_per_',cable_loss=0, iqv_no=1, report_en=0, doc='', select='',syncw=0x71764129,max_sens_sel=0):

        if max_sens_sel == 0:
            title = 'rate,chan, freq, sens(dBm), sens_rssi(dbm),PER,BER\n'
            fname = self.wifi.get_filename(self.folder,'bt_rx_sens_'+rate_name,'RX_Sens')
            csvreport1 = csvreport(fname, title)
        else:
            title = 'rate,chan, freq, max_input(dBm), sens_rssi(dbm),PER\n'
            fname = self.wifi.get_filename(self.folder,'bt_rx_max_input_'+rate_name,'RX_Sens')
            csvreport1 = csvreport(fname, title)

        title1 ='Rate,Channel,freq_offset,TX power,TX pac,RX pac,RX correct pac,PER,fail,AER, PER RX pac, RSSI\n'
        fname1 = self.wifi.get_filename(self.folder,"pwr%d_%d_"%(pwrdBm_start, pwrdBm_end)+rate_name,'RX_Scan')
        csvreport2 = csvreport(fname1, title1)

        freq_lst = np.array(channel)*2+2402
        print 'freq_ls' ,freq_lst
        framecnt_est=framecnt+5

        freqlst = [], ratelst = [], PERlst = [], senslst = [], rssilst =[], chanlst = [], passlst = []
        pass_flag = 1
        if report_en == 1:
            table = doc.Tables[table_vs_RX_rate_dic[rate_name]]
            row_len = len(table.Rows)
            col_len = len(table.Columns)
            for i in range(0,row_len):
                table.Cell(i,1).Select()
                param = select.Text.encode('unicode-escape').decode('string_escape')
                if re.match(r'Pass/Fail',param,re.M)!=None:
                    row_param = i
            select0 = table.Cell(2,2).Select()
            select.TypeText(rate_name)

        mytester=tester.tester(2402,-40,'LE_1M_prbs9',1,iqv_no,'source',cable_loss,10,0);
        for freq_offset in range (110,140,10):
            if freq_offset<0:
                freq_offset_init=freq_offset+655356
            else:
                freq_offset_init=freq_offset
            loginfo('freq_offset=%d'%freq_offset)
            self.wifi.rfchsel_offset_esp32(freq_offset_init)
            for i in range(0,len(freq_lst)):
                chan = channel[i]
                freq = freq_lst[i]
                pwrdBm=pwrdBm_start
                cur_sense_find=0
                cur_max_find = 0
                res_lst=[]
                while pwrdBm<=pwrdBm_end:
                    [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
                    pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, type_ep, len_ep, crc_ep,
                    mic_ep, sn_ep, nesn_ep,time_ep,priv_ep,]=self.rw_le_rx_per_test(framecnt=framecnt,ratename=rate_name,pwrdBm=pwrdBm, freq=freq, cable_loss=cable_loss, iqv_no=iqv_no, syncw=syncw,mytester =mytester)
                    if totalp >= framecnt+10 :
                        [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
                        pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, type_ep, len_ep, crc_ep,
                        mic_ep, sn_ep, nesn_ep,time_ep,priv_ep]=self.rw_le_rx_per_test(framecnt=framecnt,ratename=rate_name,pwrdBm=pwrdBm, freq=freq, cable_loss=cable_loss, iqv_no=iqv_no, syncw=syncw,mytester =mytester)

                    PER=1-(float(cp)/framecnt_est)

                    if PER >= per_limit:
                        fail=1
                    else:
                        fail=0
                    AER=1-(float(totalp)/framecnt_est)
                    PER_RX_pac=1
                    #print "%d\n"%totalp
                    if totalp != 0:
                        PER_RX_pac=1-(float(cp)/totalp)

                    csvreport2.write_data([rate_name,chan,freq_offset,pwrdBm,framecnt_est,totalp,cp,PER,fail,AER,PER_RX_pac,RSSI])
                    if max_sens_sel == 0 and cur_sense_find==0:
                        if PER < per_limit:
                            res_lst = [chan, freq,pwrdBm,RSSI,PER*100]
                            cur_sense_find=1
                        else:
                            res_lst = [chan, freq,pwrdBm,RSSI,PER*100]
                            cur_sense_find=0
                    if max_sens_sel == 1 and cur_max_find == 0:
                        if PER > per_limit:
                            res_lst = [chan, freq,pwrdBm,RSSI,PER*100]
                            cur_max_find=1
                        else:
                            res_lst = [chan, freq,pwrdBm,RSSI,PER*100]
                            cur_max_find=0

                    pwrdBm=pwrdBm+step

                res_flag = ''
                if report_en ==1:
                    if res_lst[2] <=BT_param_th_dict[rate_name+'_rssi']:
                        res_flag = 'pass'
                    else:
                        res_flag = 'fail'
                    res_lst.append(res_flag)
                    col = i+2
                    for row in range(3,row_len-1):
                        select1 = table.Cell(row,col).Select()
                        select.Font.Bold = False
                        select.Font.Italic = False
                        select.Font.ColorIndex = 1
                        if row>= 5 and row<=(row_param-1):
                            if  res_flag == 'fail':
                                select.Font.Bold = True
                                select.Font.ColorIndex = 5
                            select.TypeText('%2.2f'%res_lst[row-3])
                        else:
                            if  res_flag == 'fail':
                                select.Font.Bold = True
                                select.Font.ColorIndex = 5
                            select.TypeText(res_lst[row-3])

                        table.Cell(row_param,col).Select()
                        res_param = select.Text.encode('unicode-escape').decode('string_escape')
                        if re.match(r'pass',res_param,re.M)!=None:
                            pass_flag = pass_flag & 1
                        else:
                            pass_flag = 0

                passlst.append(pass_flag)
                chanlst.append(res_lst[0])
                freqlst.append(res_lst[1])
                senslst.append(res_lst[2])
                rssilst.append(res_lst[3])
                PERlst.append(res_lst[4])
                csvreport1.write_data([rate_name,res_lst[0],res_lst[1],res_lst[2],res_lst[3],res_lst[4]])

            pylab.figure(100)
            pylab.title("loss=%s"%cable_loss)
            pylab.plot(freqlst,senslst,label='sens_%s'%(rate_name))
            pylab.legend()
            pylab.grid()
            plt.savefig(file_w+'/'+'pic'+'/'+'bt_sens_%s.png'%(rate_name));
            plt.close()
            if report_en ==1:
                if pass_flag ==1:
                    table.Cell(row_len,2).Select()
                    select.Font.Bold = True
                    select.TypeText(rate_name+' meets the test requirements')
                else:
                    table.Cell(row_len,2).Select()
                    select.Font.Bold = True
                    select.Font.ColorIndex = 5
                    select.TypeText(rate_name+' does not meet the test requirements')

                select1= table.Cell(9,2).Select()
                select.InlineShapes.AddPicture(file_w+'/'+'pic'+'/'+'bt_sens_%s.png'%(rate_name))

        return pass_flag

    def rw_rx_per_test(self,framecnt=1000, edr=1,ratename='1M_DH1_prbs9',pwrdBm=-15,freq=2472, cable_loss=0, iqv_no=1,ulap=0x0,ltaddr=0,mytester=''):

        rw_freq = ((freq - 2402)/2) + (((freq -2402)%2)*40)
        print "rw_freq %d\n"%rw_freq
        self.wifi.cmdstop()

        if mytester=='iqxel' or mytester=='wt200' or mytester=='wt208c':
            self.bt.rw_rx_per(modetype=edr, rx_chan=rw_freq, ulap=ulap,ltaddr=ltaddr)
            self.interfer_test.iq_sigout(mytester,freq,pwrdBm,cable_loss,ratename,framecnt,iqv_no)
        else:
            mytester=tester.tester(freq,-40,ratename,1,iqv_no,'source',cable_loss,10,0);
            mytester.sigout(freq,pwrdBm,cable_loss,ratename,framecnt,iqv_no)
            self.bt.rw_rx_per(modetype=edr, rx_chan=rw_freq, ulap=ulap,ltaddr=ltaddr)
            mytester.trig_wave(iqv_no);
            mytester.txenable(0)

        result=self.wifi.cmdstop()
        print result
        result=result.split()
        totalp=int(result[0],16)

        cp=int(result[1],16)
        PER=1-(float(cp)/framecnt)

        totalb=int(result[22],16)
        cb_err=int(result[23],16)
        BER=0+(float(cb_err)/(totalb+0.000001))

        hec_ep=int(result[2],16)
        crc_ep=int(result[3],16)
        mic_ep=int(result[4],16)
        seq_ep=int(result[5],16)
        lt_ep=int(result[6],16)
        guard_ep=int(result[7],16)


        pwr_ib=int(result[18],16)
        pwr_fb=int(result[19],16)
        gain=int(result[20],16)
        if(totalp!=0):
            pwr_ib=0-(float(pwr_ib)/totalp)
            pwr_fb=0-(float(pwr_fb)/totalp)
            gain=float(gain)/totalp

        RSSI = pwr_ib - gain
        pwr_ibm_w_ep=int(result[9],16)
        pwr_fbm_w_ep=int(result[10],16)

        pwr_r_free_w_ep=int(result[11],16)
        pwr_r_ac_w_ep=int(result[12],16)
        pwr_r_pac_w_ep=int(result[13],16)
        pwr_d_free_w_ep=int(result[14],16)
        pwr_d_ac_w_ep=int(result[15],16)
        pwr_d_pac_w_ep=int(result[16],16)

        return [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
        pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, hec_ep, crc_ep, mic_ep,
        seq_ep, lt_ep, guard_ep, totalb, cb_err, BER
        ]



    def rw_rx_per_sweep(self,ber_limit=0.2,framecnt=1000,edr=0,rate_name='1M_DH1_prbs9',pwrdBm_start=-70,pwrdBm_end=-50,step=1, channel=[0], file_w='BT_RX',cable_loss=0, iqv_no=1,report_en=0, doc='', select='',ulap=0x6BC6967e,ltaddr=0,max_sens_sel=0):

        if max_sens_sel == 0:
            title = 'rate,chan, freq, sens(dBm), sens_rssi(dbm),PER,BER\n'
            fname = self.wifi.get_filename(self.folder+'/'+ file_w,'bt_rx_sens_'+rate_name,'RX_Sens')
            csvreport1 = csvreport(fname, title)
        else:
            title = 'rate,chan, freq, max_input(dBm), sens_rssi(dbm),PER, BER\n'
            fname = self.wifi.get_filename(self.folder+'/'+ file_w,'bt_rx_max_input_'+rate_name,'RX_Sens')
            csvreport1 = csvreport(fname, title)

        title1 ='Rate,Channel,TX power,TX pac,RX pac,RX correct pac,PER,fail,AER, PER RX pac, RSSI, RX bits,RX err bit,BER,Gain\n'
        fname1 = self.wifi.get_filename(self.folder+'/'+file_w,"pwr%d_%d_"%(pwrdBm_start, pwrdBm_end)+rate_name,'RX_Scan')
        csvreport2 = csvreport(fname1, title1)


        path = self.rf_bt_autotest_data +'/'+file_w
        if not os.path.exists(path):
            os.makedirs(path)
        if not os.path.exists(path+'/'+'pic'):
            os.makedirs(path+'/'+'pic')

        freq_lst = np.array(channel)+2402
        print 'freq_ls' ,freq_lst
        framecnt_est=framecnt

        freqlst = []; ratelst = []; PERlst = []; BERlst = []; senslst = []; rssilst =[]; chanlst = []; gainlst = [];
        pass_flag = 1

        if report_en == 1:
            table = doc.Tables[table_vs_RX_rate_dic[rate_name]]
            row_len = len(table.Rows)
            col_len = len(table.Columns)
            for i in range(0,row_len):
                table.Cell(i,1).Select()
                param = select.Text.encode('unicode-escape').decode('string_escape')
                if re.match(r'Pass/Fail',param,re.M)!=None:
                    row_param = i
            select0 = table.Cell(2,2).Select()
            select.TypeText(rate_name)
        mytester=tester.tester(2402,-40,rate_name,1,iqv_no,'source',cable_loss,10,1);
        for i in range(0,len(freq_lst)):
            chan = channel[i]
            freq = freq_lst[i]
            pwrdBm=pwrdBm_start
            cur_sense_find=0
            cur_max_find = 0
            while pwrdBm<=pwrdBm_end:
                [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
                pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, hec_ep, crc_ep, mic_ep,
                seq_ep, lt_ep, guard_ep, totalb, cb_err, BER]=self.rw_rx_per_test(framecnt=framecnt,edr=edr,ratename=rate_name,pwrdBm=pwrdBm, freq=freq, cable_loss=cable_loss, iqv_no=iqv_no,ulap=ulap,ltaddr=ltaddr, mytester=mytester)
##                if totalp >= framecnt+10 :
##                    [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
##                    pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, hec_ep, crc_ep, mic_ep,
##                    seq_ep, lt_ep, guard_ep, totalb, cb_err, BER]=self.rw_rx_per_test(framecnt=framecnt,edr=edr,ratename=rate_name,pwrdBm=pwrdBm, freq=freq, cable_loss=cable_loss, iqv_no=iqv_no, ulap=ulap,ltaddr=ltaddr,mytester=mytester)

                PER=1-(float(cp)/framecnt_est)
                AER=1-(float(totalp)/framecnt_est)
                PER_RX_pac=1
                if totalp != 0:
                    PER_RX_pac=1-(float(cp)/totalp)

                if BER >= ber_limit or PER_RX_pac==1:
                    fail=1
                else:
                    fail=0
                csvreport2.write_data([rate_name,chan,pwrdBm,framecnt_est,totalp,cp,PER,fail,AER,PER_RX_pac,RSSI,totalb, cb_err, BER*100, gain],float_num=3)

                if max_sens_sel == 0 and cur_sense_find == 0:
                    if BER < ber_limit and PER_RX_pac < 1:
                        res_lst = [chan, freq,pwrdBm,RSSI,PER*100,BER*100]
                        cur_sense_find = 1
                    else:
                        res_lst = [chan, freq,pwrdBm,RSSI,PER*100,BER*100]
                        cur_sense_find = 0

                if max_sens_sel == 1 and cur_max_find == 0:
                    if BER > ber_limit:
                        res_lst = [chan, freq,pwrdBm,RSSI,PER*100,BER*100]
                        cur_max_find=1
                    else:
                        res_lst = [chan, freq,pwrdBm,RSSI,PER*100,BER*100]
                        cur_max_find=0

                pwrdBm=pwrdBm+step

            res_flag = ''
            if report_en ==1:
                if res_lst[2] <= BT_param_th_dict[rate_name+'_rssi']:
                    res_flag = 'pass'
                else:
                    res_flag = 'fail'
                res_lst.append(res_flag)
                col = i+2
                for row in range(3,row_len-1):
                    select1 = table.Cell(row,col).Select()
                    select.Font.Bold = False
                    select.Font.Italic = False
                    select.Font.ColorIndex = 1
                    if row>= 5 and row<=(row_param-1):
                        if  res_flag == 'fail':
                            select.Font.Bold = True
                            select.Font.ColorIndex = 5
                        select.TypeText('%2.2f'%res_lst[row-3])
                    else:
                        if  res_flag == 'fail':
                            select.Font.Bold = True
                            select.Font.ColorIndex = 5
                        select.TypeText(res_lst[row-3])
                table.Cell(row_param,col).Select()
                res_param = select.Text.encode('unicode-escape').decode('string_escape')
                if re.match(r'pass',res_param,re.M)!=None:
                    pass_flag = pass_flag & 1
                else:
                    pass_flag = 0

            chanlst.append(res_lst[0])
            freqlst.append(res_lst[1])
            senslst.append(res_lst[2])

            rssilst.append(res_lst[3])
            PERlst.append(res_lst[4])
            BERlst.append(res_lst[5])
            #gainlst.append(res_lst[6])
            csvreport1.write_data([rate_name,res_lst[0],res_lst[1],res_lst[2],res_lst[3],res_lst[4],res_lst[5]],float_num=3)

        pylab.figure(100)
        pylab.title("loss=%s"%cable_loss)
        pylab.plot(freqlst,senslst,label='sens_%s'%(rate_name))
        pylab.legend()
        pylab.grid()
        plt.savefig(path+'/'+'pic'+'/'+'bt_sens_%s.png'%(rate_name));
        plt.close()

        if report_en ==1:
            if pass_flag ==1:
                table.Cell(row_len,2).Select()
                select.Font.Bold = True
                select.TypeText(rate_name+' meets the test requirements')
            else:
                table.Cell(row_len,2).Select()
                select.Font.Bold = True
                select.Font.ColorIndex = 5
                select.TypeText(rate_name+' does not meet the test requirements')

            select1= table.Cell(10,2).Select()
            select.InlineShapes.AddPicture(path+'/'+'pic'+'/'+'bt_sens_%s.png'%(rate_name))
        return pass_flag

    def rw_rx_per_sweep_freq_offset(self,ber_limit=0.2,framecnt=1000,edr=0,rate_name='1M_DH1_prbs9',pwrdBm_start=-70,pwrdBm_end=-50,step=1, channel=[0,1,2], file_w = '../bt_rx_per_',cable_loss=0, iqv_no=1,figure_en=0,report_en=0, doc='', select='',ulap=0x6BC6967e,ltaddr=0,max_sens_sel=0):

        if max_sens_sel == 0:
            file1=file_w+'bt_rx_sens_'+rate_name+'.csv'
            f1= open(file1, 'a')
            f1.write('chan, freq, sens(dBm), sens_rssi(dbm),PER,BER\n')
        else:
            file1=file_w+'bt_rx_max_input_'+rate_name+'.csv'
            f1= open(file1, 'a')
            f1.write('chan, freq, max_input(dBm), sens_rssi(dbm),PER,BER\n')

        w_str = ''

        trange="pwr%d_%d_"%(pwrdBm_start, pwrdBm_end)
        f=open(file_w+trange+rate_name+'.csv', 'w')
        f.write('Channel,TX power,freq_offset,TX pac,RX pac,RX correct pac,PER,fail,AER, PER RX pac, RSSI, RX bits,RX err bit,BER \n')
        freq_lst = np.array(channel)+2402
        print 'freq_ls' ,freq_lst
        framecnt_est=framecnt+5


        freqlst = [], ratelst = [], PERlst = [], BERlst = [], senslst = [], rssilst =[], chanlst = []
##        gainlst = []
        pass_flag = 1
        if report_en == 1:
            table = doc.Tables[table_vs_RX_rate_dic[rate_name]]
            row_len = len(table.Rows)
            col_len = len(table.Columns)
            for i in range(0,row_len):
                table.Cell(i,1).Select()
                param = select.Text.encode('unicode-escape').decode('string_escape')
                if re.match(r'Pass/Fail',param,re.M)!=None:
                    row_param = i
            select0 = table.Cell(2,2).Select()
            select.TypeText(rate_name)

        mytester=tester.tester(2402,-40,'1M_DH1_prbs9',1,iqv_no,'source',cable_loss,10,1);
        for freq_offset in range (110,140,10):
            if freq_offset<0:
                freq_offset_init=freq_offset+655356
            else:
                freq_offset_init=freq_offset
            loginfo('freq_offset=%d'%freq_offset)
            self.wifi.rfchsel_offset_esp32(freq_offset_init)
            for i in range(0,len(freq_lst)):
                chan = channel[i]
                freq = freq_lst[i]
                pwrdBm=pwrdBm_start
                cur_sense_find=0
                cur_max_find = 0
                res_lst=[]

                while pwrdBm<=pwrdBm_end:
                    f.write("%dMHz,"%freq)
                    f.write("%ddBm,"%pwrdBm)
                    print pwrdBm
                    [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
                    pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, hec_ep, crc_ep, mic_ep,
                    seq_ep, lt_ep, guard_ep, totalb, cb_err, BER]=self.rw_rx_per_test(framecnt=framecnt,edr=edr,ratename=rate_name,pwrdBm=pwrdBm, freq=freq, cable_loss=cable_loss, iqv_no=iqv_no,ulap=ulap,ltaddr=ltaddr, mytester=mytester)
                    if totalp >= framecnt+10 :
                        [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
                        pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, hec_ep, crc_ep, mic_ep,
                        seq_ep, lt_ep, guard_ep, totalb, cb_err, BER]=self.rw_rx_per_test(framecnt=framecnt,edr=edr,ratename=rate_name,pwrdBm=pwrdBm, freq=freq, cable_loss=cable_loss, iqv_no=iqv_no, ulap=ulap,ltaddr=ltaddr,mytester=mytester)

                    PER=1-(float(cp)/framecnt_est)
        ##            if PER >= per_limit:
        ##                fail=1
        ##            else:
        ##                fail=0
                    AER=1-(float(totalp)/framecnt_est)
                    PER_RX_pac=1
                    #print "%d\n"%totalp
                    if totalp != 0:
                        PER_RX_pac=1-(float(cp)/totalp)

                    if BER >= ber_limit or PER_RX_pac==1:
                        fail=1
                    else:
                        fail=0
                    f.write("%d,%d,%d,%d,%f,%d,%f,%f,%f,%d,%d,%f\n"
                    %(freq_offset, framecnt_est,totalp,cp,PER,fail,AER,PER_RX_pac,RSSI,totalb, cb_err, BER))

                    if max_sens_sel == 0 and cur_sense_find == 0:
                        if BER < ber_limit and PER_RX_pac < 1:
                            res_lst = [chan, freq,pwrdBm,RSSI,PER*100,BER*100]
                            cur_sense_find = 1
                        else:
                            res_lst = [chan, freq,pwrdBm,RSSI,PER*100,BER*100]
                            cur_sense_find = 0

                    if max_sens_sel == 1 and cur_max_find == 0:
                        if BER > ber_limit:
                            res_lst = [chan, freq,pwrdBm,RSSI,PER*100,BER*100]
                            cur_max_find=1
                        else:
                            res_lst = [chan, freq,pwrdBm,RSSI,PER*100,BER*100]
                            cur_max_find=0

                    pwrdBm=pwrdBm+step

                    res_flag = ''
                    if report_en ==1:
                        if res_lst[2] <= BT_param_th_dict[rate_name+'_rssi']:
                            res_flag = 'pass'
                        else:
                            res_flag = 'fail'
                        res_lst.append(res_flag)
                        col = i+2
                        for row in range(3,row_len-1):
                            select1 = table.Cell(row,col).Select()
                            select.Font.Bold = False
                            select.Font.Italic = False
                            select.Font.ColorIndex = 1
                            if row>= 5 and row<=(row_param-1):
                                if  res_flag == 'fail':
                                    select.Font.Bold = True
                                    select.Font.ColorIndex = 5
                                select.TypeText('%2.2f'%res_lst[row-3])
                            else:
                                if  res_flag == 'fail':
                                    select.Font.Bold = True
                                    select.Font.ColorIndex = 5
                                select.TypeText(res_lst[row-3])
                        table.Cell(row_param,col).Select()
                        res_param = select.Text.encode('unicode-escape').decode('string_escape')
                        if re.match(r'pass',res_param,re.M)!=None:
                            pass_flag = pass_flag & 1
                        else:
                            pass_flag = 0

            chanlst.append(res_lst[0])
            freqlst.append(res_lst[1])
            senslst.append(res_lst[2])

            rssilst.append(res_lst[3])
            PERlst.append(res_lst[4])
            BERlst.append(res_lst[5])
##            gainlst.append(res_lst[6])
            w_str += '%d'%res_lst[0]+','+'%s'%res_lst[1]+','+'%2.2f'%res_lst[2]+','+'%2.2f'%res_lst[3]+','+'%2.2f'%res_lst[4]+','+'%2.3f'%res_lst[5]+'\n'

        if figure_en==1:
            pylab.figure(100)
            pylab.title("loss=%s"%cable_loss)
            pylab.plot(freqlst,senslst,label='sens_%s'%(rate_name))
            pylab.legend()
            pylab.grid()
            plt.savefig(file_w+'/'+'pic'+'/'+'bt_sens_%s.png'%(rate_name));
            plt.close()

        if report_en ==1:
            if pass_flag ==1:
                table.Cell(row_len,2).Select()
                select.Font.Bold = True
                select.TypeText(rate_name+' meets the test requirements')
            else:
                table.Cell(row_len,2).Select()
                select.Font.Bold = True
                select.Font.ColorIndex = 5
                select.TypeText(rate_name+' does not meet the test requirements')

            select1= table.Cell(10,2).Select()
            select.InlineShapes.AddPicture(file_w+'/'+'pic'+'/'+'bt_sens_%s.png'%(rate_name))

        f1.write(w_str)
        f.close
        return pass_flag

    def str_into_int_arr(self,str1):
        int_list =[]
        list1 = str1.split(',')
        for i in range (0,len(list1)):
            int_list.append(int(list1[i]))
        return int_list

    def Read_bt_test_case(self,sheet_num=1):
        excelapp = win32com.client.Dispatch('Excel.Application')
        excelapp.Visible = 0
        excel = excelapp.Workbooks.Open("D:/chip/eagletest/py_script/rftest/test_script/BT_AutoTest" + "\\BT_case_setting.xls")
        sheet = excel.Worksheets(sheet_num)
        test_case_list= []
        test_chan_list = []
        test_pwr1_list = []
        test_pwr2_list = []
        test_enable_list = []
        test_information = []
        No = []

        if sheet_num == 1:
            for i in range(2,71):
                if (i == 11) or (i == 30) or (i == 43) or (i == 57):
                    print 'null'
                else:
                    test_enable = sheet.Cells(i,8).Value
                    if test_enable == 'Yes':
                      no = int(sheet.Cells(i,1).Value)
                      test_case = sheet.Cells(i,3).Value
                      loginfo('no=%s,case=%s'%(no,test_case))
                      pwr_level = sheet.Cells(i,4).Value
                      if pwr_level == 'User Defined':
                          pwr_level = self.str_into_int_arr(sheet.Cells(i,5).Value)
                      elif pwr_level == 'ALL':
                          pwr_level = [0,1,2,3,4,5,6,7,8]
                      else:
                          maxpwr = int(sheet.Cells(i,4).Value)
                          pwr_level = maxpwr
                      Channel = sheet.Cells(i,6).Value
                      if Channel == 'User Defined':
                          Channel = self.str_into_int_arr(sheet.Cells(i,7).Value)
                      elif Channel == 'ALL':
                          chan_m = []
                          if no <28 or (no >30 and no <40):
                              for m in range(0, 79):
                                  chan_m.append(m)
                          else:
                              for m in range(0, 40):
                                  chan_m.append(m)
                          Channel = chan_m
                      elif Channel == '[0&39&78]':
                          Channel = [0,39,78]
                      elif Channel == '[0&10&20&30&40&50&60&70&78]':
                          Channel = [0,10,20,30,40,50,60,70,78]
                      elif Channel == '[0&5&10&15&20&25&30&35&39]':
                          Channel = [0,5,10,15,20,25,30,35,39]
                      elif Channel == '[0&39]':
                          Channel = [0,39]
                      elif Channel == '[0&10&20&30&39]':
                          Channel = [0,10,20,30,39]
                      else:
                          Channel = [0]
                      print Channel
                      No.append(no)
                      test_case_list.append(str(test_case))
                      test_pwr1_list.append(pwr_level)
                      test_chan_list.append(Channel)
                      if i >= 35:
                          minpwr = sheet.Cells(i,5).Value
                          print minpwr
                          test_pwr2_list.append(int(minpwr))
                      else:
                          test_pwr2_list.append(-999.99)

            print No,test_case_list,test_pwr1_list,test_pwr2_list,test_chan_list

            Module_Name = str(sheet.Cells(73,3).Value)
            print 'Module_Name=',Module_Name
            Sample_Number = str(sheet.Cells(75,3).Value)
            print 'Sample_Number=',Sample_Number
            Test_Bin = str(sheet.Cells(80,3).Value)
            print 'Test_Bin=',Test_Bin
            Cable_loss = (float(sheet.Cells(81,3).Value))
            print 'Cable_loss=',Cable_loss
            rf_port = int(sheet.Cells(83,3).Value)
            print 'rf_port=',rf_port

            for row in range(73,84):
                test_information.append(str(sheet.Cells(row,3).Value))
            excel.Save()
            excel.Close()
            excelapp.Quit()

        elif sheet_num == 2:
            for i in range(2,18):
                if i == 18:
                    print 'null'
                else:
                    test_enable = sheet.Cells(i,8).Value
                    if test_enable == 'Yes':
                       no = int(sheet.Cells(i,1).Value)
                       test_case = sheet.Cells(i,3).Value
                       print 'no,case',no,test_case
                       pwr_level = sheet.Cells(i,4).Value
                       if pwr_level == 'User Defined':
                           pwr_level = self.str_into_int_arr(sheet.Cells(i,5).Value)
                       elif pwr_level == 'ALL':
                           pwr_level = [0,1,2,3,4,5,6,7,8]
                       else:
                           maxpwr = int(sheet.Cells(i,4).Value)
                           pwr_level = maxpwr
                       Channel = sheet.Cells(i,6).Value
                       if Channel == 'User Defined':
                           Channel = self.str_into_int_arr(sheet.Cells(i,7).Value)
                       elif Channel == 'ALL':
                           chan_m = []
                           if no <28 or (no >30 and no <40):
                               for m in range(0, 79):
                                   chan_m.append(m)
                           else:
                               for m in range(0, 40):
                                   chan_m.append(m)
                           Channel = chan_m
                       elif Channel == '[0&39&78]':
                           Channel = [0,39,78]
                       elif Channel == '[0&10&20&30&40&50&60&70&78]':
                           Channel = [0,10,20,30,40,50,60,70,78]
                       elif Channel == '[0&5&10&15&20&25&30&35&39]':
                           Channel = [0,5,10,15,20,25,30,35,39]
                       elif Channel == '[0&39]':
                           Channel = [0,39]
                       elif Channel == '[0&10&20&30&39]':
                           Channel = [0,10,20,30,39]
                       else:
                           Channel = [0]
                       print Channel
                       No.append(no)
                       test_case_list.append(str(test_case))
                       test_pwr1_list.append(pwr_level)
                       test_chan_list.append(Channel)
                       if i >= 6:
                           minpwr = sheet.Cells(i,5).Value
                           print minpwr
                           test_pwr2_list.append(int(minpwr))
                       else:
                           test_pwr2_list.append(-999.99)

            print No,test_case_list,test_pwr1_list,test_pwr2_list,test_chan_list

            Module_Name = str(sheet.Cells(20,3).Value)
            print 'Module_Name=',Module_Name
            Sample_Number = str(sheet.Cells(22,3).Value)
            print 'Sample_Number=',Sample_Number
            Test_Bin = str(sheet.Cells(27,3).Value)
            print 'Test_Bin=',Test_Bin
            Cable_loss = (float(sheet.Cells(28,3).Value))
            print 'Cable_loss=',Cable_loss
            rf_port = int(sheet.Cells(30,3).Value)
            print 'rf_port=',rf_port

            for row in range(20,31):
                test_information.append(str(sheet.Cells(row,3).Value))
            excel.Save()
            excel.Close()
            excelapp.Quit()

        return [No,test_case_list,test_pwr1_list,test_pwr2_list,test_chan_list,Module_Name,Sample_Number,Test_Bin,Cable_loss,rf_port,test_information]


    def write_test_information_to_word(self,test_information=[],doc='',select=''):
        table = doc.Tables[1]
        select0 = table.Select()
        row_len = len(table.Rows)
        for row in range(2,row_len):
            select1 = table.Cell(row,2).Select()
            select.TypeText(test_information[row-2])


    def bt_test_case(self,sheet=1):

        [No,test_case,test_pwr1,test_pwr2,test_chan,Module_Name,Sample_Number,Test_Bin,Cable_loss,rf_port,test_information] = self.Read_bt_test_case(sheet)
        print [No,test_case,test_pwr1,test_pwr2,test_chan,Module_Name,Sample_Number,Test_Bin,Cable_loss,rf_port,test_information]

        PATH = self.rf_bt_autotest_data
        PATH_Script =  "D:/chip/eagletest/py_script/rftest/test_script/BT_AutoTest"

        filetime = time.strftime('_%Y%m%d_%H%M%S',time.localtime(time.time()));
        data_path = PATH +'%s'%(Module_Name)+filetime+'/'
        os.mkdir(PATH +'%s'%(Module_Name)+filetime)
        file_name = '%s'%(Module_Name)+filetime

        if sheet == 1:
            for i in range (0,len(test_case)):
                print No[i],test_case[i],test_pwr1[i], test_pwr2[i],test_chan[i]
                if No[i] > 36 and No[i] < 40:
                    self.rw_rx_per_sweep(ber_limit=0.001,framecnt=1000,edr=0,rate_name=test_case[i],pwrdBm_start=test_pwr1[i],step=1,pwrdBm_end=test_pwr2[i],channel=test_chan[i],file_w=file_name,cable_loss=Cable_loss, iqv_no=rf_port,report_en=0, doc='', select='',ulap=0x6BC6967e,ltaddr=0,max_sens_sel=0)
                elif No[i] >= 40 and No[i] < 46:
                    self.rw_rx_per_sweep(ber_limit=0.0001,framecnt=1000,edr=1,rate_name=test_case[i],pwrdBm_start=test_pwr1[i],step=1,pwrdBm_end=test_pwr2[i],channel=test_chan[i],file_w=file_name,cable_loss=Cable_loss, iqv_no=rf_port,report_en=0, doc='', select='',ulap=0x6BC6967e,ltaddr=0,max_sens_sel=0)
                elif No[i] >= 46 and No[i] < 50:
                    self.rw_le_rx_per_sweep(per_limit=0.308,framecnt=1000,rate_name=test_case[i],pwrdBm_start=test_pwr1[i],step=1,pwrdBm_end=test_pwr2[i],channel=test_chan[i],file_w=file_name,cable_loss=Cable_loss, iqv_no=rf_port, report_en=0, doc='', select='',syncw=0x71764129,max_sens_sel=0)
                elif No[i] >= 50 and No[i] < 53:
                    self.rw_rx_per_sweep(ber_limit=0.001,framecnt=1000,edr=0,rate_name=test_case[i],pwrdBm_start=test_pwr1[i],step=1,pwrdBm_end=test_pwr2[i],channel=test_chan[i],file_w=file_name,cable_loss=Cable_loss, iqv_no=rf_port,report_en=0, doc='', select='',ulap=0x6BC6967e,ltaddr=0,max_sens_sel=1)
                elif No[i] >= 53 and No[i] < 59:
                    self.rw_rx_per_sweep(ber_limit=0.0001,framecnt=1000,edr=1,rate_name=test_case[i],pwrdBm_start=test_pwr1[i],step=1,pwrdBm_end=test_pwr2[i],channel=test_chan[i],file_w=file_name,cable_loss=Cable_loss, iqv_no=rf_port,report_en=0, doc='', select='',ulap=0x6BC6967e,ltaddr=0,max_sens_sel=1)
                elif No[i] >= 59 and No[i] < 63 :
                    self.rw_le_rx_per_sweep(per_limit=0.308,framecnt=1000,rate_name=test_case[i],pwrdBm_start=test_pwr1[i],step=1,pwrdBm_end=test_pwr2[i],channel=test_chan[i], file_w=file_name,cable_loss=Cable_loss, iqv_no=rf_port, report_en=0, doc='', select='',syncw=0x71764129,max_sens_sel=1)
                elif No[i] >= 1 and No[i] < 28 :
                    self.BT_TX_PWR_EVM(cable_loss=Cable_loss,pwr_level=test_pwr1[i], channel=test_chan[i],rate_lst=[str(test_case[i])],iqv_no=rf_port, iqv_num=10,file_w=file_name)
                else:
                    self.LE_TX_PWR_EVM(cable_loss=Cable_loss,pwr_level=test_pwr1[i], channel=test_chan[i],rate_lst=[str(test_case[i])],iqv_no=rf_port, iqv_num=10,file_w=file_name)

        elif sheet == 2:
            wordapp = Dispatch('Word.Application')
            wordapp.Visible = 1
            doc = wordapp.Documents.Open(PATH_Script+"\\ESP_Buletooth_A2_Test_Report.docx")
            doc.SaveAs(data_path+"\\ESP_Buletooth_A2_Test_Report_%s_%s_%s.docx"%(Module_Name,Sample_Number,Test_Bin))
            doc.Close()
            doc = wordapp.Documents.Open(data_path+"\\ESP_Buletooth_A2_Test_Report_%s_%s_%s.docx"%(Module_Name,Sample_Number,Test_Bin))
            select = wordapp.Selection
            print test_information
            self.write_test_information_to_word(test_information,doc,select)

            res_lst0 =[]
            res_lst =[]

            for i in range (0,len(test_case)):
                res = 0
                print No[i],test_case[i],test_pwr1[i], test_pwr2[i],test_chan[i]
                if No[i] == 13:
                    res =self.rw_rx_per_sweep(ber_limit=0.001,framecnt=1000,edr=0,rate_name=test_case[i],pwrdBm_start=test_pwr1[i],pwrdBm_end=test_pwr2[i],step=1,channel=test_chan[i], file_w=file_name,cable_loss=Cable_loss, iqv_no=rf_port,report_en=1, doc=doc, select=select,ulap=0x6BC6967e,ltaddr=0)
                elif No[i] >= 14 and No[i] < 16:
                    res =self.rw_rx_per_sweep(ber_limit=0.0001,framecnt=1000,edr=1,rate_name=test_case[i],pwrdBm_start=test_pwr1[i],pwrdBm_end=test_pwr2[i],step=1,channel=test_chan[i],file_w=file_name,cable_loss=Cable_loss, iqv_no=rf_port,report_en=1, doc=doc, select=select,ulap=0x6BC6967e,ltaddr=0)
                elif No[i] == 16:
                    res =self.rw_le_rx_per_sweep(per_limit=0.308,framecnt=1000,rate_name=test_case[i],pwrdBm_start=test_pwr1[i],pwrdBm_end=test_pwr2[i],step=1,channel=test_chan[i],file_w=file_name,cable_loss=Cable_loss, iqv_no=rf_port, report_en=1, doc=doc, select=select,syncw=0x71764129)
                else:
                    res =self.BT_TX_PWR_EVM_A2(cable_loss=Cable_loss,pwr_level=test_pwr1[i], channel=test_chan[i],rate_name=test_case[i],iqv_no=rf_port, iqv_num=10, report_en=1, doc=doc, select=select, file_w=file_name)

                res_lst0.append([No[i],res])

            print 'res_lst0******',res_lst0
            for i in range(1,17):
                res_lst.append([i,0])

            for j in range(0,len(res_lst0)):
                for i in range(0,len(res_lst)):
                    if res_lst0[j][0]==res_lst[i][0]:
                        res_lst[i][1] = res_lst0[j][1]
                        break

            print 'debug************',res_lst

            for i in range(0,4):
                if res_lst[i*3+0][1]==1 and res_lst[i*3+1][1]==1 and res_lst[i*3+2][1]==1:
                    table = doc.Tables[2]
                    table.Cell(3+i,3).Select()
                    select.TypeText('pass')
                else:
                    table = doc.Tables[2]
                    table.Cell(3+i,3).Select()
                    select.Font.Bold = True
                    select.Font.ColorIndex = 5
                    select.TypeText('fail')

            for i in range(0,4):
                if res_lst[12+i][1]==1:
                    table = doc.Tables[3]
                    table.Cell(3+i,3).Select()
                    select.TypeText('pass')
                else:
                    table = doc.Tables[3]
                    table.Cell(3+i,3).Select()
                    select.Font.Bold = True
                    select.Font.ColorIndex = 5
                    select.TypeText('fail')

            doc.SaveAs()
                #wordapp.Quit()

##    def combine_csv_data(self,)
##        filename_list =
##        file_list = glob.glob('D:/mystuff/Excel_App/*csv')
##        print ('total %d csv file'% len(file_list))
##        df = pd.read_csv(file_list[0])
##        df.to_csv('result.csv',encoding='utf-8-sig',index=False)
##        for i in range(1,len(file_list)):
##        df = pd.read_csv(file_list[i])
##        df.to_csv('result.csv',encoding='utf-8-sig',index=False,header=False,mode='a+')


        print '\n\n----------test complete----------------\n'


    def rw_le_rx_per_sweep_full(self,file_w='LE_RX_725_SPLITAGC',cable_loss=0, iqv_no=1):
        
        self.rw_le_rx_per_sweep(per_limit=0.3,framecnt=1000,rate_name='LE1M_4POS_prbs9',rate= 0, pwrdBm_start=-105,pwrdBm_end=-30, step=1,channel=[0,19,39], file_w =file_w,cable_loss=cable_loss, iqv_no=iqv_no, report_en=0, doc='', select='',syncw=0x71764129)
        self.rw_le_rx_per_sweep(per_limit=0.3,framecnt=1000,rate_name='LE2M_4POS_prbs9',rate= 1, pwrdBm_start=-105,pwrdBm_end=-30, step=1,channel=[0,19,39], file_w =file_w,cable_loss=cable_loss, iqv_no=iqv_no, report_en=0, doc='', select='',syncw=0x71764129)
        self.rw_le_rx_per_sweep(per_limit=0.3,framecnt=1000,rate_name='LE500K_4POS_prbs9_240',rate= 2, pwrdBm_start=-105,pwrdBm_end=-30, step=1,channel=[0,19,39], file_w =file_w,cable_loss=cable_loss, iqv_no=iqv_no, report_en=0, doc='', select='',syncw=0x71764129)
        self.rw_le_rx_per_sweep(per_limit=0.3,framecnt=1000,rate_name='LE125K_4POS_prbs9_240',rate= 2, pwrdBm_start=-105,pwrdBm_end=-30, step=1,channel=[0,19,39], file_w =file_w,cable_loss=cable_loss, iqv_no=iqv_no, report_en=0, doc='', select='',syncw=0x71764129)
         
         
        self.rw_le_rx_per_sweep(per_limit=0.3,framecnt=1000,rate_name='LE1M_1POS_prbs9',rate= 0, pwrdBm_start=-105,pwrdBm_end=-30, step=1,channel=[0,19,39], file_w =file_w,cable_loss=cable_loss, iqv_no=iqv_no, report_en=0, doc='', select='',syncw=0x71764129)
        self.rw_le_rx_per_sweep(per_limit=0.3,framecnt=1000,rate_name='LE2M_1POS_prbs9',rate= 1, pwrdBm_start=-105,pwrdBm_end=-30, step=1,channel=[0,19,39], file_w =file_w,cable_loss=cable_loss, iqv_no=iqv_no, report_en=0, doc='', select='',syncw=0x71764129)
        self.rw_le_rx_per_sweep(per_limit=0.3,framecnt=1000,rate_name='LE500K_1POS_prbs9_240',rate= 2, pwrdBm_start=-105,pwrdBm_end=-30, step=1,channel=[0,19,39], file_w =file_w,cable_loss=cable_loss, iqv_no=iqv_no, report_en=0, doc='', select='',syncw=0x71764129)
        self.rw_le_rx_per_sweep(per_limit=0.3,framecnt=1000,rate_name='LE125K_1POS_prbs9_240',rate= 2, pwrdBm_start=-105,pwrdBm_end=-30, step=1,channel=[0,19,39], file_w =file_w,cable_loss=cable_loss, iqv_no=iqv_no, report_en=0, doc='', select='',syncw=0x71764129)


    def split_agc_test(self, file_w='LE_RX_725_SPLITAGC',cable_loss=0, iqv_no=1):
        self.mem.wrm(0x60026010, 19,16,0xf)
        self.mem.wrm(0x60026010, 3,0,0xf)
        self.rw_le_rx_per_sweep_full(file_w=file_w+'_BTAGC',cable_loss=cable_loss, iqv_no=iqv_no)
        self.mem.wrm(0x60026010, 19,16,0)
        self.mem.wrm(0x60026010, 3,0,0)
        self.rw_le_rx_per_sweep_full(file_w=file_w+'_WIFIAGC',cable_loss=cable_loss, iqv_no=iqv_no)        

table_vs_TX_rate_dic = {
    '1M_DH5_1010':5,
    '1M_DH5_00001111':6,
    '1M_DH5_prbs9':7,
    '2M_DH5_1010':9,
    '2M_DH5_00001111':10,
    '2M_DH5_prbs9':11,
    '3M_DH5_1010':13,
    '3M_DH5_00001111':14,
    '3M_DH5_prbs9':15,
    'LE_1M_1010':17,
    'LE_1M_00001111':18,
    'LE_1M_prbs9':19,
}


table_vs_RX_rate_dic = {
    "1M_DH5_prbs9":21,
    "2M_DH5_prbs9":22,
    "3M_DH5_prbs9":23,
    "LE_1M_prbs9":24,
}


BT_param_th_dict ={
    'Init_Freq_Err':[-75,75],
    'deltaF1Avg':[140,175],
    'deltaF2Max':[115,500],
    'deltaF2Avg':[112,500],
    'bandwidth20dB':[500,1000],
    'LE_Init_Freq_Err':[-150,150],
    'LE_deltaF1Avg':[225,275],
    'LE_deltaF2Max':[185,500],
    'LE_deltaF2Avg':[180,500],
    'OMEGA_I':[-75,75],
    'OMEGA_O':[-10,10],
    'OMEGA_IO':[-75,75],
    '2M_DEVM_Average(%)':[0,20],
    '3M_DEVM_Average(%)':[0,13],
    '2M_DEVM_Peak(%)':[0,35],
    '3M_DEVM_Peak(%)':[0,25],
    '2M_EdrprobEVM99pass':[0,30],
    '3M_EdrprobEVM99pas':[0,20],
    'EdrPowDiffdB':[-4,1],
    '1M_DH5_prbs9_rssi':-80,
    '2M_DH5_prbs9_rssi':-80,
    '3M_DH5_prbs9_rssi':-72,
    'LE_prbs9_rssi':-85,
    'LE_1M_prbs9_rssi':-85

}



