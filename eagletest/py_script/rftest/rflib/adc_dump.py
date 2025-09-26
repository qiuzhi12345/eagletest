import baselib.plot.myplot as myplot
from baselib.loglib.log_lib import *
from hal.Init import HALS
from hal.common import *
from hal.wifi_api import WIFIAPI
from rftest.rflib.wifi_lib import WIFILIB
from rftest.rflib.rfpll import rfpll
from rftest.rflib.csv_report import csvreport
import random
import time
import numpy as np
import re
import subprocess
import rfglobal
import csv
import pylab
import matplotlib.pyplot as plt
from testcase.performanceCase.BB.bbadc import bbadc

rate_bps_dict = rfglobal.rate_bps_dict
power_dict = rfglobal.power_dict

class DUMP(object):

    def __init__(self,comport,chipv='ESP32'):
        self.comport = comport
        self.chipv = chipv
        self.mem = MEM(self.comport,self.chipv)
        self.mem_ts = MEM_TS(self.comport,self.chipv)
        self.pbus = PBUS(self.comport,self.chipv)
        self.chipid = CHIP_ID(self.comport, self.chipv)
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.wifiapi = WIFIAPI(self.comport,self.chipv)
        self.rfpll = rfpll(self.comport,self.chipv)
        self.bbadc = bbadc(self.comport, self.chipv)

    def sampledeal(self,sample,adc_version="8bit"):

        if adc_version=="10bit" :
          dc_offset=0;
          sample=(sample-dc_offset)&0x3ff;
          if sample>=512:
             sample=sample-1024;
        else :
          dc_offset=128;
          sample=(sample-dc_offset)&0xff;
          if sample>=127:
             sample=sample-256;

        return sample;

    def get_dump_data(self,dump_13bit, adc_data):
        if dump_13bit==1:
            sample_q = adc_data&0x1fff
            sample_i = (adc_data>>13)&0x1fff
    ##        if sample_q>=2**12:
    ##            sample_q=sample_q-2**13;
    ##        if sample_i>=2**12:
    ##            sample_q=sample_i-2**13;
            vga_sat=(adc_data>>26)&0x1;
            lna_sat=(adc_data>>27)&0x1;
        else:
            sample_q=self.sampledeal((adc_data&0x3ff),"10bit");
            sample_i=self.sampledeal(((adc_data>>10)&0x3ff),"10bit");
            vga_sat=(adc_data>>20)&0x1;
            lna_sat=(adc_data>>21)&0x1;
        rx_gain=(adc_data>>20)&0x7f;
        rx_err=(adc_data>>27)&0x1;
        agc_st=(adc_data>>28)&0xf;
        return [sample_q, sample_i, vga_sat, lna_sat, rx_gain, rx_err, agc_st]


    def get_dump_accm(self, accum_i, accum_q, rssi, mem_addr, burst_len):

        result=self.mem.accumiq(mem_addr,burst_len);
        resultlst=str.split(result);
        accum_i=accum_i+int(resultlst[0]);
        accum_q=accum_q+int(resultlst[1]);
        rssi=rssi+int(resultlst[2]);
        return [accum_i, accum_q, rssi]


    def write_dump_data(self, accum_i, accum_q, accum_lna_sat, accum_vga_sat, rssi, mem_addr, burst_len, csvwrite, dump_13bit=0):

        result=self.mem.rdmem(mem_addr,burst_len);
        #get each word and write into one line of file
        for i in range(0,burst_len>>2):
            try_flag=1;
            try_data=result[i];
            while try_flag==1:
                try:
                    adc_data=int(try_data,16);
                    try_flag=0;
                except:
                    loginfo( "mem_addr,burst_len: 0x%x 4"%(mem_addr));
                    try_data=self.mem.rdmem(mem_addr+i*4,4);
                [sample_q, sample_i, vga_sat, lna_sat, rx_gain, rx_err, agc_st] = self.get_dump_data(dump_13bit, adc_data)

                csvwrite.write_data([adc_data,sample_i,sample_q,rx_gain,rx_err,agc_st,hex(adc_data),lna_sat,vga_sat, adc_data>>24])

                accum_i=accum_i+sample_i;
                accum_q=accum_q+sample_q;
                rssi=rssi+(sample_i**2+sample_q**2);

                accum_lna_sat=accum_lna_sat+lna_sat;
                accum_vga_sat=accum_vga_sat+vga_sat;

        return [accum_i, accum_q, rssi, accum_lna_sat, accum_vga_sat]


    def adcdump(self,logdir,start_addr,byte_len,burst_len,buff_start,buff_size,trig_pos,adc_version="10bit",chan_no=1, dump_13bit=0):

        filename='NULL';
        if logdir!="null":
            title = '#sample iq, sample i, sample q, rx_gain, rx_err, agc_st, adc_data, lna_sat, vga_sat\n'
            fname = self.wifi.get_filename(logdir, 'dump')
            csvreport1 = csvreport(fname, title)
            filename = csvreport1.filename

        #decide if buff need wrap
        buff_end=buff_start+buff_size;
        if buff_end <start_addr+byte_len:
           mem_end_addr=buff_end;
           remain_len=byte_len-(buff_end-start_addr);
        else:
           mem_end_addr=start_addr+byte_len;
           remain_len=0;

