from hal.common import *
from rftest.rflib.wifi_lib import WIFILIB
from rftest.rflib.pbus import pbus as Pbus
import rftest.rflib.rfglobal as rfglobal
import rftest.rflib.wifi_instrum as rftx
from baselib.loglib.log_lib import *
from pylab import *
import rftest.rflib.wifi_instrum as wifi_instrum
from baselib.instrument import tester

class rfcal(object):
    def __init__(self,comport,chipv='ESP32'):

        self.comport = comport
        self.chipv = chipv
        self.wifi = WIFILIB(self.comport,self.chipv)
        ##self.wifitx = WIFITX(self.comport,self.chipv)
        ##self.wifirx = WIFIRX(self.comport,self.chipv)
        self.pbus = Pbus(self.comport,self.chipv)
        self.mem = MEM(self.comport,self.chipv)


    def tos(self,loop_time=12):
        self.wifi.stoptone()

        dco_max = 0x1ff
        dco_min = 0
        idco_c = 0x100
        qdco_c = 0x100
        idco_f = 0x100
        qdco_f = 0x100
        for stage in range(0, 2):
            idco=0x100;
            qdco=0x100;
            step=124;
            isum=0;
            qsum=0;

            self.pbus.pbus_wr('dcoi','en2',idco);
            self.pbus.pbus_wr('dcoq','en2',qdco);
            print stage

            for i in range(0,loop_time):
                if stage==0:
                    en_str = 'en1'
                else:
                    en_str = 'en2'

                self.pbus.pbus_wr('dcoi', en_str, idco)
                self.pbus.pbus_wr('dcoq', en_str, qdco)
                #enable calibration
                self.mem.wrm(0x6000E04c,23, 0, 0x113cf1)
                #trigger
                self.mem.wrm(0x6000E04c,23, 0,0x113cf3)
                rs   = self.mem.rd(0x6000E04c)
                idir = self.mem.rdm(0x6000E04c,31,31)
                qdir = self.mem.rdm(0x6000E04c,30,30)

                print "i=%d: idco=%d, qdco=%d, step=%d, idir=%d, qdir=%d"%(i,idco,qdco,step, idir,qdir)
                #print 'idir:0x%x qdir:0x%x  %d %d  %d %d  %d %d %d'%(idir>>28,qdir>>28, idco, qdco, step, idco_c, qdco_c, idco_f, qdco_f);

                #if stage==1:
                #    if idir==0: idir = 1
                #    else: idir = 0
                #    if qdir==0: qdir = 1
                #    else: qdir = 0
                if idir==0: idco=idco+step;
                else:       idco=idco-step;
                if qdir==0: qdco=qdco+step;
                else:       qdco=qdco-step;
                if(idco > dco_max):
                    idco=dco_max;
                    print "idco overflow"
                elif(idco < dco_min):
                    idco=dco_min;
                    print "idco overflow"
                if(qdco > dco_max):
                    qdco=dco_max;
                    print "qdco overflow"
                elif(qdco < dco_min):
                    qdco=dco_min;
                    print "qdco overflow"
                if step!=2: step=(step>>1)+1;
                else: step = 1;

                if(i>=(loop_time-4)):
                    isum = isum + idco;
                    qsum = qsum + qdco;
            idco = (isum + 2) >> 2
            qdco = (qsum + 2) >> 2

            self.pbus.pbus_wr('dcoi', en_str, idco)
            self.pbus.pbus_wr('dcoq', en_str, qdco)

            if stage==0:
                idco_c = idco
                qdco_c = qdco
            else:
                idco_f = idco
                qdco_f = qdco

        self.mem.wrm(0x6000E04c,23, 0,0x113cf0)
        self.mem.wrm(0x600060a0, 17, 16, 3)  #tx clock force
        rfglobal.tos_dac = [idco_c, qdco_c, idco_f, qdco_f]    # [czwang, 2012/09/11] save calibration result
        return [idco_c, qdco_c, idco_f, qdco_f];

    def tos_esp8266(self,loop_time=12):
        idco=0x40;
        qdco=0x40;
        step=28;
        isum=0;
        qsum=0;
        try:
            self.wifi.stoptone()
        except:
            pass
        #pbus.pbus('txbb2', 'en1', 0x7F)    # [czwang, 2012/09/11] disable the gain setting
        for i in range(0,loop_time):
            self.pbus.pbus('txbb2','en2',qdco);
            print 'idco:%d'%idco;
            self.pbus.pbus('txbb1','en2',idco);
            #enable calibration
            self.mem.wr(0x60000d4c,0x1113cf1)
            #trigger
            self.mem.wr(0x60000d4c,0x1113cf3)
            rs   = self.mem.rd(0x60000d4c)
            idir = rs & 0x80000000;
            qdir = rs & 0x40000000;
            print 'idir:0x%x qdir:0x%x '%(idir>>16,qdir>>16);
            if idir==0: idco=idco+step;
            else:       idco=idco-step;
            if qdir==0: qdco=qdco+step;
            else:       qdco=qdco-step;
            if(idco > 127):
                idco=127;
                print "idco overflow"
            elif(idco < 0):
                idco=0;
                print "idco overflow"
            if(qdco > 127):
                qdco=127;
                print "qdco overflow"
            elif(qdco < 0):
                qdco=0;
                print "qdco overflow"
            if step!=2: step=(step>>1)+1;
            else: step = 1;

            if(i>=(loop_time-4)):
                isum = isum + idco;
                qsum = qsum + qdco;
        idco = (isum + 2) >> 2;
        qdco = (qsum + 2) >> 2;
        self.pbus.pbus('txbb2','en2',qdco);
        print 'idco:%d'%idco;
        self.pbus.pbus('txbb1','en2',idco);
        #pbus.pbus('txbb2', 'en1', 0x7F)    # [czwang, 2012/09/11] disable the gain setting
        self.mem.wr(0x60000d4c,0x1113cf0);
        rfglobal.tos_dac = [idco, qdco]   # [czwang, 2012/09/11] save calibration result
        print [idco,qdco]
        return [idco,qdco];
