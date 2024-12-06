from hal.common import *
from hal.hwregister.hwreg.ESP32.addr_base import *
class FE(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.FE_TX_GAIN_CTRL = FE_TX_GAIN_CTRL(self.channel, self.chipv)
        self.FE_TX_GAIN_CTRL_1 = FE_TX_GAIN_CTRL_1(self.channel, self.chipv)
        self.FE_TX_GAIN_CTRL_2 = FE_TX_GAIN_CTRL_2(self.channel, self.chipv)
        self.FE_TX_GAIN_CTRL_3 = FE_TX_GAIN_CTRL_3(self.channel, self.chipv)
        self.FE_TX_GAIN_CTRL_4 = FE_TX_GAIN_CTRL_4(self.channel, self.chipv)
        self.FE_PUBS_CFG0 = FE_PUBS_CFG0(self.channel, self.chipv)
        self.FE_PUBS_CFG1 = FE_PUBS_CFG1(self.channel, self.chipv)
        self.FE_PUBS_CFG2 = FE_PUBS_CFG2(self.channel, self.chipv)
        self.FE_PUBS_CFG3 = FE_PUBS_CFG3(self.channel, self.chipv)
        self.FE_PUBS_CFG4 = FE_PUBS_CFG4(self.channel, self.chipv)
        self.FE_PUBS_CFG5 = FE_PUBS_CFG5(self.channel, self.chipv)
        self.FE_PUBS_CFG6 = FE_PUBS_CFG6(self.channel, self.chipv)
        self.FE_PUBS_CFG7 = FE_PUBS_CFG7(self.channel, self.chipv)
        self.FE_PUBS_CFG8 = FE_PUBS_CFG8(self.channel, self.chipv)
        self.FE_IQ_EST_CTRL_01 = FE_IQ_EST_CTRL_01(self.channel, self.chipv)
        self.FE_IQ_SSEA_CORR1 = FE_IQ_SSEA_CORR1(self.channel, self.chipv)
        self.FE_IQ_SSEA_CORR1_CONJ = FE_IQ_SSEA_CORR1_CONJ(self.channel, self.chipv)
        self.FE_IQ_SSEA_CORR2 = FE_IQ_SSEA_CORR2(self.channel, self.chipv)
        self.FE_IQ_SSEA_CORR2_CONJ = FE_IQ_SSEA_CORR2_CONJ(self.channel, self.chipv)
        self.FE_IQ_SSEA_DC = FE_IQ_SSEA_DC(self.channel, self.chipv)
        self.FE_IQ_SSEA_POWER = FE_IQ_SSEA_POWER(self.channel, self.chipv)
        self.FE_IQ_EST_CTRL_00 = FE_IQ_EST_CTRL_00(self.channel, self.chipv)
        self.FE_IQ_RESULT1 = FE_IQ_RESULT1(self.channel, self.chipv)
        self.FE_IQ_RESULT2 = FE_IQ_RESULT2(self.channel, self.chipv)
        self.FE_IQ_RESULT3 = FE_IQ_RESULT3(self.channel, self.chipv)
        self.FE_IQ_RESULT4 = FE_IQ_RESULT4(self.channel, self.chipv)
        self.FE_GEN_CTRL = FE_GEN_CTRL(self.channel, self.chipv)
        self.FE_PUBS_CTRL0 = FE_PUBS_CTRL0(self.channel, self.chipv)
        self.FE_PUBS_CTRL2 = FE_PUBS_CTRL2(self.channel, self.chipv)
        self.FE_PUBS_CTRL3 = FE_PUBS_CTRL3(self.channel, self.chipv)
        self.FE_PUBS_RD0 = FE_PUBS_RD0(self.channel, self.chipv)
        self.FE_PUBS_RD1 = FE_PUBS_RD1(self.channel, self.chipv)
        self.FE_PUBS_RD2 = FE_PUBS_RD2(self.channel, self.chipv)
        self.FE_PUBS_RD3 = FE_PUBS_RD3(self.channel, self.chipv)
        self.FE_PUBS_RD4 = FE_PUBS_RD4(self.channel, self.chipv)
        self.FE_TX_TEST_CTRL_0 = FE_TX_TEST_CTRL_0(self.channel, self.chipv)
        self.FE_TX_TEST_CTRL_1 = FE_TX_TEST_CTRL_1(self.channel, self.chipv)
        self.FE_TX_TEST_CTRL_2 = FE_TX_TEST_CTRL_2(self.channel, self.chipv)
        self.FE_TX_TEST_CTRL_3 = FE_TX_TEST_CTRL_3(self.channel, self.chipv)
        self.FE_IQ_RESULT_2_1 = FE_IQ_RESULT_2_1(self.channel, self.chipv)
        self.FE_IQ_RESULT_2_2 = FE_IQ_RESULT_2_2(self.channel, self.chipv)
        self.FE_IQ_RESULT_2_3 = FE_IQ_RESULT_2_3(self.channel, self.chipv)
        self.FE_IQ_RESULT_2_4 = FE_IQ_RESULT_2_4(self.channel, self.chipv)
        self.FE_IQ_RESULT_DC_I = FE_IQ_RESULT_DC_I(self.channel, self.chipv)
        self.FE_IQ_RESULT_DC_Q = FE_IQ_RESULT_DC_Q(self.channel, self.chipv)
        self.FE_IQ_RESULT_PWR = FE_IQ_RESULT_PWR(self.channel, self.chipv)
        self.FE_IQ_RESULT_PWR_I = FE_IQ_RESULT_PWR_I(self.channel, self.chipv)
        self.FE_IQ_RESULT_PWR_Q = FE_IQ_RESULT_PWR_Q(self.channel, self.chipv)
        self.FE_IQ_RESULT_PWR_IQ = FE_IQ_RESULT_PWR_IQ(self.channel, self.chipv)
        self.FE_NOUSE = FE_NOUSE(self.channel, self.chipv)
        self.FE_NOUSE_2 = FE_NOUSE_2(self.channel, self.chipv)
class FE_TX_GAIN_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x0
        self.__reg_txgain_addr_base_lsb = 18
        self.__reg_txgain_addr_base_msb = 25
        self.__reg_force_txgain_addr_lsb = 10
        self.__reg_force_txgain_addr_msb = 17
        self.__reg_force_dac_gain_lsb = 2
        self.__reg_force_dac_gain_msb = 9
        self.__reg_force_txgain_addr_en_lsb = 1
        self.__reg_force_txgain_addr_en_msb = 1
        self.__reg_force_dac_gain_en_lsb = 0
        self.__reg_force_dac_gain_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txgain_addr_base(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txgain_addr_base_msb, self.__reg_txgain_addr_base_lsb)
    @reg_txgain_addr_base.setter
    def reg_txgain_addr_base(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txgain_addr_base_msb, self.__reg_txgain_addr_base_lsb, value)

    @property
    def reg_force_txgain_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_force_txgain_addr_msb, self.__reg_force_txgain_addr_lsb)
    @reg_force_txgain_addr.setter
    def reg_force_txgain_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_force_txgain_addr_msb, self.__reg_force_txgain_addr_lsb, value)

    @property
    def reg_force_dac_gain(self):
        return self.__MEM.rdm(self.__addr, self.__reg_force_dac_gain_msb, self.__reg_force_dac_gain_lsb)
    @reg_force_dac_gain.setter
    def reg_force_dac_gain(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_force_dac_gain_msb, self.__reg_force_dac_gain_lsb, value)

    @property
    def reg_force_txgain_addr_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_force_txgain_addr_en_msb, self.__reg_force_txgain_addr_en_lsb)
    @reg_force_txgain_addr_en.setter
    def reg_force_txgain_addr_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_force_txgain_addr_en_msb, self.__reg_force_txgain_addr_en_lsb, value)

    @property
    def reg_force_dac_gain_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_force_dac_gain_en_msb, self.__reg_force_dac_gain_en_lsb)
    @reg_force_dac_gain_en.setter
    def reg_force_dac_gain_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_force_dac_gain_en_msb, self.__reg_force_dac_gain_en_lsb, value)
class FE_TX_GAIN_CTRL_1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x4
        self.__reg_tx_gain_ctrl1_lsb = 0
        self.__reg_tx_gain_ctrl1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_gain_ctrl1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_gain_ctrl1_msb, self.__reg_tx_gain_ctrl1_lsb)
    @reg_tx_gain_ctrl1.setter
    def reg_tx_gain_ctrl1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_gain_ctrl1_msb, self.__reg_tx_gain_ctrl1_lsb, value)
class FE_TX_GAIN_CTRL_2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x8
        self.__reg_tx_gain_ctrl2_lsb = 0
        self.__reg_tx_gain_ctrl2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_gain_ctrl2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_gain_ctrl2_msb, self.__reg_tx_gain_ctrl2_lsb)
    @reg_tx_gain_ctrl2.setter
    def reg_tx_gain_ctrl2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_gain_ctrl2_msb, self.__reg_tx_gain_ctrl2_lsb, value)
class FE_TX_GAIN_CTRL_3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0xc
        self.__reg_tx_gain_ctrl3_lsb = 0
        self.__reg_tx_gain_ctrl3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_gain_ctrl3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_gain_ctrl3_msb, self.__reg_tx_gain_ctrl3_lsb)
    @reg_tx_gain_ctrl3.setter
    def reg_tx_gain_ctrl3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_gain_ctrl3_msb, self.__reg_tx_gain_ctrl3_lsb, value)
