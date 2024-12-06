from rftest.rflib.wifi_lib import WIFILIB
from rftest.rflib import *
import win32com
import win32com.client
from win32com.client import Dispatch, constants, gencache
from docx import Document
import re
import baselib.test_channel.channel as chn
from baselib.loglib.log_lib import *
from baselib.instrument import *
import numpy as np
import scipy
from math import *
import time
from baselib.test_channel import *
from baselib.instrument.tester_serv import *
import sys
from baselib.instrument import *
import csv
import xlwt
import xlrd
import os
from rftest.rflib.csv_report import csvreport
from rftest.rflib import rfglobal
from baselib.instrument.tester_serv import wt200_serv
from hal.hwregister.hwi2c.all import *
from hal.wifi_api import WIFIAPI

rate_bps_dict = rfglobal.rate_bps_dict
rx_acpr_crt = rfglobal.rx_acpr_crt
rx_pwr_signal=rfglobal.rx_pwr_signal_vs_data_rate

class RF_ACPR(object):
    def __init__(self,comport,chipv='ESP32'):
        self.comport = comport
        self.chipv = chipv
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.i2c = HWI2C(self.comport,self.chipv)
        self.wifiapi = WIFIAPI(self.comport,self.chipv)
        ####self.wifitx = WIFITX(self.comport,self.chipv)
        ####self.wifirx = WIFIRX(self.comport,self.chipv)
        self.acpr_data_path = 'D:/chip/eagletest/py_script/rftest/rfdata/'

    def iq_open(self,name=''):
        if name == 'iqxel':
            iqxel_serv.init()
            iqxel_serv.open_instru('192.168.100.252')
            loginfo('iqxel is opened')
        elif name == 'wt200':
            wt200_serv.init()
            result=wt200_serv.open_instru('192.168.100.251')
            res1 = result.split(',')
            res_ID_1 = int(res1[1],10)
            return res_ID_1

        elif name == 'wt208c':
            wt200_serv.init()
            result=wt200_serv.open_instru('192.168.100.253')
            res2 = result.split(',')
            res_ID_2 = int(res2[1],10)
            return res_ID_2

        elif name == 'iqview':
            wt200_serv.init()
            result=iqv_serv.open_instru('192.168.100.254')
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
        elif name == 'iqview':
            iqv_serv.close()
            iqv_serv.term()

    def iq_sigout(self,name='',rf_freqMhz=2412,pwr=-10,ex_att=1,data_rate='11m',frmcnt=1,iqv_no=1):
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
            wt200_serv.txfrmcnt(frmcnt)
            loginfo('TX wt200 is ready!');
        elif name == 'wt208c':
            wt200_serv.setvsg(rf_freqMhz,pwr+ex_att,iqv_no)
            wt200_serv.setrate(data_rate)
            wt200_serv.txenable(1)
            wt200_serv.txfrmcnt(frmcnt)
            loginfo('TX wt208c is ready!');
        if name == 'iqview':
            iqv_serv.setvsg(rf_freqMhz,pwr+ex_att,iqv_no)
            iqv_serv.setrate(data_rate)
            iqv_serv.txenable(1)
            iqv_serv.txfrmcnt(frmcnt)
            loginfo('TX iqxel is ready!');


    def iq_vsg_stop(self,name=''):
        if name == 'iqxel':
            iqxel_serv.txenable(0)
        elif name == 'wt200':
            wt200_serv.txenable(0)
        elif name == 'wt208c':
            wt200_serv.txenable(0)
        elif name == 'iqview':
            iqv_serv.txenable(0)

    def rx_acpr(self,iq_signal='iqxel',iq_interfere='wt208c',lost_list=[11.5],iq_mode=['11b'], pwr_interfere_step=1, packnum=100, iqv_signal_no=1,iqv_interfere_no=1,Module_Name='ESP32_Testboard',Module_Num=''):

        '''
        iq_signal='iqxel' and iq_interfere='wt200': iqxel is signal source, wt200 is interfere source

    	'''
        # left_port =0,right port =1;

    	cable_lose_sig = lost_list[0]
        if len(lost_list)==1:
            cable_lose_inf = lost_list[0]
        else:
            cable_lose_inf = lost_list[1]

    	PATH = self.acpr_data_path +'rf_acpr_data'+'/'
    	filetime = time.strftime('_%Y%m%d_%H%M%S',time.localtime(time.time()));
    	data_path = PATH+'%s'%(Module_Name)+'_%s'%(Module_Num)+'%s'%('_ACPR_TEST')+filetime+'/'
    	os.mkdir(PATH+'%s'%(Module_Name)+'_%s'%(Module_Num)+'%s'%('_ACPR_TEST')+filetime)
