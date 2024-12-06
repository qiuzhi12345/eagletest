from hal.common import *
from hal.hwregister.hwreg.CHIP722.addr_base import *
class MAC_RX(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.MACBSSID0LO = MACBSSID0LO(self.channel, self.chipv)
        self.MACBSSID0HI = MACBSSID0HI(self.channel, self.chipv)
        self.MACBSSID1LO = MACBSSID1LO(self.channel, self.chipv)
        self.MACBSSID1HI = MACBSSID1HI(self.channel, self.chipv)
        self.MACBSSID2LO = MACBSSID2LO(self.channel, self.chipv)
        self.MACBSSID2HI = MACBSSID2HI(self.channel, self.chipv)
        self.MACBSSID3LO = MACBSSID3LO(self.channel, self.chipv)
        self.MACBSSID3HI = MACBSSID3HI(self.channel, self.chipv)
        self.MACBSSID0_MASKLO = MACBSSID0_MASKLO(self.channel, self.chipv)
        self.MACBSSID0_MASKHI = MACBSSID0_MASKHI(self.channel, self.chipv)
        self.MACBSSID1_MASKLO = MACBSSID1_MASKLO(self.channel, self.chipv)
        self.MACBSSID1_MASKHI = MACBSSID1_MASKHI(self.channel, self.chipv)
        self.MACBSSID2_MASKLO = MACBSSID2_MASKLO(self.channel, self.chipv)
        self.MACBSSID2_MASKHI = MACBSSID2_MASKHI(self.channel, self.chipv)
        self.MACBSSID3_MASKLO = MACBSSID3_MASKLO(self.channel, self.chipv)
        self.MACBSSID3_MASKHI = MACBSSID3_MASKHI(self.channel, self.chipv)
        self.MACDA0LO = MACDA0LO(self.channel, self.chipv)
        self.MACDA0HI = MACDA0HI(self.channel, self.chipv)
        self.MACDA1LO = MACDA1LO(self.channel, self.chipv)
        self.MACDA1HI = MACDA1HI(self.channel, self.chipv)
        self.MACDA2LO = MACDA2LO(self.channel, self.chipv)
        self.MACDA2HI = MACDA2HI(self.channel, self.chipv)
        self.MACDA3LO = MACDA3LO(self.channel, self.chipv)
        self.MACDA3HI = MACDA3HI(self.channel, self.chipv)
        self.MACDA0_MASKLO = MACDA0_MASKLO(self.channel, self.chipv)
        self.MACDA0_MASKHI = MACDA0_MASKHI(self.channel, self.chipv)
        self.MACDA1_MASKLO = MACDA1_MASKLO(self.channel, self.chipv)
        self.MACDA1_MASKHI = MACDA1_MASKHI(self.channel, self.chipv)
        self.MACDA2_MASKLO = MACDA2_MASKLO(self.channel, self.chipv)
        self.MACDA2_MASKHI = MACDA2_MASKHI(self.channel, self.chipv)
        self.MACDA3_MASKLO = MACDA3_MASKLO(self.channel, self.chipv)
        self.MACDA3_MASKHI = MACDA3_MASKHI(self.channel, self.chipv)
        self.MACRXBUF_CONF = MACRXBUF_CONF(self.channel, self.chipv)
        self.MACRXESTMODE = MACRXESTMODE(self.channel, self.chipv)
        self.MACRXMODE = MACRXMODE(self.channel, self.chipv)
        self.MACRXESTBASE = MACRXESTBASE(self.channel, self.chipv)
        self.MACRXBASE = MACRXBASE(self.channel, self.chipv)
        self.MACRXBUFDSCR_NEXT = MACRXBUFDSCR_NEXT(self.channel, self.chipv)
        self.MACRXBUFDSCR_LAST = MACRXBUFDSCR_LAST(self.channel, self.chipv)
        self.MACRXBUFBK_CNT = MACRXBUFBK_CNT(self.channel, self.chipv)
        self.MACRXBUFDSCR_START = MACRXBUFDSCR_START(self.channel, self.chipv)
        self.MACRXOPTION = MACRXOPTION(self.channel, self.chipv)
        self.MACRX_ABORT_CONF = MACRX_ABORT_CONF(self.channel, self.chipv)
        self.MACRXPMD = MACRXPMD(self.channel, self.chipv)
        self.MACRXPLCP = MACRXPLCP(self.channel, self.chipv)
        self.MACRXHTSIG1 = MACRXHTSIG1(self.channel, self.chipv)
        self.MACRXHTSIG2 = MACRXHTSIG2(self.channel, self.chipv)
        self.MACRXMPDU0 = MACRXMPDU0(self.channel, self.chipv)
        self.MACRXMPDU1 = MACRXMPDU1(self.channel, self.chipv)
        self.MACRXMPDU2 = MACRXMPDU2(self.channel, self.chipv)
        self.MACRXMPDU3 = MACRXMPDU3(self.channel, self.chipv)
        self.MACRXMPDU4 = MACRXMPDU4(self.channel, self.chipv)
        self.MACRXMPDU5 = MACRXMPDU5(self.channel, self.chipv)
        self.MACRXMPDU6 = MACRXMPDU6(self.channel, self.chipv)
        self.MACRXMPDU7 = MACRXMPDU7(self.channel, self.chipv)
        self.MACRX_CONF = MACRX_CONF(self.channel, self.chipv)
        self.MACRX_ABORT0 = MACRX_ABORT0(self.channel, self.chipv)
        self.MACRX_ABORT1 = MACRX_ABORT1(self.channel, self.chipv)
        self.MACRX_ABORT2 = MACRX_ABORT2(self.channel, self.chipv)
        self.MACRX_ABORT3 = MACRX_ABORT3(self.channel, self.chipv)
        self.MACRX_DUMP0_ERRCODE = MACRX_DUMP0_ERRCODE(self.channel, self.chipv)
        self.MACRX_DUMP1_ERRCODE = MACRX_DUMP1_ERRCODE(self.channel, self.chipv)
        self.MACRX_DUMP2_ERRCODE = MACRX_DUMP2_ERRCODE(self.channel, self.chipv)
        self.MACRX_DUMP3_ERRCODE = MACRX_DUMP3_ERRCODE(self.channel, self.chipv)
        self.MACRX_DUMP3_ERRCODE1 = MACRX_DUMP3_ERRCODE1(self.channel, self.chipv)
        self.MACRX_DUMP3_ERRCODE2 = MACRX_DUMP3_ERRCODE2(self.channel, self.chipv)
        self.MACRX_DUMP0_LIM = MACRX_DUMP0_LIM(self.channel, self.chipv)
        self.MACRX_DUMP1_LIM = MACRX_DUMP1_LIM(self.channel, self.chipv)
        self.MACRX_DUMP2_LIM = MACRX_DUMP2_LIM(self.channel, self.chipv)
        self.MACRX_DUMP3_LIM = MACRX_DUMP3_LIM(self.channel, self.chipv)
        self.MACRXCTR_BSSIDLIST = MACRXCTR_BSSIDLIST(self.channel, self.chipv)
        self.MACRXQOS_BITMAPUP_LIST = MACRXQOS_BITMAPUP_LIST(self.channel, self.chipv)
        self.MACRX_FACKHT = MACRX_FACKHT(self.channel, self.chipv)
        self.MACRXBBTF_ENA = MACRXBBTF_ENA(self.channel, self.chipv)
        self.MACRXADDR_MAX = MACRXADDR_MAX(self.channel, self.chipv)
        self.MACRXADDR_MIN = MACRXADDR_MIN(self.channel, self.chipv)
        self.MACRXENT_MAX = MACRXENT_MAX(self.channel, self.chipv)
        self.MACRXENT_MIN = MACRXENT_MIN(self.channel, self.chipv)
        self.MACBBABORTOPTION = MACBBABORTOPTION(self.channel, self.chipv)
        self.MACBBNAVOPTION = MACBBNAVOPTION(self.channel, self.chipv)
        self.MACBBABORT_RSSITAB0 = MACBBABORT_RSSITAB0(self.channel, self.chipv)
        self.MACBBABORT_RSSITAB1 = MACBBABORT_RSSITAB1(self.channel, self.chipv)
        self.MACBBABORT_LENTAB0 = MACBBABORT_LENTAB0(self.channel, self.chipv)
        self.MACBBABORT_LENTAB1 = MACBBABORT_LENTAB1(self.channel, self.chipv)
        self.MACRX_TXACK_TIMER_CYC = MACRX_TXACK_TIMER_CYC(self.channel, self.chipv)
        self.MACRX_TXACK_TIMER_US = MACRX_TXACK_TIMER_US(self.channel, self.chipv)
        self.MACRX_DATA_DUMP_CONF = MACRX_DATA_DUMP_CONF(self.channel, self.chipv)
        self.MACRX_DATA_DUMP_CONF1 = MACRX_DATA_DUMP_CONF1(self.channel, self.chipv)
        self.MACRX_DATA_FILTER0_CONF = MACRX_DATA_FILTER0_CONF(self.channel, self.chipv)
        self.MACRX_DATA_FILTER1_CONF = MACRX_DATA_FILTER1_CONF(self.channel, self.chipv)
        self.MACRX_DATA_FILTER2_CONF = MACRX_DATA_FILTER2_CONF(self.channel, self.chipv)
        self.MACRX_DATA_FILTER3_CONF = MACRX_DATA_FILTER3_CONF(self.channel, self.chipv)
        self.MACRX_DATA_FILTER4_CONF = MACRX_DATA_FILTER4_CONF(self.channel, self.chipv)
        self.MACRX_DATA_FILTER5_CONF = MACRX_DATA_FILTER5_CONF(self.channel, self.chipv)
        self.MACRX_DATA_FILTER6_CONF = MACRX_DATA_FILTER6_CONF(self.channel, self.chipv)
        self.MACRX_DATA_FILTER0_DATA = MACRX_DATA_FILTER0_DATA(self.channel, self.chipv)
        self.MACRX_DATA_FILTER1_DATA = MACRX_DATA_FILTER1_DATA(self.channel, self.chipv)
        self.MACRX_DATA_FILTER2_DATA = MACRX_DATA_FILTER2_DATA(self.channel, self.chipv)
        self.MACRX_DATA_FILTER3_DATA = MACRX_DATA_FILTER3_DATA(self.channel, self.chipv)
        self.MACRX_DATA_FILTER4_DATA = MACRX_DATA_FILTER4_DATA(self.channel, self.chipv)
        self.MACRX_DATA_FILTER5_DATA = MACRX_DATA_FILTER5_DATA(self.channel, self.chipv)
        self.MACRX_DATA_FILTER6_DATA = MACRX_DATA_FILTER6_DATA(self.channel, self.chipv)
        self.MACRX_DATA_FILTER0_MASK = MACRX_DATA_FILTER0_MASK(self.channel, self.chipv)
        self.MACRX_DATA_FILTER1_MASK = MACRX_DATA_FILTER1_MASK(self.channel, self.chipv)
        self.MACRX_DATA_FILTER2_MASK = MACRX_DATA_FILTER2_MASK(self.channel, self.chipv)
        self.MACRX_DATA_FILTER3_MASK = MACRX_DATA_FILTER3_MASK(self.channel, self.chipv)
        self.MACRX_DATA_FILTER4_MASK = MACRX_DATA_FILTER4_MASK(self.channel, self.chipv)
        self.MACRX_DATA_FILTER5_MASK = MACRX_DATA_FILTER5_MASK(self.channel, self.chipv)
        self.MACRX_DATA_FILTER6_MASK = MACRX_DATA_FILTER6_MASK(self.channel, self.chipv)
        self.MACRXBA7_CONF = MACRXBA7_CONF(self.channel, self.chipv)
        self.MACRXBA7_TAHI = MACRXBA7_TAHI(self.channel, self.chipv)
        self.MACRXBA7_TALO = MACRXBA7_TALO(self.channel, self.chipv)
        self.MACRXBA7_WINCONF = MACRXBA7_WINCONF(self.channel, self.chipv)
        self.MACRXBA7_BMHI_SW = MACRXBA7_BMHI_SW(self.channel, self.chipv)
        self.MACRXBA7_BMLO_SW = MACRXBA7_BMLO_SW(self.channel, self.chipv)
        self.MACRXBA7_BMHI = MACRXBA7_BMHI(self.channel, self.chipv)
        self.MACRXBA7_BMLO = MACRXBA7_BMLO(self.channel, self.chipv)
        self.MACRXBA6_CONF = MACRXBA6_CONF(self.channel, self.chipv)
        self.MACRXBA6_TAHI = MACRXBA6_TAHI(self.channel, self.chipv)
        self.MACRXBA6_TALO = MACRXBA6_TALO(self.channel, self.chipv)
        self.MACRXBA6_WINCONF = MACRXBA6_WINCONF(self.channel, self.chipv)
        self.MACRXBA6_BMHI_SW = MACRXBA6_BMHI_SW(self.channel, self.chipv)
        self.MACRXBA6_BMLO_SW = MACRXBA6_BMLO_SW(self.channel, self.chipv)
        self.MACRXBA6_BMHI = MACRXBA6_BMHI(self.channel, self.chipv)
        self.MACRXBA6_BMLO = MACRXBA6_BMLO(self.channel, self.chipv)
        self.MACRXBA5_CONF = MACRXBA5_CONF(self.channel, self.chipv)
        self.MACRXBA5_TAHI = MACRXBA5_TAHI(self.channel, self.chipv)
        self.MACRXBA5_TALO = MACRXBA5_TALO(self.channel, self.chipv)
        self.MACRXBA5_WINCONF = MACRXBA5_WINCONF(self.channel, self.chipv)
        self.MACRXBA5_BMHI_SW = MACRXBA5_BMHI_SW(self.channel, self.chipv)
        self.MACRXBA5_BMLO_SW = MACRXBA5_BMLO_SW(self.channel, self.chipv)
        self.MACRXBA5_BMHI = MACRXBA5_BMHI(self.channel, self.chipv)
        self.MACRXBA5_BMLO = MACRXBA5_BMLO(self.channel, self.chipv)
        self.MACRXBA4_CONF = MACRXBA4_CONF(self.channel, self.chipv)
        self.MACRXBA4_TAHI = MACRXBA4_TAHI(self.channel, self.chipv)
        self.MACRXBA4_TALO = MACRXBA4_TALO(self.channel, self.chipv)
        self.MACRXBA4_WINCONF = MACRXBA4_WINCONF(self.channel, self.chipv)
        self.MACRXBA4_BMHI_SW = MACRXBA4_BMHI_SW(self.channel, self.chipv)
        self.MACRXBA4_BMLO_SW = MACRXBA4_BMLO_SW(self.channel, self.chipv)
        self.MACRXBA4_BMHI = MACRXBA4_BMHI(self.channel, self.chipv)
        self.MACRXBA4_BMLO = MACRXBA4_BMLO(self.channel, self.chipv)
        self.MACRXBA3_CONF = MACRXBA3_CONF(self.channel, self.chipv)
        self.MACRXBA3_TAHI = MACRXBA3_TAHI(self.channel, self.chipv)
        self.MACRXBA3_TALO = MACRXBA3_TALO(self.channel, self.chipv)
        self.MACRXBA3_WINCONF = MACRXBA3_WINCONF(self.channel, self.chipv)
        self.MACRXBA3_BMHI_SW = MACRXBA3_BMHI_SW(self.channel, self.chipv)
        self.MACRXBA3_BMLO_SW = MACRXBA3_BMLO_SW(self.channel, self.chipv)
        self.MACRXBA3_BMHI = MACRXBA3_BMHI(self.channel, self.chipv)
        self.MACRXBA3_BMLO = MACRXBA3_BMLO(self.channel, self.chipv)
        self.MACRXBA2_CONF = MACRXBA2_CONF(self.channel, self.chipv)
        self.MACRXBA2_TAHI = MACRXBA2_TAHI(self.channel, self.chipv)
        self.MACRXBA2_TALO = MACRXBA2_TALO(self.channel, self.chipv)
        self.MACRXBA2_WINCONF = MACRXBA2_WINCONF(self.channel, self.chipv)
        self.MACRXBA2_BMHI_SW = MACRXBA2_BMHI_SW(self.channel, self.chipv)
        self.MACRXBA2_BMLO_SW = MACRXBA2_BMLO_SW(self.channel, self.chipv)
        self.MACRXBA2_BMHI = MACRXBA2_BMHI(self.channel, self.chipv)
        self.MACRXBA2_BMLO = MACRXBA2_BMLO(self.channel, self.chipv)
        self.MACRXBA1_CONF = MACRXBA1_CONF(self.channel, self.chipv)
        self.MACRXBA1_TAHI = MACRXBA1_TAHI(self.channel, self.chipv)
        self.MACRXBA1_TALO = MACRXBA1_TALO(self.channel, self.chipv)
        self.MACRXBA1_WINCONF = MACRXBA1_WINCONF(self.channel, self.chipv)
        self.MACRXBA1_BMHI_SW = MACRXBA1_BMHI_SW(self.channel, self.chipv)
        self.MACRXBA1_BMLO_SW = MACRXBA1_BMLO_SW(self.channel, self.chipv)
        self.MACRXBA1_BMHI = MACRXBA1_BMHI(self.channel, self.chipv)
        self.MACRXBA1_BMLO = MACRXBA1_BMLO(self.channel, self.chipv)
        self.MACRXBA0_CONF = MACRXBA0_CONF(self.channel, self.chipv)
        self.MACRXBA0_TAHI = MACRXBA0_TAHI(self.channel, self.chipv)
        self.MACRXBA0_TALO = MACRXBA0_TALO(self.channel, self.chipv)
        self.MACRXBA0_WINCONF = MACRXBA0_WINCONF(self.channel, self.chipv)
        self.MACRXBA0_BMHI_SW = MACRXBA0_BMHI_SW(self.channel, self.chipv)
        self.MACRXBA0_BMLO_SW = MACRXBA0_BMLO_SW(self.channel, self.chipv)
        self.MACRXBA0_BMHI = MACRXBA0_BMHI(self.channel, self.chipv)
        self.MACRXBA0_BMLO = MACRXBA0_BMLO(self.channel, self.chipv)
        self.MACTXBA_BMHI = MACTXBA_BMHI(self.channel, self.chipv)
        self.MACTXBA_BMLO = MACTXBA_BMLO(self.channel, self.chipv)
        self.MACTXBA_TAHI = MACTXBA_TAHI(self.channel, self.chipv)
        self.MACTXBA_TALO = MACTXBA_TALO(self.channel, self.chipv)
        self.MACTXBA_SSN = MACTXBA_SSN(self.channel, self.chipv)
        self.MACRX_ANT_CONF = MACRX_ANT_CONF(self.channel, self.chipv)
        self.MACRX_STATIS_CLEAR = MACRX_STATIS_CLEAR(self.channel, self.chipv)
        self.MACRX_CCK_ERRCNT = MACRX_CCK_ERRCNT(self.channel, self.chipv)
        self.MACRX_OFDM_ERRCNT = MACRX_OFDM_ERRCNT(self.channel, self.chipv)
        self.MACRX_AGC_ERRCNT = MACRX_AGC_ERRCNT(self.channel, self.chipv)
        self.MACRX_SF_CNT = MACRX_SF_CNT(self.channel, self.chipv)
        self.MACRX_ABORT_CNT = MACRX_ABORT_CNT(self.channel, self.chipv)
        self.MACRX_FCS_ERRCNT = MACRX_FCS_ERRCNT(self.channel, self.chipv)
        self.MACRX_FIFO_OVFCNT = MACRX_FIFO_OVFCNT(self.channel, self.chipv)
        self.MACRX_APENTRYBUF_FULLCNT = MACRX_APENTRYBUF_FULLCNT(self.channel, self.chipv)
        self.MACRX_BUF_FULLCNT = MACRX_BUF_FULLCNT(self.channel, self.chipv)
        self.MACRX_OTHER_UNICASTCNT = MACRX_OTHER_UNICASTCNT(self.channel, self.chipv)
        self.MACRX_TKIP_ERRCNT = MACRX_TKIP_ERRCNT(self.channel, self.chipv)
        self.MACRX_SAMEBM_ERRCNT = MACRX_SAMEBM_ERRCNT(self.channel, self.chipv)
        self.MACRXACK_INT_CNT = MACRXACK_INT_CNT(self.channel, self.chipv)
        self.MACRXRTS_INT_CNT = MACRXRTS_INT_CNT(self.channel, self.chipv)
        self.MACRXCTS_INT_CNT = MACRXCTS_INT_CNT(self.channel, self.chipv)
        self.MACRXRIFS_INT_CNT = MACRXRIFS_INT_CNT(self.channel, self.chipv)
        self.MACRX_DATASUC_CNT = MACRX_DATASUC_CNT(self.channel, self.chipv)
        self.MACRX_END_CNT = MACRX_END_CNT(self.channel, self.chipv)
        self.MACRX_BTBLOCK_ERR_CNT = MACRX_BTBLOCK_ERR_CNT(self.channel, self.chipv)
        self.MACRX_FREQHOP_ERR_CNT = MACRX_FREQHOP_ERR_CNT(self.channel, self.chipv)
        self.MACRX_LASTUNMATCH_ERR_CNT = MACRX_LASTUNMATCH_ERR_CNT(self.channel, self.chipv)
        self.MACRX_BLOCK_ERR_CNT = MACRX_BLOCK_ERR_CNT(self.channel, self.chipv)
        self.MACRXFRAME_LOWTO = MACRXFRAME_LOWTO(self.channel, self.chipv)
        self.MACRX_ERRTO = MACRX_ERRTO(self.channel, self.chipv)
        self.MACRX_AHB = MACRX_AHB(self.channel, self.chipv)
        self.MACDIAG4 = MACDIAG4(self.channel, self.chipv)
        self.MACDIAG5 = MACDIAG5(self.channel, self.chipv)
        self.MACDIAG6 = MACDIAG6(self.channel, self.chipv)
        self.MACDIAG7 = MACDIAG7(self.channel, self.chipv)
        self.MACRXDATE = MACRXDATE(self.channel, self.chipv)
class MACBSSID0LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x0
        self.__reg_macbssid0_lo_lsb = 0
        self.__reg_macbssid0_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macbssid0_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macbssid0_lo_msb, self.__reg_macbssid0_lo_lsb)
    @reg_macbssid0_lo.setter
    def reg_macbssid0_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macbssid0_lo_msb, self.__reg_macbssid0_lo_lsb, value)
class MACBSSID0HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x4
        self.__reg_macbssid0_hi_lsb = 0
        self.__reg_macbssid0_hi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macbssid0_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macbssid0_hi_msb, self.__reg_macbssid0_hi_lsb)
    @reg_macbssid0_hi.setter
    def reg_macbssid0_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macbssid0_hi_msb, self.__reg_macbssid0_hi_lsb, value)
class MACBSSID1LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x8
        self.__reg_macbssid1_lo_lsb = 0
        self.__reg_macbssid1_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macbssid1_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macbssid1_lo_msb, self.__reg_macbssid1_lo_lsb)
    @reg_macbssid1_lo.setter
    def reg_macbssid1_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macbssid1_lo_msb, self.__reg_macbssid1_lo_lsb, value)
class MACBSSID1HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0xc
        self.__reg_macbssid1_hi_lsb = 0
        self.__reg_macbssid1_hi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macbssid1_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macbssid1_hi_msb, self.__reg_macbssid1_hi_lsb)
    @reg_macbssid1_hi.setter
    def reg_macbssid1_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macbssid1_hi_msb, self.__reg_macbssid1_hi_lsb, value)
class MACBSSID2LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x10
        self.__reg_macbssid2_lo_lsb = 0
        self.__reg_macbssid2_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macbssid2_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macbssid2_lo_msb, self.__reg_macbssid2_lo_lsb)
    @reg_macbssid2_lo.setter
    def reg_macbssid2_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macbssid2_lo_msb, self.__reg_macbssid2_lo_lsb, value)
class MACBSSID2HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x14
        self.__reg_macbssid2_hi_lsb = 0
        self.__reg_macbssid2_hi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macbssid2_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macbssid2_hi_msb, self.__reg_macbssid2_hi_lsb)
    @reg_macbssid2_hi.setter
    def reg_macbssid2_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macbssid2_hi_msb, self.__reg_macbssid2_hi_lsb, value)
class MACBSSID3LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x18
        self.__reg_macbssid3_lo_lsb = 0
        self.__reg_macbssid3_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macbssid3_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macbssid3_lo_msb, self.__reg_macbssid3_lo_lsb)
    @reg_macbssid3_lo.setter
    def reg_macbssid3_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macbssid3_lo_msb, self.__reg_macbssid3_lo_lsb, value)
class MACBSSID3HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x1c
        self.__reg_macbssid3_hi_lsb = 0
        self.__reg_macbssid3_hi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macbssid3_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macbssid3_hi_msb, self.__reg_macbssid3_hi_lsb)
    @reg_macbssid3_hi.setter
    def reg_macbssid3_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macbssid3_hi_msb, self.__reg_macbssid3_hi_lsb, value)
class MACBSSID0_MASKLO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x20
        self.__reg_macbssid0_masklo_lsb = 0
        self.__reg_macbssid0_masklo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macbssid0_masklo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macbssid0_masklo_msb, self.__reg_macbssid0_masklo_lsb)
    @reg_macbssid0_masklo.setter
    def reg_macbssid0_masklo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macbssid0_masklo_msb, self.__reg_macbssid0_masklo_lsb, value)
class MACBSSID0_MASKHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x24
        self.__reg_macbssid0_ena_lsb = 16
        self.__reg_macbssid0_ena_msb = 16
        self.__reg_macbssid0_maskhi_lsb = 0
        self.__reg_macbssid0_maskhi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macbssid0_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macbssid0_ena_msb, self.__reg_macbssid0_ena_lsb)
    @reg_macbssid0_ena.setter
    def reg_macbssid0_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macbssid0_ena_msb, self.__reg_macbssid0_ena_lsb, value)

    @property
    def reg_macbssid0_maskhi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macbssid0_maskhi_msb, self.__reg_macbssid0_maskhi_lsb)
    @reg_macbssid0_maskhi.setter
    def reg_macbssid0_maskhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macbssid0_maskhi_msb, self.__reg_macbssid0_maskhi_lsb, value)
class MACBSSID1_MASKLO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x28
        self.__reg_macbssid1_masklo_lsb = 0
        self.__reg_macbssid1_masklo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macbssid1_masklo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macbssid1_masklo_msb, self.__reg_macbssid1_masklo_lsb)
    @reg_macbssid1_masklo.setter
    def reg_macbssid1_masklo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macbssid1_masklo_msb, self.__reg_macbssid1_masklo_lsb, value)
class MACBSSID1_MASKHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x2c
        self.__reg_macbssid1_ena_lsb = 16
        self.__reg_macbssid1_ena_msb = 16
        self.__reg_macbssid1_maskhi_lsb = 0
        self.__reg_macbssid1_maskhi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macbssid1_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macbssid1_ena_msb, self.__reg_macbssid1_ena_lsb)
    @reg_macbssid1_ena.setter
    def reg_macbssid1_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macbssid1_ena_msb, self.__reg_macbssid1_ena_lsb, value)

    @property
    def reg_macbssid1_maskhi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macbssid1_maskhi_msb, self.__reg_macbssid1_maskhi_lsb)
    @reg_macbssid1_maskhi.setter
    def reg_macbssid1_maskhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macbssid1_maskhi_msb, self.__reg_macbssid1_maskhi_lsb, value)
class MACBSSID2_MASKLO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x30
        self.__reg_macbssid2_masklo_lsb = 0
        self.__reg_macbssid2_masklo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macbssid2_masklo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macbssid2_masklo_msb, self.__reg_macbssid2_masklo_lsb)
    @reg_macbssid2_masklo.setter
    def reg_macbssid2_masklo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macbssid2_masklo_msb, self.__reg_macbssid2_masklo_lsb, value)
class MACBSSID2_MASKHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x34
        self.__reg_macbssid2_ena_lsb = 16
        self.__reg_macbssid2_ena_msb = 16
        self.__reg_macbssid2_maskhi_lsb = 0
        self.__reg_macbssid2_maskhi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macbssid2_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macbssid2_ena_msb, self.__reg_macbssid2_ena_lsb)
    @reg_macbssid2_ena.setter
    def reg_macbssid2_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macbssid2_ena_msb, self.__reg_macbssid2_ena_lsb, value)

    @property
    def reg_macbssid2_maskhi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macbssid2_maskhi_msb, self.__reg_macbssid2_maskhi_lsb)
    @reg_macbssid2_maskhi.setter
    def reg_macbssid2_maskhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macbssid2_maskhi_msb, self.__reg_macbssid2_maskhi_lsb, value)
class MACBSSID3_MASKLO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x38
        self.__reg_macbssid3_masklo_lsb = 0
        self.__reg_macbssid3_masklo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macbssid3_masklo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macbssid3_masklo_msb, self.__reg_macbssid3_masklo_lsb)
    @reg_macbssid3_masklo.setter
    def reg_macbssid3_masklo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macbssid3_masklo_msb, self.__reg_macbssid3_masklo_lsb, value)
class MACBSSID3_MASKHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x3c
        self.__reg_macbssid3_ena_lsb = 16
        self.__reg_macbssid3_ena_msb = 16
        self.__reg_macbssid3_maskhi_lsb = 0
        self.__reg_macbssid3_maskhi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macbssid3_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macbssid3_ena_msb, self.__reg_macbssid3_ena_lsb)
    @reg_macbssid3_ena.setter
    def reg_macbssid3_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macbssid3_ena_msb, self.__reg_macbssid3_ena_lsb, value)

    @property
    def reg_macbssid3_maskhi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macbssid3_maskhi_msb, self.__reg_macbssid3_maskhi_lsb)
    @reg_macbssid3_maskhi.setter
    def reg_macbssid3_maskhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macbssid3_maskhi_msb, self.__reg_macbssid3_maskhi_lsb, value)
