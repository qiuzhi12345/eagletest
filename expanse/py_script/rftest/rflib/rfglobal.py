#!/usr/bin/env python
"""RF global variable definitions.

rf_global.xlsm - major dict definitions for modu: rftx and rfscan
i2c_table.xlsm - i2c register settings for i2c.ric and i2c.wic
pbus_table.xlsx - pbus register settings for pbus.pbus_rc and pbus.pbus_wc

"""

def rate2addr(rate_sym):
    """Return mem.addr for rate_sym"""
    rate_num = ratedic[rate_sym]
    if rate_num < 8:
        rate_num = rate_num^3
    addr = 0x60000504 + rate_num*4
    return addr


#--------------------------------------------------
# WiFi Related (Chengzhou Wang, 2013/9/05)
#--------------------------------------------------
wifi_txout=False
rfcal=dict(txpwr_backoff_mcs2=0)
rfcal['atten'] = dict()
rfcal['ana_gain'] = dict()
rfcal['pa_gain'] = dict()
rfcal_pwr_backoff = dict()
#--------------------------------------------------
# LR Rate Dic (Kong Lu, 2019/05/10)
#--------------------------------------------------
lr_rate_ls = [
              'lr0'        ,
              'lr1'        ,
              'lr2'        ,
              'lr3'        ,
              'lr4'        ,
              'lr5'        ,
              'lr6'        ,
              'lr7'        ,
              'lr_0_0.125m',
              'lr_1_0.25m' ,
              'lr_2_0.5m'  ,
              'lr_3_0.25m' ,
              'lr_4_0.5m'  ,
              'lr_5_1m'    ,
              'lr_6_0.25m' ,
              'lr_7_0.5m'   ]
#--------------------------------------------------
# 11n Rate Dic (Kong Lu, 2019/06/26)
#--------------------------------------------------
ratedic_11n = {
     'mcs0_' :0x10,
     'mcs1_' :0x11,
     'mcs2_' :0x12,
     'mcs3_' :0x13,
     'mcs4_' :0x14,
     'mcs5_' :0x15,
     'mcs6_' :0x16,
     'mcs7_' :0x17,
     'mcs32_':0x30,
     }
#--------------------------------------------------
# Register Related (Chengzhou Wang, 2013/04/02)
#--------------------------------------------------
ratedic = {
     '1m'   :0x0,
     '2m'   :0x1,
     '2ms'  :0x5,
     '2ml'  :0x1,
     '5.5m' :0x2,
     '5.5ms':0x6,
     '5.5ml':0x2,
     '11m'  :0x3,
     '11ms' :0x7,
     '11ml' :0x3,
     '6m'   :0xb,
     '9m'   :0xf,
     '12m'  :0xa,
     '18m'  :0xe,
     '24m'  :0x9,
     '36m'  :0xd,
     '48m'  :0x8,
     '54m'  :0xc,
     '6m_dup' :0xb,
     '9m_dup' :0xf,
     '12m_dup':0xa,
     '18m_dup':0xe,
     '24m_dup':0x9,
     '36m_dup':0xd,
     '48m_dup':0x8,
     '54m_dup':0xc,
     '1.5m_5' :0xb,
     '2.25m_5':0xf,
     '3m_5'   :0xa,
     '4.5m_5' :0xe,
     '6m_5'   :0x9,
     '9m_5'   :0xd,
     '12m_5'  :0x8,
     '13.5m_5':0xc,
     '3m_10'  :0xb,
     '4.5m_10':0xf,
     '6m_10'  :0xa,
     '9m_10'  :0xe,
     '12m_10' :0x9,
     '18m_10' :0xd,
     '24m_10' :0x8,
     '27m_10' :0xc,
     'mcs0' :0x10,
     'mcs1' :0x11,
     'mcs2' :0x12,
     'mcs3' :0x13,
     'mcs4' :0x14,
     'mcs5' :0x15,
     'mcs6' :0x16,
     'mcs7' :0x17,
     'mcs32':0x30,
     'mcs0_40' :0x10,
     'mcs1_40' :0x11,
     'mcs2_40' :0x12,
     'mcs3_40' :0x13,
     'mcs4_40' :0x14,
     'mcs5_40' :0x15,
     'mcs6_40' :0x16,
     'mcs7_40' :0x17,
     'mcs32_40':0x30,
     'mcs0_sgi' :0x10,
     'mcs1_sgi' :0x11,
     'mcs2_sgi' :0x12,
     'mcs3_sgi' :0x13,
     'mcs4_sgi' :0x14,
     'mcs5_sgi' :0x15,
     'mcs6_sgi' :0x16,
     'mcs7_sgi' :0x17,
     'mcs32_sgi':0x30,
     'mcs0_40_sgi' :0x10,
     'mcs1_40_sgi' :0x11,
     'mcs2_40_sgi' :0x12,
     'mcs3_40_sgi' :0x13,
     'mcs4_40_sgi' :0x14,
     'mcs5_40_sgi' :0x15,
     'mcs6_40_sgi' :0x16,
     'mcs7_40_sgi' :0x17,
     'mcs32_40_sgi':0x30,
     'mcs0r' :0x10,
     'mcs1r' :0x11,
     'mcs2r' :0x12,
     'mcs3r' :0x13,
     'mcs4r' :0x14,
     'mcs5r' :0x15,
     'mcs6r' :0x16,
     'mcs7r' :0x17,
     'lr0'   :0x10,
     'lr1'   :0x11,
     'lr2'   :0x12,
     'lr3'   :0x13,
     'lr4'   :0x15,
     'lr5'   :0x16,
     'lr6'   :0x19,
     'lr7'   :0x1a,
     'lr_0_0.125m' :0x10,
     'lr_1_0.25m'  :0x11,
     'lr_2_0.5m'   :0x12,
     'lr_3_0.25m'  :0x15,
     'lr_4_0.5m'   :0x16,
     'lr_5_1m'     :0x17,
     'lr_6_0.25m'  :0x19,
     'lr_7_0.5m'   :0x1a,
     'test' :0x17}

