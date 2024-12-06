import baselib.plot.myplot as myplot
from baselib.test_channel.com import COM as com
from baselib.loglib.log_lib import *
from baselib.instrument.tester import tester
from hal.Init import HALS
from hal.common import MEM
from hal.wifi_api import WIFIAPI
import socket
from baselib.test_channel import (sock,server)
import random
import time
import numpy as np
import re
import subprocess
import rfglobal
from baselib.instrument import tester
import rftest.rflib.utility.iofunc as iofunc
from rftest.rflib.csv_report import csvreport
from hal.hwregister.hwi2c.all import *
from hal.hwregister.hwpbus.all import *
from rftest.rflib.utility import iofunc
from rftest.rflib.rfpll import rfpll
from rftest.rflib.pbus import pbus
from hal.rtc_debug import RTC_DEBUG

rate_bps_dict = rfglobal.rate_bps_dict
power_dict = rfglobal.power_dict

class WIFILIB(object):

    def __init__(self,comport, chipv='ESP32'):
        self.comport = comport
        self.chipv = chipv
##        self.hals = HALS(self.comport,self.chipv)
        self.wifiapi = WIFIAPI(self.comport,self.chipv)
        self.mem = MEM(self.comport,self.chipv)
        self.i2c = HWI2C(self.comport,self.chipv)
        self.rfpll = rfpll(self.comport,self.chipv)
        self.pbus = pbus(self.comport,self.chipv)
        self.hwpbus = HWPBUS(self.comport,self.chipv)
        self.rtc_debug = RTC_DEBUG(self.comport,self.chipv)

##    def fix_chan_set(self):
##        self.i2c_wic('rfrx', 'rfrx_lna_dboost', 0)
##        self.i2c_wic('rfrx', 'rfrx_mx_db', 2)
##        self.i2c_wic('rfrx', 'rfrx_lna_dcap', 2)
##        self.i2c_wic('rfrx', 'rfrx_vga_dcap', 11)

    def rfchsel(self,chan,cbw2040_cfg=0):
        return self.wifiapi.rfchsel(chan,cbw2040_cfg)

    def rfchsel_offset_esp32(self,freq_offset):
        return self.wifiapi.rfchsel_offset_esp32(freq_offset)

    def cbw40m_en(self,en=0):
        self.wifiapi.cbw40m_en(en)

    def ratecheck(self,rate_sym):
        if rate_sym in rfglobal.ratedic:
            result=rfglobal.ratedic[rate_sym];
        elif rate_sym.startswith(tuple(rfglobal.ratedic_11n)) == True:
            for rate in rfglobal.ratedic_11n:
                if rate_sym.startswith(rate) == True:
                    result=ratedic_11n[rate];
                    break
        else:
           result=-1;
           logwarn("Rate error, only rate available:");
           logwarn("1m,2m,2ms,2ml,5.5m,5.5ms,5.5ml,11m,11ms,11ml");
           logwarn("6m,9m,12m,18m,24m,36m,48m,54m,mcs0-7");
        return result;

    def lr_ratecheck(self,rate_sym):
        if rate_sym in rfglobal.lr_rate_ls:
           result=1;
        else:
           result=0;
        return result;

    def chan2freq(self,chan):
        chn_map={1: 2412, 2: 2417, 3: 2422,  4: 2427,  5: 2432,
	     6: 2437, 7: 2442, 8: 2447,  9: 2452, 10: 2457,
	    11: 2462,12: 2467,13: 2472, 14: 2484};
        if chan in chn_map:
            return chn_map[chan];
        else:
            print 'fail to find channel freq!';
            return [];

    def freq2chan(self,freq):
        freq_map ={2412:1,2417:2, 2422: 3,  2427:4,2432:5,
	     2437:6,  2442:7, 2447:8,  2452:9, 2457:10,
	    2462:11,2467:12, 2472:13, 2484:14}
        if freq in freq_map:
            return freq_map[freq];
        else:
            print 'fail to find channel freq!';
            return [];

    def get_ratelst(self,ratelst,rx_rate_option=''):
        #2,5.5,11 represent 2s,5.5s,11s
        rate_table=['1m','2m','2ms','2ml','5.5m','5.5ms','5.5ml','11m'  ,
    	       '11ms','11ml','6m','9m','12m','18m','24m','36m','48m','54m',
    	       'mcs0','mcs1','mcs2','mcs3','mcs4','mcs5','mcs6','mcs7',
               'mcs0_40','mcs1_40','mcs2_40','mcs3_40','mcs4_40','mcs5_40','mcs6_40','mcs7_40',
    	       'mcs0_sgi','mcs1_sgi','mcs2_sgi','mcs3_sgi','mcs4_sgi','mcs5_sgi','mcs6_sgi','mcs7_sgi',
               'mcs0_40_sgi','mcs1_40_sgi','mcs2_40_sgi','mcs3_40_sgi','mcs4_40_sgi','mcs5_40_sgi','mcs6_40_sgi','mcs7_40_sgi',
               'mcs0r','mcs1r','mcs2r','mcs3r','mcs4r','mcs5r','mcs6r','mcs7r',
               'lr0','lr1','lr2','lr3','lr4','lr5','lr6','lr7',
               'test'];
        #analyze the ratelst to get real test ratelist
        rate_list=[];

        if rx_rate_option=='':
            for rx_rate in ratelst:
                if rx_rate in rate_table:
                    rate_list.append(rx_rate);
                elif rx_rate=='a':
                    rate_list=rate_list+['6m','9m','12m','18m','24m','36m','48m','54m'];
                elif rx_rate=='b':
                    rate_list=rate_list+['1m','2ms','2ml','5.5ms','5.5ml','11ms','11ml','lr0','lr1','lr2','lr3','lr4','lr5','lr6','lr7'];
                elif rx_rate=='bl':
                    rate_list=rate_list+['1m','2ml','5.5ml','11ml'];
                elif rx_rate=='n':
                    rate_list=rate_list+['mcs0','mcs1','mcs2','mcs3','mcs4','mcs5','mcs6','mcs7'];
                elif rx_rate=='40m':
                    rate_list=rate_list+['mcs0_40','mcs1_40','mcs2_40','mcs3_40','mcs4_40','mcs5_40','mcs6_40','mcs7_40'];
                elif rx_rate=='rifs':
                    rate_list=rate_list+['mcs0r','mcs1r','mcs2r','mcs3r','mcs4r','mcs5r','mcs6r','mcs7r'];
                elif rx_rate=='ab':
                    rate_list=['1m','2ms','2ml','5.5ms','5.5ml','11ms','11ml','6m','9m','12m','18m','24m','36m','48m','54m'];
                elif rx_rate=='abn':
                    rate_list=['1m','2ms','2ml','5.5ms','5.5ml','11ms','11ml','6m','9m','12m','18m','24m','36m','48m','54m','mcs0','mcs1','mcs2','mcs3','mcs4','mcs5','mcs6','mcs7'];
                else:
                    logwarn('ratelst has unknown rate');
        else:
          for rx_rate in ratelst:
            rate_list.append(rx_rate+rx_rate_option);
        print rate_list;
        return rate_list;

    def rate2ht40(self,rate):
        if len(re.findall(r'.40',rate,re.M)) > 0:
            cbw40m = 1
        else:
            cbw40m =0
        return cbw40m

    def rate2shortGI(self, rate):
        if len(re.findall(r'.sgi',rate,re.M)) > 0:
            short_gi = 1
        else:
            short_gi = 0
        return short_gi

    def save_init_print(self,folder='',name_str=""):
        self.wifiapi.cmdstop()
        filetime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()));
        filename = self.get_filename(folder, 'init_print_%s'%name_str)
        file_w = '%s_%s.log'%(filename, filetime)
        f=open(file_w, 'w')
        result = self.wifiapi.init_print()
        f.write(result)
        f.close()

    def save_module_test(self,path_abs=0):
        self.wifiapi.cmdstop()
        filetime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()));

        if path_abs ==1:
            rfdata_path = './rftest/rfdata/'
            data_path1 = rfdata_path+'%s/'%('mod_test')
            if os.path.exists(data_path1) == False:
                os.mkdir(data_path1)

            filetime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()));
            mac = self.read_mac()

            gen_folder = '%s_%s'%(self.chipv,filetime[0:8])
            data_path2 = data_path1 +'%s/'%(gen_folder)
            if os.path.exists(data_path2) == False:
                os.mkdir(data_path2)
            filename = data_path2
            file_w = '%s_%s.log'%(filename+'/'+mac, filetime)
        else:
            filename = self.get_filename('mod_test', 'mod_test')
            file_w = '%s_%s.log'%(filename, filetime)

        f=open(file_w, 'w')
        result = self.wifiapi.esp_en_retest_print()
        f.write(result)
        f.close()


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

        gen_folder = '%s_%s_%s'%(self.chipv, mac, filetime[0:8])
        data_path2 = data_path1 +'%s/'%(gen_folder)
        if os.path.exists(data_path2) == False:
            os.mkdir(data_path2)

        fname = '%s_%s_%s'%(file_name, self.chipv, mac)
        outfile_name = data_path2 + fname

        if sub_folder != '':
            gen_folder = '%s_%s'%(sub_folder,filetime[0:8])
            sub_path = data_path2+'%s/'%(gen_folder)
            if os.path.exists(sub_path) == False:
                os.mkdir(sub_path)

            outfile_name = sub_path + file_name

        return outfile_name


    def read_mac(self):
        mac = self.wifiapi.esp_origin_mac()
        mac = mac.replace('\n','').replace('\r','')
        mac = mac.split(":")
        mac_s = '0x'
        for i in range(1, len(mac)):
            mac_s += '%s'%mac[i]
        print mac_s
        return mac_s

    def cmdstop(self, print_err=0):
        result_data = self.wifiapi.cmdstop()
        result_data_s = result_data.split(';')
        if print_err==1:
            fname = self.get_filename('rx_err_print', 'rx_err_print')
            csvreport1 = csvreport(fname, '')
            result_data = result_data.replace('#', '\n')
            csvreport1.write_string(result_data)
        return result_data_s[0]

    def i2c_ri(self,block,addr):
        data_rd_str="self.i2c.%s.reg_addr_rd(%d)"%(block,addr)
        data_rd=eval(data_rd_str)
        return data_rd

    def i2c_ric(self,block,ctrl_name):
        data_rd_str="self.i2c.%s.%s"%(block,ctrl_name)
        data_rd=eval(data_rd_str)
        return data_rd

    def i2c_wi(self,block,addr,value):
        data_wr_str="self.i2c.%s.reg_addr_wr(%d, %d)"%(block,addr,value)
        data_wr=eval(data_wr_str)
        return data_wr

    def i2c_wic(self,block,ctrl_name,value):
        data_wr_str="self.i2c.%s.%s"%(block,ctrl_name)
        exec(data_wr_str+'=%d'%value)
        data_wr=eval(data_wr_str)
        return data_wr

