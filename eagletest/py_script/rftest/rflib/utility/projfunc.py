#!/usr/bin/env python
#test function for chip_v4.0

import csv
import re
import sys
import numpy as np
import mfunc as mf
from pylab import *
from iofunc import *
import copy
import figfunc

def rxagc():
    infile = 'C:/Users/Chengzhou/Dropbox/Chengzhou/Work/Espressif/Group_doc/AgcGainScan_20121023_pbus_setting.csv'
    outfile = 'C:/Users/Chengzhou/Dropbox/Chengzhou/Work/Espressif/Group_doc/AgcGainScan_20121023_pbus_setting_czwang.csv'
    L = csv2data(infile, comment='#')
    L[0] = [L[0][0]]+['sw_h', 'sw_l','lna', 'vga_h', 'vga_l', 'lpf[7:1]', 'lpf', 'lpf_fine[2:0]'] +L[0][1:]
    for i in range(1,len(L)):
        r = mf.hex2bin(L[i][0])
        L[i] = [L[i][0]]+[r[1], r[2], r[3], r[4], r[5], r[6:13], str(r[6:13].count('1')), r[13:]]+L[i][1:]
    data2csv(outfile, L)

def fom(runset = None):
    """ calculate FOM for different matching  """
    
    L = csv2data('../common/datalist/datalist_FOM.csv', comment='#')
    F = []; 
    F.append(figfunc.fig())
    F[0].labelx = 'Pout (dBm)'
    F[0].labely = 'FOM'
    F.append(copy.copy(F[0]))
    w = [1, 5]
    dic = dict()
    k = mf.index(L[0], ['runset', 'xval'])
    L = np.array(L)
    idx = np.where(L[:, k[0]] == runset)[0]
    D = L[idx, :]
##    print D, k
    [xval, yval1, yval2] = map(eval, D[0, k[1]:])
##    print xval, yval1
    x = zeros([len(xval), len(idx), 3])
    y1, y2, FOM = copy.copy(x), copy.copy(x), copy.copy(x)
    for i in range(len(idx)):
        for j in range(len(L[0, :])):
            dic[L[0, j]] = D[i, j]
##            print dic
        f1 = figfunc.plotATE(0, dic['sheet1'], runset = dic['set'], FID = dic['ID'])
        f2 = figfunc.plotATE(0, dic['sheet2'], runset = dic['set'], FID = dic['ID'])
        X1, Y1 = f1.X[:, :, 0], f1.Y[:, :, 0]
        X2, Y2 = f2.X[:, :, 0], f2.Y[:, :, 0]
        for p in range(size(X1, 1)):
            x[:, i, p]  = xval
            y1[:, i, p] = mf.interp(xval, X1[:, p], Y1[:, p])
            y2[:, i, p] = mf.interp(xval, X2[:, 0], Y2[:, 0])
            FOM[:, i, p] = w[1]*mf.dB10(yval2/y2[:, i, p]) + w[0]*(yval1 - y1[:, i, p] )
        F[0].legends.append(copy.copy(f1.ID))
        print f1.ID
    F[1].legends = F[0].legends
    F[0].X, F[0].Y = np.dstack((x, x[:, :, 0])), np.dstack((y1, y2[:, :, 0]))
    F[1].X, F[1].Y = x, FOM
    F[0].subtitle = ['2412', '2454', '2484', 'Idc']
    F[1].subtitle = ['2412', '2454', '2484']
    for i in range(2):
        figure(i)
        figfunc.mplot(F[i])

    return F
            
##            FOM = w[1]*mf.dB10(float(dic['y2'])/Y2) + w[0]*(float(dic['y1']) - Y1 )
##            print "15 dBm EVM = %3.2f, Idc = %3.2f, fom(%s) = %3.2f"%(Y1, Y2, dic['ID'], FOM)

def tx_rate_control():
    """ Tx rate control algorithm  """

    rate_SNR_dict = {0: 10,
                1: 15,
                2: 18,
                3: 20,
                4: 22,
                5: 25,
                6: 28}
                
    rate_idx = 6
    rate = []; rate_SNR = []
    retry_threshold = [0.1, 0.2]
    credit_threshold = [-2, 8]
    SNR_packet = np.random.rand(1, 10)*20+10
    SNR_packet = []
    for m in range(10):
        x = np.random.rand();
##        x=7/20.0
        for n in range(10):
            SNR_packet.append(x*20+10)
##    print SNR_packet
    SNR = np.hstack((np.ones((10,10))*29, np.ones((10,10))*29))
    for j in range(len(SNR_packet)):
        credit = 0
        rate.append(rate_idx)
        rate_SNR.append(rate_SNR_dict[rate_idx])
        for i in range(10):
            retry = SNR2retry(SNR_packet[j], rate_SNR_dict[rate_idx])
##            print retry
            if retry > retry_threshold[1]:
                credit -= (retry - 0.1)/0.1
            elif retry >= retry_threshold[0] and retry <= retry_threshold[1]:
                pass    # keep current rate
            else:
                credit += 1
##        print credit
        if credit < credit_threshold[0] and rate_idx > min(rate_SNR_dict.keys()):
            rate_idx -= int(abs(credit)/40)+1
        elif credit >credit_threshold[1] and rate_idx < max(rate_SNR_dict.keys()):
            rate_idx += 1
        if rate_idx < min(rate_SNR_dict.keys()):
            rate_idx = min(rate_SNR_dict.keys())    
##    print rate
    clf()
    x = range(len(SNR_packet))
    plot(x, SNR_packet, 'b-o', x, rate, 'm-x', x, rate_SNR, 'r-*')
    legend(['SNR_packet', 'tx_rate', 'tx_rate_SNR'])
    ylabel('SNR(dB)')
    xlabel('number of packets')

def SNR2retry(SNR, SNR_rate_idx):
    sig_quality = SNR - SNR_rate_idx
    retry = (-sig_quality +1)* 0.1  # -9 dB = 100%, 1 dB = 0
    if retry < 0:
        retry = 0
    elif retry > 1:
        retry = 1
    return retry
        
    