class FE_TX_GAIN_CTRL_4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x10
        self.__reg_tx_gain_ctrl4_lsb = 0
        self.__reg_tx_gain_ctrl4_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_gain_ctrl4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_gain_ctrl4_msb, self.__reg_tx_gain_ctrl4_lsb)
    @reg_tx_gain_ctrl4.setter
    def reg_tx_gain_ctrl4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_gain_ctrl4_msb, self.__reg_tx_gain_ctrl4_lsb, value)
class FE_PUBS_CFG0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x30
        self.__reg_rxoff_end_lsb = 24
        self.__reg_rxoff_end_msb = 31
        self.__reg_rxoff_start_lsb = 16
        self.__reg_rxoff_start_msb = 23
        self.__reg_rxon_end_lsb = 8
        self.__reg_rxon_end_msb = 15
        self.__reg_rxon_start_lsb = 0
        self.__reg_rxon_start_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxoff_end(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxoff_end_msb, self.__reg_rxoff_end_lsb)
    @reg_rxoff_end.setter
    def reg_rxoff_end(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxoff_end_msb, self.__reg_rxoff_end_lsb, value)

    @property
    def reg_rxoff_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxoff_start_msb, self.__reg_rxoff_start_lsb)
    @reg_rxoff_start.setter
    def reg_rxoff_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxoff_start_msb, self.__reg_rxoff_start_lsb, value)

    @property
    def reg_rxon_end(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxon_end_msb, self.__reg_rxon_end_lsb)
    @reg_rxon_end.setter
    def reg_rxon_end(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxon_end_msb, self.__reg_rxon_end_lsb, value)

    @property
    def reg_rxon_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxon_start_msb, self.__reg_rxon_start_lsb)
    @reg_rxon_start.setter
    def reg_rxon_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxon_start_msb, self.__reg_rxon_start_lsb, value)
class FE_PUBS_CFG1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x34
        self.__reg_txoff_end_lsb = 24
        self.__reg_txoff_end_msb = 31
        self.__reg_txoff_start_lsb = 16
        self.__reg_txoff_start_msb = 23
        self.__reg_txon_end_lsb = 8
        self.__reg_txon_end_msb = 15
        self.__reg_txon_start_lsb = 0
        self.__reg_txon_start_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txoff_end(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txoff_end_msb, self.__reg_txoff_end_lsb)
    @reg_txoff_end.setter
    def reg_txoff_end(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txoff_end_msb, self.__reg_txoff_end_lsb, value)

    @property
    def reg_txoff_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txoff_start_msb, self.__reg_txoff_start_lsb)
    @reg_txoff_start.setter
    def reg_txoff_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txoff_start_msb, self.__reg_txoff_start_lsb, value)

    @property
    def reg_txon_end(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txon_end_msb, self.__reg_txon_end_lsb)
    @reg_txon_end.setter
    def reg_txon_end(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txon_end_msb, self.__reg_txon_end_lsb, value)

    @property
    def reg_txon_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txon_start_msb, self.__reg_txon_start_lsb)
    @reg_txon_start.setter
    def reg_txon_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txon_start_msb, self.__reg_txon_start_lsb, value)
class FE_PUBS_CFG2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x38
        self.__reg_paoff_end_lsb = 24
        self.__reg_paoff_end_msb = 31
        self.__reg_paoff_start_lsb = 16
        self.__reg_paoff_start_msb = 23
        self.__reg_paon_end_lsb = 8
        self.__reg_paon_end_msb = 15
        self.__reg_paon_start_lsb = 0
        self.__reg_paon_start_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_paoff_end(self):
        return self.__MEM.rdm(self.__addr, self.__reg_paoff_end_msb, self.__reg_paoff_end_lsb)
    @reg_paoff_end.setter
    def reg_paoff_end(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_paoff_end_msb, self.__reg_paoff_end_lsb, value)

    @property
    def reg_paoff_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_paoff_start_msb, self.__reg_paoff_start_lsb)
    @reg_paoff_start.setter
    def reg_paoff_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_paoff_start_msb, self.__reg_paoff_start_lsb, value)

    @property
    def reg_paon_end(self):
        return self.__MEM.rdm(self.__addr, self.__reg_paon_end_msb, self.__reg_paon_end_lsb)
    @reg_paon_end.setter
    def reg_paon_end(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_paon_end_msb, self.__reg_paon_end_lsb, value)

    @property
    def reg_paon_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_paon_start_msb, self.__reg_paon_start_lsb)
    @reg_paon_start.setter
    def reg_paon_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_paon_start_msb, self.__reg_paon_start_lsb, value)
class FE_PUBS_CFG3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x3c
        self.__reg_rxoff_bt_end_lsb = 24
        self.__reg_rxoff_bt_end_msb = 31
        self.__reg_rxoff_bt_start_lsb = 16
        self.__reg_rxoff_bt_start_msb = 23
        self.__reg_rxon_bt_end_lsb = 8
        self.__reg_rxon_bt_end_msb = 15
        self.__reg_rxon_bt_start_lsb = 0
        self.__reg_rxon_bt_start_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxoff_bt_end(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxoff_bt_end_msb, self.__reg_rxoff_bt_end_lsb)
    @reg_rxoff_bt_end.setter
    def reg_rxoff_bt_end(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxoff_bt_end_msb, self.__reg_rxoff_bt_end_lsb, value)

    @property
    def reg_rxoff_bt_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxoff_bt_start_msb, self.__reg_rxoff_bt_start_lsb)
    @reg_rxoff_bt_start.setter
    def reg_rxoff_bt_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxoff_bt_start_msb, self.__reg_rxoff_bt_start_lsb, value)

    @property
    def reg_rxon_bt_end(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxon_bt_end_msb, self.__reg_rxon_bt_end_lsb)
    @reg_rxon_bt_end.setter
    def reg_rxon_bt_end(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxon_bt_end_msb, self.__reg_rxon_bt_end_lsb, value)

    @property
    def reg_rxon_bt_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxon_bt_start_msb, self.__reg_rxon_bt_start_lsb)
    @reg_rxon_bt_start.setter
    def reg_rxon_bt_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxon_bt_start_msb, self.__reg_rxon_bt_start_lsb, value)
class FE_PUBS_CFG4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x40
        self.__reg_txoff_bt_end_lsb = 24
        self.__reg_txoff_bt_end_msb = 31
        self.__reg_txoff_bt_start_lsb = 16
        self.__reg_txoff_bt_start_msb = 23
        self.__reg_txon_bt_end_lsb = 8
        self.__reg_txon_bt_end_msb = 15
        self.__reg_txon_bt_start_lsb = 0
        self.__reg_txon_bt_start_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txoff_bt_end(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txoff_bt_end_msb, self.__reg_txoff_bt_end_lsb)
    @reg_txoff_bt_end.setter
    def reg_txoff_bt_end(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txoff_bt_end_msb, self.__reg_txoff_bt_end_lsb, value)

    @property
    def reg_txoff_bt_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txoff_bt_start_msb, self.__reg_txoff_bt_start_lsb)
    @reg_txoff_bt_start.setter
    def reg_txoff_bt_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txoff_bt_start_msb, self.__reg_txoff_bt_start_lsb, value)

    @property
    def reg_txon_bt_end(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txon_bt_end_msb, self.__reg_txon_bt_end_lsb)
    @reg_txon_bt_end.setter
    def reg_txon_bt_end(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txon_bt_end_msb, self.__reg_txon_bt_end_lsb, value)

    @property
    def reg_txon_bt_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txon_bt_start_msb, self.__reg_txon_bt_start_lsb)
    @reg_txon_bt_start.setter
    def reg_txon_bt_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txon_bt_start_msb, self.__reg_txon_bt_start_lsb, value)
class FE_PUBS_CFG5(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x44
        self.__reg_paoff_bt_end_lsb = 24
        self.__reg_paoff_bt_end_msb = 31
        self.__reg_paoff_bt_start_lsb = 16
        self.__reg_paoff_bt_start_msb = 23
        self.__reg_paon_bt_end_lsb = 8
        self.__reg_paon_bt_end_msb = 15
        self.__reg_paon_bt_start_lsb = 0
        self.__reg_paon_bt_start_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_paoff_bt_end(self):
        return self.__MEM.rdm(self.__addr, self.__reg_paoff_bt_end_msb, self.__reg_paoff_bt_end_lsb)
    @reg_paoff_bt_end.setter
    def reg_paoff_bt_end(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_paoff_bt_end_msb, self.__reg_paoff_bt_end_lsb, value)

    @property
    def reg_paoff_bt_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_paoff_bt_start_msb, self.__reg_paoff_bt_start_lsb)
    @reg_paoff_bt_start.setter
    def reg_paoff_bt_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_paoff_bt_start_msb, self.__reg_paoff_bt_start_lsb, value)

    @property
    def reg_paon_bt_end(self):
        return self.__MEM.rdm(self.__addr, self.__reg_paon_bt_end_msb, self.__reg_paon_bt_end_lsb)
    @reg_paon_bt_end.setter
    def reg_paon_bt_end(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_paon_bt_end_msb, self.__reg_paon_bt_end_lsb, value)

    @property
    def reg_paon_bt_start(self):
        return self.__MEM.rdm(self.__addr, self.__reg_paon_bt_start_msb, self.__reg_paon_bt_start_lsb)
    @reg_paon_bt_start.setter
    def reg_paon_bt_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_paon_bt_start_msb, self.__reg_paon_bt_start_lsb, value)
