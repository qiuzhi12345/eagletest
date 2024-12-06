import os as os
import pandas as pd
from dataprocess.volume._data_address import *

class macLookUp(object):
	'''script used to find part# based on given MAC address
		
	'''
	def __init__(self):
		pass

	def wc_chip722_800(self, inpt_mac='', en_ver=False, en_print=True):
		'''script used to find chip # using MAC address, only suitable for 800pc chip722

		   wc stands for which chip

			- needs at least last four digits for inpt_mac
		'''
		macdir   = OP_CHIP722 + '/MAC_origin/'

		'''import mac files'''
		mac_file_l = [fn for fn in os.listdir(macdir) if fn[-11:-4]!='_report' and fn[-4:]=='.csv']
		for i in mac_file_l:
			if i.find('_vA_') >0: mac_a = pd.read_csv(macdir+'/'+i)
			else:                 mac_b = pd.read_csv(macdir+'/'+i)
		
		def loop_for_mac(df_mac, inpt_val= inpt_mac):
			'''look for requested MAC address if exists'''
			found_num = found_ver = found_mac = found_row = 'Nothing MATCH'
			for val in df_mac['MAC']:
				if type(inpt_mac) == float: break
				if inpt_mac[-4:].upper() == val[-4:]:
					found_mac = val
					found_ver = df_mac[df_mac['MAC']==val]['chip_ver'].values[0]
					found_num = df_mac[df_mac['MAC']==val]['chip_num'].values[0]
					break			
			return found_num, found_ver, found_mac, found_row

		'''go through two mac files'''
		found_num, found_ver, found_mac, found_row = loop_for_mac(mac_a, inpt_mac)
		if isinstance(found_num,str):
			found_num, found_ver, found_mac, found_row = loop_for_mac(mac_b, inpt_mac)

		if not isinstance(found_num,str):
			if found_num > (265 or 665):   found_row = 3 
			elif found_num > (132 or 532): found_row = 2
			else:                          found_row = 1
		
		if en_print:
			print('NUM #%s\nVER %s\nMAC %s\nROW %s'%(found_num,found_ver,found_mac,found_row))
		if en_ver: 
			return found_num, found_ver
		else:
			return found_num

	def wc_marlin3_400(self, inpt_mac='', en_ver=False, en_print=True):
		'''script used to find chip # using MAC address, only suitable for 400pc chip722m1/marlin3

		   wc stands for which chip

			- needs at least last four digits for inpt_mac
		'''
		macdir   = OP_MARLIN3 + '/MAC_origin/'

		found_num = found_ver = found_mac = found_row = 'Nothing MATCH'

		'''import mac files'''
		mac_file_l = [fn for fn in os.listdir(macdir) if fn[-11:-4]!='_report' and fn[-4:]=='.csv']
		for i in mac_file_l: mac_b = pd.read_csv(macdir+'/'+i)

		for value_b in mac_b.MAC:
			if inpt_mac[-4:].upper() == value_b[-4:]:
				found_mac = value_b
				found_ver = mac_b[mac_b['MAC']==value_b]['chip_ver'].values[0]
				found_num = mac_b[mac_b['MAC']==value_b]['chip_num'].values[0]
				if found_num < 200: 
					found_ver += '2'
				else:
					found_ver += '3'
				break

		if en_print:
			print('NUM #%s\nVER %s\nMAC %s\n'%(found_num,found_ver,found_mac))
		if en_ver: 
			return found_num, found_ver
		else:
			return found_num

	def wc_marlin3s_600(self, inpt_mac='', en_ver=False, en_print=True):
		'''script used to find chip # using MAC address, only suitable for 600pc marlin3_skew_lot
		   
		   wc stands for which chip

			- needs at least last four digits for inpt_mac
		'''
		macdir   = OP_MARLIN3S + '/MAC_origin/'

		if type(inpt_mac) != str: inpt_mac = str(inpt_mac)
		found_num = found_ver = found_mac = found_row = 'Nothing MATCH'

		'''import mac files'''
		mac_b = pd.DataFrame()
		mac_file_l = [fn for fn in os.listdir(macdir) if fn[-10:]== ('100pcs.csv')]
		for i in mac_file_l: 
			mac_t = pd.read_csv(macdir+'/'+i)

			col_l = mac_t.columns.tolist()
			col_l.insert(len(col_l),'CORNER')
			mac_t = mac_t.reindex(columns=col_l)
			mac_t['CORNER'] = ['%s'%i[-16:-11]]*len(mac_t)

			mac_b = mac_b.append(mac_t)

		for value_b in mac_b.MAC:
			if inpt_mac[-4:].upper() == value_b[-4:]:
				found_mac = value_b
				found_ver = mac_b[mac_b['MAC']==value_b]['chip_ver'].values[0]
				found_num = mac_b[mac_b['MAC']==value_b]['chip_num'].values[0]
				found_ver += '_%s'%mac_b[mac_b['MAC']==value_b]['CORNER'].values[0]
				break

		if en_print:
			print('NUM #%s\nVER %s\nMAC %s\n'%(found_num,found_ver,found_mac))
		if en_ver: 
			return found_num, found_ver
		else:
			return found_num

	def read_mac_table_chip722_800(self):
		'''generate two pandas dataframe for chip type A & B '''
		macdir   = self.chip722dir + '/MAC_origin/' 
		# macdir     = '/home/test/Documents/ZBL/chip722/800pcs/MAC/mac_800pcs'
		mac_file_l = [fn for fn in os.listdir(macdir) if fn[-11:-4]!='_report']
		for i in mac_file_l:
			if i.find('_vA_') >0:   mac_a = pd.read_csv(macdir+'/'+i)
			elif i.find('_vB_')>0:  mac_b = pd.read_csv(macdir+'/'+i)
		return mac_a, mac_b