from hal.common import *
from hal.hwregister.hwi2c.ESP8266.addr_base import *
class BBRX(object):
    def __init__(self, channel, chipv = "ESP8266"):
        self.chipv = chipv
        self.channel = channel
        self.__I2C = I2C(self.channel, self.chipv)
        self.__base = BBRX_BASE
        self.__hostid = BBRX_HOSTID
        self.__ent_rxlpf_bias_i_lsb = 2
        self.__ent_rxlpf_bias_i_msb = 2
        self.__ent_rxlpf_bias_i_addr = 0x0
        self.__ent_rxlpf_bias_q_lsb = 3
        self.__ent_rxlpf_bias_q_msb = 3
        self.__ent_rxlpf_bias_q_addr = 0x0
        self.__ent_rxlpf_i_lsb = 4
        self.__ent_rxlpf_i_msb = 4
        self.__ent_rxlpf_i_addr = 0x0
        self.__ent_rxlpf_q_lsb = 5
        self.__ent_rxlpf_q_msb = 5
        self.__ent_rxlpf_q_addr = 0x0
        self.__dtest_lsb = 6
        self.__dtest_msb = 7
        self.__dtest_addr = 0x0
        self.__rxlpf_amp1_lsb = 0
        self.__rxlpf_amp1_msb = 2
        self.__rxlpf_amp1_addr = 0x1
        self.__rxlpf_amp2_lsb = 3
        self.__rxlpf_amp2_msb = 5
        self.__rxlpf_amp2_addr = 0x1
        self.__rxlpf_bstb_lsb = 6
        self.__rxlpf_bstb_msb = 7
        self.__rxlpf_bstb_addr = 0x1
        self.__rxlpf_dcap_lsb = 0
        self.__rxlpf_dcap_msb = 4
        self.__rxlpf_dcap_addr = 0x2
        self.__rxlpf_dedge_lsb = 5
        self.__rxlpf_dedge_msb = 6
        self.__rxlpf_dedge_addr = 0x2
        self.__rxlpf_dgdc_lsb = 7
        self.__rxlpf_dgdc_msb = 7
        self.__rxlpf_dgdc_addr = 0x2
        self.__rxlpf_d_input_ld_lsb = 0
        self.__rxlpf_d_input_ld_msb = 1
        self.__rxlpf_d_input_ld_addr = 0x3
        self.__rxlpf_en_bias_input_lsb = 2
        self.__rxlpf_en_bias_input_msb = 2
        self.__rxlpf_en_bias_input_addr = 0x3
        self.__ent_adc_lsb = 0
        self.__ent_adc_msb = 5
        self.__ent_adc_addr = 0x4
        self.__xpd_adc_lsb = 6
        self.__xpd_adc_msb = 6
        self.__xpd_adc_addr = 0x4
        self.__xpd_refgen_lsb = 7
        self.__xpd_refgen_msb = 7
        self.__xpd_refgen_addr = 0x4
        self.__adc_dp_lsb = 0
        self.__adc_dp_msb = 1
        self.__adc_dp_addr = 0x5
        self.__adc_dn_lsb = 2
        self.__adc_dn_msb = 3
        self.__adc_dn_addr = 0x5
        self.__adc_dcm_lsb = 4
        self.__adc_dcm_msb = 5
        self.__adc_dcm_addr = 0x5
        self.__adc_bstb_lsb = 6
        self.__adc_bstb_msb = 7
        self.__adc_bstb_addr = 0x5
        self.__adc_dcal_lsb = 0
        self.__adc_dcal_msb = 3
        self.__adc_dcal_addr = 0x6
        self.__adc_delay1_lsb = 4
        self.__adc_delay1_msb = 5
        self.__adc_delay1_addr = 0x6
        self.__adc_delay2_lsb = 6
        self.__adc_delay2_msb = 7
        self.__adc_delay2_addr = 0x6
        self.__adc_delay3_lsb = 0
        self.__adc_delay3_msb = 1
        self.__adc_delay3_addr = 0x7
        self.__adc_delay4_lsb = 2
        self.__adc_delay4_msb = 3
        self.__adc_delay4_addr = 0x7
        self.__adc_delay5_lsb = 4
        self.__adc_delay5_msb = 5
        self.__adc_delay5_addr = 0x7
        self.__adc_delay6_lsb = 6
        self.__adc_delay6_msb = 7
        self.__adc_delay6_addr = 0x7
        self.__adc_bitlmt_lsb = 0
        self.__adc_bitlmt_msb = 0
        self.__adc_bitlmt_addr = 0x8
        self.__adc_tmode_lsb = 1
        self.__adc_tmode_msb = 1
        self.__adc_tmode_addr = 0x8
        self.__adc_posedgeout_lsb = 2
        self.__adc_posedgeout_msb = 2
        self.__adc_posedgeout_addr = 0x8
        self.__adc_endem_lsb = 3
        self.__adc_endem_msb = 3
        self.__adc_endem_addr = 0x8
        self.__adc_en_44M_lsb = 4
        self.__adc_en_44M_msb = 4
        self.__adc_en_44M_addr = 0x8
        self.__adc_encal_lsb = 5
        self.__adc_encal_msb = 5
        self.__adc_encal_addr = 0x8
        self.__adc_rst_lsb = 6
        self.__adc_rst_msb = 6
        self.__adc_rst_addr = 0x8
        self.__adc_spare_lsb = 7
        self.__adc_spare_msb = 7
        self.__adc_spare_addr = 0x8
        self.__spare_bits0_lsb = 0
        self.__spare_bits0_msb = 7
        self.__spare_bits0_addr = 0x9
        self.__spare_bits1_lsb = 0
        self.__spare_bits1_msb = 7
        self.__spare_bits1_addr = 0xa
        self.__spare_bits2_ro_lsb = 0
        self.__spare_bits2_ro_msb = 7
        self.__spare_bits2_ro_addr = 0xb

    def reg_addr_rd(self,reg_addr):
        return self.__I2C.i2c_rd(self.__base , self.__hostid ,reg_addr)
    def reg_addr_wr(self,reg_addr,value):
        return self.__I2C.i2c_wr(self.__base , self.__hostid ,reg_addr,value)

    @property
    def ent_rxlpf_bias_i(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_rxlpf_bias_i_addr, self.__ent_rxlpf_bias_i_msb, self.__ent_rxlpf_bias_i_lsb)
    @ent_rxlpf_bias_i.setter
    def ent_rxlpf_bias_i(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_rxlpf_bias_i_addr, self.__ent_rxlpf_bias_i_msb, self.__ent_rxlpf_bias_i_lsb, value)

    @property
    def ent_rxlpf_bias_q(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_rxlpf_bias_q_addr, self.__ent_rxlpf_bias_q_msb, self.__ent_rxlpf_bias_q_lsb)
    @ent_rxlpf_bias_q.setter
    def ent_rxlpf_bias_q(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_rxlpf_bias_q_addr, self.__ent_rxlpf_bias_q_msb, self.__ent_rxlpf_bias_q_lsb, value)

    @property
    def ent_rxlpf_i(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_rxlpf_i_addr, self.__ent_rxlpf_i_msb, self.__ent_rxlpf_i_lsb)
    @ent_rxlpf_i.setter
    def ent_rxlpf_i(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_rxlpf_i_addr, self.__ent_rxlpf_i_msb, self.__ent_rxlpf_i_lsb, value)

    @property
    def ent_rxlpf_q(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_rxlpf_q_addr, self.__ent_rxlpf_q_msb, self.__ent_rxlpf_q_lsb)
    @ent_rxlpf_q.setter
    def ent_rxlpf_q(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_rxlpf_q_addr, self.__ent_rxlpf_q_msb, self.__ent_rxlpf_q_lsb, value)

    @property
    def dtest(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dtest_addr, self.__dtest_msb, self.__dtest_lsb)
    @dtest.setter
    def dtest(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dtest_addr, self.__dtest_msb, self.__dtest_lsb, value)

    @property
    def rxlpf_amp1(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rxlpf_amp1_addr, self.__rxlpf_amp1_msb, self.__rxlpf_amp1_lsb)
    @rxlpf_amp1.setter
    def rxlpf_amp1(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rxlpf_amp1_addr, self.__rxlpf_amp1_msb, self.__rxlpf_amp1_lsb, value)

    @property
    def rxlpf_amp2(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rxlpf_amp2_addr, self.__rxlpf_amp2_msb, self.__rxlpf_amp2_lsb)
    @rxlpf_amp2.setter
    def rxlpf_amp2(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rxlpf_amp2_addr, self.__rxlpf_amp2_msb, self.__rxlpf_amp2_lsb, value)

    @property
    def rxlpf_bstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rxlpf_bstb_addr, self.__rxlpf_bstb_msb, self.__rxlpf_bstb_lsb)
    @rxlpf_bstb.setter
    def rxlpf_bstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rxlpf_bstb_addr, self.__rxlpf_bstb_msb, self.__rxlpf_bstb_lsb, value)

    @property
    def rxlpf_dcap(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rxlpf_dcap_addr, self.__rxlpf_dcap_msb, self.__rxlpf_dcap_lsb)
    @rxlpf_dcap.setter
    def rxlpf_dcap(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rxlpf_dcap_addr, self.__rxlpf_dcap_msb, self.__rxlpf_dcap_lsb, value)

    @property
    def rxlpf_dedge(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rxlpf_dedge_addr, self.__rxlpf_dedge_msb, self.__rxlpf_dedge_lsb)
    @rxlpf_dedge.setter
    def rxlpf_dedge(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rxlpf_dedge_addr, self.__rxlpf_dedge_msb, self.__rxlpf_dedge_lsb, value)

    @property
    def rxlpf_dgdc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rxlpf_dgdc_addr, self.__rxlpf_dgdc_msb, self.__rxlpf_dgdc_lsb)
    @rxlpf_dgdc.setter
    def rxlpf_dgdc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rxlpf_dgdc_addr, self.__rxlpf_dgdc_msb, self.__rxlpf_dgdc_lsb, value)

    @property
    def rxlpf_d_input_ld(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rxlpf_d_input_ld_addr, self.__rxlpf_d_input_ld_msb, self.__rxlpf_d_input_ld_lsb)
    @rxlpf_d_input_ld.setter
    def rxlpf_d_input_ld(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rxlpf_d_input_ld_addr, self.__rxlpf_d_input_ld_msb, self.__rxlpf_d_input_ld_lsb, value)

    @property
    def rxlpf_en_bias_input(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rxlpf_en_bias_input_addr, self.__rxlpf_en_bias_input_msb, self.__rxlpf_en_bias_input_lsb)
    @rxlpf_en_bias_input.setter
    def rxlpf_en_bias_input(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rxlpf_en_bias_input_addr, self.__rxlpf_en_bias_input_msb, self.__rxlpf_en_bias_input_lsb, value)

    @property
    def ent_adc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_adc_addr, self.__ent_adc_msb, self.__ent_adc_lsb)
    @ent_adc.setter
    def ent_adc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_adc_addr, self.__ent_adc_msb, self.__ent_adc_lsb, value)

    @property
    def xpd_adc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_adc_addr, self.__xpd_adc_msb, self.__xpd_adc_lsb)
    @xpd_adc.setter
    def xpd_adc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_adc_addr, self.__xpd_adc_msb, self.__xpd_adc_lsb, value)

    @property
    def xpd_refgen(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_refgen_addr, self.__xpd_refgen_msb, self.__xpd_refgen_lsb)
    @xpd_refgen.setter
    def xpd_refgen(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_refgen_addr, self.__xpd_refgen_msb, self.__xpd_refgen_lsb, value)

    @property
    def adc_dp(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__adc_dp_addr, self.__adc_dp_msb, self.__adc_dp_lsb)
    @adc_dp.setter
    def adc_dp(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__adc_dp_addr, self.__adc_dp_msb, self.__adc_dp_lsb, value)

    @property
    def adc_dn(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__adc_dn_addr, self.__adc_dn_msb, self.__adc_dn_lsb)
    @adc_dn.setter
    def adc_dn(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__adc_dn_addr, self.__adc_dn_msb, self.__adc_dn_lsb, value)

    @property
    def adc_dcm(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__adc_dcm_addr, self.__adc_dcm_msb, self.__adc_dcm_lsb)
    @adc_dcm.setter
    def adc_dcm(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__adc_dcm_addr, self.__adc_dcm_msb, self.__adc_dcm_lsb, value)

    @property
    def adc_bstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__adc_bstb_addr, self.__adc_bstb_msb, self.__adc_bstb_lsb)
    @adc_bstb.setter
    def adc_bstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__adc_bstb_addr, self.__adc_bstb_msb, self.__adc_bstb_lsb, value)

    @property
    def adc_dcal(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__adc_dcal_addr, self.__adc_dcal_msb, self.__adc_dcal_lsb)
    @adc_dcal.setter
    def adc_dcal(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__adc_dcal_addr, self.__adc_dcal_msb, self.__adc_dcal_lsb, value)

    @property
    def adc_delay1(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__adc_delay1_addr, self.__adc_delay1_msb, self.__adc_delay1_lsb)
    @adc_delay1.setter
    def adc_delay1(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__adc_delay1_addr, self.__adc_delay1_msb, self.__adc_delay1_lsb, value)

    @property
    def adc_delay2(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__adc_delay2_addr, self.__adc_delay2_msb, self.__adc_delay2_lsb)
    @adc_delay2.setter
    def adc_delay2(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__adc_delay2_addr, self.__adc_delay2_msb, self.__adc_delay2_lsb, value)

    @property
    def adc_delay3(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__adc_delay3_addr, self.__adc_delay3_msb, self.__adc_delay3_lsb)
    @adc_delay3.setter
    def adc_delay3(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__adc_delay3_addr, self.__adc_delay3_msb, self.__adc_delay3_lsb, value)

    @property
    def adc_delay4(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__adc_delay4_addr, self.__adc_delay4_msb, self.__adc_delay4_lsb)
    @adc_delay4.setter
    def adc_delay4(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__adc_delay4_addr, self.__adc_delay4_msb, self.__adc_delay4_lsb, value)

    @property
    def adc_delay5(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__adc_delay5_addr, self.__adc_delay5_msb, self.__adc_delay5_lsb)
    @adc_delay5.setter
    def adc_delay5(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__adc_delay5_addr, self.__adc_delay5_msb, self.__adc_delay5_lsb, value)

    @property
    def adc_delay6(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__adc_delay6_addr, self.__adc_delay6_msb, self.__adc_delay6_lsb)
    @adc_delay6.setter
    def adc_delay6(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__adc_delay6_addr, self.__adc_delay6_msb, self.__adc_delay6_lsb, value)

    @property
    def adc_bitlmt(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__adc_bitlmt_addr, self.__adc_bitlmt_msb, self.__adc_bitlmt_lsb)
    @adc_bitlmt.setter
    def adc_bitlmt(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__adc_bitlmt_addr, self.__adc_bitlmt_msb, self.__adc_bitlmt_lsb, value)

    @property
    def adc_tmode(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__adc_tmode_addr, self.__adc_tmode_msb, self.__adc_tmode_lsb)
    @adc_tmode.setter
    def adc_tmode(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__adc_tmode_addr, self.__adc_tmode_msb, self.__adc_tmode_lsb, value)

    @property
    def adc_posedgeout(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__adc_posedgeout_addr, self.__adc_posedgeout_msb, self.__adc_posedgeout_lsb)
    @adc_posedgeout.setter
    def adc_posedgeout(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__adc_posedgeout_addr, self.__adc_posedgeout_msb, self.__adc_posedgeout_lsb, value)

    @property
    def adc_endem(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__adc_endem_addr, self.__adc_endem_msb, self.__adc_endem_lsb)
    @adc_endem.setter
    def adc_endem(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__adc_endem_addr, self.__adc_endem_msb, self.__adc_endem_lsb, value)

    @property
    def adc_en_44M(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__adc_en_44M_addr, self.__adc_en_44M_msb, self.__adc_en_44M_lsb)
    @adc_en_44M.setter
    def adc_en_44M(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__adc_en_44M_addr, self.__adc_en_44M_msb, self.__adc_en_44M_lsb, value)

    @property
    def adc_encal(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__adc_encal_addr, self.__adc_encal_msb, self.__adc_encal_lsb)
    @adc_encal.setter
    def adc_encal(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__adc_encal_addr, self.__adc_encal_msb, self.__adc_encal_lsb, value)

    @property
    def adc_rst(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__adc_rst_addr, self.__adc_rst_msb, self.__adc_rst_lsb)
    @adc_rst.setter
    def adc_rst(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__adc_rst_addr, self.__adc_rst_msb, self.__adc_rst_lsb, value)

    @property
    def adc_spare(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__adc_spare_addr, self.__adc_spare_msb, self.__adc_spare_lsb)
    @adc_spare.setter
    def adc_spare(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__adc_spare_addr, self.__adc_spare_msb, self.__adc_spare_lsb, value)

    @property
    def spare_bits0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__spare_bits0_addr, self.__spare_bits0_msb, self.__spare_bits0_lsb)
    @spare_bits0.setter
    def spare_bits0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__spare_bits0_addr, self.__spare_bits0_msb, self.__spare_bits0_lsb, value)

    @property
    def spare_bits1(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__spare_bits1_addr, self.__spare_bits1_msb, self.__spare_bits1_lsb)
    @spare_bits1.setter
    def spare_bits1(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__spare_bits1_addr, self.__spare_bits1_msb, self.__spare_bits1_lsb, value)

    @property
    def spare_bits2_ro(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__spare_bits2_ro_addr, self.__spare_bits2_ro_msb, self.__spare_bits2_ro_lsb)
    @spare_bits2_ro.setter
    def spare_bits2_ro(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__spare_bits2_ro_addr, self.__spare_bits2_ro_msb, self.__spare_bits2_ro_lsb, value)
