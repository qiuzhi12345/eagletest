# -- coding: utf-8 --
# 中文支持
from testcase.performanceCase.CONFIG.config_ptest import PtestConfig
from testcase.performanceCase.CHIPPU.chippu_ptest import ChipPuPtest
from testcase.performanceCase.SLEEP.sleep_ptest import SleepPtest
from testcase.performanceCase.STABLE.stability import Stability
from testcase.performanceCase.TSEN.tsen_ptest import TsenPtest
from testcase.performanceCase.REF.ref_ptest import LdoPtest
from testcase.performanceCase.REF.ref_ptest import RefPtest
from testcase.performanceCase.CLK.clk_ptest import ClkPtest
from testcase.performanceCase.ADC.adc_ptest import AdcPtest
from baselib.tc_platform.tc_platform import socket_test
from baselib.tc_platform.common import InstrumentRemoteControl
from baselib.loglib.log_csv import csvreport
from baselib.loglib.log_lib import *
from baselib.instrument.awg import awg
from baselib.instrument.eps import eps
from baselib.instrument.dm  import dm
from rtclib.rtc import WAKEUP_ENABLE
from functools  import wraps
from hal.Init   import HALS
import pandas as pd
import time
def param_logger_skt(level=logging.INFO,drop_self=True):
	'''a decorator used to save func parameters into separate log'''
	def decorator(orig_func):
		file_path = './log_func_run_param_skt/'
		if not os.path.exists(file_path):
			logwarn("mkdir %s"%(file_path))
			os.mkdir(file_path)
		logger_param = logging.getLogger('param_log')
		hfile     = logging.FileHandler(file_path+'{}.log'.format(orig_func.__name__))
		formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
		hfile.setFormatter(formatter)
		logger_param.setLevel(level)
		logger_param.addHandler(hfile)
		@wraps(orig_func)
		def wrapper(*args,**kwargs):
			args_to_log = args
			if drop_self: args_to_log = args[1:]
			logger_param.info('\n --FUNC--\n {}\n --RAN w/--\n args:   {}\n kwargs: {}'.format(orig_func.__name__,args_to_log,kwargs))
			print 'Func: {} params is saved into log file'.format(orig_func.__name__)
			return orig_func(*args,**kwargs)
		return wrapper
	return decorator

