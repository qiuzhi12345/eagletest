import time
import csv
import os
import serial
import codecs
import sys
import re
import matplotlib.pyplot as plt
import pylab
from baselib.loglib.log_lib import *
from rftest.rflib.csv_report import csvreport
from rftest.rflib.wifi_lib import WIFILIB
from hal.wifi_api import WIFIAPI
from hal.Init import HALS
from baselib.test_channel.com import COM as com
from rftest.rflib import rfglobal

sens_dict = rfglobal.sens_dict
target_pwr_dict = rfglobal.ESP32_target_pwr_dict
rate_list=[
    'lr6','lr7',
    '1m','2m','5.5m','11m',
    '6m','9m' ,'12m','18m','24m','36m','48m','54m',
    'mcs0','mcs1','mcs2','mcs3','mcs4','mcs5','mcs6','mcs7',
    'mcs0_40','mcs1_40','mcs2_40','mcs3_40','mcs4_40','mcs5_40','mcs6_40','mcs7_40']

PackLen_list= [1024,512,256,128,64]
#PackLen_list= [256,128,64]


class Packet_Test(object):

    def __init__(self, comport, chipv = "ESP32"):

        self.comport = comport
        self.chipv = chipv
        self.wifiapi = WIFIAPI(self.comport,self.chipv)
        self.wifi = WIFILIB(self.comport,self.chipv)

    def set_att(self,att=10, port=5, atten_fix=False):
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


    def packet_tx(self, chan=1,cbw40m=0, rate_index=0x0, PackNum=10000,PackLen=400):

        frm_delay = 20
        self.wifiapi.rfchsel(chan,cbw40m*2)
        self.wifiapi.filltxpacket(0xa0000+PackLen,28,0)
        out = self.wifiapi.txstart_over(rate_index,PackNum,10,frm_delay,cbw40m,0,1)
        return out


    def LR_test(self, comprx=5,comp_atten= 0, channel= 1,rx_per=0.9, PackNum=1000):

        title1 = 'chan, rate, hex(rate_index), PackLen, total_atten, atten, rxpwr, PackNum, DesirePackNum, rssi, gain, noise, err, err2, freqoff\n'
        fname1 = self.wifi.get_filename('packet_dut2dut', 'LR', 'packet_dut2dut')
        csvreport1 = csvreport(fname1+'_packet_dut2dut', title1)

        title2 = 'chan, date_rate,rate_index,PackLen,rxpwr,rssi,sens_find\n'
        csvreport2 = csvreport(fname1, title2)

        curr_data_path =''
        path_strlst = fname1.split('/')
        for i in range (0,(len(path_strlst)-1)):
            curr_data_path +=str(path_strlst[i])+'/'

        color_map=['b','g','r','c','m','y','k'];
        style_map=['--','-'];
        colsty=[];
        for element1 in style_map:
            for element2 in color_map:
                colsty.append(element1+element2);

        colsty_num = 1
        attenuator = 60
        cable_lose = 4
        program_atten_lose = 5

        chiprx = HALS(com(comprx))

        for PackLen_curr in PackLen_list:
            colsty_num +=1
            rate = []
            rate_index_lst = []
            PackLen = []
            sens = []
            sens_rssi = []
            err_lst = []
            err_fcs_lst = []

            for rate_curr in rate_list:

                perform_list = []

                cbw40m = self.wifi.rate2ht40(rate_curr)
                rate_index = self.wifi.ratecheck(rate_curr)
                chan = channel
                if cbw40m == 1:
                    if chan <3: chan = 3
                    elif chan>11: chan = 11

                sens_target = sens_dict[rate_curr]
                pwr_target = target_pwr_dict[rate_curr]

                set_atten = int(pwr_target - attenuator - cable_lose - program_atten_lose- sens_target)


                for att_offset in range(6,-7,-1):

                    atten = att_offset+set_atten
                    self.set_att(atten,comp_atten)
                    total_atten = attenuator + cable_lose + program_atten_lose + att_offset + set_atten
                    rxpwr = pwr_target - total_atten

                    if re.match(r'lr',rate_curr,re.M)!=None:
                        chiprx.wifiapi.enable_lr()
                        self.wifiapi.enable_lr()
                    else:
                        chiprx.wifiapi.disable_lr()
                        self.wifiapi.disable_lr()

                    chiprx.wifiapi.rx_per_init()
                    chiprx.wifiapi.cbw40m_en(cbw40m)
                    chiprx.wifiapi.esp_rx(chan,rate_index)

                    txreturn = self.packet_tx(chan,cbw40m,rate_index,PackNum,PackLen_curr)

                    if txreturn !="Tx Over, tx_state:0x0! ":
                        rxreturn = chiprx.wifiapi.cmdstop()
                        [DesirePackNum, rssi, gain, noise, err, err2, freqoff] = self.wifi.rxresult(rxreturn)

                        perform_list.append((chan, rate_curr, hex(rate_index), PackLen_curr, total_atten, atten, rxpwr, PackNum, DesirePackNum, gain, rssi, noise, err, err2, freqoff))
                        csvreport1.write_data([chan, rate_curr, hex(rate_index), PackLen_curr, total_atten, atten, rxpwr, PackNum, DesirePackNum, gain, rssi, noise, err, err2, freqoff])

                [cur_sense, cur_sense_rssi,  cur_err, cur_err_fcs, cur_sense_find] = self.find_sens(rx_per,perform_list)

                rate.append(rate_curr)
                rate_index_lst.append(rate_index)
                PackLen.append(PackLen_curr)
                sens.append(cur_sense)
                sens_rssi.append(cur_sense_rssi)
                err_lst.append(cur_err)
                err_fcs_lst.append(cur_err_fcs)

                csvreport2.write_data([chan, rate_curr, hex(rate_index),PackLen_curr,cur_sense,cur_sense_rssi,cur_sense_find])

            pylab.figure(100)
            pylab.title("Packets_test_sens")
            scale_lst = range(len(rate))
            pylab.plot(scale_lst,sens,color_map[colsty_num],label='PackLen_%s'%(PackLen_curr),linewidth=3)
            plt.xticks(scale_lst,rate,rotation=90)
            plt.tick_params(23)
            pylab.legend()
            pylab.grid()
            pylab.legend(loc='lower right',fontsize=10)
            plt.savefig(curr_data_path+'sens_all.png');

            pylab.figure(101)
            pylab.title("Packets_test_rssi")
            pylab.plot(scale_lst,sens_rssi,color_map[colsty_num],label='PackLen_%s'%(PackLen_curr),linewidth=3)
            plt.xticks(scale_lst,rate,rotation=90)
            plt.tick_params(10)
            pylab.legend()
            pylab.grid()
            pylab.legend(loc='lower right',fontsize=10)
            plt.savefig(curr_data_path+'sens_rssi_all.png');

        plt.close()
        plt.close()

        chiprx.deinit()


    def find_sens(self, rx_per, perform_list):

        cur_sense=0
        cur_sense_rssi=0
        cur_sense_find=0

        cur_err=0
        cur_err_fcs=0

        for data in perform_list:
            loginfo(data)
            csv_row=[data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14]]

            if cur_sense_find==0:
                if data[8]>=(data[7]*rx_per):
                    cur_sense=data[6]      # rxpwr
                    cur_sense_rssi=data[9] # rssi
                    cur_err=data[12]
                    cur_err_fcs = data[13]
                    cur_sense_find=1
                else:
                    cur_sense=data[6]      # rxpwr
                    cur_sense_rssi=data[9] # rssi
                    cur_err=data[12]
                    cur_err_fcs = data[13]
                    cur_sense_find=0

        return [cur_sense, cur_sense_rssi/10.0, cur_err, cur_err_fcs, cur_sense_find]

















