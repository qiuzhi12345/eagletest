from hal.common import *
from hal.hwregister.hwreg.FPGA11ac.addr_base import *
class MAC_TX(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.MACRATE_SCCKTAB1 = MACRATE_SCCKTAB1(self.channel, self.chipv)
        self.MACRATE_SCCKTAB0 = MACRATE_SCCKTAB0(self.channel, self.chipv)
        self.MACRATE_CCKTAB1 = MACRATE_CCKTAB1(self.channel, self.chipv)
        self.MACRATE_CCKTAB0 = MACRATE_CCKTAB0(self.channel, self.chipv)
        self.MACRATE_OFDMTAB1 = MACRATE_OFDMTAB1(self.channel, self.chipv)
        self.MACRATE_OFDMTAB0 = MACRATE_OFDMTAB0(self.channel, self.chipv)
        self.MACRATE_11NTAB2 = MACRATE_11NTAB2(self.channel, self.chipv)
        self.MACRATE_11NTAB1 = MACRATE_11NTAB1(self.channel, self.chipv)
        self.MACRATE_11NTAB0 = MACRATE_11NTAB0(self.channel, self.chipv)
        self.MACRATE_11ACTAB1 = MACRATE_11ACTAB1(self.channel, self.chipv)
        self.MACRATE_11ACTAB0 = MACRATE_11ACTAB0(self.channel, self.chipv)
        self.MACTXRATE_LIM = MACTXRATE_LIM(self.channel, self.chipv)
        self.MACTXOPTIONS = MACTXOPTIONS(self.channel, self.chipv)
        self.MACTXSEQ5 = MACTXSEQ5(self.channel, self.chipv)
        self.MACTXSEQ4 = MACTXSEQ4(self.channel, self.chipv)
        self.MACTXSEQ3 = MACTXSEQ3(self.channel, self.chipv)
        self.MACTXSEQ2 = MACTXSEQ2(self.channel, self.chipv)
        self.MACTXSEQ1 = MACTXSEQ1(self.channel, self.chipv)
        self.MACTXSEQ0 = MACTXSEQ0(self.channel, self.chipv)
        self.MACDIAG8 = MACDIAG8(self.channel, self.chipv)
        self.MACDIAG9 = MACDIAG9(self.channel, self.chipv)
        self.MACDIAG10 = MACDIAG10(self.channel, self.chipv)
        self.MACDIAG12 = MACDIAG12(self.channel, self.chipv)
        self.MACDBG = MACDBG(self.channel, self.chipv)
        self.MACTX_TO = MACTX_TO(self.channel, self.chipv)
        self.MACTX_AHB = MACTX_AHB(self.channel, self.chipv)
        self.MACTXDATE = MACTXDATE(self.channel, self.chipv)
class MACRATE_SCCKTAB1(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0x0
        self.__reg_ratetab_lr7_lsb = 24
        self.__reg_ratetab_lr7_msb = 31
        self.__reg_ratetab_lr6_lsb = 16
        self.__reg_ratetab_lr6_msb = 23
        self.__reg_ratetab_lr5_lsb = 8
        self.__reg_ratetab_lr5_msb = 15
        self.__reg_ratetab_lr4_lsb = 0
        self.__reg_ratetab_lr4_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ratetab_lr7(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_lr7_msb, self.__reg_ratetab_lr7_lsb)
    @reg_ratetab_lr7.setter
    def reg_ratetab_lr7(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_lr7_msb, self.__reg_ratetab_lr7_lsb, value)

    @property
    def reg_ratetab_lr6(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_lr6_msb, self.__reg_ratetab_lr6_lsb)
    @reg_ratetab_lr6.setter
    def reg_ratetab_lr6(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_lr6_msb, self.__reg_ratetab_lr6_lsb, value)

    @property
    def reg_ratetab_lr5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_lr5_msb, self.__reg_ratetab_lr5_lsb)
    @reg_ratetab_lr5.setter
    def reg_ratetab_lr5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_lr5_msb, self.__reg_ratetab_lr5_lsb, value)

    @property
    def reg_ratetab_lr4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_lr4_msb, self.__reg_ratetab_lr4_lsb)
    @reg_ratetab_lr4.setter
    def reg_ratetab_lr4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_lr4_msb, self.__reg_ratetab_lr4_lsb, value)
