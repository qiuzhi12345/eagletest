import time
import re
import csv
import os, sys
import matplotlib.pyplot as plt
import pylab
import xlrd
import numpy as np
import pandas as pd
from rftest.rflib.utility import mfunc
from baselib.instrument import dm,tester,sme
from baselib.instrument.spa import HP,Agilent
from rftest.rflib.wifi_lib import WIFILIB
from hal.Init import HALS
from hal.common import MEM,MEM_TS,CHIP_ID
from rftest.rflib.pbus import pbus as Pbus
from rftest.rflib.rfpll import rfpll
from rftest.rflib.rfcal import rfcal as _rfcal
import rftest.rflib.rfglobal as rfglobal
import rftest.rflib.wifi_instrum as wifi_instrum
from rftest.rflib.saradc import SARADC
from rftest.testcase.rf_debug.tx_gain_sweep import Sweep_TX_Gain
from rftest.rflib.iq_est import IQ_EST
from baselib.loglib.log_lib import *
from hal.hwregister.hwi2c.all import *
from hal.hwregister.hwpbus.all import *
from rftest.rflib.csv_report import csvreport
from hal.wifi_api import WIFIAPI
from rftest.rflib.adc_dump import DUMP
from baselib.instrument import *


class filter_test(object):
    def __init__(self,comport,chipv='ESP32'):
        self.comport = comport
        self.chipv = chipv
        self.hals= HALS(self.comport,self.chipv)
        self.rfcal = _rfcal(self.comport,self.chipv)
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.mem = MEM(self.comport, self.chipv)
        self.mem_ts = MEM_TS(self.comport, self.chipv)
        self.pbus = Pbus(self.comport, self.chipv)
        self.rfpll = rfpll(self.comport, self.chipv)
        self.iq_est = IQ_EST(self.comport, self.chipv)
        self.chipid = CHIP_ID(self.comport, self.chipv)
        self.i2c = HWI2C(self.comport,self.chipv)
        self.wifiapi = WIFIAPI(self.comport,self.chipv)
        self.adc_dump = DUMP(self.comport,self.chipv)
        self.curr_data_path = 'E:/chip/eagletest/py_script/rftest/rfdata/filter_test/'
        if False==os.path.exists(self.curr_data_path):
            os.mkdir(self.curr_data_path )

    def filter_tx(self,cfreq=2437, bw=60, att=0, bt_en=0, PA_gain=0x5f, filter_gain_list=[0x100,0x120,0x130,0x138,0x13c,0x13e,0x13f,0x40,0x80,0xc0,0x140,0x180,0x1c0], device_spa='E4404B'):
        for filter_gain in filter_gain_list:
            filetime = time.strftime('_%Y%m%d_%H%M%S',time.localtime(time.time()));
            chip_id= self.chipid.chip_mac()
            file=self.curr_data_path + 'tx_filter_%s_0x%x_%s.csv'%(chip_id,filter_gain,filetime)
            f=open(file,'w')
            f.write('freq,txtone_pwr\n')

            if device_spa =="":
                self.spa = HP('SA',cfreq);
            else:
                self.spa = Agilent('SA',cfreq,device=device_spa);
            self.rfpll.set_freq(cfreq,restart_en=0)
            self.pbus.pbus_debugmode()
            self.pbus.open_tx(PA_gain,filter_gain)
            self.rfcal.tos()
            self.mem.wrm(0x600060a0, 17, 16, 3)#tx clock force
