from collections import defaultdict
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
from scipy.interpolate import InterpolatedUnivariateSpline as intp
plt.ion()


class tempSensorCalibration(object):
	'''go to where data file is saved and use below scripts to generate plots for
	temperature sensor calibration results

	NOTE!!! remember to modify temperature sensor read value column name before use
	'''

	def __init__(self, data_file_path, save_path, chip_ver):
		self.df_raw = pd.read_csv(data_file_path)
		self.cv = chip_ver

		self.sp = save_path if save_path.endswith('/') else save_path+'/'

		# self.df_g = self.df_raw.groupby(['BOARD', 'LOC#', 'SUPPLY'])
		self.df_g = self.df_raw.groupby(['BOARD', 'CHIP#', 'SUPPLY'])

		#define a dictionary to record total number of parts of each board
		self.c_d = defaultdict(list)
		board_l = np.sort(self.df_raw['BOARD'].drop_duplicates().tolist())
		for _ in board_l:
			# _c_l = self.df_raw[self.df_raw['BOARD']==_]['LOC#'].drop_duplicates().tolist()
			_c_l = self.df_raw[self.df_raw['BOARD']==_]['CHIP#'].drop_duplicates().tolist()
			_c_l.sort()
			self.c_d[_] = _c_l

		self.colors_use = cm.rainbow(np.linspace(0, 1, 32))

	def plt_chk_vref_temp_relation(self, supl=3.3, mb_num='MB_1', c_i=1, t_pick=20, tsen_col_name='T_CHOP_2'):
		'''plots temperature sensor error & 1V Vref error based on assigned temperature point

		:param supl:   specify SUPPLY voltage to plot
		:param mb_num: specify multi-board number
		:param c_i:    specify chip number
		:param t_pick: pick a temperature point as error calculation base
		:param tsen_col_name: column name for temperature sensor value

		:return: dataframe which lists t-sensor & vref error v.s. temperature
		'''
		df        = self.df_g.get_group((mb_num, c_i, supl)) #choose data based on 
		compare_t = defaultdict(list)

		# vref_pick = df['Vref_1V'][df['Temp']==t_pick].values[0]
		# tsen_pick = df["1_'T_chop:2'"][df['Temp']==t_pick].values[0]
		vref_pick = df['VREF_1V_1'][df['TEMP']==t_pick].values[0]
		tsen_pick = df['T_CHOP_2'][df['TEMP']==t_pick].values[0]
		ts_p_eror = tsen_pick - t_pick

		x = df['TEMP']
		compare_t['TEMP']=x
		compare_t['VREF']=df['VREF_1V_1']
		compare_t['TSEN_E']=x -df[tsen_col_name]
		compare_t['VREF_E']=df['VREF_1V_1'] - vref_pick

		fg1,fx1=plt.subplots(2,1)
		fx1[0].plot(x,df['VREF_1V_1'],ls='',marker='o',label='1V Vref')
		fx1[1].plot(x,-df[tsen_col_name]+x,ls='',marker='o',label='TSEN_error')
		for f_i in range(2):
		    fx1[f_i].set_xticks(x)
		    fx1[f_i].set_xlim(-45,130)
		    fx1[f_i].legend(loc=0)
		fx1[0].set_title('CHIP722 TSEN error vs Vref_1V MB#%s LOC#%s'%(mb_num,c_i))

		return pd.DataFrame(compare_t)

	def plt_chk_vref_temp_relation_multiChip(self, supl=3.3,bad_data_l=[11],tsen_col_name= 'T_CHOP_2'):
		'''plot t-sensor value error & 1V vref data using all chips available
		
		:param bad_data_l: pass chip# if its data point is corrupted
		'''
		cal_t = defaultdict(list)
		fg1, fx1 = plt.subplots(2, 1)
		for mb_num in self.c_d.keys():
		    for i in self.c_d[mb_num]:
		        if i in bad_data_l: continue  # number 11 reference voltage is wrongly measured
		        df = self.df_g.get_group((mb_num, i, supl))

		        x = df['TEMP']
		        y = df[tsen_col_name]

		        fx1[0].scatter(x, x - y, color=self.colors_use[i],
		                       label='%s_C#%s' % (mb_num, i))
		        fx1[1].scatter(x, df['VREF_1V_1'], color=self.colors_use[i],
		                       label='%s_C#%s' % (mb_num, i))
		for i in range(2):
			fx1[i].set_xticks(x)
			fx1[i].legend(loc=0)
			fx1[i].set_xlabel('Oven Temperature (C)')
		fx1[0].set_ylabel('T-Sensor Error(C)')
		fx1[1].set_ylabel('1V VREF (V)')
		fx1[0].set_title('CHIP722 Temp Sensor Error vs Vref_1V all data')

	def plt_chk_vref_temp_relation_avg(self,supl=3.3,tsen_col_name='T_CHOP_2'):
		'''plot t-sensor value error & 1V vref data using all chip data averaged'''
		df_g_2 = self.df_raw.groupby(['TEMP', 'SUPPLY'])
		t_l    = self.df_raw['TEMP'].drop_duplicates()   #list of oven temperature points that being measured
		
		mean_t = defaultdict(list)
		mean_t['TEMP'] = list(t_l)
		
		for t in t_l:
		    mean_t['TSEN_E'].append(t- df_g_2.get_group((t, supl))[tsen_col_name].mean())
		    mean_t['VREF'].append(df_g_2.get_group((t, supl))['VREF_1V_1'].mean())
		df_mean = pd.DataFrame(mean_t)
		df_mean.sort_values(by='TEMP', inplace=True)

		fg1, fx1 = plt.subplots(2, 1)
		
		x = df_mean['TEMP']
		fx1[0].plot(x, df_mean.TSEN_E,label='t-sensor')   
		a_1, b_1, c_1 = np.polyfit(x, df_mean.TSEN_E, 2)
		fx1[0].plot(x, a_1 * x * x + b_1 * x + c_1, ls='--', label='polyfit')
		fx1[1].plot(x, df_mean.VREF, label='1v vref')
		for i in range(2):
			fx1[i].set_xticks(x)
			fx1[i].legend(loc=0)
			fx1[i].set_xlabel('Oven Temperature (C)')
		fx1[0].set_ylabel('T-Sensor Error(C)')
		fx1[1].set_ylabel('1V VREF (V)')
		fx1[0].set_title('CHIP722 Temp Sensor Error vs Vref_1V averaged')

	def error_lookup_table(self,supl=3.3,tsen_col_name= 'T_CHOP_2'):
		'''based on previous observation (tsensor error vs temp), there is a slope error needs to be compensated.
		we can generate a lookup table to record calibration values for each temperature point. 
		'''
		df_g_2 = self.df_raw.groupby(['TEMP', 'SUPPLY'])
		t_l    = self.df_raw['TEMP'].drop_duplicates()   #list of oven temperature points that being measured
		
		mean_t = defaultdict(list)
		mean_t['TEMP'] = list(t_l)
		
		for t in t_l:
			#equation: t-sen_error = t_env - t-sen_return_val
		    mean_t['TSEN_E'].append(t- df_g_2.get_group((t, supl))[tsen_col_name].mean())
		    mean_t['VREF'].append(df_g_2.get_group((t, supl))["VREF_1V_1"].mean())
		df_mean = pd.DataFrame(mean_t)
		df_mean.sort_values(by='TEMP', inplace=True)

		dc = intp(df_mean.TEMP, df_mean.TSEN_E)

		elt = defaultdict(list)
		_t = elt['TEMP'] = np.arange(-80, 185, 0.5)
		elt['Error'] = dc(_t)                               #t-sen return value error compared to env temp
		elt['TSEN_E'] = (_t - dc(_t)+0.5).astype(dtype=int) #temp sensor return value
		self.err_lokup_tbl = pd.DataFrame(elt)

	def est_efuse_bit(self,ratio=2):
		'''use this function to predict how many bits of efuse needs to be preserved
		'''
		self.error_lookup_table()
		e_l_t = self.err_lokup_tbl
		a     = e_l_t['Error'].apply(lambda x:float('%.1f'%x))
		efuse_bits = (a.max()-a.min())/0.1
		print 'Need to have EFUSE bits: %d'%int(np.log2(efuse_bits)+0.5)

	def plt_pst_cal(self, plt_type='boxenplot', tsen_col_name='T_CHOP_2',cal_temp=20, 
		cal_comp=0, d_r=False, plt_style=None, plt_platte=None):
		'''plot original data error, compared to post-calibration error
		
		:param plt_type:	  'boxplot', 'violinplot', 'boxenplot'
		:param tsen_col_name: temp sensor data column name
		:param cal_temp:      use specified temperature point to calculate offset 
		:param cal_comp:      used to make up for error caused by over-compensation
		:param d_r:           limit error list data decimal point to %.1f
		:param plt_style:     'whitegrid', 'darkgrid', 'white', 'dark', 'ticks'
		:param plt_platte:    'pastel', 'muted', 'bright', 'deep', 'colorblind', 'dark'
		'''
		self.error_lookup_table()
		e_l_t = self.err_lokup_tbl

		df = self.df_raw
		x = df['TEMP']
		y = df[tsen_col_name]


		bb = df[(df['TEMP']==20) & (df['SUPPLY']==3.3)][tsen_col_name] - cal_temp 
		bb += cal_comp
		bb_c = df[(df['TEMP']==20) & (df['SUPPLY']==3.3)]['CHIP#']
		bb_dict = dict(zip(bb_c.tolist(), bb.tolist()))

		bb_l = []
		for i in df['CHIP#']:
			if i in bb_c.values:
				bb_l.append(bb_dict[i])
			else:
				bb_l.append(0)
		bb_l = np.array(bb_l)
		# bb_l = np.array([bb_dict[i] for i in df['CHIP#'] if i in bb_c else 0])
		# bb = bb.values[0]

		fg1, fx1 = plt.subplots(3, 1)
		sns.set_style(plt_style)
		# sns.boxplot(x, x-y,    ax=fx1[0])
		# sns.boxplot(x, x+bb_l-y, ax=fx1[1])
		getattr(sns,plt_type)(x, x-y,    ax=fx1[0], palette=plt_platte)
		getattr(sns,plt_type)(x, x+bb_l-y, ax=fx1[1], palette=plt_platte)

		# find the right error value use error lookup table
		eror_l = [e_l_t[e_l_t['TSEN_E'] == int(tt + 0.5)]['Error'].values[0] for tt in y]
		e_l = np.array(map(lambda x: float('%.1f'%(x+0.05)),eror_l)) if d_r else np.array(eror_l)

		# sns.boxplot(x, x- (y+ e_l -bb_l), ax=fx1[2])
		getattr(sns,plt_type)(x, x- (y+ e_l -bb_l), ax=fx1[2], palette=plt_platte)

		for i in range(3):
			# fx1[i].set_xlim(-45, 130)
			fx1[i].set_ylim(-25, 25)
			fx1[i].set_ylabel('Erorr(C)')
			fx1[i].set_yticks(np.linspace(-25,25,11))
			fx1[i].axhline(5,  color='r',linestyle='dotted')
			fx1[i].axhline(-5, color='r',linestyle='dotted')

		fx1[0].set_title('original data error')
		fx1[1].set_title('calibrate error w/ offset only')
		fx1[2].set_title('calibrate error w/ offset & temp curve')


	def plt_pst_cal_scatter(self,supl=3.3,error_l=[],tsen_col_name='T_CHOP_2',cal_temp=20, 
		cal_comp=0,poly_fit=False,d_r=False):
		'''plot original data error, compared to post-calibration error
		
		:param error_l:       chip # whose data point wrongly measured
		:param tsen_col_name: temp sensor data column name
		:param cal_temp:      use specified temperature point to calculate offset 
		:param cal_comp:      used to make up for error caused by over-compensation
		:param poly_fit:      linear fit entire data points to find offset
		:param d_r:           limit error list data decimal point to %.1f
		'''
		self.error_lookup_table()
		e_l_t = self.err_lokup_tbl

		fg1, fx1 = plt.subplots(4, 1)
		for mb_num in self.c_d.keys():
		    for i, v in enumerate(self.c_d[mb_num]):
			    # number 11 reference voltage is wrongly measured
				if v in error_l: continue  
				df = self.df_g.get_group((mb_num, v, supl))
				x = df['TEMP']
				y = df[tsen_col_name]

				if poly_fit:
					aa, bb = np.polyfit(x, y, 1)
				else:
					#equation: offset = t-sen_val - t_env
					bb = y[x == cal_temp] - cal_temp 
					bb += cal_comp
					bb = bb.values[0]

				lbl_str = '%s_C#%s' % (mb_num, v) #curve label
				c_u = self.colors_use[i]		     #curve color

				fx1[0].scatter(x, x- y, color=c_u, label=lbl_str)
				fx1[1].scatter(x, df['VREF_1V_1'], color=c_u, label=lbl_str)
				fx1[2].scatter(x, x+bb-y, color=c_u, label=lbl_str)
				# find the right error value use error lookup table
				eror_l = [e_l_t[e_l_t['TSEN_E'] == int(tt + 0.5)]['Error'].values[0] for tt in y]
				e_l = np.array(map(lambda x: float('%.1f'%(x+0.05)),eror_l)) if d_r else np.array(eror_l)

				fx1[3].scatter(x, x- (y + e_l - bb), color=c_u, label=lbl_str)

		fx1[2].set_ylim(-30, 30)
		fx1[2].set_yticks(np.linspace(-30,30,13))
		fx1[3].set_ylim(-30, 30)
		fx1[3].set_yticks(np.linspace(-30,30,13))
		for i_f in range(4): fx1[i_f].set_xticks(x)
		fx1[0].set_title('original data error')
		fx1[1].set_title('1V VREF data')
		fx1[2].set_title('calibrate error w/ offset only')
		fx1[3].set_title('calibrate error w/ offset & temp curve')