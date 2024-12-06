import time
import re
import csv
import os, sys
import matplotlib.pyplot as plt
import pylab
import xlrd
import numpy as np
import pandas
from rftest.rflib.utility import mfunc
from baselib.instrument import dm,tester,eps
from baselib.instrument.spa import HP,Agilent
from rftest.rflib.wifi_lib import WIFILIB
from hal.Init import HALS
from hal.common import MEM
from hal.wifi_api import WIFIAPI
from rftest.rflib.pbus import pbus
from rftest.rflib.rfpll import rfpll
from rftest.rflib.rfcal import rfcal
import rftest.rflib.rfglobal as rfglobal
import rftest.rflib.wifi_instrum as wifi_instrum
from rftest.rflib.saradc import SARADC
from rftest.testcase.rf_debug.tx_gain_sweep import Sweep_TX_Gain
from rftest.rflib.csv_report import csvreport
from baselib.loglib.log_lib import *

class PA_OutPwr(object):

    def __init__(self,comport,chipv='ESP32'):

        self.comport = comport
        self.chipv = chipv
        self.wifiapi = WIFIAPI(self.comport,self.chipv)
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.mem = MEM(self.comport, self.chipv)
        self.pbus = pbus(self.comport, self.chipv)
        self.rfcal = rfcal(self.comport, self.chipv)
        self.rfpll = rfpll(self.comport, self.chipv)
        self.hals = HALS(self.comport,self.chipv)
        self.saradc = SARADC(self.comport,self.chipv)
        self.sweep_tx_gain = Sweep_TX_Gain(self.comport,self.chipv)
        self.curr_data_path = 'D:/chip/eagletest/py_script/rftest/rfdata/pa_outpwr_data/'

#********************************************************
#*******************TX setting***************************
#********************************************************
    def TX_init(self,PLL_freq=2484,XTAL_freq=40,Gain_Filter=0x120,Gain_PA=0x5f):

        if self.chipv == "CHIP723" or self.chipv == "CHIP724":
            self.wifiapi.phy_set_freq(freq=PLL_freq, freq_offset=0)
        else:
            self.rfpll.set_freq(PLL_freq,XTAL_freq)
        self.pbus.pbus_debugmode()
        self.pbus.open_tx(Gain_PA,Gain_Filter)
        self.rfcal.tos()
        self.wifi.force_txon(1)


    def creat_csv(self,csv_name='TX_Out_Power_Test',data_path='',Board_Num='',csv_header=[],sweep_list1=[],sweep_list2=[]):

        Test_state = 'This Test was developed for %s'%(csv_name)
        filetime = time.strftime('_%Y%m%d_%H%M%S',time.localtime(time.time()));
        folder = data_path + '%s_%s_%s_%s'%(csv_name, Board_Num, self.wifi.read_mac(),filetime);
        data_path = folder +'/'
        os.mkdir(folder)
        output_file = open(data_path +'/'+'%s_%s_%s_%s.csv'%(csv_name,Board_Num,self.wifi.read_mac(), filetime), 'ab+');
        csv.writer(output_file).writerow(['Test Introduction : %s'%Test_state]);

        for header1 in  sweep_list1:
            [block,ctrl_name,sweep_start,sweep_stop,sweep_step]=self.get_sweep_cmd(header1);
            csv_header.append(ctrl_name);

        for header2 in  sweep_list2:
            [block,ctrl_name,sweep_start,sweep_stop,sweep_step]=self.get_sweep_cmd(header2);
            csv_header.append(ctrl_name);

        csv.writer(output_file).writerow(csv_header);

        return [data_path,output_file,filetime]

    def i2c_table2list(self,sheetnamelist=['rftx'],step_auto=0,i2c_table=''):

        workbook=xlrd.open_workbook(i2c_table)
        if sheetnamelist ==[]:
            sheetnamelist=workbook.sheet_names()
        sweep_list = []
        for sname in sheetnamelist:
            block=sname.encode('utf-8')
            i2c_regdict =pandas.read_excel(i2c_table,sheetname=block)

            for index in i2c_regdict.index:
                addr=i2c_regdict.loc[index]["#addr"]
                msb=i2c_regdict.loc[index]["msb"]
                lsb=i2c_regdict.loc[index]["lsb"]
                ctrl_name=i2c_regdict.loc[index]["ctrl_name"].split("[")[0]
                data_max = 2**(msb-lsb+1)
                if step_auto == 1:
                    step = int((data_max-1)/8)+1
                else:
                    step = 1
                sweep_list.append([block,ctrl_name,'0:%d:%d'%(step,data_max)])

        return sweep_list


    def get_sweep_cmd(self,cmd_list=['rftx','PA_VCT_CSC_STG0','0:2:14']):
        if cmd_list[2].find(':') != -1:
            sweep_param = cmd_list[2].split(':')
            return [cmd_list[0], cmd_list[1], int(sweep_param[0]), int(sweep_param[2]), int(sweep_param[1])]



    def IM3_test(self,chan=1, rate='mcs0'):

        IM3_tone1_freq   = 1;
        IM3_tone2_freq   = 17;

        title = 'IM3_%s MHz, Tone1_%s MHz,Tone2_%s MHz, IM3_%s MHz, freq_sweep, power_sweep\n'%((2*IM3_tone1_freq-IM3_tone2_freq),(IM3_tone1_freq),(IM3_tone2_freq),(2*IM3_tone2_freq-IM3_tone1_freq))

        fname = self.wifi.get_filename('IM3_test', 'IM3_tests')
        csvreport1 = csvreport(fname, title)

        gain_filter = 0x120;
        gain_pa     = 0x5f;
        device_spa ="N9020A"
        cable_lose_spa = 1.5

        self.wifi.cmdstop()
        cbw40m = self.wifi.rate2ht40(rate)
        self.wifi.rfchsel(chan,cbw40m*2)
        freq_sweep = self.wifi.chan2freq(chan)
        self.pbus.pbus_debugmode()
        self.pbus.open_tx(gain_pa,gain_filter)
##        self.wifi.i2c_wic('bbtop','filter_wifitx_dcap_lq',32)
##        self.wifi.i2c_wic('bbtop','filter_wifitx_dcap_hq',33)
        self.rfcal.tos()
        self.wifi.force_txon(1)
        if self.chipv =="CHIP722":
            self.sweep_tx_gain.better_reg_set()

        if device_spa =="":
            self.spa = HP('SA',cfreq=freq_sweep,rb=30,span=5,reflvl=20);#rb and span
            SPA_Revise_Power = 2
        else:
            self.spa = Agilent('SA',cfreq=freq_sweep,rb=30,span=5,reflvl=20,device=device_spa);#rb and span
            SPA_Revise_Power = 0.2
        self.spa.set_rb(1000)
        self.spa.set_vb(3000)

        for power_sweep in range(100,20,-4):

            self.spa.set_reflvl(20);
            self.wifi.txtone(1, IM3_tone1_freq, power_sweep, 1, IM3_tone2_freq, power_sweep);
            self.wifiapi.pll_cap_track_en(1)
            self.spa.set_cfreq(cfreq=freq_sweep+IM3_tone1_freq);
            self.spa.trace_maxhold(1)
            time.sleep(1)
            Power_Tone1=self.spa.get_result('PEAK')[1]+SPA_Revise_Power+cable_lose_spa;

            self.spa.set_cfreq(cfreq=freq_sweep+IM3_tone2_freq);
            self.spa.trace_maxhold(1)
            time.sleep(1)
            Power_Tone2=self.spa.get_result('PEAK')[1]+SPA_Revise_Power+cable_lose_spa;


            self.spa.set_cfreq(cfreq=freq_sweep+2*IM3_tone1_freq-IM3_tone2_freq);
            if power_sweep > 80:
                self.spa.set_reflvl(-10)
            else:
                self.spa.set_reflvl(0)
            self.spa.trace_maxhold(1)
            time.sleep(1)
            Power_IM3_N=self.spa.get_result('PEAK')[1]+SPA_Revise_Power+cable_lose_spa;

            self.spa.set_cfreq(cfreq=freq_sweep+2*IM3_tone2_freq-IM3_tone1_freq);
            self.spa.trace_maxhold(1)
            time.sleep(1)
            Power_IM3_P=self.spa.get_result('PEAK')[1]+SPA_Revise_Power+cable_lose_spa;

            self.wifi.txtone(0, IM3_tone1_freq, power_sweep, 1, IM3_tone2_freq, power_sweep);

            csv_row=[ Power_IM3_N, Power_Tone1, Power_Tone2, Power_IM3_P, freq_sweep, power_sweep];
            logdebug(Power_IM3_N, Power_Tone1, Power_Tone2, Power_IM3_P)

            csvreport1.write_data(csv_row)



#********************************************************
#********************TX TEST************************
#********************************************************
    def PA_Test_case(self,element=0,cable_lose=0,iqv_no=0,Board_Num=''):

        sweep_list=[
        ['SA_set_cfreq','SA_set_cfreq','2412:40:2452'],# Change cfreq
        ['txtone_backoff','txtone_backoff','-60:2:10']  #
        ]

        sweep_list_i2c = [
##            ['rfpll','lf_hbw','1:1:1'],
##            ['rftx','PA2G_ICT_STG1','6:2:8']
##            ['rfpll','ir_dac_ext','12:-2:7'],
##            ['rfpll','ir_ext_dchgp', '0:4:8'],
##            ['rfpll','or_dvco_kvco', '0:2:4'],
##            ['rfpll','dlref','0:2:4'],
##            ['rfpll','dhref','0:2:4'],
##            ['rfpll','ir_amplf_close','0:4:16'],
##            ['rfpll','ir_amplf_open', '0:4:16'],
##            ['xtal','xtal_dphase','0:1:2'],
        ]
