# -- coding: utf-8 --
# 中文支持
from baselib.loglib.log_lib import *
from hal.gpio import GPIO
from hal.hwregister.hwreg import *
from baselib.eagletool.autowork import *

##import hal.hwregister.hwreg.EFUSE_REG
import time
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from baselib.test_channel.com import COM as com
from baselib.instrument.awg import awg
from baselib.instrument.eps import eps
from baselib.instrument.dm  import dm
from baselib.instrument.allInOne import allInOne
from hal.Init import HALS
from hal.common import *

class InstrumentRemoteControl(object):
    '''class to control multiple instruments for test automation

    :param:
        ins_ls: list of instruments to be used
        auto_type: skt: for socket pkg test;
                   mb:  for Multiboard pkg test
                   None: connect instrument by input ins_ls
    '''
    def __init__(self,ins_ls=['AWG','EPS','DM_C','DM_V'], auto_type=None):
        if auto_type==None:
            ins_list=ins_ls
        else:
            ins_option = raw_input('\nTYPE in your instrument option\nPlease type '+logcolor('1 or 2')
                    +'\nDefault option is 2 to be used if just press '+logcolor("Enter")
                    +'\nTYPE q to quit'
                    +'\nInstrument option details see above\n')
            while ins_option != 'q':
                if ins_option == '1':
                    ins_list = ['EPS','DM_V'] if auto_type=='mb' else ['AWG','EPS','DM_C','DM_V']
                    break
                elif ins_option == '2':
                    ins_list = ['AllInOne','DM_V'] if auto_type=='mb' else ['AWG','AllInOne','DM_V']
                    break
                elif ins_option == '':
                    ins_list = ['AWG','AllInOne','DM_V']
                    break
                else:
                    ins_option = raw_input('TYPE '+logcolor('1 or 2') +' or just press'+logcolor("Enter")+'\n')
            else:
                logwarn('TYPE 1 or 2 to choose instrument options')
                return

        ins_list = [i.upper() for i in ins_list]
        #color pattern for instrument conencting information, 'G' stands for green color
        connect_info = lambda x,y: loginfo(logcolor(x,'G')+' Connected, used for '+logcolor(y,'G'))
        self._flag_aio = False
        if 'ALLINONE' in ins_list:
            self._flag_aio = True
            self.myaio    = allInOne()
            connect_info('U3606B','SUPPL & CURR MEAS')
            self.myaio._sour_vol_rng('8V')
            self.myaio.conf_meas(func='CURR',rng='MAX')

        if 'AWG' in ins_list:
            self.myawg    = awg()
            connect_info('33120A','SIGNAL CONTROL')

        if 'DM_V' in ins_list:
            self.mydm_vol = dm(num_of_machine=0)
            connect_info('34401A','VOLT MEAS')

        if 'EPS' in ins_list:
            self.myeps    = eps()
            connect_info('E3633A','SUPPLY')

        if 'DM_C' in ins_list:
            self.mydm_cur = dm(num_of_machine=1)
            connect_info('34401A','CURR MEAS')
            self.mydm_cur.get_result('IDC')
            loginfo('34401A mode sets up to CURR MEAS')

    def supl_set(self,volt=0,ilim=3,out=1):
        '''supply voltage control
        '''
        if self._flag_aio:
            self.myaio.sour(lvl=volt,iv_lim=ilim,out=out)
        else:
            self.myeps.pwr(vol=volt,cur=ilim)
            self.myeps.out_ena(out)

    def vol_meas(self,rng='AUTO'):
        '''measure voltage
        '''
        val = self.mydm_vol.get_result('VDC',data_type=rng)
        # val =float(self.mydm_vol.get_result('VDC',data_type =rng))
        return val

    def cur_meas(self,rng='MAX'):
        '''measure current
        '''
        if self._flag_aio:
            val = self.myaio.meas(func='CURR',rng=rng)
            self.myaio.conf_meas(func='CURR',rng='MAX')
        else:
            val = self.mydm_cur.get_result('IDC',data_type=rng)
            # val =float(self.mydm_cur.get_result('IDC',data_type =rng))
        return val

    def sng_gen(self,volt=0):
        '''singal generator to control DC votlage
        '''
        self.myawg.appl('DC',0,0,volt)
        logdebug('33120A OUTPUT DC %rV'%volt)

    def supl_reset(self,volt=3.3,ilim=2,timeout=2):
        '''supply reset
        '''
        logwarn('SUPPLY RESETing ...')
        loginfo('SUPPLY will be turned off to 0V then jumps back to %rV'%volt)
        self.supl_set(volt=0,ilim=ilim,out=1)
        time.sleep(1)
        self.supl_set(volt=volt,ilim=ilim,out=1)
        time.sleep(1+timeout)
        logwarn('SUPPLY reset done ...')

    def sng_edge(self,volt=3.3,edge='rise',puls_width=1,timeout=1):
        '''signal generator reset

        :param edge: define signal edge type to be rise or fall
        :param puls_width: define pulse width in seconds
        '''
        if edge == 'rise':
            volt_0 = 0.0
            volt_1 = volt
        elif edge == 'fall':
            volt_0 = volt
            volt_1 = 0.0
        else:
            logerror('edge type is wrong, either rise or fall')
            return
        loginfo('SIGGEN will be switched to %rV then %rV after %r seconds'%(volt_0,volt_1,puls_width))
        self.sng_gen(volt=volt_0)
        time.sleep(puls_width)
        self.sng_gen(volt=volt_1)
        time.sleep(1+timeout)
        logwarn('SIGGEN reset done ...')

    def chip_power_on(self,volt=3.3,ilim=3,en_awg=True,timeout=2):
        '''turn on chip power

        :param en_awg: if choose to turn on chip_pu as well
        '''
        logwarn('... POWER ON ...')
        self.supl_set(volt=volt,ilim=ilim,out=1)
        if en_awg:
            time.sleep(1)
            self.sng_gen(volt=volt)
        time.sleep(timeout)

    def chip_power_off(self,en_awg=True,timeout=2,out=1):
        '''turn off chip power supply & chip_pu control

        :param en_awg: if choose to turn off chip_pu as well
        '''
        logwarn('... POWER OFF ...')
        self.supl_set(volt=0,ilim=0,out=1)
        if en_awg:
            time.sleep(1)
            self.sng_gen(volt=0)
        self.supl_set(volt=0,ilim=0,out=out)
        time.sleep(timeout)

    def chip_reset(self,volt=3.3,ilim=3,hard=0,hard_vth=2.8,en_awg=True,timeout=2):
        '''both supply & signal generator gets reseted
        '''
        volt_3p3 = 3.3 if (hard==0 and volt <= hard_vth) else volt

        logwarn('SUPPLY & CONTROL SIGNAL sets to 0V')
        self.chip_power_off(en_awg=en_awg,timeout=timeout)

        logwarn('SUPPLY sets to %rV'%volt_3p3)
        self.chip_power_on(volt=volt,ilim=ilim,en_awg=en_awg,timeout=timeout)
        if hard==0 and volt <= hard_vth:
            logwarn('SUPPLY resets to %rV'%volt)
            self.supl_set(volt=volt,ilim=ilim,out=1) #supply sets to specified voltage
            time.sleep(1)

