from baselib.loglib.log_lib import *
from baselib.loglib.log_csv import csvreport
from collections import OrderedDict
import re as re
import os as os
import time
import scipy.optimize as opt
import matplotlib.pyplot as plt
import pandas  as pd
import numpy   as np
import seaborn as sns

from dataprocess.volume._data_address import *

class socketVisualizer(object):
	'''class to plot measurement data sets
	
	'''
	def __init__(self, data_file_path, save_path, chip_ver):
		self.df = pd.read_csv(data_file_path)
		self.cv = chip_ver

		self.sp = save_path if save_path.endswith('/') else save_path+'/'
		if not os.path.exists(self.sp):os.makedirs(self.sp)

	def plt_kde(self,data_type='O_CODE', group_type='CORNER', ratio_unit=1,
		rug_op =False, v_alpha=0.5, bin_num=50, save_figure=False):
		'''plot density & histogram plot to check corner/suppply influence on data set

		:param data_type:  column name of data to be plotted
		:param group_type: column name used to group data 
		'''
		df_g = self.df.groupby(group_type)
		g_l  = df_g.groups.keys()

		for k in g_l:
			_df_t = df_g.get_group(k)[data_type]*ratio_unit
			_bin_max = _df_t.max()
			_bin_min = _df_t.min() if _df_t.min() >=0 else 0

			sns.distplot(_df_t, label='%r'%k, 
				rug=rug_op, kde=True, hist= True, hist_kws={'alpha':v_alpha},
				bins=np.linspace(_bin_min, _bin_max, bin_num))

		plt.legend(loc=0)
		t_str_l = [self.cv, data_type, 'by_'+group_type]
		plt.title(' -- '.join(t_str_l))

		if save_figure:
			plt.savefig(self.sp + '_'.join(t_str_l) + '.png')
			plt.close('all')

	def batch_plt(self, plt_type='kde', data_type_list=None, group_type_list=['CORNER','SUPPLY']):
		'''plot all data based on choices
		'''
		bin_num = 20

		if data_type_list == None:
			data_type_list = ['I_EN0(uA)', 'I_EN10(uA)', 'VDD33(ADC)', '32K_STARTUP(us)',
						      'FREQ_8M', 'FREQ_150K', 
						      'RTC_LDO', 'DIG_LDO','SAR1_REF', 'SAR2_REF', 'VCM', 'VREF_1V',
						      'O_CODE', 'O_CODE_0', 'O_CODE_1', 'O_CODE_2', 'O_CODE_3',
						      'PVT_DIG_DBIAS_4', 'T_OS_0', 'T_CHOP_2', 
						      'I_LSLP_WFPD0(mA)','I_LSLP_WFPD1(mA)', 'I_LSLP_WF_D(mA)',
						      'V_LSLP_7_0(V)', 'V_LSLP_6_0(V)', 'V_LSLP_3_0(V)', 'V_LSLP_0_1(V)','V_LSLP_0_5(V)',
						      'I_LSLP_7_0(mA)','I_LSLP_6_0(mA)', 'I_LSLP_3_0(mA)', 'I_LSLP_0_1(mA)', 'I_LSLP_0_5(mA)',
						      'I_DSLP(uA)']
			data_type_list = list(set(data_type_list) & set(self.df.columns))

		for _gt  in group_type_list:
			for _dt in data_type_list:
				getattr(self,'plt_'+plt_type)(data_type=_dt, group_type=_gt, save_figure=True, bin_num=bin_num)
				# self.plt_kde(data_type=_dt, group_type=_gt, save_figure=save_figure, bin_num=bin_num)

	def _plt_ot_vref_ocode(self, c_l, figure_name='MARLIN3 SKEW LOT 62pcs (TT, FF, SS)'):
		'''cross temperature plot for vref_1v & o_code

		:param c_l:         list of parts to be plotted
		'''
		df_2 = self.df[self.df['LOC#'].isin(c_l)]

		x = df_2['TEMP']
		vref_l = [i for i in df_2.columns.tolist() if i.find('VREF')!=-1]
		ocod_l = [i for i in df_2.columns.tolist() if i.find('O_CODE')!=-1]
		
		fg1, fx1 = plt.subplots(2,1)
		
		for i in vref_l:
			y = df_2[i]
			fx1[0].scatter(x,y)
		for i in ocod_l:
			y = df_2[i]
			fx1[1].scatter(x,y)
		
		for _ in range(2):
			fx1[_].set_xticks(x.drop_duplicates().tolist())
			fx1[_].set_xlabel('OVEN_TEMP (C)')

		fx1[0].set_ylabel('VREF_1V (V)')
		fx1[1].set_ylabel('O_CODE')
		fx1[0].set_title(figure_name+' VREF_1V & O_CODE')

	def _plt_ot_vref_ocode_by_corner(self):
		'''cross temperature plot for vref1v & o_code for corner lot

		'''
		dfg = self.df.groupby('CORNER')

		fg1,fx1 = plt.subplots(2,3)
		c_d = {0:'blue',1:'green',2:'red'}

		for n,c in enumerate(['ss','tt','ff']):
			_df = dfg.get_group(c)
			x = _df['TEMP']
			vref_l = [i for i in _df.columns.tolist() if i.find('VREF')!=-1]
			ocod_l = [i for i in _df.columns.tolist() if i.find('O_CODE')!=-1]
			for i in vref_l:
				y = _df[i]
				fx1[0][n].scatter(x,y,color = c_d[n])

			for i in ocod_l:
				y = _df[i]
				fx1[1][n].scatter(x,y,color = c_d[n])

			for _ in range(2):
				fx1[_][n].set_xticks(x.drop_duplicates().tolist())
				fx1[_][n].set_xlim(-45,130)
				fx1[_][n].set_xlabel('OVEN_TEMP (C)')

			fx1[0][n].set_title('%s CORNER PARTs'%c)
			fx1[0][n].set_ylabel('VREF_1V (V)')
			fx1[1][n].set_ylabel('O_CODE')

	def _plt_ot_tsen_violin_box(self):
		'''plot temperature sensor data distribution
		
		'''
		y=self.df['T_CHOP_2']
		x=self.df['TEMP']
		fg1,fx1= plt.subplots(2,1)
		sns.boxplot(x,x-y,ax=fx1[0])
		sns.violinplot(x,x-y,ax=fx1[1])
		return

