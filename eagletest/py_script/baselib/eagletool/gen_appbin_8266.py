#
#  Copyright (c) 2010 Espressif System
#
#     grab user_start() address and pass it to genflashbin program
#

#!/usr/bin/python
import platform
import string
import sys
import os
import re
import shutil

if len(sys.argv) != 5:
    print 'Usage: gen_appbin.py eagle.app.out version subversion'
    sys.exit(0)

elf_file = sys.argv[1]
ver = sys.argv[2]
subver = sys.argv[3]
gcc = sys.argv[4]
#print elf_file

cmd = '%s-nm -g '%gcc + elf_file + ' > eagle.app.sym'
print "00000000cmd:", cmd
os.system(cmd)

fp = file('./eagle.app.sym')
if fp is None:
    print "open sym file error\n"
    exit

lines = fp.readlines()

fp.close()

entry_addr = None
p = re.compile('(\w*)(\sT\s)(call_user_start)$')
for line in lines:
    m = p.search(line)
    if m != None:
        entry_addr = m.group(1)
        #entry_addr = int(entry_addr, 16)
        print "entry_addr: ", entry_addr

if entry_addr is None:
    print 'no entry point!!'
    exit

data_start_addr = '0'
p = re.compile('(\w*)(\sA\s)(_data_start)$')
for line in lines:
    m = p.search(line)
    if m != None:
        data_start_addr = m.group(1)
        print "data_start_addr: ", data_start_addr

rodata_start_addr = '0'
p = re.compile('(\w*)(\sA\s)(_rodata_start)$')
for line in lines:
    m = p.search(line)
    if m != None:
        rodata_start_addr = m.group(1)
        print "rodata_start_addr", rodata_start_addr

print "**", platform.platform()
print os.getcwd()
if platform.platform().find("Linux") != -1:
    bin_tools = './baselib/eagletool/Ccode/genflashbin%s.bin'%(ver)
else:
    os.system("cp ./baselib/eagletool/Ccode/genflashbin%s.exe ./"%(ver))
    bin_tools = "genflashbin%s.exe"%(ver)

cmd = bin_tools + \
      ' ./dist/bin/tmp/eagle.app.%s.text.bin '%(subver)+ entry_addr+ \
      ' ./dist/bin/tmp/eagle.app.%s.data.bin '%(subver)+data_start_addr+ \
      ' ./dist/bin/tmp/eagle.app.%s.rodata.bin '%(subver)+rodata_start_addr
os.system(cmd)

cmd = 'mv eagle.app.flash.bin ./dist/bin/tmp/eagle.app.%s.flash.bin'%(subver)
os.system(cmd)

if not os.path.isdir("./dist/pxp"):
    os.makedirs("./dist/pxp")
cmd = 'xxd -p -c 1 ./dist/bin/tmp/eagle.app.pro.flash.bin > ./dist/pxp/bootloader_flash.bin'
os.system(cmd)
print "PXP flash bin done!"

