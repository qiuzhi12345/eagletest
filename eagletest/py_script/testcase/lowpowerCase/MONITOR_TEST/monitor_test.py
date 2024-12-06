from baselib.loglib.log_lib import *
from hal.Init import HALS
from rtclib.rtc import ULP_PARAM
from rtclib.rtc import WAKEUP_ENABLE
from rtclib.rtc import WAKEUP_REASON
from rtclib.rtc import RESET_CAUSE
from baselib.instrument.dm import dm
from baselib.instrument.awg import awg
from rtclib.rtc import ADC_LIB
from rtclib.rtc import TSEN_LIB


class MONITOR(object):
    def __init__(self, channel, chipv = "AUTO"):
        self.chip = HALS(channel, chipv)
        self.channel = self.chip.channel
        self.chipv = self.chip.chipv
        self.monitor_data_path = '/home/lab/job/{}/lowpower_test/monitor/'.format(self.chipv)
        self.awg1 = awg(num_of_machine = 0)
        #self.awg2 = awg(num_of_machine = 1)
        #self.dm1 = dm(num_of_machine = 0)
        self.dm2 = dm(num_of_machine = 0)
        self.adc_lib = ADC_LIB(channel)
        self.tsen_lib = TSEN_LIB(channel)

    def ulp_loop_run(self):
        self.chip.ulp.init()
        self.chip.ulp.movi(ULP_PARAM['R0'].value, 0)
        self.chip.ulp.blr(5, 0x81)
        self.chip.ulp.end()
        self.chip.ulp.start(1)

    def ulp_loop_run_adc(self, adc1_channel, times = 5000, slp_cycle = 5000):
        '''
        times: 1000, slp_cycle: 1000, slp & work time equal to 12ms;
        times: 5000, slp_cycle: 6000, slp & work time equal to 65ms;
        '''
        self.chip.rtc_adc1.config()
        self.chip.rtc_adc1.set(pad = adc1_channel, ulp = True)
        self.chip.ulp.init()
        self.chip.ulp.set_ulp_slp_time(slp_cycle)
        self.chip.ulp.movi(ULP_PARAM['R0'].value, 0)
        self.chip.ulp.meas_adc0(ULP_PARAM['R2'].value, adc1_channel)
        self.chip.ulp.addi(ULP_PARAM['R0'].value, ULP_PARAM['R0'].value, 1)
        self.chip.ulp.blr(times, 0x82)
        self.chip.ulp.end()
        self.chip.ulp.start(1)

    def adc1_monitor_test(self, monitor_file, adc1_channel, times):
        num = [32, 128, 256, times, 0, times]
        k_num = [16, 64, 128, times / 2, 0, 0]
        adc_input_list = [0.5, 0.8]
        monitor_file.write("adc_input, ")
        monitor_file.write("%.1f,"%(adc_input_list[0]))
        monitor_file.write("%.1f,"%(adc_input_list[1]))
        monitor_file.write("\n")
        for atten in range(4):
            monitor_file.write("adc1_atten{},".format(atten))
            for i in range(len(adc_input_list)):
                self.awg2.appl("DC", 0, 0, adc_input_list[i])
                time.sleep(0.15)
                first_addr = self.adc_lib.adc1_deepsleep_read(adc1_channel, times, atten)
                self.chip.rtc_wdt.wdt_unlock()
                self.chip.rtc_wdt.wdt_stg_hold_len(0, 0xffff)
                self.chip.rtc_wdt.wdt_stg_act(0, 4)
                self.chip.rtc_wdt.wdt_init()
                time.sleep(2)
                reset_cause = int(self.chip.rtc.rtc_reset_cause())
                if (reset_cause == RESET_CAUSE['RTCWDT_RTC_RESET'].value):
                    self.chip.rtc_wdt.wdt_stop()
                else:
                    logerror("no reset")
                    exit(-1)
                for j in range(times):
                    Din = int(self.chip.MEM.rd(first_addr + j * 4) & 0xffff)
                    if not j:
                        Dout_f = Din
                    else:
                        if j < num[0]:
                            k = k_num[0]
                        elif j < num[1]:
                            k = k_num[1]
                        elif j < num[2]:
                            k = k_num[2]
                        elif j < num[3]:
                            k = k_num[3]
                        elif j < num[4]:
                            k = k_num[4]
                        else:
                            k = k_num[5]
                        Dout_f = (Din + (k - 1) * Dout_f) / k
                Dout_f = Dout_f + 0.5
                adc1_value = Dout_f
                monitor_file.write("%d,"%(adc1_value))
            monitor_file.write("\n")
        monitor_file.write("\n")

    def adc2_monitor_test(self, monitor_file, adc2_channel, times):
        num = [32, 128, 256, times, 0, times]
        k_num = [16, 64, 128, times / 2, 0, 0]
        adc_input_list = [0.5, 0.8]
        monitor_file.write("adc_input, ")
        monitor_file.write("%.1f,"%(adc_input_list[0]))
        monitor_file.write("%.1f,"%(adc_input_list[1]))
        monitor_file.write("\n")
        for atten in range(4):
            monitor_file.write("adc2_atten{},".format(atten))
            for i in range(len(adc_input_list)):
                self.awg2.appl("DC", 0, 0, adc_input_list[i])
                time.sleep(0.15)
                first_addr = self.adc_lib.adc2_deepsleep_read(adc2_channel, times, atten)
                self.chip.rtc_wdt.wdt_unlock()
                self.chip.rtc_wdt.wdt_stg_hold_len(0, 0xffff)
                self.chip.rtc_wdt.wdt_stg_act(0, 4)
                self.chip.rtc_wdt.wdt_init()
                time.sleep(2)
                reset_cause = int(self.chip.rtc.rtc_reset_cause())
                if (reset_cause == RESET_CAUSE['RTCWDT_RTC_RESET'].value):
                    self.chip.rtc_wdt.wdt_stop()
                else:
                    logerror("no reset")
                    exit(-1)
                for j in range(times):
                    Din = int(self.chip.MEM.rd(first_addr + j * 4) & 0xffff)
                    if not j:
                        Dout_f = Din
                    else:
                        if j < num[0]:
                            k = k_num[0]
                        elif j < num[1]:
                            k = k_num[1]
                        elif j < num[2]:
                            k = k_num[2]
                        elif j < num[3]:
                            k = k_num[3]
                        elif j < num[4]:
                            k = k_num[4]
                        else:
                            k = k_num[5]
                        Dout_f = (Din + (k - 1) * Dout_f) / k
                Dout_f = Dout_f + 0.5
                adc1_value = Dout_f
                monitor_file.write("%d,"%(adc1_value))
            monitor_file.write("\n")
        monitor_file.write("\n")

    def dac1_monitor_test(self, monitor_file, dac_times, reg_pd, dbg):
        #test dac1 when input is 100 and 200
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
        rtc_timer2_addr = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__addr
        touch_start_wait_lsb = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__reg_ulpcp_touch_start_wait_lsb
        touch_start_wait_msb = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__reg_ulpcp_touch_start_wait_msb
        lowpower_state_addr = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__addr
        lowpower_state_lsb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_lsb
        lowpower_state_msb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_msb
        dac_value_list = [100, 200]
        self.chip.MEM.wrm(rtc_timer2_addr, touch_start_wait_msb, touch_start_wait_lsb, 0x1ff)#default_value 16
        monitor_file.write("\n")
        monitor_file.write("dac_input, ")
        for i in range(len(dac_value_list)):
            input_value = dac_value_list[i]
            monitor_file.write("%d,"%(input_value))
        monitor_file.write("\n")
        self.chip.dac.dc_out(1, 10)
        monitor_file.write("dac_output,")
        for i in range(len(dac_value_list)):
            total_value = 0.0
            average_value = 0.0
            input_value = dac_value_list[i]
            self.chip.ulp.init()
            self.chip.ulp.ldr(lowpower_state_addr, lowpower_state_msb, lowpower_state_lsb)
            self.chip.ulp.blr(1, 6)
            self.chip.ulp.str(dac1_addr, dac1_xpd_msb, dac1_xpd_lsb, 1)
            self.chip.ulp.str(dac1_addr, dac1_xpd_force_msb, dac1_xpd_force_lsb, 1)
            self.chip.ulp.str(dac_ctrl2_addr, dac_cw_en1_msb, dac_cw_en1_lsb, 0)
            self.chip.ulp.str(dac1_addr, dac1_padc1_msb, dac1_pdac1_lsb,  input_value)
            self.chip.ulp.str(slp_timer_en_addr, slp_timer_en_msb, slp_timer_en_lsb, 0)
            self.chip.ulp.end()
            self.chip.ulp.start(1)
            self.chip.rtc_sleep.rtc_timer_wakeup(0, 4000000)
            self.chip.rtc_sleep.special_sleep(0x69, WAKEUP_ENABLE['TIMER_EXPIRE_EN'].value, 0)
            time.sleep(1)
            with open(self.monitor_data_path + 'dac_regpd{}_dbg{}_input{}.csv'.format(reg_pd, dbg, dac_value_list[i]), 'w') as dac_file:
                dac_file.write("input_{},".format(dac_value_list[i]))
                for i in range(dac_times):
                    output = float(self.dm1.get_result('VDC'))
                    dac_file.write("%.4f,"%(output))
                    total_value += float(output)
                dac_file.write("\n")
            average_value = float(total_value / dac_times)
            monitor_file.write("%.4f,"%(average_value))
            time.sleep(10)
            self.chip.rtc_wdt.wdt_unlock()
            self.chip.rtc_wdt.wdt_stg_hold_len(0, 0xffff)
            self.chip.rtc_wdt.wdt_stg_act(0, 4)
            self.chip.rtc_wdt.wdt_init()
            time.sleep(3)
            reset_cause = int(self.chip.rtc.rtc_reset_cause())
            if (reset_cause == RESET_CAUSE['RTCWDT_RTC_RESET'].value):
                self.chip.rtc_wdt.wdt_stop()
            else:
                logerror("no reset")
                return
        monitor_file.write("\n")

    def temp_monitor_test(self, monitor_file, times, reg_pd, dbg):
        #temperature test
        total_value = 0
        first_addr = self.tsen_lib.tsen_deepsleep_read(times)
        with open(self.monitor_data_path + 'tmp_regpd{}_dbg{}.csv'.format(reg_pd, dbg), 'w') as tmp_file:
            tmp_file.write("tmp_value:,")
            for i in range(times):
                tmp_value = int(self.chip.MEM.rd(first_addr + i * 4) & 0xffff)
                tmp_file.write("%d,"%(tmp_value))
                total_value += tmp_value
            average_value = total_value / times
            tmp_file.write("\n")
        monitor_file.write("%.1f,"%(average_value))
        monitor_file.write("\n")

    def current_ulprun_test(self, monitor_file, adc1_channel):
        #BIAS_SLEEP_FOLW_8M must be set to 0 to make bias sleep & dbg valid.
        monitor_file.write("\n")
        monitor_file.write("current when no sample(mA),")
        self.chip.gpio.rtc_gpio_hangup_all()
        self.chip.gpio.dig_gpio_hangup_all()
        self.ulp_loop_run()
        self.chip.rtc_sleep.rtc_timer_wakeup(0, 0x180000)
        self.chip.rtc_sleep.special_sleep(0x69, WAKEUP_ENABLE['TIMER_EXPIRE_EN'].value, 0)
        time.sleep(2)
        for i in range(10):
            current = float(self.dm2.get_result("IDC"))
            monitor_file.write("%.3f,"%(current * 1000))
        monitor_file.write("\n")
        time.sleep(5)
        print "chip must wakeup", self.dm2.get_result("IDC")

    def current_adccontinuoussample_test(self, monitor_file, adc1_channel):
        monitor_file.write("\n")
        monitor_file.write("current when adc1 sample(mA),")
        self.chip.gpio.rtc_gpio_hangup_all()
        self.chip.gpio.dig_gpio_hangup_all()
        self.ulp_loop_run_adc(adc1_channel)
        self.chip.rtc_sleep.special_sleep(0x69, 0, 0)
        time.sleep(2)
        self.dm2.start_rate()
        res = self.dm2.getcurve()
        for index, subres in enumerate(res):
            res[index] = float(subres*1000)
            monitor_file.write("%f,"%(res[index]))
        monitor_file.write("\n")

    def specialadc_monitor_test(self, adc1_channel, touch_start_value = 16, reg_pd = 1, dbg = 15):
        #Must set regulator_force_pd = 1, dbg = 15, RTC_CNTL_BIAS_SLEEP_FOLW_8M = 1
        rtc_timer2_addr = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__addr
        touch_start_wait_lsb = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__reg_ulpcp_touch_start_wait_lsb
        touch_start_wait_msb = self.chip.HWREG.RTC_CNTL.RTC_TIMER2._RTC_TIMER2__reg_ulpcp_touch_start_wait_msb
        lowpower_state_addr = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__addr
        lowpower_state_lsb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_lsb
        lowpower_state_msb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_msb
        with open(self.monitor_data_path + 'adc_regpd{}_dbg{}_touch_start_value{}.csv'.format(reg_pd, dbg, touch_start_value), 'w') as adc_file:
            meas_times = 500
            adc_file.write("\n")
            adc_file.write("value_beforetest: \n")
            for i in range(meas_times):
                value_beforetest = int(self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value + i * 4)) & 0xfff
                adc_file.write("%d, "%(value_beforetest))
            adc_file.write("\n")
            self.awg2.appl("DC", 0, 0, 0.5)
            time.sleep(0.15)
            self.chip.MEM.wrm(rtc_timer2_addr, touch_start_wait_msb, touch_start_wait_lsb, touch_start_value)#default_value 16
            self.chip.rtc_adc1.config()
            self.chip.rtc_adc1.set(pad = adc1_channel, ulp = True, atten = 1)
            self.chip.ulp.init()
            self.chip.ulp.ldr(lowpower_state_addr, lowpower_state_msb, lowpower_state_lsb)
            self.chip.ulp.blr(1, 5)
            self.chip.ulp.meas_adc0(ULP_PARAM['R2'].value, adc1_channel)
            self.chip.ulp.stm(ULP_PARAM['R2'].value, ULP_PARAM['R1'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.addi(ULP_PARAM['R1'].value, ULP_PARAM['R1'].value, 1)
            self.chip.ulp.jmpi(0)
            self.chip.ulp.end()
            self.chip.ulp.start(1)
            self.chip.rtc_sleep.rtc_timer_wakeup(0, 0x160000)
            self.chip.rtc_sleep.sleep(0x69, WAKEUP_ENABLE['TIMER_EXPIRE_EN'].value, 0)
            time.sleep(2)
            adc_file.write("touch_start_wait_set_{},".format(touch_start_value))
            for i in range(meas_times):
                adc_value = int(self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value + i * 4)) & 0xfff
                adc_file.write("%d, "%(adc_value))
            adc_file.write("\n")

    def param_confirm_test(self):
        lowpower_state_addr = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__addr
        lowpower_state_lsb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_lsb
        lowpower_state_msb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_msb
        delay_num = 500
        for test_no in range(100):
            self.awg1.appl("DC", 0, 0, 0)
            time.sleep(1)
            self.awg1.appl("DC", 0, 0, 3.3)
            time.sleep(1.5)
            if self.chipv == "CHIP722":
                self.chip.HWI2C.ulp.ir_force_xpd_vgate_buf = 1
                self.chip.HWI2C.ulp.ir_force_xpd_ref_out_buf = 1
            self.chip.power.ldo_debug(0, 0)
            self.chip.ulp.init()
            self.chip.ulp.ldr(lowpower_state_addr, lowpower_state_msb, lowpower_state_lsb)
            self.chip.ulp.blr(1, 2 + delay_num)
            for i in range(delay_num):
                self.chip.ulp.delay(0xffff)  #To make dbg effect
            self.chip.ulp.wakeup()
            self.chip.ulp.end()
            self.chip.ulp.start(1)
            time.sleep(1)
            loginfo("test_no: %d"%(test_no))
            self.chip.rtc_sleep.sleep(1, WAKEUP_ENABLE['SAR_TRIG_EN'].value, 0)

    def monitor_test(self, adc1_channel = 5, adc2_channel = 1, reg_pd = 0, dbg = 3, times = 1000, dac_times = 100, touch_start_value = 16):
        '''
        adc1_pad5 adc2_pad1 both connected to the same 33120A instrument
        only be used in CHIP722
        a) RTC_REGULATOR_PD = 1, DBG = 0;
        b) RTC_REGULATOR_PD = 1, DBG = 15;
        c) RTC_REGULATOR_PD = 0, DBG = 0;
        in condition above(modify opensource code), test total current, adc_vref, rtc_ldo, adc, dac, temperature, touch
        Note:
        1) when RTC_REGULATOR_PD = 1, we can't get adc_vref value(can't pull adc_vref to any pad), we can read adc_value for serval times;
        2) To make non-zero dbg value valid, we should set BIAS_SLEEP_FLOW_8M = 0.
        '''
        self.param_confirm_test()

        with open(self.monitor_data_path + 'REGPD{}_DBG{}_{}.csv'.format(reg_pd, dbg, time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())), 'w') as monitor_file:
            self.adc1_monitor_test(monitor_file, adc1_channel, times)
            self.adc2_monitor_test(monitor_file, adc2_channel, times)
            self.current_ulprun_test(monitor_file, adc1_channel)
            self.current_adccontinuoussample_test(monitor_file, adc1_channel)
            self.dac1_monitor_test(monitor_file, dac_times, reg_pd, dbg)
            self.temp_monitor_test(monitor_file, times, reg_pd, dbg)

        self.specialadc_monitor_test(adc1_channel, touch_start_value, reg_pd=1, dbg=15)#only for reg_force_pd=1, dbg=15, RTC_CNTL_BIAS_SLEEP_FOLW_8M = 1


    def monitor_test_CHIP723(self, adc1_channel = 5, adc2_channel = 1, times = 1000, dac_times = 100, touch_start_value = 16):
        regpd_dbg_list = [[0, 0], [1, 0], [0, 6], [1, 6], [1, 7]]
        for reg_pd, dbg in regpd_dbg_list:
            with open(self.monitor_data_path + 'REGPD{}_DBG{}_{}.csv'.format(reg_pd, dbg, time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())), 'w') as monitor_file:
                self.awg1.appl("DC", 0, 0, 0)
                time.sleep(1)
                self.awg1.appl("DC", 0, 0, 3.3)
                time.sleep(1.5)
                self.chip.channel.req_com("rtc_sleep_bias_init 0 0 0 0 0 %d"%(dbg))
                self.chip.HWREG.RTC_CNTL.RTC_REG.reg_rtc_regulator_force_pd = reg_pd
                self.adc1_monitor_test(monitor_file, adc1_channel, times, dbg)

                self.awg1.appl("DC", 0, 0, 0)
                time.sleep(1)
                self.awg1.appl("DC", 0, 0, 3.3)
                time.sleep(1.5)

                self.chip.HWREG.RTC_CNTL.RTC_REG.reg_rtc_regulator_force_pd = reg_pd
                self.adc2_monitor_test(monitor_file, adc2_channel, times, dbg)

                self.awg1.appl("DC", 0, 0, 0)
                time.sleep(1)
                self.awg1.appl("DC", 0, 0, 3.3)
                time.sleep(1.5)
                self.chip.HWREG.RTC_CNTL.RTC_REG.reg_rtc_regulator_force_pd = reg_pd
                self.channel.req_com("rtc_sleep_bias_init 1 1 1 1 0 %d"%(dbg))
                self.current_ulprun_test(monitor_file, adc1_channel)

                self.awg1.appl("DC", 0, 0, 0)
                time.sleep(1)
                self.awg1.appl("DC", 0, 0, 3.3)
                time.sleep(1.5)
                self.chip.HWREG.RTC_CNTL.RTC_REG.reg_rtc_regulator_force_pd = reg_pd
                self.channel.req_com("rtc_sleep_bias_init 1 1 1 1 0 %d"%(dbg))
                self.current_adccontinuoussample_test(monitor_file, adc1_channel)

                self.awg1.appl("DC", 0, 0, 0)
                time.sleep(1)
                self.awg1.appl("DC", 0, 0, 3.3)
                time.sleep(1.5)
                self.chip.HWREG.RTC_CNTL.RTC_REG.reg_rtc_regulator_force_pd = reg_pd
                self.channel.req_com("rtc_sleep_bias_init 1 1 1 1 0 %d"%(dbg))
                self.dac1_monitor_test(monitor_file, dac_times, reg_pd, dbg)

                self.awg1.appl("DC", 0, 0, 0)
                time.sleep(1)
                self.awg1.appl("DC", 0, 0, 3.3)
                time.sleep(1.5)
                self.chip.HWREG.RTC_CNTL.RTC_REG.reg_rtc_regulator_force_pd = reg_pd
                self.channel.req_com("rtc_sleep_bias_init 1 0 1 0 0 %d"%(dbg))
                self.temp_monitor_test(monitor_file, times, reg_pd, dbg)

        #self.specialadc_monitor_test(adc1_channel, touch_start_value, reg_pd=1, dbg=15)