##        loginfo( "start_addr,byte_len,mem_end_addr,remain_len,burst_len: 0x%x 0x%x 0x%x 0x%x 0x%x"%(start_addr,byte_len,mem_end_addr,remain_len,burst_len));

        #get average data
        accum_i=0;
        accum_q=0;
        accum_lna_sat=0;
        accum_vga_sat=0;
        rssi=0;
        if start_addr+burst_len>=mem_end_addr:
           mem_addr=start_addr;
        else:
            for mem_addr in range(start_addr,mem_end_addr-burst_len,burst_len):
##                loginfo( "burst_len=0x%x mem_end_addr=0x%x mem_addr=0x%x\n"%(burst_len,mem_end_addr,mem_addr))
                if logdir!="null":
                    #get burst length bytes out from memory
##                    loginfo( "stp1:mem_addr,burst_len: 0x%x 0x%x"%(mem_addr,burst_len));
                    [accum_i, accum_q, rssi, accum_lna_sat, accum_vga_sat,] = self.write_dump_data(accum_i, accum_q, accum_lna_sat, accum_vga_sat, rssi, mem_addr, burst_len, csvreport1, dump_13bit)
                else:
                    [accum_i, accum_q, rssi] = self.get_dump_accm(accum_i, accum_q, rssi, mem_addr, burst_len)
                mem_addr=mem_addr+burst_len

        #deal with tail
        #get burst length bytes out from memory
        burst_len=mem_end_addr-mem_addr;
##        loginfo( "burst_len=0x%x mem_end_addr=0x%x mem_addr=0x%x\n"%(burst_len,mem_end_addr,mem_addr))
        if logdir!="null":
##           loginfo( "stp1_tail:mem_addr,burst_len: 0x%x 0x%x"%(mem_addr,burst_len));
           [accum_i, accum_q, rssi, accum_lna_sat, accum_vga_sat] = self.write_dump_data(accum_i, accum_q, accum_lna_sat, accum_vga_sat, rssi, mem_addr, burst_len, csvreport1, dump_13bit)
        else:
           [accum_i, accum_q, rssi] = self.get_dump_accm(accum_i, accum_q, rssi, mem_addr, burst_len)


        #deal with wrap parts
        if remain_len>0:
           mem_end_addr=buff_start+remain_len;

           if buff_start+burst_len>=mem_end_addr:
              mem_addr=buff_start;
           else:
              for mem_addr in range(buff_start,mem_end_addr-burst_len,burst_len):
                    if  logdir!="null":
                      #get burst length bytes out from memory
##                        loginfo( "stp2:mem_addr,burst_len: 0x%x 0x%x"%(mem_addr,burst_len));
                        [accum_i, accum_q, rssi, accum_lna_sat, accum_vga_sat] = self.write_dump_data(accum_i, accum_q, accum_lna_sat, accum_vga_sat, rssi, mem_addr, burst_len, csvreport1, dump_13bit)
                    else:
                        [accum_i, accum_q, rssi] = self.get_dump_accm(accum_i, accum_q, rssi, mem_addr, burst_len)
                    mem_addr=mem_addr+burst_len


           #deal with tail
           #get burst length bytes out from memory
           burst_len=mem_end_addr-mem_addr;
           if  logdir!="null":
