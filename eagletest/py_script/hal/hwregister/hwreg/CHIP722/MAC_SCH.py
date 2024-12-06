from hal.common import *
from hal.hwregister.hwreg.CHIP722.addr_base import *
class MAC_SCH(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.MACGPO = MACGPO(self.channel, self.chipv)
        self.MACNAV = MACNAV(self.channel, self.chipv)
        self.MACNAVTARGET = MACNAVTARGET(self.channel, self.chipv)
        self.MACNAVSTART = MACNAVSTART(self.channel, self.chipv)
        self.MACBBRXHUNG = MACBBRXHUNG(self.channel, self.chipv)
        self.MACBBTXHUNG = MACBBTXHUNG(self.channel, self.chipv)
        self.MACBBCCAHUNG = MACBBCCAHUNG(self.channel, self.chipv)
        self.INT1_NMI_MAC = INT1_NMI_MAC(self.channel, self.chipv)
        self.INT1_ENA_MAC = INT1_ENA_MAC(self.channel, self.chipv)
        self.INT1_RAW_MAC = INT1_RAW_MAC(self.channel, self.chipv)
        self.INT1_ST_MAC = INT1_ST_MAC(self.channel, self.chipv)
        self.INT1_CLR_MAC = INT1_CLR_MAC(self.channel, self.chipv)
        self.INT_NMI_MAC = INT_NMI_MAC(self.channel, self.chipv)
        self.INT_ENA_MAC = INT_ENA_MAC(self.channel, self.chipv)
        self.INT_RAW_MAC = INT_RAW_MAC(self.channel, self.chipv)
        self.INT_ST_MAC = INT_ST_MAC(self.channel, self.chipv)
        self.INT_CLR_MAC = INT_CLR_MAC(self.channel, self.chipv)
        self.MACSLOT = MACSLOT(self.channel, self.chipv)
        self.MACDELAY = MACDELAY(self.channel, self.chipv)
        self.MACBB_INIT_VALUE = MACBB_INIT_VALUE(self.channel, self.chipv)
        self.MACHUNGRECOVER = MACHUNGRECOVER(self.channel, self.chipv)
        self.MACHUNGSTATE = MACHUNGSTATE(self.channel, self.chipv)
        self.MACAHBMTEST = MACAHBMTEST(self.channel, self.chipv)
        self.MACTXPMD = MACTXPMD(self.channel, self.chipv)
        self.MACOPTIONS = MACOPTIONS(self.channel, self.chipv)
        self.MACSECOND_CCACONF = MACSECOND_CCACONF(self.channel, self.chipv)
        self.MACRXTXOPTION = MACRXTXOPTION(self.channel, self.chipv)
        self.MACAUTOTXRX_ENA = MACAUTOTXRX_ENA(self.channel, self.chipv)
        self.MACTXRX_TAB0 = MACTXRX_TAB0(self.channel, self.chipv)
        self.MACTXRX_TAB1 = MACTXRX_TAB1(self.channel, self.chipv)
        self.MACTXRX_TAB2 = MACTXRX_TAB2(self.channel, self.chipv)
        self.MACTXRX_TAB3 = MACTXRX_TAB3(self.channel, self.chipv)
        self.MACTXRX_TAB4 = MACTXRX_TAB4(self.channel, self.chipv)
        self.MACTXRX_TAB5 = MACTXRX_TAB5(self.channel, self.chipv)
        self.MACTXRX_QNUM = MACTXRX_QNUM(self.channel, self.chipv)
        self.MACTXTARGET = MACTXTARGET(self.channel, self.chipv)
        self.MACTXTARGET_ENA = MACTXTARGET_ENA(self.channel, self.chipv)
        self.MACTXQ_BLOCK = MACTXQ_BLOCK(self.channel, self.chipv)
        self.MACTXSTATE_CLR = MACTXSTATE_CLR(self.channel, self.chipv)
        self.MACTXSTATE = MACTXSTATE(self.channel, self.chipv)
        self.MACTXENA_ST_CLR = MACTXENA_ST_CLR(self.channel, self.chipv)
        self.MACTXENA_ST = MACTXENA_ST(self.channel, self.chipv)
        self.MACTXIMR2_CONF = MACTXIMR2_CONF(self.channel, self.chipv)
        self.MACTXIMR2_PLCP0 = MACTXIMR2_PLCP0(self.channel, self.chipv)
        self.MACTXIMR1_CONF = MACTXIMR1_CONF(self.channel, self.chipv)
        self.MACTXIMR1_PLCP0 = MACTXIMR1_PLCP0(self.channel, self.chipv)
        self.MACTXIMR0_CONF = MACTXIMR0_CONF(self.channel, self.chipv)
        self.MACTXIMR0_PLCP0 = MACTXIMR0_PLCP0(self.channel, self.chipv)
        self.MACTXQ7_CONF = MACTXQ7_CONF(self.channel, self.chipv)
        self.MACTXQ7_PLCP0 = MACTXQ7_PLCP0(self.channel, self.chipv)
        self.MACTXQ6_CONF = MACTXQ6_CONF(self.channel, self.chipv)
        self.MACTXQ6_PLCP0 = MACTXQ6_PLCP0(self.channel, self.chipv)
        self.MACTXQ5_CONF = MACTXQ5_CONF(self.channel, self.chipv)
        self.MACTXQ5_PLCP0 = MACTXQ5_PLCP0(self.channel, self.chipv)
        self.MACTXQ4_CONF = MACTXQ4_CONF(self.channel, self.chipv)
        self.MACTXQ4_PLCP0 = MACTXQ4_PLCP0(self.channel, self.chipv)
        self.MACTXQ3_CONF = MACTXQ3_CONF(self.channel, self.chipv)
        self.MACTXQ3_PLCP0 = MACTXQ3_PLCP0(self.channel, self.chipv)
        self.MACTXQ2_CONF = MACTXQ2_CONF(self.channel, self.chipv)
        self.MACTXQ2_PLCP0 = MACTXQ2_PLCP0(self.channel, self.chipv)
        self.MACTXQ1_CONF = MACTXQ1_CONF(self.channel, self.chipv)
        self.MACTXQ1_PLCP0 = MACTXQ1_PLCP0(self.channel, self.chipv)
        self.MACTXQ0_CONF = MACTXQ0_CONF(self.channel, self.chipv)
        self.MACTXQ0_PLCP0 = MACTXQ0_PLCP0(self.channel, self.chipv)
        self.MACTXQ_PTI_CONF = MACTXQ_PTI_CONF(self.channel, self.chipv)
        self.MACTXQ_PRIO_CONF = MACTXQ_PRIO_CONF(self.channel, self.chipv)
        self.MACTXQMEM = MACTXQMEM(self.channel, self.chipv)
        self.MACTXSEQ_NUM = MACTXSEQ_NUM(self.channel, self.chipv)
        self.MACTX_HOLD = MACTX_HOLD(self.channel, self.chipv)
        self.MACDURSIFS = MACDURSIFS(self.channel, self.chipv)
        self.MACTIMER_TAR0_ENA = MACTIMER_TAR0_ENA(self.channel, self.chipv)
        self.MACTIMER_TAR0 = MACTIMER_TAR0(self.channel, self.chipv)
        self.MACTIMER_TAR1_ENA = MACTIMER_TAR1_ENA(self.channel, self.chipv)
        self.MACTIMER_TAR1 = MACTIMER_TAR1(self.channel, self.chipv)
        self.MACTXRTS_INT_CNT = MACTXRTS_INT_CNT(self.channel, self.chipv)
        self.MACTXCTS_INT_CNT = MACTXCTS_INT_CNT(self.channel, self.chipv)
        self.MACTXRXACK_INT_CNT = MACTXRXACK_INT_CNT(self.channel, self.chipv)
        self.MACTXRXCTS_INT_CNT = MACTXRXCTS_INT_CNT(self.channel, self.chipv)
        self.MACRXTRIGGER_CNT = MACRXTRIGGER_CNT(self.channel, self.chipv)
        self.MACRXTXHUNG_CNT = MACRXTXHUNG_CNT(self.channel, self.chipv)
        self.MACRXTXPANIC_CNT = MACRXTXPANIC_CNT(self.channel, self.chipv)
        self.MACRSSI_STATIS = MACRSSI_STATIS(self.channel, self.chipv)
        self.MACRXEND_CCACNT = MACRXEND_CCACNT(self.channel, self.chipv)
        self.MACCHAN_STATIS = MACCHAN_STATIS(self.channel, self.chipv)
        self.MACEVT_STATIS0 = MACEVT_STATIS0(self.channel, self.chipv)
        self.MACEVT_STATIS1 = MACEVT_STATIS1(self.channel, self.chipv)
        self.MACEVT_STATIS2 = MACEVT_STATIS2(self.channel, self.chipv)
        self.MACEVT_STATIS3 = MACEVT_STATIS3(self.channel, self.chipv)
        self.MACADCDUMP0 = MACADCDUMP0(self.channel, self.chipv)
        self.MACADCDUMP1 = MACADCDUMP1(self.channel, self.chipv)
        self.MACTOADCDUMP0 = MACTOADCDUMP0(self.channel, self.chipv)
        self.MACTXQ_NOENABLE_US = MACTXQ_NOENABLE_US(self.channel, self.chipv)
        self.MACBB_CCA_IND_US = MACBB_CCA_IND_US(self.channel, self.chipv)
        self.MACCCA_CNT = MACCCA_CNT(self.channel, self.chipv)
        self.MACCCA_RXFRAM_CNT = MACCCA_RXFRAM_CNT(self.channel, self.chipv)
        self.MACDIAG0 = MACDIAG0(self.channel, self.chipv)
        self.MACDIAG1 = MACDIAG1(self.channel, self.chipv)
        self.MACDIAG2 = MACDIAG2(self.channel, self.chipv)
        self.MACDIAG3 = MACDIAG3(self.channel, self.chipv)
        self.MACDIAG_SEL = MACDIAG_SEL(self.channel, self.chipv)
        self.MACTXDUMP = MACTXDUMP(self.channel, self.chipv)
        self.MACADCDUMP2 = MACADCDUMP2(self.channel, self.chipv)
        self.MACSIM_FINISH = MACSIM_FINISH(self.channel, self.chipv)
        self.MACTXENA_TO = MACTXENA_TO(self.channel, self.chipv)
        self.MACRXSTART_TIME = MACRXSTART_TIME(self.channel, self.chipv)
        self.MACRXEND_TIME = MACRXEND_TIME(self.channel, self.chipv)
        self.MACTXSTART_TIME = MACTXSTART_TIME(self.channel, self.chipv)
        self.MACTXEND_TIME = MACTXEND_TIME(self.channel, self.chipv)
        self.MACSCHDATE = MACSCHDATE(self.channel, self.chipv)
        self.MACID = MACID(self.channel, self.chipv)
class MACGPO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x0
        self.__reg_macgpo_lsb = 0
        self.__reg_macgpo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macgpo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macgpo_msb, self.__reg_macgpo_lsb)
    @reg_macgpo.setter
    def reg_macgpo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macgpo_msb, self.__reg_macgpo_lsb, value)
class MACNAV(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x4
        self.__reg_navenable_lsb = 30
        self.__reg_navenable_msb = 30
        self.__reg_nav_lsb = 0
        self.__reg_nav_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_navenable(self):
        return self.__MEM.rdm(self.__addr, self.__reg_navenable_msb, self.__reg_navenable_lsb)
    @reg_navenable.setter
    def reg_navenable(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_navenable_msb, self.__reg_navenable_lsb, value)

    @property
    def reg_nav(self):
        return self.__MEM.rdm(self.__addr, self.__reg_nav_msb, self.__reg_nav_lsb)
    @reg_nav.setter
    def reg_nav(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_nav_msb, self.__reg_nav_lsb, value)
class MACNAVTARGET(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x8
        self.__reg_navtarget_lsb = 0
        self.__reg_navtarget_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_navtarget(self):
        return self.__MEM.rdm(self.__addr, self.__reg_navtarget_msb, self.__reg_navtarget_lsb)
    @reg_navtarget.setter
    def reg_navtarget(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_navtarget_msb, self.__reg_navtarget_lsb, value)
class MACNAVSTART(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0xc
        self.__reg_navstart_lsb = 0
        self.__reg_navstart_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_navstart(self):
        return self.__MEM.rdm(self.__addr, self.__reg_navstart_msb, self.__reg_navstart_lsb)
    @reg_navstart.setter
    def reg_navstart(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_navstart_msb, self.__reg_navstart_lsb, value)
class MACBBRXHUNG(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x10
        self.__reg_bbrxhung_ena_lsb = 31
        self.__reg_bbrxhung_ena_msb = 31
        self.__reg_nosuportrate_option_lsb = 30
        self.__reg_nosuportrate_option_msb = 30
        self.__reg_bbrxhung_time_lsb = 0
        self.__reg_bbrxhung_time_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bbrxhung_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbrxhung_ena_msb, self.__reg_bbrxhung_ena_lsb)
    @reg_bbrxhung_ena.setter
    def reg_bbrxhung_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbrxhung_ena_msb, self.__reg_bbrxhung_ena_lsb, value)

    @property
    def reg_nosuportrate_option(self):
        return self.__MEM.rdm(self.__addr, self.__reg_nosuportrate_option_msb, self.__reg_nosuportrate_option_lsb)
    @reg_nosuportrate_option.setter
    def reg_nosuportrate_option(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_nosuportrate_option_msb, self.__reg_nosuportrate_option_lsb, value)

    @property
    def reg_bbrxhung_time(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbrxhung_time_msb, self.__reg_bbrxhung_time_lsb)
    @reg_bbrxhung_time.setter
    def reg_bbrxhung_time(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbrxhung_time_msb, self.__reg_bbrxhung_time_lsb, value)
class MACBBTXHUNG(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x14
        self.__reg_bbtxhung_ena_lsb = 31
        self.__reg_bbtxhung_ena_msb = 31
        self.__reg_bbtxhung_time_lsb = 0
        self.__reg_bbtxhung_time_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bbtxhung_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbtxhung_ena_msb, self.__reg_bbtxhung_ena_lsb)
    @reg_bbtxhung_ena.setter
    def reg_bbtxhung_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbtxhung_ena_msb, self.__reg_bbtxhung_ena_lsb, value)

    @property
    def reg_bbtxhung_time(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbtxhung_time_msb, self.__reg_bbtxhung_time_lsb)
    @reg_bbtxhung_time.setter
    def reg_bbtxhung_time(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbtxhung_time_msb, self.__reg_bbtxhung_time_lsb, value)
class MACBBCCAHUNG(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x18
        self.__reg_bbccahung_ena_lsb = 31
        self.__reg_bbccahung_ena_msb = 31
        self.__reg_bbccahung_time_lsb = 0
        self.__reg_bbccahung_time_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bbccahung_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbccahung_ena_msb, self.__reg_bbccahung_ena_lsb)
    @reg_bbccahung_ena.setter
    def reg_bbccahung_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbccahung_ena_msb, self.__reg_bbccahung_ena_lsb, value)

    @property
    def reg_bbccahung_time(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbccahung_time_msb, self.__reg_bbccahung_time_lsb)
    @reg_bbccahung_time.setter
    def reg_bbccahung_time(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbccahung_time_msb, self.__reg_bbccahung_time_lsb, value)
class INT1_NMI_MAC(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x1c
        self.__txto_int_nmi_lsb = 9
        self.__txto_int_nmi_msb = 9
        self.__txend_data_int_nmi_lsb = 8
        self.__txend_data_int_nmi_msb = 8
        self.__txend_cts_int_nmi_lsb = 7
        self.__txend_cts_int_nmi_msb = 7
        self.__txend_rts_int_nmi_lsb = 6
        self.__txend_rts_int_nmi_msb = 6
        self.__rxend_txack_int_nmi_lsb = 5
        self.__rxend_txack_int_nmi_msb = 5
        self.__rxend_txcts_int_nmi_lsb = 4
        self.__rxend_txcts_int_nmi_msb = 4
        self.__rxend_data_int_nmi_lsb = 3
        self.__rxend_data_int_nmi_msb = 3
        self.__rxsuc_int_nmi_lsb = 2
        self.__rxsuc_int_nmi_msb = 2
        self.__imrto_int_nmi_lsb = 1
        self.__imrto_int_nmi_msb = 1
        self.__rxto_int_nmi_lsb = 0
        self.__rxto_int_nmi_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txto_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__txto_int_nmi_msb, self.__txto_int_nmi_lsb)
    @txto_int_nmi.setter
    def txto_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txto_int_nmi_msb, self.__txto_int_nmi_lsb, value)

    @property
    def txend_data_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__txend_data_int_nmi_msb, self.__txend_data_int_nmi_lsb)
    @txend_data_int_nmi.setter
    def txend_data_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txend_data_int_nmi_msb, self.__txend_data_int_nmi_lsb, value)

    @property
    def txend_cts_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__txend_cts_int_nmi_msb, self.__txend_cts_int_nmi_lsb)
    @txend_cts_int_nmi.setter
    def txend_cts_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txend_cts_int_nmi_msb, self.__txend_cts_int_nmi_lsb, value)

    @property
    def txend_rts_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__txend_rts_int_nmi_msb, self.__txend_rts_int_nmi_lsb)
    @txend_rts_int_nmi.setter
    def txend_rts_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txend_rts_int_nmi_msb, self.__txend_rts_int_nmi_lsb, value)

    @property
    def rxend_txack_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_txack_int_nmi_msb, self.__rxend_txack_int_nmi_lsb)
    @rxend_txack_int_nmi.setter
    def rxend_txack_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_txack_int_nmi_msb, self.__rxend_txack_int_nmi_lsb, value)

    @property
    def rxend_txcts_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_txcts_int_nmi_msb, self.__rxend_txcts_int_nmi_lsb)
    @rxend_txcts_int_nmi.setter
    def rxend_txcts_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_txcts_int_nmi_msb, self.__rxend_txcts_int_nmi_lsb, value)

    @property
    def rxend_data_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_data_int_nmi_msb, self.__rxend_data_int_nmi_lsb)
    @rxend_data_int_nmi.setter
    def rxend_data_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_data_int_nmi_msb, self.__rxend_data_int_nmi_lsb, value)

    @property
    def rxsuc_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__rxsuc_int_nmi_msb, self.__rxsuc_int_nmi_lsb)
    @rxsuc_int_nmi.setter
    def rxsuc_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxsuc_int_nmi_msb, self.__rxsuc_int_nmi_lsb, value)

    @property
    def imrto_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__imrto_int_nmi_msb, self.__imrto_int_nmi_lsb)
    @imrto_int_nmi.setter
    def imrto_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__imrto_int_nmi_msb, self.__imrto_int_nmi_lsb, value)

    @property
    def rxto_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__rxto_int_nmi_msb, self.__rxto_int_nmi_lsb)
    @rxto_int_nmi.setter
    def rxto_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxto_int_nmi_msb, self.__rxto_int_nmi_lsb, value)
class INT1_ENA_MAC(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x20
        self.__txto_int_ena_lsb = 9
        self.__txto_int_ena_msb = 9
        self.__txend_data_int_ena_lsb = 8
        self.__txend_data_int_ena_msb = 8
        self.__txend_cts_int_ena_lsb = 7
        self.__txend_cts_int_ena_msb = 7
        self.__txend_rts_int_ena_lsb = 6
        self.__txend_rts_int_ena_msb = 6
        self.__rxend_txack_int_ena_lsb = 5
        self.__rxend_txack_int_ena_msb = 5
        self.__rxend_txcts_int_ena_lsb = 4
        self.__rxend_txcts_int_ena_msb = 4
        self.__rxend_data_int_ena_lsb = 3
        self.__rxend_data_int_ena_msb = 3
        self.__rxsuc_int_ena_lsb = 2
        self.__rxsuc_int_ena_msb = 2
        self.__imrto_int_ena_lsb = 1
        self.__imrto_int_ena_msb = 1
        self.__rxto_int_ena_lsb = 0
        self.__rxto_int_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txto_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__txto_int_ena_msb, self.__txto_int_ena_lsb)
    @txto_int_ena.setter
    def txto_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__txto_int_ena_msb, self.__txto_int_ena_lsb, value)

    @property
    def txend_data_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__txend_data_int_ena_msb, self.__txend_data_int_ena_lsb)
    @txend_data_int_ena.setter
    def txend_data_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__txend_data_int_ena_msb, self.__txend_data_int_ena_lsb, value)

    @property
    def txend_cts_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__txend_cts_int_ena_msb, self.__txend_cts_int_ena_lsb)
    @txend_cts_int_ena.setter
    def txend_cts_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__txend_cts_int_ena_msb, self.__txend_cts_int_ena_lsb, value)

    @property
    def txend_rts_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__txend_rts_int_ena_msb, self.__txend_rts_int_ena_lsb)
    @txend_rts_int_ena.setter
    def txend_rts_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__txend_rts_int_ena_msb, self.__txend_rts_int_ena_lsb, value)

    @property
    def rxend_txack_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_txack_int_ena_msb, self.__rxend_txack_int_ena_lsb)
    @rxend_txack_int_ena.setter
    def rxend_txack_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_txack_int_ena_msb, self.__rxend_txack_int_ena_lsb, value)

    @property
    def rxend_txcts_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_txcts_int_ena_msb, self.__rxend_txcts_int_ena_lsb)
    @rxend_txcts_int_ena.setter
    def rxend_txcts_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_txcts_int_ena_msb, self.__rxend_txcts_int_ena_lsb, value)

    @property
    def rxend_data_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_data_int_ena_msb, self.__rxend_data_int_ena_lsb)
    @rxend_data_int_ena.setter
    def rxend_data_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_data_int_ena_msb, self.__rxend_data_int_ena_lsb, value)

    @property
    def rxsuc_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rxsuc_int_ena_msb, self.__rxsuc_int_ena_lsb)
    @rxsuc_int_ena.setter
    def rxsuc_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxsuc_int_ena_msb, self.__rxsuc_int_ena_lsb, value)

    @property
    def imrto_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__imrto_int_ena_msb, self.__imrto_int_ena_lsb)
    @imrto_int_ena.setter
    def imrto_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__imrto_int_ena_msb, self.__imrto_int_ena_lsb, value)

    @property
    def rxto_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rxto_int_ena_msb, self.__rxto_int_ena_lsb)
    @rxto_int_ena.setter
    def rxto_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxto_int_ena_msb, self.__rxto_int_ena_lsb, value)
class INT1_RAW_MAC(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x24
        self.__txto_int_raw_lsb = 9
        self.__txto_int_raw_msb = 9
        self.__txend_data_int_raw_lsb = 8
        self.__txend_data_int_raw_msb = 8
        self.__txend_cts_int_raw_lsb = 7
        self.__txend_cts_int_raw_msb = 7
        self.__txend_rts_int_raw_lsb = 6
        self.__txend_rts_int_raw_msb = 6
        self.__rxend_txack_int_raw_lsb = 5
        self.__rxend_txack_int_raw_msb = 5
        self.__rxend_txcts_int_raw_lsb = 4
        self.__rxend_txcts_int_raw_msb = 4
        self.__rxend_data_int_raw_lsb = 3
        self.__rxend_data_int_raw_msb = 3
        self.__rxsuc_int_raw_lsb = 2
        self.__rxsuc_int_raw_msb = 2
        self.__imrto_int_raw_lsb = 1
        self.__imrto_int_raw_msb = 1
        self.__rxto_int_raw_lsb = 0
        self.__rxto_int_raw_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txto_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__txto_int_raw_msb, self.__txto_int_raw_lsb)
    @txto_int_raw.setter
    def txto_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__txto_int_raw_msb, self.__txto_int_raw_lsb, value)

    @property
    def txend_data_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__txend_data_int_raw_msb, self.__txend_data_int_raw_lsb)
    @txend_data_int_raw.setter
    def txend_data_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__txend_data_int_raw_msb, self.__txend_data_int_raw_lsb, value)

    @property
    def txend_cts_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__txend_cts_int_raw_msb, self.__txend_cts_int_raw_lsb)
    @txend_cts_int_raw.setter
    def txend_cts_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__txend_cts_int_raw_msb, self.__txend_cts_int_raw_lsb, value)

    @property
    def txend_rts_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__txend_rts_int_raw_msb, self.__txend_rts_int_raw_lsb)
    @txend_rts_int_raw.setter
    def txend_rts_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__txend_rts_int_raw_msb, self.__txend_rts_int_raw_lsb, value)

    @property
    def rxend_txack_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_txack_int_raw_msb, self.__rxend_txack_int_raw_lsb)
    @rxend_txack_int_raw.setter
    def rxend_txack_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_txack_int_raw_msb, self.__rxend_txack_int_raw_lsb, value)

    @property
    def rxend_txcts_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_txcts_int_raw_msb, self.__rxend_txcts_int_raw_lsb)
    @rxend_txcts_int_raw.setter
    def rxend_txcts_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_txcts_int_raw_msb, self.__rxend_txcts_int_raw_lsb, value)

    @property
    def rxend_data_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_data_int_raw_msb, self.__rxend_data_int_raw_lsb)
    @rxend_data_int_raw.setter
    def rxend_data_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_data_int_raw_msb, self.__rxend_data_int_raw_lsb, value)

    @property
    def rxsuc_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rxsuc_int_raw_msb, self.__rxsuc_int_raw_lsb)
    @rxsuc_int_raw.setter
    def rxsuc_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxsuc_int_raw_msb, self.__rxsuc_int_raw_lsb, value)

    @property
    def imrto_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__imrto_int_raw_msb, self.__imrto_int_raw_lsb)
    @imrto_int_raw.setter
    def imrto_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__imrto_int_raw_msb, self.__imrto_int_raw_lsb, value)

    @property
    def rxto_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rxto_int_raw_msb, self.__rxto_int_raw_lsb)
    @rxto_int_raw.setter
    def rxto_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxto_int_raw_msb, self.__rxto_int_raw_lsb, value)
class INT1_ST_MAC(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x28
        self.__txto_int_st_lsb = 9
        self.__txto_int_st_msb = 9
        self.__txend_data_int_st_lsb = 8
        self.__txend_data_int_st_msb = 8
        self.__txend_cts_int_st_lsb = 7
        self.__txend_cts_int_st_msb = 7
        self.__txend_rts_int_st_lsb = 6
        self.__txend_rts_int_st_msb = 6
        self.__rxend_txack_int_st_lsb = 5
        self.__rxend_txack_int_st_msb = 5
        self.__rxend_txcts_int_st_lsb = 4
        self.__rxend_txcts_int_st_msb = 4
        self.__rxend_data_int_st_lsb = 3
        self.__rxend_data_int_st_msb = 3
        self.__rxsuc_int_st_lsb = 2
        self.__rxsuc_int_st_msb = 2
        self.__imrto_int_st_lsb = 1
        self.__imrto_int_st_msb = 1
        self.__rxto_int_st_lsb = 0
        self.__rxto_int_st_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txto_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__txto_int_st_msb, self.__txto_int_st_lsb)
    @txto_int_st.setter
    def txto_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__txto_int_st_msb, self.__txto_int_st_lsb, value)

    @property
    def txend_data_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__txend_data_int_st_msb, self.__txend_data_int_st_lsb)
    @txend_data_int_st.setter
    def txend_data_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__txend_data_int_st_msb, self.__txend_data_int_st_lsb, value)

    @property
    def txend_cts_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__txend_cts_int_st_msb, self.__txend_cts_int_st_lsb)
    @txend_cts_int_st.setter
    def txend_cts_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__txend_cts_int_st_msb, self.__txend_cts_int_st_lsb, value)

    @property
    def txend_rts_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__txend_rts_int_st_msb, self.__txend_rts_int_st_lsb)
    @txend_rts_int_st.setter
    def txend_rts_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__txend_rts_int_st_msb, self.__txend_rts_int_st_lsb, value)

    @property
    def rxend_txack_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_txack_int_st_msb, self.__rxend_txack_int_st_lsb)
    @rxend_txack_int_st.setter
    def rxend_txack_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_txack_int_st_msb, self.__rxend_txack_int_st_lsb, value)

    @property
    def rxend_txcts_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_txcts_int_st_msb, self.__rxend_txcts_int_st_lsb)
    @rxend_txcts_int_st.setter
    def rxend_txcts_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_txcts_int_st_msb, self.__rxend_txcts_int_st_lsb, value)

    @property
    def rxend_data_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_data_int_st_msb, self.__rxend_data_int_st_lsb)
    @rxend_data_int_st.setter
    def rxend_data_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_data_int_st_msb, self.__rxend_data_int_st_lsb, value)

    @property
    def rxsuc_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rxsuc_int_st_msb, self.__rxsuc_int_st_lsb)
    @rxsuc_int_st.setter
    def rxsuc_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxsuc_int_st_msb, self.__rxsuc_int_st_lsb, value)

    @property
    def imrto_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__imrto_int_st_msb, self.__imrto_int_st_lsb)
    @imrto_int_st.setter
    def imrto_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__imrto_int_st_msb, self.__imrto_int_st_lsb, value)

    @property
    def rxto_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rxto_int_st_msb, self.__rxto_int_st_lsb)
    @rxto_int_st.setter
    def rxto_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxto_int_st_msb, self.__rxto_int_st_lsb, value)
class INT1_CLR_MAC(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x2c
        self.__txto_int_clr_lsb = 9
        self.__txto_int_clr_msb = 9
        self.__txend_data_int_clr_lsb = 8
        self.__txend_data_int_clr_msb = 8
        self.__txend_cts_int_clr_lsb = 7
        self.__txend_cts_int_clr_msb = 7
        self.__txend_rts_int_clr_lsb = 6
        self.__txend_rts_int_clr_msb = 6
        self.__rxend_txack_int_clr_lsb = 5
        self.__rxend_txack_int_clr_msb = 5
        self.__rxend_txcts_int_clr_lsb = 4
        self.__rxend_txcts_int_clr_msb = 4
        self.__rxend_data_int_clr_lsb = 3
        self.__rxend_data_int_clr_msb = 3
        self.__rxsuc_int_clr_lsb = 2
        self.__rxsuc_int_clr_msb = 2
        self.__imrto_int_clr_lsb = 1
        self.__imrto_int_clr_msb = 1
        self.__rxto_int_clr_lsb = 0
        self.__rxto_int_clr_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txto_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__txto_int_clr_msb, self.__txto_int_clr_lsb)
    @txto_int_clr.setter
    def txto_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__txto_int_clr_msb, self.__txto_int_clr_lsb, value)

    @property
    def txend_data_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__txend_data_int_clr_msb, self.__txend_data_int_clr_lsb)
    @txend_data_int_clr.setter
    def txend_data_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__txend_data_int_clr_msb, self.__txend_data_int_clr_lsb, value)

    @property
    def txend_cts_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__txend_cts_int_clr_msb, self.__txend_cts_int_clr_lsb)
    @txend_cts_int_clr.setter
    def txend_cts_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__txend_cts_int_clr_msb, self.__txend_cts_int_clr_lsb, value)

    @property
    def txend_rts_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__txend_rts_int_clr_msb, self.__txend_rts_int_clr_lsb)
    @txend_rts_int_clr.setter
    def txend_rts_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__txend_rts_int_clr_msb, self.__txend_rts_int_clr_lsb, value)

    @property
    def rxend_txack_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_txack_int_clr_msb, self.__rxend_txack_int_clr_lsb)
    @rxend_txack_int_clr.setter
    def rxend_txack_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_txack_int_clr_msb, self.__rxend_txack_int_clr_lsb, value)

    @property
    def rxend_txcts_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_txcts_int_clr_msb, self.__rxend_txcts_int_clr_lsb)
    @rxend_txcts_int_clr.setter
    def rxend_txcts_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_txcts_int_clr_msb, self.__rxend_txcts_int_clr_lsb, value)

    @property
    def rxend_data_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_data_int_clr_msb, self.__rxend_data_int_clr_lsb)
    @rxend_data_int_clr.setter
    def rxend_data_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_data_int_clr_msb, self.__rxend_data_int_clr_lsb, value)

    @property
    def rxsuc_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rxsuc_int_clr_msb, self.__rxsuc_int_clr_lsb)
    @rxsuc_int_clr.setter
    def rxsuc_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxsuc_int_clr_msb, self.__rxsuc_int_clr_lsb, value)

    @property
    def imrto_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__imrto_int_clr_msb, self.__imrto_int_clr_lsb)
    @imrto_int_clr.setter
    def imrto_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__imrto_int_clr_msb, self.__imrto_int_clr_lsb, value)

    @property
    def rxto_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rxto_int_clr_msb, self.__rxto_int_clr_lsb)
    @rxto_int_clr.setter
    def rxto_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxto_int_clr_msb, self.__rxto_int_clr_lsb, value)
