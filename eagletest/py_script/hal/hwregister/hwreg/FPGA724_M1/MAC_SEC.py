from hal.common import *
from hal.hwregister.hwreg.FPGA724_M1.addr_base import *
class MAC_SEC(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.MACSEC_CONF0 = MACSEC_CONF0(self.channel, self.chipv)
        self.MACSEC_CONF1 = MACSEC_CONF1(self.channel, self.chipv)
        self.MACSEC_CONF10 = MACSEC_CONF10(self.channel, self.chipv)
        self.MACSEC_CONF11 = MACSEC_CONF11(self.channel, self.chipv)
        self.MACSEC_CONF2 = MACSEC_CONF2(self.channel, self.chipv)
        self.MACSEC_CONF3 = MACSEC_CONF3(self.channel, self.chipv)
        self.MACSEC_CONF4 = MACSEC_CONF4(self.channel, self.chipv)
        self.MACSEC_CONF5 = MACSEC_CONF5(self.channel, self.chipv)
        self.MACSEC_CONF6 = MACSEC_CONF6(self.channel, self.chipv)
        self.MACSEC_CONF7 = MACSEC_CONF7(self.channel, self.chipv)
        self.MACSEC_CONF8 = MACSEC_CONF8(self.channel, self.chipv)
        self.MACSEC_CONF9 = MACSEC_CONF9(self.channel, self.chipv)
        self.MACSEC_STATE0 = MACSEC_STATE0(self.channel, self.chipv)
        self.MACSEC_STATE1 = MACSEC_STATE1(self.channel, self.chipv)
        self.MACSEC_STATE2 = MACSEC_STATE2(self.channel, self.chipv)
        self.MACSEC_STATE3 = MACSEC_STATE3(self.channel, self.chipv)
        self.MACSEC_CLK_CONF = MACSEC_CLK_CONF(self.channel, self.chipv)
        self.MACSECDATE = MACSECDATE(self.channel, self.chipv)
class MACSEC_CONF0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SEC_BASE + 0x0
        self.__reg_sec_conf0_lsb = 0
        self.__reg_sec_conf0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sec_conf0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sec_conf0_msb, self.__reg_sec_conf0_lsb)
    @reg_sec_conf0.setter
    def reg_sec_conf0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sec_conf0_msb, self.__reg_sec_conf0_lsb, value)
class MACSEC_CONF1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SEC_BASE + 0x4
        self.__reg_sec_conf1_lsb = 0
        self.__reg_sec_conf1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sec_conf1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sec_conf1_msb, self.__reg_sec_conf1_lsb)
    @reg_sec_conf1.setter
    def reg_sec_conf1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sec_conf1_msb, self.__reg_sec_conf1_lsb, value)
class MACSEC_CONF10(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SEC_BASE + 0x8
        self.__reg_sec_conf10_lsb = 0
        self.__reg_sec_conf10_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sec_conf10(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sec_conf10_msb, self.__reg_sec_conf10_lsb)
    @reg_sec_conf10.setter
    def reg_sec_conf10(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sec_conf10_msb, self.__reg_sec_conf10_lsb, value)
class MACSEC_CONF11(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SEC_BASE + 0xc
        self.__reg_sec_conf11_lsb = 0
        self.__reg_sec_conf11_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sec_conf11(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sec_conf11_msb, self.__reg_sec_conf11_lsb)
    @reg_sec_conf11.setter
    def reg_sec_conf11(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sec_conf11_msb, self.__reg_sec_conf11_lsb, value)
class MACSEC_CONF2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SEC_BASE + 0x10
        self.__reg_sec_conf2_lsb = 0
        self.__reg_sec_conf2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sec_conf2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sec_conf2_msb, self.__reg_sec_conf2_lsb)
    @reg_sec_conf2.setter
    def reg_sec_conf2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sec_conf2_msb, self.__reg_sec_conf2_lsb, value)
