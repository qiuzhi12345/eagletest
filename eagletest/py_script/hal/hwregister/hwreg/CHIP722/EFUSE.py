from hal.common import *
from hal.hwregister.hwreg.CHIP722.addr_base import *
class EFUSE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.PGM_DATA0 = PGM_DATA0(self.channel, self.chipv)
        self.PGM_DATA1 = PGM_DATA1(self.channel, self.chipv)
        self.PGM_DATA2 = PGM_DATA2(self.channel, self.chipv)
        self.PGM_DATA3 = PGM_DATA3(self.channel, self.chipv)
        self.PGM_DATA4 = PGM_DATA4(self.channel, self.chipv)
        self.PGM_DATA5 = PGM_DATA5(self.channel, self.chipv)
        self.PGM_DATA6 = PGM_DATA6(self.channel, self.chipv)
        self.PGM_DATA7 = PGM_DATA7(self.channel, self.chipv)
        self.PGM_CHECK_VALUE0 = PGM_CHECK_VALUE0(self.channel, self.chipv)
        self.PGM_CHECK_VALUE1 = PGM_CHECK_VALUE1(self.channel, self.chipv)
        self.PGM_CHECK_VALUE2 = PGM_CHECK_VALUE2(self.channel, self.chipv)
        self.RD_WR_DIS = RD_WR_DIS(self.channel, self.chipv)
        self.RD_REPEAT_DATA0 = RD_REPEAT_DATA0(self.channel, self.chipv)
        self.RD_REPEAT_DATA1 = RD_REPEAT_DATA1(self.channel, self.chipv)
        self.RD_REPEAT_DATA2 = RD_REPEAT_DATA2(self.channel, self.chipv)
        self.RD_REPEAT_DATA3 = RD_REPEAT_DATA3(self.channel, self.chipv)
        self.RD_REPEAT_DATA4 = RD_REPEAT_DATA4(self.channel, self.chipv)
        self.RD_MAC_SPI_8M_0 = RD_MAC_SPI_8M_0(self.channel, self.chipv)
        self.RD_MAC_SPI_8M_1 = RD_MAC_SPI_8M_1(self.channel, self.chipv)
        self.RD_MAC_SPI_8M_2 = RD_MAC_SPI_8M_2(self.channel, self.chipv)
        self.RD_MAC_SPI_8M_3 = RD_MAC_SPI_8M_3(self.channel, self.chipv)
        self.RD_MAC_SPI_8M_4 = RD_MAC_SPI_8M_4(self.channel, self.chipv)
        self.RD_MAC_SPI_8M_5 = RD_MAC_SPI_8M_5(self.channel, self.chipv)
        self.RD_SYS_DATA0 = RD_SYS_DATA0(self.channel, self.chipv)
        self.RD_SYS_DATA1 = RD_SYS_DATA1(self.channel, self.chipv)
        self.RD_SYS_DATA2 = RD_SYS_DATA2(self.channel, self.chipv)
        self.RD_SYS_DATA3 = RD_SYS_DATA3(self.channel, self.chipv)
        self.RD_SYS_DATA4 = RD_SYS_DATA4(self.channel, self.chipv)
        self.RD_SYS_DATA5 = RD_SYS_DATA5(self.channel, self.chipv)
        self.RD_SYS_DATA6 = RD_SYS_DATA6(self.channel, self.chipv)
        self.RD_SYS_DATA7 = RD_SYS_DATA7(self.channel, self.chipv)
        self.RD_USR_DATA0 = RD_USR_DATA0(self.channel, self.chipv)
        self.RD_USR_DATA1 = RD_USR_DATA1(self.channel, self.chipv)
        self.RD_USR_DATA2 = RD_USR_DATA2(self.channel, self.chipv)
        self.RD_USR_DATA3 = RD_USR_DATA3(self.channel, self.chipv)
        self.RD_USR_DATA4 = RD_USR_DATA4(self.channel, self.chipv)
        self.RD_USR_DATA5 = RD_USR_DATA5(self.channel, self.chipv)
        self.RD_USR_DATA6 = RD_USR_DATA6(self.channel, self.chipv)
        self.RD_USR_DATA7 = RD_USR_DATA7(self.channel, self.chipv)
        self.RD_KEY0_DATA0 = RD_KEY0_DATA0(self.channel, self.chipv)
        self.RD_KEY0_DATA1 = RD_KEY0_DATA1(self.channel, self.chipv)
        self.RD_KEY0_DATA2 = RD_KEY0_DATA2(self.channel, self.chipv)
        self.RD_KEY0_DATA3 = RD_KEY0_DATA3(self.channel, self.chipv)
        self.RD_KEY0_DATA4 = RD_KEY0_DATA4(self.channel, self.chipv)
        self.RD_KEY0_DATA5 = RD_KEY0_DATA5(self.channel, self.chipv)
        self.RD_KEY0_DATA6 = RD_KEY0_DATA6(self.channel, self.chipv)
        self.RD_KEY0_DATA7 = RD_KEY0_DATA7(self.channel, self.chipv)
        self.RD_KEY1_DATA0 = RD_KEY1_DATA0(self.channel, self.chipv)
        self.RD_KEY1_DATA1 = RD_KEY1_DATA1(self.channel, self.chipv)
        self.RD_KEY1_DATA2 = RD_KEY1_DATA2(self.channel, self.chipv)
        self.RD_KEY1_DATA3 = RD_KEY1_DATA3(self.channel, self.chipv)
        self.RD_KEY1_DATA4 = RD_KEY1_DATA4(self.channel, self.chipv)
        self.RD_KEY1_DATA5 = RD_KEY1_DATA5(self.channel, self.chipv)
        self.RD_KEY1_DATA6 = RD_KEY1_DATA6(self.channel, self.chipv)
        self.RD_KEY1_DATA7 = RD_KEY1_DATA7(self.channel, self.chipv)
        self.RD_KEY2_DATA0 = RD_KEY2_DATA0(self.channel, self.chipv)
        self.RD_KEY2_DATA1 = RD_KEY2_DATA1(self.channel, self.chipv)
        self.RD_KEY2_DATA2 = RD_KEY2_DATA2(self.channel, self.chipv)
        self.RD_KEY2_DATA3 = RD_KEY2_DATA3(self.channel, self.chipv)
        self.RD_KEY2_DATA4 = RD_KEY2_DATA4(self.channel, self.chipv)
        self.RD_KEY2_DATA5 = RD_KEY2_DATA5(self.channel, self.chipv)
        self.RD_KEY2_DATA6 = RD_KEY2_DATA6(self.channel, self.chipv)
        self.RD_KEY2_DATA7 = RD_KEY2_DATA7(self.channel, self.chipv)
        self.RD_KEY3_DATA0 = RD_KEY3_DATA0(self.channel, self.chipv)
        self.RD_KEY3_DATA1 = RD_KEY3_DATA1(self.channel, self.chipv)
        self.RD_KEY3_DATA2 = RD_KEY3_DATA2(self.channel, self.chipv)
        self.RD_KEY3_DATA3 = RD_KEY3_DATA3(self.channel, self.chipv)
        self.RD_KEY3_DATA4 = RD_KEY3_DATA4(self.channel, self.chipv)
        self.RD_KEY3_DATA5 = RD_KEY3_DATA5(self.channel, self.chipv)
        self.RD_KEY3_DATA6 = RD_KEY3_DATA6(self.channel, self.chipv)
        self.RD_KEY3_DATA7 = RD_KEY3_DATA7(self.channel, self.chipv)
        self.RD_KEY4_DATA0 = RD_KEY4_DATA0(self.channel, self.chipv)
        self.RD_KEY4_DATA1 = RD_KEY4_DATA1(self.channel, self.chipv)
        self.RD_KEY4_DATA2 = RD_KEY4_DATA2(self.channel, self.chipv)
        self.RD_KEY4_DATA3 = RD_KEY4_DATA3(self.channel, self.chipv)
        self.RD_KEY4_DATA4 = RD_KEY4_DATA4(self.channel, self.chipv)
        self.RD_KEY4_DATA5 = RD_KEY4_DATA5(self.channel, self.chipv)
        self.RD_KEY4_DATA6 = RD_KEY4_DATA6(self.channel, self.chipv)
        self.RD_KEY4_DATA7 = RD_KEY4_DATA7(self.channel, self.chipv)
        self.RD_KEY5_DATA0 = RD_KEY5_DATA0(self.channel, self.chipv)
        self.RD_KEY5_DATA1 = RD_KEY5_DATA1(self.channel, self.chipv)
        self.RD_KEY5_DATA2 = RD_KEY5_DATA2(self.channel, self.chipv)
        self.RD_KEY5_DATA3 = RD_KEY5_DATA3(self.channel, self.chipv)
        self.RD_KEY5_DATA4 = RD_KEY5_DATA4(self.channel, self.chipv)
        self.RD_KEY5_DATA5 = RD_KEY5_DATA5(self.channel, self.chipv)
        self.RD_KEY5_DATA6 = RD_KEY5_DATA6(self.channel, self.chipv)
        self.RD_KEY5_DATA7 = RD_KEY5_DATA7(self.channel, self.chipv)
        self.RD_KEY6_DATA0 = RD_KEY6_DATA0(self.channel, self.chipv)
        self.RD_KEY6_DATA1 = RD_KEY6_DATA1(self.channel, self.chipv)
        self.RD_KEY6_DATA2 = RD_KEY6_DATA2(self.channel, self.chipv)
        self.RD_KEY6_DATA3 = RD_KEY6_DATA3(self.channel, self.chipv)
        self.RD_KEY6_DATA4 = RD_KEY6_DATA4(self.channel, self.chipv)
        self.RD_KEY6_DATA5 = RD_KEY6_DATA5(self.channel, self.chipv)
        self.RD_KEY6_DATA6 = RD_KEY6_DATA6(self.channel, self.chipv)
        self.RD_KEY6_DATA7 = RD_KEY6_DATA7(self.channel, self.chipv)
        self.RD_REPEAT_ERR0 = RD_REPEAT_ERR0(self.channel, self.chipv)
        self.RD_REPEAT_ERR1 = RD_REPEAT_ERR1(self.channel, self.chipv)
        self.RD_REPEAT_ERR2 = RD_REPEAT_ERR2(self.channel, self.chipv)
        self.RD_REPEAT_ERR3 = RD_REPEAT_ERR3(self.channel, self.chipv)
        self.RD_REPEAT_ERR4 = RD_REPEAT_ERR4(self.channel, self.chipv)
        self.RD_RS_ERR0 = RD_RS_ERR0(self.channel, self.chipv)
        self.RD_RS_ERR1 = RD_RS_ERR1(self.channel, self.chipv)
        self.EFUSE_CLK = EFUSE_CLK(self.channel, self.chipv)
        self.EFUSE_CONF = EFUSE_CONF(self.channel, self.chipv)
        self.EFUSE_STATUS = EFUSE_STATUS(self.channel, self.chipv)
        self.EFUSE_CMD = EFUSE_CMD(self.channel, self.chipv)
        self.EFUSE_INT_RAW = EFUSE_INT_RAW(self.channel, self.chipv)
        self.EFUSE_INT_ST = EFUSE_INT_ST(self.channel, self.chipv)
        self.EFUSE_INT_ENA = EFUSE_INT_ENA(self.channel, self.chipv)
        self.EFUSE_INT_CLR = EFUSE_INT_CLR(self.channel, self.chipv)
        self.EFUSE_DAC_CONF = EFUSE_DAC_CONF(self.channel, self.chipv)
        self.EFUSE_RD_TIM_CONF = EFUSE_RD_TIM_CONF(self.channel, self.chipv)
        self.EFUSE_WR_TIM_CONF0 = EFUSE_WR_TIM_CONF0(self.channel, self.chipv)
        self.EFUSE_WR_TIM_CONF1 = EFUSE_WR_TIM_CONF1(self.channel, self.chipv)
        self.EFUSE_DATE = EFUSE_DATE(self.channel, self.chipv)
class PGM_DATA0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x0
        self.__reg_wr_dis_lsb = 0
        self.__reg_wr_dis_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_wr_dis(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wr_dis_msb, self.__reg_wr_dis_lsb)
    @reg_wr_dis.setter
    def reg_wr_dis(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wr_dis_msb, self.__reg_wr_dis_lsb, value)
class PGM_DATA1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x4
        self.__reg_sdio_drefh_lsb = 30
        self.__reg_sdio_drefh_msb = 31
        self.__reg_sdio_modecurlim_lsb = 29
        self.__reg_sdio_modecurlim_msb = 29
        self.__reg_usb_dres_lsb = 25
        self.__reg_usb_dres_msb = 28
        self.__reg_usb_exchg_pins_lsb = 24
        self.__reg_usb_exchg_pins_msb = 24
        self.__reg_usb_drefl_lsb = 22
        self.__reg_usb_drefl_msb = 23
        self.__reg_usb_drefh_lsb = 20
        self.__reg_usb_drefh_msb = 21
        self.__reg_dis_download_manual_encrypt_lsb = 19
        self.__reg_dis_download_manual_encrypt_msb = 19
        self.__reg_hard_dis_jtag_lsb = 18
        self.__reg_hard_dis_jtag_msb = 18
        self.__reg_soft_dis_jtag_lsb = 17
        self.__reg_soft_dis_jtag_msb = 17
        self.__reg_dis_efuse_ate_wr_lsb = 16
        self.__reg_dis_efuse_ate_wr_msb = 16
        self.__reg_dis_sdio_access_lsb = 15
        self.__reg_dis_sdio_access_msb = 15
        self.__reg_dis_can_lsb = 14
        self.__reg_dis_can_msb = 14
        self.__reg_dis_usb_lsb = 13
        self.__reg_dis_usb_msb = 13
        self.__reg_dis_bt_lsb = 12
        self.__reg_dis_bt_msb = 12
        self.__reg_dis_download_dcache_lsb = 11
        self.__reg_dis_download_dcache_msb = 11
        self.__reg_dis_download_icache_lsb = 10
        self.__reg_dis_download_icache_msb = 10
        self.__reg_dis_dcache_lsb = 9
        self.__reg_dis_dcache_msb = 9
        self.__reg_dis_icache_lsb = 8
        self.__reg_dis_icache_msb = 8
        self.__reg_dis_rtc_ram_boot_lsb = 7
        self.__reg_dis_rtc_ram_boot_msb = 7
        self.__reg_rd_dis_lsb = 0
        self.__reg_rd_dis_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_sdio_drefh(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sdio_drefh_msb, self.__reg_sdio_drefh_lsb)
    @reg_sdio_drefh.setter
    def reg_sdio_drefh(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sdio_drefh_msb, self.__reg_sdio_drefh_lsb, value)

    @property
    def reg_sdio_modecurlim(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sdio_modecurlim_msb, self.__reg_sdio_modecurlim_lsb)
    @reg_sdio_modecurlim.setter
    def reg_sdio_modecurlim(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sdio_modecurlim_msb, self.__reg_sdio_modecurlim_lsb, value)

    @property
    def reg_usb_dres(self):
        return self.__MEM.rdm(self.__addr, self.__reg_usb_dres_msb, self.__reg_usb_dres_lsb)
    @reg_usb_dres.setter
    def reg_usb_dres(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_usb_dres_msb, self.__reg_usb_dres_lsb, value)

    @property
    def reg_usb_exchg_pins(self):
        return self.__MEM.rdm(self.__addr, self.__reg_usb_exchg_pins_msb, self.__reg_usb_exchg_pins_lsb)
    @reg_usb_exchg_pins.setter
    def reg_usb_exchg_pins(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_usb_exchg_pins_msb, self.__reg_usb_exchg_pins_lsb, value)

    @property
    def reg_usb_drefl(self):
        return self.__MEM.rdm(self.__addr, self.__reg_usb_drefl_msb, self.__reg_usb_drefl_lsb)
    @reg_usb_drefl.setter
    def reg_usb_drefl(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_usb_drefl_msb, self.__reg_usb_drefl_lsb, value)

    @property
    def reg_usb_drefh(self):
        return self.__MEM.rdm(self.__addr, self.__reg_usb_drefh_msb, self.__reg_usb_drefh_lsb)
    @reg_usb_drefh.setter
    def reg_usb_drefh(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_usb_drefh_msb, self.__reg_usb_drefh_lsb, value)

    @property
    def reg_dis_download_manual_encrypt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dis_download_manual_encrypt_msb, self.__reg_dis_download_manual_encrypt_lsb)
    @reg_dis_download_manual_encrypt.setter
    def reg_dis_download_manual_encrypt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dis_download_manual_encrypt_msb, self.__reg_dis_download_manual_encrypt_lsb, value)

    @property
    def reg_hard_dis_jtag(self):
        return self.__MEM.rdm(self.__addr, self.__reg_hard_dis_jtag_msb, self.__reg_hard_dis_jtag_lsb)
    @reg_hard_dis_jtag.setter
    def reg_hard_dis_jtag(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_hard_dis_jtag_msb, self.__reg_hard_dis_jtag_lsb, value)

    @property
    def reg_soft_dis_jtag(self):
        return self.__MEM.rdm(self.__addr, self.__reg_soft_dis_jtag_msb, self.__reg_soft_dis_jtag_lsb)
    @reg_soft_dis_jtag.setter
    def reg_soft_dis_jtag(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_soft_dis_jtag_msb, self.__reg_soft_dis_jtag_lsb, value)

    @property
    def reg_dis_efuse_ate_wr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dis_efuse_ate_wr_msb, self.__reg_dis_efuse_ate_wr_lsb)
    @reg_dis_efuse_ate_wr.setter
    def reg_dis_efuse_ate_wr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dis_efuse_ate_wr_msb, self.__reg_dis_efuse_ate_wr_lsb, value)

    @property
    def reg_dis_sdio_access(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dis_sdio_access_msb, self.__reg_dis_sdio_access_lsb)
    @reg_dis_sdio_access.setter
    def reg_dis_sdio_access(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dis_sdio_access_msb, self.__reg_dis_sdio_access_lsb, value)

    @property
    def reg_dis_can(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dis_can_msb, self.__reg_dis_can_lsb)
    @reg_dis_can.setter
    def reg_dis_can(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dis_can_msb, self.__reg_dis_can_lsb, value)

    @property
    def reg_dis_usb(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dis_usb_msb, self.__reg_dis_usb_lsb)
    @reg_dis_usb.setter
    def reg_dis_usb(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dis_usb_msb, self.__reg_dis_usb_lsb, value)

    @property
    def reg_dis_bt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dis_bt_msb, self.__reg_dis_bt_lsb)
    @reg_dis_bt.setter
    def reg_dis_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dis_bt_msb, self.__reg_dis_bt_lsb, value)

    @property
    def reg_dis_download_dcache(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dis_download_dcache_msb, self.__reg_dis_download_dcache_lsb)
    @reg_dis_download_dcache.setter
    def reg_dis_download_dcache(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dis_download_dcache_msb, self.__reg_dis_download_dcache_lsb, value)

    @property
    def reg_dis_download_icache(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dis_download_icache_msb, self.__reg_dis_download_icache_lsb)
    @reg_dis_download_icache.setter
    def reg_dis_download_icache(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dis_download_icache_msb, self.__reg_dis_download_icache_lsb, value)

    @property
    def reg_dis_dcache(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dis_dcache_msb, self.__reg_dis_dcache_lsb)
    @reg_dis_dcache.setter
    def reg_dis_dcache(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dis_dcache_msb, self.__reg_dis_dcache_lsb, value)

    @property
    def reg_dis_icache(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dis_icache_msb, self.__reg_dis_icache_lsb)
    @reg_dis_icache.setter
    def reg_dis_icache(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dis_icache_msb, self.__reg_dis_icache_lsb, value)

    @property
    def reg_dis_rtc_ram_boot(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dis_rtc_ram_boot_msb, self.__reg_dis_rtc_ram_boot_lsb)
    @reg_dis_rtc_ram_boot.setter
    def reg_dis_rtc_ram_boot(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dis_rtc_ram_boot_msb, self.__reg_dis_rtc_ram_boot_lsb, value)

    @property
    def reg_rd_dis(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rd_dis_msb, self.__reg_rd_dis_lsb)
    @reg_rd_dis.setter
    def reg_rd_dis(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rd_dis_msb, self.__reg_rd_dis_lsb, value)