class INT_NMI_MAC(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x30
        self.__rxchest_int_nmi_lsb = 29
        self.__rxchest_int_nmi_msb = 29
        self.__timer1_reach_int_nmi_lsb = 28
        self.__timer1_reach_int_nmi_msb = 28
        self.__timer0_reach_int_nmi_lsb = 27
        self.__timer0_reach_int_nmi_msb = 27
        self.__tick_1s_int_nmi_lsb = 26
        self.__tick_1s_int_nmi_msb = 26
        self.__rxend_sampdu_int_nmi_lsb = 24
        self.__rxend_sampdu_int_nmi_msb = 24
        self.__txstart_data_int_nmi_lsb = 23
        self.__txstart_data_int_nmi_msb = 23
        self.__txopstart_int_nmi_lsb = 22
        self.__txopstart_int_nmi_msb = 22
        self.__txopcomplete_int_nmi_lsb = 21
        self.__txopcomplete_int_nmi_msb = 21
        self.__rxerr_to_int_nmi_lsb = 20
        self.__rxerr_to_int_nmi_msb = 20
        self.__txena_to_int_nmi_lsb = 19
        self.__txena_to_int_nmi_msb = 19
        self.__rxahberr_int_nmi_lsb = 18
        self.__rxahberr_int_nmi_msb = 18
        self.__txstart_cts_int_nmi_lsb = 13
        self.__txstart_cts_int_nmi_msb = 13
        self.__txstart_rts_int_nmi_lsb = 12
        self.__txstart_rts_int_nmi_msb = 12
        self.__panic_watchdog_int_nmi_lsb = 11
        self.__panic_watchdog_int_nmi_msb = 11
        self.__bb_dc_int_nmi_lsb = 10
        self.__bb_dc_int_nmi_msb = 10
        self.__rxbufov_int_nmi_lsb = 9
        self.__rxbufov_int_nmi_msb = 9
        self.__txcol_int_nmi_lsb = 8
        self.__txcol_int_nmi_msb = 8
        self.__txcomplete_int_nmi_lsb = 7
        self.__txcomplete_int_nmi_msb = 7
        self.__rxhung_int_nmi_lsb = 6
        self.__rxhung_int_nmi_msb = 6
        self.__rxsuc_data_int_nmi_lsb = 5
        self.__rxsuc_data_int_nmi_msb = 5
        self.__rxend_real_int_nmi_lsb = 4
        self.__rxend_real_int_nmi_msb = 4
        self.__rxstart_int_nmi_lsb = 3
        self.__rxstart_int_nmi_msb = 3
        self.__rxend_int_nmi_lsb = 2
        self.__rxend_int_nmi_msb = 2
        self.__txend_int_nmi_lsb = 1
        self.__txend_int_nmi_msb = 1
        self.__txstart_int_nmi_lsb = 0
        self.__txstart_int_nmi_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxchest_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__rxchest_int_nmi_msb, self.__rxchest_int_nmi_lsb)
    @rxchest_int_nmi.setter
    def rxchest_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxchest_int_nmi_msb, self.__rxchest_int_nmi_lsb, value)

    @property
    def timer1_reach_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__timer1_reach_int_nmi_msb, self.__timer1_reach_int_nmi_lsb)
    @timer1_reach_int_nmi.setter
    def timer1_reach_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__timer1_reach_int_nmi_msb, self.__timer1_reach_int_nmi_lsb, value)

    @property
    def timer0_reach_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__timer0_reach_int_nmi_msb, self.__timer0_reach_int_nmi_lsb)
    @timer0_reach_int_nmi.setter
    def timer0_reach_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__timer0_reach_int_nmi_msb, self.__timer0_reach_int_nmi_lsb, value)

    @property
    def tick_1s_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__tick_1s_int_nmi_msb, self.__tick_1s_int_nmi_lsb)
    @tick_1s_int_nmi.setter
    def tick_1s_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__tick_1s_int_nmi_msb, self.__tick_1s_int_nmi_lsb, value)

    @property
    def rxend_sampdu_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_sampdu_int_nmi_msb, self.__rxend_sampdu_int_nmi_lsb)
    @rxend_sampdu_int_nmi.setter
    def rxend_sampdu_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_sampdu_int_nmi_msb, self.__rxend_sampdu_int_nmi_lsb, value)

    @property
    def txstart_data_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__txstart_data_int_nmi_msb, self.__txstart_data_int_nmi_lsb)
    @txstart_data_int_nmi.setter
    def txstart_data_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txstart_data_int_nmi_msb, self.__txstart_data_int_nmi_lsb, value)

    @property
    def txopstart_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__txopstart_int_nmi_msb, self.__txopstart_int_nmi_lsb)
    @txopstart_int_nmi.setter
    def txopstart_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txopstart_int_nmi_msb, self.__txopstart_int_nmi_lsb, value)

    @property
    def txopcomplete_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__txopcomplete_int_nmi_msb, self.__txopcomplete_int_nmi_lsb)
    @txopcomplete_int_nmi.setter
    def txopcomplete_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txopcomplete_int_nmi_msb, self.__txopcomplete_int_nmi_lsb, value)

    @property
    def rxerr_to_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__rxerr_to_int_nmi_msb, self.__rxerr_to_int_nmi_lsb)
    @rxerr_to_int_nmi.setter
    def rxerr_to_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxerr_to_int_nmi_msb, self.__rxerr_to_int_nmi_lsb, value)

    @property
    def txena_to_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__txena_to_int_nmi_msb, self.__txena_to_int_nmi_lsb)
    @txena_to_int_nmi.setter
    def txena_to_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txena_to_int_nmi_msb, self.__txena_to_int_nmi_lsb, value)

    @property
    def rxahberr_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__rxahberr_int_nmi_msb, self.__rxahberr_int_nmi_lsb)
    @rxahberr_int_nmi.setter
    def rxahberr_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxahberr_int_nmi_msb, self.__rxahberr_int_nmi_lsb, value)

    @property
    def txstart_cts_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__txstart_cts_int_nmi_msb, self.__txstart_cts_int_nmi_lsb)
    @txstart_cts_int_nmi.setter
    def txstart_cts_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txstart_cts_int_nmi_msb, self.__txstart_cts_int_nmi_lsb, value)

    @property
    def txstart_rts_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__txstart_rts_int_nmi_msb, self.__txstart_rts_int_nmi_lsb)
    @txstart_rts_int_nmi.setter
    def txstart_rts_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txstart_rts_int_nmi_msb, self.__txstart_rts_int_nmi_lsb, value)

    @property
    def panic_watchdog_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__panic_watchdog_int_nmi_msb, self.__panic_watchdog_int_nmi_lsb)
    @panic_watchdog_int_nmi.setter
    def panic_watchdog_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__panic_watchdog_int_nmi_msb, self.__panic_watchdog_int_nmi_lsb, value)

    @property
    def bb_dc_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__bb_dc_int_nmi_msb, self.__bb_dc_int_nmi_lsb)
    @bb_dc_int_nmi.setter
    def bb_dc_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__bb_dc_int_nmi_msb, self.__bb_dc_int_nmi_lsb, value)

    @property
    def rxbufov_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__rxbufov_int_nmi_msb, self.__rxbufov_int_nmi_lsb)
    @rxbufov_int_nmi.setter
    def rxbufov_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxbufov_int_nmi_msb, self.__rxbufov_int_nmi_lsb, value)

    @property
    def txcol_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__txcol_int_nmi_msb, self.__txcol_int_nmi_lsb)
    @txcol_int_nmi.setter
    def txcol_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txcol_int_nmi_msb, self.__txcol_int_nmi_lsb, value)

    @property
    def txcomplete_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__txcomplete_int_nmi_msb, self.__txcomplete_int_nmi_lsb)
    @txcomplete_int_nmi.setter
    def txcomplete_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txcomplete_int_nmi_msb, self.__txcomplete_int_nmi_lsb, value)

    @property
    def rxhung_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__rxhung_int_nmi_msb, self.__rxhung_int_nmi_lsb)
    @rxhung_int_nmi.setter
    def rxhung_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxhung_int_nmi_msb, self.__rxhung_int_nmi_lsb, value)

    @property
    def rxsuc_data_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__rxsuc_data_int_nmi_msb, self.__rxsuc_data_int_nmi_lsb)
    @rxsuc_data_int_nmi.setter
    def rxsuc_data_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxsuc_data_int_nmi_msb, self.__rxsuc_data_int_nmi_lsb, value)

    @property
    def rxend_real_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_real_int_nmi_msb, self.__rxend_real_int_nmi_lsb)
    @rxend_real_int_nmi.setter
    def rxend_real_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_real_int_nmi_msb, self.__rxend_real_int_nmi_lsb, value)

    @property
    def rxstart_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__rxstart_int_nmi_msb, self.__rxstart_int_nmi_lsb)
    @rxstart_int_nmi.setter
    def rxstart_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxstart_int_nmi_msb, self.__rxstart_int_nmi_lsb, value)

    @property
    def rxend_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_int_nmi_msb, self.__rxend_int_nmi_lsb)
    @rxend_int_nmi.setter
    def rxend_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_int_nmi_msb, self.__rxend_int_nmi_lsb, value)

    @property
    def txend_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__txend_int_nmi_msb, self.__txend_int_nmi_lsb)
    @txend_int_nmi.setter
    def txend_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txend_int_nmi_msb, self.__txend_int_nmi_lsb, value)

    @property
    def txstart_int_nmi(self):
        return self.__MEM.rdm(self.__addr, self.__txstart_int_nmi_msb, self.__txstart_int_nmi_lsb)
    @txstart_int_nmi.setter
    def txstart_int_nmi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txstart_int_nmi_msb, self.__txstart_int_nmi_lsb, value)
class INT_ENA_MAC(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x34
        self.__rxchest_int_ena_lsb = 29
        self.__rxchest_int_ena_msb = 29
        self.__timer1_reach_int_ena_lsb = 28
        self.__timer1_reach_int_ena_msb = 28
        self.__timer0_reach_int_ena_lsb = 27
        self.__timer0_reach_int_ena_msb = 27
        self.__tick_1s_int_ena_lsb = 26
        self.__tick_1s_int_ena_msb = 26
        self.__rxend_sampdu_int_ena_lsb = 24
        self.__rxend_sampdu_int_ena_msb = 24
        self.__txstart_data_int_ena_lsb = 23
        self.__txstart_data_int_ena_msb = 23
        self.__txopstart_int_ena_lsb = 22
        self.__txopstart_int_ena_msb = 22
        self.__txopcomplete_int_ena_lsb = 21
        self.__txopcomplete_int_ena_msb = 21
        self.__rxerr_to_int_ena_lsb = 20
        self.__rxerr_to_int_ena_msb = 20
        self.__txena_to_int_ena_lsb = 19
        self.__txena_to_int_ena_msb = 19
        self.__rxahberr_int_ena_lsb = 18
        self.__rxahberr_int_ena_msb = 18
        self.__txstart_cts_int_ena_lsb = 13
        self.__txstart_cts_int_ena_msb = 13
        self.__txstart_rts_int_ena_lsb = 12
        self.__txstart_rts_int_ena_msb = 12
        self.__panic_watchdog_int_ena_lsb = 11
        self.__panic_watchdog_int_ena_msb = 11
        self.__bb_dc_int_ena_lsb = 10
        self.__bb_dc_int_ena_msb = 10
        self.__rxbufov_int_ena_lsb = 9
        self.__rxbufov_int_ena_msb = 9
        self.__txcol_int_ena_lsb = 8
        self.__txcol_int_ena_msb = 8
        self.__txcomplete_int_ena_lsb = 7
        self.__txcomplete_int_ena_msb = 7
        self.__rxhung_int_ena_lsb = 6
        self.__rxhung_int_ena_msb = 6
        self.__rxsuc_data_int_ena_lsb = 5
        self.__rxsuc_data_int_ena_msb = 5
        self.__rxend_real_int_ena_lsb = 4
        self.__rxend_real_int_ena_msb = 4
        self.__rxstart_int_ena_lsb = 3
        self.__rxstart_int_ena_msb = 3
        self.__rxend_int_ena_lsb = 2
        self.__rxend_int_ena_msb = 2
        self.__txend_int_ena_lsb = 1
        self.__txend_int_ena_msb = 1
        self.__txstart_int_ena_lsb = 0
        self.__txstart_int_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxchest_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rxchest_int_ena_msb, self.__rxchest_int_ena_lsb)
    @rxchest_int_ena.setter
    def rxchest_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxchest_int_ena_msb, self.__rxchest_int_ena_lsb, value)

    @property
    def timer1_reach_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__timer1_reach_int_ena_msb, self.__timer1_reach_int_ena_lsb)
    @timer1_reach_int_ena.setter
    def timer1_reach_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__timer1_reach_int_ena_msb, self.__timer1_reach_int_ena_lsb, value)

    @property
    def timer0_reach_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__timer0_reach_int_ena_msb, self.__timer0_reach_int_ena_lsb)
    @timer0_reach_int_ena.setter
    def timer0_reach_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__timer0_reach_int_ena_msb, self.__timer0_reach_int_ena_lsb, value)

    @property
    def tick_1s_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__tick_1s_int_ena_msb, self.__tick_1s_int_ena_lsb)
    @tick_1s_int_ena.setter
    def tick_1s_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__tick_1s_int_ena_msb, self.__tick_1s_int_ena_lsb, value)

    @property
    def rxend_sampdu_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_sampdu_int_ena_msb, self.__rxend_sampdu_int_ena_lsb)
    @rxend_sampdu_int_ena.setter
    def rxend_sampdu_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_sampdu_int_ena_msb, self.__rxend_sampdu_int_ena_lsb, value)

    @property
    def txstart_data_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__txstart_data_int_ena_msb, self.__txstart_data_int_ena_lsb)
    @txstart_data_int_ena.setter
    def txstart_data_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__txstart_data_int_ena_msb, self.__txstart_data_int_ena_lsb, value)

    @property
    def txopstart_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__txopstart_int_ena_msb, self.__txopstart_int_ena_lsb)
    @txopstart_int_ena.setter
    def txopstart_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__txopstart_int_ena_msb, self.__txopstart_int_ena_lsb, value)

    @property
    def txopcomplete_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__txopcomplete_int_ena_msb, self.__txopcomplete_int_ena_lsb)
    @txopcomplete_int_ena.setter
    def txopcomplete_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__txopcomplete_int_ena_msb, self.__txopcomplete_int_ena_lsb, value)

    @property
    def rxerr_to_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rxerr_to_int_ena_msb, self.__rxerr_to_int_ena_lsb)
    @rxerr_to_int_ena.setter
    def rxerr_to_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxerr_to_int_ena_msb, self.__rxerr_to_int_ena_lsb, value)

    @property
    def txena_to_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__txena_to_int_ena_msb, self.__txena_to_int_ena_lsb)
    @txena_to_int_ena.setter
    def txena_to_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__txena_to_int_ena_msb, self.__txena_to_int_ena_lsb, value)

    @property
    def rxahberr_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rxahberr_int_ena_msb, self.__rxahberr_int_ena_lsb)
    @rxahberr_int_ena.setter
    def rxahberr_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxahberr_int_ena_msb, self.__rxahberr_int_ena_lsb, value)

    @property
    def txstart_cts_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__txstart_cts_int_ena_msb, self.__txstart_cts_int_ena_lsb)
    @txstart_cts_int_ena.setter
    def txstart_cts_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__txstart_cts_int_ena_msb, self.__txstart_cts_int_ena_lsb, value)

    @property
    def txstart_rts_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__txstart_rts_int_ena_msb, self.__txstart_rts_int_ena_lsb)
    @txstart_rts_int_ena.setter
    def txstart_rts_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__txstart_rts_int_ena_msb, self.__txstart_rts_int_ena_lsb, value)

    @property
    def panic_watchdog_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__panic_watchdog_int_ena_msb, self.__panic_watchdog_int_ena_lsb)
    @panic_watchdog_int_ena.setter
    def panic_watchdog_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__panic_watchdog_int_ena_msb, self.__panic_watchdog_int_ena_lsb, value)

    @property
    def bb_dc_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__bb_dc_int_ena_msb, self.__bb_dc_int_ena_lsb)
    @bb_dc_int_ena.setter
    def bb_dc_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__bb_dc_int_ena_msb, self.__bb_dc_int_ena_lsb, value)

    @property
    def rxbufov_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rxbufov_int_ena_msb, self.__rxbufov_int_ena_lsb)
    @rxbufov_int_ena.setter
    def rxbufov_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxbufov_int_ena_msb, self.__rxbufov_int_ena_lsb, value)

    @property
    def txcol_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__txcol_int_ena_msb, self.__txcol_int_ena_lsb)
    @txcol_int_ena.setter
    def txcol_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__txcol_int_ena_msb, self.__txcol_int_ena_lsb, value)

    @property
    def txcomplete_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__txcomplete_int_ena_msb, self.__txcomplete_int_ena_lsb)
    @txcomplete_int_ena.setter
    def txcomplete_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__txcomplete_int_ena_msb, self.__txcomplete_int_ena_lsb, value)

    @property
    def rxhung_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rxhung_int_ena_msb, self.__rxhung_int_ena_lsb)
    @rxhung_int_ena.setter
    def rxhung_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxhung_int_ena_msb, self.__rxhung_int_ena_lsb, value)

    @property
    def rxsuc_data_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rxsuc_data_int_ena_msb, self.__rxsuc_data_int_ena_lsb)
    @rxsuc_data_int_ena.setter
    def rxsuc_data_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxsuc_data_int_ena_msb, self.__rxsuc_data_int_ena_lsb, value)

    @property
    def rxend_real_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_real_int_ena_msb, self.__rxend_real_int_ena_lsb)
    @rxend_real_int_ena.setter
    def rxend_real_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_real_int_ena_msb, self.__rxend_real_int_ena_lsb, value)

    @property
    def rxstart_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rxstart_int_ena_msb, self.__rxstart_int_ena_lsb)
    @rxstart_int_ena.setter
    def rxstart_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxstart_int_ena_msb, self.__rxstart_int_ena_lsb, value)

    @property
    def rxend_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_int_ena_msb, self.__rxend_int_ena_lsb)
    @rxend_int_ena.setter
    def rxend_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_int_ena_msb, self.__rxend_int_ena_lsb, value)

    @property
    def txend_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__txend_int_ena_msb, self.__txend_int_ena_lsb)
    @txend_int_ena.setter
    def txend_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__txend_int_ena_msb, self.__txend_int_ena_lsb, value)

    @property
    def txstart_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__txstart_int_ena_msb, self.__txstart_int_ena_lsb)
    @txstart_int_ena.setter
    def txstart_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__txstart_int_ena_msb, self.__txstart_int_ena_lsb, value)
class INT_RAW_MAC(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x38
        self.__rxchest_int_raw_lsb = 29
        self.__rxchest_int_raw_msb = 29
        self.__timer1_reach_int_raw_lsb = 28
        self.__timer1_reach_int_raw_msb = 28
        self.__timer0_reach_int_raw_lsb = 27
        self.__timer0_reach_int_raw_msb = 27
        self.__tick_1s_int_raw_lsb = 26
        self.__tick_1s_int_raw_msb = 26
        self.__rxend_sampdu_int_raw_lsb = 24
        self.__rxend_sampdu_int_raw_msb = 24
        self.__txstart_data_int_raw_lsb = 23
        self.__txstart_data_int_raw_msb = 23
        self.__txopstart_int_raw_lsb = 22
        self.__txopstart_int_raw_msb = 22
        self.__txopcomplete_int_raw_lsb = 21
        self.__txopcomplete_int_raw_msb = 21
        self.__rxerr_to_int_raw_lsb = 20
        self.__rxerr_to_int_raw_msb = 20
        self.__txena_to_int_raw_lsb = 19
        self.__txena_to_int_raw_msb = 19
        self.__rxahberr_int_raw_lsb = 18
        self.__rxahberr_int_raw_msb = 18
        self.__txstart_cts_int_raw_lsb = 13
        self.__txstart_cts_int_raw_msb = 13
        self.__txstart_rts_int_raw_lsb = 12
        self.__txstart_rts_int_raw_msb = 12
        self.__panic_watchdog_int_raw_lsb = 11
        self.__panic_watchdog_int_raw_msb = 11
        self.__bb_dc_int_raw_lsb = 10
        self.__bb_dc_int_raw_msb = 10
        self.__rxbufov_int_raw_lsb = 9
        self.__rxbufov_int_raw_msb = 9
        self.__txcol_int_raw_lsb = 8
        self.__txcol_int_raw_msb = 8
        self.__txcomplete_int_raw_lsb = 7
        self.__txcomplete_int_raw_msb = 7
        self.__rxhung_int_raw_lsb = 6
        self.__rxhung_int_raw_msb = 6
        self.__rxsuc_data_int_raw_lsb = 5
        self.__rxsuc_data_int_raw_msb = 5
        self.__rxend_real_int_raw_lsb = 4
        self.__rxend_real_int_raw_msb = 4
        self.__rxstart_int_raw_lsb = 3
        self.__rxstart_int_raw_msb = 3
        self.__rxend_int_raw_lsb = 2
        self.__rxend_int_raw_msb = 2
        self.__txend_int_raw_lsb = 1
        self.__txend_int_raw_msb = 1
        self.__txstart_int_raw_lsb = 0
        self.__txstart_int_raw_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxchest_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rxchest_int_raw_msb, self.__rxchest_int_raw_lsb)
    @rxchest_int_raw.setter
    def rxchest_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxchest_int_raw_msb, self.__rxchest_int_raw_lsb, value)

    @property
    def timer1_reach_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__timer1_reach_int_raw_msb, self.__timer1_reach_int_raw_lsb)
    @timer1_reach_int_raw.setter
    def timer1_reach_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__timer1_reach_int_raw_msb, self.__timer1_reach_int_raw_lsb, value)

    @property
    def timer0_reach_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__timer0_reach_int_raw_msb, self.__timer0_reach_int_raw_lsb)
    @timer0_reach_int_raw.setter
    def timer0_reach_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__timer0_reach_int_raw_msb, self.__timer0_reach_int_raw_lsb, value)

    @property
    def tick_1s_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__tick_1s_int_raw_msb, self.__tick_1s_int_raw_lsb)
    @tick_1s_int_raw.setter
    def tick_1s_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__tick_1s_int_raw_msb, self.__tick_1s_int_raw_lsb, value)

    @property
    def rxend_sampdu_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_sampdu_int_raw_msb, self.__rxend_sampdu_int_raw_lsb)
    @rxend_sampdu_int_raw.setter
    def rxend_sampdu_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_sampdu_int_raw_msb, self.__rxend_sampdu_int_raw_lsb, value)

    @property
    def txstart_data_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__txstart_data_int_raw_msb, self.__txstart_data_int_raw_lsb)
    @txstart_data_int_raw.setter
    def txstart_data_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__txstart_data_int_raw_msb, self.__txstart_data_int_raw_lsb, value)

    @property
    def txopstart_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__txopstart_int_raw_msb, self.__txopstart_int_raw_lsb)
    @txopstart_int_raw.setter
    def txopstart_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__txopstart_int_raw_msb, self.__txopstart_int_raw_lsb, value)

    @property
    def txopcomplete_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__txopcomplete_int_raw_msb, self.__txopcomplete_int_raw_lsb)
    @txopcomplete_int_raw.setter
    def txopcomplete_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__txopcomplete_int_raw_msb, self.__txopcomplete_int_raw_lsb, value)

    @property
    def rxerr_to_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rxerr_to_int_raw_msb, self.__rxerr_to_int_raw_lsb)
    @rxerr_to_int_raw.setter
    def rxerr_to_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxerr_to_int_raw_msb, self.__rxerr_to_int_raw_lsb, value)

    @property
    def txena_to_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__txena_to_int_raw_msb, self.__txena_to_int_raw_lsb)
    @txena_to_int_raw.setter
    def txena_to_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__txena_to_int_raw_msb, self.__txena_to_int_raw_lsb, value)

    @property
    def rxahberr_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rxahberr_int_raw_msb, self.__rxahberr_int_raw_lsb)
    @rxahberr_int_raw.setter
    def rxahberr_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxahberr_int_raw_msb, self.__rxahberr_int_raw_lsb, value)

    @property
    def txstart_cts_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__txstart_cts_int_raw_msb, self.__txstart_cts_int_raw_lsb)
    @txstart_cts_int_raw.setter
    def txstart_cts_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__txstart_cts_int_raw_msb, self.__txstart_cts_int_raw_lsb, value)

    @property
    def txstart_rts_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__txstart_rts_int_raw_msb, self.__txstart_rts_int_raw_lsb)
    @txstart_rts_int_raw.setter
    def txstart_rts_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__txstart_rts_int_raw_msb, self.__txstart_rts_int_raw_lsb, value)

    @property
    def panic_watchdog_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__panic_watchdog_int_raw_msb, self.__panic_watchdog_int_raw_lsb)
    @panic_watchdog_int_raw.setter
    def panic_watchdog_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__panic_watchdog_int_raw_msb, self.__panic_watchdog_int_raw_lsb, value)

    @property
    def bb_dc_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__bb_dc_int_raw_msb, self.__bb_dc_int_raw_lsb)
    @bb_dc_int_raw.setter
    def bb_dc_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__bb_dc_int_raw_msb, self.__bb_dc_int_raw_lsb, value)

    @property
    def rxbufov_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rxbufov_int_raw_msb, self.__rxbufov_int_raw_lsb)
    @rxbufov_int_raw.setter
    def rxbufov_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxbufov_int_raw_msb, self.__rxbufov_int_raw_lsb, value)

    @property
    def txcol_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__txcol_int_raw_msb, self.__txcol_int_raw_lsb)
    @txcol_int_raw.setter
    def txcol_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__txcol_int_raw_msb, self.__txcol_int_raw_lsb, value)

    @property
    def txcomplete_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__txcomplete_int_raw_msb, self.__txcomplete_int_raw_lsb)
    @txcomplete_int_raw.setter
    def txcomplete_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__txcomplete_int_raw_msb, self.__txcomplete_int_raw_lsb, value)

    @property
    def rxhung_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rxhung_int_raw_msb, self.__rxhung_int_raw_lsb)
    @rxhung_int_raw.setter
    def rxhung_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxhung_int_raw_msb, self.__rxhung_int_raw_lsb, value)

    @property
    def rxsuc_data_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rxsuc_data_int_raw_msb, self.__rxsuc_data_int_raw_lsb)
    @rxsuc_data_int_raw.setter
    def rxsuc_data_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxsuc_data_int_raw_msb, self.__rxsuc_data_int_raw_lsb, value)

    @property
    def rxend_real_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_real_int_raw_msb, self.__rxend_real_int_raw_lsb)
    @rxend_real_int_raw.setter
    def rxend_real_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_real_int_raw_msb, self.__rxend_real_int_raw_lsb, value)

    @property
    def rxstart_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rxstart_int_raw_msb, self.__rxstart_int_raw_lsb)
    @rxstart_int_raw.setter
    def rxstart_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxstart_int_raw_msb, self.__rxstart_int_raw_lsb, value)

    @property
    def rxend_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_int_raw_msb, self.__rxend_int_raw_lsb)
    @rxend_int_raw.setter
    def rxend_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_int_raw_msb, self.__rxend_int_raw_lsb, value)

    @property
    def txend_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__txend_int_raw_msb, self.__txend_int_raw_lsb)
    @txend_int_raw.setter
    def txend_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__txend_int_raw_msb, self.__txend_int_raw_lsb, value)

    @property
    def txstart_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__txstart_int_raw_msb, self.__txstart_int_raw_lsb)
    @txstart_int_raw.setter
    def txstart_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__txstart_int_raw_msb, self.__txstart_int_raw_lsb, value)
