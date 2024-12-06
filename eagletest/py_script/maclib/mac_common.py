from baselib.loglib.log_lib import *
from hal.hwregister.hwreg.all import *
from hal.common import MEM
from hal.wifimac import WIFIMAC
from hal.common import CHIP_ID
from collections import OrderedDict
from maclib.define import *
import time

class RxLinkDscr(object):
    """docstring for Rx"""
    def __init__(self, channel, chipv , base):
        self._mem = MEM(channel, chipv)
        _link0 = self._mem.rd(base)    
        _link1 = self._mem.rd(base + 4)
        _link2 = self._mem.rd(base + 8)
        self.buf_ptr = _link1
        self.next_lk_ptr = _link2
        self.size = _link0 & 0xfff
        self.length = (_link0 >> 12) & 0xfff
        self.owner = (_link0 >> 31) & 0x1
        self.eof = (_link0 >> 30) & 0x1
        self.sub_sof = (_link0 >> 29) & 0x1
        self.struct_size = 12

class RXCTRL(object):
    """
    :base:
        buffer ptr
    """
    def __init__(self, channel, chipv , rxbase):
        self.chipv = chipv
        self._mem = MEM(channel, chipv)
        self._hwreg = HWREG(channel, chipv)
        res_buffer = self._hwreg.MAC_RX.MACRXBUF_CONF.reg_rxresbuf_size

        base = rxbase + res_buffer
        _d0 = self._mem.rd(base)     
        _d1 = self._mem.rd(base + 4) 
        _d2 = self._mem.rd(base + 8) 
        _d3 = self._mem.rd(base + 12)
        _d4 = self._mem.rd(base + 16)
        _d5 = self._mem.rd(base + 20)
        _d6 = self._mem.rd(base + 24)
        _d7 = self._mem.rd(base + 28)
        _d8 = self._mem.rd(base + 32)

        self.rxmatch3 = (_d0 >> 31) & 0x1
        self.rxmatch2 = (_d0 >> 30) & 0x1
        self.rxmatch1 = (_d0 >> 29) & 0x1
        self.rxmatch0 = (_d0 >> 28) & 0x1
        self.legacy_length = (_d0 >> 16) & 0xfff
        self.sig_mode =      (_d0 >> 14) & 0x3
        self.cur_service =   (_d0 >> 13) & 0x1
        self.rate =          (_d0 >> 8)  & 0xf
        self.rssi =          (_d0 >> 0)  & 0xf
        if self.sig_mode == 3:
            self.vhtsiga = _d1 | (_d5&0x3 <<32)
            self.vhtsigb = _d6 & 0xffffff
        else:
            self.SGI = (_d1 >> 31) & 0x1
            self.FEC_CODING = (_d1 >> 30) & 0x1
            self.STBC = (_d1 >> 28) & 0x3
            self.Aggregation = (_d1 >> 27) & 0x1
            self.Not_Sounding = (_d1 >> 25) & 0x1
            self.Smoothing = (_d1 >> 24) & 0x1
            self.HT_length = (_d1 >> 8) & 0xffff
            self.CWB = (_d1 >> 7) & 0x1
            self.MCS = (_d1 >> 0) & 0x7f

        self.isgroup = (_d2 >> 31) & 0x1
        self.rxstart_time_cycle = (_d2 >> 24) & 0x7f
        self.ampdu_cnt = (_d2 >> 8) & 0xff
        self.rxend_state = (_d2 >> 0) & 0xff

        self.timestamp = _d3
        self.bb_info = _d4
        if chipv   == "FPGA723":
            self.ant_status = (_d6 >> 31) & 0x1
            self.rxstart_time_cycle_dec = (_d6 >> 20) & 0x7ff
            self.rx_channel_estimate_len = (_d6 >> 8) & 0x3ff            
        else:
            self.ant_status = (_d5 >> 31) & 0x1
            self.rxstart_time_cycle_dec = (_d5 >> 20) & 0x7ff
            self.rx_channel_estimate_len = (_d5 >> 8) & 0x3ff

        if self.chipv == "FPGA723":
            self.rx_state = (_d8 >> 24) & 0xff
            self.dump_len = (_d8 >> 12) & 0xfff
            self.sig_len  = (_d8 >> 0) & 0xfff
        elif self.chipv == "FPGA722":
            self.rx_state = (_d7 >> 24) & 0xff
            self.dump_len = (_d7 >> 12) & 0xfff
            self.sig_len  = (_d7 >> 0) & 0xfff
        else:
            self.rx_state = (_d6 >> 24) & 0xff
            self.dump_len = (_d6 >> 12) & 0xfff
            self.sig_len  = (_d6 >> 0) & 0xfff

        if self.chipv == "FPGA723":
            self.struct_size = 36 + res_buffer
        elif self.chipv == "FPGA722":
            self.struct_size = 32 + res_buffer
        else:
            self.struct_size = 28 + res_buffer

