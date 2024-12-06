from hal.common import *
from hal.hwregister.hwreg.ESP32.addr_base import *
class EFUSE(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.EFUSE_BLK0_RDATA0 = EFUSE_BLK0_RDATA0(self.channel, self.chipv)
        self.EFUSE_BLK0_RDATA1 = EFUSE_BLK0_RDATA1(self.channel, self.chipv)
        self.EFUSE_BLK0_RDATA2 = EFUSE_BLK0_RDATA2(self.channel, self.chipv)
        self.EFUSE_BLK0_RDATA3 = EFUSE_BLK0_RDATA3(self.channel, self.chipv)
        self.EFUSE_BLK0_RDATA4 = EFUSE_BLK0_RDATA4(self.channel, self.chipv)
        self.EFUSE_BLK0_RDATA5 = EFUSE_BLK0_RDATA5(self.channel, self.chipv)
        self.EFUSE_BLK0_RDATA6 = EFUSE_BLK0_RDATA6(self.channel, self.chipv)
        self.EFUSE_BLK0_WDATA0 = EFUSE_BLK0_WDATA0(self.channel, self.chipv)
        self.EFUSE_BLK0_WDATA1 = EFUSE_BLK0_WDATA1(self.channel, self.chipv)
        self.EFUSE_BLK0_WDATA2 = EFUSE_BLK0_WDATA2(self.channel, self.chipv)
        self.EFUSE_BLK0_WDATA3 = EFUSE_BLK0_WDATA3(self.channel, self.chipv)
        self.EFUSE_BLK0_WDATA4 = EFUSE_BLK0_WDATA4(self.channel, self.chipv)
        self.EFUSE_BLK0_WDATA5 = EFUSE_BLK0_WDATA5(self.channel, self.chipv)
        self.EFUSE_BLK0_WDATA6 = EFUSE_BLK0_WDATA6(self.channel, self.chipv)
        self.EFUSE_BLK1_RDATA0 = EFUSE_BLK1_RDATA0(self.channel, self.chipv)
        self.EFUSE_BLK1_RDATA1 = EFUSE_BLK1_RDATA1(self.channel, self.chipv)
        self.EFUSE_BLK1_RDATA2 = EFUSE_BLK1_RDATA2(self.channel, self.chipv)
        self.EFUSE_BLK1_RDATA3 = EFUSE_BLK1_RDATA3(self.channel, self.chipv)
        self.EFUSE_BLK1_RDATA4 = EFUSE_BLK1_RDATA4(self.channel, self.chipv)
        self.EFUSE_BLK1_RDATA5 = EFUSE_BLK1_RDATA5(self.channel, self.chipv)
        self.EFUSE_BLK1_RDATA6 = EFUSE_BLK1_RDATA6(self.channel, self.chipv)
        self.EFUSE_BLK1_RDATA7 = EFUSE_BLK1_RDATA7(self.channel, self.chipv)
        self.EFUSE_BLK2_RDATA0 = EFUSE_BLK2_RDATA0(self.channel, self.chipv)
        self.EFUSE_BLK2_RDATA1 = EFUSE_BLK2_RDATA1(self.channel, self.chipv)
        self.EFUSE_BLK2_RDATA2 = EFUSE_BLK2_RDATA2(self.channel, self.chipv)
        self.EFUSE_BLK2_RDATA3 = EFUSE_BLK2_RDATA3(self.channel, self.chipv)
        self.EFUSE_BLK2_RDATA4 = EFUSE_BLK2_RDATA4(self.channel, self.chipv)
        self.EFUSE_BLK2_RDATA5 = EFUSE_BLK2_RDATA5(self.channel, self.chipv)
        self.EFUSE_BLK2_RDATA6 = EFUSE_BLK2_RDATA6(self.channel, self.chipv)
        self.EFUSE_BLK2_RDATA7 = EFUSE_BLK2_RDATA7(self.channel, self.chipv)
        self.EFUSE_BLK3_RDATA0 = EFUSE_BLK3_RDATA0(self.channel, self.chipv)
        self.EFUSE_BLK3_RDATA1 = EFUSE_BLK3_RDATA1(self.channel, self.chipv)
        self.EFUSE_BLK3_RDATA2 = EFUSE_BLK3_RDATA2(self.channel, self.chipv)
        self.EFUSE_BLK3_RDATA3 = EFUSE_BLK3_RDATA3(self.channel, self.chipv)
        self.EFUSE_BLK3_RDATA4 = EFUSE_BLK3_RDATA4(self.channel, self.chipv)
        self.EFUSE_BLK3_RDATA5 = EFUSE_BLK3_RDATA5(self.channel, self.chipv)
        self.EFUSE_BLK3_RDATA6 = EFUSE_BLK3_RDATA6(self.channel, self.chipv)
        self.EFUSE_BLK3_RDATA7 = EFUSE_BLK3_RDATA7(self.channel, self.chipv)
        self.EFUSE_BLK1_WDATA0 = EFUSE_BLK1_WDATA0(self.channel, self.chipv)
        self.EFUSE_BLK1_WDATA1 = EFUSE_BLK1_WDATA1(self.channel, self.chipv)
        self.EFUSE_BLK1_WDATA2 = EFUSE_BLK1_WDATA2(self.channel, self.chipv)
        self.EFUSE_BLK1_WDATA3 = EFUSE_BLK1_WDATA3(self.channel, self.chipv)
        self.EFUSE_BLK1_WDATA4 = EFUSE_BLK1_WDATA4(self.channel, self.chipv)
        self.EFUSE_BLK1_WDATA5 = EFUSE_BLK1_WDATA5(self.channel, self.chipv)
        self.EFUSE_BLK1_WDATA6 = EFUSE_BLK1_WDATA6(self.channel, self.chipv)
        self.EFUSE_BLK1_WDATA7 = EFUSE_BLK1_WDATA7(self.channel, self.chipv)
        self.EFUSE_BLK2_WDATA0 = EFUSE_BLK2_WDATA0(self.channel, self.chipv)
        self.EFUSE_BLK2_WDATA1 = EFUSE_BLK2_WDATA1(self.channel, self.chipv)
        self.EFUSE_BLK2_WDATA2 = EFUSE_BLK2_WDATA2(self.channel, self.chipv)
        self.EFUSE_BLK2_WDATA3 = EFUSE_BLK2_WDATA3(self.channel, self.chipv)
        self.EFUSE_BLK2_WDATA4 = EFUSE_BLK2_WDATA4(self.channel, self.chipv)
        self.EFUSE_BLK2_WDATA5 = EFUSE_BLK2_WDATA5(self.channel, self.chipv)
        self.EFUSE_BLK2_WDATA6 = EFUSE_BLK2_WDATA6(self.channel, self.chipv)
        self.EFUSE_BLK2_WDATA7 = EFUSE_BLK2_WDATA7(self.channel, self.chipv)
        self.EFUSE_BLK3_WDATA0 = EFUSE_BLK3_WDATA0(self.channel, self.chipv)
        self.EFUSE_BLK3_WDATA1 = EFUSE_BLK3_WDATA1(self.channel, self.chipv)
        self.EFUSE_BLK3_WDATA2 = EFUSE_BLK3_WDATA2(self.channel, self.chipv)
        self.EFUSE_BLK3_WDATA3 = EFUSE_BLK3_WDATA3(self.channel, self.chipv)
        self.EFUSE_BLK3_WDATA4 = EFUSE_BLK3_WDATA4(self.channel, self.chipv)
        self.EFUSE_BLK3_WDATA5 = EFUSE_BLK3_WDATA5(self.channel, self.chipv)
        self.EFUSE_BLK3_WDATA6 = EFUSE_BLK3_WDATA6(self.channel, self.chipv)
        self.EFUSE_BLK3_WDATA7 = EFUSE_BLK3_WDATA7(self.channel, self.chipv)
        self.EFUSE_CLK = EFUSE_CLK(self.channel, self.chipv)
        self.EFUSE_CONF = EFUSE_CONF(self.channel, self.chipv)
        self.EFUSE_STATUS = EFUSE_STATUS(self.channel, self.chipv)
        self.EFUSE_CMD = EFUSE_CMD(self.channel, self.chipv)
        self.EFUSE_INT_RAW = EFUSE_INT_RAW(self.channel, self.chipv)
        self.EFUSE_INT_ST = EFUSE_INT_ST(self.channel, self.chipv)
        self.EFUSE_INT_ENA = EFUSE_INT_ENA(self.channel, self.chipv)
        self.EFUSE_INT_CLR = EFUSE_INT_CLR(self.channel, self.chipv)
        self.EFUSE_DAC_CONF = EFUSE_DAC_CONF(self.channel, self.chipv)
        self.EFUSE_DEC_STATUS = EFUSE_DEC_STATUS(self.channel, self.chipv)
        self.EFUSE_DATE = EFUSE_DATE(self.channel, self.chipv)
class EFUSE_BLK0_RDATA0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x0
        self.__rd_flash_crypt_cnt_lsb = 20
        self.__rd_flash_crypt_cnt_msb = 27
        self.__rd_efuse_rd_dis_lsb = 16
        self.__rd_efuse_rd_dis_msb = 19
        self.__rd_efuse_wr_dis_lsb = 0
        self.__rd_efuse_wr_dis_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rd_flash_crypt_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rd_flash_crypt_cnt_msb, self.__rd_flash_crypt_cnt_lsb)
    @rd_flash_crypt_cnt.setter
    def rd_flash_crypt_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_flash_crypt_cnt_msb, self.__rd_flash_crypt_cnt_lsb, value)

    @property
    def rd_efuse_rd_dis(self):
        return self.__MEM.rdm(self.__addr, self.__rd_efuse_rd_dis_msb, self.__rd_efuse_rd_dis_lsb)
    @rd_efuse_rd_dis.setter
    def rd_efuse_rd_dis(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_efuse_rd_dis_msb, self.__rd_efuse_rd_dis_lsb, value)

    @property
    def rd_efuse_wr_dis(self):
        return self.__MEM.rdm(self.__addr, self.__rd_efuse_wr_dis_msb, self.__rd_efuse_wr_dis_lsb)
    @rd_efuse_wr_dis.setter
    def rd_efuse_wr_dis(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_efuse_wr_dis_msb, self.__rd_efuse_wr_dis_lsb, value)
