#from hal.Init             import HALS
#from rftest.testcase.Init import RFTCS
import pandas            as pd
import scipy.signal      as sgnl
import numpy             as np
import matplotlib.pyplot as plt
from hal.Init import HALS
import baselib.loglib.log_lib   as loglib
import platform

class bbadc:
    def __init__(self, channel, chipv='CHIP722'):
        self.channel = channel
        self.chipv = chipv
        self.chip = HALS(self.channel, self.chipv)
##        loglib.logsetlevel('ERROR')
        if platform.platform().find("Linux") != -1:
            plt.ion()

    def bb_init(self,mode=0,bbpll_mode='480M'):
        # sw_rxtx    0    1
        #            TX   RX
        self.chip.HWI2C.bbtop.dac_ck_ph_inv = 1

        self.chip.HWI2C.bbpll.bbadc_div = 2 #adc smp clock, 1->160M, 2->80M, 3->40M
        self.chip.MEM.wrm(0x600060a0, 17, 16, 3) #force tx on
        self.chip.MEM.wrm(0x600060a0, 15, 14, 3) #force rx on
        self.chip.MEM.wrm(0x600060a0, 24, 24, 1) #pbus_bb_swap
        self.chip.MEM.wrm(0x60005114,  9,  9, 0) #turn off phase learning

        if bbpll_mode == '480M':
            self.chip.comport.req_com('rtc_clk_cpu_freq_set 1')
            self.chip.HWI2C.bbpll.mode_hf = 1
            self.chip.HWI2C.bbpll.div_dac = 0
            self.chip.mem.wrm(0x600050ec,27,27,0) # digital dac clock, 1->320M, 0->160M
        elif bbpll_mode == '320M':
            self.chip.comport.req_com('rtc_clk_cpu_freq_set 5')
            self.chip.HWI2C.bbpll.mode_hf = 0
            self.chip.HWI2C.bbpll.div_dac = 1
            self.chip.mem.wrm(0x600050ec,27,27,1) # digital dac clock, 1->320M, 0->160M
        else:
            raise Error('wrong bbpll mode')

        self.chip.HWI2C.bbpll.bbadc_dcur   = 1
        self.chip.HWI2C.bbpll.bbadc_delay1 = 1
        self.chip.HWI2C.bbpll.bbadc_delay2 = 3
        self.chip.HWI2C.bbpll.bbadc_dvdd   = 1

        self.chip.PBUS.pbus_debugmode()
        self.chip.HWPBUS.BB1.EN1  = 0x100
        self.chip.HWPBUS.DCOI.CK1 = 255
        self.chip.HWPBUS.DCOI.CK2 = 255
        self.chip.HWPBUS.DCOQ.CK1 = 255
        self.chip.HWPBUS.DCOQ.CK2 = 255
        self.chip.HWPBUS.BB1.EN1  = 0x000
        self.chip.HWPBUS.DCOI.CK1 = 255
        self.chip.HWPBUS.DCOI.CK2 = 255
        self.chip.HWPBUS.DCOQ.CK1 = 255
        self.chip.HWPBUS.DCOQ.CK2 = 255

        if mode==0: # dac,flt,adc
            self.chip.HWPBUS.RFRX1.EN1 = 0x001
            self.chip.HWPBUS.RFTX1.EN1 = 0x000
            self.chip.HWPBUS.RFTX2.EN1 = 0x000
            self.chip.HWPBUS.BB1.EN1   = 0x100
            self.chip.HWPBUS.BB1.EN1   = 0x1c9
            self.chip.HWPBUS.BB1.EN2   = 0x030
            self.chip.HWI2C.bbtop.enlb = 0
            self.chip.MEM.wrm(0x600050dc, 11, 11, 0) #txiq disable
            self.chip.MEM.wrm(0x600050dc, 27, 27, 0) #rxiq disable

        if mode==1: # loop back
            self.chip.HWPBUS.RFRX1.EN1 = 0x105
            self.chip.HWPBUS.RFTX1.EN1 = 0x07f
            self.chip.HWPBUS.RFTX2.EN1 = 0x05f
            self.chip.HWPBUS.BB1.EN1   = 0x1f9
            self.chip.HWPBUS.BB1.EN2   = 0x000
            self.chip.HWI2C.bbtop.enlb    = 1
            self.chip.HWI2C.RFRX.LB_MODE  = 1
            self.chip.HWI2C.RFTX.LB_EN    = 1
            self.chip.HWI2C.RFTX.LB_EN_IQ = 1
            self.chip.HWI2C.RFTX.LB_GCT   = 1
            #self.chip.HWI2C.RFRX.filter_rx_en_bias_input = 1
        if mode==2: # rx
            self.chip.HWPBUS.RFRX1.EN1 = 0x184
            self.chip.HWPBUS.RFTX1.EN1 = 0x000
            self.chip.HWPBUS.RFTX2.EN1 = 0x000
            self.chip.HWPBUS.BB1.EN1   = 0x188
            self.chip.HWPBUS.BB1.EN1   = 0x189
            self.chip.HWPBUS.BB1.EN2   = 0x000
        if mode==3: # tx
            self.chip.HWPBUS.RFRX1.EN1 = 0x001
            self.chip.HWPBUS.RFTX1.EN1 = 0x07f
            self.chip.HWPBUS.RFTX2.EN1 = 0x05f
            self.chip.HWPBUS.BB1.EN1   = 0x07c
            self.chip.HWPBUS.BB1.EN2   = 0x030

    def adcDump2(self,numSmp=1024,enPlot=True,enReturn=True,en80M=1,fsmp=80e6,fig=None):
        '''very slow when dump large amount data, suggest adcDump'''
        self.chip.MEM.wrm(0x6001c0b8,2,0,1)
        self.chip.MEM.wrm(0x60006090,1,0,0)
        curr_ptr,wrap_flag,buff_start,buff_size = self.chip.wifiapi.adctrig(numSmp,'sw',en80M)
        if wrap_flag:
            raise Error('wrap_flag!')
        #print(curr_ptr,wrap_flag,buff_start,buff_size)
        adc_i = []
        adc_q = []
        for i in range(numSmp):
            raw_data = self.chip.MEM.rd(buff_start+i*4)
            data_q =  raw_data      & 0x3ff
            data_i = (raw_data>>10) & 0x3ff
            #rx_gain  = (raw_data>>20) & 0x7f
            #rx_err   = (raw_data>>27) & 0x1
            #agc_st   = (raw_data>>28) & 0xf
            #vga_sat  = (raw_data>>20) & 0x1
            #lna_sat  = (raw_data>>21) & 0x1
            adc_i.append([data_i,data_i-1024][data_i>=512])
            adc_q.append([data_q,data_q-1024][data_q>=512])
        if enPlot:
            if fig is None:
                fg,fx=plt.subplots()
            else:
                fx = fig
            x = np.arange(numSmp)/fsmp
            fx.step(x,adc_i,label='adc i')
            fx.step(x,adc_q,label='adc q')
            fx.legend()
            fx.grid(True)
        if enReturn:
            return np.array(adc_i),np.array(adc_q)

    def adcDump(self,numSmp=1024,mode='10bit',enPlot=True,enReturn=True,en80M=1,
                fsmp=80e6,fig=None):
        self.chip.MEM.wrm(0x6001c0b8,2,0,1)
        self.chip.MEM.wrm(0x600050d0,24,24,1) # sync
        if mode=='10bit':
            self.chip.MEM.wrm(0x60006090,1,0,0) # 0:10bit,1:13bit
        elif mode=='13bit':
            self.chip.MEM.wrm(0x60006090,1,0,1) # 0:10bit,1:13bit
            self.chip.MEM.wrm(0x600050d0,29,29,0) # dump sel
            self.chip.MEM.wrm(0x6001c0b8,1,0,0)
            def decode(raw):
                data_bin = '{:013b}'.format(raw)
                data_lst1 = [c for i,c in enumerate(data_bin) \
                             if i in [0,1,2,4,5,6,8,9,10,12]]
                data_lst2 = ['%s00'%c for i,c in enumerate(data_bin) \
                             if i in [3,7,11]]
                data_str1 = ''.join(data_lst1)
                data_str2 = ''.join(data_lst2)[:-1]
                data = int(data_str1,2) + int(data_str2,2)
                return data
        else:
            raise ValueError('invalid mode')
        curr_ptr,wrap_flag,buff_start,buff_size = self.chip.wifiapi.adctrig(numSmp,'sw',en80M)
        burst_len = 0x1000
        if wrap_flag:
            raise Error('wrap_flag!')
        seg = int(np.ceil(numSmp*4.0/burst_len))
        adc_i = []
        adc_q = []
        #print(curr_ptr,wrap_flag,buff_start,buff_size)
        for i in range(seg):
            result_lst = self.chip.MEM.rdmem(buff_start+i*burst_len,burst_len)
            for res in result_lst:
                hex_data = int(res,16)
                if mode=='10bit':
                    data_q =  hex_data      & 0x3ff
                    data_i = (hex_data>>10) & 0x3ff
                    adc_i.append([data_i,data_i-1024][data_i>=512])
                    adc_q.append([data_q,data_q-1024][data_q>=512])
                elif mode=='13bit':
                    data_q = decode( hex_data      & 0x1fff)
                    data_i = decode((hex_data>>13) & 0x1fff)
                    adc_i.append(data_i)
                    adc_q.append(data_q)
        adc_i, adc_q = adc_i[:numSmp], adc_q[:numSmp]
        if enPlot:
            if fig is None:
                fg,fx=plt.subplots()
            else:
                fx = fig
            x = np.arange(numSmp)
            #x = np.arange(numSmp)/fsmp
            fx.step(x,adc_i,label='adc i')
            fx.step(x,adc_q,label='adc q')
            fx.legend()
            fx.grid(True)
        if enReturn:
            return np.array(adc_i),np.array(adc_q)

    def spectrum(self,din,fsmp,nfft=None,window='blackman',prominence=20,wlen=7,
                 enPlot=True,enReturn=True,fig=None):
        f,psd   = sgnl.periodogram(din,fsmp,window,nfft,scaling='spectrum')
        arg     = f.argsort()

        f       = f[arg]
        psd     = psd[arg]
        psd_log = 10*np.log10(psd)

        peaks, ppt = sgnl.find_peaks(psd_log, prominence=prominence, wlen=wlen)

        if enPlot:
            if fig is None:
                fg,fx = plt.subplots()
            else:
                fx = fig
            fx.plot(f,psd_log)
            fx.plot(f[peaks],psd_log[peaks],'x')
            fx.vlines(x=f[peaks], ymin=psd_log[peaks] - ppt["prominences"],
                      ymax = psd_log[peaks], color = "C1")
            fx.hlines(y=psd_log[peaks]-ppt["prominences"], xmin=f[ppt['left_bases']],
                      xmax = f[ppt['right_bases']], color='C1')
            fx.grid(True)

        if enReturn:
            peak_args = psd_log[peaks].argsort()[::-1]
            peak_ranges = zip(ppt['left_bases'][peak_args],ppt['right_bases'][peak_args])
            result = {'freq': f,
                      'psd': psd,
                      'psd_log': psd_log,
                      'peak_ranges': peak_ranges
                     }
            return result

    def power_cal(self, psd_info):
        psd         = psd_info['psd']
        peak_ranges = psd_info['peak_ranges']

        total_pwr = np.sum(psd)
        tone_pwr  = [np.sum(psd[range(i[0],i[1]+1)]) for i in peak_ranges]
        noise_pwr = total_pwr - np.sum(tone_pwr)
        sgnl_pwr  = tone_pwr[0]
        sfdr      = 10*np.log10(sgnl_pwr/noise_pwr)
        snr       = 10*np.log10(sgnl_pwr/(total_pwr-sgnl_pwr))

        return {'total_pwr': total_pwr,
                'tone_pwr' : tone_pwr,
                'noise_pwr': noise_pwr,
                'sfdr'     : sfdr,
                'snr'      : snr}

    def run_rx(self):
        window = 'blackman'
        fsmp = 80e6
        fg,fx = plt.subplots()
        self.chip.MEM.wrm(0x600060b8,21,21,1)
        self.chip.MEM.wrm(0x600050e8,23,16,0) #adc scale disable
        adc_i,adc_q = self.adcDump(2**10,mode='13bit',enPlot=1)
        adc_i = adc_i - np.average(adc_i)
        adc_q = adc_q - np.average(adc_q)
        adc = 1J*adc_i + adc_q
        #res = self.spectrum(adc_i,fsmp,prominence=12,enReturn=1,enPlot=1,fig=fx)
        res = self.spectrum(adc,fsmp,prominence=12,enReturn=1,enPlot=1,fig=fx)
        pwr = self.power_cal(res)
        print ''
        print 'sfdr',pwr['sfdr']
        print 'snr',pwr['snr']
        print 'noise',pwr['noise_pwr']
        print 'total',pwr['total_pwr']
        print 'signal',pwr['tone_pwr'][0]
        print 'amplitude',adc_i.max()-adc_i.min(),adc_q.max()-adc_q.min()

    def run(self,freq,atten):
        fsmp = 80e6
        window = 'blackman'
        fg,fx = plt.subplots()
        for en in [1]:#range(-15,15):
        #for atten in [0,1]:#range(-15,15):
            self.chip.wifi.txtone(en, freq, atten)
            self.chip.MEM.wrm(0x600060b8,21,21,1)
            self.chip.MEM.wrm(0x600050e8,23,16,0) #adc scale disable
            adc_i,adc_q = self.adcDump(2**10,mode='13bit',enPlot=1)
            adc_i = adc_i - np.average(adc_i)
            adc_q = adc_q - np.average(adc_q)
            adc = 1J*adc_i + adc_q
            #res = self.spectrum(adc_i,fsmp,prominence=12,enReturn=1,enPlot=1,fig=fx)
            res = self.spectrum(adc,fsmp,prominence=12,enReturn=1,enPlot=1,fig=fx)
            pwr = self.power_cal(res)
            print ''
            print 'sfdr',pwr['sfdr']
            print 'snr',pwr['snr']
            print 'noise',pwr['noise_pwr']
            print 'total',pwr['total_pwr']
            print 'signal',pwr['tone_pwr'][0]
            print 'amplitude',adc_i.max()-adc_i.min(),adc_q.max()-adc_q.min()


