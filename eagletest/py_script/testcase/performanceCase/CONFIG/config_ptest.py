from baselib.instrument.awg import awg
from baselib.instrument.eps import eps
from baselib.instrument.dm  import dm
from baselib.loglib.log_lib import *
from hal.wifi_api import WIFIAPI
from hal.Init     import HALS
# from rftest.rflib.rfcal import *
# from rftest.rflib.pbus import *
from baselib.tc_platform.common import Multiboard_CTL

class PtestConfig(object):
	"""docstring for OTHER"""
	def __init__(self, mux_chl, mcu_chl, chipv, irc):
		'''configurations to control socket/multiboard test

		:param irc: instantiated instrument_remote_control class 
		'''
		self.chipv 	 =chipv
		self.mcu_chl =mcu_chl
		self.mux_chl =mux_chl
		self.irc     =irc
		dict_cc = {'channel':self.mux_chl,'chipv':self.chipv}

		self.mctl 	 =Multiboard_CTL(mcu_chl=self.mcu_chl, mux_chl=self.mux_chl, chipv=self.chipv)
		self.chip 	 =HALS   (**dict_cc)	
		self.wifiapi =WIFIAPI(**dict_cc)

	def check_temp(self, temp, temp_log):
		'''Use MCU on multi-board to check surrounding temperature

		:param temp:     input expected temperature
		:param temp_log: csv mode to record temperature
		'''
		if 	 temp >  80:	tsen_os= (-2,5)
		elif temp < -10: 	tsen_os= (2,10)
		else: tsen_os = (0,15)
		# For MultiBoard :need remove LDO then direct pull vdd to eps
		self.irc.chip_reset(volt=3.3, ilim=3, hard=0, en_awg=False)

		'''mcu sits in the middle of the multi-board, use it to check center temperature'''
		self.mctl.mcu_chip.tsen.config(dac=tsen_os[1])
		Temp_adc = self.mctl.mcu_chip.tsen.read()
		T_mcu    = 0.4386*int(Temp_adc, 16) - 27.88*(tsen_os[0]) - 20.52 
		loginfo('mcu temperature %.2fC'%T_mcu)
		T_all=[T_mcu]

		'''use chips sits at board corners to check temperature'''
		tm_now = time.strftime('%H:%M:%S')
		for i in [0,7,24,31]:
			self.mctl.mcu_reset(i)
			time.sleep(2)
			self.chip.tsen.config(dac=tsen_os[1])
			Temp_adc = self.chip.tsen.read()
			if Temp_adc=='':
				Temper=''
				T_all.append('')
			else:
				Temper   = 0.4386*int(Temp_adc, 16) - 27.88*(tsen_os[0]) - 20.52 
				T_all.append(float('%.2f'%Temper))
			loginfo('chip#%d temperature %.2r'%(i,Temper))
		
		T_all.insert(0,tm_now)
		col_ls=['TIME','T_MCU','T_0','T_7','T_24','T_31']
		logwarn(zip(col_ls, T_all))

		temp_log.write_value(col_ls,T_all)
		temp_log.flush_line()
		
		#checks if temperature value reads within +-15C of target temperature
		n=0
		for t in T_all[1:]:
			if abs(temp)+15 >=abs(t)>=abs(temp)-15: n+=1   
		if n>=3: return True
		else:    return False	

	def rf_open(self, temp, rf_att=50, adc2_chl=7,vdd=2.6,hard=0,chip=0):
		'''
		:brief:
			suitable for multi-board to increase the current as test background 
		:param:
			- rf_att: rf_att value increase the current reduce 
			- hard: 0:chip boot at 3.3V then drop to the set vdd, 1: chip boot at set vdd
			- chip: chip num
		'''
		rf_cfg  = rfcal(self.mcu_chl,self.chipv)
		rf_pbus = pbus (self.mcu_chl,self.chipv)
		self.mcu_chl.req_com('open_rf',1)
		time.sleep(2)		
		check_info=self.mcu_chl.req_com('',1)
		print check_info
		if check_info=='':
			self.reset_chip(adc2_chl,vdd=vdd,hard=hard,mb=1,times=999,chip=chip)
			rf_mk='OpenRF_Fault!'
		# elif check_info=="cmd not exist!":
		elif check_info=="cmd syntax error!":
			rf_mk=''			
		'''
		self.chip.MEM.wrm(0x600060a0,11,8,0xe)
		self.chip.MEM.wrm(0x600060a0,17,16,0x3)
		self.mcu_chl.req_com("txtone 1 0 %d 0 0 0"%rf_att,1)
		'''
		self.mcu_chl.req_com("pbus_debugmode",1)
		rf_pbus.open_tx(0x5f, 0x120)
		rf_cfg.tos()
		self.chip.MEM.wrm(0x600060a0,17,16,0x3)
		self.mcu_chl.req_com("txtone 1 0 %d 0 0 0"%rf_att,1)
		time.sleep(1)
		temp_ls=[]
		temp_col=[]
		''' tsen_offset=[(-2,5), (-1,13), (0,15), (1,11), (2,10)]'''
		if 	 temp >  80:	tsen_os= (-2,5)
		elif temp < -10: 	tsen_os= (2,10)
		else: tsen_os = (0,15)
		self.chip.tsen.config(dac=tsen_os[1])
		for i in range(5):
			Temp_adc = self.chip.tsen.read()
			Temper   = 0.4386*int(Temp_adc, 16) - 27.88*(tsen_os[0]) - 20.52  
			logwarn('T:%.2f'%Temper)
			time.sleep(2)
			temp_col.append('T%d'%i)
			temp_ls.append('%s %.2f'%(rf_mk,Temper))
		self.chip.tsen.close()
		return [temp_col,temp_ls]

	def save_module_test(self,path_abs=0):
		'''
		:brief:
			for 800pcs CHIP722 RF_TEST	
		'''	
		self.mcu_chl.req_com('open_rf',1)
		time.sleep(2)		
		self.wifiapi.cmdstop()
		filetime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()));
		if path_abs ==1:
			rfdata_path = '/home/songlingyu/CHIP/eagletest/py_script/log/BaseFunc_Test/rfdata/'
			data_path1 = rfdata_path+'%s/'%('mod_test')
			if os.path.exists(data_path1) == False:
				os.mkdir(data_path1)
			filetime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()));
			mac = self.wifiapi.esp_origin_mac()
			mac = mac.replace('\n','').replace('\r','')
			mac = mac.split(":")
			mac_s = '0x'
			for i in range(1, len(mac)):
				mac_s += '%s'%mac[i]
			mac = mac_s
			gen_folder = '%s_%s'%(self.chipv,filetime[0:8])
			data_path2 = data_path1 +'%s/'%(gen_folder)
			if os.path.exists(data_path2) == False:
				os.mkdir(data_path2)
			filename = data_path2
			file_w = '%s_%s.log'%(filename+'/'+mac, filetime)
		else:
			filename = self.get_filename('mod_test', 'mod_test')
			file_w = '%s_%s.log'%(filename, filetime)
		f=open(file_w, 'w')
		result = self.mcu_chl.req_com("esp_en_retest", endstr='MODULE_TEST END!!!')
		f.write(result)
		f.close()

