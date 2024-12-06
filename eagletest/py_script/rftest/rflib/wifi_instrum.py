import time
import math
import csv
import random
import serial
import numpy as np
from baselib.plot import mfunc
from baselib.instrument import *
from baselib.instrument import tester
from baselib.test_channel import *
import rftest.rflib.rfglobal as rfglobal
from baselib.loglib.log_lib import *
rfglobal.iqv_arg['auto_range']=0

def iqv_set_arg(arg_name, arg_value):
    arg = rfglobal.iqv_arg
    arg[arg_name] = arg_value;
    myiqv=tester.tester(arg["rf_freq"], arg["pwr"],
                        arg["data_rate"], arg["chan_est"],
                        arg["unit_no"], arg["mode"], arg["ex_att"],arg["auto_range"])
    return myiqv


def iqv_avg(myiqv,capture_times,read_spmask='false', evm_max_in=0,SampleTime_us=5000):
    ''' return sequence: evm,pwr'''
    evm_lst = []; pwr_lst = []; iq_amp = []; iq_phase = []; d_str=''
    iq_lo = []; freqerr_lst = []; clkerr_lst = [];
    n30M = []; n20M = []; n10M = [];
    p10M = []; p20M = []; p30M = [];x=[];
    pwrramp_up = []; pwrramp_down=[];
##    evm_max = -99.9
##    evm_min = 0
    iq_mode = myiqv.get_iq_mode()
    logdebug("iq_mode:%s"%iq_mode)
    auto_range=rfglobal.iqv_arg['auto_range']
    if iq_mode in ['11n_40']:
		ht40mode=1;
    else:
		ht40mode=0;
    for i in range(0,capture_times):
##		print"auto_range1=%d"%auto_range
		myiqv.restart(SampleTime_us,ht40mode,auto_range,20);
		evm = myiqv.get_result('EVM_ALL');
		pwr = myiqv.get_result('BUR_PWR');
		lo_offset =myiqv.get_result('IQ_OFF');
		amp_err_dB = float(myiqv.get_result('GAIN_IMB'));
		phase_err =  float(myiqv.get_result('QUADERR'));
		freq_err = float(myiqv.get_result('FREQ_ERR'));
		clk_err = float(myiqv.get_result('CLK_ERR'));
##                data_rate = myiqv.get_result('DATA_RATE');
##                psdu_crc = myiqv.get_result('PSDU_CRC');
##                psdu_len = myiqv.get_result('PSDU_LEN');
		freqerr_lst.append(float(freq_err)/1000)
		clkerr_lst.append(float(clk_err))
		evm_f = float(evm)

		if evm_max_in<0 and evm_f < evm_max_in:
		    evm_lst.append(evm)
		else:
		    evm_lst.append(evm)
		pwr_lst.append(pwr);
		iq_amp.append(amp_err_dB);
		iq_phase.append(phase_err);
		iq_lo.append(lo_offset);

		if read_spmask=='true':
			x = myiqv.read_spmsk(data_type='AVER',unit_no=2);
			loginfo(x)

			n30M.append(float(x[0]));
			n20M.append(float(x[1]));
			n10M.append(float(x[2]));
			p10M.append(float(x[3]));
			p20M.append(float(x[4]));
			p30M.append(float(x[5]));