##            self.hals.HWI2C.bbtop.filter_wifitx0_dcap_lq=51
##            self.hals.HWI2C.bbtop.filter_wifitx0_dcap_hq=51
            #self.wifi.test_txtone_pwr(att,1,mode=0,step=0, delay_us=10)
            if bt_en ==1:
                bb1 = self.pbus.pbus_rd('bb', 'en1')
                self.pbus.pbus_wr('bb', 'en1', bb1|2)

            step_offset=int(bw*128/5)/2
            self.spa.set_param(cfreq,span=1,rb=3,vb=3)
            freq_r=[]
            pwr_r=[]
            w_str=''
            for step in range(4096-step_offset,4096+1):
                self.wifi.txtone_step(en1=1, step1=2*step-4096, att1=att, en2=0, step2=0, att2=0)
                cfreq_spa=float(cfreq)+float(2*(step-4096)*5)/128
                #print cfreq_spa
                self.spa.set_cfreq(cfreq_spa)
                if device_spa == "":
                    level=self.spa.pk_search(th=-80,pk_excursion=-40)[0][1]
                    self.spa.set_reflvl(int(level)+6)
                    result=self.spa.pk_search(th=-80,pk_excursion=-40)
                else:
    ##                level=self.spa.pk_search()[0][1]
    ##                self.spa.set_reflvl(int(level)+6)
                    result=self.spa.pk_search()
                freq_r.append(result[0][0])
                pwr_r.append(result[0][1])
                #time.sleep(0.1)
            for step in range(0,step_offset+1):
                self.wifi.txtone_step(en1=1, step1=2*step, att1=att, en2=0, step2=0, att2=0)
                cfreq_spa=float(cfreq)+float(2*step*5)/128
                self.spa.set_cfreq(cfreq_spa)
                if device_spa == "":
                    level=self.spa.pk_search(th=-80,pk_excursion=-40)[0][1]
                    self.spa.set_reflvl(int(level)+6)
                    result=self.spa.pk_search(th=-80,pk_excursion=-40)
                else:
    ##                level=self.spa.pk_search()[0][1]
    ##                self.spa.set_reflvl(int(level)+6)
                    result=self.spa.pk_search()
                freq_r.append(result[0][0])
                pwr_r.append(result[0][1])
                #time.sleep(0.1)
            #print freq_r
            #print pwr_r
            self.wifi.stoptone()
            for i in range(0,len(freq_r)):
                w_str+='%f'%freq_r[i]+','+'%f'%pwr_r[i]+'\n'
            f.write(w_str)
            f.closed

            pylab.ion()
            pylab.figure(filter_gain)
            pylab.plot(freq_r,pwr_r,label='filter_gain=0x%x'%filter_gain)
            pylab.xlabel('freq(MHZ)')
            pylab.ylabel('PWR(dbm)')
            pylab.legend()
            pylab.grid()
            pylab.savefig(self.curr_data_path+"tx filter gain_0x%x.png"%filter_gain)
            pylab.show()

    def filter_tx_ts(self, cfreq=2440, mixer_gain_list=range(0,8), device_spa='N9020A'):
        title = 'mixer_gain,h_gain_le,freq,txtone_pwr\n'
        fname = self.wifi.get_filename('ts_bt_test/', 'filter_tx_ts')
        fw1 = csvreport(fname, title)
        if device_spa == "":
            self.spa = HP('SA', cfreq)
        else:
            self.spa = Agilent('SA', cfreq, device=device_spa)

        chn = cfreq-2402
        self.mem_ts.wrm(0xa0422044, 10, 0, 0x7ff)  ##
        self.mem_ts.wrm(0xa0422040, 2, 0, 1)  ##tx send all '1's or all '0's
        self.mem_ts.wrm(0xa0422040, 8, 8, 1)  ##1: le mode, 0: bt mode
        self.mem_ts.wrm(0xa0422040, 9, 9, 1)  ##1: LE2M,	0:LE1M
        self.mem_ts.wr(0xa0422014, 0x0)  ##trx manual off
        self.mem_ts.wr(0xa0422014, 0xe)  ##manual tx on
        self.mem_ts.rfwr(0x22, (chn<<4)+0x4)  ##[10,4]set freq 2402+value MHz
        self.mem_ts.rfwr(0x10, 0x15fe)  ##pll cfg0
        self.mem_ts.rfwr(0x10, 0x75ff)  ##pll cfg1
        self.mem_ts.rfwr(0x24, 0x4)  ##start AFC cal
        self.mem_ts.rfwr(0x24, 0x0)  ##end AFC cal
        self.mem_ts.wrm(0xa0422040, 23, 23, 1)  ##assert tx ramp, should before modem txon
        self.mem_ts.wrm(0xa0422040, 14, 14, 1)  ##assert modem txon
        self.mem_ts.wrm(0xa0422040, 6, 4, 1)  ##assert symbol_flag_tx

        self.spa.set_param(cfreq, span=10, rb=3, vb=3)
        for mixer_gain in mixer_gain_list:
            self.mem_ts.rfwrm(0x83, 5,3,mixer_gain)  ##set mixer gain
            freq_r = []
            pwr_r = []
            step_list = []
            delta_txp = []
            for step in range(0, 65534,2000):
                self.mem_ts.wr(0xa04200e4,step)	##adjust h_gain/h_gain_le

                if device_spa == "":
                    level = self.spa.pk_search(th=-80, pk_excursion=-40)[0][1]
                    self.spa.set_reflvl(int(level) + 6)
                    result = self.spa.pk_search(th=-80, pk_excursion=-40)
                else:
                    ##                level=self.spa.pk_search()[0][1]
                    ##                self.spa.set_reflvl(int(level)+6)
                    result = self.spa.pk_search()
                freq_r.append(result[0][0])
                pwr_r.append(result[0][1])
                step_list.append(step*0.025)
                fw1.write_data([mixer_gain,step,result[0][0],result[0][1]])
                # time.sleep(0.1)
            for i in range(len(pwr_r)+1):
                delta_txp.append(pwr_r[i]-pwr_r[0])
            pylab.ion()
            pylab.figure(100)
            pylab.plot(step_list, delta_txp, label='filter_gain=0x%x' % mixer_gain)
            pylab.xlabel('freq_offset(KHZ)')
            pylab.ylabel('delta tx pwr(db)')
            pylab.legend()
            pylab.grid()
            # pylab.savefig(self.curr_data_path + "tx_filter_gain.png")
            pylab.show()

        pylab.savefig(self.curr_data_path + "tx_filter_gain.png")

    def filter_rx_epm9062(self, cfreq=2440,  device_spa='N9020A',if_bw=1, bw=4,step_acc=20):
        title = 'step_freq(MHz),measure_freq(KHz),txtone_pwr\n'
        fname = self.wifi.get_filename('ts_bt_test/', 'filter_rx_epm9062_{}m'.format(if_bw))
        fw1 = csvreport(fname, title)
        self.txg = mxg.MXG()
        # txg.arb_waveform(rate='LE_1M')
        self.txg.trriger_para_set(type='CONTinuous', count=1000)
        self.txg.output_state(1, 0)
        # txg.arb_state(1)
        self.txg.para_set(freq=cfreq, power=-60)
        if device_spa == "":
            self.spa = HP('SA', cfreq)
        else:
            self.spa = Agilent('SA', cfreq, device=device_spa)

        self.mem_ts.wr(0x50422014, 0x0)
        self.mem_ts.wrm(0x50421064, 12, 12, 1)  ##Frequency value manual enable
        self.mem_ts.wrm(0x50421064, 11, 0, cfreq)  ##Manual value of frequency (unit: MHz)
        # self.mem_ts.wrm(0xa012005c, 31, 16, 0)  ##
        # self.mem_ts.wrm(0xa0120038, 11, 8, 0)
        # self.mem_ts.wrm(0xa0120060, 7, 0, 0)  ##PC8/9/10/11
        self.mem_ts.wrm(0xa0000144, 29, 29, 1)  ##bbpll_bg_pup_ibg_tbuf
        self.mem_ts.wrm(0xa0120098, 4, 4, 1)  ##test buf en
        ##self.mem_ts.wrm(0xa01200c8,3,2,2)	##tx IF test buf
        self.mem_ts.wrm(0xa0120098, 3, 2, 1)  ##rx IF test buf

        self.mem_ts.wrm(0x504210a0, 0, 0, 1)  ##agc off

        self.spa.set_param(1, span=0.3, rb=1, vb=1)
        self.mem_ts.wr(0x50422014, 0x0)  ##manual rxon disable
        time.sleep(1)
        self.mem_ts.wr(0x50422014, 0x3)  ##manual rxon enable
        freq_r = []
        pwr_r = []
        step_list = range((-bw) * 1000 / step_acc, (bw) * 1000 / step_acc, 1)
        delta_txp = []
        mxg_freq = cfreq
        for step in step_list:
            step = step * step_acc / 1000.000
            mxg_freq = cfreq + step
            self.txg.set_cfreq(mxg_freq)

            self.spa.set_cfreq(abs(step+if_bw))

            if device_spa == "":
                level = self.spa.pk_search(th=-80, pk_excursion=-40)[0][1]
                self.spa.set_reflvl(int(level) + 6)
                result = self.spa.pk_search(th=-80, pk_excursion=-40)
            else:
                ##                level=self.spa.pk_search()[0][1]
                ##                self.spa.set_reflvl(int(level)+6)
                result = self.spa.pk_search()
            freq_r.append(result[0][0])
            pwr_r.append(result[0][1])
            fw1.write_data(
                [ step, result[0][0], result[0][1]])

    def filter_rx_epm9062_debug(self, cfreq=2440, cbpf_if_list=['1M', '1.5M','3M','4M'],
                        device_spa='N9020A', step_acc=20,bw=10):

        cbpf_ifsel_dict = {
            '1M': 3,
            '1.5M': 2,
            '3M': 1,
            '4M': 0
        }
        cbpf_ifbw_dict = {
            '1M': 1,
            '1.5M': 1.5,
            '3M': 3,
            '4M': 4
        }
        cbpf_ifvalue_dict = {
            '1M': 0x155556,
            '1.5M': 0x200001,
            '3M': 0x400002,
            '4M': 0x555558
        }
        cbpf_iop1_dict = {
            '1M': 1,
            '1.5M': 3,
            '3M': 4,
            '4M': 7
        }
        cbpf_iop2_dict = {
            '1M': 1,
            '1.5M': 1,
            '3M': 4,
            '4M': 7
        }
        for flt_bw in cbpf_if_list:
            cbpf_ifbw = cbpf_ifbw_dict[flt_bw]
            cbpf_ifsel = cbpf_ifsel_dict[flt_bw]
            ifvalue = cbpf_ifvalue_dict[flt_bw]
            cbpf_iop1 = cbpf_iop1_dict[flt_bw]
            cbpf_iop2 = cbpf_iop2_dict[flt_bw]
            self.mem_ts.wrm(0x50421100, 1, 0, cbpf_ifsel)  ##Rx CBPF IF select
            self.mem_ts.wrm(0x50421070, 22, 0, ifvalue)
            self.mem_ts.wrm(0x50421104, 2, 0, cbpf_iop1)
            self.mem_ts.wrm(0x50421104, 17, 15, cbpf_iop2)
            self.filter_rx_epm9062(cfreq=cfreq,  device_spa=device_spa,if_bw=cbpf_ifbw, bw=bw,step_acc=step_acc)


    def filter_rx_tx232(self, cfreq=2440, cbpf_if_list=['1M','1.5M'], flt_index_list=['cbpf1','cbpf1&2'], rccal_code_val_list=range(1,31,2), cbpf_bw_code_list=[2],
                        device_spa='N9020A', step_acc=20):
        title = 'rccal_code_val,IF,flt_mode,cbpf_bw_code,step_freq(MHz),measure_freq(KHz),txtone_pwr\n'
        fname = self.wifi.get_filename('ts_bt_test/', 'filter_rx_tx232')
        fw1 = csvreport(fname, title)
        self.txg = mxg.MXG()
        # txg.arb_waveform(rate='LE_1M')
        self.txg.trriger_para_set(type='CONTinuous', count=1000)
        self.txg.output_state(1, 0)
        # txg.arb_state(1)
        self.txg.para_set(freq=cfreq, power=-60)
        if device_spa == "":
            self.spa = HP('SA', cfreq)
        else:
            self.spa = Agilent('SA', cfreq, device=device_spa)

        self.mem_ts.wr(0xa0422014, 0x0)
        self.mem_ts.wrm(0xa0421064, 12, 12, 1)  ##Frequency value manual enable
        self.mem_ts.wrm(0xa0421064, 11, 0, cfreq)  ##Manual value of frequency (unit: MHz)
        self.mem_ts.wrm(0xa012005c, 31, 16, 0)  ##
        self.mem_ts.wrm(0xa0120038, 11, 8, 0)
        self.mem_ts.wrm(0xa0120060, 7, 0, 0)  ##PC8/9/10/11
        self.mem_ts.wrm(0xa01200a0, 29, 29, 1)  ##bbpll_bg_pup_ibg_tbuf
        self.mem_ts.wrm(0xa01200c8, 4, 4, 1)  ##test buf en
        ##self.mem_ts.wrm(0xa01200c8,3,2,2)	##tx IF test buf
        self.mem_ts.wrm(0xa01200c8, 3, 2, 1)  ##rx IF test buf

        self.mem_ts.wrm(0xa04210a0, 0, 0, 1)    ##agc off
        # self.mem_ts.wrm(0xa04210b4, 25, 25, 1)
        # self.mem_ts.wrm(0xa04210b4, 24, 19, 0x3f)


        # self.mem_ts.wrm(0xa0422044, 10, 0, 0x7ff)  ##
        # self.mem_ts.wrm(0xa0422040, 2, 0, 1)  ##tx send all '1's or all '0's
        # self.mem_ts.wrm(0xa0422040, 8, 8, 1)  ##1: le mode, 0: bt mode
        # self.mem_ts.wrm(0xa0422040, 9, 9, 1)  ##1: LE2M,	0:LE1M
        # self.mem_ts.wr(0xa0422014, 0x0)  ##trx manual off
        # self.mem_ts.wr(0xa0422014, 0xe)  ##manual tx on
        # self.mem_ts.rfwr(0x22, (chn<<4)+0x4)  ##[10,4]set freq 2402+value MHz
        # self.mem_ts.rfwr(0x10, 0x15fe)  ##pll cfg0
        # self.mem_ts.rfwr(0x10, 0x75ff)  ##pll cfg1
        # self.mem_ts.rfwr(0x24, 0x4)  ##start AFC cal
        # self.mem_ts.rfwr(0x24, 0x0)  ##end AFC cal
        # self.mem_ts.wrm(0xa0422040, 23, 23, 1)  ##assert tx ramp, should before modem txon
        # self.mem_ts.wrm(0xa0422040, 14, 14, 1)  ##assert modem txon
        # self.mem_ts.wrm(0xa0422040, 6, 4, 1)  ##assert symbol_flag_tx

        self.spa.set_param(1, span=0.3, rb=1, vb=1)
        for rccal_code_val in rccal_code_val_list:
            self.mem_ts.wrm(0xa0421044, 26, 26, 1)
            self.mem_ts.wrm(0xa0421044, 31, 27, rccal_code_val)
            for flt_bw in cbpf_if_list:
                if flt_bw == '1M':
                    self.mem_ts.wrm(0xa0421034, 14, 14, 0)  ##Rx CBPF IF select
                else:
                    self.mem_ts.wrm(0xa0421034, 14, 14, 1)  ##Rx CBPF IF select

                for flt_index in flt_index_list:
                    if flt_index == 'cbpf1':
                        self.mem_ts.wrm(0xa0421020, 20, 20, 0)  ##Rx CBPF mode
                    else:
                        self.mem_ts.wrm(0xa0421020, 20, 20, 1)  ##Rx CBPF mode

                    for cbpf_bw_code in cbpf_bw_code_list:
                        self.mem_ts.wrm(0xa0421034, 13, 12, cbpf_bw_code)

                        self.mem_ts.wr(0xa0422014, 0x0)  ##manual rxon disable
                        time.sleep(1)
                        self.mem_ts.wr(0xa0422014, 0x3)  ##manual rxon enable
                        freq_r = []
                        pwr_r = []
                        step_list = range(-4*1000/step_acc, 4*1000/step_acc,1)
                        delta_txp = []
                        mxg_freq = cfreq
                        for step in step_list:
                            step = step * step_acc/1000.000
                            mxg_freq = cfreq + step
                            self.txg.set_cfreq(mxg_freq)

                            self.spa.set_cfreq(abs(step+1))

                            if device_spa == "":
                                level = self.spa.pk_search(th=-80, pk_excursion=-40)[0][1]
                                self.spa.set_reflvl(int(level) + 6)
                                result = self.spa.pk_search(th=-80, pk_excursion=-40)
                            else:
                                ##                level=self.spa.pk_search()[0][1]
                                ##                self.spa.set_reflvl(int(level)+6)
                                result = self.spa.pk_search()
                            freq_r.append(result[0][0])
                            pwr_r.append(result[0][1])
                            fw1.write_data([rccal_code_val,flt_bw,flt_index,cbpf_bw_code,step,result[0][0],result[0][1]])
                            # time.sleep(0.1)
                        # for i in range(len(pwr_r)+1):
                        #     delta_txp.append(pwr_r[i]-pwr_r[0])
                        pylab.ion()
                        pylab.figure(100)
                        pylab.plot(step_list, pwr_r, label='cbpf IF={}, {},rc_code={},cbpf_bw_code={}'.format(flt_bw,flt_index,rccal_code_val,cbpf_bw_code))
                        pylab.xlabel('freq(100KHZ)')
                        pylab.ylabel('tx pwr(db)')
                        pylab.legend()
                        pylab.grid()
                        # pylab.savefig(self.curr_data_path + "tx_filter_gain.png")
                        pylab.show()

                        pylab.savefig(self.curr_data_path + "rx_filter_tx232_{}_{}_{}_{}.png".format(flt_bw,flt_index,rccal_code_val,cbpf_bw_code))

    def filter_rx_tx232_debug(self, cfreq=2440, cbpf_if_list=['1M','1.5M'], flt_index_list=['cbpf1','cbpf1&2'], rccal_code_val_list=range(1,31,2), cbpf_bw_code_list=[2],
                        device_spa='N9020A', step_acc=20):
        title = 'cbpf_vcm_trim,cbpf_bias_trim,rccal_code_val,IF,flt_mode,cbpf_bw_code,step_freq(MHz),measure_freq(KHz),txtone_pwr\n'
        fname = self.wifi.get_filename('ts_bt_test/', 'filter_rx_tx232')
        fw1 = csvreport(fname, title)
        self.txg = mxg.MXG()
        # txg.arb_waveform(rate='LE_1M')
        self.txg.trriger_para_set(type='CONTinuous', count=1000)
        self.txg.output_state(1, 0)
        # txg.arb_state(1)
        self.txg.para_set(freq=cfreq, power=-60)
        if device_spa == "":
            self.spa = HP('SA', cfreq)
        else:
            self.spa = Agilent('SA', cfreq, device=device_spa)

        self.mem_ts.wr(0xa0422014, 0x0)
        self.mem_ts.wrm(0xa0421064, 12, 12, 1)  ##Frequency value manual enable
        self.mem_ts.wrm(0xa0421064, 11, 0, cfreq)  ##Manual value of frequency (unit: MHz)
        self.mem_ts.wrm(0xa012005c, 31, 16, 0)  ##
        self.mem_ts.wrm(0xa0120038, 11, 8, 0)
        self.mem_ts.wrm(0xa0120060, 7, 0, 0)  ##PC8/9/10/11
        self.mem_ts.wrm(0xa01200a0, 29, 29, 1)  ##bbpll_bg_pup_ibg_tbuf
        self.mem_ts.wrm(0xa01200c8, 4, 4, 1)  ##test buf en
        ##self.mem_ts.wrm(0xa01200c8,3,2,2)	##tx IF test buf
        self.mem_ts.wrm(0xa01200c8, 3, 2, 1)  ##rx IF test buf

        self.mem_ts.wrm(0xa04210a0, 0, 0, 1)    ##agc off
        # self.mem_ts.wrm(0xa04210b4, 25, 25, 1)
        # self.mem_ts.wrm(0xa04210b4, 24, 19, 0x3f)
        # self.mem_ts.wrm(0xa0422044, 10, 0, 0x7ff)  ##
        # self.mem_ts.wrm(0xa0422040, 2, 0, 1)  ##tx send all '1's or all '0's
        # self.mem_ts.wrm(0xa0422040, 8, 8, 1)  ##1: le mode, 0: bt mode
        # self.mem_ts.wrm(0xa0422040, 9, 9, 1)  ##1: LE2M,	0:LE1M
        # self.mem_ts.wr(0xa0422014, 0x0)  ##trx manual off
        # self.mem_ts.wr(0xa0422014, 0xe)  ##manual tx on
        # self.mem_ts.rfwr(0x22, (chn<<4)+0x4)  ##[10,4]set freq 2402+value MHz
        # self.mem_ts.rfwr(0x10, 0x15fe)  ##pll cfg0
        # self.mem_ts.rfwr(0x10, 0x75ff)  ##pll cfg1
        # self.mem_ts.rfwr(0x24, 0x4)  ##start AFC cal
        # self.mem_ts.rfwr(0x24, 0x0)  ##end AFC cal
        # self.mem_ts.wrm(0xa0422040, 23, 23, 1)  ##assert tx ramp, should before modem txon
        # self.mem_ts.wrm(0xa0422040, 14, 14, 1)  ##assert modem txon
        # self.mem_ts.wrm(0xa0422040, 6, 4, 1)  ##assert symbol_flag_tx
        self.spa.set_param(1, span=0.3, rb=1, vb=1)
        # for cbpf_vcm_trim in range(0,4):
        for cbpf_vcm_trim in [2]:
            self.mem_ts.wrm(0xa0421034, 20, 19, cbpf_vcm_trim)
            # for cbpf_bias_trim in range(0,8):
            for cbpf_bias_trim in [2]:
                self.mem_ts.wrm(0xa0421034, 18, 16, cbpf_bias_trim)
                for rccal_code_val in rccal_code_val_list:
                # for rccal_code_val in [1]:
                    self.mem_ts.wrm(0xa0421044, 26, 26, 1)
                    self.mem_ts.wrm(0xa0421044, 31, 27, rccal_code_val)
                    for flt_bw in cbpf_if_list:
                        if flt_bw == '1M':
                            rx_if = 1
                            if self.chipv == 'TX232_MPW3':
                                self.mem_ts.wrm(0xa0421034, 15, 15, 0)  ##Rx CBPF IF select
                            else:
                                self.mem_ts.wrm(0xa0421034, 14, 14, 0)  ##Rx CBPF IF select
                        else:
                            rx_if = 1.5
                            if self.chipv == 'TX232_MPW3':
                                self.mem_ts.wrm(0xa0421024, 21, 20, 3)  ##BLE 2Mbps mode manual control
                                self.mem_ts.wrm(0xa0421034, 15, 15, 1)  ##Rx CBPF IF select 1.5M
                            else:
                                self.mem_ts.wrm(0xa0421034, 14, 14, 1)  ##Rx CBPF IF select

                        for flt_index in flt_index_list:
                            if flt_index == 'cbpf1':
                                self.mem_ts.wrm(0xa0421020, 20, 20, 0)  ##Rx CBPF mode
                            else:
                                self.mem_ts.wrm(0xa0421020, 20, 20, 1)  ##Rx CBPF mode

                            for cbpf_bw_code in cbpf_bw_code_list:
                                self.mem_ts.wrm(0xa0421034, 13, 12, cbpf_bw_code)

                                self.mem_ts.wr(0xa0422014, 0x0)  ##manual rxon disable
                                time.sleep(1)
                                self.mem_ts.wr(0xa0422014, 0x3)  ##manual rxon enable
                                freq_r = []
                                pwr_r = []
                                # step_list = range(-4*1000/step_acc, 4*1000/step_acc,1)
                                step_list = range(-4 * 1000 / step_acc, -15 * 100 / step_acc, 5) + range(-15 * 100 / step_acc, 15 * 100 / step_acc, 1) + range(15 * 100 /
                                                                                                                                                               step_acc,
                                                                                                                                                               41 * 100 /
                                                                                                                                                               step_acc, 5)
                                delta_txp = []
                                mxg_freq = cfreq
                                for step in step_list:
                                    step = step * step_acc/1000.000
                                    mxg_freq = cfreq + step
                                    self.txg.set_cfreq(mxg_freq)

                                    self.spa.set_cfreq(abs(step+rx_if))
                                    loginfo('cbpf_vcm_trim,cbpf_bias_trim,rccal_code_val,flt_bw,flt_index,cbpf_bw_code,step\n{} {}  {}  {}  {}  {}  {}'.format(cbpf_vcm_trim,cbpf_bias_trim,rccal_code_val,flt_bw,flt_index,cbpf_bw_code,step))
                                    if device_spa == "":
                                        level = self.spa.pk_search(th=-80, pk_excursion=-40)[0][1]
                                        self.spa.set_reflvl(int(level) + 6)
                                        result = self.spa.pk_search(th=-80, pk_excursion=-40)
                                    else:
                                        ##                level=self.spa.pk_search()[0][1]
                                        ##                self.spa.set_reflvl(int(level)+6)
                                        result = self.spa.pk_search()
                                    freq_r.append(result[0][0])
                                    pwr_r.append(result[0][1])
                                    fw1.write_data([cbpf_vcm_trim,cbpf_bias_trim,rccal_code_val,flt_bw,flt_index,cbpf_bw_code,step,result[0][0],result[0][1]])
                                    # time.sleep(0.1)
                                # for i in range(len(pwr_r)+1):
                                #     delta_txp.append(pwr_r[i]-pwr_r[0])
                                # pylab.ion()
                                # pylab.figure(100)
                                # pylab.plot(step_list, pwr_r, label='cbpf IF={}, {},rc_code={},cbpf_bw_code={}'.format(flt_bw,flt_index,rccal_code_val,cbpf_bw_code))
                                # pylab.xlabel('freq(100KHZ)')
                                # pylab.ylabel('tx pwr(db)')
                                # pylab.legend()
                                # pylab.grid()
                                # # pylab.savefig(self.curr_data_path + "tx_filter_gain.png")
                                # pylab.show()
                                #
                                # pylab.savefig(self.curr_data_path + "rx_filter_tx232_{}_{}_{}_{}.png".format(flt_bw,flt_index,rccal_code_val,cbpf_bw_code))

    def filter_tx_dcap_sweep(self,cfreq=2437, bw=30,  device_spa='E4404B',step=1,bt_en_list=[0,1],dedge_list=[0,7],dcap_list=[15,38,63]):

        if device_spa =="":
            self.spa = HP('SA',cfreq);
        else:
            self.spa = Agilent('SA',cfreq,device=device_spa);

