from baselib.loglib.log_lib import *
from hal.Init import HALS
from rtclib.rtc import ADC_LIB
from rtclib.rtc import RESET_CAUSE
from baselib.instrument.awg import awg


class ADC_TC_LOWPOWER(object):
    def __init__(self, channel, chipv = "AUTO"):
        self.chip = HALS(channel, chipv)
        self.chipv = self.chip.chipv
        self.adc_lib = ADC_LIB(self.chip.channel, self.chipv)
        self.adc_data_path = '/home/lab/job/{}/lowpower_test/adc/'.format(self.chipv)

    def adc1_2m_read(self, adc_file, adc1_channel, atten_value):
        self.chip.rtc_clk.set_cpu_freq(4)
        self.chip.rtc_adc1.config()
        self.chip.rtc_adc1.set(pad = adc1_channel, atten = atten_value)
        adc_file.write("2M,")
        for i in range(66):
            input_dc_value = (i + 1) * 0.05
            self.awg.appl("DC", 0, 0, input_dc_value)
            time.sleep(0.15)
            adc1_value = int(self.chip.rtc_adc1.read())
            adc_file.write("%d,"%(adc1_value))
        adc_file.write("\n")
        return

    def adc1_80m_read(self, adc_file, adc1_channel, atten_value):
        self.chip.rtc_clk.set_cpu_freq(1)
        self.chip.rtc_adc1.config()
        self.chip.rtc_adc1.set(pad = adc1_channel, atten = atten_value)
        adc_file.write("80M,")
        for i in range(66):
            input_dc_value = (i + 1) * 0.05
            self.awg.appl("DC", 0, 0, input_dc_value)
            time.sleep(0.15)
            adc1_value = int(self.chip.rtc_adc1.read())
            adc_file.write("%d,"%(adc1_value))
        adc_file.write("\n")
        return

    def adc1_wifiinit_read(self, adc_file, adc1_channel, atten_value):
        if self.chipv == "ESP32":
            self.chip.rtc_clk.set_cpu_freq(1)
            self.chip.wifimac.mac_init()
        elif self.chipv == "CHIP722":
            self.chip.power.open_rf()
            time.sleep(1)
            self.chip.rtc_clk.set_cpu_freq(5)
        self.chip.rtc_adc1.config()
        self.chip.rtc_adc1.set(pad = adc1_channel, atten = atten_value)
        adc_file.write("wifiinit,")
        for i in range(66):
            input_dc_value = (i + 1) * 0.05
            self.awg.appl("DC", 0, 0, input_dc_value)
            time.sleep(0.15)
            adc1_value = int(self.chip.rtc_adc1.read())
            adc_file.write("%d,"%(adc1_value))
        adc_file.write("\n")
        if self.chipv == "CHIP722":
            self.chip.power.close_rf()
            self.chip.rtc_clk.set_cpu_freq(1)
        return

    def adc1_lightsleep_read(self, adc_file, adc1_channel, sample_num, atten_value):
        num = [32, 128, 256, sample_num, 0, sample_num]
        k_num = [16, 64, 128, sample_num / 2, 0, 0]
        adc_file.write("lightsleep,")
        for i in range(66):
            input_dc_value = (i + 1) * 0.05
            self.awg.appl("DC", 0, 0, input_dc_value)
            time.sleep(0.15)
            first_addr = self.adc_lib.adc1_lightsleep_read(adc1_channel, sample_num, atten_value)
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
            for j in range(sample_num):
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
            adc_file.write("%d,"%(adc1_value))
        adc_file.write("\n")
        return

    def adc1_deepsleep_read(self, adc_file, adc1_channel, sample_num, atten_value):
        num = [32, 128, 256, sample_num, 0, sample_num]
        k_num = [16, 64, 128, sample_num / 2, 0, 0]
        adc_file.write("deepsleep,")
        for i in range(66):
            input_dc_value = (i + 1) * 0.05
            self.awg.appl("DC", 0, 0, input_dc_value)
            time.sleep(0.15)
            first_addr = self.adc_lib.adc1_deepsleep_read(adc1_channel, sample_num, atten_value)
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
            for j in range(sample_num):
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
            adc_file.write("%d,"%(adc1_value))
        adc_file.write("\n")
        return

    def adc2_2m_read(self, adc_file, adc2_channel, atten_value):
        self.chip.rtc_clk.set_cpu_freq(4)
        self.chip.rtc_adc2.config()
        self.chip.rtc_adc2.set(pad = adc2_channel, atten = atten_value)
        adc_file.write("2M,")
        for i in range(66):
            input_dc_value = (i + 1) * 0.05
            self.awg.appl("DC", 0, 0, input_dc_value)
            time.sleep(0.15)
            adc2_value = int(self.chip.rtc_adc2.read())
            adc_file.write("%d,"%(adc2_value))
        adc_file.write("\n")
        return

    def adc2_80m_read(self, adc_file, adc2_channel, atten_value):
        self.chip.rtc_clk.set_cpu_freq(1)
        self.chip.rtc_adc2.config()
        self.chip.rtc_adc2.set(pad = adc2_channel, atten = atten_value)
        adc_file.write("80M,")
        for i in range(66):
            input_dc_value = (i + 1) * 0.05
            self.awg.appl("DC", 0, 0, input_dc_value)
            time.sleep(0.15)
            adc2_value = int(self.chip.rtc_adc2.read())
            adc_file.write("%d,"%(adc2_value))
        adc_file.write("\n")
        return

    def adc2_wifiinit_read(self, adc_file, adc2_channel, atten_value):
        if self.chipv == "ESP32":
            self.chip.rtc_clk.set_cpu_freq(1)
            self.chip.wifimac.mac_init()
        elif self.chipv == "CHIP722":
            self.chip.power.open_rf()
            time.sleep(1)
            self.chip.rtc_clk.set_cpu_freq(5)
        self.chip.rtc_adc2.config()
        self.chip.rtc_adc2.set(pad = adc2_channel, atten = atten_value)
        adc_file.write("wifiinit,")
        for i in range(66):
            input_dc_value = (i + 1) * 0.05
            self.awg.appl("DC", 0, 0, input_dc_value)
            time.sleep(0.15)
            adc2_value = int(self.chip.rtc_adc2.read())
            adc_file.write("%d,"%(adc2_value))
        adc_file.write("\n")
        if self.chipv == "CHIP722":
            self.chip.power.close_rf()
            self.chip.rtc_clk.set_cpu_freq(1)
        return

    def adc2_lightsleep_read(self, adc_file, adc2_channel, sample_num, atten_value):
        num = [32, 128, 256, sample_num, 0, sample_num]
        k_num = [16, 64, 128, sample_num / 2, 0, 0]
        adc_file.write("lightsleep,")
        for i in range(66):
            input_dc_value = (i + 1) * 0.05
            self.awg.appl("DC", 0, 0, input_dc_value)
            time.sleep(0.15)
            first_addr = self.adc_lib.adc2_lightsleep_read(adc2_channel, sample_num, atten_value)
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
            for j in range(sample_num):
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
            adc2_value = Dout_f
            adc_file.write("%d,"%(adc2_value))
        adc_file.write("\n")
        return

    def adc2_deepsleep_read(self, adc_file, adc2_channel, sample_num, atten_value):
        num = [32, 128, 256, sample_num, 0, sample_num]
        k_num = [16, 64, 128, sample_num / 2, 0, 0]
        adc_file.write("deepsleep,")
        for i in range(66):
            input_dc_value = (i + 1) * 0.05
            self.awg.appl("DC", 0, 0, input_dc_value)
            time.sleep(0.15)
            first_addr = self.adc_lib.adc2_deepsleep_read(adc2_channel, sample_num, atten_value)
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
            for j in range(sample_num):
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
            adc_file.write("%d,"%(adc1_value))
        adc_file.write("\n")
        return

    def adc1_differentmode_run(self, adc1_channel, sample_num):
        self.awg = awg()
        for atten in range(4):
            with open(self.adc_data_path + 'adc1_atten{}_{}.csv'.format(atten, time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())), 'w') as adc_file:
                adc_file.write("input dc, ")
                for i in range(66):
                    input_dc_value = (i + 1) * 0.05
                    adc_file.write("%s,"%(input_dc_value))
                adc_file.write("\n")
                self.adc1_2m_read(adc_file, adc1_channel, atten)
                self.adc1_80m_read(adc_file, adc1_channel, atten)
                self.adc1_wifiinit_read(adc_file, adc1_channel, atten)
                self.adc1_lightsleep_read(adc_file, adc1_channel, sample_num, atten)
                self.adc1_deepsleep_read(adc_file, adc1_channel, sample_num, atten)

    def adc2_differentmode_run(self, adc2_channel, sample_num):
        self.awg = awg()
        for atten in range(4):
            with open(self.adc_data_path + 'adc2_atten{}_{}.csv'.format(atten, time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())), 'w') as adc_file:
                adc_file.write("input_dc, ")
                for i in range(66):
                    input_dc_value = (i + 1) * 0.05
                    adc_file.write("%s,"%(input_dc_value))
                adc_file.write("\n")
                if self.chipv == "ESP32":
                    self.adc2_2m_read(adc_file, adc2_channel, atten)
                self.adc2_80m_read(adc_file, adc2_channel, atten)
                self.adc2_wifiinit_read(adc_file, adc2_channel, atten)
                self.adc2_lightsleep_read(adc_file, adc2_channel, sample_num, atten)
                self.adc2_deepsleep_read(adc_file, adc2_channel, sample_num, atten)
