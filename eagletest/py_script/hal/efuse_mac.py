import csv
import os
import math
import time
class EFUSE_MAC(object):
  
  def __init__(self, channel, chipv = "ESP32"):
    self.chipv = chipv
    self.channel = channel

  def efuse_get_8m_freq(self):                  # this func return a dec data, like 799, 800, 803.
    # print 'efuse_get_8m_freq func is running.'
    return self.channel.req_com("efuse_get_8m_freq")
    # return 800

  def efuse_init(self, clk_freq):               # this func initial the configuration of eFuse 
    # print 'clk_freq %d'%clk_freq
    return self.channel.req_com("efuse_init %d"%clk_freq)

  def efuse_mac_8m(self, mac_H, mac_L, clk_8m): # this func burn MAC and 8m_clk data to eFuse
    # print 'mac_H: 0x%x, mac_L: 0x%x, clk_8m: %d'%(mac_H, mac_L, clk_8m)
    return self.channel.req_com("efuse_mac_8m 0x%x 0x%x %d"%(mac_H, mac_L, clk_8m))

  def efuse_8m_check(self):
      clk_8m_str = self.efuse_get_8m_freq()
      print 'clk_8m_str is %s'%clk_8m_str
      clk_8m = int(clk_8m_str)
      print 'clk_8m_int is %d'%clk_8m

  def efuse_burn_key6(self): 
    return self.channel.req_com("efuse_burn_key6")

  def efuse_wr_type(self, pre_type):            # this func burn the type of the chip to eFuse
    # print 'efuse_wr_type func is running. The type is %d'%pre_type
    return self.channel.req_com("efuse_wr_type %d"%pre_type)

  def efuse_read_cmd(self):                     # this func open the read access of eFuse to user
    # print "efuse_read_cmd_print func is running."
    return self.channel.req_com("efuse_read_cmd")

  def a_to_A(self, char):
    if len(char)>1:
      return '0'
    elif char>='a' and char<='z':
      return chr(ord(char)-ord('a')+ord('A'))
    elif char>='A' and char<='Z':
      return char
    else:
      return '0'

  def check_err0(self):
    self.efuse_init(80)
    self.efuse_read_cmd()
    self.efuse_rd_addr(101)
    self.efuse_check_data()

  def efuse_rd_addr(self, offset):
    rd_data = self.channel.req_com("efuse_rd_addr %d"%offset)
    print 'the Reg Data is %s '%rd_data
    return rd_data

  def efuse_wr_key6(self):
    self.efuse_init(80)
    self.efuse_read_cmd()
    pre_rd_key6 = self.efuse_rd_addr(87)
    if pre_rd_key6 != '0':
      print '!!!!!! this chip has been burned !!!!!'
      self.efuse_rd_key6_value()
      return 0
    rd_mac = self.efuse_rd_mac_hi() + self.efuse_rd_mac_lo()
    rd_8m  = self.efuse_rd_8m()
    rd_type= self.efuse_rd_type()
    self.efuse_burn_key6()
    self.efuse_read_cmd()
    result_key6 = self.channel.req_com("efuse_pgm_key6_report")
    rs_err0=self.efuse_rd_addr(101)
    rs_err1=self.efuse_rd_addr(102)
    if result_key6 != '0': print '!!Data of Key6 is Wrong!!'
    self.efuse_rd_key6_value()
    with open('./ygy_efuse/key6_report.csv','a') as f_key6:
      csv_handle = csv.writer(f_key6)
      csv_handle.writerow([rd_mac,rd_8m,rd_type,result_key6,rs_err0,rs_err1])
    

  def efuse_rd_key6_value(self):
    word0 = self.channel.req_com("efuse_rd_addr %d"%(87+0))
    word1 = self.channel.req_com("efuse_rd_addr %d"%(87+1))
    word2 = self.channel.req_com("efuse_rd_addr %d"%(87+2))
    word3 = self.channel.req_com("efuse_rd_addr %d"%(87+3))
    word4 = self.channel.req_com("efuse_rd_addr %d"%(87+4))
    word5 = self.channel.req_com("efuse_rd_addr %d"%(87+5))
    word6 = self.channel.req_com("efuse_rd_addr %d"%(87+6))
    word7 = self.channel.req_com("efuse_rd_addr %d"%(87+7))
    print ' KEY6_0: %s  \n  KEY6_1: %s  \n  KEY6_2: %s  \n  KEY6_3: %s  \n  KEY6_4: %s  \n  KEY6_5: %s  \n  KEY6_6: %s  \n  KEY6_7: %s  \n'%(word0,word1,word2,word3,word4,word5,word6,word7)

  def efuse_rd_8m(self):
    return self.channel.req_com("efuse_rd_8m")

  def efuse_rd_type(self):
    return self.channel.req_com("efuse_rd_type")    

  def efuse_rd_mac_hi(self):
    return self.channel.req_com("efuse_rd_mac_hi")

  def efuse_rd_mac_lo(self):
    return self.channel.req_com("efuse_rd_mac_lo")

  def efuse_check_data(self):
    rd_mac = self.efuse_rd_mac_hi() + self.efuse_rd_mac_lo()
    # rd_8m  = self.efuse_rd_8m()
    # rd_type= self.efuse_rd_type()
    # print ' MAC:      %s   \n clk_8m:     %s  \n type:      %s'%(rd_mac, rd_8m, rd_type)
    # return rd_mac, rd_type, rd_8m
    print ' MAC:      %s'%rd_mac
    return rd_mac

  def efuse_wr_data(self, file_path = './ygy_efuse/mac_info_722.csv', interActive = False, chipVer = 'B'):
    '''

    :note: no longer recording CLK8M & CHIP_VER into efuse any more, staring from CHIP723
    '''
    #while True:  
      # csv_name = raw_input('Enter the name of CSV file:')
      # if os.path.exists(csv_name):
      #   break;
      # else:
      #   print 'Please check the path and spelling.'
    # csv_name = './ygy_efuse/mac_info_722.csv'
    csv_name = file_path
    csv_report_name  =   csv_name[:-4] + '_report' + csv_name[-4:]
    csv_report_error =   csv_name[:-4] + '_error' + csv_name[-4:]
    #----------- check whether the chip has burned -------------------------
    self.efuse_init(80)
    self.efuse_read_cmd()
    pre_rd_mac = self.efuse_rd_mac_hi()
    pre_rd_mac += self.efuse_rd_mac_lo()
    # pre_rd_mac += ','+self.efuse_rd_8m()
    # if pre_rd_mac != '00,0':
    if pre_rd_mac != '00':
      print '!!!!!! this chip has been burned !!!!! %s' % pre_rd_mac
      return 0
    #----------- Extract data from CSV -------------------------------------
    csv_data  =   open(csv_name,'r')    # Read the datas from the CSV file
    csv_rows  =   csv_data.readlines()
    csv_data.close()
    #----------- MAIN process ----------------------------------------------
    mac_byte = [0]*6          # change mac data to byte format
    csv_row_data = [0]*3      # each row has 3 items
    for csv_row in csv_rows[1:]:
      have_burn = 0
      csv_row   = csv_row[:-1]    # delete the '\n' in the end
      csv_row_data  = csv_row.split(",")
      chip_num  = csv_row_data[0]       # the number of the MAC
      mac       = csv_row_data[1]       # data format: 01:02:03:04:05:06. The left is the lowest level.
      pre_type  = csv_row_data[2]       # preset chip type
      #----------- Find the current MAC addr ------------
      with open(csv_report_name,'r') as cc:
        lines = csv.reader(cc)
        for line in lines:
          if line[0]==chip_num:
            have_burn = 1
            break
      if have_burn==1:
        continue

      for i in range(len(mac_byte)):
        mac_byte[i] = int(mac[(2*i):(2*i+2)], 16)
      mac_H = mac_byte[0]/16<<12 | mac_byte[0]%16<<8 | mac_byte[1]/16<<4 | mac_byte[1]%16
      mac_L = mac_byte[2]/16<<28 | mac_byte[2]%16<<24 | mac_byte[3]/16<<20 | mac_byte[3]%16<<16 | mac_byte[4]/16<<12 | mac_byte[4]%16<<8 | mac_byte[5]/16<<4 | mac_byte[5]%16
      #------------ Get 8m clk --------------------
      # clk_8m_str = self.efuse_get_8m_freq()
      # clk_8m = int(clk_8m_str)
      clk_8m = 0 #no longer recrod 8M CLK into efuses
      #------------ Ensure MAC and 8M data -----------
      print 'the MAC data is  0x%x'%(mac_H<<32|mac_L)
      # print 'the clk_8m is    %d'%clk_8m 
      # check = raw_input("Are the above datas right?(y or n):")
      if interActive: check = raw_input("Are the above datas right?(y or n):")
      else: check = 'Y' 
      if check=='Y' or check=='y':
        self.efuse_mac_8m(mac_H, mac_L, clk_8m)
      else:
        print 'Task ends. Please check MAC file!!!!!'
        return 1
      #-------------- Ensure MAC Type --------------------------------
      # type_in = raw_input("Input the type('a'or'b'):")
      # if interActive: type_in = raw_input("Input the type('a'or'b'):")
      # else: type_in = chipVer
      # type_in = self.a_to_A(type_in)
      # while True:
      #   if type_in=='A' and pre_type=='A':
      #     self.efuse_wr_type(1)
      #     break
      #   elif type_in=='B' and pre_type=='B':
      #     self.efuse_wr_type(0)
      #     break
      #   else:
      #     print '!!!!The type is different from that in CSV!!!!'
      #     type_in = raw_input("!!!Please ensure and re-enter the type:")
      #     type_in = raw_input("!!!Please ensure and re-enter the type:")
      #     type_in = self.a_to_A(type_in)
      #     if type_in=='A':
      #       self.efuse_wr_type(1)
      #       break
      #     elif type_in=='B':
      #       self.efuse_wr_type(0)
      #       break
      #---------------- record error message -------------------------
      self.efuse_read_cmd()
      rs_err0=self.efuse_rd_addr(101)
      rd_mac_byte = [0]*6
      rd_mac = self.efuse_rd_mac_hi() + self.efuse_rd_mac_lo()
      for i in range(len(rd_mac_byte)):
        rd_mac_byte[i] = int(rd_mac[(2*i):(2*i+2)], 16)
      rd_mac_H = rd_mac_byte[0]/16<<12 | rd_mac_byte[0]%16<<8 | rd_mac_byte[1]/16<<4 | rd_mac_byte[1]%16
      rd_mac_L = rd_mac_byte[2]/16<<28 | rd_mac_byte[2]%16<<24 | rd_mac_byte[3]/16<<20 | rd_mac_byte[3]%16<<16 | rd_mac_byte[4]/16<<12 | rd_mac_byte[4]%16<<8 | rd_mac_byte[5]/16<<4 | rd_mac_byte[5]%16
      # rd_8m  = self.efuse_rd_8m()
      # rd_type= self.efuse_rd_type()
      # if rd_type=='1':
      #     rd_type_char='A'
      # else:
      #     rd_type_char='B'
      # if (mac_H!=rd_mac_H) or (mac_L!=rd_mac_L) or (clk_8m!=int(rd_8m)) or (type_in!=rd_type_char):
      if (mac_H!=rd_mac_H) or (mac_L!=rd_mac_L): 
        print '!!Data of MAC is WRONG!!'
        with open(csv_report_error,'a') as f2:
          csv_handle = csv.writer(f2)
          # csv_handle.writerow([mac,rd_mac,clk_8m_str,rd_8m,type_in,rd_type_char,rs_err0])
          csv_handle.writerow([mac,rd_mac,rs_err0])
      #---------------- record burning message ----------------------- 
      with open(csv_report_name,'a') as ff:
        csv_handle = csv.writer(ff)        # need import csv
        # csv_handle.writerow([chip_num, mac, clk_8m_str, type_in, rs_err0])
        csv_handle.writerow([chip_num, mac, rs_err0])
      print ''
      self.efuse_read_cmd()
      rd_mac = self.efuse_check_data()
      # return [mac, type_in, clk_8m]
      return [rd_mac]
      # os._exit(0)

