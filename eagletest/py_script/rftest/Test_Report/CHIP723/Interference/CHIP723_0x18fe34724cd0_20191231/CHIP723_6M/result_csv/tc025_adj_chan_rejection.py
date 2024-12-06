#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Test
#
# Created:     01/04/2019
# Copyright:   (c) Test 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import baselib.test_channel.channel as chn
from loglib.log_lib import *
from wifilib import *
from rf_debug import *
from baselib.plot import *
from baselib.instrument import *
import numpy as np
import scipy
from math import *
import testcase.tc006_pbus_test as pbus_test
import testcase.tc005_rf_test as rf_test
import testcase.tc002_agc_test as agc_test
import testcase.tc012_adcTest  as adcTest
#import testcase.tc017_test_pwctrl  as test_pwctrl
from shutil import copy
import time
import csv
import pylab
import matplotlib.pyplot as plt
from baselib.test_channel import *
from rf_debug.utility import (mfunc, iofunc)
import testcase.tc016_test_rx as test_rx
import xlrd
import btlib.bt as bt
from baselib.instrument.iqv import *

#import testcase.tc017_test_pwctrl  as test_pwctrl
import os
import glob
import pandas
import re
#from rftest.rflib import rfglobal

def iq_open(name=''):
    if name == 'iqxel':
        iqxel_serv.init()
        iqxel_serv.open_instru()
        loginfo('iqxel is opened')
    elif name == 'wt200':
        wt200_serv.init()
        result=wt200_serv.open_instru()
        print result
        res1 = result.split(',')
        res_ID_1 = int(res1[0],10)
        return res_ID_1

def iq_close(name=''):
    if name == 'iqxel':
        iqxel_serv.close()
        iqxel_serv.term()
    elif name == 'wt200':
        wt200_serv.close()
        wt200_serv.term()

def iq_sigout(name='',rf_freqMhz=2412,pwr=-10,ex_att=1,data_rate='11m',frmcnt=1,iqv_no=1):
    if name == 'iqxel':
        iqxel_serv.setvsg(rf_freqMhz,pwr+ex_att,iqv_no)
        iqxel_serv.setrate(data_rate)
        iqxel_serv.txenable(1)
        iqxel_serv.txfrmcnt(frmcnt)
        loginfo('TX iqxel is ready!');
    elif name == 'wt200':
        wt200_serv.setvsg(rf_freqMhz,pwr+ex_att,iqv_no)
        wt200_serv.setrate(data_rate)
        wt200_serv.txenable(1)
        wt200_serv.txfrmcnt(frmcnt)
        loginfo('TX wt200 is ready!');

def iq_trig_wave(name='',frmcnt=1):
    if name == 'iqxel':
        iqxel_serv.txenable(1)
	iqxel_serv.txfrmcnt(frmcnt)
    elif name == 'wt200':
	wt200_serv.txenable(1)
	wt200_serv.txfrmcnt(frmcnt)

def iq_vsg_stop(name=''):
    if name == 'iqxel':
        iqxel_serv.txenable(0)
    elif name == 'wt200':
        wt200_serv.txenable(0)

def get_tx_chan_freq(tx_chan):
    if tx_chan<15:
       tx_freq=wifi.chan2freq(tx_chan);
    else:
       tx_freq=tx_chan;

    print 'tx chan: %d; tx_freq: %d;'%(tx_chan,tx_freq);
    return tx_freq;


def set_rx_chan(rx_chan, sub_chan_cfg, set_chan,c_set_chan_en, mode='chip'):
    if rx_chan<15:
       rx_freq=wifi.chan2freq(rx_chan);
    else:
       rx_freq=rx_chan;

    print 'rx_chan: %d; sub_chan: %d; rx_freq: %d; set_chan: %d; c_set_chan: %d'%(rx_chan,sub_chan_cfg,rx_freq,set_chan,c_set_chan_en);
    chan_id = 'com';
    if set_chan==1:
       if rx_chan>14:
          rfpll.set_freq(rx_freq,chan_id);
          pbus_test.pbus_workmode(chan_id);
       else:
          if mode=='chip':
             if c_set_chan_en==1:
                wifi.rfchsel(rx_chan,chan_id,sub_chan_cfg);
             else:
                rfpll.set_freq(rx_freq,chan_id);
                pbus_test.pbus_workmode(chan_id);
          else:
             wifi.rfchsel(rx_chan,chan_id,sub_chan_cfg);

    return;


def adj_chn_rej_test(logpath='rx',iq_sig='iqxel',iq_adj='wt200',sig_rate='',sig_pwr=-55,adj_rate='',adj_pwr_min=-99,adj_pwr_max=-10,
                        tx_chan=8,sub_chan_cfg=1,rx_chan=8,tx_chan_adj=3,packnum=100, iqv_sig_no=1,iqv_adj_no=1,cable_lose=19,cable_lose_adj=21,chan_id='com',
                        set_chan=1,c_set_chan_en=1,rxgain_force_en=0, rxgain_force=20,board_id='',break_en=0,break_thr=90,suc_sum_thr=89):

    print sig_rate

    tx_freq = get_tx_chan_freq(tx_chan);
    tx_freq_adj = get_tx_chan_freq(tx_chan_adj);
    set_rx_chan(rx_chan, sub_chan_cfg, set_chan,c_set_chan_en);
    mem.wr(0x6001c02c,((mem.rd(0x6001c02c)&0x007fffff) | (rxgain_force<<24) | (rxgain_force_en<<23)));

