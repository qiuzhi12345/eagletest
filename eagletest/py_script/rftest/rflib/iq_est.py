import time
import re
import csv
import math
import os, sys
import matplotlib.pyplot as plt
import pylab
import xlrd
import numpy as np
import pandas
from baselib import plot
from rftest.rflib.utility import mfunc
from baselib.instrument import dm,tester
from baselib.instrument.spa import HP,Agilent
from baselib.instrument import sme
from rftest.rflib.wifi_lib import WIFILIB
from hal.wifi_api import WIFIAPI
from rftest.rflib.adc_dump import DUMP
from hal.Init import HALS
from hal.common import MEM,CHIP_ID
from rftest.rflib.pbus import pbus as Pbus
from rftest.rflib.rfpll import rfpll as RFpll
from rftest.rflib.rfcal import rfcal as RFcal
import rftest.rflib.rfglobal as rfglobal
import rftest.rflib.wifi_instrum as wifi_instrum
from hal.hwregister.hwi2c.all import *
from hal.hwregister.hwpbus.all import *
from rftest.rflib.csv_report import csvreport

class IQ_EST(object):

    def __init__(self,comport,chipv='ESP32'):

        self.comport = comport
        self.chipv = chipv
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.wifiapi = WIFIAPI(self.comport,self.chipv)
        ##self.wifitx = WIFITX(self.comport,self.chipv)
        ##self.wifirx = WIFIRX(self.comport,self.chipv)
        self.mem = MEM(self.comport, self.chipv)
        self.pbus = Pbus(self.comport, self.chipv)
        self.rfpll = RFpll(self.comport, self.chipv)
        self.rfcal = RFcal(self.comport, self.chipv)
        self.chipid = CHIP_ID(self.comport, self.chipv)
