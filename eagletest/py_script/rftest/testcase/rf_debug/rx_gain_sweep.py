import time
import re
import csv
import os, sys
import matplotlib.pyplot as plt
import pylab
import numpy as np
from baselib.instrument import dm,tester,sme
from rftest.rflib.wifi_lib import WIFILIB
from hal.common import MEM
from rftest.rflib.adc_dump import DUMP
import rftest.rflib.rfglobal as rfglobal
import rftest.rflib.wifi_instrum as instrum
from baselib.loglib.log_lib import *
from rftest.rflib.csv_report import csvreport
from rftest.rflib.pbus import pbus
from rftest.rflib.iq_est import IQ_EST
from rftest.rflib.rfpll import rfpll
from rftest.rflib.utility import iofunc
from baselib.instrument.spa import HP,Agilent
from hal.wifi_api import WIFIAPI
from testcase.performanceCase.BB.bbadc import bbadc
from hal.hwregister.hwi2c.all import *
from hal.hwregister.hwpbus.all import *
import baselib.plot.myplot as myplot
import matplotlib.pyplot as plt


class Sweep_RX_Gain(object):

    def __init__(self,comport,chipv='ESP32'):

        self.comport = comport
        self.chipv = chipv
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.wifiapi = WIFIAPI(self.comport,self.chipv)
        self.adc_dump = DUMP(self.comport,self.chipv)
        self.pbus = pbus(self.comport,self.chipv)
        self.mem = MEM(self.comport,self.chipv)
        self.iq_est = IQ_EST(self.comport,self.chipv)
        self.rfpll = rfpll(self.comport,self.chipv)
        self.bbadc = bbadc(self.comport, self.chipv)
        self.i2c = HWI2C(self.comport,self.chipv)
        self.hwpbus = HWPBUS(self.comport,self.chipv)
        self.fine_dci = []
        self.fine_dcq = []
        self.coarse_dci = []
        self.coarse_dcq = []

    def tester_init(self, tx_freq, tx_pwr, iqv_no, cable_att, device):
        print device
        if device=="TESTER":
            tester1=tester.tester(tx_freq,tx_pwr,'tone',100,iqv_no,'cw',cable_att,10, 1,0)
            return tester1
        elif device=="sme":
            tester0=sme.sme()
            return tester0
        else:
            tester2=HP('SRC',cfreq=tx_freq,rb=0,span=0,reflvl=tx_pwr)
            return tester2

    def tester_set_pwr(self, tester, tx_pwr, iqv_no, device):
        if device=="TESTER":
            tester.set_pwr(tx_pwr,0,iqv_no,'cw')  #IQV
        elif device=="sme":
            tester.setpow(tx_pwr)
        else:
            tester.set_pwr(tx_pwr)  #SPA

    def tester_txdis(self, tester, device,en=0):
        if en==0:
            if device=="TESTER":
                tester.txenable(0)  #IQV
            elif device=="sme":
                tester.rfoff()
            else:
                tester.close()  #SPA
        else:
            if device=="TESTER":
                tester.txenable(1)  #IQV
            elif device=="sme":
                tester.rfon()
            else:
                tester.open()  #SPA

    def tester_set_freq(self, tester, device, tx_freq, tx_pwr, iqv_no):
        if device=="TESTER":
##            tester.setvsg(tx_freq,tx_pwr,iqv_no);
            tester.txcw(tx_freq,tx_pwr,iqv_no);
        elif device=="sme":
            tester.setfreq(tx_freq*1e6)
            tester.setpow(tx_pwr)
        else:
            tester.set_param(tx_freq,0,0,0)
            tester.set_pwr(tx_pwr)  #SPA

    def get_tx_power(self, tester, device, tx_freq, tx_pwr, cable_att,iqv_no, dump_len):

        for i in range(0,8):

            self.tester_set_freq(tester, device, tx_freq, tx_pwr, iqv_no)

            out=self.adc_dump.adcdumptest('null',dump_len,'sw',"10bit",sample_80m=1,plot_en=0)
            rx_pwr = out[2]

            print '\ni=%d, tx_pwr=%2.2f,rx_pwr=%2.2f\n'%(i, tx_pwr, rx_pwr)

            if self.chipv=='ESP8266':  # ADC is 9 bits
                if(rx_pwr > 42):
                    tx_pwr -= 6
                elif(rx_pwr < 32):
                    tx_pwr += 6
                else:
                    break
            else:     # ADC is 10 bits
                if(rx_pwr > 50):
                    tx_pwr -= 6
                elif(rx_pwr<40):
                    tx_pwr += 6
                else:
                    break

            if tx_pwr==-70 and rx_pwr>51:
                break

            if tx_pwr < -80:
                tx_pwr = -80

            if tx_pwr+cable_att > 10:
                tx_pwr = 10-cable_att
                break

        return [tx_pwr, out]


    def check_noise_floor_table(self, chan=14):

        fname = self.wifi.get_filename('check_noise_floor', 'check_noise_floor_table_%d'%chan)
        title = 'gain, rfrx1, dci, dc1, rx_pwr, rx_noise, noise_floor, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2\n'
        fw1=csvreport(fname, title)

        self.wifi.rfchsel(chan)

        max_gain = self.mem.rdm(0x6001c02c, 14, 8)


        for  gain in range (0, max_gain):

            self.mem.wrm(0x6001c02c, 31, 23, ((gain<<1) | 0));  #set gain
            self.mem.wrm(0x6001c02c, 31, 23, ((gain<<1) | 1));  #set gain

            out=self.adc_dump.adcdumptest('null',8000,'sw',"10bit",sample_80m=1,plot_en=0)
            noise_floor = 0 #self.wifiapi.check_noise_floor()
            noise_floor = int(noise_floor)/4

            [rfrx1, rftx1, rftx2, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2] = self.pbus.all_pbus()

            fw1.write_data([gain, hex(rfrx1), out[0:4], noise_floor, hex(bb2), hex(bb1), dcoi1, dcoq1, dcoi2, dcoq2])
        self.mem.wrm(0x6001c02c, 31, 23, ((gain<<1) | 0));  #set gain

    def get_test_data(self):
        file_path = './rftest/rfdata/sweep_rfrx_reg/sweep_rfrx_reg_CHIP722_0x18fe3471a6da_20190429/'
        file_name = 'sweep_rfrx_reg_14_rfrx_mx_db_B4_CHIP722_0x18fe3471a6da_20190429_195646.csv'
        rfrx_reg = 'rfrx_mx_db'
        max_data = 4
        fname = file_path+'%s_'%rfrx_reg+file_name
        title = 'rfrx1,rx_gain_min,rx_gain_max, rx_gain_delta,rx_noise_min,rx_noise_max, rx_noise_delta,gain_min_index,gain_max_index\n'
        fw1=csvreport(fname, title)
        rfrx_m = [0x180,0x190,0x1a0,0x1b0,0x1c0,0x1d0,0x1e0,0x1f0]
        rfrx_gain = []
        for gain in rfrx_m:
            for fine in range(0,16,2):
                rfrx = gain+fine
                rfrx_gain.append(rfrx)

        csv_data = iofunc.csv2data(file_path+file_name)

        for i in range(0,len(rfrx_gain)):
            noise_m = []
            gain_m = []
            rfrx1 = rfrx_gain[i]
            for j in range(0,max_data):
                row = csv_data[i*max_data+j+1]
                noise_m.append(float(row[2]))
                gain_m.append(float(row[7]))

            gain_min = min(gain_m)
            gain_min_index = gain_m.index(gain_min)
            gain_max = max(gain_m)
            gain_max_index = gain_m.index(gain_max)
            noise_min = noise_m[gain_min_index]
            noise_max = noise_m[gain_max_index]
            gain_delta = gain_max - gain_min
            noise_delta = noise_max - noise_min
            fw1.write_data([hex(rfrx1), gain_max, gain_min, gain_delta, noise_min, noise_max, noise_delta,gain_min_index,gain_max_index])

    def i2c_rfrx_test(self, chan=14, iqv_no=2, name_str='', device='TESTER'):
        rfrx_i2c_m = ['rfrx_lna_dcap','rfrx_vga_dcap','rfrx_mx_db']
        max_bit = [3,3,1]

        num = 0
        for rfrx_reg in rfrx_i2c_m:
            reg_max = 2**(max_bit[num]+1)
            self.sweep_rfrx_reg(chan, iqv_no, rfrx_reg, reg_max, name_str, device)
            num += 1


    def sweep_rfrx_reg(self, chan=14, iqv_no=2, rfrx_reg='', reg_max=0, name_str='', device='TESTER'):

##        logsetlevel("D")
        fname = self.wifi.get_filename('sweep_rfrx_reg_%s'%name_str, 'sweep_rfrx_reg_%d_%s_%s'%(chan, rfrx_reg, name_str))
        title = 'rfrx1,%s,rx_noise, dci, dc1, rx_pwr, tx_pwr, rx_gain, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2\n'%rfrx_reg
        fw1=csvreport(fname, title)

        if chan<=14:
            self.wifi.rfchsel(chan)
##            self.wifiapi.set_rfrx_dcap()
            tx_freq = self.wifi.chan2freq(chan)+2   #5M Tone
        else:
            self.rfpll.set_freq(chan)
##            self.wifiapi.set_rfrx_dcap()
            tx_freq = chan+2


        tx_pwr = -20
        cable_att = 2
        tester = self.tester_init(tx_freq, tx_pwr, iqv_no, cable_att, device)

##        self.wifi.rx_force_gain(1, 0, 0)

        self.pbus.pbus_debugmode()

