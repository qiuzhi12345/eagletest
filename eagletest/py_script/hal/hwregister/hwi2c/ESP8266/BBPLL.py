from hal.common import *
from hal.hwregister.hwi2c.ESP8266.addr_base import *
class BBPLL(object):
    def __init__(self, channel, chipv = "ESP8266"):
        self.chipv = chipv
        self.channel = channel
        self.__I2C = I2C(self.channel, self.chipv)
        self.__base = BBPLL_BASE
        self.__hostid = BBPLL_HOSTID
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
        self.__ir_cal_ck_div_lsb = 0
        self.__ir_cal_ck_div_msb = 3
        self.__ir_cal_ck_div_addr = 0x2
        self.__oc_ref_div_lsb = 5
        self.__oc_ref_div_msb = 7
        self.__oc_ref_div_addr = 0x2
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
        self.__or_div_lsb = 0
        self.__or_div_msb = 4
        self.__or_div_addr = 0x4
        self.__oc_tschgp_lsb = 5
        self.__oc_tschgp_msb = 5
        self.__oc_tschgp_addr = 0x4
        self.__oc_lbw_lsb = 6
        self.__oc_lbw_msb = 6
        self.__oc_lbw_addr = 0x4
        self.__en_audio_clock_out_lsb = 7
        self.__en_audio_clock_out_msb = 7
        self.__en_audio_clock_out_addr = 0x4
        self.__oc_dhref_sel_lsb = 0
        self.__oc_dhref_sel_msb = 1
        self.__oc_dhref_sel_addr = 0x5
        self.__oc_dlref_sel_lsb = 2
        self.__oc_dlref_sel_msb = 3
        self.__oc_dlref_sel_addr = 0x5
        self.__oc_dchgp_lsb = 4
        self.__oc_dchgp_msb = 6
        self.__oc_dchgp_addr = 0x5
        self.__oc_enb_vcon_lsb = 7
        self.__oc_enb_vcon_msb = 7
        self.__oc_enb_vcon_addr = 0x5
        self.__or_lock1_lsb = 0
        self.__or_lock1_msb = 0
        self.__or_lock1_addr = 0x6
        self.__or_lock2_lsb = 1
        self.__or_lock2_msb = 1
        self.__or_lock2_addr = 0x6
        self.__xpd_bbpll_lsb = 0
        self.__xpd_bbpll_msb = 0
        self.__xpd_bbpll_addr = 0x7
        self.__ckgen_div_lsb = 1
        self.__ckgen_div_msb = 3
        self.__ckgen_div_addr = 0x7
        self.__force_bbpll_on_lsb = 4
        self.__force_bbpll_on_msb = 4
        self.__force_bbpll_on_addr = 0x7
        self.__force_bbdiv_on_lsb = 5
        self.__force_bbdiv_on_msb = 5
        self.__force_bbdiv_on_addr = 0x7
        self.__force_bbpll_off_lsb = 6
        self.__force_bbpll_off_msb = 6
        self.__force_bbpll_off_addr = 0x7
        self.__force_bbdiv_off_lsb = 7
        self.__force_bbdiv_off_msb = 7
        self.__force_bbdiv_off_addr = 0x7

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
    def ir_cal_ck_div(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_cal_ck_div_addr, self.__ir_cal_ck_div_msb, self.__ir_cal_ck_div_lsb)
    @ir_cal_ck_div.setter
    def ir_cal_ck_div(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_cal_ck_div_addr, self.__ir_cal_ck_div_msb, self.__ir_cal_ck_div_lsb, value)

    @property
    def oc_ref_div(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_ref_div_addr, self.__oc_ref_div_msb, self.__oc_ref_div_lsb)
    @oc_ref_div.setter
    def oc_ref_div(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_ref_div_addr, self.__oc_ref_div_msb, self.__oc_ref_div_lsb, value)

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
    def or_div(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__or_div_addr, self.__or_div_msb, self.__or_div_lsb)
    @or_div.setter
    def or_div(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__or_div_addr, self.__or_div_msb, self.__or_div_lsb, value)

    @property
    def oc_tschgp(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_tschgp_addr, self.__oc_tschgp_msb, self.__oc_tschgp_lsb)
    @oc_tschgp.setter
    def oc_tschgp(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_tschgp_addr, self.__oc_tschgp_msb, self.__oc_tschgp_lsb, value)

    @property
    def oc_lbw(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__oc_lbw_addr, self.__oc_lbw_msb, self.__oc_lbw_lsb)
    @oc_lbw.setter
    def oc_lbw(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__oc_lbw_addr, self.__oc_lbw_msb, self.__oc_lbw_lsb, value)

    @property
    def en_audio_clock_out(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__en_audio_clock_out_addr, self.__en_audio_clock_out_msb, self.__en_audio_clock_out_lsb)
    @en_audio_clock_out.setter
    def en_audio_clock_out(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__en_audio_clock_out_addr, self.__en_audio_clock_out_msb, self.__en_audio_clock_out_lsb, value)

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
    def xpd_bbpll(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_bbpll_addr, self.__xpd_bbpll_msb, self.__xpd_bbpll_lsb)
    @xpd_bbpll.setter
    def xpd_bbpll(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_bbpll_addr, self.__xpd_bbpll_msb, self.__xpd_bbpll_lsb, value)

    @property
    def ckgen_div(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ckgen_div_addr, self.__ckgen_div_msb, self.__ckgen_div_lsb)
    @ckgen_div.setter
    def ckgen_div(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ckgen_div_addr, self.__ckgen_div_msb, self.__ckgen_div_lsb, value)

    @property
    def force_bbpll_on(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__force_bbpll_on_addr, self.__force_bbpll_on_msb, self.__force_bbpll_on_lsb)
    @force_bbpll_on.setter
    def force_bbpll_on(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__force_bbpll_on_addr, self.__force_bbpll_on_msb, self.__force_bbpll_on_lsb, value)

    @property
    def force_bbdiv_on(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__force_bbdiv_on_addr, self.__force_bbdiv_on_msb, self.__force_bbdiv_on_lsb)
    @force_bbdiv_on.setter
    def force_bbdiv_on(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__force_bbdiv_on_addr, self.__force_bbdiv_on_msb, self.__force_bbdiv_on_lsb, value)

    @property
    def force_bbpll_off(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__force_bbpll_off_addr, self.__force_bbpll_off_msb, self.__force_bbpll_off_lsb)
    @force_bbpll_off.setter
    def force_bbpll_off(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__force_bbpll_off_addr, self.__force_bbpll_off_msb, self.__force_bbpll_off_lsb, value)

    @property
    def force_bbdiv_off(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__force_bbdiv_off_addr, self.__force_bbdiv_off_msb, self.__force_bbdiv_off_lsb)
    @force_bbdiv_off.setter
    def force_bbdiv_off(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__force_bbdiv_off_addr, self.__force_bbdiv_off_msb, self.__force_bbdiv_off_lsb, value)
