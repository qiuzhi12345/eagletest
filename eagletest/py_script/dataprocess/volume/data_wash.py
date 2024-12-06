from baselib.loglib.log_lib import *
from baselib.loglib.log_csv import csvreport
import re as re
import os as os
import pandas as pd
import numpy as np
import time
from collections import OrderedDict
from collections import defaultdict

from dataprocess.volume._data_address import *
from dataprocess.volume.mac_lookup import macLookUp as MLU

class dataWasher(object):
	'''script used to process data generated in volume test, like socket test, multiboard test, oven test
		
		Data file naming rules, please include below information:

		Data file examples who fits below data process script has a copy saved under:
	'''
	def __init__(self):
		self.mlu = MLU()

		#use for mac file lookup
		self.chip_type_dict={'chip722' :800,
							 'marlin3' :400,
							 'marlin3s':600
							}
		#use for OnePiece address lookup
		self.chip_addr_dict={'chip722': OP_CHIP722,
							 'marlin3': OP_MARLIN3,
							 'marlin3s': OP_MARLIN3S
							}

		#list to record if chip is a corner lot or not
		self.chip_corner_list = ['marlin3s']

		#standard column names for all kinds of test to follow
		self.column_for_all = ['TEMP','SUPPLY','BOARD','NAME', 'CHIP#', 'LOC#', 'TYPE', 'CORNER',
							   'MAC', 'CLK_8M',
							   'VREF_1V', 'O_CODE',
							   'VREF_1V_0', 'VREF_1V_1', 'VREF_1V_2', 'VREF_1V_3',
							   'O_CODE_0', 'O_CODE_1', 'O_CODE_2', 'O_CODE_3',
							   'SWD_0', 'SWD_1', 'SWD_2', 'SWD_3',
							   'RTC_LDO', 'DIG_LDO', 'SAR1_REF', 'SAR2_REF', 'VCM',
							   'FREQ_8M', 'FREQ_150K', 'FREQ_32K', '32K_STARTUP(us)',
							   'PVT_DIG_DBIAS_4', 'VDD33(ADC)',
							   'TSEN_RP_os0(V)', 'TSEN_VN_os0(V)','TSEN_VP_os0(V)', 
							   'T_CHOP_0', 'T_CHOP_1', 'T_CHOP_2', 'T_CHOP_3',
							   'T_OS_-1', 'T_OS_-2', 'T_OS_0', 'T_OS_1', 'T_OS_2', 
							   'ADC1_AT3_DREF0', 'ADC2_AT3_DREF0', 
							   'I_EN0(uA)', 'I_EN10(uA)', 
							   'I_LSLP_WFPD0(mA)', 'I_LSLP_WFPD1(mA)','I_LSLP_WF_D(mA)', 
							   'V_LSLP_7_0(V)',  'V_LSLP_6_0(V)',  'V_LSLP_3_0(V)',  'V_LSLP_0_1(V)',  'V_LSLP_0_5(V)', 
							   'V_WAKE_7_0(V)',  'V_WAKE_6_0(V)',  'V_WAKE_3_0(V)',  'V_WAKE_0_1(V)',  'V_WAKE_0_5(V)',
							   'I_LSLP_7_0(mA)', 'I_LSLP_6_0(mA)', 'I_LSLP_3_0(mA)', 'I_LSLP_0_1(mA)', 'I_LSLP_0_5(mA)', 
							   'I_WAKE_7_0(mA)', 'I_WAKE_6_0(mA)', 'I_WAKE_3_0(mA)', 'I_WAKE_0_1(mA)', 'I_WAKE_0_5(mA)',
							   'I_DSLP(uA)', 'DSLP']

		#columns not being checked for data integrity
		self.column_str_not_check = ['TEMP','SUPPLY','BOARD','NAME', 'CHIP#', 'TYPE', 'CORNER','EFUSE_BURNED',
							   'MAC', 'CLK_8M',
							   'SWD_0', 'SWD_1', 'SWD_2', 'SWD_3',
							   'V_WAKE_0_1(V)', 'V_WAKE_0_5(V)', 'V_WAKE_3_0(V)', 'V_WAKE_6_0(V)', 'V_WAKE_7_0(V)',
							   'I_WAKE_0_1(mA)', 'I_WAKE_0_5(mA)', 'I_WAKE_3_0(mA)', 'I_WAKE_6_0(mA)', 'I_WAKE_7_0(mA)',
							   'DSLP']

		#dictonaries to be used for renaming columns
		dict_marlin3_sckt_rn = dict([('CHIP_MAC','MAC'), ('CHIP_NUM','CHIP#'),('CHIP_TYPE','TYPE')] +
								   [('I(mA)_LITSLP_%s'%i,'I_LSLP_%s(mA)'%i) for i in ['0_1', '0_5', '3_0','7_0']] +
								   [('I(mA)_WAKEUP_%s'%i,'I_WAKE_%s(mA)'%i) for i in ['0_1', '0_5', '3_0','7_0']] +
								   [('V(V)_LITSLP_%s'%i,'V_LSLP_%s(V)'%i) for i in ['0_1', '0_5', '3_0','7_0']] +
								   [('V(V)_WAKEUP_%s'%i,'V_WAKE_%s(V)'%i) for i in ['0_1', '0_5', '3_0','7_0']] +
								   [('I(uA)_DSP', 'I_DSLP(uA)'),('I(uA)_EN0', 'I_EN0(uA)'), 
								   ('I(uA)_EN10', 'I_EN10(uA)'),('I_DELTA(mA)','I_LSLP_WF_D(mA)'),
								   ('I_LSLP(mA)_WIFIPD0','I_LSLP_WFPD0(mA)'),('I_LSLP(mA)_WIFIPD1','I_LSLP_WFPD1(mA)'),
								   ('TSEN_RP(V)_os0','TSEN_RP_os0(V)'),('TSEN_VN(V)_os0','TSEN_VN_os0(V)'),('TSEN_VP(V)_os0','TSEN_VP_os0(V)'),
								   ('adc1','ADC1_AT3_DREF0'),('adc2','ADC2_AT3_DREF0')])

		#dictonary for chip722
		adc_l = []
		for k in [0,1,2,3]:
			for i in [0,1,2,4]:
				adc_l.append((k,i))

		ref_l = ['Vref_1V', 'RTC_ldo', 'DIG_ldo', 'SAR1_ref', 'SAR2_ref', 'Vcm', 'T_rp(V)_offset0_', 'T_vp(V)_offset0_', 'T_vn(V)_offset0_']
		ref_l_2 = []
		for i in ref_l:
			for k in adc_l:
				ref_l_2.append(i+'(adc_atten%s_dref%s)'%(k[0],k[1]))


		ref_l_u = ['VREF_1V', 'RTC_LDO', 'DIG_LDO', 'SAR1_REF', 'SAR2_REF', 'VCM', 'TSEN_RP_os0(V)', 'TSEN_VP_os0(V)', 'TSEN_VN_os0(V)']
		ref_l_u_2 = []
		for i in ref_l_u:
			for k in adc_l:
				ref_l_u_2.append(i+'_A%s_D%s'%(k[0],k[1]))

		dict_chip722_sckt_rn = dict([('CHIP_NUM','CHIP#'),('CHIP_MAC','MAC'), ('chip_type','TYPE'), 
								     ('Vdd33(adc)','VDD33(ADC)'), 
									 ('32K_Startup(us)','32K_STARTUP(us)'), ('freq_150k','FREQ_150K'), ('freq_8m','FREQ_8M'), ('freq_32k','FREQ_32K'), 
									 ('Vref_1V','VREF_1V'), ('RTC_ldo','RTC_LDO'), ('DIG_ldo','DIG_LDO'), ('SAR1_ref','SAR1_REF'),('SAR2_ref','SAR2_REF'),('Vcm','VCM'), 
									 ('T_rp(V)_offset0','TSEN_RP_os0(V)'), ('T_vp(V)_offset0','TSEN_VP_os0(V)'), ('T_vn(V)_offset0','TSEN_VN_os0(V)'), 
									 ('Tsen_offset:-2','T_OS_-2_ADC'), ('T(/C)_offset:-2','T_OS_-2'), ('Tsen_offset:-1','T_OS_-1_ADC'), ('T(/C)_offset:-1','T_OS_-1'),
									 ('Tsen_offset:0','T_OS_0_ADC'), ('T(/C)_offset:0','T_OS_0'),('Tsen_offset:1','T_OS_1_ADC'),('T(/C)_offset:1','T_OS_1'),('Tsen_offset:2','T_OS_2_ADC'),('T(/C)_offset:2','T_OS_2'), 
									 ('Tsen_chop:0','T_CHOP_0_ADC'), ('T(/C)_chop:0','T_CHOP_0'), ('Tsen_chop:1','T_CHOP_1_ADC'), ('T(/C)_chop:1','T_CHOP_1'), ('Tsen_chop:2','T_CHOP_2_ADC'), ('T(/C)_chop:2','T_CHOP_2'),
									 ('Tsen_chop:3','T_CHOP_3_ADC'), ('T(/C)_chop:3','T_CHOP_3'), 
									 ('dbg7_dbias0_Volt(V)','V_LSLP_7_0(V'), ('dbg3_dbias0_Volt(V)','V_LSLP_3_0(V)'), ('dbg0_dbias1_Volt(V)','V_LSLP_0_1(V)'), ('dbg0_dbias5_Volt(V)','V_LSLP_0_5(V)')]+
									zip(['dbg7_dbias0_Curr(mA)', 'dbg3_dbias0_Curr(mA)', 'dbg0_dbias1_Curr(mA)', 'dbg0_dbias5_Curr(mA)'], ['I_LSLP_7_0(mA)', 'I_LSLP_3_0(mA)', 'I_LSLP_0_1(mA)', 'I_LSLP_0_5(mA)'])+
									 [('Deepslp_cur(uA)','I_DSLP(uA)')]+
									zip(ref_l_2, ref_l_u_2))



		dict_chip722_mb_rn = dict(zip(['Temp', 'Supply', 'CHIP', 'O_code_1', 'vref_1v_1', 'SWD_mk_1','SWD_mk_2','SWD_mk_3'],
									  ['TEMP', 'SUPPLY', 'CHIP#', 'O_CODE_1', 'VREF_1V_1', 'SWD_1', 'SWD_2', 'SWD_3'])+
       							  zip(['Vdd33(adc)', '32K_Startup(us)', 'freq_32k', 'freq_150k', 'freq_8m'],
       							  	  ['VDD33(ADC)', '32K_STARTUP(us)', 'FREQ_32K', 'FREQ_150K', 'FREQ_8M'])+ 
       							  zip(['Vref_1V','O_code_2', 'vref_1v_2', 'O_code_3', 'vref_1v_3'],
       							  	  ['Vref_1V', 'O_CODE_2', 'VREF_1V_2', 'O_code_3', 'VREF_1V_3'])+
       							  [('Dslp','DSLP'), ('adc1','ADC1_AT3_DREF0')]+
       							  zip(['T_rp(V)_offset0', 'T_vp(V)_offset0', 'T_vn(V)_offset0'], ['TSEN_RP_os0(V)', 'TSEN_VP_os0(V)', 'TSEN_VN_os0(V)'])+
								  zip(['VREF_1V'+'_A%s_D%s'%(k[0],k[1]) for k in adc_l], ['Vref_1V'+'(adc_atten%s_dref%s)'%(k[0],k[1]) for k in adc_l])+
								  [('v_dig_%s_V'%i, 'V_LSLP_%s(V)'%i) for i in ['7_0','3_0','0_1','0_5']]+
								  [('weakup:%s'%i, 'V_WAKE_%s(V)'%i) for i in ['7_0','3_0','0_1','0_5']]+
								  zip(['T_os:-2', 'T_os:-1', 'T_os:0', 'T_os:1', 'T_os:2', 'T_chop:0', 'T_chop:1', 'T_chop:2', 'T_chop:3'],
								      ['T_OS_-2', 'T_OS_-1', 'T_OS_0', 'T_OS_1', 'T_OS_2', 'T_CHOP_0', 'T_CHOP_1', 'T_CHOP_2', 'T_CHOP_3']))

		self.column_rename_dict = {'chip722_sckt':dict_chip722_sckt_rn,
								   'chip722_mb':  dict_chip722_mb_rn,
								   'marlin3_sckt':dict_marlin3_sckt_rn,
								   'marlin3_mb':{},
								   'marlin3s_sckt':{'CHIP_NUM':'CHIP#','CHIP_MAC':'MAC','CHIP_TYPE':'TYPE'},
								   'marlin3s_mb'  :{'TEMPR':'TEMP','SUPPLY(V)':'SUPPLY'}
								   }

	def _rd_file(self, dir_name):
		'''merge all data files under current directory to be one dataframe

		:param dir_name: given directory address where data files to be processed
		'''
		file_list = os.listdir(dir_name)
		df  = pd.DataFrame()
		for i in file_list:
			# df = df.append(pd.read_csv(dir_name+'/'+i), sort=False)
			df0 = pd.read_csv(dir_name+'/'+i)
			df = pd.concat(objs=[df,df0], axis=0, join='outer', sort=False, ignore_index=True)

		# df_l = [pd.read_csv(dir_name+'/'+i) for i in file_list]
		# df = pd.concat(objs=df_l, axis=0, join='outer', sort=False)

		#reset index for all data
		df.reset_index(drop=True, inplace=True)
		df.drop_duplicates(inplace=True)
		return df 

	'''column related actions'''
	def _rearrange_column(self, df, col_new_list):
		# df = df.ix[:,col_new_list] # not recommended
		return df.reindex(columns=col_new_list)

	def _add_column(self, df, column_name, position, new_values=None):
		'''add new column to a dataFrame or replace exsiting column values with new ones

		:param df:            dataframe to be modified
		:param column_name:   name of the column to be added
		:param position:      where to insert such column
		:param column_values: values of the new column
		'''
		if column_name not in df.columns:
			col_l = df.columns.tolist()
			col_l.insert(position,column_name)
			# df = df.reindex(columns=col_l)
			df = self._rearrange_column(df=df, col_new_list=col_l)

		if new_values is not None:
			df[column_name] = new_values

		return df

	def _rm_column(self, df, column_list):
		'''remove unwanted columns

		:param column_list: pass a list of column names to be removed
		'''
		return df.drop(columns=column_list,axis=1,inplace=True)

	def _rename_column(self, df, col_dict):
		'''rename column names based on given dictionary

		:param col_dict: {'old_name':'new_name'}
		'''
		df.rename(columns=col_dict,inplace=True)
		return df

	def _arrange_data_column_default(self,df, col_dict=None, for_merge=True):
		'''rearrange dataframe column name sequence, rename column names to be uniform
		
		'''
		if col_dict is not None:
			df = self._rename_column(df=df, col_dict=col_dict)
		if for_merge:
			df = self._rearrange_column(df=df, col_new_list=self.column_for_all)
		else:
			cnl = list(self.column_for_all)
			dfc = list(df.columns)
			#re-arrange column names 
			for i in set.difference(set(cnl), set(dfc)):
				if i in cnl:
					cnl.remove(i)
				else:
					cnl.append(i)
			df = self._rearrange_column(df=df, col_new_list =cnl)

		return df

	'''entire dataframe related actions'''
	def _sort_resetIndex_save(self, df, bylist=None, save_name = None):
		'''sort given dataframe and save as specified file name

		:param bylist:    sort values by this list
		:param save_name: use complete path & file name
		'''
		if bylist is not None:
			df.sort_values(by=bylist, inplace=True)
		df.reset_index(drop=True, inplace=True)
		# df.drop_duplicates(inplace=True)
		if save_name is not None:
			df.to_csv(save_name,index=False)
			'''not sure why drop_duplicates is not working, probabaly due to dtype of columns
			   looks like reload the file helps, added below commands for temperorary bypass
			'''
			df = pd.read_csv(save_name)
			df.drop_duplicates(inplace=True)
			df.to_csv(save_name,index=False)
		return df

	def _locate_chip_by_condition(self,df, col_n, upl, dnl):
		return df[(df[col_n]>upl) | (df[col_n] < dnl)]['CHIP#']

	def _serial_chip_num_by_MAC(self, df, chip_type='marlin3', en_ver=False, en_print=True):
		'''add CHIP# column to given dataframe use exsiting MAC column

		:param chip_type: choose from 'chip722', 'chip722m', 'marlin3'
		:param en_ver:    if True, will return chip version based on given MAC
		:param en_print:  if True, will printing MAC lookup results
		'''
		s_n = lambda x: getattr(self.mlu, 'wc_%s_%d'%(chip_type, self.chip_type_dict[chip_type]))(x,en_ver,en_print)
		if en_ver:
			col_num = [s_n(i)[0] for i in df['MAC']] 
			col_ver = [s_n(i)[1] for i in df['MAC']] 
			return col_num, col_ver
		else:
			col_num = [s_n(i)[0] for i in df['MAC']] 
			return col_num

	def _rm_bad_data_points(self, df, col_name, uplimit, dnlimit, replace_val=None):
		'''remove out of bound values of one column due to measurement offset or other issue

 		:param df:      dataframe to be washed
		:param col_ref: list of column names to be cleaned up
		:param uplimit: list of data up-limits
		:param dnlimit: list of data down-limits 
		'''
		_rm_ov_rng = lambda x: replace_val if (x>uplimit or x <dnlimit) else x
		return df[col_name].apply(_rm_ov_rng)

	def _err_lst_add_row(self, df, df_err, col_base, col_n, chip_index):
		'''add data row to errr list table

		'''
		if chip_index in df_err['INDEX'].values:
			_index = df_err[df_err['INDEX']==chip_index].index.tolist()[0]
			df_err.ix[_index, col_n] = df.loc[chip_index][col_n]
		else:
			#get chip_num and related values
			_val_list = [df.loc[chip_index][_col] for _col in (col_base+[col_n])]
			#transform into dictonary format
			_val_list.insert(0,chip_index)
			_dict_err = dict(zip(['INDEX']+col_base+[col_n],_val_list))
			df_err = df_err.append(_dict_err, ignore_index=True)
		return df_err

	def _data_wash(self,df, col_list=None, uplimit=None, dnlimit=None,replacement=None, save_name=None):
		'''set uplimit and removes out of bound data due to test error

		:param df:      dataframe to be washed
		:param col_list: list of column names to be cleaned up
		:param uplimit: list of data up-limits
		:param dnlimit: list of data down-limits
		'''
		col_base = ['LOC#','CHIP#','MAC','SUPPLY','TEMP'] if 'LOC#' in df.columns else ['CHIP#','MAC','SUPPLY','TEMP']
		df_err = pd.DataFrame(columns=['INDEX'] + col_base + col_list)

		#check if any string hide inside data column
		col_str_check = list(set(df.columns) - set(self.column_str_not_check))
		for col_n in col_str_check:
			if df[col_n].dtype == object:
				str_check = df[df[col_n].str.contains(r'(?=.*[a-zA-Z])', na=False)]
				# if str_check.index.tolist() !=[]:
				for i_str_check in str_check.index.tolist():
					df_err = self._err_lst_add_row(df=df, df_err=df_err, col_base=col_base, col_n = col_n, chip_index=i_str_check)
					df.ix[i_str_check, col_n] = None

		#rearrange data columns 
		df = self._arrange_data_column_default(df=df, for_merge=False)

		for i,col_n in enumerate(col_list):
			upl     = uplimit[i]
			dnl     = dnlimit[i]
			p_l = [logcolor(col_n,'y'), logcolor('%.2f'%upl,'r'), logcolor('%.2f'%dnl,'r')]

			print('Washing Column: %s, UP_limit: %s, DN_limit: %s'%(p_l[0],p_l[1],p_l[2]))

			#convert column data to be numerics, and report out of range ones
			df[col_n] = pd.to_numeric(df[col_n])
			for _c in self._locate_chip_by_condition(df, col_n, upl, dnl).index:
				#add error data into error list 
				df_err = self._err_lst_add_row(df=df, df_err=df_err, col_base=col_base, col_n = col_n, chip_index=_c)
				print('FOUND#%s'%df.loc[_c]['CHIP#'])

			#now wash it
			df[col_n] = self._rm_bad_data_points(df=df, col_name=col_n, uplimit=upl, dnlimit=dnl, replace_val=replacement)

		if save_name is not None:
			df     = self._sort_resetIndex_save(df=df, bylist=['CHIP#'], save_name=save_name)
			#remove empty columns
			for i in df_err.columns:
				if len(df_err[df_err[i].notna()]) == 0: df_err.drop(i,axis=1,inplace=True)
			if len(df_err) !=0:
				df_err = self._sort_resetIndex_save(df=df_err, bylist=['TEMP','SUPPLY','CHIP#'], save_name=save_name[:-4]+'_error_list.csv')
				print 'SAVED Data & Error List to path: %s'%(save_name)

		return df, df_err

	def _group_data(self, df, bylist):
		return df.groupby(bylist)

	def _slt_data(self, df, column_name, inlist):
		'''choose only data satisfies certain requirement

		:param column_name: name of column used as screen condition
		:param inlist:      pass a list of parameters meets data selection requirement
		'''
		return df[df[column_name].isin(inlist)]

	def _find_nonull_data_row(self, df, supply, temp, chip_num):
		'''locate data row based on given chip#, supply & temperature condition
		will return the row of data with lowest number of empty columns

		'''
		df_g = df.groupby(['SUPPLY','TEMP'])
		df_u = df_g.get_group((supply, temp))
		df_c = df_u[df_u['CHIP#'] == chip_num]
		if len(df_c) == 0:
			df_c = df_u[df_u['CHIP#'] == '%s'%chip_num]
		null_l  = []
		for i in df_c.index:
			_t_num = df_c.loc[i].isnull().values.tolist().count(True)
			null_l.append((_t_num, i))
		#sort data based on number of empty data points found
		null_l.sort()
		i_use = null_l[0][1]
		return df.loc[i]

	def add_serial_column(self, data_file, chip_type='marlin3', add_ver=False, corner_part=False, 
		sort_data=True, save_name=None):
		'''replace CHIP_NUM column with real chip_num according to MAC value read

		:param data_file: data in pandas dataframe format
		:param chip_type: choose from 'chip722', 'marlin3', 'marlin3s'
		:param en_ver:    add version column as well if True
		'''
		df = data_file
		chip_type = chip_type.lower()

		if not add_ver:
			#rwk stands for rework
			num_rwk = self._serial_chip_num_by_MAC(df=df, chip_type=chip_type)
			df = self._add_column(df=df, column_name='CHIP#', position=0, new_values= num_rwk)

		elif not corner_part:
			num_rwk, ver_rwk = self._serial_chip_num_by_MAC(df=df, chip_type=chip_type, en_ver=add_ver)
			df = self._add_column(df=df, column_name='CHIP#', position=0, new_values= num_rwk)
			df = self._add_column(df=df, column_name='TYPE', position=1, new_values= ver_rwk)

		else:
			num_rwk, ver_rwk = self._serial_chip_num_by_MAC(df=df, chip_type=chip_type, en_ver=add_ver)
			ver_l, cnr_l = [],[]
			for i in ver_rwk:
				if i == 'Nothing MATCH':
					ver_l.append(i)
					cnr_l.append(i)
				else:
					ver_l.append(i.split('_')[2])
					cnr_l.append(i.split('_')[1])

			df = self._add_column(df=df, column_name='CHIP#', position=0, new_values= num_rwk)
			df = self._add_column(df=df, column_name='TYPE', position=1, new_values= ver_l)
			df = self._add_column(df=df, column_name='CORNER', position=2, new_values= cnr_l)

		if sort_data:
			df = self._sort_resetIndex_save(df=df, bylist=['CHIP#'], save_name=save_name)

		return df

	def clean_measurement_error(self, df, save_name):
		'''wash columns to remove out of range data due to measurement error and 
		save it to be csv file for identification.
		- some of the columns are not checked, see self.column_str_not_check
		- two actions executed below
			- will remove out of range data
			- will report error string if found in data column 
		
		:param board_type: 'socket', 'mb1', 'mb2'
		'''
		#clean voltages
		col_to_wash = ['VREF_1V','VREF_1V_0','VREF_1V_1','VREF_1V_2','VREF_1V_3']
		uplim_l     = [1.1]*len(col_to_wash)
		dnlim_l     = [0.8]*len(col_to_wash)
		ctw_0 = ['RTC_LDO','DIG_LDO','SAR1_REF','SAR2_REF','VCM']
		ull_0 = [1.3]*len(ctw_0)
		dll_0 = [0.9]*(len(ctw_0)-1)+[0.7]
		ctw_1 = ['V_LSLP_0_1(V)', 'V_LSLP_0_5(V)', 'V_LSLP_3_0(V)', 'V_LSLP_6_0(V)', 'V_LSLP_7_0(V)']
		ull_1 = [1.1, 1.3, 1.0, 0.8, 0.8]
		dll_1 = [0.7, 0.9, 0.7, 0.6, 0.6]

		col_to_wash += ctw_0 + ctw_1
		uplim_l     += ull_0 + ull_1
		dnlim_l     += dll_0 + dll_1

		#clean currents
		ctw_s = ['I_EN0(uA)','I_EN10(uA)',
				 'I_LSLP_WFPD0(mA)', 'I_LSLP_WFPD1(mA)', 'I_LSLP_WF_D(mA)',
				 'I_LSLP_0_1(mA)', 'I_LSLP_0_5(mA)', 'I_LSLP_3_0(mA)', 'I_LSLP_6_0(mA)', 'I_LSLP_7_0(mA)',
				 'I_DSLP(uA)']
		ull_s = [1e7]*len(ctw_s)
		dll_s = [0]*len(ctw_s)
		col_to_wash += ctw_s
		uplim_l     += ull_s
		dnlim_l     += dll_s

		ctw_dict = dict(zip(col_to_wash, zip(uplim_l, dnlim_l)))

		ctw_use = list(set(col_to_wash) & set(df.columns))
		upl_use, dnl_use = [],[]
		for i in ctw_use:
			upl_use.append(ctw_dict[i][0])
			dnl_use.append(ctw_dict[i][1])

		df, df_err = self._data_wash(df=df, col_list=ctw_use, uplimit=upl_use, dnlimit=dnl_use,
			replacement=None, save_name= save_name)
		return df, df_err

	def rd_raw(self, save_dir, chip_ver='MARLIN3S', data_path =None, board_type='socket'):
		''' script to process raw marlin3s(skew lot) data

		:param save_dir:   complete directory path for data file to be saved
		:param chip_type: choose from 'chip722', 'marlin3', 'marlin3s'
		:param data_path:  default ONE PIECE directory will be used if no data_path given
		:param board_type: 'socket', 'mb1', 'mb2'
		'''
		chip_ver  = chip_ver.upper()
		op_path = self.chip_addr_dict[chip_ver.lower()] + OP_DATA_YARD 
		if board_type == 'socket':
			op_path    += '/%s'%board_type.capitalize()
			board_name = 'SCKT' 
		else:
			op_path    += '/MultiBoard/%s'%board_type.upper()
			board_name = 'MB_%s'%board_type[-1]

		if data_path == None: data_path = op_path 

		td = time.gmtime()
		tm_stamp = '%s_%s_%s'%(td.tm_year,td.tm_mon,td.tm_mday)
		file_name = '%s_%s_washed'%(chip_ver,board_type)
		save_name = save_dir + '/' + file_name + '_'+ tm_stamp +'.csv'

		#read in data files
		raw_rd = self._rd_file(dir_name= data_path)

		#rename inappropriate columns
		col_rename_dict = self.column_rename_dict['%s_%s'%(chip_ver.lower(),board_name.split('_')[0].lower())]
		raw_rd = self._rename_column(df=raw_rd, col_dict=col_rename_dict)
		
		if board_type == 'socket':
			#add temperature column
			_t = [25]*len(raw_rd)
			raw_rd = self._add_column(df=raw_rd, column_name='TEMP', position=0, new_values=_t)
		else:
			#add location# for multiboard data set
			raw_rd = self._add_column(df=raw_rd, column_name='LOC#', position=0, new_values=raw_rd['CHIP#'])
			if chip_ver == 'CHIP722':
				raw_rd['LOC#'] = raw_rd['LOC#'].apply(lambda x:int(x[1:]))
				

		#wash supply column
		if chip_ver == 'MARLIN3':
			raw_rd['SUPPLY'] = raw_rd['SUPPLY'].apply(lambda x:float(x.split('_')[0]))
		elif chip_ver == 'CHIP722':
			if board_type == 'socket':
				raw_rd = self._add_column(df=raw_rd, column_name='SUPPLY', position=0, new_values=[3.3]*len(raw_rd))
			else:
				raw_rd['SUPPLY'] = raw_rd['SUPPLY'].apply(lambda x:float(x[:-1]))


		_s = [board_name]*len(raw_rd)
		_n = [chip_ver]*len(raw_rd)
		raw_rd = self._add_column(df=raw_rd, column_name='BOARD', position=0, new_values=_s)
		raw_rd = self._add_column(df=raw_rd, column_name='NAME', position=0, new_values=_n)

		#serialize parts
		save_name_raw = (save_dir + '/' + file_name + '_raw_'+ tm_stamp +'.csv') if chip_ver == 'CHIP722' else save_name

		corner_part = True if chip_ver.lower() in self.chip_corner_list else False
		raw_rd = self.add_serial_column(data_file=raw_rd, chip_type=chip_ver, add_ver=True,
			corner_part=corner_part, sort_data=True, save_name=save_name_raw)

		#wash out of range data
		raw_rd, df_err = self.clean_measurement_error(df=raw_rd, save_name=save_name)

		#save data by supply
		raw_rd_g = self._group_data(raw_rd, ['SUPPLY'])
		for i_s in raw_rd_g.groups.keys():
			save_name = save_dir + '/' + file_name + '_%sV_'%(i_s)+ tm_stamp + '.csv'
			raw_rd_g.get_group(i_s).to_csv(save_name,index=False)

		#rearrange data as default setup
		raw_rd = self._arrange_data_column_default(df=raw_rd, for_merge=True)
		#save processed file for merging all together
		save_name = save_dir + '/' + file_name + '_for_merge_' + tm_stamp +'.csv'
		raw_rd = self._sort_resetIndex_save(df=raw_rd, bylist=['TEMP','SUPPLY','CHIP#'], save_name = save_name)
		return

	def pick_from_another_data(self, df_path, data_path, supply, temp, save_dir, merge_save=False):
		'''based on given dataframe, pick data from given file

		:param df_path:    directory & data file name who includes chip# information for picking
		:param data_path:  directory & data file name to read data for picking
		:param supply:     specify supply voltage
		:param temp:       specify temperature 
		:param save_dir:   directory to save generated dataframe
		:param merge_save: if True, will merge picked data into given dataframe and saved to save_dir
		'''
		df = pd.read_csv(df_path)          #file to pick data from 
		df_origin = pd.read_csv(data_path) #file to read chip#

		df_pick   = pd.DataFrame()
		#chip number list
		cnl = df_origin['CHIP#'].drop_duplicates().tolist()
		for i in cnl:
			df_pick = df_pick.append(self._find_nonull_data_row(df=df, supply=supply, temp=temp, chip_num=i))

		df_pick = self._rearrange_column(df=df_pick, col_new_list=df_origin.columns)
		#save original data file w/ picked data merged
		if merge_save:	
			raw_rd = df_origin.append(df_pick)
			self._sort_resetIndex_save(df=raw_rd, bylist=['TEMP','SUPPLY','CHIP#'], save_name = save_dir+'/picked_data.csv')

		return df_pick

#to be polished
	def data_adc_merge(self,data):
		'''merge adc vref data into same file

		:brief:
			- adc data file example:
				example_path/plot_adc/CHIP722_sar1&2_stepsize1mV_T40.csv & sar_ref/
		'''
		df_temp = df_125
		vref_l=[]
		temp = df_temp.get('TEMP')
		supl = df_temp.get('SUPPLY')
		chip_num = df_temp.get('CHIP#')
		adc_num = df_temp.get('ADC')
		for i in range(df_temp.count()['CHIP#']):
			vref_l.append(df[(df['TEMP']==temp[i])&(df['SUPPLY']==supl[i])&(df['CHIP#']==chip_num[i])]['SAR%d_REF'%(adc_num[i])].values[0])
		df_temp.insert(loc=6,column='VREF',value=vref_l)
		df_temp.to_csv('CHIP722_SAR1&2_StepSize1mV_T{}_wVREF.csv'.format(temp[0]))


