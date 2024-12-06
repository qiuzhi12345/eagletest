import baselib.plot.myplot as myplot
from baselib.test_channel.com import COM as com
from baselib.loglib.log_lib import *
from hal.common import PBUS
from hal.common import MEM
import rftest.rflib.rfglobal as rfglobal
from hal.hwregister.hwi2c.all import *
from hal.hwregister.hwpbus.all import *


pbus_rxbb_1_dict = {
    'lpf_dg[1:7]'       : (6,5,4,3,2,1,0),
}

pbus_rxbb_2_dict = {
    'lpf_dg_fine[2:0]'  : (5,4,3),
    'xpd_adc'           : 2,
    'xpd_filter'        : 1,
    'lpf_rstb_pkdet'    : 0,
}

pbus_txbb_1_1_dict = {
    'lpf_dg[1:2]'       : (4,3),
    'lpf_dg_fine[2:0]'  : (2,1,0)
}

pbus_txbb_1_2_dict = {
    'tos_dac_i[6:0]'    : (6,5,4,3,2,1,0)
}

pbus_txbb_2_1_dict = {
    'en_tx_ckgen'       : 6,
    'en_tx_ck'          : 5,
    'xpd_dac'           : 4,
    'xpd_ckgen'         : 3,
    'xpd_ckgen_bufrx'   : 2,
    'xpd_v2i'           : 1,
    'xpd_filter'        : 0
}

pbus_txbb_2_2_dict = {
    'tos_dac_q[6:0]'    : (6,5,4,3,2,1,0)
}

gain_to_rfrx_gain_dict = {
    10:	 "111111110",
    9:	 "111111100",
    8:	 "111110110",
    7:	 "111110100",
    6:	 "111101110",
    5:	 "111101100",
    4:	 "111100110",
    3:	 "111100100",
    2:	 "110101100",
    1:	 "110100110",
    0:	 "110100100"
}

pbus_rfrx_dict = {
    'xpd_rfrx_vga'      : 8,
    'xpd_rfrx_lna'      : 7,
    'rxsw_hg'           : 6,
    'rxsw_hg_fine'      : 5,
    'lna_dg'            : 4,
    'vga_dg_gm'         : 3,
    'vga_dg_buf'        : 2,
    'vga_dg_load'       : 1,
    'tx_on'             : 0
}

pbus_dict = {
    "rfrx1" 	  : 0,
    "bb" 	  : 1,
    "dcoi"        : 2,
    "dcoq"        : 3,
    "rftx1" 	  : 4,
    "rftx2"       : 5
}

