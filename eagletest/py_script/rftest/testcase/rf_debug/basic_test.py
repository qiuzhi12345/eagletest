import random
import time
import numpy as np
import pandas as pd
from baselib.test_channel.com import COM as com
from baselib.tc_platform.common import Multiboard_CTL as Multiboard_CTL
from baselib.loglib.log_lib import *
from hal.hwregister.hwi2c.all import *
from hal.common import *
from rftest.rflib import rfglobal
from rftest.rflib.wifi_lib import WIFILIB
from rftest.rflib.pbus import pbus
from rftest.rflib.rfpll import rfpll
from rftest.rflib.csv_report import csvreport
from rftest.rflib.utility import iofunc
from hal.wifi_api import WIFIAPI
from baselib.instrument.spa import HP,Agilent
from baselib.instrument import dm,tester
from hal.rtc_debug import RTC_DEBUG
import rftest.testcase.performance.data_summary as data_summary
import csv

mem_date_dict={
    "agc":      0x6001c3fc,
    "bb":       0x6001d3fc,
    "bbtx":     0x6001c7fc,
    "brx":      0x6001cb84,
    "nrx":      0x6001cffc,
    "FE":       0x600060fc,
    "FE2":      0x600051fc,
    "i2c_mst":  0x6000e3fc,
    "apb_ctrl": 0x600263fc,
    "rtc_ctrl": 0x6000813c
}

i2c_test_dict={
    'bias':      'rc_dcap_ext',
    'bbpll':     'ir_cal_delay',
    'rfrx':      'rfrx_lna_dcap',
    'rftx':      'TMX2G_CCT_LOAD',
    'bbtop':     'filter_wifirx0_dcap_lq',
    'ckgen':     'dres_pp2g',
    'xtal':      'enb_sck_xtal',
    'rfpll':     'ir_fcal_delay',
    'rfpll_sdm': 'lf_dlfcal',
    'apll':      'ir_cal_delay',
    'ulp':       'ext_code',
    'sar':       'sar1_smp_count'
}

i2c_max_addr={
    'bias':      range(0,5) + range(6,10),
    'bias_marlin3': range(0,5) + range(6,10),
    'bbpll':     range(0,8) + range(9,11),
    'rfrx':      range(0,11),
    'rftx':      range(0,12),
    'bbtop':     range(0,37),
    'ckgen':     range(0,5) + range(7,9),
    'xtal':      range(0,2),
    'rfpll':     range(0,5) + range(8,12),
    'rfpll_sdm': range(0,6),
    'apll':      range(0,3) + range(4,10),
    'ulp':       range(0,3) + range(5,9),
    'sar':       range(0,8)
}

pbus_dict={
    'rfrx1': ['en1'],
    'rftx1': ['en1'],
    'rftx2': ['en1'],
    'bb':    ['en1', 'en2'],
    'dcoi':  ['en1', 'en2'],
    'dcoq':  ['en1', 'en2']
}