class INT_ST_MAC(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x3c
        self.__rxchest_int_st_lsb = 29
        self.__rxchest_int_st_msb = 29
        self.__timer1_reach_int_st_lsb = 28
        self.__timer1_reach_int_st_msb = 28
        self.__timer0_reach_int_st_lsb = 27
        self.__timer0_reach_int_st_msb = 27
        self.__tick_1s_int_st_lsb = 26
        self.__tick_1s_int_st_msb = 26
        self.__rxend_sampdu_int_st_lsb = 24
        self.__rxend_sampdu_int_st_msb = 24
        self.__txstart_data_int_st_lsb = 23
        self.__txstart_data_int_st_msb = 23
        self.__txopstart_int_st_lsb = 22
        self.__txopstart_int_st_msb = 22
        self.__txopcomplete_int_st_lsb = 21
        self.__txopcomplete_int_st_msb = 21
        self.__rxerr_to_int_st_lsb = 20
        self.__rxerr_to_int_st_msb = 20
        self.__txena_to_int_st_lsb = 19
        self.__txena_to_int_st_msb = 19
        self.__rxahberr_int_st_lsb = 18
        self.__rxahberr_int_st_msb = 18
        self.__txstart_cts_int_st_lsb = 13
        self.__txstart_cts_int_st_msb = 13
        self.__txstart_rts_int_st_lsb = 12
        self.__txstart_rts_int_st_msb = 12
        self.__panic_watchdog_int_st_lsb = 11
        self.__panic_watchdog_int_st_msb = 11
        self.__bb_dc_int_st_lsb = 10
        self.__bb_dc_int_st_msb = 10
        self.__rxbufov_int_st_lsb = 9
        self.__rxbufov_int_st_msb = 9
        self.__txcol_int_st_lsb = 8
        self.__txcol_int_st_msb = 8
        self.__txcomplete_int_st_lsb = 7
        self.__txcomplete_int_st_msb = 7
        self.__rxhung_int_st_lsb = 6
        self.__rxhung_int_st_msb = 6
        self.__rxsuc_data_int_st_lsb = 5
        self.__rxsuc_data_int_st_msb = 5
        self.__rxend_real_int_st_lsb = 4
        self.__rxend_real_int_st_msb = 4
        self.__rxstart_int_st_lsb = 3
        self.__rxstart_int_st_msb = 3
        self.__rxend_int_st_lsb = 2
        self.__rxend_int_st_msb = 2
        self.__txend_int_st_lsb = 1
        self.__txend_int_st_msb = 1
        self.__txstart_int_st_lsb = 0
        self.__txstart_int_st_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxchest_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rxchest_int_st_msb, self.__rxchest_int_st_lsb)
    @rxchest_int_st.setter
    def rxchest_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxchest_int_st_msb, self.__rxchest_int_st_lsb, value)

    @property
    def timer1_reach_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__timer1_reach_int_st_msb, self.__timer1_reach_int_st_lsb)
    @timer1_reach_int_st.setter
    def timer1_reach_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__timer1_reach_int_st_msb, self.__timer1_reach_int_st_lsb, value)

    @property
    def timer0_reach_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__timer0_reach_int_st_msb, self.__timer0_reach_int_st_lsb)
    @timer0_reach_int_st.setter
    def timer0_reach_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__timer0_reach_int_st_msb, self.__timer0_reach_int_st_lsb, value)

    @property
    def tick_1s_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__tick_1s_int_st_msb, self.__tick_1s_int_st_lsb)
    @tick_1s_int_st.setter
    def tick_1s_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__tick_1s_int_st_msb, self.__tick_1s_int_st_lsb, value)

    @property
    def rxend_sampdu_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_sampdu_int_st_msb, self.__rxend_sampdu_int_st_lsb)
    @rxend_sampdu_int_st.setter
    def rxend_sampdu_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_sampdu_int_st_msb, self.__rxend_sampdu_int_st_lsb, value)

    @property
    def txstart_data_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__txstart_data_int_st_msb, self.__txstart_data_int_st_lsb)
    @txstart_data_int_st.setter
    def txstart_data_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__txstart_data_int_st_msb, self.__txstart_data_int_st_lsb, value)

    @property
    def txopstart_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__txopstart_int_st_msb, self.__txopstart_int_st_lsb)
    @txopstart_int_st.setter
    def txopstart_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__txopstart_int_st_msb, self.__txopstart_int_st_lsb, value)

    @property
    def txopcomplete_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__txopcomplete_int_st_msb, self.__txopcomplete_int_st_lsb)
    @txopcomplete_int_st.setter
    def txopcomplete_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__txopcomplete_int_st_msb, self.__txopcomplete_int_st_lsb, value)

    @property
    def rxerr_to_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rxerr_to_int_st_msb, self.__rxerr_to_int_st_lsb)
    @rxerr_to_int_st.setter
    def rxerr_to_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxerr_to_int_st_msb, self.__rxerr_to_int_st_lsb, value)

    @property
    def txena_to_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__txena_to_int_st_msb, self.__txena_to_int_st_lsb)
    @txena_to_int_st.setter
    def txena_to_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__txena_to_int_st_msb, self.__txena_to_int_st_lsb, value)

    @property
    def rxahberr_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rxahberr_int_st_msb, self.__rxahberr_int_st_lsb)
    @rxahberr_int_st.setter
    def rxahberr_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxahberr_int_st_msb, self.__rxahberr_int_st_lsb, value)

    @property
    def txstart_cts_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__txstart_cts_int_st_msb, self.__txstart_cts_int_st_lsb)
    @txstart_cts_int_st.setter
    def txstart_cts_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__txstart_cts_int_st_msb, self.__txstart_cts_int_st_lsb, value)

    @property
    def txstart_rts_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__txstart_rts_int_st_msb, self.__txstart_rts_int_st_lsb)
    @txstart_rts_int_st.setter
    def txstart_rts_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__txstart_rts_int_st_msb, self.__txstart_rts_int_st_lsb, value)

    @property
    def panic_watchdog_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__panic_watchdog_int_st_msb, self.__panic_watchdog_int_st_lsb)
    @panic_watchdog_int_st.setter
    def panic_watchdog_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__panic_watchdog_int_st_msb, self.__panic_watchdog_int_st_lsb, value)

    @property
    def bb_dc_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__bb_dc_int_st_msb, self.__bb_dc_int_st_lsb)
    @bb_dc_int_st.setter
    def bb_dc_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__bb_dc_int_st_msb, self.__bb_dc_int_st_lsb, value)

    @property
    def rxbufov_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rxbufov_int_st_msb, self.__rxbufov_int_st_lsb)
    @rxbufov_int_st.setter
    def rxbufov_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxbufov_int_st_msb, self.__rxbufov_int_st_lsb, value)

    @property
    def txcol_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__txcol_int_st_msb, self.__txcol_int_st_lsb)
    @txcol_int_st.setter
    def txcol_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__txcol_int_st_msb, self.__txcol_int_st_lsb, value)

    @property
    def txcomplete_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__txcomplete_int_st_msb, self.__txcomplete_int_st_lsb)
    @txcomplete_int_st.setter
    def txcomplete_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__txcomplete_int_st_msb, self.__txcomplete_int_st_lsb, value)

    @property
    def rxhung_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rxhung_int_st_msb, self.__rxhung_int_st_lsb)
    @rxhung_int_st.setter
    def rxhung_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxhung_int_st_msb, self.__rxhung_int_st_lsb, value)

    @property
    def rxsuc_data_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rxsuc_data_int_st_msb, self.__rxsuc_data_int_st_lsb)
    @rxsuc_data_int_st.setter
    def rxsuc_data_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxsuc_data_int_st_msb, self.__rxsuc_data_int_st_lsb, value)

    @property
    def rxend_real_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_real_int_st_msb, self.__rxend_real_int_st_lsb)
    @rxend_real_int_st.setter
    def rxend_real_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_real_int_st_msb, self.__rxend_real_int_st_lsb, value)

    @property
    def rxstart_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rxstart_int_st_msb, self.__rxstart_int_st_lsb)
    @rxstart_int_st.setter
    def rxstart_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxstart_int_st_msb, self.__rxstart_int_st_lsb, value)

    @property
    def rxend_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_int_st_msb, self.__rxend_int_st_lsb)
    @rxend_int_st.setter
    def rxend_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_int_st_msb, self.__rxend_int_st_lsb, value)

    @property
    def txend_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__txend_int_st_msb, self.__txend_int_st_lsb)
    @txend_int_st.setter
    def txend_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__txend_int_st_msb, self.__txend_int_st_lsb, value)

    @property
    def txstart_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__txstart_int_st_msb, self.__txstart_int_st_lsb)
    @txstart_int_st.setter
    def txstart_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__txstart_int_st_msb, self.__txstart_int_st_lsb, value)
class INT_CLR_MAC(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x40
        self.__rxchest_int_clr_lsb = 29
        self.__rxchest_int_clr_msb = 29
        self.__timer1_reach_int_clr_lsb = 28
        self.__timer1_reach_int_clr_msb = 28
        self.__timer0_reach_int_clr_lsb = 27
        self.__timer0_reach_int_clr_msb = 27
        self.__tick_1s_int_clr_lsb = 26
        self.__tick_1s_int_clr_msb = 26
        self.__rxend_sampdu_int_clr_lsb = 24
        self.__rxend_sampdu_int_clr_msb = 24
        self.__txstart_data_int_clr_lsb = 23
        self.__txstart_data_int_clr_msb = 23
        self.__txopstart_int_clr_lsb = 22
        self.__txopstart_int_clr_msb = 22
        self.__txopcomplete_int_clr_lsb = 21
        self.__txopcomplete_int_clr_msb = 21
        self.__rxerr_to_int_clr_lsb = 20
        self.__rxerr_to_int_clr_msb = 20
        self.__txena_to_int_clr_lsb = 19
        self.__txena_to_int_clr_msb = 19
        self.__rxahberr_int_clr_lsb = 18
        self.__rxahberr_int_clr_msb = 18
        self.__txstart_cts_int_clr_lsb = 13
        self.__txstart_cts_int_clr_msb = 13
        self.__txstart_rts_int_clr_lsb = 12
        self.__txstart_rts_int_clr_msb = 12
        self.__panic_watchdog_int_clr_lsb = 11
        self.__panic_watchdog_int_clr_msb = 11
        self.__bb_dc_int_clr_lsb = 10
        self.__bb_dc_int_clr_msb = 10
        self.__rxbufov_int_clr_lsb = 9
        self.__rxbufov_int_clr_msb = 9
        self.__txcol_int_clr_lsb = 8
        self.__txcol_int_clr_msb = 8
        self.__txcomplete_int_clr_lsb = 7
        self.__txcomplete_int_clr_msb = 7
        self.__rxhung_int_clr_lsb = 6
        self.__rxhung_int_clr_msb = 6
        self.__rxsuc_data_int_clr_lsb = 5
        self.__rxsuc_data_int_clr_msb = 5
        self.__rxend_real_int_clr_lsb = 4
        self.__rxend_real_int_clr_msb = 4
        self.__rxstart_int_clr_lsb = 3
        self.__rxstart_int_clr_msb = 3
        self.__rxend_int_clr_lsb = 2
        self.__rxend_int_clr_msb = 2
        self.__txend_int_clr_lsb = 1
        self.__txend_int_clr_msb = 1
        self.__txstart_int_clr_lsb = 0
        self.__txstart_int_clr_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxchest_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rxchest_int_clr_msb, self.__rxchest_int_clr_lsb)
    @rxchest_int_clr.setter
    def rxchest_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxchest_int_clr_msb, self.__rxchest_int_clr_lsb, value)

    @property
    def timer1_reach_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__timer1_reach_int_clr_msb, self.__timer1_reach_int_clr_lsb)
    @timer1_reach_int_clr.setter
    def timer1_reach_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__timer1_reach_int_clr_msb, self.__timer1_reach_int_clr_lsb, value)

    @property
    def timer0_reach_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__timer0_reach_int_clr_msb, self.__timer0_reach_int_clr_lsb)
    @timer0_reach_int_clr.setter
    def timer0_reach_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__timer0_reach_int_clr_msb, self.__timer0_reach_int_clr_lsb, value)

    @property
    def tick_1s_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__tick_1s_int_clr_msb, self.__tick_1s_int_clr_lsb)
    @tick_1s_int_clr.setter
    def tick_1s_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__tick_1s_int_clr_msb, self.__tick_1s_int_clr_lsb, value)

    @property
    def rxend_sampdu_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_sampdu_int_clr_msb, self.__rxend_sampdu_int_clr_lsb)
    @rxend_sampdu_int_clr.setter
    def rxend_sampdu_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_sampdu_int_clr_msb, self.__rxend_sampdu_int_clr_lsb, value)

    @property
    def txstart_data_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__txstart_data_int_clr_msb, self.__txstart_data_int_clr_lsb)
    @txstart_data_int_clr.setter
    def txstart_data_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__txstart_data_int_clr_msb, self.__txstart_data_int_clr_lsb, value)

    @property
    def txopstart_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__txopstart_int_clr_msb, self.__txopstart_int_clr_lsb)
    @txopstart_int_clr.setter
    def txopstart_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__txopstart_int_clr_msb, self.__txopstart_int_clr_lsb, value)

    @property
    def txopcomplete_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__txopcomplete_int_clr_msb, self.__txopcomplete_int_clr_lsb)
    @txopcomplete_int_clr.setter
    def txopcomplete_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__txopcomplete_int_clr_msb, self.__txopcomplete_int_clr_lsb, value)

    @property
    def rxerr_to_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rxerr_to_int_clr_msb, self.__rxerr_to_int_clr_lsb)
    @rxerr_to_int_clr.setter
    def rxerr_to_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxerr_to_int_clr_msb, self.__rxerr_to_int_clr_lsb, value)

    @property
    def txena_to_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__txena_to_int_clr_msb, self.__txena_to_int_clr_lsb)
    @txena_to_int_clr.setter
    def txena_to_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__txena_to_int_clr_msb, self.__txena_to_int_clr_lsb, value)

    @property
    def rxahberr_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rxahberr_int_clr_msb, self.__rxahberr_int_clr_lsb)
    @rxahberr_int_clr.setter
    def rxahberr_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxahberr_int_clr_msb, self.__rxahberr_int_clr_lsb, value)

    @property
    def txstart_cts_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__txstart_cts_int_clr_msb, self.__txstart_cts_int_clr_lsb)
    @txstart_cts_int_clr.setter
    def txstart_cts_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__txstart_cts_int_clr_msb, self.__txstart_cts_int_clr_lsb, value)

    @property
    def txstart_rts_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__txstart_rts_int_clr_msb, self.__txstart_rts_int_clr_lsb)
    @txstart_rts_int_clr.setter
    def txstart_rts_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__txstart_rts_int_clr_msb, self.__txstart_rts_int_clr_lsb, value)

    @property
    def panic_watchdog_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__panic_watchdog_int_clr_msb, self.__panic_watchdog_int_clr_lsb)
    @panic_watchdog_int_clr.setter
    def panic_watchdog_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__panic_watchdog_int_clr_msb, self.__panic_watchdog_int_clr_lsb, value)

    @property
    def bb_dc_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__bb_dc_int_clr_msb, self.__bb_dc_int_clr_lsb)
    @bb_dc_int_clr.setter
    def bb_dc_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__bb_dc_int_clr_msb, self.__bb_dc_int_clr_lsb, value)

    @property
    def rxbufov_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rxbufov_int_clr_msb, self.__rxbufov_int_clr_lsb)
    @rxbufov_int_clr.setter
    def rxbufov_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxbufov_int_clr_msb, self.__rxbufov_int_clr_lsb, value)

    @property
    def txcol_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__txcol_int_clr_msb, self.__txcol_int_clr_lsb)
    @txcol_int_clr.setter
    def txcol_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__txcol_int_clr_msb, self.__txcol_int_clr_lsb, value)

    @property
    def txcomplete_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__txcomplete_int_clr_msb, self.__txcomplete_int_clr_lsb)
    @txcomplete_int_clr.setter
    def txcomplete_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__txcomplete_int_clr_msb, self.__txcomplete_int_clr_lsb, value)

    @property
    def rxhung_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rxhung_int_clr_msb, self.__rxhung_int_clr_lsb)
    @rxhung_int_clr.setter
    def rxhung_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxhung_int_clr_msb, self.__rxhung_int_clr_lsb, value)

    @property
    def rxsuc_data_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rxsuc_data_int_clr_msb, self.__rxsuc_data_int_clr_lsb)
    @rxsuc_data_int_clr.setter
    def rxsuc_data_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxsuc_data_int_clr_msb, self.__rxsuc_data_int_clr_lsb, value)

    @property
    def rxend_real_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_real_int_clr_msb, self.__rxend_real_int_clr_lsb)
    @rxend_real_int_clr.setter
    def rxend_real_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_real_int_clr_msb, self.__rxend_real_int_clr_lsb, value)

    @property
    def rxstart_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rxstart_int_clr_msb, self.__rxstart_int_clr_lsb)
    @rxstart_int_clr.setter
    def rxstart_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxstart_int_clr_msb, self.__rxstart_int_clr_lsb, value)

    @property
    def rxend_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_int_clr_msb, self.__rxend_int_clr_lsb)
    @rxend_int_clr.setter
    def rxend_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_int_clr_msb, self.__rxend_int_clr_lsb, value)

    @property
    def txend_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__txend_int_clr_msb, self.__txend_int_clr_lsb)
    @txend_int_clr.setter
    def txend_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__txend_int_clr_msb, self.__txend_int_clr_lsb, value)

    @property
    def txstart_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__txstart_int_clr_msb, self.__txstart_int_clr_lsb)
    @txstart_int_clr.setter
    def txstart_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__txstart_int_clr_msb, self.__txstart_int_clr_lsb, value)
class MACSLOT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x44
        self.__reg_macslot_lsb = 24
        self.__reg_macslot_msb = 31
        self.__reg_sifs_lsb = 16
        self.__reg_sifs_msb = 23
        self.__reg_rxstartcck_delay_lsb = 8
        self.__reg_rxstartcck_delay_msb = 15
        self.__reg_rxstartofdm_delay_lsb = 0
        self.__reg_rxstartofdm_delay_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macslot(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macslot_msb, self.__reg_macslot_lsb)
    @reg_macslot.setter
    def reg_macslot(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macslot_msb, self.__reg_macslot_lsb, value)

    @property
    def reg_sifs(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sifs_msb, self.__reg_sifs_lsb)
    @reg_sifs.setter
    def reg_sifs(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sifs_msb, self.__reg_sifs_lsb, value)

    @property
    def reg_rxstartcck_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxstartcck_delay_msb, self.__reg_rxstartcck_delay_lsb)
    @reg_rxstartcck_delay.setter
    def reg_rxstartcck_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxstartcck_delay_msb, self.__reg_rxstartcck_delay_lsb, value)

    @property
    def reg_rxstartofdm_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxstartofdm_delay_msb, self.__reg_rxstartofdm_delay_lsb)
    @reg_rxstartofdm_delay.setter
    def reg_rxstartofdm_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxstartofdm_delay_msb, self.__reg_rxstartofdm_delay_lsb, value)
class MACDELAY(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x48
        self.__reg_txcck_delay_lsb = 24
        self.__reg_txcck_delay_msb = 31
        self.__reg_txofdm_delay_lsb = 16
        self.__reg_txofdm_delay_msb = 23
        self.__reg_rxcck_delay_lsb = 8
        self.__reg_rxcck_delay_msb = 15
        self.__reg_rxofdm_delay_lsb = 0
        self.__reg_rxofdm_delay_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txcck_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txcck_delay_msb, self.__reg_txcck_delay_lsb)
    @reg_txcck_delay.setter
    def reg_txcck_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txcck_delay_msb, self.__reg_txcck_delay_lsb, value)

    @property
    def reg_txofdm_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txofdm_delay_msb, self.__reg_txofdm_delay_lsb)
    @reg_txofdm_delay.setter
    def reg_txofdm_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txofdm_delay_msb, self.__reg_txofdm_delay_lsb, value)

    @property
    def reg_rxcck_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxcck_delay_msb, self.__reg_rxcck_delay_lsb)
    @reg_rxcck_delay.setter
    def reg_rxcck_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxcck_delay_msb, self.__reg_rxcck_delay_lsb, value)

    @property
    def reg_rxofdm_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxofdm_delay_msb, self.__reg_rxofdm_delay_lsb)
    @reg_rxofdm_delay.setter
    def reg_rxofdm_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxofdm_delay_msb, self.__reg_rxofdm_delay_lsb, value)
class MACBB_INIT_VALUE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x4c
        self.__reg_bb_cca_ind_lsb = 30
        self.__reg_bb_cca_ind_msb = 31
        self.__reg_bb_cca_ind_ht40_sec_lsb = 28
        self.__reg_bb_cca_ind_ht40_sec_msb = 29
        self.__reg_bb_rx_is_bw40_lsb = 26
        self.__reg_bb_rx_is_bw40_msb = 27
        self.__reg_bb_rxframe_lsb = 24
        self.__reg_bb_rxframe_msb = 25
        self.__reg_bb_rxdata_valid_lsb = 22
        self.__reg_bb_rxdata_valid_msb = 23
        self.__reg_bb_txerror_lsb = 18
        self.__reg_bb_txerror_msb = 19
        self.__reg_bb_txframe_ack_lsb = 16
        self.__reg_bb_txframe_ack_msb = 17
        self.__reg_bb_txdata_ack_lsb = 14
        self.__reg_bb_txdata_ack_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bb_cca_ind(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_cca_ind_msb, self.__reg_bb_cca_ind_lsb)
    @reg_bb_cca_ind.setter
    def reg_bb_cca_ind(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_cca_ind_msb, self.__reg_bb_cca_ind_lsb, value)

    @property
    def reg_bb_cca_ind_ht40_sec(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_cca_ind_ht40_sec_msb, self.__reg_bb_cca_ind_ht40_sec_lsb)
    @reg_bb_cca_ind_ht40_sec.setter
    def reg_bb_cca_ind_ht40_sec(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_cca_ind_ht40_sec_msb, self.__reg_bb_cca_ind_ht40_sec_lsb, value)

    @property
    def reg_bb_rx_is_bw40(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_rx_is_bw40_msb, self.__reg_bb_rx_is_bw40_lsb)
    @reg_bb_rx_is_bw40.setter
    def reg_bb_rx_is_bw40(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_rx_is_bw40_msb, self.__reg_bb_rx_is_bw40_lsb, value)

    @property
    def reg_bb_rxframe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_rxframe_msb, self.__reg_bb_rxframe_lsb)
    @reg_bb_rxframe.setter
    def reg_bb_rxframe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_rxframe_msb, self.__reg_bb_rxframe_lsb, value)

    @property
    def reg_bb_rxdata_valid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_rxdata_valid_msb, self.__reg_bb_rxdata_valid_lsb)
    @reg_bb_rxdata_valid.setter
    def reg_bb_rxdata_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_rxdata_valid_msb, self.__reg_bb_rxdata_valid_lsb, value)

    @property
    def reg_bb_txerror(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_txerror_msb, self.__reg_bb_txerror_lsb)
    @reg_bb_txerror.setter
    def reg_bb_txerror(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_txerror_msb, self.__reg_bb_txerror_lsb, value)

    @property
    def reg_bb_txframe_ack(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_txframe_ack_msb, self.__reg_bb_txframe_ack_lsb)
    @reg_bb_txframe_ack.setter
    def reg_bb_txframe_ack(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_txframe_ack_msb, self.__reg_bb_txframe_ack_lsb, value)

    @property
    def reg_bb_txdata_ack(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_txdata_ack_msb, self.__reg_bb_txdata_ack_lsb)
    @reg_bb_txdata_ack.setter
    def reg_bb_txdata_ack(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_txdata_ack_msb, self.__reg_bb_txdata_ack_lsb, value)
class MACHUNGRECOVER(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x50
        self.__reg_mac_rxhung_recover_lsb = 31
        self.__reg_mac_rxhung_recover_msb = 31
        self.__reg_mac_rxhung_timer_lsb = 16
        self.__reg_mac_rxhung_timer_msb = 30
        self.__reg_mac_txhung_recover_lsb = 15
        self.__reg_mac_txhung_recover_msb = 15
        self.__reg_mac_txhung_timer_lsb = 0
        self.__reg_mac_txhung_timer_msb = 14
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_mac_rxhung_recover(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mac_rxhung_recover_msb, self.__reg_mac_rxhung_recover_lsb)
    @reg_mac_rxhung_recover.setter
    def reg_mac_rxhung_recover(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mac_rxhung_recover_msb, self.__reg_mac_rxhung_recover_lsb, value)

    @property
    def reg_mac_rxhung_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mac_rxhung_timer_msb, self.__reg_mac_rxhung_timer_lsb)
    @reg_mac_rxhung_timer.setter
    def reg_mac_rxhung_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mac_rxhung_timer_msb, self.__reg_mac_rxhung_timer_lsb, value)

    @property
    def reg_mac_txhung_recover(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mac_txhung_recover_msb, self.__reg_mac_txhung_recover_lsb)
    @reg_mac_txhung_recover.setter
    def reg_mac_txhung_recover(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mac_txhung_recover_msb, self.__reg_mac_txhung_recover_lsb, value)

    @property
    def reg_mac_txhung_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mac_txhung_timer_msb, self.__reg_mac_txhung_timer_lsb)
    @reg_mac_txhung_timer.setter
    def reg_mac_txhung_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mac_txhung_timer_msb, self.__reg_mac_txhung_timer_lsb, value)
class MACHUNGSTATE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x54
        self.__rxhung_statis_cnt_lsb = 24
        self.__rxhung_statis_cnt_msb = 31
        self.__txhung_statis_cnt_lsb = 16
        self.__txhung_statis_cnt_msb = 23
        self.__reg_hungst_clr_lsb = 0
        self.__reg_hungst_clr_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxhung_statis_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rxhung_statis_cnt_msb, self.__rxhung_statis_cnt_lsb)
    @rxhung_statis_cnt.setter
    def rxhung_statis_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxhung_statis_cnt_msb, self.__rxhung_statis_cnt_lsb, value)

    @property
    def txhung_statis_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__txhung_statis_cnt_msb, self.__txhung_statis_cnt_lsb)
    @txhung_statis_cnt.setter
    def txhung_statis_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__txhung_statis_cnt_msb, self.__txhung_statis_cnt_lsb, value)

    @property
    def reg_hungst_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_hungst_clr_msb, self.__reg_hungst_clr_lsb)
    @reg_hungst_clr.setter
    def reg_hungst_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_hungst_clr_msb, self.__reg_hungst_clr_lsb, value)
class MACAHBMTEST(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x58
        self.__reg_tx_ahbm_testaddr_lsb = 14
        self.__reg_tx_ahbm_testaddr_msb = 15
        self.__reg_tx_ahbm_testmode_lsb = 12
        self.__reg_tx_ahbm_testmode_msb = 13
        self.__reg_rxgetdscr_ahbm_testaddr_lsb = 10
        self.__reg_rxgetdscr_ahbm_testaddr_msb = 11
        self.__reg_rxgetdscr_ahbm_testmode_lsb = 8
        self.__reg_rxgetdscr_ahbm_testmode_msb = 9
        self.__reg_rxdscr_ahbm_testaddr_lsb = 6
        self.__reg_rxdscr_ahbm_testaddr_msb = 7
        self.__reg_rxdscr_ahbm_testmode_lsb = 4
        self.__reg_rxdscr_ahbm_testmode_msb = 5
        self.__reg_rx_ahbm_testaddr_lsb = 2
        self.__reg_rx_ahbm_testaddr_msb = 3
        self.__reg_rx_ahbm_testmode_lsb = 0
        self.__reg_rx_ahbm_testmode_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_ahbm_testaddr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_ahbm_testaddr_msb, self.__reg_tx_ahbm_testaddr_lsb)
    @reg_tx_ahbm_testaddr.setter
    def reg_tx_ahbm_testaddr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_ahbm_testaddr_msb, self.__reg_tx_ahbm_testaddr_lsb, value)

    @property
    def reg_tx_ahbm_testmode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_ahbm_testmode_msb, self.__reg_tx_ahbm_testmode_lsb)
    @reg_tx_ahbm_testmode.setter
    def reg_tx_ahbm_testmode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_ahbm_testmode_msb, self.__reg_tx_ahbm_testmode_lsb, value)

    @property
    def reg_rxgetdscr_ahbm_testaddr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxgetdscr_ahbm_testaddr_msb, self.__reg_rxgetdscr_ahbm_testaddr_lsb)
    @reg_rxgetdscr_ahbm_testaddr.setter
    def reg_rxgetdscr_ahbm_testaddr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxgetdscr_ahbm_testaddr_msb, self.__reg_rxgetdscr_ahbm_testaddr_lsb, value)

    @property
    def reg_rxgetdscr_ahbm_testmode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxgetdscr_ahbm_testmode_msb, self.__reg_rxgetdscr_ahbm_testmode_lsb)
    @reg_rxgetdscr_ahbm_testmode.setter
    def reg_rxgetdscr_ahbm_testmode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxgetdscr_ahbm_testmode_msb, self.__reg_rxgetdscr_ahbm_testmode_lsb, value)

    @property
    def reg_rxdscr_ahbm_testaddr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdscr_ahbm_testaddr_msb, self.__reg_rxdscr_ahbm_testaddr_lsb)
    @reg_rxdscr_ahbm_testaddr.setter
    def reg_rxdscr_ahbm_testaddr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdscr_ahbm_testaddr_msb, self.__reg_rxdscr_ahbm_testaddr_lsb, value)

    @property
    def reg_rxdscr_ahbm_testmode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxdscr_ahbm_testmode_msb, self.__reg_rxdscr_ahbm_testmode_lsb)
    @reg_rxdscr_ahbm_testmode.setter
    def reg_rxdscr_ahbm_testmode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxdscr_ahbm_testmode_msb, self.__reg_rxdscr_ahbm_testmode_lsb, value)

    @property
    def reg_rx_ahbm_testaddr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_ahbm_testaddr_msb, self.__reg_rx_ahbm_testaddr_lsb)
    @reg_rx_ahbm_testaddr.setter
    def reg_rx_ahbm_testaddr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_ahbm_testaddr_msb, self.__reg_rx_ahbm_testaddr_lsb, value)

    @property
    def reg_rx_ahbm_testmode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_ahbm_testmode_msb, self.__reg_rx_ahbm_testmode_lsb)
    @reg_rx_ahbm_testmode.setter
    def reg_rx_ahbm_testmode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_ahbm_testmode_msb, self.__reg_rx_ahbm_testmode_lsb, value)
