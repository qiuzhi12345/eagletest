import baselib.test_channel.channel as chn
import baselib.test_channel.com as com
from baselib.instrument.tester_serv import *
from baselib.loglib.log_lib import *
import time
import csv
from baselib.plot import *
from baselib.instrument import *
from baselib.instrument import tester
import numpy as np
import pylab as plt
import matplotlib.pyplot as plt
import re
import serial
from rftest.rflib.rfpll import rfpll
from hal.wifi_api import WIFIAPI
from rftest.rflib import rfglobal
import rftest.rflib.wifi_instrum as wifi_instrum
from rftest.rflib.wifi_lib import WIFILIB
from hal.common import MEM
from rftest.rflib.rfpll import rfpll
import rftest.rflib.utility.iofunc as iofunc
from rftest.rflib.csv_report import csvreport
from hal.hwregister.hwi2c.all import *
from rftest.rflib.pbus import pbus
from rftest.testcase.rf_debug.basic_test import BasicTest
from rftest.testcase.rf_debug.rx_gain_sweep import Sweep_RX_Gain
from rftest.testcase.rf_debug.tx_gain_sweep import Sweep_TX_Gain
from rftest.testcase.rf_debug.i2c_sweep import I2C_SWEEP
from rftest.testcase.performance.wifi_txrx_test import WIFI_TXRX_TEST
from rftest.testcase.rf_debug.rfpll_test import RFPLL_TEST
from rftest.testcase.performance.wifi_feature_case import WIFI_Feature_Case
from rftest.testcase.rf_debug.pa_test import PA_OutPwr
from rftest.testcase.rf_debug.power_detect import PwrDet

rate_all = rfglobal.test_rate_all
rate_comm = rfglobal.test_rate_comm


class RF_TEST_CASE(object):

    def __init__(self,comport,chipv='ESP32'):
        self.comport = comport
        self.chipv = chipv
        self.mem = MEM(self.comport,self.chipv)
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.wifiapi = WIFIAPI(self.comport,self.chipv)
        self.rfpll = rfpll(self.comport,self.chipv)
        self.i2c = HWI2C(self.comport,self.chipv)
        self.pbus = pbus(self.comport,self.chipv)
        self.rfpll_test = RFPLL_TEST(self.comport,self.chipv)
        self.basic_test = BasicTest(self.comport,self.chipv)
        self.rxgain = Sweep_RX_Gain(self.comport,self.chipv)
        self.txgain = Sweep_TX_Gain(self.comport,self.chipv)
        self.txrx = WIFI_TXRX_TEST(self.comport,self.chipv)
        self.i2c_sweep = I2C_SWEEP(self.comport,self.chipv)
        self.pa_test = PA_OutPwr(self.comport,self.chipv)
        self.pwrdet = PwrDet(self.comport,self.chipv)
        self.rate_all = rate_all
        self.rate_comm = rate_comm
        self.rate_ht40 = ['mcs0_40','mcs1_40','mcs2_40','mcs3_40','mcs4_40','mcs5_40','mcs6_40','mcs7_40']
        self.rx_range_comm = ['[-98,0]','[-90,0]','[-95,0]','[-75,0]','[-95,0]','[-72,0]','[-95,0]','[-72,0]']
        self.rx_range_all = ['[-98,10]','[-98,10]','[-95,10]','[-90,10]',
                            '[-95,10]','[-90,0]','[-90,0]','[-90,0]','[-90,0]','[-85,0]','[-80,0]','[-75,0]',
                            '[-95,10]','[-90,0]','[-90,0]','[-90,0]','[-90,0]','[-85,0]','[-80,0]','[-73,0]',
                            '[-95,10]','[-90,0]','[-90,0]','[-90,0]','[-90,0]','[-85,0]','[-80,0]','[-73,0]']

        self.channel_comm = [1,6,11,14]
        self.channel_all = range(1,15)


    def temp_vol_case(self, temp=25, vol=3.3, iqv_no=1, cable_att=2, name_str_in=''):
        name_str = '%dD_%2.2fV_%s'%(temp, vol, name_str_in)
        file_folder = 'temp_vol_case_%s'%(name_str)
        rfglobal.file_folder = file_folder

        self.wifi.save_init_print('init_print_%s'%name_str, name_str)

        # i2c clock
        self.basic_test.i2c_clk_test(name_str)

        # rfpll
