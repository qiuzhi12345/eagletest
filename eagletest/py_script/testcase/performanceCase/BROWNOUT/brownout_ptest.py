from testcase.performanceCase.CONFIG.config_ptest import PtestConfig
from testcase.performanceCase.REF.ref_ptest import LdoPtest
from baselib.loglib.log_csv import csvreport
from baselib.loglib.log_lib import *
from baselib.instrument.eps import eps
from baselib.instrument.awg import awg
from baselib.instrument.dm import dm
from hal.Init import HALS
import numpy as np
import time

class BrownOutPtest(object):
	"""docstring for BROWN_OUT"""
	def __init__(self, channel, chipv):
		# self.connect_instrument()
		self.channel = channel
		self.chipv   = chipv
		self.chip    = HALS(channel, chipv)

	def connect_instrument(self,instrument=['AWG','EPS','DM_C','DM_V']):
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

	def scan_vth_rough(self, vth_ls = range(8), VDD_rg = [2300, 3400], step_mV = 100, repeat = 1):		
		'''
		:brief:
			Rough scan the brownout trig voltage of diff Vth 
		:param:
			VDD_rg: all Vth are same range
		'''			
		detail_pos=[i for i in np.zeros(8)]
		detail_neg=[i for i in np.zeros(8)]
		self.myeps.pwr(3.3, 0.5)
		for idx_vth,vth in enumerate(vth_ls):
			if self.chipv == "ESP32":
				self.chip.rtc_brownout.thres_set(vth)
				thres = self.chip.HWREG.RTC_CNTL.RTC_BROWN_OUT.reg_dbrown_out_thres
				for rpt in range(repeat):
					for vdd in range(VDD_rg[1], VDD_rg[0], -step_mV):
						self.myeps.pwr(vdd/1000.0, 0.5)
						self.chip.rtc_debug.TOUCH_PAD0(is_sensor=0, row=31, bitnum=0)	# "BROWN_OUT_DET" export to TOUCH1
						det = self.mydm_vol.get_result('VDC')
						if float(det) > 1:
							flag = 0
							logwarn(vdd,'V:',det)
							detail_neg[idx_vth]=vdd
							break
						elif float(det) < 1:
							flag = 1
							loginfo(vdd,'V:',det)					
			elif self.chipv == "CHIP722":
				self.chip.HWI2C.ulp.dbrown_out_thres = vth
				thres = self.chip.HWI2C.ulp.dbrown_out_thres
				logwarn('%r_brownout thres set:%r,read:%r' % (self.chipv,vth,thres))				
				for rpt in range(repeat):
					# for vdd in range(VDD_rg[0],VDD_rg[1], step_mV):
					# 	self.myeps.pwr(vdd/1000.0, 0.5)
					# 	self.chip.rtc_debug.TOUCH_PAD1(is_sensor=0, row=31, bitnum=0)	# "BROWN_OUT_DET" export to TOUCH1
					# 	det = self.mydm_vol.get_result('VDC')
					# 	if float(det) > 1:
					# 		flag = 1
					# 		logwarn(vdd,'V',det)
					# 		detail_pos[idx_vth]=vdd
					# 		break
					# 	elif float(det) < 0.2:
					# 		flag = 0
					# 		loginfo(vdd,'V',det)			
					for vdd in range(VDD_rg[1], VDD_rg[0], -step_mV):
						self.myeps.pwr(vdd/1000.0, 0.5)
						self.chip.rtc_debug.TOUCH_PAD1(is_sensor=0, row=31, bitnum=0)	# "BROWN_OUT_DET" export to TOUCH1
						det = self.mydm_vol.get_result('VDC')
						if float(det) < 1:
							flag = 0
							logwarn(vdd,'V:',det)
							detail_neg[idx_vth]=vdd
							break
						elif float(det) > 1:
							flag = 1
							loginfo(vdd,'V:',det)
		logwarn(detail_neg)
		return  detail_neg


	def scan_Vth_detail(self, vth_ls = range(8),pos_neg=1, step_mV = 10, repeat=3):
		'''
		:brief:
			Detail scan the brownout trig voltage of diff Vth 
		:param:
			- detail_pos: return from "scan_vth_rough", diff Vth have specific range 
			- pos_neg: 0 pos, 1:neg
		'''	
		self.cfg  = PtestConfig(self.channel, self.channel, chipv=self.chipv, mydm_vol=self.mydm_vol, myeps=self.myeps, myawg=self.myawg)
		self.cfg.chip_power_off()
		self.cfg.chip_power_on()

		self.ldo  = LdoPtest(self.channel, self.channel, self.chipv, mydm_vol=self.mydm_vol)
		log = csvreport('brownout/brownout')
		col_ls = ['MAC','OCODE','1V_REF']+['THRES_%d'% i for i in vth_ls]
		detail_pos = self.scan_vth_rough(vth_ls=vth_ls)
		for rpt in range(repeat):
			self.cfg.chip_power_off()
			self.cfg.chip_power_on()

			if self.chipv=='ESP32':
				mac = self.chip.CHIP_ID.chip_mac()
				ocode='NA'
				loginfo('switch dm_v to GPIO4')
				vref = self.ldo.vref(adc2_chl=0, atten_ls = [], adc_dref = [], slt_ls=range(1))
				# raw_input('switch dm_v to GPIO0')
			elif self.chipv=='CHIP722':
				mac = self.chip.efuse_mac.efuse_rd_mac_hi() + self.chip.efuse_mac.efuse_rd_mac_lo()
				ocode = self.chip.HWI2C.ulp.o_code
				raw_input('switch dm_v to GPIO18')
				vref = self.ldo.vref_bandgap(adc2_chl = 7, atten_ls = [], adc_dref = [])
				raw_input('switch dm_v to GPIO1')

			val_ls=[mac,ocode,vref[1][0]]
			for vth in vth_ls:
				if detail_pos[vth]==0:
					continue
				if pos_neg==1:	 detail_ls=range(int(detail_pos[vth]+100), int(detail_pos[vth]-100),int(-step_mV))
				elif pos_neg==0: detail_ls=range(int(detail_pos[vth]-100), int(detail_pos[vth]+100),int( step_mV))
				if self.chip.chipv == "ESP32":
					self.chip.rtc_brownout.thres_set(vth)
					thres = self.chip.HWREG.RTC_CNTL.RTC_BROWN_OUT.reg_dbrown_out_thres
					for vdd in detail_ls:
						self.myeps.pwr(vdd/1000.0, 1.5)
						self.chip.rtc_debug.TOUCH_PAD0(is_sensor=0, row=31, bitnum=0)	# "BROWN_OUT_DET" export to TOUCH0
						det = self.mydm_vol.get_result('VDC')
						if pos_neg==1:
							if float(det) > 1:
								loginfo(vdd,'V test:',det)
								val_ls.append(vdd)
								break
						elif pos_neg==0: 
							if float(det) < 1:
								loginfo(vdd,'V test:',det)
								val_ls.append(vdd)
								break
				
				elif self.chip.chipv == "CHIP722":
					self.chip.HWI2C.ulp.dbrown_out_thres = vth
					thres = self.chip.HWI2C.ulp.dbrown_out_thres
					logwarn('%r_brownout thres set:%r,read:%r' % (self.chipv,vth,thres))				
					for vdd in detail_ls:
						self.myeps.pwr(vdd/1000.0, 1.5)
						self.chip.rtc_debug.TOUCH_PAD1(is_sensor=0, row=31, bitnum=0)	# "BROWN_OUT_DET" export to TOUCH1
						det = self.mydm_vol.get_result('VDC')
						if pos_neg==1:
							if float(det) < 1:
								loginfo(vdd,'V test:',det)
								val_ls.append(vdd)
								break
						elif pos_neg==0: 
							if float(det) > 1:
								loginfo(vdd,'V test:',det)
								val_ls.append(vdd)
								break
			log.write_value(col_ls,val_ls)
			log.flush_line()
		self.cfg.chip_power_off()
		logwarn(col_ls,val_ls)
		return [col_ls,val_ls]