class MACRATE_SCCKTAB0(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0x4
        self.__reg_ratetab_lr3_lsb = 24
        self.__reg_ratetab_lr3_msb = 31
        self.__reg_ratetab_lr2_lsb = 16
        self.__reg_ratetab_lr2_msb = 23
        self.__reg_ratetab_lr1_lsb = 8
        self.__reg_ratetab_lr1_msb = 15
        self.__reg_ratetab_lr0_lsb = 0
        self.__reg_ratetab_lr0_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ratetab_lr3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_lr3_msb, self.__reg_ratetab_lr3_lsb)
    @reg_ratetab_lr3.setter
    def reg_ratetab_lr3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_lr3_msb, self.__reg_ratetab_lr3_lsb, value)

    @property
    def reg_ratetab_lr2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_lr2_msb, self.__reg_ratetab_lr2_lsb)
    @reg_ratetab_lr2.setter
    def reg_ratetab_lr2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_lr2_msb, self.__reg_ratetab_lr2_lsb, value)

    @property
    def reg_ratetab_lr1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_lr1_msb, self.__reg_ratetab_lr1_lsb)
    @reg_ratetab_lr1.setter
    def reg_ratetab_lr1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_lr1_msb, self.__reg_ratetab_lr1_lsb, value)

    @property
    def reg_ratetab_lr0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_lr0_msb, self.__reg_ratetab_lr0_lsb)
    @reg_ratetab_lr0.setter
    def reg_ratetab_lr0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_lr0_msb, self.__reg_ratetab_lr0_lsb, value)
class MACRATE_CCKTAB1(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0x8
        self.__reg_ratetab_cck7_lsb = 24
        self.__reg_ratetab_cck7_msb = 31
        self.__reg_ratetab_cck6_lsb = 16
        self.__reg_ratetab_cck6_msb = 23
        self.__reg_ratetab_cck5_lsb = 8
        self.__reg_ratetab_cck5_msb = 15
        self.__reg_ratetab_cck4_lsb = 0
        self.__reg_ratetab_cck4_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ratetab_cck7(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_cck7_msb, self.__reg_ratetab_cck7_lsb)
    @reg_ratetab_cck7.setter
    def reg_ratetab_cck7(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_cck7_msb, self.__reg_ratetab_cck7_lsb, value)

    @property
    def reg_ratetab_cck6(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_cck6_msb, self.__reg_ratetab_cck6_lsb)
    @reg_ratetab_cck6.setter
    def reg_ratetab_cck6(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_cck6_msb, self.__reg_ratetab_cck6_lsb, value)

    @property
    def reg_ratetab_cck5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_cck5_msb, self.__reg_ratetab_cck5_lsb)
    @reg_ratetab_cck5.setter
    def reg_ratetab_cck5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_cck5_msb, self.__reg_ratetab_cck5_lsb, value)

    @property
    def reg_ratetab_cck4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_cck4_msb, self.__reg_ratetab_cck4_lsb)
    @reg_ratetab_cck4.setter
    def reg_ratetab_cck4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_cck4_msb, self.__reg_ratetab_cck4_lsb, value)
class MACRATE_CCKTAB0(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0xc
        self.__reg_ratetab_cck3_lsb = 24
        self.__reg_ratetab_cck3_msb = 31
        self.__reg_ratetab_cck2_lsb = 16
        self.__reg_ratetab_cck2_msb = 23
        self.__reg_ratetab_cck1_lsb = 8
        self.__reg_ratetab_cck1_msb = 15
        self.__reg_ratetab_cck0_lsb = 0
        self.__reg_ratetab_cck0_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ratetab_cck3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_cck3_msb, self.__reg_ratetab_cck3_lsb)
    @reg_ratetab_cck3.setter
    def reg_ratetab_cck3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_cck3_msb, self.__reg_ratetab_cck3_lsb, value)

    @property
    def reg_ratetab_cck2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_cck2_msb, self.__reg_ratetab_cck2_lsb)
    @reg_ratetab_cck2.setter
    def reg_ratetab_cck2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_cck2_msb, self.__reg_ratetab_cck2_lsb, value)

    @property
    def reg_ratetab_cck1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_cck1_msb, self.__reg_ratetab_cck1_lsb)
    @reg_ratetab_cck1.setter
    def reg_ratetab_cck1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_cck1_msb, self.__reg_ratetab_cck1_lsb, value)

    @property
    def reg_ratetab_cck0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_cck0_msb, self.__reg_ratetab_cck0_lsb)
    @reg_ratetab_cck0.setter
    def reg_ratetab_cck0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_cck0_msb, self.__reg_ratetab_cck0_lsb, value)