##        self.rfpll.set_freq(cfreq,restart_en=0)
        self.wifi.rfchsel(6,0)
##        self.wifi.force_txon(1)
        self.pbus.pbus_debugmode()
        self.pbus.open_tx(0x5f,0x10)
        self.rfcal.tos()
##        self.mem.wrm(0x600060a0, 17, 16, 3)#tx clock force
        for bt_en in bt_en_list:
            if bt_en==1:
                name_str="BT"
                bb1 = self.pbus.pbus_rd('bb', 'en1')
                self.pbus.pbus_wr('bb', 'en1', bb1|2)

            else:
                name_str="wifi"
                bb1 = self.pbus.pbus_rd('bb', 'en1')
                self.pbus.pbus_wr('bb', 'en1', bb1&0x1fd)

            filetime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()));
            title = 'dedge,dcap,freq,txtone_pwr\n'
            fname = self.wifi.get_filename('filter_tx_dcap_sweep', 'filter_tx_dcap_sweep_%s'%name_str)
            csvreport1 = csvreport(fname, title)

            for dedge in dedge_list:
                if self.chipv=='CHIP724':
                    self.hals.HWI2C.bbtop.filter_wftx0_dedge=0
                    self.hals.HWI2C.bbtop.filter_bttx0_dedge=0
                elif self.chipv=='CHIP722' or self.chipv=='CHIP723':
                    self.hals.HWI2C.bbtop.filter_wifitx0_dedge=0
                elif self.chipv=='ESP32':
                    self.hals.HWI2C.bbtop.filter_wifitx_dedge=0
                    self.hals.HWI2C.bbtop.filter_bttx_dedge=0
                for dcap in dcap_list:
                    if dcap<20:
                        bw=60
                    elif 20<dcap<40:
                        bw=50
                    else:
                        bw=40
                    if bt_en==1:
                        if self.chipv=='CHIP724':
                            self.hals.HWI2C.bbtop.filter_bttx0_dcap_lq=dcap
                            self.hals.HWI2C.bbtop.filter_bttx0_dcap_hq=dcap
                        elif self.chipv=='ESP32':
                            self.hals.HWI2C.bbtop.filter_bttx_dcap_lq=dcap
                            self.hals.HWI2C.bbtop.filter_bttx_dcap_hq=dcap
                        bw=bw/5
                        step_div=step
                    else:
                        if self.chipv=='CHIP724':
                            self.hals.HWI2C.bbtop.filter_wftx0_dcap_lq=dcap
                            self.hals.HWI2C.bbtop.filter_wftx0_dcap_hq=dcap
                        elif self.chipv=='CHIP722' or self.chipv=='CHIP723':
                            self.hals.HWI2C.bbtop.filter_wifitx0_dcap_lq=dcap
                            self.hals.HWI2C.bbtop.filter_wifitx0_dcap_hq=dcap
                        elif self.chipv=='ESP32':
                            self.hals.HWI2C.bbtop.filter_wifitx_dcap_lq=dcap
                            self.hals.HWI2C.bbtop.filter_wifitx_dcap_hq=dcap
                        step_div=2*step
                    #self.wifi.test_txtone_pwr(att,1,mode=0,step=0, delay_us=10)


                    step_offset=int(bw*128/5)/2
                    self.spa.set_param(cfreq,span=1,rb=3,vb=3)
                    self.spa.set_reflvl=15

                    for step in range(4096-step_offset,4096+1,step_div):
                        self.wifi.txtone_step(en1=1, step1=step, att1=60, en2=0, step2=0, att2=0)
                        cfreq_spa=float(cfreq)+float((step-4096)*5)/128
                        #print cfreq_spa
                        self.spa.set_cfreq(cfreq_spa)
                        if device_spa == "":
                            level=self.spa.pk_search(th=-80,pk_excursion=-40)[0][1]
                            self.spa.set_reflvl(int(level)+6)
                            result=self.spa.pk_search(th=-80,pk_excursion=-40)
                        else:
                            result=self.spa.pk_search()

                        csvreport1.write_data(dedge,dcap,[result[0][0],result[0][1]],float_num=6)

                    for step in range(0,step_offset+1,step_div):
                        self.wifi.txtone_step(en1=1, step1=step, att1=60, en2=0, step2=0, att2=0)
                        cfreq_spa=float(cfreq)+float(step*5)/128
                        self.spa.set_cfreq(cfreq_spa)
                        if device_spa == "":
                            level=self.spa.pk_search(th=-80,pk_excursion=-40)[0][1]
                            self.spa.set_reflvl(int(level)+6)
                            result=self.spa.pk_search(th=-80,pk_excursion=-40)
                        else:
                            result=self.spa.pk_search()

                        csvreport1.write_data(dedge,dcap,[result[0][0],result[0][1]],float_num=6)

        self.wifi.stoptone()

