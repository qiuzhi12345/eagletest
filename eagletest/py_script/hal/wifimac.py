from baselib.loglib.log_lib import *
from hal.hwregister.hwreg.all import *
from hal.common import MEM
from collections import OrderedDict
import time

class WIFIMAC(object):
    """docstring for wifimac"""
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.hwreg = HWREG(self.channel, self.chipv)
        self.mem = MEM(self.channel, self.chipv)

    def mac_init(self,qmap=1):
        return self.channel.req_com("mac_init 0x%x"%qmap)

    def mac_int_suit(self):
        '''
        suit intterrput for WIFI MAC
        '''
        return self.channel.req_com("mac_interrupt_suit")

    def mac_int_desuit(self):
        '''
        suit intterrput for WIFI MAC
        '''
        return self.channel.req_com("mac_interrupt_desuit")

    def mac_tx_start(self, loop=0, lock = 1):
        '''
        start RX

        :lock:
            - 1 tx one time and locked until tx complete
        :loop:
            - txtime, valid when lock == 0

        :return:
            if *lock* == 1, txcomplete state,
            otherwise, invalid
        '''
        #return int(self.channel.req_com("mac_tx_start 0x%x 0x%x"%(loop, lock)), 16)
        self.channel.req_com("mac_tx_start 0x%x 0x%x"%(loop, lock))

    def mac_tx_stop(self):
        '''
        stop RX
        '''
        return self.channel.req_com("mac_tx_stop")


    def mac_txpacket_rand(self):
        '''
        random tx packet, exclude mac_head
        '''
        return self.channel.req_com("mac_txpacket_rand")
    def mac_rx_start(self):
        '''
        start RX
        '''
        # self.hwreg.MAC_RX.MACRXMODE.reg_rxbuflk_ena_frc = 1
        # self.hwreg.MAC_SCH.INT_ENA_MAC.rxsuc_data_int_ena = 1

        return self.channel.req_com("mac_rx_start")

    def mac_rx_stop(self):
        '''
        stop RX
        '''
        # self.hwreg.MAC_RX.MACRXMODE.reg_rxbuflk_ena_frc = 0
        # time.sleep(0.01)
        # self.hwreg.MAC_SCH.INT_ENA_MAC.rxsuc_data_int_ena = 0
        return self.channel.req_com("mac_rx_stop")



    def get_tx_cnt(self, clear = 0,qsel=0):
        return int(self.channel.req_com("get_tx_cnt 0x%x 0x%x"%(clear,qsel)), 16)

    def get_rx_cnt(self, clear = 0):
        '''

        :clear:
            - 0: after get the RX count , clear count
        '''
        return int(self.channel.req_com("get_rx_cnt 0x%x"%(clear)), 16)
        # rxdata_hw_suc = self.hwreg.MAC_RX.MACRX_DATASUC_CNT.reg
        # rx_bb_err = self.hwreg.MAC_RX.MACRX_CCK_ERRCNT.reg + self.hwreg.MAC_RX.MACRX_AGC_ERRCNT.reg
        # rx_fcs_err = self.hwreg.MAC_RX.MACRX_FCS_ERRCNT.reg
        # rx_abort_err = self.hwreg.MAC_RX.MACRX_ABORT_CNT.reg
        # rx_buffer_full = self.hwreg.MAC_RX.MACRX_BUF_FULLCNT.reg
        # rx_all = self.hwreg.MAC_RX.MACRX_END_CNT.reg
        # return rxdata_sw_suc, rxdata_hw_suc, rx_buffer_full, rx_bb_err, rx_fcs_err, rx_abort_err, rx_all

    def get_txpacket_buffer(self, qnum):
        '''
        :retrun:
            [txcontrol addr, txpacket buffer addr]

        '''
        txcontroll_addr = int(self.channel.req_com("get_txpacket_buffer 0x%x"%(qnum)), 16)
        if qnum == 0:
            txpacket_buffer = self.hwreg.MAC_SCH.MACTXQ0_PLCP0.reg_txq0_link_addr | 0x3ff00000
        elif qnum == 1:
            txpacket_buffer = self.hwreg.MAC_SCH.MACTXQ1_PLCP0.reg_txq1_link_addr | 0x3ff00000
        elif qnum == 2:
            txpacket_buffer = self.hwreg.MAC_SCH.MACTXQ2_PLCP0.reg_txq2_link_addr | 0x3ff00000
        elif qnum == 3:
            txpacket_buffer = self.hwreg.MAC_SCH.MACTXQ3_PLCP0.reg_txq3_link_addr | 0x3ff00000
        elif qnum == 4:
            txpacket_buffer = self.hwreg.MAC_SCH.MACTXQ4_PLCP0.reg_txq4_link_addr | 0x3ff00000
        elif qnum == 5:
            txpacket_buffer = self.hwreg.MAC_SCH.MACTXQ5_PLCP0.reg_txq5_link_addr | 0x3ff00000
        elif qnum == 6:
            txpacket_buffer = self.hwreg.MAC_SCH.MACTXQ6_PLCP0.reg_txq6_link_addr | 0x3ff00000
        elif qnum == 7:
            txpacket_buffer = self.hwreg.MAC_SCH.MACTXQ7_PLCP0.reg_txq7_link_addr | 0x3ff00000

        return  txcontroll_addr, txpacket_buffer

    def get_rxpacket_buffer(self):
        '''
        get_rxpacket_buffer link addr

        :return:
            - 0x1 : err, rxpacket_buffer is NULL
            - 0x2 : err, rxpacket_buffer is unvalid , owner == 1
            - XXX : base
        '''
        return int(self.channel.req_com("get_rxpacket_buffer"), 16)

    def set_free_rxpacket_buffer(self):
        '''
        set free rxpacket_buffer link

        :return:
            - 0x1 : rxpacket_buffer is NULL
            - 0x2 : rxpacket_buffer is unvalid , owner == 1
            - 0x0 : suc
        '''
        return int(self.channel.req_com("set_free_rxpacket_buffer"), 16)

    def set_rx_func(self, func_num, fun_sel):
        '''
        :fun_sel:
            - 0: NULL
            - 1: rxinfo
        '''
        return self.channel.req_com("set_rx_func 0x%x 0x%x"%(func_num, fun_sel))
    
    def set_tx_func(self, func_num, fun_sel):
        '''
        :fun_sel:
            - 0: NULL
            - 1: rxinfo
        '''
        return self.channel.req_com("set_tx_func 0x%x 0x%x"%(func_num, fun_sel))

    def set_rx_filter(self, bssid_sel = 0, mode = 1):
        '''
        :bssid:
            bssid select

        :mode:
            - 0: bssid da check mode, group abort
            - 1: bssid da check mode
            - 2: sniffer mode
        '''
        return self.channel.req_com("set_rx_filter 0x%x 0x%x"%(bssid_sel, mode))

    def set_rx_addr(self, bssid_sel, rxda, rxbssid):
        '''
        set rx addr

        :bssid:
            bssid select

        :rxda:
            RX DA
        :rxbssid:
            RX BSSID
        '''
        return self.channel.req_com("set_rx_addr 0x%x 0x%x 0x%x 0x%x 0x%x"%(bssid_sel, rxda&0xffffffff, (rxda>>32)&0xffff, rxbssid&0xffffffff, (rxbssid>>32)&0xffff))

    def RFChannelSel(self, rfchannel, mode = 0):
        '''
        Set WIFI channel

        :rfchannel:
            channel number 1 ~ 14
        :mode:
            - 0: 20M mode
        '''
        return self.channel.req_com("RFChannelSel 0x%x 0x%x"%(rfchannel, mode))

    def dbg_rx_link(self):
        '''
        :return:
            (rxhead, rxtail, rxpacket_head)
        '''
        res = self.channel.req_com("mac_dbg_rxhead").split()
        return int(res[0], 16), int(res[1], 16)

    def check_macinit(self):
        res = self.channel.req_com("check_macinit")
        return int(res, 16)

    def mac_qstop(self,qselect):
        res = self.channel.req_com("mac_qstop 0x%x"%(qselect))
        return int(res, 16) 

    def mac_qstop_cancel(self,qselect):
        return  self.channel.req_com("mac_qstop_cancel 0x%x"%(qselect))

    def get_tx_send_cnt(self,clear=0,qsel=0):
        res = self.channel.req_com("get_tx_send_cnt 0x%x 0x%x"%(clear,qsel))
        return int(res, 16)

    def mac_tx_finish_check(self):
        res = self.channel.req_com("mac_tx_finish_check");
        return int(res, 16)

    def mac_tx_pmd_read(self,clear=0):
        '''
            rts_err txrx_cts tx_cts tx_data txrx_ack 
        '''
        res = self.channel.req_com("mac_tx_pmd_read 0x%x"%(clear)).split()
        return int(res[0], 16), int(res[1], 16), int(res[2], 16), int(res[3], 16), int(res[4], 16)

    def mac_qblock_read(self):
        
        res = self.channel.req_com("mac_qblock_read");
        return int(res, 16)

    def mac_tx_mutiq_start(self,
                        q0_loop = 0,
                        q1_loop = 0,
                        q2_loop = 0,
                        q3_loop = 0,
                        q4_loop = 0,
                        q5_loop = 0,
                        q6_loop = 0,
                        q7_loop = 0,
                        qmap = 1
                        ):
        
        return self.channel.req_com("mac_tx_mutiq_start 0x%x 0x%x 0x%x 0x%x 0x%x 0x%x 0x%x 0x%x 0x%x"%
                                    (q0_loop,q1_loop,q2_loop,q3_loop,q4_loop,q5_loop,q6_loop,q7_loop,qmap))

    def mac_tx_col_read(self,clear=0,qnum=0):
        
        res = self.channel.req_com("mac_tx_col_read 0x%x 0x%x"%(clear,qnum))
        return int(res, 16)

    def rx_ovf_cnt_read(self,clear=0):
        
        res = self.channel.req_com("rx_ovf_cnt_read 0x%x"%(clear))
        return int(res, 16)

    def time0_tar_set(self,data_type=0,data=0):
        '''
            data_type=0: set min alarm time
            data_type=1: set max alram time
        '''        
        return self.channel.req_com("time0_tar_set 0x%x 0x%x"%(data_type,data))

    def fill_tx_buffer(self, is_first=1, qnum=0, src_num=0, eof = 1, ampdu =0, data_len=100):
        '''
            init a tx buffer
        '''
        return self.channel.req_com("fill_tx_buffer 0x%x 0x%x 0x%x 0x%x 0x%x 0x%x"%
                                    (is_first,qnum,src_num,eof,ampdu,data_len))

    def get_free_buffer(self,qnum=0):
        '''
            get a free buffer from TX buffer pool
        '''
        res = self.channel.req_com("get_free_buffer 0x%x"%(qnum))
        return int(res, 16)

    def get_buffer_link(self,buffer_num=0):
        res = self.channel.req_com("get_buffer_link 0x%x"%(buffer_num))
        return int(res,16)

    def fill_ampdu_header(self,buffer_num,ampdu_header):        
        return self.channel.req_com("fill_ampdu_header 0x%x 0x%x"%(buffer_num,ampdu_header))

    def get_total_buffer_num(self,is_tx=0):
        '''
            get total buffer num. 
            is_tx=1: get tx buffer num
            is_tx=0: get rx buffer num
        '''
        res = self.channel.req_com("get_total_buffer_num 0x%x"%(is_tx))
        return int(res, 16)

    def set_ba_level(self,level1=0,level2=0,level3=0,level4=0):
        '''
            set ba level: 4 levels in all, and level1 > ...2 > ...3 > level4
        '''
        if not (level1>=level2 and level2>=level3 and level3>=level4):
            logerror("level1 > ...2 > ...3 > level4");
            return self.channel.req_com("set_ba_level 0x%x 0x%x 0x%x 0x%x"%(0,0,0,0))
        return self.channel.req_com("set_ba_level 0x%x 0x%x 0x%x 0x%x"%(level1,level2,level3,level4))

    def get_ba_num(self, clear=0):
        res = self.channel.req_com("get_ba_num 0x%x"%(clear)).split()
        return int(res[0], 16), int(res[1], 16), int(res[2], 16), int(res[3], 16)
