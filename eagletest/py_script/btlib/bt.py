import serial
import baselib.test_channel.channel as chn
from baselib.loglib.log_lib import *
from baselib.instrument.iqv import *
import wifilib.crypto as crypto
import wifilib.mem  as mem
import numpy as np
import time
import copy
import random
import math
import binascii
from rf_debug import (rfglobal, i2c, pbus)
from rf_debug.utility import (iofunc, mfunc)
from baselib.test_channel import com
import pylab
import os
import rf_debug.i2c as i2c
##import testcase.tc006_pbus_test as pbus_test

def time_force_wifi(t=10000,chan_id='com'):
    cmdstr="t_force_wifi %d"%t;
    return chn.runcmd(cmdstr,chan_id);

def force_wifi_toggle(n=1000,chan_id='com'):
    cmdstr="force_wifi_toggle %d"%n;
    return chn.runcmd(cmdstr,chan_id);

def force_wifi(chan_id='com'):
    cmdstr="force_wifi";
    return chn.runcmd(cmdstr,chan_id);

def force_bt(chan_id='com'):
    cmdstr="force_bt";
    return chn.runcmd(cmdstr,chan_id);

def coex_bt_hp(chan_id='com'):
    cmdstr="coex_bt_hp";
    return chn.runcmd(cmdstr,chan_id);

def unforce_wifi(chan_id='com'):
    cmdstr="unforce_wifi";
    return chn.runcmd(cmdstr,chan_id);

def rw_le_adv(txpwr=0, chan_id='com'):
    cmdstr="rw_le_adv %d"%txpwr;
    return chn.runcmd(cmdstr,chan_id);

def rw_tx_test(txpwr=4, hoppe=0, chan=0, edr=0, type=4, length=27, et_mask=0x5555, data=0, chan_id='com'):
    cmdstr="rw_tx_test %d %d %d %d %d %d %d %d"%(txpwr, hoppe, chan, edr, type, length, et_mask, data);
    return chn.runcmd(cmdstr,chan_id);


def rw_fcc_bt_tx(txpwr=4, hoppe=0, chan=0, rate=0, length=1, data=0, chan_id='com'):
    cmdstr="fcc_bt_tx %d %d %d %d %d %d"%(txpwr, hoppe, chan, rate, length, data);
    return chn.runcmd(cmdstr,chan_id);


def fcc_tx(txpwr=4, hoppe=0, chan=0, rate=1, data=0):

    fi= (chan/2) + ((chan%2)*40)
    print "%d\n"%fi

    if rate == 1:
        type = 15
        length = 339
        edr =0
    elif rate == 2:
        type = 14
        length = 679
        edr =1
    elif rate == 3:
        type = 15
        length = 1021
        edr =1

    rw_tx_test(txpwr=txpwr, hoppe=hoppe, chan=fi, edr=edr, type=type, length=length, data=data)

def rw_le_tx(chana=37, chanb=39, chanc= 19, txpwr=4, mask=0xffff,chan_id='com'):
    cmdstr="rw_le_tx %d %d %d %d %d"%(chana, chanb, chanc, txpwr, mask);
    return chn.runcmd(cmdstr,chan_id);

def rw_le_tx_nohoppe(chan=37, txpwr=4, mask=0xffff, len=30, data=0,chan_id='com'):
    cmdstr="rw_le_tx_nohoppe %d %d %d %d %d"%(chan, txpwr, mask, len, data);
    return chn.runcmd(cmdstr,chan_id);

def fcc_le_tx(txpwr=4, chan=0, len=30, data=0):
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
    rw_le_tx_nohoppe(chan=fi, txpwr=txpwr,len=len, data=data)

def rw_le_rx_per(freq=0,  chan_id='com'):
    cmdstr="rw_le_rx_per %d"%(freq);
    return chn.runcmd(cmdstr,chan_id);

def rw_le_rx_per_syncw(freq=0, syncw=0x94826E8E,  chan_id='com'):
    cmdstr="rw_le_rx_per %d 0x%x"%(freq,syncw);
    return chn.runcmd(cmdstr,chan_id);

def rw_rx_per(edr=0, freq=0,  chan_id='com'):
    cmdstr="rw_rx_per %d %d"%(edr, freq);
    return chn.runcmd(cmdstr,chan_id);

def rw_rx_per_ulap(edr=0, freq=0, ulap=0x6bc6967e, ltaddr=0, chan_id='com'):
    cmdstr="rw_rx_per_ulap %d %d 0x%x %d"%(edr, freq, ulap, ltaddr);
    return chn.runcmd(cmdstr,chan_id);

def rw_rx_per_ulap_rssi(edr=0, freq=0, ulap=0x6bc6967e, ltaddr=0, chan_id='com'):
    cmdstr="rw_rx_per_ulap_rssi %d %d 0x%x %d"%(edr, freq, ulap, ltaddr);
    return chn.runcmd(cmdstr,chan_id);


def rw_rx_dump(edr=0, freq=0, ulap=0x6bc6967e, ltaddr=0, data_sel=0, dump_len=60000, dump_status=0, chan_id='com'):
    cmdstr="rw_rx_dump %d %d 0x%x %d %d %d %d"%(edr, freq, ulap, ltaddr, data_sel, dump_len, dump_status);
    return chn.runcmd(cmdstr,chan_id);

def bt_tx_GFSK(chan_id='com'):
    cmdstr="BT_tx_GFSK ";
    return chn.runcmd(cmdstr,chan_id);

def hoppe_tx_tone(bt=1,channel=13,delay=0,freq=1,tone1_att=0,chan_id='com'):
    cmdstr="hoppe_tx_tone %d %d %d %d %d"%(channel,delay,freq,tone1_att,bt);
    return chn.runcmd(cmdstr,chan_id);

def bt_tx_packet(forever=0, rate=1, freq_odd=2472, freq_even=2437, freq_offset_500k=0, slot_time=625, delay=210,  data_type=0,tx_slot=1,tx_off_delay=1, chan_id='com'):
    cmdstr="BT_tx_packet %d %d %d %d %d %d %d %d %d %d"%(forever, freq_odd, freq_even, freq_offset_500k, slot_time, delay, rate, data_type, tx_slot, tx_off_delay);
    return chn.runcmd(cmdstr,chan_id);

def bt_tx_packet_stop(rate=1,chan_id='com'):
    cmdstr="BT_tx_packet_stop %d"%rate;
    return chn.runcmd(cmdstr,chan_id);

def set_freq_fast(freq=2484,chan_id='com'):
    cmdstr="set_freq_fast %d"%freq;
    return chn.runcmd(cmdstr,chan_id);

def bt_rx_start(chan_id='com',rate=1,freq_offset_500k=0,start=1,bit_len=300, freq=2472):
    cmdstr="BT_rx_start %d %d %d %d %d"%(rate, freq_offset_500k,start,bit_len,freq);
    return chn.runcmd(cmdstr,chan_id);

def bt_mac_rx_start_debug(chan_id='com', link_type=4, chan=72):
    cmdstr="BT_mac_rx_start_debug %d %d"%(link_type, chan);
    return chn.runcmd(cmdstr,chan_id);

def bt_mac_rx_status_debug(chan_id='com'):
    intr=mem.rd(0x3ff21d04,chan_id);
    if(intr & 2)!=0:
        state=(mem.rd(0x3ff21d18,chan_id)) & 0xff;
        if state==0 or state==0x41:
            return 0;
        else:
            return 2;
    else:
        return 1;


def bt_gen_prbs9(chan_id='com'):
    cmdstr="BT_gen_prbs9 ";
    return chn.runcmd(cmdstr,chan_id);

def bt_rx_prbs9_err_bits(chan_id='com'):
    cmdstr="BT_rx_prbs9_err_bits ";
    return chn.runcmd(cmdstr,chan_id);

def bt_rx_ber(chan_id='com', bits=1600000, link_type=4, chan=72, timeout=20, biterror_thresh=30):
    cmdstr="BT_rx_ber %d %d %d %d %d"%(bits, link_type, chan, timeout, biterror_thresh);
    return chn.runcmd(cmdstr,chan_id);

def bt_rx_per(chan_id='com', link_type=4, chan=72):
    cmdstr="BT_rx_per %d %d"%(link_type, chan);
    return chn.runcmd(cmdstr,chan_id);

def bt_rx_dump(chan_id='com', link_type=4, chan=72):
    cmdstr="BT_rx_dump %d %d"%(link_type, chan);
    return chn.runcmd(cmdstr,chan_id);

def bt_mac_loopback_master(chan_id='com', freq_offset_500k=4, freq=2472, loopback=0, link_type=1, nowhite=1):
    cmdstr="BT_mac_loopback_master %d %d %d %d %d"%(loopback,freq_offset_500k,freq,link_type,nowhite);
    return chn.runcmd(cmdstr,chan_id);

def bt_mac_loopback_slave(chan_id='com', rx_payload_length=300, freq_offset_500k=4, freq=2472, loopback=0, link_type=1, nowhite=1):
    cmdstr="BT_mac_loopback_slave %d %d %d %d %d %d"%(link_type, loopback, rx_payload_length, freq_offset_500k, freq, nowhite);
    return chn.runcmd(cmdstr,chan_id);

def bt_iqv_tx_init(filename='BT/1_dh1_1010.mod',freqMHz=2470,pwrdBm=-15,framecnt=0,port='left'):
    if port=='left':
        print iqv_serv.setvsg_left(freqMHz,pwrdBm)
    else:
        print iqv_serv.setvsg(freqMHz,pwrdBm)
    print iqv_serv.ldmodfile(filename)
    print iqv_serv.txenable(1)

def bt_iqv_tx_init2(freqMHz=2470,pwrdBm=-15,framecnt=0,port='left'):
    if port=='left':
        print iqv_serv.setvsg_left(freqMHz,pwrdBm)
    else:
        print iqv_serv.setvsg(freqMHz,pwrdBm)

def bt_iqxel_tx_init(filename='BT/1_dh1_1010.mod',freqMHz=2470,pwrdBm=-15,framecnt=0,port='left'):
    if port=='left':
        print iqxel_serv.setvsg_left(freqMHz,pwrdBm)
    else:
        print iqxel_serv.setvsg(freqMHz,pwrdBm)
    print iqxel_serv.ldmodfile(filename)
    print iqxel_serv.txenable(1)

def bt_iqv_tx_stop():
    print iqv_serv.txenable(0)

def bt_iqxel_tx_stop():
    print iqxel_serv.txenable(0)

def bt_rx_sensitivity_test(ber_limit=0.00007,basebits=16000,rate=1,file_name='1_dh1_1010.mod',pwrdBm_start=-70,pwrdBm_end=-50,chan_start=72,chan_end=78, file_w = '../bt_rx_sensitivity_',atten=0, port='left'):
    trange="pwr%d_%d_chan%d_%d_"%(pwrdBm_start, pwrdBm_end, chan_start, chan_end)
    f=open(file_w+trange+file_name+'.csv', 'w')
    freq= chan_start+2402
    freq_end= chan_end + 2402
    while freq<=freq_end:
        f.write("\n%dMHz\n"%freq)
        f.write('RX power est, BER,fail, RSSI, noise, pwr inband, pwr fullband, gain, RX bits,RX pac,RX correct pac,PER,W inband max, W fullband max, W rise free, W rise ac, W rise pac, W drop free, W drop ac, W drop pac, HEC error, CRC error , TYPE error, crc_err_gain1, crc_err_gain2, crc_err_gain3, crc_err_gain4, crc_err_gain5, n_be_over_tresh\n')

        pwrdBm=pwrdBm_start
        while pwrdBm<=pwrdBm_end:
            f.write('%ddBm,'%pwrdBm)
            [total_bits,error_bits,RSSI,noise, pwr_ib, pwr_fb, gain, totalp, cp, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
    pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, hec_ep, crc_ep, type_ep,
    crc_err_gain1,crc_err_gain2,crc_err_gain3,crc_err_gain4,crc_err_gain5,be_excd]=bt_rx_ber_test__(basebits=basebits,rate=rate,filename=file_name,pwrdBm=pwrdBm, freq=freq, atten=atten,port=port)
            pwrdBm=pwrdBm+1
            if(total_bits==0):
        	    BER=1
            elif(error_bits==0):
        	    BER=0
            else:
                BER=float(error_bits)/total_bits
            if BER >= ber_limit:
                fail =1
            else :
                fail =0
            if(totalp!=0):
                PER=1-(float(cp)/totalp)
            else:
                PER=1
            f.write("%f,%d,%f,%f,%f,%f,%f,%f, %f, %f, %f, %f,%f,%f,%f,%f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f\n"%(BER,fail,RSSI,noise, pwr_ib, pwr_fb, gain,total_bits,
            totalp, cp, PER,
            pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep, pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep,
            hec_ep, crc_ep, type_ep,
            crc_err_gain1,crc_err_gain2,crc_err_gain3,crc_err_gain4,crc_err_gain5,be_excd))
        freq=freq+1
    f.close

def bt_rx_ber_test(basebits=16000,rate=1,data_type=0,pwrdBm=-15,UAP='01101011',freq=2472):
    if(rate==1):
        if(data_type==0):
            filename='BT/1_dh1_1010.mod'
            ref= ref_1m_dh1_1010()
            bit_len=240+61
        elif(data_type==1):
            filename='BT/1_dh1_prbs9.mod'
            ref= ref_1m_dh1_prbs9()
            bit_len=240+61
        else:
            filename='BT/1_dh5_prbs9.mod'
            ref= ref_1m_dh5_prbs9()
            bit_len=2744+61
    elif(rate==2):
        if(data_type==0):
            filename='BT/2_dh1_1010.mod'
            ref= ref_2m_dh1_1010()
            bit_len=464+57
        elif(data_type==1):
            filename='BT/2_dh1_prbs9.mod'
            ref= ref_2m_dh1_prbs9()
            bit_len=464+57
        else:
            filename='BT/2_dh3_prbs9.mod'
            ref= ref_2m_dh3_prbs9()
            bit_len=2968+57
    else:
        if(data_type==0):
            filename='BT/3_dh1_1010.mod'
            ref= ref_3m_dh1_1010()
            bit_len=61+696-8
        elif(data_type==1):
            filename='BT/3_dh1_prbs9.mod'
            ref= ref_3m_dh1_prbs9()
            bit_len=61+696-8
        else:
            filename='BT/3_dh3_prbs9.mod'
            ref= ref_3m_dh3_prbs9()
            bit_len=61+4448-8

    ref=ref[8:(len(ref)-18)]
    bt_iqv_tx_init(filename=filename,pwrdBm=pwrdBm,freqMHz=freq)

    if rate==1 :
        link_type=4
    else :
        link_type=5

    errorbits=0
    totalbits=0
    loop=0
    while totalbits<basebits:
        loop=loop+1
        #time.sleep(1)
        bt_mac_rx_start_debug(link_type=link_type,chan=freq-2402)
        print iqv_serv.txfrmcnt(framecnt=1)
        for j in range (1,11):
            status=bt_mac_rx_status_debug()
            if status == 0:
                break
        if status==0:
            totalbits=totalbits + 4*len(ref)
            errorbits=errorbits + bt_rx_buffer_cmp(ref)
        if loop>10 and totalbits==0 :
            break
    if(totalbits==0):
        BER=1
    elif(errorbits==0):
        BER=0
    else:
        BER=float(errorbits)/totalbits
    print "rx total %d bits\nrx error %d bits\nBER %f"%(totalbits, errorbits,BER)
    print iqv_serv.txenable(0)
    return [totalbits, errorbits]

def bt_rx_ber_test_(basebits=16000,rate=1,data_type=0,pwrdBm=-15,UAP='01101011',freq=2472):
    if(rate==1):
        if(data_type==0):
            filename='BT/1_dh1_1010.mod'
            ref= ref_1m_dh1_1010()
            bit_len=240+61
        elif(data_type==1):
            filename='BT/1_dh1_prbs9.mod'
            ref= ref_1m_dh1_prbs9()
            bit_len=240+61
        else:
            filename='BT/1_dh5_prbs9.mod'
            ref= ref_1m_dh5_prbs9()
            bit_len=2744+61
    elif(rate==2):
        if(data_type==0):
            filename='BT/2_dh1_prbs9.mod'
            ref= ref_2m_dh1_prbs9()
            bit_len=464+57
        elif(data_type==1):
            filename='BT/2_dh3_prbs9.mod'
            ref= ref_2m_dh3_prbs9()
            bit_len=2968+57
        else:
            filename='BT/2_dh5_prbs9.mod'
            ref= ref_2m_dh3_prbs9()
            bit_len=2968+57
    else:
        if(data_type==0):
            filename='BT/3_dh1_prbs9.mod'
            ref= ref_3m_dh1_prbs9()
            bit_len=61+696-8
        elif(data_type==1):
            filename='BT/3_dh3_prbs9.mod'
            ref= ref_3m_dh3_prbs9()
            bit_len=61+4448-8
        else:
            filename='BT/3_dh5_prbs9.mod'
            ref= ref_3m_dh3_prbs9()
            bit_len=61+4448-8

    ref=ref[8:(len(ref)-18)]
    bt_iqv_tx_init(filename=filename,pwrdBm=pwrdBm,freqMHz=freq)

    if rate==1 :
        link_type=4
    else :
        link_type=5

    errorbits=0
    totalbits=0
    loop=0
    bt_gen_prbs9()
    while totalbits<basebits:
        loop=loop+1
        #time.sleep(1)
        bt_mac_rx_start_debug(link_type=link_type,chan=freq-2402)
        print iqv_serv.txfrmcnt(framecnt=1)
        for j in range (1,11):
            status=bt_mac_rx_status_debug()
            if status == 0:
                break
        if status==0:
            result=bt_rx_prbs9_err_bits()
            result=result.split()
            totalbits=totalbits + int(result[0],16)
            errorbits=errorbits + int(result[1],16)
        if loop>10 and totalbits==0 :
            break
    if(totalbits==0):
        BER=1
    elif(errorbits==0):
        BER=0
    else:
        BER=float(errorbits)/totalbits
    print "rx total %d bits\nrx error %d bits\nBER %f"%(totalbits, errorbits,BER)
    print iqv_serv.txenable(0)
    return [totalbits, errorbits]

def bt_rx_ber_test__(basebits=16000,rate=1,filename='1_dh1_prbs9.mod',pwrdBm=-15,UAP='01101011',freq=2472, atten=0, biterror_thresh=30,port='left'):
    filename='BT/new/'+filename
    bt_iqv_tx_init(filename=filename,pwrdBm=pwrdBm+atten,freqMHz=freq,port=port)

    if rate==1 :
        link_type=4
    else :
        link_type=5

    errorbits=0
    totalbits=0
    loop=0

    print iqv_serv.txfrmcnt(framecnt=0)

    result=bt_rx_ber(bits=basebits, link_type=link_type, chan=freq-2402, biterror_thresh=biterror_thresh)
    print iqv_serv.txenable(0)

    result=result.split()
    totalbits=int(result[0],16)
    errorbits=int(result[1],16)
    RSSI=0-int(result[3],16)
    noise=float(((int(result[4],16)&0x3ff)-1024))/4
    pwr_ib=int(result[5],16)
    pwr_fb=int(result[6],16)
    gain=int(result[7],16)
    totalp=int(result[8],16)

    totalp1=int(result[9],16)
    cp=int(result[10],16)
    #PER=1-(float(cp)/totalp1)

    hec_ep=int(result[11],16)
    crc_ep=int(result[12],16)
    type_ep=int(result[13],16)


    pwr_ibm_w_ep=int(result[24],16)
    pwr_fbm_w_ep=int(result[25],16)

    pwr_r_free_w_ep=int(result[26],16)
    pwr_r_ac_w_ep=int(result[27],16)
    pwr_r_pac_w_ep=int(result[28],16)
    pwr_d_free_w_ep=int(result[29],16)
    pwr_d_ac_w_ep=int(result[30],16)
    pwr_d_pac_w_ep=int(result[31],16)

    crc_err_gain1=int(result[32],16)
    crc_err_gain2=int(result[33],16)
    crc_err_gain3=int(result[34],16)
    crc_err_gain4=int(result[35],16)
    crc_err_gain5=int(result[36],16)

    be_excd=int(result[37],16)





    if(totalp!=0):
        pwr_ib=0-(float(pwr_ib)/totalp)
        pwr_fb=0-(float(pwr_fb)/totalp)
        gain=float(gain)/totalp
    if(totalbits==0):
        BER=1
    elif(errorbits==0):
        BER=0
    else:
        BER=float(errorbits)/totalbits
    print "rx total %d bits\nrx error %d bits\nBER %f"%(totalbits, errorbits,BER)
    print iqv_serv.txenable(0)
    return [totalbits, errorbits,RSSI,noise,pwr_ib,pwr_fb,gain, totalp1, cp, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
    pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, hec_ep, crc_ep, type_ep,
    crc_err_gain1,crc_err_gain2,crc_err_gain3,crc_err_gain4,crc_err_gain5,be_excd]



def rw_rx_per_test(framecnt=1000, edr=1,filename='1_dh1_prbs9.mod',pwrdBm=-15,freq=2472, atten=0, port='left', iqv=1):
    filename='BT/new/'+filename
    if(iqv == 1):
        bt_iqv_tx_init(filename=filename,pwrdBm=pwrdBm+atten,freqMHz=freq, port=port)
        iqv_serv.txfrmcnt(framecnt=1)
    else :
        bt_iqxel_tx_init(filename=filename,pwrdBm=pwrdBm+atten,freqMHz=freq, port=port)
        iqxel_serv.txfrmcnt(framecnt=1)

    rw_freq = ((freq - 2402)/2) + (((freq -2402)%2)*40)
    print "rw_freq %d\n"%rw_freq

    rw_rx_per_ulap(edr=edr, freq=rw_freq)
    if(iqv == 1):
        iqv_serv.txfrmcnt(framecnt=framecnt)
    else:
        iqxel_serv.txfrmcnt(framecnt=framecnt)

    result=cmdstop()
    if(iqv == 1):
        iqv_serv.txenable(0)
    else:
        iqxel_serv.txenable(0)

    result=result.split()
    totalp=int(result[0],16)

    cp=int(result[1],16)
    PER=1-(float(cp)/framecnt)

    hec_ep=int(result[2],16)
    crc_ep=int(result[3],16)
    mic_ep=int(result[4],16)
    seq_ep=int(result[5],16)
    lt_ep=int(result[6],16)
    guard_ep=int(result[7],16)


    pwr_ib=int(result[18],16)
    pwr_fb=int(result[19],16)
    gain=int(result[20],16)
    if(totalp!=0):
        pwr_ib=0-(float(pwr_ib)/totalp)
        pwr_fb=0-(float(pwr_fb)/totalp)
        gain=float(gain)/totalp

    RSSI = pwr_ib - gain
    pwr_ibm_w_ep=int(result[9],16)
    pwr_fbm_w_ep=int(result[10],16)

    pwr_r_free_w_ep=int(result[11],16)
    pwr_r_ac_w_ep=int(result[12],16)
    pwr_r_pac_w_ep=int(result[13],16)
    pwr_d_free_w_ep=int(result[14],16)
    pwr_d_ac_w_ep=int(result[15],16)
    pwr_d_pac_w_ep=int(result[16],16)


    bits_total=int(result[22],16)
    bits_error=int(result[23],16)

    return [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
    pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, hec_ep, crc_ep, mic_ep,
    seq_ep, lt_ep, guard_ep,bits_total,bits_error
    ]