class BasicTest(object):

    def __init__(self,comport,chipv):
        self.comport = comport
        self.chipv = chipv
        self.mem = MEM(self.comport,self.chipv)
        self.pbus = pbus(self.comport, self.chipv)
        self.wifi = WIFILIB(self.comport,self.chipv)
        self.rfpll = rfpll(self.comport, self.chipv)
        self.mac = self.wifi.read_mac()
        self.i2c = HWI2C(self.comport,self.chipv)
        #self.mcu = Multiboard_CTL(self.comport)
        self.wifiapi = WIFIAPI(self.comport,self.chipv)
        self.rtc_debug = RTC_DEBUG(self.comport,self.chipv)


    def mem_test(self):
        '''
        :brief: mem read and write test
        :param: - no param
        :return: - no return
        '''
        test_m = {"agc","bb","bbtx","brx","nrx","FE","FE2","i2c_mst","apb_ctrl","rtc_ctrl"}
        for module in test_m:
            addr = mem_date_dict[module]
            data_org = self.mem.rdm(addr, 27, 0)
            for wdata in range(0, 2):
                self.mem.wrm(addr, 27, 0, wdata)
                rdata = self.mem.rdm(addr, 27, 0)
                if rdata == wdata:
                    logres('MEM test: %s 0x%x %d=%d pass'%(module, addr, rdata,wdata))
                else:
                    logres('MEM test: %s 0x%x %d=%d fail!!!'%(module, addr, rdata,wdata))
            self.mem.wrm(addr, 27, 0, data_org)

    def mem_test_one(self, base_addr=0x60008800, length=0xfc):
        '''
        :brief: mem read and write test
        :param: - no param
        :return: - no return
        '''
        logsetlevel("ERROR")
        for i in range(0, length, 4):
            addr = base_addr+i
            for wdata in range(0, 2):
                self.mem.wr(addr, wdata)
                rdata = self.mem.rd(addr)
                if rdata == wdata:
                    logres('MEM test:0x%x %d=%d pass'%(addr, rdata,wdata))
                else:
                    logres('MEM test:0x%x %d=%d fail!!!'%(addr, rdata,wdata))
        logsetlevel("DEBUG")

    def i2c_test(self):
        '''
        :brief: i2c read and write test
        :param: - no param
        :return: - no return
        '''
        logsetlevel("ERROR")
        fail_num = 0
        i2c_block = self.wifi.i2c_block_get()
        self.mem.wrm(0x60008034, 24, 24, 1)  #apll force pu
        for module in i2c_block:
            print module
            reg = i2c_test_dict[module]
            data_org = self.wifi.i2c_ric(module, reg)
            for i in range(0,2):
                wdata = data_org-i
                if wdata==-1:
                    wdata = 1
                self.wifi.i2c_wic(module, reg, wdata)
                rdata = self.wifi.i2c_ric(module, reg)
                if rdata == wdata:
                    logres('I2C test: %s %s %d=%d pass'%(module,reg, rdata,wdata))
                else:
                    logres('I2C test: %s %s %d=%d fail!!!'%(module,reg, rdata,wdata))
                    fail_num += 1
            self.wifi.i2c_wic(module, reg, data_org)
        self.mem.wrm(0x60008034, 24, 24, 0)  #apll force pu
        logsetlevel("DEBUG")
        return fail_num

    def pbus_test(self):
        '''
        :brief: pbus read and write test
        :param: - no param
        :return: - no return
        '''
        logsetlevel("ERROR")
        test_m = {'rftx1','rftx2','rfrx1','bb','dcoi','dcoq'}
        self.pbus.pbus_debugmode()

        for module in test_m:
            en_m = pbus_dict[module]
            for en in en_m:
                for wdata in range(0, 2):
                    self.pbus.pbus_wr(module, en, wdata)
                    rdata = self.pbus.pbus_rd(module, en)
                    if rdata == wdata:
                        logres('PBUS test: %s %s %d=%d pass'%(module,en, rdata,wdata))
                    else:
                        logres('PBUS test: %s %s %d!=%d fail!!!'%(module,en, rdata, wdata))
        self.pbus.pbus_workmode()
        logsetlevel("DEBUG")

    def code2int(self,code):
        """Convert a string code to int."""
        if isinstance(code, str):
            if code.startswith('0x'):   #hex
                code = int(code, 16)
            else:
                code = int(code)
        return code

    def i2c_data_read(self, block, i2c_regdict, instr=''):
        regdict = i2c_regdict[block]
        title = 'ctrl_name, addr, msb, lsb, data\n'
        fname = self.wifi.get_filename('i2c_table_read', 'i2c_%s'%block, 'i2c_table_read_%s'%instr)
        csvreport1=csvreport(fname, title, no_time=1)
        for ctrl_name in regdict:
##            print ctrl_name
            [addr, msb, lsb] = regdict[ctrl_name][0:3]
            code = self.wifi.i2c_ric(block, ctrl_name)
            data = self.code2int(code)