##    	doc_file=PATH+"\\ESP_ACPR_Test_Report.doc"
##
##    	wordapp = Dispatch('Word.Application')
##    	wordapp.Visible = 1
##    	doc = wordapp.Documents.Open(doc_file)
##    	doc.SaveAs(data_path+"\\ESP_ACPR_Test_Report_%s_%s.docx"%(Module_Name,Module_Num))
##    	doc.Close()
##    	doc = wordapp.Documents.Open(data_path+"\\ESP_ACPR_Test_Report_%s_%s.docx"%(Module_Name,Module_Num))
##    	select = wordapp.Selection

    	res_inf = self.iq_open(iq_interfere)
     	res_sig = self.iq_open(iq_signal)

    	for m in iq_mode:
    		data_rate=data_rate_vs_iq_mode_dic[m]
    		rate_l = len(data_rate)
    		for i in range(0,rate_l):
    			cur_rate = data_rate[i]
    			cbw40m = self.wifi.rate2ht40(cur_rate)
    			self.wifi.cbw40m_en(cbw40m)

    			if cur_rate in ['11m','6m','9m','12m','18m','24m','36m','48m','54m','mcs0','mcs1','mcs2','mcs3','mcs4','mcs5','mcs6','mcs7']:
    				channel_signal_list = [1,7,13]
    				channel_interfere_list = [6,12,8] #[6,12,8] 25MHz frequency space of signal and interfere for CCK

    			elif cur_rate in ['mcs0_40','mcs1_40','mcs2_40','mcs3_40','mcs4_40','mcs5_40','mcs6_40','mcs7_40']:
    				channel_signal_list = [11]
    				channel_interfere_list = [3] # 40MHz frequency space of signal and interfere for 11n-40


##    			table = doc.Tables[acpr_word_table_vs_data_rate[cur_rate]]
##    			row_len = len(table.Rows)
##    			col_len = len(table.Columns)
    			pwr_signal=rx_pwr_signal[cur_rate]
    			chan_l = len(channel_signal_list)
    			for j in range(0,chan_l):
    				perform_list=[]
    				channel_signal = channel_signal_list[j]
    				channel_interfere = channel_interfere_list[j]
    				freq_signal = self.wifi.chan2freq(channel_signal)
    				freq_interfere = self.wifi.chan2freq(channel_interfere)

##    				self.i2c.bbtop.filter_wifirx0_dcap_lq=filter_dcap
##    				self.i2c.bbtop.filter_wifirx0_dcap_hq=filter_dcap
##    				self.i2c.bbtop.filter_wifirx1_dcap_lq=filter_dcap
##    				self.i2c.bbtop.filter_wifirx1_dcap_hq=filter_dcap
##    				self.i2c.bbtop.filter_wifirx2_dcap_lq=filter_dcap
##    				self.i2c.bbtop.filter_wifirx2_dcap_hq=filter_dcap

    				if cbw40m==1:
    				    self.wifi.rfchsel(channel_signal,2)   ###for 11n-40
    				else:
    				    self.wifi.rfchsel(channel_signal,0)    ###for 11n-20