class SocketTest(object):
	"""docstring for SOCKET"""
	def __init__(self, channel, chipv):
		self.channel  = channel
		self.chipv 	  =	chipv
 		self.chip 	  = HALS(channel,chipv)
		self.chip_n   = 0
		'''timeout'''
		self.channel.req_com_timeout_block=True
		self.channel.ser.timeout=1
		loginfo('chip com timeout set',self.channel.ser.timeout)

	def _t_l_i(self,log_name):
		'''initiate a temparory log for test item data saving,to be deleted after data merged into report log

		:param log_name: pick a name you want
		'''
		log_name = 'tbd_'+log_name
		self.ff = csvreport(log_name)

	def _t_l_wr(self,result,test_item_name=None,last_one=False):
		'''
		:brief:
			 writes data into temporary log
		:param result:         pass test item name & its data in list format 
		:param test_item_name: add a name for your test result if not included
		:param last_one:       set to True is test item to be saved is last of the list
		'''
		col = ['test_item','value']
		if type(result) is not list:
			r_l = [result]
		else:
			r_l = result
		if test_item_name is not None: r_l.insert(0,test_item_name)
		new_res=zip(result[0], result[1])
		for i in range(len(new_res)):
			self.ff.write_value(col,list(new_res[i]))

		# val=[str(r_l[0]).replace(',',''), str(r_l[1:]).replace(',','')]
		# self.ff.write_value(col,val)
		if last_one: 
			self.ff.deinit()
		else:
			self.ff.flush_line()
		return result

	def _instantiate_ptestcase(self,ins_ls=[],auto_type='socket'):
		'''

		:param ins_ls:    instrument list to be used if not using auto_type
		:param auto_type: 'mb' for multiboard, anything else for socket
		'''
		self.irc  = InstrumentRemoteControl(ins_ls=ins_ls, auto_type=auto_type)
		dict_cc   = {'channel':self.channel,'chipv':self.chipv}
		
		self.clk  = ClkPtest  (**dict_cc)
		self.tsen = TsenPtest (irc=self.irc, **dict_cc)
		self.ldo  = LdoPtest  (irc=self.irc, **dict_cc)
		self.slp  = SleepPtest(irc=self.irc, **dict_cc)
		self.ref  = RefPtest  (irc=self.irc, **dict_cc)
		self.adc  = AdcPtest  (irc=self.irc, **dict_cc)

	@param_logger_skt(level=logging.INFO,drop_self=True)
	def ldo_test_items(self,para,log):
		repeat   = para[0]
		adc2_chl = para[1]
		pw_ls    = para[2]
		chip 	 = HALS(self.channel)
		slt_ls 	 = ['RTC', 'VREF', 'DIG']
		self.chip_mac = self.chip.CHIP_ID.chip_mac() 		
		for pw in pw_ls:			
			info_hd  = ['CHIP_MAC', 'VDD(V)']
			info_val = [self.chip_mac, pw]
			if len(pw_ls) > 1:
				mode_ls = ['80M']
				self.irc.myeps = eps()
				self.irc.myeps.pwr(pw, 0.5)
				time.sleep(0.5)						
			elif len(pw_ls) == 1:
				mode_ls = ['80M', '2M', 'WIFI_INIT', 'DEPSLP', 'LISLP'] 
			
			for index_slt,slt in enumerate(slt_ls):
				for mode in mode_ls:
					if mode =='80M':
						chip.rtc_clk.set_cpu_freq(1)
						chip.power.ldo_debug(index_slt, adc2_chl)
					elif mode =='2M':			
						chip.rtc_clk.set_cpu_freq(4)	
						chip.power.ldo_debug(index_slt, adc2_chl)
					elif mode == 'WIFI_INIT':
						chip.rtc_clk.set_cpu_freq(1)
						chip.wifimac.mac_init()
						chip.power.ldo_debug(index_slt, adc2_chl)
					elif mode == 'DEPSLP':
						chip.power.ldo_debug(index_slt, adc2_chl)
						chip.rtc_sleep.rtc_timer_wakeup(0, 162500*repeat) 	# 162500 about 1s
						chip.rtc_sleep.special_sleep(0x29, WAKEUP_ENABLE['TIMER_EXPIRE_EN'].value, 0)
					elif mode == 'LISLP':
						chip.power.ldo_debug(index_slt, adc2_chl)
						chip.rtc_sleep.rtc_timer_wakeup(0, 162500*repeat)
						chip.rtc_sleep.special_sleep(0x0, WAKEUP_ENABLE['TIMER_EXPIRE_EN'].value, 0)
					time.sleep(0.5)
					val_sum = 0
					for i in range(repeat):
						val = self.mydm_vol.get_result('VDC')
						val_sum += float(val)
					val_avg = val_sum/repeat 	
					info_hd.append('%s_%s' % (slt,mode))
					info_val.append(val_avg)
			log.write_value(info_hd, info_val)
			log.flush_line()

	@param_logger_skt(level=logging.INFO,drop_self=True)
	def run_ldo_test(self, repeat=1, adc2_chl=9, pw_ls=[2.7,3.3,3.6], temp_list=range(-20,100,50), chn_thc=0, device= "TEMI880"):
		'''
		:brief:
			For ESP32 Test LOD('RTC', 'VREF', 'DIG') voltage at diff work mode & vdd & temper
		:param:
			- adc2_chl: export internal vref signal to ext ADC2 channel
			- pw_ls:    vdd supply(V)
			- repeat:   sleep mode: repeat test then calculate the average 
		'''		
		logwarn ('''
        ********* PREPARE ENV *********
        EPS : supply voltage for vdd
        DM_V: test adc2_chl voltage	
        *******************************''')
		self.connect_instrument(['EPS','DM_V'])
		logname = '/SOCKET/LDO/LDO_diff_temper_vdd'
		skt = socket_test(self.channel, logname, chn_thc, device, self.ldo_test_items, repeat, adc2_chl, pw_ls, )
		skt.run(temp_list)

	@param_logger_skt(level=logging.INFO,drop_self=True)
	def _package_test_items_esp32(self,para,log):
		'''
		:brief: 
			This package for ESP32 test:Freq_8M/150K, DIG_LDO, RTC_LDO, Current_Dslp, Curr_EN=0, Curr_EN=1
		'''
		slp_md=para[0]
		self.myawg.appl('DC',0,0,0)
		time.sleep(1)
		# i_en0 = self._t_l_wr(float(self.mydm_cur.get_result('IDC',data_type='MIN'))*1e6)
		self.myawg.appl('DC',0,0,3.3)
		time.sleep(1)
		# i_en1 = self._t_l_wr(float(self.mydm_cur.get_result('IDC'))*1e3)
		mac   = self._t_l_wr(self.chip.CHIP_ID.chip_mac())
		vdd33 = self._t_l_wr(self.ldo.vdd33())
		clk   = self._t_l_wr(self.clk.freq_8m_150k())
		vref  = self._t_l_wr(self.ldo.vref(adc2_chl=9,atten_ls=[],slt_ls=range(3)))
		self.chip.rtc_sleep.special_sleep(slp_md,0,0)
		# i_slp = self._t_l_wr(float(self.mydm_cur.get_result('IDC',data_type='MIN'))*1e6, last_one=True)
		i_en0='NA'
		i_en1='NA'
		i_slp='NA'
		col_ls = ['MAC']+vdd33[0]+clk[0]+vref[0]+['I(uA)_EN0','I(mA)_EN1','I(uA)_DSLP(%r)'%slp_md]
		val_ls = [mac]+vdd33[1]+clk[1]+vref[1]+[i_en0, i_en1, i_slp]
		log.write_value(col_ls,val_ls)
		log.flush_line()
		self.myawg.appl('DC',0,0,0)		

	@param_logger_skt(level=logging.INFO,drop_self=True)
	def run_pkg_test_esp32(self, slp_md=0x7f, temp_list=[], chn_thc=0, device='TEMI880'):
		'''
		:brief:
			For Batch chip basic paramenters testing 
		:param:
			- slp_md: 0x7f deepsleep mode, close all part

		'''
		logwarn ('''
        ********* PREPARE ENV *********
        AWG : control chip_pu
        DM_C: test vdd current
        DM_V: test adc2_chl_9 voltage	
        *******************************''')
		self.connect_instrument(['AWG','DM_V'])		
		self.ldo  = LdoPtest(self.channel, self.channel, self.chipv, mydm_vol=self.mydm_vol)
		self.clk  = ClkPtest(self.channel, self.chipv)
		logname   = 'SOCKET/PACKAGE/%s_Package_Test_OnSocket' % self.chipv
		skt = socket_test(self.channel, logname, chn_thc, device, self._package_test_items_esp32,slp_md)		
		skt.run(temp_list)

	@param_logger_skt(level=logging.INFO,drop_self=True)
	def _package_test_items_chip723(self, para, log):
		'''This package include: efuse burn, CLK, vref_1v, vref_LDO, Tsen, Lslp, Dslp ...etc 
		
		:SOCKET BOARD NOTICE: Light sleep current should be tested w/ no VDD_PERI & VDD_SPI jumper 
		'''
		def reset_w_o_code(volt,hard,times):
			self.irc.chip_reset(volt=vdd,hard=hard,hard_vth=2.8)
			time.sleep(1)
			o_code=self._t_l_wr(self.ldo.vref_bandgap(times=times, o_code_only=True, swd_rd=True))
			return o_code 

		# -------- parameter preparation --------
		adc2_chl, mode, efuse, file_path, interActiv, chipVer, delay, vdd_ls, hard, repeat = para
		vref 	 	= [],[]
		burn  		= 'NA'
		smp_col_res, smp_val_res  = [],[]
		ERROR_RECORD = []
		
		# -------- start testing below --------
		for vdd in vdd_ls:
			'''go through given vdd'''
			t1 = time.time()		
			for rpt in range(repeat):
				'''repeat if needed'''

				# -------- prepare log --------
				self._t_l_i(log_name='socket_pkg_test_temporary')
				logwarn('NOW Testing @ VDD=%rV'% vdd)

				# -------- measure leakage current --------
				i_leakage = self._t_l_wr(self.slp.leakage_curr(vdd))

				# -------- check efuse status and burn --------
				'''chip reset preparation'''
				o_code_0 = reset_w_o_code(volt=vdd,hard=hard,times=0)
				'''burn efuse to record mac'''
				rd_mac = self.chip.efuse_mac.efuse_check_data()
				if efuse:
					info = self.chip.efuse_mac.efuse_wr_data(file_path = file_path, interActive = interActive)
					if info == 0:
						burn 	 = 'old'
						logres('This chip is OLD !!!')
					elif info == 1:
						burn 	 = 'Conflict_notBurn'
						logres('INFO conflicted Error, efuse not being burned')
					elif len(info) == 3:
						burn 	 = 'new'
						exp_mac  = info[0]
						logwarn('This chip is NEW !!! Below info has been burned')
						print info
						act_mac = self.chip.efuse_mac.efuse_check_data()
						if (int(exp_mac,16) == int(act_mac,16)):
							rd_mac  ='%s'%act_mac
							print rd_mac
						else:
							logres('Burned mac is not as expected!!')
							rd_mac ='Expecting: %s; Actual reading: %s' % (exp_mac, act_mac)

				# -------- select test item configurations --------
				'''adjusts test item configurations for:
				tsensor offset, adc_dref, adc_atten
				'''
				if mode == 0:
					tsen_dac_ls  = [(0,15)]
					adc_dref 	 = [0]
					atten_ls 	 = [3]
				elif mode >= 1: 
					tsen_dac_ls  = [(-2,5), (-1,13), (0,15), (1,11), (2,10)]  
					adc_dref 	 = [0]
					atten_ls 	 = [0,1,2,3]
					if mode == 2:
						adc_dref = [0,1,2,4]
					elif mode == 3:
						atten_ls = []

				# -------- rf test, saves log seperately --------				
				# self.cfg.save_module_test(1)	# Test on rfopen background

				# -------- analog test items --------
				self.irc.chip_reset(volt=vdd,hard=hard,hard_vth=2.8)   # chip reset
				'''read pvt sensor and corresponding digital ldo voltages'''
				pvt, pvt_v = [],[]
				'''go through all dig_ldo dibas config options'''
				for _ in range(7):
					'''pvt sensor read'''
					pvt  += self._t_l_wr(self.ref.pvt_test(dig_dbias=_, pvt_delay=400))
					'''config digital dbias wak register'''
					self.chip.HWREG.RTC_CNTL.RTC_REG.reg_dig_reg_dbias_wak = _
					'''measure digital ldo voltage'''
					_v    = self._t_l_wr(self.ldo.vref(adc2_chl=adc2_chl,  atten_ls= [], adc_dref =adc_dref, slt_ls=['DIG_LDO']))
					'''rename column name'''
					_v[0] = 'DIG_LDO_PVT_%d'%_
					pvt_v += _v

				'''measure wifi pd current'''
				i_pvt = self._t_l_wr(self.slp.wifipd_curr(vdd=vdd))

				# -------- vdd33 & frequency test items --------
				self.irc.chip_reset(volt=vdd,hard=hard,hard_vth=2.8)   # chip reset
				vdd33 	  = self._t_l_wr(self.ldo.vdd33())
				start_32k = self._t_l_wr(self.clk.startup_xtal32k(1,3,3))
				freq 	  = self._t_l_wr(self.clk.freq_8m_150k())

				# -------- reference voltages --------
				vref_1v   = self._t_l_wr(self.ldo.vref_bandgap(adc2_chl=adc2_chl, atten_ls=atten_ls, adc_dref=adc_dref, 
										                  times=None, o_code_only=False, swd_rd=False))
				if mode >= 1:
					slt_ls = ['RTC_LDO', 'DIG_LDO', 'SAR1_REF', 'SAR2_REF', 'VCM']
					vref  = self._t_l_wr(self.ldo.vref(adc2_chl=adc2_chl,  atten_ls= atten_ls, adc_dref =adc_dref, slt_ls=slt_ls))
				
				# -------- temperature sensor read --------
				tsensor   = self._t_l_wr(self.tsen.tsensor(adc2_chl=adc2_chl, tsen_dac_ls=tsen_dac_ls, atten_ls=atten_ls, adc_dref=adc_dref))

				adc1 	  = self.adc.adc1_80M_read(adc1_chl=9)
				adc2 	  = self.adc.adc2_80M_read(adc2_chl=1)
				'''close test mux'''
				self.chip.MEM.wrm(0x600080b8, 29, 28, 0)

				# -------- light sleep test --------
				o_code_1 = reset_w_o_code(volt=vdd,hard=hard,times=1)
				lit_slp_c = self._t_l_wr(self.slp.light_slp_vol_cur(adc2_chl=adc2_chl,delay=delay,curr_volt=1,vdd=vdd,hard=hard))
				o_code_2 = reset_w_o_code(volt=vdd,hard=hard,times=2)
				lit_slp_v = self._t_l_wr(self.slp.light_slp_vol_cur(adc2_chl=adc2_chl,delay=delay,curr_volt=2,vdd=vdd,hard=hard))

				# -------- deep sleep test --------
				o_code_3 = reset_w_o_code(volt=vdd,hard=hard,times=3)
		 		Deepslp   = self._t_l_wr(self.slp.deep_slp_cur(),last_one=True)

				# -------- prepare log data --------
				t2  	  = time.time()
				cost_t 	  = t2-t1
				d_list_0 = [o_code_0, i_leakage, pvt, pvt_v, i_pvt, vdd33, start_32k, freq]
				d_list_1 = [adc1, adc2, o_code_2, lit_slp_v, o_code_1, lit_slp_c, o_code_3, Deepslp]
				col_info = ['SUPPLY','HARD','CHIP#', 'EFUSE_BURNED', 'COST_TIME', 'MAC']
				val_info = ['%r'%vdd,'%d'%hard,'%d'%self.chip_n, burn, cost_t, rd_mac]
				
				col_res, val_res = [],[] 
				for _ in d_list_0+[vref_1v, vref, tsensor]+d_list_1:
					col_res.append(_[0])
					val_res.append(_[1])
				log.write_value(col_info+col_res, val_info+val_res)
				log.flush_line()

				self.irc.chip_power_off(en_awg=True,timeout=0,out=0)
				rpt+=1
				os.remove(self.ff.filename)

		self.chip_n += 1
		logres('Test finished, please switch chip in socket to be %r ....' % self.chip_n)

	@param_logger_skt(level=logging.INFO,drop_self=True)
	def run_pkg_test_chip723(self, vdd_ls=[3.0, 3.3, 3.6], adc2_chl=7, mode=2, hard=1,repeat=1,efuse=False, 
		                SocketNum=1, file_path='/home/test/Documents/marlin3_skew/MAC_origin', interActive=True, 
		                chipVer='tt_b2', delay=1, temp_list=[], chn_thc=0, device='TEMI880', ins_option=1):
		'''
		:brief:
			For Batch chip basic paramenters testing 
		:param:
			- mode: 0:vdd33, vref_1v, 32k_StartupTime, Clk_freq, tsensor
			        1:add ADC_atten, Tsen_offset
			        2:add ADC_dref
			- adc2_chl : Pull internal signal to external ADC2 channel
			- efuse:     burn efuse if True 
			- file_path: ref doc for burn efuse
			- chipVer:   chip version
			- vdd_ls:    scan diff vdd supply
		'''
		file_path += 'mac_info_chip723_%s_1000pcs.csv' % chipVer #updated for marlin3 skew lot
		loginfo('ref doc for burn efuse :%r' % file_path)
		logwarn ('''
        ********* PREPARE ENV *********
        BELOW instruments required for autotest
        Make sure your have them connected

        OPTION1:
        EPS : supply voltage for vdd
        DM_C: measure vdd current
        DM_V: test adc2_chl voltage
        AWG : control chip_pu

        OPTION2:
        AIO : supply voltage for vdd & current measure
        DM_V: test adc2_chl voltage')
        AWG : control chip_pu

        !!检查以下!!'
        - VDD_PERI          --> 需用 USB 供电
        - VDD_SPI STRAPPING --> GPIO45= 0
        *******************************''')
		self._instantiate_ptestcase(ins_ls=[],auto_type='socket')

		log_path = 'SOCKET/PACKAGE/'
		log_name = log_path + '%s_chip723_%s_pkg_sckt_#%d_mode_%d' % (self.chipv, chipVer, SocketNum, mode)

		skt = socket_test(self.channel, log_name, chn_thc, device, self._package_test_items_chip723, adc2_chl, mode, efuse, 
						  file_path, interActive, chipVer, delay, vdd_ls, hard, repeat)		
		skt.run(temp_list)

	@param_logger_skt(level=logging.INFO,drop_self=True)
	def _adc_test_items(self, para,log):
		adc1_chl, adc2_chl, vref_pad, vdd_ls, ain_step, atten_ls, ain_max, dref_ls = para

		self.irc.chip_power_on(volt=vdd, ilim=3)
		raw_input('Please manually reset chip, then press enter')
		time.sleep(0.1)
		for vdd in vdd_ls:
			self.irc.chip_reset(volt=vdd, ilim=3, en_awg=False)
			self._t_l_i(log_name='socket_adc_temporary')
			print self.ff.filename

			if self.chipv=='ESP32':
				chip_mac = self.chip.CHIP_ID.chip_mac()
			elif self.chipv=='CHIP722':
				chip_mac = self.chip.efuse_mac.efuse_check_data()
			
			info_head  = ['CHIP#', 'MAC', 'SUPPLY']
			info_value = [self.chip_n, chip_mac, vdd]
			time.sleep(0.1)

			vdd33 = self._t_l_wr(self.ldo.vdd33(),test_item_name=None)

			slt_ls = ['SAR1_REF', 'SAR2_REF']
			vref  = self._t_l_wr(self.ldo.vref(adc2_chl=vref_pad, atten_ls=[], adc_dref = [0], slt_ls=slt_ls),test_item_name=None)
			info_head  += vdd33[0] + vref[0]
			info_value += vdd33[1] + vref[1]
			head_ls, val_adc1, val_adc2 = self._t_l_wr(self.adc.adc_ext_vol_scan(adc1_chl=adc1_chl, adc2_chl=adc2_chl, atten_ls=atten_ls, 
				                                       ain_step=ain_step, ain_max=ain_max, vdd =vdd,dref_ls =dref_ls),test_item_name=None, last_one=True)
