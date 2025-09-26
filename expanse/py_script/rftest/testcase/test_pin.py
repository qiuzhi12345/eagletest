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
class testpin(object):
    def __init__(self, comport, chipv='tx232', jlink_en=1, jlink='59610138'):
        self.comport = comport
        self.chipv = chipv
        self.mem_ts = MEM_TS(self.comport)
        if jlink_en!=0:
            self.jlink = jlink
            self.jlink.wrm(0xa0200258, 10, 6, 6)

    def bbpll_en(self, en=1):

        if self.chipv == 'TX232_MPW3':
            if en !=0:
                self.jlink.wrm(0xa01200cc, 29, 29, 1)  ##bbpll_bg_pup enbale
                self.jlink.wrm(0xa0000144, 25, 25, 1)  ##bbpll_bg_pup_ibg_bbpll
                # self.jlink.wrm(0xa0000144, 29, 29, 1)  ##bbpll_bg_pup_ibg_tbuf
                self.jlink.wrm(0xa0000144, 20, 20, 1)  ##bbpll_bg_fc on
                self.jlink.wrm(0xa01200cc, 22, 22, 1)  ##rf_aon_xo_en_clk_ana
                self.jlink.wrm(0xa01200cc, 20, 20, 1)  ##rf_aon_xo_en_clk_ref
                self.jlink.wrm(0xa0000144, 23, 23, 1)  ##bbpll_ldo_pup
                self.jlink.wrm(0xa0000144, 22, 22, 1)  ##bbpll_pup
                self.jlink.wrm(0xa0000144, 21, 21, 0)  ##bbpll_ld_pd
                self.jlink.wrm(0xa0000144, 18, 18, 1)  ##bbpll_ldo_fc on
                self.jlink.wrm(0xa0000144, 17, 17, 1)  ##bbpll_vco_fast_en on

                ##wait 40us and end bbpll fast charge
                self.jlink.wrm(0xa0000144, 20, 20, 0)  ##bbpll_bg_fc off
                self.jlink.wrm(0xa0000144, 18, 18, 0)  ##bbpll_ldo_fc off
                self.jlink.wrm(0xa0000144, 17, 17, 0)  ##bbpll_vco_fast_en off
                self.jlink.wrm(0xa0000144, 16, 16, 1)  ##bbpll_ck_dig_en
                self.jlink.wrm(0xa0000144, 15, 15, 1)  ##bbpll_ck_codec_en
            else:
                self.jlink.wrm(0xa0000144, 23, 23, 0)  ##bbpll_ldo_pup
                self.jlink.wrm(0xa0000144, 22, 22, 0)  ##bbpll_pup
                # self.jlink.wrm(0xa01200cc, 29, 29, 0)  ##bbpll_bg_pup disbale
                self.jlink.wrm(0xa0000144, 25, 25, 0)  ##bbpll_bg_pup_ibg_bbpll
        else:
            if en!=0:
                self.jlink.wrm(0xa01200a0, 25, 25, 1)  ##bbpll_bg_pup_ibg
                self.jlink.wrm(0xa01200a0, 29, 29, 1)  ##bbpll_bg_pup_ibg_tbuf
                self.jlink.wrm(0xa01200a0, 20, 20, 1)  ##bbpll_bg_fc on
                self.jlink.wrm(0xa01200cc, 22, 22, 1)  ##rf_aon_xo_en_clk_ana
                self.jlink.wrm(0xa01200cc, 20, 20, 1)  ##rf_aon_xo_en_clk_ref
                self.jlink.wrm(0xa01200a0, 23, 23, 1)  ##bbpll_ldo_pup
                self.jlink.wrm(0xa01200a0, 22, 22, 1)  ##bbpll_pup
                self.jlink.wrm(0xa01200a0, 21, 21, 0)  ##bbpll_ld_pd
                self.jlink.wrm(0xa01200a0, 18, 18, 1)  ##bbpll_ldo_fc on
                self.jlink.wrm(0xa01200a0, 17, 17, 1)  ##bbpll_vco_fast_en on

                ##wait 40us and end bbpll fast charge
                self.jlink.wrm(0xa01200a0, 20, 20, 0)  ##bbpll_bg_fc off
                self.jlink.wrm(0xa01200a0, 18, 18, 0)  ##bbpll_ldo_fc off
                self.jlink.wrm(0xa01200a0, 17, 17, 0)  ##bbpll_vco_fast_en off
                self.jlink.wrm(0xa01200a0, 16, 16, 1)  ##bbpll_ck_dig_en
                self.jlink.wrm(0xa01200a0, 15, 15, 1)  ##bbpll_ck_codec_en
            else:
                self.jlink.wrm(0xa01200a0, 23, 23, 0)  ##bbpll_ldo_pup
                self.jlink.wrm(0xa01200a0, 22, 22, 0)  ##bbpll_pup

    def frac_pll(self,en=1):
        if en!=0:
            self.jlink.wrm(0xa000014c, 1, 1, 0)  ##frac_pll_resetn
            self.jlink.wrm(0xa000014c, 0, 0, 1) ##frac_pll enable
            self.jlink.wrm(0xa000014c, 1, 1, 1) ##frac_pll_resetn
        else:
            self.jlink.wrm(0xa000014c, 1, 1, 0)  ##frac_pll_resetn
            self.jlink.wrm(0xa000014c, 0, 0, 0) ##frac_pll enable


    def mclk1_test(self,mclk1_sel=1):
        '''
        0xa0200258[10:6]不能等于0，否则PA0上拉不出来时钟
        mclk1_sel:
        00: clk_pll0_out
        01: clk_pll1_out
        10: clk_hfrc_out
        '''
        self.jlink.wrm(0xa0200258, 10, 6, 6)
        self.jlink.wrm(0xa0200240,2,0,3)    ##PA0 func set testpin_clk
        self.jlink.wrm(0xa0200258, 5, 1, 21)    ##PA0 testpin test_clk_sel  codec_adc5_clk
        self.jlink.wrm(0xa0000044, 14, 13, 3,lsb_dis=1)     ##mclk1 enable and codec_adc5_clk enable
        self.jlink.wrm(0xa0000050,1,0,mclk1_sel)

    def mclk0_test(self,mclk0_sel=1):
        '''
        mclk0_sel:
        00: clk_pll_out,divided pll clk
        01: clk_hfrc_out(48m)
        10: clk_hfxo_out(24m)
        11: doubler clock out
        '''
        self.jlink.wrm(0xa0200258, 10, 6, 6)
        self.jlink.wrm(0xa0200240,2,0,3)
        self.jlink.wrm(0xa0200258, 5, 1, 7)
        self.jlink.wrm(0xa01200cc, 31, 31, 1)   ##doubler clock enable
        self.bbpll_en(1)
        self.jlink.wrm(0xa00000a8, 1, 0, mclk0_sel)

    def sys_clk_set(self, clk=170):
        pllput_div_init = self.jlink.rdm(0xa00000a4, 31, 24)
        clkbus_div_init = self.jlink.rdm(0xa0000054, 31, 0)
        clkm4_div_init = self.jlink.rdm(0xa0000058, 31, 0)
        loginfo('pllput_div_init:   {}  clkbus_div_init:    {}  clkm4_div_init: {}'.format(hex(pllput_div_init),hex(clkbus_div_init),hex(clkm4_div_init)))

        self.jlink.wrm(0xa00000a8, 1, 0, 1)     ##mclk0 set rc48m
        self.frac_pll(1)    ##fracpll enable
        self.frac_pll_freq_set(clk)
        self.jlink.wrm(0xa00000a4, 31, 24, 0)   ##pllout div set 0
        self.jlink.wrm(0xa0000054, 31, 0, 0)  ##mclk0_g div/ahb/apb2/apb0 div set 0
        self.jlink.wrm(0xa0000058, 31, 0, 0)  ##m4_ap_system_clk/m4_system_clk div set 0

        time.sleep(0.5)
        self.jlink.wrm(0xa00000a8, 3, 3, 1)  ##mclk0 pll sel fracpll
        self.jlink.wrm(0xa00000a8, 1, 0, 0)  ##mclk0 set pll


    def frac_pll_freq_set(self, freq=150):
        '''
        freq
        unit:   MHz
        range:  144--304    MHz
        accuracy:   62.5    kHz
        '''
        self.jlink.wrm(0xa000014c, 1, 1, 0)  ##frac_pll_resetn disable
        self.jlink.wrm(0xa000014c, 2, 2, 1)  ##frac divider enable
        fn = int((freq/8)-18)
        divf =int(((freq%8)/8.000)*(2**16))
        loginfo('{}     {}'.format(fn,divf))
        self.jlink.wrm(0xa000014c, 7, 3, fn)  ##FN select
        self.jlink.wrm(0xa000014c, 1, 1, 1)  ##frac_pll_resetn enable
        self.jlink.wrm(0xa000014c, 31, 16, divf)  ##FD select
        # self.jlink.wrm(0xa000014c, 1, 1, 1)  ##frac_pll_resetn enable

    def frac_divf_set(self, divf=0x0):
        self.jlink.wrm(0xa000014c, 1, 1, 0)  ##frac_pll_resetn disable
        self.jlink.wrm(0xa000014c, 31, 16, divf)  ##FD select
        self.jlink.wrm(0xa000014c, 1, 1, 1)  ##frac_pll_resetn enable

    def frac_pll_looptest(self, freq_list=[150,300],loop_count=1000):
        '''
        frac_clk拉到mclk1上，mclk1拉到PA0上，PA0信号耦合到RF trace来测试
        freq为非8的整数倍数
        '''
        title = 'freq_center(MHz),freq_divf-1(MHz),freq_center(MHz),freq_divf+1(MHz),freq_center_ld,freq_divf-1_ld,freq_center1_ld,freq_divf+1_ld,txp1,' \
                'txp2,txp3,txp4,divf,step\n'
        fname = rfglobal.get_filename('ts_bt_test/', 'frac_pll_looptest')
        fw1 = csvreport(fname, title)
        self.jlink.wrm(0xa0200258, 10, 6, 6)
        self.jlink.wrm(0xa0200240,2,0,3)
        self.jlink.wrm(0xa0200258, 5, 1, 8)     ##PA0 testpin test_clk_sel mclk1
        self.jlink.wrm(0xa0000044, 13, 13, 1,lsb_dis=1)
        self.jlink.wrm(0xa0000050,1,0,1)
        self.frac_pll(en=1)

        myspa = Agilent()
        myspa.set_reflvl(-10)
        myspa.set_rb_HZ(100)
        myspa.set_vb_HZ(100)
        myspa.set_span(1)

        import matplotlib.pyplot as plt
        import numpy as np
        import time
        from math import *



        for freq in freq_list:
            plt.ion()  # 开启interactive mode 成功的关键函数
            plt.figure(freq)
            per_list = []
            t = 0
            t_list = []
            self.frac_pll_freq_set(freq=freq)

            divf = int(((freq % 8) / 8.000) * (2 ** 16))
            step = (1<<10)
            myspa.set_cfreq(freq)
            for loop in range(loop_count):
                ld_list=[]
                self.frac_divf_set(divf)
                res = myspa.pk_search_timesleep(timesleep=1)
                freq_center = res[0][0]
                txp1 = res[0][1]
                ld = self.jlink.rdm(0xa0000150,3,3)
                ld_list.append(freq_center)

                self.frac_divf_set(divf-step)
                res = myspa.pk_search_timesleep(timesleep=1)
                freq_divf1 = res[0][0]
                txp2 = res[0][1]
                ld1 = self.jlink.rdm(0xa0000150, 3, 3)
                ld_list.append(freq_divf1)

                self.frac_divf_set(divf)
                res = myspa.pk_search_timesleep(timesleep=1)
                freq_center1 = res[0][0]
                txp3 = res[0][1]
                ld2 = self.jlink.rdm(0xa0000150,3,3)
                ld_list.append(freq_center1)

                self.frac_divf_set(divf+step)
                res = myspa.pk_search_timesleep(timesleep=1)
                freq_divf2 = res[0][0]
                txp4 = res[0][1]
                ld3 = self.jlink.rdm(0xa0000150, 3, 3)
                ld_list.append(freq_divf2)

                loginfo('{}'.format(freq_center,freq_divf1,freq_divf2,ld,ld1,ld2))
                fw1.write_data([freq_center,freq_divf1,freq_center1,freq_divf2,ld,ld1,ld2,ld3,txp1,txp2,txp3,txp4,divf,hex(step)],float_num=6)

                plt.clf()  # 清空画布上的所有内容

                for i in range(len(ld_list)):
                # time.sleep(time_interval)
                    t = t+1
                    # per = eval(res[1])
                    per_list.append(ld_list[i])
                    t_list.append(t)
                    plt.plot(t_list,per_list, '-r')
                    plt.pause(0.01)
                loop = loop+1

    def rw_validate(self,diag_cntl=0x29):
        '''

        '''
        self.jlink.wrm(0xa0200258,11,6,14)  ##{bt_sys_bt_dbg1,bt_sys_bt_dbg2}
        self.jlink.wrm(0xa0200240,26,3,3|(3<<3)|(3<<6)|(3<<9)|(3<<12)|(3<<15)|(3<<18)|(3<<21))  ##PA1--8 set testpin
        self.jlink.wrm(0xa0400450, 23, 23, 1)   ##bt_sys_bt_dbg2 enable
        self.jlink.wrm(0xa0400450, 22, 16, diag_cntl)   ##diag_cntl