##        self.hals = HALS(self.comport,self.chipv)
        self.i2c = HWI2C(self.comport,self.chipv)
        self.hwpbus = HWPBUS(self.comport,self.chipv)
        self.adc_dump = DUMP(self.comport,self.chipv)
        self.curr_data_path = './rftest/rfdata/iq_est/'
        if False==os.path.exists(self.curr_data_path):
            os.mkdir(self.curr_data_path )

    def wait_iqest_done(self):
        if self.chipv=="CHIP722":
            while((self.mem.rdm(0x60006138, 16, 16) == 0)):
                time.sleep(0.1)
        elif self.chipv=="ESP32":
            while((self.mem.rdm(0x6000607c, 31, 31) == 0)):
                time.sleep(0.1)

    def dc_iq_est(self,smp_num):
    ##    self.mem.wrm(0x600060a0, 17, 14, 0xf)  #force txon rxon
        self.tx_rx_clkon()
        #iq_est enable
        self.mem.wrm(0x6000607c, 16, 2, smp_num)  #iqest timmer
        self.iq_est_enable(1)
        self.wait_iqest_done()
        #read est dc
        dc_est_i = self.mem.rd(0x600060dc)
        dc_est_q = self.mem.rd(0x600060e0)
        if(dc_est_i>=(1<<31)):
            dc_est_i = dc_est_i - (1<<32)
        if(dc_est_q>=(1<<31)):
            dc_est_q = dc_est_q - (1<<32)
        dc_est_i = float(dc_est_i >> 6)/smp_num
        dc_est_q = float(dc_est_q >> 6)/smp_num
        power = float(self.mem.rd(0x600060e4)<<2)/smp_num

        self.iq_est_enable(0)
        return [dc_est_i, dc_est_q, power]

    def rx_init(self):

        #self.i2c.bbpll.div_cpu= 1

        self.i2c.bbpll.bbadc_div= 1

        self.i2c.bbpll.bbadc_delay1= 0

        self.i2c.bbpll.bbadc_delay2= 0

        self.i2c.bbpll.bbadc_delay3= 0

        self.i2c.bbpll.bbadc_delay4= 1

        self.i2c.bbpll.bbadc_delay5= 0

        self.i2c.bbpll.bbadc_delay6= 1

        self.i2c.dig_inf.reg_rx_sync_sel= 1

        self.i2c.dig_fe.reg_rx_force_on= 1

        self.mem.wrm(0x60006090, 4, 4, 0)  #disable 80mto40m filter

    def tx_rx_clkon(self,en=1):
        if en==1:
            self.mem.wrm(0x600060a0, 17, 14, 0xf)  #force txon rxon
        else:
            self.mem.wrm(0x600060a0, 17, 14, 0)  #force txon rxon

    def set_tx_dc(self,txdc_i, txdc_q):
        self.mem.wrm(0x600050d0, 9, 0, txdc_i)   #inf txdc_i
        self.mem.wrm(0x600050d0, 19, 10, txdc_q)   #inf txdc_q

    def read_sign(self,addr):
        data = self.mem.rd(addr)
        if(data > 2**31):
            data = data - 2**32
        return data

    def dac_adc_test(self):
        #rfdriver.init()   #tx init
        self.rx_init()     #rx init
        self.tx_rx_clkon()

        self.pbus.pbus_debugmode()
        self.pbus.pbus_wr('rfrx1','en1', 0x0)
        self.pbus.pbus_wr('rftx1','en1', 0x0)
        self.pbus.pbus_wr('rftx2','en1', 0x0)

        self.pbus.pbus_wr('bb','en1', 0x1fc)
        self.pbus.pbus_wr('bb','en2', 0x104)

        self.pbus.pbus_wr('dcoi','en1', 0x100)
        self.pbus.pbus_wr('dcoi','en2', 0x100)
        self.pbus.pbus_wr('dcoq','en1', 0x100)
        self.pbus.pbus_wr('dcoq','en2', 0x100)
        #[idco_c, qdco_c, idco_f, qdco_f] = rfcal.tos()
        self.i2c.bbtop.filter_rx_dlbw=3
        self.i2c.bbtop.filter_tx_dlbw=3


        length = 32
        for bbi in [3]:#range(0, 10):
            if bbi==9:
                bb1 = 0x1fd
                bb2 = 0
            else:
                bb1 = 0x1fc
                bb2 = 1 << bbi
            self.pbus.pbus_wr('bb','en1', bb1)
            self.pbus.pbus_wr('bb','en2', bb2)
            filetime = time.strftime('_%Y%m%d_%H%M%S',time.localtime(time.time()))
            f=open(self.curr_data_path +'dac_adc_test_%d_%s.csv'%(bbi,filetime), 'w')
            f.write("bb1, bb2, txdc_i, txdc_q, dc_est_i, dc_est_q\n")

            for i in range(0, length+1):
                x = i * math.pi*2/length
                y = int(math.sin(x)*400+0.5)
                txdc_i = y
                txdc_q = y
                self.set_tx_dc(txdc_i, txdc_q)

                smp_num = 1024
                [dc_est_i, dc_est_q, power] = dc_iq_est(smp_num)
                f.write(str(bb1)+','+str(bb2)+','+str(txdc_i)+','+str(txdc_q)+','+str(dc_est_i)+','+str(dc_est_q)+'\n')

                print 'dc:%d,%d, %d\n'%(dc_est_i, dc_est_q, i)
            f.close()

    def iqest_snr(self,est_len=4096, rms_sel=0):
        self.tx_rx_clkon(1)

        self.mem.wrm(0x600060b8, 21, 21, 1) #dis_phase
        self.mem.wrm(0x600060b8, 29, 29, 1) #enable tone_v7

        self.mem.wrm(0x60006060, 27, 26, 1) #iqest clk: 0-106m, 1-80m
        self.mem.wrm(0x6000607c, 20, 19, 2)
        #iq_est enable
        self.mem.wrm(0x6000607c, 16, 2, est_len-1)  #iqest timmer
        self.iq_est_enable(1)

        self.wait_iqest_done()
        if rms_sel==0:
            cw_rms1 = 511.4607
            cw_rms2 = 511.5104
        else:
            cw_rms1 = 511.5036
            cw_rms2 = 511.4963

        tot_power_reg = self.mem.rd(0x600060e4)
        i_power_reg = self.mem.rd(0x600060ec)
        q_power_reg = self.mem.rd(0x600060f0)
        dc_i_reg = self.read_sign(0x600060dc)
        dc_q_reg = self.read_sign(0x600060e0)
        result_1 = self.read_sign(0x60006080)
        result_2 = self.read_sign(0x60006084)
        result_3 = self.read_sign(0x60006088)
        result_4 = self.read_sign(0x6000608c)

        result2_1 = self.read_sign(0x600060cc)
        result2_2 = self.read_sign(0x600060d0)
        result2_3 = self.read_sign(0x600060d4)
        result2_4 = self.read_sign(0x600060d8)
        print 'read_reg:  %d, %d, %d, %d, %d, %d, %d, %d, %d'%(tot_power_reg,i_power_reg,q_power_reg,dc_i_reg,dc_q_reg,result_1, result_2, result_3, result_4)
        #iq_est disable
        self.iq_est_enable(0)

        tot_power = tot_power_reg*8.0 / est_len
        i_power = i_power_reg*4.0 / est_len
        q_power = q_power_reg*4.0 / est_len
        dc_i = dc_i_reg*4.0 / 2**8 / est_len
        dc_q = dc_q_reg*4.0 / 2**8 / est_len

        result1 = (result_1)*4.0 / est_len / cw_rms1
        result2 = (result_2)*4.0 / est_len / cw_rms1
        result3 = (result_3)*4.0 / est_len / cw_rms1
        result4 = (result_4)*4.0 / est_len / cw_rms1

        result21 = (result2_1)*4.0 / est_len / cw_rms2
        result22 = (result2_2)*4.0 / est_len / cw_rms2
        result23 = (result2_3)*4.0 / est_len / cw_rms2
        result24 = (result2_4)*4.0 / est_len / cw_rms2

        print 'sig_reg: %2.2f, %2.2f, %2.2f, %2.2f'%(result1, result2, result3, result4)
        print 'sig2_reg: %2.2f, %2.2f, %2.2f, %2.2f'%(result21, result22, result23, result24)
        #signal


        sig_i = result1 + result4
        sig_q = result2 - result3
        #iq mismatch
        sig_i1 = result1 - result4
        sig_q1 = result2 + result3
        phase_i1 = np.arctan(result1/result2)
        phase_q1 = np.arctan(-result4/result3)
        delta_phase1 = phase_i1 - phase_q1

        print 'dc: %2.2f, %2.2f, sig: %2.2f, %2.2f, %2.2f, %2.2f'%(dc_i, dc_q,sig_i, sig_q, sig_i1, sig_q1)
        sig_power = sig_i**2 + sig_q**2 + sig_i1**2 + sig_q1**2


        sig2_i = result21 + result24
        sig2_q = result22 - result23
        #iq mismatch
        sig2_i1 = result21 - result24
        sig2_q1 = result22 + result23
        sig2_power = sig2_i**2 + sig2_q**2 + sig2_i1**2 + sig2_q1**2

        dc_power = dc_i**2 + dc_q**2
        noise_power = tot_power - sig_power - dc_power - sig2_power
        n_p = noise_power
        if n_p<=0:
            n_p=0.1
        x = sig_power/n_p
        snr = 10*np.log10(x)
        print 'snr=%2.2f, tot_p=%2.2f, sig_p=%2.2f, sig2_p=%2.2f, dc_p=%2.2f, n_p=%2.2f'%(snr, tot_power, sig_power, sig2_power, dc_power, noise_power)

        sigi_power = (result1**2 + result3**2)*2
        sig2i_power = (result21**2 + result23**2)*2
        dci_power = dc_i**2
        noisei_power = i_power - sigi_power - dci_power- sig2i_power
        n_p = noisei_power
        if n_p<=0:
            n_p=0.01
        snr_i = 10*np.log10(sigi_power/n_p)
        print 'snr_i=%2.2f, toti_p=%2.2f, sigi_p=%2.2f, sigi_amp=%2.2f, sig2i_p=%2.2f, dci_p=%2.2f, ni_p=%2.2f'%(snr_i, i_power, sigi_power, np.sqrt(sigi_power), sig2i_power, dci_power, noisei_power)

        sigq_power = (result2**2 + result4**2)*2
        sig2q_power = (result22**2 + result24**2)*2
        dcq_power = dc_q**2
        noiseq_power = q_power - sigq_power - dcq_power - sig2q_power
        n_p = noiseq_power
        if n_p<=0:
            n_p=0.01
        snr_q = 10*np.log10(sigq_power/n_p)
        print 'snr_q=%2.2f, totq_p=%2.2f, sigq_p=%2.2f, sigq_amp=%2.2f, sig2q_p=%2.2f, dcq_p=%2.2f, nq_p=%2.2f'%(snr_q, q_power, sigq_power,np.sqrt(sigq_power), sig2q_power, dcq_power, noiseq_power)


        x_1 = np.sqrt(sigi_power/sigq_power) - 1
        y_1 = np.sin(phase_i1)-np.sin(phase_q1)
        evm = 20*np.log10((np.sqrt(x_1**2 + y_1**2))/2)

        con2dbm= 10*np.log10((1.1**2)/50/2*1000)
        sigi_power_dbm = 10*np.log10(sigi_power/((511**2)/2)) + con2dbm
        sigq_power_dbm = 10*np.log10(sigq_power/((511**2)/2)) + con2dbm
        print 'sigi_power=%2.2f, sigq_power=%2.2f, phase_i1=%2.2f, phase_q1=%2.2f, delta_phase1=%2.2f,x_1=%2.2f,y_1=%2.2f,evm=%2.2f'%(sigi_power, sigq_power, phase_i1, phase_q1, delta_phase1,x_1,y_1,evm)
        print 'sigi_power_dbm=%2.2f, sigq_power_dbm=%2.2f'%(sigi_power, sigq_power)

        #return [snr,tot_power_reg,i_power_reg,q_power_reg,dc_i_reg,dc_q_reg,result_1, result_2, result_3, result_4]
        return [snr, sigi_power, sigq_power, phase_i1, phase_q1, delta_phase1,evm]


    def iqest_snr_10times(self,est_len=4096,atten=240, mode=0):
        filetime = time.strftime('_%Y%m%d_%H%M%S',time.localtime(time.time()))
        f=open(self.curr_data_path +'sweep_iqest_snr_%s.csv'%filetime, 'w')
        f.write("snr,tot_power,i_power,q_power,dc_i,dc_q,result_1, result_2, result_3, result_4\n")
        result1=[]
        result2=[]
        result3=[]
        result4=[]
        for i in range(1,10):
            [snr,tot_power,i_power,q_power,dc_i,dc_q,result_1, result_2, result_3, result_4] = self.iqest_snr(est_len,atten, mode)
            f.write(str(snr)+','+str(tot_power)+','+str(i_power)+','+str(q_power)+','+str(dc_i)+','+str(dc_q)+','+str(result_1)+','+str(result_2)+','+str(result_3)+','+str(result_4)+'\n')
            result1.append(result_1)
            result2.append(result_2)
            result3.append(result_3)
            result4.append(result_4)
        print '**********************************************************************************************'
        result1_avg=np.average(result1)
        result2_avg=np.average(result2)
        result3_avg=np.average(result3)
        result4_avg=np.average(result4)
        f.close()
        return [result1_avg,result2_avg,result3_avg,result4_avg]

    def iqest_snr_compara(self,tx_dc_i_1=0,tx_dc_q_1=0,tx_dc_i_2=0,tx_dc_q_2=0,est_len=8192):
        tx_dc_i = tx_dc_i_1
        tx_dc_q = tx_dc_q_1
        self.set_tx_dc(tx_dc_i,tx_dc_q)
        [result1_avg_1,result2_avg_1,result3_avg_1,result4_avg_1] = iqest_snr_10times('dc_i='+str(tx_dc_i)+'_dc_q='+str(tx_dc_q),est_len)
        tx_dc_i = tx_dc_i_2
        tx_dc_q = tx_dc_q_2
        self.set_tx_dc(tx_dc_i,tx_dc_q)
        [result1_avg_2,result2_avg_2,result3_avg_2,result4_avg_2] = self.iqest_snr_10times('dc_i='+str(tx_dc_i)+'_dc_q='+str(tx_dc_q),est_len)
        result1_diff_reg = result1_avg_1 - result1_avg_2
        result2_diff_reg = result2_avg_1 - result2_avg_2
        result3_diff_reg = result3_avg_1 - result3_avg_2
        result4_diff_reg = result4_avg_1 - result4_avg_2

        result1_diff = result1_diff_reg*4/est_len/0.2441
        result2_diff = result2_diff_reg*4/est_len/0.2441
        result3_diff = result3_diff_reg*4/est_len/0.2441
        result4_diff = result4_diff_reg*4/est_len/0.2441
        return [result1_diff,result2_diff,result3_diff,result4_diff]

    def loopback_mode_set(self, pagain=0xf, bbgain=0x20, loop_case=0):
        self.wifi.stoptone()
