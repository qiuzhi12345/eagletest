# -- coding: utf-8 --
# 中文支持

from baselib.loglib.log_lib import *
from hal.Init import HALS
from hal.common import CHIP_ID
from baselib.instrument import awg
from baselib.tc_platform.common import *
from baselib.tc_platform.tc_platform import *
from baselib.test_channel.com import COM
import re
import scipy.optimize as opt
import matplotlib.pyplot as plt
import pandas as pd
import time

class ADC_TC_PERF(object):
    """
    用于 ADC 遍历测试： 

    """
    def __init__(self, channel, chipv = "AUTO"):
        self.chip = HALS(channel, chipv)
        self.channel = self.chip.channel
        self.chipv = self.chip.chipv

    def adc1_sameinput_looptest(self, adc1_channel, sample, adc_data_path, atten_value = 3, input_dc = 0.8, xpd_enable = 0):
        '''
        adc_data_path: "/home/lab/job/chip7.2.2/lowpower_test/adc/"
        adc1_channel connect to a fix voltage between 0 and 3.3v, eg 2.5v.
        '''
        from rtclib.rtc import ADC_LIB
        self.adc_lib = ADC_LIB(self.channel, self.chipv)
        self.awg = awg()
        self.awg.appl("DC", 0, 0, input_dc)
        time.sleep(0.15)
        self.chip.rtc_clk.set_cpu_freq(1)
        self.chip.rtc_adc1.config()
        self.chip.rtc_adc1.xpd_enable(xpd_enable)
        self.chip.rtc_adc1.set(pad = adc1_channel, atten = atten_value)
        adc_csv =  adc_data_path + 'adc1_input{}_xpdsar{}_sample{}_{}.csv'.format(input_dc, xpd_enable, sample, time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime()))
        with open(adc_csv, 'w') as adc_file:
            adc_file.write("input_dc, ")
            for i in range(sample):
                adc_file.write("%d,"%(i))
            adc_file.write("\n")
            adc_file.write("80M,")
            for i in range(sample):
                adc1_value = int(self.chip.rtc_adc1.read(filter_en = 0))
                adc_file.write("%d,"%(adc1_value))
            adc_file.write("\n")
            adc_file.write("deepsleep,")
            first_addr = self.adc_lib.adc1_deepsleep_read(adc1_channel, sample, atten_value)
            for i in range(sample):
                adc1_value = int(self.chip.MEM.rd(first_addr + i * 4) & 0xffff)
                adc_file.write("%d,"%(adc1_value))
            adc_file.write("\n")

    def __tc_adc_value_scan(self, para, log):
        '''
        para[0]: adc_en=[1,1]
        para[1]: adc_pad=[6,7]
        para[2]: wifi_en=[0,1]    
        para[3]: atten_val='[0,1,2,3]' or 'range(4)'          
        para[4]: vol_rg
        para[5]: step                
        para[6]: repeat_num                              
        '''
        adc_en      = para[0]
        adc_pad     = para[1]
        wifi_en     = para[2]
        atten_val   = eval(para[3])
        vol_rg      = para[4] 
        step        = para[5]
        repeat_num  = para[6]

        if adc_en[0]:
            self.chip.rtc_adc1.config()
        if adc_en[1]:
            self.chip.rtc_adc2.config()
        chipmac=CHIP_ID(self.channel, self.chipv).chip_mac()
        log.write_value('chip_mac', chipmac)
        for vol in range(vol_rg[0], vol_rg[1], step):
            self.myawg.appl(name='DC',freq=0, amp=0,offs=vol/1000.0)
            time.sleep(0.5)
            for i in wifi_en:
                for j in atten_val:     
                    if adc_en[0]:
                        self.chip.rtc_adc1.set(pad = adc_pad[0], atten = j)
                        for t in range(repeat_num):    
                            adc1_res = int(self.chip.rtc_adc1.read())
                            log.write_value('adc1_wf%s_atten%s_%smV_%s'%(i, j, vol, t), adc1_res)
                    if adc_en[1]:
                        self.chip.rtc_adc2.set(pad = adc_pad[1], atten = j)
                        for t in range(repeat_num):
                            adc2_res = int(self.chip.rtc_adc2.read())
                            log.write_value('adc2_wf%s_atten%s_%smV_%s'%(i, j, vol, t), adc2_res)                            
        pass

    # socket
    def tc_chip_socket_loop(self, adc_en=[1,1], adc_pad=[2,1], wifi_en=[0,1], atten_val='range(4)', vol_rg=[0,3000], step=1, repeat_num=4, \
                            chn_thc=1, device="", temper_list="[]", mode=0, binname='eagle.app.pro.flash.bin'):        
        """
        the module is used to test chips in specific sockets or modules on ESP_Test Board
        """
        self.mode   = mode
        self.binname= binname
        self.chip   = HALS(self.channel, self.chipv)
        self.myawg  = awg.awg()
        self.myawg.reset(timeout=100)
        self.myawg.clean(timeout=100)

        logname = "adc_ptest/mv%s_%s_%s_%s"%(vol_rg[0], step, vol_rg[1], device)
        #stest.socket_set("eagle.app.pro.flash.bin", self.mode)
        stest = socket_test(self.channel, logname, chn_thc, device, self.__tc_adc_value_scan, adc_en, adc_pad, wifi_en, atten_val, vol_rg, step, repeat_num)        
        stest.socket_set(self.binname, self.mode)
        stest.run(eval(temper_list))

    def __multiboard_init(self):
        '''
        cols    : input column names, should be an array of strings
        pad_cfg: initial configuration including pads initial state setting and working states of relative instruments 
        '''
        chip_array=Multiboard_Prep(self.com_mcu, self.com_mux, self.board_ver).multiboard_test_pre(chip_list)
        chip_num=chip_array.keys()
        if len(chip_num)!=len(self.chip_list):
            logerror("!!At least one module failed in connection!!")
            return -1
        # for chip_sel in self.chip_list:
        #     self.__pad_cfg(chip_sel) 

    # def __tc_adc_multiboard_wrap(self, para, log):
    #     for chip_sel in range(len(self.chip_list)):
    #         self.mcu.mcu_sel(chip_sel)
    #         loginfo("start to test chip%d"%chip_sel)
    #         self.__tc_adc_value_scan(adc_en, adc_pad, wifi_en, atten_val, vol_rg, step, repeat_num, log)

    def tc_chip_multiboard_loop(self, adc_en=[1,1], adc_pad=[2,1], wifi_en=[0,1], atten_val='range(4)', vol_rg=[0,3000], step=1, repeat_num=4,\
                            com_mcu=1, board_ver=1, chip_list='range(0,32)', chn_thc=1, device="", temper_list="[]", 
                            mode=0, binname='eagle.app.pro.flash.bin'):
        """
        the module is used to test saradc performance of ESP modules on multiboard
        """
        self.mode   = mode
        self.binname= binname
        self.mcu = Multiboard_CTL(com_mcu)
        self.mux = HALS(self.channel)
        self.chip_list=eval(chip_list)
        self.board_ver = board_ver
        self.mydm   = dm.dm()
        self.temper_list=eval(temper_list)  

        logname = "adc_ptest/mv%s_%s_%s_%dpcs_%s"%(vol_rg[0], step, vol_rg[1], len(self.chip_list), device)
        mtest = multiboard_test(com_mcu, logname, self.board_ver, chn_thc, device, self.__tc_adc_value_scan, \
            adc_en, adc_pad, wifi_en, atten_val, vol_rg, step, repeat_num)
        self.__multiboard_init()

        mtest.run(self.temper_list)      