##    res_adj = iq_open('wt200')
##    res_sig = iq_open('iqxel')

    print 'signal pwr: %d' %sig_pwr;
    print 'adj_pwr_min: %d' %adj_pwr_min;
    print 'adj_pwr_max: %d' %adj_pwr_max;

    break_flag=0;
    reg_cfg_pass = 0;
    suc_cnt = 0;
    rx_result = [];

    for adj_pwr in range(adj_pwr_min, adj_pwr_max+1):
        print 'adj_pwr, %d' %adj_pwr;

    #    iq_sigout(iq_adj,tx_freq_adj,adj_pwr,cable_lose_adj,adj_rate,0,iqv_adj_no);
        iq_sigout(iq_sig,tx_freq,sig_pwr,cable_lose,sig_rate,1,iqv_sig_no);
        wifi.rxstart(sig_rate,chan_id,0,0);
        iq_trig_wave(iq_sig,packnum);
        time.sleep(0.1);
        result_data=wifi.cmdstop(chan_id);
    #    iq_vsg_stop(iq_adj);
        iq_vsg_stop(iq_sig);

        result=str.split(result_data);
        DesirePackNum=int(wifi.GetDesirePackNum(result));
        if DesirePackNum >= break_thr:
            suc_cnt = suc_cnt + 1;
        rx_result.append([adj_pwr,DesirePackNum]);

        if (break_en==1) and (adj_pwr_max-adj_pwr+suc_cnt < suc_sum_thr):
            break_flag = 1;
            reg_cfg_pass = 0;
            break;
        else:
            adj_pwr = adj_pwr + 1;

    if suc_cnt >= suc_sum_thr:
        reg_cfg_pass = 1;

    if logpath != 'NULL':
        if False == createdir(logpath):
            print "Fail to creat direction";
        else:
            logname = logpath + '/acrscan_cfg%s_sig%d_rate%s_adjmin%d_adjmax%d' %(board_id,sig_pwr,sig_rate,adj_pwr_min,adj_pwr_max);
            createlog(logname,'csv');
            for data in rx_result:
                writelog('%s,%s'%(data[0],data[1]));
            closelog();
##    iq_close('wt200')
##    iq_close('iqxel')
    mem.wr(0x6001c02c,((mem.rd(0x6001c02c)&0xff7fffff) | (0<<23)));

    return [rx_result,reg_cfg_pass];

def reg_opt_cfg_init():
    cfg_array = [];
    for pwr_lt_thr in range(412,432,2):
        for pwr_low in range(432,452,3):
            for max_gain1 in range(38,50+1,2):
                for max_gain2 in range(28,43+1,2):
                    for max_gain3 in range(22,23,1):
                        for max_gain4 in range(0,1,1):
                            cfg_array.append([pwr_lt_thr, pwr_low, ((max_gain4<<24)+(max_gain3<<16)+(max_gain2<<8)+max_gain1)]);
    return cfg_array;


##def reg_opt_cfg_init(file_dir='D:/chip/chip_7.2/py_script/log/rx/adj_test/reg_cfg_first',file0='reg_opt__20191223124136_20191223124236_2019_12_23_15_00_58_Copy.csv'):
##    cfg_array = []
##    file_name = file_dir + '/' + file0
##    print file_name
##    input_file = file(file_name,'rb')
##    reader = csv.reader(input_file)
##    with open(file_name) as f:
##        f_csv = csv.reader(f)
##        header = next(f_csv)
##        for line in f_csv:
##            cfg_array.append(line[0])
##    return cfg_array;

def reg_opt_cfg_rxscan(cfg_array,logpath_dst='adj_opt/reg_opt_cfg_rxscan_adj_chip723_1',sig_rate='6m',sig_pwr=-55,adj_rate='6m',adj_pwr_min=-99,adj_pwr_max=-15,break_enable=0,rxnum_least=90,sum_thr=74,loop=0):
    cfg_array_new = []
    for reg_cfg in cfg_array:
        print reg_cfg
##        reg_cfg_0=int(reg_cfg[0],16);
##        reg_cfg_1=int(reg_cfg[1],16);
##        reg_cfg_2=int(reg_cfg[2],16);

        mem.wrm(0x6001c024,17,9,reg_cfg[0]) #coarse pwr low thr 430->
        mem.wrm(0x6001c0a0,8,0,reg_cfg[0]) #coarse pwr too low thr 434->
        mem.wrm(0x6001c028,17,9,reg_cfg[1]) #coarse target pwr 450->
        mem.wr(0x6001c114, reg_cfg[2]);
        reg_cfg_2=hex(reg_cfg[2]);

        #for test
        reg_cfg_pass=1;

        logpath_detail = logpath_dst + '/rxdetail'