##        rfrx_m = [0x180,0x190,0x1a0,0x1b0,0x1c0,0x1d0,0x1e0,0x1f0]
        rfrx_m = [0x180,0x1f0]

        rfrx_reg_org = self.wifi.i2c_ric('rfrx', rfrx_reg)
        print '1 %s=%d'%(rfrx_reg, self.wifi.i2c_ric('rfrx', rfrx_reg))

        for  gain in rfrx_m:
            for fine in [0x4, 0xe]: #range(0,16,4):
                rfrx = gain+fine
                bb2 = 0
                self.pbus.pbus_wr('rfrx1', 'en1', rfrx)

                if self.chipv!='ESP8266':
                    self.pbus.pbus_wr('bb', 'en2', bb2)

                for data in range(0, reg_max):
                    self.wifi.i2c_wic('rfrx', rfrx_reg, data)
                    print '2 %s=%d'%(rfrx_reg, self.wifi.i2c_ric('rfrx', rfrx_reg))

                    if self.chipv!='ESP8266':
                        self.pbus.set_dco(0x100, 0x100, 0x100, 0x100)
                        self.mem.wrm(0x600060a0, 17, 16, 3)
                        self.wifi.rxdc_cal()
                    else:
                        self.pbus.set_dco(254,287,256,256)

                    tester.txenable(1)  #IQV
                    [tx_pwr, out] = self.get_tx_power(tester, device, tx_freq, tx_pwr, cable_att,iqv_no, 8000)
                    rx_pwr = out[2]
                    get_pwr = rx_pwr - tx_pwr

                    out=self.adc_dump.adcdumptest('null',8000,'sw',"10bit",sample_80m=1,plot_en=0)

                    tester.txenable(0)  #IQV
                    noise_out=self.adc_dump.adcdumptest('null',8000,'sw',"10bit",sample_80m=1,plot_en=0)
                    rx_noise = noise_out[3]

                    [rfrx1, rftx1, rftx2, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2] = self.pbus.all_pbus()
                    rfrx_b = []
                    for kk in range(8, 0, -1):
                        rfrx_b.append((rfrx1>>kk)&1)

                    fw1.write_data([hex(rfrx1), data,rx_noise, out[0:3], tx_pwr, get_pwr, hex(bb2), hex(bb1), dcoi1, dcoq1, dcoi2, dcoq2,rfrx_b])

                    if rx_pwr < 25:
                        break
                if rx_pwr < 25:
                        break
            if rx_pwr < 25:
                    break
        self.pbus.pbus_workmode()

        self.wifi.i2c_wic('rfrx', rfrx_reg, rfrx_reg_org)
        print '3 %s=%d'%(rfrx_reg, self.wifi.i2c_ric('rfrx', rfrx_reg))

        self.tester_txdis(tester, device)
##        logsetlevel("D")


    def check_noise_floor_rfrx(self, chan=14,  name_str=''):

        fname = self.wifi.get_filename('check_noise_floor', 'check_noise_floor_rfrx_%s_%d'%(name_str,chan))
        title = 'rfrx1, remain_rxdc_i, remain_rxdc_q, rx_pwr, rx_noise, noise_floor, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2, XPD_RFRX_VGA, XPD_RFRX_LNA, RXSW_HG, RXSW_HG_FINE,LNA_DG,VGA_DG_GM,VGA_DG_BUF,VGA_DG_LOAD\n'
        fw1=csvreport(fname, title)

        if chan>15:
            self.rfpll.set_freq(chan)
        else:
            self.wifi.rfchsel(chan)
            self.wifiapi.set_rfrx_dcap()

        self.pbus.pbus_debugmode()

        rfrx_m = [0x180,0x190,0x1a0,0x1b0,0x1c0,0x1d0,0x1e0,0x1f0]

        for  gain in rfrx_m:
            for index in range(8):
                rfrx = gain+index*2
                bb2 = 0

                self.pbus.pbus_wr('rfrx1', 'en1', rfrx)
                self.pbus.pbus_wr('bb', 'en2', bb2)
                self.pbus.set_dco(0x100, 0x100, 0x100, 0x100)

    ##            if rfrx_en == 0:
                self.mem.wrm(0x600060a0, 17, 16, 3)
                self.wifi.rxdc_cal()

                out=self.adc_dump.adcdumptest('null',8000,'sw',"10bit",sample_80m=1,plot_en=0)
                noise_floor = 0 #self.wifiapi.check_noise_floor()
                noise_floor = int(noise_floor)/4

                [rfrx1, rftx1, rftx2, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2] = self.pbus.all_pbus()

                rfrx_b = []
                for i in range(8, 0, -1):
                    rfrx_b.append((rfrx1>>i)&1)

                fw1.write_data([hex(rfrx1), out[0:4], noise_floor, hex(bb2), hex(bb1), dcoi1, dcoq1, dcoi2, dcoq2, rfrx_b])

##        self.pbus.pbus_workmode()

    def dac_filt_dac_rxdc(self, chan=14, name_str=''):

        fname = self.wifi.get_filename('rxdc_test', 'dac_filt_dac_rxdc_%s_%d'%(name_str, chan))
        title = 'rfrx1, remain_rxdc_i, remain_rxdc_q, rx_pwr, rx_noise, noise_floor, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2, XPD_RFRX_VGA, XPD_RFRX_LNA, RXSW_HG, RXSW_HG_FINE,LNA_DG,VGA_DG_GM,VGA_DG_BUF,VGA_DG_LOAD\n'
        fw1=csvreport(fname, title)

        if chan>15:
            self.rfpll.set_freq(chan)
        else:
            self.wifi.rfchsel(chan)
            self.wifiapi.set_rfrx_dcap()

        bbc_m = [0x0, 0x20, 0x30, 0x38, 0x3c]
        self.pbus.pbus_debugmode()

        for  bbc in bbc_m:
            for bbf in range(0, 6):
                bb2 = (bbf<<6)+bbc
                # dac,flt,adc
                self.hwpbus.RFRX1.EN1 = 0x001
                self.hwpbus.RFTX1.EN1 = 0x000
                self.hwpbus.RFTX2.EN1 = 0x000
                self.hwpbus.BB1.EN1   = 0x100
                self.hwpbus.BB1.EN1   = 0x1c9
                self.hwpbus.BB1.EN2   = bb2
                self.i2c.bbtop.enlb = 0

                self.pbus.set_dco(0x100, 0x100, 0x100, 0x100)

                self.mem.wrm(0x600060a0, 17, 16, 3)
                self.wifi.rxdc_cal()

                out=self.adc_dump.adcdumptest('null',8000,'sw',"10bit",sample_80m=1,plot_en=0)
                noise_floor = 0 #self.wifiapi.check_noise_floor()
                noise_floor = int(noise_floor)/4

                [rfrx1, rftx1, rftx2, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2] = self.pbus.all_pbus()

                rfrx_b = []
                for i in range(8, 0, -1):
                    rfrx_b.append((rfrx1>>i)&1)

                fw1.write_data([hex(rfrx1), out[0:4], noise_floor, hex(bb2), hex(bb1), dcoi1, dcoq1, dcoi2, dcoq2, rfrx_b])

##        self.pbus.pbus_workmode()

    def rxdc_test(self, chan=14, name_str=''):

        fname = self.wifi.get_filename('rxdc_test', 'rxdc_test_%s_%d'%(name_str, chan))
        title = 'xpd_rfrx_vga(rfrx_pbus[8]),xpd_rfrx_lna(rfrx_pbus[7]),xpd_i2c_rfpll, dac_filter_adc loop_en,i2c_rfrx rfrx_mx_db,i2c_ckgen force_pd_tx,test_num,rfrx1,dcoi_coarse, dcoq_coarse, dcoi_fine, dcoq_fine,remain_rxdc_i, remain_rxdc_q,bb1, bb2\n'
        fw1=csvreport(fname, title)

        if chan>15:
            self.rfpll.set_freq(chan)
        else:
            self.wifi.rfchsel(chan)
            self.wifiapi.set_rfrx_dcap()

        bbc_m = [0x0, 0x20, 0x30, 0x38, 0x3c]
        self.pbus.pbus_debugmode()
        self.hwpbus.BB1.EN2   = 0

        for  i in range(0, 6+4):
            if i==0:
                xpd_rfrx_vga = 1
                xpd_rfrx_lna = 1
                xpd_i2c_rfpll = 1
                filt_loop_en = 0
            elif i==1:
                xpd_rfrx_vga = 1
                xpd_rfrx_lna = 1
                xpd_i2c_rfpll = 0
                filt_loop_en = 0
            elif i==2:
                xpd_rfrx_vga = 0
                xpd_rfrx_lna = 1
                xpd_i2c_rfpll = 1
                filt_loop_en = 0
            elif i==3:
                xpd_rfrx_vga = 1
                xpd_rfrx_lna = 0
                xpd_i2c_rfpll = 1
                filt_loop_en = 0
            elif i==4:
                xpd_rfrx_vga = 0
                xpd_rfrx_lna = 1
                xpd_i2c_rfpll = 0
                filt_loop_en = 0
            elif i==5:
                xpd_rfrx_vga = 0
                xpd_rfrx_lna = 0
                xpd_i2c_rfpll = 1
                filt_loop_en = 1
            else:
                xpd_rfrx_vga = 1
                xpd_rfrx_lna = 1
                xpd_i2c_rfpll = 1
                filt_loop_en = 0

            if i<6:
                rfrx_mx_db=2
            else:
                rfrx_mx_db = i-6

            self.i2c.rfrx.rfrx_mx_db = rfrx_mx_db

            if filt_loop_en==1:
                # dac,flt,adc
                self.hwpbus.RFRX1.EN1 = 0x001
                self.hwpbus.BB1.EN1   = 0x1c9
            else:
                self.hwpbus.RFRX1.EN1 = (xpd_rfrx_vga<<8)+(xpd_rfrx_lna<<7)+4
                self.hwpbus.BB1.EN1   = 0x189

            if xpd_i2c_rfpll==0:
                 self.mem.wrm(0x60008034, 31, 31, 0)
            else:
                 self.mem.wrm(0x60008034, 31, 31, 1)

            for force_pd_tx in range(0,2):
                if self.chipv=="CHIP722":
                    self.i2c.ckgen.force_pd_tx=force_pd_tx
                else:
                    self.i2c.ckgen.force_pd_tx=force_pd_tx

                for k in range(0, 2):

                    self.pbus.set_dco(0x100, 0x100, 0x100, 0x100)
                    self.mem.wrm(0x600060a0, 17, 16, 3)
                    self.wifi.rxdc_cal()

                    out=self.adc_dump.adcdumptest('null',8000,'sw',"10bit",sample_80m=1,plot_en=0)
                    noise_floor = 0 #self.wifiapi.check_noise_floor()
                    noise_floor = int(noise_floor)/4

                    [rfrx1, rftx1, rftx2, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2] = self.pbus.all_pbus()
                    fw1.write_data([xpd_rfrx_vga,xpd_rfrx_lna,xpd_i2c_rfpll,filt_loop_en,rfrx_mx_db,force_pd_tx,k,hex(rfrx1),dcoi1, dcoq1, dcoi2, dcoq2, out[0:2],hex(bb1), hex(bb2)])

