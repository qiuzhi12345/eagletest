from hal.common import *
from hal.hwregister.hwi2c.ESP8266.addr_base import *
class BBTX(object):
    def __init__(self, channel, chipv = "ESP8266"):
        self.chipv = chipv
        self.channel = channel
        self.__I2C = I2C(self.channel, self.chipv)
        self.__base = BBTX_BASE
        self.__hostid = BBTX_HOSTID
        self.__dac_ck_ph_inv_lsb = 0
        self.__dac_ck_ph_inv_msb = 0
        self.__dac_ck_ph_inv_addr = 0x0
        self.__filter_bstb_lsb = 1
        self.__filter_bstb_msb = 2
        self.__filter_bstb_addr = 0x0
        self.__filter_dinput_ld_lsb = 3
        self.__filter_dinput_ld_msb = 4
        self.__filter_dinput_ld_addr = 0x0
        self.__filter_dedge_lsb = 5
        self.__filter_dedge_msb = 6
        self.__filter_dedge_addr = 0x0
        self.__filter_dcap_lsb = 0
        self.__filter_dcap_msb = 5
        self.__filter_dcap_addr = 0x1
        self.__filter_dlbw_lsb = 6
        self.__filter_dlbw_msb = 6
        self.__filter_dlbw_addr = 0x1
        self.__dtest_lsb = 0
        self.__dtest_msb = 1
        self.__dtest_addr = 0x2
        self.__ent_filter_i_lsb = 2
        self.__ent_filter_i_msb = 2
        self.__ent_filter_i_addr = 0x2
        self.__ent_filter_q_lsb = 3
        self.__ent_filter_q_msb = 3
        self.__ent_filter_q_addr = 0x2
        self.__ent_filter_bias_i_lsb = 4
        self.__ent_filter_bias_i_msb = 4
        self.__ent_filter_bias_i_addr = 0x2
        self.__ent_filter_bias_q_lsb = 5
        self.__ent_filter_bias_q_msb = 5
        self.__ent_filter_bias_q_addr = 0x2
        self.__dsw_bias_lsb = 0
        self.__dsw_bias_msb = 1
        self.__dsw_bias_addr = 0x3
        self.__dv2i_bias_lsb = 2
        self.__dv2i_bias_msb = 3
        self.__dv2i_bias_addr = 0x3

    def reg_addr_rd(self,reg_addr):
        return self.__I2C.i2c_rd(self.__base , self.__hostid ,reg_addr)
    def reg_addr_wr(self,reg_addr,value):
        return self.__I2C.i2c_wr(self.__base , self.__hostid ,reg_addr,value)

    @property
    def dac_ck_ph_inv(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dac_ck_ph_inv_addr, self.__dac_ck_ph_inv_msb, self.__dac_ck_ph_inv_lsb)
    @dac_ck_ph_inv.setter
    def dac_ck_ph_inv(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dac_ck_ph_inv_addr, self.__dac_ck_ph_inv_msb, self.__dac_ck_ph_inv_lsb, value)

    @property
    def filter_bstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bstb_addr, self.__filter_bstb_msb, self.__filter_bstb_lsb)
    @filter_bstb.setter
    def filter_bstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bstb_addr, self.__filter_bstb_msb, self.__filter_bstb_lsb, value)

    @property
    def filter_dinput_ld(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_dinput_ld_addr, self.__filter_dinput_ld_msb, self.__filter_dinput_ld_lsb)
    @filter_dinput_ld.setter
    def filter_dinput_ld(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_dinput_ld_addr, self.__filter_dinput_ld_msb, self.__filter_dinput_ld_lsb, value)

    @property
    def filter_dedge(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_dedge_addr, self.__filter_dedge_msb, self.__filter_dedge_lsb)
    @filter_dedge.setter
    def filter_dedge(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_dedge_addr, self.__filter_dedge_msb, self.__filter_dedge_lsb, value)

    @property
    def filter_dcap(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_dcap_addr, self.__filter_dcap_msb, self.__filter_dcap_lsb)
    @filter_dcap.setter
    def filter_dcap(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_dcap_addr, self.__filter_dcap_msb, self.__filter_dcap_lsb, value)

    @property
    def filter_dlbw(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_dlbw_addr, self.__filter_dlbw_msb, self.__filter_dlbw_lsb)
    @filter_dlbw.setter
    def filter_dlbw(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_dlbw_addr, self.__filter_dlbw_msb, self.__filter_dlbw_lsb, value)

    @property
    def dtest(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dtest_addr, self.__dtest_msb, self.__dtest_lsb)
    @dtest.setter
    def dtest(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dtest_addr, self.__dtest_msb, self.__dtest_lsb, value)

    @property
    def ent_filter_i(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_filter_i_addr, self.__ent_filter_i_msb, self.__ent_filter_i_lsb)
    @ent_filter_i.setter
    def ent_filter_i(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_filter_i_addr, self.__ent_filter_i_msb, self.__ent_filter_i_lsb, value)

    @property
    def ent_filter_q(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_filter_q_addr, self.__ent_filter_q_msb, self.__ent_filter_q_lsb)
    @ent_filter_q.setter
    def ent_filter_q(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_filter_q_addr, self.__ent_filter_q_msb, self.__ent_filter_q_lsb, value)

    @property
    def ent_filter_bias_i(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_filter_bias_i_addr, self.__ent_filter_bias_i_msb, self.__ent_filter_bias_i_lsb)
    @ent_filter_bias_i.setter
    def ent_filter_bias_i(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_filter_bias_i_addr, self.__ent_filter_bias_i_msb, self.__ent_filter_bias_i_lsb, value)

    @property
    def ent_filter_bias_q(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_filter_bias_q_addr, self.__ent_filter_bias_q_msb, self.__ent_filter_bias_q_lsb)
    @ent_filter_bias_q.setter
    def ent_filter_bias_q(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_filter_bias_q_addr, self.__ent_filter_bias_q_msb, self.__ent_filter_bias_q_lsb, value)

    @property
    def dsw_bias(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dsw_bias_addr, self.__dsw_bias_msb, self.__dsw_bias_lsb)
    @dsw_bias.setter
    def dsw_bias(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dsw_bias_addr, self.__dsw_bias_msb, self.__dsw_bias_lsb, value)

    @property
    def dv2i_bias(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dv2i_bias_addr, self.__dv2i_bias_msb, self.__dv2i_bias_lsb)
    @dv2i_bias.setter
    def dv2i_bias(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dv2i_bias_addr, self.__dv2i_bias_msb, self.__dv2i_bias_lsb, value)
