from hal.common import *
from hal.hwregister.hwreg.ESP32.addr_base import *
class FE2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.FE_TX_DCOI_CTRL = FE_TX_DCOI_CTRL(self.channel, self.chipv)
        self.FE_TX_DCOQ_CTRL = FE_TX_DCOQ_CTRL(self.channel, self.chipv)
        self.FE2_NOUSE_1 = FE2_NOUSE_1(self.channel, self.chipv)
        self.FE_AGCMEM_CTRL1 = FE_AGCMEM_CTRL1(self.channel, self.chipv)
        self.FE_AGCMEM_CTRL2 = FE_AGCMEM_CTRL2(self.channel, self.chipv)
        self.FE_TX_GAIN_MAP_0 = FE_TX_GAIN_MAP_0(self.channel, self.chipv)
        self.FE_TX_GAIN_MAP_1 = FE_TX_GAIN_MAP_1(self.channel, self.chipv)
        self.FE_TX_GAIN_MAP_2 = FE_TX_GAIN_MAP_2(self.channel, self.chipv)
        self.FE_TX_GAIN_MAP_3 = FE_TX_GAIN_MAP_3(self.channel, self.chipv)
        self.FE_TX_GAIN_MAP_4 = FE_TX_GAIN_MAP_4(self.channel, self.chipv)
        self.FE_TX_GAIN_MAP_5 = FE_TX_GAIN_MAP_5(self.channel, self.chipv)
        self.FE_TX_GAIN_MAP_6 = FE_TX_GAIN_MAP_6(self.channel, self.chipv)
        self.FE_TX_GAIN_MAP_7 = FE_TX_GAIN_MAP_7(self.channel, self.chipv)
        self.FE_TX_GAIN_MAP_8 = FE_TX_GAIN_MAP_8(self.channel, self.chipv)
        self.FE_TX_GAIN_MAP_9 = FE_TX_GAIN_MAP_9(self.channel, self.chipv)
        self.FE_TX_GAIN_MAP_10 = FE_TX_GAIN_MAP_10(self.channel, self.chipv)
        self.FE_TX_GAIN_MAP_11 = FE_TX_GAIN_MAP_11(self.channel, self.chipv)
        self.FE_TX_GAIN_MAP_12 = FE_TX_GAIN_MAP_12(self.channel, self.chipv)
        self.FE_TX_GAIN_MAP_13 = FE_TX_GAIN_MAP_13(self.channel, self.chipv)
        self.FE_TX_GAIN_MAP_14 = FE_TX_GAIN_MAP_14(self.channel, self.chipv)
        self.FE_TX_GAIN_MAP_15 = FE_TX_GAIN_MAP_15(self.channel, self.chipv)
        self.DC0_CALI_CTRL_0 = DC0_CALI_CTRL_0(self.channel, self.chipv)
        self.DC0_CALI_CTRL_1 = DC0_CALI_CTRL_1(self.channel, self.chipv)
        self.DC0_CALI_CTRL_2 = DC0_CALI_CTRL_2(self.channel, self.chipv)
        self.DC0_CALI_COARSE_RESULT = DC0_CALI_COARSE_RESULT(self.channel, self.chipv)
        self.DC0_CALI_FINE_RESULT = DC0_CALI_FINE_RESULT(self.channel, self.chipv)
        self.DC_I_REMAIN = DC_I_REMAIN(self.channel, self.chipv)
        self.DC_Q_REMAIN = DC_Q_REMAIN(self.channel, self.chipv)
        self.FE_TEST_CTRL0 = FE_TEST_CTRL0(self.channel, self.chipv)
        self.TX_DCO_CALI_CTRL = TX_DCO_CALI_CTRL(self.channel, self.chipv)
        self.TX_DCO_CALI_RESULT_I = TX_DCO_CALI_RESULT_I(self.channel, self.chipv)
        self.TX_DCO_CALI_RESULT_Q = TX_DCO_CALI_RESULT_Q(self.channel, self.chipv)
        self.FE_TX_TEST_CTRL4 = FE_TX_TEST_CTRL4(self.channel, self.chipv)
        self.FE_IQ_EST_SNR = FE_IQ_EST_SNR(self.channel, self.chipv)
        self.FE_TEST_TRI_CTRL = FE_TEST_TRI_CTRL(self.channel, self.chipv)
        self.FE2_DPD_COMP_DATA = FE2_DPD_COMP_DATA(self.channel, self.chipv)
        self.FE2_FREQ_CTRL1 = FE2_FREQ_CTRL1(self.channel, self.chipv)
        self.FE2_FREQ_CTRL2 = FE2_FREQ_CTRL2(self.channel, self.chipv)
        self.FE2_TX_MASK_CTRL = FE2_TX_MASK_CTRL(self.channel, self.chipv)
        self.FE2_TX_DC_CTRL = FE2_TX_DC_CTRL(self.channel, self.chipv)
        self.FE2_RX_MASK_CTRL = FE2_RX_MASK_CTRL(self.channel, self.chipv)
        self.FE2_RX_DC_CTRL = FE2_RX_DC_CTRL(self.channel, self.chipv)
        self.FE2_IQ_MIS_CTRL = FE2_IQ_MIS_CTRL(self.channel, self.chipv)
        self.FE2_ADC_CAL_I = FE2_ADC_CAL_I(self.channel, self.chipv)
        self.ADC_CAL_Q = ADC_CAL_Q(self.channel, self.chipv)
        self.FE2_SCALE_CTRL = FE2_SCALE_CTRL(self.channel, self.chipv)
        self.FE2_TX_TONE_CTRL = FE2_TX_TONE_CTRL(self.channel, self.chipv)
        self.FE2_TX_INTERP_CTRL = FE2_TX_INTERP_CTRL(self.channel, self.chipv)
        self.FE_RX_SCALE = FE_RX_SCALE(self.channel, self.chipv)
        self.FE2_NOUSE = FE2_NOUSE(self.channel, self.chipv)
        self.FE2_DPD_CFG1 = FE2_DPD_CFG1(self.channel, self.chipv)
        self.FE2_ANT_CTRL0 = FE2_ANT_CTRL0(self.channel, self.chipv)
        self.FE2_ANT_CTRL1 = FE2_ANT_CTRL1(self.channel, self.chipv)
        self.FE2_ANT_CTRL2 = FE2_ANT_CTRL2(self.channel, self.chipv)
        self.FE2_ANT_CTRL3 = FE2_ANT_CTRL3(self.channel, self.chipv)
        self.FE_RX_SYN3 = FE_RX_SYN3(self.channel, self.chipv)
        self.FE_RX_SYN3_2 = FE_RX_SYN3_2(self.channel, self.chipv)
        self.FE2_NOUSE_2 = FE2_NOUSE_2(self.channel, self.chipv)
class FE_TX_DCOI_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x0
        self.__reg_tx_dcoi_ctrl_lsb = 0
        self.__reg_tx_dcoi_ctrl_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_dcoi_ctrl(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_dcoi_ctrl_msb, self.__reg_tx_dcoi_ctrl_lsb)
    @reg_tx_dcoi_ctrl.setter
    def reg_tx_dcoi_ctrl(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_dcoi_ctrl_msb, self.__reg_tx_dcoi_ctrl_lsb, value)
class FE_TX_DCOQ_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x4
        self.__reg_tx_dcoq_ctrl_lsb = 0
        self.__reg_tx_dcoq_ctrl_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_dcoq_ctrl(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_dcoq_ctrl_msb, self.__reg_tx_dcoq_ctrl_lsb)
    @reg_tx_dcoq_ctrl.setter
    def reg_tx_dcoq_ctrl(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_dcoq_ctrl_msb, self.__reg_tx_dcoq_ctrl_lsb, value)
class FE2_NOUSE_1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x8
        self.__reg_fe2_nouse_1_lsb = 0
        self.__reg_fe2_nouse_1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_fe2_nouse_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fe2_nouse_1_msb, self.__reg_fe2_nouse_1_lsb)
    @reg_fe2_nouse_1.setter
    def reg_fe2_nouse_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fe2_nouse_1_msb, self.__reg_fe2_nouse_1_lsb, value)
class FE_AGCMEM_CTRL1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x34
        self.__reg_apb2i2c_en_lsb = 20
        self.__reg_apb2i2c_en_msb = 20
        self.__reg_tx_gain_upd_en_lsb = 19
        self.__reg_tx_gain_upd_en_msb = 19
        self.__reg_tx_gain_upd_lsb = 18
        self.__reg_tx_gain_upd_msb = 18
        self.__reg_pbus_mem_we_lsb = 17
        self.__reg_pbus_mem_we_msb = 17
        self.__reg_agcmem_we_lsb = 16
        self.__reg_agcmem_we_msb = 16
        self.__reg_agcmem_waddr_lsb = 8
        self.__reg_agcmem_waddr_msb = 15
        self.__reg_agcmem_wbe_lsb = 0
        self.__reg_agcmem_wbe_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_apb2i2c_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_apb2i2c_en_msb, self.__reg_apb2i2c_en_lsb)
    @reg_apb2i2c_en.setter
    def reg_apb2i2c_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_apb2i2c_en_msb, self.__reg_apb2i2c_en_lsb, value)

    @property
    def reg_tx_gain_upd_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_gain_upd_en_msb, self.__reg_tx_gain_upd_en_lsb)
    @reg_tx_gain_upd_en.setter
    def reg_tx_gain_upd_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_gain_upd_en_msb, self.__reg_tx_gain_upd_en_lsb, value)

    @property
    def reg_tx_gain_upd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_gain_upd_msb, self.__reg_tx_gain_upd_lsb)
    @reg_tx_gain_upd.setter
    def reg_tx_gain_upd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_gain_upd_msb, self.__reg_tx_gain_upd_lsb, value)

    @property
    def reg_pbus_mem_we(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pbus_mem_we_msb, self.__reg_pbus_mem_we_lsb)
    @reg_pbus_mem_we.setter
    def reg_pbus_mem_we(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pbus_mem_we_msb, self.__reg_pbus_mem_we_lsb, value)

    @property
    def reg_agcmem_we(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agcmem_we_msb, self.__reg_agcmem_we_lsb)
    @reg_agcmem_we.setter
    def reg_agcmem_we(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agcmem_we_msb, self.__reg_agcmem_we_lsb, value)

    @property
    def reg_agcmem_waddr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agcmem_waddr_msb, self.__reg_agcmem_waddr_lsb)
    @reg_agcmem_waddr.setter
    def reg_agcmem_waddr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agcmem_waddr_msb, self.__reg_agcmem_waddr_lsb, value)

    @property
    def reg_agcmem_wbe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agcmem_wbe_msb, self.__reg_agcmem_wbe_lsb)
    @reg_agcmem_wbe.setter
    def reg_agcmem_wbe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agcmem_wbe_msb, self.__reg_agcmem_wbe_lsb, value)
