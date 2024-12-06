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

class gdb_server(object):
    def __init__(self,core='N22'):

        if core == 'N22':
            win32api.ShellExecute(0, 'open', 'JLinkGDBServer.exe',
                              '-select USB -device rv32 -endian little -if JTAG -speed 5000 -ir -LocalhostOnly -nologtofile -port 2335 -SWOPort 2336 -TelnetPort 2337 -jtagconf 5,1',
                              '', 1)
        else:
            win32api.ShellExecute(0, 'open', 'JLinkGDBServer.exe',
                              '-select USB -device rv32 -endian little -if JTAG -speed 5000 -ir -LocalhostOnly -nologtofile -port 2331 -SWOPort 2332 -TelnetPort 2333',
                              '', 1)


from pygdbmi.gdbcontroller import GdbController
class gdb_load_code(object):

    def __init__(self, core='N22'):
        self.core = core
        if self.core == 'N22':
            self.gdbmin = GdbController(r'E:\project_audio\expanse\tx232_driver_src\toolchains\nds32le-elf-mculib-v5\bin\riscv32-elf-gdb', ['riscv32.elf'])
        else:
            self.gdbmin = GdbController(r'E:\project_audio\expanse\tx232_driver_src\toolchains\nds32le-elf-mculib-v5f\bin\riscv32-elf-gdb', ['riscv32.elf'])
    def close(self):
        self.gdbmin.exit()
    def open(self):
        if self.core == 'N22':
            self.gdbmin = GdbController(r'E:\project_audio\expanse\tx232_driver_src\toolchains\nds32le-elf-mculib-v5\bin\riscv32-elf-gdb', ['riscv32.elf'])
        else:
            self.gdbmin = GdbController(r'E:\project_audio\expanse\tx232_driver_src\toolchains\nds32le-elf-mculib-v5f\bin\riscv32-elf-gdb', ['riscv32.elf'])
    def load_file(self,filepath=''):
        self.close()
        self.open()
        self.gdbmin.write('file {}'.format(filepath.replace('\\','/')),timeout_sec=5,read_response=False)
        self.gdbmin.write('load',timeout_sec=20,read_response=False)
        self.gdbmin.write('c',timeout_sec=20,read_response=False)