##        self.rfpll_test.rfpll_cal_time(name_str)
        self.rfpll_test.rfpll_sweep(freq_start=2200, freq_end=2600, freq_step=2, name_str=name_str)
        self.rfpll_test.rfpll_cap_evm(cable_lose=cable_att, iqv_no=iqv_no,iqv_num=10,name_str=name_str)
##        self.rfpll_test.rfpll_cap_evm_unlock(cable_lose=cable_att, iqv_no=iqv_no,iqv_num=10,dm_en=0,name_str=name_str)

        # rx gain
        self.rxgain.sweep_rx_table(cable_att=cable_att, tx_chan=14, iqv_no=iqv_no, name_str=name_str, device='TESTER')
##        self.rxgain.sweep_rxgain_force(cable_att=cable_att, chan_step=13, rfrx_en=1, iqv_no=iqv_no, device='TESTER',name_str=name_str)
##        self.rxgain.i2c_rfrx_test(iqv_no=iqv_no,name_str=name_str,device='TESTER')

        # rx performance: rx sensitivity, rx range
        self.txrx.WIFI_RX_sens(cable_lose=cable_att, chan_in=[14], data_rate=self.rate_all, iqv_no=iqv_no, name_str=name_str)
        self.txrx.WIFI_RX_range(cable_lose=cable_att, chan_in=[14], data_rate=['11m', 'mcs7'], rx_range=[], iqv_no=iqv_no,name_str=name_str)
##        self.txrx.WIFI_RX_sens(cable_lose=cable_att, chan_in=self.channel_all, data_rate=self.rate_all, iqv_no=iqv_no, name_str=name_str)
##        self.txrx.WIFI_RX_range(cable_lose=cable_att, chan_in=self.channel_all, data_rate=self.rate_all, rx_range=self.rx_range_all, iqv_no=iqv_no,name_str=name_str)

        # tx performance
        self.txrx.WIFI_TX_PWR_EVM(cable_lose=cable_att, channel=self.channel_all, data_rate=self.rate_comm, iqv_no=iqv_no, iqv_num=20, name_str=name_str)



    def rx_gain_case(self,iqv_no=2, cable_att=0, case_flag=1, name_str=''):
        '''
        :case_flag: bit[0]-sweep_rx_table, bit[1]-rfrx_gain, bit[2]-bb_gain, bit[3]-lna_vga_dcap
        '''
        self.wifi.save_init_print('init_print_%s'%name_str, name_str)
##
##        # i2c clock
##        self.basic_test.i2c_clk_test(name_str)

        # RX gain table
        if case_flag & (1<<0):
            self.rxgain.sweep_rx_table(cable_att=cable_att, tx_chan=14, iqv_no=iqv_no, name_str=name_str, device='TESTER')

        # RFRX gain
        if case_flag & (1<<1):
            self.rxgain.sweep_rxgain_force(cable_att=cable_att, chan_step=5, rfrx_en=1, iqv_no=iqv_no, device='TESTER',name_str=name_str)

        # bb filter gain
        if case_flag & (1<<2):
            self.rxgain.sweep_rxgain_force(cable_att=cable_att, chan_step=5, rfrx_en=0, iqv_no=iqv_no, device='TESTER',name_str=name_str)

        # 'rfrx_lna_dcap','rfrx_vga_dcap','rfrx_mx_db' reg test
        if case_flag & (1<<3):
            self.rxgain.i2c_rfrx_test(chan=14, iqv_no=iqv_no, name_str=name_str, device='TESTER')

        if case_flag & (1<<4):
            cable_att=self.wifi.get_rx_cable_lost(iqv_unit_no=iqv_no, cable_att=30, chan_m=[1,2,3,4,5,6,7,8,9,10,11,12,13,14],noise_ref=-95.2)
            self.rxgain.sweep_rxgain_force_all_channel_radition(cable_att_list=cable_att, chan_step=5, rfrx_en=1, iqv_no=iqv_no, device='TESTER',name_str=name_str)


    def rfpll_test_case(self,cable_att=2,iqv_no=2, case_flag=1, name_str=''):
        '''
        :case_flag: bit[0]-pll_cal_time, bit[1]-rfpll_sweep, bit[2]-rfpll_cap_evm,bit[3]-rfpll_dac_evm
        '''
