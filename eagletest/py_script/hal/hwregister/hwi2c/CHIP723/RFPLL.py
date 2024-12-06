from hal.common import *
from hal.hwregister.hwi2c.CHIP723.addr_base import *
class RFPLL(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__I2C = I2C(self.channel, self.chipv)
        self.__base = RFPLL_BASE
        self.__hostid = RFPLL_HOSTID
        self.__ir_fcal_delay_lsb = 0
        self.__ir_fcal_delay_msb = 4
        self.__ir_fcal_delay_addr = 0x0
        self.__ir_pll_cal_rstb_lsb = 5
        self.__ir_pll_cal_rstb_msb = 5
        self.__ir_pll_cal_rstb_addr = 0x0
        self.__ir_pll_cal_start_lsb = 6
        self.__ir_pll_cal_start_msb = 6
        self.__ir_pll_cal_start_addr = 0x0
        self.__ir_pll_cal_start_delta_lsb = 7
        self.__ir_pll_cal_start_delta_msb = 7
        self.__ir_pll_cal_start_delta_addr = 0x0
        self.__ir_cap_ext_lsb = 0
        self.__ir_cap_ext_msb = 7
        self.__ir_cap_ext_addr = 0x1
        self.__ir_dac_ext_lsb = 0
        self.__ir_dac_ext_msb = 3
        self.__ir_dac_ext_addr = 0x2
        self.__ir_cap_ext_8_lsb = 4
        self.__ir_cap_ext_8_msb = 4
        self.__ir_cap_ext_8_addr = 0x2
        self.__ir_enx_dac_lsb = 7
        self.__ir_enx_dac_msb = 7
        self.__ir_enx_dac_addr = 0x2
        self.__ir_en_pll_mon_lsb = 0
        self.__ir_en_pll_mon_msb = 0
        self.__ir_en_pll_mon_addr = 0x3
        self.__ir_enb_dac_dec1_lsb = 1
        self.__ir_enb_dac_dec1_msb = 1
        self.__ir_enb_dac_dec1_addr = 0x3
        self.__ir_enb_dac_dec2_lsb = 2
        self.__ir_enb_dac_dec2_msb = 2
        self.__ir_enb_dac_dec2_addr = 0x3
        self.__ir_enb_chgp_lsb = 3
        self.__ir_enb_chgp_msb = 3
        self.__ir_enb_chgp_addr = 0x3
        self.__xpd_dac_lsb = 4
        self.__xpd_dac_msb = 4
        self.__xpd_dac_addr = 0x3
        self.__xpd_vco_lsb = 5
        self.__xpd_vco_msb = 5
        self.__xpd_vco_addr = 0x3
        self.__xpd_div_lsb = 6
        self.__xpd_div_msb = 6
        self.__xpd_div_addr = 0x3
        self.__ir_sel_fcnt_cal_lsb = 7
        self.__ir_sel_fcnt_cal_msb = 7
        self.__ir_sel_fcnt_cal_addr = 0x3
        self.__ir_ext_dchgp_lsb = 0
        self.__ir_ext_dchgp_msb = 2
        self.__ir_ext_dchgp_addr = 0x4
        self.__lf_hbw_lsb = 3
        self.__lf_hbw_msb = 3
        self.__lf_hbw_addr = 0x4
        self.__dvco_amp_lsb = 4
        self.__dvco_amp_msb = 5
        self.__dvco_amp_addr = 0x4
        self.__dvco_amp_incw_lsb = 6
        self.__dvco_amp_incw_msb = 6
        self.__dvco_amp_incw_addr = 0x4
        self.__or_pll_cap_lsb = 0
        self.__or_pll_cap_msb = 7
        self.__or_pll_cap_addr = 0x5
        self.__or_pll_dac_lsb = 0
        self.__or_pll_dac_msb = 3
        self.__or_pll_dac_addr = 0x6
        self.__or_pll_amp_end_lsb = 0
        self.__or_pll_amp_end_msb = 0
        self.__or_pll_amp_end_addr = 0x7
        self.__or_pll_cal_end_lsb = 1
        self.__or_pll_cal_end_msb = 1
        self.__or_pll_cal_end_addr = 0x7
        self.__or_pll_cap_8_lsb = 2
        self.__or_pll_cap_8_msb = 2
        self.__or_pll_cap_8_addr = 0x7
        self.__dtest_lsb = 0
        self.__dtest_msb = 1
        self.__dtest_addr = 0x8
        self.__ent_vco_lsb = 2
        self.__ent_vco_msb = 2
        self.__ent_vco_addr = 0x8
        self.__ent_vco_bias_lsb = 3
        self.__ent_vco_bias_msb = 3
        self.__ent_vco_bias_addr = 0x8
        self.__enb_open_lf_lsb = 4
        self.__enb_open_lf_msb = 4
        self.__enb_open_lf_addr = 0x8
        self.__bst_sf_lsb = 5
        self.__bst_sf_msb = 5
        self.__bst_sf_addr = 0x8
        self.__or_dvco_kvco_lsb = 6
        self.__or_dvco_kvco_msb = 7
        self.__or_dvco_kvco_addr = 0x8
        self.__ir_amplf_open_lsb = 0
        self.__ir_amplf_open_msb = 3
        self.__ir_amplf_open_addr = 0x9
        self.__ir_amplf_close_lsb = 4
        self.__ir_amplf_close_msb = 7
        self.__ir_amplf_close_addr = 0x9
        self.__dhref_lsb = 4
        self.__dhref_msb = 5
        self.__dhref_addr = 0xa
        self.__dlref_lsb = 6
        self.__dlref_msb = 7
        self.__dlref_addr = 0xa
        self.__ir_acal_delay_lsb = 0
        self.__ir_acal_delay_msb = 4
        self.__ir_acal_delay_addr = 0xb
        self.__lf_hbw_2_lsb = 5
        self.__lf_hbw_2_msb = 5
        self.__lf_hbw_2_addr = 0xb
        self.__ir_enx_cap_lsb = 6
        self.__ir_enx_cap_msb = 6
        self.__ir_enx_cap_addr = 0xb
        self.__or_ampl_lsb = 0
        self.__or_ampl_msb = 0
        self.__or_ampl_addr = 0xc
        self.__or_amph_lsb = 1
        self.__or_amph_msb = 1
        self.__or_amph_addr = 0xc
        self.__or_capl_lsb = 2
        self.__or_capl_msb = 2
        self.__or_capl_addr = 0xc
        self.__or_caph_lsb = 3
        self.__or_caph_msb = 3
        self.__or_caph_addr = 0xc

    def reg_addr_rd(self,reg_addr):
        return self.__I2C.i2c_rd(self.__base , self.__hostid ,reg_addr)
    def reg_addr_wr(self,reg_addr,value):
        return self.__I2C.i2c_wr(self.__base , self.__hostid ,reg_addr,value)

    @property
    def ir_fcal_delay(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_fcal_delay_addr, self.__ir_fcal_delay_msb, self.__ir_fcal_delay_lsb)
    @ir_fcal_delay.setter
    def ir_fcal_delay(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_fcal_delay_addr, self.__ir_fcal_delay_msb, self.__ir_fcal_delay_lsb, value)

    @property
    def ir_pll_cal_rstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_pll_cal_rstb_addr, self.__ir_pll_cal_rstb_msb, self.__ir_pll_cal_rstb_lsb)
    @ir_pll_cal_rstb.setter
    def ir_pll_cal_rstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_pll_cal_rstb_addr, self.__ir_pll_cal_rstb_msb, self.__ir_pll_cal_rstb_lsb, value)

    @property
    def ir_pll_cal_start(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_pll_cal_start_addr, self.__ir_pll_cal_start_msb, self.__ir_pll_cal_start_lsb)
    @ir_pll_cal_start.setter
    def ir_pll_cal_start(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_pll_cal_start_addr, self.__ir_pll_cal_start_msb, self.__ir_pll_cal_start_lsb, value)

    @property
    def ir_pll_cal_start_delta(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_pll_cal_start_delta_addr, self.__ir_pll_cal_start_delta_msb, self.__ir_pll_cal_start_delta_lsb)
    @ir_pll_cal_start_delta.setter
    def ir_pll_cal_start_delta(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_pll_cal_start_delta_addr, self.__ir_pll_cal_start_delta_msb, self.__ir_pll_cal_start_delta_lsb, value)

    @property
    def ir_cap_ext(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_cap_ext_addr, self.__ir_cap_ext_msb, self.__ir_cap_ext_lsb)
    @ir_cap_ext.setter
    def ir_cap_ext(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_cap_ext_addr, self.__ir_cap_ext_msb, self.__ir_cap_ext_lsb, value)

    @property
    def ir_dac_ext(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_dac_ext_addr, self.__ir_dac_ext_msb, self.__ir_dac_ext_lsb)
    @ir_dac_ext.setter
    def ir_dac_ext(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_dac_ext_addr, self.__ir_dac_ext_msb, self.__ir_dac_ext_lsb, value)

    @property
    def ir_cap_ext_8(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_cap_ext_8_addr, self.__ir_cap_ext_8_msb, self.__ir_cap_ext_8_lsb)
    @ir_cap_ext_8.setter
    def ir_cap_ext_8(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_cap_ext_8_addr, self.__ir_cap_ext_8_msb, self.__ir_cap_ext_8_lsb, value)

    @property
    def ir_enx_dac(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_enx_dac_addr, self.__ir_enx_dac_msb, self.__ir_enx_dac_lsb)
    @ir_enx_dac.setter
    def ir_enx_dac(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_enx_dac_addr, self.__ir_enx_dac_msb, self.__ir_enx_dac_lsb, value)

    @property
    def ir_en_pll_mon(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_en_pll_mon_addr, self.__ir_en_pll_mon_msb, self.__ir_en_pll_mon_lsb)
    @ir_en_pll_mon.setter
    def ir_en_pll_mon(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_en_pll_mon_addr, self.__ir_en_pll_mon_msb, self.__ir_en_pll_mon_lsb, value)

    @property
    def ir_enb_dac_dec1(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_enb_dac_dec1_addr, self.__ir_enb_dac_dec1_msb, self.__ir_enb_dac_dec1_lsb)
    @ir_enb_dac_dec1.setter
    def ir_enb_dac_dec1(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_enb_dac_dec1_addr, self.__ir_enb_dac_dec1_msb, self.__ir_enb_dac_dec1_lsb, value)

    @property
    def ir_enb_dac_dec2(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_enb_dac_dec2_addr, self.__ir_enb_dac_dec2_msb, self.__ir_enb_dac_dec2_lsb)
    @ir_enb_dac_dec2.setter
    def ir_enb_dac_dec2(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_enb_dac_dec2_addr, self.__ir_enb_dac_dec2_msb, self.__ir_enb_dac_dec2_lsb, value)

    @property
    def ir_enb_chgp(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_enb_chgp_addr, self.__ir_enb_chgp_msb, self.__ir_enb_chgp_lsb)
    @ir_enb_chgp.setter
    def ir_enb_chgp(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_enb_chgp_addr, self.__ir_enb_chgp_msb, self.__ir_enb_chgp_lsb, value)

    @property
    def xpd_dac(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_dac_addr, self.__xpd_dac_msb, self.__xpd_dac_lsb)
    @xpd_dac.setter
    def xpd_dac(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_dac_addr, self.__xpd_dac_msb, self.__xpd_dac_lsb, value)

    @property
    def xpd_vco(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_vco_addr, self.__xpd_vco_msb, self.__xpd_vco_lsb)
    @xpd_vco.setter
    def xpd_vco(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_vco_addr, self.__xpd_vco_msb, self.__xpd_vco_lsb, value)

    @property
    def xpd_div(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_div_addr, self.__xpd_div_msb, self.__xpd_div_lsb)
    @xpd_div.setter
    def xpd_div(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_div_addr, self.__xpd_div_msb, self.__xpd_div_lsb, value)

    @property
    def ir_sel_fcnt_cal(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_sel_fcnt_cal_addr, self.__ir_sel_fcnt_cal_msb, self.__ir_sel_fcnt_cal_lsb)
    @ir_sel_fcnt_cal.setter
    def ir_sel_fcnt_cal(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_sel_fcnt_cal_addr, self.__ir_sel_fcnt_cal_msb, self.__ir_sel_fcnt_cal_lsb, value)

    @property
    def ir_ext_dchgp(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_ext_dchgp_addr, self.__ir_ext_dchgp_msb, self.__ir_ext_dchgp_lsb)
    @ir_ext_dchgp.setter
    def ir_ext_dchgp(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_ext_dchgp_addr, self.__ir_ext_dchgp_msb, self.__ir_ext_dchgp_lsb, value)

    @property
    def lf_hbw(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__lf_hbw_addr, self.__lf_hbw_msb, self.__lf_hbw_lsb)
    @lf_hbw.setter
    def lf_hbw(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__lf_hbw_addr, self.__lf_hbw_msb, self.__lf_hbw_lsb, value)

    @property
    def dvco_amp(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dvco_amp_addr, self.__dvco_amp_msb, self.__dvco_amp_lsb)
    @dvco_amp.setter
    def dvco_amp(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dvco_amp_addr, self.__dvco_amp_msb, self.__dvco_amp_lsb, value)

    @property
    def dvco_amp_incw(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dvco_amp_incw_addr, self.__dvco_amp_incw_msb, self.__dvco_amp_incw_lsb)
    @dvco_amp_incw.setter
    def dvco_amp_incw(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dvco_amp_incw_addr, self.__dvco_amp_incw_msb, self.__dvco_amp_incw_lsb, value)

    @property
    def or_pll_cap(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__or_pll_cap_addr, self.__or_pll_cap_msb, self.__or_pll_cap_lsb)
    @or_pll_cap.setter
    def or_pll_cap(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__or_pll_cap_addr, self.__or_pll_cap_msb, self.__or_pll_cap_lsb, value)

    @property
    def or_pll_dac(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__or_pll_dac_addr, self.__or_pll_dac_msb, self.__or_pll_dac_lsb)
    @or_pll_dac.setter
    def or_pll_dac(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__or_pll_dac_addr, self.__or_pll_dac_msb, self.__or_pll_dac_lsb, value)

    @property
    def or_pll_amp_end(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__or_pll_amp_end_addr, self.__or_pll_amp_end_msb, self.__or_pll_amp_end_lsb)
    @or_pll_amp_end.setter
    def or_pll_amp_end(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__or_pll_amp_end_addr, self.__or_pll_amp_end_msb, self.__or_pll_amp_end_lsb, value)

    @property
    def or_pll_cal_end(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__or_pll_cal_end_addr, self.__or_pll_cal_end_msb, self.__or_pll_cal_end_lsb)
    @or_pll_cal_end.setter
    def or_pll_cal_end(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__or_pll_cal_end_addr, self.__or_pll_cal_end_msb, self.__or_pll_cal_end_lsb, value)

    @property
    def or_pll_cap_8(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__or_pll_cap_8_addr, self.__or_pll_cap_8_msb, self.__or_pll_cap_8_lsb)
    @or_pll_cap_8.setter
    def or_pll_cap_8(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__or_pll_cap_8_addr, self.__or_pll_cap_8_msb, self.__or_pll_cap_8_lsb, value)

    @property
    def dtest(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dtest_addr, self.__dtest_msb, self.__dtest_lsb)
    @dtest.setter
    def dtest(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dtest_addr, self.__dtest_msb, self.__dtest_lsb, value)

    @property
    def ent_vco(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_vco_addr, self.__ent_vco_msb, self.__ent_vco_lsb)
    @ent_vco.setter
    def ent_vco(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_vco_addr, self.__ent_vco_msb, self.__ent_vco_lsb, value)

    @property
    def ent_vco_bias(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_vco_bias_addr, self.__ent_vco_bias_msb, self.__ent_vco_bias_lsb)
    @ent_vco_bias.setter
    def ent_vco_bias(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_vco_bias_addr, self.__ent_vco_bias_msb, self.__ent_vco_bias_lsb, value)

    @property
    def enb_open_lf(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__enb_open_lf_addr, self.__enb_open_lf_msb, self.__enb_open_lf_lsb)
    @enb_open_lf.setter
    def enb_open_lf(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__enb_open_lf_addr, self.__enb_open_lf_msb, self.__enb_open_lf_lsb, value)

    @property
    def bst_sf(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__bst_sf_addr, self.__bst_sf_msb, self.__bst_sf_lsb)
    @bst_sf.setter
    def bst_sf(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__bst_sf_addr, self.__bst_sf_msb, self.__bst_sf_lsb, value)

    @property
    def or_dvco_kvco(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__or_dvco_kvco_addr, self.__or_dvco_kvco_msb, self.__or_dvco_kvco_lsb)
    @or_dvco_kvco.setter
    def or_dvco_kvco(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__or_dvco_kvco_addr, self.__or_dvco_kvco_msb, self.__or_dvco_kvco_lsb, value)

    @property
    def ir_amplf_open(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_amplf_open_addr, self.__ir_amplf_open_msb, self.__ir_amplf_open_lsb)
    @ir_amplf_open.setter
    def ir_amplf_open(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_amplf_open_addr, self.__ir_amplf_open_msb, self.__ir_amplf_open_lsb, value)

    @property
    def ir_amplf_close(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_amplf_close_addr, self.__ir_amplf_close_msb, self.__ir_amplf_close_lsb)
    @ir_amplf_close.setter
    def ir_amplf_close(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_amplf_close_addr, self.__ir_amplf_close_msb, self.__ir_amplf_close_lsb, value)

    @property
    def dhref(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dhref_addr, self.__dhref_msb, self.__dhref_lsb)
    @dhref.setter
    def dhref(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dhref_addr, self.__dhref_msb, self.__dhref_lsb, value)

    @property
    def dlref(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dlref_addr, self.__dlref_msb, self.__dlref_lsb)
    @dlref.setter
    def dlref(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dlref_addr, self.__dlref_msb, self.__dlref_lsb, value)

    @property
    def ir_acal_delay(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_acal_delay_addr, self.__ir_acal_delay_msb, self.__ir_acal_delay_lsb)
    @ir_acal_delay.setter
    def ir_acal_delay(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_acal_delay_addr, self.__ir_acal_delay_msb, self.__ir_acal_delay_lsb, value)

    @property
    def lf_hbw_2(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__lf_hbw_2_addr, self.__lf_hbw_2_msb, self.__lf_hbw_2_lsb)
    @lf_hbw_2.setter
    def lf_hbw_2(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__lf_hbw_2_addr, self.__lf_hbw_2_msb, self.__lf_hbw_2_lsb, value)

    @property
    def ir_enx_cap(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_enx_cap_addr, self.__ir_enx_cap_msb, self.__ir_enx_cap_lsb)
    @ir_enx_cap.setter
    def ir_enx_cap(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_enx_cap_addr, self.__ir_enx_cap_msb, self.__ir_enx_cap_lsb, value)

    @property
    def or_ampl(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__or_ampl_addr, self.__or_ampl_msb, self.__or_ampl_lsb)
    @or_ampl.setter
    def or_ampl(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__or_ampl_addr, self.__or_ampl_msb, self.__or_ampl_lsb, value)

    @property
    def or_amph(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__or_amph_addr, self.__or_amph_msb, self.__or_amph_lsb)
    @or_amph.setter
    def or_amph(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__or_amph_addr, self.__or_amph_msb, self.__or_amph_lsb, value)

    @property
    def or_capl(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__or_capl_addr, self.__or_capl_msb, self.__or_capl_lsb)
    @or_capl.setter
    def or_capl(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__or_capl_addr, self.__or_capl_msb, self.__or_capl_lsb, value)

    @property
    def or_caph(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__or_caph_addr, self.__or_caph_msb, self.__or_caph_lsb)
    @or_caph.setter
    def or_caph(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__or_caph_addr, self.__or_caph_msb, self.__or_caph_lsb, value)
