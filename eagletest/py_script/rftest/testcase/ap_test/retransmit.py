import time
import re
import csv
import os, sys
import matplotlib.pyplot as plt
import pylab
import xlrd
import numpy as np
import pandas as pd
from collections import Counter
import serial
from scapy.all import AsyncSniffer, conf, wireshark
from baselib.instrument.smc import smc
from baselib.test_channel.com import COM as com
from baselib.loglib.log_lib import *
from rftest.rflib.wifi_lib import WIFILIB
from rftest.rflib.csv_report import csvreport
from rftest.rflib import rfglobal


ratedict_11bg={
    2:'1m',
    4:'2m',
    11:'5.5m',
    22:'11m',
    12:'6m',
    18:'9m',
    24:'12m',
    36:'18m',
    48:'24m',
    72:'36m',
    96:'48m',
    108:'54m'}
ratedict_11n={
    0:'mcs0',
    1:'mcs1',
    2:'mcs2',
    3:'mcs3',
    4:'mcs4',
    5:'mcs5',
    6:'mcs6',
    7:'mcs7'}


class sniffer(object):
    def __init__(self,interface='wlan0', cap_filter="host 192.168.0.101 and dst 192.168.0.122"):
        self.FILTER = cap_filter
        self.INTERFACE = interface
        self.DSPLAY_WITH_WIRESHARK = False
        conf.use_pcap = True


    def sniffer_set(self, iface='wlan0', channel=4, bw_en=1):
        os.system('sudo ifconfig %s down' % iface)
        os.system('sudo iw dev %s set type monitor' % iface)
        os.system('sudo ifconfig %s up' % iface)
        if bw_en == 0:
            os.system('sudo iw dev %s set channel %s HT20' % (iface, channel))
        else:
            os.system('sudo iw dev %s set channel %s HT40+' % (iface, channel))


    def process(self, packets):
        received_packets = list()
        retransmissions = list()
        # with open("result.txt", "w") as f:
        for i, pkt in enumerate(packets):
            try:
                if pkt.payload.FCfield.value & 0x8:
                    # f.write("retrans: {}, {}".format(i+1, pkt.payload.SC // 16))
                    retransmissions.append(pkt)

            except (AttributeError, TypeError):
                pass
        received_packets = packets.res
        if len(received_packets) == 0:
            logerror("no packets captured")
            retry_ratio = -99
            retry_num = 0
            packet_sum = 0
        else:
            # f.write("{:.04f}%, {} / {}".format(float(len(retransmissions) * 100) / len(received_packets),len(retransmissions), len(received_packets)))
            print
            "{:.04f}%, {} / {}".format(float(len(retransmissions) * 100) / len(received_packets),
                                       len(retransmissions), len(received_packets))
            retry_ratio = float(len(retransmissions) * 100) / len(received_packets)
            retry_num = len(retransmissions)
            packet_sum = len(received_packets)
        return [retry_ratio, retry_num, packet_sum]


    def start_sniff(self, timeout=10):
        t = AsyncSniffer(iface=self.INTERFACE, filter=self.FILTER)
        t.start()
        time.sleep(timeout)
        result = t.stop()
        res = self.process(result)
        if self.DSPLAY_WITH_WIRESHARK:
            wireshark(result)
        return res

