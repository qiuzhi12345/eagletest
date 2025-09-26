import os
import pylink
from baselib.loglib.log_lib import *
from baselib.instrument import tester
from hal.common import *
from hal.Init import *
from hal.bt_api import BTAPI
from hal.wifi_api import WIFIAPI
from hal.hwregister.hwreg.all import *
from hal.hwregister.hwi2c.all import *
from hal.hwregister.hwpbus.all import *
from rftest.rflib.wifi_lib import WIFILIB
from rftest.rflib.adc_dump import DUMP
from rftest.rflib.iq_est import IQ_EST
from rftest.rflib.rfpll import rfpll
from rftest.rflib.rfcal import rfcal
from rftest.rflib.pbus import pbus
from rftest.rflib.saradc import SARADC
from rftest.rflib import rfglobal
from baselib.instrument.tester_serv.instrum_server import instru_server
from rftest.testcase.current.current_meas import RF_Curr

from rftest.testcase.rf_debug.i2c_sweep import I2C_SWEEP
from rftest.testcase.rf_debug.tx_gain_sweep import Sweep_TX_Gain
from rftest.testcase.rf_debug.rx_gain_sweep import Sweep_RX_Gain
from rftest.testcase.rf_debug.power_detect import PwrDet
from rftest.testcase.rf_debug.pa_test import PA_OutPwr
from rftest.testcase.rf_debug.basic_test import BasicTest
from rftest.testcase.rf_debug.rx_freq_tolerence import RxFreqTol
from rftest.testcase.rf_debug.filter_test import filter_test
from rftest.testcase.rf_debug.packets_test import Packet_Test
from rftest.testcase.rf_debug.txdc_fluctuation import TXDC_fluctuation
from rftest.testcase.rf_debug.iperf_test import Iperf_Test
from rftest.testcase.rf_debug.phase_noise import PHASE_NOISE

if platform.platform().find("Linux") != -1:
    logwarn("platform is not support ACPR")
else:
    from rftest.testcase.performance.acpr_test import RF_ACPR
    from rftest.testcase.performance.Interfer_miti_test import Interfer_Test
    from rftest.testcase.performance.bt_acpr_test import Bt_Interfer_Test
    from rftest.testcase.performance.wifi_auto_test import WiFiAutoTest
    from rftest.testcase.performance.bt_auto_test import BtAutoTest
    from rftest.testcase.performance.wifi_txrx_test import WIFI_TXRX_TEST
    from rftest.testcase.performance.wifi_tx_test import WIFI_TX_TEST
    from rftest.testcase.rf_debug.rfpll_test import RFPLL_TEST
    from rftest.testcase.performance.rf_bin_test import RF_Bin_Test
    from rftest.testcase.performance.wifi_feature_case import WIFI_Feature_Case
    from rftest.testcase.performance.tx_ack_test import ACK_Test
    from rftest.testcase.performance.rf_test_case import RF_TEST_CASE
    from rftest.testcase.performance.tester_cal_pwr import TESTER_CAL_PWR
    from rftest.testcase.performance.bt_test_cmw import bt_test ,bt_signaling,bt_curr,testpin,BQB_autotest,gdb_load_code,gdb_server
    from rftest.testcase.performance.bt_test_cmw import BT_MODEM_BASE,BT_RF_BASE,BT_CORE_BASE
data_path = './rftest/rfdata'
file_name_lst = ['bt_auto_data','i2c_auto_data','rf_curr_data','rf_acpr_data','rf_wifi_autotest_data','sweep_tx_gain','sar_pwrdet_data','pa_outpwr_data','rf_wifi_qickly_test_data','rf_rxfreqtol_data','rf_bin_test']