class MACRATE_OFDMTAB1(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0x10
        self.__reg_ratetab_ofdm7_lsb = 24
        self.__reg_ratetab_ofdm7_msb = 31
        self.__reg_ratetab_ofdm6_lsb = 16
        self.__reg_ratetab_ofdm6_msb = 23
        self.__reg_ratetab_ofdm5_lsb = 8
        self.__reg_ratetab_ofdm5_msb = 15
        self.__reg_ratetab_ofdm4_lsb = 0
        self.__reg_ratetab_ofdm4_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ratetab_ofdm7(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_ofdm7_msb, self.__reg_ratetab_ofdm7_lsb)
    @reg_ratetab_ofdm7.setter
    def reg_ratetab_ofdm7(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_ofdm7_msb, self.__reg_ratetab_ofdm7_lsb, value)

    @property
    def reg_ratetab_ofdm6(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_ofdm6_msb, self.__reg_ratetab_ofdm6_lsb)
    @reg_ratetab_ofdm6.setter
    def reg_ratetab_ofdm6(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_ofdm6_msb, self.__reg_ratetab_ofdm6_lsb, value)

    @property
    def reg_ratetab_ofdm5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_ofdm5_msb, self.__reg_ratetab_ofdm5_lsb)
    @reg_ratetab_ofdm5.setter
    def reg_ratetab_ofdm5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_ofdm5_msb, self.__reg_ratetab_ofdm5_lsb, value)

    @property
    def reg_ratetab_ofdm4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_ofdm4_msb, self.__reg_ratetab_ofdm4_lsb)
    @reg_ratetab_ofdm4.setter
    def reg_ratetab_ofdm4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_ofdm4_msb, self.__reg_ratetab_ofdm4_lsb, value)
class MACRATE_OFDMTAB0(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0x14
        self.__reg_ratetab_ofdm3_lsb = 24
        self.__reg_ratetab_ofdm3_msb = 31
        self.__reg_ratetab_ofdm2_lsb = 16
        self.__reg_ratetab_ofdm2_msb = 23
        self.__reg_ratetab_ofdm1_lsb = 8
        self.__reg_ratetab_ofdm1_msb = 15
        self.__reg_ratetab_ofdm0_lsb = 0
        self.__reg_ratetab_ofdm0_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ratetab_ofdm3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_ofdm3_msb, self.__reg_ratetab_ofdm3_lsb)
    @reg_ratetab_ofdm3.setter
    def reg_ratetab_ofdm3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_ofdm3_msb, self.__reg_ratetab_ofdm3_lsb, value)

    @property
    def reg_ratetab_ofdm2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_ofdm2_msb, self.__reg_ratetab_ofdm2_lsb)
    @reg_ratetab_ofdm2.setter
    def reg_ratetab_ofdm2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_ofdm2_msb, self.__reg_ratetab_ofdm2_lsb, value)

    @property
    def reg_ratetab_ofdm1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_ofdm1_msb, self.__reg_ratetab_ofdm1_lsb)
    @reg_ratetab_ofdm1.setter
    def reg_ratetab_ofdm1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_ofdm1_msb, self.__reg_ratetab_ofdm1_lsb, value)

    @property
    def reg_ratetab_ofdm0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_ofdm0_msb, self.__reg_ratetab_ofdm0_lsb)
    @reg_ratetab_ofdm0.setter
    def reg_ratetab_ofdm0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_ofdm0_msb, self.__reg_ratetab_ofdm0_lsb, value)
