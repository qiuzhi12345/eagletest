import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from collections import defaultdict
from matplotlib.ticker import MultipleLocator 
from matplotlib.ticker import FormatStrFormatter
plt.ion()


class saradcCalibration(object):
	'''a class to be used for SAR-ADC calibration 
	'''
	def __init__(self, data_path, step_size=10, inpt_high=3300, inpt_low=10):
		'''
		'''
		#four modes of attenuation
		self.aten_l = [1.0, 0.75, 0.5, 0.25]     
		#lit of plot x-axis top limit
		self.xlim_l = [1100, 1470, 2200, 2500]   
		#two poiint calibration selections for each attnuation mode
		self.cal_point_l = [(150,850),(150,1200),(550, 1800),(150,2250)] 
		#ideal adc output formula
		self.adc   = lambda x: 4095.0/1100*(x)
		#ideal adc input voltage formula
		self.adc_r = lambda x: (x)/4095.0*1100
		#adc data file read in
		self.df = pd.read_csv(data_path)
		#adc data input voltage step size
		self.step_size = step_size
		#adc data input voltage range
		self.inpt_range = range(inpt_low, inpt_high+1, step_size)
		#adc data column naming method for input voltages
		self.col_n = lambda x:'INPUT_%d(mV)'%x
		#list of column names for input voltages 
		self.head_list = [self.col_n(i) for i in self.inpt_range]
		#condition list
		self.group_l = ['TEMP', 'ATTEN', 'ADC','CHIP#']

	def _data_pick(self, chip_num=0, adc=2, temp=25, atten=0):
		'''pick data from file based on given conditions
		'''
		dfg = self.df.groupby(by=self.group_l)
		df_use = dfg.get_group((temp, atten, adc, chip_num))
		return df_use

	def eror_est_2point_cal(self, chip_num=0, cal_point=[150,850], chk_adc=2, cal_temp=25, cal_method=1):
		'''table to visualize error 
		'''
		dict_e = defaultdict(list)
		for i in self.df['ATTEN'].drop_duplicates().tolist():
			cal_p = cal_point if cal_method==1 else self.cal_point_l[i]
			df_use = self._data_pick(temp=cal_temp, atten=i, adc=chk_adc, chip_num=chip_num)

			for p in cal_p:
				dict_e['ADC'].append(chk_adc)
				dict_e['ATTEN'].append(i)
				dict_e['V_CAL(mV)'].append(p)
				_e = df_use[self.col_n(p)] - self.adc(p)
				dict_e['MIN'].append(_e.min())
				dict_e['MEDIAN'].append(_e.median())
				dict_e['MAX'].append(_e.max())
				dict_e['MAX-MIN'].append(_e.max() - _e.min())

		col_l = ['ADC','ATTEN','V_CAL(mV)','MIN','MEDIAN','MAX','MAX-MIN']
		return pd.DataFrame(dict_e).reindex(columns=col_l)

	def _para_2point_cal(self, chip_num=0, cal_method=1, cal_point=[150,850], chk_adc=2, cal_temp=25, atten_use=0):
		'''parameter generation function for two point calibration

		:param chip_num:   number of the chip to be calibrated
		:param cal_point:  two input voltages used for calibration, unit in mV
		:param chk_adc:    choose between SAR-ADC1 or SAR-ADC2
		:param cal_temp:   temperature used to calculate calibration parameters
		:param cal_method: use same group of calibration points for each attenuation mode or not
		:param atten_use:  attenuation mode to be calibrated
		'''
		_at = self.aten_l[atten_use]
		df_use = self._data_pick(chip_num=chip_num, adc=chk_adc, temp=cal_temp, atten=atten_use)
		p1, p2 = cal_point if cal_method==1 else self.cal_point_l[atten_use]

		dict_e = defaultdict(list)
		#prepare calibration
		d_p1 = df_use[self.col_n(p1)].values[0]
		d_p2 = df_use[self.col_n(p2)].values[0]
		a_cal = float(d_p2 - d_p1)/(p2-p1)
		b_cal = d_p1 - a_cal*(p1)
		_a = 4095.0/1100/a_cal
		_b = 4095.0/1100*b_cal/a_cal
		for i in self.group_l+['MAC']:
			dict_e[i].append(df_use[i].values[0])
		dict_e['a'] = _a*_at
		dict_e['b'] = _b*_at
		# return pd.DataFrame(dict_e,index=[0])
		return dict_e['a'], dict_e['b']

	def list_para_2point_cal(self,cal_method=1, cal_point=[150,850], chk_adc=2, cal_temp=25, atten_use=0):
		'''
		'''
		dict_e = defaultdict(list)
		for n,m in self.df[['CHIP#','MAC']].drop_duplicates().values:
			dict_e['CHIP#'].append(n)
			a, b = self._para_2point_cal(n, cal_method, cal_point, chk_adc, cal_temp, atten_use)
			dict_e['MAC'].append(m)
			dict_e['a'].append(a)
			dict_e['b'].append(b)
		return pd.DataFrame(dict_e)

	def data_prepare_2point_cal(self, chip_num, chk_adc, atten_use, cal_point=[150,850], chk_temp=25, cal_temp=25, cal_method=1):
		'''currently only suitable for esp32
		'''
		_at = self.aten_l[atten_use]
		#adc input voltage range
		x   = self.inpt_range
		#ideal adc output
		y_i = [self.adc(i*_at) for i in x]
		#pick data based on selected temperature value
		y = self._data_pick(chip_num=chip_num, adc=chk_adc, temp=chk_temp, atten=atten_use).reindex(columns=self.head_list).values[0]
		#calibration parameter generation
		_a, _b = self._para_2point_cal(chip_num, cal_method, cal_point, chk_adc, cal_temp, atten_use)
		#post calibration error list
		pst_cal_l = y*_a- _b
		#post calibration error, unit in mV
		pst_cal_e    = [self.adc_r(k)/_at/x[i]*100 for i,k in enumerate(pst_cal_l-y_i)]
		pst_cal_e_2  = [(self.adc_r(k)/_at+2)/x[i]*100 for i,k in enumerate(pst_cal_l-y_i)]
		pst_cal_e_m2 = [(self.adc_r(k)/_at-2)/x[i]*100 for i,k in enumerate(pst_cal_l-y_i)]
		return y, y_i, pst_cal_e, pst_cal_e_2, pst_cal_e_m2

	def plot_adc_error(self, adc_use=2, chk_temp=25, method='2point_cal', cal_point=[150,850], 
					   xlim_top=2500, omit_list=[13,27], atten_use=0, cal_temp=25, cal_method=1):
		'''

		:param cal_point: calibration points
		:param omit_list: bypass chip#
		'''
		ymajorLocator  = MultipleLocator(1)
		xmajorLocator  = MultipleLocator(50)
		# yminLocator    = MultipleLocator(0.2)
		ymajorFormator = FormatStrFormatter('%1.1f')

		def _setup_plot(ax):
			ax.yaxis.set_major_formatter(ymajorFormator)
			ax.yaxis.set_major_locator(ymajorLocator)
			ax.xaxis.set_major_locator(xmajorLocator)
			ax.axhline(1,  color='r',linestyle='solid')
			ax.axhline(-1, color='r',linestyle='solid')
			ax.axhline(0.5,  color='r',linestyle='dashed')
			ax.axhline(-0.5, color='r',linestyle='dashed')
			ax.set_ylabel('Error (%)')
			ax.set_ylim(-2,2)
		
		x   = self.inpt_range
		cal_func = getattr(self, 'data_prepare_'+method)
		cal_para = {'cal_point':cal_point, 'chk_temp':chk_temp, 'cal_temp':cal_temp, 'cal_method':cal_method}
		dfg = self.df.groupby(by=['CHIP#','ATTEN','ADC'])

		func_get_key = lambda x: self.df[x].drop_duplicates().values

		#figure #1 four attenuation mode in one plot
		fg2,fx2 = plt.subplots(4,1, sharex=True)
		for at_u in func_get_key('ATTEN'):
			for cp_u in func_get_key('CHIP#'):
				if cp_u in omit_list: continue
				pick_para = {'chip_num':cp_u, 'atten_use':at_u, 'chk_adc':adc_use}
				y, y_i, pce, pce2, pcem2= cal_func(**dict(cal_para, **pick_para))
						
				fx2[at_u].scatter(x, pce, label='PST_CAL_ERROR')

			_setup_plot(fx2[at_u])
			fx2[at_u].set_title('ADC%d POST CAL ERROR ATTEN%d'%(adc_use,at_u))

		fx2[3].set_xlabel('Input Voltage (mV)')
		fx2[3].set_xlim(0,xlim_top)
		fx2[3].set_xticks(range(0,2550,50))

		#figure #2 compare attenuation mode 0 & 1
		ymajorLocator  = MultipleLocator(0.2)
		# fg3,fx3 = plt.subplots(2,2)
		fg3,fx3 = plt.subplots(2,1)
		# for at_u in func_get_key('ATTEN'):
		for at_u in [0,1]:
			for cp_u in func_get_key('CHIP#'):
				if cp_u in omit_list: continue
				# df = dfg.get_group((cp_u, at_u, 1))
				# y, y_i, pce, pce2, pcem2= cal_func(df, at_u, cal_point, chk_temp)
				# fx3[at_u][0].scatter(x, pst_cal_e, label='PST_CAL_ERROR')
				# df = dfg.get_group((cp_u, at_u, 2))
				# y, y_i, pce, pce2, pcem2= cal_func(df, at_u, cal_point, chk_temp)
				# fx3[at_u][1].scatter(x, pst_cal_e, label='PST_CAL_ERROR')
				pick_para = {'chip_num':cp_u, 'atten_use':at_u, 'chk_adc':adc_use}
				y, y_i, pce, pce2, pcem2 = cal_func(**dict(cal_para, **pick_para))
				fx3[at_u].scatter(x, pce, label='PST_CAL_ERROR')
				
			# fx3[at_u][0].set_title('ADC1 POST CAL ERROR ATTEN%d'%(at_u))
			# fx3[at_u][1].set_title('ADC2 POST CAL ERROR ATTEN%d'%(at_u))
			chip_total = len(func_get_key('CHIP#'))
			fx3[at_u].set_title('ADC2 POST CAL ERROR\ntemp=%d atten=%d stepsize=%dmV\n'%(chk_temp, at_u, self.step_size) +
				'%d pcs, cal points %dmV&%dmV '%(chip_total, cal_point[0], cal_point[1]))

			_setup_plot(fx3[at_u])
			fx3[at_u].set_title('ADC%d POST CAL ERROR ATTEN%d'%(adc_use,at_u))
			fx3[at_u].set_xlim(0,1250)
			fx3[at_u].set_xlabel('Input Voltage (mV)')

		#figure #3 compare post cal error w/ estimated measurement
		ymajorLocator  = MultipleLocator(0.5)
		fg1,fx1 = plt.subplots(3,1)
		for cp_u in func_get_key('CHIP#'):
			if cp_u in omit_list: continue
			pick_para = {'chip_num':cp_u, 'atten_use':atten_use, 'chk_adc':adc_use}
			y, y_i, pce, pce2, pcem2 = cal_func(**dict(cal_para, **pick_para))
			fx1[0].scatter(x, pce,   label='PST_CAL_ERROR')
			fx1[1].scatter(x, pce2,  label='PST_CAL_ERROR')
			fx1[2].scatter(x, pcem2, label='PST_CAL_ERROR')

		chip_total = len(func_get_key('CHIP#'))
		fx1[0].set_title('ADC%s POST CAL ERROR\ntemp=%d atten=%d stepsize=%dmV\n'%(adc_use, chk_temp, atten_use, self.step_size) +
				'%d pcs, cal points %dmV&%dmV'%(chip_total, cal_point[0], cal_point[1]))
		fx1[1].set_title('ADC%s POST CAL ERROR w/ +2mV measurement error'%adc_use)
		fx1[2].set_title('ADC%s POST CAL ERROR w/ -2mV measurement error'%adc_use)

		for i in range(3):
			_setup_plot(fx1[i])
			fx1[i].set_xlim(0,self.xlim_l[atten_use])
			fx1[i].set_xlabel('Input Voltage (mV)')

		#figure #4
		temp_l = func_get_key('TEMP') #total number of temperature points in data file
		fg4,fx4 = plt.subplots(len(temp_l),1, sharex=True)
		for cp_u in func_get_key('CHIP#'):
			if cp_u in omit_list: continue
			for i, t_u in enumerate(temp_l):
				pick_para = {'chip_num':cp_u, 'atten_use':atten_use, 'chk_adc':adc_use}
				cal_para = {'cal_point':cal_point, 'chk_temp':t_u, 'cal_temp':cal_temp, 'cal_method':cal_method}
				y, y_i, pce, pce2, pcem2 = cal_func(**dict(cal_para, **pick_para))
				fx4[i].scatter(x, pce, marker='x', label='PST_CAL_ERROR')
				fx4[i].set_title('TEMP:%dC ATTEN:%d\n'%(t_u, atten_use), fontsize=12)

		chip_total = len(func_get_key('CHIP#'))

		if cal_method == 1:
			fg4.suptitle('ADC%s POST CAL ERROR\n%dpcs, cal points %dmV&%dmV, StepSize:%dmV'%(adc_use, chip_total, cal_point[0], cal_point[1], self.step_size),fontsize=18)
		else:
			fg4.suptitle('ADC%s POST CAL ERROR\n%dpcs, StepSize:%dmV'%(adc_use, chip_total, self.step_size),fontsize=18)			

		for i in range(len(temp_l)):
			_setup_plot(fx4[i])
			fx4[i].set_xlim(0,self.xlim_l[atten_use])
			fx4[i].set_xticks(range(0,self.xlim_l[atten_use]+1,50))

		fx4[len(temp_l)-1].set_xlabel('Input Voltage (mV)')

		#figure #5 
		temp_l = func_get_key('TEMP') #total number of temperature points in data file
		fg5,fx5 = plt.subplots(len(temp_l),3, sharex='col')
		xlim_l_2 = [(250,1250),(1250,1800),(1800,2250)] 
		for atten_use in [1,2,3]:
			for cp_u in func_get_key('CHIP#'):
				if cp_u in omit_list: continue
				for i, t_u in enumerate(temp_l):
					pick_para = {'chip_num':cp_u, 'atten_use':atten_use, 'chk_adc':adc_use}
					cal_para = {'cal_point':cal_point, 'chk_temp':t_u, 'cal_temp':cal_temp, 'cal_method':cal_method}
					y, y_i, pce, pce2, pcem2 = cal_func(**dict(cal_para, **pick_para))
					fx5[i][atten_use-1].scatter(x, pce, marker='x', label='PST_CAL_ERROR')
					fx5[i][atten_use-1].set_title('TEMP:%dC, ATTEN:%d\n'%(t_u, atten_use), fontsize=12)

			chip_total = len(func_get_key('CHIP#'))

			if cal_method == 1:
				fg5.suptitle('ADC%s POST-CAL ERROR\n%dpcs, cal points %dmV&%dmV, StepSize:%dmV'%(adc_use, chip_total, cal_point[0], cal_point[1], self.step_size),fontsize=18)
			else:
				fg5.suptitle('ADC%s POST-CAL ERROR\n%dpcs, StepSize:%dmV'%(adc_use, chip_total, self.step_size),fontsize=18)

			xb, xt = xlim_l_2[atten_use-1]
			xaxis_l = [100, 50, 50]
			fx5[len(temp_l)-1][atten_use-1].set_xlim(xb, xt)
			fx5[len(temp_l)-1][atten_use-1].set_xlim(xb, xt)
			fx5[len(temp_l)-1][atten_use-1].set_xlabel('Input Voltage (mV)')
			
			for i in range(len(temp_l)):
				_setup_plot(fx5[i][atten_use-1])
				xmajorLocator  = MultipleLocator(xaxis_l[atten_use-1])
				fx5[i][atten_use-1].xaxis.set_major_locator(xmajorLocator)