class FE_PUBS_CFG6(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x48
        self.__reg_paoff_delay_lsb = 24
        self.__reg_paoff_delay_msb = 31
        self.__reg_txoff_delay_lsb = 16
        self.__reg_txoff_delay_msb = 23
        self.__reg_paon_delay_lsb = 8
        self.__reg_paon_delay_msb = 15
        self.__reg_txon_delay_lsb = 0
        self.__reg_txon_delay_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_paoff_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_paoff_delay_msb, self.__reg_paoff_delay_lsb)
    @reg_paoff_delay.setter
    def reg_paoff_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_paoff_delay_msb, self.__reg_paoff_delay_lsb, value)

    @property
    def reg_txoff_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txoff_delay_msb, self.__reg_txoff_delay_lsb)
    @reg_txoff_delay.setter
    def reg_txoff_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txoff_delay_msb, self.__reg_txoff_delay_lsb, value)

    @property
    def reg_paon_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_paon_delay_msb, self.__reg_paon_delay_lsb)
    @reg_paon_delay.setter
    def reg_paon_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_paon_delay_msb, self.__reg_paon_delay_lsb, value)

    @property
    def reg_txon_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txon_delay_msb, self.__reg_txon_delay_lsb)
    @reg_txon_delay.setter
    def reg_txon_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txon_delay_msb, self.__reg_txon_delay_lsb, value)
class FE_PUBS_CFG7(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x4c
        self.__reg_paoff_bt_delay_lsb = 24
        self.__reg_paoff_bt_delay_msb = 31
        self.__reg_txoff_bt_delay_lsb = 16
        self.__reg_txoff_bt_delay_msb = 23
        self.__reg_paon_bt_delay_lsb = 8
        self.__reg_paon_bt_delay_msb = 15
        self.__reg_txon_bt_delay_lsb = 0
        self.__reg_txon_bt_delay_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_paoff_bt_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_paoff_bt_delay_msb, self.__reg_paoff_bt_delay_lsb)
    @reg_paoff_bt_delay.setter
    def reg_paoff_bt_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_paoff_bt_delay_msb, self.__reg_paoff_bt_delay_lsb, value)

    @property
    def reg_txoff_bt_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txoff_bt_delay_msb, self.__reg_txoff_bt_delay_lsb)
    @reg_txoff_bt_delay.setter
    def reg_txoff_bt_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txoff_bt_delay_msb, self.__reg_txoff_bt_delay_lsb, value)

    @property
    def reg_paon_bt_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_paon_bt_delay_msb, self.__reg_paon_bt_delay_lsb)
    @reg_paon_bt_delay.setter
    def reg_paon_bt_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_paon_bt_delay_msb, self.__reg_paon_bt_delay_lsb, value)

    @property
    def reg_txon_bt_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txon_bt_delay_msb, self.__reg_txon_bt_delay_lsb)
    @reg_txon_bt_delay.setter
    def reg_txon_bt_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txon_bt_delay_msb, self.__reg_txon_bt_delay_lsb, value)
class FE_PUBS_CFG8(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x50
        self.__reg_rxon_bt_delay_lsb = 8
        self.__reg_rxon_bt_delay_msb = 15
        self.__reg_rxon_delay_lsb = 0
        self.__reg_rxon_delay_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rxon_bt_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxon_bt_delay_msb, self.__reg_rxon_bt_delay_lsb)
    @reg_rxon_bt_delay.setter
    def reg_rxon_bt_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxon_bt_delay_msb, self.__reg_rxon_bt_delay_lsb, value)

    @property
    def reg_rxon_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxon_delay_msb, self.__reg_rxon_delay_lsb)
    @reg_rxon_delay.setter
    def reg_rxon_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxon_delay_msb, self.__reg_rxon_delay_lsb, value)
class FE_IQ_EST_CTRL_01(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x60
        self.__iq_est_ssea_done_lsb = 31
        self.__iq_est_ssea_done_msb = 31
        self.__iq_est_ssea_overflowa_lsb = 30
        self.__iq_est_ssea_overflowa_msb = 30
        self.__iq_est_ssea_overflowm_lsb = 29
        self.__iq_est_ssea_overflowm_msb = 29
        self.__reg_iq_est_ctrl_1_lsb = 0
        self.__reg_iq_est_ctrl_1_msb = 28
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def iq_est_ssea_done(self):
        return self.__MEM.rdm(self.__addr, self.__iq_est_ssea_done_msb, self.__iq_est_ssea_done_lsb)
    @iq_est_ssea_done.setter
    def iq_est_ssea_done(self, value):
        return self.__MEM.wrm(self.__addr, self.__iq_est_ssea_done_msb, self.__iq_est_ssea_done_lsb, value)

    @property
    def iq_est_ssea_overflowa(self):
        return self.__MEM.rdm(self.__addr, self.__iq_est_ssea_overflowa_msb, self.__iq_est_ssea_overflowa_lsb)
    @iq_est_ssea_overflowa.setter
    def iq_est_ssea_overflowa(self, value):
        return self.__MEM.wrm(self.__addr, self.__iq_est_ssea_overflowa_msb, self.__iq_est_ssea_overflowa_lsb, value)

    @property
    def iq_est_ssea_overflowm(self):
        return self.__MEM.rdm(self.__addr, self.__iq_est_ssea_overflowm_msb, self.__iq_est_ssea_overflowm_lsb)
    @iq_est_ssea_overflowm.setter
    def iq_est_ssea_overflowm(self, value):
        return self.__MEM.wrm(self.__addr, self.__iq_est_ssea_overflowm_msb, self.__iq_est_ssea_overflowm_lsb, value)

    @property
    def reg_iq_est_ctrl_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_est_ctrl_1_msb, self.__reg_iq_est_ctrl_1_lsb)
    @reg_iq_est_ctrl_1.setter
    def reg_iq_est_ctrl_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_est_ctrl_1_msb, self.__reg_iq_est_ctrl_1_lsb, value)
class FE_IQ_SSEA_CORR1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x64
        self.__iq_est_ssea_corr1_lsb = 0
        self.__iq_est_ssea_corr1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def iq_est_ssea_corr1(self):
        return self.__MEM.rdm(self.__addr, self.__iq_est_ssea_corr1_msb, self.__iq_est_ssea_corr1_lsb)
    @iq_est_ssea_corr1.setter
    def iq_est_ssea_corr1(self, value):
        return self.__MEM.wrm(self.__addr, self.__iq_est_ssea_corr1_msb, self.__iq_est_ssea_corr1_lsb, value)
