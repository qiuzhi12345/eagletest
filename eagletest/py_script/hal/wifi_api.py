from hwregister.hwreg.ESP32 import FE,FE2

class WIFIAPI(object):

    def __init__(self,channel,chipv='ESP32'):
        self.channel=channel
        self.chipv=chipv

    def rfinit(self):
        '''
        :brief: rf init
        :param: - no param
        :return: - no return
        '''
        return self.channel.req_com("rf_init");

    def bbinit(self):
        '''
        :brief: bb init
        :param: - no param
        :return: - no return
        '''
        return self.channel.req_com("bb_init");

    def macinit(self):
        '''
        :brief: mac init
        :param: - no param
        :return: - no return
        '''
        return self.channel.req_com("mac_init");

    def phyinit(self):
        '''
        :brief: phy init(include rfinit and bbinit and macinit)
        :param: - no param
        :return: - no return
        '''
        return self.channel.req_com("phy_init", endstr='phy_init');

    def rftest_init(self):
        '''
        :brief: rftest_init
        :param: - no param
        :return: - no return
        '''
        return self.channel.req_com("rftest_init", endstr='rftest_init done');

    def init_print(self):
        '''
        :brief: init print
        :param: - no param
        :return: - no return
        '''
        return self.channel.req_com("init_print", endstr='print end')

    def rfchsel(self,chan,cbw2040_cfg=0):
        '''
        :brief: wifi channel set
        :param:
                - chan: channel number (1 to 14)
                - cbw2040_cfg:
                    - 1:HT40 enable
                    - 0:HT40 disable
        :return: - no return
        '''
        return self.channel.req_com("RFChannelSel %d %d"%(chan,cbw2040_cfg))

    def cbw40m_en(self,en=0):
        '''
        :brief: 40M bandwidth enable
        :param: - en:
                    - 0: HT40 disable
                    - 1: HT40 enable
        :return: - print the status
        '''
        return self.channel.req_com("cbw40m_en %d"%(en))

    def cmdstop(self, print_err=0):
        '''
        :brief: wifi TX/RX state stop
        :param: - no param
        :return: - no return
        '''
        return self.channel.req_com('CmdStop');

    def esp_origin_mac(self):
        '''
        :brief:  origin mac read
        :param: - no param
        :return: - the value of origin mac
        '''
        return  self.channel.req_com('esp_origin_mac')