##        self.check_noise_floor_rfrx(chan,  name_str)
##        self.pbus.pbus_workmode()

    def get_rxiq_remain(self, length=2048, plot_en=0):
        dc_offset=self.adc_dump.adcdumptest(logdir='dump',dump_num=length)
        filename = dc_offset[4]
        r_data=myplot.get_csv_vect(filename,3,1)
        i_data=myplot.get_csv_vect(filename,3,2)
        data_ll=len(r_data)
        ll=2**int(np.log2(data_ll))
        real_data=r_data[0:ll]
        image_data=i_data[0:ll]
        fftdata=myplot.fft_calc(real_data,image_data)
        db_data=10*np.log10(fftdata)
        db_data = db_data.tolist()
        ll = len(db_data)
        sig_db = max(db_data)
        freq_index = db_data.index(sig_db)
        iq_db = max(db_data[ll-freq_index-4:ll-freq_index+4])
        rxiq_db = iq_db - sig_db
##        print db_data[ll-freq_index-4:ll-freq_index+4]
##        print [sig_db, iq_db]
        if plot_en==1:
            x=np.array(range(0,ll))*80*1.0/ll
            plt.plot(x, db_data)
            plt.show()
        loginfo('rxiq_db=%2.2f'%rxiq_db)
        return rxiq_db

    def rfrx_sat_pwr(self, tester, device, tx_freq, tx_pwr, iqv_no):
        rxpwr_start = tx_pwr+5
        rxpwr_end = tx_pwr+50
        for rx_pwr in range(rxpwr_start,rxpwr_end,2):
            self.tester_set_freq(tester, device, tx_freq, rx_pwr, iqv_no)
            res=self.adc_dump.adcdumptest(logdir='dump',dump_num=100)
            vga_sat=res[6]
            lna_sat=res[5]
            print '\n11\n'
            print [rx_pwr, vga_sat, lna_sat]
            if vga_sat>0 or lna_sat>0 or rx_pwr >= 15:
                print "\nbreak\n"
                break
        return rx_pwr

    def sweep_rx_table(self,cable_att=2, tx_chan=1, iqv_no=2, name_str='', device='TESTER', bt_mode=0):

        length = 8000

        fname = self.wifi.get_filename('sweep_rx_table_%s'%name_str, 'sweep_rx_table_%d_%s'%(tx_chan, name_str))
        title = 'gain,rx_gain_force,rfrx_gain,bb_gain,tone_power,rx_power,rx_noise,rx_gain,gain_delta, rfrx_sat_power,rxiq_db,dci, dcq, cable_lose,bb1, dcoi1, dcoq1, dcoi2, dcoq2\n'
        fw1=csvreport(fname, title)

        if tx_chan<=14:
            self.wifi.rfchsel(tx_chan)
            tx_freq = self.wifi.chan2freq(tx_chan)+2   #5M Tone
        else:
            self.rfpll.set_freq(tx_chan)
            tx_freq = tx_chan+2

        tx_pwr=-20

        tester = self.tester_init(tx_freq, tx_pwr, iqv_no, cable_att, device)

        sub_pwr=0
        gain_err=''
        num = 0

        max_gain = self.wifi.rx_max_gain(bt_mode)

        tx_pwr_old = tx_pwr

        if bt_mode==1:
            self.i2c.bbtop.encmplx_btrx = 0
            self.wifi.bt_rx_force(1)

        for  gain in range (0,max_gain+1):

            self.wifi.rx_force_gain(1, gain, bt_mode)

            if device=="TESTER":
                tester.txenable(1)

            [tx_pwr, out] = self.get_tx_power(tester, device, tx_freq, tx_pwr, cable_att,iqv_no, length)

            if bt_mode==1:
                rxiq_db = 0
                rfrx_sat_power = 0
            else:
                rxiq_db = self.get_rxiq_remain(1024)
                if self.pbus.pbus_rd('bb','en2')==0:
                    rfrx_sat_power = self.rfrx_sat_pwr(tester, device, tx_freq, tx_pwr, iqv_no)

            if num>0 and tx_pwr_old!=tx_pwr:
                start = 0
            else:
                start = 1

            tx_pwr_old = tx_pwr

            for rei in range(start,2):

                if device=="TESTER":
                    tester.txenable(1)

                if rei==0:
                    gain_set = gain - 1
                else:
                    gain_set = gain

                self.wifi.rx_force_gain(1, gain_set, bt_mode)

                self.tester_set_freq(tester, device, tx_freq, tx_pwr, iqv_no)

                out=self.adc_dump.adcdumptest('null',length,'sw',"10bit",sample_80m=1,plot_en=0)
                rx_pwr = out[2]
                avgi = out[0]
                avgq = out[1]

                get_pwr = rx_pwr - tx_pwr
                print '\ni=%d, gain=%d,%d, tx_pwr=%2.2f,%2.2f, rx_pwr=%2.2f, get_pwr=%2.2f, rei=%d\n'%(rei, gain, gain_set, tx_pwr,tx_pwr_old, rx_pwr, get_pwr, rei)

                if num==0:
                    sub_pwr = 1
                else:
                    sub_pwr = get_pwr-old_pwr

                if device=="TESTER":
                    tester.txenable(0)
                else:
                    self.tester_set_pwr(tester, -97, iqv_no, device)

                noise_out=self.adc_dump.adcdumptest('null',length,'sw',"10bit",sample_80m=1,plot_en=0)
                rx_noise = noise_out[3]
                avgi = out[0]
                avgq = out[1]

                [rfrx1, rftx1, rftx2, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2] = self.pbus.all_pbus()

                if rei == 1:
                    fw1.write_data([gain, gain_set, hex(rfrx1), hex(bb2), tx_pwr,rx_pwr, rx_noise, get_pwr, sub_pwr,rfrx_sat_power,rxiq_db,avgi, avgq, cable_att,hex(bb1), dcoi1, dcoq1, dcoi2, dcoq2])

                    if(sub_pwr>1.5) or (sub_pwr<0.5):
                        gain_err += "%d,%2.2f,%2.2f,%2.2f,%2.2f\n"%(gain_set, rx_pwr, tx_pwr, get_pwr, sub_pwr)

                    old_pwr = get_pwr
                num += 1

##            if tx_pwr==-70 and rx_pwr>51:
##                break
        if bt_mode==1:
            self.wifi.bt_rx_force(0)
        self.wifi.rx_force_gain(0, gain)
        print 'rx_gain_error:\n%s'%gain_err

    def get_rxdc_min(self, num=3, est_len=4096):
        dci = 200
        dcq = 200
        for k in range(0,num):
            [dci1, dcq1, power] = self.wifiapi.dc_iq_est(est_len)
            if np.abs(dci1) < np.abs(dci):
                dci = dci1
            if np.abs(dcq1) < np.abs(dcq):
                dcq = dcq1
        return [dci,dcq]

    def rxdc_cal(self,fw1='',coarse_en=0):
        rfrx = self.pbus.pbus_rd('rfrx1', 'en1')
        bbgain = self.pbus.pbus_rd('bb', 'en2')

        bbgain_db = 0
        for k in range(0,6):
            if bbgain&(1<<k):
                bbgain_db += 6
        bbgain_db += bbgain>>6
        scale = 10**(bbgain_db/20.0)

        if coarse_en==0:
            if ((bbgain&0xf)>0):
                scale = 2*4/3.0
            else:
                scale = 4/3.0

        if bbgain_db >=12:
            thres = 5
        else:
            thres = 4

        if rfrx < 0x1fe:
            thres = 2

        for i in range(0,20):
