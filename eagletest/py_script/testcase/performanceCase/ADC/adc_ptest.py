from baselib.loglib.log_csv import csvreport
from baselib.instrument.awg import awg
from baselib.loglib.log_lib import *
from rtclib.rtc import ADC_LIB
from hal.Init import HALS
from rtclib.rtc import RESET_CAUSE
from collections import defaultdict

class AdcPtest(object):
	"""docstring for ADC"""
	def __init__(self, channel, chipv, irc):
		self.channel = channel
		self.chipv 	 = chipv
		self.chip 	 = HALS(channel, chipv)
		self.irc     = irc
		# if myawg!=None:
			# self.myawg=myawg

	# def connect_instrument(self):
	# 	'''
	# 	:brief:
	# 		Communication between instrument and PC by USB-GPIB interface
	# 	:param:
	# 		- awg: supply input signal for ADC_chl
	# 	'''
	# 	loginfo('awg')
	# 	self.myawg = awg()

	def adc1_80M_read(self, adc1_chl, atten=3, dref=0, filter_en=1):
		self.chip.rtc_adc1.config()
		self.chip.rtc_adc1.set(pad = adc1_chl, atten = atten)
		if self.chipv == 'CHIP722':
			self.chip.rtc_adc1.sar1_dref(dref)
		adc1_value = self.chip.rtc_adc1.read(filter_en)
		return ['ADC1_AT%d_DREF%d'% (atten, dref)], [adc1_value]

	def adc2_80M_read(self, adc2_chl, atten=3, dref=0,test_pad_en=0,filter_en=1):
		self.chip.rtc_adc2.config()
		self.chip.rtc_adc2.set(pad = adc2_chl, atten = atten, test_pad_en=test_pad_en)
		if self.chipv == 'CHIP722':
			self.chip.rtc_adc2.sar2_dref(dref)
		adc2_value = self.chip.rtc_adc2.read(filter_en)
		return ['ADC2_AT%d_DREF%d'% (atten, dref)], [adc2_value]

	def adc1_deepsleep(self, adc1_chl, sample_num, atten_value):
		first_addr = self.adc_lib.adc1_deepsleep_read(adc1_chl, sample_num, atten_value)
		self.chip.rtc_wdt.wdt_unlock()
		self.chip.rtc_wdt.wdt_stg_hold_len(0, 0xffff)
		self.chip.rtc_wdt.wdt_stg_act(0, 4)
		self.chip.rtc_wdt.wdt_init()
		time.sleep(2)
		reset_cause = int(self.chip.rtc.rtc_reset_cause())
		if (reset_cause == RESET_CAUSE['RTCWDT_RTC_RESET'].value):
			self.chip.rtc_wdt.wdt_stop()
		else:
			logerror("no reset")
			exit(-1)
		dslp_ls=[]
		for j in range(sample_num):
			Din = int(self.chip.MEM.rd(first_addr + j * 4) & 0xffff)
			print Din
			dslp_ls.append(Din)
		return dslp_ls	
	
	def adc2_deepsleep(self, adc2_chl, sample_num, atten_value, test_pad_en, wait_cycle):
		first_addr = self.adc_lib.adc2_deepsleep_read(adc2_chl, sample_num, atten_value, test_pad_en,wait_cycle)
		self.chip.rtc_wdt.wdt_unlock()
		self.chip.rtc_wdt.wdt_stg_hold_len(0, 0xffff)
		self.chip.rtc_wdt.wdt_stg_act(0, 4)
		self.chip.rtc_wdt.wdt_init()
		time.sleep(2)
		reset_cause = int(self.chip.rtc.rtc_reset_cause())
		if (reset_cause == RESET_CAUSE['RTCWDT_RTC_RESET'].value):
			self.chip.rtc_wdt.wdt_stop()
		else:
			logerror("no reset")
			exit(-1)
		dslp_ls=[]
		for j in range(sample_num):
			Din = int(self.chip.MEM.rd(first_addr + j * 4) & 0xffff)
			print Din
			dslp_ls.append(Din)
		return [dslp_ls]	

	def adc_ext_vol_scan(self, adc1_chl=1, adc2_chl=1, atten_ls=range(4), 
						 ain_step=100, ain_max=[1200,1500,2200,3600], 
						 vdd =3.3, filter_en=1, dref_ls=[0], mea_comp=1):		
		'''scan the adc read use awg input the signal from 0 to max 
		
		:param ain_step: step of the input voltage 
		:param ain_max:  adc max analog input at diff atten
		:param mea_comp: output voltage inaccuracy for signal generator
		'''
		def inpt_sig_gen(volt=0):
			self.irc.sng_gen(volt=volt)

		inpt_range = range(0, 3601, ain_step)
		head_ls  = ['ADC', 'ATTEN', 'DREF'] + ['INPUT_%d(mV)'%ain for ain in inpt_range]
		# val_dict = defaultdict(list)
		# val_dict['ADC'] = [1]*len(dref_ls)*len()
		val_adc1 = [[1,atten,dref] for atten in atten_ls for dref in dref_ls]
		val_adc2 = [[2,atten,dref] for atten in atten_ls for dref in dref_ls] 

		inpt_sig_gen(volt=0)
		skip=None
		for ain in inpt_range:
			# head_ls.append('INPUT_%d(mV)'%ain)
			if skip==0:
				# self.irc.sng_gen(volt=ain/1000.0)
				# added to compensate voltage inaccruracy of Signal Generator
				volt_use = ain+mea_comp if ain <=1500 else ain
				inpt_sig_gen(volt=volt_use/1000.0)
				time.sleep(3.3)	#added 2s extra delay to ensure stable DC signal
				self.chip.rtc_adc1.config()
				self.chip.rtc_adc2.config()		
				if len(dref_ls)==1:
					self.chip.rtc_adc1.sar1_dref(dref_ls[0])
					self.chip.rtc_adc2.sar2_dref(dref_ls[0])

			for idx_atn,atten in enumerate(atten_ls):
				skip=0
				# scan_range = int(vdd*1e3) if atten==3 else ain_max[atten] # ain_max valid value @Diff atten
				#
				scan_range = ain_max[atten] # ain_max valid value @Diff atten

				if ain <= scan_range:
					for idx_chl,chl in enumerate([adc1_chl,adc2_chl]):
						func=getattr(self.chip,'rtc_adc%d'%(idx_chl+1))
						func.set(atten = atten, pad = chl)
						for idx_drf,dref in enumerate(dref_ls):		
							if chl!=None and idx_chl==0:
								if len(dref_ls)!=1:
									self.chip.rtc_adc1.sar1_dref(dref)
								value_adc1 = func.read(filter_en)
								val_adc1[idx_atn*len(dref_ls)+idx_drf].append(int(value_adc1))
							elif chl!=None and idx_chl==1:
								if len(dref_ls)!=1:	
									self.chip.rtc_adc2.sar2_dref(dref)
								value_adc2 = func.read(filter_en)
								val_adc2[idx_atn*len(dref_ls)+idx_drf].append(int(value_adc2))							
						# loginfo('switch adc%d to other pad'%(idx_chl+1))
						# func.set(pad=chl-1, atten=atten)
				else:
					skip=1
					for idx_drf,dref in enumerate(dref_ls):
						if adc1_chl!=None: val_adc1[idx_atn*len(dref_ls)+idx_drf].append(0)
						if adc2_chl!=None: val_adc2[idx_atn*len(dref_ls)+idx_drf].append(0)
		
		inpt_sig_gen(volt=0)
		# self.irc.sng_gen(volt=0)
		# pd.DataFrame(dict(zip(res[0],np.array(res[1]+res[2]).T))).reindex(columns=head_ls).to_csv('/home/liuzibai/Desktop/test.csv')
		return [head_ls, val_adc1, val_adc2]

	def adc_noisefloor_active(self, internal, adc1_chl, adc2_chl,ain_ls=[0.5, 0.8], atten_ls=[0,1,2,3], sample_num=100, filter_en=0):
		'''
		:brief:
			use external signal or internal reference voltage as adc input, disable the read filter, test adc noisefloor at active mode
		:param:
			- internal: True or False
			- ain_V_ls: external signal voltage
			- sample_num: repeat read times 
			- filter_en: adc read filter =0
		'''
		log= csvreport('/ADC/adc_noisefloor_active')
		if internal==False:
			self.adc1_80M_read(adc1_chl=adc1_chl, filter_en=filter_en)
			self.adc2_80M_read(adc2_chl=adc2_chl, filter_en=filter_en)
			for ain in ain_ls:
				# self.myawg.appl('DC', 0 ,0, ain)
				self.irc.sng_gen(ain)
				time.sleep(1)
				for atten in atten_ls:
					self.chip.rtc_adc1.set( atten = atten, pad = adc1_chl)
					self.chip.rtc_adc2.set( atten = atten, pad = adc2_chl)
					col_ls=['INPUT_VOL(V)','ADC','ATTEN']
					adc1_ls=[ain,  1, atten]
					adc2_ls=[ain,  2, atten]
					
					for r in range(sample_num):
						adc1 = self.chip.rtc_adc1.read(filter_en)
						adc2 = self.chip.rtc_adc2.read(filter_en)
						adc1_ls.append(adc1)
						adc2_ls.append(adc2)
						col_ls.append('REPEAT_%d' % (r+i))
					log.write_value(col_ls,adc1_ls)
					log.write_value(col_ls,adc2_ls)
		elif internal==True:
			if self.chipv == 'ESP32':
				ain_ls = ['RTC_LDO']
			elif self.chipv == 'CHIP722':
				ain_ls = ['VREF_1V', 'RTC_LDO', 'SAR1_REF']			
			for ain_V in ain_ls:
				if ain_V == 'RTC_LDO':
					self.chip.power.ldo_debug(0, adc2_chl)	# RTC_LDO ESP32
				elif ain_V == 'VREF_1V':
					self.chip.HWI2C.bias.ent_cgm = 1		# VREF_1V
					self.chip.HWI2C.bias.dtest   = 1
				elif ain_V == 'RTC_LDO':
					self.chip.MEM.wrm(0x600080b8, 29, 28, 0)
					self.chip.rtc_debug.set_test_mux(1,0) 	# RTC_LDO CHIP722
				elif ain_V == 'SAR1_REF':
					self.chip.MEM.wrm(0x600080b8, 29, 28, 0)
					self.chip.rtc_debug.set_test_mux(1,1) 	# SAR1_REF	
				time.sleep(1)
				self.chip.rtc_adc2.config()
				for atten in atten_ls:
					col_ls  = ['INPUT_VOL(V)','ADC','ATTEN']
					adc2_ls = [ain_V,  2, atten]
					self.chip.rtc_adc2.set(atten = atten, pad = adc2_chl, test_pad_en = 1)
					for i in range(sample_num):				
						adc2 = int(self.chip.rtc_adc2.read(filter_en))
						col_ls.append('REPEAT_%d' % (i+1))
						adc2_ls.append(adc2)				
					log.write_value(col_ls, adc2_ls)				
				self.chip.HWI2C.bias.ent_cgm = 0		# close VREF_1V mux
				self.chip.HWI2C.bias.dtest   = 0	
		log.flush_line()
	
	def adc_noisefloor_depslp(self, internal,ain_V_ls=[0.5,0.8], adc1_chl=0,adc2_chl=0, sample_num=1000, atten_ls=[0,1,2,3], wait_cycle=0X1FF):
		'''
		:brief:
			use external signal or internal reference voltage as adc input, disable the read filter, test adc noisefloor at deepsleep mode
		:param:
			- internal: True or False
			- ain_V_ls: external signal voltage
			- sample_num: repeat read times 
			- wait_cycle: ulp delay cycles then read adc
		'''
		log= csvreport('/ADC/adc_noisefloor_depslp')
		col_ls  = ['INPUT_VOL(V)','ADC','ATTEN']
		if internal==False:
			ain_ls= ain_V_ls
			test_pad_en=0
		elif internal==True: 		
			test_pad_en=1		
			if self.chipv == 'ESP32':	ain_ls = ['RTC_LDO']
			elif self.chipv=='CHIP722': ain_ls = ['VREF_1V', 'RTC_LDO', 'SAR1_REF']				
		for ain_V in ain_ls:				
			logwarn(ain_V, 'testing...')
			if internal:
				if ain_V == 'RTC_LDO':
					self.chip.power.ldo_debug(0, adc2_chl)	# RTC_LDO ESP32
				elif ain_V == 'VREF_1V':
					self.chip.HWI2C.bias.ent_cgm = 1		# VREF_1V
					self.chip.HWI2C.bias.dtest   = 1
				elif ain_V == 'RTC_LDO':
					self.chip.MEM.wrm(0x600080b8, 29, 28, 0)
					self.chip.rtc_debug.set_test_mux(1,0) 	# RTC_LDO CHIP722
				elif ain_V == 'SAR1_REF':
					self.chip.MEM.wrm(0x600080b8, 29, 28, 0)
					self.chip.rtc_debug.set_test_mux(1,1) 	# SAR1_REF				
			# elif internal==False: self.myawg.appl('DC',0,0,ain_V)
			elif internal==False: self.irc.sng_gen(volt=ain_V)
			time.sleep(1)
			for atten in atten_ls:							
				adc1_ls = [ain_V,  1, atten]
				adc2_ls = [ain_V,  2, atten]
				if internal==False:
					val_ls1 = self.adc1_deepsleep(adc1_chl, sample_num, atten)
					log.write_value(col_ls+range(sample_num), adc1_ls+val_ls1)
				val_ls2 = self.adc2_deepsleep(adc2_chl, sample_num, atten, test_pad_en=test_pad_en, wait_cycle=wait_cycle)
				log.write_value(col_ls+range(sample_num), adc2_ls+val_ls2)
		log.flush_line()