##    				self.wifiapi.wifi_filtbw_set(1,1)
##    				self.i2c.bbtop.filter_wifirx3_dcap_lq=20
##    				self.i2c.bbtop.filter_wifirx3_dcap_hq=20
##    				self.i2c.bbtop.filter_wifirx1_dcap_lq=14
##    				self.i2c.bbtop.filter_wifirx1_dcap_hq=14
##       				self.i2c.bbtop.filter_wifirx2_dcap_lq=63
##    				self.i2c.bbtop.filter_wifirx2_dcap_hq=63
##       				self.i2c.bbtop.filter_wifirx0_dcap_lq=14
##    				self.i2c.bbtop.filter_wifirx0_dcap_hq=14
    				start_pwr_interfere = start_pwr_interfere_vs_data_rate[cur_rate]
    				stop_pwr_interfere = stop_pwr_interfere_vs_data_rate[cur_rate]
    				pwr_interfere = start_pwr_interfere
    				print pwr_interfere,stop_pwr_interfere
    				while pwr_interfere>=stop_pwr_interfere:

						wt200_serv._connID = res_inf
						self.iq_sigout(iq_interfere,freq_interfere,pwr_interfere,cable_lose_inf,cur_rate,0,iqv_interfere_no)
##    					self.wifi.esp_rx(channel_signal, cur_rate)
						self.wifi.rxstart(cur_rate)
						wt200_serv._connID = res_sig
						self.iq_sigout(iq_signal,freq_signal,pwr_signal,cable_lose_sig,cur_rate,packnum,iqv_signal_no)
						time.sleep(0.5)
						result_data = self.wifi.cmdstop()

						self.iq_vsg_stop(iq_interfere)
						self.iq_vsg_stop(iq_signal)
##    					time.sleep(1)
						[DesirePackNum, gain, rssi, noise, err, err2, freqoff,rssi_min,rssi_max] = self.wifi.rxresult(result_data)

						perform_list.append((pwr_interfere,pwr_signal,DesirePackNum,gain,rssi,noise,err,err2, freqoff))
						pwr_interfere=pwr_interfere-pwr_interfere_step

    #**************creat log***************#

    				cur_pwr_interfere=0
    				cur_pwr_signal=0
    				cur_sens_DesirePackNum=0
    				cur_sense_rssi=0
    				cur_pwr_interfere_find=0
    				fail=0
    				cur_err=0
    				cur_err_fcs=0
    				rx_acpr=0

    				csv_name ="Rxagcscan_sigchn%d_interchn%d_rate%s"%(channel_signal,channel_interfere,cur_rate);
    				output_file = open(data_path+'%s.csv'%(csv_name), 'wb')
    				csv_header  = ['pwr_interfere','pwr_signal','DesirePackNum','gain','rssi','noise','err','err2', 'freqoff',"filter_dcap"]
    				csv.writer(output_file).writerow(csv_header)
    				for i in range(0,len(perform_list)):
    					data=perform_list[i]
    					print data
    					csv_row=[data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]]
    					csv.writer(output_file).writerow(csv_row)
    					if cur_pwr_interfere_find==0:
    						if data[2]>=(100*0.9):

    							cur_pwr_interfere=data[0]
    							cur_pwr_signal=data[1]
    							cur_sens_DesirePackNum=data[2]
    							cur_sense_rssi=data[3]
    							cur_err=data[5]
    							cur_err_fcs = data[6]
    							cur_pwr_interfere_find=1
    							data = perform_list[i+1]
    						else:
    							cur_pwr_interfere=data[0]
    							cur_pwr_signal=data[1]
    							cur_sens_DesirePackNum=data[2]
    							cur_sense_rssi=data[3]
    							cur_err=data[5]
    							cur_err_fcs = data[6]
    							cur_pwr_interfere_find=0

    				rx_acpr=cur_pwr_interfere-pwr_signal
    				logdebug([cur_pwr_interfere, pwr_signal, rx_acpr, cur_sens_DesirePackNum, cur_sense_rssi/10.0, cur_err, cur_err_fcs])
    				rf_list=['%d'%channel_signal,'%d'%channel_interfere,'%d'%pwr_signal,'%d'%cur_pwr_interfere,'%d'%rx_acpr]
    				if cur_rate in ['54m','48m','36m','24m','18m','12m','9m','6m','mcs7','mcs6','mcs5','mcs4','mcs3','mcs2','mcs1','mcs0']:
    					col = table_chan_col_11gn_dic[channel_signal]
    				elif cur_rate in ['mcs7_40','mcs6_40','mcs5_40','mcs4_40','mcs3_40','mcs2_40','mcs1_40','mcs0_40']:
    					col = table_chan_col_11n40_dic[channel_signal]
    				else:
    					col = table_chan_col_11b_dic[channel_signal]

    				row = table_rate_row_dic[cur_rate]
