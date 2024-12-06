#!/usr/bin/env python
# encoding: utf-8
import re
import scipy.optimize as opt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import collections
import time
import os
import logging
import csv
import datetime
from enum import Enum

from baselib.loglib.log_lib import *
from hal.Init import HALS
from rtclib.rtc import ADC_LIB
from rtclib.rtc import RESET_CAUSE
from hal.common import CHIP_ID
from baselib.instrument.awg import awg
from baselib.instrument.eps import eps
from baselib.instrument.dm import dm
from baselib.loglib.log_csv import csvreport
from baselib.tc_platform.common import *
from baselib.tc_platform.tc_platform import *
from baselib.test_channel.com import COM
from collections import OrderedDict

from functools import wraps

class HtolPtest(object):
	'''Class used to save scripts for HTOL test
		
	Below functions is prepared for ESP32 to be used as the Monitor Board to receive beacon and check DUT status
	'''
	def __init__(self, channel, chipv = 'ESP32', mac_list_file ='/home/test/Desktop/chip722_m1_htol_mac_list.csv'):
		self.channel  = channel
		self.chipv    = chipv
		self.chip     = HALS(channel, chipv)
		self.mac_df   = pd.read_csv(mac_list_file)
		self.mac_list = ['0x'+i[4:] for i in self.mac_df['CHIP_MAC']]
		# with open(mac_list_file, 'r') as f:
		# 	temp_list = f.readlines()
		# self.mac_list = ['0x'+i[4:-1] for i in temp_list]
			# self.mac_list = [
			# 			'0x3471A679',
			# 			'0x3471A411',
			# 			'0x3471A538',
			# 			'0x3471A728',
			# 			'0x3471A57E'   #only module w/ 32k
			# 			] #use only last eight digits of MAC address
		self.col_l = ['TIME','ROUND#','CHIP#','CHIPVER','MAC','RSSI','RATE','LEN','FREQ','VDD33','CLK8M','CLK150K','PVT','O_CODE','CLK32K','PlaceHolder','PlaceHolder']


	def _read_tx(self,num_of_chip=0,timeout=1):
		'''receives beacon from DUT with mac defined below, Once info is collected, `CmdStop` will be executed

		:param:
			- num_of_chip: pick number of chip to be checked from MAC List
		:return:
		'''
		mac_use = self.mac_list[num_of_chip]
		rx_str  = self.channel.req_com('get_rx_buffer 1 %s'%mac_use,endstr='SA:',timeout=timeout)
		self.channel.req_com('CmdStop',timeout=timeout)
		return rx_str

	def _monitor_log_prep(self,file_path='/home/test/Desktop', file_name='rx_log'):
		'''writes column names to csv file 
		'''
		self.csv_file = file_path + '/' + file_name + '.csv'
		self.log_file = file_path + '/' + file_name + '.txt'
		with open(self.csv_file,'a+') as f_csv:
			csv_handle = csv.writer(f_csv)
			csv_handle.writerow(self.col_l)
		return		

	def run_monitor(self, num_of_chip=0,num_of_check=0):
		'''kicks a round of monitor action and records information into csv & log file
		'''
		rx_fail_flag = 0
		rx_str = self._read_tx(num_of_chip)
		with open(self.log_file,'a+') as f_log:
			f_log.write('\n'+time.asctime()+', '
				+'CHIP#%d_ver%s'%(self.mac_df['CHIP_NUM'][num_of_chip],self.mac_df['CHIP_VER'][num_of_chip])
				+': '+rx_str)

		if len(rx_str.splitlines()) > 1:
			rx_str_l = rx_str.split('\r\n')[1].split(',')
			#organize data for csv saving
			rx_str_l[0]=rx_str_l[0][3:]
			rx_str_l[1]=rx_str_l[1].split(':')[1]
			rx_str_l[2]=rx_str_l[2].split(':')[1]
			rx_str_l[3]=rx_str_l[3].split(':')[1]
			rx_str_l[4]=rx_str_l[4].split(':')[1]
			rx_str_l[6]=(1000000 << 19) /int(rx_str_l[6])*256/1.0e6
			rx_str_l[7]=(1000000 << 19) /int(rx_str_l[7])/1.0e3
			rx_str_l[10]=(1000000 << 19) /int(rx_str_l[10])/1.0e3
		else:
			rx_str_l=['']*(len(self.col_l)-3)
			rx_fail_flag = 1
			rx_str_l.insert(0,self.mac_list[num_of_chip])
		rx_str_l.insert(0,self.mac_df['CHIP_VER'][num_of_chip])
		rx_str_l.insert(0,self.mac_df['CHIP_NUM'][num_of_chip])
		rx_str_l.insert(0,num_of_check)
		rx_str_l.insert(0,time.asctime())
		with open(self.csv_file,'a+') as f_csv:
			csv_handle = csv.writer(f_csv)
			csv_handle.writerow(rx_str_l)
		return rx_fail_flag

	def daily_loop(self, check_period_in_mins=10,loop_period_in_hours=1):
		'''checks every DUTs condition w/ time period defined by parameter
		'''
		fail_dict = {'ROUND#':[],'CHIP_MAC':[],'CHIP_VER':[],'CHIP_NUM':[]}
		# date_l = time.asctime().split(' ')
		# file_name = 'CHIP722m_HTOL_Monitor_Log'+'_'+date_l[-1]+'_'+date_l[1]+date_l[2]+'_'+date_l[3]
		date_l = time.localtime()
		file_name = 'CHIP722m_HTOL_Monitor_Log'+'_%d_%d_%d_%d:%d:%d'%(date_l.tm_year,date_l.tm_mon,date_l.tm_mday,
			date_l.tm_hour,date_l.tm_min,date_l.tm_sec)
		file_path = '/home/test/Desktop'
		self._monitor_log_prep(file_path,file_name)

		num_of_checks = loop_period_in_hours*60/check_period_in_mins
		
		loginfo('LOOP CHECK starts @ %s'%time.asctime())
		loginfo('-'*18) 
		loginfo('Will check each part every %smins, total of %dhours will be spent'%(check_period_in_mins,loop_period_in_hours))		
		loginfo('-'*18) 
		for n in range(int(num_of_checks)):
			loginfo('Round# %d'%n)
			for i,v in enumerate(self.mac_list):
				logwarn('CHECKING CHIP MAC: %s'%v)
				rx_fail_flag = self.run_monitor(i,n)
				if rx_fail_flag != 0:
					fail_dict['ROUND#'].append(n)
					logerror('RX ERROR FLAG !!!')
					for key in ['CHIP_MAC','CHIP_VER','CHIP_NUM']:
						fail_dict[key].append(self.mac_df[key][i])
						logerror('%s: %s '%(key,self.mac_df[key][i]))
			wait_period = check_period_in_mins*60
			logwarn('Wait for %d mins to check another round'%check_period_in_mins)
			t_f = (datetime.datetime.now()+datetime.timedelta(minutes=check_period_in_mins)).strftime("%Y-%m-%d %H:%M:%S")
			logwarn('Next round of check is #%d, %d rounds left\n     To be started @ %s '%(n+1,num_of_checks-n-1,t_f))
			time.sleep(wait_period)
		fail_df = pd.DataFrame(fail_dict)
		print fail_df


