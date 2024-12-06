from hal.common import *
from hal.hwregister.hwi2c.CHIP724.addr_base import *
class SAR(object):
    def __init__(self, channel, chipv = "CHIP724"):
        self.chipv = chipv
        self.channel = channel
        self.__I2C = I2C(self.channel, self.chipv)
        self.__base = SAR_BASE
        self.__hostid = SAR_HOSTID
        self.__sar1_init_code_lsb_lsb = 0
        self.__sar1_init_code_lsb_msb = 7
        self.__sar1_init_code_lsb_addr = 0x0
        self.__sar1_init_code_msb_lsb = 0
        self.__sar1_init_code_msb_msb = 3
        self.__sar1_init_code_msb_addr = 0x1
        self.__sar1_redun_ptr_lsb = 4
        self.__sar1_redun_ptr_msb = 7
        self.__sar1_redun_ptr_addr = 0x1
        self.__sar1_smp_count_lsb = 0
        self.__sar1_smp_count_msb = 2
        self.__sar1_smp_count_addr = 0x2
        self.__sar1_dref_lsb = 4
        self.__sar1_dref_msb = 6
        self.__sar1_dref_addr = 0x2
        self.__sar2_init_code_lsb_lsb = 0
        self.__sar2_init_code_lsb_msb = 7
        self.__sar2_init_code_lsb_addr = 0x3
        self.__sar2_init_code_msb_lsb = 0
        self.__sar2_init_code_msb_msb = 3
        self.__sar2_init_code_msb_addr = 0x4
        self.__sar2_redun_ptr_lsb = 4
        self.__sar2_redun_ptr_msb = 7
        self.__sar2_redun_ptr_addr = 0x4
        self.__sar2_smp_count_lsb = 0
        self.__sar2_smp_count_msb = 2
        self.__sar2_smp_count_addr = 0x5
        self.__sar2_dref_lsb = 4
        self.__sar2_dref_msb = 6
        self.__sar2_dref_addr = 0x5
        self.__tsens_dac_lsb = 0
        self.__tsens_dac_msb = 3
        self.__tsens_dac_addr = 0x6
        self.__tsens_div_chop_lsb = 4
        self.__tsens_div_chop_msb = 5
        self.__tsens_div_chop_addr = 0x6
        self.__tsens_diz_lsb = 6
        self.__tsens_diz_msb = 6
        self.__tsens_diz_addr = 0x6
        self.__dtest_lsb = 0
        self.__dtest_msb = 1
        self.__dtest_addr = 0x7
        self.__ent_tsens_lsb = 2
        self.__ent_tsens_msb = 2
        self.__ent_tsens_addr = 0x7
        self.__ent_rtc_lsb = 3
        self.__ent_rtc_msb = 3
        self.__ent_rtc_addr = 0x7
        self.__sar1_encal_ref_lsb = 4
        self.__sar1_encal_ref_msb = 4
        self.__sar1_encal_ref_addr = 0x7
        self.__sar1_encal_gnd_lsb = 5
        self.__sar1_encal_gnd_msb = 5
        self.__sar1_encal_gnd_addr = 0x7
        self.__sar2_encal_ref_lsb = 6
        self.__sar2_encal_ref_msb = 6
        self.__sar2_encal_ref_addr = 0x7
        self.__sar2_encal_gnd_lsb = 7
        self.__sar2_encal_gnd_msb = 7
        self.__sar2_encal_gnd_addr = 0x7

    def reg_addr_rd(self,reg_addr):
        return self.__I2C.i2c_rd(self.__base , self.__hostid ,reg_addr)
    def reg_addr_wr(self,reg_addr,value):
        return self.__I2C.i2c_wr(self.__base , self.__hostid ,reg_addr,value)

    @property
    def sar1_init_code_lsb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sar1_init_code_lsb_addr, self.__sar1_init_code_lsb_msb, self.__sar1_init_code_lsb_lsb)
    @sar1_init_code_lsb.setter
    def sar1_init_code_lsb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sar1_init_code_lsb_addr, self.__sar1_init_code_lsb_msb, self.__sar1_init_code_lsb_lsb, value)

    @property
    def sar1_init_code_msb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sar1_init_code_msb_addr, self.__sar1_init_code_msb_msb, self.__sar1_init_code_msb_lsb)
    @sar1_init_code_msb.setter
    def sar1_init_code_msb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sar1_init_code_msb_addr, self.__sar1_init_code_msb_msb, self.__sar1_init_code_msb_lsb, value)

    @property
    def sar1_redun_ptr(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sar1_redun_ptr_addr, self.__sar1_redun_ptr_msb, self.__sar1_redun_ptr_lsb)
    @sar1_redun_ptr.setter
    def sar1_redun_ptr(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sar1_redun_ptr_addr, self.__sar1_redun_ptr_msb, self.__sar1_redun_ptr_lsb, value)

    @property
    def sar1_smp_count(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sar1_smp_count_addr, self.__sar1_smp_count_msb, self.__sar1_smp_count_lsb)
    @sar1_smp_count.setter
    def sar1_smp_count(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sar1_smp_count_addr, self.__sar1_smp_count_msb, self.__sar1_smp_count_lsb, value)

    @property
    def sar1_dref(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sar1_dref_addr, self.__sar1_dref_msb, self.__sar1_dref_lsb)
    @sar1_dref.setter
    def sar1_dref(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sar1_dref_addr, self.__sar1_dref_msb, self.__sar1_dref_lsb, value)

    @property
    def sar2_init_code_lsb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sar2_init_code_lsb_addr, self.__sar2_init_code_lsb_msb, self.__sar2_init_code_lsb_lsb)
    @sar2_init_code_lsb.setter
    def sar2_init_code_lsb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sar2_init_code_lsb_addr, self.__sar2_init_code_lsb_msb, self.__sar2_init_code_lsb_lsb, value)

    @property
    def sar2_init_code_msb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sar2_init_code_msb_addr, self.__sar2_init_code_msb_msb, self.__sar2_init_code_msb_lsb)
    @sar2_init_code_msb.setter
    def sar2_init_code_msb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sar2_init_code_msb_addr, self.__sar2_init_code_msb_msb, self.__sar2_init_code_msb_lsb, value)

    @property
    def sar2_redun_ptr(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sar2_redun_ptr_addr, self.__sar2_redun_ptr_msb, self.__sar2_redun_ptr_lsb)
    @sar2_redun_ptr.setter
    def sar2_redun_ptr(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sar2_redun_ptr_addr, self.__sar2_redun_ptr_msb, self.__sar2_redun_ptr_lsb, value)

    @property
    def sar2_smp_count(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sar2_smp_count_addr, self.__sar2_smp_count_msb, self.__sar2_smp_count_lsb)
    @sar2_smp_count.setter
    def sar2_smp_count(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sar2_smp_count_addr, self.__sar2_smp_count_msb, self.__sar2_smp_count_lsb, value)

    @property
    def sar2_dref(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sar2_dref_addr, self.__sar2_dref_msb, self.__sar2_dref_lsb)
    @sar2_dref.setter
    def sar2_dref(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sar2_dref_addr, self.__sar2_dref_msb, self.__sar2_dref_lsb, value)

    @property
    def tsens_dac(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tsens_dac_addr, self.__tsens_dac_msb, self.__tsens_dac_lsb)
    @tsens_dac.setter
    def tsens_dac(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tsens_dac_addr, self.__tsens_dac_msb, self.__tsens_dac_lsb, value)

    @property
    def tsens_div_chop(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tsens_div_chop_addr, self.__tsens_div_chop_msb, self.__tsens_div_chop_lsb)
    @tsens_div_chop.setter
    def tsens_div_chop(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tsens_div_chop_addr, self.__tsens_div_chop_msb, self.__tsens_div_chop_lsb, value)

    @property
    def tsens_diz(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tsens_diz_addr, self.__tsens_diz_msb, self.__tsens_diz_lsb)
    @tsens_diz.setter
    def tsens_diz(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tsens_diz_addr, self.__tsens_diz_msb, self.__tsens_diz_lsb, value)

    @property
    def dtest(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dtest_addr, self.__dtest_msb, self.__dtest_lsb)
    @dtest.setter
    def dtest(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dtest_addr, self.__dtest_msb, self.__dtest_lsb, value)

    @property
    def ent_tsens(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_tsens_addr, self.__ent_tsens_msb, self.__ent_tsens_lsb)
    @ent_tsens.setter
    def ent_tsens(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_tsens_addr, self.__ent_tsens_msb, self.__ent_tsens_lsb, value)

    @property
    def ent_rtc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_rtc_addr, self.__ent_rtc_msb, self.__ent_rtc_lsb)
    @ent_rtc.setter
    def ent_rtc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_rtc_addr, self.__ent_rtc_msb, self.__ent_rtc_lsb, value)

    @property
    def sar1_encal_ref(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sar1_encal_ref_addr, self.__sar1_encal_ref_msb, self.__sar1_encal_ref_lsb)
    @sar1_encal_ref.setter
    def sar1_encal_ref(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sar1_encal_ref_addr, self.__sar1_encal_ref_msb, self.__sar1_encal_ref_lsb, value)

    @property
    def sar1_encal_gnd(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sar1_encal_gnd_addr, self.__sar1_encal_gnd_msb, self.__sar1_encal_gnd_lsb)
    @sar1_encal_gnd.setter
    def sar1_encal_gnd(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sar1_encal_gnd_addr, self.__sar1_encal_gnd_msb, self.__sar1_encal_gnd_lsb, value)

    @property
    def sar2_encal_ref(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sar2_encal_ref_addr, self.__sar2_encal_ref_msb, self.__sar2_encal_ref_lsb)
    @sar2_encal_ref.setter
    def sar2_encal_ref(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sar2_encal_ref_addr, self.__sar2_encal_ref_msb, self.__sar2_encal_ref_lsb, value)

    @property
    def sar2_encal_gnd(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sar2_encal_gnd_addr, self.__sar2_encal_gnd_msb, self.__sar2_encal_gnd_lsb)
    @sar2_encal_gnd.setter
    def sar2_encal_gnd(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sar2_encal_gnd_addr, self.__sar2_encal_gnd_msb, self.__sar2_encal_gnd_lsb, value)
