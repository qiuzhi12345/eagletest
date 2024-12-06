from hal.common import *
from hal.hwregister.hwreg.ESP32.addr_base import *
class SARADC(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.SAR_READ_CTRL = SAR_READ_CTRL(self.channel, self.chipv)
        self.SAR_READ_STATUS1 = SAR_READ_STATUS1(self.channel, self.chipv)
        self.SAR_MEAS_WAIT1 = SAR_MEAS_WAIT1(self.channel, self.chipv)
        self.SAR_MEAS_WAIT2 = SAR_MEAS_WAIT2(self.channel, self.chipv)
        self.SAR_MEAS_CTRL = SAR_MEAS_CTRL(self.channel, self.chipv)
        self.SAR_READ_STATUS2 = SAR_READ_STATUS2(self.channel, self.chipv)
        self.SAR_FSM_SLEEP_CYC0 = SAR_FSM_SLEEP_CYC0(self.channel, self.chipv)
        self.SAR_FSM_SLEEP_CYC1 = SAR_FSM_SLEEP_CYC1(self.channel, self.chipv)
        self.SAR_FSM_SLEEP_CYC2 = SAR_FSM_SLEEP_CYC2(self.channel, self.chipv)
        self.SAR_FSM_SLEEP_CYC3 = SAR_FSM_SLEEP_CYC3(self.channel, self.chipv)
        self.SAR_FSM_SLEEP_CYC4 = SAR_FSM_SLEEP_CYC4(self.channel, self.chipv)
        self.SAR_START_FORCE = SAR_START_FORCE(self.channel, self.chipv)
        self.SAR_MEM_WR_CTRL = SAR_MEM_WR_CTRL(self.channel, self.chipv)
        self.SAR_ATTEN1 = SAR_ATTEN1(self.channel, self.chipv)
        self.SAR_ATTEN2 = SAR_ATTEN2(self.channel, self.chipv)
        self.SAR_SLAVE_ADDR1 = SAR_SLAVE_ADDR1(self.channel, self.chipv)
        self.SAR_SLAVE_ADDR2 = SAR_SLAVE_ADDR2(self.channel, self.chipv)
        self.SAR_SLAVE_ADDR3 = SAR_SLAVE_ADDR3(self.channel, self.chipv)
        self.SAR_SLAVE_ADDR4 = SAR_SLAVE_ADDR4(self.channel, self.chipv)
        self.SAR_TSENS_CTRL = SAR_TSENS_CTRL(self.channel, self.chipv)
        self.SAR_I2C_CTRL = SAR_I2C_CTRL(self.channel, self.chipv)
        self.SAR_MEAS_START1 = SAR_MEAS_START1(self.channel, self.chipv)
        self.SAR_TOUCH_CTRL1 = SAR_TOUCH_CTRL1(self.channel, self.chipv)
        self.SAR_TOUCH_THRES1 = SAR_TOUCH_THRES1(self.channel, self.chipv)
        self.SAR_TOUCH_THRES2 = SAR_TOUCH_THRES2(self.channel, self.chipv)
        self.SAR_TOUCH_THRES3 = SAR_TOUCH_THRES3(self.channel, self.chipv)
        self.SAR_TOUCH_THRES4 = SAR_TOUCH_THRES4(self.channel, self.chipv)
        self.SAR_TOUCH_THRES5 = SAR_TOUCH_THRES5(self.channel, self.chipv)
        self.SAR_TOUCH_OUT1 = SAR_TOUCH_OUT1(self.channel, self.chipv)
        self.SAR_TOUCH_OUT2 = SAR_TOUCH_OUT2(self.channel, self.chipv)
        self.SAR_TOUCH_OUT3 = SAR_TOUCH_OUT3(self.channel, self.chipv)
        self.SAR_TOUCH_OUT4 = SAR_TOUCH_OUT4(self.channel, self.chipv)
        self.SAR_TOUCH_OUT5 = SAR_TOUCH_OUT5(self.channel, self.chipv)
        self.SAR_TOUCH_CTRL2 = SAR_TOUCH_CTRL2(self.channel, self.chipv)
        self.SAR_TOUCH_ENABLE = SAR_TOUCH_ENABLE(self.channel, self.chipv)
        self.SAR_READ_CTRL2 = SAR_READ_CTRL2(self.channel, self.chipv)
        self.SAR_MEAS_START2 = SAR_MEAS_START2(self.channel, self.chipv)
        self.SAR_DAC_CTRL1 = SAR_DAC_CTRL1(self.channel, self.chipv)
        self.SAR_DAC_CTRL2 = SAR_DAC_CTRL2(self.channel, self.chipv)
        self.SAR_MEAS_CTRL2 = SAR_MEAS_CTRL2(self.channel, self.chipv)
        self.SAR_NOUSE = SAR_NOUSE(self.channel, self.chipv)
        self.SARDATE = SARDATE(self.channel, self.chipv)
class SAR_READ_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x0
        self.__reg_sar1_data_inv_lsb = 28
        self.__reg_sar1_data_inv_msb = 28
        self.__reg_sar1_dig_force_lsb = 27
        self.__reg_sar1_dig_force_msb = 27
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
    def reg_sar1_data_inv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar1_data_inv_msb, self.__reg_sar1_data_inv_lsb)
    @reg_sar1_data_inv.setter
    def reg_sar1_data_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar1_data_inv_msb, self.__reg_sar1_data_inv_lsb, value)

    @property
    def reg_sar1_dig_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar1_dig_force_msb, self.__reg_sar1_dig_force_lsb)
    @reg_sar1_dig_force.setter
    def reg_sar1_dig_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar1_dig_force_msb, self.__reg_sar1_dig_force_lsb, value)

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
class SAR_READ_STATUS1(object):
    def __init__(self, channel, chipv = "ESP32"):
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
class SAR_MEAS_WAIT1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x8
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
class SAR_MEAS_WAIT2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xc
        self.__reg_sar2_rstb_wait_lsb = 20
        self.__reg_sar2_rstb_wait_msb = 27
        self.__reg_force_xpd_sar_lsb = 18
        self.__reg_force_xpd_sar_msb = 19
        self.__reg_force_xpd_amp_lsb = 16
        self.__reg_force_xpd_amp_msb = 17
        self.__reg_sar_amp_wait3_lsb = 0
        self.__reg_sar_amp_wait3_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sar2_rstb_wait(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_rstb_wait_msb, self.__reg_sar2_rstb_wait_lsb)
    @reg_sar2_rstb_wait.setter
    def reg_sar2_rstb_wait(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_rstb_wait_msb, self.__reg_sar2_rstb_wait_lsb, value)

    @property
    def reg_force_xpd_sar(self):
        return self.__MEM.rdm(self.__addr, self.__reg_force_xpd_sar_msb, self.__reg_force_xpd_sar_lsb)
    @reg_force_xpd_sar.setter
    def reg_force_xpd_sar(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_force_xpd_sar_msb, self.__reg_force_xpd_sar_lsb, value)

    @property
    def reg_force_xpd_amp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_force_xpd_amp_msb, self.__reg_force_xpd_amp_lsb)
    @reg_force_xpd_amp.setter
    def reg_force_xpd_amp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_force_xpd_amp_msb, self.__reg_force_xpd_amp_lsb, value)

    @property
    def reg_sar_amp_wait3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar_amp_wait3_msb, self.__reg_sar_amp_wait3_lsb)
    @reg_sar_amp_wait3.setter
    def reg_sar_amp_wait3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar_amp_wait3_msb, self.__reg_sar_amp_wait3_lsb, value)