##class WIFITX_API(object):
##
##    def __init__(self,channel,chipv='ESP32'):
##        self.channel=channel
##        self.chipv=chipv

    def filltxpacket(self,PackLen,pdu0len,pdu1len,rate=0,key_no=0,bssid_no=0,lnkstartaddr=0,short_gi=0,ap_mac_5=1,ap_mac_4=2,ap_mac_3=3,ap_mac_2=4,ap_mac_1=5,ap_mac_0=6):
        '''
        :brief: wifi TX tone set
        :param:
            - PackLen: include que_no and packeet_len,as (que_no<<16)+packlen
            - pdu0len: include pdu0 and pdu2 length, as (pdu2len<<16)+pdu0len
            - pdu1len: include pdu1 and pdu3 length, as (pdu3len<<16)+pdu1len
            - for ampsdu and ampdu, pdu0len and pdu1len must set to zero
            - lnkstartaddr:for ver5.0 above, it <<8+bssid_no as param to board
        '''
        if (PackLen&0xffff)<4000:
            pdu0len_set = pdu0len;
            pdu1len_set = 0;
        elif (PackLen&0xffff)<8000:
            pdu0len_set = 4000;
            pdu1len_set = (PackLen&0xffff) - 4000;
        elif (PackLen&0xffff)<8192:
            pdu0len_set = 4000+(4000<<16);
            pdu1len_set = (PackLen&0xffff) - 8000;
        else :
            pdu0len_set = 4000+(4000<<16);
            pdu1len_set = (PackLen&0xffff) - 8000;
            #return "Length too long!";

        cmdstr="FillTxPacket %d %d %d %d %d %d %d %d %d %d %d %d"%(PackLen,pdu0len_set,pdu1len_set,rate,key_no,(short_gi<<28)+((lnkstartaddr%0x40000)<<8)+bssid_no,ap_mac_5,ap_mac_4,ap_mac_3,ap_mac_2,ap_mac_1,ap_mac_0);

        if ''!=self.channel.req_com(cmdstr):
           return True;
        else:
           return False;

    def txstart(self,tx_rate,packnum,que_no=1,frm_delay=100,cbw40=0,ht_dup=0,dis_cca=1,lr_en=0):
        if tx_rate != -1:
           if ''!=self.channel.req_com("WifiTxStart %d %d %d %d %d %d"%((10<<16)+(lr_en<<15)+tx_rate,packnum,frm_delay,cbw40,ht_dup,dis_cca)):
              return True;
           else:
              return False;
        else:
           return False;

    def txstart_over(self,tx_rate,packnum,que_no=1,frm_delay=100,cbw40=0,ht_dup=0, dis_cca=1):
        return self.channel.req_com("WifiTxStart %d %d %d %d %d %d"%((10<<16)+tx_rate,packnum,frm_delay,cbw40,ht_dup,dis_cca))

    def test_txtone_pwr(self,atten,loop_num,mode=0,step=0, delay_us=10):
        result = self.channel.req_com("test_txtone_pwr %d %d %d %d %d"%(atten, loop_num, mode, step, delay_us))
        return result

    def txtone_step(self, en1=1, step1=0, att1=0, en2=0, step2=0, att2=0):
    	return self.channel.req_com("txtone_step %d %d %d %d %d %d"%(en1, step1, att1, en2, step2, att2))

    def txtone(self,tone1_en=1,freq1_mhz=2,tone1_att=0,tone2_en=0,freq2_mhz=0,tone2_att=0):
        '''
        :brief: wifi TX tone set
        :param:
            - tone1_en:
                - 1: first tone enable
                - 0: fisrt tone disable
            - freq1_mhz: first tone offset frequency
            - tone1_att: first tone attenuation set
            - tone2_en:
                - 1: second tone enable
                - 0: second tone disable
            - freq2_mhz: second tone offset frequency
            - tone2_att: second tone attenuation set
        :return: - no return
        '''
        cmdstr="txtone %d %d %d %d %d %d"%(tone1_en,freq1_mhz,tone1_att,tone2_en,freq2_mhz,tone2_att);
        return self.channel.req_com(cmdstr);

    def stoptone(self,tone_no=0):
        '''
        :brief: wifi tx tone state close
        :param: - tone_no:  the number of tone
        :return: - no return
        '''
        return self.channel.req_com("stoptone %d"%tone_no);

    def target_power_backoff(self,backoff_qdb):
        '''
        :brief: wifi target power backoff
        :param: - backoff_qdb: value of backoff
        :return: - no return
        '''
        cmdstr="target_power_backoff %d"%(backoff_qdb)
        return self.channel.req_com(cmdstr, endstr='target_power_backoff')

    def tx_contin_en(self,en=0):
        '''
        :brief: Tx continuous enable
        :param: - en:
                    - 0: Tx continuous disable
                    - 1: Tx continuous enable
        :return: - print the status
        '''
        return self.channel.req_com("tx_contin_en %d"%(en))

    def tx_cbw40m_en(self,en=0):
        '''
        :brief: Tx CBW40 enable
        :param: - en:
                    - 0: Tx CBW40 disable
                    - 1: Tx CBW40 enable
        :return: - print the status
        '''
        return self.channel.req_com("tx_cbw40m_en %d"%(en))

    def wifitxout(self,chan=1,data_rate=0x17,backoff=0):
        '''
        :brief: tx packect command
        :param: - chan: channel number (1 to 14)
                - data_rate:
                    =====  =====   =====  ====    =====  ====
                    11b            11g            11n
                    param  rate    param  rate    param  rate
                    =====  =====   =====  ====    =====  ====
                    0x0    1M      0xb    6M      0x10   MCS0
                    0x1    2ML     0xf    9M      0x11   MCS1
                    0x2    5.5ML   0xa    12M     0x12   MCS2
                    0x3    11ML    0xe    18M     0x13   MCS3
                    0x4     --     0x9    24M     0x14   MCS4
                    0x5    2MS     0xd    36M     0x15   MCS5
                    0x6    5.5MS   0x8    48M     0x16   MCS6
                    0x7    11MS    0xc    54M     0x17   MCS7
                    =====  =====   =====  ====    =====  ====
                - backoff: tx power attenuation, 4 indicates an attenuation 1dB
        :return: - print the status
        '''
        return self.channel.req_com("wifitxout %d %d %d"%(chan,data_rate,backoff))

    def esp_tx(self,chan=1,data_rate=0x17,backoff=0):
        '''
        :brief: tx packect command
        :param: - chan: channel number (1 to 14)
                - data_rate:
                    =====  =====   =====  ====    =====  ====
                    11b            11g            11n
                    param  rate    param  rate    param  rate
                    =====  =====   =====  ====    =====  ====
                    0x0    1M      0xb    6M      0x10   MCS0
                    0x1    2ML     0xf    9M      0x11   MCS1
                    0x2    5.5ML   0xa    12M     0x12   MCS2
                    0x3    11ML    0xe    18M     0x13   MCS3
                    0x4     --     0x9    24M     0x14   MCS4
                    0x5    2MS     0xd    36M     0x15   MCS5
                    0x6    5.5MS   0x8    48M     0x16   MCS6
                    0x7    11MS    0xc    54M     0x17   MCS7
                    =====  =====   =====  ====    =====  ====
                - backoff: tx power attenuation, 4 indicates an attenuation 1dB
        :return: - print the status
        '''
        return self.channel.req_com("esp_tx %d %d %d"%(chan,data_rate,backoff))


    def wifiscwout(self,en=1,chan=1,backoff=0):
        '''
        :brief: SCW TX command
        :param: - en: SCW Tx enable
                    - 0: disable
                    - 1: enable
                - chan: channel number (1 to 14)
                - backoff: tx power attenuation, 4 indicates an attenuation 1dB
        :return: - print the status
        '''
        return self.channel.req_com("wifiscwout %d %d %d"%(en,chan,backoff))

    def set_tx_gain(self,pa_gain=0x5f,bb_gain=0x120):
        '''
        :brief: set tx gain command
        :param: - pa_gain: 0x1f, 0x2f,0x3f,0x4f,0x5f,0x6f,0x7f
                - bb_gain: ..., 0x100,0x140,0x20,0x60, ...
        :return: - print the status
        '''
        return self.channel.req_com("set_tx_gain %d %d "%(pa_gain, bb_gain))

    def set_tx_dig_gain(self,force_en=1 ,dig_gain=25):
        '''
        :brief: set tx digital gain command
        :param: - force_en:
                            - 0: disable;
                            - 1: enable
                - dig_gain:
        :return: - print the status
        '''
        return self.channel.req_com("set_tx_dig_gain %d %d "%(force_en, dig_gain))

    def rx_pbus_set(self,rxon_rfrx=0x184, rxon_bb1=0x189, rxoff_rfrx=0x0, rxoff_bb1=0x108):
    	cmdstr = "rx_pbus_set %d %d %d %d"%(rxon_rfrx, rxon_bb1, rxoff_rfrx, rxoff_bb1)
    	return self.channel.req_com(cmdstr)

    def tx_pbus_set(self,rxon_rfrx=0x1, rxon_bb1=0x7c, rxoff_rfrx=0x0, rxoff_bb1=8):
    	cmdstr = "tx_pbus_set %d %d %d %d"%(rxon_rfrx, rxon_bb1, rxoff_rfrx, rxoff_bb1)
    	return self.channel.req_com(cmdstr)

    def pa_pbus_set(self, on_txrf=0x7f, off_txrf=0):
    	cmdstr = "pa_pbus_set %d %d"%(on_txrf, off_txrf)
    	return self.channel.req_com(cmdstr)

    def set_pbus_mem(self,rxon_rfrx=0x184, rxon_bb1=0x189, rxoff_rfrx=0x0, rxoff_bb1=0x108,
                          txon_rfrx=0x1, txon_bb1=0x7c, txoff_rfrx=0x0, txoff_bb1=8,
                          paon_txrf=0x7f, paoff_txrf=0):
    	cmdstr = "set_pbus_mem %d %d %d %d %d %d %d %d %d %d"%(
            rxon_rfrx, rxon_bb1, rxoff_rfrx, rxoff_bb1,
            txon_rfrx, txon_bb1, txoff_rfrx, txoff_bb1,
            paon_txrf, paoff_txrf)
    	return self.channel.req_com(cmdstr)

    def txpwr_track_en(self,track_en=0,correct_en=0,print_en=0):
        '''
        :brief: track the power of packet
        '''
        return self.channel.req_com("txpwr_track_en %d %d %d "%(track_en,correct_en,print_en))

    def packet_pwdet_out(self, rate=0):
        '''
        :brief: detect the power of packet
        '''
        return self.channel.req_com("packet_pwdet_out %d"%rate)