class FE_IQ_SSEA_CORR1_CONJ(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x68
        self.__iq_est_ssea_corr1_conj_lsb = 0
        self.__iq_est_ssea_corr1_conj_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def iq_est_ssea_corr1_conj(self):
        return self.__MEM.rdm(self.__addr, self.__iq_est_ssea_corr1_conj_msb, self.__iq_est_ssea_corr1_conj_lsb)
    @iq_est_ssea_corr1_conj.setter
    def iq_est_ssea_corr1_conj(self, value):
        return self.__MEM.wrm(self.__addr, self.__iq_est_ssea_corr1_conj_msb, self.__iq_est_ssea_corr1_conj_lsb, value)
class FE_IQ_SSEA_CORR2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x6c
        self.__iq_est_ssea_corr2_lsb = 0
        self.__iq_est_ssea_corr2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def iq_est_ssea_corr2(self):
        return self.__MEM.rdm(self.__addr, self.__iq_est_ssea_corr2_msb, self.__iq_est_ssea_corr2_lsb)
    @iq_est_ssea_corr2.setter
    def iq_est_ssea_corr2(self, value):
        return self.__MEM.wrm(self.__addr, self.__iq_est_ssea_corr2_msb, self.__iq_est_ssea_corr2_lsb, value)
class FE_IQ_SSEA_CORR2_CONJ(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x70
        self.__iq_est_ssea_corr2_conj_lsb = 0
        self.__iq_est_ssea_corr2_conj_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def iq_est_ssea_corr2_conj(self):
        return self.__MEM.rdm(self.__addr, self.__iq_est_ssea_corr2_conj_msb, self.__iq_est_ssea_corr2_conj_lsb)
    @iq_est_ssea_corr2_conj.setter
    def iq_est_ssea_corr2_conj(self, value):
        return self.__MEM.wrm(self.__addr, self.__iq_est_ssea_corr2_conj_msb, self.__iq_est_ssea_corr2_conj_lsb, value)
class FE_IQ_SSEA_DC(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x74
        self.__iq_est_ssea_dc_lsb = 0
        self.__iq_est_ssea_dc_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def iq_est_ssea_dc(self):
        return self.__MEM.rdm(self.__addr, self.__iq_est_ssea_dc_msb, self.__iq_est_ssea_dc_lsb)
    @iq_est_ssea_dc.setter
    def iq_est_ssea_dc(self, value):
        return self.__MEM.wrm(self.__addr, self.__iq_est_ssea_dc_msb, self.__iq_est_ssea_dc_lsb, value)
class FE_IQ_SSEA_POWER(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x78
        self.__iq_est_ssea_power_lsb = 0
        self.__iq_est_ssea_power_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def iq_est_ssea_power(self):
        return self.__MEM.rdm(self.__addr, self.__iq_est_ssea_power_msb, self.__iq_est_ssea_power_lsb)
    @iq_est_ssea_power.setter
    def iq_est_ssea_power(self, value):
        return self.__MEM.wrm(self.__addr, self.__iq_est_ssea_power_msb, self.__iq_est_ssea_power_lsb, value)
class FE_IQ_EST_CTRL_00(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x7c
        self.__iq_est_done_lsb = 31
        self.__iq_est_done_msb = 31
        self.__reg_iq_est_ctrl_0_lsb = 0
        self.__reg_iq_est_ctrl_0_msb = 30
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def iq_est_done(self):
        return self.__MEM.rdm(self.__addr, self.__iq_est_done_msb, self.__iq_est_done_lsb)
    @iq_est_done.setter
    def iq_est_done(self, value):
        return self.__MEM.wrm(self.__addr, self.__iq_est_done_msb, self.__iq_est_done_lsb, value)

    @property
    def reg_iq_est_ctrl_0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_est_ctrl_0_msb, self.__reg_iq_est_ctrl_0_lsb)
    @reg_iq_est_ctrl_0.setter
    def reg_iq_est_ctrl_0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_est_ctrl_0_msb, self.__reg_iq_est_ctrl_0_lsb, value)
class FE_IQ_RESULT1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x80
        self.__iq_est_mult_ii_lsb = 0
        self.__iq_est_mult_ii_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def iq_est_mult_ii(self):
        return self.__MEM.rdm(self.__addr, self.__iq_est_mult_ii_msb, self.__iq_est_mult_ii_lsb)
    @iq_est_mult_ii.setter
    def iq_est_mult_ii(self, value):
        return self.__MEM.wrm(self.__addr, self.__iq_est_mult_ii_msb, self.__iq_est_mult_ii_lsb, value)
class FE_IQ_RESULT2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x84
        self.__iq_est_mult_iq_lsb = 0
        self.__iq_est_mult_iq_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def iq_est_mult_iq(self):
        return self.__MEM.rdm(self.__addr, self.__iq_est_mult_iq_msb, self.__iq_est_mult_iq_lsb)
    @iq_est_mult_iq.setter
    def iq_est_mult_iq(self, value):
        return self.__MEM.wrm(self.__addr, self.__iq_est_mult_iq_msb, self.__iq_est_mult_iq_lsb, value)
class FE_IQ_RESULT3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x88
        self.__iq_est_mult_qi_lsb = 0
        self.__iq_est_mult_qi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def iq_est_mult_qi(self):
        return self.__MEM.rdm(self.__addr, self.__iq_est_mult_qi_msb, self.__iq_est_mult_qi_lsb)
    @iq_est_mult_qi.setter
    def iq_est_mult_qi(self, value):
        return self.__MEM.wrm(self.__addr, self.__iq_est_mult_qi_msb, self.__iq_est_mult_qi_lsb, value)
class FE_IQ_RESULT4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x8c
        self.__iq_est_mult_qq_lsb = 0
        self.__iq_est_mult_qq_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def iq_est_mult_qq(self):
        return self.__MEM.rdm(self.__addr, self.__iq_est_mult_qq_msb, self.__iq_est_mult_qq_lsb)
    @iq_est_mult_qq.setter
    def iq_est_mult_qq(self, value):
        return self.__MEM.wrm(self.__addr, self.__iq_est_mult_qq_msb, self.__iq_est_mult_qq_lsb, value)
class FE_GEN_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x90
        self.__reg_iq_est_force_pu_lsb = 5
        self.__reg_iq_est_force_pu_msb = 5
        self.__reg_iq_est_force_pd_lsb = 4
        self.__reg_iq_est_force_pd_msb = 4
        self.__filt_att_1db_en_lsb = 3
        self.__filt_att_1db_en_msb = 3
        self.__reg_adc_80m_dsp_lsb = 2
        self.__reg_adc_80m_dsp_msb = 2
        self.__reg_dump_mode_lsb = 0
        self.__reg_dump_mode_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_iq_est_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_est_force_pu_msb, self.__reg_iq_est_force_pu_lsb)
    @reg_iq_est_force_pu.setter
    def reg_iq_est_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_est_force_pu_msb, self.__reg_iq_est_force_pu_lsb, value)

    @property
    def reg_iq_est_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_iq_est_force_pd_msb, self.__reg_iq_est_force_pd_lsb)
    @reg_iq_est_force_pd.setter
    def reg_iq_est_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_iq_est_force_pd_msb, self.__reg_iq_est_force_pd_lsb, value)

    @property
    def filt_att_1db_en(self):
        return self.__MEM.rdm(self.__addr, self.__filt_att_1db_en_msb, self.__filt_att_1db_en_lsb)
    @filt_att_1db_en.setter
    def filt_att_1db_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__filt_att_1db_en_msb, self.__filt_att_1db_en_lsb, value)

    @property
    def reg_adc_80m_dsp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_80m_dsp_msb, self.__reg_adc_80m_dsp_lsb)
    @reg_adc_80m_dsp.setter
    def reg_adc_80m_dsp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_80m_dsp_msb, self.__reg_adc_80m_dsp_lsb, value)

    @property
    def reg_dump_mode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dump_mode_msb, self.__reg_dump_mode_lsb)
    @reg_dump_mode.setter
    def reg_dump_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dump_mode_msb, self.__reg_dump_mode_lsb, value)
class FE_PUBS_CTRL0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x94
        self.__reg_pbus_data_ext_num_lsb = 30
        self.__reg_pbus_data_ext_num_msb = 31
        self.__reg_pbus_data_ext_lsb = 29
        self.__reg_pbus_data_ext_msb = 29
        self.__reg_pbus_en_nodelay_lsb = 28
        self.__reg_pbus_en_nodelay_msb = 28
        self.__reg_rf_cfg_force_pbus_we_lsb = 19
        self.__reg_rf_cfg_force_pbus_we_msb = 27
        self.__reg_vga_dg_buf_lsb = 18
        self.__reg_vga_dg_buf_msb = 18
        self.__reg_host_inf_2cyc_lsb = 17
        self.__reg_host_inf_2cyc_msb = 17
        self.__reg_rf_cfg_force_en_lsb = 15
        self.__reg_rf_cfg_force_en_msb = 16
        self.__reg_rf_cfg_force_pbus_lsb = 6
        self.__reg_rf_cfg_force_pbus_msb = 14
        self.__reg_rf_cfg_force_bus_sel_lsb = 2
        self.__reg_rf_cfg_force_bus_sel_msb = 5
        self.__reg_rf_cfg_force_valid_lsb = 1
        self.__reg_rf_cfg_force_valid_msb = 1
        self.__reg_rf_cfg_force_mode_lsb = 0
        self.__reg_rf_cfg_force_mode_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_pbus_data_ext_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pbus_data_ext_num_msb, self.__reg_pbus_data_ext_num_lsb)
    @reg_pbus_data_ext_num.setter
    def reg_pbus_data_ext_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pbus_data_ext_num_msb, self.__reg_pbus_data_ext_num_lsb, value)

    @property
    def reg_pbus_data_ext(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pbus_data_ext_msb, self.__reg_pbus_data_ext_lsb)
    @reg_pbus_data_ext.setter
    def reg_pbus_data_ext(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pbus_data_ext_msb, self.__reg_pbus_data_ext_lsb, value)

    @property
    def reg_pbus_en_nodelay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pbus_en_nodelay_msb, self.__reg_pbus_en_nodelay_lsb)
    @reg_pbus_en_nodelay.setter
    def reg_pbus_en_nodelay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pbus_en_nodelay_msb, self.__reg_pbus_en_nodelay_lsb, value)

    @property
    def reg_rf_cfg_force_pbus_we(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rf_cfg_force_pbus_we_msb, self.__reg_rf_cfg_force_pbus_we_lsb)
    @reg_rf_cfg_force_pbus_we.setter
    def reg_rf_cfg_force_pbus_we(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rf_cfg_force_pbus_we_msb, self.__reg_rf_cfg_force_pbus_we_lsb, value)

    @property
    def reg_vga_dg_buf(self):
        return self.__MEM.rdm(self.__addr, self.__reg_vga_dg_buf_msb, self.__reg_vga_dg_buf_lsb)
    @reg_vga_dg_buf.setter
    def reg_vga_dg_buf(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_vga_dg_buf_msb, self.__reg_vga_dg_buf_lsb, value)

    @property
    def reg_host_inf_2cyc(self):
        return self.__MEM.rdm(self.__addr, self.__reg_host_inf_2cyc_msb, self.__reg_host_inf_2cyc_lsb)
    @reg_host_inf_2cyc.setter
    def reg_host_inf_2cyc(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_host_inf_2cyc_msb, self.__reg_host_inf_2cyc_lsb, value)

    @property
    def reg_rf_cfg_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rf_cfg_force_en_msb, self.__reg_rf_cfg_force_en_lsb)
    @reg_rf_cfg_force_en.setter
    def reg_rf_cfg_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rf_cfg_force_en_msb, self.__reg_rf_cfg_force_en_lsb, value)

    @property
    def reg_rf_cfg_force_pbus(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rf_cfg_force_pbus_msb, self.__reg_rf_cfg_force_pbus_lsb)
    @reg_rf_cfg_force_pbus.setter
    def reg_rf_cfg_force_pbus(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rf_cfg_force_pbus_msb, self.__reg_rf_cfg_force_pbus_lsb, value)

    @property
    def reg_rf_cfg_force_bus_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rf_cfg_force_bus_sel_msb, self.__reg_rf_cfg_force_bus_sel_lsb)
    @reg_rf_cfg_force_bus_sel.setter
    def reg_rf_cfg_force_bus_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rf_cfg_force_bus_sel_msb, self.__reg_rf_cfg_force_bus_sel_lsb, value)

    @property
    def reg_rf_cfg_force_valid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rf_cfg_force_valid_msb, self.__reg_rf_cfg_force_valid_lsb)
    @reg_rf_cfg_force_valid.setter
    def reg_rf_cfg_force_valid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rf_cfg_force_valid_msb, self.__reg_rf_cfg_force_valid_lsb, value)

    @property
    def reg_rf_cfg_force_mode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rf_cfg_force_mode_msb, self.__reg_rf_cfg_force_mode_lsb)
    @reg_rf_cfg_force_mode.setter
    def reg_rf_cfg_force_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rf_cfg_force_mode_msb, self.__reg_rf_cfg_force_mode_lsb, value)
