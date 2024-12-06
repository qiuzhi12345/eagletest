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

class Stability(object):
	'''below scripts written based on chip722, not tested for ESP32 or other chips yet'''
	def __init__(self, channel, chipv = "CHIP722"):
		self.chipv    = chipv
		self.channel  = channel
		self.chip     = HALS(channel,chipv)

	def prep_gpib(self):
		self.mydm = dm()
		self.myeps = eps()

	def open_buf(self,ref_buf=1,vgate_buf=1):
		'''open buffer for bandgap driver capability'''
		if ref_buf == 1 or vgate_buf == 1:
			self.chip.HWI2C.ulp.ir_force_xpd_ref_out_buf = ref_buf
			self.chip.HWI2C.ulp.ir_force_xpd_vgate_buf   = vgate_buf
			loginfo('BUF REF=%d VGATE=%d'%(ref_buf,vgate_buf))
		else:
			loginfo('BUF NOT OPEN')
		return

	def parameter_config(self,wait_time=2,try_loop=20):
		''''''
		self.wait_time=wait_time
		self.try_loop =try_loop

	def clock_read(self,clk_type=0):
		'''reads slow clock mux by default
		:param:
			- clk_type: 
				- 0: esp32:slow clock mux; chip722:150K
				- 1: 8M256   
				- 2: 32KXTAL 
		'''
		wait_time = self.wait_time
		try_loop = self.try_loop
		try_time = 0
		case_info = 0
		while True:
			slow_clock_check = self.chip.rtc_clk.get_clk_calibration(clk_type)
			if slow_clock_check == '' and try_time < try_loop:
				try_time += 1
				loginfo('CHIP is sleeping or not responding, wait another %ds'%wait_time)
				time.sleep(wait_time)
			elif slow_clock_check.isdigit() and try_time < try_loop:
				if int(slow_clock_check) != 0:
					slow_clock_check_inHZ = (1000000 << 19) / int(slow_clock_check)
					loginfo('CHIP is awake, reads clock: %.2fKHz'%(slow_clock_check_inHZ/1000.0))
					case_info = 'GOOD'
					return slow_clock_check_inHZ,case_info
				elif int(slow_clock_check) == 0:
					try_time += 1
					loginfo('CHIP is awake, reads slow clock period 0, try another second')
					time.sleep(1)
			elif try_time == try_loop:
				loginfo('Tried %dx, clock reads "%s"'%(try_loop,slow_clock_check))
				case_info = 'BAD'
				# return slow_clock_check, case_info+'_Tried%dx'%try_loop
				return 0, case_info+'_Tried%dx'%try_loop
			else:
				loginfo('CHIP is awake, clock reads "%s"'%slow_clock_check)
				loginfo('Try another time in a second')
				time.sleep(1)
				slow_clock_check2 = self.chip.rtc_clk.get_clk_calibration(clk_type)
				loginfo('NOW clock freq reads "%s"'%slow_clock_check2)
				case_info = 'TBD'				
				return slow_clock_check2, case_info+'_'+slow_clock_check

	def pst_slp_chk(self):
		'''reads rtc memory to check if chip is awake or alive
		:param:
			- clk_type: 
				- 0: esp32:slow clock mux; chip722:150K
				- 1: 8M256   
				- 2: 32KXTAL 
		'''
		wait_time = self.wait_time
		try_loop = self.try_loop
		try_time = 0
		case_info = 0
		while True:
			pst_slp_chk = self.channel.req_com('rd 0x60008000',1)
			if pst_slp_chk == '' and try_time < try_loop:
				try_time += 1
				loginfo('CHIP is sleeping or not responding, wait another %ds'%wait_time)
				time.sleep(wait_time)
			elif pst_slp_chk == ('cmd not exist!' or '0x0' )and try_time < try_loop:
				case_info = 'GOOD'
				return case_info					
			elif try_time == try_loop:
				loginfo('Tried %dx, RTC MEM reads "%s"'%(try_loop,pst_slp_chk))
				case_info = 'BAD'
				return case_info+'_Tried%dx'%try_loop
			else:
				loginfo('CHIP is awake or alive, RTC MEM reads "%s"'%pst_slp_chk)
				loginfo('Try another time in a second')
				time.sleep(1)
				pst_slp_chk2 = self.channel.req_com('rd 0x60008000',1)
				loginfo('NOW RTC MEM reads "%s"'%pst_slp_chk2)
				case_info = 'TBD'				
				return case_info+'_'+pst_slp_chk2

	def cnt_dwn_timer(self,slp_time,timer_buffer=2,counting=False):
		'''maximum count down time is 10s
		:param: slp_time in mins
		'''
		if slp_time*60 > 10: cntdwn_timer = 10
		else:             cntdwn_timer = int(slp_time*60+0.5) 
		time.sleep(slp_time*60-cntdwn_timer+timer_buffer)
		if counting:
			loginfo('COUNT to %d and will check if chip is up'%cntdwn_timer)
			for i in range(cntdwn_timer):
				print '%d'%(cntdwn_timer-i)
				time.sleep(1)
		else:
			loginfo('%ds later will check if chip is up'%cntdwn_timer)
			time.sleep(cntdwn_timer+1)		

	def pst_slp_blk(self,slp_time):
		slp_timing = time.time()
		loginfo('CHIP is going to sleep for %ss'%(slp_time*60))
		#self.channel.start_mmd()
		'''wakeup counter'''
		self.cnt_dwn_timer(slp_time=slp_time)
		case_info = self.pst_slp_chk()
		wak_timing = time.time()
		loginfo('predict actual sleep time is %.2fs'%(wak_timing-slp_timing))
		return case_info

	'''clock swtich test'''
	def clk_switch_config(self,test_times=100):
		'''test for cpu clcok switching stability
		'''
		self.channel.req_com('cpu_freq_random_test_for_python %d 0'%test_times,1)
		time.sleep(test_times*0.5e-3)   #estimated 14x slow clock cycle is 0.15ms

	def clk_switch_check(self):
		case_info = self.pst_slp_chk()
		logwarn(case_info)
		return case_info

	'''light sleep related tests'''
	def light_sleep_norm_wkup(self,test_type=0,ref_buf=1,vgate_buf=1,xtal_buf_wait=80,dbg=7,dig=0,rtc=0):
		'''
		:param:
			- dbg: dbg_atten
			- rtc: rtc_dbias
			- dig: dig_dbias
		'''
		self.open_buf(ref_buf,vgate_buf)
		self.chip.HWREG.RTC_CNTL.RTC_TIMER1.xtl_buf_wait = xtal_buf_wait
		#self.channel.start_mmd()
		if test_type == 0:
			'''voltage read test'''
			self.chip.rtc_debug.set_test_mux(1,2) # dig_ldo  1,0 rtc_ldo
			self.chip.rtc_debug.pull_internal_voltage(0)   # GPIO 11
			self.channel.req_com('lslp_cur_test 0 8 %d %d %d 400000 232 0'%(dbg,rtc,dig),1)
		elif test_type == 1:
			'''current read test'''
			self.channel.req_com('lslp_cur_test 0 8 %d %d %d 400000 104 0'%(dbg,rtc,dig),1)
		'''com command copy
		lslp_cur_test 0 8 7 0 0 400000 104 0
		lslp_cur_test 0 8 7 0 0 400000 232 0
		lslp_cur_test 1 8 15 0 0 400000 104 0
		'''
		return

	def light_sleep_mac_wkup_config(self,slp_time=1):
		'''test for light sleep wake up stability by mac
		'''
		timeout =1
		#slow_clock_read= 93206
		slow_clock_read,case_info = self.clock_read(clk_type=0)
		#xtal_buf_wait_read=self.chip.HWREG.RTC_CNTL.RTC_TIMER1.xtl_buf_wait
		#logwarn(xtal_buf_wait_read)
		'''setup wakeup time use mac clock'''
		self.channel.req_com('mac_sleep_init %d 4096'%(slp_time*60*slow_clock_read),timeout)
		slp_mode   = 0x7e   #only dig power domain is not turned off
		wakeup_opt = 0x20   #use mac as wakeup source
		reject_opt = 0
		#self.chip.HWREG.RTC_CNTL.RTC_TIMER1.xtl_buf_wait = xtal_buf_wait
		'''use above parameters to put chip into sleep'''
		#self.chip.rtc_sleep.sleep(slp_mode, wakeup_opt, reject_opt)
		self.chip.rtc_sleep.special_sleep(slp_mode, wakeup_opt, reject_opt)

	def light_sleep_mac_wkup_check(self,slp_time=1):
		slp_time = slp_time*2  # timer accuracy issue caused by IDF, to be fixed
		#self.channel.start_mmd()
		case_info = self.pst_slp_blk(slp_time=slp_time)
		return case_info

	'''deep sleep test'''
	def deep_sleep_rtc_mem_config(self,clk_type=0,check_mem_enable=1,ref_buf=1,vgate_buf=1,
							slp_mode=0x67, wakeup_opt=8,reject_opt=0, slp_time=1,dbg=15):
		'''
		:brief:
			test for rtc memory stability under deep sleep
		:param: 
			- slp_time: set sleep time length in mins
			- slp_mode: fast mem check use 0x67
				- if normal sleep wakeup test, use 0x7f
		:command backup:
			- check dbg_atten: self.chip.HWREG.RTC_CNTL.RTC_BIAS_CONF.reg_dbg_atten
		'''
		if check_mem_enable == 1: 
			self.channel.req_com('check_fast_mem 1')
			loginfo('FAST MEM WRITTEN')
		'''open buf option'''
		self.open_buf(ref_buf,vgate_buf)
		'''if use 8M256 as slow clock'''
		if clk_type == 0:
			'''if use 150K as slow clock'''
			self.chip.rtc_clk.rtc_slow_clk_select(0)      #sets slow clock to 150K
			print 'USE 150K as SLOW CLK'
			'''clock read'''
			#slow_clock_read = 93206     #checks slow clock status
			slow_clock_read,case_info = self.clock_read(0)          #checks slow clock status
		elif clk_type == 2:
			'''if use 8M256 as slow clock'''		
			self.chip.rtc_clk.clk_8m_en()                 #enable 8m
			self.chip.rtc_clk.rtc_slow_clk_select(2)      #sets slow clock to 8M256
			print 'USE 8M256 as SLOW CLK'
			'''clock read'''
			slow_clock_read,case_info = self.clock_read(1)          #checks 8M256 status
		'''setup deep sleep time'''
		self.chip.rtc_sleep.rtc_timer_wakeup(0, slp_time*60*slow_clock_read)  #set sleep time length in mins
		'''put chip into deep sleep'''
		self.chip.power.sleep_cur_config(pd_cur_deep_slp=1, bias_slp_deep_slp=1, dbg_atten_deep_slp=dbg, pd_cur_monitor=0, bias_slp_monitor=0, dbg_atten_monitor=dbg)

		self.chip.rtc_sleep.special_sleep(slp_mode, wakeup_opt, reject_opt)
		# dbg=10
		# self.channel.req_com('lslp_cur_test %d 8 %d 0 0 100000 104 0'%(slp_mode,dbg) ,1)

	def deep_sleep_rtc_mem_check(self,slp_time):
		slp_time = 2*slp_time   # timer accuracy issue caused by IDF, to be fixed
		case_info = self.pst_slp_blk(slp_time=slp_time)
		'''check dbg_atten value'''
		dbg_atten_read = self.chip.HWREG.RTC_CNTL.RTC_BIAS_CONF.reg_dbg_atten
		loginfo('DBG ATTEN READ %s'%dbg_atten_read)
		'''check if fast mem check test pass or fail'''
		fast_mem_check = self.channel.req_com('check_fast_mem 0',1)
		reset_cause    = self.channel.req_com('rtc_reset_cause',1)
		if fast_mem_check[0:5] == 'ERROR': 
			logwarn('RTC MEM DEEP SLEEP TEST FAILED')
		elif fast_mem_check == '':
			loginfo('RTC MEM DEEP SLEEP TEST OKAY')
		return '%s_FASTMEM:%s_RESETCAUSE:%s'%(case_info,fast_mem_check[0:5],reset_cause)

	'''loop them all'''
	def stability_loop(self,slp_time=0.2,ref_buf=1,vgate_buf=1,loop_time=200):
		'''
		:param: slp_time: unit in mins
		'''
		wait_time = 2
		try_loop  = 20
		self.parameter_config(wait_time=wait_time,try_loop=try_loop)
		log = csvreport('stability_loop/light_deep_test')
		col_ls = [
				'TEST_TIME',
				'CLK_SIWTCH',
				'LIGHT_MAC',
				'DEEP_MEM'
				]
		for i in range(loop_time):
			vol_ls=[]
			vol_ls.append(i)
			logwarn('CLOCK SWITCH TEST')
			self.clk_switch_config(test_times=100)
			clk_switch=self.clk_switch_check()
			logwarn('LIGHT SLEEP MAC WAKEUP TEST')
			self.light_sleep_mac_wkup_config(slp_time=slp_time)
			light_mac=self.light_sleep_mac_wkup_check(slp_time=slp_time)
			logwarn('DEEP SLEEP MEM CHECK TEST')
			self.deep_sleep_rtc_mem_config(slp_time=slp_time,ref_buf=ref_buf,vgate_buf=vgate_buf)
			deep_mem=self.deep_sleep_rtc_mem_check(slp_time=slp_time)
			vol_ls.append(clk_switch)
			vol_ls.append(light_mac)
			vol_ls.append(deep_mem)
			log.write_value(col_ls,vol_ls)
			log.flush_line()
			#self.clk_switch()
