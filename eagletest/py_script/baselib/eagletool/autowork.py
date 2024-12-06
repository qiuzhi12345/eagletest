#!/usr/bin/env python
import sys
import os
import serial
import re
import time
import platform
import hashlib
from baselib.test_channel import *
import shutil
from baselib.loglib.log_lib import *
from hal.gpio import *
# from baselib.tc_platform.common import Multiboard_CTL
from baselib.test_channel.com import COM


class MboardController():
    def __init__(self, ComPort):
        self.gpio = GPIO(COM(ComPort))
        self.Mctrl = Multiboard_CTL(COM(ComPort))
        self.Bnum = 0
    def Mboard_reset(self):
        self.gpio.dig_gpio_out(5,0)
        time.sleep(2)
        self.gpio.dig_gpio_out(5,1)
        logdebug("%d board reset .."%self.Bnum)
    def Mboard_sel(self, num):
        self.Mctrl.mcu_sel(num)
        self.Bnum = num
    # def deinit(self):
    #     self.ComC.close()


class eagle_download_tool_class(object):
    """docstring for eagle_download_tool"""
    def __init__(self, channel = "", chipv = ""):
        self.channel = channel
        self.chipv = chipv
        if chipv == "ESP32":
            self.xcc = "xtensa-esp32-elf"
        elif chipv in ("FPGA722", "CHIP722", "FPGA723", "CHIP723"):
            self.xcc = "xtensa-lx7-elf"
        elif chipv == "ESP8266":
            self.xcc = "xtensa-lx106-elf"
        else:
            logerror("unkwown chip")
        self.cpu = 'pro'
        self.bin_path = "./dist/bin"
        self.bin_name = "eagle.app.%s.flash.bin"%self.cpu
        self.out_name = "eagle.app.%s.out"%self.cpu
        self.bin_gen_path = "./dist/bin/tmp"
        self.esptool_path = './baselib/eagletool'
        self.OUT_PATH = ""

        self.Mboard_mode = "NBM"
        self.Mboard_com_num = 0
        self.Mboard_map = ""
        self.Download_speed = "115200"
        self.Download_SPI_mode = "dio"
        self.FLASH_DOWNLOAD_FILE_TMP_FULL = self.bin_path + "/.eagle.app.pro.flash_tmp.bin"
        self.Download_mode = "FLASH"
        self.AGVS  = ""


    def para_path_detect(self):
        if platform.platform().find("Linux") != -1:
            path_hit_flag = 0
            for i in range(1000,1010):
                out_path_out = "/run/user/%d/gvfs/smb-share:server=192.168.0.107,share=phy_group"%i
                # print out_path_out
                if os.path.exists(out_path_out):
                    self.OUT_PATH = out_path_out
                    path_hit_flag = 1
                    print "detect phy_group at \"%s\""%self.OUT_PATH
                    break
            if path_hit_flag == 0:
                print "please make sure phy_group folder is exist"
                return False
        else:
            self.OUT_PATH = "z:"
        return True

    def para_revert(self):
        if self.chipv in ("FPGA722", "CHIP722", "FPGA723", "CHIP723"):
            args0 = " --no-stub --chip esp32c "
            ESPTOOL = "python ./baselib/eagletool/esptool.py"
            init_addr = "0x1000"
        elif self.chipv == "CHIP72":
            args0 = " --no-stub "
            ESPTOOL = "python -m esptool"
            init_addr = "0x1000"
        elif self.chipv == "ESP8266":
            args0 = " --no-stub "
            ESPTOOL = "python -m esptool"
            init_addr = "0x0"
        else:
            args0 = ""
            ESPTOOL = "python -m esptool"
            init_addr = "0x1000"
        if self.Download_mode == "FLASH":
            self.DOWNLOAD_CMD = ESPTOOL + " " + self.AGVS + args0 +" -b "+ self.Download_speed  + \
                            " -p " + "%s" + \
                            " write_flash --flash_mode " + self.Download_SPI_mode + \
                            " --flash_fre 20m " + init_addr + \
                            " " + self.FLASH_DOWNLOAD_FILE_TMP_FULL
        else:
            self.DOWNLOAD_CMD = ESPTOOL + " " + self.AGVS + args0 + " -b " + self.Download_speed  + \
                            " -p " + "%s" + \
                            " load_ram " + self.FLASH_DOWNLOAD_FILE_TMP_FULL


    def md5_calc(self, file_name):
        m = hashlib.md5()
        fid = open(file_name, 'rb')
        m.update(fid.read())
        fid.close()
        return m.hexdigest()

    def list_out_dir(self, user_path):
        try:
            dir_list = os.listdir(user_path)
        except:
            dir_list = ["0000-00-00_000000"]

    ##        print dir_list
        new_list = []
        for dir_name in dir_list:
            res = re.search("(\d\d\d\d)\-(\d\d)\-(\d\d)\_(\d\d\d\d\d\d)", dir_name)
            if res != None:
                new_list.append(int("%s%s%s%s"%(res.group(1), res.group(2), res.group(3), res.group(4))))
        new_list.sort()
        return new_list

    def print_out_list(self, num, user_path):
        file_dict = dict()
        new_list = self.list_out_dir(user_path)
        # print new_list
        if num > len(new_list):
            num = len(new_list)
        for index, sublist in enumerate(new_list):
            if index == num:
                break
            sublist = str(new_list[-1-index])[0:4]+'-'+str(new_list[-1-index])[4:6]+'-'+str(new_list[-1-index])[6:8]+'_'+str(new_list[-1-index])[8:14]
            print "%3d : %s"%(0-index, sublist)
            file_dict[0-index] = str(new_list[-1-index])
        return file_dict


    def print_bin_list(self):
        file_dict = dict()
        file_list = os.listdir(self.bin_path)
        new_bin_list = []
        for fil in file_list:
            if fil.find(".bin") != -1 and fil[0] != '.':
                new_bin_list.append(fil)
        for index, sublist in enumerate(new_bin_list):
            print "%3d : %s"%(0-index, sublist)
            file_dict[0-index] = str(sublist)
        return file_dict

    def history(self, cmd=0, new_dir = ""):
        if cmd == 0:
            if  os.path.exists(self.tmp_file):
                fid = open(self.tmp_file,'r')
                last_dir = int(fid.readline().strip("\n\r "))
                last_md5 = fid.readline().strip("\n\r ")
                fid.close()
            else:
                last_dir = 0
                last_md5 = ""
            return last_dir, last_md5
        elif new_dir != "":
            fid = open(self.tmp_file,'w')
            fid.write("%s\n"%new_dir)
            md5sum = self.md5_calc(self.bin_path + '/' + self.bin_name)
            fid.write("%s\n"%md5sum)
            fid.close()

    def show_inprogress(self, stime = 1):
        step = stime/3.
        sys.stdout.write("*")
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("*")
        sys.stdout.flush()
        time.sleep(step)
        sys.stdout.write("*")
        sys.stdout.flush()
        time.sleep(step)
        sys.stdout.write("\b\b\b   \b\b\b")
        sys.stdout.flush()

    def flow(self, user_name, user_path, new, new_bin):
        print new_bin
        if new_bin == "":
            # get history
            print "*** get history"
            last_dir, last_md5 = self.history(0)

            # get file
            print "*** get file"
            gen_flash_bin_flag = 1
            if new == "new":
                new_dir = self.fetch_new_file(user_path, last_dir)
            elif new == str(last_dir):
                new_dir = new
                if os.path.exists(self.bin_path+'/'+self.bin_name):
                    md5sum = self.md5_calc(self.bin_path+'/'+self.bin_name)
                    if last_md5 == md5sum:
                        print "*** ignore gen flash bin"
                        gen_flash_bin_flag = 0
            else:
                new_dir = new


            ## gen flash bin
            if gen_flash_bin_flag == 1:
                self.gen_flash_bin(new_dir, user_name, user_path)

            ## write history
            print "*** write history"
            self.history(1, new_dir)
        ## write flash
        print "*** write flash"
        return self.write_flash(new_bin)

    def fetch_new_file(self, user_path, last_dir):
        print "wait new file .",
        while True:
            new_list = self.list_out_dir(user_path)
            if new_list[-1] > last_dir:
                new_dir =str(new_list[-1])
                print ""
                break
            self.show_inprogress(1)
        print ""
        return new_dir
    def gen_flash_bin(self, new_dir, user_name, user_path):
        print "*** gen flash bin"
        new_dir_s = new_dir[0:4]+'-'+new_dir[4:6]+"-"+new_dir[6:8]+"_"+new_dir[8:14]
        time.sleep(2)
        print "****new file dir is %s"%new_dir_s
        out_file = user_path+"/"+new_dir_s+"/image/" + self.out_name    
        self.gen_misc(out_file)


    def gen_misc(self, out_file):
        if os.path.exists(self.bin_path + "/"+ self.bin_name):
            os.remove(self.bin_path + "/"+ self.bin_name)
        if os.path.exists(self.bin_gen_path+"/"+self.out_name):
            os.remove(self.bin_gen_path+"/"+self.out_name)


        if not os.path.exists(out_file):
            return
        if platform.platform().find("Linux") != -1:
            loginfo("ln -s %s %s"%(out_file, self.bin_gen_path+"/"+self.out_name))
            os.system("ln -s %s %s"%(out_file, self.bin_gen_path+"/"+self.out_name))
        else:
            loginfo("cp %s %s"%(out_file, self.bin_gen_path+"/"+self.out_name))
            shutil.copyfile(out_file, self.bin_gen_path+"/"+self.out_name)

        if self.chipv == "ESP8266":
            os.system(self.xcc + "-objdump -x -s %s/eagle.app.%s.out > %s/eagle.app.%s.dump"%(self.bin_gen_path,self.cpu,self.bin_gen_path,self.cpu))
            os.system(self.xcc + "-objdump -S %s/eagle.app.%s.out > %s/eagle.app.%s_S"%(self.bin_gen_path,self.cpu,self.bin_gen_path,self.cpu))
            os.system(self.xcc + "-objcopy -S -g -O binary %s/eagle.app.%s.out %s/eagle.app.%s.bin"%(self.bin_gen_path,self.cpu,self.bin_gen_path,self.cpu))
            os.system(self.xcc + "-objcopy -S -g -O srec %s/eagle.app.%s.out %s/eagle.app.%s.srec"%(self.bin_gen_path,self.cpu,self.bin_gen_path,self.cpu))
            os.system(self.xcc + "-objcopy -j .text %s/eagle.app.%s.out %s/eagle.app.%s.text.out"%(self.bin_gen_path,self.cpu,self.bin_gen_path,self.cpu))
            os.system(self.xcc + "-objcopy -S -g -O binary %s/eagle.app.%s.text.out %s/eagle.app.%s.text.bin"%(self.bin_gen_path,self.cpu,self.bin_gen_path,self.cpu))
            os.system(self.xcc + "-objcopy -j .data %s/eagle.app.%s.out %s/eagle.app.%s.data.out"%(self.bin_gen_path,self.cpu,self.bin_gen_path,self.cpu))
            os.system(self.xcc + "-objcopy -S -g -O binary %s/eagle.app.%s.data.out %s/eagle.app.%s.data.bin"%(self.bin_gen_path,self.cpu,self.bin_gen_path,self.cpu))
            os.system(self.xcc + "-objcopy -j .rodata %s/eagle.app.%s.out %s/eagle.app.%s.rodata.out"%(self.bin_gen_path,self.cpu,self.bin_gen_path,self.cpu))
            os.system(self.xcc + "-objcopy -S -g -O binary %s/eagle.app.%s.rodata.out %s/eagle.app.%s.rodata.bin"%(self.bin_gen_path,self.cpu,self.bin_gen_path,self.cpu))
            os.system("python %s/gen_appbin_8266.py %s/%s 8266 %s %s"%(self.esptool_path, self.bin_gen_path, self.out_name, self.cpu, self.xcc))
        else:
            os.system(self.xcc + "-objdump -x -s %s/eagle.app.%s.out > %s/eagle.app.%s.dump"%(self.bin_gen_path,self.cpu,self.bin_gen_path,self.cpu))
            os.system(self.xcc + "-objdump -S %s/eagle.app.%s.out > %s/eagle.app.%s_S"%(self.bin_gen_path,self.cpu,self.bin_gen_path,self.cpu))
            os.system(self.xcc + "-objcopy -S -g -O binary %s/eagle.app.%s.out %s/eagle.app.%s.bin"%(self.bin_gen_path,self.cpu,self.bin_gen_path,self.cpu))
            os.system(self.xcc + "-objcopy -S -g -O srec %s/eagle.app.%s.out %s/eagle.app.%s.srec"%(self.bin_gen_path,self.cpu,self.bin_gen_path,self.cpu))
            os.system(self.xcc + "-objcopy -j .text %s/eagle.app.%s.out %s/eagle.app.%s.text.out"%(self.bin_gen_path,self.cpu,self.bin_gen_path,self.cpu))
            os.system(self.xcc + "-objcopy -S -g -O binary %s/eagle.app.%s.text.out %s/eagle.app.%s.text.bin"%(self.bin_gen_path,self.cpu,self.bin_gen_path,self.cpu))
            os.system(self.xcc + "-objcopy -j .data %s/eagle.app.%s.out %s/eagle.app.%s.data.out"%(self.bin_gen_path,self.cpu,self.bin_gen_path,self.cpu))
            os.system(self.xcc + "-objcopy -S -g -O binary %s/eagle.app.%s.data.out %s/eagle.app.%s.data.bin"%(self.bin_gen_path,self.cpu,self.bin_gen_path,self.cpu))
            os.system(self.xcc + "-objcopy -j .rodata %s/eagle.app.%s.out %s/eagle.app.%s.rodata.out"%(self.bin_gen_path,self.cpu,self.bin_gen_path,self.cpu))
            os.system(self.xcc + "-objcopy -S -g -O binary %s/eagle.app.%s.rodata.out %s/eagle.app.%s.rodata.bin"%(self.bin_gen_path,self.cpu,self.bin_gen_path,self.cpu))
            os.system(self.xcc + "-objcopy -j .irom0.text %s/eagle.app.%s.out %s/eagle.app.%s.irom0text.out"%(self.bin_gen_path,self.cpu,self.bin_gen_path,self.cpu))
            os.system(self.xcc + "-objcopy -S -g -O binary %s/eagle.app.%s.irom0text.out %s/eagle.app.%s.irom0text.bin"%(self.bin_gen_path,self.cpu,self.bin_gen_path,self.cpu))
            os.system(self.xcc + "-objcopy -j .irom1.text %s/eagle.app.%s.out %s/eagle.app.%s.irom1text.out"%(self.bin_gen_path,self.cpu,self.bin_gen_path,self.cpu))
            os.system(self.xcc + "-objcopy -S -g -O binary %s/eagle.app.%s.irom1text.out %s/eagle.app.%s.irom1text.bin"%(self.bin_gen_path,self.cpu,self.bin_gen_path,self.cpu))
            os.system("python %s/gen_appbin.py %s/%s v7 %s %s"%(self.esptool_path, self.bin_gen_path, self.out_name, self.cpu, self.xcc))
        if os.path.exists(self.bin_gen_path + "/" + "eagle.app." + self.cpu + ".irom0text.bin"):
            shutil.copyfile(self.bin_gen_path + "/" + "eagle.app." + self.cpu + ".irom0text.bin"   , self.bin_path + "/" + "eagle.app." + self.cpu + ".irom0text.bin")
        if os.path.exists(self.bin_gen_path + "/" + "eagle.app." + self.cpu + ".irom1text.bin"):
            shutil.copyfile(self.bin_gen_path + "/" + "eagle.app." + self.cpu + ".irom1text.bin"   , self.bin_path + "/" + "eagle.app." + self.cpu + ".irom1text.bin")
        shutil.copyfile(self.bin_gen_path + "/" + "eagle.app." + self.cpu + ".flash.bin"       , self.bin_path + "/" + "eagle.app." + self.cpu + ".flash.bin")
        shutil.copyfile(self.bin_gen_path + "/" + "eagle.app." + self.cpu + "_S"               , self.bin_path + "/" + "eagle.app." + self.cpu + "_S")

    def write_flash(self, my_bin_name):
        print "Download mode %s"%self.Mboard_mode
        if my_bin_name != "":
            write_bin_name_n = self.bin_path + "/" + my_bin_name
        else:
            write_bin_name_n = self.bin_path + "/" + self.bin_name

        if os.path.exists(write_bin_name_n):
            print write_bin_name_n
            print self.FLASH_DOWNLOAD_FILE_TMP_FULL
            shutil.copy(write_bin_name_n, self.FLASH_DOWNLOAD_FILE_TMP_FULL)
        else:
            print "*** file %s is not exsit!!!"%write_bin_name_n

        if self.Mboard_mode == "NBM":
            channel_st = self.channel.isopen == True
            if channel_st:
                self.channel.deinit()
            loginfo(self.DOWNLOAD_CMD%self.channel.ComPort)
            res = os.system(self.DOWNLOAD_CMD%self.channel.ComPort)
            if channel_st:
                self.channel.open()
            if res >> 8 == 2:
                logerror("")
                logerror("download fail")
                return False
        elif self.Mboard_mode == "MBM":
            print self.Mboard_map
            MC = MboardController(self.Mboard_com_num)
            board_map = eval(self.Mboard_map)
            suc_map=[]
            fail_map=[]
            for board in board_map:
                MC.Mboard_sel(board)
                MC.Mboard_reset()
                time.sleep(2)
                channel_st = self.channel.isopen == True
                if channel_st:
                    self.channel.deinit()
                loginfo(self.DOWNLOAD_CMD%self.channel.ComPort)
                res = os.system(self.DOWNLOAD_CMD%self.channel.ComPort)
                if channel_st:
                    self.channel.open()
                if res >> 8 == 2:
                    fail_map.append(board)
                    logerror("")
                    logerror("download fail")
                else:
                    suc_map.append(board)
                logdebug("Suc board:")
                logdebug(suc_map)
                logdebug("Fail board:")
                logdebug(fail_map)
            # MC.deinit()
        print time.asctime()
        return True


    def parse(self, str_in):
        match_str = "(\w+)" + "\s*" + "(" + "\w*" + ")"
        res = re.search(match_str, str_in)
        if res:
            return True, res.group(1), res.group(2)
        else:
            return False, False, False

    def eagle_download(self, com_num = "", user_name = "gusd", args = "", Imode = True, bin_file = "esp32_test.bin"):
        '''
        :com_num:
            com port number
        :Imode:
            Interactive mode enable
        :bin_file:
            select bin file, only used not at Interactive mode
        :user_name:
            At Interactive mode, it used for point .out file name
        :args:
            Download paramter
            for CHIP72, plese use "-- no-stub"
        '''
        if com_num != "":
            self.channel = COM(ComPort = com_num, initopen = False)
            print self.channel.ComPort

        self.AGVS = args
        self.tmp_file = "./log/download_tool_tmp_%s.txt"%user_name
        user_path = ""
        print "** ", platform.platform()
        if not Imode:
            self.para_revert()
            return self.flow(user_name, "", "", bin_file)

        file_out_dict = dict()
        file_bin_dict = dict()
        exc_flag = 0
        new_out = ""
        new_bin = ""
        while True:
            print "*** Download mode: %s | %s | %s, type \"help\" for more"%(self.Mboard_mode, self.Download_mode, self.Download_speed)
            a = raw_input("please enter:")

            res, key, value = self.parse(a)
            if res:
                if key == "q":
                    print "quit"
                    break
                if key == "help":
                    print "="*10
                    print "\"enter\": use newset outfile"
                    print "lo: list outfiles"
                    print "lb: list exsiting bin"
                    print "BoardMode NMB: change to NMB mode"
                    print "NMB MBM"
                    print "DownloadMode RAM: change to RAM mode"
                    print "FLASH RAM"
                    print "DownloadSpeed 230400: change downloadspeed(Uart) to 230400"
                    print "="*10
                    continue
                # set work mode
                if key == "BoardMode":
                    self.Mboard_mode = value
                    if self.Mboard_mode =="MBM":
                        print "Mboard mode start"
                        self.Mboard_com_num = int(raw_input("please input MCU com num:"))
                        self.Mboard_map = raw_input("please input download map( e.g: [1,2] ):")
                    continue
                if key == "DownloadMode":
                    if value == "":
                        print "Download_mode: %s"%self.Download_mode
                    else:
                        print "Download to %s"%value
                        self.Download_mode = "RAM"
                    continue
                if key == "DownloadSpeed":
                    if value == "":
                        print "DownloadSpeed: %s"%self.Download_speed
                    else:
                        print "Download to %s"%value
                        self.Download_speed = value
                    continue

            # chose download files
            if a == 'lo':
                print "*** please chose out file:"
                if not self.para_path_detect():
                    break
                user_path = "%s/%s"%(self.OUT_PATH, user_name)
                file_out_dict = self.print_out_list(10, user_path)
                exc_flag = 1
                continue
            if a == "lb":
                print "*** please chose bin file:"
                file_bin_dict = self.print_bin_list()
                exc_flag = 2
                continue

            # excute para
            if a == '':
                new_out = "new"
                print "use out newest"
            elif int(a) <= 0:
                if exc_flag == 1:
                    new_out = file_out_dict[int(a)]
                    new_bin = ""
                    print "*** use out: %s(%s)"%(new_out, a)
                elif exc_flag == 2:
                    new_out = ""
                    new_bin = file_bin_dict[int(a)]
                    print "*** use bin: %s(%s)"%(new_bin,a)
                else:
                    print "*** Please lo or lb first!!"
                    continue
            else:
                print "type \"help\" for more"
                continue

            # run
            self.para_revert()
            self.flow(user_name, user_path, new_out, new_bin)



def eagle_download_tool(com_num = "", user_name = "gusd", chipv = "ESP32", args = "", Imode = True, bin_file = "esp32_test.bin"):
    u = eagle_download_tool_class(chipv = chipv)
    u.eagle_download(com_num, user_name , args, Imode, bin_file)

