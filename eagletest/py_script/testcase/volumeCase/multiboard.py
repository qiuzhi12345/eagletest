from testcase.performanceCase.CONFIG.config_ptest import PtestConfig
from testcase.performanceCase.SLEEP.sleep_ptest import SleepPtest
from testcase.performanceCase.STABLE.stability import Stability
from testcase.performanceCase.TSEN.tsen_ptest import TsenPtest
from testcase.performanceCase.REF.ref_ptest import LdoPtest
from testcase.performanceCase.REF.ref_ptest import RefPtest
from testcase.performanceCase.CLK.clk_ptest import ClkPtest
from testcase.performanceCase.ADC.adc_ptest import AdcPtest
# from testcase.volumeCase.SOCKET.socket import SocketPtest 
from baselib.loglib.log_lib import *
from baselib.loglib.log_csv import csvreport
from baselib.instrument.awg import awg
from baselib.instrument.eps import eps
from baselib.instrument.dm  import dm
from baselib.instrument.thc import thc
from baselib.tc_platform.common import InstrumentRemoteControl
from baselib.tc_platform.common import Multiboard_CTL
from functools import wraps
from hal.Init  import HALS
import time
import pandas as pd

def param_logger_multi(level=logging.INFO,drop_self=True):
	'''a decorator used to save func parameters into separate log'''
	def decorator(orig_func):
		file_path = './log_func_run_param_multi/'
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