def rw_rx_per_test_rssi(framecnt=1000, edr=1,filename='1_dh1_prbs9.mod',pwrdBm=-15,freq=2472, atten=0, port='left', iqv=1):
    filename='BT/new/'+filename
    if(iqv == 1):
        bt_iqv_tx_init(filename=filename,pwrdBm=pwrdBm+atten,freqMHz=freq, port=port)
    else :
        bt_iqxel_tx_init(filename=filename,pwrdBm=pwrdBm+atten,freqMHz=freq, port=port)
    iqv_serv.txfrmcnt(framecnt=1)
    rw_freq = ((freq - 2402)/2) + (((freq -2402)%2)*40)
    print "rw_freq %d\n"%rw_freq

    rw_rx_per_ulap_rssi(edr=edr, freq=rw_freq)
    if(iqv == 1):
        iqv_serv.txfrmcnt(framecnt=framecnt)
    else:
        iqxel_serv.txfrmcnt(framecnt=framecnt)

    result=cmdstop()
    if(iqv == 1):
        iqv_serv.txenable(0)
    else:
        iqxel_serv.txenable(0)

    result=result.split()
    totalp=int(result[0],16)

    cp=int(result[1],16)
    PER=1-(float(cp)/framecnt)

    hec_ep=int(result[2],16)
    crc_ep=int(result[3],16)
    mic_ep=int(result[4],16)
    seq_ep=int(result[5],16)
    lt_ep=int(result[6],16)
    guard_ep=int(result[7],16)


    pwr_ib=int(result[18],16)
    pwr_fb=int(result[19],16)
    gain=int(result[20],16)
    if(totalp!=0):
        pwr_ib=0-(float(pwr_ib)/totalp)
        pwr_fb=0-(float(pwr_fb)/totalp)
        gain=float(gain)/totalp

    RSSI = pwr_ib - gain
    pwr_ibm_w_ep=int(result[9],16)
    pwr_fbm_w_ep=int(result[10],16)

    pwr_r_free_w_ep=int(result[11],16)
    pwr_r_ac_w_ep=int(result[12],16)
    pwr_r_pac_w_ep=int(result[13],16)
    pwr_d_free_w_ep=int(result[14],16)
    pwr_d_ac_w_ep=int(result[15],16)
    pwr_d_pac_w_ep=int(result[16],16)


    bits_total=int(result[22],16)
    bits_error=int(result[23],16)

    gain_max=int(result[24],16)
    gain_min=int(result[25],16)
    rssi_tmp=result[26:]
    rssi_all=[]
    for rssi_p in rssi_tmp:
        rssi_p_int=int(rssi_p,16)
        rssi_all.append(rssi_p_int)

    return [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
    pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, hec_ep, crc_ep, mic_ep,
    seq_ep, lt_ep, guard_ep,bits_total,bits_error,rssi_all,gain_max,gain_min
    ]



def rw_rx_per_calc(edr=1,freq=2472,ltaddr=1):

    rw_freq = ((freq - 2402)/2) + (((freq -2402)%2)*40)
    print "rw_freq %d\n"%rw_freq

    rw_rx_per_ulap(edr=edr, freq=rw_freq, ltaddr=ltaddr)

    time.sleep(5)

    result=cmdstop()

    result=result.split()
    totalp=int(result[0],16)

    cp=int(result[1],16)
    PER=1-(float(cp)/totalp)

    hec_ep=int(result[2],16)
    crc_ep=int(result[3],16)
    mic_ep=int(result[4],16)
    seq_ep=int(result[5],16)
    lt_ep=int(result[6],16)
    guard_ep=int(result[7],16)


    pwr_ib=int(result[18],16)
    pwr_fb=int(result[19],16)
    gain=int(result[20],16)
    if(totalp!=0):
        pwr_ib=0-(float(pwr_ib)/totalp)
        pwr_fb=0-(float(pwr_fb)/totalp)
        gain=float(gain)/totalp

    RSSI = pwr_ib - gain
    pwr_ibm_w_ep=int(result[9],16)
    pwr_fbm_w_ep=int(result[10],16)

    pwr_r_free_w_ep=int(result[11],16)
    pwr_r_ac_w_ep=int(result[12],16)
    pwr_r_pac_w_ep=int(result[13],16)
    pwr_d_free_w_ep=int(result[14],16)
    pwr_d_ac_w_ep=int(result[15],16)
    pwr_d_pac_w_ep=int(result[16],16)


    bits_total=int(result[22],16)
    bits_error=int(result[23],16)

    ber=1
    if bits_total != 0:
        ber=float(bits_error)/bits_total
    print "BER %f   PER %f\n"%(ber,PER)


def rw_rx_per_test_ci(framecnt=1000, edr=1,filename='1_dh1_prbs9.mod',pwrdBm=-15,freq=2472, chan=38, atten=0, port='right'):
    filename='BT/new/'+filename
    bt_iqv_tx_init2(pwrdBm=pwrdBm+atten,freqMHz=freq, port=port)


    toff_append='_-100us.mod'
    filename=filename+toff_append
    iqv_serv.ldmodfile(filename)
    iqv_serv.txfrmcnt(framecnt=1)

    rw_freq = (chan/2) + ((chan%2)*40)
    print "rw_freq %d\n"%rw_freq

    rw_rx_per_ulap(edr=edr, freq=rw_freq)
    toff=-100

    nleft=framecnt
    #for i in range(1,framecnt+1):
    while nleft>0:
        if nleft<10:
            ntx=nleft
        else:
            ntx=10
        toff_append='_%dus.mod'%toff
        filename=filename+toff_append
        iqv_serv.ldmodfile(filename)
        iqv_serv.txfrmcnt(framecnt=ntx)
        nleft=nleft-ntx
        if toff == 0:
            toff=-100
        else:
            toff=toff+10

    result=cmdstop()


    result=result.split()
    totalp=int(result[0],16)
    cp=int(result[1],16)
    PER=1-(float(cp)/framecnt)

    hec_ep=int(result[2],16)
    crc_ep=int(result[3],16)
    mic_ep=int(result[4],16)
    seq_ep=int(result[5],16)
    lt_ep=int(result[6],16)
    guard_ep=int(result[7],16)


    pwr_ib=int(result[18],16)
    pwr_fb=int(result[19],16)
    gain=int(result[20],16)
    if(totalp!=0):
        pwr_ib=0-(float(pwr_ib)/totalp)
        pwr_fb=0-(float(pwr_fb)/totalp)
        gain=float(gain)/totalp

    RSSI = pwr_ib - gain
    pwr_ibm_w_ep=int(result[9],16)
    pwr_fbm_w_ep=int(result[10],16)

    pwr_r_free_w_ep=int(result[11],16)
    pwr_r_ac_w_ep=int(result[12],16)
    pwr_r_pac_w_ep=int(result[13],16)
    pwr_d_free_w_ep=int(result[14],16)
    pwr_d_ac_w_ep=int(result[15],16)
    pwr_d_pac_w_ep=int(result[16],16)

    bits_total=int(result[22],16)
    bits_error=int(result[23],16)

    return [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
    pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, hec_ep, crc_ep, mic_ep,
    seq_ep, lt_ep, guard_ep,bits_total,bits_error
    ]

def rw_rx_per_sweep(per_limit=0.2,framecnt=1000,edr=0,file_name='1_dh1_1010.mod',pwrdBm_start=-70,pwrdBm_end=-50,chan_start=72,chan_end=78, file_w = '../bt_rx_per_',atten=0, port='left', iqv=1):
    trange="pwr%d_%d_chan%d_%d_"%(pwrdBm_start, pwrdBm_end, chan_start, chan_end)
    f=open(file_w+trange+file_name+'.csv', 'w')
    f.write('Channel,TX power,TX pac,RX pac,RX correct pac,PER,fail,AER, PER RX pac, BER, error bits, total bits, RSSI, pwr inband, pwr fullband, gain, W inband max, W fullband max, W rise free, W rise ac, W rise pac, W drop free, W drop ac, W drop pac, HEC error, CRC error , MIC_error, SEQ_error, LT_error,  GUARD_error\n')
    freq= chan_start+2402
    freq_end= chan_end + 2402
    framecnt_est=framecnt
    while freq<=freq_end:
        pwrdBm=pwrdBm_start
        while pwrdBm<=pwrdBm_end:
            f.write("%dMHz,"%freq)
            f.write("%ddBm,"%pwrdBm)
            [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
            pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, hec_ep, crc_ep, mic_ep,
            seq_ep, lt_ep, guard_ep, bits_total, bits_error]=rw_rx_per_test(framecnt=framecnt,edr=edr,filename=file_name,pwrdBm=pwrdBm, freq=freq, atten=atten, port=port, iqv=iqv)
            if totalp >= framecnt+10 :
                [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
                pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, hec_ep, crc_ep, mic_ep,
                seq_ep, lt_ep, guard_ep, bits_total, bits_error]=rw_rx_per_test(framecnt=framecnt,edr=edr,filename=file_name,pwrdBm=pwrdBm, freq=freq, atten=atten, port=port, iqv=iqv)
            pwrdBm=pwrdBm+1
            PER=1-(float(cp)/framecnt_est)
            if PER >= per_limit:
                fail=1
            else:
                fail=0
            AER=1-(float(totalp)/framecnt_est)
            PER_RX_pac=1
            #print "%d\n"%totalp
            if totalp != 0:
                PER_RX_pac=1-(float(cp)/totalp)
            BER=1
            if bits_total != 0:
                BER=float(bits_error)/bits_total
            f.write("%d,%d,%d,%f,%d,%f,%f, %f, %d, %d, %f,%f,%f,%f,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d\n"
            %(framecnt_est,totalp,cp,PER,fail,AER,PER_RX_pac,BER,bits_error,bits_total,RSSI,
             pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
            pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep,
            pwr_d_pac_w_ep, hec_ep, crc_ep, mic_ep, seq_ep, lt_ep, guard_ep
            ))
        freq=freq+1
    f.close



def rw_rx_per_sweep_target(per_limit=0.2,framecnt=1000,edr=0,file_name='1_dh1_1010.mod',pwrdBm_start=-70,pwrdBm_end=-50,
chan_start=72,tps=-10,tpe=-35, file_w = '../bt_rx_per_', atten=0, port='left', iqv=1):
    trange="sweep_targetpwr_%d_%d_TX%d_%d_chan%d_"%(tps,tpe,pwrdBm_start, pwrdBm_end, chan_start)
    f=open(file_w+trange+file_name+'.csv', 'w')
    freq= chan_start+2402
    #f.write('Channel,TX power,TX pac,RX pac,RX correct pac,PER,fail,AER, PER RX pac, BER, error bits, total bits, RSSI, pwr inband, pwr fullband, gain, W inband max, W fullband max, W rise free, W rise ac, W rise pac, W drop free, W drop ac, W drop pac, HEC error, CRC error , MIC_error, SEQ_error, LT_error,  GUARD_error\n')
    print_lines=['channel, %d, '%freq, 'power\\target power, ']


    #freq_end= chan_end + 2402
    framecnt_est=framecnt

    mem.wrm(0x6001c080, 22,17,0)#tp 3mup0


    pwrdBm=pwrdBm_start
    pwr_idx=2
    while pwrdBm<=pwrdBm_end:
        #f.write("%dMHz,"%freq)
        #f.write("%ddBm,"%pwrdBm)
        #force gain
        print_lines=print_lines+["%ddBm, "%pwrdBm]
        tp_now=tps
        if tps>tpe:
            tp_step=-1
        else:
            tp_step=1
        while tp_now != tpe+tp_step:
            mem.wrm(0x6001c080, 16,8,512+(tp_now*2))
            [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
            pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, hec_ep, crc_ep, mic_ep,
            seq_ep, lt_ep, guard_ep, bits_total, bits_error]=rw_rx_per_test(framecnt=framecnt,edr=edr,filename=file_name,pwrdBm=pwrdBm, freq=freq, atten=atten, port=port, iqv=iqv)
            if totalp >= framecnt+10 :
                [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
                pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, hec_ep, crc_ep, mic_ep,
                seq_ep, lt_ep, guard_ep, bits_total, bits_error]=rw_rx_per_test(framecnt=framecnt,edr=edr,filename=file_name,pwrdBm=pwrdBm, freq=freq, atten=atten, port=port, iqv=iqv)

            PER=1-(float(cp)/framecnt_est)
            if PER >= per_limit:
                fail=1
            else:
                fail=0
            AER=1-(float(totalp)/framecnt_est)
            PER_RX_pac=1
            #print "%d\n"%totalp
            if totalp != 0:
                PER_RX_pac=1-(float(cp)/totalp)
            BER=1
            if bits_total != 0:
                BER=float(bits_error)/bits_total
            if pwrdBm==pwrdBm_start:
                print_lines[1]=print_lines[1]+"%d, "%tp_now
                print_lines[pwr_idx]=print_lines[pwr_idx]+"%f, "%PER
            else:
                print_lines[pwr_idx]=print_lines[pwr_idx]+"%f, "%PER

            tp_now=tp_now+tp_step
        pwrdBm=pwrdBm+1
        pwr_idx=pwr_idx+1
    for i_line in print_lines:
        f.write(i_line+'\n');
    f.close



def rw_rx_per_sweep_rssi(per_limit=0.2,framecnt=1000,edr=0,file_name='1_dh1_1010.mod',pwrdBm_start=-70,pwrdBm_end=-50,chan_start=72,chan_end=78, file_w = '../bt_rx_per_',atten=0, port='left', iqv=1):
    trange="pwr%d_%d_chan%d_%d_"%(pwrdBm_start, pwrdBm_end, chan_start, chan_end)
    f=open(file_w+trange+file_name+'.csv', 'w')
    f.write('Channel,TX power,TX pac,RX pac,RX correct pac,PER,fail,AER, PER RX pac, BER, error bits, total bits, RSSI, pwr inband, pwr fullband, gain, W inband max, W fullband max, W rise free, W rise ac, W rise pac, W drop free, W drop ac, W drop pac, HEC error, CRC error , MIC_error, SEQ_error, LT_error,  GUARD_error, max gain, min gain, RSSI\n')
    freq= chan_start+2402
    freq_end= chan_end + 2402
    framecnt_est=framecnt
    while freq<=freq_end:
        pwrdBm=pwrdBm_start
        while pwrdBm<=pwrdBm_end:
            f.write("%dMHz,"%freq)
            f.write("%ddBm,"%pwrdBm)
            [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
            pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, hec_ep, crc_ep, mic_ep,
            seq_ep, lt_ep, guard_ep, bits_total, bits_error, rssi_all, gain_max, gain_min]=rw_rx_per_test_rssi(framecnt=framecnt,edr=edr,filename=file_name,pwrdBm=pwrdBm, freq=freq, atten=atten, port=port, iqv=iqv)
            if totalp >= framecnt+10 :
                [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
                pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, hec_ep, crc_ep, mic_ep,
                seq_ep, lt_ep, guard_ep, bits_total, bits_error, rssi_all, gain_max, gain_min]=rw_rx_per_test_rssi(framecnt=framecnt,edr=edr,filename=file_name,pwrdBm=pwrdBm, freq=freq, atten=atten, port=port, iqv=iqv)
            pwrdBm=pwrdBm+1
            PER=1-(float(cp)/framecnt_est)
            if PER >= per_limit:
                fail=1
            else:
                fail=0
            AER=1-(float(totalp)/framecnt_est)
            PER_RX_pac=1
            #print "%d\n"%totalp
            if totalp != 0:
                PER_RX_pac=1-(float(cp)/totalp)
            BER=1
            if bits_total != 0:
                BER=float(bits_error)/bits_total
            f.write("%d,%d,%d,%f,%d,%f,%f, %f, %d, %d, %f,%f,%f,%f,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,"
            %(framecnt_est,totalp,cp,PER,fail,AER,PER_RX_pac,BER,bits_error,bits_total,RSSI,
             pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
            pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep,
            pwr_d_pac_w_ep, hec_ep, crc_ep, mic_ep, seq_ep, lt_ep, guard_ep,gain_max,gain_min
            ))
            for rssi_p in rssi_all:
                f.write("%d,"%-rssi_p)
            f.write("\n")
        freq=freq+1
    f.close






def rw_le_rx_per_test(framecnt=1000,filename='LETestRun1a.mod',pwrdBm=-15,freq=2472, atten=0, port='left'):
    filename='BT/LEwaveforms/DirtyPackets/'+filename
    bt_iqv_tx_init(filename=filename,pwrdBm=pwrdBm+atten,freqMHz=freq, port=port)
    iqv_serv.txfrmcnt(framecnt=1)
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

    print "rw_freq %d\n"%fi

    rw_le_rx_per( freq=fi)
    iqv_serv.txfrmcnt(framecnt=framecnt)

    result=cmdstop()
    iqv_serv.txenable(0)

    result=result.split()
    totalp=int(result[0],16)

    cp=int(result[1],16)
    PER=1-(float(cp)/framecnt)

    type_ep=int(result[2],16)
    len_ep=int(result[3],16)
    crc_ep=int(result[4],16)
    mic_ep=int(result[5],16)
    sn_ep=int(result[6],16)
    nesn_ep=int(result[7],16)
    time_ep=int(result[8],16)
    priv_ep=int(result[9],16)

    pwr_ib=int(result[20],16)
    pwr_fb=int(result[21],16)
    gain=int(result[22],16)
    if(totalp!=0):
        pwr_ib=0-(float(pwr_ib)/totalp)
        pwr_fb=0-(float(pwr_fb)/totalp)
        gain=float(gain)/totalp

    RSSI = pwr_ib - gain
    pwr_ibm_w_ep=int(result[11],16)
    pwr_fbm_w_ep=int(result[12],16)

    pwr_r_free_w_ep=int(result[13],16)
    pwr_r_ac_w_ep=int(result[14],16)
    pwr_r_pac_w_ep=int(result[15],16)
    pwr_d_free_w_ep=int(result[16],16)
    pwr_d_ac_w_ep=int(result[17],16)
    pwr_d_pac_w_ep=int(result[18],16)

    return [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
    pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, type_ep, len_ep, crc_ep,
    mic_ep, sn_ep, nesn_ep,time_ep,priv_ep
    ]

def rw_le_rx_per_sweep(per_limit=0.2,framecnt=1000,file_name='LETestRun1a.mod',pwrdBm_start=-70,pwrdBm_end=-50,chan_start=72,chan_end=78, file_w = '../bt_rx_per_',atten=0, port='left'):
    trange="pwr%d_%d_chan%d_%d_"%(pwrdBm_start, pwrdBm_end, chan_start, chan_end)
    f=open(file_w+trange+file_name+'.csv', 'w')
    f.write('Channel,TX power,TX pac,RX pac,RX correct pac,PER,fail,AER, PER RX pac, RSSI, pwr inband, pwr fullband, gain, W inband max, W fullband max, W rise free, W rise ac, W rise pac, W drop free, W drop ac, W drop pac, type error, len error , CRC error, MIC error, SN error,  NESN error, time error, priv error\n')
    freq= (chan_start+2402)&0xfffffffe
    freq_end= chan_end + 2402
    framecnt_est=framecnt
    while freq<=freq_end:
        pwrdBm=pwrdBm_start
        while pwrdBm<=pwrdBm_end:
            f.write("%dMHz,"%freq)
            f.write("%ddBm,"%pwrdBm)
            [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
            pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, type_ep, len_ep, crc_ep,
            mic_ep, sn_ep, nesn_ep,time_ep,priv_ep]=rw_le_rx_per_test(framecnt=framecnt,filename=file_name,pwrdBm=pwrdBm, freq=freq, atten=atten, port=port)
            if totalp >= framecnt+10 :
                [totalp, cp, RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
                pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, type_ep, len_ep, crc_ep,
                mic_ep, sn_ep, nesn_ep,time_ep,priv_ep]=rw_le_rx_per_test(framecnt=framecnt,filename=file_name,pwrdBm=pwrdBm, freq=freq, atten=atten, port=port)
            pwrdBm=pwrdBm+1
            PER=1-(float(cp)/framecnt_est)
            if PER >= per_limit:
                fail=1
            else:
                fail=0
            AER=1-(float(totalp)/framecnt_est)
            PER_RX_pac=1
            #print "%d\n"%totalp
            if totalp != 0:
                PER_RX_pac=1-(float(cp)/totalp)
            f.write("%d,%d,%d,%f,%d,%f,%f,%f,%f,%f,%f,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d\n"
            %(framecnt_est,totalp,cp,PER,fail,AER,PER_RX_pac,RSSI,
            pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
            pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep,
            pwr_d_pac_w_ep,  type_ep, len_ep, crc_ep, mic_ep, sn_ep, nesn_ep,time_ep,priv_ep
            ))
        freq=(freq+2)&0xfffffffe
    f.close