##        self.mem.wrm(0x600060a0, 17, 14, 0xf)  #force txon rxon
        self.tx_rx_clkon(1)
        self.pbus.pbus_debugmode()
        self.mem.wrm(0x6000607c, 30, 30, 0)  #fe loopback en

        self.mem.wrm(0x600050dc, 11, 11, 0) #txiq disable
        self.mem.wrm(0x600050dc, 27, 27, 0) #rxiq disable

        if loop_case == 2: #digital interface loop
            self.mem.wrm(0x600050d0, 28, 28, 1)  #ana inf loopback en
            self.mem.wrm(0x600050d8, 25, 25, 0)  #tx iq swap
        elif loop_case == 1: # dac, filt, adc loop
            self.mem.wrm(0x600050d0, 28, 28, 0)  #ana inf loopback en
            self.mem.wrm(0x600050d8, 25, 25, 0)  #tx iq swap
            # dac,flt,adc
            self.hwpbus.RFRX1.EN1 = 0x001
            self.hwpbus.RFTX1.EN1 = 0x000
            self.hwpbus.RFTX2.EN1 = 0x000
            self.hwpbus.BB1.EN1   = 0x100
            self.hwpbus.BB1.EN1   = 0x1c9
            self.hwpbus.BB1.EN2   = bbgain
            self.i2c.bbtop.enlb = 0
        else: # rf loopback
            self.mem.wrm(0x600050d0, 28, 28, 0)  #ana inf loopback en
            self.mem.wrm(0x600050d8, 25, 25, 1)  #tx iq swap
            self.hwpbus.RFRX1.EN1 = 0x104
            self.hwpbus.RFTX1.EN1 = 0x7f
            self.hwpbus.RFTX2.EN1 = pagain
            self.hwpbus.BB1.EN1   = 0x1f9
            self.hwpbus.BB1.EN2   = bbgain
            self.i2c.bbtop.enlb    = 1
            self.i2c.rfrx.LB_MODE  = 1
            self.i2c.rftx.LB_EN    = 1
            self.i2c.rftx.LB_EN_IQ = 1
            self.i2c.rftx.LB_GCT   = 1

        self.pbus.set_dco(0x100, 0x100, 0x100, 0x100)
        self.wifi.rxdc_cal()


    def loopback_snr(self, pagain=0xf, bbgain=0x20, tone_att=20, tone_step=64, loop_case=0, rms_sel=0):
##        self.loopback_mode_set(pagain, bbgain, loop_case)
##        self.i2c.bbtop.filter_rx_dlbw=3
##        self.i2c.bbtop.filter_tx_dlbw=3
        if tone_att<0:
            tone_att += 256
        self.wifi.txtone_step(1, 16, tone_att, 1,14, tone_att)
        self.iqest_snr(est_len=2**12, rms_sel=rms_sel)


    def tsen(self):
        self.i2c.SARADC.en_vco= 1

        self.i2c.SARADC.xpd_tsens= 1

        #self.mem.wrm(0x60000D50, 15, 8, 80) #lower temperature sensor clock to 1MHz
        self.mem.wrm(0x60000d50,5,5,0)  #sar_clk_gate
        self.mem.wrm(0x60000d5c,21,21,1)  #use_tempsensor

        self.i2c.SARADC.dump_out= 0

        self.i2c.SARADC.dump_out= 1

        temp = self.i2c.SARADC.temp

        print 'temp_code=0x%x'%temp
        self.i2c.SARADC.dump_out= 0

        self.i2c.SARADC.dump_out= 1

        temp = self.i2c.SARADC.temp

        print 'temp_code=0x%x'%temp
        self.i2c.SARADC.dump_out= 0

        self.i2c.SARADC.dump_out= 1

        temp = self.i2c.SARADC.temp

        print 'temp_code=0x%x'%temp
        return temp

    def get_iqest_power(self,est_len):
        #iq_est enable
        self.tx_rx_clkon()
        self.mem.wrm(0x60006060, 27, 26, 1) #iqest clk is 80m
        self.mem.wrm(0x6000607c, 20, 19, 2) #select cw2 to corr

        self.mem.wrm(0x6000607c, 16, 2, est_len)  #iqest timmer
        self.iq_est_enable(1)

        self.wait_iqest_done()

        cw_rms = 511.503354
        tot_power = self.mem.rd(0x600060e4)
        tot_power = float(tot_power)*8 / est_len
        i_power = self.mem.rd(0x600060ec)
        q_power = self.mem.rd(0x600060f0)
        i_power = float(i_power)*4 / est_len
        q_power = float(q_power)*4 / est_len
        dc_i = self.read_sign(0x600060dc)
        dc_q = self.read_sign(0x600060e0)
        dc_i = float(dc_i) / 2**6 / est_len  #8-2
        dc_q = float(dc_q) / 2**6 / est_len  #8-2
        dc_power = dc_i**2 + dc_q**2

        result1 = self.read_sign(0x60006080)
        result2 = self.read_sign(0x60006084)
        result3 = self.read_sign(0x60006088)
        result4 = self.read_sign(0x6000608c)
        result1 = (float(result1)*4 - est_len * dc_i * 2000/8192)/4
        result2 = (float(result2)*4 - est_len * dc_q * 2000/8192)/4
        result3 = (float(result3)*4 - est_len * dc_i * 2000/8192)/4
        result4 = (float(result4)*4 - est_len * dc_q * 2000/8192)/4
        result1 = float(result1)*4 / est_len / cw_rms
        result2 = float(result2)*4 / est_len / cw_rms
        result3 = float(result3)*4 / est_len / cw_rms
        result4 = float(result4)*4 / est_len / cw_rms
        sig_i = result1 + result4
        sig_q = result2 - result3
        #iq mismatch
        sig_i1 = result1 - result4
        sig_q1 = result2 + result3
        sig1_power = sig_i**2 + sig_q**2 + sig_i1**2 + sig_q1**2

        result1 = self.read_sign(0x600060cc)
        result2 = self.read_sign(0x600060d0)
        result3 = self.read_sign(0x600060d4)
        result4 = self.read_sign(0x600060d8)
        result1 = (float(result1)*4 - est_len * dc_i * 2000/8192)/4
        result2 = (float(result2)*4 - est_len * dc_q * 2000/8192)/4
        result3 = (float(result3)*4 - est_len * dc_i * 2000/8192)/4
        result4 = (float(result4)*4 - est_len * dc_q * 2000/8192)/4
        result1 = float(result1)*4 / est_len / cw_rms
        result2 = float(result2)*4 / est_len / cw_rms
        result3 = float(result3)*4 / est_len / cw_rms
        result4 = float(result4)*4 / est_len / cw_rms
        sig_i = result1 + result4
        sig_q = result2 - result3
        #iq mismatch
        sig_i1 = result1 - result4
        sig_q1 = result2 + result3
        sig2_power = sig_i**2 + sig_q**2 + sig_i1**2 + sig_q1**2

        #iq_est disable
        self.iq_est_enable(0)
##        print '%2.2f, %2.2f, %2.2f, %2.2f, %2.2f, %2.2f'%(tot_power, dc_i, dc_q, dc_power, sig1_power, sig2_power)
##        print 'tot_pwr=%d, i_pwr=%d, q_pwr=%d, i_amp=%d, q_amp=%d'%(tot_power, i_power, q_power, np.sqrt(i_power), np.sqrt(q_power))

        return [tot_power, i_power, q_power, np.sqrt(i_power), np.sqrt(q_power)]

    def noise_sweep(self,est_len=2**14, instr=''):
        self.wifi.stoptone(0)
        self.tx_rx_clkon()
        self.mem.wrm(0x600060b8, 29, 29, 1) #enable tone_v7
        self.mem.wrm(0x60006060, 27, 26, 0) #iqest clk is 160m
        #tx tone3
        self.mem.wrm(0x600060c4, 21, 21, 1) #dis_phase
        atten = 0
        step = 1
        self.mem.wrm(0x600060c4, 17, 10, atten)  #tone atten
        self.mem.wrm(0x600060c4, 9, 0, step >> 2) #tx tone step[11:2]
        self.mem.wrm(0x600050a8, 5, 4, step & 0x3)  #tx tone step[1:0]
        self.mem.wrm(0x600060c4, 18, 18, 1) #tone_en
        filetime = time.strftime('_%Y%m%d_%H%M%S',time.localtime(time.time()))
        f=open(self.curr_data_path +'noise_sweep_%s.csv'%(filetime), 'w')
        f.write("step, tot_power, dc_i, dc_q, dc_power, sig1_power, sig2_power\n")

        for step in range(1, 129):
            self.mem.wrm(0x600060c4, 9, 0, step >> 2) #tx tone step[11:2]
            self.mem.wrm(0x600050a8, 5, 4, step & 0x3)  #tx tone step[1:0]
            time.sleep(0.01)
            [tot_power, dc_i, dc_q, dc_power, sig1_power, sig2_power] = self.get_iqest_power(est_len)
            f.write(str(step)+','+str(tot_power)+','+str(dc_i)+','+str(dc_q)+','+str(dc_power)+','+str(sig1_power)+','+str(sig2_power)+'\n')

            print 'step=%d'%(step)

        f.close()
        self.wifi.stoptone(0)

    def ajust_iqmismatch(self,tx_q_i=11,tx_q_q=6):
        self.i2c.DIG_INF.tx_iqcorr_enable=1     #iq mismatch

        self.i2c.DIG_INF.tx_q_i_coff= 64-tx_q_i            #[-31, 31]

        self.i2c.DIG_INF.tx_q_q_coff= tx_q_q         #[-15, 15]


    def set_tx_reg_opt(self,pll_freq=5400):
        self.pbus.pbus_test.self.pbus.pbus_debugmode();
    #    adcTest.bb_init('TX')