##
##class WIFITX(object):
##
##    def __init__(self,comport,chipv='ESP32'):
##        self.comport = comport
##        self.chipv = chipv
##        self.wifitx_api = WIFITX_API(self.comport,self.chipv)
##        self.wificm_api = WIFICM_API(self.comport,self.chipv)
##        self.common = COMMON(self.comport,self.chipv)
##        self.mem = MEM(self.comport,self.chipv)

    def get_length_delay_mean(self,rate='mcs7'):
        '''
        set the diffrent duty cycle to meet average current at 140mA
        '''
        current = [360, 350, 340, 310, 280, 260]  #mA
        mean_current = 140.0  #mA
        rate_bps = rate_bps_dict[rate]
        rate_index=self.ratecheck(rate)
        power_index = power_dict[rate_index]

        ratio = []
        for i in range(0, 6):
            ratio.append((current[i]-110.0)/(mean_current-110.0))

        if(rate_index < 4):
            len_ext = 200   #11b long
        elif(rate_index <8):
    	   len_ext = 100   #11b short
        else:
    	   len_ext = 40    #11g/11n

        if(rate_index < 8):
            pocket_len = 600  #us, 1m: len_byte=50
        else:
    	   pocket_len = 166  #us

        len_byte = int((pocket_len - len_ext) * rate_bps / 8)
        delay = int((ratio[power_index] - 1) * pocket_len)

        loginfo('len=%d, delay=%d'%(len_byte, delay))
        return [len_byte, delay]


    def get_length_delay_duty(self,rate='mcs7',duty=0.1, time_us=0, length=0):
        '''
        set the duty cycle of tx packet,duty range(0,1]

        '''
        rate_bps = rate_bps_dict[rate]
        rate_index=self.ratecheck(rate)
        if(rate_index < 4):
    	   len_ext = 200   #11b long
        elif(rate_index <8):
    	   len_ext = 100   #11b short
        else:
    	   len_ext = 40    #11g/11n

        if time_us==0:
            if(rate_index< 8):
                pocket_len = 600  #us, 1m: len_byte=50
            else:
        	    pocket_len = 200  #us
        else:
            pocket_len = time_us

        if length==0:
            len_byte = int((pocket_len - len_ext) * rate_bps / 8)
        else:
            len_byte = length

        if rate_index < 16 and len_byte > 4095:
            len_byte = 4095
        elif rate_index >= 16 and len_byte > 12095:
            len_byte = 12095

        pocket_len = int(len_byte*8/rate_bps+len_ext)
        delay =int((pocket_len - pocket_len*duty)/duty) #5400  #us, 1m: len_byte=50
        loginfo('len=%d, delay=%d'%(len_byte, delay))
        return [len_byte, delay]

    def tx_contin_en(self,en=0):
        self.wifiapi.tx_contin_en(en)

    def set_dig_txdc(self, txdci=0, txdcq=0):
        if txdci < 0:
            txdci = 1024+txdci
        if txdcq < 0:
            txdcq = 1024+txdcq
        self.mem.wrm(0x600050d0,9,0,txdci)
        self.mem.wrm(0x600050d0,19,10,txdcq)

    def tx_cbw40m_en(self,en=0):
        self.wifiapi.tx_cbw40m_en(en)

    def force_txon(self,en=0):

        if self.chipv=="ESP8266":
            self.wifiapi.force_txon_ESP8266(en)
        else:
            if en==0:
                self.mem.wrm(0x600060a0, 11, 8, 0x2)
                self.mem.wrm(0x600060a0, 11, 8, 0)
                self.mem.wrm(0x600060a0, 17, 14, 0)
            else:
                self.mem.wrm(0x600060a0, 17, 14, 0xf)
                self.mem.wrm(0x600060a0, 11, 8, 0x2)
                self.mem.wrm(0x600060a0, 11, 8, 0xe)

    def txtone(self,tone1_en=1,freq1_mhz=2,tone1_att=0,tone2_en=0,freq2_mhz=0,tone2_att=0):
        if tone1_att < 0:
            tone1_att = (256 - tone1_att) & 0xff
        if tone2_att < 0:
            tone2_att = (256 - tone2_att) & 0xff
        if self.chipv != 'ESP8266':
            self.mem.wrm(0x600060a0, 17, 16, 3)  # force FE clock on
        self.wifiapi.txtone(tone1_en,freq1_mhz,tone1_att,tone2_en,freq2_mhz,tone2_att)

    def txtone_step(self,en1=1, step1=0, att1=0, en2=0, step2=0, att2=0):
        if step1<0:
            step1 += 4096
        if step2<0:
            step2 += 4096
        self.wifiapi.txtone_step(en1,step1,att1,en2,step2,att2)


    def stoptone(self):
        self.mem.wrm(0x600060a0, 17, 16, 0)
        self.wifiapi.stoptone(0)


    def test_txtone_pwr(self,atten,loop_num,mode=0,step=0, delay_us=10):
        if step<0:
            step += 4096
        return self.wifiapi.test_txtone_pwr(atten,loop_num,mode,step, delay_us)

    def wifiscwout(self,en=0,chan=1,backoff=0):
        self.wifiapi.wifiscwout(en,chan,backoff)

    def esp_tx(self,chan=1,ratenum=0x17,backoff=0):
        if type(ratenum) == str:
            ratenum = self.ratecheck(ratenum)
        self.wifiapi.esp_tx(chan,ratenum,backoff)

    def txpacket(self,txchan=1,rate_sym='mcs7', PackNum=0, cbw40=0, ht_dup=0, backoff_qdb=0, duty=0):
        self.wifiapi.cmdstop()
        if txchan>14:
            self.wifiapi.rfchsel(1,cbw40*2)
            self.rfpll.set_freq(txchan)
        else:
            self.wifiapi.rfchsel(txchan,cbw40*2)
        rate_index=self.ratecheck(rate_sym)
        if duty==0:
            [len_byte, delay] = self.get_length_delay_mean(rate_sym)
        else:
            [len_byte, delay] = self.get_length_delay_duty(rate_sym,duty, time_us=500)
##            [len_byte, delay] = self.get_length_delay_duty(rate_sym,duty)
        self.txout(rate_sym=rate_sym, PackNum=PackNum, PackLen =len_byte, cbw40=cbw40, ht_dup=ht_dup, backoff_qdb=backoff_qdb, frm_delay=delay)

    def txout(self,rate_sym, PackNum=0, PackLen=1025, cbw40=0, ht_dup=0, backoff_qdb=0, frm_delay=2000):
        self.wifiapi.cmdstop()
        rate_index=self.ratecheck(rate_sym)
        if backoff_qdb < 0:
            backoff_qdb = 256+backoff_qdb
##        loginfo("backoff_qdb=%d"%backoff_qdb)
        self.wifiapi.target_power_backoff(backoff_qdb)
        self.wifiapi.filltxpacket(0xa0000+PackLen,4,4)
        self.wifiapi.txstart(rate_index,PackNum,10,frm_delay,cbw40,ht_dup)

    def txtest(self, rate_sym, PackNum=0, PackLen=1024, cbw40=0, ht_dup=0, short_gi=0, backoff_qdb=0, frm_delay=1500, dis_cca=1):
        self.wifiapi.cmdstop()
        rate_index=self.ratecheck(rate_sym)
        print(rate_sym)
        lr_en=self.lr_ratecheck(rate_sym);

        if backoff_qdb < 0:
            backoff_qdb = 256+backoff_qdb
