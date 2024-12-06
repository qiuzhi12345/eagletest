from baselib.test_channel.com import COM as com
from baselib.loglib.log_lib import *
from hal.hwregister.hwi2c.all import *
from hal.common import *
import random
import time
import numpy as np
from rftest.rflib import rfglobal
from hal.rtc_debug import RTC_DEBUG
from hal.adc import RTC_ADC2
from hal.wifi_api import WIFIAPI
from hal.hwregister.hwreg.all import *

class rfpll(object):

    def __init__(self,comport,chipv='ESP32'):
        self.comport = comport
        self.chipv = chipv
        self.i2c = HWI2C(self.comport,self.chipv)
        self.mem = MEM(self.comport,self.chipv)
        self.rtc_debug = RTC_DEBUG(self.comport,self.chipv)
        self.rtc_adc2 = RTC_ADC2(self.comport,self.chipv)
        self.wifiapi = WIFIAPI(self.comport,self.chipv)
        self.hwreg = HWREG(self.comport,self.chipv)


    def reset(self):
        if self.chipv=='ESP8266':
            self.mem.wrm(0x600005c8,23,20,0xf) #set adc/dac_pwd for pll_cal_stop
            self.i2c.rfpll.reg_addr_wr( 10, 0xA6) # Reset VTR
            self.i2c.rfpll.reg_addr_wr( 10, 0xA7) # Start
            self.i2c.rfpll.reg_addr_wr( 10, 0xA5) # End
            self.i2c.rfpll_sdm.reg_addr_wr(1,0xF3)
            self.i2c.rfpll.reg_addr_wr(11, 0xC0)
        else:
            self.mem.wrm(0x600060a0,21,18,0xa) #set adc/dac_pwd for pll_cal_stop
##            self.i2c.rfpll_sdm.reg_addr_wr(1,0xF3)
##            self.i2c.xtal.ir_xtal_dac_ext=8
##            self.i2c.xtal.ir_xtal_dac_enx=1
##            self.i2c.rfpll.dvco_amp= 0x3
##            self.i2c.rfpll.ir_enb_dac_dec1= 0x01
##            self.i2c.rfpll.ir_enb_dac_dec2= 0x01
##            self.i2c.rfpll.or_dvco_kvco= 0x0
##            self.i2c.rfpll.dhref=0x03
##            #self.i2c.rfpll.dlref=0x3
##            self.i2c.rfpll.lf_hbw= 0x0
##            self.i2c.rfpll.ir_amplf_close= 0x0
##            self.i2c.rfpll.ir_amplf_open= 0x7 #26M---0xe;40M---0x7
##            self.i2c.rfpll.ir_fcal_delay=0x1f
            self.i2c.rfpll.ir_enx_dac = 0
            self.i2c.rfpll.ir_dac_ext = 8
            self.i2c.rfpll.ir_enx_cap = 0
##            self.i2c.rfpll.ir_cap_ext = 0


    def set_freq(self,frf,cry_freq=40, restart_en=1):
        if self.chipv == "CHIP723":
            self.wifiapi.phy_set_freq(frf, 0)
            return 1

        if restart_en==1:
            self.reset()
        fvco    = frf * 4 / 3.0
        print fvco
        div_sdm = (fvco / float(cry_freq)) - 32
        print div_sdm*256*256
        x1      = int(div_sdm)
        x2_f    = (div_sdm - x1) * 256
        x2      = int(x2_f)
        x3      = int((x2_f - x2) * 256)
        # Write results into rfpll_sdm I2C
        self.i2c.rfpll_sdm.reg_addr_wr(0x0, 0x07) # Reset SDM

        self.i2c.rfpll_sdm.reg_addr_wr(0x3, x1)

        self.i2c.rfpll_sdm.reg_addr_wr(0x4, x2)

        self.i2c.rfpll_sdm.reg_addr_wr(0x5, x3)

        self.i2c.rfpll_sdm.reg_addr_wr(0x0, 0x17) # Reset SDM

        if restart_en==1:
            self.restart_cal()

    def set_freq_test(self,frf,cry_freq=40):
        self.reset()
        self.i2c.ckgen.sel_plan_b = 1
        fvco    = frf * 3 / 2.0
        div_sdm = (fvco / float(cry_freq)) - 32
        x1      = int(div_sdm)
        x2_f    = (div_sdm - x1) * 256
        x2      = int(x2_f)
        x3      = int((x2_f - x2) * 256)
        # Write results into rfpll_sdm I2C
        self.i2c.rfpll_sdm.reg_addr_wr(0x00, 0x07) # Reset SDM

        self.i2c.rfpll_sdm.reg_addr_wr(0x03, x1)

        self.i2c.rfpll_sdm.reg_addr_wr(0x04, x2)

        self.i2c.rfpll_sdm.reg_addr_wr(0x05, x3)

        self.i2c.rfpll_sdm.reg_addr_wr(0x00, 0x17) # Reset SDM

        self.restart_cal()


    def restart_cal(self):

        self.i2c.rfpll.reg_addr_wr( 0, 0x5f)

        self.i2c.rfpll.reg_addr_wr( 0, 0x7f)

        self.i2c.rfpll.reg_addr_wr( 0, 0x3f)

        #wait pll cal end