class PGM_DATA2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x8
        self.__reg_key_purpose_1_lsb = 28
        self.__reg_key_purpose_1_msb = 31
        self.__reg_key_purpose_0_lsb = 24
        self.__reg_key_purpose_0_msb = 27
        self.__reg_secure_boot_key_revoke2_lsb = 23
        self.__reg_secure_boot_key_revoke2_msb = 23
        self.__reg_secure_boot_key_revoke1_lsb = 22
        self.__reg_secure_boot_key_revoke1_msb = 22
        self.__reg_secure_boot_key_revoke0_lsb = 21
        self.__reg_secure_boot_key_revoke0_msb = 21
        self.__reg_spi_boot_crypt_cnt_lsb = 18
        self.__reg_spi_boot_crypt_cnt_msb = 20
        self.__reg_wdt_delay_sel_lsb = 16
        self.__reg_wdt_delay_sel_msb = 17
        self.__reg_sdio_dcap_lsb = 14
        self.__reg_sdio_dcap_msb = 15
        self.__reg_sdio_init_lsb = 12
        self.__reg_sdio_init_msb = 13
        self.__reg_sdio_dcurlim_lsb = 9
        self.__reg_sdio_dcurlim_msb = 11
        self.__reg_sdio_encurlim_lsb = 8
        self.__reg_sdio_encurlim_msb = 8
        self.__reg_sdio_en_init_lsb = 7
        self.__reg_sdio_en_init_msb = 7
        self.__reg_sdio_force_lsb = 6
        self.__reg_sdio_force_msb = 6
        self.__reg_sdio_tieh_lsb = 5
        self.__reg_sdio_tieh_msb = 5
        self.__reg_sdio_xpd_lsb = 4
        self.__reg_sdio_xpd_msb = 4
        self.__reg_sdio_drefl_lsb = 2
        self.__reg_sdio_drefl_msb = 3
        self.__reg_sdio_drefm_lsb = 0
        self.__reg_sdio_drefm_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_key_purpose_1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_key_purpose_1_msb, self.__reg_key_purpose_1_lsb)
    @reg_key_purpose_1.setter
    def reg_key_purpose_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_key_purpose_1_msb, self.__reg_key_purpose_1_lsb, value)

    @property
    def reg_key_purpose_0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_key_purpose_0_msb, self.__reg_key_purpose_0_lsb)
    @reg_key_purpose_0.setter
    def reg_key_purpose_0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_key_purpose_0_msb, self.__reg_key_purpose_0_lsb, value)

    @property
    def reg_secure_boot_key_revoke2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_secure_boot_key_revoke2_msb, self.__reg_secure_boot_key_revoke2_lsb)
    @reg_secure_boot_key_revoke2.setter
    def reg_secure_boot_key_revoke2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_secure_boot_key_revoke2_msb, self.__reg_secure_boot_key_revoke2_lsb, value)

    @property
    def reg_secure_boot_key_revoke1(self):
        return self.__MEM.rdm(self.__addr, self.__reg_secure_boot_key_revoke1_msb, self.__reg_secure_boot_key_revoke1_lsb)
    @reg_secure_boot_key_revoke1.setter
    def reg_secure_boot_key_revoke1(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_secure_boot_key_revoke1_msb, self.__reg_secure_boot_key_revoke1_lsb, value)

    @property
    def reg_secure_boot_key_revoke0(self):
        return self.__MEM.rdm(self.__addr, self.__reg_secure_boot_key_revoke0_msb, self.__reg_secure_boot_key_revoke0_lsb)
    @reg_secure_boot_key_revoke0.setter
    def reg_secure_boot_key_revoke0(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_secure_boot_key_revoke0_msb, self.__reg_secure_boot_key_revoke0_lsb, value)

    @property
    def reg_spi_boot_crypt_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_spi_boot_crypt_cnt_msb, self.__reg_spi_boot_crypt_cnt_lsb)
    @reg_spi_boot_crypt_cnt.setter
    def reg_spi_boot_crypt_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_spi_boot_crypt_cnt_msb, self.__reg_spi_boot_crypt_cnt_lsb, value)

    @property
    def reg_wdt_delay_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_wdt_delay_sel_msb, self.__reg_wdt_delay_sel_lsb)
    @reg_wdt_delay_sel.setter
    def reg_wdt_delay_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_wdt_delay_sel_msb, self.__reg_wdt_delay_sel_lsb, value)

    @property
    def reg_sdio_dcap(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sdio_dcap_msb, self.__reg_sdio_dcap_lsb)
    @reg_sdio_dcap.setter
    def reg_sdio_dcap(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sdio_dcap_msb, self.__reg_sdio_dcap_lsb, value)

    @property
    def reg_sdio_init(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sdio_init_msb, self.__reg_sdio_init_lsb)
    @reg_sdio_init.setter
    def reg_sdio_init(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sdio_init_msb, self.__reg_sdio_init_lsb, value)

    @property
    def reg_sdio_dcurlim(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sdio_dcurlim_msb, self.__reg_sdio_dcurlim_lsb)
    @reg_sdio_dcurlim.setter
    def reg_sdio_dcurlim(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sdio_dcurlim_msb, self.__reg_sdio_dcurlim_lsb, value)

    @property
    def reg_sdio_encurlim(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sdio_encurlim_msb, self.__reg_sdio_encurlim_lsb)
    @reg_sdio_encurlim.setter
    def reg_sdio_encurlim(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sdio_encurlim_msb, self.__reg_sdio_encurlim_lsb, value)

    @property
    def reg_sdio_en_init(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sdio_en_init_msb, self.__reg_sdio_en_init_lsb)
    @reg_sdio_en_init.setter
    def reg_sdio_en_init(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sdio_en_init_msb, self.__reg_sdio_en_init_lsb, value)

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
    def reg_sdio_xpd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_sdio_xpd_msb, self.__reg_sdio_xpd_lsb)
    @reg_sdio_xpd.setter
    def reg_sdio_xpd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_sdio_xpd_msb, self.__reg_sdio_xpd_lsb, value)

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
class PGM_DATA3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xc
        self.__reg_flash_tpuw_lsb = 28
        self.__reg_flash_tpuw_msb = 31
        self.__reg_xtal_freq_lsb = 22
        self.__reg_xtal_freq_msb = 27
        self.__reg_secure_boot_aggressive_revoke_lsb = 21
        self.__reg_secure_boot_aggressive_revoke_msb = 21
        self.__reg_secure_boot_en_lsb = 20
        self.__reg_secure_boot_en_msb = 20
        self.__reg_key_purpose_6_lsb = 16
        self.__reg_key_purpose_6_msb = 19
        self.__reg_key_purpose_5_lsb = 12
        self.__reg_key_purpose_5_msb = 15
        self.__reg_key_purpose_4_lsb = 8
        self.__reg_key_purpose_4_msb = 11
        self.__reg_key_purpose_3_lsb = 4
        self.__reg_key_purpose_3_msb = 7
        self.__reg_key_purpose_2_lsb = 0
        self.__reg_key_purpose_2_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_flash_tpuw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_flash_tpuw_msb, self.__reg_flash_tpuw_lsb)
    @reg_flash_tpuw.setter
    def reg_flash_tpuw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_flash_tpuw_msb, self.__reg_flash_tpuw_lsb, value)

    @property
    def reg_xtal_freq(self):
        return self.__MEM.rdm(self.__addr, self.__reg_xtal_freq_msb, self.__reg_xtal_freq_lsb)
    @reg_xtal_freq.setter
    def reg_xtal_freq(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_xtal_freq_msb, self.__reg_xtal_freq_lsb, value)

    @property
    def reg_secure_boot_aggressive_revoke(self):
        return self.__MEM.rdm(self.__addr, self.__reg_secure_boot_aggressive_revoke_msb, self.__reg_secure_boot_aggressive_revoke_lsb)
    @reg_secure_boot_aggressive_revoke.setter
    def reg_secure_boot_aggressive_revoke(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_secure_boot_aggressive_revoke_msb, self.__reg_secure_boot_aggressive_revoke_lsb, value)

    @property
    def reg_secure_boot_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_secure_boot_en_msb, self.__reg_secure_boot_en_lsb)
    @reg_secure_boot_en.setter
    def reg_secure_boot_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_secure_boot_en_msb, self.__reg_secure_boot_en_lsb, value)

    @property
    def reg_key_purpose_6(self):
        return self.__MEM.rdm(self.__addr, self.__reg_key_purpose_6_msb, self.__reg_key_purpose_6_lsb)
    @reg_key_purpose_6.setter
    def reg_key_purpose_6(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_key_purpose_6_msb, self.__reg_key_purpose_6_lsb, value)

    @property
    def reg_key_purpose_5(self):
        return self.__MEM.rdm(self.__addr, self.__reg_key_purpose_5_msb, self.__reg_key_purpose_5_lsb)
    @reg_key_purpose_5.setter
    def reg_key_purpose_5(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_key_purpose_5_msb, self.__reg_key_purpose_5_lsb, value)

    @property
    def reg_key_purpose_4(self):
        return self.__MEM.rdm(self.__addr, self.__reg_key_purpose_4_msb, self.__reg_key_purpose_4_lsb)
    @reg_key_purpose_4.setter
    def reg_key_purpose_4(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_key_purpose_4_msb, self.__reg_key_purpose_4_lsb, value)

    @property
    def reg_key_purpose_3(self):
        return self.__MEM.rdm(self.__addr, self.__reg_key_purpose_3_msb, self.__reg_key_purpose_3_lsb)
    @reg_key_purpose_3.setter
    def reg_key_purpose_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_key_purpose_3_msb, self.__reg_key_purpose_3_lsb, value)

    @property
    def reg_key_purpose_2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_key_purpose_2_msb, self.__reg_key_purpose_2_lsb)
    @reg_key_purpose_2.setter
    def reg_key_purpose_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_key_purpose_2_msb, self.__reg_key_purpose_2_lsb, value)
class PGM_DATA4(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x10
        self.__reg_reserve_lsb = 8
        self.__reg_reserve_msb = 31
        self.__reg_uart_print_control_lsb = 6
        self.__reg_uart_print_control_msb = 7
        self.__reg_enable_security_download_lsb = 5
        self.__reg_enable_security_download_msb = 5
        self.__reg_dis_usb_download_mode_lsb = 4
        self.__reg_dis_usb_download_mode_msb = 4
        self.__reg_dis_tiny_basic_lsb = 3
        self.__reg_dis_tiny_basic_msb = 3
        self.__reg_uart_print_channel_lsb = 2
        self.__reg_uart_print_channel_msb = 2
        self.__reg_dis_legacy_spi_boot_lsb = 1
        self.__reg_dis_legacy_spi_boot_msb = 1
        self.__reg_dis_download_mode_lsb = 0
        self.__reg_dis_download_mode_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_reserve(self):
        return self.__MEM.rdm(self.__addr, self.__reg_reserve_msb, self.__reg_reserve_lsb)
    @reg_reserve.setter
    def reg_reserve(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_reserve_msb, self.__reg_reserve_lsb, value)

    @property
    def reg_uart_print_control(self):
        return self.__MEM.rdm(self.__addr, self.__reg_uart_print_control_msb, self.__reg_uart_print_control_lsb)
    @reg_uart_print_control.setter
    def reg_uart_print_control(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_uart_print_control_msb, self.__reg_uart_print_control_lsb, value)

    @property
    def reg_enable_security_download(self):
        return self.__MEM.rdm(self.__addr, self.__reg_enable_security_download_msb, self.__reg_enable_security_download_lsb)
    @reg_enable_security_download.setter
    def reg_enable_security_download(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_enable_security_download_msb, self.__reg_enable_security_download_lsb, value)

    @property
    def reg_dis_usb_download_mode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dis_usb_download_mode_msb, self.__reg_dis_usb_download_mode_lsb)
    @reg_dis_usb_download_mode.setter
    def reg_dis_usb_download_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dis_usb_download_mode_msb, self.__reg_dis_usb_download_mode_lsb, value)

    @property
    def reg_dis_tiny_basic(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dis_tiny_basic_msb, self.__reg_dis_tiny_basic_lsb)
    @reg_dis_tiny_basic.setter
    def reg_dis_tiny_basic(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dis_tiny_basic_msb, self.__reg_dis_tiny_basic_lsb, value)

    @property
    def reg_uart_print_channel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_uart_print_channel_msb, self.__reg_uart_print_channel_lsb)
    @reg_uart_print_channel.setter
    def reg_uart_print_channel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_uart_print_channel_msb, self.__reg_uart_print_channel_lsb, value)

    @property
    def reg_dis_legacy_spi_boot(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dis_legacy_spi_boot_msb, self.__reg_dis_legacy_spi_boot_lsb)
    @reg_dis_legacy_spi_boot.setter
    def reg_dis_legacy_spi_boot(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dis_legacy_spi_boot_msb, self.__reg_dis_legacy_spi_boot_lsb, value)

    @property
    def reg_dis_download_mode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_dis_download_mode_msb, self.__reg_dis_download_mode_lsb)
    @reg_dis_download_mode.setter
    def reg_dis_download_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_dis_download_mode_msb, self.__reg_dis_download_mode_lsb, value)
