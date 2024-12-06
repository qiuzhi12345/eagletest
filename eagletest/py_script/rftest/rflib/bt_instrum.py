import time
import math
import csv
import random
import numpy as np
from baselib.plot import mfunc
from baselib.instrument import *
from baselib.test_channel import *
import rftest.rflib.rfglobal as rfglobal
from baselib.loglib.log_lib import *


#************************BT PART**************************

drate2name = {
    1 : '1M',
    2 : '2M',
    3 : '3M'
}
name2drate = {
    '1M' : 1,
    '2M' : 2,
    '3M' : 3
}

LE_drate2name = {
    0 : '1M',
    1 : '2M',
    2 : '125K',
    3 : '500K'
}

LE_name2drate = {
    '1M' : 0,
    '2M' : 1,
    '125K' : 2,
    '500K' : 3
}


DH2name = {
    1 : 'DH1',
    3 : 'DH3',
    5 : 'DH5'
}

name2DH = {
    'DH1' : 1,
    'DH3' : 3,
    'DH5' : 5
}

dtype2name ={
    0 : '1010',
    1 : '00001111',
    2 : 'prbs9'
}

name2dtype ={
    '1010' : 0,
    '00001111' : 1,
    'prbs9': 2
}

def bt_rate_name(drate=1, DH=1, dtype=1):
    rate_name = drate2name[drate]+'_'+DH2name[DH]+'_'+dtype2name[dtype]
    logdebug(rate_name)
    return rate_name

def le_rate_name(drate=0,dtype=1):
    rate_name= 'LE_'+ LE_drate2name[drate]+'_'+ dtype2name[dtype]
    logdebug(rate_name)
    return rate_name

def name2rate(rate_name):
    name_lst = rate_name.split('_')
    if name_lst[0] =='LE':
        LE_flag = 1
        drate = LE_name2drate[name_lst[1]]
        DH = 'none'
        dtype = name2dtype[name_lst[2]]
    else:
        LE_flag = 0
        drate = name2drate[name_lst[0]]
        DH = name2DH[name_lst[1]]
        dtype = name2dtype[name_lst[2]]
    logdebug(LE_flag,drate,DH,dtype)
    return [LE_flag,drate,DH,dtype]

def le_chan2freq(freq):
    chan=(freq-2402)/2
    if chan==0:
        fi=37
    elif chan==12:
        fi=38
    elif chan==39:
        fi=39
    elif chan<=11:
        fi=chan-1
    elif chan<=38:
        fi=chan-2
    return fi