def rw_per_ci_sweep(per_limit=0.2,directory="../per/", dcap_s=110, framecnt=5000,edr=0,rate=1,file_name='1_dh1_prbs9',
pwrdBm_start=-35, pwrdBm_start_force=0,chan_start=40, ci_start=-40, ci_end=40, step=1, sig_os=0, sig_os_force=0, time_offset=-80, atten=23,save_name='', port='right'):
    dname="per_ci_sweep_dcap%d_pwr%d_chan%d_cis%d_cie%d_tos%d"%(dcap_s,pwrdBm_start, chan_start, ci_start, ci_end, time_offset)+save_name
    dname=directory+dname
    #if(not(os.path.exists(dname))):
    #    os.makedirs(dname)
    f=open(dname+'.csv', 'w')
    f.write('ci fos, TX power,TX pac,RX pac,RX correct pac,PER,fail,AER, PER RX pac, BER, error bits, total bits, RSSI, pwr inband, pwr fullband, gain, W inband max, W fullband max, W rise free, W rise ac, W rise pac, W drop free, W drop ac, W drop pac, HEC error, CRC error , MIC error, SEQ_error, LT_error, GUARD_error\n')
    freq_raw= chan_start+2402
    framecnt_est=framecnt
    pwrdBm=pwrdBm_start
    if(ci_end<ci_start):
        step=-step
    else:
        step=step
    ci=ci_start
    i2c.wic("bbtop", "filter_btrx_dcap_lq",dcap_s-2)
    i2c.wic("bbtop", "filter_btrx_dcap_hq",dcap_s)
    print iqv_serv.txenable(1)

    while(ci!=(ci_end+step)):
            if(rate==1):
                if(ci==0):
                    cidb=11
                elif(abs(ci)==1):
                    cidb=0
                elif(abs(ci)==2):
                    cidb=-30
                else:
                    cidb=-40
            elif(rate==2):
                if(ci==0):
                    cidb=13
                elif(abs(ci)==1):
                    cidb=0
                elif(abs(ci)==2):
                    cidb=-30
                else:
                    cidb=-40
            else:
                if(ci==0):
                    cidb=21
                elif(abs(ci)==1):
                    cidb=5
                elif(abs(ci)==2):
                    cidb=-25
                else:
                    cidb=-33
            if(sig_os_force==0):
                if(ci<-6):
                    if(rate==2):
                        sig_os=33
                    else:
                        sig_os=33
                elif(ci>6):
                    if(rate==2):
                        sig_os=-33
                    else:
                        sig_os=-33
                else:
                    if(freq_raw<=2441):
                        sig_os=-33
                    else:
                        sig_os=33
            freq=freq_raw-sig_os

            if(pwrdBm_start_force==0):
                if(rate==1):
                    if(ci==0):
                        pwrdBm=-60
                    elif(abs(ci)==1):
                        pwrdBm=-60
                    elif(abs(ci)==2):
                        pwrdBm=-30
                    else:
                        pwrdBm=-27
                elif(rate==2):
                    if(ci==0):
                        pwrdBm=-60
                    elif(abs(ci)==1):
                        pwrdBm=-60
                    elif(abs(ci)==2):
                        pwrdBm=-30
                    else:
                        pwrdBm=-27
                else:
                    if(ci==0):
                        pwrdBm=-60
                    elif(abs(ci)==1):
                        pwrdBm=-60
                    elif(abs(ci)==2):
                        pwrdBm=-35
                    else:
                        pwrdBm=-34

            f.write("%dMHz,"%ci)
            f.write("%ddBm,"%pwrdBm)
            if(sig_os==0):
                file_name_full="test_"+file_name+"_ci%dm_%ddB_%dus.mod"%(ci, cidb, time_offset)
            else:
                file_name_full="test_"+file_name+"_ci%dm_%ddB_sig%dm"%(ci, cidb, sig_os)
            [total_pac,cpac,RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
            pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep,
            pwr_d_pac_w_ep, hec_ep, crc_ep, mic_ep, seq_ep, lt_ep, guard_ep,bits_total,bits_error]=rw_rx_per_test_ci(framecnt=framecnt,edr=edr,filename=file_name_full,pwrdBm=pwrdBm, freq=freq, chan=chan_start, atten=atten, port=port)
            PER=1-(float(cpac)/framecnt_est)
            if PER >= per_limit:
                fail =1
            else :
                fail =0
            AER=1-(float(total_pac)/framecnt_est)
            PER_RX_pac=1
            if total_pac != 0:
                PER_RX_pac=1-(float(cpac)/total_pac)
            BER=1
            if bits_total != 0:
                BER=float(bits_error)/bits_total
            f.write("%d,%d,%d,%f,%d,%f,%f, %f, %d, %d,%f,%f,%f,%f,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d\n"
            %(framecnt_est,total_pac,cpac,PER,fail,AER,PER_RX_pac,BER,bits_error,bits_total, RSSI,
             pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
            pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep,
            pwr_d_pac_w_ep, hec_ep, crc_ep,mic_ep, seq_ep, lt_ep, guard_ep))
            ci=ci+step
    iqv_serv.txenable(0)
    f.close




def rw_per_ci_sweep_dcap(per_limit=0.2,directory="../per/", dcap_s=110, dcap_e=110, framecnt=5000,edr=0,rate=1,file_name='1_dh1_prbs9',
chan_start=40, ci_start=-40, ci_end=40, atten=23,save_name='', port='right'):

    #weights for evaluation
    wper_raw=np.ones(145)
    wper_raw[72-10]=1.2
    wper_raw[73-9]=1.2
    wper_raw[72-8]=1.2
    wper_raw[72-7]=1.2
    wper_raw[72-6]=1.2
    wper_raw[72-5]=1.5
    wper_raw[72-4]=1.7
    wper_raw[72-3]=1.9
    wper_raw[72-2]=1.9
    wper_raw[72-1]=1.9
    wper_raw[72-0]=3
    wper_raw[72+1]=1.9
    wper_raw[72+2]=0.5
    wper_raw[72+3]=0.2
    wper_raw[72+4]=0.1
    wper_raw[72+5]=0.2
    wper_raw[72+6]=0.5
    wper_raw[72+7]=1.2
    wper_raw[72+8]=1.2
    wper_raw[72+9]=1.2
    wper_raw[72+10]=1.2
    wper=np.exp(wper_raw)
    wper_sum=np.sum(wper)
    wper=wper/wper_sum

    wper_idxs=ci_start+72
    wper_idxe=ci_end+73
    wper_used=wper[wper_idxs:wper_idxe]
    wper_stored=[]

    print iqv_serv.txenable(1)
    time_offset=-80
    step=1
    pwrdBm_start_force=0
    sig_os_force=0
    dname="per_ci_sweep_dcaps%d_dcape%d_chan%d_cis%d_cie%d_"%(dcap_s,dcap_e, chan_start, ci_start, ci_end)+save_name
    dname=directory+dname
    #if(not(os.path.exists(dname))):
    #    os.makedirs(dname)
    print_lines=['interference,']

    f=open(dname+'.csv', 'w')
    #f.write('ci fos, TX power,TX pac,RX pac,RX correct pac,PER,fail,AER, PER RX pac, RSSI, pwr inband, pwr fullband, gain, W inband max, W fullband max, W rise free, W rise ac, W rise pac, W drop free, W drop ac, W drop pac, HEC error, CRC error , MIC error, SEQ_error, LT_error, GUARD_error\n')
    freq_raw= chan_start+2402
    framecnt_est=framecnt
    if(ci_end<ci_start):
        step=-step
    else:
        step=step

    dcap=dcap_s
    while(dcap!=(dcap_e+1)):
        per_stored=[]
        ci=ci_start
        ci_line=1
        i2c.wic("bbtop", "filter_btrx_dcap_lq",dcap-2)
        i2c.wic("bbtop", "filter_btrx_dcap_hq",dcap)
        print_lines[0]=print_lines[0]+'%d,'%dcap
        dcap=dcap+1
        while(ci!=(ci_end+step)):
                if(rate==1):
                    if(ci==0):
                        cidb=11
                    elif(abs(ci)==1):
                        cidb=0
                    elif(abs(ci)==2):
                        cidb=-30
                    else:
                        cidb=-40
                elif(rate==2):
                    if(ci==0):
                        cidb=13
                    elif(abs(ci)==1):
                        cidb=0
                    elif(abs(ci)==2):
                        cidb=-30
                    else:
                        cidb=-40
                else:
                    if(ci==0):
                        cidb=21
                    elif(abs(ci)==1):
                        cidb=5
                    elif(abs(ci)==2):
                        cidb=-25
                    else:
                        cidb=-33
                if(sig_os_force==0):
                    if(ci<-6):
                        if(rate==2):
                            sig_os=33
                        else:
                            sig_os=33
                    elif(ci>6):
                        if(rate==2):
                            sig_os=-33
                        else:
                            sig_os=-33
                    else:
                        if(freq_raw<=2441):
                            sig_os=-33
                        else:
                            sig_os=33
                freq=freq_raw-sig_os

                if(pwrdBm_start_force==0):
                    if(rate==1):
                        if(ci==0):
                            pwrdBm=-60
                        elif(abs(ci)==1):
                            pwrdBm=-60
                        elif(abs(ci)==2):
                            pwrdBm=-30
                        else:
                            pwrdBm=-27
                    elif(rate==2):
                        if(ci==0):
                            pwrdBm=-60
                        elif(abs(ci)==1):
                            pwrdBm=-60
                        elif(abs(ci)==2):
                            pwrdBm=-30
                        else:
                            pwrdBm=-27
                    else:
                        if(ci==0):
                            pwrdBm=-60
                        elif(abs(ci)==1):
                            pwrdBm=-60
                        elif(abs(ci)==2):
                            pwrdBm=-35
                        else:
                            pwrdBm=-34
                if(dcap==(dcap_s+1)):
                    print_lines=print_lines+["%dMHz,"%ci]
                #f.write("%dMHz,"%ci)
                #f.write("%ddBm,"%pwrdBm)
                if(sig_os==0):
                    file_name_full="test_"+file_name+"_ci%dm_%ddB_%dus.mod"%(ci, cidb, time_offset)
                else:
                    file_name_full="test_"+file_name+"_ci%dm_%ddB_sig%dm"%(ci, cidb, sig_os)
                [total_pac,cpac,RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
                pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep,
                pwr_d_pac_w_ep, hec_ep, crc_ep, mic_ep, seq_ep, lt_ep, guard_ep,bits_total,bits_error]=rw_rx_per_test_ci(framecnt=framecnt,edr=edr,filename=file_name_full,pwrdBm=pwrdBm, freq=freq, chan=chan_start, atten=atten, port=port)
                PER=1-(float(cpac)/framecnt_est)
                if PER >= per_limit:
                    fail =1
                else :
                    fail =0
                AER=1-(float(total_pac)/framecnt_est)
                PER_RX_pac=1
                if total_pac != 0:
                    PER_RX_pac=1-(float(cpac)/total_pac)
    ##            f.write("%d,%d,%d,%f,%d,%f,%f,%f,%f,%f,%f,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d\n"
    ##            %(framecnt_est,total_pac,cpac,PER,fail,AER,PER_RX_pac,RSSI,
    ##             pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
    ##            pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep,
    ##            pwr_d_pac_w_ep, hec_ep, crc_ep,mic_ep, seq_ep, lt_ep, guard_ep))
                print_lines[ci_line]=print_lines[ci_line]+"%f,"%PER
                per_stored=per_stored+[PER]
                ci=ci+step
                ci_line=ci_line+1
        print wper_used
        print per_stored
        wper_rslt=np.sum(wper_used*per_stored)
        if(dcap==(dcap_s+1)):
            print_lines=print_lines+["eva, %f, "%wper_rslt]
        else:
            print_lines[ci_end-ci_start+2]=print_lines[ci_end-ci_start+2]+"%f, "%wper_rslt
        wper_stored=wper_stored+[wper_rslt]

    wper_min=np.min(wper_stored)
    wper_min_idx=np.argmin(wper_stored)
    print_lines=print_lines+["min, "]
    for i_wper in wper_stored:
        if i_wper == wper_min:
            print_lines[ci_end-ci_start+3]=print_lines[ci_end-ci_start+3] + "1, "
        else:
            print_lines[ci_end-ci_start+3]=print_lines[ci_end-ci_start+3] + ", "

    for i_line in print_lines:
        f.write(i_line+'\n');
    iqv_serv.txenable(0)
    f.close



def rw_per_ci_sweep_dcap_target(per_limit=0.2,directory="../per/", dcap_s=110, dcap_e=110, tps=-20,tpe=-30, framecnt=5000,edr=0,rate=1,file_name='1_dh1_prbs9',
chan_start=40, ci_start=-40, ci_end=40, atten=23,save_name='', port='right'):
    mem.wrm(0x6001c080, 22,17,0)#tp 3mup0

    #weights for evaluation
    wper_raw=np.ones(145)
    wper_raw[72-10]=1.2
    wper_raw[73-9]=1.2
    wper_raw[72-8]=1.2
    wper_raw[72-7]=1.2
    wper_raw[72-6]=1.2
    wper_raw[72-5]=1.5
    wper_raw[72-4]=1.7
    wper_raw[72-3]=1.9
    wper_raw[72-2]=1.9
    wper_raw[72-1]=1.9
    wper_raw[72-0]=3
    wper_raw[72+1]=1.9
    wper_raw[72+2]=0.5
    wper_raw[72+3]=0.2
    wper_raw[72+4]=0.1
    wper_raw[72+5]=0.2
    wper_raw[72+6]=0.5
    wper_raw[72+7]=1.2
    wper_raw[72+8]=1.2
    wper_raw[72+9]=1.2
    wper_raw[72+10]=1.2
    wper=np.exp(wper_raw)
    wper_sum=np.sum(wper)
    wper=wper/wper_sum

    wper_idxs=ci_start+72
    wper_idxe=ci_end+73
    wper_used=wper[wper_idxs:wper_idxe]


    print iqv_serv.txenable(1)
    time_offset=-80
    step=1
    pwrdBm_start_force=0
    sig_os_force=0
    dname="per_ci_sweep_target_tps%d_tpe%d_dcaps%d_dcape%d_chan%d_cis%d_cie%d_"%(tps, tpe, dcap_s, dcap_e, chan_start, ci_start, ci_end)+save_name
    dname=directory+dname
    #if(not(os.path.exists(dname))):
    #    os.makedirs(dname)


    f=open(dname+'.csv', 'w')
    #f.write('ci fos, TX power,TX pac,RX pac,RX correct pac,PER,fail,AER, PER RX pac, RSSI, pwr inband, pwr fullband, gain, W inband max, W fullband max, W rise free, W rise ac, W rise pac, W drop free, W drop ac, W drop pac, HEC error, CRC error , MIC error, SEQ_error, LT_error, GUARD_error\n')
    freq_raw= chan_start+2402
    framecnt_est=framecnt
    if(ci_end<ci_start):
        step=-step
    else:
        step=step

    #loop all target
    tp_now=tps
    if tps>tpe:
        tp_step=-1
    else:
        tp_step=1
    while tp_now != tpe+tp_step:
        print_lines=['interference,']
        wper_min=1
        wper_stored=[]
        f.write("target, %d, \n"%tp_now);
        mem.wrm(0x6001c080, 16,8,512+(tp_now*2))
        dcap=dcap_s
        while(dcap!=(dcap_e+1)):
            per_stored=[]
            ci=ci_start
            ci_line=1
            i2c.wic("bbtop", "filter_btrx_dcap_lq",dcap-2)
            i2c.wic("bbtop", "filter_btrx_dcap_hq",dcap)
            print_lines[0]=print_lines[0]+'%d,'%dcap
            dcap=dcap+1
            while(ci!=(ci_end+step)):
                    if(rate==1):
                        if(ci==0):
                            cidb=11
                        elif(abs(ci)==1):
                            cidb=0
                        elif(abs(ci)==2):
                            cidb=-30
                        else:
                            cidb=-40
                    elif(rate==2):
                        if(ci==0):
                            cidb=13
                        elif(abs(ci)==1):
                            cidb=0
                        elif(abs(ci)==2):
                            cidb=-30
                        else:
                            cidb=-40
                    else:
                        if(ci==0):
                            cidb=21
                        elif(abs(ci)==1):
                            cidb=5
                        elif(abs(ci)==2):
                            cidb=-25
                        else:
                            cidb=-33
                    if(sig_os_force==0):
                        if(ci<-6):
                            if(rate==2):
                                sig_os=33
                            else:
                                sig_os=33
                        elif(ci>6):
                            if(rate==2):
                                sig_os=-33
                            else:
                                sig_os=-33
                        else:
                            if(freq_raw<=2441):
                                sig_os=-33
                            else:
                                sig_os=33
                    freq=freq_raw-sig_os

                    if(pwrdBm_start_force==0):
                        if(rate==1):
                            if(ci==0):
                                pwrdBm=-60
                            elif(abs(ci)==1):
                                pwrdBm=-60
                            elif(abs(ci)==2):
                                pwrdBm=-30
                            else:
                                pwrdBm=-27
                        elif(rate==2):
                            if(ci==0):
                                pwrdBm=-60
                            elif(abs(ci)==1):
                                pwrdBm=-60
                            elif(abs(ci)==2):
                                pwrdBm=-30
                            else:
                                pwrdBm=-27
                        else:
                            if(ci==0):
                                pwrdBm=-60
                            elif(abs(ci)==1):
                                pwrdBm=-60
                            elif(abs(ci)==2):
                                pwrdBm=-35
                            else:
                                pwrdBm=-34
                    if(dcap==(dcap_s+1)):
                        print_lines=print_lines+["%dMHz,"%ci]
                    #f.write("%dMHz,"%ci)
                    #f.write("%ddBm,"%pwrdBm)
                    if(sig_os==0):
                        file_name_full="test_"+file_name+"_ci%dm_%ddB_%dus.mod"%(ci, cidb, time_offset)
                    else:
                        file_name_full="test_"+file_name+"_ci%dm_%ddB_sig%dm"%(ci, cidb, sig_os)
                    [total_pac,cpac,RSSI, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
                    pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep,
                    pwr_d_pac_w_ep, hec_ep, crc_ep, mic_ep, seq_ep, lt_ep, guard_ep,bits_total,bits_error]=rw_rx_per_test_ci(framecnt=framecnt,edr=edr,filename=file_name_full,pwrdBm=pwrdBm, freq=freq, chan=chan_start, atten=atten, port=port)
                    PER=1-(float(cpac)/framecnt_est)
                    if PER >= per_limit:
                        fail =1
                    else :
                        fail =0
                    AER=1-(float(total_pac)/framecnt_est)
                    PER_RX_pac=1
                    if total_pac != 0:
                        PER_RX_pac=1-(float(cpac)/total_pac)
        ##            f.write("%d,%d,%d,%f,%d,%f,%f,%f,%f,%f,%f,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d\n"
        ##            %(framecnt_est,total_pac,cpac,PER,fail,AER,PER_RX_pac,RSSI,
        ##             pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
        ##            pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep,
        ##            pwr_d_pac_w_ep, hec_ep, crc_ep,mic_ep, seq_ep, lt_ep, guard_ep))
                    print_lines[ci_line]=print_lines[ci_line]+"%f,"%PER
                    per_stored=per_stored+[PER]
                    ci=ci+step
                    ci_line=ci_line+1
            #print wper_used
            #print per_stored
            wper_rslt=np.sum(wper_used*per_stored)
            if(dcap==(dcap_s+1)):
                print_lines=print_lines+["eva, %f, "%wper_rslt]
            else:
                print_lines[ci_end-ci_start+2]=print_lines[ci_end-ci_start+2]+"%f, "%wper_rslt
            wper_stored=wper_stored+[wper_rslt]

        wper_min=np.min(wper_stored)
        wper_min_idx=np.argmin(wper_stored)
        print_lines=print_lines+["min, "]
        for i_wper in wper_stored:
            if i_wper == wper_min:
                print_lines[ci_end-ci_start+3]=print_lines[ci_end-ci_start+3] + "1, "
            else:
                print_lines[ci_end-ci_start+3]=print_lines[ci_end-ci_start+3] + ", "

        for i_line in print_lines:
            f.write(i_line+'\n');
        tp_now=tp_now+tp_step
        f.write('\n\n');
    iqv_serv.txenable(0)
    f.close




def rw_rx_dump_file(directory="Y:/todd/BT/dump/", save="rw_dump_", edr=1, freq=2480,  ltaddr=1, data_sel=0, dump_len=60000, dump_status=0):
    now=time.localtime()
    file_name="%4d%2d%2d%2d%2d%2d"%(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min,now.tm_sec)
    file_name=directory+save+file_name

    rw_freq = ((freq - 2402)/2) + (((freq -2402)%2)*40)
    print "rw_freq %d\n"%rw_freq

    rslt=rw_rx_dump(edr=edr, freq=rw_freq, ltaddr=ltaddr, data_sel=data_sel, dump_len=dump_len, dump_status=dump_status)
    rslt=rslt.split()
    iteration=int(rslt[0],10)
    success=int(rslt[5],10)
    if success==1 :
        buf_base=0x3ffe8000
        f=open(file_name+'.csv', 'w')
        f.write('pwr_fb,pwr_ib,gain,rx_q,rx_i,phi\n')
        start=0
        phase=0
        trd=dump_len/1000
        rdl=np.mod(dump_len,1000)
        rdata=[]
        for ird in range(0,trd):
            rdata_=mem.rdmem(buf_base+(ird*4000),4000)
            rdata=rdata + rdata_.split()
        rdata_=mem.rdmem(buf_base+(trd*4000),rdl*4)
        rdata=rdata + rdata_.split()
##        rdata=mem.rdmem(buf_base,dump_len*4)
##        rdata=rdata.split()
##        for addr in range(0,dump_len):
##            rdata=rdata + [mem.rd(buf_base+addr*4)]
        for element in rdata:
            element=int(element,16)
            if start:
                if (element&0x80000000 == 0) and (phase==0):
                    rx_i=element&0x3fff
                    rx_q=(element>>14)&0x3fff
                    pwr_fb=(element>>23)&0xe0
                    phase=1
                elif (element&0x80000000 == 0x80000000) and (phase==1):
                    phi=element&0x3ff
                    gain=(element>>10)&0xff
                    pwr_ib=(element>>18)&0xff
                    pwr_fb=pwr_fb+((element>>26)&0x1f)
                    pwr_ib=pwr_ib-256
                    pwr_fb=pwr_fb-256
                    if rx_i >=8192:
                        rx_i=rx_i-16384
                    if rx_q >=8192:
                        rx_q=rx_q-16384
                    if phi >= 512:
                        phi=phi-1024
                    f.write('%d,%d,%d,%d,%d,%d\n'%(pwr_fb,pwr_ib,gain,rx_q,rx_i,phi))
                    phase=0
            else:
                if element&0x80000000 == 0:
                    rx_i=element&0x3fff
                    rx_q=(element>>14)&0x3fff
                    pwr_fb=(element>>23)&0xe0
                    start=1
                    phase=1


        print 'DUMP DONE!'
    else:
        print 'DUMP FAILED!'

    f.close()