class FE_AGCMEM_CTRL2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x38
        self.__reg_agcmem_wdata_lsb = 0
        self.__reg_agcmem_wdata_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_agcmem_wdata(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agcmem_wdata_msb, self.__reg_agcmem_wdata_lsb)
    @reg_agcmem_wdata.setter
    def reg_agcmem_wdata(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agcmem_wdata_msb, self.__reg_agcmem_wdata_lsb, value)
class FE_TX_GAIN_MAP_0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x3c
        self.__reg_tx_gain_map_0_lsb = 0
        self.__reg_tx_gain_map_0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_gain_map_0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_gain_map_0_msb, self.__reg_tx_gain_map_0_lsb)
    @reg_tx_gain_map_0.setter
    def reg_tx_gain_map_0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_gain_map_0_msb, self.__reg_tx_gain_map_0_lsb, value)
class FE_TX_GAIN_MAP_1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x40
        self.__reg_tx_gain_map_1_lsb = 0
        self.__reg_tx_gain_map_1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_gain_map_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_gain_map_1_msb, self.__reg_tx_gain_map_1_lsb)
    @reg_tx_gain_map_1.setter
    def reg_tx_gain_map_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_gain_map_1_msb, self.__reg_tx_gain_map_1_lsb, value)
class FE_TX_GAIN_MAP_2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x44
        self.__reg_tx_gain_map_2_lsb = 0
        self.__reg_tx_gain_map_2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_gain_map_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_gain_map_2_msb, self.__reg_tx_gain_map_2_lsb)
    @reg_tx_gain_map_2.setter
    def reg_tx_gain_map_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_gain_map_2_msb, self.__reg_tx_gain_map_2_lsb, value)
class FE_TX_GAIN_MAP_3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x48
        self.__reg_tx_gain_map_3_lsb = 0
        self.__reg_tx_gain_map_3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_gain_map_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_gain_map_3_msb, self.__reg_tx_gain_map_3_lsb)
    @reg_tx_gain_map_3.setter
    def reg_tx_gain_map_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_gain_map_3_msb, self.__reg_tx_gain_map_3_lsb, value)
class FE_TX_GAIN_MAP_4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x4c
        self.__reg_tx_gain_map_4_lsb = 0
        self.__reg_tx_gain_map_4_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_gain_map_4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_gain_map_4_msb, self.__reg_tx_gain_map_4_lsb)
    @reg_tx_gain_map_4.setter
    def reg_tx_gain_map_4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_gain_map_4_msb, self.__reg_tx_gain_map_4_lsb, value)
class FE_TX_GAIN_MAP_5(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x50
        self.__reg_tx_gain_map_5_lsb = 0
        self.__reg_tx_gain_map_5_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_gain_map_5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_gain_map_5_msb, self.__reg_tx_gain_map_5_lsb)
    @reg_tx_gain_map_5.setter
    def reg_tx_gain_map_5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_gain_map_5_msb, self.__reg_tx_gain_map_5_lsb, value)
