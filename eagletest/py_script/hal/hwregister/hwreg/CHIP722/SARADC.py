from hal.common import *
from hal.hwregister.hwreg.CHIP722.addr_base import *
class SARADC(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.SAR_READER1_CTRL = SAR_READER1_CTRL(self.channel, self.chipv)
        self.SAR_READER1_STATUS = SAR_READER1_STATUS(self.channel, self.chipv)
        self.SAR_MEAS1_CTRL1 = SAR_MEAS1_CTRL1(self.channel, self.chipv)
        self.SAR_MEAS1_CTRL2 = SAR_MEAS1_CTRL2(self.channel, self.chipv)
        self.SAR_MEAS1_MUX = SAR_MEAS1_MUX(self.channel, self.chipv)
        self.SAR_ATTEN1 = SAR_ATTEN1(self.channel, self.chipv)
        self.SAR_AMP_CTRL1 = SAR_AMP_CTRL1(self.channel, self.chipv)
        self.SAR_AMP_CTRL2 = SAR_AMP_CTRL2(self.channel, self.chipv)
        self.SAR_AMP_CTRL3 = SAR_AMP_CTRL3(self.channel, self.chipv)
        self.SAR_READER2_CTRL = SAR_READER2_CTRL(self.channel, self.chipv)
        self.SAR_READER2_STATUS = SAR_READER2_STATUS(self.channel, self.chipv)
        self.SAR_MEAS2_CTRL1 = SAR_MEAS2_CTRL1(self.channel, self.chipv)
        self.SAR_MEAS2_CTRL2 = SAR_MEAS2_CTRL2(self.channel, self.chipv)
        self.SAR_MEAS2_MUX = SAR_MEAS2_MUX(self.channel, self.chipv)
        self.SAR_ATTEN2 = SAR_ATTEN2(self.channel, self.chipv)
        self.SAR_POWER_XPD_SAR = SAR_POWER_XPD_SAR(self.channel, self.chipv)
        self.SAR_SLAVE_ADDR1 = SAR_SLAVE_ADDR1(self.channel, self.chipv)
        self.SAR_SLAVE_ADDR2 = SAR_SLAVE_ADDR2(self.channel, self.chipv)
        self.SAR_SLAVE_ADDR3 = SAR_SLAVE_ADDR3(self.channel, self.chipv)
        self.SAR_SLAVE_ADDR4 = SAR_SLAVE_ADDR4(self.channel, self.chipv)
        self.SAR_TSENS_CTRL = SAR_TSENS_CTRL(self.channel, self.chipv)
        self.SAR_TSENS_CTRL2 = SAR_TSENS_CTRL2(self.channel, self.chipv)
        self.SAR_I2C_CTRL = SAR_I2C_CTRL(self.channel, self.chipv)
        self.SAR_TOUCH_CONF = SAR_TOUCH_CONF(self.channel, self.chipv)
        self.SAR_TOUCH_THRES1 = SAR_TOUCH_THRES1(self.channel, self.chipv)
        self.SAR_TOUCH_THRES2 = SAR_TOUCH_THRES2(self.channel, self.chipv)
        self.SAR_TOUCH_THRES3 = SAR_TOUCH_THRES3(self.channel, self.chipv)
        self.SAR_TOUCH_THRES4 = SAR_TOUCH_THRES4(self.channel, self.chipv)
        self.SAR_TOUCH_THRES5 = SAR_TOUCH_THRES5(self.channel, self.chipv)
        self.SAR_TOUCH_THRES6 = SAR_TOUCH_THRES6(self.channel, self.chipv)
        self.SAR_TOUCH_THRES7 = SAR_TOUCH_THRES7(self.channel, self.chipv)
        self.SAR_TOUCH_THRES8 = SAR_TOUCH_THRES8(self.channel, self.chipv)
        self.SAR_TOUCH_THRES9 = SAR_TOUCH_THRES9(self.channel, self.chipv)
        self.SAR_TOUCH_THRES10 = SAR_TOUCH_THRES10(self.channel, self.chipv)
        self.SAR_TOUCH_THRES11 = SAR_TOUCH_THRES11(self.channel, self.chipv)
        self.SAR_TOUCH_THRES12 = SAR_TOUCH_THRES12(self.channel, self.chipv)
        self.SAR_TOUCH_THRES13 = SAR_TOUCH_THRES13(self.channel, self.chipv)
        self.SAR_TOUCH_THRES14 = SAR_TOUCH_THRES14(self.channel, self.chipv)
        self.SAR_TOUCH_OUT0 = SAR_TOUCH_OUT0(self.channel, self.chipv)
        self.SAR_TOUCH_OUT1 = SAR_TOUCH_OUT1(self.channel, self.chipv)
        self.SAR_TOUCH_OUT2 = SAR_TOUCH_OUT2(self.channel, self.chipv)
        self.SAR_TOUCH_OUT3 = SAR_TOUCH_OUT3(self.channel, self.chipv)
        self.SAR_TOUCH_OUT4 = SAR_TOUCH_OUT4(self.channel, self.chipv)
        self.SAR_TOUCH_OUT5 = SAR_TOUCH_OUT5(self.channel, self.chipv)
        self.SAR_TOUCH_OUT6 = SAR_TOUCH_OUT6(self.channel, self.chipv)
        self.SAR_TOUCH_OUT7 = SAR_TOUCH_OUT7(self.channel, self.chipv)
        self.SAR_TOUCH_OUT8 = SAR_TOUCH_OUT8(self.channel, self.chipv)
        self.SAR_TOUCH_OUT9 = SAR_TOUCH_OUT9(self.channel, self.chipv)
        self.SAR_TOUCH_OUT10 = SAR_TOUCH_OUT10(self.channel, self.chipv)
        self.SAR_TOUCH_OUT11 = SAR_TOUCH_OUT11(self.channel, self.chipv)
        self.SAR_TOUCH_OUT12 = SAR_TOUCH_OUT12(self.channel, self.chipv)
        self.SAR_TOUCH_OUT13 = SAR_TOUCH_OUT13(self.channel, self.chipv)
        self.SAR_TOUCH_OUT14 = SAR_TOUCH_OUT14(self.channel, self.chipv)
        self.SAR_TOUCH_CHN_ST = SAR_TOUCH_CHN_ST(self.channel, self.chipv)
        self.SAR_TOUCH_STATUS0 = SAR_TOUCH_STATUS0(self.channel, self.chipv)
        self.SAR_TOUCH_STATUS1 = SAR_TOUCH_STATUS1(self.channel, self.chipv)
        self.SAR_TOUCH_STATUS2 = SAR_TOUCH_STATUS2(self.channel, self.chipv)
        self.SAR_TOUCH_STATUS3 = SAR_TOUCH_STATUS3(self.channel, self.chipv)
        self.SAR_TOUCH_STATUS4 = SAR_TOUCH_STATUS4(self.channel, self.chipv)
        self.SAR_TOUCH_STATUS5 = SAR_TOUCH_STATUS5(self.channel, self.chipv)
        self.SAR_TOUCH_STATUS6 = SAR_TOUCH_STATUS6(self.channel, self.chipv)
        self.SAR_TOUCH_STATUS7 = SAR_TOUCH_STATUS7(self.channel, self.chipv)
        self.SAR_TOUCH_STATUS8 = SAR_TOUCH_STATUS8(self.channel, self.chipv)
        self.SAR_TOUCH_STATUS9 = SAR_TOUCH_STATUS9(self.channel, self.chipv)
        self.SAR_TOUCH_STATUS10 = SAR_TOUCH_STATUS10(self.channel, self.chipv)
        self.SAR_TOUCH_STATUS11 = SAR_TOUCH_STATUS11(self.channel, self.chipv)
        self.SAR_TOUCH_STATUS12 = SAR_TOUCH_STATUS12(self.channel, self.chipv)
        self.SAR_TOUCH_STATUS13 = SAR_TOUCH_STATUS13(self.channel, self.chipv)
        self.SAR_TOUCH_STATUS14 = SAR_TOUCH_STATUS14(self.channel, self.chipv)
        self.SAR_TOUCH_STATUS15 = SAR_TOUCH_STATUS15(self.channel, self.chipv)
        self.SAR_TOUCH_STATUS16 = SAR_TOUCH_STATUS16(self.channel, self.chipv)
        self.SAR_DAC_CTRL1 = SAR_DAC_CTRL1(self.channel, self.chipv)
        self.SAR_DAC_CTRL2 = SAR_DAC_CTRL2(self.channel, self.chipv)
        self.SAR_COCPU_STATE = SAR_COCPU_STATE(self.channel, self.chipv)
        self.SAR_COCPU_INT_RAW = SAR_COCPU_INT_RAW(self.channel, self.chipv)
        self.SAR_COCPU_INT_ENA = SAR_COCPU_INT_ENA(self.channel, self.chipv)
        self.SAR_COCPU_INT_ST = SAR_COCPU_INT_ST(self.channel, self.chipv)
        self.SAR_COCPU_INT_CLR = SAR_COCPU_INT_CLR(self.channel, self.chipv)
        self.SAR_COCPU_DEBUG = SAR_COCPU_DEBUG(self.channel, self.chipv)
        self.SAR_HALL_CTRL = SAR_HALL_CTRL(self.channel, self.chipv)
        self.SAR_NOUSE = SAR_NOUSE(self.channel, self.chipv)
        self.SARDATE = SARDATE(self.channel, self.chipv)
class SAR_READER1_CTRL(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x0
        self.__reg_sar1_int_en_lsb = 29
        self.__reg_sar1_int_en_msb = 29
        self.__reg_sar1_data_inv_lsb = 28
        self.__reg_sar1_data_inv_msb = 28
        self.__reg_sar1_sample_num_lsb = 19
        self.__reg_sar1_sample_num_msb = 26
        self.__reg_sar1_clk_gated_lsb = 18
        self.__reg_sar1_clk_gated_msb = 18
        self.__reg_sar1_sample_bit_lsb = 16
        self.__reg_sar1_sample_bit_msb = 17
        self.__reg_sar1_sample_cycle_lsb = 8
        self.__reg_sar1_sample_cycle_msb = 15
        self.__reg_sar1_clk_div_lsb = 0
        self.__reg_sar1_clk_div_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sar1_int_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar1_int_en_msb, self.__reg_sar1_int_en_lsb)
    @reg_sar1_int_en.setter
    def reg_sar1_int_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar1_int_en_msb, self.__reg_sar1_int_en_lsb, value)

    @property
    def reg_sar1_data_inv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar1_data_inv_msb, self.__reg_sar1_data_inv_lsb)
    @reg_sar1_data_inv.setter
    def reg_sar1_data_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar1_data_inv_msb, self.__reg_sar1_data_inv_lsb, value)

    @property
    def reg_sar1_sample_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar1_sample_num_msb, self.__reg_sar1_sample_num_lsb)
    @reg_sar1_sample_num.setter
    def reg_sar1_sample_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar1_sample_num_msb, self.__reg_sar1_sample_num_lsb, value)

    @property
    def reg_sar1_clk_gated(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar1_clk_gated_msb, self.__reg_sar1_clk_gated_lsb)
    @reg_sar1_clk_gated.setter
    def reg_sar1_clk_gated(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar1_clk_gated_msb, self.__reg_sar1_clk_gated_lsb, value)

    @property
    def reg_sar1_sample_bit(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar1_sample_bit_msb, self.__reg_sar1_sample_bit_lsb)
    @reg_sar1_sample_bit.setter
    def reg_sar1_sample_bit(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar1_sample_bit_msb, self.__reg_sar1_sample_bit_lsb, value)

    @property
    def reg_sar1_sample_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar1_sample_cycle_msb, self.__reg_sar1_sample_cycle_lsb)
    @reg_sar1_sample_cycle.setter
    def reg_sar1_sample_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar1_sample_cycle_msb, self.__reg_sar1_sample_cycle_lsb, value)

    @property
    def reg_sar1_clk_div(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar1_clk_div_msb, self.__reg_sar1_clk_div_lsb)
    @reg_sar1_clk_div.setter
    def reg_sar1_clk_div(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar1_clk_div_msb, self.__reg_sar1_clk_div_lsb, value)
