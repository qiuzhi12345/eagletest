from hal.common import *
from hal.hwregister.hwi2c.ESP8266.addr_base import *
class DIG_INF(object):
    def __init__(self, channel, chipv = "ESP8266"):
        self.chipv = chipv
        self.channel = channel
        self.__I2C = I2C(self.channel, self.chipv)
        self.__base = DIG_INF_BASE
        self.__hostid = DIG_INF_HOSTID
        self.__freq_rf_a_19_12_lsb = 0
        self.__freq_rf_a_19_12_msb = 7
        self.__freq_rf_a_19_12_addr = 0x0
        self.__freq_rf_a_11_4_lsb = 0
        self.__freq_rf_a_11_4_msb = 7
        self.__freq_rf_a_11_4_addr = 0x1
        self.__freq_rf_a_3_0_lsb = 0
        self.__freq_rf_a_3_0_msb = 3
        self.__freq_rf_a_3_0_addr = 0x2
        self.__freq_dig_b_19_16_lsb = 4
        self.__freq_dig_b_19_16_msb = 7
        self.__freq_dig_b_19_16_addr = 0x2
        self.__freq_dig_b_15_8_lsb = 0
        self.__freq_dig_b_15_8_msb = 7
        self.__freq_dig_b_15_8_addr = 0x3
        self.__freq_dig_b_7_0_lsb = 0
        self.__freq_dig_b_7_0_msb = 7
        self.__freq_dig_b_7_0_addr = 0x4
        self.__dpd_tab_i_11_4_lsb = 0
        self.__dpd_tab_i_11_4_msb = 7
        self.__dpd_tab_i_11_4_addr = 0x5
        self.__dpd_tab_i_3_0_lsb = 0
        self.__dpd_tab_i_3_0_msb = 3
        self.__dpd_tab_i_3_0_addr = 0x6
        self.__dpd_tab_q_11_8_lsb = 4
        self.__dpd_tab_q_11_8_msb = 7
        self.__dpd_tab_q_11_8_addr = 0x6
        self.__dpd_tab_q_7_0_lsb = 0
        self.__dpd_tab_q_7_0_msb = 7
        self.__dpd_tab_q_7_0_addr = 0x7
        self.__dpd_scale_lsb = 0
        self.__dpd_scale_msb = 7
        self.__dpd_scale_addr = 0x8
        self.__tx_scale_lsb = 0
        self.__tx_scale_msb = 7
        self.__tx_scale_addr = 0x9
        self.__tx_i_dc_9_2_lsb = 0
        self.__tx_i_dc_9_2_msb = 7
        self.__tx_i_dc_9_2_addr = 0xa
        self.__tx_i_dc_1_0_lsb = 0
        self.__tx_i_dc_1_0_msb = 1
        self.__tx_i_dc_1_0_addr = 0xb
        self.__tx_q_dc_9_4_lsb = 2
        self.__tx_q_dc_9_4_msb = 7
        self.__tx_q_dc_9_4_addr = 0xb
        self.__tx_q_dc_3_0_lsb = 0
        self.__tx_q_dc_3_0_msb = 3
        self.__tx_q_dc_3_0_addr = 0xc
        self.__tx_i_mask_9_6_lsb = 4
        self.__tx_i_mask_9_6_msb = 7
        self.__tx_i_mask_9_6_addr = 0xc
        self.__tx_i_mask_5_0_lsb = 0
        self.__tx_i_mask_5_0_msb = 5
        self.__tx_i_mask_5_0_addr = 0xd
        self.__tx_q_mask_9_8_lsb = 6
        self.__tx_q_mask_9_8_msb = 7
        self.__tx_q_mask_9_8_addr = 0xd
        self.__tx_q_mask_7_0_lsb = 0
        self.__tx_q_mask_7_0_msb = 7
        self.__tx_q_mask_7_0_addr = 0xe
        self.__ht40_filter_en_lsb = 0
        self.__ht40_filter_en_msb = 0
        self.__ht40_filter_en_addr = 0xf
        self.__dpd_bypass_lsb = 1
        self.__dpd_bypass_msb = 1
        self.__dpd_bypass_addr = 0xf
        self.__dpd_tab_wr_lsb = 2
        self.__dpd_tab_wr_msb = 2
        self.__dpd_tab_wr_addr = 0xf
        self.__tx_interp_bypass_lsb = 3
        self.__tx_interp_bypass_msb = 3
        self.__tx_interp_bypass_addr = 0xf
        self.__tx_filt_gain_lsb = 4
        self.__tx_filt_gain_msb = 4
        self.__tx_filt_gain_addr = 0xf
        self.__tx_edge_sel_lsb = 5
        self.__tx_edge_sel_msb = 5
        self.__tx_edge_sel_addr = 0xf
        self.__tx_i_inv_en_lsb = 6
        self.__tx_i_inv_en_msb = 6
        self.__tx_i_inv_en_addr = 0xf
        self.__tx_q_inv_en_lsb = 7
        self.__tx_q_inv_en_msb = 7
        self.__tx_q_inv_en_addr = 0xf
        self.__tx_iq_swap_en_lsb = 0
        self.__tx_iq_swap_en_msb = 0
        self.__tx_iq_swap_en_addr = 0x10
        self.__tx_most_bit_inv_lsb = 1
        self.__tx_most_bit_inv_msb = 1
        self.__tx_most_bit_inv_addr = 0x10
        self.__tx_iqcorr_enable_lsb = 2
        self.__tx_iqcorr_enable_msb = 2
        self.__tx_iqcorr_enable_addr = 0x10
        self.__tx_q_q_coff_lsb = 3
        self.__tx_q_q_coff_msb = 7
        self.__tx_q_q_coff_addr = 0x10
        self.__tx_q_i_coff_lsb = 0
        self.__tx_q_i_coff_msb = 5
        self.__tx_q_i_coff_addr = 0x11
        self.__tx_iq_coff_sel_lsb = 6
        self.__tx_iq_coff_sel_msb = 6
        self.__tx_iq_coff_sel_addr = 0x11
        self.__rx_iq_coff_sel_lsb = 7
        self.__rx_iq_coff_sel_msb = 7
        self.__rx_iq_coff_sel_addr = 0x11
        self.__rx_scale_lsb = 0
        self.__rx_scale_msb = 7
        self.__rx_scale_addr = 0x12
        self.__rx_i_dc_9_2_lsb = 0
        self.__rx_i_dc_9_2_msb = 7
        self.__rx_i_dc_9_2_addr = 0x13
        self.__rx_i_dc_1_0_lsb = 0
        self.__rx_i_dc_1_0_msb = 1
        self.__rx_i_dc_1_0_addr = 0x14
        self.__rx_q_dc_9_4_lsb = 2
        self.__rx_q_dc_9_4_msb = 7
        self.__rx_q_dc_9_4_addr = 0x14
        self.__rx_q_dc_3_0_lsb = 0
        self.__rx_q_dc_3_0_msb = 3
        self.__rx_q_dc_3_0_addr = 0x15
        self.__rx_i_mask_9_6_lsb = 4
        self.__rx_i_mask_9_6_msb = 7
        self.__rx_i_mask_9_6_addr = 0x15
        self.__rx_i_mask_5_0_lsb = 0
        self.__rx_i_mask_5_0_msb = 5
        self.__rx_i_mask_5_0_addr = 0x16
        self.__rx_q_mask_9_8_lsb = 6
        self.__rx_q_mask_9_8_msb = 7
        self.__rx_q_mask_9_8_addr = 0x16
        self.__rx_q_mask_7_0_lsb = 0
        self.__rx_q_mask_7_0_msb = 7
        self.__rx_q_mask_7_0_addr = 0x17
        self.__rx_interp_bypass_lsb = 0
        self.__rx_interp_bypass_msb = 0
        self.__rx_interp_bypass_addr = 0x18
        self.__rx_filt_gain_lsb = 1
        self.__rx_filt_gain_msb = 1
        self.__rx_filt_gain_addr = 0x18
        self.__rx_edge_sel_lsb = 2
        self.__rx_edge_sel_msb = 2
        self.__rx_edge_sel_addr = 0x18
        self.__rx_i_inv_en_lsb = 3
        self.__rx_i_inv_en_msb = 3
        self.__rx_i_inv_en_addr = 0x18
        self.__rx_q_inv_en_lsb = 4
        self.__rx_q_inv_en_msb = 4
        self.__rx_q_inv_en_addr = 0x18
        self.__rx_iq_swap_en_lsb = 5
        self.__rx_iq_swap_en_msb = 5
        self.__rx_iq_swap_en_addr = 0x18
        self.__rx_most_bit_inv_lsb = 6
        self.__rx_most_bit_inv_msb = 6
        self.__rx_most_bit_inv_addr = 0x18
        self.__rx_iqcorr_enable_lsb = 7
        self.__rx_iqcorr_enable_msb = 7
        self.__rx_iqcorr_enable_addr = 0x18
        self.__rx_q_q_coff_lsb = 0
        self.__rx_q_q_coff_msb = 4
        self.__rx_q_q_coff_addr = 0x19
        self.__rx_q_i_coff_5_3_lsb = 5
        self.__rx_q_i_coff_5_3_msb = 7
        self.__rx_q_i_coff_5_3_addr = 0x19
        self.__rx_q_i_coff_2_0_lsb = 0
        self.__rx_q_i_coff_2_0_msb = 2
        self.__rx_q_i_coff_2_0_addr = 0x1a
        self.__rst_pll_n_lsb = 3
        self.__rst_pll_n_msb = 3
        self.__rst_pll_n_addr = 0x1a
        self.__rst_tx_n_lsb = 4
        self.__rst_tx_n_msb = 4
        self.__rst_tx_n_addr = 0x1a
        self.__rst_rx_n_lsb = 5
        self.__rst_rx_n_msb = 5
        self.__rst_rx_n_addr = 0x1a
        self.__adc_test_80m_lsb = 6
        self.__adc_test_80m_msb = 6
        self.__adc_test_80m_addr = 0x1a
        self.__analog_txtone_en_lsb = 7
        self.__analog_txtone_en_msb = 7
        self.__analog_txtone_en_addr = 0x1a
        self.__dpd_tab_addr_lsb = 0
        self.__dpd_tab_addr_msb = 7
        self.__dpd_tab_addr_addr = 0x1b
        self.__clk_gating_enable_lsb = 0
        self.__clk_gating_enable_msb = 0
        self.__clk_gating_enable_addr = 0x1c
        self.__dac_160m_enable_lsb = 1
        self.__dac_160m_enable_msb = 1
        self.__dac_160m_enable_addr = 0x1c
        self.__adc_80m_enable_lsb = 2
        self.__adc_80m_enable_msb = 2
        self.__adc_80m_enable_addr = 0x1c
        self.__reg_rx_phase_det_cont_en_lsb = 3
        self.__reg_rx_phase_det_cont_en_msb = 3
        self.__reg_rx_phase_det_cont_en_addr = 0x1c
        self.__reg_tx_sync_sel_lsb = 4
        self.__reg_tx_sync_sel_msb = 4
        self.__reg_tx_sync_sel_addr = 0x1c
        self.__reg_rx_clk_force_en_lsb = 5
        self.__reg_rx_clk_force_en_msb = 5
        self.__reg_rx_clk_force_en_addr = 0x1c
        self.__reg_tx_clk_force_en_lsb = 6
        self.__reg_tx_clk_force_en_msb = 6
        self.__reg_tx_clk_force_en_addr = 0x1c
        self.__tx_tone_start_lsb = 7
        self.__tx_tone_start_msb = 7
        self.__tx_tone_start_addr = 0x1c
        self.__reg_adc_iso_force_en_lsb = 0
        self.__reg_adc_iso_force_en_msb = 0
        self.__reg_adc_iso_force_en_addr = 0x1d
        self.__reg_adc_iso_force_lsb = 1
        self.__reg_adc_iso_force_msb = 1
        self.__reg_adc_iso_force_addr = 0x1d
        self.__reg_loop_back_en_lsb = 2
        self.__reg_loop_back_en_msb = 2
        self.__reg_loop_back_en_addr = 0x1d
        self.__tx_local_edge_lsb = 3
        self.__tx_local_edge_msb = 3
        self.__tx_local_edge_addr = 0x1d
        self.__rx_local_edge_lsb = 4
        self.__rx_local_edge_msb = 4
        self.__rx_local_edge_addr = 0x1d
        self.__reg_rx_phase_det_en_lsb = 5
        self.__reg_rx_phase_det_en_msb = 5
        self.__reg_rx_phase_det_en_addr = 0x1d
        self.__reg_rx_sync_sel_lsb = 6
        self.__reg_rx_sync_sel_msb = 6
        self.__reg_rx_sync_sel_addr = 0x1d
        self.__reg_rx_sync_way2_inv_lsb = 7
        self.__reg_rx_sync_way2_inv_msb = 7
        self.__reg_rx_sync_way2_inv_addr = 0x1d
        self.__reg_rx_phase_det_delay_lsb = 0
        self.__reg_rx_phase_det_delay_msb = 7
        self.__reg_rx_phase_det_delay_addr = 0x1e
        self.__reg_tx_phase_det_delay_lsb = 0
        self.__reg_tx_phase_det_delay_msb = 7
        self.__reg_tx_phase_det_delay_addr = 0x1f

    def reg_addr_rd(self,reg_addr):
        return self.__I2C.i2c_rd(self.__base , self.__hostid ,reg_addr)
    def reg_addr_wr(self,reg_addr,value):
        return self.__I2C.i2c_wr(self.__base , self.__hostid ,reg_addr,value)

    @property
    def freq_rf_a_19_12(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__freq_rf_a_19_12_addr, self.__freq_rf_a_19_12_msb, self.__freq_rf_a_19_12_lsb)
    @freq_rf_a_19_12.setter
    def freq_rf_a_19_12(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__freq_rf_a_19_12_addr, self.__freq_rf_a_19_12_msb, self.__freq_rf_a_19_12_lsb, value)

    @property
    def freq_rf_a_11_4(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__freq_rf_a_11_4_addr, self.__freq_rf_a_11_4_msb, self.__freq_rf_a_11_4_lsb)
    @freq_rf_a_11_4.setter
    def freq_rf_a_11_4(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__freq_rf_a_11_4_addr, self.__freq_rf_a_11_4_msb, self.__freq_rf_a_11_4_lsb, value)

    @property
    def freq_rf_a_3_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__freq_rf_a_3_0_addr, self.__freq_rf_a_3_0_msb, self.__freq_rf_a_3_0_lsb)
    @freq_rf_a_3_0.setter
    def freq_rf_a_3_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__freq_rf_a_3_0_addr, self.__freq_rf_a_3_0_msb, self.__freq_rf_a_3_0_lsb, value)

    @property
    def freq_dig_b_19_16(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__freq_dig_b_19_16_addr, self.__freq_dig_b_19_16_msb, self.__freq_dig_b_19_16_lsb)
    @freq_dig_b_19_16.setter
    def freq_dig_b_19_16(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__freq_dig_b_19_16_addr, self.__freq_dig_b_19_16_msb, self.__freq_dig_b_19_16_lsb, value)

    @property
    def freq_dig_b_15_8(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__freq_dig_b_15_8_addr, self.__freq_dig_b_15_8_msb, self.__freq_dig_b_15_8_lsb)
    @freq_dig_b_15_8.setter
    def freq_dig_b_15_8(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__freq_dig_b_15_8_addr, self.__freq_dig_b_15_8_msb, self.__freq_dig_b_15_8_lsb, value)

    @property
    def freq_dig_b_7_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__freq_dig_b_7_0_addr, self.__freq_dig_b_7_0_msb, self.__freq_dig_b_7_0_lsb)
    @freq_dig_b_7_0.setter
    def freq_dig_b_7_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__freq_dig_b_7_0_addr, self.__freq_dig_b_7_0_msb, self.__freq_dig_b_7_0_lsb, value)

    @property
    def dpd_tab_i_11_4(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dpd_tab_i_11_4_addr, self.__dpd_tab_i_11_4_msb, self.__dpd_tab_i_11_4_lsb)
    @dpd_tab_i_11_4.setter
    def dpd_tab_i_11_4(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dpd_tab_i_11_4_addr, self.__dpd_tab_i_11_4_msb, self.__dpd_tab_i_11_4_lsb, value)

    @property
    def dpd_tab_i_3_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dpd_tab_i_3_0_addr, self.__dpd_tab_i_3_0_msb, self.__dpd_tab_i_3_0_lsb)
    @dpd_tab_i_3_0.setter
    def dpd_tab_i_3_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dpd_tab_i_3_0_addr, self.__dpd_tab_i_3_0_msb, self.__dpd_tab_i_3_0_lsb, value)

    @property
    def dpd_tab_q_11_8(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dpd_tab_q_11_8_addr, self.__dpd_tab_q_11_8_msb, self.__dpd_tab_q_11_8_lsb)
    @dpd_tab_q_11_8.setter
    def dpd_tab_q_11_8(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dpd_tab_q_11_8_addr, self.__dpd_tab_q_11_8_msb, self.__dpd_tab_q_11_8_lsb, value)

    @property
    def dpd_tab_q_7_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dpd_tab_q_7_0_addr, self.__dpd_tab_q_7_0_msb, self.__dpd_tab_q_7_0_lsb)
    @dpd_tab_q_7_0.setter
    def dpd_tab_q_7_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dpd_tab_q_7_0_addr, self.__dpd_tab_q_7_0_msb, self.__dpd_tab_q_7_0_lsb, value)

    @property
    def dpd_scale(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dpd_scale_addr, self.__dpd_scale_msb, self.__dpd_scale_lsb)
    @dpd_scale.setter
    def dpd_scale(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dpd_scale_addr, self.__dpd_scale_msb, self.__dpd_scale_lsb, value)

    @property
    def tx_scale(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tx_scale_addr, self.__tx_scale_msb, self.__tx_scale_lsb)
    @tx_scale.setter
    def tx_scale(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tx_scale_addr, self.__tx_scale_msb, self.__tx_scale_lsb, value)

    @property
    def tx_i_dc_9_2(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tx_i_dc_9_2_addr, self.__tx_i_dc_9_2_msb, self.__tx_i_dc_9_2_lsb)
    @tx_i_dc_9_2.setter
    def tx_i_dc_9_2(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tx_i_dc_9_2_addr, self.__tx_i_dc_9_2_msb, self.__tx_i_dc_9_2_lsb, value)

    @property
    def tx_i_dc_1_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tx_i_dc_1_0_addr, self.__tx_i_dc_1_0_msb, self.__tx_i_dc_1_0_lsb)
    @tx_i_dc_1_0.setter
    def tx_i_dc_1_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tx_i_dc_1_0_addr, self.__tx_i_dc_1_0_msb, self.__tx_i_dc_1_0_lsb, value)

    @property
    def tx_q_dc_9_4(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tx_q_dc_9_4_addr, self.__tx_q_dc_9_4_msb, self.__tx_q_dc_9_4_lsb)
    @tx_q_dc_9_4.setter
    def tx_q_dc_9_4(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tx_q_dc_9_4_addr, self.__tx_q_dc_9_4_msb, self.__tx_q_dc_9_4_lsb, value)

    @property
    def tx_q_dc_3_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tx_q_dc_3_0_addr, self.__tx_q_dc_3_0_msb, self.__tx_q_dc_3_0_lsb)
    @tx_q_dc_3_0.setter
    def tx_q_dc_3_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tx_q_dc_3_0_addr, self.__tx_q_dc_3_0_msb, self.__tx_q_dc_3_0_lsb, value)

    @property
    def tx_i_mask_9_6(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tx_i_mask_9_6_addr, self.__tx_i_mask_9_6_msb, self.__tx_i_mask_9_6_lsb)
    @tx_i_mask_9_6.setter
    def tx_i_mask_9_6(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tx_i_mask_9_6_addr, self.__tx_i_mask_9_6_msb, self.__tx_i_mask_9_6_lsb, value)

    @property
    def tx_i_mask_5_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tx_i_mask_5_0_addr, self.__tx_i_mask_5_0_msb, self.__tx_i_mask_5_0_lsb)
    @tx_i_mask_5_0.setter
    def tx_i_mask_5_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tx_i_mask_5_0_addr, self.__tx_i_mask_5_0_msb, self.__tx_i_mask_5_0_lsb, value)

    @property
    def tx_q_mask_9_8(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tx_q_mask_9_8_addr, self.__tx_q_mask_9_8_msb, self.__tx_q_mask_9_8_lsb)
    @tx_q_mask_9_8.setter
    def tx_q_mask_9_8(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tx_q_mask_9_8_addr, self.__tx_q_mask_9_8_msb, self.__tx_q_mask_9_8_lsb, value)

    @property
    def tx_q_mask_7_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tx_q_mask_7_0_addr, self.__tx_q_mask_7_0_msb, self.__tx_q_mask_7_0_lsb)
    @tx_q_mask_7_0.setter
    def tx_q_mask_7_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tx_q_mask_7_0_addr, self.__tx_q_mask_7_0_msb, self.__tx_q_mask_7_0_lsb, value)

    @property
    def ht40_filter_en(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ht40_filter_en_addr, self.__ht40_filter_en_msb, self.__ht40_filter_en_lsb)
    @ht40_filter_en.setter
    def ht40_filter_en(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ht40_filter_en_addr, self.__ht40_filter_en_msb, self.__ht40_filter_en_lsb, value)

    @property
    def dpd_bypass(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dpd_bypass_addr, self.__dpd_bypass_msb, self.__dpd_bypass_lsb)
    @dpd_bypass.setter
    def dpd_bypass(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dpd_bypass_addr, self.__dpd_bypass_msb, self.__dpd_bypass_lsb, value)

    @property
    def dpd_tab_wr(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dpd_tab_wr_addr, self.__dpd_tab_wr_msb, self.__dpd_tab_wr_lsb)
    @dpd_tab_wr.setter
    def dpd_tab_wr(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dpd_tab_wr_addr, self.__dpd_tab_wr_msb, self.__dpd_tab_wr_lsb, value)

    @property
    def tx_interp_bypass(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tx_interp_bypass_addr, self.__tx_interp_bypass_msb, self.__tx_interp_bypass_lsb)
    @tx_interp_bypass.setter
    def tx_interp_bypass(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tx_interp_bypass_addr, self.__tx_interp_bypass_msb, self.__tx_interp_bypass_lsb, value)

    @property
    def tx_filt_gain(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tx_filt_gain_addr, self.__tx_filt_gain_msb, self.__tx_filt_gain_lsb)
    @tx_filt_gain.setter
    def tx_filt_gain(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tx_filt_gain_addr, self.__tx_filt_gain_msb, self.__tx_filt_gain_lsb, value)

    @property
    def tx_edge_sel(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tx_edge_sel_addr, self.__tx_edge_sel_msb, self.__tx_edge_sel_lsb)
    @tx_edge_sel.setter
    def tx_edge_sel(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tx_edge_sel_addr, self.__tx_edge_sel_msb, self.__tx_edge_sel_lsb, value)

    @property
    def tx_i_inv_en(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tx_i_inv_en_addr, self.__tx_i_inv_en_msb, self.__tx_i_inv_en_lsb)
    @tx_i_inv_en.setter
    def tx_i_inv_en(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tx_i_inv_en_addr, self.__tx_i_inv_en_msb, self.__tx_i_inv_en_lsb, value)

    @property
    def tx_q_inv_en(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tx_q_inv_en_addr, self.__tx_q_inv_en_msb, self.__tx_q_inv_en_lsb)
    @tx_q_inv_en.setter
    def tx_q_inv_en(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tx_q_inv_en_addr, self.__tx_q_inv_en_msb, self.__tx_q_inv_en_lsb, value)

    @property
    def tx_iq_swap_en(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tx_iq_swap_en_addr, self.__tx_iq_swap_en_msb, self.__tx_iq_swap_en_lsb)
    @tx_iq_swap_en.setter
    def tx_iq_swap_en(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tx_iq_swap_en_addr, self.__tx_iq_swap_en_msb, self.__tx_iq_swap_en_lsb, value)

    @property
    def tx_most_bit_inv(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tx_most_bit_inv_addr, self.__tx_most_bit_inv_msb, self.__tx_most_bit_inv_lsb)
    @tx_most_bit_inv.setter
    def tx_most_bit_inv(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tx_most_bit_inv_addr, self.__tx_most_bit_inv_msb, self.__tx_most_bit_inv_lsb, value)

    @property
    def tx_iqcorr_enable(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tx_iqcorr_enable_addr, self.__tx_iqcorr_enable_msb, self.__tx_iqcorr_enable_lsb)
    @tx_iqcorr_enable.setter
    def tx_iqcorr_enable(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tx_iqcorr_enable_addr, self.__tx_iqcorr_enable_msb, self.__tx_iqcorr_enable_lsb, value)

    @property
    def tx_q_q_coff(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tx_q_q_coff_addr, self.__tx_q_q_coff_msb, self.__tx_q_q_coff_lsb)
    @tx_q_q_coff.setter
    def tx_q_q_coff(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tx_q_q_coff_addr, self.__tx_q_q_coff_msb, self.__tx_q_q_coff_lsb, value)

    @property
    def tx_q_i_coff(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tx_q_i_coff_addr, self.__tx_q_i_coff_msb, self.__tx_q_i_coff_lsb)
    @tx_q_i_coff.setter
    def tx_q_i_coff(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tx_q_i_coff_addr, self.__tx_q_i_coff_msb, self.__tx_q_i_coff_lsb, value)

    @property
    def tx_iq_coff_sel(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tx_iq_coff_sel_addr, self.__tx_iq_coff_sel_msb, self.__tx_iq_coff_sel_lsb)
    @tx_iq_coff_sel.setter
    def tx_iq_coff_sel(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tx_iq_coff_sel_addr, self.__tx_iq_coff_sel_msb, self.__tx_iq_coff_sel_lsb, value)

    @property
    def rx_iq_coff_sel(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rx_iq_coff_sel_addr, self.__rx_iq_coff_sel_msb, self.__rx_iq_coff_sel_lsb)
    @rx_iq_coff_sel.setter
    def rx_iq_coff_sel(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rx_iq_coff_sel_addr, self.__rx_iq_coff_sel_msb, self.__rx_iq_coff_sel_lsb, value)

    @property
    def rx_scale(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rx_scale_addr, self.__rx_scale_msb, self.__rx_scale_lsb)
    @rx_scale.setter
    def rx_scale(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rx_scale_addr, self.__rx_scale_msb, self.__rx_scale_lsb, value)

    @property
    def rx_i_dc_9_2(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rx_i_dc_9_2_addr, self.__rx_i_dc_9_2_msb, self.__rx_i_dc_9_2_lsb)
    @rx_i_dc_9_2.setter
    def rx_i_dc_9_2(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rx_i_dc_9_2_addr, self.__rx_i_dc_9_2_msb, self.__rx_i_dc_9_2_lsb, value)

    @property
    def rx_i_dc_1_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rx_i_dc_1_0_addr, self.__rx_i_dc_1_0_msb, self.__rx_i_dc_1_0_lsb)
    @rx_i_dc_1_0.setter
    def rx_i_dc_1_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rx_i_dc_1_0_addr, self.__rx_i_dc_1_0_msb, self.__rx_i_dc_1_0_lsb, value)

    @property
    def rx_q_dc_9_4(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rx_q_dc_9_4_addr, self.__rx_q_dc_9_4_msb, self.__rx_q_dc_9_4_lsb)
    @rx_q_dc_9_4.setter
    def rx_q_dc_9_4(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rx_q_dc_9_4_addr, self.__rx_q_dc_9_4_msb, self.__rx_q_dc_9_4_lsb, value)

    @property
    def rx_q_dc_3_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rx_q_dc_3_0_addr, self.__rx_q_dc_3_0_msb, self.__rx_q_dc_3_0_lsb)
    @rx_q_dc_3_0.setter
    def rx_q_dc_3_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rx_q_dc_3_0_addr, self.__rx_q_dc_3_0_msb, self.__rx_q_dc_3_0_lsb, value)

    @property
    def rx_i_mask_9_6(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rx_i_mask_9_6_addr, self.__rx_i_mask_9_6_msb, self.__rx_i_mask_9_6_lsb)
    @rx_i_mask_9_6.setter
    def rx_i_mask_9_6(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rx_i_mask_9_6_addr, self.__rx_i_mask_9_6_msb, self.__rx_i_mask_9_6_lsb, value)

    @property
    def rx_i_mask_5_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rx_i_mask_5_0_addr, self.__rx_i_mask_5_0_msb, self.__rx_i_mask_5_0_lsb)
    @rx_i_mask_5_0.setter
    def rx_i_mask_5_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rx_i_mask_5_0_addr, self.__rx_i_mask_5_0_msb, self.__rx_i_mask_5_0_lsb, value)

    @property
    def rx_q_mask_9_8(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rx_q_mask_9_8_addr, self.__rx_q_mask_9_8_msb, self.__rx_q_mask_9_8_lsb)
    @rx_q_mask_9_8.setter
    def rx_q_mask_9_8(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rx_q_mask_9_8_addr, self.__rx_q_mask_9_8_msb, self.__rx_q_mask_9_8_lsb, value)

    @property
    def rx_q_mask_7_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rx_q_mask_7_0_addr, self.__rx_q_mask_7_0_msb, self.__rx_q_mask_7_0_lsb)
    @rx_q_mask_7_0.setter
    def rx_q_mask_7_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rx_q_mask_7_0_addr, self.__rx_q_mask_7_0_msb, self.__rx_q_mask_7_0_lsb, value)

    @property
    def rx_interp_bypass(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rx_interp_bypass_addr, self.__rx_interp_bypass_msb, self.__rx_interp_bypass_lsb)
    @rx_interp_bypass.setter
    def rx_interp_bypass(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rx_interp_bypass_addr, self.__rx_interp_bypass_msb, self.__rx_interp_bypass_lsb, value)

    @property
    def rx_filt_gain(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rx_filt_gain_addr, self.__rx_filt_gain_msb, self.__rx_filt_gain_lsb)
    @rx_filt_gain.setter
    def rx_filt_gain(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rx_filt_gain_addr, self.__rx_filt_gain_msb, self.__rx_filt_gain_lsb, value)

    @property
    def rx_edge_sel(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rx_edge_sel_addr, self.__rx_edge_sel_msb, self.__rx_edge_sel_lsb)
    @rx_edge_sel.setter
    def rx_edge_sel(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rx_edge_sel_addr, self.__rx_edge_sel_msb, self.__rx_edge_sel_lsb, value)

    @property
    def rx_i_inv_en(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rx_i_inv_en_addr, self.__rx_i_inv_en_msb, self.__rx_i_inv_en_lsb)
    @rx_i_inv_en.setter
    def rx_i_inv_en(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rx_i_inv_en_addr, self.__rx_i_inv_en_msb, self.__rx_i_inv_en_lsb, value)

    @property
    def rx_q_inv_en(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rx_q_inv_en_addr, self.__rx_q_inv_en_msb, self.__rx_q_inv_en_lsb)
    @rx_q_inv_en.setter
    def rx_q_inv_en(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rx_q_inv_en_addr, self.__rx_q_inv_en_msb, self.__rx_q_inv_en_lsb, value)

    @property
    def rx_iq_swap_en(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rx_iq_swap_en_addr, self.__rx_iq_swap_en_msb, self.__rx_iq_swap_en_lsb)
    @rx_iq_swap_en.setter
    def rx_iq_swap_en(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rx_iq_swap_en_addr, self.__rx_iq_swap_en_msb, self.__rx_iq_swap_en_lsb, value)

    @property
    def rx_most_bit_inv(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rx_most_bit_inv_addr, self.__rx_most_bit_inv_msb, self.__rx_most_bit_inv_lsb)
    @rx_most_bit_inv.setter
    def rx_most_bit_inv(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rx_most_bit_inv_addr, self.__rx_most_bit_inv_msb, self.__rx_most_bit_inv_lsb, value)

    @property
    def rx_iqcorr_enable(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rx_iqcorr_enable_addr, self.__rx_iqcorr_enable_msb, self.__rx_iqcorr_enable_lsb)
    @rx_iqcorr_enable.setter
    def rx_iqcorr_enable(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rx_iqcorr_enable_addr, self.__rx_iqcorr_enable_msb, self.__rx_iqcorr_enable_lsb, value)

    @property
    def rx_q_q_coff(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rx_q_q_coff_addr, self.__rx_q_q_coff_msb, self.__rx_q_q_coff_lsb)
    @rx_q_q_coff.setter
    def rx_q_q_coff(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rx_q_q_coff_addr, self.__rx_q_q_coff_msb, self.__rx_q_q_coff_lsb, value)

    @property
    def rx_q_i_coff_5_3(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rx_q_i_coff_5_3_addr, self.__rx_q_i_coff_5_3_msb, self.__rx_q_i_coff_5_3_lsb)
    @rx_q_i_coff_5_3.setter
    def rx_q_i_coff_5_3(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rx_q_i_coff_5_3_addr, self.__rx_q_i_coff_5_3_msb, self.__rx_q_i_coff_5_3_lsb, value)

    @property
    def rx_q_i_coff_2_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rx_q_i_coff_2_0_addr, self.__rx_q_i_coff_2_0_msb, self.__rx_q_i_coff_2_0_lsb)
    @rx_q_i_coff_2_0.setter
    def rx_q_i_coff_2_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rx_q_i_coff_2_0_addr, self.__rx_q_i_coff_2_0_msb, self.__rx_q_i_coff_2_0_lsb, value)

    @property
    def rst_pll_n(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rst_pll_n_addr, self.__rst_pll_n_msb, self.__rst_pll_n_lsb)
    @rst_pll_n.setter
    def rst_pll_n(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rst_pll_n_addr, self.__rst_pll_n_msb, self.__rst_pll_n_lsb, value)

    @property
    def rst_tx_n(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rst_tx_n_addr, self.__rst_tx_n_msb, self.__rst_tx_n_lsb)
    @rst_tx_n.setter
    def rst_tx_n(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rst_tx_n_addr, self.__rst_tx_n_msb, self.__rst_tx_n_lsb, value)

    @property
    def rst_rx_n(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rst_rx_n_addr, self.__rst_rx_n_msb, self.__rst_rx_n_lsb)
    @rst_rx_n.setter
    def rst_rx_n(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rst_rx_n_addr, self.__rst_rx_n_msb, self.__rst_rx_n_lsb, value)

    @property
    def adc_test_80m(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__adc_test_80m_addr, self.__adc_test_80m_msb, self.__adc_test_80m_lsb)
    @adc_test_80m.setter
    def adc_test_80m(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__adc_test_80m_addr, self.__adc_test_80m_msb, self.__adc_test_80m_lsb, value)

    @property
    def analog_txtone_en(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__analog_txtone_en_addr, self.__analog_txtone_en_msb, self.__analog_txtone_en_lsb)
    @analog_txtone_en.setter
    def analog_txtone_en(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__analog_txtone_en_addr, self.__analog_txtone_en_msb, self.__analog_txtone_en_lsb, value)

    @property
    def dpd_tab_addr(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dpd_tab_addr_addr, self.__dpd_tab_addr_msb, self.__dpd_tab_addr_lsb)
    @dpd_tab_addr.setter
    def dpd_tab_addr(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dpd_tab_addr_addr, self.__dpd_tab_addr_msb, self.__dpd_tab_addr_lsb, value)

    @property
    def clk_gating_enable(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__clk_gating_enable_addr, self.__clk_gating_enable_msb, self.__clk_gating_enable_lsb)
    @clk_gating_enable.setter
    def clk_gating_enable(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__clk_gating_enable_addr, self.__clk_gating_enable_msb, self.__clk_gating_enable_lsb, value)

    @property
    def dac_160m_enable(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dac_160m_enable_addr, self.__dac_160m_enable_msb, self.__dac_160m_enable_lsb)
    @dac_160m_enable.setter
    def dac_160m_enable(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dac_160m_enable_addr, self.__dac_160m_enable_msb, self.__dac_160m_enable_lsb, value)

    @property
    def adc_80m_enable(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__adc_80m_enable_addr, self.__adc_80m_enable_msb, self.__adc_80m_enable_lsb)
    @adc_80m_enable.setter
    def adc_80m_enable(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__adc_80m_enable_addr, self.__adc_80m_enable_msb, self.__adc_80m_enable_lsb, value)

    @property
    def reg_rx_phase_det_cont_en(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__reg_rx_phase_det_cont_en_addr, self.__reg_rx_phase_det_cont_en_msb, self.__reg_rx_phase_det_cont_en_lsb)
    @reg_rx_phase_det_cont_en.setter
    def reg_rx_phase_det_cont_en(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__reg_rx_phase_det_cont_en_addr, self.__reg_rx_phase_det_cont_en_msb, self.__reg_rx_phase_det_cont_en_lsb, value)

    @property
    def reg_tx_sync_sel(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__reg_tx_sync_sel_addr, self.__reg_tx_sync_sel_msb, self.__reg_tx_sync_sel_lsb)
    @reg_tx_sync_sel.setter
    def reg_tx_sync_sel(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__reg_tx_sync_sel_addr, self.__reg_tx_sync_sel_msb, self.__reg_tx_sync_sel_lsb, value)

    @property
    def reg_rx_clk_force_en(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__reg_rx_clk_force_en_addr, self.__reg_rx_clk_force_en_msb, self.__reg_rx_clk_force_en_lsb)
    @reg_rx_clk_force_en.setter
    def reg_rx_clk_force_en(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__reg_rx_clk_force_en_addr, self.__reg_rx_clk_force_en_msb, self.__reg_rx_clk_force_en_lsb, value)

    @property
    def reg_tx_clk_force_en(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__reg_tx_clk_force_en_addr, self.__reg_tx_clk_force_en_msb, self.__reg_tx_clk_force_en_lsb)
    @reg_tx_clk_force_en.setter
    def reg_tx_clk_force_en(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__reg_tx_clk_force_en_addr, self.__reg_tx_clk_force_en_msb, self.__reg_tx_clk_force_en_lsb, value)

    @property
    def tx_tone_start(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tx_tone_start_addr, self.__tx_tone_start_msb, self.__tx_tone_start_lsb)
    @tx_tone_start.setter
    def tx_tone_start(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tx_tone_start_addr, self.__tx_tone_start_msb, self.__tx_tone_start_lsb, value)

    @property
    def reg_adc_iso_force_en(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__reg_adc_iso_force_en_addr, self.__reg_adc_iso_force_en_msb, self.__reg_adc_iso_force_en_lsb)
    @reg_adc_iso_force_en.setter
    def reg_adc_iso_force_en(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__reg_adc_iso_force_en_addr, self.__reg_adc_iso_force_en_msb, self.__reg_adc_iso_force_en_lsb, value)

    @property
    def reg_adc_iso_force(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__reg_adc_iso_force_addr, self.__reg_adc_iso_force_msb, self.__reg_adc_iso_force_lsb)
    @reg_adc_iso_force.setter
    def reg_adc_iso_force(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__reg_adc_iso_force_addr, self.__reg_adc_iso_force_msb, self.__reg_adc_iso_force_lsb, value)

    @property
    def reg_loop_back_en(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__reg_loop_back_en_addr, self.__reg_loop_back_en_msb, self.__reg_loop_back_en_lsb)
    @reg_loop_back_en.setter
    def reg_loop_back_en(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__reg_loop_back_en_addr, self.__reg_loop_back_en_msb, self.__reg_loop_back_en_lsb, value)

    @property
    def tx_local_edge(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tx_local_edge_addr, self.__tx_local_edge_msb, self.__tx_local_edge_lsb)
    @tx_local_edge.setter
    def tx_local_edge(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tx_local_edge_addr, self.__tx_local_edge_msb, self.__tx_local_edge_lsb, value)

    @property
    def rx_local_edge(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__rx_local_edge_addr, self.__rx_local_edge_msb, self.__rx_local_edge_lsb)
    @rx_local_edge.setter
    def rx_local_edge(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__rx_local_edge_addr, self.__rx_local_edge_msb, self.__rx_local_edge_lsb, value)

    @property
    def reg_rx_phase_det_en(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__reg_rx_phase_det_en_addr, self.__reg_rx_phase_det_en_msb, self.__reg_rx_phase_det_en_lsb)
    @reg_rx_phase_det_en.setter
    def reg_rx_phase_det_en(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__reg_rx_phase_det_en_addr, self.__reg_rx_phase_det_en_msb, self.__reg_rx_phase_det_en_lsb, value)

    @property
    def reg_rx_sync_sel(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__reg_rx_sync_sel_addr, self.__reg_rx_sync_sel_msb, self.__reg_rx_sync_sel_lsb)
    @reg_rx_sync_sel.setter
    def reg_rx_sync_sel(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__reg_rx_sync_sel_addr, self.__reg_rx_sync_sel_msb, self.__reg_rx_sync_sel_lsb, value)

    @property
    def reg_rx_sync_way2_inv(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__reg_rx_sync_way2_inv_addr, self.__reg_rx_sync_way2_inv_msb, self.__reg_rx_sync_way2_inv_lsb)
    @reg_rx_sync_way2_inv.setter
    def reg_rx_sync_way2_inv(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__reg_rx_sync_way2_inv_addr, self.__reg_rx_sync_way2_inv_msb, self.__reg_rx_sync_way2_inv_lsb, value)

    @property
    def reg_rx_phase_det_delay(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__reg_rx_phase_det_delay_addr, self.__reg_rx_phase_det_delay_msb, self.__reg_rx_phase_det_delay_lsb)
    @reg_rx_phase_det_delay.setter
    def reg_rx_phase_det_delay(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__reg_rx_phase_det_delay_addr, self.__reg_rx_phase_det_delay_msb, self.__reg_rx_phase_det_delay_lsb, value)

    @property
    def reg_tx_phase_det_delay(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__reg_tx_phase_det_delay_addr, self.__reg_tx_phase_det_delay_msb, self.__reg_tx_phase_det_delay_lsb)
    @reg_tx_phase_det_delay.setter
    def reg_tx_phase_det_delay(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__reg_tx_phase_det_delay_addr, self.__reg_tx_phase_det_delay_msb, self.__reg_tx_phase_det_delay_lsb, value)