class PGM_DATA5(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x14
        self.__reg_rs_data_23_lsb = 24
        self.__reg_rs_data_23_msb = 31
        self.__reg_chip_version_lsb = 0
        self.__reg_chip_version_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rs_data_23(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rs_data_23_msb, self.__reg_rs_data_23_lsb)
    @reg_rs_data_23.setter
    def reg_rs_data_23(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rs_data_23_msb, self.__reg_rs_data_23_lsb, value)

    @property
    def reg_chip_version(self):
        return self.__MEM.rdm(self.__addr, self.__reg_chip_version_msb, self.__reg_chip_version_lsb)
    @reg_chip_version.setter
    def reg_chip_version(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_chip_version_msb, self.__reg_chip_version_lsb, value)
class PGM_DATA6(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x18
        self.__reg_rs_data_24_27_lsb = 0
        self.__reg_rs_data_24_27_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rs_data_24_27(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rs_data_24_27_msb, self.__reg_rs_data_24_27_lsb)
    @reg_rs_data_24_27.setter
    def reg_rs_data_24_27(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rs_data_24_27_msb, self.__reg_rs_data_24_27_lsb, value)
class PGM_DATA7(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x1c
        self.__reg_rs_data_28_31_lsb = 0
        self.__reg_rs_data_28_31_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rs_data_28_31(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rs_data_28_31_msb, self.__reg_rs_data_28_31_lsb)
    @reg_rs_data_28_31.setter
    def reg_rs_data_28_31(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rs_data_28_31_msb, self.__reg_rs_data_28_31_lsb, value)
class PGM_CHECK_VALUE0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x20
        self.__reg_rs_data_32_35_lsb = 0
        self.__reg_rs_data_32_35_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rs_data_32_35(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rs_data_32_35_msb, self.__reg_rs_data_32_35_lsb)
    @reg_rs_data_32_35.setter
    def reg_rs_data_32_35(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rs_data_32_35_msb, self.__reg_rs_data_32_35_lsb, value)
class PGM_CHECK_VALUE1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x24
        self.__reg_rs_data_36_39_lsb = 0
        self.__reg_rs_data_36_39_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rs_data_36_39(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rs_data_36_39_msb, self.__reg_rs_data_36_39_lsb)
    @reg_rs_data_36_39.setter
    def reg_rs_data_36_39(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rs_data_36_39_msb, self.__reg_rs_data_36_39_lsb, value)
class PGM_CHECK_VALUE2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x28
        self.__reg_rs_data_40_43_lsb = 0
        self.__reg_rs_data_40_43_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rs_data_40_43(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rs_data_40_43_msb, self.__reg_rs_data_40_43_lsb)
    @reg_rs_data_40_43.setter
    def reg_rs_data_40_43(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rs_data_40_43_msb, self.__reg_rs_data_40_43_lsb, value)
class RD_WR_DIS(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x2c
        self.__efuse_wr_dis_lsb = 0
        self.__efuse_wr_dis_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_wr_dis(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_wr_dis_msb, self.__efuse_wr_dis_lsb)
    @efuse_wr_dis.setter
    def efuse_wr_dis(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_wr_dis_msb, self.__efuse_wr_dis_lsb, value)
class RD_REPEAT_DATA0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x30
        self.__efuse_sdio_drefh_lsb = 30
        self.__efuse_sdio_drefh_msb = 31
        self.__efuse_sdio_modecurlim_lsb = 29
        self.__efuse_sdio_modecurlim_msb = 29
        self.__efuse_usb_dres_lsb = 25
        self.__efuse_usb_dres_msb = 28
        self.__efuse_usb_exchg_pins_lsb = 24
        self.__efuse_usb_exchg_pins_msb = 24
        self.__efuse_usb_drefl_lsb = 22
        self.__efuse_usb_drefl_msb = 23
        self.__efuse_usb_drefh_lsb = 20
        self.__efuse_usb_drefh_msb = 21
        self.__efuse_dis_download_manual_encrypt_lsb = 19
        self.__efuse_dis_download_manual_encrypt_msb = 19
        self.__efuse_hard_dis_jtag_lsb = 18
        self.__efuse_hard_dis_jtag_msb = 18
        self.__efuse_soft_dis_jtag_lsb = 17
        self.__efuse_soft_dis_jtag_msb = 17
        self.__efuse_dis_efuse_ate_wr_lsb = 16
        self.__efuse_dis_efuse_ate_wr_msb = 16
        self.__efuse_dis_sdio_access_lsb = 15
        self.__efuse_dis_sdio_access_msb = 15
        self.__efuse_dis_can_lsb = 14
        self.__efuse_dis_can_msb = 14
        self.__efuse_dis_usb_lsb = 13
        self.__efuse_dis_usb_msb = 13
        self.__efuse_dis_bt_lsb = 12
        self.__efuse_dis_bt_msb = 12
        self.__efuse_dis_download_dcache_lsb = 11
        self.__efuse_dis_download_dcache_msb = 11
        self.__efuse_dis_download_icache_lsb = 10
        self.__efuse_dis_download_icache_msb = 10
        self.__efuse_dis_dcache_lsb = 9
        self.__efuse_dis_dcache_msb = 9
        self.__efuse_dis_icache_lsb = 8
        self.__efuse_dis_icache_msb = 8
        self.__efuse_dis_rtc_ram_boot_lsb = 7
        self.__efuse_dis_rtc_ram_boot_msb = 7
        self.__efuse_rd_dis_lsb = 0
        self.__efuse_rd_dis_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_sdio_drefh(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_sdio_drefh_msb, self.__efuse_sdio_drefh_lsb)
    @efuse_sdio_drefh.setter
    def efuse_sdio_drefh(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_sdio_drefh_msb, self.__efuse_sdio_drefh_lsb, value)

    @property
    def efuse_sdio_modecurlim(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_sdio_modecurlim_msb, self.__efuse_sdio_modecurlim_lsb)
    @efuse_sdio_modecurlim.setter
    def efuse_sdio_modecurlim(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_sdio_modecurlim_msb, self.__efuse_sdio_modecurlim_lsb, value)

    @property
    def efuse_usb_dres(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_usb_dres_msb, self.__efuse_usb_dres_lsb)
    @efuse_usb_dres.setter
    def efuse_usb_dres(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_usb_dres_msb, self.__efuse_usb_dres_lsb, value)

    @property
    def efuse_usb_exchg_pins(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_usb_exchg_pins_msb, self.__efuse_usb_exchg_pins_lsb)
    @efuse_usb_exchg_pins.setter
    def efuse_usb_exchg_pins(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_usb_exchg_pins_msb, self.__efuse_usb_exchg_pins_lsb, value)

    @property
    def efuse_usb_drefl(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_usb_drefl_msb, self.__efuse_usb_drefl_lsb)
    @efuse_usb_drefl.setter
    def efuse_usb_drefl(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_usb_drefl_msb, self.__efuse_usb_drefl_lsb, value)

    @property
    def efuse_usb_drefh(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_usb_drefh_msb, self.__efuse_usb_drefh_lsb)
    @efuse_usb_drefh.setter
    def efuse_usb_drefh(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_usb_drefh_msb, self.__efuse_usb_drefh_lsb, value)

    @property
    def efuse_dis_download_manual_encrypt(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_dis_download_manual_encrypt_msb, self.__efuse_dis_download_manual_encrypt_lsb)
    @efuse_dis_download_manual_encrypt.setter
    def efuse_dis_download_manual_encrypt(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_dis_download_manual_encrypt_msb, self.__efuse_dis_download_manual_encrypt_lsb, value)

    @property
    def efuse_hard_dis_jtag(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_hard_dis_jtag_msb, self.__efuse_hard_dis_jtag_lsb)
    @efuse_hard_dis_jtag.setter
    def efuse_hard_dis_jtag(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_hard_dis_jtag_msb, self.__efuse_hard_dis_jtag_lsb, value)

    @property
    def efuse_soft_dis_jtag(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_soft_dis_jtag_msb, self.__efuse_soft_dis_jtag_lsb)
    @efuse_soft_dis_jtag.setter
    def efuse_soft_dis_jtag(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_soft_dis_jtag_msb, self.__efuse_soft_dis_jtag_lsb, value)

    @property
    def efuse_dis_efuse_ate_wr(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_dis_efuse_ate_wr_msb, self.__efuse_dis_efuse_ate_wr_lsb)
    @efuse_dis_efuse_ate_wr.setter
    def efuse_dis_efuse_ate_wr(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_dis_efuse_ate_wr_msb, self.__efuse_dis_efuse_ate_wr_lsb, value)

    @property
    def efuse_dis_sdio_access(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_dis_sdio_access_msb, self.__efuse_dis_sdio_access_lsb)
    @efuse_dis_sdio_access.setter
    def efuse_dis_sdio_access(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_dis_sdio_access_msb, self.__efuse_dis_sdio_access_lsb, value)

    @property
    def efuse_dis_can(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_dis_can_msb, self.__efuse_dis_can_lsb)
    @efuse_dis_can.setter
    def efuse_dis_can(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_dis_can_msb, self.__efuse_dis_can_lsb, value)

    @property
    def efuse_dis_usb(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_dis_usb_msb, self.__efuse_dis_usb_lsb)
    @efuse_dis_usb.setter
    def efuse_dis_usb(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_dis_usb_msb, self.__efuse_dis_usb_lsb, value)

    @property
    def efuse_dis_bt(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_dis_bt_msb, self.__efuse_dis_bt_lsb)
    @efuse_dis_bt.setter
    def efuse_dis_bt(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_dis_bt_msb, self.__efuse_dis_bt_lsb, value)

    @property
    def efuse_dis_download_dcache(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_dis_download_dcache_msb, self.__efuse_dis_download_dcache_lsb)
    @efuse_dis_download_dcache.setter
    def efuse_dis_download_dcache(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_dis_download_dcache_msb, self.__efuse_dis_download_dcache_lsb, value)

    @property
    def efuse_dis_download_icache(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_dis_download_icache_msb, self.__efuse_dis_download_icache_lsb)
    @efuse_dis_download_icache.setter
    def efuse_dis_download_icache(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_dis_download_icache_msb, self.__efuse_dis_download_icache_lsb, value)

    @property
    def efuse_dis_dcache(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_dis_dcache_msb, self.__efuse_dis_dcache_lsb)
    @efuse_dis_dcache.setter
    def efuse_dis_dcache(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_dis_dcache_msb, self.__efuse_dis_dcache_lsb, value)

    @property
    def efuse_dis_icache(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_dis_icache_msb, self.__efuse_dis_icache_lsb)
    @efuse_dis_icache.setter
    def efuse_dis_icache(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_dis_icache_msb, self.__efuse_dis_icache_lsb, value)

    @property
    def efuse_dis_rtc_ram_boot(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_dis_rtc_ram_boot_msb, self.__efuse_dis_rtc_ram_boot_lsb)
    @efuse_dis_rtc_ram_boot.setter
    def efuse_dis_rtc_ram_boot(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_dis_rtc_ram_boot_msb, self.__efuse_dis_rtc_ram_boot_lsb, value)

    @property
    def efuse_rd_dis(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_rd_dis_msb, self.__efuse_rd_dis_lsb)
    @efuse_rd_dis.setter
    def efuse_rd_dis(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_rd_dis_msb, self.__efuse_rd_dis_lsb, value)
class RD_REPEAT_DATA1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x34
        self.__efuse_key_purpose_1_lsb = 28
        self.__efuse_key_purpose_1_msb = 31
        self.__efuse_key_purpose_0_lsb = 24
        self.__efuse_key_purpose_0_msb = 27
        self.__efuse_secure_boot_key_revoke2_lsb = 23
        self.__efuse_secure_boot_key_revoke2_msb = 23
        self.__efuse_secure_boot_key_revoke1_lsb = 22
        self.__efuse_secure_boot_key_revoke1_msb = 22
        self.__efuse_secure_boot_key_revoke0_lsb = 21
        self.__efuse_secure_boot_key_revoke0_msb = 21
        self.__efuse_spi_boot_crypt_cnt_lsb = 18
        self.__efuse_spi_boot_crypt_cnt_msb = 20
        self.__efuse_wdt_delay_sel_lsb = 16
        self.__efuse_wdt_delay_sel_msb = 17
        self.__eufse_sdio_dcap_lsb = 14
        self.__eufse_sdio_dcap_msb = 15
        self.__efuse_sdio_init_lsb = 12
        self.__efuse_sdio_init_msb = 13
        self.__efuse_sdio_dcurlim_lsb = 9
        self.__efuse_sdio_dcurlim_msb = 11
        self.__efuse_sdio_encurlim_lsb = 8
        self.__efuse_sdio_encurlim_msb = 8
        self.__efuse_sdio_en_init_lsb = 7
        self.__efuse_sdio_en_init_msb = 7
        self.__efuse_sdio_force_lsb = 6
        self.__efuse_sdio_force_msb = 6
        self.__efuse_sdio_tieh_lsb = 5
        self.__efuse_sdio_tieh_msb = 5
        self.__efuse_sdio_xpd_lsb = 4
        self.__efuse_sdio_xpd_msb = 4
        self.__efuse_sdio_drefl_lsb = 2
        self.__efuse_sdio_drefl_msb = 3
        self.__efuse_sdio_drefm_lsb = 0
        self.__efuse_sdio_drefm_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_key_purpose_1(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_key_purpose_1_msb, self.__efuse_key_purpose_1_lsb)
    @efuse_key_purpose_1.setter
    def efuse_key_purpose_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_key_purpose_1_msb, self.__efuse_key_purpose_1_lsb, value)

    @property
    def efuse_key_purpose_0(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_key_purpose_0_msb, self.__efuse_key_purpose_0_lsb)
    @efuse_key_purpose_0.setter
    def efuse_key_purpose_0(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_key_purpose_0_msb, self.__efuse_key_purpose_0_lsb, value)

    @property
    def efuse_secure_boot_key_revoke2(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_secure_boot_key_revoke2_msb, self.__efuse_secure_boot_key_revoke2_lsb)
    @efuse_secure_boot_key_revoke2.setter
    def efuse_secure_boot_key_revoke2(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_secure_boot_key_revoke2_msb, self.__efuse_secure_boot_key_revoke2_lsb, value)

    @property
    def efuse_secure_boot_key_revoke1(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_secure_boot_key_revoke1_msb, self.__efuse_secure_boot_key_revoke1_lsb)
    @efuse_secure_boot_key_revoke1.setter
    def efuse_secure_boot_key_revoke1(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_secure_boot_key_revoke1_msb, self.__efuse_secure_boot_key_revoke1_lsb, value)

    @property
    def efuse_secure_boot_key_revoke0(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_secure_boot_key_revoke0_msb, self.__efuse_secure_boot_key_revoke0_lsb)
    @efuse_secure_boot_key_revoke0.setter
    def efuse_secure_boot_key_revoke0(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_secure_boot_key_revoke0_msb, self.__efuse_secure_boot_key_revoke0_lsb, value)

    @property
    def efuse_spi_boot_crypt_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_spi_boot_crypt_cnt_msb, self.__efuse_spi_boot_crypt_cnt_lsb)
    @efuse_spi_boot_crypt_cnt.setter
    def efuse_spi_boot_crypt_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_spi_boot_crypt_cnt_msb, self.__efuse_spi_boot_crypt_cnt_lsb, value)

    @property
    def efuse_wdt_delay_sel(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_wdt_delay_sel_msb, self.__efuse_wdt_delay_sel_lsb)
    @efuse_wdt_delay_sel.setter
    def efuse_wdt_delay_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_wdt_delay_sel_msb, self.__efuse_wdt_delay_sel_lsb, value)

    @property
    def eufse_sdio_dcap(self):
        return self.__MEM.rdm(self.__addr, self.__eufse_sdio_dcap_msb, self.__eufse_sdio_dcap_lsb)
    @eufse_sdio_dcap.setter
    def eufse_sdio_dcap(self, value):
        return self.__MEM.wrm(self.__addr, self.__eufse_sdio_dcap_msb, self.__eufse_sdio_dcap_lsb, value)

    @property
    def efuse_sdio_init(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_sdio_init_msb, self.__efuse_sdio_init_lsb)
    @efuse_sdio_init.setter
    def efuse_sdio_init(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_sdio_init_msb, self.__efuse_sdio_init_lsb, value)

    @property
    def efuse_sdio_dcurlim(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_sdio_dcurlim_msb, self.__efuse_sdio_dcurlim_lsb)
    @efuse_sdio_dcurlim.setter
    def efuse_sdio_dcurlim(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_sdio_dcurlim_msb, self.__efuse_sdio_dcurlim_lsb, value)

    @property
    def efuse_sdio_encurlim(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_sdio_encurlim_msb, self.__efuse_sdio_encurlim_lsb)
    @efuse_sdio_encurlim.setter
    def efuse_sdio_encurlim(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_sdio_encurlim_msb, self.__efuse_sdio_encurlim_lsb, value)

    @property
    def efuse_sdio_en_init(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_sdio_en_init_msb, self.__efuse_sdio_en_init_lsb)
    @efuse_sdio_en_init.setter
    def efuse_sdio_en_init(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_sdio_en_init_msb, self.__efuse_sdio_en_init_lsb, value)

    @property
    def efuse_sdio_force(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_sdio_force_msb, self.__efuse_sdio_force_lsb)
    @efuse_sdio_force.setter
    def efuse_sdio_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_sdio_force_msb, self.__efuse_sdio_force_lsb, value)

    @property
    def efuse_sdio_tieh(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_sdio_tieh_msb, self.__efuse_sdio_tieh_lsb)
    @efuse_sdio_tieh.setter
    def efuse_sdio_tieh(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_sdio_tieh_msb, self.__efuse_sdio_tieh_lsb, value)

    @property
    def efuse_sdio_xpd(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_sdio_xpd_msb, self.__efuse_sdio_xpd_lsb)
    @efuse_sdio_xpd.setter
    def efuse_sdio_xpd(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_sdio_xpd_msb, self.__efuse_sdio_xpd_lsb, value)

    @property
    def efuse_sdio_drefl(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_sdio_drefl_msb, self.__efuse_sdio_drefl_lsb)
    @efuse_sdio_drefl.setter
    def efuse_sdio_drefl(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_sdio_drefl_msb, self.__efuse_sdio_drefl_lsb, value)

    @property
    def efuse_sdio_drefm(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_sdio_drefm_msb, self.__efuse_sdio_drefm_lsb)
    @efuse_sdio_drefm.setter
    def efuse_sdio_drefm(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_sdio_drefm_msb, self.__efuse_sdio_drefm_lsb, value)