rate_bps_dict = {
     '1m'   :1,
     '2m'   :2,
     '2ms'  :2,
     '2ml'  :2,
     '5.5m' :5.5,
     '5.5ms':5.5,
     '5.5ml':5.5,
     '11m'  :11,
     '11ms' :11,
     '11ml' :11,
     '6m'   :6,
     '9m'   :9,
     '12m'  :12,
     '18m'  :18,
     '24m'  :24,
     '36m'  :36,
     '48m'  :48,
     '54m'  :54,
     'mcs0' :6.5,
     'mcs1' :13,
     'mcs2' :19.5,
     'mcs3' :26,
     'mcs4' :39,
     'mcs5' :52,
     'mcs6' :58.5,
     'mcs7' :65,
     'mcs0_40' :13.5,
     'mcs1_40' :27,
     'mcs2_40' :40.5,
     'mcs3_40' :54,
     'mcs4_40' :81,
     'mcs5_40' :108,
     'mcs6_40' :121.5,
     'mcs7_40' :135,
     'mcs0_sgi' :7.2,
     'mcs1_sgi' :14.4,
     'mcs2_sgi' :21.7,
     'mcs3_sgi' :28.9,
     'mcs4_sgi' :43.3,
     'mcs5_sgi' :57.8,
     'mcs6_sgi' :65,
     'mcs7_sgi' :72.2,
     'mcs0_40_sgi' :15,
     'mcs1_40_sgi' :30,
     'mcs2_40_sgi' :45,
     'mcs3_40_sgi' :60,
     'mcs4_40_sgi' :90,
     'mcs5_40_sgi' :120,
     'mcs6_40_sgi' :135,
     'mcs7_40_sgi' :150
}

power_dict = {
     0x0  : 0,
     0x1  : 0,
     0x2  : 0,
     0x3  : 0,
     0x4  : 0,
     0x5  : 0,
     0x6  : 0,
     0x7  : 0,
     0xb  : 0,
     0xf  : 0,
     0xa  : 0,
     0xe  : 1,
     0x9  : 1,
     0xd  : 2,
     0x8  : 3,
     0xc  : 4,
     0x10 : 0,
     0x11 : 0,
     0x12 : 1,
     0x13 : 1,
     0x14 : 2,
     0x15 : 3,
     0x16 : 4,
     0x17 : 5}

