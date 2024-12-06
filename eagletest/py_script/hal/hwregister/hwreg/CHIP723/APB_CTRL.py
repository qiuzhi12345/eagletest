from hal.common import *
from hal.hwregister.hwreg.CHIP723.addr_base import *
class APB_CTRL(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.APB_CTRL_SYSCLK_CONF = APB_CTRL_SYSCLK_CONF(self.channel, self.chipv)
        self.APB_CTRL_TICK_CONF = APB_CTRL_TICK_CONF(self.channel, self.chipv)
        self.APB_CTRL_CLK_OUT_EN = APB_CTRL_CLK_OUT_EN(self.channel, self.chipv)
        self.HOST_INF_SEL = HOST_INF_SEL(self.channel, self.chipv)
        self.EXT_MEM_PMS_LOCK = EXT_MEM_PMS_LOCK(self.channel, self.chipv)
        self.FLASH_ACE0_ATTR = FLASH_ACE0_ATTR(self.channel, self.chipv)
        self.FLASH_ACE1_ATTR = FLASH_ACE1_ATTR(self.channel, self.chipv)
        self.FLASH_ACE2_ATTR = FLASH_ACE2_ATTR(self.channel, self.chipv)
        self.FLASH_ACE3_ATTR = FLASH_ACE3_ATTR(self.channel, self.chipv)
        self.FLASH_ACE0_ADDR = FLASH_ACE0_ADDR(self.channel, self.chipv)
        self.FLASH_ACE1_ADDR = FLASH_ACE1_ADDR(self.channel, self.chipv)
        self.FLASH_ACE2_ADDR = FLASH_ACE2_ADDR(self.channel, self.chipv)
        self.FLASH_ACE3_ADDR = FLASH_ACE3_ADDR(self.channel, self.chipv)
        self.FLASH_ACE0_SIZE = FLASH_ACE0_SIZE(self.channel, self.chipv)
        self.FLASH_ACE1_SIZE = FLASH_ACE1_SIZE(self.channel, self.chipv)
        self.FLASH_ACE2_SIZE = FLASH_ACE2_SIZE(self.channel, self.chipv)
        self.FLASH_ACE3_SIZE = FLASH_ACE3_SIZE(self.channel, self.chipv)
        self.SRAM_ACE0_ATTR = SRAM_ACE0_ATTR(self.channel, self.chipv)
        self.SRAM_ACE1_ATTR = SRAM_ACE1_ATTR(self.channel, self.chipv)
        self.SRAM_ACE2_ATTR = SRAM_ACE2_ATTR(self.channel, self.chipv)
        self.SRAM_ACE3_ATTR = SRAM_ACE3_ATTR(self.channel, self.chipv)
        self.SRAM_ACE0_ADDR = SRAM_ACE0_ADDR(self.channel, self.chipv)
        self.SRAM_ACE1_ADDR = SRAM_ACE1_ADDR(self.channel, self.chipv)
        self.SRAM_ACE2_ADDR = SRAM_ACE2_ADDR(self.channel, self.chipv)
        self.SRAM_ACE3_ADDR = SRAM_ACE3_ADDR(self.channel, self.chipv)
        self.SRAM_ACE0_SIZE = SRAM_ACE0_SIZE(self.channel, self.chipv)
        self.SRAM_ACE1_SIZE = SRAM_ACE1_SIZE(self.channel, self.chipv)
        self.SRAM_ACE2_SIZE = SRAM_ACE2_SIZE(self.channel, self.chipv)
        self.SRAM_ACE3_SIZE = SRAM_ACE3_SIZE(self.channel, self.chipv)
        self.SPI_MEM_PMS_CTRL = SPI_MEM_PMS_CTRL(self.channel, self.chipv)
        self.SPI_MEM_REJECT_ADDR = SPI_MEM_REJECT_ADDR(self.channel, self.chipv)
        self.APB_CTRL_SDIO_CTRL = APB_CTRL_SDIO_CTRL(self.channel, self.chipv)
        self.REDCY_SIG0_REG = REDCY_SIG0_REG(self.channel, self.chipv)
        self.REDCY_SIG1_REG = REDCY_SIG1_REG(self.channel, self.chipv)
        self.WIFI_BB_CFG = WIFI_BB_CFG(self.channel, self.chipv)
        self.WIFI_BB_CFG_2 = WIFI_BB_CFG_2(self.channel, self.chipv)
        self.WIFI_CLK_EN = WIFI_CLK_EN(self.channel, self.chipv)
        self.WIFI_RST_EN = WIFI_RST_EN(self.channel, self.chipv)
        self.FRONT_END_MEM_PD = FRONT_END_MEM_PD(self.channel, self.chipv)
        self.APB_CTRL_DATE = APB_CTRL_DATE(self.channel, self.chipv)
class APB_CTRL_SYSCLK_CONF(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x0
        self.__apb_ctrl_soc_clk_sel_lsb = 14
        self.__apb_ctrl_soc_clk_sel_msb = 15
        self.__apb_ctrl_rst_tick_cnt_lsb = 12
        self.__apb_ctrl_rst_tick_cnt_msb = 12
        self.__reg_clk_en_lsb = 11
        self.__reg_clk_en_msb = 11
        self.__apb_ctrl_clk_320m_en_lsb = 10
        self.__apb_ctrl_clk_320m_en_msb = 10
        self.__apb_ctrl_pre_div_cnt_lsb = 0
        self.__apb_ctrl_pre_div_cnt_msb = 9
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def apb_ctrl_soc_clk_sel(self):
        return self.__MEM.rdm(self.__addr, self.__apb_ctrl_soc_clk_sel_msb, self.__apb_ctrl_soc_clk_sel_lsb)
    @apb_ctrl_soc_clk_sel.setter
    def apb_ctrl_soc_clk_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__apb_ctrl_soc_clk_sel_msb, self.__apb_ctrl_soc_clk_sel_lsb, value)

    @property
    def apb_ctrl_rst_tick_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__apb_ctrl_rst_tick_cnt_msb, self.__apb_ctrl_rst_tick_cnt_lsb)
    @apb_ctrl_rst_tick_cnt.setter
    def apb_ctrl_rst_tick_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__apb_ctrl_rst_tick_cnt_msb, self.__apb_ctrl_rst_tick_cnt_lsb, value)

    @property
    def reg_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk_en_msb, self.__reg_clk_en_lsb)
    @reg_clk_en.setter
    def reg_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk_en_msb, self.__reg_clk_en_lsb, value)

    @property
    def apb_ctrl_clk_320m_en(self):
        return self.__MEM.rdm(self.__addr, self.__apb_ctrl_clk_320m_en_msb, self.__apb_ctrl_clk_320m_en_lsb)
    @apb_ctrl_clk_320m_en.setter
    def apb_ctrl_clk_320m_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__apb_ctrl_clk_320m_en_msb, self.__apb_ctrl_clk_320m_en_lsb, value)

    @property
    def apb_ctrl_pre_div_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__apb_ctrl_pre_div_cnt_msb, self.__apb_ctrl_pre_div_cnt_lsb)
    @apb_ctrl_pre_div_cnt.setter
    def apb_ctrl_pre_div_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__apb_ctrl_pre_div_cnt_msb, self.__apb_ctrl_pre_div_cnt_lsb, value)