class SAR_READER1_STATUS(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x4
        self.__sar1_reader_status_lsb = 0
        self.__sar1_reader_status_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sar1_reader_status(self):
        return self.__MEM.rdm(self.__addr, self.__sar1_reader_status_msb, self.__sar1_reader_status_lsb)
    @sar1_reader_status.setter
    def sar1_reader_status(self, value):
        return self.__MEM.wrm(self.__addr, self.__sar1_reader_status_msb, self.__sar1_reader_status_lsb, value)
class SAR_MEAS1_CTRL1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x8
        self.__reg_amp_short_ref_gnd_force_lsb = 30
        self.__reg_amp_short_ref_gnd_force_msb = 31
        self.__reg_amp_short_ref_force_lsb = 28
        self.__reg_amp_short_ref_force_msb = 29
        self.__reg_amp_rst_fb_force_lsb = 26
        self.__reg_amp_rst_fb_force_msb = 27
        self.__reg_force_xpd_amp_lsb = 24
        self.__reg_force_xpd_amp_msb = 25
        self.__reg_sar1_stop_lsb = 2
        self.__reg_sar1_stop_msb = 2
        self.__reg_sar1_bit_width_lsb = 0
        self.__reg_sar1_bit_width_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_amp_short_ref_gnd_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_amp_short_ref_gnd_force_msb, self.__reg_amp_short_ref_gnd_force_lsb)
    @reg_amp_short_ref_gnd_force.setter
    def reg_amp_short_ref_gnd_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_amp_short_ref_gnd_force_msb, self.__reg_amp_short_ref_gnd_force_lsb, value)

    @property
    def reg_amp_short_ref_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_amp_short_ref_force_msb, self.__reg_amp_short_ref_force_lsb)
    @reg_amp_short_ref_force.setter
    def reg_amp_short_ref_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_amp_short_ref_force_msb, self.__reg_amp_short_ref_force_lsb, value)

    @property
    def reg_amp_rst_fb_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_amp_rst_fb_force_msb, self.__reg_amp_rst_fb_force_lsb)
    @reg_amp_rst_fb_force.setter
    def reg_amp_rst_fb_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_amp_rst_fb_force_msb, self.__reg_amp_rst_fb_force_lsb, value)

    @property
    def reg_force_xpd_amp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_force_xpd_amp_msb, self.__reg_force_xpd_amp_lsb)
    @reg_force_xpd_amp.setter
    def reg_force_xpd_amp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_force_xpd_amp_msb, self.__reg_force_xpd_amp_lsb, value)

    @property
    def reg_sar1_stop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar1_stop_msb, self.__reg_sar1_stop_lsb)
    @reg_sar1_stop.setter
    def reg_sar1_stop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar1_stop_msb, self.__reg_sar1_stop_lsb, value)

    @property
    def reg_sar1_bit_width(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar1_bit_width_msb, self.__reg_sar1_bit_width_lsb)
    @reg_sar1_bit_width.setter
    def reg_sar1_bit_width(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar1_bit_width_msb, self.__reg_sar1_bit_width_lsb, value)
class SAR_MEAS1_CTRL2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xc
        self.__reg_sar1_en_pad_force_lsb = 31
        self.__reg_sar1_en_pad_force_msb = 31
        self.__reg_sar1_en_pad_lsb = 19
        self.__reg_sar1_en_pad_msb = 30
        self.__reg_meas1_start_force_lsb = 18
        self.__reg_meas1_start_force_msb = 18
        self.__reg_meas1_start_sar_lsb = 17
        self.__reg_meas1_start_sar_msb = 17
        self.__reg_meas1_done_sar_lsb = 16
        self.__reg_meas1_done_sar_msb = 16
        self.__reg_meas1_data_sar_lsb = 0
        self.__reg_meas1_data_sar_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sar1_en_pad_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar1_en_pad_force_msb, self.__reg_sar1_en_pad_force_lsb)
    @reg_sar1_en_pad_force.setter
    def reg_sar1_en_pad_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar1_en_pad_force_msb, self.__reg_sar1_en_pad_force_lsb, value)

    @property
    def reg_sar1_en_pad(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar1_en_pad_msb, self.__reg_sar1_en_pad_lsb)
    @reg_sar1_en_pad.setter
    def reg_sar1_en_pad(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar1_en_pad_msb, self.__reg_sar1_en_pad_lsb, value)

    @property
    def reg_meas1_start_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_meas1_start_force_msb, self.__reg_meas1_start_force_lsb)
    @reg_meas1_start_force.setter
    def reg_meas1_start_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_meas1_start_force_msb, self.__reg_meas1_start_force_lsb, value)

    @property
    def reg_meas1_start_sar(self):
        return self.__MEM.rdm(self.__addr, self.__reg_meas1_start_sar_msb, self.__reg_meas1_start_sar_lsb)
    @reg_meas1_start_sar.setter
    def reg_meas1_start_sar(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_meas1_start_sar_msb, self.__reg_meas1_start_sar_lsb, value)

    @property
    def reg_meas1_done_sar(self):
        return self.__MEM.rdm(self.__addr, self.__reg_meas1_done_sar_msb, self.__reg_meas1_done_sar_lsb)
    @reg_meas1_done_sar.setter
    def reg_meas1_done_sar(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_meas1_done_sar_msb, self.__reg_meas1_done_sar_lsb, value)

    @property
    def reg_meas1_data_sar(self):
        return self.__MEM.rdm(self.__addr, self.__reg_meas1_data_sar_msb, self.__reg_meas1_data_sar_lsb)
    @reg_meas1_data_sar.setter
    def reg_meas1_data_sar(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_meas1_data_sar_msb, self.__reg_meas1_data_sar_lsb, value)
class SAR_MEAS1_MUX(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x10
        self.__reg_sar1_dig_force_lsb = 31
        self.__reg_sar1_dig_force_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sar1_dig_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar1_dig_force_msb, self.__reg_sar1_dig_force_lsb)
    @reg_sar1_dig_force.setter
    def reg_sar1_dig_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar1_dig_force_msb, self.__reg_sar1_dig_force_lsb, value)
class SAR_ATTEN1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x14
        self.__reg_sar1_atten_lsb = 0
        self.__reg_sar1_atten_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sar1_atten(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar1_atten_msb, self.__reg_sar1_atten_lsb)
    @reg_sar1_atten.setter
    def reg_sar1_atten(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar1_atten_msb, self.__reg_sar1_atten_lsb, value)
class SAR_AMP_CTRL1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x18
        self.__reg_sar_amp_wait2_lsb = 16
        self.__reg_sar_amp_wait2_msb = 31
        self.__reg_sar_amp_wait1_lsb = 0
        self.__reg_sar_amp_wait1_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sar_amp_wait2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar_amp_wait2_msb, self.__reg_sar_amp_wait2_lsb)
    @reg_sar_amp_wait2.setter
    def reg_sar_amp_wait2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar_amp_wait2_msb, self.__reg_sar_amp_wait2_lsb, value)

    @property
    def reg_sar_amp_wait1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar_amp_wait1_msb, self.__reg_sar_amp_wait1_lsb)
    @reg_sar_amp_wait1.setter
    def reg_sar_amp_wait1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar_amp_wait1_msb, self.__reg_sar_amp_wait1_lsb, value)
class SAR_AMP_CTRL2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x1c
        self.__reg_sar_amp_wait3_lsb = 16
        self.__reg_sar_amp_wait3_msb = 31
        self.__reg_sar_rstb_fsm_idle_lsb = 6
        self.__reg_sar_rstb_fsm_idle_msb = 6
        self.__reg_xpd_sar_fsm_idle_lsb = 5
        self.__reg_xpd_sar_fsm_idle_msb = 5
        self.__reg_amp_short_ref_gnd_fsm_idle_lsb = 4
        self.__reg_amp_short_ref_gnd_fsm_idle_msb = 4
        self.__reg_amp_short_ref_fsm_idle_lsb = 3
        self.__reg_amp_short_ref_fsm_idle_msb = 3
        self.__reg_amp_rst_fb_fsm_idle_lsb = 2
        self.__reg_amp_rst_fb_fsm_idle_msb = 2
        self.__reg_xpd_sar_amp_fsm_idle_lsb = 1
        self.__reg_xpd_sar_amp_fsm_idle_msb = 1
        self.__reg_sar1_dac_xpd_fsm_idle_lsb = 0
        self.__reg_sar1_dac_xpd_fsm_idle_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sar_amp_wait3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar_amp_wait3_msb, self.__reg_sar_amp_wait3_lsb)
    @reg_sar_amp_wait3.setter
    def reg_sar_amp_wait3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar_amp_wait3_msb, self.__reg_sar_amp_wait3_lsb, value)

    @property
    def reg_sar_rstb_fsm_idle(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar_rstb_fsm_idle_msb, self.__reg_sar_rstb_fsm_idle_lsb)
    @reg_sar_rstb_fsm_idle.setter
    def reg_sar_rstb_fsm_idle(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar_rstb_fsm_idle_msb, self.__reg_sar_rstb_fsm_idle_lsb, value)

    @property
    def reg_xpd_sar_fsm_idle(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xpd_sar_fsm_idle_msb, self.__reg_xpd_sar_fsm_idle_lsb)
    @reg_xpd_sar_fsm_idle.setter
    def reg_xpd_sar_fsm_idle(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xpd_sar_fsm_idle_msb, self.__reg_xpd_sar_fsm_idle_lsb, value)

    @property
    def reg_amp_short_ref_gnd_fsm_idle(self):
        return self.__MEM.rdm(self.__addr, self.__reg_amp_short_ref_gnd_fsm_idle_msb, self.__reg_amp_short_ref_gnd_fsm_idle_lsb)
    @reg_amp_short_ref_gnd_fsm_idle.setter
    def reg_amp_short_ref_gnd_fsm_idle(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_amp_short_ref_gnd_fsm_idle_msb, self.__reg_amp_short_ref_gnd_fsm_idle_lsb, value)

    @property
    def reg_amp_short_ref_fsm_idle(self):
        return self.__MEM.rdm(self.__addr, self.__reg_amp_short_ref_fsm_idle_msb, self.__reg_amp_short_ref_fsm_idle_lsb)
    @reg_amp_short_ref_fsm_idle.setter
    def reg_amp_short_ref_fsm_idle(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_amp_short_ref_fsm_idle_msb, self.__reg_amp_short_ref_fsm_idle_lsb, value)

    @property
    def reg_amp_rst_fb_fsm_idle(self):
        return self.__MEM.rdm(self.__addr, self.__reg_amp_rst_fb_fsm_idle_msb, self.__reg_amp_rst_fb_fsm_idle_lsb)
    @reg_amp_rst_fb_fsm_idle.setter
    def reg_amp_rst_fb_fsm_idle(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_amp_rst_fb_fsm_idle_msb, self.__reg_amp_rst_fb_fsm_idle_lsb, value)

    @property
    def reg_xpd_sar_amp_fsm_idle(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xpd_sar_amp_fsm_idle_msb, self.__reg_xpd_sar_amp_fsm_idle_lsb)
    @reg_xpd_sar_amp_fsm_idle.setter
    def reg_xpd_sar_amp_fsm_idle(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xpd_sar_amp_fsm_idle_msb, self.__reg_xpd_sar_amp_fsm_idle_lsb, value)

    @property
    def reg_sar1_dac_xpd_fsm_idle(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar1_dac_xpd_fsm_idle_msb, self.__reg_sar1_dac_xpd_fsm_idle_lsb)
    @reg_sar1_dac_xpd_fsm_idle.setter
    def reg_sar1_dac_xpd_fsm_idle(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar1_dac_xpd_fsm_idle_msb, self.__reg_sar1_dac_xpd_fsm_idle_lsb, value)
class SAR_AMP_CTRL3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x20
        self.__reg_sar_rstb_fsm_lsb = 24
        self.__reg_sar_rstb_fsm_msb = 27
        self.__reg_xpd_sar_fsm_lsb = 20
        self.__reg_xpd_sar_fsm_msb = 23
        self.__reg_amp_short_ref_gnd_fsm_lsb = 16
        self.__reg_amp_short_ref_gnd_fsm_msb = 19
        self.__reg_amp_short_ref_fsm_lsb = 12
        self.__reg_amp_short_ref_fsm_msb = 15
        self.__reg_amp_rst_fb_fsm_lsb = 8
        self.__reg_amp_rst_fb_fsm_msb = 11
        self.__reg_xpd_sar_amp_fsm_lsb = 4
        self.__reg_xpd_sar_amp_fsm_msb = 7
        self.__reg_sar1_dac_xpd_fsm_lsb = 0
        self.__reg_sar1_dac_xpd_fsm_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sar_rstb_fsm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar_rstb_fsm_msb, self.__reg_sar_rstb_fsm_lsb)
    @reg_sar_rstb_fsm.setter
    def reg_sar_rstb_fsm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar_rstb_fsm_msb, self.__reg_sar_rstb_fsm_lsb, value)

    @property
    def reg_xpd_sar_fsm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xpd_sar_fsm_msb, self.__reg_xpd_sar_fsm_lsb)
    @reg_xpd_sar_fsm.setter
    def reg_xpd_sar_fsm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xpd_sar_fsm_msb, self.__reg_xpd_sar_fsm_lsb, value)

    @property
    def reg_amp_short_ref_gnd_fsm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_amp_short_ref_gnd_fsm_msb, self.__reg_amp_short_ref_gnd_fsm_lsb)
    @reg_amp_short_ref_gnd_fsm.setter
    def reg_amp_short_ref_gnd_fsm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_amp_short_ref_gnd_fsm_msb, self.__reg_amp_short_ref_gnd_fsm_lsb, value)

    @property
    def reg_amp_short_ref_fsm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_amp_short_ref_fsm_msb, self.__reg_amp_short_ref_fsm_lsb)
    @reg_amp_short_ref_fsm.setter
    def reg_amp_short_ref_fsm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_amp_short_ref_fsm_msb, self.__reg_amp_short_ref_fsm_lsb, value)

    @property
    def reg_amp_rst_fb_fsm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_amp_rst_fb_fsm_msb, self.__reg_amp_rst_fb_fsm_lsb)
    @reg_amp_rst_fb_fsm.setter
    def reg_amp_rst_fb_fsm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_amp_rst_fb_fsm_msb, self.__reg_amp_rst_fb_fsm_lsb, value)

    @property
    def reg_xpd_sar_amp_fsm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xpd_sar_amp_fsm_msb, self.__reg_xpd_sar_amp_fsm_lsb)
    @reg_xpd_sar_amp_fsm.setter
    def reg_xpd_sar_amp_fsm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xpd_sar_amp_fsm_msb, self.__reg_xpd_sar_amp_fsm_lsb, value)

    @property
    def reg_sar1_dac_xpd_fsm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar1_dac_xpd_fsm_msb, self.__reg_sar1_dac_xpd_fsm_lsb)
    @reg_sar1_dac_xpd_fsm.setter
    def reg_sar1_dac_xpd_fsm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar1_dac_xpd_fsm_msb, self.__reg_sar1_dac_xpd_fsm_lsb, value)