sens_dict = {
     '1m'   : -97,
     '2m'   : -95,
     '2ms'  : -95,
     '2ml'  : -95,
     '5.5m' : -93,
     '5.5ms': -93,
     '5.5ml': -93,
     '11m'  : -90,
     '11ms' : -90,
     '11ml' : -90,
     '6m'   : -92,
     '9m'   : -92,
     '12m'  : -90,
     '18m'  : -88,
     '24m'  : -85,
     '36m'  : -82,
     '48m'  : -77,
     '54m'  : -75,
     'mcs0' : -92,
     'mcs1' : -90,
     'mcs2' : -87,
     'mcs3' : -84,
     'mcs4' : -81,
     'mcs5' : -76,
     'mcs6' : -74,
     'mcs7' : -71,
     'mcs0_40' : -89,
     'mcs1_40' : -85,
     'mcs2_40' : -83,
     'mcs3_40' : -79,
     'mcs4_40' : -76,
     'mcs5_40' : -72,
     'mcs6_40' : -70,
     'mcs7_40' : -69,
     'lr0'   : -97,
     'lr1'   : -97,
     'lr2'   : -97,
     'lr3'   : -97,
     'lr4'   : -97,
     'lr5'   : -97,
     'lr6'   : -97,
     'lr7'   : -97}

rx_maxlevel_dict={
    '1m'      :  10,
    '2m'      :  10,
    '2ml'     :  10,
    '2ms'     :  10,
    '5.5m'    :  10,
    '5.5ml'   :  10,
    '5.5ms'   :  10,
    '11m'     :  10,
    '11ml'    :  10,
    '11ms'    :  10,
    '6m'      :  10,
    '9m'      :  10,
    '12m'     :  10,
    '18m'     :  4,
    '24m'     : -1,
    '36m'     : -3,
    '48m'     : -6,
    '54m'     : 5,
    'mcs0'    :  10,
    'mcs1'    :  10,
    'mcs2'    :  2,
    'mcs3'    :  3,
    'mcs4'    : -4,
    'mcs5'    : -7,
    'mcs6'    : -8,
    'mcs7'    : 5,
    'mcs0_40' :  10,
    'mcs1_40' :  10,
    'mcs2_40' :  3,
    'mcs3_40' : -2,
    'mcs4_40' : -4,
    'mcs5_40' : -6,
    'mcs6_40' : -7,
    'mcs7_40' : 5
}

ESP32_target_pwr_dict={
    '1m'      :  19.5,
    '2m'      :  19.5,
    '5.5m'    :  19.5,
    '11m'     :  19.5,
    '6m'      :  19.5,
    '9m'      :  19.5,
    '12m'     :  18,
    '18m'     :  18,
    '24m'     :  16.5,
    '36m'     :  16.5,
    '48m'     :  15,
    '54m'     :  14,
    'mcs0'    :  18,
    'mcs1'    :  18,
    'mcs2'    :  18,
    'mcs3'    :  16.5,
    'mcs4'    :  16.5,
    'mcs5'    :  15,
    'mcs6'    :  14,
    'mcs7'    :  13,
    'mcs0_40' :  18,
    'mcs1_40' :  18,
    'mcs2_40' :  18,
    'mcs3_40' :  16.5,
    'mcs4_40' :  16.5,
    'mcs5_40' :  15,
    'mcs6_40' :  14,
    'mcs7_40' :  13,
    'lr0'     :  19.5,
    'lr1'     :  19.5,
    'lr2'     :  19.5,
    'lr3'     :  19.5,
    'lr4'     :  19.5,
    'lr5'     :  19.5,
    'lr6'     :  14.5, # Cali
    'lr7'     :  14.5
}

