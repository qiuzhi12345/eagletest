# -- coding: utf-8 --
# 中文支持

from baselib.loglib.log_lib import *
from baselib.loglib.log_csv import csvreport
import time
from baselib.test_channel.com import COM as com
from baselib.instrument import thc
import platform
import os,sys

BIN_PATH = "./dist/bin/"
DOWNLOAD_CMD = "python -m esptool -b 230400" + \
                       " -p " + "%s" + \
                       " load_ram %s"

class multiboard_test(object):
    '''
    the class is for tests of multiple ESP modules on multiboard, inclusive of current, voltage, sensor performance, etc.
    '''
    #def __init__(self, chn_mcu = com(0), chn_mux = com(1), logname='test_item_name', board_ver=1, func, *args):
    def __init__(self, chn_mcu, logname, board_ver, chn_thc, device, chip_list, func, *args):
        '''
        the parameters of exterior functions should be imported from args
        temper_list: temperature sequence such as "range(0,50,10)", "[0,15,70]" for Temperature/humidity Case configuration
        '''    
        self.com_mcu = chn_mcu
        #self.com_mux = chn_mux
        self.logname = logname
        self.board_ver = board_ver
        self.chip_list=eval(chip_list)
        self.func = func
        self.args = args
        self.log = csvreport(self.logname)
        self.log.mode = 1
        self.mythc=thc.thc(chn_thc, device)
        self.scan_times=10
        self.mcu = Multiboard_CTL(self.com_mcu)

    def multiboard_set(self, binname = "", mode = 0):
        '''
        mode:
            0. flash exists on socket board, download to flash only once
            1. no flash on socket board or only need to download bin into ram for each chip
            # 2. need to download into flash on module chip
        '''
        self.mode = mode
        self.binname = binname

    def run(self, temper_list):
        if len(temper_list)==0:
            self.func(self.args, self.log)
        else:
            for i in range(len(temper_list)):
                self.log.flush_line()
                self.log.write_value('temperature/C', temper_list[i])
                self.mythc.temper_set(temper_list[i], self.scan_times, 3600)
                for chip_sel in self.chip_list:
                    self.mcu.mcu_sel(chip_sel)
                    loginfo("start to test chip%d"%chip_sel)
                    self.func(self.args, self.log)
        self.log.deinit()

class socket_test(object):
    def __init__(self, channel, logname, chn_thc, device, func, *args):
        '''
        This class is for repeative tests in socket with one chip or on ESP_Test Board with one ESP module

        init参数:

            :channel:
                socket使用的串口, e.g. com(0)

            :logname:
                test数据文件名

            :chn_thc:
                采用温箱的通讯端口, e.g. TH1800的串口为com(1)

            :device:
                温箱设备号, e.g."TH1800", "TEMI880"

            :func:
                传递外部test item的函数实体名

            :args:
                传递外部test item的参数

        '''
        super(socket_test, self).__init__()
        self.channel = channel
        self.logname = logname
        self.args = args
        self.func=func
        self.mode = 0
        self.log = csvreport(self.logname)
        self.log.mode = 1
        self.mythc=thc.thc(chn_thc, device, nolog = True)
        self.scan_times=10

    def socket_set(self, binname = "", mode = 0):
        '''
        the function is to configure whether to download chip

            :binname:
                name of bin to be downloaded into chip

            :mode:
                0. flash existing on socket board has been downloaded before test?
                1. no flash on socket board or only need to download bin into ram for each chip
        '''
        self.mode = mode
        self.binname = binname

    def __servo_run(self):
        while True:
            IN = raw_input('\033[1;32menter \"q or Q\" to quit temporarily, else continue\n:')  
            time.sleep(2)     
            if IN == "q" or IN == "Q": # make end of current temperature test
                break

            if self.mode ==1:
                # close channel for download bin
                self.channel.deinit()
                if self.__download_bin() == -1:
                    continue                
                self.channel.open()
            self.func(self.args, self.log)

    def run(self, temper_list):
        '''
        the function defines the main process of whole test, in which tests 

            :temper_list:
                temperature list for socket test, string of list type
                "[]": no temperature condition, only test once
                "t_array": here t_array is a temperature list, e.g. range(10, 40, 10), [-40, 10, 120],
                           in sequence of which tests could be repeatively executed
        '''        
        if len(temper_list)==0:
            temp_loop_list = [""]
        else:
            temp_loop_list = temper_list
            
        for index, subres in enumerate(temp_loop_list):
            if temp_loop_list[index] != "":
                if index!=0:
                    self.log.flush_line()
                
                temper_sta, temper_ret=self.mythc.temper_set(subres, self.scan_times)
                if temper_sta==0:
                    logwarn("End the test!")  
                    break               
                elif temper_sta==1:
                    real_temper = temper_ret
                    self.log.write_value('temperature/C', real_temper)       
            self.__servo_run()
        self.log.deinit()  

    def __download_bin(self):
        com_port=self.channel.ComPort
        ret = os.system(DOWNLOAD_CMD%(com_port, BIN_PATH+self.binname))    
        if ret >> 8 == 2:
            logerror("download fail")
            return -1
        return 1