class APB_CTRL_TICK_CONF(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x4
        self.__apb_ctrl_tick_enable_lsb = 16
        self.__apb_ctrl_tick_enable_msb = 16
        self.__apb_ctrl_ck8m_tick_num_lsb = 8
        self.__apb_ctrl_ck8m_tick_num_msb = 15
        self.__apb_ctrl_xtal_tick_num_lsb = 0
        self.__apb_ctrl_xtal_tick_num_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def apb_ctrl_tick_enable(self):
        return self.__MEM.rdm(self.__addr, self.__apb_ctrl_tick_enable_msb, self.__apb_ctrl_tick_enable_lsb)
    @apb_ctrl_tick_enable.setter
    def apb_ctrl_tick_enable(self, value):
        return self.__MEM.wrm(self.__addr, self.__apb_ctrl_tick_enable_msb, self.__apb_ctrl_tick_enable_lsb, value)

    @property
    def apb_ctrl_ck8m_tick_num(self):
        return self.__MEM.rdm(self.__addr, self.__apb_ctrl_ck8m_tick_num_msb, self.__apb_ctrl_ck8m_tick_num_lsb)
    @apb_ctrl_ck8m_tick_num.setter
    def apb_ctrl_ck8m_tick_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__apb_ctrl_ck8m_tick_num_msb, self.__apb_ctrl_ck8m_tick_num_lsb, value)

    @property
    def apb_ctrl_xtal_tick_num(self):
        return self.__MEM.rdm(self.__addr, self.__apb_ctrl_xtal_tick_num_msb, self.__apb_ctrl_xtal_tick_num_lsb)
    @apb_ctrl_xtal_tick_num.setter
    def apb_ctrl_xtal_tick_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__apb_ctrl_xtal_tick_num_msb, self.__apb_ctrl_xtal_tick_num_lsb, value)
