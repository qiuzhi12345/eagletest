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
class bt_api(object):
    def __init__(self, comport, chipv='TX232_MPW3', jlink='59610138',jlink_en=1,board_name=''):
        self.comport = comport
        self.chipv = chipv
        self.mem_ts = MEM_TS(self.comport)
        self.board_name = board_name
        # self.jlink = jlink
        self.jlink_en = jlink_en
        if jlink_en !=0:
            self.jlink = jlink

        self.br_len_dic = {
            'DH1': 27,
            'DH3': 183,
            'DH5': 339
        }
        self.br_rate_dic = {
            'DH1': 1,
            'DH3': 4,
            'DH5': 7
        }
        self.edr_len_dic = {
            '2_DH1': 31,
            '2_DH3': 356,
            '2_DH5': 656,
            '3_DH1': 83,
            '3_DH3': 552,
            '3_DH5': 1021,
        }
        self.edr_rate_dic = {
            '2_DH1': 2,
            '2_DH3': 5,
            '2_DH5': 8,
            '3_DH1': 3,
            '3_DH3': 6,
            '3_DH5': 9,
        }
        self.le_rate_dic = {
            'LE1M': 1,
            'LE2M': 2,
            'LE500k': 3,
            'LE125K': 4
        }

    def hci_reset(self):
        self.comport.req_com(cmdstr='\x01\x03\x0c\x00',timeout=1,endstr='TS')

    def hci_read_buffer_size(self):
        self.comport.req_com(cmdstr='\x01\x05\x10\x00', timeout=1, endstr='TS')

    def hci_enable_under_test_mode(self):
        self.comport.req_com(cmdstr='\x01\x03\x18\x00', timeout=1, endstr='TS')

    def hci_enable_write_both_scan(self):
        self.comport.req_com(cmdstr='\x01\x1a\x0c\x01\x03', timeout=1, endstr='TS')

    def hci_disable_write_both_scan(self):
        self.comport.req_com(cmdstr='\x01\x1a\x0c\x01\x00', timeout=1, endstr='TS')

    def hci_auto_accept_all_connection(self):
        self.comport.req_com(cmdstr='\x01\x05\x0c\x03\x02\x00\x02', timeout=1, endstr='TS')

    def dut_signal_mode_set(self):

        res = self.comport.req_com(cmdstr='signaltest', wr_end='\r\n', timeout=5)
        logdebug(res)
        if res.find('signal test')!=-1:
            self.comport.Hexmd = 1
            self.hci_reset()
            self.hci_read_buffer_size()
            self.hci_enable_under_test_mode()
            self.hci_enable_write_both_scan()
            self.hci_auto_accept_all_connection()
            self.comport.Hexmd = 0
        else:
            logwarn('can not enter signal test mode')

    def BT_INIT(self, rate='LE1M'):
        if rate not in ['BR','EDR','LE1M','LE2M','LELR']:
            logerror('rate is wrong,must be BR,EDR,LE1M,LE2M,LELR ')
            return False
        self.mem_ts.wr(0xa0421004, 0x37)
        self.mem_ts.wr(0xa04210f8, 0x2f0fd2c)
        if rate == 'LE1M':
            self.mem_ts.wrm(0xa0400880,7,0,0X40)
            self.mem_ts.wr(0xa01200c8, 0x1802f0)
        elif rate == 'LE2M':
            self.mem_ts.wrm(0xa0400884,7,0,0X40)


    def LE_TX(self, chan=0, len=37, ptype=2, phy=2):
        '''
        chan:   0--39
        len:    1--255
        ptype:    0 ->PSEUDO_RAND_9; 1 ->11110000; 2->10101010; 3->PSEUDO_RAND_15
                4 ->11111111;      5 ->00000000; 6->00001111; 7->01010101
        phy:    1 ->1M; 2 ->2M; 3->coded S=8; 4->coded S=2
        '''
        if chan < 0 or chan > 39:
            logerror(' le channel is out of range')
            return False
        if len < 1 or len > 255:
            logerror('le packet lenght is out of range')
            return False
        # if phy == 2:
        #     self.mem_ts.wr(0xa04200e4, 0x9d8a)  ##GFSK modulation index for BLE mode
        # self.comport.req_com("bletx ch=%d len=%d pay=%d phy=%d" %(chan, len, ptype, phy), wr_end='\r\n', timeout=5)
        self.cmdstop(0)
        self.cmdstop(1)
        for i in range(5):
            res = self.comport.req_com("bletx ch=%d len=%d pay=%d phy=%d" %(chan, len, ptype, phy), wr_end='\r\n', timeout=5)
            if res.find("bletx ch=%d len=%d pay=%d phy=%d" %(chan, len, ptype, phy)) != -1:
                logdebug('le tx ok')
                break
            i = i+1
            self.cmdstop(0)
            logwarn('cmd return error')
        # self.mem_ts.wrm(0xa04210bc, 28, 26, 7)  ##bt_padrv_gain_table_gfsk_0
        # self.mem_ts.wrm(0xa04210c0, 28, 26, 7)  ##bt_padrv_gain_table_gfsk_1
        # self.mem_ts.wrm(0xa04210b4, 28, 26, 7)  ##bt_padrv_gain_table_dpsk_0
        # self.mem_ts.wrm(0xa04210b8, 28, 26, 7)
        # # self.mem_ts.wr(0xa01200c8, 0x1c02f5)
        # self.mem_ts.wr(0xa0421088, 0x00408411)  ##PA on
        # self.mem_ts.wr(0xa01200c8, 0x0018807A)  ##xtal
        # self.mem_ts.wr(0xa01200cc, 0x00000034)  ##xtal
        # self.mem_ts.wr(0xa0421024, 0x00000F07)  ##bt_padrv_setting
        # self.mem_ts.wr(0xa0421064, 0x0311FA80)  ##vco_pkd
        time.sleep(0.5)


    def BR_TX(self, chan=0, len=37, ptype=2, rate=2):
        '''
        chan:       0--78
        len:        1--1021
                    lenMax: (DH1)->27;    (2-DH1)->54;  (3-DH1)->83
                    (DH3)->183;   (2-DH3)->367; (3-DH3)->552
                    (DH5)->339;   (2-DH5)->679; (3-DH5)->1021
        ptype:      1 ->11110000; 2->10101010;  3->11111111
                    4 ->00000000; 5->00001111;  6->01010101
        type:       1 ->(DH1);    2 ->(2-DH1);  3->(3-DH1);
                    4 ->(DH3);    5 ->(2-DH3);  6->(3-DH3);
                    7 ->(DH5);    8 ->(2-DH5);  9->(3-DH5);
        '''
        self.cmdstop(1)
        self.cmdstop(0)
        if chan < 0 or chan > 78:
            logerror(' BT channel is out of range')
            return False
        if len < 1 or len > 1021:
            logerror('BT packet lenght is out of range')
            return False
        for i in range(5):
            res = self.comport.req_com("bttx ch=%d len=%d pay=%d type=%d" %(chan, len, ptype, rate), wr_end='\r\n', timeout=5)
            if res.find("bttx ch=%d len=%d pay=%d type=%d" %(chan, len, ptype, rate)) != -1:
                logdebug('bt tx ok')
                break
            i = i+1
            self.cmdstop(1)
            logwarn('cmd return error')

        # if rate in [1, 4, 7]:
        #     self.mem_ts.wrm(0xa04210bc, 28, 26, 7)  ##bt_padrv_gain_table_gfsk_0
        #     self.mem_ts.wrm(0xa04210c0, 28, 26, 7) ##bt_padrv_gain_table_gfsk_1
        #     self.mem_ts.wrm(0xa04210b4, 28, 26, 7)  ##bt_padrv_gain_table_dpsk_0
        #     self.mem_ts.wrm(0xa04210b8, 28, 26, 7)
        # # self.mem_ts.wr(0xa01200c8,0x1c02f5)
        # self.mem_ts.wr(0xa0421088, 0x00408411)  ##PA on
        # self.mem_ts.wr(0xa01200c8, 0x0018807A)  ##xtal
        # self.mem_ts.wr(0xa01200cc, 0x00000034)  ##xtal
        # self.mem_ts.wr(0xa0421024, 0x00000F07)  ##bt_padrv_setting
        # self.mem_ts.wr(0xa0421064, 0x0311FA80)  ##vco_pkd

        # self.mem_ts.wrm(0xa0421098, 12, 10, 7)  ##Manual Tx Mixer gain setting
        # self.mem_ts.wrm(0xa0421094, 11, 10, 3)
        # self.mem_ts.wrm(0xa01200cc, 14, 11, 1)

    def BR_RX(self, chan=0, len=27, ptype=5, rate=1, ltaddr=1, uap=0x48, lap=0x000080):
        if chan < 0 or chan > 78:
            logerror(' BT channel is out of range')
            return False
        if len < 1 or len > 1021:
            logerror('BT packet length is out of range')
            return False
        if ptype < 1 or ptype > 6:
            logerror('BT packet paytype is out of range')
            return False
        self.comport.req_com("btrx ch={} len={} pay={} type={} ltaddr={} uap={} lap={}".format(chan, len, ptype, rate, ltaddr, hex(uap), hex(lap)), wr_end='\r\n', timeout=5)

    def LE_RX(self, chan=0, phy=1, mod=0, countMode=0):
        if chan < 0 or chan > 39:
            logerror(' channel is out of range')
            return False
        self.comport.req_com("blerx ch={} phy={} mod={} countMode={}".format(chan, phy, mod, countMode), wr_end='\r\n', timeout=5)

    def tx_gain_set_tx232(self, en=1,  gain=63):
        self.mem_ts.wrm(0xa0421004, 22, 22, en)  ##Manual control of Tx PA target power enable
        self.mem_ts.wrm(0xa042100c, 31, 26, gain)  ##Manual control of Tx PA target power value


    def tx_carrier(self, freq=2402 , dac_gain=0xff, pa_gain=63, tp_mode=0):
        self.mem_ts.wr(0xa0422014, 0x0)  ##manual tx off
        self.mem_ts.wrm(0xa0421004, 22, 22, 1)  ##Manual control of Tx PA target power enable
        self.mem_ts.wrm(0xa042100c, 31, 26, pa_gain)  ##Manual control of Tx PA target power value
        self.mem_ts.wrm(0xa0421064, 12, 12, 1)  ##Frequency value manual enable
        self.mem_ts.wrm(0xa0421064, 11, 0, freq)  ##Manual value of frequency (unit: MHz)
        self.mem_ts.wr(0xa0422014, 0x0)  ##manual tx off
        ##chip.mem_ts.wrm(0xa0422044,10,0,0x7ff)
        ##chip.mem_ts.wr(0xa042100c,0x103e0249)  	##rf_ctrl_clk_manual
        self.mem_ts.wrm(0xa01200cc, 23, 22, 3)  ##rf_aon_xo_en_clk_adcdac_dig & rf_aon_xo_en_clk_ana_dig
        self.mem_ts.wrm(0xa01200cc, 20, 20, 1)  ##rf_aon_xo_en_clk_ref_dig
        ##IQ MODE
        if tp_mode==0:
            self.mem_ts.wrm(0xa0421020, 25, 24, 0)
            self.mem_ts.wrm(0xa04210e8, 26, 26, 1)  ##txdcoc sw mode
            self.mem_ts.wrm(0xa04210e8, 25, 18, dac_gain)  ##Manual TX DAC value for q-path gain index 7
            self.mem_ts.wrm(0xa04210e8, 17, 10, dac_gain)  ##Manual TX DAC value for i-path gain index 7
        ##TP MODE
        else:
            self.mem_ts.wrm(0xa0421020, 25, 24, 1)
            self.mem_ts.wrm(0xa0421088, 20, 20, 1)  ##txdcoc sw mode
            self.mem_ts.wrm(0xa0421088, 28, 21, dac_gain)  ##TP modulation dac code manual value

        self.mem_ts.wr(0xa0422014, 0xe)  ##manual tx on

    def tx_carrier_stop(self):
        self.mem_ts.wrm(0xa0421020, 25, 24, 0)
        self.mem_ts.wrm(0xa0421004, 22, 22, 0)  ##Manual control of Tx PA target power disable
        self.mem_ts.wrm(0xa0421064, 12, 12, 0)  ##Frequency value manual enable
        self.mem_ts.wr(0xa0422014, 0x0)  ##manual tx off
        self.mem_ts.wrm(0xa0422044, 10, 0, 0x0)
        self.mem_ts.wrm(0xa04210e8, 26, 26, 0)  ##txdcoc sw mode

    def tx_tone(self, freq=2402, symbol_code=1, pa_gain=63):
        self.mem_ts.wr(0xa0422014, 0x0)  ##manual tx off
        self.mem_ts.wrm(0xa0421004, 22, 22, 1)  ##Manual control of Tx PA target power enable
        self.mem_ts.wrm(0xa042100c, 31, 26, pa_gain)  ##Manual control of Tx PA target power value
        self.mem_ts.wrm(0xa0421064, 12, 12, 1)  ##Frequency value manual enable
        self.mem_ts.wrm(0xa0421064, 11, 0, freq)  ##Manual value of frequency (unit: MHz)
        # self.mem_ts.wrm(0xa0422044, 10, 0, 0x7ff)
        self.mem_ts.wrm(0xa04210e8, 26, 26, 1)  ##txdcoc sw mode
        self.mem_ts.wrm(0xa04210e8, 25, 18, 0xff)  ##Manual TX DAC value for q-path gain index 7
        self.mem_ts.wrm(0xa04210e8, 17, 10, 0xff)  ##Manual TX DAC value for i-path gain index 7
        self.mem_ts.wrm(0xa0422040, 2, 0, symbol_code)  ##symbol_tx，select tx 1 or 0
        self.mem_ts.wrm(0xa0422040, 8, 8, 1)  ##le mode
        self.mem_ts.wr(0xa0422014, 0xe)  ##manual tx on
        self.mem_ts.wrm(0xa0422040, 23, 23, 1)  ##tx ramp
        self.mem_ts.wrm(0xa0422040, 14, 14, 1)  ##modem tx_en
        self.mem_ts.wrm(0xa0422040, 6, 4, 1)  ##symbol_f

    def tx_tone_stop(self):
        self.mem_ts.wrm(0xa0421004, 22, 22, 0)  ##Manual control of Tx PA target power enable
        self.mem_ts.wrm(0xa0421064, 12, 12, 0)  ##Frequency value manual enable
        self.mem_ts.wr(0xa0422014, 0x0)  ##manual tx off
        self.mem_ts.wrm(0xa0422040, 2, 0, 0)  ##symbol_tx
        self.mem_ts.wrm(0xa0422040, 8, 8, 0)  ##le mode
        self.mem_ts.wrm(0xa0422040, 23, 23, 0)  ##tx ramp
        self.mem_ts.wrm(0xa0422040, 14, 14, 0)  ##modem tx_en
        self.mem_ts.wrm(0xa0422040, 6, 4, 0)  ##symbol_flag_tx
        self.mem_ts.wrm(0xa04210e8, 26, 26, 0)  ##txdcoc sw mode

    def cmdstop(self, mode=0):

        if mode == 0 or mode == 'le':
            cmdstr = 'letestend'
        else:
            cmdstr = 'bttestend'
        for i in range(10):
            time.sleep(1)
            res = self.comport.req_com(cmdstr, endstr='TS', wr_end='\r\n', timeout=1)
            logdebug(res)
            if len(res) != 0:
                if res[0] != 'cmd   head error! Send Again!   \n':
                    break
        return res