class FE_PUBS_CTRL2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0x9c
        self.__reg_pwdet_bt_en_lsb = 31
        self.__reg_pwdet_bt_en_msb = 31
        self.__reg_pll_stop_use_bt_lsb = 30
        self.__reg_pll_stop_use_bt_msb = 30
        self.__reg_pll_stop_use_wifi_lsb = 29
        self.__reg_pll_stop_use_wifi_msb = 29
        self.__reg_pbus_bt_prot_lsb = 28
        self.__reg_pbus_bt_prot_msb = 28
        self.__reg_pbus_force_prot_lsb = 27
        self.__reg_pbus_force_prot_msb = 27
        self.__reg_pbus_rx_prot_lsb = 26
        self.__reg_pbus_rx_prot_msb = 26
        self.__reg_pbus_tx_prot_lsb = 25
        self.__reg_pbus_tx_prot_msb = 25
        self.__reg_test_fail_clr_lsb = 24
        self.__reg_test_fail_clr_msb = 24
        self.__reg_txrf2_pbus_en_mask_lsb = 23
        self.__reg_txrf2_pbus_en_mask_msb = 23
        self.__reg_txrf1_pbus_en_mask_lsb = 22
        self.__reg_txrf1_pbus_en_mask_msb = 22
        self.__reg_dcoq_pbus_en_mask_lsb = 20
        self.__reg_dcoq_pbus_en_mask_msb = 21
        self.__reg_dcoi_pbus_en_mask_lsb = 18
        self.__reg_dcoi_pbus_en_mask_msb = 19
        self.__reg_bb_pbus_en_mask_lsb = 16
        self.__reg_bb_pbus_en_mask_msb = 17
        self.__reg_rfrx_pbus_en_mask_lsb = 15
        self.__reg_rfrx_pbus_en_mask_msb = 15
        self.__reg_sw_rxtx_inv_lsb = 14
        self.__reg_sw_rxtx_inv_msb = 14
        self.__reg_sw_wifibt_inv_lsb = 13
        self.__reg_sw_wifibt_inv_msb = 13
        self.__reg_gain_change_req_en_lsb = 12
        self.__reg_gain_change_req_en_msb = 12
        self.__reg_pa_off_bt_req_en_lsb = 11
        self.__reg_pa_off_bt_req_en_msb = 11
        self.__reg_pa_on_bt_req_en_lsb = 10
        self.__reg_pa_on_bt_req_en_msb = 10
        self.__reg_tx_off_bt_req_en_lsb = 9
        self.__reg_tx_off_bt_req_en_msb = 9
        self.__reg_tx_on_bt_req_en_lsb = 8
        self.__reg_tx_on_bt_req_en_msb = 8
        self.__reg_rx_off_bt_req_en_lsb = 7
        self.__reg_rx_off_bt_req_en_msb = 7
        self.__reg_rx_on_bt_req_en_lsb = 6
        self.__reg_rx_on_bt_req_en_msb = 6
        self.__reg_pa_off_req_en_lsb = 5
        self.__reg_pa_off_req_en_msb = 5
        self.__reg_pa_on_req_en_lsb = 4
        self.__reg_pa_on_req_en_msb = 4
        self.__reg_tx_off_req_en_lsb = 3
        self.__reg_tx_off_req_en_msb = 3
        self.__reg_tx_on_req_en_lsb = 2
        self.__reg_tx_on_req_en_msb = 2
        self.__reg_rx_off_req_en_lsb = 1
        self.__reg_rx_off_req_en_msb = 1
        self.__reg_rx_on_req_en_lsb = 0
        self.__reg_rx_on_req_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_pwdet_bt_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pwdet_bt_en_msb, self.__reg_pwdet_bt_en_lsb)
    @reg_pwdet_bt_en.setter
    def reg_pwdet_bt_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pwdet_bt_en_msb, self.__reg_pwdet_bt_en_lsb, value)

    @property
    def reg_pll_stop_use_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pll_stop_use_bt_msb, self.__reg_pll_stop_use_bt_lsb)
    @reg_pll_stop_use_bt.setter
    def reg_pll_stop_use_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pll_stop_use_bt_msb, self.__reg_pll_stop_use_bt_lsb, value)

    @property
    def reg_pll_stop_use_wifi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pll_stop_use_wifi_msb, self.__reg_pll_stop_use_wifi_lsb)
    @reg_pll_stop_use_wifi.setter
    def reg_pll_stop_use_wifi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pll_stop_use_wifi_msb, self.__reg_pll_stop_use_wifi_lsb, value)

    @property
    def reg_pbus_bt_prot(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pbus_bt_prot_msb, self.__reg_pbus_bt_prot_lsb)
    @reg_pbus_bt_prot.setter
    def reg_pbus_bt_prot(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pbus_bt_prot_msb, self.__reg_pbus_bt_prot_lsb, value)

    @property
    def reg_pbus_force_prot(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pbus_force_prot_msb, self.__reg_pbus_force_prot_lsb)
    @reg_pbus_force_prot.setter
    def reg_pbus_force_prot(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pbus_force_prot_msb, self.__reg_pbus_force_prot_lsb, value)

    @property
    def reg_pbus_rx_prot(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pbus_rx_prot_msb, self.__reg_pbus_rx_prot_lsb)
    @reg_pbus_rx_prot.setter
    def reg_pbus_rx_prot(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pbus_rx_prot_msb, self.__reg_pbus_rx_prot_lsb, value)

    @property
    def reg_pbus_tx_prot(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pbus_tx_prot_msb, self.__reg_pbus_tx_prot_lsb)
    @reg_pbus_tx_prot.setter
    def reg_pbus_tx_prot(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pbus_tx_prot_msb, self.__reg_pbus_tx_prot_lsb, value)

    @property
    def reg_test_fail_clr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_test_fail_clr_msb, self.__reg_test_fail_clr_lsb)
    @reg_test_fail_clr.setter
    def reg_test_fail_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_test_fail_clr_msb, self.__reg_test_fail_clr_lsb, value)

    @property
    def reg_txrf2_pbus_en_mask(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrf2_pbus_en_mask_msb, self.__reg_txrf2_pbus_en_mask_lsb)
    @reg_txrf2_pbus_en_mask.setter
    def reg_txrf2_pbus_en_mask(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrf2_pbus_en_mask_msb, self.__reg_txrf2_pbus_en_mask_lsb, value)

    @property
    def reg_txrf1_pbus_en_mask(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrf1_pbus_en_mask_msb, self.__reg_txrf1_pbus_en_mask_lsb)
    @reg_txrf1_pbus_en_mask.setter
    def reg_txrf1_pbus_en_mask(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrf1_pbus_en_mask_msb, self.__reg_txrf1_pbus_en_mask_lsb, value)

    @property
    def reg_dcoq_pbus_en_mask(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dcoq_pbus_en_mask_msb, self.__reg_dcoq_pbus_en_mask_lsb)
    @reg_dcoq_pbus_en_mask.setter
    def reg_dcoq_pbus_en_mask(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dcoq_pbus_en_mask_msb, self.__reg_dcoq_pbus_en_mask_lsb, value)

    @property
    def reg_dcoi_pbus_en_mask(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dcoi_pbus_en_mask_msb, self.__reg_dcoi_pbus_en_mask_lsb)
    @reg_dcoi_pbus_en_mask.setter
    def reg_dcoi_pbus_en_mask(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dcoi_pbus_en_mask_msb, self.__reg_dcoi_pbus_en_mask_lsb, value)

    @property
    def reg_bb_pbus_en_mask(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bb_pbus_en_mask_msb, self.__reg_bb_pbus_en_mask_lsb)
    @reg_bb_pbus_en_mask.setter
    def reg_bb_pbus_en_mask(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bb_pbus_en_mask_msb, self.__reg_bb_pbus_en_mask_lsb, value)

    @property
    def reg_rfrx_pbus_en_mask(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rfrx_pbus_en_mask_msb, self.__reg_rfrx_pbus_en_mask_lsb)
    @reg_rfrx_pbus_en_mask.setter
    def reg_rfrx_pbus_en_mask(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rfrx_pbus_en_mask_msb, self.__reg_rfrx_pbus_en_mask_lsb, value)

    @property
    def reg_sw_rxtx_inv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sw_rxtx_inv_msb, self.__reg_sw_rxtx_inv_lsb)
    @reg_sw_rxtx_inv.setter
    def reg_sw_rxtx_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sw_rxtx_inv_msb, self.__reg_sw_rxtx_inv_lsb, value)

    @property
    def reg_sw_wifibt_inv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sw_wifibt_inv_msb, self.__reg_sw_wifibt_inv_lsb)
    @reg_sw_wifibt_inv.setter
    def reg_sw_wifibt_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sw_wifibt_inv_msb, self.__reg_sw_wifibt_inv_lsb, value)

    @property
    def reg_gain_change_req_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_gain_change_req_en_msb, self.__reg_gain_change_req_en_lsb)
    @reg_gain_change_req_en.setter
    def reg_gain_change_req_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_gain_change_req_en_msb, self.__reg_gain_change_req_en_lsb, value)

    @property
    def reg_pa_off_bt_req_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pa_off_bt_req_en_msb, self.__reg_pa_off_bt_req_en_lsb)
    @reg_pa_off_bt_req_en.setter
    def reg_pa_off_bt_req_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pa_off_bt_req_en_msb, self.__reg_pa_off_bt_req_en_lsb, value)

    @property
    def reg_pa_on_bt_req_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pa_on_bt_req_en_msb, self.__reg_pa_on_bt_req_en_lsb)
    @reg_pa_on_bt_req_en.setter
    def reg_pa_on_bt_req_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pa_on_bt_req_en_msb, self.__reg_pa_on_bt_req_en_lsb, value)

    @property
    def reg_tx_off_bt_req_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_off_bt_req_en_msb, self.__reg_tx_off_bt_req_en_lsb)
    @reg_tx_off_bt_req_en.setter
    def reg_tx_off_bt_req_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_off_bt_req_en_msb, self.__reg_tx_off_bt_req_en_lsb, value)

    @property
    def reg_tx_on_bt_req_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_on_bt_req_en_msb, self.__reg_tx_on_bt_req_en_lsb)
    @reg_tx_on_bt_req_en.setter
    def reg_tx_on_bt_req_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_on_bt_req_en_msb, self.__reg_tx_on_bt_req_en_lsb, value)

    @property
    def reg_rx_off_bt_req_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_off_bt_req_en_msb, self.__reg_rx_off_bt_req_en_lsb)
    @reg_rx_off_bt_req_en.setter
    def reg_rx_off_bt_req_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_off_bt_req_en_msb, self.__reg_rx_off_bt_req_en_lsb, value)

    @property
    def reg_rx_on_bt_req_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_on_bt_req_en_msb, self.__reg_rx_on_bt_req_en_lsb)
    @reg_rx_on_bt_req_en.setter
    def reg_rx_on_bt_req_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_on_bt_req_en_msb, self.__reg_rx_on_bt_req_en_lsb, value)

    @property
    def reg_pa_off_req_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pa_off_req_en_msb, self.__reg_pa_off_req_en_lsb)
    @reg_pa_off_req_en.setter
    def reg_pa_off_req_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pa_off_req_en_msb, self.__reg_pa_off_req_en_lsb, value)

    @property
    def reg_pa_on_req_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pa_on_req_en_msb, self.__reg_pa_on_req_en_lsb)
    @reg_pa_on_req_en.setter
    def reg_pa_on_req_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pa_on_req_en_msb, self.__reg_pa_on_req_en_lsb, value)

    @property
    def reg_tx_off_req_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_off_req_en_msb, self.__reg_tx_off_req_en_lsb)
    @reg_tx_off_req_en.setter
    def reg_tx_off_req_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_off_req_en_msb, self.__reg_tx_off_req_en_lsb, value)

    @property
    def reg_tx_on_req_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_on_req_en_msb, self.__reg_tx_on_req_en_lsb)
    @reg_tx_on_req_en.setter
    def reg_tx_on_req_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_on_req_en_msb, self.__reg_tx_on_req_en_lsb, value)

    @property
    def reg_rx_off_req_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_off_req_en_msb, self.__reg_rx_off_req_en_lsb)
    @reg_rx_off_req_en.setter
    def reg_rx_off_req_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_off_req_en_msb, self.__reg_rx_off_req_en_lsb, value)

    @property
    def reg_rx_on_req_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_on_req_en_msb, self.__reg_rx_on_req_en_lsb)
    @reg_rx_on_req_en.setter
    def reg_rx_on_req_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_on_req_en_msb, self.__reg_rx_on_req_en_lsb, value)
