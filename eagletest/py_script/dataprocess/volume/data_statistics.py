from baselib.loglib.log_lib import *
from baselib.loglib.log_csv import csvreport
import re as re
import os as os
import pandas as pd
import numpy as np
import time
from collections import OrderedDict
from collections import defaultdict

class dataStater(object):
	'''script used to summarize washed data sets

	'''
	def __init__(self):
		self.col_l_des = ['CLK_8M', '', 
						  'I_EN0(uA)','I_EN10(uA)', '',
						  'VDD33(ADC)', '', 
						  '32K_STARTUP(us)', '',
						  'FREQ_8M', 'FREQ_150K', '',
						  'RTC_LDO', 'DIG_LDO', 'SAR1_REF', 'SAR2_REF', 'VCM', '',
						  'VREF_1V', 'O_CODE', 'O_CODE_0', 'O_CODE_1', 'O_CODE_2', 'O_CODE_3', '',
						  'PVT_DIG_DBIAS_4', '',
						  'TSEN_RP_os0(V)','TSEN_VP_os0(V)', 'TSEN_VN_os0(V)', '',
						  'T_OS_0', '',
						  'I_LSLP_WFPD0(mA)', 'I_LSLP_WFPD1(mA)', 'I_LSLP_WF_D(mA)', '',
						  'V_LSLP_7_0(V)', 'V_LSLP_6_0(V)', 'V_LSLP_3_0(V)', 'V_LSLP_0_1(V)', 'V_LSLP_0_5(V)', '',
						  'I_LSLP_7_0(mA)', 'I_LSLP_6_0(mA)', 'I_LSLP_3_0(mA)', 'I_LSLP_0_1(mA)', 'I_LSLP_0_5(mA)', '',
						  'I_DSLP(uA)']

	def df_describe(self, file_name, percentiles=[.01, .03, .5, .97, .99]):
		'''function to generate data statistic summary file in csv format

		:param file_name: complete file_path + file_name
		:param chip_ver:  'chip722', 'marlin3', 'marlin3s' 
		'''
		f_n = '/'.join(file_name.split('/')[:-1])
		f_n += '/'+'_'.join(file_name.split('/')[-1].split('_')[0:2])
		raw_rd = pd.read_csv(file_name)

		df_d = pd.DataFrame()
		df_d = df_d.append(raw_rd.describe(percentiles=percentiles))
		df_d = df_d.reindex(columns=self.col_l_des).T
		df_d.to_csv(f_n +'_describe.csv')

		#3.3V corner describe
		raw_r_g = raw_rd.groupby(['SUPPLY','CORNER'])
		df_d = pd.DataFrame()
		for i in ['tt','ff','ss']:
			df_tmp = raw_r_g.get_group((3.3,'%s'%(i)))
			df_d   = df_d.append(df_tmp.describe(percentiles=percentiles))
		df_d = df_d.reindex(columns=self.col_l_des).T
		df_d.to_csv(f_n +'_3.3V_corner_describe.csv')

		#all voltages corner describe
		raw_r_g = raw_rd.groupby(['CORNER'])
		df_d = pd.DataFrame()
		for i in ['tt','ff','ss']:
			df_tmp = raw_r_g.get_group(('%s'%(i)))
			df_d   = df_d.append(df_tmp.describe(percentiles=percentiles))
		df_d = df_d.reindex(columns=self.col_l_des).T
		df_d.to_csv(f_n +'_corner_describe.csv')
		return 

	def df_describe_by_condition(self, df, column_name, condition_name, percentiles=None):
		'''generate a new dataframe describes data statistics based on given condition

		:param df:             target dataframe
		:param column_name:    name of the column to be displayed
		:param condition_name: name of the column used to group data
		:param percentiles:    customize statistic dispaly details
		'''
		df_g  = df.groupby(by=condition_name)
		key_l =  df_g.groups.keys()
		df_d  = pd.DataFrame()
		df_d  = df_d.reindex(columns= np.sort(key_l))
		for i in key_l:
		    df_d[i] = df_g.get_group(i)[column_name].describe(percentiles= percentiles)
		return df_d

	#not sure if still works, need to test
	def dt_find_3pc(self,file_name):
		'''find 3pcs chip num of min,med,max among all chips
		'''
		df = pd.read_csv(file_name)
		dict_pick = defaultdict()

		#remove columns not going to be checked
		col_name_l = df.columns.tolist()
		for col_n in ['CHIP_NUM','SUPPLY','CHIP_MAC','CHIP_TYPE']:
			col_name_l.remove(col_n)

		#go through columns find 3pcs extreme value parts
		for col_name in col_name_l:
			val_min = df[col_name].min()
			val_max = df[col_name].max()
			val_med = df[col_name].median()
			val_dict = {'MIN':val_min, 'MED':val_med, 'MAX':val_max}
			df_temp = df.sort_values(by=col_name).reset_index(drop=True)

			#go through extreme values
			for _t, _v in val_dict.items():
				i_use = df_temp[df_temp[col_name]==_v].index.values[0]
				if _t == 'MIN':
					i_use_list = [i_use,i_use+1,i_use+2]
				elif _t == 'MED':
					i_use_list = [i_use-1,i_use,i_use+1]
				else:
					i_use_list = [i_use,i_use-1,i_use-2]

				for i in i_use_list:
					dict_pick['COL_NAME'].append(col_name)
					dict_pick['CHIP_NUM'].append(df_temp.loc[i]['CHIP_NUM'])
					dict_pick['VAL_TYPE'].append('%s_%d'%(_t,i))
					dict_pick['VALUE'].append(df_temp.loc[i][col_name])

		df_pick = pd.DataFrame(dict_pick)
		df_pick.to_csv(file_name[:-4]+'_pick3pcs.csv',index=False)
		print df_pick.CHIP_NUM.drop_duplicates()