class FE_TX_GAIN_MAP_6(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x54
        self.__reg_tx_gain_map_6_lsb = 0
        self.__reg_tx_gain_map_6_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_gain_map_6(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_gain_map_6_msb, self.__reg_tx_gain_map_6_lsb)
    @reg_tx_gain_map_6.setter
    def reg_tx_gain_map_6(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_gain_map_6_msb, self.__reg_tx_gain_map_6_lsb, value)
class FE_TX_GAIN_MAP_7(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x58
        self.__reg_tx_gain_map_7_lsb = 0
        self.__reg_tx_gain_map_7_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_gain_map_7(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_gain_map_7_msb, self.__reg_tx_gain_map_7_lsb)
    @reg_tx_gain_map_7.setter
    def reg_tx_gain_map_7(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_gain_map_7_msb, self.__reg_tx_gain_map_7_lsb, value)
class FE_TX_GAIN_MAP_8(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x5c
        self.__reg_tx_gain_map_8_lsb = 0
        self.__reg_tx_gain_map_8_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_gain_map_8(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_gain_map_8_msb, self.__reg_tx_gain_map_8_lsb)
    @reg_tx_gain_map_8.setter
    def reg_tx_gain_map_8(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_gain_map_8_msb, self.__reg_tx_gain_map_8_lsb, value)
class FE_TX_GAIN_MAP_9(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x60
        self.__reg_tx_gain_map_9_lsb = 0
        self.__reg_tx_gain_map_9_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_gain_map_9(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_gain_map_9_msb, self.__reg_tx_gain_map_9_lsb)
    @reg_tx_gain_map_9.setter
    def reg_tx_gain_map_9(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_gain_map_9_msb, self.__reg_tx_gain_map_9_lsb, value)
class FE_TX_GAIN_MAP_10(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x64
        self.__reg_tx_gain_map_10_lsb = 0
        self.__reg_tx_gain_map_10_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_gain_map_10(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_gain_map_10_msb, self.__reg_tx_gain_map_10_lsb)
    @reg_tx_gain_map_10.setter
    def reg_tx_gain_map_10(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_gain_map_10_msb, self.__reg_tx_gain_map_10_lsb, value)
class FE_TX_GAIN_MAP_11(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x68
        self.__reg_tx_gain_map_11_lsb = 0
        self.__reg_tx_gain_map_11_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_gain_map_11(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_gain_map_11_msb, self.__reg_tx_gain_map_11_lsb)
    @reg_tx_gain_map_11.setter
    def reg_tx_gain_map_11(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_gain_map_11_msb, self.__reg_tx_gain_map_11_lsb, value)
class FE_TX_GAIN_MAP_12(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x6c
        self.__reg_tx_gain_map_12_lsb = 0
        self.__reg_tx_gain_map_12_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_gain_map_12(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_gain_map_12_msb, self.__reg_tx_gain_map_12_lsb)
    @reg_tx_gain_map_12.setter
    def reg_tx_gain_map_12(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_gain_map_12_msb, self.__reg_tx_gain_map_12_lsb, value)
class FE_TX_GAIN_MAP_13(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x70
        self.__reg_tx_gain_map_13_lsb = 0
        self.__reg_tx_gain_map_13_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_gain_map_13(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_gain_map_13_msb, self.__reg_tx_gain_map_13_lsb)
    @reg_tx_gain_map_13.setter
    def reg_tx_gain_map_13(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_gain_map_13_msb, self.__reg_tx_gain_map_13_lsb, value)
class FE_TX_GAIN_MAP_14(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x74
        self.__reg_tx_gain_map_14_lsb = 0
        self.__reg_tx_gain_map_14_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_gain_map_14(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_gain_map_14_msb, self.__reg_tx_gain_map_14_lsb)
    @reg_tx_gain_map_14.setter
    def reg_tx_gain_map_14(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_gain_map_14_msb, self.__reg_tx_gain_map_14_lsb, value)
class FE_TX_GAIN_MAP_15(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x78
        self.__reg_tx_gain_map_15_lsb = 0
        self.__reg_tx_gain_map_15_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_gain_map_15(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_gain_map_15_msb, self.__reg_tx_gain_map_15_lsb)
    @reg_tx_gain_map_15.setter
    def reg_tx_gain_map_15(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_gain_map_15_msb, self.__reg_tx_gain_map_15_lsb, value)
class DC0_CALI_CTRL_0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x7c
        self.__dco_cali_done_lsb = 31
        self.__dco_cali_done_msb = 31
        self.__reg_dco_cali_ctrl_0_lsb = 0
        self.__reg_dco_cali_ctrl_0_msb = 30
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def dco_cali_done(self):
        return self.__MEM.rdm(self.__addr, self.__dco_cali_done_msb, self.__dco_cali_done_lsb)
    @dco_cali_done.setter
    def dco_cali_done(self, value):
        return self.__MEM.wrm(self.__addr, self.__dco_cali_done_msb, self.__dco_cali_done_lsb, value)

    @property
    def reg_dco_cali_ctrl_0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dco_cali_ctrl_0_msb, self.__reg_dco_cali_ctrl_0_lsb)
    @reg_dco_cali_ctrl_0.setter
    def reg_dco_cali_ctrl_0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dco_cali_ctrl_0_msb, self.__reg_dco_cali_ctrl_0_lsb, value)
class DC0_CALI_CTRL_1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x80
        self.__dco_iterration_time_lsb = 22
        self.__dco_iterration_time_msb = 31
        self.__dco_cali_success_lsb = 20
        self.__dco_cali_success_msb = 21
        self.__reg_dco_cali_ctrl_1_lsb = 0
        self.__reg_dco_cali_ctrl_1_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def dco_iterration_time(self):
        return self.__MEM.rdm(self.__addr, self.__dco_iterration_time_msb, self.__dco_iterration_time_lsb)
    @dco_iterration_time.setter
    def dco_iterration_time(self, value):
        return self.__MEM.wrm(self.__addr, self.__dco_iterration_time_msb, self.__dco_iterration_time_lsb, value)

    @property
    def dco_cali_success(self):
        return self.__MEM.rdm(self.__addr, self.__dco_cali_success_msb, self.__dco_cali_success_lsb)
    @dco_cali_success.setter
    def dco_cali_success(self, value):
        return self.__MEM.wrm(self.__addr, self.__dco_cali_success_msb, self.__dco_cali_success_lsb, value)

    @property
    def reg_dco_cali_ctrl_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dco_cali_ctrl_1_msb, self.__reg_dco_cali_ctrl_1_lsb)
    @reg_dco_cali_ctrl_1.setter
    def reg_dco_cali_ctrl_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dco_cali_ctrl_1_msb, self.__reg_dco_cali_ctrl_1_lsb, value)
class DC0_CALI_CTRL_2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x84
        self.__reg_dco_cali_ctrl_2_lsb = 0
        self.__reg_dco_cali_ctrl_2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_dco_cali_ctrl_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dco_cali_ctrl_2_msb, self.__reg_dco_cali_ctrl_2_lsb)
    @reg_dco_cali_ctrl_2.setter
    def reg_dco_cali_ctrl_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dco_cali_ctrl_2_msb, self.__reg_dco_cali_ctrl_2_lsb, value)
class DC0_CALI_COARSE_RESULT(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x88
        self.__dco_coarse_result_lsb = 0
        self.__dco_coarse_result_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def dco_coarse_result(self):
        return self.__MEM.rdm(self.__addr, self.__dco_coarse_result_msb, self.__dco_coarse_result_lsb)
    @dco_coarse_result.setter
    def dco_coarse_result(self, value):
        return self.__MEM.wrm(self.__addr, self.__dco_coarse_result_msb, self.__dco_coarse_result_lsb, value)
class DC0_CALI_FINE_RESULT(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x8c
        self.__dco_fine_result_lsb = 0
        self.__dco_fine_result_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def dco_fine_result(self):
        return self.__MEM.rdm(self.__addr, self.__dco_fine_result_msb, self.__dco_fine_result_lsb)
    @dco_fine_result.setter
    def dco_fine_result(self, value):
        return self.__MEM.wrm(self.__addr, self.__dco_fine_result_msb, self.__dco_fine_result_lsb, value)
class DC_I_REMAIN(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x90
        self.__dc_i_remain_lsb = 0
        self.__dc_i_remain_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def dc_i_remain(self):
        return self.__MEM.rdm(self.__addr, self.__dc_i_remain_msb, self.__dc_i_remain_lsb)
    @dc_i_remain.setter
    def dc_i_remain(self, value):
        return self.__MEM.wrm(self.__addr, self.__dc_i_remain_msb, self.__dc_i_remain_lsb, value)
class DC_Q_REMAIN(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x94
        self.__dc_q_remain_lsb = 0
        self.__dc_q_remain_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def dc_q_remain(self):
        return self.__MEM.rdm(self.__addr, self.__dc_q_remain_msb, self.__dc_q_remain_lsb)
    @dc_q_remain.setter
    def dc_q_remain(self, value):
        return self.__MEM.wrm(self.__addr, self.__dc_q_remain_msb, self.__dc_q_remain_lsb, value)
class FE_TEST_CTRL0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x98
        self.__reg_adc_ana_oe_lsb = 0
        self.__reg_adc_ana_oe_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_adc_ana_oe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_ana_oe_msb, self.__reg_adc_ana_oe_lsb)
    @reg_adc_ana_oe.setter
    def reg_adc_ana_oe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_ana_oe_msb, self.__reg_adc_ana_oe_lsb, value)
class TX_DCO_CALI_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x9c
        self.__tx_dco_cali_done_lsb = 31
        self.__tx_dco_cali_done_msb = 31
        self.__tx_dco_cali_success_lsb = 29
        self.__tx_dco_cali_success_msb = 30
        self.__reg_tx_dco_cali_ctrl_lsb = 0
        self.__reg_tx_dco_cali_ctrl_msb = 28
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tx_dco_cali_done(self):
        return self.__MEM.rdm(self.__addr, self.__tx_dco_cali_done_msb, self.__tx_dco_cali_done_lsb)
    @tx_dco_cali_done.setter
    def tx_dco_cali_done(self, value):
        return self.__MEM.wrm(self.__addr, self.__tx_dco_cali_done_msb, self.__tx_dco_cali_done_lsb, value)

    @property
    def tx_dco_cali_success(self):
        return self.__MEM.rdm(self.__addr, self.__tx_dco_cali_success_msb, self.__tx_dco_cali_success_lsb)
    @tx_dco_cali_success.setter
    def tx_dco_cali_success(self, value):
        return self.__MEM.wrm(self.__addr, self.__tx_dco_cali_success_msb, self.__tx_dco_cali_success_lsb, value)

    @property
    def reg_tx_dco_cali_ctrl(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_dco_cali_ctrl_msb, self.__reg_tx_dco_cali_ctrl_lsb)
    @reg_tx_dco_cali_ctrl.setter
    def reg_tx_dco_cali_ctrl(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_dco_cali_ctrl_msb, self.__reg_tx_dco_cali_ctrl_lsb, value)
class TX_DCO_CALI_RESULT_I(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0xa0
        self.__tx_dco_cali_time_coarse_lsb = 27
        self.__tx_dco_cali_time_coarse_msb = 31
        self.__tx_dco_cali_time_fine_lsb = 22
        self.__tx_dco_cali_time_fine_msb = 26
        self.__tx_dco_cali_result_i_lsb = 0
        self.__tx_dco_cali_result_i_msb = 21
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tx_dco_cali_time_coarse(self):
        return self.__MEM.rdm(self.__addr, self.__tx_dco_cali_time_coarse_msb, self.__tx_dco_cali_time_coarse_lsb)
    @tx_dco_cali_time_coarse.setter
    def tx_dco_cali_time_coarse(self, value):
        return self.__MEM.wrm(self.__addr, self.__tx_dco_cali_time_coarse_msb, self.__tx_dco_cali_time_coarse_lsb, value)

    @property
    def tx_dco_cali_time_fine(self):
        return self.__MEM.rdm(self.__addr, self.__tx_dco_cali_time_fine_msb, self.__tx_dco_cali_time_fine_lsb)
    @tx_dco_cali_time_fine.setter
    def tx_dco_cali_time_fine(self, value):
        return self.__MEM.wrm(self.__addr, self.__tx_dco_cali_time_fine_msb, self.__tx_dco_cali_time_fine_lsb, value)

    @property
    def tx_dco_cali_result_i(self):
        return self.__MEM.rdm(self.__addr, self.__tx_dco_cali_result_i_msb, self.__tx_dco_cali_result_i_lsb)
    @tx_dco_cali_result_i.setter
    def tx_dco_cali_result_i(self, value):
        return self.__MEM.wrm(self.__addr, self.__tx_dco_cali_result_i_msb, self.__tx_dco_cali_result_i_lsb, value)
class TX_DCO_CALI_RESULT_Q(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0xa4
        self.__tx_dco_cali_result_q_lsb = 0
        self.__tx_dco_cali_result_q_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tx_dco_cali_result_q(self):
        return self.__MEM.rdm(self.__addr, self.__tx_dco_cali_result_q_msb, self.__tx_dco_cali_result_q_lsb)
    @tx_dco_cali_result_q.setter
    def tx_dco_cali_result_q(self, value):
        return self.__MEM.wrm(self.__addr, self.__tx_dco_cali_result_q_msb, self.__tx_dco_cali_result_q_lsb, value)
class FE_TX_TEST_CTRL4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0xa8
        self.__reg_tx_test_ctrl4_lsb = 0
        self.__reg_tx_test_ctrl4_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_test_ctrl4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_test_ctrl4_msb, self.__reg_tx_test_ctrl4_lsb)
    @reg_tx_test_ctrl4.setter
    def reg_tx_test_ctrl4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_test_ctrl4_msb, self.__reg_tx_test_ctrl4_lsb, value)
class FE_IQ_EST_SNR(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0xac
        self.__reg_fe_iq_est_snr_lsb = 0
        self.__reg_fe_iq_est_snr_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_fe_iq_est_snr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fe_iq_est_snr_msb, self.__reg_fe_iq_est_snr_lsb)
    @reg_fe_iq_est_snr.setter
    def reg_fe_iq_est_snr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fe_iq_est_snr_msb, self.__reg_fe_iq_est_snr_lsb, value)
class FE_TEST_TRI_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0xb0
        self.__reg_sw_tri_en_lsb = 26
        self.__reg_sw_tri_en_msb = 26
        self.__reg_tri_max_abs_lsb = 16
        self.__reg_tri_max_abs_msb = 25
        self.__reg_tri_clk_div_lsb = 12
        self.__reg_tri_clk_div_msb = 15
        self.__reg_sw_tri_step_lsb = 0
        self.__reg_sw_tri_step_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sw_tri_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sw_tri_en_msb, self.__reg_sw_tri_en_lsb)
    @reg_sw_tri_en.setter
    def reg_sw_tri_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sw_tri_en_msb, self.__reg_sw_tri_en_lsb, value)

    @property
    def reg_tri_max_abs(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tri_max_abs_msb, self.__reg_tri_max_abs_lsb)
    @reg_tri_max_abs.setter
    def reg_tri_max_abs(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tri_max_abs_msb, self.__reg_tri_max_abs_lsb, value)

    @property
    def reg_tri_clk_div(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tri_clk_div_msb, self.__reg_tri_clk_div_lsb)
    @reg_tri_clk_div.setter
    def reg_tri_clk_div(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tri_clk_div_msb, self.__reg_tri_clk_div_lsb, value)

    @property
    def reg_sw_tri_step(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sw_tri_step_msb, self.__reg_sw_tri_step_lsb)
    @reg_sw_tri_step.setter
    def reg_sw_tri_step(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sw_tri_step_msb, self.__reg_sw_tri_step_lsb, value)
class FE2_DPD_COMP_DATA(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0xc0
        self.__reg_dpd_comp_rd_lsb = 0
        self.__reg_dpd_comp_rd_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_dpd_comp_rd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dpd_comp_rd_msb, self.__reg_dpd_comp_rd_lsb)
    @reg_dpd_comp_rd.setter
    def reg_dpd_comp_rd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dpd_comp_rd_msb, self.__reg_dpd_comp_rd_lsb, value)
class FE2_FREQ_CTRL1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0xc4
        self.__reg_freq_rf_a_lsb = 0
        self.__reg_freq_rf_a_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_freq_rf_a(self):
        return self.__MEM.rdm(self.__addr, self.__reg_freq_rf_a_msb, self.__reg_freq_rf_a_lsb)
    @reg_freq_rf_a.setter
    def reg_freq_rf_a(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_freq_rf_a_msb, self.__reg_freq_rf_a_lsb, value)
class FE2_FREQ_CTRL2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0xc8
        self.__reg_freq_dig_b_lsb = 0
        self.__reg_freq_dig_b_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_freq_dig_b(self):
        return self.__MEM.rdm(self.__addr, self.__reg_freq_dig_b_msb, self.__reg_freq_dig_b_lsb)
    @reg_freq_dig_b.setter
    def reg_freq_dig_b(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_freq_dig_b_msb, self.__reg_freq_dig_b_lsb, value)
class FE2_TX_MASK_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0xcc
        self.__reg_analog_txtone_en_lsb = 23
        self.__reg_analog_txtone_en_msb = 23
        self.__reg_dpd_bypass_lsb = 22
        self.__reg_dpd_bypass_msb = 22
        self.__reg_tx_q_mask_lsb = 10
        self.__reg_tx_q_mask_msb = 19
        self.__reg_tx_i_mask_lsb = 0
        self.__reg_tx_i_mask_msb = 9
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_analog_txtone_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_analog_txtone_en_msb, self.__reg_analog_txtone_en_lsb)
    @reg_analog_txtone_en.setter
    def reg_analog_txtone_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_analog_txtone_en_msb, self.__reg_analog_txtone_en_lsb, value)

    @property
    def reg_dpd_bypass(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dpd_bypass_msb, self.__reg_dpd_bypass_lsb)
    @reg_dpd_bypass.setter
    def reg_dpd_bypass(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dpd_bypass_msb, self.__reg_dpd_bypass_lsb, value)

    @property
    def reg_tx_q_mask(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_q_mask_msb, self.__reg_tx_q_mask_lsb)
    @reg_tx_q_mask.setter
    def reg_tx_q_mask(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_q_mask_msb, self.__reg_tx_q_mask_lsb, value)

    @property
    def reg_tx_i_mask(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_i_mask_msb, self.__reg_tx_i_mask_lsb)
    @reg_tx_i_mask.setter
    def reg_tx_i_mask(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_i_mask_msb, self.__reg_tx_i_mask_lsb, value)