###CHIP722B23_modboard
##        match_dict={
##            '0' : 'None',
##            '1' : '2.0-1.5-3.3=19+j8',
##            '2' : '1.2-2.0-2.7=20.3-2.1',
##            '3' : '2.0-1.5-3.0=21.6+7.7',
##            '4' : '2.4-1.5-3.3=23-1j',
##            '5' : '2.7-1.2-3.3=25+13',
##            '6' : '1.2-2.2-2.4=26-j4',
##            '7' : '1.2-2.0-2.4=26-j4',
##            '8' : '1.5-1.5-2.2=27+10j',
##            '9' : '2.7-1.5-3.3=27-j4.3',
##            '10' : '2.0-1.5-2.7=28+j10',
##            '11' : '2.4-1.5-3.0=29+j3',
##            '12' : '3.0-1.5-3.3=29-j8',
##            '13' : '2.7-1.2-2.7=30+j12',
##            '14' : '2.0-1.8-2.7=33+j0',
##            '15' : '2.4-2.0-2.7=33-j15',
##            '16' : '2.2-1.5-2.7=33.6+j12',
##            '17' : '11.5-1.8-2.2=34+j5',
##            '18' : '1.5-2.0-2.2 =35+j1',
##            '19' : '2.7-1.5-2.7=35-j6',
##            '20' : '3.0-1.2-2.7=36+j11',
##            '21' : '2.2-1.8-2.7=38-j3',
##            '22' : '2.0-1.8-2.4=41+j5',
##            '23' : '1.8-2.0-2.2=41-j1',
##            '24' : '2.7-1.8-2.7=44-10',
##            '25' : '2.2-1.8-2.4=46.3+j3',
##            '26' : '2.0-2.0-2.2=47-j2',
##            '27' : '2.2-1.8-2.2=49+j9',
##            }
###CHIP723_modboard_v1.6
##        match_dict={
##            '0' : 'None',
##            '1' : '2.0-1.5-2.7=33+j4',
##            '2' : '2.0-2.0-2.7=33-j9',
##            '3' : '1.2-2.7-2.0=32-j10',
##            '4' : '1.2-2.4-2.0=34-j4',
##            '5' : '1.8-1.8-2.4=35+j10',
##            '6' : '1.5-2.7-2.0=36-j13',
##            '7' : '1.5-1.8-2.4=30+j10',
##            '8' : '1.5-2.2-2.4=30-j0',
##            '9' : '1.5-2.4-2.4=30-j4',
##            '10': '1.8-2.0-2.7=29-j0',
##            '11': '1.5-2.7-2.2=29-j11',
##            '12': '2.0-1.5-2.7=29+j15',
##            '13': '2.2-1.8-2.7=38+j0',
##            '14': '2.4-1.8-2.7=40+j3',
##            '15': '1.5-2.4-2.0=42-j5',
##            '16': '2.7-1.8-2.7=46-j5',
##            '17': '1.5-2.4-1.8=50-j1',
##            '18': '2.0-2.2-2.7=26-j6',
##            '19': '1.5-1.8-2.7=24+j7',
##            '20': '1.2-2.7-2.4=22-j7',
##
##            }
#CHIP723_TestBoard_v1.2
        match_dict={
            '0' : 'None',
            '1' : '2.4-1.8-3.0=34+j7',
            '2' : '2.2-2.2-2.7=34-j10',
            '3' : '2.4-2.0-2.7=35-j3',
            '4' : '2.4-1.8-2.7=37+j8',
            '5' : '2.0-2.0-2.7=39-0j',
            '6' : '2.2-2.0-2.7=41-j0',
            '7' : '2.7-1.8-3.0=44+j3',
            '8' : '2.0-2.2-2.4=49+j1',
            '9' : '2.0-2.2-2.7=33-j10',
            '10': '2.0-2.0-3.0=31-j2',
            '11': '2.7-1.6-3.3=30+j8',
            '12': '3.0-1.6-3.3=29+j6',
            '33': '2.0-2.2-3.0=26-j9',
            '14': '2.2-1.8-3.3=24+j4',
            '38': '2.0-1.8-3.3=21+j2',
            '22': '2.7-1.6-3.3=30+j8',
            '27': '2.0-1.6-3.3=29+j6',
            '18': '2.0-2.2-2.4=49+j1',
            }

        pll_freq         = 2412;
        tone_freq        = 1;
        IM3_Tone1_freq   = 5;
        IM3_Tone2_freq   = 8;
        gain_filter = 0x20;
        gain_pa     = 0x4f;
        spa_rb      =3;
        vol_en = 0,
        temp = 25

        chan = 1
        curr_en = 0
        EVM_en = 0
        MASK_en = 0
        cable_lose_spa = cable_lose
        cable_lose_instr = cable_lose


        device_spa = "N9020A" #"E4404B","N9020A"
        if device_spa =="":
            SPA_Revise_Power = 0.2; #HP lose:2dB
        else:
            SPA_Revise_Power = 0.2 ;

        TX_Init_Set=[Board_Num, pll_freq, tone_freq, IM3_Tone1_freq, IM3_Tone2_freq, SPA_Revise_Power, gain_filter, gain_pa, spa_rb, self.curr_data_path, device_spa, cable_lose_spa,cable_lose_instr];

        if element== 0:
            csv_name = 'TX_Out_Power_i2c_Test'
            self.TX_Out_Power_Test(TX_Init_Set, csv_name=csv_name,sweep_list1=sweep_list, sweep_list2=sweep_list_i2c,curr_en=curr_en);
        elif element== 1:
            csv_name = 'TX_Out_Power_sweep_rftx'
            sheetnamelist=['rftx']
            i2c_table =  self.curr_data_path+'/' +"chip724_sweep_i2c_reg_oktorun.xlsm"
            sweep_list_i2c = self.i2c_table2list(sheetnamelist=sheetnamelist,step_auto=1,i2c_table=i2c_table)
            TX_Init_Set[0] = Board_Num+str(sheetnamelist)
            self.TX_Out_Power_Test(TX_Init_Set, csv_name=csv_name,sweep_list1=sweep_list, sweep_list2=sweep_list_i2c,curr_en=curr_en);
        elif element == 2:
            csv_name = 'TX_P1dB_i2c_Test'
            sheetnamelist=['rftx']
            i2c_table =  self.curr_data_path+'/' +"chip724_sweep_i2c_reg_oktorun.xlsm"
            sweep_list_i2c = self.i2c_table2list(sheetnamelist=sheetnamelist,step_auto=1,i2c_table=i2c_table)
            self.TX_P1dB_Test(TX_Init_Set, csv_name=csv_name, sweep_list1=sweep_list, sweep_list2=sweep_list_i2c,curr_en=curr_en);
        elif element == 3:
            csv_name = 'TX_P1dB_Test_Matching'
            EVM_en = 0
            self.TX_P1dB_Test_Matching(TX_Init_Set, csv_name=csv_name, sweep_list1=sweep_list, sweep_list2=match_dict,curr_en=curr_en,chan=chan,EVM_en=EVM_en,iqv_no=iqv_no);
        elif element == 4:
            sweep_list=[
            ['SA_set_cfreq','SA_set_cfreq','2412:80:2484'],# Change cfreq
            ['txtone_backoff','txtone_backoff','-120:2:0']  #
            ]
            csv_name = 'TX_IM3_Test_Matching'
            MASK_en = 0
            self.TX_IM3_Test_Matching(TX_Init_Set, csv_name=csv_name, sweep_list1=sweep_list, sweep_list2=match_dict,chan=chan, MASK_en=MASK_en,iqv_no=iqv_no);

        elif element == 5:
            TX_Init_Set=[Board_Num, pll_freq, tone_freq, IM3_Tone1_freq, IM3_Tone2_freq, SPA_Revise_Power, gain_filter, gain_pa, spa_rb, self.curr_data_path, device_spa, cable_lose_spa,cable_lose_instr,vol_en,temp];
            csv_name = 'TX_P1dB_Debug_Test_Matching'
            self.TX_P1dB_Test_Matching_debug(TX_Init_Set, csv_name=csv_name, sweep_list1=sweep_list, sweep_list2=match_dict,curr_en=curr_en,chan=chan,EVM_en=EVM_en,iqv_no=iqv_no);

        elif element == 6:
            TX_Init_Set=[Board_Num, pll_freq, tone_freq, IM3_Tone1_freq, IM3_Tone2_freq, SPA_Revise_Power, gain_filter, gain_pa, spa_rb, self.curr_data_path, device_spa, cable_lose_spa,cable_lose_instr,vol_en,temp];
            csv_name = 'TX_IM3_Debug_Test_Matching'
            sweep_list=[
            ['SA_set_cfreq','SA_set_cfreq','2412:80:2484'],# Change cfreq
            ['txtone_backoff','txtone_backoff','-120:2:0']  #
            ]
            csv_name = 'TX_IM3_Test_Matching'
            self.TX_IM3_Test_Matching_debug(TX_Init_Set, csv_name=csv_name, sweep_list1=sweep_list, sweep_list2=match_dict,chan=chan, MASK_en=MASK_en,iqv_no=iqv_no);


    def TX_Out_Power_Test(self,  Init_Set, csv_name, sweep_list1, sweep_list2, curr_en):

        [Board_Num, pll_freq, tone_freq, IM3_Tone1_freq, IM3_Tone2_freq, SPA_Revise_Power, gain_filter, gain_pa, spa_rb, data_path, device_spa, cable_lose_spa, cable_lose_instr]=Init_Set;
        csv_header=['IDC_mA','SAR_PWR','SPA_PEAK'];
        [data_path,output_file,filetime] = self.creat_csv(csv_name=csv_name,data_path=data_path,Board_Num=Board_Num,csv_header=csv_header,sweep_list1=sweep_list1,sweep_list2=sweep_list2)

        if device_spa =="":
            self.spa = HP('SA',cfreq=pll_freq+tone_freq,rb=spa_rb,span=1,reflvl=20);#rb and span
        else:
            self.spa = Agilent('SA',cfreq=pll_freq+tone_freq,rb=spa_rb,span=1,reflvl=20,device=device_spa);#rb and span
        if curr_en == 1:
            mydm=dm.dm('34401A');

        # Creat Sweep Data Table
        cmd_list1=[];
        cmd_list2=[];
        reg_data=[];

        for list1 in  sweep_list1:
            cmd_list1.append(self.get_sweep_cmd(list1));

        for list2 in  sweep_list2:
            cmd_list2.append(self.get_sweep_cmd(list2));

        for kk0 in range(0, len(sweep_list2), 1):
            reg_data.append(self.wifi.i2c_ric(cmd_list2[kk0][0], cmd_list2[kk0][1]));

        self.TX_init(PLL_freq=pll_freq,XTAL_freq=40,Gain_Filter=gain_filter,Gain_PA=gain_pa);

        for i in range(0,len(sweep_list2),1):

            for kk1 in range(0, len(sweep_list2), 1):
                reg_data.append(self.wifi.i2c_wic(cmd_list2[kk1][0], cmd_list2[kk1][1], reg_data[kk1]));

            for freq_sweep in range(cmd_list1[0][2], cmd_list1[0][3], cmd_list1[0][4]):
                if self.chipv == "CHIP723" or self.chipv == "CHIP724":
                    self.wifiapi.phy_set_freq(freq=freq_sweep, freq_offset=0)
                else:
                    self.rfpll.set_freq(freq_sweep)
                if device_spa =="":
                    self.spa = HP('SA',cfreq=freq_sweep+tone_freq,rb=spa_rb,span=1,reflvl=25);#rb and span
                else:
                    self.spa = Agilent('SA',cfreq=freq_sweep+tone_freq,rb=spa_rb,span=1,reflvl=25,device=device_spa);
                self.spa.set_rb(30);
                data=[];
                data.append(csv_header);

                for loop_value in range(cmd_list2[i][2], cmd_list2[i][3], cmd_list2[i][4]):

                    self.wifi.i2c_wic(cmd_list2[i][0], cmd_list2[i][1], loop_value);

                    for power_sweep in range(cmd_list1[1][2], cmd_list1[1][3], cmd_list1[1][4]):

                        self.wifi.txtone(1, tone_freq, power_sweep)