##        while 1:
##           if(self.i2c.rfpll.reg_addr_rd( 7)&0x80!=0):
##
##              break;

        if self.chipv=='ESP8266':
			self.mem.wrm(0x600005c8,23,20,0x0) #set adc/dac_pwd for pll_cal_stop
        else:
        	self.mem.wrm(0x600060a0,21,18,0x0) #set adc/dac_pwd for pll_cal_stop

    #==========================
    # rfpll_sdm registers
    #==========================
    #00_0    xpd_sdm          {1}
    #00_1    xpd_chgp         {1}
    #00_2    xpd_test         {1}
    #00_3    sdm_stop         {0}
    #00_4    sdm_rstb         {1}
    #00_5    sdm_dither       {1}
    #01_2_1  dtest[1:0]       {00}
    #01_3    ent_chgp         {0}
    #01_4    ent_sdm          {0}
    #01_5    ent_bias         {0}
    #02_0    dsdm_24          {0}
    #03_7_0  dsdm_23_16       {00101001}
    #04_7_0  dsdm_15_8        {01100110}
    #05_7_0  dsdm_7_0         {01100110}

    def read_rfpll_reg(self):

        self.i2c.xtal.ir_xtal_dac_ext

        self.i2c.xtal.ir_xtal_dac_enx

        self.i2c.rfpll.dvco_amp

        ##self.i2c.rfpll.ir_ext_dchgp= 0x0

        ##self.i2c.rfpll.ir_enx_dchgp= 0x1

        self.i2c.rfpll.or_dvco_kvco

        self.i2c.rfpll.lf_hbw

        self.i2c.rfpll.ir_amplf_close

        self.i2c.rfpll.ir_amplf_open

        self.i2c.rfpll.ir_fcal_delay

        self.i2c.rfpll.ir_ext_dchgp

        self.i2c.rfpll.ir_enx_dchgp


    def set_freq_outband(freq):
    #    rfpll.reset()
        self.set_freq(freq)
        dict_cct = {
            2300: [15, 15],
            2400: [12, 12],
            2500: [10, 10],
            2600: [8, 8],
            2700: [6, 6],
            2800: [5, 5],
            2900: [4, 4]
            }
        if freq in dict_cct:
            self.i2c.RFTX.TMX_CCT_LOAD=dict_cct[freq][0]
            self.i2c.RFTX.TMX_CCT_LOAD=dict_cct[freq][1]

    def rf_counter(self,fc_counts_en=240, RF_freq=2452):
        if self.chipv=="CHIP722":
            self.i2c.rfpll.ir_sel_fcnt_cal = 1
            self.i2c.xtal.xpd_rc = 1
            self.i2c.ckgen.xpd_fc = 1
##            self.i2c.ckgen.sel_plan_b = 1

            self.i2c.ckgen.fc_counts_en_7_0 = fc_counts_en&0xff
            self.i2c.ckgen.fc_counts_en_9_8 = fc_counts_en>>8

            cout_target = (fc_counts_en*RF_freq*2/40/3)
            print cout_target
            self.i2c.ckgen.fc_cout_target_7_0 = cout_target & 0xff
            self.i2c.ckgen.fc_cout_target_13_8 = cout_target >> 8


            self.i2c.ckgen.fc_start = 0
            self.i2c.ckgen.fc_reset_n = 0
            self.i2c.ckgen.fc_reset_n = 1
            self.i2c.ckgen.fc_start = 1
            time.sleep(0.1)

            cint = (self.i2c.ckgen.fc_cint_13_8<<8) + self.i2c.ckgen.fc_cint_7_0
            print cint
            self.i2c.xtal.xpd_rc = 1