def bt_rx_per_test(framecnt=1000, rate=1,filename='1_dh1_prbs9.mod',pwrdBm=-15,UAP='01101011',freq=2472, atten=0,port='left'):
    filename='BT/new/'+filename
    bt_iqv_tx_init(filename=filename,pwrdBm=pwrdBm+atten,freqMHz=freq, port=port)

    if rate==1 :
        link_type=4
    else :
        link_type=5

    errorbits=0
    totalbits=0
    loop=0

    bt_rx_per(link_type=link_type, chan=freq-2402)
    print iqv_serv.txfrmcnt(framecnt=framecnt)


    result=cmdstop()
    print iqv_serv.txenable(0)

    result=result.split()
    totalp=int(result[0],16)
    cp=int(result[1],16)
    PER=1-(float(cp)/framecnt)
    RSSI=0-int(result[24],16)
    noise=float(((int(result[25],16)&0x3ff)-1024))/4

    pwr_ib=int(result[26],16)
    pwr_fb=int(result[27],16)
    gain=int(result[28],16)
    if(totalp!=0):
        pwr_ib=0-(float(pwr_ib)/totalp)
        pwr_fb=0-(float(pwr_fb)/totalp)
        gain=float(gain)/totalp
    hec_ep=int(result[2],16)
    crc_ep=int(result[3],16)
    type_ep=int(result[4],16)

    pwr_ibm_w_ep=int(result[15],16)
    pwr_fbm_w_ep=int(result[16],16)

    pwr_r_free_w_ep=int(result[17],16)
    pwr_r_ac_w_ep=int(result[18],16)
    pwr_r_pac_w_ep=int(result[19],16)
    pwr_d_free_w_ep=int(result[20],16)
    pwr_d_ac_w_ep=int(result[21],16)
    pwr_d_pac_w_ep=int(result[22],16)

    crc_err_gain1=int(result[29],16)
    crc_err_gain2=int(result[30],16)
    crc_err_gain3=int(result[31],16)
    crc_err_gain4=int(result[32],16)
    crc_err_gain5=int(result[33],16)

    print "tx total pac %d\nrx total pac %d     rx correct pac %d\nPER %f\n"%(framecnt, totalp, cp, PER)
    return [totalp, cp, RSSI, noise, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
    pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, hec_ep, crc_ep, type_ep,
    crc_err_gain1,crc_err_gain2,crc_err_gain3,crc_err_gain4,crc_err_gain5]


def bt_rx_per_sweep(per_limit=0.2,framecnt=1000,rate=1,file_name='1_dh1_1010.mod',pwrdBm_start=-70,pwrdBm_end=-50,chan_start=72,chan_end=78, file_w = '../bt_rx_per_',atten=0,port='left'):
    trange="pwr%d_%d_chan%d_%d_"%(pwrdBm_start, pwrdBm_end, chan_start, chan_end)
    f=open(file_w+trange+file_name+'.csv', 'w')
    f.write('Channel,TX power,TX pac,RX pac,RX correct pac,PER,fail,AER, PER RX pac, RSSI, noise, pwr inband, pwr fullband, gain, W inband max, W fullband max, W rise free, W rise ac, W rise pac, W drop free, W drop ac, W drop pac, HEC error, CRC error , TYPE error, crc_err_gain1, crc_err_gain2, crc_err_gain3, crc_err_gain4, crc_err_gain5\n')
    freq= chan_start+2402
    freq_end= chan_end + 2402
    framecnt_est=framecnt+5
    while freq<=freq_end:
        pwrdBm=pwrdBm_start
        while pwrdBm<=pwrdBm_end:
            f.write("%dMHz,"%freq)
            f.write("%ddBm,"%pwrdBm)
            [total_pac,cpac,RSSI,noise, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
            pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep,
            pwr_d_pac_w_ep, hec_ep, crc_ep, type_ep, crc_err_gain1,crc_err_gain2,crc_err_gain3,crc_err_gain4,crc_err_gain5]=bt_rx_per_test(framecnt=framecnt,rate=rate,filename=file_name,pwrdBm=pwrdBm, freq=freq, atten=atten, port=port)
            if total_pac>=framecnt+10:
                [total_pac,cpac,RSSI,noise, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
                pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep,
                pwr_d_pac_w_ep, hec_ep, crc_ep, type_ep, crc_err_gain1,crc_err_gain2,crc_err_gain3,crc_err_gain4,crc_err_gain5]=bt_rx_per_test(framecnt=framecnt,rate=rate,filename=file_name,pwrdBm=pwrdBm, freq=freq, atten=atten, port=port)
            pwrdBm=pwrdBm+1
            PER=1-(float(cpac)/framecnt_est)
            if PER >= per_limit :
                fail =1
            else:
                fail =0
            AER=1-(float(total_pac)/framecnt_est)
            PER_RX_pac=1
            if total_pac != 0:
                PER_RX_pac=1-(float(cpac)/total_pac)
            f.write("%d,%d,%d,%f,%d,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f\n"
            %(framecnt_est,total_pac,cpac,PER,fail,AER,PER_RX_pac,RSSI,noise,
             pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
            pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep,
            pwr_d_pac_w_ep, hec_ep, crc_ep, type_ep,
            crc_err_gain1,crc_err_gain2,crc_err_gain3,crc_err_gain4,crc_err_gain5))
        freq=freq+1
    f.close



def bt_mem_tst(rate=1,data_type=0):
    if(rate==1):
        if(data_type==0):
            filename='BT/1_dh1_1010.mod'
            ref= ref_1m_dh1_1010()
        elif(data_type==1):
            filename='BT/1_dh1_prbs9.mod'
            ref= ref_1m_dh1_prbs9()
        else:
            filename='BT/1_dh5_prbs9.mod'
            ref= ref_1m_dh5_prbs9()
    elif(rate==2):
        if(data_type==0):
            filename='BT/2_dh1_1010.mod'
            ref= ref_2m_dh1_1010()
        elif(data_type==1):
            filename='BT/2_dh1_prbs9.mod'
            ref= ref_2m_dh1_prbs9()
        else:
            filename='BT/2_dh3_prbs9.mod'
            ref= ref_2m_dh3_prbs9()
    else:
        if(data_type==0):
            filename='BT/3_dh1_1010.mod'
            ref= ref_3m_dh1_1010()
        elif(data_type==1):
            filename='BT/3_dh1_prbs9.mod'
            ref= ref_3m_dh1_prbs9()
        else:
            filename='BT/3_dh3_prbs9.mod'
            ref= ref_3m_dh3_prbs9()
    mem.wr(0x6001103c,0x80000000)
    dat=mem.rd(0x60012000)
    print read_compare(mem_data=dat,reference='ffffffff')
    dat=mem.rd(0x60012004)
    print read_compare(mem_data=dat,reference='ffffffff')
    dat=mem.rd(0x60012008)
    print read_compare(mem_data=dat,reference='ffffffff')
    dat=mem.rd(0x6001200c)
    print read_compare(mem_data=dat,reference='ffffffff')
    print bt_rx_buffer_cmp(ref)

def bt_rx_buffer_cmp(ref):
    errorbits=0
    len_ref=len(ref)/2
    print "ref_len=%d"%len_ref;
    print "rx_len=%d"%(mem.rd(0x3ffe8000)&0xfff);
    for i in range (0,(len(ref)/2)):
        byte=i
        word_offset=byte/4
        byte_offset=byte%4
        content=ref[2*(len_ref-i-1):2*(len_ref-i)]
        errorbits=errorbits + read_compare((mem.rd(0x3ffe8000+4*(word_offset+3))>>(8*byte_offset))&0xff,content)
    return errorbits

def read_compare(mem_data,reference): #return number of error bits
    hex_data=hex(mem_data)
    #print hex_data
    if (len(hex_data)==4) and (hex_data[3]=='L'):
        hex_data= '0'+hex_data[2]
    else:
        hex_data=hex_data[2:4]
    #print hex_data
    len_data=len(hex_data)
    len_ref=len(reference)
    errorbits=0
    if len_data<len_ref:
        for i in range (1,len_ref-len_data+1):
            hex_data='0'+hex_data
    #print len_data
    #print len_ref
    print hex_data
    print reference
    for idx, content in enumerate(hex_data):
        errorbits=errorbits+compare_bits(content,reference[idx])
    return errorbits

def compare_bits(data,reference):
    hex2bits=[  '0000',
                '0001',
                '0010',
                '0011',
                '0100',
                '0101',
                '0110',
                '0111',
                '1000',
                '1001',
                '1010',
                '1011',
                '1100',
                '1101',
                '1110',
                '1111',
                ]
    data=hex2bits[int(data,16)]
    reference=hex2bits[int(reference,16)]
    errorbits=0
    for idx, content in enumerate(data):
        if content!=reference[idx]:
            errorbits=errorbits+1
    return errorbits



def ref_1m_dh1_1010():
    ref='000099F1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD8003FE38FC0038000'
    return  ref

def ref_1m_dh1_prbs9():
    ref='00007A6CE5A8513B2F61AA721884022323AB638951B3E78B72904CE8FBC1FFD8003FE38FC0038000'
    return  ref

def ref_1m_dh5_prbs9():
    ref='0000B78290C42011191D5B1C4A8D9F3C5B94826747DE0FF87B859B7A1CC24575E4B9C0EE9EA502ABEB41BB6B05DF1E69AE345FD2C53180CCAC9FB4937E5A8513B2F61AA721884022323AB638951B3E78B72904CE8FBC1FF0F70B36F439848AEBC97381DD3D4A0557D68376D60BBE3CD35C68BFA58A630199593F6926FCB50A2765EC354E4310804464756C712A367CF16E52099D1F783FE1EE166DE8730915D792E703BA7A940AAFAD06EDAC177C79A6B8D17F4B14C60332B27ED24DF96A144ECBD86A9C86210088C8EAD8E2546CF9E2DCA4133A3EF07FC3DC2CDBD0E6122BAF25CE0774F528155F5A0DDB582EF8F34D71A2FE96298C066564FDA49BF2D4289D97B0D5390C42011191D5B1C4A8D9F3C5B94826747DE0FF87B859B7A1CC24575E4B9C0EE9EA502ABEB41BB6B05DF1E69AE345FD2C53180CCAC9FB4937E5A8513B2F61AA721884022323AB638951B3E78B72904CE8FBC1FF0A98000003F1C01FFE'
    return  ref

def ref_2m_dh1_1010():
    ref='00009847AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA01B0003FE38FC00380'
    return ref

def ref_2m_dh1_prbs9():
    ref='0000F3EC9C0EE9EA502ABEB41BB6B05DF1E69AE345FD2C53180CCAC9FB4937E5A8513B2F61AA721884022323AB638951B3E78B72904CE8FBC1FF01B0003FE38FC00380'
    return ref

def ref_2m_dh3_prbs9():
    ref='00009A18F5A0DDB582EF8F34D71A2FE96298C066564FDA49BF2D4289D97B0D5390C42011191D5B1C4A8D9F3C5B94826747DE0FF87B859B7A1CC24575E4B9C0EE9EA502ABEB41BB6B05DF1E69AE345FD2C53180CCAC9FB4937E5A8513B2F61AA721884022323AB638951B3E78B72904CE8FBC1FF0F70B36F439848AEBC97381DD3D4A0557D68376D60BBE3CD35C68BFA58A630199593F6926FCB50A2765EC354E4310804464756C712A367CF16E52099D1F783FE1EE166DE8730915D792E703BA7A940AAFAD06EDAC177C79A6B8D17F4B14C60332B27ED24DF96A144ECBD86A9C86210088C8EAD8E2546CF9E2DCA4133A3EF07FC3DC2CDBD0E6122BAF25CE0774F528155F5A0DDB582EF8F34D71A2FE96298C066564FDA49BF2D4289D97B0D5390C42011191D5B1C4A8D9F3C5B94826747DE0FF87B859B7A1CC24575E4B9C0EE9EA502ABEB41BB6B05DF1E69AE345FD2C53180CCAC9FB4937E5A8513B2F61AA721884022323AB638951B3E78B72904CE8FBC1FF0B7800001C71C01C70'
    return ref

def ref_3m_dh1_1010():
    ref='00003DEEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA02980007FC0E001C00'
    return ref

def ref_3m_dh1_prbs9():
    ref='0000C3CB0C42011191D5B1C4A8D9F3C5B94826747DE0FF87B859B7A1CC24575E4B9C0EE9EA502ABEB41BB6B05DF1E69AE345FD2C53180CCAC9FB4937E5A8513B2F61AA721884022323AB638951B3E78B72904CE8FBC1FF02980007FC0E001C00'
    return ref

def ref_3m_dh3_prbs9():
    ref='000093EDE69AE345FD2C53180CCAC9FB4937E5A8513B2F61AA721884022323AB638951B3E78B72904CE8FBC1FF0F70B36F439848AEBC97381DD3D4A0557D68376D60BBE3CD35C68BFA58A630199593F6926FCB50A2765EC354E4310804464756C712A367CF16E52099D1F783FE1EE166DE8730915D792E703BA7A940AAFAD06EDAC177C79A6B8D17F4B14C60332B27ED24DF96A144ECBD86A9C86210088C8EAD8E2546CF9E2DCA4133A3EF07FC3DC2CDBD0E6122BAF25CE0774F528155F5A0DDB582EF8F34D71A2FE96298C066564FDA49BF2D4289D97B0D5390C42011191D5B1C4A8D9F3C5B94826747DE0FF87B859B7A1CC24575E4B9C0EE9EA502ABEB41BB6B05DF1E69AE345FD2C53180CCAC9FB4937E5A8513B2F61AA721884022323AB638951B3E78B72904CE8FBC1FF0F70B36F439848AEBC97381DD3D4A0557D68376D60BBE3CD35C68BFA58A630199593F6926FCB50A2765EC354E4310804464756C712A367CF16E52099D1F783FE1EE166DE8730915D792E703BA7A940AAFAD06EDAC177C79A6B8D17F4B14C60332B27ED24DF96A144ECBD86A9C86210088C8EAD8E2546CF9E2DCA4133A3EF07FC3DC2CDBD0E6122BAF25CE0774F528155F5A0DDB582EF8F34D71A2FE96298C066564FDA49BF2D4289D97B0D5390C42011191D5B1C4A8D9F3C5B94826747DE0FF87B859B7A1CC24575E4B9C0EE9EA502ABEB41BB6B05DF1E69AE345FD2C53180CCAC9FB4937E5A8513B2F61AA721884022323AB638951B3E78B72904CE8FBC1FF1140'
    ref=ref+'003F000FC01C7E'
    return ref

def bt_iqv_init(sel='iqview'):
    if sel=='iqview':
       print iqv_serv.init()
       print iqv_serv.open()
    else:
       print iqxel_serv.init()
       print iqxel_serv.open()
def bt_iqv_close():
    print iqv_serv.close()
    print iqv_serv.term()
    print iqxel_serv.close()
    print iqxel_serv.term()

def bt_iqv_tx_stop(sel='iqview'):
    if sel=='iqview':
       print iqv_serv.txenable(0)
    else:
       print iqxel_serv.txenable(0)

def bt_rx_ber_test_alpha(loop=1,rate=1,freq_offset_500k=4,data_type=0,pwrdBm=-15,hec=1,UAP='01101011'):
    if(rate==1):
        if(data_type==0):
            filename='BT/1_dh1_1010.mod'
            ref= ref_1m_dh1_1010()
            bit_len=240+61
        elif(data_type==1):
            filename='BT/1_dh1_prbs9.mod'
            ref= ref_1m_dh1_prbs9()
            bit_len=240+61
        else:
            filename='BT/1_dh5_prbs9.mod'
            ref= ref_1m_dh5_prbs9()
            bit_len=2744+61
    elif(rate==2):
        if(data_type==0):
            filename='BT/2_dh1_1010.mod'
            ref= ref_2m_dh1_1010()
            bit_len=464+57
        elif(data_type==1):
            filename='BT/2_dh1_prbs9.mod'
            ref= ref_2m_dh1_prbs9()
            bit_len=464+57
        else:
            filename='BT/2_dh3_prbs9.mod'
            ref= ref_2m_dh3_prbs9()
            bit_len=2968+57
    else:
        if(data_type==0):
            filename='BT/3_dh1_1010.mod'
            ref= ref_3m_dh1_1010()
            bit_len=61+696-8
        elif(data_type==1):
            filename='BT/3_dh1_prbs9.mod'
            ref= ref_3m_dh1_prbs9()
            bit_len=61+696-8
        else:
            filename='BT/3_dh3_prbs9.mod'
            ref= ref_3m_dh3_prbs9()
            bit_len=61+4448-8
    #bt_iqv_tx_init(filename=filename,pwrdBm=pwrdBm)

    errorbits=0
    totalbits=0
    for i in range(1,loop+1):
        #time.sleep(1)
        bt_rx_start(rate=rate,freq_offset_500k=freq_offset_500k,bit_len=bit_len)
        if(mem.rd(0x6001108c)<16):
            #print iqv_serv.txfrmcnt(framecnt=1)
            if hec==1:
                hec_correct=bt_header_hec(mem.rd(0x60012000),mem.rd(0x60012004),UAP)
            else:
                hec_correct=1
            if hec_correct==1:
                totalbits=totalbits + 32*len(ref)
                errorbits=errorbits + bt_rx_buffer_cmp(ref)

    print "rx total %d bits\nrx error %d bits\nBER %f"%(totalbits, errorbits,float(errorbits)/totalbits)
    #print iqv_serv.txenable(0)

def int2bits(integer):
    hex_data=hex(integer)
    hex_data=hex_data[2:10]
    len_data=len(hex_data)
    rslt=''
    if len_data<8:
        for i in range (1,8-len_data+1):
            hex_data='0'+hex_data
    hex2bits=[  '0000',
                '0001',
                '0010',
                '0011',
                '0100',
                '0101',
                '0110',
                '0111',
                '1000',
                '1001',
                '1010',
                '1011',
                '1100',
                '1101',
                '1110',
                '1111',
                ]
    for idx, content in enumerate(hex_data):
        rslt=rslt+hex2bits[int(content,16)]
    return rslt

def bitsXOR(bits):
    count=0
    for idx, content in enumerate(bits):
        if content=='1':
            count=count+1
    if count%2==0:
        return '0'
    else:
        return '1'

def bt_header_hec(integer0,integer1,UAP):
    header_rcved=int2bits(integer1)+int2bits(integer0)
    header=''
    for i in range (1,19):
        header=header_rcved[63-(1+(i-1)*3)]+header
    print header
    hec0=header[17-2]+header[17-4]+header[17-6]+header[17-8]+header[17-9]+UAP[2]+UAP[4]+UAP[6]
    hec1=header[17-2]+header[17-3]+header[17-4]+header[17-5]+header[17-6]+header[17-7]+header[17-8]+UAP[2]+UAP[3]+UAP[4]+UAP[5]+UAP[6]+UAP[7]
    hec2=header[17-9]+header[17-3]+header[17-4]+header[17-5]+header[17-6]+header[17-7]+header[17-8]+UAP[3]+UAP[4]+UAP[5]+UAP[6]+UAP[7]
    hec3=header[17-0]+header[17-2]+header[17-5]+header[17-7]+UAP[0]+UAP[2]+UAP[5]+UAP[7]
    hec4=header[17-1]+header[17-3]+header[17-6]+header[17-8]+UAP[1]+UAP[3]+UAP[6]
    hec5=header[17-0]+header[17-2]+header[17-4]+header[17-7]+header[17-9]+UAP[0]+UAP[2]+UAP[4]+UAP[7]
    hec6=header[17-9]+header[17-3]+header[17-4]+header[17-5]+header[17-6]+header[17-0]+header[17-1]+header[17-2]+UAP[0]+UAP[1]+UAP[2]+UAP[3]+UAP[4]+UAP[5]+UAP[6]
    hec7=header[17-1]+header[17-3]+header[17-5]+header[17-7]+header[17-8]+header[17-9]+UAP[1]+UAP[3]+UAP[5]+UAP[7]
    hec=bitsXOR(hec7)+bitsXOR(hec6)+bitsXOR(hec5)+bitsXOR(hec4)+bitsXOR(hec3)+bitsXOR(hec2)+bitsXOR(hec1)+bitsXOR(hec0)
    hec_rcved=header[0:8]
    print hec
    print hec_rcved
    if hec==hec_rcved:
        return 1
    else:
        return 0

def bt_tx_sim_debug(chan_id='com'):
    cmdstr="BT_tx_sim_debug ";
    return chn.runcmd(cmdstr,chan_id);

def bt_rx_sim_debug(chan_id='com'):
    cmdstr="BT_rx_sim_debug ";
    return chn.runcmd(cmdstr,chan_id);

def bt_testmode_init(chan_id='com', freq_offset_500k=4, freq=2472, nowhite=0):
    cmdstr="BT_testmode_init %d %d %d"%(freq_offset_500k, freq, nowhite);
    return chn.runcmd(cmdstr,chan_id);

def bt_set_packet_attributes(chan_id='com', type_code=1, link_type=1, payload_header_len=0, payload1_header_len=0, payload_len=0, device_sel=0):
    cmdstr="BT_set_packet_attributes %d %d %d %d %d %d"%(type_code, link_type, payload_header_len, payload1_header_len, payload_len, device_sel);
    return chn.runcmd(cmdstr,chan_id);

def bt_fill_tx_payload(chan_id='com',start_addr=0x3fff0000, payload_header_len=0, payload_len=0):
    # call thie before bt_set_packet_attributes
    word_len= ((payload_header_len+payload_len+2)/4) + 1;
    for i in range (0, word_len):
        content=random.randint(0,0xffffffff);
        mem.wr(start_addr+(4*i),content,chan_id);

def bt_get_a_data_type():
    data_type_seq=(1,2,3,4,9);
    data_type=random.choice(data_type_seq);
    return data_type;