class TXPMD(object):
    """docstring for TXPMD"""
    def __init__(self, channel, chipv):
        self.channel = channel
        self._hwreg = HWREG(channel, chipv)

    @property
    def txcomp_st(self):
        return self._hwreg.MAC_TXQMEM.MACTXQ0PMD.reg & 0xffff

    @property
    def txcomplete_num(self):
        return self._hwreg.MAC_TXQMEM.MACTXQ0PMD.txq0complete_num

    @property
    def txq_txstart_us(self):
        '''
        :return:
            (us, cycle@80M)
        '''
        return self._hwreg.MAC_TXQMEM.MACTXQ0_TXSTART_US.txq0_txstart_us, self._hwreg.MAC_TXQMEM.MACTXQ0_TXSTART_CYC.txq0_txstart_cycle

class TXCTRL(object):
    """docstring for TXHEAD"""
    def __init__(self, channel, chipv , base):
        self.channel = channel
        self._mem = MEM(channel, chipv)
        self._addr = base

    @property
    def aifs(self):
        return self._mem.rdm(self._addr, 15, 0)
    @aifs.setter
    def aifs(self, value):
        return self._mem.wrm(self._addr, 15, 0, value)
        
    @property
    def backoff(self):
        return self._mem.rdm(self._addr, 31, 16)
    @backoff.setter
    def backoff(self, value):
        return self._mem.wrm(self._addr, 31, 16, value)
    
    @property
    def sig_mode(self):
        return self._mem.rdm(self._addr+4, 15, 0)
    @sig_mode.setter
    def sig_mode(self, value):
        return self._mem.wrm(self._addr+4, 15, 0, value)
    
    @property
    def rate(self):
        return self._mem.rdm(self._addr+4, 15, 0)
    @rate.setter
    def rate(self, value):
        return self._mem.wrm(self._addr+4, 15, 0, value)
        
    @property
    def SGI(self):
        return self._mem.rdm(self._addr+4, 31, 16)
    @SGI.setter
    def SGI(self, value):
        return self._mem.wrm(self._addr+4, 31, 16, value)
        
    @property
    def CWB(self):
        return self._mem.rdm(self._addr+8, 15, 0)
    @CWB.setter
    def CWB(self, value):
        return self._mem.wrm(self._addr+8, 15, 0, value)
  
    @property
    def length(self):
        return self._mem.rdm(self._addr+8, 31, 16)
    @length.setter
    def length(self, value):
        return self._mem.wrm(self._addr+8, 31, 16, value)
        
    @property
    def txrts(self):
        return self._mem.rdm(self._addr+12, 15, 0)
    @txrts.setter
    def txrts(self, value):
        return self._mem.wrm(self._addr+12, 15, 0, value)
        
    @property
    def txcts(self):
        return self._mem.rdm(self._addr+12, 31, 16)
    @txcts.setter
    def txcts(self, value):
        return self._mem.wrm(self._addr+12, 31, 16, value)
        
    @property
    def txop(self):
        return self._mem.rdm(self._addr+16, 15, 0)
    @txop.setter
    def txop(self, value):
        return self._mem.wrm(self._addr+16, 15, 0, value)
        
    @property
    def waitack(self):
        return self._mem.rdm(self._addr+16, 31, 16)
    @waitack.setter
    def waitack(self, value):
        return self._mem.wrm(self._addr+16, 31, 16, value)    

    @property
    def Aggregation(self):
        return self._mem.rdm(self._addr+20, 15, 0)
    @CWB.setter
    def Aggregation(self, value):
        return self._mem.wrm(self._addr+20, 15, 0, value)
    

    def txq_init(self,qsel=0):
        self.channel.req_com("txq_init 0x%x"%qsel)
    
