from hal.common import *
from hal.hwregister.hwi2c.ESP8266.addr_base import *
class SARADC(object):
    def __init__(self, channel, chipv = "ESP8266"):
        self.chipv = chipv
        self.channel = channel
        self.__I2C = I2C(self.channel, self.chipv)
        self.__base = SARADC_BASE
        self.__hostid = SARADC_HOSTID
        self.__xpd_tsens_lsb = 0
        self.__xpd_tsens_msb = 0
        self.__xpd_tsens_addr = 0x0
        self.__en_lna_lsb = 1
        self.__en_lna_msb = 1
        self.__en_lna_addr = 0x0
        self.__en_pa_lsb = 2
        self.__en_pa_msb = 2
        self.__en_pa_addr = 0x0
        self.__en_vco_lsb = 3
        self.__en_vco_msb = 3
        self.__en_vco_addr = 0x0
        self.__xpd_sar_lsb = 4
        self.__xpd_sar_msb = 4
        self.__xpd_sar_addr = 0x0
        self.__en_test_lsb = 5
        self.__en_test_msb = 5
        self.__en_test_addr = 0x0
        self.__dump_out_lsb = 6
        self.__dump_out_msb = 6
        self.__dump_out_addr = 0x0
        self.__en_sar_ck_lsb = 7
        self.__en_sar_ck_msb = 7
        self.__en_sar_ck_addr = 0x0
        self.__bit_width_lsb = 0
        self.__bit_width_msb = 1
        self.__bit_width_addr = 0x1
        self.__pwdet_cct_lsb = 2
        self.__pwdet_cct_msb = 4
        self.__pwdet_cct_addr = 0x1
        self.__sar_adc_rstb_lsb = 5
        self.__sar_adc_rstb_msb = 5
        self.__sar_adc_rstb_addr = 0x1
        self.__sar_adc_start_lsb = 6
        self.__sar_adc_start_msb = 6
        self.__sar_adc_start_addr = 0x1
        self.__sar_adc_stop_lsb = 7
        self.__sar_adc_stop_msb = 7
        self.__sar_adc_stop_addr = 0x1
        self.__temp_lsb = 0
        self.__temp_msb = 7
        self.__temp_addr = 0x2
        self.__temp_rdy_lsb = 0
        self.__temp_rdy_msb = 0
        self.__temp_rdy_addr = 0x3
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
    def xpd_tsens(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_tsens_addr, self.__xpd_tsens_msb, self.__xpd_tsens_lsb)
    @xpd_tsens.setter
    def xpd_tsens(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_tsens_addr, self.__xpd_tsens_msb, self.__xpd_tsens_lsb, value)

    @property
    def en_lna(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__en_lna_addr, self.__en_lna_msb, self.__en_lna_lsb)
    @en_lna.setter
    def en_lna(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__en_lna_addr, self.__en_lna_msb, self.__en_lna_lsb, value)

    @property
    def en_pa(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__en_pa_addr, self.__en_pa_msb, self.__en_pa_lsb)
    @en_pa.setter
    def en_pa(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__en_pa_addr, self.__en_pa_msb, self.__en_pa_lsb, value)

    @property
    def en_vco(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__en_vco_addr, self.__en_vco_msb, self.__en_vco_lsb)
    @en_vco.setter
    def en_vco(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__en_vco_addr, self.__en_vco_msb, self.__en_vco_lsb, value)

    @property
    def xpd_sar(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_sar_addr, self.__xpd_sar_msb, self.__xpd_sar_lsb)
    @xpd_sar.setter
    def xpd_sar(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_sar_addr, self.__xpd_sar_msb, self.__xpd_sar_lsb, value)

    @property
    def en_test(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__en_test_addr, self.__en_test_msb, self.__en_test_lsb)
    @en_test.setter
    def en_test(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__en_test_addr, self.__en_test_msb, self.__en_test_lsb, value)

    @property
    def dump_out(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dump_out_addr, self.__dump_out_msb, self.__dump_out_lsb)
    @dump_out.setter
    def dump_out(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dump_out_addr, self.__dump_out_msb, self.__dump_out_lsb, value)

    @property
    def en_sar_ck(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__en_sar_ck_addr, self.__en_sar_ck_msb, self.__en_sar_ck_lsb)
    @en_sar_ck.setter
    def en_sar_ck(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__en_sar_ck_addr, self.__en_sar_ck_msb, self.__en_sar_ck_lsb, value)

    @property
    def bit_width(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__bit_width_addr, self.__bit_width_msb, self.__bit_width_lsb)
    @bit_width.setter
    def bit_width(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__bit_width_addr, self.__bit_width_msb, self.__bit_width_lsb, value)

    @property
    def pwdet_cct(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__pwdet_cct_addr, self.__pwdet_cct_msb, self.__pwdet_cct_lsb)
    @pwdet_cct.setter
    def pwdet_cct(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__pwdet_cct_addr, self.__pwdet_cct_msb, self.__pwdet_cct_lsb, value)

    @property
    def sar_adc_rstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sar_adc_rstb_addr, self.__sar_adc_rstb_msb, self.__sar_adc_rstb_lsb)
    @sar_adc_rstb.setter
    def sar_adc_rstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sar_adc_rstb_addr, self.__sar_adc_rstb_msb, self.__sar_adc_rstb_lsb, value)

    @property
    def sar_adc_start(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sar_adc_start_addr, self.__sar_adc_start_msb, self.__sar_adc_start_lsb)
    @sar_adc_start.setter
    def sar_adc_start(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sar_adc_start_addr, self.__sar_adc_start_msb, self.__sar_adc_start_lsb, value)

    @property
    def sar_adc_stop(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sar_adc_stop_addr, self.__sar_adc_stop_msb, self.__sar_adc_stop_lsb)
    @sar_adc_stop.setter
    def sar_adc_stop(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sar_adc_stop_addr, self.__sar_adc_stop_msb, self.__sar_adc_stop_lsb, value)

    @property
    def temp(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__temp_addr, self.__temp_msb, self.__temp_lsb)
    @temp.setter
    def temp(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__temp_addr, self.__temp_msb, self.__temp_lsb, value)

    @property
    def temp_rdy(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__temp_rdy_addr, self.__temp_rdy_msb, self.__temp_rdy_lsb)
    @temp_rdy.setter
    def temp_rdy(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__temp_rdy_addr, self.__temp_rdy_msb, self.__temp_rdy_lsb, value)

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