##                        self.wifiapi.pll_cap_track_en(1)
                        time.sleep(1)
                        SPA_pwr = self.spa.get_result('PEAK')[1]+SPA_Revise_Power+cable_lose_spa
                        self.saradc.en_pwdet()
                        sarpwr= self.saradc.sar_dout(8, signal='tone', pwr_dis=0);
                        self.wifi.txtone(0, tone_freq, power_sweep)
                        if curr_en == 1:
                            IDC0 = int(abs(float(mydm.get_result('IDC'))*1000))
                        else:
                            IDC0 = 0
                        csv_row=[IDC0,sarpwr,SPA_pwr,freq_sweep, power_sweep]
                        for kk2 in range(0, len(sweep_list2), 1):
                            csv_row.append(self.wifi.i2c_ric(cmd_list2[kk2][0], cmd_list2[kk2][1]));
                        csv.writer(output_file).writerow(csv_row);
                        data.append(csv_row);
                        time.sleep(1)
                pylab.figure();
                [xlabel_name, ylabel_name, freq]=data_ananysis(data,xvalue='txtone_backoff',yvalue='SPA_PEAK',zvalue=cmd_list2[i][1],wvalue='PA_CCT_STG0_DRAIN',w_en=0, IM3_Test_Memu=['','','','']);
                Fig_Label(xlabel_name, ylabel_name, freq,'lower right');
                plt.savefig(data_path+'TX_Out_Power_Test_Power_%s_%s.png'%(cmd_list2[i][1],freq_sweep));
                plt.close()
                if curr_en == 1:
                    pylab.figure();
                    [xlabel_name, ylabel_name, freq]=data_ananysis(data,xvalue='txtone_backoff',yvalue='IDC_mA',zvalue=cmd_list2[i][1],wvalue='PA_CCT_STG0_DRAIN',w_en=0, IM3_Test_Memu=['','','','']);
                    Fig_Label(xlabel_name, ylabel_name, freq);
                    plt.savefig(data_path+'TX_Out_Power_Test_IDC0_%s_%s.png'%(cmd_list2[i][1],freq_sweep));
                    plt.close()

        output_file.close();


    def TX_P1dB_Test(self, Init_Set, csv_name, sweep_list1, sweep_list2, curr_en):

        [Board_Num, pll_freq, tone_freq, IM3_Tone1_freq, IM3_Tone2_freq, SPA_Revise_Power, gain_filter, gain_pa, spa_rb, data_path, device_spa, cable_lose_spa,cable_lose_instr]=Init_Set;

        csv_header=['IDC_mA','SAR_PWR','SPA_PEAK'];
        [data_path,output_file,filetime] = self.creat_csv(csv_name=csv_name,data_path=data_path,Board_Num=Board_Num,csv_header=csv_header,sweep_list1=sweep_list1,sweep_list2=sweep_list2)

        if device_spa =="":
            self.spa = HP('SA',cfreq=pll_freq+tone_freq,rb=spa_rb,span=1,reflvl=20);#rb and span
        else:
            self.spa = Agilent('SA',cfreq=pll_freq+tone_freq,rb=spa_rb,span=1,reflvl=20,device=device_spa);#rb and span
        if curr_en == 1:
            mydm=dm.dm('34401A');

        # Creat Sweep Data Table
        cmd_list1=[];
        cmd_list2=[];
        reg_data=[];

        for list1 in  sweep_list1:
            cmd_list1.append(self.get_sweep_cmd(list1));

        for list2 in  sweep_list2:
            cmd_list2.append(self.get_sweep_cmd(list2));

        for kk0 in range(0, len(sweep_list2), 1):
            reg_data.append(self.wifi.i2c_ric(cmd_list2[kk0][0], cmd_list2[kk0][1]));

        self.TX_init(PLL_freq=pll_freq,XTAL_freq=40,Gain_Filter=gain_filter,Gain_PA=gain_pa);

        for i in range(0,len(sweep_list2),1):

            for kk1 in range(0, len(sweep_list2), 1):
                reg_data.append(self.wifi.i2c_wic(cmd_list2[kk1][0], cmd_list2[kk1][1], reg_data[kk1]));

            for freq_sweep in range(cmd_list1[0][2], cmd_list1[0][3], cmd_list1[0][4]):

                if self.chipv == "CHIP723" or self.chipv == "CHIP724":
                    self.wifiapi.phy_set_freq(freq=freq_sweep, freq_offset=0)
                else:
                    self.rfpll.set_freq(freq_sweep)

                if device_spa =="":
                    self.spa = HP('SA',cfreq=freq_sweep+tone_freq,rb=spa_rb,span=1,reflvl=20);#rb and span
                else:
                    self.spa = Agilent('SA',cfreq=freq_sweep+tone_freq,rb=spa_rb,span=1,reflvl=20,device=device_spa);
                self.spa.set_rb(30);

                for loop_value in range(cmd_list2[i][2], cmd_list2[i][3], cmd_list2[i][4]):

                    self.wifi.i2c_wic(cmd_list2[i][0], cmd_list2[i][1], loop_value);
                    data=[];
                    data.append(csv_header);

                    for power_sweep in range(cmd_list1[1][2], cmd_list1[1][3], cmd_list1[1][4]):

                        self.wifi.txtone(1, tone_freq, power_sweep)
                        #self.wifiapi.pll_cap_track_en(1)
                        time.sleep(1)

                        SPA_pwr = self.spa.get_result('PEAK')[1]+SPA_Revise_Power+cable_lose_spa
                        #self.saradc.en_pwdet()
                        sarpwr=0 # self.saradc.sar_dout(8, signal='tone', pwr_dis=0);
                        self.wifi.txtone(0, tone_freq, power_sweep)
                        if curr_en == 1:
                            IDC0 = int(abs(float(mydm.get_result('IDC'))*1000))
                        else:
                            IDC0 = 0
                        csv_row=[IDC0,sarpwr,SPA_pwr,freq_sweep, power_sweep]
                        for kk2 in range(0, len(sweep_list2), 1):
                            csv_row.append(self.wifi.i2c_ric(cmd_list2[kk2][0], cmd_list2[kk2][1]));
                        csv.writer(output_file).writerow(csv_row)
                        data.append(csv_row)
                        time.sleep(5)
                    tone_step = cmd_list1[1][4]
                    pylab.figure()
                    [xlabel_name, ylabel_name, freq]=data_ananysis(data,xvalue='txtone_backoff',yvalue='SPA_PEAK',zvalue=cmd_list2[i][1],wvalue='PA_CCT_STG0_DRAIN',w_en=0, IM3_Test_Memu=['','','','']);
                    [P1dB_IN,P1dB_OUT,kk,Delta_out]= P1dB_Data_Analysis(data,tone_step);
                    addition='P1dB_IN_%s_out_%s'%(P1dB_IN,P1dB_OUT);
                    Fig_Label(xlabel_name, ylabel_name, freq, addition,'lower right');
                    plt.savefig(data_path+'TX_P1dB_Test_%s_%s_%s.png'%(cmd_list2[i][1],loop_value,freq_sweep));
                    plt.close()

        output_file.close();


    def TX_P1dB_Test_Matching(self, Init_Set, csv_name, sweep_list1, sweep_list2, curr_en, chan, EVM_en, iqv_no):

        [Board_Num, pll_freq, tone_freq, IM3_Tone1_freq, IM3_Tone2_freq, SPA_Revise_Power, gain_filter, gain_pa, spa_rb, data_path, device_spa, cable_lose_spa, cable_lose_instr]=Init_Set;
        print cable_lose_spa