class SAR_MEAS_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x10
        self.__reg_sar2_xpd_wait_lsb = 24
        self.__reg_sar2_xpd_wait_msb = 31
        self.__reg_sar_rstb_fsm_lsb = 20
        self.__reg_sar_rstb_fsm_msb = 23
        self.__reg_xpd_sar_fsm_lsb = 16
        self.__reg_xpd_sar_fsm_msb = 19
        self.__reg_amp_short_ref_gnd_fsm_lsb = 12
        self.__reg_amp_short_ref_gnd_fsm_msb = 15
        self.__reg_amp_short_ref_fsm_lsb = 8
        self.__reg_amp_short_ref_fsm_msb = 11
        self.__reg_amp_rst_fb_fsm_lsb = 4
        self.__reg_amp_rst_fb_fsm_msb = 7
        self.__reg_xpd_sar_amp_fsm_lsb = 0
        self.__reg_xpd_sar_amp_fsm_msb = 3
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
class SAR_READ_STATUS2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x14
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
class SAR_FSM_SLEEP_CYC0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x18
        self.__reg_sleep_cycles_s0_lsb = 0
        self.__reg_sleep_cycles_s0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sleep_cycles_s0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sleep_cycles_s0_msb, self.__reg_sleep_cycles_s0_lsb)
    @reg_sleep_cycles_s0.setter
    def reg_sleep_cycles_s0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sleep_cycles_s0_msb, self.__reg_sleep_cycles_s0_lsb, value)
