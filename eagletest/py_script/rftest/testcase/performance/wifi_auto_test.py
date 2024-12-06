
from rftest.rflib.wifi_lib import WIFILIB
from hal.common import MEM
from rftest.rflib import rfglobal
from rftest.rflib import wifi_instrum
import win32com
import win32com.client
from win32com.client import Dispatch, constants, gencache
from docx import Document
import re
import baselib.test_channel.channel as chn
from baselib.loglib.log_lib import *
from baselib.plot import *
from baselib.instrument import *
import numpy as np
import scipy
from math import *
import time
from baselib.test_channel import *
from baselib.test_channel import com
from baselib.instrument.tester_serv import *
import sys
from baselib.instrument import *
from baselib.instrument import tester
import xlwt
import xlrd
import os
import docx
import csv
import pylab
import matplotlib.pyplot as plt
from math import *
from shutil import copy
from rftest.rflib.csv_report import csvreport


sens_dict = rfglobal.sens_dict
rate_bps_dict = rfglobal.rate_bps_dict
rx_maxlevel_dict = rfglobal.rx_maxlevel_dict

table_rate_row_dic = {
	'11m':5,
	'5.5m':6,       ## sensitivity of every rate's word cell location
	'2m':7,
	'1m':8,
    '54m':5,
	'48m':6,
	'36m':7,
	'24m':8,
	'18m':9,
	'12m':10,
	'9m':11,
	'6m':12,
	'mcs7':5,
	'mcs6':6,
	'mcs5':7,
	'mcs4':8,
	'mcs3':9,
	'mcs2':10,
	'mcs1':11,
	'mcs0':12,
	'mcs7_40':5,
	'mcs6_40':6,
	'mcs5_40':7,
	'mcs4_40':8,
	'mcs3_40':9,
	'mcs2_40':10,
	'mcs1_40':11,
	'mcs0_40':12}


table_chan_col_20M_dic = {
    1 : 2,
    2 : 3,
    3 : 4,
    4 : 5,
    5 : 6,
    6 : 7,
    7 : 8,
    8 : 9,
    9 : 10,
    10 : 11,
    11 : 12,
    12 : 13,
    13 : 14,
    14 : 15
}

table_chan_col_40M_dic = {
    3 : 2,
    4 : 3,
    5 : 4,
    6 : 5,
    7 : 6,
    8 : 7,
    9 : 8
}


rx_sensitivity_crt = {
    '11m' : -85,
    '5.5m' : -88,
    '2m' : -91,
    '1m' : -94,
    '54m' : -71,
    '48m' : -72,
    '36m' : -76,
    '24m' : -80,
    '18m' : -83,
    '12m' : -85,
    '9m'  : -87,
    '6m'  : -88,
    'mcs7' : -70,
    'mcs6' : -71,
    'mcs5' : -72,
    'mcs4' : -76,
    'mcs3' : -80,
    'mcs2' : -83,
    'mcs1' : -85,
    'mcs0' : -88,
    'mcs7_40' : -67,
    'mcs6_40' : -68,
    'mcs5_40' : -69,
    'mcs4_40' : -73,
    'mcs3_40' : -77,
    'mcs2_40' : -80,
    'mcs1_40' : -82,
    'mcs0_40' : -85
}

detailed_word_table_vs_rate_dic = {
    "11m":4,
    "1m":5,
    "2m":6,
    "5.5m":7,     ## TX_PWR_EVM table number_details
    "54m":8,
    "6m":9,
    "9m":10,
    "12m":11,
    "18m":12,
    "24m":13,
    "36m":14,
    "48m":15,
    "mcs7":16,
    "mcs0":17,
    "mcs1":18,
    "mcs2":19,
    "mcs3":20,
    "mcs4":21,
    "mcs5":22,
    "mcs6":23,
    "mcs7_40":24,
    "mcs0_40":25,
    "mcs1_40":26,
    "mcs2_40":27,
    "mcs3_40":28,
    "mcs4_40":29,
    "mcs5_40":30,
    "mcs6_40":31,

}
detail_mask_flatness_rate_vs_table_dic={
    '1m': 32,
    '6m': 33,
    'mcs0': 34,
    'mcs0_40' : 35,
    '54m': 36,
    'mcs7':37,
    'mcs7_40':38
}

detailed_rx_sensitivity_word_table_vs_rate_dic = {
    "1m": 72,            # Table 48
    "2m": 72,            # Table 48
    "5.5m": 72,            # Table 48
    "11m": 72,            # Table 48
    "6m": 73,            # Table 35
    "9m": 73,            # Table 35
    "12m": 73,            # Table 35
    "18m": 73,            # Table 35
    "24m": 73,            # Table 35
    "36m": 73,            # Table 35
    "48m": 73,            # Table 35
    "54m": 73,            # Table 35
    "mcs0": 74,         # Table 36
    "mcs1": 74,         # Table 36
    "mcs2": 74,         # Table 36
    "mcs3": 74,         # Table 36
    "mcs4": 74,         # Table 36
    "mcs5": 74,         # Table 36
    "mcs6": 74,         # Table 36
    "mcs7": 74,         # Table 36
    "mcs0_40": 75,         # Table 37
    "mcs1_40": 75,         # Table 37
    "mcs2_40": 75,         # Table 37
    "mcs3_40": 75,         # Table 37
    "mcs4_40": 75,         # Table 37
    "mcs5_40": 75,         # Table 37
    "mcs6_40": 75,         # Table 37
    "mcs7_40": 75
}


detailed_rx_max_word_table_vs_rate_dic = {
    "1m": 68,            # Table 30
    "2m": 68,            # Table 30
    "5.5m": 68,            # Table 30
    "11m": 68,            # Table 30
    "6m": 69,            # Table 31
    "9m": 69,            # Table 31
    "12m": 69,            # Table 31
    "18m": 69,            # Table 31
    "24m": 69,            # Table 31
    "36m": 69,            # Table 31
    "48m": 69,            # Table 31
    "54m": 69,            # Table 31
    "mcs0": 70,         # Table 32
    "mcs1": 70,         # Table 32
    "mcs2": 70,         # Table 32
    "mcs3": 70,         # Table 32
    "mcs4": 70,         # Table 32
    "mcs5": 70,         # Table 32
    "mcs6": 70,         # Table 32
    "mcs7": 70,         # Table 32
    "mcs0_40": 71,         # Table 33
    "mcs1_40": 71,         # Table 33
    "mcs2_40": 71,         # Table 33
    "mcs3_40": 71,         # Table 33
    "mcs4_40": 71,         # Table 33
    "mcs5_40": 71,         # Table 33
    "mcs6_40": 71,         # Table 33
    "mcs7_40": 71
}

detailed_TX_word_table_excel_sheet_dic = {
    4:"TX-11Mbps",
    5:"TX-1Mbps",
    6:"TX-2Mbps",
    7:"TX-5.5Mbps",
    8:"TX-54Mbps",
    9:"TX-6Mbps",
    10:"TX-9Mbps",
    11:"TX-12Mbps",
    12:"TX-18Mbps",
    13:"TX-24Mbps",
    14:"TX-36Mbps",
    15:"TX-48Mbps",
    16:"TX-mcs7_20",
    17:"TX-mcs0_20",
    18:"TX-mcs1_20",
    19:"TX-mcs2_20",
    20:"TX-mcs3_20",
    21:"TX-mcs4_20",
    22:"TX-mcs5_20",
    23:"TX-mcs6_20",
    24:"TX-mcs7_40",
    25:"TX-mcs0_40",
    26:"TX-mcs1_40",
    27:"TX-mcs2_40",
    28:"TX-mcs3_40",
    29:"TX-mcs4_40",
    30:"TX-mcs5_40",
    31:"TX-mcs6_40"
}

