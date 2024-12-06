import time
import re
import csv
import os, sys
import matplotlib.pyplot as plt
import pylab
import numpy as np


esp8266_sleep_param = [
'param_flag',
'txdc',
'chan_backoff',
'txiq',
'rxiq',
'txcap',
'rx_dcap',
'tx_dcap',
'rx_noise',
'channel',
'atten_max_ofdm',
'target_power',
'pwctrl_atten',
'loop_pwdet_error',
'fcc_en',
'dpd_att',
'vdd33',
'rxdc']

esp8266_sleep_param_dict = {
'param_flag' : ['u32', 1],
'txdc' : ['u16', 4],
'chan_backoff' : ['s16', 4],
'txiq' : ['u16', 1],
'rxiq' : ['u16', 5],
'txcap' : ['u8', 12],
'rx_dcap':['u8', 1],
'tx_dcap':['u8', 1],
'rx_noise':['s16', 1],
'channel':['u8', 1],
'atten_max_ofdm':['u8',1],
'target_power':['u8', 6],
'pwctrl_atten':['s8',24],
'loop_pwdet_error':['s16', 1],
'fcc_en':['u8', 1],
'dpd_att':['s8', 1],
'vdd33':['u32', 1],
'rxdc':['u32', 60]
}

esp8266_rx_table = {
'rx_gain':['u32', 64],
'rxdc':['u32', 64]
}


def get_type_data(u8_data,type_in='u32', index=0):
    if type_in[1:] == '32':
        data_out = 0
        for i in range(0,4):
            data_out += u8_data[index+i]<<(i*8)
        if type_in == 's32':
            if data_out >= (1<<31):
                data_out -= (1<<32)
        index += 4
    elif type_in[1:] == '16':
        data_out = 0
        for i in range(0,2):
            data_out += u8_data[index+i]<<(i*8)
        if type_in == 's16':
            if data_out >= (1<<15):
                data_out -= (1<<16)
        index += 2
    elif type_in[1:] == '8':
        data_out = u8_data[index]
        if type_in == 's8':
            if data_out >= (1<<7):
                data_out -= (1<<8)
        index += 1
    else:
        print 'error'
        data_out = 0
        index = 0
    return [data_out, index]

def esp8266_print(param, data_in):
    if param == 'param_flag':
        print '%s, 0x%x'%(param, data_in[0])
    elif param == 'txdc':
        data_s = ''
        for data in data_in:
            data_s += '%d,%d,'%(data&0xff, data>>8)
        print '%s, %s'%(param, data_s)
    elif param == 'rxdc':
        data_s = ''
        for data in data_in:
            data_s += '%d,%d,'%(data&0x1ff, data>>9)
        print '%s, %s'%(param, data_s)
    elif param=='chan_backoff':
        data_s = ''
        for data in data_in:
            data_s += '%d,'%(data)
        print '%s, %s'%(param, data_s)
    elif param=='txiq':
        data_s = ''
        for data in data_in:
            data_i = data&0xff
            if data_i >= 32:
                data_i -= 64
            data_q = data>>8
            if data_i >= 16:
                data_i -= 32
            data_s += '%d,%d,'%(data_i, data_q)
        print '%s, %s'%(param, data_s)
    elif param=='rxiq':
        data_s = ''
        for data in data_in:
            data_i = data&0x3f
            if data_i >= 32:
                data_i -= 64
            data_q = data>>6
            if data_i >= 16:
                data_i -= 32
            data_s += '%d,%d,'%(data_i, data_q)
        print '%s, %s'%(param, data_s)
    elif param=='txcap' or param=='target_power' or param=='pwctrl_atten':
        data_s = ''
        for data in data_in:
            data_s += '%d,'%(data)
        print '%s, %s'%(param, data_s)
    elif param=='vdd33':
        print '%s, %d'%(param, data_in[0]>>16)
    else:
        print "%s, %d"%(param, data_in[0])

def esp8266_rfcal_data_check(bin_name='esp_init_data.bin'):
    f = open(bin_name, 'rb')
    bin_data = []
    for i in range(0, 0xfb300):
        s = f.read(1)
        if i >= 0xfb000:
            byte = ord(s)
##            print '%d, %x'%(i, byte)
            bin_data.append(byte)

    index = 0
    for sleep_param in esp8266_sleep_param:
        if sleep_param == 'rxdc':
            index = 0x180
        [type_in, num] = esp8266_sleep_param_dict[sleep_param]
        data_m = []
        for i in range(0,num):
            [data_out, index] = get_type_data(bin_data,type_in, index)
            data_m.append(data_out)
        esp8266_print(sleep_param, data_m)


def get_folder_file(source=''):
    _dir=os.path.abspath(source)
    tlist=os.listdir(_dir)
    all_file = []
    for i in range (len(tlist)):
        tname = tlist[i]
        fpath = source+'/'+tname
        all_file.append(fpath)
    return all_file

def check_all_bin(folder='./flash_dump_data'):
    all_file = get_folder_file(folder)
    i = 0
    for file_in in all_file:
        print '\n%d\n%s'%(i, file_in)
        esp8266_rfcal_data_check(bin_name=file_in)
        i += 1


if __name__=='__main__':

    check_all_bin()