class MACDA0LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x40
        self.__reg_macda0_lo_lsb = 0
        self.__reg_macda0_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macda0_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macda0_lo_msb, self.__reg_macda0_lo_lsb)
    @reg_macda0_lo.setter
    def reg_macda0_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macda0_lo_msb, self.__reg_macda0_lo_lsb, value)
class MACDA0HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x44
        self.__reg_macda0_hi_lsb = 0
        self.__reg_macda0_hi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macda0_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macda0_hi_msb, self.__reg_macda0_hi_lsb)
    @reg_macda0_hi.setter
    def reg_macda0_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macda0_hi_msb, self.__reg_macda0_hi_lsb, value)
class MACDA1LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x48
        self.__reg_macda1_lo_lsb = 0
        self.__reg_macda1_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macda1_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macda1_lo_msb, self.__reg_macda1_lo_lsb)
    @reg_macda1_lo.setter
    def reg_macda1_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macda1_lo_msb, self.__reg_macda1_lo_lsb, value)
class MACDA1HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x4c
        self.__reg_macda1_hi_lsb = 0
        self.__reg_macda1_hi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macda1_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macda1_hi_msb, self.__reg_macda1_hi_lsb)
    @reg_macda1_hi.setter
    def reg_macda1_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macda1_hi_msb, self.__reg_macda1_hi_lsb, value)
class MACDA2LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x50
        self.__reg_macda2_lo_lsb = 0
        self.__reg_macda2_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macda2_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macda2_lo_msb, self.__reg_macda2_lo_lsb)
    @reg_macda2_lo.setter
    def reg_macda2_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macda2_lo_msb, self.__reg_macda2_lo_lsb, value)
class MACDA2HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x54
        self.__reg_macda2_hi_lsb = 0
        self.__reg_macda2_hi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macda2_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macda2_hi_msb, self.__reg_macda2_hi_lsb)
    @reg_macda2_hi.setter
    def reg_macda2_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macda2_hi_msb, self.__reg_macda2_hi_lsb, value)
class MACDA3LO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x58
        self.__reg_macda3_lo_lsb = 0
        self.__reg_macda3_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macda3_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macda3_lo_msb, self.__reg_macda3_lo_lsb)
    @reg_macda3_lo.setter
    def reg_macda3_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macda3_lo_msb, self.__reg_macda3_lo_lsb, value)
class MACDA3HI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x5c
        self.__reg_macda3_hi_lsb = 0
        self.__reg_macda3_hi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macda3_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macda3_hi_msb, self.__reg_macda3_hi_lsb)
    @reg_macda3_hi.setter
    def reg_macda3_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macda3_hi_msb, self.__reg_macda3_hi_lsb, value)
class MACDA0_MASKLO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x60
        self.__reg_macda0_masklo_lsb = 0
        self.__reg_macda0_masklo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macda0_masklo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macda0_masklo_msb, self.__reg_macda0_masklo_lsb)
    @reg_macda0_masklo.setter
    def reg_macda0_masklo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macda0_masklo_msb, self.__reg_macda0_masklo_lsb, value)
class MACDA0_MASKHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x64
        self.__reg_macda0_ena_lsb = 16
        self.__reg_macda0_ena_msb = 16
        self.__reg_macda0_maskhi_lsb = 0
        self.__reg_macda0_maskhi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macda0_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macda0_ena_msb, self.__reg_macda0_ena_lsb)
    @reg_macda0_ena.setter
    def reg_macda0_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macda0_ena_msb, self.__reg_macda0_ena_lsb, value)

    @property
    def reg_macda0_maskhi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macda0_maskhi_msb, self.__reg_macda0_maskhi_lsb)
    @reg_macda0_maskhi.setter
    def reg_macda0_maskhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macda0_maskhi_msb, self.__reg_macda0_maskhi_lsb, value)
class MACDA1_MASKLO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x68
        self.__reg_macda1_masklo_lsb = 0
        self.__reg_macda1_masklo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macda1_masklo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macda1_masklo_msb, self.__reg_macda1_masklo_lsb)
    @reg_macda1_masklo.setter
    def reg_macda1_masklo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macda1_masklo_msb, self.__reg_macda1_masklo_lsb, value)
class MACDA1_MASKHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x6c
        self.__reg_macda1_ena_lsb = 16
        self.__reg_macda1_ena_msb = 16
        self.__reg_macda1_maskhi_lsb = 0
        self.__reg_macda1_maskhi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macda1_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macda1_ena_msb, self.__reg_macda1_ena_lsb)
    @reg_macda1_ena.setter
    def reg_macda1_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macda1_ena_msb, self.__reg_macda1_ena_lsb, value)

    @property
    def reg_macda1_maskhi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macda1_maskhi_msb, self.__reg_macda1_maskhi_lsb)
    @reg_macda1_maskhi.setter
    def reg_macda1_maskhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macda1_maskhi_msb, self.__reg_macda1_maskhi_lsb, value)
class MACDA2_MASKLO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x70
        self.__reg_macda2_masklo_lsb = 0
        self.__reg_macda2_masklo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macda2_masklo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macda2_masklo_msb, self.__reg_macda2_masklo_lsb)
    @reg_macda2_masklo.setter
    def reg_macda2_masklo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macda2_masklo_msb, self.__reg_macda2_masklo_lsb, value)
class MACDA2_MASKHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x74
        self.__reg_macda2_ena_lsb = 16
        self.__reg_macda2_ena_msb = 16
        self.__reg_macda2_maskhi_lsb = 0
        self.__reg_macda2_maskhi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macda2_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macda2_ena_msb, self.__reg_macda2_ena_lsb)
    @reg_macda2_ena.setter
    def reg_macda2_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macda2_ena_msb, self.__reg_macda2_ena_lsb, value)

    @property
    def reg_macda2_maskhi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macda2_maskhi_msb, self.__reg_macda2_maskhi_lsb)
    @reg_macda2_maskhi.setter
    def reg_macda2_maskhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macda2_maskhi_msb, self.__reg_macda2_maskhi_lsb, value)
class MACDA3_MASKLO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x78
        self.__reg_macda3_masklo_lsb = 0
        self.__reg_macda3_masklo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macda3_masklo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macda3_masklo_msb, self.__reg_macda3_masklo_lsb)
    @reg_macda3_masklo.setter
    def reg_macda3_masklo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macda3_masklo_msb, self.__reg_macda3_masklo_lsb, value)
class MACDA3_MASKHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x7c
        self.__reg_macda3_ena_lsb = 16
        self.__reg_macda3_ena_msb = 16
        self.__reg_macda3_maskhi_lsb = 0
        self.__reg_macda3_maskhi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macda3_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macda3_ena_msb, self.__reg_macda3_ena_lsb)
    @reg_macda3_ena.setter
    def reg_macda3_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macda3_ena_msb, self.__reg_macda3_ena_lsb, value)

    @property
    def reg_macda3_maskhi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macda3_maskhi_msb, self.__reg_macda3_maskhi_lsb)
    @reg_macda3_maskhi.setter
    def reg_macda3_maskhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macda3_maskhi_msb, self.__reg_macda3_maskhi_lsb, value)
class MACRXBUF_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x80
        self.__reg_rxaplk_ena_lsb = 29
        self.__reg_rxaplk_ena_msb = 29
        self.__reg_rxdumpcon_ena_lsb = 28
        self.__reg_rxdumpcon_ena_msb = 28
        self.__reg_rxresbuf_size_lsb = 0
        self.__reg_rxresbuf_size_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxaplk_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxaplk_ena_msb, self.__reg_rxaplk_ena_lsb)
    @reg_rxaplk_ena.setter
    def reg_rxaplk_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxaplk_ena_msb, self.__reg_rxaplk_ena_lsb, value)

    @property
    def reg_rxdumpcon_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdumpcon_ena_msb, self.__reg_rxdumpcon_ena_lsb)
    @reg_rxdumpcon_ena.setter
    def reg_rxdumpcon_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdumpcon_ena_msb, self.__reg_rxdumpcon_ena_lsb, value)

    @property
    def reg_rxresbuf_size(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxresbuf_size_msb, self.__reg_rxresbuf_size_lsb)
    @reg_rxresbuf_size.setter
    def reg_rxresbuf_size(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxresbuf_size_msb, self.__reg_rxresbuf_size_lsb, value)
class MACRXESTMODE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x84
        self.__reg_rxest_ena_frc_lsb = 31
        self.__reg_rxest_ena_frc_msb = 31
        self.__reg_rxest_ena_suc_lsb = 30
        self.__reg_rxest_ena_suc_msb = 30
        self.__reg_rxest_ena_any_lsb = 29
        self.__reg_rxest_ena_any_msb = 29
        self.__reg_rxest_size_lsb = 0
        self.__reg_rxest_size_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxest_ena_frc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxest_ena_frc_msb, self.__reg_rxest_ena_frc_lsb)
    @reg_rxest_ena_frc.setter
    def reg_rxest_ena_frc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxest_ena_frc_msb, self.__reg_rxest_ena_frc_lsb, value)

    @property
    def reg_rxest_ena_suc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxest_ena_suc_msb, self.__reg_rxest_ena_suc_lsb)
    @reg_rxest_ena_suc.setter
    def reg_rxest_ena_suc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxest_ena_suc_msb, self.__reg_rxest_ena_suc_lsb, value)

    @property
    def reg_rxest_ena_any(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxest_ena_any_msb, self.__reg_rxest_ena_any_lsb)
    @reg_rxest_ena_any.setter
    def reg_rxest_ena_any(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxest_ena_any_msb, self.__reg_rxest_ena_any_lsb, value)

    @property
    def reg_rxest_size(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxest_size_msb, self.__reg_rxest_size_lsb)
    @reg_rxest_size.setter
    def reg_rxest_size(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxest_size_msb, self.__reg_rxest_size_lsb, value)
class MACRXMODE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x88
        self.__reg_rxbuflk_ena_frc_lsb = 31
        self.__reg_rxbuflk_ena_frc_msb = 31
        self.__reg_rxbuflk_ena_suc_lsb = 30
        self.__reg_rxbuflk_ena_suc_msb = 30
        self.__reg_rxbuflk_ena_any_lsb = 29
        self.__reg_rxbuflk_ena_any_msb = 29
        self.__reg_rxbufdscr_reload_lsb = 0
        self.__reg_rxbufdscr_reload_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxbuflk_ena_frc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxbuflk_ena_frc_msb, self.__reg_rxbuflk_ena_frc_lsb)
    @reg_rxbuflk_ena_frc.setter
    def reg_rxbuflk_ena_frc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxbuflk_ena_frc_msb, self.__reg_rxbuflk_ena_frc_lsb, value)

    @property
    def reg_rxbuflk_ena_suc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxbuflk_ena_suc_msb, self.__reg_rxbuflk_ena_suc_lsb)
    @reg_rxbuflk_ena_suc.setter
    def reg_rxbuflk_ena_suc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxbuflk_ena_suc_msb, self.__reg_rxbuflk_ena_suc_lsb, value)

    @property
    def reg_rxbuflk_ena_any(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxbuflk_ena_any_msb, self.__reg_rxbuflk_ena_any_lsb)
    @reg_rxbuflk_ena_any.setter
    def reg_rxbuflk_ena_any(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxbuflk_ena_any_msb, self.__reg_rxbuflk_ena_any_lsb, value)

    @property
    def reg_rxbufdscr_reload(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxbufdscr_reload_msb, self.__reg_rxbufdscr_reload_lsb)
    @reg_rxbufdscr_reload.setter
    def reg_rxbufdscr_reload(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxbufdscr_reload_msb, self.__reg_rxbufdscr_reload_lsb, value)
class MACRXESTBASE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x8c
        self.__reg_rxest_base_lsb = 0
        self.__reg_rxest_base_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxest_base(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxest_base_msb, self.__reg_rxest_base_lsb)
    @reg_rxest_base.setter
    def reg_rxest_base(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxest_base_msb, self.__reg_rxest_base_lsb, value)
class MACRXBASE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x90
        self.__reg_rxbuflk_base_lsb = 0
        self.__reg_rxbuflk_base_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxbuflk_base(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxbuflk_base_msb, self.__reg_rxbuflk_base_lsb)
    @reg_rxbuflk_base.setter
    def reg_rxbuflk_base(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxbuflk_base_msb, self.__reg_rxbuflk_base_lsb, value)
class MACRXBUFDSCR_NEXT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x94
        self.__next_rxbufdscr_lsb = 0
        self.__next_rxbufdscr_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def next_rxbufdscr(self):
        return self.__MEM.rdm(self.__addr, self.__next_rxbufdscr_msb, self.__next_rxbufdscr_lsb)
    @next_rxbufdscr.setter
    def next_rxbufdscr(self, value):
        return self.__MEM.wrm(self.__addr, self.__next_rxbufdscr_msb, self.__next_rxbufdscr_lsb, value)
class MACRXBUFDSCR_LAST(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x98
        self.__last_rxbufdscr_lsb = 0
        self.__last_rxbufdscr_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def last_rxbufdscr(self):
        return self.__MEM.rdm(self.__addr, self.__last_rxbufdscr_msb, self.__last_rxbufdscr_lsb)
    @last_rxbufdscr.setter
    def last_rxbufdscr(self, value):
        return self.__MEM.wrm(self.__addr, self.__last_rxbufdscr_msb, self.__last_rxbufdscr_lsb, value)
class MACRXBUFBK_CNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x9c
        self.__last_rxbufbk_cnt_lsb = 0
        self.__last_rxbufbk_cnt_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def last_rxbufbk_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__last_rxbufbk_cnt_msb, self.__last_rxbufbk_cnt_lsb)
    @last_rxbufbk_cnt.setter
    def last_rxbufbk_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__last_rxbufbk_cnt_msb, self.__last_rxbufbk_cnt_lsb, value)
class MACRXBUFDSCR_START(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0xa0
        self.__start_rxbufdscr_lsb = 0
        self.__start_rxbufdscr_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def start_rxbufdscr(self):
        return self.__MEM.rdm(self.__addr, self.__start_rxbufdscr_msb, self.__start_rxbufdscr_lsb)
    @start_rxbufdscr.setter
    def start_rxbufdscr(self, value):
        return self.__MEM.wrm(self.__addr, self.__start_rxbufdscr_msb, self.__start_rxbufdscr_lsb, value)
class MACRXOPTION(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0xa4
        self.__reg_rxclk_en_lsb = 30
        self.__reg_rxclk_en_msb = 30
        self.__reg_rx_bbfifo_clka_en_lsb = 29
        self.__reg_rx_bbfifo_clka_en_msb = 29
        self.__reg_rx_bbfifo_clkb_en_lsb = 28
        self.__reg_rx_bbfifo_clkb_en_msb = 28
        self.__reg_rxlastblock_buf_ena_lsb = 27
        self.__reg_rxlastblock_buf_ena_msb = 27
        self.__reg_btrxabort_ena_lsb = 26
        self.__reg_btrxabort_ena_msb = 26
        self.__reg_rxchaest_dump_ena_lsb = 23
        self.__reg_rxchaest_dump_ena_msb = 23
        self.__reg_rxbuf_dump_est_ena_lsb = 22
        self.__reg_rxbuf_dump_est_ena_msb = 22
        self.__reg_rxbuf_est_close_lsb = 21
        self.__reg_rxbuf_est_close_msb = 21
        self.__reg_rxabortfrself_ena_lsb = 20
        self.__reg_rxabortfrself_ena_msb = 20
        self.__reg_rxblock_int_size_lsb = 8
        self.__reg_rxblock_int_size_msb = 15
        self.__reg_rxsampdu_int_size_lsb = 0
        self.__reg_rxsampdu_int_size_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxclk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxclk_en_msb, self.__reg_rxclk_en_lsb)
    @reg_rxclk_en.setter
    def reg_rxclk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxclk_en_msb, self.__reg_rxclk_en_lsb, value)

    @property
    def reg_rx_bbfifo_clka_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_bbfifo_clka_en_msb, self.__reg_rx_bbfifo_clka_en_lsb)
    @reg_rx_bbfifo_clka_en.setter
    def reg_rx_bbfifo_clka_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_bbfifo_clka_en_msb, self.__reg_rx_bbfifo_clka_en_lsb, value)

    @property
    def reg_rx_bbfifo_clkb_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_bbfifo_clkb_en_msb, self.__reg_rx_bbfifo_clkb_en_lsb)
    @reg_rx_bbfifo_clkb_en.setter
    def reg_rx_bbfifo_clkb_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_bbfifo_clkb_en_msb, self.__reg_rx_bbfifo_clkb_en_lsb, value)

    @property
    def reg_rxlastblock_buf_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxlastblock_buf_ena_msb, self.__reg_rxlastblock_buf_ena_lsb)
    @reg_rxlastblock_buf_ena.setter
    def reg_rxlastblock_buf_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxlastblock_buf_ena_msb, self.__reg_rxlastblock_buf_ena_lsb, value)

    @property
    def reg_btrxabort_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_btrxabort_ena_msb, self.__reg_btrxabort_ena_lsb)
    @reg_btrxabort_ena.setter
    def reg_btrxabort_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_btrxabort_ena_msb, self.__reg_btrxabort_ena_lsb, value)

    @property
    def reg_rxchaest_dump_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxchaest_dump_ena_msb, self.__reg_rxchaest_dump_ena_lsb)
    @reg_rxchaest_dump_ena.setter
    def reg_rxchaest_dump_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxchaest_dump_ena_msb, self.__reg_rxchaest_dump_ena_lsb, value)

    @property
    def reg_rxbuf_dump_est_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxbuf_dump_est_ena_msb, self.__reg_rxbuf_dump_est_ena_lsb)
    @reg_rxbuf_dump_est_ena.setter
    def reg_rxbuf_dump_est_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxbuf_dump_est_ena_msb, self.__reg_rxbuf_dump_est_ena_lsb, value)

    @property
    def reg_rxbuf_est_close(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxbuf_est_close_msb, self.__reg_rxbuf_est_close_lsb)
    @reg_rxbuf_est_close.setter
    def reg_rxbuf_est_close(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxbuf_est_close_msb, self.__reg_rxbuf_est_close_lsb, value)

    @property
    def reg_rxabortfrself_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxabortfrself_ena_msb, self.__reg_rxabortfrself_ena_lsb)
    @reg_rxabortfrself_ena.setter
    def reg_rxabortfrself_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxabortfrself_ena_msb, self.__reg_rxabortfrself_ena_lsb, value)

    @property
    def reg_rxblock_int_size(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxblock_int_size_msb, self.__reg_rxblock_int_size_lsb)
    @reg_rxblock_int_size.setter
    def reg_rxblock_int_size(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxblock_int_size_msb, self.__reg_rxblock_int_size_lsb, value)

    @property
    def reg_rxsampdu_int_size(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxsampdu_int_size_msb, self.__reg_rxsampdu_int_size_lsb)
    @reg_rxsampdu_int_size.setter
    def reg_rxsampdu_int_size(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxsampdu_int_size_msb, self.__reg_rxsampdu_int_size_lsb, value)
class MACRX_ABORT_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0xa8
        self.__reg_rxabort_bytenum_lsb = 24
        self.__reg_rxabort_bytenum_msb = 31
        self.__reg_bssidwds0_ena_lsb = 23
        self.__reg_bssidwds0_ena_msb = 23
        self.__reg_bssidwds1_ena_lsb = 22
        self.__reg_bssidwds1_ena_msb = 22
        self.__reg_bssidwds2_ena_lsb = 21
        self.__reg_bssidwds2_ena_msb = 21
        self.__reg_bssidwds3_ena_lsb = 20
        self.__reg_bssidwds3_ena_msb = 20
        self.__reg_bssidwds_sel_lsb = 18
        self.__reg_bssidwds_sel_msb = 19
        self.__reg_bssidsec_sel_lsb = 16
        self.__reg_bssidsec_sel_msb = 17
        self.__reg_bssid_default_sel_lsb = 12
        self.__reg_bssid_default_sel_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxabort_bytenum(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxabort_bytenum_msb, self.__reg_rxabort_bytenum_lsb)
    @reg_rxabort_bytenum.setter
    def reg_rxabort_bytenum(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxabort_bytenum_msb, self.__reg_rxabort_bytenum_lsb, value)

    @property
    def reg_bssidwds0_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bssidwds0_ena_msb, self.__reg_bssidwds0_ena_lsb)
    @reg_bssidwds0_ena.setter
    def reg_bssidwds0_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bssidwds0_ena_msb, self.__reg_bssidwds0_ena_lsb, value)

    @property
    def reg_bssidwds1_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bssidwds1_ena_msb, self.__reg_bssidwds1_ena_lsb)
    @reg_bssidwds1_ena.setter
    def reg_bssidwds1_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bssidwds1_ena_msb, self.__reg_bssidwds1_ena_lsb, value)

    @property
    def reg_bssidwds2_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bssidwds2_ena_msb, self.__reg_bssidwds2_ena_lsb)
    @reg_bssidwds2_ena.setter
    def reg_bssidwds2_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bssidwds2_ena_msb, self.__reg_bssidwds2_ena_lsb, value)

    @property
    def reg_bssidwds3_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bssidwds3_ena_msb, self.__reg_bssidwds3_ena_lsb)
    @reg_bssidwds3_ena.setter
    def reg_bssidwds3_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bssidwds3_ena_msb, self.__reg_bssidwds3_ena_lsb, value)

    @property
    def reg_bssidwds_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bssidwds_sel_msb, self.__reg_bssidwds_sel_lsb)
    @reg_bssidwds_sel.setter
    def reg_bssidwds_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bssidwds_sel_msb, self.__reg_bssidwds_sel_lsb, value)

    @property
    def reg_bssidsec_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bssidsec_sel_msb, self.__reg_bssidsec_sel_lsb)
    @reg_bssidsec_sel.setter
    def reg_bssidsec_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bssidsec_sel_msb, self.__reg_bssidsec_sel_lsb, value)

    @property
    def reg_bssid_default_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bssid_default_sel_msb, self.__reg_bssid_default_sel_lsb)
    @reg_bssid_default_sel.setter
    def reg_bssid_default_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bssid_default_sel_msb, self.__reg_bssid_default_sel_lsb, value)
class MACRXPMD(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0xac
        self.__rx_is_ack_lsb = 26
        self.__rx_is_ack_msb = 26
        self.__rx_is_cts_lsb = 25
        self.__rx_is_cts_msb = 25
        self.__rx_is_rts_lsb = 24
        self.__rx_is_rts_msb = 24
        self.__rxda_ampdu_lsb = 21
        self.__rxda_ampdu_msb = 21
        self.__rxda_group_lsb = 20
        self.__rxda_group_msb = 20
        self.__rxbssid_match1_lsb = 19
        self.__rxbssid_match1_msb = 19
        self.__rxbssid_match0_lsb = 18
        self.__rxbssid_match0_msb = 18
        self.__rxda_match1_lsb = 17
        self.__rxda_match1_msb = 17
        self.__rxda_match0_lsb = 16
        self.__rxda_match0_msb = 16
        self.__rxend_state_lsb = 0
        self.__rxend_state_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rx_is_ack(self):
        return self.__MEM.rdm(self.__addr, self.__rx_is_ack_msb, self.__rx_is_ack_lsb)
    @rx_is_ack.setter
    def rx_is_ack(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_is_ack_msb, self.__rx_is_ack_lsb, value)

    @property
    def rx_is_cts(self):
        return self.__MEM.rdm(self.__addr, self.__rx_is_cts_msb, self.__rx_is_cts_lsb)
    @rx_is_cts.setter
    def rx_is_cts(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_is_cts_msb, self.__rx_is_cts_lsb, value)

    @property
    def rx_is_rts(self):
        return self.__MEM.rdm(self.__addr, self.__rx_is_rts_msb, self.__rx_is_rts_lsb)
    @rx_is_rts.setter
    def rx_is_rts(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_is_rts_msb, self.__rx_is_rts_lsb, value)

    @property
    def rxda_ampdu(self):
        return self.__MEM.rdm(self.__addr, self.__rxda_ampdu_msb, self.__rxda_ampdu_lsb)
    @rxda_ampdu.setter
    def rxda_ampdu(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxda_ampdu_msb, self.__rxda_ampdu_lsb, value)

    @property
    def rxda_group(self):
        return self.__MEM.rdm(self.__addr, self.__rxda_group_msb, self.__rxda_group_lsb)
    @rxda_group.setter
    def rxda_group(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxda_group_msb, self.__rxda_group_lsb, value)

    @property
    def rxbssid_match1(self):
        return self.__MEM.rdm(self.__addr, self.__rxbssid_match1_msb, self.__rxbssid_match1_lsb)
    @rxbssid_match1.setter
    def rxbssid_match1(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxbssid_match1_msb, self.__rxbssid_match1_lsb, value)

    @property
    def rxbssid_match0(self):
        return self.__MEM.rdm(self.__addr, self.__rxbssid_match0_msb, self.__rxbssid_match0_lsb)
    @rxbssid_match0.setter
    def rxbssid_match0(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxbssid_match0_msb, self.__rxbssid_match0_lsb, value)

    @property
    def rxda_match1(self):
        return self.__MEM.rdm(self.__addr, self.__rxda_match1_msb, self.__rxda_match1_lsb)
    @rxda_match1.setter
    def rxda_match1(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxda_match1_msb, self.__rxda_match1_lsb, value)

    @property
    def rxda_match0(self):
        return self.__MEM.rdm(self.__addr, self.__rxda_match0_msb, self.__rxda_match0_lsb)
    @rxda_match0.setter
    def rxda_match0(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxda_match0_msb, self.__rxda_match0_lsb, value)

    @property
    def rxend_state(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_state_msb, self.__rxend_state_lsb)
    @rxend_state.setter
    def rxend_state(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_state_msb, self.__rxend_state_lsb, value)
class MACRXPLCP(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0xb0
        self.__rx_rssi_lsb = 24
        self.__rx_rssi_msb = 31
        self.__rx_sig_mode_lsb = 22
        self.__rx_sig_mode_msb = 23
        self.__rx_rate_lsb = 16
        self.__rx_rate_msb = 20
        self.__rx_is_40m_lsb = 14
        self.__rx_is_40m_msb = 15
        self.__rx_is_20m_lsb = 12
        self.__rx_is_20m_msb = 13
        self.__rx_legacy_length_lsb = 0
        self.__rx_legacy_length_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rx_rssi(self):
        return self.__MEM.rdm(self.__addr, self.__rx_rssi_msb, self.__rx_rssi_lsb)
    @rx_rssi.setter
    def rx_rssi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_rssi_msb, self.__rx_rssi_lsb, value)

    @property
    def rx_sig_mode(self):
        return self.__MEM.rdm(self.__addr, self.__rx_sig_mode_msb, self.__rx_sig_mode_lsb)
    @rx_sig_mode.setter
    def rx_sig_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_sig_mode_msb, self.__rx_sig_mode_lsb, value)

    @property
    def rx_rate(self):
        return self.__MEM.rdm(self.__addr, self.__rx_rate_msb, self.__rx_rate_lsb)
    @rx_rate.setter
    def rx_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_rate_msb, self.__rx_rate_lsb, value)

    @property
    def rx_is_40m(self):
        return self.__MEM.rdm(self.__addr, self.__rx_is_40m_msb, self.__rx_is_40m_lsb)
    @rx_is_40m.setter
    def rx_is_40m(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_is_40m_msb, self.__rx_is_40m_lsb, value)

    @property
    def rx_is_20m(self):
        return self.__MEM.rdm(self.__addr, self.__rx_is_20m_msb, self.__rx_is_20m_lsb)
    @rx_is_20m.setter
    def rx_is_20m(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_is_20m_msb, self.__rx_is_20m_lsb, value)

    @property
    def rx_legacy_length(self):
        return self.__MEM.rdm(self.__addr, self.__rx_legacy_length_msb, self.__rx_legacy_length_lsb)
    @rx_legacy_length.setter
    def rx_legacy_length(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_legacy_length_msb, self.__rx_legacy_length_lsb, value)
class MACRXHTSIG1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0xb4
        self.__rx_htsig_lo_lsb = 0
        self.__rx_htsig_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rx_htsig_lo(self):
        return self.__MEM.rdm(self.__addr, self.__rx_htsig_lo_msb, self.__rx_htsig_lo_lsb)
    @rx_htsig_lo.setter
    def rx_htsig_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_htsig_lo_msb, self.__rx_htsig_lo_lsb, value)
class MACRXHTSIG2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0xb8
        self.__rx_htsig_hi_lsb = 0
        self.__rx_htsig_hi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rx_htsig_hi(self):
        return self.__MEM.rdm(self.__addr, self.__rx_htsig_hi_msb, self.__rx_htsig_hi_lsb)
    @rx_htsig_hi.setter
    def rx_htsig_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_htsig_hi_msb, self.__rx_htsig_hi_lsb, value)
class MACRXMPDU0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0xbc
        self.__rx_mpdu0_lsb = 0
        self.__rx_mpdu0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rx_mpdu0(self):
        return self.__MEM.rdm(self.__addr, self.__rx_mpdu0_msb, self.__rx_mpdu0_lsb)
    @rx_mpdu0.setter
    def rx_mpdu0(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_mpdu0_msb, self.__rx_mpdu0_lsb, value)