#to be polished a lot below, not ready to be used 
	'''use socket value to plot'''
	def plot_light_sleep_current(self,sort_column='Vref_1V',savefig=True,legend_loc=0):
		'''sort data value by selected column and plot light sleep current & voltage using that sequence
		'''
		cur_dir = os.path.realpath('')
		pic_path = cur_dir + '/light_sleep_plot'
		if not os.path.exists(pic_path):os.makedirs(pic_path)

		fg1,fx1 = plt.subplots(2,1)
		data_local = self.data_dict_sckt['data_sckt']
		data_local.sort_values(by=sort_column,inplace=True)
		I_list= ['I_lsp_70','I_lsp_30','I_lsp_01','I_lsp_05']
		V_list= ['V_lsp_70','V_lsp_30','V_lsp_01','V_lsp_05']
		marker_list = ['d','v','x','o']
		x = np.arange(len(data_local['%s'%sort_column]))
		for i,v in enumerate(V_list):
			i_col = I_list[i]
			m_use = marker_list[i]
			fx1[0].plot(x,data_local['%s'%i_col],label='%s'%i_col,marker=m_use)
			fx1[1].plot(x,data_local['%s'%v],label='%s'%v,marker=m_use)

		fx1[0].set_ylabel('Current (mA)')
		fx1[1].set_ylabel('Voltage (V)')
		fx1[0].set_title('chip722 light sleep Current socket test sort by %s'%(sort_column))
		fx1[1].set_title('chip722 light sleep Voltage socket test sort by %s'%(sort_column))
		# for plt_i in [1,2]:
		# 	fx1[plt_i].set_ylim(1.00,1.12)
		for plt_i in [0,1]:fx1[plt_i].legend(loc=legend_loc)
			# fx1[plt_i].set_xlim((x.min()-5),x.max()+5)
			# fx1[plt_i].set_xticks(np.arange(x.min(),x.max()+5,20))
			# fx1[plt_i].set_xlabel('Oven Temp (C)')fx1[plt_i].legend(loc=legend_loc)
		# fg1.set_size_inches(fig_size[0],fig_size[1])
		if savefig is True: 
			fg1.savefig(pic_path+'/chip722_light_sleep_socket_test_sort_by_%s'%(sort_column),dpi=300)
			plt.close()
		return 

	'''use temp scan data to plot'''
	def plot_temp_sensor(self,boardNum=1,chip_num=[0],avg=True,legend_loc=0,
						lin_fit=True,fig_size=[15,10],savefig=True,refline=True):
		'''plot temperature sensor data versus temperature to check linearity
			- legend_loc: 
				- 0:'best'
				- 2:'upper left'
		'''
		data_local = self.df
		cur_dir = os.path.realpath('')
		pic_path = cur_dir + '/temp_sensor_plot'
		if not os.path.exists(pic_path):os.makedirs(pic_path)
		supply_l = ['2.7V','3.3V','3.6V']

		fg1,fx1 = plt.subplots(1,1)
		x = data_local[data_local['CHIP#'] == 0]['Temp']
		a = []
		b = []
		for i in chip_num:
			marker_use = self.marker_l[i%10-1]
			color_use  = self.color_l[i%6-1]
			data_local_chip = data_local[data_local['CHIP#'] == i]
			y_avg = data_local_chip['T_chop2_1']
			for check_time in [2,3]:
				'''temperatuer sensor reads 3x, use average value to do linear fit'''
				y_avg += data_local_chip['T_chop2_%s'%check_time]
			y_avg = y_avg/3.0
			slope,intercept = np.polyfit(x,y_avg,1)
			if avg:
				fx1.scatter(x,y_avg,label='chip#%d'%i,marker = marker_use,color=color_use)
			else:
				for read_time in [1,2,3]:
					y = data_local[data_local['CHIP#'] == i]['T_chop2_%s'%read_time]
					fx1.scatter(x,y,label='chip#%d_#%d'%(i,read_time),marker = marker_use,color=color_use)
			if lin_fit: 
				x_full = np.arange(x.min(),x.max()+5,5)
				fx1.plot(x_full,slope*x_full+intercept,label='linear_fit#%d'%i)
				fx1.text(-40,100,'chip#%d: slope=%.3f,intcept=%.3f'%(i,slope,intercept),fontsize=12)
			if refline:
				x_full = np.arange(x.min(),x.max()+5,5)
				fx1.plot(x_full,x_full,'--',label='reference_line#%d'%i)
			a.append(slope)
			b.append(intercept)
		fx1.set_ylim((x.min()-10),x.max()+20)
		fx1.set_yticks(np.arange((x.min()-10),x.max()+25,5))
		fx1.set_xlim((x.min()-5),x.max()+5)
		fx1.set_xticks(np.arange(x.min(),x.max()+5,20))
		fx1.set_xlabel('Oven Temp (C)')
		fx1.set_ylabel('Sensor Read (C)')
		fx1.legend(loc=legend_loc)
		fx1.set_title('chip722 temp sensor MB#%s chip#%s Supply=2.7V,3.3V,3.6V'%(boardNum,chip_num))
		fg1.set_size_inches(fig_size[0],fig_size[1])
		if savefig is True: 
			fg1.savefig(pic_path+'/chip722_temp_sensor_MB#%s_chip#%s'%(boardNum,chip_num),dpi=300)
			plt.close()
		# if savefig is True: fg1.savefig(pic_path+'/chip722_temp_sensorchip#%s'%chip_num,bbox_inches='tight',dpi=300)
		return a,b

	'''use temp scan data to plot'''
	def plot_vref1v(self,boardNum=1,chip_num=[0],legend_loc=0,
						lin_fit=False,fig_size=[15,20],savefig=True):
		'''plot 1V Reference & O_code data versus temperature to check linearity
			- legend_loc: 
				- 0:'best'
				- 2:'upper left'
		'''
		cur_dir = os.path.realpath('')
		pic_path = cur_dir + '/vref_1v_plot'
		if not os.path.exists(pic_path):os.makedirs(pic_path)
		supply_l = ['2.7V','3.3V','3.6V']

		fg1,fx1 = plt.subplots(2,1)
		data_local = self.data_dict_temp['data_mb%d'%boardNum]
		x = data_local[data_local['CHIP#'] == 0]['Temp']
		a = []
		b = []
		for i in chip_num:
			data_local_chip = data_local[data_local['CHIP#'] == i]
			y_avg = data_local_chip['Vref_1V']
			slope,intercept = np.polyfit(x,y_avg,1)

			# y = data_local[data_local['CHIP#'] == i]['Vref_1V']
			# fx1.scatter(x,y,label='chip#%d'%i,marker = marker_use,color=color_use)
			for s_i, supply_n in enumerate(supply_l):
				marker_use = self.marker_l[(i+s_i)%10-1]
				color_use  = self.color_l[(i+s_i)%6-1]
				# marker_num = i%10-1+s_i
				# if marker_num >9: marker_num = 0
				# color_num = i%6-1+s_i
				# if color_num >5: color_num = 0
				# marker_use = self.marker_l[marker_num]
				# color_use  = self.color_l[color_num]
				data_loc_chip_sup = data_local_chip[data_local_chip['Supply']==supply_n]
				x = data_loc_chip_sup['Temp']
				y = data_loc_chip_sup['Vref_1V']
				fx1[0].scatter(x,y,label='chip#%d_%s'%(i,supply_n),marker = marker_use,color=color_use)
				y = data_loc_chip_sup['O_code_1']
				fx1[1].scatter(x,y,label='chip#%d_%s'%(i,supply_n),marker = marker_use,color=color_use)
			if lin_fit: 
				x_full = np.arange(x.min(),x.max()+5,5)
				fx1[0].plot(x_full,slope*x_full+intercept,label='linear_fit#%d'%i)
				fx1[0].text(-40,100,'chip#%d: slope=%.3f,intcept=%.3f'%(i,slope,intercept),fontsize=12)
			# if refline:
			# 	x_full = np.arange(x.min(),x.max()+5,5)
			# 	fx1.plot(x_full,x_full,'--',label='reference_line#%d'%i)
			a.append(slope)
			b.append(intercept)
		# fx1.set_ylim((x.min()-10),x.max()+20)
		# fx1.set_yticks(np.arange((x.min()-10),x.max()+25,5))
		fx1[0].set_ylabel('1V VREF (V)')
		fx1[1].set_ylabel('O CODE')
		fx1[0].set_title('chip722 1v VREF MB#%s chip#%s Supply=2.7V,3.3V,3.6V'%(boardNum,chip_num))
		fx1[1].set_title('chip722 O CODE  MB#%s chip#%s Supply=2.7V,3.3V,3.6V'%(boardNum,chip_num))
		fx1[1].set_ylim((y.min()-5),y.max()+5)
		fx1[1].set_yticks(np.arange(y.min()-5,y.max()+6,1))
		for i in [0,1]:
			fx1[i].set_xlim((x.min()-5),x.max()+5)
			fx1[i].set_xticks(np.arange(x.min(),x.max()+5,20))
			fx1[i].set_xlabel('Oven Temp (C)')
			fx1[i].legend(loc=legend_loc)
		fg1.set_size_inches(fig_size[0],fig_size[1])
		if savefig is True: 
			fg1.savefig(pic_path+'/chip722_1v_vref_MB#%s_chip#%s'%(boardNum,chip_num),dpi=300)
			plt.close()
		return a,b

	'''use temp scan data to plot'''
	def plot_ldo(self,boardNum=1,chip_num=[0],legend_loc=0,
						fig_size=[15,20],savefig=True):
		'''plot dig ldo & rtc ldo data versus temperature to check linearity
			- legend_loc: 
				- 0:'best'
				- 2:'upper left'
		'''
		cur_dir = os.path.realpath('')
		pic_path = cur_dir + '/ldo_plot/MB#%s'%boardNum
		if not os.path.exists(pic_path):os.makedirs(pic_path)
		
		data_local = self.data_dict_temp['data_mb%d'%boardNum]
		supply_l = data_local[data_local['CHIP#'] == 0]['Supply']
		supply_l = np.sort(supply_l.drop_duplicates())
		x = data_local[data_local['CHIP#'] == 0]['Temp']
		for i in chip_num:
			fg1,fx1 = plt.subplots(3,1)
			data_local_chip = data_local[data_local['CHIP#'] == i]

			for s_i, supply_n in enumerate(supply_l):
				marker_use = self.marker_l[(i+s_i)%10-1]
				color_use  = self.color_l[(i+s_i)%6-1]
				data_loc_chip_sup = data_local_chip[data_local_chip['Supply']==supply_n]
				x = data_loc_chip_sup['Temp']
				y = data_loc_chip_sup['Vref_1V']
				fx1[0].scatter(x,y,label='chip#%d_%s'%(i,supply_n),marker = marker_use,color=color_use)
				y = data_loc_chip_sup['RTC_ldo']
				fx1[1].scatter(x,y,label='chip#%d_%s'%(i,supply_n),marker = marker_use,color=color_use)
				y = data_loc_chip_sup['DIG_ldo']
				fx1[2].scatter(x,y,label='chip#%d_%s'%(i,supply_n),marker = marker_use,color=color_use)

			fx1[0].set_ylabel('1V VREF (V)')
			fx1[1].set_ylabel('RTC_ldo (V)')
			fx1[2].set_ylabel('DIG_ldo (V)')
			fx1[0].set_title('chip722 1V VREF MB#%s chip#%s Supply=2.7V,3.3V,3.6V'%(boardNum,i))
			fx1[1].set_title('chip722 RTC_ldo MB#%s chip#%s Supply=2.7V,3.3V,3.6V'%(boardNum,i))
			fx1[2].set_title('chip722 DIG_ldo MB#%s chip#%s Supply=2.7V,3.3V,3.6V'%(boardNum,i))
			# fx1[1].set_ylim((y.min()-5),y.max()+5)
			# fx1[1].set_yticks(np.arange(y.min()-5,y.max()+6,1))
			for plt_i in [1,2]:
				fx1[plt_i].set_ylim(1.00,1.12)
			for plt_i in [0,1,2]:
				fx1[plt_i].set_xlim((x.min()-5),x.max()+5)
				fx1[plt_i].set_xticks(np.arange(x.min(),x.max()+5,20))
				fx1[plt_i].set_xlabel('Oven Temp (C)')
				fx1[plt_i].legend(loc=legend_loc)
			fg1.set_size_inches(fig_size[0],fig_size[1])
			if savefig is True: 
				fg1.savefig(pic_path+'/chip722_ldo_MB#%s_chip#%s'%(boardNum,i),dpi=300)
				plt.close()
		return 

	'''use temp scan data to plot'''
	def plot_clk_150k(self,boardNum=1,chip_num=[0],legend_loc=0,
						fig_size=[12,12],savefig=True):
		'''plot 150K clock data versus temperature 
			- legend_loc: 
				- 0:'best'
				- 2:'upper left'
		'''
		cur_dir = os.path.realpath('')
		pic_path = cur_dir + '/clk_150k_plot/MB#%s'%boardNum
		if not os.path.exists(pic_path):os.makedirs(pic_path)
		
		data_local = self.data_dict_temp['data_mb%d'%boardNum]
		supply_l = data_local[data_local['CHIP#'] == 0]['Supply']
		supply_l = np.sort(supply_l.drop_duplicates())
		clk_name_l = ['150k_min','150k_mid','150k_max']
		x = data_local[data_local['CHIP#'] == 0]['Temp']
		for i in chip_num:
			fg1,fx1 = plt.subplots(1,1)
			data_local_chip = data_local[data_local['CHIP#'] == i]

			for s_i, supply_n in enumerate(supply_l):
				marker_use = self.marker_l[(i+s_i)%10-1]
				color_use  = self.color_l[(i+s_i)%6-1]
				data_loc_chip_sup = data_local_chip[data_local_chip['Supply']==supply_n]
				x = data_loc_chip_sup['Temp']
				for plt_i,clk_name in enumerate(clk_name_l):
					y = data_loc_chip_sup['%s'%clk_name]/1e3
					fx1.scatter(x,y,label='%s_%s'%(clk_name[5:],supply_n),marker = marker_use,color=color_use)
				# y = data_loc_chip_sup['150k_mid']
				# fx1[1].scatter(x,y,label='chip#%d_%s'%(i,supply_n),marker = marker_use,color=color_use)
				# y = data_loc_chip_sup['150k_max']
				# fx1[1].scatter(x,y,label='chip#%d_%s'%(i,supply_n),marker = marker_use,color=color_use)

			for plt_i,clk_name in enumerate(clk_name_l):
				fx1.set_ylabel('150K (KHz)')
				fx1.set_title('chip722 %s MB#%s chip#%s Supply=2.7V,3.3V,3.6V'%(clk_name[:-4],boardNum,i))
				# fx1.set_ylim(1.00,1.12)
				fx1.set_xlim((x.min()-5),x.max()+5)
				fx1.set_xticks(np.arange(x.min(),x.max()+5,20))
				fx1.set_xlabel('Oven Temp (C)')
				fx1.legend(loc=legend_loc,fontsize='small')
			fg1.set_size_inches(fig_size[0],fig_size[1])
			if savefig is True: 
				fg1.savefig(pic_path+'/chip722_clk_150k_MB#%s_chip#%s'%(boardNum,i),dpi=300)
				plt.close()
		return 

	'''use temp scan data to plot'''
	def plot_8m_clk(self,boardNum=1,chip_num=[0],legend_loc=2,
						lin_fit=False,fig_size=[20,15],savefig=True):
		'''plot 8m cal value sweep data versus temperature 
			- plt_method:
				- 'supply'
				- 'temp'
			- legend_loc: 
				- 0:'best'
				- 2:'upper left'
		'''
		cur_dir = os.path.realpath('')
		pic_path = cur_dir + '/clk_8m_plot/MB#%s'%boardNum
		if not os.path.exists(pic_path):os.makedirs(pic_path)

		data_local = self.data_dict_temp['data_8m_mb%d'%boardNum]
		# x = data_local[data_local['CHIP#'] == 0]['Temp']
		# x_sort = np.sort(x.drop_duplicates())
		temp_l   = data_local[data_local['CHIP#'] == 0]['TEMP']
		temp_l   = np.sort(temp_l.drop_duplicates())
		supply_l = data_local[data_local['CHIP#'] == 0]['SUPPLY']
		supply_l = np.sort(supply_l.drop_duplicates())
		temp_typ   = 40
		supply_typ = 3.3 
		# a = []
		# b = []
		best_code_dict = OrderedDict()
		best_code_dict['CHIP#']=[]
		best_code_dict['DREQ_best']=[]
		best_code_dict['FREQ_8m_best']=[]
		for i in chip_num:
			fg1,fx1  = plt.subplots(2,1)
			data_local_chip = data_local[data_local['CHIP#'] == i]
			# y_avg = data_local_chip['Vref_1V']
			# slope,intercept = np.polyfit(x,y_avg,1)
			# y = data_local[data_local['CHIP#'] == i]['Vref_1V']
			# fx1.scatter(x,y,label='chip#%d'%i,marker = marker_use,color=color_use)
			x = np.arange(2**8)
			for s_i, supply_n in enumerate(supply_l):
				marker_use = self.marker_l[(i+s_i)%10-1]
				color_use  = self.color_l[(i+s_i)%6-1]
				data_lc_temp = data_local_chip[data_local_chip['TEMP']==temp_typ]
				y = data_lc_temp[data_lc_temp['SUPPLY']==supply_n].T[5:]/1e6
				fx1[0].scatter(x,y,label='%sV'%(supply_n),marker = marker_use,color=color_use)
			for s_i, temp_n in enumerate(temp_l):
				marker_use = self.marker_l[(i+s_i)%10-1]
				color_use  = self.color_l[(i+s_i)%6-1]
				data_lc_supl = data_local_chip[data_local_chip['SUPPLY']==supply_typ]
				y = data_lc_supl[data_lc_supl['TEMP']==temp_n].T[5:]/1e6
				fx1[1].scatter(x,y,label='%sC'%(temp_n),marker = marker_use,color=color_use)
			'''find smallest var dfreq code'''
			code_std     = data_lc_supl['0'].std()
			min_var_code = 0
			for var_i in np.arange(2**8): 
				if data_lc_supl['%d'%var_i].std() < code_std: 
					min_var_code = var_i
					code_std     = data_lc_supl['%d'%var_i].std()
			freq_8m_best = data_lc_supl[data_lc_supl['TEMP']==40]['%d'%min_var_code].values[0]/1e6
			best_code_dict['CHIP#'].append(i)
			best_code_dict['DREQ_best'].append(min_var_code)
			best_code_dict['FREQ_8m_best'].append(freq_8m_best)
			# if refline:
			# 	x_full = np.arange(x.min(),x.max()+5,5)
			# 	fx1.plot(x_full,x_full,'--',label='reference_line#%d'%i)
			# a.append(slope)
			# b.append(intercept)
		# fx1.set_ylim((x.min()-10),x.max()+20)
		# fx1.set_yticks(np.arange((x.min()-10),x.max()+25,5))
			fx1[0].set_title('chip722 8M CLK MB#%s chip#%s Temp=40C'%(boardNum,i))
			fx1[1].set_title('chip722 8M CLK MB#%s chip#%s Supply=3.3V'%(boardNum,i))
			fx1[1].text(30,y.median()+1,'bset_code=%d\nf_8m=%.2f\n'%(min_var_code,freq_8m_best),fontsize=12)
		# fx1[1].set_ylim((y.min()-5),y.max()+5)
		# fx1[1].set_yticks(np.arange(y.min()-5,y.max()+6,1))
			for pic_i in [0,1]:
				fx1[pic_i].set_ylabel('8M CLK (MHz)')
				fx1[pic_i].set_xlim(0,255)
				fx1[pic_i].set_xticks(np.arange(0,2**8,5))
				fx1[pic_i].set_xlabel('dfreq')
				fx1[pic_i].legend(loc=legend_loc)
			fg1.set_size_inches(fig_size[0],fig_size[1])
			if savefig is True: 
				fg1.savefig(pic_path+'/chip722_8m_clk_MB#%s_chip#%s'%(boardNum,i),dpi=300)
				plt.close()
		best_code_dict = pd.DataFrame(best_code_dict)
		best_code_dict.to_csv(pic_path+'/chip722_8m_clk_best_code_MB#%s.csv'%(boardNum))
		return best_code_dict

	def plot_adc(self,data,boardNum=1,sarNum=2,chiptype='chip722',
				chip_l=None,atten_l=None,supl_l=None,inl_cal=False,normalize=True,savefig=False):
		'''
		:brief:
		use adc data and plot INL, DNL, raw input in one plot
		
		:param:
		- inl_cal: calculates inl based on difference between raw data & fitting curve
		'''
		cur_dir = os.path.realpath('')
		pic_path = cur_dir + '/SARADC%s/MB#%s'%(sarNum,boardNum)
		if not os.path.exists(pic_path):os.makedirs(pic_path)

		data_local = data

		#generate a list of chip serial numbers
		if chip_l is None:    
			if data_local.get('CHIP_NUM') is None:
				chip_l = data_local.get('CHIP#').drop_duplicates().tolist()
				c_n_n  = 'CHIP#'  #record column name for CHIP number
			else:
				chip_l = data_local.get('CHIP_NUM').drop_duplicates().tolist()
				c_n_n  = 'CHIP_NUM'  #record column name for CHIP number
		#genrate a list of supply being used to test
		if 'Supply' in data_local.columns:
			s_n = 'Supply'
		else:
			s_n = 'SUPPLY'
		if supl_l is None:    supl_l = data_local.get('%s'%s_n).drop_duplicates().tolist()
		#genrate a list of atten configurations being used to test
		if atten_l is None:
			if 'config' in  data_local.columns:   
				atten_l = data_local['config'].drop_duplicates().values.tolist()
			else:
				atten_l = data_local['ATTEN']
				atten_l = ['%s'%i for i in atten_l]
		else:
			atten_l = ['%s'%i for i in atten_l]
		
		#import input sweep voltage information: range & step size
		v_inpt = [np.int(col[:-2]) for col in data.columns if col[:-2].isdigit() is True]
		if v_inpt == []:
			v_inpt = [np.int(col.split('_')[1][:-4]) for col in data.columns if col[:5]=='INPUT']
		inpt_step = v_inpt[1]-v_inpt[0]

		inpt_lim = [1100,1500,2200,3600]     #valid input voltage range 
		inpt_plt_step = [50,50,100,150]      #x scale step size used for plot
		aten_ratio_l = [1.0,0.75,0.5,0.25]   #attenuation ration if use different attenuation setup

 		fname = '%s_sar%s_adc_input_sweep'%(chiptype,sarNum)
 		plt.figure(fname)
 		fx1 = plt.subplot(221)
 		fx2 = plt.subplot(223)
 		fx3 = plt.subplot(122)

 		slope_l =[]
 		inter_l = []
		for supl in supl_l:
			for aten in atten_l:
				aten_val = np.int(aten[-1])
				aten_ratio = aten_ratio_l[aten_val]

				#detect data file column name 
				if 'config' in  data_local.columns: 
					data_sa = data_local[(data_local['%s'%s_n]==supl) & (data_local['config']=='ADC%s_atten%s'%(sarNum,aten[-1]))]
				else:
					data_sa = data_local[(data_local['%s'%s_n]==supl) & (data_local['ADC']==sarNum) & (data_local['ATTEN']==int(aten))]

				for chip_n in chip_l:
					data_chip = data_sa[data_sa['%s'%c_n_n]==chip_n]  #slice into one chip data

					#import SAR ADC reference voltage value
					if data_chip.get('SAR%d_Vref'%sarNum) is not None:
						ref_adc=data_chip.get('SAR%d_Vref'%sarNum)*1000.0
					elif data_chip.get('VREF') is not None:
						ref_adc=(data_chip.get('VREF')*1000.0).values[0]
					else:
						ref_adc = 1100.0

					d_val_in_lsb = inpt_step*aten_ratio*(4095/ref_adc)  # one step size equal to how much lsb
					lsb_mv       = 1.0/4095*ref_adc*aten_ratio          # one lsb equals to how much input voltage
					norm_ratio   = 1
					if normalize is True: norm_ratio = d_val_in_lsb     # inl & dnl results to be normalized by input voltage step size

					for i,col_n in enumerate(data_chip.columns): 
						if (col_n == '0mV') or (col_n == 'INPUT_0(mV)'):
							i_chop=i
							break
					d_l = data_chip.ix[:,data_chip.columns[i_chop:]] #chop out other information except ADC outputs
					df_temp = pd.DataFrame()
					df_temp['v_inpt']    = v_inpt
					for sat_val in [0,4095]: d_l.replace(d_l[d_l==sat_val].values,np.nan,inplace=True) #wash data
					d_l = d_l.values.tolist()[0]
					df_temp['raw']=d_l
	 				index_nz = df_temp[df_temp['raw'].notna()]['v_inpt'].index   # generate index whose value is not empty
					
					'''dnl calculation'''
					d_l.insert(0,0)
					d_l.pop(-1)
					df_temp['raw_shift'] = d_l
					# print df_temp['raw_shift'] - df_temp['raw']
					# df_temp['dnl']       = (df_temp['raw']-df_temp['raw_shift'])-d_val_in_lsb
					df_temp['dnl']       = (df_temp['raw']-df_temp['raw_shift'])/norm_ratio-1          

	 				'''use below commands if remove input offset'''
	 				delta_inpt = df_temp['v_inpt'][index_nz] - df_temp['v_inpt'][index_nz[0]]
	 				delta_d    = df_temp['raw'][index_nz] - df_temp['raw'][index_nz[0]]
	 				'''use below commands if not consider input offset'''
	 				# delta_inpt = df_temp['v_inpt'][index_nz]
	 				# delta_d    = df_temp['raw'][index_nz]
	 				slope,intercept = np.polyfit(delta_inpt,df_temp['raw'][index_nz],1)
					
					'''inl calculation'''
	 				'''choose if want to plot inl with ADC output data calibrated'''
	 				# if inl_cal is True: df_temp['inl'] = delta_d/slope*(4095.0/ref_adc*aten_ratio) - delta_inpt/lsb_mv
	 				# else:               df_temp['inl'] = delta_d - delta_inpt/lsb_mv   
	 				if inl_cal is True: df_temp['inl'] = (delta_d - delta_inpt*slope - intercept)/norm_ratio   
	 				# if inl_cal is True: df_temp['inl'] = (delta_d/slope*(4095.0/ref_adc*aten_ratio) - delta_inpt/lsb_mv)/d_val_in_lsb
	 				else:               df_temp['inl'] = (delta_d - delta_inpt/lsb_mv)/norm_ratio             

	 				val_clip=np.int(len(index_nz)*0.1)
	 				print 'INL DATA SUM CLIP BY 10%% head and tail'
	 				print 'INL MIN: %.2f'%df_temp['inl'][index_nz[val_clip:-val_clip]].min()
	 				print 'INL MED: %.2f'%df_temp['inl'][index_nz[val_clip:-val_clip]].median()
	 				print 'INL MAX: %.2f'%df_temp['inl'][index_nz[val_clip:-val_clip]].max()
	 				print 'LINE FIT slope = %.2f,intercept=%.2f'%(slope,intercept)
	 				print 'CHIP#%s'%chip_n

	 				slope_ideal = 4095.0/ref_adc*aten_ratio
	 				print 'Predict  slope = %.2f'%slope_ideal
	 				slope_l.append(slope)
	 				inter_l.append(intercept)

	 				x = df_temp['v_inpt']
	 				xlim = inpt_lim[np.int(aten[-1])]
	 				xstp = inpt_plt_step[np.int(aten[-1])]
	 				#plot INL
	 				fx2.plot(x,df_temp['inl'],label='chip#%s_VDD%s_atten%s'%(chip_n,supl,aten[-1]))
	 				fx2.set_xlim(0,xlim)
	 				fx2.set_xticks(np.arange(0,(xlim+1),xstp))
					fx2.set_xlabel('Input VOL(mv)')
					fx2.set_ylabel('ADC Measure (LSB)')
					fx2.set_title('- INL -  %s SAR%s-ADC step_size%dmV'%(chiptype,sarNum,inpt_step))
					if inl_cal:
						ylim =35
		 				fx2.set_ylim(-ylim,ylim)
		 				fx2.set_yticks(np.arange(-ylim,ylim+1,5))
					fx2.legend(loc=0)
					#plot DNL
					fx1.plot(x,df_temp['dnl'],label='chip#%s_VDD%s_atten%s'%(chip_n,supl,aten[-1]))
	 				fx1.set_xlim(0,xlim)
	 				fx1.set_xticks(np.arange(0,(xlim+1),xstp))
	 				# fx1.set_ylim(-25,25)
					fx1.set_xlabel('Input VOL(mv)')
					fx1.set_ylabel('ADC Measure (LSB)')
					fx1.legend(loc=0)
					fx1.set_title('- DNL -  %s SAR%s-ADC step_size%dmV'%(chiptype,sarNum,inpt_step))
					#plot RAW data
					fx3.plot(x,df_temp['raw'],label='chip#%s_VDD%s_atten%s'%(chip_n,supl,aten[-1]))
					'''use ideal slope to plot adc output'''
					x_ideal = df_temp['v_inpt'][index_nz]
					y_ideal = slope_ideal*x_ideal
					fx3.plot(x_ideal,y_ideal,'--',label='chip#%s_VDD%s_atten%s_ideal'%(chip_n,supl,aten[-1]))
	 				# fx3.set_xticks(np.arange(0,inpt_lim[np.int(aten)]+10,inpt_step))
	 				fx3.set_xlim(0,xlim)
	 				fx3.set_xticks(np.arange(0,(xlim+1),xstp))
	 				fx3.set_ylim(0,4095)
					fx3.set_xlabel('Input VOL(mv)')
					fx3.set_ylabel('ADC Measure (LSB)')
					fx3.set_title('- RAW -  %s SAR%s-ADC step_size%dmV'%(chiptype,sarNum,inpt_step))
					fx3.legend(loc=0)

		# for i,s in enumerate(supl_l):
		# 	fx3.text(50,(3000-100*i),'Supply=%s: slope:%.2f intcept=%.2f'%(s,slope_l[i],inter_l[i]),fontsize=12)
		if savefig is True: 
			fg1.savefig(pic_path+'/%s_sar%s_MB#%s'%(chiptype,sarNum,boardNum),dpi=300)
			plt.close()

	def plot_adc_noise_floor(self,data,sample_cnt=1000,atten_l=None,chip_num=1,recenter=False,x_lim=None):
		'''
		:brief: plots adc input noise floor
		:file:  file_example: adc_noisefloor_32vs722.csv
		:param:
			- chip: choose how many chips to be plotted in same figure,
					check available number of chips to be plotted
			- recenter: center data to y-axis using mean value reduction
			- x_lim: set xlim_range
		'''
		data_local  = data
		chip_type_l = data_local.CHIP_TYPE.drop_duplicates().values
		if atten_l == None:     atten_l     = [0,1,2,3]
		adc_type_l  = [1,2]

		cnt = 0
		l_722,l_32  = [],[]
		for c_t in chip_type_l:
			if c_t.split('_')[0] == '722':  l_722.append(c_t)
			elif c_t.split('_')[0] == '32': l_32.append(c_t)
		chip_use = l_722[:chip_num]+l_32[:chip_num]

		# top_rng = []
		# bot_rng = []

		fg1,fx1=plt.subplots(2,1)
		for c_t in chip_use:
			data_pick = data_local[data_local.CHIP_TYPE == c_t]
			for aten in atten_l:
				data_pic = data_pick[data_pick.ATTEN == aten]
				for adc_t in adc_type_l:
					data_pi = data_pic[data_pic.ADC == adc_t]
					y = [data_pi['%s'%i].values[0] for i in np.arange(sample_cnt)]
					if recenter == True: y = y - np.array(y).mean() 
					fx1[adc_t-1].hist(y,bins=100,alpha=0.5,label='%s ATTEN=%s std=%.2f'%(
										data_pi.CHIP_TYPE.values[0],aten,np.array(y).std()))

		fx1[0].set_title('SAR1-ADC Noise Floor 32 vs 722 ')
		fx1[1].set_title('SAR2-ADC Noise Floor 32 vs 722 ')
		for i in adc_type_l:
			fx1[i-1].set_ylabel('ADC OUTPUT')
			fx1[i-1].legend()
			if x_lim is not None: fx1[i-1].set_xlim(-x_lim,x_lim)
			
		# for i in [1,2]:
		# 	data_pick  = data_local.loc[i]
		# 	#use alpha to set color transparency
		# 	data_pick[1:].plot.hist(bins=100,alpha=0.5,label='%s'%data_pick[0])
		# 	top_range.append((data_pick[1:].max()/100+1)*100) 
		# 	btm_range.append((data_pick[1:].min()/100)*100) 
		# plt.legend()
		# t_u = np.array(top_rng).max()
		# b_u = np.array(btm_rng).min()
		# plt.xticks(np.arange(b_u,(t_u+10),10))
		# plt.title('CHIP722 ADC1&2 Noise Floor Vin=%s %s'%(data_pick[0][:5],data_pick[0][-6:]))

	def plot_pvt(self,data,sor_val=0,plot_all=True,ldo_nume=False):
		'''
		:brief: plots to compare pvt sensor, digital ldo, light sleep current
		'''
		# sor_l = ['DIG_LDO','dig_dbias=0','v_dig_7_0_Curr(mA)']
		sor_l = ['DIG_LDO','PVT_DIG_DBIAS_0','I(mA)_LITSLP_7_0','V(V)_LITSLP_7_0','I(uA)_DSP']
		data_sort = data.sort_values(by='%s'%sor_l[sor_val]).reset_index(drop=True)
		fg1,fx1=plt.subplots(4,1,sharex=True)
		fx1[0].scatter(data_sort.DIG_LDO.index,data_sort.DIG_LDO.values)
		fx1[0].set_title('DIG LDO')
		fx1[0].set_ylabel('Voltage (V)')
		mrk_l = ['d','v','o','x']
		clr_l = ['b','r','k','g']
		if plot_all == True:
			pvt_l = [0,4,7]
			lsp_l = ['7_0','3_0','0_1','0_5']
		else:
			pvt_l = [0]
			lsp_l = ['7_0']
		for i,p in enumerate(pvt_l):
			d_u = data_sort['%s%d'%(sor_l[1][:-1],p)]
			if ldo_nume:
				fx1[1].scatter(d_u.index,(d_u/data_sort['DIG_LDO']/data_sort['DIG_LDO']).values,
					color=clr_l[i],marker=mrk_l[i],label='dbias=%d'%p)			
			else:
				fx1[1].scatter(d_u.index,d_u.values,color=clr_l[i],marker=mrk_l[i],label='dbias=%d'%p)
		for i,l in enumerate(lsp_l):
			d_u = data_sort['%s%s'%(sor_l[2][:-3],l)]
			fx1[2].scatter(d_u.index,d_u.values,color=clr_l[i],marker=mrk_l[i],label='config=%s'%l)
			# d_u = data_sort['%s%s'%(sor_l[3][:-3],l)]
			# d_u = data_sort['%s%d%s'%(sor_l[3][:6],l,sor_l[3][-9:])]
			# fx1[3].scatter(d_u.index,d_u.values,color=clr_l[i],marker=mrk_l[i],label='config=%s'%l)
			d_u = data_sort['%s'%(sor_l[4])]
			fx1[3].scatter(d_u.index,d_u.values,color=clr_l[i],marker=mrk_l[i],label='config=%s'%l)

		fx1[1].set_title('PVT READ')
		fx1[2].set_title('LIGHT SLEEP CURRENT')
		fx1[3].set_title('%s'%sor_l[4])
		# fx1[3].set_title('LIGHT SLEEP VOLTAGE')
		fx1[2].set_ylabel('Current (mA)')
		fx1[3].set_ylabel('Current (uA)')
		# fx1[3].set_ylabel('Voltage (V)')
		for i in [0,1,2,3]: fx1[i].legend()
		fx1[3].set_xlim(-1,len(data_sort))
		# fx1[3].set_xlim(-1,40)
		# fx1[0].set_ylim(1.04,1.09)
		# fx1[3].set_ylim(0.68,0.73)

