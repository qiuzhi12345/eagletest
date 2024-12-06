import os, sys
import pandas as pd
import numpy as np
from baselib.loglib.log_lib import *

REGF_PATH = "./hal/hwregister/hwreg/"
I2CF_PATH = "./hal/hwregister/hwi2c/"
RFTEST_PATH = "./rftest/rflib/"

class csv2py(object):
    """docstring for csv2py"""
    def __init__(self, fname, database, outpath, chipv="ESP32"):
        '''
        outpath: python path
        fname:    csv file name
        '''
        super(csv2py, self).__init__()
        self.chipv = chipv
        self.path = outpath
        self.df = database
        self.fname = fname
        self.type = "reg"
    def reg2pyinit(self):
        self.stripspace()
        self.addr_base_name = self.fname + "_BASE"
        self.addr_host_name = self.fname + "_HOSTID"
        self.pyfid = open(self.path + self.fname+".py", 'w')
        self.mainimp = ""
        self.mainclass = ""
        self.subregclasshead = ""
        self.subregclass = ""
        self.regclass = ""

    def stripspace(self):
        new_col = []
        for i in self.df.columns:
            new_col.append(i.strip(" "))
        self.df.columns = new_col

    def i2c_gen_base(self):
        fid = open(self.path + "addr_base.py", 'w')
        for index in self.df.index:
            base_name = self.df.loc[index]["#macro"]
            base_addr = self.df.loc[index]["addr"]
            base_hostid = self.df.loc[index]["host"]
            fid.write(str.upper(base_name.encode('utf-8'))+"_BASE" + " = " + base_addr + "\n")
            fid.write(str.upper(base_name.encode('utf-8'))+"_HOSTID" + " = " + "0x%x"%base_hostid + "\n")

        fid.close()
    def i2c2py(self):
        self.type = "i2c"
        self.AddImport()
        self.AddRegHead(self.fname)
        for index in self.df.index:
            if not self.df.loc[index].isnull()["ctrl_name"]:
                addr = "0x%x"%(self.df.loc[index]["#addr"])
                reg_name = self.df.loc[index]["ctrl_name"].split("[")[0]
                msb = self.df.loc[index]["msb"]
                lsb = self.df.loc[index]["lsb"]
                self.AddRegMLsb(reg_name, lsb, msb, addr)
                self.Reg2Class(reg_name)
                # self.regclass = self.regclass + self.subregclasshead + self.subregclass
        self.regclass = self.regclass + self.subregclasshead + self.subregclass
        self.write_out()

    def reggenpy(self):
        self.type = "reg"
        self.AddImport()
        self.AddMainClassHead()
        for index in self.df.index:
            if not self.df.loc[index].isnull()["RegName"]:
                if self.fname[:4] == "RTC_" and self.chipv in ["ESP32", "CHIP72"] :
                    addr = "0x%x"%(int(self.df.loc[index]["Address"].strip(" "), 16) * 4)
                else:
                    addr = "0x%x"%(int(self.df.loc[index]["Address"].strip(" "), 16))

                reg_name = self.df.loc[index]["RegName"].strip(" ")
                if reg_name != "":
                    self.regclass = self.regclass + self.subregclasshead + self.subregclass
                    self.subregclasshead = ""
                    self.subregclass = ""
                    self.AddMainReg(reg_name)
                    self.AddRegHead(reg_name, addr)
                    self.RRegClass()
            if not self.df.loc[index].isnull()["Signal"]:
                signal_name = self.df.loc[index]["Signal"].strip(" ")
                default_value = ""
                if signal_name[-4:] == "date":
                    default_value = "0x" + self.df.loc[index]["Default"].split("h")[1]
                if signal_name != "":
                    bits = self.df.loc[index]["BitPos"].strip(" ")[1:-1]
                    bits = bits.split(":")
                    if len(bits) == 1:
                        lsb = bits[0]
                        msb = bits[0]
                    elif len(bits) == 2:
                        lsb = bits[1]
                        msb = bits[0]
                    self.AddRegMLsb(signal_name, lsb, msb)
                    self.Reg2Class(signal_name, default_value)
        self.regclass = self.regclass + self.subregclasshead + self.subregclass
        self.write_out()

    def AddImport(self):
        self.mainimp = self.mainimp + ("from hal.common import *\n")
        self.mainimp = self.mainimp + ("from hal.hwregister.hw%s.%s.addr_base import *\n"%(self.type, self.chipv))

    def AddMainClassHead(self):
        logdebug("AddMainClassHead %s"%(self.fname))
        self.mainclass = self.mainclass + ("class %s(object):\n"%self.fname)
        self.mainclass = self.mainclass + ("    def __init__(self, channel, chipv = \"%s\"):\n"%(self.chipv))
        self.mainclass = self.mainclass + ("        self.chipv = chipv\n")
        self.mainclass = self.mainclass + ("        self.channel = channel\n")

    def AddMainReg(self, reg_name):
        self.mainclass = self.mainclass + ("        self.%s = %s(self.channel, self.chipv)\n"%(reg_name, reg_name))


    def AddRegHead(self, reg_name, addr = ""):
        logdebug("AddRegHead %s"%(reg_name))
        self.subregclasshead = self.subregclasshead + ("class %s(object):\n"%reg_name)
        self.subregclasshead = self.subregclasshead + ("    def __init__(self, channel, chipv = \"%s\"):\n"%(self.chipv))
        self.subregclasshead = self.subregclasshead + ("        self.chipv = chipv\n")
        self.subregclasshead = self.subregclasshead + ("        self.channel = channel\n")
        if self.type == "reg":
            self.subregclasshead = self.subregclasshead + ("        self.__MEM = MEM(self.channel, self.chipv)\n")
            self.subregclasshead = self.subregclasshead + ("        self.__addr = %s + %s\n"%(self.addr_base_name, addr))
        else:
            self.subregclasshead = self.subregclasshead + ("        self.__I2C = I2C(self.channel, self.chipv)\n")
            self.subregclasshead = self.subregclasshead + ("        self.__base = %s\n"%(self.addr_base_name))
            self.subregclasshead = self.subregclasshead + ("        self.__hostid = %s\n"%(self.addr_host_name))
        if not(self.type == "reg"):
            self.subregclass = self.subregclass + ("\n")
            self.subregclass = self.subregclass + ("    def reg_addr_rd(self,reg_addr):\n")
            self.subregclass = self.subregclass + ("        return self.__I2C.i2c_rd(self.__base , self.__hostid ,reg_addr)\n")
            self.subregclass = self.subregclass + ("    def reg_addr_wr(self,reg_addr,value):\n")
            self.subregclass = self.subregclass + ("        return self.__I2C.i2c_wr(self.__base , self.__hostid ,reg_addr,value)\n")
    def AddRegMLsb(self, signal_name, lsb, msb, addr = ""):
        self.subregclasshead = self.subregclasshead + ("        self.__%s_lsb = %s\n"%(signal_name, lsb))
        self.subregclasshead = self.subregclasshead + ("        self.__%s_msb = %s\n"%(signal_name, msb))
        if self.type == "i2c":
             self.subregclasshead = self.subregclasshead + ("        self.__%s_addr = %s\n"%(signal_name, addr))
    def Reg2Class(self, signal_name, default_value = ""):
        self.subregclass = self.subregclass + ("\n")
        self.subregclass = self.subregclass + ("    @property\n")
        self.subregclass = self.subregclass + ("    def %s(self):\n"%signal_name)
        if self.type == "reg":
            self.subregclass = self.subregclass + ("        return self.__MEM.rdm(self.__addr, self.__%s_msb, self.__%s_lsb)\n"%(signal_name, signal_name))
        else:
            self.subregclass = self.subregclass + ("        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__%s_addr, self.__%s_msb, self.__%s_lsb)\n"%(signal_name, signal_name, signal_name))
        self.subregclass = self.subregclass + ("    @%s.setter\n"%signal_name)
        self.subregclass = self.subregclass + ("    def %s(self, value):\n"%signal_name)
        if self.type == "reg":
            self.subregclass = self.subregclass + ("        return self.__MEM.wrm(self.__addr, self.__%s_msb, self.__%s_lsb, value)\n"%(signal_name, signal_name))
        else:
            self.subregclass = self.subregclass + ("        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__%s_addr, self.__%s_msb, self.__%s_lsb, value)\n"%(signal_name, signal_name, signal_name))

        if signal_name[-4:] == "date":
            self.subregclass = self.subregclass + ("    @property\n")
            self.subregclass = self.subregclass + ("    def default_value(self):\n")
            self.subregclass = self.subregclass + ("        return %s\n"%(default_value))

    def RRegClass(self):
        self.subregclass = self.subregclass + ("    @property\n")
        self.subregclass = self.subregclass + ("    def reg(self):\n")
        self.subregclass = self.subregclass + ("        return self.__MEM.rdm(self.__addr, 31, 0)\n")
        self.subregclass = self.subregclass + ("    @reg.setter\n")
        self.subregclass = self.subregclass + ("    def reg(self, value):\n")
        self.subregclass = self.subregclass + ("        return self.__MEM.wrm(self.__addr, 31, 0, value)\n")

    def write_out(self):
        self.pyfid.write(self.mainimp)
        self.pyfid.write(self.mainclass)
        self.pyfid.write(self.regclass)

    def deinit(self):
        self.pyfid.close()


