import os
import pylink
from baselib.loglib.log_lib import *

from hal.common import jlink
from hal.common import *
from rftest.rflib.adc_dump import DUMP
from rftest.testcase.filter_test import filter_test
from rftest.testcase.bt_api import bt_api
from rftest.testcase.bt_nosignal_test import bt_nosignal_test
from rftest.testcase.bt_signal_test import bt_signaling,BQB_autotest
from rftest.testcase.curr_test import bt_curr
from rftest.testcase.rf_debug import rf_debug
from rftest.testcase.rf_diag_test import rf_diag_test
from rftest.testcase.test_pin import testpin
from rftest.testcase.excel_to_code import excel_to_c
from rftest.testcase.gdb import gdb_server,gdb_load_code

data_path = './rftest/rfdata'
# file_name_lst = ['bt_auto_data','i2c_auto_data','rf_curr_data','rf_acpr_data','rf_wifi_autotest_data','sweep_tx_gain','sar_pwrdet_data','pa_outpwr_data',
#                   'rf_wifi_qickly_test_data','rf_rxfreqtol_data','rf_bin_test']



class RFTCS(object):
    """docstring for TCS"""
    def __init__(self, comport, chipv = "AUTO", jlink_en=1, jlink_sn='59610042'):
        self.comport = comport
        # try:
        # self.hals = HALS(self.comport, chipv)
        self.chipv = chipv
        # loginfo("Dectect chip: %s"%(self.chipv))
        self.jlink_en = jlink_en
        # if jlink_en != 0:
        #     self.jlink = pylink.JLink()
        #     self.jlink_sn = jlink_sn
        #     self.jlink.open()
        #     self.jlink.set_tif(pylink.enums.JLinkInterfaces.SWD)
        #     self.jlink.connect('ARMCM4_FP')


        #common

        self.mem = MEM(self.comport,self.chipv)
        self.MEM = MEM(self.comport,self.chipv)
        self.mem_ts = MEM_TS(self.comport)
        self.MEM_TS = MEM_TS(self.comport)
        self.adc_dump = DUMP(self.comport, self.chipv)
        if jlink_en != 0:
            self.JLINK = jlink(jlink_sn=jlink_sn)
        #rflib
            self.bt_api = bt_api(self.comport,self.chipv,jlink=self.JLINK ,jlink_en=jlink_en)
            self.bt_nosignal_test = bt_nosignal_test(self.comport,self.chipv,jlink=self.JLINK ,jlink_en=jlink_en)
            self.curr_test = bt_curr(self.comport,self.chipv,jlink=self.JLINK ,jlink_en=jlink_en)
            self.rf_debug = rf_debug(self.comport,self.chipv,jlink=self.JLINK ,jlink_en=jlink_en)
            self.rf_diag_test = rf_diag_test(self.comport,self.chipv,jlink=self.JLINK ,jlink_en=jlink_en)
            self.test_pin = testpin(self.comport,self.chipv,jlink=self.JLINK ,jlink_en=jlink_en)
        else:
            self.bt_api = bt_api(self.comport,self.chipv,jlink_en=jlink_en)
            self.bt_nosignal_test = bt_nosignal_test(self.comport,self.chipv,jlink_en=jlink_en)
            self.curr_test = bt_curr(self.comport,self.chipv,jlink_en=jlink_en)
            self.rf_debug = rf_debug(self.comport,self.chipv,jlink_en=jlink_en)
            self.rf_diag_test = rf_diag_test(self.comport,self.chipv,jlink_en=jlink_en)
            self.test_pin = testpin(self.comport,self.chipv,jlink_en=jlink_en)

        # self.csp = bt_signaling(self.comport,self.chipv)

        # caselist

        #except:
        #logwarn("Load RFTCS fail")
        if os.path.exists(data_path):
            pass
        else:
            os.mkdir(data_path)

        # for file_name in file_name_lst:
        #     if os.path.exists(data_path+'/'+file_name):
        #         pass
        #     else:
        #         os.mkdir(data_path+'/'+file_name)

    def deinit(self):
        self.comport.deinit()
        if self.jlink_en != 0:
            self.JLINK.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.deinit()