class MACSEC_CONF3(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SEC_BASE + 0x14
        self.__reg_sec_conf3_lsb = 0
        self.__reg_sec_conf3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sec_conf3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sec_conf3_msb, self.__reg_sec_conf3_lsb)
    @reg_sec_conf3.setter
    def reg_sec_conf3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sec_conf3_msb, self.__reg_sec_conf3_lsb, value)
class MACSEC_CONF4(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SEC_BASE + 0x18
        self.__reg_sec_conf4_lsb = 0
        self.__reg_sec_conf4_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sec_conf4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sec_conf4_msb, self.__reg_sec_conf4_lsb)
    @reg_sec_conf4.setter
    def reg_sec_conf4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sec_conf4_msb, self.__reg_sec_conf4_lsb, value)
class MACSEC_CONF5(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SEC_BASE + 0x1c
        self.__reg_sec_conf5_lsb = 0
        self.__reg_sec_conf5_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sec_conf5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sec_conf5_msb, self.__reg_sec_conf5_lsb)
    @reg_sec_conf5.setter
    def reg_sec_conf5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sec_conf5_msb, self.__reg_sec_conf5_lsb, value)
class MACSEC_CONF6(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SEC_BASE + 0x20
        self.__reg_sec_conf6_lsb = 0
        self.__reg_sec_conf6_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sec_conf6(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sec_conf6_msb, self.__reg_sec_conf6_lsb)
    @reg_sec_conf6.setter
    def reg_sec_conf6(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sec_conf6_msb, self.__reg_sec_conf6_lsb, value)
class MACSEC_CONF7(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SEC_BASE + 0x24
        self.__reg_sec_conf7_lsb = 0
        self.__reg_sec_conf7_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sec_conf7(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sec_conf7_msb, self.__reg_sec_conf7_lsb)
    @reg_sec_conf7.setter
    def reg_sec_conf7(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sec_conf7_msb, self.__reg_sec_conf7_lsb, value)
class MACSEC_CONF8(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SEC_BASE + 0x28
        self.__reg_sec_conf8_lsb = 0
        self.__reg_sec_conf8_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sec_conf8(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sec_conf8_msb, self.__reg_sec_conf8_lsb)
    @reg_sec_conf8.setter
    def reg_sec_conf8(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sec_conf8_msb, self.__reg_sec_conf8_lsb, value)
class MACSEC_CONF9(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SEC_BASE + 0x2c
        self.__reg_sec_conf9_lsb = 0
        self.__reg_sec_conf9_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sec_conf9(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sec_conf9_msb, self.__reg_sec_conf9_lsb)
    @reg_sec_conf9.setter
    def reg_sec_conf9(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sec_conf9_msb, self.__reg_sec_conf9_lsb, value)
class MACSEC_STATE0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SEC_BASE + 0x30
        self.__sec_state0_lsb = 0
        self.__sec_state0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sec_state0(self):
        return self.__MEM.rdm(self.__addr, self.__sec_state0_msb, self.__sec_state0_lsb)
    @sec_state0.setter
    def sec_state0(self, value):
        return self.__MEM.wrm(self.__addr, self.__sec_state0_msb, self.__sec_state0_lsb, value)
class MACSEC_STATE1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SEC_BASE + 0x34
        self.__sec_state1_lsb = 0
        self.__sec_state1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sec_state1(self):
        return self.__MEM.rdm(self.__addr, self.__sec_state1_msb, self.__sec_state1_lsb)
    @sec_state1.setter
    def sec_state1(self, value):
        return self.__MEM.wrm(self.__addr, self.__sec_state1_msb, self.__sec_state1_lsb, value)
class MACSEC_STATE2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SEC_BASE + 0x38
        self.__sec_state2_lsb = 0
        self.__sec_state2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sec_state2(self):
        return self.__MEM.rdm(self.__addr, self.__sec_state2_msb, self.__sec_state2_lsb)
    @sec_state2.setter
    def sec_state2(self, value):
        return self.__MEM.wrm(self.__addr, self.__sec_state2_msb, self.__sec_state2_lsb, value)
class MACSEC_STATE3(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SEC_BASE + 0x3c
        self.__sec_state3_lsb = 0
        self.__sec_state3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sec_state3(self):
        return self.__MEM.rdm(self.__addr, self.__sec_state3_msb, self.__sec_state3_lsb)
    @sec_state3.setter
    def sec_state3(self, value):
        return self.__MEM.wrm(self.__addr, self.__sec_state3_msb, self.__sec_state3_lsb, value)
class MACSEC_CLK_CONF(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SEC_BASE + 0x40
        self.__reg_kmem_clk_en_lsb = 6
        self.__reg_kmem_clk_en_msb = 6
        self.__reg_secclk_en_lsb = 5
        self.__reg_secclk_en_msb = 5
        self.__reg_sectx_clk_en_lsb = 4
        self.__reg_sectx_clk_en_msb = 4
        self.__reg_secrx_clk_en_lsb = 3
        self.__reg_secrx_clk_en_msb = 3
        self.__reg_tkip_clk_en_lsb = 2
        self.__reg_tkip_clk_en_msb = 2
        self.__reg_wapi_clk_en_lsb = 1
        self.__reg_wapi_clk_en_msb = 1
        self.__reg_ccmp_clk_en_lsb = 0
        self.__reg_ccmp_clk_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_kmem_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_kmem_clk_en_msb, self.__reg_kmem_clk_en_lsb)
    @reg_kmem_clk_en.setter
    def reg_kmem_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_kmem_clk_en_msb, self.__reg_kmem_clk_en_lsb, value)

    @property
    def reg_secclk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_secclk_en_msb, self.__reg_secclk_en_lsb)
    @reg_secclk_en.setter
    def reg_secclk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_secclk_en_msb, self.__reg_secclk_en_lsb, value)

    @property
    def reg_sectx_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sectx_clk_en_msb, self.__reg_sectx_clk_en_lsb)
    @reg_sectx_clk_en.setter
    def reg_sectx_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sectx_clk_en_msb, self.__reg_sectx_clk_en_lsb, value)

    @property
    def reg_secrx_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_secrx_clk_en_msb, self.__reg_secrx_clk_en_lsb)
    @reg_secrx_clk_en.setter
    def reg_secrx_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_secrx_clk_en_msb, self.__reg_secrx_clk_en_lsb, value)

    @property
    def reg_tkip_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tkip_clk_en_msb, self.__reg_tkip_clk_en_lsb)
    @reg_tkip_clk_en.setter
    def reg_tkip_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tkip_clk_en_msb, self.__reg_tkip_clk_en_lsb, value)

    @property
    def reg_wapi_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wapi_clk_en_msb, self.__reg_wapi_clk_en_lsb)
    @reg_wapi_clk_en.setter
    def reg_wapi_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wapi_clk_en_msb, self.__reg_wapi_clk_en_lsb, value)

    @property
    def reg_ccmp_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ccmp_clk_en_msb, self.__reg_ccmp_clk_en_lsb)
    @reg_ccmp_clk_en.setter
    def reg_ccmp_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ccmp_clk_en_msb, self.__reg_ccmp_clk_en_lsb, value)
class MACSECDATE(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_SEC_BASE + 0x3f8
        self.__reg_macsec_date_lsb = 0
        self.__reg_macsec_date_msb = 27
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_macsec_date(self):
        return self.__MEM.rdm(self.__addr, self.__reg_macsec_date_msb, self.__reg_macsec_date_lsb)
    @reg_macsec_date.setter
    def reg_macsec_date(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_macsec_date_msb, self.__reg_macsec_date_lsb, value)
    @property
    def default_value(self):
        return 0x1505051