##            if coarse_en == 0:
##                self.pbus.pbus_wr('bb','en2',bbgain)
##                [dci1,dcq1] = self.get_rxdc_min(num=3,est_len=4096)
##                self.pbus.pbus_wr('bb','en2',bbgain|0x8)
##                [dci2,dcq2] = self.get_rxdc_min(num=3,est_len=4096)
##                dci = dci2 - dci1
##                dcq = dcq2 - dcq1
##                loginfo(dci1,dcq1,dci2,dcq2)

            [dci,dcq] = self.get_rxdc_min(num=3,est_len=4096)

            dc_coarse_i = self.pbus.pbus_rd('dcoi', 'en1')
            dc_coarse_q = self.pbus.pbus_rd('dcoq', 'en1')
            dc_fine_i = self.pbus.pbus_rd('dcoi', 'en2')
            dc_fine_q = self.pbus.pbus_rd('dcoq', 'en2')

            dci_comp = int(-dci/scale)
            dcq_comp = int(-dcq/scale)

            if (dci_comp == 0) and (dci > thres or dci < -thres):
                dci_comp = np.sign(-dci)
            if (dcq_comp == 0) and (dcq > thres or dcq < -thres):
                dcq_comp = np.sign(-dcq)

            loginfo(hex(rfrx),hex(bbgain),i,dc_coarse_i,dc_coarse_q,dc_fine_i,dc_fine_q,dci,dcq, bbgain_db, scale, dci_comp, dcq_comp)
            if fw1 != '':
                fw1.write_data([hex(rfrx),hex(bbgain),i,dc_coarse_i,dc_coarse_q,dc_fine_i,dc_fine_q,dci,dcq, bbgain_db, scale])

            if (dci <= thres and dci >= -thres) and (dcq <= thres and dcq >= -thres):
                break
            else:
                if coarse_en == 1:
                    dc_coarse_i += dci_comp
                    dc_coarse_q += dcq_comp
                    self.pbus.pbus_wr('dcoi', 'en1', dc_coarse_i)
                    self.pbus.pbus_wr('dcoq', 'en1', dc_coarse_q)
                else:
                    dc_fine_i += dci_comp
                    dc_fine_q += dcq_comp
                    self.pbus.pbus_wr('dcoi', 'en2', dc_fine_i)
                    self.pbus.pbus_wr('dcoq', 'en2', dc_fine_q)

        self.pbus.pbus_wr('bb', 'en2', bbgain)
        return [dc_coarse_i,dc_coarse_q,dc_fine_i,dc_fine_q,i,dci,dcq]

    def rxdc_cal_coarse(self,name_str=''):

        fname = self.wifi.get_filename('rxdc_cal_test', 'rxdc_cal_coarse_%s'%(name_str))
        title = 'chan, index,rfrx1,bbgain,bbgain_db,dcoi_coarse, dcoq_coarse, dcoi_fine, dcoq_fine,dc_cal_num,dc_est_i, dc_est_q\n'
        fw1=csvreport(fname, title)

        rfrx_m = [0x1a0,0x184,0x1ee,0x1f8,0x1fe,0x1fe,0x1fe,0x1fe]
        bbc_m = [0,0,0,0,0,0x20,0x30,0x32]
        bbf_m = range(0,6,2)

        dc_coarse_i = 256
        dc_coarse_q = 256

        for chan in range(2,16,2):
            self.wifi.rfchsel(chan)
            self.pbus.pbus_debugmode()
            for index in range(0,len(rfrx_m)):
                rfrx = rfrx_m[index]
                bbc = bbc_m[index]

                bbgain_db_c = 0
                for k in range(0,6):
                    if bbc&(1<<k):
                        bbgain_db_c += 6

                for bbf in bbf_m:
                    bb = (bbf<<6) + bbc
                    self.pbus.pbus_wr('rfrx1','en1',rfrx)
                    self.pbus.pbus_wr('bb','en2',bb)
                    bbgain_db = bbgain_db_c + bbf
                    self.pbus.set_dco(dc_coarse_i,dc_coarse_q, 256, 256)
                    [dc_coarse_i,dc_coarse_q,dc_fine_i,dc_fine_q,i,dci,dcq] = self.rxdc_cal('',coarse_en=1)
                    loginfo(chan,index,hex(rfrx),hex(bb),dc_coarse_i,dc_coarse_q,dc_fine_i,dc_fine_q,i,dci,dcq)
                    fw1.write_data([chan,index,hex(rfrx),hex(bb),bbgain_db,dc_coarse_i,dc_coarse_q,dc_fine_i,dc_fine_q,i,dci,dcq])
            self.pbus.pbus_workmode()

    def rfrx_rxdc_coarse_cal(self, fw1=''):
        rfrx_cal_dci = []
        rfrx_cal_dcq = []
        rfrx_cal = [0x1a0,0x184,0x1ee,0x1f8,0x1fe]
        bbf_m = [1,4]
        for rfrx in rfrx_cal:
            for bbf in bbf_m:
                bb = bbf<<6
                self.pbus.pbus_wr('rfrx1','en1',rfrx)
                self.pbus.pbus_wr('bb','en2',bb)
                self.pbus.set_dco(256,256, 256, 256)
                [dc_coarse_i,dc_coarse_q,dc_fine_i,dc_fine_q,i,dci,dcq] = self.rxdc_cal('',coarse_en=1)
                [rfrx, rftx1, rftx2, bb, bb1, dc_coarse_i,dc_coarse_q,dc_fine_i,dc_fine_q] = self.pbus.all_pbus()
                loginfo(hex(rfrx),hex(bb),dc_coarse_i,dc_coarse_q,dc_fine_i,dc_fine_q,i,dci,dcq)
                if fw1 != '':
                    fw1.write_data([6,55,hex(rfrx),hex(bb),55,dc_coarse_i,dc_coarse_q,dc_fine_i,dc_fine_q,dci,dcq])
                rfrx_cal_dci.append(dc_coarse_i)
                rfrx_cal_dcq.append(dc_coarse_q)
        return [rfrx_cal_dci, rfrx_cal_dcq]

    def chan_rxdc_fine_cal(self, fw1, rfrx_cal_dci, rfrx_cal_dcq):
        chan_cal_dci = []
        chan_cal_dcq = []
        dc_coarse_i = rfrx_cal_dci[-1]
        dc_coarse_q = rfrx_cal_dcq[-1]
        dc_fine_i = 256
        dc_fine_q = 256
        bbc_cal = [0x120,0x130]
        for chan in range(2,16,2):
            rfrx = 0x1fe
            for bb in bbc_cal:
                self.pbus.pbus_wr('rfrx1','en1',rfrx)
                self.pbus.pbus_wr('bb','en2',bb)
                self.pbus.set_dco(dc_coarse_i,dc_coarse_q, 256, 256)
                [dc_coarse_i,dc_coarse_q,dc_fine_i,dc_fine_q,i,dci,dcq] = self.rxdc_cal('',coarse_en=0)
                [rfrx, rftx1, rftx2, bb, bb1, dc_coarse_i,dc_coarse_q,dc_fine_i,dc_fine_q] = self.pbus.all_pbus()
                loginfo(chan,hex(rfrx),hex(bb),dc_coarse_i,dc_coarse_q,dc_fine_i,dc_fine_q,i,dci,dcq)
                if fw1 != '':
                    fw1.write_data([chan,55,hex(rfrx),hex(bb),55,dc_coarse_i,dc_coarse_q,dc_fine_i,dc_fine_q,dci,dcq])
                chan_cal_dci.append(dc_fine_i)
                chan_cal_dcq.append(dc_fine_q)
        return [chan_cal_dci, chan_cal_dcq]

    def rxdc_cal_test(self,name_str=''):
        fname = self.wifi.get_filename('rxdc_cal_test', 'rxdc_cal_test1_%s'%(name_str))
        title = 'chan, rfrx1,bbgain,bbgain_db,dcoi_coarse, dcoq_coarse, dcoi_fine, dcoq_fine,dc_cal_num,dc_est_i, dc_est_q\n'
        fw1=csvreport(fname, title)

        self.pbus.pbus_debugmode()
        self.wifi.rfchsel(6)

        [rfrx_cal_dci, rfrx_cal_dcq] = self.rfrx_rxdc_coarse_cal(fw1)

        [chan_cal_dci, chan_cal_dcq] = self.chan_rxdc_fine_cal(fw1, rfrx_cal_dci, rfrx_cal_dcq)

        rfrx_m = [0x1a0,0x184,0x1ee,0x1f8,0x1fe,0x1fe,0x1fe,0x1fe]
        bbc_m = [0,0,0,0,0,0x20,0x30,0x32]
        bbf_m = range(0,6,2)
        for chan in range(2,16,2):
            self.wifi.rfchsel(chan)
            for index in range(0,len(rfrx_m)):
                rfrx = rfrx_m[index]
                bbc = bbc_m[index]

                bbgain_db_c = 0
                for k in range(0,6):
                    if bbc&(1<<k):
                        bbgain_db_c += 6

                for bbf in bbf_m:
                    bb = (bbf<<6) + bbc
                    self.pbus.pbus_wr('rfrx1','en1',rfrx)
                    self.pbus.pbus_wr('bb','en2',bb)
                    bbgain_db = bbgain_db_c + bbf

                    i1 = index
                    if i1>4:
                        i1 = 4
                    if bbf<3:
                        dc_coarse_i = rfrx_cal_dci[i1*2]
                        dc_coarse_q = rfrx_cal_dcq[i1*2]
                    else:
                        dc_coarse_i = rfrx_cal_dci[i1*2+1]
                        dc_coarse_q = rfrx_cal_dcq[i1*2+1]

                    if rfrx < 0x1fe:
                        dc_fine_i = 256
                        dc_fine_q = 256
                    else:
                        if bbc < 0x30:
                            dc_fine_i = chan_cal_dci[chan-2]
                            dc_fine_q = chan_cal_dcq[chan-2]
                        else:
                            dc_fine_i = chan_cal_dci[chan-2+1]
                            dc_fine_q = chan_cal_dcq[chan-2+1]

                    self.pbus.set_dco(dc_coarse_i,dc_coarse_q, dc_fine_i,dc_fine_q)
                    [dci,dcq] = self.get_rxdc_min(num=3,est_len=4096)
                    [rfrx, rftx1, rftx2, bb, bb1, dc_coarse_i,dc_coarse_q,dc_fine_i,dc_fine_q] = self.pbus.all_pbus()
                    loginfo(chan,index,hex(rfrx),hex(bb),dc_coarse_i,dc_coarse_q,dc_fine_i,dc_fine_q,dci,dcq)
                    fw1.write_data([chan,index,hex(rfrx),hex(bb),bbgain_db,dc_coarse_i,dc_coarse_q,dc_fine_i,dc_fine_q,dci,dcq])


    def check_rxdc_cal(self,fw1='',name_str=''):
        fname = self.wifi.get_filename('rxdc_cal_test', 'check_rxdc_cal_%s'%(name_str))
        title = 'rfrx1,bbgain,chan,i,dcoi_coarse, dcoq_coarse, dcoi_fine, dcoq_fine,dci_remain,dcq_remain\n'
        if fw1=='':
            fw1=csvreport(fname, title)

        logsetlevel("I")
        self.wifi.rfchsel(14,0)
        self.mem.wrm(0x600050e8,23,16,0) #fe_rx_scale
        self.mem.wrm(0x6001c02c,31,23,(((70)<<1) | 1)) #force gain(for rssi=-68)
        [rfrx1_rd, rftx1, rftx2, bb2_rd, bb1_rd, dcoi_c_org, dcoq_c_org, dcoi_f_org, dcoq_f_org] = self.pbus.all_pbus()

        self.pbus.pbus_debugmode()
        bbc_m = [0,0x20,0x30,0x32]
        bbf_m = range(0,6,2)
        rfrx = 0x1fe
        i = 0
        for bbc in bbc_m:
            for bbf in bbf_m:
                bb = (bbf<<6) + bbc
                self.pbus.pbus_wr('rfrx1','en1',rfrx)
                self.pbus.pbus_wr('bb','en2',bb)
                self.pbus.set_dco(dcoi_c_org, dcoq_c_org, dcoi_f_org, dcoq_f_org)

                if bbc == 0x32:
                    thres = 6
                else:
                    thres = 3
                [dc_coarse_i,dc_coarse_q,dc_fine_i,dc_fine_q] = self.rxdc_cal(coarse_en=0,thres=thres)
                i += 1
                dci_m = []
                dcq_m = []
                for chan in range(1,15,2):
                    if chan==14:
                        freq = 2484
                    else:
                        freq = 2412 + (chan-1)*5
                    self.wifiapi.phy_set_freq(freq)
                    #[dc_coarse_i,dc_coarse_q,dc_fine_i,dc_fine_q] = self.rxdc_cal(coarse_en=1,thres=3)
                    for j in range(0,2):
                        dci = 100
                        dcq = 100
                        for k in range(0,3):
                            [dci1, dcq1, power] = self.iq_est.dc_iq_est(4000)
                            if np.abs(dci1) < np.abs(dci):
                                dci = dci1
                            if np.abs(dcq1) < np.abs(dcq):
                                dcq = dcq1

                        loginfo(hex(rfrx),hex(bb),chan,j,dc_coarse_i,dc_coarse_q,dc_fine_i,dc_fine_q,dci,dcq)
                        fw1.write_data([hex(rfrx),hex(bb),chan,j,dc_coarse_i,dc_coarse_q,dc_fine_i,dc_fine_q,dci,dcq])
        self.pbus.pbus_workmode()


    def sweep_rxdc_chan(self,rfrx_en=0, chan_step=1,name_str=''):

        fname = self.wifi.get_filename('sweep_rxdc_chan', 'sweep_rxdc_chan_%d_%s'%(rfrx_en, name_str))
        title = 'rfrx1, bbc, bbf,dcoi_coarse, dcoq_coarse, dcoi_fine, dcoq_fine,'
        title += self.rxdc_title_chan(step=chan_step, freq_en=0)
        title += '\n'
        fw1=csvreport(fname, title)

        self.mem.wrm(0x600050e8,23,16,0) #fe_rx_scale

        self.mem.wrm(0x6001c02c,31,23,(((10)<<1) | 1)) #force gain(for rssi=-68)

        rfrx_m = [0x1a0,0x184,0x1a6,0x1b4,0x1e4,0x1c6,0x1e6,0x1ee,0x1d0,0x1d4,0x1f4,0x1f8,0x1fe]
        bbc_m = [0,0x20,0x30,0x32,0x38, 0x8,0x2]
        bbf_m = range(0,6)

        if rfrx_en ==1:
            bbc_m = [0,0x20]
            bbf_m = [0]
        else:
            rfrx_m = [0]

        self.pbus.pbus_debugmode()

        for rfrx in rfrx_m:
            for bbc in bbc_m:
                for bbf in bbf_m:

                    bb = (bbf<<6) + bbc
                    self.pbus.pbus_wr('rfrx1','en1',rfrx)
                    self.pbus.pbus_wr('bb','en2',bb)
                    self.pbus.set_dco(256, 256, 256, 256)
                    [rfrx1_rd, rftx1, rftx2, bb2_rd, bb1_rd, dcoi_c_org, dcoq_c_org, dcoi_f_org, dcoq_f_org] = self.pbus.all_pbus()
                    dci_m = []
                    dcq_m = []
                    for chan in range(1,15,chan_step):
                        self.wifi.rfchsel(chan, 0)
                        [dc_est_i, dc_est_q, power] = self.iq_est.dc_iq_est(8000)
                        dci_m.append(dc_est_i)
                        dcq_m.append(dc_est_q)

                    fw1.write_data([hex(rfrx),hex(bbc),hex(bbf),dcoi_c_org, dcoq_c_org, dcoi_f_org, dcoq_f_org, dci_m, dcq_m])
        self.pbus.pbus_workmode()


    def sweep_rxdc(self,rfrx_en=0, name_str=''):

        tx_chan = 1
        fname = self.wifi.get_filename('sweep_rxdc', 'sweep_rxdc_%d_%d_%s'%(tx_chan, rfrx_en, name_str))
        title = 'rfrx1, bbc, bbf, i,dcoi_coarse, dcoq_coarse, dcoi_fine, dcoq_fine, adc_i, adc_i1, adc_i2, adc_q, adc_q1,adc_q2, scale_i, scale_i1, scale_i2, scale_q, scale_q1, scale_q2\n'
        fw1=csvreport(fname, title)

        self.wifi.rfchsel(tx_chan)

        self.mem.wrm(0x600050e8,23,16,0) #fe_rx_scale

        self.mem.wrm(0x6001c02c,31,23,(((10)<<1) | 1)) #force gain(for rssi=-68)
        rfrx1 = 0x184

        self.pbus.pbus_debugmode()

        num = 0