class MACRXMPDU1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0xc0
        self.__rx_mpdu1_lsb = 0
        self.__rx_mpdu1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rx_mpdu1(self):
        return self.__MEM.rdm(self.__addr, self.__rx_mpdu1_msb, self.__rx_mpdu1_lsb)
    @rx_mpdu1.setter
    def rx_mpdu1(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_mpdu1_msb, self.__rx_mpdu1_lsb, value)
class MACRXMPDU2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0xc4
        self.__rx_mpdu2_lsb = 0
        self.__rx_mpdu2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rx_mpdu2(self):
        return self.__MEM.rdm(self.__addr, self.__rx_mpdu2_msb, self.__rx_mpdu2_lsb)
    @rx_mpdu2.setter
    def rx_mpdu2(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_mpdu2_msb, self.__rx_mpdu2_lsb, value)
class MACRXMPDU3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0xc8
        self.__rx_mpdu3_lsb = 0
        self.__rx_mpdu3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rx_mpdu3(self):
        return self.__MEM.rdm(self.__addr, self.__rx_mpdu3_msb, self.__rx_mpdu3_lsb)
    @rx_mpdu3.setter
    def rx_mpdu3(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_mpdu3_msb, self.__rx_mpdu3_lsb, value)
class MACRXMPDU4(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0xcc
        self.__rx_mpdu4_lsb = 0
        self.__rx_mpdu4_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rx_mpdu4(self):
        return self.__MEM.rdm(self.__addr, self.__rx_mpdu4_msb, self.__rx_mpdu4_lsb)
    @rx_mpdu4.setter
    def rx_mpdu4(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_mpdu4_msb, self.__rx_mpdu4_lsb, value)
class MACRXMPDU5(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0xd0
        self.__rx_mpdu5_lsb = 0
        self.__rx_mpdu5_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rx_mpdu5(self):
        return self.__MEM.rdm(self.__addr, self.__rx_mpdu5_msb, self.__rx_mpdu5_lsb)
    @rx_mpdu5.setter
    def rx_mpdu5(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_mpdu5_msb, self.__rx_mpdu5_lsb, value)
class MACRXMPDU6(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0xd4
        self.__rx_mpdu6_lsb = 0
        self.__rx_mpdu6_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rx_mpdu6(self):
        return self.__MEM.rdm(self.__addr, self.__rx_mpdu6_msb, self.__rx_mpdu6_lsb)
    @rx_mpdu6.setter
    def rx_mpdu6(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_mpdu6_msb, self.__rx_mpdu6_lsb, value)
class MACRXMPDU7(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0xd8
        self.__rx_mpdu7_lsb = 0
        self.__rx_mpdu7_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rx_mpdu7(self):
        return self.__MEM.rdm(self.__addr, self.__rx_mpdu7_msb, self.__rx_mpdu7_lsb)
    @rx_mpdu7.setter
    def rx_mpdu7(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_mpdu7_msb, self.__rx_mpdu7_lsb, value)
class MACRX_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0xdc
        self.__reg_frmhdr_align_lsb = 0
        self.__reg_frmhdr_align_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_frmhdr_align(self):
        return self.__MEM.rdm(self.__addr, self.__reg_frmhdr_align_msb, self.__reg_frmhdr_align_lsb)
    @reg_frmhdr_align.setter
    def reg_frmhdr_align(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_frmhdr_align_msb, self.__reg_frmhdr_align_lsb, value)
class MACRX_ABORT0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0xe0
        self.__reg_autoack_secerr0_dis_lsb = 16
        self.__reg_autoack_secerr0_dis_msb = 16
        self.__reg_autoack_disable0_lsb = 15
        self.__reg_autoack_disable0_msb = 15
        self.__reg_autoack_notgroup0_lsb = 14
        self.__reg_autoack_notgroup0_msb = 14
        self.__reg_autoack_bbssid0chk_lsb = 13
        self.__reg_autoack_bbssid0chk_msb = 13
        self.__reg_autoack_da0chk_lsb = 12
        self.__reg_autoack_da0chk_msb = 12
        self.__reg_autoack_bssid0chk_lsb = 11
        self.__reg_autoack_bssid0chk_msb = 11
        self.__reg_autoack_frds0chk_lsb = 10
        self.__reg_autoack_frds0chk_msb = 10
        self.__reg_autoack_tods0chk_lsb = 9
        self.__reg_autoack_tods0chk_msb = 9
        self.__reg_rxmanager_notck0_bssid_lsb = 8
        self.__reg_rxmanager_notck0_bssid_msb = 8
        self.__reg_rxsecerr_dump0_ena_lsb = 7
        self.__reg_rxsecerr_dump0_ena_msb = 7
        self.__reg_rxsectkiperr_dump0_ena_lsb = 6
        self.__reg_rxsectkiperr_dump0_ena_msb = 6
        self.__reg_rxsamebm_dump0_ena_lsb = 5
        self.__reg_rxsamebm_dump0_ena_msb = 5
        self.__reg_rxpassbeacon0_ena_lsb = 4
        self.__reg_rxpassbeacon0_ena_msb = 4
        self.__reg_rxabortgroup0_ena_lsb = 3
        self.__reg_rxabortgroup0_ena_msb = 3
        self.__reg_rxabortbbsc0_ena_lsb = 2
        self.__reg_rxabortbbsc0_ena_msb = 2
        self.__reg_rxabortubsc0_ena_lsb = 1
        self.__reg_rxabortubsc0_ena_msb = 1
        self.__reg_rxabortudac0_ena_lsb = 0
        self.__reg_rxabortudac0_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_autoack_secerr0_dis(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_secerr0_dis_msb, self.__reg_autoack_secerr0_dis_lsb)
    @reg_autoack_secerr0_dis.setter
    def reg_autoack_secerr0_dis(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_secerr0_dis_msb, self.__reg_autoack_secerr0_dis_lsb, value)

    @property
    def reg_autoack_disable0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_disable0_msb, self.__reg_autoack_disable0_lsb)
    @reg_autoack_disable0.setter
    def reg_autoack_disable0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_disable0_msb, self.__reg_autoack_disable0_lsb, value)

    @property
    def reg_autoack_notgroup0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_notgroup0_msb, self.__reg_autoack_notgroup0_lsb)
    @reg_autoack_notgroup0.setter
    def reg_autoack_notgroup0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_notgroup0_msb, self.__reg_autoack_notgroup0_lsb, value)

    @property
    def reg_autoack_bbssid0chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_bbssid0chk_msb, self.__reg_autoack_bbssid0chk_lsb)
    @reg_autoack_bbssid0chk.setter
    def reg_autoack_bbssid0chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_bbssid0chk_msb, self.__reg_autoack_bbssid0chk_lsb, value)

    @property
    def reg_autoack_da0chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_da0chk_msb, self.__reg_autoack_da0chk_lsb)
    @reg_autoack_da0chk.setter
    def reg_autoack_da0chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_da0chk_msb, self.__reg_autoack_da0chk_lsb, value)

    @property
    def reg_autoack_bssid0chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_bssid0chk_msb, self.__reg_autoack_bssid0chk_lsb)
    @reg_autoack_bssid0chk.setter
    def reg_autoack_bssid0chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_bssid0chk_msb, self.__reg_autoack_bssid0chk_lsb, value)

    @property
    def reg_autoack_frds0chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_frds0chk_msb, self.__reg_autoack_frds0chk_lsb)
    @reg_autoack_frds0chk.setter
    def reg_autoack_frds0chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_frds0chk_msb, self.__reg_autoack_frds0chk_lsb, value)

    @property
    def reg_autoack_tods0chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_tods0chk_msb, self.__reg_autoack_tods0chk_lsb)
    @reg_autoack_tods0chk.setter
    def reg_autoack_tods0chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_tods0chk_msb, self.__reg_autoack_tods0chk_lsb, value)

    @property
    def reg_rxmanager_notck0_bssid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxmanager_notck0_bssid_msb, self.__reg_rxmanager_notck0_bssid_lsb)
    @reg_rxmanager_notck0_bssid.setter
    def reg_rxmanager_notck0_bssid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxmanager_notck0_bssid_msb, self.__reg_rxmanager_notck0_bssid_lsb, value)

    @property
    def reg_rxsecerr_dump0_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxsecerr_dump0_ena_msb, self.__reg_rxsecerr_dump0_ena_lsb)
    @reg_rxsecerr_dump0_ena.setter
    def reg_rxsecerr_dump0_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxsecerr_dump0_ena_msb, self.__reg_rxsecerr_dump0_ena_lsb, value)

    @property
    def reg_rxsectkiperr_dump0_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxsectkiperr_dump0_ena_msb, self.__reg_rxsectkiperr_dump0_ena_lsb)
    @reg_rxsectkiperr_dump0_ena.setter
    def reg_rxsectkiperr_dump0_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxsectkiperr_dump0_ena_msb, self.__reg_rxsectkiperr_dump0_ena_lsb, value)

    @property
    def reg_rxsamebm_dump0_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxsamebm_dump0_ena_msb, self.__reg_rxsamebm_dump0_ena_lsb)
    @reg_rxsamebm_dump0_ena.setter
    def reg_rxsamebm_dump0_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxsamebm_dump0_ena_msb, self.__reg_rxsamebm_dump0_ena_lsb, value)

    @property
    def reg_rxpassbeacon0_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxpassbeacon0_ena_msb, self.__reg_rxpassbeacon0_ena_lsb)
    @reg_rxpassbeacon0_ena.setter
    def reg_rxpassbeacon0_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxpassbeacon0_ena_msb, self.__reg_rxpassbeacon0_ena_lsb, value)

    @property
    def reg_rxabortgroup0_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxabortgroup0_ena_msb, self.__reg_rxabortgroup0_ena_lsb)
    @reg_rxabortgroup0_ena.setter
    def reg_rxabortgroup0_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxabortgroup0_ena_msb, self.__reg_rxabortgroup0_ena_lsb, value)

    @property
    def reg_rxabortbbsc0_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxabortbbsc0_ena_msb, self.__reg_rxabortbbsc0_ena_lsb)
    @reg_rxabortbbsc0_ena.setter
    def reg_rxabortbbsc0_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxabortbbsc0_ena_msb, self.__reg_rxabortbbsc0_ena_lsb, value)

    @property
    def reg_rxabortubsc0_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxabortubsc0_ena_msb, self.__reg_rxabortubsc0_ena_lsb)
    @reg_rxabortubsc0_ena.setter
    def reg_rxabortubsc0_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxabortubsc0_ena_msb, self.__reg_rxabortubsc0_ena_lsb, value)

    @property
    def reg_rxabortudac0_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxabortudac0_ena_msb, self.__reg_rxabortudac0_ena_lsb)
    @reg_rxabortudac0_ena.setter
    def reg_rxabortudac0_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxabortudac0_ena_msb, self.__reg_rxabortudac0_ena_lsb, value)
class MACRX_ABORT1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0xe4
        self.__reg_autoack_secerr1_dis_lsb = 16
        self.__reg_autoack_secerr1_dis_msb = 16
        self.__reg_autoack_disable1_lsb = 15
        self.__reg_autoack_disable1_msb = 15
        self.__reg_autoack_notgroup1_lsb = 14
        self.__reg_autoack_notgroup1_msb = 14
        self.__reg_autoack_bbssid1chk_lsb = 13
        self.__reg_autoack_bbssid1chk_msb = 13
        self.__reg_autoack_da1chk_lsb = 12
        self.__reg_autoack_da1chk_msb = 12
        self.__reg_autoack_bssid1chk_lsb = 11
        self.__reg_autoack_bssid1chk_msb = 11
        self.__reg_autoack_frds1chk_lsb = 10
        self.__reg_autoack_frds1chk_msb = 10
        self.__reg_autoack_tods1chk_lsb = 9
        self.__reg_autoack_tods1chk_msb = 9
        self.__reg_rxmanager_notck1_bssid_lsb = 8
        self.__reg_rxmanager_notck1_bssid_msb = 8
        self.__reg_rxsecerr_dump1_ena_lsb = 7
        self.__reg_rxsecerr_dump1_ena_msb = 7
        self.__reg_rxsectkiperr_dump1_ena_lsb = 6
        self.__reg_rxsectkiperr_dump1_ena_msb = 6
        self.__reg_rxsamebm_dump1_ena_lsb = 5
        self.__reg_rxsamebm_dump1_ena_msb = 5
        self.__reg_rxpassbeacon1_ena_lsb = 4
        self.__reg_rxpassbeacon1_ena_msb = 4
        self.__reg_rxabortgroup1_ena_lsb = 3
        self.__reg_rxabortgroup1_ena_msb = 3
        self.__reg_rxabortbbsc1_ena_lsb = 2
        self.__reg_rxabortbbsc1_ena_msb = 2
        self.__reg_rxabortubsc1_ena_lsb = 1
        self.__reg_rxabortubsc1_ena_msb = 1
        self.__reg_rxabortudac1_ena_lsb = 0
        self.__reg_rxabortudac1_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_autoack_secerr1_dis(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_secerr1_dis_msb, self.__reg_autoack_secerr1_dis_lsb)
    @reg_autoack_secerr1_dis.setter
    def reg_autoack_secerr1_dis(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_secerr1_dis_msb, self.__reg_autoack_secerr1_dis_lsb, value)

    @property
    def reg_autoack_disable1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_disable1_msb, self.__reg_autoack_disable1_lsb)
    @reg_autoack_disable1.setter
    def reg_autoack_disable1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_disable1_msb, self.__reg_autoack_disable1_lsb, value)

    @property
    def reg_autoack_notgroup1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_notgroup1_msb, self.__reg_autoack_notgroup1_lsb)
    @reg_autoack_notgroup1.setter
    def reg_autoack_notgroup1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_notgroup1_msb, self.__reg_autoack_notgroup1_lsb, value)

    @property
    def reg_autoack_bbssid1chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_bbssid1chk_msb, self.__reg_autoack_bbssid1chk_lsb)
    @reg_autoack_bbssid1chk.setter
    def reg_autoack_bbssid1chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_bbssid1chk_msb, self.__reg_autoack_bbssid1chk_lsb, value)

    @property
    def reg_autoack_da1chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_da1chk_msb, self.__reg_autoack_da1chk_lsb)
    @reg_autoack_da1chk.setter
    def reg_autoack_da1chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_da1chk_msb, self.__reg_autoack_da1chk_lsb, value)

    @property
    def reg_autoack_bssid1chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_bssid1chk_msb, self.__reg_autoack_bssid1chk_lsb)
    @reg_autoack_bssid1chk.setter
    def reg_autoack_bssid1chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_bssid1chk_msb, self.__reg_autoack_bssid1chk_lsb, value)

    @property
    def reg_autoack_frds1chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_frds1chk_msb, self.__reg_autoack_frds1chk_lsb)
    @reg_autoack_frds1chk.setter
    def reg_autoack_frds1chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_frds1chk_msb, self.__reg_autoack_frds1chk_lsb, value)

    @property
    def reg_autoack_tods1chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_tods1chk_msb, self.__reg_autoack_tods1chk_lsb)
    @reg_autoack_tods1chk.setter
    def reg_autoack_tods1chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_tods1chk_msb, self.__reg_autoack_tods1chk_lsb, value)

    @property
    def reg_rxmanager_notck1_bssid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxmanager_notck1_bssid_msb, self.__reg_rxmanager_notck1_bssid_lsb)
    @reg_rxmanager_notck1_bssid.setter
    def reg_rxmanager_notck1_bssid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxmanager_notck1_bssid_msb, self.__reg_rxmanager_notck1_bssid_lsb, value)

    @property
    def reg_rxsecerr_dump1_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxsecerr_dump1_ena_msb, self.__reg_rxsecerr_dump1_ena_lsb)
    @reg_rxsecerr_dump1_ena.setter
    def reg_rxsecerr_dump1_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxsecerr_dump1_ena_msb, self.__reg_rxsecerr_dump1_ena_lsb, value)

    @property
    def reg_rxsectkiperr_dump1_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxsectkiperr_dump1_ena_msb, self.__reg_rxsectkiperr_dump1_ena_lsb)
    @reg_rxsectkiperr_dump1_ena.setter
    def reg_rxsectkiperr_dump1_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxsectkiperr_dump1_ena_msb, self.__reg_rxsectkiperr_dump1_ena_lsb, value)

    @property
    def reg_rxsamebm_dump1_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxsamebm_dump1_ena_msb, self.__reg_rxsamebm_dump1_ena_lsb)
    @reg_rxsamebm_dump1_ena.setter
    def reg_rxsamebm_dump1_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxsamebm_dump1_ena_msb, self.__reg_rxsamebm_dump1_ena_lsb, value)

    @property
    def reg_rxpassbeacon1_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxpassbeacon1_ena_msb, self.__reg_rxpassbeacon1_ena_lsb)
    @reg_rxpassbeacon1_ena.setter
    def reg_rxpassbeacon1_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxpassbeacon1_ena_msb, self.__reg_rxpassbeacon1_ena_lsb, value)

    @property
    def reg_rxabortgroup1_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxabortgroup1_ena_msb, self.__reg_rxabortgroup1_ena_lsb)
    @reg_rxabortgroup1_ena.setter
    def reg_rxabortgroup1_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxabortgroup1_ena_msb, self.__reg_rxabortgroup1_ena_lsb, value)

    @property
    def reg_rxabortbbsc1_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxabortbbsc1_ena_msb, self.__reg_rxabortbbsc1_ena_lsb)
    @reg_rxabortbbsc1_ena.setter
    def reg_rxabortbbsc1_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxabortbbsc1_ena_msb, self.__reg_rxabortbbsc1_ena_lsb, value)

    @property
    def reg_rxabortubsc1_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxabortubsc1_ena_msb, self.__reg_rxabortubsc1_ena_lsb)
    @reg_rxabortubsc1_ena.setter
    def reg_rxabortubsc1_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxabortubsc1_ena_msb, self.__reg_rxabortubsc1_ena_lsb, value)

    @property
    def reg_rxabortudac1_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxabortudac1_ena_msb, self.__reg_rxabortudac1_ena_lsb)
    @reg_rxabortudac1_ena.setter
    def reg_rxabortudac1_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxabortudac1_ena_msb, self.__reg_rxabortudac1_ena_lsb, value)
class MACRX_ABORT2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0xe8
        self.__reg_autoack_secerr2_dis_lsb = 16
        self.__reg_autoack_secerr2_dis_msb = 16
        self.__reg_autoack_disable2_lsb = 15
        self.__reg_autoack_disable2_msb = 15
        self.__reg_autoack_notgroup2_lsb = 14
        self.__reg_autoack_notgroup2_msb = 14
        self.__reg_autoack_bbssid2chk_lsb = 13
        self.__reg_autoack_bbssid2chk_msb = 13
        self.__reg_autoack_da2chk_lsb = 12
        self.__reg_autoack_da2chk_msb = 12
        self.__reg_autoack_bssid2chk_lsb = 11
        self.__reg_autoack_bssid2chk_msb = 11
        self.__reg_autoack_frds2chk_lsb = 10
        self.__reg_autoack_frds2chk_msb = 10
        self.__reg_autoack_tods2chk_lsb = 9
        self.__reg_autoack_tods2chk_msb = 9
        self.__reg_rxmanager_notck2_bssid_lsb = 8
        self.__reg_rxmanager_notck2_bssid_msb = 8
        self.__reg_rxsecerr_dump2_ena_lsb = 7
        self.__reg_rxsecerr_dump2_ena_msb = 7
        self.__reg_rxsectkiperr_dump2_ena_lsb = 6
        self.__reg_rxsectkiperr_dump2_ena_msb = 6
        self.__reg_rxsamebm_dump2_ena_lsb = 5
        self.__reg_rxsamebm_dump2_ena_msb = 5
        self.__reg_rxpassbeacon2_ena_lsb = 4
        self.__reg_rxpassbeacon2_ena_msb = 4
        self.__reg_rxabortgroup2_ena_lsb = 3
        self.__reg_rxabortgroup2_ena_msb = 3
        self.__reg_rxabortbbsc2_ena_lsb = 2
        self.__reg_rxabortbbsc2_ena_msb = 2
        self.__reg_rxabortubsc2_ena_lsb = 1
        self.__reg_rxabortubsc2_ena_msb = 1
        self.__reg_rxabortudac2_ena_lsb = 0
        self.__reg_rxabortudac2_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_autoack_secerr2_dis(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_secerr2_dis_msb, self.__reg_autoack_secerr2_dis_lsb)
    @reg_autoack_secerr2_dis.setter
    def reg_autoack_secerr2_dis(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_secerr2_dis_msb, self.__reg_autoack_secerr2_dis_lsb, value)

    @property
    def reg_autoack_disable2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_disable2_msb, self.__reg_autoack_disable2_lsb)
    @reg_autoack_disable2.setter
    def reg_autoack_disable2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_disable2_msb, self.__reg_autoack_disable2_lsb, value)

    @property
    def reg_autoack_notgroup2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_notgroup2_msb, self.__reg_autoack_notgroup2_lsb)
    @reg_autoack_notgroup2.setter
    def reg_autoack_notgroup2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_notgroup2_msb, self.__reg_autoack_notgroup2_lsb, value)

    @property
    def reg_autoack_bbssid2chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_bbssid2chk_msb, self.__reg_autoack_bbssid2chk_lsb)
    @reg_autoack_bbssid2chk.setter
    def reg_autoack_bbssid2chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_bbssid2chk_msb, self.__reg_autoack_bbssid2chk_lsb, value)

    @property
    def reg_autoack_da2chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_da2chk_msb, self.__reg_autoack_da2chk_lsb)
    @reg_autoack_da2chk.setter
    def reg_autoack_da2chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_da2chk_msb, self.__reg_autoack_da2chk_lsb, value)

    @property
    def reg_autoack_bssid2chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_bssid2chk_msb, self.__reg_autoack_bssid2chk_lsb)
    @reg_autoack_bssid2chk.setter
    def reg_autoack_bssid2chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_bssid2chk_msb, self.__reg_autoack_bssid2chk_lsb, value)

    @property
    def reg_autoack_frds2chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_frds2chk_msb, self.__reg_autoack_frds2chk_lsb)
    @reg_autoack_frds2chk.setter
    def reg_autoack_frds2chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_frds2chk_msb, self.__reg_autoack_frds2chk_lsb, value)

    @property
    def reg_autoack_tods2chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_tods2chk_msb, self.__reg_autoack_tods2chk_lsb)
    @reg_autoack_tods2chk.setter
    def reg_autoack_tods2chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_tods2chk_msb, self.__reg_autoack_tods2chk_lsb, value)

    @property
    def reg_rxmanager_notck2_bssid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxmanager_notck2_bssid_msb, self.__reg_rxmanager_notck2_bssid_lsb)
    @reg_rxmanager_notck2_bssid.setter
    def reg_rxmanager_notck2_bssid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxmanager_notck2_bssid_msb, self.__reg_rxmanager_notck2_bssid_lsb, value)

    @property
    def reg_rxsecerr_dump2_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxsecerr_dump2_ena_msb, self.__reg_rxsecerr_dump2_ena_lsb)
    @reg_rxsecerr_dump2_ena.setter
    def reg_rxsecerr_dump2_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxsecerr_dump2_ena_msb, self.__reg_rxsecerr_dump2_ena_lsb, value)

    @property
    def reg_rxsectkiperr_dump2_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxsectkiperr_dump2_ena_msb, self.__reg_rxsectkiperr_dump2_ena_lsb)
    @reg_rxsectkiperr_dump2_ena.setter
    def reg_rxsectkiperr_dump2_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxsectkiperr_dump2_ena_msb, self.__reg_rxsectkiperr_dump2_ena_lsb, value)

    @property
    def reg_rxsamebm_dump2_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxsamebm_dump2_ena_msb, self.__reg_rxsamebm_dump2_ena_lsb)
    @reg_rxsamebm_dump2_ena.setter
    def reg_rxsamebm_dump2_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxsamebm_dump2_ena_msb, self.__reg_rxsamebm_dump2_ena_lsb, value)

    @property
    def reg_rxpassbeacon2_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxpassbeacon2_ena_msb, self.__reg_rxpassbeacon2_ena_lsb)
    @reg_rxpassbeacon2_ena.setter
    def reg_rxpassbeacon2_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxpassbeacon2_ena_msb, self.__reg_rxpassbeacon2_ena_lsb, value)

    @property
    def reg_rxabortgroup2_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxabortgroup2_ena_msb, self.__reg_rxabortgroup2_ena_lsb)
    @reg_rxabortgroup2_ena.setter
    def reg_rxabortgroup2_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxabortgroup2_ena_msb, self.__reg_rxabortgroup2_ena_lsb, value)

    @property
    def reg_rxabortbbsc2_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxabortbbsc2_ena_msb, self.__reg_rxabortbbsc2_ena_lsb)
    @reg_rxabortbbsc2_ena.setter
    def reg_rxabortbbsc2_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxabortbbsc2_ena_msb, self.__reg_rxabortbbsc2_ena_lsb, value)

    @property
    def reg_rxabortubsc2_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxabortubsc2_ena_msb, self.__reg_rxabortubsc2_ena_lsb)
    @reg_rxabortubsc2_ena.setter
    def reg_rxabortubsc2_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxabortubsc2_ena_msb, self.__reg_rxabortubsc2_ena_lsb, value)

    @property
    def reg_rxabortudac2_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxabortudac2_ena_msb, self.__reg_rxabortudac2_ena_lsb)
    @reg_rxabortudac2_ena.setter
    def reg_rxabortudac2_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxabortudac2_ena_msb, self.__reg_rxabortudac2_ena_lsb, value)
class MACRX_ABORT3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0xec
        self.__reg_autoack_secerr3_dis_lsb = 16
        self.__reg_autoack_secerr3_dis_msb = 16
        self.__reg_autoack_disable3_lsb = 15
        self.__reg_autoack_disable3_msb = 15
        self.__reg_autoack_notgroup3_lsb = 14
        self.__reg_autoack_notgroup3_msb = 14
        self.__reg_autoack_bbssid3chk_lsb = 13
        self.__reg_autoack_bbssid3chk_msb = 13
        self.__reg_autoack_da3chk_lsb = 12
        self.__reg_autoack_da3chk_msb = 12
        self.__reg_autoack_bssid3chk_lsb = 11
        self.__reg_autoack_bssid3chk_msb = 11
        self.__reg_autoack_frds3chk_lsb = 10
        self.__reg_autoack_frds3chk_msb = 10
        self.__reg_autoack_tods3chk_lsb = 9
        self.__reg_autoack_tods3chk_msb = 9
        self.__reg_rxmanager_notck3_bssid_lsb = 8
        self.__reg_rxmanager_notck3_bssid_msb = 8
        self.__reg_rxsecerr_dump3_ena_lsb = 7
        self.__reg_rxsecerr_dump3_ena_msb = 7
        self.__reg_rxsectkiperr_dump3_ena_lsb = 6
        self.__reg_rxsectkiperr_dump3_ena_msb = 6
        self.__reg_rxsamebm_dump3_ena_lsb = 5
        self.__reg_rxsamebm_dump3_ena_msb = 5
        self.__reg_rxpassbeacon3_ena_lsb = 4
        self.__reg_rxpassbeacon3_ena_msb = 4
        self.__reg_rxabortgroup3_ena_lsb = 3
        self.__reg_rxabortgroup3_ena_msb = 3
        self.__reg_rxabortbbsc3_ena_lsb = 2
        self.__reg_rxabortbbsc3_ena_msb = 2
        self.__reg_rxabortubsc3_ena_lsb = 1
        self.__reg_rxabortubsc3_ena_msb = 1
        self.__reg_rxabortudac3_ena_lsb = 0
        self.__reg_rxabortudac3_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_autoack_secerr3_dis(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_secerr3_dis_msb, self.__reg_autoack_secerr3_dis_lsb)
    @reg_autoack_secerr3_dis.setter
    def reg_autoack_secerr3_dis(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_secerr3_dis_msb, self.__reg_autoack_secerr3_dis_lsb, value)

    @property
    def reg_autoack_disable3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_disable3_msb, self.__reg_autoack_disable3_lsb)
    @reg_autoack_disable3.setter
    def reg_autoack_disable3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_disable3_msb, self.__reg_autoack_disable3_lsb, value)

    @property
    def reg_autoack_notgroup3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_notgroup3_msb, self.__reg_autoack_notgroup3_lsb)
    @reg_autoack_notgroup3.setter
    def reg_autoack_notgroup3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_notgroup3_msb, self.__reg_autoack_notgroup3_lsb, value)

    @property
    def reg_autoack_bbssid3chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_bbssid3chk_msb, self.__reg_autoack_bbssid3chk_lsb)
    @reg_autoack_bbssid3chk.setter
    def reg_autoack_bbssid3chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_bbssid3chk_msb, self.__reg_autoack_bbssid3chk_lsb, value)

    @property
    def reg_autoack_da3chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_da3chk_msb, self.__reg_autoack_da3chk_lsb)
    @reg_autoack_da3chk.setter
    def reg_autoack_da3chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_da3chk_msb, self.__reg_autoack_da3chk_lsb, value)

    @property
    def reg_autoack_bssid3chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_bssid3chk_msb, self.__reg_autoack_bssid3chk_lsb)
    @reg_autoack_bssid3chk.setter
    def reg_autoack_bssid3chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_bssid3chk_msb, self.__reg_autoack_bssid3chk_lsb, value)

    @property
    def reg_autoack_frds3chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_frds3chk_msb, self.__reg_autoack_frds3chk_lsb)
    @reg_autoack_frds3chk.setter
    def reg_autoack_frds3chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_frds3chk_msb, self.__reg_autoack_frds3chk_lsb, value)

    @property
    def reg_autoack_tods3chk(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autoack_tods3chk_msb, self.__reg_autoack_tods3chk_lsb)
    @reg_autoack_tods3chk.setter
    def reg_autoack_tods3chk(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autoack_tods3chk_msb, self.__reg_autoack_tods3chk_lsb, value)

    @property
    def reg_rxmanager_notck3_bssid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxmanager_notck3_bssid_msb, self.__reg_rxmanager_notck3_bssid_lsb)
    @reg_rxmanager_notck3_bssid.setter
    def reg_rxmanager_notck3_bssid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxmanager_notck3_bssid_msb, self.__reg_rxmanager_notck3_bssid_lsb, value)

    @property
    def reg_rxsecerr_dump3_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxsecerr_dump3_ena_msb, self.__reg_rxsecerr_dump3_ena_lsb)
    @reg_rxsecerr_dump3_ena.setter
    def reg_rxsecerr_dump3_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxsecerr_dump3_ena_msb, self.__reg_rxsecerr_dump3_ena_lsb, value)

    @property
    def reg_rxsectkiperr_dump3_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxsectkiperr_dump3_ena_msb, self.__reg_rxsectkiperr_dump3_ena_lsb)
    @reg_rxsectkiperr_dump3_ena.setter
    def reg_rxsectkiperr_dump3_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxsectkiperr_dump3_ena_msb, self.__reg_rxsectkiperr_dump3_ena_lsb, value)

    @property
    def reg_rxsamebm_dump3_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxsamebm_dump3_ena_msb, self.__reg_rxsamebm_dump3_ena_lsb)
    @reg_rxsamebm_dump3_ena.setter
    def reg_rxsamebm_dump3_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxsamebm_dump3_ena_msb, self.__reg_rxsamebm_dump3_ena_lsb, value)

    @property
    def reg_rxpassbeacon3_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxpassbeacon3_ena_msb, self.__reg_rxpassbeacon3_ena_lsb)
    @reg_rxpassbeacon3_ena.setter
    def reg_rxpassbeacon3_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxpassbeacon3_ena_msb, self.__reg_rxpassbeacon3_ena_lsb, value)

    @property
    def reg_rxabortgroup3_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxabortgroup3_ena_msb, self.__reg_rxabortgroup3_ena_lsb)
    @reg_rxabortgroup3_ena.setter
    def reg_rxabortgroup3_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxabortgroup3_ena_msb, self.__reg_rxabortgroup3_ena_lsb, value)

    @property
    def reg_rxabortbbsc3_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxabortbbsc3_ena_msb, self.__reg_rxabortbbsc3_ena_lsb)
    @reg_rxabortbbsc3_ena.setter
    def reg_rxabortbbsc3_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxabortbbsc3_ena_msb, self.__reg_rxabortbbsc3_ena_lsb, value)

    @property
    def reg_rxabortubsc3_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxabortubsc3_ena_msb, self.__reg_rxabortubsc3_ena_lsb)
    @reg_rxabortubsc3_ena.setter
    def reg_rxabortubsc3_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxabortubsc3_ena_msb, self.__reg_rxabortubsc3_ena_lsb, value)

    @property
    def reg_rxabortudac3_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxabortudac3_ena_msb, self.__reg_rxabortudac3_ena_lsb)
    @reg_rxabortudac3_ena.setter
    def reg_rxabortudac3_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxabortudac3_ena_msb, self.__reg_rxabortudac3_ena_lsb, value)