##        rfdriver.init()
##        rftx.init();
        self.i2c.BIAS.cp1p1_pvt_reg=0x03


        self.rfpll.set_freq_outband(pll_freq/2);

        self.pbus.pbus_wr('bb', 'en2', 0x18)
        self.rfcal.tos();

        self.i2c.BIAS.cp1p6_dreg=3;

        self.i2c.BIAS.cgm_bias=3;


        self.i2c.bbtop.filter_tx_bstb=3;

        self.i2c.BIAS.dres12k=0;

        self.i2c.BIAS.dres12k_force_on=1;


        self.i2c.RFTX.PA_VCT_CSC_STG0=0x6;

        self.i2c.RFTX.PA_VCT_CSC_STG1=0x3;

        self.i2c.RFTX.PA_ICT_STG0=0xa;

        self.i2c.RFTX.PA_ICT_STG1=0x3;


        self.i2c.DIG_INF.reg_tx_sync_sel= 1





    def txtone_inf(self,en=1, freq1_mhz=2, atten=240):
        #tx_rx_clkon()
        self.i2c.DIG_INF.tx_tone_start= en & 1

        self.i2c.DIG_INF.analog_txtone_en= en & 1

        self.i2c.DIG_INF.reg_tx_in_rate_sel= en & 1

        self.i2c.DIG_INF.dac_160m_enable= en & 1   #dac_320_enable

        if en==1:
            self.i2c.DIG_INF.tx_scale=  atten

        else:
            self.i2c.DIG_INF.tx_scale=  0


        self.i2c.DIG_INF.reg_cw_gen_sel= 1


        cpu_320 = self.i2c.bbpll.div_cpu

        if cpu_320==1:
            freq1=int(1000*freq1_mhz/2)*2;
        else:
            freq1=int(1000*freq1_mhz)*2;
        freq1 = (freq1 *64/5000) & 0xfff
        self.i2c.DIG_INF.reg_inf_fstep_11_8= freq1 >> 8

        self.i2c.DIG_INF.reg_inf_fstep_7_0= freq1 & 0xff


    def max_min(self,arry):
        #find the max value and min value of the arry
        length=len(arry);
        max_value=arry[0]
        min_value=arry[0]
        for i in range(0,length):
            if max_value<arry[i]:
                max_value=arry[i]
            if min_value>arry[i]:
                min_value=arry[i]
        return [max_value,min_value,max_value-min_value]

    def v2power(self,arry):
        length=len(arry);
        power=0
        DC=0

        for num in range(0,length):
            DC=DC+arry[num];

        avg_dc=DC/length

        for i in range(0,length):
            power=power+(arry[i]-avg_dc)*(arry[i]-avg_dc)

        return float(power)/length

    def power_w2dBm(self,arry):
        length=len(arry)
        for num in range(0,length):
            arry[num]=10*math.log10(float(arry[num]))

        return arry

    def rx_regset(self,lna_dboost_1=0,lna_dcap_31=21,vga_dcap_31=28,incap2_15=5,incap1_15=9,mx_db_3=3):
        self.i2c.RFRX.rfrx_lna_dboost=lna_dboost_1

        self.i2c.RFRX.rfrx_lna_dcap=lna_dcap_31

        self.i2c.RFRX.rfrx_vga_dcap=vga_dcap_31

        self.i2c.RFRX.lna_incap2=incap2_15

        self.i2c.RFRX.lna_incap1=incap1_15

        self.i2c.RFRX.rfrx_mx_db=mx_db_3


    def Sig_Gen(self,Enable=1,Freq_MHz=5401,Power_dBm=-80):
        mysig_gen = sme.sme();
        mysig_gen.rfoff();
        mysig_gen.setfreq(Freq_MHz*1e6)
        mysig_gen.setpow(Power_dBm)
        if Enable==1:
            mysig_gen.rfon();
            print 'Signal Generater Turn On OK!'
        if Enable==0:
            mysig_gen.rfoff();
            print 'Signal Generater Turn Off OK!'

    def tone_corr(self,est_len):
        [tot_power, dc_i, dc_q, dc_power, sig1_power, sig2_power] = get_iqest_power(est_len)
        #print 'tot=%d, dci=%d, dcq=%d, dcp=%d, sig1=%d, sig2=%d'%(tot_power, dc_i, dc_q, dc_power, sig1_power, sig2_power)
        #tx tone3
        '''
        tone_step=int(freq*4096/160)
        print 'tone_step=%d'%tone_step
        if (tone_step&0x1!=0x1):
            tone_step=tone_step+1
        self.mem.wrm(0x600060b8, 29, 29, 1) #enable tone_v7
        self.mem.wrm(0x600060c4, 21, 21, 1) #dis_phase
        self.mem.wrm(0x600060c4, 9, 0, tone_step >> 2) #tx tone step[11:2]
        self.mem.wrm(0x600050a8, 5, 4, tone_step & 0x3)  #tx tone step[1:0]
        self.mem.wrm(0x600060c4, 18, 18, 1) #tone_en
        '''
        self.mem.wrm(0x600060c4, 28, 28, 1) #im3_en
        [tot_power, dc_i, dc_q, dc_power, sig1_power, sig3_power] = self.get_iqest_power(est_len)
        #print 'tot=%d, dci=%d, dcq=%d, dcp=%d, sig1=%d, sig3=%d'%(tot_power, dc_i, dc_q, dc_power, sig1_power, sig3_power)
        pwr_db = 10*math.log10(tot_power)
        sig1_db = 10*math.log10(sig1_power)
        sig2_db = 10*math.log10(sig2_power)
        sig3_db = 10*math.log10(sig3_power)
        print 'tot=%ddB, sig1=%d, sig2=%d, sig3=%d'%(pwr_db, sig1_db, sig2_db, sig3_db)
        self.mem.wrm(0x600060c4, 28, 28, 0) #im3_en
        return [pwr_db, sig1_db, sig2_db, sig3_db]

    def iq_est_enable(self,en=1):
        if en==1:
            self.mem.wrm(0x6000607c, 0, 0, 1)  #clk en
            time.sleep(0.01)
            self.mem.wrm(0x6000607c, 1, 1, 1)  #iq est en,
        else:
            self.mem.wrm(0x6000607c, 1, 1, 0)  #iq est en,
            time.sleep(0.01)
            self.mem.wrm(0x6000607c, 0, 0, 0)  #clk en


    def iq_est_simple(self,freq=2, att=-80, est_len=2**10, mode=0):
    ##    wifi.tx_tone1(1, freq, att)
    ##    self.mem.wrm(0x600060a0, 17, 14, 0xf)  #force txon rxon
    ##    if mode==0:
    ##        self.mem.wrm(0x600050d0, 28, 28, 1)  #ana inf loopback en
    ##        self.mem.wrm(0x6000607c, 30, 30, 0)  #fe loopback en
    ##    elif mode==1:
    ##        self.mem.wrm(0x6000607c, 30, 30, 1)  #fe loopback en
    ##        self.mem.wrm(0x600050d0, 28, 28, 0)  #ana inf loopback en
        self.mem.wrm(0x6000607c, 16, 2, est_len)  #iqest timmer
        self.iq_est_enable(1)

        self.wait_iqest_done()

        cw_rms = 511.503354
        tot_power = self.mem.rd(0x600060e4)
        tot_power = float(tot_power)*8 / est_len
        i_power = self.mem.rd(0x600060ec)
        q_power = self.mem.rd(0x600060f0)
        i_power = float(i_power)*4 / est_len
        q_power = float(q_power)*4 / est_len
        dc_i = self.read_sign(0x600060dc)
        dc_q = self.read_sign(0x600060e0)
        dc_i = float(dc_i) / 2**6 / est_len  #8-2
        dc_q = float(dc_q) / 2**6 / est_len  #8-2
        dc_power = dc_i**2 + dc_q**2

        self.iq_est_enable(0)
    ##    wifi.tx_tone1(0, freq, att)
        print '%2.2f, %2.2f, %2.2f, %2.2f, %2.2f, %2.2f'%(tot_power, dc_i, dc_q, i_power, q_power, np.sqrt(tot_power))
        return [np.sqrt(tot_power), dc_i, dc_q]

    def loopback_test(self,freq=2, att=24, est_len=2**10,bb=0x80, rftx2=0x3, btmode=0):
    ##    wifi.tx_tone1(1, freq, att)
