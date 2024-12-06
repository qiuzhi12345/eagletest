from hal.common import *
from hal.hwregister.hwi2c.ESP8266.addr_base import *
class BIAS(object):
    def __init__(self, channel, chipv = "ESP8266"):
        self.chipv = chipv
        self.channel = channel
        self.__I2C = I2C(self.channel, self.chipv)
        self.__base = BIAS_BASE
        self.__hostid = BIAS_HOSTID
        self.__cp1p6_dreg_lsb = 0
        self.__cp1p6_dreg_msb = 1
        self.__cp1p6_dreg_addr = 0x0
        self.__cp1p2_dreg_lsb = 2
        self.__cp1p2_dreg_msb = 3
        self.__cp1p2_dreg_addr = 0x0
        self.__rc_dvref_lsb = 4
        self.__rc_dvref_msb = 5
        self.__rc_dvref_addr = 0x0
        self.__rc_enx_lsb = 6
        self.__rc_enx_msb = 6
        self.__rc_enx_addr = 0x0
        self.__ent_bg_lsb = 0
        self.__ent_bg_msb = 0
        self.__ent_bg_addr = 0x1
        self.__ent_consti_lsb = 1
        self.__ent_consti_msb = 1
        self.__ent_consti_addr = 0x1
        self.__rc_dcap_ext_lsb = 2
        self.__rc_dcap_ext_msb = 7
        self.__rc_dcap_ext_addr = 0x1
        self.__ent_cpreg_1p6_lsb = 0
        self.__ent_cpreg_1p6_msb = 0
        self.__ent_cpreg_1p6_addr = 0x2
        self.__ent_cgm_lsb = 1
        self.__ent_cgm_msb = 1
        self.__ent_cgm_addr = 0x2
        self.__cgm_bias_lsb = 2
        self.__cgm_bias_msb = 3
        self.__cgm_bias_addr = 0x2
        self.__cp1p1_pvt_reg_lsb = 4
        self.__cp1p1_pvt_reg_msb = 5
        self.__cp1p1_pvt_reg_addr = 0x2
        self.__dref_igm_lsb = 6
        self.__dref_igm_msb = 6
        self.__dref_igm_addr = 0x2
        self.__rc_cap_ext_lsb = 0
        self.__rc_cap_ext_msb = 5
        self.__rc_cap_ext_addr = 0x3
        self.__rc_start_lsb = 6
        self.__rc_start_msb = 6
        self.__rc_start_addr = 0x3
        self.__xpd_rc_lsb = 0
        self.__xpd_rc_msb = 0
        self.__xpd_rc_addr = 0x4
        self.__xpd_bg_lsb = 1
        self.__xpd_bg_msb = 1
        self.__xpd_bg_addr = 0x4
        self.__xpd_icx_lsb = 2
        self.__xpd_icx_msb = 2
        self.__xpd_icx_addr = 0x4
        self.__rc_rstb_lsb = 3
        self.__rc_rstb_msb = 3
        self.__rc_rstb_addr = 0x4
        self.__rc_div_lsb = 4
        self.__rc_div_msb = 7
        self.__rc_div_addr = 0x4
        self.__rc_cap_lsb = 0
        self.__rc_cap_msb = 5
        self.__rc_cap_addr = 0x5
        self.__dc_ud_lsb = 6
        self.__dc_ud_msb = 6
        self.__dc_ud_addr = 0x5
        self.__rc_chg_count_lsb = 0
        self.__rc_chg_count_msb = 4
        self.__rc_chg_count_addr = 0x6
        self.__xpd_cpreg_1p6_lsb = 0
        self.__xpd_cpreg_1p6_msb = 0
        self.__xpd_cpreg_1p6_addr = 0x7
        self.__xpd_cpreg_1p2_lsb = 1
        self.__xpd_cpreg_1p2_msb = 1
        self.__xpd_cpreg_1p2_addr = 0x7
        self.__xpd_cgm_lsb = 2
        self.__xpd_cgm_msb = 2
        self.__xpd_cgm_addr = 0x7
        self.__dtest_lsb = 3
        self.__dtest_msb = 4
        self.__dtest_addr = 0x7
        self.__sclock_dcap_lsb = 0
        self.__sclock_dcap_msb = 4
        self.__sclock_dcap_addr = 0x8
        self.__enb_sck_core_lsb = 5
        self.__enb_sck_core_msb = 5
        self.__enb_sck_core_addr = 0x8
        self.__spare_bit0_lsb = 6
        self.__spare_bit0_msb = 7
        self.__spare_bit0_addr = 0x8
        self.__spare_bit1_lsb = 0
        self.__spare_bit1_msb = 3
        self.__spare_bit1_addr = 0x9
        self.__spare_bit00_lsb = 4
        self.__spare_bit00_msb = 7
        self.__spare_bit00_addr = 0x9

    def reg_addr_rd(self,reg_addr):
        return self.__I2C.i2c_rd(self.__base , self.__hostid ,reg_addr)
    def reg_addr_wr(self,reg_addr,value):
        return self.__I2C.i2c_wr(self.__base , self.__hostid ,reg_addr,value)

    @property
    def cp1p6_dreg(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__cp1p6_dreg_addr, self.__cp1p6_dreg_msb, self.__cp1p6_dreg_lsb)
    @cp1p6_dreg.setter
    def cp1p6_dreg(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__cp1p6_dreg_addr, self.__cp1p6_dreg_msb, self.__cp1p6_dreg_lsb, value)

    @property
    def cp1p2_dreg(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__cp1p2_dreg_addr, self.__cp1p2_dreg_msb, self.__cp1p2_dreg_lsb)
    @cp1p2_dreg.setter
    def cp1p2_dreg(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__cp1p2_dreg_addr, self.__cp1p2_dreg_msb, self.__cp1p2_dreg_lsb, value)

    @property
    def rc_dvref(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rc_dvref_addr, self.__rc_dvref_msb, self.__rc_dvref_lsb)
    @rc_dvref.setter
    def rc_dvref(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rc_dvref_addr, self.__rc_dvref_msb, self.__rc_dvref_lsb, value)

    @property
    def rc_enx(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rc_enx_addr, self.__rc_enx_msb, self.__rc_enx_lsb)
    @rc_enx.setter
    def rc_enx(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rc_enx_addr, self.__rc_enx_msb, self.__rc_enx_lsb, value)

    @property
    def ent_bg(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_bg_addr, self.__ent_bg_msb, self.__ent_bg_lsb)
    @ent_bg.setter
    def ent_bg(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_bg_addr, self.__ent_bg_msb, self.__ent_bg_lsb, value)

    @property
    def ent_consti(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_consti_addr, self.__ent_consti_msb, self.__ent_consti_lsb)
    @ent_consti.setter
    def ent_consti(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_consti_addr, self.__ent_consti_msb, self.__ent_consti_lsb, value)

    @property
    def rc_dcap_ext(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rc_dcap_ext_addr, self.__rc_dcap_ext_msb, self.__rc_dcap_ext_lsb)
    @rc_dcap_ext.setter
    def rc_dcap_ext(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rc_dcap_ext_addr, self.__rc_dcap_ext_msb, self.__rc_dcap_ext_lsb, value)

    @property
    def ent_cpreg_1p6(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_cpreg_1p6_addr, self.__ent_cpreg_1p6_msb, self.__ent_cpreg_1p6_lsb)
    @ent_cpreg_1p6.setter
    def ent_cpreg_1p6(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_cpreg_1p6_addr, self.__ent_cpreg_1p6_msb, self.__ent_cpreg_1p6_lsb, value)

    @property
    def ent_cgm(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_cgm_addr, self.__ent_cgm_msb, self.__ent_cgm_lsb)
    @ent_cgm.setter
    def ent_cgm(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_cgm_addr, self.__ent_cgm_msb, self.__ent_cgm_lsb, value)

    @property
    def cgm_bias(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__cgm_bias_addr, self.__cgm_bias_msb, self.__cgm_bias_lsb)
    @cgm_bias.setter
    def cgm_bias(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__cgm_bias_addr, self.__cgm_bias_msb, self.__cgm_bias_lsb, value)

    @property
    def cp1p1_pvt_reg(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__cp1p1_pvt_reg_addr, self.__cp1p1_pvt_reg_msb, self.__cp1p1_pvt_reg_lsb)
    @cp1p1_pvt_reg.setter
    def cp1p1_pvt_reg(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__cp1p1_pvt_reg_addr, self.__cp1p1_pvt_reg_msb, self.__cp1p1_pvt_reg_lsb, value)

    @property
    def dref_igm(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dref_igm_addr, self.__dref_igm_msb, self.__dref_igm_lsb)
    @dref_igm.setter
    def dref_igm(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dref_igm_addr, self.__dref_igm_msb, self.__dref_igm_lsb, value)

    @property
    def rc_cap_ext(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rc_cap_ext_addr, self.__rc_cap_ext_msb, self.__rc_cap_ext_lsb)
    @rc_cap_ext.setter
    def rc_cap_ext(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rc_cap_ext_addr, self.__rc_cap_ext_msb, self.__rc_cap_ext_lsb, value)

    @property
    def rc_start(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rc_start_addr, self.__rc_start_msb, self.__rc_start_lsb)
    @rc_start.setter
    def rc_start(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rc_start_addr, self.__rc_start_msb, self.__rc_start_lsb, value)

    @property
    def xpd_rc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_rc_addr, self.__xpd_rc_msb, self.__xpd_rc_lsb)
    @xpd_rc.setter
    def xpd_rc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_rc_addr, self.__xpd_rc_msb, self.__xpd_rc_lsb, value)

    @property
    def xpd_bg(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_bg_addr, self.__xpd_bg_msb, self.__xpd_bg_lsb)
    @xpd_bg.setter
    def xpd_bg(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_bg_addr, self.__xpd_bg_msb, self.__xpd_bg_lsb, value)

    @property
    def xpd_icx(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_icx_addr, self.__xpd_icx_msb, self.__xpd_icx_lsb)
    @xpd_icx.setter
    def xpd_icx(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_icx_addr, self.__xpd_icx_msb, self.__xpd_icx_lsb, value)

    @property
    def rc_rstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rc_rstb_addr, self.__rc_rstb_msb, self.__rc_rstb_lsb)
    @rc_rstb.setter
    def rc_rstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rc_rstb_addr, self.__rc_rstb_msb, self.__rc_rstb_lsb, value)

    @property
    def rc_div(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rc_div_addr, self.__rc_div_msb, self.__rc_div_lsb)
    @rc_div.setter
    def rc_div(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rc_div_addr, self.__rc_div_msb, self.__rc_div_lsb, value)

    @property
    def rc_cap(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rc_cap_addr, self.__rc_cap_msb, self.__rc_cap_lsb)
    @rc_cap.setter
    def rc_cap(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rc_cap_addr, self.__rc_cap_msb, self.__rc_cap_lsb, value)

    @property
    def dc_ud(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dc_ud_addr, self.__dc_ud_msb, self.__dc_ud_lsb)
    @dc_ud.setter
    def dc_ud(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dc_ud_addr, self.__dc_ud_msb, self.__dc_ud_lsb, value)

    @property
    def rc_chg_count(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rc_chg_count_addr, self.__rc_chg_count_msb, self.__rc_chg_count_lsb)
    @rc_chg_count.setter
    def rc_chg_count(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rc_chg_count_addr, self.__rc_chg_count_msb, self.__rc_chg_count_lsb, value)

    @property
    def xpd_cpreg_1p6(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_cpreg_1p6_addr, self.__xpd_cpreg_1p6_msb, self.__xpd_cpreg_1p6_lsb)
    @xpd_cpreg_1p6.setter
    def xpd_cpreg_1p6(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_cpreg_1p6_addr, self.__xpd_cpreg_1p6_msb, self.__xpd_cpreg_1p6_lsb, value)

    @property
    def xpd_cpreg_1p2(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_cpreg_1p2_addr, self.__xpd_cpreg_1p2_msb, self.__xpd_cpreg_1p2_lsb)
    @xpd_cpreg_1p2.setter
    def xpd_cpreg_1p2(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_cpreg_1p2_addr, self.__xpd_cpreg_1p2_msb, self.__xpd_cpreg_1p2_lsb, value)

    @property
    def xpd_cgm(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_cgm_addr, self.__xpd_cgm_msb, self.__xpd_cgm_lsb)
    @xpd_cgm.setter
    def xpd_cgm(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_cgm_addr, self.__xpd_cgm_msb, self.__xpd_cgm_lsb, value)

    @property
    def dtest(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dtest_addr, self.__dtest_msb, self.__dtest_lsb)
    @dtest.setter
    def dtest(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dtest_addr, self.__dtest_msb, self.__dtest_lsb, value)

    @property
    def sclock_dcap(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sclock_dcap_addr, self.__sclock_dcap_msb, self.__sclock_dcap_lsb)
    @sclock_dcap.setter
    def sclock_dcap(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sclock_dcap_addr, self.__sclock_dcap_msb, self.__sclock_dcap_lsb, value)

    @property
    def enb_sck_core(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__enb_sck_core_addr, self.__enb_sck_core_msb, self.__enb_sck_core_lsb)
    @enb_sck_core.setter
    def enb_sck_core(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__enb_sck_core_addr, self.__enb_sck_core_msb, self.__enb_sck_core_lsb, value)

    @property
    def spare_bit0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__spare_bit0_addr, self.__spare_bit0_msb, self.__spare_bit0_lsb)
    @spare_bit0.setter
    def spare_bit0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__spare_bit0_addr, self.__spare_bit0_msb, self.__spare_bit0_lsb, value)

    @property
    def spare_bit1(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__spare_bit1_addr, self.__spare_bit1_msb, self.__spare_bit1_lsb)
    @spare_bit1.setter
    def spare_bit1(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__spare_bit1_addr, self.__spare_bit1_msb, self.__spare_bit1_lsb, value)

    @property
    def spare_bit00(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__spare_bit00_addr, self.__spare_bit00_msb, self.__spare_bit00_lsb)
    @spare_bit00.setter
    def spare_bit00(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__spare_bit00_addr, self.__spare_bit00_msb, self.__spare_bit00_lsb, value)