class MACRX_DUMP0_ERRCODE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0xf0
        self.__reg_dump0_errcode_lsb = 8
        self.__reg_dump0_errcode_msb = 15
        self.__reg_dump0_errcode_mask_lsb = 0
        self.__reg_dump0_errcode_mask_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_dump0_errcode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dump0_errcode_msb, self.__reg_dump0_errcode_lsb)
    @reg_dump0_errcode.setter
    def reg_dump0_errcode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dump0_errcode_msb, self.__reg_dump0_errcode_lsb, value)

    @property
    def reg_dump0_errcode_mask(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dump0_errcode_mask_msb, self.__reg_dump0_errcode_mask_lsb)
    @reg_dump0_errcode_mask.setter
    def reg_dump0_errcode_mask(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dump0_errcode_mask_msb, self.__reg_dump0_errcode_mask_lsb, value)
class MACRX_DUMP1_ERRCODE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0xf4
        self.__reg_dump1_errcode_lsb = 8
        self.__reg_dump1_errcode_msb = 15
        self.__reg_dump1_errcode_mask_lsb = 0
        self.__reg_dump1_errcode_mask_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_dump1_errcode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dump1_errcode_msb, self.__reg_dump1_errcode_lsb)
    @reg_dump1_errcode.setter
    def reg_dump1_errcode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dump1_errcode_msb, self.__reg_dump1_errcode_lsb, value)

    @property
    def reg_dump1_errcode_mask(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dump1_errcode_mask_msb, self.__reg_dump1_errcode_mask_lsb)
    @reg_dump1_errcode_mask.setter
    def reg_dump1_errcode_mask(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dump1_errcode_mask_msb, self.__reg_dump1_errcode_mask_lsb, value)
class MACRX_DUMP2_ERRCODE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0xf8
        self.__reg_dump2_errcode_lsb = 8
        self.__reg_dump2_errcode_msb = 15
        self.__reg_dump2_errcode_mask_lsb = 0
        self.__reg_dump2_errcode_mask_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_dump2_errcode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dump2_errcode_msb, self.__reg_dump2_errcode_lsb)
    @reg_dump2_errcode.setter
    def reg_dump2_errcode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dump2_errcode_msb, self.__reg_dump2_errcode_lsb, value)

    @property
    def reg_dump2_errcode_mask(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dump2_errcode_mask_msb, self.__reg_dump2_errcode_mask_lsb)
    @reg_dump2_errcode_mask.setter
    def reg_dump2_errcode_mask(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dump2_errcode_mask_msb, self.__reg_dump2_errcode_mask_lsb, value)
class MACRX_DUMP3_ERRCODE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0xfc
        self.__reg_dump3_errcode_lsb = 8
        self.__reg_dump3_errcode_msb = 15
        self.__reg_dump3_errcode_mask_lsb = 0
        self.__reg_dump3_errcode_mask_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_dump3_errcode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dump3_errcode_msb, self.__reg_dump3_errcode_lsb)
    @reg_dump3_errcode.setter
    def reg_dump3_errcode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dump3_errcode_msb, self.__reg_dump3_errcode_lsb, value)

    @property
    def reg_dump3_errcode_mask(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dump3_errcode_mask_msb, self.__reg_dump3_errcode_mask_lsb)
    @reg_dump3_errcode_mask.setter
    def reg_dump3_errcode_mask(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dump3_errcode_mask_msb, self.__reg_dump3_errcode_mask_lsb, value)
class MACRX_DUMP3_ERRCODE1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x100
        self.__reg_dump3_errcode1_lsb = 8
        self.__reg_dump3_errcode1_msb = 15
        self.__reg_dump3_errcode1_mask_lsb = 0
        self.__reg_dump3_errcode1_mask_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_dump3_errcode1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dump3_errcode1_msb, self.__reg_dump3_errcode1_lsb)
    @reg_dump3_errcode1.setter
    def reg_dump3_errcode1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dump3_errcode1_msb, self.__reg_dump3_errcode1_lsb, value)

    @property
    def reg_dump3_errcode1_mask(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dump3_errcode1_mask_msb, self.__reg_dump3_errcode1_mask_lsb)
    @reg_dump3_errcode1_mask.setter
    def reg_dump3_errcode1_mask(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dump3_errcode1_mask_msb, self.__reg_dump3_errcode1_mask_lsb, value)
class MACRX_DUMP3_ERRCODE2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x104
        self.__reg_dump3_errcode2_lsb = 8
        self.__reg_dump3_errcode2_msb = 15
        self.__reg_dump3_errcode2_mask_lsb = 0
        self.__reg_dump3_errcode2_mask_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_dump3_errcode2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dump3_errcode2_msb, self.__reg_dump3_errcode2_lsb)
    @reg_dump3_errcode2.setter
    def reg_dump3_errcode2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dump3_errcode2_msb, self.__reg_dump3_errcode2_lsb, value)

    @property
    def reg_dump3_errcode2_mask(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dump3_errcode2_mask_msb, self.__reg_dump3_errcode2_mask_lsb)
    @reg_dump3_errcode2_mask.setter
    def reg_dump3_errcode2_mask(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dump3_errcode2_mask_msb, self.__reg_dump3_errcode2_mask_lsb, value)
class MACRX_DUMP0_LIM(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x108
        self.__reg_rxctldump0_ena_lsb = 16
        self.__reg_rxctldump0_ena_msb = 31
        self.__reg_rxdump0_len_lsb = 0
        self.__reg_rxdump0_len_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxctldump0_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxctldump0_ena_msb, self.__reg_rxctldump0_ena_lsb)
    @reg_rxctldump0_ena.setter
    def reg_rxctldump0_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxctldump0_ena_msb, self.__reg_rxctldump0_ena_lsb, value)

    @property
    def reg_rxdump0_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdump0_len_msb, self.__reg_rxdump0_len_lsb)
    @reg_rxdump0_len.setter
    def reg_rxdump0_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdump0_len_msb, self.__reg_rxdump0_len_lsb, value)
class MACRX_DUMP1_LIM(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x10c
        self.__reg_rxctldump1_ena_lsb = 16
        self.__reg_rxctldump1_ena_msb = 31
        self.__reg_rxdump1_len_lsb = 0
        self.__reg_rxdump1_len_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxctldump1_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxctldump1_ena_msb, self.__reg_rxctldump1_ena_lsb)
    @reg_rxctldump1_ena.setter
    def reg_rxctldump1_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxctldump1_ena_msb, self.__reg_rxctldump1_ena_lsb, value)

    @property
    def reg_rxdump1_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdump1_len_msb, self.__reg_rxdump1_len_lsb)
    @reg_rxdump1_len.setter
    def reg_rxdump1_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdump1_len_msb, self.__reg_rxdump1_len_lsb, value)
class MACRX_DUMP2_LIM(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x110
        self.__reg_rxctldump2_ena_lsb = 16
        self.__reg_rxctldump2_ena_msb = 31
        self.__reg_rxdump2_len_lsb = 0
        self.__reg_rxdump2_len_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxctldump2_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxctldump2_ena_msb, self.__reg_rxctldump2_ena_lsb)
    @reg_rxctldump2_ena.setter
    def reg_rxctldump2_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxctldump2_ena_msb, self.__reg_rxctldump2_ena_lsb, value)

    @property
    def reg_rxdump2_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdump2_len_msb, self.__reg_rxdump2_len_lsb)
    @reg_rxdump2_len.setter
    def reg_rxdump2_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdump2_len_msb, self.__reg_rxdump2_len_lsb, value)
class MACRX_DUMP3_LIM(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x114
        self.__reg_rxctldump3_ena_lsb = 16
        self.__reg_rxctldump3_ena_msb = 31
        self.__reg_rxdump3_len_lsb = 0
        self.__reg_rxdump3_len_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxctldump3_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxctldump3_ena_msb, self.__reg_rxctldump3_ena_lsb)
    @reg_rxctldump3_ena.setter
    def reg_rxctldump3_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxctldump3_ena_msb, self.__reg_rxctldump3_ena_lsb, value)

    @property
    def reg_rxdump3_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdump3_len_msb, self.__reg_rxdump3_len_lsb)
    @reg_rxdump3_len.setter
    def reg_rxdump3_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdump3_len_msb, self.__reg_rxdump3_len_lsb, value)
class MACRXCTR_BSSIDLIST(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x118
        self.__reg_rxctl15_bssid_pos_lsb = 30
        self.__reg_rxctl15_bssid_pos_msb = 31
        self.__reg_rxctl14_bssid_pos_lsb = 28
        self.__reg_rxctl14_bssid_pos_msb = 29
        self.__reg_rxctl13_bssid_pos_lsb = 26
        self.__reg_rxctl13_bssid_pos_msb = 27
        self.__reg_rxctl12_bssid_pos_lsb = 24
        self.__reg_rxctl12_bssid_pos_msb = 25
        self.__reg_rxctl11_bssid_pos_lsb = 22
        self.__reg_rxctl11_bssid_pos_msb = 23
        self.__reg_rxctl10_bssid_pos_lsb = 20
        self.__reg_rxctl10_bssid_pos_msb = 21
        self.__reg_rxctl9_bssid_pos_lsb = 18
        self.__reg_rxctl9_bssid_pos_msb = 19
        self.__reg_rxctl8_bssid_pos_lsb = 16
        self.__reg_rxctl8_bssid_pos_msb = 17
        self.__reg_rxctl7_bssid_pos_lsb = 14
        self.__reg_rxctl7_bssid_pos_msb = 15
        self.__reg_rxctl6_bssid_pos_lsb = 12
        self.__reg_rxctl6_bssid_pos_msb = 13
        self.__reg_rxctl5_bssid_pos_lsb = 10
        self.__reg_rxctl5_bssid_pos_msb = 11
        self.__reg_rxctl4_bssid_pos_lsb = 8
        self.__reg_rxctl4_bssid_pos_msb = 9
        self.__reg_rxctl3_bssid_pos_lsb = 6
        self.__reg_rxctl3_bssid_pos_msb = 7
        self.__reg_rxctl2_bssid_pos_lsb = 4
        self.__reg_rxctl2_bssid_pos_msb = 5
        self.__reg_rxctl1_bssid_pos_lsb = 2
        self.__reg_rxctl1_bssid_pos_msb = 3
        self.__reg_rxctl0_bssid_pos_lsb = 0
        self.__reg_rxctl0_bssid_pos_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxctl15_bssid_pos(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxctl15_bssid_pos_msb, self.__reg_rxctl15_bssid_pos_lsb)
    @reg_rxctl15_bssid_pos.setter
    def reg_rxctl15_bssid_pos(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxctl15_bssid_pos_msb, self.__reg_rxctl15_bssid_pos_lsb, value)

    @property
    def reg_rxctl14_bssid_pos(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxctl14_bssid_pos_msb, self.__reg_rxctl14_bssid_pos_lsb)
    @reg_rxctl14_bssid_pos.setter
    def reg_rxctl14_bssid_pos(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxctl14_bssid_pos_msb, self.__reg_rxctl14_bssid_pos_lsb, value)

    @property
    def reg_rxctl13_bssid_pos(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxctl13_bssid_pos_msb, self.__reg_rxctl13_bssid_pos_lsb)
    @reg_rxctl13_bssid_pos.setter
    def reg_rxctl13_bssid_pos(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxctl13_bssid_pos_msb, self.__reg_rxctl13_bssid_pos_lsb, value)

    @property
    def reg_rxctl12_bssid_pos(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxctl12_bssid_pos_msb, self.__reg_rxctl12_bssid_pos_lsb)
    @reg_rxctl12_bssid_pos.setter
    def reg_rxctl12_bssid_pos(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxctl12_bssid_pos_msb, self.__reg_rxctl12_bssid_pos_lsb, value)

    @property
    def reg_rxctl11_bssid_pos(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxctl11_bssid_pos_msb, self.__reg_rxctl11_bssid_pos_lsb)
    @reg_rxctl11_bssid_pos.setter
    def reg_rxctl11_bssid_pos(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxctl11_bssid_pos_msb, self.__reg_rxctl11_bssid_pos_lsb, value)

    @property
    def reg_rxctl10_bssid_pos(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxctl10_bssid_pos_msb, self.__reg_rxctl10_bssid_pos_lsb)
    @reg_rxctl10_bssid_pos.setter
    def reg_rxctl10_bssid_pos(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxctl10_bssid_pos_msb, self.__reg_rxctl10_bssid_pos_lsb, value)

    @property
    def reg_rxctl9_bssid_pos(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxctl9_bssid_pos_msb, self.__reg_rxctl9_bssid_pos_lsb)
    @reg_rxctl9_bssid_pos.setter
    def reg_rxctl9_bssid_pos(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxctl9_bssid_pos_msb, self.__reg_rxctl9_bssid_pos_lsb, value)

    @property
    def reg_rxctl8_bssid_pos(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxctl8_bssid_pos_msb, self.__reg_rxctl8_bssid_pos_lsb)
    @reg_rxctl8_bssid_pos.setter
    def reg_rxctl8_bssid_pos(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxctl8_bssid_pos_msb, self.__reg_rxctl8_bssid_pos_lsb, value)

    @property
    def reg_rxctl7_bssid_pos(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxctl7_bssid_pos_msb, self.__reg_rxctl7_bssid_pos_lsb)
    @reg_rxctl7_bssid_pos.setter
    def reg_rxctl7_bssid_pos(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxctl7_bssid_pos_msb, self.__reg_rxctl7_bssid_pos_lsb, value)

    @property
    def reg_rxctl6_bssid_pos(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxctl6_bssid_pos_msb, self.__reg_rxctl6_bssid_pos_lsb)
    @reg_rxctl6_bssid_pos.setter
    def reg_rxctl6_bssid_pos(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxctl6_bssid_pos_msb, self.__reg_rxctl6_bssid_pos_lsb, value)

    @property
    def reg_rxctl5_bssid_pos(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxctl5_bssid_pos_msb, self.__reg_rxctl5_bssid_pos_lsb)
    @reg_rxctl5_bssid_pos.setter
    def reg_rxctl5_bssid_pos(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxctl5_bssid_pos_msb, self.__reg_rxctl5_bssid_pos_lsb, value)

    @property
    def reg_rxctl4_bssid_pos(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxctl4_bssid_pos_msb, self.__reg_rxctl4_bssid_pos_lsb)
    @reg_rxctl4_bssid_pos.setter
    def reg_rxctl4_bssid_pos(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxctl4_bssid_pos_msb, self.__reg_rxctl4_bssid_pos_lsb, value)

    @property
    def reg_rxctl3_bssid_pos(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxctl3_bssid_pos_msb, self.__reg_rxctl3_bssid_pos_lsb)
    @reg_rxctl3_bssid_pos.setter
    def reg_rxctl3_bssid_pos(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxctl3_bssid_pos_msb, self.__reg_rxctl3_bssid_pos_lsb, value)

    @property
    def reg_rxctl2_bssid_pos(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxctl2_bssid_pos_msb, self.__reg_rxctl2_bssid_pos_lsb)
    @reg_rxctl2_bssid_pos.setter
    def reg_rxctl2_bssid_pos(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxctl2_bssid_pos_msb, self.__reg_rxctl2_bssid_pos_lsb, value)

    @property
    def reg_rxctl1_bssid_pos(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxctl1_bssid_pos_msb, self.__reg_rxctl1_bssid_pos_lsb)
    @reg_rxctl1_bssid_pos.setter
    def reg_rxctl1_bssid_pos(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxctl1_bssid_pos_msb, self.__reg_rxctl1_bssid_pos_lsb, value)

    @property
    def reg_rxctl0_bssid_pos(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxctl0_bssid_pos_msb, self.__reg_rxctl0_bssid_pos_lsb)
    @reg_rxctl0_bssid_pos.setter
    def reg_rxctl0_bssid_pos(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxctl0_bssid_pos_msb, self.__reg_rxctl0_bssid_pos_lsb, value)
class MACRXQOS_BITMAPUP_LIST(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x11c
        self.__reg_rxqos_bitmapup7_ena_lsb = 7
        self.__reg_rxqos_bitmapup7_ena_msb = 7
        self.__reg_rxqos_bitmapup6_ena_lsb = 6
        self.__reg_rxqos_bitmapup6_ena_msb = 6
        self.__reg_rxqos_bitmapup5_ena_lsb = 5
        self.__reg_rxqos_bitmapup5_ena_msb = 5
        self.__reg_rxqos_bitmapup4_ena_lsb = 4
        self.__reg_rxqos_bitmapup4_ena_msb = 4
        self.__reg_rxqos_bitmapup3_ena_lsb = 3
        self.__reg_rxqos_bitmapup3_ena_msb = 3
        self.__reg_rxqos_bitmapup2_ena_lsb = 2
        self.__reg_rxqos_bitmapup2_ena_msb = 2
        self.__reg_rxqos_bitmapup1_ena_lsb = 1
        self.__reg_rxqos_bitmapup1_ena_msb = 1
        self.__reg_rxqos_bitmapup0_ena_lsb = 0
        self.__reg_rxqos_bitmapup0_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxqos_bitmapup7_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxqos_bitmapup7_ena_msb, self.__reg_rxqos_bitmapup7_ena_lsb)
    @reg_rxqos_bitmapup7_ena.setter
    def reg_rxqos_bitmapup7_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxqos_bitmapup7_ena_msb, self.__reg_rxqos_bitmapup7_ena_lsb, value)

    @property
    def reg_rxqos_bitmapup6_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxqos_bitmapup6_ena_msb, self.__reg_rxqos_bitmapup6_ena_lsb)
    @reg_rxqos_bitmapup6_ena.setter
    def reg_rxqos_bitmapup6_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxqos_bitmapup6_ena_msb, self.__reg_rxqos_bitmapup6_ena_lsb, value)

    @property
    def reg_rxqos_bitmapup5_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxqos_bitmapup5_ena_msb, self.__reg_rxqos_bitmapup5_ena_lsb)
    @reg_rxqos_bitmapup5_ena.setter
    def reg_rxqos_bitmapup5_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxqos_bitmapup5_ena_msb, self.__reg_rxqos_bitmapup5_ena_lsb, value)

    @property
    def reg_rxqos_bitmapup4_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxqos_bitmapup4_ena_msb, self.__reg_rxqos_bitmapup4_ena_lsb)
    @reg_rxqos_bitmapup4_ena.setter
    def reg_rxqos_bitmapup4_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxqos_bitmapup4_ena_msb, self.__reg_rxqos_bitmapup4_ena_lsb, value)

    @property
    def reg_rxqos_bitmapup3_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxqos_bitmapup3_ena_msb, self.__reg_rxqos_bitmapup3_ena_lsb)
    @reg_rxqos_bitmapup3_ena.setter
    def reg_rxqos_bitmapup3_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxqos_bitmapup3_ena_msb, self.__reg_rxqos_bitmapup3_ena_lsb, value)

    @property
    def reg_rxqos_bitmapup2_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxqos_bitmapup2_ena_msb, self.__reg_rxqos_bitmapup2_ena_lsb)
    @reg_rxqos_bitmapup2_ena.setter
    def reg_rxqos_bitmapup2_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxqos_bitmapup2_ena_msb, self.__reg_rxqos_bitmapup2_ena_lsb, value)

    @property
    def reg_rxqos_bitmapup1_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxqos_bitmapup1_ena_msb, self.__reg_rxqos_bitmapup1_ena_lsb)
    @reg_rxqos_bitmapup1_ena.setter
    def reg_rxqos_bitmapup1_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxqos_bitmapup1_ena_msb, self.__reg_rxqos_bitmapup1_ena_lsb, value)

    @property
    def reg_rxqos_bitmapup0_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxqos_bitmapup0_ena_msb, self.__reg_rxqos_bitmapup0_ena_lsb)
    @reg_rxqos_bitmapup0_ena.setter
    def reg_rxqos_bitmapup0_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxqos_bitmapup0_ena_msb, self.__reg_rxqos_bitmapup0_ena_lsb, value)
class MACRX_FACKHT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x120
        self.__reg_rx_fake_ht_lsb = 0
        self.__reg_rx_fake_ht_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rx_fake_ht(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_fake_ht_msb, self.__reg_rx_fake_ht_lsb)
    @reg_rx_fake_ht.setter
    def reg_rx_fake_ht(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_fake_ht_msb, self.__reg_rx_fake_ht_lsb, value)
class MACRXBBTF_ENA(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x124
        self.__reg_rxbbtf_ena_lsb = 31
        self.__reg_rxbbtf_ena_msb = 31
        self.__reg_rxbbtf_timer_lsb = 20
        self.__reg_rxbbtf_timer_msb = 27
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxbbtf_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxbbtf_ena_msb, self.__reg_rxbbtf_ena_lsb)
    @reg_rxbbtf_ena.setter
    def reg_rxbbtf_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxbbtf_ena_msb, self.__reg_rxbbtf_ena_lsb, value)

    @property
    def reg_rxbbtf_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxbbtf_timer_msb, self.__reg_rxbbtf_timer_lsb)
    @reg_rxbbtf_timer.setter
    def reg_rxbbtf_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxbbtf_timer_msb, self.__reg_rxbbtf_timer_lsb, value)
class MACRXADDR_MAX(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x128
        self.__reg_maxrxaddr_lsb = 0
        self.__reg_maxrxaddr_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_maxrxaddr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_maxrxaddr_msb, self.__reg_maxrxaddr_lsb)
    @reg_maxrxaddr.setter
    def reg_maxrxaddr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_maxrxaddr_msb, self.__reg_maxrxaddr_lsb, value)
class MACRXADDR_MIN(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x12c
        self.__reg_minrxaddr_lsb = 0
        self.__reg_minrxaddr_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_minrxaddr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_minrxaddr_msb, self.__reg_minrxaddr_lsb)
    @reg_minrxaddr.setter
    def reg_minrxaddr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_minrxaddr_msb, self.__reg_minrxaddr_lsb, value)
class MACRXENT_MAX(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x130
        self.__reg_maxrxent_lsb = 0
        self.__reg_maxrxent_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_maxrxent(self):
        return self.__MEM.rdm(self.__addr, self.__reg_maxrxent_msb, self.__reg_maxrxent_lsb)
    @reg_maxrxent.setter
    def reg_maxrxent(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_maxrxent_msb, self.__reg_maxrxent_lsb, value)
class MACRXENT_MIN(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x134
        self.__reg_minrxent_lsb = 0
        self.__reg_minrxent_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_minrxent(self):
        return self.__MEM.rdm(self.__addr, self.__reg_minrxent_msb, self.__reg_minrxent_lsb)
    @reg_minrxent.setter
    def reg_minrxent(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_minrxent_msb, self.__reg_minrxent_lsb, value)
class MACBBABORTOPTION(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x138
        self.__reg_bbabort_ena_lsb = 31
        self.__reg_bbabort_ena_msb = 31
        self.__reg_durtrust_ft_lsb = 0
        self.__reg_durtrust_ft_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bbabort_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbabort_ena_msb, self.__reg_bbabort_ena_lsb)
    @reg_bbabort_ena.setter
    def reg_bbabort_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbabort_ena_msb, self.__reg_bbabort_ena_lsb, value)

    @property
    def reg_durtrust_ft(self):
        return self.__MEM.rdm(self.__addr, self.__reg_durtrust_ft_msb, self.__reg_durtrust_ft_lsb)
    @reg_durtrust_ft.setter
    def reg_durtrust_ft(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_durtrust_ft_msb, self.__reg_durtrust_ft_lsb, value)
class MACBBNAVOPTION(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x13c
        self.__reg_bbnav_ena_lsb = 31
        self.__reg_bbnav_ena_msb = 31
        self.__reg_bbnavena_ft_lsb = 0
        self.__reg_bbnavena_ft_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bbnav_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbnav_ena_msb, self.__reg_bbnav_ena_lsb)
    @reg_bbnav_ena.setter
    def reg_bbnav_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbnav_ena_msb, self.__reg_bbnav_ena_lsb, value)

    @property
    def reg_bbnavena_ft(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbnavena_ft_msb, self.__reg_bbnavena_ft_lsb)
    @reg_bbnavena_ft.setter
    def reg_bbnavena_ft(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbnavena_ft_msb, self.__reg_bbnavena_ft_lsb, value)
class MACBBABORT_RSSITAB0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x140
        self.__reg_bbabort_rssi3_lsb = 24
        self.__reg_bbabort_rssi3_msb = 31
        self.__reg_bbabort_rssi2_lsb = 16
        self.__reg_bbabort_rssi2_msb = 23
        self.__reg_bbabort_rssi1_lsb = 8
        self.__reg_bbabort_rssi1_msb = 15
        self.__reg_bbabort_rssi0_lsb = 0
        self.__reg_bbabort_rssi0_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bbabort_rssi3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbabort_rssi3_msb, self.__reg_bbabort_rssi3_lsb)
    @reg_bbabort_rssi3.setter
    def reg_bbabort_rssi3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbabort_rssi3_msb, self.__reg_bbabort_rssi3_lsb, value)

    @property
    def reg_bbabort_rssi2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbabort_rssi2_msb, self.__reg_bbabort_rssi2_lsb)
    @reg_bbabort_rssi2.setter
    def reg_bbabort_rssi2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbabort_rssi2_msb, self.__reg_bbabort_rssi2_lsb, value)

    @property
    def reg_bbabort_rssi1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbabort_rssi1_msb, self.__reg_bbabort_rssi1_lsb)
    @reg_bbabort_rssi1.setter
    def reg_bbabort_rssi1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbabort_rssi1_msb, self.__reg_bbabort_rssi1_lsb, value)

    @property
    def reg_bbabort_rssi0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbabort_rssi0_msb, self.__reg_bbabort_rssi0_lsb)
    @reg_bbabort_rssi0.setter
    def reg_bbabort_rssi0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbabort_rssi0_msb, self.__reg_bbabort_rssi0_lsb, value)