##        wifi.txtone_step(1, 128, att, 0, 0, 0)
##        self.wifi.txtone_step(1, 16, att, 1, 14, att)
        self.wifi.txtone(0, freq, att)
        self.mem.wrm(0x600060a0, 17, 14, 0xf)  #force txon rxon
        self.pbus.pbus_debugmode()
        self.mem.wrm(0x6000607c, 30, 30, 0)  #fe loopback en
        self.mem.wrm(0x600050d0, 28, 28, 0)  #ana inf loopback en

        # dac,flt,adc
        self.hwpbus.RFRX1.EN1 = 0x001
        self.hwpbus.RFTX1.EN1 = 0x000
        self.hwpbus.RFTX2.EN1 = 0x000
        self.hwpbus.BB1.EN1   = 0x100
        self.hwpbus.BB1.EN1   = 0x1c9
        self.hwpbus.BB1.EN2   = 0x030
        self.i2c.bbtop.enlb = 0
        self.mem.wrm(0x600050dc, 11, 11, 0) #txiq disable
        self.mem.wrm(0x600050dc, 27, 27, 0) #rxiq disable

        self.pbus.set_dco(0x100, 0x100, 0x100, 0x100)
        self.mem.wrm(0x600060a0, 17, 16, 3)
        self.wifi.rxdc_cal()

        self.wifi.txtone(1, freq, att)
##        self.i2c.bbtop.enlb=1
##        self.pbus.pbus_wr('rfrx1', 'en1', 0x104)
##        self.pbus.pbus_wr('rftx1', 'en1', 0x7f)
##        self.pbus.pbus_wr('rftx2', 'en1', rftx2)
##        if btmode==0:
##            self.pbus.pbus_wr("bb","en1",0x1f9)
##        else:
##            self.pbus.pbus_wr("bb","en1",0x1fb)
##        self.pbus.pbus_wr("bb","en2",bb)
##        self.pbus.set_dco(0x100, 0x100, 0x100, 0x100)
    ##    self.pbus.pbus_test.self.pbus.pbus_dco_way2()
##        self.wifi.rxdc_cal()

        self.mem.wrm(0x6000607c, 16, 2, est_len)  #iqest timmer
        self.iq_est_enable(1)

        self.wait_iqest_done()

        cw_rms = 511.503354
        tot_power = self.mem.rd(0x600060e4)
        tot_power = float(tot_power)*8 / est_len
        i_power = self.mem.rd(0x600060ec)
        q_power = self.mem.rd(0x600060f0)
        i_power = float(i_power)*4 / est_len
        q_power = float(q_power)*4 / est_len
        dc_i = self.read_sign(0x600060dc)
        dc_q = self.read_sign(0x600060e0)
        dc_i = float(dc_i) / 2**6 / est_len  #8-2
        dc_q = float(dc_q) / 2**6 / est_len  #8-2
        dc_power = dc_i**2 + dc_q**2

        self.iq_est_enable(0)
    ##    wifi.tx_tone1(0, freq, att)
        print '%2.2f, %2.2f, %2.2f, min=%2.2f, max=%2.2f, %2.2f'%(tot_power, dc_i, dc_q, 1<<12, 1<<18, np.sqrt(tot_power))

    def test_rxdc(self):
        rfrx = [0x184, 0x1a4, 0x1a6, 0x1ac, 0x1ae, 0x1bc, 0x1be, 0x1c6, 0x1cc, 0x1ce, 0x1d6, 0x1dc, 0x1de]
        num = len(rfrx)
        bb = 0xf8
        filetime = time.strftime('_%Y%m%d_%H%M%S',time.localtime(time.time()))
        f=open(self.curr_data_path +'rxdc_debug_%s.csv'%filetime, 'w')
        f.write("rfrx, bb2, bbc1, bbc2, bbf, dci_c, dcq_c, dci_f, dcq_f\n")

        self.mem.wrm(0x6001c02c, 31, 23, ((70<<1)|1)); #force gain
        self.pbus.pbus_debugmode()
        for i in range(0, num):
            rfrx1=rfrx[i]
            print 'rfrx1=0x%x'%rfrx1
            self.pbus.pbus_wr('rfrx1', 'en1', rfrx1)
            bbg_c = 0
            for bbc in range(2, 3):
                bbg_c += 1<<(5-bbc)
                for bbf in range(2, 3):
                   bb2 = (bbf << 6) + bbg_c
                   self.pbus.pbus_wr('bb', 'en2', bb2)
                   rxdc = self.wifi.rxdc_cal()
                   rxdc = rxdc.replace(':', ',').replace(' ', ',')
                   rxdc = rxdc.split(',')
                   print rxdc

                   w_str = '0x%x, 0x%x, 0x%x, %d, %d'%(rfrx1, bb2, bbg_c, bbc, bbf)+','+rxdc[2]+','+rxdc[3]+','+rxdc[4]+','+rxdc[5]+'\n'
                   f.write(w_str)

    def test_rxdc_remain(self):
        rfrx = [0x184, 0x1a4, 0x1a6, 0x1ac, 0x1ae, 0x1bc, 0x1be, 0x1c6, 0x1cc, 0x1ce, 0x1d4, 0x1d6, 0x1dc, 0x1de]
        num = len(rfrx)
        filetime = time.strftime('_%Y%m%d_%H%M%S',time.localtime(time.time()))
        f=open(self.curr_data_path +'rxdc_debug_%s.csv'%filetime, 'w')
        f.write("rfrx, bb2, bbc1, bbc2, bbf, dc_i, dc_q\n")

        self.pbus.pbus_debugmode()
        self.pbus.open_rx()
    ##    self.pbus.pbus_wr('bb', 'en1', 0x18b)
        bbg_c = 0
        for bbc in range(0, 3):
            bbg_c += 1<<(6-bbc)
            bbg_c &= 0x3f
            ##bbg_c = 0x3c
            for i in range(0, num):
                rfrx1=rfrx[i]
                bbf = 0
                bb2 = (bbf << 6) + bbg_c
                print 'rfrx1=0x%x'%rfrx1
                self.pbus.pbus_wr('rfrx1', 'en1', rfrx1)
                self.pbus.pbus_wr('bb', 'en2', bb2)
                for k in range(0, 1):
                    dc1 = 0x100+(k==1)*10
                    dc2 = 0x100+(k==2)*10
                    dc3 = 0x100+(k==3)*10
                    dc4 = 0x100+(k==4)*10
                    self.pbus.set_dco(dc1, dc2, dc3, dc4)
                    [a, dc_i, dc_q] = iq_est_simple(est_len=2**14)
                    w_str = '0x%x, 0x%x, 0x%x, %d, %d, %d, %d, , %d, %d, %d, %d'%(rfrx1, bb2, bbg_c, bbc, bbf, dc_i, dc_q, dc1, dc2, dc3, dc4)+'\n'
                    f.write(w_str)

    def test_rxiq(self):
        chan = 1
        freq = 2412
        tone_freq = freq+5
        sme06 = sme.sme()
        sme06.setfreq(tone_freq*1e6)
        sme06.rfoff()

        rfrx = [0x184, 0x1a4, 0x1a6, 0x1ac, 0x1ae, 0x1bc, 0x1be, 0x1c6, 0x1cc, 0x1ce, 0x1d4, 0x1d6, 0x1dc, 0x1de]
        bbc = [0x0, 0x20, 0x30, 0x38, 0x3c, 0x3e]
        num = len(rfrx)
        num1 = len(bbc)
        filetime = time.strftime('_%Y%m%d_%H%M%S',time.localtime(time.time()))
        f=open(self.curr_data_path +'test_rxiq_%s.csv'%filetime, 'w')
        f.write(", , rfrx1, bb2, power, sig_amp, dc_i, dc_q, , iq_gain1, iq_phase1, iq_gain2, iq_phase2, iq_gain_sum, iq_phase_sum, power, freq_offset, snr\n")

        self.pbus.pbus_debugmode()
        self.pbus.open_rx()
        for i in range(0, 2):
            if i==0:
                num = len(rfrx)
            else:
                num = 36  #len(bbc)
            power = -20
            for j in range(0, num):
                self.wifi.rfchsel(chan)
                sme06.rfoff()
                if i==0:
                    rfrx1=rfrx[j]
                    bb2 = 0 #bbc[1]
                else:
                    rfrx1=rfrx[0]
                    bb2 = ((j%6)<<6)+ bbc[j/6]
                print 'rfrx1=0x%x'%rfrx1
                self.pbus.pbus_wr('bb', 'en1', 0x189)
                self.pbus.pbus_wr('rfrx1', 'en1', rfrx1)
                self.pbus.pbus_wr('bb', 'en2', bb2)
                rxdc = self.wifi.rxdc_cal()
                print rxdc
                sig_amp = 0

                sme06.rfon()
                k = 0
                while ((sig_amp>400) or (sig_amp<100)) and (k<10):
                    k = k+1
                    sme06.setpow(power)
                    time.sleep(0.1)
                    [sig_amp, dc_i, dc_q] = self.iq_est_simple(est_len=2**14)
                    if (sig_amp>400):
                        power = power - 6
                    elif (sig_amp<100):
                        power = power + 6
                    print power
        ##        sme06.rfoff()
        ##        time.sleep(0.1)
                print 'power=%d'%power
                w_str1 = '%d, %d, 0x%x, 0x%x, %d, %d, %d, %d, '%(i, j, rfrx1, bb2, power, sig_amp, dc_i, dc_q)

                data = wifi.test_rxiq(freq, 0, 0)
                print data
                w_str = w_str1 + data +'\n'
                f.write(w_str)
    ##        data=data.split(',')

    ##        self.pbus.pbus_wr('bb', 'en1', 0x18b)
    ##        rxdc = wifi.rxdc_cal()
    ##        print rxdc
    ##        sme06.rfon()
    ##        sme06.setpow(power)
    ##        time.sleep(0.1)
    ##        [sig_amp, dc_i, dc_q] = iq_est_simple(est_len=2**14)
    ####

    def check_rxiq(self,force_en=1, gain=70, bt_mode=0):
        chan = 1
        freq = 2412
        tone_freq = freq+1
        sme06 = sme.sme()
        sme06.setfreq(tone_freq*1e6)
        sme06.rfoff()
        self.wifi.rfchsel(chan)

        power = -20
        if force_en==1:
            num = 1
        else:
            num = 10
        for i in range(0, num):
            if force_en==1:
                force_gain = gain
            else:
                force_gain = 2 + i*8
            self.mem.wrm(0x6001c02c, 31, 23, ((force_gain<<1)|1)); #force gain
            if(bt_mode==1):
                self.pbus.pbus_debugmode()
                self.pbus.pbus_wr('bb', 'en1', 0x18b)

            sme06.rfon()
            k = 0
            sig_amp = 0

            while ((sig_amp>400) or (sig_amp<100)) and (k<20):
                k = k+1
                sme06.setpow(power)
                time.sleep(0.1)
                [sig_amp, dc_i, dc_q] = self.iq_est_simple(est_len=2**14)
                if (sig_amp>400):
                    power = power - 6
                elif (sig_amp<100):
                    power = power + 6
                print power

            title = 'force_gain=%d'%force_gain