##        loginfo("backoff_qdb=%d"%backoff_qdb)

        self.wifiapi.target_power_backoff(backoff_qdb)
        self.wifiapi.filltxpacket(0xa0000+PackLen,4,4,short_gi=short_gi)
        self.wifiapi.txstart(rate_index,PackNum,10,frm_delay,cbw40,ht_dup,dis_cca,lr_en)

    def txout_new(self, txchan, rate_sym, PackNum=0, time_us=500, duty=0.1, backoff_qdb=0):
        rate_index=self.ratecheck(rate_sym)
        if backoff_qdb < 0:
            backoff_qdb = 256+backoff_qdb

        cbw40 = self.rate2ht40(rate_sym)
        short_gi = self.rate2shortGI(rate_sym)

        if txchan>14:
            self.wifiapi.rfchsel(1,cbw40*2)
            self.rfpll.set_freq(txchan)
        else:
            self.wifiapi.rfchsel(txchan,cbw40*2)

        loginfo('cbw40=%d, short_gi=%s'%(cbw40, short_gi))

        [len_byte, frm_delay] = self.get_length_delay_duty(rate_sym, duty, time_us)
        print  [len_byte, frm_delay]
        self.wifiapi.target_power_backoff(backoff_qdb)
        self.wifiapi.filltxpacket(0xa0000+len_byte,28,4,short_gi=short_gi)
        self.wifiapi.txstart(rate_index,PackNum,10,frm_delay,cbw40,0)


    def force_tx_gain_init(self, chan=1, rate='mcs7',pa_gain=0x5f,bb_gain=0x120,dig_atten=20):

        self.wifiapi.cmdstop()
        cbw40m = self.rate2ht40(rate)

        if chan>14:
            self.wifiapi.rfchsel(1,0)
            if self.chipv == 'CHIP723' or self.chipv == 'CHIP724' :
                self.wifiapi.phy_set_freq(chan)
            else:
                self.rfpll.set_freq(chan)
        else:
            self.wifiapi.rfchsel(chan,cbw40m*2)
        self.wifiapi.set_tx_gain(pa_gain, bb_gain)
        self.wifiapi.set_tx_dig_gain(1,(256-dig_atten)) #256-bk

        if self.chipv == 'CHIP724':
            self.i2c.bias.dreg_2p2 = 0
            self.txiq_set(1,0,0)

        [len_byte, delay] = self.get_length_delay_duty(rate,0.2)
        self.txout(rate_sym=rate, PackNum=0, PackLen =len_byte, cbw40=cbw40m, ht_dup=0, backoff_qdb=0, frm_delay=delay)

    def txp_force_gain(self, chan=1, rate='mcs7', pa_gain=0x5f, bb_gain=0x120, dig_atten=24, txiq_gain=0, txiq_phase=0):
        self.wifiapi.cmdstop()
        cbw40m = self.rate2ht40(rate)
        if chan <=14:
            self.wifiapi.rfchsel(chan,cbw40m)
        else:
            freq= chan
            if self.chipv =="CHIP724":
                self.wifiapi.phy_set_freq(freq)
            else:
                self.rfpll.set_freq(freq)
        self.wifiapi.set_tx_gain(pa_gain, bb_gain)
        self.wifiapi.set_tx_dig_gain(1,(256-dig_atten)) #256-bk
 ##        self.txiq_set(1,txiq_gain,txiq_phase)
        [len_byte, delay] = self.get_length_delay_duty(rate,0.2)
        self.txout(rate_sym=rate, PackNum=0, PackLen =len_byte, cbw40=cbw40m, ht_dup=0, backoff_qdb=0, frm_delay=delay)


    def txp_force_gain_debug(self, sel=0,chan=1, rate='mcs7', pa_gain=0x5f, bb_gain=0x120, dig_atten=24, txiq_gain=0, txiq_phase=0):
        self.wifiapi.cmdstop()
        cbw40m = self.rate2ht40(rate)
        self.wifiapi.rfchsel(chan,cbw40m)

        self.wifiapi.set_tx_gain(pa_gain, bb_gain)
        self.wifiapi.set_tx_dig_gain(1,(256-dig_atten)) #256-bk
        if sel==0:
            self.i2c.rftx.PA2G_ICT_STG0_CGM =2#
            self.i2c.rftx.PA2G_ICT_STG1=8#
            self.i2c.rftx.PA2G_ICT_STG1_CGM=10
            self.i2c.rftx.PA2G_STG1_SEL_ICGM=1
            self.i2c.rftx.PA2G_STG1_SEL_ICGM_N=1
            self.i2c.rftx.PA2G_VCT_CSC_STG0=10
            self.i2c.rftx.PA2G_VCT_CSC_STG1=4
            self.i2c.bias.cgm_bias=2
            self.i2c.bias.cgm_bias=2
            self.i2c.bias.cp1p6_dreg=7
            self.i2c.bias.cp1p2_dreg=7
            self.i2c.bias.dres12k=7
            self.i2c.bias.cp1p1_pvt_reg=7
        elif sel==1:

##            self.i2c.rftx.PA2G_ICT_STG0_CGM =8#
##            self.i2c.rftx.PA2G_ICT_STG1=8#
##            self.i2c.rftx.PA2G_ICT_STG1_CGM=10
##            self.i2c.rftx.PA2G_STG1_SEL_ICGM=0
##            self.i2c.rftx.PA2G_STG1_SEL_ICGM_N=1
##            self.i2c.rftx.PA2G_VCT_CSC_STG0=12
##            self.i2c.rftx.PA2G_VCT_CSC_STG1=4
####            self.i2c.bias.cgm_bias=0
##            self.i2c.rftx.PA2G_ICT_STG0_CGM =2#
##            self.i2c.rftx.PA2G_ICT_STG1=8#
##            self.i2c.rftx.PA2G_ICT_STG1_CGM=10
##            self.i2c.rftx.PA2G_STG1_SEL_ICGM=1
##            self.i2c.rftx.PA2G_STG1_SEL_ICGM_N=1
##            self.i2c.rftx.PA2G_VCT_CSC_STG0=10
##            self.i2c.rftx.PA2G_VCT_CSC_STG1=4
##            self.i2c.rftx.PA2G_VCT_CSC_STG2=2
##
##            self.i2c.bias.cp1p6_dreg=0
##            self.i2c.bias.cp1p2_dreg=6
            self.i2c.bias.dres12k=13
            self.i2c.bias.cgm_bias=1
##            self.i2c.bias.cp1p1_pvt_reg=7



##        self.txiq_set(1,txiq_gain,txiq_phase)
        [len_byte, delay] = self.get_length_delay_duty(rate,0.2)
        self.txout(rate_sym=rate, PackNum=0, PackLen =len_byte, cbw40=cbw40m, ht_dup=0, backoff_qdb=0, frm_delay=delay)


    def tx_rc_filter(self, en=0,txdc_i=-53,txdc_q=-14):
        self.i2c.bbtop.enlb    = en
        self.i2c.rfrx.LB_MODE  = en
        self.i2c.rftx.LB_EN    = en
        self.i2c.rftx.LB_EN_IQ = en
        self.i2c.rftx.LB_GCT   = en
        if en==1:
##            self.pbus.pbus_wr('bb','en1', 0x170)
            self.wifiapi.tx_pbus_set(rxon_bb1=0x70)
            self.set_dig_txdc(txdc_i, txdc_q)
        else:
##            self.pbus.pbus_wr('bb','en1', 0x7c)
            self.wifiapi.tx_pbus_set(rxon_bb1=0x7c)
            self.set_dig_txdc(txdci=0, txdcq=0)

