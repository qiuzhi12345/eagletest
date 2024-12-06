from baselib.test_channel.com import COM as com
from baselib.loglib.log_lib import *
from hal.Init import HALS
from rtclib.rtc import WAKEUP_ENABLE
from baselib.instrument.dm import dm
import string

class DAC_TC_FUNC(object):
    def __init__(self, channel, chipv = "AUTO"):
        self.chip = HALS(channel, chipv)
        self.chipv = self.chip.chipv

    def tc000_dac1_dc_low_test(self):
        self.chip.dac.dc_out(1, 0)
    
    def tc001_dac1_dc_high_test(self):
        self.chip.dac.dc_out(1, 0xff)
        
    def tc002_dac2_dc_low_test(self):
        self.chip.dac.dc_out(2, 0)
    
    def tc003_dac2_dc_high_test(self):
        self.chip.dac.dc_out(2, 0xff)

    def tc004_dac1_ac_normal_test(self):
        self.chip.dac.cw_out(1)
        
    def tc005_dac2_ac_normal_test(self):
        self.chip.dac.cw_out(2)
        
    def tc006_ac_dcOffset_test(self):
        for i in range(0x12):
            self.chip.dac.cw_out(1, dc_offset = 0xf * i)
            time.sleep(1)

    def tc007_ac_fstep_test(self):
        for i in range(0x20):
            self.chip.dac.cw_out(1, fstep = 0x100 * (i + 1))
            time.sleep(1)

    def tc008_ac_scale_test(self):
        cw_scale_list = [0, 1, 2, 3]
        for scale_value in cw_scale_list:
            self.chip.dac.cw_out(1, cw_scale = scale_value)
            time.sleep(1)

    def tc009_ac_inv_test(self):
        phase_inv_list = [0, 1, 2, 3]
        for inv in phase_inv_list:
            self.chip.dac.cw_out(1, phase_inv = inv)
            time.sleep(1)

    def tc010_dac_lightsleep_test(self):
        self.mydm = dm()
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
        dac_value1 = string.atof(self.mydm.get_result('VDC'))
        self.chip.ulp.init()
        if self.chipv == "ESP32":
            self.chip.ulp.ldr(lowpower_state_addr, 19, 19)
        else:
            self.chip.ulp.ldr(lowpower_state_addr, lowpower_state_msb, lowpower_state_lsb)
        self.chip.ulp.blr(1, 6)
        self.chip.ulp.str(dac1_addr, dac1_xpd_msb, dac1_xpd_lsb, 1)
        self.chip.ulp.str(dac1_addr, dac1_xpd_force_msb, dac1_xpd_force_lsb, 1)
        self.chip.ulp.str(dac_ctrl2_addr, dac_cw_en1_msb, dac_cw_en1_lsb, 0)
        self.chip.ulp.str(dac1_addr, dac1_padc1_msb, dac1_pdac1_lsb,  0xff)
        self.chip.ulp.str(slp_timer_en_addr, slp_timer_en_msb, slp_timer_en_lsb, 0)
        self.chip.ulp.end()
        self.chip.ulp.start(1)
        self.chip.rtc_sleep.rtc_timer_wakeup(0, 650000)#about 4 seconds
        self.chip.rtc_sleep.special_sleep(0, WAKEUP_ENABLE['TIMER_EXPIRE_EN'].value, 0)
        time.sleep(0.5)
        dac_value2 =  string.atof(self.mydm.get_result('VDC'))
        if (dac_value1 < 1) and (dac_value2 > 3):
            return logpass()
        else:
            loginfo("dac_value1: %f, dac_value2: %f"%(dac_value1, dac_value2))
            return logfail()
        return

    def tc011_dac_deepsleep_test(self):
        self.mydm = dm()
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
        dac_value1 = string.atof(self.mydm.get_result('VDC'))
        self.chip.ulp.init()
        if self.chipv == "ESP32":
            self.chip.ulp.ldr(lowpower_state_addr, 19, 19)
        else:
            self.chip.ulp.ldr(lowpower_state_addr, lowpower_state_msb, lowpower_state_lsb)
        self.chip.ulp.blr(1, 6)
        self.chip.ulp.str(dac1_addr, dac1_xpd_msb, dac1_xpd_lsb, 1)
        self.chip.ulp.str(dac1_addr, dac1_xpd_force_msb, dac1_xpd_force_lsb, 1)
        self.chip.ulp.str(dac_ctrl2_addr, dac_cw_en1_msb, dac_cw_en1_lsb, 0)
        self.chip.ulp.str(dac1_addr, dac1_padc1_msb, dac1_pdac1_lsb,  0xff)
        self.chip.ulp.str(slp_timer_en_addr, slp_timer_en_msb, slp_timer_en_lsb, 0)
        self.chip.ulp.end()
        self.chip.ulp.start(1)
        self.chip.rtc_sleep.rtc_timer_wakeup(0, 650000)#about 4 seconds
        self.chip.rtc_sleep.special_sleep(0x29, WAKEUP_ENABLE['TIMER_EXPIRE_EN'].value, 0)
        time.sleep(0.5)
        dac_value2 =  string.atof(self.mydm.get_result('VDC'))
        if (dac_value1 < 1) and (dac_value2 > 3):
            return logpass()
        else:
            loginfo("dac_value1: %f, dac_value2: %f"%(dac_value1, dac_value2))
            return logfail()
        return
