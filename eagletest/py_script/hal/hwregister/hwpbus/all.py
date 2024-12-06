class HWPBUS(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        if chipv == "ESP32" or chipv == "CHIP72" or chipv == "CHIP722" or chipv == "CHIP723":
            from hal.hwregister.hwpbus.ESP32.PBUS import *
            self.RFRX1=RFRX1(channel,chipv)
            self.BB1=BB1(channel,chipv)
            self.RFTX1=RFTX1(channel,chipv)
            self.RFTX2= RFTX2(channel,chipv)
            self.DCOI=DCOI(channel,chipv)
            self.DCOQ=DCOQ(channel,chipv)

        elif chipv == "ESP8266":
            from hal.hwregister.hwpbus.ESP8266.PBUS import *
            self.RFRX1=RFRX1(channel,chipv)
            self.TXBB1=TXBB1(channel,chipv)
            self.TXBB2=TXBB2(channel,chipv)
            self.BBRX1=BBRX1(channel,chipv)
            self.RFTX1=RFTX1(channel,chipv)
            self.RFTX2= RFTX2(channel,chipv)
            self.DCOI=DCOI(channel,chipv)
            self.DCOQ=DCOQ(channel,chipv)
