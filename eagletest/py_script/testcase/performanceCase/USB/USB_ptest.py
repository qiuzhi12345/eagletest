#!/usr/bin/env python
# encoding: utf-8
# 如果觉得不错，可以推荐给你的朋友！http://tool.lu/pyc
from baselib.loglib.log_lib import *
from hal.Init import HALS
from hal.common import CHIP_ID
from baselib.instrument.awg import awg
from baselib.instrument.eps import eps
from baselib.tc_platform.common import *
from baselib.tc_platform.tc_platform import *
from baselib.test_channel.com import COM
import re
import scipy.optimize as opt
import matplotlib.pyplot as plt
import pandas as pd
import collections
import time
import os


class USB_TC_PERF(object):
    '''
    :brief:
        - test USB configuration,covers tests
        - Ouput Driver Impedance
        - Single ended input threshold search
        - Pull up and down resistance 
        - Differential input common mode and resolution 
    :param:
        Use below table to find corresponding bit location
        - All start w/ USB_WRAP_TEST_
        - ENABLE, USB_OE, TXDP, TXDM, RX_RCV, RX_DP, RX_DM --> bit 0 to bit 6 
        - All sart w/ USB_WRAP
        - PAD_PULL_OVERRIDE, PULLUP, PULLDOWN, PULLUP_VALUE, USB_PAD_ENABLE
        - Above line --> bit 12 to bit 18
    '''

    def __init__(self, channel, chipv='CHIP722'):
        self.channel = channel
        self.chipv = chipv
        self.chip = HALS(channel, chipv)

    def usb_otg_conf_rdm(self, lsb):
        return self.chip.MEM.rdm(reg_addr=1610846208, msb=lsb, lsb=lsb)

    def usb_otg_conf_rdm_multi(self, msb, lsb):
        return self.chip.MEM.rdm(reg_addr=1610846208, msb=msb, lsb=lsb)

    def usb_test_rdm(self, lsb):
        return self.chip.MEM.rdm(reg_addr=1610846212, msb=lsb, lsb=lsb)

    def usb_otg_conf_wrm(self, lsb, value):
        return self.chip.MEM.wrm(reg_addr=1610846208, msb=lsb, lsb=lsb, value=value)

    def usb_otg_conf_wrm_multi(self, msb, lsb, value):
        return self.chip.MEM.wrm(reg_addr=1610846208, msb=msb, lsb=lsb, value=value)

    def usb_test_wrm(self, lsb, value):
        return self.chip.MEM.wrm(reg_addr=1610846212, msb=lsb, lsb=lsb, value=value)

    def usb_test_wrm_multi(self, msb, lsb, value):
        return self.chip.MEM.wrm(reg_addr=1610846212, msb=msb, lsb=lsb, value=value)

    def test_swap_rxtx(self, tx=1):
        self.usb_test_wrm(lsb=1, value=tx)

    def test_enable_PADforUSB(self, enable=1):
        self.usb_otg_conf_wrm(18, enable)
        if enable == 1:
            print 'USB PHY ENABLED'
        elif enable == 0:
            print 'USB PHY DISABLED'

    def test_checkEnableOrNot(self):
        res = self.chip.HWI2C.bbpll.en_usb
        return res

    def test_rd_inpt_conf(self, enable=1, refh=0, refl=0):
        '''
        :brief:
            Changes USB to RX Mode and sets reference voltage level
        :param:
            - refh [1:0] 1.76V to 2V step 80mV
            - refl [1:0] 0.8V to 1.04V step 80mV
        '''
        self.usb_otg_conf_wrm(18, enable)
        self.test_swap_rxtx(tx=0)
        print 'USB RX mode'
        self.usb_otg_conf_wrm(11, enable)
        self.usb_otg_conf_wrm_multi(8, 7, refh)
        print 'VREFH sets to %d' % refh
        self.usb_otg_conf_wrm(11, enable)
        self.usb_otg_conf_wrm_multi(10, 9, refl)
        print 'VREFL sets to %d' % refl

    def test_rd_inpt(self, pinNum=0):
        '''
        :brief:
            Ouput USB RX results
        :param:
            pinNum: 0: D- GPIO19; 1: D+ GPIO20; 2: Diff=(D+ - D-)
        '''
        if pinNum == 0:
            res = self.usb_test_rdm(6)
            print 'D- Reads %d' % res
        elif pinNum == 1:
            res = self.usb_test_rdm(5)
            print 'D+ Reads %d' % res
        elif pinNum == 2:
            res = self.usb_test_rdm(4)
            print 'Diff Reads %d' % res
        return res

    def test_prep(self, dp=1, drv=0):
        '''
        :brief:
            - disable GPIO IE, RDE, RUE and choose its drive level
            - drv = 0 for low speed; drv = 3 for high speed
        :param:
            dp: 1: controls D+ pin; 0: controls D- pin
            drv: as above
        '''
        if dp == 1:
            gpio_num = 20
        elif dp == 0:
            gpio_num = 19
        self.chip.gpio.rtc_gpio_out(gpio_num, 0, drv)
        self.chip.gpio.rtc_gpio_hang_up(gpio_num)

    def test_otpt_conf(self, enable=1):
        '''
        :brief:
            Configs USB to TX Mode and outputs value
        '''
        self.usb_otg_conf_wrm(18, enable)
        self.usb_test_wrm(0, 1)
        self.test_swap_rxtx(tx=1)
        print 'USB TX mode'

    def test_otpt(self, pinNum=0, value=1, drv=0):
        '''
        :brief:
            Outputs value to USB pad
        :param:
            pinNum: 0: D- GPIO19; 1: D+ GPIO20
        '''
        self.test_prep(dp=pinNum, drv=drv)
        if pinNum == 0:
            res = self.usb_test_wrm(3, value)
            print 'Set D- Output %d' % value
        elif pinNum == 1:
            res = self.usb_test_wrm(2, value)
            print 'Set D+ Output %d' % value

    def test_otpt_crx(self, dpVal=1, drv=0):
        '''
        '''
        self.test_prep(dp=0, drv=drv)
        self.test_prep(dp=1, drv=drv)
        self.test_otpt_conf()
        if dpVal == 0:
            res = self.usb_test_wrm_multi(3, 2, 2)
            print 'Set D- 1, D+ 0'
        elif dpVal == 1:
            res = self.usb_test_wrm_multi(3, 2, 1)
            print 'Set D- 0, D+ 1'

    def test_otpt_eye(self,drv=0):
        '''
        eye diagram
        '''
        self.test_prep(dp=0, drv=drv)
        self.test_prep(dp=1, drv=drv)
        self.test_otpt_conf()
        while True:
            res = self.usb_test_wrm_multi(3, 2, 2)
            res = self.usb_test_wrm_multi(3, 2, 1)
            print 'Set D- 1, D+ 0'

    def test_pull(self, enable=1, dp=1, up=0, upres=0):
        '''
        :brief:
            test USB pull up & pull down function
        :param:
            dp: 1: controls D+ pin; 0: controls D- pin
            up: 0: pullDown; 1: pullUp
            upres: 0: 2.4K; 1: 1.2K
        '''
        if enable == 1:
            enOrnot = 'ENABLED'
        elif enable == 0:
            enOrnot = 'DISABLED'
        self.usb_otg_conf_wrm(18, enable)
        self.usb_otg_conf_wrm(12, enable)
        self.usb_otg_conf_wrm(17, upres)
        if dp == 1:
            if up == 1:
                self.usb_otg_conf_wrm(13, enable)
                self.usb_otg_conf_wrm(14, 0)
                print 'D+ PullUp %s' % enOrnot
            elif up == 0:
                self.usb_otg_conf_wrm(14, enable)
                self.usb_otg_conf_wrm(13, 0)
                print 'D+ PullDown %s' % enOrnot

        elif dp == 0:
            if up == 1:
                self.usb_otg_conf_wrm(15, enable)
                self.usb_otg_conf_wrm(16, 0)
                print 'D- PullUp %s' % enOrnot
            elif up == 0:
                self.usb_otg_conf_wrm(16, enable)
                self.usb_otg_conf_wrm(15, 0)
                print 'D- PullDown %s' % enOrnot

    def test_pull_2(self, enable=1, dp=1, up=0, upres=0):
        '''
        :brief:
            test USB pull up & pull down function
        :param:
            dp: 1: controls D+ pin; 0: controls D- pin
            up: 0: pullDown; 1: pullUp
            upres: 0: 2.4K; 1: 1.2K
        '''
        if enable == 1:
            enOrnot = 'ENABLED'
        elif enable == 0:
            enOrnot = 'DISABLED'
        self.usb_otg_conf_wrm(18, enable)
        self.usb_otg_conf_wrm(12, enable)
        self.usb_otg_conf_wrm(17, upres)
        if dp == 1:
            if up == 1:
                self.usb_otg_conf_wrm(13, enable)
                self.usb_otg_conf_wrm(14, 0)
                print 'D+ PullUp %s' % enOrnot
            elif up == 0:
                self.usb_otg_conf_wrm(13, 0)
                print 'D+ PullDown %s' % enOrnot

        elif dp == 0:
            if up == 1:
                self.usb_otg_conf_wrm(15, enable)
                self.usb_otg_conf_wrm(16, 0)
                print 'D- PullUp %s' % enOrnot
            elif up == 0:
                self.usb_otg_conf_wrm(15, 0)
                print 'D- PullDown %s' % enOrnot

    def test_drvImp(self, pinNum=0, value=1, drv=0, pinBias=1.5):
        a = awg()
        self.test_otpt_conf(enable=1)
        self.test_otpt(pinNum=pinNum, value=value, drv=drv)
        a.appl('DC', 0, 0, pinBias)

    def test_inptSwep(self, stepSize=10, pinNum=0, refh=0, refl=0, ins='aw', dely=0.5):
        """
        :brief:
            test USB single-ended input threshold
            Use wave-generator to sweep pad input voltage 
        :param:
            - ins: 
                - 'aw': wave generator
                - 'ps': power supply
        """
        if pinNum == 0:
            padName = 'D-'
        elif pinNum == 1:
            padName = 'D+'

        def eqp_otpt(eqp=ins, volt=(0, )):
            if ins == 'aw':
                eqp = awg()
                eqp.appl('DC', 0, 0, volt)
            elif ins == 'ps':
                eqp = eps()
                eqp.pwr(np.float(volt), 0.05)

        resfile_inc = collections.OrderedDict()
        resfile_dec = collections.OrderedDict()
        res_l = []
        inpt_l = []
        self.test_rd_inpt_conf(refh=refh, refl=refl)
        for i in np.arange(1500, 2201, stepSize):
            eqp_otpt(volt=i / 1000)
            time.sleep(dely)
            inpt_l.append(i / 1000)
            res = self.test_rd_inpt(pinNum=pinNum)
            res_l.append(res)

        resfile_inc.update({'Vin': inpt_l})
        resfile_inc.update({'%s_readVal_inc' % padName: res_l})
        res_l = []
        inpt_l = []
        for i in np.arange(1500, 2201, stepSize):
            inptVal = 2.7 - i / 1000
            eqp_otpt(volt=inptVal)
            time.sleep(dely)
            inpt_l.append(inptVal)
            res = self.test_rd_inpt(pinNum=pinNum)
            res_l.append(res)

        resfile_dec.update({'Vin': inpt_l})
        resfile_dec.update({'%s_readVal_dec' % padName: res_l})
        res_inc = pd.DataFrame(resfile_inc)
        res_dec = pd.DataFrame(resfile_dec)
        rh = res_inc['Vin'][res_inc['%s_readVal_inc' % padName] == 1][0:5]
        rl = res_dec['Vin'][res_dec['%s_readVal_dec' % padName] == 0][0:5]
        print 'rh below, sets to %d' % refh
        print rh
        print 'rl below, sets to %d' % refl
        print rl
        return (res_inc, res_dec)

    def __comMode_eqpPre(self):
        '''
        :brief:
            - reads GPIB address for Power supply and Wave generator
        '''
        a = awg()
        e = eps()
        return (a, e)

    def __comMode_eqpConfig(self, a, e, diff=0.1, ve=0):
        '''
        :brief:
            - configs a Power Supply and a Wave Genrator
            - Use wave generator for D+ and power supply for D-
        :param:
            - 
        '''
        e.pwr(np.float(ve), 0.05)
        Vdp = ve + diff
        a.appl('DC', 0, 0, Vdp)
        print 'Powr suply @ %.3f' % ve
        print 'Wave Gentr @ %.3f' % Vdp

    def test_diffMode(self, difstp=0.02, vcom=1.5, resrng=0.3):
        '''
        :brief:
            - Test USB common mode range and input sensitivity
        :param:
            - vcom sets common mode
            - difstep sets sweep step size
        '''
        (a, e) = self.__comMode_eqpPre()
        self.test_rd_inpt_conf()
        res = collections.OrderedDict()
        res_l = []
        if vcom >= resrng:
            vol_l = np.arange(-resrng, resrng + 0.001, difstp)
        else:
            vol_l = np.arange(-vcom, vcom + 0.001, difstp)
        for i in vol_l:
            self.__comMode_eqpConfig(a=a, e=e, diff=i, ve=vcom)
            time.sleep(0.5)
            r = self.test_rd_inpt(pinNum=2)
            res_l.append(r)

        res.update({'ComRng': vol_l})
        res.update({'DiffRd': res_l})
        res = pd.DataFrame(res)
        resolution = res['ComRng'][res['DiffRd'] == 1][0:1]
        print 'Common Mode Voltage %.3fV' % vcom
        print 'Resolution is %dmV' % resolution * 1000
        return res