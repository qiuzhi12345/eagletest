import baselib.plot.myplot as myplot
from baselib.loglib.log_lib import *
from hal.common import *
from rftest.rflib.csv_report import csvreport
import random
import time
import numpy as np
import re
import subprocess
import csv
import pylab
import matplotlib.pyplot as plt
from rftest.testcase.bt_api import bt_api
from rftest.rflib import rfglobal

class DUMP(object):

    def __init__(self,comport,chipv='tx232'):
        self.comport = comport
        self.chipv = chipv
        self.mem = MEM(self.comport,self.chipv)
        self.mem_ts = MEM_TS(self.comport)


    def get_ts_txt_data(self,file_name='E:/chip/eagletest/py_script/rftest/rfdata/SaveWindows2020_7_15_17-27-26.TXT'):
        title = 'adc_data,i_data,q_data\n'
        fname = rfglobal.get_filename('adc/','adc_dump_ts')
        fw1=csvreport(fname,title)
        i_data_list=[]
        q_data_list=[]
        with open(file_name, 'r') as f:
            # f_csv=csv.reader(f)
            # header=next(f_csv)
            while True:
                lines = f.readline()
                if not lines:
                    break
                sample_data = lines.split(':')[1].split(', ')[0:31]
                for i in range(0, len(sample_data)):
                    i_data = eval(sample_data[i]) >> 20
                    if i_data >= 2048:
                        i_data = i_data-4096
                    q_data = (eval(sample_data[i]) >> 4) & 0xfff
                    if q_data >= 2048:
                        q_data = q_data-4096
                    i_data_list.append(i_data)
                    q_data_list.append(q_data)
                    fw1.write_data([hex(eval(sample_data[i])),i_data,q_data])
        fftdata=myplot.fft_calc(i_data_list,q_data_list)
        myplot.fft_plot(fftdata,13,2402)

    def get_ts_txt_data_wnf9062(self,file_name='E:/chip/eagletest/py_script/rftest/rfdata/SaveWindows2020_7_15_17-27-26.TXT'):
        title = 'adc_data,i_data,q_data\n'
        fname = rfglobal.get_filename('adc/','adc_dump_ts')
        fw1=csvreport(fname,title)
        i_data_list=[]
        q_data_list=[]
        data_list = []
        with open(file_name, 'r') as f:
            # f_csv=csv.reader(f)
            # header=next(f_csv)
            while True:
                lines = f.readline()
                if not lines:
                    break
                if lines.find('seek=')!=-1:
                    lines = lines.strip()
                    lines = lines.strip(',')
                    data = lines.split(':')
                    data = data[1].split(',')

                    data_list = data_list + data
        for sample_data in data_list:
            # sample_data = lines
            i_data = (eval(sample_data)) >> 22
            q_data = (eval(sample_data) >> 6) & 0x3ff

            i_data_list.append(i_data)
            q_data_list.append(q_data)
            fw1.write_data([hex(eval(sample_data)),i_data,q_data])

        pylab.ion()
        pylab.subplot(211)
        pylab.plot(i_data_list, label='line')
        pylab.title("adc_i_data")
        pylab.grid()
        pylab.legend()

        pylab.subplot(212)
        pylab.plot(q_data_list, label='line')
        pylab.title("adc_q_data")
        pylab.grid()
        pylab.legend()

        fftdata=myplot.fft_calc(i_data_list,q_data_list)
        myplot.fft_plot(fftdata,12,2402)

    def get_ts_csv_data(self,file_name='E:/chip/eagletest/py_script/rftest/rfdata/SaveWindows2020_7_15_17-27-26.csv'):
        i_data_list=[]
        q_data_list=[]
        with open(file_name, 'r') as f:
            f_csv=csv.reader(f)
            header=next(f_csv)
            for lines in f_csv:
                # print lines
                i_data = eval(lines[1])
                q_data = eval(lines[2])
                i_data_list.append(i_data)
                q_data_list.append(q_data)
        pylab.ion()
        fftdata=myplot.fft_calc(i_data_list,q_data_list)
        myplot.fft_plot(fftdata,13,2402)

    def get_ts_csv_data_debug(self,file_name='E:/chip/eagletest/py_script/rftest/rfdata/SaveWindows2020_7_15_17-27-26.csv'):
        i_data_list=[]
        q_data_list=[]
        with open(file_name, 'r') as f:
            f_csv=csv.reader(f)
            header=next(f_csv)
            for lines in f_csv:
                # print lines
                i_data = (eval(lines[0]) >> 16) & 0xfff
                q_data = eval(lines[2]) & 0xfff
                # if i_data >= 2048:
                #     i_data = i_data - 4096
                # if q_data >= 2048:
                #     q_data = q_data - 4096
                i_data_list.append(i_data)
                q_data_list.append(q_data)
        pylab.ion()
        pylab.subplot(211)
        pylab.plot(i_data_list, label='line')
        pylab.title("adc_i_data")
        pylab.grid()
        pylab.legend()

        pylab.subplot(212)
        pylab.plot(q_data_list, label='line')
        pylab.title("adc_q_data")
        pylab.grid()
        pylab.legend()

        fftdata=myplot.fft_calc(i_data_list,q_data_list)
        myplot.fft_plot(fftdata,13,0)

    def ts_adc_dump_config(self,data_sel=1,dbm_data_sel=0x10,agc_en=0,rxgain_index=0x7,rxon_man=1):
        '''
        data_sel:   1: sel sar adc data;    0:  sel modem dbm_modem_data
        dbm_data_sel:
        5'h0::  gfilter_tx_dout
        5'h1::  symbol2iq_tx_dout_q: symbol2iq_tx_dout_i
        5'h2::  cordic_tx_amp_dout: cordic_tx_angle_dout
        5'h3::  ampm_tx_dout_am: ampm_tx_dout_pm
        5'h4::  diff_tx_dout
        5'h5::  freq_blend_tx_dout
        5'h6::  intigrate_tx_dout
        5'h7::  cordic_iq_tx_dout_q: cordic_iq_tx_dout_i
        5'h8::  dout_tx_13m_q: dout_tx_13m_i
        5'h9::  iqim_cancel_dout_q: iqim_cancel_dout_i
        5'ha::  dout_tx_26m_q: dout_tx_26m_i
        5'hb::  dout_tx_52m_q: dout_tx_52m_i
        5'hc:: dac_grp_bit_q_outp: dac_grp_bit_i_outp
        5'h10:: adc_data_q: adc_data_i
        5'h11:: adc_din_q: adc_din_i
        5'h12:: lpf_q: lpf_i
        5'h13:: rateconv_q: rateconv_i
        5'h14:: calib_q: calib_i
        5'h15:: dc_calib_q: dc_calib_i
        5'h16:: cancel_flt_i: cancel_flt_q
        5'h17:: notch_q: notch_i
        5'h18:: gain_q: gain_i
        5'h19:: ble_mux_q: ble_mux_i
        5'h1a:: mixer_q: mixer_i
        5'h1b:: srrc_q: srrc_i
        5'h1c:: rssi_out
        5'h1d:: angle_rc: angle
        5'h1e:: angle_offset1: angle_offset
        5'h1f:: err_dpsk: err_gfsk
        '''
        self.mem_ts.wrm(0xa04210a0,0,0,agc_en)
        self.mem_ts.wrm(0xa04210a0,20,17,rxgain_index)
        self.mem_ts.wrm(0xa0423000,1,1,data_sel)
        self.mem_ts.wrm(0xa04200e0,4,0,dbm_data_sel)
        if rxon_man != 0:
            self.mem_ts.wrm(0xa0422014,3,0,0x3)
        else:
            self.mem_ts.wrm(0xa0422014, 3, 0, 0x0)

    def ts_adc_dump(self, cmd='dump'):
        title = 'adc_data,i_data,q_data\n'
        fname = rfglobal.get_filename('ts_adc_dump/','adc_dump_ts')
        fw1=csvreport(fname,title)
        i_data_list=[]
        q_data_list=[]
        # self.comport.req_com('rfrx 1', wr_end='\r\n')

        res = self.comport.req_com(cmd, endstr='TS', wr_end='\r\n')
        for i in range(len(res)):
            if res[i].find('seek=') != -1:
                sample_data = res[i].split(':')[1].split(', ')[0:31]
                # logdebug(sample_data)
                for i in range(0, len(sample_data)):
                    i_data = eval(sample_data[i]) >> 22
                    # if i_data >= 2048:
                    #     i_data = i_data - 4096
                    q_data = (eval(sample_data[i]) >> 6) & 0x3ff
                    # if q_data >= 2048:
                    #     q_data = q_data - 4096
                    i_data_list.append(i_data)
                    q_data_list.append(q_data)
                    fw1.write_data([hex(eval(sample_data[i])),i_data,q_data])
        pylab.ion()
        pylab.subplot(211)
        pylab.plot(i_data_list, label='line')
        pylab.title("adc_i_data")
        pylab.grid()
        pylab.legend()

        pylab.subplot(212)
        pylab.plot(q_data_list, label='line')
        pylab.title("adc_q_data")
        pylab.grid()
        pylab.legend()

        # fftdata=myplot.fft_calc(i_data_list,q_data_list)
        # myplot.fft_plot(fftdata,13,0)


    def ts_adc_dump_manu(self, buf_size=3,sign_en=1):
        title = 'adc_data,i_data,q_data\n'
        fname = rfglobal.get_filename('ts_adc_dump/','adc_dump_ts')
        fw1=csvreport(fname,title)
        i_data_list=[]
        q_data_list=[]
        self.comport.req_com('dmaon buf=%d' % buf_size,  wr_end='\r\n')
        # self.comport.req_com('dmaon', wr_end='\r\n')
        time.sleep(2)
        res = self.comport.req_com('dmaoff', endstr='TS', wr_end='\r\n')
        for i in range(len(res)):
            if res[i].find('seek=') != -1:
                sample_data = res[i].split(':')[1].split(', ')[0:31]
                #logdebug(sample_data)
                for i in range(0, len(sample_data)):
                    i_data = (eval(sample_data[i]) >> 16) & 0xfff
                    q_data = eval(sample_data[i]) & 0xfff

                    if sign_en == 1:
                        if i_data >= 2048:
                            i_data = i_data - 4096
                        if q_data >= 2048:
                            q_data = q_data - 4096
                    i_data_list.append(i_data)
                    q_data_list.append(q_data)
                    fw1.write_data([hex(eval(sample_data[i])),i_data,q_data])
        pylab.ion()
        pylab.subplot(211)
        pylab.plot(i_data_list, label='line')
        pylab.title("adc_i_data")
        pylab.grid()
        pylab.legend()

        pylab.subplot(212)
        pylab.plot(q_data_list, label='line')
        pylab.title("adc_q_data")
        pylab.grid()
        pylab.legend()

        fftdata=myplot.fft_calc(i_data_list,q_data_list)
        myplot.fft_plot(fftdata,13,0)


    # def get_filename(self, folder, file_name, sub_folder=''):
    #     '''
    #     :folder: file store folder
    #     :file_name:  file name
    #     :sub_folder: if not need, it may be default ""
    #     '''
    #     if rfglobal.file_folder=="":
    #         rfdata_path = './rftest/rfdata/'
    #     else:
    #         rfdata_path = './rftest/rfdata/%s/'%rfglobal.file_folder
    #         if os.path.exists(rfdata_path) == False:
    #             os.mkdir(rfdata_path)
    #
    #     data_path1 = rfdata_path+'%s/'%(folder)
    #     if os.path.exists(data_path1) == False:
    #         os.mkdir(data_path1)
    #
    #     filetime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()));
    #     # mac = self.read_mac()
    #     mac = ''
    #
    #     gen_folder = '_%s'%(filetime[0:8])
    #     data_path2 = data_path1 +'%s/'%(gen_folder)
    #     if os.path.exists(data_path2) == False:
    #         os.mkdir(data_path2)
    #
    #     fname = '%s'%(file_name)
    #     outfile_name = data_path2 + fname
    #
    #     if sub_folder != '':
    #         gen_folder = '%s_%s'%(sub_folder,filetime[0:8])
    #         sub_path = data_path2+'%s/'%(gen_folder)
    #         if os.path.exists(sub_path) == False:
    #             os.mkdir(sub_path)
    #
    #         outfile_name = sub_path + file_name
    #
    #     return outfile_name
