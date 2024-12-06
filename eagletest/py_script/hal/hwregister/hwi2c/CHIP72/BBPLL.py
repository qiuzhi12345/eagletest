from hal.common import *
from hal.hwregister.hwi2c.CHIP72.addr_base import *
class BBPLL(object):
    def __init__(self, channel, chipv = "CHIP72"):
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
        self.__oc_dchgp_lsb = 4
        self.__oc_dchgp_msb = 6
        self.__oc_dchgp_addr = 0x2
        self.__oc_enb_fcal_lsb = 7
        self.__oc_enb_fcal_msb = 7
        self.__oc_enb_fcal_addr = 0x2
        self.__oc_div_lsb = 0
        self.__oc_div_msb = 7
        self.__oc_div_addr = 0x3
        self.__rstb_div_adc_lsb = 0
        self.__rstb_div_adc_msb = 0
        self.__rstb_div_adc_addr = 0x4
        self.__mode_hf_lsb = 1
        self.__mode_hf_msb = 1
        self.__mode_hf_addr = 0x4
        self.__div_adc_lsb = 2
        self.__div_adc_msb = 3
        self.__div_adc_addr = 0x4
        self.__div_dac_lsb = 4
        self.__div_dac_msb = 4
        self.__div_dac_addr = 0x4
        self.__div_cpu_lsb = 5
        self.__div_cpu_msb = 5
        self.__div_cpu_addr = 0x4
        self.__oc_enb_vcon_lsb = 6
        self.__oc_enb_vcon_msb = 6
        self.__oc_enb_vcon_addr = 0x4
        self.__oc_tschgp_lsb = 7
        self.__oc_tschgp_msb = 7
        self.__oc_tschgp_addr = 0x4
        self.__oc_dr1_lsb = 0
        self.__oc_dr1_msb = 2
        self.__oc_dr1_addr = 0x5
        self.__oc_dr3_lsb = 4
        self.__oc_dr3_msb = 6
        self.__oc_dr3_addr = 0x5
        self.__oc_dcur_lsb = 0
        self.__oc_dcur_msb = 2
        self.__oc_dcur_addr = 0x6
        self.__inc_cur_lsb = 3
        self.__inc_cur_msb = 3
        self.__inc_cur_addr = 0x6
        self.__oc_dhref_sel_lsb = 4
        self.__oc_dhref_sel_msb = 5
        self.__oc_dhref_sel_addr = 0x6
        self.__oc_dlref_sel_lsb = 6
        self.__oc_dlref_sel_msb = 7
        self.__oc_dlref_sel_addr = 0x6
        self.__or_cal_cap_lsb = 0
        self.__or_cal_cap_msb = 3
        self.__or_cal_cap_addr = 0x8
        self.__or_cal_udf_lsb = 4
        self.__or_cal_udf_msb = 4
        self.__or_cal_udf_addr = 0x8
        self.__or_cal_ovf_lsb = 5
        self.__or_cal_ovf_msb = 5
        self.__or_cal_ovf_addr = 0x8
        self.__or_cal_end_lsb = 6
        self.__or_cal_end_msb = 6
        self.__or_cal_end_addr = 0x8
        self.__or_lock_lsb = 7
        self.__or_lock_msb = 7
        self.__or_lock_addr = 0x8
        self.__bbadc_delay1_lsb = 0
        self.__bbadc_delay1_msb = 1
        self.__bbadc_delay1_addr = 0x9
        self.__bbadc_delay2_lsb = 2
        self.__bbadc_delay2_msb = 3
        self.__bbadc_delay2_addr = 0x9
        self.__bbadc_dvdd_lsb = 4
        self.__bbadc_dvdd_msb = 5
        self.__bbadc_dvdd_addr = 0x9
        self.__bbadc_dref_lsb = 6
        self.__bbadc_dref_msb = 7
        self.__bbadc_dref_addr = 0x9
        self.__bbadc_dcur_lsb = 0
        self.__bbadc_dcur_msb = 1
        self.__bbadc_dcur_addr = 0xa
        self.__bbadc_input_short_lsb = 2
        self.__bbadc_input_short_msb = 2
        self.__bbadc_input_short_addr = 0xa
        self.__ent_pll_lsb = 3
        self.__ent_pll_msb = 3
        self.__ent_pll_addr = 0xa
        self.__dtest_lsb = 4
        self.__dtest_msb = 5
        self.__dtest_addr = 0xa
        self.__ent_adc_lsb = 6
        self.__ent_adc_msb = 7
        self.__ent_adc_addr = 0xa

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
    def oc_dchgp(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_dchgp_addr, self.__oc_dchgp_msb, self.__oc_dchgp_lsb)
    @oc_dchgp.setter
    def oc_dchgp(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_dchgp_addr, self.__oc_dchgp_msb, self.__oc_dchgp_lsb, value)

    @property
    def oc_enb_fcal(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_enb_fcal_addr, self.__oc_enb_fcal_msb, self.__oc_enb_fcal_lsb)
    @oc_enb_fcal.setter
    def oc_enb_fcal(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_enb_fcal_addr, self.__oc_enb_fcal_msb, self.__oc_enb_fcal_lsb, value)

    @property
    def oc_div(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_div_addr, self.__oc_div_msb, self.__oc_div_lsb)
    @oc_div.setter
    def oc_div(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_div_addr, self.__oc_div_msb, self.__oc_div_lsb, value)

    @property
    def rstb_div_adc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rstb_div_adc_addr, self.__rstb_div_adc_msb, self.__rstb_div_adc_lsb)
    @rstb_div_adc.setter
    def rstb_div_adc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rstb_div_adc_addr, self.__rstb_div_adc_msb, self.__rstb_div_adc_lsb, value)

    @property
    def mode_hf(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__mode_hf_addr, self.__mode_hf_msb, self.__mode_hf_lsb)
    @mode_hf.setter
    def mode_hf(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__mode_hf_addr, self.__mode_hf_msb, self.__mode_hf_lsb, value)

    @property
    def div_adc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__div_adc_addr, self.__div_adc_msb, self.__div_adc_lsb)
    @div_adc.setter
    def div_adc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__div_adc_addr, self.__div_adc_msb, self.__div_adc_lsb, value)

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
    def oc_enb_vcon(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_enb_vcon_addr, self.__oc_enb_vcon_msb, self.__oc_enb_vcon_lsb)
    @oc_enb_vcon.setter
    def oc_enb_vcon(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_enb_vcon_addr, self.__oc_enb_vcon_msb, self.__oc_enb_vcon_lsb, value)

    @property
    def oc_tschgp(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_tschgp_addr, self.__oc_tschgp_msb, self.__oc_tschgp_lsb)
    @oc_tschgp.setter
    def oc_tschgp(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_tschgp_addr, self.__oc_tschgp_msb, self.__oc_tschgp_lsb, value)

    @property
    def oc_dr1(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_dr1_addr, self.__oc_dr1_msb, self.__oc_dr1_lsb)
    @oc_dr1.setter
    def oc_dr1(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_dr1_addr, self.__oc_dr1_msb, self.__oc_dr1_lsb, value)

    @property
    def oc_dr3(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_dr3_addr, self.__oc_dr3_msb, self.__oc_dr3_lsb)
    @oc_dr3.setter
    def oc_dr3(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_dr3_addr, self.__oc_dr3_msb, self.__oc_dr3_lsb, value)

    @property
    def oc_dcur(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_dcur_addr, self.__oc_dcur_msb, self.__oc_dcur_lsb)
    @oc_dcur.setter
    def oc_dcur(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_dcur_addr, self.__oc_dcur_msb, self.__oc_dcur_lsb, value)

    @property
    def inc_cur(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__inc_cur_addr, self.__inc_cur_msb, self.__inc_cur_lsb)
    @inc_cur.setter
    def inc_cur(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__inc_cur_addr, self.__inc_cur_msb, self.__inc_cur_lsb, value)

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
    def or_lock(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__or_lock_addr, self.__or_lock_msb, self.__or_lock_lsb)
    @or_lock.setter
    def or_lock(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__or_lock_addr, self.__or_lock_msb, self.__or_lock_lsb, value)

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
    def bbadc_dvdd(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__bbadc_dvdd_addr, self.__bbadc_dvdd_msb, self.__bbadc_dvdd_lsb)
    @bbadc_dvdd.setter
    def bbadc_dvdd(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__bbadc_dvdd_addr, self.__bbadc_dvdd_msb, self.__bbadc_dvdd_lsb, value)

    @property
    def bbadc_dref(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__bbadc_dref_addr, self.__bbadc_dref_msb, self.__bbadc_dref_lsb)
    @bbadc_dref.setter
    def bbadc_dref(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__bbadc_dref_addr, self.__bbadc_dref_msb, self.__bbadc_dref_lsb, value)

    @property
    def bbadc_dcur(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__bbadc_dcur_addr, self.__bbadc_dcur_msb, self.__bbadc_dcur_lsb)
    @bbadc_dcur.setter
    def bbadc_dcur(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__bbadc_dcur_addr, self.__bbadc_dcur_msb, self.__bbadc_dcur_lsb, value)

    @property
    def bbadc_input_short(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__bbadc_input_short_addr, self.__bbadc_input_short_msb, self.__bbadc_input_short_lsb)
    @bbadc_input_short.setter
    def bbadc_input_short(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__bbadc_input_short_addr, self.__bbadc_input_short_msb, self.__bbadc_input_short_lsb, value)

    @property
    def ent_pll(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_pll_addr, self.__ent_pll_msb, self.__ent_pll_lsb)
    @ent_pll.setter
    def ent_pll(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_pll_addr, self.__ent_pll_msb, self.__ent_pll_lsb, value)

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