class SAR_FSM_SLEEP_CYC1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x1c
        self.__reg_sleep_cycles_s1_lsb = 0
        self.__reg_sleep_cycles_s1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sleep_cycles_s1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sleep_cycles_s1_msb, self.__reg_sleep_cycles_s1_lsb)
    @reg_sleep_cycles_s1.setter
    def reg_sleep_cycles_s1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sleep_cycles_s1_msb, self.__reg_sleep_cycles_s1_lsb, value)
class SAR_FSM_SLEEP_CYC2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x20
        self.__reg_sleep_cycles_s2_lsb = 0
        self.__reg_sleep_cycles_s2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sleep_cycles_s2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sleep_cycles_s2_msb, self.__reg_sleep_cycles_s2_lsb)
    @reg_sleep_cycles_s2.setter
    def reg_sleep_cycles_s2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sleep_cycles_s2_msb, self.__reg_sleep_cycles_s2_lsb, value)
class SAR_FSM_SLEEP_CYC3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x24
        self.__reg_sleep_cycles_s3_lsb = 0
        self.__reg_sleep_cycles_s3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sleep_cycles_s3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sleep_cycles_s3_msb, self.__reg_sleep_cycles_s3_lsb)
    @reg_sleep_cycles_s3.setter
    def reg_sleep_cycles_s3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sleep_cycles_s3_msb, self.__reg_sleep_cycles_s3_lsb, value)
class SAR_FSM_SLEEP_CYC4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x28
        self.__reg_sleep_cycles_s4_lsb = 0
        self.__reg_sleep_cycles_s4_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sleep_cycles_s4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sleep_cycles_s4_msb, self.__reg_sleep_cycles_s4_lsb)
    @reg_sleep_cycles_s4.setter
    def reg_sleep_cycles_s4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sleep_cycles_s4_msb, self.__reg_sleep_cycles_s4_lsb, value)
class SAR_START_FORCE(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x2c
        self.__reg_sar2_pwdet_en_lsb = 24
        self.__reg_sar2_pwdet_en_msb = 24
        self.__reg_sar1_stop_lsb = 23
        self.__reg_sar1_stop_msb = 23
        self.__reg_sar2_stop_lsb = 22
        self.__reg_sar2_stop_msb = 22
        self.__reg_pc_init_lsb = 11
        self.__reg_pc_init_msb = 21
        self.__reg_sarclk_en_lsb = 10
        self.__reg_sarclk_en_msb = 10
        self.__reg_saradc_start_top_lsb = 9
        self.__reg_saradc_start_top_msb = 9
        self.__reg_saradc_force_start_top_lsb = 8
        self.__reg_saradc_force_start_top_msb = 8
        self.__reg_sar2_pwdet_cct_lsb = 5
        self.__reg_sar2_pwdet_cct_msb = 7
        self.__reg_sar2_en_test_lsb = 4
        self.__reg_sar2_en_test_msb = 4
        self.__reg_sar2_bit_width_lsb = 2
        self.__reg_sar2_bit_width_msb = 3
        self.__reg_sar1_bit_width_lsb = 0
        self.__reg_sar1_bit_width_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sar2_pwdet_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_pwdet_en_msb, self.__reg_sar2_pwdet_en_lsb)
    @reg_sar2_pwdet_en.setter
    def reg_sar2_pwdet_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_pwdet_en_msb, self.__reg_sar2_pwdet_en_lsb, value)

    @property
    def reg_sar1_stop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar1_stop_msb, self.__reg_sar1_stop_lsb)
    @reg_sar1_stop.setter
    def reg_sar1_stop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar1_stop_msb, self.__reg_sar1_stop_lsb, value)

    @property
    def reg_sar2_stop(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_stop_msb, self.__reg_sar2_stop_lsb)
    @reg_sar2_stop.setter
    def reg_sar2_stop(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_stop_msb, self.__reg_sar2_stop_lsb, value)

    @property
    def reg_pc_init(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pc_init_msb, self.__reg_pc_init_lsb)
    @reg_pc_init.setter
    def reg_pc_init(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pc_init_msb, self.__reg_pc_init_lsb, value)

    @property
    def reg_sarclk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sarclk_en_msb, self.__reg_sarclk_en_lsb)
    @reg_sarclk_en.setter
    def reg_sarclk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sarclk_en_msb, self.__reg_sarclk_en_lsb, value)

    @property
    def reg_saradc_start_top(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_start_top_msb, self.__reg_saradc_start_top_lsb)
    @reg_saradc_start_top.setter
    def reg_saradc_start_top(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_start_top_msb, self.__reg_saradc_start_top_lsb, value)

    @property
    def reg_saradc_force_start_top(self):
        return self.__MEM.rdm(self.__addr, self.__reg_saradc_force_start_top_msb, self.__reg_saradc_force_start_top_lsb)
    @reg_saradc_force_start_top.setter
    def reg_saradc_force_start_top(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_saradc_force_start_top_msb, self.__reg_saradc_force_start_top_lsb, value)

    @property
    def reg_sar2_pwdet_cct(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_pwdet_cct_msb, self.__reg_sar2_pwdet_cct_lsb)
    @reg_sar2_pwdet_cct.setter
    def reg_sar2_pwdet_cct(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_pwdet_cct_msb, self.__reg_sar2_pwdet_cct_lsb, value)

    @property
    def reg_sar2_en_test(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_en_test_msb, self.__reg_sar2_en_test_lsb)
    @reg_sar2_en_test.setter
    def reg_sar2_en_test(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_en_test_msb, self.__reg_sar2_en_test_lsb, value)

    @property
    def reg_sar2_bit_width(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_bit_width_msb, self.__reg_sar2_bit_width_lsb)
    @reg_sar2_bit_width.setter
    def reg_sar2_bit_width(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_bit_width_msb, self.__reg_sar2_bit_width_lsb, value)

    @property
    def reg_sar1_bit_width(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar1_bit_width_msb, self.__reg_sar1_bit_width_lsb)
    @reg_sar1_bit_width.setter
    def reg_sar1_bit_width(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar1_bit_width_msb, self.__reg_sar1_bit_width_lsb, value)
