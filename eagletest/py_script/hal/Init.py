from baselib.loglib.log_lib import *
import baselib.eagletool.autowork as ak
from hal.common import *
from hal.hwregister.hwreg.all import *
from hal.hwregister.hwi2c.all import *
from hal.hwregister.hwpbus.all import *
from hal.gpio import GPIO
from hal.touch import TOUCH
from hal.rtc_timer import RTC_TIMER
from hal.rtc_sleep import RTC_SLEEP
from hal.rtc_wdt import RTC_WDT
from hal.rtc import RTC
from hal.dac import DAC
from hal.ulp import ULP
from hal.wifimac import WIFIMAC
from maclib.mac_common import mac_common
from hal.bt_api import BTAPI
from hal.wifi_api import WIFIAPI
from hal.rtc_clock import RTC_CLK
from hal.adc import RTC_ADC1, RTC_ADC2, DIG_ADC, ADC2_ARB
from hal.rtc_debug import *
from hal.hall_sens import HALL_SENS
from hal.tsen import TSEN
from hal.power import POWER
from hal.rtc_brownout import RTC_BROWNOUT
from hal.riscv import RISCV
from hal.x32k_wdt import X32K_WDT
from hal.swd import SWD
from hal.efuse_mac import *

class HALS(object):
    """docstring for HALS"""
    def __init__(self, channel, chipv = "AUTO"):
        self.channel = channel
        # try:
        if chipv == "AUTO":
            self.chipv = CHIP_INFO(self.channel, chipv).get_chipv()
        else:
            self.chipv = chipv
        self.CHIP_ID = CHIP_ID(self.channel, self.chipv)

        self.MEM = MEM(self.channel, self.chipv)
        self.MEM_TS = MEM_TS(self.channel ,self.chipv)
        self.PBUS= PBUS(self.channel,self.chipv)
        self.HWPBUS= HWPBUS(self.channel,self.chipv)
        self.HWREG = HWREG(self.channel, self.chipv)
        self.HWI2C = HWI2C(self.channel, self.chipv)
        self.i2c = I2C(self.channel, self.chipv)
        self.gpio = GPIO(self.channel, self.chipv)
        self.rtc_timer = RTC_TIMER(self.channel, self.chipv)
        self.rtc_sleep = RTC_SLEEP(self.channel, self.chipv)
        self.rtc_wdt = RTC_WDT(self.channel, self.chipv)
        self.rtc = RTC(self.channel, self.chipv)
        self.touch = TOUCH(self.channel, self.chipv)
        self.dac = DAC(self.channel, self.chipv)
        self.ulp = ULP(self.channel, self.chipv)
        self.wifiapi = WIFIAPI(self.channel, self.chipv)
        self.btapi = BTAPI(self.channel, self.chipv)
        self.rtc_clk = RTC_CLK(self.channel, self.chipv)
        self.rtc_adc1 = RTC_ADC1(self.channel, self.chipv)
        self.rtc_adc2 = RTC_ADC2(self.channel, self.chipv)
        self.dig_adc = DIG_ADC(self.channel, self.chipv)
        self.adc2_arb = ADC2_ARB(self.channel, self.chipv)
        self.rtc_debug = RTC_DEBUG(self.channel, self.chipv)
        self.hall_sens = HALL_SENS(self.channel, self.chipv)
        self.tsen = TSEN(self.channel, self.chipv)
        self.power = POWER(self.channel, self.chipv)
        self.rtc_brownout = RTC_BROWNOUT(self.channel, self.chipv)
        self.efuse_mac = EFUSE_MAC(self.channel, self.chipv)
        if self.chipv == "CHIP722" or self.chipv == "CHIP723":
            self.x32k_wdt = X32K_WDT(self.channel, self.chipv)
            self.swd = SWD(self.channel, self.chipv)
        # except:
        #     logwarn("Load HAL fail")
        self.wifimac = WIFIMAC(self.channel, self.chipv)
        self.riscv = RISCV(self.channel,self.chipv)
        # lib
        self.mac_common = mac_common(self.channel, self.chipv)

    def deinit(self):
        self.channel.deinit()

    def eagle_download(self, user_name = "gusd", args = "", Imode = True, bin_file = "eagle_test.bin"):
        u = ak.eagle_download_tool_class(self.channel, self.chipv)
        u.eagle_download("", user_name , args, Imode, bin_file)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.deinit()