class RFTCS(object):
    """docstring for TCS"""
    def __init__(self, comport, chipv = "AUTO", jlink_en=1, jlink_sn='601012495'):
        self.comport = comport
        # try:
        self.hals = HALS(self.comport, chipv)
        self.chipv = self.hals.chipv
        loginfo("Dectect chip: %s"%(self.chipv))
        self.jlink_en = jlink_en
        # if jlink_en != 0:
        #     self.jlink = pylink.JLink()
        #     self.jlink_sn = jlink_sn
        #     self.jlink.open()
        #     self.jlink.set_tif(pylink.enums.JLinkInterfaces.SWD)
        #     self.jlink.connect('ARMCM4_FP')


        if self.chipv == "epm9062":
            rfglobal.BT_MODEM_BASE = 0x50420000
            rfglobal.BT_RF_BASE = 0x50421000
            rfglobal.BT_CORE_BASE = 0x50422000
            rfglobal.BT_BASEBAND = 0x50400000

        elif self.chipv == "TX232_MPW3":
            rfglobal.BT_MODEM_BASE = 0xA0420000
            rfglobal.BT_RF_BASE = 0xA0421000
            rfglobal.BT_CORE_BASE = 0xA0422000
            rfglobal.BT_BASEBAND = 0xa0400000

        #common
##        self.wifitx_api = WIFITX_API(self.comport,self.chipv)
##        self.wifirx_api = WIFIRX_API(self.comport,self.chipv)
        self.HWPBUS= HWPBUS(self.comport,self.chipv)
        self.HWREG = HWREG(self.comport, self.chipv)
        self.HWI2C = HWI2C(self.comport, self.chipv)

        self.wifiapi = WIFIAPI(self.comport,self.chipv)
        self.i2c = HWI2C(self.comport,self.chipv)
        self.mem = MEM(self.comport,self.chipv)
        self.MEM = MEM(self.comport,self.chipv)
        self.mem_ts = MEM_TS(self.comport,self.chipv)
        self.MEM_TS = MEM_TS(self.comport,self.chipv)
        if jlink_en != 0:
            if self.chipv == "epm9062":
                gdb_server('N22')
                self.JLINK = MEM_GDB()
            elif self.chipv == "TX232_MPW3":
                self.JLINK = jlink(jlink_sn=jlink_sn)
        #rflib
        self.adc_dump = DUMP(self.comport,self.chipv)
##        self.wifitx = WIFITX(self.comport,self.chipv)
##        self.wifirx = WIFIRX(self.comport,self.chipv)
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.bt = BTAPI(self.comport,self.chipv)
        self.bt_ts = bt_test(self.comport,self.chipv)
        # self.csp = bt_signaling(self.comport,self.chipv)
##        self.btrx = BTRX(self.comport,self.chipv)
        self.rfpll = rfpll(self.comport,self.chipv)
        self.rfcal = rfcal(self.comport,self.chipv)
        self.pbus = pbus(self.comport,self.chipv)
        self.PBUS = pbus(self.comport,self.chipv)
        self.saradc = SARADC(self.comport,self.chipv)
        self.iq_est = IQ_EST(self.comport,self.chipv)

        # caselist
##        self.rf_curr = RF_Curr(self.comport,self.chipv)
##        self.rf_acpr = RF_ACPR(self.comport,self.chipv)
##        self.wifi_auto_test = WiFiAutoTest(self.comport,self.chipv)
        self.bt_auto_test = BtAutoTest(self.comport,self.chipv)
        self.bt_acpr_test = Bt_Interfer_Test(self.comport,self.chipv)
#         self.i2c_sweep = I2C_SWEEP(self.comport,self.chipv)
##        self.tx_gain_sweep = Sweep_TX_Gain(self.comport,self.chipv)
##        self.rx_gain_sweep = Sweep_RX_Gain(self.comport,self.chipv)
##        self.saradc = SARADC(self.comport,self.chipv)
##        self.pwrdet = PwrDet(self.comport,self.chipv)
##        self.wifi_test_simple = WIFI_TEST_SIMPLE(self.comport,self.chipv)
##        self.pa_outpwr = PA_OutPwr(self.comport,self.chipv)
##        self.basic_test = BasicTest(self.comport,self.chipv)
##        self.rx_freq_tol_test = RxFreqTol(self.comport,self.chipv)
##        self.rf_bin_test = RF_Bin_Test(self.comport,self.chipv)

        #except:
        #logwarn("Load RFTCS fail")
        if os.path.exists(data_path):
            pass
        else:
            os.mkdir(data_path)

        for file_name in file_name_lst:
            if os.path.exists(data_path+'/'+file_name):
                pass
            else:
                os.mkdir(data_path+'/'+file_name)

    def deinit(self):
        self.comport.deinit()
        if self.jlink_en != 0:
            self.JLINK.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.deinit()