##               loginfo( "stp2_tail:mem_addr,burst_len: 0x%x 0x%x"%(mem_addr,burst_len));
               [accum_i, accum_q, rssi, accum_lna_sat, accum_vga_sat] = self.write_dump_data(accum_i, accum_q, accum_lna_sat, accum_vga_sat, rssi, mem_addr, burst_len, csvreport1, dump_13bit)

           else:
                [accum_i, accum_q, rssi] = self.get_dump_accm(accum_i, accum_q, rssi, mem_addr, burst_len)


        #display average i,q
        avg_i=1.0*accum_i/(byte_len>>2);
        avg_q=1.0*accum_q/(byte_len>>2);
        rssi_ac=1.0*rssi/(byte_len>>2)-(avg_i**2+avg_q**2);
        rssi_db=10*np.log10(1.0*rssi/(byte_len>>2));
        rssiac_db=10*np.log10(rssi_ac);
        loginfo('average I:%3.1f'%avg_i);
        loginfo('average Q:%3.1f'%avg_q);
        loginfo('rssi:%3.1f'%rssi_db);
        loginfo('rssi_ac:%3.1f'%rssiac_db);
        loginfo('sat: lna/vga = %d %d'%(accum_lna_sat,accum_vga_sat));

        sig_str = 'avg_i=%2.2f avg_q=%2.2f rssi_db=%2.2f rssiac_db=%2.2f'%(avg_i,avg_q,rssi_db,rssiac_db)
        if logdir!="null":
            csvreport1.write_data([sig_str])
        #combine i,q data
##        print "avg_i,avg_q,rssi_db,rssiac_db,filename,lna_sat,vga_sat: "
        return [avg_i,avg_q,rssi_db,rssiac_db,filename,accum_lna_sat,accum_vga_sat];


    def set_dump_mode(self, reg_dump_mod=0):
        if self.chipv != "ESP8266":
            if reg_dump_mod==1:   # dump 13 bits
                self.mem.wrm(0x6001c0b8, 2, 0, 0)  #dump data sel fe_dump_data
                self.mem.wrm(0x60005114, 9, 9, 0)  #reg_rx_way3_en=0
                self.mem.wrm(0x600050d0, 29, 29, 0) #reg_adc_dump_sel=0, dump ADC_OUT[12:0]
##                self.mem.wrm(0x60006090, 1, 0, 1)  #reg_dump_mod=1, 13bits
            else:  #default value
##                self.mem.wrm(0x6001c0b8, 2, 0, 1)  #bb dump
##                self.mem.wrm(0x60005114, 9, 9, 1)  #reg_rx_way3_en=1
##                self.mem.wrm(0x600050d0, 29, 29, 0) #reg_adc_dump_sel=0, dump ADC_OUT[12:0]
##                self.mem.wrm(0x60006090, 1, 0, 0)  #reg_dump_mod=0, 10bits

                self.mem.wrm(0x6001c0b8, 2, 0, 0)
            self.mem.wrm(0x60006090, 1, 0, reg_dump_mod)


    def adcdumptest(self,logdir='dump',dump_num=1024,trig_mode='sw',adc_version="10bit",sample_80m=1,plot_en=0,chan_en=0,chan=14,sub_chan_cfg=2,force_gain_en=0,force_gain=70,force_gain0=70,gain0_wait=0,rxgain_offset=40,trigcase=0,dump_trig=0,subplot_en=0,subplot_row=3,subplot_col=3,index=0,plot_save=0, reg_dump_mode=0):
        '''
        dump_trig: 1 is dump first, then trig, 0 is trig first, then dump.
        reg_dump_mode: 0-> normal mode, 1-> 13bits, 2-> loop mode1, tx_inf_i[19:10], 3-> loop mode2, tx_inf_q[19:10]
        '''
        self.set_dump_mode(reg_dump_mode)
        if reg_dump_mode==1:
            dump_13bit = 1
        else:
            dump_13bit = 0

        loglevel_old=loggetlevel();
        if loglevel_old =='DEBUG':
           logsetlevel('ERROR');
           #logsetlevel('DEBUG');

        if chan_en==1:
           if chan<15:
              self.wifi.rfchsel(chan,sub_chan_cfg);
           else:
              self.rfpll.set_freq(chan);