rx_acpr_crt = {
    '11b' : [35],    #'11m','5.5m','2m','1m'
    '11m' : 35,
    '11g' : [-1,0,4,8,11,13,15,16],  #'54m','48m','36m','24m','18m','12m','9m','6m'
    '54m' : -1,
    '48m' : 0,
    '36m' : 4,
    '24m' : 8,
    '18m' : 11,
    '12m' : 13,
    '9m'  : 15,
    '6m'  : 16,
    '11n_20' : [-2,-1,0,4,8,11,13,16],  #'mcs7','mcs6','mcs5','mcs4','mcs3','mcs2','mcs1','mcs0'
    'mcs7' : -2,
    'mcs6' : -1,
    'mcs5' : 0,
    'mcs4' : 4,
    'mcs3' : 8,
    'mcs2' : 11,
    'mcs1' : 13,
    'mcs0' : 16,
    '11n_40' : [-2,-1,0,4,8,11,13,16],   #'mcs7_40','mcs6_40','mcs5_40','mcs4_40','mcs3_40','mcs2_40','mcs1_40','mcs0_40'
    'mcs7_40' : -2,
    'mcs6_40' : -1,
    'mcs5_40' : 0,
    'mcs4_40' : 4,
    'mcs3_40' : 8,
    'mcs2_40' : 11,
    'mcs1_40' : 13,
    'mcs0_40' : 16
}

rx_pwr_signal_vs_data_rate={
    "11m":-70,
    "6m":-79,
    "9m":-78,
    "12m":-76,
    "18m":-74,
    "24m":-71,
    "36m":-67,
    "48m":-63,
    "54m":-62,
    "mcs0":-79,
    "mcs1":-76,
    "mcs2":-74,
    "mcs3":-71,
    "mcs4":-67,
    "mcs5":-63,
    "mcs6":-62,
    "mcs7":-61,
    "mcs0_40":-76,
    "mcs1_40":-73,
    "mcs2_40":-71,
    "mcs3_40":-68,
    "mcs4_40":-64,
    "mcs5_40":-60,
    "mcs6_40":-59,
    "mcs7_40":-58
}

reg = dict()
reg['txpwr_ref'] = dict(txpwr_tx_scale=0) # absolute reference
for rate in ratedic:
    reg['txpwr_ref']['txpwr_dig_gain_'+rate] = 0

pbus_mode = 'work'
#--------------------------------------------------
# Testing Script Related (Chengzhou Wang, 2012/10/15)
#--------------------------------------------------
adc_dump = [0,0,0,0,'']
saradc = [0, 0, 0, 0, 0, 0]

#cable_loss = 0
cable_loss = 1

#  IQview = [pwr, evm, iqamp, iqphase, evm_wo_iq]
test_para = dict(preamble = ['sym_by_sym','raw_long','on','long_train','off'],
                 preamble_amptrack = ['sym_by_sym','raw_long','on','long_train','on'],
                 payload = ['sym_by_sym','raw_full','on','full_packet','off'],
                 payload_amptrack = ['sym_by_sym','raw_full','on','full_packet','on'])
#iqv_ip_addr = '192.168.100.8'
iqv_ip_addr = '192.168.100.210'
iqv = {
    "evm_sorted": 0,
    "pwr":      -99.9,
    "evm_raw":  -99.9,
    "evm_std":  -99.9,
    "evm_max":  -99.9,
    "iqamp":    -99.9,
    "iqphase":  -99.9,
    "evm_wo_iq":    -99.9,
    "lo_leakage":    -99.9,
    "freq_err":    -99.9,
    "clk_err":    -99.9,
    "evm_max":  -99.9,
    "pwr_bt":    "/",
    "Init_Freq_Err": "/",
    "deltaF1Avg": "/",
    "deltaF2Max": "/",
    "deltaF2Avg": "/",
    "pwr_le_pk": "/",
    "bandwidth20dB" :"/",
    "EdrExtremeOmegaI": "/",
    "EdrExtremeOmegaO": "/",
    "EdrExtremeOmegaIO": "/",
    "EdrEVMAv": "/",
    "EdrEVMpk": "/",
    "EdrprobEVM99pass":"/",
    "EdrEVMvalid":"/",
    "EdrPowDiffdB":"/",
    }
iqv_arg = {
    "rf_freq":      2452,
    "pwr":  -100,
    "data_rate":    '6m',
    "chan_est":  ['sym_by_sym','raw_full','on','full_packet','on'],
    "unit_no":    1,
    "mode":    'measure',
    "ex_att":    0.6,
    "auto_range":1
    }
#
txout_att_arg= {
    "rate_sym": '6m',
    "atten":    20,
    "PackNum":  0,
    "PackLen":  1024,
    "txchan":   'com',
    "mode":     'work',
    "pwr_ref":  'absolute'  # or "pwrcal"
    }
txout_pwctrl_arg= {
    "rate_sym": '6m',
    "PackNum":  0,
    "PackLen":  1024,
    "txchan":   'com'
    }
