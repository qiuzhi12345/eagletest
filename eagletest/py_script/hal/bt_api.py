from hwregister.hwreg.ESP32 import FE,FE2

class BTAPI(object):

    def __init__(self,channel,chipv='ESP32'):
        self.channel=channel
        self.chipv=chipv

    def bt_tx_tone(self,en=0, chan=1, backoff=0):
        '''
        :brief:  BT tx tone open
        :param:
            - en:
                - 1: BT tx tone enable
                - 0: BT tx tone disable
            - chan: BT tx channel set (0 to 78)
            - backoff: tone power attenuation set,step is 1(0.25dbm)
        :return: - no return
        '''
        return  self.channel.req_com("bt_tx_tone %d %d %d"%(en,chan,backoff))

    def fcc_bt_tx(self,pwr_level,FH_en,tx_chan,rate,DH,datatype):
        '''
        :brief:  BR/EDR tx open
        :param:
            - pwr_level: TX power level,range 0 to 7,step 3dbm
            - FH_en:
                - 1: frequency hopping enable
                - 0: frequency hopping disable
            - tx_chan: BT tx channel set (0 to 78)
            - rate: tx rate set,1=1Mbps,2=2Mbps,3=3Mbps
            - DH: 1=DH1.3=DH3,5=DH5
            - datatype: 0: 01010101, 1: 00001111, 2: prbs9
        :return: - no return
        '''
        return  self.channel.req_com("fcc_bt_tx %d %d %d %d %d %d"%(pwr_level,FH_en,tx_chan,rate,DH,datatype))

    def fcc_le_tx(self,pwr_level,tx_chan,payload_len,datatype):
        '''
        :brief:  LE tx open
        :param: - pwr_level: TX power level,range 0 to 9,step 2dbm,deafult 4
               - tx_chan: BT tx channel set (0 to 39)
               - payload_len: payload length,range 0 to 255,deafult 250
               - datatype: 0: 01010101, 1: 00001111, 2: prbs9
        :return: - no return
        '''
        return  self.channel.req_com("fcc_le_tx %d %d %d %d"%(pwr_level,tx_chan,payload_len,datatype))

    def fcc_le_tx_syncw(self,pwr_level,tx_chan,payload_len,datatype,syncw):
        '''
        :brief:  le tx (add synchronization of DC offset compensation and identification)open
        :param: - pwr_level: TX power level,range 0 to 9,step 2dbm,deafult 4
               - tx_chan: BT tx channel set (0 to 39)
               - payload_len: payload length,range 0 to 255,deafult 250
               - datatype: 0: 01010101, 1: 00001111, 2: prbs9
               - syncw: deafult syncw=0x71764129
        :return: - no return
        '''
        return  self.channel.req_com("fcc_le_tx_syncw %d %d %d %d 0x%x"%(pwr_level,tx_chan,payload_len,datatype,syncw))


##class BTRX(object):
##
##    def __init__(self,channel,chipv='ESP32'):
##        self.channel=channel
##        self.chipv=chipv

    def rw_rx_per(self,modetype,rx_chan,ulap,ltaddr):
        '''
        :brief:  BR/EDR Rx open
        :param:
            - modetype:
                - 0: BR
                - 1: EDR
            - rx_chan: rx channel set (0 to 78),even number channel is from 0 to 39,uneven number is from 40 to 78, for example: 1 is channel 2, 40 is channel 1
            - ulap: BT MAC,size is 32bit,include UAP(8bit) + LAP(24bit),the param is decide for instrument
            - ltaddr: logical transport address,is decide for instrument,range 0 to 7
        :return: - no return
        '''
        return  self.channel.req_com("rw_rx_per %d %d %d %d"%(modetype,rx_chan,ulap,ltaddr))

    def rw_le_rx_per(self,rx_chan,syncw):
        '''
        :brief:  LE Rx open
        :param:
            - rx_chan: rx channel set (0 to 39)
                - channel 0、1、2--10 is corresponding frequency 2404MHz、2406MHz、2408MHz--2424MHz
                - channel 11、12、13--36 is corresponding frequency 2428MHz、2430MHz、2432MHz--2478MHz
                - channel 37、38、39 is corresponding frequency 2402MHz、2426MHz、2480MHz
            - syncw: synchronization of DC offset compensation and identification，is decide for instrument
        :return: - no return
        '''
        return  self.channel.req_com("rw_le_rx_per %d %d"%(rx_chan,syncw))



    def bt_txpwr_backoff(self, backoff=0):
        backoff_in = backoff
        if backoff_in<0:
            backoff_in += 256
        return self.channel.req_com("bt_txpwr_backoff %d"%backoff_in)

    def btpwr_track_en(self,pll_track=1,en=1):
        return  self.channel.req_com("bt_track_en %d %d"%(pll_track,en))

    def rtc_get_tsen(self,delay=1000,div=1):
        return self.channel.req_com("rtc_get_tsen %d %d"%(delay,div))

    def tsen_code(self):
        '''
        bt temp sensor data

        '''
        return self.channel.req_com("tsen_code")


