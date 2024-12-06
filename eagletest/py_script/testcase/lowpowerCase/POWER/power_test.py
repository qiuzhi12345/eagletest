from hal.Init import HALS
from baselib.instrument.dm import dm
from baselib.instrument.awg import awg
from baselib.instrument.eps import eps
from baselib.loglib.log_csv import csvreport
from baselib.tc_platform.tc_platform import socket_test
from baselib.loglib.log_lib import *
from hal.wifi_api import WIFIAPI
from baselib.instrument.dm import dm
from baselib.instrument.awg import awg

class POWER_TEST():
	def __init__(self, channel, chipv='CHIP722'):
		self.chip = HALS(channel)
		self.channel = self.chip.channel
		self.chipv = self.chip.chipv
		self.mydm = dm(num_of_machine = 0)
		self.awg = awg(num_of_machine = 0)
		self.current_data_path = '/home/lab/job/{}/lowpower_test/current/'.format(self.chipv)

	def write_current(self):
		with open(self.current_data_path + 'IDF_current_{}.csv'.format(time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())), 'w') as cfile:
			for i in range(100):
				value = float(self.mydm.get_result("IDC"))
				cfile.write("%.3f\n"%(value * 1000))

	def deepsleep_current_test(self, dbg = 0, slp_mode = 0x7f, dcap = 0xff, div = 0, ana2_pd = 7):
		dbg_list = [0, 7, 15]
		slp_mode_list = [0x71, 0x7d, 0x7f]
		dcap_div_list = [[0, 0], [30, 0], [80, 0], [150, 0], [0xff, 0], [0xff, 0xff]]
		with open(self.current_data_path + 'deepsleep_current_{}.csv'.format(time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())), 'w') as cfile:
			cfile.write(",")
			for dcap, div in dcap_div_list:
				cfile.write("dcap{}_div{},".format(dcap, div))
			cfile.write("\n")
			for dbg in dbg_list:
				cfile.write("DBG={}\n".format(dbg))
				for slp_mode in slp_mode_list:
					cfile.write("slp_mode={},".format(slp_mode))
					for dcap, div in dcap_div_list:
						self.awg.appl("DC", 0, 0, 0)
						time.sleep(1)
						self.awg.appl("DC", 0, 0, 3.3)
						time.sleep(1.5)
						self.chip.HWREG.RTC_CNTL.RTC_SLOW_CLK_CONF.reg_rtc_ana_clk_div = div
						self.chip.HWREG.RTC_CNTL.RTC_REG.reg_sck_dcap = dcap
						self.chip.riscv.mem_load()
						self.chip.power.deepsleep_cur(dbg, slp_mode)
						time.sleep(25)
						cur_value = float(self.mydm.get_result("IDC", data_type="MIN"))
						cfile.write("%.3f,"%(cur_value * 1000 * 1000))
					cfile.write("\n")
				cfile.write("\n\n")

	def lightsleep_current_test(self, dbg = 0, dig_dbias = 0, slp_mode = 0x0, xtal_fpu = 0, pll_320m_fpu = 0, pll_480m_fpu = 0, apll_fpu = 0, pd_rom_ram_cache = 1, wakeup_opt = 0, slp_time = 0):
		if self.chipv == "ESP32":
			dbg_list = [0, 1, 2, 3]
		else:
			dbg_list = [0, 3, 7, 15]
		dig_dbias_list = [0, 1, 2, 4, 7]
		with open(self.current_data_path + 'lightsleep_current_{}.csv'.format(time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())), 'w') as cfile:
			cfile.write(",Total_Current\n")
			for dbg in dbg_list:
				for dig_dbias in dig_dbias_list:
					cfile.write("dbg{}_digdbias{}:\n".format(dbg, dig_dbias))
					cfile.write("ALL_ON, ")
					self.awg.appl("DC", 0, 0, 0)
					time.sleep(1)
					self.awg.appl("DC", 0, 0, 3.3)
					time.sleep(1.5)
					slp_mode_value = 0
					xtal_fpu_value = 0
					pll_320m_fpu_value = 0
					pll_480m_fpu_value = 0
					apll_fpu_value = 0
					self.chip.power.lightsleep_cur(dbg, dig_dbias, slp_mode=slp_mode_value, wakeup_opt=wakeup_opt, xtal_fpu=xtal_fpu_value, pll_320m_fpu=pll_320m_fpu_value, pll_480m_fpu=pll_480m_fpu_value, apll_fpu=apll_fpu_value)
					time.sleep(10)
					value = float(self.mydm.get_result("IDC"))
					cfile.write("%.3f\n"%(value * 1000))

					cfile.write("VDDSDIO_PD, ")
					self.awg.appl("DC", 0, 0, 0)
					time.sleep(1)
					self.awg.appl("DC", 0, 0, 3.3)
					time.sleep(1.5)
					slp_mode_value = 0x20
					xtal_fpu_value = 0
					pll_320m_fpu_value = 0
					pll_480m_fpu_value = 0
					apll_fpu_value = 0
					self.chip.power.lightsleep_cur(dbg, dig_dbias, slp_mode=slp_mode_value, wakeup_opt=wakeup_opt, xtal_fpu=xtal_fpu_value, pll_320m_fpu=pll_320m_fpu_value, pll_480m_fpu=pll_480m_fpu_value, apll_fpu=apll_fpu_value)
					time.sleep(20)
					value = float(self.mydm.get_result("IDC"))
					cfile.write("%.3f\n"%(value * 1000))

					cfile.write("PD_WIFI, ")
					self.awg.appl("DC", 0, 0, 0)
					time.sleep(1)
					self.awg.appl("DC", 0, 0, 3.3)
					time.sleep(1.5)
					slp_mode_value = 0x40
					xtal_fpu_value = 0
					pll_320m_fpu_value = 0
					pll_480m_fpu_value = 0
					apll_fpu_value = 0
					self.chip.power.lightsleep_cur(dbg, dig_dbias, slp_mode=slp_mode_value, wakeup_opt=wakeup_opt, xtal_fpu=xtal_fpu_value, pll_320m_fpu=pll_320m_fpu_value, pll_480m_fpu=pll_480m_fpu_value, apll_fpu=apll_fpu_value)
					time.sleep(20)
					value = float(self.mydm.get_result("IDC"))
					cfile.write("%.3f\n"%(value * 1000))

					cfile.write("PD_MEM, ")
					self.awg.appl("DC", 0, 0, 0)
					time.sleep(1)
					self.awg.appl("DC", 0, 0, 3.3)
					time.sleep(1.5)
					slp_mode_value = 0xc
					xtal_fpu_value = 0
					pll_320m_fpu_value = 0
					pll_480m_fpu_value = 0
					apll_fpu_value = 0
					self.chip.power.lightsleep_cur(dbg, dig_dbias, slp_mode=slp_mode_value, wakeup_opt=wakeup_opt, xtal_fpu=xtal_fpu_value, pll_320m_fpu=pll_320m_fpu_value, pll_480m_fpu=pll_480m_fpu_value, apll_fpu=apll_fpu_value)
					time.sleep(20)
					value = float(self.mydm.get_result("IDC"))
					cfile.write("%.3f\n"%(value * 1000))
					
					cfile.write("XTAL_ON, ")
					self.awg.appl("DC", 0, 0, 0)
					time.sleep(1)
					self.awg.appl("DC", 0, 0, 3.3)
					time.sleep(1.5)
					slp_mode_value = 0
					xtal_fpu_value = 1
					pll_320m_fpu_value = 0
					pll_480m_fpu_value = 0
					apll_fpu_value = 0
					self.chip.power.lightsleep_cur(dbg, dig_dbias, slp_mode=slp_mode_value, wakeup_opt=wakeup_opt, xtal_fpu=xtal_fpu_value, pll_320m_fpu=pll_320m_fpu_value, pll_480m_fpu=pll_480m_fpu_value, apll_fpu=apll_fpu_value)
					time.sleep(10)
					value = float(self.mydm.get_result("IDC"))
					cfile.write("%.3f\n"%(value * 1000))
					
					cfile.write("PLL320M_ON, ")
					self.awg.appl("DC", 0, 0, 0)
					time.sleep(1)
					self.awg.appl("DC", 0, 0, 3.3)
					time.sleep(1.5)
					slp_mode_value = 0
					xtal_fpu_value = 0
					pll_320m_fpu_value = 1
					pll_480m_fpu_value = 0
					apll_fpu_value = 0
					self.chip.power.lightsleep_cur(dbg, dig_dbias, slp_mode=slp_mode_value, wakeup_opt=wakeup_opt, xtal_fpu=xtal_fpu_value, pll_320m_fpu=pll_320m_fpu_value, pll_480m_fpu=pll_480m_fpu_value, apll_fpu=apll_fpu_value)
					time.sleep(20)
					value = float(self.mydm.get_result("IDC"))
					cfile.write("%.3f\n"%(value * 1000))

					cfile.write("PLL480M_ON, ")
					self.awg.appl("DC", 0, 0, 0)
					time.sleep(1)
					self.awg.appl("DC", 0, 0, 3.3)
					time.sleep(1.5)
					slp_mode_value = 0
					xtal_fpu_value = 0
					pll_320m_fpu_value = 0
					pll_480m_fpu_value = 1
					apll_fpu_value = 0
					self.chip.power.lightsleep_cur(dbg, dig_dbias, slp_mode=slp_mode_value, wakeup_opt=wakeup_opt, xtal_fpu=xtal_fpu_value, pll_320m_fpu=pll_320m_fpu_value, pll_480m_fpu=pll_480m_fpu_value, apll_fpu=apll_fpu_value)
					time.sleep(20)
					value = float(self.mydm.get_result("IDC"))
					cfile.write("%.3f\n"%(value * 1000))

					cfile.write("APLL_ON, ")
					self.awg.appl("DC", 0, 0, 0)
					time.sleep(1)
					self.awg.appl("DC", 0, 0, 3.3)
					time.sleep(1.5)
					slp_mode_value = 0
					xtal_fpu_value = 0
					pll_320m_fpu_value = 0
					pll_480m_fpu_value = 0
					apll_fpu_value = 1
					self.chip.power.lightsleep_cur(dbg, dig_dbias, slp_mode=slp_mode_value, wakeup_opt=wakeup_opt, xtal_fpu=xtal_fpu_value, pll_320m_fpu=pll_320m_fpu_value, pll_480m_fpu=pll_480m_fpu_value, apll_fpu=apll_fpu_value)
					time.sleep(20)
					value = float(self.mydm.get_result("IDC"))
					cfile.write("%.3f\n\n"%(value * 1000))

				cfile.write("\n")

	def lightsleep_current_trend_test(self, dbg=7, dig_dbias = 4, wakeup_opt = 0):
		with open(self.current_data_path + 'lightsleepcurrent_dbg{}_dbias{}_{}.csv'.format(dbg, dig_dbias,time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())), 'w') as cfile:
			test_num = 1
			cfile.write("waittime, ")
			for i in range(40):
				waittime = i * 0.5
				cfile.write("%.1f, "%(waittime))
			cfile.write("\n")
			for times in range(test_num):
				self.awg.appl("DC", 0, 0, 0)
				time.sleep(1)
				self.awg.appl("DC", 0, 0, 3.3)
				time.sleep(1.5)
				cfile.write("times_%d,"%(times))
				self.chip.power.lightsleep_cur(dbg, dig_dbias, wakeup_opt=wakeup_opt)
				value = float(self.mydm.get_result("IDC"))
				cfile.write("%.3f,"%(value * 1000))
				for i in range(39):
					waittime = (i + 1) * 0.5
					time.sleep(waittime)
					value = float(self.mydm.get_result("IDC"))
					cfile.write("%.3f,"%(value * 1000))
				cfile.write("\n")

	def modemsleep_current_test(self):
		'''
		should connected GPIO1 to GND by default
		- wifi_peri_list: [wifi_pd_value, wifi_clkgating_value, peri_clkgating_value]
			- WIFI_CLKGATING: [0, 1, 0];
			- wifi&peri_clking: [0, 1, 1];
			- wifipd_periclkgating: [1, 0, 1].
		- cpu_state_list: [cpu_run_value, cpu_waiti_value]
		'''
		delay_time = 2
		wifi_peri_list = [[0, 1, 0], [0, 1, 1], [1, 1, 1]]
		cpu_state_list = [[1, 0], [0, 1]]
		dig_dbias_list = [0, 1, 2, 3, 4, 5, 6, 7]
		if self.chipv == "ESP32":
			cpu_freq_list = [3, 2, 1, 0]
		else:
			cpu_freq_list = [3, 2, 1, 0, 7, 8, 9]
		with open(self.current_data_path + 'modemsleep_current_{}.csv'.format(time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())), 'w') as cfile:
			for wifi_pd_value, wifi_clkgating_value, peri_clkgating_value in wifi_peri_list:
				if (wifi_pd_value == 0) and (wifi_clkgating_value == 1) and (peri_clkgating_value == 0):
					cfile.write("wificlkgating:\n")
				elif (wifi_pd_value == 0) and (wifi_clkgating_value == 1) and (peri_clkgating_value == 1):
					cfile.write("wificlkgating_periclkgating:\n")
				elif (wifi_pd_value == 1) and (wifi_clkgating_value == 1) and (peri_clkgating_value == 1):
					cfile.write("wifipd_wificlkgating_periclkgating:\n")

				dig_dbias_value = 4
				for cpu_run_value, cpu_waiti_value in cpu_state_list:
					if cpu_run_value:
						cfile.write("CPU_KEEPRUNNING:\n")
					else:
						cfile.write("CPU_WAITI:\n")
					for cpu_freq_value in cpu_freq_list:
						cfile.write("cpu_freq{},".format(cpu_freq_value))
						self.awg.appl("DC", 0, 0, 0)
						time.sleep(1)
						self.awg.appl("DC", 0, 0, 3.3)
						time.sleep(1.5)
						self.chip.power.modemsleep_cur(cpu_freq = cpu_freq_value, wifi_pd = wifi_pd_value, wifi_clkgating = wifi_clkgating_value, peri_clkgating = peri_clkgating_value, cpu_waiti = cpu_waiti_value, cpu_keeprun = cpu_run_value, dig_dbias = dig_dbias_value)
						time.sleep(delay_time)
						value = float(self.mydm.get_result("IDC"))
						cfile.write("%.3f\n"%(value * 1000))

				cpu_freq_value = 1
				cpu_run_value = 1
				cfile.write("CPU_KEEPRUNNING & CPU_FREQ{}:\n".format(cpu_freq_value))
				for dig_dbias_value in dig_dbias_list:
					cfile.write("dig_dbias{},".format(dig_dbias_value))
					self.awg.appl("DC", 0, 0, 0)
					time.sleep(1)
					self.awg.appl("DC", 0, 0, 3.3)
					time.sleep(1.5)
					self.chip.power.modemsleep_cur(cpu_freq = cpu_freq_value, wifi_pd = wifi_pd_value, wifi_clkgating = wifi_clkgating_value, peri_clkgating = peri_clkgating_value, cpu_keeprun = cpu_run_value, dig_dbias = dig_dbias_value)
					time.sleep(delay_time)
					value = float(self.mydm.get_result("IDC"))
					cfile.write("%.3f\n"%(value * 1000))
				cfile.write("\n\n")

			cfile.write("poweronphy_periclkgating\n")
			cpu_freq_value = 1
			cfile.write("CPU_WAITI: \n")
			cfile.write("cpu_freq{}, ".format(cpu_freq_value))
			self.awg.appl("DC", 0, 0, 0)
			time.sleep(1)
			self.awg.appl("DC", 0, 0, 3.3)
			time.sleep(1.5)
			self.chip.power.modemsleep_cur(close_phy = 0, cpu_freq = cpu_freq_value, peri_clkgating = 1, cpu_waiti = 1)
			time.sleep(delay_time)
			value = float(self.mydm.get_result("IDC"))
			cfile.write("%.3f\n\n"%(value * 1000))

			cfile.write("usecache_wificlkgating_periclkgating: \n")
			cpu_freq_list2 = [3, 2, 1, 0]
			cfile.write("USE CACHE:\n")
			for cpu_freq_value in cpu_freq_list2:
				cfile.write("cpu_freq{},".format(cpu_freq_value))
				self.awg.appl("DC", 0, 0, 0)
				time.sleep(1)
				self.awg.appl("DC", 0, 0, 3.3)
				time.sleep(1.5)
				self.chip.power.modemsleep_cur(cpu_freq = cpu_freq_value, wifi_clkgating = 1, peri_clkgating = 1, use_cache = 1)
				time.sleep(delay_time)
				value = float(self.mydm.get_result("IDC"))
				cfile.write("%.3f\n"%(value * 1000))
			
			cfile.write("NOT USE CACHE:\n")
			for cpu_freq_value in cpu_freq_list2:
				cfile.write("cpu_freq{},".format(cpu_freq_value))
				self.awg.appl("DC", 0, 0, 0)
				time.sleep(1)
				self.awg.appl("DC", 0, 0, 3.3)
				time.sleep(1.5)
				self.chip.power.modemsleep_cur(cpu_freq = cpu_freq_value, wifi_clkgating = 1, peri_clkgating = 1, cpu_keeprun = 1)
				time.sleep(delay_time)
				value = float(self.mydm.get_result("IDC"))
				cfile.write("%.3f\n"%(value * 1000))

	def current_test(self):
		self.deepsleep_current_test()
		self.lightsleep_current_test()
		self.modemsleep_current_test()