class APB_CTRL_CLK_OUT_EN(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x8
        self.__reg_clk_xtal_oen_lsb = 10
        self.__reg_clk_xtal_oen_msb = 10
        self.__reg_clk40x_bb_oen_lsb = 9
        self.__reg_clk40x_bb_oen_msb = 9
        self.__reg_clk_dac_cpu_oen_lsb = 8
        self.__reg_clk_dac_cpu_oen_msb = 8
        self.__reg_clk_adc_inf_oen_lsb = 7
        self.__reg_clk_adc_inf_oen_msb = 7
        self.__reg_clk_320m_oen_lsb = 6
        self.__reg_clk_320m_oen_msb = 6
        self.__reg_clk160_oen_lsb = 5
        self.__reg_clk160_oen_msb = 5
        self.__reg_clk80_oen_lsb = 4
        self.__reg_clk80_oen_msb = 4
        self.__reg_clk_bb_oen_lsb = 3
        self.__reg_clk_bb_oen_msb = 3
        self.__reg_clk44_oen_lsb = 2
        self.__reg_clk44_oen_msb = 2
        self.__reg_clk22_oen_lsb = 1
        self.__reg_clk22_oen_msb = 1
        self.__reg_clk20_oen_lsb = 0
        self.__reg_clk20_oen_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_clk_xtal_oen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk_xtal_oen_msb, self.__reg_clk_xtal_oen_lsb)
    @reg_clk_xtal_oen.setter
    def reg_clk_xtal_oen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk_xtal_oen_msb, self.__reg_clk_xtal_oen_lsb, value)

    @property
    def reg_clk40x_bb_oen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk40x_bb_oen_msb, self.__reg_clk40x_bb_oen_lsb)
    @reg_clk40x_bb_oen.setter
    def reg_clk40x_bb_oen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk40x_bb_oen_msb, self.__reg_clk40x_bb_oen_lsb, value)

    @property
    def reg_clk_dac_cpu_oen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk_dac_cpu_oen_msb, self.__reg_clk_dac_cpu_oen_lsb)
    @reg_clk_dac_cpu_oen.setter
    def reg_clk_dac_cpu_oen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk_dac_cpu_oen_msb, self.__reg_clk_dac_cpu_oen_lsb, value)

    @property
    def reg_clk_adc_inf_oen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk_adc_inf_oen_msb, self.__reg_clk_adc_inf_oen_lsb)
    @reg_clk_adc_inf_oen.setter
    def reg_clk_adc_inf_oen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk_adc_inf_oen_msb, self.__reg_clk_adc_inf_oen_lsb, value)

    @property
    def reg_clk_320m_oen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk_320m_oen_msb, self.__reg_clk_320m_oen_lsb)
    @reg_clk_320m_oen.setter
    def reg_clk_320m_oen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk_320m_oen_msb, self.__reg_clk_320m_oen_lsb, value)

    @property
    def reg_clk160_oen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk160_oen_msb, self.__reg_clk160_oen_lsb)
    @reg_clk160_oen.setter
    def reg_clk160_oen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk160_oen_msb, self.__reg_clk160_oen_lsb, value)

    @property
    def reg_clk80_oen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk80_oen_msb, self.__reg_clk80_oen_lsb)
    @reg_clk80_oen.setter
    def reg_clk80_oen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk80_oen_msb, self.__reg_clk80_oen_lsb, value)

    @property
    def reg_clk_bb_oen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk_bb_oen_msb, self.__reg_clk_bb_oen_lsb)
    @reg_clk_bb_oen.setter
    def reg_clk_bb_oen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk_bb_oen_msb, self.__reg_clk_bb_oen_lsb, value)

    @property
    def reg_clk44_oen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk44_oen_msb, self.__reg_clk44_oen_lsb)
    @reg_clk44_oen.setter
    def reg_clk44_oen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk44_oen_msb, self.__reg_clk44_oen_lsb, value)

    @property
    def reg_clk22_oen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk22_oen_msb, self.__reg_clk22_oen_lsb)
    @reg_clk22_oen.setter
    def reg_clk22_oen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk22_oen_msb, self.__reg_clk22_oen_lsb, value)

    @property
    def reg_clk20_oen(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk20_oen_msb, self.__reg_clk20_oen_lsb)
    @reg_clk20_oen.setter
    def reg_clk20_oen(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk20_oen_msb, self.__reg_clk20_oen_lsb, value)