class EFUSE_BLK0_RDATA1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x4
        self.__rd_wifi_mac_crc_low_lsb = 0
        self.__rd_wifi_mac_crc_low_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rd_wifi_mac_crc_low(self):
        return self.__MEM.rdm(self.__addr, self.__rd_wifi_mac_crc_low_msb, self.__rd_wifi_mac_crc_low_lsb)
    @rd_wifi_mac_crc_low.setter
    def rd_wifi_mac_crc_low(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_wifi_mac_crc_low_msb, self.__rd_wifi_mac_crc_low_lsb, value)
class EFUSE_BLK0_RDATA2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x8
        self.__rd_wifi_mac_crc_high_lsb = 0
        self.__rd_wifi_mac_crc_high_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rd_wifi_mac_crc_high(self):
        return self.__MEM.rdm(self.__addr, self.__rd_wifi_mac_crc_high_msb, self.__rd_wifi_mac_crc_high_lsb)
    @rd_wifi_mac_crc_high.setter
    def rd_wifi_mac_crc_high(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_wifi_mac_crc_high_msb, self.__rd_wifi_mac_crc_high_lsb, value)
class EFUSE_BLK0_RDATA3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xc
        self.__rd_chip_ver_reserve_lsb = 4
        self.__rd_chip_ver_reserve_msb = 16
        self.__rd_chip_ver_dis_cache_lsb = 3
        self.__rd_chip_ver_dis_cache_msb = 3
        self.__rd_chip_ver_32pad_lsb = 2
        self.__rd_chip_ver_32pad_msb = 2
        self.__rd_chip_ver_dis_bt_lsb = 1
        self.__rd_chip_ver_dis_bt_msb = 1
        self.__rd_chip_ver_dis_app_cpu_lsb = 0
        self.__rd_chip_ver_dis_app_cpu_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rd_chip_ver_reserve(self):
        return self.__MEM.rdm(self.__addr, self.__rd_chip_ver_reserve_msb, self.__rd_chip_ver_reserve_lsb)
    @rd_chip_ver_reserve.setter
    def rd_chip_ver_reserve(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_chip_ver_reserve_msb, self.__rd_chip_ver_reserve_lsb, value)

    @property
    def rd_chip_ver_dis_cache(self):
        return self.__MEM.rdm(self.__addr, self.__rd_chip_ver_dis_cache_msb, self.__rd_chip_ver_dis_cache_lsb)
    @rd_chip_ver_dis_cache.setter
    def rd_chip_ver_dis_cache(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_chip_ver_dis_cache_msb, self.__rd_chip_ver_dis_cache_lsb, value)

    @property
    def rd_chip_ver_32pad(self):
        return self.__MEM.rdm(self.__addr, self.__rd_chip_ver_32pad_msb, self.__rd_chip_ver_32pad_lsb)
    @rd_chip_ver_32pad.setter
    def rd_chip_ver_32pad(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_chip_ver_32pad_msb, self.__rd_chip_ver_32pad_lsb, value)

    @property
    def rd_chip_ver_dis_bt(self):
        return self.__MEM.rdm(self.__addr, self.__rd_chip_ver_dis_bt_msb, self.__rd_chip_ver_dis_bt_lsb)
    @rd_chip_ver_dis_bt.setter
    def rd_chip_ver_dis_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_chip_ver_dis_bt_msb, self.__rd_chip_ver_dis_bt_lsb, value)

    @property
    def rd_chip_ver_dis_app_cpu(self):
        return self.__MEM.rdm(self.__addr, self.__rd_chip_ver_dis_app_cpu_msb, self.__rd_chip_ver_dis_app_cpu_lsb)
    @rd_chip_ver_dis_app_cpu.setter
    def rd_chip_ver_dis_app_cpu(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_chip_ver_dis_app_cpu_msb, self.__rd_chip_ver_dis_app_cpu_lsb, value)
