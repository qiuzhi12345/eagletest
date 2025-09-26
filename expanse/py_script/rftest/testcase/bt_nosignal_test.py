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
from rftest.testcase.bt_api import bt_api
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
class tester_cmw(object):
    def __init__(self, mode=0, rfport=2, cable_loss=1, bt_mode='LE1M', freq=2440, target_power=10, umargin=20, detect_mode='AUTO', burst_type='LE', phy='LE1M',repetition='SING', asyn='ON', bdaddr='050604010203', count=20, tout=10):
        if mode == 0:
            self.stx = standalone_tx('CMW')
            self.stx.reset(10)
            self.stx.rf_port(mode=mode, rfport=rfport, atten=cable_loss)
            self.stx.mode_set(mode=bt_mode)
            self.stx.analyzer_settings(enpower=target_power, umargin=umargin, freq=freq)
            self.stx.input_signal_settings(dmode=detect_mode, asyn=asyn, btype=burst_type, phy=phy, bdaddr=bdaddr)
            self.stx.measure_para(tout=tout, repetition=repetition, count=count)
            self.stx.measure_states(state=0)
        elif mode == 1:
            self.srx = standalone_rx('CMW')
            self.srx.rf_port(mode=mode, rfport=rfport, atten=cable_loss)
            self.srx.para_settings(freq=freq, level=-30)