Test_case_word_table_detailed_dic = {
    "TX_11m": 4,                # Table 6
    "TX_1m": 5,                 # Table 7
    "TX_2m": 6,                 # Table 7
    "TX_5.5m": 7,                 # Table 7
    "TX_54m": 8,                # Table 8
    "TX_6m": 9,                 # Table 9
    "TX_9m": 10,                 # Table 9
    "TX_12m": 11,                 # Table 9
    "TX_18m": 12,                 # Table 9
    "TX_24m": 13,                 # Table 9
    "TX_36m": 14,                 # Table 9
    "TX_48m": 15,                 # Table 9
    "TX_mcs7": 16,               # Table 10
    "TX_mcs0": 17,              # Table 11
    "TX_mcs1": 18,              # Table 11
    "TX_mcs2": 19,              # Table 11
    "TX_mcs3": 20,              # Table 11
    "TX_mcs4": 21,              # Table 11
    "TX_mcs5": 22,              # Table 11
    "TX_mcs6": 23,              # Table 11
    "TX_mcs7_40": 24,           # Table 12
    "TX_mcs0_40": 25,           # Table 13
    "TX_mcs1_40": 26,           # Table 13
    "TX_mcs2_40": 27,           # Table 13
    "TX_mcs3_40": 28,           # Table 13
    "TX_mcs4_40": 29,           # Table 13
    "TX_mcs5_40": 30,           # Table 13
    "TX_mcs6_40": 31,           # Table 13
    "Mask_margin_1m": 32,       # Table 18
    "Mask_margin_6m": 33,       # Table 19
    "Mask_margin_mcs0": 34,     # Table 20
    "Mask_margin_mcs0_40": 35,  # Table 21
    "Flatness_54m": 36,         # Table 22
    "Flatness_mcs7": 37,        # Table 23
    "Flatness_mcs7_40": 38,     # Table 40
    "TX_Ramp": 39,              # Table 41
    "RX_DR_1m": 40,            # Table 26
    "RX_DR_2m": 41,            # Table 26
    "RX_DR_5.5m": 42,            # Table 26
    "RX_DR_11m": 43,            # Table 26
    "RX_DR_6m": 44,            # Table 27
    "RX_DR_9m": 45,            # Table 27
    "RX_DR_12m": 46,            # Table 27
    "RX_DR_18m": 47,            # Table 27
    "RX_DR_24m": 48,            # Table 27
    "RX_DR_36m": 49,            # Table 27
    "RX_DR_48m": 50,            # Table 27
    "RX_DR_54m": 51,            # Table 27
    "RX_DR_mcs0": 52,         # Table 28
    "RX_DR_mcs1": 53,         # Table 28
    "RX_DR_mcs2": 54,         # Table 28
    "RX_DR_mcs3": 55,         # Table 28
    "RX_DR_mcs4": 56,         # Table 28
    "RX_DR_mcs5": 57,         # Table 28
    "RX_DR_mcs6": 58,         # Table 28
    "RX_DR_mcs7": 59,         # Table 28
    "RX_DR_mcs0_40": 60,         # Table 29
    "RX_DR_mcs1_40": 61,         # Table 29
    "RX_DR_mcs2_40": 62,         # Table 29
    "RX_DR_mcs3_40": 63,         # Table 29
    "RX_DR_mcs4_40": 64,         # Table 29
    "RX_DR_mcs5_40": 65,         # Table 29
    "RX_DR_mcs6_40": 66,         # Table 29
    "RX_DR_mcs7_40": 67,         # Table 29
    "RX_Max_1m": 68,            # Table 30
    "RX_Max_2m": 68,            # Table 30
    "RX_Max_5.5m": 68,            # Table 30
    "RX_Max_11m": 68,            # Table 30
    "RX_Max_6m": 69,            # Table 31
    "RX_Max_9m": 69,            # Table 31
    "RX_Max_12m": 69,            # Table 31
    "RX_Max_18m": 69,            # Table 31
    "RX_Max_24m": 69,            # Table 31
    "RX_Max_36m": 69,            # Table 31
    "RX_Max_48m": 69,            # Table 31
    "RX_Max_54m": 69,            # Table 31
    "RX_Max_mcs0": 70,         # Table 32
    "RX_Max_mcs1": 70,         # Table 32
    "RX_Max_mcs2": 70,         # Table 32
    "RX_Max_mcs3": 70,         # Table 32
    "RX_Max_mcs4": 70,         # Table 32
    "RX_Max_mcs5": 70,         # Table 32
    "RX_Max_mcs6": 70,         # Table 32
    "RX_Max_mcs7": 70,         # Table 32
    "RX_Max_mcs0_40": 71,         # Table 33
    "RX_Max_mcs1_40": 71,         # Table 33
    "RX_Max_mcs2_40": 71,         # Table 33
    "RX_Max_mcs3_40": 71,         # Table 33
    "RX_Max_mcs4_40": 71,         # Table 33
    "RX_Max_mcs5_40": 71,         # Table 33
    "RX_Max_mcs6_40": 71,         # Table 33
    "RX_Max_mcs7_40": 71,         # Table 33
    "RX_Sens_1m": 72,            # Table 48
    "RX_Sens_2m": 72,            # Table 48
    "RX_Sens_5.5m": 72,            # Table 48
    "RX_Sens_11m": 72,            # Table 48
    "RX_Sens_6m": 73,            # Table 35
    "RX_Sens_9m": 73,            # Table 35
    "RX_Sens_12m": 73,            # Table 35
    "RX_Sens_18m": 73,            # Table 35
    "RX_Sens_24m": 73,            # Table 35
    "RX_Sens_36m": 73,            # Table 35
    "RX_Sens_48m": 73,            # Table 35
    "RX_Sens_54m": 73,            # Table 35
    "RX_Sens_mcs0": 74,         # Table 36
    "RX_Sens_mcs1": 74,         # Table 36
    "RX_Sens_mcs2": 74,         # Table 36
    "RX_Sens_mcs3": 74,         # Table 36
    "RX_Sens_mcs4": 74,         # Table 36
    "RX_Sens_mcs5": 74,         # Table 36
    "RX_Sens_mcs6": 74,         # Table 36
    "RX_Sens_mcs7": 74,         # Table 36
    "RX_Sens_mcs0_40": 75,         # Table 37
    "RX_Sens_mcs1_40": 75,         # Table 37
    "RX_Sens_mcs2_40": 75,         # Table 37
    "RX_Sens_mcs3_40": 75,         # Table 37
    "RX_Sens_mcs4_40": 75,         # Table 37
    "RX_Sens_mcs5_40": 75,         # Table 37
    "RX_Sens_mcs6_40": 75,         # Table 37
    "RX_Sens_mcs7_40": 75         # Table 37
}

Test_case_data_rate_dic = {
    "TX_11m": ['11m'],                # Table 6
    "TX_1m": ['1m'],                 # Table 7
    "TX_2m": ['2m'],                 # Table 7
    "TX_5.5m": ['5.5m'],                 # Table 7
    "TX_54m": ['54m'],                # Table 8
    "TX_6m": ['6m'],                 # Table 9
    "TX_9m": ['9m'],                 # Table 9
    "TX_12m": ['12m'],                 # Table 9
    "TX_18m": ['18m'],                 # Table 9
    "TX_24m": ['24m'],                 # Table 9
    "TX_36m": ['36m'],                 # Table 9
    "TX_48m": ['48m'],                 # Table 9
    "TX_mcs7": ['mcs7'],               # Table 10
    "TX_mcs0": ['mcs0'],              # Table 11
    "TX_mcs1": ['mcs1'],              # Table 11
    "TX_mcs2": ['mcs2'],              # Table 11
    "TX_mcs3": ['mcs3'],              # Table 11
    "TX_mcs4": ['mcs4'],              # Table 11
    "TX_mcs5": ['mcs5'],              # Table 11
    "TX_mcs6": ['mcs6'],              # Table 11
    "TX_mcs7_40": ['mcs7_40'],           # Table 12
    "TX_mcs0_40": ['mcs0_40'],           # Table 13
    "TX_mcs1_40": ['mcs1_40'],           # Table 13
    "TX_mcs2_40": ['mcs2_40'],           # Table 13
    "TX_mcs3_40": ['mcs3_40'],           # Table 13
    "TX_mcs4_40": ['mcs4_40'],           # Table 13
    "TX_mcs5_40": ['mcs5_40'],           # Table 13
    "TX_mcs6_40": ['mcs6_40'],           # Table 13
    'Mask_margin_1m' : ['1m'],
    'Mask_margin_6m' : ['6m'],
    'Mask_margin_mcs0' : ['mcs0'],
    'Mask_margin_mcs0_40' : ['mcs0_40'],
    'Flatness_54m' : ['54m'],
    'Flatness_mcs7' : ['mcs7'],
    'Flatness_mcs7_40' : ['mcs7_40'],
    "RX_DR_1m": ['1m'],            # Table 26
    "RX_DR_2m": ['2m'],            # Table 26
    "RX_DR_5.5m": ['5.5m'],            # Table 26
    "RX_DR_11m": ['11m'],            # Table 26
    "RX_DR_6m": ['6m'],            # Table 27
    "RX_DR_9m": ['9m'],            # Table 27
    "RX_DR_12m": ['12m'],            # Table 27
    "RX_DR_18m": ['18m'],            # Table 27
    "RX_DR_24m": ['24m'],            # Table 27
    "RX_DR_36m": ['36m'],            # Table 27
    "RX_DR_48m": ['48m'],            # Table 27
    "RX_DR_54m": ['54m'],            # Table 27
    "RX_DR_mcs0": ['mcs0'],         # Table 28
    "RX_DR_mcs1": ['mcs1'],         # Table 28
    "RX_DR_mcs2": ['mcs2'],         # Table 28
    "RX_DR_mcs3": ['mcs3'],         # Table 28
    "RX_DR_mcs4": ['mcs4'],         # Table 28
    "RX_DR_mcs5": ['mcs5'],         # Table 28
    "RX_DR_mcs6": ['mcs6'],         # Table 28
    "RX_DR_mcs7": ['mcs7'],         # Table 28
    "RX_DR_mcs0_40": ['mcs0_40'],         # Table 29
    "RX_DR_mcs1_40": ['mcs1_40'],         # Table 29
    "RX_DR_mcs2_40": ['mcs2_40'],         # Table 29
    "RX_DR_mcs3_40": ['mcs3_40'],         # Table 29
    "RX_DR_mcs4_40": ['mcs4_40'],         # Table 29
    "RX_DR_mcs5_40": ['mcs5_40'],         # Table 29
    "RX_DR_mcs6_40": ['mcs6_40'],         # Table 29
    "RX_DR_mcs7_40": ['mcs7_40'],         # Table 29
    "RX_Max_1m": ['1m'],            # Table 30
    "RX_Max_2m": ['2m'],            # Table 30
    "RX_Max_5.5m": ['5.5m'],            # Table 30
    "RX_Max_11m": ['11m'],            # Table 30
    "RX_Max_6m": ['6m'],            # Table 31
    "RX_Max_9m": ['9m'],            # Table 31
    "RX_Max_12m": ['12m'],            # Table 31
    "RX_Max_18m": ['18m'],            # Table 31
    "RX_Max_24m": ['24m'],            # Table 31
    "RX_Max_36m": ['36m'],            # Table 31
    "RX_Max_48m": ['48m'],            # Table 31
    "RX_Max_54m": ['54m'],            # Table 31
    "RX_Max_mcs0": ['mcs0'],         # Table 32
    "RX_Max_mcs1": ['mcs1'],         # Table 32
    "RX_Max_mcs2": ['mcs2'],         # Table 32
    "RX_Max_mcs3": ['mcs3'],         # Table 32
    "RX_Max_mcs4": ['mcs4'],         # Table 32
    "RX_Max_mcs5": ['mcs5'],         # Table 32
    "RX_Max_mcs6": ['mcs6'],         # Table 32
    "RX_Max_mcs7": ['mcs7'],         # Table 32
    "RX_Max_mcs0_40": ['mcs0_40'],         # Table 33
    "RX_Max_mcs1_40": ['mcs1_40'],         # Table 33
    "RX_Max_mcs2_40": ['mcs2_40'],         # Table 33
    "RX_Max_mcs3_40": ['mcs3_40'],         # Table 33
    "RX_Max_mcs4_40": ['mcs4_40'],         # Table 33
    "RX_Max_mcs5_40": ['mcs5_40'],         # Table 33
    "RX_Max_mcs6_40": ['mcs6_40'],         # Table 33
    "RX_Max_mcs7_40": ['mcs7_40'],         # Table 33
    "RX_Sens_1m": ['1m'],            # Table 34
    "RX_Sens_2m": ['2m'],            # Table 34
    "RX_Sens_5.5m": ['5.5m'],            # Table 34
    "RX_Sens_11m": ['11m'],            # Table 34
    "RX_Sens_6m": ['6m'],            # Table 35
    "RX_Sens_9m": ['9m'],            # Table 35
    "RX_Sens_12m": ['12m'],            # Table 35
    "RX_Sens_18m": ['18m'],            # Table 35
    "RX_Sens_24m": ['24m'],            # Table 35
    "RX_Sens_36m": ['36m'],            # Table 35
    "RX_Sens_48m": ['48m'],            # Table 35
    "RX_Sens_54m": ['54m'],            # Table 35
    "RX_Sens_mcs0": ['mcs0'],         # Table 36
    "RX_Sens_mcs1": ['mcs1'],         # Table 36
    "RX_Sens_mcs2": ['mcs2'],         # Table 36
    "RX_Sens_mcs3": ['mcs3'],         # Table 36
    "RX_Sens_mcs4": ['mcs4'],         # Table 36
    "RX_Sens_mcs5": ['mcs5'],         # Table 36
    "RX_Sens_mcs6": ['mcs6'],         # Table 36
    "RX_Sens_mcs7": ['mcs7'],         # Table 36
    "RX_Sens_mcs0_40": ['mcs0_40'],         # Table 37
    "RX_Sens_mcs1_40": ['mcs1_40'],         # Table 37
    "RX_Sens_mcs2_40": ['mcs2_40'],         # Table 37
    "RX_Sens_mcs3_40": ['mcs3_40'],         # Table 37
    "RX_Sens_mcs4_40": ['mcs4_40'],         # Table 37
    "RX_Sens_mcs5_40": ['mcs5_40'],         # Table 37
    "RX_Sens_mcs6_40": ['mcs6_40'],         # Table 37
    "RX_Sens_mcs7_40": ['mcs7_40'],         # Table 37
}