class MACBBABORT_RSSITAB1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x144
        self.__reg_bbabort_rssi7_lsb = 24
        self.__reg_bbabort_rssi7_msb = 31
        self.__reg_bbabort_rssi6_lsb = 16
        self.__reg_bbabort_rssi6_msb = 23
        self.__reg_bbabort_rssi5_lsb = 8
        self.__reg_bbabort_rssi5_msb = 15
        self.__reg_bbabort_rssi4_lsb = 0
        self.__reg_bbabort_rssi4_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bbabort_rssi7(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbabort_rssi7_msb, self.__reg_bbabort_rssi7_lsb)
    @reg_bbabort_rssi7.setter
    def reg_bbabort_rssi7(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbabort_rssi7_msb, self.__reg_bbabort_rssi7_lsb, value)

    @property
    def reg_bbabort_rssi6(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbabort_rssi6_msb, self.__reg_bbabort_rssi6_lsb)
    @reg_bbabort_rssi6.setter
    def reg_bbabort_rssi6(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbabort_rssi6_msb, self.__reg_bbabort_rssi6_lsb, value)

    @property
    def reg_bbabort_rssi5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbabort_rssi5_msb, self.__reg_bbabort_rssi5_lsb)
    @reg_bbabort_rssi5.setter
    def reg_bbabort_rssi5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbabort_rssi5_msb, self.__reg_bbabort_rssi5_lsb, value)

    @property
    def reg_bbabort_rssi4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbabort_rssi4_msb, self.__reg_bbabort_rssi4_lsb)
    @reg_bbabort_rssi4.setter
    def reg_bbabort_rssi4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbabort_rssi4_msb, self.__reg_bbabort_rssi4_lsb, value)
class MACBBABORT_LENTAB0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x148
        self.__reg_bbabort_len3_lsb = 24
        self.__reg_bbabort_len3_msb = 31
        self.__reg_bbabort_len2_lsb = 16
        self.__reg_bbabort_len2_msb = 23
        self.__reg_bbabort_len1_lsb = 8
        self.__reg_bbabort_len1_msb = 15
        self.__reg_bbabort_len0_lsb = 0
        self.__reg_bbabort_len0_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bbabort_len3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbabort_len3_msb, self.__reg_bbabort_len3_lsb)
    @reg_bbabort_len3.setter
    def reg_bbabort_len3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbabort_len3_msb, self.__reg_bbabort_len3_lsb, value)

    @property
    def reg_bbabort_len2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbabort_len2_msb, self.__reg_bbabort_len2_lsb)
    @reg_bbabort_len2.setter
    def reg_bbabort_len2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbabort_len2_msb, self.__reg_bbabort_len2_lsb, value)

    @property
    def reg_bbabort_len1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbabort_len1_msb, self.__reg_bbabort_len1_lsb)
    @reg_bbabort_len1.setter
    def reg_bbabort_len1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbabort_len1_msb, self.__reg_bbabort_len1_lsb, value)

    @property
    def reg_bbabort_len0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbabort_len0_msb, self.__reg_bbabort_len0_lsb)
    @reg_bbabort_len0.setter
    def reg_bbabort_len0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbabort_len0_msb, self.__reg_bbabort_len0_lsb, value)
class MACBBABORT_LENTAB1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x14c
        self.__reg_bbabort_len7_lsb = 24
        self.__reg_bbabort_len7_msb = 31
        self.__reg_bbabort_len6_lsb = 16
        self.__reg_bbabort_len6_msb = 23
        self.__reg_bbabort_len5_lsb = 8
        self.__reg_bbabort_len5_msb = 15
        self.__reg_bbabort_len4_lsb = 0
        self.__reg_bbabort_len4_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bbabort_len7(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbabort_len7_msb, self.__reg_bbabort_len7_lsb)
    @reg_bbabort_len7.setter
    def reg_bbabort_len7(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbabort_len7_msb, self.__reg_bbabort_len7_lsb, value)

    @property
    def reg_bbabort_len6(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbabort_len6_msb, self.__reg_bbabort_len6_lsb)
    @reg_bbabort_len6.setter
    def reg_bbabort_len6(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbabort_len6_msb, self.__reg_bbabort_len6_lsb, value)

    @property
    def reg_bbabort_len5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbabort_len5_msb, self.__reg_bbabort_len5_lsb)
    @reg_bbabort_len5.setter
    def reg_bbabort_len5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbabort_len5_msb, self.__reg_bbabort_len5_lsb, value)

    @property
    def reg_bbabort_len4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbabort_len4_msb, self.__reg_bbabort_len4_lsb)
    @reg_bbabort_len4.setter
    def reg_bbabort_len4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbabort_len4_msb, self.__reg_bbabort_len4_lsb, value)
class MACRX_TXACK_TIMER_CYC(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x150
        self.__reg_rxtxack_timer_start_lsb = 31
        self.__reg_rxtxack_timer_start_msb = 31
        self.__rxtxack_timer_valid_lsb = 30
        self.__rxtxack_timer_valid_msb = 30
        self.__rxtxack_timer_cyc_lsb = 0
        self.__rxtxack_timer_cyc_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxtxack_timer_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxtxack_timer_start_msb, self.__reg_rxtxack_timer_start_lsb)
    @reg_rxtxack_timer_start.setter
    def reg_rxtxack_timer_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxtxack_timer_start_msb, self.__reg_rxtxack_timer_start_lsb, value)

    @property
    def rxtxack_timer_valid(self):
        return self.__MEM.rdm(self.__addr, self.__rxtxack_timer_valid_msb, self.__rxtxack_timer_valid_lsb)
    @rxtxack_timer_valid.setter
    def rxtxack_timer_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxtxack_timer_valid_msb, self.__rxtxack_timer_valid_lsb, value)

    @property
    def rxtxack_timer_cyc(self):
        return self.__MEM.rdm(self.__addr, self.__rxtxack_timer_cyc_msb, self.__rxtxack_timer_cyc_lsb)
    @rxtxack_timer_cyc.setter
    def rxtxack_timer_cyc(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxtxack_timer_cyc_msb, self.__rxtxack_timer_cyc_lsb, value)
class MACRX_TXACK_TIMER_US(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x154
        self.__rxtxack_timer_us_lsb = 0
        self.__rxtxack_timer_us_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxtxack_timer_us(self):
        return self.__MEM.rdm(self.__addr, self.__rxtxack_timer_us_msb, self.__rxtxack_timer_us_lsb)
    @rxtxack_timer_us.setter
    def rxtxack_timer_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxtxack_timer_us_msb, self.__rxtxack_timer_us_lsb, value)
class MACRX_DATA_DUMP_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x158
        self.__reg_rxest_dump_filter0_op_lsb = 27
        self.__reg_rxest_dump_filter0_op_msb = 27
        self.__reg_rxest_dump_filter1_op_lsb = 26
        self.__reg_rxest_dump_filter1_op_msb = 26
        self.__reg_rxest_dump_filter2_op_lsb = 25
        self.__reg_rxest_dump_filter2_op_msb = 25
        self.__reg_rxest_dump_filter3_op_lsb = 24
        self.__reg_rxest_dump_filter3_op_msb = 24
        self.__reg_rxest_dump_filter4_op_lsb = 23
        self.__reg_rxest_dump_filter4_op_msb = 23
        self.__reg_rxest_dump_filter5_op_lsb = 22
        self.__reg_rxest_dump_filter5_op_msb = 22
        self.__reg_rxest_dump_filter6_op_lsb = 21
        self.__reg_rxest_dump_filter6_op_msb = 21
        self.__reg_rxest_dump_filter0_ena_lsb = 20
        self.__reg_rxest_dump_filter0_ena_msb = 20
        self.__reg_rxest_dump_filter1_ena_lsb = 19
        self.__reg_rxest_dump_filter1_ena_msb = 19
        self.__reg_rxest_dump_filter2_ena_lsb = 18
        self.__reg_rxest_dump_filter2_ena_msb = 18
        self.__reg_rxest_dump_filter3_ena_lsb = 17
        self.__reg_rxest_dump_filter3_ena_msb = 17
        self.__reg_rxest_dump_filter4_ena_lsb = 16
        self.__reg_rxest_dump_filter4_ena_msb = 16
        self.__reg_rxest_dump_filter5_ena_lsb = 15
        self.__reg_rxest_dump_filter5_ena_msb = 15
        self.__reg_rxest_dump_filter6_ena_lsb = 14
        self.__reg_rxest_dump_filter6_ena_msb = 14
        self.__reg_lastbuf_dump_filter0_op_lsb = 13
        self.__reg_lastbuf_dump_filter0_op_msb = 13
        self.__reg_lastbuf_dump_filter1_op_lsb = 12
        self.__reg_lastbuf_dump_filter1_op_msb = 12
        self.__reg_lastbuf_dump_filter2_op_lsb = 11
        self.__reg_lastbuf_dump_filter2_op_msb = 11
        self.__reg_lastbuf_dump_filter3_op_lsb = 10
        self.__reg_lastbuf_dump_filter3_op_msb = 10
        self.__reg_lastbuf_dump_filter4_op_lsb = 9
        self.__reg_lastbuf_dump_filter4_op_msb = 9
        self.__reg_lastbuf_dump_filter5_op_lsb = 8
        self.__reg_lastbuf_dump_filter5_op_msb = 8
        self.__reg_lastbuf_dump_filter6_op_lsb = 7
        self.__reg_lastbuf_dump_filter6_op_msb = 7
        self.__reg_lastbuf_dump_filter0_ena_lsb = 6
        self.__reg_lastbuf_dump_filter0_ena_msb = 6
        self.__reg_lastbuf_dump_filter1_ena_lsb = 5
        self.__reg_lastbuf_dump_filter1_ena_msb = 5
        self.__reg_lastbuf_dump_filter2_ena_lsb = 4
        self.__reg_lastbuf_dump_filter2_ena_msb = 4
        self.__reg_lastbuf_dump_filter3_ena_lsb = 3
        self.__reg_lastbuf_dump_filter3_ena_msb = 3
        self.__reg_lastbuf_dump_filter4_ena_lsb = 2
        self.__reg_lastbuf_dump_filter4_ena_msb = 2
        self.__reg_lastbuf_dump_filter5_ena_lsb = 1
        self.__reg_lastbuf_dump_filter5_ena_msb = 1
        self.__reg_lastbuf_dump_filter6_ena_lsb = 0
        self.__reg_lastbuf_dump_filter6_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxest_dump_filter0_op(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxest_dump_filter0_op_msb, self.__reg_rxest_dump_filter0_op_lsb)
    @reg_rxest_dump_filter0_op.setter
    def reg_rxest_dump_filter0_op(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxest_dump_filter0_op_msb, self.__reg_rxest_dump_filter0_op_lsb, value)

    @property
    def reg_rxest_dump_filter1_op(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxest_dump_filter1_op_msb, self.__reg_rxest_dump_filter1_op_lsb)
    @reg_rxest_dump_filter1_op.setter
    def reg_rxest_dump_filter1_op(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxest_dump_filter1_op_msb, self.__reg_rxest_dump_filter1_op_lsb, value)

    @property
    def reg_rxest_dump_filter2_op(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxest_dump_filter2_op_msb, self.__reg_rxest_dump_filter2_op_lsb)
    @reg_rxest_dump_filter2_op.setter
    def reg_rxest_dump_filter2_op(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxest_dump_filter2_op_msb, self.__reg_rxest_dump_filter2_op_lsb, value)

    @property
    def reg_rxest_dump_filter3_op(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxest_dump_filter3_op_msb, self.__reg_rxest_dump_filter3_op_lsb)
    @reg_rxest_dump_filter3_op.setter
    def reg_rxest_dump_filter3_op(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxest_dump_filter3_op_msb, self.__reg_rxest_dump_filter3_op_lsb, value)

    @property
    def reg_rxest_dump_filter4_op(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxest_dump_filter4_op_msb, self.__reg_rxest_dump_filter4_op_lsb)
    @reg_rxest_dump_filter4_op.setter
    def reg_rxest_dump_filter4_op(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxest_dump_filter4_op_msb, self.__reg_rxest_dump_filter4_op_lsb, value)

    @property
    def reg_rxest_dump_filter5_op(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxest_dump_filter5_op_msb, self.__reg_rxest_dump_filter5_op_lsb)
    @reg_rxest_dump_filter5_op.setter
    def reg_rxest_dump_filter5_op(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxest_dump_filter5_op_msb, self.__reg_rxest_dump_filter5_op_lsb, value)

    @property
    def reg_rxest_dump_filter6_op(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxest_dump_filter6_op_msb, self.__reg_rxest_dump_filter6_op_lsb)
    @reg_rxest_dump_filter6_op.setter
    def reg_rxest_dump_filter6_op(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxest_dump_filter6_op_msb, self.__reg_rxest_dump_filter6_op_lsb, value)

    @property
    def reg_rxest_dump_filter0_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxest_dump_filter0_ena_msb, self.__reg_rxest_dump_filter0_ena_lsb)
    @reg_rxest_dump_filter0_ena.setter
    def reg_rxest_dump_filter0_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxest_dump_filter0_ena_msb, self.__reg_rxest_dump_filter0_ena_lsb, value)

    @property
    def reg_rxest_dump_filter1_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxest_dump_filter1_ena_msb, self.__reg_rxest_dump_filter1_ena_lsb)
    @reg_rxest_dump_filter1_ena.setter
    def reg_rxest_dump_filter1_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxest_dump_filter1_ena_msb, self.__reg_rxest_dump_filter1_ena_lsb, value)

    @property
    def reg_rxest_dump_filter2_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxest_dump_filter2_ena_msb, self.__reg_rxest_dump_filter2_ena_lsb)
    @reg_rxest_dump_filter2_ena.setter
    def reg_rxest_dump_filter2_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxest_dump_filter2_ena_msb, self.__reg_rxest_dump_filter2_ena_lsb, value)

    @property
    def reg_rxest_dump_filter3_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxest_dump_filter3_ena_msb, self.__reg_rxest_dump_filter3_ena_lsb)
    @reg_rxest_dump_filter3_ena.setter
    def reg_rxest_dump_filter3_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxest_dump_filter3_ena_msb, self.__reg_rxest_dump_filter3_ena_lsb, value)

    @property
    def reg_rxest_dump_filter4_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxest_dump_filter4_ena_msb, self.__reg_rxest_dump_filter4_ena_lsb)
    @reg_rxest_dump_filter4_ena.setter
    def reg_rxest_dump_filter4_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxest_dump_filter4_ena_msb, self.__reg_rxest_dump_filter4_ena_lsb, value)

    @property
    def reg_rxest_dump_filter5_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxest_dump_filter5_ena_msb, self.__reg_rxest_dump_filter5_ena_lsb)
    @reg_rxest_dump_filter5_ena.setter
    def reg_rxest_dump_filter5_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxest_dump_filter5_ena_msb, self.__reg_rxest_dump_filter5_ena_lsb, value)

    @property
    def reg_rxest_dump_filter6_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxest_dump_filter6_ena_msb, self.__reg_rxest_dump_filter6_ena_lsb)
    @reg_rxest_dump_filter6_ena.setter
    def reg_rxest_dump_filter6_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxest_dump_filter6_ena_msb, self.__reg_rxest_dump_filter6_ena_lsb, value)

    @property
    def reg_lastbuf_dump_filter0_op(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lastbuf_dump_filter0_op_msb, self.__reg_lastbuf_dump_filter0_op_lsb)
    @reg_lastbuf_dump_filter0_op.setter
    def reg_lastbuf_dump_filter0_op(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lastbuf_dump_filter0_op_msb, self.__reg_lastbuf_dump_filter0_op_lsb, value)

    @property
    def reg_lastbuf_dump_filter1_op(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lastbuf_dump_filter1_op_msb, self.__reg_lastbuf_dump_filter1_op_lsb)
    @reg_lastbuf_dump_filter1_op.setter
    def reg_lastbuf_dump_filter1_op(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lastbuf_dump_filter1_op_msb, self.__reg_lastbuf_dump_filter1_op_lsb, value)

    @property
    def reg_lastbuf_dump_filter2_op(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lastbuf_dump_filter2_op_msb, self.__reg_lastbuf_dump_filter2_op_lsb)
    @reg_lastbuf_dump_filter2_op.setter
    def reg_lastbuf_dump_filter2_op(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lastbuf_dump_filter2_op_msb, self.__reg_lastbuf_dump_filter2_op_lsb, value)

    @property
    def reg_lastbuf_dump_filter3_op(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lastbuf_dump_filter3_op_msb, self.__reg_lastbuf_dump_filter3_op_lsb)
    @reg_lastbuf_dump_filter3_op.setter
    def reg_lastbuf_dump_filter3_op(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lastbuf_dump_filter3_op_msb, self.__reg_lastbuf_dump_filter3_op_lsb, value)

    @property
    def reg_lastbuf_dump_filter4_op(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lastbuf_dump_filter4_op_msb, self.__reg_lastbuf_dump_filter4_op_lsb)
    @reg_lastbuf_dump_filter4_op.setter
    def reg_lastbuf_dump_filter4_op(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lastbuf_dump_filter4_op_msb, self.__reg_lastbuf_dump_filter4_op_lsb, value)

    @property
    def reg_lastbuf_dump_filter5_op(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lastbuf_dump_filter5_op_msb, self.__reg_lastbuf_dump_filter5_op_lsb)
    @reg_lastbuf_dump_filter5_op.setter
    def reg_lastbuf_dump_filter5_op(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lastbuf_dump_filter5_op_msb, self.__reg_lastbuf_dump_filter5_op_lsb, value)

    @property
    def reg_lastbuf_dump_filter6_op(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lastbuf_dump_filter6_op_msb, self.__reg_lastbuf_dump_filter6_op_lsb)
    @reg_lastbuf_dump_filter6_op.setter
    def reg_lastbuf_dump_filter6_op(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lastbuf_dump_filter6_op_msb, self.__reg_lastbuf_dump_filter6_op_lsb, value)

    @property
    def reg_lastbuf_dump_filter0_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lastbuf_dump_filter0_ena_msb, self.__reg_lastbuf_dump_filter0_ena_lsb)
    @reg_lastbuf_dump_filter0_ena.setter
    def reg_lastbuf_dump_filter0_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lastbuf_dump_filter0_ena_msb, self.__reg_lastbuf_dump_filter0_ena_lsb, value)

    @property
    def reg_lastbuf_dump_filter1_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lastbuf_dump_filter1_ena_msb, self.__reg_lastbuf_dump_filter1_ena_lsb)
    @reg_lastbuf_dump_filter1_ena.setter
    def reg_lastbuf_dump_filter1_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lastbuf_dump_filter1_ena_msb, self.__reg_lastbuf_dump_filter1_ena_lsb, value)

    @property
    def reg_lastbuf_dump_filter2_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lastbuf_dump_filter2_ena_msb, self.__reg_lastbuf_dump_filter2_ena_lsb)
    @reg_lastbuf_dump_filter2_ena.setter
    def reg_lastbuf_dump_filter2_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lastbuf_dump_filter2_ena_msb, self.__reg_lastbuf_dump_filter2_ena_lsb, value)

    @property
    def reg_lastbuf_dump_filter3_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lastbuf_dump_filter3_ena_msb, self.__reg_lastbuf_dump_filter3_ena_lsb)
    @reg_lastbuf_dump_filter3_ena.setter
    def reg_lastbuf_dump_filter3_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lastbuf_dump_filter3_ena_msb, self.__reg_lastbuf_dump_filter3_ena_lsb, value)

    @property
    def reg_lastbuf_dump_filter4_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lastbuf_dump_filter4_ena_msb, self.__reg_lastbuf_dump_filter4_ena_lsb)
    @reg_lastbuf_dump_filter4_ena.setter
    def reg_lastbuf_dump_filter4_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lastbuf_dump_filter4_ena_msb, self.__reg_lastbuf_dump_filter4_ena_lsb, value)

    @property
    def reg_lastbuf_dump_filter5_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lastbuf_dump_filter5_ena_msb, self.__reg_lastbuf_dump_filter5_ena_lsb)
    @reg_lastbuf_dump_filter5_ena.setter
    def reg_lastbuf_dump_filter5_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lastbuf_dump_filter5_ena_msb, self.__reg_lastbuf_dump_filter5_ena_lsb, value)

    @property
    def reg_lastbuf_dump_filter6_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lastbuf_dump_filter6_ena_msb, self.__reg_lastbuf_dump_filter6_ena_lsb)
    @reg_lastbuf_dump_filter6_ena.setter
    def reg_lastbuf_dump_filter6_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lastbuf_dump_filter6_ena_msb, self.__reg_lastbuf_dump_filter6_ena_lsb, value)
class MACRX_DATA_DUMP_CONF1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x15c
        self.__reg_txacktimer_dump_filter0_op_lsb = 13
        self.__reg_txacktimer_dump_filter0_op_msb = 13
        self.__reg_txacktimer_dump_filter1_op_lsb = 12
        self.__reg_txacktimer_dump_filter1_op_msb = 12
        self.__reg_txacktimer_dump_filter2_op_lsb = 11
        self.__reg_txacktimer_dump_filter2_op_msb = 11
        self.__reg_txacktimer_dump_filter3_op_lsb = 10
        self.__reg_txacktimer_dump_filter3_op_msb = 10
        self.__reg_txacktimer_dump_filter4_op_lsb = 9
        self.__reg_txacktimer_dump_filter4_op_msb = 9
        self.__reg_txacktimer_dump_filter5_op_lsb = 8
        self.__reg_txacktimer_dump_filter5_op_msb = 8
        self.__reg_txacktimer_dump_filter6_op_lsb = 7
        self.__reg_txacktimer_dump_filter6_op_msb = 7
        self.__reg_txacktimer_dump_filter0_ena_lsb = 6
        self.__reg_txacktimer_dump_filter0_ena_msb = 6
        self.__reg_txacktimer_dump_filter1_ena_lsb = 5
        self.__reg_txacktimer_dump_filter1_ena_msb = 5
        self.__reg_txacktimer_dump_filter2_ena_lsb = 4
        self.__reg_txacktimer_dump_filter2_ena_msb = 4
        self.__reg_txacktimer_dump_filter3_ena_lsb = 3
        self.__reg_txacktimer_dump_filter3_ena_msb = 3
        self.__reg_txacktimer_dump_filter4_ena_lsb = 2
        self.__reg_txacktimer_dump_filter4_ena_msb = 2
        self.__reg_txacktimer_dump_filter5_ena_lsb = 1
        self.__reg_txacktimer_dump_filter5_ena_msb = 1
        self.__reg_txacktimer_dump_filter6_ena_lsb = 0
        self.__reg_txacktimer_dump_filter6_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txacktimer_dump_filter0_op(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txacktimer_dump_filter0_op_msb, self.__reg_txacktimer_dump_filter0_op_lsb)
    @reg_txacktimer_dump_filter0_op.setter
    def reg_txacktimer_dump_filter0_op(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txacktimer_dump_filter0_op_msb, self.__reg_txacktimer_dump_filter0_op_lsb, value)

    @property
    def reg_txacktimer_dump_filter1_op(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txacktimer_dump_filter1_op_msb, self.__reg_txacktimer_dump_filter1_op_lsb)
    @reg_txacktimer_dump_filter1_op.setter
    def reg_txacktimer_dump_filter1_op(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txacktimer_dump_filter1_op_msb, self.__reg_txacktimer_dump_filter1_op_lsb, value)

    @property
    def reg_txacktimer_dump_filter2_op(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txacktimer_dump_filter2_op_msb, self.__reg_txacktimer_dump_filter2_op_lsb)
    @reg_txacktimer_dump_filter2_op.setter
    def reg_txacktimer_dump_filter2_op(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txacktimer_dump_filter2_op_msb, self.__reg_txacktimer_dump_filter2_op_lsb, value)

    @property
    def reg_txacktimer_dump_filter3_op(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txacktimer_dump_filter3_op_msb, self.__reg_txacktimer_dump_filter3_op_lsb)
    @reg_txacktimer_dump_filter3_op.setter
    def reg_txacktimer_dump_filter3_op(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txacktimer_dump_filter3_op_msb, self.__reg_txacktimer_dump_filter3_op_lsb, value)

    @property
    def reg_txacktimer_dump_filter4_op(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txacktimer_dump_filter4_op_msb, self.__reg_txacktimer_dump_filter4_op_lsb)
    @reg_txacktimer_dump_filter4_op.setter
    def reg_txacktimer_dump_filter4_op(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txacktimer_dump_filter4_op_msb, self.__reg_txacktimer_dump_filter4_op_lsb, value)

    @property
    def reg_txacktimer_dump_filter5_op(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txacktimer_dump_filter5_op_msb, self.__reg_txacktimer_dump_filter5_op_lsb)
    @reg_txacktimer_dump_filter5_op.setter
    def reg_txacktimer_dump_filter5_op(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txacktimer_dump_filter5_op_msb, self.__reg_txacktimer_dump_filter5_op_lsb, value)

    @property
    def reg_txacktimer_dump_filter6_op(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txacktimer_dump_filter6_op_msb, self.__reg_txacktimer_dump_filter6_op_lsb)
    @reg_txacktimer_dump_filter6_op.setter
    def reg_txacktimer_dump_filter6_op(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txacktimer_dump_filter6_op_msb, self.__reg_txacktimer_dump_filter6_op_lsb, value)

    @property
    def reg_txacktimer_dump_filter0_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txacktimer_dump_filter0_ena_msb, self.__reg_txacktimer_dump_filter0_ena_lsb)
    @reg_txacktimer_dump_filter0_ena.setter
    def reg_txacktimer_dump_filter0_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txacktimer_dump_filter0_ena_msb, self.__reg_txacktimer_dump_filter0_ena_lsb, value)

    @property
    def reg_txacktimer_dump_filter1_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txacktimer_dump_filter1_ena_msb, self.__reg_txacktimer_dump_filter1_ena_lsb)
    @reg_txacktimer_dump_filter1_ena.setter
    def reg_txacktimer_dump_filter1_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txacktimer_dump_filter1_ena_msb, self.__reg_txacktimer_dump_filter1_ena_lsb, value)

    @property
    def reg_txacktimer_dump_filter2_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txacktimer_dump_filter2_ena_msb, self.__reg_txacktimer_dump_filter2_ena_lsb)
    @reg_txacktimer_dump_filter2_ena.setter
    def reg_txacktimer_dump_filter2_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txacktimer_dump_filter2_ena_msb, self.__reg_txacktimer_dump_filter2_ena_lsb, value)

    @property
    def reg_txacktimer_dump_filter3_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txacktimer_dump_filter3_ena_msb, self.__reg_txacktimer_dump_filter3_ena_lsb)
    @reg_txacktimer_dump_filter3_ena.setter
    def reg_txacktimer_dump_filter3_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txacktimer_dump_filter3_ena_msb, self.__reg_txacktimer_dump_filter3_ena_lsb, value)

    @property
    def reg_txacktimer_dump_filter4_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txacktimer_dump_filter4_ena_msb, self.__reg_txacktimer_dump_filter4_ena_lsb)
    @reg_txacktimer_dump_filter4_ena.setter
    def reg_txacktimer_dump_filter4_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txacktimer_dump_filter4_ena_msb, self.__reg_txacktimer_dump_filter4_ena_lsb, value)

    @property
    def reg_txacktimer_dump_filter5_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txacktimer_dump_filter5_ena_msb, self.__reg_txacktimer_dump_filter5_ena_lsb)
    @reg_txacktimer_dump_filter5_ena.setter
    def reg_txacktimer_dump_filter5_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txacktimer_dump_filter5_ena_msb, self.__reg_txacktimer_dump_filter5_ena_lsb, value)

    @property
    def reg_txacktimer_dump_filter6_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txacktimer_dump_filter6_ena_msb, self.__reg_txacktimer_dump_filter6_ena_lsb)
    @reg_txacktimer_dump_filter6_ena.setter
    def reg_txacktimer_dump_filter6_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txacktimer_dump_filter6_ena_msb, self.__reg_txacktimer_dump_filter6_ena_lsb, value)
class MACRX_DATA_FILTER0_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x160
        self.__reg_rxdata_filter0_frbody_lsb = 17
        self.__reg_rxdata_filter0_frbody_msb = 17
        self.__reg_rxdata_filter0_frplcp_lsb = 16
        self.__reg_rxdata_filter0_frplcp_msb = 16
        self.__reg_rxdata_filter0_bssid_lsb = 12
        self.__reg_rxdata_filter0_bssid_msb = 15
        self.__reg_rxdata_filter0_offset_lsb = 0
        self.__reg_rxdata_filter0_offset_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxdata_filter0_frbody(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter0_frbody_msb, self.__reg_rxdata_filter0_frbody_lsb)
    @reg_rxdata_filter0_frbody.setter
    def reg_rxdata_filter0_frbody(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter0_frbody_msb, self.__reg_rxdata_filter0_frbody_lsb, value)

    @property
    def reg_rxdata_filter0_frplcp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter0_frplcp_msb, self.__reg_rxdata_filter0_frplcp_lsb)
    @reg_rxdata_filter0_frplcp.setter
    def reg_rxdata_filter0_frplcp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter0_frplcp_msb, self.__reg_rxdata_filter0_frplcp_lsb, value)

    @property
    def reg_rxdata_filter0_bssid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter0_bssid_msb, self.__reg_rxdata_filter0_bssid_lsb)
    @reg_rxdata_filter0_bssid.setter
    def reg_rxdata_filter0_bssid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter0_bssid_msb, self.__reg_rxdata_filter0_bssid_lsb, value)

    @property
    def reg_rxdata_filter0_offset(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter0_offset_msb, self.__reg_rxdata_filter0_offset_lsb)
    @reg_rxdata_filter0_offset.setter
    def reg_rxdata_filter0_offset(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter0_offset_msb, self.__reg_rxdata_filter0_offset_lsb, value)