class SAR_MEM_WR_CTRL(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x30
        self.__rtc_mem_wr_offst_clr_lsb = 22
        self.__rtc_mem_wr_offst_clr_msb = 22
        self.__reg_mem_wr_addr_size_lsb = 11
        self.__reg_mem_wr_addr_size_msb = 21
        self.__reg_mem_wr_addr_init_lsb = 0
        self.__reg_mem_wr_addr_init_msb = 10
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rtc_mem_wr_offst_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rtc_mem_wr_offst_clr_msb, self.__rtc_mem_wr_offst_clr_lsb)
    @rtc_mem_wr_offst_clr.setter
    def rtc_mem_wr_offst_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtc_mem_wr_offst_clr_msb, self.__rtc_mem_wr_offst_clr_lsb, value)

    @property
    def reg_mem_wr_addr_size(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mem_wr_addr_size_msb, self.__reg_mem_wr_addr_size_lsb)
    @reg_mem_wr_addr_size.setter
    def reg_mem_wr_addr_size(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mem_wr_addr_size_msb, self.__reg_mem_wr_addr_size_lsb, value)

    @property
    def reg_mem_wr_addr_init(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mem_wr_addr_init_msb, self.__reg_mem_wr_addr_init_lsb)
    @reg_mem_wr_addr_init.setter
    def reg_mem_wr_addr_init(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mem_wr_addr_init_msb, self.__reg_mem_wr_addr_init_lsb, value)