class SAR_READER2_CTRL(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x24
        self.__reg_sar2_int_en_lsb = 30
        self.__reg_sar2_int_en_msb = 30
        self.__reg_sar2_data_inv_lsb = 29
        self.__reg_sar2_data_inv_msb = 29
        self.__reg_sar2_sample_num_lsb = 19
        self.__reg_sar2_sample_num_msb = 26
        self.__reg_sar2_clk_gated_lsb = 18
        self.__reg_sar2_clk_gated_msb = 18
        self.__reg_sar2_sample_bit_lsb = 16
        self.__reg_sar2_sample_bit_msb = 17
        self.__reg_sar2_sample_cycle_lsb = 8
        self.__reg_sar2_sample_cycle_msb = 15
        self.__reg_sar2_clk_div_lsb = 0
        self.__reg_sar2_clk_div_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sar2_int_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_int_en_msb, self.__reg_sar2_int_en_lsb)
    @reg_sar2_int_en.setter
    def reg_sar2_int_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_int_en_msb, self.__reg_sar2_int_en_lsb, value)

    @property
    def reg_sar2_data_inv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_data_inv_msb, self.__reg_sar2_data_inv_lsb)
    @reg_sar2_data_inv.setter
    def reg_sar2_data_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_data_inv_msb, self.__reg_sar2_data_inv_lsb, value)

    @property
    def reg_sar2_sample_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_sample_num_msb, self.__reg_sar2_sample_num_lsb)
    @reg_sar2_sample_num.setter
    def reg_sar2_sample_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_sample_num_msb, self.__reg_sar2_sample_num_lsb, value)

    @property
    def reg_sar2_clk_gated(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_clk_gated_msb, self.__reg_sar2_clk_gated_lsb)
    @reg_sar2_clk_gated.setter
    def reg_sar2_clk_gated(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_clk_gated_msb, self.__reg_sar2_clk_gated_lsb, value)

    @property
    def reg_sar2_sample_bit(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_sample_bit_msb, self.__reg_sar2_sample_bit_lsb)
    @reg_sar2_sample_bit.setter
    def reg_sar2_sample_bit(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_sample_bit_msb, self.__reg_sar2_sample_bit_lsb, value)

    @property
    def reg_sar2_sample_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_sample_cycle_msb, self.__reg_sar2_sample_cycle_lsb)
    @reg_sar2_sample_cycle.setter
    def reg_sar2_sample_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_sample_cycle_msb, self.__reg_sar2_sample_cycle_lsb, value)

    @property
    def reg_sar2_clk_div(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_clk_div_msb, self.__reg_sar2_clk_div_lsb)
    @reg_sar2_clk_div.setter
    def reg_sar2_clk_div(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_clk_div_msb, self.__reg_sar2_clk_div_lsb, value)
class SAR_READER2_STATUS(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x28
        self.__sar2_reader_status_lsb = 0
        self.__sar2_reader_status_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sar2_reader_status(self):
        return self.__MEM.rdm(self.__addr, self.__sar2_reader_status_msb, self.__sar2_reader_status_lsb)
    @sar2_reader_status.setter
    def sar2_reader_status(self, value):
        return self.__MEM.wrm(self.__addr, self.__sar2_reader_status_msb, self.__sar2_reader_status_lsb, value)
class SAR_MEAS2_CTRL1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x2c
        self.__reg_sar2_xpd_wait_lsb = 24
        self.__reg_sar2_xpd_wait_msb = 31
        self.__reg_sar2_rstb_wait_lsb = 16
        self.__reg_sar2_rstb_wait_msb = 23
        self.__reg_sar2_standby_wait_lsb = 8
        self.__reg_sar2_standby_wait_msb = 15
        self.__reg_sar2_rstb_force_lsb = 6
        self.__reg_sar2_rstb_force_msb = 7
        self.__reg_sar2_en_test_lsb = 5
        self.__reg_sar2_en_test_msb = 5
        self.__reg_sar2_pkdet_cal_en_lsb = 4
        self.__reg_sar2_pkdet_cal_en_msb = 4
        self.__reg_sar2_pwdet_cal_en_lsb = 3
        self.__reg_sar2_pwdet_cal_en_msb = 3
        self.__reg_sar2_stop_lsb = 2
        self.__reg_sar2_stop_msb = 2
        self.__reg_sar2_bit_width_lsb = 0
        self.__reg_sar2_bit_width_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sar2_xpd_wait(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_xpd_wait_msb, self.__reg_sar2_xpd_wait_lsb)
    @reg_sar2_xpd_wait.setter
    def reg_sar2_xpd_wait(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_xpd_wait_msb, self.__reg_sar2_xpd_wait_lsb, value)

    @property
    def reg_sar2_rstb_wait(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_rstb_wait_msb, self.__reg_sar2_rstb_wait_lsb)
    @reg_sar2_rstb_wait.setter
    def reg_sar2_rstb_wait(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_rstb_wait_msb, self.__reg_sar2_rstb_wait_lsb, value)

    @property
    def reg_sar2_standby_wait(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_standby_wait_msb, self.__reg_sar2_standby_wait_lsb)
    @reg_sar2_standby_wait.setter
    def reg_sar2_standby_wait(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_standby_wait_msb, self.__reg_sar2_standby_wait_lsb, value)

    @property
    def reg_sar2_rstb_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_rstb_force_msb, self.__reg_sar2_rstb_force_lsb)
    @reg_sar2_rstb_force.setter
    def reg_sar2_rstb_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_rstb_force_msb, self.__reg_sar2_rstb_force_lsb, value)

    @property
    def reg_sar2_en_test(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_en_test_msb, self.__reg_sar2_en_test_lsb)
    @reg_sar2_en_test.setter
    def reg_sar2_en_test(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_en_test_msb, self.__reg_sar2_en_test_lsb, value)

    @property
    def reg_sar2_pkdet_cal_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_pkdet_cal_en_msb, self.__reg_sar2_pkdet_cal_en_lsb)
    @reg_sar2_pkdet_cal_en.setter
    def reg_sar2_pkdet_cal_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_pkdet_cal_en_msb, self.__reg_sar2_pkdet_cal_en_lsb, value)

    @property
    def reg_sar2_pwdet_cal_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_pwdet_cal_en_msb, self.__reg_sar2_pwdet_cal_en_lsb)
    @reg_sar2_pwdet_cal_en.setter
    def reg_sar2_pwdet_cal_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_pwdet_cal_en_msb, self.__reg_sar2_pwdet_cal_en_lsb, value)

    @property
    def reg_sar2_stop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_stop_msb, self.__reg_sar2_stop_lsb)
    @reg_sar2_stop.setter
    def reg_sar2_stop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_stop_msb, self.__reg_sar2_stop_lsb, value)

    @property
    def reg_sar2_bit_width(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_bit_width_msb, self.__reg_sar2_bit_width_lsb)
    @reg_sar2_bit_width.setter
    def reg_sar2_bit_width(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_bit_width_msb, self.__reg_sar2_bit_width_lsb, value)
class SAR_MEAS2_CTRL2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x30
        self.__reg_sar2_en_pad_force_lsb = 31
        self.__reg_sar2_en_pad_force_msb = 31
        self.__reg_sar2_en_pad_lsb = 19
        self.__reg_sar2_en_pad_msb = 30
        self.__reg_meas2_start_force_lsb = 18
        self.__reg_meas2_start_force_msb = 18
        self.__reg_meas2_start_sar_lsb = 17
        self.__reg_meas2_start_sar_msb = 17
        self.__reg_meas2_done_sar_lsb = 16
        self.__reg_meas2_done_sar_msb = 16
        self.__reg_meas2_data_sar_lsb = 0
        self.__reg_meas2_data_sar_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sar2_en_pad_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_en_pad_force_msb, self.__reg_sar2_en_pad_force_lsb)
    @reg_sar2_en_pad_force.setter
    def reg_sar2_en_pad_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_en_pad_force_msb, self.__reg_sar2_en_pad_force_lsb, value)

    @property
    def reg_sar2_en_pad(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_en_pad_msb, self.__reg_sar2_en_pad_lsb)
    @reg_sar2_en_pad.setter
    def reg_sar2_en_pad(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_en_pad_msb, self.__reg_sar2_en_pad_lsb, value)

    @property
    def reg_meas2_start_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_meas2_start_force_msb, self.__reg_meas2_start_force_lsb)
    @reg_meas2_start_force.setter
    def reg_meas2_start_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_meas2_start_force_msb, self.__reg_meas2_start_force_lsb, value)

    @property
    def reg_meas2_start_sar(self):
        return self.__MEM.rdm(self.__addr, self.__reg_meas2_start_sar_msb, self.__reg_meas2_start_sar_lsb)
    @reg_meas2_start_sar.setter
    def reg_meas2_start_sar(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_meas2_start_sar_msb, self.__reg_meas2_start_sar_lsb, value)

    @property
    def reg_meas2_done_sar(self):
        return self.__MEM.rdm(self.__addr, self.__reg_meas2_done_sar_msb, self.__reg_meas2_done_sar_lsb)
    @reg_meas2_done_sar.setter
    def reg_meas2_done_sar(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_meas2_done_sar_msb, self.__reg_meas2_done_sar_lsb, value)

    @property
    def reg_meas2_data_sar(self):
        return self.__MEM.rdm(self.__addr, self.__reg_meas2_data_sar_msb, self.__reg_meas2_data_sar_lsb)
    @reg_meas2_data_sar.setter
    def reg_meas2_data_sar(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_meas2_data_sar_msb, self.__reg_meas2_data_sar_lsb, value)
class SAR_MEAS2_MUX(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x34
        self.__reg_sar2_rtc_force_lsb = 31
        self.__reg_sar2_rtc_force_msb = 31
        self.__reg_sar2_pwdet_cct_lsb = 28
        self.__reg_sar2_pwdet_cct_msb = 30
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sar2_rtc_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_rtc_force_msb, self.__reg_sar2_rtc_force_lsb)
    @reg_sar2_rtc_force.setter
    def reg_sar2_rtc_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_rtc_force_msb, self.__reg_sar2_rtc_force_lsb, value)

    @property
    def reg_sar2_pwdet_cct(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_pwdet_cct_msb, self.__reg_sar2_pwdet_cct_lsb)
    @reg_sar2_pwdet_cct.setter
    def reg_sar2_pwdet_cct(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_pwdet_cct_msb, self.__reg_sar2_pwdet_cct_lsb, value)
class SAR_ATTEN2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x38
        self.__reg_sar2_atten_lsb = 0
        self.__reg_sar2_atten_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sar2_atten(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_atten_msb, self.__reg_sar2_atten_lsb)
    @reg_sar2_atten.setter
    def reg_sar2_atten(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_atten_msb, self.__reg_sar2_atten_lsb, value)
class SAR_POWER_XPD_SAR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x3c
        self.__reg_sarclk_en_lsb = 31
        self.__reg_sarclk_en_msb = 31
        self.__reg_force_xpd_sar_lsb = 29
        self.__reg_force_xpd_sar_msb = 30
        self.__reg_sar1_dref_lsb = 26
        self.__reg_sar1_dref_msb = 28
        self.__reg_sar2_dref_lsb = 23
        self.__reg_sar2_dref_msb = 25
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sarclk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sarclk_en_msb, self.__reg_sarclk_en_lsb)
    @reg_sarclk_en.setter
    def reg_sarclk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sarclk_en_msb, self.__reg_sarclk_en_lsb, value)

    @property
    def reg_force_xpd_sar(self):
        return self.__MEM.rdm(self.__addr, self.__reg_force_xpd_sar_msb, self.__reg_force_xpd_sar_lsb)
    @reg_force_xpd_sar.setter
    def reg_force_xpd_sar(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_force_xpd_sar_msb, self.__reg_force_xpd_sar_lsb, value)

    @property
    def reg_sar1_dref(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar1_dref_msb, self.__reg_sar1_dref_lsb)
    @reg_sar1_dref.setter
    def reg_sar1_dref(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar1_dref_msb, self.__reg_sar1_dref_lsb, value)

    @property
    def reg_sar2_dref(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_dref_msb, self.__reg_sar2_dref_lsb)
    @reg_sar2_dref.setter
    def reg_sar2_dref(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_dref_msb, self.__reg_sar2_dref_lsb, value)
class SAR_SLAVE_ADDR1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x40
        self.__saradc_meas_status_lsb = 22
        self.__saradc_meas_status_msb = 29
        self.__reg_i2c_slave_addr0_lsb = 11
        self.__reg_i2c_slave_addr0_msb = 21
        self.__reg_i2c_slave_addr1_lsb = 0
        self.__reg_i2c_slave_addr1_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def saradc_meas_status(self):
        return self.__MEM.rdm(self.__addr, self.__saradc_meas_status_msb, self.__saradc_meas_status_lsb)
    @saradc_meas_status.setter
    def saradc_meas_status(self, value):
        return self.__MEM.wrm(self.__addr, self.__saradc_meas_status_msb, self.__saradc_meas_status_lsb, value)

    @property
    def reg_i2c_slave_addr0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2c_slave_addr0_msb, self.__reg_i2c_slave_addr0_lsb)
    @reg_i2c_slave_addr0.setter
    def reg_i2c_slave_addr0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2c_slave_addr0_msb, self.__reg_i2c_slave_addr0_lsb, value)

    @property
    def reg_i2c_slave_addr1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2c_slave_addr1_msb, self.__reg_i2c_slave_addr1_lsb)
    @reg_i2c_slave_addr1.setter
    def reg_i2c_slave_addr1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2c_slave_addr1_msb, self.__reg_i2c_slave_addr1_lsb, value)