class FE2_TX_DC_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0xd0
        self.__reg_tx_filt_gain_lsb = 31
        self.__reg_tx_filt_gain_msb = 31
        self.__reg_tx_interp_bypass_lsb = 30
        self.__reg_tx_interp_bypass_msb = 30
        self.__reg_adc_dump_sel_lsb = 29
        self.__reg_adc_dump_sel_msb = 29
        self.__reg_loop_back_en_lsb = 28
        self.__reg_loop_back_en_msb = 28
        self.__reg_tx_local_edge_lsb = 27
        self.__reg_tx_local_edge_msb = 27
        self.__reg_rx_local_edge_lsb = 26
        self.__reg_rx_local_edge_msb = 26
        self.__reg_rx_phase_det_en_lsb = 25
        self.__reg_rx_phase_det_en_msb = 25
        self.__reg_rx_sync_sel_lsb = 24
        self.__reg_rx_sync_sel_msb = 24
        self.__reg_rx_sync_way2_inv_lsb = 23
        self.__reg_rx_sync_way2_inv_msb = 23
        self.__reg_tx_ht2040_test_lsb = 22
        self.__reg_tx_ht2040_test_msb = 22
        self.__reg_tx_40to80_en_lsb = 21
        self.__reg_tx_40to80_en_msb = 21
        self.__reg_adc_quick_oe_lsb = 20
        self.__reg_adc_quick_oe_msb = 20
        self.__reg_tx_q_dc_lsb = 10
        self.__reg_tx_q_dc_msb = 19
        self.__reg_tx_i_dc_lsb = 0
        self.__reg_tx_i_dc_msb = 9
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_filt_gain(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_filt_gain_msb, self.__reg_tx_filt_gain_lsb)
    @reg_tx_filt_gain.setter
    def reg_tx_filt_gain(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_filt_gain_msb, self.__reg_tx_filt_gain_lsb, value)

    @property
    def reg_tx_interp_bypass(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_interp_bypass_msb, self.__reg_tx_interp_bypass_lsb)
    @reg_tx_interp_bypass.setter
    def reg_tx_interp_bypass(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_interp_bypass_msb, self.__reg_tx_interp_bypass_lsb, value)

    @property
    def reg_adc_dump_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_dump_sel_msb, self.__reg_adc_dump_sel_lsb)
    @reg_adc_dump_sel.setter
    def reg_adc_dump_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_dump_sel_msb, self.__reg_adc_dump_sel_lsb, value)

    @property
    def reg_loop_back_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_loop_back_en_msb, self.__reg_loop_back_en_lsb)
    @reg_loop_back_en.setter
    def reg_loop_back_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_loop_back_en_msb, self.__reg_loop_back_en_lsb, value)

    @property
    def reg_tx_local_edge(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_local_edge_msb, self.__reg_tx_local_edge_lsb)
    @reg_tx_local_edge.setter
    def reg_tx_local_edge(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_local_edge_msb, self.__reg_tx_local_edge_lsb, value)

    @property
    def reg_rx_local_edge(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_local_edge_msb, self.__reg_rx_local_edge_lsb)
    @reg_rx_local_edge.setter
    def reg_rx_local_edge(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_local_edge_msb, self.__reg_rx_local_edge_lsb, value)

    @property
    def reg_rx_phase_det_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_phase_det_en_msb, self.__reg_rx_phase_det_en_lsb)
    @reg_rx_phase_det_en.setter
    def reg_rx_phase_det_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_phase_det_en_msb, self.__reg_rx_phase_det_en_lsb, value)

    @property
    def reg_rx_sync_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_sync_sel_msb, self.__reg_rx_sync_sel_lsb)
    @reg_rx_sync_sel.setter
    def reg_rx_sync_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_sync_sel_msb, self.__reg_rx_sync_sel_lsb, value)

    @property
    def reg_rx_sync_way2_inv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_sync_way2_inv_msb, self.__reg_rx_sync_way2_inv_lsb)
    @reg_rx_sync_way2_inv.setter
    def reg_rx_sync_way2_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_sync_way2_inv_msb, self.__reg_rx_sync_way2_inv_lsb, value)

    @property
    def reg_tx_ht2040_test(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_ht2040_test_msb, self.__reg_tx_ht2040_test_lsb)
    @reg_tx_ht2040_test.setter
    def reg_tx_ht2040_test(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_ht2040_test_msb, self.__reg_tx_ht2040_test_lsb, value)

    @property
    def reg_tx_40to80_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_40to80_en_msb, self.__reg_tx_40to80_en_lsb)
    @reg_tx_40to80_en.setter
    def reg_tx_40to80_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_40to80_en_msb, self.__reg_tx_40to80_en_lsb, value)

    @property
    def reg_adc_quick_oe(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_quick_oe_msb, self.__reg_adc_quick_oe_lsb)
    @reg_adc_quick_oe.setter
    def reg_adc_quick_oe(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_quick_oe_msb, self.__reg_adc_quick_oe_lsb, value)

    @property
    def reg_tx_q_dc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_q_dc_msb, self.__reg_tx_q_dc_lsb)
    @reg_tx_q_dc.setter
    def reg_tx_q_dc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_q_dc_msb, self.__reg_tx_q_dc_lsb, value)

    @property
    def reg_tx_i_dc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_i_dc_msb, self.__reg_tx_i_dc_lsb)
    @reg_tx_i_dc.setter
    def reg_tx_i_dc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_i_dc_msb, self.__reg_tx_i_dc_lsb, value)
class FE2_RX_MASK_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0xd4
        self.__reg_rx_phase_det_delay_lsb = 24
        self.__reg_rx_phase_det_delay_msb = 31
        self.__reg_tx_phase_det_delay_lsb = 18
        self.__reg_tx_phase_det_delay_msb = 23
        self.__reg_rx_q_mask_lsb = 9
        self.__reg_rx_q_mask_msb = 17
        self.__reg_rx_i_mask_lsb = 0
        self.__reg_rx_i_mask_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rx_phase_det_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_phase_det_delay_msb, self.__reg_rx_phase_det_delay_lsb)
    @reg_rx_phase_det_delay.setter
    def reg_rx_phase_det_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_phase_det_delay_msb, self.__reg_rx_phase_det_delay_lsb, value)

    @property
    def reg_tx_phase_det_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_phase_det_delay_msb, self.__reg_tx_phase_det_delay_lsb)
    @reg_tx_phase_det_delay.setter
    def reg_tx_phase_det_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_phase_det_delay_msb, self.__reg_tx_phase_det_delay_lsb, value)

    @property
    def reg_rx_q_mask(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_q_mask_msb, self.__reg_rx_q_mask_lsb)
    @reg_rx_q_mask.setter
    def reg_rx_q_mask(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_q_mask_msb, self.__reg_rx_q_mask_lsb, value)

    @property
    def reg_rx_i_mask(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_i_mask_msb, self.__reg_rx_i_mask_lsb)
    @reg_rx_i_mask.setter
    def reg_rx_i_mask(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_i_mask_msb, self.__reg_rx_i_mask_lsb, value)