class MACTXPMD(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x5c
        self.__txcomplete_state_lsb = 28
        self.__txcomplete_state_msb = 31
        self.__txcomplete_st_match_lsb = 24
        self.__txcomplete_st_match_msb = 27
        self.__txcomplete_errcode_lsb = 16
        self.__txcomplete_errcode_msb = 23
        self.__txstart_qsel_lsb = 12
        self.__txstart_qsel_msb = 15
        self.__txcomplete_qsel_lsb = 8
        self.__txcomplete_qsel_msb = 11
        self.__txend_state_lsb = 0
        self.__txend_state_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txcomplete_state(self):
        return self.__MEM.rdm(self.__addr, self.__txcomplete_state_msb, self.__txcomplete_state_lsb)
    @txcomplete_state.setter
    def txcomplete_state(self, value):
        return self.__MEM.wrm(self.__addr, self.__txcomplete_state_msb, self.__txcomplete_state_lsb, value)

    @property
    def txcomplete_st_match(self):
        return self.__MEM.rdm(self.__addr, self.__txcomplete_st_match_msb, self.__txcomplete_st_match_lsb)
    @txcomplete_st_match.setter
    def txcomplete_st_match(self, value):
        return self.__MEM.wrm(self.__addr, self.__txcomplete_st_match_msb, self.__txcomplete_st_match_lsb, value)

    @property
    def txcomplete_errcode(self):
        return self.__MEM.rdm(self.__addr, self.__txcomplete_errcode_msb, self.__txcomplete_errcode_lsb)
    @txcomplete_errcode.setter
    def txcomplete_errcode(self, value):
        return self.__MEM.wrm(self.__addr, self.__txcomplete_errcode_msb, self.__txcomplete_errcode_lsb, value)

    @property
    def txstart_qsel(self):
        return self.__MEM.rdm(self.__addr, self.__txstart_qsel_msb, self.__txstart_qsel_lsb)
    @txstart_qsel.setter
    def txstart_qsel(self, value):
        return self.__MEM.wrm(self.__addr, self.__txstart_qsel_msb, self.__txstart_qsel_lsb, value)

    @property
    def txcomplete_qsel(self):
        return self.__MEM.rdm(self.__addr, self.__txcomplete_qsel_msb, self.__txcomplete_qsel_lsb)
    @txcomplete_qsel.setter
    def txcomplete_qsel(self, value):
        return self.__MEM.wrm(self.__addr, self.__txcomplete_qsel_msb, self.__txcomplete_qsel_lsb, value)

    @property
    def txend_state(self):
        return self.__MEM.rdm(self.__addr, self.__txend_state_msb, self.__txend_state_lsb)
    @txend_state.setter
    def txend_state(self, value):
        return self.__MEM.wrm(self.__addr, self.__txend_state_msb, self.__txend_state_lsb, value)
class MACOPTIONS(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x60
        self.__reg_auto_filltsf_ena_lsb = 31
        self.__reg_auto_filltsf_ena_msb = 31
        self.__reg_txcompint_option_lsb = 30
        self.__reg_txcompint_option_msb = 30
        self.__reg_batab_ena_lsb = 29
        self.__reg_batab_ena_msb = 29
        self.__reg_waitingack_nocase_buffer_lsb = 28
        self.__reg_waitingack_nocase_buffer_msb = 28
        self.__reg_force_center_lsb = 27
        self.__reg_force_center_msb = 27
        self.__reg_btprio11_force_rxerr_lsb = 26
        self.__reg_btprio11_force_rxerr_msb = 26
        self.__reg_rxcw40frht_lsb = 25
        self.__reg_rxcw40frht_msb = 25
        self.__reg_tmstp_tsfup_filter_lsb = 24
        self.__reg_tmstp_tsfup_filter_msb = 24
        self.__reg_rxlastdscr_fix_lsb = 23
        self.__reg_rxlastdscr_fix_msb = 23
        self.__reg_duration_bwmode_lsb = 16
        self.__reg_duration_bwmode_msb = 17
        self.__reg_txrxtime_use_bb_lsb = 15
        self.__reg_txrxtime_use_bb_msb = 15
        self.__reg_rxapdumpmode_ena_lsb = 14
        self.__reg_rxapdumpmode_ena_msb = 14
        self.__reg_rxsamebm_err_ena_lsb = 13
        self.__reg_rxsamebm_err_ena_msb = 13
        self.__reg_txop_int_used_lsb = 11
        self.__reg_txop_int_used_msb = 11
        self.__reg_lock_autotx_lsb = 10
        self.__reg_lock_autotx_msb = 10
        self.__reg_rxsublen_replace_leglen_lsb = 9
        self.__reg_rxsublen_replace_leglen_msb = 9
        self.__reg_txht40_multilen_lsb = 8
        self.__reg_txht40_multilen_msb = 8
        self.__reg_txwaitack_till_timout_lsb = 7
        self.__reg_txwaitack_till_timout_msb = 7
        self.__reg_cca_equ_rxfram_lsb = 6
        self.__reg_cca_equ_rxfram_msb = 6
        self.__reg_txcol_version_lsb = 5
        self.__reg_txcol_version_msb = 5
        self.__reg_txampdu_disable_en_lsb = 4
        self.__reg_txampdu_disable_en_msb = 4
        self.__reg_txauto_len_calc_lsb = 2
        self.__reg_txauto_len_calc_msb = 2
        self.__reg_tx11n_len_check_lsb = 1
        self.__reg_tx11n_len_check_msb = 1
        self.__reg_schclk_en_lsb = 0
        self.__reg_schclk_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_auto_filltsf_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_auto_filltsf_ena_msb, self.__reg_auto_filltsf_ena_lsb)
    @reg_auto_filltsf_ena.setter
    def reg_auto_filltsf_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_auto_filltsf_ena_msb, self.__reg_auto_filltsf_ena_lsb, value)

    @property
    def reg_txcompint_option(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txcompint_option_msb, self.__reg_txcompint_option_lsb)
    @reg_txcompint_option.setter
    def reg_txcompint_option(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txcompint_option_msb, self.__reg_txcompint_option_lsb, value)

    @property
    def reg_batab_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_batab_ena_msb, self.__reg_batab_ena_lsb)
    @reg_batab_ena.setter
    def reg_batab_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_batab_ena_msb, self.__reg_batab_ena_lsb, value)

    @property
    def reg_waitingack_nocase_buffer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_waitingack_nocase_buffer_msb, self.__reg_waitingack_nocase_buffer_lsb)
    @reg_waitingack_nocase_buffer.setter
    def reg_waitingack_nocase_buffer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_waitingack_nocase_buffer_msb, self.__reg_waitingack_nocase_buffer_lsb, value)

    @property
    def reg_force_center(self):
        return self.__MEM.rdm(self.__addr, self.__reg_force_center_msb, self.__reg_force_center_lsb)
    @reg_force_center.setter
    def reg_force_center(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_force_center_msb, self.__reg_force_center_lsb, value)

    @property
    def reg_btprio11_force_rxerr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_btprio11_force_rxerr_msb, self.__reg_btprio11_force_rxerr_lsb)
    @reg_btprio11_force_rxerr.setter
    def reg_btprio11_force_rxerr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_btprio11_force_rxerr_msb, self.__reg_btprio11_force_rxerr_lsb, value)

    @property
    def reg_rxcw40frht(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxcw40frht_msb, self.__reg_rxcw40frht_lsb)
    @reg_rxcw40frht.setter
    def reg_rxcw40frht(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxcw40frht_msb, self.__reg_rxcw40frht_lsb, value)

    @property
    def reg_tmstp_tsfup_filter(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tmstp_tsfup_filter_msb, self.__reg_tmstp_tsfup_filter_lsb)
    @reg_tmstp_tsfup_filter.setter
    def reg_tmstp_tsfup_filter(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tmstp_tsfup_filter_msb, self.__reg_tmstp_tsfup_filter_lsb, value)

    @property
    def reg_rxlastdscr_fix(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxlastdscr_fix_msb, self.__reg_rxlastdscr_fix_lsb)
    @reg_rxlastdscr_fix.setter
    def reg_rxlastdscr_fix(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxlastdscr_fix_msb, self.__reg_rxlastdscr_fix_lsb, value)

    @property
    def reg_duration_bwmode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_duration_bwmode_msb, self.__reg_duration_bwmode_lsb)
    @reg_duration_bwmode.setter
    def reg_duration_bwmode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_duration_bwmode_msb, self.__reg_duration_bwmode_lsb, value)

    @property
    def reg_txrxtime_use_bb(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrxtime_use_bb_msb, self.__reg_txrxtime_use_bb_lsb)
    @reg_txrxtime_use_bb.setter
    def reg_txrxtime_use_bb(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrxtime_use_bb_msb, self.__reg_txrxtime_use_bb_lsb, value)

    @property
    def reg_rxapdumpmode_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxapdumpmode_ena_msb, self.__reg_rxapdumpmode_ena_lsb)
    @reg_rxapdumpmode_ena.setter
    def reg_rxapdumpmode_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxapdumpmode_ena_msb, self.__reg_rxapdumpmode_ena_lsb, value)

    @property
    def reg_rxsamebm_err_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxsamebm_err_ena_msb, self.__reg_rxsamebm_err_ena_lsb)
    @reg_rxsamebm_err_ena.setter
    def reg_rxsamebm_err_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxsamebm_err_ena_msb, self.__reg_rxsamebm_err_ena_lsb, value)

    @property
    def reg_txop_int_used(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop_int_used_msb, self.__reg_txop_int_used_lsb)
    @reg_txop_int_used.setter
    def reg_txop_int_used(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop_int_used_msb, self.__reg_txop_int_used_lsb, value)

    @property
    def reg_lock_autotx(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lock_autotx_msb, self.__reg_lock_autotx_lsb)
    @reg_lock_autotx.setter
    def reg_lock_autotx(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lock_autotx_msb, self.__reg_lock_autotx_lsb, value)

    @property
    def reg_rxsublen_replace_leglen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxsublen_replace_leglen_msb, self.__reg_rxsublen_replace_leglen_lsb)
    @reg_rxsublen_replace_leglen.setter
    def reg_rxsublen_replace_leglen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxsublen_replace_leglen_msb, self.__reg_rxsublen_replace_leglen_lsb, value)

    @property
    def reg_txht40_multilen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txht40_multilen_msb, self.__reg_txht40_multilen_lsb)
    @reg_txht40_multilen.setter
    def reg_txht40_multilen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txht40_multilen_msb, self.__reg_txht40_multilen_lsb, value)

    @property
    def reg_txwaitack_till_timout(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txwaitack_till_timout_msb, self.__reg_txwaitack_till_timout_lsb)
    @reg_txwaitack_till_timout.setter
    def reg_txwaitack_till_timout(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txwaitack_till_timout_msb, self.__reg_txwaitack_till_timout_lsb, value)

    @property
    def reg_cca_equ_rxfram(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cca_equ_rxfram_msb, self.__reg_cca_equ_rxfram_lsb)
    @reg_cca_equ_rxfram.setter
    def reg_cca_equ_rxfram(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cca_equ_rxfram_msb, self.__reg_cca_equ_rxfram_lsb, value)

    @property
    def reg_txcol_version(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txcol_version_msb, self.__reg_txcol_version_lsb)
    @reg_txcol_version.setter
    def reg_txcol_version(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txcol_version_msb, self.__reg_txcol_version_lsb, value)

    @property
    def reg_txampdu_disable_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txampdu_disable_en_msb, self.__reg_txampdu_disable_en_lsb)
    @reg_txampdu_disable_en.setter
    def reg_txampdu_disable_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txampdu_disable_en_msb, self.__reg_txampdu_disable_en_lsb, value)

    @property
    def reg_txauto_len_calc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txauto_len_calc_msb, self.__reg_txauto_len_calc_lsb)
    @reg_txauto_len_calc.setter
    def reg_txauto_len_calc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txauto_len_calc_msb, self.__reg_txauto_len_calc_lsb, value)

    @property
    def reg_tx11n_len_check(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx11n_len_check_msb, self.__reg_tx11n_len_check_lsb)
    @reg_tx11n_len_check.setter
    def reg_tx11n_len_check(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx11n_len_check_msb, self.__reg_tx11n_len_check_lsb, value)

    @property
    def reg_schclk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_schclk_en_msb, self.__reg_schclk_en_lsb)
    @reg_schclk_en.setter
    def reg_schclk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_schclk_en_msb, self.__reg_schclk_en_lsb, value)
class MACSECOND_CCACONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x64
        self.__reg_txdata_ht40_care_curseccca_lsb = 31
        self.__reg_txdata_ht40_care_curseccca_msb = 31
        self.__reg_txdata_ht40_care_rxcts_lsb = 30
        self.__reg_txdata_ht40_care_rxcts_msb = 30
        self.__reg_txdata_ht20_care_rxcts_lsb = 29
        self.__reg_txdata_ht20_care_rxcts_msb = 29
        self.__reg_autorxtxcts_care_curseccca_lsb = 28
        self.__reg_autorxtxcts_care_curseccca_msb = 28
        self.__reg_secondcca_count_lsb = 0
        self.__reg_secondcca_count_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txdata_ht40_care_curseccca(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txdata_ht40_care_curseccca_msb, self.__reg_txdata_ht40_care_curseccca_lsb)
    @reg_txdata_ht40_care_curseccca.setter
    def reg_txdata_ht40_care_curseccca(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txdata_ht40_care_curseccca_msb, self.__reg_txdata_ht40_care_curseccca_lsb, value)

    @property
    def reg_txdata_ht40_care_rxcts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txdata_ht40_care_rxcts_msb, self.__reg_txdata_ht40_care_rxcts_lsb)
    @reg_txdata_ht40_care_rxcts.setter
    def reg_txdata_ht40_care_rxcts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txdata_ht40_care_rxcts_msb, self.__reg_txdata_ht40_care_rxcts_lsb, value)

    @property
    def reg_txdata_ht20_care_rxcts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txdata_ht20_care_rxcts_msb, self.__reg_txdata_ht20_care_rxcts_lsb)
    @reg_txdata_ht20_care_rxcts.setter
    def reg_txdata_ht20_care_rxcts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txdata_ht20_care_rxcts_msb, self.__reg_txdata_ht20_care_rxcts_lsb, value)

    @property
    def reg_autorxtxcts_care_curseccca(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autorxtxcts_care_curseccca_msb, self.__reg_autorxtxcts_care_curseccca_lsb)
    @reg_autorxtxcts_care_curseccca.setter
    def reg_autorxtxcts_care_curseccca(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autorxtxcts_care_curseccca_msb, self.__reg_autorxtxcts_care_curseccca_lsb, value)

    @property
    def reg_secondcca_count(self):
        return self.__MEM.rdm(self.__addr, self.__reg_secondcca_count_msb, self.__reg_secondcca_count_lsb)
    @reg_secondcca_count.setter
    def reg_secondcca_count(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_secondcca_count_msb, self.__reg_secondcca_count_lsb, value)
class MACRXTXOPTION(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x68
        self.__reg_autotxcts_imr_lsb = 3
        self.__reg_autotxcts_imr_msb = 3
        self.__reg_txack_pmg_lsb = 2
        self.__reg_txack_pmg_msb = 2
        self.__reg_txba_pmg_lsb = 1
        self.__reg_txba_pmg_msb = 1
        self.__reg_txmcs_sel_lsb = 0
        self.__reg_txmcs_sel_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_autotxcts_imr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autotxcts_imr_msb, self.__reg_autotxcts_imr_lsb)
    @reg_autotxcts_imr.setter
    def reg_autotxcts_imr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autotxcts_imr_msb, self.__reg_autotxcts_imr_lsb, value)

    @property
    def reg_txack_pmg(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txack_pmg_msb, self.__reg_txack_pmg_lsb)
    @reg_txack_pmg.setter
    def reg_txack_pmg(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txack_pmg_msb, self.__reg_txack_pmg_lsb, value)

    @property
    def reg_txba_pmg(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txba_pmg_msb, self.__reg_txba_pmg_lsb)
    @reg_txba_pmg.setter
    def reg_txba_pmg(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txba_pmg_msb, self.__reg_txba_pmg_lsb, value)

    @property
    def reg_txmcs_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txmcs_sel_msb, self.__reg_txmcs_sel_lsb)
    @reg_txmcs_sel.setter
    def reg_txmcs_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txmcs_sel_msb, self.__reg_txmcs_sel_lsb, value)
class MACAUTOTXRX_ENA(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x6c
        self.__reg_autotx_ena_lsb = 1
        self.__reg_autotx_ena_msb = 1
        self.__reg_autorxtx_ena_lsb = 0
        self.__reg_autorxtx_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_autotx_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autotx_ena_msb, self.__reg_autotx_ena_lsb)
    @reg_autotx_ena.setter
    def reg_autotx_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autotx_ena_msb, self.__reg_autotx_ena_lsb, value)

    @property
    def reg_autorxtx_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autorxtx_ena_msb, self.__reg_autorxtx_ena_lsb)
    @reg_autorxtx_ena.setter
    def reg_autorxtx_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autorxtx_ena_msb, self.__reg_autorxtx_ena_lsb, value)
class MACTXRX_TAB0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x70
        self.__reg_txrx_assreq_lsb = 28
        self.__reg_txrx_assreq_msb = 31
        self.__reg_txrx_assres_lsb = 24
        self.__reg_txrx_assres_msb = 27
        self.__reg_txrx_reareq_lsb = 20
        self.__reg_txrx_reareq_msb = 23
        self.__reg_txrx_reares_lsb = 16
        self.__reg_txrx_reares_msb = 19
        self.__reg_txrx_proreq_lsb = 12
        self.__reg_txrx_proreq_msb = 15
        self.__reg_txrx_prores_lsb = 8
        self.__reg_txrx_prores_msb = 11
        self.__reg_txrx_000110_lsb = 4
        self.__reg_txrx_000110_msb = 7
        self.__reg_txrx_000111_lsb = 0
        self.__reg_txrx_000111_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txrx_assreq(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_assreq_msb, self.__reg_txrx_assreq_lsb)
    @reg_txrx_assreq.setter
    def reg_txrx_assreq(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_assreq_msb, self.__reg_txrx_assreq_lsb, value)

    @property
    def reg_txrx_assres(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_assres_msb, self.__reg_txrx_assres_lsb)
    @reg_txrx_assres.setter
    def reg_txrx_assres(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_assres_msb, self.__reg_txrx_assres_lsb, value)

    @property
    def reg_txrx_reareq(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_reareq_msb, self.__reg_txrx_reareq_lsb)
    @reg_txrx_reareq.setter
    def reg_txrx_reareq(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_reareq_msb, self.__reg_txrx_reareq_lsb, value)

    @property
    def reg_txrx_reares(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_reares_msb, self.__reg_txrx_reares_lsb)
    @reg_txrx_reares.setter
    def reg_txrx_reares(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_reares_msb, self.__reg_txrx_reares_lsb, value)

    @property
    def reg_txrx_proreq(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_proreq_msb, self.__reg_txrx_proreq_lsb)
    @reg_txrx_proreq.setter
    def reg_txrx_proreq(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_proreq_msb, self.__reg_txrx_proreq_lsb, value)

    @property
    def reg_txrx_prores(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_prores_msb, self.__reg_txrx_prores_lsb)
    @reg_txrx_prores.setter
    def reg_txrx_prores(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_prores_msb, self.__reg_txrx_prores_lsb, value)

    @property
    def reg_txrx_000110(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_000110_msb, self.__reg_txrx_000110_lsb)
    @reg_txrx_000110.setter
    def reg_txrx_000110(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_000110_msb, self.__reg_txrx_000110_lsb, value)

    @property
    def reg_txrx_000111(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_000111_msb, self.__reg_txrx_000111_lsb)
    @reg_txrx_000111.setter
    def reg_txrx_000111(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_000111_msb, self.__reg_txrx_000111_lsb, value)
class MACTXRX_TAB1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x74
        self.__reg_txrx_beacon_lsb = 28
        self.__reg_txrx_beacon_msb = 31
        self.__reg_txrx_atim_lsb = 24
        self.__reg_txrx_atim_msb = 27
        self.__reg_txrx_disass_lsb = 20
        self.__reg_txrx_disass_msb = 23
        self.__reg_txrx_authen_lsb = 16
        self.__reg_txrx_authen_msb = 19
        self.__reg_txrx_deauth_lsb = 12
        self.__reg_txrx_deauth_msb = 15
        self.__reg_txrx_action_lsb = 8
        self.__reg_txrx_action_msb = 11
        self.__reg_txrx_actnoack_lsb = 4
        self.__reg_txrx_actnoack_msb = 7
        self.__reg_txrx_001111_lsb = 0
        self.__reg_txrx_001111_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txrx_beacon(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_beacon_msb, self.__reg_txrx_beacon_lsb)
    @reg_txrx_beacon.setter
    def reg_txrx_beacon(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_beacon_msb, self.__reg_txrx_beacon_lsb, value)

    @property
    def reg_txrx_atim(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_atim_msb, self.__reg_txrx_atim_lsb)
    @reg_txrx_atim.setter
    def reg_txrx_atim(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_atim_msb, self.__reg_txrx_atim_lsb, value)

    @property
    def reg_txrx_disass(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_disass_msb, self.__reg_txrx_disass_lsb)
    @reg_txrx_disass.setter
    def reg_txrx_disass(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_disass_msb, self.__reg_txrx_disass_lsb, value)

    @property
    def reg_txrx_authen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_authen_msb, self.__reg_txrx_authen_lsb)
    @reg_txrx_authen.setter
    def reg_txrx_authen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_authen_msb, self.__reg_txrx_authen_lsb, value)

    @property
    def reg_txrx_deauth(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_deauth_msb, self.__reg_txrx_deauth_lsb)
    @reg_txrx_deauth.setter
    def reg_txrx_deauth(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_deauth_msb, self.__reg_txrx_deauth_lsb, value)

    @property
    def reg_txrx_action(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_action_msb, self.__reg_txrx_action_lsb)
    @reg_txrx_action.setter
    def reg_txrx_action(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_action_msb, self.__reg_txrx_action_lsb, value)

    @property
    def reg_txrx_actnoack(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_actnoack_msb, self.__reg_txrx_actnoack_lsb)
    @reg_txrx_actnoack.setter
    def reg_txrx_actnoack(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_actnoack_msb, self.__reg_txrx_actnoack_lsb, value)

    @property
    def reg_txrx_001111(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_001111_msb, self.__reg_txrx_001111_lsb)
    @reg_txrx_001111.setter
    def reg_txrx_001111(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_001111_msb, self.__reg_txrx_001111_lsb, value)
class MACTXRX_TAB2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x78
        self.__reg_txrx_010000_lsb = 28
        self.__reg_txrx_010000_msb = 31
        self.__reg_txrx_010001_lsb = 24
        self.__reg_txrx_010001_msb = 27
        self.__reg_txrx_010010_lsb = 20
        self.__reg_txrx_010010_msb = 23
        self.__reg_txrx_010011_lsb = 16
        self.__reg_txrx_010011_msb = 19
        self.__reg_txrx_010100_lsb = 12
        self.__reg_txrx_010100_msb = 15
        self.__reg_txrx_010101_lsb = 8
        self.__reg_txrx_010101_msb = 11
        self.__reg_txrx_010110_lsb = 4
        self.__reg_txrx_010110_msb = 7
        self.__reg_txrx_conwar_lsb = 0
        self.__reg_txrx_conwar_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txrx_010000(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_010000_msb, self.__reg_txrx_010000_lsb)
    @reg_txrx_010000.setter
    def reg_txrx_010000(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_010000_msb, self.__reg_txrx_010000_lsb, value)

    @property
    def reg_txrx_010001(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_010001_msb, self.__reg_txrx_010001_lsb)
    @reg_txrx_010001.setter
    def reg_txrx_010001(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_010001_msb, self.__reg_txrx_010001_lsb, value)

    @property
    def reg_txrx_010010(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_010010_msb, self.__reg_txrx_010010_lsb)
    @reg_txrx_010010.setter
    def reg_txrx_010010(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_010010_msb, self.__reg_txrx_010010_lsb, value)

    @property
    def reg_txrx_010011(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_010011_msb, self.__reg_txrx_010011_lsb)
    @reg_txrx_010011.setter
    def reg_txrx_010011(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_010011_msb, self.__reg_txrx_010011_lsb, value)

    @property
    def reg_txrx_010100(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_010100_msb, self.__reg_txrx_010100_lsb)
    @reg_txrx_010100.setter
    def reg_txrx_010100(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_010100_msb, self.__reg_txrx_010100_lsb, value)

    @property
    def reg_txrx_010101(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_010101_msb, self.__reg_txrx_010101_lsb)
    @reg_txrx_010101.setter
    def reg_txrx_010101(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_010101_msb, self.__reg_txrx_010101_lsb, value)

    @property
    def reg_txrx_010110(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_010110_msb, self.__reg_txrx_010110_lsb)
    @reg_txrx_010110.setter
    def reg_txrx_010110(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_010110_msb, self.__reg_txrx_010110_lsb, value)

    @property
    def reg_txrx_conwar(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_conwar_msb, self.__reg_txrx_conwar_lsb)
    @reg_txrx_conwar.setter
    def reg_txrx_conwar(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_conwar_msb, self.__reg_txrx_conwar_lsb, value)
class MACTXRX_TAB3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x7c
        self.__reg_txrx_bareq_lsb = 28
        self.__reg_txrx_bareq_msb = 31
        self.__reg_txrx_ba_lsb = 24
        self.__reg_txrx_ba_msb = 27
        self.__reg_txrx_pspoll_lsb = 20
        self.__reg_txrx_pspoll_msb = 23
        self.__reg_txrx_rts_lsb = 16
        self.__reg_txrx_rts_msb = 19
        self.__reg_txrx_cts_lsb = 12
        self.__reg_txrx_cts_msb = 15
        self.__reg_txrx_ack_lsb = 8
        self.__reg_txrx_ack_msb = 11
        self.__reg_txrx_cfend_lsb = 4
        self.__reg_txrx_cfend_msb = 7
        self.__reg_txrx_cfendcfack_lsb = 0
        self.__reg_txrx_cfendcfack_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txrx_bareq(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_bareq_msb, self.__reg_txrx_bareq_lsb)
    @reg_txrx_bareq.setter
    def reg_txrx_bareq(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_bareq_msb, self.__reg_txrx_bareq_lsb, value)

    @property
    def reg_txrx_ba(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_ba_msb, self.__reg_txrx_ba_lsb)
    @reg_txrx_ba.setter
    def reg_txrx_ba(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_ba_msb, self.__reg_txrx_ba_lsb, value)

    @property
    def reg_txrx_pspoll(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_pspoll_msb, self.__reg_txrx_pspoll_lsb)
    @reg_txrx_pspoll.setter
    def reg_txrx_pspoll(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_pspoll_msb, self.__reg_txrx_pspoll_lsb, value)

    @property
    def reg_txrx_rts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_rts_msb, self.__reg_txrx_rts_lsb)
    @reg_txrx_rts.setter
    def reg_txrx_rts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_rts_msb, self.__reg_txrx_rts_lsb, value)

    @property
    def reg_txrx_cts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_cts_msb, self.__reg_txrx_cts_lsb)
    @reg_txrx_cts.setter
    def reg_txrx_cts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_cts_msb, self.__reg_txrx_cts_lsb, value)

    @property
    def reg_txrx_ack(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_ack_msb, self.__reg_txrx_ack_lsb)
    @reg_txrx_ack.setter
    def reg_txrx_ack(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_ack_msb, self.__reg_txrx_ack_lsb, value)

    @property
    def reg_txrx_cfend(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_cfend_msb, self.__reg_txrx_cfend_lsb)
    @reg_txrx_cfend.setter
    def reg_txrx_cfend(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_cfend_msb, self.__reg_txrx_cfend_lsb, value)

    @property
    def reg_txrx_cfendcfack(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_cfendcfack_msb, self.__reg_txrx_cfendcfack_lsb)
    @reg_txrx_cfendcfack.setter
    def reg_txrx_cfendcfack(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_cfendcfack_msb, self.__reg_txrx_cfendcfack_lsb, value)
class MACTXRX_TAB4(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x80
        self.__reg_txrx_data_lsb = 28
        self.__reg_txrx_data_msb = 31
        self.__reg_txrx_datacfack_lsb = 24
        self.__reg_txrx_datacfack_msb = 27
        self.__reg_txrx_datacfpoll_lsb = 20
        self.__reg_txrx_datacfpoll_msb = 23
        self.__reg_txrx_datacfackcfpoll_lsb = 16
        self.__reg_txrx_datacfackcfpoll_msb = 19
        self.__reg_txrx_null_lsb = 12
        self.__reg_txrx_null_msb = 15
        self.__reg_txrx_cfack_lsb = 8
        self.__reg_txrx_cfack_msb = 11
        self.__reg_txrx_cfpoll_lsb = 4
        self.__reg_txrx_cfpoll_msb = 7
        self.__reg_txrx_cfackcfpoll_lsb = 0
        self.__reg_txrx_cfackcfpoll_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txrx_data(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_data_msb, self.__reg_txrx_data_lsb)
    @reg_txrx_data.setter
    def reg_txrx_data(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_data_msb, self.__reg_txrx_data_lsb, value)

    @property
    def reg_txrx_datacfack(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_datacfack_msb, self.__reg_txrx_datacfack_lsb)
    @reg_txrx_datacfack.setter
    def reg_txrx_datacfack(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_datacfack_msb, self.__reg_txrx_datacfack_lsb, value)

    @property
    def reg_txrx_datacfpoll(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_datacfpoll_msb, self.__reg_txrx_datacfpoll_lsb)
    @reg_txrx_datacfpoll.setter
    def reg_txrx_datacfpoll(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_datacfpoll_msb, self.__reg_txrx_datacfpoll_lsb, value)

    @property
    def reg_txrx_datacfackcfpoll(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_datacfackcfpoll_msb, self.__reg_txrx_datacfackcfpoll_lsb)
    @reg_txrx_datacfackcfpoll.setter
    def reg_txrx_datacfackcfpoll(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_datacfackcfpoll_msb, self.__reg_txrx_datacfackcfpoll_lsb, value)

    @property
    def reg_txrx_null(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_null_msb, self.__reg_txrx_null_lsb)
    @reg_txrx_null.setter
    def reg_txrx_null(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_null_msb, self.__reg_txrx_null_lsb, value)

    @property
    def reg_txrx_cfack(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_cfack_msb, self.__reg_txrx_cfack_lsb)
    @reg_txrx_cfack.setter
    def reg_txrx_cfack(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_cfack_msb, self.__reg_txrx_cfack_lsb, value)

    @property
    def reg_txrx_cfpoll(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_cfpoll_msb, self.__reg_txrx_cfpoll_lsb)
    @reg_txrx_cfpoll.setter
    def reg_txrx_cfpoll(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_cfpoll_msb, self.__reg_txrx_cfpoll_lsb, value)

    @property
    def reg_txrx_cfackcfpoll(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_cfackcfpoll_msb, self.__reg_txrx_cfackcfpoll_lsb)
    @reg_txrx_cfackcfpoll.setter
    def reg_txrx_cfackcfpoll(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_cfackcfpoll_msb, self.__reg_txrx_cfackcfpoll_lsb, value)
class MACTXRX_TAB5(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x84
        self.__reg_txrx_qosdata_lsb = 28
        self.__reg_txrx_qosdata_msb = 31
        self.__reg_txrx_qosdatacfack_lsb = 24
        self.__reg_txrx_qosdatacfack_msb = 27
        self.__reg_txrx_qosdatacfpoll_lsb = 20
        self.__reg_txrx_qosdatacfpoll_msb = 23
        self.__reg_txrx_qosdatacfackcfpoll_lsb = 16
        self.__reg_txrx_qosdatacfackcfpoll_msb = 19
        self.__reg_txrx_qosnull_lsb = 12
        self.__reg_txrx_qosnull_msb = 15
        self.__reg_txrx_101101_lsb = 8
        self.__reg_txrx_101101_msb = 11
        self.__reg_txrx_qoscpoll_lsb = 4
        self.__reg_txrx_qoscpoll_msb = 7
        self.__reg_txrx_qoscfackcfpoll_lsb = 0
        self.__reg_txrx_qoscfackcfpoll_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txrx_qosdata(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_qosdata_msb, self.__reg_txrx_qosdata_lsb)
    @reg_txrx_qosdata.setter
    def reg_txrx_qosdata(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_qosdata_msb, self.__reg_txrx_qosdata_lsb, value)

    @property
    def reg_txrx_qosdatacfack(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_qosdatacfack_msb, self.__reg_txrx_qosdatacfack_lsb)
    @reg_txrx_qosdatacfack.setter
    def reg_txrx_qosdatacfack(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_qosdatacfack_msb, self.__reg_txrx_qosdatacfack_lsb, value)

    @property
    def reg_txrx_qosdatacfpoll(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_qosdatacfpoll_msb, self.__reg_txrx_qosdatacfpoll_lsb)
    @reg_txrx_qosdatacfpoll.setter
    def reg_txrx_qosdatacfpoll(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_qosdatacfpoll_msb, self.__reg_txrx_qosdatacfpoll_lsb, value)

    @property
    def reg_txrx_qosdatacfackcfpoll(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_qosdatacfackcfpoll_msb, self.__reg_txrx_qosdatacfackcfpoll_lsb)
    @reg_txrx_qosdatacfackcfpoll.setter
    def reg_txrx_qosdatacfackcfpoll(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_qosdatacfackcfpoll_msb, self.__reg_txrx_qosdatacfackcfpoll_lsb, value)

    @property
    def reg_txrx_qosnull(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_qosnull_msb, self.__reg_txrx_qosnull_lsb)
    @reg_txrx_qosnull.setter
    def reg_txrx_qosnull(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_qosnull_msb, self.__reg_txrx_qosnull_lsb, value)

    @property
    def reg_txrx_101101(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_101101_msb, self.__reg_txrx_101101_lsb)
    @reg_txrx_101101.setter
    def reg_txrx_101101(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_101101_msb, self.__reg_txrx_101101_lsb, value)

    @property
    def reg_txrx_qoscpoll(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_qoscpoll_msb, self.__reg_txrx_qoscpoll_lsb)
    @reg_txrx_qoscpoll.setter
    def reg_txrx_qoscpoll(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_qoscpoll_msb, self.__reg_txrx_qoscpoll_lsb, value)

    @property
    def reg_txrx_qoscfackcfpoll(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_qoscfackcfpoll_msb, self.__reg_txrx_qoscfackcfpoll_lsb)
    @reg_txrx_qoscfackcfpoll.setter
    def reg_txrx_qoscfackcfpoll(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_qoscfackcfpoll_msb, self.__reg_txrx_qoscfackcfpoll_lsb, value)
class MACTXRX_QNUM(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x88
        self.__reg_beacon_qnum_lsb = 4
        self.__reg_beacon_qnum_msb = 7
        self.__reg_txrx_qnum_lsb = 0
        self.__reg_txrx_qnum_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_beacon_qnum(self):
        return self.__MEM.rdm(self.__addr, self.__reg_beacon_qnum_msb, self.__reg_beacon_qnum_lsb)
    @reg_beacon_qnum.setter
    def reg_beacon_qnum(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_beacon_qnum_msb, self.__reg_beacon_qnum_lsb, value)

    @property
    def reg_txrx_qnum(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrx_qnum_msb, self.__reg_txrx_qnum_lsb)
    @reg_txrx_qnum.setter
    def reg_txrx_qnum(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrx_qnum_msb, self.__reg_txrx_qnum_lsb, value)
class MACTXTARGET(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x8c
        self.__reg_tx_target_lsb = 0
        self.__reg_tx_target_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_target(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_target_msb, self.__reg_tx_target_lsb)
    @reg_tx_target.setter
    def reg_tx_target(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_target_msb, self.__reg_tx_target_lsb, value)
class MACTXTARGET_ENA(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x90
        self.__reg_txtime_ena_lsb = 0
        self.__reg_txtime_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txtime_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txtime_ena_msb, self.__reg_txtime_ena_lsb)
    @reg_txtime_ena.setter
    def reg_txtime_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txtime_ena_msb, self.__reg_txtime_ena_lsb, value)
class MACTXQ_BLOCK(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x94
        self.__reg_tximr2_com_stop_lsb = 26
        self.__reg_tximr2_com_stop_msb = 26
        self.__reg_tximr1_com_stop_lsb = 25
        self.__reg_tximr1_com_stop_msb = 25
        self.__reg_tximr0_com_stop_lsb = 24
        self.__reg_tximr0_com_stop_msb = 24
        self.__reg_txq7_com_stop_lsb = 23
        self.__reg_txq7_com_stop_msb = 23
        self.__reg_txq6_com_stop_lsb = 22
        self.__reg_txq6_com_stop_msb = 22
        self.__reg_txq5_com_stop_lsb = 21
        self.__reg_txq5_com_stop_msb = 21
        self.__reg_txq4_com_stop_lsb = 20
        self.__reg_txq4_com_stop_msb = 20
        self.__reg_txq3_com_stop_lsb = 19
        self.__reg_txq3_com_stop_msb = 19
        self.__reg_txq2_com_stop_lsb = 18
        self.__reg_txq2_com_stop_msb = 18
        self.__reg_txq1_com_stop_lsb = 17
        self.__reg_txq1_com_stop_msb = 17
        self.__reg_txq0_com_stop_lsb = 16
        self.__reg_txq0_com_stop_msb = 16
        self.__reg_autorxtx_stop_lsb = 15
        self.__reg_autorxtx_stop_msb = 15
        self.__rxing_lsb = 14
        self.__rxing_msb = 14
        self.__txing_lsb = 13
        self.__txing_msb = 13
        self.__reg_rxblock_lsb = 12
        self.__reg_rxblock_msb = 12
        self.__reg_tximr2_block_lsb = 10
        self.__reg_tximr2_block_msb = 10
        self.__reg_tximr1_block_lsb = 9
        self.__reg_tximr1_block_msb = 9
        self.__reg_tximr0_block_lsb = 8
        self.__reg_tximr0_block_msb = 8
        self.__reg_txq7_block_lsb = 7
        self.__reg_txq7_block_msb = 7
        self.__reg_txq6_block_lsb = 6
        self.__reg_txq6_block_msb = 6
        self.__reg_txq5_block_lsb = 5
        self.__reg_txq5_block_msb = 5
        self.__reg_txq4_block_lsb = 4
        self.__reg_txq4_block_msb = 4
        self.__reg_txq3_block_lsb = 3
        self.__reg_txq3_block_msb = 3
        self.__reg_txq2_block_lsb = 2
        self.__reg_txq2_block_msb = 2
        self.__reg_txq1_block_lsb = 1
        self.__reg_txq1_block_msb = 1
        self.__reg_txq0_block_lsb = 0
        self.__reg_txq0_block_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr2_com_stop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_com_stop_msb, self.__reg_tximr2_com_stop_lsb)
    @reg_tximr2_com_stop.setter
    def reg_tximr2_com_stop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_com_stop_msb, self.__reg_tximr2_com_stop_lsb, value)

    @property
    def reg_tximr1_com_stop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_com_stop_msb, self.__reg_tximr1_com_stop_lsb)
    @reg_tximr1_com_stop.setter
    def reg_tximr1_com_stop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_com_stop_msb, self.__reg_tximr1_com_stop_lsb, value)

    @property
    def reg_tximr0_com_stop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_com_stop_msb, self.__reg_tximr0_com_stop_lsb)
    @reg_tximr0_com_stop.setter
    def reg_tximr0_com_stop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_com_stop_msb, self.__reg_tximr0_com_stop_lsb, value)

    @property
    def reg_txq7_com_stop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_com_stop_msb, self.__reg_txq7_com_stop_lsb)
    @reg_txq7_com_stop.setter
    def reg_txq7_com_stop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_com_stop_msb, self.__reg_txq7_com_stop_lsb, value)

    @property
    def reg_txq6_com_stop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_com_stop_msb, self.__reg_txq6_com_stop_lsb)
    @reg_txq6_com_stop.setter
    def reg_txq6_com_stop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_com_stop_msb, self.__reg_txq6_com_stop_lsb, value)

    @property
    def reg_txq5_com_stop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_com_stop_msb, self.__reg_txq5_com_stop_lsb)
    @reg_txq5_com_stop.setter
    def reg_txq5_com_stop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_com_stop_msb, self.__reg_txq5_com_stop_lsb, value)

    @property
    def reg_txq4_com_stop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_com_stop_msb, self.__reg_txq4_com_stop_lsb)
    @reg_txq4_com_stop.setter
    def reg_txq4_com_stop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_com_stop_msb, self.__reg_txq4_com_stop_lsb, value)

    @property
    def reg_txq3_com_stop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_com_stop_msb, self.__reg_txq3_com_stop_lsb)
    @reg_txq3_com_stop.setter
    def reg_txq3_com_stop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_com_stop_msb, self.__reg_txq3_com_stop_lsb, value)

    @property
    def reg_txq2_com_stop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_com_stop_msb, self.__reg_txq2_com_stop_lsb)
    @reg_txq2_com_stop.setter
    def reg_txq2_com_stop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_com_stop_msb, self.__reg_txq2_com_stop_lsb, value)

    @property
    def reg_txq1_com_stop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_com_stop_msb, self.__reg_txq1_com_stop_lsb)
    @reg_txq1_com_stop.setter
    def reg_txq1_com_stop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_com_stop_msb, self.__reg_txq1_com_stop_lsb, value)

    @property
    def reg_txq0_com_stop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_com_stop_msb, self.__reg_txq0_com_stop_lsb)
    @reg_txq0_com_stop.setter
    def reg_txq0_com_stop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_com_stop_msb, self.__reg_txq0_com_stop_lsb, value)

    @property
    def reg_autorxtx_stop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_autorxtx_stop_msb, self.__reg_autorxtx_stop_lsb)
    @reg_autorxtx_stop.setter
    def reg_autorxtx_stop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_autorxtx_stop_msb, self.__reg_autorxtx_stop_lsb, value)

    @property
    def rxing(self):
        return self.__MEM.rdm(self.__addr, self.__rxing_msb, self.__rxing_lsb)
    @rxing.setter
    def rxing(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxing_msb, self.__rxing_lsb, value)

    @property
    def txing(self):
        return self.__MEM.rdm(self.__addr, self.__txing_msb, self.__txing_lsb)
    @txing.setter
    def txing(self, value):
        return self.__MEM.wrm(self.__addr, self.__txing_msb, self.__txing_lsb, value)

    @property
    def reg_rxblock(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxblock_msb, self.__reg_rxblock_lsb)
    @reg_rxblock.setter
    def reg_rxblock(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxblock_msb, self.__reg_rxblock_lsb, value)

    @property
    def reg_tximr2_block(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_block_msb, self.__reg_tximr2_block_lsb)
    @reg_tximr2_block.setter
    def reg_tximr2_block(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_block_msb, self.__reg_tximr2_block_lsb, value)

    @property
    def reg_tximr1_block(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_block_msb, self.__reg_tximr1_block_lsb)
    @reg_tximr1_block.setter
    def reg_tximr1_block(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_block_msb, self.__reg_tximr1_block_lsb, value)

    @property
    def reg_tximr0_block(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_block_msb, self.__reg_tximr0_block_lsb)
    @reg_tximr0_block.setter
    def reg_tximr0_block(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_block_msb, self.__reg_tximr0_block_lsb, value)

    @property
    def reg_txq7_block(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_block_msb, self.__reg_txq7_block_lsb)
    @reg_txq7_block.setter
    def reg_txq7_block(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_block_msb, self.__reg_txq7_block_lsb, value)

    @property
    def reg_txq6_block(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_block_msb, self.__reg_txq6_block_lsb)
    @reg_txq6_block.setter
    def reg_txq6_block(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_block_msb, self.__reg_txq6_block_lsb, value)

    @property
    def reg_txq5_block(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_block_msb, self.__reg_txq5_block_lsb)
    @reg_txq5_block.setter
    def reg_txq5_block(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_block_msb, self.__reg_txq5_block_lsb, value)

    @property
    def reg_txq4_block(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_block_msb, self.__reg_txq4_block_lsb)
    @reg_txq4_block.setter
    def reg_txq4_block(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_block_msb, self.__reg_txq4_block_lsb, value)

    @property
    def reg_txq3_block(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_block_msb, self.__reg_txq3_block_lsb)
    @reg_txq3_block.setter
    def reg_txq3_block(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_block_msb, self.__reg_txq3_block_lsb, value)

    @property
    def reg_txq2_block(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_block_msb, self.__reg_txq2_block_lsb)
    @reg_txq2_block.setter
    def reg_txq2_block(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_block_msb, self.__reg_txq2_block_lsb, value)

    @property
    def reg_txq1_block(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_block_msb, self.__reg_txq1_block_lsb)
    @reg_txq1_block.setter
    def reg_txq1_block(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_block_msb, self.__reg_txq1_block_lsb, value)

    @property
    def reg_txq0_block(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_block_msb, self.__reg_txq0_block_lsb)
    @reg_txq0_block.setter
    def reg_txq0_block(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_block_msb, self.__reg_txq0_block_lsb, value)