##        csv_header=['Temperature','VDD','NO','IDC_mA','SAR_PWR','SPA_PEAK'];
        csv_header=['Temperature','IDC_mA','SAR_PWR','SPA_PEAK'];
        [data_path,output_file,filetime] = self.creat_csv(csv_name=csv_name,data_path=data_path,Board_Num=Board_Num,csv_header=csv_header,sweep_list1=sweep_list1,sweep_list2=[])

        if device_spa =="":
            self.spa = HP('SA',cfreq=pll_freq+tone_freq,rb=spa_rb,span=1,reflvl=20);#rb and span
        else:
            self.spa = Agilent('SA',cfreq=pll_freq+tone_freq,rb=spa_rb,span=1,reflvl=20,device=device_spa);#rb and span
        if curr_en == 1:
            mydm=dm.dm('34401A');

##        if vol_en ==1:
##            myeps=eps.eps("E3633A")

        reset_flag = 0
        # Creat Sweep Data Table
        cmd_list1 = []
        Delta_out = []
        for list1 in  sweep_list1:
            cmd_list1.append(self.get_sweep_cmd(list1));

        with open(data_path+'TX_P1dB_Test_Matching_list_%s_%s.csv'%(self.wifi.read_mac(),filetime),'a+') as file1:
            file1.write('matching_no,matching,P1dB_In,P1dB_Out,frequency,')
            if  EVM_en == 1 :
                file1.write('rftx,bbgian,dig_atten,channel,rate, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),')
            for power_i in range(cmd_list1[1][2], cmd_list1[1][3], cmd_list1[1][4]):
                file1.write('%d,'%(power_i))
            file1.write('\n')

            try:
                while True:
                    test_choose=str(raw_input('Please input matching num or "e" to exit:\n'))
                    if test_choose == "e":
                        break
                    logdebug(list(sweep_list2.keys()))
                    Flag=Input_Test(data_in=test_choose,data_ref=list(sweep_list2.keys()));
                    while Flag==False:
                        test_choose=str(raw_input('Please input the right number or "e" to exit: \n'))
                        if test_choose == "e":
                            break
                        Flag=Input_Test(data_in=test_choose,data_ref=list(sweep_list2.keys()))
                    w_str2 =''
                    if  EVM_en == 1 :
                        w_str2 += self.sweep_tx_gain.force_gain_rf(cable_lose=cable_lose_instr,chan=chan, rate='mcs7',target_power = 13,rfgain=gain_pa,bbgain =gain_filter, dig_atten=12, max_pwr=25,num=20, iqv_no=iqv_no,reset_flag=reset_flag,target_pwr_dis=1, evm_list_en=1)
                        w_str2 +='\n'+' , , , , ,'
                        w_str2 +=self.sweep_tx_gain.force_gain_rf(cable_lose=cable_lose_instr,chan=chan, rate='mcs7',target_power = 13,rfgain=gain_pa,bbgain =gain_filter, dig_atten=12, max_pwr=25,num=20, iqv_no=iqv_no,reset_flag=reset_flag,target_pwr_dis=0, evm_list_en=1)
                        reset_flag = 1
                    self.TX_init(PLL_freq=pll_freq,XTAL_freq=40,Gain_Filter=gain_filter,Gain_PA=gain_pa)
                    for freq_sweep in range(cmd_list1[0][2], cmd_list1[0][3], cmd_list1[0][4]):
                        if self.chipv == "CHIP723"or self.chipv == "CHIP724":
                            self.wifiapi.phy_set_freq(freq=freq_sweep, freq_offset=0)
                        else:
                            self.rfpll.set_freq(freq_sweep)
                        if device_spa =="":
                            self.spa = HP('SA',cfreq=freq_sweep+tone_freq,rb=spa_rb,span=1,reflvl=20);#rb and span
                        else:
                            self.spa = Agilent('SA',cfreq=freq_sweep+tone_freq,rb=spa_rb,span=1,reflvl=20,device=device_spa)
                        self.spa.set_rb(spa_rb);
                        data=[];
                        data.append(csv_header);
                        for power_sweep in range(cmd_list1[1][2], cmd_list1[1][3], cmd_list1[1][4]):
                            self.wifi.txtone(1, tone_freq, power_sweep)
##                            self.wifiapi.pll_cap_track_en(1)
                            time.sleep(1)

                            SPA_pwr = self.spa.get_result('PEAK')[1]+SPA_Revise_Power+cable_lose_spa
                            #self.saradc.en_pwdet()
                            sarpwr = 0 #self.saradc.sar_dout(8, signal='tone', pwr_dis=0);
                            self.wifi.txtone(0, tone_freq, power_sweep)
                            if curr_en == 1:
                                IDC0 = int(abs(float(mydm.get_result('IDC'))*1000));
                            else:
                                IDC0 = 0
                            csv_row = [int(test_choose), IDC0,sarpwr,SPA_pwr,freq_sweep, power_sweep];
                            csv.writer(output_file).writerow(csv_row);
                            data.append(csv_row);
                            time.sleep(5)
                        tone_step = cmd_list1[1][4]
                        print data
                        pylab.figure()
                        [xlabel_name, ylabel_name, freq]=data_ananysis(data,xvalue='txtone_backoff',yvalue='SPA_PEAK',zvalue='SA_set_cfreq',wvalue='PA_CCT_STG0_DRAIN',w_en=0, IM3_Test_Memu=['','','','']);
                        [P1dB_IN,P1dB_OUT,kk,Delta_out]= P1dB_Data_Analysis(data,tone_step);
                        addition='P1dB_IN_%s_out_%s'%(P1dB_IN,P1dB_OUT);
                        Fig_Label(xlabel_name, ylabel_name, freq, addition);
                        plt.savefig(data_path+'TX_P1dB_Test_%s_%s_%s.png'%(test_choose,sweep_list2[test_choose],freq_sweep));
                        plt.close()
                        w_str =''
                        w_str3 = ''
                        w_str += " %s, %s ,%d, %2.2f, %d,"%(test_choose,sweep_list2[test_choose],P1dB_IN,P1dB_OUT,freq_sweep)
                        for i in range(0, len(Delta_out), 1):
                            w_str3 +="%2.2f," %(Delta_out[i])
                        file1.write(w_str+w_str2+w_str3+'\n')
            except (IOError,ZeroDivisionError):
                output_file.close();
##                loginfo(e,'Exception occur!')
        output_file.close();

    def TX_P1dB_Test_Matching_debug(self, Init_Set, csv_name, sweep_list1, sweep_list2, curr_en, chan, EVM_en, iqv_no):

        [Board_Num, pll_freq, tone_freq, IM3_Tone1_freq, IM3_Tone2_freq, SPA_Revise_Power, gain_filter, gain_pa, spa_rb, data_path, device_spa, cable_lose_spa, cable_lose_instr,vol_en,temp]=Init_Set;

        csv_header=['Temperature','VDD','NO','IDC_mA','SAR_PWR','SPA_PEAK'];
        [data_path,output_file,filetime] = self.creat_csv(csv_name=csv_name,data_path=data_path,Board_Num=Board_Num,csv_header=csv_header,sweep_list1=sweep_list1,sweep_list2=[])

        if device_spa =="":
            self.spa = HP('SA',cfreq=pll_freq+tone_freq,rb=spa_rb,span=1,reflvl=20);#rb and span
        else:
            self.spa = Agilent('SA',cfreq=pll_freq+tone_freq,rb=spa_rb,span=1,reflvl=20,device=device_spa);#rb and span
        if curr_en == 1:
            mydm=dm.dm('34401A');

        if vol_en ==1:
            myeps=eps.eps("E3633A")

        reset_flag = 0
        # Creat Sweep Data Table
        cmd_list1 = []
        Delta_out = []
        for list1 in  sweep_list1:
            cmd_list1.append(self.get_sweep_cmd(list1));

        with open(data_path+'TX_P1dB_Test_Matching_list_%s_%s.csv'%(self.wifi.read_mac(),filetime),'a+') as file1:
            file1.write('matching_no,matching,P1dB_In,P1dB_Out,frequency,')
            if  EVM_en == 1 :
                file1.write('rftx,bbgian,dig_atten,channel,rate, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),')
            for power_i in range(cmd_list1[1][2], cmd_list1[1][3], cmd_list1[1][4]):
                file1.write('%d,'%(power_i))
            file1.write('\n')

            try:
                while True:
                    test_choose=str(raw_input('Please input matching num or "e" to exit:\n'))
                    if test_choose == "e":
                        break
                    logdebug(list(sweep_list2.keys()))
                    Flag=Input_Test(data_in=test_choose,data_ref=list(sweep_list2.keys()));
                    while Flag==False:
                        test_choose=str(raw_input('Please input the right number or "e" to exit: \n'))
                        if test_choose == "e":
                            break
                        Flag=Input_Test(data_in=test_choose,data_ref=list(sweep_list2.keys()))
                    w_str2 =''
                    csv_header.pop(0)
                    csv_header.pop(0)
                    for vol in (2.7,3.3,3.6):