##            print code
            csvreport1.write_data([ctrl_name, addr, msb, lsb, data])

    def i2c_table_read(self, instr=''):
        print instr
        i2c_regdict = self.wifi.i2c_regdict_get()
        i2c_block = self.wifi.i2c_block_get()
        for block in i2c_block:
            self.i2c_data_read(block, i2c_regdict, instr)

    def agc_mem_read(self):
        title = 'addr, data\n'
        fname = self.wifi.get_filename('agc_mem_read', 'agc_mem_read')
        csvreport1=csvreport(fname, title)
        base_addr = 0x6001c000
        for i in range(0,0x159,4):
            addr = base_addr+i
            data = self.mem.rd(addr)
            csvreport1.write_data([hex(addr), hex(data)])

        addr = base_addr+0x3fc
        data = self.mem.rd(addr)
        csvreport1.write_data([hex(addr), hex(data)])

    def esp8266_sar_read(self):

        # set pbus and test reg
        self.i2c.saradc.en_pa=1
        self.i2c.rftx.TE_PWDET= 1      # Test Enable

        self.pbus.pbus_debugmode()
        self.pbus.pbus_wr('rftx1','en1', 2)        # Power up PWDET
        self.i2c.saradc.en_test = 1            # select Test MUX

        # SARADC read code
        self.mem.wr(0x60000710,(self.mem.rd(0x60000710)&0xfdffffff | (0x1<<25))) #XPD_SAR_I2C=bit[25]
        self.i2c.saradc.xpd_sar=1  #xpd_sar=bit[4]

        self.mem.setmask(0x60000D5c,0x800000)
        self.mem.clrmask(0x60000D5c,0x200000)

        self.mem.clrmask(0x60000D50,0x2)
        self.mem.setmask(0x60000D50,0x2)

        d_str=''
        e=[1,2,3,4,5,6,7,8]
        for i in range(0,8):
           c=self.mem.rd(0x60000D80+i*4)&0xfff
           e[i] = 2048-c
           d_str = d_str+'%d,'%e[i];

        vout = np.average(e)/2048.0*1.0

        # recover the initial pbus and reg settings
        self.pbus.pbus_wr('rftx1','en1', 0)        # Power up PWDET
        self.i2c.saradc.en_test = 0            # select Test MUX

        self.i2c.saradc.en_pa = 0
        self.i2c.rftx.TE_PWDET = 0      # Test Enable

        vout = vout*12/11
        return vout

    def i2c_clk_test(self, name_str=''):
        logsetlevel('I')
        num_str = ''
        for i in range(1, 20):
            num_str+='%d,'%i
        title = 'block, clk_sel, read_fail_num, read_data%s\n'%num_str
        fname = self.wifi.get_filename('i2c_clk_test_%s'%name_str, 'i2c_clk_test_%s'%name_str)
        csvreport1=csvreport(fname, title)

        self.wifiapi.i2c_clk_change(0)
        self.wifiapi.pll_cap_track_en(0)
        self.mem.wrm(0x60008034, 24, 24, 1)  #apll force pu
        i2c_block = self.wifi.i2c_block_get()
        fail_dict = ''
        for block in i2c_block:
            max_addr_m = i2c_max_addr[block]
            max_addr = max_addr_m[-1]+1
            print block
            print max_addr
            fail_num_m = []
            for clk_sel in range(5,-1, -1):
                self.wifiapi.i2c_clk_sel(clk_sel)
                fail_num = 0
                read_data = []
                data_ones = 0
                data_zeros = 0
                num_i = 0
                for addr in range(0, max_addr):
                    if addr == max_addr_m[num_i]:
                        data = self.wifi.i2c_ri(block, addr)
                        num_i += 1
                    else:
                        data = 0
                    read_data.append(data)
                    if data==0xff:
                        data_ones += 1
                    if data==0x0:
                        data_zeros += 1
                loginfo('block=%s, clk_sel=%d'%(block, clk_sel))
                loginfo(read_data)
                if clk_sel==5:
                    read_data_org = read_data
                if (read_data_org != read_data) or (data_ones>=max_addr-1) or (data_zeros>=max_addr-1):
                    fail_num = 1
                fail_num_m.append(fail_num)

                csvreport1.write_data([block, clk_sel, fail_num, read_data])

            if fail_num_m != [0,0,0,0,0,0]:
                fail_dict += '%s,%s\n'%(block, fail_num_m)
        csvreport1.write_string(fail_dict)
        self.mem.wrm(0x60008034, 24, 24, 0)  #apll force pu
        self.wifiapi.i2c_clk_change(1)
        logsetlevel('D')
        loginfo(fail_dict)
        return fail_dict

    def dtest_vol_test(self, cp_reg=7, name_str=''):
##        logsetlevel('I')
        mux_dict={
        'bbpll': ['ent_adc[4]', 'ent_pll','dtest'],
        'rfrx': ['ent_vga', 'ent_lna', 'ent_mx','dtest'],
        'rftx': ['TE_PWDET',''],
        'ckgen': ['ent_ckgen_pkdet','dtest_ckgen_pkdet'],
        'rfpll': ['ent_vco', 'ent_vco_bias', 'dtest'],
        'bias_marlin3': ['ent_consti', 'ent_cpreg', 'ent_cgm','ent_bg','dtest']
        }