pbus_en_dict = {
    "en1" 	  : 1,
    "en2" 	  : 2,
    "en3" 	  : 4
}
#-------------------------------------------------------------------------------#
# PBUS func,
#-------------------------------------------------------------------------------#
class pbus(object):
    def __init__(self,comport,chipv='ESP32'):
        self.comport = comport
        self.chipv = chipv
        self.pbus = PBUS(self.comport,self.chipv)
        self.mem = MEM(self.comport,self.chipv)
        self.i2c = HWI2C(self.comport,self.chipv)
        self.hwpbus = HWPBUS(self.comport,self.chipv)

    def pbus_debugmode(self):
        return self.pbus.pbus_debugmode()

    def pbus_workmode(self):
        self.pbus.pbus_workmode()
        if self.chipv != 'ESP8266':  #return to RX state
            self.mem.wrm(0x600060a0, 11, 8, 0xe)  #force tx/rx off
            self.mem.wrm(0x600060a0, 11, 8, 0)  #release force

    def pbus_rd(self,pbus_sel,pbus_en_sel):
        return self.pbus.pbus_rd(pbus_sel,pbus_en_sel)

    def pbus_wr(self,pbus_sel,pbus_en_sel,value):
        return self.pbus.pbus_wr(pbus_sel,pbus_en_sel,value)

    def read_dco(self):
        i1=self.pbus_rd('dcoi', 'en1')
        i2=self.pbus_rd('dcoi', 'en2')
        q1=self.pbus_rd('dcoq', 'en1')
        q2=self.pbus_rd('dcoq', 'en2')
        loginfo("i1=%d, i2=%d, q1=%d, q2=%d"%(i1, i2, q1, q2))
        return [i1, q1, i2, q2]

    def set_dco(self,i1=0x100, q1=0x100, i2=0x100, q2=0x100):
        self.pbus_wr('dcoi', 'en1', i1)
        self.pbus_wr('dcoi', 'en2', i2)
        self.pbus_wr('dcoq', 'en1', q1)
        self.pbus_wr('dcoq', 'en2', q2)

    def open_tx(self,pa=0x5f, bb=0x120):
        if self.chipv=="ESP8266":
            self.pbus_wr('txbb2', 'en1', 0x7F)
            self.pbus_wr('txbb1', 'en1', bb)
            self.pbus_wr('bbrx1', 'en1', 0x0)
            self.pbus_wr('bbrx1', 'en2', 0x0)
            self.pbus_wr('rfrx1', 'en1', 0x1)
            self.set_dco(256,256,256,256)
            self.pbus_wr('rftx2', 'en1', pa)   # PA gain to
            self.pbus_wr('rftx1', 'en1', 0x7F)

        else:
            self.pbus_wr('rfrx1', 'en1', 0x1)
            self.pbus_wr('bb', 'en1', 0x7c)
            self.pbus_wr('bb', 'en2', bb)
            self.set_dco(256,256,256,256)
            self.pbus_wr('rftx1', 'en1', 0x7f)
            self.pbus_wr('rftx2', 'en1', pa)

    def open_rx(self, rfrx1=0x184, bb_gain=0, filter_atten=0,bt_mode=0):
        if self.chipv=="ESP8266":
            self.pbus_wr('rftx1', 'en1', 0x0)
            self.pbus_wr('rftx2', 'en1', 0x0)
            self.pbus_wr('txbb2', 'en1', 0xC)
            self.pbus_wr('rfrx1', 'en1', 0x184)
            self.pbus_wr('bbrx1', 'en1', 0x0)
            self.pbus_wr('bbrx1', 'en2', 0x6)
            self.set_dco(0xf6,0x100,0x100,0x108)
        else :
            self.pbus_wr('rftx1', 'en1', 0x0)
            self.pbus_wr('rftx2', 'en1', 0x0)
            self.pbus_wr('rftx1', 'en2', 0x0)
            self.pbus_wr('rfrx1', 'en1', rfrx1)
            if bt_mode==1:
                self.pbus_wr('bb', 'en1', 0x18b)
                self.pbus_wr('rftx1', 'en2', filter_atten<<3)
            else:
                self.pbus_wr('bb', 'en1', 0x189)
            self.pbus_wr('bb', 'en2', bb_gain)
            self.set_dco(0x100,0x100,0x100,0x100)

    def loop_adc_flt_adc(self, en=1):
        if en==1:
            self.hwpbus.RFRX1.EN1 = 0x001
            self.hwpbus.RFTX1.EN1 = 0x000
            self.hwpbus.RFTX2.EN1 = 0x000
            self.hwpbus.BB1.EN1   = 0x1c9
            self.hwpbus.BB1.EN2   = 0
            self.i2c.bbtop.enlb = 0
        else:
            self.hwpbus.RFRX1.EN1 = 0x184
            self.hwpbus.RFTX1.EN1 = 0x000
            self.hwpbus.RFTX2.EN1 = 0x000
            self.hwpbus.BB1.EN1   = 0x189
            self.hwpbus.BB1.EN2   = 0


    def all_pbus(self):
        if self.chipv=="ESP8266":
            rfrx1 = self.pbus_rd('rfrx1','en1')
            bb1 = self.pbus_rd('bbrx1','en1')
            bb2 = self.pbus_rd('bbrx1','en2')
            rftx1 = self.pbus_rd('rftx1', 'en1')
            rftx2 = self.pbus_rd('rftx2', 'en1')
            txbb1 = self.pbus_rd('txbb1','en1')
            txbb2 = self.pbus_rd('txbb2','en1')
            dcoi1 = self.pbus_rd('dcoi', 'en1')
            dcoq1 = self.pbus_rd('dcoq', 'en1')
            dcoi2 = self.pbus_rd('dcoi', 'en2')
            dcoq2 = self.pbus_rd('dcoq', 'en2')
            loginfo('\n'+'rfrx1:0x%x\n'%rfrx1+'rftx1:0x%x\n'%rftx1+'rftx2:0x%x\n'%rftx2+'bb1  :0x%x\n'%bb1+'bb2  :0x%x\n'%bb2+'%d, %d, %d, %d\n'%(dcoi1, dcoq1, dcoi2, dcoq2))
            return [rfrx1, rftx1, rftx2, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2]

        else:
            rfrx1 = self.pbus_rd('rfrx1', 'en1')
            rftx1 = self.pbus_rd('rftx1', 'en1')
            rftx1_en2 = self.pbus_rd('rftx1', 'en2')
            rftx2 = self.pbus_rd('rftx2', 'en1')
            bb1   = self.pbus_rd('bb', 'en1')
            bb2   = self.pbus_rd('bb', 'en2')
            dcoi1 = self.pbus_rd('dcoi', 'en1')
            dcoq1 = self.pbus_rd('dcoq', 'en1')
            dcoi2 = self.pbus_rd('dcoi', 'en2')
            dcoq2 = self.pbus_rd('dcoq', 'en2')
            loginfo('\n'+'rfrx1:0x%x\n'%rfrx1+'rftx1:0x%x\n'%rftx1+'rftx1_en2:0x%x\n'%rftx1_en2+'rftx2:0x%x\n'%rftx2+'bb1  :0x%x\n'%bb1+'bb2  :0x%x\n'%bb2+'%d, %d, %d, %d\n'%(dcoi1, dcoq1, dcoi2, dcoq2))
            return [rfrx1, rftx1, rftx2, bb2, bb1, dcoi1, dcoq1, dcoi2, dcoq2]









