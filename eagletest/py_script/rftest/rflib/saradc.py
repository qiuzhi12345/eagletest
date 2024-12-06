from hal.common import *
from rftest.rflib.wifi_lib import WIFILIB
from rftest.rflib.pbus import pbus as Pbus
import rftest.rflib.rfglobal as rfglobal
import rftest.rflib.wifi_instrum as rftx
from baselib.loglib.log_lib import *
from pylab import *
from hal.hwregister.hwi2c.all import *

class SARADC(object):

    def __init__(self,comport,chipv='ESP32'):

        self.comport = comport
        self.chipv = chipv
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.mem = MEM(self.comport, self.chipv)
        self.pbus = Pbus(self.comport, self.chipv)
        self.i2c = HWI2C(self.comport,self.chipv)

    def sar_init(self):
        if self.chipv == "ESP8266":
            self.mem.wr(0x60000710,(self.mem.rd(0x60000710)&0xfdffffff | (0x1<<25))) #XPD_SAR_I2C=bit[25]
##            i2c.wic('saradc','xpd_sar',1)  #xpd_sar=bit[4]
##            i2c_wrm.wim('saradc',1,0,0,0)  #w
        else:
            self.mem.wrm(0x6000882c, 7, 5, 4)  # pwdet_cct
            self.mem.wrm(0x60008890, 27, 27, 1)  #sar2_pwdet_force
            self.mem.wrm(0x6000880c, 19, 18, 3)  #sar_xpd_fsm
            self.mem.wrm(0x600060c0, 7, 7, 1)  #swap pkdet and pwdet

    def en_pwdet(self,signal='tone'):
        self.sar_init()

        if self.chipv == "ESP8266":
            self.mem.setmask(0x60000D5c,0x800000)
            self.mem.clrmask(0x60000D5c,0x200000)
            if signal == 'tone':
                self.mem.clrmask(0x60000D50,0x1)
            elif signal == 'ofdm':
                self.mem.setmask(0x60000D50,0x1)
                #for sar adc(for chip_5.0's bug)
                self.mem.wrm(0x600005c8,7,0,0x4,'com');
            else :
                print "error: signal must be 'tone' or 'ofdm'"

        else:

            self.mem.wrm(0x6000e05c, 23, 23, 0)  #use pkdet
            self.mem.wrm(0x6000e05c, 21, 21, 0)  #use temperature

            if signal == 'tone':
                self.mem.clrmask(0x6000E050,0x1)
            elif signal == 'ofdm':
                self.mem.setmask(0x6000E050,0x1)
            else :
                loginfo("error: signal must be 'tone' or 'ofdm'")

    def en_pkdet(self):
        self.sar_init()
        if self.chipv == "ESP8266":
            self.mem.setmask(0x60000D5c,0x800000)
            self.mem.clrmask(0x60000D5c,0x200000)
        else:
            self.mem.wrm(0x6000e05c, 23, 23, 1)  #pkdet

    def saradc2pwr(self, offset, cal=False):
        d = rfglobal.saradc;
        if cal:
            d = mfunc.saradc_cal(d)
        # for ---  mem.wr(0x60000D5C,0x0005a8)
        vdc = np.average(d[6:8])
        vsig = np.average(d[1:4])
        vref = np.average(d[4:6])
        print 'vdc=%d, vsig=%d, vref=%d'%(vdc, vsig, vref)
        vs = vref-vdc
        if vs == 0:
            vs = 1
        Pout = 10*np.log10((vsig-vdc)/vs)+offset
        linear_p = ((vsig-vdc)*1024/vs)
        pwr = ('%2.2f'%Pout)
        return [pwr, linear_p]

    def sar_dout(self,num, signal='tone', pwr_dis=0, offset=19):
        if signal == 'tone':
            if self.chipv == 'ESP8266':
                self.mem.clrmask(0x60000D50,0x2)
                self.mem.setmask(0x60000D50,0x2)
            else:
                self.mem.clrmask(0x6000E050,0x2)
                self.mem.setmask(0x6000E050,0x2)
        elif signal == 'ofdm':
            self.wifi.cmdstop()
        else :
            loginfo("error: signal must be 'tone' or 'ofdm'")

        d_str=''
        e=[1,2,3,4,5,6,7,8]
        for i in range(0,num):
            if self.chipv == 'ESP8266':
                c=self.mem.rd(0x60000D80+i*4)&0xfff
            else:
                c=self.mem.rd(0x6000E080+i*4)&0xfff
            e[i] = 4095-c
            d_str = d_str+'%d,'%e[i]
        rfglobal.saradc = e
        if pwr_dis == 0:
            [pwr, linear_p] = self.saradc2pwr(offset)
            d_str += '%s, %d, '%(pwr, linear_p)
            loginfo('pwdet calculated power: %s'%pwr)
            return pwr
        else:
            return d_str

    def saradc2v(self):
        d = rfglobal.saradc;
        vout = np.average(d)/2048.0*1.0
        print vout
        return vout

    def readvdd33(self, atten=0):
        '''Set dmux testpoint and return a voltage.'''
        self.i2c.rftx.TE_PWDET = 1  # Test Enable
        self.i2c.rftx.TR = 0        # select Test Register

        if self.chipv == 'ESP8266':
            self.i2c.saradc.en_test = 1
        else:
            self.mem.wrm(0x6000882c, 4, 4, 1)  #sar2 en test
            self.mem.wrm(0x60008838, 31, 30, atten)
        # SARADC read code
        self.en_pkdet()
        self.sar_dout(8, pwr_dis=1)                 # it saves the codes to rfglobal.saradc
        vdd33 = self.saradc2v() * 4.0      # the testpoint is 1/4 of VDD33
        print vdd33

        self.i2c.rftx.TE_PWDET = 0     # Test Disable

        if self.chipv == 'ESP8266':
            self.i2c.saradc.en_test= 0
        else:
            self.mem.wrm(0x6000882c, 4, 4, 0)  #sar2 en test

        return vdd33

