from hal.common import *
from hal.hwregister.hwi2c.CHIP72.addr_base import *
class APLL(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__I2C = I2C(self.channel, self.chipv)
        self.__base = APLL_BASE
        self.__hostid = APLL_HOSTID
        self.__ir_cal_delay_lsb = 0
        self.__ir_cal_delay_msb = 3
        self.__ir_cal_delay_addr = 0x0
        self.__ir_cal_rstb_lsb = 4
        self.__ir_cal_rstb_msb = 4
        self.__ir_cal_rstb_addr = 0x0
        self.__ir_cal_start_lsb = 5
        self.__ir_cal_start_msb = 5
        self.__ir_cal_start_addr = 0x0
        self.__ir_cal_unstop_lsb = 6
        self.__ir_cal_unstop_msb = 6
        self.__ir_cal_unstop_addr = 0x0
        self.__oc_enb_fcal_lsb = 7
        self.__oc_enb_fcal_msb = 7
        self.__oc_enb_fcal_addr = 0x0
        self.__ir_cal_ext_cap_lsb = 0
        self.__ir_cal_ext_cap_msb = 4
        self.__ir_cal_ext_cap_addr = 0x1
        self.__ir_cal_enx_cap_lsb = 5
        self.__ir_cal_enx_cap_msb = 5
        self.__ir_cal_enx_cap_addr = 0x1
        self.__oc_lbw_lsb = 6
        self.__oc_lbw_msb = 6
        self.__oc_lbw_addr = 0x1
        self.__ir_cal_ck_div_lsb = 0
        self.__ir_cal_ck_div_msb = 3
        self.__ir_cal_ck_div_addr = 0x2
        self.__oc_dchgp_lsb = 4
        self.__oc_dchgp_msb = 6
        self.__oc_dchgp_addr = 0x2
        self.__oc_enb_vcon_lsb = 7
        self.__oc_enb_vcon_msb = 7
        self.__oc_enb_vcon_addr = 0x2
        self.__or_cal_cap_lsb = 0
        self.__or_cal_cap_msb = 4
        self.__or_cal_cap_addr = 0x3
        self.__or_cal_udf_lsb = 5
        self.__or_cal_udf_msb = 5
        self.__or_cal_udf_addr = 0x3
        self.__or_cal_ovf_lsb = 6
        self.__or_cal_ovf_msb = 6
        self.__or_cal_ovf_addr = 0x3
        self.__or_cal_end_lsb = 7
        self.__or_cal_end_msb = 7
        self.__or_cal_end_addr = 0x3
        self.__or_output_div_lsb = 0
        self.__or_output_div_msb = 4
        self.__or_output_div_addr = 0x4
        self.__oc_tschgp_lsb = 6
        self.__oc_tschgp_msb = 6
        self.__oc_tschgp_addr = 0x4
        self.__en_fast_cal_lsb = 7
        self.__en_fast_cal_msb = 7
        self.__en_fast_cal_addr = 0x4
        self.__oc_dhref_sel_lsb = 0
        self.__oc_dhref_sel_msb = 1
        self.__oc_dhref_sel_addr = 0x5
        self.__oc_dlref_sel_lsb = 2
        self.__oc_dlref_sel_msb = 3
        self.__oc_dlref_sel_addr = 0x5
        self.__sdm_dither_lsb = 4
        self.__sdm_dither_msb = 4
        self.__sdm_dither_addr = 0x5
        self.__sdm_stop_lsb = 5
        self.__sdm_stop_msb = 5
        self.__sdm_stop_addr = 0x5
        self.__sdm_rstb_lsb = 6
        self.__sdm_rstb_msb = 6
        self.__sdm_rstb_addr = 0x5
        self.__oc_dvdd_lsb = 0
        self.__oc_dvdd_msb = 4
        self.__oc_dvdd_addr = 0x6
        self.__oc_ref_div_lsb = 5
        self.__oc_ref_div_msb = 7
        self.__oc_ref_div_addr = 0x6
        self.__dsdm2_lsb = 0
        self.__dsdm2_msb = 5
        self.__dsdm2_addr = 0x7
        self.__dsdm1_lsb = 0
        self.__dsdm1_msb = 7
        self.__dsdm1_addr = 0x8
        self.__dsdm0_lsb = 0
        self.__dsdm0_msb = 7
        self.__dsdm0_addr = 0x9

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
    def oc_enb_fcal(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_enb_fcal_addr, self.__oc_enb_fcal_msb, self.__oc_enb_fcal_lsb)
    @oc_enb_fcal.setter
    def oc_enb_fcal(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_enb_fcal_addr, self.__oc_enb_fcal_msb, self.__oc_enb_fcal_lsb, value)

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
    def oc_lbw(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_lbw_addr, self.__oc_lbw_msb, self.__oc_lbw_lsb)
    @oc_lbw.setter
    def oc_lbw(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_lbw_addr, self.__oc_lbw_msb, self.__oc_lbw_lsb, value)

    @property
    def ir_cal_ck_div(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_cal_ck_div_addr, self.__ir_cal_ck_div_msb, self.__ir_cal_ck_div_lsb)
    @ir_cal_ck_div.setter
    def ir_cal_ck_div(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_cal_ck_div_addr, self.__ir_cal_ck_div_msb, self.__ir_cal_ck_div_lsb, value)

    @property
    def oc_dchgp(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_dchgp_addr, self.__oc_dchgp_msb, self.__oc_dchgp_lsb)
    @oc_dchgp.setter
    def oc_dchgp(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_dchgp_addr, self.__oc_dchgp_msb, self.__oc_dchgp_lsb, value)

    @property
    def oc_enb_vcon(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_enb_vcon_addr, self.__oc_enb_vcon_msb, self.__oc_enb_vcon_lsb)
    @oc_enb_vcon.setter
    def oc_enb_vcon(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_enb_vcon_addr, self.__oc_enb_vcon_msb, self.__oc_enb_vcon_lsb, value)

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
    def or_output_div(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__or_output_div_addr, self.__or_output_div_msb, self.__or_output_div_lsb)
    @or_output_div.setter
    def or_output_div(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__or_output_div_addr, self.__or_output_div_msb, self.__or_output_div_lsb, value)

    @property
    def oc_tschgp(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_tschgp_addr, self.__oc_tschgp_msb, self.__oc_tschgp_lsb)
    @oc_tschgp.setter
    def oc_tschgp(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_tschgp_addr, self.__oc_tschgp_msb, self.__oc_tschgp_lsb, value)

    @property
    def en_fast_cal(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__en_fast_cal_addr, self.__en_fast_cal_msb, self.__en_fast_cal_lsb)
    @en_fast_cal.setter
    def en_fast_cal(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__en_fast_cal_addr, self.__en_fast_cal_msb, self.__en_fast_cal_lsb, value)

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
    def sdm_dither(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sdm_dither_addr, self.__sdm_dither_msb, self.__sdm_dither_lsb)
    @sdm_dither.setter
    def sdm_dither(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sdm_dither_addr, self.__sdm_dither_msb, self.__sdm_dither_lsb, value)

    @property
    def sdm_stop(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sdm_stop_addr, self.__sdm_stop_msb, self.__sdm_stop_lsb)
    @sdm_stop.setter
    def sdm_stop(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sdm_stop_addr, self.__sdm_stop_msb, self.__sdm_stop_lsb, value)

    @property
    def sdm_rstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sdm_rstb_addr, self.__sdm_rstb_msb, self.__sdm_rstb_lsb)
    @sdm_rstb.setter
    def sdm_rstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sdm_rstb_addr, self.__sdm_rstb_msb, self.__sdm_rstb_lsb, value)

    @property
    def oc_dvdd(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_dvdd_addr, self.__oc_dvdd_msb, self.__oc_dvdd_lsb)
    @oc_dvdd.setter
    def oc_dvdd(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_dvdd_addr, self.__oc_dvdd_msb, self.__oc_dvdd_lsb, value)

    @property
    def oc_ref_div(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_ref_div_addr, self.__oc_ref_div_msb, self.__oc_ref_div_lsb)
    @oc_ref_div.setter
    def oc_ref_div(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_ref_div_addr, self.__oc_ref_div_msb, self.__oc_ref_div_lsb, value)

    @property
    def dsdm2(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dsdm2_addr, self.__dsdm2_msb, self.__dsdm2_lsb)
    @dsdm2.setter
    def dsdm2(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dsdm2_addr, self.__dsdm2_msb, self.__dsdm2_lsb, value)

    @property
    def dsdm1(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dsdm1_addr, self.__dsdm1_msb, self.__dsdm1_lsb)
    @dsdm1.setter
    def dsdm1(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dsdm1_addr, self.__dsdm1_msb, self.__dsdm1_lsb, value)

    @property
    def dsdm0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dsdm0_addr, self.__dsdm0_msb, self.__dsdm0_lsb)
    @dsdm0.setter
    def dsdm0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dsdm0_addr, self.__dsdm0_msb, self.__dsdm0_lsb, value)
