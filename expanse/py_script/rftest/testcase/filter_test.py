import time
import re
import csv
import os, sys
from baselib.loglib.log_lib import *
import matplotlib.pyplot as plt
import pylab
import xlrd
import numpy as np
import pandas as pd
from rftest.rflib.utility import mfunc
from baselib.instrument import dm,sme
from baselib.instrument.spa import HP,Agilent
from hal.common import MEM,MEM_TS

from rftest.rflib.csv_report import csvreport
from rftest.rflib.adc_dump import DUMP
from baselib.instrument import *
from rftest.testcase.bt_api import bt_api
from rftest.rflib import rfglobal

class filter_test(object):
    def __init__(self,comport,chipv='ESP32'):

        self.comport = comport
        self.chipv = chipv
        self.mem = MEM(self.comport, self.chipv)
        self.mem_ts = MEM_TS(self.comport)

        self.adc_dump = DUMP(self.comport,self.chipv)
        self.curr_data_path = 'E:/chip/eagletest/py_script/rftest/rfdata/filter_test/'
        if False==os.path.exists(self.curr_data_path):
            os.mkdir(self.curr_data_path )

    def filter_tx_ts(self, cfreq=2440, mixer_gain_list=range(0,8), device_spa='N9020A'):
        title = 'mixer_gain,h_gain_le,freq,txtone_pwr\n'
        fname = self.get_filename('ts_bt_test/', 'filter_tx_ts')
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

    def filter_rx_tx232(self, cfreq=2440, cbpf_if_list=['1M','1.5M'], flt_index_list=['cbpf1','cbpf1&2'], rccal_code_val_list=range(1,31,2), cbpf_bw_code_list=[2],
                        device_spa='N9020A', step_acc=20):
        title = 'rccal_code_val,IF,flt_mode,cbpf_bw_code,step_freq(MHz),measure_freq(KHz),txtone_pwr\n'
        fname = self.get_filename('ts_bt_test/', 'filter_rx_tx232')
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
        fname = self.get_filename('ts_bt_test/', 'filter_rx_tx232')
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
                # for rccal_code_val in rccal_code_val_list:
                for rccal_code_val in [1]:
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
                                step_list = range(-4 * 1000 / step_acc, -2 * 1000 / step_acc, 2) + range(-2 * 1000 / step_acc, 2 * 1000 / step_acc, 1) + range(2 * 1000 /
                                                                                                                                                               step_acc,
                                                                                                                                                               4 * 1000 /
                                                                                                                                                               step_acc, 2)
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
                    print (row[0],row[1])
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
                    print (row[0],row[1])
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

    def get_filename(self, folder, file_name, sub_folder=''):
        '''
        :folder: file store folder
        :file_name:  file name
        :sub_folder: if not need, it may be default ""
        '''
        if rfglobal.file_folder=="":
            rfdata_path = './rftest/rfdata/'
        else:
            rfdata_path = './rftest/rfdata/%s/'%rfglobal.file_folder
            if os.path.exists(rfdata_path) == False:
                os.mkdir(rfdata_path)

        data_path1 = rfdata_path+'%s/'%(folder)
        if os.path.exists(data_path1) == False:
            os.mkdir(data_path1)

        filetime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()));
        # mac = self.read_mac()
        mac = ''

        gen_folder = '_%s'%(filetime[0:8])
        data_path2 = data_path1 +'%s/'%(gen_folder)
        if os.path.exists(data_path2) == False:
            os.mkdir(data_path2)

        fname = '%s'%(file_name)
        outfile_name = data_path2 + fname

        if sub_folder != '':
            gen_folder = '%s_%s'%(sub_folder,filetime[0:8])
            sub_path = data_path2+'%s/'%(gen_folder)
            if os.path.exists(sub_path) == False:
                os.mkdir(sub_path)

            outfile_name = sub_path + file_name

        return outfile_name