##            self.i2c.ckgen.sel_plan_b = 1

            self.i2c.rfpll.ir_sel_fcnt_cal = 1
            self.i2c.rfpll.ir_pll_cal_start = 1
##            self.i2c.rfpll.ir_pll_cal_rstb = 0
##            self.i2c.rfpll.ir_pll_cal_rstb = 1
            self.i2c.rfpll.ir_pll_cal_start = 0


##            self.i2c.rfpll.ir_sel_fcnt_cal = 1
##            self.restart_cal()
##
##            _cint = (self.i2c.ckgen.fc_cint_13_8<<8) + self.i2c.ckgen.fc_cint_7_0
##            print hex(_cint)


##            self.i2c.rfpll.ir_sel_fcnt_cal = 0
##            self.i2c.ckgen.xpd_fc = 1
##            self.i2c.ckgen.fc_counts_en_7_0 = fc_counts_en
##            self.i2c.ckgen.fc_cout_target_7_0 = ((fc_counts_en/40)*2/3*RF_freq)&0xff
##            self.i2c.ckgen.fc_cout_target_13_8 = ((fc_counts_en/40)*2/3*RF_freq)>>8
##            time.sleep(0.1)
##
##            cint = (self.i2c.ckgen.fc_cint_13_8<<8) + self.i2c.ckgen.fc_cint_7_0
##            print hex(cint)
##
##            self.i2c.rfpll.ir_sel_fcnt_cal = 1
##            self.restart_cal()
##
##            cint = (self.i2c.ckgen.fc_cint_13_8<<8) + self.i2c.ckgen.fc_cint_7_0
##            print hex(cint)

        else:
            self.i2c.xtal.xpd_rc = 1
            self.i2c.ckgen.xpd_fc = 1
            self.i2c.ckgen.sel_plan_b = 1
            self.i2c.ckgen.fc_counts_en_7_0 = count_en&0xff
            self.i2c.ckgen.fc_counts_en_9_8 = count_en>>8
            self.i2c.ckgen.fc_reset_n = 0
            self.i2c.ckgen.fc_start = 0
            self.i2c.ckgen.fc_reset_n = 1
            self.i2c.ckgen.fc_start = 1
            time.sleep(0.1)

##            cint = (self.i2c.ckgen.fc_cint_13_8<<8) + self.i2c.ckgen.fc_cint_7_0
            self.i2c.ckgen.sel_plan_b = 0
            self.i2c.xtal.xpd_rc = 0
            self.i2c.rfpll.ir_sel_fcnt_cal=1
##            print cint

    def rfpll_set_reg(self, modify=1):
        if modify==1:
            self.i2c.rfpll.dvco_amp_incw=1
            self.i2c.rfpll.or_dvco_kvco = 2
            self.i2c.rfpll.ir_ext_dchgp = 0
            self.i2c.rfpll.dhref = 2
            self.i2c.rfpll.dlref = 2
        else:
            self.i2c.rfpll.dvco_amp_incw=0
            self.i2c.rfpll.or_dvco_kvco = 0
            self.i2c.rfpll.ir_ext_dchgp = 7
            self.i2c.rfpll.dhref = 3
            self.i2c.rfpll.dlref = 2
##        print "ir_cap_ext=%d"%self.i2c.rfpll.ir_cap_ext
##        print "ir_enb_dac_dec1=%d"%self.i2c.rfpll.ir_enb_dac_dec1
##        print "ir_enb_dac_dec2=%d"%self.i2c.rfpll.ir_enb_dac_dec2
##        print "ir_enx_dchgp=%d"%self.i2c.rfpll.ir_enx_dchgp
##        print "dvco_amp=%d"%self.i2c.rfpll.dvco_amp
##
##        self.i2c.rfpll.ir_cap_ext = 63
##        self.i2c.rfpll.ir_enb_dac_dec1 = 0
##        self.i2c.rfpll.ir_enb_dac_dec2 = 0
##        self.i2c.rfpll.ir_enx_dchgp = 0
##        self.i2c.rfpll.dvco_amp = 2
##
##        print "ir_cap_ext=%d"%self.i2c.rfpll.ir_cap_ext
##        print "ir_enb_dac_dec1=%d"%self.i2c.rfpll.ir_enb_dac_dec1
##        print "ir_enb_dac_dec2=%d"%self.i2c.rfpll.ir_enb_dac_dec2
##        print "ir_enx_dchgp=%d"%self.i2c.rfpll.ir_enx_dchgp
##        print "dvco_amp=%d"%self.i2c.rfpll.dvco_amp