class Multiboard_CTL(object):
    '''
    this class is used for mcu's control of selected ESP chip module on multiboard
    '''
    def __init__(self,  mux_chl, mcu_chl, board_ver = 1, chipv = "ESP32"):
        '''

        :param mux_chl: com# for ESP chip module
        :param mcu_chl: com# for mcu
        '''
        self.mcu_chl   = mcu_chl
        self.mux_chl   = mux_chl
        self.chipv     = chipv
        self.board_ver = board_ver

        #instantiate mcu
        self.mcu_chip = HALS(self.mcu_chl, self.chipv)
        self.mcu_gpio = GPIO(self.mcu_chl, self.chipv)

        if self.chipv   == 'ESP32':
            self.chip_pu = 5
            self.IO_0    = 12
        elif self.chipv == 'CHIP722'or self.chipv =='CHIP723':
            self.chip_pu = 17
            self.IO_0    = 41

    def mcu_slt(self, chip_sel = 0):
        '''mcu selects the ESP chip module to be tested on multiboard

        :param chip_sel:    # of chip to be selected
        :note: A0~A4: IO[15, 2, 4, 26, 27]
        '''
        time.sleep(1)
        io_val =[i for i in np.zeros((5,),dtype=int)]
        io_addr=[i for i in np.zeros((5,),dtype=int)]

        if self.chipv=='ESP32':
            #tb_ver->1 for new burning testboard
            io_addr  = [15, 2, 4, 26, 27] if self.board_ver==1 else [16, 2, 4, 26, 27]
        elif self.chipv =='CHIP722' or self.chipv =='CHIP723':
            io_addr  = [40, 19, 20, 26, 18]

        logdebug("MCU SELECT CHIP #%d ..."%chip_sel)
        for i in range(0,len(io_addr)):
            io_val[i]=(chip_sel>>i)&0x1
            self.mcu_gpio.dig_gpio_out(io_addr[i],io_val[i])
            logdebug("MCU: gpio%d_out->%d"%(io_addr[i],io_val[i]))
        logdebug("MCU SELECT CHIP #%d done"%chip_sel)

    def download(self, chip_sel, bin_file):
        '''mcu selects ESP chip and downloads bin file into ESP chip

        :param chip_sel:    # of chip to be selected
        '''
        self.mcu_slt(chip_sel)
        time.sleep(1)
        logwarn("MCU: reseting CHIP#%r & sets GPIO0 to 0" % chip_sel)
        # self.mcu_gpio.dig_gpio_out(self.chip_pu,1)
        self.mcu_gpio.dig_gpio_out(self.chip_pu,0)
        self.mcu_gpio.dig_gpio_out(self.IO_0, 0)
        time.sleep(0.5)
        self.mcu_gpio.dig_gpio_out(self.chip_pu,1)

        time.sleep(1)
        logwarn("MCU: CHIP#%r now enters DOWNLOAD mode" % chip_sel)
        comNum        = int(filter(str.isdigit, self.mux_chl.ComPort))

        eagle_download_tool(com_num=comNum, user_name='sly', chipv = self.chipv,Imode = False,bin_file = bin_file)
        # self.mcu_gpio.dig_gpio_out(self.IO_0, 1)

    def mcu_reset(self, chip_sel = 0):
        '''mcu resets the ESP chip module to be tested on multiboard

        '''
        self.mcu_slt(chip_sel)
        loginfo("Chip_%r reseting..." % chip_sel)
        self.mcu_gpio.dig_gpio_out(self.chip_pu, 0)
        time.sleep(0.5)
        self.mcu_gpio.dig_gpio_out(self.IO_0, 1)
        self.mcu_gpio.dig_gpio_out(self.chip_pu, 1)
        loginfo("Chip_%r reset done" % chip_sel)

    def mcu_sel_chip(self, chip_sel=0, connect_try = 10):
        '''this function selects chip but also checks if connection is successful

        :param connect_try: number of times to try to cnnect if no mac addres acquired

        :return res:      True if successfully connected
        :return mac_addr: mac address if successfully connected, else 0
        '''
        self.mcu_slt(chip_sel)
        loginfo("CHIP#%d SELECTED"%chip_sel)
        mux=HALS(self.mux_chl)
        res = False
        com_error_cnt=0
        mac_addr=0
        while True:
            time.sleep(1)
            chip_mac=mux.CHIP_ID.chip_mac()
            logdebug("chip mac returns: %s"%chip_mac)
            if chip_mac != -1:
                res = True
                mac_addr=chip_mac
                break
            else:
                if com_error_cnt==connect_try:
                    logwarn("Connection fails after %dx tries..."%com_error_cnt)
                    res = False
                    break
                mcu.mcu_reset(chip_sel)
                time.sleep(3)
                com_error_cnt=com_error_cnt+1
        return res, mac_addr

    def mcu_power_reset(self, chip_n, irc, volt=3.3, ilim=3, hard=0, hard_vth=2.8, timeout=2):
        '''

        :param chip_n: CHIP# to be tested and reseted
        :param irc:    pass instrument control instance
        '''
        volt_3p3 = 3.3 if (hard==0 and volt <= hard_vth) else volt

        logwarn('SUPPLY & CONTROL SIGNAL sets to 0V')
        irc.chip_power_off(en_awg=False,timeout=timeout)
        logwarn('SUPPLY sets to %rV'%volt_3p3)
        irc.chip_power_on(volt=volt,ilim=ilim,en_awg=False,timeout=timeout)

        self.mcu_reset(chip_n)

        if hard==0 and volt <= hard_vth:
            logwarn('SUPPLY resets to %rV'%volt)
            irc.supl_set(volt=volt,ilim=ilim,out=1) #supply sets to specified voltage
            time.sleep(timeout)

        logwarn('RESET DONE chip#%s selected'%chip_n)
        self.mcu_sel_chip(chip_sel=chip_n)

    def mcu_batch_rst(self,chip_ls=range(32)):
        '''resets ESP chips in batch

        :param chip_ls:  pass a list of chips to be reseted by MCU
        '''
        logdebug("MCU will reset CHIP from #%d to #%d"%(chip_ls[0],chip_ls[-1]))
        for i in chip_ls:
            logdebug("RESETing CHIP#%d..."%(i))
            self.mcu_reset(i)
            time.sleep(0.1)
        logdebug("MCU reset done")

    def mcu_batch_dwn(self, chip_ls = range(20), bin_file = 'fixedSlpCounterError/eagle.app.pro.flash_fixTimer.bin'):
        '''batch download bin to multiboard chips

        :param chip_ls: pass a list of chips to be downloaded
        '''
        logdebug("MCU will download CHIP from #%d to #%d"%(chip_ls[0],chip_ls[-1]))
        for i in chip_ls:
            self.mcu_reset(i)
            self.download(chip_sel=i, bin_file=bin_file)
        logdebug("MCU download done")
        return