def iqv_bt_avg(rate_name,myiqv,capture_times=10):

    pwr_lst = []; deltaF1Avg_lst = []; deltaF2Max_lst = []; deltaF2Avg_lst = []; EdrEVMAv_lst =[]; EdrEVMpk_lst = [];
    Init_Freq_Err_lst = []; EdrExtremeOmegaI_lst =[];EdrExtremeOmegaO_lst =[];EdrExtremeOmegaIO_lst =[];bandwidth20dB_lst=[];
    maxPowerAcpDbm_lst =[]; maxPowerEdrDbm_lst = [];EdrprobEVM99pass_lst =[];pwr_le_pk_lst =[];EdrEVMvalid_lst=[];EdrPowDiffdB_lst=[]
    rate_dtype_dic = {
    '1M_DH1_1010':'BR_1010',
    '1M_DH3_1010':'BR_1010',
    '1M_DH5_1010':'BR_1010',
    '1M_DH1_00001111':'BR_00001111',
    '1M_DH3_00001111':'BR_00001111',
    '1M_DH5_00001111':'BR_00001111',
    '1M_DH1_prbs9':'BR_prbs9',
    '1M_DH3_prbs9':'BR_prbs9',
    '1M_DH5_prbs9':'BR_prbs9',
    '2M_DH1_1010':'EDR',
    '2M_DH3_1010':'EDR',
    '2M_DH5_1010':'EDR',
    '2M_DH1_00001111':'EDR',
    '2M_DH3_00001111':'EDR',
    '2M_DH5_00001111':'EDR',
    '2M_DH1_prbs9':'EDR',
    '2M_DH3_prbs9':'EDR',
    '2M_DH5_prbs9':'EDR',
    '3M_DH1_1010':'EDR',
    '3M_DH3_1010':'EDR',
    '3M_DH5_1010':'EDR',
    '3M_DH1_00001111':'EDR',
    '3M_DH3_00001111':'EDR',
    '3M_DH5_00001111':'EDR',
    '3M_DH1_prbs9':'EDR',
    '3M_DH3_prbs9':'EDR',
    '3M_DH5_prbs9':'EDR',
    'LE_1M_1010':'LE_1010',
    'LE_1M_00001111':'LE_00001111',
    'LE_1M_prbs9':'LE_prbs9',
    'LE_2M_1010':'LE_1010',
    'LE_2M_00001111':'LE_00001111',
    'LE_2M_prbs9':'LE_prbs9',
    'LE_125K_1010':'LE_Coded',
    'LE_125K_00001111':'LE_Coded',
    'LE_125K_prbs9':'LE_Coded',
    'LE_500K_1010':'LE_Coded',
    'LE_500K_00001111':'LE_Coded',
    'LE_500K_prbs9':'LE_Coded',
    }
    print_en=1
    iq_id=sock.get_IQ_ID()  # used to identify which instrument is connected
    loginfo("iqv_avg,IQ_ID=%s"%iq_id)
    for i in range(0,capture_times):
        myiqv.restart(5000,0,1,150)
        if iq_id == 3: # IQVIEW
            pwr = myiqv.get_result('P_av_each_burst')
        else:
            pwr = myiqv.get_result('P_av_each_burst_dBm')
        pwr_lst.append(pwr)
        if rate_dtype_dic[rate_name] == 'BR_1010':
            Init_Freq_Err_lst.append(float(myiqv.get_result('freq_est'))/1000)
            deltaF2Max_lst.append(float(myiqv.get_result('deltaF2Max'))/1000)
            deltaF2Avg_lst.append(float(myiqv.get_result('deltaF2Average'))/1000)
            bandwidth20dB_lst.append(float(myiqv.get_result('bandwidth20dB'))/1000);

        elif rate_dtype_dic[rate_name] == 'BR_00001111' :
            Init_Freq_Err_lst.append(float(myiqv.get_result('freq_est'))/1000);
            deltaF1Avg_lst.append(float(myiqv.get_result('deltaF1Average'))/1000)
            bandwidth20dB_lst.append(float(myiqv.get_result('bandwidth20dB'))/1000);

        elif rate_dtype_dic[rate_name] == 'BR_prbs9':
            Init_Freq_Err_lst.append(float(myiqv.get_result('freq_est'))/1000);
            bandwidth20dB_lst.append(float(myiqv.get_result('bandwidth20dB'))/1000);
        #******BLE********
        elif rate_dtype_dic[rate_name] == 'LE_1010':
            pwr_le_pk_lst.append(myiqv.get_result('P_pk_each_burst_dBm'))
            Init_Freq_Err_lst.append(float(myiqv.get_result('freq_est'))/1000);
            deltaF2Max_lst.append(float(myiqv.get_result('deltaF2Max'))/1000);
            deltaF2Avg_lst.append(float(myiqv.get_result('deltaF2Average'))/1000);


        elif rate_dtype_dic[rate_name] == 'LE_00001111' :
            pwr_le_pk_lst.append(myiqv.get_result('P_pk_each_burst_dBm'))
            Init_Freq_Err_lst.append(float(myiqv.get_result('freq_est'))/1000);
            deltaF1Avg_lst.append(float(myiqv.get_result('deltaF1Average'))/1000)

        elif rate_dtype_dic[rate_name] == 'LE_prbs9' or rate_dtype_dic[rate_name] == 'LE_Coded':
            pwr_le_pk_lst.append(myiqv.get_result('P_pk_each_burst_dBm'))
            Init_Freq_Err_lst.append(float(myiqv.get_result('freq_est'))/1000);

        #******EDR********
        elif rate_dtype_dic[rate_name] == 'EDR':
            Init_Freq_Err_lst.append(float(myiqv.get_result('freq_est'))/1000);
            EdrExtremeOmegaI_lst.append(float(myiqv.get_result('EdrOmegaI'))/1000)
            EdrExtremeOmegaO_lst.append(float(myiqv.get_result('EdrExtremeOmega0'))/1000)
            EdrExtremeOmegaIO_lst.append(float(myiqv.get_result('EdrExtremeOmegaI0'))/1000)

            if iq_id == 1 or iq_id == 3 : # IQxel
                EdrEVMAv_lst.append(float(myiqv.get_result('EdrEVMAv'))*100);
                EdrEVMpk_lst.append(float(myiqv.get_result('EdrEVMpk'))*100);
                EdrprobEVM99pass_lst.append(float(myiqv.get_result('EdrprobEVM99pass')))
            elif iq_id == 2: # wt200
                EdrEVMAv_lst.append(float(myiqv.get_result('EdrEVMAv')));
                EdrEVMpk_lst.append(float(myiqv.get_result('EdrEVMpk')));
                EdrprobEVM99pass_lst.append(float(myiqv.get_result('EdrprobEVM99pass'))/100)

            EdrEVMvalid_lst.append(float(myiqv.get_result('EdrEVMvalid')))
            EdrPowDiffdB_lst.append(float(myiqv.get_result('EdrPowDiffdB')))

    if iq_id == 3: # IQVIEW
        pwr_avg0 = mfunc.avg_dB10(pwr_lst)
        pwr_avg = 10*np.log10(pwr_avg0)
    else:
        pwr_avg = mfunc.avg_dB10(pwr_lst)

    rfglobal.iqv["pwr_bt"]  = pwr_avg
    #******1M********
    if rate_dtype_dic[rate_name] == 'BR_1010':

        rfglobal.iqv["Init_Freq_Err"] = np.average(Init_Freq_Err_lst)
        rfglobal.iqv["deltaF2Max"] = np.average(deltaF2Max_lst)
        rfglobal.iqv["deltaF2Avg"] = np.average(deltaF2Avg_lst)
        rfglobal.iqv["bandwidth20dB"] = np.average(bandwidth20dB_lst)
        iqv=rfglobal.iqv
        tx_result=[iqv['pwr_bt'],iqv['Init_Freq_Err'],'/',iqv['deltaF2Max'],iqv['deltaF2Avg'],'/','/','/','/','/','/','/','/','/']

    elif rate_dtype_dic[rate_name] == 'BR_00001111' :

        rfglobal.iqv["Init_Freq_Err"]  = np.average(Init_Freq_Err_lst)
        rfglobal.iqv["deltaF1Avg"] = np.average(deltaF1Avg_lst)
        rfglobal.iqv['bandwidth20dB'] = np.average(bandwidth20dB_lst)
        iqv=rfglobal.iqv
        tx_result=[iqv['pwr_bt'],iqv['Init_Freq_Err'],iqv['deltaF1Avg'],'/','/','/','/','/','/','/','/','/','/','/']

    elif rate_dtype_dic[rate_name] == 'BR_prbs9' :

        Init_Freq_Err_avg = np.average(Init_Freq_Err_lst)
        bandwidth20dB_avg = np.average(bandwidth20dB_lst)
        rfglobal.iqv["Init_Freq_Err"] = Init_Freq_Err_avg
        rfglobal.iqv["bandwidth20dB"] = bandwidth20dB_avg
        iqv=rfglobal.iqv
        tx_result=[iqv['pwr_bt'],iqv['Init_Freq_Err'],'/','/','/',iqv['bandwidth20dB'],'/','/','/','/','/','/','/','/']

    #******LE********
    elif rate_dtype_dic[rate_name] == 'LE_1010':

        rfglobal.iqv["Init_Freq_Err"] = np.average(Init_Freq_Err_lst)
        rfglobal.iqv["deltaF2Max"] = np.average(deltaF2Max_lst)
        rfglobal.iqv["deltaF2Avg"] = np.average(deltaF2Avg_lst)
        rfglobal.iqv["pwr_le_pk"]  = mfunc.avg_dB10(pwr_le_pk_lst)
        iqv = rfglobal.iqv
        tx_result =[iqv['pwr_bt'],iqv['Init_Freq_Err'],'/',iqv['deltaF2Max'],iqv['deltaF2Avg'],iqv['pwr_le_pk']]

    elif rate_dtype_dic[rate_name] == 'LE_00001111' :

        rfglobal.iqv["Init_Freq_Err"] = np.average(Init_Freq_Err_lst)
        rfglobal.iqv["deltaF1Avg"] = np.average(deltaF1Avg_lst)
        rfglobal.iqv["pwr_le_pk"] = mfunc.avg_dB10(pwr_le_pk_lst)
        iqv = rfglobal.iqv
        tx_result =[iqv['pwr_bt'],iqv['Init_Freq_Err'],rfglobal.iqv["deltaF1Avg"],'/','/',iqv['pwr_le_pk']]

    elif rate_dtype_dic[rate_name] == 'LE_prbs9' or rate_dtype_dic[rate_name] == 'LE_Coded' :

        rfglobal.iqv["Init_Freq_Err"]= np.average(Init_Freq_Err_lst)
        rfglobal.iqv["pwr_le_pk"]  = mfunc.avg_dB10(pwr_le_pk_lst)
        iqv = rfglobal.iqv
        tx_result =[iqv['pwr_bt'],iqv['Init_Freq_Err'],'/','/','/',iqv['pwr_le_pk']]

    #******EDR********
    elif rate_dtype_dic[rate_name] == 'EDR':
        rfglobal.iqv["Init_Freq_Err"] = np.average(Init_Freq_Err_lst)
        rfglobal.iqv["EdrExtremeOmegaI"] = np.average(EdrExtremeOmegaI_lst)
        rfglobal.iqv["EdrExtremeOmegaO"] = np.average(EdrExtremeOmegaO_lst)
        rfglobal.iqv["EdrExtremeOmegaIO"] = np.average(EdrExtremeOmegaIO_lst)
        rfglobal.iqv["EdrEVMAv"] = np.average(EdrEVMAv_lst)
        rfglobal.iqv["EdrEVMpk"] = np.average(EdrEVMpk_lst)
        rfglobal.iqv["EdrprobEVM99pass"] = np.average(EdrprobEVM99pass_lst)
        rfglobal.iqv["EdrEVMvalid"] =np.average(EdrEVMvalid_lst)
        rfglobal.iqv["EdrPowDiffdB"]= mfunc.avg_dB10(EdrPowDiffdB_lst)
        rfglobal.iqv["EdrprobEVM99pass"] = np.average(EdrprobEVM99pass_lst)
        iqv = rfglobal.iqv
        tx_result=[iqv['pwr_bt'],iqv['Init_Freq_Err'],'/','/','/','/',iqv['EdrExtremeOmegaI'],iqv['EdrExtremeOmegaO'],iqv['EdrExtremeOmegaIO'],iqv['EdrEVMAv'],iqv['EdrEVMpk'],iqv['EdrprobEVM99pass'],iqv['EdrEVMvalid'],iqv['EdrPowDiffdB']]

    return [tx_result]

