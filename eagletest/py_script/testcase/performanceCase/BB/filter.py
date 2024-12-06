#from hal.Init             import HALS
#from rftest.testcase.Init import RFTCS
import pandas            as pd
import scipy.signal      as sgnl
import numpy             as np
import matplotlib.pyplot as plt
import scipy.interpolate as intp

import baselib.loglib.log_lib   as loglib
from hal.Init import HALS
from baselib.test_channel.com import COM as com

from baselib.instrument import dm,sme
import time

from bbadc import bbadc

class filter(object):
    def __init__(self, channel, chipv = "AUTO"):
        self.chip = HALS(channel, chipv)
        self.channel = self.chip.channel
        self.chipv = self.chip.chipv
        self.bbadc = bbadc(self.channel, self.chipv)
##        loglib.logsetlevel('ERROR')
        plt.ion()


    def rc_cal(self, bw=9.5, xtal='40M'):
        if xtal == '40M':
            self.chip.HWI2C.bias.rc_div = 11
        elif xtal == '26M':
            self.chip.HWI2C.bias.rc_div = 7
        elif xtal == '24M':
            self.chip.HWI2C.bias.rc_div = 6
        else:
            raise ValueError('WRONG XTAL')
        self.chip.HWI2C.bias.rc_chg_count = 2
        self.chip.HWI2C.bias.rc_dvref = 2

        self.chip.HWI2C.xtal.xpd_rc = 1
        self.chip.HWI2C.bias.xpd_rc = 1

        self.chip.HWI2C.bias.rc_start = 0
        self.chip.HWI2C.bias.rc_rstb = 0
        self.chip.HWI2C.bias.rc_rstb = 1
        self.chip.HWI2C.bias.rc_start = 1

        rc = self.chip.HWI2C.bias.rc_cap
        dcap = int(round(5.7*(rc+56)/bw - 6.2))

        self.chip.HWI2C.xtal.xpd_rc = 0
        self.chip.HWI2C.bias.xpd_rc = 0

        dcap_str_lst = ['filter_wifi%sx%d_dcap_%sq'%(rt, num, lh) \
                           for rt in ['r','t'] \
                           for num in range(4) \
                           for lh in ['l','h']]
        for dcap_str in dcap_str_lst:
            setattr(self.chip.HWI2C.bbtop, dcap_str, dcap)
        print('bw=%.1f, rc=%d, dcap=%d'%(bw,rc,dcap))
    def sweep_bw(self, stop=15, step=0.5):
        self.chip.MEM.wrm(0x600060b8,21,21,1)
        self.chip.MEM.wrm(0x600050e8,23,16,0) #adc scale disable

        self.s = sme.sme()
        #self.s.setpow(0)

        freq_lst = np.arange(-stop,stop,step)
        dg_lst = [0x000,0x020,0x030,0x038,0x03c,0x03e,0x03f]
        pw_lst = [0, -6, -12, -18, -24, -30, -36]

        self.s.setfreq(2432e6)
        fg,fx = plt.subplots(2)
        self.chip.PBUS.pbus_debugmode()
        for dg,pw in zip(dg_lst[:2],pw_lst[:2]):
            var_i = []
            var_q = []
            self.s.setpow(-10)
            self.chip.HWPBUS.BB1.EN2 = dg
            for freq in freq_lst:
                self.chip.rfpll.set_freq(2432+freq)
                adc_i,adc_q = self.bbadc.adcDump(2**10,mode='13bit',enPlot=0)
                var_i.append(np.var(adc_i))
                var_q.append(np.var(adc_q))
                print(freq,var_i[-1],var_q[-1])
            fx[0].plot(freq_lst, 10*np.log10(var_i), label=hex(dg))
            fx[1].plot(freq_lst, 10*np.log10(var_q), label=hex(dg))
        for i in [0,1]:
            fx[i].grid(True)
            fx[i].legend()

    def bbflt(self, fsig=1e6, bw=19.5e6, enPlot=1):
        frange = np.arange(-25e6, 25e6, 5001)
        wrange = 2*np.pi*frange

        flt = sgnl.filter_design.cheby1(N=5,rp=0.5,Wn=bw*np.pi*2,analog=True)
        print flt
        print flt[0]
        print flt[1]
        _, flt_value = sgnl.freqs(flt[0], flt[1], wrange)
        mag = 20*np.log10(np.abs(flt_value))
        phase = np.angle(flt_value,0)

        for i in range(len(frange)-1):
            if (phase[i+1]-phase[i]) > 6:
                phase[i+1:] -= 2*np.pi
            elif (phase[i+1]-phase[i]) < -6:
                phase[i+1:] += 2*np.pi
        phase += 2*np.pi

        fun_phase = intp.InterpolatedUnivariateSpline(wrange, phase)
        fun_groupDelay = fun_phase.derivative()

        if enPlot:
            #plt.ion()
            fg,fx = plt.subplots(2)
            fx[0].plot(frange, mag, label='magnitude')
            #fx[1].plot(frange, phase)
            fx[1].plot(frange, -fun_groupDelay(wrange),label='group delay(phase derivative)')
            fx[1].plot(frange, -phase/wrange, label='phase/w')

            for i in range(2):
                fx[i].grid(True)
                fx[i].legend()
            plt.show()

        return fun_groupDelay(fsig)


class rfpll_vcon_measure:
    def __init__(self, channel, chipv='chip722'):
        self.chip = channel
        loglib.logsetlevel('ERROR')
        if platform.platform().find("Linux") != -1:
            plt.ion()

        self.chip.comport.req_com('pull_internal_voltage 0')
    def measure(self,freq):
        self.chip.rfpll.set_freq(freq)
        dcap = self.chip.HWI2C.rfpll.or_pll_cap
        dac  = self.chip.HWI2C.rfpll.or_pll_dac

        vout = []
        for ent1,ent2 in [[1,0],[0,1],[0,0]]:
            self.chip.HWI2C.rfpll.ent_vco      = ent1
            self.chip.HWI2C.rfpll.ent_vco_bias = ent2
            if ent1+ent2 !=0:
                for dtest in range(4):
                    self.chip.HWI2C.rfpll.dtest = dtest
                    vv = dm.dm()
                    _vv=vv.get_result('VDC')

                    time.sleep(2)
                    vout.append(_vv)

        keys = ['%s_%d'%(ent,dtest) for ent in ['ent_vco','ent_vco_bias'] \
                                    for dtest in range(4)]

        val = {'freq':freq,'dcap':dcap,'dac':dac}
        val.update({k:v for k,v in zip(keys,vout)} )
        return val
    def repeat(self):
        data=[]
        for freq in np.arange(2550,2560.5,0.1):
            data.append(self.measure(freq))
        data = pd.DataFrame(data)
        return data
    def process_data(self, data):
        fg,fx = plt.subplots()
        for dcap in range(0,60):
            selected = data[data.dcap==dcap]
            vcon = selected.ent_vco_0
            freq = selected.freq
            fx.plot(vcon, freq, label='dcap=%d'%dcap)
        fx.set_xlabel('vcon')
        fx.set_ylabel('freq')
        fx.legend()
        fx.grid(True)
        return fg,fx


