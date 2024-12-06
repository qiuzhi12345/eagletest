#!/usr/bin/env python
# encoding: utf-8
from baselib.loglib.log_lib import *
from hal.Init import HALS
from rtclib.rtc import ADC_LIB
from rtclib.rtc import RESET_CAUSE
from hal.common import CHIP_ID
from enum import Enum
from baselib.instrument.awg import awg
from baselib.instrument.eps import eps
from baselib.instrument.dm import dm
from baselib.loglib.log_csv import csvreport
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

class BBPLL(object):
    '''
    :brief:
        - test base band PLL frequency for chip 7.2.2
        - use function freqSweep to go through PLL output frequency
            - need GPIB & digital multimeter for GPIO11 voltage measurement
            - see details in function description
        - use function debug to test singal frequency
            - clock frequency is exported to GPIO18, use oscilloscope to check
            - need GPIB & digital multimeter for GPIO11 voltage measurement
            - Will lose serial port connection every time function is executed, reset part to fix
    '''
    def __init__(self, channel, chipv='CHIP722'):
        self.channel = channel
        self.chipv = chipv
        self.chip = HALS(self.channel, self.chipv)
        plt.ion()

    def reg_read(self,reg_list):
        '''
        :brief:
            reads bbpll registers
        '''
        rd_list =[]
        for reg in reg_list:
            reg_rd = getattr(self.chip.HWI2C.bbpll,'%s'%reg)
            rd_list.append(reg_rd)
        return rd_list

    def reg_list(self):
        oc_reg_l  = np.array(['bbadc_dcur','oc_dr1','oc_dr3','oc_dchgp'])
        or_reg_l  = np.array(['or_cal_cap','or_cal_udf','or_cal_ovf','or_cal_end','or_lock'])   
        cfg_reg_l = np.array(['oc_ref_div','oc_div'])
        return oc_reg_l, or_reg_l, cfg_reg_l

    def bbpll_config(self,Rdcur,Rdr1,Rdr3,Rdchgp,Rref_div,Rdiv,frcCap,capVal):
        '''
        :brief:
            - setup bbpll parameters
        '''
        self.chip.HWREG.RTC_CNTL.RTC_OPTIONS0.reg_bb_i2c_force_pd=0
        self.chip.HWREG.RTC_CNTL.RTC_OPTIONS0.reg_bbpll_i2c_force_pd=0
        self.chip.HWREG.RTC_CNTL.RTC_OPTIONS0.reg_bbpll_force_pd=0
        #time.sleep(0.5)
        self.chip.HWREG.APB_CTRL.APB_CTRL_SYSCLK_CONF.apb_ctrl_clk_320m_en =1
        #self.chip.HWREG.APB_CTRL.APB_CTRL_CLK_OUT_EN.reg_ctrl_clk_320m_oen =1
        #config PLL
        self.chip.HWI2C.bbpll.bbadc_dcur = Rdcur
        self.chip.HWI2C.bbpll.oc_dr1     = Rdr1
        self.chip.HWI2C.bbpll.oc_dr3     = Rdr3
        self.chip.HWI2C.bbpll.oc_dchgp   = Rdchgp
        self.chip.HWI2C.bbpll.oc_ref_div = Rref_div
        self.chip.HWI2C.bbpll.oc_div     = Rdiv
        self.chip.HWI2C.bbpll.ir_cal_enx_cap = frcCap
        self.chip.HWI2C.bbpll.ir_cal_ext_cap = capVal
        bbpll_freq = 40.0/(1+Rref_div)*(Rdiv+4)
        return bbpll_freq

    def prep_gpib_equip(self):
        '''
        :brief: 
            setup digital multimeter 
        '''
        self.mydm = dm()

    def exportRef(self,enable=0,dtest=0):
        '''
        :brief:
            export pll reference votlages to GPIO11, and measure its value
        '''
        self.chip.rtc_debug.pull_internal_voltage(0)
        self.chip.HWI2C.bbpll.ent_pll = enable
        self.chip.HWI2C.bbpll.dtest   = dtest
        if enable == 1:
            time.sleep(0.5) 
            mrd = np.float(self.mydm.get_result('VDC')) * 1000
        else: mrd = 0 
        return mrd

    def debug(self,Rdcur=1,Rdr1=3,Rdr3=3,Rdchgp=2,Rref_div=15,Rdiv=20,frcCap =0,capVal=4):
        '''
        :brief:
            - exports PLL output to PAD GPIO18
        :param:
            - frcCap: force calibration cap to be fixed
        '''
        self.prep_gpib_equip()
        self.chip.rtc_clk.set_cpu_freq(0)  # set cpu clock to 40M Xtal
        self.chip.rtc_debug.CLK(11,3,1)    # export bbpll signal to PAD DAC2(GPIO18)
        #open clock gating
        en_320m =self.chip.HWREG.APB_CTRL.APB_CTRL_SYSCLK_CONF.apb_ctrl_clk_320m_en
        soc_clk = self.chip.HWREG.APB_CTRL.APB_CTRL_SYSCLK_CONF.apb_ctrl_soc_clk_sel
        oen_320m = self.chip.HWREG.APB_CTRL.APB_CTRL_CLK_OUT_EN.reg_clk_320m_oen
        print 'en:%d oen:%d soc_clk:%d'%(en_320m,oen_320m,soc_clk)
        #setup bbpll
        bbpll_freq = self.bbpll_config(Rdcur,Rdr1,Rdr3,Rdchgp,Rref_div,Rdiv,frcCap,capVal)
        print 'bbpll frequency sets to %dMHz'%bbpll_freq
        time.sleep(1)
        #collect bbpll information
        oc_reg_l = np.array(['bbadc_dcur','oc_dr1','oc_dr3','oc_dchgp'])
        or_reg_l = np.array(['or_cal_cap','or_cal_udf','or_cal_ovf','or_cal_end','or_lock'])    
        cfg_reg_l = np.array(['oc_ref_div','oc_div'])
        cf_rd_l = self.reg_read(cfg_reg_l)
        or_rd_l = self.reg_read(or_reg_l)
        oc_rd_l = self.reg_read(oc_reg_l)
        #pull vcon signal to pad for measurement
        mrd = self.exportRef(enable=1,dtest=0)
        print 'bbpll freq sets to %dMHz'%bbpll_freq
        if frcCap == 1: print 'Force Cap = %d'%capVal
        print 'Divider: %s'%zip(cfg_reg_l,cf_rd_l)
        print 'Configu: %s'%zip(oc_reg_l,oc_rd_l)
        print 'Calibra: %s'%zip(or_reg_l,or_rd_l)
        print 'vcon   : %.2fmV'%mrd
        #open final gating for pll output to GPIO18
        self.chip.HWREG.APB_CTRL.APB_CTRL_SYSCLK_CONF.apb_ctrl_soc_clk_sel =1
        return

    def manualCal_prep(self):
        '''
        :brief:
            - manually calibrate bbpll by using frcCap function
            - observe or_cal_cap reg value:
                - 0: cap value is okay
                - 1: cap value is too small
                - 2: cap value is too high
        :param:
            - frcCap: force calibration cap to be fixed

        '''
        self.chip.rtc_clk.set_cpu_freq(0)  # set cpu clock to 40M Xtal
        #open clock gating
        en_320m =self.chip.HWREG.APB_CTRL.APB_CTRL_SYSCLK_CONF.apb_ctrl_clk_320m_en
        soc_clk = self.chip.HWREG.APB_CTRL.APB_CTRL_SYSCLK_CONF.apb_ctrl_soc_clk_sel
        oen_320m = self.chip.HWREG.APB_CTRL.APB_CTRL_CLK_OUT_EN.reg_clk_320m_oen
        print 'en:%d oen:%d soc_clk:%d'%(en_320m,oen_320m,soc_clk)

    def manualCal(self,Rdcur=1,Rdr1=3,Rdr3=3,Rdchgp=2,Rref_div=15,Rdiv=20,frcCap =1,capVal=4):
        '''
        :brief:
            - manually calibrate bbpll by using frcCap function
            - observe or_cal_cap reg value:
                - 0: cap value is okay
                - 1: cap value is too small
                - 2: cap value is too high
        :param:
            - frcCap: force calibration cap to be fixed

        '''
        #setup bbpll
        self.prep_gpib_equip()
        bbpll_freq = self.bbpll_config(Rdcur,Rdr1,Rdr3,Rdchgp,Rref_div,Rdiv,frcCap,capVal)
        print 'bbpll frequency sets to %dMHz'%bbpll_freq
        time.sleep(1)
        #collect bbpll information
        oc_reg_l = np.array(['bbadc_dcur','oc_dr1','oc_dr3','oc_dchgp'])
        or_reg_l = np.array(['or_cal_cap','or_cal_udf','or_cal_ovf','or_cal_end','or_lock'])    
        cfg_reg_l = np.array(['oc_ref_div','oc_div'])
        cf_rd_l = self.reg_read(cfg_reg_l)
        or_rd_l = self.reg_read(or_reg_l)
        oc_rd_l = self.reg_read(oc_reg_l)
        #pull vcon signal to pad for measurement
        mrd = self.exportRef(enable=1,dtest=0)
        print 'bbpll freq sets to %dMHz'%bbpll_freq
        if frcCap == 1: print 'Force Cap = %d'%capVal
        print 'Divider: %s'%zip(cfg_reg_l,cf_rd_l)
        print 'Configu: %s'%zip(oc_reg_l,oc_rd_l)
        print 'Calibra: %s'%zip(or_reg_l,or_rd_l)
        print 'vcon   : %.2fmV'%mrd
        return

    def regread_update(self,bbpll_table,pll_freq,update_freq=False):
        '''
        :brief:
            - reads register values and update into a dict
            - need to pass a dict, and a list

        '''
        oc_reg_l, or_reg_l, cfg_reg_l = self.reg_list()
        cf_rd_l = self.reg_read(cfg_reg_l)
        or_rd_l = self.reg_read(or_reg_l)
        oc_rd_l = self.reg_read(oc_reg_l)
        for i in np.arange(len(oc_reg_l)): bbpll_table[oc_reg_l[i]].append(oc_rd_l[i])
        for i in np.arange(len(or_reg_l)): bbpll_table[or_reg_l[i]].append(or_rd_l[i])
        for i in np.arange(len(cfg_reg_l)): bbpll_table[cfg_reg_l[i]].append(cf_rd_l[i])
        if update_freq is True:     
            bbpll_freq = 40.0/(1+np.float(cf_rd_l[0]))*(np.float(cf_rd_l[1])+4)
            pll_freq.append(bbpll_freq)
        return cf_rd_l,oc_rd_l,or_rd_l

    def manualCal_swp(self,Rdcur=1,Rdr1=3,Rdr3=3,Rdchgp=2,Rref_div=15,Rdiv=20):
        '''
        :brief:
            - manually calibrate bbpll by using frcCap function
                - ir_cal_ext_cap value is swept from 0 to 15 for specific PLL freq defined above
            - observe or_cal_cap reg value:
                - 0: cap value is okay
                - 1: cap value is too small
                - 2: cap value is too high
        :param:
            - frcCap: force calibration cap to be fixed

        '''
        #setup bbpll
        bbpll_table = collections.OrderedDict()
        oc_reg_l, or_reg_l, cfg_reg_l = self.reg_list()
        for i in np.arange(len(cfg_reg_l)): bbpll_table.update({cfg_reg_l[i]:[]})
        bbpll_table.update({'PLL FREQ':[]})
        for i in np.arange(len(oc_reg_l)): bbpll_table.update({oc_reg_l[i]:[]})
        for i in np.arange(1,len(or_reg_l)): bbpll_table.update({or_reg_l[i]:[]})
        bbpll_table.update({'FrcCapVal':[]})
        bbpll_table.update({or_reg_l[0]:[]}) 
        bbpll_table.update({'vcon'   :[]})
        bbpll_table.update({'dtest=1':[]})
        bbpll_table.update({'dtest=2':[]})
        bbpll_table.update({'dtest=3':[]})
        mtr_0 = []
        mtr_1 = []
        mtr_2 = []
        mtr_3 = []
        pll_freq=[]
        frcCapVal = []
        self.prep_gpib_equip()
        #start_up read
        frcCapVal.append('origin')
        self.regread_update(bbpll_table=bbpll_table,pll_freq=pll_freq,update_freq=True)
        rd_dc = self.exportRef(enable=0)
        mtr_0.append(rd_dc)
        #start to sweep prepare
        self.manualCal_prep()
        #change CPU clock to 40MXtal & pull signal to pad
        self.chip.rtc_clk.set_cpu_freq(0)
        self.chip.rtc_debug.pull_internal_voltage(0)
        #start to sweep
        #translate frequency to oc_div config value
        for i in np.arange(0,16):
            frcCapVal.append(i)
            self.chip.HWREG.RTC_CNTL.RTC_OPTIONS0.reg_bbpll_force_pd=1
            time.sleep(0.5)
            #pll config
            bbpll_freq = self.bbpll_config(Rdcur,Rdr1,Rdr3,Rdchgp,Rref_div,Rdiv,1,i)      
            pll_freq.append(bbpll_freq)
            time.sleep(1)
            cfl,ocl,orl=self.regread_update(bbpll_table=bbpll_table,pll_freq=pll_freq) #read regsiter values
            time.sleep(0.5)
            mtr_read = self.exportRef(enable=1,dtest=0)
            mtr_0.append(mtr_read)
            print 'bbpll frequency sets to %.2fMHz'%bbpll_freq
            print 'Force Cap = %d'%i
            print 'Divider: %s'%zip(cfg_reg_l,cfl)
            print 'Configu: %s'%zip(oc_reg_l,ocl)
            print 'Calibra: %s'%zip(or_reg_l,orl)
            print 'vcon   : %.2fmV'%mtr_read
            self.exportRef(enable=0)
        bbpll_table['FrcCapVal'] =  frcCapVal
        bbpll_table['PLL FREQ'] = pll_freq
        bbpll_table['vcon']    = mtr_0
        bbpll_table['dtest=1'] = mtr_1
        bbpll_table['dtest=2'] = mtr_2
        bbpll_table['dtest=3'] = mtr_3
        bbpll_table = pd.DataFrame(bbpll_table)
        tt = bbpll_table.T
        file_path = '/home/test/Documents/ZBL/chip722/Test/'
        tt.to_csv(file_path+'bbpll_%dMHz_%d_%d_%d_%d_%d_frcCapSwp.csv'
                    %(bbpll_freq,Rdcur,Rdr1,Rdr3,Rdchgp,Rref_div))
        return bbpll_table

    def freqSweep(self,strtFreq=320,endFreq=480,Rdcur=1,Rdr1=3,Rdr3=3,Rdchgp=2,Rref_div=15,
                    frcCap=0, capVal=4):
        '''
        :brief:
            this function sweeps PLL frequency and records register values & vcon voltage
            - Need to use digital multimeter & GPIB
            - results will be saved, check below path_file for specific location
        :param:
            - strtFreq & endFreq: sets pll frequency sweeping range, unit in MHz
        '''
        bbpll_table = collections.OrderedDict()
        oc_reg_l, or_reg_l, cfg_reg_l = self.reg_list()
        for i in np.arange(len(cfg_reg_l)): bbpll_table.update({cfg_reg_l[i]:[]})
        bbpll_table.update({'PLL FREQ':[]})
        for i in np.arange(len(oc_reg_l)): bbpll_table.update({oc_reg_l[i]:[]})
        for i in np.arange(1,len(or_reg_l)): bbpll_table.update({or_reg_l[i]:[]})
        bbpll_table.update({'FrcCapVal':[]})
        bbpll_table.update({or_reg_l[0]:[]}) 
        bbpll_table.update({'vcon'   :[]})
        bbpll_table.update({'dtest=1':[]})
        bbpll_table.update({'dtest=2':[]})
        bbpll_table.update({'dtest=3':[]})
        mtr_0 = []
        mtr_1 = []
        mtr_2 = []
        mtr_3 = []
        pll_freq=[]
        #start_up read
        self.prep_gpib_equip()
        self.regread_update(bbpll_table=bbpll_table,pll_freq=pll_freq,update_freq=True)
        rd_dc = self.exportRef(enable=0)
        mtr_0.append(rd_dc)
        mtr_1.append(rd_dc)
        mtr_2.append(rd_dc)
        mtr_3.append(rd_dc)
        #change CPU clock to 40MXtal & pull signal to pad
        self.chip.rtc_clk.set_cpu_freq(0)
        self.chip.rtc_debug.pull_internal_voltage(0)
        #start to sweep
        #translate frequency to oc_div config value
        strtcnt = np.int(strtFreq/(40.0/(Rref_div+1)))-4
        endcnt  = np.int(endFreq/(40.0/(Rref_div+1)))-4
        for i in np.arange(strtcnt, endcnt+1,1):
            self.chip.HWREG.RTC_CNTL.RTC_OPTIONS0.reg_bbpll_force_pd=1
            time.sleep(0.5)
            #pll config
            bbpll_freq = self.bbpll_config(Rdcur,Rdr1,Rdr3,Rdchgp,Rref_div,i,frcCap,capVal)      
            pll_freq.append(bbpll_freq)
            print 'bbpll frequency sets to %.2fMHz'%bbpll_freq
            time.sleep(1)
            cfl,ocl,orl=self.regread_update(bbpll_table=bbpll_table,pll_freq=pll_freq) #read regsiter values
            time.sleep(0.5)
            rd_dc = []
            for i in np.arange(0,4,1):
                mtr_read = self.exportRef(enable=1,dtest=i)
                rd_dc.append(mtr_read)
            mtr_0.append(rd_dc[0])
            mtr_1.append(rd_dc[1])
            mtr_2.append(rd_dc[2])
            mtr_3.append(rd_dc[3])
            print 'Divider: %s'%zip(cfg_reg_l,cfl)
            print 'Configu: %s'%zip(oc_reg_l,ocl)
            print 'Calibra: %s'%zip(or_reg_l,orl)
            print 'vcon   : %.2fmV'%rd_dc[0]
            self.exportRef(enable=0)
        bbpll_table['PLL FREQ']= pll_freq
        bbpll_table['vcon']    = mtr_0
        bbpll_table['dtest=1'] = mtr_1
        bbpll_table['dtest=2'] = mtr_2
        bbpll_table['dtest=3'] = mtr_3
        bbpll_table = pd.DataFrame(bbpll_table)
        tt = bbpll_table.T
        file_path = '/home/test/Documents/ZBL/chip722/Test/'
        if frcCap == 0:
            tt.to_csv(file_path+'bbpll_%dMHz_%dMHz_%d_%d_%d_%d_%d.csv'
                    %(strtFreq,endFreq,Rdcur,Rdr1,Rdr3,Rdchgp,Rref_div))
        elif frcCap == 1:
            tt.to_csv(file_path+'bbpll_%dMHz_%dMHz_%d_%d_%d_%d_%d_frcCap%d.csv'
                    %(strtFreq,endFreq,Rdcur,Rdr1,Rdr3,Rdchgp,Rref_div,capVal))
        return bbpll_table

    def freqSwp_cal(self,strtFreq=320,endFreq=480,Rdcur=1,Rdr1=3,Rdr3=3,Rdchgp=2,Rref_div=15):
        '''
        :brief:
            this function sweeps PLL frequency and records register values & vcon voltage
            NOTE: force cap function is used as calibration method
            - cal method: scans ir_cal_ext_cap value is swept from 0 to 15 to find best fit
            - Need to use digital multimeter & GPIB
            - results will be saved, check below path_file for specific location
        :param:
            - strtFreq & endFreq: sets pll frequency sweeping range, unit in MHz
        '''
        bbpll_table = collections.OrderedDict()
        oc_reg_l, or_reg_l, cfg_reg_l = self.reg_list()
        for i in np.arange(len(cfg_reg_l)): bbpll_table.update({cfg_reg_l[i]:[]})
        bbpll_table.update({'PLL FREQ':[]})
        for i in np.arange(len(oc_reg_l)): bbpll_table.update({oc_reg_l[i]:[]})
        for i in np.arange(1,len(or_reg_l)): bbpll_table.update({or_reg_l[i]:[]})
        bbpll_table.update({'FrcCapVal':[]})
        bbpll_table.update({or_reg_l[0]:[]}) 
        bbpll_table.update({'vcon'   :[]})
        pll_freq  = []
        frcCapVal = []
        mtr_0     = []

        #start_up read
        self.prep_gpib_equip()
        self.regread_update(bbpll_table=bbpll_table,pll_freq=pll_freq,update_freq=True)
        rd_dc = self.exportRef(enable=0)
        mtr_0.append(rd_dc)
        frcCapVal.append('origin')
        #change CPU clock to 40MXtal & pull signal to pad
        self.chip.rtc_clk.set_cpu_freq(0)
        self.chip.rtc_debug.pull_internal_voltage(0)
        #start to sweep
        #translate frequency to oc_div config value
        strtcnt = np.int(strtFreq/(40.0/(Rref_div+1)))-4
        endcnt  = np.int(endFreq/(40.0/(Rref_div+1)))-4
        for i in np.arange(strtcnt, endcnt+1,1):
            self.chip.HWREG.RTC_CNTL.RTC_OPTIONS0.reg_bbpll_force_pd=1
            time.sleep(0.5)
            #pll config
            for n in np.arange(16):
                #calibration loop to find desired cap value, when or_cal_cap == 0
                capVal = 15-n
                bbpll_freq = self.bbpll_config(Rdcur,Rdr1,Rdr3,Rdchgp,Rref_div,i,1,capVal)
                time.sleep(1)
                or_rd_tmp = self.reg_read(or_reg_l)
                print 'Try capVal: %s'%capVal
                print 'or_cal_cap: %s'%or_rd_tmp[0]
                if or_rd_tmp[0] == 0: break
            print 'or_cal_cap is 0, returns %d'%capVal
            cfl,ocl,orl=self.regread_update(bbpll_table=bbpll_table,pll_freq=pll_freq) #read regsiter values
            frcCapVal.append(capVal)
            time.sleep(0.5)
            mtr_read = self.exportRef(enable=1,dtest=0)
            pll_freq.append(bbpll_freq)
            mtr_0.append(mtr_read)
            print 'bbpll frequency sets to %.2fMHz'%bbpll_freq
            print 'FrcCapVal: %s'%capVal
            print 'Divider: %s'%zip(cfg_reg_l,cfl)
            print 'Configu: %s'%zip(oc_reg_l,ocl)
            print 'Calibra: %s'%zip(or_reg_l,orl)
            print 'vcon   : %.2fmV'%mtr_read
            self.exportRef(enable=0)
        bbpll_table['PLL FREQ'] =pll_freq
        bbpll_table['FrcCapVal']=frcCapVal
        bbpll_table['vcon']     =mtr_0
        bbpll_table = pd.DataFrame(bbpll_table)
        tt = bbpll_table.T
        file_path = '/home/test/Documents/ZBL/chip722/Test/'
        tt.to_csv(file_path+'bbpll_%dMHz_%dMHz_%d_%d_%d_%d_%d_frcCapCal.csv'
                    %(strtFreq,endFreq,Rdcur,Rdr1,Rdr3,Rdchgp,Rref_div))
        return bbpll_table

    def freqSwp_frcCap(self,strtFreq=320,endFreq=480,Rdcur=1,Rdr1=3,Rdr3=3,Rdchgp=2,Rref_div=15,capVal=4):
        '''
        :brief:
            this function sweeps PLL frequency and records register values & vcon voltage
            NOTE: 
            - force cap function is used as calibration method
            - fixed ir_cal_ext_cap value is usec
            - Need to use digital multimeter & GPIB
            - results will be saved, check below path_file for specific location
        :param:
            - strtFreq & endFreq: sets pll frequency sweeping range, unit in MHz
        '''
        #data prepare
        bbpll_table = collections.OrderedDict()
        oc_reg_l, or_reg_l, cfg_reg_l = self.reg_list()
        for i in np.arange(len(cfg_reg_l)): bbpll_table.update({cfg_reg_l[i]:[]})
        bbpll_table.update({'PLL FREQ':[]})
        for i in np.arange(len(oc_reg_l)): bbpll_table.update({oc_reg_l[i]:[]})
        for i in np.arange(1,len(or_reg_l)): bbpll_table.update({or_reg_l[i]:[]})
        bbpll_table.update({'FrcCapVal':[]})
        bbpll_table.update({or_reg_l[0]:[]}) 
        bbpll_table.update({'vcon'   :[]})
        pll_freq  = []
        frcCapVal = []
        mtr_0     = []
        #start_up read
        self.prep_gpib_equip()
        self.regread_update(bbpll_table=bbpll_table,pll_freq=pll_freq,update_freq=True)
        rd_dc = self.exportRef(enable=0)
        mtr_0.append(rd_dc)
        frcCapVal.append('origin')
        #change CPU clock to 40MXtal & pull signal to pad
        self.chip.rtc_clk.set_cpu_freq(0)
        self.chip.rtc_debug.pull_internal_voltage(0)
        #start to sweep
        #translate frequency to oc_div config value
        strtcnt = np.int(strtFreq/(40.0/(Rref_div+1)))-4
        endcnt  = np.int(endFreq/(40.0/(Rref_div+1)))-4
        bbpll_freq = self.bbpll_config(Rdcur,Rdr1,Rdr3,Rdchgp,Rref_div,strtcnt,1,capVal)
        for i in np.arange(strtcnt, endcnt+1,1): 
            #pll config
            self.chip.HWI2C.bbpll.oc_div     = i
            bbpll_freq = 40.0/(1+Rref_div)*(i+4)
            cfl,ocl,orl=self.regread_update(bbpll_table=bbpll_table,pll_freq=pll_freq) #read regsiter values
            frcCapVal.append(capVal)
            time.sleep(0.5)
            mtr_read = self.exportRef(enable=1,dtest=0)
            pll_freq.append(bbpll_freq)
            mtr_0.append(mtr_read)
            print 'bbpll frequency sets to %.2fMHz'%bbpll_freq
            print 'FrcCapVal: %s'%capVal
            print 'Divider: %s'%zip(cfg_reg_l,cfl)
            print 'Configu: %s'%zip(oc_reg_l,ocl)
            print 'Calibra: %s'%zip(or_reg_l,orl)
            print 'vcon   : %.2fmV'%mtr_read
            self.exportRef(enable=0)
        bbpll_table['PLL FREQ'] =pll_freq
        bbpll_table['FrcCapVal']=frcCapVal
        bbpll_table['vcon']     =mtr_0
        bbpll_table = pd.DataFrame(bbpll_table)
        tt = bbpll_table.T
        file_path = '/home/test/Documents/ZBL/chip722/Test/'
        tt.to_csv(file_path+'bbpll_%dMHz_%dMHz_%d_%d_%d_%d_%d_fixedCapVal%d.csv'
                    %(strtFreq,endFreq,Rdcur,Rdr1,Rdr3,Rdchgp,Rref_div,capVal))
        return bbpll_table