##            pylab.ion()
##            pylab.figure(filter_gain)
##            pylab.plot(freq_r,pwr_r,label='filter_gain=0x%x'%filter_gain)
##            pylab.xlabel('freq(MHZ)')
##            pylab.ylabel('PWR(dbm)')
##            pylab.legend()
##            pylab.grid()
##            pylab.savefig(self.curr_data_path+"tx filter gain_0x%x.png"%filter_gain)
##            pylab.show()


    def filter_rx(self,force_gain=5, chan=1,bw=13,bw_rb=10, bt_en=0,est_len=1024,dcap_lq=40,dcap_hq=40,dedge=0,plot_en=1,board_name=""):
        filetime = time.strftime('_%Y%m%d_%H%M%S',time.localtime(time.time()));
        chip_id= self.chipid.chip_mac()
        file=self.curr_data_path + 'rx_filter_%s_%s.csv'%(chip_id,filetime)
        f=open(file,'w')
        f.write('freq,filter_dcap,tot_pwr,tot_pwr_db,i_pwr,q_pwr,i_amp,q_amp\n')
        self.wifi.rfchsel(chan)
        if bt_en==1:
            self.mem.wrm(0x6001c080,7,6,3) #force bt_mode
            self.mem.wrm(0x60011018,31,31,1) #force bt_rx_en
        self.mem.wrm(0x6001c02c,31,23,(((force_gain)<<1) | 1)) #force gain(for rssi=-68)
        freq=2412+5*(chan-1)
        a=sme.sme("SME06")
        a.setpow(-10)
        a.rfon()
        w_str=''
        step_offset=int(bw*bw_rb)
        result=[]
        tot_pwr=[]
        tot_pwr_db_list=[]
        i_pwr=[]
        q_pwr=[]
        i_amp=[]
        q_amp=[]
        freq_set=[]

