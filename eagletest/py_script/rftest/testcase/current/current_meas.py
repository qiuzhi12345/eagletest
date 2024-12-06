import time
import re
import csv
import os, sys
import matplotlib.pyplot as plt
import pylab
import numpy as np
from baselib.instrument import dm,tester
from rftest.rflib.wifi_lib import WIFILIB
from hal.common import MEM
import rftest.rflib.rfglobal as rfglobal
import rftest.rflib.wifi_instrum as instrum
from baselib.loglib.log_lib import *
from rftest.rflib.csv_report import csvreport
from rftest.testcase.rf_debug.tx_gain_sweep import Sweep_TX_Gain
from rftest.rflib.rfpll import rfpll
from rftest.rflib.rfcal import rfcal
from hal.common import PBUS
from hal.hwregister.hwpbus.all import *
from hal.power import POWER

rate_bps_dict = rfglobal.rate_bps_dict
sens_dict = rfglobal.sens_dict
rate_dict = rfglobal.ratedic
maxleve_dict = rfglobal.rx_maxlevel_dict
##dig_atten_lst = [-14,-8,-8,8,12]
dig_atten_vs_rate = {
        "mcs0": -8 ,
        "mcs1": -8 ,
        "mcs2": -8 ,
        "mcs3": -2 ,
        "mcs4": -2 ,
        "mcs5":  4 ,
        "mcs6":  8 ,
        "mcs7": 12 ,
        "mcs0_40": -8 ,
        "mcs1_40": -8 ,
        "mcs2_40": -8 ,
        "mcs3_40": -2 ,
        "mcs4_40": -2 ,
        "mcs5_40":  4 ,
        "mcs6_40":  8 ,
        "mcs7_40": 12 ,
        "6m":  -8,
        "9m":  -8,
        "12m": -8,
        "18m": -8,
        "24m": -2,
        "36m": -2,
        "48m": 4,
        "54m": 4,
        "1m": -18 ,
        "2m": -18 ,
        "5.5m": -18,
        "11m":-18
        }
Force_gain = 0