class FE2_RX_DC_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0xd8
        self.__reg_rx_most_bit_inv_lsb = 31
        self.__reg_rx_most_bit_inv_msb = 31
        self.__reg_rx_iq_swap_en_lsb = 30
        self.__reg_rx_iq_swap_en_msb = 30
        self.__reg_rx_q_inv_en_lsb = 29
        self.__reg_rx_q_inv_en_msb = 29
        self.__reg_rx_i_inv_en_lsb = 28
        self.__reg_rx_i_inv_en_msb = 28
        self.__reg_rx_edge_sel_lsb = 27
        self.__reg_rx_edge_sel_msb = 27
        self.__reg_tx_most_bit_inv_lsb = 26
        self.__reg_tx_most_bit_inv_msb = 26
        self.__reg_tx_iq_swap_en_lsb = 25
        self.__reg_tx_iq_swap_en_msb = 25
        self.__reg_tx_q_inv_en_lsb = 24
        self.__reg_tx_q_inv_en_msb = 24
        self.__reg_tx_i_inv_en_lsb = 23
        self.__reg_tx_i_inv_en_msb = 23
        self.__reg_tx_edge_sel_lsb = 22
        self.__reg_tx_edge_sel_msb = 22
        self.__reg_rx_q_dc_lsb = 11
        self.__reg_rx_q_dc_msb = 21
        self.__reg_rx_i_dc_lsb = 0
        self.__reg_rx_i_dc_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rx_most_bit_inv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_most_bit_inv_msb, self.__reg_rx_most_bit_inv_lsb)
    @reg_rx_most_bit_inv.setter
    def reg_rx_most_bit_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_most_bit_inv_msb, self.__reg_rx_most_bit_inv_lsb, value)

    @property
    def reg_rx_iq_swap_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_iq_swap_en_msb, self.__reg_rx_iq_swap_en_lsb)
    @reg_rx_iq_swap_en.setter
    def reg_rx_iq_swap_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_iq_swap_en_msb, self.__reg_rx_iq_swap_en_lsb, value)

    @property
    def reg_rx_q_inv_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_q_inv_en_msb, self.__reg_rx_q_inv_en_lsb)
    @reg_rx_q_inv_en.setter
    def reg_rx_q_inv_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_q_inv_en_msb, self.__reg_rx_q_inv_en_lsb, value)

    @property
    def reg_rx_i_inv_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_i_inv_en_msb, self.__reg_rx_i_inv_en_lsb)
    @reg_rx_i_inv_en.setter
    def reg_rx_i_inv_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_i_inv_en_msb, self.__reg_rx_i_inv_en_lsb, value)

    @property
    def reg_rx_edge_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_edge_sel_msb, self.__reg_rx_edge_sel_lsb)
    @reg_rx_edge_sel.setter
    def reg_rx_edge_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_edge_sel_msb, self.__reg_rx_edge_sel_lsb, value)

    @property
    def reg_tx_most_bit_inv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_most_bit_inv_msb, self.__reg_tx_most_bit_inv_lsb)
    @reg_tx_most_bit_inv.setter
    def reg_tx_most_bit_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_most_bit_inv_msb, self.__reg_tx_most_bit_inv_lsb, value)

    @property
    def reg_tx_iq_swap_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_iq_swap_en_msb, self.__reg_tx_iq_swap_en_lsb)
    @reg_tx_iq_swap_en.setter
    def reg_tx_iq_swap_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_iq_swap_en_msb, self.__reg_tx_iq_swap_en_lsb, value)

    @property
    def reg_tx_q_inv_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_q_inv_en_msb, self.__reg_tx_q_inv_en_lsb)
    @reg_tx_q_inv_en.setter
    def reg_tx_q_inv_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_q_inv_en_msb, self.__reg_tx_q_inv_en_lsb, value)

    @property
    def reg_tx_i_inv_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_i_inv_en_msb, self.__reg_tx_i_inv_en_lsb)
    @reg_tx_i_inv_en.setter
    def reg_tx_i_inv_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_i_inv_en_msb, self.__reg_tx_i_inv_en_lsb, value)

    @property
    def reg_tx_edge_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_edge_sel_msb, self.__reg_tx_edge_sel_lsb)
    @reg_tx_edge_sel.setter
    def reg_tx_edge_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_edge_sel_msb, self.__reg_tx_edge_sel_lsb, value)

    @property
    def reg_rx_q_dc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_q_dc_msb, self.__reg_rx_q_dc_lsb)
    @reg_rx_q_dc.setter
    def reg_rx_q_dc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_q_dc_msb, self.__reg_rx_q_dc_lsb, value)

    @property
    def reg_rx_i_dc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_i_dc_msb, self.__reg_rx_i_dc_lsb)
    @reg_rx_i_dc.setter
    def reg_rx_i_dc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_i_dc_msb, self.__reg_rx_i_dc_lsb, value)
class FE2_IQ_MIS_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0xdc
        self.__reg_clk_1_rx_sync_sel_lsb = 31
        self.__reg_clk_1_rx_sync_sel_msb = 31
        self.__reg_clk_2_rx_sync_sel_lsb = 30
        self.__reg_clk_2_rx_sync_sel_msb = 30
        self.__reg_rx_iqam_x2_lsb = 29
        self.__reg_rx_iqam_x2_msb = 29
        self.__reg_rx_iq_coff_sel_lsb = 28
        self.__reg_rx_iq_coff_sel_msb = 28
        self.__reg_rx_iqcorr_enable_lsb = 27
        self.__reg_rx_iqcorr_enable_msb = 27
        self.__reg_rx_q_i_coff_lsb = 21
        self.__reg_rx_q_i_coff_msb = 26
        self.__reg_rx_q_q_coff_lsb = 16
        self.__reg_rx_q_q_coff_msb = 20
        self.__reg_tx_clk_force_en_lsb = 15
        self.__reg_tx_clk_force_en_msb = 15
        self.__reg_rx_clk_force_en_lsb = 14
        self.__reg_rx_clk_force_en_msb = 14
        self.__reg_tx_iqam_x2_lsb = 13
        self.__reg_tx_iqam_x2_msb = 13
        self.__reg_tx_iq_coff_sel_lsb = 12
        self.__reg_tx_iq_coff_sel_msb = 12
        self.__reg_tx_iqcorr_enable_lsb = 11
        self.__reg_tx_iqcorr_enable_msb = 11
        self.__reg_tx_q_i_coff_lsb = 5
        self.__reg_tx_q_i_coff_msb = 10
        self.__reg_tx_q_q_coff_lsb = 0
        self.__reg_tx_q_q_coff_msb = 4
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_clk_1_rx_sync_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk_1_rx_sync_sel_msb, self.__reg_clk_1_rx_sync_sel_lsb)
    @reg_clk_1_rx_sync_sel.setter
    def reg_clk_1_rx_sync_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk_1_rx_sync_sel_msb, self.__reg_clk_1_rx_sync_sel_lsb, value)

    @property
    def reg_clk_2_rx_sync_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk_2_rx_sync_sel_msb, self.__reg_clk_2_rx_sync_sel_lsb)
    @reg_clk_2_rx_sync_sel.setter
    def reg_clk_2_rx_sync_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk_2_rx_sync_sel_msb, self.__reg_clk_2_rx_sync_sel_lsb, value)

    @property
    def reg_rx_iqam_x2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_iqam_x2_msb, self.__reg_rx_iqam_x2_lsb)
    @reg_rx_iqam_x2.setter
    def reg_rx_iqam_x2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_iqam_x2_msb, self.__reg_rx_iqam_x2_lsb, value)

    @property
    def reg_rx_iq_coff_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_iq_coff_sel_msb, self.__reg_rx_iq_coff_sel_lsb)
    @reg_rx_iq_coff_sel.setter
    def reg_rx_iq_coff_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_iq_coff_sel_msb, self.__reg_rx_iq_coff_sel_lsb, value)

    @property
    def reg_rx_iqcorr_enable(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_iqcorr_enable_msb, self.__reg_rx_iqcorr_enable_lsb)
    @reg_rx_iqcorr_enable.setter
    def reg_rx_iqcorr_enable(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_iqcorr_enable_msb, self.__reg_rx_iqcorr_enable_lsb, value)

    @property
    def reg_rx_q_i_coff(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_q_i_coff_msb, self.__reg_rx_q_i_coff_lsb)
    @reg_rx_q_i_coff.setter
    def reg_rx_q_i_coff(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_q_i_coff_msb, self.__reg_rx_q_i_coff_lsb, value)

    @property
    def reg_rx_q_q_coff(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_q_q_coff_msb, self.__reg_rx_q_q_coff_lsb)
    @reg_rx_q_q_coff.setter
    def reg_rx_q_q_coff(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_q_q_coff_msb, self.__reg_rx_q_q_coff_lsb, value)

    @property
    def reg_tx_clk_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_clk_force_en_msb, self.__reg_tx_clk_force_en_lsb)
    @reg_tx_clk_force_en.setter
    def reg_tx_clk_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_clk_force_en_msb, self.__reg_tx_clk_force_en_lsb, value)

    @property
    def reg_rx_clk_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_clk_force_en_msb, self.__reg_rx_clk_force_en_lsb)
    @reg_rx_clk_force_en.setter
    def reg_rx_clk_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_clk_force_en_msb, self.__reg_rx_clk_force_en_lsb, value)

    @property
    def reg_tx_iqam_x2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_iqam_x2_msb, self.__reg_tx_iqam_x2_lsb)
    @reg_tx_iqam_x2.setter
    def reg_tx_iqam_x2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_iqam_x2_msb, self.__reg_tx_iqam_x2_lsb, value)

    @property
    def reg_tx_iq_coff_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_iq_coff_sel_msb, self.__reg_tx_iq_coff_sel_lsb)
    @reg_tx_iq_coff_sel.setter
    def reg_tx_iq_coff_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_iq_coff_sel_msb, self.__reg_tx_iq_coff_sel_lsb, value)

    @property
    def reg_tx_iqcorr_enable(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_iqcorr_enable_msb, self.__reg_tx_iqcorr_enable_lsb)
    @reg_tx_iqcorr_enable.setter
    def reg_tx_iqcorr_enable(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_iqcorr_enable_msb, self.__reg_tx_iqcorr_enable_lsb, value)

    @property
    def reg_tx_q_i_coff(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_q_i_coff_msb, self.__reg_tx_q_i_coff_lsb)
    @reg_tx_q_i_coff.setter
    def reg_tx_q_i_coff(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_q_i_coff_msb, self.__reg_tx_q_i_coff_lsb, value)

    @property
    def reg_tx_q_q_coff(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_q_q_coff_msb, self.__reg_tx_q_q_coff_lsb)
    @reg_tx_q_q_coff.setter
    def reg_tx_q_q_coff(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_q_q_coff_msb, self.__reg_tx_q_q_coff_lsb, value)