detailed_word_table_index_vs_word_sections = {
    4:4,     #Table 6 vs section 6
    5:5,     #Table 7 vs section 7
    6:6,     #Table 8 vs section 8
    7:7,     #Table 9 vs section 9
    8:8,     #Table 10 vs section 10
    9:9,     #Table 11 vs section 11
    10:10,     #Table 12 vs section 12
    11:11,     #Table 13 vs section 13
    12:12,     #Table 14 vs section 14
    13:13,     #Table 15 vs section 15
    14:14,     #Table 16 vs section 16
    15:15,     #Table 17 vs section 17
    15:16,     #Table 18 vs section 18
    17:17,     #Table 19 vs section 19
    18:18,     #Table 20 vs section 20
    19:19,     #Table 21 vs section 21
    20:20,     #Table 22 vs section 22
    21:21,     #Table 23 vs section 23
    22:22,     #Table 24 vs section 24
    23:23,     #Table 25 vs section 25
    24:24,     #Table 26 vs section 26
    25:25,     #Table 27 vs section 27
    26:26,     #Table 28 vs section 28
    27:27,     #Table 29 vs section 29
    28:28,     #Table 30 vs section 30
    29:29,     #Table 31 vs section 31
    30:30,     #Table 32 vs section 32
    31:31,     #Table 33 vs section 33
    32:32,     #Table 54 vs section 45
    33:33,     #Table 55 vs section 46
    34:34,     #Table 56 vs section 47
    35:35,
    36:36,
    37:37,
    38:38,
    39:39,
    40:40,
    41:41,
    42:42,
    43:43,
    44:44,
    45:45,
    46:46,
    47:47,
    48:48,
    49:49,
    50:50,
    51:51     #Table 57 vs section 48
}

detailed_word_test_item_vs_table_index_dic={
    'Max_Tx_Performance':[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
    'Tx_Mask_Margin':[31,32,33,34],
    'Tx_Flatness':[35,36,37],
    'Tx_Ramp':[38],
    'Rx_Dr':[40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66],
    'Rx_Max':[67,68,69,70],
    'Rx_Sens':[71,72,73,74]}

wifi_rate_vs_mode_dic={
	'11b':['11m','5.5m','2m','1m'],
	'11g':['54m','48m','36m','24m','18m','12m','9m','6m'],
	'11n_20':['mcs7','mcs6','mcs5','mcs4','mcs3','mcs2','mcs1','mcs0'],
	'11n_40':['mcs7_40','mcs6_40','mcs5_40','mcs4_40','mcs3_40','mcs2_40','mcs1_40','mcs0_40']
}



rf_crt_tx_vs_rate_dic = {
    "1m":[17,-10,25,2],#output_power>18dBm,EVM<-22(8%),Freq_err +-25,lo_leakage<2
    "2m":[17,-10,25,2],
    "5.5m":[17,-10,25,2],
    "11m":[17,-10,25,2],
    "6m":[18,-5,25,-15],
    "9m":[16,-8,25,-15],
    "12m":[16,-10,25,-15],
    "18m":[15,-13,25,-15],
    "24m":[15,-16,25,-15],
    "36m":[14,-19,25,-15],
    "48m":[14,-22,25,-15],
    "54m":[12,-25,25,-15],
    "mcs0":[17,-5,25,-15],
    "mcs1":[16,-10,25,-15],
    "mcs2":[16,-13,25,-15],
    "mcs3":[15,-16,25,-15],
    "mcs4":[15,-19,25,-15],
    "mcs5":[14,-22,25,-15],
    "mcs6":[14,-25,25,-15],
    "mcs7":[12,-27,25,-15],
    "mcs0_40":[17,-5,25,-20],
    "mcs1_40":[16,-10,25,-20],
    "mcs2_40":[16,-13,25,-20],
    "mcs3_40":[15,-16,25,-20],
    "mcs4_40":[15,-19,25,-20],
    "mcs5_40":[14,-22,25,-20],
    "mcs6_40":[14,-25,25,-20],
    "mcs7_40":[12,-27,25,-20]
}

detailed_rx_DR_word_table_vs_rate_dic={
    "11m":40,
    "2m":41,
    "5.5m":42,
    "1m":43,
    "6m":44,
    "9m":45,
    "12m":46,
    "18m":47,
    "24m":48,
    "36m":49,
    "48m":50,
    "54m":51,
    "mcs0":52,
    "mcs1":53,
    "mcs2":54,
    "mcs3":55,
    "mcs4":56,
    "mcs5":57,
    "mcs6":58,
    "mcs7":59,
    "mcs0_40":60,
    "mcs1_40":61,
    "mcs2_40":62,
    "mcs3_40":63,
    "mcs4_40":64,
    "mcs5_40":65,
    "mcs6_40":66,
    "mcs7_40":67,
    }



class WiFiAutoTest(object):
    def __init__(self,comport,chipv='ESP32'):
        self.comport = comport
        self.chipv = chipv
        self._MEM = MEM(self.comport,self.chipv)
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.rf_wifi_autotest_data = "D:/chip/eagletest/py_script/rftest/rfdata/rf_wifi_autotest_data/"
        self.folder= "rf_wifi_autotest_data"

    def TX_PWR_EVM_table_list(self,lost_list=[2], channel=[1,14], data_rate=['mcs6','mcs7'], iqv_no=1, iqv_num=10, doc='', select='',rf_crt_dic=[],comment=''):

        """
    	--iqv_no: 1-left port, 2-right port
    	--iqv_num: iqview average number
    	--para_set: 'default', 'normal', 'better', 'best'
    	--Only support the following data rate:11m,1m,54m,6m,mcs7,mcs0,mcs7_40,mcs0_40'
    	"""

    	cable_lose = lost_list[0]
    	chan_lst = []
    	pwr_lst = []
    	EVM_lst = []

    	title = 'channel, rate, power, evm, evm_std,evm_max,freq_error(kHz), syclk_error(ppm),lo_leakage(dB),iq_imb_amp(dB),iq_imb_phase(deg), evm_list\n'
    	fname = self.wifi.get_filename(self.folder, "TX_PWR_EVM_test_%s"%(data_rate), 'TX')
    	csvreport1 = csvreport(fname, title)
    	self.wifi.cmdstop()
    	for i  in range (0, len(data_rate)):
    		rate = data_rate[i]
    		for j in range(0, len(channel)):
    			chan = channel[j]
    			max_pwr = 25-cable_lose
     			loginfo(("rate=%s, channel=%d")%(rate, chan))
    			self.wifi.cmdstop()
    			cbw40m = self.wifi.rate2ht40(rate)
    			self.wifi.cbw40m_en(cbw40m)
    			freq = self.wifi.chan2freq(chan)
    			test_para = wifi_instrum.test_para(rate)
    			self.wifi.txpacket(chan,rate,0,cbw40m, 0,0,0.2)

    			myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10, 1)
    			[pwr, freq_err, clk_err, evm, evm_std, evm_max, evm_list,lo_leakage,iq_imb_amp,iq_imb_phase] = wifi_instrum.iqv_avg(myiqv, iqv_num,'false')

    			wifi_instrum.spectrum_mask(myiqv, iqv_num, 99) # only output 'pass' or 'fail' of the mask
    			iqv_mask = rfglobal.iqv_mask
    			spectrum_fail_point = iqv_mask['spectrum_fail_point']
    			obw_mhz = iqv_mask['obw_mhz']
    			if spectrum_fail_point == 0:
    				print 'mask pass'
    				mask_flag = 'pass'
    			else:
    				print 'mask fail'
    				mask_flag = 'fail'
    			print 'OBW = %f MHz'%(obw_mhz/1e6)
    			self.wifi.cmdstop()
    			rf_list=['%d'%chan,'%2.2f'%pwr,'%2.2f'%evm,'%2.2f'%freq_err,'%2.2f'%(clk_err),'%2.2f'%(lo_leakage),'%2.2f'%iq_imb_amp,'%2.2f'%iq_imb_phase,'%s'%(mask_flag)]

    			csvreport1.write_data([chan,rate,pwr,evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase,evm_list])

    			chan_lst.append(chan)
    			pwr_lst.append(rf_list[1])
    			EVM_lst.append(rf_list[2])

# -----word's data collect--------

     			table = doc.Tables[detailed_word_table_vs_rate_dic[rate]]
        		row_len = len(table.Rows) # word sheet
        		col_len = len(table.Columns)

        		col = j+2
    			select0 = table.Select()
    			for row in range(4,row_len):  # the first row =1
    				select1 = table.Cell(row,col).Select()
    				select.Font.Bold = False
    				select.Font.Italic = False
    				select.Font.ColorIndex = 0
    				select.TypeText(rf_list[row-4])

    			rf_crt =rf_crt_dic[rate]

    			if ((rf_crt[0]+rf_crt[1])>=float(rf_list[1]) >= (rf_crt[0]-rf_crt[1])) and (float(rf_list[2]) < rf_crt[2]) and  (abs(float(rf_list[4])) < rf_crt[3]) and (float(rf_list[5]) < rf_crt[4]) and (rf_list[8] == 'pass'):
    				select2 = table.Cell(3,j+2).Select()
    				select.Font.ColorIndex = 11  # color is green
    				select.TypeText('pass')
    			if float(rf_list[1]) < (rf_crt[0]-rf_crt[1]) or float(rf_list[1]) > (rf_crt[0]+rf_crt[1]) :
    				select2 = table.Cell(3,j+2).Select()
    				select.Font.ColorIndex = 6  # color is red
    				select.TypeText('fail')
    				select3 = table.Cell(5,col).Select()
    				select.Font.Bold = True
    			if float(rf_list[2]) > rf_crt[2]:
    				select2 = table.Cell(3,j+2).Select()
    				select.Font.ColorIndex = 6  # color is red
    				select.TypeText('fail')
    				select3 = table.Cell(6,col).Select()
    				select.Font.Bold = True
    			if abs(float(rf_list[4])) > rf_crt[3]:
    				select2 = table.Cell(3,j+2).Select()
    				select.Font.ColorIndex = 6  # color is red
    				select.TypeText('fail')
    				select3 = table.Cell(8,col).Select()
    				select.Font.Bold = True
    			if float(rf_list[5]) > rf_crt[4]:
    				select2 = table.Cell(3,j+2).Select()
    				select.Font.ColorIndex = 6  # color is red
    				select.TypeText('fail')
    				select3 = table.Cell(9,col).Select()
    				select.Font.Bold = True

    			if rf_list[8] != 'pass':
    				select2 = table.Cell(3,j+2).Select()
    				select.Font.ColorIndex = 6  # color is red
    				select.TypeText('fail')
    				select3 = table.Cell(10,col).Select()
    				select.Font.Bold = True