class RF_Curr(object):

    def __init__(self,comport,chipv='ESP32'):

        self.comport = comport
        self.chipv = chipv
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.pbus = PBUS(self.comport,self.chipv)
        self.hwpbus = HWPBUS(self.comport,self.chipv)
        self.sweep_tx_gain = Sweep_TX_Gain(self.comport,self.chipv)
        self.mem = MEM(self.comport,self.chipv)
        self.rfcal = rfcal(self.comport, self.chipv)
        self.rfpll = rfpll(self.comport, self.chipv)
        self.power =POWER(self.comport,self.chipv)

    def measure_current(self, plot=1, sample_rate=0.001,sample_num=512,maxvalue=0.8,labels='', hold=0, color='blue', title="",path=''):

        '''
        :brief:
            Digit Multimeter used to test current ,then produce picture and return the test result
        '''
        self.mydm = dm.dm()
        if path=='':
            path = path +'current_figure/'
        if title=='':
            filetime = time.strftime('_%Y%m%d_%H%M%S',time.localtime(time.time()));
            title = filetime

        I_sum=0;
        max_cur = 0
        min_cur = 2000
        self.mydm.start_rate(sample_num=sample_num,meastype='CURR',maxvalue=maxvalue,sample_rate=sample_rate)
        res = self.mydm.getcurve()
        # A to mA
        for index, subres in enumerate(res):
            res[index] = subres*1000
            I_sum=I_sum+res[index]
            if res[index] > max_cur:
                max_cur = res[index]
            if res[index] < min_cur:
                min_cur = res[index]
        result_average = I_sum/sample_num;

        loginfo("max_current=%f"%max_cur)
        loginfo("min_current=%f"%min_cur)
        loginfo("result_average=%f"%result_average)
        # plot
        if(plot):
            x = np.array(range(0, len(res)));
            y = np.array(res);
            if(hold):
                plt.hold;
            else:
                plt.figure(figsize=(8,8));
            plt.step(x,y,color,linewidth=2,label=labels+" max_curr: %3.2f min_curr: %3.2f"%(max_cur, min_cur));
            plt.title(title);
            plt.xlabel("time unit: %dms"%(sample_rate*1000));
            plt.ylabel("current unit: 1mA");
            pylab.legend()
            pylab.grid()
            plt.savefig(path+'_current_%s.png'%(title));
            plt.close()

        return [max_cur,min_cur,result_average]



    def txrate_curr(self,channel=[1,6,11], data_rate=['mcs0','mcs7'], cable_lose=1, rf_en =0, iqv_no=1):

        '''
        :brief:
            test current in tx mode
        :param:
            - channel    : 1~14
            - data_rate  : date rate
            - cable_lose : the lose of cable
            - rf_en      : enable tx performace test
            - iqv_no     : 1 - left ; 2- right

        :return:
            csv report
        '''
        if Force_gain == 1:
            title = 'cbw40m, rate, channel,pa_gain,bb_gain,dig_atten,curr_max,curr_min,curr_avg_duty20,max_cal,avg_duty50_cal'
        else:
            title = 'cbw40m, rate, channel,curr_max,curr_min,curr_avg_duty20,max_cal,avg_duty50_cal'

        fname = self.wifi.get_filename('rf_curr_data', 'rf_tx_current', 'rf_tx_current')
        if rf_en == 1:
            title +=',pwr,evm'
        csvreport1 = csvreport(fname, title+'\n')

        rate_l = len(data_rate)
        chan_l = len(channel)
        w_str =''
        cbw40m = 0
        reset_flag = 0
        ext_atten = cable_lose
        max_pwr = 25 - ext_atten

        for i in range(0, rate_l):
            for j in range(0, chan_l):

                rate = data_rate[i]
                chan = channel[j]
                freq = self.wifi.chan2freq(chan)
                loginfo("rate=%s,chan=%d"%(rate,chan))
                self.wifi.cmdstop()
                cbw40m = self.wifi.rate2ht40(rate)
                if Force_gain == 1:
                    dig_atten= dig_atten_vs_rate[rate]
                    pa_gain=0x5f
                    bb_gain=0xa0
                    self.sweep_tx_gain.fix_gain_rate_sweep(cable_lose=cable_lose, channel=[chan], data_rate=[rate], iqv_num=20, target_pwr_dis=1,iqv_no=iqv_no, board_no='chip722_Marlins')
                else:
                    self.wifi.txout_new(txchan=chan,rate_sym=rate,PackNum=0,time_us=500,duty=0.5,backoff_qdb=0)
                if rf_en == 1 :

                    if reset_flag == 0:
                        myiqv = tester.tester(freq, max_pwr, rate, instrum.test_para(rate), iqv_no,'measure', ext_atten, 10, 0)
                        reset_flag = 1
                    else:
                        myiqv = tester.tester(freq, max_pwr, rate, instrum.test_para(rate), iqv_no,'measure', ext_atten, 10, 0)

                    logdebug("exit tester ")
                    instrum.iqv_avg(myiqv, 10,'false')
                    iqv = rfglobal.iqv
                    evm = iqv['evm_raw']
                    evm_std = iqv['evm_std']
                    evm_max = iqv['evm_max']
                    pwr = iqv['pwr']
                    freq_err = iqv['freq_err']
                    clk_err = iqv['clk_err']

                time.sleep(1)
                curr = self.measure_current(plot=1, sample_rate=0.0005,sample_num=512,maxvalue=0.8,labels='', hold=0, color='blue', title=rate+'_chan'+str(chan),path=fname)
                max_cal = (curr[2] - 0.5*curr[1])/0.5
                avg50_cal = (max_cal - curr[1])/2 + curr[1]
                if rf_en == 1:
                    if Force_gain == 1:
                        csv_row=[cbw40m,rate,chan,pa_gain,bb_gain,dig_atten,curr[0],curr[1],curr[2],max_cal,avg50_cal,pwr,evm]
                    else:
                        csv_row=[cbw40m,rate,chan,curr[0],curr[1],curr[2],max_cal,avg50_cal,pwr,evm]

                else:
                    csv_row=[cbw40m,rate,chan,curr[0],curr[1],curr[2],max_cal,avg50_cal]
                self.wifi.cmdstop()
                self.wifi.cbw40m_en(0)

                csvreport1.write_data(csv_row)


    def rxrate_curr(self,channel=[1,6,11],data_rate=['1m','mcs7_40']):

        '''
        :brief:
            test current in rx mode
        :param:
            - channel    : 1~14
            - data_rate  : date rate
        :return:
            csv report
        '''

        title = 'cbw40m, rate, channel,curr_max,curr_min,curr_avg\n'
        fname = self.wifi.get_filename('rf_curr_data', 'rx_current', 'rx_current')
        csvreport1 = csvreport(fname, title)

        rate_l = len(data_rate)
        chan_l = len(channel)
        w_str =''
        cbw40m = 0
        if self.chipv =="CHIP723" or self.chipv =="CHIP724":
            self.comport.req_com("close_peri")
        for i in range(0, rate_l):
            for j in range(0, chan_l):

                rate = data_rate[i]
                chan = channel[j]
                self.wifi.cmdstop()
                cbw40m = self.wifi.rate2ht40(rate)
                self.wifi.cbw40m_en(cbw40m)

                self.wifi.esp_rx(chan, rate)
                time.sleep(1)