class SAR_SLAVE_ADDR2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x44
        self.__reg_i2c_slave_addr2_lsb = 11
        self.__reg_i2c_slave_addr2_msb = 21
        self.__reg_i2c_slave_addr3_lsb = 0
        self.__reg_i2c_slave_addr3_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_i2c_slave_addr2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2c_slave_addr2_msb, self.__reg_i2c_slave_addr2_lsb)
    @reg_i2c_slave_addr2.setter
    def reg_i2c_slave_addr2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2c_slave_addr2_msb, self.__reg_i2c_slave_addr2_lsb, value)

    @property
    def reg_i2c_slave_addr3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2c_slave_addr3_msb, self.__reg_i2c_slave_addr3_lsb)
    @reg_i2c_slave_addr3.setter
    def reg_i2c_slave_addr3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2c_slave_addr3_msb, self.__reg_i2c_slave_addr3_lsb, value)
class SAR_SLAVE_ADDR3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x48
        self.__reg_i2c_slave_addr4_lsb = 11
        self.__reg_i2c_slave_addr4_msb = 21
        self.__reg_i2c_slave_addr5_lsb = 0
        self.__reg_i2c_slave_addr5_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_i2c_slave_addr4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2c_slave_addr4_msb, self.__reg_i2c_slave_addr4_lsb)
    @reg_i2c_slave_addr4.setter
    def reg_i2c_slave_addr4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2c_slave_addr4_msb, self.__reg_i2c_slave_addr4_lsb, value)

    @property
    def reg_i2c_slave_addr5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2c_slave_addr5_msb, self.__reg_i2c_slave_addr5_lsb)
    @reg_i2c_slave_addr5.setter
    def reg_i2c_slave_addr5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2c_slave_addr5_msb, self.__reg_i2c_slave_addr5_lsb, value)
class SAR_SLAVE_ADDR4(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x4c
        self.__reg_i2c_slave_addr6_lsb = 11
        self.__reg_i2c_slave_addr6_msb = 21
        self.__reg_i2c_slave_addr7_lsb = 0
        self.__reg_i2c_slave_addr7_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_i2c_slave_addr6(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2c_slave_addr6_msb, self.__reg_i2c_slave_addr6_lsb)
    @reg_i2c_slave_addr6.setter
    def reg_i2c_slave_addr6(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2c_slave_addr6_msb, self.__reg_i2c_slave_addr6_lsb, value)

    @property
    def reg_i2c_slave_addr7(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2c_slave_addr7_msb, self.__reg_i2c_slave_addr7_lsb)
    @reg_i2c_slave_addr7.setter
    def reg_i2c_slave_addr7(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2c_slave_addr7_msb, self.__reg_i2c_slave_addr7_lsb, value)
class SAR_TSENS_CTRL(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x50
        self.__reg_tsens_dac_lsb = 28
        self.__reg_tsens_dac_msb = 31
        self.__reg_tsens_div_chop_lsb = 26
        self.__reg_tsens_div_chop_msb = 27
        self.__reg_tsens_diz_lsb = 25
        self.__reg_tsens_diz_msb = 25
        self.__reg_tsens_dump_out_lsb = 24
        self.__reg_tsens_dump_out_msb = 24
        self.__reg_tsens_power_up_force_lsb = 23
        self.__reg_tsens_power_up_force_msb = 23
        self.__reg_tsens_power_up_lsb = 22
        self.__reg_tsens_power_up_msb = 22
        self.__reg_tsens_clk_div_lsb = 14
        self.__reg_tsens_clk_div_msb = 21
        self.__reg_tsens_in_inv_lsb = 13
        self.__reg_tsens_in_inv_msb = 13
        self.__reg_tsens_int_en_lsb = 12
        self.__reg_tsens_int_en_msb = 12
        self.__reg_tsens_ready_lsb = 8
        self.__reg_tsens_ready_msb = 8
        self.__reg_tsens_out_lsb = 0
        self.__reg_tsens_out_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tsens_dac(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsens_dac_msb, self.__reg_tsens_dac_lsb)
    @reg_tsens_dac.setter
    def reg_tsens_dac(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsens_dac_msb, self.__reg_tsens_dac_lsb, value)

    @property
    def reg_tsens_div_chop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsens_div_chop_msb, self.__reg_tsens_div_chop_lsb)
    @reg_tsens_div_chop.setter
    def reg_tsens_div_chop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsens_div_chop_msb, self.__reg_tsens_div_chop_lsb, value)

    @property
    def reg_tsens_diz(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsens_diz_msb, self.__reg_tsens_diz_lsb)
    @reg_tsens_diz.setter
    def reg_tsens_diz(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsens_diz_msb, self.__reg_tsens_diz_lsb, value)

    @property
    def reg_tsens_dump_out(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsens_dump_out_msb, self.__reg_tsens_dump_out_lsb)
    @reg_tsens_dump_out.setter
    def reg_tsens_dump_out(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsens_dump_out_msb, self.__reg_tsens_dump_out_lsb, value)

    @property
    def reg_tsens_power_up_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsens_power_up_force_msb, self.__reg_tsens_power_up_force_lsb)
    @reg_tsens_power_up_force.setter
    def reg_tsens_power_up_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsens_power_up_force_msb, self.__reg_tsens_power_up_force_lsb, value)

    @property
    def reg_tsens_power_up(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsens_power_up_msb, self.__reg_tsens_power_up_lsb)
    @reg_tsens_power_up.setter
    def reg_tsens_power_up(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsens_power_up_msb, self.__reg_tsens_power_up_lsb, value)

    @property
    def reg_tsens_clk_div(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsens_clk_div_msb, self.__reg_tsens_clk_div_lsb)
    @reg_tsens_clk_div.setter
    def reg_tsens_clk_div(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsens_clk_div_msb, self.__reg_tsens_clk_div_lsb, value)

    @property
    def reg_tsens_in_inv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsens_in_inv_msb, self.__reg_tsens_in_inv_lsb)
    @reg_tsens_in_inv.setter
    def reg_tsens_in_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsens_in_inv_msb, self.__reg_tsens_in_inv_lsb, value)

    @property
    def reg_tsens_int_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsens_int_en_msb, self.__reg_tsens_int_en_lsb)
    @reg_tsens_int_en.setter
    def reg_tsens_int_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsens_int_en_msb, self.__reg_tsens_int_en_lsb, value)

    @property
    def reg_tsens_ready(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsens_ready_msb, self.__reg_tsens_ready_lsb)
    @reg_tsens_ready.setter
    def reg_tsens_ready(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsens_ready_msb, self.__reg_tsens_ready_lsb, value)

    @property
    def reg_tsens_out(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsens_out_msb, self.__reg_tsens_out_lsb)
    @reg_tsens_out.setter
    def reg_tsens_out(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsens_out_msb, self.__reg_tsens_out_lsb, value)
class SAR_TSENS_CTRL2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x54
        self.__reg_tsens_reset_lsb = 16
        self.__reg_tsens_reset_msb = 16
        self.__reg_tsens_clkgate_en_lsb = 15
        self.__reg_tsens_clkgate_en_msb = 15
        self.__reg_tsens_clk_inv_lsb = 14
        self.__reg_tsens_clk_inv_msb = 14
        self.__reg_tsens_xpd_force_lsb = 12
        self.__reg_tsens_xpd_force_msb = 13
        self.__reg_tsens_xpd_wait_lsb = 0
        self.__reg_tsens_xpd_wait_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tsens_reset(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsens_reset_msb, self.__reg_tsens_reset_lsb)
    @reg_tsens_reset.setter
    def reg_tsens_reset(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsens_reset_msb, self.__reg_tsens_reset_lsb, value)

    @property
    def reg_tsens_clkgate_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsens_clkgate_en_msb, self.__reg_tsens_clkgate_en_lsb)
    @reg_tsens_clkgate_en.setter
    def reg_tsens_clkgate_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsens_clkgate_en_msb, self.__reg_tsens_clkgate_en_lsb, value)

    @property
    def reg_tsens_clk_inv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsens_clk_inv_msb, self.__reg_tsens_clk_inv_lsb)
    @reg_tsens_clk_inv.setter
    def reg_tsens_clk_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsens_clk_inv_msb, self.__reg_tsens_clk_inv_lsb, value)

    @property
    def reg_tsens_xpd_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsens_xpd_force_msb, self.__reg_tsens_xpd_force_lsb)
    @reg_tsens_xpd_force.setter
    def reg_tsens_xpd_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsens_xpd_force_msb, self.__reg_tsens_xpd_force_lsb, value)

    @property
    def reg_tsens_xpd_wait(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsens_xpd_wait_msb, self.__reg_tsens_xpd_wait_lsb)
    @reg_tsens_xpd_wait.setter
    def reg_tsens_xpd_wait(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsens_xpd_wait_msb, self.__reg_tsens_xpd_wait_lsb, value)
class SAR_I2C_CTRL(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x58
        self.__reg_sar_i2c_start_force_lsb = 29
        self.__reg_sar_i2c_start_force_msb = 29
        self.__reg_sar_i2c_start_lsb = 28
        self.__reg_sar_i2c_start_msb = 28
        self.__reg_sar_i2c_ctrl_lsb = 0
        self.__reg_sar_i2c_ctrl_msb = 27
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sar_i2c_start_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar_i2c_start_force_msb, self.__reg_sar_i2c_start_force_lsb)
    @reg_sar_i2c_start_force.setter
    def reg_sar_i2c_start_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar_i2c_start_force_msb, self.__reg_sar_i2c_start_force_lsb, value)

    @property
    def reg_sar_i2c_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar_i2c_start_msb, self.__reg_sar_i2c_start_lsb)
    @reg_sar_i2c_start.setter
    def reg_sar_i2c_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar_i2c_start_msb, self.__reg_sar_i2c_start_lsb, value)

    @property
    def reg_sar_i2c_ctrl(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar_i2c_ctrl_msb, self.__reg_sar_i2c_ctrl_lsb)
    @reg_sar_i2c_ctrl.setter
    def reg_sar_i2c_ctrl(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar_i2c_ctrl_msb, self.__reg_sar_i2c_ctrl_lsb, value)
class SAR_TOUCH_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x5c
        self.__reg_touch_approach_pad0_lsb = 28
        self.__reg_touch_approach_pad0_msb = 31
        self.__reg_touch_approach_pad1_lsb = 24
        self.__reg_touch_approach_pad1_msb = 27
        self.__reg_touch_approach_pad2_lsb = 20
        self.__reg_touch_approach_pad2_msb = 23
        self.__reg_touch_status_clr_lsb = 15
        self.__reg_touch_status_clr_msb = 15
        self.__reg_touch_outen_lsb = 0
        self.__reg_touch_outen_msb = 14
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_approach_pad0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_approach_pad0_msb, self.__reg_touch_approach_pad0_lsb)
    @reg_touch_approach_pad0.setter
    def reg_touch_approach_pad0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_approach_pad0_msb, self.__reg_touch_approach_pad0_lsb, value)

    @property
    def reg_touch_approach_pad1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_approach_pad1_msb, self.__reg_touch_approach_pad1_lsb)
    @reg_touch_approach_pad1.setter
    def reg_touch_approach_pad1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_approach_pad1_msb, self.__reg_touch_approach_pad1_lsb, value)

    @property
    def reg_touch_approach_pad2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_approach_pad2_msb, self.__reg_touch_approach_pad2_lsb)
    @reg_touch_approach_pad2.setter
    def reg_touch_approach_pad2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_approach_pad2_msb, self.__reg_touch_approach_pad2_lsb, value)

    @property
    def reg_touch_status_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_status_clr_msb, self.__reg_touch_status_clr_lsb)
    @reg_touch_status_clr.setter
    def reg_touch_status_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_status_clr_msb, self.__reg_touch_status_clr_lsb, value)

    @property
    def reg_touch_outen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_outen_msb, self.__reg_touch_outen_lsb)
    @reg_touch_outen.setter
    def reg_touch_outen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_outen_msb, self.__reg_touch_outen_lsb, value)
class SAR_TOUCH_THRES1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x60
        self.__reg_touch_out_th1_lsb = 0
        self.__reg_touch_out_th1_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_out_th1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_out_th1_msb, self.__reg_touch_out_th1_lsb)
    @reg_touch_out_th1.setter
    def reg_touch_out_th1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_out_th1_msb, self.__reg_touch_out_th1_lsb, value)
class SAR_TOUCH_THRES2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x64
        self.__reg_touch_out_th2_lsb = 0
        self.__reg_touch_out_th2_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_out_th2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_out_th2_msb, self.__reg_touch_out_th2_lsb)
    @reg_touch_out_th2.setter
    def reg_touch_out_th2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_out_th2_msb, self.__reg_touch_out_th2_lsb, value)
class SAR_TOUCH_THRES3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x68
        self.__reg_touch_out_th3_lsb = 0
        self.__reg_touch_out_th3_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_out_th3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_out_th3_msb, self.__reg_touch_out_th3_lsb)
    @reg_touch_out_th3.setter
    def reg_touch_out_th3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_out_th3_msb, self.__reg_touch_out_th3_lsb, value)
class SAR_TOUCH_THRES4(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x6c
        self.__reg_touch_out_th4_lsb = 0
        self.__reg_touch_out_th4_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_out_th4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_out_th4_msb, self.__reg_touch_out_th4_lsb)
    @reg_touch_out_th4.setter
    def reg_touch_out_th4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_out_th4_msb, self.__reg_touch_out_th4_lsb, value)