##    		csvreport1.write_data([chan,rate,pwr,evm,evm_std,evm_max,freq_err,clk_err, lo_leakage,iq_imb_amp,iq_imb_phase,evm_list])
    		select4 = table.Cell(5,col_len).Select()
    		table.Cell(5,col_len).Range.Text=rf_crt[0]
    		select.EndKey()
    		select.Text = '+'
    		select.EndKey()
    		select.Text = '-'
    		select.EndKey()
    		select.Text = rf_crt[1]

    		select5 = table.Cell(6,col_len).Select()
    		table.Cell(6,col_len).Range.Text='<'
    		select.EndKey()
    		select.Text = rf_crt[2]

    		select6 = table.Cell(8,col_len).Select()
    		table.Cell(8,col_len).Range.Text='+'
    		select.EndKey()
    		select.Text = '-'
    		select.EndKey()
    		select.Text = rf_crt[3]

    		select7 = table.Cell(9,col_len).Select()
    		table.Cell(9,col_len).Range.Text='<'
    		select.EndKey()
    		select.Text = rf_crt[4]

    		select8 = table.Cell(2,4).Select()
    		table.Cell(2,4).Range.Text=rate

#**********Draw pictures***********
##
        print "Begin to draw pic"
    	pylab.figure(100)
        pylab.title("Tx_Pwr_%s"%rate)
        pylab.plot(chan_lst,pwr_lst,label='%s'%(chan_lst))
        pylab.legend()
        pylab.grid()
        plt.savefig(self.rf_wifi_autotest_data+'/'+'pic'+'/'+'Tx_pwr_%s_%s.png'%(rate,comment))
        plt.close()

    	pylab.figure(100)
        pylab.title("Tx_EVM_%s"%rate)
        pylab.plot(chan_lst,EVM_lst,label='%s'%(chan_lst))
        pylab.legend()
        pylab.grid()
        plt.savefig(self.rf_wifi_autotest_data+'/'+'pic'+'/'+'Tx_EVM_%s_%s.png'%(rate,comment))
        plt.close()

        select1= table.Cell(13,2).Select()
        select.InlineShapes.AddPicture(self.rf_wifi_autotest_data+'/'+'pic'+'/'+'Tx_pwr_%s_%s.png'%(rate,comment))
        select1= table.Cell(13,3).Select()
        select.InlineShapes.AddPicture(self.rf_wifi_autotest_data+'/'+'pic'+'/'+'Tx_EVM_%s_%s.png'%(rate,comment))

    	print '\n\n------------Tx test complete--------------\n'

    def TX_spectrum_mask(self,lost_list=[1.5],channel=[1,14],data_rate=['1m','6m','mcs0','mcs0_40'],iqv_no=2,iqv_num=20, doc='', select='',comment=''):
    	"""
    	Can read the value of mask margin, only test data_rate '1m', '6m', 'mcs0', 'mcs0_40'
    	--iqv_no: 1-left port, 2-right port
    	--iqv_num: iqview average number
    	"""

    	cable_lose = lost_list[0]
    	self.wifi.cmdstop()
    	title = "cbw40m, rate ,chan,lower4_marg, lower3_marg, lower2_marg, lower1_marg, upper1_marg, upper2_marg, upper3_marg, upper4_marg\n"
    	fname = self.wifi.get_filename(self.folder, 'TX_spectrum_mask_test_%s'%data_rate, 'TX')
    	csvreport1 = csvreport(fname, title)
    	for rate in data_rate:

    		table = doc.Tables[detail_mask_flatness_rate_vs_table_dic[rate]]

    		for j in range (0,len(channel)):
				max_pwr = 25-cable_lose
				chan = channel[j]
				loginfo(("rate=%s, channel=%d")%(rate, chan))
				freq = self.wifi.chan2freq(chan)
				self.wifi.cmdstop()
				test_para = wifi_instrum.test_para(rate)
				cbw40m = self.wifi.rate2ht40(rate)
				self.wifi.cbw40m_en(cbw40m)
				self.wifi.txpacket(chan,rate,0,cbw40m, 0, 0, 0.5)
				myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure',cable_lose, 10, 0)
				[freq_list,marg_list] = wifi_instrum.spectrum_mask_flatness(myiqv, iqv_num,99)
				self.wifi.cmdstop()
				csvreport1.write_data([cbw40m,rate,chan,marg_list])

				col_freq = j*2+2
				col_marg = j*2+3
				select0 = table.Select()
				row_len = len(table.Rows)
				col_len = len(table.Columns)
				for row in range(6,row_len):
   					select1 = table.Cell(row,col_freq).Select()
   					select.Font.Bold = False
   					select.Font.Italic = False
   					select.Font.ColorIndex = 0
   					if rate in ('1m'):
   					    select.TypeText(freq_list[row-4])
   					else:
   					    select.TypeText(freq_list[row-6])
				for row in range(6,row_len):
   					select1 = table.Cell(row,col_marg).Select()
   					select.Font.Bold = False
   					select.Font.Italic = False
   					select.Font.ColorIndex = 0
   					if rate in('1m'):
   					    select.TypeText(marg_list[row-4])
   					else:
   					    select.TypeText(marg_list[row-6])
				for k in range(2,len(marg_list)-2):
   					if float(marg_list[k]) > 1.5:
  						flag_true=1
   					else:
  						flag_true=0
  						break
				print flag_true

				if flag_true == 1:
					select2 = table.Cell(5,col_freq).Select()
					select.Font.ColorIndex = 11  # color is green
					select.TypeText('pass')
					select2 = table.Cell(5,col_marg).Select()
					select.Font.ColorIndex = 11  # color is green
					select.TypeText('pass')
				else:
					select2 = table.Cell(5,col_freq).Select()
					select.Font.ColorIndex = 6  # color is red
					select.TypeText('fail')
					select2 = table.Cell(5,col_marg).Select()
					select.Font.ColorIndex = 6  # color is red
					select.TypeText('fail')

    	print '\n\n------------TX Mask test complete-------------\n'

    def TX_spectrum_flatness(self,lost_list=[1.5],channel=[1,14],data_rate=['54m','mcs7','mcs7_40'],iqv_no=2,iqv_num=20,doc='', select=''):
    	"""
    	only test data_rate '54m', 'mcs7', 'mcs7_40'
    	--iqv_no: 1-left port, 2-right port
    	--iqv_num: iqview average number
    	"""
    	iq_id=sock.get_IQ_ID()
    	print "IQ_ID=",iq_id
        cable_lose=lost_list[0]
    	self.wifi.cmdstop()
    	for rate in data_rate:
    		test_para = wifi_instrum.test_para(rate)

    		table = doc.Tables[detail_mask_flatness_rate_vs_table_dic[rate]]
    		rf_crt = ['pass']
    		for j in range (0,len(channel)):
    			max_pwr = 25-cable_lose
    			chan = channel[j]
    			loginfo (("rate=%s, channel=%d")%(rate, chan))
    			freq = self.wifi.chan2freq(chan)
    			self.wifi.cmdstop()
    			cbw40m = self.wifi.rate2ht40(rate)
    			self.wifi.cbw40m_en(cbw40m)
    			self.wifi.txpacket(txchan=chan,rate_sym=rate, PackNum=0, cbw40=cbw40m, ht_dup=0, backoff_qdb=0, duty=0.5)
    			myiqv=tester.tester(freq, max_pwr, rate,test_para, iqv_no,'measure', cable_lose, 10, 0)
    			if iq_id == 1:    # IQxel
     				result = wifi_instrum.spectrum_mask_flatness(myiqv, iqv_num, 99)
     				print result
     				flatness_marg_list=result[2]
    				for i in range(0,len(flatness_marg_list)):
    					if flatness_marg_list[i] >= 0:
    						flat_pass = 'pass'
    					else:
    						flat_pass = 'fail'
    						break
    			elif iq_id == 2: #wt200
    				flatness_passed = wifi_instrum.spectrum_flatness_wt200(myiqv, iqv_num )
    				print flatness_passed
    				if  flatness_passed == 0:
    					flat_pass = 'fail'
    				else:
    					flat_pass = 'pass'
    			self.wifi.cmdstop()
    			rf_list=['%d'%chan,'%s'%flat_pass]
    			col = j+2
    			select0 = table.Select()
    			row_len = len(table.Rows)
    			col_len = len(table.Columns)
    			for row in range(3,row_len):
    				select1 = table.Cell(row,col).Select()
    				select.Font.Bold = False
    				select.Font.Italic = False
    				select.TypeText(rf_list[row-3])

    			if rf_list[1] == rf_crt[0]:
    				select2 = table.Cell(4,col).Select()
    				select.Font.Bold = True
    				select.Font.ColorIndex = 11  # color is green
    			elif rf_list[1] != rf_crt[0]:
    				select2 = table.Cell(4,col).Select()
    				select.Font.Bold = True
    				select.Font.ColorIndex = 6  # color is red

    	print '\n\n--------------test complete------------\n'

    def power_on_down_ramp_11b_1m(self,lost_list=[1.5], iqv_no=1, iqv_num=10, doc='', select=''):
    	"""
    	only test data_rate '1m'
    	--iqv_no: 1-left port, 2-right port
    	--iqv_num: iqview average number
    	"""

    	self.wifi.cmdstop()
    	channel = [1,5,9,13]
    	data_rate = '1m'
    	cable_lose= lost_list[0]
    	table = doc.Tables[39]
    	rf_crt = [2,2]
    	for j in range (0,len(channel)):
    		max_pwr = 25-cable_lose
    		chan = channel[j]
    		loginfo(( "rate=%s, channel=%d")%(data_rate, chan))
    		freq = self.wifi.chan2freq(chan)
    		self.wifi.cmdstop()
    		self.wifi.txpacket(txchan=chan,rate_sym=data_rate, PackNum=0, cbw40=0, ht_dup=0, backoff_qdb=0, duty=0.5)
    		myiqv=tester.tester(freq, max_pwr, data_rate, wifi_instrum.test_para(data_rate), iqv_no,'measure', cable_lose, 10, 0)
    		[rampup,rampdown]= wifi_instrum.pwrramp(myiqv, iqv_num)
    		self.wifi.cmdstop()
    		rf_list=[chan,rampup,rampdown]
    		col = j+2
    		select0 = table.Select()
    		row_len = len(table.Rows)
    		col_len = len(table.Columns)
    		for row in range(4,row_len):
    			select1 = table.Cell(row,col).Select()
    			select.Font.Bold = False
    			select.Font.Italic = False
    			select.Font.ColorIndex = 0
    			select.TypeText(rf_list[row-4])


    		if (float(rf_list[1]) < rf_crt[0]) and (float(rf_list[2]) < rf_crt[1]):
    			select2 = table.Cell(3,j+2).Select()
    			select.Font.ColorIndex = 11  # color is green
    			select.TypeText('pass')
    		if float(rf_list[1]) > rf_crt[0]:
    			select2 = table.Cell(3,j+2).Select()
    			select.Font.ColorIndex = 6  # color is red
    			select.TypeText('fail')
    			select3 = table.Cell(5,col).Select()
    			select.Font.Bold = True

    		if float(rf_list[2]) > rf_crt[1]:
    			select2 = table.Cell(3,j+2).Select()
    			select.Font.ColorIndex = 6  # color is red
    			select.TypeText('fail')
    			select3 = table.Cell(6,col).Select()
    			select.Font.Bold = True


    	print '\n\n--------------------------\n'


    def WIFI_RX_per(self,cable_lose=13,rx_chan=11,tx_chan=11, rx_ratelst=['mcs6'], minpwr=-80, maxpwr=-30,pwr_step =1, packnum=100,iqv_no=1):

    	if tx_chan<15:
    		tx_freq=self.wifi.chan2freq(tx_chan)
    	else:
    		tx_freq=tx_chan

    	if rx_chan<15:
    		rx_freq=self.wifi.chan2freq(rx_chan)
    	else:
    		rx_freq=rx_chan
    	loginfo('tx chan cfg: %d %d'%(tx_chan,tx_freq))
    	loginfo('rx chan cfg: %d %d'%(rx_chan,rx_freq))

    	mytester=tester.tester(tx_freq,-40,'1m',1,iqv_no,'source',cable_lose,10,0);
    	title = "rfpwr,rxnum,rssi,gain,noise,err,fcs,freqoff\n"
    	filename = self.wifi.get_filename(self.folder,"Rxagcscan_%d_%s"%(tx_chan,rx_ratelst),'Rx_Scan')
    	csvreport1 = csvreport(filename,title)


    	for rx_rate in rx_ratelst:
    		perform_list=[];
    		rfpwr= minpwr;

    		mytester.sigout(tx_freq,rfpwr,cable_lose,rx_rate,packnum,iqv_no)
    		sens=minpwr+20
    		sens_rssi=minpwr+20
    		while rfpwr<=maxpwr:
    			mytester.sigout(tx_freq,rfpwr,cable_lose,rx_rate,packnum,iqv_no)
    			cbw40m = self.wifi.rate2ht40(rx_rate)
    			self.wifi.cbw40m_en(cbw40m)
    			self.wifi.esp_rx(tx_chan, rx_rate)
    			mytester.trig_wave(iqv_no);
    			time.sleep(0.1)
    			result_data = self.wifi.cmdstop()

    			[DesirePackNum, gain, rssi, noise, err, err2, freqoff, rssi_min, rssi_max] = self.wifi.rxresult(result_data)

    			perform_list.append((rfpwr,DesirePackNum,rssi,noise,err,err2, freqoff));
    			loginfo(result_data)

    			rfpwr=rfpwr+pwr_step;
    			mytester.set_pwr(rfpwr,0,iqv_no,'source');
    			csvreport1.write_data([rfpwr,DesirePackNum,rssi,gain,noise,err,err2,freqoff])



    #**************creat log***************#
    		cur_sens=0
    		cur_sens_rssi=0
    		cur_sens_find=0
    		cur_max=0
    		cur_max_rssi=0
    		cur_max_find=0
    		cur_max_start = 0
    		fail=0
    		cur_err=0
    		cur_err_fcs=0



    		for data in perform_list:

    			if cur_sens_find==0:
    				if data[1]>=(packnum*0.9):
    					cur_sens=data[0]
    					cur_sens_rssi=data[2]
    					cur_err=data[4]
    					cur_err_fcs = data[5]
    					cur_sens_find=1
    				else:
    					cur_sens=data[0]
    					cur_sens_rssi=data[2]
    					cur_err=data[4]
    					cur_err_fcs = data[5]
    					cur_sens_find=0
    			if cur_max_find==0:
    				if cur_max_start==0:
    					if data[1]>=(packnum*0.95):
    						cur_max_start=1
    				else:
    					if data[1]<(packnum*0.9):
    						cur_max_find=1
    					else:
    						cur_max=data[0]
    						cur_max_rssi=data[2]
    						cur_max_find=0
    	mytester.gen_switch('OFF',iqv_no);
    	return [cur_sens, cur_sens_rssi/10.0, cur_sens_find, cur_max, cur_max_rssi/10.0, cur_max_find, perform_list]


    def sensitivity_word(self,lost_list=[13],channel=[1,6,11],data_rate=['mcs6','mcs7'], pwr_step=1, packnum=100, iqv_no=1,doc='', select='',comment=''):

    	cable_lose = lost_list[0]
        title ="Channel, Rate,sens,sens_rssi_lst\n"
    	filename = self.wifi.get_filename(self.folder,'RFTest_RX_Sens_%s'%data_rate,'Rx_Sens')
    	csvreport1 = csvreport(filename,title)
    	chan_lst = []
    	rate_lst = []
    	sens = []
    	sens_rssi_lst = []
    	cur_sens_find_lst = []

    	for i in range (0,len(data_rate)):

    		cur_rate = data_rate[i]
    		rate_sens = sens_dict[cur_rate]
    		minpwr = rate_sens - 3
    		maxpwr = rate_sens + 10
    		cbw40m = self.wifi.rate2ht40(cur_rate)
    		self.wifi.cbw40m_en(cbw40m)

    		table = doc.Tables[detailed_rx_sensitivity_word_table_vs_rate_dic[cur_rate]]

    		row_len = len(table.Rows)
    		col_len = len(table.Columns)
    		print "row=%d,col_len=%d"%(row_len,col_len)

    		mytester=tester.tester(2412,-40,'1m',1,iqv_no,'source',cable_lose,10,0)
    		for j in range(0,len(channel)):
    			rx_chan =channel[j];
    			tx_chan = channel[j];

    			[cur_sens, cur_sens_rssi, cur_sens_find, cur_max, cur_max_rssi, cur_max_find, perform_list] = self.WIFI_RX_per(cable_lose,rx_chan,tx_chan,[cur_rate],minpwr,maxpwr,pwr_step,packnum,iqv_no)

    			chan_lst.append(channel[j]);
    			rate_lst.append(cur_rate);
    			sens.append(cur_sens);
    			sens_rssi_lst.append(cur_sens_rssi);
    			cur_sens_find_lst.append(cur_sens_find)
    			csvreport1.write_data([tx_chan,cur_rate,cur_sens,cur_sens_rssi])

    			if cur_rate in ['mcs7_40','mcs6_40','mcs5_40','mcs4_40','mcs3_40','mcs2_40','mcs1_40','mcs0_40']:
    				col = table_chan_col_40M_dic[channel[j]]
    			else:
    				col = table_chan_col_20M_dic[channel[j]]

    			row = table_rate_row_dic[cur_rate]
    			select0 = table.Select()
    			select1 = table.Cell(row,col).Select()
    			select.Font.Bold = False
    			select.Font.Italic = False
    			select.Font.ColorIndex = 0
    			select.TypeText(cur_sens)

		print "Begin to draw pic"
		pylab.figure(100)
		pylab.title("Rx_Sens_by_channel")
		pylab.plot(chan_lst,sens,label='%s'%(cur_rate))

    	print "save pic"
    	pylab.legend()
    	pylab.grid()
    	plt.savefig(self.rf_wifi_autotest_data+'/'+'pic'+'/'+'Rx_Sens_%s_%s.png'%(cur_rate,comment))
    	plt.close()