<<<<<<< Updated upstream

			for idx_atn,atten in enumerate(atten_ls):
				for idx_drf,dref in enumerate(dref_ls):	
					log.write_value(info_head, info_value)
					if adc1_chl!=None:
						adc1=val_adc1[idx_atn*len(dref_ls)+idx_drf]
						log.write_value(head_ls,adc1)
					if adc1_chl!=None:
						adc2=val_adc2[idx_atn*len(dref_ls)+idx_drf]	
						log.write_value(head_ls,adc2)
=======
			# for idx_atn,atten in enumerate(atten_ls):
			# 	for idx_drf,dref in enumerate(dref_ls):	
			# 		log.write_value(info_head, info_value)
			# 		if adc1_chl!=None:
			# 			adc1=val_adc1[idx_atn*len(dref_ls)+idx_drf]
			# 			log.write_value(head_ls,adc1)
			# 		if adc1_chl!=None:
			# 			adc2=val_adc2[idx_atn*len(dref_ls)+idx_drf]	
			# 			log.write_value(head_ls,adc2)
			# 		log.flush_line()
			if adc1_chl is not None:
				for _ in val_adc1:
					log.write_value(info_head+head_ls, info_value+_)
>>>>>>> Stashed changes
					log.flush_line()
			if adc2_chl is not None:
				for _ in val_adc2:
					log.write_value(info_head+head_ls, info_value+_)
					log.flush_line()

			os.remove(self.ff.filename)

		self.irc.myawg.appl('DC',0,0,0)
		self.irc.myeps.pwr(vdd, 1.5)
		self.chip_n += 1

	@param_logger_skt(level=logging.INFO,drop_self=True)
	def run_adc_test(self, adc1_chl=1, adc2_chl=1, vref_pad=7, vdd_ls=[2.7, 3.3, 3.6], ain_step=100, atten_ls=range(4), 
		             ain_max=[1200,1500,2200,3600], dref_ls=[0,1,2,4], temp_list=[], chn_thc=0, device='TEMI880'):
		'''
		:brief:
			scan the adc1&2 input and meas sar1_ref & sar2_ref voltage, and read vdd33 
		:param:
			- adc1_chl: ext signal input channel for adc1
			- adc2_chl: ext signal input channel for adc2
			- vref_pad: export sar1_ref/sar2_ref signal to adc2_chl 
			- vdd_ls:   scan diff vdd supply
			- ain_step: step of input voltage(mV)
			- atten_ls: adc atten: [0,1,2,3]
			- dref_ls:  adc dref: [0,1,2,4]
			- ain_max:  the max valid input voltage(mV) under each atten
			            atten:    [0,   1,   2,   3   ]
			            valid_max:[1200,1500,2200,3600]
		'''		
		logwarn ('''
        ********* PREPARE ENV *********
        EPS : supply voltage for vdd
        AWG : input voltage for adc
        DM_V: test vref_pad voltage        
        *******************************''')
		self.connect_instrument(['EPS','AWG','DM_V'])
		logname  = '/SOCKET/ADC/%s_ADC_scan'%self.chipv
		self.ldo = LdoPtest(self.channel, self.channel, self.chipv, mydm_vol=self.mydm_vol)
		self.adc = AdcPtest(self.channel,self.chipv, myawg=self.myawg)
		skt = socket_test(self.channel, logname, chn_thc, device, self._adc_test_items, adc1_chl, adc2_chl, vref_pad, vdd_ls, ain_step, atten_ls, ain_max,dref_ls )
		skt.run(temp_list)

	@param_logger_skt(level=logging.INFO,drop_self=True)	
	def pvt_test_items(self, para, log):
		t1=time.time()
		adc2_chl 	 = para[0] 	 
		vdd_ls 		 = para[1]
		dig_dbias_ls = para[2]

		for vdd in vdd_ls:
			self._t_l_i(log_name='socket_temp_pvt')
			pvt_col	= []	
			pvt_val = []
			self.irc.myeps.pwr(vdd, 1)
			self.cfg.reset_chip(adc2_chl=adc2_chl,vdd=vdd,hard=1,mb=0,times=0,o_code=False)
			if self.chipv=='ESP32':
				CHIP_MAC 	= self.chip.CHIP_ID.chip_mac()
			elif self.chipv=='CHIP722':			
				CHIP_MAC = self.chip.efuse_mac.efuse_check_data()
			dig_ldo   = self._t_l_wr(result=self.ldo.vref(adc2_chl=adc2_chl, atten_ls = [], adc_dref = [0], slt_ls=range(1,2)),test_item_name=None)
			clk_32k   = self._t_l_wr(result=self.clk.startup_xtal32k(),test_item_name=None)
			clk_8m 	  = self._t_l_wr(result=self.clk.freq_8m_150k(),test_item_name=None)
			for dig_dbias in dig_dbias_ls:
				pvt   = self._t_l_wr(result=self.ref.pvt_test(dig_dbias=dig_dbias,pvt_res_en=0, pvt_delay=400),test_item_name=None)
				pvt_col+=pvt[0]
				pvt_val+=pvt[1]
			lit_slp_v = self._t_l_wr(self.slp.light_slp_vol_cur(adc2_chl=adc2_chl,delay=1,curr_volt=2,vdd=vdd,hard=1,mb=0),test_item_name=None)
			o_code_1  = self._t_l_wr(self.cfg.reset_chip(adc2_chl=adc2_chl,vdd=vdd,hard=1,mb=0,times=1,o_code=False),test_item_name=None)
			lit_slp_c = self._t_l_wr(self.slp.light_slp_vol_cur(adc2_chl=adc2_chl,delay=1,curr_volt=1,vdd=vdd,hard=1,mb=0), test_item_name=None) 	# light_slp current,test_item_name=None)
			o_code_2  = self._t_l_wr(self.cfg.reset_chip(adc2_chl=adc2_chl,vdd=vdd,hard=1,mb=0,times=2,o_code=False),test_item_name=None)
			depslp_c  = self._t_l_wr(self.slp.deep_slp_cur(),test_item_name=None,last_one=True)
			col_ls = ['VDD','CHIP_MAC', 'EFUSE_8M']+dig_ldo[0]+clk_32k[0]+clk_8m[0]+pvt_col+lit_slp_v[0]+o_code_1[0]+lit_slp_c[0]+o_code_2[0]+depslp_c[0]
			val_ls = [vdd, CHIP_MAC[0],CHIP_MAC[2]]+dig_ldo[1]+clk_32k[1]+clk_8m[1]+pvt_val+lit_slp_v[1]+o_code_1[1]+lit_slp_c[1]+o_code_2[1]+depslp_c[1]
			log.write_value(col_ls,val_ls)
			log.flush_line()
			os.remove(self.ff.filename)
		# raw_input('make sure current...')
		self.irc.myeps.pwr(0, 0)
		self.irc.myawg.appl('DC',0,0,0)
		t2=time.time()
		loginfo('cost %.2f s'%(t2-t1))

	@param_logger_skt(level=logging.INFO,drop_self=True)
	def run_pvt_test(self,adc2_chl=7, vdd_ls=[2.7,3.3,3.6], dig_dbias_ls=[0,4,7], temp_list=[], chn_thc=0, device='TEMI880'):
		'''
		:brief:
			Test PVT value and the lightsleep current at diff VDD(DIG_LDO), confirm the effect of current on dig_ldo voltage and conner
		:param:
			- adc2_chl: for test DIG_LDO voltage
			- vdd_ls: supply voltage(V)
			- dig_dbias_ls: dig_ldo bias(0~7)
		'''			
		logwarn ('''
        ********* PREPARE ENV *********
        EPS : supply voltage for vdd
        AWG : control chip_pu
        DM_V: test adc2_chl voltage	
        DM_C: test vdd current
        *******************************''')
		self.connect_instrument(['EPS','AWG','DM_V','DM_C'])
		self.clk = ClkPtest(self.channel, self.chipv)
		self.ldo = LdoPtest(self.channel, self.channel, self.chipv, mydm_vol=self.mydm_vol)
		self.slp = SleepPtest(self.channel, self.channel, self.chipv, mydm_vol=self.mydm_vol, mydm_cur=self.mydm_cur,  myeps=self.myeps, myawg=self.myawg)
		self.cfg = PtestConfig(self.channel, mcu_chl=self.channel, chipv=self.chipv, mydm_vol=self.mydm_vol, myeps=self.myeps, myawg=self.myawg)
		self.ref = RefPtest(self.channel,self.chipv)
		
		logname= '/SOCKET/PVT/%s_pvt_test'%self.chipv
		skt = socket_test(self.channel, logname, chn_thc, device, self.pvt_test_items, adc2_chl, vdd_ls, dig_dbias_ls)
		skt.run(temp_list)

	@param_logger_skt(level=logging.INFO,drop_self=True)	
	def chippu_test_items(self,para,log):
		vdd_ls=para[0]
		for vdd in vdd_ls:
			raw_input('VDD:%rV...'%vdd)
			col,val=self.pu.chippu_vth(Von_l=1500,Von_h=3000,Voff_l=900,Voff_h=1600,step=100)
			col_ls,val_ls=self.pu.chippu_vth(Von_l=val[1]-100,Von_h=val[1]+100,Voff_l=val[2]-100,Voff_h=val[2]+100,step=10)
			log.write_value(['VDD']+col_ls, [vdd]+val_ls)
			log.flush_line()
			logres(col_ls,val_ls)

	@param_logger_skt(level=logging.INFO,drop_self=True)	
	def run_chippu_test(self,vdd_ls=[2.7,3.3,3.6], temp_list=[], chn_thc=0, device='TEMI880'):
		'''
		:brief:
			This test ChipPuPtest voltage thres at diff vdd   
		:param:
			- vdd_ls: vdd supply voltage(V)
		'''	
		logwarn ('''
        ********* PREPARE ENV *********
        POWER : supply voltage for vdd
        EPS   : supply voltage for chippu
        *******************************''')
		self.connect_instrument(['EPS'])
		self.pu = ChipPuPtest(self.channel,self.chipv, myeps=self.myeps)
		logname = '/SOCKET/CHIPPU/%s_ChipPU_Vth'%self.chipv
		skt = socket_test(self.channel, logname, chn_thc, device, self.chippu_test_items,vdd_ls)
		skt.run(temp_list)

	def run_pvt_modem(self,dig_dbias=4 ,pvt_delay_ls=[400,800,1000], adc2_chl=7,slp_s=5, func_md=0, log=None):
		'''
		:brief:
			test the correlation between PVT and Current and DIG_LDO
		:param:
			- dig_dbias:[0~7],typical value is 4
			- pvt_delay_ls: pvt_test delay time
			- adc2_chl: export DIG_LDO to adc2_chl7
			- slp_s: sleep time(s)
			- func_md: 0:lightsleep_cur  1:modemsleep_cur  2:all
		'''			
		logwarn ('''
        ********* PREPARE ENV *********
        EPS : supply voltage for vdd
        AWG : control chip_pu
        DM_V: test adc2_chl voltage	
        DM_C: test vdd current
        *******************************''')
		if log==None:
			log 	= csvreport('SOCKET/PVT_RF_MODEM')
		pvt_col = []
		pvt_val = []
		I_slp   = []
		I_modem = []
		slp_mode_ls = [0x3e, 0x7e]
		def curr_get():
			I = float(self.mydm_cur.get_result('IDC'))*1e3
			return I
		self.connect_instrument()		
		self.cfg = PtestConfig(self.channel, mcu_chl=self.channel, chipv=self.chipv, mydm_vol=self.mydm_vol, myeps=self.myeps, myawg=self.myawg)
		self.ref = RefPtest(self.channel,self.chipv)
		self.ldo = LdoPtest(self.channel, self.channel, self.chipv, mydm_vol=self.mydm_vol)
		self.cfg.chip_power_on()		
		
		self.chip.HWREG.RTC_CNTL.RTC_REG.reg_dig_reg_dbias_wak = dig_dbias 
		
		mac = self.chip.efuse_mac.efuse_check_data()
		ldo = self.ldo.vref(7,slt_ls=[1],atten_ls=[])
		I0  = curr_get()
		for p_d in pvt_delay_ls:
			pvt = self.ref.pvt_test(dig_dbias=dig_dbias, pvt_delay=p_d)
			pvt_col += ['%s_%r'%(pvt[0][0],p_d)]
			pvt_val += pvt[1]
		
		col_ls = ['MAC', 'I(mA)_POWERON']+ldo[0]+pvt_col
		val_ls = [mac[0], I0]+ldo[1]+pvt_val
		if func_md==0 or func_md>1:
			loginfo('lightsleep test..')
			for slp_md in slp_mode_ls:			
				self.chip.power.lightsleep_cur(dbg=0,dig_dbias=dig_dbias,slp_mode=slp_md,slp_time =150000*slp_s)
				time.sleep(1)
				I1 = curr_get()		
				self.cfg.reset_chip(adc2_chl=adc2_chl,vdd=3.3,hard=1,mb=0,times=2,o_code=False)
				I_slp.append(I1)	
				col_ls+=['I_LSLP(mA)_WIFIPD0', 'I_LSLP(mA)_WIFIPD1']
				val_ls+=I_slp
		if func_md==1 or func_md>1:
			loginfo('modemsleep test..')
			for wifi_pd in [0, 1]:
				self.chip.power.modemsleep_cur(wifi_pd=wifi_pd)
				time.sleep(1)
				I2 = curr_get()
				I_modem.append(I2)
				col_ls+=['I(mA)_MODEM0', 'I(mA)_MODEM1']
				val_ls+=I_modem
		log.write_value(col_ls,val_ls)
		log.flush_line()
		self.cfg.chip_power_off()
		data_table = pd.DataFrame(data={'col':col_ls,'val':val_ls})
		return data_table

	def pvt_repeat(repeat=5,pvt_delay_ls=[400,1000],dig_dbias =4):
		'''
		:brief:
			重复上电读取PVT,以及上电之后读5次PVT分布
		'''
		df_val=[]
		for rp in range(repeat):
			tcs.cfg_tc_perf.chip_power_on()
			tcs.channel.req_com("close_rf")
			pvt_col=[]
			pvt_val=[]
			print('dig_dbias=%d'%dig_dbias)
			tcs.hals.HWREG.RTC_CNTL.RTC_REG.reg_dig_reg_dbias_wak = dig_dbias
			ocode1=tcs.hals.HWI2C.ulp.o_code
			if rp==0:
				mac=tcs.hals.efuse_mac.efuse_check_data()
			dig_ldo=tcs.ldo_tc_perf.vref(slt_ls=[1],adc2_chl=7,atten_ls=[])
			tsen1=tcs.tsen_tc_perf.tsensor(adc2_chl=7, tsen_dac_ls=[(0, 15)], atten_ls=[], adc_dref=[0], temp=25, chop_ls=[], ref_vol=0)
			for i in range(5):
				for pvt_delay in pvt_delay_ls:
					PVT=tcs.ref_tc_perf.pvt_test(dig_dbias=4,pvt_delay=pvt_delay)
					pvt_col.append("PVT_%d_%d"%(pvt_delay, i))
					pvt_val.append(PVT[1][0])
			tsen2=tcs.tsen_tc_perf.tsensor(adc2_chl=7, tsen_dac_ls=[(0, 15)], atten_ls=[], adc_dref=[0], temp=25, chop_ls=[], ref_vol=0)
			ocode2=tcs.hals.HWI2C.ulp.o_code
			col_ls=['MAC', 'O_CODE_1', 'O_CODE_2', 'TSEN_1', 'TSEN_2', 'DIG_LDO']+pvt_col
			val_ls=[mac[0], ocode1, ocode2] +tsen1[1]+ tsen2[1]+dig_ldo[1]+pvt_val
			log.write_value(col_ls,val_ls)
			log.flush_line()
			df_val.append(pd.DataFrame(val_ls))
			tcs.cfg_tc_perf.chip_power_off()
		df_val.insert(0,pd.DataFrame(col_ls))
		data_table=pd.concat(df_val,axis=1)
		# data_table = pd.DataFrame(data={'col':col_ls,'val':df_val})
		return data_table

	@param_logger_skt(level=logging.INFO,drop_self=True)
	def _htol_current_test_items(self, para, log):
		'''covers shutdown current, 0.75V light sleep current, deep sleep current

		NEEDS to manually change Module
		'''
		# delay, vdd_ls, hard, repeat = para
		delay    = para[0]
		vdd_ls   = para[1]
		hard     = para[2]
		repeat   = para[3]

		for vdd in vdd_ls:
			for rpt in range(repeat):
				self._t_l_i(log_name='htol_temp_pkg')
				logwarn('VDD%r TEST..'% vdd)
				'''leakage current'''
				i_leakage = self._t_l_wr(self.slp.leakage_curr(vdd))
				self.irc.chip_reset(volt=vdd,hard=hard,hard_vth=2.8,en_awg=True)
				'''record mac, chip-ver, 8M freq'''
				rd_mac, rd_type, rd_8m = self.chip.efuse_mac.efuse_check_data()
				'''analog test'''   
				lit_slp_c = self._t_l_wr(self.slp.light_slp_vol_cur(adc2_chl=7,delay=delay,curr_volt=1,vdd=vdd,hard=hard))
				self.irc.chip_reset(volt=vdd,hard=hard,hard_vth=2.8,en_awg=True)
		 		Deepslp   = self._t_l_wr(self.slp.deep_slp_cur(),last_one=True)
				'''prepare logdata''' 
				col_res	  = i_leakage[0] + lit_slp_c[0] + Deepslp[0]
				val_res	  = i_leakage[1] + lit_slp_c[1] + Deepslp[1]
				col_info = ['SUPPLY','HARD','CHIP#', 'MAC', 'TYPE', 'CLK_8M']
				val_info = ['%r'%vdd,'%d'%hard,'%d'%self.chip_n, rd_mac, rd_type, rd_8m]
				col_ls = col_info + col_res
				val_ls = val_info + val_res
				log.write_value(col_ls, val_ls)
				log.flush_line()										
				self.irc.chip_power_off(en_awg=True,timeout=0,out=0)
				rpt+=1
				os.remove(self.ff.filename)

		self.chip_n += 1
		logres('SWITCH CHIP %r ....' % self.chip_n)		

	@param_logger_skt(level=logging.INFO,drop_self=True)
	def run_htol_current_test(self, vdd_ls=[3.0, 3.3, 3.6], hard=1, repeat=1, delay=1,
							  ins_ls=['AWG','AllInOne'], temp_list=[]):
		'''For Batch chip basic paramenters testing 
		
		:param vdd_ls:    scan diff vdd supply
		:param adc2_chl:  
		'''
		logwarn ('''
        ********* PREPARE ENV *********
        BELOW instruments required for autotest
        Make sure your have them connected

        OPTION1:
        EPS : supply voltage for vdd
        DM_C: measure vdd current
        AWG : control chip_pu

        OPTION2:
        AIO : supply voltage for vdd & current measure
        AWG : control chip_pu
        *******************************''')
		self.irc = InstrumentRemoteControl(ins_ls=ins_ls, auto_type=None)
		#instantiate test cases
		dict_cc = {'channel':self.channel,'chipv':self.chipv}
		self.slp  = SleepPtest(irc=self.irc, **dict_cc)
		log_path = 'HTOL/PACKAGE/'
		log_name = log_path + 'marlin3_htol_current_test'
		self.log  = csvreport(log_name)

		skt = socket_test(self.channel,log_name, 0,'TEMI880', 
						  self._htol_current_test_items, delay, vdd_ls, hard, repeat)
		skt.run(temp_list)
		return