class MACTXSTATE_CLR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x98
        self.__reg_tximr2_enato_clr_lsb = 26
        self.__reg_tximr2_enato_clr_msb = 26
        self.__reg_tximr1_enato_clr_lsb = 25
        self.__reg_tximr1_enato_clr_msb = 25
        self.__reg_tximr0_enato_clr_lsb = 24
        self.__reg_tximr0_enato_clr_msb = 24
        self.__reg_txq7_enato_clr_lsb = 23
        self.__reg_txq7_enato_clr_msb = 23
        self.__reg_txq6_enato_clr_lsb = 22
        self.__reg_txq6_enato_clr_msb = 22
        self.__reg_txq5_enato_clr_lsb = 21
        self.__reg_txq5_enato_clr_msb = 21
        self.__reg_txq4_enato_clr_lsb = 20
        self.__reg_txq4_enato_clr_msb = 20
        self.__reg_txq3_enato_clr_lsb = 19
        self.__reg_txq3_enato_clr_msb = 19
        self.__reg_txq2_enato_clr_lsb = 18
        self.__reg_txq2_enato_clr_msb = 18
        self.__reg_txq1_enato_clr_lsb = 17
        self.__reg_txq1_enato_clr_msb = 17
        self.__reg_txq0_enato_clr_lsb = 16
        self.__reg_txq0_enato_clr_msb = 16
        self.__reg_tximr2_col_clr_lsb = 10
        self.__reg_tximr2_col_clr_msb = 10
        self.__reg_tximr1_col_clr_lsb = 9
        self.__reg_tximr1_col_clr_msb = 9
        self.__reg_tximr0_col_clr_lsb = 8
        self.__reg_tximr0_col_clr_msb = 8
        self.__reg_txq7_col_clr_lsb = 7
        self.__reg_txq7_col_clr_msb = 7
        self.__reg_txq6_col_clr_lsb = 6
        self.__reg_txq6_col_clr_msb = 6
        self.__reg_txq5_col_clr_lsb = 5
        self.__reg_txq5_col_clr_msb = 5
        self.__reg_txq4_col_clr_lsb = 4
        self.__reg_txq4_col_clr_msb = 4
        self.__reg_txq3_col_clr_lsb = 3
        self.__reg_txq3_col_clr_msb = 3
        self.__reg_txq2_col_clr_lsb = 2
        self.__reg_txq2_col_clr_msb = 2
        self.__reg_txq1_col_clr_lsb = 1
        self.__reg_txq1_col_clr_msb = 1
        self.__reg_txq0_col_clr_lsb = 0
        self.__reg_txq0_col_clr_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr2_enato_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_enato_clr_msb, self.__reg_tximr2_enato_clr_lsb)
    @reg_tximr2_enato_clr.setter
    def reg_tximr2_enato_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_enato_clr_msb, self.__reg_tximr2_enato_clr_lsb, value)

    @property
    def reg_tximr1_enato_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_enato_clr_msb, self.__reg_tximr1_enato_clr_lsb)
    @reg_tximr1_enato_clr.setter
    def reg_tximr1_enato_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_enato_clr_msb, self.__reg_tximr1_enato_clr_lsb, value)

    @property
    def reg_tximr0_enato_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_enato_clr_msb, self.__reg_tximr0_enato_clr_lsb)
    @reg_tximr0_enato_clr.setter
    def reg_tximr0_enato_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_enato_clr_msb, self.__reg_tximr0_enato_clr_lsb, value)

    @property
    def reg_txq7_enato_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_enato_clr_msb, self.__reg_txq7_enato_clr_lsb)
    @reg_txq7_enato_clr.setter
    def reg_txq7_enato_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_enato_clr_msb, self.__reg_txq7_enato_clr_lsb, value)

    @property
    def reg_txq6_enato_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_enato_clr_msb, self.__reg_txq6_enato_clr_lsb)
    @reg_txq6_enato_clr.setter
    def reg_txq6_enato_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_enato_clr_msb, self.__reg_txq6_enato_clr_lsb, value)

    @property
    def reg_txq5_enato_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_enato_clr_msb, self.__reg_txq5_enato_clr_lsb)
    @reg_txq5_enato_clr.setter
    def reg_txq5_enato_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_enato_clr_msb, self.__reg_txq5_enato_clr_lsb, value)

    @property
    def reg_txq4_enato_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_enato_clr_msb, self.__reg_txq4_enato_clr_lsb)
    @reg_txq4_enato_clr.setter
    def reg_txq4_enato_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_enato_clr_msb, self.__reg_txq4_enato_clr_lsb, value)

    @property
    def reg_txq3_enato_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_enato_clr_msb, self.__reg_txq3_enato_clr_lsb)
    @reg_txq3_enato_clr.setter
    def reg_txq3_enato_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_enato_clr_msb, self.__reg_txq3_enato_clr_lsb, value)

    @property
    def reg_txq2_enato_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_enato_clr_msb, self.__reg_txq2_enato_clr_lsb)
    @reg_txq2_enato_clr.setter
    def reg_txq2_enato_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_enato_clr_msb, self.__reg_txq2_enato_clr_lsb, value)

    @property
    def reg_txq1_enato_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_enato_clr_msb, self.__reg_txq1_enato_clr_lsb)
    @reg_txq1_enato_clr.setter
    def reg_txq1_enato_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_enato_clr_msb, self.__reg_txq1_enato_clr_lsb, value)

    @property
    def reg_txq0_enato_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_enato_clr_msb, self.__reg_txq0_enato_clr_lsb)
    @reg_txq0_enato_clr.setter
    def reg_txq0_enato_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_enato_clr_msb, self.__reg_txq0_enato_clr_lsb, value)

    @property
    def reg_tximr2_col_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_col_clr_msb, self.__reg_tximr2_col_clr_lsb)
    @reg_tximr2_col_clr.setter
    def reg_tximr2_col_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_col_clr_msb, self.__reg_tximr2_col_clr_lsb, value)

    @property
    def reg_tximr1_col_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_col_clr_msb, self.__reg_tximr1_col_clr_lsb)
    @reg_tximr1_col_clr.setter
    def reg_tximr1_col_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_col_clr_msb, self.__reg_tximr1_col_clr_lsb, value)

    @property
    def reg_tximr0_col_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_col_clr_msb, self.__reg_tximr0_col_clr_lsb)
    @reg_tximr0_col_clr.setter
    def reg_tximr0_col_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_col_clr_msb, self.__reg_tximr0_col_clr_lsb, value)

    @property
    def reg_txq7_col_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_col_clr_msb, self.__reg_txq7_col_clr_lsb)
    @reg_txq7_col_clr.setter
    def reg_txq7_col_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_col_clr_msb, self.__reg_txq7_col_clr_lsb, value)

    @property
    def reg_txq6_col_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_col_clr_msb, self.__reg_txq6_col_clr_lsb)
    @reg_txq6_col_clr.setter
    def reg_txq6_col_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_col_clr_msb, self.__reg_txq6_col_clr_lsb, value)

    @property
    def reg_txq5_col_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_col_clr_msb, self.__reg_txq5_col_clr_lsb)
    @reg_txq5_col_clr.setter
    def reg_txq5_col_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_col_clr_msb, self.__reg_txq5_col_clr_lsb, value)

    @property
    def reg_txq4_col_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_col_clr_msb, self.__reg_txq4_col_clr_lsb)
    @reg_txq4_col_clr.setter
    def reg_txq4_col_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_col_clr_msb, self.__reg_txq4_col_clr_lsb, value)

    @property
    def reg_txq3_col_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_col_clr_msb, self.__reg_txq3_col_clr_lsb)
    @reg_txq3_col_clr.setter
    def reg_txq3_col_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_col_clr_msb, self.__reg_txq3_col_clr_lsb, value)

    @property
    def reg_txq2_col_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_col_clr_msb, self.__reg_txq2_col_clr_lsb)
    @reg_txq2_col_clr.setter
    def reg_txq2_col_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_col_clr_msb, self.__reg_txq2_col_clr_lsb, value)

    @property
    def reg_txq1_col_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_col_clr_msb, self.__reg_txq1_col_clr_lsb)
    @reg_txq1_col_clr.setter
    def reg_txq1_col_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_col_clr_msb, self.__reg_txq1_col_clr_lsb, value)

    @property
    def reg_txq0_col_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_col_clr_msb, self.__reg_txq0_col_clr_lsb)
    @reg_txq0_col_clr.setter
    def reg_txq0_col_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_col_clr_msb, self.__reg_txq0_col_clr_lsb, value)
class MACTXSTATE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x9c
        self.__reg_tximr2_enato_st_lsb = 26
        self.__reg_tximr2_enato_st_msb = 26
        self.__reg_tximr1_enato_st_lsb = 25
        self.__reg_tximr1_enato_st_msb = 25
        self.__reg_tximr0_enato_st_lsb = 24
        self.__reg_tximr0_enato_st_msb = 24
        self.__reg_txq7_enato_st_lsb = 23
        self.__reg_txq7_enato_st_msb = 23
        self.__reg_txq6_enato_st_lsb = 22
        self.__reg_txq6_enato_st_msb = 22
        self.__reg_txq5_enato_st_lsb = 21
        self.__reg_txq5_enato_st_msb = 21
        self.__reg_txq4_enato_st_lsb = 20
        self.__reg_txq4_enato_st_msb = 20
        self.__reg_txq3_enato_st_lsb = 19
        self.__reg_txq3_enato_st_msb = 19
        self.__reg_txq2_enato_st_lsb = 18
        self.__reg_txq2_enato_st_msb = 18
        self.__reg_txq1_enato_st_lsb = 17
        self.__reg_txq1_enato_st_msb = 17
        self.__reg_txq0_enato_st_lsb = 16
        self.__reg_txq0_enato_st_msb = 16
        self.__reg_tximr2_col_lsb = 10
        self.__reg_tximr2_col_msb = 10
        self.__reg_tximr1_col_lsb = 9
        self.__reg_tximr1_col_msb = 9
        self.__reg_tximr0_col_lsb = 8
        self.__reg_tximr0_col_msb = 8
        self.__reg_txq7_col_lsb = 7
        self.__reg_txq7_col_msb = 7
        self.__reg_txq6_col_lsb = 6
        self.__reg_txq6_col_msb = 6
        self.__reg_txq5_col_lsb = 5
        self.__reg_txq5_col_msb = 5
        self.__reg_txq4_col_lsb = 4
        self.__reg_txq4_col_msb = 4
        self.__reg_txq3_col_lsb = 3
        self.__reg_txq3_col_msb = 3
        self.__reg_txq2_col_lsb = 2
        self.__reg_txq2_col_msb = 2
        self.__reg_txq1_col_lsb = 1
        self.__reg_txq1_col_msb = 1
        self.__reg_txq0_col_lsb = 0
        self.__reg_txq0_col_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr2_enato_st(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_enato_st_msb, self.__reg_tximr2_enato_st_lsb)
    @reg_tximr2_enato_st.setter
    def reg_tximr2_enato_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_enato_st_msb, self.__reg_tximr2_enato_st_lsb, value)

    @property
    def reg_tximr1_enato_st(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_enato_st_msb, self.__reg_tximr1_enato_st_lsb)
    @reg_tximr1_enato_st.setter
    def reg_tximr1_enato_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_enato_st_msb, self.__reg_tximr1_enato_st_lsb, value)

    @property
    def reg_tximr0_enato_st(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_enato_st_msb, self.__reg_tximr0_enato_st_lsb)
    @reg_tximr0_enato_st.setter
    def reg_tximr0_enato_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_enato_st_msb, self.__reg_tximr0_enato_st_lsb, value)

    @property
    def reg_txq7_enato_st(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_enato_st_msb, self.__reg_txq7_enato_st_lsb)
    @reg_txq7_enato_st.setter
    def reg_txq7_enato_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_enato_st_msb, self.__reg_txq7_enato_st_lsb, value)

    @property
    def reg_txq6_enato_st(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_enato_st_msb, self.__reg_txq6_enato_st_lsb)
    @reg_txq6_enato_st.setter
    def reg_txq6_enato_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_enato_st_msb, self.__reg_txq6_enato_st_lsb, value)

    @property
    def reg_txq5_enato_st(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_enato_st_msb, self.__reg_txq5_enato_st_lsb)
    @reg_txq5_enato_st.setter
    def reg_txq5_enato_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_enato_st_msb, self.__reg_txq5_enato_st_lsb, value)

    @property
    def reg_txq4_enato_st(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_enato_st_msb, self.__reg_txq4_enato_st_lsb)
    @reg_txq4_enato_st.setter
    def reg_txq4_enato_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_enato_st_msb, self.__reg_txq4_enato_st_lsb, value)

    @property
    def reg_txq3_enato_st(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_enato_st_msb, self.__reg_txq3_enato_st_lsb)
    @reg_txq3_enato_st.setter
    def reg_txq3_enato_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_enato_st_msb, self.__reg_txq3_enato_st_lsb, value)

    @property
    def reg_txq2_enato_st(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_enato_st_msb, self.__reg_txq2_enato_st_lsb)
    @reg_txq2_enato_st.setter
    def reg_txq2_enato_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_enato_st_msb, self.__reg_txq2_enato_st_lsb, value)

    @property
    def reg_txq1_enato_st(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_enato_st_msb, self.__reg_txq1_enato_st_lsb)
    @reg_txq1_enato_st.setter
    def reg_txq1_enato_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_enato_st_msb, self.__reg_txq1_enato_st_lsb, value)

    @property
    def reg_txq0_enato_st(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_enato_st_msb, self.__reg_txq0_enato_st_lsb)
    @reg_txq0_enato_st.setter
    def reg_txq0_enato_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_enato_st_msb, self.__reg_txq0_enato_st_lsb, value)

    @property
    def reg_tximr2_col(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_col_msb, self.__reg_tximr2_col_lsb)
    @reg_tximr2_col.setter
    def reg_tximr2_col(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_col_msb, self.__reg_tximr2_col_lsb, value)

    @property
    def reg_tximr1_col(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_col_msb, self.__reg_tximr1_col_lsb)
    @reg_tximr1_col.setter
    def reg_tximr1_col(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_col_msb, self.__reg_tximr1_col_lsb, value)

    @property
    def reg_tximr0_col(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_col_msb, self.__reg_tximr0_col_lsb)
    @reg_tximr0_col.setter
    def reg_tximr0_col(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_col_msb, self.__reg_tximr0_col_lsb, value)

    @property
    def reg_txq7_col(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_col_msb, self.__reg_txq7_col_lsb)
    @reg_txq7_col.setter
    def reg_txq7_col(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_col_msb, self.__reg_txq7_col_lsb, value)

    @property
    def reg_txq6_col(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_col_msb, self.__reg_txq6_col_lsb)
    @reg_txq6_col.setter
    def reg_txq6_col(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_col_msb, self.__reg_txq6_col_lsb, value)

    @property
    def reg_txq5_col(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_col_msb, self.__reg_txq5_col_lsb)
    @reg_txq5_col.setter
    def reg_txq5_col(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_col_msb, self.__reg_txq5_col_lsb, value)

    @property
    def reg_txq4_col(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_col_msb, self.__reg_txq4_col_lsb)
    @reg_txq4_col.setter
    def reg_txq4_col(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_col_msb, self.__reg_txq4_col_lsb, value)

    @property
    def reg_txq3_col(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_col_msb, self.__reg_txq3_col_lsb)
    @reg_txq3_col.setter
    def reg_txq3_col(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_col_msb, self.__reg_txq3_col_lsb, value)

    @property
    def reg_txq2_col(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_col_msb, self.__reg_txq2_col_lsb)
    @reg_txq2_col.setter
    def reg_txq2_col(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_col_msb, self.__reg_txq2_col_lsb, value)

    @property
    def reg_txq1_col(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_col_msb, self.__reg_txq1_col_lsb)
    @reg_txq1_col.setter
    def reg_txq1_col(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_col_msb, self.__reg_txq1_col_lsb, value)

    @property
    def reg_txq0_col(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_col_msb, self.__reg_txq0_col_lsb)
    @reg_txq0_col.setter
    def reg_txq0_col(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_col_msb, self.__reg_txq0_col_lsb, value)
class MACTXENA_ST_CLR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0xa0
        self.__tximr2_ena_st_clr_lsb = 10
        self.__tximr2_ena_st_clr_msb = 10
        self.__tximr1_ena_st_clr_lsb = 9
        self.__tximr1_ena_st_clr_msb = 9
        self.__tximr0_ena_st_clr_lsb = 8
        self.__tximr0_ena_st_clr_msb = 8
        self.__txq7_ena_st_clr_lsb = 7
        self.__txq7_ena_st_clr_msb = 7
        self.__txq6_ena_st_clr_lsb = 6
        self.__txq6_ena_st_clr_msb = 6
        self.__txq5_ena_st_clr_lsb = 5
        self.__txq5_ena_st_clr_msb = 5
        self.__txq4_ena_st_clr_lsb = 4
        self.__txq4_ena_st_clr_msb = 4
        self.__txq3_ena_st_clr_lsb = 3
        self.__txq3_ena_st_clr_msb = 3
        self.__txq2_ena_st_clr_lsb = 2
        self.__txq2_ena_st_clr_msb = 2
        self.__txq1_ena_st_clr_lsb = 1
        self.__txq1_ena_st_clr_msb = 1
        self.__txq0_ena_st_clr_lsb = 0
        self.__txq0_ena_st_clr_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr2_ena_st_clr(self):
        return self.__MEM.rdm(self.__addr, self.__tximr2_ena_st_clr_msb, self.__tximr2_ena_st_clr_lsb)
    @tximr2_ena_st_clr.setter
    def tximr2_ena_st_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr2_ena_st_clr_msb, self.__tximr2_ena_st_clr_lsb, value)

    @property
    def tximr1_ena_st_clr(self):
        return self.__MEM.rdm(self.__addr, self.__tximr1_ena_st_clr_msb, self.__tximr1_ena_st_clr_lsb)
    @tximr1_ena_st_clr.setter
    def tximr1_ena_st_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr1_ena_st_clr_msb, self.__tximr1_ena_st_clr_lsb, value)

    @property
    def tximr0_ena_st_clr(self):
        return self.__MEM.rdm(self.__addr, self.__tximr0_ena_st_clr_msb, self.__tximr0_ena_st_clr_lsb)
    @tximr0_ena_st_clr.setter
    def tximr0_ena_st_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr0_ena_st_clr_msb, self.__tximr0_ena_st_clr_lsb, value)

    @property
    def txq7_ena_st_clr(self):
        return self.__MEM.rdm(self.__addr, self.__txq7_ena_st_clr_msb, self.__txq7_ena_st_clr_lsb)
    @txq7_ena_st_clr.setter
    def txq7_ena_st_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq7_ena_st_clr_msb, self.__txq7_ena_st_clr_lsb, value)

    @property
    def txq6_ena_st_clr(self):
        return self.__MEM.rdm(self.__addr, self.__txq6_ena_st_clr_msb, self.__txq6_ena_st_clr_lsb)
    @txq6_ena_st_clr.setter
    def txq6_ena_st_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq6_ena_st_clr_msb, self.__txq6_ena_st_clr_lsb, value)

    @property
    def txq5_ena_st_clr(self):
        return self.__MEM.rdm(self.__addr, self.__txq5_ena_st_clr_msb, self.__txq5_ena_st_clr_lsb)
    @txq5_ena_st_clr.setter
    def txq5_ena_st_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq5_ena_st_clr_msb, self.__txq5_ena_st_clr_lsb, value)

    @property
    def txq4_ena_st_clr(self):
        return self.__MEM.rdm(self.__addr, self.__txq4_ena_st_clr_msb, self.__txq4_ena_st_clr_lsb)
    @txq4_ena_st_clr.setter
    def txq4_ena_st_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq4_ena_st_clr_msb, self.__txq4_ena_st_clr_lsb, value)

    @property
    def txq3_ena_st_clr(self):
        return self.__MEM.rdm(self.__addr, self.__txq3_ena_st_clr_msb, self.__txq3_ena_st_clr_lsb)
    @txq3_ena_st_clr.setter
    def txq3_ena_st_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq3_ena_st_clr_msb, self.__txq3_ena_st_clr_lsb, value)

    @property
    def txq2_ena_st_clr(self):
        return self.__MEM.rdm(self.__addr, self.__txq2_ena_st_clr_msb, self.__txq2_ena_st_clr_lsb)
    @txq2_ena_st_clr.setter
    def txq2_ena_st_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq2_ena_st_clr_msb, self.__txq2_ena_st_clr_lsb, value)

    @property
    def txq1_ena_st_clr(self):
        return self.__MEM.rdm(self.__addr, self.__txq1_ena_st_clr_msb, self.__txq1_ena_st_clr_lsb)
    @txq1_ena_st_clr.setter
    def txq1_ena_st_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq1_ena_st_clr_msb, self.__txq1_ena_st_clr_lsb, value)

    @property
    def txq0_ena_st_clr(self):
        return self.__MEM.rdm(self.__addr, self.__txq0_ena_st_clr_msb, self.__txq0_ena_st_clr_lsb)
    @txq0_ena_st_clr.setter
    def txq0_ena_st_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq0_ena_st_clr_msb, self.__txq0_ena_st_clr_lsb, value)
class MACTXENA_ST(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0xa4
        self.__tximr2_ena_st_lsb = 10
        self.__tximr2_ena_st_msb = 10
        self.__tximr1_ena_st_lsb = 9
        self.__tximr1_ena_st_msb = 9
        self.__tximr0_ena_st_lsb = 8
        self.__tximr0_ena_st_msb = 8
        self.__txq7_ena_st_lsb = 7
        self.__txq7_ena_st_msb = 7
        self.__txq6_ena_st_lsb = 6
        self.__txq6_ena_st_msb = 6
        self.__txq5_ena_st_lsb = 5
        self.__txq5_ena_st_msb = 5
        self.__txq4_ena_st_lsb = 4
        self.__txq4_ena_st_msb = 4
        self.__txq3_ena_st_lsb = 3
        self.__txq3_ena_st_msb = 3
        self.__txq2_ena_st_lsb = 2
        self.__txq2_ena_st_msb = 2
        self.__txq1_ena_st_lsb = 1
        self.__txq1_ena_st_msb = 1
        self.__txq0_ena_st_lsb = 0
        self.__txq0_ena_st_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr2_ena_st(self):
        return self.__MEM.rdm(self.__addr, self.__tximr2_ena_st_msb, self.__tximr2_ena_st_lsb)
    @tximr2_ena_st.setter
    def tximr2_ena_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr2_ena_st_msb, self.__tximr2_ena_st_lsb, value)

    @property
    def tximr1_ena_st(self):
        return self.__MEM.rdm(self.__addr, self.__tximr1_ena_st_msb, self.__tximr1_ena_st_lsb)
    @tximr1_ena_st.setter
    def tximr1_ena_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr1_ena_st_msb, self.__tximr1_ena_st_lsb, value)

    @property
    def tximr0_ena_st(self):
        return self.__MEM.rdm(self.__addr, self.__tximr0_ena_st_msb, self.__tximr0_ena_st_lsb)
    @tximr0_ena_st.setter
    def tximr0_ena_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr0_ena_st_msb, self.__tximr0_ena_st_lsb, value)

    @property
    def txq7_ena_st(self):
        return self.__MEM.rdm(self.__addr, self.__txq7_ena_st_msb, self.__txq7_ena_st_lsb)
    @txq7_ena_st.setter
    def txq7_ena_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq7_ena_st_msb, self.__txq7_ena_st_lsb, value)

    @property
    def txq6_ena_st(self):
        return self.__MEM.rdm(self.__addr, self.__txq6_ena_st_msb, self.__txq6_ena_st_lsb)
    @txq6_ena_st.setter
    def txq6_ena_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq6_ena_st_msb, self.__txq6_ena_st_lsb, value)

    @property
    def txq5_ena_st(self):
        return self.__MEM.rdm(self.__addr, self.__txq5_ena_st_msb, self.__txq5_ena_st_lsb)
    @txq5_ena_st.setter
    def txq5_ena_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq5_ena_st_msb, self.__txq5_ena_st_lsb, value)

    @property
    def txq4_ena_st(self):
        return self.__MEM.rdm(self.__addr, self.__txq4_ena_st_msb, self.__txq4_ena_st_lsb)
    @txq4_ena_st.setter
    def txq4_ena_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq4_ena_st_msb, self.__txq4_ena_st_lsb, value)

    @property
    def txq3_ena_st(self):
        return self.__MEM.rdm(self.__addr, self.__txq3_ena_st_msb, self.__txq3_ena_st_lsb)
    @txq3_ena_st.setter
    def txq3_ena_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq3_ena_st_msb, self.__txq3_ena_st_lsb, value)

    @property
    def txq2_ena_st(self):
        return self.__MEM.rdm(self.__addr, self.__txq2_ena_st_msb, self.__txq2_ena_st_lsb)
    @txq2_ena_st.setter
    def txq2_ena_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq2_ena_st_msb, self.__txq2_ena_st_lsb, value)

    @property
    def txq1_ena_st(self):
        return self.__MEM.rdm(self.__addr, self.__txq1_ena_st_msb, self.__txq1_ena_st_lsb)
    @txq1_ena_st.setter
    def txq1_ena_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq1_ena_st_msb, self.__txq1_ena_st_lsb, value)

    @property
    def txq0_ena_st(self):
        return self.__MEM.rdm(self.__addr, self.__txq0_ena_st_msb, self.__txq0_ena_st_lsb)
    @txq0_ena_st.setter
    def txq0_ena_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq0_ena_st_msb, self.__txq0_ena_st_lsb, value)