##        block_m = ['bbpll', 'rfrx', 'rftx', 'ckgen', 'rfpll','bias_marlin3']
        block_m = ['bias_marlin3']

        title = 'mac, pvt, block, ent_reg, dtest, dm_volt, sar2_atten0_code, sar2_atten1_code, sar2_atten2_code, sar2_atten3_code\n'
        fname = self.wifi.get_filename('dtest_vol_test', 'dtest_vol_test_%s'%name_str)
        csvreport1=csvreport(fname, title)

        pvt = self.wifiapi.pvt_test()

        self.mydm = dm.dm()
##        self.mydm.start_rate(meastype='VOLT')
        if cp_reg==7:
            self.i2c.bias_marlin3.cp1p6_dreg=7
            self.i2c.bias_marlin3.cp1p2_dreg=7
            self.i2c.bias_marlin3.cp1p1_pvt_reg=7
            self.i2c.bias_marlin3.dres12k=7
        else:
            self.i2c.bias_marlin3.cp1p6_dreg=7
            self.i2c.bias_marlin3.cp1p2_dreg=7
            self.i2c.bias_marlin3.cp1p1_pvt_reg=4
            self.i2c.bias_marlin3.dres12k=7

        for block in block_m:
            reg_m = mux_dict[block]
            length = len(reg_m)
            for i in range(0,length-1):
                ent_reg = reg_m[i]
                dtest_reg = reg_m[-1]

                if ent_reg[-1]==']':
                    reg = ent_reg[0:-3]
                    data_max = int(ent_reg[-2])
                else:
                    reg = ent_reg
                    data_max = 2

                if dtest_reg != '':
                    dtest_max = 4
                else:
                    dtest_max = 1

                for reg_data in range(1,data_max):
                    for dtest_data in range(0, dtest_max):
                        self.wifi.i2c_wic(block, reg, reg_data)
                        if dtest_reg != '':
                            self.wifi.i2c_wic(block, dtest_reg, dtest_data)

                        reg_str = '%s_%d'%(reg, reg_data)
                        dtest_str = '%s_%d'%(dtest_reg, dtest_data)
                        code = []
                        for atten in range(0,4):
                            code.append(self.wifiapi.get_sar2_vol(atten))

                        self.rtc_debug.pull_internal_voltage(1)
                        time.sleep(0.2)
                        dm_volt = self.mydm.get_result("VDC",data_type = 'MAX')

                        csvreport1.write_data([self.mac, pvt, block, reg_str, dtest_str, dm_volt, code])
                        print [pvt, block, reg_str, dtest_str, dm_volt, code]

                self.wifi.i2c_wic(block, reg, 0)
                if dtest_reg != '':
                    self.wifi.i2c_wic(block, dtest_reg, 0)



    def mcu_ctrl_uart_reset(self,dut_sel=[]):
        for chip_sel in dut_sel:
            loginfo('dut_sel reset: %d start!!!'%chip_sel)
            self.mcu.mcu_reset(chip_sel-1)
            time.sleep(5)
            loginfo('dut_sel reset: %d end!!!'%chip_sel)


    mem_dict = {
    'MACRX': [0x60033000,0x3f8],
    'MACTX': [0x60033400,0x3f8],
    'MACSEC': [0x60033800,0x3f8],
    'MACSCH': [0x60033c00,0x3fc],
    'MACTXQ': [0x60034000,0x400],
    'MACPWR': [0x60035000,0x3f8],
    'fe':     [0x60006000,0x1fc],
    'fe2':    [0x60005000,0x1fc],
    'i2cmst': [0x6000e000,0x3fc],
    'agc':    [0x6001c000,0x3fc],
    'bbtx':   [0x6001c400,0x3fc],
    'brx':    [0x6001c800,0x384],
    'nrx':    [0x6001cc00,0x3fc],
    'bb':     [0x6001d000,0x3fc]
    }

    mem_dict_8266 = {
    'rtc':    [0x60000700,0xfc],
    'fe':     [0x60000400,0xfc],
    'fe2':    [0x60000500,0xfc],
    'i2cmst': [0x60000d00,0xfc],
    'bb':     [0x60009800,0x7fc]
    }




    def mem_block_read(self, block='MAC_SCH', base_addr=0x60033c00, offset=0x3fc, instr=''):
        title = 'block, address, data\n'
        fname = self.wifi.get_filename('mem_block_read',  'mem_block_read_%s'%(block), 'mem_block_read_%s'%instr)
        csvreport1 = csvreport(fname, title, no_time=1)
        for i in range(0, offset+1, 4):
            address = base_addr+i
            data = self.mem.rd(address)
            csvreport1.write_data([block, hex(address), hex(data)])

    def mem_all_read(self, instr=''):
        #block_m = ['MACRX', 'MACTX', 'MACSEC', 'MACSCH', 'MACTXQ', 'MACPWR']
        if self.chipv=='ESP8266':
            block_m = ['rtc','fe', 'fe2', 'i2cmst','bb']
        else:
            block_m = ['fe', 'fe2', 'i2cmst','agc','bbtx','brx','nrx','bb']
        for block in block_m:
            if self.chipv=='ESP8266':
                addr = self.mem_dict_8266[block]
            else:
                addr = self.mem_dict[block]
            self.mem_block_read(block, addr[0], addr[1], instr)

    def csv_data_check(self, reg_csv='', reg_base=0x0, data_csv=''):
        fi = open(reg_csv, 'r')
        reg_info = []
        i = 0
        for line in fi:
            if i > 0:
                line = line.split(';')
    ##            addr = line[0]
                if line[0] !='':
                    addr = line[0].replace(' ','')
                    addr = hex(int(addr,16)+reg_base)
                sig = line[6].replace(' ','')
                bits = line[7].replace(' ','').replace('[','').replace(']','')
                bits = bits.split(':')
                if len(bits)==2:
                    max_bit = bits[0]
                    min_bit = bits[1]
                else:
                    max_bit = bits[0]
                    min_bit = bits[0]
                default = line[8]
                rw = line[9]
                reg_info.append([addr, max_bit, min_bit, sig, rw, default])
            i += 1
        print reg_info
    def reg_table_default_gen(self, path=''):
        '''
        path:   chip reg_csv folder path
        '''
        reg_base_dict = {
        'MACRX': [0x60033000,0x3f8],
        'MACTX': [0x60033400,0x3f8],
        'MACSEC': [0x60033800,0x3f8],
        'MACSCH': [0x60033c00,0x3fc],
        'MACTXQ': [0x60034000,0x400],
        'MACPWR': [0x60035000,0x3f8],
        'fe':     [0x60006000,0x1fc],
        'fe2':    [0x60005000,0x1fc],
        'i2cmst': [0x6000e000,0x3fc],
        'agc':    [0x6001c000,0x3fc],
        'bb_tx':   [0x6001c400,0x3fc],
        'brx':    [0x6001c800,0x384],
        'nrx':    [0x6001cc00,0x3fc],
        'bb':     [0x6001d000,0x3fc]
        }
        file_list=os.listdir(path)
        fname = self.wifi.get_filename('reg_table_gen',  'reg_table_gen')
        logtime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))

        self.filename = '%s_%s.xlsx'%(fname, logtime)
        writer = pd.ExcelWriter(self.filename,mode='a')

        for f in file_list:
            fi = open('%s/%s'%(path,f), 'r')
            f_name = f.split('.')[0][:-4]
            print f_name

            if f_name in reg_base_dict:
                reg_base = reg_base_dict[f_name][0]
                reg_info = []
                fi.next()
                for line in fi:
                    line = line.split(';')
                    if line[0] !='':
                        addr = line[0].replace(' ','')
                        print addr
                        addr = hex(int(addr,16)+reg_base)
                    sig = line[6].replace(' ','')
                    if sig !='':
                        bits = line[7].replace(' ','').replace('[','').replace(']','')
                        bits = bits.split(':')
                        if len(bits)==2:
                            max_bit = bits[0]
                            min_bit = bits[1]
                        else:
                            max_bit = bits[0]
                            min_bit = bits[0]
                        default = eval('0x%s'%(line[8].split("'")[1][1:].replace('_','')))
                        rw = line[9]
                        reg_info.append([addr, eval(max_bit), eval(min_bit), sig, rw, default])
                df = pd.DataFrame(reg_info,columns=['addr','msb','lsb','ctrl_name','rw','default'])
                df.to_excel(writer,sheet_name=f_name,index=False)
                writer.save()
    def reg_table_check(self,f=''):
        '''
        f:  reg_table_default file
        '''
        xl=pd.ExcelFile(f)
        sheetname_list=xl.sheet_names

        fname = self.wifi.get_filename('reg_table_check',  'reg_table_check')
        logtime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))
        self.filename = '%s_%s.xlsx'%(fname, logtime)
        writer = pd.ExcelWriter(self.filename,mode='a')

        for sheetname in sheetname_list:
            df = pd.read_excel(f,index=False,sheet_name=sheetname)
            diff = []
            for i in df.index:
                addr = eval(df.iloc[i,0])
                msb = df.iloc[i,1]
                lsb = df.iloc[i,2]
                ctrl_name = df.iloc[i,3]
                rw = df.iloc[i,4]
                dft = df.iloc[i,5]
                value = self.mem.rdm(addr,msb,lsb)
                logdebug('{},{},{},{},{},{}'.format(hex(addr),msb,lsb,ctrl_name,dft,value))
                if value != dft :
                    diff.append([hex(addr),msb,lsb,ctrl_name,rw,dft,value])
            df_diff = pd.DataFrame(diff,columns=['addr','msb','lsb','ctrl_name','rw','default','rd_value'])
            df_diff.to_excel(writer,sheet_name=sheetname,index=False)
            writer.save()

    def mem_sleep_check(self, wr_en=0):
        if self.chipv=='ESP8266':
            block_m = ['rtc','fe', 'fe2', 'i2cmst','bb']
        else:
            block_m = ['fe', 'fe2', 'i2cmst','agc','bbtx','brx','nrx','bb']
        for block in block_m:
            if self.chipv=='ESP8266':
                addr = self.mem_dict_8266[block]
            else:
                addr = self.mem_dict[block]
            address = addr[0]+addr[1]
            if(wr_en==1):
                self.mem.wr(address, 0x5a5a5a5a)
            else:
                loginfo("%s, 0x%x=0x%x\n"%(block, address, self.mem.rd(address)))


    def test_txcap(self, num=0):
        title = 'num, chan, txpwr, TMX2G_CCT_LOAD, PA2G_CCT_STG1, PA2G_CCT_STG2\n'
        fname = self.wifi.get_filename('test_txcap',  'test_txcap')
        csvreport1 = csvreport(fname, title, 1)
        for chan in range(1, 15):
            self.wifi.rfchsel(chan)
            self.wifiapi.set_tx_gain(0x4f, 0x20)
            self.wifi.force_txon(1)
            txpwr = self.wifiapi.meas_tone_pwr_db(40, 64)
            self.wifi.force_txon(0)
            TMX2G_CCT_LOAD = self.i2c.rftx.TMX2G_CCT_LOAD
            PA2G_CCT_STG1 = self.i2c.rftx.PA2G_CCT_STG1
            PA2G_CCT_STG2 = self.i2c.rftx.PA2G_CCT_STG2
            csvreport1.write_data([num, chan, txpwr, TMX2G_CCT_LOAD, PA2G_CCT_STG1, PA2G_CCT_STG2])

    def rfpll_cap_time(self):
        title = ''
        for i in range(0, 40):
            title += '%d,'%i
        fname = self.wifi.get_filename('rfpll_cap_time',  'rfpll_cap_time')
        csvreport1 = csvreport(fname, title)
        for chan in range(1, 15):
            ostr = self.wifi.rfchsel(chan)
            csvreport1.write_string("\nchan=%d\n"%chan+ostr)