class RD_REPEAT_DATA2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x38
        self.__efuse_flash_tpuw_lsb = 28
        self.__efuse_flash_tpuw_msb = 31
        self.__efuse_xtal_freq_lsb = 22
        self.__efuse_xtal_freq_msb = 27
        self.__efuse_secure_boot_aggressive_revoke_lsb = 21
        self.__efuse_secure_boot_aggressive_revoke_msb = 21
        self.__efuse_secure_boot_en_lsb = 20
        self.__efuse_secure_boot_en_msb = 20
        self.__efuse_key_purpose_6_lsb = 16
        self.__efuse_key_purpose_6_msb = 19
        self.__efuse_key_purpose_5_lsb = 12
        self.__efuse_key_purpose_5_msb = 15
        self.__efuse_key_purpose_4_lsb = 8
        self.__efuse_key_purpose_4_msb = 11
        self.__efuse_key_purpose_3_lsb = 4
        self.__efuse_key_purpose_3_msb = 7
        self.__efuse_key_purpose_2_lsb = 0
        self.__efuse_key_purpose_2_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_flash_tpuw(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_flash_tpuw_msb, self.__efuse_flash_tpuw_lsb)
    @efuse_flash_tpuw.setter
    def efuse_flash_tpuw(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_flash_tpuw_msb, self.__efuse_flash_tpuw_lsb, value)

    @property
    def efuse_xtal_freq(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_xtal_freq_msb, self.__efuse_xtal_freq_lsb)
    @efuse_xtal_freq.setter
    def efuse_xtal_freq(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_xtal_freq_msb, self.__efuse_xtal_freq_lsb, value)

    @property
    def efuse_secure_boot_aggressive_revoke(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_secure_boot_aggressive_revoke_msb, self.__efuse_secure_boot_aggressive_revoke_lsb)
    @efuse_secure_boot_aggressive_revoke.setter
    def efuse_secure_boot_aggressive_revoke(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_secure_boot_aggressive_revoke_msb, self.__efuse_secure_boot_aggressive_revoke_lsb, value)

    @property
    def efuse_secure_boot_en(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_secure_boot_en_msb, self.__efuse_secure_boot_en_lsb)
    @efuse_secure_boot_en.setter
    def efuse_secure_boot_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_secure_boot_en_msb, self.__efuse_secure_boot_en_lsb, value)

    @property
    def efuse_key_purpose_6(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_key_purpose_6_msb, self.__efuse_key_purpose_6_lsb)
    @efuse_key_purpose_6.setter
    def efuse_key_purpose_6(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_key_purpose_6_msb, self.__efuse_key_purpose_6_lsb, value)

    @property
    def efuse_key_purpose_5(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_key_purpose_5_msb, self.__efuse_key_purpose_5_lsb)
    @efuse_key_purpose_5.setter
    def efuse_key_purpose_5(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_key_purpose_5_msb, self.__efuse_key_purpose_5_lsb, value)

    @property
    def efuse_key_purpose_4(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_key_purpose_4_msb, self.__efuse_key_purpose_4_lsb)
    @efuse_key_purpose_4.setter
    def efuse_key_purpose_4(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_key_purpose_4_msb, self.__efuse_key_purpose_4_lsb, value)

    @property
    def efuse_key_purpose_3(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_key_purpose_3_msb, self.__efuse_key_purpose_3_lsb)
    @efuse_key_purpose_3.setter
    def efuse_key_purpose_3(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_key_purpose_3_msb, self.__efuse_key_purpose_3_lsb, value)

    @property
    def efuse_key_purpose_2(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_key_purpose_2_msb, self.__efuse_key_purpose_2_lsb)
    @efuse_key_purpose_2.setter
    def efuse_key_purpose_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_key_purpose_2_msb, self.__efuse_key_purpose_2_lsb, value)
class RD_REPEAT_DATA3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x3c
        self.__efuse_reserve_lsb = 8
        self.__efuse_reserve_msb = 31
        self.__efuse_uart_print_control_lsb = 6
        self.__efuse_uart_print_control_msb = 7
        self.__efuse_enable_security_download_lsb = 5
        self.__efuse_enable_security_download_msb = 5
        self.__efuse_dis_usb_download_mode_lsb = 4
        self.__efuse_dis_usb_download_mode_msb = 4
        self.__efuse_dis_tiny_basic_lsb = 3
        self.__efuse_dis_tiny_basic_msb = 3
        self.__efuse_uart_print_channel_lsb = 2
        self.__efuse_uart_print_channel_msb = 2
        self.__efuse_dis_legacy_spi_boot_lsb = 1
        self.__efuse_dis_legacy_spi_boot_msb = 1
        self.__efuse_dis_download_mode_lsb = 0
        self.__efuse_dis_download_mode_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_reserve(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_reserve_msb, self.__efuse_reserve_lsb)
    @efuse_reserve.setter
    def efuse_reserve(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_reserve_msb, self.__efuse_reserve_lsb, value)

    @property
    def efuse_uart_print_control(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_uart_print_control_msb, self.__efuse_uart_print_control_lsb)
    @efuse_uart_print_control.setter
    def efuse_uart_print_control(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_uart_print_control_msb, self.__efuse_uart_print_control_lsb, value)

    @property
    def efuse_enable_security_download(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_enable_security_download_msb, self.__efuse_enable_security_download_lsb)
    @efuse_enable_security_download.setter
    def efuse_enable_security_download(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_enable_security_download_msb, self.__efuse_enable_security_download_lsb, value)

    @property
    def efuse_dis_usb_download_mode(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_dis_usb_download_mode_msb, self.__efuse_dis_usb_download_mode_lsb)
    @efuse_dis_usb_download_mode.setter
    def efuse_dis_usb_download_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_dis_usb_download_mode_msb, self.__efuse_dis_usb_download_mode_lsb, value)

    @property
    def efuse_dis_tiny_basic(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_dis_tiny_basic_msb, self.__efuse_dis_tiny_basic_lsb)
    @efuse_dis_tiny_basic.setter
    def efuse_dis_tiny_basic(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_dis_tiny_basic_msb, self.__efuse_dis_tiny_basic_lsb, value)

    @property
    def efuse_uart_print_channel(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_uart_print_channel_msb, self.__efuse_uart_print_channel_lsb)
    @efuse_uart_print_channel.setter
    def efuse_uart_print_channel(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_uart_print_channel_msb, self.__efuse_uart_print_channel_lsb, value)

    @property
    def efuse_dis_legacy_spi_boot(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_dis_legacy_spi_boot_msb, self.__efuse_dis_legacy_spi_boot_lsb)
    @efuse_dis_legacy_spi_boot.setter
    def efuse_dis_legacy_spi_boot(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_dis_legacy_spi_boot_msb, self.__efuse_dis_legacy_spi_boot_lsb, value)

    @property
    def efuse_dis_download_mode(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_dis_download_mode_msb, self.__efuse_dis_download_mode_lsb)
    @efuse_dis_download_mode.setter
    def efuse_dis_download_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_dis_download_mode_msb, self.__efuse_dis_download_mode_lsb, value)
class RD_REPEAT_DATA4(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x40
        self.__efuse_chip_version_lsb = 0
        self.__efuse_chip_version_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_chip_version(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_chip_version_msb, self.__efuse_chip_version_lsb)
    @efuse_chip_version.setter
    def efuse_chip_version(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_chip_version_msb, self.__efuse_chip_version_lsb, value)
class RD_MAC_SPI_8M_0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x44
        self.__efuse_mac_0_lsb = 0
        self.__efuse_mac_0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_mac_0(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_mac_0_msb, self.__efuse_mac_0_lsb)
    @efuse_mac_0.setter
    def efuse_mac_0(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_mac_0_msb, self.__efuse_mac_0_lsb, value)
class RD_MAC_SPI_8M_1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x48
        self.__efuse_spi_pad_conf_0_lsb = 16
        self.__efuse_spi_pad_conf_0_msb = 31
        self.__efuse_mac_1_lsb = 0
        self.__efuse_mac_1_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_spi_pad_conf_0(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_spi_pad_conf_0_msb, self.__efuse_spi_pad_conf_0_lsb)
    @efuse_spi_pad_conf_0.setter
    def efuse_spi_pad_conf_0(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_spi_pad_conf_0_msb, self.__efuse_spi_pad_conf_0_lsb, value)

    @property
    def efuse_mac_1(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_mac_1_msb, self.__efuse_mac_1_lsb)
    @efuse_mac_1.setter
    def efuse_mac_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_mac_1_msb, self.__efuse_mac_1_lsb, value)
class RD_MAC_SPI_8M_2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x4c
        self.__efuse_clk8m_freq_lsb = 20
        self.__efuse_clk8m_freq_msb = 31
        self.__efuse_spi_pad_conf_1_lsb = 0
        self.__efuse_spi_pad_conf_1_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_clk8m_freq(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_clk8m_freq_msb, self.__efuse_clk8m_freq_lsb)
    @efuse_clk8m_freq.setter
    def efuse_clk8m_freq(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_clk8m_freq_msb, self.__efuse_clk8m_freq_lsb, value)

    @property
    def efuse_spi_pad_conf_1(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_spi_pad_conf_1_msb, self.__efuse_spi_pad_conf_1_lsb)
    @efuse_spi_pad_conf_1.setter
    def efuse_spi_pad_conf_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_spi_pad_conf_1_msb, self.__efuse_spi_pad_conf_1_lsb, value)
class RD_MAC_SPI_8M_3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x50
        self.__efuse_sys_data_part0_0_lsb = 0
        self.__efuse_sys_data_part0_0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_sys_data_part0_0(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_sys_data_part0_0_msb, self.__efuse_sys_data_part0_0_lsb)
    @efuse_sys_data_part0_0.setter
    def efuse_sys_data_part0_0(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_sys_data_part0_0_msb, self.__efuse_sys_data_part0_0_lsb, value)