class MACTXIMR2_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0xa8
        self.__reg_tximr2_pti_lsb = 28
        self.__reg_tximr2_pti_msb = 31
        self.__reg_tximr2_enato_timer_lsb = 0
        self.__reg_tximr2_enato_timer_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr2_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_pti_msb, self.__reg_tximr2_pti_lsb)
    @reg_tximr2_pti.setter
    def reg_tximr2_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_pti_msb, self.__reg_tximr2_pti_lsb, value)

    @property
    def reg_tximr2_enato_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_enato_timer_msb, self.__reg_tximr2_enato_timer_lsb)
    @reg_tximr2_enato_timer.setter
    def reg_tximr2_enato_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_enato_timer_msb, self.__reg_tximr2_enato_timer_lsb, value)
class MACTXIMR2_PLCP0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0xac
        self.__reg_tximr2_ena_lsb = 31
        self.__reg_tximr2_ena_msb = 31
        self.__reg_tximr2_valid_lsb = 30
        self.__reg_tximr2_valid_msb = 30
        self.__reg_tximr2_txop_lsb = 29
        self.__reg_tximr2_txop_msb = 29
        self.__reg_tximr2_cts_lsb = 28
        self.__reg_tximr2_cts_msb = 28
        self.__reg_tximr2_rts_lsb = 27
        self.__reg_tximr2_rts_msb = 27
        self.__reg_tximr2_ack_lsb = 24
        self.__reg_tximr2_ack_msb = 26
        self.__reg_tximr2_cf_lsb = 23
        self.__reg_tximr2_cf_msb = 23
        self.__reg_tximr2_autodur_lsb = 22
        self.__reg_tximr2_autodur_msb = 22
        self.__reg_tximr2_txenato_lsb = 21
        self.__reg_tximr2_txenato_msb = 21
        self.__reg_tximr2_hwseq_lsb = 20
        self.__reg_tximr2_hwseq_msb = 20
        self.__reg_tximr2_link_addr_lsb = 0
        self.__reg_tximr2_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr2_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_ena_msb, self.__reg_tximr2_ena_lsb)
    @reg_tximr2_ena.setter
    def reg_tximr2_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_ena_msb, self.__reg_tximr2_ena_lsb, value)

    @property
    def reg_tximr2_valid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_valid_msb, self.__reg_tximr2_valid_lsb)
    @reg_tximr2_valid.setter
    def reg_tximr2_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_valid_msb, self.__reg_tximr2_valid_lsb, value)

    @property
    def reg_tximr2_txop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_txop_msb, self.__reg_tximr2_txop_lsb)
    @reg_tximr2_txop.setter
    def reg_tximr2_txop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_txop_msb, self.__reg_tximr2_txop_lsb, value)

    @property
    def reg_tximr2_cts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_cts_msb, self.__reg_tximr2_cts_lsb)
    @reg_tximr2_cts.setter
    def reg_tximr2_cts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_cts_msb, self.__reg_tximr2_cts_lsb, value)

    @property
    def reg_tximr2_rts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_rts_msb, self.__reg_tximr2_rts_lsb)
    @reg_tximr2_rts.setter
    def reg_tximr2_rts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_rts_msb, self.__reg_tximr2_rts_lsb, value)

    @property
    def reg_tximr2_ack(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_ack_msb, self.__reg_tximr2_ack_lsb)
    @reg_tximr2_ack.setter
    def reg_tximr2_ack(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_ack_msb, self.__reg_tximr2_ack_lsb, value)

    @property
    def reg_tximr2_cf(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_cf_msb, self.__reg_tximr2_cf_lsb)
    @reg_tximr2_cf.setter
    def reg_tximr2_cf(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_cf_msb, self.__reg_tximr2_cf_lsb, value)

    @property
    def reg_tximr2_autodur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_autodur_msb, self.__reg_tximr2_autodur_lsb)
    @reg_tximr2_autodur.setter
    def reg_tximr2_autodur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_autodur_msb, self.__reg_tximr2_autodur_lsb, value)

    @property
    def reg_tximr2_txenato(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_txenato_msb, self.__reg_tximr2_txenato_lsb)
    @reg_tximr2_txenato.setter
    def reg_tximr2_txenato(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_txenato_msb, self.__reg_tximr2_txenato_lsb, value)

    @property
    def reg_tximr2_hwseq(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_hwseq_msb, self.__reg_tximr2_hwseq_lsb)
    @reg_tximr2_hwseq.setter
    def reg_tximr2_hwseq(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_hwseq_msb, self.__reg_tximr2_hwseq_lsb, value)

    @property
    def reg_tximr2_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_link_addr_msb, self.__reg_tximr2_link_addr_lsb)
    @reg_tximr2_link_addr.setter
    def reg_tximr2_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_link_addr_msb, self.__reg_tximr2_link_addr_lsb, value)
class MACTXIMR1_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0xb0
        self.__reg_tximr1_pti_lsb = 28
        self.__reg_tximr1_pti_msb = 31
        self.__reg_tximr1_enato_timer_lsb = 0
        self.__reg_tximr1_enato_timer_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr1_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_pti_msb, self.__reg_tximr1_pti_lsb)
    @reg_tximr1_pti.setter
    def reg_tximr1_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_pti_msb, self.__reg_tximr1_pti_lsb, value)

    @property
    def reg_tximr1_enato_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_enato_timer_msb, self.__reg_tximr1_enato_timer_lsb)
    @reg_tximr1_enato_timer.setter
    def reg_tximr1_enato_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_enato_timer_msb, self.__reg_tximr1_enato_timer_lsb, value)
class MACTXIMR1_PLCP0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0xb4
        self.__reg_tximr1_ena_lsb = 31
        self.__reg_tximr1_ena_msb = 31
        self.__reg_tximr1_valid_lsb = 30
        self.__reg_tximr1_valid_msb = 30
        self.__reg_tximr1_txop_lsb = 29
        self.__reg_tximr1_txop_msb = 29
        self.__reg_tximr1_cts_lsb = 28
        self.__reg_tximr1_cts_msb = 28
        self.__reg_tximr1_rts_lsb = 27
        self.__reg_tximr1_rts_msb = 27
        self.__reg_tximr1_ack_lsb = 24
        self.__reg_tximr1_ack_msb = 26
        self.__reg_tximr1_cf_lsb = 23
        self.__reg_tximr1_cf_msb = 23
        self.__reg_tximr1_autodur_lsb = 22
        self.__reg_tximr1_autodur_msb = 22
        self.__reg_tximr1_txenato_lsb = 21
        self.__reg_tximr1_txenato_msb = 21
        self.__reg_tximr1_hwseq_lsb = 20
        self.__reg_tximr1_hwseq_msb = 20
        self.__reg_tximr1_link_addr_lsb = 0
        self.__reg_tximr1_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr1_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_ena_msb, self.__reg_tximr1_ena_lsb)
    @reg_tximr1_ena.setter
    def reg_tximr1_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_ena_msb, self.__reg_tximr1_ena_lsb, value)

    @property
    def reg_tximr1_valid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_valid_msb, self.__reg_tximr1_valid_lsb)
    @reg_tximr1_valid.setter
    def reg_tximr1_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_valid_msb, self.__reg_tximr1_valid_lsb, value)

    @property
    def reg_tximr1_txop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_txop_msb, self.__reg_tximr1_txop_lsb)
    @reg_tximr1_txop.setter
    def reg_tximr1_txop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_txop_msb, self.__reg_tximr1_txop_lsb, value)

    @property
    def reg_tximr1_cts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_cts_msb, self.__reg_tximr1_cts_lsb)
    @reg_tximr1_cts.setter
    def reg_tximr1_cts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_cts_msb, self.__reg_tximr1_cts_lsb, value)

    @property
    def reg_tximr1_rts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_rts_msb, self.__reg_tximr1_rts_lsb)
    @reg_tximr1_rts.setter
    def reg_tximr1_rts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_rts_msb, self.__reg_tximr1_rts_lsb, value)

    @property
    def reg_tximr1_ack(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_ack_msb, self.__reg_tximr1_ack_lsb)
    @reg_tximr1_ack.setter
    def reg_tximr1_ack(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_ack_msb, self.__reg_tximr1_ack_lsb, value)

    @property
    def reg_tximr1_cf(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_cf_msb, self.__reg_tximr1_cf_lsb)
    @reg_tximr1_cf.setter
    def reg_tximr1_cf(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_cf_msb, self.__reg_tximr1_cf_lsb, value)

    @property
    def reg_tximr1_autodur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_autodur_msb, self.__reg_tximr1_autodur_lsb)
    @reg_tximr1_autodur.setter
    def reg_tximr1_autodur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_autodur_msb, self.__reg_tximr1_autodur_lsb, value)

    @property
    def reg_tximr1_txenato(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_txenato_msb, self.__reg_tximr1_txenato_lsb)
    @reg_tximr1_txenato.setter
    def reg_tximr1_txenato(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_txenato_msb, self.__reg_tximr1_txenato_lsb, value)

    @property
    def reg_tximr1_hwseq(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_hwseq_msb, self.__reg_tximr1_hwseq_lsb)
    @reg_tximr1_hwseq.setter
    def reg_tximr1_hwseq(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_hwseq_msb, self.__reg_tximr1_hwseq_lsb, value)

    @property
    def reg_tximr1_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_link_addr_msb, self.__reg_tximr1_link_addr_lsb)
    @reg_tximr1_link_addr.setter
    def reg_tximr1_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_link_addr_msb, self.__reg_tximr1_link_addr_lsb, value)
class MACTXIMR0_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0xb8
        self.__reg_tximr0_pti_lsb = 28
        self.__reg_tximr0_pti_msb = 31
        self.__reg_tximr0_enato_timer_lsb = 0
        self.__reg_tximr0_enato_timer_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr0_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_pti_msb, self.__reg_tximr0_pti_lsb)
    @reg_tximr0_pti.setter
    def reg_tximr0_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_pti_msb, self.__reg_tximr0_pti_lsb, value)

    @property
    def reg_tximr0_enato_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_enato_timer_msb, self.__reg_tximr0_enato_timer_lsb)
    @reg_tximr0_enato_timer.setter
    def reg_tximr0_enato_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_enato_timer_msb, self.__reg_tximr0_enato_timer_lsb, value)
class MACTXIMR0_PLCP0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0xbc
        self.__reg_tximr0_ena_lsb = 31
        self.__reg_tximr0_ena_msb = 31
        self.__reg_tximr0_valid_lsb = 30
        self.__reg_tximr0_valid_msb = 30
        self.__reg_tximr0_txop_lsb = 29
        self.__reg_tximr0_txop_msb = 29
        self.__reg_tximr0_cts_lsb = 28
        self.__reg_tximr0_cts_msb = 28
        self.__reg_tximr0_rts_lsb = 27
        self.__reg_tximr0_rts_msb = 27
        self.__reg_tximr0_ack_lsb = 24
        self.__reg_tximr0_ack_msb = 26
        self.__reg_tximr0_cf_lsb = 23
        self.__reg_tximr0_cf_msb = 23
        self.__reg_tximr0_autodur_lsb = 22
        self.__reg_tximr0_autodur_msb = 22
        self.__reg_tximr0_txenato_lsb = 21
        self.__reg_tximr0_txenato_msb = 21
        self.__reg_tximr0_hwseq_lsb = 20
        self.__reg_tximr0_hwseq_msb = 20
        self.__reg_tximr0_link_addr_lsb = 0
        self.__reg_tximr0_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr0_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_ena_msb, self.__reg_tximr0_ena_lsb)
    @reg_tximr0_ena.setter
    def reg_tximr0_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_ena_msb, self.__reg_tximr0_ena_lsb, value)

    @property
    def reg_tximr0_valid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_valid_msb, self.__reg_tximr0_valid_lsb)
    @reg_tximr0_valid.setter
    def reg_tximr0_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_valid_msb, self.__reg_tximr0_valid_lsb, value)

    @property
    def reg_tximr0_txop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_txop_msb, self.__reg_tximr0_txop_lsb)
    @reg_tximr0_txop.setter
    def reg_tximr0_txop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_txop_msb, self.__reg_tximr0_txop_lsb, value)

    @property
    def reg_tximr0_cts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_cts_msb, self.__reg_tximr0_cts_lsb)
    @reg_tximr0_cts.setter
    def reg_tximr0_cts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_cts_msb, self.__reg_tximr0_cts_lsb, value)

    @property
    def reg_tximr0_rts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_rts_msb, self.__reg_tximr0_rts_lsb)
    @reg_tximr0_rts.setter
    def reg_tximr0_rts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_rts_msb, self.__reg_tximr0_rts_lsb, value)

    @property
    def reg_tximr0_ack(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_ack_msb, self.__reg_tximr0_ack_lsb)
    @reg_tximr0_ack.setter
    def reg_tximr0_ack(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_ack_msb, self.__reg_tximr0_ack_lsb, value)

    @property
    def reg_tximr0_cf(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_cf_msb, self.__reg_tximr0_cf_lsb)
    @reg_tximr0_cf.setter
    def reg_tximr0_cf(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_cf_msb, self.__reg_tximr0_cf_lsb, value)

    @property
    def reg_tximr0_autodur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_autodur_msb, self.__reg_tximr0_autodur_lsb)
    @reg_tximr0_autodur.setter
    def reg_tximr0_autodur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_autodur_msb, self.__reg_tximr0_autodur_lsb, value)

    @property
    def reg_tximr0_txenato(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_txenato_msb, self.__reg_tximr0_txenato_lsb)
    @reg_tximr0_txenato.setter
    def reg_tximr0_txenato(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_txenato_msb, self.__reg_tximr0_txenato_lsb, value)

    @property
    def reg_tximr0_hwseq(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_hwseq_msb, self.__reg_tximr0_hwseq_lsb)
    @reg_tximr0_hwseq.setter
    def reg_tximr0_hwseq(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_hwseq_msb, self.__reg_tximr0_hwseq_lsb, value)

    @property
    def reg_tximr0_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_link_addr_msb, self.__reg_tximr0_link_addr_lsb)
    @reg_tximr0_link_addr.setter
    def reg_tximr0_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_link_addr_msb, self.__reg_tximr0_link_addr_lsb, value)
class MACTXQ7_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0xc0
        self.__reg_txq7_pti_lsb = 28
        self.__reg_txq7_pti_msb = 31
        self.__reg_txq7_aifs_lsb = 24
        self.__reg_txq7_aifs_msb = 27
        self.__txq7_inbackoff_lsb = 23
        self.__txq7_inbackoff_msb = 23
        self.__txq7_inaifs_lsb = 22
        self.__txq7_inaifs_msb = 22
        self.__reg_txq7_backoff_lsb = 12
        self.__reg_txq7_backoff_msb = 21
        self.__reg_txq7_enato_timer_lsb = 0
        self.__reg_txq7_enato_timer_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq7_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_pti_msb, self.__reg_txq7_pti_lsb)
    @reg_txq7_pti.setter
    def reg_txq7_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_pti_msb, self.__reg_txq7_pti_lsb, value)

    @property
    def reg_txq7_aifs(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_aifs_msb, self.__reg_txq7_aifs_lsb)
    @reg_txq7_aifs.setter
    def reg_txq7_aifs(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_aifs_msb, self.__reg_txq7_aifs_lsb, value)

    @property
    def txq7_inbackoff(self):
        return self.__MEM.rdm(self.__addr, self.__txq7_inbackoff_msb, self.__txq7_inbackoff_lsb)
    @txq7_inbackoff.setter
    def txq7_inbackoff(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq7_inbackoff_msb, self.__txq7_inbackoff_lsb, value)

    @property
    def txq7_inaifs(self):
        return self.__MEM.rdm(self.__addr, self.__txq7_inaifs_msb, self.__txq7_inaifs_lsb)
    @txq7_inaifs.setter
    def txq7_inaifs(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq7_inaifs_msb, self.__txq7_inaifs_lsb, value)

    @property
    def reg_txq7_backoff(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_backoff_msb, self.__reg_txq7_backoff_lsb)
    @reg_txq7_backoff.setter
    def reg_txq7_backoff(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_backoff_msb, self.__reg_txq7_backoff_lsb, value)

    @property
    def reg_txq7_enato_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_enato_timer_msb, self.__reg_txq7_enato_timer_lsb)
    @reg_txq7_enato_timer.setter
    def reg_txq7_enato_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_enato_timer_msb, self.__reg_txq7_enato_timer_lsb, value)
class MACTXQ7_PLCP0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0xc4
        self.__reg_txq7_ena_lsb = 31
        self.__reg_txq7_ena_msb = 31
        self.__reg_txq7_valid_lsb = 30
        self.__reg_txq7_valid_msb = 30
        self.__reg_txq7_txop_lsb = 29
        self.__reg_txq7_txop_msb = 29
        self.__reg_txq7_cts_lsb = 28
        self.__reg_txq7_cts_msb = 28
        self.__reg_txq7_rts_lsb = 27
        self.__reg_txq7_rts_msb = 27
        self.__reg_txq7_ack_lsb = 24
        self.__reg_txq7_ack_msb = 26
        self.__reg_txq7_cf_lsb = 23
        self.__reg_txq7_cf_msb = 23
        self.__reg_txq7_autodur_lsb = 22
        self.__reg_txq7_autodur_msb = 22
        self.__reg_txq7_txenato_lsb = 21
        self.__reg_txq7_txenato_msb = 21
        self.__reg_txq7_hwseq_lsb = 20
        self.__reg_txq7_hwseq_msb = 20
        self.__reg_txq7_link_addr_lsb = 0
        self.__reg_txq7_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq7_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_ena_msb, self.__reg_txq7_ena_lsb)
    @reg_txq7_ena.setter
    def reg_txq7_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_ena_msb, self.__reg_txq7_ena_lsb, value)

    @property
    def reg_txq7_valid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_valid_msb, self.__reg_txq7_valid_lsb)
    @reg_txq7_valid.setter
    def reg_txq7_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_valid_msb, self.__reg_txq7_valid_lsb, value)

    @property
    def reg_txq7_txop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_txop_msb, self.__reg_txq7_txop_lsb)
    @reg_txq7_txop.setter
    def reg_txq7_txop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_txop_msb, self.__reg_txq7_txop_lsb, value)

    @property
    def reg_txq7_cts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_cts_msb, self.__reg_txq7_cts_lsb)
    @reg_txq7_cts.setter
    def reg_txq7_cts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_cts_msb, self.__reg_txq7_cts_lsb, value)

    @property
    def reg_txq7_rts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_rts_msb, self.__reg_txq7_rts_lsb)
    @reg_txq7_rts.setter
    def reg_txq7_rts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_rts_msb, self.__reg_txq7_rts_lsb, value)

    @property
    def reg_txq7_ack(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_ack_msb, self.__reg_txq7_ack_lsb)
    @reg_txq7_ack.setter
    def reg_txq7_ack(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_ack_msb, self.__reg_txq7_ack_lsb, value)

    @property
    def reg_txq7_cf(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_cf_msb, self.__reg_txq7_cf_lsb)
    @reg_txq7_cf.setter
    def reg_txq7_cf(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_cf_msb, self.__reg_txq7_cf_lsb, value)

    @property
    def reg_txq7_autodur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_autodur_msb, self.__reg_txq7_autodur_lsb)
    @reg_txq7_autodur.setter
    def reg_txq7_autodur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_autodur_msb, self.__reg_txq7_autodur_lsb, value)

    @property
    def reg_txq7_txenato(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_txenato_msb, self.__reg_txq7_txenato_lsb)
    @reg_txq7_txenato.setter
    def reg_txq7_txenato(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_txenato_msb, self.__reg_txq7_txenato_lsb, value)

    @property
    def reg_txq7_hwseq(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_hwseq_msb, self.__reg_txq7_hwseq_lsb)
    @reg_txq7_hwseq.setter
    def reg_txq7_hwseq(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_hwseq_msb, self.__reg_txq7_hwseq_lsb, value)

    @property
    def reg_txq7_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_link_addr_msb, self.__reg_txq7_link_addr_lsb)
    @reg_txq7_link_addr.setter
    def reg_txq7_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_link_addr_msb, self.__reg_txq7_link_addr_lsb, value)
class MACTXQ6_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0xc8
        self.__reg_txq6_pti_lsb = 28
        self.__reg_txq6_pti_msb = 31
        self.__reg_txq6_aifs_lsb = 24
        self.__reg_txq6_aifs_msb = 27
        self.__txq6_inbackoff_lsb = 23
        self.__txq6_inbackoff_msb = 23
        self.__txq6_inaifs_lsb = 22
        self.__txq6_inaifs_msb = 22
        self.__reg_txq6_backoff_lsb = 12
        self.__reg_txq6_backoff_msb = 21
        self.__reg_txq6_enato_timer_lsb = 0
        self.__reg_txq6_enato_timer_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq6_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_pti_msb, self.__reg_txq6_pti_lsb)
    @reg_txq6_pti.setter
    def reg_txq6_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_pti_msb, self.__reg_txq6_pti_lsb, value)

    @property
    def reg_txq6_aifs(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_aifs_msb, self.__reg_txq6_aifs_lsb)
    @reg_txq6_aifs.setter
    def reg_txq6_aifs(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_aifs_msb, self.__reg_txq6_aifs_lsb, value)

    @property
    def txq6_inbackoff(self):
        return self.__MEM.rdm(self.__addr, self.__txq6_inbackoff_msb, self.__txq6_inbackoff_lsb)
    @txq6_inbackoff.setter
    def txq6_inbackoff(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq6_inbackoff_msb, self.__txq6_inbackoff_lsb, value)

    @property
    def txq6_inaifs(self):
        return self.__MEM.rdm(self.__addr, self.__txq6_inaifs_msb, self.__txq6_inaifs_lsb)
    @txq6_inaifs.setter
    def txq6_inaifs(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq6_inaifs_msb, self.__txq6_inaifs_lsb, value)

    @property
    def reg_txq6_backoff(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_backoff_msb, self.__reg_txq6_backoff_lsb)
    @reg_txq6_backoff.setter
    def reg_txq6_backoff(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_backoff_msb, self.__reg_txq6_backoff_lsb, value)

    @property
    def reg_txq6_enato_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_enato_timer_msb, self.__reg_txq6_enato_timer_lsb)
    @reg_txq6_enato_timer.setter
    def reg_txq6_enato_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_enato_timer_msb, self.__reg_txq6_enato_timer_lsb, value)
class MACTXQ6_PLCP0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0xcc
        self.__reg_txq6_ena_lsb = 31
        self.__reg_txq6_ena_msb = 31
        self.__reg_txq6_valid_lsb = 30
        self.__reg_txq6_valid_msb = 30
        self.__reg_txq6_txop_lsb = 29
        self.__reg_txq6_txop_msb = 29
        self.__reg_txq6_cts_lsb = 28
        self.__reg_txq6_cts_msb = 28
        self.__reg_txq6_rts_lsb = 27
        self.__reg_txq6_rts_msb = 27
        self.__reg_txq6_ack_lsb = 24
        self.__reg_txq6_ack_msb = 26
        self.__reg_txq6_cf_lsb = 23
        self.__reg_txq6_cf_msb = 23
        self.__reg_txq6_autodur_lsb = 22
        self.__reg_txq6_autodur_msb = 22
        self.__reg_txq6_txenato_lsb = 21
        self.__reg_txq6_txenato_msb = 21
        self.__reg_txq6_hwseq_lsb = 20
        self.__reg_txq6_hwseq_msb = 20
        self.__reg_txq6_link_addr_lsb = 0
        self.__reg_txq6_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq6_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_ena_msb, self.__reg_txq6_ena_lsb)
    @reg_txq6_ena.setter
    def reg_txq6_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_ena_msb, self.__reg_txq6_ena_lsb, value)

    @property
    def reg_txq6_valid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_valid_msb, self.__reg_txq6_valid_lsb)
    @reg_txq6_valid.setter
    def reg_txq6_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_valid_msb, self.__reg_txq6_valid_lsb, value)

    @property
    def reg_txq6_txop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_txop_msb, self.__reg_txq6_txop_lsb)
    @reg_txq6_txop.setter
    def reg_txq6_txop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_txop_msb, self.__reg_txq6_txop_lsb, value)

    @property
    def reg_txq6_cts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_cts_msb, self.__reg_txq6_cts_lsb)
    @reg_txq6_cts.setter
    def reg_txq6_cts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_cts_msb, self.__reg_txq6_cts_lsb, value)

    @property
    def reg_txq6_rts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_rts_msb, self.__reg_txq6_rts_lsb)
    @reg_txq6_rts.setter
    def reg_txq6_rts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_rts_msb, self.__reg_txq6_rts_lsb, value)

    @property
    def reg_txq6_ack(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_ack_msb, self.__reg_txq6_ack_lsb)
    @reg_txq6_ack.setter
    def reg_txq6_ack(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_ack_msb, self.__reg_txq6_ack_lsb, value)

    @property
    def reg_txq6_cf(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_cf_msb, self.__reg_txq6_cf_lsb)
    @reg_txq6_cf.setter
    def reg_txq6_cf(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_cf_msb, self.__reg_txq6_cf_lsb, value)

    @property
    def reg_txq6_autodur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_autodur_msb, self.__reg_txq6_autodur_lsb)
    @reg_txq6_autodur.setter
    def reg_txq6_autodur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_autodur_msb, self.__reg_txq6_autodur_lsb, value)

    @property
    def reg_txq6_txenato(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_txenato_msb, self.__reg_txq6_txenato_lsb)
    @reg_txq6_txenato.setter
    def reg_txq6_txenato(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_txenato_msb, self.__reg_txq6_txenato_lsb, value)

    @property
    def reg_txq6_hwseq(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_hwseq_msb, self.__reg_txq6_hwseq_lsb)
    @reg_txq6_hwseq.setter
    def reg_txq6_hwseq(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_hwseq_msb, self.__reg_txq6_hwseq_lsb, value)

    @property
    def reg_txq6_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_link_addr_msb, self.__reg_txq6_link_addr_lsb)
    @reg_txq6_link_addr.setter
    def reg_txq6_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_link_addr_msb, self.__reg_txq6_link_addr_lsb, value)
class MACTXQ5_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0xd0
        self.__reg_txq5_pti_lsb = 28
        self.__reg_txq5_pti_msb = 31
        self.__reg_txq5_aifs_lsb = 24
        self.__reg_txq5_aifs_msb = 27
        self.__txq5_inbackoff_lsb = 23
        self.__txq5_inbackoff_msb = 23
        self.__txq5_inaifs_lsb = 22
        self.__txq5_inaifs_msb = 22
        self.__reg_txq5_backoff_lsb = 12
        self.__reg_txq5_backoff_msb = 21
        self.__reg_txq5_enato_timer_lsb = 0
        self.__reg_txq5_enato_timer_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq5_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_pti_msb, self.__reg_txq5_pti_lsb)
    @reg_txq5_pti.setter
    def reg_txq5_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_pti_msb, self.__reg_txq5_pti_lsb, value)

    @property
    def reg_txq5_aifs(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_aifs_msb, self.__reg_txq5_aifs_lsb)
    @reg_txq5_aifs.setter
    def reg_txq5_aifs(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_aifs_msb, self.__reg_txq5_aifs_lsb, value)

    @property
    def txq5_inbackoff(self):
        return self.__MEM.rdm(self.__addr, self.__txq5_inbackoff_msb, self.__txq5_inbackoff_lsb)
    @txq5_inbackoff.setter
    def txq5_inbackoff(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq5_inbackoff_msb, self.__txq5_inbackoff_lsb, value)

    @property
    def txq5_inaifs(self):
        return self.__MEM.rdm(self.__addr, self.__txq5_inaifs_msb, self.__txq5_inaifs_lsb)
    @txq5_inaifs.setter
    def txq5_inaifs(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq5_inaifs_msb, self.__txq5_inaifs_lsb, value)

    @property
    def reg_txq5_backoff(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_backoff_msb, self.__reg_txq5_backoff_lsb)
    @reg_txq5_backoff.setter
    def reg_txq5_backoff(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_backoff_msb, self.__reg_txq5_backoff_lsb, value)

    @property
    def reg_txq5_enato_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_enato_timer_msb, self.__reg_txq5_enato_timer_lsb)
    @reg_txq5_enato_timer.setter
    def reg_txq5_enato_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_enato_timer_msb, self.__reg_txq5_enato_timer_lsb, value)
class MACTXQ5_PLCP0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0xd4
        self.__reg_txq5_ena_lsb = 31
        self.__reg_txq5_ena_msb = 31
        self.__reg_txq5_valid_lsb = 30
        self.__reg_txq5_valid_msb = 30
        self.__reg_txq5_txop_lsb = 29
        self.__reg_txq5_txop_msb = 29
        self.__reg_txq5_cts_lsb = 28
        self.__reg_txq5_cts_msb = 28
        self.__reg_txq5_rts_lsb = 27
        self.__reg_txq5_rts_msb = 27
        self.__reg_txq5_ack_lsb = 24
        self.__reg_txq5_ack_msb = 26
        self.__reg_txq5_cf_lsb = 23
        self.__reg_txq5_cf_msb = 23
        self.__reg_txq5_autodur_lsb = 22
        self.__reg_txq5_autodur_msb = 22
        self.__reg_txq5_txenato_lsb = 21
        self.__reg_txq5_txenato_msb = 21
        self.__reg_txq5_hwseq_lsb = 20
        self.__reg_txq5_hwseq_msb = 20
        self.__reg_txq5_link_addr_lsb = 0
        self.__reg_txq5_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq5_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_ena_msb, self.__reg_txq5_ena_lsb)
    @reg_txq5_ena.setter
    def reg_txq5_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_ena_msb, self.__reg_txq5_ena_lsb, value)

    @property
    def reg_txq5_valid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_valid_msb, self.__reg_txq5_valid_lsb)
    @reg_txq5_valid.setter
    def reg_txq5_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_valid_msb, self.__reg_txq5_valid_lsb, value)

    @property
    def reg_txq5_txop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_txop_msb, self.__reg_txq5_txop_lsb)
    @reg_txq5_txop.setter
    def reg_txq5_txop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_txop_msb, self.__reg_txq5_txop_lsb, value)

    @property
    def reg_txq5_cts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_cts_msb, self.__reg_txq5_cts_lsb)
    @reg_txq5_cts.setter
    def reg_txq5_cts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_cts_msb, self.__reg_txq5_cts_lsb, value)

    @property
    def reg_txq5_rts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_rts_msb, self.__reg_txq5_rts_lsb)
    @reg_txq5_rts.setter
    def reg_txq5_rts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_rts_msb, self.__reg_txq5_rts_lsb, value)

    @property
    def reg_txq5_ack(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_ack_msb, self.__reg_txq5_ack_lsb)
    @reg_txq5_ack.setter
    def reg_txq5_ack(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_ack_msb, self.__reg_txq5_ack_lsb, value)

    @property
    def reg_txq5_cf(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_cf_msb, self.__reg_txq5_cf_lsb)
    @reg_txq5_cf.setter
    def reg_txq5_cf(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_cf_msb, self.__reg_txq5_cf_lsb, value)

    @property
    def reg_txq5_autodur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_autodur_msb, self.__reg_txq5_autodur_lsb)
    @reg_txq5_autodur.setter
    def reg_txq5_autodur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_autodur_msb, self.__reg_txq5_autodur_lsb, value)

    @property
    def reg_txq5_txenato(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_txenato_msb, self.__reg_txq5_txenato_lsb)
    @reg_txq5_txenato.setter
    def reg_txq5_txenato(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_txenato_msb, self.__reg_txq5_txenato_lsb, value)

    @property
    def reg_txq5_hwseq(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_hwseq_msb, self.__reg_txq5_hwseq_lsb)
    @reg_txq5_hwseq.setter
    def reg_txq5_hwseq(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_hwseq_msb, self.__reg_txq5_hwseq_lsb, value)

    @property
    def reg_txq5_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_link_addr_msb, self.__reg_txq5_link_addr_lsb)
    @reg_txq5_link_addr.setter
    def reg_txq5_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_link_addr_msb, self.__reg_txq5_link_addr_lsb, value)