##class WIFIRX(object):
##
##    def __init__(self,comport,chipv='ESP32'):
##        self.comport = comport
##        self.chipv = chipv
##        self.wifirx_api = WIFIRX_API(self.comport,self.chipv)
##        self.wificm_api = WIFICM_API(self.comport,self.chipv)
##        self.common = COMMON(self.comport,self.chipv)
##        self.mem = MEM(self.comport,self.chipv)

    def rf_tune(self):
        pll_cap = self.i2c.rfpll.or_pll_cap
        lna_cap = (pll_cap*24 - 453 + 113)/227
        vga_cap = (pll_cap*23 - 74 + 103)/207

        if(lna_cap>0xf):
            lna_cap=0xf
        if(lna_cap<0):
            lna_cap=0x0

        if(vga_cap>0xf):
            vga_cap=0xf
        if(vga_cap<0):
            vga_cap=0x0
        self.i2c.rfrx.rfrx_lna_dcap=lna_cap
        self.i2c.rfrx.rfrx_vga_dcap=vga_cap

    def get_rx_tone_pwr(self,rx_freq_mhz=5, rx_freq_cmp_mult20=0, gain_force=0, gain=40):
        rx_freq_cfg = rx_freq_mhz + rx_freq_cmp_mult20/20.0;#rx_freq_mhz*64/5+rx_freq_cmp;
        loginfo(rx_freq_cfg);
        self._mem.wrm(0x6001c02c,31,23,((gain<<1) | gain_force)) #force gain
        result=self.wifiapi.get_rx_tone_pwr(rx_freq_cfg)
        rs=result.split(',');
        return [(int(data,10)/16.0) for data in rs];

    def get_rx_tone_pwr_scan(self,rx_freq_mhz=5, gain_force=0, gain=40, scan_range=10):
        rx_pwr=0;
        rx_freq_cmp=0;
        for shift in range(-scan_range,scan_range):
           rx_pwr_new=self.get_rx_tone_pwr(rx_freq_mhz, shift, gain_force, gain);
           if(rx_pwr_new[1]>rx_pwr):
              rx_pwr=rx_pwr_new[1];
              rx_freq_cmp=shift;
           print (shift,(rx_freq_mhz + shift/20.0), rx_pwr_new[0], rx_pwr_new[1]);

        return rx_freq_cmp;

    def rxstart(self,rate_sym, peint_err_code=0,rssi_data_base=0):
        self.wifiapi.rxstart((rssi_data_base<<24)|(peint_err_code<<17)|self.ratecheck(rate_sym))

    def esp_rx(self,chan,rate_sym,peint_err_code=0,rssi_data_base=0):
        #rate_index=self.ratecheck(rate_sym)
        self.wifiapi.esp_rx(chan,(rssi_data_base<<24)|(peint_err_code<<17)|self.ratecheck(rate_sym))

    def rxdc_cal(self, print_en=0):
        return self.wifiapi.rxdc_cal(print_en)

    def rx_force_gain(self, en=0, gain=20, bt_mode=0):
        if self.chipv=="ESP8266":
            self.mem.wrm(0x60009a34, 9, 0, ((gain<<2) | (en<<0))) #force gain
        else:
            if bt_mode==1:
                if self.chipv=="CHIP724":
                    self.mem.wrm(0x6001c02c, 31, 23, (((gain)<<1) | en));  #set gain
                else:
                    self.mem.wrm(0x6001c02c, 31, 23, (((gain+128)<<1) | en));  #set gain
            else:
                self.mem.wrm(0x6001c02c, 31, 23, ((gain<<1) | en));  #set gain

    def btrx_force_gain(self, max_gain=10, min_gain=10):
        self.mem.wrm(0x6001c0a4, 29, 22, min_gain) #bt rx min gain
        self.mem.wrm(0x6001c0a4, 21, 15, max_gain) #bt rx max gain
        self.mem.wrm(0x6001c02c, 14, 8, max_gain) #wifi max gain
        self.mem.wrm(0x6001c02c, 21, 15, min_gain) #wifi min gain
        self.mem.wrm(0x6001c1a4,25,19, min_gain)  #bt init gain
        self.mem.wrm(0x6001c094,8,2, min_gain)  #wifi init gain

    def rx_max_gain(self, bt_mode=0):
        if self.chipv=="ESP8266":
            max_gain = self.mem.rdm(0x60009b48, 6, 0)
        else:
            if bt_mode==1:
                max_gain = self.mem.rdm(0x6001c0a4, 21, 15)
            else:
                max_gain = self.mem.rdm(0x6001c02c, 14, 8)
        return max_gain

    def GetGoodPackNum(self,result):
        return result[1];

    def GetDesirePackNum(self,result):
        return result[3];

    def GetRssi(self,result):
        return result[5];

    def GetNoise(self,result):
        return result[7];

    def GetGain(self,result):
        return result[9];

    def GetTotErr(self,result):
        return result[11];

    def GetFcsErr(self,result):
        return result[13];

    def GetFreqoff(self,result):
        if len(result)>=16 and type(result[15])==str:
            return result[15];
        else:
            return 0

    def GetRssiMin(self,result):
        if len(result) == 20:
            return result[17]
        else:
            return 0


    def GetRssiMax(self,result):
        if len(result) == 20:
            return result[19]
        else:
            return 0


    def GetRssiBaseP5(self,result):
        if len(result) == 42:
            return result[-21]
        else:
            return 0

    def GetRssiBaseP4(self,result):
        if len(result) == 42:
            return result[-19]
        else:
            return 0

    def GetRssiBaseP3(self,result):
        if len(result) == 42:
            return result[-17]
        else:
            return 0

    def GetRssiBaseP2(self,result):
        if len(result) == 42:
            return result[-15]
        else:
            return 0

    def GetRssiBaseP1(self,result):
        if len(result) == 42:
            return result[-13]
        else:
            return 0

    def GetRssiBaseN0(self,result):
        if len(result) == 42:
            return result[-11]
        else:
            return 0

    def GetRssiBaseN1(self,result):
        if len(result) == 42:
            return result[-9]
        else:
            return 0

    def GetRssiBaseN2(self,result):
        if len(result) == 42:
            return result[-7]
        else:
            return 0

    def GetRssiBaseN3(self,result):
        if len(result) == 42:
            return result[-5]
        else:
            return 0

    def GetRssiBaseN4(self,result):
        if len(result) == 42:
            return result[-3]
        else:
            return 0

    def GetRssiBaseN5(self,result):
        if len(result) == 42:
            return result[-1]
        else:
            return 0

    def rxresult(self, result_data):
        result=str.split(result_data)
        DesirePackNum=int(self.GetDesirePackNum(result));
        gain=int(self.GetGain(result));
        rssi=int(self.GetRssi(result));
        noise=int(self.GetNoise(result));
        err=int(self.GetTotErr(result));
        err2=int(self.GetFcsErr(result));
        freqoff=int(self.GetFreqoff(result));
        rssi_min =0#int(self.GetRssiMin(result));
        rssi_max =0#int(self.GetRssiMax(result));
##        rssi_base_p5=int(self.GetRssiBaseP5(result))
##        rssi_base_p4=int(self.GetRssiBaseP4(result))
##        rssi_base_p3=int(self.GetRssiBaseP3(result))
##        rssi_base_p2=int(self.GetRssiBaseP2(result))
##        rssi_base_p1=int(self.GetRssiBaseP1(result))
##        rssi_base_n0=int(self.GetRssiBaseN0(result))
##        rssi_base_n1=int(self.GetRssiBaseN1(result))
##        rssi_base_n2=int(self.GetRssiBaseN2(result))
##        rssi_base_n3=int(self.GetRssiBaseN3(result))
##        rssi_base_n4=int(self.GetRssiBaseN4(result))
##        rssi_base_n5=int(self.GetRssiBaseN5(result))

        return [DesirePackNum, gain, rssi, noise, err, err2,freqoff,rssi_min,rssi_max]
        #return [DesirePackNum, gain, rssi, noise, err, err2,freqoff,rssi_min,rssi_max,rssi_base_p5,rssi_base_p4,rssi_base_p3,rssi_base_p2,rssi_base_p1,rssi_base_n0,rssi_base_n1,rssi_base_n2,rssi_base_n3,rssi_base_n4,rssi_base_n5]

    def noise_check(self, chan_en=0, chan=14, cbw2040_cfg=0, force_gain_en=0, force_gain=70, check_level=7):

        if chan_en:
           if chan<15:
              self.rfchsel(chan,cbw2040_cfg);
              time.sleep(0.5);
           else:
              self.rfpll.reset();
              self.rfpll.set_freq(chan);
              self.restart_cal();

        data=self.mem.rd(0x6001c02c);
        data2=self.mem.rd(0x6001c018);
        self.mem.wr(0x6001c02c,((data&0x007fffff) | (force_gain<<24) | (force_gain_en<<23)));
        time.sleep(0.5);

        self.mem.wrm(0x6001c018,2,0,check_level)  #cfg

        self.mem.wrm(0x6001c018,28,28,0) #auto_en
        self.mem.wrm(0x6001c018,23,23,0) #cal_en
        self.mem.wrm(0x6001c018,25,25,1) #clr
        self.mem.wrm(0x6001c018,25,25,0)
        self.mem.wrm(0x6001c018,23,23,1)
        time.sleep(0.5);

        while 1:
           status=self.mem.rdm(0x6001c018,24,24);
           if(status==0x1):
              break;

        noise = float(((self.mem.rd(0x6001c050)) & 0x3ff) -1024)/4.0

        self.mem.wr(0x6001c02c,((data&0x007fffff) | (force_gain<<24) | (0<<23)));
        noise_force = float(((self.mem.rd(0x6001c018)>>5) & 0x3ff) - 1024)*10/4.0
        loginfo("noise_force=%d\n"%noise_force)

        return noise

    def auto_noise_test(self, check_level=7, rc_shift_max=0,rc_in_max=-99,rc_in_min=-80):

        self.mem.wrm(0x6001c018,2,0,check_level)  #cfg
        self.mem.wrm(0x6001c018,23,23,1) #noise_cal
        self.mem.wrm(0x6001c018,28,28,1) #auto_en
        self.mem.wrm(0x6001c018,4,4,0) #hw_force_en
        self.mem.wrm(0x6001c018,3,3,1) #hw_upd_en
        self.mem.wrm(0x6001c130,26,26,1) #rc_filter_noise_en
        self.mem.wrm(0x6001c134,26,24,rc_shift_max) #rc_shift_max
        self.mem.wrm(0x6001c134,23,12,(rc_in_max*16+4096)) #rc_in_max
        self.mem.wrm(0x6001c134,11,0,(rc_in_min*16+4096)) #rc_in_min

        noise1 = float(((self.mem.rd(0x6001c050)) & 0x3ff) -1024)/4.0
        noise2 = float(((self.mem.rd(0x6001c018)>>5) & 0x3ff) -1024)/4.0
        noise3 = float(((self.mem.rd(0x6001c08c)>>0) & 0xfff) -4096)/16.0

        print "noise1=%2.2f, noise2=%2.2f, noise3=%2.2f"%(noise1, noise2, noise3)

    def noise_check_sweep(self):

        fname = self.get_filename('noise_check_sweep', 'noise_check_sweep')
        title = 'chan,gain,noise,noise_force\n'
        fw1=csvreport(fname, title)

        max_gain = int(self.rx_max_gain(0))
        force_gain_en = 1
        check_level = 7

        for chan in range(1,15):
            for force_gain in range(0,max_gain+1):
                if chan<15:
                  self.rfchsel(chan,0);
                  time.sleep(0.5);
                else:
                  self.rfpll.reset();
                  self.rfpll.set_freq(chan);
                  self.restart_cal();

                data=self.mem.rd(0x6001c02c);
                data2=self.mem.rd(0x6001c018);
                self.mem.wr(0x6001c02c,((data&0x007fffff) | (force_gain<<24) | (force_gain_en<<23)));
                time.sleep(0.5);

                self.mem.wrm(0x6001c018,2,0,check_level)  #cfg
                self.mem.wrm(0x6001c018,28,28,0) #auto_en
                self.mem.wrm(0x6001c018,23,23,0) #cal_en
                self.mem.wrm(0x6001c018,25,25,1) #clr
                self.mem.wrm(0x6001c018,25,25,0)
                self.mem.wrm(0x6001c018,23,23,1)
                time.sleep(0.5);

                while 1:
                   status=self.mem.rdm(0x6001c018,24,24);
                   if(status==0x1):
                      break;

                noise = float(((self.mem.rd(0x6001c050)) & 0x3ff) -1024)/4.0

                self.mem.wr(0x6001c02c,((data&0x007fffff) | (force_gain<<24) | (0<<23)));
                noise_force = float(((self.mem.rd(0x6001c018)>>5) & 0x3ff) - 1024)*10/4.0
                loginfo("chan=%d,gain=%d,noise=%d,noise_force=%d\n"%(chan,force_gain,noise,noise_force))
                fw1.write_data([chan,force_gain,noise,noise_force])

        return noise

    def dig_gain_clip(self,clip_val=0x0,clip_comp=5):