class SAR_ATTEN1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x34
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
class SAR_ATTEN2(object):
    def __init__(self, channel, chipv = "ESP32"):
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
class SAR_SLAVE_ADDR1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x3c
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x40
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x44
        self.__reg_tsens_rdy_out_lsb = 30
        self.__reg_tsens_rdy_out_msb = 30
        self.__reg_tsens_out_lsb = 22
        self.__reg_tsens_out_msb = 29
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
    def reg_tsens_rdy_out(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsens_rdy_out_msb, self.__reg_tsens_rdy_out_lsb)
    @reg_tsens_rdy_out.setter
    def reg_tsens_rdy_out(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsens_rdy_out_msb, self.__reg_tsens_rdy_out_lsb, value)

    @property
    def reg_tsens_out(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsens_out_msb, self.__reg_tsens_out_lsb)
    @reg_tsens_out.setter
    def reg_tsens_out(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsens_out_msb, self.__reg_tsens_out_lsb, value)

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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x48
        self.__reg_i2c_done_lsb = 30
        self.__reg_i2c_done_msb = 30
        self.__reg_i2c_rdata_lsb = 22
        self.__reg_i2c_rdata_msb = 29
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
    def reg_i2c_done(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2c_done_msb, self.__reg_i2c_done_lsb)
    @reg_i2c_done.setter
    def reg_i2c_done(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2c_done_msb, self.__reg_i2c_done_lsb, value)

    @property
    def reg_i2c_rdata(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2c_rdata_msb, self.__reg_i2c_rdata_lsb)
    @reg_i2c_rdata.setter
    def reg_i2c_rdata(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2c_rdata_msb, self.__reg_i2c_rdata_lsb, value)

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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x4c
        self.__reg_tsens_dump_out_lsb = 26
        self.__reg_tsens_dump_out_msb = 26
        self.__reg_tsens_power_up_force_lsb = 25
        self.__reg_tsens_power_up_force_msb = 25
        self.__reg_tsens_power_up_lsb = 24
        self.__reg_tsens_power_up_msb = 24
        self.__reg_tsens_clk_div_lsb = 16
        self.__reg_tsens_clk_div_msb = 23
        self.__reg_tsens_in_inv_lsb = 15
        self.__reg_tsens_in_inv_msb = 15
        self.__reg_tsens_clk_gated_lsb = 14
        self.__reg_tsens_clk_gated_msb = 14
        self.__reg_tsens_clk_inv_lsb = 13
        self.__reg_tsens_clk_inv_msb = 13
        self.__reg_tsens_xpd_force_lsb = 12
        self.__reg_tsens_xpd_force_msb = 12
        self.__reg_tsens_xpd_wait_lsb = 0
        self.__reg_tsens_xpd_wait_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

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
    def reg_tsens_clk_gated(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tsens_clk_gated_msb, self.__reg_tsens_clk_gated_lsb)
    @reg_tsens_clk_gated.setter
    def reg_tsens_clk_gated(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tsens_clk_gated_msb, self.__reg_tsens_clk_gated_lsb, value)

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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x50
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
class SAR_MEAS_START1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x54
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
class SAR_TOUCH_CTRL1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x58
        self.__reg_hall_phase_force_lsb = 27
        self.__reg_hall_phase_force_msb = 27
        self.__reg_xpd_hall_force_lsb = 26
        self.__reg_xpd_hall_force_msb = 26
        self.__reg_touch_out_1en_lsb = 25
        self.__reg_touch_out_1en_msb = 25
        self.__reg_touch_out_sel_lsb = 24
        self.__reg_touch_out_sel_msb = 24
        self.__reg_touch_xpd_wait_lsb = 16
        self.__reg_touch_xpd_wait_msb = 23
        self.__reg_touch_meas_delay_lsb = 0
        self.__reg_touch_meas_delay_msb = 15
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
    def reg_xpd_hall_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xpd_hall_force_msb, self.__reg_xpd_hall_force_lsb)
    @reg_xpd_hall_force.setter
    def reg_xpd_hall_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xpd_hall_force_msb, self.__reg_xpd_hall_force_lsb, value)

    @property
    def reg_touch_out_1en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_out_1en_msb, self.__reg_touch_out_1en_lsb)
    @reg_touch_out_1en.setter
    def reg_touch_out_1en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_out_1en_msb, self.__reg_touch_out_1en_lsb, value)

    @property
    def reg_touch_out_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_out_sel_msb, self.__reg_touch_out_sel_lsb)
    @reg_touch_out_sel.setter
    def reg_touch_out_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_out_sel_msb, self.__reg_touch_out_sel_lsb, value)

    @property
    def reg_touch_xpd_wait(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_xpd_wait_msb, self.__reg_touch_xpd_wait_lsb)
    @reg_touch_xpd_wait.setter
    def reg_touch_xpd_wait(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_xpd_wait_msb, self.__reg_touch_xpd_wait_lsb, value)

    @property
    def reg_touch_meas_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_meas_delay_msb, self.__reg_touch_meas_delay_lsb)
    @reg_touch_meas_delay.setter
    def reg_touch_meas_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_meas_delay_msb, self.__reg_touch_meas_delay_lsb, value)
class SAR_TOUCH_THRES1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x5c
        self.__reg_touch_out_th0_lsb = 16
        self.__reg_touch_out_th0_msb = 31
        self.__reg_touch_out_th1_lsb = 0
        self.__reg_touch_out_th1_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_out_th0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_out_th0_msb, self.__reg_touch_out_th0_lsb)
    @reg_touch_out_th0.setter
    def reg_touch_out_th0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_out_th0_msb, self.__reg_touch_out_th0_lsb, value)

    @property
    def reg_touch_out_th1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_out_th1_msb, self.__reg_touch_out_th1_lsb)
    @reg_touch_out_th1.setter
    def reg_touch_out_th1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_out_th1_msb, self.__reg_touch_out_th1_lsb, value)