class MACRATE_11NTAB2(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0x18
        self.__reg_ratetab_11n32_lsb = 0
        self.__reg_ratetab_11n32_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ratetab_11n32(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_11n32_msb, self.__reg_ratetab_11n32_lsb)
    @reg_ratetab_11n32.setter
    def reg_ratetab_11n32(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_11n32_msb, self.__reg_ratetab_11n32_lsb, value)
class MACRATE_11NTAB1(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0x1c
        self.__reg_ratetab_11n7_lsb = 24
        self.__reg_ratetab_11n7_msb = 31
        self.__reg_ratetab_11n6_lsb = 16
        self.__reg_ratetab_11n6_msb = 23
        self.__reg_ratetab_11n5_lsb = 8
        self.__reg_ratetab_11n5_msb = 15
        self.__reg_ratetab_11n4_lsb = 0
        self.__reg_ratetab_11n4_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ratetab_11n7(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_11n7_msb, self.__reg_ratetab_11n7_lsb)
    @reg_ratetab_11n7.setter
    def reg_ratetab_11n7(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_11n7_msb, self.__reg_ratetab_11n7_lsb, value)

    @property
    def reg_ratetab_11n6(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_11n6_msb, self.__reg_ratetab_11n6_lsb)
    @reg_ratetab_11n6.setter
    def reg_ratetab_11n6(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_11n6_msb, self.__reg_ratetab_11n6_lsb, value)

    @property
    def reg_ratetab_11n5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_11n5_msb, self.__reg_ratetab_11n5_lsb)
    @reg_ratetab_11n5.setter
    def reg_ratetab_11n5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_11n5_msb, self.__reg_ratetab_11n5_lsb, value)

    @property
    def reg_ratetab_11n4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_11n4_msb, self.__reg_ratetab_11n4_lsb)
    @reg_ratetab_11n4.setter
    def reg_ratetab_11n4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_11n4_msb, self.__reg_ratetab_11n4_lsb, value)
class MACRATE_11NTAB0(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0x20
        self.__reg_ratetab_11n3_lsb = 24
        self.__reg_ratetab_11n3_msb = 31
        self.__reg_ratetab_11n2_lsb = 16
        self.__reg_ratetab_11n2_msb = 23
        self.__reg_ratetab_11n1_lsb = 8
        self.__reg_ratetab_11n1_msb = 15
        self.__reg_ratetab_11n0_lsb = 0
        self.__reg_ratetab_11n0_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ratetab_11n3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_11n3_msb, self.__reg_ratetab_11n3_lsb)
    @reg_ratetab_11n3.setter
    def reg_ratetab_11n3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_11n3_msb, self.__reg_ratetab_11n3_lsb, value)

    @property
    def reg_ratetab_11n2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_11n2_msb, self.__reg_ratetab_11n2_lsb)
    @reg_ratetab_11n2.setter
    def reg_ratetab_11n2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_11n2_msb, self.__reg_ratetab_11n2_lsb, value)

    @property
    def reg_ratetab_11n1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_11n1_msb, self.__reg_ratetab_11n1_lsb)
    @reg_ratetab_11n1.setter
    def reg_ratetab_11n1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_11n1_msb, self.__reg_ratetab_11n1_lsb, value)

    @property
    def reg_ratetab_11n0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_11n0_msb, self.__reg_ratetab_11n0_lsb)
    @reg_ratetab_11n0.setter
    def reg_ratetab_11n0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_11n0_msb, self.__reg_ratetab_11n0_lsb, value)
class MACRATE_11ACTAB1(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0x24
        self.__reg_ratetab_11ac7_lsb = 24
        self.__reg_ratetab_11ac7_msb = 31
        self.__reg_ratetab_11ac6_lsb = 16
        self.__reg_ratetab_11ac6_msb = 23
        self.__reg_ratetab_11ac5_lsb = 8
        self.__reg_ratetab_11ac5_msb = 15
        self.__reg_ratetab_11ac4_lsb = 0
        self.__reg_ratetab_11ac4_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ratetab_11ac7(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_11ac7_msb, self.__reg_ratetab_11ac7_lsb)
    @reg_ratetab_11ac7.setter
    def reg_ratetab_11ac7(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_11ac7_msb, self.__reg_ratetab_11ac7_lsb, value)

    @property
    def reg_ratetab_11ac6(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_11ac6_msb, self.__reg_ratetab_11ac6_lsb)
    @reg_ratetab_11ac6.setter
    def reg_ratetab_11ac6(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_11ac6_msb, self.__reg_ratetab_11ac6_lsb, value)

    @property
    def reg_ratetab_11ac5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_11ac5_msb, self.__reg_ratetab_11ac5_lsb)
    @reg_ratetab_11ac5.setter
    def reg_ratetab_11ac5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_11ac5_msb, self.__reg_ratetab_11ac5_lsb, value)

    @property
    def reg_ratetab_11ac4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_11ac4_msb, self.__reg_ratetab_11ac4_lsb)
    @reg_ratetab_11ac4.setter
    def reg_ratetab_11ac4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_11ac4_msb, self.__reg_ratetab_11ac4_lsb, value)