class FE2_ADC_CAL_I(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0xe0
        self.__reg_adc_cal3_i_lsb = 24
        self.__reg_adc_cal3_i_msb = 31
        self.__reg_adc_cal2_i_lsb = 16
        self.__reg_adc_cal2_i_msb = 23
        self.__reg_adc_cal1_i_lsb = 8
        self.__reg_adc_cal1_i_msb = 15
        self.__reg_adc_cal0_i_lsb = 0
        self.__reg_adc_cal0_i_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_adc_cal3_i(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_cal3_i_msb, self.__reg_adc_cal3_i_lsb)
    @reg_adc_cal3_i.setter
    def reg_adc_cal3_i(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_cal3_i_msb, self.__reg_adc_cal3_i_lsb, value)

    @property
    def reg_adc_cal2_i(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_cal2_i_msb, self.__reg_adc_cal2_i_lsb)
    @reg_adc_cal2_i.setter
    def reg_adc_cal2_i(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_cal2_i_msb, self.__reg_adc_cal2_i_lsb, value)

    @property
    def reg_adc_cal1_i(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_cal1_i_msb, self.__reg_adc_cal1_i_lsb)
    @reg_adc_cal1_i.setter
    def reg_adc_cal1_i(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_cal1_i_msb, self.__reg_adc_cal1_i_lsb, value)

    @property
    def reg_adc_cal0_i(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_cal0_i_msb, self.__reg_adc_cal0_i_lsb)
    @reg_adc_cal0_i.setter
    def reg_adc_cal0_i(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_cal0_i_msb, self.__reg_adc_cal0_i_lsb, value)
class ADC_CAL_Q(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0xe4
        self.__reg_adc_cal3_q_lsb = 24
        self.__reg_adc_cal3_q_msb = 31
        self.__reg_adc_cal2_q_lsb = 16
        self.__reg_adc_cal2_q_msb = 23
        self.__reg_adc_cal1_q_lsb = 8
        self.__reg_adc_cal1_q_msb = 15
        self.__reg_adc_cal0_q_lsb = 0
        self.__reg_adc_cal0_q_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_adc_cal3_q(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_cal3_q_msb, self.__reg_adc_cal3_q_lsb)
    @reg_adc_cal3_q.setter
    def reg_adc_cal3_q(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_cal3_q_msb, self.__reg_adc_cal3_q_lsb, value)

    @property
    def reg_adc_cal2_q(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_cal2_q_msb, self.__reg_adc_cal2_q_lsb)
    @reg_adc_cal2_q.setter
    def reg_adc_cal2_q(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_cal2_q_msb, self.__reg_adc_cal2_q_lsb, value)

    @property
    def reg_adc_cal1_q(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_cal1_q_msb, self.__reg_adc_cal1_q_lsb)
    @reg_adc_cal1_q.setter
    def reg_adc_cal1_q(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_cal1_q_msb, self.__reg_adc_cal1_q_lsb, value)

    @property
    def reg_adc_cal0_q(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_cal0_q_msb, self.__reg_adc_cal0_q_lsb)
    @reg_adc_cal0_q.setter
    def reg_adc_cal0_q(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_cal0_q_msb, self.__reg_adc_cal0_q_lsb, value)
class FE2_SCALE_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0xe8
        self.__reg_cal_sel3_q_lsb = 31
        self.__reg_cal_sel3_q_msb = 31
        self.__reg_cal_sel2_q_lsb = 30
        self.__reg_cal_sel2_q_msb = 30
        self.__reg_cal_sel1_q_lsb = 29
        self.__reg_cal_sel1_q_msb = 29
        self.__reg_cal_sel0_q_lsb = 28
        self.__reg_cal_sel0_q_msb = 28
        self.__reg_cal_sel3_i_lsb = 27
        self.__reg_cal_sel3_i_msb = 27
        self.__reg_cal_sel2_i_lsb = 26
        self.__reg_cal_sel2_i_msb = 26
        self.__reg_cal_sel1_i_lsb = 25
        self.__reg_cal_sel1_i_msb = 25
        self.__reg_cal_sel0_i_lsb = 24
        self.__reg_cal_sel0_i_msb = 24
        self.__reg_rx_scale_lsb = 16
        self.__reg_rx_scale_msb = 23
        self.__reg_tx_scale_lsb = 8
        self.__reg_tx_scale_msb = 15
        self.__reg_dpd_scale_lsb = 0
        self.__reg_dpd_scale_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_cal_sel3_q(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cal_sel3_q_msb, self.__reg_cal_sel3_q_lsb)
    @reg_cal_sel3_q.setter
    def reg_cal_sel3_q(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cal_sel3_q_msb, self.__reg_cal_sel3_q_lsb, value)

    @property
    def reg_cal_sel2_q(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cal_sel2_q_msb, self.__reg_cal_sel2_q_lsb)
    @reg_cal_sel2_q.setter
    def reg_cal_sel2_q(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cal_sel2_q_msb, self.__reg_cal_sel2_q_lsb, value)

    @property
    def reg_cal_sel1_q(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cal_sel1_q_msb, self.__reg_cal_sel1_q_lsb)
    @reg_cal_sel1_q.setter
    def reg_cal_sel1_q(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cal_sel1_q_msb, self.__reg_cal_sel1_q_lsb, value)

    @property
    def reg_cal_sel0_q(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cal_sel0_q_msb, self.__reg_cal_sel0_q_lsb)
    @reg_cal_sel0_q.setter
    def reg_cal_sel0_q(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cal_sel0_q_msb, self.__reg_cal_sel0_q_lsb, value)

    @property
    def reg_cal_sel3_i(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cal_sel3_i_msb, self.__reg_cal_sel3_i_lsb)
    @reg_cal_sel3_i.setter
    def reg_cal_sel3_i(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cal_sel3_i_msb, self.__reg_cal_sel3_i_lsb, value)

    @property
    def reg_cal_sel2_i(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cal_sel2_i_msb, self.__reg_cal_sel2_i_lsb)
    @reg_cal_sel2_i.setter
    def reg_cal_sel2_i(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cal_sel2_i_msb, self.__reg_cal_sel2_i_lsb, value)

    @property
    def reg_cal_sel1_i(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cal_sel1_i_msb, self.__reg_cal_sel1_i_lsb)
    @reg_cal_sel1_i.setter
    def reg_cal_sel1_i(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cal_sel1_i_msb, self.__reg_cal_sel1_i_lsb, value)

    @property
    def reg_cal_sel0_i(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cal_sel0_i_msb, self.__reg_cal_sel0_i_lsb)
    @reg_cal_sel0_i.setter
    def reg_cal_sel0_i(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cal_sel0_i_msb, self.__reg_cal_sel0_i_lsb, value)

    @property
    def reg_rx_scale(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_scale_msb, self.__reg_rx_scale_lsb)
    @reg_rx_scale.setter
    def reg_rx_scale(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_scale_msb, self.__reg_rx_scale_lsb, value)

    @property
    def reg_tx_scale(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_scale_msb, self.__reg_tx_scale_lsb)
    @reg_tx_scale.setter
    def reg_tx_scale(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_scale_msb, self.__reg_tx_scale_lsb, value)

    @property
    def reg_dpd_scale(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dpd_scale_msb, self.__reg_dpd_scale_lsb)
    @reg_dpd_scale.setter
    def reg_dpd_scale(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dpd_scale_msb, self.__reg_dpd_scale_lsb, value)
class FE2_TX_TONE_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0xec
        self.__reg_wait_dac_mode_lsb = 31
        self.__reg_wait_dac_mode_msb = 31
        self.__reg_tx_sync_sel_lsb = 30
        self.__reg_tx_sync_sel_msb = 30
        self.__reg_rx_phase_det_cont_en_lsb = 29
        self.__reg_rx_phase_det_cont_en_msb = 29
        self.__reg_adc_160m_dsp_lsb = 28
        self.__reg_adc_160m_dsp_msb = 28
        self.__reg_dac_320m_enable_lsb = 27
        self.__reg_dac_320m_enable_msb = 27
        self.__reg_rst_rx_n_lsb = 26
        self.__reg_rst_rx_n_msb = 26
        self.__reg_rst_tx_n_lsb = 25
        self.__reg_rst_tx_n_msb = 25
        self.__reg_rst_pll_n_lsb = 24
        self.__reg_rst_pll_n_msb = 24
        self.__reg_tx_tone_start_lsb = 23
        self.__reg_tx_tone_start_msb = 23
        self.__reg_cw_gen_sel_lsb = 22
        self.__reg_cw_gen_sel_msb = 22
        self.__reg_inf_tone_sel_lsb = 20
        self.__reg_inf_tone_sel_msb = 21
        self.__reg_inf_phase_cfg_lsb = 17
        self.__reg_inf_phase_cfg_msb = 19
        self.__reg_inf_dis_phase_lsb = 16
        self.__reg_inf_dis_phase_msb = 16
        self.__reg_inf_inv_lsb = 12
        self.__reg_inf_inv_msb = 15
        self.__reg_inf_fstep_lsb = 0
        self.__reg_inf_fstep_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wait_dac_mode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wait_dac_mode_msb, self.__reg_wait_dac_mode_lsb)
    @reg_wait_dac_mode.setter
    def reg_wait_dac_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wait_dac_mode_msb, self.__reg_wait_dac_mode_lsb, value)

    @property
    def reg_tx_sync_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_sync_sel_msb, self.__reg_tx_sync_sel_lsb)
    @reg_tx_sync_sel.setter
    def reg_tx_sync_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_sync_sel_msb, self.__reg_tx_sync_sel_lsb, value)

    @property
    def reg_rx_phase_det_cont_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_phase_det_cont_en_msb, self.__reg_rx_phase_det_cont_en_lsb)
    @reg_rx_phase_det_cont_en.setter
    def reg_rx_phase_det_cont_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_phase_det_cont_en_msb, self.__reg_rx_phase_det_cont_en_lsb, value)

    @property
    def reg_adc_160m_dsp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_160m_dsp_msb, self.__reg_adc_160m_dsp_lsb)
    @reg_adc_160m_dsp.setter
    def reg_adc_160m_dsp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_160m_dsp_msb, self.__reg_adc_160m_dsp_lsb, value)

    @property
    def reg_dac_320m_enable(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dac_320m_enable_msb, self.__reg_dac_320m_enable_lsb)
    @reg_dac_320m_enable.setter
    def reg_dac_320m_enable(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dac_320m_enable_msb, self.__reg_dac_320m_enable_lsb, value)

    @property
    def reg_rst_rx_n(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rst_rx_n_msb, self.__reg_rst_rx_n_lsb)
    @reg_rst_rx_n.setter
    def reg_rst_rx_n(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rst_rx_n_msb, self.__reg_rst_rx_n_lsb, value)

    @property
    def reg_rst_tx_n(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rst_tx_n_msb, self.__reg_rst_tx_n_lsb)
    @reg_rst_tx_n.setter
    def reg_rst_tx_n(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rst_tx_n_msb, self.__reg_rst_tx_n_lsb, value)

    @property
    def reg_rst_pll_n(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rst_pll_n_msb, self.__reg_rst_pll_n_lsb)
    @reg_rst_pll_n.setter
    def reg_rst_pll_n(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rst_pll_n_msb, self.__reg_rst_pll_n_lsb, value)

    @property
    def reg_tx_tone_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_tone_start_msb, self.__reg_tx_tone_start_lsb)
    @reg_tx_tone_start.setter
    def reg_tx_tone_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_tone_start_msb, self.__reg_tx_tone_start_lsb, value)

    @property
    def reg_cw_gen_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cw_gen_sel_msb, self.__reg_cw_gen_sel_lsb)
    @reg_cw_gen_sel.setter
    def reg_cw_gen_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cw_gen_sel_msb, self.__reg_cw_gen_sel_lsb, value)

    @property
    def reg_inf_tone_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inf_tone_sel_msb, self.__reg_inf_tone_sel_lsb)
    @reg_inf_tone_sel.setter
    def reg_inf_tone_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inf_tone_sel_msb, self.__reg_inf_tone_sel_lsb, value)

    @property
    def reg_inf_phase_cfg(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inf_phase_cfg_msb, self.__reg_inf_phase_cfg_lsb)
    @reg_inf_phase_cfg.setter
    def reg_inf_phase_cfg(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inf_phase_cfg_msb, self.__reg_inf_phase_cfg_lsb, value)

    @property
    def reg_inf_dis_phase(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inf_dis_phase_msb, self.__reg_inf_dis_phase_lsb)
    @reg_inf_dis_phase.setter
    def reg_inf_dis_phase(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inf_dis_phase_msb, self.__reg_inf_dis_phase_lsb, value)

    @property
    def reg_inf_inv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inf_inv_msb, self.__reg_inf_inv_lsb)
    @reg_inf_inv.setter
    def reg_inf_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inf_inv_msb, self.__reg_inf_inv_lsb, value)

    @property
    def reg_inf_fstep(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inf_fstep_msb, self.__reg_inf_fstep_lsb)
    @reg_inf_fstep.setter
    def reg_inf_fstep(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inf_fstep_msb, self.__reg_inf_fstep_lsb, value)