class EFUSE_BLK0_RDATA4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x10
        self.__rd_sdio_force_lsb = 16
        self.__rd_sdio_force_msb = 16
        self.__rd_sdio_tieh_lsb = 15
        self.__rd_sdio_tieh_msb = 15
        self.__rd_xpd_sdio_reg_lsb = 14
        self.__rd_xpd_sdio_reg_msb = 14
        self.__rd_sdio_drefl_lsb = 12
        self.__rd_sdio_drefl_msb = 13
        self.__rd_sdio_drefm_lsb = 10
        self.__rd_sdio_drefm_msb = 11
        self.__rd_sdio_drefh_lsb = 8
        self.__rd_sdio_drefh_msb = 9
        self.__rd_ck8m_freq_lsb = 0
        self.__rd_ck8m_freq_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rd_sdio_force(self):
        return self.__MEM.rdm(self.__addr, self.__rd_sdio_force_msb, self.__rd_sdio_force_lsb)
    @rd_sdio_force.setter
    def rd_sdio_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_sdio_force_msb, self.__rd_sdio_force_lsb, value)

    @property
    def rd_sdio_tieh(self):
        return self.__MEM.rdm(self.__addr, self.__rd_sdio_tieh_msb, self.__rd_sdio_tieh_lsb)
    @rd_sdio_tieh.setter
    def rd_sdio_tieh(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_sdio_tieh_msb, self.__rd_sdio_tieh_lsb, value)

    @property
    def rd_xpd_sdio_reg(self):
        return self.__MEM.rdm(self.__addr, self.__rd_xpd_sdio_reg_msb, self.__rd_xpd_sdio_reg_lsb)
    @rd_xpd_sdio_reg.setter
    def rd_xpd_sdio_reg(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_xpd_sdio_reg_msb, self.__rd_xpd_sdio_reg_lsb, value)

    @property
    def rd_sdio_drefl(self):
        return self.__MEM.rdm(self.__addr, self.__rd_sdio_drefl_msb, self.__rd_sdio_drefl_lsb)
    @rd_sdio_drefl.setter
    def rd_sdio_drefl(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_sdio_drefl_msb, self.__rd_sdio_drefl_lsb, value)

    @property
    def rd_sdio_drefm(self):
        return self.__MEM.rdm(self.__addr, self.__rd_sdio_drefm_msb, self.__rd_sdio_drefm_lsb)
    @rd_sdio_drefm.setter
    def rd_sdio_drefm(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_sdio_drefm_msb, self.__rd_sdio_drefm_lsb, value)

    @property
    def rd_sdio_drefh(self):
        return self.__MEM.rdm(self.__addr, self.__rd_sdio_drefh_msb, self.__rd_sdio_drefh_lsb)
    @rd_sdio_drefh.setter
    def rd_sdio_drefh(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_sdio_drefh_msb, self.__rd_sdio_drefh_lsb, value)

    @property
    def rd_ck8m_freq(self):
        return self.__MEM.rdm(self.__addr, self.__rd_ck8m_freq_msb, self.__rd_ck8m_freq_lsb)
    @rd_ck8m_freq.setter
    def rd_ck8m_freq(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_ck8m_freq_msb, self.__rd_ck8m_freq_lsb, value)
class EFUSE_BLK0_RDATA5(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x14
        self.__rd_flash_crypt_config_lsb = 28
        self.__rd_flash_crypt_config_msb = 31
        self.__rd_inst_config_lsb = 20
        self.__rd_inst_config_msb = 27
        self.__rd_spi_pad_config_lsb = 0
        self.__rd_spi_pad_config_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rd_flash_crypt_config(self):
        return self.__MEM.rdm(self.__addr, self.__rd_flash_crypt_config_msb, self.__rd_flash_crypt_config_lsb)
    @rd_flash_crypt_config.setter
    def rd_flash_crypt_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_flash_crypt_config_msb, self.__rd_flash_crypt_config_lsb, value)

    @property
    def rd_inst_config(self):
        return self.__MEM.rdm(self.__addr, self.__rd_inst_config_msb, self.__rd_inst_config_lsb)
    @rd_inst_config.setter
    def rd_inst_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_inst_config_msb, self.__rd_inst_config_lsb, value)

    @property
    def rd_spi_pad_config(self):
        return self.__MEM.rdm(self.__addr, self.__rd_spi_pad_config_msb, self.__rd_spi_pad_config_lsb)
    @rd_spi_pad_config.setter
    def rd_spi_pad_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_spi_pad_config_msb, self.__rd_spi_pad_config_lsb, value)
class EFUSE_BLK0_RDATA6(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x18
        self.__rd_key_status_lsb = 10
        self.__rd_key_status_msb = 10
        self.__rd_disable_dl_cache_lsb = 9
        self.__rd_disable_dl_cache_msb = 9
        self.__rd_disable_dl_decrypt_lsb = 8
        self.__rd_disable_dl_decrypt_msb = 8
        self.__rd_disable_dl_encrypt_lsb = 7
        self.__rd_disable_dl_encrypt_msb = 7
        self.__rd_disable_jtag_lsb = 6
        self.__rd_disable_jtag_msb = 6
        self.__rd_abs_done_1_lsb = 5
        self.__rd_abs_done_1_msb = 5
        self.__rd_abs_done_0_lsb = 4
        self.__rd_abs_done_0_msb = 4
        self.__rd_disable_sdio_host_lsb = 3
        self.__rd_disable_sdio_host_msb = 3
        self.__rd_dig_reserve_lsb = 2
        self.__rd_dig_reserve_msb = 2
        self.__rd_coding_scheme_lsb = 0
        self.__rd_coding_scheme_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rd_key_status(self):
        return self.__MEM.rdm(self.__addr, self.__rd_key_status_msb, self.__rd_key_status_lsb)
    @rd_key_status.setter
    def rd_key_status(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_key_status_msb, self.__rd_key_status_lsb, value)

    @property
    def rd_disable_dl_cache(self):
        return self.__MEM.rdm(self.__addr, self.__rd_disable_dl_cache_msb, self.__rd_disable_dl_cache_lsb)
    @rd_disable_dl_cache.setter
    def rd_disable_dl_cache(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_disable_dl_cache_msb, self.__rd_disable_dl_cache_lsb, value)

    @property
    def rd_disable_dl_decrypt(self):
        return self.__MEM.rdm(self.__addr, self.__rd_disable_dl_decrypt_msb, self.__rd_disable_dl_decrypt_lsb)
    @rd_disable_dl_decrypt.setter
    def rd_disable_dl_decrypt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_disable_dl_decrypt_msb, self.__rd_disable_dl_decrypt_lsb, value)

    @property
    def rd_disable_dl_encrypt(self):
        return self.__MEM.rdm(self.__addr, self.__rd_disable_dl_encrypt_msb, self.__rd_disable_dl_encrypt_lsb)
    @rd_disable_dl_encrypt.setter
    def rd_disable_dl_encrypt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_disable_dl_encrypt_msb, self.__rd_disable_dl_encrypt_lsb, value)

    @property
    def rd_disable_jtag(self):
        return self.__MEM.rdm(self.__addr, self.__rd_disable_jtag_msb, self.__rd_disable_jtag_lsb)
    @rd_disable_jtag.setter
    def rd_disable_jtag(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_disable_jtag_msb, self.__rd_disable_jtag_lsb, value)

    @property
    def rd_abs_done_1(self):
        return self.__MEM.rdm(self.__addr, self.__rd_abs_done_1_msb, self.__rd_abs_done_1_lsb)
    @rd_abs_done_1.setter
    def rd_abs_done_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_abs_done_1_msb, self.__rd_abs_done_1_lsb, value)

    @property
    def rd_abs_done_0(self):
        return self.__MEM.rdm(self.__addr, self.__rd_abs_done_0_msb, self.__rd_abs_done_0_lsb)
    @rd_abs_done_0.setter
    def rd_abs_done_0(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_abs_done_0_msb, self.__rd_abs_done_0_lsb, value)

    @property
    def rd_disable_sdio_host(self):
        return self.__MEM.rdm(self.__addr, self.__rd_disable_sdio_host_msb, self.__rd_disable_sdio_host_lsb)
    @rd_disable_sdio_host.setter
    def rd_disable_sdio_host(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_disable_sdio_host_msb, self.__rd_disable_sdio_host_lsb, value)

    @property
    def rd_dig_reserve(self):
        return self.__MEM.rdm(self.__addr, self.__rd_dig_reserve_msb, self.__rd_dig_reserve_lsb)
    @rd_dig_reserve.setter
    def rd_dig_reserve(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_dig_reserve_msb, self.__rd_dig_reserve_lsb, value)

    @property
    def rd_coding_scheme(self):
        return self.__MEM.rdm(self.__addr, self.__rd_coding_scheme_msb, self.__rd_coding_scheme_lsb)
    @rd_coding_scheme.setter
    def rd_coding_scheme(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_coding_scheme_msb, self.__rd_coding_scheme_lsb, value)