##        bbc_m = [0x0,0x2,0x8,0xc,0x10,0x12,0x18,0x1c, 0x20,0x28,0x22,0x2c, 0x30, 0x38,0x32,0x3c]
##        rfrx_m = [0x184, 0x186, 0x18e, 0x194, 0x196, 0x19e, 0x1a4, 0x1a6, 0x1ae, 0x1b4, 0x1b6, 0x1be, 0x1c4, 0x1c6, 0x1ce, 0x1d4, 0x1d6, 0x1de, 0x1e4, 0x1e6, 0x1ee, 0x1f4, 0x1f6, 0x1fe]
##        rfrx_m = [0x182,0x186,0x18e,0x19e,0x1be,0x1fe]
        rfrx_m = [0x0,0x100,0x104,0x184,0x186,0x18e,0x19e,0x1be,0x1fe]
        bbc_m = [0,0x20,0x30,0x32,0x38, 0x8,0x2]

##        if rfrx_en==0:
##            for bbc in bbc_m:
##                self.sweep_rxdc_slv(fw1, rfrx1, bbc, 2, rfrx_en)
##                num = num +1
##                print num
##            for bbf in range (0, 6):
##                self.sweep_rxdc_slv(fw1, rfrx1, 0x20, bbf, rfrx_en)
##                num = num +1
##                print num

        if rfrx_en==0:
            for bbc in bbc_m:
                for bbf in range (0, 6):
                    self.sweep_rxdc_slv(fw1, 0, bbc, bbf, 1)
                    num = num +1
                    print num
        else:
            for rfrx in rfrx_m:
                for bbc in [0x0, 0x20]:
                    for bbf in [3]:
                        self.sweep_rxdc_slv(fw1, rfrx, bbc, bbf, 0)
                        num = num +1
                        print num
        self.pbus.pbus_workmode()


    def sweep_rxdc_slv(self,fw, rfrx1, bbc, bbf, set_dco=0):

        scale = 10
        length = 8000
        test_time = 1
        #pbus.pbus('rfrx1','en1',0x1e0)
        bb = (bbf<<6) + bbc
        self.pbus.pbus_wr('rfrx1','en1',rfrx1)
        self.pbus.pbus_wr('bb','en2',bb)

        if set_dco==1:
            self.pbus.set_dco(256, 256, 256, 256)
##            test_time = 1
##        else:
##            self.wifi.rxdc_cal()
        [rfrx1_rd, rftx1, rftx2, bb2_rd, bb1_rd, dcoi_c_org, dcoq_c_org, dcoi_f_org, dcoq_f_org] = self.pbus.all_pbus()

        for j in range(test_time):
            if j==0:
                dco_data = [dcoi_c_org,dcoq_c_org,dcoi_f_org,dcoq_f_org]
            elif j==1:
                dco_data = [dcoi_c_org+scale,dcoq_c_org+scale,dcoi_f_org,dcoq_f_org]
            else:
                dco_data = [dcoi_c_org,dcoq_c_org,dcoi_f_org+scale,dcoq_f_org+scale]

            self.pbus.pbus_wr('dcoi', 'en1', dco_data[0])
            self.pbus.pbus_wr('dcoq', 'en1', dco_data[1])
            self.pbus.pbus_wr('dcoi', 'en2', dco_data[2])
            self.pbus.pbus_wr('dcoq', 'en2', dco_data[3])

            dci = []
            dcq = []
            for k in range(3):
                [dc_est_i, dc_est_q, power] = self.iq_est.dc_iq_est(length)
                dci.append(dc_est_i)
                dcq.append(dc_est_q)

            if j==0:
                dci_org = dci
                dcq_org = dcq

            gain_i = []
            gain_q = []
            for k in range(3):
                gain_i.append(float(dci[k]-dci_org[k])/scale)
                gain_q.append(float(dcq[k]-dcq_org[k])/scale)

            fw.write_data([hex(rfrx1),hex(bbc),hex(bbf),j, dco_data, dci, dcq, gain_i, gain_q])

    def rxdc_title_chan(self, step=1, freq_en=0):
        title = ''
        for i in range(1,15,step):
            if freq_en:
                freq = 2412 + (i-1)*5
                title += 'dci_%d,'%(freq)
            else:
                title += 'dci_%d,'%(i)
        for i in range(1,15,step):
            if freq_en:
                freq = 2412 + (i-1)*5
                title += 'dcq_%d,'%(freq)
            else:
                title += 'dcq_%d,'%(i)
        return title

    def rxdc_remain_check(self,name_str='', freq_en=0, step=3):

        fname = self.wifi.get_filename('rxdc_remain_check_%s'%name_str, 'rxdc_remain_check_%s'%(name_str))
        title = 'gain,chan,rfrx1,bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2,dc_est_i,dc_est_q,dc_est_i,dc_est_q\n'
        fw1=csvreport(fname, title)

        logsetlevel("I")
##        self.wifi.rfchsel(6)
        max_gain = 20#self.wifi.rx_max_gain(0)
        start =  0#max_gain-34 #0
        for  gain in range (start, max_gain+1, 1):
            for i in range(1,15,step):
                self.wifi.rx_force_gain(0, gain, 0)
                if freq_en:
                    freq = 2412 + (i-1)*5
                    self.wifiapi.phy_set_freq(freq)
                else:
                    chan = i
                    self.wifi.rfchsel(chan)

                self.wifi.rx_force_gain(1, gain, 0)
                datai = []
                dataq = []
                for k in range(2):
                    [dc_est_i, dc_est_q] = self.get_rxdc_min(num=3,est_len=4095)
                    datai.append(dc_est_i)
                    dataq.append(dc_est_q)
                [rfrx1, rftx1, rftx2, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2] = self.pbus.all_pbus()
                loginfo(gain,i,hex(rfrx1),hex(bb2),hex(bb1), dcoi1, dcoq1, dcoi2, dcoq2,datai,dataq)
                fw1.write_data([gain,i,hex(rfrx1),hex(bb2),hex(bb1),(dcoi1),(dcoq1),(dcoi2),(dcoq2),datai,dataq])

    def sweep_rxgain_force_all_channel_radition(self, cable_att_list=[12], chan_step=2, rfrx_en=1, iqv_no=1, device="TESTER", fix_pwr=0, name_str=''):
        '''iq_no: 1 means right port, 0 means left port'''

        logsetlevel("ERROR")
        dump_len = 8000
        tx_pwr = -20
        cable_att = cable_att_list[0]
