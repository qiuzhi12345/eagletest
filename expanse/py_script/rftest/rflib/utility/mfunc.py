# -*- coding: utf-8 -*-
import numpy as np
import re, copy
from Tkinter import *

def intersect(a, b):
     return list(set(a) & set(b))
 
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

def transpose(x):
    if isinstance(x, list):
        return map(list, zip(*x))
    elif isinstance(x, tuple):
        return zip(*x)

def index(C, D):
    k = []
    for item in D:
        k.append(C.index(item))
    return k

def indexreg(L, regexp):
    return [i for (i, x) in enumerate(L) if re.search(regexp, x)]

def listreg(L, regexp):
    return [x for (i, x) in enumerate(L) if re.search(regexp, x)]
    
    
def strcat(char, C):
    if isinstance(C, str):
        return char+C
    elif isinstance(C, (list, tuple, np.ndarray)):
        return map(lambda x: char+x, C)

def interp(x, xp, fp):
    i = np.argsort(xp)
    return np.interp(x, xp[i], fp[i])

def col(x, idx):
    return [row[idx] for row in x]

def str2cellstr(C, delimiter=r'[\s;]+', filter_empty=True):
    if isinstance(delimiter, list):
        for dlm in delimiter:
            C = str2cellstr(C, dlm, filter_empty)
    elif isinstance(delimiter, str):
        if isinstance(C, list):
            C = [str2cellstr(x, delimiter, filter_empty) for x in C]
        elif isinstance(C, str):
            C = re.split(delimiter, C)
            if filter_empty:
                C = filter(None, C)
    return C
    
def unique_no_sort(seq): 
   # order preserving
   x = []
   [x.append(i) for i in seq if not x.count(i)]
   return x

def dec2hex(n):
    """return the hexadecimal string representation of integer n"""
    return "%X" % n
def hex2dec(s):
    """return the integer value of a hexadecimal string s"""
    return int(s, 16)

def hex2bin(s):
    s = re.sub('^0x', '', s)
    bin = ['0000','0001','0010','0011',
        '0100','0101','0110','0111',
        '1000','1001','1010','1011',
        '1100','1101','1110','1111']
    aa = ''
    for i in range(len(s)):
        aa += bin[hex2dec(s[i])]
    return aa
 
def bin2hex(binstring):
    return "0x%x" % int(binstring, 2)


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

def str2num(s, ftype=None):
    '''convert a str(list) to a numeric(list)
    '''
    if isinstance(s, (list, tuple)):
        s = map(lambda x:str2num(x, ftype), s)
    else:
        if isinstance(s, str):
            if s=='None':
                s = None
            else:
                if ftype in (int, float):
                    if isnum(s, ftype):
                        s = ftype(s)
                elif ftype == None:
                    if isnum(s, int):
                        s = str2num(s, int)
                    elif isnum(s, float):
                        s = str2num(s, float)
                    else:
                        pass
        elif isinstance(s, (int, float)):
            pass
        else:
            print "error: input has to be a string"
    return s
    
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
            ftype(s)
            return True
        except ValueError:
            return False

from numpy import where, dstack, diff, meshgrid

def find_intersections(A, B):

    # min, max and all for arrays
    amin = lambda x1, x2: where(x1<x2, x1, x2)
    amax = lambda x1, x2: where(x1>x2, x1, x2)
    aall = lambda abools: dstack(abools).all(axis=2)
    slope = lambda line: (lambda d: d[:,1]/d[:,0])(diff(line, axis=0))

    x11, x21 = meshgrid(A[:-1, 0], B[:-1, 0])
    x12, x22 = meshgrid(A[1:, 0], B[1:, 0])
    y11, y21 = meshgrid(A[:-1, 1], B[:-1, 1])
    y12, y22 = meshgrid(A[1:, 1], B[1:, 1])

    m1, m2 = meshgrid(slope(A), slope(B))
    m1inv, m2inv = 1/m1, 1/m2

    yi = (m1*(x21-x11-m2inv*y21) + y11)/(1 - m1*m2inv)
    xi = (yi - y21)*m2inv + x21

    xconds = (amin(x11, x12) < xi, xi <= amax(x11, x12), 
              amin(x21, x22) < xi, xi <= amax(x21, x22) )
    yconds = (amin(y11, y12) < yi, yi <= amax(y11, y12),
              amin(y21, y22) < yi, yi <= amax(y21, y22) )

    return xi[aall(xconds)], yi[aall(yconds)]

# PROJECT RELATED FUNCTIONS
def saradc2pwr(D, offset=20, cal=True, output='', algorithm='czwang'):
    if isinstance(D, str):
        D = str2num(str2cellstr(D, ['\|', '-']), float)
        if cal:
            D = saradc_cal(D, algorithm)
        D = np.array(D)
        P = []
        vref_list = []
        vsig_list = []
        for m in range(D.shape[0]):
            vdc = np.mean(D[m, [0, -2, -1]])
            vsig = np.mean(D[m, 1:3])
            vref = np.mean(D[m, 4:6])
            P.append((vsig-vdc)/(vref-vdc))
            vref_list.append(vref-vdc) 
            vsig_list.append(vsig-vdc) 
#         print 10*np.log10(P)+offset
        if output == 'vref':
            return np.mean(vref_list)
        elif output == 'vsig':
            return np.mean(vsig_list)
        elif output == 'vratio':
            return np.mean(vsig_list)/np.mean(vref_list)
        else:
            return 10*np.log10(np.mean(P))+offset
    
def saradc_cal(D, algorithm='czwang'):
    if isinstance(D, list):
        D = [saradc_cal(x, algorithm) for x in D]  
    else:
        if algorithm == 'czwang':
            D = D - (int(D)/256)*27
        elif algorithm == 'cff':
            D = int(D)
            temp = (( D & 0xff)- 21);
            if (temp < 0): temp = 0;
            temp = (temp * 279) >> 8;  # temp * 255/(255-21)
            if (temp > 255): temp = 255;
            D = (D & 0xf00) + temp;
 
#         if D >= 1280:
#             D = D - 24
#         if D >= 1024:
#             D = D - 24
#         if D >= 768:
#             D = D - 30
#         if D >= 512:
#             D = D - 26
#         if D >= 256:
#             D = D - 28
    return D
         
def tovector(D):
    keys = D.keys()
    X = []
    print D[keys[0]]
    for i in range(len(D[keys[0]])):
        T = copy.deepcopy(D)
        print i
        for key in T:
            T[key] = T[key][i]
        X.append(T)
    return X        
    
