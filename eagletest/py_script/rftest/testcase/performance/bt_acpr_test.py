from rftest.rflib.wifi_lib import WIFILIB
from hal.bt_api import BTAPI
from hal.Init import HALS
from hal.common import *
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
from rftest.rflib import bt_instrum
from baselib.instrument.tester_serv import wt200_serv
from baselib.instrument import sme
from rftest.rflib.csv_report import csvreport
from rftest.rflib import rfglobal
from rftest.testcase.performance.wifi_txrx_test import WIFI_TXRX_TEST
from baselib.instrument import tester
from rftest.testcase.performance.Interfer_miti_test import Interfer_Test
from rftest.testcase.performance.bt_auto_test import BtAutoTest
from baselib.instrument.spa import HP,Agilent
from rftest.rflib.adc_dump import DUMP
from rftest.rflib.pbus import pbus
from hal.wifi_api import WIFIAPI
CI_ratio_vs_data_rate = {
'1M_DH5_prbs9':  [11,  0, -30, -40, -9, -20], # C/I ratio : f_RX + [0 , ?1, ?2,...]
'2M_DH5_prbs9':  [13,  0, -30, -40, -7, -20],
'3M_DH5_prbs9':  [21,  5, -25, -33,  0, -13],
'LE_1M_prbs9':   [21, 15, -17, -27, -9, -15],
'LE_2M_prbs9':   [21, 15, -17, -27, -9, -15],
'LE_125K_prbs9': [12,  6, -26, -36,-18, -24],
'LE_500K_prbs9': [17, 11, -21, -31,-13, -19]
}

pwr_interfere_vs_data_rate = {
'1M_DH5_prbs9':[-71,-60,-30,-27,-58,-47],
'2M_DH5_prbs9':[-73,-60,-30,-27,-60,-47],
'3M_DH5_prbs9':[-81,-65,-35,-34,-67,-54],
'LE_1M_prbs9': [-88,-82,-50,-40,-58,-52],
'LE_2M_prbs9': [-88,-82,-50,-40,-58,-52],
'LE_125K_prbs9': [-91,-85,-53,-43,-61,-55],
'LE_500K_prbs9': [-89,-83,-51,-41,-59,-53],
}

pwr_signal_vs_data_rate ={
'1M_DH5_prbs9': [-60,-60,-60,-67,-67,-67],# ref sensitivity level:-70; 10dB over the reference sensitivity level for co_channel?adjacent 1M?2M; 3dB over the reference sensitivity level for Interfering signal on all other frequencies
'2M_DH5_prbs9': [-60,-60,-60,-67,-67,-67],
'3M_DH5_prbs9': [-60,-60,-60,-67,-67,-67],# ref sensitivity level:-70; 10dB over the reference sensitivity level for co_channel,adjacent 1M\2M; 3dB over the reference sensitivity level for Interfering signal on all other frequencies
'LE_1M_prbs9':  [-67,-67,-67,-67,-67,-67], # 3dB over the reference sensitivity(-70) level for Interfering signal on all other frequencies,
'LE_2M_prbs9':  [-67,-67,-67,-67,-67,-67],
'LE_125K_prbs9':  [-79,-79,-79,-79,-79,-79], # sensitivity -82
'LE_500K_prbs9':  [-72,-72,-72,-72,-72,-72], # sensitivity -75
}