class MACRX_DATA_FILTER1_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x164
        self.__reg_rxdata_filter1_frbody_lsb = 17
        self.__reg_rxdata_filter1_frbody_msb = 17
        self.__reg_rxdata_filter1_frplcp_lsb = 16
        self.__reg_rxdata_filter1_frplcp_msb = 16
        self.__reg_rxdata_filter1_bssid_lsb = 12
        self.__reg_rxdata_filter1_bssid_msb = 15
        self.__reg_rxdata_filter1_offset_lsb = 0
        self.__reg_rxdata_filter1_offset_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxdata_filter1_frbody(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter1_frbody_msb, self.__reg_rxdata_filter1_frbody_lsb)
    @reg_rxdata_filter1_frbody.setter
    def reg_rxdata_filter1_frbody(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter1_frbody_msb, self.__reg_rxdata_filter1_frbody_lsb, value)

    @property
    def reg_rxdata_filter1_frplcp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter1_frplcp_msb, self.__reg_rxdata_filter1_frplcp_lsb)
    @reg_rxdata_filter1_frplcp.setter
    def reg_rxdata_filter1_frplcp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter1_frplcp_msb, self.__reg_rxdata_filter1_frplcp_lsb, value)

    @property
    def reg_rxdata_filter1_bssid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter1_bssid_msb, self.__reg_rxdata_filter1_bssid_lsb)
    @reg_rxdata_filter1_bssid.setter
    def reg_rxdata_filter1_bssid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter1_bssid_msb, self.__reg_rxdata_filter1_bssid_lsb, value)

    @property
    def reg_rxdata_filter1_offset(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter1_offset_msb, self.__reg_rxdata_filter1_offset_lsb)
    @reg_rxdata_filter1_offset.setter
    def reg_rxdata_filter1_offset(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter1_offset_msb, self.__reg_rxdata_filter1_offset_lsb, value)
class MACRX_DATA_FILTER2_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x168
        self.__reg_rxdata_filter2_frbody_lsb = 17
        self.__reg_rxdata_filter2_frbody_msb = 17
        self.__reg_rxdata_filter2_frplcp_lsb = 16
        self.__reg_rxdata_filter2_frplcp_msb = 16
        self.__reg_rxdata_filter2_bssid_lsb = 12
        self.__reg_rxdata_filter2_bssid_msb = 15
        self.__reg_rxdata_filter2_offset_lsb = 0
        self.__reg_rxdata_filter2_offset_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxdata_filter2_frbody(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter2_frbody_msb, self.__reg_rxdata_filter2_frbody_lsb)
    @reg_rxdata_filter2_frbody.setter
    def reg_rxdata_filter2_frbody(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter2_frbody_msb, self.__reg_rxdata_filter2_frbody_lsb, value)

    @property
    def reg_rxdata_filter2_frplcp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter2_frplcp_msb, self.__reg_rxdata_filter2_frplcp_lsb)
    @reg_rxdata_filter2_frplcp.setter
    def reg_rxdata_filter2_frplcp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter2_frplcp_msb, self.__reg_rxdata_filter2_frplcp_lsb, value)

    @property
    def reg_rxdata_filter2_bssid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter2_bssid_msb, self.__reg_rxdata_filter2_bssid_lsb)
    @reg_rxdata_filter2_bssid.setter
    def reg_rxdata_filter2_bssid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter2_bssid_msb, self.__reg_rxdata_filter2_bssid_lsb, value)

    @property
    def reg_rxdata_filter2_offset(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter2_offset_msb, self.__reg_rxdata_filter2_offset_lsb)
    @reg_rxdata_filter2_offset.setter
    def reg_rxdata_filter2_offset(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter2_offset_msb, self.__reg_rxdata_filter2_offset_lsb, value)
class MACRX_DATA_FILTER3_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x16c
        self.__reg_rxdata_filter3_frbody_lsb = 17
        self.__reg_rxdata_filter3_frbody_msb = 17
        self.__reg_rxdata_filter3_frplcp_lsb = 16
        self.__reg_rxdata_filter3_frplcp_msb = 16
        self.__reg_rxdata_filter3_bssid_lsb = 12
        self.__reg_rxdata_filter3_bssid_msb = 15
        self.__reg_rxdata_filter3_offset_lsb = 0
        self.__reg_rxdata_filter3_offset_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxdata_filter3_frbody(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter3_frbody_msb, self.__reg_rxdata_filter3_frbody_lsb)
    @reg_rxdata_filter3_frbody.setter
    def reg_rxdata_filter3_frbody(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter3_frbody_msb, self.__reg_rxdata_filter3_frbody_lsb, value)

    @property
    def reg_rxdata_filter3_frplcp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter3_frplcp_msb, self.__reg_rxdata_filter3_frplcp_lsb)
    @reg_rxdata_filter3_frplcp.setter
    def reg_rxdata_filter3_frplcp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter3_frplcp_msb, self.__reg_rxdata_filter3_frplcp_lsb, value)

    @property
    def reg_rxdata_filter3_bssid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter3_bssid_msb, self.__reg_rxdata_filter3_bssid_lsb)
    @reg_rxdata_filter3_bssid.setter
    def reg_rxdata_filter3_bssid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter3_bssid_msb, self.__reg_rxdata_filter3_bssid_lsb, value)

    @property
    def reg_rxdata_filter3_offset(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter3_offset_msb, self.__reg_rxdata_filter3_offset_lsb)
    @reg_rxdata_filter3_offset.setter
    def reg_rxdata_filter3_offset(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter3_offset_msb, self.__reg_rxdata_filter3_offset_lsb, value)
class MACRX_DATA_FILTER4_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x170
        self.__reg_rxdata_filter4_frbody_lsb = 17
        self.__reg_rxdata_filter4_frbody_msb = 17
        self.__reg_rxdata_filter4_frplcp_lsb = 16
        self.__reg_rxdata_filter4_frplcp_msb = 16
        self.__reg_rxdata_filter4_bssid_lsb = 12
        self.__reg_rxdata_filter4_bssid_msb = 15
        self.__reg_rxdata_filter4_offset_lsb = 0
        self.__reg_rxdata_filter4_offset_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxdata_filter4_frbody(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter4_frbody_msb, self.__reg_rxdata_filter4_frbody_lsb)
    @reg_rxdata_filter4_frbody.setter
    def reg_rxdata_filter4_frbody(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter4_frbody_msb, self.__reg_rxdata_filter4_frbody_lsb, value)

    @property
    def reg_rxdata_filter4_frplcp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter4_frplcp_msb, self.__reg_rxdata_filter4_frplcp_lsb)
    @reg_rxdata_filter4_frplcp.setter
    def reg_rxdata_filter4_frplcp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter4_frplcp_msb, self.__reg_rxdata_filter4_frplcp_lsb, value)

    @property
    def reg_rxdata_filter4_bssid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter4_bssid_msb, self.__reg_rxdata_filter4_bssid_lsb)
    @reg_rxdata_filter4_bssid.setter
    def reg_rxdata_filter4_bssid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter4_bssid_msb, self.__reg_rxdata_filter4_bssid_lsb, value)

    @property
    def reg_rxdata_filter4_offset(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter4_offset_msb, self.__reg_rxdata_filter4_offset_lsb)
    @reg_rxdata_filter4_offset.setter
    def reg_rxdata_filter4_offset(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter4_offset_msb, self.__reg_rxdata_filter4_offset_lsb, value)
class MACRX_DATA_FILTER5_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x174
        self.__reg_rxdata_filter5_frbody_lsb = 17
        self.__reg_rxdata_filter5_frbody_msb = 17
        self.__reg_rxdata_filter5_frplcp_lsb = 16
        self.__reg_rxdata_filter5_frplcp_msb = 16
        self.__reg_rxdata_filter5_bssid_lsb = 12
        self.__reg_rxdata_filter5_bssid_msb = 15
        self.__reg_rxdata_filter5_offset_lsb = 0
        self.__reg_rxdata_filter5_offset_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxdata_filter5_frbody(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter5_frbody_msb, self.__reg_rxdata_filter5_frbody_lsb)
    @reg_rxdata_filter5_frbody.setter
    def reg_rxdata_filter5_frbody(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter5_frbody_msb, self.__reg_rxdata_filter5_frbody_lsb, value)

    @property
    def reg_rxdata_filter5_frplcp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter5_frplcp_msb, self.__reg_rxdata_filter5_frplcp_lsb)
    @reg_rxdata_filter5_frplcp.setter
    def reg_rxdata_filter5_frplcp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter5_frplcp_msb, self.__reg_rxdata_filter5_frplcp_lsb, value)

    @property
    def reg_rxdata_filter5_bssid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter5_bssid_msb, self.__reg_rxdata_filter5_bssid_lsb)
    @reg_rxdata_filter5_bssid.setter
    def reg_rxdata_filter5_bssid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter5_bssid_msb, self.__reg_rxdata_filter5_bssid_lsb, value)

    @property
    def reg_rxdata_filter5_offset(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter5_offset_msb, self.__reg_rxdata_filter5_offset_lsb)
    @reg_rxdata_filter5_offset.setter
    def reg_rxdata_filter5_offset(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter5_offset_msb, self.__reg_rxdata_filter5_offset_lsb, value)
class MACRX_DATA_FILTER6_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x178
        self.__reg_rxdata_filter6_frbody_lsb = 17
        self.__reg_rxdata_filter6_frbody_msb = 17
        self.__reg_rxdata_filter6_frplcp_lsb = 16
        self.__reg_rxdata_filter6_frplcp_msb = 16
        self.__reg_rxdata_filter6_bssid_lsb = 12
        self.__reg_rxdata_filter6_bssid_msb = 15
        self.__reg_rxdata_filter6_offset_lsb = 0
        self.__reg_rxdata_filter6_offset_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxdata_filter6_frbody(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter6_frbody_msb, self.__reg_rxdata_filter6_frbody_lsb)
    @reg_rxdata_filter6_frbody.setter
    def reg_rxdata_filter6_frbody(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter6_frbody_msb, self.__reg_rxdata_filter6_frbody_lsb, value)

    @property
    def reg_rxdata_filter6_frplcp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter6_frplcp_msb, self.__reg_rxdata_filter6_frplcp_lsb)
    @reg_rxdata_filter6_frplcp.setter
    def reg_rxdata_filter6_frplcp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter6_frplcp_msb, self.__reg_rxdata_filter6_frplcp_lsb, value)

    @property
    def reg_rxdata_filter6_bssid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter6_bssid_msb, self.__reg_rxdata_filter6_bssid_lsb)
    @reg_rxdata_filter6_bssid.setter
    def reg_rxdata_filter6_bssid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter6_bssid_msb, self.__reg_rxdata_filter6_bssid_lsb, value)

    @property
    def reg_rxdata_filter6_offset(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter6_offset_msb, self.__reg_rxdata_filter6_offset_lsb)
    @reg_rxdata_filter6_offset.setter
    def reg_rxdata_filter6_offset(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter6_offset_msb, self.__reg_rxdata_filter6_offset_lsb, value)
class MACRX_DATA_FILTER0_DATA(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x17c
        self.__reg_rxdata_filter0_data_lsb = 0
        self.__reg_rxdata_filter0_data_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxdata_filter0_data(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter0_data_msb, self.__reg_rxdata_filter0_data_lsb)
    @reg_rxdata_filter0_data.setter
    def reg_rxdata_filter0_data(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter0_data_msb, self.__reg_rxdata_filter0_data_lsb, value)
class MACRX_DATA_FILTER1_DATA(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x180
        self.__reg_rxdata_filter1_data_lsb = 0
        self.__reg_rxdata_filter1_data_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxdata_filter1_data(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter1_data_msb, self.__reg_rxdata_filter1_data_lsb)
    @reg_rxdata_filter1_data.setter
    def reg_rxdata_filter1_data(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter1_data_msb, self.__reg_rxdata_filter1_data_lsb, value)
class MACRX_DATA_FILTER2_DATA(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x184
        self.__reg_rxdata_filter2_data_lsb = 0
        self.__reg_rxdata_filter2_data_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxdata_filter2_data(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter2_data_msb, self.__reg_rxdata_filter2_data_lsb)
    @reg_rxdata_filter2_data.setter
    def reg_rxdata_filter2_data(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter2_data_msb, self.__reg_rxdata_filter2_data_lsb, value)
class MACRX_DATA_FILTER3_DATA(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x188
        self.__reg_rxdata_filter3_data_lsb = 0
        self.__reg_rxdata_filter3_data_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxdata_filter3_data(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter3_data_msb, self.__reg_rxdata_filter3_data_lsb)
    @reg_rxdata_filter3_data.setter
    def reg_rxdata_filter3_data(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter3_data_msb, self.__reg_rxdata_filter3_data_lsb, value)
class MACRX_DATA_FILTER4_DATA(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x18c
        self.__reg_rxdata_filter4_data_lsb = 0
        self.__reg_rxdata_filter4_data_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxdata_filter4_data(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter4_data_msb, self.__reg_rxdata_filter4_data_lsb)
    @reg_rxdata_filter4_data.setter
    def reg_rxdata_filter4_data(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter4_data_msb, self.__reg_rxdata_filter4_data_lsb, value)
class MACRX_DATA_FILTER5_DATA(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x190
        self.__reg_rxdata_filter5_data_lsb = 0
        self.__reg_rxdata_filter5_data_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxdata_filter5_data(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter5_data_msb, self.__reg_rxdata_filter5_data_lsb)
    @reg_rxdata_filter5_data.setter
    def reg_rxdata_filter5_data(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter5_data_msb, self.__reg_rxdata_filter5_data_lsb, value)
class MACRX_DATA_FILTER6_DATA(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x194
        self.__reg_rxdata_filter6_data_lsb = 0
        self.__reg_rxdata_filter6_data_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxdata_filter6_data(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter6_data_msb, self.__reg_rxdata_filter6_data_lsb)
    @reg_rxdata_filter6_data.setter
    def reg_rxdata_filter6_data(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter6_data_msb, self.__reg_rxdata_filter6_data_lsb, value)
class MACRX_DATA_FILTER0_MASK(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x198
        self.__reg_rxdata_filter0_mask_lsb = 0
        self.__reg_rxdata_filter0_mask_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxdata_filter0_mask(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter0_mask_msb, self.__reg_rxdata_filter0_mask_lsb)
    @reg_rxdata_filter0_mask.setter
    def reg_rxdata_filter0_mask(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter0_mask_msb, self.__reg_rxdata_filter0_mask_lsb, value)
class MACRX_DATA_FILTER1_MASK(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x19c
        self.__reg_rxdata_filter1_mask_lsb = 0
        self.__reg_rxdata_filter1_mask_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxdata_filter1_mask(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter1_mask_msb, self.__reg_rxdata_filter1_mask_lsb)
    @reg_rxdata_filter1_mask.setter
    def reg_rxdata_filter1_mask(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter1_mask_msb, self.__reg_rxdata_filter1_mask_lsb, value)
class MACRX_DATA_FILTER2_MASK(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x1a0
        self.__reg_rxdata_filter2_mask_lsb = 0
        self.__reg_rxdata_filter2_mask_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxdata_filter2_mask(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter2_mask_msb, self.__reg_rxdata_filter2_mask_lsb)
    @reg_rxdata_filter2_mask.setter
    def reg_rxdata_filter2_mask(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter2_mask_msb, self.__reg_rxdata_filter2_mask_lsb, value)
class MACRX_DATA_FILTER3_MASK(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x1a4
        self.__reg_rxdata_filter3_mask_lsb = 0
        self.__reg_rxdata_filter3_mask_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxdata_filter3_mask(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter3_mask_msb, self.__reg_rxdata_filter3_mask_lsb)
    @reg_rxdata_filter3_mask.setter
    def reg_rxdata_filter3_mask(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter3_mask_msb, self.__reg_rxdata_filter3_mask_lsb, value)
class MACRX_DATA_FILTER4_MASK(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x1a8
        self.__reg_rxdata_filter4_mask_lsb = 0
        self.__reg_rxdata_filter4_mask_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxdata_filter4_mask(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter4_mask_msb, self.__reg_rxdata_filter4_mask_lsb)
    @reg_rxdata_filter4_mask.setter
    def reg_rxdata_filter4_mask(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter4_mask_msb, self.__reg_rxdata_filter4_mask_lsb, value)
class MACRX_DATA_FILTER5_MASK(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x1ac
        self.__reg_rxdata_filter5_mask_lsb = 0
        self.__reg_rxdata_filter5_mask_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxdata_filter5_mask(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter5_mask_msb, self.__reg_rxdata_filter5_mask_lsb)
    @reg_rxdata_filter5_mask.setter
    def reg_rxdata_filter5_mask(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter5_mask_msb, self.__reg_rxdata_filter5_mask_lsb, value)
class MACRX_DATA_FILTER6_MASK(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x1b0
        self.__reg_rxdata_filter6_mask_lsb = 0
        self.__reg_rxdata_filter6_mask_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxdata_filter6_mask(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdata_filter6_mask_msb, self.__reg_rxdata_filter6_mask_lsb)
    @reg_rxdata_filter6_mask.setter
    def reg_rxdata_filter6_mask(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdata_filter6_mask_msb, self.__reg_rxdata_filter6_mask_lsb, value)
class MACRXBA7_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x1b4
        self.__reg_rxba7_ena_lsb = 31
        self.__reg_rxba7_ena_msb = 31
        self.__reg_rxba7_imr_lsb = 30
        self.__reg_rxba7_imr_msb = 30
        self.__reg_rxba7_tid_lsb = 12
        self.__reg_rxba7_tid_msb = 15
        self.__reg_rxba7_compbm_lsb = 2
        self.__reg_rxba7_compbm_msb = 2
        self.__reg_rxba7_multitid_lsb = 1
        self.__reg_rxba7_multitid_msb = 1
        self.__reg_rxba7_ackpolicy_lsb = 0
        self.__reg_rxba7_ackpolicy_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba7_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba7_ena_msb, self.__reg_rxba7_ena_lsb)
    @reg_rxba7_ena.setter
    def reg_rxba7_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba7_ena_msb, self.__reg_rxba7_ena_lsb, value)

    @property
    def reg_rxba7_imr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba7_imr_msb, self.__reg_rxba7_imr_lsb)
    @reg_rxba7_imr.setter
    def reg_rxba7_imr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba7_imr_msb, self.__reg_rxba7_imr_lsb, value)

    @property
    def reg_rxba7_tid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba7_tid_msb, self.__reg_rxba7_tid_lsb)
    @reg_rxba7_tid.setter
    def reg_rxba7_tid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba7_tid_msb, self.__reg_rxba7_tid_lsb, value)

    @property
    def reg_rxba7_compbm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba7_compbm_msb, self.__reg_rxba7_compbm_lsb)
    @reg_rxba7_compbm.setter
    def reg_rxba7_compbm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba7_compbm_msb, self.__reg_rxba7_compbm_lsb, value)

    @property
    def reg_rxba7_multitid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba7_multitid_msb, self.__reg_rxba7_multitid_lsb)
    @reg_rxba7_multitid.setter
    def reg_rxba7_multitid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba7_multitid_msb, self.__reg_rxba7_multitid_lsb, value)

    @property
    def reg_rxba7_ackpolicy(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba7_ackpolicy_msb, self.__reg_rxba7_ackpolicy_lsb)
    @reg_rxba7_ackpolicy.setter
    def reg_rxba7_ackpolicy(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba7_ackpolicy_msb, self.__reg_rxba7_ackpolicy_lsb, value)
class MACRXBA7_TAHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x1b8
        self.__reg_rxba7_bssidsel_lsb = 16
        self.__reg_rxba7_bssidsel_msb = 17
        self.__reg_rxba7_tahi_lsb = 0
        self.__reg_rxba7_tahi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba7_bssidsel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba7_bssidsel_msb, self.__reg_rxba7_bssidsel_lsb)
    @reg_rxba7_bssidsel.setter
    def reg_rxba7_bssidsel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba7_bssidsel_msb, self.__reg_rxba7_bssidsel_lsb, value)

    @property
    def reg_rxba7_tahi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba7_tahi_msb, self.__reg_rxba7_tahi_lsb)
    @reg_rxba7_tahi.setter
    def reg_rxba7_tahi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba7_tahi_msb, self.__reg_rxba7_tahi_lsb, value)
class MACRXBA7_TALO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x1bc
        self.__reg_rxba7_talo_lsb = 0
        self.__reg_rxba7_talo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba7_talo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba7_talo_msb, self.__reg_rxba7_talo_lsb)
    @reg_rxba7_talo.setter
    def reg_rxba7_talo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba7_talo_msb, self.__reg_rxba7_talo_lsb, value)
class MACRXBA7_WINCONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x1c0
        self.__rxba7_curr_ws_lsb = 20
        self.__rxba7_curr_ws_msb = 31
        self.__reg_rxba7_winlen_lsb = 13
        self.__reg_rxba7_winlen_msb = 19
        self.__reg_rxba7_winstart_lsb = 0
        self.__reg_rxba7_winstart_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxba7_curr_ws(self):
        return self.__MEM.rdm(self.__addr, self.__rxba7_curr_ws_msb, self.__rxba7_curr_ws_lsb)
    @rxba7_curr_ws.setter
    def rxba7_curr_ws(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxba7_curr_ws_msb, self.__rxba7_curr_ws_lsb, value)

    @property
    def reg_rxba7_winlen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba7_winlen_msb, self.__reg_rxba7_winlen_lsb)
    @reg_rxba7_winlen.setter
    def reg_rxba7_winlen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba7_winlen_msb, self.__reg_rxba7_winlen_lsb, value)

    @property
    def reg_rxba7_winstart(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba7_winstart_msb, self.__reg_rxba7_winstart_lsb)
    @reg_rxba7_winstart.setter
    def reg_rxba7_winstart(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba7_winstart_msb, self.__reg_rxba7_winstart_lsb, value)
class MACRXBA7_BMHI_SW(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x1c4
        self.__reg_rxba7_bmhi_sw_lsb = 0
        self.__reg_rxba7_bmhi_sw_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba7_bmhi_sw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba7_bmhi_sw_msb, self.__reg_rxba7_bmhi_sw_lsb)
    @reg_rxba7_bmhi_sw.setter
    def reg_rxba7_bmhi_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba7_bmhi_sw_msb, self.__reg_rxba7_bmhi_sw_lsb, value)
class MACRXBA7_BMLO_SW(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x1c8
        self.__reg_rxba7_bmlo_sw_lsb = 0
        self.__reg_rxba7_bmlo_sw_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba7_bmlo_sw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba7_bmlo_sw_msb, self.__reg_rxba7_bmlo_sw_lsb)
    @reg_rxba7_bmlo_sw.setter
    def reg_rxba7_bmlo_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba7_bmlo_sw_msb, self.__reg_rxba7_bmlo_sw_lsb, value)
class MACRXBA7_BMHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x1cc
        self.__rxba7_bmhi_lsb = 0
        self.__rxba7_bmhi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxba7_bmhi(self):
        return self.__MEM.rdm(self.__addr, self.__rxba7_bmhi_msb, self.__rxba7_bmhi_lsb)
    @rxba7_bmhi.setter
    def rxba7_bmhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxba7_bmhi_msb, self.__rxba7_bmhi_lsb, value)
class MACRXBA7_BMLO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x1d0
        self.__rxba7_bmlo_lsb = 0
        self.__rxba7_bmlo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxba7_bmlo(self):
        return self.__MEM.rdm(self.__addr, self.__rxba7_bmlo_msb, self.__rxba7_bmlo_lsb)
    @rxba7_bmlo.setter
    def rxba7_bmlo(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxba7_bmlo_msb, self.__rxba7_bmlo_lsb, value)
class MACRXBA6_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x1d4
        self.__reg_rxba6_ena_lsb = 31
        self.__reg_rxba6_ena_msb = 31
        self.__reg_rxba6_imr_lsb = 30
        self.__reg_rxba6_imr_msb = 30
        self.__reg_rxba6_tid_lsb = 12
        self.__reg_rxba6_tid_msb = 15
        self.__reg_rxba6_compbm_lsb = 2
        self.__reg_rxba6_compbm_msb = 2
        self.__reg_rxba6_multitid_lsb = 1
        self.__reg_rxba6_multitid_msb = 1
        self.__reg_rxba6_ackpolicy_lsb = 0
        self.__reg_rxba6_ackpolicy_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba6_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba6_ena_msb, self.__reg_rxba6_ena_lsb)
    @reg_rxba6_ena.setter
    def reg_rxba6_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba6_ena_msb, self.__reg_rxba6_ena_lsb, value)

    @property
    def reg_rxba6_imr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba6_imr_msb, self.__reg_rxba6_imr_lsb)
    @reg_rxba6_imr.setter
    def reg_rxba6_imr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba6_imr_msb, self.__reg_rxba6_imr_lsb, value)

    @property
    def reg_rxba6_tid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba6_tid_msb, self.__reg_rxba6_tid_lsb)
    @reg_rxba6_tid.setter
    def reg_rxba6_tid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba6_tid_msb, self.__reg_rxba6_tid_lsb, value)

    @property
    def reg_rxba6_compbm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba6_compbm_msb, self.__reg_rxba6_compbm_lsb)
    @reg_rxba6_compbm.setter
    def reg_rxba6_compbm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba6_compbm_msb, self.__reg_rxba6_compbm_lsb, value)

    @property
    def reg_rxba6_multitid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba6_multitid_msb, self.__reg_rxba6_multitid_lsb)
    @reg_rxba6_multitid.setter
    def reg_rxba6_multitid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba6_multitid_msb, self.__reg_rxba6_multitid_lsb, value)

    @property
    def reg_rxba6_ackpolicy(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba6_ackpolicy_msb, self.__reg_rxba6_ackpolicy_lsb)
    @reg_rxba6_ackpolicy.setter
    def reg_rxba6_ackpolicy(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba6_ackpolicy_msb, self.__reg_rxba6_ackpolicy_lsb, value)
class MACRXBA6_TAHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x1d8
        self.__reg_rxba6_bssidsel_lsb = 16
        self.__reg_rxba6_bssidsel_msb = 17
        self.__reg_rxba6_tahi_lsb = 0
        self.__reg_rxba6_tahi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba6_bssidsel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba6_bssidsel_msb, self.__reg_rxba6_bssidsel_lsb)
    @reg_rxba6_bssidsel.setter
    def reg_rxba6_bssidsel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba6_bssidsel_msb, self.__reg_rxba6_bssidsel_lsb, value)

    @property
    def reg_rxba6_tahi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba6_tahi_msb, self.__reg_rxba6_tahi_lsb)
    @reg_rxba6_tahi.setter
    def reg_rxba6_tahi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba6_tahi_msb, self.__reg_rxba6_tahi_lsb, value)
class MACRXBA6_TALO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x1dc
        self.__reg_rxba6_talo_lsb = 0
        self.__reg_rxba6_talo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba6_talo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba6_talo_msb, self.__reg_rxba6_talo_lsb)
    @reg_rxba6_talo.setter
    def reg_rxba6_talo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba6_talo_msb, self.__reg_rxba6_talo_lsb, value)
class MACRXBA6_WINCONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x1e0
        self.__rxba6_curr_ws_lsb = 20
        self.__rxba6_curr_ws_msb = 31
        self.__reg_rxba6_winlen_lsb = 13
        self.__reg_rxba6_winlen_msb = 19
        self.__reg_rxba6_winstart_lsb = 0
        self.__reg_rxba6_winstart_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxba6_curr_ws(self):
        return self.__MEM.rdm(self.__addr, self.__rxba6_curr_ws_msb, self.__rxba6_curr_ws_lsb)
    @rxba6_curr_ws.setter
    def rxba6_curr_ws(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxba6_curr_ws_msb, self.__rxba6_curr_ws_lsb, value)

    @property
    def reg_rxba6_winlen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba6_winlen_msb, self.__reg_rxba6_winlen_lsb)
    @reg_rxba6_winlen.setter
    def reg_rxba6_winlen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba6_winlen_msb, self.__reg_rxba6_winlen_lsb, value)

    @property
    def reg_rxba6_winstart(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba6_winstart_msb, self.__reg_rxba6_winstart_lsb)
    @reg_rxba6_winstart.setter
    def reg_rxba6_winstart(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba6_winstart_msb, self.__reg_rxba6_winstart_lsb, value)
class MACRXBA6_BMHI_SW(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x1e4
        self.__reg_rxba6_bmhi_sw_lsb = 0
        self.__reg_rxba6_bmhi_sw_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba6_bmhi_sw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba6_bmhi_sw_msb, self.__reg_rxba6_bmhi_sw_lsb)
    @reg_rxba6_bmhi_sw.setter
    def reg_rxba6_bmhi_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba6_bmhi_sw_msb, self.__reg_rxba6_bmhi_sw_lsb, value)
class MACRXBA6_BMLO_SW(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x1e8
        self.__reg_rxba6_bmlo_sw_lsb = 0
        self.__reg_rxba6_bmlo_sw_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba6_bmlo_sw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba6_bmlo_sw_msb, self.__reg_rxba6_bmlo_sw_lsb)
    @reg_rxba6_bmlo_sw.setter
    def reg_rxba6_bmlo_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba6_bmlo_sw_msb, self.__reg_rxba6_bmlo_sw_lsb, value)
class MACRXBA6_BMHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x1ec
        self.__rxba6_bmhi_lsb = 0
        self.__rxba6_bmhi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxba6_bmhi(self):
        return self.__MEM.rdm(self.__addr, self.__rxba6_bmhi_msb, self.__rxba6_bmhi_lsb)
    @rxba6_bmhi.setter
    def rxba6_bmhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxba6_bmhi_msb, self.__rxba6_bmhi_lsb, value)
