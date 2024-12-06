# -- coding: utf-8 --
from baselib.test_channel.com import COM as com
from baselib.loglib.log_lib import *
from hal.Init import HALS
from rtclib.rtc import WAKEUP_REASON
from rtclib.rtc import WAKEUP_ENABLE

class X32K_WDT_TC_FUNC(object):
    def __init__(self, channel, chipv = "AUTO"):
        self.chip = HALS(channel, chipv)
        self.chipv = self.chip.chipv

    def backup_32k_factor(self):
        #假如有个value_min，则有(8-n)个value_max, 则value_min * n + value_max *(8-n) = S
        period_150k = int(self.chip.rtc_clk.get_clk_calibration(0))
        freq_150k = (1000000 << 19) / period_150k / 1000
        S = freq_150k / 8
        value_min = S / 8
        value_max = value_min + 1
        n = (8 * value_max - S)/(value_max - value_min)
        fvalue = 0
        for i in range(n):
            fvalue +=  (value_min << (28 -  4 * i))
        for j in range(8-n):
            fvalue += (value_max << (4 * j))
        loginfo("150k freq: %d, fvalue: 0x%x"%(freq_150k, fvalue))
        return fvalue

    def tc000_x32k_wdt_wakeup_test(self):
        '''
        进入deepsleep后x32k晶振短路（手动接地）
        '''
        wakeup_cause0 = int(self.chip.rtc_sleep.wakeup_cause())
        if (WAKEUP_REASON['X32K_DEAD_TRIG'].value == wakeup_cause0):
            logerror("chip need reset, wakeup_cause0: %d\n"%(WAKEUP_REASON['X32K_DEAD_TRIG'].value))
            return
        self.chip.rtc_clk.set_32k()
        self.chip.rtc_clk.start_32k(1)
        time.sleep(1)
        self.chip.rtc_clk.rtc_slow_clk_select(1)
        self.chip.x32k_wdt.wdt_int_clr()
        fvalue = self.backup_32k_factor()
        self.chip.x32k_wdt.wdt_init(factor_value = fvalue)
        self.chip.x32k_wdt.wdt_config()
        self.chip.rtc_sleep.sleep(0x3f, WAKEUP_ENABLE['X32K_DEAD_TRIG_EN'].value, 0)
        time.sleep(2)
        wakeup_cause = int(self.chip.rtc_sleep.wakeup_cause())
        if (wakeup_cause == WAKEUP_REASON['X32K_DEAD_TRIG'].value):
            return logpass()
        else:
            return logfail()

    def tc001_send_int_test(self):
        raw = int(self.chip.x32k_wdt.wdt_int_raw_sts())
        if raw:
            logerror("need reset chip, raw is not 0: %d\n"%(raw))
            return
        self.chip.rtc_clk.set_32k()
        self.chip.rtc_clk.start_32k(1)
        time.sleep(1)
        self.chip.rtc_clk.rtc_slow_clk_select(1)
        self.chip.x32k_wdt.wdt_int_clr()
        fvalue = self.backup_32k_factor()
        self.chip.x32k_wdt.wdt_init(factor_value = fvalue)
        self.chip.x32k_wdt.wdt_config()
        #need connect x32k to ground in 3 seconds.
        time.sleep(3)
        raw0 = int(self.chip.x32k_wdt.wdt_int_raw_sts())
        self.chip.x32k_wdt.wdt_int_enable(1)
        sts0 = int(self.chip.x32k_wdt.wdt_int_sts())
        self.chip.x32k_wdt.wdt_int_enable(0)
        sts1 = int(self.chip.x32k_wdt.wdt_int_sts())
        self.chip.x32k_wdt.wdt_int_clr()
        raw1 = int(self.chip.x32k_wdt.wdt_int_raw_sts())
        if (1 != raw0) or (1 != sts0) or (0 != sts1) or (0 != raw1):
            logerror("fail, raw0: %d, sts0: %d, sts1: %d, raw1: %d\n"%(raw0, sts0, sts1, raw1))
            return logfail()
        else:
            return logpass()

    def tc002_x32k_auto_return_test(self):
        '''
        用示波器看波形，刚开始有x32k时钟，进入deepsleep后x32k晶振短路（手动接地），x32k时钟消失－》backup_32k时钟出现－》x32k时钟起振，backup时钟消失;
        x32k wdt时钟与backup_32k或x32k时钟相同，与哪个时钟相同取决于当前哪个时钟起来。
        '''
        self.chip.rtc_debug.TOUCH_PAD5(0, 10, 3)#backup 32k
        self.chip.rtc_debug.TOUCH_PAD1(0, 4, 0)#xtal 32k
        self.chip.rtc_debug.TOUCH_PAD2(0, 20, 2)#x32k wdt
        self.chip.rtc_clk.set_32k()
        self.chip.rtc_clk.start_32k(1)
        time.sleep(1)
        self.chip.rtc_clk.rtc_slow_clk_select(1)
        fvalue = self.backup_32k_factor()
        self.chip.x32k_wdt.wdt_init(factor_value = fvalue)
        self.chip.x32k_wdt.wdt_config()
        self.chip.rtc_sleep.sleep(0x3d, 0, 0)

    def tc003_x32k_software_return_test(self):
        '''
        用示波器看波形，backup_32k在x32k未enable之前有振幅（因为打开x32k的方式为软件打开，所以无法自动打开x32k）；
        xtal 32k在x32k未enable前为低电平，enable后变成32k方波。
        '''
        self.chip.rtc_debug.TOUCH_PAD5(0, 10, 3)#backup 32k
        self.chip.rtc_debug.TOUCH_PAD1(0, 4, 0)#xtal 32k
        self.chip.rtc_debug.TOUCH_PAD2(0, 20, 2)#x32k wdt
        self.chip.rtc_clk.set_32k()
        self.chip.rtc_clk.start_32k(0)
        fvalue = self.backup_32k_factor()
        self.chip.x32k_wdt.wdt_init(factor_value = fvalue)
        self.chip.x32k_wdt.wdt_config()
        self.chip.x32k_wdt.x32k_poweron_bysoftware(1)
        loginfo("delay begin")
        time.sleep(5)
        loginfo("delay end")
        self.chip.rtc_clk.start_32k(1)