##    				select0 = table.Select()
##    				select1 = table.Cell(row,col).Select()
##    				select.Font.Bold = False
##    				select.Font.Italic = False
##    				select.Font.ColorIndex = 0
##    				select.TypeText(rx_acpr)
    #********************** pass or fail***************************#
##    		col_start = 2
##    		col_end = 5
##    		acpr_lst = []
##    		k_flag = []
##    		row_start = table_rate_row_dic[data_rate[0]]
##    		row_end = table_rate_row_dic[data_rate[len(data_rate)-1]]
##    		row_lst = []
##    		for n in range (0,len(data_rate)):
##    			row = table_rate_row_dic[data_rate[n]]
##    			row_lst.append(row)
##
##    		print row_lst
##    		for col in range (col_start,col_end):
##    			for row in row_lst:
##    				select2 = table.Cell(int(row),col).Select()
##    				acpr_1 = table.Cell(int(row),col).Range.Text
##    				acpr_2=acpr_1.encode('ascii')
##    				acpr = re.findall(r"\d+\.?\d*",acpr_2)
##    				if acpr != []:
##    					a = int(acpr[0])
##    				else:
##    					a = []
##
##    				acpr_lst.append(a)
##    				print acpr_lst
##    			acpr_dic = {}
##    			for x in range (0,len(acpr_lst)):
##    				acpr_dic[data_rate[x]] = acpr_lst[x]
##    			flag_none = 3
##    			flag = 3
##    			logdebug(acpr_dic)
##    			for k in range (0,len(acpr_dic)):
##    				if acpr_dic[data_rate[k]] == []:
##    					flag_none = 1
##    				elif acpr_dic[data_rate[k]] >= rx_acpr_crt[data_rate[k]]:
##    					flag = 1
##    				elif acpr_dic[data_rate[k]] < rx_acpr_crt[data_rate[k]]:
##    					flag = 0
##    					k_flag.append(k)
##    			if flag_none == 1:
##    				select3 = table.Cell(3,col).Select()
##    				select.TypeText('')
##    			elif len(k_flag) == 0:
##    				select3 = table.Cell(3,col).Select()
##    				select.TypeText('pass')
##    			else:
##    				select3 = table.Cell(3,col).Select()
##    				select.TypeText('fail')
##    				for m in range(0,len(k_flag)):
##    					row_flag = table_rate_row_dic[data_rate[k_flag[m]]]
##    					select3 = table.Cell(row_flag,col).Select()
##    					select.Font.Bold = True
##
##    			acpr_lst = []
##    			k_flag = []
##    			flag = 3
##    			flag_none = 3

    	self.iq_close(iq_signal)
    	self.iq_close(iq_interfere)