##                    if vol_en==1:
##                        vol=2.7
                        myeps.pwr(vol,1)
                        self.wifiapi.phyinit()
                        if  EVM_en == 1 :
                            w_str2 = self.sweep_tx_gain.force_gain_rf(cable_lose=cable_lose_instr,chan=chan, freq=2412, rate='54m',target_power = 13,rfgain=gain_pa,bbgain =gain_filter, mcs7_atten1=12, max_pwr=25,num=20, iqv_no=iqv_no,reset_flag=reset_flag,target_pwr_dis=1, evm_list_en=1,workmode_en=0)
                            self.sweep_tx_gain.sweep_tx_gain_EVM(cable_lose=cable_lose_instr, channel=[1], data_rate=['54m'], num=20, target_pwr_dis=0,iqv_no=iqv_no, board_no=sweep_list2[test_choose])
                            reset_flag = 1
                        self.TX_init(PLL_freq=pll_freq,XTAL_freq=40,Gain_Filter=gain_filter,Gain_PA=gain_pa)
                        for freq_sweep in range(cmd_list1[0][2], cmd_list1[0][3], cmd_list1[0][4]):

                            self.rfpll.set_freq(freq_sweep)
                            if device_spa =="":
                                self.spa = HP('SA',cfreq=freq_sweep+tone_freq,rb=spa_rb,span=1,reflvl=20);#rb and span
                            else:
                                self.spa = Agilent('SA',cfreq=freq_sweep+tone_freq,rb=spa_rb,span=1,reflvl=20,device=device_spa)
                            self.spa.set_rb(spa_rb);
                            data=[];
                            data.append(csv_header);
                            for power_sweep in range(cmd_list1[1][2], cmd_list1[1][3], cmd_list1[1][4]):
                                self.wifi.force_txon(1)
                                self.wifi.txtone(1, tone_freq, power_sweep)
                                SPA_pwr = self.spa.get_result('PEAK')[1]+SPA_Revise_Power+cable_lose_spa
                                self.saradc.en_pwdet()
                                sarpwr = self.saradc.sar_dout(8, signal='tone', pwr_dis=0);

                                if curr_en == 1:
                                    IDC0 = int(abs(float(mydm.get_result('IDC'))*1000));
                                else:
                                    IDC0 = 0

                                self.wifi.txtone(0, tone_freq, power_sweep)
                                self.wifi.force_txon(0)
                                csv_row = [int(test_choose), IDC0,sarpwr,SPA_pwr,freq_sweep, power_sweep];
                                csv_row1 = [temp,vol,int(test_choose), IDC0,sarpwr,SPA_pwr,freq_sweep, power_sweep];
                                csv.writer(output_file).writerow(csv_row1);
                                data.append(csv_row);
                                time.sleep(5)
                        print data
                        tone_step = cmd_list1[1][4]
                        pylab.figure()
                        [xlabel_name, ylabel_name, freq]=data_ananysis(data,xvalue='txtone_backoff',yvalue='SPA_PEAK',zvalue='SA_set_cfreq',wvalue='PA_CCT_STG0_DRAIN',w_en=0, IM3_Test_Memu=['','','','']);
                        [P1dB_IN,P1dB_OUT,kk,Delta_out]= P1dB_Data_Analysis(data,tone_step);
                        addition='P1dB_IN_%s_out_%s'%(P1dB_IN,P1dB_OUT);
                        Fig_Label(xlabel_name, ylabel_name, freq, addition);
                        plt.savefig(data_path+'TX_P1dB_Test_%s_%s_%s.png'%(test_choose,sweep_list2[test_choose],freq_sweep));
                        plt.close()
                        w_str =''
                        w_str3 = ''
                        w_str += " %s, %s ,%d, %2.2f, %d,"%(test_choose,sweep_list2[test_choose],P1dB_IN,P1dB_OUT,freq_sweep)
                        for i in range(0, len(Delta_out), 1):
                            w_str3 +="%2.2f," %(Delta_out[i])
                        file1.write(w_str+w_str2+w_str3+'\n')
            except (IOError,ZeroDivisionError):
                output_file.close();
