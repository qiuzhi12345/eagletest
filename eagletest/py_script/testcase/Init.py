from baselib.loglib.log_lib import *
from hal.common import *
from hal.Init import *
from maclib.mac_common import mac_dbg
from functionCase.GPIO.gpio_test import GPIO_TC_FUNC
from functionCase.RTC_TIMER.rtc_timer_test import RTC_TIMER_TC_FUNC
from functionCase.RTC_WDT.rtc_wdt_test import RTC_WDT_TC_FUNC
from functionCase.TOUCH.touch_test import TOUCH_TC_FUNC
from functionCase.ULP.ulp_test import ULP_TC_FUNC
from functionCase.SARADC.saradc_test import SARADC_TC_FUNC
from functionCase.DAC.dac_test import DAC_TC_FUNC
from functionCase.HALL_SENS.hall_sens_test import HALL_SENS_TC_FUNC
from functionCase.TSEN.tsen_test import TSEN_TC_FUNC
from functionCase.WIFIMAC.wifimac import WIFIMAC_TC_FUNC
from functionCase.WIFIMAC.wifimac import WIFISLEEP_TC_FUNC
from functionCase.CLOCK.clock_test import CLOCK_TC_FUNC
from functionCase.X32K_WDT.x32k_wdt_test import X32K_WDT_TC_FUNC
from functionCase.SWD.swd_test import SWD_TC_FUNC
from functionCase.RTC_BROWNOUT.rtc_brownout_test import RTC_BROWNOUT_TC_FUNC
from functionCase.SARADC.current_test import CURRENT_TC
from performanceCase.DAC.DAC_ptest           import DAC_TC_PERF
from performanceCase.CLK.CLKINT_ptest        import CLK_TC_PERF
from performanceCase.USB.USB_ptest           import USB_TC_PERF
from performanceCase.BB.bbpll                import BBPLL
from performanceCase.STABLE.stability        import Stability
from performanceCase.ADC.adc_ptest           import AdcPtest
from performanceCase.BROWNOUT.brownout_ptest import BrownOutPtest
from performanceCase.CHIPPU.chippu_ptest     import ChipPuPtest
from performanceCase.CLK.clk_ptest           import ClkPtest
from performanceCase.CONFIG.config_ptest     import PtestConfig
from performanceCase.CLK.CLKINT_ptest        import CLK_TC_PERF
from performanceCase.GPIO.gpio_ptest         import GpioPtest
from performanceCase.REF.ref_ptest           import RefPtest
from performanceCase.REF.ref_ptest           import LdoPtest
from performanceCase.SLEEP.sleep_ptest       import SleepPtest
from performanceCase.SPI.spi_ptest           import SpiPtest
from performanceCase.TOUCH.touch_ptest       import TouchPtest
from performanceCase.TSEN.tsen_ptest         import TsenPtest
from lowpowerCase.TSEN.tsen_ltest        import TSEN_TC_LOWPOWER
from lowpowerCase.ADC.adc_ltest          import ADC_TC_LOWPOWER
from lowpowerCase.DAC.dac_ltest          import DAC_TC_LOWPOWER
from lowpowerCase.LDO.internal_ldo       import INTERNAL_LDO
# from volumeCase.SOCKET.socket            import SocketPtest
# from volumeCase.MULTIBOARD.multiboard    import MultiBoardPtest

class TCS(object):
    """docstring for TCS"""
    def __init__(self, channel, chipv = "AUTO"):
        self.hals = HALS(channel, chipv)
        self.chipv = self.hals.chipv
        self.channel = self.hals.channel

        # function testcase
        self.gpio_tc_func = GPIO_TC_FUNC(self.channel, self.chipv)
        self.rtc_timer_tc_func = RTC_TIMER_TC_FUNC(self.channel, self.chipv)
        self.rtc_wdt_tc_func = RTC_WDT_TC_FUNC(self.channel, self.chipv)
        self.touch_tc_func = TOUCH_TC_FUNC(self.channel, self.chipv)
        self.ulp_tc_func = ULP_TC_FUNC(self.channel, self.chipv)
        self.adc_tc_func = SARADC_TC_FUNC(self.channel, self.chipv)
        self.dac_tc_func = DAC_TC_FUNC(self.channel, self.chipv)
        self.hall_sens_tc_func = HALL_SENS_TC_FUNC(self.channel, self.chipv)
        self.tsen_tc_func = TSEN_TC_FUNC(self.channel, self.chipv)
        self.wifimac_tc_func = WIFIMAC_TC_FUNC(self.channel, self.chipv)
        self.wifisleep_tc_func = WIFISLEEP_TC_FUNC(self.channel, self.chipv)
        self.wifidbg_tc_func = mac_dbg(self.channel, self.chipv)
        self.clock_tc_func = CLOCK_TC_FUNC(self.channel, self.chipv)
        self.brownout_tc_func = RTC_BROWNOUT_TC_FUNC(self.channel, self.chipv)
        if self.chipv == "CHIP722" or self.chipv == "CHIP723":
            self.x32k_wdt_tc_func = X32K_WDT_TC_FUNC(self.channel, self.chipv)
            self.swd_tc_func = SWD_TC_FUNC(self.channel, self.chipv)

        # lowpower testcase
        # self.tsen_tc_lowpower = TSEN_TC_LOWPOWER(self.channel, self.chipv)
        # self.adc_tc_lowpower = ADC_TC_LOWPOWER(self.channel, self.chipv)
        # self.dac_tc_lowpower = DAC_TC_LOWPOWER(self.channel, self.chipv)
        # self.internal_ldo = INTERNAL_LDO(self.channel, self.chipv)
        # if self.chipv == "CHIP722":
        #     self.current_tc_func = CURRENT_TC(self.channel,self.chipv)

        # performance testcase
        # self.dac_tc_perf     = DAC_TC_PERF(self.channel, self.chipv)        
        # self.bbpll           = BBPLL(self.channel,self.chipv)
        # self.adc_tc_perf     = AdcPtest(self.channel,self.chipv)
        # self.ref_tc_perf     = RefPtest(self.channel, self.chipv)
        # self.ldo_tc_perf     = LdoPtest(self.channel, self.channel, self.chipv)
        # self.touch_tc_perf   = TouchPtest(self.channel,self.chipv)
        # self.spi_tc_perf     = SpiPtest(self.channel,self.chipv)
        # self.brownout_tc_perf= BrownOutPtest(self.channel, self.chipv)
        # self.chippu_tc_perf  = ChipPuPtest(self.channel, self.chipv)
        # self.cfg_tc_perf     = PtestConfig(self.channel,self.channel, self.chipv)
        # self.clk_tc_perf     = ClkPtest(self.channel, self.chipv)
        # self.tsen_tc_perf    = TsenPtest(self.channel, self.chipv)
        # if self.chipv == "CHIP722":
        #     self.usb_tc_perf = USB_TC_PERF(self.channel,self.chipv)
        #     self.stable      = Stability(self.channel,self.chipv)
        #     self.socket_run  = SocketPtest(self.channel,self.chipv)
        #     self.mb_run      = MultiBoardPtest(self.channel,self.channel,self.chipv)
        #     self.mb_data_p   = DATA_PROCESS_MB()
            # self.clk_p   = CLK_TC_PERF(self.channel,self.chipv)

    def deinit(self):
        self.channel.deinit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.deinit()
