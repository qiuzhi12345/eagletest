#!/usr/bin/python
# -*- coding:utf8 -*-

import re
from baselib.loglib.log_lib import *
from baselib.plot import *
from baselib.instrument import *
import numpy as np
import pandas as pd
import scipy
from math import *
from shutil import copy
import time
import csv
import pylab
import matplotlib.pyplot as plt
from baselib.test_channel import *
import xlrd
import sys
import random
import os
from baselib.instrument.cmw_bt import *
from baselib.instrument.spa import *
from rftest.rflib import *
from hal.common import *
from rftest.rflib.csv_report import csvreport
from rftest.rflib import rfglobal

import serial
from sys import argv
import binascii
from binascii import b2a_hex, a2b_hex
import pylink
import docx
from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.enum.text import WD_TAB_ALIGNMENT,WD_TAB_LEADER #设置制表符等
from docx.shared import Inches #设置图像大小
from docx.shared import Pt #设置像素、缩进等
from docx.shared import RGBColor #设置字体颜色
from docx.shared import Length #设置宽度
import win32api
import shutil
class rf_diag_test(object):
    def __init__(self, comport, chipv='TX232_MPW3', jlink='59610138',jlink_en=1,board_name=''):
        self.comport = comport
        self.chipv = chipv
        self.mem_ts = MEM_TS(self.comport)
        self.board_name = board_name
        self.jlink_en = jlink_en
        if jlink_en != 0:
            self.jlink = jlink
    def bbpll_en(self, en=1):
        if en != 0:
            if self.chipv == 'TX232_MPW3':
                self.mem_ts.wrm(0xa00000a8, 1, 0, 1)
                self.mem_ts.wrm(0xa0000144, 25, 25, 1)  ##bbpll_bg_pup_ibg_bbpll
                self.mem_ts.wrm(0xa0000144, 29, 29, 1)  ##bbpll_bg_pup_ibg_tbuf
                self.mem_ts.wrm(0xa0000144, 20, 20, 1)  ##bbpll_bg_fc on
                self.mem_ts.wrm(0xa0000144, 22, 22, 1)  ##rf_aon_xo_en_clk_ana
                self.mem_ts.wrm(0xa0000144, 20, 20, 1)  ##rf_aon_xo_en_clk_ref
                self.mem_ts.wrm(0xa0000144, 23, 23, 1)  ##bbpll_ldo_pup
                self.mem_ts.wrm(0xa0000144, 22, 22, 1)  ##bbpll_pup
                self.mem_ts.wrm(0xa0000144, 21, 21, 0)  ##bbpll_ld_pd
                self.mem_ts.wrm(0xa0000144, 18, 18, 1)  ##bbpll_ldo_fc on
                self.mem_ts.wrm(0xa0000144, 17, 17, 1)  ##bbpll_vco_fast_en on

                ##wait 40us and end bbpll fast charge
                self.mem_ts.wrm(0xa0000144, 20, 20, 0)  ##bbpll_bg_fc off
                self.mem_ts.wrm(0xa0000144, 18, 18, 0)  ##bbpll_ldo_fc off
                self.mem_ts.wrm(0xa0000144, 17, 17, 0)  ##bbpll_vco_fast_en off
                self.mem_ts.wrm(0xa0000144, 16, 16, 1)  ##bbpll_ck_dig_en
                self.mem_ts.wrm(0xa0000144, 15, 15, 1)  ##bbpll_ck_codec_en
            else:
                self.mem_ts.wrm(0xa01200a0, 25, 25, 1)  ##bbpll_bg_pup_ibg
                self.mem_ts.wrm(0xa01200a0, 29, 29, 1)  ##bbpll_bg_pup_ibg_tbuf
                self.mem_ts.wrm(0xa01200a0, 20, 20, 1)  ##bbpll_bg_fc on
                self.mem_ts.wrm(0xa01200cc, 22, 22, 1)  ##rf_aon_xo_en_clk_ana
                self.mem_ts.wrm(0xa01200cc, 20, 20, 1)  ##rf_aon_xo_en_clk_ref
                self.mem_ts.wrm(0xa01200a0, 23, 23, 1)  ##bbpll_ldo_pup
                self.mem_ts.wrm(0xa01200a0, 22, 22, 1)  ##bbpll_pup
                self.mem_ts.wrm(0xa01200a0, 21, 21, 0)  ##bbpll_ld_pd
                self.mem_ts.wrm(0xa01200a0, 18, 18, 1)  ##bbpll_ldo_fc on
                self.mem_ts.wrm(0xa01200a0, 17, 17, 1)  ##bbpll_vco_fast_en on

                ##wait 40us and end bbpll fast charge
                self.mem_ts.wrm(0xa01200a0, 20, 20, 0)  ##bbpll_bg_fc off
                self.mem_ts.wrm(0xa01200a0, 18, 18, 0)  ##bbpll_ldo_fc off
                self.mem_ts.wrm(0xa01200a0, 17, 17, 0)  ##bbpll_vco_fast_en off
                self.mem_ts.wrm(0xa01200a0, 16, 16, 1)  ##bbpll_ck_dig_en
                self.mem_ts.wrm(0xa01200a0, 15, 15, 1)  ##bbpll_ck_codec_en
        else:
            if self.chipv == 'TX232_MPW3':
                self.mem_ts.wrm(0xa0000144, 23, 23, 0)  ##bbpll_ldo_pup
                self.mem_ts.wrm(0xa0000144, 22, 22, 0)  ##bbpll_pup
            else:
                self.mem_ts.wrm(0xa01200a0, 23, 23, 0)  ##bbpll_ldo_pup
                self.mem_ts.wrm(0xa01200a0, 22, 22, 0)  ##bbpll_pup

    def bbpll_diag(self, mode=0, diag_code=1):
        '''
        mode    0:  bbpll ck test
                1:  bbpll locked voltage test
                2:  bbpll ldo output test
        diag_code is useful for mode2
        '''
        self.bbpll_en(1)
        if self.chipv == 'TX232_MPW3':
            self.mem_ts.wrm(0xa0000148, 0, 0, 0)  ##bbpll_ck6p144m_test_en
            self.mem_ts.wrm(0xa0000148, 3, 3, 0)  ##bbpll_ck_test_en
            self.mem_ts.wrm(0xa0000148, 1, 1, 0)  ##bbpll_vctl_test_en
            self.mem_ts.wrm(0xa0000148, 2, 2, 0)  ##bbpll_dc_test_en
            self.mem_ts.wrm(0xa0000148, 7, 7, 0)  ##bbpll_ldo_diag_sel
            self.mem_ts.wrm(0xa0000148, 6, 4, 0)  ##bbpll_diag_code
            if mode == 0:
                self.mem_ts.wrm(0xa0000148, 0, 0, 1)  ##bbpll_ck6p144m_test_en
                self.mem_ts.wrm(0xa0000148, 3, 3, 1)  ##bbpll_ck_test_en
            elif mode == 1:
                self.mem_ts.wrm(0xa0000148, 1, 1, 1)  ##bbpll_vctl_test_en
                self.mem_ts.wrm(0xa0000148, 2, 2, 1)  ##bbpll_dc_test_en
            else:
                self.mem_ts.wrm(0xa0000148, 7, 7, 1)  ##bbpll_ldo_diag_sel
                self.mem_ts.wrm(0xa0000148, 6, 4, diag_code)  ##bbpll_diag_code
        else:
            self.mem_ts.wrm(0xa01200e0, 0, 0, 0)  ##bbpll_ck6p144m_test_en
            self.mem_ts.wrm(0xa01200e0, 11, 11, 0)  ##bbpll_ck_test_en
            self.mem_ts.wrm(0xa01200e0, 1, 1, 0)  ##bbpll_vctl_test_en
            self.mem_ts.wrm(0xa01200e0, 10, 10, 0)  ##bbpll_dc_test_en
            self.mem_ts.wrm(0xa01200e0, 16, 16, 0)  ##bbpll_ldo_diag_sel
            self.mem_ts.wrm(0xa01200e0, 15, 13, 0)  ##bbpll_diag_code
            if mode == 0:
                self.mem_ts.wrm(0xa01200e0, 0, 0, 1)  ##bbpll_ck6p144m_test_en
                self.mem_ts.wrm(0xa01200e0, 11, 11, 1)  ##bbpll_ck_test_en
            elif mode == 1:
                self.mem_ts.wrm(0xa01200e0, 1, 1, 1)  ##bbpll_vctl_test_en
                self.mem_ts.wrm(0xa01200e0, 10, 10, 1)  ##bbpll_dc_test_en
            else:
                self.mem_ts.wrm(0xa01200e0, 16, 16, 1)  ##bbpll_ldo_diag_sel
                self.mem_ts.wrm(0xa01200e0, 15, 13, diag_code)  ##bbpll_diag_code

    def ldo_bbpll_trim_diag(self, device_name='MY50180049'):
        title = 'bbpll_bg_trim,ldo_bbpll_trim,diag_code,volt(v)\n'
        fname = rfglobal.get_filename('ts_bt_test/', 'test232_ldo_bbpll_trim_diag_{}'.format(self.board_name))
        fw1 = csvreport(fname, title)
        mydm = dm.dm(device_name=device_name, num_of_machine=0, comm='USB')
        self.bbpll_en(1)
        self.bbpll_diag(2, 1)
        if self.chipv == 'TX232_MPW3':
            init_value = self.mem_ts.rdm(0xa0000144, 14, 12)
            bg_trim_init = self.mem_ts.rdm(0xa01200c8, 7, 5)
            for bg_trim in range(8):
                self.mem_ts.wrm(0xa01200c8, 7, 5, bg_trim)
                for value in range(0, 8):
                    self.mem_ts.wrm(0xa0000144, 14, 12, value)
                    for diag_code in range(1, 2):
                        # for diag_code in range(1, 8):
                        self.mem_ts.wrm(0xa0000148, 6, 4, diag_code)
                        time.sleep(0.2)
                        dd = mydm.device.ask('MEAS:VOLT? 10, 0.0001')
                        res = eval(dd)

                        loginfo('ldo_bbpll_trim:{}     diag_code:{}       volt:{}'.format(value, diag_code, res))
                        fw1.write_data([bg_trim, value, diag_code, res], float_num=4)
            self.mem_ts.wrm(0xa0000144, 14, 12, init_value)
            self.mem_ts.wrm(0xa01200c8, 7, 5, bg_trim_init)
        else:
            init_value = self.mem_ts.rdm(0xa01200a0, 13, 12)
            bg_trim_init = self.mem_ts.rdm(0xa01200a0, 11, 9)
            for bg_trim in range(8):
                self.mem_ts.wrm(0xa01200a0, 11, 9, bg_trim)
                for value in range(0, 4):
                    self.mem_ts.wrm(0xa01200a0, 13, 12, value)
                    for diag_code in range(1, 8):
                        self.mem_ts.wrm(0xa01200e0, 15, 13, diag_code)
                        time.sleep(5)
                        dd = mydm.device.ask('MEAS:VOLT? 10, 0.0001')
                        res = eval(dd)

                        loginfo('ldo_bbpll_trim:{}     diag_code:{}       volt:{}'.format(value, diag_code, res))
                        fw1.write_data([bg_trim, value, diag_code, res], float_num=4)
            self.mem_ts.wrm(0xa01200a0, 13, 12, init_value)
            self.mem_ts.wrm(0xa01200a0, 11, 9, bg_trim_init)

    def rf_diag(self, mode=0, diag_code=1):
        '''
        mode    2:  xo diag select
                3:  xo LDO diag select
                4:  Bandgap diag select
                5:  LV LDO diag select
                6:  TRXHF LDO diag select
                7:  TRXLF LDO diag select
                8:  PLL LDO diag select
                9:  VCO LDO diag select
                10:  Rx LNA diag select
                11:  Rx CBPF diag select
                12:  Tx PA diag select
                13:  Tx Mixer diag select
                14:  Tx LPF diag select
                15:  Tx DAC diag select
                16:  PLL diag select
        diag_code
        '''
        diag_dic = {
            2: 'xo diag select',
            3: 'xo LDO diag select',
            4: 'Bandgap diag select',
            5: 'LV LDO diag select',
            6: 'TRXHF LDO diag select',
            7: 'TRXLF LDO diag select',
            8: 'PLL LDO diag select',
            9: 'VCO LDO diag select',
            10: 'Rx LNA diag select',
            11: 'Rx CBPF diag select',
            12: 'Tx PA diag select',
            13: 'Tx Mixer diag select',
            14: 'Tx LPF diag select',
            15: 'Tx DAC diag select',
            16: 'PLL diag select',
            }
        self.mem_ts.wrm(0xa0421024, 17, 17, 1)  ##RF diag  soc enable
        self.mem_ts.wrm(0xa0421024, 3, 3, 0)  ##RF diag  enable
        self.mem_ts.wrm(0xa0421024, 16, 4, 0)
        self.mem_ts.wrm(0xa01200cc, 3, 2, 0)
        if mode < 4:
            self.mem_ts.wrm(0xa01200cc, mode, mode, 1)
        else:
            self.mem_ts.wrm(0xa0421024, mode, mode, 1)
        self.mem_ts.wrm(0xa0421024, 2, 0, diag_code)  ##RF diag code select
        loginfo("{}     diag code:  {}".format(diag_dic[mode], diag_code))

    def pkd_trim_diag(self, device_name='MY49260023', cableloss=1.5):
        title = 'pkd_ref,VDD,VREF(V),VREF1(V),VREF2(V)\n'
        fname = rfglobal.get_filename('ts_bt_test/', 'test232_pkd_trim_diag{}'.format(self.board_name))
        fw1 = csvreport(fname, title)
        mydm = dm.dm(device_name=device_name, num_of_machine=0, comm='USB')
        init_value = self.mem_ts.rdm(0xa0421028, 25, 19)

        self.mem_ts.wrm(0xa0421024, 3, 3, 0)
        self.mem_ts.wrm(0xa0421024, 17, 17, 1)
        self.mem_ts.wrm(0xa0421028, 31, 31, 1)  ##diag select pkd
        self.mem_ts.wrm(0xa0422014, 7, 0, 0x3)  ##rxon enable

        for value in range(0, 2 ** 7):
            self.mem_ts.wrm(0xa0421028, 25, 19, value)
            res_list = []
            for diag_code in [2, 4, 5, 6]:
                self.mem_ts.wrm(0xa0421024, 2, 0, diag_code)
                time.sleep(2)
                dd = mydm.device.ask('MEAS:VOLT? 10, 0.0001')
                res = eval(dd)
                res_list.append(res)

                loginfo('pkd_ref:{}     diag_code:{}       volt:{}'.format(value, diag_code, res))
            fw1.write_data([value] + res_list, float_num=4)
        self.mem_ts.wrm(0xa0421028, 25, 19, init_value)

        fw1.write_string('pkd_ref,rx_gain_index,input_level(dbm),VIN(V)\n')
        txg = mxg.MXG()
        # txg.arb_waveform(rate='LE_1M')
        txg.trriger_para_set(type='CONTinuous', count=1000)
        txg.output_state(1, 0)
        # txg.arb_state(1)
        txg.set_cfreq(2475)
        self.mem_ts.wrm(0xa0421064, 12, 12, 1)
        self.mem_ts.wrm(0xa0421064, 11, 0, 2475)  ##set freq
        self.mem_ts.wrm(0xa04210A0, 0, 0, 0x1)  ##AGC OFF
        pkd_ref = self.mem_ts.rdm(0xa0421028, 25, 19)
        rx_gain_index = self.mem_ts.rdm(0xa04210a0, 20, 17)
        self.mem_ts.wrm(0xa0421024, 2, 0, 3)
        for rxlevel in range(-990, 10, 5):
            self.mem_ts.wrm(0xa0422014, 7, 0, 0x0)
            txg.set_power(rxlevel / 10.0 + cableloss)
            time.sleep(0.2)
            self.mem_ts.wrm(0xa0422014, 7, 0, 0x3)
            dd = mydm.device.ask('MEAS:VOLT? 10, 0.0001')
            res = eval(dd)
            loginfo('pkd_ref:{}     rx_gain_index:{}   rxlevel:{}    VIN:{}'.format(pkd_ref, rx_gain_index, rxlevel, res))
            fw1.write_data([pkd_ref, rx_gain_index, rxlevel, res], float_num=4)

        self.mem_ts.wrm(0xa04210A0, 0, 0, 0x0)  ##AGC ON
        self.mem_ts.wrm(0xa0421064, 12, 12, 0)  ##freq auto
        self.mem_ts.wrm(0xa0422014, 7, 0, 0x0)

    def bg_trim_diag(self):
        title = 'bg_trim,diag_code,volt(v)\n'
        fname = rfglobal.get_filename('ts_bt_test/', 'test232_bg_trim_diag_{}'.format(self.board_name))
        fw1 = csvreport(fname, title)
        mydm = dm.dm(device_name='MY50180049', num_of_machine=0, comm='USB')
        self.rf_diag(4, 1)
        init_value = self.mem_ts.rdm(0xa0421028, 2, 0)
        self.mem_ts.wr(0xa0422014, 0x3)
        for value in range(0, 8):
            self.mem_ts.wrm(0xa0421028, 2, 0, value)
            for diag_code in range(1, 8):
                self.mem_ts.wrm(0xa0421024, 2, 0, diag_code)
                time.sleep(5)
                dd = mydm.device.ask('MEAS:VOLT? 10, 0.0001')
                res = eval(dd)

                loginfo('bg trim:{}     diag_code:{}       volt:{}'.format(value, diag_code, res))
                fw1.write_data([value, diag_code, res], float_num=4)
        self.mem_ts.wrm(0xa0421028, 2, 0, init_value)
        self.mem_ts.wr(0xa0422014, 0x0)

    def ldo_trxhf_trim_diag(self):
        title = 'ldo_trxhf_trim,diag_code,volt(v)\n'
        fname = rfglobal.get_filename('ts_bt_test/', 'test232_ldo_trxhf_trim_diag_{}'.format(self.board_name))
        fw1 = csvreport(fname, title)
        mydm = dm.dm(device_name='MY50180049', num_of_machine=0, comm='USB')
        self.rf_diag(6, 1)
        init_value = self.mem_ts.rdm(0xa0421028, 7, 6)
        self.mem_ts.wr(0xa0422014, 0x3)
        for value in range(0, 4):
            self.mem_ts.wrm(0xa0421028, 7, 6, value)
            for diag_code in range(1, 8):
                self.mem_ts.wrm(0xa0421024, 2, 0, diag_code)
                time.sleep(5)
                dd = mydm.device.ask('MEAS:VOLT? 10, 0.0001')
                res = eval(dd)

                loginfo('ldo_trxhf_trim:{}     diag_code:{}       volt:{}'.format(value, diag_code, res))
                fw1.write_data([value, diag_code, res], float_num=4)
        self.mem_ts.wrm(0xa0421028, 7, 6, init_value)
        self.mem_ts.wr(0xa0422014, 0x0)

    def ldo_trxlf_trim_diag(self):
        title = 'ldo_trxlf_trim,diag_code,volt(v)\n'
        fname = rfglobal.get_filename('ts_bt_test/', 'test232_ldo_trxlf_trim_diag_{}'.format(self.board_name))
        fw1 = csvreport(fname, title)
        mydm = dm.dm(device_name='MY50180049', num_of_machine=0, comm='USB')
        self.rf_diag(7, 1)
        init_value = self.mem_ts.rdm(0xa0421034, 26, 24)
        self.mem_ts.wr(0xa0422014, 0x3)
        for value in [0, 1, 3, 7]:
            self.mem_ts.wrm(0xa0421034, 26, 24, value)
            for diag_code in [1]:
                self.mem_ts.wrm(0xa0421024, 2, 0, diag_code)
                time.sleep(5)
                dd = mydm.device.ask('MEAS:VOLT? 10, 0.0001')
                res = eval(dd)

                loginfo('ldo_trxlf_trim:{}     diag_code:{}       volt:{}'.format(value, diag_code, res))
                fw1.write_data([value, diag_code, res], float_num=4)
        self.mem_ts.wrm(0xa0421034, 26, 24, init_value)
        self.mem_ts.wr(0xa0422014, 0x0)

    def ldo_rfpll_trim_diag(self):
        title = 'ldo_rfpll_trim,diag_code,volt(v)\n'
        fname = rfglobal.get_filename('ts_bt_test/', 'test232_ldo_rfpll_trim_diag_{}'.format(self.board_name))
        fw1 = csvreport(fname, title)
        mydm = dm.dm(device_name='MY50180049', num_of_machine=0, comm='USB')
        self.trf_diag(8, 1)
        init_value = self.mem_ts.rdm(0xa0421028, 12, 11)
        self.mem_ts.wr(0xa0422014, 0x3)
        for value in range(0, 4):
            self.mem_ts.wrm(0xa0421028, 12, 11, value)
            for diag_code in range(1, 8):
                self.mem_ts.wrm(0xa0421024, 2, 0, diag_code)
                time.sleep(5)
                dd = mydm.device.ask('MEAS:VOLT? 10, 0.0001')
                res = eval(dd)

                loginfo('ldo_rfpll_trim:{}     diag_code:{}       volt:{}'.format(value, diag_code, res))
                fw1.write_data([value, diag_code, res], float_num=4)
        self.mem_ts.wrm(0xa0421028, 12, 11, init_value)
        self.mem_ts.wr(0xa0422014, 0x0)

    def ldo_vco_trim_diag(self):
        title = 'ldo_vco_trim,diag_code,volt(v)\n'
        fname = rfglobal.get_filename('ts_bt_test/', 'test232_ldo_vco_trim_diag_{}'.format(self.board_name))
        fw1 = csvreport(fname, title)
        mydm = dm.dm(device_name='MY50180049', num_of_machine=0, comm='USB')
        self.rf_diag(9, 1)
        init_value = self.mem_ts.rdm(0xa0421028, 15, 14)
        self.mem_ts.wr(0xa0422014, 0x3)
        for value in range(0, 4):
            self.mem_ts.wrm(0xa0421028, 15, 14, value)
            for diag_code in range(1, 8):
                self.mem_ts.wrm(0xa0421024, 2, 0, diag_code)
                time.sleep(5)
                dd = mydm.device.ask('MEAS:VOLT? 10, 0.0001')
                res = eval(dd)

                loginfo('ldo_vco_trim:{}     diag_code:{}       volt:{}'.format(value, diag_code, res))
                fw1.write_data([value, diag_code, res], float_num=4)
        self.mem_ts.wrm(0xa0421028, 15, 14, init_value)
        self.mem_ts.wr(0xa0422014, 0x0)

    def ldo_xo_trim_diag(self, device_name='MY50180049'):
        '''
        TX232_MPW3 xo使用bbpll bg，MPW2使用的是rfpll bg
        '''
        title = 'bg_trim,ldo_xo_trim,diag_code,volt(v)\n'
        fname = rfglobal.get_filename('ts_bt_test/', 'test232_ldo_xo_trim_diag_{}'.format(self.board_name))
        fw1 = csvreport(fname, title)
        mydm = dm.dm(device_name=device_name, num_of_machine=0, comm='USB')
        self.rf_diag(3, 1)
        init_value = self.mem_ts.rdm(0xa01200cc, 5, 4)
        if self.chipv == 'TX232_MPW3':
            bg_trim_init = self.mem_ts.rdm(0xa01200c8, 7, 5)
        else:
            bg_trim_init = self.mem_ts.rdm(0xa0421028, 2, 0)
        self.mem_ts.wr(0xa0422014, 0x3)
        for bg_trim in range(8):
            if self.chipv == 'TX232_MPW3':
                self.mem_ts.wrm(0xa01200c8, 7, 5, bg_trim)
            else:
                self.mem_ts.wrm(0xa0421028, 2, 0, bg_trim)
            for value in range(0, 4):
                self.mem_ts.wrm(0xa01200cc, 5, 4, value)
                for diag_code in range(1, 6):
                    self.mem_ts.wrm(0xa0421024, 2, 0, diag_code)
                    time.sleep(0.2)
                    dd = mydm.device.ask('MEAS:VOLT? 10, 0.001')
                    res = eval(dd)

                    loginfo('ldo xo trim:{}     diag_code:{}       volt:{}'.format(value, diag_code, res))
                    fw1.write_data([bg_trim, value, diag_code, res], float_num=4)
        self.mem_ts.wrm(0xa01200cc, 5, 4, init_value)
        if self.chipv == 'TX232_MPW3':
            bg_trim_init = self.mem_ts.wrm(0xa01200c8, 7, 5, bg_trim_init)
        else:
            bg_trim_init = self.mem_ts.wrm(0xa0421028, 2, 0, bg_trim_init)
        self.mem_ts.wr(0xa0422014, 0x0)

    def rf_ldo_trim_diag(self, device_name='MY50180049'):
        ldo_diag_dic = {
            # 3:  'LDO_XO',
            # 4:  'Bandgap',
            5: 'LDO_LV',
            6: 'LDO_TRXHF',
            7: 'LDO_TRXLF',
            8: 'LDO_PLL',
            9: 'LDO_VCO',
            }
        ldo_trim_dic = {
            # 3: '0xa01200cc 5 4',
            # 4: '0xa0421028 2 0',
            5: '0xa0421028 4 4',
            6: '0xa0421028 7 6',
            7: '0xa0421034 26 24',
            8: '0xa0421028 12 11',
            9: '0xa0421028 15 14',
            }
        title = 'item,bg_trim,trim value,diag_code,volt(v)\n'
        fname = rfglobal.get_filename('ts_bt_test/', 'test232_rf_ldo_trim_diag_{}'.format(self.board_name))
        fw1 = csvreport(fname, title)
        mydm = dm.dm(device_name=device_name, num_of_machine=0, comm='USB')
        bg_trim_init = self.mem_ts.rdm(0xa0421028, 2, 0)
        self.mem_ts.wr(0xa0422014, 0x3)
        for val in range(5, 10):
            self.rf_diag(val, 1)
            ldo_type = ldo_diag_dic[val]
            ldo_trim_str = ldo_trim_dic[val]
            ldo_trim_strr = ldo_trim_str.split()
            ldo_trim_reg_addr = eval(ldo_trim_strr[0])
            ldo_trim_reg_msb = eval(ldo_trim_strr[1])
            ldo_trim_reg_lsb = eval(ldo_trim_strr[2])
            init_value = self.mem_ts.rdm(ldo_trim_reg_addr, ldo_trim_reg_msb, ldo_trim_reg_lsb)
            for bg_trim in range(8):
                self.mem_ts.wrm(0xa0421028, 2, 0, bg_trim)
                for trim_value in range(0, 2 ** (ldo_trim_reg_msb - ldo_trim_reg_lsb + 1)):
                    self.mem_ts.wrm(ldo_trim_reg_addr, ldo_trim_reg_msb, ldo_trim_reg_lsb, trim_value)
                    for diag_code in range(1, 2):
                        # for diag_code in range(1, 8):
                        self.mem_ts.wrm(0xa0421024, 2, 0, diag_code)
                        time.sleep(0.2)
                        dd = mydm.device.ask('MEAS:VOLT? 10, 0.001')
                        res = eval(dd)

                        loginfo('{} trim     trim_value:{}       volt:{}'.format(ldo_type, trim_value, res))
                        fw1.write_data([ldo_type, bg_trim, trim_value, diag_code, res], float_num=4)
            self.mem_ts.wrm(ldo_trim_reg_addr, ldo_trim_reg_msb, ldo_trim_reg_lsb, init_value)
        self.mem_ts.wr(0xa0422014, 0x0)

        # self.test232_ldo_bbpll_trim_diag(device_name=device_name)
        self.ldo_xo_trim_diag(device_name=device_name)

    def rfpll_vtune(self):
        title = 'freq(MHz),rfpll_vtune(v)\n'
        fname = rfglobal.get_filename('ts_bt_test/', 'test232_rfpll_vtune')
        fw1 = csvreport(fname, title)
        mydm = dm.dm(device_name='MY50180049', num_of_machine=0, comm='USB')
        # self.mem_ts.wrm(0xa0421024, 17, 17, 1)  ##RF diag  soc enable
        # self.mem_ts.wrm(0xa0421024, 16, 16, 1)  ##RF PLL diag select
        # self.mem_ts.wrm(0xa0421024, 3, 3, 0)  ##RF diag  enable
        # self.mem_ts.wrm(0xa0421024, 2, 0, 1)  ##RF diag code select
        self.rf_diag(16, 1)
        self.mem_ts.wrm(0xa0421064, 12, 12, 1)  ##Frequency value manual enable
        for channel in range(0, 79):
            self.mem_ts.wrm(0xa0421064, 11, 0, 2402 + channel)
            self.mem_ts.wr(0xa0422014, 0x0)
            time.sleep(2)
            self.mem_ts.wr(0xa0422014, 0xe)
            time.sleep(5)
            dd = mydm.device.ask('MEAS:VOLT?')
            res = eval(dd)

            loginfo('channel:{}     vtune:{}'.format(channel, res))
            fw1.write_data([channel, res], float_num=4)

    def rf_buf(self, mode='rx'):
        self.mem_ts.wrm(0xa0120038, 11, 8, 0)
        self.mem_ts.wrm(0xa012005c, 31, 16, 0)  ##
        self.mem_ts.wrm(0xa0120060, 7, 0, 0)  ##PC8/9/10/11 高阻
        self.mem_ts.wrm(0xa01200a0, 29, 29, 1)  ##bbpll_bg_pup_ibg_tbuf
        self.mem_ts.wrm(0xa01200c8, 4, 4, 1)  ##test buf en
        if mode == 'tx':
            self.mem_ts.wrm(0xa01200c8, 3, 2, 2)  ##tx IF test buf
        else:
            self.mem_ts.wrm(0xa01200c8, 3, 2, 1)  ##rx IF test buf