##                loginfo(e,'Exception occur!')
        output_file.close();

    def TX_IM3_Test_Matching(self, Init_Set, csv_name, sweep_list1, sweep_list2, chan, MASK_en, iqv_no):

        [Board_Num, pll_freq, tone_freq, IM3_tone1_freq, IM3_tone2_freq, SPA_Revise_Power, gain_filter, gain_pa, spa_rb, data_path, device_spa, cable_lose_spa,cable_lose_instr]=Init_Set;

        csv_header=['NO','IM3_%s MHz'%(2*IM3_tone1_freq-IM3_tone2_freq),'Tone1_%s MHz'%(IM3_tone1_freq),'Tone2_%s MHz'%(IM3_tone2_freq),'IM3_%s MHz'%(2*IM3_tone2_freq-IM3_tone1_freq)];
        [data_path,output_file,filetime] = self.creat_csv(csv_name=csv_name,data_path=data_path,Board_Num=Board_Num,csv_header=csv_header,sweep_list1=sweep_list1,sweep_list2=[])

        if device_spa =="":
            self.spa = HP('SA',cfreq=pll_freq+tone_freq,rb=spa_rb,span=1,reflvl=20);#rb and span
        else:
            self.spa = Agilent('SA',cfreq=pll_freq+tone_freq,rb=spa_rb,span=1,reflvl=20,device=device_spa);#rb and span

        IM3_Test_Memu=['IM3_%s MHz'%(2*IM3_tone1_freq-IM3_tone2_freq),'Tone1_%s MHz'%(IM3_tone1_freq),'Tone2_%s MHz'%(IM3_tone2_freq),'IM3_%s MHz'%(2*IM3_tone2_freq-IM3_tone1_freq)]

        reset_flag = 0
        #Creat Sweep Data Table
        cmd_list1=[];
        cmd_list2=[];
        reg_data=[];

        for list1 in  sweep_list1:
            cmd_list1.append(self.get_sweep_cmd(list1))
        with open(data_path+'TX_IM3_Test_Matching_list_%s_%s.csv'%(self.wifi.read_mac(),filetime),'a+') as file1:
            file1.write('matching_no,matching,IM3_N,tone1_%s,tone2_%s,IM3_P,IMD_N,IMD_P,INPUT,frequency,'%(IM3_tone1_freq,IM3_tone2_freq))
            if  MASK_en == 1 :
                file1.write('rftx,bbgian,dig_atten,channel,rate, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lower4_freq,lower4_marg, lower3_freq, lower3_marg, lower2_freq, lower2_marg, lower1_freq,lower1_marg, upper1_freq, upper1_marg,upper2_freq,upper2_marg, upper3_freq, upper3_marg, upper4_freq,upper4_marg')
            file1.write('\n')
            try:
                while True:
                    test_choose=str(raw_input('Please input matching num or "e" to exit:\n'))
                    if test_choose == "e":
                        break
                    logdebug(list(sweep_list2.keys()))
                    Flag=Input_Test(data_in=test_choose,data_ref=list(sweep_list2.keys()));
                    while Flag==False:
                        test_choose=str(raw_input('Please input the right number or "e" to exit: \n'))
                        if test_choose == "e":
                            break
                        Flag=Input_Test(data_in=test_choose,data_ref=list(sweep_list2.keys()))
                    w_str2 =''
                    if  MASK_en == 1 :
                        w_str2 = self.sweep_tx_gain.force_gain_rf(cable_lose=cable_lose_instr,chan=chan, rate='mcs0',target_power = 19,rfgain=gain_pa,bbgain =gain_filter, dig_atten=12, max_pwr=25,num=10, iqv_no=iqv_no,target_pwr_dis=0,reset_flag=reset_flag)
                        reset_flag = 1

                    self.TX_init(PLL_freq=pll_freq,XTAL_freq=40,Gain_Filter=gain_filter,Gain_PA=gain_pa)
                    for freq_sweep in range(cmd_list1[0][2], cmd_list1[0][3], cmd_list1[0][4]):

                        self.rfpll.set_freq(freq_sweep)
                        if device_spa =="":
                            self.spa = HP('SA',cfreq=freq_sweep,rb=spa_rb,span=1,reflvl=20);
                        else:
                            self.spa = Agilent('SA',cfreq=freq_sweep,rb=spa_rb,span=1,reflvl=20,device=device_spa);
                        self.spa.set_rb(spa_rb);

                        data=[];
                        data.append(csv_header);

                        for power_sweep in range(cmd_list1[1][2], cmd_list1[1][3], cmd_list1[1][4]):
                            if power_sweep < -50:
                                self.spa.set_reflvl(20);
                            elif power_sweep < -40:
                                self.spa.set_reflvl(20);
                            else:
                                self.spa.set_reflvl(20);

                            self.wifi.txtone(1, IM3_tone1_freq, power_sweep, 1, IM3_tone2_freq, power_sweep);
                            self.wifiapi.pll_cap_track_en(1)
                            self.spa.trace_maxhold(1)
                            time.sleep(1)

                            self.spa.set_cfreq(cfreq=freq_sweep+IM3_tone1_freq);
                            Power_Tone1=self.spa.get_result('PEAK')[1]+SPA_Revise_Power+cable_lose_spa;
                            self.spa.trace_maxhold(1)
                            time.sleep(1)

                            self.spa.set_cfreq(cfreq=freq_sweep+IM3_tone2_freq);
                            Power_Tone2=self.spa.get_result('PEAK')[1]+SPA_Revise_Power+cable_lose_spa;
                            self.spa.trace_maxhold(1)
                            time.sleep(1)

                            self.spa.set_cfreq(cfreq=freq_sweep+2*IM3_tone1_freq-IM3_tone2_freq);
                            Power_IM3_N=self.spa.get_result('PEAK')[1]+SPA_Revise_Power+cable_lose_spa;
                            self.spa.trace_maxhold(1)
                            time.sleep(3)

                            self.spa.set_cfreq(cfreq=freq_sweep+2*IM3_tone2_freq-IM3_tone1_freq);
                            Power_IM3_P=self.spa.get_result('PEAK')[1]+SPA_Revise_Power+cable_lose_spa;
                            self.spa.trace_maxhold(1)
                            time.sleep(3)

                            self.wifi.txtone(0, IM3_tone1_freq, power_sweep, 1, IM3_tone2_freq, power_sweep);
                            time.sleep(5)

                            csv_row=[test_choose, Power_IM3_N, Power_Tone1, Power_Tone2, Power_IM3_P, freq_sweep, power_sweep];

                            csv.writer(output_file).writerow(csv_row);
                            data.append(csv_row);

                        pylab.figure();
                        [xlabel_name_back_off, ylabel_name_IM3_N, freq_IM3_N]=data_ananysis(data,xvalue='txtone_backoff',yvalue='IM3_%s MHz'%(2*IM3_tone1_freq-IM3_tone2_freq),zvalue='SA_set_cfreq',wvalue='PA_CCT_STG0_DRAIN',w_en=0, IM3_Test_Memu=IM3_Test_Memu);
                        [xlabel_name_back_off, ylabel_name_Tone_N, freq_Tone_N]=data_ananysis(data,xvalue='txtone_backoff',yvalue='Tone1_%s MHz'%(IM3_tone1_freq),zvalue='SA_set_cfreq',wvalue='PA_CCT_STG0_DRAIN',w_en=0, IM3_Test_Memu=IM3_Test_Memu);
                        [O_IP3_N, I_IP3_N, O_IP3_P, I_IP3_P,IM3_N_MARK,Tone_N_MARK,Tone_P_MARK,IM3_P_MARK,Power_IN_MARK]=IM3_Data_Analysis(data, IM3_Test_Memu, N_plot_EN=1, P_plot_EN=0,MARK_PWR=16)
                        addition='OIP3 is %s'%O_IP3_N;
                        Fig_Label(xlabel_name_back_off, ylabel_name_Tone_N, freq_Tone_N, addition,'lower right');
                        plt.savefig(data_path+'TX_IM3_N_Test_%s_%s_%s.png'%(test_choose,sweep_list2[test_choose],freq_sweep));
                        plt.close()

                        pylab.figure();
                        [xlabel_name_back_off, ylabel_name_Tone_P, freq_Tone_P]=data_ananysis(data,xvalue='txtone_backoff',yvalue='Tone2_%s MHz'%(IM3_tone2_freq),zvalue='SA_set_cfreq',wvalue='PA_CCT_STG0_DRAIN',w_en=0, IM3_Test_Memu=IM3_Test_Memu);
                        [xlabel_name_back_off, ylabel_name_IM3_P, freq_IM3_P]=data_ananysis(data,xvalue='txtone_backoff',yvalue='IM3_%s MHz'%(2*IM3_tone2_freq-IM3_tone1_freq),zvalue='SA_set_cfreq',wvalue='PA_CCT_STG0_DRAIN',w_en=0, IM3_Test_Memu=IM3_Test_Memu);
                        [O_IP3_N, I_IP3_N, O_IP3_P, I_IP3_P]=IM3_Data_Analysis(data, IM3_Test_Memu, N_plot_EN=0, P_plot_EN=1,MARK_PWR=0)
                        addition='OIP3 is %s'%O_IP3_P;
                        Fig_Label(xlabel_name_back_off, ylabel_name_Tone_P, freq_Tone_P, addition,'lower right');
                        plt.savefig(data_path+'TX_IM3_P_Test_%s_%s_%s.png'%(test_choose,sweep_list2[test_choose],freq_sweep));
                        plt.close()

                        w_str =''
                        w_str += " %s, %s, %2.2f, %2.2f, %2.2f,%2.2f,%2.2f,%2.2f,%2.2f,%d,"%(test_choose,sweep_list2[test_choose],IM3_N_MARK,Tone_N_MARK,Tone_P_MARK,IM3_P_MARK,Tone_N_MARK-IM3_N_MARK,Tone_P_MARK-IM3_P_MARK,Power_IN_MARK,freq_sweep)
                        file1.write(w_str+w_str2+'\n')

            except (IOError,ZeroDivisionError):
                output_file.close();
                loginfo(e,'Exception occur!')
        output_file.close();

    def TX_IM3_Test_Matching_debug(self, Init_Set, csv_name, sweep_list1, sweep_list2, chan, MASK_en, iqv_no):

        [Board_Num, pll_freq, tone_freq, IM3_tone1_freq, IM3_tone2_freq, SPA_Revise_Power, gain_filter, gain_pa, spa_rb, data_path, device_spa, cable_lose_spa,cable_lose_instr,vol_en,temp]=Init_Set;

        csv_header=['temperature','VDD','NO','IM3_%s MHz'%(2*IM3_tone1_freq-IM3_tone2_freq),'Tone1_%s MHz'%(IM3_tone1_freq),'Tone2_%s MHz'%(IM3_tone2_freq),'IM3_%s MHz'%(2*IM3_tone2_freq-IM3_tone1_freq)];
        [data_path,output_file,filetime] = self.creat_csv(csv_name=csv_name,data_path=data_path,Board_Num=Board_Num,csv_header=csv_header,sweep_list1=sweep_list1,sweep_list2=[])

        if device_spa =="":
            self.spa = HP('SA',cfreq=pll_freq+tone_freq,rb=spa_rb,span=1,reflvl=20);#rb and span
        else:
            self.spa = Agilent('SA',cfreq=pll_freq+tone_freq,rb=spa_rb,span=1,reflvl=20,device=device_spa);#rb and span

        IM3_Test_Memu=['IM3_%s MHz'%(2*IM3_tone1_freq-IM3_tone2_freq),'Tone1_%s MHz'%(IM3_tone1_freq),'Tone2_%s MHz'%(IM3_tone2_freq),'IM3_%s MHz'%(2*IM3_tone2_freq-IM3_tone1_freq)]

        reset_flag = 0
        #Creat Sweep Data Table
        cmd_list1=[];
        cmd_list2=[];
        reg_data=[];
        if vol_en == 1:
            myeps=eps.eps("E3633A")

        for list1 in  sweep_list1:
            cmd_list1.append(self.get_sweep_cmd(list1))
        with open(data_path+'TX_IM3_Test_Matching_list_debug_%s_%s.csv'%(self.wifi.read_mac(),filetime),'a+') as file1:
            file1.write('matching_no,matching,IM3_N,tone1_%s,tone2_%s,IM3_P,IMD_N,IMD_P,INPUT,frequency,'%(IM3_tone1_freq,IM3_tone2_freq))
            if  MASK_en == 1 :
                file1.write('rftx,bbgian,dig_atten,channel,rate, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lower4_freq,lower4_marg, lower3_freq, lower3_marg, lower2_freq, lower2_marg, lower1_freq,lower1_marg, upper1_freq, upper1_marg,upper2_freq,upper2_marg, upper3_freq, upper3_marg, upper4_freq,upper4_marg')
            file1.write('\n')
            try:
                while True:
                    test_choose=str(raw_input('Please input matching num or "e" to exit:\n'))
                    if test_choose == "e":
                        break
                    logdebug(list(sweep_list2.keys()))
                    Flag=Input_Test(data_in=test_choose,data_ref=list(sweep_list2.keys()));
                    while Flag==False:
                        test_choose=str(raw_input('Please input the right number or "e" to exit: \n'))
                        if test_choose == "e":
                            break
                        Flag=Input_Test(data_in=test_choose,data_ref=list(sweep_list2.keys()))
                    w_str2 =''
                    csv_header.pop(0)
                    csv_header.pop(0)
                    for vol in (2.7,3.3,3.6):
                        myeps.pwr(vol,1)
##                        self.wifiapi.phyinit()
                        if  MASK_en == 1 :
                            w_str2 = self.sweep_tx_gain.force_gain_rf(cable_lose=cable_lose_instr,chan=chan, freq=self.wifi.chan2freq(chan), rate='mcs0',target_power = 19,rfgain=gain_pa,bbgain =gain_filter, mcs7_atten1=12, max_pwr=25,num=10, iqv_no=iqv_no,reset_flag=reset_flag)
                            reset_flag = 1

                        self.TX_init(PLL_freq=pll_freq,XTAL_freq=40,Gain_Filter=gain_filter,Gain_PA=gain_pa)
                        for freq_sweep in range(cmd_list1[0][2], cmd_list1[0][3], cmd_list1[0][4]):

                            self.rfpll.set_freq(freq_sweep)
                            if device_spa =="":
                                self.spa = HP('SA',cfreq=freq_sweep,rb=spa_rb,span=1,reflvl=20);
                            else:
                                self.spa = Agilent('SA',cfreq=freq_sweep,rb=spa_rb,span=1,reflvl=20,device=device_spa);
                            self.spa.set_rb(spa_rb);

                            data=[];
                            data.append(csv_header);