class MACTXQ4_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0xd8
        self.__reg_txq4_pti_lsb = 28
        self.__reg_txq4_pti_msb = 31
        self.__reg_txq4_aifs_lsb = 24
        self.__reg_txq4_aifs_msb = 27
        self.__txq4_inbackoff_lsb = 23
        self.__txq4_inbackoff_msb = 23
        self.__txq4_inaifs_lsb = 22
        self.__txq4_inaifs_msb = 22
        self.__reg_txq4_backoff_lsb = 12
        self.__reg_txq4_backoff_msb = 21
        self.__reg_txq4_enato_timer_lsb = 0
        self.__reg_txq4_enato_timer_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq4_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_pti_msb, self.__reg_txq4_pti_lsb)
    @reg_txq4_pti.setter
    def reg_txq4_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_pti_msb, self.__reg_txq4_pti_lsb, value)

    @property
    def reg_txq4_aifs(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_aifs_msb, self.__reg_txq4_aifs_lsb)
    @reg_txq4_aifs.setter
    def reg_txq4_aifs(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_aifs_msb, self.__reg_txq4_aifs_lsb, value)

    @property
    def txq4_inbackoff(self):
        return self.__MEM.rdm(self.__addr, self.__txq4_inbackoff_msb, self.__txq4_inbackoff_lsb)
    @txq4_inbackoff.setter
    def txq4_inbackoff(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq4_inbackoff_msb, self.__txq4_inbackoff_lsb, value)

    @property
    def txq4_inaifs(self):
        return self.__MEM.rdm(self.__addr, self.__txq4_inaifs_msb, self.__txq4_inaifs_lsb)
    @txq4_inaifs.setter
    def txq4_inaifs(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq4_inaifs_msb, self.__txq4_inaifs_lsb, value)

    @property
    def reg_txq4_backoff(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_backoff_msb, self.__reg_txq4_backoff_lsb)
    @reg_txq4_backoff.setter
    def reg_txq4_backoff(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_backoff_msb, self.__reg_txq4_backoff_lsb, value)

    @property
    def reg_txq4_enato_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_enato_timer_msb, self.__reg_txq4_enato_timer_lsb)
    @reg_txq4_enato_timer.setter
    def reg_txq4_enato_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_enato_timer_msb, self.__reg_txq4_enato_timer_lsb, value)
class MACTXQ4_PLCP0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0xdc
        self.__reg_txq4_ena_lsb = 31
        self.__reg_txq4_ena_msb = 31
        self.__reg_txq4_valid_lsb = 30
        self.__reg_txq4_valid_msb = 30
        self.__reg_txq4_txop_lsb = 29
        self.__reg_txq4_txop_msb = 29
        self.__reg_txq4_cts_lsb = 28
        self.__reg_txq4_cts_msb = 28
        self.__reg_txq4_rts_lsb = 27
        self.__reg_txq4_rts_msb = 27
        self.__reg_txq4_ack_lsb = 24
        self.__reg_txq4_ack_msb = 26
        self.__reg_txq4_cf_lsb = 23
        self.__reg_txq4_cf_msb = 23
        self.__reg_txq4_autodur_lsb = 22
        self.__reg_txq4_autodur_msb = 22
        self.__reg_txq4_txenato_lsb = 21
        self.__reg_txq4_txenato_msb = 21
        self.__reg_txq4_hwseq_lsb = 20
        self.__reg_txq4_hwseq_msb = 20
        self.__reg_txq4_link_addr_lsb = 0
        self.__reg_txq4_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq4_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_ena_msb, self.__reg_txq4_ena_lsb)
    @reg_txq4_ena.setter
    def reg_txq4_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_ena_msb, self.__reg_txq4_ena_lsb, value)

    @property
    def reg_txq4_valid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_valid_msb, self.__reg_txq4_valid_lsb)
    @reg_txq4_valid.setter
    def reg_txq4_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_valid_msb, self.__reg_txq4_valid_lsb, value)

    @property
    def reg_txq4_txop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_txop_msb, self.__reg_txq4_txop_lsb)
    @reg_txq4_txop.setter
    def reg_txq4_txop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_txop_msb, self.__reg_txq4_txop_lsb, value)

    @property
    def reg_txq4_cts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_cts_msb, self.__reg_txq4_cts_lsb)
    @reg_txq4_cts.setter
    def reg_txq4_cts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_cts_msb, self.__reg_txq4_cts_lsb, value)

    @property
    def reg_txq4_rts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_rts_msb, self.__reg_txq4_rts_lsb)
    @reg_txq4_rts.setter
    def reg_txq4_rts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_rts_msb, self.__reg_txq4_rts_lsb, value)

    @property
    def reg_txq4_ack(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_ack_msb, self.__reg_txq4_ack_lsb)
    @reg_txq4_ack.setter
    def reg_txq4_ack(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_ack_msb, self.__reg_txq4_ack_lsb, value)

    @property
    def reg_txq4_cf(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_cf_msb, self.__reg_txq4_cf_lsb)
    @reg_txq4_cf.setter
    def reg_txq4_cf(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_cf_msb, self.__reg_txq4_cf_lsb, value)

    @property
    def reg_txq4_autodur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_autodur_msb, self.__reg_txq4_autodur_lsb)
    @reg_txq4_autodur.setter
    def reg_txq4_autodur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_autodur_msb, self.__reg_txq4_autodur_lsb, value)

    @property
    def reg_txq4_txenato(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_txenato_msb, self.__reg_txq4_txenato_lsb)
    @reg_txq4_txenato.setter
    def reg_txq4_txenato(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_txenato_msb, self.__reg_txq4_txenato_lsb, value)

    @property
    def reg_txq4_hwseq(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_hwseq_msb, self.__reg_txq4_hwseq_lsb)
    @reg_txq4_hwseq.setter
    def reg_txq4_hwseq(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_hwseq_msb, self.__reg_txq4_hwseq_lsb, value)

    @property
    def reg_txq4_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_link_addr_msb, self.__reg_txq4_link_addr_lsb)
    @reg_txq4_link_addr.setter
    def reg_txq4_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_link_addr_msb, self.__reg_txq4_link_addr_lsb, value)
class MACTXQ3_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0xe0
        self.__reg_txq3_pti_lsb = 28
        self.__reg_txq3_pti_msb = 31
        self.__reg_txq3_aifs_lsb = 24
        self.__reg_txq3_aifs_msb = 27
        self.__txq3_inbackoff_lsb = 23
        self.__txq3_inbackoff_msb = 23
        self.__txq3_inaifs_lsb = 22
        self.__txq3_inaifs_msb = 22
        self.__reg_txq3_backoff_lsb = 12
        self.__reg_txq3_backoff_msb = 21
        self.__reg_txq3_enato_timer_lsb = 0
        self.__reg_txq3_enato_timer_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq3_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_pti_msb, self.__reg_txq3_pti_lsb)
    @reg_txq3_pti.setter
    def reg_txq3_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_pti_msb, self.__reg_txq3_pti_lsb, value)

    @property
    def reg_txq3_aifs(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_aifs_msb, self.__reg_txq3_aifs_lsb)
    @reg_txq3_aifs.setter
    def reg_txq3_aifs(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_aifs_msb, self.__reg_txq3_aifs_lsb, value)

    @property
    def txq3_inbackoff(self):
        return self.__MEM.rdm(self.__addr, self.__txq3_inbackoff_msb, self.__txq3_inbackoff_lsb)
    @txq3_inbackoff.setter
    def txq3_inbackoff(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq3_inbackoff_msb, self.__txq3_inbackoff_lsb, value)

    @property
    def txq3_inaifs(self):
        return self.__MEM.rdm(self.__addr, self.__txq3_inaifs_msb, self.__txq3_inaifs_lsb)
    @txq3_inaifs.setter
    def txq3_inaifs(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq3_inaifs_msb, self.__txq3_inaifs_lsb, value)

    @property
    def reg_txq3_backoff(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_backoff_msb, self.__reg_txq3_backoff_lsb)
    @reg_txq3_backoff.setter
    def reg_txq3_backoff(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_backoff_msb, self.__reg_txq3_backoff_lsb, value)

    @property
    def reg_txq3_enato_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_enato_timer_msb, self.__reg_txq3_enato_timer_lsb)
    @reg_txq3_enato_timer.setter
    def reg_txq3_enato_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_enato_timer_msb, self.__reg_txq3_enato_timer_lsb, value)
class MACTXQ3_PLCP0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0xe4
        self.__reg_txq3_ena_lsb = 31
        self.__reg_txq3_ena_msb = 31
        self.__reg_txq3_valid_lsb = 30
        self.__reg_txq3_valid_msb = 30
        self.__reg_txq3_txop_lsb = 29
        self.__reg_txq3_txop_msb = 29
        self.__reg_txq3_cts_lsb = 28
        self.__reg_txq3_cts_msb = 28
        self.__reg_txq3_rts_lsb = 27
        self.__reg_txq3_rts_msb = 27
        self.__reg_txq3_ack_lsb = 24
        self.__reg_txq3_ack_msb = 26
        self.__reg_txq3_cf_lsb = 23
        self.__reg_txq3_cf_msb = 23
        self.__reg_txq3_autodur_lsb = 22
        self.__reg_txq3_autodur_msb = 22
        self.__reg_txq3_txenato_lsb = 21
        self.__reg_txq3_txenato_msb = 21
        self.__reg_txq3_hwseq_lsb = 20
        self.__reg_txq3_hwseq_msb = 20
        self.__reg_txq3_link_addr_lsb = 0
        self.__reg_txq3_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq3_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_ena_msb, self.__reg_txq3_ena_lsb)
    @reg_txq3_ena.setter
    def reg_txq3_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_ena_msb, self.__reg_txq3_ena_lsb, value)

    @property
    def reg_txq3_valid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_valid_msb, self.__reg_txq3_valid_lsb)
    @reg_txq3_valid.setter
    def reg_txq3_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_valid_msb, self.__reg_txq3_valid_lsb, value)

    @property
    def reg_txq3_txop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_txop_msb, self.__reg_txq3_txop_lsb)
    @reg_txq3_txop.setter
    def reg_txq3_txop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_txop_msb, self.__reg_txq3_txop_lsb, value)

    @property
    def reg_txq3_cts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_cts_msb, self.__reg_txq3_cts_lsb)
    @reg_txq3_cts.setter
    def reg_txq3_cts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_cts_msb, self.__reg_txq3_cts_lsb, value)

    @property
    def reg_txq3_rts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_rts_msb, self.__reg_txq3_rts_lsb)
    @reg_txq3_rts.setter
    def reg_txq3_rts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_rts_msb, self.__reg_txq3_rts_lsb, value)

    @property
    def reg_txq3_ack(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_ack_msb, self.__reg_txq3_ack_lsb)
    @reg_txq3_ack.setter
    def reg_txq3_ack(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_ack_msb, self.__reg_txq3_ack_lsb, value)

    @property
    def reg_txq3_cf(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_cf_msb, self.__reg_txq3_cf_lsb)
    @reg_txq3_cf.setter
    def reg_txq3_cf(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_cf_msb, self.__reg_txq3_cf_lsb, value)

    @property
    def reg_txq3_autodur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_autodur_msb, self.__reg_txq3_autodur_lsb)
    @reg_txq3_autodur.setter
    def reg_txq3_autodur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_autodur_msb, self.__reg_txq3_autodur_lsb, value)

    @property
    def reg_txq3_txenato(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_txenato_msb, self.__reg_txq3_txenato_lsb)
    @reg_txq3_txenato.setter
    def reg_txq3_txenato(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_txenato_msb, self.__reg_txq3_txenato_lsb, value)

    @property
    def reg_txq3_hwseq(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_hwseq_msb, self.__reg_txq3_hwseq_lsb)
    @reg_txq3_hwseq.setter
    def reg_txq3_hwseq(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_hwseq_msb, self.__reg_txq3_hwseq_lsb, value)

    @property
    def reg_txq3_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_link_addr_msb, self.__reg_txq3_link_addr_lsb)
    @reg_txq3_link_addr.setter
    def reg_txq3_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_link_addr_msb, self.__reg_txq3_link_addr_lsb, value)
class MACTXQ2_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0xe8
        self.__reg_txq2_pti_lsb = 28
        self.__reg_txq2_pti_msb = 31
        self.__reg_txq2_aifs_lsb = 24
        self.__reg_txq2_aifs_msb = 27
        self.__txq2_inbackoff_lsb = 23
        self.__txq2_inbackoff_msb = 23
        self.__txq2_inaifs_lsb = 22
        self.__txq2_inaifs_msb = 22
        self.__reg_txq2_backoff_lsb = 12
        self.__reg_txq2_backoff_msb = 21
        self.__reg_txq2_enato_timer_lsb = 0
        self.__reg_txq2_enato_timer_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq2_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_pti_msb, self.__reg_txq2_pti_lsb)
    @reg_txq2_pti.setter
    def reg_txq2_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_pti_msb, self.__reg_txq2_pti_lsb, value)

    @property
    def reg_txq2_aifs(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_aifs_msb, self.__reg_txq2_aifs_lsb)
    @reg_txq2_aifs.setter
    def reg_txq2_aifs(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_aifs_msb, self.__reg_txq2_aifs_lsb, value)

    @property
    def txq2_inbackoff(self):
        return self.__MEM.rdm(self.__addr, self.__txq2_inbackoff_msb, self.__txq2_inbackoff_lsb)
    @txq2_inbackoff.setter
    def txq2_inbackoff(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq2_inbackoff_msb, self.__txq2_inbackoff_lsb, value)

    @property
    def txq2_inaifs(self):
        return self.__MEM.rdm(self.__addr, self.__txq2_inaifs_msb, self.__txq2_inaifs_lsb)
    @txq2_inaifs.setter
    def txq2_inaifs(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq2_inaifs_msb, self.__txq2_inaifs_lsb, value)

    @property
    def reg_txq2_backoff(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_backoff_msb, self.__reg_txq2_backoff_lsb)
    @reg_txq2_backoff.setter
    def reg_txq2_backoff(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_backoff_msb, self.__reg_txq2_backoff_lsb, value)

    @property
    def reg_txq2_enato_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_enato_timer_msb, self.__reg_txq2_enato_timer_lsb)
    @reg_txq2_enato_timer.setter
    def reg_txq2_enato_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_enato_timer_msb, self.__reg_txq2_enato_timer_lsb, value)
class MACTXQ2_PLCP0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0xec
        self.__reg_txq2_ena_lsb = 31
        self.__reg_txq2_ena_msb = 31
        self.__reg_txq2_valid_lsb = 30
        self.__reg_txq2_valid_msb = 30
        self.__reg_txq2_txop_lsb = 29
        self.__reg_txq2_txop_msb = 29
        self.__reg_txq2_cts_lsb = 28
        self.__reg_txq2_cts_msb = 28
        self.__reg_txq2_rts_lsb = 27
        self.__reg_txq2_rts_msb = 27
        self.__reg_txq2_ack_lsb = 24
        self.__reg_txq2_ack_msb = 26
        self.__reg_txq2_cf_lsb = 23
        self.__reg_txq2_cf_msb = 23
        self.__reg_txq2_autodur_lsb = 22
        self.__reg_txq2_autodur_msb = 22
        self.__reg_txq2_txenato_lsb = 21
        self.__reg_txq2_txenato_msb = 21
        self.__reg_txq2_hwseq_lsb = 20
        self.__reg_txq2_hwseq_msb = 20
        self.__reg_txq2_link_addr_lsb = 0
        self.__reg_txq2_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq2_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_ena_msb, self.__reg_txq2_ena_lsb)
    @reg_txq2_ena.setter
    def reg_txq2_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_ena_msb, self.__reg_txq2_ena_lsb, value)

    @property
    def reg_txq2_valid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_valid_msb, self.__reg_txq2_valid_lsb)
    @reg_txq2_valid.setter
    def reg_txq2_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_valid_msb, self.__reg_txq2_valid_lsb, value)

    @property
    def reg_txq2_txop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_txop_msb, self.__reg_txq2_txop_lsb)
    @reg_txq2_txop.setter
    def reg_txq2_txop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_txop_msb, self.__reg_txq2_txop_lsb, value)

    @property
    def reg_txq2_cts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_cts_msb, self.__reg_txq2_cts_lsb)
    @reg_txq2_cts.setter
    def reg_txq2_cts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_cts_msb, self.__reg_txq2_cts_lsb, value)

    @property
    def reg_txq2_rts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_rts_msb, self.__reg_txq2_rts_lsb)
    @reg_txq2_rts.setter
    def reg_txq2_rts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_rts_msb, self.__reg_txq2_rts_lsb, value)

    @property
    def reg_txq2_ack(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_ack_msb, self.__reg_txq2_ack_lsb)
    @reg_txq2_ack.setter
    def reg_txq2_ack(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_ack_msb, self.__reg_txq2_ack_lsb, value)

    @property
    def reg_txq2_cf(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_cf_msb, self.__reg_txq2_cf_lsb)
    @reg_txq2_cf.setter
    def reg_txq2_cf(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_cf_msb, self.__reg_txq2_cf_lsb, value)

    @property
    def reg_txq2_autodur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_autodur_msb, self.__reg_txq2_autodur_lsb)
    @reg_txq2_autodur.setter
    def reg_txq2_autodur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_autodur_msb, self.__reg_txq2_autodur_lsb, value)

    @property
    def reg_txq2_txenato(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_txenato_msb, self.__reg_txq2_txenato_lsb)
    @reg_txq2_txenato.setter
    def reg_txq2_txenato(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_txenato_msb, self.__reg_txq2_txenato_lsb, value)

    @property
    def reg_txq2_hwseq(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_hwseq_msb, self.__reg_txq2_hwseq_lsb)
    @reg_txq2_hwseq.setter
    def reg_txq2_hwseq(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_hwseq_msb, self.__reg_txq2_hwseq_lsb, value)

    @property
    def reg_txq2_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_link_addr_msb, self.__reg_txq2_link_addr_lsb)
    @reg_txq2_link_addr.setter
    def reg_txq2_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_link_addr_msb, self.__reg_txq2_link_addr_lsb, value)
class MACTXQ1_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0xf0
        self.__reg_txq1_pti_lsb = 28
        self.__reg_txq1_pti_msb = 31
        self.__reg_txq1_aifs_lsb = 24
        self.__reg_txq1_aifs_msb = 27
        self.__txq1_inbackoff_lsb = 23
        self.__txq1_inbackoff_msb = 23
        self.__txq1_inaifs_lsb = 22
        self.__txq1_inaifs_msb = 22
        self.__reg_txq1_backoff_lsb = 12
        self.__reg_txq1_backoff_msb = 21
        self.__reg_txq1_enato_timer_lsb = 0
        self.__reg_txq1_enato_timer_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq1_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_pti_msb, self.__reg_txq1_pti_lsb)
    @reg_txq1_pti.setter
    def reg_txq1_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_pti_msb, self.__reg_txq1_pti_lsb, value)

    @property
    def reg_txq1_aifs(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_aifs_msb, self.__reg_txq1_aifs_lsb)
    @reg_txq1_aifs.setter
    def reg_txq1_aifs(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_aifs_msb, self.__reg_txq1_aifs_lsb, value)

    @property
    def txq1_inbackoff(self):
        return self.__MEM.rdm(self.__addr, self.__txq1_inbackoff_msb, self.__txq1_inbackoff_lsb)
    @txq1_inbackoff.setter
    def txq1_inbackoff(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq1_inbackoff_msb, self.__txq1_inbackoff_lsb, value)

    @property
    def txq1_inaifs(self):
        return self.__MEM.rdm(self.__addr, self.__txq1_inaifs_msb, self.__txq1_inaifs_lsb)
    @txq1_inaifs.setter
    def txq1_inaifs(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq1_inaifs_msb, self.__txq1_inaifs_lsb, value)

    @property
    def reg_txq1_backoff(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_backoff_msb, self.__reg_txq1_backoff_lsb)
    @reg_txq1_backoff.setter
    def reg_txq1_backoff(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_backoff_msb, self.__reg_txq1_backoff_lsb, value)

    @property
    def reg_txq1_enato_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_enato_timer_msb, self.__reg_txq1_enato_timer_lsb)
    @reg_txq1_enato_timer.setter
    def reg_txq1_enato_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_enato_timer_msb, self.__reg_txq1_enato_timer_lsb, value)
class MACTXQ1_PLCP0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0xf4
        self.__reg_txq1_ena_lsb = 31
        self.__reg_txq1_ena_msb = 31
        self.__reg_txq1_valid_lsb = 30
        self.__reg_txq1_valid_msb = 30
        self.__reg_txq1_txop_lsb = 29
        self.__reg_txq1_txop_msb = 29
        self.__reg_txq1_cts_lsb = 28
        self.__reg_txq1_cts_msb = 28
        self.__reg_txq1_rts_lsb = 27
        self.__reg_txq1_rts_msb = 27
        self.__reg_txq1_ack_lsb = 24
        self.__reg_txq1_ack_msb = 26
        self.__reg_txq1_cf_lsb = 23
        self.__reg_txq1_cf_msb = 23
        self.__reg_txq1_autodur_lsb = 22
        self.__reg_txq1_autodur_msb = 22
        self.__reg_txq1_txenato_lsb = 21
        self.__reg_txq1_txenato_msb = 21
        self.__reg_txq1_hwseq_lsb = 20
        self.__reg_txq1_hwseq_msb = 20
        self.__reg_txq1_link_addr_lsb = 0
        self.__reg_txq1_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq1_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_ena_msb, self.__reg_txq1_ena_lsb)
    @reg_txq1_ena.setter
    def reg_txq1_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_ena_msb, self.__reg_txq1_ena_lsb, value)

    @property
    def reg_txq1_valid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_valid_msb, self.__reg_txq1_valid_lsb)
    @reg_txq1_valid.setter
    def reg_txq1_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_valid_msb, self.__reg_txq1_valid_lsb, value)

    @property
    def reg_txq1_txop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_txop_msb, self.__reg_txq1_txop_lsb)
    @reg_txq1_txop.setter
    def reg_txq1_txop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_txop_msb, self.__reg_txq1_txop_lsb, value)

    @property
    def reg_txq1_cts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_cts_msb, self.__reg_txq1_cts_lsb)
    @reg_txq1_cts.setter
    def reg_txq1_cts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_cts_msb, self.__reg_txq1_cts_lsb, value)

    @property
    def reg_txq1_rts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_rts_msb, self.__reg_txq1_rts_lsb)
    @reg_txq1_rts.setter
    def reg_txq1_rts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_rts_msb, self.__reg_txq1_rts_lsb, value)

    @property
    def reg_txq1_ack(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_ack_msb, self.__reg_txq1_ack_lsb)
    @reg_txq1_ack.setter
    def reg_txq1_ack(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_ack_msb, self.__reg_txq1_ack_lsb, value)

    @property
    def reg_txq1_cf(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_cf_msb, self.__reg_txq1_cf_lsb)
    @reg_txq1_cf.setter
    def reg_txq1_cf(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_cf_msb, self.__reg_txq1_cf_lsb, value)

    @property
    def reg_txq1_autodur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_autodur_msb, self.__reg_txq1_autodur_lsb)
    @reg_txq1_autodur.setter
    def reg_txq1_autodur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_autodur_msb, self.__reg_txq1_autodur_lsb, value)

    @property
    def reg_txq1_txenato(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_txenato_msb, self.__reg_txq1_txenato_lsb)
    @reg_txq1_txenato.setter
    def reg_txq1_txenato(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_txenato_msb, self.__reg_txq1_txenato_lsb, value)

    @property
    def reg_txq1_hwseq(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_hwseq_msb, self.__reg_txq1_hwseq_lsb)
    @reg_txq1_hwseq.setter
    def reg_txq1_hwseq(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_hwseq_msb, self.__reg_txq1_hwseq_lsb, value)

    @property
    def reg_txq1_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_link_addr_msb, self.__reg_txq1_link_addr_lsb)
    @reg_txq1_link_addr.setter
    def reg_txq1_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_link_addr_msb, self.__reg_txq1_link_addr_lsb, value)
class MACTXQ0_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0xf8
        self.__reg_txq0_pti_lsb = 28
        self.__reg_txq0_pti_msb = 31
        self.__reg_txq0_aifs_lsb = 24
        self.__reg_txq0_aifs_msb = 27
        self.__txq0_inbackoff_lsb = 23
        self.__txq0_inbackoff_msb = 23
        self.__txq0_inaifs_lsb = 22
        self.__txq0_inaifs_msb = 22
        self.__reg_txq0_backoff_lsb = 12
        self.__reg_txq0_backoff_msb = 21
        self.__reg_txq0_enato_timer_lsb = 0
        self.__reg_txq0_enato_timer_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq0_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_pti_msb, self.__reg_txq0_pti_lsb)
    @reg_txq0_pti.setter
    def reg_txq0_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_pti_msb, self.__reg_txq0_pti_lsb, value)

    @property
    def reg_txq0_aifs(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_aifs_msb, self.__reg_txq0_aifs_lsb)
    @reg_txq0_aifs.setter
    def reg_txq0_aifs(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_aifs_msb, self.__reg_txq0_aifs_lsb, value)

    @property
    def txq0_inbackoff(self):
        return self.__MEM.rdm(self.__addr, self.__txq0_inbackoff_msb, self.__txq0_inbackoff_lsb)
    @txq0_inbackoff.setter
    def txq0_inbackoff(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq0_inbackoff_msb, self.__txq0_inbackoff_lsb, value)

    @property
    def txq0_inaifs(self):
        return self.__MEM.rdm(self.__addr, self.__txq0_inaifs_msb, self.__txq0_inaifs_lsb)
    @txq0_inaifs.setter
    def txq0_inaifs(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq0_inaifs_msb, self.__txq0_inaifs_lsb, value)

    @property
    def reg_txq0_backoff(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_backoff_msb, self.__reg_txq0_backoff_lsb)
    @reg_txq0_backoff.setter
    def reg_txq0_backoff(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_backoff_msb, self.__reg_txq0_backoff_lsb, value)

    @property
    def reg_txq0_enato_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_enato_timer_msb, self.__reg_txq0_enato_timer_lsb)
    @reg_txq0_enato_timer.setter
    def reg_txq0_enato_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_enato_timer_msb, self.__reg_txq0_enato_timer_lsb, value)
class MACTXQ0_PLCP0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0xfc
        self.__reg_txq0_ena_lsb = 31
        self.__reg_txq0_ena_msb = 31
        self.__reg_txq0_valid_lsb = 30
        self.__reg_txq0_valid_msb = 30
        self.__reg_txq0_txop_lsb = 29
        self.__reg_txq0_txop_msb = 29
        self.__reg_txq0_cts_lsb = 28
        self.__reg_txq0_cts_msb = 28
        self.__reg_txq0_rts_lsb = 27
        self.__reg_txq0_rts_msb = 27
        self.__reg_txq0_ack_lsb = 24
        self.__reg_txq0_ack_msb = 26
        self.__reg_txq0_cf_lsb = 23
        self.__reg_txq0_cf_msb = 23
        self.__reg_txq0_autodur_lsb = 22
        self.__reg_txq0_autodur_msb = 22
        self.__reg_txq0_txenato_lsb = 21
        self.__reg_txq0_txenato_msb = 21
        self.__reg_txq0_hwseq_lsb = 20
        self.__reg_txq0_hwseq_msb = 20
        self.__reg_txq0_link_addr_lsb = 0
        self.__reg_txq0_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq0_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_ena_msb, self.__reg_txq0_ena_lsb)
    @reg_txq0_ena.setter
    def reg_txq0_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_ena_msb, self.__reg_txq0_ena_lsb, value)

    @property
    def reg_txq0_valid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_valid_msb, self.__reg_txq0_valid_lsb)
    @reg_txq0_valid.setter
    def reg_txq0_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_valid_msb, self.__reg_txq0_valid_lsb, value)

    @property
    def reg_txq0_txop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_txop_msb, self.__reg_txq0_txop_lsb)
    @reg_txq0_txop.setter
    def reg_txq0_txop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_txop_msb, self.__reg_txq0_txop_lsb, value)

    @property
    def reg_txq0_cts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_cts_msb, self.__reg_txq0_cts_lsb)
    @reg_txq0_cts.setter
    def reg_txq0_cts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_cts_msb, self.__reg_txq0_cts_lsb, value)

    @property
    def reg_txq0_rts(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_rts_msb, self.__reg_txq0_rts_lsb)
    @reg_txq0_rts.setter
    def reg_txq0_rts(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_rts_msb, self.__reg_txq0_rts_lsb, value)

    @property
    def reg_txq0_ack(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_ack_msb, self.__reg_txq0_ack_lsb)
    @reg_txq0_ack.setter
    def reg_txq0_ack(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_ack_msb, self.__reg_txq0_ack_lsb, value)

    @property
    def reg_txq0_cf(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_cf_msb, self.__reg_txq0_cf_lsb)
    @reg_txq0_cf.setter
    def reg_txq0_cf(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_cf_msb, self.__reg_txq0_cf_lsb, value)

    @property
    def reg_txq0_autodur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_autodur_msb, self.__reg_txq0_autodur_lsb)
    @reg_txq0_autodur.setter
    def reg_txq0_autodur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_autodur_msb, self.__reg_txq0_autodur_lsb, value)

    @property
    def reg_txq0_txenato(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_txenato_msb, self.__reg_txq0_txenato_lsb)
    @reg_txq0_txenato.setter
    def reg_txq0_txenato(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_txenato_msb, self.__reg_txq0_txenato_lsb, value)

    @property
    def reg_txq0_hwseq(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_hwseq_msb, self.__reg_txq0_hwseq_lsb)
    @reg_txq0_hwseq.setter
    def reg_txq0_hwseq(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_hwseq_msb, self.__reg_txq0_hwseq_lsb, value)

    @property
    def reg_txq0_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_link_addr_msb, self.__reg_txq0_link_addr_lsb)
    @reg_txq0_link_addr.setter
    def reg_txq0_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_link_addr_msb, self.__reg_txq0_link_addr_lsb, value)
class MACTXQ_PTI_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x100
        self.__reg_txq_pti_ahead_lsb = 31
        self.__reg_txq_pti_ahead_msb = 31
        self.__reg_txq_pti_aheadmode_lsb = 29
        self.__reg_txq_pti_aheadmode_msb = 30
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq_pti_ahead(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq_pti_ahead_msb, self.__reg_txq_pti_ahead_lsb)
    @reg_txq_pti_ahead.setter
    def reg_txq_pti_ahead(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq_pti_ahead_msb, self.__reg_txq_pti_ahead_lsb, value)

    @property
    def reg_txq_pti_aheadmode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq_pti_aheadmode_msb, self.__reg_txq_pti_aheadmode_lsb)
    @reg_txq_pti_aheadmode.setter
    def reg_txq_pti_aheadmode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq_pti_aheadmode_msb, self.__reg_txq_pti_aheadmode_lsb, value)
