# -*- coding: utf-8 -*-
import numpy as np

def std_dB10(dB_list):
    x = np.array(dB_list, dtype=np.float);
    evm_std = np.std(x)
    return evm_std

def max_dB10(dB_list):
    x = np.array(dB_list, dtype=np.float);
    max_d = np.max(x)
    return max_d

def min_dB10(dB_list):
    x = np.array(dB_list, dtype=np.float);
    min_d = np.min(x)
    return min_d

def avg_dB10(dB_list):
    x = np.array(dB_list, dtype=np.float);
    avg_dB = 10*np.log10(np.average(10**(x/10)))
    return avg_dB

def avg_dB20(dB_list):
    x = np.array(dB_list, dtype=np.float);
    avg_dB = 20*np.log10(np.average(10**(x/20)))
    return avg_dB

def dB10(x_list):
    x = np.array(x_list, dtype=np.float);
    dB = 10*np.log10(x)
    return dB
def dB10inv(dB_list):
    dB = np.array(dB_list, dtype=np.float);
    x = 10**(dB/10)
    return x

def isvalid(v, vrange, vstr = ''):
    ''' judge whether vmeas is in vrange([vmin, vmax]) '''
    [vmin, vmax] = [min(vrange), max(vrange)]
    if (v < vmin) or (v > vmax):
        if vstr:
            print "----- fail: %s = %g is out of [%g, %g]" %(vstr, v, vmin, vmax)
        return False
    else :
        if vstr:
            print "----- pass: %s = %g is within [%g, %g]" %(vstr, v, vmin, vmax)
        return True

def isnum(s, ftype):
    '''return whether a str (list) is numeric
        e.g. isnum(['1', '2'], int) # check integer
        e.g. isnum(['1', '2'], float) # check float
    '''

    if isinstance(s, list) or isinstance(s, tuple):
        tf = True
        for si in s:
            tf = tf and isnum(si, ftype)
        return tf
    elif isinstance(s, str):
        try:
            int(s)
            return True
        except ValueError:
            return False