##    	doc.Save()
##    	doc.Close()
##    	wordapp.Quit()

	print '\n\n----------test complete----------------\n'

    def rx_acpr_debug(self,iq_signal='iqxel',iq_interfere='wt208c',lost_list=[11.5],iq_mode=['11b'], pwr_interfere_step=1, packnum=100, iqv_signal_no=1,iqv_interfere_no=1,Module_Name='ESP32_Testboard',Module_Num=''):

        '''
        iq_signal='iqxel' and iq_interfere='wt200': iqxel is signal source, wt200 is interfere source

    	'''
        # left_port =0,right port =1;

    	cable_lose_sig = lost_list[0]
        if len(lost_list)==1:
            cable_lose_inf = lost_list[0]
        else:
            cable_lose_inf = lost_list[1]

    	PATH = self.acpr_data_path +'rf_acpr_data'+'/'
    	filetime = time.strftime('_%Y%m%d_%H%M%S',time.localtime(time.time()));
    	data_path = PATH+'%s'%(Module_Name)+'_%s'%(Module_Num)+'%s'%('_ACPR_TEST')+filetime+'/'
    	os.mkdir(PATH+'%s'%(Module_Name)+'_%s'%(Module_Num)+'%s'%('_ACPR_TEST')+filetime)
##    	doc_file=PATH+"\\ESP_ACPR_Test_Report.doc"
##
##    	wordapp = Dispatch('Word.Application')
##    	wordapp.Visible = 1
##    	doc = wordapp.Documents.Open(doc_file)
##    	doc.SaveAs(data_path+"\\ESP_ACPR_Test_Report_%s_%s.docx"%(Module_Name,Module_Num))
##    	doc.Close()
##    	doc = wordapp.Documents.Open(data_path+"\\ESP_ACPR_Test_Report_%s_%s.docx"%(Module_Name,Module_Num))
##    	select = wordapp.Selection

    	res_inf = self.iq_open(iq_interfere)
     	res_sig = self.iq_open(iq_signal)

    	for m in iq_mode:
    		data_rate=data_rate_vs_iq_mode_dic[m]
    		rate_l = len(data_rate)
    		for i in range(0,rate_l):
    			cur_rate = data_rate[i]
    			cbw40m = self.wifi.rate2ht40(cur_rate)
    			self.wifi.cbw40m_en(cbw40m)

    			if cur_rate in ['11m','6m','9m','12m','18m','24m','36m','48m','54m','mcs0','mcs1','mcs2','mcs3','mcs4','mcs5','mcs6','mcs7']:
    				channel_signal_list = [1]
    				channel_interfere_list = [6] #[6,12,8] 25MHz frequency space of signal and interfere for CCK

    			elif cur_rate in ['mcs0_40','mcs1_40','mcs2_40','mcs3_40','mcs4_40','mcs5_40','mcs6_40','mcs7_40']:
    				channel_signal_list = [3]
    				channel_interfere_list = [11] # 40MHz frequency space of signal and interfere for 11n-40


##    			table = doc.Tables[acpr_word_table_vs_data_rate[cur_rate]]
##    			row_len = len(table.Rows)
##    			col_len = len(table.Columns)
    			pwr_signal=rx_pwr_signal[cur_rate]
    			chan_l = len(channel_signal_list)
    			for j in range(0,chan_l):
    				perform_list=[]
    				channel_signal = channel_signal_list[j]
    				channel_interfere = channel_interfere_list[j]
    				freq_signal = self.wifi.chan2freq(channel_signal)
    				freq_interfere = self.wifi.chan2freq(channel_interfere)


    				self.wifi.rfchsel(channel_signal,0)