##        for dcap_lq in (20,40):
##        self.hals.HWI2C.bbtop.filter_wfrx0_dcap_lq=dcap_lq
##        self.hals.HWI2C.bbtop.filter_wfrx0_dcap_hq=dcap_lq
##        self.hals.HWI2C.bbtop.filter_wfrx0_dedge=dedge
##        self.hals.HWI2C.bbtop.filter_btrx0_dedge=dedge
        for step in range(-step_offset,step_offset,1):
            freq_sme=float(freq)+float(step)/bw_rb
            print freq_sme
            a.setfreq(freq_sme*1000000)
            result=self.iq_est.get_iqest_power(est_len)
            time.sleep(0.1)
            tot_pwr_db=10*np.log10(result[0])
            tot_pwr_db_list.append(tot_pwr_db)
            tot_pwr.append(result[0])
            i_pwr.append(result[1])
            q_pwr.append(result[2])
            i_amp.append(result[3])
            q_amp.append(result[4])
            freq_set.append(freq_sme)
            w_str+='%f'%freq_sme+','+'%d'%dcap_lq+','+'%f'%result[0]+','+'%f'%tot_pwr_db+','+'%f'%result[1]+','+'%f'%result[2]+','+'%f'%result[3]+','+'%f'%result[4]+'\n'
        f.write(w_str)
        f.closed
        if plot_en!=0:
            pylab.ion()
            pylab.figure(freq)
            pylab.subplot(211)
            pylab.plot(freq_set,tot_pwr,label='filter_wifirx0_dcap_lq=%s')
            pylab.xlabel('freq(MHZ)')
            pylab.ylabel('value')
            pylab.legend()
            pylab.grid()
            pylab.subplot(212)
            pylab.plot(freq_set,tot_pwr_db_list,label='filter_wifirx0_dcap_lq=%s')
            pylab.xlabel('freq(MHZ)')
            pylab.ylabel('db')
            pylab.legend()
            pylab.grid()
            #pylab.savefig(self.curr_data_path+"rxfilter_%s"%board_name)
            pylab.show()

    def filter_rx_dcap_sweep(self,force_gain=5, chan=1,bw=13,bw_rb=10,est_len=1024,bt_en_list=[0,1],dedge_list=[0,7],dcap_list=[15,38,63]):

        self.wifi.rfchsel(chan)
        self.pbus.pbus_debugmode()