##                self.power.modemsleep_cur(close_phy = 0, cpu_freq = 1, wifi_pd = 0, wifi_clkgating = 0, peri_clkgating = 1, cpu_waiti = 1, cpu_keeprun = 0, use_cache = 0, rtc_dbias = 4, dig_dbias = 4)
                curr = self.measure_current(plot=1, sample_rate=0.001,sample_num=512,maxvalue=0.8,labels='', hold=0, color='blue', title=rate+'_chan'+str(chan),path=fname)
                csvreport1.write_data([cbw40m,rate,chan,curr[0],curr[1],curr[2]])
                self.wifi.cmdstop()
                self.wifi.cbw40m_en(0)


    def Diff_RX_part_current(self):

        title = 'rfrx1,rftx1,bb1,ck_gen_i2c_pu,rfpll_i2c_pu,bbpll_i2c_pd,curr_avg\n'
        fname = self.wifi.get_filename('rf_curr_data', 'Diff_part_current', 'Diff_part_current')
        csvreport1 = csvreport(fname, title)
        self.power.modemsleep_cur(close_phy = 0, peri_clkgating = 1, cpu_waiti = 1)

        PA_gain = 0x00
        BB_gain = 0x00
        self.mem.rdm(0x60008000+0x34,31,31)
        rfpll_pd = self.mem.rdm(0x60008000+0x34,31,31)
        ck_gen_pd = self.mem.rdm(0x60008000+0x34,30,30)
        bbpll_pd = self.mem.rdm(0x60008000+0,11,10)
        print rfpll_pd, ck_gen_pd, bbpll_pd
        self.pbus.pbus_debugmode()
        rftx1 = 0
        self.hwpbus.RFTX1.EN1 = rftx1
        self.hwpbus.RFTX2.EN1 = PA_gain
        self.hwpbus.BB1.EN2   = BB_gain
        for bb1,flag in[[0x189,-2],[0x189,-1],[0x189,0],[0x189,1],[0x189,2],[0x109,0],[0x101,0],[0x100,0],[0x00,0]]:
            if  flag == -2:
                rfrx1 = 0x1fe
                self.hwpbus.RFRX1.EN1 = rfrx1
                self.hwpbus.BB1.EN1   = bb1
            elif flag == -1:
                rfrx1 = 0x184
                self.hwpbus.RFRX1.EN1 = rfrx1
                self.hwpbus.BB1.EN1   = bb1
            else:
                rfrx1 = 0
                self.hwpbus.RFRX1.EN1 = rfrx1
                self.hwpbus.BB1.EN1   = bb1
                if flag == 1:
                    self.mem.wrm(0x60008000+0x34,30,30,0)
                elif flag == 2:
                    self.mem.wrm(0x60008000+0x34,31,31,0)
            rfpll_pd = self.mem.rdm(0x60008000+0x34,31,31)
            ck_gen_pd = self.mem.rdm(0x60008000+0x34,30,30)
            bbpll_pd = self.mem.rdm(0x60008000+0,11,10)
            time.sleep(1)
            I_=dm.dm()
            curr = float(I_.get_result("IDC"))*1000
            print curr
            csvreport1.write_data([hex(self.hwpbus.RFRX1.EN1),hex(self.hwpbus.RFTX1.EN1),hex(self.hwpbus.BB1.EN1),ck_gen_pd,rfpll_pd,bbpll_pd,curr])




    def Diff_TX_part_current(self):

        title = 'rfrx1,rftx1,bb1,ck_gen_i2c_pu,rfpll_i2c_pu,bbpll_i2c_pd,curr_avg\n'
        fname = self.wifi.get_filename('rf_curr_data', 'Diff_part_current', 'Diff_part_current')
        csvreport1 = csvreport(fname, title)
        self.power.modemsleep_cur(close_phy = 0, peri_clkgating = 1, cpu_waiti = 1)

        PA_gain = 0x00
        BB_gain = 0x00
        rfpll_pd = self.mem.rdm(0x60008000+0x34,31,31)
        ck_gen_pd = self.mem.rdm(0x60008000+0x34,30,30)
        bbpll_pd = self.mem.rdm(0x60008000+0,11,10)
        print rfpll_pd, ck_gen_pd, bbpll_pd
        self.pbus.pbus_debugmode()
        rfrx1 = 0x1
        self.hwpbus.RFRX1.EN1 = rfrx1
        self.hwpbus.RFTX2.EN1 = PA_gain
        self.hwpbus.BB1.EN2   = BB_gain
        for bb1,flag in[[0x7c,-1],[0x7c,0],[0x78,0],[0x68,0],[0x48,0],[0x48,1],[0x48,2],[0x40,0],[0x0,0]]:
            if flag == -1:
                rftx1 = 0x7f
                self.hwpbus.RFTX1.EN1 = rftx1
                self.hwpbus.BB1.EN1   = bb1
            else:
                rftx1 = 0
                self.hwpbus.RFTX1.EN1 = rftx1
                self.hwpbus.BB1.EN1   = bb1
                if flag == 1:
                    self.mem.wrm(0x60008000+0x34,30,30,0)
                elif flag == 2:
                    self.mem.wrm(0x60008000+0x34,31,31,0)
            rfpll_pd = self.mem.rdm(0x60008000+0x34,31,31)
            ck_gen_pd = self.mem.rdm(0x60008000+0x34,30,30)
            bbpll_pd = self.mem.rdm(0x60008000+0,11,10)
            time.sleep(1)
            I_=dm.dm()
            curr = float(I_.get_result("IDC"))*1000
            print curr
            csvreport1.write_data([hex(self.hwpbus.RFRX1.EN1),hex(self.hwpbus.RFTX1.EN1),hex(self.hwpbus.BB1.EN1),ck_gen_pd,rfpll_pd,bbpll_pd,curr])

    def rxrate_curr_rx_pwr(self,cable_lose=2, channel=[14],data_rate=['1m','mcs7_40'],minpwr=-98,maxpwr=0,pwr_step=1,iqv_no=1):

        '''
        :brief:
            test current in rx mode with different RX power level
        :param:
            - channel    : 1~14
            - data_rate  : date rate
        :return:
            csv report
        '''
        title = 'channel, rate, rfpwr,DesirepackNum,rssi,curr_max,curr_min,curr_avg\n'
        fname = self.wifi.get_filename('rf_curr_data', 'rx_current', 'rx_current')
        csvreport1 = csvreport(fname, title)
        packnum=100

        for i in range(0, len(data_rate)):
            for j in range(0,len(channel)):
                cur_rate = data_rate[i]
                chan_no = channel[j]

                freq = self.wifi.chan2freq(chan_no)

