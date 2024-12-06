from hal.Init import HALS
import time
class POWER_CONTROL():
    def __init__(self, channel, chipv = "ESP32"):
        self.channel = channel
        self.chipv = chipv
        self.chip = HALS(self.channel, self.chipv)
        self.chip.rtc_wdt.wdt_unlock()
        self.chip.rtc_wdt.wdt_init()
        time.sleep(1)

    def chip_reset(self, chip_en_pad, stripping_pad):
        self.chip.gpio.dig_gpio_out(stripping_pad, 1, 3)
        self.chip.gpio.dig_gpio_out(chip_en_pad, 0, 3)
        self.chip.gpio.dig_gpio_out(chip_en_pad, 1, 3)

    def chip_download(self, chip_en_pad, stripping_pad):
        self.chip.gpio.dig_gpio_out(stripping_pad, 0, 3)
        self.chip.gpio.dig_gpio_out(chip_en_pad, 0, 3)
        self.chip.gpio.dig_gpio_out(chip_en_pad, 1, 3)
