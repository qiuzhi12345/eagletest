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
from rftest.rflib import rfglobal
from hal.common import *
from rftest.rflib.csv_report import csvreport
from rftest.testcase.bt_api import bt_api
from rftest.testcase.bt_nosignal_test import tester_cmw
from rftest.testcase.test_pin import testpin
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

class bt_curr(object):
    def __init__(self, comport, chipv='TX232', jlink_en=1,jlink='59610138'):
        self.comport = comport
        self.chipv = chipv
        self.mem_ts = MEM_TS(self.comport)
        self.jlink_en = jlink_en
        if jlink_en!=0:
            self.jlink = jlink
            self.btapi = bt_api(self.comport, chipv=self.chipv, jlink_en=jlink_en,jlink=self.jlink)
            self.tp = testpin(self.comport, chipv=self.chipv, jlink_en=jlink_en,jlink=self.jlink)
        else:
            self.btapi = bt_api(self.comport, chipv=self.chipv, jlink_en=jlink_en)
            self.tp = testpin(self.comport, chipv=self.chipv, jlink_en=jlink_en)


    def curr_paramp_tx_carrier(self, device_name='MY49260023', freq_list=[2402], vdd_pa_list=[3.3], cable_loss=2.6, tpmode=1, name_str='tpmode'):
        title = 'freq(MHz),vdd_pa(mv),pa_ramp,tx_carrier_pwr(dBm),curr_vddpa(mA),curr_vline3(mA)\n'
        fname = rfglobal.get_filename('ts_bt_test/', 'curr_pa_tx_carrier_{}'.format(name_str))
        fw1 = csvreport(fname, title)
        self.jlink.wrm(0xa0120080,9,9,0)
        self.jlink.wrm(0xa0120080,28,25,0)
        DM_VDDPA = dm.dm(device_name=device_name, num_of_machine=0, comm='USB')
        DM_VDDPA.device.write('VOLT {}'.format(3.3))
        DM_VDDPA.device.write('OUTPUT ON')
        # DM_VLINE3 = dm.dm(device_name='MY49260023', num_of_machine=0, comm='USB')
        myspa = Agilent()
        myspa.set_reflvl(15)
        self.jlink.wrm(0xa0120080, 9, 9, 1)
        # btapi = bt_api(self.comport, chipv=self.chipv, jlink=self.jlink)
        for freq in freq_list:
            myspa.set_param(freq, 100)
            for vdd_pa in vdd_pa_list:
                DM_VDDPA.device.write('VOLT {}'.format(vdd_pa/1000.00))
                time.sleep(2)

                for ramp in range(63,0,-1):
                    self.btapi.tx_carrier_stop()
                    self.btapi.tx_carrier(freq,0xff,ramp,tpmode)
                    res = myspa.pk_search_timesleep(timesleep=1.5)
                    txp = res[0][1]+cable_loss
                    curr_vddpa = eval(DM_VDDPA.device.ask('SENS:CURR?'))*1000
                    # curr_vline3 = eval(DM_VLINE3.device.ask('MEAS:CURR?'))*1000
                    loginfo('ramp:  {}  txp:   {}  curr_vddpa:  {}  '.format(ramp,txp,curr_vddpa))
                    fw1.write_data([freq,vdd_pa,ramp,txp,curr_vddpa])
        self.btapi.tx_carrier_stop()

    def curr_reg_tx_carrier(self, freq=2402, vdd_pa=3.3,cable_loss=4 ):
        title = 'freq(MHz),vdd_pa(v),pa_ramp,pa_vbiasb_trim,pa_vbiasa_trim,pa_ptat_trim,pa_vblowcas_trim,pa_vbcas_trim,tx_carrier_pwr(dBm),curr_vddpa(mA),curr_vline3(mA),txp_br,' \
                'delta_f2_99,delta_f2_avg,curr_br_vddpa,curr_br_vline3,txp_edr2,DEVM_RMS,curr_edr2_vddpa,curr_edr2_vline3\n'
        fname = rfglobal.get_filename('ts_bt_test/', 'curr_reg_tx_carrier')
        fw1 = csvreport(fname, title)
        self.jlink.wrm(0xa0120080,9,9,0)
        self.jlink.wrm(0xa0120080,28,25,8)
        DM_VDDPA = dm.dm(device_name='MY50180049', num_of_machine=0, comm='USB')
        DM_VDDPA.device.write('VOLT {}'.format(vdd_pa))
        DM_VDDPA.device.write('OUTPUT ON')
        DM_VLINE3 = dm.dm(device_name='MY49260023', num_of_machine=0, comm='USB')
        myspa = Agilent()
        tester = tester_cmw(mode=0, rfport=1, cable_loss=cable_loss, bt_mode='BR', freq=freq,
                            target_power=15, burst_type='BR', asyn='OFF', bdaddr='050604010203')
        # self.BT_INIT('BR')
        # btapi = bt_api(self.comport, chipv=self.chipv, jlink=self.jlink)
        self.btapi.cmdstop(1)
        self.btapi.cmdstop(0)
        self.btapi.tx_carrier_stop()
        myspa.set_param(freq,100)
        myspa.set_reflvl(15)
        self.jlink.wrm(0xa0120080, 9, 9, 1)

        reg_dic={
            0:  ['pa_vbiasb_trim',[28,27]],
            1: ['pa_vbiasa_trim', [26, 25]],
            2:  ['pa_ptat_trim',[7,6]],
            3: ['pa_vblowcas_trim',[4,3]],
            4: ['pa_vbcas_trim',[2,1]]
            }
        msb0 = reg_dic[0][1][0]
        lsb0 = reg_dic[0][1][1]
        init_pa_vbiasb_trim = self.jlink.rdm(0xa0421038, msb0, lsb0)
        msb1 = reg_dic[1][1][0]
        lsb1 = reg_dic[1][1][1]
        init_pa_vbiasa_trim = self.jlink.rdm(0xa0421038, msb1, lsb1)
        msb2 = reg_dic[2][1][0]
        lsb2 = reg_dic[2][1][1]
        init_pa_ptat_trim = self.jlink.rdm(0xa0421038, msb2, lsb2)
        msb3 = reg_dic[3][1][0]
        lsb3 = reg_dic[3][1][1]
        init_pa_vblowcas_trim = self.jlink.rdm(0xa0421038, msb3, lsb3)
        msb4 = reg_dic[4][1][0]
        lsb4 = reg_dic[4][1][1]
        init_pa_vbcas_trim = self.jlink.rdm(0xa0421038, msb4, lsb4)
        for ramp in [63]:

            for pa_vbiasb_trim in range(0,-1,-1):
                self.jlink.wrm(0xa0421038, msb0, lsb0, pa_vbiasb_trim)
                for pa_vbiasa_trim in range(0,-1,-1):
                    self.jlink.wrm(0xa0421038, msb1, lsb1, pa_vbiasa_trim)
                    for pa_ptat_trim in range(3,-1,-1):
                        self.jlink.wrm(0xa0421038, msb2, lsb2, pa_ptat_trim)
                        for pa_vblowcas_trim in range(3,-1,-1):
                            self.jlink.wrm(0xa0421038, msb3, lsb3, pa_vblowcas_trim)
                            for pa_vbcas_trim in range(3,-1,-1):
                                self.jlink.wrm(0xa0421038, msb4, lsb4, pa_vbcas_trim)

                                self.btapi.tx_carrier(freq, 0xff, ramp)
                                res = myspa.pk_search_avg_timesleep(timesleep=1.5)
                                tx_tone_pwr = res[0][1]
                                curr_tone_vddpa = eval(DM_VDDPA.device.ask('SENS:CURR?'))*1000
                                time.sleep(0.5)
                                curr_tone_vline3 = eval(DM_VLINE3.device.ask('MEAS:CURR?'))*1000
                                self.btapi.tx_carrier_stop()

                                self.btapi.BR_TX(chan=0,len=27,ptype=2,rate=1)
                                tester.stx.mode_set('BR')
                                tester.stx.input_signal_settings(btype='BR',asyn='OFF')
                                res = tester.stx.get_modulation_measure_res()
                                curr_br_vddpa = eval(DM_VDDPA.device.ask('SENS:CURR?'))*1000
                                time.sleep(0.5)
                                curr_br_vline3 = eval(DM_VLINE3.device.ask('MEAS:CURR?'))*1000
                                logdebug('{}'.format(res))

                                delta_f2_99 = eval(res[2]) / 1000.00
                                freq_accuracy = eval(res[3]) / 1000.00
                                freq_drift = eval(res[4]) / 1000.00
                                drift_rate = eval(res[5]) / 1000.00
                                delta_f2_avg = eval(res[9]) / 1000.00
                                delta_f2_min = eval(res[10]) / 1000.00
                                delta_f2_max = eval(res[11]) / 1000.00
                                txp_br = eval(res[12])
                                self.btapi.cmdstop(1)
                                self.btapi.BR_TX(chan=0, len=54, ptype=7, rate=2)
                                tester.stx.mode_set('EDR')
                                tester.stx.input_signal_settings(btype='EDR',asyn='OFF')
                                res = tester.stx.get_modulation_measure_res()
                                curr_edr2_vddpa = eval(DM_VDDPA.device.ask('SENS:CURR?'))*1000
                                time.sleep(0.5)
                                curr_edr2_vline3 = eval(DM_VLINE3.device.ask('MEAS:CURR?'))*1000
                                logdebug('{}'.format(res))

                                res = [eval(i) for i in res[0:]]

                                wi = res[2] / 1000.00
                                w0_wi = res[3] / 1000.00
                                w0_max = res[4] / 1000.00
                                DEVM_RMS = res[5]
                                DEVM_peak = res[6]
                                DEVM_P99 = res[7]
                                txp_edr2 = res[8]
                                self.btapi.cmdstop(1)


                                loginfo('ramp:  {}  txp:   {}  curr_vddpa:  {}  curr_vline3:    {}'.format(ramp, tx_tone_pwr, curr_tone_vddpa, curr_tone_vline3))
                                fw1.write_data([freq,vdd_pa,ramp,pa_vbiasb_trim,pa_vbiasa_trim,pa_ptat_trim,pa_vblowcas_trim,pa_vbcas_trim,tx_tone_pwr, curr_tone_vddpa,
                                                curr_tone_vline3,txp_br,delta_f2_99,delta_f2_avg,curr_br_vddpa,curr_br_vline3,txp_edr2,DEVM_RMS,curr_edr2_vddpa,curr_edr2_vline3])

        self.jlink.wrm(0xa0421038, msb0, lsb0, init_pa_vbiasb_trim)
        self.jlink.wrm(0xa0421038, msb1, lsb1, init_pa_vbiasa_trim)
        self.jlink.wrm(0xa0421038, msb2, lsb2, init_pa_ptat_trim)
        self.jlink.wrm(0xa0421038, msb3, lsb3, init_pa_vblowcas_trim)
        self.jlink.wrm(0xa0421038, msb4, lsb4, init_pa_vbcas_trim)

    def curr_lna(self,freq=2402,device_name='MY50180049'):
        title = 'freq(MHz),lna_itrim,lna_hgain_code,curr_vline1(mA)\n'
        fname = rfglobal.get_filename('ts_bt_test/', 'curr_lna')
        fw1 = csvreport(fname, title)
        DM_VLINE1 = dm.dm(device_name=device_name, num_of_machine=0, comm='USB')
        self.jlink.wrm(0xa04210a0,0,0,1)   ##agc disable
        self.jlink.wrm(0xa04210a0, 20, 17, 0xc)  ##AGC initial index
        self.jlink.wr(0xa0422014,0x3)  ##manual rxon
        for lna_itrim in range(3,-1,-1):
            self.jlink.wrm(0xa0421034, 8, 7, lna_itrim)
            for lna_hgain_code in range(6):
                self.jlink.wrm(0xa04210b4, 25, 25, 1)  ##lna_hgain_pwup
                self.jlink.wrm(0xa04210b4, 24, 19, 0x3f>>lna_hgain_code)
                curr_vline1 = eval(DM_VLINE1.device.ask('MEAS:CURR?')) * 1000
                loginfo('lna_itrim:     {}   lna_hgain_code:    {}      curr_vline1:    {}'.format(lna_itrim,0x3f>>lna_hgain_code,curr_vline1))
                fw1.write_data([freq, lna_itrim,0x3f>>lna_hgain_code,curr_vline1])
        fw1.write_string('freq(MHz),lna_itrim,lna_lgain_code,curr_vline1(mA)\n')
        for lna_itrim in range(3,-1,-1):
            self.jlink.wrm(0xa0421034, 8, 7, lna_itrim)
            for lna_lgain_code in range(3,-1,-1):
                self.jlink.wrm(0xa04210b4, 25, 25, 0)  ##lna_hgain_pwup
                self.jlink.wrm(0xa04210b4, 18, 17, lna_lgain_code)
                curr_vline1 = eval(DM_VLINE1.device.ask('MEAS:CURR?')) * 1000
                loginfo('lna_itrim:     {}   lna_lgain_code:    {}      curr_vline1:    {}'.format(lna_itrim,lna_lgain_code,curr_vline1))
                fw1.write_data([freq, lna_itrim,lna_lgain_code,curr_vline1])
        self.jlink.wrm(0xa04210b4,25,17,0x1ff)
        self.jlink.wrm(0xa04210a0, 0, 0, 0)  ##agc enable
    def xo_manual(self,en=1):
        if en!=0:
            self.jlink.wrm(0xa01200cc, 29, 29, 1)  ##bbpll_bg_pup enable
            self.jlink.wrm(0xa01200cc, 30, 30, 1)  ##bg_pup_ibg_xo
            self.jlink.wrm(0xa01200cc, 26, 25, 3)  ##manual xo pup enable
            self.jlink.wrm(0xa01200cc, 27, 27, 0)  ##manual xo pup
        else:
            self.jlink.wrm(0xa01200cc, 27, 27, 1)  ##auto xo

    def curr_xo(self, device_name='MY49260023'):
        '''
        测试的是xo与bbpll_bg合在一起的电流
        '''
        title = 'xo_ldo_trim,xo_isel,curr_vline3(mA)\n'
        fname = rfglobal.get_filename('ts_bt_test/', 'curr_xo')
        fw1 = csvreport(fname, title)
        DM_VLINE3 = dm.dm(device_name=device_name, num_of_machine=0, comm='USB')
        self.jlink.wr(0xa0422014, 0x0)
        self.jlink.wrm(0xa00000a8, 1, 0,1)  ##mclk0_sel rc48m
        self.tp.bbpll_en(0)
        self.xo_manual(1)
        init_xo_ldo = self.jlink.rdm(0xa01200cc, 5, 4)
        init_xo_isel = self.jlink.rdm(0xa01200cc, 10, 7)
        for xo_ldo_trim in range(3,-1,-1):
            self.jlink.wrm(0xa01200cc, 5, 4, xo_ldo_trim)
            for xo_isel in range(0xf,-1,-1):
                self.jlink.wrm(0xa01200cc, 10, 7, xo_isel)
                time.sleep(1)
                curr_vline3 = eval(DM_VLINE3.device.ask('MEAS:CURR?')) * 1000
                loginfo('xo_ldo_trim:   {}  xo_isel:    {}  curr_vline3:    {}'.format(xo_ldo_trim,xo_isel,curr_vline3))
                fw1.write_data([xo_ldo_trim,xo_isel,curr_vline3])
        self.jlink.wrm(0xa01200cc, 5, 4, init_xo_ldo)
        self.jlink.wrm(0xa01200cc, 10, 7, init_xo_isel)

    def vline1_init(self):
        self.jlink.wrm(0xa0421004, 9, 9, 0)  ##lna_pup
        self.jlink.wrm(0xa0421004, 12, 12, 0)  ##cbpf1_pup
        self.jlink.wrm(0xa0421000, 17, 17, 0)  ##ldo_trxhf_pup
        self.jlink.wrm(0xa0421000, 11, 11, 0)  ##bg_pup
        self.jlink.wrm(0xa0421004, 17, 17, 0)  ##txmix_pup
        self.jlink.wrm(0xa0421004, 16, 16, 0)  ##txpa_pup

    def curr_vline1(self, device_name='MY50180049'):
        title = 'mode,curr_init(mA),curr_LNA+mix_off(mA),curr_cbpf_off(mA),curr_ldo_trxhf_off(mA),curr_bg_off(mA)\n'
        fname = rfglobal.get_filename('ts_bt_test/', 'curr_vline1')
        fw1 = csvreport(fname, title)
        DM_VLINE = dm.dm(device_name=device_name, num_of_machine=0, comm='USB')
        self.jlink.wrm(0xa00000a8, 1, 0,1)  ##mclk0_sel rc48m
        self.jlink.wrm(0xa04210a0,0,0,1)   ##agc disable
        self.jlink.wrm(0xa04210a0, 20, 17, 0xc)  ##AGC initial index

        for lna_itrim in range(4):
            self.jlink.wrm(0xa0421034, 8, 7, lna_itrim)
            for cbpf_bias_trim in range(8):
                self.jlink.wrm(0xa0421034, 18, 16, cbpf_bias_trim)
                for ldo_trxhf_trim in range(4):
                    self.jlink.wrm(0xa0421028, 7, 6, ldo_trxhf_trim)

                    self.vline1_init()
                    self.jlink.wr(0xa0422014, 0x3)  ##manual rxon
                    curr_init = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
                    self.jlink.wrm(0xa0421004, 9, 9, 1)  ##lna_pup disable
                    curr_lna_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
                    self.jlink.wrm(0xa0421004, 12, 12, 1)  ##cbpf1_pupp disable
                    curr_cbpf_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
                    self.jlink.wrm(0xa0421000, 17, 17, 1)  ##ldo_trxhf_pup disable
                    curr_trxhf_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
                    self.jlink.wrm(0xa0421000, 11, 11, 1)  ##bg_pup disable
                    curr_bg_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
                    loginfo('rxon curr:  {}      {}  {}  {}  {}  {}'.format('rxon', curr_init, curr_lna_off, curr_cbpf_off, curr_trxhf_off, curr_bg_off))
                    fw1.write_data(['rxon', curr_init, curr_lna_off, curr_cbpf_off, curr_trxhf_off, curr_bg_off])


        fw1.write_string('mode,curr_init(mA),curr_txmix_off(mA),curr_txpa_off(mA),curr_ldo_trxhf_off(mA),curr_bg_off(mA)\n')
        self.vline1_init()
        self.jlink.wr(0xa0422014, 0xe)  ##manual rxon
        curr_init = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
        self.jlink.wrm(0xa0421004, 17, 17, 0)  ##txmix_pupp disable
        curr_txmix_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
        self.jlink.wrm(0xa0421004, 16, 16, 0)  ##txpa_pup disable
        curr_txpa_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
        self.jlink.wrm(0xa0421000, 17, 17, 1)  ##ldo_trxhf_pup disable
        curr_trxhf_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
        self.jlink.wrm(0xa0421000, 11, 11, 1)  ##bg_pup disable
        curr_bg_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
        loginfo('txon curr:  {}      {}  {}  {}  {}  {}'.format('rxon', curr_init, curr_txmix_off, curr_txpa_off, curr_trxhf_off, curr_bg_off))
        fw1.write_data(['txon', curr_init, curr_txmix_off, curr_txpa_off, curr_trxhf_off, curr_bg_off])

        self.vline1_init()

    def vline2_init(self):
        self.jlink.wrm(0xa0421020, 25, 25, 1)  ##iq mode
        self.jlink.wrm(0xa0421004, 3, 2, 0)  ##lo_pup_vlo_txfskdrv and lo_pup_vlo_txfsk
        self.jlink.wrm(0xa0421004, 1, 0, 0)  ##lo_pup_vlo_txdrv and lo_pup_vlo_tx
        self.jlink.wrm(0xa0421000, 31, 30, 0)  ##lo_pup_vlo_rxdrv and lo_pup_vlo_rx
        self.jlink.wrm(0xa0421000, 28, 28, 0)  ##vcodiv2_pup
        self.jlink.wrm(0xa0421000, 27, 27, 0)  ##vco_pup
        self.jlink.wrm(0xa0421000, 23, 23, 0)  ##ldo_vco_pup

    def curr_vline2(self, device_name='MY50180049'):
        title = 'mode,ldo_vco_trim,curr_init(mA),curr_vlo_rx_off(mA),curr_vcodiv2_off(mA),curr_vco_off(mA),curr_ldo_vco_off(mA)\n'
        fname = rfglobal.get_filename('ts_bt_test/', 'curr_vline2')
        fw1 = csvreport(fname, title)
        DM_VLINE2 = dm.dm(device_name=device_name, num_of_machine=0, comm='USB')

        self.jlink.wrm(0xa00000a8, 1, 0,1)  ##mclk0_sel rc48m
        for ldo_vco_trim in range(0,4):
            self.jlink.wrm(0xa0421028, 15, 14, ldo_vco_trim)
            self.vline2_init()
            self.jlink.wr(0xa0422014, 0x3)  ##manual rxon
            curr_init = eval(DM_VLINE2.device.ask('MEAS:CURR?')) * 1000
            self.jlink.wrm(0xa0421000, 31, 30, 3)  ##lo_pup_vlo_rxdrv and lo_pup_vlo_rx disable
            curr_vlo_rx_off = eval(DM_VLINE2.device.ask('MEAS:CURR?')) * 1000
            self.jlink.wrm(0xa0421000, 28, 28, 1)  ##vcodiv2_pup disable
            curr_vcodiv2_off = eval(DM_VLINE2.device.ask('MEAS:CURR?')) * 1000
            self.jlink.wrm(0xa0421000, 27, 27, 1)  ##vco_pup disable
            curr_vco_off = eval(DM_VLINE2.device.ask('MEAS:CURR?')) * 1000
            self.jlink.wrm(0xa0421000, 23, 23, 1)  ##ldo_vco_pup disable
            curr_ldo_vco_off = eval(DM_VLINE2.device.ask('MEAS:CURR?')) * 1000
            loginfo('{}     {}  {}  {}  {}  {}  {}'.format('rxon',ldo_vco_trim,curr_init,curr_vlo_rx_off,curr_vcodiv2_off,curr_vco_off,curr_ldo_vco_off))
            fw1.write_data(['rxon',ldo_vco_trim,curr_init,curr_vlo_rx_off,curr_vcodiv2_off,curr_vco_off,curr_ldo_vco_off])

        fw1.write_string('mode,ldo_vco_trim,curr_init(mA),curr_vlo_tx_off(mA),curr_vcodiv2_off(mA),curr_vco_off(mA),curr_ldo_vco_off(mA)\n')
        for ldo_vco_trim in range(0, 4):
            self.jlink.wrm(0xa0421028, 15, 14, ldo_vco_trim)
            self.vline2_init()
            self.jlink.wr(0xa0422014, 0xe)  ##manual txon
            curr_init = eval(DM_VLINE2.device.ask('MEAS:CURR?')) * 1000
            self.jlink.wrm(0xa0421004, 1, 0, 3)  ##lo_pup_vlo_txdrv and lo_pup_vlo_tx disable
            curr_vlo_tx_off = eval(DM_VLINE2.device.ask('MEAS:CURR?')) * 1000
            self.jlink.wrm(0xa0421000, 28, 28, 1)  ##vcodiv2_pup disable
            curr_vcodiv2_off = eval(DM_VLINE2.device.ask('MEAS:CURR?')) * 1000
            self.jlink.wrm(0xa0421000, 27, 27, 1)  ##vco_pup disable
            curr_vco_off = eval(DM_VLINE2.device.ask('MEAS:CURR?')) * 1000
            self.jlink.wrm(0xa0421000, 23, 23, 1)  ##ldo_vco_pup disable
            curr_ldo_vco_off = eval(DM_VLINE2.device.ask('MEAS:CURR?')) * 1000
            loginfo('{}     {}  {}  {}  {}  {}  {}'.format('rxon', ldo_vco_trim, curr_init, curr_vlo_tx_off, curr_vcodiv2_off, curr_vco_off, curr_ldo_vco_off))
            fw1.write_data(['txon', ldo_vco_trim, curr_init, curr_vlo_tx_off, curr_vcodiv2_off, curr_vco_off, curr_ldo_vco_off])

        fw1.write_string('mode,ldo_vco_trim,curr_init(mA),curr_vlo_txgfsk_off(mA),curr_vcodiv2_off(mA),curr_vco_off(mA),curr_ldo_vco_off(mA)\n')
        for ldo_vco_trim in range(0, 4):
            self.vline2_init()
            self.jlink.wr(0xa0422014, 0x0)  ##auto txrx
            self.jlink.wrm(0xa0421020, 25, 25, 0)  ##tp mode
            self.jlink.wr(0xa0422014, 0xe)  ##manual txon
            curr_init = eval(DM_VLINE2.device.ask('MEAS:CURR?')) * 1000
            self.jlink.wrm(0xa0421004, 3, 2, 3)  ##lo_pup_vlo_txdrv and lo_pup_vlo_tx disable
            curr_vlo_txgfsk_off = eval(DM_VLINE2.device.ask('MEAS:CURR?')) * 1000
            self.jlink.wrm(0xa0421000, 28, 28, 1)  ##vcodiv2_pup disable
            curr_vcodiv2_off = eval(DM_VLINE2.device.ask('MEAS:CURR?')) * 1000
            self.jlink.wrm(0xa0421000, 27, 27, 1)  ##vco_pup disable
            curr_vco_off = eval(DM_VLINE2.device.ask('MEAS:CURR?')) * 1000
            self.jlink.wrm(0xa0421000, 23, 23, 1)  ##ldo_vco_pup disable
            curr_ldo_vco_off = eval(DM_VLINE2.device.ask('MEAS:CURR?')) * 1000
            loginfo('{}     {}  {}  {}  {}  {}  {}'.format('rxon', ldo_vco_trim, curr_init, curr_vlo_txgfsk_off, curr_vcodiv2_off, curr_vco_off, curr_ldo_vco_off))
            fw1.write_data(['txon_tp', ldo_vco_trim, curr_init, curr_vlo_txgfsk_off, curr_vcodiv2_off, curr_vco_off, curr_ldo_vco_off])
        self.vline2_init()

    def vline3_init(self):
        self.jlink.wrm(0xa0421004, 15, 15, 0)  ##adc_pup
        self.jlink.wrm(0xa0421004, 6, 6, 0)  ##pfdcp_pup
        self.jlink.wrm(0xa0421004, 5, 5, 0)  ##divn_pup
        self.jlink.wrm(0xa0421000, 21, 21, 0)  ##ldo_pll_pup
        self.jlink.wrm(0xa0421000, 19, 19, 0)  ##ldo_trxlf_pup
        self.jlink.wrm(0xa0421000, 16, 16, 0)  ##ldo_lv_pup
        self.tp.bbpll_en(1)
        self.jlink.wrm(0xa01200cc,27,27,1)     ##xo
        self.jlink.wrm(0xa0421004, 18, 18, 0)  ##txlpf_pup
        self.jlink.wrm(0xa0421004, 20, 20, 0)  ##txdac_pup
    def curr_vline3(self, device_name='MY50180049'):
        title = 'mode,curr_init(mA),curr_adc_off(mA),curr_pfdcp_off(mA),curr_divn_off(mA),curr_ldo_pll_off(mA),curr_ldo_trxlf_off(mA),curr_ldo_lv_off(mA),curr_bbpll_off(mA),' \
                'curr_xo_off(mA)\n'
        fname = rfglobal.get_filename('ts_bt_test/', 'curr_vline3')
        fw1 = csvreport(fname, title)
        DM_VLINE = dm.dm(device_name=device_name, num_of_machine=0, comm='USB')
        self.jlink.wrm(0xa00000a8, 1, 0,1)  ##mclk0_sel rc48m

        self.vline3_init()
        self.jlink.wr(0xa0422014, 0x3)  ##manual rxon
        curr_init = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
        self.jlink.wrm(0xa0421004, 15, 15, 1)  ##adc_pup disable
        curr_adc_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
        self.jlink.wrm(0xa0421004, 6, 6, 1)  ##pfdcp_pup disable
        curr_pfdcp_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
        self.jlink.wrm(0xa0421004, 5, 5, 1)  ##divn_pup disable
        curr_divn_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
        self.jlink.wrm(0xa0421000, 21, 21, 1)  ##ldo_pll_pup disable
        curr_ldo_pll_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
        self.jlink.wrm(0xa0421000, 19, 19, 1)  ##ldo_trxlf_pup disable
        curr_ldo_trxlf_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
        self.jlink.wrm(0xa0421000, 16, 16, 1)  ##ldo_lv_pup disable
        curr_ldo_lv_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
        self.jlink.wrm(0xa0000144, 23, 22, 0)  ##bbpll disable
        curr_bbpll_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
        self.jlink.wrm(0xa01200cc, 27, 27, 0)  ##xo disable
        self.jlink.wrm(0xa01200cc, 29, 29, 0)  ##bbpll_bg disable
        curr_xo_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
        self.jlink.wrm(0xa01200cc, 29, 29, 1)  ##bbpll_bg enable
        self.jlink.wrm(0xa01200cc, 27, 27, 1)  ##xo enable

        loginfo('rxon curr:  {}      {}  {}  {}  {}  {}     {}  {}  {}  {}'.format('rxon', curr_init, curr_adc_off, curr_pfdcp_off, curr_divn_off, curr_ldo_pll_off,
                                                                                  curr_ldo_trxlf_off,
                                                                      curr_ldo_lv_off,curr_bbpll_off,curr_xo_off))
        fw1.write_data(['rxon', curr_init, curr_adc_off, curr_pfdcp_off, curr_divn_off, curr_ldo_pll_off,curr_ldo_trxlf_off,curr_ldo_lv_off,curr_bbpll_off,curr_xo_off])

        fw1.write_string('mode,curr_init(mA),curr_txlpf_off(mA),curr_txdac_off(mA),curr_pfdcp_off(mA),curr_divn_off(mA),curr_ldo_pll_off(mA),curr_ldo_trxlf_off(mA),'
                         'curr_ldo_lv_off(mA),curr_bbpll_off(mA),curr_xo_off(mA)\n')
        self.vline3_init()
        self.jlink.wr(0xa0422014, 0xe)  ##manual rxon
        curr_init = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
        self.jlink.wrm(0xa0421004, 18, 18, 1)  ##txlpf_pup disable
        curr_txlpf_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
        self.jlink.wrm(0xa0421004, 20, 20, 1)  ##txdac_pup disable
        curr_txdac_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
        self.jlink.wrm(0xa0421004, 6, 6, 1)  ##pfdcp_pup disable
        curr_pfdcp_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
        self.jlink.wrm(0xa0421004, 5, 5, 1)  ##divn_pup disable
        curr_divn_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
        self.jlink.wrm(0xa0421000, 21, 21, 1)  ##ldo_pll_pup disable
        curr_ldo_pll_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
        self.jlink.wrm(0xa0421000, 19, 19, 1)  ##ldo_trxlf_pup disable
        curr_ldo_trxlf_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
        self.jlink.wrm(0xa0421000, 16, 16, 1)  ##ldo_lv_pup disable
        curr_ldo_lv_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
        self.jlink.wrm(0xa0000144, 23, 22, 0)  ##bbpll disable
        curr_bbpll_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
        self.jlink.wrm(0xa01200cc, 27, 27, 0)  ##xo disable
        curr_xo_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
        self.jlink.wrm(0xa01200cc, 27, 27, 1)  ##xo enable

        loginfo('txon curr:  {}      {}  {}  {}  {}  {}     {}  {}  {}  {}'.format('txon', curr_init, curr_txlpf_off, curr_txdac_off, curr_pfdcp_off, curr_divn_off,
                                                                                   curr_ldo_pll_off,
                                                                                  curr_ldo_trxlf_off,
                                                                      curr_ldo_lv_off,curr_bbpll_off,curr_xo_off))
        fw1.write_data(['txon', curr_init, curr_txlpf_off, curr_txdac_off, curr_pfdcp_off, curr_divn_off, curr_ldo_pll_off,curr_ldo_trxlf_off,curr_ldo_lv_off,curr_bbpll_off,\
                                                                          curr_xo_off])
        self.vline3_init()


    def curr_bbpll(self, device_name='MY50180049'):
        title = 'bbpll_ldo_trim,curr_init(mA),curr_bbpll_off(mA),curr_bbpll_ldo_off(mA),curr_xo_off(mA),curr_bg_off(mA)\n'
        fname = rfglobal.get_filename('ts_bt_test/', 'curr_bbpll')
        fw1 = csvreport(fname, title)
        DM_VLINE = dm.dm(device_name=device_name, num_of_machine=0, comm='USB')
        self.jlink.wr(0xa0422014, 0x0)
        self.jlink.wrm(0xa00000a8, 1, 0, 1)  ##mclk0_sel rc48m
        self.xo_manual(1)
        bbpll_ldo_trim_init = self.jlink.rdm(0xa0000144, 14, 12)
        for bbpll_ldo_trim in range(8):
            self.jlink.wrm(0xa0000144, 14, 12, bbpll_ldo_trim)
            self.xo_manual(1)
            self.tp.bbpll_en(1)
            curr_init = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
            self.jlink.wrm(0xa0000144, 22, 22, 0)  ##bbpll_pup disable
            curr_bbpll_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
            self.jlink.wrm(0xa0000144, 23, 23, 0)  ##bbpll_ldo_pup disable
            self.jlink.wrm(0xa0000144, 25, 25, 0)  ##bbpll_bg_pup_ibg_bbpll
            curr_bbpll_ldo_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
            self.jlink.wrm(0xa01200cc, 26, 25, 0)  ##xo_pup disable
            curr_xo_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
            self.jlink.wrm(0xa01200cc, 30, 29, 0)  ##bg_pup disable
            curr_bg_off = eval(DM_VLINE.device.ask('MEAS:CURR?')) * 1000
            loginfo('bbpll curr:  {}      {}  {}  {}  {} {}'.format( bbpll_ldo_trim,curr_init, curr_bbpll_off, curr_bbpll_ldo_off,curr_xo_off,curr_bg_off))
            fw1.write_data([bbpll_ldo_trim,curr_init, curr_bbpll_off, curr_bbpll_ldo_off,curr_xo_off,curr_bg_off])
        self.xo_manual(1)
        self.tp.bbpll_en(1)
        self.jlink.wrm(0xa0000144, 14, 12, bbpll_ldo_trim_init)
