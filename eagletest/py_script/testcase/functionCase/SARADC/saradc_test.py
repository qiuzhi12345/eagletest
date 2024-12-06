# -- coding: utf-8 --
from baselib.test_channel.com import COM as com
from baselib.loglib.log_lib import *
from hal.Init import HALS
from rtclib.rtc import ULP_PARAM
from rtclib.rtc import WAKEUP_ENABLE
from rtclib.rtc import WAKEUP_REASON
from baselib.instrument.awg import awg
import random

class SARADC_TC_FUNC(object):
    def __init__(self, channel, chipv = "AUTO"):
        self.chip = HALS(channel, chipv)
        self.chipv = self.chip.chipv

    def tc000_rtc_adc1_low_test(self):
        '''all adc1 channel in adc1_channel_list should connect to low(GND)'''
        if self.chipv == "ESP32":
            adc1_channel_list = [0, 1, 2, 6, 7]
        else:
            adc1_channel_list = range(10)
        fail_num = 0
        self.chip.rtc_adc1.config()
        for adc1_channel in adc1_channel_list:
            self.chip.rtc_adc1.set(pad = adc1_channel)
            read_value = int(self.chip.rtc_adc1.read())
            if (0 != read_value):
                fail_num += 1
                logerror("fail when adc1_channel: %d, read_value: 0x%x\n"%(adc1_channel, read_value))
        if (0 != fail_num):
            logerror("fail_num: %d"%(fail_num))
            return logfail()
        else:
            return logpass()

    def tc001_rtc_adc1_high_test(self):
        '''all adc1 channel in adc1_channel_list should connect to high(3.3v)'''
        if self.chipv == "ESP32":
            adc1_channel_list = [0, 1, 2, 6, 7]
        else:
            adc1_channel_list = range(10)
        fail_num = 0
        self.chip.rtc_adc1.config()
        for adc1_channel in adc1_channel_list:
            self.chip.rtc_adc1.set(pad = adc1_channel)
            read_value = int(self.chip.rtc_adc1.read(0))
            if self.chipv == "ESP8266" or self.chipv == "ESP32" or self.chipv == "CHIP722":
                if (0xfff != read_value):
                    fail_num += 1
                    logerror("fail when adc1_channel: %d, read_value: 0x%x\n"%(adc1_channel, read_value))
            else:
                if (0x1fff != read_value):
                    fail_num += 1
                    logerror("fail when adc1_channel: %d, read_value: 0x%x\n"%(adc1_channel, read_value))
        if (0 != fail_num):
            logerror("fail_num: %d"%(fail_num))
            return logfail()
        else:
            return logpass()
            
    def tc002_rtc_adc2_low_test(self):
        '''all adc2 channel in adc2_channel_list should connect to low(GND)'''
        if self.chipv == "ESP32":
            adc2_channel_list = [0, 6, 7, 8, 9]
        else:
            adc2_channel_list = range(10)
        fail_num = 0
        self.chip.rtc_adc2.config()
        for adc2_channel in adc2_channel_list:
            self.chip.rtc_adc2.set(pad = adc2_channel)
            read_value = int(self.chip.rtc_adc2.read())
            if (0 != read_value):
                fail_num += 1
                logerror("fail when adc2_channel: %d, read_value: 0x%x\n"%(adc2_channel, read_value))
        if (0 != fail_num):
            logerror("fail_num: %d"%(fail_num))
            return logfail()
        else:
            return logpass()

    def tc003_rtc_adc2_high_test(self):
        '''all adc2 channel in adc2_channel_list should connect to 3.3v'''
        if self.chipv == "ESP32":
            adc2_channel_list = [0, 6, 7, 8, 9]
        else:
            adc2_channel_list = range(10)
        fail_num = 0
        self.chip.rtc_adc2.config()
        for adc2_channel in adc2_channel_list:
            self.chip.rtc_adc2.set(pad = adc2_channel)
            read_value = int(self.chip.rtc_adc2.read())
            if self.chipv == "ESP32" or self.chipv == "CHIP722":
                if (0xfff != read_value):
                    fail_num += 1
                    logerror("fail when adc2_channel: %d, read_value: 0x%x\n"%(adc2_channel, read_value))
            else:
                if (0x1ff != read_value):
                    fail_num += 1
                    logerror("fail when adc2_channel: %d, read_value: 0x%x\n"%(adc2_channel, read_value))
        if (0 != fail_num):
            logerror("fail_num: %d"%(fail_num))
            return logfail()
        else:
            return logpass()
     
    def tc004_dig_adc1_low_test(self):
        '''all adc1 channel in adc1_channel_list should connect to low(GND)'''
        if self.chipv == "ESP32":
            adc1_channel_list = [0, 1, 2, 6, 7]
        else:
            adc1_channel_list = range(10)
        fail_num = 0
        chn_num = len(adc1_channel_list)
        full_pattern = 0xffffffff
        table1 = 0xffffffff
        table2 = 0xffffffff
        table3 = 0xffffffff
        pattern1 = 0
        pattern2 = 0
        pattern3 = 0
        if self.chipv == "CHIP722":
            if chn_num > 10:
                logerror("wrong channel_list, the length is overflow: %d"%chn_num)
                return
        else:
            if chn_num > 8:
                logerror("wrong channel_list, the length is overflow: %d"%chn_num)
                return
        for i in range(chn_num):
            if i < 4:
                chan = table1 >> (28 - i * 8) & adc1_channel_list[i]
                table1 = (chan << (28 - i * 8)) | (full_pattern >> (2 * i + 1) * 4) | pattern1
                pattern1 = table1 >> (24 - i * 8)  << (24 - i * 8) 
            elif i < 8:
                j = i - 4
                chan = table2 >> (28 - j * 8) & adc1_channel_list[i]
                table2 = (chan << (28 - j * 8)) | (full_pattern >> (2 * j + 1) * 4) | pattern2
                pattern2 = table2 >> (24 - j * 8)  << (24 - j * 8)
            else:
                j = i - 8
                chan = table3 >> (28 - j * 8) & adc1_channel_list[i]
                table3 = (chan << (28 - j * 8)) | (full_pattern >> (2 * j + 1) * 4) | pattern3
                pattern3 = table2 >> (24 - j * 8)  << (24 - j * 8)
        loginfo("table1: 0x%x"%table1)
        loginfo("table2: 0x%x"%table2)
        loginfo("table3: 0x%x"%table3)
        self.chip.dig_adc.config()
        self.chip.dig_adc.i2s()
        self.chip.dig_adc.set_adc1(sar1_patt_len = chn_num - 1, table1 = table1, table2 = table2, table3 = table3)
        first_mem_addr = int(self.chip.dig_adc.read(), 16)
        for i in range(chn_num):
            mem_addr = first_mem_addr + (i / 2) *4
            value = self.chip.MEM.rd(mem_addr)
            if (0 == i % 2):
                loginfo("mem_addr: 0x%x, value: 0x%x"%(mem_addr, value))
                data = value & 0xfff
            else:
                data = (value >> 16) & 0xfff
            if (0 != data):
                fail_num += 1
                logerror("data is: 0x%x, when i: %d"%(data, i)) 
        if (0 != fail_num):
            logerror("fail_num: %d"%(fail_num))
            return logfail()
        else:
            return logpass()

    def tc005_dig_adc1_high_test(self):
        '''all adc1 channel in adc1_channel_list should connect to high(3.3v)'''
        if self.chipv == "ESP32":
            adc1_channel_list = [0, 1, 2, 6, 7]
        else:
            adc1_channel_list = range(10)
        fail_num = 0
        chn_num = len(adc1_channel_list)
        full_pattern = 0xffffffff
        table1 = 0xffffffff
        table2 = 0xffffffff
        table3 = 0xffffffff
        pattern1 = 0
        pattern2 = 0
        pattern3 = 0
        if self.chipv == "CHIP722":
            if chn_num > 10:
                logerror("wrong channel_list, the length is overflow: %d"%chn_num)
                return
        else:
            if chn_num > 8:
                logerror("wrong channel_list, the length is overflow: %d"%chn_num)
                return
        for i in range(chn_num):
            if i < 4:
                chan = table1 >> (28 - i * 8) & adc1_channel_list[i]
                table1 = (chan << (28 - i * 8)) | (full_pattern >> (2 * i + 1) * 4) | pattern1
                pattern1 = table1 >> (24 - i * 8)  << (24 - i * 8) 
            elif i < 8:
                j = i - 4
                chan = table2 >> (28 - j * 8) & adc1_channel_list[i]
                table2 = (chan << (28 - j * 8)) | (full_pattern >> (2 * j + 1) * 4) | pattern2
                pattern2 = table2 >> (24 - j * 8)  << (24 - j * 8)
            else:
                j = i - 8
                chan = table3 >> (28 - j * 8) & adc1_channel_list[i]
                table3 = (chan << (28 - j * 8)) | (full_pattern >> (2 * j + 1) * 4) | pattern3
                pattern3 = table2 >> (24 - j * 8)  << (24 - j * 8)
        loginfo("table1: 0x%x"%table1)
        loginfo("table2: 0x%x"%table2)
        loginfo("table3: 0x%x"%table3)
        self.chip.dig_adc.config()
        self.chip.dig_adc.i2s()
        self.chip.dig_adc.set_adc1(sar1_patt_len = chn_num - 1, table1 = table1, table2 = table2, table3 = table3)
        first_mem_addr = int(self.chip.dig_adc.read(), 16)
        for i in range(chn_num):
            mem_addr = first_mem_addr + (i / 2) *4
            value = self.chip.MEM.rd(mem_addr)
            if (0 == i % 2):
                loginfo("mem_addr: 0x%x, value: 0x%x"%(mem_addr, value))
                data = value & 0xfff
            else:
                data = (value >> 16) & 0xfff
            if (0xfff != data):
                fail_num += 1
                logerror("data is: 0x%x, when i: %d"%(data, i)) 
        if (0 != fail_num):
            logerror("fail_num: %d"%(fail_num))
            return logfail()
        else:
            return logpass()

    def tc006_dig_adc2_low_test(self):
        '''all adc2 channel in adc2_channel_list should connect to low(GND)'''
        if self.chipv == "ESP32":
            adc2_channel_list = [0, 6, 7, 8, 9]
        else:
            adc2_channel_list = range(10)
        fail_num = 0
        chn_num = len(adc2_channel_list)
        full_pattern = 0xffffffff
        table1 = 0xffffffff
        table2 = 0xffffffff
        table3 = 0xffffffff
        pattern1 = 0
        pattern2 = 0
        pattern3 = 0
        if chn_num > 10:
            logerror("wrong channel_list, the length is overflow: %d"%chn_num)
            return
        for i in range(chn_num):
            if i < 4:
                chan = table1 >> (28 - i * 8) & adc2_channel_list[i]
                table1 = (chan << (28 - i * 8)) | (full_pattern >> (2 * i + 1) * 4) | pattern1
                pattern1 = table1 >> (24 - i * 8)  << (24 - i * 8) 
            elif i < 8:
                j = i - 4
                chan = table2 >> (28 - j * 8) & adc2_channel_list[i]
                table2 = (chan << (28 - j * 8)) | (full_pattern >> (2 * j + 1) * 4) | pattern2
                pattern2 = table2 >> (24 - j * 8)  << (24 - j * 8)
            else:
                j = i - 8
                chan = table3 >> (28 - j * 8) & adc2_channel_list[i]
                table3 = (chan << (28 - j * 8)) | (full_pattern >> (2 * j + 1) * 4) | pattern3
                pattern3 = table3 >> (24 - j * 8)  << (24 - j * 8)
        loginfo("table1: 0x%x"%table1)
        loginfo("table2: 0x%x"%table2)
        loginfo("table3: 0x%x"%table3)
        self.chip.dig_adc.config()
        self.chip.dig_adc.i2s()
        self.chip.dig_adc.set_adc2(sar2_patt_len = chn_num - 1, table1 = table1, table2 = table2, table3 = table3)
        first_mem_addr = int(self.chip.dig_adc.read(), 16)
        for i in range(chn_num):
            mem_addr = first_mem_addr + (i / 2) *4
            value = self.chip.MEM.rd(mem_addr)
            if (0 == i % 2):
                loginfo("mem_addr: 0x%x, value: 0x%x"%(mem_addr, value))
                data = value & 0xfff
            else:
                data = (value >> 16) & 0xfff
            if (0 != data):
                fail_num += 1
                logerror("data is: 0x%x, when i: %d, mem_addr: 0x%x"%(data, i, mem_addr)) 
        if (0 != fail_num):
            logerror("fail_num: %d"%(fail_num))
            return logfail()
        else:
            return logpass()

    def tc007_dig_adc2_high_test(self):
        '''all adc2 channel in adc2_channel_list should connect to high(3.3v)'''
        if self.chipv == "ESP32":
            adc2_channel_list = [0, 6, 7, 8, 9]
        else:
            adc2_channel_list = range(10)
        fail_num = 0
        chn_num = len(adc2_channel_list)
        full_pattern = 0xffffffff
        table1 = 0xffffffff
        table2 = 0xffffffff
        table3 = 0xffffffff
        pattern1 = 0
        pattern2 = 0
        pattern3 = 0
        if chn_num > 10:
            logerror("wrong channel_list, the length is overflow: %d"%chn_num)
            return
        for i in range(chn_num):
            if i < 4:
                chan = table1 >> (28 - i * 8) & adc2_channel_list[i]
                table1 = (chan << (28 - i * 8)) | (full_pattern >> (2 * i + 1) * 4) | pattern1
                pattern1 = table1 >> (24 - i * 8)  << (24 - i * 8) 
            elif i < 8:
                j = i - 4
                chan = table2 >> (28 - j * 8) & adc2_channel_list[i]
                table2 = (chan << (28 - j * 8)) | (full_pattern >> (2 * j + 1) * 4) | pattern2
                pattern2 = table2 >> (24 - j * 8)  << (24 - j * 8)
            else:
                j = i - 8
                chan = table3 >> (28 - j * 8) & adc2_channel_list[i]
                table3 = (chan << (28 - j * 8)) | (full_pattern >> (2 * j + 1) * 4) | pattern3
                pattern3 = table3 >> (24 - j * 8)  << (24 - j * 8)
        loginfo("table1: 0x%x"%table1)
        loginfo("table2: 0x%x"%table2)
        loginfo("table3: 0x%x"%table3)
        self.chip.dig_adc.config()
        self.chip.dig_adc.i2s()
        self.chip.dig_adc.set_adc2(sar2_patt_len = chn_num - 1, table1 = table1, table2 = table2, table3 = table3)
        first_mem_addr = int(self.chip.dig_adc.read(), 16)
        for i in range(chn_num):
            mem_addr = first_mem_addr + (i / 2) *4
            value = self.chip.MEM.rd(mem_addr)
            if (0 == i % 2):
                loginfo("mem_addr: 0x%x, value: 0x%x"%(mem_addr, value))
                data = value & 0xfff
            else:
                data = (value >> 16) & 0xfff
            if (0xfff != data):
                fail_num += 1
                logerror("data is: 0x%x, when i: %d, mem_addr: 0x%x"%(data, i, mem_addr)) 
        if (0 != fail_num):
            logerror("fail_num: %d"%(fail_num))
            return logfail()
        else:
            return logpass()

    def tc008_double_mode_test(self):
        '''adc1 channel connect to high, adc2 channel connect to low'''
        adc1_channel = 6
        adc2_channel = 4
        full_pattern = 0xffffffff
        adc1_table1 = 0xffffffff
        adc2_table1 = 0xffffffff
        chan_adc1 = (adc1_table1 >> 28) & adc1_channel
        adc1_table1 = (chan_adc1 << 28) | (full_pattern >> 4)
        chan_adc2 = (adc2_table1 >> 28) & adc2_channel
        adc2_table1 = (chan_adc2 << 28) | (full_pattern >> 4)
        loginfo("adc1_table1: 0x%x"%adc1_table1)
        loginfo("adc2_table1: 0x%x"%adc2_table1)
        self.chip.dig_adc.config(work_mod = 1)
        self.chip.dig_adc.i2s(fifo_mode = 0)
        self.chip.dig_adc.set_adc1(sar1_patt_len = 0, table1 = adc1_table1)
        self.chip.dig_adc.set_adc2(sar2_patt_len = 0, table1 = adc2_table1)
        mem_addr = int(self.chip.dig_adc.read(), 16)
        value = self.chip.MEM.rd(mem_addr)
        loginfo("mem_addr: 0x%x, value: 0x%x"%(mem_addr, value))
        high_value = value >> 16
        low_value = value & 0xffff
        sar_sel_high = high_value >> 15
        ch_sel_high = (high_value & 0x7800) >> 11
        adc_data_high = high_value & 0x7ff
        sar_sel_low = low_value >> 15
        ch_sel_low = (low_value & 0x7800) >> 11
        adc_data_low = low_value & 0x7ff
        if (0 != sar_sel_high) or (1 != sar_sel_low) or (adc1_channel != ch_sel_high) or (adc2_channel != ch_sel_low) or (0x7ff != adc_data_high) or (0 != adc_data_low):
            logerror("sar_sel_high: %d, sar_sel_low: %d"%(sar_sel_high, sar_sel_low))
            logerror("ch_sel_high: %d, ch_sel_low: %d"%(ch_sel_high, ch_sel_low))
            logerror("adc_data_high: 0x%x, adc_data_low: 0x%x"%(adc_data_high, adc_data_low))
            return logfail()
        else:
            return logpass()

    def tc009_alternate_mode_test(self):
        '''adc1 channel connect to high, adc2 channel connect to low.'''
        adc1_channel = 6
        adc2_channel = 4
        full_pattern = 0xffffffff
        adc1_table1 = 0xffffffff
        adc2_table1 = 0xffffffff
        chan_adc1 = (adc1_table1 >> 28) & adc1_channel
        adc1_table1 = (chan_adc1 << 28) | (full_pattern >> 4)
        chan_adc2 = (adc2_table1 >> 28) & adc2_channel
        adc2_table1 = (chan_adc2 << 28) | (full_pattern >> 4)
        loginfo("adc1_table1: 0x%x"%adc1_table1)
        loginfo("adc2_table1: 0x%x"%adc2_table1)
        self.chip.dig_adc.config(work_mod = 2)
        self.chip.dig_adc.i2s(fifo_mode = 0)
        self.chip.dig_adc.set_adc1(sar1_patt_len = 0, table1 = adc1_table1)
        self.chip.dig_adc.set_adc2(sar2_patt_len = 0, table1 = adc2_table1)
        mem_addr = int(self.chip.dig_adc.read(), 16)
        value1 = self.chip.MEM.rd(mem_addr)
        value2 = self.chip.MEM.rd(mem_addr + 4)
        loginfo("mem_addr: 0x%x, value1: 0x%x, value2: 0x%x"%(mem_addr, value1, value2))
        high_value1 = value1 >> 16
        low_value1 = value1 & 0xffff
        sar_sel_high1 = high_value1 >> 15
        ch_sel_high1 = (high_value1 & 0x7800) >> 11
        adc_data_high1 = high_value1 & 0x7ff
        sar_sel_low1 = low_value1 >> 15
        ch_sel_low1 = (low_value1 & 0x7800) >> 11
        adc_data_low1 = low_value1 & 0x7ff
        high_value2 = value2 >> 16
        low_value2 = value2 & 0xffff
        sar_sel_high2 = high_value2 >> 15
        ch_sel_high2 = (high_value2 & 0x7800) >> 11
        adc_data_high2 = high_value2 & 0x7ff
        sar_sel_low2 = low_value2 >> 15
        ch_sel_low2 = (low_value2 & 0x7800) >> 11
        adc_data_low2 = low_value2 & 0x7ff
        if ((0 != sar_sel_high1) or (0 != sar_sel_low1) or (adc1_channel != ch_sel_high1) or (adc1_channel != ch_sel_low1) or (0x7ff != adc_data_high1) or (0x7ff != adc_data_low1))     \
            or ((1 != sar_sel_high2) or (1 != sar_sel_low2) or (adc2_channel != ch_sel_high2) or (adc2_channel != ch_sel_low2) or (0 != adc_data_high2) or (0 != adc_data_low2)):
            logerror("sar_sel_high1: %d, sar_sel_low1: %d"%(sar_sel_high1, sar_sel_low1))
            logerror("ch_sel_high1: %d, ch_sel_low1: %d"%(ch_sel_high1, ch_sel_low1))
            logerror("adc_data_high1: 0x%x, adc_data_low1: 0x%x"%(adc_data_high1, adc_data_low1))
            logerror("sar_sel_high2: %d, sar_sel_low2: %d"%(sar_sel_high2, sar_sel_low2))
            logerror("ch_sel_high2: %d, ch_sel_low2: %d"%(ch_sel_high2, ch_sel_low2))
            logerror("adc_data_high2: 0x%x, adc_data_low2: 0x%x"%(adc_data_high2, adc_data_low2))
            return logfail()
        else:
            return logpass()

    def tc010_patt_len_test(self):
        '''set sar1_patt_len to 0, and channel num is more than 1, test if only the fist channel can sample.'''
        adc1_channel_list = [6, 7]
        adc1_chn_num = len(adc1_channel_list)
        full_pattern = 0xffffffff
        adc1_table1 = 0xffffffff
        pattern1 = 0
        for i in range(adc1_chn_num):
            chan = adc1_table1 >> (28 - i * 8) & adc1_channel_list[i]
            adc1_table1 = (chan << (28 - i * 8)) | (full_pattern >> (2 * i + 1) * 4) | pattern1
            pattern1 = adc1_table1 >> (24 - i * 8)  << (24 - i * 8)
        loginfo("adc1_table1: 0x%x"%adc1_table1)
        self.chip.dig_adc.config()
        self.chip.dig_adc.i2s()
        self.chip.dig_adc.set_adc1(sar1_patt_len = 0, table1 = adc1_table1)
        mem_addr = int(self.chip.dig_adc.read(), 16)
        value = self.chip.MEM.rd(mem_addr)
        loginfo("mem_addr: 0x%x, value: 0x%x"%(mem_addr, value))
        channel_1 = value >> 28
        channel_2 = (value >> 12) & 0xf
        loginfo("channel_1: %d, channel_2: %d"%(channel_1, channel_2))
        if (adc1_channel_list[0] != channel_2):
            return logfail()
        else:
            return logpass()

    def tc011_max_meas_num_test(self):
        '''set sar1_patt_len to 0, and channel num is more than 1, test if only the fist channel can sample.'''
        adc1_channel_list = [6, 7]
        adc1_chn_num = len(adc1_channel_list)
        full_pattern = 0xffffffff
        adc1_table1 = 0xffffffff
        pattern1 = 0
        for i in range(adc1_chn_num):
            chan = adc1_table1 >> (28 - i * 8) & adc1_channel_list[i]
            adc1_table1 = (chan << (28 - i * 8)) | (full_pattern >> (2 * i + 1) * 4) | pattern1
            pattern1 = adc1_table1 >> (24 - i * 8)  << (24 - i * 8)
        loginfo("adc1_table1: 0x%x"%adc1_table1)
        self.chip.dig_adc.config()
        self.chip.dig_adc.i2s()
        self.chip.dig_adc.set_adc1(sar1_patt_len = 0, max_meas_num = 1, table1 = adc1_table1)
        mem_addr = int(self.chip.dig_adc.read(), 16)
        value = self.chip.MEM.rd(mem_addr)
        loginfo("mem_addr: 0x%x, value: 0x%x"%(mem_addr, value))
        channel_2 = (value >> 12) & 0xf
        loginfo("channel_2: 0x%x"%( channel_2))
        if (adc1_channel_list[0] == channel_2):
            return logfail()
        else:
            return logpass()

    def tc012_num_limit_test(self):
        '''set sar1_patt_len to 0, and channel num is more than 1, test if only the fist channel can sample.'''
        adc1_channel_list = [1, 2]
        adc1_chn_num = len(adc1_channel_list)
        full_pattern = 0xffffffff
        adc1_table1 = 0xffffffff
        pattern1 = 0
        for i in range(adc1_chn_num):
            chan = adc1_table1 >> (28 - i * 8) & adc1_channel_list[i]
            adc1_table1 = (chan << (28 - i * 8)) | (full_pattern >> (2 * i + 1) * 4) | pattern1
            pattern1 = adc1_table1 >> (24 - i * 8)  << (24 - i * 8)
        loginfo("adc1_table1: 0x%x"%adc1_table1)
        self.chip.dig_adc.config(num_limit = 0)
        self.chip.dig_adc.i2s()
        self.chip.dig_adc.set_adc1(sar1_patt_len = 0, max_meas_num = 1, table1 = adc1_table1)
        read_str = self.chip.dig_adc.read()
        #It's a bug in ESP32
        if self.chipv == "ESP32":
            if (read_str == "TIMEOUT"):
                return logpass()
            else:
                return logfail()
        else:
            if (read_str == "TIMEOUT"):
                return logfail()
            else:
                return logpass()

    def tc013_rtc_adc1_atten_test(self, voltage):
        '''all adc1 channel(connect to awg instrument) in adc1_channel_list should connect to 1.1v(input voltage 1.1v).'''
        self.awg = awg()
        self.awg.appl("DC", 0, 0, voltage)
        time.sleep(0.15)
        return
        adc1_channel_list = [0]
        fail_num = 0
        self.chip.rtc_adc1.config()
        for adc1_channel in adc1_channel_list:
            self.chip.rtc_adc1.set(pad = adc1_channel, atten = 0)
            read_value = int(self.chip.rtc_adc1.read())
            if self.chipv == "ESP8266" or self.chipv == "ESP32" or self.chipv == "CHIP722":
                if (0xfff != read_value):
                    fail_num += 1
                    logerror("fail when adc1_channel: %d, read_value: %d\n"%(adc1_channel, read_value))
            else:
                if (0x1ff != read_value):
                    fail_num += 1
                    logerror("fail when adc1_channel: %d, read_value: %d\n"%(adc1_channel, read_value))
        if (0 != fail_num):
            logerror("fail_num: %d"%(fail_num))
            return logfail()
        else:
            return logpass()

    def tc014_adc1_read_lightsleep(self):
        '''adc1 channel(adc1_channel 6) should connect to high(3.3v)'''
        if self.chipv == "ESP32":
            lowpower_state_addr = self.chip.HWREG.RTC_CNTL.RTC_DIAG0._RTC_DIAG0__addr
            slp_timer_en_addr = self.chip.HWREG.RTC_CNTL.RTC_STATE0._RTC_STATE0__addr
            slp_timer_en_lsb = self.chip.HWREG.RTC_CNTL.RTC_STATE0._RTC_STATE0__reg_sar_slp_timer_en_lsb
            slp_timer_en_msb = self.chip.HWREG.RTC_CNTL.RTC_STATE0._RTC_STATE0__reg_sar_slp_timer_en_msb
        else:
            lowpower_state_addr = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__addr
            lowpower_state_lsb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_lsb
            lowpower_state_msb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_msb
            slp_timer_en_addr = self.chip.HWREG.RTC_CNTL.RTC_ULP_CP_TIMER._RTC_ULP_CP_TIMER__addr
            slp_timer_en_lsb = self.chip.HWREG.RTC_CNTL.RTC_ULP_CP_TIMER._RTC_ULP_CP_TIMER__reg_ulp_cp_slp_timer_en_lsb
            slp_timer_en_msb = self.chip.HWREG.RTC_CNTL.RTC_ULP_CP_TIMER._RTC_ULP_CP_TIMER__reg_ulp_cp_slp_timer_en_msb
        adc1_channel = 6
        self.chip.rtc_adc1.config()
        self.chip.rtc_adc1.set(pad = adc1_channel, ulp = True)
        self.chip.ulp.init()
        self.chip.ulp.movi(ULP_PARAM['R1'].value, 0)
        if self.chipv == "ESP32":
            self.chip.ulp.ldr(lowpower_state_addr, 19, 19)
        else:
            self.chip.ulp.ldr(lowpower_state_addr, lowpower_state_msb, lowpower_state_lsb)
        self.chip.ulp.blr(1, 5)
        if self.chipv == "ESP32":
            self.chip.ulp.meas_adc0(ULP_PARAM['R2'].value, adc1_channel + 1)
        else:
            self.chip.ulp.meas_adc0(ULP_PARAM['R2'].value, adc1_channel)
        self.chip.ulp.stm(ULP_PARAM['R2'].value, ULP_PARAM['R1'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.str(slp_timer_en_addr, slp_timer_en_msb, slp_timer_en_lsb, 0)
        self.chip.ulp.wakeup()
        self.chip.ulp.end()
        self.chip.ulp.start(1)
        self.chip.rtc_sleep.sleep(0, WAKEUP_ENABLE['SAR_TRIG_EN'].value, 0)
        time.sleep(1)
        wakeup_cause = int(self.chip.rtc_sleep.wakeup_cause())
        if wakeup_cause == WAKEUP_REASON['SAR_TRIG'].value:
            adc1_value = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
            if (0xfff != adc1_value):
                logerror("adc1_value: 0x%x\n"%(adc1_value))
                return logfail()
            else:
                return logpass()
        else:
            return logfail()

    def tc015_adc1_read_deepsleep(self):
        '''adc1 channel(adc1_channel 6) should connect to high(3.3v)'''
        if self.chipv == "ESP32":
            lowpower_state_addr = self.chip.HWREG.RTC_CNTL.RTC_DIAG0._RTC_DIAG0__addr
            slp_timer_en_addr = self.chip.HWREG.RTC_CNTL.RTC_STATE0._RTC_STATE0__addr
            slp_timer_en_lsb = self.chip.HWREG.RTC_CNTL.RTC_STATE0._RTC_STATE0__reg_sar_slp_timer_en_lsb
            slp_timer_en_msb = self.chip.HWREG.RTC_CNTL.RTC_STATE0._RTC_STATE0__reg_sar_slp_timer_en_msb
        else:
            lowpower_state_addr = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__addr
            lowpower_state_lsb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_lsb
            lowpower_state_msb = self.chip.HWREG.RTC_CNTL.RTC_LOW_POWER_ST._RTC_LOW_POWER_ST__rtc_in_low_power_state_msb
            slp_timer_en_addr = self.chip.HWREG.RTC_CNTL.RTC_ULP_CP_TIMER._RTC_ULP_CP_TIMER__addr
            slp_timer_en_lsb = self.chip.HWREG.RTC_CNTL.RTC_ULP_CP_TIMER._RTC_ULP_CP_TIMER__reg_ulp_cp_slp_timer_en_lsb
            slp_timer_en_msb = self.chip.HWREG.RTC_CNTL.RTC_ULP_CP_TIMER._RTC_ULP_CP_TIMER__reg_ulp_cp_slp_timer_en_msb
        adc1_channel = 6
        self.chip.rtc_adc1.config()
        self.chip.rtc_adc1.set(pad = adc1_channel, ulp = True)
        self.chip.ulp.init()
        self.chip.ulp.movi(ULP_PARAM['R1'].value, 0)
        if self.chipv == "ESP32":
            self.chip.ulp.ldr(lowpower_state_addr, 19, 19)
        else:
            self.chip.ulp.ldr(lowpower_state_addr, lowpower_state_msb, lowpower_state_lsb)
        self.chip.ulp.blr(1, 5)
        if self.chipv == "ESP32":
            self.chip.ulp.meas_adc0(ULP_PARAM['R2'].value, adc1_channel + 1)
        else:
            self.chip.ulp.meas_adc0(ULP_PARAM['R2'].value, adc1_channel)
        self.chip.ulp.stm(ULP_PARAM['R2'].value, ULP_PARAM['R1'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
        self.chip.ulp.str(slp_timer_en_addr, slp_timer_en_msb, slp_timer_en_lsb, 0)
        self.chip.ulp.wakeup()
        self.chip.ulp.end()
        self.chip.ulp.start(1)
        self.chip.rtc_sleep.sleep(0x21, WAKEUP_ENABLE['SAR_TRIG_EN'].value, 0)
        time.sleep(1)
        wakeup_cause = int(self.chip.rtc_sleep.wakeup_cause())
        if wakeup_cause == WAKEUP_REASON['SAR_TRIG'].value:
            adc1_value = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value) & 0xffff
            if (0xfff != adc1_value):
                logerror("adc1_value: 0x%x\n"%(adc1_value))
                return logfail()
            else:
                return logpass()
        else:
            return logfail()

    def tc016_adc1_read_lowspeed(self):
        '''adc1 channel(adc1_channel 6) should connect to high(3.3v)'''
        adc1_channel = 6
        self.chip.rtc_clk.set_cpu_freq(4)
        self.chip.rtc_adc1.config()
        self.chip.rtc_adc1.set(pad = adc1_channel)
        adc1_value = int(self.chip.rtc_adc1.read())
        if self.chipv == "ESP8266" or self.chipv == "ESP32" or self.chipv == "CHIP722":
            if (0xfff != adc1_value):
                logerror("adc1_value: 0x%x"%(adc1_value))
                return logfail()
            else:
                return logpass()
        else:
            if (0x1ff != adc1_value):
                logerror("adc1_value: 0x%x"%(adc1_value))
                return logfail()
            else:
                return logpass()

    def tc017_adc1_read_wifiinit(self):
        '''adc1 channel(adc1_channel 6) should connect to high(3.3v)'''
        adc1_channel = 6
        self.chip.wifimac.mac_init()
        self.chip.rtc_adc1.config()
        self.chip.rtc_adc1.set(pad = adc1_channel)
        adc1_value = int(self.chip.rtc_adc1.read())
        if self.chipv == "ESP8266" or self.chipv == "ESP32" or self.chipv == "CHIP722":
            if (0xfff != adc1_value):
                logerror("adc1_value: 0x%x"%(adc1_value))
                return logfail()
        else:
            if (0x1ff != adc1_value):
                logerror("adc1_value: 0x%x"%(adc1_value))
                return logfail()
        return logpass()

    def tc018_adc2_grantforce_test(self, adc2_channel = 6):
        if self.chipv == "CHIP722":
            self.chip.rtc_adc2.config()
            self.chip.rtc_adc2.set(pad = adc2_channel)
            table1 = 0xfffffff + (adc2_channel << 28)
            loginfo("table1: 0x%x"%table1)
            self.chip.dig_adc.config()
            self.chip.dig_adc.i2s()
            self.chip.dig_adc.set_adc2(sar2_patt_len = 0, table1 = table1)
            self.chip.adc2_arb.config(grant_force = 1,  wifi_force = 1)
            rtc_value1 = int(self.chip.rtc_adc2.read())
            mem_addr1 = int(self.chip.dig_adc.read(), 16)
            dig_value1 = ((self.chip.MEM.rd(mem_addr1)) >> 16) & 0xffff
            vdd33_value1 = int(self.chip.adc2_arb.get_vdd33())
            rtc_flag1 = rtc_value1 >> 14
            dig_flag1 = dig_value1 >> 12
            vdd33_flag1 = vdd33_value1 >> 12
            loginfo("when wifi_force=1, rtc_value1: 0x%x, dig_value1: 0x%x, vdd33_value1: %d"%(rtc_value1, dig_value1, vdd33_value1))
            loginfo("when wifi_force=1, rtc_flag1: 0x%x, dig_flag1: 0x%x, vdd33_flag1: %d"%(rtc_flag1, dig_flag1, vdd33_flag1))
            self.chip.adc2_arb.config(grant_force = 1,  rtc_force = 1)
            rtc_value2 = int(self.chip.rtc_adc2.read())
            mem_addr2 = int(self.chip.dig_adc.read(), 16)
            dig_value2 = ((self.chip.MEM.rd(mem_addr2)) >> 16) & 0xffff
            vdd33_value2 = int(self.chip.adc2_arb.get_vdd33())
            rtc_flag2 = rtc_value2 >> 14
            dig_flag2 = dig_value2 >> 12
            vdd33_flag2 = vdd33_value2 >> 12
            loginfo("when rtc_force = 1, rtc_value2: 0x%x, dig_value2: 0x%x, vdd33_value2: %d"%(rtc_value2, dig_value2, vdd33_value2))
            loginfo("when rtc_force=1, rtc_flag2: 0x%x, dig_flag2: 0x%x, vdd33_flag2: %d"%(rtc_flag2, dig_flag2, vdd33_flag2))
            self.chip.adc2_arb.config(grant_force = 1,  dig_force = 1)
            rtc_value3 = int(self.chip.rtc_adc2.read())
            mem_addr3 = int(self.chip.dig_adc.read(), 16)
            dig_value3 = ((self.chip.MEM.rd(mem_addr3)) >> 16) & 0xffff
            vdd33_value3 = int(self.chip.adc2_arb.get_vdd33())
            rtc_flag3 = rtc_value3 >> 14
            dig_flag3 = dig_value3 >> 12
            vdd33_flag3 = vdd33_value3 >> 12
            loginfo("when dig_force = 1, rtc_value3: 0x%x, dig_value3: 0x%x, vdd33_value3: %d"%(rtc_value3, dig_value3, vdd33_value3))
            loginfo("when dig_force=1, rtc_flag3: 0x%x, dig_flag3: 0x%x, vdd33_flag3: %d"%(rtc_flag3, dig_flag3, vdd33_flag3))
            if ((1 == rtc_flag1) and (0xe == dig_flag1) and not vdd33_flag1) and (not rtc_flag2 and (0xe == dig_flag2) and (1 == vdd33_flag2)) and ((1 == rtc_flag3) and (adc2_channel == dig_flag3) and (1 == vdd33_flag3)):
                return logpass()
            else:
                return logfail()

    def tc019_adc2_fixpri_test(self, adc2_channel = 6, rtc_pri = 1, dig_pri = 2, wifi_pri = 0):
        if self.chipv == "CHIP722":
            rtc_arb_symble = 0
            vdd33_arb_symble = 0
            read_times = 20
            self.chip.adc2_arb.config(fix_pri = 1, rtc_pri = rtc_pri, dig_pri = dig_pri, wifi_pri = wifi_pri)
            self.chip.rtc_adc2.config()
            self.chip.rtc_adc2.set(pad = adc2_channel, ulp = True)
            table1 = 0xfffffff + (adc2_channel << 28)
            loginfo("table1: 0x%x"%table1)
            self.chip.dig_adc.config()
            self.chip.dig_adc.set_adc2(sar2_patt_len = 0, table1 = table1)
            self.chip.dig_adc.dig_adc_timer_en()
            rtc_value_list = []
            vdd33_value_list = []
            self.chip.ulp.init()
            self.chip.ulp.set_ulp_slp_time(10)
            self.chip.ulp.meas_adc1(ULP_PARAM['R1'].value, adc2_channel)
            self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R0'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.addi(ULP_PARAM['R0'].value, ULP_PARAM['R0'].value, 1)
            self.chip.ulp.end()
            self.chip.ulp.start(1)
            for i in range(read_times):
                rtc_value = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value + i * 4) & 0xffff
                rtc_value_list.append(rtc_value)
                rtc_arbiter_flag = rtc_value >> 14
                if (rtc_arbiter_flag != 0):
                    rtc_arb_symble = rtc_arb_symble + 1
                vdd33_value = int(self.chip.adc2_arb.get_vdd33())
                vdd33_value_list.append(vdd33_value)
                vdd33_arbiter_flag = vdd33_value >> 12
                if (vdd33_arbiter_flag != 0):
                    vdd33_arb_symble = vdd33_arb_symble + 1
            loginfo("rtc_value_list: ", rtc_value_list)
            loginfo("vdd33_value_list: ", vdd33_value_list)
            loginfo("rtc_arb_symble: %d, vdd33_arb_symble: %d"%(rtc_arb_symble, vdd33_arb_symble))
            if (read_times == rtc_arb_symble) and (read_times == vdd33_arb_symble):
                return logpass()
            else:
                return logfail()

    def tc020_adc2_looppri_wifi_test(self, adc2_channel = 6, ulp_slptime = 500, times = 1000):
        '''
        要测试到vdd33和adc(rtc_adc或dig_adc)碰撞的情况，增加碰撞概率需满足以下条件才可能产生：
        a) ulp_slptime时间设置为较大值（此时rtc_adc可能无法得到有效adc数值）；
        b) vdd33 max_sample设置为0，缩短vdd33时间；
        c) SAR2 XPD_WAIT配置为最大值0xff, SAR2_RSTB_WAIT配置为对大值0xff，增加dig_adc2一次采样时间；
        '''
        if self.chipv == "CHIP722":
            self.chip.adc2_arb.config(fix_pri = 0)
            self.chip.rtc_adc2.config()
            self.chip.rtc_adc2.set(pad = adc2_channel, ulp = True)
            self.chip.ulp.init()
            self.chip.ulp.set_ulp_slp_time(ulp_slptime)
            self.chip.ulp.meas_adc1(ULP_PARAM['R1'].value, adc2_channel)
            self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R0'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.addi(ULP_PARAM['R0'].value, ULP_PARAM['R0'].value, 1)
            self.chip.ulp.end()
            self.chip.ulp.start(1)
            table1 = 0xfffffff + (adc2_channel << 28)
            loginfo("table1: 0x%x"%table1)
            self.chip.dig_adc.config()
            self.chip.dig_adc.set_adc2(sar2_patt_len = 0, table1 = table1)
            self.chip.dig_adc.dig_adc_timer_en(cycle=256)
            self.chip.HWREG.SARADC.SAR_MEAS2_CTRL1.reg_sar2_xpd_wait = 0xff
            self.chip.HWREG.SARADC.SAR_MEAS2_CTRL1.reg_sar2_rstb_wait = 0xff
            vdd33value_withflag_num = 0
            vdd33value_withflag_list, flag_list = [], []
            for i in range(times):
                vdd33_value = int(self.chip.adc2_arb.get_vdd33(sample_num = 0))
                vdd33_arbiter_flag = vdd33_value >> 12
                if vdd33_arbiter_flag:
                    vdd33value_withflag_list.append(vdd33_value)
                    flag_list.append(vdd33_arbiter_flag)
                    vdd33value_withflag_num = vdd33value_withflag_num + 1
            loginfo("vdd33value_withflag_list: ", vdd33value_withflag_list)
            loginfo("flag_list: ", flag_list)
            loginfo("vdd33value_withflag_num: [%d]"%(vdd33value_withflag_num))
            if vdd33value_withflag_num:
                return logpass()
            else:
                return logfail()

    def tc021_adc2_looppri_rtcadc_test(self, adc2_channel = 6, ulp_slptime = 10, times = 1000):
        '''
        ulp_slptime和dig_adc　timer时间都设置为尽量小的数值，增加rtc_adc和digital_adc碰撞的几率。
        '''
        if self.chipv == "CHIP722":
            self.chip.adc2_arb.config(fix_pri = 0)
            self.chip.rtc_adc2.config()
            self.chip.rtc_adc2.set(pad = adc2_channel, ulp = True)
            table1 = 0xfffffff + (adc2_channel << 28)
            loginfo("table1: 0x%x"%table1)
            self.chip.dig_adc.config()
            self.chip.dig_adc.set_adc2(sar2_patt_len = 0, table1 = table1)
            self.chip.dig_adc.dig_adc_timer_en(cycle = 10)
            self.chip.ulp.init()
            self.chip.ulp.set_ulp_slp_time(ulp_slptime)
            self.chip.ulp.meas_adc1(ULP_PARAM['R1'].value, adc2_channel)
            self.chip.ulp.stm(ULP_PARAM['R1'].value, ULP_PARAM['R0'].value, ULP_PARAM['RTC_MEM_DATA_OFFSET'].value)
            self.chip.ulp.addi(ULP_PARAM['R0'].value, ULP_PARAM['R0'].value, 1)
            self.chip.ulp.end()
            self.chip.ulp.start(1)
            rtcvalue_withflag_num, fail_num, flag_symble = 0, 0, 1
            rtcvalue_withflag_list, flag_list = [], []
            for i in range(times):
                rtc_value = self.chip.MEM.rd(ULP_PARAM['RTC_MEM_DATA'].value + i * 4) & 0xffff
                rtc_arbiter_flag = rtc_value >> 14
                if rtc_arbiter_flag:
                    rtcvalue_withflag_list.append(rtc_value)
                    flag_list.append(rtc_arbiter_flag)
                    rtcvalue_withflag_num = rtcvalue_withflag_num + 1
            for flag_value in flag_list:
                if (flag_symble != flag_value):
                    fail_num += 1
            loginfo("rtcvalue_withflag_list: ", rtcvalue_withflag_list)
            loginfo("flag_list: ", flag_list)
            loginfo("rtcvalue_withflag_num: [%d], fail_num: [%d]"%(rtcvalue_withflag_num, fail_num))
            if rtcvalue_withflag_num and not fail_num:
                return logpass()
            else:
                return logfail()