class SAR_TOUCH_THRES5(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x70
        self.__reg_touch_out_th5_lsb = 0
        self.__reg_touch_out_th5_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_out_th5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_out_th5_msb, self.__reg_touch_out_th5_lsb)
    @reg_touch_out_th5.setter
    def reg_touch_out_th5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_out_th5_msb, self.__reg_touch_out_th5_lsb, value)
class SAR_TOUCH_THRES6(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x74
        self.__reg_touch_out_th6_lsb = 0
        self.__reg_touch_out_th6_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_out_th6(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_out_th6_msb, self.__reg_touch_out_th6_lsb)
    @reg_touch_out_th6.setter
    def reg_touch_out_th6(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_out_th6_msb, self.__reg_touch_out_th6_lsb, value)
class SAR_TOUCH_THRES7(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x78
        self.__reg_touch_out_th7_lsb = 0
        self.__reg_touch_out_th7_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_out_th7(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_out_th7_msb, self.__reg_touch_out_th7_lsb)
    @reg_touch_out_th7.setter
    def reg_touch_out_th7(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_out_th7_msb, self.__reg_touch_out_th7_lsb, value)
class SAR_TOUCH_THRES8(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x7c
        self.__reg_touch_out_th8_lsb = 0
        self.__reg_touch_out_th8_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_out_th8(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_out_th8_msb, self.__reg_touch_out_th8_lsb)
    @reg_touch_out_th8.setter
    def reg_touch_out_th8(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_out_th8_msb, self.__reg_touch_out_th8_lsb, value)
class SAR_TOUCH_THRES9(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x80
        self.__reg_touch_out_th9_lsb = 0
        self.__reg_touch_out_th9_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_out_th9(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_out_th9_msb, self.__reg_touch_out_th9_lsb)
    @reg_touch_out_th9.setter
    def reg_touch_out_th9(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_out_th9_msb, self.__reg_touch_out_th9_lsb, value)
class SAR_TOUCH_THRES10(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x84
        self.__reg_touch_out_th10_lsb = 0
        self.__reg_touch_out_th10_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_out_th10(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_out_th10_msb, self.__reg_touch_out_th10_lsb)
    @reg_touch_out_th10.setter
    def reg_touch_out_th10(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_out_th10_msb, self.__reg_touch_out_th10_lsb, value)
class SAR_TOUCH_THRES11(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x88
        self.__reg_touch_out_th11_lsb = 0
        self.__reg_touch_out_th11_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_out_th11(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_out_th11_msb, self.__reg_touch_out_th11_lsb)
    @reg_touch_out_th11.setter
    def reg_touch_out_th11(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_out_th11_msb, self.__reg_touch_out_th11_lsb, value)
class SAR_TOUCH_THRES12(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x8c
        self.__reg_touch_out_th12_lsb = 0
        self.__reg_touch_out_th12_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_out_th12(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_out_th12_msb, self.__reg_touch_out_th12_lsb)
    @reg_touch_out_th12.setter
    def reg_touch_out_th12(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_out_th12_msb, self.__reg_touch_out_th12_lsb, value)
class SAR_TOUCH_THRES13(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x90
        self.__reg_touch_out_th13_lsb = 0
        self.__reg_touch_out_th13_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_out_th13(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_out_th13_msb, self.__reg_touch_out_th13_lsb)
    @reg_touch_out_th13.setter
    def reg_touch_out_th13(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_out_th13_msb, self.__reg_touch_out_th13_lsb, value)
class SAR_TOUCH_THRES14(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x94
        self.__reg_touch_out_th14_lsb = 0
        self.__reg_touch_out_th14_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_out_th14(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_out_th14_msb, self.__reg_touch_out_th14_lsb)
    @reg_touch_out_th14.setter
    def reg_touch_out_th14(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_out_th14_msb, self.__reg_touch_out_th14_lsb, value)
class SAR_TOUCH_OUT0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x98
        self.__reg_touch_meas_out0_lsb = 0
        self.__reg_touch_meas_out0_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_meas_out0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_meas_out0_msb, self.__reg_touch_meas_out0_lsb)
    @reg_touch_meas_out0.setter
    def reg_touch_meas_out0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_meas_out0_msb, self.__reg_touch_meas_out0_lsb, value)
class SAR_TOUCH_OUT1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x9c
        self.__reg_touch_meas_out1_lsb = 0
        self.__reg_touch_meas_out1_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_meas_out1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_meas_out1_msb, self.__reg_touch_meas_out1_lsb)
    @reg_touch_meas_out1.setter
    def reg_touch_meas_out1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_meas_out1_msb, self.__reg_touch_meas_out1_lsb, value)
class SAR_TOUCH_OUT2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xa0
        self.__reg_touch_meas_out2_lsb = 0
        self.__reg_touch_meas_out2_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_meas_out2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_meas_out2_msb, self.__reg_touch_meas_out2_lsb)
    @reg_touch_meas_out2.setter
    def reg_touch_meas_out2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_meas_out2_msb, self.__reg_touch_meas_out2_lsb, value)
class SAR_TOUCH_OUT3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xa4
        self.__reg_touch_meas_out3_lsb = 0
        self.__reg_touch_meas_out3_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_meas_out3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_meas_out3_msb, self.__reg_touch_meas_out3_lsb)
    @reg_touch_meas_out3.setter
    def reg_touch_meas_out3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_meas_out3_msb, self.__reg_touch_meas_out3_lsb, value)
class SAR_TOUCH_OUT4(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xa8
        self.__reg_touch_meas_out4_lsb = 0
        self.__reg_touch_meas_out4_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_meas_out4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_meas_out4_msb, self.__reg_touch_meas_out4_lsb)
    @reg_touch_meas_out4.setter
    def reg_touch_meas_out4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_meas_out4_msb, self.__reg_touch_meas_out4_lsb, value)
class SAR_TOUCH_OUT5(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xac
        self.__reg_touch_meas_out5_lsb = 0
        self.__reg_touch_meas_out5_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_meas_out5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_meas_out5_msb, self.__reg_touch_meas_out5_lsb)
    @reg_touch_meas_out5.setter
    def reg_touch_meas_out5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_meas_out5_msb, self.__reg_touch_meas_out5_lsb, value)