##            adcTest.plot_adcspectra(title)

        if(bt_mode==1):
            self.pbus.pbus_workmode()


    def test_remain_rxiqdc(self,chan=1, bt_mode=0):
    ##    chan = 1
        freq = 2412+(chan-1)*5
        tone = 1
        tone_freq = freq+tone
        sme06 = sme.sme()
        wifi.rfchsel(chan)
        sme06.setfreq(tone_freq*1e6)
        sme06.rfoff()
        if bt_mode==1:
            mode='bt'
        else:
            mode = 'wifi'
        filetime = time.strftime('_%Y%m%d_%H%M%S',time.localtime(time.time()))
        f=open(self.curr_data_path +'test_rxremain_chan%d_%s_%s.csv'%(chan, mode,filetime), 'w')
        f.write("i, rfrx1, bben1, bb2, dc_i, dc_q, sig_amp, rxiq\n")

        power = -10
        for i in range(1, 96, 2):
            for j in range(0, 1):
                gain = i
                if bt_mode==1:
                    gain += 128
                print '\ngain=%d\n'%gain
                self.mem.wrm(0x6001c02c, 31, 23, ((gain<<1)|0)); #force gain
                time.sleep(0.001)
                self.mem.wrm(0x6001c02c, 31, 23, ((gain<<1)|1)); #force gain
                self.pbus.pbus_debugmode()
                if bt_mode==1:
                    self.pbus.pbus_wr('bb', 'en1', 0x18b)
                else:
                    self.pbus.pbus_wr('bb', 'en1', 0x189)

                rfrx1=self.pbus.pbus_rd('rfrx1', 'en1')
                bben1 = self.pbus.pbus_rd('bb', 'en1')
                bb2 = self.pbus.pbus_rd('bb', 'en2')
                i1 = self.pbus.pbus_rd('dcoi', 'en1')
                q1 = self.pbus.pbus_rd('dcoq', 'en1')
                i2 = self.pbus.pbus_rd('dcoi', 'en2')
                q2 = self.pbus.pbus_rd('dcoq', 'en2')
                [sig_amp1, dc_i, dc_q] = self.iq_est_simple(est_len=2**14)

                sig_amp = 0
                k = 0
                sme06.rfon()
                self.pbus.pbus_wr('rfrx1', 'en1', 0x184)
                while ((sig_amp>400) or (sig_amp<100)) and (k<20):
                    k = k+1
                    sme06.setpow(power)
                    time.sleep(0.1)
                    [sig_amp, dc_i1, dc_q1] = self.iq_est_simple(est_len=2**14)
                    if (sig_amp>400):
                        power = power - 6
                    elif (sig_amp<100):
                        power = power + 6
                    print power
                print 'power=%d'%power

                [din_i, din_q] = self.adcDump(2048,False,1)
                [sig_pwr,iqmis_pwr,dc_pwr,harm_pwr,noise,noise_ob]=self.pbus.pbus_test.fft_analyze(din_i, din_q,80,tone);
    ##            w_str2 = '%d, %d, '%(iqmis_pwr-sig_pwr,self.pbus.pbus_test.db2dbfs(dc_pwr))
                w_str2 = '%d, '%(iqmis_pwr-sig_pwr)

                self.pbus.pbus_workmode()
                w_str = '%d, 0x%x, 0x%x, 0x%x, %d, %d, %d, '%(i, rfrx1, bben1, bb2, dc_i, dc_q, sig_amp1)+w_str2+'\n'
                f.write(w_str)

    def test_rxdciq(self):
        for chan in range(1, 14, 5):
            for bt_mode in range(0, 2):
                self.test_remain_rxiqdc(chan, bt_mode)


    def sweep_rx_dc(self):
        filetime = time.strftime('_%Y%m%d_%H%M%S',time.localtime(time.time()))
        file_w = self.curr_data_path +'sweep_rx_dc_%s.csv'%filetime
        f=open(file_w, 'w')
        f.write('rfrx1, bbc, bbf, [dcoi en1], [dcoq en1], [dcoi en2], [dcoq en2], adc_i, adc_q, gain_i, gain_q\n')

    ##    #change digital reg
    ##    self.mem.wrm(0x600005c0,0,0,0) #fe_dump
    ##    temp=int(self.i2c.DIG_INF.reg_addr_rd(18),16) #rx_scale

    ##    self.i2c.DIG_INF.reg_addr_wr(180) #rx_scale

    ##    self.mem.wr(0x60000590, (self.mem.rd(0x60000590) & 0xffffffef) + (0x0<<4))  #disable rx_fil80_en
    ##    self.i2c.DIG_INF.reg_rx_clk_force_en= 1;  #open rx clock

    ##    self.i2c.DIG_FE.reg_rx_force_on= 1;  #force rx on

        self.mem.wrm(0x600050e8,23,16,0) #fe_rx_scale
        self.mem.wrm(0x6001c02c, 31, 23, ((70<<1)|1));   #force gain

        self.pbus.pbus_debugmode()
        self.pbus.open_rx()

        rfrx1 = 0x1de
        num = 0
        bbc_m = [0x0, 0x20, 0x30, 0x38, 0x3c, 0x3e, 0x3f]
        for bbc in bbc_m:
            self.sweep_rx_dc_slv(f, rfrx1, bbc, 2)
            num = num +1
            print num
        for bbf in range (0, 6):
            self.sweep_rx_dc_slv(f, rfrx1, 0x20, bbf)
            num = num +1
            print num

    def sweep_rx_dc_slv(self,f, rfrx1, bbc, bbf):
        scale = 40
        #self.pbus.pbus_wr('rfrx1','en1',0x1e0)
        bb = (bbf<<6) + bbc
        self.pbus.pbus_wr('rfrx1','en1',rfrx1)
        self.pbus.pbus_wr('bb','en2',bb)

        dco = ['dcoi', 'dcoq']
        en = ['en1', 'en2']
        smp_num_bits = 6  #len = 2^6

        for i in range(0,4):
            self.pbus.pbus_wr(dco[i%2], en[i/2], 256)
        [dc256_i, dc256_q, power] = self.dc_iq_est(4096)
        f.write(hex(rfrx1)+','+hex(bbc)+','+hex(bbf)+','+'256, 256, 256, 256,'+str(dc256_i)+','+str(dc256_q)+'\n')

        for j in range(2):
            f.write(hex(rfrx1)+','+hex(bbc)+','+hex(bbf)+',')
    ##        for j in range(4):
    ##            if j==i:
    ##                data_w = 256+scale
    ##            else:
    ##                data_w = 256
    ##            self.pbus.pbus_wr(dco[j%2], en[j/2], data_w)
    ##            f.write(str(data_w)+',')
            for i in range(2):
                if i==j:
                    data_w = 256+scale
                else:
                    data_w = 256
                self.pbus.pbus_wr('dcoi', en[i], data_w)
                self.pbus.pbus_wr('dcoq', en[i], data_w)

                f.write(str(data_w)+','+str(data_w)+',')

            [dc_est_i, dc_est_q, power] = self.dc_iq_est(4096)
            [dc_est_i1, dc_est_q1, power] = self.dc_iq_est(4096)
            [dc_est_i2, dc_est_q2, power] = self.dc_iq_est(4096)
            gain_i = float(dc_est_i-dc256_i)/scale
            gain_q = float(dc_est_q-dc256_q)/scale
            gain_i1 = float(dc_est_i1-dc256_i)/scale
            gain_q1 = float(dc_est_q1-dc256_q)/scale
            gain_i2 = float(dc_est_i2-dc256_i)/scale
            gain_q2 = float(dc_est_q2-dc256_q)/scale
            f.write("%2.2f, %2.2f, %2.2f, %2.2f, %2.2f, %2.2f, %2.2f, %2.2f, %2.2f, %2.2f, %2.2f, %2.2f\n"%(dc_est_i,dc_est_q,dc_est_i1, dc_est_q1,dc_est_i2, dc_est_q2,gain_i,gain_q,gain_i1,gain_q1,gain_i2,gain_q2))
    ##        f.write(str(dc_est_i)+','+str(dc_est_q)+','+str(gain_i)+','+str(gain_q)+','+str(gain_i1)+','+str(gain_q1)+','+str(gain_i2)+','+str(gain_q2)+'\n')

    def test_rxdc(self,freq=2500):
        self.rfpll.set_freq(freq)
        self.wifi.rf_tune()
        mac = self.chipid.chip_mac()
        filetime = time.strftime('_%Y%m%d_%H%M%S',time.localtime(time.time()))
        file_w = self.curr_data_path +'test_rxdc_%s_%d_%s.csv'%(mac, freq, filetime)
        f=open(file_w, 'w')
        f.write('rfrx1, bb2, dcoi1, dcoq1, dcoi2, dcoq2, adc_i, adc_q\n')
        self.mem.wrm(0x600050e8,23,16,0) #fe_rx_scale
        self.mem.wrm(0x6001c02c, 31, 23, ((70<<1)|1));   #force gain
    ##    rfrx_m = [0, 0x184, 0x186, 0x1b4, 0x1b6, 0x1bc, 0x1c4, 0x1c6, 0x1cc, 0x1d4, 0x1d6, 0x1dc, 0x1de, 0x19e]
        rfrx_m = [0, 0x184, 0x10e, 0x18e, 0x19e, 0x1be, 0x1ce, 0x1de]
        bb2_m = [0x20, 0x30, 0x38, 0x3c]
        self.pbus.pbus_debugmode()
        self.pbus.open_rx()
        dco = 0x100
        self.pbus.set_dco(dco,dco,dco,dco)
        bb2 = 0x30
        for bb2 in bb2_m:
            for rfrx1 in rfrx_m:
                self.pbus.pbus_wr('rfrx1', 'en1', rfrx1)
                self.pbus.pbus_wr('bb', 'en2', bb2)
                [dc_est_i, dc_est_q, power] = self.dc_iq_est(4096)
                [dc_est_i1, dc_est_q1, power] = self.dc_iq_est(4096)
                [dc_est_i2, dc_est_q2, power] = self.dc_iq_est(4096)
                if(rfrx1==0):
                    bbdci = dc_est_i
                    bbdci1 = dc_est_i1
                    bbdci2 = dc_est_i2
                    bbdcq = dc_est_q
                    bbdcq1 = dc_est_q1
                    bbdcq2 = dc_est_q2
                f.write("0x%x, 0x%x, 0x%x, 0x%x,  0x%x,  0x%x, %2.2f, %2.2f, %2.2f, %2.2f, %2.2f, %2.2f, , %2.2f, %2.2f, %2.2f, %2.2f, %2.2f, %2.2f\n"%(rfrx1,bb2,dco, dco,dco, dco,dc_est_i,dc_est_i1,dc_est_i2,dc_est_q,dc_est_q1,dc_est_q2, dc_est_i-bbdci,dc_est_i1-bbdci1,dc_est_i2-bbdci2,dc_est_q-bbdcq,dc_est_q1-bbdcq1,dc_est_q2-bbdcq2))


    def sweep_rxdc_freq(self):
        filetime = time.strftime('_%Y%m%d_%H%M%S',time.localtime(time.time()))
        file_w = self.curr_data_path +'sweep_rxdc_freq_%s.csv'%(filetime)
        f=open(file_w, 'w')
        f.write('rfrx1, bb2, freq, min_i, max_i, min_q, max_q\n')
        self.mem.wrm(0x600050e8,23,16,0) #fe_rx_scale
        self.mem.wrm(0x6001c02c, 31, 23, ((70<<1)|1));   #force gain
        rfrx_m = [0x1de]  #[0x184, 0x186, 0x1b4, 0x1b6, 0x1bc, 0x1c4, 0x1c6, 0x1cc, 0x1d4, 0x1d6, 0x1dc, 0x1de]
        bb2_m = [0x0]  #[0x20, 0x30, 0x38, 0x3c]
        self.pbus.pbus_debugmode()
        self.pbus.open_rx()
        dco = 0x100
        self.pbus.set_dco(dco,dco,dco,dco)
        self.pbus.pbus_wr('rfrx1', 'en1', 0x1de)
        self.pbus.pbus_wr('bb', 'en2', 0x0)
        for freq in range(2480, 2550, 5):
            self.rfpll.set_freq(freq)
            self.wifi.rf_tune()
            max_i = 0
            max_q = 0
            min_i = 0
            min_q = 0
            for num in range(0, 50):
                [outi, outq] = self.adcDump(numSmp = 1024, enPlot = False, en80M=1, append=True, enReturn=True)
                if(min(outi) < min_i):
                    min_i = min(outi)
                if(max(outi) > max_i):
                    max_i = max(outi)
                if(min(outq) < min_q):
                    min_q = min(outq)
                if(max(outq) > max_q):
                    max_q = max(outq)
                print [min_i, max_i, min_q, max_q]

                if((min_i==-512) or (min_q==-512) or (max_i==511) or (max_q==511)):
                    break

            f.write('0x1de, 0, %d, %d, %d, %d, %d\n'%(freq, min_i, max_i, min_q, max_q))

    def adcDump(self,numSmp = 1024, enPlot = True, en80M=1, append=True, enReturn=True):
        self.mem.wrm(0x6001c0b8,2,0,1)
        self.mem.wrm(0x60006090,1,0,0)
        adc_out = self.adc_dump.adcdumptest('dump',numSmp,'sw','com','10bit',en80M) #80m, plot, chan, gain
        out_i = plot.myplot.get_csv_vect(adc_out[4],3,1)
        out_q = plot.myplot.get_csv_vect(adc_out[4],3,2)
        if enPlot:
            if not append: plt.figure()
            plt.step(range(numSmp),out_i,label='i out')
            plt.step(range(numSmp),out_q,label='q out')
            plt.legend()
            plt.grid()
            plt.show()
        print 'tone power i:',10*np.log10(np.var(out_i))
        print 'tone power q:',10*np.log10(np.var(out_q))
        if enReturn:
            return [out_i, out_q]

    def loopback_test_phase(self,tone_step=8, est_len=2**12, loop_case=0):
        att = 24
        bbgain = 0x20
        pagain = 0xf
        self.wifi.txtone_step(0, tone_step, att)

        self.wifi.set_loopback_mode(self,pa_gain=0xf, bbgain=0x20, loop_case=0)

        self.wifi.txtone_step(1, tone_step, att)
        self.mem.wrm(0x600060b8, 21, 21,1)  #dis_phase

        self.mem.wrm(0x6000607c, 16, 2, est_len)  #iqest timmer
        self.iq_est_enable(1)
        self.wait_iqest_done()

        cw_rms = 511.503354
        tot_power = self.mem.rd(0x600060e4)
        tot_power = float(tot_power)*8 / est_len
        i_power = self.mem.rd(0x600060ec)
        q_power = self.mem.rd(0x600060f0)
        i_power = float(i_power)*4 / est_len
        q_power = float(q_power)*4 / est_len
        dc_i = self.read_sign(0x600060dc)
        dc_q = self.read_sign(0x600060e0)
        dc_i = float(dc_i) / 2**6 / est_len  #8-2
        dc_q = float(dc_q) / 2**6 / est_len  #8-2
        dc_power = dc_i**2 + dc_q**2

        result1 = self.read_sign(0x60006080)
        result2 = self.read_sign(0x60006084)
        result3 = self.read_sign(0x60006088)
        result4 = self.read_sign(0x6000608c)