##    def tos_dig(self,loop_time=20):
##
##        self.pbus.set_dco()
##        self.mem.wrm(0x600060a0, 17, 16, 3)  #tx clock force
##
##        dco_max = 100
##        dco_min = -100
##
##        idco=0;
##        qdco=0;
##        step=10;
##        isum=0;
##        qsum=0;
##
##        for i in range(0,loop_time):
##
##            self.wifi.set_dig_txdc(idco, qdco)
##
##            #enable calibration
##            self.mem.wrm(0x6000E04c,23, 0, 0x113cf1)
##            #trigger
##            self.mem.wrm(0x6000E04c,23, 0,0x113cf3)
##            rs   = self.mem.rd(0x6000E04c)
##            idir = self.mem.rdm(0x6000E04c,31,31)
##            qdir = self.mem.rdm(0x6000E04c,30,30)
##
##            print "i=%d: idco=%d, qdco=%d, step=%d, idir=%d, qdir=%d"%(i,idco,qdco,step, idir,qdir)
##
####            if idir==0: idco=idco-step;
####            else:       idco=idco+step;
####            if qdir==0: qdco=qdco-step;
####            else:       qdco=qdco+step;
##            if(idco > dco_max):
##                idco=dco_max;
##                print "idco overflow"
##            elif(idco < dco_min):
##                idco=dco_min;
##                print "idco overflow"
##            if(qdco > dco_max):
##                qdco=dco_max;
##                print "qdco overflow"
##            elif(qdco < dco_min):
##                qdco=dco_min;
##                print "qdco overflow"
####            if step!=2: step=(step>>1)+1;
####            else: step = 1;
##
##            if(i>=(loop_time-4)):
##                isum = isum + idco;
##                qsum = qsum + qdco;
##
##        idco = (isum + 2) >> 2
##        qdco = (qsum + 2) >> 2
##
##        self.wifi.set_dig_txdc(idco, qdco)
##
##        self.mem.wrm(0x6000E04c,23, 0,0x113cf0)
##        self.mem.wrm(0x600060a0, 17, 16, 3)  #tx clock force
##
##        return [idco, qdco];


    def txiq_cal(self, cable_lose=2,iqv_no=1):
        chan = 14
        freq = self.wifi.chan2freq(chan)
        self.wifi.rfchsel(chan)
        self.wifi.cmdstop()
##        max_pwr = 25 - cable_lose
        max_pwr = 25
        rate = 'mcs7'
        self.wifi.txout(rate)
        test_para = wifi_instrum.test_para(rate)
        myiqv=tester.tester(freq, max_pwr, rate, test_para, iqv_no,'measure', cable_lose, 10,1,1,20)
        iq_amp = 0
        iq_phase = 0
        scale_amp = 0
        scale_phase = 0
        for i in range(20):
            self.wifi.txiq_set(en=1, txiq_gain=iq_amp, txiq_phase=iq_phase)
            self.wifi.txout(rate)
            [pwr, freq_err, clk_err, evm, evm_std, evm_max, lo_leakage,iq_imb_amp,iq_imb_phase, evm_list] = wifi_instrum.iqv_avg(myiqv, 1,'false')
            if (iq_imb_amp > -0.05 and iq_imb_amp < 0.05) and (iq_imb_phase > -0.5 and iq_imb_phase < 0.5):
                break
            if (iq_imb_amp <= -0.05 or iq_imb_amp >= 0.05):
                scale_amp = int(iq_imb_amp/0.05)
                print scale_amp
                iq_amp += scale_amp
            if (iq_imb_phase <= -0.5 or iq_imb_phase >= 0.5):
                scale_phase =  int(iq_imb_phase/0.5)
                iq_phase += scale_phase
        print [i, iq_imb_amp, iq_imb_phase, scale_amp, scale_phase,iq_amp,iq_phase]
        return [iq_amp,iq_phase]