##		if float(evm) > evm_max:
##			evm_max = float(evm)
##
##		if float(evm) < evm_min:
##			evm_min = evm
##    print "rfglobal.iqv['pwr']:",rfglobal.iqv['pwr']
##    print "rfglobal.iqv['evm_sorted']:",rfglobal.iqv['evm_sorted']

    evm_sorted = rfglobal.iqv['evm_sorted']
    if  evm_sorted == 1:
        evm_lst = sorted(evm_lst)
        half_num = int(len(evm_lst)/2)
        evm_lst_upper = evm_lst[half_num:]
        evm_avg = mfunc.avg_dB10(evm_lst_upper);
    else:
        evm_avg = mfunc.avg_dB10(evm_lst);
    evm_std = mfunc.std_dB10(evm_lst);
    evm_max = mfunc.max_dB10(evm_lst);
    evm_min = mfunc.min_dB10(evm_lst);
    pwr_avg = mfunc.avg_dB10(pwr_lst);
    iqamp_avg = mfunc.avg_dB20(iq_amp);
    #lo_leakage = mfunc.avg_dB10(iq_lo) + 10*np.log10(float(26*2));
    lo_leakage = mfunc.avg_dB10(iq_lo);
    iqphase_avg = np.average(iq_phase);
    evm_wo_iq = mfunc.dB10(mfunc.dB10inv(evm_avg) - mfunc.dB10inv(iqmis2db(iqamp_avg, iqphase_avg)));
    freqerr_avg = np.average(freqerr_lst)
    clkerr_avg = np.average(clkerr_lst)

    rfglobal.iqv = {
        "evm_sorted": evm_sorted,
        "pwr":      pwr_avg,
        "evm_raw":  evm_avg,
        "evm_std":  evm_std,
        "evm_max":  evm_max,
        "iqamp":    iqamp_avg,
        "iqphase":  iqphase_avg,
        "evm_wo_iq":    evm_wo_iq,
        "lo_leakage":    lo_leakage,
        "freq_err":    freqerr_avg,
        "clk_err":    clkerr_avg,
        "evm_min":  evm_min,
        "evm_list": evm_lst,
##        "data_rate": data_rate,
##        "psdu_crc": psdu_crc,
##        "psdu_len": psdu_len
        }
    if read_spmask=='true':
        n30M_avg = mfunc.avg_dB10(n30M);
        n20M_avg = mfunc.avg_dB10(n20M);
        n10M_avg = mfunc.avg_dB10(n10M);
        p30M_avg = mfunc.avg_dB10(p30M);
        p20M_avg = mfunc.avg_dB10(p20M);
        p10M_avg = mfunc.avg_dB10(p10M);

        rfglobal.iqv_spmask = [n30M_avg, n20M_avg, n10M_avg, p30M_avg, p20M_avg, p10M_avg];

    iqv = rfglobal.iqv
    #iqv_mask = rfglobal.iqv_spmask
    evm = iqv['evm_raw']
    evm_std = iqv['evm_std']
    evm_max = iqv['evm_max']
    evm_min = iqv['evm_min']
    pwr = iqv['pwr']
    freq_err = iqv['freq_err']
    clk_err = iqv['clk_err']
    evm_list = iqv['evm_list']
    lo_leakage = iqv['lo_leakage']
    iq_imb_amp = iqv['iqamp']
    iq_imb_phase = iqv ['iqphase']
##    return '%3.2f,%3.2f,%3.2f,%3.2f,%3.2f,%3.2f'%(pwr_avg,evm_avg,iqamp_avg,iqphase_avg,evm_wo_iq, lo_leakage),evm_lst
    return [pwr, freq_err, clk_err, evm, evm_std, evm_max, lo_leakage,iq_imb_amp,iq_imb_phase, evm_list,]

def pwrramp(myiqv,capture_times):
    pwrramp_up = []; pwrramp_down=[];
    for i in range(0,capture_times):
		myiqv.restart(5000,0,auto_range,20);
		rampup,rampdown = myiqv.pwrramp('11b');
		pwrramp_up.append(rampup);
		pwrramp_down.append(rampdown);
		logdebug(rampup,rampdown)
    rampup_avg = np.average(pwrramp_up)
    rampdown_avg = np.average(pwrramp_down)
    rfglobal.iqv = {
        "ramp_up": rampup_avg,
        "ramp_down": rampdown_avg,
        }

    return['%3.2f'%rampup_avg,'%3.2f'%rampdown_avg]
## mask pass or fail
def spectrum_mask(myiqv, capture_times, technology):
	''' only return the specturm mask, "pass" or "fail" '''
	Spectrum_fail_point = []; Spectrum_obw = [];
	auto_range=rfglobal.iqv_arg['auto_range']
	iq_id=sock.get_IQ_ID()
	loginfo("IQ_ID=%s"%iq_id)
	iq_mode = myiqv.get_iq_mode()
	if iq_mode in ['11n_40']:
		ht40mode=1;
	else:
		ht40mode=0;
	for i in range(0,capture_times):
		if iq_id == 1: # IQxel
			myiqv.restart(5000,ht40mode,auto_range,20);
			myiqv.fft(technology);
		elif iq_id == 2: # wt200
			myiqv.restart(5000,ht40mode,auto_range,20);
