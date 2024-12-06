from testcase.performanceCase.CONFIG.config_ptest import PtestConfig
from baselib.loglib.log_csv import csvreport
from baselib.loglib.log_lib import *
from baselib.instrument.awg import awg
from baselib.instrument.eps import eps
from baselib.instrument.dm  import dm
from baselib.instrument.mdo import mdo
from hal.rtc_clock import RTC_CLK
from hal.Init import HALS
import pandas as pd
import numpy  as np
from testcase.performanceCase.REF.ref_ptest import LdoPtest

class ClkPtest(object):
	def __init__(self, channel, chipv):
		self.channel = channel
		self.chipv 	 = chipv
		self.chip 	 = HALS(channel, chipv)

	def connect_instrument(self,instrument=['EPS','OSC']):
		'''
		:brief:
			Communication between instrument and PC by USB-GPIB interface
		:param:
			- eps: supply diff voltage
		'''

		if 'OSC' in instrument:
			loginfo('OSC')
			self.tek = mdo()
		if 'EPS' in instrument:
			loginfo('EPS')
			self.myeps    = eps()
		if 'AWG' in instrument:		
			loginfo('AWG')
			self.myawg    = awg()
		if 'DM_V' in instrument:
			loginfo('DM_V')
			self.mydm_vol = dm(num_of_machine=0)
		if 'DM_C' in instrument:
			loginfo('DM_C')
			self.mydm_cur = dm(num_of_machine=1)
			self.mydm_cur.get_result('IDC')
	def clk_export(self, RTC_DEBUG_chl = 2, CLK_OUT_chl = 1):
		'''
		:brief:
			export the clk to GPIO and use scope capture the waveform
		:param:
			- RTC_DEBUG_chl: for 32K, 150K
			- CLK_OUT_chl:   for 8M, 40M
		'''		
		'''XTAL_32K'''
		raw_input('32K:Connect probe to touch_padD%d' % RTC_DEBUG_chl)		
		if self.chip.chipv == 'CHIP722':
			dac_ls  = dgm_ls = range(0,8)
			curr_ls = range(0, 8)
			dbuf_ls = [0]

		for dac in dac_ls:
			for curr in curr_ls:
				for dbuf in dbuf_ls:					
					self.chip.rtc_clk.set_32k(dac = (curr<<3)+dac, dres = 3, dgm = dac, dbuf = 0)
					self.chip.rtc_clk.start_32k()
					getattr(self.chip.rtc_debug,'TOUCH_PAD%d' % RTC_DEBUG_chl)(0,4,0)
					print (curr<<3)+dac, dac,curr,dbuf
					raw_input('save pic ..')		
		'''150K'''
		raw_input('150k:connect probe to touch_pad%d' % RTC_DEBUG_chl)
		getattr(self.chip.rtc_debug,'TOUCH_PAD%d' % RTC_DEBUG_chl)(0, 5, 0)
		
		'''8M'''
		raw_input('8M:connect probe to clk_out%d' % CLK_OUT_chl)
		self.chip.rtc_clk.clk_8m_en()
		self.chip.rtc_debug.CLK(14, XTAL_40M_chl, 1) # pull to GPIO_20

		'''40M'''
		raw_input('40m:connect probe to clk_out%d' % CLK_OUT_chl)
		self.chip.rtc_debug.CLK(5, XTAL_40M_chl, 1) # pull to GPIO_20
  	
  	def diff_vdd_clk(self, vdd_ls=[2.63,2.65,2.7,3.0,3.3,3.6]):
		'''
		:brief:
			config diff vdd test the freq of 150K and 8M
		:param:
			- vdd_ls: vdd supply
		'''	  		
  		log = csvreport('/CLK/diff_vdd_clk')
  		col_ls = ['VDD(V)', 'FREQ_150K', 'FREQ_8M']
  		self.myeps = eps()
  		for vdd in vdd_ls:
  			val_ls=[]
  			self.myeps.pwr(vdd, 0.5)
  			raw_input('chipen cntl...')
  			self.chip = HALS(self.channel)
  			self.chip.rtc_clk.clk_8m_en()
  			cyc_150k = int(self.chip.rtc_clk.get_clk_calibration(0))
			cyc_8m   = int(self.chip.rtc_clk.get_clk_calibration(1)) 	# 8m/256
			freq_150k = (1000000 << 19) / cyc_150k
			freq_8m   = (1000000 << 19) / cyc_8m * 256
			val_ls = [vdd, freq_150k, freq_8m]
			log.write_value(col_ls, val_ls)
		log.flush_line()
		self.myeps.pwr(0, 0.5)

	def startup_xtal32k(self, dbuf = 1, dac = 3, dres = 3, touch=1):
		'''
		:brief:
			Read 32k_Xtal Startup time and Frequency
		:param:
			- CHIP722: dbuf:0~1, dac:0~7, dres:0~7
			- ESP32:   touch:0~7
		'''
		if self.chipv == 'ESP32':
			Startup_32K_str = self.channel.req_com("get_xtal_startup_time %d 1 3 0" % touch, 1)

		elif self.chipv == 'CHIP722':
			Startup_32K_str = self.channel.req_com("get_xtal_startup_time %d %d %d %d" % (dbuf, dac, dres, dac), 1)		
		time.sleep(2)
		cyc_32k = self.chip.rtc_clk.get_clk_calibration(2)
		try:
			type(int(cyc_32k))==type(1)
			if int(cyc_32k)==0:
				freq_32k=0
			else:
				freq_32k=(1000000 << 19) / int(cyc_32k)
		except:
			freq_32k=cyc_32k
		Startup_32K = filter(str.isdigit, Startup_32K_str)
		logwarn(['32K_STARTUP(us)','FREQ_32K'], [Startup_32K, freq_32k])
		return [['32K_STARTUP(us)','FREQ_32K'], [Startup_32K, freq_32k]]

	def freq_8m_150k(self):
		'''
		:brief: 
			Read 150K and 8M CLK Frequency
		:param:
			clk_ls=[0,1]: 0:150K, 1:8M/256
		'''	
		clk_ls=[0,1]			
		if self.chipv == 'ESP32' or self.chipv == 'CHIP722':
			self.chip.rtc_clk.clk_8m_en(1,1)
			time.sleep(1)
			clk_freq_list=['','']
			for cal_num in clk_ls:
				for i in range(3):
					freq_temp = self.chip.rtc_clk.get_clk_calibration(cal_clk=cal_num)
					if freq_temp == '':
						time.sleep(1)
						print 'returns %s, wait a second'%freq_temp 
					else:
						print 'returns %s, data recorded'%freq_temp 
						if int(freq_temp)==0:
							clk_freq_list[cal_num]=0
							break
						else:
							if cal_num == 1: clk_freq_list[cal_num]=(1000000 << 19) / int(freq_temp)*256
							else:            clk_freq_list[cal_num]=(1000000 << 19) / int(freq_temp)
							break
			col_ls = ['FREQ_150K', 'FREQ_8M']
			val_ls = clk_freq_list
			logwarn(col_ls,val_ls)				
			return [col_ls,val_ls]

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
		return [reg_read, freq_inHz]

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
		val_reg_l = [default_reg]
		val_frq_l = [original_read]
		for i in check_points:
			reg_read,freq_read = self.clk_freq_read(clk_type=clk_type,dreg=i)
			val_reg_l.append(reg_read)
			val_frq_l.append(freq_read)
		data_table = pd.DataFrame(data={'reg':val_reg_l,'freq':val_frq_l})
		return data_table

	def startup_32kxtal(self,touch_dac_val = 0,oldBin=False): 
		'''
		:brief:
			Crystal startUp function
		'''
		timeout=1
		if oldBin is False:
			self.channel.req_com("rtc_clk_32k_set 1 3 0",timeout)
			self.channel.req_com("rtc_clk_32k_ext_dac_set %d"%(touch_dac_val),timeout)
			self.channel.req_com("rtc_clk_32k_enable 1",timeout)
			time.sleep(1)
			for i in range(2):
				returnVal = self.channel.req_com("rtc_clk_cal 2 128", timeout)
		else:
			if self.chipv=='CHIP722':
				returnVal = self.channel.req_com("get_xtal_startup_time 1 3 3 3",timeout)
			elif self.chipv=='ESP32':
				returnVal = self.channel.req_com("get_xtal_startup_time 0 1 3 0",timeout)
		return returnVal



	def sleep_test(self, t_slp=10000, clk_op=2):
		#self.channel.req_com('get_xtal_startup_time 1 3 3 3',1)
		self.chip.rtc_clk.rtc_slow_clk_select(clk_op)
		time.sleep(1)
		self.chip.rtc_clk.clk_8m_en(1)
		loginfo('"clk12m_rtc" export to CLKOUT2 (DAC2)')
		self.chip.HWREG.RTC_IO.RTC_DEBUG_SEL.reg_rtc_debug_12m_no_gating=1
		self.chip.rtc_debug.TOUCH_PAD1(0,0,0)
		#self.chip.rtc_debug.CLK(14,3,1)
		#loginfo('"8MD256" export to TOUCH_PAD1')
		#self.chip.rtc_debug.TOUCH_PAD1(0,6,0)
		self.chip.HWREG.RTC_CNTL.RTC_CLK_CONF.reg_ck8m_force_pu=1
		self.chip.rtc_sleep.rtc_timer_wakeup(0,t_slp)
		self.chip.rtc_sleep.special_sleep(0x3d,8,0)
		self.channel.start_mmd()


	def osc_8m(self, t_slp=32768*10, clk_op=2, slp_md=[0, 0x3d],read_times=1000, folw_8m=1):
		'''
		:param:
			- t_slp: sleep time
			- clk_op:
		        - 0: RTC_SLOW_FREQ_RTC 150K
		      	- 1: XTAL_32K
		        - 2: 8MD256
		    - slp_md: 0: lightsleep; 0x3d: deepsleep
		    - read_times: freq read times
		'''
		freq_ls=[]
		freq_pd=[]
		if clk_op==2:
			row=0
			cal_clk=1
			div=256
			clk_md='8M'
		elif clk_op==1:
			row=4
			cal_clk=2
			div=1
			clk_md='XTAL_32K'
			self.chip.rtc_clk.x32k_startup_time(1,3,3,3)
			time.sleep(1)
		elif clk_op==0:
			row=5
			cal_clk=0
			div=1
			clk_md='150K'
		self.connect_instrument(['DM_V'])
		self.ldo  = LdoPtest(self.channel, self.channel, self.chipv, mydm_vol=self.mydm_vol)
		self.chip.rtc_clk.clk_8m_en(1)
		time.sleep(2)
		for i in range(read_times):
			freq=(1000000 << 19)/float(self.chip.rtc_clk.get_clk_calibration(cal_clk))*div
			freq_ls.append(int(freq))
		data=np.array(freq_ls)
		rd_8m = ['FREQ', data[0], data.mean(), data.min(), data.max(), data.std()]
		freq_pd.append(pd.DataFrame(['TYP', 'VAL', 'MEAN', 'MIN', 'MAX', 'STD']))		
		freq_pd.append(pd.DataFrame(rd_8m))
		self.chip.rtc_clk.rtc_slow_clk_select(clk_op)
		time.sleep(1)

		loginfo('"8MD256" export to TOUCH_PAD1')
		self.chip.HWREG.RTC_IO.RTC_DEBUG_SEL.reg_rtc_debug_12m_no_gating=1
		self.chip.rtc_debug.TOUCH_PAD1(0,row,0)
		self.chip.HWREG.RTC_CNTL.RTC_CLK_CONF.reg_ck8m_force_pu=1
		
		print self.chip.HWREG.RTC_CNTL.RTC_REG.reg_rtc_dbias_wak
		print self.chip.HWREG.RTC_CNTL.RTC_REG.reg_dig_reg_dbias_wak
		print self.chip.HWREG.RTC_CNTL.RTC_BIAS_CONF.reg_dbg_atten
		# self.tek.clean()
		# f_osc_slp=self.tek.meas(mod='MEASU',_type='FREQ')
		# f_osc=pd.DataFrame(np.array(f_osc_slp))
		# freq_pd.append(f_osc)
		# self.tek.wait()
		if folw_8m:
			self.chip.HWREG.RTC_CNTL.RTC_OPTIONS0.reg_bias_sleep_folw_8m=0
			print 'folw_8m=0'
			wait_cycle=5000
			rtc_timer2_addr = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__addr
			touch_start_wait_lsb = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__reg_ulpcp_touch_start_wait_lsb
			touch_start_wait_msb = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__reg_ulpcp_touch_start_wait_msb		
			self.chip.MEM.wrm(rtc_timer2_addr, touch_start_wait_msb, touch_start_wait_lsb, wait_cycle)
		


		self.ldo.vref(adc2_chl=7,atten_ls=[],slt_ls=range(2,3))
		for slp in slp_md:
			self.chip.rtc_sleep.rtc_timer_wakeup(0,t_slp)
			self.chip.rtc_sleep.sleep(slp,8,0)
			time.sleep(2)
			# self.tek.clean()
			# f_osc_slp=self.tek.meas(mod='MEASU',_type='FREQ')
			# f_osc_s=pd.DataFrame(np.array(f_osc_slp))
			# freq_pd.append(f_osc_s)
			logwarn(self.chip.HWREG.RTC_CNTL.RTC_RESET_STATE.reset_cause_appcpu)
			# self.channel.start_mmd()
			# raw_input('wait...')
			print self.chip.HWREG.RTC_CNTL.RTC_REG.reg_rtc_dbias_slp
			print self.chip.HWREG.RTC_CNTL.RTC_REG.reg_dig_reg_dbias_slp
			print self.chip.HWREG.RTC_CNTL.RTC_BIAS_CONF.reg_dbg_atten

		# freq_8m=pd.concat(freq_pd,axis=1)
		# freq_8m.columns=['MODE','READ_%s'%clk_md, 'OSC_%s'%clk_md, 'OSC_LSLP', 'OSC_DSLP']
		# freq_8m.to_csv('log/freq_8m_sleep_wake.csv', )
		# return freq_8m

	def xtal32k_osc(self,dac_ls=range(4),dres_ls=range(4),dbias_ls=range(4),touch=0):
		'''
		ESP32 ECO XTAL32K TEST
		'''
		self.connect_instrument(['EPS','OSC','AWG'])
		self.cfg  = PtestConfig(self.channel, self.channel, chipv=self.chipv, myeps=self.myeps, myawg=self.myawg)
		log= csvreport('32k_cfg_sweep')
		typ_ls=['FREQ', 'HIGH', 'LOW','PDU']
		for dac in dac_ls:
			for dres in dres_ls:
				for dbias in dbias_ls:
					loginfo('dac:%d dres:%d dbias:%d'% (dac,dres,dbias))
					self.cfg.chip_power_on()
					self.chip.rtc_debug.TOUCH_PAD0(0,4,0)
					if self.chipv == 'ESP32':
						Startup_32K_str = self.channel.req_com("get_xtal_startup_time %d %d %d %d" % (touch,dac,dres,dbias))
						time.sleep(1)
					else:
						pass
					val_ls=['%d_%d_%d'%(dac,dres,dbias),Startup_32K_str]
					for typ in typ_ls:
						val=self.tek.meas('IMMED',typ)
						self.tek.wait()
						val_ls.append(val[1])
					log.write_value(['CFG_DAC_DRES_DBIAS','STARTUP']+typ_ls, val_ls)
					log.flush_line()
					self.cfg.chip_power_off()