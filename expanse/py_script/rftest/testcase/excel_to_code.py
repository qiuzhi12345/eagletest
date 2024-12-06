#!/usr/bin/python
# -*- coding:utf8 -*-

import re
from baselib.loglib.log_lib import *

import numpy as np
import pandas as pd
import scipy
from math import *
from shutil import copy
import time
import csv
import pylab
import matplotlib.pyplot as plt
from baselib.test_channel import *
import xlrd
import sys
import random
import os

import serial
from sys import argv
import binascii
from binascii import b2a_hex, a2b_hex
import pylink
import docx
from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.enum.text import WD_TAB_ALIGNMENT,WD_TAB_LEADER #设置制表符等
from docx.shared import Inches #设置图像大小
from docx.shared import Pt #设置像素、缩进等
from docx.shared import RGBColor #设置字体颜色
from docx.shared import Length #设置宽度
import win32api
import shutil


def excel_to_c(self, filepath=''):
    import xlrd
    from glob import glob
    '''
    获取要转换的excel文件路径
    '''
    # path_name_list=[]
    # if os.path.isdir(filepath):
    #     path_names = os.listdir(filepath)
    #     for _path_name in path_names:
    #         if _path_name.find('bt_') !=-1:
    #             _path_name = os.path.join(filepath,_path_name)
    #             path_name_list.append(_path_name)
    path_name_list = glob(filepath + '\\bt_*.xlsx')
    '''
    读取excel表格并转换为c代码
    '''
    for path_name in path_name_list:
        datafile = xlrd.open_workbook(filename=path_name)
        names = datafile.sheet_names()
        for name in names:
            logdebug(name)
            fname = self.get_filename('ts_bt_test/', name)
            with open('{}.h'.format(fname), 'w+') as f:
                # f.write('struct {}'.format(name.upper())+'{\n')
                f.write('#ifndef __{}_H__\n'.format(name.upper()))
                f.write('#define __{}_H__\n \n'.format(name.upper()))
                f.write('#include "chip_public.h"\n \n')
                if name == 'bt_modem':
                    table = datafile.sheet_by_name(name)
                    nrows = table.nrows
                    logdebug(nrows)
                    struct_name_list = []
                    for i in range(nrows):
                        if table.cell_value(i, 0).find('0x') != -1:  ##addr offset所在行查找
                            addr_offset = table.cell_value(i, 0)
                            struct_name = table.cell_value(i, 1)
                            struct_name_list.append([struct_name, addr_offset])
                            logdebug('addr_offset: {};   struct_name:   {}'.format(addr_offset, struct_name))
                            w_str = '//offset address: {}\n'.format(addr_offset) + '  union REG_{}\n'.format(struct_name.upper()) + '  {\n' + '    DRV_IOM uint32_t raw;\n' + '    ' \
                                                                                                                                                                              'struct' + '{\n'
                            for j in range(40):
                                if table.cell_value(i + j, 0).find(':0]') != -1 or table.cell_value(i + j, 0) == '0]':  ##一个32位寄存器所有bit定义的起始行查找
                                    w_bit_row_start = i + j
                                    w_bit_row_stop = i + 1
                                    logdebug('w_bit_row_start:  {}; w_bit_row_stop: {}'.format(w_bit_row_start, w_bit_row_stop))
                                    break
                            bit_num_check = 0
                            for row in range(w_bit_row_start, i, -1):  ##bit位定义，bit位数确定以及定义，描述
                                reg_bit = table.cell_value(row, 0).replace(']', '').replace('[', '')
                                logdebug('reg_bit:  {}'.format(reg_bit))
                                if reg_bit.find(':') != -1:
                                    _reg_bit = reg_bit.split(':')
                                    bit_num = eval(_reg_bit[0]) - eval(_reg_bit[1]) + 1
                                elif reg_bit == '':
                                    continue
                                else:
                                    bit_num = 1
                                logdebug('bit_num:  {}'.format(bit_num))
                                bit_num_check = bit_num_check + bit_num
                                reg_name = table.cell_value(row, 1).replace('reserved', '  ')
                                reg_name = reg_name.split('[')[0]
                                reg_desc = table.cell_value(row, 4).replace('\n', ';  ')
                                logdebug('reg_name:{}    reg_desc:{}'.format(reg_name, reg_desc))
                                w_bit = '      DRV_IOM uint32_t {}'.format(reg_name) + (40 - len(reg_name)) * ' ' + ':{} ;      //{}\n'.format(bit_num, reg_desc)
                                w_str = w_str + w_bit
                            if bit_num_check != 32:
                                logerror('{}    {}      bit total is {},please check table!'.format(name, struct_name, bit_num_check))
                                raise
                            w_str = w_str + '         }' + 'bits;\n' + '  }' + ';\n' + '\n'
                            f.write(w_str)

                    w_str = 'typedef struct {}_reg\n'.format(name) + '{\n'
                    f.write(w_str)
                    addr_offset_pre = 0
                    addr_step_flag = 0
                    for struct_name_t in struct_name_list:
                        addr_offset_now = eval(struct_name_t[1])
                        addr_step = addr_offset_now - addr_offset_pre
                        if addr_step > 4:
                            w_str_addr_offset = 'DRV_IOM uint32_t  rev_{}[({} - {}) / 4 - 1];\n'.format(addr_step_flag, addr_offset_now, addr_offset_pre)
                            addr_step_flag = addr_step_flag + 1
                            f.write(w_str_addr_offset)
                        w_str_name_t = 'union REG_{}'.format(struct_name_t[0].upper()) + (40 - len(struct_name_t[0])) * ' ' + '{};\n'.format(struct_name_t[0].upper())
                        f.write(w_str_name_t)
                        addr_offset_pre = addr_offset_now
                    f.write('}' + '{}_reg_t;\n \n'.format(name))
                    f.write('#define {}                                (({}_reg_t *) {}_BASE)\n \n#endif'.format(name.upper(), name, name.upper()))
                    f.close()
                # elif name == 'bt_rf':
                #     table = datafile.sheet_by_name(name)
                #     nrows = table.nrows
                #     logdebug(nrows)
                #     struct_name_list = []
                #     for i in range(nrows):
                #         if type(table.cell_value(i, 1)) == int or type(table.cell_value(i, 1)) == float:
                #             aa = str(table.cell_value(i, 1))
                #         else:
                #             aa = table.cell_value(i, 1)
                #         logdebug(aa.encode('utf-8'))
                #         if aa.encode('utf-8').find('Offset:') != -1:
                #             addr_offset = table.cell_value(i, 0).split(':')[1]
                #             if name == 'bt_core_reg':
                #                 struct_name = table.cell_value(i - 1, 0).split('(')[0].replace(' ', '')
                #             else:
                #                 struct_name = table.cell_value(i - 1, 0).split('(')[1].replace(')', '')
                #             logdebug('addr_offset: {};   struct_name:   {}'.format(addr_offset, struct_name))
                #             struct_name_list.append([struct_name, addr_offset])
                #             w_str = '//offset address: {}\n'.format(addr_offset) + '  union REG_{}\n'.format(
                #                 struct_name.upper()) + '  {\n' + '    DRV_IOM uint32_t raw;\n' + '    ' \
                #                                                                                  'struct' + '{\n'
                #             for j in range(1, 40):
                #                 if str(table.cell_value(i + j, 0)).find(':0') != -1 or str(table.cell_value(i + j, 0)) == '0' or str(table.cell_value(i + j, 0)) == '0.0':
                #                     w_bit_row_start = i + j
                #                     w_bit_row_stop = i + 1
                #                     logdebug('w_bit_row_start:  {}; w_bit_row_stop: {}'.format(w_bit_row_start, w_bit_row_stop))
                #                     break
                #             bit_num_check = 0
                #             for row in range(w_bit_row_start, i + 1, -1):
                #                 reg_bit = str(table.cell_value(row, 0)).replace(']', '').replace('[', '')
                #                 logdebug('reg_bit:  {}'.format(reg_bit))
                #                 if reg_bit.find(':') != -1:
                #                     _reg_bit = reg_bit.split(':')
                #                     bit_num = eval(_reg_bit[0]) - eval(_reg_bit[1]) + 1
                #                 elif reg_bit == '':
                #                     continue
                #                 else:
                #                     bit_num = 1
                #                 logdebug('bit_num:  {}'.format(bit_num))
                #                 bit_num_check = bit_num_check + bit_num
                #                 reg_name = table.cell_value(row, 1).replace('NA', '  ').replace('reserved', '  ')
                #                 # reg_name = table.cell_value(row, 2).replace('reserved', '  ')
                #                 reg_name = reg_name.split('[')[0]
                #                 reg_desc = table.cell_value(row, 4).replace('-', '').replace('\n', ';  ').encode('utf-8')
                #                 logdebug('reg_name:{}    reg_desc:{}'.format(reg_name, reg_desc))
                #                 w_bit = '      DRV_IOM uint32_t {}'.format(reg_name) + (40 - len(reg_name)) * ' ' + ':{} ;      //{}\n'.format(bit_num, reg_desc)
                #                 w_str = w_str + w_bit
                #             if bit_num_check != 32:
                #                 logerror('{}    {}      bit total is {},please check table!'.format(name, struct_name, bit_num_check))
                #                 raise
                #             w_str = w_str + '         }' + 'bits;\n' + '  }' + ';\n' + '\n'
                #             f.write(w_str)
                #
                #     w_str = 'typedef struct {}_reg\n'.format(name) + '{\n'
                #     f.write(w_str)
                #     addr_offset_pre = 0
                #     addr_step_flag = 0
                #     for struct_name_t in struct_name_list:
                #         addr_offset_now = eval(struct_name_t[1])
                #         addr_step = addr_offset_now - addr_offset_pre
                #         if addr_step > 4:
                #             w_str_addr_offset = 'DRV_IOM uint32_t  rev_{}[({} - {}) / 4 - 1];\n'.format(addr_step_flag, addr_offset_now, addr_offset_pre)
                #             addr_step_flag = addr_step_flag + 1
                #             f.write(w_str_addr_offset)
                #         w_str_name_t = 'union REG_{}'.format(struct_name_t[0].upper()) + (40 - len(struct_name_t[0])) * ' ' + '{};\n'.format(struct_name_t[0].upper())
                #         f.write(w_str_name_t)
                #         addr_offset_pre = addr_offset_now
                #     f.write('}' + '{}_reg_t;\n \n'.format(name))
                #     f.write('#define {}                                (({}_reg_t *) {}_BASE)\n \n#endif'.format(name.upper(), name, name.upper()))
                #     f.close()
                else:
                    table = datafile.sheet_by_name(name)
                    nrows = table.nrows
                    logdebug(nrows)
                    struct_name_list = []
                    for i in range(nrows):
                        if type(table.cell_value(i, 0)) == int or type(table.cell_value(i, 0)) == float:
                            aa = str(table.cell_value(i, 0))
                        else:
                            aa = table.cell_value(i, 0)
                        logdebug(aa.encode('utf-8'))
                        if aa.encode('utf-8').find('Offset:') != -1:
                            addr_offset = table.cell_value(i, 0).split(':')[1]
                            if name == 'bt_core_reg':
                                struct_name = table.cell_value(i - 1, 0).split('(')[0].replace(' ', '')
                            else:
                                struct_name = table.cell_value(i - 1, 0).split('(')[1].replace(')', '')
                            logdebug('addr_offset: {};   struct_name:   {}'.format(addr_offset, struct_name))
                            struct_name_list.append([struct_name, addr_offset])
                            w_str = '//offset address: {}\n'.format(addr_offset) + '  union REG_{}\n'.format(struct_name.upper()) + '  {\n' + '    DRV_IOM uint32_t raw;\n' + '    ' \
                                                                                                                                                                              'struct' + '{\n'
                            for j in range(1, 40):
                                if str(table.cell_value(i + j, 0)).find(':0') != -1 or str(table.cell_value(i + j, 0)) == '0' or str(table.cell_value(i + j, 0)) == '0.0':
                                    w_bit_row_start = i + j
                                    w_bit_row_stop = i + 1
                                    logdebug('w_bit_row_start:  {}; w_bit_row_stop: {}'.format(w_bit_row_start, w_bit_row_stop))
                                    break
                            bit_num_check = 0
                            for row in range(w_bit_row_start, i + 1, -1):
                                reg_bit = str(table.cell_value(row, 0)).replace(']', '').replace('[', '')
                                logdebug('reg_bit:  {}'.format(reg_bit))
                                if reg_bit.find(':') != -1:
                                    _reg_bit = reg_bit.split(':')
                                    bit_num = eval(_reg_bit[0]) - eval(_reg_bit[1]) + 1
                                elif reg_bit == '':
                                    continue
                                else:
                                    bit_num = 1
                                logdebug('bit_num:  {}'.format(bit_num))
                                bit_num_check = bit_num_check + bit_num
                                reg_name = table.cell_value(row, 1).replace('NA', '  ').replace('reserved', '  ')
                                # reg_name = table.cell_value(row, 1).replace('reserved', '  ')
                                reg_name = reg_name.split('[')[0]
                                reg_desc = table.cell_value(row, 4).replace('-', '').replace('\n', ';  ').encode('utf-8')
                                logdebug('reg_name:{}    reg_desc:{}'.format(reg_name, reg_desc))
                                w_bit = '      DRV_IOM uint32_t {}'.format(reg_name) + (40 - len(reg_name)) * ' ' + ':{} ;      //{}\n'.format(bit_num, reg_desc)
                                w_str = w_str + w_bit
                            if bit_num_check != 32:
                                logerror('{}    {}      bit total is {},please check table!'.format(name, struct_name, bit_num_check))
                                raise
                            w_str = w_str + '         }' + 'bits;\n' + '  }' + ';\n' + '\n'
                            f.write(w_str)

                    w_str = 'typedef struct {}_reg\n'.format(name) + '{\n'
                    f.write(w_str)
                    addr_offset_pre = 0
                    addr_step_flag = 0
                    for struct_name_t in struct_name_list:
                        addr_offset_now = eval(struct_name_t[1])
                        addr_step = addr_offset_now - addr_offset_pre
                        if addr_step > 4:
                            w_str_addr_offset = 'DRV_IOM uint32_t  rev_{}[({} - {}) / 4 - 1];\n'.format(addr_step_flag, addr_offset_now, addr_offset_pre)
                            addr_step_flag = addr_step_flag + 1
                            f.write(w_str_addr_offset)
                        w_str_name_t = 'union REG_{}'.format(struct_name_t[0].upper()) + (40 - len(struct_name_t[0])) * ' ' + '{};\n'.format(struct_name_t[0].upper())
                        f.write(w_str_name_t)
                        addr_offset_pre = addr_offset_now
                    f.write('}' + '{}_reg_t;\n \n'.format(name))
                    f.write('#define {}                                (({}_reg_t *) {}_BASE)\n \n#endif'.format(name.upper(), name, name.upper()))
                    f.close()