class RD_MAC_SPI_8M_4(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x54
        self.__efuse_sys_data_part0_1_lsb = 0
        self.__efuse_sys_data_part0_1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_sys_data_part0_1(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_sys_data_part0_1_msb, self.__efuse_sys_data_part0_1_lsb)
    @efuse_sys_data_part0_1.setter
    def efuse_sys_data_part0_1(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_sys_data_part0_1_msb, self.__efuse_sys_data_part0_1_lsb, value)
class RD_MAC_SPI_8M_5(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x58
        self.__efuse_sys_data_part0_2_lsb = 0
        self.__efuse_sys_data_part0_2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_sys_data_part0_2(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_sys_data_part0_2_msb, self.__efuse_sys_data_part0_2_lsb)
    @efuse_sys_data_part0_2.setter
    def efuse_sys_data_part0_2(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_sys_data_part0_2_msb, self.__efuse_sys_data_part0_2_lsb, value)
class RD_SYS_DATA0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x5c
        self.__efuse_sys_data0_lsb = 0
        self.__efuse_sys_data0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_sys_data0(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_sys_data0_msb, self.__efuse_sys_data0_lsb)
    @efuse_sys_data0.setter
    def efuse_sys_data0(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_sys_data0_msb, self.__efuse_sys_data0_lsb, value)
class RD_SYS_DATA1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x60
        self.__efuse_sys_data1_lsb = 0
        self.__efuse_sys_data1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_sys_data1(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_sys_data1_msb, self.__efuse_sys_data1_lsb)
    @efuse_sys_data1.setter
    def efuse_sys_data1(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_sys_data1_msb, self.__efuse_sys_data1_lsb, value)
class RD_SYS_DATA2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x64
        self.__efuse_sys_data2_lsb = 0
        self.__efuse_sys_data2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_sys_data2(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_sys_data2_msb, self.__efuse_sys_data2_lsb)
    @efuse_sys_data2.setter
    def efuse_sys_data2(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_sys_data2_msb, self.__efuse_sys_data2_lsb, value)
class RD_SYS_DATA3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x68
        self.__efuse_sys_data3_lsb = 0
        self.__efuse_sys_data3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_sys_data3(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_sys_data3_msb, self.__efuse_sys_data3_lsb)
    @efuse_sys_data3.setter
    def efuse_sys_data3(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_sys_data3_msb, self.__efuse_sys_data3_lsb, value)
class RD_SYS_DATA4(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x6c
        self.__efuse_sys_data4_lsb = 0
        self.__efuse_sys_data4_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_sys_data4(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_sys_data4_msb, self.__efuse_sys_data4_lsb)
    @efuse_sys_data4.setter
    def efuse_sys_data4(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_sys_data4_msb, self.__efuse_sys_data4_lsb, value)
class RD_SYS_DATA5(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x70
        self.__efuse_sys_data5_lsb = 0
        self.__efuse_sys_data5_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_sys_data5(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_sys_data5_msb, self.__efuse_sys_data5_lsb)
    @efuse_sys_data5.setter
    def efuse_sys_data5(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_sys_data5_msb, self.__efuse_sys_data5_lsb, value)
class RD_SYS_DATA6(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x74
        self.__efuse_sys_data6_lsb = 0
        self.__efuse_sys_data6_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_sys_data6(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_sys_data6_msb, self.__efuse_sys_data6_lsb)
    @efuse_sys_data6.setter
    def efuse_sys_data6(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_sys_data6_msb, self.__efuse_sys_data6_lsb, value)
class RD_SYS_DATA7(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x78
        self.__efuse_sys_data7_lsb = 0
        self.__efuse_sys_data7_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_sys_data7(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_sys_data7_msb, self.__efuse_sys_data7_lsb)
    @efuse_sys_data7.setter
    def efuse_sys_data7(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_sys_data7_msb, self.__efuse_sys_data7_lsb, value)
class RD_USR_DATA0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x7c
        self.__efuse_usr_data0_lsb = 0
        self.__efuse_usr_data0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_usr_data0(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_usr_data0_msb, self.__efuse_usr_data0_lsb)
    @efuse_usr_data0.setter
    def efuse_usr_data0(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_usr_data0_msb, self.__efuse_usr_data0_lsb, value)
class RD_USR_DATA1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x80
        self.__efuse_usr_data1_lsb = 0
        self.__efuse_usr_data1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_usr_data1(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_usr_data1_msb, self.__efuse_usr_data1_lsb)
    @efuse_usr_data1.setter
    def efuse_usr_data1(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_usr_data1_msb, self.__efuse_usr_data1_lsb, value)
class RD_USR_DATA2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x84
        self.__efuse_usr_data2_lsb = 0
        self.__efuse_usr_data2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_usr_data2(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_usr_data2_msb, self.__efuse_usr_data2_lsb)
    @efuse_usr_data2.setter
    def efuse_usr_data2(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_usr_data2_msb, self.__efuse_usr_data2_lsb, value)
class RD_USR_DATA3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x88
        self.__efuse_usr_data3_lsb = 0
        self.__efuse_usr_data3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_usr_data3(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_usr_data3_msb, self.__efuse_usr_data3_lsb)
    @efuse_usr_data3.setter
    def efuse_usr_data3(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_usr_data3_msb, self.__efuse_usr_data3_lsb, value)
class RD_USR_DATA4(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x8c
        self.__efuse_usr_data4_lsb = 0
        self.__efuse_usr_data4_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_usr_data4(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_usr_data4_msb, self.__efuse_usr_data4_lsb)
    @efuse_usr_data4.setter
    def efuse_usr_data4(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_usr_data4_msb, self.__efuse_usr_data4_lsb, value)
class RD_USR_DATA5(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x90
        self.__efuse_usr_data5_lsb = 0
        self.__efuse_usr_data5_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_usr_data5(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_usr_data5_msb, self.__efuse_usr_data5_lsb)
    @efuse_usr_data5.setter
    def efuse_usr_data5(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_usr_data5_msb, self.__efuse_usr_data5_lsb, value)
class RD_USR_DATA6(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x94
        self.__efuse_usr_data6_lsb = 0
        self.__efuse_usr_data6_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_usr_data6(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_usr_data6_msb, self.__efuse_usr_data6_lsb)
    @efuse_usr_data6.setter
    def efuse_usr_data6(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_usr_data6_msb, self.__efuse_usr_data6_lsb, value)
class RD_USR_DATA7(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x98
        self.__efuse_usr_data7_lsb = 0
        self.__efuse_usr_data7_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_usr_data7(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_usr_data7_msb, self.__efuse_usr_data7_lsb)
    @efuse_usr_data7.setter
    def efuse_usr_data7(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_usr_data7_msb, self.__efuse_usr_data7_lsb, value)
class RD_KEY0_DATA0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x9c
        self.__key0_data0_lsb = 0
        self.__key0_data0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key0_data0(self):
        return self.__MEM.rdm(self.__addr, self.__key0_data0_msb, self.__key0_data0_lsb)
    @key0_data0.setter
    def key0_data0(self, value):
        return self.__MEM.wrm(self.__addr, self.__key0_data0_msb, self.__key0_data0_lsb, value)
class RD_KEY0_DATA1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xa0
        self.__key0_data1_lsb = 0
        self.__key0_data1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key0_data1(self):
        return self.__MEM.rdm(self.__addr, self.__key0_data1_msb, self.__key0_data1_lsb)
    @key0_data1.setter
    def key0_data1(self, value):
        return self.__MEM.wrm(self.__addr, self.__key0_data1_msb, self.__key0_data1_lsb, value)
class RD_KEY0_DATA2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xa4
        self.__key0_data2_lsb = 0
        self.__key0_data2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key0_data2(self):
        return self.__MEM.rdm(self.__addr, self.__key0_data2_msb, self.__key0_data2_lsb)
    @key0_data2.setter
    def key0_data2(self, value):
        return self.__MEM.wrm(self.__addr, self.__key0_data2_msb, self.__key0_data2_lsb, value)
class RD_KEY0_DATA3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xa8
        self.__key0_data3_lsb = 0
        self.__key0_data3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key0_data3(self):
        return self.__MEM.rdm(self.__addr, self.__key0_data3_msb, self.__key0_data3_lsb)
    @key0_data3.setter
    def key0_data3(self, value):
        return self.__MEM.wrm(self.__addr, self.__key0_data3_msb, self.__key0_data3_lsb, value)
class RD_KEY0_DATA4(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xac
        self.__key0_data4_lsb = 0
        self.__key0_data4_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key0_data4(self):
        return self.__MEM.rdm(self.__addr, self.__key0_data4_msb, self.__key0_data4_lsb)
    @key0_data4.setter
    def key0_data4(self, value):
        return self.__MEM.wrm(self.__addr, self.__key0_data4_msb, self.__key0_data4_lsb, value)
class RD_KEY0_DATA5(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xb0
        self.__key0_data5_lsb = 0
        self.__key0_data5_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key0_data5(self):
        return self.__MEM.rdm(self.__addr, self.__key0_data5_msb, self.__key0_data5_lsb)
    @key0_data5.setter
    def key0_data5(self, value):
        return self.__MEM.wrm(self.__addr, self.__key0_data5_msb, self.__key0_data5_lsb, value)
class RD_KEY0_DATA6(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xb4
        self.__key0_data6_lsb = 0
        self.__key0_data6_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key0_data6(self):
        return self.__MEM.rdm(self.__addr, self.__key0_data6_msb, self.__key0_data6_lsb)
    @key0_data6.setter
    def key0_data6(self, value):
        return self.__MEM.wrm(self.__addr, self.__key0_data6_msb, self.__key0_data6_lsb, value)
class RD_KEY0_DATA7(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xb8
        self.__key0_data7_lsb = 0
        self.__key0_data7_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key0_data7(self):
        return self.__MEM.rdm(self.__addr, self.__key0_data7_msb, self.__key0_data7_lsb)
    @key0_data7.setter
    def key0_data7(self, value):
        return self.__MEM.wrm(self.__addr, self.__key0_data7_msb, self.__key0_data7_lsb, value)
class RD_KEY1_DATA0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xbc
        self.__key1_data0_lsb = 0
        self.__key1_data0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key1_data0(self):
        return self.__MEM.rdm(self.__addr, self.__key1_data0_msb, self.__key1_data0_lsb)
    @key1_data0.setter
    def key1_data0(self, value):
        return self.__MEM.wrm(self.__addr, self.__key1_data0_msb, self.__key1_data0_lsb, value)
class RD_KEY1_DATA1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xc0
        self.__key1_data1_lsb = 0
        self.__key1_data1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key1_data1(self):
        return self.__MEM.rdm(self.__addr, self.__key1_data1_msb, self.__key1_data1_lsb)
    @key1_data1.setter
    def key1_data1(self, value):
        return self.__MEM.wrm(self.__addr, self.__key1_data1_msb, self.__key1_data1_lsb, value)
class RD_KEY1_DATA2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xc4
        self.__key1_data2_lsb = 0
        self.__key1_data2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key1_data2(self):
        return self.__MEM.rdm(self.__addr, self.__key1_data2_msb, self.__key1_data2_lsb)
    @key1_data2.setter
    def key1_data2(self, value):
        return self.__MEM.wrm(self.__addr, self.__key1_data2_msb, self.__key1_data2_lsb, value)
class RD_KEY1_DATA3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xc8
        self.__key1_data3_lsb = 0
        self.__key1_data3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key1_data3(self):
        return self.__MEM.rdm(self.__addr, self.__key1_data3_msb, self.__key1_data3_lsb)
    @key1_data3.setter
    def key1_data3(self, value):
        return self.__MEM.wrm(self.__addr, self.__key1_data3_msb, self.__key1_data3_lsb, value)
class RD_KEY1_DATA4(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xcc
        self.__key1_data4_lsb = 0
        self.__key1_data4_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key1_data4(self):
        return self.__MEM.rdm(self.__addr, self.__key1_data4_msb, self.__key1_data4_lsb)
    @key1_data4.setter
    def key1_data4(self, value):
        return self.__MEM.wrm(self.__addr, self.__key1_data4_msb, self.__key1_data4_lsb, value)
class RD_KEY1_DATA5(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xd0
        self.__key1_data5_lsb = 0
        self.__key1_data5_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key1_data5(self):
        return self.__MEM.rdm(self.__addr, self.__key1_data5_msb, self.__key1_data5_lsb)
    @key1_data5.setter
    def key1_data5(self, value):
        return self.__MEM.wrm(self.__addr, self.__key1_data5_msb, self.__key1_data5_lsb, value)
class RD_KEY1_DATA6(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xd4
        self.__key1_data6_lsb = 0
        self.__key1_data6_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key1_data6(self):
        return self.__MEM.rdm(self.__addr, self.__key1_data6_msb, self.__key1_data6_lsb)
    @key1_data6.setter
    def key1_data6(self, value):
        return self.__MEM.wrm(self.__addr, self.__key1_data6_msb, self.__key1_data6_lsb, value)
class RD_KEY1_DATA7(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xd8
        self.__key1_data7_lsb = 0
        self.__key1_data7_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key1_data7(self):
        return self.__MEM.rdm(self.__addr, self.__key1_data7_msb, self.__key1_data7_lsb)
    @key1_data7.setter
    def key1_data7(self, value):
        return self.__MEM.wrm(self.__addr, self.__key1_data7_msb, self.__key1_data7_lsb, value)
class RD_KEY2_DATA0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xdc
        self.__key2_data0_lsb = 0
        self.__key2_data0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key2_data0(self):
        return self.__MEM.rdm(self.__addr, self.__key2_data0_msb, self.__key2_data0_lsb)
    @key2_data0.setter
    def key2_data0(self, value):
        return self.__MEM.wrm(self.__addr, self.__key2_data0_msb, self.__key2_data0_lsb, value)
class RD_KEY2_DATA1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xe0
        self.__key2_data1_lsb = 0
        self.__key2_data1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key2_data1(self):
        return self.__MEM.rdm(self.__addr, self.__key2_data1_msb, self.__key2_data1_lsb)
    @key2_data1.setter
    def key2_data1(self, value):
        return self.__MEM.wrm(self.__addr, self.__key2_data1_msb, self.__key2_data1_lsb, value)
class RD_KEY2_DATA2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xe4
        self.__key2_data2_lsb = 0
        self.__key2_data2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key2_data2(self):
        return self.__MEM.rdm(self.__addr, self.__key2_data2_msb, self.__key2_data2_lsb)
    @key2_data2.setter
    def key2_data2(self, value):
        return self.__MEM.wrm(self.__addr, self.__key2_data2_msb, self.__key2_data2_lsb, value)
class RD_KEY2_DATA3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xe8
        self.__key2_data3_lsb = 0
        self.__key2_data3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key2_data3(self):
        return self.__MEM.rdm(self.__addr, self.__key2_data3_msb, self.__key2_data3_lsb)
    @key2_data3.setter
    def key2_data3(self, value):
        return self.__MEM.wrm(self.__addr, self.__key2_data3_msb, self.__key2_data3_lsb, value)
class RD_KEY2_DATA4(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xec
        self.__key2_data4_lsb = 0
        self.__key2_data4_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key2_data4(self):
        return self.__MEM.rdm(self.__addr, self.__key2_data4_msb, self.__key2_data4_lsb)
    @key2_data4.setter
    def key2_data4(self, value):
        return self.__MEM.wrm(self.__addr, self.__key2_data4_msb, self.__key2_data4_lsb, value)
class RD_KEY2_DATA5(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xf0
        self.__key2_data5_lsb = 0
        self.__key2_data5_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key2_data5(self):
        return self.__MEM.rdm(self.__addr, self.__key2_data5_msb, self.__key2_data5_lsb)
    @key2_data5.setter
    def key2_data5(self, value):
        return self.__MEM.wrm(self.__addr, self.__key2_data5_msb, self.__key2_data5_lsb, value)
class RD_KEY2_DATA6(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xf4
        self.__key2_data6_lsb = 0
        self.__key2_data6_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key2_data6(self):
        return self.__MEM.rdm(self.__addr, self.__key2_data6_msb, self.__key2_data6_lsb)
    @key2_data6.setter
    def key2_data6(self, value):
        return self.__MEM.wrm(self.__addr, self.__key2_data6_msb, self.__key2_data6_lsb, value)
class RD_KEY2_DATA7(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xf8
        self.__key2_data7_lsb = 0
        self.__key2_data7_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key2_data7(self):
        return self.__MEM.rdm(self.__addr, self.__key2_data7_msb, self.__key2_data7_lsb)
    @key2_data7.setter
    def key2_data7(self, value):
        return self.__MEM.wrm(self.__addr, self.__key2_data7_msb, self.__key2_data7_lsb, value)
class RD_KEY3_DATA0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0xfc
        self.__key3_data0_lsb = 0
        self.__key3_data0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key3_data0(self):
        return self.__MEM.rdm(self.__addr, self.__key3_data0_msb, self.__key3_data0_lsb)
    @key3_data0.setter
    def key3_data0(self, value):
        return self.__MEM.wrm(self.__addr, self.__key3_data0_msb, self.__key3_data0_lsb, value)
class RD_KEY3_DATA1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x100
        self.__key3_data1_lsb = 0
        self.__key3_data1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key3_data1(self):
        return self.__MEM.rdm(self.__addr, self.__key3_data1_msb, self.__key3_data1_lsb)
    @key3_data1.setter
    def key3_data1(self, value):
        return self.__MEM.wrm(self.__addr, self.__key3_data1_msb, self.__key3_data1_lsb, value)
class RD_KEY3_DATA2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x104
        self.__key3_data2_lsb = 0
        self.__key3_data2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key3_data2(self):
        return self.__MEM.rdm(self.__addr, self.__key3_data2_msb, self.__key3_data2_lsb)
    @key3_data2.setter
    def key3_data2(self, value):
        return self.__MEM.wrm(self.__addr, self.__key3_data2_msb, self.__key3_data2_lsb, value)
class RD_KEY3_DATA3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x108
        self.__key3_data3_lsb = 0
        self.__key3_data3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key3_data3(self):
        return self.__MEM.rdm(self.__addr, self.__key3_data3_msb, self.__key3_data3_lsb)
    @key3_data3.setter
    def key3_data3(self, value):
        return self.__MEM.wrm(self.__addr, self.__key3_data3_msb, self.__key3_data3_lsb, value)
class RD_KEY3_DATA4(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x10c
        self.__key3_data4_lsb = 0
        self.__key3_data4_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key3_data4(self):
        return self.__MEM.rdm(self.__addr, self.__key3_data4_msb, self.__key3_data4_lsb)
    @key3_data4.setter
    def key3_data4(self, value):
        return self.__MEM.wrm(self.__addr, self.__key3_data4_msb, self.__key3_data4_lsb, value)
class RD_KEY3_DATA5(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x110
        self.__key3_data5_lsb = 0
        self.__key3_data5_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key3_data5(self):
        return self.__MEM.rdm(self.__addr, self.__key3_data5_msb, self.__key3_data5_lsb)
    @key3_data5.setter
    def key3_data5(self, value):
        return self.__MEM.wrm(self.__addr, self.__key3_data5_msb, self.__key3_data5_lsb, value)
class RD_KEY3_DATA6(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x114
        self.__key3_data6_lsb = 0
        self.__key3_data6_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key3_data6(self):
        return self.__MEM.rdm(self.__addr, self.__key3_data6_msb, self.__key3_data6_lsb)
    @key3_data6.setter
    def key3_data6(self, value):
        return self.__MEM.wrm(self.__addr, self.__key3_data6_msb, self.__key3_data6_lsb, value)
class RD_KEY3_DATA7(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x118
        self.__key3_data7_lsb = 0
        self.__key3_data7_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key3_data7(self):
        return self.__MEM.rdm(self.__addr, self.__key3_data7_msb, self.__key3_data7_lsb)
    @key3_data7.setter
    def key3_data7(self, value):
        return self.__MEM.wrm(self.__addr, self.__key3_data7_msb, self.__key3_data7_lsb, value)
class RD_KEY4_DATA0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x11c
        self.__key4_data0_lsb = 0
        self.__key4_data0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key4_data0(self):
        return self.__MEM.rdm(self.__addr, self.__key4_data0_msb, self.__key4_data0_lsb)
    @key4_data0.setter
    def key4_data0(self, value):
        return self.__MEM.wrm(self.__addr, self.__key4_data0_msb, self.__key4_data0_lsb, value)
class RD_KEY4_DATA1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x120
        self.__key4_data1_lsb = 0
        self.__key4_data1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key4_data1(self):
        return self.__MEM.rdm(self.__addr, self.__key4_data1_msb, self.__key4_data1_lsb)
    @key4_data1.setter
    def key4_data1(self, value):
        return self.__MEM.wrm(self.__addr, self.__key4_data1_msb, self.__key4_data1_lsb, value)
class RD_KEY4_DATA2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x124
        self.__key4_data2_lsb = 0
        self.__key4_data2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key4_data2(self):
        return self.__MEM.rdm(self.__addr, self.__key4_data2_msb, self.__key4_data2_lsb)
    @key4_data2.setter
    def key4_data2(self, value):
        return self.__MEM.wrm(self.__addr, self.__key4_data2_msb, self.__key4_data2_lsb, value)
class RD_KEY4_DATA3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x128
        self.__key4_data3_lsb = 0
        self.__key4_data3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key4_data3(self):
        return self.__MEM.rdm(self.__addr, self.__key4_data3_msb, self.__key4_data3_lsb)
    @key4_data3.setter
    def key4_data3(self, value):
        return self.__MEM.wrm(self.__addr, self.__key4_data3_msb, self.__key4_data3_lsb, value)
class RD_KEY4_DATA4(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x12c
        self.__key4_data4_lsb = 0
        self.__key4_data4_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key4_data4(self):
        return self.__MEM.rdm(self.__addr, self.__key4_data4_msb, self.__key4_data4_lsb)
    @key4_data4.setter
    def key4_data4(self, value):
        return self.__MEM.wrm(self.__addr, self.__key4_data4_msb, self.__key4_data4_lsb, value)
class RD_KEY4_DATA5(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x130
        self.__key4_data5_lsb = 0
        self.__key4_data5_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key4_data5(self):
        return self.__MEM.rdm(self.__addr, self.__key4_data5_msb, self.__key4_data5_lsb)
    @key4_data5.setter
    def key4_data5(self, value):
        return self.__MEM.wrm(self.__addr, self.__key4_data5_msb, self.__key4_data5_lsb, value)
class RD_KEY4_DATA6(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x134
        self.__key4_data6_lsb = 0
        self.__key4_data6_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key4_data6(self):
        return self.__MEM.rdm(self.__addr, self.__key4_data6_msb, self.__key4_data6_lsb)
    @key4_data6.setter
    def key4_data6(self, value):
        return self.__MEM.wrm(self.__addr, self.__key4_data6_msb, self.__key4_data6_lsb, value)
class RD_KEY4_DATA7(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x138
        self.__key4_data7_lsb = 0
        self.__key4_data7_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key4_data7(self):
        return self.__MEM.rdm(self.__addr, self.__key4_data7_msb, self.__key4_data7_lsb)
    @key4_data7.setter
    def key4_data7(self, value):
        return self.__MEM.wrm(self.__addr, self.__key4_data7_msb, self.__key4_data7_lsb, value)
class RD_KEY5_DATA0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x13c
        self.__key5_data0_lsb = 0
        self.__key5_data0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key5_data0(self):
        return self.__MEM.rdm(self.__addr, self.__key5_data0_msb, self.__key5_data0_lsb)
    @key5_data0.setter
    def key5_data0(self, value):
        return self.__MEM.wrm(self.__addr, self.__key5_data0_msb, self.__key5_data0_lsb, value)
class RD_KEY5_DATA1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x140
        self.__key5_data1_lsb = 0
        self.__key5_data1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key5_data1(self):
        return self.__MEM.rdm(self.__addr, self.__key5_data1_msb, self.__key5_data1_lsb)
    @key5_data1.setter
    def key5_data1(self, value):
        return self.__MEM.wrm(self.__addr, self.__key5_data1_msb, self.__key5_data1_lsb, value)
class RD_KEY5_DATA2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x144
        self.__key5_data2_lsb = 0
        self.__key5_data2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key5_data2(self):
        return self.__MEM.rdm(self.__addr, self.__key5_data2_msb, self.__key5_data2_lsb)
    @key5_data2.setter
    def key5_data2(self, value):
        return self.__MEM.wrm(self.__addr, self.__key5_data2_msb, self.__key5_data2_lsb, value)
class RD_KEY5_DATA3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x148
        self.__key5_data3_lsb = 0
        self.__key5_data3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key5_data3(self):
        return self.__MEM.rdm(self.__addr, self.__key5_data3_msb, self.__key5_data3_lsb)
    @key5_data3.setter
    def key5_data3(self, value):
        return self.__MEM.wrm(self.__addr, self.__key5_data3_msb, self.__key5_data3_lsb, value)
class RD_KEY5_DATA4(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x14c
        self.__key5_data4_lsb = 0
        self.__key5_data4_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key5_data4(self):
        return self.__MEM.rdm(self.__addr, self.__key5_data4_msb, self.__key5_data4_lsb)
    @key5_data4.setter
    def key5_data4(self, value):
        return self.__MEM.wrm(self.__addr, self.__key5_data4_msb, self.__key5_data4_lsb, value)
class RD_KEY5_DATA5(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x150
        self.__key5_data5_lsb = 0
        self.__key5_data5_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key5_data5(self):
        return self.__MEM.rdm(self.__addr, self.__key5_data5_msb, self.__key5_data5_lsb)
    @key5_data5.setter
    def key5_data5(self, value):
        return self.__MEM.wrm(self.__addr, self.__key5_data5_msb, self.__key5_data5_lsb, value)
class RD_KEY5_DATA6(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x154
        self.__key5_data6_lsb = 0
        self.__key5_data6_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key5_data6(self):
        return self.__MEM.rdm(self.__addr, self.__key5_data6_msb, self.__key5_data6_lsb)
    @key5_data6.setter
    def key5_data6(self, value):
        return self.__MEM.wrm(self.__addr, self.__key5_data6_msb, self.__key5_data6_lsb, value)
class RD_KEY5_DATA7(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x158
        self.__key5_data7_lsb = 0
        self.__key5_data7_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key5_data7(self):
        return self.__MEM.rdm(self.__addr, self.__key5_data7_msb, self.__key5_data7_lsb)
    @key5_data7.setter
    def key5_data7(self, value):
        return self.__MEM.wrm(self.__addr, self.__key5_data7_msb, self.__key5_data7_lsb, value)
class RD_KEY6_DATA0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x15c
        self.__key6_data0_lsb = 0
        self.__key6_data0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key6_data0(self):
        return self.__MEM.rdm(self.__addr, self.__key6_data0_msb, self.__key6_data0_lsb)
    @key6_data0.setter
    def key6_data0(self, value):
        return self.__MEM.wrm(self.__addr, self.__key6_data0_msb, self.__key6_data0_lsb, value)
class RD_KEY6_DATA1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x160
        self.__key6_data1_lsb = 0
        self.__key6_data1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key6_data1(self):
        return self.__MEM.rdm(self.__addr, self.__key6_data1_msb, self.__key6_data1_lsb)
    @key6_data1.setter
    def key6_data1(self, value):
        return self.__MEM.wrm(self.__addr, self.__key6_data1_msb, self.__key6_data1_lsb, value)
class RD_KEY6_DATA2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x164
        self.__key6_data2_lsb = 0
        self.__key6_data2_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key6_data2(self):
        return self.__MEM.rdm(self.__addr, self.__key6_data2_msb, self.__key6_data2_lsb)
    @key6_data2.setter
    def key6_data2(self, value):
        return self.__MEM.wrm(self.__addr, self.__key6_data2_msb, self.__key6_data2_lsb, value)
class RD_KEY6_DATA3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x168
        self.__key6_data3_lsb = 0
        self.__key6_data3_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key6_data3(self):
        return self.__MEM.rdm(self.__addr, self.__key6_data3_msb, self.__key6_data3_lsb)
    @key6_data3.setter
    def key6_data3(self, value):
        return self.__MEM.wrm(self.__addr, self.__key6_data3_msb, self.__key6_data3_lsb, value)
class RD_KEY6_DATA4(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x16c
        self.__key6_data4_lsb = 0
        self.__key6_data4_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key6_data4(self):
        return self.__MEM.rdm(self.__addr, self.__key6_data4_msb, self.__key6_data4_lsb)
    @key6_data4.setter
    def key6_data4(self, value):
        return self.__MEM.wrm(self.__addr, self.__key6_data4_msb, self.__key6_data4_lsb, value)
class RD_KEY6_DATA5(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x170
        self.__key6_data5_lsb = 0
        self.__key6_data5_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key6_data5(self):
        return self.__MEM.rdm(self.__addr, self.__key6_data5_msb, self.__key6_data5_lsb)
    @key6_data5.setter
    def key6_data5(self, value):
        return self.__MEM.wrm(self.__addr, self.__key6_data5_msb, self.__key6_data5_lsb, value)
class RD_KEY6_DATA6(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x174
        self.__key6_data6_lsb = 0
        self.__key6_data6_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key6_data6(self):
        return self.__MEM.rdm(self.__addr, self.__key6_data6_msb, self.__key6_data6_lsb)
    @key6_data6.setter
    def key6_data6(self, value):
        return self.__MEM.wrm(self.__addr, self.__key6_data6_msb, self.__key6_data6_lsb, value)
class RD_KEY6_DATA7(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x178
        self.__key6_data7_lsb = 0
        self.__key6_data7_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def key6_data7(self):
        return self.__MEM.rdm(self.__addr, self.__key6_data7_msb, self.__key6_data7_lsb)
    @key6_data7.setter
    def key6_data7(self, value):
        return self.__MEM.wrm(self.__addr, self.__key6_data7_msb, self.__key6_data7_lsb, value)
class RD_REPEAT_ERR0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x17c
        self.__rd_sdio_drefh_err_lsb = 30
        self.__rd_sdio_drefh_err_msb = 31
        self.__rd_sdio_modecurlim_err_lsb = 29
        self.__rd_sdio_modecurlim_err_msb = 29
        self.__rd_usb_dres_err_lsb = 25
        self.__rd_usb_dres_err_msb = 28
        self.__rd_usb_exchg_pins_err_lsb = 24
        self.__rd_usb_exchg_pins_err_msb = 24
        self.__rd_usb_drefl_err_lsb = 22
        self.__rd_usb_drefl_err_msb = 23
        self.__rd_usb_drefh_err_lsb = 20
        self.__rd_usb_drefh_err_msb = 21
        self.__rd_dis_download_manual_encrypt_err_lsb = 19
        self.__rd_dis_download_manual_encrypt_err_msb = 19
        self.__rd_hard_dis_jtag_err_lsb = 18
        self.__rd_hard_dis_jtag_err_msb = 18
        self.__rd_soft_dis_jtag_err_lsb = 17
        self.__rd_soft_dis_jtag_err_msb = 17
        self.__rd_dis_efuse_ate_wr_err_lsb = 16
        self.__rd_dis_efuse_ate_wr_err_msb = 16
        self.__rd_dis_sdio_access_err_lsb = 15
        self.__rd_dis_sdio_access_err_msb = 15
        self.__rd_dis_can_err_lsb = 14
        self.__rd_dis_can_err_msb = 14
        self.__rd_dis_usb_err_lsb = 13
        self.__rd_dis_usb_err_msb = 13
        self.__rd_dis_bt_err_lsb = 12
        self.__rd_dis_bt_err_msb = 12
        self.__rd_dis_download_dcache_err_lsb = 11
        self.__rd_dis_download_dcache_err_msb = 11
        self.__rd_dis_download_icache_err_lsb = 10
        self.__rd_dis_download_icache_err_msb = 10
        self.__rd_dis_dcache_err_lsb = 9
        self.__rd_dis_dcache_err_msb = 9
        self.__rd_dis_icache_err_lsb = 8
        self.__rd_dis_icache_err_msb = 8
        self.__rd_dis_rtc_ram_boot_err_lsb = 7
        self.__rd_dis_rtc_ram_boot_err_msb = 7
        self.__rd_rd_dis_err_lsb = 0
        self.__rd_rd_dis_err_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rd_sdio_drefh_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_sdio_drefh_err_msb, self.__rd_sdio_drefh_err_lsb)
    @rd_sdio_drefh_err.setter
    def rd_sdio_drefh_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_sdio_drefh_err_msb, self.__rd_sdio_drefh_err_lsb, value)

    @property
    def rd_sdio_modecurlim_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_sdio_modecurlim_err_msb, self.__rd_sdio_modecurlim_err_lsb)
    @rd_sdio_modecurlim_err.setter
    def rd_sdio_modecurlim_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_sdio_modecurlim_err_msb, self.__rd_sdio_modecurlim_err_lsb, value)

    @property
    def rd_usb_dres_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_usb_dres_err_msb, self.__rd_usb_dres_err_lsb)
    @rd_usb_dres_err.setter
    def rd_usb_dres_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_usb_dres_err_msb, self.__rd_usb_dres_err_lsb, value)

    @property
    def rd_usb_exchg_pins_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_usb_exchg_pins_err_msb, self.__rd_usb_exchg_pins_err_lsb)
    @rd_usb_exchg_pins_err.setter
    def rd_usb_exchg_pins_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_usb_exchg_pins_err_msb, self.__rd_usb_exchg_pins_err_lsb, value)

    @property
    def rd_usb_drefl_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_usb_drefl_err_msb, self.__rd_usb_drefl_err_lsb)
    @rd_usb_drefl_err.setter
    def rd_usb_drefl_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_usb_drefl_err_msb, self.__rd_usb_drefl_err_lsb, value)

    @property
    def rd_usb_drefh_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_usb_drefh_err_msb, self.__rd_usb_drefh_err_lsb)
    @rd_usb_drefh_err.setter
    def rd_usb_drefh_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_usb_drefh_err_msb, self.__rd_usb_drefh_err_lsb, value)

    @property
    def rd_dis_download_manual_encrypt_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_dis_download_manual_encrypt_err_msb, self.__rd_dis_download_manual_encrypt_err_lsb)
    @rd_dis_download_manual_encrypt_err.setter
    def rd_dis_download_manual_encrypt_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_dis_download_manual_encrypt_err_msb, self.__rd_dis_download_manual_encrypt_err_lsb, value)

    @property
    def rd_hard_dis_jtag_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_hard_dis_jtag_err_msb, self.__rd_hard_dis_jtag_err_lsb)
    @rd_hard_dis_jtag_err.setter
    def rd_hard_dis_jtag_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_hard_dis_jtag_err_msb, self.__rd_hard_dis_jtag_err_lsb, value)

    @property
    def rd_soft_dis_jtag_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_soft_dis_jtag_err_msb, self.__rd_soft_dis_jtag_err_lsb)
    @rd_soft_dis_jtag_err.setter
    def rd_soft_dis_jtag_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_soft_dis_jtag_err_msb, self.__rd_soft_dis_jtag_err_lsb, value)

    @property
    def rd_dis_efuse_ate_wr_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_dis_efuse_ate_wr_err_msb, self.__rd_dis_efuse_ate_wr_err_lsb)
    @rd_dis_efuse_ate_wr_err.setter
    def rd_dis_efuse_ate_wr_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_dis_efuse_ate_wr_err_msb, self.__rd_dis_efuse_ate_wr_err_lsb, value)

    @property
    def rd_dis_sdio_access_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_dis_sdio_access_err_msb, self.__rd_dis_sdio_access_err_lsb)
    @rd_dis_sdio_access_err.setter
    def rd_dis_sdio_access_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_dis_sdio_access_err_msb, self.__rd_dis_sdio_access_err_lsb, value)

    @property
    def rd_dis_can_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_dis_can_err_msb, self.__rd_dis_can_err_lsb)
    @rd_dis_can_err.setter
    def rd_dis_can_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_dis_can_err_msb, self.__rd_dis_can_err_lsb, value)

    @property
    def rd_dis_usb_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_dis_usb_err_msb, self.__rd_dis_usb_err_lsb)
    @rd_dis_usb_err.setter
    def rd_dis_usb_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_dis_usb_err_msb, self.__rd_dis_usb_err_lsb, value)

    @property
    def rd_dis_bt_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_dis_bt_err_msb, self.__rd_dis_bt_err_lsb)
    @rd_dis_bt_err.setter
    def rd_dis_bt_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_dis_bt_err_msb, self.__rd_dis_bt_err_lsb, value)

    @property
    def rd_dis_download_dcache_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_dis_download_dcache_err_msb, self.__rd_dis_download_dcache_err_lsb)
    @rd_dis_download_dcache_err.setter
    def rd_dis_download_dcache_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_dis_download_dcache_err_msb, self.__rd_dis_download_dcache_err_lsb, value)

    @property
    def rd_dis_download_icache_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_dis_download_icache_err_msb, self.__rd_dis_download_icache_err_lsb)
    @rd_dis_download_icache_err.setter
    def rd_dis_download_icache_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_dis_download_icache_err_msb, self.__rd_dis_download_icache_err_lsb, value)

    @property
    def rd_dis_dcache_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_dis_dcache_err_msb, self.__rd_dis_dcache_err_lsb)
    @rd_dis_dcache_err.setter
    def rd_dis_dcache_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_dis_dcache_err_msb, self.__rd_dis_dcache_err_lsb, value)

    @property
    def rd_dis_icache_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_dis_icache_err_msb, self.__rd_dis_icache_err_lsb)
    @rd_dis_icache_err.setter
    def rd_dis_icache_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_dis_icache_err_msb, self.__rd_dis_icache_err_lsb, value)

    @property
    def rd_dis_rtc_ram_boot_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_dis_rtc_ram_boot_err_msb, self.__rd_dis_rtc_ram_boot_err_lsb)
    @rd_dis_rtc_ram_boot_err.setter
    def rd_dis_rtc_ram_boot_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_dis_rtc_ram_boot_err_msb, self.__rd_dis_rtc_ram_boot_err_lsb, value)

    @property
    def rd_rd_dis_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_rd_dis_err_msb, self.__rd_rd_dis_err_lsb)
    @rd_rd_dis_err.setter
    def rd_rd_dis_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_rd_dis_err_msb, self.__rd_rd_dis_err_lsb, value)
