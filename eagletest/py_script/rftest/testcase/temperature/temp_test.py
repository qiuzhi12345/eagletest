#-------------------------------------------------------------------------------
# Name:        TXP VS Temperature
# Purpose:
#
# Author:      QZ
#
# Created:     5/5/2019
# Copyright:   (c) Test 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time
import re
import csv
import os, sys
import matplotlib.pyplot as plt
import pylab
import numpy as np
from baselib.loglib.log_lib import *
from baselib.test_channel.com import COM as com
from rftest.testcase.Init import RFTCS
from rftest.testcase.Init import *
from rftest.rflib.csv_report import csvreport
from rftest.testcase.performance.rf_test_case import RF_TEST_CASE
from testcase.volumeCase.MULTIBOARD.multiboard_ctl import MultiBoardControl
from baselib.instrument import eps,dm


def temp_test(com_list=[18],cable_loss=2,instru_no=2,temperature=20,voltage=3.3):
    temp_vol="%d_%d"%(temperature,voltage)
    for i in com_list:
        chip=RFTCS(com(i))
        chip.wifiapi.phyinit()
##        basictest=BasicTest(chip.comport,chip.chipv)
##        basictest.rfpll_sweep(freq_start=2400, freq_end=2500, freq_step=1,name_str=temp_vol)         #rfpll dcap,dac sweep
##        wifitxrx=WIFI_TXRX_TEST(chip.comport,chip.chipv)
##        wifitxrx.wifi_test(0x9,temp_vol)        #init_print,
##        wifitxrx.tx_gain_fast_test(cable_loss, channel=[1], iqv_no=iqv_no,iqv_num=10,name_str=temp_vol)
##        rx_gain_sweep=Sweep_RX_Gain(chip.comport,chip.chipv)
##        rx_gain_sweep.sweep_rxgain_force_freq(cable_att=cable_loss, tx_chan=2484, rfrx_en=1, iqv_no=iqv_no, name_str=temp_vol, device="TESTER", fix_pwr=0)
        rftestcase=RF_TEST_CASE(chip.comport,chip.chipv)
        rftestcase.temp_vol_case(temp=temperature, vol=voltage, iqv_no=instru_no, cable_att=cable_loss)
        chip.deinit()

    for j in com_list:
        chip=RFTCS(com(j))
        basictest=BasicTest(chip.comport,chip.chipv)
        basictest.i2c_table_read(instr=temp_vol)
        chip.deinit()

def temp_burn_in_test(com_list=[18]):
    for k in com_list:
        chip=RFTCS(com(k))
        chip.wifiapi.burn_in_test()
        time.sleep(120)
        chip.wifi.cmdstop()
        res=chip.wifi.cmdstop()
        if res=="cmd not exist!":
            chip.deinit()

def temp_multiboard(com_mcu=78,com_chip=79,_chipv="CHIP722",vol_list=[2.7,3.3,3.7],chip_list=range(14),instru_no=1,cable_loss=0):
    a=eps.eps("E3633A")
    for vol in vol_list:
        a.pwr(vol,2)
        MB=MultiBoardControl(com(com_chip),com(com_mcu),_chipv)
        fail_list=[]
        for chip_num in chip_list:
            print "now test chip is num %d"%chip_num
            MB.mcu_slt(chip_num)
            time.sleep(1)
            MB.mcu_gpio.dig_gpio_out(MB.IO_0,1)
            time.sleep(1)
            MB.mcu_gpio.dig_gpio_out(MB.chip_pu,1)
            time.sleep(1)
            chip=RFTCS(MB.comNum,_chipv)

            #RF test
##            rftestcase=RF_TEST_CASE(chip.comport,chip.chipv)
##            rftestcase.temp_vol_case(temp=temperature, vol=voltage, iqv_no=instru_no, cable_att=cable_loss)

            #burn in test
            chip.wifiapi.burn_in_test()
            time.sleep(120)
            res=chip.wifi.cmdstop()
            if res=="cmd not exist!":
                print "fail burn in test chip num is %d"%chip_num
                fail_list.append(chip_num)

            print fail_list
        MB.mcu_chl.deinit()
        MB.comNum.deinit()

def temp_dtest_vol(com_list=[18],freq=2412,num=20,temp_offset=30):
    for k in com_list:
        chip=RFTCS(com(k))
        title = 'chipID,freq,ir_cap_ext,temperature(c),dtest_vol(mV)\n'
        fname = chip.wifi.get_filename('dtest_vol', 'dtest_vol')
        csvreport2 = csvreport(fname, title)
        id=chip.wifiapi.esp_origin_mac()
        chip.rfpll.set_freq(freq)
        or_cap=chip.hals.HWI2C.rfpll.or_pll_cap
        chip.hals.HWI2C.rfpll.ir_cap_ext=or_cap
        chip.hals.HWI2C.rfpll.ir_enx_cap=1
        chip.hals.tsen.config()
        chip.hals.rtc_adc2.config()
        chip.hals.rtc_adc2.set(atten=1,pad = 1)
        chip.hals.HWI2C.rfpll.ent_vco_bias=1
        chip.hals.HWI2C.rfpll.dtest=1
        chip.hals.rtc_debug.pull_internal_voltage(1)
        while 1:
            _temp=0.4386*int(chip.hals.tsen.read(),16)-20.52
            vol_list=[]
            temp_list=[]
            loginfo(_temp)
            if int(_temp) in range(temp_offset-5,temp_offset+5):
                for i in range(num):
                    vol=1000*1.7*int(chip.hals.rtc_adc2.read())/4095
                    temp=0.4386*int(chip.hals.tsen.read(),16)-20.52
                    vol_list.append(vol)
                    temp_list.append(temp)

                vol_avg=np.average(np.array(vol_list,dtype=float))
                temp_avg=np.average(np.array(temp_list,dtype=float))
                csvreport2.write_data([id,freq,or_cap, temp_avg, vol_avg])
                loginfo([id,freq,or_cap, temp_avg, vol_avg])
                temp_offset=temp_offset + 5
##            else:
##                loginfo("temp not in temp_offset range")
##                break
            if temp_offset>100:
                break
        chip.deinit()