#********************pass or fail ***********************
    	for rate in data_rate:
    		if rate in ['mcs7_40','mcs6_40','mcs5_40','mcs4_40','mcs3_40','mcs2_40','mcs1_40','mcs0_40']:
    			col_start = channel[0]-1
    			col_end = channel[len(channel)-1]
    		else:
    			col_start = channel[0]+1
    			col_end = channel[len(channel)-1]+2
    	sens_lst = []
    	k_flag = []

    	row_start = table_rate_row_dic[data_rate[0]]
    	row_end = table_rate_row_dic[data_rate[len(data_rate)-1]]
    	row_lst = []
    	for rate in data_rate:
    		row = table_rate_row_dic[rate]
    		row_lst.append(row)

    	print row_lst
    	for col in range (col_start,col_end):
    		for row in row_lst:
    			select2 = table.Cell(int(row),col).Select()
    			sens_1 = table.Cell(int(row),col).Range.Text
    			sens_2=sens_1.encode('ascii')
    			sensitivity = re.findall(r"\-+\d+\.?\d*",sens_2)
    			if sensitivity != []:
    				a = int(sensitivity[0])
    			else:
    				a = []

    			sens_lst.append(a)
    		sens_dic = {}
    		for x in range (0,len(sens_lst)):
    			sens_dic[data_rate[x]] = sens_lst[x]
    		flag_none = 3
    		flag = 3
    		for k in range (0,len(sens_dic)):
    			if sens_dic[data_rate[k]] == []:
    				flag_none = 1
    			elif sens_dic[data_rate[k]] <= rx_sensitivity_crt[data_rate[k]]:
    				flag = 1
    			elif sens_dic[data_rate[k]] > rx_sensitivity_crt[data_rate[k]]:
    				flag = 0
    				k_flag.append(k)
    		if flag_none == 1:
    			select3 = table.Cell(4,col).Select()
    			select.TypeText('')
    		elif len(k_flag) == 0:
    			select3 = table.Cell(4,col).Select()
    			select.Font.ColorIndex = 11  # color is green
    			select.TypeText('pass')
    		else:
    			select3 = table.Cell(4,col).Select()
    			select.Font.ColorIndex = 6  # color is red
    			select.TypeText('fail')
    			for m in range(0,len(k_flag)):
    				row_flag = table_rate_row_dic[data_rate[k_flag[m]]]
    				select3 = table.Cell(row_flag,col).Select()
     				select.Font.Bold = True


		sens_lst = []
		k_flag = []
		flag = 3
		flag_none = 3
    	print '\n\n----------test complete----------------\n'



    def rx_max_word(self,lost_list=[13],channel=[1,6,11],data_rate=['mcs6','mcs7'], pwr_step=1, packnum=100, iqv_no=1, doc='', select='',comment=''):
    	'''
    	--minpwr: min input power setting in 'rfglobal.rx_search_power_start'
    	--dynamic_mode: 0 means search sensitivity, 1 means rx dynamic range
    	'''
    	title = "chan, rate, maxlevel, maxlevel_rssi\n"
    	fname = self.wifi.get_filename(self.folder,"Rx_Maxlevel",'Rx_Maxlevel')
    	csvreport1 = csvreport(fname,title)
    	chan = []
    	rate = []
    	sens = []
    	sens_rssi = []
    	err = []
    	err_fcs = []
    	cable_lose = lost_list[0]
    	chan_sel=channel
    	rate_l = len(data_rate)
    	chan_l = len(chan_sel)
    	for i in range(0,rate_l):
    		cur_rate = data_rate[i]
    		rx_maxlevel =rx_maxlevel_dict[cur_rate]
    		minpwr = -10
    		maxpwr = 10
    		cbw40m =self.wifi.rate2ht40(cur_rate)
    		self.wifi.cbw40m_en(cbw40m)
    		table = doc.Tables[detailed_rx_max_word_table_vs_rate_dic[cur_rate]]
    		row_len = len(table.Rows)
    		col_len = len(table.Columns)
    		for j in range(0,chan_l):
    			rx_chan = chan_sel[j];
    			tx_chan = chan_sel[j];
    			[cur_sens, cur_sens_rssi, cur_sens_find, cur_max, cur_max_rssi, cur_max_find, perform_list] = self.WIFI_RX_per(cable_lose,rx_chan,tx_chan,[cur_rate],minpwr,maxpwr,pwr_step,packnum,iqv_no)
    			chan.append(chan_sel[j]);
    			rate.append(cur_rate);
    			sens.append(cur_sens);
    			sens_rssi.append(cur_sens_rssi);