def i2c2pyclass():
    all_fid1_str = ""
    all_fid2_str = ""
    all_fid3_str = ""
    all_fid1_str = all_fid1_str + "class HWI2C(object):\n"
    all_fid1_str = all_fid1_str + "    def __init__(self, channel, chipv = \"ESP32\"):\n"
    all_fid1_str = all_fid1_str + "        self.chipv = chipv\n"
    all_fid1_str = all_fid1_str + "        self.channel = channel\n"
    for chip in os.listdir(I2CF_PATH):
        if chip == "ESP8266":
            i2c_list = ["addr_base", "BIAS", "BBPLL", "RFTX", "RFRX","BBTX","BBRX", 'SARADC', 'CKGEN', 'XTAL', 'RFPLL','RFPLL_SDM', 'DIG_FE','DIG_INF' ]
        elif chip == "CHIP722":
            i2c_list = ["addr_base", "BIAS", "BBPLL", "RFTX", "RFRX", 'BBTOP',  'CKGEN', 'XTAL', 'RFPLL', 'RFPLL_SDM',  'APLL', 'ULP','BIAS_MARLIN3']
        elif chip == "CHIP723" or chip=="CHIP724":
            i2c_list = ["addr_base", "BIAS", "BBPLL", "RFTX", "RFRX", 'BBTOP',  'CKGEN',  'RFPLL', 'RFPLL_SDM',  'APLL', 'ULP','SAR']
        else:
            i2c_list = ["addr_base", "BIAS", "BBPLL", "RFTX", "RFRX", 'BBTOP', 'SARADC', 'CKGEN', 'XTAL', 'RFPLL', 'RFPLL_SDM', 'DIG_FE', "DIG_ANA", "DIG_TEST", 'APLL']
        if not os.path.isdir(I2CF_PATH + chip):
            continue
        loginfo("find CHIP:%s"%chip)
        # gen base
        chip_I2CF_PATH = I2CF_PATH + chip + "/"
        df = pd.read_excel(chip_I2CF_PATH+"csv/i2c_table.xlsm", sheetname="i2c_host")
        a = csv2py("", df, chip_I2CF_PATH)
        a.i2c_gen_base()
        # init.py
        fid = open(chip_I2CF_PATH+"__init__.py", 'w')
        fid.write("__all__ = %s"%(str(i2c_list)))
        i2c_list.remove("addr_base")
        loginfo(i2c_list)
        fid.close()
        # gen pyclass
        for i in i2c_list:
            loginfo(i)
            df = pd.read_excel(chip_I2CF_PATH+"csv/i2c_table.xlsm", sheetname=str.lower(i))
            i = str.upper(i.encode('utf-8'))
            a = csv2py(i, df, chip_I2CF_PATH,chip)
            a.reg2pyinit()
            a.i2c2py()
            a.deinit()

        all_fid3_str = all_fid3_str + "        if self.chipv == \"%s\":\n"%(chip)
        all_fid3_str = all_fid3_str + "            from hal.hwregister.hwi2c.%s import *\n"%(chip)
        for i in i2c_list:
            all_fid3_str = all_fid3_str + "            self.%s = %s.%s(channel, chipv)\n"%(str.lower(i),i,i)

    all_fid1 = open(I2CF_PATH+"all.py", 'w')
    all_fid1.write(all_fid2_str + all_fid1_str + all_fid3_str)
    all_fid1.close()

