from hal.common import *
from hal.hwregister.hwi2c.ESP32.addr_base import *
class BBPLL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__I2C = I2C(self.channel, self.chipv)
        self.__base = BBPLL_BASE
        self.__hostid = BBPLL_HOSTID
        self.__ir_cal_delay_lsb = 0
        self.__ir_cal_delay_msb = 3
        self.__ir_cal_delay_addr = 0x0
        self.__ir_cal_ck_div_lsb = 4
        self.__ir_cal_ck_div_msb = 7
        self.__ir_cal_ck_div_addr = 0x0
        self.__ir_cal_ext_cap_lsb = 0
        self.__ir_cal_ext_cap_msb = 3
        self.__ir_cal_ext_cap_addr = 0x1
        self.__ir_cal_enx_cap_lsb = 4
        self.__ir_cal_enx_cap_msb = 4
        self.__ir_cal_enx_cap_addr = 0x1
        self.__ir_cal_rstb_lsb = 5
        self.__ir_cal_rstb_msb = 5
        self.__ir_cal_rstb_addr = 0x1
        self.__ir_cal_start_lsb = 6
        self.__ir_cal_start_msb = 6
        self.__ir_cal_start_addr = 0x1
        self.__ir_cal_unstop_lsb = 7
        self.__ir_cal_unstop_msb = 7
        self.__ir_cal_unstop_addr = 0x1
        self.__oc_ref_div_lsb = 0
        self.__oc_ref_div_msb = 3
        self.__oc_ref_div_addr = 0x2
        self.__oc_div_lsb = 4
        self.__oc_div_msb = 6
        self.__oc_div_addr = 0x2
        self.__oc_lref_lsb = 7
        self.__oc_lref_msb = 7
        self.__oc_lref_addr = 0x2
        self.__oc_div_lsb = 0
        self.__oc_div_msb = 7
        self.__oc_div_addr = 0x3
        self.__oc_enb_fcal_lsb = 0
        self.__oc_enb_fcal_msb = 0
        self.__oc_enb_fcal_addr = 0x4
        self.__oc_dchgp_lsb = 1
        self.__oc_dchgp_msb = 3
        self.__oc_dchgp_addr = 0x4
        self.__oc_dhref_sel_lsb = 4
        self.__oc_dhref_sel_msb = 5
        self.__oc_dhref_sel_addr = 0x4
        self.__oc_dlref_sel_lsb = 6
        self.__oc_dlref_sel_msb = 7
        self.__oc_dlref_sel_addr = 0x4
        self.__oc_dcur_lsb = 0
        self.__oc_dcur_msb = 2
        self.__oc_dcur_addr = 0x5
        self.__oc_bst_div_lsb = 3
        self.__oc_bst_div_msb = 3
        self.__oc_bst_div_addr = 0x5
        self.__oc_bst_e2c_lsb = 4
        self.__oc_bst_e2c_msb = 4
        self.__oc_bst_e2c_addr = 0x5
        self.__oc_tschgp_lsb = 5
        self.__oc_tschgp_msb = 5
        self.__oc_tschgp_addr = 0x5
        self.__oc_bw_lsb = 6
        self.__oc_bw_msb = 7
        self.__oc_bw_addr = 0x5
        self.__or_lock1_lsb = 0
        self.__or_lock1_msb = 0
        self.__or_lock1_addr = 0x6
        self.__or_lock2_lsb = 1
        self.__or_lock2_msb = 1
        self.__or_lock2_addr = 0x6
        self.__or_cal_cap_lsb = 0
        self.__or_cal_cap_msb = 3
        self.__or_cal_cap_addr = 0x7
        self.__or_cal_udf_lsb = 4
        self.__or_cal_udf_msb = 4
        self.__or_cal_udf_addr = 0x7
        self.__or_cal_ovf_lsb = 5
        self.__or_cal_ovf_msb = 5
        self.__or_cal_ovf_addr = 0x7
        self.__or_cal_end_lsb = 6
        self.__or_cal_end_msb = 6
        self.__or_cal_end_addr = 0x7
        self.__bbadc_delay1_lsb = 0
        self.__bbadc_delay1_msb = 1
        self.__bbadc_delay1_addr = 0x8
        self.__bbadc_delay2_lsb = 2
        self.__bbadc_delay2_msb = 3
        self.__bbadc_delay2_addr = 0x8
        self.__bbadc_delay3_lsb = 4
        self.__bbadc_delay3_msb = 5
        self.__bbadc_delay3_addr = 0x8
        self.__bbadc_delay4_lsb = 6
        self.__bbadc_delay4_msb = 7
        self.__bbadc_delay4_addr = 0x8
        self.__bbadc_delay5_lsb = 0
        self.__bbadc_delay5_msb = 1
        self.__bbadc_delay5_addr = 0x9
        self.__bbadc_delay6_lsb = 2
        self.__bbadc_delay6_msb = 3
        self.__bbadc_delay6_addr = 0x9
        self.__bbadc_dsmp_lsb = 4
        self.__bbadc_dsmp_msb = 7
        self.__bbadc_dsmp_addr = 0x9
        self.__dtest_lsb = 0
        self.__dtest_msb = 1
        self.__dtest_addr = 0xa
        self.__ent_adc_lsb = 2
        self.__ent_adc_msb = 3
        self.__ent_adc_addr = 0xa
        self.__bbadc_div_lsb = 4
        self.__bbadc_div_msb = 5
        self.__bbadc_div_addr = 0xa
        self.__ent_pll_lsb = 6
        self.__ent_pll_msb = 6
        self.__ent_pll_addr = 0xa
        self.__oc_enb_vcon_lsb = 7
        self.__oc_enb_vcon_msb = 7
        self.__oc_enb_vcon_addr = 0xa
        self.__div_dac_lsb = 0
        self.__div_dac_msb = 0
        self.__div_dac_addr = 0xb
        self.__div_cpu_lsb = 1
        self.__div_cpu_msb = 1
        self.__div_cpu_addr = 0xb
        self.__bbadc_input_short_lsb = 2
        self.__bbadc_input_short_msb = 2
        self.__bbadc_input_short_addr = 0xb
        self.__bbadc_cal_lsb = 3
        self.__bbadc_cal_msb = 4
        self.__bbadc_cal_addr = 0xb
        self.__bbadc_dcm_lsb = 5
        self.__bbadc_dcm_msb = 6
        self.__bbadc_dcm_addr = 0xb
        self.__endiv5_lsb = 7
        self.__endiv5_msb = 7
        self.__endiv5_addr = 0xb
        self.__bbadc_cal_lsb = 0
        self.__bbadc_cal_msb = 7
        self.__bbadc_cal_addr = 0xc

    def reg_addr_rd(self,reg_addr):
        return self.__I2C.i2c_rd(self.__base , self.__hostid ,reg_addr)
    def reg_addr_wr(self,reg_addr,value):
        return self.__I2C.i2c_wr(self.__base , self.__hostid ,reg_addr,value)

    @property
    def ir_cal_delay(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_cal_delay_addr, self.__ir_cal_delay_msb, self.__ir_cal_delay_lsb)
    @ir_cal_delay.setter
    def ir_cal_delay(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_cal_delay_addr, self.__ir_cal_delay_msb, self.__ir_cal_delay_lsb, value)

    @property
    def ir_cal_ck_div(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_cal_ck_div_addr, self.__ir_cal_ck_div_msb, self.__ir_cal_ck_div_lsb)
    @ir_cal_ck_div.setter
    def ir_cal_ck_div(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_cal_ck_div_addr, self.__ir_cal_ck_div_msb, self.__ir_cal_ck_div_lsb, value)

    @property
    def ir_cal_ext_cap(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_cal_ext_cap_addr, self.__ir_cal_ext_cap_msb, self.__ir_cal_ext_cap_lsb)
    @ir_cal_ext_cap.setter
    def ir_cal_ext_cap(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_cal_ext_cap_addr, self.__ir_cal_ext_cap_msb, self.__ir_cal_ext_cap_lsb, value)

    @property
    def ir_cal_enx_cap(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_cal_enx_cap_addr, self.__ir_cal_enx_cap_msb, self.__ir_cal_enx_cap_lsb)
    @ir_cal_enx_cap.setter
    def ir_cal_enx_cap(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_cal_enx_cap_addr, self.__ir_cal_enx_cap_msb, self.__ir_cal_enx_cap_lsb, value)

    @property
    def ir_cal_rstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_cal_rstb_addr, self.__ir_cal_rstb_msb, self.__ir_cal_rstb_lsb)
    @ir_cal_rstb.setter
    def ir_cal_rstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_cal_rstb_addr, self.__ir_cal_rstb_msb, self.__ir_cal_rstb_lsb, value)

    @property
    def ir_cal_start(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_cal_start_addr, self.__ir_cal_start_msb, self.__ir_cal_start_lsb)
    @ir_cal_start.setter
    def ir_cal_start(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_cal_start_addr, self.__ir_cal_start_msb, self.__ir_cal_start_lsb, value)

    @property
    def ir_cal_unstop(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_cal_unstop_addr, self.__ir_cal_unstop_msb, self.__ir_cal_unstop_lsb)
    @ir_cal_unstop.setter
    def ir_cal_unstop(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_cal_unstop_addr, self.__ir_cal_unstop_msb, self.__ir_cal_unstop_lsb, value)

    @property
    def oc_ref_div(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_ref_div_addr, self.__oc_ref_div_msb, self.__oc_ref_div_lsb)
    @oc_ref_div.setter
    def oc_ref_div(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_ref_div_addr, self.__oc_ref_div_msb, self.__oc_ref_div_lsb, value)

    @property
    def oc_div(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_div_addr, self.__oc_div_msb, self.__oc_div_lsb)
    @oc_div.setter
    def oc_div(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_div_addr, self.__oc_div_msb, self.__oc_div_lsb, value)

    @property
    def oc_lref(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_lref_addr, self.__oc_lref_msb, self.__oc_lref_lsb)
    @oc_lref.setter
    def oc_lref(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_lref_addr, self.__oc_lref_msb, self.__oc_lref_lsb, value)

    @property
    def oc_div(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_div_addr, self.__oc_div_msb, self.__oc_div_lsb)
    @oc_div.setter
    def oc_div(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_div_addr, self.__oc_div_msb, self.__oc_div_lsb, value)

    @property
    def oc_enb_fcal(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_enb_fcal_addr, self.__oc_enb_fcal_msb, self.__oc_enb_fcal_lsb)
    @oc_enb_fcal.setter
    def oc_enb_fcal(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_enb_fcal_addr, self.__oc_enb_fcal_msb, self.__oc_enb_fcal_lsb, value)

    @property
    def oc_dchgp(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_dchgp_addr, self.__oc_dchgp_msb, self.__oc_dchgp_lsb)
    @oc_dchgp.setter
    def oc_dchgp(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_dchgp_addr, self.__oc_dchgp_msb, self.__oc_dchgp_lsb, value)

    @property
    def oc_dhref_sel(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_dhref_sel_addr, self.__oc_dhref_sel_msb, self.__oc_dhref_sel_lsb)
    @oc_dhref_sel.setter
    def oc_dhref_sel(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_dhref_sel_addr, self.__oc_dhref_sel_msb, self.__oc_dhref_sel_lsb, value)

    @property
    def oc_dlref_sel(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_dlref_sel_addr, self.__oc_dlref_sel_msb, self.__oc_dlref_sel_lsb)
    @oc_dlref_sel.setter
    def oc_dlref_sel(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_dlref_sel_addr, self.__oc_dlref_sel_msb, self.__oc_dlref_sel_lsb, value)

    @property
    def oc_dcur(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_dcur_addr, self.__oc_dcur_msb, self.__oc_dcur_lsb)
    @oc_dcur.setter
    def oc_dcur(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_dcur_addr, self.__oc_dcur_msb, self.__oc_dcur_lsb, value)

    @property
    def oc_bst_div(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_bst_div_addr, self.__oc_bst_div_msb, self.__oc_bst_div_lsb)
    @oc_bst_div.setter
    def oc_bst_div(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_bst_div_addr, self.__oc_bst_div_msb, self.__oc_bst_div_lsb, value)

    @property
    def oc_bst_e2c(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_bst_e2c_addr, self.__oc_bst_e2c_msb, self.__oc_bst_e2c_lsb)
    @oc_bst_e2c.setter
    def oc_bst_e2c(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_bst_e2c_addr, self.__oc_bst_e2c_msb, self.__oc_bst_e2c_lsb, value)

    @property
    def oc_tschgp(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_tschgp_addr, self.__oc_tschgp_msb, self.__oc_tschgp_lsb)
    @oc_tschgp.setter
    def oc_tschgp(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_tschgp_addr, self.__oc_tschgp_msb, self.__oc_tschgp_lsb, value)

    @property
    def oc_bw(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_bw_addr, self.__oc_bw_msb, self.__oc_bw_lsb)
    @oc_bw.setter
    def oc_bw(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_bw_addr, self.__oc_bw_msb, self.__oc_bw_lsb, value)

    @property
    def or_lock1(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__or_lock1_addr, self.__or_lock1_msb, self.__or_lock1_lsb)
    @or_lock1.setter
    def or_lock1(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__or_lock1_addr, self.__or_lock1_msb, self.__or_lock1_lsb, value)

    @property
    def or_lock2(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__or_lock2_addr, self.__or_lock2_msb, self.__or_lock2_lsb)
    @or_lock2.setter
    def or_lock2(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__or_lock2_addr, self.__or_lock2_msb, self.__or_lock2_lsb, value)

    @property
    def or_cal_cap(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__or_cal_cap_addr, self.__or_cal_cap_msb, self.__or_cal_cap_lsb)
    @or_cal_cap.setter
    def or_cal_cap(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__or_cal_cap_addr, self.__or_cal_cap_msb, self.__or_cal_cap_lsb, value)

    @property
    def or_cal_udf(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__or_cal_udf_addr, self.__or_cal_udf_msb, self.__or_cal_udf_lsb)
    @or_cal_udf.setter
    def or_cal_udf(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__or_cal_udf_addr, self.__or_cal_udf_msb, self.__or_cal_udf_lsb, value)

    @property
    def or_cal_ovf(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__or_cal_ovf_addr, self.__or_cal_ovf_msb, self.__or_cal_ovf_lsb)
    @or_cal_ovf.setter
    def or_cal_ovf(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__or_cal_ovf_addr, self.__or_cal_ovf_msb, self.__or_cal_ovf_lsb, value)

    @property
    def or_cal_end(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__or_cal_end_addr, self.__or_cal_end_msb, self.__or_cal_end_lsb)
    @or_cal_end.setter
    def or_cal_end(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__or_cal_end_addr, self.__or_cal_end_msb, self.__or_cal_end_lsb, value)

    @property
    def bbadc_delay1(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__bbadc_delay1_addr, self.__bbadc_delay1_msb, self.__bbadc_delay1_lsb)
    @bbadc_delay1.setter
    def bbadc_delay1(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__bbadc_delay1_addr, self.__bbadc_delay1_msb, self.__bbadc_delay1_lsb, value)

    @property
    def bbadc_delay2(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__bbadc_delay2_addr, self.__bbadc_delay2_msb, self.__bbadc_delay2_lsb)
    @bbadc_delay2.setter
    def bbadc_delay2(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__bbadc_delay2_addr, self.__bbadc_delay2_msb, self.__bbadc_delay2_lsb, value)

    @property
    def bbadc_delay3(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__bbadc_delay3_addr, self.__bbadc_delay3_msb, self.__bbadc_delay3_lsb)
    @bbadc_delay3.setter
    def bbadc_delay3(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__bbadc_delay3_addr, self.__bbadc_delay3_msb, self.__bbadc_delay3_lsb, value)

    @property
    def bbadc_delay4(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__bbadc_delay4_addr, self.__bbadc_delay4_msb, self.__bbadc_delay4_lsb)
    @bbadc_delay4.setter
    def bbadc_delay4(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__bbadc_delay4_addr, self.__bbadc_delay4_msb, self.__bbadc_delay4_lsb, value)

    @property
    def bbadc_delay5(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__bbadc_delay5_addr, self.__bbadc_delay5_msb, self.__bbadc_delay5_lsb)
    @bbadc_delay5.setter
    def bbadc_delay5(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__bbadc_delay5_addr, self.__bbadc_delay5_msb, self.__bbadc_delay5_lsb, value)

    @property
    def bbadc_delay6(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__bbadc_delay6_addr, self.__bbadc_delay6_msb, self.__bbadc_delay6_lsb)
    @bbadc_delay6.setter
    def bbadc_delay6(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__bbadc_delay6_addr, self.__bbadc_delay6_msb, self.__bbadc_delay6_lsb, value)

    @property
    def bbadc_dsmp(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__bbadc_dsmp_addr, self.__bbadc_dsmp_msb, self.__bbadc_dsmp_lsb)
    @bbadc_dsmp.setter
    def bbadc_dsmp(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__bbadc_dsmp_addr, self.__bbadc_dsmp_msb, self.__bbadc_dsmp_lsb, value)

    @property
    def dtest(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dtest_addr, self.__dtest_msb, self.__dtest_lsb)
    @dtest.setter
    def dtest(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dtest_addr, self.__dtest_msb, self.__dtest_lsb, value)

    @property
    def ent_adc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_adc_addr, self.__ent_adc_msb, self.__ent_adc_lsb)
    @ent_adc.setter
    def ent_adc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_adc_addr, self.__ent_adc_msb, self.__ent_adc_lsb, value)

    @property
    def bbadc_div(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__bbadc_div_addr, self.__bbadc_div_msb, self.__bbadc_div_lsb)
    @bbadc_div.setter
    def bbadc_div(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__bbadc_div_addr, self.__bbadc_div_msb, self.__bbadc_div_lsb, value)

    @property
    def ent_pll(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_pll_addr, self.__ent_pll_msb, self.__ent_pll_lsb)
    @ent_pll.setter
    def ent_pll(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_pll_addr, self.__ent_pll_msb, self.__ent_pll_lsb, value)

    @property
    def oc_enb_vcon(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_enb_vcon_addr, self.__oc_enb_vcon_msb, self.__oc_enb_vcon_lsb)
    @oc_enb_vcon.setter
    def oc_enb_vcon(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_enb_vcon_addr, self.__oc_enb_vcon_msb, self.__oc_enb_vcon_lsb, value)

    @property
    def div_dac(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__div_dac_addr, self.__div_dac_msb, self.__div_dac_lsb)
    @div_dac.setter
    def div_dac(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__div_dac_addr, self.__div_dac_msb, self.__div_dac_lsb, value)

    @property
    def div_cpu(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__div_cpu_addr, self.__div_cpu_msb, self.__div_cpu_lsb)
    @div_cpu.setter
    def div_cpu(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__div_cpu_addr, self.__div_cpu_msb, self.__div_cpu_lsb, value)

    @property
    def bbadc_input_short(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__bbadc_input_short_addr, self.__bbadc_input_short_msb, self.__bbadc_input_short_lsb)
    @bbadc_input_short.setter
    def bbadc_input_short(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__bbadc_input_short_addr, self.__bbadc_input_short_msb, self.__bbadc_input_short_lsb, value)

    @property
    def bbadc_cal(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__bbadc_cal_addr, self.__bbadc_cal_msb, self.__bbadc_cal_lsb)
    @bbadc_cal.setter
    def bbadc_cal(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__bbadc_cal_addr, self.__bbadc_cal_msb, self.__bbadc_cal_lsb, value)

    @property
    def bbadc_dcm(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__bbadc_dcm_addr, self.__bbadc_dcm_msb, self.__bbadc_dcm_lsb)
    @bbadc_dcm.setter
    def bbadc_dcm(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__bbadc_dcm_addr, self.__bbadc_dcm_msb, self.__bbadc_dcm_lsb, value)

    @property
    def endiv5(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__endiv5_addr, self.__endiv5_msb, self.__endiv5_lsb)
    @endiv5.setter
    def endiv5(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__endiv5_addr, self.__endiv5_msb, self.__endiv5_lsb, value)

    @property
    def bbadc_cal(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__bbadc_cal_addr, self.__bbadc_cal_msb, self.__bbadc_cal_lsb)
    @bbadc_cal.setter
    def bbadc_cal(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__bbadc_cal_addr, self.__bbadc_cal_msb, self.__bbadc_cal_lsb, value)