##        tx_gain_ctrl1 = self.mem.rd(0x60006004)
##        self.mem.wr(0x60006004,(tx_gain_ctrl1 & 0xffff00ff)| ((256-clip_val)<<8 & 0xff00))
        self.mem.wrm(0x60006000,9,2,clip_val)
        self.mem.wrm(0x60006000,26,26,1)
        self.mem.wr(0x6000614c, ((256-clip_val + clip_comp)<<8 & 0xff00))

    def write_dig_gain(self, gain0=0,gain1=0,gain2=0,gain3=0,gain4=0,gain5=0,gain6=0,gain7=0):
        self.mem.wr(0x60006004, (gain3<<24)|(gain2<<16)|(gain1<<8)|gain0)
        self.mem.wr(0x60006008, (gain7<<24)|(gain6<<16)|(gain5<<8)|gain4)

    def dig_gain_clip_722(self, dig_gain1=0, dig_gain2=-20):
        if dig_gain1<0:
            dig_gain1 += 256
        if dig_gain2<0:
            dig_gain2 += 256
        self.write_dig_gain(gain0=dig_gain1,gain1=dig_gain1,gain2=dig_gain1,gain3=dig_gain1,gain4=dig_gain1,gain5=dig_gain1,gain6=dig_gain1,gain7=dig_gain1)
        self.wifiapi.write_dac_gain2(dac_gain2_en=1, gain0=dig_gain2,gain1=dig_gain2,gain2=dig_gain2,gain3=dig_gain2,gain4=dig_gain2,gain5=dig_gain2,gain6=dig_gain2,gain7=dig_gain2)

    def cable_lose_cal(self, chan=14, rx_power=-58, cable_att=30, iqv_no=1, fine_cal=1):
        rx_rate = '36m'
        packnum = 100
        self.rx_force_gain(0, 0, 0)
        self.rfchsel(chan)
        rx_freq = self.chan2freq(chan)
        mytester=tester.tester(rx_freq, rx_power,rx_rate,1,iqv_no,'source',cable_att)
        mytester.sigout(rx_freq,rx_power,cable_att,rx_rate,packnum,iqv_no);
        power = rx_power
        lost_a = 0
        cable_lost = cable_att+lost_a
        for i in range(0,5):
            self.rxstart(rx_rate)
            time.sleep(0.01)
            mytester.trig_wave(1)
            result_data=self.cmdstop()
            [DesirePackNum, gain, rssi, noise, err, err2, freqoff, rssi_min, rssi_max]=self.rxresult(result_data)
            rx_rssi=rssi/10.0;
            lost = rx_power - rx_rssi
            loginfo('chan=%d,pwr=%2.2f, rssi=%2.2f, num=%d, noise=%d, lost=%2.2f, att=%2.2f'%(chan, power, rx_rssi, DesirePackNum, noise, lost, cable_att+lost_a))
            if(lost<=0.2) and (lost>=-0.2):
                break
            lost_a += lost
            cable_lost = cable_att+lost_a
            power = rx_power + lost_a
            mytester.set_pwr(power,0,iqv_no,'source')
##        loginfo(lost_a)
        if fine_cal==1:
            pwr_sum = 0
            pwr_i = 0
            step = -0.2
            si = 0
            self.rx_force_gain(1, gain/10, 0)
            for i in range(11):
                pwr_in = power+si*step
                mytester.set_pwr(pwr_in,0,iqv_no,'source')
                self.rxstart(rx_rate)
                time.sleep(0.01)
                mytester.trig_wave(1)
                result_data=self.cmdstop()
                [DesirePackNum, gain, rssi, noise, err, err2, freqoff, rssi_min, rssi_max]=self.rxresult(result_data)
                rx_rssi=rssi/10.0;
                lost = rx_power - rx_rssi
                loginfo('%d chan=%d,pwr=%2.2f,si=%d,step=%d,rssi=%2.2f, num=%d, lost=%2.2f, att=%2.2f'%(i,chan, pwr_in, si, step,rx_rssi, DesirePackNum, lost, cable_att+lost_a))

                if lost > 0.2:
                    step = 0.2
                    si = 1
                elif step == 0.2 and lost < -0.2:
                    break
                else:
                    si += 1

                if(lost<=0.2) and (lost>=-0.2):
                    pwr_sum += pwr_in
                    pwr_i += 1

            self.rx_force_gain(0, gain/10, 0)
            pwr_mean = pwr_sum/pwr_i
            lost_a = pwr_mean - rx_power
##            loginfo(pwr_mean, lost_a)

        mytester.gen_switch('OFF',1)
        cable_lost = cable_att+lost_a
        return [cable_lost,rx_rssi]

    def rx_chan_noise(self, rx_gain=68, chan=1):
        self.rx_force_gain(1, rx_gain, 0)
        noise = self.wifiapi.rx_chan_noise(chan)
        self.rx_force_gain(0, rx_gain, 0)
        return noise

    def get_rx_noise(self, rx_gain=68):
        self.rx_force_gain(1, rx_gain, 0)
        noise = self.wifiapi.rx_chan_noise_all()
        self.rx_force_gain(0, rx_gain, 0)
        return noise

    def get_rx_cable_lost(self,iqv_no=1, chan_m=[14],name_str=''):

        title = 'channel, cable_att, gain_comp, noise,noise_debug, noise_comp, cable_lost\n'
        fname = self.get_filename('get_rx_calbe_lost_%s'%name_str, 'cable_cal_%s'%name_str)
        csvreport1 = csvreport(fname, title)
        logsetlevel('I')
        if self.chipv=="CHIP724":
            noise_ref=-96.2
            rx_gain =68
            rx_power = -68
        elif self.chipv=="CHIP723":
            noise_ref=-95.6
            rx_gain = 70
            rx_power = -68
        else:
            noise_ref=-95.2
            rx_gain = 70
            rx_power =-70

        cable_lost = 30

        [cable_lost,rx_rssi] = self.cable_lose_cal(chan=14, rx_power=rx_power, cable_att=cable_lost, iqv_no=iqv_no, fine_cal=0)

        if self.chipv=='CHIP724' or self.chipv=='CHIP723':
            noise_min = self.get_rx_noise(rx_gain)
            gain_comp = self.rx_gain_comp()
        else:
            noise_min = 0
            gain_comp = [0]

        self.wifiapi.rssi_min_max_print()
        cable_list = []

        for chan in chan_m:

            [cable_att,rx_rssi] = self.cable_lose_cal(chan=chan, rx_power=rx_power, cable_att=cable_lost, iqv_no=iqv_no, fine_cal=1)

            loginfo ('chan=%d, cable_att=%2.2f'%(chan,cable_att))
            cable_lost=cable_att

            if self.chipv=='CHIP724' or self.chipv=='CHIP723':
                noise = noise_min
##                noise = self.rx_chan_noise(rx_gain, chan)
            else:
                noise = self.noise_check(1, chan, 0, 1, rx_gain)

##            loginfo("noise=%2.2f, gain_comp=%d"%(noise, gain_comp[chan-1]))

            noise_comp = noise - noise_ref
            noise_debug = noise_comp

            if self.chipv == "CHIP724" and noise_comp < 0 :
                noise_comp = noise_comp*3

            if self.chipv == 'CHIP723' and noise_comp < -0.1:
                noise_comp -= 0.5

            if noise_comp>2 :
                noise_comp = 2
            elif noise_comp<-2:
                noise_comp = -2
            print 'noise_comp=%2.2f'%noise_comp
            if rx_rssi==0:
                cable_lost = 200
