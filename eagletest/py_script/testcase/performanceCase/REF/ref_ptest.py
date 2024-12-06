# -- coding: utf-8 --
# 中文支持

from baselib.instrument.dm import dm
from baselib.loglib.log_lib import *
from hal.Init import HALS
from hal.common import CHIP_ID
from baselib.instrument import awg
from baselib.tc_platform.common import *
from baselib.tc_platform.tc_platform import *
from baselib.test_channel.com import COM
from collections import OrderedDict
import csv
import re
import scipy.optimize as opt
import matplotlib.pyplot as plt
import pandas as pd
import time

class RefPtest(object):
    """
    用于 Internal Reference Signal 遍历测试： 

    """
    def __init__(self, channel, irc,chipv = "AUTO"):
        self.chip    = HALS(channel, chipv)
        self.channel = self.chip.channel
        self.chipv   = self.chip.chipv
        self.irc     = irc

    def prepGPIB(self):
        '''
        :brief:
            Communication between instrument and PC by USB-GPIB interface
        :param:
            - dm_vol: Voltage test
        '''
        self.mydm = dm(num_of_machine=0)

    def pvt_test(self,dig_dbias=0,pvt_res_en=0,pvt_delay=400,timeout=1):
        '''
        :brief: tested on-chip pvt detector, output value indicates chip corner
        :param:
            - dig_dbias: configs digital ldo voltage level 0-7
                - typical is 4 and voltage level 1.06V
                - 0: voltage level drops to 0.86V
                - 7: voltage levle raise up to 1.214V
            - pvt_res_en: not sure what's the purpose here
            - pvt_delay:  not sure function either
        '''
        self.channel.req_com("pvt_pwr %d"%1)
        pvt_read = self.channel.req_com("pvt_det %d %d %d"%(dig_dbias,pvt_res_en,pvt_delay),timeout)
        print 'PVT Setup: dig_dbias=%s\nPVT Reads: %s'%(dig_dbias,pvt_read)
        #turns off pvt sensor, and dig_dbias sets back to 4
        self.channel.req_com("pvt_pwr %d"%0)
        return [['PVT_DIG_DBIAS_%d'% dig_dbias],[pvt_read]]
    
    def rtc_sleep(self, slp_mode = 127, wakeup_mode = 0, reject_mode = 0, 
                  dbg = 0, rtc_dbias = 1, dig_dbias = 0):
        '''
        :brief:
            - This is a special command,not applied to all bin
            - Can be used to check dbg, rtc_dbias & dig_dbias sweep 
        '''
        timeout = 1
        self.channel.req_com('rtc_sleep_dbg_dbias %d %d %d %d %d %d' 
            % (slp_mode, wakeup_mode, reject_mode, dbg, rtc_dbias, dig_dbias), timeout)

    def refread(self, igmcode=0, outcode =1, iphcode =1, vgtcode=1):
        '''
        :brief:
            - reads all test mux available reference signal
            - sweeps I2C regs to check voltage level
        :param:
            - dref_igm: default value is 1, if change to 0, 
                - expect to see when ent_cpreg =1, dtest=2 value equals dtest=3 value 
        '''
        self.prepGPIB()
        log = csvreport('/brokenChip/vbg_sweep')
        col_ls = [
            'dref_igm','ref_out_buf','iph','vgate_buf'
            'case',
            '1V reference',
            'rtc',
            'dig',
            'sar1',
            'sar2',
            'vcm']
        for reg_n in ['ent_cgm', 'ent_consti', 'ent_cpreg']:
            for i in np.arange(0,4):
                #if   reg_n is 'ent_cgm'   and i == 2: continue
                if reg_n is 'ent_cpreg' and i == 1: continue 
                col_ls.append('%s_%s'%(reg_n,i))
        col_ls.append('o_done_flg')
        col_ls.append('bg_o_done_flg')
        self.chip.rtc_debug.pull_internal_voltage(0)
        
        def readVol(ext_code='origin'):
            self.chip.HWI2C.bias.ent_cgm = 1
            self.chip.HWI2C.bias.dtest = 1
            # v_1V = np.float(self.mydm.get_result('VDC')) * 1000
            v_1V = self.irc.vol_meas() * 1000
            self.chip.HWI2C.bias.ent_cgm = 0
            self.chip.HWI2C.bias.dtest = 0
            #start to measure test mux
            self.chip.rtc_debug.set_test_mux(0, 0)
            # v_sar2 = np.float(self.mydm.get_result('VDC')) * 1000
            v_sar2 = self.irc.vol_meas() * 1000
            self.chip.rtc_debug.set_test_mux(1, 0)
            # v_rtc = np.float(self.mydm.get_result('VDC')) * 1000
            v_rtc = self.irc.vol_meas() * 1000
            self.chip.rtc_debug.set_test_mux(1, 1)
            # v_sar1 = np.float(self.mydm.get_result('VDC')) * 1000
            v_sar1 = self.irc.vol_meas() * 1000
            self.chip.rtc_debug.set_test_mux(1, 2)
            # v_dig = np.float(self.mydm.get_result('VDC')) * 1000
            v_dig = self.irc.vol_meas() * 1000
            self.chip.rtc_debug.set_test_mux(1, 3)
            # v_vcm = np.float(self.mydm.get_result('VDC')) * 1000
            v_vcm = self.irc.vol_meas() * 1000
            self.chip.MEM.wrm(1610645688, 29, 28, 0)
            vol_ls = [v_1V, v_rtc, v_dig, v_sar1, v_sar2, v_vcm]
            #i2c sweep
            self.chip.rtc_clk.set_cpu_freq(0)
            #option configuration
            self.chip.HWI2C.bias.dref_igm                = igmcode
            self.chip.HWI2C.ulp.ir_force_xpd_ref_out_buf = outcode
            self.chip.HWI2C.ulp.ir_force_xpd_iph         = iphcode
            self.chip.HWI2C.ulp.ir_force_xpd_vgate_buf   = vgtcode
            for reg_n in ['cgm', 'consti', 'cpreg']:
                setattr(self.chip.HWI2C.bias,'ent_%s'%reg_n,1)
                for i in np.arange(0,4):
                    #if   reg_n is 'cgm' and i == 2: continue
                    if reg_n is 'cpreg' and i == 1: continue
                    self.chip.HWI2C.bias.dtest = i
                    print 'I2C writes ent_%s_%s'%(reg_n,i)
                    time.sleep(0.2)
                    # vol_m = np.float(self.mydm.get_result('VDC'))*1000
                    vol_m = self.irc.vol_meas() * 1000
                    vol_ls.append(vol_m)
                setattr(self.chip.HWI2C.bias,'ent_%s'%reg_n,0)
            o_done_flg = self.chip.HWI2C.ulp.o_done_flag
            bg_o_done_flg = self.chip.HWI2C.ulp.bg_o_done_flag
            vol_ls.append(o_done_flg)
            vol_ls.append(bg_o_done_flg)
            return vol_ls

        print 'original read'
        vol_ls = readVol(ext_code = 'origin')
        vol_ls.insert(0,igmcode)
        vol_ls.insert(1,outcode)
        vol_ls.insert(2,iphcode)
        vol_ls.insert(3,vgtcode)
        log.write_value(col_ls, vol_ls)
        log.flush_line()
        print 'I2C config: igm =%d, out =%d, iph =%d, vgate =%d'%(igmcode,outcode,iphcode,vgtcode)

    def vbg_sweep(self, ext_code):
        '''
        :brief:
            - sweeps ext_code to for slave bandgap recalibration
        :param:
            - ext_code: range 0 -255
        '''
        self.prepGPIB()
        log = csvreport('/brokenChip/vbg_sweep')
        col_ls = [
            'ext_code',
            '1V reference',
            'rtc',
            'dig',
            'sar1',
            'sar2',
            'vcm']
        self.chip.rtc_debug.pull_internal_voltage(0)
        logwarn('Signal Export to CHIP722: ADC2_CH0/GPIO11')
        
        def readVol(ext_code):
            self.chip.HWI2C.bias.ent_cgm = 1
            self.chip.HWI2C.bias.dtest = 1
            # v_1V = np.float(self.mydm.get_result('VDC')) * 1000
            v_1V = self.irc.vol_meas() * 1000
            self.chip.HWI2C.bias.ent_cgm = 0
            self.chip.HWI2C.bias.dtest = 0
            self.chip.rtc_debug.set_test_mux(0, 0)
            # v_sar2 = np.float(self.mydm.get_result('VDC')) * 1000
            v_sar2 = self.irc.vol_meas() * 1000
            self.chip.rtc_debug.set_test_mux(1, 0)
            # v_rtc = np.float(self.mydm.get_result('VDC')) * 1000
            v_rtc = self.irc.vol_meas() * 1000
            self.chip.rtc_debug.set_test_mux(1, 1)
            # v_sar1 = np.float(self.mydm.get_result('VDC')) * 1000
            v_sar1 = self.irc.vol_meas() * 1000
            self.chip.rtc_debug.set_test_mux(1, 2)
            # v_dig = np.float(self.mydm.get_result('VDC')) * 1000
            v_dig = self.irc.vol_meas() * 1000
            self.chip.rtc_debug.set_test_mux(1, 3)
            # v_vcm = np.float(self.mydm.get_result('VDC')) * 1000
            v_vcm = self.irc.vol_meas() * 1000
            self.chip.MEM.wrm(1610645688, 29, 28, 0)
            vol_ls = [
                ext_code,
                v_1V,
                v_rtc,
                v_dig,
                v_sar1,
                v_sar2,
                v_vcm]
            return vol_ls

        print 'original read'
        vol_ls = readVol(ext_code = 'origin')
        log.write_value(col_ls, vol_ls)
        log.flush_line()
        o_code = self.chip.HWI2C.ulp.o_code
        for i in np.arange(o_code, ext_code):
            self.chip.HWI2C.ulp.ext_code = i
            self.chip.HWI2C.ulp.ir_force_code = 1
            time.sleep(0.1)
            print 'ext_code =%d read' % i
            vol_ls = readVol(ext_code = i)
            log.write_value(col_ls, vol_ls)
            log.flush_line()
    
    def vbg_plot(gd_file = None, bd_file = None):
        '''
        :brief:
            - used to plot above vbg_sweep function results
            - need to change data log file name & address below by hand
        '''
        plt.ion()
        bd_file = '/home/test/chip/eagletest/py_script/log/brokenChip/vbg_sweep_2019_03_21_15_14_58.csv'
        gd_file = '/home/test/chip/eagletest/py_script/log/brokenChip/godpart#1_sckt3.csv'
        vbg_bd = pd.read_csv(bd_file)
        vbg_gd = pd.read_csv(gd_file)
        x_bd = np.array(vbg_bd['ext_code'][1:], dtype = float)
        x_gd = np.array(vbg_gd['ext_code'][1:], dtype = float)
        plt.scatter(x_bd, vbg_bd['1V reference'][1:], label = 'BadPart_1V', c = 'r', marker = 'x')
        plt.scatter(x_bd, vbg_bd['rtc'][1:], label = 'BadPart_RTC', c = 'r')
        plt.scatter(x_bd, vbg_bd['sar1'][1:], label = 'GoodPart_SAR1', c = 'r', marker = 'v')
        plt.scatter(x_gd, vbg_gd['sar1'][1:], label = 'GoodPart_SAR1', c = 'b', marker = 'v')
        plt.scatter(x_gd, vbg_gd['1V reference'][1:], label = 'GoodPart_1V', c = 'b', marker = 'x')
        plt.scatter(x_gd, vbg_gd['rtc'][1:], label = 'GoodPart_RTC', c = 'b')
        plt.ylim(600, 1200)
        plt.grid()
        plt.legend(loc = 0)
        plt.xlabel('ext_code')
        plt.ylabel('Voltage (V)')

    def vbg_reg_read(self):
        '''go through all I2C regs used for bandgap
        '''
        file_name = '/home/test/Desktop/chip722_m1_o_code.csv'
        temp_dict = OrderedDict()
        reg_name_l = [
        'ir_resetb',
        'ir_start',
        'ir_force_xpd_ck',
        'ir_force_pd_ref_out_buf',
        'ir_force_pd_iph',
        'ir_force_pd_vgate_buf',
        'ir_disable_watchdog_ck',
        'bg_i_smp_period',
        'i_smp_period',
        'o_done_flag',
        'o_udf',
        'o_ovf',
        'bg_o_done_flag',
        'bg_o_udf',
        'bg_o_ovf',
        'vdda_2p0_rdy',
        'o_code',
        'dbrown_out_thres',
        'ir_force_xpd_ref_out_buf',
        'ir_force_xpd_iph',
        'ir_force_xpd_vgate_buf',
        'ir_force_code',
        'ir_xpd_vdda_det_2p0',
        'ext_code',
        ]
        mac_rd = self.chip.CHIP_ID.chip_mac()
        for i in reg_name_l:
            temp_dict[i]=getattr(self.chip.HWI2C.ulp,i)
        if not os.path.exists(file_name):
            col_l = reg_name_l.insert
            with open(file_name,'a+') as ff:
                csv_handle = csv.writer(ff)
                csv_handle.writerow(['MAC']+reg_name_l)
        
        val_l = [mac_rd]+[v for i,v in temp_dict.items()]
        with open(file_name,'a+') as ff:
            csv_handle = csv.writer(ff)
            csv_handle.writerow(val_l)
        df = pd.DataFrame(temp_dict,index=[0])
        return df.T