class FE_PUBS_CTRL3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0xa0
        self.__rf_cfg_force_busy_lsb = 31
        self.__rf_cfg_force_busy_msb = 31
        self.__pbus_cfg_force_mode_lsb = 30
        self.__pbus_cfg_force_mode_msb = 30
        self.__reg_pbus_rxon_bt_force_en_lsb = 28
        self.__reg_pbus_rxon_bt_force_en_msb = 28
        self.__reg_pbus_rxon_bt_force_lsb = 27
        self.__reg_pbus_rxon_bt_force_msb = 27
        self.__reg_pbus_rxon_force_en_lsb = 26
        self.__reg_pbus_rxon_force_en_msb = 26
        self.__reg_pbus_rxon_force_lsb = 25
        self.__reg_pbus_rxon_force_msb = 25
        self.__reg_pbus_en_swap_lsb = 22
        self.__reg_pbus_en_swap_msb = 24
        self.__reg_dacpwd_force_en_lsb = 21
        self.__reg_dacpwd_force_en_msb = 21
        self.__reg_dacpwd_force_lsb = 20
        self.__reg_dacpwd_force_msb = 20
        self.__reg_adcpwd_force_en_lsb = 19
        self.__reg_adcpwd_force_en_msb = 19
        self.__reg_adcpwd_force_lsb = 18
        self.__reg_adcpwd_force_msb = 18
        self.__reg_txon_force_en_lsb = 17
        self.__reg_txon_force_en_msb = 17
        self.__reg_txon_force_lsb = 16
        self.__reg_txon_force_msb = 16
        self.__reg_rxon_force_en_lsb = 15
        self.__reg_rxon_force_en_msb = 15
        self.__reg_rxon_force_lsb = 14
        self.__reg_rxon_force_msb = 14
        self.__reg_bt_mode_on_force_en_lsb = 13
        self.__reg_bt_mode_on_force_en_msb = 13
        self.__reg_bt_mode_on_force_lsb = 12
        self.__reg_bt_mode_on_force_msb = 12
        self.__reg_dac_on_force_en_lsb = 11
        self.__reg_dac_on_force_en_msb = 11
        self.__reg_dac_on_force_lsb = 10
        self.__reg_dac_on_force_msb = 10
        self.__reg_adc_on_force_en_lsb = 9
        self.__reg_adc_on_force_en_msb = 9
        self.__reg_adc_on_force_lsb = 8
        self.__reg_adc_on_force_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rf_cfg_force_busy(self):
        return self.__MEM.rdm(self.__addr, self.__rf_cfg_force_busy_msb, self.__rf_cfg_force_busy_lsb)
    @rf_cfg_force_busy.setter
    def rf_cfg_force_busy(self, value):
        return self.__MEM.wrm(self.__addr, self.__rf_cfg_force_busy_msb, self.__rf_cfg_force_busy_lsb, value)

    @property
    def pbus_cfg_force_mode(self):
        return self.__MEM.rdm(self.__addr, self.__pbus_cfg_force_mode_msb, self.__pbus_cfg_force_mode_lsb)
    @pbus_cfg_force_mode.setter
    def pbus_cfg_force_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__pbus_cfg_force_mode_msb, self.__pbus_cfg_force_mode_lsb, value)

    @property
    def reg_pbus_rxon_bt_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pbus_rxon_bt_force_en_msb, self.__reg_pbus_rxon_bt_force_en_lsb)
    @reg_pbus_rxon_bt_force_en.setter
    def reg_pbus_rxon_bt_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pbus_rxon_bt_force_en_msb, self.__reg_pbus_rxon_bt_force_en_lsb, value)

    @property
    def reg_pbus_rxon_bt_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pbus_rxon_bt_force_msb, self.__reg_pbus_rxon_bt_force_lsb)
    @reg_pbus_rxon_bt_force.setter
    def reg_pbus_rxon_bt_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pbus_rxon_bt_force_msb, self.__reg_pbus_rxon_bt_force_lsb, value)

    @property
    def reg_pbus_rxon_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pbus_rxon_force_en_msb, self.__reg_pbus_rxon_force_en_lsb)
    @reg_pbus_rxon_force_en.setter
    def reg_pbus_rxon_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pbus_rxon_force_en_msb, self.__reg_pbus_rxon_force_en_lsb, value)

    @property
    def reg_pbus_rxon_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pbus_rxon_force_msb, self.__reg_pbus_rxon_force_lsb)
    @reg_pbus_rxon_force.setter
    def reg_pbus_rxon_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pbus_rxon_force_msb, self.__reg_pbus_rxon_force_lsb, value)

    @property
    def reg_pbus_en_swap(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pbus_en_swap_msb, self.__reg_pbus_en_swap_lsb)
    @reg_pbus_en_swap.setter
    def reg_pbus_en_swap(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pbus_en_swap_msb, self.__reg_pbus_en_swap_lsb, value)

    @property
    def reg_dacpwd_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dacpwd_force_en_msb, self.__reg_dacpwd_force_en_lsb)
    @reg_dacpwd_force_en.setter
    def reg_dacpwd_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dacpwd_force_en_msb, self.__reg_dacpwd_force_en_lsb, value)

    @property
    def reg_dacpwd_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dacpwd_force_msb, self.__reg_dacpwd_force_lsb)
    @reg_dacpwd_force.setter
    def reg_dacpwd_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dacpwd_force_msb, self.__reg_dacpwd_force_lsb, value)

    @property
    def reg_adcpwd_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcpwd_force_en_msb, self.__reg_adcpwd_force_en_lsb)
    @reg_adcpwd_force_en.setter
    def reg_adcpwd_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcpwd_force_en_msb, self.__reg_adcpwd_force_en_lsb, value)

    @property
    def reg_adcpwd_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adcpwd_force_msb, self.__reg_adcpwd_force_lsb)
    @reg_adcpwd_force.setter
    def reg_adcpwd_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adcpwd_force_msb, self.__reg_adcpwd_force_lsb, value)

    @property
    def reg_txon_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txon_force_en_msb, self.__reg_txon_force_en_lsb)
    @reg_txon_force_en.setter
    def reg_txon_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txon_force_en_msb, self.__reg_txon_force_en_lsb, value)

    @property
    def reg_txon_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txon_force_msb, self.__reg_txon_force_lsb)
    @reg_txon_force.setter
    def reg_txon_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txon_force_msb, self.__reg_txon_force_lsb, value)

    @property
    def reg_rxon_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxon_force_en_msb, self.__reg_rxon_force_en_lsb)
    @reg_rxon_force_en.setter
    def reg_rxon_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxon_force_en_msb, self.__reg_rxon_force_en_lsb, value)

    @property
    def reg_rxon_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rxon_force_msb, self.__reg_rxon_force_lsb)
    @reg_rxon_force.setter
    def reg_rxon_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rxon_force_msb, self.__reg_rxon_force_lsb, value)

    @property
    def reg_bt_mode_on_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bt_mode_on_force_en_msb, self.__reg_bt_mode_on_force_en_lsb)
    @reg_bt_mode_on_force_en.setter
    def reg_bt_mode_on_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bt_mode_on_force_en_msb, self.__reg_bt_mode_on_force_en_lsb, value)

    @property
    def reg_bt_mode_on_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_bt_mode_on_force_msb, self.__reg_bt_mode_on_force_lsb)
    @reg_bt_mode_on_force.setter
    def reg_bt_mode_on_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_bt_mode_on_force_msb, self.__reg_bt_mode_on_force_lsb, value)

    @property
    def reg_dac_on_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dac_on_force_en_msb, self.__reg_dac_on_force_en_lsb)
    @reg_dac_on_force_en.setter
    def reg_dac_on_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dac_on_force_en_msb, self.__reg_dac_on_force_en_lsb, value)

    @property
    def reg_dac_on_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dac_on_force_msb, self.__reg_dac_on_force_lsb)
    @reg_dac_on_force.setter
    def reg_dac_on_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dac_on_force_msb, self.__reg_dac_on_force_lsb, value)

    @property
    def reg_adc_on_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_on_force_en_msb, self.__reg_adc_on_force_en_lsb)
    @reg_adc_on_force_en.setter
    def reg_adc_on_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_on_force_en_msb, self.__reg_adc_on_force_en_lsb, value)

    @property
    def reg_adc_on_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_adc_on_force_msb, self.__reg_adc_on_force_lsb)
    @reg_adc_on_force.setter
    def reg_adc_on_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_adc_on_force_msb, self.__reg_adc_on_force_lsb, value)