class INLDNL_ANLY(object):
    """
    用于分析 ADC_TC_PERF 所生成的数据
    1. DNL
    2. INL

    每次只能单独分析一组数据，比如:
    - ADC1
    - WIFI关，
    - atten 值
    - 电压范围
    - 选取第几次测试

    详见 *data_init* 函数

    流程：
        .. code:: python
            adc = INLDNL_ANLY(df)
            adc.data_init()
            adc.do_anly()
            adc.report_plot()

    """
    def __init__(self, database):
        self.df_raw = database

    def data_init(self, adc = 1, 
                        wifi_en = 0,
                        atten_val = 0,
                        vol_rg = [0,3301],
                        step = 1,
                        num = 0,
                        sat_val = [0,4095]
                    ):
        '''
        从 ADC_TC_PERF 测试结果中提取对应分析数据数据。

        :adc wifi_en atten_val num:
        以上参数分别随影测试结果 adc*1*_wf*0*_atten*0*_10mV_*0*
        
        :vol_rg:
        电压范围

        :step:
        电压步进

        :sat_val:
        测量饱和点，用于线性拟合的时候把饱和点去掉。
        '''

        # get data
        col = []
        for i in range(vol_rg[0], vol_rg[1], 1):
            col.append("adc%d_wf%s_atten%s_%smV_%s"%(adc, wifi_en, atten_val, i, num))
            #col.append("%smV_ADC%s_CH2_atten%s_%s"%(i,adc,atten_val,num))
        self.df = self.df_raw.loc[:,col]

        self.df.loc["Input"] = range(vol_rg[0], vol_rg[1], 1)
        self.df_res = dict()

        self.__adc = adc
        self.__wifi_en = wifi_en
        self.__atten_val = atten_val
        self.__sat_val = sat_val
        self.__vol_rg = vol_rg

    def __calc(self, ratio = [1,1]):
        a = ratio[0]
        b = ratio[1]
        iy1 = a * self.ix + b
        res_t = np.sum((self.iy.flatten()-iy1.flatten())**2)
        return res_t

    def __calc_ideal(self, datebase):        
        self.ix = np.array(datebase.loc["Input"])
        self.iy = np.array(datebase.loc["raw"])
        res = opt.minimize(self.__calc, [1,1])

        ia = res.x[0]
        ib = res.x[1]
        ideal_df = []
        for i in self.ix:
            ideal_df.append(round(ia * i + ib))
        return ideal_df, ia

    def __remove_saturation(self, database):
        for col in database.columns:
            if database.loc["raw"][col] <= self.__sat_val[0]:
                database = database.drop([col], axis=1)
            else:
                break
        for col in database.columns[::-1]:
            if database.loc["raw"][col] >= self.__sat_val[1]:
                database = database.drop([col], axis=1)
            else:
                break
        return database

    def do_anly(self):
        for chip in self.df.index:
            if chip != "Input":
                loginfo("chip: %s"%chip)
                # new a dataframe
                df_tmp = pd.DataFrame(columns = self.df.columns)
                df_tmp.loc["Input"] = self.df.loc["Input"]
                df_tmp.loc["raw"] = self.df.loc[chip]
                df_tmp.loc["col"] = self.df.columns
                # 
                df_tmp = self.__remove_saturation(df_tmp)
                df_tmp.loc["ideal"], K = self.__calc_ideal(df_tmp)

                raw_mv = list(df_tmp.loc["raw"])
                raw_mv.insert(0,raw_mv[0])
                raw_mv.pop(-1)
                df_tmp.loc["raw_mv"] = raw_mv
                df_tmp.loc["dnl_f"] = df_tmp.loc["raw"] - df_tmp.loc["raw_mv"]

                df_tmp.loc["INL"] = df_tmp.loc["ideal"] - df_tmp.loc["raw"]
                # 由于测试结果单位是1mV， 所以DNL在计算的时候最后减去的是1mV的LSB，并非1LSB
                df_tmp.loc["DNL"] = df_tmp.loc["dnl_f"] - K*1

                self.df_res[chip] = df_tmp.copy()


    def report_plot(self, savefig = False):
        '''
        生成图表
        '''
        plt.ion()
        fgname = "ADC%s-ATTEN%s-WIFI%s-[%s-%s]"%(self.__adc, self.__atten_val, self.__wifi_en, self.__sat_val[0], self.__sat_val[1])
        plt.figure(fgname)
        plt.subplot(221)
        for k, v in self.df_res.items():
            plt.plot(v.loc["Input"], v.loc["INL"], '--', label=k)

        plt.xlabel('Input VOL(mv)')
        plt.ylabel('ADC Measure (LSB)')
        plt.title("INL")
        plt.grid()
        plt.legend()

        plt.subplot(223)
        for k, v in self.df_res.items():
            plt.plot(v.loc["Input"], v.loc["DNL"], '--', label=k)
        plt.xlabel('Input VOL(mv)')
        plt.ylabel('ADC Measure (LSB)')
        plt.title("DNL")
        plt.grid()
        plt.legend()

        plt.subplot(122)
        for k, v in self.df_res.items():
            plt.plot(v.loc["Input"], v.loc["raw"], '--', label=k)
        plt.xlabel('Input VOL(mv)')
        plt.ylabel('ADC Measure (LSB)')
        plt.title("RAW-DATA")
        plt.grid()
        plt.legend()

        if savefig:
            plt.savefig('./log/%s.png'%fgname, dpi=300)

