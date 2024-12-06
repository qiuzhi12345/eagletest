#!/usr/bin/env python
import i2c
from wifilib import mem
global xtal, div_offset
xtal       = 40
div_offset = 32

def reset(chan_id='com'):
    mem.wrm(0x600060a0,21,18,0xa) #set adc/dac_pwd for pll_cal_stop

    i2c.wi('rfpll_sdm',1,0xF3, chan_id)
    #i2c.wi('rfpll',8, 0x00, chan_id)
    i2c.wic('xtal','ir_xtal_dac_ext',8)
    i2c.wic('xtal','ir_xtal_dac_enx',1)
    #i2c.wic('rfpll','dvco_amp', 0x1)
    i2c.wic('rfpll','dvco_amp', 0x3)
    i2c.wic('rfpll','ir_enb_dac_dec1', 0x01)
    i2c.wic('rfpll','ir_enb_dac_dec2', 0x01)
    ##i2c.wic('rfpll','ir_ext_dchgp', 0x0)
    ##i2c.wic('rfpll','ir_enx_dchgp', 0x1)
    i2c.wic('rfpll','or_dvco_kvco', 0x0)
    i2c.wic('rfpll','dhref',0x03)
    #i2c.wic('rfpll','or_dvco_kvco', 0x1)
    i2c.wic('rfpll','lf_hbw', 0x1)
    i2c.wic('rfpll','ir_amplf_close', 0x0)
    i2c.wic('rfpll','ir_amplf_open', 0x7) #26M---0xe;40M---0x7
    i2c.wic('rfpll','ir_fcal_delay',0x1f)
    ##i2c.wic('ckgen','sel_plan_b',1)
    ##i2c.wi('rfpll',3, 0x71, chan_id)
    ##i2c.wi('rfpll',4, 0x30, chan_id)
##    i2c.wi('xtal' ,0, 0x53, chan_id)  //40m crystal not work
##    i2c.wi('rfpll', 10, 0xA6, chan_id) # Reset VTR
##    i2c.wi('rfpll', 10, 0xA7, chan_id) # Start
##    i2c.wi('rfpll', 10, 0xA5, chan_id) # End
##    i2c.wi('rfpll_sdm',1,0xF3, chan_id)
##    i2c.wi('rfpll',11, 0xC0, chan_id)


def reset_old(chan_id='com'):
    mem.wrm(0x600060a0,21,18,0xa) #set adc/dac_pwd for pll_cal_stop

    i2c.wi('rfpll_sdm',1,0xF3, chan_id)
    #i2c.wic('rfpll','or_dvco_kvco', 0x0)
    #i2c.wic('rfpll','ir_ext_dchgp', 0x0)
    #i2c.wic('rfpll','dvco_amp', 0x1)
    #i2c.wic('rfpll','lf_hbw', 0x0)
    #i2c.wic('rfpll','ir_enx_dchgp',0)
    i2c.wi('rfpll',8, 0x00, chan_id)
    i2c.wi('rfpll',3, 0x71, chan_id)
    i2c.wi('rfpll',4, 0x10, chan_id)
##    i2c.wi('xtal' ,0, 0x53, chan_id)
##    i2c.wi('rfpll', 10, 0xA6, chan_id) # Reset VTR
##    i2c.wi('rfpll', 10, 0xA7, chan_id) # Start
##    i2c.wi('rfpll', 10, 0xA5, chan_id) # End
##    i2c.wi('rfpll_sdm',1,0xF3, chan_id)
##    i2c.wi('rfpll',11, 0xC0, chan_id)


def set_freq(frf, chan_id='com',cry_freq=40):
    reset(chan_id)
    fvco    = frf * 4 / 3.0
    div_sdm = (fvco / float(cry_freq)) - 32
    x1      = int(div_sdm)
    x2_f    = (div_sdm - x1) * 256
    x2      = int(x2_f)
    x3      = int((x2_f - x2) * 256)
    # Write results into RFPLL_SDM I2C
    i2c.wi('rfpll_sdm',0x00, 0x07, chan_id) # Reset SDM
    i2c.wi('rfpll_sdm',0x03, x1, chan_id)
    i2c.wi('rfpll_sdm',0x04, x2, chan_id)
    i2c.wi('rfpll_sdm',0x05, x3, chan_id)
    i2c.wi('rfpll_sdm',0x00, 0x17, chan_id) # Reset SDM
    restart_cal(chan_id)

def set_freq_26M(frf, chan_id='com'):
    #i2c.wi('xtal' ,0, 0x53, chan_id)
    reset(chan_id)
    fvco    = frf * 4 / 3.0
    div_sdm = (fvco / 26.0) - 32
    x1      = int(div_sdm)
    x2_f    = (div_sdm - x1) * 256
    x2      = int(x2_f)
    x3      = int((x2_f - x2) * 256)
    # Write results into RFPLL_SDM I2C
    i2c.wi('rfpll_sdm',0x00, 0x07, chan_id) # Reset SDM
    i2c.wi('rfpll_sdm',0x03, x1, chan_id)
    i2c.wi('rfpll_sdm',0x04, x2, chan_id)
    i2c.wi('rfpll_sdm',0x05, x3, chan_id)
    i2c.wi('rfpll_sdm',0x00, 0x17, chan_id) # Reset SDM
    restart_cal(chan_id)