class SAR_TOUCH_THRES2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x60
        self.__reg_touch_out_th2_lsb = 16
        self.__reg_touch_out_th2_msb = 31
        self.__reg_touch_out_th3_lsb = 0
        self.__reg_touch_out_th3_msb = 15
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

    @property
    def reg_touch_out_th3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_out_th3_msb, self.__reg_touch_out_th3_lsb)
    @reg_touch_out_th3.setter
    def reg_touch_out_th3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_out_th3_msb, self.__reg_touch_out_th3_lsb, value)
class SAR_TOUCH_THRES3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x64
        self.__reg_touch_out_th4_lsb = 16
        self.__reg_touch_out_th4_msb = 31
        self.__reg_touch_out_th5_lsb = 0
        self.__reg_touch_out_th5_msb = 15
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

    @property
    def reg_touch_out_th5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_out_th5_msb, self.__reg_touch_out_th5_lsb)
    @reg_touch_out_th5.setter
    def reg_touch_out_th5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_out_th5_msb, self.__reg_touch_out_th5_lsb, value)
class SAR_TOUCH_THRES4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x68
        self.__reg_touch_out_th6_lsb = 16
        self.__reg_touch_out_th6_msb = 31
        self.__reg_touch_out_th7_lsb = 0
        self.__reg_touch_out_th7_msb = 15
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

    @property
    def reg_touch_out_th7(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_out_th7_msb, self.__reg_touch_out_th7_lsb)
    @reg_touch_out_th7.setter
    def reg_touch_out_th7(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_out_th7_msb, self.__reg_touch_out_th7_lsb, value)
class SAR_TOUCH_THRES5(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x6c
        self.__reg_touch_out_th8_lsb = 16
        self.__reg_touch_out_th8_msb = 31
        self.__reg_touch_out_th9_lsb = 0
        self.__reg_touch_out_th9_msb = 15
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

    @property
    def reg_touch_out_th9(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_out_th9_msb, self.__reg_touch_out_th9_lsb)
    @reg_touch_out_th9.setter
    def reg_touch_out_th9(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_out_th9_msb, self.__reg_touch_out_th9_lsb, value)
class SAR_TOUCH_OUT1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x70
        self.__reg_touch_meas_out0_lsb = 16
        self.__reg_touch_meas_out0_msb = 31
        self.__reg_touch_meas_out1_lsb = 0
        self.__reg_touch_meas_out1_msb = 15
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

    @property
    def reg_touch_meas_out1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_meas_out1_msb, self.__reg_touch_meas_out1_lsb)
    @reg_touch_meas_out1.setter
    def reg_touch_meas_out1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_meas_out1_msb, self.__reg_touch_meas_out1_lsb, value)
class SAR_TOUCH_OUT2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x74
        self.__reg_touch_meas_out2_lsb = 16
        self.__reg_touch_meas_out2_msb = 31
        self.__reg_touch_meas_out3_lsb = 0
        self.__reg_touch_meas_out3_msb = 15
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

    @property
    def reg_touch_meas_out3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_meas_out3_msb, self.__reg_touch_meas_out3_lsb)
    @reg_touch_meas_out3.setter
    def reg_touch_meas_out3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_meas_out3_msb, self.__reg_touch_meas_out3_lsb, value)
class SAR_TOUCH_OUT3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x78
        self.__reg_touch_meas_out4_lsb = 16
        self.__reg_touch_meas_out4_msb = 31
        self.__reg_touch_meas_out5_lsb = 0
        self.__reg_touch_meas_out5_msb = 15
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

    @property
    def reg_touch_meas_out5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_meas_out5_msb, self.__reg_touch_meas_out5_lsb)
    @reg_touch_meas_out5.setter
    def reg_touch_meas_out5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_meas_out5_msb, self.__reg_touch_meas_out5_lsb, value)
class SAR_TOUCH_OUT4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x7c
        self.__reg_touch_meas_out6_lsb = 16
        self.__reg_touch_meas_out6_msb = 31
        self.__reg_touch_meas_out7_lsb = 0
        self.__reg_touch_meas_out7_msb = 15
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

    @property
    def reg_touch_meas_out7(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_meas_out7_msb, self.__reg_touch_meas_out7_lsb)
    @reg_touch_meas_out7.setter
    def reg_touch_meas_out7(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_meas_out7_msb, self.__reg_touch_meas_out7_lsb, value)
