import numpy as np
import pandas as pd
import time
import re
import csv
import os, sys
import matplotlib.pyplot as plt
import pylab
import xlrd

def get_data(path='', para1='atten', para2=0, para3='angle', para4='rx_retry_ratio'):
    df1 = pd.read_csv(path, index_col=False)
    df2 = df1.loc[df1['{}'.format(para1)].isin(['{}'.format(para2)])]
    data_axis = df2['{}'.format(para3)].tolist()
    data_colum = df2['{}'.format(para4)].tolist()
    plt.ion()
    plt.figure(100)
    plt.plot(data_axis, data_colum, linewidth=0.5, label='{}={}'.format(para1,para2))
    plt.xlabel('{}'.format(para3))
    plt.ylabel('{}'.format(para4))
    plt.legend()
    plt.grid()
    plt.show()



def get_data_rxretry(path='', para1='atten', para2_list=range(0,41,5), para3='angle', para4='rx_retry_ratio'):
    for i in para2_list:
        get_data(path=path, para1=para1, para2=i, para3=para3, para4=para4)



def reg_wrm(reg_addr,reg_value,msb,lsb,value):
    # reg_value = self.reg_rd(reg_addr)
    # reg_value = eval(reg_value.split(",")[1])
    mask = (1<<(msb+1))-(1<<lsb)
    result = (reg_value & ~mask) | ((value<<lsb) & mask)
    return hex(result)