class LdoPtest(object):
    def __init__(self, channel, chipv, irc):
        self.channel = channel
        self.chipv   = chipv
        self.chip    = HALS(channel, chipv)
        self.irc     = irc

    def _measure_list_add_val(self, c_l, v_l, m_n, m_v, times=None):
        '''

        :param c_l:   measurement column name list
        :param v_l:   measurement value list
        :param m_n:   measurement name
        :param m_v:   measurement value
        :param times: if multiple times of measurement has been done
        '''
        c_l += ['%s_%d'%(m_n, times)] if times!=None else ['%s'%m_n]
        v_l += [m_v]

    def vdd33(self, filter = 1):
        '''use adc to read internal VDD33 divider voltege 
        
        :param:
            - filter: adc read filter
        '''
        if self.chipv == 'ESP32':
            Vdd33 = self.channel.req_com('read_vdd33 %d' % filter,1)
        
        elif self.chipv == 'CHIP722':
            self.channel.req_com('open_rf',timeout=3)
            # self.channel.req_com('open_rf',endstr='CHIP722')
            time.sleep(3)
            try:
                Vdd33 = self.chip.channel.req_com('read_vdd33 %d' % filter,1)
            except:
                Vdd33 = ''
            self.channel.req_com('close_rf',1)
            # time.sleep(3)
        return [['VDD33(ADC)'], [Vdd33]]

    def vref_bandgap(self, adc2_chl=7, atten_ls = [3], adc_dref = [0],times=None, o_code_only=False, swd_rd=True):
        '''Measure 1V_Vref Voltage & ADC2 Internal Read
        
        :param adc2_chl: Pull internal signal to external ADC2 channel
                         - SingleBoard: 0~9
                         - MultiBoard : CHIP722->7; ESP32->9
        :param atten_ls: [0,1,2,3]; Skip adc read when it is empty 
        :param adc_dref: [0,1,2,4]
        '''     
        col_ls, val_ls = [],[]

        if self.chipv == 'CHIP722':
            o_code  = self.chip.HWI2C.ulp.o_code
            self._measure_list_add_val(col_ls, val_ls, 'O_CODE', o_code, times)

            if swd_rd:
                '''check super watch dog register values'''
                swd = self.chip.channel.req_com('rd 0x600080b0',1)
                self._measure_list_add_val(col_ls, val_ls, 'SWD', swd, times)

            if not o_code_only:
                self.chip.rtc_debug.pull_internal_voltage(adc2_chl)                     
                self.chip.HWI2C.bias.ent_cgm = 1    # set mux
                self.chip.HWI2C.bias.dtest   = 1    # set mux

                #if use ADC to measure 1V VREF     
                for atten in atten_ls:
                    self.chip.rtc_adc2.config()
                    self.chip.rtc_adc2.set( atten = atten, pad = adc2_chl, test_pad_en = 1)
                    for dref in adc_dref:
                        self.chip.rtc_adc2.sar2_dref(dref)
                        vref_1v_adc = self.chip.rtc_adc2.read(1)
                        col_ls.append('VREF_1V_ADC_ATN%d_DREF%d'%(atten, dref))
                        val_ls.append(vref_1v_adc)

                Vref_1V = self.irc.vol_meas()
                self._measure_list_add_val(col_ls, val_ls, 'VREF_1V', Vref_1V, times)

                loginfo('close mux')             
                self.chip.HWI2C.bias.ent_cgm = 0    # close mux
                self.chip.HWI2C.bias.dtest   = 0    # close mux

            logwarn(zip(col_ls, val_ls))
        return [col_ls, val_ls]

    def vref(self, adc2_chl, atten_ls = [3], adc_dref = [0], 
             slt_ls=['RTC_LDO', 'DIG_LDO', 'SAR1_REF', 'SAR2_REF', 'VCM']):
        '''
        :brief:
            Measure Internal 'RTC_ldo', 'DIG_ldo', 'SAR1_ref', 'SAR2_ref', 'Vcm' Voltage & ADC2 Internal Read
        :param:     
            - adc2_chl : Pull internal signal to external ADC2 channel
                         - SingleBoard: 0~9
                         - MultiBoard : CHIP722->7; ESP32->9
            - atten_ls : [0,1,2,3]; Skip adc read when it is empty 
            - adc_dref : [0,1,2,4]
            - slt_ls   : select the vref will be test form 'vref_mux'
        '''
        col_ls, val_ls = [],[]

        if self.chipv == 'ESP32':
            vref_mux = {'RTC_LDO':0, 'SAR2_REF':1, 'DIG_LDO':2}

            for slt in slt_ls:
                self.chip.power.ldo_debug(vref_mux[slt], adc2_chl)    # pull adc2_vref to adc2_ch9
                Vref = self.irc.vol_meas()
                val_ls.append(Vref)                     
            self.chip.power.ldo_debug(2,adc2_chl+1)         # switch to other channel mux
            col_ls = slt_ls

        elif self.chipv == 'CHIP722':
            vref_mux    = {'RTC_LDO': (1,0), 'DIG_LDO':(1,2), 'SAR1_REF':(1,1), 'SAR2_REF':(0,0), 'VCM':(1,3)}                     

            for slt in slt_ls:  
                self.chip.rtc_debug.set_test_mux(is_rtc=vref_mux[slt][0],test_mux=vref_mux[slt][1])
                
                # -------- if use sar-adc to measure internal voltages --------
                if atten_ls !=[]:
                    self.chip.rtc_adc2.config()
                    for atten in atten_ls:
                        self.chip.rtc_adc2.set(atten = atten, pad = adc2_chl, test_pad_en = 1)
                        for dref in adc_dref:
                            self.chip.rtc_adc2.sar2_dref(dref)  
                            ref_adc = self.chip.rtc_adc2.read(1)
                            val_ls.append(ref_adc)
                            col_ls.append('%s(ADC_ATN%d_DREF%d)'%(slt, atten, dref))

                self.chip.rtc_debug.pull_internal_voltage(adc2_chl) 
                ref = self.irc.vol_meas()                        
                val_ls.append(ref)
                col_ls.append(slt)

            loginfo('close mux')
            self.chip.MEM.wrm(0x600080b8, 29, 28, 0)

        logwarn(zip(col_ls, val_ls))
        return [col_ls, val_ls]

    def rfpll_ref_scan(self,sar2_chnl=0):
        '''measure rfpll related reference voltages

        :param_sar2_chnl: choose SAR-ADC2 channel to mux out internal voltages
        '''
        self.chip.channel.req_com('open_rf')
        time.sleep(2)
        col_ls,val_ls = [],[]
        bias_marlin3_ent_l = ['ent_cpreg','ent_cgm','ent_consti']
        rfpll_ent_l        = ['ent_vco','ent_vco_bias']
        self.chip.rtc_debug.pull_internal_voltage(sar2_chnl)
        for bias_ent in bias_marlin3_ent_l:
            setattr(self.chip.HWI2C.bias_marlin3,bias_ent,1)
            loginfo('open ent: %s'%bias_ent)
            for i in range(4):
                self.chip.HWI2C.bias_marlin3.dtest = i
                col_ls.append(bias_ent+'_%d'%i)
                # vol_read = self.mydm_vol.get_result('VDC')
                vol_read = self.irc.vol_meas()
                logwarn('%s_dtest:%d voltage reads %.2f'%(bias_ent,i,float(vol_read)))
                val_ls.append(vol_read)
            setattr(self.chip.HWI2C.bias_marlin3,bias_ent,0)
            loginfo('close ent: %s'%bias_ent)

        for rfpll_ent in rfpll_ent_l:
            setattr(self.chip.HWI2C.rfpll,rfpll_ent,1)            
            loginfo('open ent: %s'%rfpll_ent)
            for i in range(4):
                self.chip.HWI2C.rfpll.dtest = i
                col_ls.append(rfpll_ent+'_%d'%i)
                # vol_read = self.mydm_vol.get_result('VDC')
                vol_read = self.irc.vol_meas()
                logwarn('%s_dtest:%d voltage reads %.2f'%(rfpll_ent,i,float(vol_read)))
                val_ls.append(vol_read)
            setattr(self.chip.HWI2C.rfpll,rfpll_ent,0)
            loginfo('close ent: %s'%rfpll_ent)
        df = pd.DataFrame(data=val_ls,index=col_ls)
        print df
        return [col_ls, val_ls],df