##    			err.append(cur_err);
##    			err_fcs.append(cur_err_fcs);
    			csvreport1.write_data([tx_chan,cur_rate,cur_max,cur_max_rssi])

    			if cur_rate in ['mcs0_40','mcs1_40','mcs2_40','mcs3_40','mcs4_40','mcs5_40','mcs6_40','mcs7_40']:
    				col = table_chan_col_40M_dic[chan_sel[j]]
    			else:
    				col = table_chan_col_20M_dic[chan_sel[j]]

    			row = table_rate_row_dic[cur_rate]
    			select0 = table.Select()
    			select1 = table.Cell(row,col).Select()
    			select.Font.Bold = False
    			select.Font.Italic = False
    			select.Font.ColorIndex = 0
    			select.TypeText(cur_max)


    	for i in range(0,len(data_rate)):
    		if data_rate[i] in ['mcs7_40','mcs6_40','mcs5_40','mcs4_40','mcs3_40','mcs2_40','mcs1_40','mcs0_40']:
    			col_start = chan_sel[0]+1-2
    			col_end = chan_sel[len(chan_sel)-1]
    		else:
    			col_start = chan_sel[0]+1
    			col_end = chan_sel[len(chan_sel)-1]+1+1
    	sens_lst = []
    	k_flag = []

    	row_start = table_rate_row_dic[data_rate[0]]
    	row_end = table_rate_row_dic[data_rate[len(data_rate)-1]]
    	row_lst = []
    	for n in range (0,len(data_rate)):
    		row = table_rate_row_dic[data_rate[n]]
    		row_lst.append(row)

    	print row_lst
    	for col in range (col_start,col_end):
    		for row in row_lst:
    			select2 = table.Cell(int(row),col).Select()
    			sens_1 = table.Cell(int(row),col).Range.Text
    			sens_2=sens_1.encode('ascii')
    			sensitivity = re.findall(r"\-+\d+\.?\d*",sens_2)
    			if sensitivity != []:
    				a = int(sensitivity[0])
    			else:
    				a = []

    			sens_lst.append(a)
    		sens_dic = {}
    		for x in range (0,len(sens_lst)):
    			print sens_lst[x]
    			sens_dic[data_rate[x]] = sens_lst[x]
    		flag_none = 3
    		flag = 3
    		for k in range (0,len(sens_dic)):
    			print rx_maxlevel_dict[data_rate[k]]
    			print sens_dic[data_rate[k]]
    			if sens_dic[data_rate[k]] == []:

    				flag_none = 1
    			elif sens_dic[data_rate[k]] < rx_maxlevel_dict[data_rate[k]]:
    				flag = 1
    			elif sens_dic[data_rate[k]] >= rx_maxlevel_dict[data_rate[k]]:
    				flag = 0
    				k_flag.append(k)
    		if flag_none == 1:
    			select3 = table.Cell(4,col).Select()
    			select.TypeText('')
    		elif len(k_flag) == 0:
    			select3 = table.Cell(4,col).Select()
    			select.Font.ColorIndex = 11  # color is green
    			select.TypeText('pass')
    		else:
    			select3 = table.Cell(4,col).Select()
    			select.Font.ColorIndex = 6  # color is red
    			select.TypeText('fail')
    			for m in range(0,len(k_flag)):
    				row_flag = table_rate_row_dic[data_rate[k_flag[m]]]
    				select3 = table.Cell(row_flag,col).Select()
    				select.Font.Bold = True

    		sens_lst = []
    		k_flag = []
    		flag = 3
    		flag_none = 3
    	print "Begin to draw pic"
    	pylab.figure(100)
    	pylab.title("Rx_Maxlevel_%s"%cur_rate)
    	pylab.plot(chan,sens,label='%s'%(cur_rate))
    	pylab.legend()
    	pylab.grid()
    	plt.savefig(self.rf_wifi_autotest_data+'/'+'pic'+'/'+'Rx_Maxlevel_%s_%s.png'%(cur_rate,comment))
    	plt.close()

    	return [sens,sens_rssi,err]
    	print '\n\n----------test complete----------------\n'

    def rx_dynamic_range_excel(self,lost_list=[13],channel=[11], data_rate=['mcs6'],packnum=100,iqv_no=1, doc='', select='',comment=''):
    	'''
    	--dynamic_mode:0 means search sensitivity, 1 means rx dynamic range
     '''
    	title = "chan, rate, maxlevel, maxlevel_rssi,sens,sens_rssi\n"
    	fname = self.wifi.get_filename(self.folder,"Rx_DR",'Rx_DR')
    	csvreport1 = csvreport(fname,title)
    	cable_lose = lost_list[0]
    	success_lst = []
    	chan_lst=[]
    	rx_rssi_lst=[]

    	pwr_step = 1
    	for i in range (0,len(data_rate)):
    		cur_rate = data_rate[i]
    		cbw40m = self.wifi.rate2ht40(cur_rate)
    		maxpwr = rx_maxlevel_dict[cur_rate]
    		minpwr = sens_dict[cur_rate] - 3
##      		maxpwr = -40
##    		minpwr = -50
    		self.wifi.cbw40m_en(cbw40m)
    		for j in range (0,len(channel)):
    			tx_chan = channel[j]
    			rx_chan = channel[j]