##    				self.wifiapi.wifi_filtbw_set(1,1)
##    				for filter_dcap in (40,63):
##    					self.i2c.bbtop.filter_wifirx0_dcap_lq=filter_dcap
##    					self.i2c.bbtop.filter_wifirx0_dcap_hq=filter_dcap
##    					self.i2c.bbtop.filter_wifirx1_dcap_lq=filter_dcap
##    					self.i2c.bbtop.filter_wifirx1_dcap_hq=filter_dcap
##    					self.i2c.bbtop.filter_wifirx2_dcap_lq=filter_dcap
##    					self.i2c.bbtop.filter_wifirx2_dcap_hq=filter_dcap
##    					self.i2c.bbtop.filter_wifirx3_dcap_lq=filter_dcap
##    					self.i2c.bbtop.filter_wifirx3_dcap_hq=filter_dcap
##    					print "filter_dacp=%s"%filter_dcap
    				filter_dcap=self.i2c.bbtop.filter_wifirx0_dcap_lq
    				for rxgain in (40,55,56):
        				self.wifi.rx_force_gain(1,rxgain)
        				print "rxgain=%s"%rxgain
        				start_pwr_interfere = start_pwr_interfere_vs_data_rate[cur_rate]
        				stop_pwr_interfere = stop_pwr_interfere_vs_data_rate[cur_rate]
        				pwr_interfere = start_pwr_interfere
        				print pwr_interfere,stop_pwr_interfere
        				while pwr_interfere>=stop_pwr_interfere:

    						wt200_serv._connID = res_inf
    						self.iq_sigout(iq_interfere,freq_interfere,pwr_interfere,cable_lose_inf,cur_rate,0,iqv_interfere_no)
    ##    					self.wifi.esp_rx(channel_signal, cur_rate)
    						self.wifi.rxstart(cur_rate)
    						wt200_serv._connID = res_sig
    						self.iq_sigout(iq_signal,freq_signal,pwr_signal,cable_lose_sig,cur_rate,packnum,iqv_signal_no)
    						time.sleep(0.5)
    						result_data = self.wifi.cmdstop()

    						self.iq_vsg_stop(iq_interfere)
    						self.iq_vsg_stop(iq_signal)
    ##    					time.sleep(1)
    						[DesirePackNum, gain, rssi, noise, err, err2, freqoff,rssi_min,rssi_max] = self.wifi.rxresult(result_data)

    						perform_list.append((pwr_interfere,pwr_signal,DesirePackNum,rssi,rxgain,noise,err,err2, freqoff,filter_dcap))
    						pwr_interfere=pwr_interfere-pwr_interfere_step

    #**************creat log***************#

    				cur_pwr_interfere=0
    				cur_pwr_signal=0
    				cur_sens_DesirePackNum=0
    				cur_sense_rssi=0
    				cur_pwr_interfere_find=0
    				fail=0
    				cur_err=0
    				cur_err_fcs=0
    				rx_acpr=0

    				csv_name ="Rxagcscan_sigchn%d_interchn%d_rate%s"%(channel_signal,channel_interfere,cur_rate);
    				output_file = open(data_path+'%s.csv'%(csv_name), 'wb')
    				csv_header  = ['pwr_interfere','pwr_signal','DesirePackNum','rssi','gain','noise','err','err2', 'freqoff',"filter_dcap"]
    				csv.writer(output_file).writerow(csv_header)
    				for i in range(0,len(perform_list)):
    					data=perform_list[i]
    					print data
    					csv_row=[data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9]]
    					csv.writer(output_file).writerow(csv_row)
    					if cur_pwr_interfere_find==0:
    						if data[2]>=(100*0.9):

    							cur_pwr_interfere=data[0]
    							cur_pwr_signal=data[1]
    							cur_sens_DesirePackNum=data[2]
    							cur_sense_rssi=data[3]
    							cur_err=data[5]
    							cur_err_fcs = data[6]
    							cur_pwr_interfere_find=1
    							data = perform_list[i+1]
    						else:
    							cur_pwr_interfere=data[0]
    							cur_pwr_signal=data[1]
    							cur_sens_DesirePackNum=data[2]
    							cur_sense_rssi=data[3]
    							cur_err=data[5]
    							cur_err_fcs = data[6]
    							cur_pwr_interfere_find=0

    				rx_acpr=cur_pwr_interfere-pwr_signal
    				logdebug([cur_pwr_interfere, pwr_signal, rx_acpr, cur_sens_DesirePackNum, cur_sense_rssi/10.0, cur_err, cur_err_fcs])
    				rf_list=['%d'%channel_signal,'%d'%channel_interfere,'%d'%pwr_signal,'%d'%cur_pwr_interfere,'%d'%rx_acpr]
    				if cur_rate in ['54m','48m','36m','24m','18m','12m','9m','6m','mcs7','mcs6','mcs5','mcs4','mcs3','mcs2','mcs1','mcs0']:
    					col = table_chan_col_11gn_dic[channel_signal]
    				elif cur_rate in ['mcs7_40','mcs6_40','mcs5_40','mcs4_40','mcs3_40','mcs2_40','mcs1_40','mcs0_40']:
    					col = table_chan_col_11n40_dic[channel_signal]
    				else:
    					col = table_chan_col_11b_dic[channel_signal]

    				row = table_rate_row_dic[cur_rate]