class FE2_TX_INTERP_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0xf0
        self.__reg_tx_inf_force_pu_lsb = 10
        self.__reg_tx_inf_force_pu_msb = 10
        self.__reg_tx_inf_force_pd_lsb = 9
        self.__reg_tx_inf_force_pd_msb = 9
        self.__reg_tx_interp_delay_lsb = 0
        self.__reg_tx_interp_delay_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_inf_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_inf_force_pu_msb, self.__reg_tx_inf_force_pu_lsb)
    @reg_tx_inf_force_pu.setter
    def reg_tx_inf_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_inf_force_pu_msb, self.__reg_tx_inf_force_pu_lsb, value)

    @property
    def reg_tx_inf_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_inf_force_pd_msb, self.__reg_tx_inf_force_pd_lsb)
    @reg_tx_inf_force_pd.setter
    def reg_tx_inf_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_inf_force_pd_msb, self.__reg_tx_inf_force_pd_lsb, value)

    @property
    def reg_tx_interp_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_interp_delay_msb, self.__reg_tx_interp_delay_lsb)
    @reg_tx_interp_delay.setter
    def reg_tx_interp_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_interp_delay_msb, self.__reg_tx_interp_delay_lsb, value)
class FE_RX_SCALE(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0xf4
        self.__reg_fe_rx_in_160m_lsb = 10
        self.__reg_fe_rx_in_160m_msb = 10
        self.__reg_fe_rx_in_80m_lsb = 9
        self.__reg_fe_rx_in_80m_msb = 9
        self.__reg_fe_rx_scale_en_lsb = 8
        self.__reg_fe_rx_scale_en_msb = 8
        self.__reg_fe_rx_scale_db_lsb = 0
        self.__reg_fe_rx_scale_db_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_fe_rx_in_160m(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fe_rx_in_160m_msb, self.__reg_fe_rx_in_160m_lsb)
    @reg_fe_rx_in_160m.setter
    def reg_fe_rx_in_160m(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fe_rx_in_160m_msb, self.__reg_fe_rx_in_160m_lsb, value)

    @property
    def reg_fe_rx_in_80m(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fe_rx_in_80m_msb, self.__reg_fe_rx_in_80m_lsb)
    @reg_fe_rx_in_80m.setter
    def reg_fe_rx_in_80m(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fe_rx_in_80m_msb, self.__reg_fe_rx_in_80m_lsb, value)

    @property
    def reg_fe_rx_scale_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fe_rx_scale_en_msb, self.__reg_fe_rx_scale_en_lsb)
    @reg_fe_rx_scale_en.setter
    def reg_fe_rx_scale_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fe_rx_scale_en_msb, self.__reg_fe_rx_scale_en_lsb, value)

    @property
    def reg_fe_rx_scale_db(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fe_rx_scale_db_msb, self.__reg_fe_rx_scale_db_lsb)
    @reg_fe_rx_scale_db.setter
    def reg_fe_rx_scale_db(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fe_rx_scale_db_msb, self.__reg_fe_rx_scale_db_lsb, value)
class FE2_NOUSE(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0xf8
        self.__reg_fe2_nouse_lsb = 0
        self.__reg_fe2_nouse_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_fe2_nouse(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fe2_nouse_msb, self.__reg_fe2_nouse_lsb)
    @reg_fe2_nouse.setter
    def reg_fe2_nouse(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fe2_nouse_msb, self.__reg_fe2_nouse_lsb, value)
class FE2_DPD_CFG1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x100
        self.__reg_dpd_comp_sel_lsb = 30
        self.__reg_dpd_comp_sel_msb = 30
        self.__reg_dpd_gain_sat_lsb = 20
        self.__reg_dpd_gain_sat_msb = 29
        self.__reg_dpd_interp_shift_lsb = 16
        self.__reg_dpd_interp_shift_msb = 19
        self.__reg_dpd_interp_mult_lsb = 8
        self.__reg_dpd_interp_mult_msb = 15
        self.__reg_dpd_index1_lsb = 0
        self.__reg_dpd_index1_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_dpd_comp_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dpd_comp_sel_msb, self.__reg_dpd_comp_sel_lsb)
    @reg_dpd_comp_sel.setter
    def reg_dpd_comp_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dpd_comp_sel_msb, self.__reg_dpd_comp_sel_lsb, value)

    @property
    def reg_dpd_gain_sat(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dpd_gain_sat_msb, self.__reg_dpd_gain_sat_lsb)
    @reg_dpd_gain_sat.setter
    def reg_dpd_gain_sat(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dpd_gain_sat_msb, self.__reg_dpd_gain_sat_lsb, value)

    @property
    def reg_dpd_interp_shift(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dpd_interp_shift_msb, self.__reg_dpd_interp_shift_lsb)
    @reg_dpd_interp_shift.setter
    def reg_dpd_interp_shift(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dpd_interp_shift_msb, self.__reg_dpd_interp_shift_lsb, value)

    @property
    def reg_dpd_interp_mult(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dpd_interp_mult_msb, self.__reg_dpd_interp_mult_lsb)
    @reg_dpd_interp_mult.setter
    def reg_dpd_interp_mult(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dpd_interp_mult_msb, self.__reg_dpd_interp_mult_lsb, value)

    @property
    def reg_dpd_index1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dpd_index1_msb, self.__reg_dpd_index1_lsb)
    @reg_dpd_index1.setter
    def reg_dpd_index1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dpd_index1_msb, self.__reg_dpd_index1_lsb, value)
class FE2_ANT_CTRL0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x104
        self.__reg_ant_cfg3_lsb = 24
        self.__reg_ant_cfg3_msb = 31
        self.__reg_ant_cfg2_lsb = 16
        self.__reg_ant_cfg2_msb = 23
        self.__reg_ant_cfg1_lsb = 8
        self.__reg_ant_cfg1_msb = 15
        self.__reg_ant_cfg0_lsb = 0
        self.__reg_ant_cfg0_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ant_cfg3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ant_cfg3_msb, self.__reg_ant_cfg3_lsb)
    @reg_ant_cfg3.setter
    def reg_ant_cfg3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ant_cfg3_msb, self.__reg_ant_cfg3_lsb, value)

    @property
    def reg_ant_cfg2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ant_cfg2_msb, self.__reg_ant_cfg2_lsb)
    @reg_ant_cfg2.setter
    def reg_ant_cfg2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ant_cfg2_msb, self.__reg_ant_cfg2_lsb, value)

    @property
    def reg_ant_cfg1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ant_cfg1_msb, self.__reg_ant_cfg1_lsb)
    @reg_ant_cfg1.setter
    def reg_ant_cfg1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ant_cfg1_msb, self.__reg_ant_cfg1_lsb, value)

    @property
    def reg_ant_cfg0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ant_cfg0_msb, self.__reg_ant_cfg0_lsb)
    @reg_ant_cfg0.setter
    def reg_ant_cfg0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ant_cfg0_msb, self.__reg_ant_cfg0_lsb, value)