##        tx_freq = self.wifi.chan2freq(tx_chan)+5   #5M Tone
##        self.rfpll.set_freq(tx_freq)
        tx_freq = 2484
##        self.rfpll.set_freq(tx_freq)
        tester = self.tester_init(tx_freq+2, tx_pwr, iqv_no, cable_att, device)

        self.pbus.pbus_debugmode()
        num = 0
        tx_pwr_m = [5,-20,-15, -25,-30,-30, 5,0,0, -30,-35,-35, -25, -30,-40, -45, -45, -55, -30, -35, -35, -50,-55, -55]

        rfrx_m = [0x180,0x190,0x1a0,0x1b0,0x1c0,0x1d0,0x1e0,0x1f0]
        rfrx_f = range(0,16,2)

        bb_m = [0, 0x20, 0x30, 0x38, 0x32]
        bb_f = range(0,6,1)

        chan_s = ''
        delta_s = ''
        lna_dcap_s = ''
        vga_dcap_s = ''
        for chan in [1,2,3,4,5,6,7,8,9,10,11,12,13,14]: #range(1,15, chan_step):
            chan_s += "chan%d_rx_gain,"%chan
            cable_att = cable_att_list[chan-1]
            delta_s += 'chan%d_gain_delta,'%chan
            lna_dcap_s += 'lna_dcap_%d,'%chan
            vga_dcap_s += 'vga_dcap_%d,'%chan

        title = 'rfrx_gain,bb_gain,tone_power,rx_power,rx_noise,rx_gain,max_delta,min_delta,rxdc_i,rxdc_q,' +chan_s+delta_s+lna_dcap_s+vga_dcap_s+'XPD_RFRX_VGA, XPD_RFRX_LNA, RXSW_HG, RXSW_HG_FINE,LNA_DG,VGA_DG_GM,VGA_DG_BUF,VGA_DG_LOAD, bb1, dcoi1, dcoq1, dcoi2, dcoq2\n'


        if rfrx_en==1:
            gain_m = rfrx_m
            gain_f = rfrx_f
        else:
            gain_m = bb_m
            gain_f = bb_f

        fname = self.wifi.get_filename('sweep_rxgain_force_%s'%name_str, 'sweep_rxgain_force_%d_%d_%s'%(tx_freq,rfrx_en, name_str))
        fw1=csvreport(fname, title)

        num = 0
        for  gain in gain_m:
            for fine_gain in gain_f:
                if rfrx_en==1:
                    rfrx = gain+fine_gain
                    bb2 = 0
                else:
                    rfrx = 0x184
                    bb2 = gain+(fine_gain<<6)

                self.pbus.pbus_wr('rfrx1', 'en1', rfrx)

                if self.chipv=='ESP8266':
                    self.pbus.set_dco(254,287,256,256)

                else:
                    self.pbus.pbus_wr('bb', 'en2', bb2)
                    self.pbus.set_dco(0x100, 0x100, 0x100, 0x100)
                    self.mem.wrm(0x600060a0, 17, 16, 3)
                    self.wifi.rxdc_cal()

                if fix_pwr==1:
                    tx_pwr = tx_pwr_m[num]
                    self.tester_set_freq(tester, device, tx_freq+2, tx_pwr, iqv_no)
                else:
                    [tx_pwr, out] = self.get_tx_power(tester, device, tx_freq+2, tx_pwr, cable_att,iqv_no, dump_len)

                mean_pwr = 0
                get_pwr_m = []
                max_dci = 0
                max_dcq = 0
                lna_dcap_m = []
                vga_dcap_m = []
                for chan in [1,2,3,4,5,6,7,8,9,10,11,12,13,14]: #range(1,15, chan_step):
                    self.wifi.rfchsel(chan, 0)

                    self.wifiapi.set_rfrx_dcap()
                    lna_dcap_m.append(self.wifi.i2c_ric('rfrx', 'rfrx_lna_dcap'))
                    vga_dcap_m.append(self.wifi.i2c_ric('rfrx', 'rfrx_vga_dcap'))

                    tx_freq = self.wifi.chan2freq(chan)   #5M Tone
    ##                self.rfpll.set_freq(tx_freq)
                    self.wifi.rxdc_cal()

                    self.tester_set_freq(tester, device, tx_freq+2, tx_pwr, iqv_no)

                    for kk in range(2):
                        out=self.adc_dump.adcdumptest('null',dump_len,'sw',"10bit",sample_80m=1,plot_en=0)
                        print chan
                        print out
                    avgi = out[0]
                    avgq = out[1]
                    rx_pwr = out[2]

                    get_pwr = rx_pwr - tx_pwr
                    mean_pwr +=get_pwr
                    get_pwr_m.append(get_pwr)

                    if avgi>max_dci:
                        max_dci = avgi
                    if avgq > max_dcq:
                        max_dcq = avgq

                pwr_len = len(get_pwr_m)
                mean_pwr = mean_pwr/pwr_len
                delta_m = []
                max_delta = 0
                min_delta = 0
                print get_pwr_m
                print pwr_len
                print mean_pwr
                for i in range(0,pwr_len):
                    delta = get_pwr_m[i]-mean_pwr
                    if delta < min_delta:
                        min_delta = delta
                    if delta > max_delta:
                        max_delta = delta
                    delta_m.append(delta)

                [rfrx1, rftx1, rftx2, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2] = self.pbus.all_pbus()

                rfrx_b = []
                if rfrx_en==1:
                    for i in range(8, 0, -1):
                        rfrx_b.append((rfrx1>>i)&1)

                tester.txenable(0)  #IQV
                noise_out=self.adc_dump.adcdumptest('null',dump_len,'sw',"10bit",sample_80m=1,plot_en=0)
                rx_noise = noise_out[3]
                tester.txenable(1)  #IQV

                fw1.write_data([hex(rfrx1),hex(bb2),tx_pwr, rx_pwr, rx_noise, mean_pwr,max_delta, min_delta, max_dci, max_dcq, get_pwr_m, delta_m,lna_dcap_m,vga_dcap_m,rfrx_b, hex(bb1), dcoi1, dcoq1, dcoi2, dcoq2])

                old_pwr = get_pwr
                num += 1

        self.pbus.pbus_workmode()
        logsetlevel("DEBUG")
        self.tester_txdis(tester, device)

    def sweep_rxgain_force(self, cable_att=12, chan_step=4, rfrx_en=1, iqv_no=1, device="TESTER", name_str=''):
        '''iq_no: 1 means right port, 0 means left port'''

        logsetlevel("ERROR")
        dump_len = 8000
        tx_pwr = -20
##        tx_freq = self.wifi.chan2freq(tx_chan)+5   #5M Tone
##        self.rfpll.set_freq(tx_freq)
        tx_freq = 2484
##        self.rfpll.set_freq(tx_freq)
        tester = self.tester_init(tx_freq+2, tx_pwr, iqv_no, cable_att, device)

        self.pbus.pbus_debugmode()
        num = 0
        rfrx_m = [0x180,0x190,0x1a0,0x1b0,0x1c0,0x1d0,0x1e0,0x1f0]
##        rfrx_m = [0x180,0x1f0]
        rfrx_f = range(0,16,2)

        bb_m = [0, 0x20, 0x30, 0x38, 0x32]
        bb_f = range(0,6,1)

        chan_s = ''
        delta_s = ''
        lna_dcap_s = ''
        vga_dcap_s = ''
        for chan in range(14,15,chan_step):
            chan_s += "chan%d_rx_gain,"%chan
            delta_s += 'chan%d_gain_delta,'%chan
            lna_dcap_s += 'lna_dcap_%d,'%chan
            vga_dcap_s += 'vga_dcap_%d,'%chan

        title = 'rfrx_gain,bb_gain,tone_power,rx_power,rfrx_sat_pwr,rx_noise,rx_gain,max_delta,min_delta,rxdc_i,rxdc_q,' +chan_s+delta_s+lna_dcap_s+vga_dcap_s+'XPD_RFRX_VGA, XPD_RFRX_LNA, RXSW_HG, RXSW_HG_FINE,LNA_DG,VGA_DG_GM,VGA_DG_BUF,VGA_DG_LOAD, bb1, dcoi1, dcoq1, dcoi2, dcoq2\n'

        if rfrx_en==1:
            gain_m = rfrx_m
            gain_f = rfrx_f
        else:
            gain_m = bb_m
            gain_f = bb_f

        fname = self.wifi.get_filename('sweep_rxgain_force_%s'%name_str, 'sweep_rxgain_force_%d_%d_%s'%(tx_freq,rfrx_en, name_str))
        fw1=csvreport(fname, title)

        num = 0
        for  gain in gain_m:
            for fine_gain in gain_f:
                if rfrx_en==1:
                    rfrx = gain+fine_gain
                    bb2 = 0
                else:
                    rfrx = 0x184
                    bb2 = gain+(fine_gain<<6)

                self.pbus.pbus_wr('rfrx1', 'en1', rfrx)

                if self.chipv=='ESP8266':
                    self.pbus.set_dco(254,287,256,256)

                else:
                    self.pbus.pbus_wr('bb', 'en2', bb2)
                    self.pbus.set_dco(0x100, 0x100, 0x100, 0x100)
                    self.mem.wrm(0x600060a0, 17, 16, 3)
                    self.wifi.rxdc_cal()

                [tx_pwr, out] = self.get_tx_power(tester, device, tx_freq+2, tx_pwr, cable_att,iqv_no, dump_len)
                rfrx_sat_pwr = self.rfrx_sat_pwr(tester, device, tx_freq+2, tx_pwr, iqv_no)

                mean_pwr = 0
                get_pwr_m = []
                max_dci = 0
                max_dcq = 0
                lna_dcap_m = []
                vga_dcap_m = []
                for chan in range(14,15,chan_step):
                    self.wifi.rfchsel(chan, 0)