class Bt_Interfer_Test(object):

    def __init__(self,comport,chipv='ESP32'):
        self.comport = comport
        self.chipv = chipv
        self.mem = MEM(self.comport,self.chipv)
        self.wifiapi = WIFIAPI(self.comport,self.chipv)
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.bt = BTAPI(self.comport,self.chipv)
        self.bt_a2_test = BtAutoTest(self.comport,self.chipv)
        self.interfer_test = Interfer_Test(self.comport,self.chipv)
        self.pbus = pbus(self.comport,self.chipv)
        self.adc_dump = DUMP(self.comport,self.chipv)
        self.rf_bt_autotest_data = "D:/chip/eagletest/py_script/rftest/rfdata/bt_auto_data/"
        self.folder = 'bt_auto_data'



    def bt_block_test(self,iq_signal='iqxel', lost_list=[8,6.3], pwr_interfere_step=1, iqv_signal_no=1,Module_Name='ESP32_Testboard',Module_Num=''):

        '''
        iq_signal='iqxel' or 'wt200'

        '''
        cable_lose_signal = lost_list[0]
        cable_lose_interfere = lost_list[1]
        #data_rate = ['1M_DH1_prbs9',]
        if self.chipv == "ESP32":
            data_rate = ['LE_1M_prbs9','1M_DH1_prbs9','2M_DH1_prbs9','3M_DH1_prbs9']
        elif self.chipv == "CHIP724":
            data_rate = ['LE_1M_prbs9','LE_2M_prbs9','LE_125K_prbs9','LE_500K_prbs9']

        LE_interfere ={
           '0': [2400,2484,-67,-30,-30,2], #test sme
           '1': [30,  2000,-67, -10,-30,10], #Blocking signal level at IUT input port -30
           '2': [2003,2300,-67, -10,-35, 3], #Blocking signal level at IUT input port -35
           '3': [2300,2399,-67, -15,-35, 3], #Blocking signal level at IUT input port -35
           '4': [2484,2600,-67, -15,-35, 3], #Blocking signal level at IUT input port -35
           '5': [2600,2997,-67, -10,-35, 3], #Blocking signal level at IUT input port -35
           '6': [3000,6000,-67, -10,-30, 25], #Blocking signal level at IUT input port -30
           '7': [1213,1213,-67, -10,-20, 10], #Blocking signal level at IUT input port -35,using esp_filter,2.4G atten 38dB ,1.2G atten 1.8dB
        }

        BT_interfere ={
           '0': [2400,2484,-67,-27,-27,2], #test sme
           '1': [30,  2000,-67,-5,-10, 10], #Blocking signal level at IUT input port -10
           '2': [2000,2300,-67,-10,-25, 3],  #Blocking signal level at IUT input port -27
           '3': [2300,2400,-67,-15,-25, 3],  #Blocking signal level at IUT input port -27
           '4': [2500,2600,-67,-15,-25, 3],  #Blocking signal level at IUT input port -27
           '5': [2600,3000,-67,-10,-25, 3],  #Blocking signal level at IUT input port -27
           '6': [3000,6000,-67,-5,-10, 25] , #Blocking signal level at IUT input port -10
           '7': [1230,1230,-67,-17,-27,10],  #Blocking signal level at IUT input port -27, using esp_filter,2.4G atten 38dB ,1.2G atten 1.8dB
        }
        inter_freq_len = 6
        LE_freq_signal = 2426
        BT_freq_signal = 2460

        framecnt  = 1500
        framecnt_est = framecnt
        per_limit  = 0.308
        ber_limit ={
        '1M_DH1_prbs9' : 0.001,
        '2M_DH1_prbs9' : 0.0001,
        '3M_DH1_prbs9' : 0.0001
        }

        # wanted signal
        mytester=tester.tester(2402,-40,'1M_DH1_prbs9',1,iqv_signal_no,'source',cable_lose_signal,isreset=1);
        # Interfering signal
        mysig_gen = sme.sme();# signal generator!

        for cur_rate in data_rate:

            [LE_flag,drate,DH,dtype] = bt_instrum.name2rate(cur_rate)

            for interfere_j in range(1,7):
                interfere_j = str(interfere_j)
                if LE_flag == 1:
                    freq_signal = LE_freq_signal
                    start_freq_interfere = LE_interfere[interfere_j][0]
                    stop_freq_interfere = LE_interfere[interfere_j][1]
                    pwr_signal = LE_interfere[interfere_j][2]
                    start_pwr_interfere = LE_interfere[interfere_j][3]
                    stop_pwr_interfere = LE_interfere[interfere_j][4]
                    step_freq_interfere = LE_interfere[interfere_j][5]
                else:
                    freq_signal = BT_freq_signal
                    start_freq_interfere = BT_interfere[interfere_j][0]
                    stop_freq_interfere = BT_interfere[interfere_j][1]
                    pwr_signal = BT_interfere[interfere_j][2]
                    start_pwr_interfere = BT_interfere[interfere_j][3]
                    stop_pwr_interfere = BT_interfere[interfere_j][4]
                    step_freq_interfere = BT_interfere[interfere_j][5]

                w_str = ''

                name_str = '%s_freq_signal_%s_%s_freq_interfere_%s_%s_interferce_%s_%s'%(cur_rate,freq_signal,pwr_signal,start_freq_interfere,stop_freq_interfere ,start_pwr_interfere,stop_pwr_interfere)
                #f=open(data_path+name_str+'.csv', 'a')
                fname = self.wifi.get_filename(self.folder,'bt_blocking_%s'%(name_str),'BT_Blocking')
                title = 'freq_signal,pwr_signal,freq_interfere,pwr_interfere,TX pac,RX pac,RX correct pac,PER,fail,AER, PER RX pac, RSSI, RX bits,RX err bit,BER,gain \n'
                fw1=csvreport(fname,title)

                pwr_interfere = start_pwr_interfere

                while pwr_interfere >= stop_pwr_interfere :

                    mysig_gen.setpow(pwr_interfere+cable_lose_interfere)
                    loginfo("start_freq_interfere=%d,stop_freq_interfere=%d,pwr_interfere=%d,freq_signal=%d,pwr_signal=%d"%(start_freq_interfere,stop_freq_interfere,pwr_interfere,freq_signal,pwr_signal))

                    freq_interfere = start_freq_interfere
                    while freq_interfere <= stop_freq_interfere:

                        mysig_gen.setfreq(freq_interfere*1e6)
                        mysig_gen.setpow(pwr_interfere+cable_lose_interfere)
                        mysig_gen.rfon();
                        #cur_sense_find=0

                        if LE_flag ==1:
                            [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, type_ep, len_ep, crc_ep,
                            mic_ep, sn_ep, nesn_ep,time_ep,priv_ep,gainmax, gainmin, rssimax, rssimin]=self.bt_a2_test.rw_le_rx_per_test(framecnt=framecnt,ratename=cur_rate,rate=drate, pwrdBm=pwr_signal, freq=freq_signal, cable_loss=cable_lose_signal, iqv_no=iqv_signal_no, syncw=0x71764129,mytester =mytester)
                            totalb = - 0.99
                            cb_err = -0.99
                            BER = -0.99
                        else:
                            if drate >1 :
                                edr = 1
                            else:
                                edr = 0
                            [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, hec_ep, crc_ep, mic_ep,
                            seq_ep, lt_ep, guard_ep, totalb, cb_err, BER]=self.bt_a2_test.rw_rx_per_test(framecnt=framecnt,edr=edr,ratename=cur_rate,pwrdBm=pwr_signal, freq=freq_signal, cable_loss=cable_lose_signal, iqv_no=iqv_signal_no,ulap=0x6BC6967e,ltaddr=0, mytester=mytester)

                        PER=1-(float(cp)/framecnt_est)
                        if LE_flag ==1:
                            if PER >= per_limit or cp == 0:
                                fail=1
                            else:
                                fail=0
                        else:
                            if BER >= ber_limit[cur_rate] or cp == 0:
                                fail=1
                            else:
                                fail=0
                        AER=1-(float(totalp)/framecnt_est)
                        PER_RX_pac=1

                        if totalp != 0:
                            PER_RX_pac=1-(float(cp)/totalp)
                        fw1.write_data([freq_signal,pwr_signal,freq_interfere,pwr_interfere,framecnt_est,totalp,cp,PER,fail,AER,PER_RX_pac,RSSI,totalb, cb_err, BER,gain])

                        freq_interfere=freq_interfere+step_freq_interfere
                    pwr_interfere = pwr_interfere - pwr_interfere_step
            mytester.gen_switch('OFF',iqv_signal_no)
            mysig_gen.rfoff()



    def bt_acpr_test(self,iq_signal='wt208c',iq_interfere='iqxel', lost_list=[8,6.3], pwr_interfere_step=1, pwr_signal_step=1, iqv_signal_no=1,iqv_interfere_no=1,Module_Name='ESP32_Testboard',Module_Num='',ci_num=2):


        '''
        iq_signal='iqxel' and iq_interfere='wt200': iqxel is signal source, wt200 is interfere source

        '''
        logsetlevel("D")
        fname = self.wifi.get_filename(self.folder,'bt_acpr_test','BT_ACPR')
        title = 'rate, rx_freq, sens, freq_interfere,pwr_interfere,sens_rssi, sens_find, PER, BER,Ratio_limit,ratio,margin\n'
        fw1=csvreport(fname,title)

        cable_lose_signal = lost_list[0]
        cable_lose_interfere = lost_list[1]

        if self.chipv == "ESP32":
            data_rate = ['LE_1M_prbs9','1M_DH5_prbs9','2M_DH5_prbs9','3M_DH5_prbs9']
        elif self.chipv == "CHIP724":
            data_rate = ['LE_1M_prbs9','LE_2M_prbs9','LE_125K_prbs9','LE_500K_prbs9']

        freq_signal_list = [2441]
        #freq_signal_list = [2405,2441,2477]  #   freq_signal + 1 ,LE : [2406,2442,2478]
        freq_image = 4
        framecnt  = 1500
        framecnt_est = framecnt
        per_limit  = 0.308
        ber_limit ={
        '1M_DH5_prbs9' : 0.001,
        '2M_DH5_prbs9' : 0.001,
        '3M_DH5_prbs9' : 0.001
        }

        freq_signal_lst = []
        pwr_signal_lst = []
        freq_offset_interfere_lst = []
        pwr_interfere_lst = []
        senslst = []
        rssilst = []
        PERlst = []
        BERlst = []
        ratio_lst = []

        # wanted signal
        if iq_signal == 'iqview':
            mytester=tester.tester(2402,-40,'LE_1M_prbs9',1,iqv_signal_no,'source',cable_lose_signal,isreset=1)
            res_sig = -99
        else:
            res_sig = self.interfer_test.iq_open(iq_signal)
            mytester = iq_signal
        # Interfering signal
        res_inf = self.interfer_test.iq_open(iq_interfere)

        sig_freq_l = len(freq_signal_list)

        for cur_rate in data_rate:
            [LE_flag,drate,DH,dtype] = bt_instrum.name2rate(cur_rate)
            if LE_flag == 1 and drate ==1 :
                freq_image_offset = 2
            else:
                freq_image_offset = 1

            for j in range(0,sig_freq_l):
                freq_signal = freq_signal_list[j]
                if LE_flag == 1:
                    freq_signal = freq_signal + 1

                for freq_offset in range(-1,2,2):
                    if freq_offset==0: num = 1
                    else: num = ci_num

                    for i in range(0,num):
                        if i == 0 :
                            freq_interfere_offset = freq_offset
                        else:
                            freq_interfere_offset= -freq_offset

                        if LE_flag == 1 and drate ==1 : # LE_2M, freq_offset * 2
                            freq_interfere_offset = freq_interfere_offset * 2

                        if abs(freq_interfere_offset) <= 3 or ( LE_flag == 1 and drate ==1 and (abs(freq_interfere_offset/2) <=3)):
                            if LE_flag == 1 and drate ==1 :
                                freq_offset_index = abs(freq_interfere_offset/2)
                            else:
                                freq_offset_index = abs(freq_interfere_offset)
                            Ratio_limit = CI_ratio_vs_data_rate[cur_rate][abs(freq_offset_index)]
                            pwr_interfere_org = pwr_interfere_vs_data_rate[cur_rate][abs(freq_offset_index)]

                        else :
                            Ratio_limit = CI_ratio_vs_data_rate[cur_rate][3]
                            pwr_interfere_org = pwr_interfere_vs_data_rate[cur_rate][3]

                        if freq_interfere_offset == freq_image:
                            Ratio_limit = CI_ratio_vs_data_rate[cur_rate][4]
                            pwr_interfere_org = pwr_interfere_vs_data_rate[cur_rate][4]

                        if (freq_interfere_offset == (freq_image + freq_image_offset)) or (freq_interfere_offset == (freq_image - freq_image_offset)):
                            Ratio_limit = CI_ratio_vs_data_rate[cur_rate][5]
                            pwr_interfere_org = pwr_interfere_vs_data_rate[cur_rate][5]

                        freq_interfere = freq_interfere_offset + freq_signal

                        if abs(freq_interfere_offset) <= 5:
                            pwr_signal_min=pwr_signal_vs_data_rate[cur_rate][abs(freq_interfere_offset)]
                            pwr_signal_max=pwr_signal_vs_data_rate[cur_rate][abs(freq_interfere_offset)]
                        else:
                            pwr_signal_min=pwr_signal_vs_data_rate[cur_rate][3]
                            pwr_signal_max=pwr_signal_vs_data_rate[cur_rate][3]
                        pwr_signal = pwr_signal_min

                        while pwr_signal <= pwr_signal_max:

                            start_pwr_interfere = pwr_interfere_org + 20
                            stop_pwr_interfere = pwr_interfere_org - 30

                            loginfo("start_pwr_interfere=%d,stop_pwr_interfere=%d,pwr_signal_min=%d,pwr_signal_max=%d,freq_signal=%d,freq_interfere=%d"%(start_pwr_interfere,stop_pwr_interfere,pwr_signal_min,pwr_signal_max,freq_signal,freq_interfere))
                            name_str = 'freq_signal_%s_freq_offset_interfere_%s_%s_%s_interferce_%s_%s'%(freq_signal,freq_interfere_offset, cur_rate, pwr_signal,start_pwr_interfere,stop_pwr_interfere)
                            fname = self.wifi.get_filename(self.folder,'bt_acpr_%s'%(name_str),'BT_ACPR')
                            title = 'freq_signal,pwr_signal,freq_offset_interfere,pwr_interfere,TX pac,RX pac,RX correct pac,PER,fail,AER, PER RX pac, RSSI, RX bits,RX err bit,BER,gain,inband\n'
                            fw2=csvreport(fname,title)
                            cur_sense_find=0

                            pwr_interfere = start_pwr_interfere
                            while pwr_interfere >= stop_pwr_interfere:

                                wt200_serv._connID = res_inf
                                self.interfer_test.iq_sigout(iq_interfere,freq_interfere,pwr_interfere,cable_lose_interfere,cur_rate[:-1]+'15_D100',0,iqv_interfere_no,0)

                                wt200_serv._connID = res_sig

                                if LE_flag ==1:
                                    [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, type_ep, len_ep, crc_ep,
                                    mic_ep, sn_ep, nesn_ep,time_ep,priv_ep,gainmax, gainmin, rssimax, rssimin]=self.bt_a2_test.rw_le_rx_per_test(framecnt=framecnt,ratename=cur_rate,rate=drate, pwrdBm=pwr_signal, freq=freq_signal, cable_loss=cable_lose_signal, iqv_no=iqv_signal_no, syncw=0x71764129,mytester =mytester)
                                    totalb = - 0.99
                                    cb_err = -0.99
                                    BER = -0.99
                                else:
                                    if drate >1 :
                                        edr = 1
                                    else:
                                        edr = 0
                                    [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, hec_ep, crc_ep, mic_ep,
                                    seq_ep, lt_ep, guard_ep, totalb, cb_err, BER]=self.bt_a2_test.rw_rx_per_test(framecnt=framecnt,edr=edr,ratename=cur_rate,pwrdBm=pwr_signal, freq=freq_signal, cable_loss=cable_lose_signal, iqv_no=iqv_signal_no,ulap=0x6BC6967e,ltaddr=0, mytester=mytester)

                                #self.interfer_test.iq_vsg_stop(iq_signal)
                                PER=1-(float(cp)/framecnt_est)
                                if LE_flag ==1:
                                    if PER >= per_limit or cp == 0:
                                        fail=1
                                    else:
                                        fail=0
                                else:
                                    if BER >= ber_limit[cur_rate] or  PER >= per_limit or cp == 0:
                                        fail=1
                                    else:
                                        fail=0
                                AER=1-(float(totalp)/framecnt_est)
                                PER_RX_pac=1

                                if totalp != 0:
                                    PER_RX_pac=1-(float(cp)/totalp)

                                fw2.write_data([freq_signal,pwr_signal,freq_interfere_offset,pwr_interfere,framecnt_est,totalp,cp,PER,fail,AER,PER_RX_pac,RSSI,totalb, cb_err, BER, gain,pwr_ib],float_num=4)

                                if  cur_sense_find == 0:
                                    res_lst = [freq_signal,pwr_signal,freq_interfere_offset,pwr_interfere,RSSI,PER*100,BER*100]
                                    if LE_flag == 1:
                                        if PER < per_limit and cp > 0:
                                            cur_sense_find = 1
                                        else:
                                            cur_sense_find = 0
                                    else:
                                        if BER < ber_limit[cur_rate] and PER < per_limit and cp > 0:
                                            cur_sense_find = 1
                                        else:
                                            cur_sense_find = 0
                                if fail == 0:
                                    break

                                pwr_interfere=pwr_interfere-pwr_interfere_step

                            fw1.write_data([cur_rate,res_lst[0],res_lst[1],res_lst[2],res_lst[3],res_lst[4],cur_sense_find,res_lst[5],res_lst[6],Ratio_limit,(res_lst[1]-res_lst[3]),Ratio_limit-(res_lst[1]-res_lst[3])],float_num=4)
                            pwr_signal = pwr_signal + pwr_signal_step
                            self.interfer_test.iq_vsg_stop(iq_interfere)
                        self.interfer_test.iq_vsg_stop(iq_signal)
        if iq_signal == 'iqview':
            mytester.gen_switch('OFF',iqv_signal_no)
        else:
            self.interfer_test.iq_close(iq_signal)
        self.interfer_test.iq_close(iq_interfere)


    def bt_acpr_force_gain(self,iq_signal='wt208c',iq_interfere='iqxel', lost_list=[8,6.3], pwr_interfere_step=1, pwr_signal_step=1, iqv_signal_no=1,iqv_interfere_no=1,Module_Name='ESP32_Testboard',Module_Num=''):

        '''
        iq_signal='iqxel' and iq_interfere='wt200': iqxel is signal source, wt200 is interfere source

        '''
        logsetlevel("D")
        fname = self.wifi.get_filename(self.folder,'bt_acpr_force_gain','BT_ACPR_FORCE_GAIN')
        title = 'rate, rx_freq, sens, freq_interfere,pwr_interfere,sens_rssi, sens_find, PER, BER,Ratio_limit,ratio\n'
        fw1=csvreport(fname,title)

        cable_lose_signal = lost_list[0]
        cable_lose_interfere = lost_list[1]

        #data_rate = ['LE_1M_prbs9']
        data_rate = ['1M_DH5_prbs9','2M_DH5_prbs9','3M_DH5_prbs9']
        freq_signal_list = [2441]
        #freq_signal_list = [2405,2441,2477] #LE : [2406,2442,2478]
        freq_image = 4
        framecnt  = 1500
        framecnt_est = framecnt
        per_limit  = 0.308
        ber_limit ={
        '1M_DH5_prbs9' : 0.001,
        '2M_DH5_prbs9' : 0.0001,
        '3M_DH5_prbs9' : 0.0001
        }

        freq_signal_lst = []
        pwr_signal_lst = []
        freq_offset_interfere_lst = []
        pwr_interfere_lst = []
        senslst = []
        rssilst = []
        PERlst = []
        BERlst = []
        ratio_lst = []
        rfrx_m = [0x1b0,0x1c0,0x1d0,0x1e0,0x1f0] # [0x180,0x190,0x1a0,0x1b0,0x1c0,0x1d0,0x1e0,0x1f0]
        bbgain_m =[0x0,0x80,0x100,0x20,0xa0,0x120,0x30,0xb0,0x130,0x38,0xb8]

        # wanted signal
        if iq_signal == 'iqview':
            mytester=tester.tester(2402,-40,'LE_1M_prbs9',1,iqv_signal_no,'source',cable_lose_signal,isreset=1)
            res_sig = -99
        else:
            res_sig = self.interfer_test.iq_open(iq_signal)
            mytester = iq_signal
        # Interfering signal
        #res_inf = self.interfer_test.iq_open(iq_interfere)

        sig_freq_l = len(freq_signal_list)

        for cur_rate in data_rate:
            [LE_flag,drate,DH,dtype] = bt_instrum.name2rate(cur_rate)
            if LE_flag == 1 and drate ==1 :
                freq_image_offset = 2
            else:
                freq_image_offset = 1

            for j in range(0,sig_freq_l):
                freq_signal = freq_signal_list[j]
                if LE_flag == 1:
                    freq_signal = freq_signal + 1

                for freq_offset in range(10,11):

                    if freq_offset==0: num = 1
                    else: num = 1
                    for i in range(0,num):
                        if i == 0 :
                            freq_interfere_offset = freq_offset
                        else:
                            freq_interfere_offset= -freq_offset

                        if LE_flag == 1 and drate ==1 : # LE_2M, freq_offset * 2
                            freq_interfere_offset = freq_interfere_offset * 2

                        if abs(freq_interfere_offset) <= 3 or ( LE_flag == 1 and drate ==1 and (abs(freq_interfere_offset/2) <=3)):
                            if LE_flag == 1 and drate ==1 :
                                freq_offset_index = abs(freq_interfere_offset/2)
                            else:
                                freq_offset_index = abs(freq_interfere_offset)
                            Ratio_limit = CI_ratio_vs_data_rate[cur_rate][abs(freq_offset_index)]
                            pwr_interfere_org = pwr_interfere_vs_data_rate[cur_rate][abs(freq_offset_index)]
                        else :
                            Ratio_limit = CI_ratio_vs_data_rate[cur_rate][3]
                            pwr_interfere_org = pwr_interfere_vs_data_rate[cur_rate][3]

                        if freq_interfere_offset == freq_image:
                            Ratio_limit = CI_ratio_vs_data_rate[cur_rate][4]
                            pwr_interfere_org = pwr_interfere_vs_data_rate[cur_rate][4]

                        if (freq_interfere_offset == (freq_image + freq_image_offset)) or (freq_interfere_offset == (freq_image - freq_image_offset)):
                            Ratio_limit = CI_ratio_vs_data_rate[cur_rate][5]
                            pwr_interfere_org = pwr_interfere_vs_data_rate[cur_rate][5]

                        freq_interfere = freq_interfere_offset + freq_signal

                        name_str = 'freq_signal_%s_freq_offset_interfere_%s_%s_interferce_%s'%(freq_signal,freq_interfere_offset, cur_rate,pwr_interfere_org)
                        fname = self.wifi.get_filename(self.folder,'bt_acpr_%s'%(name_str),'BT_ACPR_FORCE_GAIN')
                        title = 'rfrx1,bb2,bb1,freq_signal,pwr_signal,freq_offset_interfere,pwr_interfere,TX pac,RX pac,RX correct pac,PER,fail,AER, PER RX pac, RSSI, RX bits,RX err bit,BER,gain\n'
                        fw2=csvreport(fname,title)

                        for  rfrx_gain in rfrx_m:
                            for fine in range(0,16,2):
                                rfrx = rfrx_gain+fine
                                for bb_gain in bbgain_m:

                                    self.wifi.pbus_set_rx(pbusmode_en=1, rfrx1=rfrx, bb_gain=bb_gain, filter_atten=0,bt_mode=1)

                                    [rfrx1, rftx1, rftx2, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2] = self.pbus.all_pbus()


                                    if abs(freq_interfere_offset) <= 5:
                                        pwr_signal_min=pwr_signal_vs_data_rate[cur_rate][abs(freq_interfere_offset)]
                                        pwr_signal_max=pwr_signal_vs_data_rate[cur_rate][abs(freq_interfere_offset)]
                                    else:
                                        pwr_signal_min=pwr_signal_vs_data_rate[cur_rate][3]
                                        pwr_signal_max=pwr_signal_vs_data_rate[cur_rate][3]
                                    pwr_signal = pwr_signal_min

                                    while pwr_signal <= pwr_signal_max:

                                        start_pwr_interfere = pwr_interfere_org - 0
                                        stop_pwr_interfere = pwr_interfere_org + 0
                                        pwr_interfere = start_pwr_interfere
                                        cur_sense_find=0

                                        while pwr_interfere <= stop_pwr_interfere:

                                            #wt200_serv._connID = res_inf
                                            #self.interfer_test.iq_sigout(iq_interfere,freq_interfere,pwr_interfere,cable_lose_interfere,cur_rate[:-1]+'15_D100',0,iqv_interfere_no,0)
                                            wt200_serv._connID = res_sig

                                            if LE_flag ==1:
                                                [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, type_ep, len_ep, crc_ep,
                                                mic_ep, sn_ep, nesn_ep,time_ep,priv_ep,gainmax, gainmin, rssimax, rssimin]=self.bt_a2_test.rw_le_rx_per_test(framecnt=framecnt,ratename=cur_rate,pwrdBm=pwr_signal, freq=freq_signal, cable_loss=cable_lose_signal, iqv_no=iqv_signal_no, syncw=0x71764129,mytester =mytester)
                                                totalb = - 0.99
                                                cb_err = -0.99
                                                BER = -0.99
                                            else:
                                                if drate >1 :
                                                    edr = 1
                                                else:
                                                    edr = 0
                                                [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, hec_ep, crc_ep, mic_ep,
                                                seq_ep, lt_ep, guard_ep, totalb, cb_err, BER]=self.bt_a2_test.rw_rx_per_test(framecnt=framecnt,edr=edr,ratename=cur_rate,pwrdBm=pwr_signal, freq=freq_signal, cable_loss=cable_lose_signal, iqv_no=iqv_signal_no,ulap=0x6BC6967e,ltaddr=0, mytester=mytester)

                                            #self.interfer_test.iq_vsg_stop(iq_signal)
                                            PER=1-(float(cp)/framecnt_est)
                                            if LE_flag ==1:
                                                if PER >= per_limit or cp == 0:
                                                    fail=1
                                                else:
                                                    fail=0
                                            else:
                                                if BER >= ber_limit[cur_rate] or cp == 0:
                                                    fail=1
                                                else:
                                                    fail=0
                                            AER=1-(float(totalp)/framecnt_est)
                                            PER_RX_pac=1

                                            if totalp != 0:
                                                PER_RX_pac=1-(float(cp)/totalp)

                                            fw2.write_data([hex(rfrx1),hex(bb2),hex(bb1),freq_signal,pwr_signal,freq_interfere_offset,pwr_interfere,framecnt_est,totalp,cp,PER,fail,AER,PER_RX_pac,RSSI,totalb, cb_err, BER, gain,dcoi1, dcoq1, dcoi2, dcoq2],float_num=4)

                                            if  cur_sense_find == 0:
                                                res_lst = [freq_signal,pwr_signal,freq_interfere_offset,pwr_interfere,RSSI,PER*100,BER*100]
                                                if LE_flag == 1:
                                                    if PER < per_limit and cp > 0:
                                                        cur_sense_find = 1
                                                    else:
                                                        cur_sense_find = 0
                                                else:
                                                    if BER < ber_limit[cur_rate] and cp > 0:
                                                        cur_sense_find = 1
                                                    else:
                                                        cur_sense_find = 0

                                            pwr_interfere=pwr_interfere+pwr_interfere_step

                                        fw1.write_data([cur_rate,res_lst[0],res_lst[1],res_lst[2],res_lst[3],res_lst[4],cur_sense_find,res_lst[5],res_lst[6],Ratio_limit,(res_lst[1]-res_lst[3])],float_num=4)
                                        pwr_signal = pwr_signal + pwr_signal_step
                                        #self.interfer_test.iq_vsg_stop(iq_interfere)
                                    self.interfer_test.iq_vsg_stop(iq_signal)
        self.wifi.pbus_set_rx(pbusmode_en=0, rfrx1=0x184, bb_gain=0, filter_atten=0,bt_mode=0)
        if iq_signal == 'iqview':
            mytester.gen_switch('OFF',iqv_signal_no)
        else:
            self.interfer_test.iq_close(iq_signal)
        #self.interfer_test.iq_close(iq_interfere)


    def rx_gain_saturation_test(self, iq_signal='wt200',iq_interfere='wt208c',lost_list=[6.3,8], freq_sig=2404, rxgain_start=6,ragain_end=70, iqv_signal_no=1,iqv_interfere_no=1,name_str=''):

        title = 'pwr_signal,freq_sig,pwr_interfere,freq_interfer,lna_sat, vga_sat,rfrx1,bb2,bb1\n'
        fname = self.wifi.get_filename(self.folder, 'rx_gain_saturation_test_%d_%s'%(freq_sig, name_str))
        fw1=csvreport(fname, title)
        cable_lose_signal = lost_list[0]
        cable_lose_interfere = lost_list[1]

        pwr_signal=-67
        cur_rate = 'LE_1M_prbs9'
        freq_interfere_offset = -3
        freq_interfere = freq_sig+freq_interfere_offset

        res_sig = self.interfer_test.iq_open(iq_signal)
        res_inf = self.interfer_test.iq_open(iq_interfere)

        wt200_serv._connID = res_sig
        self.interfer_test.iq_sigout(iq_signal,freq_sig,pwr_signal,cable_lose_signal,cur_rate,0,iqv_signal_no,0)

        for rfrx,bb_gain in [[0x1cc,0x30]]:
            print rfrx,bb_gain
            self.wifi.pbus_set_rx(pbusmode_en=1, rfrx1=rfrx, bb_gain=bb_gain, filter_atten=3,bt_mode=1)
            for pwr_interfere in range(-40,-42,-2):
                wt200_serv._connID = res_inf
                self.interfer_test.iq_sigout(iq_interfere,freq_interfere,pwr_interfere,cable_lose_interfere,cur_rate[:-1]+'15_D100',0,iqv_interfere_no,0)
                self.wifiapi.phy_set_freq(2406)
                res=self.adc_dump.adcdumptest(logdir='dump',dump_num=10000,trig_mode='sw',adc_version="10bit",sample_80m=1,plot_en=1,chan_en=0,chan=freq_sig,force_gain_en=0,force_gain=0)
                vga_sat=res[6]
                lna_sat=res[5]
                [rfrx1, rftx1, rftx2, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2] = self.pbus.all_pbus()
                fw1.write_data([pwr_signal,freq_sig,pwr_interfere,freq_interfere,lna_sat,vga_sat,hex(rfrx1), hex(bb2), hex(bb1)])
                if vga_sat==0 and lna_sat==0:
                    break
        self.wifi.pbus_set_rx(pbusmode_en=0, rfrx1=0x184, bb_gain=0, filter_atten=0,bt_mode=0)
        self.interfer_test.iq_close(iq_signal)
        self.interfer_test.iq_close(iq_interfere)


    def bt_intermodulation_test(self, iq_signal='wt200',iq_interfere='wt208c',lost_list=[6.3,8],  iqv_signal_no=1,iqv_interfere_no=1,name_str=''):

        '''
        iq_signal='iqxel' and iq_interfere='wt200': iqxel is signal source, wt200 is interfere source

        '''
        logsetlevel("D")
        fname = self.wifi.get_filename(self.folder,'bt_intermodulation_test','BT_intermodulation')
        title = 'rate, rx_freq, sens, freq_interfere,pwr_interfere,sens_rssi, sens_find, PER, BER,Ratio_limit,ratio\n'
        fw1=csvreport(fname,title)

        cable_lose_signal = lost_list[0]
        cable_lose_interfere1 = lost_list[1]
        cable_lose_interfere2 = lost_list[2]
        data_rate = ['LE_1M_prbs9'] #['LE_1M_prbs9','LE_2M_prbs9','LE_125K_prbs9','LE_500K_prbs9']
        data_rate = ['1M_DH5_prbs9','2M_DH5_prbs9','3M_DH5_prbs9']
        freq_signal_list = [2441]
        #freq_signal_list = [2405,2441,2477]  #   freq_signal + 1 ,LE : [2406,2442,2478]
        framecnt  = 1500
        framecnt_est = framecnt
        per_limit  = 0.308
        ber_limit ={
        '1M_DH5_prbs9' : 0.001,
        '2M_DH5_prbs9' : 0.0001,
        '3M_DH5_prbs9' : 0.0001
        }

        freq_signal_lst = []
        pwr_signal_lst = []
        freq_offset_interfere_lst = []
        pwr_interfere_lst = []
        senslst = []
        rssilst = []
        PERlst = []
        BERlst = []
        ratio_lst = []

        # wanted signal
        res_sig = self.interfer_test.iq_open(iq_signal)
        mytester = iq_signal
        # Interfering signal
        res_inf = self.interfer_test.iq_open(iq_interfere)
        # Interfering signal
        mysig_gen = sme.sme();# signal generator!

        pwr1_interfere = -50  # IQV
        pwr2_interfere = -50  # SME

        for cur_rate in data_rate:

            [LE_flag,drate,DH,dtype] = bt_instrum.name2rate(cur_rate)
            for freq_signal in freq_signal_list:

                for freq_offset in range(3,6):

                    for i in range(0,2):
                        if i == 0 :
                            n = freq_offset
                        else:
                            n= -freq_offset

                    f1_interfere = freq_signal - n
                    f2_interfere = freq_signal - 2*n

                    wt200_serv._connID = res_inf
                    self.interfer_test.iq_sigout(iq_interfere,f1_interfere,pwr1_interfere,cable_lose_interfere1,cur_rate[:-1]+'15_D100',0,iqv_interfere_no,0)
                    mysig_gen.setfreq(f2_interfere*1e6)
                    mysig_gen.setpow(pwr2_interfere+cable_lose_interfere2)
                    mysig_gen.rfon();

                    pwr_signal = -64
                    pwr_signal_min = pwr_signal - 10
                    pwr_signal_max = pwr_signal + 10
                    pwr_signal = pwr_signal_min
                    loginfo("freq_signal=%d,f1_interfere=%d,f2_interfere=%d,pwr_signal=%d,pwr1_interfere=%d,pwr2_interfere=%d"%(freq_signal,f1_interfere,f2_interfere,pwr_signal,pwr1_interfere,pwr2_interfere))

                    name_str = '%s_freq_signal_%s_freq_interfere_%s_%s_signal_pwr_%s_interferce_%s_%s'%(cur_rate,freq_signal,f1_interfere, f2_interfere, pwr_signal_min, pwr_signal_max,pwr_interfere)
                    fname = self.wifi.get_filename(self.folder,'bt_intermodulation_test_%s'%(name_str),'BT_intermodulation')
                    title = 'cur_rate,freq_signal,f1_interfere,f2_interfere,pwr_signal,pwr1_interfere,pwr2_interfere,TX pac,RX pac,RX correct pac,PER,fail,AER, PER RX pac, RSSI, RX bits,RX err bit,BER,gain\n'
                    fw2=csvreport(fname,title)
                    cur_sense_find=0

                    wt200_serv._connID = res_sig
                    while pwr_signal <= pwr_signal_max:

                        if LE_flag ==1:
                            [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, type_ep, len_ep, crc_ep,
                            mic_ep, sn_ep, nesn_ep,time_ep,priv_ep,gainmax, gainmin, rssimax, rssimin]=self.bt_a2_test.rw_le_rx_per_test(framecnt=framecnt,ratename=cur_rate,rate=drate, pwrdBm=pwr_signal, freq=freq_signal, cable_loss=cable_lose_signal, iqv_no=iqv_signal_no, syncw=0x71764129,mytester =mytester)
                            totalb = - 0.99
                            cb_err = -0.99
                            BER = -0.99
                        else:
                            if drate >1 :
                                edr = 1
                            else:
                                edr = 0
                            [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, hec_ep, crc_ep, mic_ep,
                            seq_ep, lt_ep, guard_ep, totalb, cb_err, BER]=self.bt_a2_test.rw_rx_per_test(framecnt=framecnt,edr=edr,ratename=cur_rate,pwrdBm=pwr_signal, freq=freq_signal, cable_loss=cable_lose_signal, iqv_no=iqv_signal_no,ulap=0x6BC6967e,ltaddr=0, mytester=mytester)

                        PER=1-(float(cp)/framecnt_est)
                        if LE_flag ==1:
                            if PER >= per_limit or cp == 0:
                                fail=1
                            else:
                                fail=0
                        else:
                            if BER >= ber_limit[cur_rate] or cp == 0:
                                fail=1
                            else:
                                fail=0
                        AER=1-(float(totalp)/framecnt_est)
                        PER_RX_pac=1

                        if totalp != 0:
                            PER_RX_pac=1-(float(cp)/totalp)

                        fw2.write_data([freq_signal,pwr_signal,freq_interfere_offset,pwr_interfere,framecnt_est,totalp,cp,PER,fail,AER,PER_RX_pac,RSSI,totalb, cb_err, BER, gain],float_num=4)

                        if  cur_sense_find == 0:
                            res_lst = [freq_signal,f1_interfere,f2_interfere,pwr_signal,pwr1_interfere,pwr2_interfere,RSSI,PER*100,BER*100]
                            if LE_flag == 1:
                                if PER < per_limit and cp > 0:
                                    cur_sense_find = 1
                                else:
                                    cur_sense_find = 0
                            else:
                                if BER < ber_limit[cur_rate] and cp > 0:
                                    cur_sense_find = 1
                                else:
                                    cur_sense_find = 0

                        pwr_signal = pwr_signal + pwr_signal_step

                    fw1.write_data([cur_rate,res_lst[0],res_lst[1],res_lst[2],res_lst[3],res_lst[4],res_lst[5],cur_sense_find,res_lst[6],res_lst[7],res_lst[8]],float_num=4)
                    pwr_interfere=pwr_interfere+pwr_interfere_step
                    self.interfer_test.iq_vsg_stop(iq_signal)
                self.interfer_test.iq_vsg_stop(iq_interfere)
                self.interfer_test.iq_close(iq_signal)
                self.interfer_test.iq_close(iq_interfere)