class HOST_INF_SEL(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0xc
        self.__peri_io_swap_lsb = 0
        self.__peri_io_swap_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def peri_io_swap(self):
        return self.__MEM.rdm(self.__addr, self.__peri_io_swap_msb, self.__peri_io_swap_lsb)
    @peri_io_swap.setter
    def peri_io_swap(self, value):
        return self.__MEM.wrm(self.__addr, self.__peri_io_swap_msb, self.__peri_io_swap_lsb, value)
class EXT_MEM_PMS_LOCK(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x10
        self.__ext_mem_pms_lock_lsb = 0
        self.__ext_mem_pms_lock_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def ext_mem_pms_lock(self):
        return self.__MEM.rdm(self.__addr, self.__ext_mem_pms_lock_msb, self.__ext_mem_pms_lock_lsb)
    @ext_mem_pms_lock.setter
    def ext_mem_pms_lock(self, value):
        return self.__MEM.wrm(self.__addr, self.__ext_mem_pms_lock_msb, self.__ext_mem_pms_lock_lsb, value)
class FLASH_ACE0_ATTR(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x14
        self.__flash_ace0_attr_lsb = 0
        self.__flash_ace0_attr_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def flash_ace0_attr(self):
        return self.__MEM.rdm(self.__addr, self.__flash_ace0_attr_msb, self.__flash_ace0_attr_lsb)
    @flash_ace0_attr.setter
    def flash_ace0_attr(self, value):
        return self.__MEM.wrm(self.__addr, self.__flash_ace0_attr_msb, self.__flash_ace0_attr_lsb, value)
class FLASH_ACE1_ATTR(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x18
        self.__flash_ace1_attr_lsb = 0
        self.__flash_ace1_attr_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def flash_ace1_attr(self):
        return self.__MEM.rdm(self.__addr, self.__flash_ace1_attr_msb, self.__flash_ace1_attr_lsb)
    @flash_ace1_attr.setter
    def flash_ace1_attr(self, value):
        return self.__MEM.wrm(self.__addr, self.__flash_ace1_attr_msb, self.__flash_ace1_attr_lsb, value)
class FLASH_ACE2_ATTR(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x1c
        self.__flash_ace2_attr_lsb = 0
        self.__flash_ace2_attr_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def flash_ace2_attr(self):
        return self.__MEM.rdm(self.__addr, self.__flash_ace2_attr_msb, self.__flash_ace2_attr_lsb)
    @flash_ace2_attr.setter
    def flash_ace2_attr(self, value):
        return self.__MEM.wrm(self.__addr, self.__flash_ace2_attr_msb, self.__flash_ace2_attr_lsb, value)
class FLASH_ACE3_ATTR(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x20
        self.__flash_ace3_attr_lsb = 0
        self.__flash_ace3_attr_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def flash_ace3_attr(self):
        return self.__MEM.rdm(self.__addr, self.__flash_ace3_attr_msb, self.__flash_ace3_attr_lsb)
    @flash_ace3_attr.setter
    def flash_ace3_attr(self, value):
        return self.__MEM.wrm(self.__addr, self.__flash_ace3_attr_msb, self.__flash_ace3_attr_lsb, value)
class FLASH_ACE0_ADDR(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x24
        self.__flash_ace0_addr_s_lsb = 0
        self.__flash_ace0_addr_s_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def flash_ace0_addr_s(self):
        return self.__MEM.rdm(self.__addr, self.__flash_ace0_addr_s_msb, self.__flash_ace0_addr_s_lsb)
    @flash_ace0_addr_s.setter
    def flash_ace0_addr_s(self, value):
        return self.__MEM.wrm(self.__addr, self.__flash_ace0_addr_s_msb, self.__flash_ace0_addr_s_lsb, value)
class FLASH_ACE1_ADDR(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x28
        self.__flash_ace1_addr_s_lsb = 0
        self.__flash_ace1_addr_s_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def flash_ace1_addr_s(self):
        return self.__MEM.rdm(self.__addr, self.__flash_ace1_addr_s_msb, self.__flash_ace1_addr_s_lsb)
    @flash_ace1_addr_s.setter
    def flash_ace1_addr_s(self, value):
        return self.__MEM.wrm(self.__addr, self.__flash_ace1_addr_s_msb, self.__flash_ace1_addr_s_lsb, value)
class FLASH_ACE2_ADDR(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x2c
        self.__flash_ace2_addr_s_lsb = 0
        self.__flash_ace2_addr_s_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def flash_ace2_addr_s(self):
        return self.__MEM.rdm(self.__addr, self.__flash_ace2_addr_s_msb, self.__flash_ace2_addr_s_lsb)
    @flash_ace2_addr_s.setter
    def flash_ace2_addr_s(self, value):
        return self.__MEM.wrm(self.__addr, self.__flash_ace2_addr_s_msb, self.__flash_ace2_addr_s_lsb, value)
class FLASH_ACE3_ADDR(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x30
        self.__flash_ace3_addr_s_lsb = 0
        self.__flash_ace3_addr_s_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def flash_ace3_addr_s(self):
        return self.__MEM.rdm(self.__addr, self.__flash_ace3_addr_s_msb, self.__flash_ace3_addr_s_lsb)
    @flash_ace3_addr_s.setter
    def flash_ace3_addr_s(self, value):
        return self.__MEM.wrm(self.__addr, self.__flash_ace3_addr_s_msb, self.__flash_ace3_addr_s_lsb, value)
class FLASH_ACE0_SIZE(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x34
        self.__flash_ace0_size_lsb = 0
        self.__flash_ace0_size_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def flash_ace0_size(self):
        return self.__MEM.rdm(self.__addr, self.__flash_ace0_size_msb, self.__flash_ace0_size_lsb)
    @flash_ace0_size.setter
    def flash_ace0_size(self, value):
        return self.__MEM.wrm(self.__addr, self.__flash_ace0_size_msb, self.__flash_ace0_size_lsb, value)
class FLASH_ACE1_SIZE(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x38
        self.__flash_ace1_size_lsb = 0
        self.__flash_ace1_size_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def flash_ace1_size(self):
        return self.__MEM.rdm(self.__addr, self.__flash_ace1_size_msb, self.__flash_ace1_size_lsb)
    @flash_ace1_size.setter
    def flash_ace1_size(self, value):
        return self.__MEM.wrm(self.__addr, self.__flash_ace1_size_msb, self.__flash_ace1_size_lsb, value)
class FLASH_ACE2_SIZE(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x3c
        self.__flash_ace2_size_lsb = 0
        self.__flash_ace2_size_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def flash_ace2_size(self):
        return self.__MEM.rdm(self.__addr, self.__flash_ace2_size_msb, self.__flash_ace2_size_lsb)
    @flash_ace2_size.setter
    def flash_ace2_size(self, value):
        return self.__MEM.wrm(self.__addr, self.__flash_ace2_size_msb, self.__flash_ace2_size_lsb, value)
class FLASH_ACE3_SIZE(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x40
        self.__flash_ace3_size_lsb = 0
        self.__flash_ace3_size_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def flash_ace3_size(self):
        return self.__MEM.rdm(self.__addr, self.__flash_ace3_size_msb, self.__flash_ace3_size_lsb)
    @flash_ace3_size.setter
    def flash_ace3_size(self, value):
        return self.__MEM.wrm(self.__addr, self.__flash_ace3_size_msb, self.__flash_ace3_size_lsb, value)
class SRAM_ACE0_ATTR(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x44
        self.__sram_ace0_attr_lsb = 0
        self.__sram_ace0_attr_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_ace0_attr(self):
        return self.__MEM.rdm(self.__addr, self.__sram_ace0_attr_msb, self.__sram_ace0_attr_lsb)
    @sram_ace0_attr.setter
    def sram_ace0_attr(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_ace0_attr_msb, self.__sram_ace0_attr_lsb, value)
class SRAM_ACE1_ATTR(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x48
        self.__sram_ace1_attr_lsb = 0
        self.__sram_ace1_attr_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_ace1_attr(self):
        return self.__MEM.rdm(self.__addr, self.__sram_ace1_attr_msb, self.__sram_ace1_attr_lsb)
    @sram_ace1_attr.setter
    def sram_ace1_attr(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_ace1_attr_msb, self.__sram_ace1_attr_lsb, value)
class SRAM_ACE2_ATTR(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x4c
        self.__sram_ace2_attr_lsb = 0
        self.__sram_ace2_attr_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_ace2_attr(self):
        return self.__MEM.rdm(self.__addr, self.__sram_ace2_attr_msb, self.__sram_ace2_attr_lsb)
    @sram_ace2_attr.setter
    def sram_ace2_attr(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_ace2_attr_msb, self.__sram_ace2_attr_lsb, value)
class SRAM_ACE3_ATTR(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x50
        self.__sram_ace3_attr_lsb = 0
        self.__sram_ace3_attr_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_ace3_attr(self):
        return self.__MEM.rdm(self.__addr, self.__sram_ace3_attr_msb, self.__sram_ace3_attr_lsb)
    @sram_ace3_attr.setter
    def sram_ace3_attr(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_ace3_attr_msb, self.__sram_ace3_attr_lsb, value)
class SRAM_ACE0_ADDR(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x54
        self.__sram_ace0_addr_s_lsb = 0
        self.__sram_ace0_addr_s_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_ace0_addr_s(self):
        return self.__MEM.rdm(self.__addr, self.__sram_ace0_addr_s_msb, self.__sram_ace0_addr_s_lsb)
    @sram_ace0_addr_s.setter
    def sram_ace0_addr_s(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_ace0_addr_s_msb, self.__sram_ace0_addr_s_lsb, value)
class SRAM_ACE1_ADDR(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x58
        self.__sram_ace1_addr_s_lsb = 0
        self.__sram_ace1_addr_s_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_ace1_addr_s(self):
        return self.__MEM.rdm(self.__addr, self.__sram_ace1_addr_s_msb, self.__sram_ace1_addr_s_lsb)
    @sram_ace1_addr_s.setter
    def sram_ace1_addr_s(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_ace1_addr_s_msb, self.__sram_ace1_addr_s_lsb, value)
class SRAM_ACE2_ADDR(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x5c
        self.__sram_ace2_addr_s_lsb = 0
        self.__sram_ace2_addr_s_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_ace2_addr_s(self):
        return self.__MEM.rdm(self.__addr, self.__sram_ace2_addr_s_msb, self.__sram_ace2_addr_s_lsb)
    @sram_ace2_addr_s.setter
    def sram_ace2_addr_s(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_ace2_addr_s_msb, self.__sram_ace2_addr_s_lsb, value)
class SRAM_ACE3_ADDR(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x60
        self.__sram_ace3_addr_s_lsb = 0
        self.__sram_ace3_addr_s_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_ace3_addr_s(self):
        return self.__MEM.rdm(self.__addr, self.__sram_ace3_addr_s_msb, self.__sram_ace3_addr_s_lsb)
    @sram_ace3_addr_s.setter
    def sram_ace3_addr_s(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_ace3_addr_s_msb, self.__sram_ace3_addr_s_lsb, value)
class SRAM_ACE0_SIZE(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x64
        self.__sram_ace0_size_lsb = 0
        self.__sram_ace0_size_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_ace0_size(self):
        return self.__MEM.rdm(self.__addr, self.__sram_ace0_size_msb, self.__sram_ace0_size_lsb)
    @sram_ace0_size.setter
    def sram_ace0_size(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_ace0_size_msb, self.__sram_ace0_size_lsb, value)
class SRAM_ACE1_SIZE(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x68
        self.__sram_ace1_size_lsb = 0
        self.__sram_ace1_size_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_ace1_size(self):
        return self.__MEM.rdm(self.__addr, self.__sram_ace1_size_msb, self.__sram_ace1_size_lsb)
    @sram_ace1_size.setter
    def sram_ace1_size(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_ace1_size_msb, self.__sram_ace1_size_lsb, value)
class SRAM_ACE2_SIZE(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x6c
        self.__sram_ace2_size_lsb = 0
        self.__sram_ace2_size_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_ace2_size(self):
        return self.__MEM.rdm(self.__addr, self.__sram_ace2_size_msb, self.__sram_ace2_size_lsb)
    @sram_ace2_size.setter
    def sram_ace2_size(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_ace2_size_msb, self.__sram_ace2_size_lsb, value)
class SRAM_ACE3_SIZE(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x70
        self.__sram_ace3_size_lsb = 0
        self.__sram_ace3_size_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def sram_ace3_size(self):
        return self.__MEM.rdm(self.__addr, self.__sram_ace3_size_msb, self.__sram_ace3_size_lsb)
    @sram_ace3_size.setter
    def sram_ace3_size(self, value):
        return self.__MEM.wrm(self.__addr, self.__sram_ace3_size_msb, self.__sram_ace3_size_lsb, value)
class SPI_MEM_PMS_CTRL(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x74
        self.__spi_mem_reject_cde_lsb = 2
        self.__spi_mem_reject_cde_msb = 6
        self.__spi_mem_reject_clr_lsb = 1
        self.__spi_mem_reject_clr_msb = 1
        self.__spi_mem_reject_int_lsb = 0
        self.__spi_mem_reject_int_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def spi_mem_reject_cde(self):
        return self.__MEM.rdm(self.__addr, self.__spi_mem_reject_cde_msb, self.__spi_mem_reject_cde_lsb)
    @spi_mem_reject_cde.setter
    def spi_mem_reject_cde(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi_mem_reject_cde_msb, self.__spi_mem_reject_cde_lsb, value)

    @property
    def spi_mem_reject_clr(self):
        return self.__MEM.rdm(self.__addr, self.__spi_mem_reject_clr_msb, self.__spi_mem_reject_clr_lsb)
    @spi_mem_reject_clr.setter
    def spi_mem_reject_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi_mem_reject_clr_msb, self.__spi_mem_reject_clr_lsb, value)

    @property
    def spi_mem_reject_int(self):
        return self.__MEM.rdm(self.__addr, self.__spi_mem_reject_int_msb, self.__spi_mem_reject_int_lsb)
    @spi_mem_reject_int.setter
    def spi_mem_reject_int(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi_mem_reject_int_msb, self.__spi_mem_reject_int_lsb, value)
class SPI_MEM_REJECT_ADDR(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x78
        self.__spi_mem_reject_addr_lsb = 0
        self.__spi_mem_reject_addr_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def spi_mem_reject_addr(self):
        return self.__MEM.rdm(self.__addr, self.__spi_mem_reject_addr_msb, self.__spi_mem_reject_addr_lsb)
    @spi_mem_reject_addr.setter
    def spi_mem_reject_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__spi_mem_reject_addr_msb, self.__spi_mem_reject_addr_lsb, value)
class APB_CTRL_SDIO_CTRL(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x7c
        self.__reg_sdio_win_access_en_lsb = 0
        self.__reg_sdio_win_access_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sdio_win_access_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sdio_win_access_en_msb, self.__reg_sdio_win_access_en_lsb)
    @reg_sdio_win_access_en.setter
    def reg_sdio_win_access_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sdio_win_access_en_msb, self.__reg_sdio_win_access_en_lsb, value)
class REDCY_SIG0_REG(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x80
        self.__redcy_andor_lsb = 31
        self.__redcy_andor_msb = 31
        self.__redcy_sig0_lsb = 0
        self.__redcy_sig0_msb = 30
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def redcy_andor(self):
        return self.__MEM.rdm(self.__addr, self.__redcy_andor_msb, self.__redcy_andor_lsb)
    @redcy_andor.setter
    def redcy_andor(self, value):
        return self.__MEM.wrm(self.__addr, self.__redcy_andor_msb, self.__redcy_andor_lsb, value)

    @property
    def redcy_sig0(self):
        return self.__MEM.rdm(self.__addr, self.__redcy_sig0_msb, self.__redcy_sig0_lsb)
    @redcy_sig0.setter
    def redcy_sig0(self, value):
        return self.__MEM.wrm(self.__addr, self.__redcy_sig0_msb, self.__redcy_sig0_lsb, value)
class REDCY_SIG1_REG(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x84
        self.__redcy_nandor_lsb = 31
        self.__redcy_nandor_msb = 31
        self.__redcy_sig1_lsb = 0
        self.__redcy_sig1_msb = 30
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def redcy_nandor(self):
        return self.__MEM.rdm(self.__addr, self.__redcy_nandor_msb, self.__redcy_nandor_lsb)
    @redcy_nandor.setter
    def redcy_nandor(self, value):
        return self.__MEM.wrm(self.__addr, self.__redcy_nandor_msb, self.__redcy_nandor_lsb, value)

    @property
    def redcy_sig1(self):
        return self.__MEM.rdm(self.__addr, self.__redcy_sig1_msb, self.__redcy_sig1_lsb)
    @redcy_sig1.setter
    def redcy_sig1(self, value):
        return self.__MEM.wrm(self.__addr, self.__redcy_sig1_msb, self.__redcy_sig1_lsb, value)
class WIFI_BB_CFG(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x88
        self.__reg_wifi_bb_cfg_lsb = 0
        self.__reg_wifi_bb_cfg_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wifi_bb_cfg(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wifi_bb_cfg_msb, self.__reg_wifi_bb_cfg_lsb)
    @reg_wifi_bb_cfg.setter
    def reg_wifi_bb_cfg(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wifi_bb_cfg_msb, self.__reg_wifi_bb_cfg_lsb, value)
class WIFI_BB_CFG_2(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x8c
        self.__reg_wifi_bb_cfg_2_lsb = 0
        self.__reg_wifi_bb_cfg_2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wifi_bb_cfg_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wifi_bb_cfg_2_msb, self.__reg_wifi_bb_cfg_2_lsb)
    @reg_wifi_bb_cfg_2.setter
    def reg_wifi_bb_cfg_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wifi_bb_cfg_2_msb, self.__reg_wifi_bb_cfg_2_lsb, value)
class WIFI_CLK_EN(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x90
        self.__reg_wifi_clk_en_lsb = 0
        self.__reg_wifi_clk_en_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wifi_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wifi_clk_en_msb, self.__reg_wifi_clk_en_lsb)
    @reg_wifi_clk_en.setter
    def reg_wifi_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wifi_clk_en_msb, self.__reg_wifi_clk_en_lsb, value)
class WIFI_RST_EN(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x94
        self.__reg_wifi_rst_lsb = 0
        self.__reg_wifi_rst_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wifi_rst(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wifi_rst_msb, self.__reg_wifi_rst_lsb)
    @reg_wifi_rst.setter
    def reg_wifi_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wifi_rst_msb, self.__reg_wifi_rst_lsb, value)
class FRONT_END_MEM_PD(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x98
        self.__reg_dc_mem_force_pd_lsb = 5
        self.__reg_dc_mem_force_pd_msb = 5
        self.__reg_dc_mem_force_pu_lsb = 4
        self.__reg_dc_mem_force_pu_msb = 4
        self.__reg_pbus_mem_force_pd_lsb = 3
        self.__reg_pbus_mem_force_pd_msb = 3
        self.__reg_pbus_mem_force_pu_lsb = 2
        self.__reg_pbus_mem_force_pu_msb = 2
        self.__reg_agc_mem_force_pd_lsb = 1
        self.__reg_agc_mem_force_pd_msb = 1
        self.__reg_agc_mem_force_pu_lsb = 0
        self.__reg_agc_mem_force_pu_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_dc_mem_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_mem_force_pd_msb, self.__reg_dc_mem_force_pd_lsb)
    @reg_dc_mem_force_pd.setter
    def reg_dc_mem_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_mem_force_pd_msb, self.__reg_dc_mem_force_pd_lsb, value)

    @property
    def reg_dc_mem_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dc_mem_force_pu_msb, self.__reg_dc_mem_force_pu_lsb)
    @reg_dc_mem_force_pu.setter
    def reg_dc_mem_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dc_mem_force_pu_msb, self.__reg_dc_mem_force_pu_lsb, value)

    @property
    def reg_pbus_mem_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pbus_mem_force_pd_msb, self.__reg_pbus_mem_force_pd_lsb)
    @reg_pbus_mem_force_pd.setter
    def reg_pbus_mem_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pbus_mem_force_pd_msb, self.__reg_pbus_mem_force_pd_lsb, value)

    @property
    def reg_pbus_mem_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pbus_mem_force_pu_msb, self.__reg_pbus_mem_force_pu_lsb)
    @reg_pbus_mem_force_pu.setter
    def reg_pbus_mem_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pbus_mem_force_pu_msb, self.__reg_pbus_mem_force_pu_lsb, value)

    @property
    def reg_agc_mem_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_mem_force_pd_msb, self.__reg_agc_mem_force_pd_lsb)
    @reg_agc_mem_force_pd.setter
    def reg_agc_mem_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_mem_force_pd_msb, self.__reg_agc_mem_force_pd_lsb, value)

    @property
    def reg_agc_mem_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_agc_mem_force_pu_msb, self.__reg_agc_mem_force_pu_lsb)
    @reg_agc_mem_force_pu.setter
    def reg_agc_mem_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_agc_mem_force_pu_msb, self.__reg_agc_mem_force_pu_lsb, value)
class APB_CTRL_DATE(object):
    def __init__(self, channel, chipv = "CHIP723"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = APB_CTRL_BASE + 0x3fc
        self.__apb_ctrl_date_lsb = 0
        self.__apb_ctrl_date_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def apb_ctrl_date(self):
        return self.__MEM.rdm(self.__addr, self.__apb_ctrl_date_msb, self.__apb_ctrl_date_lsb)
    @apb_ctrl_date.setter
    def apb_ctrl_date(self, value):
        return self.__MEM.wrm(self.__addr, self.__apb_ctrl_date_msb, self.__apb_ctrl_date_lsb, value)
    @property
    def default_value(self):
        return 0x1906210
