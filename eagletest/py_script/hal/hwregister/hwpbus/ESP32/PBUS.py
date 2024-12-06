from hal.common import *
class RFRX1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self._PBUS = PBUS(self.channel,self.chipv)
        self.rfrx1_sel='rfrx1'
        self.en1_sel='en1'
    @property
    def EN1(self):
        return self._PBUS.pbus_rd(self.rfrx1_sel,self.en1_sel)
    @EN1.setter
    def EN1(self,value):
        self._PBUS.pbus_debugmode()
        return self._PBUS.pbus_wr(self.rfrx1_sel,self.en1_sel,value)

class BB1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self._PBUS = PBUS(self.channel,self.chipv)
        self.bb1_sel = 'bb'
        self.en1_sel = 'en1'
        self.en2_sel = 'en2'
    @property
    def EN1(self):
        return self._PBUS.pbus_rd(self.bb1_sel,self.en1_sel)
    @EN1.setter
    def EN1(self,value):
        self._PBUS.pbus_debugmode()
        return self._PBUS.pbus_wr(self.bb1_sel,self.en1_sel,value)
    @property
    def EN2(self):
        return self._PBUS.pbus_rd(self.bb1_sel,self.en2_sel)
    @EN2.setter
    def EN2(self,value):
        self._PBUS.pbus_debugmode()
        return self._PBUS.pbus_wr(self.bb1_sel,self.en2_sel,value)

class RFTX1(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self._PBUS = PBUS(self.channel,self.chipv)
        self.rftx1_sel = 'rftx1'
        self.en1_sel = 'en1'
    @property
    def EN1(self):
        return self._PBUS.pbus_rd(self.rftx1_sel,self.en1_sel)
    @EN1.setter
    def EN1(self,value):
        self._PBUS.pbus_debugmode()
        return self._PBUS.pbus_wr(self.rftx1_sel,self.en1_sel,value)

class RFTX2(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self._PBUS = PBUS(self.channel,self.chipv)
        self.rftx2_sel = 'rftx2'
        self.en1_sel = 'en1'
    @property
    def EN1(self):
        return self._PBUS.pbus_rd(self.rftx2_sel,self.en1_sel)
    @EN1.setter
    def EN1(self,value):
        self._PBUS.pbus_debugmode()
        return self._PBUS.pbus_wr(self.rftx2_sel,self.en1_sel,value)

class DCOI(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self._PBUS = PBUS(self.channel,self.chipv)
        self.dcoi_sel = 'dcoi'
        self.en1_sel = 'en1'
        self.en2_sel = 'en2'
    @property
    def CK1(self):
        return self._PBUS.pbus_rd(self.dcoi_sel,self.en1_sel)
    @CK1.setter
    def CK1(self,value):
        self._PBUS.pbus_debugmode()
        return self._PBUS.pbus_wr(self.dcoi_sel,self.en1_sel,value)
    @property
    def CK2(self):
        return self._PBUS.pbus_rd(self.dcoi_sel,self.en2_sel)
    @CK2.setter
    def CK2(self,value):
        self._PBUS.pbus_debugmode()
        return self._PBUS.pbus_wr(self.dcoi_sel,self.en2_sel,value)

class DCOQ(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self._PBUS = PBUS(self.channel,self.chipv)
        self.dcoq_sel = 'dcoq'
        self.en1_sel = 'en1'
        self.en2_sel = 'en2'
    @property
    def CK1(self):
        return self._PBUS.pbus_rd(self.dcoq_sel,self.en1_sel)
    @CK1.setter
    def CK1(self,value):
        self._PBUS.pbus_debugmode()
        return self._PBUS.pbus_wr(self.dcoq_sel,self.en1_sel,value)
    @property
    def CK2(self):
        return self._PBUS.pbus_rd(self.dcoq_sel,self.en2_sel)
    @CK2.setter
    def CK2(self,value):
        self._PBUS.pbus_debugmode()
        return self._PBUS.pbus_wr(self.dcoq_sel,self.en2_sel,value)