##        self.wifi.save_init_print('init_print_%s'%name_str, name_str)

        # i2c clock
##        self.basic_test.i2c_clk_test(name_str)

        if case_flag & (1<<0):
            self.rfpll_test.rfpll_cal_time(name_str)

        if case_flag & (1<<1):
            self.rfpll_test.rfpll_sweep(freq_start=2200, freq_end=2600, freq_step=2, name_str=name_str)

        if case_flag & (1<<2):
            self.rfpll_test.rfpll_cap_evm(cable_lose=cable_att, iqv_no=iqv_no,iqv_num=10,name_str=name_str)
        if case_flag & (1<<3):
            self.rfpll_test.rfpll_dac_evm(cable_lose=cable_att, iqv_no=iqv_no,iqv_num=10,name_str=name_str)


    def tx_perform_case(self, cable_att=23, iqv_no=1, case_flag=0x1, name_str=''):

        self.txrx.WIFI_TX_PWR_EVM(cable_lose=cable_att, channel=self.channel_comm, data_rate=self.rate_comm, iqv_no=iqv_no, iqv_num=10, name_str=name_str)


    def rx_perform_case(self, cable_att=23, iqv_no=1, case_flag=0x1, name_str=''):
        '''
        :case_flag: bit[0]-RX_Sens, bit[1]-RX_Range, bit[2]-RX_table, bit[3]-RX_MaxLevel
        '''

        if case_flag & (1<<0):
##            self.wifi.save_init_print('init_print_%s'%name_str, name_str)
            self.txrx.WIFI_RX_sens(cable_lose=cable_att, chan_in=[14], data_rate=self.rate_all, iqv_no=iqv_no,name_str=name_str)
##            self.rxgain.sweep_rx_table(cable_att=cable_att, tx_chan=14, iqv_no=iqv_no, name_str=name_str, device='TESTER')
##            self.txrx.WIFI_TX_PWR_EVM(cable_lose=cable_att, channel=[1,6,11,14], data_rate=['mcs7'], iqv_no=iqv_no, iqv_num=10, name_str=name_str)

        if case_flag & (1<<1):
            self.txrx.WIFI_RX_range(cable_lose=cable_att, chan_in=[1,14], data_rate=['11m', 'mcs7'], rx_range=[], iqv_no=iqv_no,name_str=name_str)

        if case_flag & (1<<2):
            self.wifi.save_init_print('init_print_%s'%name_str, name_str)
            self.rxgain.sweep_rx_table(cable_att=cable_att, tx_chan=14, iqv_no=iqv_no, name_str=name_str, device='TESTER')
            self.rxgain.sweep_rxgain_force(cable_att=cable_att, chan_step=5, rfrx_en=1, iqv_no=iqv_no, device='TESTER',name_str=name_str)

        if case_flag & (1<<3):
            self.txrx.WIFI_RX_maxlevel(cable_lose=cable_att, chan_in=[14],data_rate=self.rate_comm,iqv_no=iqv_no,name_str=name_str)

        if case_flag & (1<<4):
##            self.txrx.WIFI_HT40_RX_range(cable_lose=cable_att, chan_in=range(3,4), data_rate=['mcs7','54m'], rx_range_max=0, iqv_no=iqv_no,name_str=name_str)
            self.txrx.WIFI_HT40_RX_range(cable_lose=cable_att, chan_in=range(5,6), data_rate=self.rate_ht40, rx_range_max=0, iqv_no=iqv_no,name_str=name_str)


    def tx_matching_case(self,case_flag=0, cable_att=2,iqv_no=2,name_str=''):

        '''
        case_flag:
            1:matching_test at a Fix_gain
            2:P1dB vs EVM
            4:sweep date rate
        '''

        if case_flag & (1<<0):
            # matching_test at a Fix_gain
