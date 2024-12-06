# -- coding: utf-8 --
# 中文支持

from baselib.loglib.log_lib import *
from hal.Init import HALS
from hal.common import CHIP_ID
from baselib.instrument.awg import awg
from baselib.instrument.eps import eps
from baselib.instrument.dm  import dm
from baselib.tc_platform.common import *
from baselib.tc_platform.tc_platform import *
from baselib.test_channel.com import COM
from baselib.loglib.log_csv import csvreport
import re
import scipy.optimize as opt
import matplotlib.pyplot as plt
import pandas as pd
import time

class CLK_TC_PERF(object):
	'''below scripts written based on chip722, not tested for ESP32 or other chips yet'''
	def __init__(self, channel, chipv = "CHIP722"):
		self.chipv    = chipv
		self.channel  = channel
		self.chip     = HALS(channel,chipv)

	def clk_freq_read(self,clk_type=0,dreg=100,default_val=False):
		''' returns clock frequency read in Hz
		:param: 
			- clk_type: 0: 150K 1: 8M
			- dreg range: 0-256 for both clock types
		'''
		if clk_type   == 0:
			reg_name_pre = 'RTC_REG' 
			reg_name     = 'reg_sck_dcap'
			freq_ratio = 1
		elif clk_type == 1:
			reg_name_pre = 'RTC_CLK_CONF' 
			reg_name     = 'reg_ck8m_dfreq'
			freq_ratio = 256
			self.chip.rtc_clk.clk_8m_en()    #enable 8m
		if default_val: 
			freq_read = self.chip.rtc_clk.get_clk_calibration(clk_type)
			reg_read  = getattr(getattr(self.chip.HWREG.RTC_CNTL,reg_name_pre),reg_name)
		else: 
			setattr(getattr(self.chip.HWREG.RTC_CNTL,reg_name_pre),reg_name,dreg)
			reg_read  = getattr(getattr(self.chip.HWREG.RTC_CNTL,reg_name_pre),reg_name)
			freq_read = self.chip.rtc_clk.get_clk_calibration(clk_type)

		if freq_read.isdigit():
			freq_inHz = (1000000 << 19) / int(freq_read) * freq_ratio
		else:
			freq_inHz = freq_read
		return reg_read, freq_inHz

	def clk_freq_scan(self,clk_type=0,reg_start=0,reg_end=256):
		''' returns clock frequency read in Hz
		:param: 
			- clk_type: 0: 150K 1: 8M
			- reg range: 0-256 for both clock types
		'''
		start_timing=time.time()
		default_reg, original_read = self.clk_freq_read(clk_type=clk_type,default_val=True)
		# val_reg_l = ['o_'+ '%d'%default_reg]
		val_reg_l = [default_reg]
		val_frq_l = [original_read]
		for i in range(reg_start,reg_end):
			reg_read,freq_read = self.clk_freq_read(clk_type=clk_type,dreg=i)
			val_reg_l.append(reg_read)
			val_frq_l.append(freq_read)
		logwarn('TIME SPENT %d'%(time.time()-start_timing))
		data_table = pd.DataFrame(data={'reg':val_reg_l,'freq':val_frq_l})
		return data_table

	def clk_freq_3point(self,clk_type=0,check_points=[0,128,255]):
		''' returns clock frequency read in Hz
		:param: 
			- clk_type: 0: 150K 1: 8M
			- reg range: 0-256 for both clock types
		'''
		default_reg, original_read = self.clk_freq_read(clk_type=clk_type,default_val=True)
		# val_reg_l = ['o_'+ '%d'%default_reg]
		val_reg_l = [default_reg]
		val_frq_l = [original_read]
		for i in check_points:
			reg_read,freq_read = self.clk_freq_read(clk_type=clk_type,dreg=i)
			val_reg_l.append(reg_read)
			val_frq_l.append(freq_read)
		data_table = pd.DataFrame(data={'reg':val_reg_l,'freq':val_frq_l})
		return data_table

	def clk_8m_freq_read(self,dfreq=100,default_val=False):
		self.chip.rtc_clk.clk_8m_en()                 #enable 8m
		#self.chip.rtc_clk.rtc_slow_clk_select(2)
		if default_val:
			freq_8m256_read = self.chip.rtc_clk.get_clk_calibration(1)
		else: 
			self.chip.HWREG.RTC_CNTL.RTC_CLK_CONF.reg_ck8m_dfreq = dfreq
			freq_8m256_read = self.chip.rtc_clk.get_clk_calibration(1)
		if freq_8m256_read.isdigit():
			freq_8m = (1000000 << 19) / int(freq_8m256_read) * 256
		else:
			freq_8m = freq_8m256
		return freq_8m

	def clk_8m_freq_scan(self,reg_start=0,reg_end=256):
		start_timing=time.time()
		original_read = self.clk_8m_freq_read(default_val=True)
		default_reg  = self.chip.HWREG.RTC_CNTL.RTC_CLK_CONF.reg_ck8m_dfreq
		# val_reg_l = ['o_'+ '%d'%default_reg]
		val_reg_l = [default_reg]
		val_frq_l = [original_read]
		for i in range(reg_start,reg_end):
			val_reg_l.append(i)
			val_frq_l.append(self.clk_8m_freq_read(dfreq=i))
		logwarn('TIME SPENT %d'%(time.time()-start_timing))
		data_table = pd.DataFrame(data={'reg':val_reg_l,'freq':val_frq_l})
		return data_table

	def clk_150k_freq_read(self,dcap=100,default_val=False):
		#self.chip.rtc_clk.rtc_slow_clk_select(2)
		if default_val:
			freq_read = self.chip.rtc_clk.get_clk_calibration(0)
		else: 
			self.chip.HWREG.RTC_CNTL.RTC_REG.reg_sck_dcap= dcap
			freq_read = self.chip.rtc_clk.get_clk_calibration(0)
		if freq_read.isdigit():
			freq_150k = (1000000 << 19) / int(freq_read)
		else:
			freq_150k = freq_read
		return freq_150k

	def clk_150k_freq_scan(self,reg_start=0,reg_end=256):
		start_timing=time.time()
		original_read = self.clk_150k_freq_read(default_val=True)
		default_reg  = self.chip.HWREG.RTC_CNTL.RTC_REG.reg_sck_dcap
		# val_reg_l = ['o_'+ '%d'%default_reg]
		val_reg_l = [default_reg]
		val_frq_l = [original_read]
		for i in range(reg_start,reg_end):
			val_reg_l.append(i)
			val_frq_l.append(self.clk_150k_freq_read(dcap=i))
		logwarn('TIME SPENT %d'%(time.time()-start_timing))
		data_table = pd.DataFrame(data={'reg':val_reg_l,'freq':val_frq_l})
		return data_table

	def clk_i2s_debug(self, i2s_type=0, int_div=4):
		'''Suitable for ESP32: export i2s clock to GPIO0 & use apll as clk source

		:param:
			- i2s_type: 0--i2s0, 1--i2s1
			- int_div: integer divder value, configs apll frequency
		'''
		self.chip.rtc_debug.CLK(0,1,1) #export i2s clock to GPIO0
		if i2s_type == 0:
			self.chip.MEM.wrm(0x3ff000c0,4,4,enable)  #open i2s0 clock gating for memory write
			self.chip.MEM.wrm(0x3ff4f0ac,21,21,enable) #enable clk_apll as i2s clock via i2s0 configuration
   			chip.hals.MEM.wrm(0x3ff4f0ac,7,0,div) #clk_apll I2S_CLKM_DIV_NUM integer clock divider
		elif i2s_type ==1:
			self.chip.MEM.wrm(0x3ff000c0,21,21,enable) #open i2s1 clock gating for memory write
			self.chip.MEM.wrm(0x3ff6d0ac,21,21,enable)
   			chip.hals.MEM.wrm(0x3ff6d0ac,7,0,div) #clk_apll I2S_CLKM_DIV_NUM integer clock divider
   		return