class FE_PUBS_RD0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0xa4
        self.__r_bb_pbus_2_bt_rx_lsb = 18
        self.__r_bb_pbus_2_bt_rx_msb = 26
        self.__r_bb_pbus_2_wifi_rx_lsb = 9
        self.__r_bb_pbus_2_wifi_rx_msb = 17
        self.__r_bb_pbus_2_bt_tx_lsb = 0
        self.__r_bb_pbus_2_bt_tx_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def r_bb_pbus_2_bt_rx(self):
        return self.__MEM.rdm(self.__addr, self.__r_bb_pbus_2_bt_rx_msb, self.__r_bb_pbus_2_bt_rx_lsb)
    @r_bb_pbus_2_bt_rx.setter
    def r_bb_pbus_2_bt_rx(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_bb_pbus_2_bt_rx_msb, self.__r_bb_pbus_2_bt_rx_lsb, value)

    @property
    def r_bb_pbus_2_wifi_rx(self):
        return self.__MEM.rdm(self.__addr, self.__r_bb_pbus_2_wifi_rx_msb, self.__r_bb_pbus_2_wifi_rx_lsb)
    @r_bb_pbus_2_wifi_rx.setter
    def r_bb_pbus_2_wifi_rx(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_bb_pbus_2_wifi_rx_msb, self.__r_bb_pbus_2_wifi_rx_lsb, value)

    @property
    def r_bb_pbus_2_bt_tx(self):
        return self.__MEM.rdm(self.__addr, self.__r_bb_pbus_2_bt_tx_msb, self.__r_bb_pbus_2_bt_tx_lsb)
    @r_bb_pbus_2_bt_tx.setter
    def r_bb_pbus_2_bt_tx(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_bb_pbus_2_bt_tx_msb, self.__r_bb_pbus_2_bt_tx_lsb, value)
class FE_PUBS_RD1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0xa8
        self.__r_bb_pbus_2_wifi_tx_lsb = 18
        self.__r_bb_pbus_2_wifi_tx_msb = 26
        self.__r_rfrx_pbus_1_lsb = 9
        self.__r_rfrx_pbus_1_msb = 17
        self.__r_bb_pbus_1_lsb = 0
        self.__r_bb_pbus_1_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def r_bb_pbus_2_wifi_tx(self):
        return self.__MEM.rdm(self.__addr, self.__r_bb_pbus_2_wifi_tx_msb, self.__r_bb_pbus_2_wifi_tx_lsb)
    @r_bb_pbus_2_wifi_tx.setter
    def r_bb_pbus_2_wifi_tx(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_bb_pbus_2_wifi_tx_msb, self.__r_bb_pbus_2_wifi_tx_lsb, value)

    @property
    def r_rfrx_pbus_1(self):
        return self.__MEM.rdm(self.__addr, self.__r_rfrx_pbus_1_msb, self.__r_rfrx_pbus_1_lsb)
    @r_rfrx_pbus_1.setter
    def r_rfrx_pbus_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_rfrx_pbus_1_msb, self.__r_rfrx_pbus_1_lsb, value)

    @property
    def r_bb_pbus_1(self):
        return self.__MEM.rdm(self.__addr, self.__r_bb_pbus_1_msb, self.__r_bb_pbus_1_lsb)
    @r_bb_pbus_1.setter
    def r_bb_pbus_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_bb_pbus_1_msb, self.__r_bb_pbus_1_lsb, value)
class FE_PUBS_RD2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0xac
        self.__r_bb_pbus_2_lsb = 18
        self.__r_bb_pbus_2_msb = 26
        self.__r_dcoi_pbus_1_lsb = 9
        self.__r_dcoi_pbus_1_msb = 17
        self.__r_dcoi_pbus_2_lsb = 0
        self.__r_dcoi_pbus_2_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def r_bb_pbus_2(self):
        return self.__MEM.rdm(self.__addr, self.__r_bb_pbus_2_msb, self.__r_bb_pbus_2_lsb)
    @r_bb_pbus_2.setter
    def r_bb_pbus_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_bb_pbus_2_msb, self.__r_bb_pbus_2_lsb, value)

    @property
    def r_dcoi_pbus_1(self):
        return self.__MEM.rdm(self.__addr, self.__r_dcoi_pbus_1_msb, self.__r_dcoi_pbus_1_lsb)
    @r_dcoi_pbus_1.setter
    def r_dcoi_pbus_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_dcoi_pbus_1_msb, self.__r_dcoi_pbus_1_lsb, value)

    @property
    def r_dcoi_pbus_2(self):
        return self.__MEM.rdm(self.__addr, self.__r_dcoi_pbus_2_msb, self.__r_dcoi_pbus_2_lsb)
    @r_dcoi_pbus_2.setter
    def r_dcoi_pbus_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_dcoi_pbus_2_msb, self.__r_dcoi_pbus_2_lsb, value)
class FE_PUBS_RD3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0xb0
        self.__cfg_req_fail_h_lsb = 27
        self.__cfg_req_fail_h_msb = 30
        self.__r_dcoq_pbus_1_lsb = 18
        self.__r_dcoq_pbus_1_msb = 26
        self.__r_dcoq_pbus_2_lsb = 9
        self.__r_dcoq_pbus_2_msb = 17
        self.__r_txrf1_pbus_1_lsb = 0
        self.__r_txrf1_pbus_1_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def cfg_req_fail_h(self):
        return self.__MEM.rdm(self.__addr, self.__cfg_req_fail_h_msb, self.__cfg_req_fail_h_lsb)
    @cfg_req_fail_h.setter
    def cfg_req_fail_h(self, value):
        return self.__MEM.wrm(self.__addr, self.__cfg_req_fail_h_msb, self.__cfg_req_fail_h_lsb, value)

    @property
    def r_dcoq_pbus_1(self):
        return self.__MEM.rdm(self.__addr, self.__r_dcoq_pbus_1_msb, self.__r_dcoq_pbus_1_lsb)
    @r_dcoq_pbus_1.setter
    def r_dcoq_pbus_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_dcoq_pbus_1_msb, self.__r_dcoq_pbus_1_lsb, value)

    @property
    def r_dcoq_pbus_2(self):
        return self.__MEM.rdm(self.__addr, self.__r_dcoq_pbus_2_msb, self.__r_dcoq_pbus_2_lsb)
    @r_dcoq_pbus_2.setter
    def r_dcoq_pbus_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_dcoq_pbus_2_msb, self.__r_dcoq_pbus_2_lsb, value)

    @property
    def r_txrf1_pbus_1(self):
        return self.__MEM.rdm(self.__addr, self.__r_txrf1_pbus_1_msb, self.__r_txrf1_pbus_1_lsb)
    @r_txrf1_pbus_1.setter
    def r_txrf1_pbus_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_txrf1_pbus_1_msb, self.__r_txrf1_pbus_1_lsb, value)
class FE_PUBS_RD4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0xb4
        self.__cfg_req_fail_l_lsb = 23
        self.__cfg_req_fail_l_msb = 31
        self.__test_fail_lsb = 22
        self.__test_fail_msb = 22
        self.__cfg_req_d1_lsb = 9
        self.__cfg_req_d1_msb = 21
        self.__r_txrf2_pbus_1_lsb = 0
        self.__r_txrf2_pbus_1_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def cfg_req_fail_l(self):
        return self.__MEM.rdm(self.__addr, self.__cfg_req_fail_l_msb, self.__cfg_req_fail_l_lsb)
    @cfg_req_fail_l.setter
    def cfg_req_fail_l(self, value):
        return self.__MEM.wrm(self.__addr, self.__cfg_req_fail_l_msb, self.__cfg_req_fail_l_lsb, value)

    @property
    def test_fail(self):
        return self.__MEM.rdm(self.__addr, self.__test_fail_msb, self.__test_fail_lsb)
    @test_fail.setter
    def test_fail(self, value):
        return self.__MEM.wrm(self.__addr, self.__test_fail_msb, self.__test_fail_lsb, value)

    @property
    def cfg_req_d1(self):
        return self.__MEM.rdm(self.__addr, self.__cfg_req_d1_msb, self.__cfg_req_d1_lsb)
    @cfg_req_d1.setter
    def cfg_req_d1(self, value):
        return self.__MEM.wrm(self.__addr, self.__cfg_req_d1_msb, self.__cfg_req_d1_lsb, value)

    @property
    def r_txrf2_pbus_1(self):
        return self.__MEM.rdm(self.__addr, self.__r_txrf2_pbus_1_msb, self.__r_txrf2_pbus_1_lsb)
    @r_txrf2_pbus_1.setter
    def r_txrf2_pbus_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__r_txrf2_pbus_1_msb, self.__r_txrf2_pbus_1_lsb, value)