##class WIFIRX_API(object):
##
##    def __init__(self,channel,chipv='ESP32'):
##        self.channel=channel
##        self.chipv=chipv

    def get_rx_tone_pwr(self,rx_freq_cfg):
        return self.channel.req_com("get_rx_tone_pwr %d"%rx_freq_cfg);

    def rxdc_cal(self, print_en=0):
        return self.channel.req_com("rxdc_cal %d"%print_en);

    def rxstart(self,rate_sym):
        '''
        :brief: wifi RX state open
        :param: - rate_sym:  wifi rate (need to measure RX performance)
        :return: - no return
        '''
        if rate_sym!=-1:
           if ''!=self.channel.req_com("WifiRxStart 0x%x"%rate_sym):
              return True;
           else:
              return False;
        else:
           self.channel.req_com("WifiRxStart %d"%rate_sym)

    def check_noise_floor(self):
        '''
        :brief: RF noisefloor check
        :param: - noise:  value of noisefloor
        :return: - no return
        '''
        cmdstr="check_noise_floor"
        return self.channel.req_com(cmdstr)

    def set_noise_floor(self,noise=95*4):
        '''
        :brief: RF noisefloor set
        :param: - noise:  value of noisefloor
        :return: - no return
        '''
        cmdstr="set_noise_floor %d"%(noise)
        return self.channel.req_com(cmdstr)

    def read_hw_noisefloor(self):
        '''
        :brief: RF noisefloor read
        :param: - no param
        :return: - the value of hardware noisefloor
        '''
        return self.channel.req_com("read_hw_noisefloor")

    def esp_rx(self,chan=1,data_rate=0x17):
        '''
        :brief: rx packect command
        :param: - chan: channel number (1 to 14)
                - data_rate:
                    =====  =====   =====  ====    =====  ====
                    11b            11g            11n
                    param  rate    param  rate    param  rate
                    =====  =====   =====  ====    =====  ====
                    0x0    1M      0xb    6M      0x10   MCS0
                    0x1    2ML     0xf    9M      0x11   MCS1
                    0x2    5.5ML   0xa    12M     0x12   MCS2
                    0x3    11ML    0xe    18M     0x13   MCS3
                    0x4     --     0x9    24M     0x14   MCS4
                    0x5    2MS     0xd    36M     0x15   MCS5
                    0x6    5.5MS   0x8    48M     0x16   MCS6
                    0x7    11MS    0xc    54M     0x17   MCS7
                    =====  =====   =====  ====    =====  ====
        :return: - print the status
        '''
        return self.channel.req_com("esp_rx %d %d"%(chan,data_rate))


    def adctrig(self,smp_num_aft_trig,trig_mode='sw',sample_80m=0,trigcase=0,dump_trig=0,rx_gain_mode=0,rx_gain=0,rx_gain0=0,gain0_wait=0):
        '''return curr_ptr,wrap_flag, buff_addr, buff_size'''
        trig_dic={
        'sw'     :(0,0),
        'bb'     :(1,0),
        'cca'    :(2,0),
        'rxstart':(3,0),
        'rxend'  :(4,0),
        'txstart':(5,0),
        'txend'  :(6,0),
        'rxerr0' :(7,0),
        'rxerr1' :(7,1),
        'rxerr' :(7,trigcase)};

        if trig_mode in trig_dic:
            trigmode=trig_dic[trig_mode][0];
            trigcase=trig_dic[trig_mode][1];
        else:
            logwarn("mode err,only allow mode:");
            logwarn("sw, bb, cca, rxstart, rxend, txstart, txend, rxerr0, rxerr1");
            return [];
        result=self.channel.req_com("adctrig 0x%x %d %d %d %d %d %d %d %d"%(smp_num_aft_trig,trigmode,trigcase,sample_80m,dump_trig,rx_gain_mode,rx_gain,rx_gain0,gain0_wait));
        if result in ['','fail']:
            return [];
        rs=result.split(',');
        return [int(data,16) for data in rs];

    def adc_rand(self,en=1):
        '''
        :brief: get adc rand
        :param: en:  enable output rand mode
        :return: - no return
        '''
        cmdstr="adc_rand %d"%(en)
        return self.channel.req_com(cmdstr)


    def rx_per_init(self):
        return self.channel.req_com("rx_per_init")


    def enable_lr(self):
        return self.channel.req_com("enable_lr")

    def disable_lr(self):
        return self.channel.req_com("disable_lr")

    def disable_lr(self):
        return self.channel.req_com("disable_lr")

    def disable_lr(self):
        return self.channel.req_com("disable_lr")

    def init_para_chg(self,wr=0, index=0, data=0):
        if data<0:
            data = 2**16+data
        return self.channel.req_com("init_para_chg %d %d %d"%(wr, index, data))

    def set_rfrx_dcap(self):
        return self.channel.req_com("set_rfrx_dcap")

    def flash_test_enable(self, en=1):
        return self.channel.req_com("flash_test_enable %d"%en)

    def flash_test_init(self, clk_div=2, drv=3, mode=0):
        return self.channel.req_com("flash_test_init %d %d %d"%(clk_div, drv, mode))

    def rssi_min_max_print(self, en=1):
        return self.channel.req_com("rssi_min_max_print %d"%en)

    def pll_cap_track_en(self, en=1):
        print 'pll_cap_track_en %d'%en
        return self.channel.req_com("pll_cap_track_en %d"%en)

    def flash_pad_drv(self, clk_drv=3, cmd_drv=3, data0_drv=3, data1_drv=3, data2_drv=3, data3_drv=3):
        return self.channel.req_com("flash_pad_drv %d %d %d %d %d %d"%(clk_drv, cmd_drv,data0_drv,data1_drv,data2_drv,data3_drv))

    def burn_in_test(self):
        return self.channel.req_com("burn_in_test")

    def pll_vol_cal(self):
        return self.channel.req_com("pll_vol_cal")

    def test_i2c_time(self, write_en=1):
        return self.channel.req_com("test_i2c_time %d"%write_en)

    def set_freq_time(self, channel=1):
        return self.channel.req_com("set_freq_time %d"%channel)

    def get_pll_vol(self, atten=0):
        code = self.channel.req_com("get_pll_vol %d"%atten)
        vol = float(code)*1.7/4095.0
        return int(code)

    def i2c_clk_sel(self, clk_sel=1):
        return self.channel.req_com("i2c_clk_sel %d"%clk_sel)

    def i2c_clk_change(self, change=0):
        return self.channel.req_com("i2c_clk_change %d"%change)

    def get_sar2_vol(self, atten=0):
        return self.channel.req_com("get_sar2_vol %d"%atten)

    def pvt_test(self):
        return self.channel.req_com("pvt_test")

    def write_dac_gain2(self, dac_gain2_en=0, gain0=0,gain1=0,gain2=0,gain3=0,gain4=0,gain5=0,gain6=0,gain7=0):
        comstr = "write_dac_gain2 %d %d %d %d %d %d %d %d %d"%(dac_gain2_en, gain0,gain1,gain2,gain3,gain4,gain5,gain6,gain7)
        return self.channel.req_com(comstr)

    def wifi_filtbw_set(self, txfbw_en=0, rxfbw_en=0):
        #rxfbw_en=1: filt0-agc, filt1-11g/n, filt2-11b, filt3-11n low rate
        comstr = "wifi_filtbw_set %d %d"%(txfbw_en, rxfbw_en)
        return self.channel.req_com(comstr)

    def print_pwr_index(self):
        comstr = "print_pwr_index"
        return self.channel.req_com(comstr)

    def tx_fbw_enable(self, en=1):
        comstr = "tx_fbw_enable %d"%en
        return self.channel.req_com(comstr)

    def phy_close_rf(self):
        comstr = "phy_close_rf"
        return self.channel.req_com(comstr)

    def meas_tone_pwr_db(self, tone_atten=0, tone_step=64, pwr_offset=18.5*16):
        comstr = "meas_tone_pwr_db %d %d %d"%(tone_atten, tone_step, pwr_offset)
        return self.channel.req_com(comstr)

    def adc_rand(self, en=1):
        comstr = "adc_rand %d"%en
        return self.channel.req_com(comstr)

    def remove_11b_4p8G_spur(self, en=1, num=4):
        comstr = "remove_11b_4p8G_spur %d %d"%(en,num)
        return self.channel.req_com(comstr)

    def dig_11b_filter_sel(self, sel=1):
        comstr = "dig_11b_filter_sel %d"%(sel)
        return self.channel.req_com(comstr)

    def coex_test(self, mode=0):
        comstr = "coex_test %d"%(mode)
        return self.channel.req_com(comstr)

    def coex_test_init(self):
        comstr = "coex_test_init"
        return self.channel.req_com(comstr)

    def tx_ack_test(self,ap_addr0=0x0,ap_addr1=0x0,tx_rate=0x10,tx_num=100,txlength=1024,backoff=0,aifs=3,delay_ms=0):
        return self.channel.req_com("tx_ack_test 0x%x 0x%x 0x%x %d %d %d %d %d"%(ap_addr0,ap_addr1,tx_rate,tx_num,txlength,backoff,aifs,delay_ms),endstr='flag:')

    def wifi_ack_test(self, tx_num=100, test_num=20, backoff=1, test_mode=0, delay_ms=0):
        '''
        :(ESP32) test_mode: 0-coex_test, 1-set channel, 2-modem sleep, 3-light sleep NO WIFI_PD, 4-light Sleep WIFI_PD
        '''
        comstr = "wifi_ack_test %d %d %d %d %d"%(tx_num, test_num, backoff, test_mode, delay_ms)
        return self.channel.req_com(comstr)

    def sleep_proc_test(self,sleep_mode=0, sleep_time=100, wakeup=1):
        comstr = "sleep_proc_test %d %d %d"%(sleep_mode, wakeup, sleep_time)
        return self.channel.req_com(comstr)

    def light_sleep_test(self,sleep_mode=0, sleep_time=100, init_en=1):
        comstr = "light_sleep_test %d %d %d"%(sleep_mode, sleep_time, init_en)
        return self.channel.req_com(comstr)

    def tx_ack_start(self,tx_num=100,backoff=0,aifs=0,delay_ms=0):
        return self.channel.req_com("tx_ack_start %d %d %d %d"%(tx_num,backoff,aifs,delay_ms))


    def wifi_ack_test(self,ap_addr0=0x0,ap_addr1=0x0,tx_rate=0x10,txlength=1024,chan_org=1,chan_cfg_org=0,tx_num=100,test_num=1,backoff=0,test_mode=0,delay_ms=0):
        return self.channel.req_com("wifi_ack_test 0x%x 0x%x 0x%x %d %d %d %d %d %d %d %d"%(ap_addr0,ap_addr1,tx_rate,txlength,chan_org,chan_cfg_org,tx_num,test_num,backoff,test_mode,delay_ms),endstr='ack_num,')

    def rfpll_cal_time(self,chan_freq=12, mode=1):
        # mode=1: chan_freq is valid
        # mode=0: test ir_cap_ext
        result = self.channel.req_com("rfpll_cal_time %d %d"%(chan_freq,mode), endstr='rfpll_cal_time')
        result = result.replace('\r', '').replace('=',',').replace(':', ',')
        for i in range(1, 100):
            if result[-i] == '\n':
                end_index = -i
        return result[0:end_index+1]

    def rc_cal(self):
        return self.channel.req_com("rc_cal")

    def get_rx_result(self):
        return self.channel.req_com("esp_get_rx_result")

    def freq_init(self):
        return self.channel.req_com("freq_init", endstr='freq_init')

    def force_txtone(self, atten=0, delay_us=200):
        return self.channel.req_com("force_txtone %d %d"%(atten, delay_us))

    def wifi_init_8266(self, byte_112=0, byte_113=0):
        if byte_113<0:
            byte_113 += 256
        return self.channel.req_com("WifiInit %d %d"%(byte_112, byte_113))

    def rfchsel_offset_esp8266(self,chan, offset=0):
        if offset<0:
            offset += 2**16
        return self.channel.req_com("RFChannelSel_Offset %d %d"%(chan, offset))

    def rfchsel_offset_esp32(self,freq_offset):
        return self.channel.req_com("set_chan_offset %d"%(freq_offset))

    def uart_test_enable(self, enable=0):
        return self.channel.req_com("uart_test_enable %d"%enable)

    def gpio_test_init(self, gpio_mask=0):
        return self.channel.req_com("gpio_test_init %d"%gpio_mask)

    def test_tout(self):
        return self.channel.req_com("test_tout 0")

    def iq_est_enable(self, length=14):
        return self.channel.req_com("iq_est_enable %d"%length)

    def set_cca(self, en= 1, rssi=-96):
        return self.channel.req_com("set_cca %d %d"%(en, ((rssi+256)&0xff)))

    def set_rx_sense(self, rssi=-96):
        return self.channel.req_com("set_rx_sense %d"%((rssi+256)&0xff))

    def phy_set_freq(self, freq=2412, freq_offset=0):
        if freq_offset < 0:
            freq_offset += 65536
        return self.channel.req_com("phy_set_freq %d %d"%(freq, freq_offset))

    def get_tx_rate(self):
        self.cmdstop('com')
        tx_rate=self.channel.req_com("get_tx_rate")
        if ''!=tx_rate:
            rate=int(tx_rate.split('=')[1])
            #return [rate/4, rate&0x3]
            return rate;
        else:
            return False;

    def phy_get_vdd33(self):
        return self.channel.req_com("phy_get_vdd33")

    def force_txon_ESP8266(self,en=0):
        return self.channel.req_com("set_tx_pbus_on %d"%(en))