class Multiboard_Prep(object):
    '''this class preapares MCU & MUX & chips to be tested on multiboard
    '''
    def __init__(self, chan_mcu, chan_mux, board_ver = 1, chipv = "ESP32"):
        self.chipv = chipv
        self.com_mcu = chan_mcu
        self.com_mux = chan_mux
        self.board_ver = board_ver
        self.mcu=Multiboard_CTL(self.com_mcu, board_ver=self.board_ver)
        self.mux=HALS(self.com_mux)

    def mcu_sel_chip(self, chip_sel=0, connect_try = 10):
        '''this function selects chip but also checks if connection is successful

        :param connect_try: number of times to try to cnnect if no mac addres acquired

        :return res:      True if successfully connected
        :return mac_addr: mac address if successfully connected, else 0
        '''
        # mcu=Multiboard_CTL(self.com_mcu, board_ver=self.board_ver)
        # mux=HALS(self.com_mux)
        self.mcu.mcu_slt(chip_sel)
        loginfo("CHIP#%d SELECTED"%chip_sel)
        res = False
        com_error_cnt=0
        mac_addr=0
        while True:
            time.sleep(1)
            chip_mac=self.mux.CHIP_ID.chip_mac()
            logdebug("chip mac returns: %s"%chip_mac)
            if chip_mac != -1:
                res = True
                mac_addr=chip_mac
                break
            else:
                if com_error_cnt==connect_try:
                    logwarn("Connection fails after %dx tries..."%com_error_cnt)
                    res = False
                    break
                mcu.mcu_reset(chip_sel)
                time.sleep(3)
                com_error_cnt=com_error_cnt+1
        return res, mac_addr

    def multiboard_test_pre(self, chip_list=range(0,11)):
        '''this function returns a list of working chips & their CHIP_ID within given range

        :param chip_list: pass a list of chips to be tested
        '''
        Chip_Array= eval(chip_list) if type(chip_list) is str else chip_list
        logdebug("chip_list inputed:\n%s"%Chip_Array)

        fail_list=[]
        work_list = {'CHIP#':[],'MAC':[]}
        chip_res=0
        chip_mac=0

        for chip_sel in Chip_Array:
            chip_res, chip_mac=self.mcu_sel_chip(chip_sel)
            if chip_res:
                work_list['CHIP#'].append(chip_sel)
                work_list['MAC'].append(chip_mac)
            else:
                fail_list.append(chip_sel)
                logdebug("chip#%d failed to be connected!!"%chip_sel)

        logdebug("list of function chips:\n%s"%work_list)
        if not fail_list == []:
            logwarn("list of chips not responding:\n%s"%fail_list)
        return work_list