class MACRATE_11ACTAB0(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0x28
        self.__reg_ratetab_11ac3_lsb = 24
        self.__reg_ratetab_11ac3_msb = 31
        self.__reg_ratetab_11ac2_lsb = 16
        self.__reg_ratetab_11ac2_msb = 23
        self.__reg_ratetab_11ac1_lsb = 8
        self.__reg_ratetab_11ac1_msb = 15
        self.__reg_ratetab_11ac0_lsb = 0
        self.__reg_ratetab_11ac0_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ratetab_11ac3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_11ac3_msb, self.__reg_ratetab_11ac3_lsb)
    @reg_ratetab_11ac3.setter
    def reg_ratetab_11ac3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_11ac3_msb, self.__reg_ratetab_11ac3_lsb, value)

    @property
    def reg_ratetab_11ac2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_11ac2_msb, self.__reg_ratetab_11ac2_lsb)
    @reg_ratetab_11ac2.setter
    def reg_ratetab_11ac2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_11ac2_msb, self.__reg_ratetab_11ac2_lsb, value)

    @property
    def reg_ratetab_11ac1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_11ac1_msb, self.__reg_ratetab_11ac1_lsb)
    @reg_ratetab_11ac1.setter
    def reg_ratetab_11ac1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_11ac1_msb, self.__reg_ratetab_11ac1_lsb, value)

    @property
    def reg_ratetab_11ac0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ratetab_11ac0_msb, self.__reg_ratetab_11ac0_lsb)
    @reg_ratetab_11ac0.setter
    def reg_ratetab_11ac0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ratetab_11ac0_msb, self.__reg_ratetab_11ac0_lsb, value)
class MACTXRATE_LIM(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0x2c
        self.__reg_max11ac_lsb = 24
        self.__reg_max11ac_msb = 31
        self.__reg_maxlr_lsb = 20
        self.__reg_maxlr_msb = 23
        self.__reg_maxcck_lsb = 16
        self.__reg_maxcck_msb = 19
        self.__reg_maxofdm_lsb = 8
        self.__reg_maxofdm_msb = 11
        self.__reg_max11n_lsb = 0
        self.__reg_max11n_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_max11ac(self):
        return self.__MEM.rdm(self.__addr, self.__reg_max11ac_msb, self.__reg_max11ac_lsb)
    @reg_max11ac.setter
    def reg_max11ac(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_max11ac_msb, self.__reg_max11ac_lsb, value)

    @property
    def reg_maxlr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_maxlr_msb, self.__reg_maxlr_lsb)
    @reg_maxlr.setter
    def reg_maxlr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_maxlr_msb, self.__reg_maxlr_lsb, value)

    @property
    def reg_maxcck(self):
        return self.__MEM.rdm(self.__addr, self.__reg_maxcck_msb, self.__reg_maxcck_lsb)
    @reg_maxcck.setter
    def reg_maxcck(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_maxcck_msb, self.__reg_maxcck_lsb, value)

    @property
    def reg_maxofdm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_maxofdm_msb, self.__reg_maxofdm_lsb)
    @reg_maxofdm.setter
    def reg_maxofdm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_maxofdm_msb, self.__reg_maxofdm_lsb, value)

    @property
    def reg_max11n(self):
        return self.__MEM.rdm(self.__addr, self.__reg_max11n_msb, self.__reg_max11n_lsb)
    @reg_max11n.setter
    def reg_max11n(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_max11n_msb, self.__reg_max11n_lsb, value)