def reg2pyclass(chip_list = []):
    #REGF_PATH = "/home/lab/chip/eagletest/py_script/hal/hwregister/hwreg/"
    all_fid1_str = ""
    all_fid2_str = ""
    all_fid3_str = ""
    all_fid1_str = all_fid1_str + "class HWREG(object):\n"
    all_fid1_str = all_fid1_str + "    def __init__(self, channel, chipv = \"ESP32\"):\n"
    all_fid1_str = all_fid1_str + "        self.chipv = chipv\n"
    all_fid1_str = all_fid1_str + "        self.channel = channel\n"

    if chip_list == []:
        chip_list = os.listdir(REGF_PATH)

    for chip in chip_list:
        if not os.path.exists(REGF_PATH + chip):
            continue
        if not os.path.isdir(REGF_PATH + chip):
            continue

        loginfo("find CHIP:%s"%chip)
        chip_REGF_PATH = REGF_PATH + chip + "/"

        fid = open(chip_REGF_PATH+"__init__.py", 'w')
        init_list = ["addr_base"]
        for file in os.listdir(chip_REGF_PATH + "csv/"):
            if file[-4:] == ".csv":
                loginfo(chip_REGF_PATH+"csv/"+file)
                fname = str.upper(file[0:-4]).replace("_REG","")
                df = pd.read_csv(chip_REGF_PATH+"csv/"+file, sep=';')
                a = csv2py(fname, df, chip_REGF_PATH, chip)
                a.reg2pyinit()
                a.reggenpy()
                a.deinit()
                init_list.append(str.upper(fname))
        fid.write("__all__ = %s"%(str(init_list)))
        fid.close()
