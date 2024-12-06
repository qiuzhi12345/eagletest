from baselib.test_channel.com import COM as com
from baselib.loglib.log_lib import *
from hal.Init import HALS

class HALL_SENS_TC_FUNC(object):
    def __init__(self, channel, chipv = "AUTO"):
        self.chip = HALS(channel, chipv)
        self.chipv = self.chip.chipv

    def tc000_hall_vdd_test(self):
        self.chip.hall_sens.config()
        time.sleep(0.001)
        self.chip.rtc_adc1.config()
        self.chip.rtc_adc1.set(0)
        vp0 = int(self.chip.rtc_adc1.read())
        self.chip.rtc_adc1.set(3)
        vn0 = int(self.chip.rtc_adc1.read())
        self.chip.hall_sens.phase_inv()
        self.chip.rtc_adc1.set(0)
        vp1 = int(self.chip.rtc_adc1.read())
        self.chip.rtc_adc1.set(3)
        vn1 = int(self.chip.rtc_adc1.read())
        vdd = (vp0 - vp1) - (vn0 - vn1)
        loginfo("vp0: %d, vp1: %d, vn0: %d, vn1: %d\n"%(vp0, vp1, vn0, vn1))
        loginfo("vdd: %d\n"%(vdd))
        
        
        
        



