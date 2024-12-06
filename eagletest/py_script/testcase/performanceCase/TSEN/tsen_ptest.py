# -- coding: utf-8 --
# 中文支持
from baselib.loglib.log_csv import csvreport
from baselib.loglib.log_lib import *
from baselib.instrument.awg import awg
from baselib.instrument.eps import eps
from baselib.instrument.dm import dm
from hal.Init import HALS
from testcase.performanceCase.CONFIG.config_ptest import PtestConfig

class TsenPtest(object):
	"""docstring for TSEN_PTEST"""
	def __init__(self, channel, chipv, irc):
		self.channel = channel
		self.chipv 	 = chipv
		self.chip 	 = HALS(channel, chipv)
		self.irc     = irc

	def _dac_os_relation(self,dac):
		if dac == 5:
			offset = -2
		elif dac == 13 or dac == 7:
			offset = -1
		elif dac == 15:
			offset = 0
		elif dac == 11 or dac == 14:
			offset = 1
		elif dac == 10:
			offset = 2
		return offset 

	def _tsen_read(self, dac=15, div_chop=2, shutdown=False,clk_inv=0,clk_div=3):
		'''processes temperature sensor return value to human readable results

		:param dac: offset value to meet different temperatur range
		:param div_chop: offset chopping options, range 0,1,2,3
		'''
		offset = self._dac_os_relation(dac)
		self.chip.tsen.config(dac=dac, div_chop=div_chop,clk_div=clk_div,clk_inv=clk_inv)
		tsen_adc = self.chip.tsen.read()
		if tsen_adc!='':
			temp_read = 0.4386*int(tsen_adc, 16) - 27.88*(offset) - 20.52
			temp_read = '%.2f'%temp_read
			# val_ls.append("%.2f"%temp_read)
		else: 
			# val_ls.append(Temp_adc)
			temp_read = tsen_adc
		if shutdown:
			self.chip.tsen.close()

		return temp_read

	def _tsen_os_use(self,temp):
		'''give me a temperaure value and I return you a right os config
		'''
		if 	 temp >  80:	tsen_os= (-2,5)
		elif temp < -10: 	tsen_os= (2,10)
		else: tsen_os = (0,15)
		return tsen_os

	def scan_tsen(self, dac_ls = [5,13,15,11,10], xpd_force = 0, clk_inv=0 ,clk_div_ls = range(3,4), 
		chop_ls = [0,1,2,3], adc2_chl = 7, vol_ref = False):
		'''		
		:brief: 
			scan Tsensor under all parameters configuration
		:param:	
			- dac_ls: offset
		'''
		if vol_ref: self.connect_instrument()
		log 	= csvreport("/TSEN/%s_Tsen_scan" % self.chipv)
		ref_log = csvreport("/TSEN/%s_Tsen_vol_ref" % self.chipv)
		offset_mux = [(-2,5), (-1,13), (0,15), (1,11), (2,10)]
		for chop in chop_ls:	
			for clk_div in clk_div_ls:	
				col_ls  = ["chop"]
				temp_ls = ["temp"]
				val_ls  = ["chop%d_clkdiv%d" % (chop,clk_div)]	
				for dac in dac_ls:
					temp = self._tsen_read(dac = dac,clk_inv=clk_inv, clk_div = clk_div, div_chop = chop)
					if vol_ref:
						col_ref = ['CHOP', 'CLK_INV', 'CLK_DIV', 'OFFSET', 'READ', 'TEMPER', 'RP', 'VP', 'VN']						
						self.chip.rtc_debug.pull_internal_voltage(adc2_chl)

						int_vol_l = []   # a list of internal voltages rp, vp, vn
						for i_int_vol in [1,2,3]:					
							self.chip.rtc_debug.set_test_mux(0, i_int_vol)
							int_vol_l.append(self.irc.vol_meas())
						val_ref = [chop, clk_inv, clk_div, offset, val, temp] + int_vol_l

						ref_log.write_value(col_ref, val_ref)						
					val_ls.append(val)
					temp_ls.append(temp)
					col_ls.append("offset%d_dac%d" % (offset,dac))
				log.write_value(col_ls, val_ls)
				log.write_value(col_ls, temp_ls)
		log.flush_line()
		ref_log.flush_line()

	def tsensor(self, adc2_chl=7, tsen_dac_ls = [], atten_ls = [3], adc_dref = [0], temp=25, chop_ls = [0,1,2,3],ref_vol=1):
		'''		
		:brief:
			Measure Tsensor Vref:T_rp T_vp T_vn and pull to adc2_chl
			Read the temperature at diff offset and diff chop 
		:param:	
			- adc2_chl : Pull internal VRef to external ADC2 channel
			             - SingleBoard: 0~9
			             - MultiBoard : CHIP722->7; ESP32->9			
			- tsen_dac_ls : [(offset, dac)]
			                 [(-2,     5), 50~125
			                  (-1,    13), 20~100
			                  ( 0,    15), -10~80
			                  ( 1,    11), -30~50
			                  ( 2,    10)] -40~20
			- atten_ls : [0,1,2,3]; Skip adc read when it is empty
			- adc_dref : [0,1,2,4]
			- temp    : Tsensor Offset selection based on temper, 
			             T> 80: offset=-2
			             T<-10: offset=2
			             else : offset=0			
			- chop_ls  : [0,1,2,3]; Skip chop scan when it is empty
			- ref_vol  : 0: Skip the Vref test, 1:Vref test is included
		'''
		if self.chipv == 'ESP32':
			pass
		
		elif self.chipv == 'CHIP722':
			tsen_col_ls	= ['TSEN_RP', 'TSEN_VP', 'TSEN_VN']		
			tsen_mux_ls = [(0,1), (0,2), (0,3)]
			col_ls, val_ls = [], []
			# if 	 temp >  80:	tsen_os= (-2,5)
			# elif temp < -10: 	tsen_os= (2,10)
			# else: tsen_os = (0,15)
			tsen_os = self._tsen_os_use(temp=temp) #choose correct offset setup option based on target temprature
			if tsen_dac_ls==[]: tsen_dac_ls=[tsen_os]

			if ref_vol:							# MEAS T_rp T_vp T_vn Voltage & ADC2 Internal Read
				self.chip.tsen.config()
				for index,tsen_mux in enumerate(tsen_mux_ls):
					self.chip.rtc_debug.set_test_mux(tsen_mux[0], tsen_mux[1])
					self.chip.rtc_adc2.config()
					for atten in atten_ls:
						self.chip.rtc_adc2.set(atten = atten, pad = adc2_chl, test_pad_en=1)
						for dref in adc_dref:
							self.chip.rtc_adc2.sar2_dref(dref)
							tsen_adc = self.chip.rtc_adc2.read(1)
							val_ls.append(tsen_adc)
							col_ls.append('%s_OS0_ADC_ATN%d_DREF%d' % ((tsen_col_ls[index][:-3]), atten, dref))
					self.chip.rtc_debug.pull_internal_voltage(adc2_chl)	
					val_ls.append(self.irc.vol_meas())
					col_ls.append('%s_os0(V)' % (tsen_col_ls[index]))
				self.chip.MEM.wrm(0x600080b8, 29, 28, 0)			# close mux	

			for tsen_dac in tsen_dac_ls:
				val_tsen = self._tsen_read(dac=tsen_dac[1],div_chop=2) # Config different offset Read Temperature
				val_ls.append(val_tsen)
				col_ls.append('T_OS_%r' % tsen_dac[0])

			for chop in chop_ls:
				val_tsen = self._tsen_read(dac=tsen_os[1],div_chop=chop) # Config diff chop Read Temprature
				val_ls.append(val_tsen)
				col_ls.append('T_CHOP_%r' % chop)

			self.chip.tsen.close()
			self.chip.MEM.wrm(0x600080b8, 29, 28, 0)
			logwarn(col_ls, val_ls)
			return [col_ls, val_ls]

	def theta_ja(self,att_rf=20,hot=15,cool=25, temp=25, log=None, calib=True):
		'''
		:brief:
			Measure package theta-JA /JC /CA
		:param:	
			att_rf: TxTone atten(20,50,80)
			hot: wait for chip heating times: hot*10s
			coll: wait for chip cooling times: cool*10s
			temper: environment temperature
		'''
		logwarn ('''
        ********** Add "rftest" package *********
        1.need copy "rftest" package from RF group
        2."config_ptest.py" add import module:
          from rftest.rflib.rfcal import *
          from rftest.rflib.pbus import *
        *****************************************''')
		def get_power():
			# curr  = float(self.mydm_cur.get_result('IDC'))
			# volt = float(self.mydm_vol.get_result('VDC'))
			curr = self.irc.cur_meas()
			volt = self.irc.vol_meas()
			power = curr*volt			
			return volt,curr,power
		if log ==None:
			log  = csvreport('/TSEN/Theta_JA_txtone_atten%d'%att_rf)
		self.cfg  = PtestConfig(self.channel, self.channel, chipv=self.chipv)
		col_ls = ['temp','TXTONE','TIME','VDD(V)','I(mA)','POWER','T_DIE']
		temp_ls = []
		temp_dw = ['power_down']
		# self.myawg.appl('DC',0,0,0)
		# time.sleep(0.5)
		# self.myawg.appl('DC',0,0,3.3)
		# time.sleep(2)
		self.irc.sng_edge(volt=3.3,edge='rise',puls_width=0.5,timeout=1)

		# if 	 temp >  80:	tsen_os= (-2,5)
		# elif temp < -10: 	tsen_os= (2,10)
		# else: tsen_os = (0,15)
		tsen_os = self._tsen_os_use(temp=temp) #choose correct offset setup option based on target temprature

		temp_0 = self.tsensor(adc2_chl=7, tsen_dac_ls=[tsen_os], atten_ls=[], adc_dref=[0], temp=25, chop_ls=[], ref_vol=0)
		v_0,c_0,p_0 = get_power()

		self.cfg.rf_open(temp,att_rf,adc2_chl=7,vdd=3.3)
		temp_1  = self.tsensor(adc2_chl=7, tsen_dac_ls=[tsen_os], atten_ls=[], adc_dref=[0], temp=25, chop_ls=[], ref_vol=0)

		if calib :
			# volt_1t = float(self.mydm_vol.get_result('VDC'))
			# self.myeps.pwr(6.6-volt_1t,1.5)	
			volt_lt = self.irc.vol_meas()
			self.irc.supl_set(6.6-volt_1t, 1.5)
			loginfo('pre VDD:%.4f'%volt_1t,'set:%.4f'%(6.6-volt_1t))
			v_delta=3.3-volt_1t

		v_1,c_1,p_1 = get_power()
		loginfo('after compensation:%.4f'%v_1)
		temp_ls = ['power_on',temp_0]
		log.write_value(col_ls,[temp,att_rf,'power_on',v_0,c_0*1e3,p_0,temp_0[1][0]])
		log.write_value(col_ls,[temp,att_rf,'txtone_att%d'%att_rf,v_1,c_1*1e3,p_1,temp_1[1][0]])

		for i in range(hot):
			time.sleep(8)
			if calib : 
				# volt_t = float(self.mydm_vol.get_result('VDC'))
				volt_t = self.irc.vol_meas()			
				v_delta += 3.3-volt_t
				# self.myeps.pwr(3.3+v_delta,1.5)	
				self.irc.supl_set(3.3+v_delta, 1.5)

				loginfo('pre VDD:%.4f'%volt_t,'set:%.4f'%(3.3+v_delta))
			v,c,p_h=get_power()
			loginfo('after compensation:%.4f'%v)
			temp_h = self.tsensor(adc2_chl=7, tsen_dac_ls=[tsen_os], atten_ls=[], adc_dref=[0], temp=25, chop_ls=[], ref_vol=0)
			temp_ls.append(temp_h[1])
			log.write_value(col_ls,[temp,att_rf,'hot_%r'%((i+1)*10),v, c*1e3, p_h, temp_h[1][0]])
			log.flush_line()
		# self.myeps.pwr(3.3, 1.5)
		self.irc.supl_set(volt=3.3,ilim=1.5,out=1)
		for j in range(cool):
			# loginfo('power_down....')
			# self.myawg.appl('DC',0,0,0)
			# time.sleep(10)
			# self.myawg.appl('DC',0,0,3.3)
			# time.sleep(1)
			# loginfo('power_on....')
			self.irc.sng_edge(volt=3.3,edge='rise',puls_width=10,timeout=0) #control signal rise from 0 to 3.3V
			v,c,p_c=get_power()
			temp_c = self.tsensor(adc2_chl=7, tsen_dac_ls=[tsen_os], atten_ls=[], adc_dref=[0], temp=25, chop_ls=[], ref_vol=0)
			temp_dw.append(temp_c[1])
			log.write_value(col_ls,[temp,att_rf, 'cool_%r'%((j+1)*10),v, c*1e3, p_c,temp_c[1][0]])
			log.flush_line()
		# self.myawg.appl('DC',0,0,0)
		self.irc.sng_gen(volt=0)
		return temp_ls,temp_dw

	def scan_theta(self,temps=[0,-40],pre_min=30,post_min=60,mins=1, at_wait_min=10,hot=20,cool=15,att_max=100,att_min=0,calib =True):
		'''
		'''
		all_log = csvreport('/TSEN/Theta_JA_txtone_atten100-10')

		def theta_tsen_read(tsen_os):
			'''turn-on chip_pu, read temp-sensor, then turn-off chip_pu
			'''
			self.irc.sng_edge(volt=3.3,edge='rise',puls_width=0.5,timeout=1) #control signal rise from 0 to 3.3V
			temp_0 = self.tsensor(adc2_chl=7, tsen_dac_ls=[tsen_os], atten_ls=[], adc_dref=[0], temp=25, chop_ls=[], ref_vol=0)
			self.irc.sng_gen(volt=0)
			return temp_0

		# self.myeps.pwr(3.3,1.5)
		self.irc.supl_set(volt=3.3,ilim=1.5,out=1)

		temp_ls=[]
		for temp in temps:
			# if 	 temp >  80:	tsen_os= (-2,5)
			# elif temp < -10: 	tsen_os= (2,10)
			# else: tsen_os = (0,15)
			tsen_os = self._tsen_os_use(temp=temp) #choose correct offset setup option based on target temprature

			temp_ls.append(temp)
			for rpt in range(pre_min):
				print 'pre waiting... %dmin '%rpt
				time.sleep(60*mins)
				# self.myawg.appl('DC',0,0,0)
				# time.sleep(0.5)
				# self.myawg.appl('DC',0,0,3.3)
				# time.sleep(2)
				# temp_0 = self.tsensor(adc2_chl=7, tsen_dac_ls=[tsen_os], atten_ls=[], adc_dref=[0], temp=25, chop_ls=[], ref_vol=0)
				# self.myawg.appl('DC',0,0,0)
				temp_0 = theta_tsen_read(tsen_os=tsen_os)
				temp_ls.append('pre_%r'%(temp_0[1][0]))

			for i in range(att_max,att_min,-10):
			    logwarn('atten %d testing...'% i)
			    self.theta_ja(i,hot=hot,cool=cool,temp=temp,log=all_log,calib=calib)
			    time.sleep(at_wait_min*60)
			    print 'wait.....'

			for rpt in range(post_min):
				print 'post waiting...%d min '%post_min
				time.sleep(60*mins)
				# self.myawg.appl('DC',0,0,0)
				# time.sleep(0.5)
				# self.myawg.appl('DC',0,0,3.3)
				# time.sleep(2)
				# temp_0 = self.tsensor(adc2_chl=7, tsen_dac_ls=[tsen_os], atten_ls=[], adc_dref=[0], temp=25, chop_ls=[], ref_vol=0)
				# self.myawg.appl('DC',0,0,0)
				temp_0 = theta_tsen_read(tsen_os=tsen_os)
				temp_ls.append('post_%r'%(temp_0[1][0]))

		print temp_ls
		return temp_ls