class MACHEAD(object):
    """
    :base:
        TX packet ptr
    """
    def __init__(self, channel, chipv , base):
        self._mem = MEM(channel, chipv)
        self._addr = base
    
    @property
    def fc(self):
        return self._mem.rdm(self._addr, 15, 0)
    @fc.setter
    def fc(self, value):
        return self._mem.wrm(self._addr, 15, 0, value)

    @property
    def duration(self):
        return self._mem.rdm(self._addr, 31, 16) 
    @duration.setter
    def duration(self, value):
        return self._mem.wrm(self._addr, 31, 16, value)

    @property
    def addr0(self):
        return self._mem.rd(self._addr+4) |  (self._mem.rd(self._addr+8) & 0xffff) <<32
    @addr0.setter
    def addr0(self, value):
        self._mem.wr(self._addr+4, value&0xffffffff)
        self._mem.wrm(self._addr+8, 15, 0, value>>32)
    
    @property
    def addr1(self):
        return ((self._mem.rd(self._addr+8) >> 16) & 0xffff) | self._mem.rd(self._addr+12) << 16
    @addr1.setter
    def addr1(self, value):
        self._mem.wrm(self._addr+8, 31, 16, value&0xffff)
        self._mem.wr(self._addr+12, value>>16 & 0xffffffff)
    
    @property
    def addr2(self):
        return self._mem.rd(self._addr+16) |  (self._mem.rd(self._addr+20) & 0xffff) <<32
    @addr2.setter
    def addr2(self, value):
        self._mem.wr(self._addr+16, value&0xffffffff)
        self._mem.wrm(self._addr+20, 15, 0, value>>32)

    @property
    def sequence(self):
        return self._mem.rdm(self._addr+20, 31, 16) 
    @addr2.setter
    def sequence(self, value):
        return self._mem.wrm(self._addr+20, 31, 16, value)

    @property
    def qos(self):
        return self._mem.rdm(self._addr+24, 15, 0) 
    @addr2.setter
    def qos(self, value):
        return self._mem.wrm(self._addr+24, 15, 0, value)


