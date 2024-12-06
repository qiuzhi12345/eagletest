from baselib.loglib.log_csv import csvreport
from baselib.instrument.eps import eps
from baselib.instrument.awg import awg
from baselib.instrument.dm import dm
from baselib.loglib.log_lib import *
from hal.Init import HALS
import time

class ChipPuPtest(object):
	"""docstring for CHIP_PU"""
	def __init__(self, channel, chipv='CHIP722', myeps=None):
		self.channel = channel
		self.chipv 	 = chipv
		self.chip 	 = HALS(channel, chipv)
		if eps!=None:
			self.myeps=myeps

	def connect_instrument(self):
		'''
		:brief:
			Communication between instrument and PC by USB-GPIB interface
		:param:
			- eps: supply voltage for chip_pu scan the threshold 
		'''
		self.myeps = eps()
		self.mydm  = dm()

	def set_flag(self, flg_set):
		'''
		:brief:
			write one bit register with value for chip reset check
		:param:	
			flg_set: set diff value with default
		'''
		if self.chipv == "ESP32":	
			flg = self.chip.HWREG.RTC_CNTL.RTC_BROWN_OUT.reg_dbrown_out_thres = 3
		elif self.chipv == "CHIP722":
			flg = self.chip.HWI2C.ulp.dbrown_out_thres = flg_set			
		loginfo('set flg', flg)
		return flg

	def read_flag(self, default=False):
		'''
		:brief:
			read the flag value 
		:param:
		'''
		if default:
			if self.chipv == 'ESP32':
				
				dft_flg = self.chip.HWREG.RTC_CNTL.RTC_BROWN_OUT.reg_dbrown_out_thres
			elif self.chipv == 'CHIP722':
				dft_flg = self.chip.HWI2C.ulp.dbrown_out_thres
			return dft_flg
		if self.chipv == "ESP32":
			flg = self.chip.HWREG.RTC_CNTL.RTC_BROWN_OUT.reg_dbrown_out_thres
		elif self.chipv == "CHIP722":
			flg = self.chip.HWI2C.ulp.dbrown_out_thres
		loginfo('read flg',flg)
		return flg
	
	def pulse_generator(self, ctl_channnel, rtcIO = 12, width_us = 20, drv = 3, mode = 0 ,first = False):
		'''
		:brief:
			generate pulse
		:param:
			- ctl_channnel: the com(n) of the generate pulse chip
			- rtcIO: pulse output IO
			- width_us: pulse width(us)
			- drv: IO drive(0~3)
			- mode: pulsemode 0:1-0-1, 1:0-1-0
		'''		
		# if self.chipv=='ESP32':
		self.pulse_gen = HALS(ctl_channnel,'ESP32' )
		if mode == 0 :
			if first:
				self.pulse_gen.gpio.rtc_gpio_out(rtcIO, 1, 3)
		self.pulse_gen.rtc_debug.gpio_pulse(rtc_gpio_no=rtcIO, drv=drv, delay_us=width_us, mode=mode)

	def scan_pulse_width(self, ctl_chl, ctl_rtcIO = 12, width_rg_us = [1,100], step = 10):
		'''
		:brief:
			Measure the reset pulse off Chip_PU
		:param:
			- ctl_chl: the com(n) of the generate pulse chip
			- ctl_rtcIO: pulse output IO
			- width_rg_us: pulse width scan range
		'''
		self.channel.req_com_timeout_block=True
		self.channel.ser.timeout=1
		loginfo('chip com timeout set',self.channel.ser.timeout)
		log 	= csvreport('CHIP_PU/ChipPu_PulseWidth')
		col_ls  = ['PULSE_WIDTH(us)', 'FLAG1', 'FLAG2', 'RESET']
		res_ls  = []
		
		self.pulse_generator(ctl_channnel=ctl_chl, rtcIO=ctl_rtcIO, width_us=1000, first=True)
		loginfo('chipen_on')		
		time.sleep(2)
		dft_flg = self.read_flag(True)
		loginfo("default_flg:",dft_flg)
		f_ls=['reset False']
		t_ls=['reset True']
		na_ls=['no return']	
		for width in range(width_rg_us[1], width_rg_us[0], -step):
			loginfo('pulsewidth %dus testing...' % width)
			self.pulse_generator(ctl_channnel=ctl_chl, rtcIO=ctl_rtcIO, width_us=1000,first=True)
			time.sleep(2)
			self.set_flag(dft_flg+1)
			flg_1 = self.read_flag()
			time.sleep(8)			
			self.pulse_generator(ctl_channnel=ctl_chl, rtcIO=ctl_rtcIO, width_us=width)	
			loginfo('chip reseting...')
			time.sleep(2)
			flg_2  = self.read_flag()
			if flg_1!=flg_2 and flg_2==dft_flg:
				reset=True
				t_ls.append(width)
				loginfo('reset True')
			elif flg_1==flg_2:
				reset=False
				f_ls.append(width)
				logres('reset flag False ')
			else:
				reset=flg_2
				na_ls.append(width)
				logres('reset no return ')
			res_ls = [width, flg_1, flg_2, reset]
			log.write_value(col_ls, res_ls)
			log.flush_line()
			logwarn(width,'RESET:',reset)
		return 	t_ls,f_ls,na_ls
	def chippu_vth(self, Von_l=1500,Von_h=2500,Voff_l=1000,Voff_h=1800,step=50):
		'''
		:brief:
			Measure  the threshold voltage of the Chip_PU
		:param: 	
			- Von_l  :  the min point for scan the lowest voltage(mV) required to make the chip work
			- Von_h  :  the max point for scan the lowest voltage(mV) required to make the chip work
			- Voff_l :  the min point for scan the highest voltage(mV) required to make the chip shutdown		
			- Voff_h :  the max point for scan the highest voltage(mV) required to make the chip shutdown
			- step   :  step for the scan range 
		'''			
		if self.chipv == 'ESP32':
			pass
		elif self.chipv == 'CHIP722':
			self.myeps.pwr(0,0)
			time.sleep(2)
			for chipen in range(Von_l, Von_h, step):
				self.myeps.pwr(chipen/1000.0, 0.5)
				time.sleep(3)
				self.channel.req_com('check',1)
				mac=self.channel.req_com('efuse_rd_mac_hi',1) + self.channel.req_com("efuse_rd_mac_lo",1) #to be updated once commands is merged to HALS				
				if mac!='':
					logwarn('%r(mv): chip is active:%r'% (chipen, mac))
					mac_on=mac
					break
				else:
					mac_on=''
					continue
			for chipen_off in range(Voff_h, Voff_l, -step):
				self.myeps.pwr(chipen_off/1000.0, 0.5)
				time.sleep(3)
				self.channel.req_com('check',1)
				mac=self.channel.req_com('efuse_rd_mac_hi',1) + self.channel.req_com("efuse_rd_mac_lo",1)
				if mac=='':
					logwarn('%r(mv): chip is down:%r'% (chipen_off, mac))
					break
				else:
					loginfo('chippu:%r(mV), mac:%r'%(chipen_off,mac))
					continue
			self.myeps.pwr(0, 0)
			
			col_ls = ['CHIPMAC','CHIP_PU_ON', 'CHIP_PU_OFF']
			val_ls = [mac_on, chipen, chipen_off]
			logwarn(col_ls,val_ls)
			return [col_ls,val_ls]



