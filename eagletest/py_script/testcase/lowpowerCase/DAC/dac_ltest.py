# -- coding: utf-8 --
from baselib.loglib.log_lib import *
from hal.Init import HALS
from baselib.instrument.dm import dm
from rtclib.rtc import ULP_PARAM
from rtclib.rtc import WAKEUP_ENABLE

class DAC_TC_LOWPOWER(object):
    def __init__(self, channel, chipv = "AUTO"):
        self.chip = HALS(channel, chipv)
        self.chipv = self.chip.chipv
        self.dac_data_path = '/home/lab/job/{}/lowpower_test/dac/'.format(self.chipv)

    def dac_2m_read(self, dac_file, dac_channel):
        self.chip.rtc_clk.set_cpu_freq(4)
        dac_file.write("2M,")
        for i in range(0, 0xff + 1, 5):
            self.chip.dac.dc_out(dac_channel, i)
            output = self.mydm.get_result('VDC')
            dac_file.write("%s,"%(output))
        dac_file.write("\n")
        return

    def dac_80m_read(self, dac_file, dac_channel):
        self.chip.rtc_clk.set_cpu_freq(1)
        dac_file.write("80M,")
        for i in range(0, 0xff + 1, 5):
            self.chip.dac.dc_out(dac_channel, i)
            output = self.mydm.get_result('VDC')
            dac_file.write("%s,"%(output))
        dac_file.write("\n")
        return

    def dac_wifiinit_read(self, dac_file, dac_channel):
        self.chip.rtc_clk.set_cpu_freq(1)
        self.chip.wifimac.mac_init()
        dac_file.write("wifiinit,")
        for i in range(0, 0xff + 1, 5):
            self.chip.dac.dc_out(dac_channel, i)
            output = self.mydm.get_result('VDC')
            dac_file.write("%s,"%(output))
        dac_file.write("\n")
        return

    def dac_lightsleep_read(self, dac_file, dac_channel):
        rtc_diag0_addr = self.chip.HWREG.RTC_CNTL.RTC_DIAG0._RTC_DIAG0__addr
        if self.chipv == "ESP32":
            lowpower_state_addr = self.chip.HWREG.RTC_CNTL.RTC_DIAG0._RTC_DIAG0__addr
            slp_timer_en_addr = self.chip.HWREG.RTC_CNTL.RTC_STATE0._RTC_STATE0__addr
            slp_timer_en_lsb = self.chip.HWREG.RTC_CNTL.RTC_STATE0._RTC_STATE0__reg_sar_slp_timer_en_lsb
            slp_timer_en_msb = self.chip.HWREG.RTC_CNTL.RTC_STATE0._RTC_STATE0__reg_sar_slp_timer_en_msb
        else:
            lowpower_state_addr = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__addr
            lowpower_state_lsb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_lsb
            lowpower_state_msb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_msb
            slp_timer_en_addr = self.chip.HWREG.RTC_CNTL.RTC_ULP_CP_TIMER._RTC_ULP_CP_TIMER__addr
            slp_timer_en_lsb = self.chip.HWREG.RTC_CNTL.RTC_ULP_CP_TIMER._RTC_ULP_CP_TIMER__reg_ulp_cp_slp_timer_en_lsb
            slp_timer_en_msb = self.chip.HWREG.RTC_CNTL.RTC_ULP_CP_TIMER._RTC_ULP_CP_TIMER__reg_ulp_cp_slp_timer_en_msb
        dac1_addr = self.chip.HWREG.RTC_IO.PAD_DAC1._PAD_DAC1__addr
        dac1_xpd_lsb = self.chip.HWREG.RTC_IO.PAD_DAC1._PAD_DAC1__reg_pdac1_xpd_dac_lsb
        dac1_xpd_msb = self.chip.HWREG.RTC_IO.PAD_DAC1._PAD_DAC1__reg_pdac1_xpd_dac_msb
        dac1_xpd_force_lsb = self.chip.HWREG.RTC_IO.PAD_DAC1._PAD_DAC1__reg_pdac1_dac_xpd_force_lsb
        dac1_xpd_force_msb = self.chip.HWREG.RTC_IO.PAD_DAC1._PAD_DAC1__reg_pdac1_dac_xpd_force_msb
        dac1_pdac1_lsb = self.chip.HWREG.RTC_IO.PAD_DAC1._PAD_DAC1__reg_pdac1_dac_lsb
        dac1_padc1_msb = self.chip.HWREG.RTC_IO.PAD_DAC1._PAD_DAC1__reg_pdac1_dac_msb
        dac_ctrl2_addr = self.chip.HWREG.SARADC.SAR_DAC_CTRL2._SAR_DAC_CTRL2__addr
        dac_cw_en1_lsb = self.chip.HWREG.SARADC.SAR_DAC_CTRL2._SAR_DAC_CTRL2__reg_dac_cw_en1_lsb
        dac_cw_en1_msb = self.chip.HWREG.SARADC.SAR_DAC_CTRL2._SAR_DAC_CTRL2__reg_dac_cw_en1_msb
        self.chip.dac.dc_out(1, 10)
        dac_file.write("lightsleep,")
        for i in range(0, 0xff + 1, 5):
            self.chip.rtc_timer.set_alarm_time_high(0xffffffff)
            self.chip.rtc_timer.set_alarm_time_low(0xffffffff)
            self.chip.ulp.init()
            if self.chipv == "ESP32":
                self.chip.ulp.ldr(lowpower_state_addr, 19, 19)
            else:
                self.chip.ulp.ldr(lowpower_state_addr, lowpower_state_msb, lowpower_state_lsb)
            self.chip.ulp.blr(1, 6)
            self.chip.ulp.str(dac1_addr, dac1_xpd_msb, dac1_xpd_lsb, 1)
            self.chip.ulp.str(dac1_addr, dac1_xpd_force_msb, dac1_xpd_force_lsb, 1)
            self.chip.ulp.str(dac_ctrl2_addr, dac_cw_en1_msb, dac_cw_en1_lsb, 0)
            self.chip.ulp.str(dac1_addr, dac1_padc1_msb, dac1_pdac1_lsb,  i)
            self.chip.ulp.str(slp_timer_en_addr, slp_timer_en_msb, slp_timer_en_lsb, 0)
            self.chip.ulp.end()
            self.chip.ulp.start(1)
            self.chip.rtc_sleep.rtc_timer_wakeup(0, 650000)#about 4 seconds
            self.chip.rtc_sleep.special_sleep(0, WAKEUP_ENABLE['TIMER_EXPIRE_EN'].value, 0)
            time.sleep(1)
            output = self.mydm.get_result('VDC')
            dac_file.write("%s,"%(output))
            time.sleep(4)
        dac_file.write("\n")
        return

    def dac_deepsleep_read(self, dac_file, dac_channel):
        if self.chipv == "ESP32":
            lowpower_state_addr = self.chip.HWREG.RTC_CNTL.RTC_DIAG0._RTC_DIAG0__addr
            slp_timer_en_addr = self.chip.HWREG.RTC_CNTL.RTC_STATE0._RTC_STATE0__addr
            slp_timer_en_lsb = self.chip.HWREG.RTC_CNTL.RTC_STATE0._RTC_STATE0__reg_sar_slp_timer_en_lsb
            slp_timer_en_msb = self.chip.HWREG.RTC_CNTL.RTC_STATE0._RTC_STATE0__reg_sar_slp_timer_en_msb
        else:
            lowpower_state_addr = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__addr
            lowpower_state_lsb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_lsb
            lowpower_state_msb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_msb
            slp_timer_en_addr = self.chip.HWREG.RTC_CNTL.RTC_ULP_CP_TIMER._RTC_ULP_CP_TIMER__addr
            slp_timer_en_lsb = self.chip.HWREG.RTC_CNTL.RTC_ULP_CP_TIMER._RTC_ULP_CP_TIMER__reg_ulp_cp_slp_timer_en_lsb
            slp_timer_en_msb = self.chip.HWREG.RTC_CNTL.RTC_ULP_CP_TIMER._RTC_ULP_CP_TIMER__reg_ulp_cp_slp_timer_en_msb
        dac1_addr = self.chip.HWREG.RTC_IO.PAD_DAC1._PAD_DAC1__addr
        dac1_xpd_lsb = self.chip.HWREG.RTC_IO.PAD_DAC1._PAD_DAC1__reg_pdac1_xpd_dac_lsb
        dac1_xpd_msb = self.chip.HWREG.RTC_IO.PAD_DAC1._PAD_DAC1__reg_pdac1_xpd_dac_msb
        dac1_xpd_force_lsb = self.chip.HWREG.RTC_IO.PAD_DAC1._PAD_DAC1__reg_pdac1_dac_xpd_force_lsb
        dac1_xpd_force_msb = self.chip.HWREG.RTC_IO.PAD_DAC1._PAD_DAC1__reg_pdac1_dac_xpd_force_msb
        dac1_pdac1_lsb = self.chip.HWREG.RTC_IO.PAD_DAC1._PAD_DAC1__reg_pdac1_dac_lsb
        dac1_padc1_msb = self.chip.HWREG.RTC_IO.PAD_DAC1._PAD_DAC1__reg_pdac1_dac_msb
        dac_ctrl2_addr = self.chip.HWREG.SARADC.SAR_DAC_CTRL2._SAR_DAC_CTRL2__addr
        dac_cw_en1_lsb = self.chip.HWREG.SARADC.SAR_DAC_CTRL2._SAR_DAC_CTRL2__reg_dac_cw_en1_lsb
        dac_cw_en1_msb = self.chip.HWREG.SARADC.SAR_DAC_CTRL2._SAR_DAC_CTRL2__reg_dac_cw_en1_msb
        self.chip.dac.dc_out(1, 10)
        dac_file.write("deepsleep,")
        for i in range(0, 0xff + 1, 5):
            self.chip.rtc_timer.set_alarm_time_high(0xffffffff)
            self.chip.rtc_timer.set_alarm_time_low(0xffffffff)
            self.chip.ulp.init()
            if self.chipv == "ESP32":
                self.chip.ulp.ldr(lowpower_state_addr, 19, 19)
            else:
                self.chip.ulp.ldr(lowpower_state_addr, lowpower_state_msb, lowpower_state_lsb)
            self.chip.ulp.blr(1, 6)
            self.chip.ulp.str(dac1_addr, dac1_xpd_msb, dac1_xpd_lsb, 1)
            self.chip.ulp.str(dac1_addr, dac1_xpd_force_msb, dac1_xpd_force_lsb, 1)
            self.chip.ulp.str(dac_ctrl2_addr, dac_cw_en1_msb, dac_cw_en1_lsb, 0)
            self.chip.ulp.str(dac1_addr, dac1_padc1_msb, dac1_pdac1_lsb,  i)
            self.chip.ulp.str(slp_timer_en_addr, slp_timer_en_msb, slp_timer_en_lsb, 0)
            self.chip.ulp.end()
            self.chip.ulp.start(1)
            self.chip.rtc_sleep.rtc_timer_wakeup(0, 650000)#about 4 seconds
            self.chip.rtc_sleep.special_sleep(0x29, WAKEUP_ENABLE['TIMER_EXPIRE_EN'].value, 0)
            time.sleep(1)
            output = self.mydm.get_result('VDC')
            dac_file.write("%s,"%(output))
            time.sleep(4)
        dac_file.write("\n")
        return

    def dac_differentmode_run(self, dac_channel = 1):
        '''
        测试时，只测试dac_channel为1的情况，以方便sleep时配置寄存器读取dac值。
        '''
        self.mydm = dm()
        with open(self.dac_data_path + 'dac_{}.csv'.format(time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())), 'w') as dac_file:
            dac_file.write("dac_input, ")
            for i in range(0, 0xff + 1, 5):
                dac_file.write("%d,"%(i))
            dac_file.write("\n")
            self.dac_2m_read(dac_file, dac_channel)
            self.dac_80m_read(dac_file, dac_channel)
            #self.dac_wifiinit_read(dac_file, dac_channel)
            self.dac_lightsleep_read(dac_file, dac_channel)
            self.chip.rtc_wdt.wdt_unlock()
            self.chip.rtc_wdt.wdt_stg_hold_len(0, 0xffff)
            self.chip.rtc_wdt.wdt_stg_act(0, 4)
            self.chip.rtc_wdt.wdt_init()
            time.sleep(2)
            self.dac_deepsleep_read(dac_file, dac_channel)
