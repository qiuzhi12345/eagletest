from hal.common import *
from hal.hwregister.hwi2c.CHIP724.addr_base import *
class RFPLL_SDM(object):
    def __init__(self, channel, chipv = "CHIP724"):
        self.chipv = chipv
        self.channel = channel
        self.__I2C = I2C(self.channel, self.chipv)
        self.__base = RFPLL_SDM_BASE
        self.__hostid = RFPLL_SDM_HOSTID
        self.__xpd_sdm_lsb = 0
        self.__xpd_sdm_msb = 0
        self.__xpd_sdm_addr = 0x0
        self.__xpd_chgp_lsb = 1
        self.__xpd_chgp_msb = 1
        self.__xpd_chgp_addr = 0x0
        self.__xpd_test_lsb = 2
        self.__xpd_test_msb = 2
        self.__xpd_test_addr = 0x0
        self.__sdm_stop_lsb = 3
        self.__sdm_stop_msb = 3
        self.__sdm_stop_addr = 0x0
        self.__sdm_rstb_lsb = 4
        self.__sdm_rstb_msb = 4
        self.__sdm_rstb_addr = 0x0
        self.__sdm_dither_lsb = 5
        self.__sdm_dither_msb = 5
        self.__sdm_dither_addr = 0x0
        self.__bst_e2c_lsb = 6
        self.__bst_e2c_msb = 6
        self.__bst_e2c_addr = 0x0
        self.__xpd_lf_lsb = 0
        self.__xpd_lf_msb = 0
        self.__xpd_lf_addr = 0x1
        self.__xpd_div_lsb = 1
        self.__xpd_div_msb = 1
        self.__xpd_div_addr = 0x1
        self.__bst_div_lsb = 2
        self.__bst_div_msb = 2
        self.__bst_div_addr = 0x1
        self.__enb_open_lf_lsb = 3
        self.__enb_open_lf_msb = 3
        self.__enb_open_lf_addr = 0x1
        self.__lf_dlfcal_lsb = 4
        self.__lf_dlfcal_msb = 5
        self.__lf_dlfcal_addr = 0x1
        self.__lf_dhfcal_lsb = 6
        self.__lf_dhfcal_msb = 7
        self.__lf_dhfcal_addr = 0x1
        self.__dsdm_24_lsb = 0
        self.__dsdm_24_msb = 0
        self.__dsdm_24_addr = 0x2
        self.__dsdm_23_16_lsb = 0
        self.__dsdm_23_16_msb = 7
        self.__dsdm_23_16_addr = 0x3
        self.__dsdm_15_8_lsb = 0
        self.__dsdm_15_8_msb = 7
        self.__dsdm_15_8_addr = 0x4
        self.__dsdm_7_0_lsb = 0
        self.__dsdm_7_0_msb = 7
        self.__dsdm_7_0_addr = 0x5

    def reg_addr_rd(self,reg_addr):
        return self.__I2C.i2c_rd(self.__base , self.__hostid ,reg_addr)
    def reg_addr_wr(self,reg_addr,value):
        return self.__I2C.i2c_wr(self.__base , self.__hostid ,reg_addr,value)

    @property
    def xpd_sdm(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_sdm_addr, self.__xpd_sdm_msb, self.__xpd_sdm_lsb)
    @xpd_sdm.setter
    def xpd_sdm(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_sdm_addr, self.__xpd_sdm_msb, self.__xpd_sdm_lsb, value)

    @property
    def xpd_chgp(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_chgp_addr, self.__xpd_chgp_msb, self.__xpd_chgp_lsb)
    @xpd_chgp.setter
    def xpd_chgp(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_chgp_addr, self.__xpd_chgp_msb, self.__xpd_chgp_lsb, value)

    @property
    def xpd_test(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_test_addr, self.__xpd_test_msb, self.__xpd_test_lsb)
    @xpd_test.setter
    def xpd_test(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_test_addr, self.__xpd_test_msb, self.__xpd_test_lsb, value)

    @property
    def sdm_stop(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sdm_stop_addr, self.__sdm_stop_msb, self.__sdm_stop_lsb)
    @sdm_stop.setter
    def sdm_stop(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sdm_stop_addr, self.__sdm_stop_msb, self.__sdm_stop_lsb, value)

    @property
    def sdm_rstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sdm_rstb_addr, self.__sdm_rstb_msb, self.__sdm_rstb_lsb)
    @sdm_rstb.setter
    def sdm_rstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sdm_rstb_addr, self.__sdm_rstb_msb, self.__sdm_rstb_lsb, value)

    @property
    def sdm_dither(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sdm_dither_addr, self.__sdm_dither_msb, self.__sdm_dither_lsb)
    @sdm_dither.setter
    def sdm_dither(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sdm_dither_addr, self.__sdm_dither_msb, self.__sdm_dither_lsb, value)

    @property
    def bst_e2c(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__bst_e2c_addr, self.__bst_e2c_msb, self.__bst_e2c_lsb)
    @bst_e2c.setter
    def bst_e2c(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__bst_e2c_addr, self.__bst_e2c_msb, self.__bst_e2c_lsb, value)

    @property
    def xpd_lf(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_lf_addr, self.__xpd_lf_msb, self.__xpd_lf_lsb)
    @xpd_lf.setter
    def xpd_lf(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_lf_addr, self.__xpd_lf_msb, self.__xpd_lf_lsb, value)

    @property
    def xpd_div(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_div_addr, self.__xpd_div_msb, self.__xpd_div_lsb)
    @xpd_div.setter
    def xpd_div(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_div_addr, self.__xpd_div_msb, self.__xpd_div_lsb, value)

    @property
    def bst_div(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__bst_div_addr, self.__bst_div_msb, self.__bst_div_lsb)
    @bst_div.setter
    def bst_div(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__bst_div_addr, self.__bst_div_msb, self.__bst_div_lsb, value)

    @property
    def enb_open_lf(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__enb_open_lf_addr, self.__enb_open_lf_msb, self.__enb_open_lf_lsb)
    @enb_open_lf.setter
    def enb_open_lf(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__enb_open_lf_addr, self.__enb_open_lf_msb, self.__enb_open_lf_lsb, value)

    @property
    def lf_dlfcal(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__lf_dlfcal_addr, self.__lf_dlfcal_msb, self.__lf_dlfcal_lsb)
    @lf_dlfcal.setter
    def lf_dlfcal(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__lf_dlfcal_addr, self.__lf_dlfcal_msb, self.__lf_dlfcal_lsb, value)

    @property
    def lf_dhfcal(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__lf_dhfcal_addr, self.__lf_dhfcal_msb, self.__lf_dhfcal_lsb)
    @lf_dhfcal.setter
    def lf_dhfcal(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__lf_dhfcal_addr, self.__lf_dhfcal_msb, self.__lf_dhfcal_lsb, value)

    @property
    def dsdm_24(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dsdm_24_addr, self.__dsdm_24_msb, self.__dsdm_24_lsb)
    @dsdm_24.setter
    def dsdm_24(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dsdm_24_addr, self.__dsdm_24_msb, self.__dsdm_24_lsb, value)

    @property
    def dsdm_23_16(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dsdm_23_16_addr, self.__dsdm_23_16_msb, self.__dsdm_23_16_lsb)
    @dsdm_23_16.setter
    def dsdm_23_16(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dsdm_23_16_addr, self.__dsdm_23_16_msb, self.__dsdm_23_16_lsb, value)

    @property
    def dsdm_15_8(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dsdm_15_8_addr, self.__dsdm_15_8_msb, self.__dsdm_15_8_lsb)
    @dsdm_15_8.setter
    def dsdm_15_8(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dsdm_15_8_addr, self.__dsdm_15_8_msb, self.__dsdm_15_8_lsb, value)

    @property
    def dsdm_7_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dsdm_7_0_addr, self.__dsdm_7_0_msb, self.__dsdm_7_0_lsb)
    @dsdm_7_0.setter
    def dsdm_7_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dsdm_7_0_addr, self.__dsdm_7_0_msb, self.__dsdm_7_0_lsb, value)