def bt_get_a_packet():
    link_type=random.randint(1,5);
    #link_type=1;
    if link_type==1:
        type_code_seq=(0,1,3,5,6,7,8);
    elif link_type==2:
        type_code_seq=(0,1,7,12,13);
    elif link_type==3:
        type_code_seq=(0,1,7,12,13,6);
    elif link_type==4:
        type_code_seq=(0,1,3,4,9,10,11,14,15);
    elif link_type==5:
        type_code_seq=(0,1,3,4,8,9,10,11,14,15);
    else:
        print "link_type error %d\n"%link_type;
    type_code=random.choice(type_code_seq);

    if link_type==1:
        if type_code==0: # NULL
            payload_header_len=0;
            payload1_header_len=0;
            payload_len=0;
        elif type_code==1: # POLL
            payload_header_len=0;
            payload1_header_len=0;
            payload_len=0;
        elif type_code==2: # FHS
            payload_header_len=0;
            payload1_header_len=0;
            payload_len=18;
        elif type_code==3: # DM1
            payload_header_len=1;
            payload1_header_len=0;
            payload_len=random.randint(0,17);
        elif type_code==5:
            payload_header_len=0;
            payload1_header_len=0;
            payload_len=10;
        elif type_code==6:
            payload_header_len=0;
            payload1_header_len=0;
            payload_len=20;
        elif type_code==7:
            payload_header_len=0;
            payload1_header_len=0;
            payload_len=30;
        elif type_code==8:
            payload_header_len=0;
            payload1_header_len=1;
            payload_len=random.randint(10,19);
        else:
            print "type_code error %d\n"%type_code;
    elif link_type==2:
        if type_code==0: # NULL
            payload_header_len=0;
            payload1_header_len=0;
            payload_len=0;
        elif type_code==1: # POLL
            payload_header_len=0;
            payload1_header_len=0;
            payload_len=0;
        elif type_code==7: # EV3
            payload_header_len=0;
            payload1_header_len=0;
            payload_len=random.randint(1,30);
        elif type_code==12: # EV4
            payload_header_len=0;
            payload1_header_len=0;
            payload_len=random.randint(1,120);
        elif type_code==13: #EV5
            payload_header_len=0;
            payload1_header_len=0;
            payload_len=random.randint(1,180);
        else:
            print "type_code error %d\n"%type_code;
    elif link_type==3:
        if type_code==0: # NULL
            payload_header_len=0;
            payload1_header_len=0;
            payload_len=0;
        elif type_code==1: # POLL
            payload_header_len=0;
            payload1_header_len=0;
            payload_len=0;
        elif type_code==6: # 2EV3
            payload_header_len=0;
            payload1_header_len=0;
            payload_len=random.randint(1,60);
        elif type_code==7: # 3EV3
            payload_header_len=0;
            payload1_header_len=0;
            payload_len=random.randint(1,90);
        elif type_code==12: #2EV5
            payload_header_len=0;
            payload1_header_len=0;
            payload_len=random.randint(1,360);
        elif type_code==13: #3EV5
            payload_header_len=0;
            payload1_header_len=0;
            payload_len=random.randint(1,540);
        else:
            print "type_code error %d\n"%type_code;
    elif link_type==4:
        if type_code==0: # NULL
            payload_header_len=0;
            payload1_header_len=0;
            payload_len=0;
        elif type_code==1: # POLL
            payload_header_len=0;
            payload1_header_len=0;
            payload_len=0;
        elif type_code==2: # FHS
            payload_header_len=0;
            payload1_header_len=0;
            payload_len=18;
        elif type_code==3: # DM1
            payload_header_len=1;
            payload1_header_len=0;
            payload_len=random.randint(0,17);
        elif type_code==4: #DH1
            payload_header_len=1;
            payload1_header_len=0;
            payload_len=random.randint(0,27);
        elif type_code==9: #AUX1
            payload_header_len=1;
            payload1_header_len=0;
            payload_len=random.randint(0,29);
        elif type_code==10: #DM3
            payload_header_len=2;
            payload1_header_len=0;
            payload_len=random.randint(0,121);
        elif type_code==11: #DH3
            payload_header_len=2;
            payload1_header_len=0;
            payload_len=random.randint(0,183);
        elif type_code==14: #DM5
            payload_header_len=2;
            payload1_header_len=0;
            payload_len=random.randint(0,224);
        elif type_code==15: #DH5
            payload_header_len=2;
            payload1_header_len=0;
            payload_len=random.randint(0,339);
        else:
            print "type_code error %d\n"%type_code;
    elif link_type==5:
        if type_code==0: # NULL
            payload_header_len=0;
            payload1_header_len=0;
            payload_len=0;
        elif type_code==1: # POLL
            payload_header_len=0;
            payload1_header_len=0;
            payload_len=0;
        elif type_code==2: # FHS
            payload_header_len=0;
            payload1_header_len=0;
            payload_len=18;
        elif type_code==3: # DM1
            payload_header_len=1;
            payload1_header_len=0;
            payload_len=random.randint(0,17);
        elif type_code==4: #2DH1
            payload_header_len=2;
            payload1_header_len=0;
            payload_len=random.randint(0,54);
        elif type_code==8: #3DH1
            payload_header_len=2;
            payload1_header_len=0;
            payload_len=random.randint(0,83);
        elif type_code==9: #AUX1
            payload_header_len=1;
            payload1_header_len=0;
            payload_len=random.randint(0,29);
        elif type_code==10: #2DH3
            payload_header_len=2;
            payload1_header_len=0;
            payload_len=random.randint(0,367);
        elif type_code==11: #3DH3
            payload_header_len=2;
            payload1_header_len=0;
            payload_len=random.randint(0,552);
        elif type_code==14: #2DH5
            payload_header_len=2;
            payload1_header_len=0;
            payload_len=random.randint(0,679);
        elif type_code==15: #3DH5
            payload_header_len=2;
            payload1_header_len=0;
            payload_len=random.randint(0,1021);
        else:
            print "type_code error %d\n"%type_code;
    return (link_type, type_code, payload_header_len, payload1_header_len, payload_len)

def tx_rx_a_rand_packet(tx_chan_id='com',rx_chan_id='sock'):
    (link_type, type_code, payload_header_len, payload1_header_len, payload_len)=bt_get_a_packet();
    bt_fill_tx_payload(chan_id=tx_chan_id,start_addr=0x3fff0000, payload_header_len=payload_header_len, payload_len=payload_len);
    bt_set_packet_attributes(chan_id=tx_chan_id, type_code=type_code, link_type=link_type, payload_header_len=payload_header_len, payload1_header_len=payload1_header_len, payload_len=payload_len);
    bt_set_packet_attributes(chan_id=rx_chan_id, type_code=type_code, link_type=link_type, payload_header_len=payload_header_len, payload1_header_len=payload1_header_len, payload_len=payload_len);
    bt_rx_sim_debug(rx_chan_id);
    return bt_tx_sim_debug(tx_chan_id)

def tx_rx_rand_test(tx_chan_id='com', rx_chan_id='sock', loop=1):
    bt_testmode_init(chan_id=tx_chan_id);
    bt_testmode_init(chan_id=rx_chan_id);

    for i in range (0,loop):
        rslt=tx_rx_a_rand_packet(tx_chan_id,rx_chan_id);
        if rslt=='0':
            print "tx success\n"
        else :
            print "tx fail\n"
        tx_rx_diff(tx_chan_id=tx_chan_id,rx_chan_id=rx_chan_id);

def tx_rx_diff(tx_chan_id='com', rx_chan_id='sock', tx_base=0x3fff0000, rx_base=0x3ffe8000, tx_len_addr=0x3ff21c44, rx_end_state_addr=0x3ff21c84):
    rslt=0;
    rx_success=mem.rd(rx_end_state_addr,rx_chan_id);
    print "rx: %d"%rx_success;
    if rx_success==0:
        print "rx success!\n";
        tx_len=mem.rd(tx_len_addr, tx_chan_id);
        rx_len_1=mem.rd(rx_base,rx_chan_id);
        rx_len=rx_len_1&0xffff;
        if tx_len!=rx_len:
            print "len mismatch! tx_len=%d, rx_len=%d\n"%(tx_len, rx_len);
        else:
            addr_offset_1=0xffff;
            for i in range (0,tx_len):
                addr_offset=i/4;
                shift=i%4;
                if addr_offset_1!=addr_offset:
                    addr_offset_1=addr_offset;
                    rx_content=mem.rd(rx_base+(4*(2+addr_offset)),rx_chan_id);
                    tx_content=mem.rd(tx_base+(4*(addr_offset)),tx_chan_id);

                if (addr_offset==0) and (shift==1):
                    if (rx_content&0x300)!=(tx_content&0x300):
                        rslt=1;
                else :
                    if shift==0:
                        if (rx_content&0xff)!=(tx_content&0xff):
                            rslt=1;
                    if shift==1:
                        if (rx_content&0xff00)!=(tx_content&0xff00):
                            rslt=1;
                    if shift==2:
                        if (rx_content&0xff0000)!=(tx_content&0xff0000):
                            rslt=1;
                    if shift==3:
                        if (rx_content&0xff000000)!=(tx_content&0xff000000):
                            rslt=1;
            if rslt==0:
                print "match tx rx header and payload!\n";
            else :
                print "mismatch tx rx header and payload!!!\n";
    else:
        print "rx fail!\n";


def inquiry_test(chan_id='com',hoppe_en=0,chan=74):
    cmdstr="BT_inquiry_test %d %d"%(hoppe_en,chan);
    return chn.runcmd(cmdstr,chan_id);


def inquiry_scan_test(chan_id='com',hoppe_en=0,chan=74):
    cmdstr="BT_inquiry_scan_test %d %d"%(hoppe_en,chan);
    return chn.runcmd(cmdstr,chan_id);

def hoppe_init(chan_id='com', tx_offset=2, rx_offset=1, freq_offset=65536-512):
    cmdstr="hoppe_init %d %d %d"%(tx_offset, rx_offset, freq_offset);
    return chn.runcmd(cmdstr,chan_id);

def phy_init(chan_id='com', wifibb=0):
    cmdstr="phy_init %d"%wifibb;
    return chn.runcmd(cmdstr,chan_id);

def freq_offset_cfg(chan_id='com', tx_offset_bb=0, rx_offset_bb=2, tx_offset_hoppe=2,
rx_offset_hoppe=1, cmpx_on=1, cmpx_offset=0, bt_mode_force_en=0, bt_mode_force=0, bt_rx_force_on=0):
    cmdstr="freq_offset_cfg %d %d %d %d %d %d %d %d %d"%(tx_offset_bb, rx_offset_bb, tx_offset_hoppe,
    rx_offset_hoppe, cmpx_on, cmpx_offset, bt_mode_force_en, bt_mode_force, bt_rx_force_on);
    return chn.runcmd(cmdstr,chan_id);


def tx_cfg(chan_id='com', offset=0):
    cmdstr="BT_tx_cfg %d"%offset;
    return chn.runcmd(cmdstr,chan_id);

def set_chan_sw_check(chan_id='com', chan_a=1, chan_b=14, ext=1, enx=0):
    cmdstr="set_chan_sw_check %d %d %d %d"%(chan_a,chan_b,ext,enx);
    return chn.runcmd(cmdstr,chan_id);

def tx_gain(gain=2):
    cmdstr="bt_tx_gain %d"%gain
    return chn.runcmd(cmdstr,chan_id='com');



def con_tx_test(chan_id='com', chan_a=72, chan_b=77, pa_type=1, pla_type=0, pb_type=1, plb_type=0):
    '''
    pa_type: /3 is rate, %3 is slot 1/3/5
    pla_type: 0: 0000, 1: 1111, 2: 1010, 3:
    '''
    cmdstr="BT_con_tx_test %d %d %d %d %d %d"%(chan_a,chan_b,pa_type,pb_type,pla_type,plb_type);
    return chn.runcmd(cmdstr,chan_id);

def page_test(chan_id='com', link_type=5,hoppe_en=1,loopback=1):
    cmdstr="BT_page_test %d %d %d"%(link_type,hoppe_en,loopback);
    return chn.runcmd(cmdstr,chan_id);

def page_scan_test(chan_id='com', link_type=5,hoppe_en=1,loopback=1):
    cmdstr="BT_page_scan_test %d %d %d"%(link_type,hoppe_en,loopback);
    return chn.runcmd(cmdstr,chan_id);

def inq(chan_id='com', hoppe_en=1):
    cmdstr="BT_inq %d"%(hoppe_en);
    return chn.runcmd(cmdstr,chan_id);

def inq_scan(chan_id='com', hoppe_en=1):
    cmdstr="BT_inq_scan %d"%(hoppe_en);
    return chn.runcmd(cmdstr,chan_id);

def page(chan_id='com', hoppe_en=1,mulap=0x11223344,mnap=0x5566,sulap=0xddaabbcc,snap=0xeeff,clock_offset=0):
    cmdstr="BT_page %d %d %d %d %d %d"%(hoppe_en,mulap,mnap,sulap,snap,clock_offset);
    return chn.runcmd(cmdstr,chan_id);

def page_scan(chan_id='com', hoppe_en=1,slave_sel=1):
    cmdstr="BT_page_scan %d %d"%(hoppe_en,slave_sel);
    return chn.runcmd(cmdstr,chan_id);

def cmdstop(chan_id='com'):
    cmdstr="CmdStop ";
    return chn.runcmd(cmdstr,chan_id);

def cmdstatus(chan_id='com'):
    cmdstr="CmdStatus ";
    return chn.runcmd(cmdstr,chan_id);

def test_mode_fill_tx_payload(chan_id='com',lheader=2,lpayload=1,data_type=3,loopback=1, device_sel=0):
    cmdstr="BT_test_mode_fill_tx_payload %d %d %d %d %d"%(lheader,lpayload,data_type,loopback, device_sel);
    return chn.runcmd(cmdstr,chan_id);

def con_loopback_master(chan_id='sock',loopback=1):
    cmdstr="BT_con_loopback_master %d"%loopback;
    return chn.runcmd(cmdstr,chan_id);

def con_loopback_slave(chan_id='sock',link_type=1,loopback=1,payload_len=10,slave_sel=1):
    cmdstr="BT_con_loopback_slave %d %d %d %d"%(link_type,loopback,payload_len,slave_sel);
    return chn.runcmd(cmdstr,chan_id);

def con_loopback(chan_idm='sock',chan_ids='com',slave_sel=1):
    (link_type, type_code, payload_header_len, payload1_header_len, payload_len)=bt_get_a_packet();
    data_type=bt_get_a_data_type();
    test_mode_fill_tx_payload(chan_id=chan_idm,lheader=2+payload_header_len,lpayload=payload_len,data_type=data_type,loopback=0);
    bt_set_packet_attributes(chan_id=chan_idm, type_code=type_code, link_type=link_type, payload_header_len=payload_header_len, payload1_header_len=payload1_header_len, payload_len=payload_len, device_sel= 0);
    con_loopback_slave(chan_id=chan_ids,link_type=link_type,loopback=1,payload_len=payload_len,slave_sel=slave_sel);
    rslt=con_loopback_master(chan_id=chan_idm,loopback=1);
    rslt=rslt.split();
    for idx,item in enumerate(rslt):
        rslt[idx] = int(rslt[idx]);
    return (rslt,link_type,type_code,payload_header_len, payload1_header_len, payload_len);

def discon(chan_idm='sock',chan_ids='com',slave_en=1,master_en=1,slave_device=1):
    if master_en==1:
        cmdstr="BT_m_discon ";
        chn.runcmd(cmdstr,chan_idm);
    if slave_en==1:
        cmdstr="BT_s_discon %d"%slave_device;
        chn.runcmd(cmdstr,chan_ids);


def con(chan_idm='sock',chan_ids='com',slave_en=1,master_en=1,slave_device=1):
    if master_en==1:
        cmdstr="BT_con 0";
        chn.runcmd(cmdstr,chan_idm);
    if slave_en==1:
        cmdstr="BT_con %d"%slave_device;
        chn.runcmd(cmdstr,chan_ids);


def inq_page_con_loopback_test(chan_idm='sock',chan_ids='com', slap='aabbcc',slave_en=1,master_en=1,hoppe_en=1,loop=10,filename="btlog0",slave_sel=1):
    if master_en==1:
        inq(chan_id=chan_idm);
        for i in range (0,10):
            if slave_en==1:
                inq_scan(chan_id=chan_ids);
            for q in range (0,10):
                rslt=cmdstatus(chan_id=chan_idm);
                rslt=rslt.split();
                if rslt[0]=='S':
                    print "nap: 0x%x"%int(rslt[1],16);
                    print "uap: 0x%x"%int(rslt[2],16);
                    print "lap: 0x%x"%int(rslt[3],16);
                    print "lt_addr: 0x%x"%int(rslt[4],16);
                    print "clk27_2: 0x%x"%int(rslt[5],16);
                    print "clkn: 0x%x"%int(rslt[6],16);
                    print "eir: 0x%x"%int(rslt[7],16);
                    print "eir state: 0x%x"%int(rslt[8],16);
                    print "eir first word: 0x%x"%int(rslt[9],16);
                if rslt[0]=='S' :
                #if rslt[0]=='S' and int(rslt[3]) == int('aabbcc',16):
                    print "clk_offset = %d"%(int(rslt[5],16)-(int(rslt[6],16)>>2));

                #if rslt[0]=='S' and int(rslt[3]) == int(slap,16):
                if rslt[0]=='S':
                    nap=int(rslt[1],16);
                    ulap=(int(rslt[2],16)<<24)|int(rslt[3],16);
                    clk27_2=int(rslt[5],16);
                    clkn=int(rslt[6],16);
                    clk_offset=(clk27_2-(clkn>>2))*4;
                    if clk_offset<0:
                        clk_offset= (1<<28)+clk_offset;
                    break;
            if slave_en==1:
                cmdstop(chan_id=chan_ids);
        cmdstop(chan_id=chan_idm);
        print"nap: 0x%x"%nap;
        print"ulap: 0x%x"%ulap;
        print"clk_offset: 0x%x"%clk_offset;
    else:
        inq_scan(chan_id=chan_ids);
        time.sleep(10);
        cmdstop(chan_id=chan_ids);
    if slave_en==1:
        page_scan(chan_id=chan_ids,hoppe_en=hoppe_en,slave_sel=slave_sel);
    if master_en==1:
        page(chan_id=chan_idm, hoppe_en=hoppe_en,mulap=0x11223344,mnap=0x5566,sulap=ulap,snap=nap,clock_offset=clk_offset);
    #time.sleep(0.1);
    #time.sleep(1);
    if slave_en==1:
        sstatus=cmdstatus(chan_id=chan_ids);
        ts=0;
        while sstatus != '0' and sstatus != '1':
            ts=ts+1;
            sstatus=cmdstatus(chan_id=chan_ids);
            if ts>100:
                sstatus=cmdstop(chan_id=chan_ids);
                while sstatus != '0' and sstatus != '1':
                    sstatus=cmdstop(chan_id=chan_ids);
        #mem.rd(0x3ff21c4c,chan_ids); // page end status
    if master_en==1:
        mstatus=cmdstatus(chan_id=chan_idm);
        while mstatus != '0' and mstatus != '1':
            mstatus=cmdstatus(chan_id=chan_idm);
            ts=ts+1;
            if (ts>100) or (sstatus==1):
                mstatus=cmdstop(chan_id=chan_idm);
                while mstatus != '0' and mstatus != '1':
                    mstatus=cmdstop(chan_id=chan_idm);
    #discon(chan_idm=chan_idm,chan_ids=chan_ids,slave_en=1,master_en=1);
    if (mstatus == '0') and (sstatus == '0'):
        #for i in range (0,20):
            #rslt=con_loopback(chan_idm=chan_idm,chan_ids=chan_ids);
            #print"%d %d %d %d %d %d" %(rslt[0][0],rslt[1],rslt[2],rslt[3],rslt[4],rslt[5]);
            #cmdstatus(chan_id=chan_ids);
        packet_sweep_print(chan_idm=chan_idm,chan_ids=chan_ids,loop=loop, filename=filename,slave_sel=slave_sel);
    discon(chan_idm=chan_idm,chan_ids=chan_ids,slave_en=1,master_en=1);


def inq_page_con2_loopback_test(chan_idm='sock',chan_ids='com', slap='aabbcc',slave_en=1,master_en=1,hoppe_en=1,loop=10,filename="btlog0"):
    slave_sel=1;
    if master_en==1:
        inq(chan_id=chan_idm);
        for i in range (0,10):
            if slave_en==1:
                inq_scan(chan_id=chan_ids);
            for q in range (0,10):
                rslt=cmdstatus(chan_id=chan_idm);
                rslt=rslt.split();
                if rslt[0]=='S':
                    print "nap: 0x%x"%int(rslt[1],16);
                    print "uap: 0x%x"%int(rslt[2],16);
                    print "lap: 0x%x"%int(rslt[3],16);
                    print "lt_addr: 0x%x"%int(rslt[4],16);
                    print "clk27_2: 0x%x"%int(rslt[5],16);
                    print "clkn: 0x%x"%int(rslt[6],16);
                    print "eir: 0x%x"%int(rslt[7],16);
                    print "eir state: 0x%x"%int(rslt[8],16);
                    print "eir first word: 0x%x"%int(rslt[9],16);
                if rslt[0]=='S' :
                #if rslt[0]=='S' and int(rslt[3]) == int('aabbcc',16):
                    print "clk_offset = %d"%(int(rslt[5],16)-(int(rslt[6],16)>>2));

                #if rslt[0]=='S' and int(rslt[3]) == int(slap,16):
                if rslt[0]=='S':
                    nap=int(rslt[1],16);
                    ulap=(int(rslt[2],16)<<24)|int(rslt[3],16);
                    clk27_2=int(rslt[5],16);
                    clkn=int(rslt[6],16);
                    clk_offset=(clk27_2-(clkn>>2))*4;
                    if clk_offset<0:
                        clk_offset= (1<<28)+clk_offset;
                    break;
            if slave_en==1:
                cmdstop(chan_id=chan_ids);
        cmdstop(chan_id=chan_idm);
        print"nap: 0x%x"%nap;
        print"ulap: 0x%x"%ulap;
        print"clk_offset: 0x%x"%clk_offset;
    else:
        inq_scan(chan_id=chan_ids);
        time.sleep(10);
        cmdstop(chan_id=chan_ids);