##        all_fid2_str = all_fid1_str + "if self.chipv == \"%s\\n":"%(chip)
##        all_fid2_str = all_fid1_str + "    from hal.hwregister.hwreg.%s import *\n"%(chip)

        all_fid3_str = all_fid3_str + "        if self.chipv == \"%s\":\n"%(chip)
        all_fid3_str = all_fid3_str + "            from hal.hwregister.hwreg.%s import *\n"%(chip)
        init_list.remove(init_list[0])
        for i in init_list:
            all_fid3_str = all_fid3_str + "            self.%s = %s.%s(channel, chipv)\n"%(i,i,i)


    all_fid1 = open(REGF_PATH+"all.py", 'w')
    all_fid1.write(all_fid2_str + all_fid1_str + all_fid3_str)
    all_fid1.close()


def rftestpyclass(fname='./rftest/rflib/rfpll.py'):
    import re
    all_fid1_str = ""
    all_fid1_str = all_fid1_str + "from baselib.test_channel.com import COM as com\n"
    all_fid1_str = all_fid1_str + "from baselib.loglib.log_lib import *\n"
    all_fid1_str = all_fid1_str + "from hal.Init import HALS\n"
    all_fid1_str = all_fid1_str + "from hal.common import *\n"
    all_fid1_str = all_fid1_str + "import random\n" + "import time\n" + "import numpy as np\n" + "from rftest.rflib import rfglobal\n" + "from rftest.rflib.pbus import pbus\n"
    all_fid1_str = all_fid1_str + "class rfpll(object):\n" + "    def __init__(self,channel,chipv='ESP32'):\n" + "        self.channel = channel\n" + "        self.chipv = chipv\n"
    all_fid1_str = all_fid1_str + "        self.HALS = HALS(self.channel,self.chipv)\n" + "        self.pbus = pbus(self.channel,self.chipv)\n"
    loginfo(all_fid1_str)
    with open(fname,'rt') as f:
        all_fid2_str = ""
        line_new=""
        for line in f:
            loginfo(line)
            line=line.replace("chan_id='com'","")
            line=line.replace("'com'","")
            line=line.replace(", )",")")
            line=line.replace("chan_id","")
            line=line.replace("mem.","self._MEM.")
            line=line.replace(", ,",",")
            index1=line.find('i2c.')
            loginfo(index1)
            if index1==-1:
                if line.startswith('def') and line.endswith('):\n'):
                    line=line.replace("(","(self,")
                    line=line.replace(",)",")")
