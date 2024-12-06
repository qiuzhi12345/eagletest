from hal.common import *
from hal.hwregister.hwi2c.ESP32.addr_base import *
class SARADC(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__I2C = I2C(self.channel, self.chipv)
        self.__base = SARADC_BASE
        self.__hostid = SARADC_HOSTID
        self.__sar1_bit_width_lsb = 0
        self.__sar1_bit_width_msb = 1
        self.__sar1_bit_width_addr = 0x1
        self.__sar2_bit_width_lsb = 2
        self.__sar2_bit_width_msb = 3
        self.__sar2_bit_width_addr = 0x1
        self.__sar2_pwdet_cct_lsb = 4
        self.__sar2_pwdet_cct_msb = 6
        self.__sar2_pwdet_cct_addr = 0x1
        self.__sar_adc_msb_lsb = 0
        self.__sar_adc_msb_msb = 7
        self.__sar_adc_msb_addr = 0x4
        self.__sar_adc_lsb_lsb = 0
        self.__sar_adc_lsb_msb = 7
        self.__sar_adc_lsb_addr = 0x5

    def reg_addr_rd(self,reg_addr):
        return self.__I2C.i2c_rd(self.__base , self.__hostid ,reg_addr)
    def reg_addr_wr(self,reg_addr,value):
        return self.__I2C.i2c_wr(self.__base , self.__hostid ,reg_addr,value)

    @property
    def sar1_bit_width(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sar1_bit_width_addr, self.__sar1_bit_width_msb, self.__sar1_bit_width_lsb)
    @sar1_bit_width.setter
    def sar1_bit_width(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sar1_bit_width_addr, self.__sar1_bit_width_msb, self.__sar1_bit_width_lsb, value)

    @property
    def sar2_bit_width(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sar2_bit_width_addr, self.__sar2_bit_width_msb, self.__sar2_bit_width_lsb)
    @sar2_bit_width.setter
    def sar2_bit_width(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sar2_bit_width_addr, self.__sar2_bit_width_msb, self.__sar2_bit_width_lsb, value)

    @property
    def sar2_pwdet_cct(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sar2_pwdet_cct_addr, self.__sar2_pwdet_cct_msb, self.__sar2_pwdet_cct_lsb)
    @sar2_pwdet_cct.setter
    def sar2_pwdet_cct(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sar2_pwdet_cct_addr, self.__sar2_pwdet_cct_msb, self.__sar2_pwdet_cct_lsb, value)

    @property
    def sar_adc_msb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sar_adc_msb_addr, self.__sar_adc_msb_msb, self.__sar_adc_msb_lsb)
    @sar_adc_msb.setter
    def sar_adc_msb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sar_adc_msb_addr, self.__sar_adc_msb_msb, self.__sar_adc_msb_lsb, value)

    @property
    def sar_adc_lsb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sar_adc_lsb_addr, self.__sar_adc_lsb_msb, self.__sar_adc_lsb_lsb)
    @sar_adc_lsb.setter
    def sar_adc_lsb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sar_adc_lsb_addr, self.__sar_adc_lsb_msb, self.__sar_adc_lsb_lsb, value)