class FE_TX_TEST_CTRL_0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0xb8
        self.__reg_tx_test_ctrl0_lsb = 0
        self.__reg_tx_test_ctrl0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_test_ctrl0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_test_ctrl0_msb, self.__reg_tx_test_ctrl0_lsb)
    @reg_tx_test_ctrl0.setter
    def reg_tx_test_ctrl0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_test_ctrl0_msb, self.__reg_tx_test_ctrl0_lsb, value)
class FE_TX_TEST_CTRL_1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0xbc
        self.__reg_tx_test_ctrl1_lsb = 0
        self.__reg_tx_test_ctrl1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_test_ctrl1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_test_ctrl1_msb, self.__reg_tx_test_ctrl1_lsb)
    @reg_tx_test_ctrl1.setter
    def reg_tx_test_ctrl1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_test_ctrl1_msb, self.__reg_tx_test_ctrl1_lsb, value)
class FE_TX_TEST_CTRL_2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0xc0
        self.__reg_tx_test_ctrl2_lsb = 0
        self.__reg_tx_test_ctrl2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_test_ctrl2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_test_ctrl2_msb, self.__reg_tx_test_ctrl2_lsb)
    @reg_tx_test_ctrl2.setter
    def reg_tx_test_ctrl2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_test_ctrl2_msb, self.__reg_tx_test_ctrl2_lsb, value)
class FE_TX_TEST_CTRL_3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0xc4
        self.__reg_tx_test_ctrl3_lsb = 0
        self.__reg_tx_test_ctrl3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_test_ctrl3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_test_ctrl3_msb, self.__reg_tx_test_ctrl3_lsb)
    @reg_tx_test_ctrl3.setter
    def reg_tx_test_ctrl3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_test_ctrl3_msb, self.__reg_tx_test_ctrl3_lsb, value)
class FE_IQ_RESULT_2_1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0xcc
        self.__iq_est_mult2_ii_lsb = 0
        self.__iq_est_mult2_ii_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def iq_est_mult2_ii(self):
        return self.__MEM.rdm(self.__addr, self.__iq_est_mult2_ii_msb, self.__iq_est_mult2_ii_lsb)
    @iq_est_mult2_ii.setter
    def iq_est_mult2_ii(self, value):
        return self.__MEM.wrm(self.__addr, self.__iq_est_mult2_ii_msb, self.__iq_est_mult2_ii_lsb, value)
class FE_IQ_RESULT_2_2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0xd0
        self.__iq_est_mult2_iq_lsb = 0
        self.__iq_est_mult2_iq_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def iq_est_mult2_iq(self):
        return self.__MEM.rdm(self.__addr, self.__iq_est_mult2_iq_msb, self.__iq_est_mult2_iq_lsb)
    @iq_est_mult2_iq.setter
    def iq_est_mult2_iq(self, value):
        return self.__MEM.wrm(self.__addr, self.__iq_est_mult2_iq_msb, self.__iq_est_mult2_iq_lsb, value)
class FE_IQ_RESULT_2_3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0xd4
        self.__iq_est_mult2_qi_lsb = 0
        self.__iq_est_mult2_qi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def iq_est_mult2_qi(self):
        return self.__MEM.rdm(self.__addr, self.__iq_est_mult2_qi_msb, self.__iq_est_mult2_qi_lsb)
    @iq_est_mult2_qi.setter
    def iq_est_mult2_qi(self, value):
        return self.__MEM.wrm(self.__addr, self.__iq_est_mult2_qi_msb, self.__iq_est_mult2_qi_lsb, value)
class FE_IQ_RESULT_2_4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0xd8
        self.__iq_est_mult2_qq_lsb = 0
        self.__iq_est_mult2_qq_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def iq_est_mult2_qq(self):
        return self.__MEM.rdm(self.__addr, self.__iq_est_mult2_qq_msb, self.__iq_est_mult2_qq_lsb)
    @iq_est_mult2_qq.setter
    def iq_est_mult2_qq(self, value):
        return self.__MEM.wrm(self.__addr, self.__iq_est_mult2_qq_msb, self.__iq_est_mult2_qq_lsb, value)
class FE_IQ_RESULT_DC_I(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0xdc
        self.__iq_est_mult_dc_i_lsb = 0
        self.__iq_est_mult_dc_i_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def iq_est_mult_dc_i(self):
        return self.__MEM.rdm(self.__addr, self.__iq_est_mult_dc_i_msb, self.__iq_est_mult_dc_i_lsb)
    @iq_est_mult_dc_i.setter
    def iq_est_mult_dc_i(self, value):
        return self.__MEM.wrm(self.__addr, self.__iq_est_mult_dc_i_msb, self.__iq_est_mult_dc_i_lsb, value)
class FE_IQ_RESULT_DC_Q(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0xe0
        self.__iq_est_mult_dc_q_lsb = 0
        self.__iq_est_mult_dc_q_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def iq_est_mult_dc_q(self):
        return self.__MEM.rdm(self.__addr, self.__iq_est_mult_dc_q_msb, self.__iq_est_mult_dc_q_lsb)
    @iq_est_mult_dc_q.setter
    def iq_est_mult_dc_q(self, value):
        return self.__MEM.wrm(self.__addr, self.__iq_est_mult_dc_q_msb, self.__iq_est_mult_dc_q_lsb, value)
class FE_IQ_RESULT_PWR(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0xe4
        self.__iq_est_mult_pwr_lsb = 0
        self.__iq_est_mult_pwr_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def iq_est_mult_pwr(self):
        return self.__MEM.rdm(self.__addr, self.__iq_est_mult_pwr_msb, self.__iq_est_mult_pwr_lsb)
    @iq_est_mult_pwr.setter
    def iq_est_mult_pwr(self, value):
        return self.__MEM.wrm(self.__addr, self.__iq_est_mult_pwr_msb, self.__iq_est_mult_pwr_lsb, value)
class FE_IQ_RESULT_PWR_I(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0xec
        self.__iq_est_mult_pwr_i_lsb = 0
        self.__iq_est_mult_pwr_i_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def iq_est_mult_pwr_i(self):
        return self.__MEM.rdm(self.__addr, self.__iq_est_mult_pwr_i_msb, self.__iq_est_mult_pwr_i_lsb)
    @iq_est_mult_pwr_i.setter
    def iq_est_mult_pwr_i(self, value):
        return self.__MEM.wrm(self.__addr, self.__iq_est_mult_pwr_i_msb, self.__iq_est_mult_pwr_i_lsb, value)
class FE_IQ_RESULT_PWR_Q(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0xf0
        self.__iq_est_mult_pwr_q_lsb = 0
        self.__iq_est_mult_pwr_q_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def iq_est_mult_pwr_q(self):
        return self.__MEM.rdm(self.__addr, self.__iq_est_mult_pwr_q_msb, self.__iq_est_mult_pwr_q_lsb)
    @iq_est_mult_pwr_q.setter
    def iq_est_mult_pwr_q(self, value):
        return self.__MEM.wrm(self.__addr, self.__iq_est_mult_pwr_q_msb, self.__iq_est_mult_pwr_q_lsb, value)
class FE_IQ_RESULT_PWR_IQ(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0xf4
        self.__iq_est_mult_pwr_iq_lsb = 0
        self.__iq_est_mult_pwr_iq_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def iq_est_mult_pwr_iq(self):
        return self.__MEM.rdm(self.__addr, self.__iq_est_mult_pwr_iq_msb, self.__iq_est_mult_pwr_iq_lsb)
    @iq_est_mult_pwr_iq.setter
    def iq_est_mult_pwr_iq(self, value):
        return self.__MEM.wrm(self.__addr, self.__iq_est_mult_pwr_iq_msb, self.__iq_est_mult_pwr_iq_lsb, value)
class FE_NOUSE(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0xf8
        self.__reg_fe_nouse_lsb = 0
        self.__reg_fe_nouse_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_fe_nouse(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fe_nouse_msb, self.__reg_fe_nouse_lsb)
    @reg_fe_nouse.setter
    def reg_fe_nouse(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fe_nouse_msb, self.__reg_fe_nouse_lsb, value)
class FE_NOUSE_2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = FE_BASE + 0xfc
        self.__reg_fe_clk_en_lsb = 28
        self.__reg_fe_clk_en_msb = 28
        self.__reg_fe_date_lsb = 0
        self.__reg_fe_date_msb = 27
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_fe_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fe_clk_en_msb, self.__reg_fe_clk_en_lsb)
    @reg_fe_clk_en.setter
    def reg_fe_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fe_clk_en_msb, self.__reg_fe_clk_en_lsb, value)

    @property
    def reg_fe_date(self):
        return self.__MEM.rdm(self.__addr, self.__reg_fe_date_msb, self.__reg_fe_date_lsb)
    @reg_fe_date.setter
    def reg_fe_date(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_fe_date_msb, self.__reg_fe_date_lsb, value)
    @property
    def default_value(self):
        return 0x1604201