##            elif -95.5 <= noise <= -94.5:
##                cable_lost = cable_lost
            else:
                 cable_lost += noise_comp

            loginfo('cable_lost=%2.2fdB'%(cable_lost))

            csvreport1.write_data([chan,cable_att,gain_comp[chan], noise, noise_debug,noise_comp, cable_lost])
            cable_list.append(cable_lost)
        loginfo(cable_list)
        return cable_list

    def txpwr_track_en(self,track_en=0,correct_en=0,print_en=0):
        self.wifiapi.txpwr_track_en(track_en,correct_en,print_en)

    def i2c_block_get(self):
        if self.chipv=='CHIP723' or self.chipv=="CHIP724":
            block_m = {'bias','bbpll','rfrx','rftx','bbtop','ckgen','rfpll','rfpll_sdm','apll','ulp','sar'}
        elif self.chipv=='CHIP722':
            block_m = {'bias_marlin3','bbpll','rfrx','rftx','bbtop','ckgen','rfpll','rfpll_sdm','apll','ulp'}
        elif self.chipv=='ESP32':
            block_m = {'bias','bbpll','rfrx','rftx','bbtop','ckgen','xtal','rfpll','rfpll_sdm','apll'}
        elif self.chipv=='ESP8266':
            block_m = {'bias','bbpll','rfrx','rftx','bbtx','bbrx','ckgen','xtal','rfpll','rfpll_sdm','dig_fe','dig_inf','saradc'}

        else:
            block_m = {'bias','bbpll','rfrx','rftx','bbtop','ckgen','rfpll','rfpll_sdm','apll','ulp','sar'}

        return block_m

    def i2c_regdict_get(self):
        i2c_table = './docs/common/i2c_table_%s.xlsm'%self.chipv
        i2c_regdict = dict()
        test_m = self.i2c_block_get()
        for block in test_m:
            print block
            i2c_regdict[block] = iofunc.csv2regdict(i2c_table, block, dict_type='ctrl')
        return i2c_regdict

    def i2c_clk_sel(self, clk_sel=1):
        if self.chipv=='CHIP722':
            if clk_sel==0:
                self.mem.wrm(0x6000e048, 16, 16, 1)  #1
                self.mem.wrm(0x6000e020, 6, 4, 0)  #1,2,3
                self.mem.wrm(0x6000e024, 6, 4, 0)  #1,2,3
            else:
                self.mem.wrm(0x6000e048, 16, 16, 0)
                self.mem.wrm(0x6000e020, 6, 4, clk_sel-1)
                self.mem.wrm(0x6000e024, 6, 4, clk_sel-1)
        elif self.chipv=='ESP32':
            self.mem.wrm(0x6000e020, 6, 4, clk_sel)
            self.mem.wrm(0x6000e024, 6, 4, clk_sel)
            self.mem.wrm(0x6000e028, 6, 4, clk_sel)
            self.mem.wrm(0x6000e02c, 6, 4, clk_sel)
            self.mem.wrm(0x6000e030, 6, 4, clk_sel)


    def filter_bw_set(self, bw0=0, bw1=0, bw2=0, bw3=0):
        self.i2c.bbtop.filter_wifitx0_dcap_lq=bw0
        self.i2c.bbtop.filter_wifitx0_dcap_hq=bw0
        self.i2c.bbtop.filter_wifitx1_dcap_lq=bw1
        self.i2c.bbtop.filter_wifitx1_dcap_hq=bw1
        self.i2c.bbtop.filter_wifitx2_dcap_lq=bw2
        self.i2c.bbtop.filter_wifitx2_dcap_hq=bw2
        self.i2c.bbtop.filter_wifitx3_dcap_lq=bw3
        self.i2c.bbtop.filter_wifitx3_dcap_hq=bw3

    def dac_rate_test(self, bbdac_320=0, dig_320=0):
        self.i2c.bbpll.div_dac=bbdac_320  #0:160MHz,1:320MHz
        self.mem.wrm(0x600050ec, 27, 27, dig_320)

    def adc_sync_test(self, way1_en=0):
        self.mem.wrm(0x600050d0, 24, 24, way1_en)  #1:way1, 0: auto detect
        self.mem.rdm(0x600050d0, 26, 26)  #way1, rx_local_edge
        self.mem.rdm(0x600050d8, 27, 27)  #rx_edge_sel

    def txon_delay(self, paon_delay=240, btx_wait=63, ntx_wait=51, ntx40_wait=61, stf_num=3):
        if self.chipv=='ESP32':
            self.mem.wrm(0x60006048, 15, 8, paon_delay)  #paon delay
            self.mem.wrm(0x6001d000, 28, 23, btx_wait)  #11b start delay
            self.mem.wrm(0x6001d000, 22, 17, ntx_wait)  #ofdm start delay
            self.mem.wrm(0x6001c400, 18, 16, stf_num)  #premble num
        elif self.chipv=="CHIP722" or self.chipv=="CHIP723" :
            self.mem.wrm(0x60006048, 15, 8, paon_delay)  #paon delay
            self.mem.wrm(0x6001d06c, 29, 20, btx_wait)  #11b start delay
            self.mem.wrm(0x6001d06c, 9, 0, ntx_wait)  #ofdm start delay
            self.mem.wrm(0x6001d06c, 19, 10, ntx40_wait)  #ofdm start delay
            self.mem.wrm(0x6001c400, 18, 16, stf_num)  #premble num

    def test_pvt(self, dbias=4, pvt_en_res=1, pvt_delay=400):
        self.mem.wrm(0x6000807c,13,11,dbias) #dig_dbias
        self.mem.wrm(0x6000e0f8,9,0,pvt_delay) #pvt count delay, 0.025us*pvt_delay
        self.mem.wrm(0x6000e0f8,11,11,pvt_en_res) #pvt en res
        if self.chipv=='CHIP722':
            self.mem.wrm(0x60008034,26,26,1) #pvt xpd
        elif self.chipv=='ESP32':
            self.mem.wrm(0x60008030,26,26,1) #pvt xpd
        self.mem.wrm(0x6000e0f8,10,10,0) #pvt start
        self.mem.wrm(0x6000e0f8,10,10,1) #pvt start
        while (self.mem.rdm(0x6000e0f8, 31, 31) == 0):  #wait done
            time.sleep(0.01)
        count = self.mem.rdm(0x6000e0f8, 29, 16)
        self.mem.wrm(0x60008030,26,26,0) #pvt xpd
        print 'count=%d'%count

    def bt_tx_force(self, en=1):
        if en==1:
            self.mem.wrm(0x6001c080,7,6,3) #force bt_mode
            self.mem.wrm(0x600060a0,11,8,0xe) #force dac on
        else:
            self.mem.wrm(0x6001c080,7,6,0) #force bt_mode
            self.mem.wrm(0x600060a0,11,8,0x0)
##        if bt_mode>0:
####            self.mem.wrm(0x6001c080,7,6,3) #force bt_mode
##            self.mem.wrm(0x60035144,31,28,0xf) # coex_timer
##            self.mem.wrm(0x60035144,27,24,0xf) # coex_timer pti
##            self.mem.wrm(0x60035138,5,3,1) #GPIO bt active sel
####            self.mem.wrm(0x60004218,6,6,1) #GPIO 49 in invert
####            self.mem.wrm(0x60011004,11,10,3) #force bt_tx
##            self.mem.wrm(0x600060a0,11,10,3) #force tx on
##        else:
####            self.mem.wrm(0x6001c080,7,6,0) #force bt_mode
##            self.mem.wrm(0x60035144,31,28,0x0) #force coex_timer
##            self.mem.wrm(0x60035138,5,3,0) #GPIO bt active sel
####            self.mem.wrm(0x60035144,27,24,0xf) #force coex_timer pti
####            self.mem.wrm(0x60011004,11,10,0) #force bt_tx
##            self.mem.wrm(0x600060a0,11,10,0) #force tx on

    def bt_rx_force(self, en=1):
        if en==1:
            self.mem.wrm(0x6001c080,7,6,3) #force bt_mode
            self.mem.wrm(0x600060a0,11,8,0x2) #force adc on
            self.mem.wrm(0x600060a0,11,8,0x3) #force adc on
        else:
            self.mem.wrm(0x6001c080,7,6,0) #force bt_mode
            self.mem.wrm(0x600060a0,11,8,0x2) #force adc on
            self.mem.wrm(0x600060a0,11,8,0x3) #force adc on
            self.mem.wrm(0x600060a0,11,8,0x0) #force adc on
##        if en==1:
##            self.mem.wrm(0x60035144,31,28,0xf) # coex_timer
##            self.mem.wrm(0x60035144,27,24,0xf) # coex_timer pti
##            self.mem.wrm(0x60035138,5,3,1) #GPIO bt active sel
####            self.mem.wrm(0x6001c080,7,6,3) #force bt_mode
####            time.sleep(0.1)
####            self.mem.wrm(0x60011018,31,31,1) #force bt_rx_en
##            self.mem.wrm(0x60011004,9,8,3) #force bt_rx
##        else:
##            self.mem.wrm(0x60035144,31,28,0x0) #force coex_timer
##            self.mem.wrm(0x60035138,5,3,0) #GPIO bt active sel
####            self.mem.wrm(0x6001c080,7,6,0) #force bt_mode
####            self.mem.wrm(0x60011018,31,31,0) #force bt_rx_en
##            self.mem.wrm(0x60011004,9,8,0) #force bt_rx

    def loopback_mode(self, loop_mode=2, pagain=0xf, bbgain=0x20, tone_step=64, tone_att=40):
        self.txtone_step(0, tone_step, tone_att)
        self.mem.wrm(0x600060a0, 17, 14, 0xf)  #force txon rxon
        self.pbus.pbus_debugmode()
        self.mem.wrm(0x6000607c, 30, 30, 0)  #fe loopback en

        if loop_mode == 1: #digital interface loop
            self.mem.wrm(0x600050d0, 28, 28, 1)  #ana inf loopback en
            self.mem.wrm(0x600050d8, 25, 25, 0)  #tx iq swap
        elif loop_mode == 2: # dac, filt, adc loop
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
            self.hwpbus.RFRX1.EN1 = 0x105
            self.hwpbus.RFTX1.EN1 = 0x7f
            self.hwpbus.RFTX2.EN1 = pagain
            self.hwpbus.BB1.EN1   = 0x1f9
            self.hwpbus.BB1.EN2   = bbgain
            self.i2c.bbtop.enlb    = 1
            self.i2c.rfrx.LB_MODE  = 0