cal_txcap = {
    "TMX2G_CCT_LOAD":   0,
    "PA2G_CCT_STG2":    0,
    "PA2G_CCT_STG1":    0
    }
tos_dac = [256, 256, 256, 256]

file_folder = ''

test_rate_11b = ['1m','2ml','5.5ml','11ml','2ms','5.5ms','11ms']

test_rate_11g = ['6m','9m','12m','18m','24m','36m','48m','54m']

test_rate_11n_20 = ['mcs0','mcs1','mcs2','mcs3','mcs4','mcs5','mcs6','mcs7']

test_rate_11n_40 = ['mcs0_40','mcs1_40','mcs2_40','mcs3_40','mcs4_40','mcs5_40','mcs6_40','mcs7_40']

test_rate_all = ['1m','2ml','5.5ml','11ml','2ms','5.5ms','11ms',
          '6m','9m','12m','18m','24m','36m','48m','54m',
          'mcs0','mcs1','mcs2','mcs3','mcs4','mcs5','mcs6','mcs7',
          'mcs0_40','mcs1_40','mcs2_40','mcs3_40','mcs4_40','mcs5_40','mcs6_40','mcs7_40']

test_rate_comm = ['1m','11m','6m', '54m', 'mcs0', 'mcs7', 'mcs0_40', 'mcs7_40']

'''
rftest: 1, ac49865-dirty, Jan 14 2020, 15:17:08
CHIP_ID: 0x34724c3f, 0x18fe
param_flag: 0x1ff66f8
vdd33=3311, temp_code=0, offset=-1
rc_dout, 40; wifi: 36, 11, 0, 0, bt: 0, 0
cal_rf_ana_gain, rf_gain=0x5f, ana_gain=0x20
RX_NOISEFLOOR, -377
RX_NOISEFLOOR, -378
RX_NOISEFLOOR, -375
TXCAP_TMX2G_CCT_LOAD, 11, 9, 7, 7,
TXCAP_PA2G_CCT_STG1, 13, 11, 11, 11,
TXCAP_PA2G_CCT_STG2, 3, 3, 11, 11,
TX_POWER_BACKOFF, 0, 0, 0, 0,
TX_PWRCTRL_ATTEN, -9, -3, 1, 5, 9, 15, -8, -2, 2, 6, 10, 16, -10, -4, 0, 4, 8, 14, -10, -4, 0, 4, 8, 14,
TXIQ,-3, 1; -3, 2;
TXDC, 277, 245, 258, 257; 271, 249, 256, 256; 271, 248, 256, 257; 270, 249, 257, 255; 266, 249, 255, 257;
RXIQ, -6, -2; -6, -2; -5, -2; -4, -3;
RXDC_RFRX_WIFI, 280, 237; 280, 236; 280, 231; 280, 231; 280, 231; 280, 231; 280, 231; 279, 227; 279, 232; 279, 232; 279, 232; 276, 231;
273, 218; 273, 218; 273, 219; 272, 220; 272, 220; 272, 220; 272, 221; 272, 222; 271, 223; 271, 224; 271, 224; 272, 223; 272, 224; 272, 225;
RXDC_RXBB_WIFI, 278, 256;
TX_VDD33=3311
sar_dc_code=1388, sar_ref_code=2336

'''
init_print_dict = {
'rftest': range(0,6),
'CHIP_ID' : [0,1],
'param_flag': [0],
'vdd33': [0],
'temp_code' : [0],
'rc_dout': [0,2,3,4,5],
'rf_gain' : [0],
'ana_gain' : [0],
'RX_NOISEFLOOR' : [0,2,4],
'TXCAP_TMX2G_CCT_LOAD' : range(4),
'TXCAP_PA2G_CCT_STG1' : range(4),
'TXCAP_PA2G_CCT_STG2' : range(4),
'TX_POWER_BACKOFF' : range(4),
'TX_PWRCTRL_ATTEN' : range(24),
'TXIQ' : range(4),
'TXDC' : range(20),
'RXIQ' : range(8),
'RXDC_RFRX_WIFI' : range(52),
'RXDC_RXBB_WIFI' : range(2),
'sar_dc_code' : [0],
'sar_ref_code' : [0]
}



