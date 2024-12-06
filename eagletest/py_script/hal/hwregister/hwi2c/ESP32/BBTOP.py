from hal.common import *
from hal.hwregister.hwi2c.ESP32.addr_base import *
class BBTOP(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__I2C = I2C(self.channel, self.chipv)
        self.__base = BBTOP_BASE
        self.__hostid = BBTOP_HOSTID
        self.__filter_dtest_lsb = 0
        self.__filter_dtest_msb = 1
        self.__filter_dtest_addr = 0x0
        self.__ent_filter_i_lsb = 2
        self.__ent_filter_i_msb = 2
        self.__ent_filter_i_addr = 0x0
        self.__ent_filter_q_lsb = 3
        self.__ent_filter_q_msb = 3
        self.__ent_filter_q_addr = 0x0
        self.__ent_filter_bias_i_lsb = 4
        self.__ent_filter_bias_i_msb = 4
        self.__ent_filter_bias_i_addr = 0x0
        self.__ent_filter_bias_q_lsb = 5
        self.__ent_filter_bias_q_msb = 5
        self.__ent_filter_bias_q_addr = 0x0
        self.__enlb_lsb = 6
        self.__enlb_msb = 6
        self.__enlb_addr = 0x0
        self.__filter_wifirx_dcap_lq_lsb = 0
        self.__filter_wifirx_dcap_lq_msb = 6
        self.__filter_wifirx_dcap_lq_addr = 0x1
        self.__BBADC_TMODE_I_lsb = 7
        self.__BBADC_TMODE_I_msb = 7
        self.__BBADC_TMODE_I_addr = 0x1
        self.__filter_wifirx_dcap_hq_lsb = 0
        self.__filter_wifirx_dcap_hq_msb = 6
        self.__filter_wifirx_dcap_hq_addr = 0x2
        self.__BBADC_TMODE_Q_lsb = 7
        self.__BBADC_TMODE_Q_msb = 7
        self.__BBADC_TMODE_Q_addr = 0x2
        self.__filter_wifitx_dcap_lq_lsb = 0
        self.__filter_wifitx_dcap_lq_msb = 6
        self.__filter_wifitx_dcap_lq_addr = 0x3
        self.__nc3_lsb = 7
        self.__nc3_msb = 7
        self.__nc3_addr = 0x3
        self.__filter_wifitx_dcap_hq_lsb = 0
        self.__filter_wifitx_dcap_hq_msb = 6
        self.__filter_wifitx_dcap_hq_addr = 0x4
        self.__nc4_lsb = 7
        self.__nc4_msb = 7
        self.__nc4_addr = 0x4
        self.__filter_btrx_dcap_lq_lsb = 0
        self.__filter_btrx_dcap_lq_msb = 6
        self.__filter_btrx_dcap_lq_addr = 0x5
        self.__nc5_lsb = 7
        self.__nc5_msb = 7
        self.__nc5_addr = 0x5
        self.__filter_btrx_dcap_hq_lsb = 0
        self.__filter_btrx_dcap_hq_msb = 6
        self.__filter_btrx_dcap_hq_addr = 0x6
        self.__nc6_lsb = 7
        self.__nc6_msb = 7
        self.__nc6_addr = 0x6
        self.__filter_bttx_dcap_lq_lsb = 0
        self.__filter_bttx_dcap_lq_msb = 6
        self.__filter_bttx_dcap_lq_addr = 0x7
        self.__nc7_lsb = 7
        self.__nc7_msb = 7
        self.__nc7_addr = 0x7
        self.__filter_bttx_dcap_hq_lsb = 0
        self.__filter_bttx_dcap_hq_msb = 6
        self.__filter_bttx_dcap_hq_addr = 0x8
        self.__nc8_lsb = 7
        self.__nc8_msb = 7
        self.__nc8_addr = 0x8
        self.__filter_wifirx_dgdc_lsb = 0
        self.__filter_wifirx_dgdc_msb = 0
        self.__filter_wifirx_dgdc_addr = 0x9
        self.__filter_wifirx_input_ld_lsb = 1
        self.__filter_wifirx_input_ld_msb = 2
        self.__filter_wifirx_input_ld_addr = 0x9
        self.__filter_wifirx_bstb_lsb = 3
        self.__filter_wifirx_bstb_msb = 4
        self.__filter_wifirx_bstb_addr = 0x9
        self.__filter_wifirx_dedge_lsb = 5
        self.__filter_wifirx_dedge_msb = 7
        self.__filter_wifirx_dedge_addr = 0x9
        self.__filter_wifitx_dgdc_lsb = 0
        self.__filter_wifitx_dgdc_msb = 0
        self.__filter_wifitx_dgdc_addr = 0xa
        self.__filter_wifitx_input_ld_lsb = 1
        self.__filter_wifitx_input_ld_msb = 2
        self.__filter_wifitx_input_ld_addr = 0xa
        self.__filter_wifitx_bstb_lsb = 3
        self.__filter_wifitx_bstb_msb = 4
        self.__filter_wifitx_bstb_addr = 0xa
        self.__filter_wifitx_dedge_lsb = 5
        self.__filter_wifitx_dedge_msb = 7
        self.__filter_wifitx_dedge_addr = 0xa
        self.__filter_btrx_dgdc_lsb = 0
        self.__filter_btrx_dgdc_msb = 0
        self.__filter_btrx_dgdc_addr = 0xb
        self.__filter_btrx_input_ld_lsb = 1
        self.__filter_btrx_input_ld_msb = 2
        self.__filter_btrx_input_ld_addr = 0xb
        self.__filter_btrx_bstb_lsb = 3
        self.__filter_btrx_bstb_msb = 4
        self.__filter_btrx_bstb_addr = 0xb
        self.__filter_btrx_dedge_lsb = 5
        self.__filter_btrx_dedge_msb = 7
        self.__filter_btrx_dedge_addr = 0xb
        self.__filter_bttx_dgdc_lsb = 0
        self.__filter_bttx_dgdc_msb = 0
        self.__filter_bttx_dgdc_addr = 0xc
        self.__filter_bttx_input_ld_lsb = 1
        self.__filter_bttx_input_ld_msb = 2
        self.__filter_bttx_input_ld_addr = 0xc
        self.__filter_bttx_bstb_lsb = 3
        self.__filter_bttx_bstb_msb = 4
        self.__filter_bttx_bstb_addr = 0xc
        self.__filter_bttx_dedge_lsb = 5
        self.__filter_bttx_dedge_msb = 7
        self.__filter_bttx_dedge_addr = 0xc
        self.__tmx_lbd1_lsb = 0
        self.__tmx_lbd1_msb = 3
        self.__tmx_lbd1_addr = 0xd
        self.__tmx_lbd2_lsb = 4
        self.__tmx_lbd2_msb = 7
        self.__tmx_lbd2_addr = 0xd
        self.__tmx_dsw_bias_lsb = 0
        self.__tmx_dsw_bias_msb = 1
        self.__tmx_dsw_bias_addr = 0xe
        self.__tmx_dv2i_bias_lsb = 2
        self.__tmx_dv2i_bias_msb = 3
        self.__tmx_dv2i_bias_addr = 0xe
        self.__dac_ck_ph_inv_lsb = 4
        self.__dac_ck_ph_inv_msb = 4
        self.__dac_ck_ph_inv_addr = 0xe
        self.__filter_xpd_lat_lsb = 5
        self.__filter_xpd_lat_msb = 5
        self.__filter_xpd_lat_addr = 0xe
        self.__nc9_lsb = 6
        self.__nc9_msb = 7
        self.__nc9_addr = 0xe
        self.__filter_cmplx_ctrl_lsb = 0
        self.__filter_cmplx_ctrl_msb = 2
        self.__filter_cmplx_ctrl_addr = 0xf
        self.__encmplx_btrx_lsb = 3
        self.__encmplx_btrx_msb = 3
        self.__encmplx_btrx_addr = 0xf
        self.__encmplx_bttx_lsb = 4
        self.__encmplx_bttx_msb = 4
        self.__encmplx_bttx_addr = 0xf
        self.__nc10_lsb = 5
        self.__nc10_msb = 7
        self.__nc10_addr = 0xf

    def reg_addr_rd(self,reg_addr):
        return self.__I2C.i2c_rd(self.__base , self.__hostid ,reg_addr)
    def reg_addr_wr(self,reg_addr,value):
        return self.__I2C.i2c_wr(self.__base , self.__hostid ,reg_addr,value)

    @property
    def filter_dtest(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_dtest_addr, self.__filter_dtest_msb, self.__filter_dtest_lsb)
    @filter_dtest.setter
    def filter_dtest(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_dtest_addr, self.__filter_dtest_msb, self.__filter_dtest_lsb, value)

    @property
    def ent_filter_i(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_filter_i_addr, self.__ent_filter_i_msb, self.__ent_filter_i_lsb)
    @ent_filter_i.setter
    def ent_filter_i(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_filter_i_addr, self.__ent_filter_i_msb, self.__ent_filter_i_lsb, value)

    @property
    def ent_filter_q(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_filter_q_addr, self.__ent_filter_q_msb, self.__ent_filter_q_lsb)
    @ent_filter_q.setter
    def ent_filter_q(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_filter_q_addr, self.__ent_filter_q_msb, self.__ent_filter_q_lsb, value)

    @property
    def ent_filter_bias_i(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_filter_bias_i_addr, self.__ent_filter_bias_i_msb, self.__ent_filter_bias_i_lsb)
    @ent_filter_bias_i.setter
    def ent_filter_bias_i(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_filter_bias_i_addr, self.__ent_filter_bias_i_msb, self.__ent_filter_bias_i_lsb, value)

    @property
    def ent_filter_bias_q(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_filter_bias_q_addr, self.__ent_filter_bias_q_msb, self.__ent_filter_bias_q_lsb)
    @ent_filter_bias_q.setter
    def ent_filter_bias_q(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_filter_bias_q_addr, self.__ent_filter_bias_q_msb, self.__ent_filter_bias_q_lsb, value)

    @property
    def enlb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__enlb_addr, self.__enlb_msb, self.__enlb_lsb)
    @enlb.setter
    def enlb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__enlb_addr, self.__enlb_msb, self.__enlb_lsb, value)

    @property
    def filter_wifirx_dcap_lq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wifirx_dcap_lq_addr, self.__filter_wifirx_dcap_lq_msb, self.__filter_wifirx_dcap_lq_lsb)
    @filter_wifirx_dcap_lq.setter
    def filter_wifirx_dcap_lq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wifirx_dcap_lq_addr, self.__filter_wifirx_dcap_lq_msb, self.__filter_wifirx_dcap_lq_lsb, value)

    @property
    def BBADC_TMODE_I(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__BBADC_TMODE_I_addr, self.__BBADC_TMODE_I_msb, self.__BBADC_TMODE_I_lsb)
    @BBADC_TMODE_I.setter
    def BBADC_TMODE_I(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__BBADC_TMODE_I_addr, self.__BBADC_TMODE_I_msb, self.__BBADC_TMODE_I_lsb, value)

    @property
    def filter_wifirx_dcap_hq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wifirx_dcap_hq_addr, self.__filter_wifirx_dcap_hq_msb, self.__filter_wifirx_dcap_hq_lsb)
    @filter_wifirx_dcap_hq.setter
    def filter_wifirx_dcap_hq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wifirx_dcap_hq_addr, self.__filter_wifirx_dcap_hq_msb, self.__filter_wifirx_dcap_hq_lsb, value)

    @property
    def BBADC_TMODE_Q(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__BBADC_TMODE_Q_addr, self.__BBADC_TMODE_Q_msb, self.__BBADC_TMODE_Q_lsb)
    @BBADC_TMODE_Q.setter
    def BBADC_TMODE_Q(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__BBADC_TMODE_Q_addr, self.__BBADC_TMODE_Q_msb, self.__BBADC_TMODE_Q_lsb, value)

    @property
    def filter_wifitx_dcap_lq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wifitx_dcap_lq_addr, self.__filter_wifitx_dcap_lq_msb, self.__filter_wifitx_dcap_lq_lsb)
    @filter_wifitx_dcap_lq.setter
    def filter_wifitx_dcap_lq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wifitx_dcap_lq_addr, self.__filter_wifitx_dcap_lq_msb, self.__filter_wifitx_dcap_lq_lsb, value)

    @property
    def nc3(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__nc3_addr, self.__nc3_msb, self.__nc3_lsb)
    @nc3.setter
    def nc3(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__nc3_addr, self.__nc3_msb, self.__nc3_lsb, value)

    @property
    def filter_wifitx_dcap_hq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wifitx_dcap_hq_addr, self.__filter_wifitx_dcap_hq_msb, self.__filter_wifitx_dcap_hq_lsb)
    @filter_wifitx_dcap_hq.setter
    def filter_wifitx_dcap_hq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wifitx_dcap_hq_addr, self.__filter_wifitx_dcap_hq_msb, self.__filter_wifitx_dcap_hq_lsb, value)

    @property
    def nc4(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__nc4_addr, self.__nc4_msb, self.__nc4_lsb)
    @nc4.setter
    def nc4(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__nc4_addr, self.__nc4_msb, self.__nc4_lsb, value)

    @property
    def filter_btrx_dcap_lq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx_dcap_lq_addr, self.__filter_btrx_dcap_lq_msb, self.__filter_btrx_dcap_lq_lsb)
    @filter_btrx_dcap_lq.setter
    def filter_btrx_dcap_lq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx_dcap_lq_addr, self.__filter_btrx_dcap_lq_msb, self.__filter_btrx_dcap_lq_lsb, value)

    @property
    def nc5(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__nc5_addr, self.__nc5_msb, self.__nc5_lsb)
    @nc5.setter
    def nc5(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__nc5_addr, self.__nc5_msb, self.__nc5_lsb, value)

    @property
    def filter_btrx_dcap_hq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx_dcap_hq_addr, self.__filter_btrx_dcap_hq_msb, self.__filter_btrx_dcap_hq_lsb)
    @filter_btrx_dcap_hq.setter
    def filter_btrx_dcap_hq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx_dcap_hq_addr, self.__filter_btrx_dcap_hq_msb, self.__filter_btrx_dcap_hq_lsb, value)

    @property
    def nc6(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__nc6_addr, self.__nc6_msb, self.__nc6_lsb)
    @nc6.setter
    def nc6(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__nc6_addr, self.__nc6_msb, self.__nc6_lsb, value)

    @property
    def filter_bttx_dcap_lq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx_dcap_lq_addr, self.__filter_bttx_dcap_lq_msb, self.__filter_bttx_dcap_lq_lsb)
    @filter_bttx_dcap_lq.setter
    def filter_bttx_dcap_lq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx_dcap_lq_addr, self.__filter_bttx_dcap_lq_msb, self.__filter_bttx_dcap_lq_lsb, value)

    @property
    def nc7(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__nc7_addr, self.__nc7_msb, self.__nc7_lsb)
    @nc7.setter
    def nc7(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__nc7_addr, self.__nc7_msb, self.__nc7_lsb, value)

    @property
    def filter_bttx_dcap_hq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx_dcap_hq_addr, self.__filter_bttx_dcap_hq_msb, self.__filter_bttx_dcap_hq_lsb)
    @filter_bttx_dcap_hq.setter
    def filter_bttx_dcap_hq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx_dcap_hq_addr, self.__filter_bttx_dcap_hq_msb, self.__filter_bttx_dcap_hq_lsb, value)

    @property
    def nc8(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__nc8_addr, self.__nc8_msb, self.__nc8_lsb)
    @nc8.setter
    def nc8(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__nc8_addr, self.__nc8_msb, self.__nc8_lsb, value)

    @property
    def filter_wifirx_dgdc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wifirx_dgdc_addr, self.__filter_wifirx_dgdc_msb, self.__filter_wifirx_dgdc_lsb)
    @filter_wifirx_dgdc.setter
    def filter_wifirx_dgdc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wifirx_dgdc_addr, self.__filter_wifirx_dgdc_msb, self.__filter_wifirx_dgdc_lsb, value)

    @property
    def filter_wifirx_input_ld(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wifirx_input_ld_addr, self.__filter_wifirx_input_ld_msb, self.__filter_wifirx_input_ld_lsb)
    @filter_wifirx_input_ld.setter
    def filter_wifirx_input_ld(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wifirx_input_ld_addr, self.__filter_wifirx_input_ld_msb, self.__filter_wifirx_input_ld_lsb, value)

    @property
    def filter_wifirx_bstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wifirx_bstb_addr, self.__filter_wifirx_bstb_msb, self.__filter_wifirx_bstb_lsb)
    @filter_wifirx_bstb.setter
    def filter_wifirx_bstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wifirx_bstb_addr, self.__filter_wifirx_bstb_msb, self.__filter_wifirx_bstb_lsb, value)

    @property
    def filter_wifirx_dedge(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wifirx_dedge_addr, self.__filter_wifirx_dedge_msb, self.__filter_wifirx_dedge_lsb)
    @filter_wifirx_dedge.setter
    def filter_wifirx_dedge(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wifirx_dedge_addr, self.__filter_wifirx_dedge_msb, self.__filter_wifirx_dedge_lsb, value)

    @property
    def filter_wifitx_dgdc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wifitx_dgdc_addr, self.__filter_wifitx_dgdc_msb, self.__filter_wifitx_dgdc_lsb)
    @filter_wifitx_dgdc.setter
    def filter_wifitx_dgdc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wifitx_dgdc_addr, self.__filter_wifitx_dgdc_msb, self.__filter_wifitx_dgdc_lsb, value)

    @property
    def filter_wifitx_input_ld(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wifitx_input_ld_addr, self.__filter_wifitx_input_ld_msb, self.__filter_wifitx_input_ld_lsb)
    @filter_wifitx_input_ld.setter
    def filter_wifitx_input_ld(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wifitx_input_ld_addr, self.__filter_wifitx_input_ld_msb, self.__filter_wifitx_input_ld_lsb, value)

    @property
    def filter_wifitx_bstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wifitx_bstb_addr, self.__filter_wifitx_bstb_msb, self.__filter_wifitx_bstb_lsb)
    @filter_wifitx_bstb.setter
    def filter_wifitx_bstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wifitx_bstb_addr, self.__filter_wifitx_bstb_msb, self.__filter_wifitx_bstb_lsb, value)

    @property
    def filter_wifitx_dedge(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wifitx_dedge_addr, self.__filter_wifitx_dedge_msb, self.__filter_wifitx_dedge_lsb)
    @filter_wifitx_dedge.setter
    def filter_wifitx_dedge(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wifitx_dedge_addr, self.__filter_wifitx_dedge_msb, self.__filter_wifitx_dedge_lsb, value)

    @property
    def filter_btrx_dgdc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx_dgdc_addr, self.__filter_btrx_dgdc_msb, self.__filter_btrx_dgdc_lsb)
    @filter_btrx_dgdc.setter
    def filter_btrx_dgdc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx_dgdc_addr, self.__filter_btrx_dgdc_msb, self.__filter_btrx_dgdc_lsb, value)

    @property
    def filter_btrx_input_ld(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx_input_ld_addr, self.__filter_btrx_input_ld_msb, self.__filter_btrx_input_ld_lsb)
    @filter_btrx_input_ld.setter
    def filter_btrx_input_ld(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx_input_ld_addr, self.__filter_btrx_input_ld_msb, self.__filter_btrx_input_ld_lsb, value)

    @property
    def filter_btrx_bstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx_bstb_addr, self.__filter_btrx_bstb_msb, self.__filter_btrx_bstb_lsb)
    @filter_btrx_bstb.setter
    def filter_btrx_bstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx_bstb_addr, self.__filter_btrx_bstb_msb, self.__filter_btrx_bstb_lsb, value)

    @property
    def filter_btrx_dedge(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx_dedge_addr, self.__filter_btrx_dedge_msb, self.__filter_btrx_dedge_lsb)
    @filter_btrx_dedge.setter
    def filter_btrx_dedge(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx_dedge_addr, self.__filter_btrx_dedge_msb, self.__filter_btrx_dedge_lsb, value)

    @property
    def filter_bttx_dgdc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx_dgdc_addr, self.__filter_bttx_dgdc_msb, self.__filter_bttx_dgdc_lsb)
    @filter_bttx_dgdc.setter
    def filter_bttx_dgdc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx_dgdc_addr, self.__filter_bttx_dgdc_msb, self.__filter_bttx_dgdc_lsb, value)

    @property
    def filter_bttx_input_ld(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx_input_ld_addr, self.__filter_bttx_input_ld_msb, self.__filter_bttx_input_ld_lsb)
    @filter_bttx_input_ld.setter
    def filter_bttx_input_ld(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx_input_ld_addr, self.__filter_bttx_input_ld_msb, self.__filter_bttx_input_ld_lsb, value)

    @property
    def filter_bttx_bstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx_bstb_addr, self.__filter_bttx_bstb_msb, self.__filter_bttx_bstb_lsb)
    @filter_bttx_bstb.setter
    def filter_bttx_bstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx_bstb_addr, self.__filter_bttx_bstb_msb, self.__filter_bttx_bstb_lsb, value)

    @property
    def filter_bttx_dedge(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx_dedge_addr, self.__filter_bttx_dedge_msb, self.__filter_bttx_dedge_lsb)
    @filter_bttx_dedge.setter
    def filter_bttx_dedge(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx_dedge_addr, self.__filter_bttx_dedge_msb, self.__filter_bttx_dedge_lsb, value)

    @property
    def tmx_lbd1(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tmx_lbd1_addr, self.__tmx_lbd1_msb, self.__tmx_lbd1_lsb)
    @tmx_lbd1.setter
    def tmx_lbd1(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tmx_lbd1_addr, self.__tmx_lbd1_msb, self.__tmx_lbd1_lsb, value)

    @property
    def tmx_lbd2(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tmx_lbd2_addr, self.__tmx_lbd2_msb, self.__tmx_lbd2_lsb)
    @tmx_lbd2.setter
    def tmx_lbd2(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tmx_lbd2_addr, self.__tmx_lbd2_msb, self.__tmx_lbd2_lsb, value)

    @property
    def tmx_dsw_bias(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tmx_dsw_bias_addr, self.__tmx_dsw_bias_msb, self.__tmx_dsw_bias_lsb)
    @tmx_dsw_bias.setter
    def tmx_dsw_bias(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tmx_dsw_bias_addr, self.__tmx_dsw_bias_msb, self.__tmx_dsw_bias_lsb, value)

    @property
    def tmx_dv2i_bias(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tmx_dv2i_bias_addr, self.__tmx_dv2i_bias_msb, self.__tmx_dv2i_bias_lsb)
    @tmx_dv2i_bias.setter
    def tmx_dv2i_bias(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tmx_dv2i_bias_addr, self.__tmx_dv2i_bias_msb, self.__tmx_dv2i_bias_lsb, value)

    @property
    def dac_ck_ph_inv(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dac_ck_ph_inv_addr, self.__dac_ck_ph_inv_msb, self.__dac_ck_ph_inv_lsb)
    @dac_ck_ph_inv.setter
    def dac_ck_ph_inv(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dac_ck_ph_inv_addr, self.__dac_ck_ph_inv_msb, self.__dac_ck_ph_inv_lsb, value)

    @property
    def filter_xpd_lat(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_xpd_lat_addr, self.__filter_xpd_lat_msb, self.__filter_xpd_lat_lsb)
    @filter_xpd_lat.setter
    def filter_xpd_lat(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_xpd_lat_addr, self.__filter_xpd_lat_msb, self.__filter_xpd_lat_lsb, value)

    @property
    def nc9(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__nc9_addr, self.__nc9_msb, self.__nc9_lsb)
    @nc9.setter
    def nc9(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__nc9_addr, self.__nc9_msb, self.__nc9_lsb, value)

    @property
    def filter_cmplx_ctrl(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_cmplx_ctrl_addr, self.__filter_cmplx_ctrl_msb, self.__filter_cmplx_ctrl_lsb)
    @filter_cmplx_ctrl.setter
    def filter_cmplx_ctrl(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_cmplx_ctrl_addr, self.__filter_cmplx_ctrl_msb, self.__filter_cmplx_ctrl_lsb, value)

    @property
    def encmplx_btrx(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__encmplx_btrx_addr, self.__encmplx_btrx_msb, self.__encmplx_btrx_lsb)
    @encmplx_btrx.setter
    def encmplx_btrx(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__encmplx_btrx_addr, self.__encmplx_btrx_msb, self.__encmplx_btrx_lsb, value)

    @property
    def encmplx_bttx(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__encmplx_bttx_addr, self.__encmplx_bttx_msb, self.__encmplx_bttx_lsb)
    @encmplx_bttx.setter
    def encmplx_bttx(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__encmplx_bttx_addr, self.__encmplx_bttx_msb, self.__encmplx_bttx_lsb, value)

    @property
    def nc10(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__nc10_addr, self.__nc10_msb, self.__nc10_lsb)
    @nc10.setter
    def nc10(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__nc10_addr, self.__nc10_msb, self.__nc10_lsb, value)