##            self.txgain.fixed_gain_matching(cable_lose=cable_att, channel=[1,7,13], data_rate=['mcs7'], target_pwr_dis_m =[1], iqv_num=20, iqv_no=iqv_no, board_no=name_str,recal=0)
            self.txgain.fixed_gain_matching(cable_lose=cable_att, channel=[1,2,3,4,5,6,7,8,9,10,11,12,13,14], data_rate=['mcs7'], target_pwr_dis_m =[1], iqv_num=20, iqv_no=iqv_no, board_no=name_str,recal=0)

##            self.txgain.fixed_gain_matching(cable_lose=cable_att, channel=[1,7,13], data_rate=['mcs7'], target_pwr_dis_m =[1], iqv_num=20, iqv_no=iqv_no, board_no=name_str)
        if case_flag & (1<<1):
            # P1dB vs EVM
            self.pa_test.PA_Test_case(element=3,cable_lose=cable_att,iqv_no=iqv_no,Board_Num=name_str)

        if case_flag & (1<<2):
            #sweep date rate
            self.txgain.fix_gain_rate_sweep(cable_lose=cable_att, channel=[1,2,3,4,5,6,7,8,9,10,11,12,13], data_rate=rate_all, iqv_num=20, iqv_no=iqv_no, board_no=name_str)


    def tx_gain_case(self,case_flag=0,cable_att=2,iqv_no=2):

        '''
        case_flag:
        1: bb filter
        2: rc filter
        4: pa adn bb gain
        8: digital gain
        '''

        if case_flag & (1<<0):
            # BB filter: GAIN vs EVM
            self.txgain.tx_gain_evm( cable_lose=cable_att, channel=[2430,2432], iqv_no=iqv_no,iqv_num=10, rc_en=0,name_str="bb_filter")

        if case_flag & (1<<1):
            # RC filter: GAIN vs EVM
            self.txgain.tx_gain_evm( cable_lose=cable_att, channel=[2430,2432], iqv_no=iqv_no,iqv_num=10, rc_en=1,name_str="rc_filter")

        if case_flag & (1<<2):
            # fast_gain_test: PA_gain and BB_gain
            self.txgain.tx_gain_fast_test(cable_lose=cable_att, channel=[1], iqv_no=iqv_no,iqv_num=10,name_str='')

        if case_flag & (1<<3):
            #digital_gain
            self.txgain.tx_dig_gain_sweep(cable_lose=cable_att, channel=[1], iqv_no=iqv_no,iqv_num=10)

        if case_flag & (1<<4):
            # sweep_gain_table
            self.txgain.tx_gain_table_sweep(cable_lose=cable_att, channel=[1], iqv_no=iqv_no,iqv_num=10)

        if case_flag & (1<<5):
            self.txgain.tx_gain_target_pwr_sweep(cable_lose=cable_att, channel=[1], iqv_no=iqv_no,iqv_num=50)


    def tx_i2c_case(self,case_flag=0,cable_att=2,iqv_no=2):
        '''
        case_flag:
            1. I2C_vs_EVM
            2. I2C_vs_Mask
            8. combine_I2C_vs_EVM
            16.combine_I2C_vs_mask
        '''

        if case_flag & (1<<0):
            # sweep rftx i2c_vs_EVM
            self.i2c_sweep.i2c_EVM_MASK(cable_lose=cable_att, channel=[1,3,6,9,12,14], sheetnamelist=['rftx'], curr_en=0, mask_en=0, num=20, iqv_no=iqv_no)
        if case_flag & (1<<1):
            # sweep rftx i2c_vs_MASK
            self.i2c_sweep.i2c_EVM_MASK(cable_lose=cable_att, channel=[1], sheetnamelist=['rftx'], curr_en=0, mask_en=1, num=20, iqv_no=iqv_no)
        if case_flag & (1<<2):
            # sweep rftx i2c_vs_EVM
            self.i2c_sweep.i2c_EVM_MASK(cable_lose=cable_att, channel=[1], sheetnamelist=['bias','xtal','rfpll','bbtop'], curr_en=0, mask_en=0, num=20, iqv_no=iqv_no)
        if case_flag & (1<<3):
            self.i2c_sweep.combi2c_EVM_MASK(cable_lose=cable_att, channel=[1], sheetnamelist=['rftx'], curr_en=0, mask_en=0, target_pwr_dis=0, num=20, iqv_no=iqv_no)
        if case_flag & (1<<4):
            self.i2c_sweep.combi2c_EVM_MASK(cable_lose=cable_att, channel=[1], sheetnamelist=['rftx'], curr_en=0, mask_en=1, target_pwr_dis=0, num=20, iqv_no=iqv_no)



    def tx_pa_case(self,case_flag=0, cable_att=2,iqv_no=2,name_str=''):
        if case_flag & (1<<0):
            # sweep rftx i2c_vs_P1DB
            self.pa_test.PA_Test_case(element=2,cable_lose=cable_att,iqv_no=iqv_no,Board_Num=name_str)
        if case_flag & (1<<1):
            # sweep rftx i2c_vs_PA
            self.pa_test.PA_Test_case(element=1,cable_lose=cable_att,iqv_no=iqv_no,Board_Num=name_str)
        if case_flag & (1<<2):
            # TX_IM3_Test_Matching
            self.pa_test.PA_Test_case(element=4,cable_lose=cable_att,iqv_no=iqv_no,Board_Num=name_str)


    def tx_pwrdet_case(self,case_flag=0, cable_att=2,iqv_no=2,name_str=''):
        '''
        case_flag 1:
            packet_power_detector
        case_flag 2:
            tone_power_detector
        case_flag 4:
            tone_pwdet_spa
        case_flag 8:
            pwrdet linear,pwdet all rate power,pwdet tracking power (rate & channel)
        '''
        if case_flag & (1<<0):
            self.pwrdet.packet_power_detector(cable_lose=cable_att, channel=[1], data_rate=['1m'], num=10, iqv_no=iqv_no)
        if case_flag & (1<<1):
            self.pwrdet.tone_power_detector(backoff=-80,cable_lose=cable_att,channel=[1],name_str='')
        if case_flag & (1<<2):
            self.pwrdet.tone_pwdet_spa(cable_lose=cable_att, instr='')
        if case_flag & (1<<3):
            self.pwrdet.pocket_power_linear(cable_lose=cable_att, iqv_no=iqv_no, iqv_num=1, name_str=name_str)
            self.pwrdet.pocket_power_test(cable_lose=cable_att, iqv_no=iqv_no, iqv_num=1, name_str=name_str)
            self.pwrdet.pwdet_track_test(name_str=name_str)


    def phy_release_case(self, phy_version='', iqv_no=1, cable_att=2):
        name_str = phy_version
        file_folder = '%s_phy_release_%s'%(self.chipv, name_str)
        rfglobal.file_folder = file_folder

        if self.chipv != 'ESP8266':
            self.wifi.save_init_print('init_print_%s'%name_str, name_str)

        # rx gain
        self.rxgain.sweep_rx_table(cable_att=cable_att, tx_chan=14, iqv_no=iqv_no, name_str=name_str, device='TESTER')

        # rx performance: rx sensitivity, rx range
        self.txrx.WIFI_RX_sens(cable_lose=cable_att, chan_in=[14], data_rate=self.rate_comm, iqv_no=iqv_no, name_str=name_str)
        self.txrx.WIFI_RX_range(cable_lose=cable_att, chan_in=[14], data_rate=['11m', 'mcs7'], rx_range=['[-92, 0]', '[-73,0]'], iqv_no=iqv_no,name_str=name_str)

        # tx performance
        self.txrx.WIFI_TX_PWR_EVM(cable_lose=cable_att, channel=self.channel_all, data_rate=self.rate_comm, iqv_no=iqv_no, iqv_num=20, name_str=name_str)

        case1 = WIFI_Feature_Case(self.comport, self.chipv)

        if self.chipv=='ESP8266':
            case1.esp8266_freq_offset_test(cable_lose=cable_att, iqv_no=iqv_no, name_str=name_str)

