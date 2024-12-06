from baselib.loglib.log_lib import *
import os, sys
import socket
import pandas as pd
from math import *
import pylink
from pygdbmi.gdbcontroller import GdbController
class MEM_GDB(object):
    def __init__(self):
        self.open()
        self.open_c()

    def open(self):
        self.gdbmin_mem = GdbController(r'E:\project_audio\expanse\tx232_driver_src\toolchains\nds32le-elf-mculib-v5\bin\riscv32-elf-gdb', ['riscv32.elf'])

    def open_c(self):
        self.gdbmin_mem_c = GdbController(r'E:\project_audio\expanse\tx232_driver_src\toolchains\nds32le-elf-mculib-v5\bin\riscv32-elf-gdb', ['riscv32.elf'])

    def close(self):
        self.gdbmin_mem.exit()
    def close_c(self):
        self.gdbmin_mem_c.exit()

    def rd(self, addr):
        # self.close()
        # self.open()
        for i in range(10):
            result = self.gdbmin_mem.write("x/x 0x%x"%(addr),timeout_sec=0.1,read_response=True)
            logdebug(result)
            result = result[len(result)-1]['payload'].split('\t')[1]
            # logdebug(result)
            if len(result) > 0:
                break
            else:
                logerror('no response,please check gdb connect')
                raise
        return result

    def rdm(self, addr=0xa04210a0, msb=1, lsb=0):
        result = self.rd(addr=addr)
        mask = (1<<(msb+1)) - (1<<lsb);
        try:
            result = (eval(result) & mask) >> lsb;
            # logdebug("resm:" + "0x%x"%result)
        except:
            logerror("mem reads " + "%s"%result)
        return result

    def wr(self, addr=0xa04210a0, value=0x18c619):
        self.close_c()
        self.open_c()
        self.gdbmin_mem.write('set *(unsigned int *) {}={}'.format(addr,value),timeout_sec=0.1,read_response=False)
        self.gdbmin_mem_c.write('c', timeout_sec=2, read_response=False)
        res = self.rd(addr)

        if eval(res) != value:
            logerror('gdb write reg fail')
            raise
        else:
            return res

    def wrm(self, addr, msb, lsb, value, lsb_dis=0):
        result = self.rd(addr=addr)
        mask = (1<<(msb+1)) - (1<<lsb);
        try:
            if lsb_dis !=0:
                result = (eval(result) & ~mask) | ((value << lsb) & mask) | (((1<<(msb+1-lsb))-1)<<(lsb+16))
            else:
                result = (eval(result) & ~mask) | ((value << lsb) & mask)
            # logdebug('{}'.format(result))
            res = self.wr(addr,result)
            logdebug(res)
            return self.rdm(addr, msb, lsb)
        except:
            logerror("mem write fail, reads  %s"%result)
            return