class EFUSE_BLK0_WDATA0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x1c
        self.__reg_flash_crypt_cnt_lsb = 20
        self.__reg_flash_crypt_cnt_msb = 27
        self.__reg_efuse_rd_dis_lsb = 16
        self.__reg_efuse_rd_dis_msb = 19
        self.__reg_efuse_wr_dis_lsb = 0
        self.__reg_efuse_wr_dis_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_flash_crypt_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_flash_crypt_cnt_msb, self.__reg_flash_crypt_cnt_lsb)
    @reg_flash_crypt_cnt.setter
    def reg_flash_crypt_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_flash_crypt_cnt_msb, self.__reg_flash_crypt_cnt_lsb, value)

    @property
    def reg_efuse_rd_dis(self):
        return self.__MEM.rdm(self.__addr, self.__reg_efuse_rd_dis_msb, self.__reg_efuse_rd_dis_lsb)
    @reg_efuse_rd_dis.setter
    def reg_efuse_rd_dis(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_efuse_rd_dis_msb, self.__reg_efuse_rd_dis_lsb, value)

    @property
    def reg_efuse_wr_dis(self):
        return self.__MEM.rdm(self.__addr, self.__reg_efuse_wr_dis_msb, self.__reg_efuse_wr_dis_lsb)
    @reg_efuse_wr_dis.setter
    def reg_efuse_wr_dis(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_efuse_wr_dis_msb, self.__reg_efuse_wr_dis_lsb, value)
class EFUSE_BLK0_WDATA1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x20
        self.__reg_wifi_mac_crc_low_lsb = 0
        self.__reg_wifi_mac_crc_low_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wifi_mac_crc_low(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wifi_mac_crc_low_msb, self.__reg_wifi_mac_crc_low_lsb)
    @reg_wifi_mac_crc_low.setter
    def reg_wifi_mac_crc_low(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wifi_mac_crc_low_msb, self.__reg_wifi_mac_crc_low_lsb, value)
class EFUSE_BLK0_WDATA2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x24
        self.__reg_wifi_mac_crc_high_lsb = 0
        self.__reg_wifi_mac_crc_high_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wifi_mac_crc_high(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wifi_mac_crc_high_msb, self.__reg_wifi_mac_crc_high_lsb)
    @reg_wifi_mac_crc_high.setter
    def reg_wifi_mac_crc_high(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wifi_mac_crc_high_msb, self.__reg_wifi_mac_crc_high_lsb, value)
class EFUSE_BLK0_WDATA3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x28
        self.__reg_chip_ver_reserve_lsb = 4
        self.__reg_chip_ver_reserve_msb = 16
        self.__reg_chip_ver_dis_cache_lsb = 3
        self.__reg_chip_ver_dis_cache_msb = 3
        self.__reg_chip_ver_32pad_lsb = 2
        self.__reg_chip_ver_32pad_msb = 2
        self.__reg_chip_ver_dis_bt_lsb = 1
        self.__reg_chip_ver_dis_bt_msb = 1
        self.__reg_chip_ver_dis_app_cpu_lsb = 0
        self.__reg_chip_ver_dis_app_cpu_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_chip_ver_reserve(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chip_ver_reserve_msb, self.__reg_chip_ver_reserve_lsb)
    @reg_chip_ver_reserve.setter
    def reg_chip_ver_reserve(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chip_ver_reserve_msb, self.__reg_chip_ver_reserve_lsb, value)

    @property
    def reg_chip_ver_dis_cache(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chip_ver_dis_cache_msb, self.__reg_chip_ver_dis_cache_lsb)
    @reg_chip_ver_dis_cache.setter
    def reg_chip_ver_dis_cache(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chip_ver_dis_cache_msb, self.__reg_chip_ver_dis_cache_lsb, value)

    @property
    def reg_chip_ver_32pad(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chip_ver_32pad_msb, self.__reg_chip_ver_32pad_lsb)
    @reg_chip_ver_32pad.setter
    def reg_chip_ver_32pad(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chip_ver_32pad_msb, self.__reg_chip_ver_32pad_lsb, value)

    @property
    def reg_chip_ver_dis_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chip_ver_dis_bt_msb, self.__reg_chip_ver_dis_bt_lsb)
    @reg_chip_ver_dis_bt.setter
    def reg_chip_ver_dis_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chip_ver_dis_bt_msb, self.__reg_chip_ver_dis_bt_lsb, value)

    @property
    def reg_chip_ver_dis_app_cpu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chip_ver_dis_app_cpu_msb, self.__reg_chip_ver_dis_app_cpu_lsb)
    @reg_chip_ver_dis_app_cpu.setter
    def reg_chip_ver_dis_app_cpu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chip_ver_dis_app_cpu_msb, self.__reg_chip_ver_dis_app_cpu_lsb, value)
class EFUSE_BLK0_WDATA4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x2c
        self.__reg_sdio_force_lsb = 16
        self.__reg_sdio_force_msb = 16
        self.__reg_sdio_tieh_lsb = 15
        self.__reg_sdio_tieh_msb = 15
        self.__reg_xpd_sdio_reg_lsb = 14
        self.__reg_xpd_sdio_reg_msb = 14
        self.__reg_sdio_drefl_lsb = 12
        self.__reg_sdio_drefl_msb = 13
        self.__reg_sdio_drefm_lsb = 10
        self.__reg_sdio_drefm_msb = 11
        self.__reg_sdio_drefh_lsb = 8
        self.__reg_sdio_drefh_msb = 9
        self.__reg_ck8m_freq_lsb = 0
        self.__reg_ck8m_freq_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sdio_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sdio_force_msb, self.__reg_sdio_force_lsb)
    @reg_sdio_force.setter
    def reg_sdio_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sdio_force_msb, self.__reg_sdio_force_lsb, value)

    @property
    def reg_sdio_tieh(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sdio_tieh_msb, self.__reg_sdio_tieh_lsb)
    @reg_sdio_tieh.setter
    def reg_sdio_tieh(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sdio_tieh_msb, self.__reg_sdio_tieh_lsb, value)

    @property
    def reg_xpd_sdio_reg(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xpd_sdio_reg_msb, self.__reg_xpd_sdio_reg_lsb)
    @reg_xpd_sdio_reg.setter
    def reg_xpd_sdio_reg(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xpd_sdio_reg_msb, self.__reg_xpd_sdio_reg_lsb, value)

    @property
    def reg_sdio_drefl(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sdio_drefl_msb, self.__reg_sdio_drefl_lsb)
    @reg_sdio_drefl.setter
    def reg_sdio_drefl(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sdio_drefl_msb, self.__reg_sdio_drefl_lsb, value)

    @property
    def reg_sdio_drefm(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sdio_drefm_msb, self.__reg_sdio_drefm_lsb)
    @reg_sdio_drefm.setter
    def reg_sdio_drefm(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sdio_drefm_msb, self.__reg_sdio_drefm_lsb, value)

    @property
    def reg_sdio_drefh(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sdio_drefh_msb, self.__reg_sdio_drefh_lsb)
    @reg_sdio_drefh.setter
    def reg_sdio_drefh(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sdio_drefh_msb, self.__reg_sdio_drefh_lsb, value)

    @property
    def reg_ck8m_freq(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ck8m_freq_msb, self.__reg_ck8m_freq_lsb)
    @reg_ck8m_freq.setter
    def reg_ck8m_freq(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ck8m_freq_msb, self.__reg_ck8m_freq_lsb, value)
class EFUSE_BLK0_WDATA5(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x30
        self.__reg_flash_crypt_config_lsb = 28
        self.__reg_flash_crypt_config_msb = 31
        self.__reg_inst_config_lsb = 20
        self.__reg_inst_config_msb = 27
        self.__reg_spi_pad_config_lsb = 0
        self.__reg_spi_pad_config_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_flash_crypt_config(self):
        return self.__MEM.rdm(self.__addr, self.__reg_flash_crypt_config_msb, self.__reg_flash_crypt_config_lsb)
    @reg_flash_crypt_config.setter
    def reg_flash_crypt_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_flash_crypt_config_msb, self.__reg_flash_crypt_config_lsb, value)

    @property
    def reg_inst_config(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inst_config_msb, self.__reg_inst_config_lsb)
    @reg_inst_config.setter
    def reg_inst_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inst_config_msb, self.__reg_inst_config_lsb, value)

    @property
    def reg_spi_pad_config(self):
        return self.__MEM.rdm(self.__addr, self.__reg_spi_pad_config_msb, self.__reg_spi_pad_config_lsb)
    @reg_spi_pad_config.setter
    def reg_spi_pad_config(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_spi_pad_config_msb, self.__reg_spi_pad_config_lsb, value)