##    				select0 = table.Select()
##    				select1 = table.Cell(row,col).Select()
##    				select.Font.Bold = False
##    				select.Font.Italic = False
##    				select.Font.ColorIndex = 0
##    				select.TypeText(rx_acpr)
    #********************** pass or fail***************************#
##    		col_start = 2
##    		col_end = 5
##    		acpr_lst = []
##    		k_flag = []
##    		row_start = table_rate_row_dic[data_rate[0]]
##    		row_end = table_rate_row_dic[data_rate[len(data_rate)-1]]
##    		row_lst = []
##    		for n in range (0,len(data_rate)):
##    			row = table_rate_row_dic[data_rate[n]]
##    			row_lst.append(row)
##
##    		print row_lst
##    		for col in range (col_start,col_end):
##    			for row in row_lst:
##    				select2 = table.Cell(int(row),col).Select()
##    				acpr_1 = table.Cell(int(row),col).Range.Text
##    				acpr_2=acpr_1.encode('ascii')
##    				acpr = re.findall(r"\d+\.?\d*",acpr_2)
##    				if acpr != []:
##    					a = int(acpr[0])
##    				else:
##    					a = []
##
##    				acpr_lst.append(a)
##    				print acpr_lst
##    			acpr_dic = {}
##    			for x in range (0,len(acpr_lst)):
##    				acpr_dic[data_rate[x]] = acpr_lst[x]
##    			flag_none = 3
##    			flag = 3
##    			logdebug(acpr_dic)
##    			for k in range (0,len(acpr_dic)):
##    				if acpr_dic[data_rate[k]] == []:
##    					flag_none = 1
##    				elif acpr_dic[data_rate[k]] >= rx_acpr_crt[data_rate[k]]:
##    					flag = 1
##    				elif acpr_dic[data_rate[k]] < rx_acpr_crt[data_rate[k]]:
##    					flag = 0
##    					k_flag.append(k)
##    			if flag_none == 1:
##    				select3 = table.Cell(3,col).Select()
##    				select.TypeText('')
##    			elif len(k_flag) == 0:
##    				select3 = table.Cell(3,col).Select()
##    				select.TypeText('pass')
##    			else:
##    				select3 = table.Cell(3,col).Select()
##    				select.TypeText('fail')
##    				for m in range(0,len(k_flag)):
##    					row_flag = table_rate_row_dic[data_rate[k_flag[m]]]
##    					select3 = table.Cell(row_flag,col).Select()
##    					select.Font.Bold = True
##
##    			acpr_lst = []
##    			k_flag = []
##    			flag = 3
##    			flag_none = 3

    	self.iq_close(iq_signal)
    	self.iq_close(iq_interfere)
##    	doc.Save()
##    	doc.Close()
##    	wordapp.Quit()

	print '\n\n----------test complete----------------\n'