class MACTXOPTIONS(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0x30
        self.__reg_bbst_quit_ena_lsb = 31
        self.__reg_bbst_quit_ena_msb = 31
        self.__reg_bbstop_by_bbst_lsb = 30
        self.__reg_bbstop_by_bbst_msb = 30
        self.__reg_tx_dyn_nonht_bw_en_lsb = 4
        self.__reg_tx_dyn_nonht_bw_en_msb = 4
        self.__reg_txht80_force_offset_lsb = 2
        self.__reg_txht80_force_offset_msb = 3
        self.__reg_txht40_force_offset_lsb = 0
        self.__reg_txht40_force_offset_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_bbst_quit_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbst_quit_ena_msb, self.__reg_bbst_quit_ena_lsb)
    @reg_bbst_quit_ena.setter
    def reg_bbst_quit_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbst_quit_ena_msb, self.__reg_bbst_quit_ena_lsb, value)

    @property
    def reg_bbstop_by_bbst(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bbstop_by_bbst_msb, self.__reg_bbstop_by_bbst_lsb)
    @reg_bbstop_by_bbst.setter
    def reg_bbstop_by_bbst(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bbstop_by_bbst_msb, self.__reg_bbstop_by_bbst_lsb, value)

    @property
    def reg_tx_dyn_nonht_bw_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_dyn_nonht_bw_en_msb, self.__reg_tx_dyn_nonht_bw_en_lsb)
    @reg_tx_dyn_nonht_bw_en.setter
    def reg_tx_dyn_nonht_bw_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_dyn_nonht_bw_en_msb, self.__reg_tx_dyn_nonht_bw_en_lsb, value)

    @property
    def reg_txht80_force_offset(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txht80_force_offset_msb, self.__reg_txht80_force_offset_lsb)
    @reg_txht80_force_offset.setter
    def reg_txht80_force_offset(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txht80_force_offset_msb, self.__reg_txht80_force_offset_lsb, value)

    @property
    def reg_txht40_force_offset(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txht40_force_offset_msb, self.__reg_txht40_force_offset_lsb)
    @reg_txht40_force_offset.setter
    def reg_txht40_force_offset(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txht40_force_offset_msb, self.__reg_txht40_force_offset_lsb, value)
class MACTXSEQ5(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0x34
        self.__reg_txseq5_ena_lsb = 31
        self.__reg_txseq5_ena_msb = 31
        self.__txseq5_num_lsb = 12
        self.__txseq5_num_msb = 23
        self.__reg_txseq5_init_lsb = 0
        self.__reg_txseq5_init_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txseq5_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txseq5_ena_msb, self.__reg_txseq5_ena_lsb)
    @reg_txseq5_ena.setter
    def reg_txseq5_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txseq5_ena_msb, self.__reg_txseq5_ena_lsb, value)

    @property
    def txseq5_num(self):
        return self.__MEM.rdm(self.__addr, self.__txseq5_num_msb, self.__txseq5_num_lsb)
    @txseq5_num.setter
    def txseq5_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__txseq5_num_msb, self.__txseq5_num_lsb, value)

    @property
    def reg_txseq5_init(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txseq5_init_msb, self.__reg_txseq5_init_lsb)
    @reg_txseq5_init.setter
    def reg_txseq5_init(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txseq5_init_msb, self.__reg_txseq5_init_lsb, value)
class MACTXSEQ4(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0x38
        self.__reg_txseq4_ena_lsb = 31
        self.__reg_txseq4_ena_msb = 31
        self.__txseq4_num_lsb = 12
        self.__txseq4_num_msb = 23
        self.__reg_txseq4_init_lsb = 0
        self.__reg_txseq4_init_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txseq4_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txseq4_ena_msb, self.__reg_txseq4_ena_lsb)
    @reg_txseq4_ena.setter
    def reg_txseq4_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txseq4_ena_msb, self.__reg_txseq4_ena_lsb, value)

    @property
    def txseq4_num(self):
        return self.__MEM.rdm(self.__addr, self.__txseq4_num_msb, self.__txseq4_num_lsb)
    @txseq4_num.setter
    def txseq4_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__txseq4_num_msb, self.__txseq4_num_lsb, value)

    @property
    def reg_txseq4_init(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txseq4_init_msb, self.__reg_txseq4_init_lsb)
    @reg_txseq4_init.setter
    def reg_txseq4_init(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txseq4_init_msb, self.__reg_txseq4_init_lsb, value)
class MACTXSEQ3(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0x3c
        self.__reg_txseq3_ena_lsb = 31
        self.__reg_txseq3_ena_msb = 31
        self.__txseq3_num_lsb = 12
        self.__txseq3_num_msb = 23
        self.__reg_txseq3_init_lsb = 0
        self.__reg_txseq3_init_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txseq3_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txseq3_ena_msb, self.__reg_txseq3_ena_lsb)
    @reg_txseq3_ena.setter
    def reg_txseq3_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txseq3_ena_msb, self.__reg_txseq3_ena_lsb, value)

    @property
    def txseq3_num(self):
        return self.__MEM.rdm(self.__addr, self.__txseq3_num_msb, self.__txseq3_num_lsb)
    @txseq3_num.setter
    def txseq3_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__txseq3_num_msb, self.__txseq3_num_lsb, value)

    @property
    def reg_txseq3_init(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txseq3_init_msb, self.__reg_txseq3_init_lsb)
    @reg_txseq3_init.setter
    def reg_txseq3_init(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txseq3_init_msb, self.__reg_txseq3_init_lsb, value)