class htolVisualizer(object):
	'''class to plot measurement data sets
	
	'''
	def __init__(self, data_file_path, save_path, chip_ver):
		self.df = pd.read_csv(data_file_path)
		self.cv = chip_ver

		self.sp = save_path if save_path.endswith('/') else save_path+'/'
		if not os.path.exists(self.sp):os.makedirs(self.sp)

		#standard column list
		self.s_c_l = ['TEMP','SUPPLY','CHIP#','MAC',
		'SWD_1','O_CODE_1','I_EN0(uA)','I_EN10(uA)',
		'I_LSLP_6_0(mA)','I_WAKE_6_0(mA)','I_DSLP(uA)',
		'PVT_DIG_DBIAS_4','VDD33(ADC)','32K_STARTUP(us)','FREQ_32K','FREQ_150K','FREQ_8M',
		'VREF_1V','RTC_LDO','DIG_LDO','SAR1_REF','SAR2_REF','VCM',
		'TSEN_RP_os0(V)','TSEN_VP_os0(V)','TSEN_VN_os0(V)','T_CHOP_2','O_CODE_2','SWD_2',
		'V_LSLP_7_0(V)','V_WAKE_7_0(V)','V_LSLP_6_0(V)','V_WAKE_6_0(V)','V_LSLP_3_0(V)','V_WAKE_3_0(V)','V_LSLP_0_1(V)','V_WAKE_0_1(V)','V_LSLP_0_5(V)','V_WAKE_0_5(V)',
		'ADC1_AT3_DREF0','ADC2_AT3_DREF0','O_CODE_3','SWD_3','DSLP']
		
		#standard column list used for plots
		self.s_c_l_plot = ['O_CODE_1','O_CODE_2','O_CODE_3',
		'I_EN0(uA)','I_EN10(uA)','I_LSLP_6_0(mA)','I_DSLP(uA)',
		'PVT_DIG_DBIAS_4','VDD33(ADC)','32K_STARTUP(us)','FREQ_32K','FREQ_150K','FREQ_8M',
		'VREF_1V','RTC_LDO','DIG_LDO','SAR1_REF','SAR2_REF','VCM',
		'TSEN_RP_os0(V)','TSEN_VP_os0(V)','TSEN_VN_os0(V)','T_CHOP_2',
		'V_LSLP_7_0(V)','V_LSLP_6_0(V)','V_LSLP_3_0(V)','V_LSLP_0_1(V)','V_LSLP_0_5(V)',
		'ADC1_AT3_DREF0','ADC2_AT3_DREF0']

	def plot_htol_diff(self, file_path):
		'''compare each htol phase value difference in one plot

		:param file_path: full path of data excel file
		'''
		sheet_l = ['168h-0h','500h-0h', '500h-168h']
		df_l = [pd.read_excel(file_path,sheet_name= s) for s in sheet_l]
		for chk_item in self.s_c_l_plot:
			fg1,fx1=plt.subplots(3,1, sharex=True)
			for i, s in enumerate(sheet_l):
				for v in [2.7, 3.3, 3.6]:
					_df = df_l[i].groupby('SUPPLY').get_group((v))[chk_item]
					_bin_max = _df.max()
					_bin_min = _df.min()
					bin_range = np.linspace(_df.min(), _df.max(), 30)

					sns.distplot(_df, ax=fx1[i],label='%sV'%v, kde=True, hist= True,bins=bin_range)

				fx1[i].legend()
				fx1[i].set_title('%s HTOL %s -- '%(self.cv.upper(),s) + chk_item)
				fx1[i].axvline(0,color='r',linestyle='dashed')
			fg1.set_size_inches(12,15)
			fg1.savefig(self.sp+'%s_htol_%s.png'%(self.cv.lower(), chk_item),dpi=300)
			plt.close('all')

	def plot_htol(self, data_path, chk_item = 'I_DSLP(uA)'):
		'''use below script to compare between different htol phases

		'''
		f_l = ['CHIP722M1_HTOL_PST332H_BOMFAIL.csv', 'CHIP722M1_HTOL_PST500H.csv']
		fg1, fx1 = plt.subplots(2,1, sharex=True)
		for _, k in enumerate(f_l):
			df = pd.read_csv(data_path+'/'+k)
			dfg=df.groupby('SUPPLY')
			for i in [2.7, 3.3, 3.6]:

				dfg.get_group((i))[chk_item].plot.hist(bins=100,alpha=0.5, ax=fx1[_],label='VDD=%s'%i)
			fx1[_].legend()
		fx1[0].set_title('MARLIN3 HTOL PST 332Hours')
		fx1[1].set_title('MARLIN3 HTOL PST 500Hours')