#pico 1
    mstatus='1';
    sstatus='1';
    if slave_en==1:
        page_scan(chan_id=chan_ids,hoppe_en=hoppe_en,slave_sel=slave_sel);
    if master_en==1:
        page(chan_id=chan_idm, hoppe_en=hoppe_en,mulap=0x11223344,mnap=0x5566,sulap=ulap,snap=nap,clock_offset=clk_offset);
    #time.sleep(0.1);
    #time.sleep(1);
    if slave_en==1:
        sstatus=cmdstatus(chan_id=chan_ids);
        ts=0;
        while sstatus != '0' and sstatus != '1':
            ts=ts+1;
            sstatus=cmdstatus(chan_id=chan_ids);
            if ts>100:
                sstatus=cmdstop(chan_id=chan_ids);
                while sstatus != '0' and sstatus != '1':
                    sstatus=cmdstop(chan_id=chan_ids);
        #mem.rd(0x3ff21c4c,chan_ids); // page end status
    if master_en==1:
        mstatus=cmdstatus(chan_id=chan_idm);
        while mstatus != '0' and mstatus != '1':
            mstatus=cmdstatus(chan_id=chan_idm);
            ts=ts+1;
            if (ts>100) or (sstatus==1):
                mstatus=cmdstop(chan_id=chan_idm);
                while mstatus != '0' and mstatus != '1':
                    mstatus=cmdstop(chan_id=chan_idm);
    if (mstatus == '0') and (sstatus == '0'):
        pico1=1;
    else:
        pico1=0;
    discon(chan_idm=chan_idm,chan_ids=chan_ids,slave_en=1,master_en=1,slave_device=slave_sel);

#pico 2
    mstatus='1';
    sstatus='1';
    slave_sel=2;
    if slave_en==1:
        page_scan(chan_id=chan_ids,hoppe_en=hoppe_en,slave_sel=slave_sel);
    if master_en==1:
        page(chan_id=chan_idm, hoppe_en=hoppe_en,mulap=0x11223344,mnap=0x5566,sulap=ulap,snap=nap,clock_offset=clk_offset);
    #time.sleep(0.1);
    #time.sleep(1);
    if slave_en==1:
        sstatus=cmdstatus(chan_id=chan_ids);
        ts=0;
        while sstatus != '0' and sstatus != '1':
            ts=ts+1;
            sstatus=cmdstatus(chan_id=chan_ids);
            if ts>100:
                sstatus=cmdstop(chan_id=chan_ids);
                while sstatus != '0' and sstatus != '1':
                    sstatus=cmdstop(chan_id=chan_ids);
        #mem.rd(0x3ff21c4c,chan_ids); // page end status
    if master_en==1:
        mstatus=cmdstatus(chan_id=chan_idm);
        while mstatus != '0' and mstatus != '1':
            mstatus=cmdstatus(chan_id=chan_idm);
            ts=ts+1;
            if (ts>100) or (sstatus==1):
                mstatus=cmdstop(chan_id=chan_idm);
                while mstatus != '0' and mstatus != '1':
                    mstatus=cmdstop(chan_id=chan_idm);
    if (mstatus == '0') and (sstatus == '0'):
        pico2=1;
    else:
        pico2=0;
    discon(chan_idm=chan_idm,chan_ids=chan_ids,slave_en=1,master_en=1,slave_device=slave_sel);

    if pico2==1:
        con(chan_idm=chan_idm,chan_ids=chan_ids,slave_device=2);
        packet_sweep_print(chan_idm=chan_idm,chan_ids=chan_ids,loop=loop, filename=filename,slave_sel=2);
        discon(chan_idm=chan_idm,chan_ids=chan_ids,slave_en=1,master_en=1,slave_device=2);
    if pico1==1:
        con(chan_idm=chan_idm,chan_ids=chan_ids,slave_device=1);
        packet_sweep_print(chan_idm=chan_idm,chan_ids=chan_ids,loop=loop, filename=filename,slave_sel=1);
        discon(chan_idm=chan_idm,chan_ids=chan_ids,slave_en=1,master_en=1,slave_device=1);


def inq_test(chan_idm='sock',chan_ids='com', slap='aabbcc',slave_en=1,master_en=1,hoppe_en=1,loop=10,filename="btlog0",slave_sel=1):
    if master_en==1:
        inq(chan_id=chan_idm,hoppe_en=hoppe_en);
        for i in range (0,100):
            if slave_en==1:
                inq_scan(chan_id=chan_ids,hoppe_en=hoppe_en);
            for q in range (0,10):
                rslt=cmdstatus(chan_id=chan_idm);
                rslt=rslt.split();
                if rslt[0]=='S':
                    print "nap: 0x%x"%int(rslt[1],16);
                    print "uap: 0x%x"%int(rslt[2],16);
                    print "lap: 0x%x"%int(rslt[3],16);
                    print "lt_addr: 0x%x"%int(rslt[4],16);
                    print "clk27_2: 0x%x"%int(rslt[5],16);
                    print "clkn: 0x%x"%int(rslt[6],16);
                    print "eir: 0x%x"%int(rslt[7],16);
                    print "eir state: 0x%x"%int(rslt[8],16);
                    print "eir first word: 0x%x"%int(rslt[9],16);
                if rslt[0]=='S' :
                #if rslt[0]=='S' and int(rslt[3]) == int('aabbcc',16):
                    print "clk_offset = %d"%(int(rslt[5],16)-(int(rslt[6],16)>>2));

                #if rslt[0]=='S' and int(rslt[3]) == int(slap,16):
                if rslt[0]=='S':
                    nap=int(rslt[1],16);
                    ulap=(int(rslt[2],16)<<24)|int(rslt[3],16);
                    clk27_2=int(rslt[5],16);
                    clkn=int(rslt[6],16);
                    clk_offset=(clk27_2-(clkn>>2))*4;
                    if clk_offset<0:
                        clk_offset= (1<<28)+clk_offset;
                    break;
            if slave_en==1:
                cmdstop(chan_id=chan_ids);
        cmdstop(chan_id=chan_idm);
        print"nap: 0x%x"%nap;
        print"ulap: 0x%x"%ulap;
        print"clk_offset: 0x%x"%clk_offset;
    else:
        inq_scan(chan_id=chan_ids);
        time.sleep(10);
        cmdstop(chan_id=chan_ids);
    if slave_en==1:
        page_scan(chan_id=chan_ids,hoppe_en=hoppe_en,slave_sel=slave_sel);
    if master_en==1:
        page(chan_id=chan_idm, hoppe_en=hoppe_en,mulap=0x11223344,mnap=0x5566,sulap=ulap,snap=nap,clock_offset=clk_offset);
    time.sleep(0.1);
    #time.sleep(1);
    if slave_en==1:
        sstatus=cmdstatus(chan_id=chan_ids);
        ts=0;
        while sstatus != '0' and sstatus != '1':
            ts=ts+1;
            sstatus=cmdstatus(chan_id=chan_ids);
            if ts>100:
                sstatus=cmdstop(chan_id=chan_ids);
                while sstatus != '0' and sstatus != '1':
                    sstatus=cmdstop(chan_id=chan_ids);
        #mem.rd(0x3ff21c4c,chan_ids); // page end status
    if master_en==1:
        mstatus=cmdstatus(chan_id=chan_idm);
        while mstatus != '0' and mstatus != '1':
            mstatus=cmdstatus(chan_id=chan_idm);
            ts=ts+1;
            if (ts>100) or (sstatus==1):
                mstatus=cmdstop(chan_id=chan_idm);
                while mstatus != '0' and mstatus != '1':
                    mstatus=cmdstop(chan_id=chan_idm);
    discon(chan_idm=chan_idm,chan_ids=chan_ids,slave_en=1,master_en=1);


def ipcipc(chan_idm='sock',chan_ids='com', slap='aabbcc',slave_en=1,master_en=1,hoppe_en=1,loop=10,filename="ipcipc"):
    inq_page_con_loopback_test(chan_idm=chan_idm,chan_ids=chan_ids, slap=slap,slave_en=slave_en,master_en=master_en,hoppe_en=hoppe_en,loop=loop,filename=filename,slave_sel=1)
    discon(chan_idm=chan_idm,chan_ids=chan_ids,slave_en=1,master_en=1);
    inq_page_con_loopback_test(chan_idm=chan_idm,chan_ids=chan_ids, slap=slap,slave_en=slave_en,master_en=master_en,hoppe_en=hoppe_en,loop=loop,filename=filename,slave_sel=2)

def packet_sweep_print(chan_idm='sock',chan_ids='com',loop=10, filename="bt_log0",slave_sel=1):
    lineone="link type,type code,m tx error,m BTRX_BB_ERR0 0x1,m BTRX_BB_ERR1 0x2,m BTRX_BB_ERR2 03,m BTRX_AC_TO_FORCE 0x38,m BTRX_AC_TO 0x39,m BTRX_AC_TO_NO 0x43,m BTRX_FRBB_OVERFLOW 0x44,m BTRX_LEN_ERR 0x42,m BTRX_HEC_ERR 0x40,m BTRX_CRC_ERR 0x41,m BTRX_DEFEC13_ERR 0x45,m BTRX_DEFEC23_ERR 0x46,m BTRX_TYPE_ERR 0x47,s BTRX_BB_ERR0 0x1,s BTRX_BB_ERR1 0x2,s BTRX_BB_ERR2 03,s BTRX_AC_TO_FORCE 0x38,s BTRX_AC_TO 0x39,s BTRX_AC_TO_NO 0x43,s BTRX_FRBB_OVERFLOW 0x44,s BTRX_LEN_ERR 0x42,s BTRX_HEC_ERR 0x40,s BTRX_CRC_ERR 0x41,s BTRX_DEFEC13_ERR 0x45,s BTRX_DEFEC23_ERR 0x46,s BTRX_TYPE_ERR 0x47,ste,length mismatch,error bits,total bits in error bits packet,fail,total";
    matrix=[];
    for i in range(loop):
        #print matrix;
        (rsltm,link_type,type_code,payload_header_len, payload1_header_len, payload_len)=con_loopback(chan_idm=chan_idm,chan_ids=chan_ids,slave_sel=slave_sel);
        rslts=cmdstatus(chan_id=chan_ids);
        rslts = rslts.split();
        for idx,item in enumerate(rslts):
            rslts[idx]=int(item);
        print rslts;
        if i==0:
            matrix=packet_sweep_print_append(matrix,rslts,rsltm,link_type,type_code,payload_header_len, payload1_header_len, payload_len);
        else :
            matrix=packet_sweep_print_update(matrix,rslts,rsltm,link_type,type_code,payload_header_len, payload1_header_len, payload_len);
    createlog(filename,'csv');
    writelog(lineone);
    for idx,content in enumerate(matrix):
        line="";
        for indx,ctt in enumerate(content):
            line=line+("%d,"%ctt);
        writelog(line);
    closelog();


def packet_sweep_print_line_update(line,rslts,rsltm,link_type,type_code,payload_header_len, payload1_header_len, payload_len):
    myline=line;
    if rsltm[0]==3:
        myline[2]=line[2]+1;
    elif rsltm[0]==4:
        if rsltm[1]==1:
            myline[3]=line[3]+1;
        elif rsltm[1]==2:
            myline[4]=line[4]+1;
        elif rsltm[1]==3:
            myline[5]=line[5]+1;
        elif rsltm[1]==38:
            myline[6]=line[6]+1;
        elif rsltm[1]==39:
            myline[7]=line[7]+1;
        elif rsltm[1]==43:
            myline[8]=line[8]+1;
        elif rsltm[1]==44:
            myline[9]=line[9]+1;
        elif rsltm[1]==42:
            myline[10]=line[10]+1;
        elif rsltm[1]==40:
            myline[11]=line[11]+1;
        elif rsltm[1]==41:
            myline[12]=line[12]+1;
        elif rsltm[1]==45:
            myline[13]=line[13]+1;
        elif rsltm[1]==46:
            myline[14]=line[14]+1;
        elif rsltm[1]==47:
            myline[15]=line[15]+1;
    elif rsltm[0]==2:
        myline[31]=line[31]+rsltm[1];
        myline[32]=line[32]+((payload_len+2+payload_header_len)*8);
    elif rsltm[0]==1:
        myline[30]=line[30]+1;
    if rslts[0]==1:
        if rslts[1]==1:
            myline[3+13]=line[3+13]+1;
        elif rslts[1]==2:
            myline[4+13]=line[4+13]+1;
        elif rslts[1]==3:
            myline[5+13]=line[5+13]+1;
        elif rslts[1]==38:
            myline[6+13]=line[6+13]+1;
        elif rslts[1]==39:
            myline[7+13]=line[7+13]+1;
        elif rslts[1]==43:
            myline[8+13]=line[8+13]+1;
        elif rslts[1]==44:
            myline[9+13]=line[9+13]+1;
        elif rslts[1]==42:
            myline[10+13]=line[10+13]+1;
        elif rslts[1]==40:
            myline[11+13]=line[11+13]+1;
        elif rslts[1]==41:
            myline[12+13]=line[12+13]+1;
        elif rslts[1]==45:
            myline[13+13]=line[13+13]+1;
        elif rslts[1]==46:
            myline[14+13]=line[14+13]+1;
        elif rslts[1]==47:
            myline[15+13]=line[15+13]+1;
    elif rslts[0]==2:
        myline[29]=line[29]+1;
    if (rslts[0]!=0) or (rsltm[0]!=0):
            myline[33]=line[33]+1;
    myline[34]=line[34]+1;
    return myline;

def packet_sweep_print_append(matrix,rslts,rsltm,link_type,type_code,payload_header_len, payload1_header_len, payload_len):
    mtx=matrix;
    line=[0 for i in range(35)];
    line[0]=link_type;
    line[1]=type_code;
    line=packet_sweep_print_line_update(line,rslts,rsltm,link_type,type_code,payload_header_len, payload1_header_len, payload_len);
    mtx.append(line);
    return mtx;

def packet_sweep_print_update(matrix,rslts,rsltm,link_type,type_code,payload_header_len, payload1_header_len, payload_len):
    find=0;
    mtx=matrix;
    for idx,content in enumerate(mtx):
        if(content[0]==link_type) and (content[1]==type_code):
            line=packet_sweep_print_line_update(content,rslts,rsltm,link_type,type_code,payload_header_len, payload1_header_len, payload_len);
            mtx[idx]=line;
            find=1;
            break;
    if find==0:
        mtx=packet_sweep_print_append(mtx,rslts,rsltm,link_type,type_code,payload_header_len, payload1_header_len, payload_len);
    return mtx;


# LE ###
def LE_start_tx(chan_id='com',channel=74,data_type=0,loop=1):
    cmdstr="LE_start_tx %d %d %d"%(channel,data_type,loop);
    return chn.runcmd(cmdstr,chan_id);


# test mode

def prbs9_test(chan_id='com'):
    cmdstr="prbs9_test ";
    return chn.runcmd(cmdstr,chan_id);


def le_rx_per(chan_id='com', chan=72):
    cmdstr="LE_rx_per %d"%chan;
    return chn.runcmd(cmdstr,chan_id);


def le_rx_per_test(framecnt=1000, filename='LETestRun1a.mod',pwrdBm=-15,freq=2472, atten=0,port='right'):
    filename='BT/LEwaveforms/DirtyPackets/'+filename
    bt_iqv_tx_init(filename=filename,pwrdBm=pwrdBm+atten,freqMHz=freq, port=port)

    errorbits=0
    totalbits=0
    loop=0

    le_rx_per( chan=freq-2402)
    print iqv_serv.txfrmcnt(framecnt=framecnt)


    result=cmdstop()
    print iqv_serv.txenable(0)

    result=result.split()
    totalp=int(result[0],16)
    cp=int(result[1],16)
    RSSI=0 - int(result[15],16)
    noise=float(((int(result[16],16)&0x3ff)-1024))/4
    noise_1m_min=0 - int(result[17],16)
    noise_1m_average= 0 - int(result[18],16)
    PER=1-(float(cp)/framecnt)
    print "tx total pac %d\nrx total pac %d     rx correct pac %d\nPER %f\n"%(framecnt, totalp, cp, PER)
    return [totalp, cp , RSSI, noise, noise_1m_min, noise_1m_average]


def le_rx_per_sweep(framecnt=1000,file_name='LETestRun1a.mod',pwrdBm_start=-70,pwrdBm_end=-50,chan_start=72,chan_end=78, file_w = '../bt_rx_per_',atten=0, port='right'):
    trange="pwr%d_%d_chan%d_%d_"%(pwrdBm_start, pwrdBm_end, chan_start, chan_end)
    f=open(file_w+trange+file_name+'.csv', 'w')
    f.write('Channel,TX power,TX pac,RX pac,RX correct pac,PER,AER,PER RX pac,RSSI,noise, noise 1m floor, noise 1m average\n')
    freq= chan_start+2402
    freq_end= chan_end + 2402
    framecnt_est=framecnt+5
    while freq<=freq_end:
        pwrdBm=pwrdBm_start
        while pwrdBm<=pwrdBm_end:
            f.write("%dMHz,"%freq)
            f.write("%ddBm,"%pwrdBm)
            [total_pac,cpac,RSSI,noise, noise_1m_min, noise_1m_average]=le_rx_per_test(framecnt=framecnt,filename=file_name,pwrdBm=pwrdBm, freq=freq, atten=atten,port=port)
            pwrdBm=pwrdBm+1
            PER=1-(float(cpac)/framecnt_est)
            AER=1-(float(total_pac)/framecnt_est)
            PER_rx_pac=1
            if(total_pac!=0):
                PER_rx_pac=1-(float(cpac)/total_pac)
            f.write("%d,%d,%d,%f,%f,%f,%f,%f,%f,%f\n"%(framecnt_est,total_pac,cpac,PER,AER,PER_rx_pac,RSSI,noise, noise_1m_min, noise_1m_average))
        freq=freq+1
    f.close



def le_rx_ber(chan_id='com', bits=1600000, chan=72):
    cmdstr="LE_rx_ber %d %d"%(bits, chan);
    return chn.runcmd(cmdstr,chan_id);

def le_rx_ber_test(basebits=16000,rate=1,filename='LETestRun1a.mod',pwrdBm=-15,freq=2472, atten=0):
    filename='BT/LEwaveforms/DirtyPackets/'+filename
    bt_iqv_tx_init(filename=filename,pwrdBm=pwrdBm+atten,freqMHz=freq)

    errorbits=0
    totalbits=0
    loop=0

    print iqv_serv.txfrmcnt(framecnt=0)

    result=le_rx_ber(bits=basebits, chan=freq-2402)
    print iqv_serv.txenable(0)

    result=result.split()
    totalbits=int(result[0],16)
    errorbits=int(result[1],16)
    RSSI=0-int(result[3],16)
    noise=float(((int(result[4],16)&0x3ff)-1024))/4
    np=int(result[6],16)
    cp=int(result[7],16)
    crc=int(result[8],16)
    ecp=int(result[9],16)
    if(totalbits==0):
        BER=1
    elif(errorbits==0):
        BER=0
    else:
        BER=float(errorbits)/totalbits
    print "rx total %d bits\nrx error %d bits\nBER %f"%(totalbits, errorbits,BER)
    print iqv_serv.txenable(0)
    return [totalbits, errorbits,RSSI,noise, np, cp, crc, ecp]




def le_rx_sensitivity_test(basebits=16000,file_name='LETestRun1a.mod',pwrdBm_start=-70,pwrdBm_end=-50,chan_start=72,chan_end=78, file_w = '../bt_rx_sensitivity_',atten=0):
    trange="pwr%d_%d_chan%d_%d_"%(pwrdBm_start, pwrdBm_end, chan_start, chan_end)
    f=open(file_w+trange+file_name+'.csv', 'w')
    freq= chan_start+2402
    freq_end= chan_end + 2402
    while freq<=freq_end:
        f.write("\n%dMHz\n"%freq)
        f.write('RX power est, BER, RSSI, noise, np, cp, crc, ecp\n')

        pwrdBm=pwrdBm_start
        while pwrdBm<=pwrdBm_end:
            f.write('%ddBm,'%pwrdBm)
            [total_bits,error_bits,RSSI,noise, np, cp, crc, ecp]=le_rx_ber_test(basebits=basebits,filename=file_name,pwrdBm=pwrdBm, freq=freq, atten=atten)
            pwrdBm=pwrdBm+1
            if(total_bits==0):
        	    BER=1
            elif(error_bits==0):
        	    BER=0
            else:
                BER=float(error_bits)/total_bits
            f.write("%f,%f,%f,%d,%d,%d,%d\n"%(BER,RSSI,noise, np, cp, crc, ecp))
        freq=freq+1
    f.close


def bt_rx_noise(chan=66, n=10):
    cmdstr="BT_rx_noise %d %d"%(chan, n);
    rslt=chn.runcmd(cmdstr,'com');
    rslt=rslt.split()
    noise_min=0 - int(rslt[0],16)
    noise_average=0 - int(rslt[1],16)
    noise_filted=0 - int(rslt[2],16)
    noise_fb=0 - int(rslt[3],16)

    print "noise min %f    moise average %f  noise filted %f    noise fb %f\n"%( noise_min,noise_average,noise_filted,noise_fb)

def uart_loop(n=100):
    if com.ser.isOpen()==False:
        logerror('Com is not open!')
        return ''
    loop=0
    odd=1
    com.ser.timeout=0.1
    com.ser.flushInput()
    com.ser.flushOutput()
    while loop<n:
      com.ser.write(chr(loop))
      loop=loop+1
      com.ser.write(chr(loop))
      print "send %x%x"%(loop-1,loop)
      a=com.ser.read(size=1)
      b=com.ser.read(size=1)
      if a != "":
         print "get %x%x"%(ord(a),ord(b))
      loop=loop+1
      odd=(~odd)&1

def le_dtm_cmd_print(cmd=0):
    cmd=cmd>>14
    if cmd==0 :
        print "LE DTM reset"

    elif cmd==1 :
        print "LE DTM RX test"
    elif cmd==2 :
        print "LE DTM TX test"
    else:
        print "LE DTM test end"

def le_dtm_event_print(a=0,b=0):
    print "%x%x"%(a,b)
    event=a>>7
    if event==0 :
        if (b&1)==0:
            print "LE DTM status success"
        else :
            print "LE DTM status error"
    else :
        count= ((a&0x7f)<<8) | b
        print "LE DTM report %d"%count;