class SAR_TOUCH_OUT6(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xb0
        self.__reg_touch_meas_out6_lsb = 0
        self.__reg_touch_meas_out6_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_meas_out6(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_meas_out6_msb, self.__reg_touch_meas_out6_lsb)
    @reg_touch_meas_out6.setter
    def reg_touch_meas_out6(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_meas_out6_msb, self.__reg_touch_meas_out6_lsb, value)
class SAR_TOUCH_OUT7(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xb4
        self.__reg_touch_meas_out7_lsb = 0
        self.__reg_touch_meas_out7_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_meas_out7(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_meas_out7_msb, self.__reg_touch_meas_out7_lsb)
    @reg_touch_meas_out7.setter
    def reg_touch_meas_out7(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_meas_out7_msb, self.__reg_touch_meas_out7_lsb, value)
class SAR_TOUCH_OUT8(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xb8
        self.__reg_touch_meas_out8_lsb = 0
        self.__reg_touch_meas_out8_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_meas_out8(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_meas_out8_msb, self.__reg_touch_meas_out8_lsb)
    @reg_touch_meas_out8.setter
    def reg_touch_meas_out8(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_meas_out8_msb, self.__reg_touch_meas_out8_lsb, value)
class SAR_TOUCH_OUT9(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xbc
        self.__reg_touch_meas_out9_lsb = 0
        self.__reg_touch_meas_out9_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_meas_out9(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_meas_out9_msb, self.__reg_touch_meas_out9_lsb)
    @reg_touch_meas_out9.setter
    def reg_touch_meas_out9(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_meas_out9_msb, self.__reg_touch_meas_out9_lsb, value)
class SAR_TOUCH_OUT10(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xc0
        self.__reg_touch_meas_out10_lsb = 0
        self.__reg_touch_meas_out10_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_meas_out10(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_meas_out10_msb, self.__reg_touch_meas_out10_lsb)
    @reg_touch_meas_out10.setter
    def reg_touch_meas_out10(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_meas_out10_msb, self.__reg_touch_meas_out10_lsb, value)
class SAR_TOUCH_OUT11(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xc4
        self.__reg_touch_meas_out11_lsb = 0
        self.__reg_touch_meas_out11_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_meas_out11(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_meas_out11_msb, self.__reg_touch_meas_out11_lsb)
    @reg_touch_meas_out11.setter
    def reg_touch_meas_out11(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_meas_out11_msb, self.__reg_touch_meas_out11_lsb, value)
class SAR_TOUCH_OUT12(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xc8
        self.__reg_touch_meas_out12_lsb = 0
        self.__reg_touch_meas_out12_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_meas_out12(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_meas_out12_msb, self.__reg_touch_meas_out12_lsb)
    @reg_touch_meas_out12.setter
    def reg_touch_meas_out12(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_meas_out12_msb, self.__reg_touch_meas_out12_lsb, value)
class SAR_TOUCH_OUT13(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xcc
        self.__reg_touch_meas_out13_lsb = 0
        self.__reg_touch_meas_out13_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_meas_out13(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_meas_out13_msb, self.__reg_touch_meas_out13_lsb)
    @reg_touch_meas_out13.setter
    def reg_touch_meas_out13(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_meas_out13_msb, self.__reg_touch_meas_out13_lsb, value)
class SAR_TOUCH_OUT14(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xd0
        self.__reg_touch_meas_out14_lsb = 0
        self.__reg_touch_meas_out14_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_meas_out14(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_meas_out14_msb, self.__reg_touch_meas_out14_lsb)
    @reg_touch_meas_out14.setter
    def reg_touch_meas_out14(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_meas_out14_msb, self.__reg_touch_meas_out14_lsb, value)
class SAR_TOUCH_CHN_ST(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xd4
        self.__touch_meas_done_lsb = 31
        self.__touch_meas_done_msb = 31
        self.__reg_touch_channel_clr_lsb = 15
        self.__reg_touch_channel_clr_msb = 29
        self.__touch_pad_active_lsb = 0
        self.__touch_pad_active_msb = 14
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def touch_meas_done(self):
        return self.__MEM.rdm(self.__addr, self.__touch_meas_done_msb, self.__touch_meas_done_lsb)
    @touch_meas_done.setter
    def touch_meas_done(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_meas_done_msb, self.__touch_meas_done_lsb, value)

    @property
    def reg_touch_channel_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_channel_clr_msb, self.__reg_touch_channel_clr_lsb)
    @reg_touch_channel_clr.setter
    def reg_touch_channel_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_channel_clr_msb, self.__reg_touch_channel_clr_lsb, value)

    @property
    def touch_pad_active(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad_active_msb, self.__touch_pad_active_lsb)
    @touch_pad_active.setter
    def touch_pad_active(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad_active_msb, self.__touch_pad_active_lsb, value)
class SAR_TOUCH_STATUS0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xd8
        self.__touch_scan_curr_lsb = 22
        self.__touch_scan_curr_msb = 25
        self.__touch_denoise_data_lsb = 0
        self.__touch_denoise_data_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def touch_scan_curr(self):
        return self.__MEM.rdm(self.__addr, self.__touch_scan_curr_msb, self.__touch_scan_curr_lsb)
    @touch_scan_curr.setter
    def touch_scan_curr(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_scan_curr_msb, self.__touch_scan_curr_lsb, value)

    @property
    def touch_denoise_data(self):
        return self.__MEM.rdm(self.__addr, self.__touch_denoise_data_msb, self.__touch_denoise_data_lsb)
    @touch_denoise_data.setter
    def touch_denoise_data(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_denoise_data_msb, self.__touch_denoise_data_lsb, value)
class SAR_TOUCH_STATUS1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xdc
        self.__touch_pad1_debounce_lsb = 29
        self.__touch_pad1_debounce_msb = 31
        self.__touch_pad1_baseline_lsb = 0
        self.__touch_pad1_baseline_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def touch_pad1_debounce(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad1_debounce_msb, self.__touch_pad1_debounce_lsb)
    @touch_pad1_debounce.setter
    def touch_pad1_debounce(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad1_debounce_msb, self.__touch_pad1_debounce_lsb, value)

    @property
    def touch_pad1_baseline(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad1_baseline_msb, self.__touch_pad1_baseline_lsb)
    @touch_pad1_baseline.setter
    def touch_pad1_baseline(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad1_baseline_msb, self.__touch_pad1_baseline_lsb, value)
class SAR_TOUCH_STATUS2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xe0
        self.__touch_pad2_debounce_lsb = 29
        self.__touch_pad2_debounce_msb = 31
        self.__touch_pad2_baseline_lsb = 0
        self.__touch_pad2_baseline_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def touch_pad2_debounce(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad2_debounce_msb, self.__touch_pad2_debounce_lsb)
    @touch_pad2_debounce.setter
    def touch_pad2_debounce(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad2_debounce_msb, self.__touch_pad2_debounce_lsb, value)

    @property
    def touch_pad2_baseline(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad2_baseline_msb, self.__touch_pad2_baseline_lsb)
    @touch_pad2_baseline.setter
    def touch_pad2_baseline(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad2_baseline_msb, self.__touch_pad2_baseline_lsb, value)
class SAR_TOUCH_STATUS3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xe4
        self.__touch_pad3_debounce_lsb = 29
        self.__touch_pad3_debounce_msb = 31
        self.__touch_pad3_baseline_lsb = 0
        self.__touch_pad3_baseline_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def touch_pad3_debounce(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad3_debounce_msb, self.__touch_pad3_debounce_lsb)
    @touch_pad3_debounce.setter
    def touch_pad3_debounce(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad3_debounce_msb, self.__touch_pad3_debounce_lsb, value)

    @property
    def touch_pad3_baseline(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad3_baseline_msb, self.__touch_pad3_baseline_lsb)
    @touch_pad3_baseline.setter
    def touch_pad3_baseline(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad3_baseline_msb, self.__touch_pad3_baseline_lsb, value)
class SAR_TOUCH_STATUS4(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xe8
        self.__touch_pad4_debounce_lsb = 29
        self.__touch_pad4_debounce_msb = 31
        self.__touch_pad4_baseline_lsb = 0
        self.__touch_pad4_baseline_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def touch_pad4_debounce(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad4_debounce_msb, self.__touch_pad4_debounce_lsb)
    @touch_pad4_debounce.setter
    def touch_pad4_debounce(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad4_debounce_msb, self.__touch_pad4_debounce_lsb, value)

    @property
    def touch_pad4_baseline(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad4_baseline_msb, self.__touch_pad4_baseline_lsb)
    @touch_pad4_baseline.setter
    def touch_pad4_baseline(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad4_baseline_msb, self.__touch_pad4_baseline_lsb, value)
class SAR_TOUCH_STATUS5(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xec
        self.__touch_pad5_debounce_lsb = 29
        self.__touch_pad5_debounce_msb = 31
        self.__touch_pad5_baseline_lsb = 0
        self.__touch_pad5_baseline_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def touch_pad5_debounce(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad5_debounce_msb, self.__touch_pad5_debounce_lsb)
    @touch_pad5_debounce.setter
    def touch_pad5_debounce(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad5_debounce_msb, self.__touch_pad5_debounce_lsb, value)

    @property
    def touch_pad5_baseline(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad5_baseline_msb, self.__touch_pad5_baseline_lsb)
    @touch_pad5_baseline.setter
    def touch_pad5_baseline(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad5_baseline_msb, self.__touch_pad5_baseline_lsb, value)
class SAR_TOUCH_STATUS6(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xf0
        self.__touch_pad6_debounce_lsb = 29
        self.__touch_pad6_debounce_msb = 31
        self.__touch_pad6_baseline_lsb = 0
        self.__touch_pad6_baseline_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def touch_pad6_debounce(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad6_debounce_msb, self.__touch_pad6_debounce_lsb)
    @touch_pad6_debounce.setter
    def touch_pad6_debounce(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad6_debounce_msb, self.__touch_pad6_debounce_lsb, value)

    @property
    def touch_pad6_baseline(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad6_baseline_msb, self.__touch_pad6_baseline_lsb)
    @touch_pad6_baseline.setter
    def touch_pad6_baseline(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad6_baseline_msb, self.__touch_pad6_baseline_lsb, value)
class SAR_TOUCH_STATUS7(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xf4
        self.__touch_pad7_debounce_lsb = 29
        self.__touch_pad7_debounce_msb = 31
        self.__touch_pad7_baseline_lsb = 0
        self.__touch_pad7_baseline_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def touch_pad7_debounce(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad7_debounce_msb, self.__touch_pad7_debounce_lsb)
    @touch_pad7_debounce.setter
    def touch_pad7_debounce(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad7_debounce_msb, self.__touch_pad7_debounce_lsb, value)

    @property
    def touch_pad7_baseline(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad7_baseline_msb, self.__touch_pad7_baseline_lsb)
    @touch_pad7_baseline.setter
    def touch_pad7_baseline(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad7_baseline_msb, self.__touch_pad7_baseline_lsb, value)
class SAR_TOUCH_STATUS8(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xf8
        self.__touch_pad8_debounce_lsb = 29
        self.__touch_pad8_debounce_msb = 31
        self.__touch_pad8_baseline_lsb = 0
        self.__touch_pad8_baseline_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def touch_pad8_debounce(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad8_debounce_msb, self.__touch_pad8_debounce_lsb)
    @touch_pad8_debounce.setter
    def touch_pad8_debounce(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad8_debounce_msb, self.__touch_pad8_debounce_lsb, value)

    @property
    def touch_pad8_baseline(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad8_baseline_msb, self.__touch_pad8_baseline_lsb)
    @touch_pad8_baseline.setter
    def touch_pad8_baseline(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad8_baseline_msb, self.__touch_pad8_baseline_lsb, value)
class SAR_TOUCH_STATUS9(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xfc
        self.__touch_pad9_debounce_lsb = 29
        self.__touch_pad9_debounce_msb = 31
        self.__touch_pad9_baseline_lsb = 0
        self.__touch_pad9_baseline_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def touch_pad9_debounce(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad9_debounce_msb, self.__touch_pad9_debounce_lsb)
    @touch_pad9_debounce.setter
    def touch_pad9_debounce(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad9_debounce_msb, self.__touch_pad9_debounce_lsb, value)

    @property
    def touch_pad9_baseline(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad9_baseline_msb, self.__touch_pad9_baseline_lsb)
    @touch_pad9_baseline.setter
    def touch_pad9_baseline(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad9_baseline_msb, self.__touch_pad9_baseline_lsb, value)
class SAR_TOUCH_STATUS10(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x100
        self.__touch_pad10_debounce_lsb = 29
        self.__touch_pad10_debounce_msb = 31
        self.__touch_pad10_baseline_lsb = 0
        self.__touch_pad10_baseline_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def touch_pad10_debounce(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad10_debounce_msb, self.__touch_pad10_debounce_lsb)
    @touch_pad10_debounce.setter
    def touch_pad10_debounce(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad10_debounce_msb, self.__touch_pad10_debounce_lsb, value)

    @property
    def touch_pad10_baseline(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad10_baseline_msb, self.__touch_pad10_baseline_lsb)
    @touch_pad10_baseline.setter
    def touch_pad10_baseline(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad10_baseline_msb, self.__touch_pad10_baseline_lsb, value)
class SAR_TOUCH_STATUS11(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x104
        self.__touch_pad11_debounce_lsb = 29
        self.__touch_pad11_debounce_msb = 31
        self.__touch_pad11_baseline_lsb = 0
        self.__touch_pad11_baseline_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def touch_pad11_debounce(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad11_debounce_msb, self.__touch_pad11_debounce_lsb)
    @touch_pad11_debounce.setter
    def touch_pad11_debounce(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad11_debounce_msb, self.__touch_pad11_debounce_lsb, value)

    @property
    def touch_pad11_baseline(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad11_baseline_msb, self.__touch_pad11_baseline_lsb)
    @touch_pad11_baseline.setter
    def touch_pad11_baseline(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad11_baseline_msb, self.__touch_pad11_baseline_lsb, value)
class SAR_TOUCH_STATUS12(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x108
        self.__touch_pad12_debounce_lsb = 29
        self.__touch_pad12_debounce_msb = 31
        self.__touch_pad12_baseline_lsb = 0
        self.__touch_pad12_baseline_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def touch_pad12_debounce(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad12_debounce_msb, self.__touch_pad12_debounce_lsb)
    @touch_pad12_debounce.setter
    def touch_pad12_debounce(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad12_debounce_msb, self.__touch_pad12_debounce_lsb, value)

    @property
    def touch_pad12_baseline(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad12_baseline_msb, self.__touch_pad12_baseline_lsb)
    @touch_pad12_baseline.setter
    def touch_pad12_baseline(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad12_baseline_msb, self.__touch_pad12_baseline_lsb, value)
class SAR_TOUCH_STATUS13(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x10c
        self.__touch_pad13_debounce_lsb = 29
        self.__touch_pad13_debounce_msb = 31
        self.__touch_pad13_baseline_lsb = 0
        self.__touch_pad13_baseline_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def touch_pad13_debounce(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad13_debounce_msb, self.__touch_pad13_debounce_lsb)
    @touch_pad13_debounce.setter
    def touch_pad13_debounce(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad13_debounce_msb, self.__touch_pad13_debounce_lsb, value)

    @property
    def touch_pad13_baseline(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad13_baseline_msb, self.__touch_pad13_baseline_lsb)
    @touch_pad13_baseline.setter
    def touch_pad13_baseline(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad13_baseline_msb, self.__touch_pad13_baseline_lsb, value)
class SAR_TOUCH_STATUS14(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x110
        self.__touch_pad14_debounce_lsb = 29
        self.__touch_pad14_debounce_msb = 31
        self.__touch_pad14_baseline_lsb = 0
        self.__touch_pad14_baseline_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def touch_pad14_debounce(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad14_debounce_msb, self.__touch_pad14_debounce_lsb)
    @touch_pad14_debounce.setter
    def touch_pad14_debounce(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad14_debounce_msb, self.__touch_pad14_debounce_lsb, value)

    @property
    def touch_pad14_baseline(self):
        return self.__MEM.rdm(self.__addr, self.__touch_pad14_baseline_msb, self.__touch_pad14_baseline_lsb)
    @touch_pad14_baseline.setter
    def touch_pad14_baseline(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_pad14_baseline_msb, self.__touch_pad14_baseline_lsb, value)
class SAR_TOUCH_STATUS15(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x114
        self.__touch_slp_debounce_lsb = 29
        self.__touch_slp_debounce_msb = 31
        self.__touch_slp_baseline_lsb = 0
        self.__touch_slp_baseline_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def touch_slp_debounce(self):
        return self.__MEM.rdm(self.__addr, self.__touch_slp_debounce_msb, self.__touch_slp_debounce_lsb)
    @touch_slp_debounce.setter
    def touch_slp_debounce(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_slp_debounce_msb, self.__touch_slp_debounce_lsb, value)

    @property
    def touch_slp_baseline(self):
        return self.__MEM.rdm(self.__addr, self.__touch_slp_baseline_msb, self.__touch_slp_baseline_lsb)
    @touch_slp_baseline.setter
    def touch_slp_baseline(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_slp_baseline_msb, self.__touch_slp_baseline_lsb, value)
class SAR_TOUCH_STATUS16(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x118
        self.__touch_slp_approach_cnt_lsb = 24
        self.__touch_slp_approach_cnt_msb = 31
        self.__touch_approach_pad0_cnt_lsb = 16
        self.__touch_approach_pad0_cnt_msb = 23
        self.__touch_approach_pad1_cnt_lsb = 8
        self.__touch_approach_pad1_cnt_msb = 15
        self.__touch_approach_pad2_cnt_lsb = 0
        self.__touch_approach_pad2_cnt_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def touch_slp_approach_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__touch_slp_approach_cnt_msb, self.__touch_slp_approach_cnt_lsb)
    @touch_slp_approach_cnt.setter
    def touch_slp_approach_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_slp_approach_cnt_msb, self.__touch_slp_approach_cnt_lsb, value)

    @property
    def touch_approach_pad0_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__touch_approach_pad0_cnt_msb, self.__touch_approach_pad0_cnt_lsb)
    @touch_approach_pad0_cnt.setter
    def touch_approach_pad0_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_approach_pad0_cnt_msb, self.__touch_approach_pad0_cnt_lsb, value)

    @property
    def touch_approach_pad1_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__touch_approach_pad1_cnt_msb, self.__touch_approach_pad1_cnt_lsb)
    @touch_approach_pad1_cnt.setter
    def touch_approach_pad1_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_approach_pad1_cnt_msb, self.__touch_approach_pad1_cnt_lsb, value)

    @property
    def touch_approach_pad2_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__touch_approach_pad2_cnt_msb, self.__touch_approach_pad2_cnt_lsb)
    @touch_approach_pad2_cnt.setter
    def touch_approach_pad2_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_approach_pad2_cnt_msb, self.__touch_approach_pad2_cnt_lsb, value)
class SAR_DAC_CTRL1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x11c
        self.__reg_dac_clk_inv_lsb = 25
        self.__reg_dac_clk_inv_msb = 25
        self.__reg_dac_clk_force_high_lsb = 24
        self.__reg_dac_clk_force_high_msb = 24
        self.__reg_dac_clk_force_low_lsb = 23
        self.__reg_dac_clk_force_low_msb = 23
        self.__reg_dac_dig_force_lsb = 22
        self.__reg_dac_dig_force_msb = 22
        self.__reg_debug_bit_sel_lsb = 17
        self.__reg_debug_bit_sel_msb = 21
        self.__reg_sw_tone_en_lsb = 16
        self.__reg_sw_tone_en_msb = 16
        self.__reg_sw_fstep_lsb = 0
        self.__reg_sw_fstep_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_dac_clk_inv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dac_clk_inv_msb, self.__reg_dac_clk_inv_lsb)
    @reg_dac_clk_inv.setter
    def reg_dac_clk_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dac_clk_inv_msb, self.__reg_dac_clk_inv_lsb, value)

    @property
    def reg_dac_clk_force_high(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dac_clk_force_high_msb, self.__reg_dac_clk_force_high_lsb)
    @reg_dac_clk_force_high.setter
    def reg_dac_clk_force_high(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dac_clk_force_high_msb, self.__reg_dac_clk_force_high_lsb, value)

    @property
    def reg_dac_clk_force_low(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dac_clk_force_low_msb, self.__reg_dac_clk_force_low_lsb)
    @reg_dac_clk_force_low.setter
    def reg_dac_clk_force_low(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dac_clk_force_low_msb, self.__reg_dac_clk_force_low_lsb, value)

    @property
    def reg_dac_dig_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dac_dig_force_msb, self.__reg_dac_dig_force_lsb)
    @reg_dac_dig_force.setter
    def reg_dac_dig_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dac_dig_force_msb, self.__reg_dac_dig_force_lsb, value)

    @property
    def reg_debug_bit_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_debug_bit_sel_msb, self.__reg_debug_bit_sel_lsb)
    @reg_debug_bit_sel.setter
    def reg_debug_bit_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_debug_bit_sel_msb, self.__reg_debug_bit_sel_lsb, value)

    @property
    def reg_sw_tone_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sw_tone_en_msb, self.__reg_sw_tone_en_lsb)
    @reg_sw_tone_en.setter
    def reg_sw_tone_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sw_tone_en_msb, self.__reg_sw_tone_en_lsb, value)

    @property
    def reg_sw_fstep(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sw_fstep_msb, self.__reg_sw_fstep_lsb)
    @reg_sw_fstep.setter
    def reg_sw_fstep(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sw_fstep_msb, self.__reg_sw_fstep_lsb, value)
class SAR_DAC_CTRL2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x120
        self.__reg_dac_cw_en2_lsb = 25
        self.__reg_dac_cw_en2_msb = 25
        self.__reg_dac_cw_en1_lsb = 24
        self.__reg_dac_cw_en1_msb = 24
        self.__reg_dac_inv2_lsb = 22
        self.__reg_dac_inv2_msb = 23
        self.__reg_dac_inv1_lsb = 20
        self.__reg_dac_inv1_msb = 21
        self.__reg_dac_scale2_lsb = 18
        self.__reg_dac_scale2_msb = 19
        self.__reg_dac_scale1_lsb = 16
        self.__reg_dac_scale1_msb = 17
        self.__reg_dac_dc2_lsb = 8
        self.__reg_dac_dc2_msb = 15
        self.__reg_dac_dc1_lsb = 0
        self.__reg_dac_dc1_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_dac_cw_en2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dac_cw_en2_msb, self.__reg_dac_cw_en2_lsb)
    @reg_dac_cw_en2.setter
    def reg_dac_cw_en2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dac_cw_en2_msb, self.__reg_dac_cw_en2_lsb, value)

    @property
    def reg_dac_cw_en1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dac_cw_en1_msb, self.__reg_dac_cw_en1_lsb)
    @reg_dac_cw_en1.setter
    def reg_dac_cw_en1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dac_cw_en1_msb, self.__reg_dac_cw_en1_lsb, value)

    @property
    def reg_dac_inv2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dac_inv2_msb, self.__reg_dac_inv2_lsb)
    @reg_dac_inv2.setter
    def reg_dac_inv2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dac_inv2_msb, self.__reg_dac_inv2_lsb, value)

    @property
    def reg_dac_inv1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dac_inv1_msb, self.__reg_dac_inv1_lsb)
    @reg_dac_inv1.setter
    def reg_dac_inv1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dac_inv1_msb, self.__reg_dac_inv1_lsb, value)

    @property
    def reg_dac_scale2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dac_scale2_msb, self.__reg_dac_scale2_lsb)
    @reg_dac_scale2.setter
    def reg_dac_scale2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dac_scale2_msb, self.__reg_dac_scale2_lsb, value)

    @property
    def reg_dac_scale1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dac_scale1_msb, self.__reg_dac_scale1_lsb)
    @reg_dac_scale1.setter
    def reg_dac_scale1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dac_scale1_msb, self.__reg_dac_scale1_lsb, value)

    @property
    def reg_dac_dc2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dac_dc2_msb, self.__reg_dac_dc2_lsb)
    @reg_dac_dc2.setter
    def reg_dac_dc2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dac_dc2_msb, self.__reg_dac_dc2_lsb, value)

    @property
    def reg_dac_dc1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dac_dc1_msb, self.__reg_dac_dc1_lsb)
    @reg_dac_dc1.setter
    def reg_dac_dc1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dac_dc1_msb, self.__reg_dac_dc1_lsb, value)