class RD_REPEAT_ERR1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x180
        self.__rd_key_purpose_1_err_lsb = 28
        self.__rd_key_purpose_1_err_msb = 31
        self.__rd_key_purpose_0_err_lsb = 24
        self.__rd_key_purpose_0_err_msb = 27
        self.__rd_secure_boot_key_revoke2_err_lsb = 23
        self.__rd_secure_boot_key_revoke2_err_msb = 23
        self.__rd_secure_boot_key_revoke1_err_lsb = 22
        self.__rd_secure_boot_key_revoke1_err_msb = 22
        self.__rd_secure_boot_key_revoke0_err_lsb = 21
        self.__rd_secure_boot_key_revoke0_err_msb = 21
        self.__rd_spi_boot_crypt_cnt_err_lsb = 18
        self.__rd_spi_boot_crypt_cnt_err_msb = 20
        self.__rd_wdt_delay_sel_err_lsb = 16
        self.__rd_wdt_delay_sel_err_msb = 17
        self.__rd_sdio_dcap_err_lsb = 14
        self.__rd_sdio_dcap_err_msb = 15
        self.__rd_sdio_init_err_lsb = 12
        self.__rd_sdio_init_err_msb = 13
        self.__rd_sdio_dcurlim_err_lsb = 9
        self.__rd_sdio_dcurlim_err_msb = 11
        self.__rd_sdio_encurlim_err_lsb = 8
        self.__rd_sdio_encurlim_err_msb = 8
        self.__rd_sdio_en_init_err_lsb = 7
        self.__rd_sdio_en_init_err_msb = 7
        self.__rd_sdio_force_err_lsb = 6
        self.__rd_sdio_force_err_msb = 6
        self.__rd_sdio_tieh_err_lsb = 5
        self.__rd_sdio_tieh_err_msb = 5
        self.__rd_sdio_xpd_err_lsb = 4
        self.__rd_sdio_xpd_err_msb = 4
        self.__rd_sdio_drefl_err_lsb = 2
        self.__rd_sdio_drefl_err_msb = 3
        self.__rd_sdio_drefm_err_lsb = 0
        self.__rd_sdio_drefm_err_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rd_key_purpose_1_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_key_purpose_1_err_msb, self.__rd_key_purpose_1_err_lsb)
    @rd_key_purpose_1_err.setter
    def rd_key_purpose_1_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_key_purpose_1_err_msb, self.__rd_key_purpose_1_err_lsb, value)

    @property
    def rd_key_purpose_0_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_key_purpose_0_err_msb, self.__rd_key_purpose_0_err_lsb)
    @rd_key_purpose_0_err.setter
    def rd_key_purpose_0_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_key_purpose_0_err_msb, self.__rd_key_purpose_0_err_lsb, value)

    @property
    def rd_secure_boot_key_revoke2_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_secure_boot_key_revoke2_err_msb, self.__rd_secure_boot_key_revoke2_err_lsb)
    @rd_secure_boot_key_revoke2_err.setter
    def rd_secure_boot_key_revoke2_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_secure_boot_key_revoke2_err_msb, self.__rd_secure_boot_key_revoke2_err_lsb, value)

    @property
    def rd_secure_boot_key_revoke1_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_secure_boot_key_revoke1_err_msb, self.__rd_secure_boot_key_revoke1_err_lsb)
    @rd_secure_boot_key_revoke1_err.setter
    def rd_secure_boot_key_revoke1_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_secure_boot_key_revoke1_err_msb, self.__rd_secure_boot_key_revoke1_err_lsb, value)

    @property
    def rd_secure_boot_key_revoke0_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_secure_boot_key_revoke0_err_msb, self.__rd_secure_boot_key_revoke0_err_lsb)
    @rd_secure_boot_key_revoke0_err.setter
    def rd_secure_boot_key_revoke0_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_secure_boot_key_revoke0_err_msb, self.__rd_secure_boot_key_revoke0_err_lsb, value)

    @property
    def rd_spi_boot_crypt_cnt_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_spi_boot_crypt_cnt_err_msb, self.__rd_spi_boot_crypt_cnt_err_lsb)
    @rd_spi_boot_crypt_cnt_err.setter
    def rd_spi_boot_crypt_cnt_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_spi_boot_crypt_cnt_err_msb, self.__rd_spi_boot_crypt_cnt_err_lsb, value)

    @property
    def rd_wdt_delay_sel_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_wdt_delay_sel_err_msb, self.__rd_wdt_delay_sel_err_lsb)
    @rd_wdt_delay_sel_err.setter
    def rd_wdt_delay_sel_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_wdt_delay_sel_err_msb, self.__rd_wdt_delay_sel_err_lsb, value)

    @property
    def rd_sdio_dcap_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_sdio_dcap_err_msb, self.__rd_sdio_dcap_err_lsb)
    @rd_sdio_dcap_err.setter
    def rd_sdio_dcap_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_sdio_dcap_err_msb, self.__rd_sdio_dcap_err_lsb, value)

    @property
    def rd_sdio_init_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_sdio_init_err_msb, self.__rd_sdio_init_err_lsb)
    @rd_sdio_init_err.setter
    def rd_sdio_init_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_sdio_init_err_msb, self.__rd_sdio_init_err_lsb, value)

    @property
    def rd_sdio_dcurlim_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_sdio_dcurlim_err_msb, self.__rd_sdio_dcurlim_err_lsb)
    @rd_sdio_dcurlim_err.setter
    def rd_sdio_dcurlim_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_sdio_dcurlim_err_msb, self.__rd_sdio_dcurlim_err_lsb, value)

    @property
    def rd_sdio_encurlim_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_sdio_encurlim_err_msb, self.__rd_sdio_encurlim_err_lsb)
    @rd_sdio_encurlim_err.setter
    def rd_sdio_encurlim_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_sdio_encurlim_err_msb, self.__rd_sdio_encurlim_err_lsb, value)

    @property
    def rd_sdio_en_init_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_sdio_en_init_err_msb, self.__rd_sdio_en_init_err_lsb)
    @rd_sdio_en_init_err.setter
    def rd_sdio_en_init_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_sdio_en_init_err_msb, self.__rd_sdio_en_init_err_lsb, value)

    @property
    def rd_sdio_force_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_sdio_force_err_msb, self.__rd_sdio_force_err_lsb)
    @rd_sdio_force_err.setter
    def rd_sdio_force_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_sdio_force_err_msb, self.__rd_sdio_force_err_lsb, value)

    @property
    def rd_sdio_tieh_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_sdio_tieh_err_msb, self.__rd_sdio_tieh_err_lsb)
    @rd_sdio_tieh_err.setter
    def rd_sdio_tieh_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_sdio_tieh_err_msb, self.__rd_sdio_tieh_err_lsb, value)

    @property
    def rd_sdio_xpd_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_sdio_xpd_err_msb, self.__rd_sdio_xpd_err_lsb)
    @rd_sdio_xpd_err.setter
    def rd_sdio_xpd_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_sdio_xpd_err_msb, self.__rd_sdio_xpd_err_lsb, value)

    @property
    def rd_sdio_drefl_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_sdio_drefl_err_msb, self.__rd_sdio_drefl_err_lsb)
    @rd_sdio_drefl_err.setter
    def rd_sdio_drefl_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_sdio_drefl_err_msb, self.__rd_sdio_drefl_err_lsb, value)

    @property
    def rd_sdio_drefm_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_sdio_drefm_err_msb, self.__rd_sdio_drefm_err_lsb)
    @rd_sdio_drefm_err.setter
    def rd_sdio_drefm_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_sdio_drefm_err_msb, self.__rd_sdio_drefm_err_lsb, value)