def set_freq_24M(frf, chan_id='com'):
    reset(chan_id)
    fvco    = frf * 4 / 3.0
    div_sdm = (fvco / 24.0) - 32
    x1      = int(div_sdm)
    x2_f    = (div_sdm - x1) * 256
    x2      = int(x2_f)
    x3      = int((x2_f - x2) * 256)
    # Write results into RFPLL_SDM I2C
    i2c.wi('rfpll_sdm',0x00, 0x07, chan_id) # Reset SDM
    i2c.wi('rfpll_sdm',0x03, x1, chan_id)
    i2c.wi('rfpll_sdm',0x04, x2, chan_id)
    i2c.wi('rfpll_sdm',0x05, x3, chan_id)
    i2c.wi('rfpll_sdm',0x00, 0x17, chan_id) # Reset SDM
    restart_cal(chan_id)

def restart_cal(chan_id='com'):
    i2c.wic('rfpll','ir_enx_dchgp', 0x1)
    i2c.wi('rfpll', 0, 0x5f, chan_id)
    i2c.wi('rfpll', 0, 0x7f, chan_id)
    i2c.wi('rfpll', 0, 0x3f, chan_id)
    #wait pll cal end
    while 1:
       if(int(i2c.ri('rfpll', 7),16)&0x80!=0):
          break;
    i2c.wic('rfpll','ir_ext_dchgp', 0x2)# 40M---2;26M---3
    i2c.wic('rfpll','ir_enx_dchgp', 0x1)# 40M---1

    mem.wrm(0x600060a0,21,18,0x0) #set adc/dac_pwd for pll_cal_stop


def force_dac_cap(force=0, cap=0x80, dac=0x10):
    if force==1:
        i2c.wic('rfpll', 'ir_cap_ext', cap)
        i2c.wic('rfpll', 'ir_dac_ext', dac)
    or_pll_cap = i2c.ric('rfpll', 'or_pll_cap')
    or_pll_dac = i2c.ric('rfpll', 'or_pll_dac')
    ir_cap_ext = i2c.ric('rfpll', 'ir_cap_ext')
    ir_dac_ext = i2c.ric('rfpll', 'ir_dac_ext')
    print 'or_pll_cap=%d, or_pll_dac=%d, ir_cap_ext=%d, ir_dac_ext=%d\n'%(or_pll_cap, or_pll_dac, ir_cap_ext, ir_dac_ext)
    return [or_pll_cap, or_pll_dac, ir_cap_ext, ir_dac_ext]


def rfpll_ircap_sweep(instr=''):
    f = open('../rfpll_ircap_sweep_ESP32_%s.csv'%instr, 'w')
    f.write('freq, ir_cap_ext, ir_dac_ext, or_pll_cap, or_pll_dac\n')
    freq=2412
    for ircap in range(0, 130):
        for irdac in range(0, 20, 8):
            if irdac==16:
                irdac = 15
            force_dac_cap(force=1, cap=ircap, dac=irdac)
            for i in range(0,2):
                set_freq(freq)
                [or_pll_cap, or_pll_dac, ir_cap_ext, ir_dac_ext] = force_dac_cap()
                f.write('%d,%d,%d,%d,%d\n'%(freq, ir_cap_ext, ir_dac_ext, or_pll_cap, or_pll_dac))


#==========================
# RFPLL_SDM registers
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

def read_rfpll_reg():

    i2c.ric('xtal','ir_xtal_dac_ext')
    i2c.ric('xtal','ir_xtal_dac_enx')
    i2c.ric('rfpll','dvco_amp')
    ##i2c.wic('rfpll','ir_ext_dchgp', 0x0)
    ##i2c.wic('rfpll','ir_enx_dchgp', 0x1)
    i2c.ric('rfpll','or_dvco_kvco')
    i2c.ric('rfpll','lf_hbw')
    i2c.ric('rfpll','ir_amplf_close')
    i2c.ric('rfpll','ir_amplf_open')
    i2c.ric('rfpll','ir_fcal_delay')
    i2c.ric('rfpll','ir_ext_dchgp')
    i2c.ric('rfpll','ir_enx_dchgp')

def rfpll_reg_set(read=0, ir_amplf_open=0, ir_amplf_close=7, ir_en_pll_mon=1, ir_enx_dac=1, ir_dac_ext=12):
    if read==1:
        ir_amplf_open = i2c.ric('rfpll','ir_amplf_open')
        ir_amplf_close = i2c.ric('rfpll','ir_amplf_close')
        ir_en_pll_mon = i2c.ric('rfpll','ir_en_pll_mon')
        ir_enx_dac = i2c.ric('rfpll','ir_enx_dac')
        ir_dac_ext = i2c.ric('rfpll','ir_dac_ext')
        print "ir_amplf_open=%d"%ir_amplf_open
        print "ir_amplf_close=%d"%ir_amplf_close
        print "ir_en_pll_mon=%d"%ir_en_pll_mon
        print "ir_enx_dac=%d"%ir_enx_dac
        print "ir_dac_ext=%d"%ir_dac_ext
    else:
        i2c.wic('rfpll','ir_amplf_open', ir_amplf_open)
        i2c.wic('rfpll','ir_amplf_close', ir_amplf_close)
        i2c.wic('rfpll','ir_en_pll_mon', ir_en_pll_mon)
        i2c.wic('rfpll','ir_enx_dac', ir_enx_dac)
        i2c.wic('rfpll','ir_dac_ext', ir_dac_ext)