##        self.mem.wrm(0x6001c02c, 31, 23, ((force_gain<<1) | force_gain_en));  #set gain
        if self.chipv=="ESP8266":
##            self.mem.wr(0x60009a34,((self.mem.rd(0x60009a34)&0xfffffc00) | (force_gain<<2) | (force_gain_en<<0)));  #set gain
            self.mem.wrm(0x60000590,4,4,1)

        rfrx1=self.pbus.pbus_rd('rfrx1','en1')

        if self.chipv=="ESP8266":
            bb2=self.pbus.pbus_rd('txbb1','en1')
        else:
		    bb2=self.pbus.pbus_rd('bb','en2')

        sw=(rfrx1>>5)&0x3
        lna=(rfrx1>>4)&1
        vga=(((rfrx1>>3)&0x1)<<1) + ((rfrx1>>1)&0x1);
##        loginfo( '"sw,lna,vga,bb2: ",0x%x,0x%x,0x%x,0x%x'%(sw,lna,vga,bb2));

        if force_gain_en==1:
           rxgain_abs=force_gain+rxgain_offset;
        else:
           rxgain_abs=0;

        result=self.wifiapi.adctrig(dump_num-1,trig_mode,sample_80m,trigcase,dump_trig,force_gain_en,force_gain,force_gain0,gain0_wait);
        time.sleep(0.2)
##        print result

        if result==[]:
           return False;

        #get data out, wrap decide valid data
        curr_ptr=result[0];
        #iram1 left parts from base 64k
        buff_start=result[2];
        #size is 128K
        buff_size=result[3];
        #burst length
        burst_len=0x1000;
        #wrap flag
        wrap_flag=result[1];
##        loginfo( 'curr_ptr:0x%x 0x%x 0x%x 0x%x'%(curr_ptr,wrap_flag,buff_start,buff_size));
        #trigger pos
        if wrap_flag==1:
           trig_pos=buff_size/4 -dump_num;
        else:
           trig_pos=curr_ptr-(dump_num-1);

        #if wrap occur!
        if curr_ptr>=dump_num:
           start_addr=buff_start+4*(curr_ptr-dump_num);
        else:
           start_addr=buff_start+buff_size-4*(dump_num-curr_ptr);

        byte_len=4*dump_num;
##        loginfo( "start_addr,byte_len,burst_len,buff_start,buff_size: 0x%x 0x%x 0x%x 0x%x 0x%x"%(start_addr,byte_len,burst_len,buff_start,buff_size));
        dc_offset=self.adcdump(logdir,start_addr,byte_len,burst_len,buff_start,buff_size,trig_pos,adc_version,chan, dump_13bit);
        #mem.wrm(0x6001c02c, 31, 23, ((force_gain<<1) | 0),chan_id);  #set gain
##        loginfo("total sample number:%d"%(byte_len/4));

        logsetlevel(loglevel_old);

        filename = dc_offset[4];
        loginfo(filename)

        if filename!="NULL":

           r_data=myplot.get_csv_vect(filename,3,1);
           i_data=myplot.get_csv_vect(filename,3,2);
           data_ll=len(r_data);
           ll=2**int(np.log2(data_ll));
           real_data=r_data[0:ll];
           image_data=i_data[0:ll];

           if plot_en==1:
               if sample_80m==1:
                  sample_freq_mhz=80;
               else:
                  sample_freq_mhz=40;

               if chan_en==1:
                  if chan<15:
                    center_freq_mhz=self.wifi.chan2freq(chan)
                  else:
                    center_freq_mhz=chan;
               else:
                  center_freq_mhz=0;

               # pylab.ion()
               fftdata=myplot.fft_calc(real_data,image_data);
##               myplot.fft_plot(fftdata,sample_freq_mhz,center_freq_mhz,rxgain_abs,subplot_en,subplot_row,subplot_col,index,plot_save,logdir,filename);
               myplot.fft_plot(fftdata,sample_freq_mhz,center_freq_mhz,rxgain_abs,subplot_en,subplot_row,subplot_col,index,plot_save,logdir);

               myplot.iqwave(filename,fig_type='iq', plot_save=plot_save)

