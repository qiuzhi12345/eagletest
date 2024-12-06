#!/usr/bin/env python
# encoding: utf-8
import re
import scipy.optimize as opt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import collections
import time
import os
import logging
from enum import Enum

from baselib.loglib.log_lib import *
from hal.Init import HALS
from rtclib.rtc import ADC_LIB
from rtclib.rtc import RESET_CAUSE
from hal.common import CHIP_ID
from baselib.instrument.awg import awg
from baselib.instrument.eps import eps
from baselib.instrument.dm import dm
from baselib.loglib.log_csv import csvreport
from baselib.tc_platform.common import *
from baselib.tc_platform.tc_platform import *
from baselib.test_channel.com import COM
from collections import OrderedDict

from functools import wraps

class SpiPtest(object):
    '''
    :brief: 
        - test SPI LDO function
        - function tc031_sleep_time_test is not related to SPI but to test deep_sleep vbg wakeup speed
    :param:
    '''
    def __init__(self, channel, chipv = 'CHIP722'):
        self.channel = channel
        self.chipv = chipv
        self.chip = HALS(channel, chipv)

    def vdd_sdio_set(self, drefh = 0, drefm = 0, drefl = 1, 
                    tie_h = 0, xpd_reg = 1, 
                    encurlim = 1, modecurlim = 0, dcurlim = 0, 
                    initi = 1, en_initi = 1, dcap = 3, dthdrv = 3):
        '''
        :brief:
            - need to use special bin chip722_spi.bin under path Documents/ZBL/binYard
        :param:
            - xpd_reg: used to turn on/off SPI fucntion
            - tie_h:   used to change between 3.3V & 1.8V modes
            - dcap:    used to change ripple frequency
        '''
        timeout = 1
        self.channel.req_com('vdd_sdio_set %d %d %d %d %d %d %d %d %d %d %d %d'%
            (drefh, drefm, drefl,tie_h, xpd_reg, encurlim, modecurlim, dcurlim, 
            initi, en_initi, dcap, dthdrv), timeout)

    def sdio_mem_read(self):
        '''
        '''
        xpd_sdio_reg = self.chip.MEM.rdm(1610645628, 31, 31)
        drefh        = self.chip.MEM.rdm(1610645628, 30, 29)
        drefm        = self.chip.MEM.rdm(1610645628, 28, 27)
        drefl        = self.chip.MEM.rdm(1610645628, 26, 25)
        reg1p8_ready = self.chip.MEM.rdm(1610645628, 24, 24)
        tieh         = self.chip.MEM.rdm(1610645628, 23, 23)
        force        = self.chip.MEM.rdm(1610645628, 22, 22)
        reg_pd_en    = self.chip.MEM.rdm(1610645628, 21, 21)
        encurlim     = self.chip.MEM.rdm(1610645628, 20, 20)
        modecurlim   = self.chip.MEM.rdm(1610645628, 19, 19)
        dcurlim      = self.chip.MEM.rdm(1610645628, 18, 16)
        en_initi     = self.chip.MEM.rdm(1610645628, 15, 15)
        initi        = self.chip.MEM.rdm(1610645628, 14, 13)
        dcap         = self.chip.MEM.rdm(1610645628, 12, 11)
        dthdrv       = self.chip.MEM.rdm(1610645628, 10, 9)
        memtable = collections.OrderedDict()
        memtable.update({'xpd': xpd_sdio_reg })
        memtable.update({'drefh': drefh })
        memtable.update({'drefm': drefm })
        memtable.update({'drefl': drefl })
        memtable.update({'1p8_rdy': reg1p8_ready })
        memtable.update({'tieh': tieh })
        memtable.update({'force': force })
        memtable.update({'pd_en': reg_pd_en })
        memtable.update({'encurlim': encurlim })
        memtable.update({'modecurlim': modecurlim })
        memtable.update({'dcurlim': dcurlim })
        memtable.update({'en_initi': en_initi })
        memtable.update({'initi': initi })
        memtable.update({'dacp': dcap })
        memtable.update({'dthdrv': dthdrv })
        mt = pd.DataFrame(data = memtable, index = ['Value'])
        mc = mt.T
        return mc

    def sdio_set_by_mem(self,xpd_reg=1, tie_h=1, drefh=0,drefm=0, drefl=1,
                        dcap=3, dthdrv=3, force=1):
        '''
        :brief: direct write memory address to config spi mode
        :param: 
        '''
        self.chip.MEM.wrm(1610645628, 31, 31, xpd_reg)
        self.chip.MEM.wrm(1610645628, 30, 29, drefh)
        self.chip.MEM.wrm(1610645628, 28, 27, drefm)
        self.chip.MEM.wrm(1610645628, 26, 25, drefl)

        self.chip.MEM.wrm(1610645628, 23, 23, tie_h)
        self.chip.MEM.wrm(1610645628, 22, 22, force)
        self.chip.MEM.wrm(1610645628, 12, 11, dcap)
        self.chip.MEM.wrm(1610645628, 10, 9, dthdrv)

    def sdio_gpio_out(self,tie_h=0,gpio_num=31,otpt_val=1):
        '''
        :brief:
            SET GPIO OUPUT VALUE in SPI/SDIO domain
        :param:
            - gpio_num: 26 SPICS1; 27 SPIHD; 28 SPIWP; 29 SPICS0; 30 SPICLK; 31 SPIQ; 32 SPID
        '''
        self.sdio_set_by_mem(tie_h = tie_h)
        self.chip.gpio.dig_gpio_hang_up(gpio_num)
        self.chip.gpio.dig_gpio_out(gpio_num,otpt_val)
        logwarn('SPI GPIO #%d OUPUT sets to %d'%(gpio_num,otpt_val))

    def sdio_inpt_vth_sweep(self,tie_h=0,gpio_num=31,reverse=False):
        '''
        :brief:
            scan to check input threshold of SPI domain gpio
        :param:
            - gpio_num: 26 SPICS1; 27 SPIHD; 28 SPIWP; 29 SPICS0; 30 SPICLK; 31 SPIQ; 32 SPID
            - tie_h:    set to 0 for 1.8V mode scan
        '''
        myawg= awg()
        self.sdio_set_by_mem(tie_h = tie_h)
        self.chip.gpio.dig_gpio_hang_up(gpio_num)
        spi_dict = OrderedDict()
        spi_dict['inpt']=[]
        spi_dict['read']=[]

        inpt_range = [1.5,2.5]
        e_val = inpt_range[tie_h]
        s_val = e_val-1.5
        step_size = e_val/0.01+1
        if reverse: s_val,e_val = e_val,s_val
        for i in np.linspace(s_val,e_val,step_size):
            myawg.appl('DC',0,0,i)
            spi_dict['inpt'].append(i)
            read=self.chip.gpio.dig_gpio_in(gpio_num)
            spi_dict['read'].append(read)

        spi_dict = pd.DataFrame(spi_dict)
        spi_vth  = spi_dict[spi_dict['read']=='1']['inpt'].min()
        logwarn('SPI VTH = %.3f'%spi_vth)
        return spi_dict

    def blanking_time_test(self, sleep_time_us=1000, wait_cycle=16, delay_cycle=16, gpioNum=6,slp_mode =1
                            ,ulp_mode=1, sig_slt =0,buf_en = False):
        '''
        :brief:
            - to be used for observing monitor mode reference voltage change 
        :param:
            - sig_select: 0: vdd_rtc; 1: vref_sar1; 2: vref_sar2
            - wait_cycle: used to setup ulp delay: 16 cycle = 180us
            - delay_cycle: used to config GPIO6(indicates ULP status) Pulse width
        '''
        #define RTC gpio parameters
        rtc_gpio_no = gpioNum
        rtc_gpio_out_w1ts = self.chip.HWREG.RTC_IO.RTC_GPIO_OUT_W1TS._RTC_GPIO_OUT_W1TS__addr
        rtc_gpio_out_data_w1ts_lsb = self.chip.HWREG.RTC_IO.RTC_GPIO_OUT_W1TS._RTC_GPIO_OUT_W1TS__rtc_gpio_out_data_w1ts_lsb + rtc_gpio_no
        rtc_gpio_out_data_w1ts_msb = self.chip.HWREG.RTC_IO.RTC_GPIO_OUT_W1TS._RTC_GPIO_OUT_W1TS__rtc_gpio_out_data_w1ts_lsb + rtc_gpio_no
        rtc_gpio_out_w1tc = self.chip.HWREG.RTC_IO.RTC_GPIO_OUT_W1TC._RTC_GPIO_OUT_W1TC__addr
        rtc_gpio_out_data_w1tc_lsb = self.chip.HWREG.RTC_IO.RTC_GPIO_OUT_W1TC._RTC_GPIO_OUT_W1TC__rtc_gpio_out_data_w1tc_lsb + rtc_gpio_no
        rtc_gpio_out_data_w1tc_msb = self.chip.HWREG.RTC_IO.RTC_GPIO_OUT_W1TC._RTC_GPIO_OUT_W1TC__rtc_gpio_out_data_w1tc_lsb + rtc_gpio_no

        if self.chipv == "ESP32":
            rtc_timer2_addr = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__addr
            touch_start_wait_lsb = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__reg_sar_touch_start_wait_lsb
            touch_start_wait_msb = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__reg_sar_touch_start_wait_msb
        else:
            rtc_timer2_addr = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__addr
            touch_start_wait_lsb = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__reg_ulpcp_touch_start_wait_lsb
            touch_start_wait_msb = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__reg_ulpcp_touch_start_wait_msb

        period     = int(self.chip.rtc_clk.get_clk_calibration(0))
        cycle_str  = self.chip.rtc_clk.conv_us_to_slowclk(sleep_time_us, period)
        cycle_list = cycle_str.split(',')
        low_slp    = int(cycle_list[0])
        high_slp   = int(cycle_list[1])
        loginfo("low_slp: %d, high_slp: %d\n"%(low_slp, high_slp))
        #config voltage buffers
        if buf_en is True:
            self.chip.HWI2C.ulp.ir_force_xpd_ref_out_buf = 1
            self.chip.HWI2C.ulp.ir_force_xpd_iph         = 1
            self.chip.HWI2C.ulp.ir_force_xpd_vgate_buf   = 1
        #pull internal signal to external pad GPIO11
        self.chip.rtc_debug.pull_internal_voltage(0)
        if   sig_slt == 0: self.chip.rtc_debug.set_test_mux(1,0) #vdd_rtc
        elif sig_slt == 1: self.chip.rtc_debug.set_test_mux(1,1) #vref_sar1
        elif sig_slt == 2: self.chip.rtc_debug.set_test_mux(0,0) #vref_sar2
        #pull bias_sleep signal to external pad GPIO4
        self.chip.rtc_debug.TOUCH_PAD4(0,24,4)
        #self.chip.rtc_debug.PDAC2(0,24,4)
        time.sleep(1)
        self.chip.gpio.rtc_gpio_out(gpioNum, 1)
        self.chip.MEM.wrm(rtc_timer2_addr, touch_start_wait_msb, touch_start_wait_lsb, wait_cycle) #default_value 16 = 180us
        #ulp setup
        self.chip.ulp.init()
        self.chip.ulp.str(rtc_gpio_out_w1ts, rtc_gpio_out_data_w1ts_msb, rtc_gpio_out_data_w1ts_lsb, 1)#rtc_gpio_out(rtc_gpio_no, 1)
        #ulp operating ADC
        self.chip.ulp.delay(delay_cycle) # decides gpio_out=high time width
        self.chip.ulp.str(rtc_gpio_out_w1tc, rtc_gpio_out_data_w1tc_msb, rtc_gpio_out_data_w1tc_lsb, 1)#rtc_gpio_out(rtc_gpio_no, 0)
        self.chip.ulp.set_ulp_slp_time(low_slp)
        self.chip.ulp.end()
        self.chip.ulp.start(ulp_mode)
        self.chip.rtc_sleep.special_sleep(slp_mode, 0, 0)

    def tie_high_resistance(self,supply_drop,check_num,vdd=3.3,sup_ilim=1,dthdrv=3):
        ''' test SPI tie high mode effective resistance
        :param:
            - supply_drop: lowset SPI load voltage you want to test
            - supply_step:   voltage step size to check
        :instrument:
            - GPIB
            - eps
            - dm
        '''
        def check_current(vdd_set):
            myeps.pwr(vdd_set,sup_ilim)
            i_spi = float(mydm.get_result('IDC'))*1000
            r_spi = (3.3-vdd_set)/i_spi*1000
            return i_spi,r_spi

        myeps = eps()
        mydm  = dm()
        spi_dict=OrderedDict()
        supply=[]
        current=[]
        resistance=[]
        self.chip.HWREG.RTC_CNTL.RTC_SDIO_CONF.reg_sdio_dthdrv = dthdrv
        for sup in np.linspace(vdd,(vdd-supply_drop),check_num):
        # for sup in np.linspace(vdd,(supply_drop+supply_step),supply_step):
            supply.append(sup)
            i,r=check_current(float(sup))
            current.append(i)
            resistance.append(r)
        spi_dict['Supply(V)']=supply
        spi_dict['Current(mA)']=current
        spi_dict['res(Ohm)']=resistance
        spi_dict = pd.DataFrame(spi_dict)
        return spi_dict