class MACRXBA6_BMLO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x1f0
        self.__rxba6_bmlo_lsb = 0
        self.__rxba6_bmlo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxba6_bmlo(self):
        return self.__MEM.rdm(self.__addr, self.__rxba6_bmlo_msb, self.__rxba6_bmlo_lsb)
    @rxba6_bmlo.setter
    def rxba6_bmlo(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxba6_bmlo_msb, self.__rxba6_bmlo_lsb, value)
class MACRXBA5_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x1f4
        self.__reg_rxba5_ena_lsb = 31
        self.__reg_rxba5_ena_msb = 31
        self.__reg_rxba5_imr_lsb = 30
        self.__reg_rxba5_imr_msb = 30
        self.__reg_rxba5_tid_lsb = 12
        self.__reg_rxba5_tid_msb = 15
        self.__reg_rxba5_compbm_lsb = 2
        self.__reg_rxba5_compbm_msb = 2
        self.__reg_rxba5_multitid_lsb = 1
        self.__reg_rxba5_multitid_msb = 1
        self.__reg_rxba5_ackpolicy_lsb = 0
        self.__reg_rxba5_ackpolicy_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba5_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba5_ena_msb, self.__reg_rxba5_ena_lsb)
    @reg_rxba5_ena.setter
    def reg_rxba5_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba5_ena_msb, self.__reg_rxba5_ena_lsb, value)

    @property
    def reg_rxba5_imr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba5_imr_msb, self.__reg_rxba5_imr_lsb)
    @reg_rxba5_imr.setter
    def reg_rxba5_imr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba5_imr_msb, self.__reg_rxba5_imr_lsb, value)

    @property
    def reg_rxba5_tid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba5_tid_msb, self.__reg_rxba5_tid_lsb)
    @reg_rxba5_tid.setter
    def reg_rxba5_tid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba5_tid_msb, self.__reg_rxba5_tid_lsb, value)

    @property
    def reg_rxba5_compbm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba5_compbm_msb, self.__reg_rxba5_compbm_lsb)
    @reg_rxba5_compbm.setter
    def reg_rxba5_compbm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba5_compbm_msb, self.__reg_rxba5_compbm_lsb, value)

    @property
    def reg_rxba5_multitid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba5_multitid_msb, self.__reg_rxba5_multitid_lsb)
    @reg_rxba5_multitid.setter
    def reg_rxba5_multitid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba5_multitid_msb, self.__reg_rxba5_multitid_lsb, value)

    @property
    def reg_rxba5_ackpolicy(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba5_ackpolicy_msb, self.__reg_rxba5_ackpolicy_lsb)
    @reg_rxba5_ackpolicy.setter
    def reg_rxba5_ackpolicy(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba5_ackpolicy_msb, self.__reg_rxba5_ackpolicy_lsb, value)
class MACRXBA5_TAHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x1f8
        self.__reg_rxba5_bssidsel_lsb = 16
        self.__reg_rxba5_bssidsel_msb = 17
        self.__reg_rxba5_tahi_lsb = 0
        self.__reg_rxba5_tahi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba5_bssidsel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba5_bssidsel_msb, self.__reg_rxba5_bssidsel_lsb)
    @reg_rxba5_bssidsel.setter
    def reg_rxba5_bssidsel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba5_bssidsel_msb, self.__reg_rxba5_bssidsel_lsb, value)

    @property
    def reg_rxba5_tahi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba5_tahi_msb, self.__reg_rxba5_tahi_lsb)
    @reg_rxba5_tahi.setter
    def reg_rxba5_tahi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba5_tahi_msb, self.__reg_rxba5_tahi_lsb, value)
class MACRXBA5_TALO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x1fc
        self.__reg_rxba5_talo_lsb = 0
        self.__reg_rxba5_talo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba5_talo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba5_talo_msb, self.__reg_rxba5_talo_lsb)
    @reg_rxba5_talo.setter
    def reg_rxba5_talo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba5_talo_msb, self.__reg_rxba5_talo_lsb, value)
class MACRXBA5_WINCONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x200
        self.__rxba5_curr_ws_lsb = 20
        self.__rxba5_curr_ws_msb = 31
        self.__reg_rxba5_winlen_lsb = 13
        self.__reg_rxba5_winlen_msb = 19
        self.__reg_rxba5_winstart_lsb = 0
        self.__reg_rxba5_winstart_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxba5_curr_ws(self):
        return self.__MEM.rdm(self.__addr, self.__rxba5_curr_ws_msb, self.__rxba5_curr_ws_lsb)
    @rxba5_curr_ws.setter
    def rxba5_curr_ws(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxba5_curr_ws_msb, self.__rxba5_curr_ws_lsb, value)

    @property
    def reg_rxba5_winlen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba5_winlen_msb, self.__reg_rxba5_winlen_lsb)
    @reg_rxba5_winlen.setter
    def reg_rxba5_winlen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba5_winlen_msb, self.__reg_rxba5_winlen_lsb, value)

    @property
    def reg_rxba5_winstart(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba5_winstart_msb, self.__reg_rxba5_winstart_lsb)
    @reg_rxba5_winstart.setter
    def reg_rxba5_winstart(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba5_winstart_msb, self.__reg_rxba5_winstart_lsb, value)
class MACRXBA5_BMHI_SW(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x204
        self.__reg_rxba5_bmhi_sw_lsb = 0
        self.__reg_rxba5_bmhi_sw_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba5_bmhi_sw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba5_bmhi_sw_msb, self.__reg_rxba5_bmhi_sw_lsb)
    @reg_rxba5_bmhi_sw.setter
    def reg_rxba5_bmhi_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba5_bmhi_sw_msb, self.__reg_rxba5_bmhi_sw_lsb, value)
class MACRXBA5_BMLO_SW(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x208
        self.__reg_rxba5_bmlo_sw_lsb = 0
        self.__reg_rxba5_bmlo_sw_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba5_bmlo_sw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba5_bmlo_sw_msb, self.__reg_rxba5_bmlo_sw_lsb)
    @reg_rxba5_bmlo_sw.setter
    def reg_rxba5_bmlo_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba5_bmlo_sw_msb, self.__reg_rxba5_bmlo_sw_lsb, value)
class MACRXBA5_BMHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x20c
        self.__rxba5_bmhi_lsb = 0
        self.__rxba5_bmhi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxba5_bmhi(self):
        return self.__MEM.rdm(self.__addr, self.__rxba5_bmhi_msb, self.__rxba5_bmhi_lsb)
    @rxba5_bmhi.setter
    def rxba5_bmhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxba5_bmhi_msb, self.__rxba5_bmhi_lsb, value)
class MACRXBA5_BMLO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x210
        self.__rxba5_bmlo_lsb = 0
        self.__rxba5_bmlo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxba5_bmlo(self):
        return self.__MEM.rdm(self.__addr, self.__rxba5_bmlo_msb, self.__rxba5_bmlo_lsb)
    @rxba5_bmlo.setter
    def rxba5_bmlo(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxba5_bmlo_msb, self.__rxba5_bmlo_lsb, value)
class MACRXBA4_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x214
        self.__reg_rxba4_ena_lsb = 31
        self.__reg_rxba4_ena_msb = 31
        self.__reg_rxba4_imr_lsb = 30
        self.__reg_rxba4_imr_msb = 30
        self.__reg_rxba4_tid_lsb = 12
        self.__reg_rxba4_tid_msb = 15
        self.__reg_rxba4_compbm_lsb = 2
        self.__reg_rxba4_compbm_msb = 2
        self.__reg_rxba4_multitid_lsb = 1
        self.__reg_rxba4_multitid_msb = 1
        self.__reg_rxba4_ackpolicy_lsb = 0
        self.__reg_rxba4_ackpolicy_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba4_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba4_ena_msb, self.__reg_rxba4_ena_lsb)
    @reg_rxba4_ena.setter
    def reg_rxba4_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba4_ena_msb, self.__reg_rxba4_ena_lsb, value)

    @property
    def reg_rxba4_imr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba4_imr_msb, self.__reg_rxba4_imr_lsb)
    @reg_rxba4_imr.setter
    def reg_rxba4_imr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba4_imr_msb, self.__reg_rxba4_imr_lsb, value)

    @property
    def reg_rxba4_tid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba4_tid_msb, self.__reg_rxba4_tid_lsb)
    @reg_rxba4_tid.setter
    def reg_rxba4_tid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba4_tid_msb, self.__reg_rxba4_tid_lsb, value)

    @property
    def reg_rxba4_compbm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba4_compbm_msb, self.__reg_rxba4_compbm_lsb)
    @reg_rxba4_compbm.setter
    def reg_rxba4_compbm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba4_compbm_msb, self.__reg_rxba4_compbm_lsb, value)

    @property
    def reg_rxba4_multitid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba4_multitid_msb, self.__reg_rxba4_multitid_lsb)
    @reg_rxba4_multitid.setter
    def reg_rxba4_multitid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba4_multitid_msb, self.__reg_rxba4_multitid_lsb, value)

    @property
    def reg_rxba4_ackpolicy(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba4_ackpolicy_msb, self.__reg_rxba4_ackpolicy_lsb)
    @reg_rxba4_ackpolicy.setter
    def reg_rxba4_ackpolicy(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba4_ackpolicy_msb, self.__reg_rxba4_ackpolicy_lsb, value)
class MACRXBA4_TAHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x218
        self.__reg_rxba4_bssidsel_lsb = 16
        self.__reg_rxba4_bssidsel_msb = 17
        self.__reg_rxba4_tahi_lsb = 0
        self.__reg_rxba4_tahi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba4_bssidsel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba4_bssidsel_msb, self.__reg_rxba4_bssidsel_lsb)
    @reg_rxba4_bssidsel.setter
    def reg_rxba4_bssidsel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba4_bssidsel_msb, self.__reg_rxba4_bssidsel_lsb, value)

    @property
    def reg_rxba4_tahi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba4_tahi_msb, self.__reg_rxba4_tahi_lsb)
    @reg_rxba4_tahi.setter
    def reg_rxba4_tahi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba4_tahi_msb, self.__reg_rxba4_tahi_lsb, value)
class MACRXBA4_TALO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x21c
        self.__reg_rxba4_talo_lsb = 0
        self.__reg_rxba4_talo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba4_talo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba4_talo_msb, self.__reg_rxba4_talo_lsb)
    @reg_rxba4_talo.setter
    def reg_rxba4_talo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba4_talo_msb, self.__reg_rxba4_talo_lsb, value)
class MACRXBA4_WINCONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x220
        self.__rxba4_curr_ws_lsb = 20
        self.__rxba4_curr_ws_msb = 31
        self.__reg_rxba4_winlen_lsb = 13
        self.__reg_rxba4_winlen_msb = 19
        self.__reg_rxba4_winstart_lsb = 0
        self.__reg_rxba4_winstart_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxba4_curr_ws(self):
        return self.__MEM.rdm(self.__addr, self.__rxba4_curr_ws_msb, self.__rxba4_curr_ws_lsb)
    @rxba4_curr_ws.setter
    def rxba4_curr_ws(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxba4_curr_ws_msb, self.__rxba4_curr_ws_lsb, value)

    @property
    def reg_rxba4_winlen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba4_winlen_msb, self.__reg_rxba4_winlen_lsb)
    @reg_rxba4_winlen.setter
    def reg_rxba4_winlen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba4_winlen_msb, self.__reg_rxba4_winlen_lsb, value)

    @property
    def reg_rxba4_winstart(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba4_winstart_msb, self.__reg_rxba4_winstart_lsb)
    @reg_rxba4_winstart.setter
    def reg_rxba4_winstart(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba4_winstart_msb, self.__reg_rxba4_winstart_lsb, value)
class MACRXBA4_BMHI_SW(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x224
        self.__reg_rxba4_bmhi_sw_lsb = 0
        self.__reg_rxba4_bmhi_sw_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba4_bmhi_sw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba4_bmhi_sw_msb, self.__reg_rxba4_bmhi_sw_lsb)
    @reg_rxba4_bmhi_sw.setter
    def reg_rxba4_bmhi_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba4_bmhi_sw_msb, self.__reg_rxba4_bmhi_sw_lsb, value)
class MACRXBA4_BMLO_SW(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x228
        self.__reg_rxba4_bmlo_sw_lsb = 0
        self.__reg_rxba4_bmlo_sw_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba4_bmlo_sw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba4_bmlo_sw_msb, self.__reg_rxba4_bmlo_sw_lsb)
    @reg_rxba4_bmlo_sw.setter
    def reg_rxba4_bmlo_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba4_bmlo_sw_msb, self.__reg_rxba4_bmlo_sw_lsb, value)
class MACRXBA4_BMHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x22c
        self.__rxba4_bmhi_lsb = 0
        self.__rxba4_bmhi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxba4_bmhi(self):
        return self.__MEM.rdm(self.__addr, self.__rxba4_bmhi_msb, self.__rxba4_bmhi_lsb)
    @rxba4_bmhi.setter
    def rxba4_bmhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxba4_bmhi_msb, self.__rxba4_bmhi_lsb, value)
class MACRXBA4_BMLO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x230
        self.__rxba4_bmlo_lsb = 0
        self.__rxba4_bmlo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxba4_bmlo(self):
        return self.__MEM.rdm(self.__addr, self.__rxba4_bmlo_msb, self.__rxba4_bmlo_lsb)
    @rxba4_bmlo.setter
    def rxba4_bmlo(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxba4_bmlo_msb, self.__rxba4_bmlo_lsb, value)
class MACRXBA3_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x234
        self.__reg_rxba3_ena_lsb = 31
        self.__reg_rxba3_ena_msb = 31
        self.__reg_rxba3_imr_lsb = 30
        self.__reg_rxba3_imr_msb = 30
        self.__reg_rxba3_tid_lsb = 12
        self.__reg_rxba3_tid_msb = 15
        self.__reg_rxba3_compbm_lsb = 2
        self.__reg_rxba3_compbm_msb = 2
        self.__reg_rxba3_multitid_lsb = 1
        self.__reg_rxba3_multitid_msb = 1
        self.__reg_rxba3_ackpolicy_lsb = 0
        self.__reg_rxba3_ackpolicy_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba3_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba3_ena_msb, self.__reg_rxba3_ena_lsb)
    @reg_rxba3_ena.setter
    def reg_rxba3_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba3_ena_msb, self.__reg_rxba3_ena_lsb, value)

    @property
    def reg_rxba3_imr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba3_imr_msb, self.__reg_rxba3_imr_lsb)
    @reg_rxba3_imr.setter
    def reg_rxba3_imr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba3_imr_msb, self.__reg_rxba3_imr_lsb, value)

    @property
    def reg_rxba3_tid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba3_tid_msb, self.__reg_rxba3_tid_lsb)
    @reg_rxba3_tid.setter
    def reg_rxba3_tid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba3_tid_msb, self.__reg_rxba3_tid_lsb, value)

    @property
    def reg_rxba3_compbm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba3_compbm_msb, self.__reg_rxba3_compbm_lsb)
    @reg_rxba3_compbm.setter
    def reg_rxba3_compbm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba3_compbm_msb, self.__reg_rxba3_compbm_lsb, value)

    @property
    def reg_rxba3_multitid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba3_multitid_msb, self.__reg_rxba3_multitid_lsb)
    @reg_rxba3_multitid.setter
    def reg_rxba3_multitid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba3_multitid_msb, self.__reg_rxba3_multitid_lsb, value)

    @property
    def reg_rxba3_ackpolicy(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba3_ackpolicy_msb, self.__reg_rxba3_ackpolicy_lsb)
    @reg_rxba3_ackpolicy.setter
    def reg_rxba3_ackpolicy(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba3_ackpolicy_msb, self.__reg_rxba3_ackpolicy_lsb, value)
class MACRXBA3_TAHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x238
        self.__reg_rxba3_bssidsel_lsb = 16
        self.__reg_rxba3_bssidsel_msb = 17
        self.__reg_rxba3_tahi_lsb = 0
        self.__reg_rxba3_tahi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba3_bssidsel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba3_bssidsel_msb, self.__reg_rxba3_bssidsel_lsb)
    @reg_rxba3_bssidsel.setter
    def reg_rxba3_bssidsel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba3_bssidsel_msb, self.__reg_rxba3_bssidsel_lsb, value)

    @property
    def reg_rxba3_tahi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba3_tahi_msb, self.__reg_rxba3_tahi_lsb)
    @reg_rxba3_tahi.setter
    def reg_rxba3_tahi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba3_tahi_msb, self.__reg_rxba3_tahi_lsb, value)
class MACRXBA3_TALO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x23c
        self.__reg_rxba3_talo_lsb = 0
        self.__reg_rxba3_talo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba3_talo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba3_talo_msb, self.__reg_rxba3_talo_lsb)
    @reg_rxba3_talo.setter
    def reg_rxba3_talo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba3_talo_msb, self.__reg_rxba3_talo_lsb, value)
class MACRXBA3_WINCONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x240
        self.__rxba3_curr_ws_lsb = 20
        self.__rxba3_curr_ws_msb = 31
        self.__reg_rxba3_winlen_lsb = 13
        self.__reg_rxba3_winlen_msb = 19
        self.__reg_rxba3_winstart_lsb = 0
        self.__reg_rxba3_winstart_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxba3_curr_ws(self):
        return self.__MEM.rdm(self.__addr, self.__rxba3_curr_ws_msb, self.__rxba3_curr_ws_lsb)
    @rxba3_curr_ws.setter
    def rxba3_curr_ws(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxba3_curr_ws_msb, self.__rxba3_curr_ws_lsb, value)

    @property
    def reg_rxba3_winlen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba3_winlen_msb, self.__reg_rxba3_winlen_lsb)
    @reg_rxba3_winlen.setter
    def reg_rxba3_winlen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba3_winlen_msb, self.__reg_rxba3_winlen_lsb, value)

    @property
    def reg_rxba3_winstart(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba3_winstart_msb, self.__reg_rxba3_winstart_lsb)
    @reg_rxba3_winstart.setter
    def reg_rxba3_winstart(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba3_winstart_msb, self.__reg_rxba3_winstart_lsb, value)
class MACRXBA3_BMHI_SW(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x244
        self.__reg_rxba3_bmhi_sw_lsb = 0
        self.__reg_rxba3_bmhi_sw_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba3_bmhi_sw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba3_bmhi_sw_msb, self.__reg_rxba3_bmhi_sw_lsb)
    @reg_rxba3_bmhi_sw.setter
    def reg_rxba3_bmhi_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba3_bmhi_sw_msb, self.__reg_rxba3_bmhi_sw_lsb, value)
class MACRXBA3_BMLO_SW(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x248
        self.__reg_rxba3_bmlo_sw_lsb = 0
        self.__reg_rxba3_bmlo_sw_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba3_bmlo_sw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba3_bmlo_sw_msb, self.__reg_rxba3_bmlo_sw_lsb)
    @reg_rxba3_bmlo_sw.setter
    def reg_rxba3_bmlo_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba3_bmlo_sw_msb, self.__reg_rxba3_bmlo_sw_lsb, value)
class MACRXBA3_BMHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x24c
        self.__rxba3_bmhi_lsb = 0
        self.__rxba3_bmhi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxba3_bmhi(self):
        return self.__MEM.rdm(self.__addr, self.__rxba3_bmhi_msb, self.__rxba3_bmhi_lsb)
    @rxba3_bmhi.setter
    def rxba3_bmhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxba3_bmhi_msb, self.__rxba3_bmhi_lsb, value)
class MACRXBA3_BMLO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x250
        self.__rxba3_bmlo_lsb = 0
        self.__rxba3_bmlo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxba3_bmlo(self):
        return self.__MEM.rdm(self.__addr, self.__rxba3_bmlo_msb, self.__rxba3_bmlo_lsb)
    @rxba3_bmlo.setter
    def rxba3_bmlo(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxba3_bmlo_msb, self.__rxba3_bmlo_lsb, value)
class MACRXBA2_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x254
        self.__reg_rxba2_ena_lsb = 31
        self.__reg_rxba2_ena_msb = 31
        self.__reg_rxba2_imr_lsb = 30
        self.__reg_rxba2_imr_msb = 30
        self.__reg_rxba2_tid_lsb = 12
        self.__reg_rxba2_tid_msb = 15
        self.__reg_rxba2_compbm_lsb = 2
        self.__reg_rxba2_compbm_msb = 2
        self.__reg_rxba2_multitid_lsb = 1
        self.__reg_rxba2_multitid_msb = 1
        self.__reg_rxba2_ackpolicy_lsb = 0
        self.__reg_rxba2_ackpolicy_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba2_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba2_ena_msb, self.__reg_rxba2_ena_lsb)
    @reg_rxba2_ena.setter
    def reg_rxba2_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba2_ena_msb, self.__reg_rxba2_ena_lsb, value)

    @property
    def reg_rxba2_imr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba2_imr_msb, self.__reg_rxba2_imr_lsb)
    @reg_rxba2_imr.setter
    def reg_rxba2_imr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba2_imr_msb, self.__reg_rxba2_imr_lsb, value)

    @property
    def reg_rxba2_tid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba2_tid_msb, self.__reg_rxba2_tid_lsb)
    @reg_rxba2_tid.setter
    def reg_rxba2_tid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba2_tid_msb, self.__reg_rxba2_tid_lsb, value)

    @property
    def reg_rxba2_compbm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba2_compbm_msb, self.__reg_rxba2_compbm_lsb)
    @reg_rxba2_compbm.setter
    def reg_rxba2_compbm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba2_compbm_msb, self.__reg_rxba2_compbm_lsb, value)

    @property
    def reg_rxba2_multitid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba2_multitid_msb, self.__reg_rxba2_multitid_lsb)
    @reg_rxba2_multitid.setter
    def reg_rxba2_multitid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba2_multitid_msb, self.__reg_rxba2_multitid_lsb, value)

    @property
    def reg_rxba2_ackpolicy(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba2_ackpolicy_msb, self.__reg_rxba2_ackpolicy_lsb)
    @reg_rxba2_ackpolicy.setter
    def reg_rxba2_ackpolicy(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba2_ackpolicy_msb, self.__reg_rxba2_ackpolicy_lsb, value)
class MACRXBA2_TAHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x258
        self.__reg_rxba2_bssidsel_lsb = 16
        self.__reg_rxba2_bssidsel_msb = 17
        self.__reg_rxba2_tahi_lsb = 0
        self.__reg_rxba2_tahi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba2_bssidsel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba2_bssidsel_msb, self.__reg_rxba2_bssidsel_lsb)
    @reg_rxba2_bssidsel.setter
    def reg_rxba2_bssidsel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba2_bssidsel_msb, self.__reg_rxba2_bssidsel_lsb, value)

    @property
    def reg_rxba2_tahi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba2_tahi_msb, self.__reg_rxba2_tahi_lsb)
    @reg_rxba2_tahi.setter
    def reg_rxba2_tahi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba2_tahi_msb, self.__reg_rxba2_tahi_lsb, value)
class MACRXBA2_TALO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x25c
        self.__reg_rxba2_talo_lsb = 0
        self.__reg_rxba2_talo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba2_talo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba2_talo_msb, self.__reg_rxba2_talo_lsb)
    @reg_rxba2_talo.setter
    def reg_rxba2_talo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba2_talo_msb, self.__reg_rxba2_talo_lsb, value)
class MACRXBA2_WINCONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x260
        self.__rxba2_curr_ws_lsb = 20
        self.__rxba2_curr_ws_msb = 31
        self.__reg_rxba2_winlen_lsb = 13
        self.__reg_rxba2_winlen_msb = 19
        self.__reg_rxba2_winstart_lsb = 0
        self.__reg_rxba2_winstart_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxba2_curr_ws(self):
        return self.__MEM.rdm(self.__addr, self.__rxba2_curr_ws_msb, self.__rxba2_curr_ws_lsb)
    @rxba2_curr_ws.setter
    def rxba2_curr_ws(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxba2_curr_ws_msb, self.__rxba2_curr_ws_lsb, value)

    @property
    def reg_rxba2_winlen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba2_winlen_msb, self.__reg_rxba2_winlen_lsb)
    @reg_rxba2_winlen.setter
    def reg_rxba2_winlen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba2_winlen_msb, self.__reg_rxba2_winlen_lsb, value)

    @property
    def reg_rxba2_winstart(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba2_winstart_msb, self.__reg_rxba2_winstart_lsb)
    @reg_rxba2_winstart.setter
    def reg_rxba2_winstart(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba2_winstart_msb, self.__reg_rxba2_winstart_lsb, value)
class MACRXBA2_BMHI_SW(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x264
        self.__reg_rxba2_bmhi_sw_lsb = 0
        self.__reg_rxba2_bmhi_sw_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba2_bmhi_sw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba2_bmhi_sw_msb, self.__reg_rxba2_bmhi_sw_lsb)
    @reg_rxba2_bmhi_sw.setter
    def reg_rxba2_bmhi_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba2_bmhi_sw_msb, self.__reg_rxba2_bmhi_sw_lsb, value)
class MACRXBA2_BMLO_SW(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x268
        self.__reg_rxba2_bmlo_sw_lsb = 0
        self.__reg_rxba2_bmlo_sw_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba2_bmlo_sw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba2_bmlo_sw_msb, self.__reg_rxba2_bmlo_sw_lsb)
    @reg_rxba2_bmlo_sw.setter
    def reg_rxba2_bmlo_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba2_bmlo_sw_msb, self.__reg_rxba2_bmlo_sw_lsb, value)
class MACRXBA2_BMHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x26c
        self.__rxba2_bmhi_lsb = 0
        self.__rxba2_bmhi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxba2_bmhi(self):
        return self.__MEM.rdm(self.__addr, self.__rxba2_bmhi_msb, self.__rxba2_bmhi_lsb)
    @rxba2_bmhi.setter
    def rxba2_bmhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxba2_bmhi_msb, self.__rxba2_bmhi_lsb, value)
class MACRXBA2_BMLO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x270
        self.__rxba2_bmlo_lsb = 0
        self.__rxba2_bmlo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxba2_bmlo(self):
        return self.__MEM.rdm(self.__addr, self.__rxba2_bmlo_msb, self.__rxba2_bmlo_lsb)
    @rxba2_bmlo.setter
    def rxba2_bmlo(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxba2_bmlo_msb, self.__rxba2_bmlo_lsb, value)
class MACRXBA1_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x274
        self.__reg_rxba1_ena_lsb = 31
        self.__reg_rxba1_ena_msb = 31
        self.__reg_rxba1_imr_lsb = 30
        self.__reg_rxba1_imr_msb = 30
        self.__reg_rxba1_tid_lsb = 12
        self.__reg_rxba1_tid_msb = 15
        self.__reg_rxba1_compbm_lsb = 2
        self.__reg_rxba1_compbm_msb = 2
        self.__reg_rxba1_multitid_lsb = 1
        self.__reg_rxba1_multitid_msb = 1
        self.__reg_rxba1_ackpolicy_lsb = 0
        self.__reg_rxba1_ackpolicy_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba1_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba1_ena_msb, self.__reg_rxba1_ena_lsb)
    @reg_rxba1_ena.setter
    def reg_rxba1_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba1_ena_msb, self.__reg_rxba1_ena_lsb, value)

    @property
    def reg_rxba1_imr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba1_imr_msb, self.__reg_rxba1_imr_lsb)
    @reg_rxba1_imr.setter
    def reg_rxba1_imr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba1_imr_msb, self.__reg_rxba1_imr_lsb, value)

    @property
    def reg_rxba1_tid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba1_tid_msb, self.__reg_rxba1_tid_lsb)
    @reg_rxba1_tid.setter
    def reg_rxba1_tid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba1_tid_msb, self.__reg_rxba1_tid_lsb, value)

    @property
    def reg_rxba1_compbm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba1_compbm_msb, self.__reg_rxba1_compbm_lsb)
    @reg_rxba1_compbm.setter
    def reg_rxba1_compbm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba1_compbm_msb, self.__reg_rxba1_compbm_lsb, value)

    @property
    def reg_rxba1_multitid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba1_multitid_msb, self.__reg_rxba1_multitid_lsb)
    @reg_rxba1_multitid.setter
    def reg_rxba1_multitid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba1_multitid_msb, self.__reg_rxba1_multitid_lsb, value)

    @property
    def reg_rxba1_ackpolicy(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba1_ackpolicy_msb, self.__reg_rxba1_ackpolicy_lsb)
    @reg_rxba1_ackpolicy.setter
    def reg_rxba1_ackpolicy(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba1_ackpolicy_msb, self.__reg_rxba1_ackpolicy_lsb, value)
class MACRXBA1_TAHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x278
        self.__reg_rxba1_bssidsel_lsb = 16
        self.__reg_rxba1_bssidsel_msb = 17
        self.__reg_rxba1_tahi_lsb = 0
        self.__reg_rxba1_tahi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba1_bssidsel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba1_bssidsel_msb, self.__reg_rxba1_bssidsel_lsb)
    @reg_rxba1_bssidsel.setter
    def reg_rxba1_bssidsel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba1_bssidsel_msb, self.__reg_rxba1_bssidsel_lsb, value)

    @property
    def reg_rxba1_tahi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba1_tahi_msb, self.__reg_rxba1_tahi_lsb)
    @reg_rxba1_tahi.setter
    def reg_rxba1_tahi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba1_tahi_msb, self.__reg_rxba1_tahi_lsb, value)