#		result1 = myiqv.get_result('valid');
#		result2 = myiqv.get_result('length');
#		print result1, result2;
		spectrum_fail = myiqv.get_result('spectrumAverViolationPercentage');
		logdebug(spectrum_fail);
		Spectrum_fail_point.append(float(spectrum_fail));
		obw_mhz = myiqv.get_result('spectrumAverObw');
		logdebug(obw_mhz);
		Spectrum_obw.append(float(obw_mhz));
	logdebug(Spectrum_fail_point)
	logdebug(Spectrum_obw)
	spectrum_fail_avg = np.average(Spectrum_fail_point);
	obw_mhz_avg = np.average(Spectrum_obw);


	rfglobal.iqv_mask = {
		"spectrum_fail_point":spectrum_fail_avg,
		"obw_mhz":obw_mhz_avg,
		}
	return [spectrum_fail_avg,obw_mhz_avg]

##	return '%3.2f,%3.2f'%(spectrum_fail_avg,obw_mhz_avg)

def spectrum_mask_flatness(myiqv, capture_times, technology=3):
    '''
    :return the value of spectrum mask margin!!,
    :retrun the specturm flatness, flatness all > 0("pass")
    '''
    auto_range=rfglobal.iqv_arg['auto_range']
    margin_freq=[]
    margin_db=[]
    flatness_marg=[]
    margin_freq_max=[]
    spectrumMarginFreq=[];spectrumMarginDb=[];flatnessMargin=[];
##    auto_range=0
    iq_id=sock.get_IQ_ID()  # used to identify what instrument to connect
    loginfo("IQ_ID=%s"%iq_id)
    iq_mode = myiqv.get_iq_mode()
    if iq_mode in ['11n_40']:
		ht40mode=1;
    else:
		ht40mode=0;

    if iq_id == 3:  #iqview can not get mask
        freq_mask = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        marg = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        return [freq_mask, marg]
    for i in range(0,capture_times):
        if iq_mode in ['11g','11n_20','11n_40']:
			if iq_id == 1: # IQxel
				myiqv.restart(5000,ht40mode,auto_range,20);
				myiqv.fft(99);  #technology
			elif iq_id == 2: # wt200
				myiqv.restart(5000,ht40mode,auto_range,20);

        elif iq_mode in ['11b']:
			if iq_id == 1: # IQxel
				myiqv.restart(5000,0,auto_range,20);
				myiqv.fft(3);  #technology
			elif iq_id == 2: # wt200
				myiqv.restart(50000,0,auto_range,20);
        spectrumMarginFreq = myiqv.get_vect_result('spectrumMarginOffsetFreqHz');
        spectrumMarginDb = myiqv.get_vect_result('spectrumMarginDb');

        margin_freq.append(spectrumMarginFreq)
        margin_db.append(spectrumMarginDb)
        flatness_marg.append(flatnessMargin)

    margin_db_max=np.array(margin_db,dtype=float).min(axis=0)
    flatness_marg_max=np.array(flatness_marg,dtype=float).min(axis=0)
    n=np.argwhere(margin_db==margin_db_max)
    _n=n[np.lexsort(n.T)]
    m=_n.tolist()
    for i in range(len(m)):
        margin_freq_max.append(np.array(margin_freq,dtype=float)[m[i][0],m[i][1]]/1e6)


    if iq_mode in ['11b']:
        marg_db=["null","null"]
        _margin_db_max=margin_db_max.tolist()
        _margin_db_max.extend(['null','null'])
        marg_db.extend(_margin_db_max)
        marg_freq=['null','null']
        margin_freq_max.extend(['null','null'])
        marg_freq.extend(margin_freq_max)
    else:
        marg_db = margin_db_max.tolist()
        marg_freq = margin_freq_max
    return [marg_freq, marg_db]


def spectrum_flatness_wt200(myiqv, capture_times ):
	'''only return the spectrum flatness,"pass" or "fail"'''
	auto_range=rfglobal.iqv_arg['auto_range']
	spectrum_flat=[]
	iq_mode = myiqv.get_iq_mode()
	if iq_mode in ['11n_40']:
		ht40mode=1;
	else:
		ht40mode=0;
	for i in range(0,capture_times):
		myiqv.restart(5000,ht40mode,auto_range,20);
		flatness = float(myiqv.get_result('flatness_passed_wt200'));
		logdebug(flatness)
		spectrum_flat.append(flatness);
	logdebug(spectrum_flat)
	flatness_avg = np.average(spectrum_flat)
	rfglobal.flatness_passed = {
        "flatness": flatness_avg
        }
	logdebug(flatness_avg)

	return '%f'%flatness_avg


