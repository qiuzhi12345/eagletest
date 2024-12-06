import baselib.test_channel.channel as chn
import baselib.test_channel.com as com
from baselib.instrument.tester_serv import *
from baselib.loglib.log_lib import *
import time
import csv
from baselib.plot import *
from baselib.instrument import *
from baselib.instrument import tester
import numpy as np
import pandas as pd
import pylab as plb
import matplotlib.pyplot as plt
import re
import serial
from rftest.rflib.rfpll import rfpll
from hal.wifi_api import WIFIAPI
from rftest.rflib import rfglobal
import rftest.rflib.wifi_instrum as wifi_instrum
from rftest.rflib.wifi_lib import WIFILIB
from hal.common import MEM
from rftest.rflib.rfpll import rfpll
import rftest.rflib.utility.iofunc as iofunc
from rftest.rflib.csv_report import csvreport
from hal.hwregister.hwi2c.all import *
from rftest.rflib.pbus import pbus
from rftest.testcase.rf_debug.basic_test import BasicTest
from baselib.instrument.spa import HP,Agilent,phnoise
from baselib.instrument import dm,smc
from baselib.instrument.smc import smc
from hal.rtc_debug import RTC_DEBUG
from hal.adc import RTC_ADC2


rate_bps_dict = rfglobal.rate_bps_dict
sens_dict = rfglobal.sens_dict
rate_dict = rfglobal.ratedic
maxleve_dict = rfglobal.rx_maxlevel_dict


class SPUR_EMI(object):

    def __init__(self,comport,smc_comport,chipv='ESP32', name_str=''):
        self.comport = comport
        self.smc_com = smc_comport
        self.chipv = chipv
        self.mem = MEM(self.comport,self.chipv)
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.wifiapi = WIFIAPI(self.comport,self.chipv)
        self.rfpll = rfpll(self.comport,self.chipv)
        self.i2c = HWI2C(self.comport,self.chipv)
        self.pbus = pbus(self.comport,self.chipv)
        self.rtc_debug = RTC_DEBUG(self.comport,self.chipv)
        self.rtc_adc2 = RTC_ADC2(self.comport,self.chipv)
        self.name_str=name_str
        self.smc = smc(self.smc_com)


    def spurious_emissions_test(self, chan=1,backoff_qdb=0,angle_div=1,distance=30,device_spa='N9020A',name_str='',plt_en=1):
        """

        """
        filetime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()));
        title = 'angle, p_2rd,p_4rd,p_2rd_spa,p_4rd_spa\n'
        fname = self.wifi.get_filename('spurious_emissions_test%s'%name_str, 'spurious_emissions_test%s'%name_str)
        csvreport1 = csvreport(fname, title)

##        self.wifiapi.pll_cap_track_en(0)
        self.wifi.cmdstop()
        self.wifi.rfchsel(chan,0)
        self.wifi.txout("1m", PackLen=100,cbw40=0,backoff_qdb=backoff_qdb,frm_delay=100)
        cfreq=self.wifi.chan2freq(chan)
        self.spa = Agilent('SA',cfreq,device=device_spa)
        self.spa.set_param(cfreq,span=1,rb=3,vb=3)
        self.spa.set_reflvl(-10)

        sum_angle=360/angle_div
        self.smc.return_origin_angle()
        res_max=[]
        for i in range(0,sum_angle):
            self.smc.run(angle=angle_div)
            self.spa.set_cfreq(cfreq*2)
            res1=self.spa.pk_search()
            p_2rd=res1[0][1]+32.5+20*np.log10(cfreq*2)+20*np.log10(distance*1e-5)-10+4.7
            self.spa.set_cfreq(cfreq*4)
            res2=self.spa.pk_search()
            p_4rd=res2[0][1]+32.5+20*np.log10(cfreq*4)+20*np.log10(distance*1e-5)-13+7

            angle_cur=angle_div*i
            csvreport1.write_data([angle_cur,p_2rd,p_4rd,res1[0][1],res2[0][1]],float_num=6)
            res_max.append([angle_cur,p_2rd,p_4rd])

        df=pd.DataFrame(res_max,columns=['angle','p_2rd','p_4rd'])
        data_max=df.max().tolist()
        p_2rd_max=data_max[1]
        p_4rd_max=data_max[2]
        p_2rd_max_angle=df.iloc[df[df.p_2rd==p_2rd_max].index.tolist()[0],0]
        p_4rd_max_angle=df.iloc[df[df.p_4rd==p_4rd_max].index.tolist()[0],0]
        loginfo('   harmomic_2rd max:  %s  dBm |   angle:  %s'%(p_2rd_max,p_2rd_max_angle))
        loginfo('   harmomic_4rd max:  %s  dBm |   angle:  %s'%(p_4rd_max,p_4rd_max_angle))

        if plt_en!=0:
            df1=pd.concat([df,pd.DataFrame(df.iloc[0]).T],ignore_index=True)
            labels=df1['angle']
            p_2rd_data=df1['p_2rd']
            p_4rd_data=df1['p_4rd']
            angles=np.linspace(0,2*np.pi,len(res_max),endpoint=False)
            angles=np.concatenate((angles,[angles[0]]))

            plt.ion()
            fig=plt.figure()
            ax=fig.add_subplot(111,polar=True)

            ax.plot(angles,p_2rd_data,linewidth=2,label='harmomic_2rd')
            ax.plot(angles,p_4rd_data,linewidth=2,label='harmomic_4rd')

            ax.set_thetagrids(angles*180/np.pi,labels)
            plt.legend()
            plt.show()


        self.smc.return_origin_angle()