##        if self.chipv=="CHIP724" or self.chipv=="ESP32":
##            bt_en_list=[0,1]
##        else:
##            bt_en_list=[0]

        self.hals.HWI2C.bbtop.encmplx_btrx=0
        for bt_en in bt_en_list:
##            bt_en=1
            print "bt_en:%d"%bt_en
            if bt_en==1:
                name_str="BT"
                bb1 = self.pbus.pbus_rd('bb', 'en1')
                self.pbus.pbus_wr('bb', 'en1', bb1|2)
                if self.chipv=="CHIP724":
                    txen2=self.pbus.pbus_rd('rftx1','en2')
                    self.pbus.pbus_wr('rftx1','en2',txen2|0x18)
            else:
                name_str="wifi"
                bb1 = self.pbus.pbus_rd('bb', 'en1')
                self.pbus.pbus_wr('bb', 'en1', bb1&0x1fd)
                if self.chipv=="CHIP724":
                    txen2=self.pbus.pbus_rd('rftx1','en2')
                    self.pbus.pbus_wr('rftx1','en2',txen2&0x1e7)

            filetime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()));
            title = 'freq,dedge,filter_dcap,tot_pwr,tot_pwr_db,i_pwr,q_pwr,i_amp,q_amp\n'
            fname = self.wifi.get_filename('test_rxfilter_dcap', 'test_rxfilter_dcap_%s'%name_str)
            csvreport1 = csvreport(fname, title)

##        self.wifi.rfchsel(chan)
##        if bt_en==1:
##            self.pbus.pbus_debugmode()
##            bb1 = self.pbus.pbus_rd('bb', 'en1')
##            self.pbus.pbus_wr('bb', 'en1', bb1|2)
##            if self.chipv=="CHIP724":
##                self.pbus.pbus_wr('rftx1','en2',0x8)
####            self.mem.wrm(0x6001c080,7,6,3) #force bt_mode
####            self.mem.wrm(0x60011018,31,31,1) #force bt_rx_en
            self.mem.wrm(0x6001c02c,31,23,(((force_gain)<<1) | 1)) #force gain(for rssi=-68)
            freq=2412+5*(chan-1)
            a=sme.sme("SME06")
            a.setpow(-30)
            a.rfon()
            w_str=''
            result=[]
            tot_pwr=[]
            i_pwr=[]
            q_pwr=[]
            i_amp=[]
            q_amp=[]
            freq_set=[]
            if bt_en==1:
                bw=bw/5
                bw_rb=bw_rb*5
            for dedge in dedge_list:
                if bt_en==1:
                    self.hals.HWI2C.bbtop.filter_btrx0_dedge=dedge
                    self.hals.HWI2C.bbtop.filter_btrx1_dedge=dedge
                    self.hals.HWI2C.bbtop.filter_btrx2_dedge=dedge
                    self.hals.HWI2C.bbtop.filter_btrx3_dedge=dedge

                    self.hals.HWI2C.bbtop.filter_bttx0_dedge=dedge
                    self.hals.HWI2C.bbtop.filter_bttx1_dedge=dedge
                    self.hals.HWI2C.bbtop.filter_bttx2_dedge=dedge
                    self.hals.HWI2C.bbtop.filter_bttx3_dedge=dedge
                else:
                    if self.chipv=="CHIP724":
                        self.hals.HWI2C.bbtop.filter_wfrx0_dedge=dedge
                    elif self.chipv=='CHIP723' or self.chipv=='CHIP722' :
                        self.hals.HWI2C.bbtop.filter_wifirx0_dedge=dedge
                    elif self.chipv=='ESP32':
                        self.hals.HWI2C.bbtop.filter_wifirx_dedge=dedge
                bw1=bw
                for dcap in dcap_list:
                    if bt_en==1:
                        self.hals.HWI2C.bbtop.filter_btrx0_dcap_lq=dcap
                        self.hals.HWI2C.bbtop.filter_btrx0_dcap_hq=dcap
                        self.hals.HWI2C.bbtop.filter_btrx1_dcap_lq=dcap
                        self.hals.HWI2C.bbtop.filter_btrx1_dcap_hq=dcap
                        self.hals.HWI2C.bbtop.filter_btrx2_dcap_lq=dcap
                        self.hals.HWI2C.bbtop.filter_btrx2_dcap_hq=dcap
                        self.hals.HWI2C.bbtop.filter_btrx3_dcap_lq=dcap
                        self.hals.HWI2C.bbtop.filter_btrx3_dcap_hq=dcap
                    else:
                        if self.chipv=='CHIP724':
                            self.hals.HWI2C.bbtop.filter_wfrx0_dcap_lq=dcap
                            self.hals.HWI2C.bbtop.filter_wfrx0_dcap_hq=dcap
                        elif self.chipv=='CHIP723' or self.chipv=='CHIP722' :
                            self.hals.HWI2C.bbtop.filter_wifirx0_dcap_lq=dcap
                            self.hals.HWI2C.bbtop.filter_wifirx0_dcap_hq=dcap
                        elif self.chipv=='ESP32':
                            self.hals.HWI2C.bbtop.filter_wfrx_dcap_lq=dcap
                            self.hals.HWI2C.bbtop.filter_wfrx_dcap_hq=dcap

                    step_offset=bw1*bw_rb

                    for step in range(-step_offset,step_offset,2):
                        freq_sme=float(freq)+float(step)/bw_rb
                        print freq_sme
                        a.setfreq(freq_sme*1000000)
                        result=self.iq_est.get_iqest_power(est_len)
                        time.sleep(0.1)
                        tot_pwr_db=10*np.log10(result[0])
                        tot_pwr.append([freq_sme,tot_pwr_db])
                        i_pwr.append(result[1])
                        q_pwr.append(result[2])
                        i_amp.append(result[3])
                        q_amp.append(result[4])
                        freq_set.append(freq_sme)
                        csvreport1.write_data([freq_sme,dedge,dcap,result[0],tot_pwr_db,result[1],result[2],result[3],result[4]])
        ##                w_str+='%f'%freq_sme+','+'%d'%dcap_lq+','+'%f'%result[0]+','+'%f'%tot_pwr_db+','+'%f'%result[1]+','+'%f'%result[2]+','+'%f'%result[3]+','+'%f'%result[4]+'\n'
                    if bt_en==1:
                        bw1=bw1-2
                    else:
                        bw1=bw1-5
##        f.write(w_str)
##        f.closed

    def read_csv_filter(self,fname="",mode=1):
        if mode==1:
            with open(fname) as f:
                f_csv=csv.reader(f)
                headers=next(f_csv)
                    #print headers
                rx_pwr=[]
                freq=[]
                tx_power=[]
                i_amp=[]
                for row in f_csv:
                    print row[0],row[1]
                    freq.append(float(row[0]))
                    tx_power.append(float(row[1]))
##                    rx_pwr.append(10*np.log10(float(row[1])))
##                    i_amp.append(float(row[4]))
            pylab.ion()
            pylab.figure(100)
            pylab.plot(freq,tx_power,label='deafult')
            pylab.xlabel('freq(MHZ)')
            pylab.ylabel('PWR(db)')
            pylab.legend()
            pylab.grid()
            pylab.show()
        else:
            with open(fname) as f:
                f_csv=csv.reader(f)
                headers=next(f_csv)
                    #print headers
                rx_pwr=[]
                freq=[]
                tx_power=[]
                i_amp=[]
                for row in f_csv:
                    print row[0],row[1]
                    freq.append(float(row[0]))