class FE2_ANT_CTRL1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x108
        self.__reg_ant_cfg7_lsb = 24
        self.__reg_ant_cfg7_msb = 31
        self.__reg_ant_cfg6_lsb = 16
        self.__reg_ant_cfg6_msb = 23
        self.__reg_ant_cfg5_lsb = 8
        self.__reg_ant_cfg5_msb = 15
        self.__reg_ant_cfg4_lsb = 0
        self.__reg_ant_cfg4_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ant_cfg7(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ant_cfg7_msb, self.__reg_ant_cfg7_lsb)
    @reg_ant_cfg7.setter
    def reg_ant_cfg7(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ant_cfg7_msb, self.__reg_ant_cfg7_lsb, value)

    @property
    def reg_ant_cfg6(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ant_cfg6_msb, self.__reg_ant_cfg6_lsb)
    @reg_ant_cfg6.setter
    def reg_ant_cfg6(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ant_cfg6_msb, self.__reg_ant_cfg6_lsb, value)

    @property
    def reg_ant_cfg5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ant_cfg5_msb, self.__reg_ant_cfg5_lsb)
    @reg_ant_cfg5.setter
    def reg_ant_cfg5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ant_cfg5_msb, self.__reg_ant_cfg5_lsb, value)

    @property
    def reg_ant_cfg4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ant_cfg4_msb, self.__reg_ant_cfg4_lsb)
    @reg_ant_cfg4.setter
    def reg_ant_cfg4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ant_cfg4_msb, self.__reg_ant_cfg4_lsb, value)
class FE2_ANT_CTRL2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x10c
        self.__reg_ant_cfg11_lsb = 24
        self.__reg_ant_cfg11_msb = 31
        self.__reg_ant_cfg10_lsb = 16
        self.__reg_ant_cfg10_msb = 23
        self.__reg_ant_cfg9_lsb = 8
        self.__reg_ant_cfg9_msb = 15
        self.__reg_ant_cfg8_lsb = 0
        self.__reg_ant_cfg8_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ant_cfg11(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ant_cfg11_msb, self.__reg_ant_cfg11_lsb)
    @reg_ant_cfg11.setter
    def reg_ant_cfg11(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ant_cfg11_msb, self.__reg_ant_cfg11_lsb, value)

    @property
    def reg_ant_cfg10(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ant_cfg10_msb, self.__reg_ant_cfg10_lsb)
    @reg_ant_cfg10.setter
    def reg_ant_cfg10(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ant_cfg10_msb, self.__reg_ant_cfg10_lsb, value)

    @property
    def reg_ant_cfg9(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ant_cfg9_msb, self.__reg_ant_cfg9_lsb)
    @reg_ant_cfg9.setter
    def reg_ant_cfg9(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ant_cfg9_msb, self.__reg_ant_cfg9_lsb, value)

    @property
    def reg_ant_cfg8(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ant_cfg8_msb, self.__reg_ant_cfg8_lsb)
    @reg_ant_cfg8.setter
    def reg_ant_cfg8(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ant_cfg8_msb, self.__reg_ant_cfg8_lsb, value)
class FE2_ANT_CTRL3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x110
        self.__reg_ant_cfg_force_en_lsb = 16
        self.__reg_ant_cfg_force_en_msb = 16
        self.__reg_ant_cfg_force_lsb = 8
        self.__reg_ant_cfg_force_msb = 15
        self.__reg_ant_cfg12_lsb = 0
        self.__reg_ant_cfg12_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_ant_cfg_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ant_cfg_force_en_msb, self.__reg_ant_cfg_force_en_lsb)
    @reg_ant_cfg_force_en.setter
    def reg_ant_cfg_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ant_cfg_force_en_msb, self.__reg_ant_cfg_force_en_lsb, value)

    @property
    def reg_ant_cfg_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ant_cfg_force_msb, self.__reg_ant_cfg_force_lsb)
    @reg_ant_cfg_force.setter
    def reg_ant_cfg_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ant_cfg_force_msb, self.__reg_ant_cfg_force_lsb, value)

    @property
    def reg_ant_cfg12(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ant_cfg12_msb, self.__reg_ant_cfg12_lsb)
    @reg_ant_cfg12.setter
    def reg_ant_cfg12(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ant_cfg12_msb, self.__reg_ant_cfg12_lsb, value)
class FE_RX_SYN3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x114
        self.__way3_sel_lsb = 30
        self.__way3_sel_msb = 31
        self.__way3_det_suc_lsb = 29
        self.__way3_det_suc_msb = 29
        self.__way3_det_done_lsb = 28
        self.__way3_det_done_msb = 28
        self.__adc_smp_pha_i_sw_lsb = 19
        self.__adc_smp_pha_i_sw_msb = 27
        self.__adc_smp_pha_q_sw_lsb = 10
        self.__adc_smp_pha_q_sw_msb = 18
        self.__reg_rx_way3_en_lsb = 9
        self.__reg_rx_way3_en_msb = 9
        self.__reg_rx_way3_sel_f_en_lsb = 8
        self.__reg_rx_way3_sel_f_en_msb = 8
        self.__reg_rx_way3_sel_f_lsb = 6
        self.__reg_rx_way3_sel_f_msb = 7
        self.__reg_rx_way3_cnt_init_lsb = 1
        self.__reg_rx_way3_cnt_init_msb = 5
        self.__reg_rx_way3_det_en_lsb = 0
        self.__reg_rx_way3_det_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def way3_sel(self):
        return self.__MEM.rdm(self.__addr, self.__way3_sel_msb, self.__way3_sel_lsb)
    @way3_sel.setter
    def way3_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__way3_sel_msb, self.__way3_sel_lsb, value)

    @property
    def way3_det_suc(self):
        return self.__MEM.rdm(self.__addr, self.__way3_det_suc_msb, self.__way3_det_suc_lsb)
    @way3_det_suc.setter
    def way3_det_suc(self, value):
        return self.__MEM.wrm(self.__addr, self.__way3_det_suc_msb, self.__way3_det_suc_lsb, value)

    @property
    def way3_det_done(self):
        return self.__MEM.rdm(self.__addr, self.__way3_det_done_msb, self.__way3_det_done_lsb)
    @way3_det_done.setter
    def way3_det_done(self, value):
        return self.__MEM.wrm(self.__addr, self.__way3_det_done_msb, self.__way3_det_done_lsb, value)

    @property
    def adc_smp_pha_i_sw(self):
        return self.__MEM.rdm(self.__addr, self.__adc_smp_pha_i_sw_msb, self.__adc_smp_pha_i_sw_lsb)
    @adc_smp_pha_i_sw.setter
    def adc_smp_pha_i_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__adc_smp_pha_i_sw_msb, self.__adc_smp_pha_i_sw_lsb, value)

    @property
    def adc_smp_pha_q_sw(self):
        return self.__MEM.rdm(self.__addr, self.__adc_smp_pha_q_sw_msb, self.__adc_smp_pha_q_sw_lsb)
    @adc_smp_pha_q_sw.setter
    def adc_smp_pha_q_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__adc_smp_pha_q_sw_msb, self.__adc_smp_pha_q_sw_lsb, value)

    @property
    def reg_rx_way3_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_way3_en_msb, self.__reg_rx_way3_en_lsb)
    @reg_rx_way3_en.setter
    def reg_rx_way3_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_way3_en_msb, self.__reg_rx_way3_en_lsb, value)

    @property
    def reg_rx_way3_sel_f_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_way3_sel_f_en_msb, self.__reg_rx_way3_sel_f_en_lsb)
    @reg_rx_way3_sel_f_en.setter
    def reg_rx_way3_sel_f_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_way3_sel_f_en_msb, self.__reg_rx_way3_sel_f_en_lsb, value)

    @property
    def reg_rx_way3_sel_f(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_way3_sel_f_msb, self.__reg_rx_way3_sel_f_lsb)
    @reg_rx_way3_sel_f.setter
    def reg_rx_way3_sel_f(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_way3_sel_f_msb, self.__reg_rx_way3_sel_f_lsb, value)

    @property
    def reg_rx_way3_cnt_init(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_way3_cnt_init_msb, self.__reg_rx_way3_cnt_init_lsb)
    @reg_rx_way3_cnt_init.setter
    def reg_rx_way3_cnt_init(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_way3_cnt_init_msb, self.__reg_rx_way3_cnt_init_lsb, value)

    @property
    def reg_rx_way3_det_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_way3_det_en_msb, self.__reg_rx_way3_det_en_lsb)
    @reg_rx_way3_det_en.setter
    def reg_rx_way3_det_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_way3_det_en_msb, self.__reg_rx_way3_det_en_lsb, value)
class FE_RX_SYN3_2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x118
        self.__reg_way3_det_iq_inv_lsb = 1
        self.__reg_way3_det_iq_inv_msb = 1
        self.__reg_way3_det_cont_en_lsb = 0
        self.__reg_way3_det_cont_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_way3_det_iq_inv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_way3_det_iq_inv_msb, self.__reg_way3_det_iq_inv_lsb)
    @reg_way3_det_iq_inv.setter
    def reg_way3_det_iq_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_way3_det_iq_inv_msb, self.__reg_way3_det_iq_inv_lsb, value)

    @property
    def reg_way3_det_cont_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_way3_det_cont_en_msb, self.__reg_way3_det_cont_en_lsb)
    @reg_way3_det_cont_en.setter
    def reg_way3_det_cont_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_way3_det_cont_en_msb, self.__reg_way3_det_cont_en_lsb, value)
class FE2_NOUSE_2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE2_BASE + 0x1fc
        self.__reg_fe2_clk_en_lsb = 28
        self.__reg_fe2_clk_en_msb = 28
        self.__reg_fe2_date_lsb = 0
        self.__reg_fe2_date_msb = 27
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_fe2_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fe2_clk_en_msb, self.__reg_fe2_clk_en_lsb)
    @reg_fe2_clk_en.setter
    def reg_fe2_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fe2_clk_en_msb, self.__reg_fe2_clk_en_lsb, value)

    @property
    def reg_fe2_date(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fe2_date_msb, self.__reg_fe2_date_lsb)
    @reg_fe2_date.setter
    def reg_fe2_date(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fe2_date_msb, self.__reg_fe2_date_lsb, value)
    @property
    def default_value(self):
        return 0x1605181