class MACTXSEQ2(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0x40
        self.__reg_txseq2_ena_lsb = 31
        self.__reg_txseq2_ena_msb = 31
        self.__txseq2_num_lsb = 12
        self.__txseq2_num_msb = 23
        self.__reg_txseq2_init_lsb = 0
        self.__reg_txseq2_init_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txseq2_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txseq2_ena_msb, self.__reg_txseq2_ena_lsb)
    @reg_txseq2_ena.setter
    def reg_txseq2_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txseq2_ena_msb, self.__reg_txseq2_ena_lsb, value)

    @property
    def txseq2_num(self):
        return self.__MEM.rdm(self.__addr, self.__txseq2_num_msb, self.__txseq2_num_lsb)
    @txseq2_num.setter
    def txseq2_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__txseq2_num_msb, self.__txseq2_num_lsb, value)

    @property
    def reg_txseq2_init(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txseq2_init_msb, self.__reg_txseq2_init_lsb)
    @reg_txseq2_init.setter
    def reg_txseq2_init(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txseq2_init_msb, self.__reg_txseq2_init_lsb, value)
class MACTXSEQ1(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0x44
        self.__reg_txseq1_ena_lsb = 31
        self.__reg_txseq1_ena_msb = 31
        self.__txseq1_num_lsb = 12
        self.__txseq1_num_msb = 23
        self.__reg_txseq1_init_lsb = 0
        self.__reg_txseq1_init_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txseq1_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txseq1_ena_msb, self.__reg_txseq1_ena_lsb)
    @reg_txseq1_ena.setter
    def reg_txseq1_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txseq1_ena_msb, self.__reg_txseq1_ena_lsb, value)

    @property
    def txseq1_num(self):
        return self.__MEM.rdm(self.__addr, self.__txseq1_num_msb, self.__txseq1_num_lsb)
    @txseq1_num.setter
    def txseq1_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__txseq1_num_msb, self.__txseq1_num_lsb, value)

    @property
    def reg_txseq1_init(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txseq1_init_msb, self.__reg_txseq1_init_lsb)
    @reg_txseq1_init.setter
    def reg_txseq1_init(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txseq1_init_msb, self.__reg_txseq1_init_lsb, value)
class MACTXSEQ0(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0x48
        self.__reg_txseq0_ena_lsb = 31
        self.__reg_txseq0_ena_msb = 31
        self.__txseq0_num_lsb = 12
        self.__txseq0_num_msb = 23
        self.__reg_txseq0_init_lsb = 0
        self.__reg_txseq0_init_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txseq0_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txseq0_ena_msb, self.__reg_txseq0_ena_lsb)
    @reg_txseq0_ena.setter
    def reg_txseq0_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txseq0_ena_msb, self.__reg_txseq0_ena_lsb, value)

    @property
    def txseq0_num(self):
        return self.__MEM.rdm(self.__addr, self.__txseq0_num_msb, self.__txseq0_num_lsb)
    @txseq0_num.setter
    def txseq0_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__txseq0_num_msb, self.__txseq0_num_lsb, value)

    @property
    def reg_txseq0_init(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txseq0_init_msb, self.__reg_txseq0_init_lsb)
    @reg_txseq0_init.setter
    def reg_txseq0_init(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txseq0_init_msb, self.__reg_txseq0_init_lsb, value)