class RD_REPEAT_ERR2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x184
        self.__rd_flash_tpuw_err_lsb = 28
        self.__rd_flash_tpuw_err_msb = 31
        self.__rd_xtal_freq_err_lsb = 22
        self.__rd_xtal_freq_err_msb = 27
        self.__rd_secure_boot_aggressive_revoke_err_lsb = 21
        self.__rd_secure_boot_aggressive_revoke_err_msb = 21
        self.__rd_secure_boot_en_err_lsb = 20
        self.__rd_secure_boot_en_err_msb = 20
        self.__rd_key_purpose_6_err_lsb = 16
        self.__rd_key_purpose_6_err_msb = 19
        self.__rd_key_purpose_5_err_lsb = 12
        self.__rd_key_purpose_5_err_msb = 15
        self.__rd_key_purpose_4_err_lsb = 8
        self.__rd_key_purpose_4_err_msb = 11
        self.__rd_key_purpose_3_err_lsb = 4
        self.__rd_key_purpose_3_err_msb = 7
        self.__rd_key_purpose_2_err_lsb = 0
        self.__rd_key_purpose_2_err_msb = 3
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rd_flash_tpuw_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_flash_tpuw_err_msb, self.__rd_flash_tpuw_err_lsb)
    @rd_flash_tpuw_err.setter
    def rd_flash_tpuw_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_flash_tpuw_err_msb, self.__rd_flash_tpuw_err_lsb, value)

    @property
    def rd_xtal_freq_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_xtal_freq_err_msb, self.__rd_xtal_freq_err_lsb)
    @rd_xtal_freq_err.setter
    def rd_xtal_freq_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_xtal_freq_err_msb, self.__rd_xtal_freq_err_lsb, value)

    @property
    def rd_secure_boot_aggressive_revoke_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_secure_boot_aggressive_revoke_err_msb, self.__rd_secure_boot_aggressive_revoke_err_lsb)
    @rd_secure_boot_aggressive_revoke_err.setter
    def rd_secure_boot_aggressive_revoke_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_secure_boot_aggressive_revoke_err_msb, self.__rd_secure_boot_aggressive_revoke_err_lsb, value)

    @property
    def rd_secure_boot_en_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_secure_boot_en_err_msb, self.__rd_secure_boot_en_err_lsb)
    @rd_secure_boot_en_err.setter
    def rd_secure_boot_en_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_secure_boot_en_err_msb, self.__rd_secure_boot_en_err_lsb, value)

    @property
    def rd_key_purpose_6_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_key_purpose_6_err_msb, self.__rd_key_purpose_6_err_lsb)
    @rd_key_purpose_6_err.setter
    def rd_key_purpose_6_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_key_purpose_6_err_msb, self.__rd_key_purpose_6_err_lsb, value)

    @property
    def rd_key_purpose_5_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_key_purpose_5_err_msb, self.__rd_key_purpose_5_err_lsb)
    @rd_key_purpose_5_err.setter
    def rd_key_purpose_5_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_key_purpose_5_err_msb, self.__rd_key_purpose_5_err_lsb, value)

    @property
    def rd_key_purpose_4_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_key_purpose_4_err_msb, self.__rd_key_purpose_4_err_lsb)
    @rd_key_purpose_4_err.setter
    def rd_key_purpose_4_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_key_purpose_4_err_msb, self.__rd_key_purpose_4_err_lsb, value)

    @property
    def rd_key_purpose_3_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_key_purpose_3_err_msb, self.__rd_key_purpose_3_err_lsb)
    @rd_key_purpose_3_err.setter
    def rd_key_purpose_3_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_key_purpose_3_err_msb, self.__rd_key_purpose_3_err_lsb, value)

    @property
    def rd_key_purpose_2_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_key_purpose_2_err_msb, self.__rd_key_purpose_2_err_lsb)
    @rd_key_purpose_2_err.setter
    def rd_key_purpose_2_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_key_purpose_2_err_msb, self.__rd_key_purpose_2_err_lsb, value)
class RD_REPEAT_ERR3(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x188
        self.__rd_reserve_err_lsb = 8
        self.__rd_reserve_err_msb = 31
        self.__rd_uart_print_control_lsb = 6
        self.__rd_uart_print_control_msb = 7
        self.__rd_enable_security_download_lsb = 5
        self.__rd_enable_security_download_msb = 5
        self.__rd_dis_usb_download_mode_lsb = 4
        self.__rd_dis_usb_download_mode_msb = 4
        self.__rd_dis_tiny_basic_lsb = 3
        self.__rd_dis_tiny_basic_msb = 3
        self.__rd_uart_print_channel_lsb = 2
        self.__rd_uart_print_channel_msb = 2
        self.__rd_dis_legacy_spi_boot_err_lsb = 1
        self.__rd_dis_legacy_spi_boot_err_msb = 1
        self.__rd_dis_download_mode_err_lsb = 0
        self.__rd_dis_download_mode_err_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rd_reserve_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_reserve_err_msb, self.__rd_reserve_err_lsb)
    @rd_reserve_err.setter
    def rd_reserve_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_reserve_err_msb, self.__rd_reserve_err_lsb, value)

    @property
    def rd_uart_print_control(self):
        return self.__MEM.rdm(self.__addr, self.__rd_uart_print_control_msb, self.__rd_uart_print_control_lsb)
    @rd_uart_print_control.setter
    def rd_uart_print_control(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_uart_print_control_msb, self.__rd_uart_print_control_lsb, value)

    @property
    def rd_enable_security_download(self):
        return self.__MEM.rdm(self.__addr, self.__rd_enable_security_download_msb, self.__rd_enable_security_download_lsb)
    @rd_enable_security_download.setter
    def rd_enable_security_download(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_enable_security_download_msb, self.__rd_enable_security_download_lsb, value)

    @property
    def rd_dis_usb_download_mode(self):
        return self.__MEM.rdm(self.__addr, self.__rd_dis_usb_download_mode_msb, self.__rd_dis_usb_download_mode_lsb)
    @rd_dis_usb_download_mode.setter
    def rd_dis_usb_download_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_dis_usb_download_mode_msb, self.__rd_dis_usb_download_mode_lsb, value)

    @property
    def rd_dis_tiny_basic(self):
        return self.__MEM.rdm(self.__addr, self.__rd_dis_tiny_basic_msb, self.__rd_dis_tiny_basic_lsb)
    @rd_dis_tiny_basic.setter
    def rd_dis_tiny_basic(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_dis_tiny_basic_msb, self.__rd_dis_tiny_basic_lsb, value)

    @property
    def rd_uart_print_channel(self):
        return self.__MEM.rdm(self.__addr, self.__rd_uart_print_channel_msb, self.__rd_uart_print_channel_lsb)
    @rd_uart_print_channel.setter
    def rd_uart_print_channel(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_uart_print_channel_msb, self.__rd_uart_print_channel_lsb, value)

    @property
    def rd_dis_legacy_spi_boot_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_dis_legacy_spi_boot_err_msb, self.__rd_dis_legacy_spi_boot_err_lsb)
    @rd_dis_legacy_spi_boot_err.setter
    def rd_dis_legacy_spi_boot_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_dis_legacy_spi_boot_err_msb, self.__rd_dis_legacy_spi_boot_err_lsb, value)

    @property
    def rd_dis_download_mode_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_dis_download_mode_err_msb, self.__rd_dis_download_mode_err_lsb)
    @rd_dis_download_mode_err.setter
    def rd_dis_download_mode_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_dis_download_mode_err_msb, self.__rd_dis_download_mode_err_lsb, value)
class RD_REPEAT_ERR4(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x190
        self.__rd_chip_version_err_lsb = 0
        self.__rd_chip_version_err_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rd_chip_version_err(self):
        return self.__MEM.rdm(self.__addr, self.__rd_chip_version_err_msb, self.__rd_chip_version_err_lsb)
    @rd_chip_version_err.setter
    def rd_chip_version_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_chip_version_err_msb, self.__rd_chip_version_err_lsb, value)