##        self.i2c.rfpll.dvco_amp_incw=0
##        self.i2c.rfpll.dvco_amp = 0
##        self.i2c.rfpll.ir_enb_dac_dec1 = 0
##        self.i2c.rfpll.ir_enb_dac_dec2 = 0


    def pll_cap_cal_init(self):
##        self.rtc_adc2.config()
##        self.rtc_adc2.set(atten=2, pad=0,test_pad_en = 1)
##        self.hwreg.SARADC.SAR_READER2_CTRL.reg_sar2_clk_div=1
        self.rtc_debug.pull_internal_voltage(1)
        self.i2c.rfpll.ent_vco_bias = 1
        self.i2c.rfpll.dtest=1
##        self.wifiapi.pll_cap_track_en(0)

    def pll_cap_cal_read(self):
        code_sum = 0
        sum_num = 8
        self.i2c.rfpll.ent_vco_bias = 1
        self.i2c.rfpll.dtest=1
        self.mem.wrm(0x60008834, 31,31, 1)
        self.mem.wrm(0x6000882c, 5,5, 1)
        for i in range(0,sum_num):
            code_sum += int(self.rtc_adc2.read())
        code = float(code_sum)/sum_num
        vol = code/4095.0*1.7
        return [code, vol]

    def get_pll_vol(self, atten=2):
        self.i2c.rfpll.ent_vco_bias = 1
        self.i2c.rfpll.dtest=1
        code = int(self.wifiapi.get_sar2_vol(atten))
        if self.chipv=='CHIP722':
##            vol = code/2.9-250
            vol = code*1.7/4
        elif self.chipv=='ESP32':
            vol = code*1.7/4
        self.mem.wrm(0x6000882c, 5,5, 1) #sar2_en_test
        self.mem.wrm(0x60008834, 31,31, 1) #sar2_rtc_force
        if vol < 0 :
            vol = 0
        return [code, vol]


    def rfpll_dac_test(self, dac_low=1):
        if dac_low==1:
            self.i2c.rfpll.dvco_amp = 0
            self.i2c.rfpll.ir_enb_dac_dec1 = 0
            self.i2c.rfpll.ir_enb_dac_dec2 = 0
        else:
            self.i2c.rfpll.dvco_amp = 3
            self.i2c.rfpll.ir_enb_dac_dec1 = 1
            self.i2c.rfpll.ir_enb_dac_dec2 = 1

    def read_reg(self):
        print 'or_pll_cap=%d'%self.i2c.rfpll.or_pll_cap
        print 'or_pll_cap_8=%d'%self.i2c.rfpll.or_pll_cap_8
        print 'or_pll_dac=%d'%self.i2c.rfpll.or_pll_dac
        print 'or_pll_amp_end=%d'%self.i2c.rfpll.or_pll_amp_end
        print 'or_pll_cal_end=%d'%self.i2c.rfpll.or_pll_cal_end
        print 'or_ampl=%d'%self.i2c.rfpll.or_ampl
        print 'or_amph=%d'%self.i2c.rfpll.or_amph
        print 'or_capl=%d'%self.i2c.rfpll.or_capl
        print 'or_caph=%d'%self.i2c.rfpll.or_caph

    def set_pll_cap(self, channel=1, cap_ext=170):
        self.wifiapi.rfchsel(channel)
        self.i2c.rfpll.ir_ext_dchgp = 7
        self.i2c.rfpll.ir_enx_dac = 1
        self.i2c.rfpll.ir_dac_ext = 15
        self.i2c.rfpll.ir_enx_cap = 1
        self.i2c.rfpll.ir_cap_ext = cap_ext
        self.i2c.rfpll.ir_cap_ext_8 = 0
        self.i2c.rftx.TMX2G_CCT_LOAD = 11
        self.i2c.rftx.PA2G_CCT_STG1 = 11
        self.i2c.rftx.PA2G_CCT_STG2 = 11
        self.wifiapi.set_tx_gain(0x5f, 0x120)