##                    self.wifiapi.set_rfrx_dcap()
                    lna_dcap_m.append(self.wifi.i2c_ric('rfrx', 'rfrx_lna_dcap'))
                    vga_dcap_m.append(self.wifi.i2c_ric('rfrx', 'rfrx_vga_dcap'))

                    tx_freq = self.wifi.chan2freq(chan)   #5M Tone
    ##                self.rfpll.set_freq(tx_freq)
                    self.wifi.rxdc_cal()

                    self.tester_set_freq(tester, device, tx_freq+2, tx_pwr, iqv_no)

                    for kk in range(2):
                        out=self.adc_dump.adcdumptest('null',dump_len,'sw',"10bit",sample_80m=1,plot_en=0)
                        print chan
                        print out
                    avgi = out[0]
                    avgq = out[1]
                    rx_pwr = out[2]

                    get_pwr = rx_pwr - tx_pwr
                    mean_pwr +=get_pwr
                    get_pwr_m.append(get_pwr)

                    if avgi>max_dci:
                        max_dci = avgi
                    if avgq > max_dcq:
                        max_dcq = avgq

                pwr_len = len(get_pwr_m)
                mean_pwr = mean_pwr/pwr_len
                delta_m = []
                max_delta = 0
                min_delta = 0
                print get_pwr_m
                print pwr_len
                print mean_pwr
                for i in range(0,pwr_len):
                    delta = get_pwr_m[i]-mean_pwr
                    if delta < min_delta:
                        min_delta = delta
                    if delta > max_delta:
                        max_delta = delta
                    delta_m.append(delta)

                [rfrx1, rftx1, rftx2, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2] = self.pbus.all_pbus()

                rfrx_b = []
                if rfrx_en==1:
                    for i in range(8, 0, -1):
                        rfrx_b.append((rfrx1>>i)&1)

                tester.txenable(0)  #IQV
                noise_out=self.adc_dump.adcdumptest('null',dump_len,'sw',"10bit",sample_80m=1,plot_en=0)
                rx_noise = noise_out[3]
                tester.txenable(1)  #IQV

                fw1.write_data([hex(rfrx1),hex(bb2),tx_pwr, rx_pwr, rfrx_sat_pwr,rx_noise, mean_pwr,max_delta, min_delta, max_dci, max_dcq, get_pwr_m, delta_m,lna_dcap_m,vga_dcap_m,rfrx_b, hex(bb1), dcoi1, dcoq1, dcoi2, dcoq2])

                old_pwr = get_pwr
                num += 1

        self.pbus.pbus_workmode()
        logsetlevel("DEBUG")
        self.tester_txdis(tester, device)


    def sweep_rxgain_force_freq(self, cable_att=12, tx_chan=2590, rfrx_en=1, iqv_no=1, name_str='', device="TESTER", fix_pwr=0):
        '''iq_no: 1 means right port, 0 means left port'''

        logsetlevel("ERROR")
        dump_len = 8000
        tx_pwr = -20

        if tx_chan<=14:
            self.wifi.rfchsel(tx_chan)
            tx_freq = self.wifi.chan2freq(tx_chan)+2   #5M Tone
        else:
            self.rfpll.set_freq(tx_chan)
            tx_freq = tx_chan+2

##        self.wifiapi.set_rfrx_dcap()
##        self.i2c.rfrx.rfrx_lna_dcap = 2
##        self.i2c.rfrx.rfrx_vga_dcap = 11
##        self.i2c.bbtop.filter_wifirx0_dgdc = 1
##        self.i2c.rfrx.rfrx_mx_db = 1
        lna_dcap = self.i2c.rfrx.rfrx_lna_dcap
        vga_dcap = self.i2c.rfrx.rfrx_vga_dcap
##        rfrx_mx_db = self.i2c.rfrx.rfrx_mx_db
##        filter_wifirx0_dgdc = self.i2c.bbtop.filter_wifirx0_dgdc

        tester = self.tester_init(tx_freq, tx_pwr, iqv_no, cable_att, device)

        self.pbus.pbus_debugmode()
        num = 0
        rfrx_m = [0x180,0x190,0x1a0,0x1b0,0x1c0,0x1d0,0x1e0,0x1f0]
##        rfrx_m = [0x180,0x1f0]
        tx_pwr_m = [5,-20,-15, -25,-30,-30, 5,0,0, -30,-35,-35, -25, -30,-40, -45, -45, -55, -30, -35, -35, -50,-55, -55]

        bb_m = [0, 0x20, 0x30, 0x32, 0x38]
        bbf = [0,1,2,3,4,5]
        rfrx_f = [0x4,0x6,0xc,0xe]

        if rfrx_en==1:
            gain_m = rfrx_m
            title = 'tx_tone_pwr, rx_pwr, rxdc_i, rxdc_q, rfrx1,rx_gain, rx_noise, bb2, XPD_RFRX_VGA, XPD_RFRX_LNA, RXSW_HG, RXSW_HG_FINE,LNA_DG,VGA_DG_GM,VGA_DG_BUF,VGA_DG_LOAD, bb1, dcoi1, dcoq1, dcoi2, dcoq2, lna_dcap, vga_dcap\n'
        else:
            title = 'tx_tone_pwr, rx_pwr, rxdc_i, rxdc_q, rfrx1,rx_gain, rx_noise, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2, lna_dcap, vga_dcap\n'
            gain_m = bb_m

        fname = self.wifi.get_filename('sweep_rxgain_force', 'sweep_rxgain_force_%d_%d_%s_lna_dcap=%d_vga_dcap=%d'%(tx_chan,rfrx_en, name_str, lna_dcap, vga_dcap))
        fw1=csvreport(fname, title)

        num = 0

        if rfrx_en==1:
            fine_gain_m = rfrx_f
        else:
            fine_gain_m = bbf

        for  gain in gain_m:
            for fine_gain in fine_gain_m:
                if rfrx_en==1:
                    rfrx = gain+fine_gain
                    bb2 = 0
                else:
                    rfrx = 0x184
                    bb2 = (fine_gain<<6)+gain

                self.pbus.pbus_wr('rfrx1', 'en1', rfrx)
                self.pbus.pbus_wr('bb', 'en2', bb2)
                self.pbus.set_dco(0x100, 0x100, 0x100, 0x100)

    ##            if rfrx_en == 0:
                self.mem.wrm(0x600060a0, 17, 16, 3)
                self.wifi.rxdc_cal()

                if fix_pwr==1:
                    tx_pwr = tx_pwr_m[num]
                    self.tester_set_freq(tester, device, tx_freq, tx_pwr, iqv_no)
                else:
                    [tx_pwr, out] = self.get_tx_power(tester, device, tx_freq, tx_pwr, cable_att,iqv_no, dump_len)

                self.tester_set_freq(tester, device, tx_freq, tx_pwr, iqv_no)

                out=self.adc_dump.adcdumptest('null',dump_len,'sw',"10bit",sample_80m=1,plot_en=0)
                print out
                avgi = out[0]
                avgq = out[1]
                rx_pwr = out[2]

                get_pwr = rx_pwr - tx_pwr

                [rfrx1, rftx1, rftx2, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2] = self.pbus.all_pbus()

                rfrx_b = []
                if rfrx_en==1:
                    for i in range(8, 0, -1):
                        rfrx_b.append((rfrx1>>i)&1)

##                self.tester_set_pwr(tester, -120, iqv_no, device)
                self.tester_txdis(tester, device,0)  #IQV
                noise_out=self.adc_dump.adcdumptest('null',dump_len,'sw',"10bit",sample_80m=1,plot_en=0)
                rx_noise = noise_out[3]
                self.tester_txdis(tester, device,1)   #IQV

                fw1.write_data([tx_pwr, rx_pwr, avgi, avgq, hex(rfrx1), get_pwr,rx_noise,  hex(bb2), rfrx_b, hex(bb1), dcoi1, dcoq1, dcoi2, dcoq2,lna_dcap,vga_dcap])

                old_pwr = get_pwr
                num += 1

        logsetlevel("DEBUG")
        self.tester_txdis(tester, device)


    def rx_gain_saturation_test(self, cable_att=12, tx_freq=2484, rxgain_start=6,ragain_end=70,rxpwr_start=-50,rxpwr_end=0, iqv_no=1, name_str='', device="TESTER" ):
        title = 'rx_pwr, rx_gain, lna_sat, vga_sat\n'
        fname = self.wifi.get_filename('rx_gain_saturation_test', 'rx_gain_saturation_test_%d_%s'%(tx_freq, name_str))
        fw1=csvreport(fname, title)
        tx_pwr=-20
        tester = self.tester_init(tx_freq, tx_pwr, iqv_no, cable_att, device)
        for rx_gain in range(rxgain_start,ragain_end):
            for rx_pwr in range(rxpwr_start,rxpwr_end,-1):
                self.tester_set_freq(tester, device, tx_freq, rx_pwr+cable_att, iqv_no)
                self.tester_txdis(tester, device, 1)
                loginfo("rxgain=%d"%rx_gain)
                res=self.adc_dump.adcdumptest(logdir='dump',dump_num=1024,trig_mode='sw',adc_version="10bit",sample_80m=1,plot_en=0,chan_en=1,chan=tx_freq,force_gain_en=1,force_gain=rx_gain)
                vga_sat=res[6]
                lna_sat=res[5]
                fw1.write_data([rx_pwr,rx_gain,lna_sat,vga_sat])
                if vga_sat==0 and lna_sat==0:
                    break

    def rfrx_saturation_test(self, cable_att=12, tx_freq=2484,rxpwr_start=-50,rxpwr_end=0, iqv_no=1, name_str='', device="TESTER" ):
        title = 'rx_pwr, rx_gain, lna_sat, vga_sat\n'
        fname = self.wifi.get_filename('rx_gain_saturation_test', 'rx_gain_saturation_test_%d_%s'%(tx_freq, name_str))
        fw1=csvreport(fname, title)
        tx_pwr=-20
        tester = self.tester_init(tx_freq, tx_pwr, iqv_no, cable_att, device)
        self.pbus.pbus_debugmode()
        for rfrx_b in range(0,0x40):
            rfrx=0x180+(rfrx_b<<1)
            self.pbus.pbus_wr('rfrx1', 'en1', rfrx)
            self.pbus.pbus_wr('bb', 'en2', 0x120)
            self.pbus.set_dco(0x100, 0x100, 0x100, 0x100)