def le_dtm_tx(freq=0, len=30, type=0):
    if com.ser.isOpen()==False:
        logerror('Com is not open!')
        return ''
    com.ser.timeout=0.04
    com.ser.flushInput()
    com.ser.flushOutput()
    cmd= (2<<14) | ((freq&0x3f)<<8) | ((len&0x3f)<<2) | (type&0x3)
    print cmd>>8
    com.ser.write(chr(cmd>>8))
    com.ser.write(chr(cmd&0xff))
    a=ord(com.ser.read(size=1))
    b=ord(com.ser.read(size=1))
    le_dtm_event_print(a,b)

def le_dtm_test_end():
    if com.ser.isOpen()==False:
        logerror('Com is not open!')
        return ''
    com.ser.timeout=0.04
    com.ser.flushInput()
    com.ser.flushOutput()
    cmd= (3<<14)
    com.ser.write(chr(cmd>>8))
    com.ser.write(chr(cmd&0xff))
    a=ord(com.ser.read(size=1))
    b=ord(com.ser.read(size=1))
    le_dtm_event_print(a,b)

def le_dtm_rx(freq=0):
    if com.ser.isOpen()==False:
        logerror('Com is not open!')
        return ''
    com.ser.timeout=0.04
    com.ser.flushInput()
    com.ser.flushOutput()
    cmd= (1<<14) | ((freq&0x3f)<<8)
    com.ser.write(chr(cmd>>8))
    com.ser.write(chr(cmd&0xff))
    a=ord(com.ser.read(size=1))
    b=ord(com.ser.read(size=1))
    le_dtm_event_print(a,b)

def le_dtm_rx_iqv(file_name='LETestRun4a.mod', framecnt=1000,pwrdBm=-70,chan=0, atten=21, port='left'):
    filename='BT/LEwaveforms/DirtyPackets/'+file_name
    bt_iqv_tx_init(filename=filename,pwrdBm=pwrdBm+atten,freqMHz=(chan*2)+2402, port=port)

    le_dtm_rx(freq=chan)
    iqv_serv.txfrmcnt(framecnt=framecnt)
    le_dtm_test_end()
    iqv_serv.txenable(0)

def DUT_CMPLX_FLT():
    cmdstr="DUT_CMPLX_FLT";
    rslt=chn.runcmd(cmdstr,'com');

def DUT_BOOST_CONSECT(cnt=5):
    cmdstr="DUT_BOOST_CONSECT %d"%cnt;
    rslt=chn.runcmd(cmdstr,'com');

def DUT_BOOST():
    cmdstr="DUT_BOOST";
    rslt=chn.runcmd(cmdstr,'com');

def BT_TM_DUT():
    cmdstr="BT_TM_DUT";
    rslt=chn.runcmd(cmdstr,'com');

def LE_DTM():
    cmdstr="LE_DTM";
    rslt=chn.runcmd(cmdstr,'com');



def per_cmpxfilter_sweep(directory="../per/", dcap_s=108,dcap_e=30, step=1, framecnt=5000,rate=1,file_name='1_dh1_1010.mod',
pwrdBm_start=-70,pwrdBm_end=-50,chan_start=72,chan_end=78, atten=23,save_name=''):
    dname=file_name+"_dcap%d_%d_pwr%d_%d_chan%d_%d"%(dcap_s,dcap_e,pwrdBm_start, pwrdBm_end, chan_start, chan_end)+save_name
    dname=directory+dname
    if(not(os.path.exists(dname))):
        os.makedirs(dname)
    if(dcap_e<dcap_s):
        step=-step
    else:
        step=step
    dcap=dcap_s
    while(dcap!=(dcap_e+step)):
        i2c.wic("bbtop", "filter_btrx_dcap_lq",dcap)
        i2c.wic("bbtop", "filter_btrx_dcap_hq",dcap)
        bt_rx_per_sweep(framecnt=framecnt,rate=rate,file_name=file_name,pwrdBm_start=pwrdBm_start,pwrdBm_end=pwrdBm_end,chan_start=chan_start,chan_end=chan_end, file_w = dname+"/dcap%d_pwr%d_%d_chan%d_%d_"%(dcap,pwrdBm_start, pwrdBm_end, chan_start, chan_end),atten=atten)
        dcap=dcap+step


def ber_cmpxfilter_sweep(directory="../ber/", dcap_s=108,dcap_e=30, step=1, basebits=16000,rate=1,file_name='1_dh1_1010.mod',
pwrdBm_start=-70,pwrdBm_end=-50,chan_start=72,chan_end=78,atten=23):
    dname=file_name+"_dcap%d_%d_pwr%d_%d_chan%d_%d/"%(dcap_s,dcap_e,pwrdBm_start, pwrdBm_end, chan_start, chan_end)
    dname=directory+dname
    if(not(os.path.exists(dname))):
        os.makedirs(dname)
    if(dcap_e<dcap_s):
        step=-step
    else:
        step=step
    dcap=dcap_s
    while(dcap!=(dcap_e+step)):
        i2c.wic("bbtop", "filter_btrx_dcap_lq",dcap)
        i2c.wic("bbtop", "filter_btrx_dcap_hq",dcap)
        bt_rx_sensitivity_test(basebits=basebits,rate=rate,file_name=file_name,pwrdBm_start=pwrdBm_start,pwrdBm_end=pwrdBm_end,chan_start=chan_start,chan_end=chan_end, file_w = dname+"/dcap%d_pwr%d_%d_chan%d_%d_"%(dcap,pwrdBm_start, pwrdBm_end, chan_start, chan_end),atten=atten)
        dcap=dcap+step


def bt_rx_per_test_ci(framecnt=1000, rate=1,filename='1_dh1_prbs9.mod',pwrdBm=-15,UAP='01101011',freq=2472, chan=38, atten=0, port='left'):
    filename='BT/new/'+filename
    bt_iqv_tx_init(filename=filename,pwrdBm=pwrdBm+atten,freqMHz=freq,port=port)

    if rate==1 :
        link_type=4
    else :
        link_type=5

    errorbits=0
    totalbits=0
    loop=0

    bt_rx_per(link_type=link_type, chan=chan)
    print iqv_serv.txfrmcnt(framecnt=framecnt)


    result=cmdstop()
    print iqv_serv.txenable(0)

    result=result.split()
    totalp=int(result[0],16)
    cp=int(result[1],16)
    PER=1-(float(cp)/framecnt)
    RSSI=0-int(result[24],16)
    noise=float(((int(result[25],16)&0x3ff)-1024))/4

    pwr_ib=int(result[26],16)
    pwr_fb=int(result[27],16)
    gain=int(result[28],16)
    if(totalp!=0):
        pwr_ib=0-(float(pwr_ib)/totalp)
        pwr_fb=0-(float(pwr_fb)/totalp)
        gain=float(gain)/totalp
    hec_ep=int(result[2],16)
    crc_ep=int(result[3],16)
    type_ep=int(result[4],16)

    pwr_ibm_w_ep=int(result[15],16)
    pwr_fbm_w_ep=int(result[16],16)

    pwr_r_free_w_ep=int(result[17],16)
    pwr_r_ac_w_ep=int(result[18],16)
    pwr_r_pac_w_ep=int(result[19],16)
    pwr_d_free_w_ep=int(result[20],16)
    pwr_d_ac_w_ep=int(result[21],16)
    pwr_d_pac_w_ep=int(result[22],16)

    crc_err_gain1=int(result[29],16)
    crc_err_gain2=int(result[30],16)
    crc_err_gain3=int(result[31],16)
    crc_err_gain4=int(result[32],16)
    crc_err_gain5=int(result[33],16)

    print "tx total pac %d\nrx total pac %d     rx correct pac %d\nPER %f\n"%(framecnt, totalp, cp, PER)
    return [totalp, cp, RSSI, noise, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
    pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, hec_ep, crc_ep, type_ep,
    crc_err_gain1,crc_err_gain2,crc_err_gain3,crc_err_gain4,crc_err_gain5]


def bt_rx_ber_test__ci(basebits=16000,rate=1,filename='1_dh1_prbs9.mod',pwrdBm=-15,UAP='01101011',freq=2472, chan=38, atten=0, biterror_thresh=30, port='left'):
    filename='BT/new/'+filename
    bt_iqv_tx_init(filename=filename,pwrdBm=pwrdBm+atten,freqMHz=freq, port=port)

    if rate==1 :
        link_type=4
    else :
        link_type=5

    errorbits=0
    totalbits=0
    loop=0

    print iqv_serv.txfrmcnt(framecnt=0)

    result=bt_rx_ber(bits=basebits, link_type=link_type, chan=chan, biterror_thresh=biterror_thresh)
    print iqv_serv.txenable(0)

    result=result.split()
    totalbits=int(result[0],16)
    errorbits=int(result[1],16)
    RSSI=0-int(result[3],16)
    noise=float(((int(result[4],16)&0x3ff)-1024))/4
    pwr_ib=int(result[5],16)
    pwr_fb=int(result[6],16)
    gain=int(result[7],16)
    totalp=int(result[8],16)



    totalp1=int(result[9],16)
    cp=int(result[10],16)
    #PER=1-(float(cp)/totalp1)

    hec_ep=int(result[11],16)
    crc_ep=int(result[12],16)
    type_ep=int(result[13],16)

    pwr_ibm_w_ep=int(result[24],16)
    pwr_fbm_w_ep=int(result[25],16)

    pwr_r_free_w_ep=int(result[26],16)
    pwr_r_ac_w_ep=int(result[27],16)
    pwr_r_pac_w_ep=int(result[28],16)
    pwr_d_free_w_ep=int(result[29],16)
    pwr_d_ac_w_ep=int(result[30],16)
    pwr_d_pac_w_ep=int(result[31],16)

    crc_err_gain1=int(result[32],16)
    crc_err_gain2=int(result[33],16)
    crc_err_gain3=int(result[34],16)
    crc_err_gain4=int(result[35],16)
    crc_err_gain5=int(result[36],16)

    be_excd=int(result[37],16)




    if(totalp!=0):
        pwr_ib=0-(float(pwr_ib)/totalp)
        pwr_fb=0-(float(pwr_fb)/totalp)
        gain=float(gain)/totalp
    if(totalbits==0):
        BER=1
    elif(errorbits==0):
        BER=0
    else:
        BER=float(errorbits)/totalbits
    print "rx total %d bits\nrx error %d bits\nBER %f"%(totalbits, errorbits,BER)
    print iqv_serv.txenable(0)
    return [totalbits, errorbits,RSSI,noise,pwr_ib,pwr_fb,gain, totalp1, cp, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
    pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, hec_ep, crc_ep, type_ep,
    crc_err_gain1,crc_err_gain2,crc_err_gain3,crc_err_gain4,crc_err_gain5,be_excd]




def per_ci_sweep(per_limit=0.2,directory="../per/", dcap_s=100, framecnt=5000,rate=1,file_name='1_dh1_prbs9',
pwrdBm_start=-35, pwrdBm_start_force=0,chan_start=40, ci_start=-40, ci_end=40, step=1, sig_os=0, sig_os_force=0, time_offset=-80, atten=23,save_name='', port='left'):
    dname="per_ci_sweep_dcap%d_pwr%d_chan%d_cis%d_cie%d_tos%d"%(dcap_s,pwrdBm_start, chan_start, ci_start, ci_end, time_offset)+save_name
    dname=directory+dname
    #if(not(os.path.exists(dname))):
    #    os.makedirs(dname)
    f=open(dname+'.csv', 'w')
    f.write('ci fos, TX power,TX pac,RX pac,RX correct pac,PER,fail,AER, PER RX pac, RSSI, noise, pwr inband, pwr fullband, gain, W inband max, W fullband max, W rise free, W rise ac, W rise pac, W drop free, W drop ac, W drop pac, HEC error, CRC error , TYPE error, crc_err_gain1, crc_err_gain2, crc_err_gain3, crc_err_gain4, crc_err_gain5\n')
    freq_raw= chan_start+2402
    framecnt_est=framecnt+5
    pwrdBm=pwrdBm_start
    if(ci_end<ci_start):
        step=-step
    else:
        step=step
    ci=ci_start
    i2c.wic("bbtop", "filter_btrx_dcap_lq",dcap_s)
    i2c.wic("bbtop", "filter_btrx_dcap_hq",dcap_s)


    while(ci!=(ci_end+step)):
            if(rate==1):
                if(ci==0):
                    cidb=11
                elif(abs(ci)==1):
                    cidb=0
                elif(abs(ci)==2):
                    cidb=-30
                else:
                    cidb=-40
            elif(rate==2):
                if(ci==0):
                    cidb=13
                elif(abs(ci)==1):
                    cidb=0
                elif(abs(ci)==2):
                    cidb=-30
                else:
                    cidb=-40
            else:
                if(ci==0):
                    cidb=21
                elif(abs(ci)==1):
                    cidb=5
                elif(abs(ci)==2):
                    cidb=-25
                else:
                    cidb=-33
            if(sig_os_force==0):
                if(ci<0):
                    if(rate==2):
                        sig_os=33
                    else:
                        sig_os=33
                else:
                    if(rate==2):
                        sig_os=-33
                    else:
                        sig_os=-33
            freq=freq_raw-sig_os

            if(pwrdBm_start_force==0):
                if(rate==1):
                    if(ci==0):
                        pwrdBm=-60
                    elif(abs(ci)==1):
                        pwrdBm=-60
                    elif(abs(ci)==2):
                        pwrdBm=-30
                    else:
                        pwrdBm=-27
                elif(rate==2):
                    if(ci==0):
                        pwrdBm=-60
                    elif(abs(ci)==1):
                        pwrdBm=-60
                    elif(abs(ci)==2):
                        pwrdBm=-30
                    else:
                        pwrdBm=-27
                else:
                    if(ci==0):
                        pwrdBm=-60
                    elif(abs(ci)==1):
                        pwrdBm=-60
                    elif(abs(ci)==2):
                        pwrdBm=-35
                    else:
                        pwrdBm=-34

            f.write("%dMHz,"%ci)
            f.write("%ddBm,"%pwrdBm)
            if(sig_os==0):
                file_name_full="test_"+file_name+"_ci%dm_%ddB_%dus.mod"%(ci, cidb, time_offset)
            else:
                file_name_full="test_"+file_name+"_ci%dm_%ddB_sig%dm_%dus.mod"%(ci, cidb, sig_os, time_offset)
            [total_pac,cpac,RSSI,noise, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
            pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep,
            pwr_d_pac_w_ep, hec_ep, crc_ep, type_ep, crc_err_gain1,crc_err_gain2,crc_err_gain3,crc_err_gain4,crc_err_gain5]=bt_rx_per_test_ci(framecnt=framecnt,rate=rate,filename=file_name_full,pwrdBm=pwrdBm, freq=freq, chan=chan_start, atten=atten,port=port)
            if total_pac >= framecnt+10 :
                [total_pac,cpac,RSSI,noise, pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
                pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep,
                pwr_d_pac_w_ep, hec_ep, crc_ep, type_ep, crc_err_gain1,crc_err_gain2,crc_err_gain3,crc_err_gain4,crc_err_gain5]=bt_rx_per_test_ci(framecnt=framecnt,rate=rate,filename=file_name_full,pwrdBm=pwrdBm, freq=freq, chan=chan_start, atten=atten,port=port)
            PER=1-(float(cpac)/framecnt_est)
            if PER >= per_limit:
                fail =1
            else:
                fail=0
            AER=1-(float(total_pac)/framecnt_est)
            PER_RX_pac=1
            if total_pac != 0:
                PER_RX_pac=1-(float(cpac)/total_pac)
            f.write("%d,%d,%d,%f,%d,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f\n"
            %(framecnt_est,total_pac,cpac,PER,fail,AER,PER_RX_pac,RSSI,noise,
             pwr_ib, pwr_fb, gain, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
            pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep,
            pwr_d_pac_w_ep, hec_ep, crc_ep, type_ep,
            crc_err_gain1,crc_err_gain2,crc_err_gain3,crc_err_gain4,crc_err_gain5))
            ci=ci+step
    f.close




def ber_ci_sweep(ber_limit=0.001,directory="../per/", dcap_force=0, dcap_s=100, basebits=160000,rate=1,file_name='1_dh1_prbs9',
pwrdBm_start=-35, pwrdBm_start_force=0, chan_start=40, ci_start=-40, ci_end=40, step=1, sig_os=33, sig_os_force=0, time_offset=-80, atten=23,save_name='', co_sweep=0, port='left'):
    dname="ber_ci_sweep_"+file_name+"_dcap%d_pwr%d_chan%d_cis%d_cie%d_tos%d"%(dcap_s,pwrdBm_start, chan_start, ci_start, ci_end, time_offset)+save_name
    dname=directory+dname
    #if(not(os.path.exists(dname))):
    #    os.makedirs(dname)
    f=open(dname+'.csv', 'w')
    f.write('ci fos, RX power est, BER,fail, RSSI, noise, pwr inband, pwr fullband, gain, rxbits,  RX pac,RX correct pac,PER,W inband max, W fullband max, W rise free, W rise ac, W rise pac, W drop free, W drop ac, W drop pac, HEC error, CRC error , TYPE error, crc_err_gain1, crc_err_gain2, crc_err_gain3, crc_err_gain4, crc_err_gain5, n_be_over_tresh\n')
    freq_raw= chan_start+2402
    pwrdBm=pwrdBm_start
    if(ci_end<ci_start):
        step=-step
    else:
        step=step
    ci=ci_start
    if(dcap_force != 0):
        i2c.wic("bbtop", "filter_btrx_dcap_lq",dcap_s)
        i2c.wic("bbtop", "filter_btrx_dcap_hq",dcap_s)


    while(ci!=(ci_end+step)):
            if(rate==1):
                if(ci==0):
                    cidb=11
                elif(abs(ci)==1):
                    cidb=0
                elif(abs(ci)==2):
                    cidb=-30
                else:
                    cidb=-40
            elif(rate==2):
                if(ci==0):
                    cidb=13
                elif(abs(ci)==1):
                    cidb=0
                elif(abs(ci)==2):
                    cidb=-30
                else:
                    cidb=-40
            else:
                if(ci==0):
                    cidb=21
                elif(abs(ci)==1):
                    cidb=5
                elif(abs(ci)==2):
                    cidb=-25
                else:
                    cidb=-33
            if(sig_os_force==0):
                if(ci<-6):
                    if(rate==2):
                        sig_os=33
                    else:
                        sig_os=33
                elif(ci>6):
                    if(rate==2):
                        sig_os=-33
                    else:
                        sig_os=-33
                else:
                    if(freq_raw<=2441):
                        sig_os=-33
                    else:
                        sig_os=33
            freq=freq_raw-sig_os

            if(pwrdBm_start_force==0):
                if(rate==1):
                    if(ci==0):
                        pwrdBm=-60
                    elif(abs(ci)==1):
                        pwrdBm=-60
                    elif(abs(ci)==2):
                        pwrdBm=-30
                    else:
                        pwrdBm=-27
                elif(rate==2):
                    if(ci==0):
                        pwrdBm=-60
                    elif(abs(ci)==1):
                        pwrdBm=-60
                    elif(abs(ci)==2):
                        pwrdBm=-30
                    else:
                        pwrdBm=-27
                else:
                    if(ci==0):
                        pwrdBm=-60
                    elif(abs(ci)==1):
                        pwrdBm=-60
                    elif(abs(ci)==2):
                        pwrdBm=-35
                    else:
                        pwrdBm=-34

            f.write("%dMHz,"%ci)
            f.write("%ddBm,"%pwrdBm)
            if(co_sweep==1):
                file_name_full="test_"+file_name+"_ci%dm_%ddB_sig%dm_%dus.mod"%(ci, cidb, sig_os, time_offset)
            else:
                file_name_full="test_"+file_name+"_ci%dm_%ddB_sig%dm_%dus.mod"%(ci, cidb, sig_os, time_offset)
##                if(sig_os==0):
##                    file_name_full="test_"+file_name+"_ci%dm_%ddB_%dus.mod"%(ci, cidb, time_offset)
##                else:
##                    file_name_full="test_"+file_name+"_ci%dm_%ddB_sig%dm_%dus.mod"%(ci, cidb, sig_os, time_offset)
            [total_bits,error_bits,RSSI,noise, pwr_ib, pwr_fb, gain, totalp, cp, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
    pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, hec_ep, crc_ep, type_ep,
    crc_err_gain1,crc_err_gain2,crc_err_gain3,crc_err_gain4,crc_err_gain5,be_excd]=bt_rx_ber_test__ci(basebits=basebits,rate=rate,filename=file_name_full,pwrdBm=pwrdBm, freq=freq, chan=chan_start, atten=atten, port=port)
            if(total_bits==0):
        	    BER=1
            elif(error_bits==0):
        	    BER=0
            else:
                BER=float(error_bits)/total_bits
            if BER >= ber_limit:
                fail=1
            else:
                fail=0
            if(totalp!=0):
                PER=1-(float(cp)/totalp)
            else:
                PER=1
            f.write("%f,%d,%f,%f,%f,%f,%f,%f, %f, %f, %f, %f,%f,%f,%f,%f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f\n"%(BER,fail,RSSI,noise, pwr_ib, pwr_fb, gain,total_bits,
            totalp, cp, PER,
            pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep, pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep,
            hec_ep, crc_ep, type_ep,
            crc_err_gain1,crc_err_gain2,crc_err_gain3,crc_err_gain4,crc_err_gain5,be_excd))
            ci=ci+step
    f.close


