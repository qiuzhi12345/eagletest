from baselib.test_channel.com import COM as com
from baselib.loglib.log_lib import *
from hal.Init import HALS
from rtclib.rtc import ULP_PARAM
from rtclib.rtc import WAKEUP_ENABLE
from rtclib.rtc import WAKEUP_REASON

class ULP_TC_FUNC(object):
    def __init__(self, channel, chipv = "AUTO"):
        self.chip = HALS(channel, chipv)
        self.chipv = self.chip.chipv
        
    def tc000_store_mem_byTimer_test(self):
        store_value_16bit = 0xaabb
        self.chip.ulp.init()
        self.chip.ulp.movi(ULP_PARAM['R1'].value, store_value_16bit)
        self.chip.ulp.movi(ULP_PARAM['R3'].value, 0)
        self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R3'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.end()
        self.chip.ulp.start(1)
        time.sleep(0.05)
        read_value_low16 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
        loginfo("store_value: 0x%x, read_value_low16: 0x%x\n"%(store_value_16bit, read_value_low16))
        if (read_value_low16 == store_value_16bit):
            return logpass()
        else:
            return logfail()
    
    def tc001_store_mem_byTOP_test(self):
        store_value_16bit = 0xccdd
        self.chip.ulp.init()
        self.chip.ulp.movi(ULP_PARAM['R1'].value, store_value_16bit)
        self.chip.ulp.movi(ULP_PARAM['R3'].value, 0)
        self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R3'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.end()
        self.chip.ulp.start(0)
        if self.chipv == "ESP32":
            time.sleep(0.05)
        else:
            time.sleep(1)
        read_value_low16 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
        loginfo("store_value: 0x%x, read_value_low16: 0x%x\n"%(store_value_16bit, read_value_low16))
        if (read_value_low16 == store_value_16bit):
            return logpass()
        else:
            logres("tc001_store_mem_byTOP_test: TEST FAIL\n")
            return logfail()

    def tc002_timer_wakeup_test(self):
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
        self.chip.ulp.init()
        if self.chipv == "ESP32":
            self.chip.ulp.ldr(lowpower_state_addr, 19, 19)
        else:
            self.chip.ulp.ldr(lowpower_state_addr, lowpower_state_msb, lowpower_state_lsb)
        self.chip.ulp.blr(1, 3)
        self.chip.ulp.str(slp_timer_en_addr, slp_timer_en_msb, slp_timer_en_lsb, 0)
        self.chip.ulp.wakeup()
        self.chip.ulp.end()
        self.chip.ulp.start(1)
        time.sleep(0.001)
        self.chip.rtc_sleep.sleep(0x2b, WAKEUP_ENABLE['SAR_TRIG_EN'].value, 0)
        time.sleep(1)
        wakeup_cause = int(self.chip.rtc_sleep.wakeup_cause())
        if wakeup_cause == WAKEUP_REASON['SAR_TRIG'].value:
            return logpass()
        else:
            return logfail()
    
    def tc003_alu_addi_test(self):
        value1_16bit = 0xb
        value2_16bit = 0xa
        self.chip.ulp.init()
        self.chip.ulp.movi(ULP_PARAM['R0'].value, 0)
        self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
        self.chip.ulp.addi(ULP_PARAM['R2'].value, ULP_PARAM['R1'].value, value2_16bit)
        self.chip.ulp.stm(ULP_PARAM['R2'].value, ULP_PARAM['R0'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.end()
        self.chip.ulp.start(0)
        time.sleep(0.05)
        read_value_low16 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
        loginfo("value1: %d, value2:%d, read_value_low16: %d\n"%(value1_16bit, value2_16bit, read_value_low16))
        if ((value1_16bit + value2_16bit) == read_value_low16):
            return logpass()
        else:
            return logfail()
    
    def tc004_alu_subi_test(self):
        value1_16bit = 0xb
        value2_16bit = 0xa
        self.chip.ulp.init()
        self.chip.ulp.movi(ULP_PARAM['R0'].value, 0)
        self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
        self.chip.ulp.subi(ULP_PARAM['R2'].value, ULP_PARAM['R1'].value, value2_16bit)
        self.chip.ulp.stm(ULP_PARAM['R2'].value, ULP_PARAM['R0'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.end()
        self.chip.ulp.start(0)
        time.sleep(0.05)
        read_value_low16 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
        loginfo("value1: %d, value2:%d, read_value_low16: %d\n"%(value1_16bit, value2_16bit, read_value_low16))
        if ((value1_16bit - value2_16bit) == read_value_low16):
            return logpass()
        else:
            return logfail()
    
    def tc005_alu_andi_test(self):
        value1_16bit = 0xb
        value2_16bit = 0
        self.chip.ulp.init()
        self.chip.ulp.movi(ULP_PARAM['R0'].value, 0)
        self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
        self.chip.ulp.andi(ULP_PARAM['R2'].value, ULP_PARAM['R1'].value, value2_16bit)
        self.chip.ulp.stm(ULP_PARAM['R2'].value, ULP_PARAM['R0'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.end()
        self.chip.ulp.start(0)
        time.sleep(0.05)
        read_value_low16 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
        loginfo("value1: %d, value2:%d, read_value_low16: %d\n"%(value1_16bit, value2_16bit, read_value_low16))
        if ((value1_16bit & value2_16bit) == read_value_low16):
            return logpass()
        else:
            return logfail()
    
    def tc006_alu_ori_test(self):
        value1_16bit = 0xb
        value2_16bit = 0
        self.chip.ulp.init()
        self.chip.ulp.movi(ULP_PARAM['R0'].value, 0)
        self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
        self.chip.ulp.ori(ULP_PARAM['R2'].value, ULP_PARAM['R1'].value, value2_16bit)
        self.chip.ulp.stm(ULP_PARAM['R2'].value, ULP_PARAM['R0'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.end()
        self.chip.ulp.start(0)
        time.sleep(0.05)
        read_value_low16 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
        loginfo("value1: %d, value2:%d, read_value_low16: %d\n"%(value1_16bit, value2_16bit, read_value_low16))
        if ((value1_16bit | value2_16bit) == read_value_low16):
            return logpass()
        else:
            return logfail()
    
    def tc007_alu_lshi_test(self):
        value1_16bit = 5
        left = 2
        self.chip.ulp.init()
        self.chip.ulp.movi(ULP_PARAM['R0'].value, 0)
        self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
        self.chip.ulp.lshi(ULP_PARAM['R2'].value, ULP_PARAM['R1'].value, left)
        self.chip.ulp.stm(ULP_PARAM['R2'].value, ULP_PARAM['R0'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.end()
        self.chip.ulp.start(0)
        time.sleep(0.05)
        read_value_low16 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
        loginfo("value1: %d, left: %d, read_value_low16: %d\n"%(value1_16bit, left, read_value_low16))
        if ((value1_16bit << left) == read_value_low16):
            return logpass()
        else:
            return logfail()
    
    def tc008_alu_rshi_test(self):
        value1_16bit = 0xf
        right = 2
        self.chip.ulp.init()
        self.chip.ulp.movi(ULP_PARAM['R0'].value, 0)
        self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
        self.chip.ulp.rshi(ULP_PARAM['R2'].value, ULP_PARAM['R1'].value, right)
        self.chip.ulp.stm(ULP_PARAM['R2'].value, ULP_PARAM['R0'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.end()
        self.chip.ulp.start(0)
        time.sleep(0.05)
        read_value_low16 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
        loginfo("value1: %d, left: %d, read_value_low16: %d\n"%(value1_16bit, right, read_value_low16))
        if ((value1_16bit >> right) == read_value_low16):
            return logpass()
        else:
            return logfail()
    
    def tc009_alu_movr_test(self):
        value_R1 = 0xf
        self.chip.ulp.init()
        self.chip.ulp.movi(ULP_PARAM['R0'].value, 0)
        self.chip.ulp.movi(ULP_PARAM['R1'].value, value_R1)
        self.chip.ulp.movr(ULP_PARAM['R2'].value, ULP_PARAM['R1'].value)
        self.chip.ulp.stm(ULP_PARAM['R2'].value, ULP_PARAM['R0'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.end()
        self.chip.ulp.start(0)
        time.sleep(0.05)
        value_R2 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
        loginfo("value_R1: %d, read_value_low16: %d\n"%(value_R1, value_R2))
        if (value_R2 == value_R1):
            return logpass()
        else:
            return logfail()
    
    def tc010_alu_addr_test(self):
        value1_16bit = 0xa
        value2_16bit = 0xb
        self.chip.ulp.init()
        self.chip.ulp.movi(ULP_PARAM['R0'].value, 0)
        self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
        self.chip.ulp.movi(ULP_PARAM['R2'].value, value2_16bit)
        self.chip.ulp.addr(ULP_PARAM['R3'].value, ULP_PARAM['R1'].value, ULP_PARAM['R2'].value)
        self.chip.ulp.stm(ULP_PARAM['R3'].value, ULP_PARAM['R0'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.end()
        self.chip.ulp.start(0)
        time.sleep(0.05)
        read_value = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
        loginfo("value1_16bit: %d, value2_16bit: %d, read_value_low16: %d\n"%(value1_16bit, value2_16bit, read_value))
        if ((value1_16bit + value2_16bit) == read_value):
            return logpass()
        else:
            return logfail()
    
    def tc011_alu_subr_test(self):
        value1_16bit = 0xb
        value2_16bit = 0xa
        self.chip.ulp.init()
        self.chip.ulp.movi(ULP_PARAM['R0'].value, 0)
        self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
        self.chip.ulp.movi(ULP_PARAM['R2'].value, value2_16bit)
        self.chip.ulp.subr(ULP_PARAM['R3'].value, ULP_PARAM['R1'].value, ULP_PARAM['R2'].value)
        self.chip.ulp.stm(ULP_PARAM['R3'].value, ULP_PARAM['R0'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.end()
        self.chip.ulp.start(0)
        time.sleep(0.05)
        read_value = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
        loginfo("value1_16bit: %d, value2_16bit: %d, read_value_low16: %d\n"%(value1_16bit, value2_16bit, read_value))
        if ((value1_16bit - value2_16bit) == read_value):
            return logpass()
        else:
            return logfail()
    
    def tc012_alu_andr_test(self):
        value1_16bit = 0xa
        value2_16bit = 0x0
        self.chip.ulp.init()
        self.chip.ulp.movi(ULP_PARAM['R0'].value, 0)
        self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
        self.chip.ulp.movi(ULP_PARAM['R2'].value, value2_16bit)
        self.chip.ulp.andr(ULP_PARAM['R3'].value, ULP_PARAM['R1'].value, ULP_PARAM['R2'].value)
        self.chip.ulp.stm(ULP_PARAM['R3'].value, ULP_PARAM['R0'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.end()
        self.chip.ulp.start(0)
        time.sleep(0.05)
        read_value = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
        loginfo("value1_16bit: %d, value2_16bit: %d, read_value_low16: %d\n"%(value1_16bit, value2_16bit, read_value))
        if ((value1_16bit & value2_16bit) == read_value):
            return logpass()
        else:
            return logfail()
    
    def tc013_alu_orr_test(self):
        value1_16bit = 0xa
        value2_16bit = 0x0
        self.chip.ulp.init()
        self.chip.ulp.movi(ULP_PARAM['R0'].value, 0)
        self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
        self.chip.ulp.movi(ULP_PARAM['R2'].value, value2_16bit)
        self.chip.ulp.orr(ULP_PARAM['R3'].value, ULP_PARAM['R1'].value, ULP_PARAM['R2'].value)
        self.chip.ulp.stm(ULP_PARAM['R3'].value, ULP_PARAM['R0'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.end()
        self.chip.ulp.start(0)
        time.sleep(0.05)
        read_value = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
        loginfo("value1_16bit: %d, value2_16bit: %d, read_value_low16: %d\n"%(value1_16bit, value2_16bit, read_value))
        if ((value1_16bit | value2_16bit) == read_value):
            return logpass()
        else:
            return logfail()
    
    def tc014_alu_lshr_test(self):
        value1_16bit = 0xa
        shift = 1
        self.chip.ulp.init()
        self.chip.ulp.movi(ULP_PARAM['R0'].value, 0)
        self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
        self.chip.ulp.movi(ULP_PARAM['R2'].value, shift)
        self.chip.ulp.lshr(ULP_PARAM['R3'].value, ULP_PARAM['R1'].value, ULP_PARAM['R2'].value)
        self.chip.ulp.stm(ULP_PARAM['R3'].value, ULP_PARAM['R0'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.end()
        self.chip.ulp.start(0)
        time.sleep(0.05)
        read_value_low16 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
        loginfo("value1_16bit: %d, shift: %d, read_value_low16: %d\n"%(value1_16bit, shift, read_value_low16))
        if ((value1_16bit << shift) == read_value_low16):
            return logpass()
        else:
            return logfail()
    
    def tc015_alu_rshr_test(self):
        value1_16bit = 0xa
        shift = 1
        self.chip.ulp.init()
        self.chip.ulp.movi(ULP_PARAM['R0'].value, 0)
        self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
        self.chip.ulp.movi(ULP_PARAM['R2'].value, shift)
        self.chip.ulp.rshr(ULP_PARAM['R3'].value, ULP_PARAM['R1'].value, ULP_PARAM['R2'].value)
        self.chip.ulp.stm(ULP_PARAM['R3'].value, ULP_PARAM['R0'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.end()
        self.chip.ulp.start(0)
        time.sleep(0.05)
        read_value_low16 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
        loginfo("value1_16bit: %d, shift: %d, read_value_low16: %d\n"%(value1_16bit, shift, read_value_low16))
        if ((value1_16bit >> shift) == read_value_low16):
            return logpass()
        else:
            return logfail()
    
    def tc016_jump_blr_test(self):
        value1_16bit = 0x9
        value2_16bit = 0x5
        fail_num = 0
        value_list = [(0, 1), (1, 1), (2, 1)]
        for value, thres in value_list:
            self.chip.ulp.init()
            self.chip.ulp.movi(ULP_PARAM['R3'].value, 0)
            self.chip.ulp.movi(ULP_PARAM['R0'].value, value)
            self.chip.ulp.blr(thres, 4)
            self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
            self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R3'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.end()
            self.chip.ulp.movi(ULP_PARAM['R1'].value, value2_16bit)
            self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R3'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.end()
            self.chip.ulp.start(0)
            time.sleep(0.05)
            read_value = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
            if (value < thres) and (read_value != value2_16bit):
                fail_num += 1
                logerror("fail, when value: %d, thres: %d, read_value: %d\n"%(value, thres, read_value))
            elif (value >= thres) and (read_value != value1_16bit):
                fail_num += 1
                logerror("fail, when value: %d, thres: %d, read_value: %d \n"%(value, thres, read_value))
            else:
                logdebug("test pass when value: %d, thres: %d, read_value: %d\n"%(value, thres, read_value))
        if (0 != fail_num):
            return logfail()
        else:
            return logpass()
    
    def tc017_jump_bhr_test(self):
        value1_16bit = 0x9
        value2_16bit = 0x5
        fail_num = 0
        value_list = [(0, 1), (1, 1), (2, 1)]
        for value, thres in value_list:
            self.chip.ulp.init()
            self.chip.ulp.movi(ULP_PARAM['R3'].value, 0)
            self.chip.ulp.movi(ULP_PARAM['R0'].value, value)
            self.chip.ulp.bhr(thres, 4)
            self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
            self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R3'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.end()
            self.chip.ulp.movi(ULP_PARAM['R1'].value, value2_16bit)
            self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R3'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.end()
            self.chip.ulp.start(0)
            time.sleep(0.05)
            read_value = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
            if self.chipv == "ESP32":
                if (value >= thres) and (read_value != value2_16bit):
                    fail_num += 1
                    logerror("fail, when value: %d, thres: %d, read_value: %d \n"%(value, thres, read_value))
                elif (value < thres) and (read_value != value1_16bit):
                    fail_num += 1
                    logerror("fail, when value: %d, thres: %d, read_value: %d \n"%(value, thres, read_value))
                else:
                    logdebug("test pass when value: %d, thres: %d, read_value: %d\n"%(value, thres, read_value))
            else:
                if (value > thres) and (read_value != value2_16bit):
                    fail_num += 1
                    logerror("fail, when value: %d, thres: %d, read_value: %d \n"%(value, thres, read_value))
                elif (value <= thres) and (read_value != value1_16bit):
                    fail_num += 1
                    logerror("fail, when value: %d, thres: %d, read_value: %d \n"%(value, thres, read_value))
                else:
                    logdebug("test pass when value: %d, thres: %d, read_value: %d\n"%(value, thres, read_value))
        if (0 != fail_num):
            return logfail()
        else:
            return logpass()
    
    def tc018_jump_bls_test(self):
        value1_16bit = 0x9
        value2_16bit = 0x5
        fail_num = 0
        value_list = [(0, 1), (1, 1), (2, 1)]
        for value, thres in value_list:
            self.chip.ulp.init()
            self.chip.ulp.movi(ULP_PARAM['R2'].value, 0)
            self.chip.ulp.rsts()
            self.chip.ulp.adds(value)
            self.chip.ulp.bls(thres, 4)
            self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
            self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R2'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.end()
            self.chip.ulp.movi(ULP_PARAM['R1'].value, value2_16bit)
            self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R2'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.end()
            self.chip.ulp.start(0)
            time.sleep(0.05)
            read_value = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
            if (value < thres) and (read_value != value2_16bit):
                fail_num += 1
                logerror("fail, when value: %d, thres: %d, read_value: %d \n"%(value, thres, read_value))
            elif (value >= thres) and (read_value != value1_16bit):
                fail_num += 1
                logerror("fail, when value: %d, thres: %d, read_value: %d \n"%(value, thres, read_value))
            else:
                logdebug("test pass when value: %d, thres: %d, read_value: %d\n"%(value, thres, read_value))
        if (0 != fail_num):
            return logfail()
        else:
            return logpass()
    
    def tc019_jump_bes_test(self):
        #in ESP32: test fail when value is less than thres, i.g: imm_value = 0, thres = 1
        value1_16bit = 0x9
        value2_16bit = 0x5
        fail_num = 0
        value_list = [(0, 1), (1, 1), (2, 1)]
        for value, thres in value_list:
            self.chip.ulp.init()
            self.chip.ulp.movi(ULP_PARAM['R2'].value, 0)
            self.chip.ulp.rsts()
            self.chip.ulp.adds(value)
            self.chip.ulp.bes(thres, 4)
            self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
            self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R2'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.end()
            self.chip.ulp.movi(ULP_PARAM['R1'].value, value2_16bit)
            self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R2'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.end()
            self.chip.ulp.start(0)
            time.sleep(0.05)
            read_value = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
            if (value == thres) and (read_value != value2_16bit):
                fail_num += 1
                logerror("fail, when value: %d, thres: %d, read_value: %d \n"%(value, thres, read_value))
            elif ((value != thres) and (read_value != value1_16bit)):
                fail_num += 1
                logerror("fail, when value: %d, thres: %d, read_value: %d \n"%(value, thres, read_value))
            else:
                logdebug("test pass when value: %d, thres: %d, read_value: %d\n"%(value, thres, read_value))
        if (0 != fail_num):
            return logfail()
        else:
            return logpass()
    
    def tc020_jump_bhs_test(self):
        #in ESP32: test fail when inn_value is equal with thres, i.g: imm_value = 1, thres = 1
        value1_16bit = 0x9
        value2_16bit = 0x5
        fail_num = 0
        value_list = [(0, 1), (1, 1), (2, 1)]
        for value, thres in value_list:
            self.chip.ulp.init()
            self.chip.ulp.movi(ULP_PARAM['R2'].value, 0)
            self.chip.ulp.rsts()
            self.chip.ulp.adds(value)
            self.chip.ulp.bhs(thres, 4)
            self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
            self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R2'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.end()
            self.chip.ulp.movi(ULP_PARAM['R1'].value, value2_16bit)
            self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R2'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.end()
            self.chip.ulp.start(0)
            time.sleep(0.05)
            read_value = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
            if (value > thres) and (read_value != value2_16bit):
                fail_num += 1
                logerror("fail, when value: %d, thres: %d, read_value: %d \n"%(value, thres, read_value))
            elif ((value <= thres) and (read_value != value1_16bit)):
                fail_num += 1
                logerror("fail, when value: %d, thres: %d, read_value: %d \n"%(value, thres, read_value))
            else:
                logdebug("test pass when value: %d, thres: %d, read_value: %d\n"%(value, thres, read_value))
        if (0 != fail_num):
            return logfail()
        else:
            return logpass()
    
    def tc021_jmpi_test(self):
        value1_16bit = 5
        value2_16bit = 6
        self.chip.ulp.init()
        self.chip.ulp.movi(ULP_PARAM['R2'].value, 0)
        self.chip.ulp.jmpi(5)
        self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
        self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R2'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.end()
        self.chip.ulp.movi(ULP_PARAM['R1'].value, value2_16bit)
        self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R2'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.end()
        self.chip.ulp.start(0)
        time.sleep(0.05)
        read_value = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
        loginfo("read_value_low16: %d\n"%(read_value))
        if (value2_16bit ==  read_value):
            return logpass()
        else:
            return logfail()
    
    def tc022_jmpr_test(self):
        value1_16bit = 8
        value2_16bit = 9
        self.chip.ulp.init()
        self.chip.ulp.movi(ULP_PARAM['R0'].value, 6)
        self.chip.ulp.movi(ULP_PARAM['R2'].value, 0)
        self.chip.ulp.jmpr(ULP_PARAM['R0'].value)
        self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
        self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R2'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.end()
        self.chip.ulp.movi(ULP_PARAM['R1'].value, value2_16bit)
        self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R2'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.end()
        self.chip.ulp.start(0)
        time.sleep(0.05)
        read_value = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
        loginfo("read_value_low16: %d\n"%(read_value))
        if (value2_16bit ==  read_value):
            return logpass()
        else:
            return logfail()
    
    def tc023_jzi_test(self):
        value1_16bit = 5
        value2_16bit = 6
        fail_num = 0
        iszero_list = [0, 3]
        for value in iszero_list:
            self.chip.ulp.init()
            self.chip.ulp.movi(ULP_PARAM['R2'].value, 0)
            self.chip.ulp.movi(ULP_PARAM['R3'].value, value)
            self.chip.ulp.jzi(6)
            self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
            self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R2'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.end()
            self.chip.ulp.movi(ULP_PARAM['R1'].value, value2_16bit)
            self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R2'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.end()
            self.chip.ulp.start(0)
            time.sleep(0.05)
            read_value = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
            if (0 == value) and (value2_16bit !=  read_value):
                fail_num += 1
                logerror("fail, when value is 0, read_value: %d\n", read_value)
            elif (value) and (value1_16bit !=  read_value):
                fail_num += 1
                logerror("fail, when value is not equal 0, read_value: %d\n", read_value)
            else:
                logdebug("test pass when value: %d, read_value: %d\n"%(value, read_value))
        if (0 != fail_num):
            return logfail()
        else:
            return logpass()
        
    def tc024_jzr_test(self):
        value1_16bit = 5
        value2_16bit = 6
        fail_num = 0
        iszero_list = [0, 3]
        for value in iszero_list:
            self.chip.ulp.init()
            self.chip.ulp.movi(ULP_PARAM['R0'].value, 7)
            self.chip.ulp.movi(ULP_PARAM['R2'].value, 0)
            self.chip.ulp.movi(ULP_PARAM['R3'].value, value)
            self.chip.ulp.jzr(ULP_PARAM['R0'].value)
            self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
            self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R2'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.end()
            self.chip.ulp.movi(ULP_PARAM['R1'].value, value2_16bit)
            self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R2'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.end()
            self.chip.ulp.start(0)
            time.sleep(0.05)
            read_value = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
            if (0 == value) and (value2_16bit !=  read_value):
                fail_num += 1
                logerror("fail, when value is 0, read_value: %d\n", read_value)
            elif (value) and (value1_16bit !=  read_value):
                fail_num += 1
                logerror("fail, when value is not equal 0, read_value: %d\n", read_value)
            else:
                loginfo("test pass when value: %d, read_value: %d\n"%(value, read_value))
        if (0 != fail_num):
            return logfail()
        else:
            return logpass()
    
    def tc025_joi_test(self):
        value1_16bit = 5
        value2_16bit = 6
        fail_num = 0
        iszero_list = [0, 3]
        for value in iszero_list:
            self.chip.ulp.init()
            self.chip.ulp.movi(ULP_PARAM['R2'].value, 0)
            self.chip.ulp.movi(ULP_PARAM['R3'].value, 0xffff)
            self.chip.ulp.addi(ULP_PARAM['R3'].value, ULP_PARAM['R3'].value, value)
            self.chip.ulp.joi(7)
            self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
            self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R2'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.end()
            self.chip.ulp.movi(ULP_PARAM['R1'].value, value2_16bit)
            self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R2'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.end()
            self.chip.ulp.start(0)
            time.sleep(0.05)
            read_value = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
            if (value) and (value2_16bit !=  read_value):
                fail_num += 1
                logerror("fail, when value is not equal 0, read_value: %d\n", read_value)
            elif (0 == value) and (value1_16bit !=  read_value):
                fail_num += 1
                logerror("fail, when value is 0, read_value: %d\n", read_value)
            else:
                loginfo("test pass when value: %d, read_value: %d\n"%(value, read_value))
        if (0 != fail_num):
            return logfail()
        else:
            return logpass()
    
    def tc026_jor_test(self):
        value1_16bit = 5
        value2_16bit = 6
        fail_num = 0
        iszero_list = [0, 3]
        for value in iszero_list:
            self.chip.ulp.init()
            self.chip.ulp.movi(ULP_PARAM['R0'].value, 8)
            self.chip.ulp.movi(ULP_PARAM['R2'].value, 0)
            self.chip.ulp.movi(ULP_PARAM['R3'].value, 0xffff)
            self.chip.ulp.addi(ULP_PARAM['R3'].value, ULP_PARAM['R3'].value, value)
            self.chip.ulp.jor(ULP_PARAM['R0'].value)
            self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
            self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R2'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.end()
            self.chip.ulp.movi(ULP_PARAM['R1'].value, value2_16bit)
            self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R2'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.end()
            self.chip.ulp.start(0)
            time.sleep(0.05)
            read_value = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
            if (value) and (value2_16bit !=  read_value):
                fail_num += 1
                logerror("fail, when value is not equal 0, read_value: %d\n", read_value)
            elif (0 == value) and (value1_16bit !=  read_value):
                fail_num += 1
                logerror("fail, when value is 0, read_value: %d\n", read_value)
            else:
                loginfo("test pass when value: %d, read_value: %d\n"%(value, read_value))
        if (0 != fail_num):
            return logfail()
        else:
            return logpass()
    
    def tc027_ldm_test(self):
        value1 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value)
        add_value = 0xa
        self.chip.ulp.init()
        self.chip.ulp.movi(ULP_PARAM['R0'].value, 0)
        self.chip.ulp.ldm(ULP_PARAM['R1'].value, ULP_PARAM['R0'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.addi(ULP_PARAM['R2'].value, ULP_PARAM['R1'].value, add_value)
        self.chip.ulp.stm(ULP_PARAM['R2'].value, ULP_PARAM['R0'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.end()
        self.chip.ulp.start(0)
        time.sleep(0.05)
        value2 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value)
        loginfo("value1: 0x%x, add_value: 0x%x, read_value2: 0x%x\n"%(value1, add_value, value2))
        if ((value1 & 0xffff) + add_value == (value2 & 0xffff)):
            return logpass()
        else:
            return logfail()

    def tc028_adc1_test(self):
        '''
        adc1 channel should connect to high(3.3v).
        '''
        adc1_channel = 6
        self.chip.rtc_adc1.config()
        self.chip.rtc_adc1.set(pad = adc1_channel, ulp = True)
        self.chip.ulp.init()
        self.chip.ulp.movi(ULP_PARAM['R0'].value, 0)
        if self.chipv == "ESP32":
            self.chip.ulp.meas_adc0(ULP_PARAM['R1'].value, adc1_channel + 1)
        else:
            self.chip.ulp.meas_adc0(ULP_PARAM['R1'].value, adc1_channel)
        self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R0'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.end()
        self.chip.ulp.start(0)
        time.sleep(0.001)
        read_value_low16 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
        if (0xfff != read_value_low16):
            logdebug("read_value_low16: 0x%x"%(read_value_low16))
            return logfail()
        else:
            return logpass()

    def tc029_adc2_test(self):
        '''
        adc2 channel should connect to high(3.3v).
        '''
        adc2_channel = 6
        self.chip.rtc_adc2.config()
        self.chip.rtc_adc2.set(pad = adc2_channel, ulp = True)
        if self.chipv != "ESP32":
            self.chip.adc2_arb.rtc_force()
        self.chip.ulp.init()
        self.chip.ulp.movi(ULP_PARAM['R0'].value, 0)
        if self.chipv == "ESP32":
            self.chip.ulp.meas_adc1(ULP_PARAM['R1'].value, adc2_channel + 1)
        else:
            self.chip.ulp.meas_adc1(ULP_PARAM['R1'].value, adc2_channel)
        self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R0'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.movi(ULP_PARAM['R2'].value, 1)
        self.chip.ulp.movi(ULP_PARAM['R3'].value, 0xaabb)
        self.chip.ulp.stm(ULP_PARAM['R3'].value, ULP_PARAM['R2'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.end()
        self.chip.ulp.start(0)
        time.sleep(2)
        read_value_low16 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
        if self.chipv == "CHIP723":
            if (0x1fff != read_value_low16):
                logerror("read_value_low16: 0x%x"%(read_value_low16))
                return logfail()
        else:
            if (0xfff != read_value_low16):
                logdebug("read_value_low16: 0x%x"%(read_value_low16))
                return logfail()
        return logpass()

    def tc030_tsen_test(self):
        if self.chipv == "CHIP722":
            tsen_ctrl2_addr = self.chip.HWREG.SARADC.SAR_TSENS_CTRL2._SAR_TSENS_CTRL2__addr
            tsen_reset_lsb = self.chip.HWREG.SARADC.SAR_TSENS_CTRL2._SAR_TSENS_CTRL2__reg_tsens_reset_lsb
            tsen_reset_msb = self.chip.HWREG.SARADC.SAR_TSENS_CTRL2._SAR_TSENS_CTRL2__reg_tsens_reset_msb
        self.chip.tsen.config(ulp = 1)
        self.chip.ulp.init()
        i = 0
        while(1):
            self.chip.ulp.movi(ULP_PARAM['R0'].value, 0)
            self.chip.ulp.tsens(ULP_PARAM['R1'].value, 100)
            self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R0'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            if self.chipv == "CHIP722":
                self.chip.ulp.str(tsen_ctrl2_addr, tsen_reset_msb, tsen_reset_lsb, 1)
                self.chip.ulp.str(tsen_ctrl2_addr, tsen_reset_msb, tsen_reset_lsb, 0)
            self.chip.ulp.end()
            self.chip.ulp.start(0)
            time.sleep(0.2)
            read_value_low16 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
            loginfo("tmp[%d]: 0x%x\n"%(i, read_value_low16))
            i += 1

    def tc030_2_tsen_test(self): #valid from CHIP722
        if self.chipv == "CHIP722":
            tsen_ctrl2_addr = self.chip.HWREG.SARADC.SAR_TSENS_CTRL2._SAR_TSENS_CTRL2__addr
            tsen_reset_lsb = self.chip.HWREG.SARADC.SAR_TSENS_CTRL2._SAR_TSENS_CTRL2__reg_tsens_reset_lsb
            tsen_reset_msb = self.chip.HWREG.SARADC.SAR_TSENS_CTRL2._SAR_TSENS_CTRL2__reg_tsens_reset_msb
        rtc_ctrl_addr = self.chip.HWREG.RTC_CNTL.RTC_STATE0._RTC_STATE0__addr
        rtc_sw_cpu_int_lsb = self.chip.HWREG.RTC_CNTL.RTC_STATE0._RTC_STATE0__rtc_sw_cpu_int_lsb
        rtc_sw_cpu_int_msb = self.chip.HWREG.RTC_CNTL.RTC_STATE0._RTC_STATE0__rtc_sw_cpu_int_msb
        self.chip.tsen.config(ulp = 1)
        self.chip.ulp.init()
        self.chip.ulp.tsens(ULP_PARAM['R1'].value, 1000)
        self.chip.ulp.str(rtc_ctrl_addr, rtc_sw_cpu_int_msb, rtc_sw_cpu_int_lsb, 1)
        self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R0'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        if self.chipv == "CHIP722":
            self.chip.ulp.str(tsen_ctrl2_addr, tsen_reset_msb, tsen_reset_lsb, 1)
            self.chip.ulp.str(tsen_ctrl2_addr, tsen_reset_msb, tsen_reset_lsb, 0)
        self.chip.ulp.end()
        self.chip.ulp.start(1)
        i = 0
        while(1):
            time.sleep(0.05)
            if (int(self.chip.HWREG.RTC_CNTL.INT_RAW_RTC.rtc_cocpu_int_raw)):
                read_value_low16 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
                loginfo("tmp[%d]: 0x%x\n"%(i, read_value_low16))
                self.chip.HWREG.RTC_CNTL.INT_CLR_RTC.rtc_cocpu_int_clr = 1
                i += 1

    def tc031_sleep_time_test(self, sleep_time_us, wait_cycle):
        self.chip.rtc_debug.TOUCH_PAD1(0, 11, 0)
        rtc_gpio_no = 6
        rtc_gpio_out_w1ts = self.chip.HWREG.RTC_IO.RTC_GPIO_OUT_W1TS._RTC_GPIO_OUT_W1TS__addr
        rtc_gpio_out_data_w1ts_lsb = self.chip.HWREG.RTC_IO.RTC_GPIO_OUT_W1TS._RTC_GPIO_OUT_W1TS__rtc_gpio_out_data_w1ts_lsb + rtc_gpio_no
        rtc_gpio_out_data_w1ts_msb = self.chip.HWREG.RTC_IO.RTC_GPIO_OUT_W1TS._RTC_GPIO_OUT_W1TS__rtc_gpio_out_data_w1ts_lsb + rtc_gpio_no
        rtc_gpio_out_w1tc = self.chip.HWREG.RTC_IO.RTC_GPIO_OUT_W1TC._RTC_GPIO_OUT_W1TC__addr
        rtc_gpio_out_data_w1tc_lsb = self.chip.HWREG.RTC_IO.RTC_GPIO_OUT_W1TC._RTC_GPIO_OUT_W1TC__rtc_gpio_out_data_w1tc_lsb + rtc_gpio_no
        rtc_gpio_out_data_w1tc_msb = self.chip.HWREG.RTC_IO.RTC_GPIO_OUT_W1TC._RTC_GPIO_OUT_W1TC__rtc_gpio_out_data_w1tc_lsb + rtc_gpio_no
        if self.chipv == "ESP32":
            rtc_timer2_addr = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__addr
            touch_start_wait_lsb = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__reg_sar_touch_start_wait_lsb
            touch_start_wait_msb = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__reg_sar_touch_start_wait_msb
        else:
            rtc_timer2_addr = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__addr
            touch_start_wait_lsb = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__reg_ulpcp_touch_start_wait_lsb
            touch_start_wait_msb = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__reg_ulpcp_touch_start_wait_msb
        period = int(self.chip.rtc_clk.get_clk_calibration(0))
        cycle_str = self.chip.rtc_clk.conv_us_to_slowclk(sleep_time_us, period)
        cycle_list = cycle_str.split(',')
        low_slp = int(cycle_list[0])
        high_slp = int(cycle_list[1])
        loginfo("low_slp: %d, high_slp: %d\n"%(low_slp, high_slp))
        self.chip.gpio.rtc_gpio_out(6, 0)
        self.chip.MEM.wrm(rtc_timer2_addr, touch_start_wait_msb, touch_start_wait_lsb, wait_cycle)#default_value 16
        self.chip.ulp.init()
        self.chip.ulp.str(rtc_gpio_out_w1ts, rtc_gpio_out_data_w1ts_msb, rtc_gpio_out_data_w1ts_lsb, 1)#rtc_gpio_out(rtc_gpio_no, 1)
        self.chip.ulp.str(rtc_gpio_out_w1tc, rtc_gpio_out_data_w1tc_msb, rtc_gpio_out_data_w1tc_lsb, 1)#rtc_gpio_out(rtc_gpio_no, 0)
        self.chip.ulp.set_ulp_slp_time(low_slp)
        self.chip.ulp.end()
        self.chip.ulp.start(1)
        time.sleep(1)
        self.chip.rtc_sleep.sleep(1, 0, 0, 0)

    def tc032_ldmu_test(self):
        if self.chipv != "ESP32":
            value1 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value)
            add_value = 0xa
            self.chip.ulp.init()
            self.chip.ulp.movi(ULP_PARAM['R0'].value, 0)
            self.chip.ulp.ldmu(ULP_PARAM['R1'].value, ULP_PARAM['R0'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.addi(ULP_PARAM['R2'].value, ULP_PARAM['R1'].value, add_value)
            self.chip.ulp.stm(ULP_PARAM['R2'].value, ULP_PARAM['R0'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.end()
            self.chip.ulp.start(0)
            time.sleep(0.05)
            value2 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value)
            loginfo("value1: 0x%x, add_value: 0x%x, read_value2: 0x%x\n"%(value1, add_value, value2))
            if ((value1 >> 16) + add_value == (value2 & 0xffff)):
                return logpass()
            else:
                return logfail()

    def tc033_jump_bles_test(self):
        if self.chipv != "ESP32":
            value1_16bit = 0x9
            value2_16bit = 0x5
            fail_num = 0
            value_list = [(0, 1), (1, 1), (2, 1)]
            for value, thres in value_list:
                self.chip.ulp.init()
                self.chip.ulp.movi(ULP_PARAM['R2'].value, 0)
                self.chip.ulp.rsts()
                self.chip.ulp.adds(value)
                self.chip.ulp.bles(thres, 4)
                self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
                self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R2'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
                self.chip.ulp.end()
                self.chip.ulp.movi(ULP_PARAM['R1'].value, value2_16bit)
                self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R2'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
                self.chip.ulp.end()
                self.chip.ulp.start(0)
                time.sleep(0.05)
                read_value = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
                if (value <= thres) and (read_value != value2_16bit):
                    fail_num += 1
                    logerror("fail, when value: %d, thres: %d, read_value: %d \n"%(value, thres, read_value))
                elif (value > thres) and (read_value != value1_16bit):
                    fail_num += 1
                    logerror("fail, when value: %d, thres: %d, read_value: %d \n"%(value, thres, read_value))
                else:
                    logdebug("test pass when value: %d, thres: %d, read_value: %d\n"%(value, thres, read_value))
            if (0 != fail_num):
                return logfail()
            else:
                return logpass()

    def tc034_jump_bhes_test(self):
        if self.chipv != "ESP32":
            value1_16bit = 0x9
            value2_16bit = 0x5
            fail_num = 0
            value_list = [(0, 1), (1, 1), (2, 1)]
            for value, thres in value_list:
                self.chip.ulp.init()
                self.chip.ulp.movi(ULP_PARAM['R2'].value, 0)
                self.chip.ulp.rsts()
                self.chip.ulp.adds(value)
                self.chip.ulp.bhes(thres, 4)
                self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
                self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R2'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
                self.chip.ulp.end()
                self.chip.ulp.movi(ULP_PARAM['R1'].value, value2_16bit)
                self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R2'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
                self.chip.ulp.end()
                self.chip.ulp.start(0)
                time.sleep(0.05)
                read_value = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
                if (value >= thres) and (read_value != value2_16bit):
                    fail_num += 1
                    logerror("fail, when value: %d, thres: %d, read_value: %d \n"%(value, thres, read_value))
                elif (value < thres) and (read_value != value1_16bit):
                    fail_num += 1
                    logerror("fail, when value: %d, thres: %d, read_value: %d \n"%(value, thres, read_value))
                else:
                    logdebug("test pass when value: %d, thres: %d, read_value: %d\n"%(value, thres, read_value))
            if (0 != fail_num):
                return logfail()
            else:
                return logpass()

    def tc035_jump_ber_test(self):
        if self.chipv != "ESP32":
            value1_16bit = 0x9
            value2_16bit = 0x5
            fail_num = 0
            value_list = [(0, 1), (1, 1), (2, 1)]
            for value, thres in value_list:
                self.chip.ulp.init()
                self.chip.ulp.movi(ULP_PARAM['R3'].value, 0)
                self.chip.ulp.movi(ULP_PARAM['R0'].value, value)
                self.chip.ulp.ber(thres, 4)
                self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
                self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R3'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
                self.chip.ulp.end()
                self.chip.ulp.movi(ULP_PARAM['R1'].value, value2_16bit)
                self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R3'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
                self.chip.ulp.end()
                self.chip.ulp.start(0)
                time.sleep(0.05)
                read_value = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
                if (value == thres) and (read_value != value2_16bit):
                    fail_num += 1
                    logerror("fail, when value: %d, thres: %d, read_value: %d\n"%(value, thres, read_value))
                elif ((value > thres) or (value < thres)) and (read_value != value1_16bit):
                    fail_num += 1
                    logerror("fail, when value: %d, thres: %d, read_value: %d \n"%(value, thres, read_value))
                else:
                    logdebug("test pass when value: %d, thres: %d, read_value: %d\n"%(value, thres, read_value))
            if (0 != fail_num):
                return logfail()
            else:
                return logpass()

    def tc036_stw_test(self):
        if self.chipv != "ESP32":
            data_offset = ULP_PARAM['RTC_MEM_DATA_OFFSET'].value
            value1_16bit = 0xaa
            value2_16bit = 0xbb
            self.chip.ulp.init()
            self.chip.ulp.set_offset(data_offset)
            self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
            self.chip.ulp.movi(ULP_PARAM['R3'].value, 0)
            self.chip.ulp.stw(ULP_PARAM['R3'].value, ULP_PARAM['R1'].value)
            self.chip.ulp.movi(ULP_PARAM['R1'].value, value2_16bit)
            self.chip.ulp.stw(ULP_PARAM['R3'].value, ULP_PARAM['R1'].value)
            self.chip.ulp.end()
            self.chip.ulp.start(0)
            time.sleep(0.05)
            read_value1 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
            read_value2 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value + 4) & 0xffff
            if (value1_16bit == read_value1) and (value2_16bit == read_value2):
                return logpass()
            else:
                return logfail()

    def tc037_stc_test(self):
        if self.chipv != "ESP32":
            data_offset = ULP_PARAM['RTC_MEM_DATA_OFFSET'].value
            value1_16bit = 0xaa
            value2_16bit = 0xbb
            self.chip.ulp.init()
            self.chip.ulp.set_offset(data_offset)
            self.chip.ulp.movi(ULP_PARAM['R1'].value, value1_16bit)
            self.chip.ulp.movi(ULP_PARAM['R3'].value, 0)
            self.chip.ulp.stc(ULP_PARAM['R3'].value, ULP_PARAM['R1'].value)
            self.chip.ulp.movi(ULP_PARAM['R1'].value, value2_16bit)
            self.chip.ulp.stc(ULP_PARAM['R3'].value, ULP_PARAM['R1'].value)
            self.chip.ulp.end()
            self.chip.ulp.start(0)
            time.sleep(0.05)
            read_value1 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
            read_value2 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) >> 16
            if (value1_16bit == read_value1) and (value2_16bit == read_value2):
                return logpass()
            else:
                return logfail()

    def tc038_stm32l_test(self):
        if self.chipv != "ESP32":
            store_value_16bit = 0xaaaa
            self.chip.ulp.init()
            self.chip.ulp.movi(ULP_PARAM['R1'].value, store_value_16bit)
            self.chip.ulp.movi(ULP_PARAM['R3'].value, 0)
            self.chip.ulp.stm32l(ULP_PARAM['R1'].value, ULP_PARAM['R3'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.end()
            self.chip.ulp.start(0)
            time.sleep(0.05)
            read_value = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value)
            loginfo("store_value: 0x%x, read_value: 0x%x\n"%(store_value_16bit, read_value))
            if ((read_value & 0xffff) == store_value_16bit):
                return logpass()
            else:
                return logfail()

    def tc039_stm32u_test(self):
        if self.chipv != "ESP32":
            store_value_16bit = 0xbbbb
            self.chip.ulp.init()
            self.chip.ulp.movi(ULP_PARAM['R1'].value, store_value_16bit)
            self.chip.ulp.movi(ULP_PARAM['R3'].value, 0)
            self.chip.ulp.stm32u(ULP_PARAM['R1'].value, ULP_PARAM['R3'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.end()
            self.chip.ulp.start(0)
            time.sleep(0.05)
            read_value = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value)
            loginfo("store_value: 0x%x, read_value: 0x%x\n"%(store_value_16bit, read_value))
            if ((read_value >> 16) == store_value_16bit):
                return logpass()
            else:
                return logfail()

    def tc040_stmlbl_test(self):
        if self.chipv != "ESP32":
            set_label = 3
            set_value = 0xaabb
            self.chip.ulp.init()
            self.chip.ulp.movi(ULP_PARAM['R1'].value, set_value)
            self.chip.ulp.movi(ULP_PARAM['R3'].value, 0)
            self.chip.ulp.stmlbl(set_label, ULP_PARAM['R1'].value, ULP_PARAM['R3'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.end()
            self.chip.ulp.start(0)
            time.sleep(0.05)
            read_value_16bit = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
            read_label = read_value_16bit >> 14
            read_value_14bit = read_value_16bit & 0x3fff
            loginfo("set_label: 0x%x, set_value&0x3fff: 0x%x"%(set_label, set_value & 0x3fff))
            loginfo("read_value_16bit: 0x%x, read_label: 0x%x, read_value_14bit: 0x%x\n"%(read_value_16bit, read_label, read_value_14bit))
            if ((set_label & 0x3) == read_label) and ((set_value & 0x3fff) == read_value_14bit):
                return logpass()
            else:
                return logfail()

    def tc041_stmlbu_test(self):
        if self.chipv != "ESP32":
            set_label = 3
            set_value = 0xabcd
            self.chip.ulp.init()
            self.chip.ulp.movi(ULP_PARAM['R1'].value, set_value)
            self.chip.ulp.movi(ULP_PARAM['R3'].value, 0)
            self.chip.ulp.stmlbu(set_label, ULP_PARAM['R1'].value, ULP_PARAM['R3'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.end()
            self.chip.ulp.start(0)
            time.sleep(0.05)
            read_value_32bit = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value)
            read_label = read_value_32bit >> 30
            read_value = (read_value_32bit >> 16) & 0x3fff
            loginfo("read_label: 0x%x, read_value: 0x%x\n"%(read_label, read_value))
            if ((set_label & 0x3) == read_label) and ((set_value & 0x3fff) == read_value):
                return logpass()
            else:
                return logfail()

    def tc042_start_byGpio_in_active_test(self, rtc_in_no):
        '''
        rtc_in_no should connected to low, then connected to high
        '''
        store_value_16bit = 0xaabb
        self.chip.ulp.init()
        self.chip.ulp.movi(ULP_PARAM['R1'].value, store_value_16bit)
        self.chip.ulp.movi(ULP_PARAM['R3'].value, 0)
        self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R3'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.end()
        self.chip.gpio.rtc_gpio_wakeup_enable(rtc_in_no, 5)
        self.chip.gpio.rtc_gpio_in(rtc_in_no)
        self.chip.ulp.start(2)
        time.sleep(0.05)
        value1 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
        loginfo("value1: 0x%x"%(value1))
        time.sleep(3)#rtc_gpio0 connected to high
        value2 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
        loginfo("value2: 0x%x"%(value2))
        if (store_value_16bit != value1) and (store_value_16bit == value2):
            return logpass()
        else:
            return logfail()

    def tc043_start_byGpio_in_sleep_test(self, rtc_in_no):
        '''
        rtc_in_no should connected to low, then connected to high
        '''
        store_value_16bit = 0xccdd
        self.chip.ulp.init()
        self.chip.ulp.movi(ULP_PARAM['R1'].value, store_value_16bit)
        self.chip.ulp.movi(ULP_PARAM['R3'].value, 0)
        self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R3'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.end()
        self.chip.gpio.rtc_gpio_wakeup_enable(rtc_in_no, 5)
        self.chip.gpio.rtc_gpio_in(rtc_in_no)
        self.chip.ulp.start(2)
        time.sleep(0.05)
        value1 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
        self.chip.rtc_sleep.rtc_timer_wakeup(0, 0x50000)
        loginfo("goto sleep")
        self.chip.rtc_sleep.sleep(0x61, 8, 0)#rtc_gpio0 connected to high
        loginfo("wakeup")
        time.sleep(0.5)
        value2 = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
        loginfo("value1: 0x%x, value2: 0x%x"%(value1, value2))
        if (store_value_16bit != value1) and (store_value_16bit == value2):
            return logpass()
        else:
            return logfail()