class SAR_TOUCH_OUT5(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x80
        self.__reg_touch_meas_out8_lsb = 16
        self.__reg_touch_meas_out8_msb = 31
        self.__reg_touch_meas_out9_lsb = 0
        self.__reg_touch_meas_out9_msb = 15
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

    @property
    def reg_touch_meas_out9(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_meas_out9_msb, self.__reg_touch_meas_out9_lsb)
    @reg_touch_meas_out9.setter
    def reg_touch_meas_out9(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_meas_out9_msb, self.__reg_touch_meas_out9_lsb, value)
class SAR_TOUCH_CTRL2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x84
        self.__touch_meas_en_clr_lsb = 30
        self.__touch_meas_en_clr_msb = 30
        self.__reg_touch_sleep_cycles_lsb = 14
        self.__reg_touch_sleep_cycles_msb = 29
        self.__reg_touch_start_force_lsb = 13
        self.__reg_touch_start_force_msb = 13
        self.__reg_touch_start_en_lsb = 12
        self.__reg_touch_start_en_msb = 12
        self.__reg_touch_start_fsm_en_lsb = 11
        self.__reg_touch_start_fsm_en_msb = 11
        self.__touch_meas_done_lsb = 10
        self.__touch_meas_done_msb = 10
        self.__reg_touch_meas_en_lsb = 0
        self.__reg_touch_meas_en_msb = 9
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def touch_meas_en_clr(self):
        return self.__MEM.rdm(self.__addr, self.__touch_meas_en_clr_msb, self.__touch_meas_en_clr_lsb)
    @touch_meas_en_clr.setter
    def touch_meas_en_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_meas_en_clr_msb, self.__touch_meas_en_clr_lsb, value)

    @property
    def reg_touch_sleep_cycles(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_sleep_cycles_msb, self.__reg_touch_sleep_cycles_lsb)
    @reg_touch_sleep_cycles.setter
    def reg_touch_sleep_cycles(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_sleep_cycles_msb, self.__reg_touch_sleep_cycles_lsb, value)

    @property
    def reg_touch_start_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_start_force_msb, self.__reg_touch_start_force_lsb)
    @reg_touch_start_force.setter
    def reg_touch_start_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_start_force_msb, self.__reg_touch_start_force_lsb, value)

    @property
    def reg_touch_start_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_start_en_msb, self.__reg_touch_start_en_lsb)
    @reg_touch_start_en.setter
    def reg_touch_start_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_start_en_msb, self.__reg_touch_start_en_lsb, value)

    @property
    def reg_touch_start_fsm_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_start_fsm_en_msb, self.__reg_touch_start_fsm_en_lsb)
    @reg_touch_start_fsm_en.setter
    def reg_touch_start_fsm_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_start_fsm_en_msb, self.__reg_touch_start_fsm_en_lsb, value)

    @property
    def touch_meas_done(self):
        return self.__MEM.rdm(self.__addr, self.__touch_meas_done_msb, self.__touch_meas_done_lsb)
    @touch_meas_done.setter
    def touch_meas_done(self, value):
        return self.__MEM.wrm(self.__addr, self.__touch_meas_done_msb, self.__touch_meas_done_lsb, value)

    @property
    def reg_touch_meas_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_meas_en_msb, self.__reg_touch_meas_en_lsb)
    @reg_touch_meas_en.setter
    def reg_touch_meas_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_meas_en_msb, self.__reg_touch_meas_en_lsb, value)
class SAR_TOUCH_ENABLE(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x8c
        self.__reg_touch_pad_outen1_lsb = 20
        self.__reg_touch_pad_outen1_msb = 29
        self.__reg_touch_pad_outen2_lsb = 10
        self.__reg_touch_pad_outen2_msb = 19
        self.__reg_touch_pad_worken_lsb = 0
        self.__reg_touch_pad_worken_msb = 9
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_touch_pad_outen1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad_outen1_msb, self.__reg_touch_pad_outen1_lsb)
    @reg_touch_pad_outen1.setter
    def reg_touch_pad_outen1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad_outen1_msb, self.__reg_touch_pad_outen1_lsb, value)

    @property
    def reg_touch_pad_outen2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad_outen2_msb, self.__reg_touch_pad_outen2_lsb)
    @reg_touch_pad_outen2.setter
    def reg_touch_pad_outen2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad_outen2_msb, self.__reg_touch_pad_outen2_lsb, value)

    @property
    def reg_touch_pad_worken(self):
        return self.__MEM.rdm(self.__addr, self.__reg_touch_pad_worken_msb, self.__reg_touch_pad_worken_lsb)
    @reg_touch_pad_worken.setter
    def reg_touch_pad_worken(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_touch_pad_worken_msb, self.__reg_touch_pad_worken_lsb, value)
