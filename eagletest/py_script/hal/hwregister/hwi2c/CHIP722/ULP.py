from hal.common import *
from hal.hwregister.hwi2c.CHIP722.addr_base import *
class ULP(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__I2C = I2C(self.channel, self.chipv)
        self.__base = ULP_BASE
        self.__hostid = ULP_HOSTID
        self.__ir_resetb_lsb = 0
        self.__ir_resetb_msb = 0
        self.__ir_resetb_addr = 0x0
        self.__ir_start_lsb = 1
        self.__ir_start_msb = 1
        self.__ir_start_addr = 0x0
        self.__ir_force_xpd_ck_lsb = 2
        self.__ir_force_xpd_ck_msb = 2
        self.__ir_force_xpd_ck_addr = 0x0
        self.__ir_force_xpd_ref_out_buf_lsb = 3
        self.__ir_force_xpd_ref_out_buf_msb = 3
        self.__ir_force_xpd_ref_out_buf_addr = 0x0
        self.__ir_force_xpd_iph_lsb = 4
        self.__ir_force_xpd_iph_msb = 4
        self.__ir_force_xpd_iph_addr = 0x0
        self.__ir_force_xpd_vgate_buf_lsb = 5
        self.__ir_force_xpd_vgate_buf_msb = 5
        self.__ir_force_xpd_vgate_buf_addr = 0x0
        self.__ir_disable_watchdog_ck_lsb = 6
        self.__ir_disable_watchdog_ck_msb = 6
        self.__ir_disable_watchdog_ck_addr = 0x0
        self.__bg_i_smp_period_lsb = 0
        self.__bg_i_smp_period_msb = 4
        self.__bg_i_smp_period_addr = 0x1
        self.__i_smp_period_lsb = 0
        self.__i_smp_period_msb = 4
        self.__i_smp_period_addr = 0x2
        self.__o_done_flag_lsb = 0
        self.__o_done_flag_msb = 0
        self.__o_done_flag_addr = 0x3
        self.__o_udf_lsb = 1
        self.__o_udf_msb = 1
        self.__o_udf_addr = 0x3
        self.__o_ovf_lsb = 2
        self.__o_ovf_msb = 2
        self.__o_ovf_addr = 0x3
        self.__bg_o_done_flag_lsb = 3
        self.__bg_o_done_flag_msb = 3
        self.__bg_o_done_flag_addr = 0x3
        self.__bg_o_udf_lsb = 4
        self.__bg_o_udf_msb = 4
        self.__bg_o_udf_addr = 0x3
        self.__bg_o_ovf_lsb = 5
        self.__bg_o_ovf_msb = 5
        self.__bg_o_ovf_addr = 0x3
        self.__vdda_2p0_rdy_lsb = 6
        self.__vdda_2p0_rdy_msb = 6
        self.__vdda_2p0_rdy_addr = 0x3
        self.__o_code_lsb = 0
        self.__o_code_msb = 7
        self.__o_code_addr = 0x4
        self.__dbrown_out_thres_lsb = 0
        self.__dbrown_out_thres_msb = 2
        self.__dbrown_out_thres_addr = 0x5
        self.__ir_force_pd_ref_out_buf_lsb = 3
        self.__ir_force_pd_ref_out_buf_msb = 3
        self.__ir_force_pd_ref_out_buf_addr = 0x5
        self.__ir_force_pd_iph_lsb = 4
        self.__ir_force_pd_iph_msb = 4
        self.__ir_force_pd_iph_addr = 0x5
        self.__ir_force_pd_vgate_buf_lsb = 5
        self.__ir_force_pd_vgate_buf_msb = 5
        self.__ir_force_pd_vgate_buf_addr = 0x5
        self.__ir_force_code_lsb = 6
        self.__ir_force_code_msb = 6
        self.__ir_force_code_addr = 0x5
        self.__ir_xpd_vdda_det_2p0_lsb = 7
        self.__ir_xpd_vdda_det_2p0_msb = 7
        self.__ir_xpd_vdda_det_2p0_addr = 0x5
        self.__ext_code_lsb = 0
        self.__ext_code_msb = 7
        self.__ext_code_addr = 0x6
        self.__xtal_dac_lsb = 0
        self.__xtal_dac_msb = 3
        self.__xtal_dac_addr = 0x7
        self.__xpd_xtal_lsb = 0
        self.__xpd_xtal_msb = 0
        self.__xpd_xtal_addr = 0x8
        self.__xpd_xtal_buf_lsb = 1
        self.__xpd_xtal_buf_msb = 1
        self.__xpd_xtal_buf_addr = 0x8
        self.__xpd_rc_ck_lsb = 2
        self.__xpd_rc_ck_msb = 2
        self.__xpd_rc_ck_addr = 0x8
        self.__xtal_dphase_lsb = 3
        self.__xtal_dphase_msb = 3
        self.__xtal_dphase_addr = 0x8

    def reg_addr_rd(self,reg_addr):
        return self.__I2C.i2c_rd(self.__base , self.__hostid ,reg_addr)
    def reg_addr_wr(self,reg_addr,value):
        return self.__I2C.i2c_wr(self.__base , self.__hostid ,reg_addr,value)

    @property
    def ir_resetb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_resetb_addr, self.__ir_resetb_msb, self.__ir_resetb_lsb)
    @ir_resetb.setter
    def ir_resetb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_resetb_addr, self.__ir_resetb_msb, self.__ir_resetb_lsb, value)

    @property
    def ir_start(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_start_addr, self.__ir_start_msb, self.__ir_start_lsb)
    @ir_start.setter
    def ir_start(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_start_addr, self.__ir_start_msb, self.__ir_start_lsb, value)

    @property
    def ir_force_xpd_ck(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_force_xpd_ck_addr, self.__ir_force_xpd_ck_msb, self.__ir_force_xpd_ck_lsb)
    @ir_force_xpd_ck.setter
    def ir_force_xpd_ck(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_force_xpd_ck_addr, self.__ir_force_xpd_ck_msb, self.__ir_force_xpd_ck_lsb, value)

    @property
    def ir_force_xpd_ref_out_buf(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_force_xpd_ref_out_buf_addr, self.__ir_force_xpd_ref_out_buf_msb, self.__ir_force_xpd_ref_out_buf_lsb)
    @ir_force_xpd_ref_out_buf.setter
    def ir_force_xpd_ref_out_buf(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_force_xpd_ref_out_buf_addr, self.__ir_force_xpd_ref_out_buf_msb, self.__ir_force_xpd_ref_out_buf_lsb, value)

    @property
    def ir_force_xpd_iph(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_force_xpd_iph_addr, self.__ir_force_xpd_iph_msb, self.__ir_force_xpd_iph_lsb)
    @ir_force_xpd_iph.setter
    def ir_force_xpd_iph(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_force_xpd_iph_addr, self.__ir_force_xpd_iph_msb, self.__ir_force_xpd_iph_lsb, value)

    @property
    def ir_force_xpd_vgate_buf(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_force_xpd_vgate_buf_addr, self.__ir_force_xpd_vgate_buf_msb, self.__ir_force_xpd_vgate_buf_lsb)
    @ir_force_xpd_vgate_buf.setter
    def ir_force_xpd_vgate_buf(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_force_xpd_vgate_buf_addr, self.__ir_force_xpd_vgate_buf_msb, self.__ir_force_xpd_vgate_buf_lsb, value)

    @property
    def ir_disable_watchdog_ck(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_disable_watchdog_ck_addr, self.__ir_disable_watchdog_ck_msb, self.__ir_disable_watchdog_ck_lsb)
    @ir_disable_watchdog_ck.setter
    def ir_disable_watchdog_ck(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_disable_watchdog_ck_addr, self.__ir_disable_watchdog_ck_msb, self.__ir_disable_watchdog_ck_lsb, value)

    @property
    def bg_i_smp_period(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__bg_i_smp_period_addr, self.__bg_i_smp_period_msb, self.__bg_i_smp_period_lsb)
    @bg_i_smp_period.setter
    def bg_i_smp_period(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__bg_i_smp_period_addr, self.__bg_i_smp_period_msb, self.__bg_i_smp_period_lsb, value)

    @property
    def i_smp_period(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__i_smp_period_addr, self.__i_smp_period_msb, self.__i_smp_period_lsb)
    @i_smp_period.setter
    def i_smp_period(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__i_smp_period_addr, self.__i_smp_period_msb, self.__i_smp_period_lsb, value)

    @property
    def o_done_flag(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__o_done_flag_addr, self.__o_done_flag_msb, self.__o_done_flag_lsb)
    @o_done_flag.setter
    def o_done_flag(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__o_done_flag_addr, self.__o_done_flag_msb, self.__o_done_flag_lsb, value)

    @property
    def o_udf(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__o_udf_addr, self.__o_udf_msb, self.__o_udf_lsb)
    @o_udf.setter
    def o_udf(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__o_udf_addr, self.__o_udf_msb, self.__o_udf_lsb, value)

    @property
    def o_ovf(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__o_ovf_addr, self.__o_ovf_msb, self.__o_ovf_lsb)
    @o_ovf.setter
    def o_ovf(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__o_ovf_addr, self.__o_ovf_msb, self.__o_ovf_lsb, value)

    @property
    def bg_o_done_flag(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__bg_o_done_flag_addr, self.__bg_o_done_flag_msb, self.__bg_o_done_flag_lsb)
    @bg_o_done_flag.setter
    def bg_o_done_flag(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__bg_o_done_flag_addr, self.__bg_o_done_flag_msb, self.__bg_o_done_flag_lsb, value)

    @property
    def bg_o_udf(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__bg_o_udf_addr, self.__bg_o_udf_msb, self.__bg_o_udf_lsb)
    @bg_o_udf.setter
    def bg_o_udf(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__bg_o_udf_addr, self.__bg_o_udf_msb, self.__bg_o_udf_lsb, value)

    @property
    def bg_o_ovf(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__bg_o_ovf_addr, self.__bg_o_ovf_msb, self.__bg_o_ovf_lsb)
    @bg_o_ovf.setter
    def bg_o_ovf(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__bg_o_ovf_addr, self.__bg_o_ovf_msb, self.__bg_o_ovf_lsb, value)

    @property
    def vdda_2p0_rdy(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__vdda_2p0_rdy_addr, self.__vdda_2p0_rdy_msb, self.__vdda_2p0_rdy_lsb)
    @vdda_2p0_rdy.setter
    def vdda_2p0_rdy(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__vdda_2p0_rdy_addr, self.__vdda_2p0_rdy_msb, self.__vdda_2p0_rdy_lsb, value)

    @property
    def o_code(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__o_code_addr, self.__o_code_msb, self.__o_code_lsb)
    @o_code.setter
    def o_code(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__o_code_addr, self.__o_code_msb, self.__o_code_lsb, value)

    @property
    def dbrown_out_thres(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dbrown_out_thres_addr, self.__dbrown_out_thres_msb, self.__dbrown_out_thres_lsb)
    @dbrown_out_thres.setter
    def dbrown_out_thres(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dbrown_out_thres_addr, self.__dbrown_out_thres_msb, self.__dbrown_out_thres_lsb, value)

    @property
    def ir_force_pd_ref_out_buf(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_force_pd_ref_out_buf_addr, self.__ir_force_pd_ref_out_buf_msb, self.__ir_force_pd_ref_out_buf_lsb)
    @ir_force_pd_ref_out_buf.setter
    def ir_force_pd_ref_out_buf(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_force_pd_ref_out_buf_addr, self.__ir_force_pd_ref_out_buf_msb, self.__ir_force_pd_ref_out_buf_lsb, value)

    @property
    def ir_force_pd_iph(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_force_pd_iph_addr, self.__ir_force_pd_iph_msb, self.__ir_force_pd_iph_lsb)
    @ir_force_pd_iph.setter
    def ir_force_pd_iph(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_force_pd_iph_addr, self.__ir_force_pd_iph_msb, self.__ir_force_pd_iph_lsb, value)

    @property
    def ir_force_pd_vgate_buf(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_force_pd_vgate_buf_addr, self.__ir_force_pd_vgate_buf_msb, self.__ir_force_pd_vgate_buf_lsb)
    @ir_force_pd_vgate_buf.setter
    def ir_force_pd_vgate_buf(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_force_pd_vgate_buf_addr, self.__ir_force_pd_vgate_buf_msb, self.__ir_force_pd_vgate_buf_lsb, value)

    @property
    def ir_force_code(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_force_code_addr, self.__ir_force_code_msb, self.__ir_force_code_lsb)
    @ir_force_code.setter
    def ir_force_code(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_force_code_addr, self.__ir_force_code_msb, self.__ir_force_code_lsb, value)

    @property
    def ir_xpd_vdda_det_2p0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ir_xpd_vdda_det_2p0_addr, self.__ir_xpd_vdda_det_2p0_msb, self.__ir_xpd_vdda_det_2p0_lsb)
    @ir_xpd_vdda_det_2p0.setter
    def ir_xpd_vdda_det_2p0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ir_xpd_vdda_det_2p0_addr, self.__ir_xpd_vdda_det_2p0_msb, self.__ir_xpd_vdda_det_2p0_lsb, value)

    @property
    def ext_code(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ext_code_addr, self.__ext_code_msb, self.__ext_code_lsb)
    @ext_code.setter
    def ext_code(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ext_code_addr, self.__ext_code_msb, self.__ext_code_lsb, value)

    @property
    def xtal_dac(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xtal_dac_addr, self.__xtal_dac_msb, self.__xtal_dac_lsb)
    @xtal_dac.setter
    def xtal_dac(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xtal_dac_addr, self.__xtal_dac_msb, self.__xtal_dac_lsb, value)

    @property
    def xpd_xtal(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_xtal_addr, self.__xpd_xtal_msb, self.__xpd_xtal_lsb)
    @xpd_xtal.setter
    def xpd_xtal(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_xtal_addr, self.__xpd_xtal_msb, self.__xpd_xtal_lsb, value)

    @property
    def xpd_xtal_buf(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_xtal_buf_addr, self.__xpd_xtal_buf_msb, self.__xpd_xtal_buf_lsb)
    @xpd_xtal_buf.setter
    def xpd_xtal_buf(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_xtal_buf_addr, self.__xpd_xtal_buf_msb, self.__xpd_xtal_buf_lsb, value)

    @property
    def xpd_rc_ck(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_rc_ck_addr, self.__xpd_rc_ck_msb, self.__xpd_rc_ck_lsb)
    @xpd_rc_ck.setter
    def xpd_rc_ck(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_rc_ck_addr, self.__xpd_rc_ck_msb, self.__xpd_rc_ck_lsb, value)

    @property
    def xtal_dphase(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xtal_dphase_addr, self.__xtal_dphase_msb, self.__xtal_dphase_lsb)
    @xtal_dphase.setter
    def xtal_dphase(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xtal_dphase_addr, self.__xtal_dphase_msb, self.__xtal_dphase_lsb, value)