def max_Power_Acp(myiqv, capture_times=10):
    '''
    :return the value of max power adjancent channel power!

    '''
    maxPowerAcpDbm_lst=[]
    maxPowerAcpFreqHz_lst=[]
    maxPowerAcpFreqHz_max=[]
    iq_id=sock.get_IQ_ID()  # used to identify what instrument to connect
    loginfo("IQ_ID=%s"%iq_id)
    for i in range(0,capture_times):
        myiqv.restart(5000,0,1,150)

        maxPowerAcpFreqHz = myiqv.get_vect_result('maxPowerAcpFreqHz')
        maxPowerAcpDbm = myiqv.get_vect_result('maxPowerAcpDbm');
        maxPowerAcpDbm_lst.append(maxPowerAcpDbm)
        maxPowerAcpFreqHz_lst.append(maxPowerAcpFreqHz)
        print maxPowerAcpDbm_lst

    maxPowerAcpDbm_max=np.array(maxPowerAcpDbm_lst,dtype=float).min(axis=0)
    n=np.argwhere(maxPowerAcpDbm_lst==maxPowerAcpDbm_max)
    _n=n[np.lexsort(n.T)]
    m=_n.tolist()
    for i in range(len(m)):
        maxPowerAcpFreqHz_max.append(np.array(maxPowerAcpFreqHz_lst,dtype=float)[m[i][0],m[i][1]]/1e6)

    maxPowerAcpDbm_lst = maxPowerAcpDbm_max.tolist()
    maxPowerAcpFreqHz_lst = maxPowerAcpFreqHz_max

    return [maxPowerAcpFreqHz_lst,maxPowerAcpDbm_lst]