##            if rfrx_en == 0:
            self.mem.wrm(0x600060a0, 17, 16, 3)
            self.wifi.rxdc_cal()
            for rx_pwr in range(rxpwr_start,rxpwr_end,-1):
                self.tester_set_freq(tester, device, tx_freq, rx_pwr+cable_att, iqv_no)
                self.tester_txdis(tester, device, 1)
                loginfo("rfrx1=%s"%hex(rfrx))
                loginfo("rxpower=%d"%rx_pwr)
                res=self.adc_dump.adcdumptest(logdir='dump',dump_num=1024,trig_mode='sw',adc_version="10bit",sample_80m=1,plot_en=0,chan_en=1,chan=tx_freq,force_gain_en=0,force_gain=0)
                vga_sat=res[6]
                lna_sat=res[5]
                fw1.write_data([rx_pwr,hex(rfrx),lna_sat,vga_sat])
                if vga_sat==0 and lna_sat==0:
                    break
        self.pbus.pbus_workmode()

    def bt_rx_gain_check(self,bt_mode=1):
        logsetlevel("I")
        title = 'bt_mode,gain,rfrx1, rftx1, rftx2, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2\n'
        fname = self.wifi.get_filename('bt_rx_gain_check', 'bt_rx_gain_check_%d'%bt_mode)
        csvreport1 = csvreport(fname, title)
        self.wifi.bt_rx_force(bt_mode)
        max_gain = self.wifi.rx_max_gain(bt_mode)
        for gain in range(0,max_gain):
            self.wifi.rx_force_gain(1, gain, bt_mode=bt_mode)
            [rfrx1, rftx1, rftx2, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2] = self.pbus.all_pbus()
            csvreport1.write_data([bt_mode,gain,hex(rfrx1), rftx1, rftx2, hex(bb2), hex(bb1), dcoi1, dcoq1, dcoi2, dcoq2])

        self.wifi.rx_force_gain(0, 0, bt_mode=bt_mode)
        self.wifi.bt_rx_force(0)


    def bt_rx_gain_sweep(self):
        logsetlevel("I")
        title = 'bt_mode,gain,rfrx1, rftx1, rftx2, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2\n'
        fname = self.wifi.get_filename('bt_rx_gain_check', 'bt_rx_gain_check_%d'%bt_mode)
        csvreport1 = csvreport(fname, title)
        self.wifi.bt_rx_force(bt_mode)
        max_gain = self.wifi.rx_max_gain(bt_mode)
        for gain in range(0,max_gain):
            self.wifi.rx_force_gain(1, gain, bt_mode=bt_mode)
            [rfrx1, rftx1, rftx2, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2] = self.pbus.all_pbus()
            csvreport1.write_data([bt_mode,gain,hex(rfrx1), rftx1, rftx2, hex(bb2), hex(bb1), dcoi1, dcoq1, dcoi2, dcoq2])

        self.wifi.rx_force_gain(0, 0, bt_mode=bt_mode)
        self.wifi.bt_rx_force(0)

    def test_chan_rx_lose(self, iqv_no=2):
        logsetlevel("I")
        title = 'chan, bbgain, bbc, bbf, i,rx_pwr,tot_pwr_db,pll_cap\n'
        fname = self.wifi.get_filename('test_chan_rx_lose', 'test_chan_rx_lose')
        csvreport1 = csvreport(fname, title)

        self.pbus.pbus_debugmode()
        self.pbus.pbus_wr('rfrx1','en1', 0x1ae)
        self.pbus.pbus_wr('rftx1','en1', 0x0)
        self.pbus.pbus_wr('rftx2','en1', 0)
        self.pbus.pbus_wr('bb','en1', 0x189)
        self.pbus.pbus_wr('bb','en2', 0)
        self.pbus.pbus_wr('rftx1','en2', 0)

        bbc_m = [0, 0x20, 0x30, 0x32]
        bbf_m = range(0,6,1)
        self.wifiapi.pll_cap_track_en(0)
        dump_len = 4095
        rx_pwr_m = []
        for chan in range(1,15):#chan_m:
            self.wifi.rfchsel(chan, 0)
            for bbi in range(1):
                bbc = bbc_m[bbi/6]
                bbf = bbi%6
                bbgain = bbc + (bbf<<6)

                self.pbus.pbus_wr('bb','en2', bbgain)

                for i in range(2):
                    self.pbus.set_dco(0x100, 0x100, 0x100, 0x100)
                    self.wifi.rxdc_cal()
                    tx_freq = self.wifi.chan2freq(chan)+5
                    tx_pwr = 0

                    mytester=tester.tester(tx_freq,tx_pwr,'tone',100,iqv_no,'cw',0,10, 1,0)
                    result=self.iq_est.get_iqest_power(dump_len)
                    tot_pwr_db=10*np.log10(result[0])
                    out=self.adc_dump.adcdumptest('null',dump_len,'sw',"10bit",sample_80m=1,plot_en=0)
                    rx_pwr = out[3]
                    rx_pwr_m.append(rx_pwr)
                    ir_pll_cap = self.i2c.rfpll.ir_cap_ext
                    mytester.txenable(0)
                    csvreport1.write_data([chan, hex(bbgain), hex(bbc), bbf, i,rx_pwr,tot_pwr_db,ir_pll_cap])
                    loginfo([chan, hex(bbgain), hex(bbc), bbf, i,rx_pwr,tot_pwr_db,ir_pll_cap])

                if rx_pwr > 45:
                    break

        self.pbus.pbus_workmode()

    def test_loop_gain(self):
        logsetlevel("I")
        title = 'chan,rfrx,lna_dcap,atten,bbgain,rx_pwr\n'
        fname = self.wifi.get_filename('test_loop_gain', 'test_loop_gain')
        csvreport1 = csvreport(fname, title)
##        rfrx_m = [0x184,0x186,0x18e,0x192,0x1b2,0x1b8,0x1ce,0x1d0]
##        rftx_m = [0xf,  0x7,  0x3,  0x1,  0x1,  0x0,  0x0,  0x0]
##        atten_m = [24,  24,   24,   24,   24,   24,   60,   80]
        rfrx_m = [0x198,0x19e,0x1c4,0x1ce]
        rftx_m = 0x0
        atten_m = [6,20,6,40]

        for i in range(len(rfrx_m)):
            rfrx = rfrx_m[i]
            rftx = rftx_m
            atten = atten_m[i]
            bbgain = 0x0
            gain_m = []
            for chan in range(1,15,2):
                self.wifi.rfchsel(chan, 0)
                self.wifi.set_loopback_mode(pa_gain=rftx, bbgain=bbgain,loop_case=0)
                self.pbus.pbus_wr('rfrx1','en1', rfrx)
                self.pbus.set_dco(0x100, 0x100, 0x100, 0x100)
                self.wifi.rxdc_cal()
                self.wifi.txtone_step(1,128, atten)
                rx_pwr = self.get_rx_pwr()
                self.pbus.pbus_workmode()
                gain_m.append(rx_pwr)
                self.wifi.txtone_step(0,128,16)
                lna_dcap = self.i2c.rfrx.rfrx_lna_dcap
                csvreport1.write_data([chan,hex(rfrx),lna_dcap,atten,hex(bbgain),rx_pwr])
                loginfo([chan,hex(rfrx),lna_dcap,atten,hex(bbgain),rx_pwr])
##        return gain_m

    def test_lna_dcap(self,cable_lose=1,iqv_no=1):
        chan = 1
        rxgain = 58
        self.wifi.rfchsel(chan, 0)
        self.i2c.bbtop.filter_wfrx0_dcap_hq = 33
        self.i2c.bbtop.filter_wfrx0_dcap_lq = 33
        self.wifi.rx_force_gain(1, rxgain,0)
        tx_freq = self.wifi.chan2freq(chan)+3
        tx_pwr = -rxgain+cable_lose
        mytester=tester.tester(tx_freq,tx_pwr,'tone',100,iqv_no,'cw',0,10, 1,0)
        rx_pwr_m=[]
        for dcap in range(8):
            self.i2c.rfrx.rfrx_lna_dcap = dcap
            rx_pwr = self.get_max_rx_pwr()
            loginfo(dcap,rx_pwr)
            rx_pwr_m.append(rx_pwr)
        return rx_pwr_m

    def get_rx_pwr(self):
        min_pwr = 100
        for i in range(4):
            result=self.wifiapi.get_iq_est_pwr()
            rx_pwr=10*np.log10(int(result,10))
            if rx_pwr < min_pwr:
                min_pwr = rx_pwr
##            loginfo(rx_pwr)
        return min_pwr

    def test_gain_table(self, cable_lose=1,iqv_no=1):
        logsetlevel("I")
        title = 'rxgain,chan,rx_pwr,lna_dcap,rfrx1, rftx1, rftx2, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2\n'
        fname = self.wifi.get_filename('test_gain_table', 'test_gain_table')
        csvreport1 = csvreport(fname, title)
        rx_pwr_m=[]
        rxgain_m = [0,8,12,17,22,26,31,38,46,50,54,58]
##        rxgain_m = [38,58]
        for rxgain in rxgain_m:
            for chan in range(1,15):
                self.wifi.rfchsel(chan, 0)
                self.wifi.rx_force_gain(1, rxgain,0)
                tx_freq = self.wifi.chan2freq(chan)+3
                tx_pwr = -rxgain+cable_lose
                mytester=tester.tester(tx_freq,tx_pwr,'tone',100,iqv_no,'cw',0,10, 1,0)
                rx_pwr = self.get_rx_pwr()
                rx_pwr_m.append(rx_pwr)
                lna_dcap = self.i2c.rfrx.rfrx_lna_dcap
                get_gain = rx_pwr + rxgain
                [rfrx1, rftx1, rftx2, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2] = self.pbus.all_pbus()
                csvreport1.write_data([rxgain,chan,rx_pwr,lna_dcap,hex(rfrx1), rftx1, rftx2, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2])
                loginfo(rxgain,chan,rx_pwr,lna_dcap)
        mytester.txenable(0)
        rx_comp = self.wifi.rx_gain_comp()
        chan_atten = self.wifiapi.tx_chan_atten()
        csvreport1.write_data(['rx_pwr',rx_pwr_m])
        csvreport1.write_data(['rx_gain_comp',rx_comp])
        csvreport1.write_data(['tx_chan_atten',chan_atten])