##                    tx_power.append(float(row[1]))
                    rx_pwr.append(10*np.log10(float(row[1])))
                    i_amp.append(float(row[4]))
            pylab.ion()
##            pylab.figure(100)
##            pylab.plot(freq,tx_power,label='deafult')
##            pylab.xlabel('freq(MHZ)')
##            pylab.ylabel('PWR(db)')
##            pylab.legend()
##            pylab.grid()
##            pylab.show()
            pylab.figure(100)
            pylab.subplot(210)
            pylab.plot(freq,rx_pwr,label='deafult')
            pylab.xlabel('freq(MHZ)')
            pylab.ylabel('PWR(db)')
            pylab.legend()
            pylab.grid()
            pylab.subplot(211)
            pylab.plot(freq,i_amp,label='deafult')
            pylab.xlabel('freq(MHZ)')
            pylab.ylabel('amp')
            pylab.legend()
            pylab.grid()
            pylab.show()


    def filter_dcap_data_anay(self,data_file=""):
        filetime = time.strftime('_%Y%m%d_%H%M%S',time.localtime(time.time()));
        chip_id= self.chipid.chip_mac()
        file=self.curr_data_path + 'rx_filter_band_dcap_%s_%s.csv'%(chip_id,filetime)
        f=open(file,'w')
        f.write('chipid,filter_dcap,filter_band\n')
        w_str=''
        data=pd.read_csv(data_file)
        df=pd.DataFrame(data)
        for dcap in range(15,64,4):
##            tot_pwr_ref=df.tot_pwr_db[df.freq==2442][df.filter_dcap==dcap]
            tot_pwr_left=df.tot_pwr_db[df.filter_dcap==dcap][df.freq<2442][df.tot_pwr_db>27]
            print tot_pwr_left
            for i in range(1,len(tot_pwr_left)):
                print tot_pwr_left.iloc[i]
                if tot_pwr_left.iloc[i]>tot_pwr_left.iloc[i+1]:
                    tot_pwr_left_ref=tot_pwr_left.iloc[i]
                    break
            freq_down_ref=df.freq[df.filter_dcap==dcap][df.freq<2442][df.tot_pwr_db==tot_pwr_left_ref].iloc[0]
            print freq_down_ref

            tot_pwr_right=df.tot_pwr_db[df.filter_dcap==dcap][df.freq>2442][df.tot_pwr_db>27].sort_index(axis=0,ascending=False)
            print"right"
            print tot_pwr_right
            for i in range(1,len(tot_pwr_right)):
                print tot_pwr_right.iloc[i]
                if tot_pwr_right.iloc[i]>tot_pwr_right.iloc[i+1]:

                    tot_pwr_right_ref=tot_pwr_right.iloc[i]
                    break
            freq_up_ref=df.freq[df.filter_dcap==dcap][df.freq>2442][df.tot_pwr_db==tot_pwr_right_ref].iloc[0]

            freq_down=df.freq[df.filter_dcap==dcap][df.freq<freq_down_ref][df.tot_pwr_db<(float(tot_pwr_left_ref)-0.5)].max(axis=0)
            freq_up=df.freq[df.filter_dcap==dcap][df.freq>freq_up_ref][df.tot_pwr_db<(float(tot_pwr_right_ref)-0.5)].min(axis=0)
            filter_band=freq_up-freq_down
            w_str+='%s'%chip_id+','+'%d'%dcap+','+'%f'%filter_band+'\n'

        f.write(w_str)
        f.closed

    def set_tx_dcc(self, dcap=0):
        if dcap>45:
            dcc = 3
        elif dcap>30:
            dcc = 2
        elif dcap>15:
            dcc = 1
        else:
            dcc = 0
        if self.chipv=="CHIP724":
            self.i2c.bbtop.filter_wftx0_dcc=dcc
            self.i2c.bbtop.filter_bttx0_dcc=dcc
        elif self.chipv=="CHIP723":
            self.i2c.bbtop.filter_wifitx0_dcc=dcc

    def set_tx_dcap(self,dcap=0):
        if self.chipv=="CHIP724":
            self.i2c.bbtop.filter_wftx0_dcap_lq=dcap
            self.i2c.bbtop.filter_wftx0_dcap_hq=dcap
            self.i2c.bbtop.filter_bttx0_dcap_lq=dcap
            self.i2c.bbtop.filter_bttx0_dcap_hq=dcap
        elif self.chipv=="CHIP723":
            self.i2c.bbtop.filter_wifitx0_dcap_lq=dcap
            self.i2c.bbtop.filter_wifitx0_dcap_hq=dcap
        elif self.chipv=="ESP32":
            self.i2c.bbtop.filter_wifitx_dcap_lq=dcap
            self.i2c.bbtop.filter_wifitx_dcap_hq=dcap
            self.i2c.bbtop.filter_bttx_dcap_lq=dcap
            self.i2c.bbtop.filter_bttx_dcap_hq=dcap
        self.set_tx_dcc(dcap)

    def test_filter_band_reg(self,instr=''):
        title = 'dcap,reg,reg_data,freq_step,freq,power\n'
        fname = self.wifi.get_filename('test_filter_band', 'test_filter_band_%s'%instr)
        csvreport1 = csvreport(fname, title)
        logsetlevel('I')
        dcap = 40
        #for dcap in range(30,50,2):
        self.set_tx_dcap(dcap)
        if self.chipv == "CHIP724":
            reg_m = {
                'filter_wftx0_dgdc':1,
                'filter_wftx0_input_ld':3,
                'filter_wftx0_bstb':3,
                'filter_wftx0_dedge':7,
                'filter_wftx0_dcc':3
                }
        elif self.chipv == "CHIP723":
            reg_m = {
                'filter_wifitx0_dgdc':1,
                'filter_wifitx0_input_ld':3,
                'filter_wifitx0_bstb':3,
                'filter_wifitx0_dedge':7,
                'filter_wifitx0_dcc':3
                }

        for reg in reg_m:
            data_max = reg_m[reg]
            data_org = self.wifi.i2c_ric('bbtop', reg)
            for reg_data in range(0,data_max+1):
                self.wifi.i2c_wic('bbtop', reg, reg_data)
                for step in range(-511,512):
                    freq = step/128.0*5
                    power = float(self.wifi.test_txtone_pwr(40,1,1,step))/16.0
                    csvreport1.write_data([dcap, reg,reg_data,step, freq,power])
                    loginfo([dcap,reg,reg_data,step, freq,power])
            self.wifi.i2c_wic('bbtop', reg, data_org)

    def get_tx_power(self, freq_step=0, atten=0):
        self.wifi.txtone_step(0, freq_step, atten)
        power = self.wifiapi.get_power_db()/16.0
        return power

    def get_filter_band(self, bt_mode=0,min_freq_in=0,max_freq_in=0):

        max_power =  float(self.wifi.test_txtone_pwr(40,1,1,0))/16.0 #self.get_tx_power(freq_step=0, atten=40)

        db_ref = 3
        max_freq = 0
        min_step = int(min_freq_in*128/5)
        max_step = int(max_freq_in*128/5)
        print[min_step, max_step, max_power]

        power_ref = max_power-db_ref

        min_freq = 0
        flag  = 0
        scale = -5
        step = min_step
        for i in range(500):
            freq = step/128.0*5
            power =  float(self.wifi.test_txtone_pwr(40,1,1,step))/16.0 #self.get_tx_power(freq_step=step, atten=40)
            loginfo([step,flag,scale,power])

            if min_freq==0 and flag==1 and (power <= power_ref):
                min_freq = freq
                break

            if scale == -5 and (power < power_ref-2):
                scale = 5
            elif scale==5 and (power > power_ref):
                flag = 1
                scale = -1
            step += scale

        max_freq = 0
        flag  = 0
        scale = 5
        step = max_step
        for i in range(500):
            freq = step/128.0*5
            power =  float(self.wifi.test_txtone_pwr(40,1,1,step))/16.0 #self.get_tx_power(freq_step=step, atten=40)
            loginfo([step,flag,scale,power])

            if max_freq==0 and flag==1 and (power <= power_ref):
                max_freq = freq
                break

            if scale ==5 and (power < power_ref-2):
                scale = -5
            elif scale == -5 and (power > power_ref):
                flag = 1
                scale = 1
            step += scale

        band = max_freq-min_freq
        loginfo([band,min_freq,max_freq])
        return [band,min_freq,max_freq]

    def get_freq_power(self, step_ref=512):
        power = []
        freq = []
        for step in range(-step_ref,step_ref):
            power.append(self.get_tx_power(freq_step=step, atten=40))
            freq.append(step/128.0*5)
            loginfo([])
        return [power,freq]

    def test_filter_band_power(self,bt_mode=0,dcap_in=0,dedge=1,instr=''):
        title = 'bt_mode,dcap,dedge,freq,power\n'
        fname = self.wifi.get_filename('test_filter_band', 'test_filter_band_bt%d_dcap%d_dedge%d_%s'%(bt_mode,dcap_in,dedge,instr))
        csvreport1 = csvreport(fname, title)
        logsetlevel('I')

        for bt_mode in range(bt_mode,bt_mode+1):
            if bt_mode==1:
                self.pbus.pbus_debugmode()
                self.pbus.open_tx(0x5e,0x0)
                self.pbus.pbus_wr('bb','en1',0x7e)
                self.rfcal.tos()
            else:
                self.wifi.force_txon(1)
            dcap = dcap_in
            self.i2c.bbtop.filter_wftx0_dedge=dedge
            self.i2c.bbtop.filter_bttx0_dedge=dedge
            self.set_tx_dcap(dcap)
            dcc = self.i2c.bbtop.filter_wftx0_dcc

            if bt_mode==0:
                step_ref = 600
            else:
                step_ref = 64
            for step in range(-step_ref,step_ref):
                power=(self.get_tx_power(freq_step=step, atten=40))
                freq=(step/128.0*5)
                loginfo([step,power])
                csvreport1.write_data([bt_mode,dcap,dedge,freq,power])

            if bt_mode==1:
                self.pbus.pbus_workmode()
            else:
                self.wifi.force_txon(0)

    def test_filter_band(self,instr=''):
        title = 'bt_mode,dcap,band,min_freq,max_freq\n'
        fname = self.wifi.get_filename('test_filter_band', 'test_filter_band_%s'%(instr))
        csvreport1 = csvreport(fname, title)
        logsetlevel('I')
        if self.chipv == "CHIP723":
            mode_num = 1
        elif self.chipv == "CHIP724" or self.chipv == "ESP32" :
            mode_num = 2
        for bt_mode in range(mode_num):
            if bt_mode==1:
                self.pbus.pbus_debugmode()
                self.pbus.open_tx(0x5e,0x0)
                self.pbus.pbus_wr('bb','en1',0x7e)
                self.rfcal.tos()
            else:
                self.wifi.force_txon(1)

            if bt_mode==0:
                min_freq = -25
                max_freq = 25
            else:
                min_freq = -5
                max_freq = 5
            power_m = []
            for dcap in range(5,60,1):
                if self.chipv == "CHIP724":
                    self.i2c.bbtop.filter_wftx0_dedge=1
                elif self.chipv == "CHIP723":
                    self.i2c.bbtop.filter_wftx0_dedge=3
                self.set_tx_dcap(dcap)
                [band,min_freq,max_freq] = self.get_filter_band(bt_mode,min_freq,max_freq)
                csvreport1.write_data([bt_mode,dcap,band,min_freq,max_freq])
                loginfo([bt_mode,dcap,band,min_freq,max_freq])