class SAR_COCPU_STATE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x124
        self.__reg_cocpu_ebreak_lsb = 30
        self.__reg_cocpu_ebreak_msb = 30
        self.__reg_cocpu_trap_lsb = 29
        self.__reg_cocpu_trap_msb = 29
        self.__reg_cocpu_eoi_lsb = 28
        self.__reg_cocpu_eoi_msb = 28
        self.__reg_cocpu_reset_n_lsb = 27
        self.__reg_cocpu_reset_n_msb = 27
        self.__reg_cocpu_clk_en_lsb = 26
        self.__reg_cocpu_clk_en_msb = 26
        self.__reg_cocpu_dbg_trigger_lsb = 25
        self.__reg_cocpu_dbg_trigger_msb = 25
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_cocpu_ebreak(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_ebreak_msb, self.__reg_cocpu_ebreak_lsb)
    @reg_cocpu_ebreak.setter
    def reg_cocpu_ebreak(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_ebreak_msb, self.__reg_cocpu_ebreak_lsb, value)

    @property
    def reg_cocpu_trap(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_trap_msb, self.__reg_cocpu_trap_lsb)
    @reg_cocpu_trap.setter
    def reg_cocpu_trap(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_trap_msb, self.__reg_cocpu_trap_lsb, value)

    @property
    def reg_cocpu_eoi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_eoi_msb, self.__reg_cocpu_eoi_lsb)
    @reg_cocpu_eoi.setter
    def reg_cocpu_eoi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_eoi_msb, self.__reg_cocpu_eoi_lsb, value)

    @property
    def reg_cocpu_reset_n(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_reset_n_msb, self.__reg_cocpu_reset_n_lsb)
    @reg_cocpu_reset_n.setter
    def reg_cocpu_reset_n(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_reset_n_msb, self.__reg_cocpu_reset_n_lsb, value)

    @property
    def reg_cocpu_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_clk_en_msb, self.__reg_cocpu_clk_en_lsb)
    @reg_cocpu_clk_en.setter
    def reg_cocpu_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_clk_en_msb, self.__reg_cocpu_clk_en_lsb, value)

    @property
    def reg_cocpu_dbg_trigger(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_dbg_trigger_msb, self.__reg_cocpu_dbg_trigger_lsb)
    @reg_cocpu_dbg_trigger.setter
    def reg_cocpu_dbg_trigger(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_dbg_trigger_msb, self.__reg_cocpu_dbg_trigger_lsb, value)
class SAR_COCPU_INT_RAW(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x128
        self.__reg_cocpu_swd_int_raw_lsb = 8
        self.__reg_cocpu_swd_int_raw_msb = 8
        self.__reg_cocpu_sw_int_raw_lsb = 7
        self.__reg_cocpu_sw_int_raw_msb = 7
        self.__reg_cocpu_start_int_raw_lsb = 6
        self.__reg_cocpu_start_int_raw_msb = 6
        self.__reg_cocpu_tsens_int_raw_lsb = 5
        self.__reg_cocpu_tsens_int_raw_msb = 5
        self.__reg_cocpu_saradc2_int_raw_lsb = 4
        self.__reg_cocpu_saradc2_int_raw_msb = 4
        self.__reg_cocpu_saradc1_int_raw_lsb = 3
        self.__reg_cocpu_saradc1_int_raw_msb = 3
        self.__reg_cocpu_touch_active_int_raw_lsb = 2
        self.__reg_cocpu_touch_active_int_raw_msb = 2
        self.__reg_cocpu_touch_inactive_int_raw_lsb = 1
        self.__reg_cocpu_touch_inactive_int_raw_msb = 1
        self.__reg_cocpu_touch_done_int_raw_lsb = 0
        self.__reg_cocpu_touch_done_int_raw_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_cocpu_swd_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_swd_int_raw_msb, self.__reg_cocpu_swd_int_raw_lsb)
    @reg_cocpu_swd_int_raw.setter
    def reg_cocpu_swd_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_swd_int_raw_msb, self.__reg_cocpu_swd_int_raw_lsb, value)

    @property
    def reg_cocpu_sw_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_sw_int_raw_msb, self.__reg_cocpu_sw_int_raw_lsb)
    @reg_cocpu_sw_int_raw.setter
    def reg_cocpu_sw_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_sw_int_raw_msb, self.__reg_cocpu_sw_int_raw_lsb, value)

    @property
    def reg_cocpu_start_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_start_int_raw_msb, self.__reg_cocpu_start_int_raw_lsb)
    @reg_cocpu_start_int_raw.setter
    def reg_cocpu_start_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_start_int_raw_msb, self.__reg_cocpu_start_int_raw_lsb, value)

    @property
    def reg_cocpu_tsens_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_tsens_int_raw_msb, self.__reg_cocpu_tsens_int_raw_lsb)
    @reg_cocpu_tsens_int_raw.setter
    def reg_cocpu_tsens_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_tsens_int_raw_msb, self.__reg_cocpu_tsens_int_raw_lsb, value)

    @property
    def reg_cocpu_saradc2_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_saradc2_int_raw_msb, self.__reg_cocpu_saradc2_int_raw_lsb)
    @reg_cocpu_saradc2_int_raw.setter
    def reg_cocpu_saradc2_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_saradc2_int_raw_msb, self.__reg_cocpu_saradc2_int_raw_lsb, value)

    @property
    def reg_cocpu_saradc1_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_saradc1_int_raw_msb, self.__reg_cocpu_saradc1_int_raw_lsb)
    @reg_cocpu_saradc1_int_raw.setter
    def reg_cocpu_saradc1_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_saradc1_int_raw_msb, self.__reg_cocpu_saradc1_int_raw_lsb, value)

    @property
    def reg_cocpu_touch_active_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_touch_active_int_raw_msb, self.__reg_cocpu_touch_active_int_raw_lsb)
    @reg_cocpu_touch_active_int_raw.setter
    def reg_cocpu_touch_active_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_touch_active_int_raw_msb, self.__reg_cocpu_touch_active_int_raw_lsb, value)

    @property
    def reg_cocpu_touch_inactive_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_touch_inactive_int_raw_msb, self.__reg_cocpu_touch_inactive_int_raw_lsb)
    @reg_cocpu_touch_inactive_int_raw.setter
    def reg_cocpu_touch_inactive_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_touch_inactive_int_raw_msb, self.__reg_cocpu_touch_inactive_int_raw_lsb, value)

    @property
    def reg_cocpu_touch_done_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_touch_done_int_raw_msb, self.__reg_cocpu_touch_done_int_raw_lsb)
    @reg_cocpu_touch_done_int_raw.setter
    def reg_cocpu_touch_done_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_touch_done_int_raw_msb, self.__reg_cocpu_touch_done_int_raw_lsb, value)
class SAR_COCPU_INT_ENA(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x12c
        self.__reg_cocpu_swd_int_ena_lsb = 8
        self.__reg_cocpu_swd_int_ena_msb = 8
        self.__reg_cocpu_sw_int_ena_lsb = 7
        self.__reg_cocpu_sw_int_ena_msb = 7
        self.__reg_cocpu_start_int_ena_lsb = 6
        self.__reg_cocpu_start_int_ena_msb = 6
        self.__reg_cocpu_tsens_int_ena_lsb = 5
        self.__reg_cocpu_tsens_int_ena_msb = 5
        self.__reg_cocpu_saradc2_int_ena_lsb = 4
        self.__reg_cocpu_saradc2_int_ena_msb = 4
        self.__reg_cocpu_saradc1_int_ena_lsb = 3
        self.__reg_cocpu_saradc1_int_ena_msb = 3
        self.__reg_cocpu_touch_active_int_ena_lsb = 2
        self.__reg_cocpu_touch_active_int_ena_msb = 2
        self.__reg_cocpu_touch_inactive_int_ena_lsb = 1
        self.__reg_cocpu_touch_inactive_int_ena_msb = 1
        self.__reg_cocpu_touch_done_int_ena_lsb = 0
        self.__reg_cocpu_touch_done_int_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_cocpu_swd_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_swd_int_ena_msb, self.__reg_cocpu_swd_int_ena_lsb)
    @reg_cocpu_swd_int_ena.setter
    def reg_cocpu_swd_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_swd_int_ena_msb, self.__reg_cocpu_swd_int_ena_lsb, value)

    @property
    def reg_cocpu_sw_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_sw_int_ena_msb, self.__reg_cocpu_sw_int_ena_lsb)
    @reg_cocpu_sw_int_ena.setter
    def reg_cocpu_sw_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_sw_int_ena_msb, self.__reg_cocpu_sw_int_ena_lsb, value)

    @property
    def reg_cocpu_start_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_start_int_ena_msb, self.__reg_cocpu_start_int_ena_lsb)
    @reg_cocpu_start_int_ena.setter
    def reg_cocpu_start_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_start_int_ena_msb, self.__reg_cocpu_start_int_ena_lsb, value)

    @property
    def reg_cocpu_tsens_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_tsens_int_ena_msb, self.__reg_cocpu_tsens_int_ena_lsb)
    @reg_cocpu_tsens_int_ena.setter
    def reg_cocpu_tsens_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_tsens_int_ena_msb, self.__reg_cocpu_tsens_int_ena_lsb, value)

    @property
    def reg_cocpu_saradc2_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_saradc2_int_ena_msb, self.__reg_cocpu_saradc2_int_ena_lsb)
    @reg_cocpu_saradc2_int_ena.setter
    def reg_cocpu_saradc2_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_saradc2_int_ena_msb, self.__reg_cocpu_saradc2_int_ena_lsb, value)

    @property
    def reg_cocpu_saradc1_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_saradc1_int_ena_msb, self.__reg_cocpu_saradc1_int_ena_lsb)
    @reg_cocpu_saradc1_int_ena.setter
    def reg_cocpu_saradc1_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_saradc1_int_ena_msb, self.__reg_cocpu_saradc1_int_ena_lsb, value)

    @property
    def reg_cocpu_touch_active_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_touch_active_int_ena_msb, self.__reg_cocpu_touch_active_int_ena_lsb)
    @reg_cocpu_touch_active_int_ena.setter
    def reg_cocpu_touch_active_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_touch_active_int_ena_msb, self.__reg_cocpu_touch_active_int_ena_lsb, value)

    @property
    def reg_cocpu_touch_inactive_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_touch_inactive_int_ena_msb, self.__reg_cocpu_touch_inactive_int_ena_lsb)
    @reg_cocpu_touch_inactive_int_ena.setter
    def reg_cocpu_touch_inactive_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_touch_inactive_int_ena_msb, self.__reg_cocpu_touch_inactive_int_ena_lsb, value)

    @property
    def reg_cocpu_touch_done_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_touch_done_int_ena_msb, self.__reg_cocpu_touch_done_int_ena_lsb)
    @reg_cocpu_touch_done_int_ena.setter
    def reg_cocpu_touch_done_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_touch_done_int_ena_msb, self.__reg_cocpu_touch_done_int_ena_lsb, value)