##        result1 = (float(result1)*4 - est_len * dc_i * 2000/8192)/4
##        result2 = (float(result2)*4 - est_len * dc_q * 2000/8192)/4
##        result3 = (float(result3)*4 - est_len * dc_i * 2000/8192)/4
##        result4 = (float(result4)*4 - est_len * dc_q * 2000/8192)/4
        result1 = float(result1)*4 / est_len
        result2 = float(result2)*4 / est_len
        result3 = float(result3)*4 / est_len
        result4 = float(result4)*4 / est_len
##        print "r1=%2.2f,r2=%2.2f,r3=%2.2f,r4=%2.2f"%(result1,result2,result3,result4)
        sig_i = result1 + result4
        sig_q = result3 - result2
        phase = math.atan2(sig_q,sig_i)/math.pi*180
        if phase<0:
            phase = phase + 360

        T = (2**11 *1.0 / tone_step / 80.0)

        t_us = (phase / 360.0)*T
        cycle = t_us * 80

        self.iq_est_enable(0)
        sig_amp = np.sqrt(tot_power)
    ##    wifi.tx_tone1(0, freq, att)
##        print '%2.2f, %2.2f, %2.2f, min=%2.2f, max=%2.2f, %2.2f,sig_i=%2.2f, sig_q=%2.2f, tan=%2.2f, angle=%f, t=%f, cycle=%f'%(tot_power, dc_i, dc_q, 1<<12, 1<<18, np.sqrt(tot_power),sig_i, sig_q, sig_q/sig_i, phase, t_us, cycle)
##        print 'step=%d, %2.2f, tan=%2.2f, angle=%f, t=%f, cycle=%f'%(tone_step, sig_amp, sig_q/sig_i, phase, t_us, cycle)
        return [sig_amp, phase, cycle]

    def test_phase_case(self, test_num=0):
        title = 'MAC, test_num, tone_step, filter_40m, dac_filt_adc sig_amp, dac_filt_adc phase, dac_filt_adc cycles, dig_loop sig_amp, dig_loop phase, dig_loop cycles\n'
        fname = self.wifi.get_filename('test_phase_case', 'test_phase_case')
        csvreport1 = csvreport(fname, title, 1)
        mac = self.wifi.read_mac()
        freq_m = [8,16,32,64]
        for step in freq_m:
            for band_40m in range(0,2):
                self.wifi.rfchsel(1,band_40m*2)
                [sig_amp1, phase1, cycle1] = self.loopback_test_phase(step, 2**14, 1)
                [sig_amp2, phase2, cycle2] = self.loopback_test_phase(step, 2**14, 2)
                csvreport1.write_data([mac, test_num, step, band_40m, sig_amp1, phase1, cycle1,sig_amp2, phase2, cycle2])
                print [mac, test_num, step, band_40m, sig_amp1, phase1, cycle1,sig_amp2, phase2, cycle2]

    def pa_loopback_test(self,tone_att=24, pa_gain=0xf, bbgain=0x20, loop_case=0, est_len=2**12):

        tone_step1 = 128
        tone_step2 = 40
        self.wifi.txtone_step(0, tone_step1, tone_att, 0, tone_step2, tone_att)

        self.wifi.set_loopback_mode(pa_gain, bbgain, loop_case)

        self.wifi.txtone_step(1, tone_step1, tone_att, 0, tone_step2, tone_att)
        self.mem.wrm(0x600060b8, 21, 21,1)  #dis_phase

        self.mem.wrm(0x6000607c, 16, 2, est_len)  #iqest timmer
        self.iq_est_enable(1)
        self.wait_iqest_done()

        cw_rms = 511.503354
        tot_power = self.mem.rd(0x600060e4)
        tot_power = float(tot_power)*8 / est_len
        i_power = self.mem.rd(0x600060ec)
        q_power = self.mem.rd(0x600060f0)
        i_power = float(i_power)*4 / est_len
        q_power = float(q_power)*4 / est_len
        dc_i = self.read_sign(0x600060dc)
        dc_q = self.read_sign(0x600060e0)
        dc_i = float(dc_i) / 2**6 / est_len  #8-2
        dc_q = float(dc_q) / 2**6 / est_len  #8-2
        dc_power = dc_i**2 + dc_q**2

        result1 = self.read_sign(0x60006080)
        result2 = self.read_sign(0x60006084)
        result3 = self.read_sign(0x60006088)
        result4 = self.read_sign(0x6000608c)