##        [perform,reg_cfg_pass]=adj_chn_rej_test(logpath=logpath_detail,iq_sig='iqxel',iq_adj='wt200',sig_rate=sig_rate,sig_pwr=sig_pwr,adj_rate=adj_rate,
##                                                adj_pwr_min=adj_pwr_min,adj_pwr_max=adj_pwr_max,tx_chan=6,sub_chan_cfg=1,rx_chan=6,tx_chan_adj=1,packnum=100,
##                                                iqv_sig_no=0,iqv_adj_no=0,cable_lose=16.5,cable_lose_adj=19.5,chan_id='com',set_chan=1,c_set_chan_en=1,
##                                                board_id=reg_cfg_2,break_en=break_enable,break_thr=rxnum_least,suc_sum_thr=sum_thr);
        if reg_cfg_pass==1:
            cfg_array_new.append([reg_cfg[0],reg_cfg[1],reg_cfg_2]);

    createdir(logpath_dst)
    logname = logpath_dst + '/acrscan_cfgpass_loop%d_sig%d_adjmin%d_adjmax%d' %(loop,sig_pwr,adj_pwr_min,adj_pwr_max)
    createlog(logname,'csv')
    for reg_cfg in cfg_array_new:
        writelog('%s,%s,%s' %(reg_cfg[0],reg_cfg[1],reg_cfg[2]));
    closelog();
    print cfg_array_new
    return cfg_array_new


#def reg_opt_wrap(per_thr=100, sum_thr=50, dyn_thr=0, rxsens_thr=-70):
def reg_opt_wrap():
    case_list = [
        ['sig_rate','sig_pwr','adj_rate','adj_pwr_min','adj_pwr_max','per_thr','sum_thr,dyn_thr'],
        ['6m',-55,'6m',-30,-24,100,6,0],
        ['6m',-85,'6m',-53,-49,0,4,0],
##        ['6m',-55,'6m',-30,-24,80,6,0],
##        ['6m',-85,'6m',-53,-49,80,4,0],
##        ['6m',-80,'6m',-52,-48,80,4,0],
##        ['6m',-75,'6m',-49,-47,95,2,0],
##        ['6m',-65,'6m',-32,-28,75,4,0],
##        ['6m',-60,'6m',-33,-27,85,6,0],
##        ['6m',-50,'6m',-25,-21,95,4,0],
        ['6m',-45,'6m',-35,-26,93,6,0]
##        ['6m',-40,'6m',-35,-24,98],
##        ['6m',-35,'6m',-29,-21,98]
    ];

    #res_adj = iq_open('wt200');
    res_sig = iq_open('iqxel');
    cfg_array_input = reg_opt_cfg_init();
    #cfg_array=['0x8112727','0x4152727']
    for i in range(1,len(case_list)):
        cfg_array_output=reg_opt_cfg_rxscan(cfg_array_input,logpath_dst='rx/adj_test/loop3',sig_rate=case_list[i][0],sig_pwr=case_list[i][1],adj_rate=case_list[i][2],adj_pwr_min=case_list[i][3],
                                            adj_pwr_max=case_list[i][4],break_enable=0,rxnum_least=case_list[i][5],sum_thr=case_list[i][6],loop=i);
        cfg_array_input = cfg_array_output;

    return cfg_array_output;

def dump_pack_evm_test(path='',outpath='',tx_pwr=-10,test_chan=6,tx_port=0,rx_port=1,cable_att=3,times=10):
    pack_list=[]
    pack_perform_table=[]
    pack_perform_vec=[]
    file = os.listdir(path)
    for file_name in file:
        if 'mod' in file_name:
            pack_list.append(file_name[:-4])
    tx_freq=wifi.chan2freq(test_chan)
    rx_freq=wifi.chan2freq(test_chan)
    mytester=tester.tester('iqv',tx_freq,-40,'1m',1,tx_port,'source',cable_att);
   # pack_list=pack_list[:1]
#    rx_rate=pack_list[0]
    print pack_list
    if outpath != 'NULL':
        if False == createdir(outpath):
            print "Fail to creat direction"
        else:
            logname = outpath + '/dump_pack_evm'
            createlog(logname,'csv')
    for rx_rate in pack_list:
        pack_perform_vec = ''
        pack_perform_vec = pack_perform_vec + rx_rate+','
        mytester.sigout(tx_freq,tx_pwr,cable_att,rx_rate,0,tx_port);
        for i in range(0,times):
            mytester.trig_wave(tx_port)
            iqxel_serv.init()
            iqxel_serv.open_instru()
            iqxel_serv.reset()
            iqxel_serv.setvsa(rx_freq,-99,0,rx_port,1)
            result = iqxel_serv.capture_free_run(500,1)
            iqxel_serv.set11nrxmethod()
            result = iqxel_serv.getmeasdata(iq_mode='11n_40',meas_type='evmAvgAll')
            print result
            pack_perform_vec = pack_perform_vec + str(result[1])+','
            mytester.txenable(0)
            iq_close('iqxel')
        writelog(pack_perform_vec)
    closelog()