class RD_RS_ERR0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x194
        self.__rd_key4_fail_lsb = 31
        self.__rd_key4_fail_msb = 31
        self.__rd_key4_err_num_lsb = 28
        self.__rd_key4_err_num_msb = 30
        self.__rd_key3_fail_lsb = 27
        self.__rd_key3_fail_msb = 27
        self.__rd_key3_err_num_lsb = 24
        self.__rd_key3_err_num_msb = 26
        self.__rd_key2_fail_lsb = 23
        self.__rd_key2_fail_msb = 23
        self.__rd_key2_err_num_lsb = 20
        self.__rd_key2_err_num_msb = 22
        self.__rd_key1_fail_lsb = 19
        self.__rd_key1_fail_msb = 19
        self.__rd_key1_err_num_lsb = 16
        self.__rd_key1_err_num_msb = 18
        self.__rd_key0_fail_lsb = 15
        self.__rd_key0_fail_msb = 15
        self.__rd_key0_err_num_lsb = 12
        self.__rd_key0_err_num_msb = 14
        self.__rd_usr_data_fail_lsb = 11
        self.__rd_usr_data_fail_msb = 11
        self.__rd_usr_data_err_num_lsb = 8
        self.__rd_usr_data_err_num_msb = 10
        self.__rd_sys_err_fail_lsb = 7
        self.__rd_sys_err_fail_msb = 7
        self.__rd_sys_err_num_lsb = 4
        self.__rd_sys_err_num_msb = 6
        self.__rd_mac_spi_8m_fail_lsb = 3
        self.__rd_mac_spi_8m_fail_msb = 3
        self.__rd_mac_spi_8m_err_num_lsb = 0
        self.__rd_mac_spi_8m_err_num_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rd_key4_fail(self):
        return self.__MEM.rdm(self.__addr, self.__rd_key4_fail_msb, self.__rd_key4_fail_lsb)
    @rd_key4_fail.setter
    def rd_key4_fail(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_key4_fail_msb, self.__rd_key4_fail_lsb, value)

    @property
    def rd_key4_err_num(self):
        return self.__MEM.rdm(self.__addr, self.__rd_key4_err_num_msb, self.__rd_key4_err_num_lsb)
    @rd_key4_err_num.setter
    def rd_key4_err_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_key4_err_num_msb, self.__rd_key4_err_num_lsb, value)

    @property
    def rd_key3_fail(self):
        return self.__MEM.rdm(self.__addr, self.__rd_key3_fail_msb, self.__rd_key3_fail_lsb)
    @rd_key3_fail.setter
    def rd_key3_fail(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_key3_fail_msb, self.__rd_key3_fail_lsb, value)

    @property
    def rd_key3_err_num(self):
        return self.__MEM.rdm(self.__addr, self.__rd_key3_err_num_msb, self.__rd_key3_err_num_lsb)
    @rd_key3_err_num.setter
    def rd_key3_err_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_key3_err_num_msb, self.__rd_key3_err_num_lsb, value)

    @property
    def rd_key2_fail(self):
        return self.__MEM.rdm(self.__addr, self.__rd_key2_fail_msb, self.__rd_key2_fail_lsb)
    @rd_key2_fail.setter
    def rd_key2_fail(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_key2_fail_msb, self.__rd_key2_fail_lsb, value)

    @property
    def rd_key2_err_num(self):
        return self.__MEM.rdm(self.__addr, self.__rd_key2_err_num_msb, self.__rd_key2_err_num_lsb)
    @rd_key2_err_num.setter
    def rd_key2_err_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_key2_err_num_msb, self.__rd_key2_err_num_lsb, value)

    @property
    def rd_key1_fail(self):
        return self.__MEM.rdm(self.__addr, self.__rd_key1_fail_msb, self.__rd_key1_fail_lsb)
    @rd_key1_fail.setter
    def rd_key1_fail(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_key1_fail_msb, self.__rd_key1_fail_lsb, value)

    @property
    def rd_key1_err_num(self):
        return self.__MEM.rdm(self.__addr, self.__rd_key1_err_num_msb, self.__rd_key1_err_num_lsb)
    @rd_key1_err_num.setter
    def rd_key1_err_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_key1_err_num_msb, self.__rd_key1_err_num_lsb, value)

    @property
    def rd_key0_fail(self):
        return self.__MEM.rdm(self.__addr, self.__rd_key0_fail_msb, self.__rd_key0_fail_lsb)
    @rd_key0_fail.setter
    def rd_key0_fail(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_key0_fail_msb, self.__rd_key0_fail_lsb, value)

    @property
    def rd_key0_err_num(self):
        return self.__MEM.rdm(self.__addr, self.__rd_key0_err_num_msb, self.__rd_key0_err_num_lsb)
    @rd_key0_err_num.setter
    def rd_key0_err_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_key0_err_num_msb, self.__rd_key0_err_num_lsb, value)

    @property
    def rd_usr_data_fail(self):
        return self.__MEM.rdm(self.__addr, self.__rd_usr_data_fail_msb, self.__rd_usr_data_fail_lsb)
    @rd_usr_data_fail.setter
    def rd_usr_data_fail(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_usr_data_fail_msb, self.__rd_usr_data_fail_lsb, value)

    @property
    def rd_usr_data_err_num(self):
        return self.__MEM.rdm(self.__addr, self.__rd_usr_data_err_num_msb, self.__rd_usr_data_err_num_lsb)
    @rd_usr_data_err_num.setter
    def rd_usr_data_err_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_usr_data_err_num_msb, self.__rd_usr_data_err_num_lsb, value)

    @property
    def rd_sys_err_fail(self):
        return self.__MEM.rdm(self.__addr, self.__rd_sys_err_fail_msb, self.__rd_sys_err_fail_lsb)
    @rd_sys_err_fail.setter
    def rd_sys_err_fail(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_sys_err_fail_msb, self.__rd_sys_err_fail_lsb, value)

    @property
    def rd_sys_err_num(self):
        return self.__MEM.rdm(self.__addr, self.__rd_sys_err_num_msb, self.__rd_sys_err_num_lsb)
    @rd_sys_err_num.setter
    def rd_sys_err_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_sys_err_num_msb, self.__rd_sys_err_num_lsb, value)

    @property
    def rd_mac_spi_8m_fail(self):
        return self.__MEM.rdm(self.__addr, self.__rd_mac_spi_8m_fail_msb, self.__rd_mac_spi_8m_fail_lsb)
    @rd_mac_spi_8m_fail.setter
    def rd_mac_spi_8m_fail(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_mac_spi_8m_fail_msb, self.__rd_mac_spi_8m_fail_lsb, value)

    @property
    def rd_mac_spi_8m_err_num(self):
        return self.__MEM.rdm(self.__addr, self.__rd_mac_spi_8m_err_num_msb, self.__rd_mac_spi_8m_err_num_lsb)
    @rd_mac_spi_8m_err_num.setter
    def rd_mac_spi_8m_err_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_mac_spi_8m_err_num_msb, self.__rd_mac_spi_8m_err_num_lsb, value)
class RD_RS_ERR1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x198
        self.__rd_key6_fail_lsb = 7
        self.__rd_key6_fail_msb = 7
        self.__rd_key6_err_num_lsb = 4
        self.__rd_key6_err_num_msb = 6
        self.__rd_key5_fail_lsb = 3
        self.__rd_key5_fail_msb = 3
        self.__rd_key5_err_num_lsb = 0
        self.__rd_key5_err_num_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rd_key6_fail(self):
        return self.__MEM.rdm(self.__addr, self.__rd_key6_fail_msb, self.__rd_key6_fail_lsb)
    @rd_key6_fail.setter
    def rd_key6_fail(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_key6_fail_msb, self.__rd_key6_fail_lsb, value)

    @property
    def rd_key6_err_num(self):
        return self.__MEM.rdm(self.__addr, self.__rd_key6_err_num_msb, self.__rd_key6_err_num_lsb)
    @rd_key6_err_num.setter
    def rd_key6_err_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_key6_err_num_msb, self.__rd_key6_err_num_lsb, value)

    @property
    def rd_key5_fail(self):
        return self.__MEM.rdm(self.__addr, self.__rd_key5_fail_msb, self.__rd_key5_fail_lsb)
    @rd_key5_fail.setter
    def rd_key5_fail(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_key5_fail_msb, self.__rd_key5_fail_lsb, value)

    @property
    def rd_key5_err_num(self):
        return self.__MEM.rdm(self.__addr, self.__rd_key5_err_num_msb, self.__rd_key5_err_num_lsb)
    @rd_key5_err_num.setter
    def rd_key5_err_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__rd_key5_err_num_msb, self.__rd_key5_err_num_lsb, value)
class EFUSE_CLK(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x19c
        self.__reg_clk_en_lsb = 16
        self.__reg_clk_en_msb = 16
        self.__reg_mem_pd_lsb = 0
        self.__reg_mem_pd_msb = 0
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
    def reg_mem_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mem_pd_msb, self.__reg_mem_pd_lsb)
    @reg_mem_pd.setter
    def reg_mem_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mem_pd_msb, self.__reg_mem_pd_lsb, value)
class EFUSE_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x1a0
        self.__efuse_op_code_lsb = 0
        self.__efuse_op_code_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_op_code(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_op_code_msb, self.__efuse_op_code_lsb)
    @efuse_op_code.setter
    def efuse_op_code(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_op_code_msb, self.__efuse_op_code_lsb, value)
class EFUSE_STATUS(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x1a4
        self.__repeat_err_cnt_lsb = 9
        self.__repeat_err_cnt_msb = 16
        self.__otp_vddq_is_sw_lsb = 8
        self.__otp_vddq_is_sw_msb = 8
        self.__otp_pgenb_sw_lsb = 7
        self.__otp_pgenb_sw_msb = 7
        self.__otp_csb_sw_lsb = 6
        self.__otp_csb_sw_msb = 6
        self.__otp_strobe_sw_lsb = 5
        self.__otp_strobe_sw_msb = 5
        self.__otp_vddq_c_sync2_lsb = 4
        self.__otp_vddq_c_sync2_msb = 4
        self.__otp_load_sw_lsb = 3
        self.__otp_load_sw_msb = 3
        self.__state_lsb = 0
        self.__state_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def repeat_err_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__repeat_err_cnt_msb, self.__repeat_err_cnt_lsb)
    @repeat_err_cnt.setter
    def repeat_err_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__repeat_err_cnt_msb, self.__repeat_err_cnt_lsb, value)

    @property
    def otp_vddq_is_sw(self):
        return self.__MEM.rdm(self.__addr, self.__otp_vddq_is_sw_msb, self.__otp_vddq_is_sw_lsb)
    @otp_vddq_is_sw.setter
    def otp_vddq_is_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__otp_vddq_is_sw_msb, self.__otp_vddq_is_sw_lsb, value)

    @property
    def otp_pgenb_sw(self):
        return self.__MEM.rdm(self.__addr, self.__otp_pgenb_sw_msb, self.__otp_pgenb_sw_lsb)
    @otp_pgenb_sw.setter
    def otp_pgenb_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__otp_pgenb_sw_msb, self.__otp_pgenb_sw_lsb, value)

    @property
    def otp_csb_sw(self):
        return self.__MEM.rdm(self.__addr, self.__otp_csb_sw_msb, self.__otp_csb_sw_lsb)
    @otp_csb_sw.setter
    def otp_csb_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__otp_csb_sw_msb, self.__otp_csb_sw_lsb, value)

    @property
    def otp_strobe_sw(self):
        return self.__MEM.rdm(self.__addr, self.__otp_strobe_sw_msb, self.__otp_strobe_sw_lsb)
    @otp_strobe_sw.setter
    def otp_strobe_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__otp_strobe_sw_msb, self.__otp_strobe_sw_lsb, value)

    @property
    def otp_vddq_c_sync2(self):
        return self.__MEM.rdm(self.__addr, self.__otp_vddq_c_sync2_msb, self.__otp_vddq_c_sync2_lsb)
    @otp_vddq_c_sync2.setter
    def otp_vddq_c_sync2(self, value):
        return self.__MEM.wrm(self.__addr, self.__otp_vddq_c_sync2_msb, self.__otp_vddq_c_sync2_lsb, value)

    @property
    def otp_load_sw(self):
        return self.__MEM.rdm(self.__addr, self.__otp_load_sw_msb, self.__otp_load_sw_lsb)
    @otp_load_sw.setter
    def otp_load_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__otp_load_sw_msb, self.__otp_load_sw_lsb, value)

    @property
    def state(self):
        return self.__MEM.rdm(self.__addr, self.__state_msb, self.__state_lsb)
    @state.setter
    def state(self, value):
        return self.__MEM.wrm(self.__addr, self.__state_msb, self.__state_lsb, value)
class EFUSE_CMD(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x1a8
        self.__efuse_blk_num_lsb = 2
        self.__efuse_blk_num_msb = 5
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
    def efuse_blk_num(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_blk_num_msb, self.__efuse_blk_num_lsb)
    @efuse_blk_num.setter
    def efuse_blk_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_blk_num_msb, self.__efuse_blk_num_lsb, value)

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
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x1ac
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
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x1b0
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
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x1b4
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
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x1b8
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
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x1bc
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
class EFUSE_RD_TIM_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x1c0
        self.__read_init_num_lsb = 24
        self.__read_init_num_msb = 31
        self.__efuse_tsur_a_lsb = 16
        self.__efuse_tsur_a_msb = 23
        self.__efuse_trd_lsb = 8
        self.__efuse_trd_msb = 15
        self.__efuse_thr_a_lsb = 0
        self.__efuse_thr_a_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def read_init_num(self):
        return self.__MEM.rdm(self.__addr, self.__read_init_num_msb, self.__read_init_num_lsb)
    @read_init_num.setter
    def read_init_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__read_init_num_msb, self.__read_init_num_lsb, value)

    @property
    def efuse_tsur_a(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_tsur_a_msb, self.__efuse_tsur_a_lsb)
    @efuse_tsur_a.setter
    def efuse_tsur_a(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_tsur_a_msb, self.__efuse_tsur_a_lsb, value)

    @property
    def efuse_trd(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_trd_msb, self.__efuse_trd_lsb)
    @efuse_trd.setter
    def efuse_trd(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_trd_msb, self.__efuse_trd_lsb, value)

    @property
    def efuse_thr_a(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_thr_a_msb, self.__efuse_thr_a_lsb)
    @efuse_thr_a.setter
    def efuse_thr_a(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_thr_a_msb, self.__efuse_thr_a_lsb, value)
class EFUSE_WR_TIM_CONF0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x1c4
        self.__efuse_tpgm_lsb = 16
        self.__efuse_tpgm_msb = 31
        self.__efuse_tpgm_inactive_lsb = 8
        self.__efuse_tpgm_inactive_msb = 15
        self.__efuse_thp_a_lsb = 0
        self.__efuse_thp_a_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def efuse_tpgm(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_tpgm_msb, self.__efuse_tpgm_lsb)
    @efuse_tpgm.setter
    def efuse_tpgm(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_tpgm_msb, self.__efuse_tpgm_lsb, value)

    @property
    def efuse_tpgm_inactive(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_tpgm_inactive_msb, self.__efuse_tpgm_inactive_lsb)
    @efuse_tpgm_inactive.setter
    def efuse_tpgm_inactive(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_tpgm_inactive_msb, self.__efuse_tpgm_inactive_lsb, value)

    @property
    def efuse_thp_a(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_thp_a_msb, self.__efuse_thp_a_lsb)
    @efuse_thp_a.setter
    def efuse_thp_a(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_thp_a_msb, self.__efuse_thp_a_lsb, value)
class EFUSE_WR_TIM_CONF1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = EFUSE_BASE + 0x1c8
        self.__pwr_on_num_lsb = 8
        self.__pwr_on_num_msb = 23
        self.__efuse_tsup_a_lsb = 0
        self.__efuse_tsup_a_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pwr_on_num(self):
        return self.__MEM.rdm(self.__addr, self.__pwr_on_num_msb, self.__pwr_on_num_lsb)
    @pwr_on_num.setter
    def pwr_on_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__pwr_on_num_msb, self.__pwr_on_num_lsb, value)

    @property
    def efuse_tsup_a(self):
        return self.__MEM.rdm(self.__addr, self.__efuse_tsup_a_msb, self.__efuse_tsup_a_lsb)
    @efuse_tsup_a.setter
    def efuse_tsup_a(self, value):
        return self.__MEM.wrm(self.__addr, self.__efuse_tsup_a_msb, self.__efuse_tsup_a_lsb, value)
class EFUSE_DATE(object):
    def __init__(self, channel, chipv = "CHIP722"):
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
        return 0x18101600