class SAR_READ_CTRL2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x90
        self.__reg_sar2_data_inv_lsb = 29
        self.__reg_sar2_data_inv_msb = 29
        self.__reg_sar2_dig_force_lsb = 28
        self.__reg_sar2_dig_force_msb = 28
        self.__reg_sar2_pwdet_force_lsb = 27
        self.__reg_sar2_pwdet_force_msb = 27
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
    def reg_sar2_data_inv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_data_inv_msb, self.__reg_sar2_data_inv_lsb)
    @reg_sar2_data_inv.setter
    def reg_sar2_data_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_data_inv_msb, self.__reg_sar2_data_inv_lsb, value)

    @property
    def reg_sar2_dig_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_dig_force_msb, self.__reg_sar2_dig_force_lsb)
    @reg_sar2_dig_force.setter
    def reg_sar2_dig_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_dig_force_msb, self.__reg_sar2_dig_force_lsb, value)

    @property
    def reg_sar2_pwdet_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_pwdet_force_msb, self.__reg_sar2_pwdet_force_lsb)
    @reg_sar2_pwdet_force.setter
    def reg_sar2_pwdet_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_pwdet_force_msb, self.__reg_sar2_pwdet_force_lsb, value)

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
class SAR_MEAS_START2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x94
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
class SAR_DAC_CTRL1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x98
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0x9c
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
class SAR_MEAS_CTRL2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xa0
        self.__reg_amp_short_ref_gnd_force_lsb = 17
        self.__reg_amp_short_ref_gnd_force_msb = 18
        self.__reg_amp_short_ref_force_lsb = 15
        self.__reg_amp_short_ref_force_msb = 16
        self.__reg_amp_rst_fb_force_lsb = 13
        self.__reg_amp_rst_fb_force_msb = 14
        self.__reg_sar2_rstb_force_lsb = 11
        self.__reg_sar2_rstb_force_msb = 12
        self.__reg_sar_rstb_fsm_idle_lsb = 10
        self.__reg_sar_rstb_fsm_idle_msb = 10
        self.__reg_xpd_sar_fsm_idle_lsb = 9
        self.__reg_xpd_sar_fsm_idle_msb = 9
        self.__reg_amp_short_ref_gnd_fsm_idle_lsb = 8
        self.__reg_amp_short_ref_gnd_fsm_idle_msb = 8
        self.__reg_amp_short_ref_fsm_idle_lsb = 7
        self.__reg_amp_short_ref_fsm_idle_msb = 7
        self.__reg_amp_rst_fb_fsm_idle_lsb = 6
        self.__reg_amp_rst_fb_fsm_idle_msb = 6
        self.__reg_xpd_sar_amp_fsm_idle_lsb = 5
        self.__reg_xpd_sar_amp_fsm_idle_msb = 5
        self.__reg_sar1_dac_xpd_fsm_idle_lsb = 4
        self.__reg_sar1_dac_xpd_fsm_idle_msb = 4
        self.__reg_sar1_dac_xpd_fsm_lsb = 0
        self.__reg_sar1_dac_xpd_fsm_msb = 3
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
    def reg_sar2_rstb_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar2_rstb_force_msb, self.__reg_sar2_rstb_force_lsb)
    @reg_sar2_rstb_force.setter
    def reg_sar2_rstb_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar2_rstb_force_msb, self.__reg_sar2_rstb_force_lsb, value)

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

    @property
    def reg_sar1_dac_xpd_fsm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sar1_dac_xpd_fsm_msb, self.__reg_sar1_dac_xpd_fsm_lsb)
    @reg_sar1_dac_xpd_fsm.setter
    def reg_sar1_dac_xpd_fsm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sar1_dac_xpd_fsm_msb, self.__reg_sar1_dac_xpd_fsm_lsb, value)
class SAR_NOUSE(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xf8
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
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = SARADC_BASE + 0xfc
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
        return 0x1605180 