class MEM_TS(object):
    """docstring for common"""
    def __init__(self, channel):
        self.channel = channel



    def rd(self, reg_addr):
        for i in range(10):
            result = self.channel.req_com("rl 0x%x"%(reg_addr), wr_end='\r\n')
            if result.find('value:') != -1:
            #logdebug("res:" + result)
                result = result.split('value:')[1]
                break
            elif i == 9:
                logwarn('rd fail,result:{} ,try agian {}'.format(result,i))
        try:
            result_int = int(result, 16)
            return result_int
        except:
            return result

    def wr(self, reg_addr, value):
        for i in range(10):
            result = self.channel.req_com("wl 0x%x 0x%x"%(reg_addr, value), wr_end='\r\n')
            if result.find('value:') != -1:
            # logdebug("res:" + result)
                result = result.split('value:')[1]
                break
            elif result.find('val:') != -1:
                result = result.split('val:')[1]
                break
            elif i == 9:
                logwarn('wr fail,result:{} ,try agian {}'.format(result,i))
        try:
            result_int = int(result, 16)
            return result_int
        except:
            return result

    def rdm(self, reg_addr, msb, lsb):
        result = self.rd(reg_addr);
        mask = (1<<(msb+1)) - (1<<lsb);
        try:
            result = (result & mask) >> lsb;
            # logdebug("resm:" + "0x%x"%result)
        except:
            logerror("mem reads " + "%s"%result)
        return result

    def wrm(self, reg_addr,msb,lsb,value):
        result = self.rd(reg_addr);
        mask = (1<<(msb+1)) - (1<<lsb);
        try:
            result = (result & ~mask) | ((value << lsb) & mask);
            return self.wr(reg_addr,result);
        except:
            logerror("mem write fail, reads  %s"%result)
            return

    def rfrd(self, reg_addr):
        for i in range(10):
            result = self.channel.req_com("rfrl 0x%x"%(reg_addr), wr_end='\r\n')
            if result.find('value:') != -1:
            #logdebug("res:" + result)
                result = result.split('value:')[1]
                break
            elif i == 9:
                logwarn('rd fail,result:{} ,try agian {}'.format(result,i))
        time.sleep(0.5)
        try:
            result_int = int(result, 16)
            return result_int
        except:
            return result


    def rfwr(self, reg_addr, value):
        for i in range(10):
            result = self.channel.req_com("rfwl 0x%x 0x%x"%(reg_addr, value), wr_end='\r\n')
            if result.find('value:') != -1:
            # logdebug("res:" + result)
                result = result.split('value:')[1]
                break
            elif i == 9:
                logwarn('wr fail,result:{} ,try agian {}'.format(result,i))
        time.sleep(0.5)
        try:
            result_int = int(result, 16)
            return result_int
        except:
            return result


    def rfrdm(self, reg_addr, msb, lsb):
        result = self.rfrd(reg_addr);
        mask = (1<<(msb+1)) - (1<<lsb);
        try:
            result = (result & mask) >> lsb;
            # logdebug("resm:" + "0x%x"%result)
        except:
            logerror("mem reads " + "%s"%result)
        return result

    def rfwrm(self, reg_addr,msb,lsb,value):
        result = self.rfrd(reg_addr);
        mask = (1<<(msb+1)) - (1<<lsb);
        try:
            result = (result & ~mask) | ((value << lsb) & mask);
            return self.rfwr(reg_addr,result);
        except:
            logerror("mem write fail, reads  %s"%result)
            return

class jlink(object):
    def __init__(self, jlink_sn="59610042"):
        self.jlink = pylink.JLink()
        self.jlink_sn = jlink_sn
        if self.jlink.opened() == False:
            self.jlink.open(self.jlink_sn)
        self.jlink.set_tif(pylink.enums.JLinkInterfaces.SWD)
        self.jlink.connect('ARMCM4_FP')
    def close(self):
        self.jlink.close()

    def jlink_connect(self):
        if self.jlink.opened() == False:
            self.jlink.open(self.jlink_sn)
        self.jlink.set_tif(pylink.enums.JLinkInterfaces.SWD)
        self.jlink.connect('ARMCM4_FP')

    def rd(self, addr=0xa04210a0):
        res = self.jlink.memory_read(addr,4)
        logdebug('{}'.format(res))
        res_int = 0x1000000*res[3] + 0x10000*res[2] + 0x100*res[1] + res[0]
        res = '0x%x'%(res_int)
        loginfo('addr:  {}  value:  {}'.format(hex(addr), res))
        return res

    def rdm(self, addr=0xa04210a0, msb=1, lsb=0):
        result = self.rd(addr=addr)
        mask = (1<<(msb+1)) - (1<<lsb);
        try:
            result = (eval(result) & mask) >> lsb;
            # logdebug("resm:" + "0x%x"%result)
        except:
            logerror("mem reads " + "%s"%result)
        return result

    def wr(self, addr=0xa04210a0, value=0x18c619):

        value_list = [value&0xff,(value&0xff00)>>8,(value&0xff0000)>>16,(value&0xff000000)>>24]
        loginfo('{}'.format(value_list))
        self.jlink.memory_write(addr,value_list)
        res = self.rd(addr)

    def wrm(self, addr, msb, lsb, value, lsb_dis=0):
        result = self.rd(addr=addr)
        mask = (1<<(msb+1)) - (1<<lsb);
        try:
            if lsb_dis !=0:
                result = (eval(result) & ~mask) | ((value << lsb) & mask) | (((1<<(msb+1-lsb))-1)<<(lsb+16))
            else:
                result = (eval(result) & ~mask) | ((value << lsb) & mask)
            logdebug('{}'.format(result))
            return self.wr(addr,result);
        except:
            logerror("mem write fail, reads  %s"%result)
            return