def full_sweep(directory="../bt_iqv/full_sweep/1208/DUT1/"):
    if(not(os.path.exists(directory))):
        os.makedirs(directory)
    #sensitivity sweep
    bt_rx_per_sweep(framecnt=100, rate=1, file_name='1_dh1_prbs9.mod', pwrdBm_start=-95, pwrdBm_end=-20, chan_start=78, chan_end=78, file_w=directory+'per_', atten=23)
    bt_rx_per_sweep(framecnt=100, rate=1, file_name='1_dh1_prbs9.mod', pwrdBm_start=-95, pwrdBm_end=-20, chan_start=38, chan_end=38, file_w=directory+'per_', atten=23)
    bt_rx_per_sweep(framecnt=100, rate=1, file_name='1_dh1_prbs9.mod', pwrdBm_start=-95, pwrdBm_end=-20, chan_start=0, chan_end=0, file_w=directory+'per_', atten=23)
    bt_rx_sensitivity_test(basebits=160000, rate=2, file_name='2_dh5_prbs9.mod', pwrdBm_start=-90, pwrdBm_end=-60, chan_start=78, chan_end=78, file_w=directory+'ber_', atten=23)
    bt_rx_sensitivity_test(basebits=160000, rate=2, file_name='2_dh5_prbs9.mod', pwrdBm_start=-90, pwrdBm_end=-60, chan_start=38, chan_end=38, file_w=directory+'ber_', atten=23)
    bt_rx_sensitivity_test(basebits=160000, rate=2, file_name='2_dh5_prbs9.mod', pwrdBm_start=-90, pwrdBm_end=-60, chan_start=0, chan_end=0, file_w=directory+'ber_', atten=23)
    bt_rx_sensitivity_test(basebits=160000, rate=3, file_name='3_dh5_prbs9.mod', pwrdBm_start=-90, pwrdBm_end=-60, chan_start=78, chan_end=78, file_w=directory+'ber_', atten=23)
    bt_rx_sensitivity_test(basebits=160000, rate=3, file_name='3_dh5_prbs9.mod', pwrdBm_start=-90, pwrdBm_end=-60, chan_start=38, chan_end=38, file_w=directory+'ber_', atten=23)
    bt_rx_sensitivity_test(basebits=160000, rate=3, file_name='3_dh5_prbs9.mod', pwrdBm_start=-90, pwrdBm_end=-60, chan_start=0, chan_end=0, file_w=directory+'ber_', atten=23)

    #ci
##    per_ci_sweep(directory=directory, dcap_s=110, framecnt=100,rate=1,file_name='1_dh1_prbs9',
##pwrdBm_start=-35, pwrdBm_start_force=0,chan_start=78, ci_start=-72, ci_end=0, step=1, sig_os=0, sig_os_force=0, time_offset=-80, atten=23,save_name='')
##    per_ci_sweep(directory=directory, dcap_s=110, framecnt=100,rate=1,file_name='1_dh1_prbs9',
##pwrdBm_start=-35, pwrdBm_start_force=0,chan_start=38, ci_start=-72, ci_end=72, step=1, sig_os=0, sig_os_force=0, time_offset=-80, atten=23,save_name='')
##    per_ci_sweep(directory=directory, dcap_s=110, framecnt=100,rate=1,file_name='1_dh1_prbs9',
##pwrdBm_start=-35, pwrdBm_start_force=0,chan_start=0, ci_start=0, ci_end=72, step=1, sig_os=0, sig_os_force=0, time_offset=-80, atten=23,save_name='')
##
##    ber_ci_sweep(directory=directory, dcap_s=110, basebits=160000,rate=1,file_name='1_dh1_prbs9',
##pwrdBm_start=-35, pwrdBm_start_force=0, chan_start=78, ci_start=-72, ci_end=0, step=1, sig_os=33, sig_os_force=0, time_offset=-80, atten=23,save_name='')
##    ber_ci_sweep(directory=directory, dcap_s=110, basebits=160000,rate=1,file_name='1_dh1_prbs9',
##pwrdBm_start=-35, pwrdBm_start_force=0, chan_start=38, ci_start=-72, ci_end=72, step=1, sig_os=33, sig_os_force=0, time_offset=-80, atten=23,save_name='')
##    ber_ci_sweep(directory=directory, dcap_s=110, basebits=160000,rate=1,file_name='1_dh1_prbs9',
##pwrdBm_start=-35, pwrdBm_start_force=0, chan_start=0, ci_start=0, ci_end=72, step=1, sig_os=33, sig_os_force=0, time_offset=-80, atten=23,save_name='')
##
##    ber_ci_sweep(directory=directory, dcap_s=110, basebits=160000,rate=2,file_name='2_dh1_prbs9',
##pwrdBm_start=-35, pwrdBm_start_force=0, chan_start=78, ci_start=-72, ci_end=0, step=1, sig_os=33, sig_os_force=0, time_offset=-80, atten=23,save_name='')
##    ber_ci_sweep(directory=directory, dcap_s=110, basebits=160000,rate=2,file_name='2_dh1_prbs9',
##pwrdBm_start=-35, pwrdBm_start_force=0, chan_start=38, ci_start=-72, ci_end=72, step=1, sig_os=33, sig_os_force=0, time_offset=-80, atten=23,save_name='')
##    ber_ci_sweep(directory=directory, dcap_s=110, basebits=160000,rate=2,file_name='2_dh1_prbs9',
##pwrdBm_start=-35, pwrdBm_start_force=0, chan_start=0, ci_start=0, ci_end=72, step=1, sig_os=33, sig_os_force=0, time_offset=-80, atten=23,save_name='')
##
##    ber_ci_sweep(directory=directory, dcap_s=110, basebits=160000,rate=3,file_name='3_dh1_prbs9',
##pwrdBm_start=-35, pwrdBm_start_force=0, chan_start=78, ci_start=-72, ci_end=0, step=1, sig_os=33, sig_os_force=0, time_offset=-80, atten=23,save_name='')
##    ber_ci_sweep(directory=directory, dcap_s=110, basebits=160000,rate=3,file_name='3_dh1_prbs9',
##pwrdBm_start=-35, pwrdBm_start_force=0, chan_start=38, ci_start=-72, ci_end=72, step=1, sig_os=33, sig_os_force=0, time_offset=-80, atten=23,save_name='')
##    ber_ci_sweep(directory=directory, dcap_s=110, basebits=160000,rate=3,file_name='3_dh1_prbs9',
##pwrdBm_start=-35, pwrdBm_start_force=0, chan_start=0, ci_start=0, ci_end=72, step=1, sig_os=33, sig_os_force=0, time_offset=-80, atten=23,save_name='')



def ber_ci_sweep_co(f, dcap_s=110, basebits=160000,rate=1,file_name='1_dh1_prbs9',
pwrdBm_start=-35, pwrdBm_start_force=0, chan_start=40, ci_start=-40, ci_end=40, step=1, sig_os=33, sig_os_force=0, time_offset=-80, atten=23, biterror_thresh=30,save_name='', co_sweep=0):
    freq_raw= chan_start+2402
    pwrdBm=pwrdBm_start
    if(ci_end<ci_start):
        step=-step
    else:
        step=step
    ci=ci_start
    i2c.wic("bbtop", "filter_btrx_dcap_lq",dcap_s)
    i2c.wic("bbtop", "filter_btrx_dcap_hq",dcap_s)


    while(ci!=(ci_end+step)):
            if(rate==1):
                if(ci==0):
                    cidb=11
                elif(abs(ci)==1):
                    cidb=0
                elif(abs(ci)==2):
                    cidb=-30
                else:
                    cidb=-40
            elif(rate==2):
                if(ci==0):
                    cidb=13
                elif(abs(ci)==1):
                    cidb=0
                elif(abs(ci)==2):
                    cidb=-30
                else:
                    cidb=-40
            else:
                if(ci==0):
                    cidb=21
                elif(abs(ci)==1):
                    cidb=5
                elif(abs(ci)==2):
                    cidb=-25
                else:
                    cidb=-33
            if(sig_os_force==0):
                if(ci<0):
                    if(rate==2):
                        sig_os=33
                    else:
                        sig_os=33
                else:
                    if(rate==2):
                        sig_os=-33
                    else:
                        sig_os=-33
            freq=freq_raw-sig_os

            if(pwrdBm_start_force==0):
                if(rate==1):
                    if(ci==0):
                        pwrdBm=-60
                    elif(abs(ci)==1):
                        pwrdBm=-60
                    elif(abs(ci)==2):
                        pwrdBm=-30
                    else:
                        pwrdBm=-27
                elif(rate==2):
                    if(ci==0):
                        pwrdBm=-60
                    elif(abs(ci)==1):
                        pwrdBm=-60
                    elif(abs(ci)==2):
                        pwrdBm=-30
                    else:
                        pwrdBm=-27
                else:
                    if(ci==0):
                        pwrdBm=-60
                    elif(abs(ci)==1):
                        pwrdBm=-60
                    elif(abs(ci)==2):
                        pwrdBm=-35
                    else:
                        pwrdBm=-34
            f.write("%dus,"%time_offset)
            f.write("%dMHz,"%ci)
            f.write("%ddBm,"%pwrdBm)
            if(co_sweep==1):
                file_name_full="test_"+file_name+"_ci%dm_%ddB_sig%dm_%dus.mod"%(ci, cidb, sig_os, time_offset)
            else:
                if(sig_os==0):
                    file_name_full="test_"+file_name+"_ci%dm_%ddB_%dus.mod"%(ci, cidb, time_offset)
                else:
                    file_name_full="test_"+file_name+"_ci%dm_%ddB_sig%dm_%dus.mod"%(ci, cidb, sig_os, time_offset)
            [total_bits,error_bits,RSSI,noise, pwr_ib, pwr_fb, gain, totalp, cp, pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep,
    pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep, hec_ep, crc_ep, type_ep,
    crc_err_gain1,crc_err_gain2,crc_err_gain3,crc_err_gain4,crc_err_gain5,be_excd]=bt_rx_ber_test__ci(basebits=basebits,rate=rate,filename=file_name_full,pwrdBm=pwrdBm, freq=freq, chan=chan_start, atten=atten, biterror_thresh=biterror_thresh)
            if(total_bits==0):
        	    BER=1
            elif(error_bits==0):
        	    BER=0
            else:
                BER=float(error_bits)/total_bits
            if(totalp!=0):
                PER=1-(float(cp)/totalp)
            else:
                PER=1
            f.write("%f,%f,%f,%f,%f,%f,%f, %f, %f, %f, %f,%f,%f,%f,%f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f\n"%(BER,RSSI,noise, pwr_ib, pwr_fb, gain,total_bits,
            totalp, cp, PER,
            pwr_ibm_w_ep, pwr_fbm_w_ep, pwr_r_free_w_ep, pwr_r_ac_w_ep, pwr_r_pac_w_ep, pwr_d_free_w_ep, pwr_d_ac_w_ep, pwr_d_pac_w_ep,
            hec_ep, crc_ep, type_ep,
            crc_err_gain1,crc_err_gain2,crc_err_gain3,crc_err_gain4,crc_err_gain5,be_excd))
            ci=ci+step


def ber_coci_sweep(directory= "../bt_iqv/co_sweep/", os_range=60, basebits=160000, chan_start=40, atten=23, biterror_thresh=30,save_name=""):
    if(not(os.path.exists(directory))):
        os.makedirs(directory)
    dname="ber_cochannel_ci_sweep_os_range%d_chan%d"%(os_range, chan_start)+save_name
    dname=directory+dname
    #if(not(os.path.exists(dname))):
    #    os.makedirs(dname)
    f=open(dname+'.csv', 'w')
    f.write('tos, ci fos, RX power est, BER, RSSI, noise, pwr inband, pwr fullband, gain, rxbits,   RX pac,RX correct pac,PER,W inband max, W fullband max, W rise free, W rise ac, W rise pac, W drop free, W drop ac, W drop pac, HEC error, CRC error , TYPE error, crc_err_gain1, crc_err_gain2, crc_err_gain3, crc_err_gain4, crc_err_gain5, n_be_over_tresh\n')
    os_now=-os_range;
    while(os_now<(os_range+1)):
        ber_ci_sweep_co(f=f, dcap_s=110, basebits=basebits, rate=1, file_name='1_dh1_prbs9',
pwrdBm_start=-35, pwrdBm_start_force=0, chan_start=chan_start, ci_start=0, ci_end=0, step=1, sig_os=0, sig_os_force=1, time_offset=os_now, atten=23,save_name='', co_sweep=1)
        os_now=os_now+1
    f.close()



def ber_ci_sweep_scan(cur='1207_scan_2',basebits=16000,gainlst=[]):
    mem.wrm(0x600060a0,26,25,2) #force wifi off
    mem.wrm(0x600060a0,28,27,3) #force bt on
    mem.wrm(0x60011018,31,31,1) #force bt_rx_en
    mem.wrm(0x3ff0002c,17,16,2) #dump
    mem.wrm(0x6001c024,17,9,300) #pwr low
    mem.wrm(0x6001c0a0,8,0,300) #pwr too low
    mem.wrm(0x6001c084,26,22,31) #bt_fine_rec_thr
    mem.wrm(0x6001c02c, 31, 23, (((128+40)<<1) | 1)) #force gain

    gain_bit14_13=[0,1,2];  #sw
    gain_bit12_10=range(0,8); #lna, vga_h, vga_l
    gain_bit9_3=[0,0x1,0x3,0x7,0xf,0x1f,0x3f];  #lpf_coarse
    gain_bit2_0=[0,2,4]; #lpf_fine

    if (gainlst==[]):
        for bit9_3 in gain_bit9_3:
            for bit2_0 in gain_bit2_0:
                for bit14_13 in gain_bit14_13:
                    for bit12_10 in gain_bit12_10:
                        gainlst.append((bit14_13<<13)+(bit12_10<<10)+(bit9_3<<3)+bit2_0);

    for rx_gain in gainlst:
##        [dcoi1_c,dcoq1_c,dcoi1_f,dcoq1_f]= pbus_test.pbus_gain_dccal(rx_gain, 'com');
        save_name='_0x%x_'%rx_gain
        ber_ci_sweep(directory="../BT_iqv/ber_"+cur+"/", dcap_s=110, basebits=basebits,rate=3,file_name='3_dh1_prbs9',pwrdBm_start=-35,chan_start=40, ci_start=-39, ci_end=-36, step=1, time_offset=-80, sig_os=0, sig_os_force=1, atten=23,save_name=save_name)



def iqx_mea_tx_init(freqMHz=2470,pwrdBm=0,ex_att=0,port='left'):
    if port=='left':
        print iqxel_serv.setvsa(freqMhz=freqMHz,rxmaxpwr=pwrdBm,exAttenDb=ex_att)
    else:
        print iqxel_serv.setvsa_right(freqMhz=freqMHz,rxmaxpwr=pwrdBm,exAttenDb=ex_att)


def iqx_mea_tx(tcapms=10,rate=1 ):
    iqxel_serv.capture(smplTm_microSecs=tcapms)
    iqxel_serv.setbtrxmethod(bt_data_rate=rate)

def mea_df1(n=1,txpwr=4,freqMHz=2470,pwrdBm=0,ex_att=0,port='left'):
    chan=freqMHz-2402
    fcc_tx(txpwr=txpwr, hoppe=0, chan=chan, rate=1, data=1,)
##    iqx_mea_tx_init(freqMHz=freqMHz,pwrdBm=pwrdBm,ex_att=ex_att,port=port)
    nmeas=0
    sum_df1=0
    tout=0
    while nmeas < n:
        tout=tout+1
        iqx_mea_tx(rate=1)
        df1=iqxel_serv.getmeasdata(iq_mode='bt',meas_type='deltaF1Average')
##        print df1
        if df1[0]==0:
            nmeas=nmeas+1
            sum_df1=sum_df1+df1[1]
        if tout>(n*10):
            break

    result=cmdstop()
    return sum_df1/n


def mea_df2(n=1,txpwr=4,freqMHz=2470,pwrdBm=0,ex_att=0,port='left'):
    chan=freqMHz-2402
    fcc_tx(txpwr=txpwr, hoppe=0, chan=chan, rate=1, data=0,)
##    iqx_mea_tx_init(freqMHz=freqMHz,pwrdBm=pwrdBm,ex_att=ex_att,port=port)
    nmeas=0
    sum_df2=0
    tout=0
    while nmeas < n:
        tout=tout+1
        iqx_mea_tx(rate=1)
        df2=iqxel_serv.getmeasdata(iq_mode='bt',meas_type='deltaF2Average')
##        print df2
        if df2[0]==0:
            nmeas=nmeas+1
            sum_df2=sum_df2+df2[1]
        if tout>(n*10):
            break

    result=cmdstop()
    return sum_df2/n


def mea_df2max(n=1,txpwr=4,freqMHz=2470,pwrdBm=0,ex_att=0,port='left'):
    chan=freqMHz-2402
    fcc_tx(txpwr=txpwr, hoppe=0, chan=chan, rate=1, data=1,)
##    iqx_mea_tx_init(freqMHz=freqMHz,pwrdBm=pwrdBm,ex_att=ex_att,port=port)
    nmeas=0
    tout=0
    while nmeas < n:
        tout=tout+1
        iqx_mea_tx(rate=1)
        df2m=iqxel_serv.getmeasdata(iq_mode='bt',meas_type='deltaF2Average')
##        print df2m
        if df2m[0]==0:
            nmeas=nmeas+1
            if nmeas==1:
                rslt_df2m=df2m[1]
            else:
                rslt_df2m=[rslt_df2m,df2m[1]]
        if tout>(n*10):
            break

    result=cmdstop()
    return rslt_df2m

def mea_df2df1(txpwr=4,freqMHz=2470,pwrdBm=0,ex_att=0,port='left'):
    iqx_mea_tx_init(freqMHz=freqMHz,pwrdBm=pwrdBm,ex_att=ex_att,port=port)
    df1=mea_df1(n=1,txpwr=txpwr,freqMHz=freqMHz,pwrdBm=pwrdBm,ex_att=ex_att,port=port)
    df2=mea_df2(n=1,txpwr=txpwr,freqMHz=freqMHz,pwrdBm=pwrdBm,ex_att=ex_att,port=port)
    return df2/df1




def fcc_mea_df1(n=1,txpwr=4,freqMHz=2470,pwrdBm=0,ex_att=0,port='left'):
    chan=freqMHz-2402
    #fcc_tx(txpwr=txpwr, hoppe=0, chan=chan, rate=1, data=1,)
    rw_fcc_bt_tx(txpwr=txpwr, hoppe=0, chan=chan, rate=1, length=5, data=1)
##    iqx_mea_tx_init(freqMHz=freqMHz,pwrdBm=pwrdBm,ex_att=ex_att,port=port)
    nmeas=0
    sum_df1=0
    tout=0
    while nmeas < n:
        tout=tout+1
        iqx_mea_tx(rate=1)
        df1=iqxel_serv.getmeasdata(iq_mode='bt',meas_type='deltaF1Average')
##        print df1
        if df1[0]==0:
            nmeas=nmeas+1
            sum_df1=sum_df1+df1[1]
        if tout>(n*10):
            break

    result=cmdstop()
    return sum_df1/n


def fcc_mea_df2(n=1,txpwr=4,freqMHz=2470,pwrdBm=0,ex_att=0,port='left'):
    chan=freqMHz-2402
    #fcc_tx(txpwr=txpwr, hoppe=0, chan=chan, rate=1, data=0,)
    rw_fcc_bt_tx(txpwr=txpwr, hoppe=0, chan=chan, rate=1, length=5, data=0)
##    iqx_mea_tx_init(freqMHz=freqMHz,pwrdBm=pwrdBm,ex_att=ex_att,port=port)
    nmeas=0
    sum_df2=0
    tout=0
    while nmeas < n:
        tout=tout+1
        iqx_mea_tx(rate=1)
        df2=iqxel_serv.getmeasdata(iq_mode='bt',meas_type='deltaF2Average')
##        print df2
        if df2[0]==0:
            nmeas=nmeas+1
            sum_df2=sum_df2+df2[1]
        if tout>(n*10):
            break

    result=cmdstop()
    return sum_df2/n


def fcc_mea_df2max(n=1,txpwr=4,freqMHz=2470,pwrdBm=0,ex_att=0,port='left'):
    chan=freqMHz-2402
    #fcc_tx(txpwr=txpwr, hoppe=0, chan=chan, rate=1, data=1,)
    rw_fcc_bt_tx(txpwr=txpwr, hoppe=0, chan=chan, rate=1, length=5, data=0)
##    iqx_mea_tx_init(freqMHz=freqMHz,pwrdBm=pwrdBm,ex_att=ex_att,port=port)
    nmeas=0
    tout=0
    while nmeas < n:
        tout=tout+1
        iqx_mea_tx(rate=1)
        df2m=iqxel_serv.getmeasdata(iq_mode='bt',meas_type='deltaF2Average')
##        print df2m
        if df2m[0]==0:
            nmeas=nmeas+1
            if nmeas==1:
                rslt_df2m=df2m[1]
            else:
                rslt_df2m=[rslt_df2m,df2m[1]]
        if tout>(n*10):
            break

    result=cmdstop()
    return rslt_df2m

def fcc_mea_df2df1(txpwr=4,freqMHz=2470,pwrdBm=0,ex_att=0,port='left'):
    iqx_mea_tx_init(freqMHz=freqMHz,pwrdBm=pwrdBm,ex_att=ex_att,port=port)
    df1=fcc_mea_df1(n=1,txpwr=txpwr,freqMHz=freqMHz,pwrdBm=pwrdBm,ex_att=ex_att,port=port)
    df2=fcc_mea_df2(n=1,txpwr=txpwr,freqMHz=freqMHz,pwrdBm=pwrdBm,ex_att=ex_att,port=port)
    return df2/df1





def sweep_dcap_mea_df2df1(ntest=10,txpwr=4,freqMHz=2470,pwrdBm=0,ex_att=0,dcap_start=70,dcap_end=110,file_w = '../sweep_dcap_mea_df2df1_',port='left'):
    trange="txpwr%d_chan%d_dcap_start%d_dcap_end%d"%(txpwr, freqMHz,dcap_start,dcap_end)
    f=open(file_w+trange+'.csv', 'w')
    f.write('dcap,df2df1\n')

    if dcap_start<=dcap_end:
        dcap_step=1;
    else:
        dcap_step=-1;
    dcap_now_lp=dcap_start;
    dcap_now_hp=dcap_start+2;

    while dcap_now_lp != dcap_end+dcap_step:
        i2c.wic("bbtop", "filter_bttx_dcap_lq",dcap_now_lp)
        i2c.wic("bbtop", "filter_bttx_dcap_hq",dcap_now_hp)
        f.write('%d,'%dcap_now_lp)
        for loop in range(0,ntest):
            rslt=mea_df2df1(txpwr=txpwr,freqMHz=freqMHz,pwrdBm=pwrdBm,ex_att=ex_att,port=port)
            f.write('%f,'%rslt)
            if loop==0:
                rslt_min=rslt
            elif rslt_min>rslt:
                rslt_min=rslt
        f.write('%f,\n'%rslt_min)
        dcap_now_lp=dcap_now_lp+dcap_step
        dcap_now_hp=dcap_now_hp+dcap_step
    f.close

