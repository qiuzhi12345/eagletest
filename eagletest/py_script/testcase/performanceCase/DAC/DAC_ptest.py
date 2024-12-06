# -- coding: utf-8 --
# 中文支持

from baselib.test_channel.com import COM as com
import baselib.instrument.dm as dm
from baselib.loglib.log_lib import *
from hal.Init import HALS
from hal.common import CHIP_ID
from baselib.tc_platform.common import *
import os, sys
import re
import csv
import numpy as np
import time
import glob
import pandas as pd
import matplotlib.pyplot as plt

class DAC_TC_PERF(object):
    """
    用于 DAC 遍历测试： 
       
    """
    def __init__(self, channel, chipv = "AUTO"):
        self.chip = HALS(channel, chipv)
        self.channel = self.chip.channel
        self.chipv = self.chip.chipv

    def __dm_acq_dac(self, chk_num, drange='[0,3.3]'):
        thres_l, thres_h=eval(drange)
        while chk_num:
            dm_res=mydm.get_result(name='VDC' ,data_type = 'MAX')
            try:
                data_res=float(dm_res)
                if data_res<thres_h and data_res>thres_l:
                    break
            except:
                logwarn("dm error")
                mydm.reset()
                chk_num=chk_num-1
                continue
        return float(dm_res)

    def __tc_dac_scan(self, para, log):
        '''
        para[0]:  dac_en=[1,1]
        para[1]:  din_rg=[0,256]
        para[2]:  step
        para[3]:  repeat_num
        '''    
        dac_en      = para[0]
        din_rg      = para[1]
        step        = para[2]
        repeat_num  = para[3]
        chipmac=CHIP_ID(self.channel, self.chipv).chip_mac()
        log.write_value('chip_mac', chipmac)
        for din in range(din_rg[0], din_rg[1], step):
            if dac_en[0]:
                for i in range(repeat_num):
                    self.chip.dac.dc_out(1, din)
                    dac1_res = self.__dm_acq_dac(3)
                    log.write_value('dac1_din%s_%s'%(din, i), dac1_res)
            if dac_en[1]:
                for i in range(repeat_num):
                    self.chip.dac.dc_out(2, din)
                    dac2_res = self.__dm_acq_dac(3)
                    log.write_value('dac2_din%s_%s'%(din, i), dac2_res)
        pass

    #   socket test
    def tc_chip_socket_loop(self, dac_en, din_rg, step, repeat_num, chn_thc, device="", temper_list="[]", mode=0, binname='eagle.app.pro.flash.bin'):
        """
        the module is used to test chips in specific sockets or modules on ESP_Test Board
        """
        self.mode   = mode
        self.binname= binname
        self.chip   = HALS(self.channel, self.chipv)
        self.mydm   = dm.dm()

        logname = "dac_ptest/din%s_%s_%s_%s"%(din_rg[0], step, din_rg[1], device)
        stest = socket_test(self.channel, logname, chn_thc, device, self.__tc_dac_scan, dac_en, din_rg, step, repeat_num)
        stest.socket_set(self.binname, self.mode)
        stest.run(eval(self.temper_list))

    # multiboard test
    def __pad_cfg(self, chip_sel):
        '''
        dac_pad hard-wired together outside on old multiboards, thus idle dac pads should be floating
        '''
        self.mcu.mcu_sel(chip_sel)
        time.sleep(2)
        self.mux.dac.dac_out(1,0)
        self.mux.gpio.dig_gpio_hang_up(25)
        self.mux.dac.dac_out(2,0)
        self.mux.gpio.dig_gpio_hang_up(26)

    def __multiboard_init(self):
        '''
        cols    : input column names, should be an array of strings
        pad_cfg: initial configuration including pads initial state setting and working states of relative instruments 
        '''
        chip_array=Multiboard_Prep(self.com_mcu, self.com_mux, self.board_ver).multiboard_test_pre(chip_list)
        chip_num=chip_array.keys()
        if len(chip_num)!=len(self.chip_list):
            logerror("!!At least one module failed in connection!!")
            return -1
        for chip_sel in self.chip_list:
            self.__pad_cfg(chip_sel) 

    # def __tc_dac_multiboard_wrap(self, para, log):
    #     '''
    #     para[0]:  dac_en=[1,1]
    #     para[1]:  din_rg=[0,256]
    #     para[2]:  step
    #     para[3]:  repeat_num
    #     '''    
    #     dac_en      = para[0]
    #     din_rg      = para[1]
    #     step        = para[2]
    #     repeat_num  = para[3]
    #     for chip_sel in range(len(self.chip_list)):
    #         self.mcu.mcu_sel(chip_sel)
    #         loginfo("start to test chip%d"%chip_sel)
    #         self.__tc_dac_scan(dac_en, din_rg, step, repeat_num, log)

    def tc_chip_multiboard_loop(self, dac_en, din_rg, step, repeat_num, com_mcu, board_ver, chip_list='range(0,32)', chn_thc=1, device="", temper_list="[]", mode=0, binname='eagle.app.pro.flash.bin'):
        """
        the module is used to test chips in specific sockets or modules on ESP_Test Board
        """
        self.mode   = mode
        self.binname= binname
        self.mcu = Multiboard_CTL(com_mcu)
        self.mux = HALS(self.channel)
        self.chip_list=eval(chip_list)
        self.board_ver = board_ver
        self.mydm   = dm.dm()
        #self.temper_list=eval(temper_list)

        logname = "dac_ptest/din%s_%s_%s_%dpcs_%s"%(din_rg[0], step, din_rg[1], len(self.chip_list), device)
        mtest = multiboard_test(com_mcu, logname, self.board_ver, chn_thc, device, chip_list, self.__tc_dac_scan, dac_en, din_rg, step, repeat_num)
        self.__multiboard_init()

        mtest.run(eval(self.temper_list))