import threading

class ThreadControl(object):
	"""docstring for ThreadControl"""
	def __init__(self,channel):
		self.chip=HALS(channel)

	def connect_instrument(self,instrument=['AWG','EPS','DM_C','DM_V']):
		if 'EPS' in instrument:
			loginfo('EPS')
			self.myeps    = eps(num_of_machine=0)
		if 'EPS_2' in instrument:
			loginfo('EPS_2')
			self.myeps_2    = eps(num_of_machine=1)			
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


		
	def start(self, instr_ls=['EPS', 'EPS_2'],t_delta=0.001):
		'''
		def pulse_gen(instr='EPS',times=1):
			if instr=='EPS':
				# self.myeps.reset()
				# time.sleep(2)
				time.sleep(times)
				self.myeps.pwr(3.3,1)
				time.sleep(10)
				self.myeps.pwr(0,0)
			if instr=='EPS_2':
				# self.myeps_2.reset()
				# time.sleep(2)				
				time.sleep(times)
				self.myeps_2.pwr(3.3,1)
				time.sleep(10)
				self.myeps_2.pwr(0,0)
			elif instr=='AWG':
				# self.myawg.reset()
				# time.sleep(2)
				# self.myawg.appl('DC',0,0,0)
				time.sleep(times)
				self.myawg.appl('DC',0,0,3.3)
				self.myawg.appl('DC',0,0,0)
				

	 	# instr_ls=['EPS', 'AWG']
	 	self.connect_instrument(instr_ls)
	 	# times_ls=[0.831,1.0075]
	 	threads=[]
	 	print 'start..'
	 	for index,instr in enumerate(instr_ls):
	 		print instr,'......'
	 		t = threading.Thread(target=pulse_gen, args=(instr,times_ls[index]))
	 		threads.append(t)
	 	for i in range(len(instr_ls)):
	 		threads[i].start()

	 	for i in range(len(instr_ls)):
	 		threads[i].join()
	 	print 'end..'
	 	'''	

		def pulse_gen_1(times=1,num=1):
			time.sleep(times)
			self.myeps.pwr(3.3,10)
			time.sleep(2)
			self.myeps.pwr(0,0)

		def pulse_gen_2(times=1,num=2):
			time.sleep(times)
			self.myeps_2.pwr(3.3,10)
			time.sleep(2)
			self.myeps_2.pwr(0,0)

		def pulse_gen_3(times=1,num=3):
			# AWG
			time.sleep(times)
			self.myawg.appl('DC',0,0,3.3)

			time.sleep(2)
	 		print self.chip.HWI2C.ulp.o_code
			time.sleep(0.5)
			self.myawg.appl('DC',0,0,0)
			

	 	# self.connect_instrument(instr_ls)
	 	
	 	threads=[]
	 	print 'start..'
	 	delay=1
	 	t1 = threading.Thread(target=pulse_gen_1, args=(delay,2))
	 	t2 = threading.Thread(target=pulse_gen_3, args=(delay+t_delta,3))
	 	t1.start()
	 	t2.start()
	 	time.sleep(0.3)
	 	t1.join()
	 	t2.join()
	 	print 'end..'