##        result1 = (float(result1)*4 - est_len * dc_i * 2000/8192)/4
##        result2 = (float(result2)*4 - est_len * dc_q * 2000/8192)/4
##        result3 = (float(result3)*4 - est_len * dc_i * 2000/8192)/4
##        result4 = (float(result4)*4 - est_len * dc_q * 2000/8192)/4
        result1 = float(result1)*4 / est_len
        result2 = float(result2)*4 / est_len
        result3 = float(result3)*4 / est_len
        result4 = float(result4)*4 / est_len
##        print "r1=%2.2f,r2=%2.2f,r3=%2.2f,r4=%2.2f"%(result1,result2,result3,result4)
        sig_i = result1 + result4
        sig_q = result3 - result2

        self.iq_est_enable(0)
        sig_amp = np.sqrt(tot_power)
    ##    wifi.tx_tone1(0, freq, att)
        print '%2.2f, %2.2f, %2.2f, min=%2.2f, max=%2.2f, %2.2f,sig_i=%2.2f, sig_q=%2.2f'%(tot_power, dc_i, dc_q, 1<<12, 1<<18, np.sqrt(tot_power),sig_i, sig_q)
##        print 'step=%d, %2.2f, tan=%2.2f, angle=%f, t=%f, cycle=%f'%(tone_step, sig_amp, sig_q/sig_i, phase, t_us, cycle)
        return [sig_amp]


    def rxiq_cal_test(self):
        title = 'reg, cp1p1_pvt_reg,cp1p6_dreg,cp1p2_dreg,rfrx_mx_db,cgm_bias,dres12k,RXIQ: \n'
        fname = self.wifi.get_filename('test_rx_iq', 'test_rx_iq')
        csvreport1 = csvreport(fname, title, 1)
        mac = self.wifi.read_mac()

        cp1p1_pvt_org = self.i2c.bias.cp1p1_pvt_reg
        cp1p6_org = self.i2c.bias.cp1p6_dreg
        cp1p2_org = self.i2c.bias.cp1p2_dreg
        rfrx_mx_org = self.i2c.rfrx.rfrx_mx_db
        cgm_bias_org = self.i2c.bias.cgm_bias
        dres12k_org = self.i2c.bias.dres12k


        for case,data_min,data_max in [[0,0,15],[1,0,15],[2,0,15],[3,0,3],[4,0,3],[5,0,15]]:
            for i in range(data_min,data_max+1):
                if case == 0 :
                    self.i2c.bias.cp1p1_pvt_reg = i
                elif case == 1:
                    self.i2c.bias.cp1p6_dreg = i
                elif case == 2:
                    self.i2c.bias.cp1p2_dreg = i
                elif case ==  3:
                    self.i2c.rfrx.rfrx_mx_db = i
                elif case ==  4:
                    self.i2c.bias.cgm_bias = i
                elif case ==  5:
                    self.i2c.bias.dres12k = i

                cp1p1_pvt_reg = self.i2c.bias.cp1p1_pvt_reg
                cp1p6_dreg = self.i2c.bias.cp1p6_dreg
                cp1p2_dreg = self.i2c.bias.cp1p2_dreg
                rfrx_mx_db = self.i2c.rfrx.rfrx_mx_db
                cgm_bias = self.i2c.bias.cgm_bias
                dres12k = self.i2c.bias.dres12k
                result = self.comport.req_com("rx_cal_iq 0")


                result = str.split(result)
                print result
                csvreport1.write_data([mac, cp1p1_pvt_reg, cp1p6_dreg, cp1p2_dreg, rfrx_mx_db,cgm_bias,dres12k,result[1],result[2],result[3],result[4],result[5],result[6]])
            self.i2c.bias.cp1p1_pvt_reg = 7
            self.i2c.bias.cp1p6_dreg = cp1p6_org
            self.i2c.bias.cp1p2_dreg = cp1p2_org
            self.i2c.rfrx.rfrx_mx_db = rfrx_mx_org
            self.i2c.bias.cgm_bias = cgm_bias_org
            self.i2c.bias.dres12k = dres12k_org