##                minpwr = sens_dict[cur_rate]
##                maxpwr = maxleve_dict[cur_rate]

                print 'minpwr=%d, maxpwr=%d'%(minpwr,maxpwr)
                mytester=tester.tester(freq,-40,'1m',1,iqv_no,'source',cable_lose,isreset=0)

                cbw40m = self.wifi.rate2ht40(cur_rate)
                rfpwr = minpwr

                while rfpwr<=maxpwr:
                    mytester.sigout(freq,rfpwr,cable_lose,cur_rate,packnum,iqv_no)

    ##                    self.wifi.rxstart(rx_rate)
                    self.wifi.esp_rx(chan_no, cur_rate)
                    mytester.trig_wave(iqv_no);
                    time.sleep(0.1)
                    curr = self.measure_current(plot=1, sample_rate=0.001,sample_num=512,maxvalue=0.8,labels='', hold=0, color='blue', title=cur_rate+'_chan'+str(chan_no),path=fname)
                    result_data = self.wifi.cmdstop()

                    [DesirePackNum, gain, rssi, noise, err, err2, freqoff] = self.wifi.rxresult(result_data)

    ##                    perform_list.append((rfpwr,DesirePackNum,rssi,gain,noise,err,err2, freqoff));
                    loginfo(result_data)
                    csvreport1.write_data([chan_no,cur_rate,rfpwr,DesirePackNum,rssi,curr[0],curr[1],curr[2]])

                    rfpwr=rfpwr+pwr_step;
                    mytester.set_pwr(rfpwr,0,iqv_no,'source');
                mytester.gen_switch('OFF',iqv_no)