##                            self.wifi.tx_rc_filter(1,15,10)
##                            self.wifi.force_txon(1)
                            for power_sweep in range(cmd_list1[1][2], cmd_list1[1][3], cmd_list1[1][4]):
                                self.wifi.force_txon(1)
                                if power_sweep < -50:
                                    self.spa.set_reflvl(10);
                                elif power_sweep < -40:
                                    self.spa.set_reflvl(10);
                                else:
                                    self.spa.set_reflvl(10);

                                self.wifi.txtone(1, IM3_tone1_freq, power_sweep, 1, IM3_tone2_freq, power_sweep);

                                self.spa.set_cfreq(cfreq=freq_sweep+IM3_tone1_freq);
                                Power_Tone1=self.spa.get_result('PEAK')[1]+SPA_Revise_Power+cable_lose_spa;

                                self.spa.set_cfreq(cfreq=freq_sweep+IM3_tone2_freq);
                                Power_Tone2=self.spa.get_result('PEAK')[1]+SPA_Revise_Power+cable_lose_spa;


                                self.spa.set_cfreq(cfreq=freq_sweep+2*IM3_tone1_freq-IM3_tone2_freq);
                                Power_IM3_N=self.spa.get_result('PEAK')[1]+SPA_Revise_Power+cable_lose_spa;

                                self.spa.set_cfreq(cfreq=freq_sweep+2*IM3_tone2_freq-IM3_tone1_freq);
                                Power_IM3_P=self.spa.get_result('PEAK')[1]+SPA_Revise_Power+cable_lose_spa;

                                self.wifi.txtone(0, IM3_tone1_freq, power_sweep, 0, IM3_tone2_freq, power_sweep);
                                self.wifi.force_txon(0)

                                csv_row=[test_choose, Power_IM3_N, Power_Tone1, Power_Tone2, Power_IM3_P, freq_sweep, power_sweep];
                                csv_row1=[temp,vol,test_choose, Power_IM3_N, Power_Tone1, Power_Tone2, Power_IM3_P, freq_sweep, power_sweep];
                                csv.writer(output_file).writerow(csv_row1);
                                data.append(csv_row);
                                time.sleep(5)

                        pylab.figure();
                        [xlabel_name_back_off, ylabel_name_IM3_N, freq_IM3_N]=data_ananysis(data,xvalue='txtone_backoff',yvalue='IM3_%s MHz'%(2*IM3_tone1_freq-IM3_tone2_freq),zvalue='SA_set_cfreq',wvalue='PA_CCT_STG0_DRAIN',w_en=0, IM3_Test_Memu=IM3_Test_Memu);
                        [xlabel_name_back_off, ylabel_name_Tone_N, freq_Tone_N]=data_ananysis(data,xvalue='txtone_backoff',yvalue='Tone1_%s MHz'%(IM3_tone1_freq),zvalue='SA_set_cfreq',wvalue='PA_CCT_STG0_DRAIN',w_en=0, IM3_Test_Memu=IM3_Test_Memu);
                        [O_IP3_N, I_IP3_N, O_IP3_P, I_IP3_P,IM3_N_MARK,Tone_N_MARK,Tone_P_MARK,IM3_P_MARK,Power_IN_MARK]=IM3_Data_Analysis(data, IM3_Test_Memu, N_plot_EN=1, P_plot_EN=0,MARK_PWR=16)
                        addition='OIP3 is %s'%O_IP3_N;
                        Fig_Label(xlabel_name_back_off, ylabel_name_Tone_N, freq_Tone_N, addition,'lower right');
                        plt.savefig(data_path+'TX_IM3_N_Test_%s_%s_%s.png'%(test_choose,sweep_list2[test_choose],freq_sweep));
                        plt.close()

                        pylab.figure();
                        [xlabel_name_back_off, ylabel_name_Tone_P, freq_Tone_P]=data_ananysis(data,xvalue='txtone_backoff',yvalue='Tone2_%s MHz'%(IM3_tone2_freq),zvalue='SA_set_cfreq',wvalue='PA_CCT_STG0_DRAIN',w_en=0, IM3_Test_Memu=IM3_Test_Memu);
                        [xlabel_name_back_off, ylabel_name_IM3_P, freq_IM3_P]=data_ananysis(data,xvalue='txtone_backoff',yvalue='IM3_%s MHz'%(2*IM3_tone2_freq-IM3_tone1_freq),zvalue='SA_set_cfreq',wvalue='PA_CCT_STG0_DRAIN',w_en=0, IM3_Test_Memu=IM3_Test_Memu);
                        [O_IP3_N, I_IP3_N, O_IP3_P, I_IP3_P]=IM3_Data_Analysis(data, IM3_Test_Memu, N_plot_EN=0, P_plot_EN=1,MARK_PWR=0)
                        addition='OIP3 is %s'%O_IP3_P;
                        Fig_Label(xlabel_name_back_off, ylabel_name_Tone_P, freq_Tone_P, addition,'lower right');
                        plt.savefig(data_path+'TX_IM3_P_Test_%s_%s_%s.png'%(test_choose,sweep_list2[test_choose],freq_sweep));
                        plt.close()

                        w_str =''
                        w_str += " %s, %s, %2.2f, %2.2f, %2.2f,%2.2f,%2.2f,%2.2f,%2.2f,%d,"%(test_choose,sweep_list2[test_choose],IM3_N_MARK,Tone_N_MARK,Tone_P_MARK,IM3_P_MARK,Tone_N_MARK-IM3_N_MARK,Tone_P_MARK-IM3_P_MARK,Power_IN_MARK,freq_sweep)
                        file1.write(w_str+w_str2+'\n')

            except (IOError,ZeroDivisionError):
                output_file.close();
                loginfo(e,'Exception occur!')
        output_file.close();

#********************************************************************
#************************** DATA plot & Analysis*********************
#********************************************************************

def data_ananysis(data,xvalue='txtone_backoff',yvalue='IDC0',zvalue='IDC1',wvalue='PA_CCT_STG0_DRAIN',w_en=1, IM3_Test_Memu=['','','','']):

    name_table= [
                ['SPA_PEAK','Output Power (dBm)'],
                ['SAR_PWR','SAR PWR'],
                ['SA_set_cfreq','Freqency '],
                ['txtone_backoff','txtone Backoff'],
                ['IDC_mA','IDC_mA'],
                ['TMX_CCT_LOAD','TMX CCT LOAD'],
                ['TMX_RCT_LOAD','TMX RCT LOAD'],
                ['PA_GCT_STG0','PA GCT STG0'],
                ['PA_GCT_STG1','PA GCT STG1'],
                ['PA_GCT_STG2','PA GCT STG2'],
                ['PA_CCT_STG0_DRAIN','PA CCT STG0 DRAIN'],
                ['PA_CCT_STG1','PA CCT STG1'],
                ['PA_CCT_STG2','PA CCT STG2'],
                ['PA_RCT_STG2','PA RCT STG2'],
                ['txbb_gain','txbb_gain'],
                [IM3_Test_Memu[0],IM3_Test_Memu[0]],
                [IM3_Test_Memu[1],IM3_Test_Memu[1]],
                [IM3_Test_Memu[2],IM3_Test_Memu[2]],
                [IM3_Test_Memu[3],IM3_Test_Memu[3]]
                ];
    color_map=['b','g','r','c','m','y','k'];
#    style_map=['-','--','v','^','<','>','1','2','3','4','s','*','+','x','|','D','--',':','.'];
    style_map=['-','--'];


    colsty=[];
    for element1 in style_map:
        for element2 in color_map:
            colsty.append(element1+element2);

    name_rows=np.size(name_table,0);# rows =19
    name_lines=np.size(name_table,1); # lines=2

    for i in range(0,name_rows,1):
        if name_table[i][0]==xvalue:
            xlabel_name=name_table[i][1];
        if name_table[i][0]==yvalue:
            ylabel_name=name_table[i][1];
        if name_table[i][0]==zvalue:
            zlabel_name=name_table[i][1];

    for jj in range(0,len(data[0]),1):
        if data[0][jj]=='SA_set_cfreq':
            freq_line=jj;

    freq = data[1][freq_line];


    if w_en==1:
        title_wvalue=wvalue;

    [x_line, y_line, z_line, w_line]=xyz_find(data, xvalue, yvalue, zvalue, wvalue, w_en);
    [x_data, y_data, z_data, w_data]=xyz_data(data, x_line, y_line, z_line, w_line, w_en);
    z_value=z_diff(z_data);

    map_num=int(np.random.random_sample()*len(colsty));

    for kk5 in z_value:

        x_plot=[];
        y_plot=[];
        for kk7 in range(0,len(z_data),1):
            if z_data[kk7]==kk5:
                x_plot.append(x_data[kk7]);
                y_plot.append(y_data[kk7]);

#            z_label=z_value[kk5];

        map_num=(map_num+1)%len(colsty);

        if xvalue=='txtone_backoff':
            x_plot=arry_gain(x_plot,gain=1)

        pylab.plot(x_plot,y_plot,colsty[map_num],label='%s = %s'%(zvalue,kk5),linewidth=3);

    return [xlabel_name, ylabel_name, freq];


def Fig_Label(xlabel_name, ylabel_name, freq, addition='',loc='upper left'):
    pylab.xlabel('%s'%xlabel_name);                 #creat xlabel
    pylab.ylabel('%s'%ylabel_name);     #creat ylabel
    pylab.title('%s VS %s %s @ %s'%(ylabel_name, xlabel_name, addition, freq));    #creat title of the picture

    pylab.xscale('linear');             #'linear','log','symlog'
    pylab.grid();     #creat grid lines
    #pylab.show();    #show the picture
    pylab.legend(loc=loc,fontsize=10);   #creat a label of many lines