class bt_nosignal_test(object):
    def __init__(self, comport, chipv='TX232_MPW3', jlink='59610138',jlink_en=1,board_name=''):
        self.comport = comport
        self.chipv = chipv
        self.mem_ts = MEM_TS(self.comport)
        self.board_name = board_name
        self.jlink_en = jlink_en
        if jlink_en!=0:
            self.jlink = jlink
            self.btapi = bt_api(self.comport, chipv=self.chipv, jlink_en=jlink_en,jlink=self.jlink)
        else:
            self.btapi = bt_api(self.comport, chipv=self.chipv, jlink_en=jlink_en)
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


    def get_cmw_exp_pwr(self, tester=tester_cmw, target_power=30):
        self.btapi.BR_TX(chan=0, len=27, ptype=1, rate=1)
        for i in range(15):
            tester.stx.analyzer_settings(enpower=target_power, umargin=8, freq=2402)
            res = tester.stx.get_power_measure_res()
            if eval(res[0]) == 0:
                txpower = eval(res[3])
                target_power = txpower +10
                break
            else:
                target_power = target_power-5
        loginfo('target power set {}'.format(target_power))
        return target_power

    def br_tx(self,chan_list=[0,39,78], rfport=2, cable_loss=1, rate_list=['DH1'],  target_power=10, fig_en=1, csv_save=True, report_save=True):

        if csv_save :
            title = 'channel,type,nominal_pow(dBm),peak_pow(dBm),leakage_pow(dBm),freq_accuracy(kHz),freq_drift(kHz),drift_rate(Hz/50 μs),'
            title = title + 'delta_f1_avg(kHz),delta_f1_min(kHz),delta_f1_max(kHz),delta_f2_avg(kHz),delta_f2_min(kHz),delta_f2_max(kHz),mod_ratio,delta_f2_99(kHz),'
            title = title + 'obw(kHz),frange_l(kHz),frange_h(kHz),acp_list_21ch\n'
            fname = rfglobal.get_filename('ts_bt_test/','test_br_tx_{}'.format(self.board_name))
            fw1=csvreport(fname,title)
        if report_save:
            title2 = 'BR_tx_performance'
            fname2 = self.get_filename('ts_bt_test/','test_br_tx_report_{}'.format(self.board_name))
            fw2=csvreport(fname2,title2)
            item = ['channel', 'DH', u'Tx/01 - Output Power  - Average', u'- Peak',
                    u'@   - Leakage',
                    u' @   - Packet Timing',
                    u'Tx/04 - Spectrum - Frequency Range - Left',
                    u'- Right',
                    u'Tx/05 - Spectrum - 20 dB Bandwidth - f(L)',
                    u'- f(H)',
                    u'- f(H) - f(L)',
                    u'Tx/06 - Spectrum - Adjacent channel power - Max Power',
                    u'- ACP - >3 MHz',
                    u'- ACP -3 MHz',
                    u'- ACP -2 MHz',
                    u'- ACP -1 MHz',
                    u' - ACP +1 MHz',
                    u'- ACP +2 MHz',
                    u'- ACP +3 MHz',
                    u'- ACP + >3 MHz',
                    u'Tx/07 - Modulation Characteristics - Delta F1 Avg',
                    u'Tx/07 - Modulation Characteristics - Delta F2 Avg',
                    u'- Delta F2 Max 99%',
                    u'- Delta F2 Avg/Delta F1 Avg',
                    u'Tx/08 - Initial Carrier Frequency Tolerance - Avg',
                    u'- Max',
                    u'Tx/09 - Carrier Frequency Drift - Max.Drift DH1',
                    u' - Max.Drift DH5',
                    u' - Max.Drift',
                    u' - Max.Drift Rate/50us DH1',
                    u' - Max.Drift Rate/50us DH5',
                    u'- Max.Drift Rate/50us',
                    u'Harmonic Spurs']

            df = pd.DataFrame(item)
            df.to_csv(fw2.filename, index=False)

        tester = tester_cmw(mode=0, rfport=rfport, cable_loss=cable_loss, bt_mode='BR', freq=2402, target_power=target_power, burst_type='BR', asyn='OFF', bdaddr='050604010203')
        res_list = []
        self.btapi.cmdstop(1)
        self.btapi.cmdstop(0)
        tester.stx.trigger_settings(source='power', threshold=-20, tout=1)
        flag = True
        for chan in chan_list:
            for DH in rate_list:
                tester.stx.analyzer_settings(enpower=target_power, freq=2402 + chan)
                br_len = self.br_len_dic[DH]
                _rate = self.br_rate_dic[DH]
                self.btapi.BR_TX(chan=chan, len=br_len, ptype=1, rate=_rate)
                res = tester.stx.get_modulation_measure_res()
                logdebug('{}'.format(res))

                delta_f1_avg = eval(res[6])/1000.00
                delta_f1_min = eval(res[7])/1000.00
                delta_f1_max = eval(res[8])/1000.00

                time.sleep(0.5)
                self.btapi.cmdstop(1)
                self.btapi.BR_TX(chan=chan, len=br_len, ptype=2, rate=_rate)
                res = tester.stx.get_modulation_measure_res()

                logdebug('{}'.format(res))

                delta_f2_99 = eval(res[2])/1000.00
                freq_accuracy = eval(res[3])/1000.00
                freq_drift = eval(res[4])/1000.00
                drift_rate = eval(res[5])/1000.00
                delta_f2_avg = eval(res[9])/1000.00
                delta_f2_min = eval(res[10])/1000.00
                delta_f2_max = eval(res[11])/1000.00
                mod_ratio = delta_f2_avg/delta_f1_avg

                _res = tester.stx.get_modulation_measure_res(data_type='MAX')
                freq_drift = eval(_res[4])/1000.00
                drift_rate = eval(_res[5])/1000.00

                time.sleep(0.5)
                self.btapi.cmdstop(1)
                self.btapi.BR_TX(chan=chan, len=br_len, ptype=7, rate=_rate)
                res1 = tester.stx.get_power_measure_res()
                print(res1)
                if eval(res1[0]) != 0:
                    self.btapi.cmdstop(1)
                    self.btapi.BR_TX(chan=chan, len=br_len, ptype=7, rate=_rate)
                    res1 = tester.stx.get_power_measure_res()
                res2 = tester.stx.get_acp_res()
                print(res2)
                if eval(res2[0]) != 0:
                    self.btapi.cmdstop(1)
                    self.btapi.BR_TX(chan=chan, len=br_len, ptype=7, rate=_rate)
                    res2 = tester.stx.get_acp_res()
                res3 = tester.stx.get_obw_res()
                print(res3)
                if eval(res3[0]) != 0:
                    self.btapi.cmdstop(1)
                    self.btapi.BR_TX(chan=chan, len=br_len, ptype=7, rate=_rate)
                    res3 = tester.stx.get_obw_res()
                logdebug('{}'.format(res1))
                logdebug('{}'.format(res2))
                logdebug('{}'.format(res3))

                nominal_pow = eval(res1[2])
                peak_pow = eval(res1[3])
                leakage_pow = eval(res1[4])
                PacketTiming = eval(res1[5])
                acp_list = [eval(i) for i in res2[1:]]
                print (acp_list)

                acp_center = 10
                acp_max_pwr = acp_list[acp_center]
                acp_r4 = acp_list[acp_center + 4]
                acp_r3 = acp_list[acp_center + 3]
                acp_r2 = acp_list[acp_center + 2]
                acp_r1 = acp_list[acp_center + 1]
                acp_l1 = acp_list[acp_center - 1]
                acp_l2 = acp_list[acp_center - 2]
                acp_l3 = acp_list[acp_center - 3]
                acp_l4 = acp_list[acp_center - 4]
                obw = eval(res3[6])/1000.00
                obw_l = eval(res3[4])/1000.00
                obw_h = eval(res3[5])/1000.00


                time.sleep(0.5)
                self.btapi.cmdstop(1)
                self.btapi.BR_TX(chan=0, len=br_len, ptype=7, rate=_rate)
                tester.stx.analyzer_settings(enpower=target_power, freq=2402)
                res4 = tester.stx.get_frange_res()
                print(res4)
                if eval(res4[0]) != 0:
                    self.btapi.cmdstop(1)
                    self.btapi.BR_TX(chan=0, len=br_len, ptype=7, rate=_rate)
                    res4 = tester.stx.get_frange_res()
                logdebug('{}'.format(res4))
                frange_l = eval(res4[3])/1000.00

                self.btapi.cmdstop(1)
                self.btapi.BR_TX(chan=78, len=br_len, ptype=7, rate=_rate)
                tester.stx.analyzer_settings(enpower=target_power, freq=2480)
                res4 = tester.stx.get_frange_res()
                print(res4)
                if eval(res4[0]) != 0:
                    self.btapi.cmdstop(1)
                    self.btapi.BR_TX(chan=78, len=br_len, ptype=7, rate=_rate)
                    res4 = tester.stx.get_frange_res()
                logdebug('{}'.format(res4))
                frange_h = eval(res4[4])/1000.00
                self.btapi.cmdstop(1)

                loginfo("channel: {}    packet type: {}     payload length: {}".format(chan, DH, len))
                loginfo("nominal power: {}      peak power: {}      leakage power: {}   unit: dBm".format(nominal_pow, peak_pow, leakage_pow))
                loginfo("freq accuracy: {}      freq drift: {}      drift rate: {}  unit: Hz".format(freq_accuracy, freq_drift, drift_rate))
                loginfo("delta f1 avg: {}       delta f1 min: {}       delta f1 max: {}  unit: Hz".format(delta_f1_avg, delta_f1_min, delta_f1_max))
                loginfo("delta f2 avg: {}       delta f2 min: {}       delta f2 max: {}  unit: Hz".format(delta_f2_avg, delta_f2_min, delta_f2_max))
                loginfo("mod ratio: {}".format(mod_ratio))
                loginfo("delta f2 99.9%: {}  unit: Hz".format(delta_f2_99))
                loginfo("spectrum 20 dB bandwidth: {}".format(obw))
                loginfo("spectrum freq range: {} -- {} MHz".format(frange_l, frange_h))

                if fig_en != 0:
                    plt.ion()
                    x = [2402+chan+xi for xi in range(-10, 11, 1)]
                    fig = plt.figure('br_acp_channel{}_{}'.format(chan,DH))
                    fig.set_size_inches(13, 7)
                    ax = fig.add_subplot(111)
                    ax.bar(x, 80+np.array(acp_list), width=0.5, bottom=-80)
                    ax.set_xticks(np.array(x))
                    ax.set_xlabel('freq(MHz)')
                    ax.set_ylabel('txp(dBm)')
                    ax.set_title('BR_ACP')
                    for xi,yi in zip(x,acp_list):
                        ax.text(xi-0.25, yi+0.25, '%.2f'%yi, fontsize=8)
                    plt.savefig(fname+'br_acp_channel{}_{}_{}'.format(chan,DH,time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))))
                    # plt.show()
                if report_save:
                    df = pd.DataFrame(pd.read_csv(fw2.filename))
                    df_value = [chan,DH,nominal_pow,peak_pow,leakage_pow,PacketTiming,frange_l,frange_h,obw_l,obw_h,obw,acp_max_pwr,acp_l4,acp_l3,
                                                           acp_l2,acp_l1,acp_r1,acp_r2,acp_r3,acp_r4,delta_f1_avg,delta_f2_avg,delta_f2_99,mod_ratio,freq_accuracy,'',freq_drift,
                                                           '','',drift_rate,'','','']
                    print (len(df_value))
                    df['channel_{}_{}'.format(chan,DH)] = df_value
                    df.to_csv(fw2.filename,index=False)
                if csv_save:
                    fw1.write_data([chan,DH,nominal_pow,peak_pow,leakage_pow,freq_accuracy,freq_drift,drift_rate,delta_f1_avg,delta_f1_min,delta_f1_max,delta_f2_avg,delta_f2_min,delta_f2_max,mod_ratio,delta_f2_99,obw,frange_l,frange_h,acp_list])
                else:
                    res_list.append([chan,DH,nominal_pow,peak_pow,leakage_pow,freq_accuracy,freq_drift,drift_rate,delta_f1_avg,delta_f1_min,delta_f1_max,delta_f2_avg,delta_f2_min,delta_f2_max,mod_ratio,delta_f2_99,obw,frange_l,frange_h,acp_list])
        return res_list


    def edr_tx(self,chan_list=[0,39,78], rfport=2, cable_loss=1, rate_list=['2_DH1'],  target_power=10, fig_en=1, csv_save=True, report_save=True):
        if csv_save:
            title = 'rate,channel,nominal_pwr(dBm),peak_pwr(dBm),gfsk_pwr(dBm),dpsk_pwr(dBm),dpsk_gfsk_diff_pwr,guard_period(us),'
            title = title + 'wi(KHz),w0_wi(KHz),w0_max(KHz),DEVM_RMS(%),DEVM_peak(%),DEVM_P99(%),bit_error_rate,packet0error,'
            title = title + 'PTxRef(dBm),N26ChN1Abs(dBm),N26ChP1Abs(dBm),N26ChN1Rel(dBm),N26ChP1Rel(dBm),acp_list\n'
            fname = rfglobal.get_filename('ts_bt_test/', 'test_edr_tx_{}'.format(self.board_name))
            fw1 = csvreport(fname, title)
        if report_save:
            title2 = 'BR_tx_performance'
            fname2 = rfglobal.get_filename('ts_bt_test/','test_edr_tx_report_{}'.format(self.board_name))
            fw2=csvreport(fname2,title2)
            item = ['channel', 'rate', u'Tx/10 - EDR Relative Transmit Power - PGFSK - Max Power', u' - PDPSK',
                    u'- PDPSK - PGFSK',
                    u'@   - Nomimal Power',
                    u'@   - Guard Period',
                    u'@   - Packet Timing',
                    u'Tx/11 - CFS and MA - omega i',
                    u' - omega i + omega o',
                    u'- omega o',
                    u'- DEVM RMS',
                    u'- DEVM Peak',
                    u'- DEVM 99% - Max 0.30',
                    u'Tx/12 - EDR Differential Phase Encoding',
                    u'Tx/13 - In Band Spurious Emissins - Nominal Power',
                    u' - ACPower:-3',
                    u'- ACPower:-2',
                    u'- ACPower:-1,Ptx-26dB',
                    u' - ACPower:Center Ptxref',
                    u'- ACPower:1,Ptx-26dB',
                    u'- ACPower:+2',
                    u'- ACPower:+3',
                    u'- ACPower:+- >3',]
            df = pd.DataFrame(item)
            df.to_csv(fw2.filename, index=False)
        tester = tester_cmw(mode=0, rfport=rfport, cable_loss=cable_loss, bt_mode='EDR', freq=2402, target_power=target_power, burst_type='EDR', asyn='OFF', bdaddr='050604010203')
        # self.BT_INIT('EDR')
        self.btapi.cmdstop(1)
        self.btapi.cmdstop(0)
        self.btapi.BR_TX(chan=0, len=54, ptype=1, rate=2)
        for i in range(15):
            tester.stx.analyzer_settings(enpower=target_power, umargin=8, freq=2402)
            res = tester.stx.get_power_measure_res()
            if eval(res[0]) == 0:
                txpower = eval(res[3])
                target_power = txpower + 10
                break
            else:
                target_power = target_power - 5
        loginfo('target power set {}'.format(target_power))
        for rate in rate_list:
            for chan in chan_list:
                tester.stx.analyzer_settings(enpower=target_power, freq=2402+chan)
                edr_len = self.edr_len_dic[rate]
                _rate = self.edr_rate_dic[rate]
                self.btapi.cmdstop(1)
                self.btapi.BR_TX(chan=chan, len=edr_len, ptype=7, rate=_rate)
                res = tester.stx.get_modulation_measure_res()
                logdebug('{}'.format(res))

                res = [eval(i) for i in res[0:]]

                wi = res[2]/1000.00
                w0_wi = res[3]/1000.00
                w0_max = res[4]/1000.00
                DEVM_RMS = res[5]
                DEVM_peak = res[6]
                DEVM_P99 = res[7]

                res1 = tester.stx.get_power_measure_res()
                logdebug('{}'.format(res1))
                res1 = [eval(i) for i in res1[0:]]
                nominal_pwr = res1[2]
                gfsk_pwr = res1[3]
                dpsk_pwr = res1[4]
                dpsk_gfsk_diff_pwr = res1[5]
                guard_period = res1[6]
                packet_timing = res1[7]
                peak_pwr = res1[8]

                res2 = tester.stx.get_diff_phase_encoding_res()
                logdebug('{}'.format(res2))
                res2 = [eval(i) for i in res2[0:]]
                bit_error_rate = res2[2]
                packet0error = res2[3]

                [res3, res4] = tester.stx.get_acp_res_edr()
                logdebug('{}'.format(res3))
                logdebug('{}'.format(res4))
                res3 = [eval(i) for i in res3[0:]]
                res4 = [eval(i) for i in res4[0:]]
                acp_nominal_pwr = res3[2]
                PTxRef = res3[4]
                N26ChN1Abs = res3[5]
                N26ChP1Abs = res3[6]
                N26ChN1Rel = res3[7]
                N26ChP1Rel = res3[8]

                acp_list = res4[1:]
                acp_center = len(acp_list)/2
                acp_max_pwr = acp_list[acp_center]
                acp_r4 = acp_list[acp_center + 4]
                acp_r3 = acp_list[acp_center + 3]
                acp_r2 = acp_list[acp_center + 2]
                acp_r1 = acp_list[acp_center + 1]
                acp_l1 = acp_list[acp_center - 1]
                acp_l2 = acp_list[acp_center - 2]
                acp_l3 = acp_list[acp_center - 3]
                acp_l4 = acp_list[acp_center - 4]

                loginfo("channel: {}    packet type: {}     payload length: {}".format(chan, rate, len))
                loginfo("nominal power: {}      peak power: {}      gfsk_pwr: {}    dpsk_pwr: {}".format(nominal_pwr, peak_pwr, gfsk_pwr,dpsk_pwr))
                loginfo("dpsk_gfsk_diff_pwr: {}      guard_period: {}      ".format(dpsk_gfsk_diff_pwr, guard_period))
                loginfo("wi: {}       w0_wi: {}       w0_max: {}".format(wi, w0_wi, w0_max))
                loginfo("DEVM_RMS: {}       DEVM_peak: {}       DEVM_P99: {}".format(DEVM_RMS, DEVM_peak, DEVM_P99))
                loginfo("bit_error_rate: {}     packet0error: {}".format(bit_error_rate, packet0error))
                loginfo("PTxRef: {} N26ChN1Abs: {}  N26ChP1Abs: {}  N26ChN1Rel: {}  N26ChP1Rel:{}".format(PTxRef, N26ChN1Abs, N26ChP1Abs, N26ChN1Rel, N26ChP1Rel))

                if fig_en != 0:
                    plt.ion()
                    x = [2402+chan+xi for xi in range(-10, 11, 1)]
                    fig = plt.figure('edr_acp_channel{}_{}'.format(chan,rate))
                    fig.set_size_inches(13, 7)
                    ax = fig.add_subplot(111)
                    ax.bar(x, 80+np.array(acp_list), width=0.5, bottom=-80)
                    ax.set_xticks(np.array(x))
                    ax.set_xlabel('freq(MHz)')
                    ax.set_ylabel('txp(dBm)')
                    ax.set_title('%s_ACP'%rate)
                    for xi,yi in zip(x,acp_list):
                        ax.text(xi-0.25, yi+0.25, '%.2f'%yi, fontsize=8)
                    plt.savefig(fname + 'edr_acp_channel{}_{}_{}'.format(chan, rate, time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))))
                        # plt.show()
                if csv_save:
                    fw1.write_data([rate,chan,nominal_pwr,peak_pwr,gfsk_pwr,dpsk_pwr,dpsk_gfsk_diff_pwr,guard_period,wi,w0_wi,w0_max,DEVM_RMS,DEVM_peak,DEVM_P99,bit_error_rate,packet0error,PTxRef,N26ChN1Abs,N26ChP1Abs,N26ChN1Rel,N26ChP1Rel,acp_list])
                if report_save:
                    df = pd.DataFrame(pd.read_csv(fw2.filename))
                    df_value = [chan,rate,peak_pwr,dpsk_pwr,dpsk_gfsk_diff_pwr,nominal_pwr,guard_period,packet_timing,wi,w0_wi,w0_max,DEVM_RMS,DEVM_peak,DEVM_P99,'',
                                acp_nominal_pwr,acp_l3,acp_l2,N26ChN1Rel,PTxRef,N26ChP1Rel,acp_r2,acp_r3,max([acp_l4,acp_r4])]

                    df['channel_{}_{}'.format(chan,rate)] = df_value
                    df.to_csv(fw2.filename,index=False)
                self.cmdstop(1)


    def le_tx(self,chan_list=[0,19,38], rfport=2, cable_loss=1, rate_list=['LE1M'],  target_power=10, fig_en=1, csv_save=True, report_save=True):

        if csv_save:
            title = 'channel,type,nominal_pow(dBm),peak_pow(dBm),leakage_pow(dBm),freq_accuracy(KHz),freq_drift(KHz),drift_rate(Hz/50us),'
            title = title + 'delta_f1_avg(KHz),delta_f1_min(KHz),delta_f1_max(KHz),delta_f2_avg(KHz),delta_f2_min(KHz),delta_f2_max(KHz),mod_ratio,delta_f1_99(KHz),delta_f2_99(KHz),'
            title = title + 'acp_list_21ch\n'
            fname = rfglobal.get_filename('ts_bt_test/','test_le_tx_{}'.format(self.board_name))
            fw1=csvreport(fname,title)
        if report_save:
            title2 = 'BR_tx_performance'
            fname2 = rfglobal.get_filename('ts_bt_test/','test_le_tx_report_{}'.format(self.board_name))
            fw2=csvreport(fname2,title2)
            item = ['channel', 'rate', u'TP/TRM-LE/CA/BV-01-C - Output power  - Average Power', u' - Peak Power',
                    u'- Peak - Average Power',
                    u'- leakage Power',
                    u'TP/TRM-LE/CA/BV-03-C - In-Band Emissions -   -10',
                    u'TP/TRM-LE/CA/BV-03-C - In-Band Emissions -   -9',
                    u'TP/TRM-LE/CA/BV-03-C - In-Band Emissions -   -8',
                    u'TP/TRM-LE/CA/BV-03-C - In-Band Emissions -   -7',
                    u'TP/TRM-LE/CA/BV-03-C - In-Band Emissions -   -6',
                    u'TP/TRM-LE/CA/BV-03-C - In-Band Emissions -   -5',
                    u'TP/TRM-LE/CA/BV-03-C - In-Band Emissions -   -4',
                    u'TP/TRM-LE/CA/BV-03-C - In-Band Emissions -   -3',
                    u'TP/TRM-LE/CA/BV-03-C - In-Band Emissions -   -2',
                    u'TP/TRM-LE/CA/BV-03-C - In-Band Emissions -   -1',
                    u'TP/TRM-LE/CA/BV-03-C - In-Band Emissions -    Ptx',
                    u'TP/TRM-LE/CA/BV-03-C - In-Band Emissions -   1',
                    u'TP/TRM-LE/CA/BV-03-C - In-Band Emissions -   2',
                    u'TP/TRM-LE/CA/BV-03-C - In-Band Emissions -   3',
                    u'TP/TRM-LE/CA/BV-03-C - In-Band Emissions -   4',
                    u'TP/TRM-LE/CA/BV-03-C - In-Band Emissions -   5',
                    u'TP/TRM-LE/CA/BV-03-C - In-Band Emissions -   6',
                    u'TP/TRM-LE/CA/BV-03-C - In-Band Emissions -   7',
                    u'TP/TRM-LE/CA/BV-03-C - In-Band Emissions -   8',
                    u'TP/TRM-LE/CA/BV-03-C - In-Band Emissions -   9',
                    u'TP/TRM-LE/CA/BV-03-C - In-Band Emissions -   10',
                    u'TP/TRM-LE/CA/BV-05-C - Modulation Characteristics - Fre Accuracy',
                    u'- Delta F1 Avg',
                    u' - Delta F1 Min',
                    u' - Delta F1Max',
                    u'- Delta F2 Avg',
                    u'- Delta F2 Min',
                    u'- Delta F2Max',
                    u' - Delta F2 Max 99%',
                    u'- Delta F2 Avg/Delta F1 Avg',
                    u'- Frequency Accuracy',
                    u' - Frequency Offset',
                    u'- Frequency Drift',
                    u'- Max Drift Rate - 50us',
                    u'- Intial Frequency Drift',
                    ]
            df = pd.DataFrame(item)
            df.to_csv(fw2.filename, index=False)
        tester = tester_cmw(mode=0, rfport=rfport, cable_loss=cable_loss, bt_mode='LE1M', freq=2402, target_power=target_power, burst_type='LE', asyn='ON', bdaddr='050604010203')
        tester.stx.trigger_settings(source='power', threshold=-20, tout=1)
        self.btapi.cmdstop(0)
        self.btapi.cmdstop(1)
        res_lsit=[]
        for chan in chan_list:
            tester.stx.analyzer_settings(enpower=target_power, umargin=8, freq=2402+chan*2)
            for rate in rate_list:
                # self.BT_INIT(rate)
                _rate = self.le_rate_dic[rate]
                tester.stx.input_signal_settings(btype='LE', phy=rate)
                time.sleep(0.5)
                delta_f1_99,delta_f2_99,delta_f2_avg,delta_f2_min,delta_f2_max,mod_ratio = -999,-999,-999,-999,-999,-999
                if _rate > 2:
                    self.btapi.LE_TX(chan=chan, len=255, ptype=1, phy=_rate)
                    tester.stx.mode = 'LRANge'
                    res = tester.stx.get_modulation_measure_res()
                    if eval(res[0]) != 0:
                        self.btapi.cmdstop(0)
                        self.btapi.LE_TX(chan=chan, len=255, ptype=1, phy=_rate)
                        res = tester.stx.get_modulation_measure_res()
                    logdebug('{}'.format(res))

                    delta_f1_99 = eval(res[2])/1000.00
                    freq_accuracy = eval(res[3])/1000.00
                    freq_drift = eval(res[4])/1000.00
                    drift_rate = eval(res[5])
                    delta_f1_avg = eval(res[6])/1000.00
                    delta_f1_min = eval(res[7])/1000.00
                    delta_f1_max = eval(res[8])/1000.00
                else:
                    self.btapi.LE_TX(chan=chan, len=255, ptype=1, phy=_rate)
                    tester.stx.mode = rate
                    res = tester.stx.get_modulation_measure_res()
                    if eval(res[0]) != 0:
                        self.btapi.cmdstop(0)
                        self.btapi.LE_TX(chan=chan, len=255, ptype=1, phy=_rate)
                        res = tester.stx.get_modulation_measure_res()
                    logdebug('{}'.format(res))

                    delta_f1_avg = eval(res[6])/1000.00
                    delta_f1_min = eval(res[7])/1000.00
                    delta_f1_max = eval(res[8])/1000.00

                    time.sleep(0.5)
                    self.btapi.cmdstop(0)
                    self.btapi.LE_TX(chan=chan, len=255, ptype=2, phy=_rate)
                    res = tester.stx.get_modulation_measure_res()
                    if eval(res[0]) != 0:
                        self.btapi.cmdstop(0)
                        self.btapi.LE_TX(chan=chan, len=255, ptype=2, phy=_rate)
                        res = tester.stx.get_modulation_measure_res()
                    logdebug('{}'.format(res))

                    delta_f2_99 = eval(res[2])/1000.00
                    freq_accuracy = eval(res[3])/1000.00
                    freq_drift = eval(res[4])/1000.00
                    drift_rate = eval(res[5])
                    delta_f2_avg = eval(res[9])/1000.00
                    delta_f2_min = eval(res[10])/1000.00
                    delta_f2_max = eval(res[11])/1000.00
                    mod_ratio = delta_f2_avg/delta_f1_avg
                    freq_offset = eval(res[14])/1000.00
                    init_drift = eval(res[15]) / 1000.00

                time.sleep(0.5)
                self.btapi.cmdstop(0)
                self.btapi.LE_TX(chan=chan, len=255, ptype=0, phy=_rate)
                res1 = tester.stx.get_power_measure_res()
                if eval(res1[0]) != 0:
                    self.btapi.cmdstop(0)
                    self.btapi.LE_TX(chan=chan, len=255, ptype=0, phy=_rate)
                    res1 = tester.stx.get_power_measure_res()
                res2 = tester.stx.get_acp_res()
                if eval(res2[0]) != 0:
                    self.btapi.cmdstop(0)
                    self.btapi.LE_TX(chan=chan, len=255, ptype=0, phy=_rate)
                    res2 = tester.stx.get_acp_res()
                logdebug('{}'.format(res1))
                logdebug('{}'.format(res2))

                nominal_pow = eval(res1[2])
                peak_pow = eval(res1[3])
                peak_avg_pwr = eval(res1[5])
                leakage_pow = eval(res1[4])
                acp_list = [eval(i) for i in res2[1:]]
                acp_center = len(acp_list)/2
                acp_max_pwr = acp_list[acp_center]
                acp_r10 = acp_list[acp_center + 10]
                acp_r9 = acp_list[acp_center + 9]
                acp_r8 = acp_list[acp_center + 8]
                acp_r7 = acp_list[acp_center + 7]
                acp_r6 = acp_list[acp_center + 6]
                acp_r5 = acp_list[acp_center + 5]
                acp_r4 = acp_list[acp_center + 4]
                acp_r3 = acp_list[acp_center + 3]
                acp_r2 = acp_list[acp_center + 2]
                acp_r1 = acp_list[acp_center + 1]
                acp_l1 = acp_list[acp_center - 1]
                acp_l2 = acp_list[acp_center - 2]
                acp_l3 = acp_list[acp_center - 3]
                acp_l4 = acp_list[acp_center - 4]
                acp_l5 = acp_list[acp_center - 5]
                acp_l6 = acp_list[acp_center - 6]
                acp_l7 = acp_list[acp_center - 7]
                acp_l8 = acp_list[acp_center - 8]
                acp_l9 = acp_list[acp_center - 9]
                acp_l10 = acp_list[acp_center - 10]

                loginfo("channel: {}    packet type: {} ".format(chan, rate))
                loginfo("nominal power: {} dBm      peak power: {} dBm      leakage power: {} dBm ".format(nominal_pow, peak_pow, leakage_pow))
                loginfo("freq accuracy: {} Hz     freq drift: {} Hz     drift rate: {} Hz".format(freq_accuracy, freq_drift, drift_rate))
                loginfo("delta f1 avg: {}  Hz     delta f1 min: {} Hz      delta f1 max: {} Hz".format(delta_f1_avg, delta_f1_min, delta_f1_max))
                if _rate < 3:
                    loginfo("delta f2 avg: {} Hz      delta f2 min: {} Hz      delta f2 max: {} Hz".format(delta_f2_avg, delta_f2_min, delta_f2_max))
                    loginfo("mod ratio: {}".format(mod_ratio))
                    loginfo("delta f2 99.9%: {} Hz".format(delta_f2_99))
                else:
                    loginfo("delta f1 99.9%: {} Hz".format(delta_f1_99))


                if fig_en != 0:
                    plt.ion()
                    x = [2402+chan*2+xi for xi in range(-10, 11, 1)]
                    fig = plt.figure('le_acp_channel{}_{}'.format(chan,rate))
                    fig.set_size_inches(13, 7)
                    ax = fig.add_subplot(111)
                    ax.bar(x, 80+np.array(acp_list), width=0.5, bottom=-80)
                    ax.set_xticks(np.array(x))
                    ax.set_xlabel('freq(MHz)')
                    ax.set_ylabel('txp(dBm)')
                    ax.set_title('%s_ACP'%rate)
                    for xi,yi in zip(x,acp_list):
                        ax.text(xi-0.25, yi+0.25, '%.2f'%yi, fontsize=8)
                    plt.savefig(fname + 'le_acp_channel{}_{}_{}'.format(chan, rate, time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))))
                    # plt.show()
                if report_save:
                    df = pd.DataFrame(pd.read_csv(fw2.filename))
                    df_value = [chan,rate,nominal_pow,peak_pow,peak_avg_pwr,leakage_pow,acp_l10,acp_l9,acp_l8,acp_l7,acp_l6,acp_l5,acp_l4,acp_l3,acp_l2,acp_l1,acp_max_pwr,
                                acp_r1,acp_r2,acp_r3,acp_r4,acp_r5,acp_r6,acp_r7,acp_r8,acp_r9,acp_r10,freq_accuracy,delta_f1_avg,delta_f1_min,delta_f1_max,delta_f2_avg,
                                delta_f2_min,delta_f2_max,delta_f1_99,mod_ratio,freq_accuracy,freq_offset,freq_drift,drift_rate,init_drift]

                    df['channel_{}_{}'.format(chan,rate)] = df_value
                    df.to_csv(fw2.filename,index=False)
                if csv_save:
                    fw1.write_data([chan,rate,nominal_pow,peak_pow,leakage_pow,freq_accuracy,freq_drift,drift_rate,delta_f1_avg,delta_f1_min,delta_f1_max,delta_f2_avg,delta_f2_min,delta_f2_max,mod_ratio,delta_f1_99,delta_f2_99,acp_list])
                else:
                    res_lsit.append([chan,rate,nominal_pow,peak_pow,leakage_pow,freq_accuracy,freq_drift,drift_rate,delta_f1_avg,delta_f1_min,delta_f1_max,delta_f2_avg,delta_f2_min,delta_f2_max,mod_ratio,delta_f1_99,delta_f2_99,acp_list])

                self.btapi.cmdstop(0)

        return res_lsit



    def bt_per(self, rfport=2, cable_loss=5, chan=0, rate='1M_DH1', rxpwr_range=[-98,-20], pkt_num=1000, dirty_en=0, csv_save=True, device='CMW', num_of_machine=1):
        if csv_save:
            title = 'channel,rate,rxpwr,rev_pkg,total_pkg,err_bit,total_bit,err_bit_ratio(%)\n'
            fname = rfglobal.get_filename('ts_bt_test/','rw_per_{}_{}'.format(rate,chan))
            fw1 = csvreport(fname,title)
        perform_list = []
        rxpwr_max = max(rxpwr_range)
        rxpwr_min = min(rxpwr_range)

        if device == 'CMW':
            tester = tester_cmw(mode=1, rfport=rfport, cable_loss=cable_loss)
            tester.srx.gen_wave(repeat=pkt_num, data_rate=rate, dirty_en=dirty_en)
        else:
            tester = mxg.MXG(device, num_of_machine)
            tester.arb_waveform(rate=rate)
            tester.trriger_para_set(type='SINGle', count=pkt_num)
            tester.output_state(1, 1)
            tester.arb_state(1)

        for rxpwr in  range(rxpwr_min, rxpwr_max+1):
            tester.srx.para_settings(freq=2402 + chan, level=rxpwr)
            self.btapi.BR_RX()
            tester.srx.gen_switch('ON')
            time.sleep(pkt_num*2e-3)
            res = self.btapi.cmdstop(1)
            rev_pkg = res[1]
            err_bit = res[2]
            total_bit = res[3]
            err_bit_ratio = (100*err_bit+0.01)/total_bit
            if csv_save:
                fw1.write_data([chan,rate,rxpwr,rev_pkg,pkt_num,err_bit,total_bit,err_bit_ratio])
            perform_list.append([chan,rate,rxpwr,rev_pkg,pkt_num,err_bit,total_bit,err_bit_ratio])
        return perform_list

    def le_per(self, rfport=1, cable_loss=5, chan_list=[0], rate_list=['LE_1M'], rxpwr_range=[-98,-20], pkt_num=2000, dirty_en=0, csv_save=True, device='CMW',
               num_of_machine=1):
        self.btapi.cmdstop(0)
        self.btapi.cmdstop(1)
        # self.mem_ts.wrm(0xa0420004,30,16,0x1c4)
        if csv_save:
            title = 'channel,rate,rxpwr,total_pkg,rev_pkg,per(%)\n'
            fname = rfglobal.get_filename('ts_bt_test/','le_per_{}'.format(self.board_name))
            fw1 = csvreport(fname,title)
        perform_list = []
        rxpwr_max = max(rxpwr_range)
        rxpwr_min = min(rxpwr_range)
        for chan in chan_list:
            for rate in rate_list:
                if device == 'CMW':
                    tester = tester_cmw(mode=1, rfport=rfport, cable_loss=cable_loss)
                    tester.srx.gen_wave(repeat=pkt_num, data_rate=rate, dirty_en=dirty_en)
                else:
                    tester = mxg.MXG(device, num_of_machine)
                    tester.arb_waveform(rate=rate)
                    tester.trriger_para_set(type='SINGle', count=pkt_num)
                    tester.output_state(1,1)
                    tester.arb_state(1)

                if rate.find('LE_1M') != -1:
                    phy = 1
                else:
                    phy = 2
                for rxpwr in  range(rxpwr_min, rxpwr_max+1):
                    self.btapi.LE_RX(chan=chan, phy=phy, mod=0, countMode=0)
                    if device == 'CMW':
                        tester.srx.para_settings(freq=2402 + chan*2, level=rxpwr)
                        tester.srx.gen_switch('ON')
                    else:
                        tester.para_set(freq=2402+chan*2, power=rxpwr+cable_loss)
                        tester.trigger_on()
                    time.sleep(pkt_num*3e-3)
                    res = self.btapi.cmdstop(0)
                    print(res)
                    res = res[0].split('bleRxCount=')[1].strip('\r\n')
                    logdebug('rev_pkt:  {}'.format(res))
                    rev_pkg = eval(res)
                    per = (pkt_num-rev_pkg)*100.0/pkt_num
                    loginfo('{}     {}      {}      {}      {}      {}'.format(chan,rate,rxpwr,pkt_num,rev_pkg,per))
                    if csv_save:
                        fw1.write_data([chan,rate,rxpwr,pkt_num,rev_pkg,per])

                    perform_list.append([chan,rate,rxpwr,pkt_num,rev_pkg,per])
        return perform_list

    def le_rx_ci(self, rfport=1, cable_loss=5, chan_list=[0], rate_list=['LE_1M'], pkt_num=2000, dirty_en=0, csv_save=True, device_signal='N5182B', rxgain='0xfb'):
        self.dict_pwr_inter_freqoffset = {
            0: range(-90, -60),
            1: range(-80, -40),
            2: range(-52, -20),
            3: range(-41, -10),
            -1: range(-80, -40),
            -2: range(-52, -20),
            -3: range(-41, -10)
            }
        self.btapi.cmdstop(0)
        self.btapi.cmdstop(1)
        # self.mem_ts.wrm(0xa0420004,30,16,0x1c4)
        if csv_save:
            title = 'signal_channel,rate,freq_interference,rxpwr_interference,total_pkg,rev_pkg,per(%)\n'
            fname = rfglobal.get_filename('ts_bt_test/','le_rx_ci_{}'.format(self.board_name))
            fw1 = csvreport(fname,title)
        for chan in chan_list:
            for rate in rate_list:
                if device_signal == 'CMW':
                    tester_signal = tester_cmw(mode=1, rfport=rfport, cable_loss=cable_loss)
                    tester_signal.srx.gen_wave(repeat=pkt_num, data_rate=rate, dirty_en=dirty_en)
                    tester_signal.srx.para_settings(freq=2402 + chan*2, level=-67)
                    tester_interference = mxg.MXG()
                else:
                    tester_signal = mxg.MXG('N5182B',1)
                    tester_signal.arb_waveform(rate=rate)
                    tester_signal.trriger_para_set(type='SINGle', count=pkt_num)
                    tester_signal.output_state(1,1)
                    tester_signal.arb_state(1)
                    tester_signal.para_set(freq=2402 + chan*2, power=-67 + cable_loss)

                    tester_interference = mxg.MXG('N5182B',2)
                tester_interference.arb_waveform(rate=rate+'_PN15')
                tester_interference.trriger_para_set(type='CONT', count=pkt_num)
                tester_interference.output_state(1, 1)
                tester_interference.arb_state(1)

                if rate.find('LE_1M') != -1:
                    phy = 1
                    freq_inter_offset_list = [0,1,-1,2,-2,3,-3]
                else:
                    phy = 2
                    freq_inter_offset_list = [0, 2, -2, 4, -4, 6, -6]
                for freq_inter_offset in freq_inter_offset_list:
                    freq_inter = freq_inter_offset+2402+chan*2
                    pwr_list = self.dict_pwr_inter_freqoffset[freq_inter_offset/phy]
                    for power_inter in pwr_list:
                        tester_interference.para_set(freq=freq_inter, power=power_inter + cable_loss)
                        time.sleep(0.2)
                        loginfo('freq_inter:    {}      pwr_inter:  {}'.format(freq_inter,power_inter))
                        self.btapi.LE_RX(chan=chan, phy=phy, mod=0, countMode=0)
                        if device_signal == 'CMW':
                            tester_signal.srx.gen_switch('ON')
                        else:
                            tester_signal.trigger_on()
                        if phy == 2:
                            time.sleep(pkt_num * 3e-3)
                        else:
                            time.sleep(pkt_num * 1.5e-3)
                        res = self.btapi.cmdstop(0)
                        res = res[0].split('bleRxCount=')[1].strip('\r\n')
                        logdebug('rev_pkt:  {}'.format(res))
                        rev_pkg = eval(res)
                        per = (pkt_num - rev_pkg) * 100.0 / pkt_num
                        loginfo('{}     {}      {}      {}      {}      {}      {}'.format(chan, rate, freq_inter, power_inter, pkt_num, rev_pkg, per))
                        fw1.write_data([chan, rate, freq_inter, power_inter, pkt_num, rev_pkg, per])

    def le_rx_ci_rxgain(self, rxgain_list=[0xff,0xfd,0xfb,0xf9], rfport=1, cable_loss=5, chan_list=[0], rate_list=['LE_1M'], pkt_num=2000, dirty_en=0, csv_save=True,
                        device_signal='N5182B'):
        self.dict_pwr_inter_freqoffset = {
            0: range(-90, -60),
            1: range(-85, -50),
            2: range(-52, -30),
            3: range(-41, -18),
            -1: range(-85, -50),
            -2: range(-52, -30),
            -3: range(-41, -18)
            }
        self.btapi.cmdstop(0)
        self.btapi.cmdstop(1)
        self.mem_ts.wrm(0xa0420004,30,16,0x1c4)
        if csv_save:
            title = 'rxgain,signal_channel,rate,freq_interference,rxpwr_interference,total_pkg,rev_pkg,per(%)\n'
            fname = rfglobal.get_filename('ts_bt_test/','le_rx_ci_{}'.format(self.board_name))
            fw1 = csvreport(fname,title)
        for rxgain in rxgain_list:
            for chan in chan_list:
                for rate in rate_list:
                    if device_signal == 'CMW':
                        tester_signal = tester_cmw(mode=1, rfport=rfport, cable_loss=cable_loss)
                        tester_signal.srx.gen_wave(repeat=pkt_num, data_rate=rate, dirty_en=dirty_en)
                        tester_signal.srx.para_settings(freq=2402 + chan*2, level=-67)
                        tester_interference = mxg.MXG()
                    else:
                        tester_signal = mxg.MXG('N5182B',1)
                        tester_signal.arb_waveform(rate=rate)
                        tester_signal.trriger_para_set(type='SINGle', count=pkt_num)
                        tester_signal.output_state(1,1)
                        tester_signal.arb_state(1)
                        tester_signal.para_set(freq=2402 + chan*2, power=-67 + cable_loss)

                        tester_interference = mxg.MXG('N5182B',2)
                    tester_interference.arb_waveform(rate=rate+'_PN15')
                    tester_interference.trriger_para_set(type='CONT', count=pkt_num)
                    tester_interference.output_state(1, 1)
                    tester_interference.arb_state(1)

                    if rate.find('LE_1M') != -1:
                        phy = 1
                    else:
                        phy = 2
                    for freq_inter_offset in[0,1,-1,2,-2,3,-3]:
                        freq_inter = freq_inter_offset+2402+chan*2
                        pwr_list = self.dict_pwr_inter_freqoffset[freq_inter_offset]
                        for power_inter in pwr_list:
                            tester_interference.para_set(freq=freq_inter, power=power_inter + cable_loss)
                            time.sleep(0.2)
                            loginfo('freq_inter:    {}      pwr_inter:  {}'.format(freq_inter,power_inter))
                            self.mem_ts.wrm(0xa042205c, 7, 0, rxgain)
                            self.btapi.LE_RX(chan=chan, phy=phy, mod=0, countMode=0)
                            if device_signal == 'CMW':
                                tester_signal.srx.gen_switch('ON')
                            else:
                                tester_signal.trigger_on()
                            time.sleep(pkt_num * 1e-3)
                            res = self.btapi.cmdstop(0)
                            res = res[0].split('bleRxCount=')[1].strip('\r\n')
                            logdebug('rev_pkt:  {}'.format(res))
                            rev_pkg = eval(res)
                            per = (pkt_num - rev_pkg) * 100.0 / pkt_num
                            loginfo('{}     {}      {}      {}      {}      {}      {}      {}'.format(rxgain, chan, rate, freq_inter, power_inter, pkt_num, rev_pkg, per))
                            fw1.write_data([rxgain, chan, rate, freq_inter, power_inter, pkt_num, rev_pkg, per])

    def le_rx_blocking(self, rfport=1, cable_loss=5,  rate_list=['LE_1M'], inter_power_list=[], pkt_num=2000, dirty_en=0, csv_save=True, device_signal='N5182B'):
        self.btapi.cmdstop(0)
        self.btapi.cmdstop(1)
        # self.mem_ts.wrm(0xa0420004,30,16,0x1c4)
        if csv_save:
            title = 'rate,freq_blocking_1,freq_blocking_2,per(%)\n'
            fname = rfglobal.get_filename('ts_bt_test/','le_rx_blocking_{}'.format(self.board_name))
            fw1 = csvreport(fname,title)
        freq_blocking_1_list = []
        freq_blocking_2_list = []
        for rate in rate_list:
            if device_signal == 'CMW':
                tester_signal = tester_cmw(mode=1, rfport=rfport, cable_loss=cable_loss)
                tester_signal.srx.gen_wave(repeat=pkt_num, data_rate=rate, dirty_en=dirty_en)
                tester_signal.srx.para_settings(freq=2426, level=-67)
                tester_interference = mxg.MXG()
            else:
                tester_signal = mxg.MXG('N5182B', 1)
                tester_signal.arb_waveform(rate=rate)
                tester_signal.trriger_para_set(type='SINGle', count=pkt_num)
                tester_signal.output_state(1, 1)
                tester_signal.arb_state(1)
                tester_signal.para_set(freq=2426, power=-67 + cable_loss)

                tester_interference = mxg.MXG('N5182B', 2)
            tester_interference.output_state(1, 0)

            if rate.find('LE_1M') != -1:
                phy = 1
            else:
                phy = 2
            freq_range= range(30,2001,10)+range(2003,2400,3)+range(2484,2998,3)+range(3000,6000,25)
            freq_blocking_2 = 'NA'
            for inter_pwr in inter_power_list:
                for freq_inter in freq_range:
                    if freq_inter < 2001 or freq_inter > 2999:
                        tester_interference.para_set(freq=freq_inter, power=inter_pwr + cable_loss)
                    else:
                        tester_interference.para_set(freq=freq_inter, power=inter_pwr - 5 + cable_loss)
                    loginfo('freq_inter:    {}'.format(freq_inter))
                    # self.mem_ts.wrm(0xa042205c, 7, 0, rxgain)
                    self.btapi.LE_RX(chan=12, phy=phy, mod=0, countMode=0)
                    if device_signal == 'CMW':
                        tester_signal.srx.gen_switch('ON')
                    else:
                        tester_signal.trigger_on()
                    time.sleep(pkt_num * 1e-3)
                    res = self.btapi.cmdstop(0)
                    res = res[0].split('bleRxCount=')[1].strip('\r\n')
                    logdebug('rev_pkt:  {}'.format(res))
                    rev_pkg = eval(res)
                    per = (pkt_num - rev_pkg) * 100.0 / pkt_num
                    if per > 31:
                        freq_blocking_1 = freq_inter
                        freq_blocking_1_list.append(freq_blocking_1)
                        fw1.write_data([rate,freq_blocking_1,freq_blocking_2,per])

                freq_blocking_1 = 'NA'
                for freq_inter in freq_range:
                    tester_interference.para_set(freq=freq_inter, power=inter_pwr - 20 + cable_loss)
                    loginfo('freq_inter:    {}'.format(freq_inter))
                    # self.mem_ts.wrm(0xa042205c, 7, 0, rxgain)
                    self.btapi.LE_RX(chan=12, phy=phy, mod=0, countMode=0)
                    if device_signal == 'CMW':
                        tester_signal.srx.gen_switch('ON')
                    else:
                        tester_signal.trigger_on()
                    time.sleep(pkt_num * 1e-3)
                    res = self.btapi.cmdstop(0)
                    res = res[0].split('bleRxCount=')[1].strip('\r\n')
                    logdebug('rev_pkt:  {}'.format(res))
                    rev_pkg = eval(res)
                    per = (pkt_num - rev_pkg) * 100.0 / pkt_num
                    if per > 31:
                        freq_blocking_2 = freq_inter
                        freq_blocking_2_list.append(freq_blocking_2)
                        fw1.write_data([rate,freq_blocking_1,freq_blocking_2,per])
        return freq_blocking_1_list + [len(freq_blocking_1_list)], freq_blocking_2_list + [len(freq_blocking_2_list)]

    def bt_rx(self,rfport=2, cable_loss=5, chan_list=[0], rate_list=['1M_DH1'], rxpwr_range=[-98,-20], pkt_num=1000, dirty_en=0):
        tester = tester_cmw(mode=1, rfport=rfport, cable_loss=cable_loss)
        for chan in chan_list:
            for rate in rate_list:
                perform_list = self.bt_per(rfport=rfport, cable_loss=cable_loss, chan=chan, rate= rate, rxpwr_range=rxpwr_range, pkt_num=pkt_num, dirty_en=dirty_en)


    # def get_filename(self, folder, file_name, sub_folder=''):
    #     '''
    #     :folder: file store folder
    #     :file_name:  file name
    #     :sub_folder: if not need, it may be default ""
    #     '''
    #     if rfglobal.file_folder=="":
    #         rfdata_path = './rftest/rfdata/'
    #     else:
    #         rfdata_path = './rftest/rfdata/%s/'%rfglobal.file_folder
    #         if os.path.exists(rfdata_path) == False:
    #             os.mkdir(rfdata_path)
    #
    #     data_path1 = rfdata_path+'%s/'%(folder)
    #     if os.path.exists(data_path1) == False:
    #         os.mkdir(data_path1)
    #
    #     filetime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()));
    #     # mac = self.read_mac()
    #     mac = ''
    #
    #     gen_folder = '_%s'%(filetime[0:8])
    #     data_path2 = data_path1 +'%s/'%(gen_folder)
    #     if os.path.exists(data_path2) == False:
    #         os.mkdir(data_path2)
    #
    #     fname = '%s'%(file_name)
    #     outfile_name = data_path2 + fname
    #
    #     if sub_folder != '':
    #         gen_folder = '%s_%s'%(sub_folder,filetime[0:8])
    #         sub_path = data_path2+'%s/'%(gen_folder)
    #         if os.path.exists(sub_path) == False:
    #             os.mkdir(sub_path)
    #
    #         outfile_name = sub_path + file_name
    #
    #     return outfile_name