##            self.i2c.rftx.LB_EN    = 0
##            self.i2c.rftx.LB_EN_IQ = 0
##            self.i2c.rftx.LB_GCT   = 0

        self.pbus.set_dco(0x100, 0x100, 0x100, 0x100)
        self.rxdc_cal()
        self.txtone_step(1, tone_step, tone_att)

    def set_freq_mem(self, wr_en=0, freq=12, cap=93):
        addr = freq*3
        self.mem.wrm(0x6000e0c4, 7, 0, addr)
        r_data = self.mem.rd(0x6000e0c0)   #read mem data
        old_cap = r_data & 0xff
        if(wr_en==1):
            w_data = (r_data & 0xffffff00) + cap
            self.mem.wr(0x6000e148, w_data)    #write data
            self.mem.wrm(0x6000e0c4, 9, 9, 1)  #write enable
            self.mem.wrm(0x6000e0c4, 9, 9, 0)
            r_data = self.mem.rd(0x6000e0c0)   #read mem data
            new_cap = r_data & 0xff
            print 'freq=%d, old_cap=%d, new_cap=%d'%(freq, old_cap, new_cap)
        else:
            print 'freq=%d, old_cap=%d'%(freq, old_cap)

    def wifi_pti_set(self, pti=0xf):
        self.mem.wrm(0x60035128, 11, 8, pti)

    def noise_auto_test(self, auto_init=1):
        if auto_init==1:
            self.mem.wrm(0x6001c018, 4, 4, 0)   #noise hw force en
            self.mem.wrm(0x6001c018, 3, 3, 1)   #noise update en
            self.mem.wrm(0x6001c018, 23, 23, 1) #noise cal
            self.mem.wrm(0x6001c018, 28, 28, 1) #noise auto
            time.sleep(0.1)
        noise = self.mem.rdm(0x6001c08c, 11, 0) #noise rd
        noise = (noise-2**12)/16.0
        print noise

    def debug_rx_sens(self):
        self.mem.wrm(0x6001c13c, 30, 18, (66+10))
        self.mem.wrm(0x6001c0a4, 13, 7, (60+10))
        self.mem.wrm(0x6001c0a4, 6, 0, (60+10))

    def rxiq_set(self, en=0, rxiq_gain=0, rxiq_phase=0):
        if rxiq_phase < 0:
            rxiq_phase += 64
        if rxiq_gain < 0:
            rxiq_gain += 32
        self.mem.wrm(0x600050dc, 27, 27, en) #rxiq enable
        self.mem.wrm(0x600050dc, 28, 28, 0) #rxiq sel
        self.mem.wrm(0x600050dc, 20, 16, rxiq_gain) #rxiq gain
        self.mem.wrm(0x600050dc, 26, 21, rxiq_phase) #rxiq phase

    def txiq_set(self, en=0, txiq_gain=0, txiq_phase=0):
        if txiq_phase < 0:
            txiq_phase += 64
        if txiq_gain < 0:
            txiq_gain += 32
        self.mem.wrm(0x600050dc, 11, 11, en) #txiq enable
        self.mem.wrm(0x600050dc, 12, 12, 0) #txiq sel
        self.mem.wrm(0x600050dc, 4, 0, txiq_gain) #txiq_gain
        self.mem.wrm(0x600050dc, 10, 5, txiq_phase) #txiq_phase


    def bias_reg_default(self, old_set=1):
        if old_set==1:
            self.i2c.bias_marlin3.cp1p6_dreg=0
            self.i2c.bias_marlin3.cp1p2_dreg=0
            self.i2c.bias_marlin3.cp1p1_pvt_reg=4
            self.i2c.bias_marlin3.dres12k=0
##            self.i2c.bias.rc_dvref=2
##            self.i2c.bias.rc_enx=1
##            self.i2c.bias.ent_bg=0
##            self.i2c.bias.ent_consti=0
##            self.i2c.bias.rc_dcap_ext=32
##            self.i2c.bias.rc_start=1
##            self.i2c.bias.xpd_bg=1
####            self.i2c.bias.rc_cap=39
##            self.i2c.bias.dres12k_force_on=1
##            self.i2c.bias.dres12k=8
##            self.i2c.bias.db_atten_on=0
##            self.i2c.bias.en_bias_sleep_atten=1
        else:
            self.i2c.bias.cp1p6_dreg=3
            self.i2c.bias.rc_dvref=3
            self.i2c.bias.rc_enx=1
            self.i2c.bias.ent_bg=1
            self.i2c.bias.ent_consti=1
            self.i2c.bias.rc_dcap_ext=29
            self.i2c.bias.rc_start=0
            self.i2c.bias.xpd_bg=0
            self.i2c.bias.rc_cap=56
            self.i2c.bias.dres12k_force_on=0
            self.i2c.bias.dres12k=0
            self.i2c.bias.db_atten_on=3
            self.i2c.bias.en_bias_sleep_atten=0


    def dtest_vol_pullout(self):
        self.rtc_debug.pull_internal_voltage(1)
        self.i2c.rfpll.ent_vco_bias = 1
        self.i2c.rfpll.dtest=1
##        self.i2c.bias_marlin3.ent_cgm = 1
##        self.i2c.bias_marlin3.dtest =1
    def fcc_limit_set(self, chan=1, cbw40=0, rate_index=0, backoff_db=0):
        self.wifiapi.init_para_chg(wr=1, index=61, data=2)
        if cbw40==0:
            index = 62+chan-1
            data = int(self.wifiapi.init_para_chg(wr=0, index=index, data=0),16)
            if rate_index < 8:
                data = (data & 0xf) | (backoff_db<<4)
            else:
                data = (data & 0xf0) | (backoff_db)
        else:
            index = 76+((chan-1)/2)-1
            data = int(self.wifiapi.init_para_chg(wr=0, index=index, data=0),16)
            if (chan-1)%2==1:
                data = (data & 0xf) | (backoff_db<<4)
            else:
                data = (data & 0xf0) | (backoff_db)
        self.wifiapi.init_para_chg(wr=1, index=index, data=data)

    def fcc_init_test(self, fcc_enable=2):
        self.wifiapi.init_para_chg(wr=1, index=61, data=fcc_enable)
        self.wifiapi.init_para_chg(wr=1, index=62, data=0x5a)  #cbw20m 11b\gn chan=1
        self.wifiapi.init_para_chg(wr=1, index=63, data=0x59)  #cbw20m 11b\gn chan=2
        self.wifiapi.init_para_chg(wr=1, index=64, data=0x58)  #cbw20m 11b\gn chan=3
        self.wifiapi.init_para_chg(wr=1, index=65, data=0x57)  #cbw20m 11b\gn chan=4
        self.wifiapi.init_para_chg(wr=1, index=66, data=0x56)  #cbw20m 11b\gn chan=5
        self.wifiapi.init_para_chg(wr=1, index=67, data=0x55)  #cbw20m 11b\gn chan=6
        self.wifiapi.init_para_chg(wr=1, index=68, data=0x54)  #cbw20m 11b\gn chan=7
        self.wifiapi.init_para_chg(wr=1, index=69, data=0x53)  #cbw20m 11b\gn chan=8
        self.wifiapi.init_para_chg(wr=1, index=70, data=0x52)  #cbw20m 11b\gn chan=9
        self.wifiapi.init_para_chg(wr=1, index=71, data=0x51)  #cbw20m 11b\gn chan=10
        self.wifiapi.init_para_chg(wr=1, index=72, data=0x50)  #cbw20m 11b\gn chan=11
        self.wifiapi.init_para_chg(wr=1, index=73, data=0x0a)  #cbw20m 11b\gn chan=12
        self.wifiapi.init_para_chg(wr=1, index=74, data=0x2a)  #cbw20m 11b\gn chan=13
        self.wifiapi.init_para_chg(wr=1, index=75, data=0x4a)  #cbw20m 11b\gn chan=14
        self.wifiapi.init_para_chg(wr=1, index=76, data=0xaa)  #cbw40m 11n chan=3,4
        self.wifiapi.init_para_chg(wr=1, index=77, data=0x88)  #cbw40m 11n chan=5,6
        self.wifiapi.init_para_chg(wr=1, index=78, data=0x66)  #cbw40m 11n chan=7,8
        self.wifiapi.init_para_chg(wr=1, index=79, data=0x44)  #cbw40m 11n chan=9,10
        self.wifiapi.init_para_chg(wr=1, index=80, data=0x22)  #cbw40m 11n chan=11

    def open_rf_xpd(self):
        self.mem.wrm(0x60008034, 31,27, 0x1f)
        self.mem.wr(0x600260d4, 0xffffffff)


    def rssi_debug(self, new_set=1):
        if new_set==1:
            self.mem.wrm(0x6001c088, 7, 0, 5)    #8
            self.mem.wrm(0x6001c0a0, 31, 24, 0)  #0
            self.mem.wrm(0x6001c02c, 7, 0, 0)    #254
            self.mem.wrm(0x6001c104, 15, 15, 0)  #1
        else:
            self.mem.wrm(0x6001c088, 7, 0, 8)    #8
            self.mem.wrm(0x6001c0a0, 31, 24, 0)  #0
            self.mem.wrm(0x6001c02c, 7, 0, 254)    #254
            self.mem.wrm(0x6001c104, 15, 15, 1)  #1
        self.mem.wrm(0x6001c038,27,27, 0)    #1


    def reboot_test(self,folder=''):
        filetime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()));
        filename = self.get_filename(folder, 'reboot_test')
        file_w = '%s_%s.log'%(filename, filetime)
        f=open(file_w, 'a')
        for i in range(1000):
            result = self.comport.req_com("esp_en_reboot",endstr='autotest git ver')
            f.write(result)
        f.close()

    def sar2_init_code(self,init_code=1400):
        self.i2c.sar.sar2_init_code_msb = init_code>>8
        self.i2c.sar.sar2_init_code_lsb = init_code&0xff

    def sar_delay_set(self, wr=0,state0=160,state1=15,state2=15,state3=15,state4=255,state5=23,state6=255,sar_delay=255,sar_start_befor=0,sample_num=0, atten=3):
        if wr==1:
            self.mem.wrm(0x6000e060,23,16, state0)
            self.mem.wrm(0x6000e054, 7, 0, state1)
            self.mem.wrm(0x6000e054,15, 8, state2)
            self.mem.wrm(0x6000e054,23,16, state3)
            self.mem.wrm(0x6000e058, 7, 0, state4)
            self.mem.wrm(0x6000e058,15, 8, state5)
            self.mem.wrm(0x6000e058,23,16, state6)
            self.mem.wrm(0x6000e060,15, 8, sar_delay)
            self.mem.wrm(0x6000e05c, 20, 20,sar_start_befor)
            self.mem.wrm(0x6000e050, 4, 2,sample_num)
            self.mem.wrm(0x6000e060, 4,3,atten)  #atten

        print "state0=%d"%self.mem.rdm(0x6000e060,23,16)
        print "state1=%d"%self.mem.rdm(0x6000e054, 7, 0)
        print "state2=%d"%self.mem.rdm(0x6000e054,15, 8)
        print "state3=%d"%self.mem.rdm(0x6000e054,23,16)
        print "state4=%d"%self.mem.rdm(0x6000e058, 7, 0)
        print "state5=%d"%self.mem.rdm(0x6000e058,15, 8)
        print "state6=%d"%self.mem.rdm(0x6000e058,23,16)
        print "sar_delay=%d"%self.mem.rdm(0x6000e060,15, 8)
        print "sar_start_befor=%d"%self.mem.rdm(0x6000e05c, 20, 20)
        print "sample_num=%d"%self.mem.rdm(0x6000e050, 4, 2)
        print "atten=%d"%self.mem.rdm(0x6000e060, 4,3)

    def rssi_offset(self,en,rssi_offset_0,rssi_offset_1,rssi_offset_2):
        self.wifiapi.init_para_chg(en,32,rssi_offset_0)
        self.wifiapi.init_para_chg(en,33,rssi_offset_1)
        self.wifiapi.init_para_chg(en,34,rssi_offset_2)
        self.rfchsel(1,0)
        ##        if rx_chan < 4:
##            self.mem.wrm(0x6001c02c,7,0,-28)
##        elif rx_chan <9 :
##            self.mem.wrm(0x6001c02c,7,0,-28)
##        else:
##            self.mem.wrm(0x6001c02c,7,0,-28)

    def set_loopback_mode(self,pa_gain=0xf, bbgain=0x20, loop_case=0,bt_mode=0,bb_atten=0):

        self.pbus.pbus_debugmode()
        self.mem.wrm(0x600060a0, 17, 14, 0xf)  #force txon rxon
        self.mem.wrm(0x6000607c, 30, 30, 0)  #fe loopback en

        if loop_case == 2: #digital interface loop
            self.mem.wrm(0x600050d0, 28, 28, 1)  #ana inf loopback en
            self.mem.wrm(0x600050d8, 25, 25, 0)  #tx iq swap
        elif loop_case == 1: # dac, filt, adc loop
            self.mem.wrm(0x600050d0, 28, 28, 0)  #ana inf loopback en
            self.mem.wrm(0x600050d8, 25, 25, 0)  #tx iq swap
            # dac,flt,adc
            self.pbus.pbus_wr('rfrx1','en1', 0x001)
            self.pbus.pbus_wr('rftx1','en1', 0x0)
            self.pbus.pbus_wr('rftx2','en1', 0x0)
            self.pbus.pbus_wr('bb','en1', 0x100)
            if bt_mode==0:
                self.pbus.pbus_wr('bb','en1', 0x1c9)
            else:
                self.pbus.pbus_wr('bb','en1', 0x1cb)
            self.pbus.pbus_wr('bb','en2', bbgain)
            self.i2c.bbtop.enlb = 0
        else:
            self.mem.wrm(0x600050d0, 28, 28, 0)  #ana inf loopback en
            self.mem.wrm(0x600050d8, 25, 25, 1)  #tx iq swap
            self.pbus.pbus_wr('rfrx1','en1', 0x104)
            self.pbus.pbus_wr('rftx1','en1', 0x7f)
            self.pbus.pbus_wr('rftx2','en1', pa_gain)
            if bt_mode==0:
                self.pbus.pbus_wr('bb','en1', 0x1f9)
            else:
                self.pbus.pbus_wr('bb','en1', 0x1fb)
            self.pbus.pbus_wr('bb','en2', bbgain)
            self.pbus.pbus_wr('rftx1','en2', bb_atten<<3)
            self.i2c.bbtop.enlb  = 1

        self.mem.wrm(0x600050dc, 11, 11, 0) #txiq disable
        self.mem.wrm(0x600050dc, 27, 27, 0) #rxiq disable

        self.pbus.set_dco(0x100, 0x100, 0x100, 0x100)
        self.rxdc_cal()

    def rx_gain_comp(self):
        target_pwr = 43.8
        num = 10
        chan_pwr_all = []
        for k in range(num):
            data = self.wifiapi.rx_gain_comp()
            data = data.split(',')
            chan_pwr = []
            for i in range(14):
                pwr = 10*np.log10(int(data[i],10))
                chan_pwr.append(pwr)
##            loginfo(k, chan_pwr)
            chan_pwr_all.append(chan_pwr)

        chan_pwr = []
        gain_comp = []
        for i in range(14):
            pwr_list = []
            for k in range(num):
                pwr_list.append(chan_pwr_all[k][i])
            min_pwr = min(pwr_list)
            gain_comp.append(target_pwr - min_pwr)
            chan_pwr.append(min_pwr)
##        loginfo(gain_comp)

##        gain_comp_re = []
##        for i in range(14):
##            comp_re = int(gain_comp[i]*2)/2.0
##            if comp_re > 2:
##                comp_re = 2
##            elif comp_re < -2:
##                comp_re = -2
##            gain_comp_re.append(comp_re)
##        loginfo(gain_comp_re)
##        return min(gain_comp_re)
        return gain_comp

    def get_rx_cable_lost_default(self,iqv_unit_no=1, cable_att=30, chan_m=[14],noise_ref=-95.2):
        u0 = time.time()
        rx_rate = '36m'
        packnum = 100
##        if self.chipv=="CHIP722":
##            rx_power=-50
##        else:
##            rx_power=-65
        rx_power =-70

        self.wifiapi.rssi_min_max_print()
        cable_list = []
        for chan in chan_m:
            rx_freq = self.chan2freq(chan)
            print chan
            self.rfchsel(chan,0)
            mytester=tester.tester(rx_freq, rx_power,rx_rate,1,iqv_unit_no,'source',cable_att)
            mytester.sigout(rx_freq,rx_power,cable_att,rx_rate,packnum,iqv_unit_no);
            power = rx_power
            lost_a = 0
##            if self.chipv=="CHIP722":
##                self.rx_force_gain(1, gain=7)

            for i in range(0,5):
                self.rxstart(rx_rate);
                time.sleep(0.1)
                mytester.trig_wave(1);
                result_data=self.cmdstop();
                [DesirePackNum, gain, rssi, noise, err, err2, freqoff, rssi_min, rssi_max]=self.rxresult(result_data)
                #[DesirePackNum, gain, rssi, noise, err, err2, freqoff, rssi_min, rssi_max,rssi_base_p5,rssi_base_p4,rssi_base_p3,rssi_base_p2,rssi_base_p1,rssi_base_n0,rssi_base_n1,rssi_base_n2,rssi_base_n3,rssi_base_n4,rssi_base_n5]=self.rxresult(result_data)

                rx_rssi=rssi/10.0;

                lost = rx_power - rx_rssi
                loginfo('pwr=%2.2f, rssi=%2.2f, lost=%2.2f, att=%2.2f'%(power, rx_rssi, lost, cable_att+lost_a))
                if(lost<=0) and (lost>=-0.3):
                    break
                lost_a += lost
                power = rx_power + lost_a
                mytester.set_pwr(power,0,iqv_unit_no,'source');

            cable_lost = cable_att+lost_a
            loginfo ('1:%2.2f'%cable_lost)
            mytester.gen_switch('OFF',1);

            rx_gain =  (gain+5)/10
            if rx_gain<60:
                rx_gain = 60
            noise = self.noise_check(1, chan, 0, 1, rx_gain)

            #noise = int(self.wifiapi.check_noise_floor())/4.0

            loginfo("noise check:%2.2f"%noise)

            if rx_rssi==0:
                cable_lost = 200
            else:
                cable_lost += noise-noise_ref;

            loginfo('cable_lost=%2.2fdB'%(cable_lost))
            cable_list.append(cable_lost)

        print 'time: %2.2f'%(time.time()-u0)
        loginfo(cable_list)
        return cable_list

    def pbus_set_rx(self, pbusmode_en=1, rfrx1=0x184, bb_gain=0, filter_atten=0,bt_mode=0):
        if pbusmode_en==1:
            self.pbus.pbus_debugmode()
            self.pbus.open_rx(rfrx1, bb_gain, filter_atten,bt_mode)
            self.wifiapi.rxdc_cal()
            if bt_mode==1:
                self.pbus.pbus_wr('dcoi', 'en2', 256)
                self.pbus.pbus_wr('dcoq', 'en2', 256)
        else:
            self.pbus.pbus_workmode()