##                if index2==-1:
##
##                    all_fid2_str = all_fid2_str + '    '+line
##
                else:
                    line=line.replace("pbus.","self.pbus.")
                    line=line.replace("pbus_","self.pbus.pbus_")
                    line=line.replace("pbus.pbus(","pbus.pbus_wr(")
                    line=line.replace("wifi.","self.wifi.")
                    line=line.replace("rfpll.","self.rfpll.")
                    line=line.replace("agc_test.","self.adcdump.")
                all_fid2_str = all_fid2_str + '    '+line

            else:
                line_list_op=line.split('i2c.',1)[1].split('(',1)[0]
                line_list_op_1=line.split('i2c.',1)[1].split('(',1)[1].split(',',1)[0]
                if type(eval(line_list_op_1))==type(''):
                    line_list=line.replace("i2c.","self.HALS.HWI2C.stest.")
                    #line_list=line.split('i2c.',1)[0]+'self.HALS.HWI2C.stest.'
                    line_list_re0=line_list.split('stest.',1)
                    line_list_re1=re.split(r'[(,)]',line_list_re0[1])
                    print line_list
                    print len(line_list_re0)
                    print line_list_re0
                    print line_list_re1
                    if line_list_op=="ri":
                        line_new=line_list_re0[0]+eval(str.upper(line_list_re1[1]))+"."+"reg_addr_rd(%s)"%line_list_re1[2]+line_list_re0[1].split(")",1)[1]+"\n"
                    elif line_list_op=="wi":
                        line_new=line_list_re0[0]+eval(str.upper(line_list_re1[1]))+"."+"reg_addr_wr(%s"%line_list_re1[2]+line_list_re0[1].split(",",2)[2]+"\n"

                    elif line_list_op=="ric":
                        line_new=line_list_re0[0]+eval(str.upper(line_list_re1[1]))+"."+eval(line_list_re1[2])+line_list_re0[1].split(")",1)[1]+"\n"

                    elif line_list_op=="wic":
                        line_new=line_list_re0[0]+eval(str.upper(line_list_re1[1]))+"."+eval(line_list_re1[2])+"=%s"%line_list_re1[3]+line_list_re0[1].split(")",1)[1]+"\n"
                else:
                    line_new=line.replace("i2c.ri","self.HALS.i2c.rd")
                    line_new=line_new.replace("i2c.wi","self.HALS.i2c.wr")

                all_fid2_str = all_fid2_str + '    '+line_new

    str_all=all_fid1_str + all_fid2_str
    pyfid = open(os.path.split(fname)[0] + "/temp"+str.upper(os.path.split(fname)[1].encode("utf-8")), 'w')
    loginfo(pyfid)
    pyfid.write(str_all)
    pyfid.close()


def rflibpyclass(bfname=[""],afname=[""],fname='./rftest/rflib/tc006_pbus_test.py'):
    with open(fname,'rt') as f:
        all_fid2_str = ""
        line_new=""
        for line in f:
            loginfo(line)
            spaces=0
            for i in range(len(line)):
                spaces=i
                if line[i]!=' ':
                    break
            line=line[spaces:]
            print line
            for j in range(1,20):
                print j
                if 4*j<spaces<4*(j+1):
                    spaces=4*(j+1)
                    break
            line=' '*spaces + line
            print line
            for k in range(len(bfname)):
                line=line.replace(bfname[k],afname[k])
                all_fid2_str = all_fid2_str +line
    pyfid = open(os.path.split(fname)[0] + "/"+os.path.split(fname)[1].encode("utf-8"), 'w')
    loginfo(pyfid)
    pyfid.write(all_fid2_str)
    pyfid.close()