##           adc = np.array(real_data) + np.array(image_data)
##           res = self.bbadc.spectrum(adc,80e6,prominence=12,enReturn=1,enPlot=0)
##           pwr = self.bbadc.power_cal(res)
##           print ''
##           print 'sfdr',pwr['sfdr']
##           print 'snr',pwr['snr']
##           print 'noise',pwr['noise_pwr']
##           print 'total',pwr['total_pwr']
##           print 'signal',pwr['tone_pwr'][0]
##
##           dc_offset.append(pwr['snr'])

        return dc_offset;

    def get_txtone_amp(self):
        result = self.adcdumptest(reg_dump_mode=2)
        ifile = result[4]
        result = self.adcdumptest(reg_dump_mode=3)
        qfile = result[4]
        sig_amp = myplot.get_txtone_amp(ifile, qfile)
        return sig_amp


    def get_ts_txt_data(self,file_name='E:/chip/eagletest/py_script/rftest/rfdata/SaveWindows2020_7_15_17-27-26.TXT'):
        title = 'adc_data,i_data,q_data\n'
        fname = self.wifi.get_filename('adc/','adc_dump_ts')
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
        fname = self.wifi.get_filename('adc/','adc_dump_ts')
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

    def get_ts_txt_aomen_data(self,file_name='E:/chip/eagletest/py_script/rftest/rfdata/SaveWindows2020_7_15_17-27-26.TXT'):
        title = 'adc_data,i_data,q_data\n'
        fname = self.wifi.get_filename('adc/','adc_dump_ts')
        fw1=csvreport(fname,title)
        i_data_list=[]
        q_data_list=[]

        with open(file_name, 'r') as f:
            # f_csv=csv.reader(f)
            # header=next(f_csv)
            while True:
                lines = f.readline()
                print lines
                if not lines:
                    break
                sample_data=[]
                lines=lines.split(',')[0:31]
                for i in range(len(lines)):
                    _data = '0x%s'%(eval(lines[i]))
                    sample_data.append(_data)
                print sample_data
                for i in range(0, len(sample_data)):
                    i_data = eval(sample_data[i]) >> 20
                    # if i_data >= 2048:
                    #     i_data = i_data-4096
                    q_data = (eval(sample_data[i]) >> 4) & 0xfff
                    # if q_data >= 2048:
                    #     q_data = q_data-4096
                    i_data_list.append(i_data)
                    q_data_list.append(q_data)
                    fw1.write_data([hex(eval(sample_data[i])),i_data,q_data])
        plt.ion()

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

    def ts_adc_dump(self, cmd='dump',label_name='line'):
        title = 'adc_data,i_data,q_data\n'
        fname = self.wifi.get_filename('ts_adc_dump/','adc_dump_ts')
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
        pylab.plot(i_data_list, label=label_name)
        pylab.title("adc_i_data")
        # pylab.ylim(0,1024)
        pylab.grid()
        pylab.legend()

        pylab.subplot(212)
        pylab.plot(q_data_list, label=label_name)
        pylab.title("adc_q_data")
        # pylab.ylim(0, 1024)
        pylab.grid()
        pylab.legend()

        fftdata=myplot.fft_calc(i_data_list,q_data_list)
        myplot.fft_plot(fftdata,24,0)

    def ts_adc_dump_new(self, buf_size=3, ):
        title = 'adc_data,i_data,q_data\n'
        fname = self.wifi.get_filename('ts_adc_dump/','adc_dump_ts')
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
                    i_data = eval(sample_data[i]) >> 20
                    # if i_data >= 2048:
                    #     i_data = i_data - 4096
                    q_data = (eval(sample_data[i]) >> 4) & 0xfff
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

        fftdata=myplot.fft_calc(i_data_list,q_data_list)
        myplot.fft_plot(fftdata,13,0)

    def ts_adc_dump_manu(self, buf_size=3,sign_en=1):
        title = 'adc_data,i_data,q_data\n'
        fname = self.wifi.get_filename('ts_adc_dump/','adc_dump_ts')
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