class EFUSE_BLK0_WDATA6(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x34
        self.__reg_key_status_lsb = 10
        self.__reg_key_status_msb = 10
        self.__reg_disable_dl_cache_lsb = 9
        self.__reg_disable_dl_cache_msb = 9
        self.__reg_disable_dl_decrypt_lsb = 8
        self.__reg_disable_dl_decrypt_msb = 8
        self.__reg_disable_dl_encrypt_lsb = 7
        self.__reg_disable_dl_encrypt_msb = 7
        self.__reg_disable_jtag_lsb = 6
        self.__reg_disable_jtag_msb = 6
        self.__reg_abs_done_1_lsb = 5
        self.__reg_abs_done_1_msb = 5
        self.__reg_abs_done_0_lsb = 4
        self.__reg_abs_done_0_msb = 4
        self.__reg_disable_sdio_host_lsb = 3
        self.__reg_disable_sdio_host_msb = 3
        self.__reg_dig_reserve_lsb = 2
        self.__reg_dig_reserve_msb = 2
        self.__reg_coding_scheme_lsb = 0
        self.__reg_coding_scheme_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_key_status(self):
        return self.__MEM.rdm(self.__addr, self.__reg_key_status_msb, self.__reg_key_status_lsb)
    @reg_key_status.setter
    def reg_key_status(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_key_status_msb, self.__reg_key_status_lsb, value)

    @property
    def reg_disable_dl_cache(self):
        return self.__MEM.rdm(self.__addr, self.__reg_disable_dl_cache_msb, self.__reg_disable_dl_cache_lsb)
    @reg_disable_dl_cache.setter
    def reg_disable_dl_cache(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_disable_dl_cache_msb, self.__reg_disable_dl_cache_lsb, value)

    @property
    def reg_disable_dl_decrypt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_disable_dl_decrypt_msb, self.__reg_disable_dl_decrypt_lsb)
    @reg_disable_dl_decrypt.setter
    def reg_disable_dl_decrypt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_disable_dl_decrypt_msb, self.__reg_disable_dl_decrypt_lsb, value)

    @property
    def reg_disable_dl_encrypt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_disable_dl_encrypt_msb, self.__reg_disable_dl_encrypt_lsb)
    @reg_disable_dl_encrypt.setter
    def reg_disable_dl_encrypt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_disable_dl_encrypt_msb, self.__reg_disable_dl_encrypt_lsb, value)

    @property
    def reg_disable_jtag(self):
        return self.__MEM.rdm(self.__addr, self.__reg_disable_jtag_msb, self.__reg_disable_jtag_lsb)
    @reg_disable_jtag.setter
    def reg_disable_jtag(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_disable_jtag_msb, self.__reg_disable_jtag_lsb, value)

    @property
    def reg_abs_done_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_abs_done_1_msb, self.__reg_abs_done_1_lsb)
    @reg_abs_done_1.setter
    def reg_abs_done_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_abs_done_1_msb, self.__reg_abs_done_1_lsb, value)

    @property
    def reg_abs_done_0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_abs_done_0_msb, self.__reg_abs_done_0_lsb)
    @reg_abs_done_0.setter
    def reg_abs_done_0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_abs_done_0_msb, self.__reg_abs_done_0_lsb, value)

    @property
    def reg_disable_sdio_host(self):
        return self.__MEM.rdm(self.__addr, self.__reg_disable_sdio_host_msb, self.__reg_disable_sdio_host_lsb)
    @reg_disable_sdio_host.setter
    def reg_disable_sdio_host(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_disable_sdio_host_msb, self.__reg_disable_sdio_host_lsb, value)

    @property
    def reg_dig_reserve(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dig_reserve_msb, self.__reg_dig_reserve_lsb)
    @reg_dig_reserve.setter
    def reg_dig_reserve(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dig_reserve_msb, self.__reg_dig_reserve_lsb, value)

    @property
    def reg_coding_scheme(self):
        return self.__MEM.rdm(self.__addr, self.__reg_coding_scheme_msb, self.__reg_coding_scheme_lsb)
    @reg_coding_scheme.setter
    def reg_coding_scheme(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_coding_scheme_msb, self.__reg_coding_scheme_lsb, value)
class EFUSE_BLK1_RDATA0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x38
        self.__efuse_blk1_dout0_lsb = 0
        self.__efuse_blk1_dout0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk1_dout0(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk1_dout0_msb, self.__efuse_blk1_dout0_lsb)
    @efuse_blk1_dout0.setter
    def efuse_blk1_dout0(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk1_dout0_msb, self.__efuse_blk1_dout0_lsb, value)
class EFUSE_BLK1_RDATA1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x3c
        self.__efuse_blk1_dout1_lsb = 0
        self.__efuse_blk1_dout1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk1_dout1(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk1_dout1_msb, self.__efuse_blk1_dout1_lsb)
    @efuse_blk1_dout1.setter
    def efuse_blk1_dout1(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk1_dout1_msb, self.__efuse_blk1_dout1_lsb, value)
class EFUSE_BLK1_RDATA2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x40
        self.__efuse_blk1_dout2_lsb = 0
        self.__efuse_blk1_dout2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk1_dout2(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk1_dout2_msb, self.__efuse_blk1_dout2_lsb)
    @efuse_blk1_dout2.setter
    def efuse_blk1_dout2(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk1_dout2_msb, self.__efuse_blk1_dout2_lsb, value)
class EFUSE_BLK1_RDATA3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x44
        self.__efuse_blk1_dout3_lsb = 0
        self.__efuse_blk1_dout3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk1_dout3(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk1_dout3_msb, self.__efuse_blk1_dout3_lsb)
    @efuse_blk1_dout3.setter
    def efuse_blk1_dout3(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk1_dout3_msb, self.__efuse_blk1_dout3_lsb, value)
class EFUSE_BLK1_RDATA4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x48
        self.__efuse_blk1_dout4_lsb = 0
        self.__efuse_blk1_dout4_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk1_dout4(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk1_dout4_msb, self.__efuse_blk1_dout4_lsb)
    @efuse_blk1_dout4.setter
    def efuse_blk1_dout4(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk1_dout4_msb, self.__efuse_blk1_dout4_lsb, value)
