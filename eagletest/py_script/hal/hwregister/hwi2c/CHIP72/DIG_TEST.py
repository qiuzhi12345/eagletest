from hal.common import *
from hal.hwregister.hwi2c.CHIP72.addr_base import *
class DIG_TEST(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__I2C = I2C(self.channel, self.chipv)
        self.__base = DIG_TEST_BASE
        self.__hostid = DIG_TEST_HOSTID
        self.__reg_tmp_lsb = 0
        self.__reg_tmp_msb = 7
        self.__reg_tmp_addr = 0x0

    def reg_addr_rd(self,reg_addr):
        return self.__I2C.i2c_rd(self.__base , self.__hostid ,reg_addr)
    def reg_addr_wr(self,reg_addr,value):
        return self.__I2C.i2c_wr(self.__base , self.__hostid ,reg_addr,value)

    @property
    def reg_tmp(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__reg_tmp_addr, self.__reg_tmp_msb, self.__reg_tmp_lsb)
    @reg_tmp.setter
    def reg_tmp(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__reg_tmp_addr, self.__reg_tmp_msb, self.__reg_tmp_lsb, value)