##    			tx_freq=self.wifi.chan2freq(tx_chan)
    			[cur_sens, cur_sens_rssi, cur_sens_find, cur_max, cur_max_rssi, cur_max_find, perform_list] = self.WIFI_RX_per(cable_lose,rx_chan,tx_chan,[cur_rate],minpwr,maxpwr,pwr_step,packnum,iqv_no)
    			success_lst = []
    			rx_rssi_lst = []
    			for data in perform_list:
        			success_lst.append(data[1])
        			rx_rssi_lst.append(data[0])

    			csvreport1.write_data([tx_chan,cur_rate,cur_max,cur_max_rssi,cur_sens,cur_sens_rssi])

     			table = doc.Tables[detailed_rx_DR_word_table_vs_rate_dic[cur_rate]]
          		row_len = len(table.Rows) # word sheet
          		col_len = len(table.Columns)
          		print "row_len=%d,col_len=%d"%(row_len,col_len)
          		print_lst =[tx_chan,cur_max,cur_sens]
          		col = j+2
          		select0 = table.Select()
    			for row in range(4,row_len):
        			select1 = table.Cell(row,col).Select()
        			select.Font.Bold = False
        			select.Font.Italic = False
        			select.Font.ColorIndex = 0
        			select.TypeText(print_lst[row-4])

		print "begin to draw"
		pylab.figure(100)
		pylab.title("Rx_DR_%s"%cur_rate)
		label = 'chan%d'%(tx_chan)
		plt1=pylab.plot(rx_rssi_lst,success_lst,label=label)

		pylab.legend()
		pylab.grid()
		plt.savefig(self.rf_wifi_autotest_data+'/'+'pic'+'/'+'Rx_DR_%s_%s.png'%(cur_rate,comment))
		plt.close()

    	select1=table.Cell(7,2).Select()
    	select.InlineShapes.AddPicture(self.rf_wifi_autotest_data+'/'+'pic'+'/'+'Rx_DR_%s_%s.png'%(cur_rate,comment))

        #----------------------------pass or fail-----------------------------#

    	print '\n\n----------test complete----------------\n'



    def Read_test_case(self,path='',test_case_file=''):     #test case an zhao No jin xing pai xu

		excelapp = win32com.client.Dispatch('Excel.Application')
		excelapp.Visible = 1
		excel = excelapp.Workbooks.Open(path+"\\%s"%test_case_file)
		sheet = excel.Worksheets(1)
		test_case_list=[]
		test_enable_list = []
		channel_sigle_list = []
		channel_total_list = []
		Cable_loss = []
		Back_off = []
		test_information = []
		No = []
		for i in range(2,122):
			no = int(sheet.Cells(i,1).Value)
			test_case = sheet.Cells(i,2).Value
			test_enable = sheet.Cells(i,3).Value
			channel_sel = sheet.Cells(i,4).Value
			channel_sel = channel_sel.replace('[','').replace(']','')
			channel_sel = channel_sel.split(',')
			for i in range(len(channel_sel)):
				channel_sel[i] = channel_sel[i].replace(",",'')
				channel_sigle_list.append(int(channel_sel[i]))

			No.append(no)
			test_case_list.append(str(test_case))
			test_enable_list.append(str(test_enable))
			channel_total_list.append(channel_sigle_list)
			channel_sigle_list = []

		Module_Name = str(sheet.Cells(2,7).Value)
		Sample_Number = str(sheet.Cells(4,7).Value)
		Test_Bin = str(sheet.Cells(9,7).Value)
		Cable_loss.append(float(sheet.Cells(10,7).Value))
		Back_off.append(int(sheet.Cells(11,7).Value))
		rf_port = int(sheet.Cells(13,7).Value)


		for row in range(2,13):
			test_information.append(str(sheet.Cells(row,7).Value))

		excel.Close()
		excelapp.Quit()

		No_test_case_dict={}
		No_test_enable_dict={}
		for i in range(0,len(No)):
			No_test_case_dict[No[i]] = test_case_list[i]
		for i in range(0,len(No)):
			No_test_enable_dict[No[i]] = test_enable_list[i]
		No_final =[]
		for key in No_test_enable_dict:
			if No_test_enable_dict[key] == 'Yes':
				No_final.append(key)
		No_final.sort()
		test_case_final = []
		for j in range(0,len(No_final)):
			test_case_final.append(No_test_case_dict[No_final[j]])
		print test_case_final

		test_case_channel_sel_dict={}
		for i in range(0,len(test_case_list)):
			test_case_channel_sel_dict[test_case_list[i]] = channel_total_list[i]

		return [test_case_final,Module_Name,Sample_Number,Test_Bin,Cable_loss,Back_off,rf_port,test_information,test_case_channel_sel_dict]


    def Read_RF_Performance_Criterion(self,path='',test_case_file=''):

    	excelapp = win32com.client.Dispatch('Excel.Application')
    	excelapp.Visible = 0
    	excel = excelapp.Workbooks.Open(path+"\\%s"%test_case_file)
    	sheet = excel.Worksheets(1)
    	rf_crt_dic = {}
    	for row in range(3,31):
    		rf_crt = []
    		for col in range(9,15):
    			rf_crt.append(sheet.Cells(row,col).Value)
    		key = str(rf_crt[0])
    		value = []
    		for i in range(1,len(rf_crt)):
    			value.append(float(rf_crt[i]))
    		rf_crt_dic[key]=value
    	dic = sorted(rf_crt_dic.iteritems(),key=lambda d:d[0])
    	rf_crt_dic = dict(dic)
    	excel.Close()
    	excelapp.Quit()

    	return rf_crt_dic

    def write_test_information_to_word(self,test_information=[],doc='',select=''):
    	table = doc.Tables[1]
    	select0 = table.Select()
    	row_len = len(table.Rows)
    	for row in range(1,row_len):
    		select1 = table.Cell(row,2).Select()
    		select.TypeText(test_information[row-1])


    def pass_or_fail_of_test_item_summary(self,doc_file=''):

        doc = Document(doc_file)
        names=locals()
        table_vs_pass_dic={}
        for key in detailed_word_test_item_vs_table_index_dic:
            table_index_list =detailed_word_test_item_vs_table_index_dic[key]
            for table_index in table_index_list:
                table = doc.tables[table_index]
                names['pass_or_fail_table_%s'%(table_index)]=[]
                for col in range(1,len(table.columns)):
                    if key == 'Max_Tx_Performance':
                        names['pass_or_fail_table_%s'%(table_index)].append((table.cell(2,col).text).encode('ascii'))
                    elif key == 'Tx_Mask_Margin':
                        names['pass_or_fail_table_%s'%(table_index)].append((table.cell(4,col).text).encode('ascii'))
                    elif key == 'Tx_Flatness':
                        names['pass_or_fail_table_%s'%(table_index)].append((table.cell(3,col).text).encode('ascii'))
                    elif key == 'Tx_Ramp':
                        names['pass_or_fail_table_%s'%(table_index)].append((table.cell(2,col).text).encode('ascii'))
                    elif key in['Rx_Max','Rx_Sens']:
                        names['pass_or_fail_table_%s'%(table_index)].append((table.cell(3,col).text).encode('ascii'))
                flag_none=[]
                for i in range(0,len(names['pass_or_fail_table_%s'%(table_index)])):
                    if names['pass_or_fail_table_%s'%(table_index)][i] == 'fail':
                        flag_pass = 0 # only one fail means 'fail'
                        break
                    elif names['pass_or_fail_table_%s'%(table_index)][i] != 'pass' and names['pass_or_fail_table_%s'%(table_index)][i] != 'fail':
                        flag_none.append(1)
                    else:
                        flag_pass = 1 # all pass means 'pass'
                if len(flag_none) == len(names['pass_or_fail_table_%s'%(table_index)]):
                    flag_pass = 2 # means this table not test
                table_vs_pass_dic[table_index] = flag_pass

        Tx_table_fail_list=[]
        Tx_table_pass_list=[]
        Tx_table_none_list=[]
        Mask_table_fail_list=[]
        Mask_table_pass_list=[]
        Mask_table_none_list=[]
        Flatness_table_fail_list=[]
        Flatness_table_pass_list=[]
        Flatness_table_none_list=[]
        Ramp_table_fail_list=[]
        Ramp_table_pass_list=[]
        Ramp_table_none_list=[]
        Rx_max_table_fail_list=[]
        Rx_max_table_pass_list=[]
        Rx_max_table_none_list=[]
        Rx_sens_table_fail_list=[]
        Rx_sens_table_pass_list=[]
        Rx_sens_table_none_list=[]
        Tx_table_index=detailed_word_test_item_vs_table_index_dic['Max_Tx_Performance']
        mask_table_index=detailed_word_test_item_vs_table_index_dic['Tx_Mask_Margin']
        flatness_table_index=detailed_word_test_item_vs_table_index_dic['Tx_Flatness']
        ramp_table_index=detailed_word_test_item_vs_table_index_dic['Tx_Ramp']
        rx_max_table_index=detailed_word_test_item_vs_table_index_dic['Rx_Max']
        rx_sens_table_index=detailed_word_test_item_vs_table_index_dic['Rx_Sens']
        for key in Tx_table_index:
            if table_vs_pass_dic[key] == 0:
                Tx_table_fail_list.append(key)
            elif table_vs_pass_dic[key] ==1:
                Tx_table_pass_list.append(key)
            elif table_vs_pass_dic[key] == 2:
                Tx_table_none_list.append(key)
        for key in mask_table_index:
            if table_vs_pass_dic[key] == 0:
                Mask_table_fail_list.append(key)
            elif table_vs_pass_dic[key] ==1:
                Mask_table_pass_list.append(key)
            elif table_vs_pass_dic[key] == 2:
                Mask_table_none_list.append(key)
        for key in flatness_table_index:
            if table_vs_pass_dic[key] == 0:
                Flatness_table_fail_list.append(key)
            elif table_vs_pass_dic[key] ==1:
                Flatness_table_pass_list.append(key)
            elif table_vs_pass_dic[key] == 2:
                Flatness_table_none_list.append(key)
        for key in ramp_table_index:
            if table_vs_pass_dic[key] == 0:
                Ramp_table_fail_list.append(key)
            elif table_vs_pass_dic[key] ==1:
                Ramp_table_pass_list.append(key)
            elif table_vs_pass_dic[key] == 2:
                Ramp_table_none_list.append(key)
        for key in rx_max_table_index:
            if table_vs_pass_dic[key] == 0:
                Rx_max_table_fail_list.append(key)
            elif table_vs_pass_dic[key] ==1:
                Rx_max_table_pass_list.append(key)
            elif table_vs_pass_dic[key] == 2:
                Rx_max_table_none_list.append(key)
        for key in rx_sens_table_index:
            if table_vs_pass_dic[key] == 0:
                Rx_sens_table_fail_list.append(key)
            elif table_vs_pass_dic[key] ==1:
                Rx_sens_table_pass_list.append(key)
            elif table_vs_pass_dic[key] == 2:
                Rx_sens_table_none_list.append(key)

        doc.save(doc_file)

        wordapp = Dispatch('Word.Application')
        wordapp.Visible = 1
        doc = wordapp.Documents.Open(doc_file)
        select = wordapp.Selection

        table1=doc.Tables[2]
        table2=doc.Tables[3]

        if len(Tx_table_fail_list) != 0:
            select1 = table1.Cell(3,3).Select()
            select.Font.ColorIndex = 6  # color is red
            select.TypeText('fail')
        elif len(Tx_table_pass_list) ==len(detailed_word_test_item_vs_table_index_dic['Max_Tx_Performance']):
            select1 = table1.Cell(3,3).Select()
            select.Font.ColorIndex = 11  # color is green
            select.TypeText('pass')
        elif len(Tx_table_pass_list) != 0 and len(Tx_table_none_list) == (len(detailed_word_test_item_vs_table_index_dic['Max_Tx_Performance'])-len(Tx_table_pass_list)):
            select1 = table1.Cell(3,3).Select()
            select.Font.ColorIndex = 11  # color is green
            select.TypeText('pass')
        elif len(Tx_table_fail_list) == 0 and len(Tx_table_pass_list)== 0:
            select1 = table1.Cell(3,3).Select()
            select.TypeText('Not test')

        if len(Mask_table_fail_list) != 0:
            select1 = table1.Cell(4,3).Select()
            select.Font.ColorIndex = 6  # color is red
            select.TypeText('fail')
        elif len(Mask_table_pass_list) ==len(detailed_word_test_item_vs_table_index_dic['Tx_Mask_Margin']):
            select1 = table1.Cell(4,3).Select()
            select.Font.ColorIndex = 11  # color is green
            select.TypeText('pass')
        elif len(Mask_table_pass_list) != 0 and len(Mask_table_none_list) == (len(detailed_word_test_item_vs_table_index_dic['Tx_Mask_Margin'])-len(Mask_table_pass_list)):
            select1 = table1.Cell(4,3).Select()
            select.Font.ColorIndex = 11  # color is green
            select.TypeText('pass')
        elif len(Mask_table_fail_list) == 0 and len(Mask_table_pass_list)== 0:
            select1 = table1.Cell(4,3).Select()
            select.TypeText('Not test')

        if len(Flatness_table_fail_list) != 0:
            select1 = table1.Cell(5,3).Select()
            select.Font.ColorIndex = 6  # color is red
            select.TypeText('fail')
        elif len(Flatness_table_pass_list) ==len(detailed_word_test_item_vs_table_index_dic['Tx_Flatness']):
            select1 = table1.Cell(5,3).Select()
            select.Font.ColorIndex = 11  # color is green
            select.TypeText('pass')
        elif len(Flatness_table_pass_list) != 0 and len(Flatness_table_none_list) == (len(detailed_word_test_item_vs_table_index_dic['Tx_Flatness'])-len(Flatness_table_pass_list)):
            select1 = table1.Cell(5,3).Select()
            select.Font.ColorIndex = 11  # color is green
            select.TypeText('pass')
        elif len(Flatness_table_fail_list) == 0 and len(Flatness_table_pass_list)== 0:
            select1 = table1.Cell(5,3).Select()
            select.TypeText('Not test')

        if len(Ramp_table_fail_list) != 0:
            select1 = table1.Cell(6,3).Select()
            select.Font.ColorIndex = 6  # color is red
            select.TypeText('fail')
        elif len(Ramp_table_pass_list) ==len(detailed_word_test_item_vs_table_index_dic['Tx_Ramp']):
            select1 = table1.Cell(6,3).Select()
            select.Font.ColorIndex = 11  # color is green
            select.TypeText('pass')
        elif len(Ramp_table_pass_list) != 0 and len(Ramp_table_none_list) == (len(detailed_word_test_item_vs_table_index_dic['Tx_Ramp'])-len(Ramp_table_pass_list)):
            select1 = table1.Cell(6,3).Select()
            select.Font.ColorIndex = 11  # color is green
            select.TypeText('pass')
        elif len(Ramp_table_fail_list) == 0 and len(Ramp_table_pass_list)== 0:
            select1 = table1.Cell(6,3).Select()
            select.TypeText('Not test')