def iqv_rd(type):
    ''' read global "iqv" and return specified parameters (can be "pwr" "evm_raw" "iqamp" "iqphase" "evm_wo_iq")  '''
    if type in (["pwr", "evm_raw", "iqamp", "iqphase", "evm_wo_iq"]):
        iqv = rfglobal.iqv
        return iqv[type]
    elif type == 'spmask':
        iqv = rfglobal.iqv_spmask;
        return '%3.2f,%3.2f,%3.2f,%3.2f,%3.2f,%3.2f'%(iqv[0],iqv[1],iqv[2],iqv[3],iqv[4],iqv[5])
    else:
        loginfo("error: %s is not a valid name"%type)
        return -99.9

def iqmis2db(amp_err_db,phase_err):
    '''Function Description: from IQmismatch value to get EVM value'''
    phase_err_fig=(abs(phase_err/2.0)/180*3.14)**2;
    amp_err_fig=(abs(10**(amp_err_db/20)-1)/2)**2;
    if phase_err_fig+amp_err_fig < 0.00001 :
        return -50.0
    else :
        return 10*math.log10(phase_err_fig+amp_err_fig);

def test_para(rate):
    rate_num = rfglobal.ratedic[rate]
    test_para_11n=['EWC','nxn',1,1,0,1,0,'auto_detect','ltf']  #default
    test_para_11a=['sym_by_sym','raw_long','on','long_train','off']  #default
    test_para_11b=['off','off','std_tx_gac']   #default
    rate_num = rfglobal.ratedic[rate]
    if rate_num < 8:
        test_para = test_para_11b
    elif rate_num < 16:
        test_para = test_para_11a
    else:
        test_para = test_para_11n
    return test_para

def trig_wave(mytester,iqv_no):
    mytester.trig_wave(iqv_no);

def instru_tx_signal(source='', tx_freq=2484,tx_pwr=-60, tx_rate='54m', packnum=100,cable_lose=2,iqv_no=1):
    if source=='tone':
        mytester=tester.tester(tx_freq,tx_pwr,'tone',100,iqv_no,'cw',cable_lose,10, 1,0)
    elif source=='bt':
        rate_name='LE_1M_prbs9'
        mytester=tester.tester(tx_freq,tx_pwr,rate_name,1,iqv_no,'source',cable_lose,10,0);
        mytester.sigout(tx_freq,tx_pwr,cable_lose,rate_name,packnum,iqv_no)
        mytester.trig_wave(iqv_no);
    else:
        mytester=tester.tester(tx_freq,-40,'1m',1,iqv_no,'source',cable_lose,isreset=0)
        mytester.sigout(tx_freq,tx_pwr,cable_lose,tx_rate,packnum,iqv_no)
        mytester.trig_wave(iqv_no)
    return mytester

def set_att(att=10, port=5, atten_fix=False):
    if att > 63:
        print "att must be 0~63 !!"
        return False
    # fix atte
    if atten_fix == True:
        if att >= 33 and (att-30+1)%4 == 0:
            att_t = att - 1
        elif att >= 33 and (att-30)%4 == 0:
            att_t = att + 1
        else:
            att_t = att
    else:
        att_t = att
    att_ser = serial.Serial(port-1)
    if att_ser.isOpen() == True:
        print 'com %d open suc'%(port)
    else:
        print 'com %d open fail'%(port)
        return False

    if att_t < 0x10:
        cmd_t = '7e7e100%x%x'%(att_t,0x10+att_t)
        exp_res_t = '7e7e200%x00%x'%(att_t, 0x20+att_t)
    else:
        cmd_t = '7e7e10%x%x'%(att_t,0x10+att_t)
        exp_res_t = '7e7e20%x00%x'%(att_t, 0x20+att_t)

    cmd = cmd_t.decode("hex")
    exp_res =exp_res_t.decode("hex")

    att_ser.write(cmd)
    time.sleep(0.1)
    res_num = att_ser.inWaiting()

    res = att_ser.read(res_num)
    att_ser.close()

    if res == exp_res :
        print "atte set %d suc !!"%(att)
        return True
    else :
        print "atte set %d fail !!"%(att)
        return False