class mac_dbg(object):
    """docstring for mac_dbg"""
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.hwreg = HWREG(self.channel, self.chipv)
        self.mem = MEM(self.channel, self.chipv)        
        self.wifimac = WIFIMAC(self.channel, self.chipv)

    def dbg_rxstatus(self):
        logsetlevel("INFO")
        loginfo("="*50)
        loginfo("%s %d"%("MACRX_CCK_ERRCNT           ",self.hwreg.MAC_RX.MACRX_CCK_ERRCNT.reg))
        loginfo("%s %d"%("MACRX_AGC_ERRCNT           ",self.hwreg.MAC_RX.MACRX_AGC_ERRCNT.reg))
        loginfo("%s %d"%("MACRX_SF_CNT               ",self.hwreg.MAC_RX.MACRX_SF_CNT.reg))
        loginfo("%s %d"%("MACRX_ABORT_CNT            ",self.hwreg.MAC_RX.MACRX_ABORT_CNT.reg))
        loginfo("%s %d"%("MACRX_FCS_ERRCNT           ",self.hwreg.MAC_RX.MACRX_FCS_ERRCNT.reg))
        loginfo("%s %d"%("MACRX_FIFO_OVFCNT          ",self.hwreg.MAC_RX.MACRX_FIFO_OVFCNT.reg))
        loginfo("%s %d"%("MACRX_APENTRYBUF_FULLCNT   ",self.hwreg.MAC_RX.MACRX_APENTRYBUF_FULLCNT.reg))
        loginfo("%s %d"%("MACRX_BUF_FULLCNT          ",self.hwreg.MAC_RX.MACRX_BUF_FULLCNT.reg))
        loginfo("%s %d"%("MACRX_OTHER_UNICASTCNT     ",self.hwreg.MAC_RX.MACRX_OTHER_UNICASTCNT.reg))
        loginfo("%s %d"%("MACRX_TKIP_ERRCNT          ",self.hwreg.MAC_RX.MACRX_TKIP_ERRCNT.reg))
        loginfo("%s %d"%("MACRX_SAMEBM_ERRCNT        ",self.hwreg.MAC_RX.MACRX_SAMEBM_ERRCNT.reg))
        loginfo("%s %d"%("MACRXACK_INT_CNT           ",self.hwreg.MAC_RX.MACRXACK_INT_CNT.reg))
        loginfo("%s %d"%("MACRXRTS_INT_CNT           ",self.hwreg.MAC_RX.MACRXRTS_INT_CNT.reg))
        loginfo("%s %d"%("MACRXCTS_INT_CNT           ",self.hwreg.MAC_RX.MACRXCTS_INT_CNT.reg))
        loginfo("%s %d"%("MACRXRIFS_INT_CNT          ",self.hwreg.MAC_RX.MACRXRIFS_INT_CNT.reg))
        loginfo("%s %d"%("MACRX_DATASUC_CNT          ",self.hwreg.MAC_RX.MACRX_DATASUC_CNT.reg))
        loginfo("%s %d"%("MACRX_END_CNT              ",self.hwreg.MAC_RX.MACRX_END_CNT.reg))
        loginfo("%s %d"%("MACRX_BTBLOCK_ERR_CNT      ",self.hwreg.MAC_RX.MACRX_BTBLOCK_ERR_CNT.reg))
        loginfo("%s %d"%("MACRX_FREQHOP_ERR_CNT      ",self.hwreg.MAC_RX.MACRX_FREQHOP_ERR_CNT.reg))
        loginfo("%s %d"%("MACRX_LASTUNMATCH_ERR_CNT  ",self.hwreg.MAC_RX.MACRX_LASTUNMATCH_ERR_CNT.reg))
        loginfo("%s %d"%("MACRX_BLOCK_ERR_CNT        ",self.hwreg.MAC_RX.MACRX_BLOCK_ERR_CNT.reg))
        loginfo("="*50)
        loginfo("%s 0x%x"%("SCH DIAG0                  ",self.hwreg.MAC_SCH.MACDIAG0.reg))
        loginfo("%s 0x%x"%("SCH DIAG1                  ",self.hwreg.MAC_SCH.MACDIAG1.reg))
        loginfo("%s 0x%x"%("SCH DIAG2                  ",self.hwreg.MAC_SCH.MACDIAG2.reg))
        loginfo("%s 0x%x"%("SCH DIAG3                  ",self.hwreg.MAC_SCH.MACDIAG3.reg))
        loginfo("="*50)
        loginfo("%s 0x%x"%("RX  DIAG4                  ",self.hwreg.MAC_RX.MACDIAG4.reg))
        loginfo("%s 0x%x"%("RX  DIAG5                  ",self.hwreg.MAC_RX.MACDIAG5.reg))
        loginfo("%s 0x%x"%("RX  DIAG6                  ",self.hwreg.MAC_RX.MACDIAG6.reg))
        loginfo("%s 0x%x"%("RX  DIAG7                  ",self.hwreg.MAC_RX.MACDIAG7.reg))
        logsetlevel("DEBUG")



    def dbg_showrxlink_full(self):
        '''
        Get current rxhead and rxtail
        '''
        link_addr = self.wifimac.dbg_rx_link()[0]
        self.dbg_dump_link(link_addr)

    def dbg_showrxlink(self):
        '''
        Get current rxhead and rxtail
        '''
        link_addr = self.wifimac.get_rxpacket_buffer()
        self.dbg_dump_link(link_addr)

    def dbg_showtxlink(self):
        '''
        Get current rxhead and rxtail
        '''
        link_addr = self.wifimac.get_txpacket_buffer(0)[1]
        self.dbg_dump_link(link_addr)

    def dbg_showrxbuffer(self, buflen = 40):
        link_addr = self.wifimac.get_rxpacket_buffer()
        self.dbg_dump_buffer(link_addr, buflen)

    def dbg_showtxbuffer(self, buflen = 40):
        link_addr = self.wifimac.get_txpacket_buffer(0)[1]
        self.dbg_dump_buffer(link_addr, buflen)


    def dbg_dump_link(self, base):
        link_addr = base
        while True:
            loginfo("="*10)
            loginfo("** 0x%x **"%link_addr)
            rxlink = RxLinkDscr(self.channel, self.chipv, link_addr)
            loginfo("owner      ", rxlink.owner)
            loginfo("eof        ", rxlink.eof)
            loginfo("sub_sof    ", rxlink.sub_sof)
            loginfo("size       ", rxlink.size)
            loginfo("length     ", rxlink.length)
            loginfo("buf_ptr     0x%x"%rxlink.buf_ptr)
            loginfo("next_lk_ptr 0x%x"%rxlink.next_lk_ptr)
            if rxlink.buf_ptr & 0x3ff00000 != 0x3ff00000:
                break
            elif rxlink.next_lk_ptr & 0x3ff00000 != 0x3ff00000:
                break
            link_addr = rxlink.next_lk_ptr

    def dbg_dump_buffer(self, base, buflen):
        '''
        :base:
            rxbase, u can get it by call *get_rxpacket_buffer()*
        :buflen:
            dump length
        '''
        link_addr = base
        left_buflen = (buflen>>2)<<2 + 4
        buffer_con = OrderedDict()
        while True:
            if left_buflen < 4 or (link_addr & 0x3ff00000 != 0x3ff00000):
                break
            rxlink = RxLinkDscr(self.channel, self.chipv, link_addr)
            if rxlink.buf_ptr & 0x3ff00000 != 0x3ff00000:
                logerror("link error")
                break
            link_addr = rxlink.next_lk_ptr

            buffer_con[rxlink.buf_ptr] = []
            if rxlink.size >= left_buflen:
                dump_len = left_buflen
            else:
                dump_len = rxlink.size
            left_buflen = left_buflen - dump_len

            for i in range(rxlink.buf_ptr, rxlink.buf_ptr + dump_len, 4):
                buffer_con[rxlink.buf_ptr].append(self.mem.rd(i))

        head_flag = True
        for k,v in buffer_con.items():
            if head_flag:
                rxctrl = RXCTRL(self.channel, self.chipv, k)  
            for index, d in enumerate(v):
                if index%8 == 0 and index != 0:
                    split_size = 0
                    if head_flag:
                        if (index > rxctrl.struct_size/4) and (rxctrl.struct_size/4 > index - 8):
                            split_size = (rxctrl.struct_size/4)%8
                        elif (index > (rxctrl.struct_size + rxctrl.rx_channel_estimate_len)/4) and ((rxctrl.struct_size + rxctrl.rx_channel_estimate_len)/4 > index -8):
                            split_size = ((rxctrl.struct_size + rxctrl.rx_channel_estimate_len)/4)%8
                    data = [v[index-8], v[index-7], v[index-6], v[index-5], v[index-4], v[index-3], v[index-2], v[index-1]]
                    self.__show(k+(index-8)*4, data, split_size)
            if head_flag:
                head_flag = False

    def __show(self, addr, data, split_size):
        if split_size == 0:
            loginfo("0x%08x: 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x 0x%08x"%(addr, data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
        else:
            d0 = "0x%x: "%addr
            d1 = "0x%x: "%addr
            for i in range(0,8):
                if i <= split_size-1:
                    d0 = d0 + "0x%08x"%data[i] + " "
                    d1 = d1 + "="*10 + " "
                else:
                    d1 = d1 + "0x%08x"%data[i] + " "
                    d0 = d0 + "="*10 + " "
            loginfo(d0)
            loginfo(d1)

class mac_common(object):
    """docstring for mac_common"""
        
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.wifimac = WIFIMAC(self.channel, self.chipv)
        self.dbg = mac_dbg(self.channel, self.chipv)
        self._mem = MEM(self.channel, self.chipv)

    def __checkhead(self):
        hwreg = HWREG(self.channel, self.chipv)
        if not (hwreg.MAC_TX.MACTXDATE.reg ==  hwreg.MAC_TX.MACTXDATE.default_value):
            logerror("register MAC_TX unmatch 0x%x 0x%x"%(hwreg.MAC_TX.MACTXDATE.reg, hwreg.MAC_TX.MACTXDATE.default_value))

        if not (hwreg.MAC_RX.MACRXDATE.reg ==  hwreg.MAC_RX.MACRXDATE.default_value):
            logerror("register MAC_RX unmatch 0x%x 0x%x"%(hwreg.MAC_RX.MACRXDATE.reg, hwreg.MAC_RX.MACRXDATE.default_value))

        if not (hwreg.MAC_SCH.MACSCHDATE.reg ==  hwreg.MAC_SCH.MACSCHDATE.default_value):
            logerror("register MAC_SCH unmatch 0x%x 0x%x"%(hwreg.MAC_SCH.MACSCHDATE.reg, hwreg.MAC_SCH.MACSCHDATE.default_value))

        if not (hwreg.MAC_TXQMEM.MACTXMEMQDATE.reg ==  hwreg.MAC_TXQMEM.MACTXMEMQDATE.default_value):
            logerror("register MAC_TXQMEM unmatch 0x%x 0x%x"%(hwreg.MAC_TXQMEM.MACTXMEMQDATE.reg, hwreg.MAC_TXQMEM.MACTXMEMQDATE.default_value))

        if not (hwreg.MAC_SEC.MACSECDATE.reg ==  hwreg.MAC_SEC.MACSECDATE.default_value):
            logerror("register MAC_SEC unmatch 0x%x 0x%x"%(hwreg.MAC_SEC.MACSECDATE.reg, hwreg.MAC_SEC.MACSECDATE.default_value))


    def mac_txrx_init(self, rfchannel, rfchmd = 0, qmap = 1):
        '''
        1. mac init
        2. set channel
        3. suit initerrput 
        '''
        if not self.wifimac.check_macinit():
            self.wifimac.mac_init(qmap)
            loginfo("mac init first time")
            if self.chipv in ("FPGA722", "FPGA723"):
                time.sleep(15)
            else:
                time.sleep(1)
        self.__checkhead()
        if self.chipv == "FPGA723":
            self._mem.wr(0x6000456c, 0xd8)
            self._mem.wr(0x60004570, 0xd7)
            self._mem.wr(0x6001c11c, 0xf000)
            loginfo("ant GPIO init on FPGA")
        self.wifimac.RFChannelSel(rfchannel, rfchmd)
        self.wifimac.mac_int_suit()


    def set_rx_conf(self, mode = 0):
        chip_mac = int(CHIP_ID(self.channel, self.chipv).chip_mac(), 16)
        self.wifimac.set_rx_addr(0, chip_mac, chip_mac)
        self.wifimac.set_rx_filter(0, mode)
        self.wifimac.mac_rx_start()
        return chip_mac

    def set_tx_packet(self, addr, 
                    rate = 0xb, 
                    sgi = 0,
                    cwb = 0,
                    length= 100,
                    qsel = 0,
                    is_first=1,                    
                    eof=1,
                    ampdu=0,
                    delim_num=4):

        txbase = self.wifimac.get_txpacket_buffer(qsel)
        
        txctrl = TXCTRL(self.channel, self.chipv, txbase[0])
        
        '''
            add to enable TX buffer alloc 
        '''
        buf_num = self.wifimac.get_free_buffer(qsel)
        if buf_num > 0xffff:
            logerror('No free tx buffer')
            return

        self.wifimac.fill_tx_buffer(is_first,qsel,buf_num,eof,ampdu,length)

        txlink = RxLinkDscr(self.channel, self.chipv, self.wifimac.get_buffer_link(buf_num))


        if ampdu==1 :
            self.wifimac.fill_ampdu_header(buf_num,(delim_num<<12) | length)
            machead = MACHEAD(self.channel, self.chipv, (txlink.buf_ptr+4))
        else:
            machead = MACHEAD(self.channel, self.chipv, txlink.buf_ptr)
        
        '''
            add end
        '''
        
        chip_mac = int(CHIP_ID(self.channel, self.chipv).chip_mac(), 16)
        self.wifimac.set_rx_addr(0, chip_mac, chip_mac)
        if ampdu==1:
            machead.fc = 0x0088
            machead.qos = 0
        else:
            machead.fc = 0x0008
        machead.addr0 = addr
        machead.addr1 = chip_mac
        machead.addr2 = addr

        txctrl.rate = rate
        txctrl.SGI = sgi
        txctrl.CWB = cwb
        txctrl.Aggregation = ampdu
        if is_first==1:
            if ampdu == 1:
                txctrl.length = length + 4*(delim_num+1)
            else:
                txctrl.length = length
        else:
            if ampdu == 1 :
                if eof == 1:
                    txctrl.length = txctrl.length + length + 4
                else:
                    txctrl.length = txctrl.length + length + 4*(delim_num+1)
            else:
                txctrl.length = txctrl.length + length
        txctrl.txq_init(qsel)
        return txlink

    def tx_q_conf(self,
                    cts = 0,
                    rts = 0,
                    ack = 0,
                    txop = 0,
                    aifs = 10,
                    qsel = 0,
                    backoff = 0):
        txbase = self.wifimac.get_txpacket_buffer(qsel)
        txctrl = TXCTRL(self.channel, self.chipv, txbase[0])
        txctrl.txcts = cts
        txctrl.txrts = rts
        txctrl.txop = txop
        txctrl.waitack =ack
        txctrl.backoff = backoff 
        txctrl.aifs = 3
        txctrl.txq_init(qsel)

    def CSI(self, enable=1):
        if self.chipv in ("FPGA722"):
            hwreg = HWREG(self.channel, self.chipv)
            if enable:
                hwreg.NRX.NRXCHANDUMP.reg_chan_dump_bypass_test = 0
                hwreg.MAC_RX.MACRXOPTION.reg_rxchaest_dump_ena = 1
                hwreg.MAC_RX.MACRXOPTION.reg_rxbuf_est_close = 0
                hwreg.MAC_RX.MACRXOPTION.reg_rxbuf_dump_est_ena = 1
            else:
                hwreg.NRX.NRXCHANDUMP.reg_chan_dump_bypass_test = 1
                hwreg.MAC_RX.MACRXOPTION.reg_rxchaest_dump_ena = 1
                hwreg.MAC_RX.MACRXOPTION.reg_rxbuf_est_close = 0
                hwreg.MAC_RX.MACRXOPTION.reg_rxbuf_dump_est_ena = 0

class get_rxpacket(object):
    """docstring for get_rxpacket"""
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.wifimac = WIFIMAC(self.channel, self.chipv)        
        while True:
            self.rxbase = self.wifimac.get_rxpacket_buffer()
            if self.rxbase&0x3ff00000 == 0x3ff00000:
                break

    def __enter__(self):
        return self.rxbase

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.wifimac.set_free_rxprandom_stopfer()
