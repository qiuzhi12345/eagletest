from baselib.loglib.log_lib import *
from hal.Init import HALS
from rtclib.rtc import ULP_PARAM
from rtclib.rtc import WAKEUP_ENABLE
from baselib.instrument.dm import dm


class INTERNAL_LDO(object):
    def __init__(self, channel, chipv = "AUTO"):
        self.chip = HALS(channel, chipv)
        self.chipv = self.chip.chipv
        self.ldo_data_path = '/home/lab/job/{}/lowpower_test/ldo/'.format(self.chipv)

    def ldo_2m_read(self, num, ldo_file, select, adc2_channel, is_rtc):
        self.chip.rtc_clk.set_cpu_freq(4)
        self.chip.power.ldo_debug(select, adc2_channel, is_rtc = is_rtc)
        ldo_file.write("2M,")
        for i in range(num):
            ldo_data = self.mydm.get_result('VDC')
            ldo_file.write("%s,"%(ldo_data))
        ldo_file.write("\n")
        return

    def ldo_80m_read(self, num, ldo_file, select, adc2_channel, is_rtc):
        self.chip.rtc_clk.set_cpu_freq(1)
        self.chip.power.ldo_debug(select, adc2_channel, is_rtc = is_rtc)
        ldo_file.write("80M,")
        for i in range(num):
            ldo_data = self.mydm.get_result('VDC')
            ldo_file.write("%s,"%(ldo_data))
        ldo_file.write("\n")
        return

    def ldo_wifiinit_read(self, num, ldo_file, select, adc2_channel, is_rtc):
        self.chip.rtc_clk.set_cpu_freq(1)
        self.chip.wifimac.mac_init()
        self.chip.power.ldo_debug(select, adc2_channel, is_rtc = is_rtc)
        ldo_file.write("wifiinit,")
        for i in range(num):
            ldo_data = self.mydm.get_result('VDC')
            ldo_file.write("%s,"%(ldo_data))
        ldo_file.write("\n")
        return

    def ldo_lightsleep_read(self, num, ldo_file, select, adc2_channel, is_rtc):
        self.chip.power.ldo_debug(select, adc2_channel, is_rtc = is_rtc)
        ldo_file.write("lightsleep,")
        self.chip.rtc_sleep.special_sleep(0, WAKEUP_ENABLE['TIMER_EXPIRE_EN'].value, 0)
        time.sleep(1)
        for i in range(num):
            output = self.mydm.get_result('VDC')
            ldo_file.write("%s,"%(output))
        time.sleep(4)
        ldo_file.write("\n")
        return

    def ldo_deepsleep_read(self, num, ldo_file, select, adc2_channel, is_rtc):
        self.chip.power.ldo_debug(select, adc2_channel, is_rtc = is_rtc)
        ldo_file.write("deepsleep,")
        self.chip.rtc_sleep.special_sleep(0x29, WAKEUP_ENABLE['TIMER_EXPIRE_EN'].value, 0)
        time.sleep(1)
        for i in range(num):
            output = self.mydm.get_result('VDC')
            ldo_file.write("%s,"%(output))
        time.sleep(4)
        ldo_file.write("\n")
        return

    def ldo_diffmode_test(self, select, test_num, adc2_channel, is_rtc = True):
        '''For chip ESP32: adc2_channel should set to 0,2,7,8,9;
           For CHIP722: if test adc2_vref, is_rtc should set to 0.
        '''
        self.mydm = dm()
        if self.chipv == "ESP32":
            if select == 0:
                ldo_name = "rtc_ldo"
            elif select == 1:
                ldo_name = "adc2_vref"
            elif select == 2:
                ldo_name = "digital_ldo"
            else:
                logerror("input select param wrong")
                return
        else:
            if is_rtc and (0 == select):
                ldo_name = "rtc_ldo"
            elif is_rtc and (1 == select):
                ldo_name = "adc1_vref"
            elif is_rtc and (2 == select):
                ldo_name = "digital_ldo"
            elif (not is_rtc) and (0 == select):
                ldo_name = "adc2_vref"
            else:
                logerror("input select param wrong")
                return

        with open(self.ldo_data_path + '{}_{}.csv'.format(ldo_name, time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())), 'w') as ldo_file:
            self.ldo_2m_read(test_num, ldo_file, select, adc2_channel, is_rtc)
            self.ldo_80m_read(test_num, ldo_file, select, adc2_channel, is_rtc)
            #self.ldo_wifiinit_read(test_num, ldo_file, select, adc2_channel, is_rtc)
            self.ldo_lightsleep_read(test_num, ldo_file, select, adc2_channel, is_rtc)
            #self.ldo_deepsleep_read(test_num, ldo_file, select, adc2_channel, is_rtc)