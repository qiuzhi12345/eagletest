from testcase.performanceCase.CONFIG.config_ptest import PtestConfig
from testcase.performanceCase.CLK.clk_ptest import ClkPtest
from baselib.instrument.dm import dm
from baselib.instrument.awg import awg
from baselib.instrument.eps import eps
from baselib.loglib.log_lib import *
from hal.Init import HALS
from hal.common import *

class SleepPtest(object):
	def __init__(self,channel,chipv, irc):
		self.channel = channel
		self.chipv 	 = chipv
		self.chip 	 = HALS(self.channel, self.chipv)
		self.irc     = irc			

	def leakage_curr(self, vdd):
		'''measure shutdown current under given vdd voltage

		'''
		self.irc.supl_reset(volt=vdd,ilim=2)   #supply reset
		time.sleep(1)
		curr_en0 = self.irc.cur_meas(rng='MIN')*1e6

		self.irc.sng_edge(volt=vdd,edge='fall',puls_width=1) #chip_pu on and off
		curr_en10 = self.irc.cur_meas(rng='MIN')*1e6    
		return ['I_EN0(uA)', 'I_EN10(uA)'], [curr_en0, curr_en10]

	def sleep_buf(self, en=1):
		'''config bandgap buffers to assist sleep wakeup
		
		:param en: 1 on, 0 off
		'''
		self.chip.HWI2C.ulp.ir_force_xpd_ref_out_buf = en
		self.chip.HWI2C.ulp.ir_force_xpd_vgate_buf   = en

	def light_slp_config(self, delay, typ='IDC', slp_mode = 0x0, wakeup_opt = 0x8,
		dbg_atten = 0,rtc_dbias = 0, dig_dbias = 4, slp_time = 2*1E5, pull_ldo=0,folw_8m=False):
		'''
		:brief:
			lightsleep Current or DigLDO Voltage test config
		:param: 
			- delay 	: after chip go to sleep wait times test the voltage or current
			- typ 		: 'IDC' or 'VDC' for dm instrument
			- dm_n		: 'mydm_cur' or 'mydm_vol' for dm instrument
			- slp_time	: lightsleep time = slp_time * (1.0/freq_150k)
		'''			
		loginfo('chip is awake')
		self.chip.HWREG.RTC_CNTL.RTC_TIMER1.xtl_buf_wait=200
		logwarn(self.chip.HWREG.RTC_CNTL.RTC_TIMER1.xtl_buf_wait)
		'''Read 150k clk actual Freq and Config lightsleep delay time'''
		for i in range(1,10):
			clk=self.chip.rtc_clk.get_clk_calibration(0)
			if clk=='0':
				self.chip.rtc_clk.get_clk_calibration(1)
				continue
			else:
				break
		freq_150k   = (1000000 << 19) / int(self.chip.rtc_clk.get_clk_calibration(0))
		delay_real = (1.0/freq_150k * slp_time)
		loginfo('expect actal sleep time %.2f'%delay_real)
		'''DEBUG: FLOW 8M=0'''
		if folw_8m:
			self.chip.HWREG.RTC_CNTL.RTC_OPTIONS0.reg_bias_sleep_folw_8m=0
			print 'folw_8m=0'
			wait_cycle=5000
			rtc_timer2_addr      = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__addr
			touch_start_wait_lsb = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__reg_ulpcp_touch_start_wait_lsb
			touch_start_wait_msb = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__reg_ulpcp_touch_start_wait_msb		
			self.chip.MEM.wrm(rtc_timer2_addr, touch_start_wait_msb, touch_start_wait_lsb, wait_cycle)

		pd_cur_bias_slp=1 if typ =='IDC' else 0
		self.chip.power.sleep_cur_config(pd_cur_deep_slp=pd_cur_bias_slp, bias_slp_deep_slp=pd_cur_bias_slp, 
										 dbg_atten_deep_slp=dbg_atten,    dbg_atten_monitor=dbg_atten,
										 pd_cur_monitor=0,                bias_slp_monitor=0)		
		time.sleep(0.5)
		self.chip.power.lightsleep_cur(dbg=dbg_atten,dig_dbias=dig_dbias,slp_mode=slp_mode,slp_time =150000*2,pull_ldo =pull_ldo)		

		loginfo('now sleep for %ss'%(slp_time/100000.0))
		# func = getattr(self, dm_n)
		time.sleep(1)
		if typ == 'IDC':
			m_slp = self.irc.cur_meas(rng='MAX')*1e3
		elif typ == 'VDC':
			m_slp = self.irc.vol_meas()

		loginfo('Reads %s %s'%(typ,m_slp))
		loginfo('Will wait for another %.2fs before wakeup'%(delay_real-delay))
		time.sleep(delay_real-delay)
		return m_slp

	def light_slp_vol_cur(self, adc2_chl, delay, curr_volt, slp_mode=0, vdd=3.3, hard=1, 
						 mb=0, chip=0, mctl=None):
		'''Measure lightsleep Current or DigLDO Voltage

		:param curr_volt: 1-Current test 2-Voltage test
		:param hard:      0-chip boot at 3.3V then down to vdd set
			              1-vdd boot with vdd set
		:param mb: 	      0-for signalboard
			              1-for multiboard  
		:param mctl:      pass multiboard control if testing w/ multiboard
		'''
		def chip_is_responding():
			'''read chipv to check chip is awake or not
			
			:return: True: awake, False: fault
			'''
			check_chipv=CHIP_INFO(self.channel).get_chipv()
			return True if check_chipv==self.chipv else False

		def chip_reset(vdd, hard, chip, mb, mctl, pull_ldo):
			'''function to reset chip and pull digital voltage to pad if required
			'''
			if mb:
				self.mctl = mctl
				self.mctl.mcu_power_reset(chip_n=chip, irc=self.irc, volt=vdd, ilim=3, hard=hard, timeout=2)
			else:
				self.irc.chip_reset(volt=vdd,hard=hard,hard_vth=2.8,en_awg=True)
			time.sleep(1)
			logerror("Reseted chip!!!")
			if pull_ldo:
				self.chip.rtc_debug.set_test_mux(1,2)				# set mux select Dig_LDO 
				self.chip.rtc_debug.pull_internal_voltage(adc2_chl)	# pull to adc2_chl0

		def check_if_wakeup():
			'''check if chip wakes up from sleep
			'''
			wakeup_try  = 0
			while getattr(self.chip.rtc_clk.get_clk_calibration(2),'isdigit')() is False and wakeup_try<=3: 
				loginfo('not awake yet, wait another second')
				wakeup_try = wakeup_try +1
				time.sleep(1)
				if wakeup_try == 3:
					loginfo('tried 3x, not responding, will reset chip')
					dead_info ='%s is %s'%(mode[:4], func())
					logerror(dead_info)
					chip_reset(vdd=vdd, hard=hard, mb=mb, chip=chip, mctl=mctl, pull_ldo=pull_ldo)		
					return dead_info
			else:
				return 'True'

		col_ls, val_ls = [],[]

		if self.chipv == 'ESP32':
			pass		
		elif self.chipv == 'CHIP722':
			if curr_volt == 1:		# Current test
				mode = 'CURR(mA)'
				typ  = 'IDC'
				func = self.irc.cur_meas

				slp_time      = 200000
				dbg_dbias     = [(7,0),(6,0), (3,0), (0,1), (0,5)]
				pull_ldo      =0
			elif curr_volt == 2: 	# Voltage test
				mode = 'VOLT(V)'
				typ  = 'VDC'
				func = self.irc.vol_meas
				
				slp_time      = 200000
				dbg_dbias     = [(7,0),(6,0), (3,0), (0,1), (0,5)] 	# [(3,0), (3,1), (3,2), (0,0), (0,1), (0,2), (0,4), (0,5), (0,6)]
				pull_ldo      = 1	                                # has to be enabled for voltage mux-out
				self.chip.rtc_debug.set_test_mux(1,2)				# set mux select Dig_LDO 
				self.chip.rtc_debug.pull_internal_voltage(adc2_chl)	# pull to adc2_chl0	

			for dbg,dbias in dbg_dbias:
				loginfo('... TESTing: Light Sleep Current & Voltages ...')
				col_ls.append('%s_LSLP_%d_%d%s' % (typ[0],dbg,dbias,mode[4:]))
				col_ls.append('%s_WAKE_%d_%d%s' % (typ[0],dbg,dbias,mode[4:]))

				'''check if chip is responding, if not will force reset by chip_pu'''
				rpt=0
				while not chip_is_responding() and rpt<=3:
					if rpt == 3:
						logwarn("Chip not responding... test item to be skipped!!!")
						val_ls+=['SKIP','SKIP']
						break
					chip_reset(vdd=vdd, hard=hard, mb=mb, chip=chip, mctl=mctl, pull_ldo=pull_ldo)		
					rpt+=1
				else:
					val = self.light_slp_config(delay, slp_mode = slp_mode, typ = typ, dbg_atten = dbg, dig_dbias = dbias, 
						slp_time=slp_time, pull_ldo =pull_ldo)
					val_ls.append(val)
				
					time.sleep(1)
					wake_info = check_if_wakeup()
					val_ls.append(wake_info)

			logwarn(zip(col_ls, val_ls))			
			return [col_ls, val_ls]

	def wifipd_curr(self, vdd=3.3,dbg=0,dig_dbias=4,slp_mode_ls=[0x0, 0x40], slp_s=2):
		'''
		'''
		loginfo('... TESTing: Light Sleep Wifi pd Current ...')
		Ipvt_slp=[]
		for slp_md in slp_mode_ls:
					
			self.chip.power.sleep_cur_config(pd_cur_deep_slp=1, bias_slp_deep_slp=1, 
				                             dbg_atten_deep_slp=dbg, dbg_atten_monitor=dbg,
				                             pd_cur_monitor=0, bias_slp_monitor=0)
			time.sleep(0.5)
			self.chip.power.lightsleep_cur(dig_dbias=dig_dbias,slp_mode=slp_md,slp_time =150000*slp_s,pull_ldo = 0)
			time.sleep(0.5)
			# I1 = float(self.mydm_cur.get_result('IDC'))
			I1 = self.irc.cur_meas()

			time.sleep(slp_s+3)
			# self.cfg.reset_chip(adc2_chl=7,vdd=3.3,hard=1,mb=0,times=2,o_code=False)
			Ipvt_slp.append(I1*1e3)
		col_ls=['I_LSLP_WFPD0(mA)', 'I_LSLP_WFPD1(mA)', 'I_LSLP_WF_D(mA)']
		val_ls=Ipvt_slp+[Ipvt_slp[0]-Ipvt_slp[1]]
		return col_ls, val_ls

	def deep_slp_cur(self,slp_mode = 0x7f, pd=7, rtc_dbias=0, dig_dbias=0, dbg=15):
		''' Measure deepsleep Current
		
		:note: not configured for wakeup			
		'''
		if self.chipv == 'ESP32':
			pass
		elif self.chipv == 'CHIP722':
			'''below commands for CHIP722_m1'''
			logwarn('... TESTing: Deep Sleep Current ...')
			self.chip.power.sleep_cur_config(pd_cur_deep_slp=1, bias_slp_deep_slp=1, 
				                             dbg_atten_deep_slp=dbg, dbg_atten_monitor=dbg,
				                             pd_cur_monitor=0, bias_slp_monitor=0)
			time.sleep(0.5)
			self.chip.rtc_sleep.special_sleep(slp_mode, 0, 0) 		
			time.sleep(2)
			curr_D = self.irc.cur_meas(rng='MIN')

			logwarn(['I_DSLP(uA)'] ,[curr_D*1e6])
			return [['I_DSLP(uA)'] ,[curr_D*1e6]]

	def sleep_wake_esp32(self,sleep_sec=10, chip_n=1):
		'''
		:brief:
			For ESP32 deepsleep & lightsleep wakeup test under High/Low temper & voltage
		:param:
			- sleep_sec: sleep time(s)
			- chip_n: chip number
		'''
		col_ls=['LITSLP%d'%chip_n, 'DEPSLP%d'%chip_n]
		val_ls=[]
		# raw_input('supply %rV'% vdd)		
		loginfo('lightsleep test...')	
		self.chip.rtc_clk.rtc_slow_clk_select(0) #0:150k,1:32k,2:8M/256
		self.chip.rtc_sleep.rtc_timer_wakeup(0,150000*sleep_sec)
		self.chip.rtc_sleep.special_sleep(slp_mode=0, wakeup_opt=8, reject_opt=0)
		time.sleep(sleep_sec+1)
		clk_150 = self.chip.rtc_clk.get_clk_calibration(0)
		val_ls.append(clk_150)
		
		loginfo('deepsleep test...')
		self.chip.rtc_clk.rtc_slow_clk_select(0) #0:150k,1:32k,2:8M/256
		self.chip.rtc_sleep.rtc_timer_wakeup(0,150000*sleep_sec)
		self.chip.rtc_sleep.special_sleep(slp_mode=0x3f, wakeup_opt=8, reject_opt=0)
		time.sleep(sleep_sec+1)
		clk_150 = self.chip.rtc_clk.get_clk_calibration(0)
		val_ls.append(clk_150)
		logwarn(col_ls,val_ls)
		return [col_ls,val_ls]

	def gotosleep_32kxtal(self,chip_slt,opD=0,slp_time=1):
		'''
		:brief:
			just for 32kxtal test,small function to put chip into sleep
		'''
		#Put chip into deep-sleep      
		time.sleep(0.2)
		timeout=1
		sleepCheck = 'initial'
		TryTimer   = 0

		for TryTimer in range(9):
			if sleepCheck == '':
				break
			else:
				self.channel.req_com("rtc_clk_slow_freq_set 1",timeout)
				if opD == 0:   self.channel.req_com("slp_cnt_wakeup 0 %d"%(slp_time*60*32768),timeout)
				elif opD == 1: self.channel.req_com("slp_cnt_wakeup 0 0xffffffff",timeout) #slp for 36 hours 
				elif opD == 3: self.channel.req_com("slp_cnt_wakeup 1 0xffffffff",timeout) #slp for 72 hours
				elif opD == 6: self.channel.req_com("slp_cnt_wakeup 3 0xffffffff",timeout) #slp for 6 days
				#Export 32K to IO2         
				# self.channel.req_com("TOUCH_PAD2_DEBUG_CFG 0 4 0",timeout)
				# self.channel.req_com("TOUCH_PAD0_DEBUG_CFG 0 4 0",timeout)
				# loginfo('CHIP#%s exported XTAL_32K CLK to IO2'%(chip_slt))
				#Enter Sleep
				#self.channel.req_com("slp_cnt_wakeup 0 0x6666666",timeout)
				self.channel.req_com("rtc_sleep 0x3d 8 0",timeout)
				loginfo('CHIP#%s Round#%s sets sleep time: %smins' % (chip_slt,TryTimer,slp_time))
				#check if really falls asleep
				for i in range(2):
					sleepCheck=self.channel.req_com("rtc_clk_cal 2 128", timeout)
				loginfo('CHIP#%s sleepCheck:%s'%(chip_slt,sleepCheck))
				TryTimer = TryTimer + 1 
		#Report sleep status
		if TryTimer <= 9 and (sleepCheck == ''):
			loginfo('CHIP#%s is sleeping' % (chip_slt))
			slpChkInfo = 'Sleeping Tried%sx'%TryTimer
		else:
			loginfo('CHIP#%s tried 10 times, wont sleep' % (chip_slt))
			slpChkInfo = 'Tried 10x Failed'
		slpCheck=slpChkInfo
		put2slp=time.asctime()
		return slpCheck , put2slp

	def wakeupcheck_32kxtal(self,chip_slt = 0):
		'''
		:brief:
			just for 32kxtal test, small funciton to check chip status if wakesup
		'''

		timeout=1
		rpt_32k=0
		wkFromSlp=time.asctime()
		#Use frequency read to check if wakeup     
		time.sleep(0.2)                    
		freq=self.channel.req_com("rtc_clk_cal 2 128", timeout)     # freq = self.chip.rtc_timer.get_clk_calibration(2)
		if freq=='':
			error_ls.append(chip_slt)
			noReturn_freq_ls.append(chip_slt)
			freq_lis='No return'
			loginfo('CHIP#%s reads freq: NO RETURN!!'%(chip_slt))   
		elif freq=='0':
			while freq=='0' and  rpt_32k<5:
				logwarn('repeat read 32K freq...')
				freq=self.channel.req_com("rtc_clk_cal 2 128", timeout)
				rpt_32k+=1
			freq_lis=freq
		else:
			freq_lis=freq
			loginfo('CHIP#%s reads freq:%s'%(chip_slt,freq))   
		#Return wakeup cause
		time.sleep(0.2)        
		wkcus=self.channel.req_com('rtc_wakeup_cause',timeout)
		if wkcus != '8':
			wk='No return'
			loginfo('CHIP#%s wakeup_cause: No RETURN!!'%(chip_slt))
			noReturn_wk_ls.append(chip_slt)
		else:
			loginfo('CHIP#%s wakeup_cause:%s'%(chip_slt,wkcus))                 
			wk=wkcus

		if (freq =='' or freq=='0') and (wkcus != '8'):
			self.clk  = ClkPtest(self.channel,self.chipv)
			startUp = self.clk.startup_32kxtal(touch_dac_val=touch_dac_val,oldBin=oldBin)
			if startUp =='':
				tryToFix = 'SSorCD'
				loginfo('Still Sleeping or Completely Dead!!')
			else:
				tryToFix = startUp[:-30]
				loginfo('Revived and startUp time is %s'%startUp[:-30])
		else:
			tryToFix = 'He is good'
		return tryToFix,wkFromSlp,freq_lis,wk