from hal.common import *
from hal.hwregister.hwi2c.CHIP72.addr_base import *
class RFRX(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__I2C = I2C(self.channel, self.chipv)
        self.__base = RFRX_BASE
        self.__hostid = RFRX_HOSTID
        self.__ent_vga_lsb = 2
        self.__ent_vga_msb = 2
        self.__ent_vga_addr = 0x0
        self.__ent_lna_lsb = 3
        self.__ent_lna_msb = 3
        self.__ent_lna_addr = 0x0
        self.__ent_mx_lsb = 4
        self.__ent_mx_msb = 4
        self.__ent_mx_addr = 0x0
        self.__dtest_lsb = 1
        self.__dtest_msb = 2
        self.__dtest_addr = 0x1
        self.__rfrx_lna_dboost_lsb = 6
        self.__rfrx_lna_dboost_msb = 6
        self.__rfrx_lna_dboost_addr = 0x3
        self.__rfrx_lna_dcap_lsb = 0
        self.__rfrx_lna_dcap_msb = 3
        self.__rfrx_lna_dcap_addr = 0x4
        self.__rfrx_lna_ngm_lsb = 4
        self.__rfrx_lna_ngm_msb = 6
        self.__rfrx_lna_ngm_addr = 0x4
        self.__LB_MODE_lsb = 7
        self.__LB_MODE_msb = 7
        self.__LB_MODE_addr = 0x4
        self.__rfrx_mx_db_lsb = 0
        self.__rfrx_mx_db_msb = 1
        self.__rfrx_mx_db_addr = 0x5
        self.__lna_pd_amp_lsb = 2
        self.__lna_pd_amp_msb = 4
        self.__lna_pd_amp_addr = 0x5
        self.__lna_pd_dac_lsb = 0
        self.__lna_pd_dac_msb = 4
        self.__lna_pd_dac_addr = 0x6
        self.__rfrx_vga_dcap_lsb = 0
        self.__rfrx_vga_dcap_msb = 3
        self.__rfrx_vga_dcap_addr = 0x7
        self.__rfrx_vga_ngm_lsb = 4
        self.__rfrx_vga_ngm_msb = 6
        self.__rfrx_vga_ngm_addr = 0x7
        self.__vga_pd_amp_lsb = 0
        self.__vga_pd_amp_msb = 2
        self.__vga_pd_amp_addr = 0x8
        self.__vga_pd_dac_lsb = 3
        self.__vga_pd_dac_msb = 7
        self.__vga_pd_dac_addr = 0x8
        self.__spare_bits0_lsb = 0
        self.__spare_bits0_msb = 3
        self.__spare_bits0_addr = 0x9
        self.__ckbuf_dbst_lsb = 4
        self.__ckbuf_dbst_msb = 4
        self.__ckbuf_dbst_addr = 0x9
        self.__ckbuf_dphase_lsb = 5
        self.__ckbuf_dphase_msb = 6
        self.__ckbuf_dphase_addr = 0x9
        self.__filter_rx_en_bias_input_lsb = 7
        self.__filter_rx_en_bias_input_msb = 7
        self.__filter_rx_en_bias_input_addr = 0x9
        self.__spare_bits1_lsb = 0
        self.__spare_bits1_msb = 7
        self.__spare_bits1_addr = 0xa

    def reg_addr_rd(self,reg_addr):
        return self.__I2C.i2c_rd(self.__base , self.__hostid ,reg_addr)
    def reg_addr_wr(self,reg_addr,value):
        return self.__I2C.i2c_wr(self.__base , self.__hostid ,reg_addr,value)

    @property
    def ent_vga(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_vga_addr, self.__ent_vga_msb, self.__ent_vga_lsb)
    @ent_vga.setter
    def ent_vga(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_vga_addr, self.__ent_vga_msb, self.__ent_vga_lsb, value)

    @property
    def ent_lna(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_lna_addr, self.__ent_lna_msb, self.__ent_lna_lsb)
    @ent_lna.setter
    def ent_lna(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_lna_addr, self.__ent_lna_msb, self.__ent_lna_lsb, value)

    @property
    def ent_mx(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_mx_addr, self.__ent_mx_msb, self.__ent_mx_lsb)
    @ent_mx.setter
    def ent_mx(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_mx_addr, self.__ent_mx_msb, self.__ent_mx_lsb, value)

    @property
    def dtest(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dtest_addr, self.__dtest_msb, self.__dtest_lsb)
    @dtest.setter
    def dtest(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dtest_addr, self.__dtest_msb, self.__dtest_lsb, value)

    @property
    def rfrx_lna_dboost(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rfrx_lna_dboost_addr, self.__rfrx_lna_dboost_msb, self.__rfrx_lna_dboost_lsb)
    @rfrx_lna_dboost.setter
    def rfrx_lna_dboost(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rfrx_lna_dboost_addr, self.__rfrx_lna_dboost_msb, self.__rfrx_lna_dboost_lsb, value)

    @property
    def rfrx_lna_dcap(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rfrx_lna_dcap_addr, self.__rfrx_lna_dcap_msb, self.__rfrx_lna_dcap_lsb)
    @rfrx_lna_dcap.setter
    def rfrx_lna_dcap(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rfrx_lna_dcap_addr, self.__rfrx_lna_dcap_msb, self.__rfrx_lna_dcap_lsb, value)

    @property
    def rfrx_lna_ngm(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rfrx_lna_ngm_addr, self.__rfrx_lna_ngm_msb, self.__rfrx_lna_ngm_lsb)
    @rfrx_lna_ngm.setter
    def rfrx_lna_ngm(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rfrx_lna_ngm_addr, self.__rfrx_lna_ngm_msb, self.__rfrx_lna_ngm_lsb, value)

    @property
    def LB_MODE(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__LB_MODE_addr, self.__LB_MODE_msb, self.__LB_MODE_lsb)
    @LB_MODE.setter
    def LB_MODE(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__LB_MODE_addr, self.__LB_MODE_msb, self.__LB_MODE_lsb, value)

    @property
    def rfrx_mx_db(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rfrx_mx_db_addr, self.__rfrx_mx_db_msb, self.__rfrx_mx_db_lsb)
    @rfrx_mx_db.setter
    def rfrx_mx_db(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rfrx_mx_db_addr, self.__rfrx_mx_db_msb, self.__rfrx_mx_db_lsb, value)

    @property
    def lna_pd_amp(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__lna_pd_amp_addr, self.__lna_pd_amp_msb, self.__lna_pd_amp_lsb)
    @lna_pd_amp.setter
    def lna_pd_amp(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__lna_pd_amp_addr, self.__lna_pd_amp_msb, self.__lna_pd_amp_lsb, value)

    @property
    def lna_pd_dac(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__lna_pd_dac_addr, self.__lna_pd_dac_msb, self.__lna_pd_dac_lsb)
    @lna_pd_dac.setter
    def lna_pd_dac(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__lna_pd_dac_addr, self.__lna_pd_dac_msb, self.__lna_pd_dac_lsb, value)

    @property
    def rfrx_vga_dcap(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rfrx_vga_dcap_addr, self.__rfrx_vga_dcap_msb, self.__rfrx_vga_dcap_lsb)
    @rfrx_vga_dcap.setter
    def rfrx_vga_dcap(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rfrx_vga_dcap_addr, self.__rfrx_vga_dcap_msb, self.__rfrx_vga_dcap_lsb, value)

    @property
    def rfrx_vga_ngm(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rfrx_vga_ngm_addr, self.__rfrx_vga_ngm_msb, self.__rfrx_vga_ngm_lsb)
    @rfrx_vga_ngm.setter
    def rfrx_vga_ngm(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rfrx_vga_ngm_addr, self.__rfrx_vga_ngm_msb, self.__rfrx_vga_ngm_lsb, value)

    @property
    def vga_pd_amp(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__vga_pd_amp_addr, self.__vga_pd_amp_msb, self.__vga_pd_amp_lsb)
    @vga_pd_amp.setter
    def vga_pd_amp(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__vga_pd_amp_addr, self.__vga_pd_amp_msb, self.__vga_pd_amp_lsb, value)

    @property
    def vga_pd_dac(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__vga_pd_dac_addr, self.__vga_pd_dac_msb, self.__vga_pd_dac_lsb)
    @vga_pd_dac.setter
    def vga_pd_dac(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__vga_pd_dac_addr, self.__vga_pd_dac_msb, self.__vga_pd_dac_lsb, value)

    @property
    def spare_bits0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__spare_bits0_addr, self.__spare_bits0_msb, self.__spare_bits0_lsb)
    @spare_bits0.setter
    def spare_bits0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__spare_bits0_addr, self.__spare_bits0_msb, self.__spare_bits0_lsb, value)

    @property
    def ckbuf_dbst(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ckbuf_dbst_addr, self.__ckbuf_dbst_msb, self.__ckbuf_dbst_lsb)
    @ckbuf_dbst.setter
    def ckbuf_dbst(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ckbuf_dbst_addr, self.__ckbuf_dbst_msb, self.__ckbuf_dbst_lsb, value)

    @property
    def ckbuf_dphase(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ckbuf_dphase_addr, self.__ckbuf_dphase_msb, self.__ckbuf_dphase_lsb)
    @ckbuf_dphase.setter
    def ckbuf_dphase(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ckbuf_dphase_addr, self.__ckbuf_dphase_msb, self.__ckbuf_dphase_lsb, value)

    @property
    def filter_rx_en_bias_input(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_rx_en_bias_input_addr, self.__filter_rx_en_bias_input_msb, self.__filter_rx_en_bias_input_lsb)
    @filter_rx_en_bias_input.setter
    def filter_rx_en_bias_input(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_rx_en_bias_input_addr, self.__filter_rx_en_bias_input_msb, self.__filter_rx_en_bias_input_lsb, value)

    @property
    def spare_bits1(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__spare_bits1_addr, self.__spare_bits1_msb, self.__spare_bits1_lsb)
    @spare_bits1.setter
    def spare_bits1(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__spare_bits1_addr, self.__spare_bits1_msb, self.__spare_bits1_lsb, value)