class MACRXBA1_TALO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x27c
        self.__reg_rxba1_talo_lsb = 0
        self.__reg_rxba1_talo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba1_talo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba1_talo_msb, self.__reg_rxba1_talo_lsb)
    @reg_rxba1_talo.setter
    def reg_rxba1_talo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba1_talo_msb, self.__reg_rxba1_talo_lsb, value)
class MACRXBA1_WINCONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x280
        self.__rxba1_curr_ws_lsb = 20
        self.__rxba1_curr_ws_msb = 31
        self.__reg_rxba1_winlen_lsb = 13
        self.__reg_rxba1_winlen_msb = 19
        self.__reg_rxba1_winstart_lsb = 0
        self.__reg_rxba1_winstart_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxba1_curr_ws(self):
        return self.__MEM.rdm(self.__addr, self.__rxba1_curr_ws_msb, self.__rxba1_curr_ws_lsb)
    @rxba1_curr_ws.setter
    def rxba1_curr_ws(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxba1_curr_ws_msb, self.__rxba1_curr_ws_lsb, value)

    @property
    def reg_rxba1_winlen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba1_winlen_msb, self.__reg_rxba1_winlen_lsb)
    @reg_rxba1_winlen.setter
    def reg_rxba1_winlen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba1_winlen_msb, self.__reg_rxba1_winlen_lsb, value)

    @property
    def reg_rxba1_winstart(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba1_winstart_msb, self.__reg_rxba1_winstart_lsb)
    @reg_rxba1_winstart.setter
    def reg_rxba1_winstart(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba1_winstart_msb, self.__reg_rxba1_winstart_lsb, value)
class MACRXBA1_BMHI_SW(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x284
        self.__reg_rxba1_bmhi_sw_lsb = 0
        self.__reg_rxba1_bmhi_sw_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba1_bmhi_sw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba1_bmhi_sw_msb, self.__reg_rxba1_bmhi_sw_lsb)
    @reg_rxba1_bmhi_sw.setter
    def reg_rxba1_bmhi_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba1_bmhi_sw_msb, self.__reg_rxba1_bmhi_sw_lsb, value)
class MACRXBA1_BMLO_SW(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x288
        self.__reg_rxba1_bmlo_sw_lsb = 0
        self.__reg_rxba1_bmlo_sw_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba1_bmlo_sw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba1_bmlo_sw_msb, self.__reg_rxba1_bmlo_sw_lsb)
    @reg_rxba1_bmlo_sw.setter
    def reg_rxba1_bmlo_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba1_bmlo_sw_msb, self.__reg_rxba1_bmlo_sw_lsb, value)
class MACRXBA1_BMHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x28c
        self.__rxba1_bmhi_lsb = 0
        self.__rxba1_bmhi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxba1_bmhi(self):
        return self.__MEM.rdm(self.__addr, self.__rxba1_bmhi_msb, self.__rxba1_bmhi_lsb)
    @rxba1_bmhi.setter
    def rxba1_bmhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxba1_bmhi_msb, self.__rxba1_bmhi_lsb, value)
class MACRXBA1_BMLO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x290
        self.__rxba1_bmlo_lsb = 0
        self.__rxba1_bmlo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxba1_bmlo(self):
        return self.__MEM.rdm(self.__addr, self.__rxba1_bmlo_msb, self.__rxba1_bmlo_lsb)
    @rxba1_bmlo.setter
    def rxba1_bmlo(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxba1_bmlo_msb, self.__rxba1_bmlo_lsb, value)
class MACRXBA0_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x294
        self.__reg_rxba0_ena_lsb = 31
        self.__reg_rxba0_ena_msb = 31
        self.__reg_rxba0_imr_lsb = 30
        self.__reg_rxba0_imr_msb = 30
        self.__reg_rxba0_tid_lsb = 12
        self.__reg_rxba0_tid_msb = 15
        self.__reg_rxba0_compbm_lsb = 2
        self.__reg_rxba0_compbm_msb = 2
        self.__reg_rxba0_multitid_lsb = 1
        self.__reg_rxba0_multitid_msb = 1
        self.__reg_rxba0_ackpolicy_lsb = 0
        self.__reg_rxba0_ackpolicy_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba0_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba0_ena_msb, self.__reg_rxba0_ena_lsb)
    @reg_rxba0_ena.setter
    def reg_rxba0_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba0_ena_msb, self.__reg_rxba0_ena_lsb, value)

    @property
    def reg_rxba0_imr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba0_imr_msb, self.__reg_rxba0_imr_lsb)
    @reg_rxba0_imr.setter
    def reg_rxba0_imr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba0_imr_msb, self.__reg_rxba0_imr_lsb, value)

    @property
    def reg_rxba0_tid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba0_tid_msb, self.__reg_rxba0_tid_lsb)
    @reg_rxba0_tid.setter
    def reg_rxba0_tid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba0_tid_msb, self.__reg_rxba0_tid_lsb, value)

    @property
    def reg_rxba0_compbm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba0_compbm_msb, self.__reg_rxba0_compbm_lsb)
    @reg_rxba0_compbm.setter
    def reg_rxba0_compbm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba0_compbm_msb, self.__reg_rxba0_compbm_lsb, value)

    @property
    def reg_rxba0_multitid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba0_multitid_msb, self.__reg_rxba0_multitid_lsb)
    @reg_rxba0_multitid.setter
    def reg_rxba0_multitid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba0_multitid_msb, self.__reg_rxba0_multitid_lsb, value)

    @property
    def reg_rxba0_ackpolicy(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba0_ackpolicy_msb, self.__reg_rxba0_ackpolicy_lsb)
    @reg_rxba0_ackpolicy.setter
    def reg_rxba0_ackpolicy(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba0_ackpolicy_msb, self.__reg_rxba0_ackpolicy_lsb, value)
class MACRXBA0_TAHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x298
        self.__reg_rxba0_bssidsel_lsb = 16
        self.__reg_rxba0_bssidsel_msb = 17
        self.__reg_rxba0_tahi_lsb = 0
        self.__reg_rxba0_tahi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba0_bssidsel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba0_bssidsel_msb, self.__reg_rxba0_bssidsel_lsb)
    @reg_rxba0_bssidsel.setter
    def reg_rxba0_bssidsel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba0_bssidsel_msb, self.__reg_rxba0_bssidsel_lsb, value)

    @property
    def reg_rxba0_tahi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba0_tahi_msb, self.__reg_rxba0_tahi_lsb)
    @reg_rxba0_tahi.setter
    def reg_rxba0_tahi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba0_tahi_msb, self.__reg_rxba0_tahi_lsb, value)
class MACRXBA0_TALO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x29c
        self.__reg_rxba0_talo_lsb = 0
        self.__reg_rxba0_talo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba0_talo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba0_talo_msb, self.__reg_rxba0_talo_lsb)
    @reg_rxba0_talo.setter
    def reg_rxba0_talo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba0_talo_msb, self.__reg_rxba0_talo_lsb, value)
class MACRXBA0_WINCONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x2a0
        self.__rxba0_curr_ws_lsb = 20
        self.__rxba0_curr_ws_msb = 31
        self.__reg_rxba0_winlen_lsb = 13
        self.__reg_rxba0_winlen_msb = 19
        self.__reg_rxba0_winstart_lsb = 0
        self.__reg_rxba0_winstart_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxba0_curr_ws(self):
        return self.__MEM.rdm(self.__addr, self.__rxba0_curr_ws_msb, self.__rxba0_curr_ws_lsb)
    @rxba0_curr_ws.setter
    def rxba0_curr_ws(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxba0_curr_ws_msb, self.__rxba0_curr_ws_lsb, value)

    @property
    def reg_rxba0_winlen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba0_winlen_msb, self.__reg_rxba0_winlen_lsb)
    @reg_rxba0_winlen.setter
    def reg_rxba0_winlen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba0_winlen_msb, self.__reg_rxba0_winlen_lsb, value)

    @property
    def reg_rxba0_winstart(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba0_winstart_msb, self.__reg_rxba0_winstart_lsb)
    @reg_rxba0_winstart.setter
    def reg_rxba0_winstart(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba0_winstart_msb, self.__reg_rxba0_winstart_lsb, value)
class MACRXBA0_BMHI_SW(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x2a4
        self.__reg_rxba0_bmhi_sw_lsb = 0
        self.__reg_rxba0_bmhi_sw_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba0_bmhi_sw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba0_bmhi_sw_msb, self.__reg_rxba0_bmhi_sw_lsb)
    @reg_rxba0_bmhi_sw.setter
    def reg_rxba0_bmhi_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba0_bmhi_sw_msb, self.__reg_rxba0_bmhi_sw_lsb, value)
class MACRXBA0_BMLO_SW(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x2a8
        self.__reg_rxba0_bmlo_sw_lsb = 0
        self.__reg_rxba0_bmlo_sw_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxba0_bmlo_sw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxba0_bmlo_sw_msb, self.__reg_rxba0_bmlo_sw_lsb)
    @reg_rxba0_bmlo_sw.setter
    def reg_rxba0_bmlo_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxba0_bmlo_sw_msb, self.__reg_rxba0_bmlo_sw_lsb, value)
class MACRXBA0_BMHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x2ac
        self.__rxba0_bmhi_lsb = 0
        self.__rxba0_bmhi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxba0_bmhi(self):
        return self.__MEM.rdm(self.__addr, self.__rxba0_bmhi_msb, self.__rxba0_bmhi_lsb)
    @rxba0_bmhi.setter
    def rxba0_bmhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxba0_bmhi_msb, self.__rxba0_bmhi_lsb, value)
class MACRXBA0_BMLO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x2b0
        self.__rxba0_bmlo_lsb = 0
        self.__rxba0_bmlo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxba0_bmlo(self):
        return self.__MEM.rdm(self.__addr, self.__rxba0_bmlo_msb, self.__rxba0_bmlo_lsb)
    @rxba0_bmlo.setter
    def rxba0_bmlo(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxba0_bmlo_msb, self.__rxba0_bmlo_lsb, value)
class MACTXBA_BMHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x2b4
        self.__txba_bmhi_lsb = 0
        self.__txba_bmhi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txba_bmhi(self):
        return self.__MEM.rdm(self.__addr, self.__txba_bmhi_msb, self.__txba_bmhi_lsb)
    @txba_bmhi.setter
    def txba_bmhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txba_bmhi_msb, self.__txba_bmhi_lsb, value)
class MACTXBA_BMLO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x2b8
        self.__txba_bmlo_lsb = 0
        self.__txba_bmlo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txba_bmlo(self):
        return self.__MEM.rdm(self.__addr, self.__txba_bmlo_msb, self.__txba_bmlo_lsb)
    @txba_bmlo.setter
    def txba_bmlo(self, value):
        return self.__MEM.wrm(self.__addr, self.__txba_bmlo_msb, self.__txba_bmlo_lsb, value)
class MACTXBA_TAHI(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x2bc
        self.__txba_tahi_lsb = 0
        self.__txba_tahi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txba_tahi(self):
        return self.__MEM.rdm(self.__addr, self.__txba_tahi_msb, self.__txba_tahi_lsb)
    @txba_tahi.setter
    def txba_tahi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txba_tahi_msb, self.__txba_tahi_lsb, value)
class MACTXBA_TALO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x2c0
        self.__txba_talo_lsb = 0
        self.__txba_talo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txba_talo(self):
        return self.__MEM.rdm(self.__addr, self.__txba_talo_msb, self.__txba_talo_lsb)
    @txba_talo.setter
    def txba_talo(self, value):
        return self.__MEM.wrm(self.__addr, self.__txba_talo_msb, self.__txba_talo_lsb, value)
class MACTXBA_SSN(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x2c4
        self.__txba_tid_lsb = 12
        self.__txba_tid_msb = 15
        self.__txba_ssn_lsb = 0
        self.__txba_ssn_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txba_tid(self):
        return self.__MEM.rdm(self.__addr, self.__txba_tid_msb, self.__txba_tid_lsb)
    @txba_tid.setter
    def txba_tid(self, value):
        return self.__MEM.wrm(self.__addr, self.__txba_tid_msb, self.__txba_tid_lsb, value)

    @property
    def txba_ssn(self):
        return self.__MEM.rdm(self.__addr, self.__txba_ssn_msb, self.__txba_ssn_lsb)
    @txba_ssn.setter
    def txba_ssn(self, value):
        return self.__MEM.wrm(self.__addr, self.__txba_ssn_msb, self.__txba_ssn_lsb, value)
class MACRX_ANT_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x2c8
        self.__reg_rxtxant_last_lsb = 5
        self.__reg_rxtxant_last_msb = 5
        self.__reg_rxtxant_value_lsb = 4
        self.__reg_rxtxant_value_msb = 4
        self.__reg_rxtxant_force_lsb = 3
        self.__reg_rxtxant_force_msb = 3
        self.__reg_rxant_last_lsb = 2
        self.__reg_rxant_last_msb = 2
        self.__reg_rxant_value_lsb = 1
        self.__reg_rxant_value_msb = 1
        self.__reg_rxant_force_lsb = 0
        self.__reg_rxant_force_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxtxant_last(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxtxant_last_msb, self.__reg_rxtxant_last_lsb)
    @reg_rxtxant_last.setter
    def reg_rxtxant_last(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxtxant_last_msb, self.__reg_rxtxant_last_lsb, value)

    @property
    def reg_rxtxant_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxtxant_value_msb, self.__reg_rxtxant_value_lsb)
    @reg_rxtxant_value.setter
    def reg_rxtxant_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxtxant_value_msb, self.__reg_rxtxant_value_lsb, value)

    @property
    def reg_rxtxant_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxtxant_force_msb, self.__reg_rxtxant_force_lsb)
    @reg_rxtxant_force.setter
    def reg_rxtxant_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxtxant_force_msb, self.__reg_rxtxant_force_lsb, value)

    @property
    def reg_rxant_last(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxant_last_msb, self.__reg_rxant_last_lsb)
    @reg_rxant_last.setter
    def reg_rxant_last(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxant_last_msb, self.__reg_rxant_last_lsb, value)

    @property
    def reg_rxant_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxant_value_msb, self.__reg_rxant_value_lsb)
    @reg_rxant_value.setter
    def reg_rxant_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxant_value_msb, self.__reg_rxant_value_lsb, value)

    @property
    def reg_rxant_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxant_force_msb, self.__reg_rxant_force_lsb)
    @reg_rxant_force.setter
    def reg_rxant_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxant_force_msb, self.__reg_rxant_force_lsb, value)
class MACRX_STATIS_CLEAR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x2cc
        self.__reg_rx_statis_ena_lsb = 1
        self.__reg_rx_statis_ena_msb = 1
        self.__reg_rx_statis_clear_lsb = 0
        self.__reg_rx_statis_clear_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rx_statis_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_statis_ena_msb, self.__reg_rx_statis_ena_lsb)
    @reg_rx_statis_ena.setter
    def reg_rx_statis_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_statis_ena_msb, self.__reg_rx_statis_ena_lsb, value)

    @property
    def reg_rx_statis_clear(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_statis_clear_msb, self.__reg_rx_statis_clear_lsb)
    @reg_rx_statis_clear.setter
    def reg_rx_statis_clear(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_statis_clear_msb, self.__reg_rx_statis_clear_lsb, value)
class MACRX_CCK_ERRCNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x2d0
        self.__rxcck_err_cnt_lsb = 0
        self.__rxcck_err_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxcck_err_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rxcck_err_cnt_msb, self.__rxcck_err_cnt_lsb)
    @rxcck_err_cnt.setter
    def rxcck_err_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxcck_err_cnt_msb, self.__rxcck_err_cnt_lsb, value)
class MACRX_OFDM_ERRCNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x2d4
        self.__rxofdm_err_cnt_lsb = 0
        self.__rxofdm_err_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxofdm_err_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rxofdm_err_cnt_msb, self.__rxofdm_err_cnt_lsb)
    @rxofdm_err_cnt.setter
    def rxofdm_err_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxofdm_err_cnt_msb, self.__rxofdm_err_cnt_lsb, value)
class MACRX_AGC_ERRCNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x2d8
        self.__rxagc_err_cnt_lsb = 0
        self.__rxagc_err_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxagc_err_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rxagc_err_cnt_msb, self.__rxagc_err_cnt_lsb)
    @rxagc_err_cnt.setter
    def rxagc_err_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxagc_err_cnt_msb, self.__rxagc_err_cnt_lsb, value)
class MACRX_SF_CNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x2dc
        self.__rxsf_cnt_lsb = 0
        self.__rxsf_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxsf_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rxsf_cnt_msb, self.__rxsf_cnt_lsb)
    @rxsf_cnt.setter
    def rxsf_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxsf_cnt_msb, self.__rxsf_cnt_lsb, value)
class MACRX_ABORT_CNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x2e0
        self.__rxabort_cnt_lsb = 0
        self.__rxabort_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxabort_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rxabort_cnt_msb, self.__rxabort_cnt_lsb)
    @rxabort_cnt.setter
    def rxabort_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxabort_cnt_msb, self.__rxabort_cnt_lsb, value)
class MACRX_FCS_ERRCNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x2e4
        self.__rxfcs_err_cnt_lsb = 0
        self.__rxfcs_err_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxfcs_err_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rxfcs_err_cnt_msb, self.__rxfcs_err_cnt_lsb)
    @rxfcs_err_cnt.setter
    def rxfcs_err_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxfcs_err_cnt_msb, self.__rxfcs_err_cnt_lsb, value)
class MACRX_FIFO_OVFCNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x2e8
        self.__rxfifo_ovf_cnt_lsb = 0
        self.__rxfifo_ovf_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxfifo_ovf_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rxfifo_ovf_cnt_msb, self.__rxfifo_ovf_cnt_lsb)
    @rxfifo_ovf_cnt.setter
    def rxfifo_ovf_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxfifo_ovf_cnt_msb, self.__rxfifo_ovf_cnt_lsb, value)
class MACRX_APENTRYBUF_FULLCNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x2ec
        self.__rxapentrybuf_full_cnt_lsb = 0
        self.__rxapentrybuf_full_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxapentrybuf_full_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rxapentrybuf_full_cnt_msb, self.__rxapentrybuf_full_cnt_lsb)
    @rxapentrybuf_full_cnt.setter
    def rxapentrybuf_full_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxapentrybuf_full_cnt_msb, self.__rxapentrybuf_full_cnt_lsb, value)
class MACRX_BUF_FULLCNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x2f0
        self.__rxbuf_full_cnt_lsb = 0
        self.__rxbuf_full_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxbuf_full_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rxbuf_full_cnt_msb, self.__rxbuf_full_cnt_lsb)
    @rxbuf_full_cnt.setter
    def rxbuf_full_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxbuf_full_cnt_msb, self.__rxbuf_full_cnt_lsb, value)
class MACRX_OTHER_UNICASTCNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x2f4
        self.__rxother_unicast_cnt_lsb = 0
        self.__rxother_unicast_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxother_unicast_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rxother_unicast_cnt_msb, self.__rxother_unicast_cnt_lsb)
    @rxother_unicast_cnt.setter
    def rxother_unicast_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxother_unicast_cnt_msb, self.__rxother_unicast_cnt_lsb, value)
class MACRX_TKIP_ERRCNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x2f8
        self.__rxtkip_err_cnt_lsb = 0
        self.__rxtkip_err_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxtkip_err_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rxtkip_err_cnt_msb, self.__rxtkip_err_cnt_lsb)
    @rxtkip_err_cnt.setter
    def rxtkip_err_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxtkip_err_cnt_msb, self.__rxtkip_err_cnt_lsb, value)
class MACRX_SAMEBM_ERRCNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x2fc
        self.__rxsamebm_err_cnt_lsb = 0
        self.__rxsamebm_err_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxsamebm_err_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rxsamebm_err_cnt_msb, self.__rxsamebm_err_cnt_lsb)
    @rxsamebm_err_cnt.setter
    def rxsamebm_err_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxsamebm_err_cnt_msb, self.__rxsamebm_err_cnt_lsb, value)
class MACRXACK_INT_CNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x300
        self.__rxackint_cnt_lsb = 0
        self.__rxackint_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxackint_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rxackint_cnt_msb, self.__rxackint_cnt_lsb)
    @rxackint_cnt.setter
    def rxackint_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxackint_cnt_msb, self.__rxackint_cnt_lsb, value)
class MACRXRTS_INT_CNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x304
        self.__rxrtsint_cnt_lsb = 0
        self.__rxrtsint_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxrtsint_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rxrtsint_cnt_msb, self.__rxrtsint_cnt_lsb)
    @rxrtsint_cnt.setter
    def rxrtsint_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxrtsint_cnt_msb, self.__rxrtsint_cnt_lsb, value)
class MACRXCTS_INT_CNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x308
        self.__rxctsint_cnt_lsb = 0
        self.__rxctsint_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxctsint_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rxctsint_cnt_msb, self.__rxctsint_cnt_lsb)
    @rxctsint_cnt.setter
    def rxctsint_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxctsint_cnt_msb, self.__rxctsint_cnt_lsb, value)
class MACRXRIFS_INT_CNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x30c
        self.__rxrifsint_cnt_lsb = 0
        self.__rxrifsint_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxrifsint_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rxrifsint_cnt_msb, self.__rxrifsint_cnt_lsb)
    @rxrifsint_cnt.setter
    def rxrifsint_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxrifsint_cnt_msb, self.__rxrifsint_cnt_lsb, value)
class MACRX_DATASUC_CNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x310
        self.__rxdata_suc_cnt_lsb = 0
        self.__rxdata_suc_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxdata_suc_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rxdata_suc_cnt_msb, self.__rxdata_suc_cnt_lsb)
    @rxdata_suc_cnt.setter
    def rxdata_suc_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxdata_suc_cnt_msb, self.__rxdata_suc_cnt_lsb, value)
class MACRX_END_CNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x314
        self.__rxend_cnt_lsb = 0
        self.__rxend_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxend_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_cnt_msb, self.__rxend_cnt_lsb)
    @rxend_cnt.setter
    def rxend_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_cnt_msb, self.__rxend_cnt_lsb, value)
class MACRX_BTBLOCK_ERR_CNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x318
        self.__rxbtblock_err_cnt_lsb = 0
        self.__rxbtblock_err_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxbtblock_err_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rxbtblock_err_cnt_msb, self.__rxbtblock_err_cnt_lsb)
    @rxbtblock_err_cnt.setter
    def rxbtblock_err_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxbtblock_err_cnt_msb, self.__rxbtblock_err_cnt_lsb, value)
class MACRX_FREQHOP_ERR_CNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x31c
        self.__rxfreq_hop_err_cnt_lsb = 0
        self.__rxfreq_hop_err_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxfreq_hop_err_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rxfreq_hop_err_cnt_msb, self.__rxfreq_hop_err_cnt_lsb)
    @rxfreq_hop_err_cnt.setter
    def rxfreq_hop_err_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxfreq_hop_err_cnt_msb, self.__rxfreq_hop_err_cnt_lsb, value)
class MACRX_LASTUNMATCH_ERR_CNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x320
        self.__rxlast_unmatch_err_cnt_lsb = 0
        self.__rxlast_unmatch_err_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxlast_unmatch_err_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rxlast_unmatch_err_cnt_msb, self.__rxlast_unmatch_err_cnt_lsb)
    @rxlast_unmatch_err_cnt.setter
    def rxlast_unmatch_err_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxlast_unmatch_err_cnt_msb, self.__rxlast_unmatch_err_cnt_lsb, value)
class MACRX_BLOCK_ERR_CNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x324
        self.__rxblock_err_cnt_lsb = 0
        self.__rxblock_err_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxblock_err_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rxblock_err_cnt_msb, self.__rxblock_err_cnt_lsb)
    @rxblock_err_cnt.setter
    def rxblock_err_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxblock_err_cnt_msb, self.__rxblock_err_cnt_lsb, value)
class MACRXFRAME_LOWTO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x328
        self.__reg_rxframe_lowto_ena_lsb = 31
        self.__reg_rxframe_lowto_ena_msb = 31
        self.__reg_rxframe_lowto_timer_lsb = 0
        self.__reg_rxframe_lowto_timer_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxframe_lowto_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxframe_lowto_ena_msb, self.__reg_rxframe_lowto_ena_lsb)
    @reg_rxframe_lowto_ena.setter
    def reg_rxframe_lowto_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxframe_lowto_ena_msb, self.__reg_rxframe_lowto_ena_lsb, value)

    @property
    def reg_rxframe_lowto_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxframe_lowto_timer_msb, self.__reg_rxframe_lowto_timer_lsb)
    @reg_rxframe_lowto_timer.setter
    def reg_rxframe_lowto_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxframe_lowto_timer_msb, self.__reg_rxframe_lowto_timer_lsb, value)
class MACRX_ERRTO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x32c
        self.__reg_rxerr_to_ena_lsb = 31
        self.__reg_rxerr_to_ena_msb = 31
        self.__reg_fcserr_only_lsb = 30
        self.__reg_fcserr_only_msb = 30
        self.__reg_rxerr_to_timer_lsb = 0
        self.__reg_rxerr_to_timer_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxerr_to_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxerr_to_ena_msb, self.__reg_rxerr_to_ena_lsb)
    @reg_rxerr_to_ena.setter
    def reg_rxerr_to_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxerr_to_ena_msb, self.__reg_rxerr_to_ena_lsb, value)

    @property
    def reg_fcserr_only(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fcserr_only_msb, self.__reg_fcserr_only_lsb)
    @reg_fcserr_only.setter
    def reg_fcserr_only(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fcserr_only_msb, self.__reg_fcserr_only_lsb, value)

    @property
    def reg_rxerr_to_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxerr_to_timer_msb, self.__reg_rxerr_to_timer_lsb)
    @reg_rxerr_to_timer.setter
    def reg_rxerr_to_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxerr_to_timer_msb, self.__reg_rxerr_to_timer_lsb, value)
class MACRX_AHB(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x330
        self.__reg_rxestburst_max_len_lsb = 8
        self.__reg_rxestburst_max_len_msb = 11
        self.__reg_rxdscrburst_max_len_lsb = 4
        self.__reg_rxdscrburst_max_len_msb = 7
        self.__reg_rxburst_max_len_lsb = 0
        self.__reg_rxburst_max_len_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxestburst_max_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxestburst_max_len_msb, self.__reg_rxestburst_max_len_lsb)
    @reg_rxestburst_max_len.setter
    def reg_rxestburst_max_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxestburst_max_len_msb, self.__reg_rxestburst_max_len_lsb, value)

    @property
    def reg_rxdscrburst_max_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdscrburst_max_len_msb, self.__reg_rxdscrburst_max_len_lsb)
    @reg_rxdscrburst_max_len.setter
    def reg_rxdscrburst_max_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdscrburst_max_len_msb, self.__reg_rxdscrburst_max_len_lsb, value)

    @property
    def reg_rxburst_max_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxburst_max_len_msb, self.__reg_rxburst_max_len_lsb)
    @reg_rxburst_max_len.setter
    def reg_rxburst_max_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxburst_max_len_msb, self.__reg_rxburst_max_len_lsb, value)
class MACDIAG4(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x334
        self.__mac_rx_diag0_lsb = 0
        self.__mac_rx_diag0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def mac_rx_diag0(self):
        return self.__MEM.rdm(self.__addr, self.__mac_rx_diag0_msb, self.__mac_rx_diag0_lsb)
    @mac_rx_diag0.setter
    def mac_rx_diag0(self, value):
        return self.__MEM.wrm(self.__addr, self.__mac_rx_diag0_msb, self.__mac_rx_diag0_lsb, value)
class MACDIAG5(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x338
        self.__mac_rx_diag1_lsb = 0
        self.__mac_rx_diag1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def mac_rx_diag1(self):
        return self.__MEM.rdm(self.__addr, self.__mac_rx_diag1_msb, self.__mac_rx_diag1_lsb)
    @mac_rx_diag1.setter
    def mac_rx_diag1(self, value):
        return self.__MEM.wrm(self.__addr, self.__mac_rx_diag1_msb, self.__mac_rx_diag1_lsb, value)
class MACDIAG6(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x33c
        self.__mac_rx_diag2_lsb = 0
        self.__mac_rx_diag2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def mac_rx_diag2(self):
        return self.__MEM.rdm(self.__addr, self.__mac_rx_diag2_msb, self.__mac_rx_diag2_lsb)
    @mac_rx_diag2.setter
    def mac_rx_diag2(self, value):
        return self.__MEM.wrm(self.__addr, self.__mac_rx_diag2_msb, self.__mac_rx_diag2_lsb, value)
class MACDIAG7(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x340
        self.__mac_rx_diag3_lsb = 0
        self.__mac_rx_diag3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def mac_rx_diag3(self):
        return self.__MEM.rdm(self.__addr, self.__mac_rx_diag3_msb, self.__mac_rx_diag3_lsb)
    @mac_rx_diag3.setter
    def mac_rx_diag3(self, value):
        return self.__MEM.wrm(self.__addr, self.__mac_rx_diag3_msb, self.__mac_rx_diag3_lsb, value)
class MACRXDATE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_RX_BASE + 0x3f8
        self.__reg_macrx_date_lsb = 0
        self.__reg_macrx_date_msb = 27
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macrx_date(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macrx_date_msb, self.__reg_macrx_date_lsb)
    @reg_macrx_date.setter
    def reg_macrx_date(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macrx_date_msb, self.__reg_macrx_date_lsb, value)
    @property
    def default_value(self):
        return 0x1810081
