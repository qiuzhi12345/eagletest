from hal.common import *
from hal.hwregister.hwi2c.ESP32.addr_base import *
class DIG_FE(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__I2C = I2C(self.channel, self.chipv)
        self.__base = DIG_FE_BASE
        self.__hostid = DIG_FE_HOSTID
        self.__reg_rfcfg_slv_ctrl0_lsb = 0
        self.__reg_rfcfg_slv_ctrl0_msb = 7
        self.__reg_rfcfg_slv_ctrl0_addr = 0x0
        self.__reg_fe_ctrl0_lsb = 0
        self.__reg_fe_ctrl0_msb = 7
        self.__reg_fe_ctrl0_addr = 0x1
        self.__reg_fe_ctrl1_lsb = 0
        self.__reg_fe_ctrl1_msb = 7
        self.__reg_fe_ctrl1_addr = 0x2
        self.__r_txbb1_pbus_1_7_0_lsb = 0
        self.__r_txbb1_pbus_1_7_0_msb = 7
        self.__r_txbb1_pbus_1_7_0_addr = 0x3
        self.__r_txbb1_pbus_1_8_8_lsb = 0
        self.__r_txbb1_pbus_1_8_8_msb = 0
        self.__r_txbb1_pbus_1_8_8_addr = 0x4
        self.__r_txbb1_pbus_2_6_0_lsb = 1
        self.__r_txbb1_pbus_2_6_0_msb = 7
        self.__r_txbb1_pbus_2_6_0_addr = 0x4
        self.__r_txbb1_pbus_2_8_7_lsb = 0
        self.__r_txbb1_pbus_2_8_7_msb = 1
        self.__r_txbb1_pbus_2_8_7_addr = 0x5
        self.__r_txbb2_pbus_1_5_0_lsb = 2
        self.__r_txbb2_pbus_1_5_0_msb = 7
        self.__r_txbb2_pbus_1_5_0_addr = 0x5
        self.__r_txbb2_pbus_1_8_6_lsb = 0
        self.__r_txbb2_pbus_1_8_6_msb = 2
        self.__r_txbb2_pbus_1_8_6_addr = 0x6
        self.__r_txbb2_pbus_2_4_0_lsb = 3
        self.__r_txbb2_pbus_2_4_0_msb = 7
        self.__r_txbb2_pbus_2_4_0_addr = 0x6
        self.__r_txbb2_pbus_2_8_5_lsb = 0
        self.__r_txbb2_pbus_2_8_5_msb = 3
        self.__r_txbb2_pbus_2_8_5_addr = 0x7
        self.__r_rfrx_pbus_1_3_0_lsb = 4
        self.__r_rfrx_pbus_1_3_0_msb = 7
        self.__r_rfrx_pbus_1_3_0_addr = 0x7
        self.__r_rfrx_pbus_1_8_4_lsb = 0
        self.__r_rfrx_pbus_1_8_4_msb = 4
        self.__r_rfrx_pbus_1_8_4_addr = 0x8
        self.__r_bbrx_pbus_1_2_0_lsb = 5
        self.__r_bbrx_pbus_1_2_0_msb = 7
        self.__r_bbrx_pbus_1_2_0_addr = 0x8
        self.__r_bbrx_pbus_1_8_3_lsb = 0
        self.__r_bbrx_pbus_1_8_3_msb = 5
        self.__r_bbrx_pbus_1_8_3_addr = 0x9
        self.__r_bbrx_pbus_2_1_0_lsb = 6
        self.__r_bbrx_pbus_2_1_0_msb = 7
        self.__r_bbrx_pbus_2_1_0_addr = 0x9
        self.__r_bbrx_pbus_2_8_2_lsb = 0
        self.__r_bbrx_pbus_2_8_2_msb = 6
        self.__r_bbrx_pbus_2_8_2_addr = 0xa
        self.__r_dcoi_pbus_1_0_0_lsb = 7
        self.__r_dcoi_pbus_1_0_0_msb = 7
        self.__r_dcoi_pbus_1_0_0_addr = 0xa
        self.__r_dcoi_pbus_1_8_1_lsb = 0
        self.__r_dcoi_pbus_1_8_1_msb = 7
        self.__r_dcoi_pbus_1_8_1_addr = 0xb
        self.__r_dcoi_pbus_2_7_0_lsb = 0
        self.__r_dcoi_pbus_2_7_0_msb = 7
        self.__r_dcoi_pbus_2_7_0_addr = 0xc
        self.__r_dcoi_pbus_2_8_8_lsb = 0
        self.__r_dcoi_pbus_2_8_8_msb = 0
        self.__r_dcoi_pbus_2_8_8_addr = 0xd
        self.__r_dcoq_pbus_1_6_0_lsb = 1
        self.__r_dcoq_pbus_1_6_0_msb = 7
        self.__r_dcoq_pbus_1_6_0_addr = 0xd
        self.__r_dcoq_pbus_1_8_7_lsb = 0
        self.__r_dcoq_pbus_1_8_7_msb = 1
        self.__r_dcoq_pbus_1_8_7_addr = 0xe
        self.__r_dcoq_pbus_2_5_0_lsb = 2
        self.__r_dcoq_pbus_2_5_0_msb = 7
        self.__r_dcoq_pbus_2_5_0_addr = 0xe
        self.__r_dcoq_pbus_2_8_6_lsb = 0
        self.__r_dcoq_pbus_2_8_6_msb = 2
        self.__r_dcoq_pbus_2_8_6_addr = 0xf
        self.__r_txrf1_pbus_1_4_0_lsb = 3
        self.__r_txrf1_pbus_1_4_0_msb = 7
        self.__r_txrf1_pbus_1_4_0_addr = 0xf
        self.__r_txrf1_pbus_1_8_5_lsb = 0
        self.__r_txrf1_pbus_1_8_5_msb = 3
        self.__r_txrf1_pbus_1_8_5_addr = 0x10
        self.__r_txrf2_pbus_1_3_0_lsb = 4
        self.__r_txrf2_pbus_1_3_0_msb = 7
        self.__r_txrf2_pbus_1_3_0_addr = 0x10
        self.__r_txrf2_pbus_1_8_4_lsb = 0
        self.__r_txrf2_pbus_1_8_4_msb = 4
        self.__r_txrf2_pbus_1_8_4_addr = 0x11
        self.__reg_rfcfg_slv_ctrl1_lsb = 0
        self.__reg_rfcfg_slv_ctrl1_msb = 7
        self.__reg_rfcfg_slv_ctrl1_addr = 0x12
        self.__reg_pbus_data_7_0_lsb = 0
        self.__reg_pbus_data_7_0_msb = 7
        self.__reg_pbus_data_7_0_addr = 0x13
        self.__reg_pbus_data_8_lsb = 0
        self.__reg_pbus_data_8_msb = 0
        self.__reg_pbus_data_8_addr = 0x14
        self.__reg_pbus_name_lsb = 1
        self.__reg_pbus_name_msb = 3
        self.__reg_pbus_name_addr = 0x14
        self.__reg_pbus_en_no_lsb = 4
        self.__reg_pbus_en_no_msb = 4
        self.__reg_pbus_en_no_addr = 0x14
        self.__reg_pbus_en_lsb = 5
        self.__reg_pbus_en_msb = 5
        self.__reg_pbus_en_addr = 0x14
        self.__reg_ate_mode_lsb = 6
        self.__reg_ate_mode_msb = 6
        self.__reg_ate_mode_addr = 0x14
        self.__reg_tx_force_on_lsb = 0
        self.__reg_tx_force_on_msb = 0
        self.__reg_tx_force_on_addr = 0x15
        self.__reg_rx_force_on_lsb = 1
        self.__reg_rx_force_on_msb = 1
        self.__reg_rx_force_on_addr = 0x15
        self.__reg_rx_satb_dir_out_lsb = 2
        self.__reg_rx_satb_dir_out_msb = 2
        self.__reg_rx_satb_dir_out_addr = 0x15

    def reg_addr_rd(self,reg_addr):
        return self.__I2C.i2c_rd(self.__base , self.__hostid ,reg_addr)
    def reg_addr_wr(self,reg_addr,value):
        return self.__I2C.i2c_wr(self.__base , self.__hostid ,reg_addr,value)

    @property
    def reg_rfcfg_slv_ctrl0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__reg_rfcfg_slv_ctrl0_addr, self.__reg_rfcfg_slv_ctrl0_msb, self.__reg_rfcfg_slv_ctrl0_lsb)
    @reg_rfcfg_slv_ctrl0.setter
    def reg_rfcfg_slv_ctrl0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__reg_rfcfg_slv_ctrl0_addr, self.__reg_rfcfg_slv_ctrl0_msb, self.__reg_rfcfg_slv_ctrl0_lsb, value)

    @property
    def reg_fe_ctrl0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__reg_fe_ctrl0_addr, self.__reg_fe_ctrl0_msb, self.__reg_fe_ctrl0_lsb)
    @reg_fe_ctrl0.setter
    def reg_fe_ctrl0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__reg_fe_ctrl0_addr, self.__reg_fe_ctrl0_msb, self.__reg_fe_ctrl0_lsb, value)

    @property
    def reg_fe_ctrl1(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__reg_fe_ctrl1_addr, self.__reg_fe_ctrl1_msb, self.__reg_fe_ctrl1_lsb)
    @reg_fe_ctrl1.setter
    def reg_fe_ctrl1(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__reg_fe_ctrl1_addr, self.__reg_fe_ctrl1_msb, self.__reg_fe_ctrl1_lsb, value)

    @property
    def r_txbb1_pbus_1_7_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__r_txbb1_pbus_1_7_0_addr, self.__r_txbb1_pbus_1_7_0_msb, self.__r_txbb1_pbus_1_7_0_lsb)
    @r_txbb1_pbus_1_7_0.setter
    def r_txbb1_pbus_1_7_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__r_txbb1_pbus_1_7_0_addr, self.__r_txbb1_pbus_1_7_0_msb, self.__r_txbb1_pbus_1_7_0_lsb, value)

    @property
    def r_txbb1_pbus_1_8_8(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__r_txbb1_pbus_1_8_8_addr, self.__r_txbb1_pbus_1_8_8_msb, self.__r_txbb1_pbus_1_8_8_lsb)
    @r_txbb1_pbus_1_8_8.setter
    def r_txbb1_pbus_1_8_8(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__r_txbb1_pbus_1_8_8_addr, self.__r_txbb1_pbus_1_8_8_msb, self.__r_txbb1_pbus_1_8_8_lsb, value)

    @property
    def r_txbb1_pbus_2_6_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__r_txbb1_pbus_2_6_0_addr, self.__r_txbb1_pbus_2_6_0_msb, self.__r_txbb1_pbus_2_6_0_lsb)
    @r_txbb1_pbus_2_6_0.setter
    def r_txbb1_pbus_2_6_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__r_txbb1_pbus_2_6_0_addr, self.__r_txbb1_pbus_2_6_0_msb, self.__r_txbb1_pbus_2_6_0_lsb, value)

    @property
    def r_txbb1_pbus_2_8_7(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__r_txbb1_pbus_2_8_7_addr, self.__r_txbb1_pbus_2_8_7_msb, self.__r_txbb1_pbus_2_8_7_lsb)
    @r_txbb1_pbus_2_8_7.setter
    def r_txbb1_pbus_2_8_7(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__r_txbb1_pbus_2_8_7_addr, self.__r_txbb1_pbus_2_8_7_msb, self.__r_txbb1_pbus_2_8_7_lsb, value)

    @property
    def r_txbb2_pbus_1_5_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__r_txbb2_pbus_1_5_0_addr, self.__r_txbb2_pbus_1_5_0_msb, self.__r_txbb2_pbus_1_5_0_lsb)
    @r_txbb2_pbus_1_5_0.setter
    def r_txbb2_pbus_1_5_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__r_txbb2_pbus_1_5_0_addr, self.__r_txbb2_pbus_1_5_0_msb, self.__r_txbb2_pbus_1_5_0_lsb, value)

    @property
    def r_txbb2_pbus_1_8_6(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__r_txbb2_pbus_1_8_6_addr, self.__r_txbb2_pbus_1_8_6_msb, self.__r_txbb2_pbus_1_8_6_lsb)
    @r_txbb2_pbus_1_8_6.setter
    def r_txbb2_pbus_1_8_6(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__r_txbb2_pbus_1_8_6_addr, self.__r_txbb2_pbus_1_8_6_msb, self.__r_txbb2_pbus_1_8_6_lsb, value)

    @property
    def r_txbb2_pbus_2_4_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__r_txbb2_pbus_2_4_0_addr, self.__r_txbb2_pbus_2_4_0_msb, self.__r_txbb2_pbus_2_4_0_lsb)
    @r_txbb2_pbus_2_4_0.setter
    def r_txbb2_pbus_2_4_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__r_txbb2_pbus_2_4_0_addr, self.__r_txbb2_pbus_2_4_0_msb, self.__r_txbb2_pbus_2_4_0_lsb, value)

    @property
    def r_txbb2_pbus_2_8_5(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__r_txbb2_pbus_2_8_5_addr, self.__r_txbb2_pbus_2_8_5_msb, self.__r_txbb2_pbus_2_8_5_lsb)
    @r_txbb2_pbus_2_8_5.setter
    def r_txbb2_pbus_2_8_5(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__r_txbb2_pbus_2_8_5_addr, self.__r_txbb2_pbus_2_8_5_msb, self.__r_txbb2_pbus_2_8_5_lsb, value)

    @property
    def r_rfrx_pbus_1_3_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__r_rfrx_pbus_1_3_0_addr, self.__r_rfrx_pbus_1_3_0_msb, self.__r_rfrx_pbus_1_3_0_lsb)
    @r_rfrx_pbus_1_3_0.setter
    def r_rfrx_pbus_1_3_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__r_rfrx_pbus_1_3_0_addr, self.__r_rfrx_pbus_1_3_0_msb, self.__r_rfrx_pbus_1_3_0_lsb, value)

    @property
    def r_rfrx_pbus_1_8_4(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__r_rfrx_pbus_1_8_4_addr, self.__r_rfrx_pbus_1_8_4_msb, self.__r_rfrx_pbus_1_8_4_lsb)
    @r_rfrx_pbus_1_8_4.setter
    def r_rfrx_pbus_1_8_4(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__r_rfrx_pbus_1_8_4_addr, self.__r_rfrx_pbus_1_8_4_msb, self.__r_rfrx_pbus_1_8_4_lsb, value)

    @property
    def r_bbrx_pbus_1_2_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__r_bbrx_pbus_1_2_0_addr, self.__r_bbrx_pbus_1_2_0_msb, self.__r_bbrx_pbus_1_2_0_lsb)
    @r_bbrx_pbus_1_2_0.setter
    def r_bbrx_pbus_1_2_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__r_bbrx_pbus_1_2_0_addr, self.__r_bbrx_pbus_1_2_0_msb, self.__r_bbrx_pbus_1_2_0_lsb, value)

    @property
    def r_bbrx_pbus_1_8_3(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__r_bbrx_pbus_1_8_3_addr, self.__r_bbrx_pbus_1_8_3_msb, self.__r_bbrx_pbus_1_8_3_lsb)
    @r_bbrx_pbus_1_8_3.setter
    def r_bbrx_pbus_1_8_3(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__r_bbrx_pbus_1_8_3_addr, self.__r_bbrx_pbus_1_8_3_msb, self.__r_bbrx_pbus_1_8_3_lsb, value)

    @property
    def r_bbrx_pbus_2_1_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__r_bbrx_pbus_2_1_0_addr, self.__r_bbrx_pbus_2_1_0_msb, self.__r_bbrx_pbus_2_1_0_lsb)
    @r_bbrx_pbus_2_1_0.setter
    def r_bbrx_pbus_2_1_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__r_bbrx_pbus_2_1_0_addr, self.__r_bbrx_pbus_2_1_0_msb, self.__r_bbrx_pbus_2_1_0_lsb, value)

    @property
    def r_bbrx_pbus_2_8_2(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__r_bbrx_pbus_2_8_2_addr, self.__r_bbrx_pbus_2_8_2_msb, self.__r_bbrx_pbus_2_8_2_lsb)
    @r_bbrx_pbus_2_8_2.setter
    def r_bbrx_pbus_2_8_2(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__r_bbrx_pbus_2_8_2_addr, self.__r_bbrx_pbus_2_8_2_msb, self.__r_bbrx_pbus_2_8_2_lsb, value)

    @property
    def r_dcoi_pbus_1_0_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__r_dcoi_pbus_1_0_0_addr, self.__r_dcoi_pbus_1_0_0_msb, self.__r_dcoi_pbus_1_0_0_lsb)
    @r_dcoi_pbus_1_0_0.setter
    def r_dcoi_pbus_1_0_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__r_dcoi_pbus_1_0_0_addr, self.__r_dcoi_pbus_1_0_0_msb, self.__r_dcoi_pbus_1_0_0_lsb, value)

    @property
    def r_dcoi_pbus_1_8_1(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__r_dcoi_pbus_1_8_1_addr, self.__r_dcoi_pbus_1_8_1_msb, self.__r_dcoi_pbus_1_8_1_lsb)
    @r_dcoi_pbus_1_8_1.setter
    def r_dcoi_pbus_1_8_1(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__r_dcoi_pbus_1_8_1_addr, self.__r_dcoi_pbus_1_8_1_msb, self.__r_dcoi_pbus_1_8_1_lsb, value)

    @property
    def r_dcoi_pbus_2_7_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__r_dcoi_pbus_2_7_0_addr, self.__r_dcoi_pbus_2_7_0_msb, self.__r_dcoi_pbus_2_7_0_lsb)
    @r_dcoi_pbus_2_7_0.setter
    def r_dcoi_pbus_2_7_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__r_dcoi_pbus_2_7_0_addr, self.__r_dcoi_pbus_2_7_0_msb, self.__r_dcoi_pbus_2_7_0_lsb, value)

    @property
    def r_dcoi_pbus_2_8_8(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__r_dcoi_pbus_2_8_8_addr, self.__r_dcoi_pbus_2_8_8_msb, self.__r_dcoi_pbus_2_8_8_lsb)
    @r_dcoi_pbus_2_8_8.setter
    def r_dcoi_pbus_2_8_8(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__r_dcoi_pbus_2_8_8_addr, self.__r_dcoi_pbus_2_8_8_msb, self.__r_dcoi_pbus_2_8_8_lsb, value)

    @property
    def r_dcoq_pbus_1_6_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__r_dcoq_pbus_1_6_0_addr, self.__r_dcoq_pbus_1_6_0_msb, self.__r_dcoq_pbus_1_6_0_lsb)
    @r_dcoq_pbus_1_6_0.setter
    def r_dcoq_pbus_1_6_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__r_dcoq_pbus_1_6_0_addr, self.__r_dcoq_pbus_1_6_0_msb, self.__r_dcoq_pbus_1_6_0_lsb, value)

    @property
    def r_dcoq_pbus_1_8_7(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__r_dcoq_pbus_1_8_7_addr, self.__r_dcoq_pbus_1_8_7_msb, self.__r_dcoq_pbus_1_8_7_lsb)
    @r_dcoq_pbus_1_8_7.setter
    def r_dcoq_pbus_1_8_7(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__r_dcoq_pbus_1_8_7_addr, self.__r_dcoq_pbus_1_8_7_msb, self.__r_dcoq_pbus_1_8_7_lsb, value)

    @property
    def r_dcoq_pbus_2_5_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__r_dcoq_pbus_2_5_0_addr, self.__r_dcoq_pbus_2_5_0_msb, self.__r_dcoq_pbus_2_5_0_lsb)
    @r_dcoq_pbus_2_5_0.setter
    def r_dcoq_pbus_2_5_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__r_dcoq_pbus_2_5_0_addr, self.__r_dcoq_pbus_2_5_0_msb, self.__r_dcoq_pbus_2_5_0_lsb, value)

    @property
    def r_dcoq_pbus_2_8_6(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__r_dcoq_pbus_2_8_6_addr, self.__r_dcoq_pbus_2_8_6_msb, self.__r_dcoq_pbus_2_8_6_lsb)
    @r_dcoq_pbus_2_8_6.setter
    def r_dcoq_pbus_2_8_6(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__r_dcoq_pbus_2_8_6_addr, self.__r_dcoq_pbus_2_8_6_msb, self.__r_dcoq_pbus_2_8_6_lsb, value)

    @property
    def r_txrf1_pbus_1_4_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__r_txrf1_pbus_1_4_0_addr, self.__r_txrf1_pbus_1_4_0_msb, self.__r_txrf1_pbus_1_4_0_lsb)
    @r_txrf1_pbus_1_4_0.setter
    def r_txrf1_pbus_1_4_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__r_txrf1_pbus_1_4_0_addr, self.__r_txrf1_pbus_1_4_0_msb, self.__r_txrf1_pbus_1_4_0_lsb, value)

    @property
    def r_txrf1_pbus_1_8_5(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__r_txrf1_pbus_1_8_5_addr, self.__r_txrf1_pbus_1_8_5_msb, self.__r_txrf1_pbus_1_8_5_lsb)
    @r_txrf1_pbus_1_8_5.setter
    def r_txrf1_pbus_1_8_5(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__r_txrf1_pbus_1_8_5_addr, self.__r_txrf1_pbus_1_8_5_msb, self.__r_txrf1_pbus_1_8_5_lsb, value)

    @property
    def r_txrf2_pbus_1_3_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__r_txrf2_pbus_1_3_0_addr, self.__r_txrf2_pbus_1_3_0_msb, self.__r_txrf2_pbus_1_3_0_lsb)
    @r_txrf2_pbus_1_3_0.setter
    def r_txrf2_pbus_1_3_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__r_txrf2_pbus_1_3_0_addr, self.__r_txrf2_pbus_1_3_0_msb, self.__r_txrf2_pbus_1_3_0_lsb, value)

    @property
    def r_txrf2_pbus_1_8_4(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__r_txrf2_pbus_1_8_4_addr, self.__r_txrf2_pbus_1_8_4_msb, self.__r_txrf2_pbus_1_8_4_lsb)
    @r_txrf2_pbus_1_8_4.setter
    def r_txrf2_pbus_1_8_4(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__r_txrf2_pbus_1_8_4_addr, self.__r_txrf2_pbus_1_8_4_msb, self.__r_txrf2_pbus_1_8_4_lsb, value)

    @property
    def reg_rfcfg_slv_ctrl1(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__reg_rfcfg_slv_ctrl1_addr, self.__reg_rfcfg_slv_ctrl1_msb, self.__reg_rfcfg_slv_ctrl1_lsb)
    @reg_rfcfg_slv_ctrl1.setter
    def reg_rfcfg_slv_ctrl1(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__reg_rfcfg_slv_ctrl1_addr, self.__reg_rfcfg_slv_ctrl1_msb, self.__reg_rfcfg_slv_ctrl1_lsb, value)

    @property
    def reg_pbus_data_7_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__reg_pbus_data_7_0_addr, self.__reg_pbus_data_7_0_msb, self.__reg_pbus_data_7_0_lsb)
    @reg_pbus_data_7_0.setter
    def reg_pbus_data_7_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__reg_pbus_data_7_0_addr, self.__reg_pbus_data_7_0_msb, self.__reg_pbus_data_7_0_lsb, value)

    @property
    def reg_pbus_data_8(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__reg_pbus_data_8_addr, self.__reg_pbus_data_8_msb, self.__reg_pbus_data_8_lsb)
    @reg_pbus_data_8.setter
    def reg_pbus_data_8(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__reg_pbus_data_8_addr, self.__reg_pbus_data_8_msb, self.__reg_pbus_data_8_lsb, value)

    @property
    def reg_pbus_name(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__reg_pbus_name_addr, self.__reg_pbus_name_msb, self.__reg_pbus_name_lsb)
    @reg_pbus_name.setter
    def reg_pbus_name(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__reg_pbus_name_addr, self.__reg_pbus_name_msb, self.__reg_pbus_name_lsb, value)

    @property
    def reg_pbus_en_no(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__reg_pbus_en_no_addr, self.__reg_pbus_en_no_msb, self.__reg_pbus_en_no_lsb)
    @reg_pbus_en_no.setter
    def reg_pbus_en_no(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__reg_pbus_en_no_addr, self.__reg_pbus_en_no_msb, self.__reg_pbus_en_no_lsb, value)

    @property
    def reg_pbus_en(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__reg_pbus_en_addr, self.__reg_pbus_en_msb, self.__reg_pbus_en_lsb)
    @reg_pbus_en.setter
    def reg_pbus_en(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__reg_pbus_en_addr, self.__reg_pbus_en_msb, self.__reg_pbus_en_lsb, value)

    @property
    def reg_ate_mode(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__reg_ate_mode_addr, self.__reg_ate_mode_msb, self.__reg_ate_mode_lsb)
    @reg_ate_mode.setter
    def reg_ate_mode(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__reg_ate_mode_addr, self.__reg_ate_mode_msb, self.__reg_ate_mode_lsb, value)

    @property
    def reg_tx_force_on(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__reg_tx_force_on_addr, self.__reg_tx_force_on_msb, self.__reg_tx_force_on_lsb)
    @reg_tx_force_on.setter
    def reg_tx_force_on(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__reg_tx_force_on_addr, self.__reg_tx_force_on_msb, self.__reg_tx_force_on_lsb, value)

    @property
    def reg_rx_force_on(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__reg_rx_force_on_addr, self.__reg_rx_force_on_msb, self.__reg_rx_force_on_lsb)
    @reg_rx_force_on.setter
    def reg_rx_force_on(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__reg_rx_force_on_addr, self.__reg_rx_force_on_msb, self.__reg_rx_force_on_lsb, value)

    @property
    def reg_rx_satb_dir_out(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__reg_rx_satb_dir_out_addr, self.__reg_rx_satb_dir_out_msb, self.__reg_rx_satb_dir_out_lsb)
    @reg_rx_satb_dir_out.setter
    def reg_rx_satb_dir_out(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__reg_rx_satb_dir_out_addr, self.__reg_rx_satb_dir_out_msb, self.__reg_rx_satb_dir_out_lsb, value)