def IM3_Data_Analysis( data, IM3_Test_Memu, N_plot_EN=1, P_plot_EN=1, MARK_PWR=16):
    lines = np.size(data,1);
    rows  = np.size(data,0);

    for i in range(0,lines,1):
        if data[0][i]==IM3_Test_Memu[0]:
            IM3_N_line=i;
        if data[0][i]==IM3_Test_Memu[1]:
            Tone_N_line=i;
        if data[0][i]==IM3_Test_Memu[2]:
            Tone_P_line=i;
        if data[0][i]==IM3_Test_Memu[3]:
            IM3_P_line=i;
        if data[0][i]=='txtone_backoff':
            Input_Pow_line=i;


    IM3_N_Data=[];
    IM3_P_Data=[];
    Tone_N_Data=[];
    Tone_P_Data=[];
    Input_Data=[];

    for kk1 in range(1,rows,1):
        IM3_N_Data.append(data[kk1][IM3_N_line]);
        IM3_P_Data.append(data[kk1][IM3_P_line]);
        Tone_N_Data.append(data[kk1][Tone_N_line]);
        Tone_P_Data.append(data[kk1][Tone_P_line]);
        Input_Data.append(data[kk1][Input_Pow_line]);

    delta=2;
    print '*****************************************'
    print Input_Data;

    for kks in range(0,len(Input_Data),1):
        print Input_Data[kks]
        if abs(Input_Data[kks])<80:
            POW_IN1=Input_Data[kks];
            IM3_N1=IM3_N_Data[kks];
            IM3_P1=IM3_P_Data[kks];
            TONE_N1=Tone_N_Data[kks];
            TONE_P1=Tone_P_Data[kks];

            POW_IN2=Input_Data[kks+delta];
            IM3_N2=IM3_N_Data[kks+delta];
            IM3_P2=IM3_P_Data[kks+delta];
            TONE_N2=Tone_N_Data[kks+delta];
            TONE_P2=Tone_P_Data[kks+delta];
            print kks
            break;




    [I_IP3_N, O_IP3_N, pow_in_N, tone_line_N, im3_lin3_N]=cal_IP3(pow_in=Input_Data, pow_in_p1=POW_IN1, im3_p1=IM3_N1, tone_p1=TONE_N1, pow_in_p2=POW_IN2, im3_p2=IM3_N2, tone_p2=TONE_N2);
    [I_IP3_P, O_IP3_P, pow_in_P, tone_line_P, im3_lin3_P]=cal_IP3(pow_in=Input_Data, pow_in_p1=POW_IN1, im3_p1=IM3_P1, tone_p1=TONE_P1, pow_in_p2=POW_IN2, im3_p2=IM3_P2, tone_p2=TONE_P2);

    x_plot_N=arry_gain(pow_in_N,gain=1)
    x_plot_P=arry_gain(pow_in_P,gain=1)

    if N_plot_EN==1:
        pylab.plot(x_plot_N,tone_line_N,'b--',label='TONE_N',linewidth=3);
        pylab.plot(x_plot_N,im3_lin3_N,'g--',label='IM3_N',linewidth=3);

    if P_plot_EN==1:
        pylab.plot(x_plot_P,tone_line_P,'r--',label='TONE_P',linewidth=3);
        pylab.plot(x_plot_P,im3_lin3_P,'c--',label='IM3_P',linewidth=3);

    cur_PWR_find = 0
    Power_IN_MARK = -99.9
    IM3_N_MARK = -99.9
    Tone_N_MARK = -99.9
    Tone_P_MARK = -99.9
    IM3_P_MARK = -99.9
    cur_P1dB_find = 1
    rows1  = np.size(Tone_N_Data,0);
    if MARK_PWR > 0:
        for kk2 in range(0,rows1,1):
            if cur_PWR_find ==0:
                if Tone_N_Data[kk2] >= 16  :
                    Power_IN_MARK = Input_Data[kk2]
                    IM3_N_MARK = IM3_N_Data[kk2]
                    Tone_N_MARK = Tone_N_Data[kk2];
                    Tone_P_MARK = Tone_P_Data[kk2];
                    IM3_P_MARK = IM3_P_Data[kk2]
                    cur_PWR_find = 1
                else:
                    Power_IN_MARK = Input_Data[kk2]
                    IM3_N_MARK = IM3_N_Data[kk2]
                    Tone_N_MARK = Tone_N_Data[kk2];
                    Tone_P_MARK = Tone_P_Data[kk2];
                    IM3_P_MARK = IM3_P_Data[kk2]
                    cur_PWR_find = 0

        return [O_IP3_N, I_IP3_N, O_IP3_P, I_IP3_P,IM3_N_MARK,Tone_N_MARK,Tone_P_MARK,IM3_P_MARK,Power_IN_MARK];
    else:
     return [O_IP3_N, I_IP3_N, O_IP3_P, I_IP3_P]




def cal_IP3(pow_in, pow_in_p1, im3_p1, tone_p1, pow_in_p2, im3_p2, tone_p2):
    logdebug(pow_in, pow_in_p1, im3_p1, tone_p1, pow_in_p2, im3_p2, tone_p2)
    k_tone = (tone_p2-tone_p1)/(pow_in_p2-pow_in_p1);
    k_im3  = (im3_p2 - im3_p1)/(pow_in_p2-pow_in_p1);

    I_IP3=(pow_in_p1*(k_tone-k_im3)-(tone_p1-im3_p1))/(k_tone-k_im3);

    tone_line=[];
    im3_line=[];
    for element in pow_in:
        tone_line.append(k_tone*(element-pow_in_p1)+tone_p1);
        im3_line.append(k_im3*(element-pow_in_p1)+im3_p1);

    O_IP3=k_tone*(I_IP3-pow_in_p1)+tone_p1;

    return [I_IP3, O_IP3, pow_in, tone_line, im3_line];


def P1dB_Data_Analysis(data,tone_step):
    lines = np.size(data,1);
    rows  = np.size(data,0);

    for i in range(0,lines,1):
        if data[0][i]=='txtone_backoff':
            IN_line=i;
        if data[0][i]=='SPA_PEAK':
            OUT_line=i;

    IN_Data=[];
    OUT_Data=[];

    for kk1 in range(1,rows,1):
        IN_Data.append(data[kk1][IN_line]);
        OUT_Data.append(data[kk1][OUT_line]);

    delta=int(8/tone_step); # delta =  2dB
    for kks in range(0,len(IN_Data),1):
        print IN_Data[kks]
        if abs(IN_Data[kks])<80:
            IN1=IN_Data[kks];
            OUT1=OUT_Data[kks];

            IN2=IN_Data[kks+delta];
            OUT2=OUT_Data[kks+delta];

            print kks
            break;

    [I_P1dB_line,O_P1dB_line]=cal_P1dB(IN=IN_Data, X1=IN1, X2=IN2,Y1=OUT1,Y2=OUT2);

    P1dB_IN = -99.9;
    P1dB_OUT = -99.9
    cur_P1dB_find = 0
    P1dB_kk1 = 0
    rows1  = np.size(OUT_Data,0);
    for kk1 in range(0,rows1,1):
        delta = O_P1dB_line[kk1]-OUT_Data[kk1];
        Flag  = bool(delta >= 1.0);
        if cur_P1dB_find ==0 and Flag :
            P1dB_kk1 = kk1
            P1dB_IN = IN_Data[kk1];
            P1dB_OUT = OUT_Data[kk1];
            cur_P1dB_find = 1
            break;
    logdebug('P1dB_IN is %s,P1dB_OUT %s, kk1 is %s'%(P1dB_IN,P1dB_OUT,P1dB_kk1));

    pylab.plot(I_P1dB_line,O_P1dB_line,'r--',label='P1dB_line',linewidth=3);
    pylab.plot([I_P1dB_line[P1dB_kk1],I_P1dB_line[P1dB_kk1]],[int(O_P1dB_line[0]),O_P1dB_line[P1dB_kk1]],'k--',linewidth=1.0);
    pylab.plot([IN_Data[0],IN_Data[P1dB_kk1]],[OUT_Data[P1dB_kk1],OUT_Data[P1dB_kk1]],'k--',linewidth=1.0);
    #pylab.scatter([IN_Data[P1dB_kk1],],[OUT_Data[P1dB_kk1],],s=20,c='r')
    delta_OUT = list(np.array(O_P1dB_line)-np.array(OUT_Data))
    return [P1dB_IN,P1dB_OUT,P1dB_kk1,delta_OUT];


def cal_P1dB(IN, X1, X2,Y1,Y2):

    k = (Y2-Y1)/(X2-X1);

    OUT=[];

    for element in IN:

        OUT.append(k*(element-X1)+Y1);

    return [IN,OUT];


def arry_gain(data,gain=-1):
    data_out=[];
    for element in data:
        data_out.append(element*gain);

    return data_out;




def xyz_find(data,xvalue,yvalue,zvalue,wvalue,w_en):
    rows=np.size(data,1);
    for kk1 in range(0,rows,1):
        if xvalue==data[0][kk1]:
            x_line=kk1;
        if yvalue==data[0][kk1]:
            y_line=kk1;
        if zvalue==data[0][kk1]:
            z_line=kk1;

        if w_en==1:
            if wvalue==data[0][kk1]:
                w_line=kk1;
        else:
            w_line='';
    return [x_line, y_line, z_line, w_line]




def xyz_data(data,x_line,y_line,z_line,w_line,w_en):
    data_rows  = np.size(data,0);
    data_lines = np.size(data,1);

    x_data=[];
    y_data=[];
    z_data=[];
    w_data=[];

    for kk2 in range(1,data_rows,1):
        x_data.append(data[kk2][x_line]);
        y_data.append(data[kk2][y_line]);
        z_data.append(data[kk2][z_line]);

        if w_en==1:
            w_data.append(data[kk2][w_line]);
        else:
            w_data.append('');


    return [x_data,y_data,z_data,w_data];



def z_diff(z_data):
    # How many different Z values in the table;
    z_value=[];
    z_value.append(z_data[0]);
    k=1;
    csv_rows=len(z_data);
    for kk3 in range(0,csv_rows,1):
        count=0;
        for kk4 in range(0,k,1):
            if z_value[kk4]==z_data[kk3]:
                break;
            count=count+1;

        if count==k:
            k=k+1;
            z_value.append(z_data[kk3]);

    return z_value;


def Input_Test(data_in='0',data_ref=['0','1','2']):

    Flag=False;

    for kk2 in range(0,len(data_ref),1):
        if data_in == data_ref[kk2]:
            Flag=True;
            break;

    if Flag==False:
        print 'Input Erro!';

    return Flag








