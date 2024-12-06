from baselib.loglib.log_lib import *
from baselib.loglib.log_csv import csvreport
from hal.Init import HALS
from rtclib.rtc import TSEN_LIB
import numpy as np
import matplotlib.pyplot as plt, csv
import pandas as pd


class TSEN_TC_LOWPOWER(object):
    def __init__(self, channel, chipv = "AUTO"):
        self.chip = HALS(channel, chipv)
        self.chipv = self.chip.chipv
        self.tsen_lib = TSEN_LIB(self.chip.channel, self.chipv)
        self.tsen_data_path = '/home/lab/job/{}/lowpower_test/tsen/'.format(self.chipv)

    def tsen_2m_read(self, tsen_file, sample_num, env_tmp):
        tsen_file.write("20M_tmp-{},".format(env_tmp))
        tsen_list = self.tsen_lib.tsen_2m_read(sample_num)
        for i in range(len(tsen_list)):
            tsen_data = int(tsen_list[i])
            tsen_file.write("%d,"%(tsen_data))
        tsen_file.write("\n")
        return

    def tsen_80m_read(self, tsen_file, sample_num, env_tmp):
        tsen_file.write("80M_tmp-{},".format(env_tmp))
        tsen_list = self.tsen_lib.tsen_80m_read(sample_num)
        for i in range(len(tsen_list)):
            tsen_data = int(tsen_list[i])
            tsen_file.write("%d,"%(tsen_data))
        tsen_file.write("\n")
        return
    
    def tsen_wifiinit_read(self, tsen_file, sample_num, env_tmp):
        tsen_file.write("wifiinit_tmp-{},".format(env_tmp))
        tsen_list = self.tsen_lib.tsen_wifiinit_read(sample_num)
        for i in range(len(tsen_list)):
            tsen_data = int(tsen_list[i])
            tsen_file.write("%d,"%(tsen_data))
        tsen_file.write("\n")
        return
                
    def tsen_lightsleep_read(self, tsen_file, sample_num, env_tmp):
        first_addr = self.tsen_lib.tsen_lightsleep_read(sample_num)
        tsen_file.write("lightsleep_tmp-{},".format(env_tmp))
        for i in range(sample_num):
            addr = first_addr + i * 4
            tsen_data = int(self.chip.MEM.rd(addr) & 0xffff)
            tsen_file.write("%d,"%(tsen_data))
        tsen_file.write("\n")
        return
    
    def tsen_deepleep_read(self, tsen_file, sample_num, env_tmp):
        first_addr = self.tsen_lib.tsen_deepsleep_read(sample_num)
        tsen_file.write("deepsleep_tmp-{},".format(env_tmp))
        for i in range(sample_num):
            addr = first_addr + i * 4
            tsen_data = int(self.chip.MEM.rd(addr) & 0xffff)
            tsen_file.write("%d,"%(tsen_data))
        tsen_file.write("\n")
        return

    def tsen_differentmode_run(self, sample_num):
        with open(self.tsen_data_path + 'tsen_{}times_{}.csv'.format(sample_num, time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())), 'w') as tsen_file:
            self.chip.rtc_wdt.wdt_unlock()
            self.chip.rtc_wdt.wdt_stg_hold_len(0, 0xffff)
            self.chip.rtc_wdt.wdt_stg_act(0, 4)
            self.chip.rtc_wdt.wdt_init()
            time.sleep(2)
            self.tsen_deepleep_read(tsen_file, sample_num, '40')
            self.chip.rtc_wdt.wdt_unlock()
            self.chip.rtc_wdt.wdt_stg_hold_len(0, 0xffff)
            self.chip.rtc_wdt.wdt_stg_act(0, 4)
            self.chip.rtc_wdt.wdt_init()
            time.sleep(2)
            self.tsen_lightsleep_read(tsen_file, sample_num, '40')
            self.tsen_2m_read(tsen_file, sample_num, '40')
            self.tsen_80m_read(tsen_file, sample_num, '40')
            #self.tsen_wifiinit_read(tsen_file, sample_num, '40')