class MACTXQ_PRIO_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x104
        self.__reg_txq7_prio_lsb = 28
        self.__reg_txq7_prio_msb = 31
        self.__reg_txq6_prio_lsb = 24
        self.__reg_txq6_prio_msb = 27
        self.__reg_txq5_prio_lsb = 20
        self.__reg_txq5_prio_msb = 23
        self.__reg_txq4_prio_lsb = 16
        self.__reg_txq4_prio_msb = 19
        self.__reg_txq3_prio_lsb = 12
        self.__reg_txq3_prio_msb = 15
        self.__reg_txq2_prio_lsb = 8
        self.__reg_txq2_prio_msb = 11
        self.__reg_txq1_prio_lsb = 4
        self.__reg_txq1_prio_msb = 7
        self.__reg_txq0_prio_lsb = 0
        self.__reg_txq0_prio_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq7_prio(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_prio_msb, self.__reg_txq7_prio_lsb)
    @reg_txq7_prio.setter
    def reg_txq7_prio(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_prio_msb, self.__reg_txq7_prio_lsb, value)

    @property
    def reg_txq6_prio(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_prio_msb, self.__reg_txq6_prio_lsb)
    @reg_txq6_prio.setter
    def reg_txq6_prio(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_prio_msb, self.__reg_txq6_prio_lsb, value)

    @property
    def reg_txq5_prio(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_prio_msb, self.__reg_txq5_prio_lsb)
    @reg_txq5_prio.setter
    def reg_txq5_prio(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_prio_msb, self.__reg_txq5_prio_lsb, value)

    @property
    def reg_txq4_prio(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_prio_msb, self.__reg_txq4_prio_lsb)
    @reg_txq4_prio.setter
    def reg_txq4_prio(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_prio_msb, self.__reg_txq4_prio_lsb, value)

    @property
    def reg_txq3_prio(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_prio_msb, self.__reg_txq3_prio_lsb)
    @reg_txq3_prio.setter
    def reg_txq3_prio(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_prio_msb, self.__reg_txq3_prio_lsb, value)

    @property
    def reg_txq2_prio(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_prio_msb, self.__reg_txq2_prio_lsb)
    @reg_txq2_prio.setter
    def reg_txq2_prio(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_prio_msb, self.__reg_txq2_prio_lsb, value)

    @property
    def reg_txq1_prio(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_prio_msb, self.__reg_txq1_prio_lsb)
    @reg_txq1_prio.setter
    def reg_txq1_prio(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_prio_msb, self.__reg_txq1_prio_lsb, value)

    @property
    def reg_txq0_prio(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_prio_msb, self.__reg_txq0_prio_lsb)
    @reg_txq0_prio.setter
    def reg_txq0_prio(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_prio_msb, self.__reg_txq0_prio_lsb, value)
class MACTXQMEM(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x108
        self.__reg_txqmem_clear_lsb = 1
        self.__reg_txqmem_clear_msb = 1
        self.__txqmem_ready_lsb = 0
        self.__txqmem_ready_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txqmem_clear(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txqmem_clear_msb, self.__reg_txqmem_clear_lsb)
    @reg_txqmem_clear.setter
    def reg_txqmem_clear(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txqmem_clear_msb, self.__reg_txqmem_clear_lsb, value)

    @property
    def txqmem_ready(self):
        return self.__MEM.rdm(self.__addr, self.__txqmem_ready_msb, self.__txqmem_ready_lsb)
    @txqmem_ready.setter
    def txqmem_ready(self, value):
        return self.__MEM.wrm(self.__addr, self.__txqmem_ready_msb, self.__txqmem_ready_lsb, value)
class MACTXSEQ_NUM(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x10c
        self.__curr_seqnum_lsb = 12
        self.__curr_seqnum_msb = 23
        self.__reg_start_seqnum_lsb = 0
        self.__reg_start_seqnum_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def curr_seqnum(self):
        return self.__MEM.rdm(self.__addr, self.__curr_seqnum_msb, self.__curr_seqnum_lsb)
    @curr_seqnum.setter
    def curr_seqnum(self, value):
        return self.__MEM.wrm(self.__addr, self.__curr_seqnum_msb, self.__curr_seqnum_lsb, value)

    @property
    def reg_start_seqnum(self):
        return self.__MEM.rdm(self.__addr, self.__reg_start_seqnum_msb, self.__reg_start_seqnum_lsb)
    @reg_start_seqnum.setter
    def reg_start_seqnum(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_start_seqnum_msb, self.__reg_start_seqnum_lsb, value)
class MACTX_HOLD(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x110
        self.__reg_txhold_ofdm_lsb = 8
        self.__reg_txhold_ofdm_msb = 13
        self.__reg_txhold_cck_lsb = 0
        self.__reg_txhold_cck_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txhold_ofdm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txhold_ofdm_msb, self.__reg_txhold_ofdm_lsb)
    @reg_txhold_ofdm.setter
    def reg_txhold_ofdm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txhold_ofdm_msb, self.__reg_txhold_ofdm_lsb, value)

    @property
    def reg_txhold_cck(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txhold_cck_msb, self.__reg_txhold_cck_lsb)
    @reg_txhold_cck.setter
    def reg_txhold_cck(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txhold_cck_msb, self.__reg_txhold_cck_lsb, value)
class MACDURSIFS(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x114
        self.__reg_dur_sifs11lr_lsb = 24
        self.__reg_dur_sifs11lr_msb = 31
        self.__reg_dur_sifs11b_lsb = 16
        self.__reg_dur_sifs11b_msb = 23
        self.__reg_dur_sifs11g_lsb = 8
        self.__reg_dur_sifs11g_msb = 15
        self.__reg_dur_sifs11n_lsb = 0
        self.__reg_dur_sifs11n_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_dur_sifs11lr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dur_sifs11lr_msb, self.__reg_dur_sifs11lr_lsb)
    @reg_dur_sifs11lr.setter
    def reg_dur_sifs11lr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dur_sifs11lr_msb, self.__reg_dur_sifs11lr_lsb, value)

    @property
    def reg_dur_sifs11b(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dur_sifs11b_msb, self.__reg_dur_sifs11b_lsb)
    @reg_dur_sifs11b.setter
    def reg_dur_sifs11b(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dur_sifs11b_msb, self.__reg_dur_sifs11b_lsb, value)

    @property
    def reg_dur_sifs11g(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dur_sifs11g_msb, self.__reg_dur_sifs11g_lsb)
    @reg_dur_sifs11g.setter
    def reg_dur_sifs11g(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dur_sifs11g_msb, self.__reg_dur_sifs11g_lsb, value)

    @property
    def reg_dur_sifs11n(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dur_sifs11n_msb, self.__reg_dur_sifs11n_lsb)
    @reg_dur_sifs11n.setter
    def reg_dur_sifs11n(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dur_sifs11n_msb, self.__reg_dur_sifs11n_lsb, value)
class MACTIMER_TAR0_ENA(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x118
        self.__reg_timer_target0_ena_lsb = 0
        self.__reg_timer_target0_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_timer_target0_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_timer_target0_ena_msb, self.__reg_timer_target0_ena_lsb)
    @reg_timer_target0_ena.setter
    def reg_timer_target0_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_timer_target0_ena_msb, self.__reg_timer_target0_ena_lsb, value)
class MACTIMER_TAR0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x11c
        self.__reg_timer_target0_lsb = 0
        self.__reg_timer_target0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_timer_target0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_timer_target0_msb, self.__reg_timer_target0_lsb)
    @reg_timer_target0.setter
    def reg_timer_target0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_timer_target0_msb, self.__reg_timer_target0_lsb, value)
class MACTIMER_TAR1_ENA(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x120
        self.__reg_timer_target1_ena_lsb = 0
        self.__reg_timer_target1_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_timer_target1_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_timer_target1_ena_msb, self.__reg_timer_target1_ena_lsb)
    @reg_timer_target1_ena.setter
    def reg_timer_target1_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_timer_target1_ena_msb, self.__reg_timer_target1_ena_lsb, value)
class MACTIMER_TAR1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x124
        self.__reg_timer_target1_lsb = 0
        self.__reg_timer_target1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_timer_target1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_timer_target1_msb, self.__reg_timer_target1_lsb)
    @reg_timer_target1.setter
    def reg_timer_target1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_timer_target1_msb, self.__reg_timer_target1_lsb, value)
class MACTXRTS_INT_CNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x128
        self.__txrtsint_cnt_lsb = 0
        self.__txrtsint_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txrtsint_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__txrtsint_cnt_msb, self.__txrtsint_cnt_lsb)
    @txrtsint_cnt.setter
    def txrtsint_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__txrtsint_cnt_msb, self.__txrtsint_cnt_lsb, value)
class MACTXCTS_INT_CNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x12c
        self.__txctsint_cnt_lsb = 0
        self.__txctsint_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txctsint_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__txctsint_cnt_msb, self.__txctsint_cnt_lsb)
    @txctsint_cnt.setter
    def txctsint_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__txctsint_cnt_msb, self.__txctsint_cnt_lsb, value)
class MACTXRXACK_INT_CNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x130
        self.__txrxackint_cnt_lsb = 0
        self.__txrxackint_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txrxackint_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__txrxackint_cnt_msb, self.__txrxackint_cnt_lsb)
    @txrxackint_cnt.setter
    def txrxackint_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__txrxackint_cnt_msb, self.__txrxackint_cnt_lsb, value)
class MACTXRXCTS_INT_CNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x134
        self.__txrxctsint_cnt_lsb = 0
        self.__txrxctsint_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txrxctsint_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__txrxctsint_cnt_msb, self.__txrxctsint_cnt_lsb)
    @txrxctsint_cnt.setter
    def txrxctsint_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__txrxctsint_cnt_msb, self.__txrxctsint_cnt_lsb, value)
class MACRXTRIGGER_CNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x138
        self.__trigger_cnt_lsb = 0
        self.__trigger_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def trigger_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__trigger_cnt_msb, self.__trigger_cnt_lsb)
    @trigger_cnt.setter
    def trigger_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__trigger_cnt_msb, self.__trigger_cnt_lsb, value)
class MACRXTXHUNG_CNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x13c
        self.__hung_cnt_lsb = 0
        self.__hung_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def hung_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__hung_cnt_msb, self.__hung_cnt_lsb)
    @hung_cnt.setter
    def hung_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__hung_cnt_msb, self.__hung_cnt_lsb, value)
class MACRXTXPANIC_CNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x140
        self.__panic_cnt_lsb = 0
        self.__panic_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def panic_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__panic_cnt_msb, self.__panic_cnt_lsb)
    @panic_cnt.setter
    def panic_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__panic_cnt_msb, self.__panic_cnt_lsb, value)
class MACRSSI_STATIS(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x144
        self.__txop_rssi_valid_lsb = 24
        self.__txop_rssi_valid_msb = 24
        self.__txop_rssi_lsb = 16
        self.__txop_rssi_msb = 23
        self.__rxop_rssi_valid_lsb = 8
        self.__rxop_rssi_valid_msb = 8
        self.__rxop_rssi_lsb = 0
        self.__rxop_rssi_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txop_rssi_valid(self):
        return self.__MEM.rdm(self.__addr, self.__txop_rssi_valid_msb, self.__txop_rssi_valid_lsb)
    @txop_rssi_valid.setter
    def txop_rssi_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__txop_rssi_valid_msb, self.__txop_rssi_valid_lsb, value)

    @property
    def txop_rssi(self):
        return self.__MEM.rdm(self.__addr, self.__txop_rssi_msb, self.__txop_rssi_lsb)
    @txop_rssi.setter
    def txop_rssi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txop_rssi_msb, self.__txop_rssi_lsb, value)

    @property
    def rxop_rssi_valid(self):
        return self.__MEM.rdm(self.__addr, self.__rxop_rssi_valid_msb, self.__rxop_rssi_valid_lsb)
    @rxop_rssi_valid.setter
    def rxop_rssi_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxop_rssi_valid_msb, self.__rxop_rssi_valid_lsb, value)

    @property
    def rxop_rssi(self):
        return self.__MEM.rdm(self.__addr, self.__rxop_rssi_msb, self.__rxop_rssi_lsb)
    @rxop_rssi.setter
    def rxop_rssi(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxop_rssi_msb, self.__rxop_rssi_lsb, value)
class MACRXEND_CCACNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x148
        self.__reg_navcomp_lsb = 8
        self.__reg_navcomp_msb = 8
        self.__reg_max_ccacnt_lsb = 4
        self.__reg_max_ccacnt_msb = 7
        self.__rxend_ccacnt_lsb = 0
        self.__rxend_ccacnt_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_navcomp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_navcomp_msb, self.__reg_navcomp_lsb)
    @reg_navcomp.setter
    def reg_navcomp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_navcomp_msb, self.__reg_navcomp_lsb, value)

    @property
    def reg_max_ccacnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_max_ccacnt_msb, self.__reg_max_ccacnt_lsb)
    @reg_max_ccacnt.setter
    def reg_max_ccacnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_max_ccacnt_msb, self.__reg_max_ccacnt_lsb, value)

    @property
    def rxend_ccacnt(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_ccacnt_msb, self.__rxend_ccacnt_lsb)
    @rxend_ccacnt.setter
    def rxend_ccacnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_ccacnt_msb, self.__rxend_ccacnt_lsb, value)
class MACCHAN_STATIS(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x14c
        self.__reg_clear_statis_lsb = 31
        self.__reg_clear_statis_msb = 31
        self.__reg_statis_mode_lsb = 30
        self.__reg_statis_mode_msb = 30
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_clear_statis(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clear_statis_msb, self.__reg_clear_statis_lsb)
    @reg_clear_statis.setter
    def reg_clear_statis(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clear_statis_msb, self.__reg_clear_statis_lsb, value)

    @property
    def reg_statis_mode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_statis_mode_msb, self.__reg_statis_mode_lsb)
    @reg_statis_mode.setter
    def reg_statis_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_statis_mode_msb, self.__reg_statis_mode_lsb, value)
class MACEVT_STATIS0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x150
        self.__chan_act_cnt_lsb = 0
        self.__chan_act_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def chan_act_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__chan_act_cnt_msb, self.__chan_act_cnt_lsb)
    @chan_act_cnt.setter
    def chan_act_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__chan_act_cnt_msb, self.__chan_act_cnt_lsb, value)
class MACEVT_STATIS1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x154
        self.__chan_rxend_cnt_lsb = 0
        self.__chan_rxend_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def chan_rxend_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__chan_rxend_cnt_msb, self.__chan_rxend_cnt_lsb)
    @chan_rxend_cnt.setter
    def chan_rxend_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__chan_rxend_cnt_msb, self.__chan_rxend_cnt_lsb, value)
class MACEVT_STATIS2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x158
        self.__chan_rxstart_cnt_lsb = 0
        self.__chan_rxstart_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def chan_rxstart_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__chan_rxstart_cnt_msb, self.__chan_rxstart_cnt_lsb)
    @chan_rxstart_cnt.setter
    def chan_rxstart_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__chan_rxstart_cnt_msb, self.__chan_rxstart_cnt_lsb, value)
class MACEVT_STATIS3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x15c
        self.__chan_cca_cnt_lsb = 0
        self.__chan_cca_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def chan_cca_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__chan_cca_cnt_msb, self.__chan_cca_cnt_lsb)
    @chan_cca_cnt.setter
    def chan_cca_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__chan_cca_cnt_msb, self.__chan_cca_cnt_lsb, value)
class MACADCDUMP0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x160
        self.__reg_adcdump_ena_lsb = 31
        self.__reg_adcdump_ena_msb = 31
        self.__reg_adcdump_sel_lsb = 28
        self.__reg_adcdump_sel_msb = 30
        self.__reg_adcdump_case_lsb = 20
        self.__reg_adcdump_case_msb = 27
        self.__reg_adcdump_start_lsb = 19
        self.__reg_adcdump_start_msb = 19
        self.__adcdump_done_lsb = 18
        self.__adcdump_done_msb = 18
        self.__reg_dump_trig_mode_lsb = 17
        self.__reg_dump_trig_mode_msb = 17
        self.__reg_adcdump_rate_lsb = 15
        self.__reg_adcdump_rate_msb = 16
        self.__reg_adcdump_size_lsb = 0
        self.__reg_adcdump_size_msb = 14
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_adcdump_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcdump_ena_msb, self.__reg_adcdump_ena_lsb)
    @reg_adcdump_ena.setter
    def reg_adcdump_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcdump_ena_msb, self.__reg_adcdump_ena_lsb, value)

    @property
    def reg_adcdump_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcdump_sel_msb, self.__reg_adcdump_sel_lsb)
    @reg_adcdump_sel.setter
    def reg_adcdump_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcdump_sel_msb, self.__reg_adcdump_sel_lsb, value)

    @property
    def reg_adcdump_case(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcdump_case_msb, self.__reg_adcdump_case_lsb)
    @reg_adcdump_case.setter
    def reg_adcdump_case(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcdump_case_msb, self.__reg_adcdump_case_lsb, value)

    @property
    def reg_adcdump_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcdump_start_msb, self.__reg_adcdump_start_lsb)
    @reg_adcdump_start.setter
    def reg_adcdump_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcdump_start_msb, self.__reg_adcdump_start_lsb, value)

    @property
    def adcdump_done(self):
        return self.__MEM.rdm(self.__addr, self.__adcdump_done_msb, self.__adcdump_done_lsb)
    @adcdump_done.setter
    def adcdump_done(self, value):
        return self.__MEM.wrm(self.__addr, self.__adcdump_done_msb, self.__adcdump_done_lsb, value)

    @property
    def reg_dump_trig_mode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dump_trig_mode_msb, self.__reg_dump_trig_mode_lsb)
    @reg_dump_trig_mode.setter
    def reg_dump_trig_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dump_trig_mode_msb, self.__reg_dump_trig_mode_lsb, value)

    @property
    def reg_adcdump_rate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcdump_rate_msb, self.__reg_adcdump_rate_lsb)
    @reg_adcdump_rate.setter
    def reg_adcdump_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcdump_rate_msb, self.__reg_adcdump_rate_lsb, value)

    @property
    def reg_adcdump_size(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcdump_size_msb, self.__reg_adcdump_size_lsb)
    @reg_adcdump_size.setter
    def reg_adcdump_size(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcdump_size_msb, self.__reg_adcdump_size_lsb, value)
class MACADCDUMP1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x164
        self.__adcdump_wrap_lsb = 14
        self.__adcdump_wrap_msb = 14
        self.__adcdump_ptr_lsb = 0
        self.__adcdump_ptr_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def adcdump_wrap(self):
        return self.__MEM.rdm(self.__addr, self.__adcdump_wrap_msb, self.__adcdump_wrap_lsb)
    @adcdump_wrap.setter
    def adcdump_wrap(self, value):
        return self.__MEM.wrm(self.__addr, self.__adcdump_wrap_msb, self.__adcdump_wrap_lsb, value)

    @property
    def adcdump_ptr(self):
        return self.__MEM.rdm(self.__addr, self.__adcdump_ptr_msb, self.__adcdump_ptr_lsb)
    @adcdump_ptr.setter
    def adcdump_ptr(self, value):
        return self.__MEM.wrm(self.__addr, self.__adcdump_ptr_msb, self.__adcdump_ptr_lsb, value)
class MACTOADCDUMP0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x168
        self.__reg_toadcdump_ena_lsb = 31
        self.__reg_toadcdump_ena_msb = 31
        self.__reg_loop_cycle_lsb = 20
        self.__reg_loop_cycle_msb = 27
        self.__reg_toadcdump_loopen_lsb = 19
        self.__reg_toadcdump_loopen_msb = 19
        self.__toadcdump_done_lsb = 18
        self.__toadcdump_done_msb = 18
        self.__reg_toadcdump_rate_lsb = 15
        self.__reg_toadcdump_rate_msb = 15
        self.__reg_toadcdump_size_lsb = 0
        self.__reg_toadcdump_size_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_toadcdump_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_toadcdump_ena_msb, self.__reg_toadcdump_ena_lsb)
    @reg_toadcdump_ena.setter
    def reg_toadcdump_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_toadcdump_ena_msb, self.__reg_toadcdump_ena_lsb, value)

    @property
    def reg_loop_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__reg_loop_cycle_msb, self.__reg_loop_cycle_lsb)
    @reg_loop_cycle.setter
    def reg_loop_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_loop_cycle_msb, self.__reg_loop_cycle_lsb, value)

    @property
    def reg_toadcdump_loopen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_toadcdump_loopen_msb, self.__reg_toadcdump_loopen_lsb)
    @reg_toadcdump_loopen.setter
    def reg_toadcdump_loopen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_toadcdump_loopen_msb, self.__reg_toadcdump_loopen_lsb, value)

    @property
    def toadcdump_done(self):
        return self.__MEM.rdm(self.__addr, self.__toadcdump_done_msb, self.__toadcdump_done_lsb)
    @toadcdump_done.setter
    def toadcdump_done(self, value):
        return self.__MEM.wrm(self.__addr, self.__toadcdump_done_msb, self.__toadcdump_done_lsb, value)

    @property
    def reg_toadcdump_rate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_toadcdump_rate_msb, self.__reg_toadcdump_rate_lsb)
    @reg_toadcdump_rate.setter
    def reg_toadcdump_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_toadcdump_rate_msb, self.__reg_toadcdump_rate_lsb, value)

    @property
    def reg_toadcdump_size(self):
        return self.__MEM.rdm(self.__addr, self.__reg_toadcdump_size_msb, self.__reg_toadcdump_size_lsb)
    @reg_toadcdump_size.setter
    def reg_toadcdump_size(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_toadcdump_size_msb, self.__reg_toadcdump_size_lsb, value)
class MACTXQ_NOENABLE_US(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x16c
        self.__txq_noenable_us_lsb = 0
        self.__txq_noenable_us_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq_noenable_us(self):
        return self.__MEM.rdm(self.__addr, self.__txq_noenable_us_msb, self.__txq_noenable_us_lsb)
    @txq_noenable_us.setter
    def txq_noenable_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq_noenable_us_msb, self.__txq_noenable_us_lsb, value)
class MACBB_CCA_IND_US(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x170
        self.__bb_cca_ind_us_lsb = 0
        self.__bb_cca_ind_us_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def bb_cca_ind_us(self):
        return self.__MEM.rdm(self.__addr, self.__bb_cca_ind_us_msb, self.__bb_cca_ind_us_lsb)
    @bb_cca_ind_us.setter
    def bb_cca_ind_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__bb_cca_ind_us_msb, self.__bb_cca_ind_us_lsb, value)
class MACCCA_CNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x174
        self.__cca_cnt_lsb = 0
        self.__cca_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def cca_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__cca_cnt_msb, self.__cca_cnt_lsb)
    @cca_cnt.setter
    def cca_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__cca_cnt_msb, self.__cca_cnt_lsb, value)
class MACCCA_RXFRAM_CNT(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x178
        self.__cca_rxfram_cnt_lsb = 0
        self.__cca_rxfram_cnt_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def cca_rxfram_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__cca_rxfram_cnt_msb, self.__cca_rxfram_cnt_lsb)
    @cca_rxfram_cnt.setter
    def cca_rxfram_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__cca_rxfram_cnt_msb, self.__cca_rxfram_cnt_lsb, value)
class MACDIAG0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x17c
        self.__mac_edca_diag0_lsb = 0
        self.__mac_edca_diag0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def mac_edca_diag0(self):
        return self.__MEM.rdm(self.__addr, self.__mac_edca_diag0_msb, self.__mac_edca_diag0_lsb)
    @mac_edca_diag0.setter
    def mac_edca_diag0(self, value):
        return self.__MEM.wrm(self.__addr, self.__mac_edca_diag0_msb, self.__mac_edca_diag0_lsb, value)
class MACDIAG1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x180
        self.__mac_edca_diag1_lsb = 0
        self.__mac_edca_diag1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def mac_edca_diag1(self):
        return self.__MEM.rdm(self.__addr, self.__mac_edca_diag1_msb, self.__mac_edca_diag1_lsb)
    @mac_edca_diag1.setter
    def mac_edca_diag1(self, value):
        return self.__MEM.wrm(self.__addr, self.__mac_edca_diag1_msb, self.__mac_edca_diag1_lsb, value)
class MACDIAG2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x184
        self.__mac_edca_diag2_lsb = 0
        self.__mac_edca_diag2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def mac_edca_diag2(self):
        return self.__MEM.rdm(self.__addr, self.__mac_edca_diag2_msb, self.__mac_edca_diag2_lsb)
    @mac_edca_diag2.setter
    def mac_edca_diag2(self, value):
        return self.__MEM.wrm(self.__addr, self.__mac_edca_diag2_msb, self.__mac_edca_diag2_lsb, value)
class MACDIAG3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x188
        self.__mac_sch_diag0_lsb = 0
        self.__mac_sch_diag0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def mac_sch_diag0(self):
        return self.__MEM.rdm(self.__addr, self.__mac_sch_diag0_msb, self.__mac_sch_diag0_lsb)
    @mac_sch_diag0.setter
    def mac_sch_diag0(self, value):
        return self.__MEM.wrm(self.__addr, self.__mac_sch_diag0_msb, self.__mac_sch_diag0_lsb, value)
class MACDIAG_SEL(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x18c
        self.__reg_macdiag_sel_lsb = 0
        self.__reg_macdiag_sel_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macdiag_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macdiag_sel_msb, self.__reg_macdiag_sel_lsb)
    @reg_macdiag_sel.setter
    def reg_macdiag_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macdiag_sel_msb, self.__reg_macdiag_sel_lsb, value)
class MACTXDUMP(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x190
        self.__reg_mac_txdump_en_lsb = 31
        self.__reg_mac_txdump_en_msb = 31
        self.__reg_mac_txdump_start_addr_lsb = 16
        self.__reg_mac_txdump_start_addr_msb = 29
        self.__reg_mac_txdump_clr_lsb = 15
        self.__reg_mac_txdump_clr_msb = 15
        self.__reg_mac_txdump_size_lsb = 0
        self.__reg_mac_txdump_size_msb = 13
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_mac_txdump_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mac_txdump_en_msb, self.__reg_mac_txdump_en_lsb)
    @reg_mac_txdump_en.setter
    def reg_mac_txdump_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mac_txdump_en_msb, self.__reg_mac_txdump_en_lsb, value)

    @property
    def reg_mac_txdump_start_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mac_txdump_start_addr_msb, self.__reg_mac_txdump_start_addr_lsb)
    @reg_mac_txdump_start_addr.setter
    def reg_mac_txdump_start_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mac_txdump_start_addr_msb, self.__reg_mac_txdump_start_addr_lsb, value)

    @property
    def reg_mac_txdump_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mac_txdump_clr_msb, self.__reg_mac_txdump_clr_lsb)
    @reg_mac_txdump_clr.setter
    def reg_mac_txdump_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mac_txdump_clr_msb, self.__reg_mac_txdump_clr_lsb, value)

    @property
    def reg_mac_txdump_size(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mac_txdump_size_msb, self.__reg_mac_txdump_size_lsb)
    @reg_mac_txdump_size.setter
    def reg_mac_txdump_size(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mac_txdump_size_msb, self.__reg_mac_txdump_size_lsb, value)
class MACADCDUMP2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x194
        self.__reg_adcdump_agc_dbg_lsb = 24
        self.__reg_adcdump_agc_dbg_msb = 24
        self.__reg_adcdump_byte3_sel_lsb = 18
        self.__reg_adcdump_byte3_sel_msb = 23
        self.__reg_adcdump_byte2_sel_lsb = 12
        self.__reg_adcdump_byte2_sel_msb = 17
        self.__reg_adcdump_byte1_sel_lsb = 6
        self.__reg_adcdump_byte1_sel_msb = 11
        self.__reg_adcdump_byte0_sel_lsb = 0
        self.__reg_adcdump_byte0_sel_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_adcdump_agc_dbg(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcdump_agc_dbg_msb, self.__reg_adcdump_agc_dbg_lsb)
    @reg_adcdump_agc_dbg.setter
    def reg_adcdump_agc_dbg(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcdump_agc_dbg_msb, self.__reg_adcdump_agc_dbg_lsb, value)

    @property
    def reg_adcdump_byte3_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcdump_byte3_sel_msb, self.__reg_adcdump_byte3_sel_lsb)
    @reg_adcdump_byte3_sel.setter
    def reg_adcdump_byte3_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcdump_byte3_sel_msb, self.__reg_adcdump_byte3_sel_lsb, value)

    @property
    def reg_adcdump_byte2_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcdump_byte2_sel_msb, self.__reg_adcdump_byte2_sel_lsb)
    @reg_adcdump_byte2_sel.setter
    def reg_adcdump_byte2_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcdump_byte2_sel_msb, self.__reg_adcdump_byte2_sel_lsb, value)

    @property
    def reg_adcdump_byte1_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcdump_byte1_sel_msb, self.__reg_adcdump_byte1_sel_lsb)
    @reg_adcdump_byte1_sel.setter
    def reg_adcdump_byte1_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcdump_byte1_sel_msb, self.__reg_adcdump_byte1_sel_lsb, value)

    @property
    def reg_adcdump_byte0_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcdump_byte0_sel_msb, self.__reg_adcdump_byte0_sel_lsb)
    @reg_adcdump_byte0_sel.setter
    def reg_adcdump_byte0_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcdump_byte0_sel_msb, self.__reg_adcdump_byte0_sel_lsb, value)
class MACSIM_FINISH(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x198
        self.__reg_macsim_finish_lsb = 0
        self.__reg_macsim_finish_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macsim_finish(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macsim_finish_msb, self.__reg_macsim_finish_lsb)
    @reg_macsim_finish.setter
    def reg_macsim_finish(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macsim_finish_msb, self.__reg_macsim_finish_lsb, value)
class MACTXENA_TO(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x19c
        self.__reg_txena_to_ena_lsb = 31
        self.__reg_txena_to_ena_msb = 31
        self.__reg_txena_imr0_ena_lsb = 30
        self.__reg_txena_imr0_ena_msb = 30
        self.__reg_txena_to_timer_lsb = 0
        self.__reg_txena_to_timer_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txena_to_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txena_to_ena_msb, self.__reg_txena_to_ena_lsb)
    @reg_txena_to_ena.setter
    def reg_txena_to_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txena_to_ena_msb, self.__reg_txena_to_ena_lsb, value)

    @property
    def reg_txena_imr0_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txena_imr0_ena_msb, self.__reg_txena_imr0_ena_lsb)
    @reg_txena_imr0_ena.setter
    def reg_txena_imr0_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txena_imr0_ena_msb, self.__reg_txena_imr0_ena_lsb, value)

    @property
    def reg_txena_to_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txena_to_timer_msb, self.__reg_txena_to_timer_lsb)
    @reg_txena_to_timer.setter
    def reg_txena_to_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txena_to_timer_msb, self.__reg_txena_to_timer_lsb, value)
class MACRXSTART_TIME(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x1a0
        self.__rxstart_time_lsb = 0
        self.__rxstart_time_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxstart_time(self):
        return self.__MEM.rdm(self.__addr, self.__rxstart_time_msb, self.__rxstart_time_lsb)
    @rxstart_time.setter
    def rxstart_time(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxstart_time_msb, self.__rxstart_time_lsb, value)
class MACRXEND_TIME(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x1a4
        self.__rxend_time_lsb = 0
        self.__rxend_time_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxend_time(self):
        return self.__MEM.rdm(self.__addr, self.__rxend_time_msb, self.__rxend_time_lsb)
    @rxend_time.setter
    def rxend_time(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxend_time_msb, self.__rxend_time_lsb, value)
class MACTXSTART_TIME(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x1a8
        self.__txstart_time_lsb = 0
        self.__txstart_time_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txstart_time(self):
        return self.__MEM.rdm(self.__addr, self.__txstart_time_msb, self.__txstart_time_lsb)
    @txstart_time.setter
    def txstart_time(self, value):
        return self.__MEM.wrm(self.__addr, self.__txstart_time_msb, self.__txstart_time_lsb, value)
class MACTXEND_TIME(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x1ac
        self.__txend_time_lsb = 0
        self.__txend_time_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txend_time(self):
        return self.__MEM.rdm(self.__addr, self.__txend_time_msb, self.__txend_time_lsb)
    @txend_time.setter
    def txend_time(self, value):
        return self.__MEM.wrm(self.__addr, self.__txend_time_msb, self.__txend_time_lsb, value)
class MACSCHDATE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x3f8
        self.__reg_macsch_date_lsb = 0
        self.__reg_macsch_date_msb = 27
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macsch_date(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macsch_date_msb, self.__reg_macsch_date_lsb)
    @reg_macsch_date.setter
    def reg_macsch_date(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macsch_date_msb, self.__reg_macsch_date_lsb, value)
    @property
    def default_value(self):
        return 0x1810100
class MACID(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SCH_BASE + 0x3fc
        self.__mac_fpga_ver_lsb = 0
        self.__mac_fpga_ver_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def mac_fpga_ver(self):
        return self.__MEM.rdm(self.__addr, self.__mac_fpga_ver_msb, self.__mac_fpga_ver_lsb)
    @mac_fpga_ver.setter
    def mac_fpga_ver(self, value):
        return self.__MEM.wrm(self.__addr, self.__mac_fpga_ver_msb, self.__mac_fpga_ver_lsb, value)