stop_pwr_interfere_vs_data_rate={  #start_pwr_interfere-pwr_signal=acpr_creterion-5
    "11m":-40,
    "6m":-68,
    "9m":-68,
    "12m":-68,
    "18m":-68,
    "24m":-68,
    "36m":-68,
    "48m":-68,
    "54m":-68,
    "mcs0":-68,
    "mcs1":-68,
    "mcs2":-68,
    "mcs3":-68,
    "mcs4":-68,
    "mcs5":-68,
    "mcs6":-68,
    "mcs7":-68,
    "mcs0_40":-65,
    "mcs1_40":-65,
    "mcs2_40":-65,
    "mcs3_40":-65,
    "mcs4_40":-65,
    "mcs5_40":-65,
    "mcs6_40":-65,
    "mcs7_40":-65
}

start_pwr_interfere_vs_data_rate={
    "11m":-30,
    "6m":-48,
    "9m":-48,
    "12m":-48,
    "18m":-48,
    "24m":-48,
    "36m":-48,
    "48m":-48,
    "54m":-48,
    "mcs0":-48,
    "mcs1":-48,
    "mcs2":-48,
    "mcs3":-48,
    "mcs4":-48,
    "mcs5":-48,
    "mcs6":-48,
    "mcs7":-48,
    "mcs0_40":-45,
    "mcs1_40":-45,
    "mcs2_40":-45,
    "mcs3_40":-45,
    "mcs4_40":-45,
    "mcs5_40":-45,
    "mcs6_40":-45,
    "mcs7_40":-45
}

acpr_word_table_vs_data_rate={
    "11m":2,
    "6m":3,
    "9m":3,
    "12m":3,
    "18m":3,
    "24m":3,
    "36m":3,
    "48m":3,
    "54m":3,
    "mcs0":4,
    "mcs1":4,
    "mcs2":4,
    "mcs3":4,
    "mcs4":4,
    "mcs5":4,
    "mcs6":4,
    "mcs7":4,
    "mcs0_40":5,
    "mcs1_40":5,
    "mcs2_40":5,
    "mcs3_40":5,
    "mcs4_40":5,
    "mcs5_40":5,
    "mcs6_40":5,
    "mcs7_40":5
}
table_chan_col_11b_dic={
    1:2,
    7:3,
    13:4
}
table_chan_col_11gn_dic={
    1:2,
    7:3,
    13:4
}
table_chan_col_11n40_dic={
    3:2,
    9:3,
    11:4
}
table_rate_row_dic = {
	'11m':5,
    '54m':5,
	'48m':6,
	'36m':7,
	'24m':8,
	'18m':9,
	'12m':10,
	'9m':11,
	'6m':12,
	'mcs7':5,
	'mcs6':6,
	'mcs5':7,
	'mcs4':8,
	'mcs3':9,
	'mcs2':10,
	'mcs1':11,
	'mcs0':12,
	'mcs7_40':5,
	'mcs6_40':6,
	'mcs5_40':7,
	'mcs4_40':8,
	'mcs3_40':9,
	'mcs2_40':10,
	'mcs1_40':11,
	'mcs0_40':12}

data_rate_vs_iq_mode_dic={
    '11b':['11m'],
##    '11g':['54m','48m','36m','24m','18m','12m','9m','6m'],
    '11g':['54m','6m'],
##    '11n-20':['mcs7','mcs6','mcs5','mcs4','mcs3','mcs2','mcs1','mcs0'],
    '11n-20':['mcs7','mcs0'],
    '11n-40':['mcs0_40']
##    11n-40':['mcs7_40','mcs6_40','mcs5_40','mcs4_40','mcs3_40','mcs2_40','mcs1_40','mcs0_40']
}
data_rate=['11m','54m','48m','36m','24m','18m','12m','9m','6m','mcs7','mcs6','mcs5','mcs4','mcs3','mcs2','mcs1','mcs0','mcs7_40','mcs6_40','mcs5_40','mcs4_40','mcs3_40','mcs2_40','mcs1_40','mcs0_40']
#sensitivity_word(lost_list=[13],channel=[1,6,11],data_rate=['mcs6','mcs7'], maxpwr=-30, pwr_step=1, packnum=100, instru='iqv', iqv_no=1,data_rx=[],dynamic_mode=0):

