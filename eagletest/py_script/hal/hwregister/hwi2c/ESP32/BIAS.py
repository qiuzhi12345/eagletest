from hal.common import *
from hal.hwregister.hwi2c.ESP32.addr_base import *
class BIAS(object):
    def __init__(self, channel, chipv = "ESP32"):
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
        self.__ent_cpreg_lsb = 0
        self.__ent_cpreg_msb = 0
        self.__ent_cpreg_addr = 0x2
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
        self.__rc_ud_lsb = 6
        self.__rc_ud_msb = 6
        self.__rc_ud_addr = 0x5
        self.__res_det_out_lsb = 7
        self.__res_det_out_msb = 7
        self.__res_det_out_addr = 0x5
        self.__rc_chg_count_lsb = 0
        self.__rc_chg_count_msb = 4
        self.__rc_chg_count_addr = 0x6
        self.__dres12k_force_on_lsb = 5
        self.__dres12k_force_on_msb = 5
        self.__dres12k_force_on_addr = 0x6
        self.__dres12k_force_off_lsb = 6
        self.__dres12k_force_off_msb = 6
        self.__dres12k_force_off_addr = 0x6
        self.__xpd_cpreg_lsb = 0
        self.__xpd_cpreg_msb = 0
        self.__xpd_cpreg_addr = 0x7
        self.__xpd_cgm_lsb = 1
        self.__xpd_cgm_msb = 1
        self.__xpd_cgm_addr = 0x7
        self.__dtest_lsb = 2
        self.__dtest_msb = 3
        self.__dtest_addr = 0x7
        self.__dres12k_lsb = 4
        self.__dres12k_msb = 7
        self.__dres12k_addr = 0x7
        self.__bg_en_j25_lsb = 0
        self.__bg_en_j25_msb = 3
        self.__bg_en_j25_addr = 0x8
        self.__bg_en_lnoise_lsb = 4
        self.__bg_en_lnoise_msb = 4
        self.__bg_en_lnoise_addr = 0x8
        self.__db_atten_on_lsb = 0
        self.__db_atten_on_msb = 1
        self.__db_atten_on_addr = 0x9
        self.__db_atten_off_lsb = 2
        self.__db_atten_off_msb = 3
        self.__db_atten_off_addr = 0x9
        self.__en_bias_sleep_atten_lsb = 4
        self.__en_bias_sleep_atten_msb = 4
        self.__en_bias_sleep_atten_addr = 0x9

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
    def ent_cpreg(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_cpreg_addr, self.__ent_cpreg_msb, self.__ent_cpreg_lsb)
    @ent_cpreg.setter
    def ent_cpreg(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_cpreg_addr, self.__ent_cpreg_msb, self.__ent_cpreg_lsb, value)

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
    def rc_ud(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rc_ud_addr, self.__rc_ud_msb, self.__rc_ud_lsb)
    @rc_ud.setter
    def rc_ud(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rc_ud_addr, self.__rc_ud_msb, self.__rc_ud_lsb, value)

    @property
    def res_det_out(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__res_det_out_addr, self.__res_det_out_msb, self.__res_det_out_lsb)
    @res_det_out.setter
    def res_det_out(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__res_det_out_addr, self.__res_det_out_msb, self.__res_det_out_lsb, value)

    @property
    def rc_chg_count(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rc_chg_count_addr, self.__rc_chg_count_msb, self.__rc_chg_count_lsb)
    @rc_chg_count.setter
    def rc_chg_count(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rc_chg_count_addr, self.__rc_chg_count_msb, self.__rc_chg_count_lsb, value)

    @property
    def dres12k_force_on(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dres12k_force_on_addr, self.__dres12k_force_on_msb, self.__dres12k_force_on_lsb)
    @dres12k_force_on.setter
    def dres12k_force_on(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dres12k_force_on_addr, self.__dres12k_force_on_msb, self.__dres12k_force_on_lsb, value)

    @property
    def dres12k_force_off(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dres12k_force_off_addr, self.__dres12k_force_off_msb, self.__dres12k_force_off_lsb)
    @dres12k_force_off.setter
    def dres12k_force_off(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dres12k_force_off_addr, self.__dres12k_force_off_msb, self.__dres12k_force_off_lsb, value)

    @property
    def xpd_cpreg(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_cpreg_addr, self.__xpd_cpreg_msb, self.__xpd_cpreg_lsb)
    @xpd_cpreg.setter
    def xpd_cpreg(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_cpreg_addr, self.__xpd_cpreg_msb, self.__xpd_cpreg_lsb, value)

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
    def dres12k(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dres12k_addr, self.__dres12k_msb, self.__dres12k_lsb)
    @dres12k.setter
    def dres12k(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dres12k_addr, self.__dres12k_msb, self.__dres12k_lsb, value)

    @property
    def bg_en_j25(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__bg_en_j25_addr, self.__bg_en_j25_msb, self.__bg_en_j25_lsb)
    @bg_en_j25.setter
    def bg_en_j25(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__bg_en_j25_addr, self.__bg_en_j25_msb, self.__bg_en_j25_lsb, value)

    @property
    def bg_en_lnoise(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__bg_en_lnoise_addr, self.__bg_en_lnoise_msb, self.__bg_en_lnoise_lsb)
    @bg_en_lnoise.setter
    def bg_en_lnoise(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__bg_en_lnoise_addr, self.__bg_en_lnoise_msb, self.__bg_en_lnoise_lsb, value)

    @property
    def db_atten_on(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__db_atten_on_addr, self.__db_atten_on_msb, self.__db_atten_on_lsb)
    @db_atten_on.setter
    def db_atten_on(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__db_atten_on_addr, self.__db_atten_on_msb, self.__db_atten_on_lsb, value)

    @property
    def db_atten_off(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__db_atten_off_addr, self.__db_atten_off_msb, self.__db_atten_off_lsb)
    @db_atten_off.setter
    def db_atten_off(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__db_atten_off_addr, self.__db_atten_off_msb, self.__db_atten_off_lsb, value)

    @property
    def en_bias_sleep_atten(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__en_bias_sleep_atten_addr, self.__en_bias_sleep_atten_msb, self.__en_bias_sleep_atten_lsb)
    @en_bias_sleep_atten.setter
    def en_bias_sleep_atten(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__en_bias_sleep_atten_addr, self.__en_bias_sleep_atten_msb, self.__en_bias_sleep_atten_lsb, value)