##                [power, freq] = self.get_freq_power()
##                    loginfo([dcap,step,freq,power])
##                    csvreport1.write_data([dcap,step, freq,power])

            if bt_mode==1:
                self.pbus.pbus_workmode()
            else:
                self.wifi.force_txon(0)

    def rc_to_dcap(self, bt_mode=0,rc_dout=0,band=0):
        if self.chipv=='CHIP723':
            dcap = (10.3*(rc_dout+56)/band)-8.06
        elif self.chipv=='CHIP724':
            if bt_mode==0:
                dcap = (8.2*(rc_dout+56)/band)-8.06
            else:
                dcap = (8.2*(rc_dout+56)/(10.4*band))-8.06
        return dcap

    def filter_rx_loop(self, bt_mode=0,bb_atten=0,instr=''):
        logsetlevel("I")
        title = 'bt_mode,step,rx_power,avgi,avgq\n'
        fname = self.wifi.get_filename('filter_rx_loop', 'filter_rx_loop_%s'%instr)
        csvreport1 = csvreport(fname, title)
        if bt_mode==0:
            step_ref = 600
            self.wifi.set_loopback_mode(pa_gain=0xf,bbgain=0x20,loop_case=0,bt_mode=bt_mode,bb_atten=0)
        else:
            step_ref = 128
            self.i2c.bbtop.encmplx_btrx=1
            self.wifi.set_loopback_mode(pa_gain=0xc,bbgain=0,loop_case=0,bt_mode=bt_mode,bb_atten=3)

        for ctrl in range(0,4):
            self.i2c.bbtop.filter_cmplx_ctrl = ctrl
            length = 4096
            step_m = []
            power_m = []
            for step in range(-step_ref,step_ref,2):
                self.wifi.txtone_step(1,step,8)
                result=self.iq_est.get_iqest_power(length)
                tot_pwr_db=10*np.log10(result[0])
                step_m.append(step)
                power_m.append(tot_pwr_db)
                loginfo([ctrl,step,tot_pwr_db])
            if ctrl==0:
                csvreport1.write_data([ctrl,step_m])
            csvreport1.write_data([ctrl,power_m])

        self.wifi.txtone_step(0,step,16)


    def filter_rx_cap_loop(self, bt_mode=0,bb_atten=0,instr=''):
        logsetlevel("I")
        title = 'bt_mode,step,rx_power,avgi,avgq\n'
        fname = self.wifi.get_filename('filter_rx_loop', 'filter_rx_loop_%s'%instr)
        csvreport1 = csvreport(fname, title)

        if bt_mode==0:
            step_ref = 600
            self.wifi.set_loopback_mode(pa_gain=0xf,bbgain=0x20,loop_case=0,bt_mode=bt_mode,bb_atten=0)
        else:
            step_ref = 128
            self.i2c.bbtop.encmplx_btrx=1
            self.wifi.set_loopback_mode(pa_gain=0xc,bbgain=0,loop_case=0,bt_mode=bt_mode,bb_atten=0)
        for dcap in range(10,150,10):
        #for dcap in range(5,40,2):
            if self.chipv == "CHIP724":
                self.i2c.bbtop.filter_btrx0_dcap_lq = dcap
                self.i2c.bbtop.filter_btrx0_dcap_hq = dcap
            elif self.chipv == "ESP32":
                self.i2c.bbtop.filter_btrx_dcap_lq = dcap
                self.i2c.bbtop.filter_btrx_dcap_hq = dcap
            length = 4096
            step_m = []
            power_m = []
            for step in range(-2*step_ref+step_ref/2,step_ref/2,2):
                self.wifi.txtone_step(1,step,8)
                result=self.iq_est.get_iqest_power(length)
                tot_pwr_db=10*np.log10(result[0])
                step_m.append(float(step/128*5))
                power_m.append(tot_pwr_db)
                loginfo([dcap,step,tot_pwr_db])
            if dcap==0:
                csvreport1.write_data([step,step_m])
            csvreport1.write_data([dcap,power_m])

        self.wifi.txtone_step(0,step,16)