class MultiBoardTest(object):
	'''docstring for MultiBoard'''
	def __init__(self, mux_chl, mcu_chl, chipv):
		'''

		:param mux_chl: channel number for MUX, which connects to DUT chip, syntax: com(#)
		:param mcu_chl: channel number for MCU chip, syntax: com(#)
		'''
		self.chip_n   = 0
		'''HAL'''
		self.mux_chl  = mux_chl
		self.mcu_chl  = mcu_chl
		self.chipv 	  =	chipv
 		self.chip 	  = HALS(mux_chl,chipv)
		'''setup multiboard control'''
		comNum  	  = int(filter(str.isdigit, self.mux_chl.ComPort))
		self.mctl 	  = Multiboard_CTL(mux_chl=self.mux_chl, mcu_chl=self.mcu_chl, chipv = self.chipv)
		'''universal timeout setup for both mcu & dut'''
		for i in ['mux', 'mcu']:
			getattr(self, '%s_chl'%i).req_com_timeout_block = True
			getattr(self, '%s_chl'%i).ser.timeout           =1
			loginfo('%s com timeout sets to'%i.upper(),self.mux_chl.ser.timeout)

	def _instantiate_irc(self, ins_ls, auto_type):
		'''instantiate remote instruments control
		
		'''
		self.irc = InstrumentRemoteControl(ins_ls=ins_ls, auto_type=auto_type)
		return

	def _t_l_i(self,log_name):
		'''initiate a temparory log for test item data saving,to be deleted after data merged into report log

		:param log_name: pick a name you want
		'''
		log_name = 'tbd_'+log_name
		self.ff = csvreport(log_name)

	def _t_l_wr(self,result,test_item_name=None,last_one=False):
		'''writes data into temporary log

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
		if last_one: 
			print self.ff.filename
			self.ff.deinit()
		else:
			self.ff.flush_line()
		return result

	def _write_to_log(self, log_file, col_name, val_name):
		log_file.write_value(col_name,val_name)
		log_file.flush_line()

	def _measurements_validation(self, col_ls, val_ls, checklist=['VREF_1V', 'RTC_LDO', 'DIG_LDO', 'SAR1_REF', 'VCM']):
		'''check if the test result is valid
		
		:param col_ls:    columns of the result
		:param val_ls:    values of the result
		:param checklist: check list of the test items of 'ALL'
		:return:
			- True: the test values contains ERROR data
			- False: all data PASS
		''' 
		
		valid_range={'VDD33(ADC)':[2000, 4096],
					 'FREQ_150K': [8*1E4, 2*1E5], 
					 'FREQ_32K':  [3*1E4, 4*1E4], 
					 'FREQ_8M':   [8*1E6, 9*1E6],
					 'VREF_1V':   [0.8, 1.3], 
					 'RTC_LDO':   [1.00, 1.20], 
					 'DIG_LDO':   [1.00, 1.20], 
					 'SAR1_REF':  [1.05, 1.2], 
					 'SAR2_REF':  [1.05, 1.2], 
					 'VCM':       [0.9, 1.0],

					 'V_LSLP_7_0(V)': [0.65, 0.75], 
					 'V_LSLP_3_0(V)': [0.75, 0.85], 
					 'V_LSLP_0_1(V)': [0.85, 0.95], 
					 'V_LSLP_0_5(V)': [1.05, 1.15]
					 }
		if checklist=='ALL': checklist=valid_range.keys()	
		
		error_ls=[]
		if '' in val_ls:
			item=col_ls[val_ls.index('')]
			return True, [item,'']			
		if 'SKIP' in val_ls:
			item=col_ls[val_ls.index('SKIP')]
			return True, [item,'SKIP']
		for item in checklist:
			if item in col_ls:
				idx=col_ls.index(item)
				if valid_range[item][0]<=float(val_ls[idx])<=valid_range[item][1]:
					logwarn(item, float(val_ls[idx]), 'PASS')
					if item==checklist[-1]:	return False,['ALL', 'PASS']
				else:
					error_ls+=[item,val_ls[idx]]
					logres(item, float(val_ls[idx]), 'ERROR')
					logres('ERROR_CHECK:',[item,val_ls[idx]])
					return True, error_ls

	@param_logger_multi(level=logging.INFO,drop_self=True)
	def _pkg_test_items(self, adc2_chl, atten_ls, dref_ls, vdd, hard, temp, dut_num, irc):
		'''

		:param adc2_chl: SAR-ADC2 channel pin number, which is used to mux out internal voltage for external measurements
		:param atten_ls: SAR-ADC2 attenuation value list to be used for test 
		:param dref_ls:  SAR-ADC2 DREF register value list to be used for test
		:param vdd:      Supply voltage for DUT chips
		:param hard:     mode of boot, chip has to straight boot up under hard mode, otherwise, boot under 3.3V, then drop to test voltage
		:param temp:     oven temperature used for testing
		:param dut_num:  DUT# on multi-board to be picked for testing
		:return col_ls:  list of column names
		:return val_ls:  list of measurement values
		:return col_smp: list of column names (simple log version)
		:return val_smp: list of measurement values (simple log version)
		'''
		if self.chipv == 'ESP32':
			Vdd33 	  = self._t_l_wr(self.ldo.vdd33())
			Start_32K = self._t_l_wr(self.clk.startup_xtal32k(1,3,3))
			Freq 	  = self._t_l_wr(self.clk.freq_8m_150k() )
			vref 	  = self._t_l_wr(self.ldo.vref(adc2_chl, atten_ls))
			col_ls = Vdd33[0] + Start_32K[0] + Freq[0] + vref[0] 
			val_ls = Vdd33[1] + Start_32K[1] + Freq[1] + vref[1] 
			return col_ls, val_ls

		elif self.chipv == 'CHIP722':
			tsen_dac_ls = [(-2,5), (-1,13), (0,15), (1,11), (2,10)]
			pvt 	  = self._t_l_wr(self.ref.pvt_test(dig_dbias=4, pvt_delay=400))
			mac 	  = self._t_l_wr(self.chip.efuse_mac.efuse_check_data())
			Freq 	  = self._t_l_wr(self.clk.freq_8m_150k())
			Vref_1V   = self._t_l_wr(self.ldo.vref_bandgap( adc2_chl=adc2_chl, atten_ls=atten_ls, adc_dref=dref_ls, o_code_only=False, swd_rd=False))
			vref   	  = self._t_l_wr(self.ldo.vref(    adc2_chl=adc2_chl, atten_ls=atten_ls, adc_dref=dref_ls, slt_ls=range(5)))			
			tsensor   = self._t_l_wr(self.tsen.tsensor(adc2_chl=adc2_chl, tsen_dac_ls=tsen_dac_ls, atten_ls=[], temp=temp))
			Vdd33 	  = self._t_l_wr(self.ldo.vdd33())
			Start_32K = self._t_l_wr(self.clk.startup_xtal32k(1,3,3))

			self.mctl.mcu_power_reset(chip_n=dut_num, irc=irc, volt=vdd, ilim=3, hard=hard)
			o_code_2 = self._t_l_wr(self.ldo.vref_bandgap(adc2_chl=adc2_chl, times=2, o_code_only=True, swd_rd=True))		
			
			if temp>400: self._t_l_wr(self.slp.sleep_buf(1))
			Dig_slp_v = self._t_l_wr(self.slp.light_slp_vol_cur(adc2_chl=adc2_chl, delay=1, curr_volt=2, vdd=vdd, hard=hard, 
															   mb=1,chip=dut_num, mctl=self.mctl))
			adc1 	  = self._t_l_wr(self.adc.adc1_80M_read(0))
			adc2 	  = self._t_l_wr(self.adc.adc2_80M_read(0))
			self.mctl.mcu_power_reset(chip_n=dut_num, irc=irc, volt=vdd, ilim=3, hard=hard)
			o_code_3 = self._t_l_wr(self.ldo.vref_bandgap(adc2_chl=adc2_chl, times=3, o_code_only=True, swd_rd=True))		

			self.stab.parameter_config(wait_time=2, try_loop=3)
			self.stab.deep_sleep_rtc_mem_config(slp_time=0.02, ref_buf=1, vgate_buf=1)
			Dslp      = self._t_l_wr(self.stab.deep_sleep_rtc_mem_check(slp_time=0.02), last_one=1)
			logwarn('DSLP:',Dslp)

			#save complete log
			col_ls_h = ['MAC'] +pvt[0]+Vdd33[0]+Start_32K[0]+Freq[0]
			val_ls_h = [mac[0]]+pvt[1]+Vdd33[1]+Start_32K[1]+Freq[1]
			col_ls_e = o_code_2[0]+Dig_slp_v[0]+adc1[0]+adc2[0]+o_code_3[0]+['DSLP']
			val_ls_e = o_code_2[1]+Dig_slp_v[1]+adc1[1]+adc2[1]+o_code_3[1]+[Dslp]

			col_ls  = col_ls_h+Vref_1V[0]+vref[0]+tsensor[0]+col_ls_e
			val_ls  = val_ls_h+Vref_1V[1]+vref[1]+tsensor[1]+val_ls_e
			
			#save simpler version log
			Vref_1V_smp, Tsen_smp, vref_smp = [[],[]], [[],[]], [[],[]]
			adc_len=len(atten_ls)*len(dref_ls)
			#pick data to construct simple version list
			for i in range(2):
				for j in range(5):
					vref_smp[i].append(vref[i][adc_len + j*(adc_len+1)])
				for k in range(3):
					Tsen_smp[i].append(tsensor[i][adc_len + k*(adc_len+1)])
				Tsen_smp[i].append(tsensor[i][-2])
				for n in range(1):
					Vref_1V_smp[i].append(Vref_1V[i][len(Vref_1V[0])-1+n])

			col_smp = col_ls_h+Vref_1V_smp[0]+vref_smp[0]+Tsen_smp[0]+col_ls_e
			val_smp = val_ls_h+Vref_1V_smp[1]+vref_smp[1]+Tsen_smp[1]+val_ls_e

			return col_ls,val_ls,col_smp,val_smp

	@param_logger_multi(level=logging.INFO,drop_self=True)
	def run_pkg_test(self, adc2_chl=7, hard=1, rf_att=50, atten_ls=range(4), dref_ls=[0,1,2,4], 
					chip_ls=range(28), vdd_ls=[2.7, 3.3],temp_check=False, temp_ls=[25]):
		'''Use MB test basic paramenters at diff temperature 
		
		:param adc2_chl:   Pull internal signal to external ADC2 channel
		:param rf_att:     txtone atten :45, if None skip test at rf_open background
		:param hard:       chip power on mode: 0:chip boot at 3.3V then drop to the set vdd, 1: chip boot at set vdd
		:param atten_ls:   [0,1,2,3], skip adc read ref voltage 
		:param dref_ls:    [0,1,2,4]
		:param chip_ls:    chip list will be test on MultiBoard: range(32)
		:param vdd_ls:     scan diff vdd(V) supply
		:param temp_ls:    the temperature list
		:param temp_check: True-> will check multiboard around chip and mcu temper; False->ignore
		'''
		logwarn ('''
        ************ PREPARE ENV ****************
        BELOW instruments required for autotest
        Make sure your have them connected

        OPTION1:
        EPS : supply voltage for vdd
        DM_V: test adc2_chl voltage

        OPTION2:
        AIO : supply voltage for vdd & current measure
        DM_V: test adc2_chl voltage')
        *****************************************''')
		logwarn (logcolor('''
        ********** Add "rftest" package *********
        1.need copy "rftest" package from RF group
        2."config_ptest.py" add import module:
          from rftest.rflib.rfcal import *
          from rftest.rflib.pbus import *
        *****************************************''',c_u='y'))
        #setup GPIB controlled machines        
		self.irc = InstrumentRemoteControl(auto_type='mb')
		#instantiate test cases
		dict_cc = {'channel':self.mux_chl,'chipv':self.chipv}
		self.clk  = ClkPtest  (**dict_cc)
		self.stab = Stability (**dict_cc)
		self.slp  = SleepPtest(irc=self.irc,**dict_cc)
		self.tsen = TsenPtest (irc=self.irc,**dict_cc)
		self.adc  = AdcPtest  (irc=self.irc,**dict_cc)
		self.ldo  = LdoPtest  (irc=self.irc,**dict_cc)
		self.ref  = RefPtest  (irc=self.irc,**dict_cc)
		self.cfg  = PtestConfig(mux_chl=self.mux_chl, mcu_chl=self.mcu_chl, chipv=self.chipv, irc =self.irc)
		#prepare log 
		log_name = '/MultiBoard/PKG/%s_pkg_test'%self.chipv
		self.log 	 = csvreport(log_name)
		self.log_smp = csvreport(log_name + '_simple')
		#check if test RF open condition, and prepare log accordingly
		if rf_att != None:
			self.rf 	 = csvreport(log_name + '_rfon')
			self.rf_smp	 = csvreport(log_name + '_rfon_simple')
		#check if oven test or room temp, and preapre log accordingly
		if temp_check:
			thc_chl=raw_input('TYPE OVEN COM number below:\n')
			thc_ctl=thc(com(int(thc_chl)))
			self.temp_log = csvreport('/MultiBoard/PKG/%s_oven_temperature_record'%self.chipv)

		rpt_ls=1 if rf_att==None else 2
		ERROR_chips, ERROR_items=[], []

		for temp in temp_ls:
			cyc=3 if temp==-40 else 2 #if -40C will wait extra cycle
			loginfo('Wait %r cycles for oven to reach set temperature'%cyc)
			if temp_check:
				thc_ctl.temper_set(temp,1)
				#wait 10mins for each cycle, break loop if reaches set temprature
				for cyc_num in range(cyc):
					t_rd=(thc_ctl.rd_register_cmd())/10
					if t_rd==temp: break
					loginfo('CYCLE#%d: Wait another 10mins....'%(cyc_num+1))
					time.sleep(60*10)

			for rpt in range(rpt_ls):
				'''rpt=0: rf_close
				   rpt=1: rf_open in background
				'''
				for vdd in vdd_ls:
					loginfo('TEST CHIP @ SUPPLY: %r' % vdd)
					self.irc.chip_reset(volt=vdd, ilim=3, hard=hard, en_awg=False)

					for chip_n in chip_ls:
						error_rpt  =0
						error_mark =True
						while error_mark and error_rpt<3:
							if error_rpt>0: logerror('ERROR detected and retest....%d'% error_rpt)

							self._t_l_i(log_name='multi_temp_pkg')							
							
							#reset part to be tested and select it 
							self.mctl.mcu_power_reset(chip_n=chip_n, irc=self.irc, volt=vdd, ilim=3, 
								hard=hard, timeout=2)

							time.sleep(2)

							o_code_1 = self.ldo.vref_bandgap(adc2_chl=adc2_chl, times=1, o_code_only=True, swd_rd=True)

							col_info=['TEMP','SUPPLY','CHIP#']+o_code_1[0]
							val_info=[temp,   vdd,     chip_n]+o_code_1[1]						
					
							if rpt==0:
								loginfo('... CLOSE RF Test ...')
								self.mux_chl.req_com('close_rf',1)
							elif rpt == 1:
								loginfo('... OPEN RF Test ...')
								temp=self.cfg.rf_open(temp,rf_att=rf_att)
								col_info +=temp[0]
								val_info +=temp[1]

							col_ls,val_ls,col_sip,val_sip= self._pkg_test_items(adc2_chl, atten_ls, dref_ls, vdd, hard,temp,
								dut_num=chip_n, irc=self.irc)

							#save log based on rf open or not
							log_to_save = 'log' if rpt==0 else 'rf'
							self._write_to_log(getattr(self, log_to_save), col_info+col_ls,  val_info+val_ls)
							self._write_to_log(getattr(self, log_to_save+'_smp'), col_info+col_sip, val_info+val_sip)

							os.remove(self.ff.filename)
							error_check = self._measurements_validation(col_ls,val_ls,checklist=['VREF_1V'])
							error_mark  = True if error_check[0] else False
							error_rpt   +=1
							ERROR_chips +=['CHIP%d_rpt%d'%(chip_n,error_rpt)]
							ERROR_items +=[error_check[1]]

		self.irc.chip_power_off(en_awg=False, out=0)
		return pd.DataFrame(data=ERROR_items, index=ERROR_chips)

	@param_logger_multi(level=logging.INFO,drop_self=True)
	def tsensor_test_items(self, adc2_chl, atten_ls, dref_ls, vdd, hard, temp, chip):
		if self.chipv == 'ESP32':
			Vdd33 	  = self._t_l_wr(self.vdd33())
			Start_32K = self._t_l_wr(self.startup_xtal32k(1,3,3))
			Freq 	  = self._t_l_wr(self.freq_8m_150k())
			vref 	  = self._t_l_wr(self.Vref(adc2_chl, atten_ls),last_one=True)
			col_ls = Vdd33[0] + Start_32K[0] + Freq[0] + vref[0]
			val_ls = Vdd33[1] + Start_32K[1] + Freq[1] + vref[1]
			return col_ls, val_ls

		elif self.chipv == 'CHIP722':
			mac 	  	= self._t_l_wr(self.chip.efuse_mac.efuse_check_data())
			Tsensor1   	= self._t_l_wr(self.tsen.tsensor(adc2_chl, tsen_dac_ls=[], atten_ls=atten_ls,temp=temp,chop_ls=[2],ref_vol=0))
			Vref_1V   	= self._t_l_wr(self.ldo.vref_bandgap(adc2_chl, atten_ls=range(4), adc_dref=[0], o_code_only=False, swd_rd=False))
			Vref  	  	= self._t_l_wr(self.ldo.vref(adc2_chl, atten_ls, adc_dref=[]))
			Tsensor2  	= self._t_l_wr(self.tsen.tsensor(adc2_chl, tsen_dac_ls=[], atten_ls=atten_ls,temp=temp,chop_ls=[2],ref_vol=0))
			Vdd33 	  	= self._t_l_wr(self.ldo.vdd33())
			clk_150_4 	= self._t_l_wr(self.clk.clk_freq_3point(clk_type=0))
			clk_8m_4  	= self._t_l_wr(self.clk.clk_freq_3point(clk_type=1))
			clk_8m_scan = self._t_l_wr(self.clk.clk_freq_scan(clk_type=1))
			Tsensor3  	= self._t_l_wr(self.tsen.tsensor(adc2_chl, tsen_dac_ls=[], atten_ls=atten_ls,temp=temp,chop_ls=[2],ref_vol=0),last_one=True)

			col_ls = ['MAC'] + Vref_1V[0] + Vref[0] + Vdd33[0] + ['1_%r'%Tsensor1[0][0]] + ['2_%r'%Tsensor2[0][0]] + ['3_%r'%Tsensor3[0][0]]
			val_ls = [mac[0]]+ Vref_1V[1] + Vref[1] + Vdd33[1] + Tsensor1[1] + Tsensor2[1] + Tsensor3[1]
			col_ls += ['8M_ORIGIN','8M_MIN','8M_MID','8m_MAX'] + ['150K_ORIGIN','150K_MIN','150K_MID','150K_MAX']
			val_ls += list(clk_8m_4['freq']) + list(clk_150_4['freq'])
			
			Vref_1V_smp=[[],[]]
			Vref_1V_smp[0].append(Vref_1V[0][4])
			Vref_1V_smp[1].append(Vref_1V[1][4])
			col_sip = ['MAC']  + Vref_1V_smp[0] + Vref[0] + Vdd33[0] + ['1_%r'%Tsensor1[0][0]] + ['2_%r'%Tsensor2[0][0]] + ['3_%r'%Tsensor3[0][0]]
			val_sip = [mac[0]] + Vref_1V_smp[1] + Vref[1] + Vdd33[1] + Tsensor1[1] + Tsensor2[1] + Tsensor3[1]
			return col_ls,val_ls,col_sip,val_sip,clk_8m_scan

	@param_logger_multi(level=logging.INFO,drop_self=True)
	def run_tsensor_test(self, adc2_chl=7, hard=0, atten_ls=[], dref_ls=[], chip_ls=range(28), vdd_ls=[2.7, 3.3], temp_ls=[20,30]):
		'''
		:brief:
			For tsensor linearity test and scan 8m/150k_freq range through config reg
		:param:
			- adc2_chl : Pull internal signal to external ADC2 channel
			- hard: chip power on mode: 0:chip boot at 3.3V then drop to the set vdd, 1: chip boot at set vdd
			- atten_ls: []:skip adc read the tsensor ref voltage 
			- dref_ls: []
			- chip_ls: chip list will be test on MultiBoard: range(32)
			- vdd_ls: scan diff vdd(V) supply
			- temp_ls: the temperature list
		'''
		logwarn ('''
        ********* PREPARE ENV *********
        EPS : supply voltage for vdd
        AWG : input voltage for adc
        DM_V: test vref_pad voltage        
        *******************************''')		
		self.connect_instrument(['EPS','AWG','DM_V'])
		self.tsen = TsenPtest  (self.mux_chl, self.chipv)
		self.clk  = ClkPtest   (self.mux_chl, self.chipv)
		self.ldo  = LdoPtest   (self.mux_chl, self.mcu_chl, self.chipv, mydm_vol=self.mydm_vol)
		self.cfg  = PtestConfig(self.mux_chl, self.mcu_chl, self.chipv, mydm_vol=self.mydm_vol, myeps=self.myeps, myawg=self.myawg)
		log 	 = csvreport('MultiBoard/TSEN/%s_temp_scan'%self.chipv)
		log_8m   = csvreport('MultiBoard/TSEN/%s_8m_freq_scan'%self.chipv)

		col_8m_ls = ['TEMP','SUPPLY','CHIP#','ORIGIN']+range(256)
		temp = raw_input('pls enter the temperature:')

		for vdd in vdd_ls:
			logwarn('Supply: %rV testing..' % vdd)
			self.myeps.pwr(0, 0)
			time.sleep(1)
			self.myeps.pwr(vdd, 3)
			time.sleep(2)
			for chip_n in chip_ls:
				self._t_l_i(log_name='multi_temp_tsen')
				self.mcu.mcu_slt(chip_n)
				time.sleep(1)

				o_code_1  = self._t_l_wr(self.cfg.mb_chip_reset(adc2_chl,vdd=vdd,hard=hard,mb=1,times=1,chip=chip_n))
				col_info=['TEMP', 'SUPPLY(V)','CHIP#']+o_code_1[0]
				val_info=[temp, 	vdd, 	   chip_n]+o_code_1[1]
				logwarn('...CLOSE_RF_TEST...')
				self.mux_chl.req_com('close_rf',1)
				col_ls,val_ls,col_sip,val_sip,clk_8m_scan= self.tsensor_test_items(adc2_chl, atten_ls, dref_ls, vdd, hard,temp,chip=chip_n )
				val_8m_ls = [temp,vdd,chip_n]+list(clk_8m_scan['freq'])
				write_to_log(log_8m,col_8m_ls,val_8m_ls)
				write_to_log(log,col_info+col_ls, val_info+val_ls)
				os.remove(self.ff.filename)

	@param_logger_multi(level=logging.INFO,drop_self=True)
	def _adc_test_items(self, para,log):
		adc1_chl, adc2_chl, vref_pad, vdd, ain_step, atten_ls, ain_max, dref_ls, chip, temp = para
		
		time.sleep(0.1)
		if self.chipv=='ESP32':
			chip_mac = self.chip.CHIP_ID.chip_mac()
		elif self.chipv=='CHIP722':
			chip_mac, rd_type, rd_8m = self._t_l_wr(self.chip.efuse_mac.efuse_check_data())

		info_head  = ['TEMP','CHIP#','MAC','SUPPLY']
		info_value = [temp,  chip,   chip_mac,  vdd]

		vdd33 = self._t_l_wr(self.ldo.vdd33())
		vref  = self._t_l_wr(self.ldo.vref(adc2_chl=vref_pad, atten_ls = [], adc_dref = [0], slt_ls=range(2,4)))
		info_head  = info_head  + vdd33[0] + vref[0]
		info_value = info_value + vdd33[1] + vref[1]

		head_ls, val_adc1, val_adc2 = self._t_l_wr(
			self.adc.adc_ext_vol_scan(adc1_chl=adc1_chl, adc2_chl=adc2_chl, atten_ls=atten_ls, 
									  ain_step=ain_step, ain_max=ain_max, vdd =vdd, dref_ls =dref_ls),
			                                       last_one=True)
		for idx_atn,atten in enumerate(atten_ls):
			for idx_drf,dref in enumerate(dref_ls):	
				log.write_value(info_head, info_value)
				if adc1_chl!=None:
					adc1=val_adc1[idx_atn*len(dref_ls)+idx_drf]
					log.write_value(head_ls,adc1)
				if adc1_chl!=None:
					adc2=val_adc2[idx_atn*len(dref_ls)+idx_drf]	
					log.write_value(head_ls,adc2)
				log.flush_line()

	@param_logger_multi(level=logging.INFO,drop_self=True)
	def run_adc_test(self, adc1_chl=0, adc2_chl=7, vref_pad=9, vdd_ls=[2.7, 3.3, 3.6], ain_step=1000, atten_ls=range(4), 
		             dref_ls=[0],ain_max=[1200,1500,2200,3600], chip_ls=range(32),temp_list=[-40,40,85,125], wifion=False):		
		'''
		:brief:
			Use AWG input analog signal to ADC1&2, scan the converted digital signal at diff atten & vdd & temper
		:param:
			- adc1_chl: chl0
			- adc2_chl: chl7
			- vref_pad: pull SAR_Vref to adc2_chl, but only adc2_chl7 export to multi_ctl board 			
			- vdd_ls  : supply voltage(V) list
			- ain_step: analog signal input step(mV)
			- atten_ls: [0,1,2,3]
			- dref_ls : [0,1,2,4]
			- ain_max : max analog input at diff atten
			- chip_ls : range(32)
			- temp_list: temperature list:[-40,0,40,125]
		'''	
		logwarn ('''
        ********* PREPARE ENV *********
        EPS : supply voltage for vdd
        AWG : input voltage for adc
        DM_V: test vref_pad voltage        
        *******************************''')		
		self.irc = InstrumentRemoteControl(ins_ls=['ALLINONE','AWG','DM_V'],auto_type=None)
		self.adc = AdcPtest(self.mux_chl, self.chipv, self.irc)
		self.ldo = LdoPtest(self.mux_chl, self.chipv, self.irc)

		if 	 adc1_chl == None:	adc_test = 'sar2'
		elif adc2_chl == None: 	adc_test = 'sar1'
		else:                   adc_test = 'sar1&2' 
		wifi_status = 'on' if wifion else 'off'  
		log= csvreport('/MultiBoard/ADC/%s_%s_stepsize%dmV_wifi_%s'%(self.chipv,adc_test,ain_step,wifi_status))
		for temp in temp_list:			
			# raw_input('input the temperature...\n')
			for chip in chip_ls:
				for vdd in vdd_ls:
					self.irc.chip_power_on(volt=vdd, en_awg=False)
					self._t_l_i(log_name='multi_temp_adc')
					self.mctl.mcu_power_reset(chip_n=chip, irc=self.irc, volt=vdd, ilim=3, hard=0, timeout=2)
					if wifion:
						self.chip.wifimac.mac_init()
						time.sleep(2)		
					para=[adc1_chl, adc2_chl, vref_pad, vdd, ain_step, atten_ls, ain_max,dref_ls, chip, temp]
					self._adc_test_items(para,log)
					os.remove(self.ff.filename)

		self.irc.chip_power_off(en_awg=True, out=0)

	@param_logger_multi(level=logging.INFO,drop_self=True)
	def run_stability_test(self,adc2_chl=7,hard=0,chip_ls=range(32),vdd_ls=[2.7,2.8,3.0,3.3,3.6],slp_time = 10):
		'''test chip stability
		:param:
			- slp_time: unit in mins
		'''
		# supply_ldo=[(3.0, 4.1), (2.8, 3.88), (2.7, 3.77)]
		self.connect_instrument()
		self.stab = Stability(self.mux_chl, self.chipv)
		self.cfg  = PtestConfig(self.mux_chl, self.mcu_chl, self.chipv, mydm_vol=self.mydm_vol, myeps=self.myeps, myawg=self.myawg)
		log_data = csvreport('/MultiBoard/STABLE/%s_stable_test'%self.chipv)		
		rpt_times = 20
		wait_time = 5   #unit in seconds
		try_loop  = 20  #number of times to try
		slp_time_cal = slp_time*2   #IDF ERROR to be fixed

		def temp_read():
			temp_l = []
			for tsen_os in [(-2,5),(2,10),(0,15)]:
				self.chip.tsen.config(dac=tsen_os[1])
				Temp_adc = self.chip.tsen.read()
				if Temp_adc=='': temp_l.append('')
				else:            
					temp_cal = 0.4386*int(Temp_adc, 16) - 27.88*(tsen_os[0]) - 20.52
					loginfo(temp_cal)
					temp_l.append(temp_cal)
			return temp_l
		# for temp in temp_ls:
		# 	logwarn('Waiting for Temperature achieved %r C' % temp)
		# 	'''read temp'''
		# 	if temp==-40: cyc=3
		# 	else:     cyc=3
		# 	logres('will wait:',cyc,'cyc')
		# 	for wait_min in range(cyc):
		# 		T_flg=self.check_temp(temp,temp_log)
		# 		if T_flg: break
		# 		logres('cyc%d :delay 10mins....'%(wait_min+1))
		# 		time.sleep(60*10)
		# 	# raw_input('ENTER THE Temperature:')
		loginfo('vdd_ls:',vdd_ls)
		for rpt in range(rpt_times):
			for vdd in vdd_ls:
				logwarn('Supply: %rV testing.. ROUND#%d' %(vdd,rpt))
				temp_l_0   = ['TEMP-2']
				temp_l_1   = ['TEMP 2']
				temp_l_2   = ['TEMP 0']
				supply_l   = ['SUPPLY']
				chip_l     = ['CHIP_NUM']
				o_code_l   = ['O_CODE']
				num_of_run = ['RUN#']
				clk_sw_l   = ['CLK_SW']
				# clk_sw2_l = []
				light_mac_l = ['LIGHT_SW']
				deep_mem_l  = ['DEEP_MEM']
				#logwarn('Supply: %rV testing..' % vdd)
				# ain_ls = range(0, int(vdd*1e3)+1, adc_step) 
				self.myeps.pwr(0, 0)
				time.sleep(1)
				self.myeps.pwr(vdd, 3)  # For MultiBoard :need remove LDO then direct pull vdd to eps
				time.sleep(2)

				for chip_n in chip_ls:
					logwarn('TEST CHIP #%d'%chip_n)
					# self.mcu.mcu_reset(chip_n)
					self.mcu.mcu_slt(chip_n)
					time.sleep(1)
					hold_time=2
					o_code_1  = self.cfg.mb_chip_reset(adc2_chl,vdd=vdd,hard=hard,mb=1,times=1,chip=chip_n,hold_time=hold_time)
					temp_l_3  = temp_read()
					#col_info=['Temp', 'Supply','CHIP']+o_code_1[0]
					#val_info=[temp, '%rV'%vdd, '#%d'%chip_n]+o_code_1[1]
					temp_l_0.append(temp_l_3[0])
					temp_l_1.append(temp_l_3[1])
					temp_l_2.append(temp_l_3[2])
					supply_l.append(vdd)
					num_of_run.append(rpt)
					chip_l.append(chip_n)
					o_code_l.append(o_code_1[1][0])
					self.mux_chl.req_com('close_rf',1)
					# if rpt==0:
					# logwarn('...CLOSE_RF_TEST...')
					# self.channel.req_com('close_rf',1)
					# elif rpt == 1:
					# 	logwarn('...OPEN_RF_TEST...')
					# 	temp=self.rf_open(temp,rf_att=rf_att)
					# 	col_info=col_info+temp[0]
					# 	val_info=val_info+temp[1]
					self.stab.parameter_config(wait_time=wait_time,try_loop=try_loop)
					logwarn('CLOCK SWITCH TEST')
					self.stab.clk_switch_config(test_times=1000)
					clk_sw_l.append(self.stab.clk_switch_check())
					logwarn('LIGHT SLEEP MAC WAKEUP TEST')
					self.stab.light_sleep_mac_wkup_config(slp_time=slp_time)

				self._write_to_log(log_data,chip_l,supply_l)					
				self._write_to_log(log_data,chip_l,num_of_run)					
				self._write_to_log(log_data,chip_l,temp_l_0)
				self._write_to_log(log_data,chip_l,temp_l_1)
				self._write_to_log(log_data,chip_l,temp_l_2)
				self._write_to_log(log_data,chip_l,o_code_l)					
				self._write_to_log(log_data,chip_l,clk_sw_l)	

				'''check light sleep'''
				time.sleep(slp_time_cal)
				for chip_n in chip_ls:
					light_mac_l.append(self.stab.light_sleep_mac_wkup_check(slp_time=0.05))
					logwarn('DEEP SLEEP MEM CHECK TEST')
					self.stab.deep_sleep_rtc_mem_config(slp_time=slp_time,ref_buf=1,vgate_buf=1)
				self._write_to_log(log_data,chip_l,light_mac_l)					
				'''check deep sleep'''
				time.sleep(slp_time_cal)
				for chip_n in chip_ls:
					deep_mem_l.append(self.stab.deep_sleep_rtc_mem_check(slp_time=0.05))
				self._write_to_log(log_data,chip_l,deep_mem_l)					
		return

	@param_logger_multi(level=logging.INFO,drop_self=True)
	def run_sleep_wakeup_test(self, vdd_ls=[3.6],slp_md_ls=[0,0x3f], chip_ls=range(32),sleep_sec=10, temp_ls=[25]):
		'''
		:brief:
			For ESP32 deepsleep & lightsleep wakeup test under High/Low temper & voltage
		:param:
			- vdd_ls: 
			- slp_md_ls: 0: lightsleep, 1:deepsleep
			- chip_ls: range(32)
			- sleep_sec: sleep second
		'''
		self.slp = SleepPtest(self.mux_chl,self.mux_chl,self.chipv)		
		log 	 = csvreport('/MultiBoard/SLEEP/%s_sleep_wake'%self.chipv)
		for temp in temp_ls:
			raw_input('input temperature...')
			for vdd in vdd_ls:				
				# self.myeps.pwr(vdd, 2)
				time.sleep(1)
				for slp_md in slp_md_ls:
					col_ls=['TEMPER','VDD','SLP_MODE']
					val_ls=[temp, vdd, slp_md]
					for chip_n in chip_ls:
						pre_150 = self.chip.rtc_clk.get_clk_calibration(0)
						loginfo('pre_read_150k %r'%pre_150)
						loginfo('go to sleep chip# %d'%chip_n)
						self.mcu.mcu_slt(chip_n)
						time.sleep(1)
						self.chip.rtc_clk.rtc_slow_clk_select(0) #0:150k,1:32k,2:8M/256
						self.chip.rtc_sleep.rtc_timer_wakeup(0,150000*sleep_sec)
						self.chip.rtc_sleep.special_sleep(slp_mode=slp_md, wakeup_opt=8, reject_opt=0)
					time.sleep(sleep_sec)
					for chip_n in chip_ls:
						rpt=0
						error_ls=[]
						loginfo('check chip# %d'%chip_n)
						self.mcu.mcu_slt(chip_n)
						time.sleep(1)						
						clk_150 = self.chip.rtc_clk.get_clk_calibration(0)
						while clk_150=='' and rpt<5:
							clk_150 = self.chip.rtc_clk.get_clk_calibration(0)
							time.sleep(1)
							rpt+=1
						if clk_150=='':
							error_ls.append(chip_n)
							logwarn('chip#%d no wake!!!'%chip_n)
						col_ls.append('CHIP#%d'%chip_n)
						if pre_150!='':
							val_ls.append(clk_150)
						elif pre_150=='':
							val_ls.append('pre_%r_wk_%r'%(pre_150,clk_150))
					log.write_value(col_ls, val_ls)
			log.flush_line()
			logwarn(error_ls)

	@param_logger_multi(level=logging.INFO,drop_self=True)
	def run_32k_sleep_test(self,comNum=1,chip_ls=range(3),slp_time=37,timeout=1,opD=0,FIB=False,oldBin=True,mb=0):
		'''
		Vbg:
		get_xtal_startup_time 1 1 3 0
		rtc_timer_slp_test 0x6666 0x41
		Above sleep mode setup note(bit7=1 vbg=1.5V,bit7=0 vbg=1.2V)
		Set oldBin to be False if uses new fixed timer bin
		opD = 0 for normal, opD=1 for 36hours, opD=3 for 3 days, opD=6 for 6 days
		'''                        
		if   opD == 1: slp_time = 2190 # mins for 36 hours
		elif opD == 3: slp_time = 4370 # mins for 72 hours
		elif opD == 6: slp_time = 8800 # mins for 6 days 
		'''Set touch dac level for 32K cyrstal based on chip type'''
		if FIB is True: touch_dac_val = 0
		else:           touch_dac_val = 1
		if mb == 0: 
			chip_ty = 'Sng' 
			mb_com  = comNum
		else: 
			chip_ty = 'Mul' 
			mb_com  = mb
		self.clk  = ClkPtest(self.mux_chl,self.chipv)
		slpTestLog  = csvreport('/MultiBoard/XTAL_32K/sleepTest_%sB#%s_vbg1p2V_%smins' % (chip_ty,mb_com,slp_time))
		self.slp  = SleepPtest(self.mux_chl,self.mux_chl,self.chipv)

		if oldBin is False: startUp_ls = ['StartUp Freq']
		else:               startUp_ls = ['StartUp Time']
		mac_ls           = ['CHIP_MAC']
		chipNum_ls       = ['CHIP#']
		error_ls         = []
		noReturn_freq_ls = []
		noReturn_wk_ls   = []            
		wkFromSlp_ls     = ['WAKE UP NOW !!']        
		freq_ls          = ['FREQ READ'] 
		wk_ls            = ['WAKEUP CAUSE']
		put2slp_ls       = ['Go to bed for %dmins'%slp_time]
		saveIt_ls        = ['Try to restart 32k']
		slpCheck_ls      = ['Check if sleeps']            
		sleepCheck       = 'initial'

		'''write data little function'''
		def addDataToLog(listOfData=[]):
			slpTestLog.write_value(mac_ls,listOfData)
			slpTestLog.flush_line()
			return  
		'''Sleep Cycle Test Starts Here'''
		# self._t_l_i(log_name='multi_temp_32k_start')
		for chip_slt in chip_ls: 
			chipNum_ls.append(chip_slt+1)
			self.mcu.mcu_slt(chip_slt)
			time.sleep(1)
			if self.chipv=='ESP32':
			    CHIP_MAC = self.chip.CHIP_ID.chip_mac()
			elif self.chipv=='CHIP722':
			    CHIP_MAC = self.mux_chl.req_com("efuse_rd_mac_hi",1)+ self.mux_chl.req_com("efuse_rd_mac_lo",1) 
			logres(CHIP_MAC)
			mac_ls.append(CHIP_MAC)
			'''StartUp 32K Xtal'''
			print touch_dac_val
			startUp = self.clk.startup_32kxtal(touch_dac_val=touch_dac_val,oldBin=oldBin)
			startUp_ls.append(startUp)
			# startUp_ls.append(startUp[:-30])
			'''Read Frequency '''
			time.sleep(1)   
			freq=self.chip.rtc_clk.get_clk_calibration(2)
			freq_ls.append(freq)
			'''Export Xtal 32K to IO2'''
			time.sleep(0.2)                
			# self.chip.rtc_debug.TOUCH_PAD2(0, 4, 0)
			# loginfo('Exported XTAL_32K CLK to IO2')
		logres(mac_ls)
		slpTestLog.write_value(mac_ls,startUp_ls)
		slpTestLog.flush_line()
		addDataToLog(chipNum_ls)
		addDataToLog(freq_ls)
		# os.remove(self.ff.filename)
		'''Initial Sleep'''                     
		for chip_slt in chip_ls:
			last_flag=True if chip_slt==chip_ls[-1] else False
			self.mcu.mcu_slt(chip_slt)
			time.sleep(0.5) 
			slpCheck, put2slp=self.slp.gotosleep_32kxtal(chip_slt,opD=opD,slp_time=slp_time)
			put2slp_ls.append(put2slp)
			slpCheck_ls.append(slpCheck)
		addDataToLog(put2slp_ls)
		addDataToLog(slpCheck_ls)
		'''Loop Test'''
		rpt = 1
		while True:
			logwarn('waiting...%rmins'%(slp_time+2))
			logwarn(time.strftime('%H:%M:%S'))
			time.sleep((slp_time+2)*60) #PYTHON wait for same sleep period and 2more minutes
			'''prepare noReturn list'''
			noReturn_freq_ls = []
			noReturn_wk_ls   = []            
			wkFromSlp_ls     = ['WAKE UP NOW !!']        
			wk_ls            = ['WakeUp Cause_%d'%rpt]
			saveIt_ls        = ['Try to restart 32k']
			freq_ls          = ['Freq Read'] 
			put2slp_ls       = ['Go to bed for %dmins'%slp_time]        
			slpCheck_ls      = ['Check if sleeps']
			'''Check Chips and put to sleep'''
			self._t_l_i(log_name='multi_temp_32k_loop')
			for chip_slt in chip_ls:  
				self.mcu.mcu_slt(chip_slt)
				'''wake up check'''
				time.sleep(0.2)
				tryToFix, wkFromSlp,freq_lis,wk=self.slp.wakeupcheck_32kxtal(chip_slt)
				wkFromSlp_ls.append(wkFromSlp)
				saveIt_ls.append(tryToFix)
				freq_ls.append(freq_lis)
				wk_ls.append(wk)
				'''Put chip to sleep'''
				time.sleep(0.2)
				slpCheck , put2slp=self.slp.gotosleep_32kxtal(chip_slt,opD=opD,slp_time=slp_time)
				put2slp_ls.append(put2slp)
				slpCheck_ls.append(slpCheck)
			if noReturn_freq_ls == [] and noReturn_wk_ls == []:
				print 'THIS CYCLE ALL GOOD'
			else:
				print 'Guys Not Wake Up Below'
				loginfo('FREQ NO RETURN CHIP:%s'%noReturn_freq_ls)
				loginfo('WAKUP NO RETURN CHIP:%s'%noReturn_wk_ls)
			addDataToLog(wkFromSlp_ls)
			addDataToLog(freq_ls)
			addDataToLog(wk_ls)
			addDataToLog(saveIt_ls)
			addDataToLog(put2slp_ls)
			addDataToLog(slpCheck_ls)
			rpt += 1
		return

	def run_vref_1v(self,adc2_chl=7,vdd_ls=[3.6,3.3],chip_ls=range(10),atten_ls=[],dref_ls=[],temp_ls=[25],
					ins_list=[], auto_type='mb'):
		
		self.irc = InstrumentRemoteControl(ins_ls=ins_list,auto_type=auto_type)
		self.ldo  = LdoPtest(irc=self.irc, channel=self.mux_chl, chipv=self.chipv)

		log 	 = csvreport('/MultiBoard/VREF_1V/%s_vref_1V_test'%self.chipv)
		def vref_1v_mb():
			mac 	  = self.chip.efuse_mac.efuse_check_data()
			Vref_1V   = self.ldo.vref_bandgap(adc2_chl=adc2_chl, atten_ls=atten_ls,adc_dref=dref_ls)
			return ['MAC']+Vref_1V[0], [mac[0]]+Vref_1V[1]

		for temp in temp_ls:
			loginfo('waiting for temperature to achieve %r(C)' % temp)
			for vdd in vdd_ls:
				loginfo('supply: %rV testing..' % vdd)
				self.irc.chip_reset(volt=vdd,hard=0,hard_vth=2.8)   # chip reset 
				for chip_n in chip_ls:
					self.mcu.mcu_reset(chip_n)
					time.sleep(1)
					res=vref_1v_mb()
					log.write_value(['TEMP','SUPPLY']+res[0], [temp,vdd]+res[1])
					log.flush_line()