class SAR_COCPU_INT_ST(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x130
        self.__reg_cocpu_swd_int_st_lsb = 8
        self.__reg_cocpu_swd_int_st_msb = 8
        self.__reg_cocpu_sw_int_st_lsb = 7
        self.__reg_cocpu_sw_int_st_msb = 7
        self.__reg_cocpu_start_int_st_lsb = 6
        self.__reg_cocpu_start_int_st_msb = 6
        self.__reg_cocpu_tsens_int_st_lsb = 5
        self.__reg_cocpu_tsens_int_st_msb = 5
        self.__reg_cocpu_saradc2_int_st_lsb = 4
        self.__reg_cocpu_saradc2_int_st_msb = 4
        self.__reg_cocpu_saradc1_int_st_lsb = 3
        self.__reg_cocpu_saradc1_int_st_msb = 3
        self.__reg_cocpu_touch_active_int_st_lsb = 2
        self.__reg_cocpu_touch_active_int_st_msb = 2
        self.__reg_cocpu_touch_inactive_int_st_lsb = 1
        self.__reg_cocpu_touch_inactive_int_st_msb = 1
        self.__reg_cocpu_touch_done_int_st_lsb = 0
        self.__reg_cocpu_touch_done_int_st_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_cocpu_swd_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_swd_int_st_msb, self.__reg_cocpu_swd_int_st_lsb)
    @reg_cocpu_swd_int_st.setter
    def reg_cocpu_swd_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_swd_int_st_msb, self.__reg_cocpu_swd_int_st_lsb, value)

    @property
    def reg_cocpu_sw_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_sw_int_st_msb, self.__reg_cocpu_sw_int_st_lsb)
    @reg_cocpu_sw_int_st.setter
    def reg_cocpu_sw_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_sw_int_st_msb, self.__reg_cocpu_sw_int_st_lsb, value)

    @property
    def reg_cocpu_start_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_start_int_st_msb, self.__reg_cocpu_start_int_st_lsb)
    @reg_cocpu_start_int_st.setter
    def reg_cocpu_start_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_start_int_st_msb, self.__reg_cocpu_start_int_st_lsb, value)

    @property
    def reg_cocpu_tsens_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_tsens_int_st_msb, self.__reg_cocpu_tsens_int_st_lsb)
    @reg_cocpu_tsens_int_st.setter
    def reg_cocpu_tsens_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_tsens_int_st_msb, self.__reg_cocpu_tsens_int_st_lsb, value)

    @property
    def reg_cocpu_saradc2_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_saradc2_int_st_msb, self.__reg_cocpu_saradc2_int_st_lsb)
    @reg_cocpu_saradc2_int_st.setter
    def reg_cocpu_saradc2_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_saradc2_int_st_msb, self.__reg_cocpu_saradc2_int_st_lsb, value)

    @property
    def reg_cocpu_saradc1_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_saradc1_int_st_msb, self.__reg_cocpu_saradc1_int_st_lsb)
    @reg_cocpu_saradc1_int_st.setter
    def reg_cocpu_saradc1_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_saradc1_int_st_msb, self.__reg_cocpu_saradc1_int_st_lsb, value)

    @property
    def reg_cocpu_touch_active_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_touch_active_int_st_msb, self.__reg_cocpu_touch_active_int_st_lsb)
    @reg_cocpu_touch_active_int_st.setter
    def reg_cocpu_touch_active_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_touch_active_int_st_msb, self.__reg_cocpu_touch_active_int_st_lsb, value)

    @property
    def reg_cocpu_touch_inactive_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_touch_inactive_int_st_msb, self.__reg_cocpu_touch_inactive_int_st_lsb)
    @reg_cocpu_touch_inactive_int_st.setter
    def reg_cocpu_touch_inactive_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_touch_inactive_int_st_msb, self.__reg_cocpu_touch_inactive_int_st_lsb, value)

    @property
    def reg_cocpu_touch_done_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_touch_done_int_st_msb, self.__reg_cocpu_touch_done_int_st_lsb)
    @reg_cocpu_touch_done_int_st.setter
    def reg_cocpu_touch_done_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_touch_done_int_st_msb, self.__reg_cocpu_touch_done_int_st_lsb, value)
class SAR_COCPU_INT_CLR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x134
        self.__reg_cocpu_swd_int_clr_lsb = 8
        self.__reg_cocpu_swd_int_clr_msb = 8
        self.__reg_cocpu_sw_int_clr_lsb = 7
        self.__reg_cocpu_sw_int_clr_msb = 7
        self.__reg_cocpu_start_int_clr_lsb = 6
        self.__reg_cocpu_start_int_clr_msb = 6
        self.__reg_cocpu_tsens_int_clr_lsb = 5
        self.__reg_cocpu_tsens_int_clr_msb = 5
        self.__reg_cocpu_saradc2_int_clr_lsb = 4
        self.__reg_cocpu_saradc2_int_clr_msb = 4
        self.__reg_cocpu_saradc1_int_clr_lsb = 3
        self.__reg_cocpu_saradc1_int_clr_msb = 3
        self.__reg_cocpu_touch_active_int_clr_lsb = 2
        self.__reg_cocpu_touch_active_int_clr_msb = 2
        self.__reg_cocpu_touch_inactive_int_clr_lsb = 1
        self.__reg_cocpu_touch_inactive_int_clr_msb = 1
        self.__reg_cocpu_touch_done_int_clr_lsb = 0
        self.__reg_cocpu_touch_done_int_clr_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_cocpu_swd_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_swd_int_clr_msb, self.__reg_cocpu_swd_int_clr_lsb)
    @reg_cocpu_swd_int_clr.setter
    def reg_cocpu_swd_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_swd_int_clr_msb, self.__reg_cocpu_swd_int_clr_lsb, value)

    @property
    def reg_cocpu_sw_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_sw_int_clr_msb, self.__reg_cocpu_sw_int_clr_lsb)
    @reg_cocpu_sw_int_clr.setter
    def reg_cocpu_sw_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_sw_int_clr_msb, self.__reg_cocpu_sw_int_clr_lsb, value)

    @property
    def reg_cocpu_start_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_start_int_clr_msb, self.__reg_cocpu_start_int_clr_lsb)
    @reg_cocpu_start_int_clr.setter
    def reg_cocpu_start_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_start_int_clr_msb, self.__reg_cocpu_start_int_clr_lsb, value)

    @property
    def reg_cocpu_tsens_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_tsens_int_clr_msb, self.__reg_cocpu_tsens_int_clr_lsb)
    @reg_cocpu_tsens_int_clr.setter
    def reg_cocpu_tsens_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_tsens_int_clr_msb, self.__reg_cocpu_tsens_int_clr_lsb, value)

    @property
    def reg_cocpu_saradc2_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_saradc2_int_clr_msb, self.__reg_cocpu_saradc2_int_clr_lsb)
    @reg_cocpu_saradc2_int_clr.setter
    def reg_cocpu_saradc2_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_saradc2_int_clr_msb, self.__reg_cocpu_saradc2_int_clr_lsb, value)

    @property
    def reg_cocpu_saradc1_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_saradc1_int_clr_msb, self.__reg_cocpu_saradc1_int_clr_lsb)
    @reg_cocpu_saradc1_int_clr.setter
    def reg_cocpu_saradc1_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_saradc1_int_clr_msb, self.__reg_cocpu_saradc1_int_clr_lsb, value)

    @property
    def reg_cocpu_touch_active_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_touch_active_int_clr_msb, self.__reg_cocpu_touch_active_int_clr_lsb)
    @reg_cocpu_touch_active_int_clr.setter
    def reg_cocpu_touch_active_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_touch_active_int_clr_msb, self.__reg_cocpu_touch_active_int_clr_lsb, value)

    @property
    def reg_cocpu_touch_inactive_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_touch_inactive_int_clr_msb, self.__reg_cocpu_touch_inactive_int_clr_lsb)
    @reg_cocpu_touch_inactive_int_clr.setter
    def reg_cocpu_touch_inactive_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_touch_inactive_int_clr_msb, self.__reg_cocpu_touch_inactive_int_clr_lsb, value)

    @property
    def reg_cocpu_touch_done_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_touch_done_int_clr_msb, self.__reg_cocpu_touch_done_int_clr_lsb)
    @reg_cocpu_touch_done_int_clr.setter
    def reg_cocpu_touch_done_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_touch_done_int_clr_msb, self.__reg_cocpu_touch_done_int_clr_lsb, value)
class SAR_COCPU_DEBUG(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x138
        self.__reg_cocpu_mem_addr_lsb = 19
        self.__reg_cocpu_mem_addr_msb = 31
        self.__reg_cocpu_mem_wen_lsb = 15
        self.__reg_cocpu_mem_wen_msb = 18
        self.__reg_cocpu_mem_rdy_lsb = 14
        self.__reg_cocpu_mem_rdy_msb = 14
        self.__reg_cocpu_mem_vld_lsb = 13
        self.__reg_cocpu_mem_vld_msb = 13
        self.__reg_cocpu_pc_lsb = 0
        self.__reg_cocpu_pc_msb = 12
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_cocpu_mem_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_mem_addr_msb, self.__reg_cocpu_mem_addr_lsb)
    @reg_cocpu_mem_addr.setter
    def reg_cocpu_mem_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_mem_addr_msb, self.__reg_cocpu_mem_addr_lsb, value)

    @property
    def reg_cocpu_mem_wen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_mem_wen_msb, self.__reg_cocpu_mem_wen_lsb)
    @reg_cocpu_mem_wen.setter
    def reg_cocpu_mem_wen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_mem_wen_msb, self.__reg_cocpu_mem_wen_lsb, value)

    @property
    def reg_cocpu_mem_rdy(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_mem_rdy_msb, self.__reg_cocpu_mem_rdy_lsb)
    @reg_cocpu_mem_rdy.setter
    def reg_cocpu_mem_rdy(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_mem_rdy_msb, self.__reg_cocpu_mem_rdy_lsb, value)

    @property
    def reg_cocpu_mem_vld(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_mem_vld_msb, self.__reg_cocpu_mem_vld_lsb)
    @reg_cocpu_mem_vld.setter
    def reg_cocpu_mem_vld(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_mem_vld_msb, self.__reg_cocpu_mem_vld_lsb, value)

    @property
    def reg_cocpu_pc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cocpu_pc_msb, self.__reg_cocpu_pc_lsb)
    @reg_cocpu_pc.setter
    def reg_cocpu_pc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cocpu_pc_msb, self.__reg_cocpu_pc_lsb, value)
class SAR_HALL_CTRL(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x13c
        self.__reg_hall_phase_force_lsb = 31
        self.__reg_hall_phase_force_msb = 31
        self.__reg_hall_phase_lsb = 30
        self.__reg_hall_phase_msb = 30
        self.__reg_xpd_hall_force_lsb = 29
        self.__reg_xpd_hall_force_msb = 29
        self.__reg_xpd_hall_lsb = 28
        self.__reg_xpd_hall_msb = 28
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_hall_phase_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_hall_phase_force_msb, self.__reg_hall_phase_force_lsb)
    @reg_hall_phase_force.setter
    def reg_hall_phase_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_hall_phase_force_msb, self.__reg_hall_phase_force_lsb, value)

    @property
    def reg_hall_phase(self):
        return self.__MEM.rdm(self.__addr, self.__reg_hall_phase_msb, self.__reg_hall_phase_lsb)
    @reg_hall_phase.setter
    def reg_hall_phase(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_hall_phase_msb, self.__reg_hall_phase_lsb, value)

    @property
    def reg_xpd_hall_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xpd_hall_force_msb, self.__reg_xpd_hall_force_lsb)
    @reg_xpd_hall_force.setter
    def reg_xpd_hall_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xpd_hall_force_msb, self.__reg_xpd_hall_force_lsb, value)

    @property
    def reg_xpd_hall(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xpd_hall_msb, self.__reg_xpd_hall_lsb)
    @reg_xpd_hall.setter
    def reg_xpd_hall(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xpd_hall_msb, self.__reg_xpd_hall_lsb, value)
class SAR_NOUSE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x140
        self.__reg_sar_nouse_lsb = 0
        self.__reg_sar_nouse_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sar_nouse(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar_nouse_msb, self.__reg_sar_nouse_lsb)
    @reg_sar_nouse.setter
    def reg_sar_nouse(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar_nouse_msb, self.__reg_sar_nouse_lsb, value)
class SARDATE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x144
        self.__reg_sar_date_lsb = 0
        self.__reg_sar_date_msb = 27
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sar_date(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar_date_msb, self.__reg_sar_date_lsb)
    @reg_sar_date.setter
    def reg_sar_date(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar_date_msb, self.__reg_sar_date_lsb, value)
    @property
    def default_value(self):
        return 0x1809210
