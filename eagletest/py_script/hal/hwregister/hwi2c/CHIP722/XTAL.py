from hal.common import *
from hal.hwregister.hwi2c.CHIP722.addr_base import *
class XTAL(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__I2C = I2C(self.channel, self.chipv)
        self.__base = XTAL_BASE
        self.__hostid = XTAL_HOSTID
        self.__xpd_xtal_lsb = 0
        self.__xpd_xtal_msb = 0
        self.__xpd_xtal_addr = 0x0
        self.__xpd_xtal_buf_lsb = 1
        self.__xpd_xtal_buf_msb = 1
        self.__xpd_xtal_buf_addr = 0x0
        self.__ir_xtal_dac_ext_lsb = 2
        self.__ir_xtal_dac_ext_msb = 5
        self.__ir_xtal_dac_ext_addr = 0x0
        self.__ir_xtal_dac_enx_lsb = 6
        self.__ir_xtal_dac_enx_msb = 6
        self.__ir_xtal_dac_enx_addr = 0x0
        self.__ir_xtal_cal_stop_lsb = 7
        self.__ir_xtal_cal_stop_msb = 7
        self.__ir_xtal_cal_stop_addr = 0x0
        self.__xpd_rc_lsb = 5
        self.__xpd_rc_msb = 5
        self.__xpd_rc_addr = 0x1
        self.__enb_sck_xtal_lsb = 6
        self.__enb_sck_xtal_msb = 6
        self.__enb_sck_xtal_addr = 0x1
        self.__xtal_dphase_lsb = 7
        self.__xtal_dphase_msb = 7
        self.__xtal_dphase_addr = 0x1
        self.__or_xtal_dac_lsb = 0
        self.__or_xtal_dac_msb = 3
        self.__or_xtal_dac_addr = 0x2

    def reg_addr_rd(self,reg_addr):
        return self.__I2C.i2c_rd(self.__base , self.__hostid ,reg_addr)
    def reg_addr_wr(self,reg_addr,value):
        return self.__I2C.i2c_wr(self.__base , self.__hostid ,reg_addr,value)

    @property
    def xpd_xtal(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_xtal_addr, self.__xpd_xtal_msb, self.__xpd_xtal_lsb)
    @xpd_xtal.setter
    def xpd_xtal(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_xtal_addr, self.__xpd_xtal_msb, self.__xpd_xtal_lsb, value)

    @property
    def xpd_xtal_buf(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_xtal_buf_addr, self.__xpd_xtal_buf_msb, self.__xpd_xtal_buf_lsb)
    @xpd_xtal_buf.setter
    def xpd_xtal_buf(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_xtal_buf_addr, self.__xpd_xtal_buf_msb, self.__xpd_xtal_buf_lsb, value)

    @property
    def ir_xtal_dac_ext(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_xtal_dac_ext_addr, self.__ir_xtal_dac_ext_msb, self.__ir_xtal_dac_ext_lsb)
    @ir_xtal_dac_ext.setter
    def ir_xtal_dac_ext(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_xtal_dac_ext_addr, self.__ir_xtal_dac_ext_msb, self.__ir_xtal_dac_ext_lsb, value)

    @property
    def ir_xtal_dac_enx(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_xtal_dac_enx_addr, self.__ir_xtal_dac_enx_msb, self.__ir_xtal_dac_enx_lsb)
    @ir_xtal_dac_enx.setter
    def ir_xtal_dac_enx(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_xtal_dac_enx_addr, self.__ir_xtal_dac_enx_msb, self.__ir_xtal_dac_enx_lsb, value)

    @property
    def ir_xtal_cal_stop(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_xtal_cal_stop_addr, self.__ir_xtal_cal_stop_msb, self.__ir_xtal_cal_stop_lsb)
    @ir_xtal_cal_stop.setter
    def ir_xtal_cal_stop(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_xtal_cal_stop_addr, self.__ir_xtal_cal_stop_msb, self.__ir_xtal_cal_stop_lsb, value)

    @property
    def xpd_rc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_rc_addr, self.__xpd_rc_msb, self.__xpd_rc_lsb)
    @xpd_rc.setter
    def xpd_rc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_rc_addr, self.__xpd_rc_msb, self.__xpd_rc_lsb, value)

    @property
    def enb_sck_xtal(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__enb_sck_xtal_addr, self.__enb_sck_xtal_msb, self.__enb_sck_xtal_lsb)
    @enb_sck_xtal.setter
    def enb_sck_xtal(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__enb_sck_xtal_addr, self.__enb_sck_xtal_msb, self.__enb_sck_xtal_lsb, value)

    @property
    def xtal_dphase(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xtal_dphase_addr, self.__xtal_dphase_msb, self.__xtal_dphase_lsb)
    @xtal_dphase.setter
    def xtal_dphase(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xtal_dphase_addr, self.__xtal_dphase_msb, self.__xtal_dphase_lsb, value)

    @property
    def or_xtal_dac(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__or_xtal_dac_addr, self.__or_xtal_dac_msb, self.__or_xtal_dac_lsb)
    @or_xtal_dac.setter
    def or_xtal_dac(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__or_xtal_dac_addr, self.__or_xtal_dac_msb, self.__or_xtal_dac_lsb, value)