class EFUSE_BLK1_RDATA5(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x4c
        self.__efuse_blk1_dout5_lsb = 0
        self.__efuse_blk1_dout5_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk1_dout5(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk1_dout5_msb, self.__efuse_blk1_dout5_lsb)
    @efuse_blk1_dout5.setter
    def efuse_blk1_dout5(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk1_dout5_msb, self.__efuse_blk1_dout5_lsb, value)
class EFUSE_BLK1_RDATA6(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x50
        self.__efuse_blk1_dout6_lsb = 0
        self.__efuse_blk1_dout6_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk1_dout6(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk1_dout6_msb, self.__efuse_blk1_dout6_lsb)
    @efuse_blk1_dout6.setter
    def efuse_blk1_dout6(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk1_dout6_msb, self.__efuse_blk1_dout6_lsb, value)
class EFUSE_BLK1_RDATA7(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x54
        self.__efuse_blk1_dout7_lsb = 0
        self.__efuse_blk1_dout7_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk1_dout7(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk1_dout7_msb, self.__efuse_blk1_dout7_lsb)
    @efuse_blk1_dout7.setter
    def efuse_blk1_dout7(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk1_dout7_msb, self.__efuse_blk1_dout7_lsb, value)
class EFUSE_BLK2_RDATA0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x58
        self.__efuse_blk2_dout0_lsb = 0
        self.__efuse_blk2_dout0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk2_dout0(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk2_dout0_msb, self.__efuse_blk2_dout0_lsb)
    @efuse_blk2_dout0.setter
    def efuse_blk2_dout0(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk2_dout0_msb, self.__efuse_blk2_dout0_lsb, value)
class EFUSE_BLK2_RDATA1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x5c
        self.__efuse_blk2_dout1_lsb = 0
        self.__efuse_blk2_dout1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk2_dout1(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk2_dout1_msb, self.__efuse_blk2_dout1_lsb)
    @efuse_blk2_dout1.setter
    def efuse_blk2_dout1(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk2_dout1_msb, self.__efuse_blk2_dout1_lsb, value)
class EFUSE_BLK2_RDATA2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x60
        self.__efuse_blk2_dout2_lsb = 0
        self.__efuse_blk2_dout2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk2_dout2(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk2_dout2_msb, self.__efuse_blk2_dout2_lsb)
    @efuse_blk2_dout2.setter
    def efuse_blk2_dout2(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk2_dout2_msb, self.__efuse_blk2_dout2_lsb, value)
class EFUSE_BLK2_RDATA3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x64
        self.__efuse_blk2_dout3_lsb = 0
        self.__efuse_blk2_dout3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk2_dout3(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk2_dout3_msb, self.__efuse_blk2_dout3_lsb)
    @efuse_blk2_dout3.setter
    def efuse_blk2_dout3(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk2_dout3_msb, self.__efuse_blk2_dout3_lsb, value)
class EFUSE_BLK2_RDATA4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x68
        self.__efuse_blk2_dout4_lsb = 0
        self.__efuse_blk2_dout4_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk2_dout4(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk2_dout4_msb, self.__efuse_blk2_dout4_lsb)
    @efuse_blk2_dout4.setter
    def efuse_blk2_dout4(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk2_dout4_msb, self.__efuse_blk2_dout4_lsb, value)
class EFUSE_BLK2_RDATA5(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x6c
        self.__efuse_blk2_dout5_lsb = 0
        self.__efuse_blk2_dout5_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk2_dout5(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk2_dout5_msb, self.__efuse_blk2_dout5_lsb)
    @efuse_blk2_dout5.setter
    def efuse_blk2_dout5(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk2_dout5_msb, self.__efuse_blk2_dout5_lsb, value)
class EFUSE_BLK2_RDATA6(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x70
        self.__efuse_blk2_dout6_lsb = 0
        self.__efuse_blk2_dout6_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk2_dout6(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk2_dout6_msb, self.__efuse_blk2_dout6_lsb)
    @efuse_blk2_dout6.setter
    def efuse_blk2_dout6(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk2_dout6_msb, self.__efuse_blk2_dout6_lsb, value)
class EFUSE_BLK2_RDATA7(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x74
        self.__efuse_blk2_dout7_lsb = 0
        self.__efuse_blk2_dout7_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk2_dout7(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk2_dout7_msb, self.__efuse_blk2_dout7_lsb)
    @efuse_blk2_dout7.setter
    def efuse_blk2_dout7(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk2_dout7_msb, self.__efuse_blk2_dout7_lsb, value)
class EFUSE_BLK3_RDATA0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x78
        self.__efuse_blk3_dout0_lsb = 0
        self.__efuse_blk3_dout0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk3_dout0(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk3_dout0_msb, self.__efuse_blk3_dout0_lsb)
    @efuse_blk3_dout0.setter
    def efuse_blk3_dout0(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk3_dout0_msb, self.__efuse_blk3_dout0_lsb, value)
class EFUSE_BLK3_RDATA1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x7c
        self.__efuse_blk3_dout1_lsb = 0
        self.__efuse_blk3_dout1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk3_dout1(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk3_dout1_msb, self.__efuse_blk3_dout1_lsb)
    @efuse_blk3_dout1.setter
    def efuse_blk3_dout1(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk3_dout1_msb, self.__efuse_blk3_dout1_lsb, value)
class EFUSE_BLK3_RDATA2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x80
        self.__efuse_blk3_dout2_lsb = 0
        self.__efuse_blk3_dout2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk3_dout2(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk3_dout2_msb, self.__efuse_blk3_dout2_lsb)
    @efuse_blk3_dout2.setter
    def efuse_blk3_dout2(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk3_dout2_msb, self.__efuse_blk3_dout2_lsb, value)
class EFUSE_BLK3_RDATA3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x84
        self.__efuse_blk3_dout3_lsb = 0
        self.__efuse_blk3_dout3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk3_dout3(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk3_dout3_msb, self.__efuse_blk3_dout3_lsb)
    @efuse_blk3_dout3.setter
    def efuse_blk3_dout3(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk3_dout3_msb, self.__efuse_blk3_dout3_lsb, value)
class EFUSE_BLK3_RDATA4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x88
        self.__efuse_blk3_dout4_lsb = 0
        self.__efuse_blk3_dout4_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk3_dout4(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk3_dout4_msb, self.__efuse_blk3_dout4_lsb)
    @efuse_blk3_dout4.setter
    def efuse_blk3_dout4(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk3_dout4_msb, self.__efuse_blk3_dout4_lsb, value)
class EFUSE_BLK3_RDATA5(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x8c
        self.__efuse_blk3_dout5_lsb = 0
        self.__efuse_blk3_dout5_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk3_dout5(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk3_dout5_msb, self.__efuse_blk3_dout5_lsb)
    @efuse_blk3_dout5.setter
    def efuse_blk3_dout5(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk3_dout5_msb, self.__efuse_blk3_dout5_lsb, value)
class EFUSE_BLK3_RDATA6(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x90
        self.__efuse_blk3_dout6_lsb = 0
        self.__efuse_blk3_dout6_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk3_dout6(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk3_dout6_msb, self.__efuse_blk3_dout6_lsb)
    @efuse_blk3_dout6.setter
    def efuse_blk3_dout6(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk3_dout6_msb, self.__efuse_blk3_dout6_lsb, value)
class EFUSE_BLK3_RDATA7(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x94
        self.__efuse_blk3_dout7_lsb = 0
        self.__efuse_blk3_dout7_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk3_dout7(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk3_dout7_msb, self.__efuse_blk3_dout7_lsb)
    @efuse_blk3_dout7.setter
    def efuse_blk3_dout7(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk3_dout7_msb, self.__efuse_blk3_dout7_lsb, value)
class EFUSE_BLK1_WDATA0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x98
        self.__efuse_blk1_din0_lsb = 0
        self.__efuse_blk1_din0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk1_din0(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk1_din0_msb, self.__efuse_blk1_din0_lsb)
    @efuse_blk1_din0.setter
    def efuse_blk1_din0(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk1_din0_msb, self.__efuse_blk1_din0_lsb, value)
class EFUSE_BLK1_WDATA1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x9c
        self.__efuse_blk1_din1_lsb = 0
        self.__efuse_blk1_din1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk1_din1(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk1_din1_msb, self.__efuse_blk1_din1_lsb)
    @efuse_blk1_din1.setter
    def efuse_blk1_din1(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk1_din1_msb, self.__efuse_blk1_din1_lsb, value)
class EFUSE_BLK1_WDATA2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xa0
        self.__efuse_blk1_din2_lsb = 0
        self.__efuse_blk1_din2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk1_din2(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk1_din2_msb, self.__efuse_blk1_din2_lsb)
    @efuse_blk1_din2.setter
    def efuse_blk1_din2(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk1_din2_msb, self.__efuse_blk1_din2_lsb, value)
class EFUSE_BLK1_WDATA3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xa4
        self.__efuse_blk1_din3_lsb = 0
        self.__efuse_blk1_din3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk1_din3(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk1_din3_msb, self.__efuse_blk1_din3_lsb)
    @efuse_blk1_din3.setter
    def efuse_blk1_din3(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk1_din3_msb, self.__efuse_blk1_din3_lsb, value)
class EFUSE_BLK1_WDATA4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xa8
        self.__efuse_blk1_din4_lsb = 0
        self.__efuse_blk1_din4_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk1_din4(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk1_din4_msb, self.__efuse_blk1_din4_lsb)
    @efuse_blk1_din4.setter
    def efuse_blk1_din4(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk1_din4_msb, self.__efuse_blk1_din4_lsb, value)
class EFUSE_BLK1_WDATA5(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xac
        self.__efuse_blk1_din5_lsb = 0
        self.__efuse_blk1_din5_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk1_din5(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk1_din5_msb, self.__efuse_blk1_din5_lsb)
    @efuse_blk1_din5.setter
    def efuse_blk1_din5(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk1_din5_msb, self.__efuse_blk1_din5_lsb, value)
class EFUSE_BLK1_WDATA6(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xb0
        self.__efuse_blk1_din6_lsb = 0
        self.__efuse_blk1_din6_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk1_din6(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk1_din6_msb, self.__efuse_blk1_din6_lsb)
    @efuse_blk1_din6.setter
    def efuse_blk1_din6(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk1_din6_msb, self.__efuse_blk1_din6_lsb, value)
class EFUSE_BLK1_WDATA7(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xb4
        self.__efuse_blk1_din7_lsb = 0
        self.__efuse_blk1_din7_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk1_din7(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk1_din7_msb, self.__efuse_blk1_din7_lsb)
    @efuse_blk1_din7.setter
    def efuse_blk1_din7(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk1_din7_msb, self.__efuse_blk1_din7_lsb, value)
class EFUSE_BLK2_WDATA0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xb8
        self.__efuse_blk2_din0_lsb = 0
        self.__efuse_blk2_din0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk2_din0(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk2_din0_msb, self.__efuse_blk2_din0_lsb)
    @efuse_blk2_din0.setter
    def efuse_blk2_din0(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk2_din0_msb, self.__efuse_blk2_din0_lsb, value)
class EFUSE_BLK2_WDATA1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xbc
        self.__efuse_blk2_din1_lsb = 0
        self.__efuse_blk2_din1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk2_din1(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk2_din1_msb, self.__efuse_blk2_din1_lsb)
    @efuse_blk2_din1.setter
    def efuse_blk2_din1(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk2_din1_msb, self.__efuse_blk2_din1_lsb, value)
class EFUSE_BLK2_WDATA2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xc0
        self.__efuse_blk2_din2_lsb = 0
        self.__efuse_blk2_din2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk2_din2(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk2_din2_msb, self.__efuse_blk2_din2_lsb)
    @efuse_blk2_din2.setter
    def efuse_blk2_din2(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk2_din2_msb, self.__efuse_blk2_din2_lsb, value)
class EFUSE_BLK2_WDATA3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xc4
        self.__efuse_blk2_din3_lsb = 0
        self.__efuse_blk2_din3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk2_din3(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk2_din3_msb, self.__efuse_blk2_din3_lsb)
    @efuse_blk2_din3.setter
    def efuse_blk2_din3(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk2_din3_msb, self.__efuse_blk2_din3_lsb, value)
class EFUSE_BLK2_WDATA4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xc8
        self.__efuse_blk2_din4_lsb = 0
        self.__efuse_blk2_din4_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk2_din4(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk2_din4_msb, self.__efuse_blk2_din4_lsb)
    @efuse_blk2_din4.setter
    def efuse_blk2_din4(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk2_din4_msb, self.__efuse_blk2_din4_lsb, value)
class EFUSE_BLK2_WDATA5(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xcc
        self.__efuse_blk2_din5_lsb = 0
        self.__efuse_blk2_din5_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk2_din5(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk2_din5_msb, self.__efuse_blk2_din5_lsb)
    @efuse_blk2_din5.setter
    def efuse_blk2_din5(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk2_din5_msb, self.__efuse_blk2_din5_lsb, value)
class EFUSE_BLK2_WDATA6(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xd0
        self.__efuse_blk2_din6_lsb = 0
        self.__efuse_blk2_din6_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk2_din6(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk2_din6_msb, self.__efuse_blk2_din6_lsb)
    @efuse_blk2_din6.setter
    def efuse_blk2_din6(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk2_din6_msb, self.__efuse_blk2_din6_lsb, value)
class EFUSE_BLK2_WDATA7(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xd4
        self.__efuse_blk2_din7_lsb = 0
        self.__efuse_blk2_din7_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk2_din7(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk2_din7_msb, self.__efuse_blk2_din7_lsb)
    @efuse_blk2_din7.setter
    def efuse_blk2_din7(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk2_din7_msb, self.__efuse_blk2_din7_lsb, value)
class EFUSE_BLK3_WDATA0(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xd8
        self.__efuse_blk3_din0_lsb = 0
        self.__efuse_blk3_din0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk3_din0(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk3_din0_msb, self.__efuse_blk3_din0_lsb)
    @efuse_blk3_din0.setter
    def efuse_blk3_din0(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk3_din0_msb, self.__efuse_blk3_din0_lsb, value)
class EFUSE_BLK3_WDATA1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xdc
        self.__efuse_blk3_din1_lsb = 0
        self.__efuse_blk3_din1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk3_din1(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk3_din1_msb, self.__efuse_blk3_din1_lsb)
    @efuse_blk3_din1.setter
    def efuse_blk3_din1(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk3_din1_msb, self.__efuse_blk3_din1_lsb, value)
class EFUSE_BLK3_WDATA2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xe0
        self.__efuse_blk3_din2_lsb = 0
        self.__efuse_blk3_din2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk3_din2(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk3_din2_msb, self.__efuse_blk3_din2_lsb)
    @efuse_blk3_din2.setter
    def efuse_blk3_din2(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk3_din2_msb, self.__efuse_blk3_din2_lsb, value)
class EFUSE_BLK3_WDATA3(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xe4
        self.__efuse_blk3_din3_lsb = 0
        self.__efuse_blk3_din3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk3_din3(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk3_din3_msb, self.__efuse_blk3_din3_lsb)
    @efuse_blk3_din3.setter
    def efuse_blk3_din3(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk3_din3_msb, self.__efuse_blk3_din3_lsb, value)
class EFUSE_BLK3_WDATA4(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xe8
        self.__efuse_blk3_din4_lsb = 0
        self.__efuse_blk3_din4_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk3_din4(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk3_din4_msb, self.__efuse_blk3_din4_lsb)
    @efuse_blk3_din4.setter
    def efuse_blk3_din4(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk3_din4_msb, self.__efuse_blk3_din4_lsb, value)
class EFUSE_BLK3_WDATA5(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xec
        self.__efuse_blk3_din5_lsb = 0
        self.__efuse_blk3_din5_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk3_din5(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk3_din5_msb, self.__efuse_blk3_din5_lsb)
    @efuse_blk3_din5.setter
    def efuse_blk3_din5(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk3_din5_msb, self.__efuse_blk3_din5_lsb, value)
class EFUSE_BLK3_WDATA6(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xf0
        self.__efuse_blk3_din6_lsb = 0
        self.__efuse_blk3_din6_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk3_din6(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk3_din6_msb, self.__efuse_blk3_din6_lsb)
    @efuse_blk3_din6.setter
    def efuse_blk3_din6(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk3_din6_msb, self.__efuse_blk3_din6_lsb, value)
class EFUSE_BLK3_WDATA7(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xf4
        self.__efuse_blk3_din7_lsb = 0
        self.__efuse_blk3_din7_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_blk3_din7(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk3_din7_msb, self.__efuse_blk3_din7_lsb)
    @efuse_blk3_din7.setter
    def efuse_blk3_din7(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk3_din7_msb, self.__efuse_blk3_din7_lsb, value)
class EFUSE_CLK(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xf8
        self.__reg_clk_en_lsb = 16
        self.__reg_clk_en_msb = 16
        self.__efuse_clk_sel1_lsb = 8
        self.__efuse_clk_sel1_msb = 15
        self.__efuse_clk_sel0_lsb = 0
        self.__efuse_clk_sel0_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk_en_msb, self.__reg_clk_en_lsb)
    @reg_clk_en.setter
    def reg_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk_en_msb, self.__reg_clk_en_lsb, value)

    @property
    def efuse_clk_sel1(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_clk_sel1_msb, self.__efuse_clk_sel1_lsb)
    @efuse_clk_sel1.setter
    def efuse_clk_sel1(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_clk_sel1_msb, self.__efuse_clk_sel1_lsb, value)

    @property
    def efuse_clk_sel0(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_clk_sel0_msb, self.__efuse_clk_sel0_lsb)
    @efuse_clk_sel0.setter
    def efuse_clk_sel0(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_clk_sel0_msb, self.__efuse_clk_sel0_lsb, value)
class EFUSE_CONF(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xfc
        self.__efuse_force_no_wr_rd_dis_lsb = 16
        self.__efuse_force_no_wr_rd_dis_msb = 16
        self.__efuse_op_code_lsb = 0
        self.__efuse_op_code_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_force_no_wr_rd_dis(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_force_no_wr_rd_dis_msb, self.__efuse_force_no_wr_rd_dis_lsb)
    @efuse_force_no_wr_rd_dis.setter
    def efuse_force_no_wr_rd_dis(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_force_no_wr_rd_dis_msb, self.__efuse_force_no_wr_rd_dis_lsb, value)

    @property
    def efuse_op_code(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_op_code_msb, self.__efuse_op_code_lsb)
    @efuse_op_code.setter
    def efuse_op_code(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_op_code_msb, self.__efuse_op_code_lsb, value)
class EFUSE_STATUS(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x100
        self.__efuse_debug_lsb = 0
        self.__efuse_debug_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_debug(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_debug_msb, self.__efuse_debug_lsb)
    @efuse_debug.setter
    def efuse_debug(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_debug_msb, self.__efuse_debug_lsb, value)
class EFUSE_CMD(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x104
        self.__efuse_pgm_cmd_lsb = 1
        self.__efuse_pgm_cmd_msb = 1
        self.__efuse_read_cmd_lsb = 0
        self.__efuse_read_cmd_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_pgm_cmd(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_pgm_cmd_msb, self.__efuse_pgm_cmd_lsb)
    @efuse_pgm_cmd.setter
    def efuse_pgm_cmd(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_pgm_cmd_msb, self.__efuse_pgm_cmd_lsb, value)

    @property
    def efuse_read_cmd(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_read_cmd_msb, self.__efuse_read_cmd_lsb)
    @efuse_read_cmd.setter
    def efuse_read_cmd(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_read_cmd_msb, self.__efuse_read_cmd_lsb, value)
class EFUSE_INT_RAW(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x108
        self.__efuse_pgm_done_int_raw_lsb = 1
        self.__efuse_pgm_done_int_raw_msb = 1
        self.__efuse_read_done_int_raw_lsb = 0
        self.__efuse_read_done_int_raw_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_pgm_done_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_pgm_done_int_raw_msb, self.__efuse_pgm_done_int_raw_lsb)
    @efuse_pgm_done_int_raw.setter
    def efuse_pgm_done_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_pgm_done_int_raw_msb, self.__efuse_pgm_done_int_raw_lsb, value)

    @property
    def efuse_read_done_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_read_done_int_raw_msb, self.__efuse_read_done_int_raw_lsb)
    @efuse_read_done_int_raw.setter
    def efuse_read_done_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_read_done_int_raw_msb, self.__efuse_read_done_int_raw_lsb, value)
class EFUSE_INT_ST(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x10c
        self.__efuse_pgm_done_int_st_lsb = 1
        self.__efuse_pgm_done_int_st_msb = 1
        self.__efuse_read_done_int_st_lsb = 0
        self.__efuse_read_done_int_st_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_pgm_done_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_pgm_done_int_st_msb, self.__efuse_pgm_done_int_st_lsb)
    @efuse_pgm_done_int_st.setter
    def efuse_pgm_done_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_pgm_done_int_st_msb, self.__efuse_pgm_done_int_st_lsb, value)

    @property
    def efuse_read_done_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_read_done_int_st_msb, self.__efuse_read_done_int_st_lsb)
    @efuse_read_done_int_st.setter
    def efuse_read_done_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_read_done_int_st_msb, self.__efuse_read_done_int_st_lsb, value)
class EFUSE_INT_ENA(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x110
        self.__efuse_pgm_done_int_ena_lsb = 1
        self.__efuse_pgm_done_int_ena_msb = 1
        self.__efuse_read_done_int_ena_lsb = 0
        self.__efuse_read_done_int_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_pgm_done_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_pgm_done_int_ena_msb, self.__efuse_pgm_done_int_ena_lsb)
    @efuse_pgm_done_int_ena.setter
    def efuse_pgm_done_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_pgm_done_int_ena_msb, self.__efuse_pgm_done_int_ena_lsb, value)

    @property
    def efuse_read_done_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_read_done_int_ena_msb, self.__efuse_read_done_int_ena_lsb)
    @efuse_read_done_int_ena.setter
    def efuse_read_done_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_read_done_int_ena_msb, self.__efuse_read_done_int_ena_lsb, value)
class EFUSE_INT_CLR(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x114
        self.__efuse_pgm_done_int_clr_lsb = 1
        self.__efuse_pgm_done_int_clr_msb = 1
        self.__efuse_read_done_int_clr_lsb = 0
        self.__efuse_read_done_int_clr_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_pgm_done_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_pgm_done_int_clr_msb, self.__efuse_pgm_done_int_clr_lsb)
    @efuse_pgm_done_int_clr.setter
    def efuse_pgm_done_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_pgm_done_int_clr_msb, self.__efuse_pgm_done_int_clr_lsb, value)

    @property
    def efuse_read_done_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_read_done_int_clr_msb, self.__efuse_read_done_int_clr_lsb)
    @efuse_read_done_int_clr.setter
    def efuse_read_done_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_read_done_int_clr_msb, self.__efuse_read_done_int_clr_lsb, value)
class EFUSE_DAC_CONF(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x118
        self.__efuse_dac_clk_pad_sel_lsb = 8
        self.__efuse_dac_clk_pad_sel_msb = 8
        self.__efuse_dac_clk_div_lsb = 0
        self.__efuse_dac_clk_div_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_dac_clk_pad_sel(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_dac_clk_pad_sel_msb, self.__efuse_dac_clk_pad_sel_lsb)
    @efuse_dac_clk_pad_sel.setter
    def efuse_dac_clk_pad_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_dac_clk_pad_sel_msb, self.__efuse_dac_clk_pad_sel_lsb, value)

    @property
    def efuse_dac_clk_div(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_dac_clk_div_msb, self.__efuse_dac_clk_div_lsb)
    @efuse_dac_clk_div.setter
    def efuse_dac_clk_div(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_dac_clk_div_msb, self.__efuse_dac_clk_div_lsb, value)
class EFUSE_DEC_STATUS(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x11c
        self.__efuse_dec_warnings_lsb = 0
        self.__efuse_dec_warnings_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_dec_warnings(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_dec_warnings_msb, self.__efuse_dec_warnings_lsb)
    @efuse_dec_warnings.setter
    def efuse_dec_warnings(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_dec_warnings_msb, self.__efuse_dec_warnings_lsb, value)
class EFUSE_DATE(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x1fc
        self.__efuse_date_lsb = 0
        self.__efuse_date_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_date(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_date_msb, self.__efuse_date_lsb)
    @efuse_date.setter
    def efuse_date(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_date_msb, self.__efuse_date_lsb, value)
    @property
    def default_value(self):
        return 0x16042600