class MEM(object):
    """docstring for common"""
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel

    def rd(self, reg_addr):
        result = self.channel.req_com("rd 0x%x"%(reg_addr))
        #logdebug("res:" + result)
        try:
            result_int = int(result, 16)
            return result_int
        except:
            return result

    def wr(self, reg_addr, value):
        result = self.channel.req_com("wr 0x%x 0x%x"%(reg_addr, value))
        # logdebug("res:" + result)
        try:
            result_int = int(result, 16)
            return result_int
        except:
            return result

    def rdm(self, reg_addr, msb, lsb):
        result = self.rd(reg_addr);
        mask = (1<<(msb+1)) - (1<<lsb);
        try:
            result = (result & mask) >> lsb;
            # logdebug("resm:" + "0x%x"%result)
        except:
            logerror("mem reads " + "%s"%result)
        return result;

    def rdmem(self,mem_addr,data_len):
        rm_hdr_len=(mem_addr&0x3);
        mem_addr_align=mem_addr-rm_hdr_len;
        align_data_len=data_len+rm_hdr_len;
        data_len=4*int(ceil(align_data_len*1.0/4));
        burst_len=32;
        burst_startaddr = mem_addr_align;
        burst_len_lst=[];
        burst_startaddr_lst=[]
        times=int(ceil(data_len*1.0/burst_len));
        while times>1:
            burst_len_lst.append(burst_len);
            burst_startaddr_lst.append(burst_startaddr);
            burst_startaddr = burst_startaddr+burst_len
            times=times-1;
            data_len=data_len-burst_len;
        burst_len_lst.append(data_len);
        burst_startaddr_lst.append(burst_startaddr);
        result_str='';
        cnt=0
        for datalen in burst_len_lst:
            rpt=1;
            while rpt==1:
               result=self.channel.req_com("RdMem 0x%x %d"%(burst_startaddr_lst[cnt],datalen));
               rs_lst=result.split();
               try:
                 rs_data=[int(i,16) for i in rs_lst];
                 if len(rs_data)!=int(ceil(datalen*1.0/4)):
                    rpt=1;
                 else:
                    rpt=0;
               except:
                 rpt=1;

            result_str=result_str+' '+result;
            cnt=cnt+1
        res_word = [int(i,16) for i in result_str.split()];
        res = [];
##        return result_str
        return str.split(result_str)
##        for i in range(0,align_data_len):
##           res.append(((res_word[i/4])>>(i%4*8))&0xff);
##        return res[rm_hdr_len:];

    def wrm(self, reg_addr,msb,lsb,value):
        result = self.rd(reg_addr);
        mask = (1<<(msb+1)) - (1<<lsb);
        try:
            result = (result & ~mask) | ((value << lsb) & mask);
            return self.wr(reg_addr,result);
        except:
            logerror("mem write fail, reads  %s"%result)
            return

    def accumiq(self,mem_addr,burst_len):
        result=self.channel.req_com("accumiq 0x%x %d"%(mem_addr,burst_len));
        return result

    def setmask(self, reg_addr, mask):
        return self.wr(reg_addr, self.rd(reg_addr) | mask)

    def clrmask(self, reg_addr, mask):
        return self.wr(reg_addr, self.rd(reg_addr) & (~mask))