class data_fit(object):
    '''
    this module is used for data fitting and plot
    '''
    def __init__(self, x_in=[], y_in=[]):
        self.x_in = x_in
        self.y_in = y_in

    def data_plot(self, hold=True,save_path='./log/DAC_vs_temp/DAC_data_final/DAC_fig/',data_name='data_name', label=['input_val','df_vol/mV'], plt_clr=True):
        '''
        plot figures for input x_in and y_in
        '''
        plt.ion()
        if hold:
            plt.hold(True)
        x = np.array(self.x_in)
        y = np.array(self.y_in)
        plt.plot(x,y,"b--")
        plt.xlabel(label[0])
        plt.ylabel(label[1])
        plt.title('ff1_pvt_vs_dig_max')
        if save_path!='':
            plt.savefig(save_path+data_name)
        plt.show()
        if plt_clr:
            plt.close()

    def f_curve_fit(self, plt_en=0):
        '''
        Use non-linear least squares to fit a function
        '''
        def f_linear(x,k,b):
            return k*x+b
        k,b=optimize.curve_fit(f_linear, self.x_in, self.y_in)[0]
        if plt_en:
            plt.figure()
            x1=np.arange(min(self.x_in),max(self.x_in)+1)
            y1=k*x1+b
            plt.plot(x1,y1,"blue")
        return k,b

    def data_curve_fit(self):
        '''
        recursive minimization of squares of errors between f(x) and corresponding iy.
        '''
        def calc(ratio = [1,1]):
            a = ratio[0]
            b = ratio[1]
            iy1 = a * self.ix + b
            res_t = np.sum((self.iy.flatten()-iy1.flatten())**2)
            return res_t
        self.ix = []
        self.iy = []
        ix = np.array(self.x_in)
        iy = np.array(self.y_in)
        res = optimize.minimize(calc, [1,1])
        ia = res.x[0]
        ib = res.x[1]
        return ia, ib