class MACDIAG8(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0x4c
        self.__mac_tx_diag0_lsb = 0
        self.__mac_tx_diag0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def mac_tx_diag0(self):
        return self.__MEM.rdm(self.__addr, self.__mac_tx_diag0_msb, self.__mac_tx_diag0_lsb)
    @mac_tx_diag0.setter
    def mac_tx_diag0(self, value):
        return self.__MEM.wrm(self.__addr, self.__mac_tx_diag0_msb, self.__mac_tx_diag0_lsb, value)
class MACDIAG9(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0x50
        self.__mac_tx_diag1_lsb = 0
        self.__mac_tx_diag1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def mac_tx_diag1(self):
        return self.__MEM.rdm(self.__addr, self.__mac_tx_diag1_msb, self.__mac_tx_diag1_lsb)
    @mac_tx_diag1.setter
    def mac_tx_diag1(self, value):
        return self.__MEM.wrm(self.__addr, self.__mac_tx_diag1_msb, self.__mac_tx_diag1_lsb, value)
class MACDIAG10(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0x54
        self.__mac_tx_diag2_lsb = 0
        self.__mac_tx_diag2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def mac_tx_diag2(self):
        return self.__MEM.rdm(self.__addr, self.__mac_tx_diag2_msb, self.__mac_tx_diag2_lsb)
    @mac_tx_diag2.setter
    def mac_tx_diag2(self, value):
        return self.__MEM.wrm(self.__addr, self.__mac_tx_diag2_msb, self.__mac_tx_diag2_lsb, value)
class MACDIAG12(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0x58
        self.__mac_tx_diag3_lsb = 0
        self.__mac_tx_diag3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def mac_tx_diag3(self):
        return self.__MEM.rdm(self.__addr, self.__mac_tx_diag3_msb, self.__mac_tx_diag3_lsb)
    @mac_tx_diag3.setter
    def mac_tx_diag3(self, value):
        return self.__MEM.wrm(self.__addr, self.__mac_tx_diag3_msb, self.__mac_tx_diag3_lsb, value)
class MACDBG(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0x5c
        self.__reg_tobb_fifo_clkb_en_lsb = 3
        self.__reg_tobb_fifo_clkb_en_msb = 3
        self.__reg_tobb_fifo_clka_en_lsb = 2
        self.__reg_tobb_fifo_clka_en_msb = 2
        self.__reg_txclk_en_lsb = 1
        self.__reg_txclk_en_msb = 1
        self.__reg_always_tx_lsb = 0
        self.__reg_always_tx_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tobb_fifo_clkb_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tobb_fifo_clkb_en_msb, self.__reg_tobb_fifo_clkb_en_lsb)
    @reg_tobb_fifo_clkb_en.setter
    def reg_tobb_fifo_clkb_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tobb_fifo_clkb_en_msb, self.__reg_tobb_fifo_clkb_en_lsb, value)

    @property
    def reg_tobb_fifo_clka_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tobb_fifo_clka_en_msb, self.__reg_tobb_fifo_clka_en_lsb)
    @reg_tobb_fifo_clka_en.setter
    def reg_tobb_fifo_clka_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tobb_fifo_clka_en_msb, self.__reg_tobb_fifo_clka_en_lsb, value)

    @property
    def reg_txclk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txclk_en_msb, self.__reg_txclk_en_lsb)
    @reg_txclk_en.setter
    def reg_txclk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txclk_en_msb, self.__reg_txclk_en_lsb, value)

    @property
    def reg_always_tx(self):
        return self.__MEM.rdm(self.__addr, self.__reg_always_tx_msb, self.__reg_always_tx_lsb)
    @reg_always_tx.setter
    def reg_always_tx(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_always_tx_msb, self.__reg_always_tx_lsb, value)
class MACTX_TO(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0x60
        self.__reg_txto_ena_lsb = 31
        self.__reg_txto_ena_msb = 31
        self.__reg_txto_timer_lsb = 0
        self.__reg_txto_timer_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txto_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txto_ena_msb, self.__reg_txto_ena_lsb)
    @reg_txto_ena.setter
    def reg_txto_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txto_ena_msb, self.__reg_txto_ena_lsb, value)

    @property
    def reg_txto_timer(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txto_timer_msb, self.__reg_txto_timer_lsb)
    @reg_txto_timer.setter
    def reg_txto_timer(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txto_timer_msb, self.__reg_txto_timer_lsb, value)
class MACTX_AHB(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0x64
        self.__reg_txburst_max_len_lsb = 0
        self.__reg_txburst_max_len_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txburst_max_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txburst_max_len_msb, self.__reg_txburst_max_len_lsb)
    @reg_txburst_max_len.setter
    def reg_txburst_max_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txburst_max_len_msb, self.__reg_txburst_max_len_lsb, value)
class MACTXDATE(object):
    def __init__(self, channel, chipv = "FPGA11ac"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TX_BASE + 0x3f8
        self.__reg_mactx_date_lsb = 0
        self.__reg_mactx_date_msb = 27
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_mactx_date(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mactx_date_msb, self.__reg_mactx_date_lsb)
    @reg_mactx_date.setter
    def reg_mactx_date(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mactx_date_msb, self.__reg_mactx_date_lsb, value)
    @property
    def default_value(self):
        return 0x1906170