##            if len(dr_table_fail_list) != 0:
##                select1 = table2.Cell(3,3).Select()
##                select.Font.ColorIndex = 6  # color is red
##                select.TypeText('fail')
##            elif len(dr_table_pass_list) ==len(detailed_word_test_item_vs_table_index_dic['Rx_DR']):
##                select1 = table2.Cell(3,3).Select()
##                select.Font.ColorIndex = 11  # color is green
##                select.TypeText('pass')
##            elif len(dr_table_pass_list) != 0 and len(dr_table_none_list) == (len(detailed_word_test_item_vs_table_index_dic['Rx_DR'])-len(dr_table_pass_list)):
##                select1 = table2.Cell(3,3).Select()
##                select.Font.ColorIndex = 11  # color is green
##                select.TypeText('pass')
##            elif len(dr_table_fail_list) == 0 and len(dr_table_pass_list)== 0:
##                select1 = table2.Cell(3,3).Select()
##                select.TypeText('Not test')

        if len(Rx_max_table_fail_list) != 0:
            select1 = table2.Cell(4,3).Select()
            select.Font.ColorIndex = 6  # color is red
            select.TypeText('fail')
        elif len(Rx_max_table_pass_list) ==len(detailed_word_test_item_vs_table_index_dic['Rx_Max']):
            select1 = table2.Cell(4,3).Select()
            select.Font.ColorIndex = 11  # color is green
            select.TypeText('pass')
        elif len(Rx_max_table_pass_list) != 0 and len(Rx_max_table_none_list) == (len(detailed_word_test_item_vs_table_index_dic['Rx_Max'])-len(Rx_max_table_pass_list)):
            select1 = table2.Cell(4,3).Select()
            select.Font.ColorIndex = 11  # color is green
            select.TypeText('pass')
        elif len(Rx_max_table_fail_list) == 0 and len(Rx_max_table_pass_list)== 0:
            select1 = table2.Cell(4,3).Select()
            select.TypeText('Not test')

        if len(Rx_sens_table_fail_list) != 0:
            select1 = table2.Cell(5,3).Select()
            select.Font.ColorIndex = 6  # color is red
            select.TypeText('fail')
        elif len(Rx_sens_table_pass_list) ==len(detailed_word_test_item_vs_table_index_dic['Rx_Sens']):
            select1 = table2.Cell(5,3).Select()
            select.Font.ColorIndex = 11  # color is green
            select.TypeText('pass')
        elif len(Rx_sens_table_pass_list) != 0 and len(Rx_sens_table_none_list) == (len(detailed_word_test_item_vs_table_index_dic['Rx_Sens'])-len(Rx_sens_table_pass_list)):
            select1 = table2.Cell(5,3).Select()
            select.Font.ColorIndex = 11  # color is green
            select.TypeText('pass')
        elif len(Rx_sens_table_fail_list) == 0 and len(Rx_sens_table_pass_list)== 0:
            select1 = table2.Cell(5,3).Select()
            select.TypeText('Not test')
        doc.Save()
        doc.Close()

    print #------------------------------test complete------------------------------#


##    def pass_or_fail_of_dr(self,dr_pass_vs_rate_dic={}):
##        keys_pass_list=list(dr_pass_vs_rate_dic.keys())
##        names=locals()
##        dr_table_fail_list=[]
##        dr_table_pass_list=[]
##        dr_table_none_list=[]
##        for mode in wifi_rate_vs_mode_dic:
##
##        	names['test_%s'%(mode)] = list(set(keys_pass_list) & set(wifi_rate_vs_mode_dic[mode]))
##        	if names['test_%s'%(mode)]==[]:
##        		names['flag_%s'%(mode)]=2
##        	else:
##        		for rate in names['test_%s'%(mode)]:
##        			if dr_pass_vs_rate_dic[rate]==0:
##        				names['flag_%s'%(mode)]=0
##        				break
##        			else:
##        				names['flag_%s'%(mode)]=1
##        	if names['flag_%s'%(mode)] == 2:
##        		dr_table_none_list.append(dr_table_vs_mode_dic[mode])
##        	elif names['flag_%s'%(mode)]==0:
##        		dr_table_fail_list.append(dr_table_vs_mode_dic[mode])
##        	elif names['flag_%s'%(mode)]==1:
##        		dr_table_pass_list.append(dr_table_vs_mode_dic[mode])
##
####        print dr_table_fail_list
####        print dr_table_pass_list
####        print dr_table_none_list
##        return dr_table_fail_list,dr_table_pass_list,dr_table_none_list




    def wifi_test_case(self,comment=''):

    	PATH = self.rf_wifi_autotest_data
        PATH_Script = "D:/chip/eagletest/py_script/rftest/test_script/wifi_autotest/"
    	filetime = time.strftime('_%Y%m%d_%H%M%S',time.localtime(time.time()));

    	test_case_file='Test_case_setting.xls'
    	[test_case,Module_Name,Sample_Number,Test_Bin,Cable_loss,Back_off,rf_port,test_information,test_case_channel_sel_dict] = self.Read_test_case(PATH_Script,test_case_file)

    	rf_crt_dic = self.Read_RF_Performance_Criterion(PATH_Script,test_case_file)

    	data_path = PATH+'%s'%(Module_Name)+filetime+'/'
    	os.mkdir(PATH+'%s'%(Module_Name)+filetime)

##    	path_report=PATH_Script+'/clean_report/Detailed_test/'+'/'
    	doc_file=PATH_Script+"\\ESP_ESP32U_A2_Test_Report_clean.docx"

    	wordapp = Dispatch('Word.Application')
    	wordapp.Visible = 1
    	doc = wordapp.Documents.Open(doc_file)
    	doc.SaveAs(data_path+"\\ESP_A2_Test_Report_%s_%s_%s%s.docx"%(Module_Name,Sample_Number,Test_Bin,filetime))
    	doc.Close()
    	doc = wordapp.Documents.Open(data_path+"\\ESP_A2_Test_Report_%s_%s_%s%s.docx"%(Module_Name,Sample_Number,Test_Bin,filetime))
    	select = wordapp.Selection
    	self.write_test_information_to_word(test_information,doc,select)

    	for i in range (0,len(test_case)):
    		case = test_case[i]
    		if case in ['TX_11m','TX_1m','TX_2m','TX_5.5m','TX_54m','TX_6m','TX_9m','TX_12m','TX_18m','TX_24m','TX_36m','TX_48m','TX_mcs7','TX_mcs0','TX_mcs1','TX_mcs2','TX_mcs3','TX_mcs4','TX_mcs5','TX_mcs6','TX_mcs7_40','TX_mcs0_40','TX_mcs1_40','TX_mcs2_40','TX_mcs3_40','TX_mcs4_40','TX_mcs5_40','TX_mcs6_40']:
    			self.TX_PWR_EVM_table_list(lost_list=Cable_loss, channel=test_case_channel_sel_dict[case], data_rate=Test_case_data_rate_dic[case], iqv_no=rf_port, iqv_num=20, doc=doc, select=select,rf_crt_dic=rf_crt_dic,comment=comment)
    		elif case in [ 'Mask_margin_1m','Mask_margin_6m','Mask_margin_mcs0','Mask_margin_mcs0_40']:
    			self.TX_spectrum_mask(lost_list=Cable_loss,channel=test_case_channel_sel_dict[case],data_rate=Test_case_data_rate_dic[case],iqv_no=rf_port,iqv_num=20, doc=doc, select=select,comment=comment)
    		elif case in ['Flatness_54m','Flatness_mcs7','Flatness_mcs7_40']:
    			self.TX_spectrum_flatness(lost_list=Cable_loss,channel=test_case_channel_sel_dict[case],data_rate=Test_case_data_rate_dic[case],iqv_no=rf_port,iqv_num=20, doc=doc, select=select)
    		elif case == 'TX_Ramp':
    			self.power_on_down_ramp_11b_1m(lost_list=Cable_loss,iqv_no=rf_port, iqv_num=10, doc=doc, select=select)
    		elif case in ['RX_DR_1m','RX_DR_2m','RX_DR_5.5m','RX_DR_11m','RX_DR_6m','RX_DR_9m','RX_DR_12m','RX_DR_18m','RX_DR_24m','RX_DR_36m','RX_DR_48m','RX_DR_54m','RX_DR_mcs0','RX_DR_mcs1','RX_DR_mcs2','RX_DR_mcs3','RX_DR_mcs4','RX_DR_mcs5','RX_DR_mcs6','RX_DR_mcs7','RX_DR_mcs0_40','RX_DR_mcs1_40','RX_DR_mcs2_40','RX_DR_mcs3_40','RX_DR_mcs4_40','RX_DR_mcs5_40','RX_DR_mcs6_40','RX_DR_mcs7_40']:
    			self.rx_dynamic_range_excel(lost_list=Cable_loss,channel=test_case_channel_sel_dict[case], data_rate=Test_case_data_rate_dic[case], packnum=100,iqv_no=rf_port,doc=doc, select=select,comment=comment)
    		elif case in ['RX_Max_1m','RX_Max_2m','RX_Max_5.5m','RX_Max_11m','RX_Max_6m','RX_Max_9m','RX_Max_12m','RX_Max_18m','RX_Max_24m','RX_Max_36m','RX_Max_48m','RX_Max_54m','RX_Max_mcs0','RX_Max_mcs1','RX_Max_mcs2','RX_Max_mcs3','RX_Max_mcs4','RX_Max_mcs5','RX_Max_mcs6','RX_Max_mcs7','RX_Max_mcs0_40','RX_Max_mcs1_40','RX_Max_mcs2_40','RX_Max_mcs3_40','RX_Max_mcs4_40','RX_Max_mcs5_40','RX_Max_mcs6_40','RX_Max_mcs7_40']:
    			self.rx_max_word(lost_list=Cable_loss,channel=test_case_channel_sel_dict[case],data_rate=Test_case_data_rate_dic[case], pwr_step=1, packnum=100, iqv_no=rf_port, doc=doc, select=select,comment=comment)
    		elif case in ['RX_Sens_1m','RX_Sens_2m','RX_Sens_5.5m','RX_Sens_11m','RX_Sens_6m','RX_Sens_9m','RX_Sens_12m','RX_Sens_18m','RX_Sens_24m','RX_Sens_36m','RX_Sens_48m','RX_Sens_54m','RX_Sens_mcs0','RX_Sens_mcs1','RX_Sens_mcs2','RX_Sens_mcs3','RX_Sens_mcs4','RX_Sens_mcs5','RX_Sens_mcs6','RX_Sens_mcs7','RX_Sens_mcs0_40','RX_Sens_mcs1_40','RX_Sens_mcs2_40','RX_Sens_mcs3_40','RX_Sens_mcs4_40','RX_Sens_mcs5_40','RX_Sens_mcs6_40','RX_Sens_mcs7_40']:
    			self.sensitivity_word(lost_list=Cable_loss,channel=test_case_channel_sel_dict[case],data_rate=Test_case_data_rate_dic[case], pwr_step=1, packnum=100, iqv_no=rf_port,doc=doc, select=select,comment=comment)
    		else:
    			print "error"

    	doc.Save()
    	doc.Close()

    	self.pass_or_fail_of_test_item_summary(data_path+"\\ESP_A2_Test_Report_%s_%s_%s%s.docx"%(Module_Name,Sample_Number,Test_Bin,filetime))

    	wordapp.DisplayAlerts = 1
    	doc = wordapp.Documents.Open(data_path+"\\ESP_A2_Test_Report_%s_%s_%s%s.docx"%(Module_Name,Sample_Number,Test_Bin,filetime))
    	doc.Save()
    	loginfo( "Running in export to PDF,please waiting about 5 seconds... ")
    	doc.ExportAsFixedFormat(data_path+"\\ESP_A2_Test_Report_%s_%s_%s%s.pdf"%(Module_Name,Sample_Number,Test_Bin,filetime), 17)
    	doc.Close()

    	print '\n\n----------test complete----------------\n'


