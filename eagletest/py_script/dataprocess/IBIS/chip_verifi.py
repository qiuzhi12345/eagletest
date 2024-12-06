#below commands require eagletest platform support
from baselib.instrument.eps import eps
from baselib.instrument.dm import dm
from baselib.instrument.awg import awg
from baselib.instrument.allInOne import allInOne
from collections import defaultdict
import numpy as np
import pandas as pd
import matplotlib.cm as cm

class ibisChipMeas(object):
	'''script used to verify gpio pin i-v curve under multiple modes
	'''
	def __init__(self):
		'''below instruments required for test automation
		
			- E3633A, 34401A, U3606B, 33120A
		'''
		self.veri_f_path = '/home/test/Desktop/IBIS/ESP32_board_veri/'
		if not os.path.exists(self.veri_f_path):os.makedirs(self.veri_f_path)
		self.myeps = eps()
		self.mydm  = dm()
		self.myawg = awg()
		self.myaio = allInOne()

	def io_tbl(self):
		'''IO pin name mapping

		- PIN NAME:   actual pin name on chip
		- IO NUM:     name used as rtc_io/dig_io/etc.
		- SUP_DOMAIN: power domain where this pin belongs to
		'''
		io_tbl = pd.DataFrame()
		io_tbl['PIN_NAME']   = ['SD3', 12,   15,   17,    18,   22,   23,   25,   26,   27]
		io_tbl['IO_NUM']     = [10,    15,   13,   17,    18,   22,   23,   6,    7,    17]
		io_tbl['SUP_DOMAIN'] = ['SDIO','RTC','RTC','SDIO','CPU','CPU','CPU','RTC','RTC','RTC']
		return self.df_io_tbl

	def ibis_gpio_config(self,mode,pull=0,drv=0,io_num=6, pin_num = '25'):
		'''use GPIO25 (RTC_IO6) as pin for test

			- :param mode: 
				- choose gpio mode: output, input, resistor pull
				- 'o', 'i', 'r'
			- :param pull: 
				- 1 for pullup, 0 for pulldown
				- resistor pull mode: -1 for hangup
			- :param drv:  choose output strength, 0-3
			- :param io_num: GPIO25 is RTC#6
		'''
		if mode == 'i':
			#input mode
			logwarn('GPIO%s in INPUT mode'%pin_num)
			return chip.hals.gpio.rtc_gpio_in(io_num)
		elif mode == 'o':
			#output mode 			
			chip.hals.gpio.rtc_gpio_pu(io_num,0)
			chip.hals.gpio.rtc_gpio_pd(io_num,0)
			chip.hals.gpio.rtc_gpio_out(io_num,pull,drv=drv)
			p_t = 'UP' if pull == 1 else 'DOWN'
			logwarn('GPIO%s in OUTPUT mode\nPull: %s\nDrive: %d\n'%(pin_num,p_t,drv))
		elif mode == 'r':
			#resistor pull up & down mode
			if pull == 1:
				chip.hals.gpio.rtc_gpio_pd(io_num,0)
				chip.hals.gpio.rtc_gpio_pu(io_num,1)
				logwarn('GPIO%s in RESISTOR PULL mode: UP'%pin_num)
			elif pull == 0:
				chip.hals.gpio.rtc_gpio_pu(io_num,0)
				chip.hals.gpio.rtc_gpio_pd(io_num,1)
				logwarn('GPIO%s in RESISTOR PULL mode: DOWN'%pin_num)
			elif pull == -1:
				chip.hals.gpio.rtc_gpio_pu(io_num,0)
				chip.hals.gpio.rtc_gpio_pd(io_num,0)
				chip.hals.gpio.rtc_gpio_hang_up(io_num)
				logwarn('GPIO%s in RESISTOR PULL mode: HANGUP'%pin_num)

	def ibis_dig_gpio_config(self,mode,pull=0,drv=0,io_num=22, pin_num ='22'):
		'''use GPIO2 as pin for test

			- :param mode: 
				- choose gpio mode: output, input, resistor pull
				- 'o', 'i', 'r'
			- :param pull: 
				- 1 for pullup, 0 for pulldown
				- resistor pull mode: -1 for hangup
			- :param drv:  choose output strength, 0-3
			- :param io_num: GPIO25 is RTC#6
		'''
		if mode == 'i':
			#input mode
			logwarn('GPIO%s in INPUT mode'%pin_num)
			return chip.hals.gpio.dig_gpio_in(io_num)
		elif mode == 'o':
			#output mode 			
			chip.hals.gpio.dig_gpio_pu(io_num,0)
			chip.hals.gpio.dig_gpio_pd(io_num,0)
			chip.hals.gpio.dig_gpio_out(io_num,pull,drv=drv)
			p_t = 'UP' if pull == 1 else 'DOWN'
			logwarn('GPIO%s in OUTPUT mode\nPull: %s\nDrive: %d\n'%(pin_num,p_t,drv))
		elif mode == 'r':
			#resistor pull up & down mode
			if pull == 1:
				chip.hals.gpio.dig_gpio_pd(io_num,0)
				chip.hals.gpio.dig_gpio_pu(io_num,1)
				logwarn('GPIO%s in RESISTOR PULL mode: UP'%pin_num)
			elif pull == 0:
				chip.hals.gpio.dig_gpio_pu(io_num,0)
				chip.hals.gpio.dig_gpio_pd(io_num,1)
				logwarn('GPIO%s in RESISTOR PULL mode: DOWN'%pin_num)
			elif pull == -1:
				chip.hals.gpio.dig_gpio_pu(io_num,0)
				chip.hals.gpio.dig_gpio_pd(io_num,0)
				chip.hals.gpio.dig_gpio_hang_up(io_num)
				logwarn('GPIO%s in RESISTOR PULL mode: HANGUP'%pin_num)

	def supl(self,vol, ilim = 20):
		'''power supply'''
		self.myeps.pwr(vol, ilim)
		loginfo('Supply sets to %.2fV, w/ current limit %.2f'%(vol,ilim))

	def digm(self,m_type='VDC', u_uA=False):
		'''digital multimeter'''
		val = float(self.mydm.get_result(m_type))
		unit = 'V' if m_type == 'VDC' else 'A'
		ratio = 1 
		if u_uA: 
			unit  ='uA'
			ratio = 1e6
		loginfo('DM reads %s: %.2f%s'%(m_type,val*ratio,unit))
		return val

	def sigg(self,vol):
		'''signal generator'''
		self.myawg.appl('DC',0,0,vol)
		loginfo('Signal Gen sets to %.2fV'%vol)

	def reset_all(self):
		self.myaio.sour_out() #turn off pin bias
		self.supl(0.0)        #turn off power supply
		self.self.sigg(0.0)        #turn off signal generator

	def inpt_vth(self,edge_type='r', scan_btm=1.0, scan_top=2.0,step=0.05):
		'''search for input mode vthh & vthl'''
		if edge_type == 'r':
			self.sigg(scan_btm)
		elif edge_type == 'f':
			self.sigg(scan_top)
			scan_btm, scan_top = scan_top, scan_btm

		time.sleep(0.5)
		vth_l = defaultdict(list)
		for i in np.linspace(scan_btm,scan_top,abs(scan_top - scan_btm)/step):
			self.sigg(i)
			time.sleep(0.2)
			vth_l['V_INPUT'].append(i)
			vth_l['READs'].append(self.ibis_gpio_config('i'))
		df_vth = pd.DataFrame(vth_l)
		df_    = df_vth.drop_duplicates(subset=['READs'])
		if edge_type == 'r':
			vth = df_['V_INPUT'][df_['READs']=='1'].values[0]
			loginfo( 'VTH_H: %.2fV'%vth)
		elif edge_type == 'f':
			vth = df_['V_INPUT'][df_['READs']=='0'].values[0]
			loginfo( 'VTH_L: %.2fV'%vth)
		return vth

	def inpt_vth_tbl(self,step_size=0.02):
		'''scans input thresholds at 3 supply
		
		results is saved to ~/Desktop/IBIS/ESP32_board_veri/
		'''
		vth_tbl = defaultdict(list)
		supl_l  = [2.7,3.3,3.6]
		for i in supl_l:
			self.supl(i)
			vth_tbl['SUPPLY'].append(i)
			time.sleep(2)
			vth_tbl['VTH_H'].append(self.inpt_vth(edge_type='r',step=step_size))
			vth_tbl['VTH_F'].append(self.inpt_vth(edge_type='f',step=step_size))
		df_i_vth_t = pd.DataFrame(vth_tbl)
		df_i_vth_t.to_csv(self.veri_f_path+'inpt_vth.csv',index=False)
		return df_i_vth_t

	def otpt_dc(self,mode= 'o',pull = 1, r_load = 50, drv=0,io_num=6, pin_num = '25'):
		'''checks pin voltage level @ given load condition & drive strength'''
		tie_ = 'GND' if pull == 1 else 'VDD'
		mode_print = 'OUTPUT' if mode == 'o' else 'RESISTOR PULL'
		logwarn('PREPARE to test GPIO%s mode: %s\n'%(pin_num, mode_print))
		confirm_act = raw_input('ACTION:\nConnect load %s ohm to GPIO%s & %s\nTYPE c to confirm\n'%(r_load,pin_num,tie_))
		if confirm_act == 'c':
			self.ibis_gpio_config(mode=mode,pull=pull,drv=drv,io_num=io_num,pin_num=pin_num)
			time.sleep(0.1)
			pin_vol = self.digm()
			self.ibis_gpio_config(mode='r',pull=-1,drv=drv,io_num=io_num,pin_num=pin_num) #hangup GPIO25
		return pin_vol

	def otpt_tbl(self,mode='o',r_load=50,io_num=6, pin_num = '25'):
		'''checks pin voltage level with given load @ 3 supply and all drive strength
		'''
		o_tbl = defaultdict(list)
		for i_p in [0,1]:
			pull_type = 'UP' if i_p == 1 else 'DN'
			tie_      = 'GND' if i_p == 1 else 'VDD'
			logwarn('\n*** NOTE!!! ****\nPREPARE to measure PULL %s\nCONNCECT load to %s\n*********\n'%(pull_type,tie_))
			for i in [2.7,3.3,3.6]:
				self.supl(i)
				time.sleep(2)
				o_tbl['SUPPLY'].append(i)
				o_tbl['PULL'].append(pull_type)
				if mode == 'o':
					for i_d in [0,1,2,3]:
						o_tbl['DRV%d'%i_d].append(otpt_dc(mode=mode,pull=i_p,r_load=r_load,drv=i_d))
				elif mode == 'r':
					o_tbl['VPin'].append(otpt_dc(mode=mode,pull=i_p,r_load=r_load,drv=0))

		if mode == 'o':
			df_o_tbl = pd.DataFrame(o_tbl,columns=['SUPPLY','PULL','DRV0','DRV1','DRV2','DRV3'])
			df_o_tbl.to_csv(self.veri_f_path+'otpt_r_%sohm.csv'%r_load, index=False)
		else:
			df_o_tbl = pd.DataFrame(o_tbl,columns=['SUPPLY','PULL','VPin'])
			df_o_tbl.to_csv(self.veri_f_path+'rpud_r_%sohm.csv'%r_load, index=False)

	def clamp_iv(self,v_supl=3.3,clamp_type='pwr', end_pnt=4.0, step_size=0.1,io_num=6, pin_num = '25',interact=False,dig=False):
		'''measure power clamp iv curve, raise pin voltage above supply
		'''
		f_to_sv = self.veri_f_path+'clamp_%s_gpio_%s.csv'%(clamp_type,pin_num)
		self.supl(v_supl)
		time.sleep(2)
		if not dig:
			self.ibis_gpio_config(mode='r',pull=-1,io_num=io_num,pin_num=pin_num) #hangup gpio
		else:
			self.ibis_dig_gpio_config(mode='r',pull=-1,io_num=io_num,pin_num=pin_num) #hangup gpio
		with open(f_to_sv, 'a+') as f:
			f.write('V_pin,I_pin(uA)\n')
			f.flush()

		start_pnt = v_supl-step_size if clamp_type == 'pwr' else 0
		for i in np.linspace(start_pnt, end_pnt, abs(end_pnt - start_pnt)/step_size+1 ):
			if clamp_type == 'pwr':
				self.myaio.sour(lvl=float(i),out='ON')
				v_val = i
			elif clamp_type == 'gnd':
				self.sigg(float(i))
				time.sleep(0.5)
				v_val = self.myaio.meas()
			if interact: 
				confirm_act = raw_input('ACTION:\nChange Pin Bias to %sV\nTYPE c to confirm, TYPE q to quit\n'%(i))
			else:
				time.sleep(1)
				confirm_act = 'c'
			if confirm_act == 'c':
				i_val = self.digm(m_type='IDC',u_uA=True)
				with open(f_to_sv, 'a+') as f:
					f.write('%.2f, %.2f\n'%(v_val,i_val*1e6))
			elif confirm_act == 'q':
				self.myaio.sour_out() #turn off pin bias
				return 
		self.myaio.sour_out() #turn off pin bias

	def plt_all(self,df_io_tbl):
		colors_use = cm.rainbow(np.linspace(0, 1, len(df_io_tbl)))
		for i in df_io_tbl.index:
			pin_n = df_io_tbl.loc[i]['PIN_NAME']
			io_n  = df_io_tbl.loc[i]['IO_NUM']
			sup_d = df_io_tbl.loc[i]['SUP_DOMAIN']
			df_t = pd.read_csv(self.veri_f_path+'clamp_pwr_gpio_%s.csv'%pin_n)
			x = df_t['V_pin']
			y = df_t['I_pin(uA)']
			plt.scatter(x,y,label='GPIO%s_%s'%(pin_n,sup_d),color=colors_use[i])
		plt.legend(loc=0)
		plt.xlabel('V_pin(V)')
		plt.xlabel('I_pin(uA)')
		plt.title('ESP32 GPIO POWER CLAMP plot')