##            self.wifi.force_txon(1)
##            self.wifi.txtone(1, 2, 40)
##            ostr = self.wifi.rfchsel(chan)
##            csvreport1.write_string("\nchan=%d\n"%chan+ostr)
##            self.wifi.force_txon(0)
##            self.wifi.txtone(0, 2, 40)



    def test_rxreg_esp32(self,wr_en=0):

        logsetlevel("INFO")
        # 1 : cca
        if(wr_en==1):
            self.mem.wrm(0x6001c01c,  7,  0, 0xBF) # org :  0x1F
            self.mem.wrm(0x6001c018, 30, 30, 1)# org :  0x0
        else:
            loginfo("cca,0x%x,0x%x\n"%(self.mem.rdm(0x6001c01c, 7,0), self.mem.rdm(0x6001c018,30,30)))
        # 2 : hung thr
        if(wr_en==1):
            self.mem.wrm(0x60033c1c, 11, 0, 0x00d) # LR_mode :  0x03d , org : 0xf0
            self.mem.wrm(0x60033c20, 11, 0, 0x00c) # LR_mode :  0x035 , org : 0xf0
        else:
            loginfo("hung thr,0x%x,0x%x\n"%(self.mem.rdm(0x60033c1c, 11, 0), self.mem.rdm(0x60033c20, 11, 0)))
        # 3 : RX DET
        if(wr_en==1):
            self.mem.wrm(0x6001cc08, 13,  7, 0x1a) # org :  0x26
            self.mem.wrm(0x6001cc08,  6,  0, 0x20) # org :  0x30
            self.mem.wrm(0x6001ccc8, 13,  7, 0x24) # org :  0x36
            self.mem.wrm(0x6001ccc8,  6,  0, 0x24) # org :  0x36
            self.mem.wrm(0x6001ccdc, 13,  7, 0x10) # org :  0x16
            self.mem.wrm(0x6001ccdc,  6,  0, 0x28) # org :  0x3c
            self.mem.wrm(0x6001c044, 24, 16, 507)  # org :  0x511

            self.mem.wrm(0x6001c024, 17,  9, 0x1b4) # org :  0x1ae
            self.mem.wrm(0x6001c094,  0,  0, 0x1)  # org :  0x0
            self.mem.wrm(0x6001c094, 27, 25, 0x0)  # org :  0x5
        else:
            loginfo("RX det,0x%x,0x%x,0x%x,0x%x,0x%x,0x%x,0x%x,0x%x,0x%x,0x%x\n"%(self.mem.rdm(0x6001cc08, 13, 7), self.mem.rdm(0x6001cc08,  6, 0),self.mem.rdm(0x6001ccc8, 13, 7),self.mem.rdm(0x6001ccc8,  6, 0),\
            self.mem.rdm(0x6001ccdc, 13, 7), self.mem.rdm(0x6001ccdc,  6, 0),self.mem.rdm(0x6001c044, 24,16),self.mem.rdm(0x6001c024, 17,  9),self.mem.rdm(0x6001c094,  0,  0),\
            self.mem.rdm(0x6001c094, 27, 25)))
        # 4 : RSSI
        if(wr_en==1):
            self.mem.wrm(0x6001c088,  7,  0, 0x5) # org : 0x5
            self.mem.wrm(0x6001c0a0, 31, 24, 0x0) # org : 0xfe
            self.mem.wrm(0x6001c02c,  7,  0, 0x0) # org : 0xfe
            self.mem.wrm(0x6001c104, 15, 15, 0x0) # org : 0
            self.mem.wrm(0x6001c038, 27, 27, 0x0) # org : 0
        else:
            loginfo("RSSI,0x%x,0x%x,0x%x,0x%x,0x%x\n"%(self.mem.rdm(0x6001c088,  7,  0), self.mem.rdm(0x6001c0a0, 31, 24),self.mem.rdm(0x6001c02c,  7,  0),self.mem.rdm(0x6001c104, 15, 15),\
            self.mem.rdm(0x6001c038, 27, 27)))
        # 5 : RX ACK

        if(wr_en==1):
            self.mem.wrm(0x60006050,  7,  0, 0xff) # org : 0x04
            self.mem.wrm(0x60033114, 31, 31,  0x1) # org : 0x00
            self.mem.wrm(0x60033114, 27, 20, 0x20) # org : 0x0e
        else:
            loginfo("ACK,0x%x,0x%x,0x%x\n"%(self.mem.rdm(0x60006050,  7,  0), self.mem.rdm(0x60033114, 31, 31),self.mem.rdm(0x60033114, 27, 20)))


    def phy_init_stable_check(self, name_str=''):
        result = self.wifiapi.init_print()
        [data_result, title] = data_summary.get_init_print_data(result)
        fname = self.wifi.get_filename('phy_init_stable_check_%s'%name_str, 'phy_init_stable_check_%s'%name_str)
        csvreport1=csvreport(fname, title)

        for i in range(100):
            self.wifiapi.phyinit()
            result = self.wifiapi.init_print()
            [data_result, title] = data_summary.get_init_print_data(result)
            csvreport1.write_data(data_result)


