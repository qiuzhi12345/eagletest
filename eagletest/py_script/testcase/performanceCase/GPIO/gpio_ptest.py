from baselib.loglib.log_csv import csvreport
from baselib.loglib.log_lib import *
from baselib.instrument.dm import dm
from baselib.instrument.awg import awg
from baselib.instrument.eps import eps
from hal.Init import HALS

class GpioPtest(object):
	"""docstring for GPIO_PTEST"""
	def __init__(self, channel):
		self.channel = channel
		self.chip 	 = HALS(self.channel)

	def connect_instrument(self):
		'''
		:brief:
			Communication between instrument and PC by USB-GPIB interface
		:param:
			- eps: supply diff voltage
			- dm_curr: test the current
		'''
		loginfo('eps')
		self.myeps    = eps()
		self.mydm_cur = dm(num_of_machine=1)
		self.mydm_cur.get_result('IDC')

	def gpio_input_test(self, rtcIO = 1, vol_ls = range(0,3300,100)):
		'''
		:brief:
			scan the gpio input thres
		:param:
			- rtcIO: RTC_IO num
			- vol_ls: input voltage(mV) scan range
		'''		
		log    = csvreport('GPIO/GPIO_INPUT')
		col_ls = ['RTC_GIPO', 'INPUT(V)', 'STATE']
		for vol_m in vol_ls:
			vol = vol_m/1000.0
			self.myeps.pwr(vol, 0.5)
			val    = self.chip.gpio.rtc_gpio_in(rtcIO)
			val_ls = [rtcIO, vol, val]
			log.write_value(col_ls, val_ls)
		log.flush_line()
		self.myeps.pwr(0, 0.5)

	def gpio_output_curr(self, rtcIO = 1, drv_ls = [0,1,2,3], pw_ls = range(0,3301,100)):
		'''
		:brief:
			scan the gpio output current
		:param:
			- rtcIO: RTC_IO num
			- drv_ls: IO drive(0~3)
			- pw_ls: supply voltage
		'''
		log_c = csvreport('/GPIO/current')		
		logwarn('output_1 test...')
		for pw_m in pw_ls:
			pw = pw_m/1000.0
			col_ls = ['RTC_GIPO', 'IO_OUT', 'BIAS(V)']
			val_ls = [rtcIO, 1, pw]
			self.myeps.pwr(pw, 0.5)
			for drv in drv_ls:			
				self.chip.gpio.rtc_gpio_out(rtcIO, 1, drv)
				curr = self.mydm_cur.get_result('IDC')
				col_ls.append('I(A)_DRV%d' % drv)
				val_ls.append(curr)			
			log_c.write_value(col_ls, val_ls)

		logwarn('output_0 test...')
		for pw_m in pw_ls:
			pw = pw_m/1000.0
			col_ls = ['RTC_GIPO', 'IO_OUT', 'BIAS(V)']
			val_ls = [rtcIO, 0, pw]
			self.myeps.pwr(pw, 0.5)
			for drv in drv_ls:
				self.chip.gpio.rtc_gpio_out(rtcIO, 0, drv)
				curr = -float(self.mydm_cur.get_result('IDC'))
				col_ls.append('I(A)_DRV%d' % drv)
				val_ls.append(curr)				
			log_c.write_value(col_ls, val_ls)
		log_c.flush_line()
		self.myeps.pwr(0, 0)

	def gpio_pupd_resistor(self, rtcIO = 1, pw_ls = range(0,3301,100)):	
		'''
		:brief:
			- PULL UP/DOWN Resistor Test
		:param:
			- rtcIO: RTC_IO num
			- pw_ls: supply voltage			
		'''
		log_r  = csvreport('/GPIO/resistor')
		col_ls = ['RTC_GIPO', 'PU_BIAS(V)','CURRENT', 'R(OHM)']
		self.chip.gpio.rtc_gpio_out(rtcIO, 0, 0)
		self.chip.gpio.rtc_gpio_hang_up(rtcIO)
		logwarn('pull up test...')
		for pw_m in pw_ls:
			pw 	   = pw_m/1000.0
			self.chip.gpio.rtc_gpio_pu(rtcIO,1)
			self.myeps.pwr(pw, 0.5)
			curr   = self.mydm_cur.get_result('IDC')
			Rpu    = (3.3-pw)/float(curr)
			Rpu_ls = [rtcIO, pw, curr, Rpu]
			log_r.write_value(col_ls, Rpu_ls)
			# raw_input('recode voltage....')
		self.chip.gpio.rtc_gpio_pu(rtcIO,0)

		logwarn('pull down test...')
		for pw_m in pw_ls:
			pw 	   = pw_m/1000.0
			self.chip.gpio.rtc_gpio_pd(rtcIO,1)
			self.myeps.pwr(pw, 0.5)
			curr   = -float(self.mydm_cur.get_result('IDC'))
			Rpd    = pw/float(curr)
			Rpd_ls = [rtcIO, pw, curr, Rpd]
			log_r.write_value(col_ls, Rpd_ls)
			# raw_input('recode voltage....')
		self.chip.gpio.rtc_gpio_pd(rtcIO,0)
		log_r.flush_line()
		self.myeps.pwr(0, 0.5)