class retransmit(object):
    def __init__(self,com_smc=0,comport=1,interface='wlan0',channel=4,cap_filter="host 192.168.0.101 and dst 192.168.0.122",ssid='test727'):
        self.FILTER = cap_filter
        self.INTERFACE = interface
        self.DSPLAY_WITH_WIRESHARK = False
        self.sc=smc(com(com_smc))
        self.comport=com(comport)
        self.channel=channel
        conf.use_pcap = True
        self.reg_set()
        self.stbc_str=''
        self.bw_str=''
        self.ssid=ssid
        self.sniffer_set(iface=self.INTERFACE,channel=self.channel,bw_en=1)

    def idf_reboot(self):
        self.comport.req_com("reboot",timeout=10)
        time.sleep(10)

    def reg_set(self):
        self.reg_wr(0x60004570,0xc8)
        time.sleep(0.5)
        self.reg_wr(0x6000456c, 0xc9)
        time.sleep(0.5)
        self.reg_wr(0x6001c058, 0x79bf91b0)
        time.sleep(0.5)
        self.reg_wr(0x6001cc94, 0x00543210)
        time.sleep(0.5)
        self.reg_wr(0x6001cd44, 0x3d3a4d53)
        time.sleep(0.5)

    def reg_rd(self,reg_addr):
        self.comport.req_com('reg -R -a %s'%reg_addr,timeout=10)

    def reg_wr(self,reg_addr,reg_value):
        self.comport.req_com('reg -W -a %s -v %s' % (reg_addr,reg_value),timeout=10)

    def reg_rdm(self,reg_value,msb,lsb):
        mask=(1<<(msb+1))-(1<<lsb)
        result=(reg_value & mask)>>lsb
        return hex(result)

    def reg_wrm(self,reg_addr,reg_value,msb,lsb,value):
        mask=(1<<(msb+1))-(1<<lsb)
        result=(reg_value & ~mask) | ((value<<lsb) & mask)
        self.reg_wr(reg_addr,result)


    def sniffer_set(self,iface='wlan0',channel=4,bw_en=1):
        os.system('sudo ifconfig %s down'%iface)
        os.system('sudo iw dev %s set type monitor' % iface)
        os.system('sudo ifconfig %s up' % iface)
        if bw_en==0:
            os.system('sudo iw dev %s set channel %s HT20' % (iface,channel))
        else:
            os.system('sudo iw dev %s set channel %s HT40+' % (iface, channel))
        time.sleep(0.5)

    def ssid_set(self,ssid="unifi_test"):
        self.ssid=ssid

    def stbc_set(self,stbc_en=0):
        if stbc_en==0:
            self.comport.req_com('config -S -s 0', timeout=10)
            self.stbc_str='nostbc'
        else:
            self.comport.req_com('config -S -s 1', timeout=10)
            self.stbc_str = 'stbc'
        time.sleep(0.5)
        self.comport.req_com('sta -C -s %s'%self.ssid, timeout=10)
        time.sleep(2)
        self.comport.req_com('sta -D', timeout=10)
        time.sleep(0.5)
        self.comport.req_com('sta -C -s %s'%self.ssid, timeout=10)
        time.sleep(2)

    def bw40_set(self,bw40_en=1):
        if bw40_en!=0:
            self.comport.req_com('sta -D', timeout=10)
            time.sleep(0.5)
            self.comport.req_com('phy -S -o 0 -m n -b 40', timeout=10)
            self.bw_str="HT40"
            time.sleep(0.5)
            self.sniffer_set(iface=self.INTERFACE, channel=self.channel, bw_en=1)
        else:
            self.comport.req_com('sta -D', timeout=10)
            time.sleep(0.5)
            self.comport.req_com('phy -S -o 0 -m n -b 20', timeout=10)
            self.bw_str = "HT20"
            time.sleep(0.5)
            self.sniffer_set(iface=self.INTERFACE, channel=self.channel, bw_en=0)

    def dut_mode_set(self,stbc_en=0,bw40_en=1):
        self.bw40_set(bw40_en=bw40_en)
        time.sleep(1)
        self.stbc_set(stbc_en=stbc_en)

    def test_retry(self,mode_set_en=1,stbc_en=0,bw40_en=1,angle_div=45,captrue_time=60,loop_num=1,fig_en=1,module_name='fpga724_v2.6',info="ch6_rx_unifi"):
        if mode_set_en!=0:
            self.dut_mode_set(stbc_en=stbc_en,bw40_en=bw40_en)
        for loop in range(loop_num):
            title = 'angle,rx_retry_ratio,retry_packet,total_packet,rate_max1,rate_ratio_max1,rssi_max1,rate_max2,rate_ratio_max2,rssi_max2,rate_max3,rate_ratio_max3,rssi_max3,rate_retry,rate_retry_ratio\n'
            fname = self.get_filename('retransmit_%s'%module_name, '%s_%s_%s_%s'%(module_name,self.stbc_str,self.bw_str, info))
            csvreport1 = csvreport(fname, title)
            res_sum=[]
            res_angle = []
            res_retry = []
            sum_angle=360/angle_div
            self.sc.return_origin_angle()
            for i in range(0,sum_angle):
                [retry_ratio, retry_num,packet_sum,rate_max1,rate_ratio_max1,rssi_max1,rate_max2,rate_ratio_max2,rssi_max2,rate_max3,rate_ratio_max3,rssi_max3,rate_retry,rate_retry_ratio]= self.start_sniff(captrue_time)
                angle_cur=angle_div*i
                i+=1
                loginfo("retry_ratio,angle : %s,%s"%(retry_ratio,angle_cur))
                res_sum.append([retry_ratio,angle_cur])
                res_angle.append(angle_cur)
                res_retry.append(retry_ratio)
                csvreport1.write_data([angle_cur,retry_ratio, retry_num,packet_sum,rate_max1,rate_ratio_max1,rssi_max1,rate_max2,rate_ratio_max2,rssi_max2,rate_max3,rate_ratio_max3,rssi_max3,rate_retry,rate_retry_ratio])
                self.sc.run(angle=angle_div,)
                time.sleep(1)
            self.sc.return_origin_angle()
            #print res_sum
            loop+=1
            if fig_en!=0:
                pylab.ion()
                plt.plot(res_angle, res_retry)
                pylab.show()

    def test_retry_debug(self,stbc_en=0,bw40_en=1,angle_div=45,angle_start=0,angle_end=360,captrue_time=60,module_name='fpga724_v2.6',info="ch6_rx_unifi"):
        self.dut_mode_set(stbc_en=stbc_en, bw40_en=bw40_en)
        title1 = 'angle,rx_retry_ratio,retry_packet,total_packet,rate_max1,rate_ratio_max1,rssi_max1,rate_max2,rate_ratio_max2,rssi_max2,rate_max3,rate_ratio_max3,rssi_max3,rate_retry,rate_retry_ratio\n'
        fname1 = self.get_filename('retransmit_%s' % module_name, '%s_%s_%s_%s'%(module_name,self.stbc_str,self.bw_str, info))
        csvreport1 = csvreport(fname1, title1)
        res_sum = []
        res_angle = []
        res_retry = []
        sum_angle = (angle_end - angle_start) / angle_div
        self.sc.return_origin_angle()
        self.sc.run(angle=angle_start)
        for i in range(0, sum_angle):
            [retry_ratio, retry_num,packet_sum,rate_max1,rate_ratio_max1,rssi_max1,rate_max2,rate_ratio_max2,rssi_max2,rate_max3,rate_ratio_max3,rssi_max3,rate_retry,rate_retry_ratio] = self.start_sniff(captrue_time)
            angle_cur = angle_div * i
            i += 1
            loginfo("retry_ratio,angle : %s,%s" % (retry_ratio, angle_cur))
            res_sum.append([retry_ratio, angle_cur])
            res_angle.append(angle_cur)
            res_retry.append(retry_ratio)
            csvreport1.write_data([angle_cur,retry_ratio, retry_num,packet_sum,rate_max1,rate_ratio_max1,rssi_max1,rate_max2,rate_ratio_max2,rssi_max2,rate_max3,rate_ratio_max3,rssi_max3,rate_retry,rate_retry_ratio])
            self.sc.run(angle=angle_div)
            time.sleep(1)
        self.sc.return_origin_angle()
        return res_angle,res_retry,res_sum


    def test_retry_loop(self,angle_div=45,angle_start=0,angle_end=360,captrue_time=60,loop_num=1,module_name='fpga724_v2.6',info="ht40_ch6_rx_unifi"):
        for loop in range(loop_num):
            self.test_retry_debug(angle_div=angle_div,angle_start=angle_start,angle_end=angle_end,captrue_time=captrue_time,module_name=module_name,info=info)
            loop += 1

    def test_retry_reg_scan(self,angle_div=45,stbc_en=0,bw40_en=1,reg_addr='0x6001cd3c',reg_start=0,reg_end=0xff,angle_start=0,angle_end=360,captrue_time=60,fig_en=1,module_name='fpga724_v2.6',info="ch6_rx_unifi"):
        self.dut_mode_set(stbc_en=stbc_en,bw40_en=bw40_en)
        self.reg_set()
        title0 = 'reg_addr,reg_value,angle,rx_retry_ratio\n'
        fname0 = self.get_filename('retransmit_reg_sum_%s' % module_name, '%s_%s_%s_%s'%(module_name,self.stbc_str,self.bw_str, info))
        csvreport0 = csvreport(fname0, title0)

        for reg_value in range(reg_start,reg_end,4):
            reg=(reg_value<<24)+(reg_value<<16)+(reg_value<<8)+reg_value
            loginfo('reg value :   %s'%hex(reg))
            #cmdstr="reg -W -a %s -v %s"%(reg_addr,hex(reg))
            #self.comport.req_com(cmdstr,timeout=10)
            self.reg_wr(reg_addr,hex(reg))
            _info=info+'_%s'%hex(reg)
            res_angle,res_retry,res_sum=self.test_retry_debug(angle_div=angle_div, angle_start=angle_start, angle_end=angle_end,
                                  captrue_time=captrue_time, module_name=module_name, info=_info)
            for i in range(len(res_sum)):
                csvreport0.write_data([reg_addr,hex(reg),res_sum[i][1],res_sum[i][0]])
                i+=1

            if fig_en!=0:
                pylab.ion()
                plt.plot(res_angle, res_retry, label='%s' % hex(reg_value))
                pylab.show()
                filetime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
                plt.savefig('%s_%s'%(info,filetime))

    def test_retry_allmode(self,angle_div=6,angle_start=0,angle_end=360,captrue_time=5,module_name='fpga724_m1_v2.6.6',info="ch6_rx_unifi"):
        for i in (1,0):
            for j in (0,1):
                self.test_retry_debug(stbc_en=j,bw40_en=i,angle_div=angle_div,angle_start=angle_start,angle_end=angle_end,captrue_time=captrue_time,module_name=module_name,info=info)

    def test_retry_reg_scan_allmode(self,angle_div=6,reg_addr='0x6001cd3c',reg_start=0,reg_end=0xff,angle_start=0,angle_end=360,captrue_time=60,fig_en=1,module_name='fpga724_m1_v2.6.6',info="ch6_rx_unifi"):
        for i in (1,0):
            for j in (0,1):
                self.test_retry_reg_scan(angle_div=angle_div,stbc_en=j,bw40_en=i,reg_addr=reg_addr,reg_start=reg_start,reg_end=reg_end,angle_start=angle_start,angle_end=angle_end,captrue_time=captrue_time,fig_en=fig_en,module_name=module_name,info=info)

    def test_retry_total(self,module_name='fpga724_m1_v2.6.6',info="ch6_rx_unifi"):
        self.test_retry_allmode(module_name=module_name,info=info)
        self.test_retry_reg_scan_allmode(module_name=module_name,info=info)

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
                os.makedirs(rfdata_path)

        data_path1 = rfdata_path+'%s/'%(folder)
        if os.path.exists(data_path1) == False:
            os.makedirs(data_path1)

        filetime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()));

        gen_folder = '%s'%(filetime[0:8])
        data_path2 = data_path1 +'%s/'%(gen_folder)
        if os.path.exists(data_path2) == False:
            os.makedirs(data_path2)

        fname = '%s_'%(file_name)
        outfile_name = data_path2 + fname

        if sub_folder != '':
            gen_folder = '%s_%s'%(sub_folder,filetime[0:8])
            sub_path = data_path2+'%s/'%(gen_folder)
            if os.path.exists(sub_path) == False:
                os.makedirs(sub_path)

            outfile_name = sub_path + file_name

        return outfile_name

    def process(self,packets):
        received_packets = list()
        retransmissions = list()
        rate_list = list()
        rssi = list()
        res=list()
        rate_retry=list()
        #with open("result.txt", "w") as f:
        for i, pkt in enumerate(packets):
            try:
                if pkt.ChannelFlags.value &(1<<5) > 0:
                    wifi_mode="11b"
                    rate=ratedict_11bg[pkt.Rate]
                elif pkt.ChannelFlags.value &(1<<6) > 0:
                    wifi_mode="11g"
                    rate = ratedict_11bg[pkt.Rate]
                elif pkt.ChannelFlags.value &(1<<10) > 0:
                    if pkt.MCS_bandwidth==0:
                        wifi_mode="11n_20"
                    elif pkt.MCS_bandwidth==1:
                        wifi_mode="11n_40"
                    rate=ratedict_11n[pkt.MCS_index]
                _rate="%s_%s"%(wifi_mode,rate)
                rate_list.append(_rate)
                _rssi=pkt.dBm_AntSignal
                rssi.append(_rssi)
                res.append([_rate,_rssi])
                if pkt.payload.FCfield.value & 0x8:
                    rate_retry.append(_rate)
                    #f.write("retrans: {}, {}".format(i+1, pkt.payload.SC // 16))
                    retransmissions.append(pkt)

            except (AttributeError, TypeError):
                pass
        received_packets = packets.res
        rate_info = []
        if len(received_packets) == 0:
            logerror("no packets captured")
            retry_ratio=-1
            retry_num=0
            packet_sum=0
            rate_info=[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
            rate_retry_info = [-1, -1]
        else:
            #f.write("{:.04f}%, {} / {}".format(float(len(retransmissions) * 100) / len(received_packets),len(retransmissions), len(received_packets)))
            print"{:.04f}%, {} / {}".format(float(len(retransmissions) * 100) / len(received_packets),
                                               len(retransmissions), len(received_packets))
            retry_ratio= float(len(retransmissions) * 100) / len(received_packets)
            retry_num=len(retransmissions)
            packet_sum=len(received_packets)

            if len(rate_retry)==0:
                rate_retry_info=[-1,-1]
            else:
                df_retry=pd.DataFrame(np.array(rate_retry),columns=['rate'])
                _df_retry=df_retry['rate'].value_counts()
                rate_retry_info=[_df_retry.index[0],(_df_retry.iloc[0])*100/float(len(retransmissions))]

            df=pd.DataFrame(np.array(res),columns=['rate','rssi'])
            df1=df['rate'].value_counts()
            for i in range(len(df1.index)):
                rate_max=df1.index[i]
                data_tmp1 = df.loc[df['rate']==rate_max].rssi
                data_t3=pd.to_numeric(data_tmp1,errors='coerce')
                data_tmp2 = data_t3.mean()
                rssi_avg = data_tmp2
                rate_ratio = (df1.iloc[i]) *100/ float(len(received_packets))
                rate_info.append([rate_max,rate_ratio,rssi_avg])
                if len(df1.index)==1:
                    rate_info.append([-1,-1,-1])
                    rate_info.append([-1, -1, -1])
                if len(df1.index)==2 and i==1:
                    rate_info.append([-1, -1, -1])
                if i>=2:
                    break
        print rate_info
        return [retry_ratio,retry_num,packet_sum,rate_info[0][0],rate_info[0][1],rate_info[0][2],rate_info[1][0],rate_info[1][1],rate_info[1][2],rate_info[2][0],rate_info[2][1],rate_info[2][2],rate_retry_info[0],rate_retry_info[1]]

    def start_sniff(self,timeout=10):
        t = AsyncSniffer(iface=self.INTERFACE, filter=self.FILTER)
        t.start()
        time.sleep(timeout)
        result = t.stop()
        res=self.process(result)
        if self.DSPLAY_WITH_WIRESHARK:
            wireshark(result)
        return res

class ack(object):
    def __init__(self,interface='wlan0',channel=4,bw_en=0,dst_mac='74:05:a5:3f:ec:41'):
        self.INTERFACE = interface
        self.dst_mac=dst_mac
        self.DSPLAY_WITH_WIRESHARK = False
        self.channel=channel
        conf.use_pcap = True
        self.sniffer_set(iface=self.INTERFACE,channel=self.channel,bw_en=bw_en)

    def process(self,packets):
        ack_list=list()
        #with open("result.txt", "w") as f:
        for i, pkt in enumerate(packets):
            try:
                if pkt.payload.type==1 and pkt.payload.subtype==0xd:
                    if pkt.payload.addr1==self.dst_mac:
                        ack_list.append(pkt)

            except (AttributeError, TypeError):
                pass
        received_packets = packets.res
        if len(received_packets) == 0:
            logerror("no packets captured")
        else:
            #f.write("{:.04f}%, {} / {}".format(float(len(retransmissions) * 100) / len(received_packets),len(retransmissions), len(received_packets)))
            print len(ack_list)
        return len(ack_list)

    def start_sniff(self,timeout=10):
        t = AsyncSniffer(iface=self.INTERFACE)
        t.start()
        time.sleep(timeout)
        result = t.stop()
        res=self.process(result)
        if self.DSPLAY_WITH_WIRESHARK:
            wireshark(result)
        return res

    def sniffer_set(self,iface='wlan0',channel=4,bw_en=1):
        os.system('sudo ifconfig %s down'%iface)
        os.system('sudo iw dev %s set type monitor' % iface)
        os.system('sudo ifconfig %s up' % iface)
        if bw_en==0:
            os.system('sudo iw dev %s set channel %s HT20' % (iface,channel))
        else:
            os.system('sudo iw dev %s set channel %s HT40+' % (iface, channel))
        time.sleep(0.5)
