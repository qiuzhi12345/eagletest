from hal.Init import HALS
from baselib.loglib.log_lib import *
from baselib.loglib.log_csv import csvreport
from testcase.volumeCase.MULTIBOARD.multiboard_ctl import MultiBoardControl
import re

class XTAL_32K(object):
    def __init__(self, channel, mcu_chl, chipv = "AUTO"):
        self.mcu_chl  = mcu_chl
        self.chip     = HALS(channel, chipv)
        self.channel = self.chip.channel
        self.chipv = self.chip.chipv

    def scan_startup_time(self, touch_ls = [0,1,2,3,4], dac_ls = [0,1,2,3]):
        self.log = csvreport('/XTAL_32K/%s/32k_scan_startup_time' % time.strftime('%y_%m_%d'))
        self.log.write_value('CHIP_MAC', self.CHIP_MAC)
        for t in touch_ls:
            for d in dac_ls:
                time_str = self.channel.req_com("get_xtal_startup_time %d %d %d %d" % (t,d,3,0))
                times    = filter(str.isdigit, time_str) 
                self.log.write_value('Touch%d_dac%d' % (t,d), times)                
                self.chip.rtc_clk.start_32k(0)
                loginfo(times)
                time.sleep(1)
        self.log.flush_line()
 
    def read_32k_freq(self, delay = 10, touch = 0, dac = 1):
        log_freq = csvreport('/XTAL_32K/%s/32k_freq' % time.strftime('%y_%m_%d') )
        repeat   = 1
        col      = ['CHIP_MAC', self.CHIP_MAC]
        self.channel.req_com("get_xtal_startup_time %d %d %d %d" % (touch, dac, 3, 0))       
        while True: 
            time.sleep(delay)       
            freq    = self.chip.rtc_timer.get_clk_calibration(2)            
            val     = ['times_%d' % repeat , freq]
            repeat += 1
            log_freq.write_value(col,val)
            log_freq.flush_line()

    def ulp_multi(self, chip_list = [31,30], slp_time = 3, detect = 20, timeout = 1):
        '''
        - ulp_cp_xtal_test 1 1 3 0 0x20000
        - ulp_get_sleep_moment
        - ulp_cp_xtal_from_slp 0x20000
        - rd 0x6000804c 
                return 2 bit:
                0 init
                1 ulp_stop
                2 xtal_dead
                3 running
        - rtc_wakeup_cause
        '''
        ulp_log = csvreport('/XTAL_32K/%s/ULP_multi_%smin' % (time.strftime('%y_%m_%d'),slp_time))
        mu      = MultiBoardControl(self.mcu_chl)                        
        mac_ls  = ['chip_mac']
        for chip_slt in chip_list: 
            mu.mcu_slt(chip_slt)
            time.sleep(1)
            self.CHIP_MAC = self.chip.CHIP_ID.chip_mac()
            mac_ls.append(self.CHIP_MAC)
            self.channel.req_com("ulp_cp_xtal_test 1 1 3 0 %d" % (slp_time*60*0x6666))
        times=1
        while True:            
            val_ls = ['%d_times_%s' % (detect, times)]
            for chip_slt in chip_list:
                mu.mcu_slt(chip_slt)
                time.sleep(1)            
                ulp_state    = self.channel.req_com("rd 0x6000804c",1)
                wakeup_cause = self.channel.req_com("rtc_wakeup_cause", 1)
                info_s       = self.channel.req_com('ulp_get_sleep_moment',1)
                info         = re.sub(',','',info_s)
                logwarn(info, ulp_state, wakeup_cause)            
                if 'Dead' in info:
                    self.chip.rtc_timer.get_clk_calibration(2)
                    freq = self.chip.rtc_timer.get_clk_calibration(2)                    
                    val_ls.append('%s_F%s_ulp%s_w%s' % (info,freq,ulp_state,wakeup_cause))
                    self.channel.req_com('ulp_cp_xtal_from_slp %d' % (slp_time*60*0x6666) ,1)
                elif 'Alive' in info:                    
                    val_ls.append('%s_ulp%s_w%s' % (info,ulp_state, wakeup_cause))
                    self.channel.req_com('ulp_cp_xtal_from_slp %d' % (slp_time*60*0x6666) ,1)
                elif info == '':
                    val_ls.append('ok')                
                else:
                    val_ls.append(info)
            logwarn(freq_ls)
            ulp_log.write_value(mac_ls, val_ls)    
            ulp_log.flush_line() 
            times += 1
            time.sleep(detect)
            
    def vbg_multi(self, chip_list=[31,30], slp_time=6, step=1, timeout=1):
        '''
        Vbg:
        get_xtal_startup_time 1 1 3 0
        rtc_timer_slp_test 0x6666 0x41
                           cycle  slp_mode(b`7=1 vbg=1.5V;b`7=0 vbg=1.2V)
        '''
        vbg_log  = csvreport('/XTAL_32K/%s/Vbg_multi_%smin' % (time.strftime('%y_%m_%d'), slp_time))
        mu       = MultiBoardControl(self.mcu_chl)                        
        mac_ls   = ['chip_mac']
        error_ls = []
        # Read all chip_ls CHIPMAC
        for chip_slt in chip_list: 
            mu.mcu_slt(chip_slt)
            time.sleep(1)
            self.CHIP_MAC = self.chip.CHIP_ID.chip_mac()
            mac_ls.append(self.CHIP_MAC)
            self.channel.req_com("get_xtal_startup_time 1 1 3 0")
        # LOOP TEST           
        while True:
            freq_ls=['slp_times_%d' % slp_time] 
            # Config all chip to sleep_mode           
            for chip_slt in chip_list:
                if chip_slt in error_ls:
                    continue                  
                mu.mcu_slt(chip_slt)
                time.sleep(0.5) 
                self.channel.req_com("rtc_timer_slp_test %d 0x41" % (slp_time*0x6666), timeout)             
                loginfo('%s set:%s' % (chip_slt,slp_time))
            time.sleep(slp_time)            
            # Wait chip wakeup read freq
            for chip_slt in chip_list:  
                if chip_slt in error_ls:
                    freq_ls.append('err')           
                mu.mcu_slt(chip_slt)  
                time.sleep(0.2)                              
                self.channel.req_com("rtc_clk_cal 2 128", timeout)
                freq = self.channel.req_com("rtc_clk_cal 2 128", timeout)
                if freq == '':
                    error_ls.append(chip_slt)
                    freq_ls.append('err')
                else:
                    freq_ls.append(freq)            
            vbg_log.write_value(mac_ls, freq_ls)
            vbg_log.flush_line()            
            slp_time = slp_time*step

    def ulp_single(self, slp_time, detect = 10, timeout = 1):
        ulp_log = csvreport('/XTAL_32K/%s/ULP_single_%s' % (time.strftime('%y_%m_%d'), slp_time))
        mu      = MultiBoardControl(self.mcu_chl)
        self.channel.req_com("ulp_cp_xtal_test 1 1 3 0 %d" % (slp_time*60*0x6666))
        mac_ls  = ['chip_mac', self.CHIP_MAC]
        times   = 1
        while True:
            val_ls       = ['%d_times_%s' % (detect, times)]
            info_s       = self.channel.req_com('ulp_get_sleep_moment',1)
            ulp_state    = self.channel.req_com("rd 0x6000804c",1)
            wakeup_cause = self.channel.req_com("rtc_wakeup_cause", 1)
            info         = re.sub(',', '', info_s)
            logwarn(info)
            if 'Dead' in info:
                self.chip.rtc_timer.get_clk_calibration(2)
                freq = self.chip.rtc_timer.get_clk_calibration(2)
                self.channel.req_com('ulp_cp_xtal_from_slp %d' % (slp_time*60*0x6666) ,1)
                val_ls.append('%s_F%s_ulp%s_w%s' % (info,freq,ulp_state,wakeup_cause))
                logwarn('%s_F%s_ulp%s_w%s' % (info,freq,ulp_state,wakeup_cause))
            elif 'Alive' in info:
                val_ls.append('%s_ulp%s_w%s' % (info,ulp_state,wakeup_cause))
                self.channel.req_com('ulp_cp_xtal_from_slp %d' % (slp_time*60*0x6666) ,1)
                logwarn('%s_ulp%s_w%s' % (info,ulp_state,wakeup_cause))
            elif '' == info:
                val_ls.append('ok')            
            else:
                val_ls.append(info)
            ulp_log.write_value(mac_ls, val_ls)    
            ulp_log.flush_line()
            times += 1
            time.sleep(detect)

    def sleep_test(self,comNum=1,slp_time=37,timeout=1,opD=0,FIB=False,oldBin=True,mb=0):        
        '''
        a copy from longSlpMulti
        Vbg:
        get_xtal_startup_time 1 1 3 0
        rtc_timer_slp_test 0x6666 0x41
        Above sleep mode setup note(bit7=1 vbg=1.5V,bit7=0 vbg=1.2V)
        Set oldBin to be False if uses new fixed timer bin
        opD = 0 for normal, opD=1 for 36hours, opD=3 for 3 days, opD=6 for 6 days
        ''' 
        if mb == 0:chip_list = range(1)               
        elif mb == 1:chip_list = range(14,16)       
        elif mb == 2:chip_list = range(31)                        
        if   opD == 1: slp_time = 2190 # mins for 36 hours
        elif opD == 3: slp_time = 4370 # mins for 72 hours
        elif opD == 6: slp_time = 8800 # mins for 6 days 
        #Set touch dac level for 32K cyrstal based on chip type
        if FIB is True: touch_dac_val = 0
        else:           touch_dac_val = 1

        if mb == 0: slpTestLog  = csvreport('/XTAL_32K/sleepTest_SngB#%s_vbg1p2V_%smins' % (comNum,slp_time))
        else      : slpTestLog  = csvreport('/XTAL_32K/sleepTest_MulB#%s_vbg1p2V_%smins' % (mb,slp_time))
        # mu     = MultiBoardControl(comNum,self.mcu_chl)                        
        mu     = MultiBoardControl(comNum=comNum, mcu_chl=self.mcu_chl, chipv = self.chipv)  
        mac_ls           = ['chip_mac']
        if oldBin is False: startUp_ls = ['StartUp Freq']
        else:               startUp_ls = ['StartUp Time']
        chipNum_ls       = ['chip#']
        error_ls         = []
        noReturn_freq_ls = []
        noReturn_wk_ls   = []            
        wkFromSlp_ls     = ['WAKE UP NOW !!']        
        freq_ls          = ['Freq Read'] 
        wk_ls            = ['WakeUp Cause']
        put2slp_ls       = ['Go to bed for %dmins'%slp_time]
        saveIt_ls        = ['Try to restart 32k']
        slpCheck_ls      = ['Check if sleeps']            
        sleepCheck       = 'initial'
        #Crystal startUp function
        def startUpXtal(touch_dac_val = touch_dac_val,oldBin=oldBin): 
            if oldBin is False:
                self.channel.req_com("rtc_clk_32k_set 1 3 0",timeout)
                self.channel.req_com("rtc_clk_32k_ext_dac_set %d"%(touch_dac_val),timeout)
                self.channel.req_com("rtc_clk_32k_enable 1",timeout)
                time.sleep(1)
                for i in range(2):
                    returnVal = self.channel.req_com("rtc_clk_cal 2 128", timeout)
            else:
                returnVal = self.channel.req_com("get_xtal_startup_time 1 3 3 3",timeout)
                # returnVal = self.channel.req_com("get_xtal_startup_time 0 1 3 0",timeout)
            return returnVal

        #write data little function
        def addDataToLog(listOfData=[]):
            slpTestLog.write_value(mac_ls,listOfData)
            slpTestLog.flush_line()
            return
        #small function to put chip into sleep
        def goToSleep(opD=opD,slp_time=slp_time):                
            #Put chip into deep-sleep      
            time.sleep(0.2)  
            sleepCheck = 'initial'
            TryTimer   = 0
            for TryTimer in range(9):
                if sleepCheck == '':
                    break
                else:
                    self.channel.req_com("rtc_clk_slow_freq_set 1",timeout)
                    if opD == 0:   self.channel.req_com("slp_cnt_wakeup 0 %d"%(slp_time*60*32768),timeout)
                    elif opD == 1: self.channel.req_com("slp_cnt_wakeup 0 0xffffffff",timeout) #slp for 36 hours 
                    elif opD == 3: self.channel.req_com("slp_cnt_wakeup 1 0xffffffff",timeout) #slp for 72 hours
                    elif opD == 6: self.channel.req_com("slp_cnt_wakeup 3 0xffffffff",timeout) #slp for 6 days                        
                    #Export 32K to IO2         
                    self.channel.req_com("TOUCH_PAD2_DEBUG_CFG 0 4 0",timeout)
                    # self.channel.req_com("TOUCH_PAD0_DEBUG_CFG 0 4 0",timeout)
                    loginfo('CHIP#%s exported XTAL_32K CLK to IO2'%(chip_slt))
                    #Enter Sleep
                    #self.channel.req_com("slp_cnt_wakeup 0 0x6666666",timeout)                         
                    self.channel.req_com("rtc_sleep 0x3d 8 0",timeout)
                    loginfo('CHIP#%s Round#%s sets sleep time: %smins' % (chip_slt,TryTimer,slp_time))            
                    #check if really falls asleep         
                    for i in range(2):
                        sleepCheck=self.channel.req_com("rtc_clk_cal 2 128", timeout)
                    loginfo('CHIP#%s sleepCheck:%s'%(chip_slt,sleepCheck))
                    TryTimer = TryTimer + 1 
            #Report sleep status
            if TryTimer <= 9 and (sleepCheck == ''): 
                loginfo('CHIP#%s is sleeping' % (chip_slt))
                slpChkInfo = 'Sleeping Tried%sx'%TryTimer
            else:
                loginfo('CHIP#%s tried 10 times, wont sleep' % (chip_slt))                
                slpChkInfo = 'Tried 10x Failed'
            slpCheck_ls.append(slpChkInfo)
            put2slp_ls.append(time.asctime())
            return          
        #small funciton to check chip status if wakesup            
        def wakeUpCheck(chip_slt = 0):
            rpt_32k=0
            wkFromSlp_ls.append(time.asctime())
            #Use frequency read to check if wakeup     
            time.sleep(0.2)                    
            freq=self.channel.req_com("rtc_clk_cal 2 128", timeout)     # freq = self.chip.rtc_timer.get_clk_calibration(2)
            if freq=='':
                error_ls.append(chip_slt)
                noReturn_freq_ls.append(chip_slt)
                freq_ls.append('No return')
                loginfo('CHIP#%s reads freq: NO RETURN!!'%(chip_slt))   
            elif freq=='0':
                while freq=='0' and  rpt_32k<5:
                    logwarn('repeat read 32K freq...')
                    freq=self.channel.req_com("rtc_clk_cal 2 128", timeout)
                    rpt_32k+=1
                freq_ls.append(freq)
            else:
                freq_ls.append(freq) 
                loginfo('CHIP#%s reads freq:%s'%(chip_slt,freq))   
            #Return wakeup cause
            time.sleep(0.2)        
            wkcus=self.channel.req_com('rtc_wakeup_cause',timeout)
            if wkcus != '8':
                wk_ls.append('No return')
                loginfo('CHIP#%s wakeup_cause: No RETURN!!'%(chip_slt))
                noReturn_wk_ls.append(chip_slt)
            else:
                loginfo('CHIP#%s wakeup_cause:%s'%(chip_slt,wkcus))                 
                wk_ls.append(wkcus)
            
            if (freq =='' or freq=='0') and (wkcus != '8'):
                startUp = startUpXtal(touch_dac_val=touch_dac_val,oldBin=oldBin)
                if startUp =='':
                    tryToFix = 'SSorCD'
                    loginfo('Still Sleeping or Completely Dead!!')
                else:
                    tryToFix = startUp[:-30]
                    loginfo('Revived and startUp time is %s'%startUp[:-30])
            else:
                tryToFix = 'He is good'
            return tryToFix

        # Sleep Cycle Test Starts Here
        for chip_slt in chip_list: 
            chipNum_ls.append(chip_slt+1)
            mu.mcu_slt(chip_slt)
            time.sleep(1)
            if self.chipv=='ESP32':
                CHIP_MAC = self.chip.CHIP_ID.chip_mac()
            elif self.chipv=='CHIP722':
                CHIP_MAC = self.channel.req_com("efuse_rd_mac_hi",1)+ self.channel.req_com("efuse_rd_mac_lo",1) 
            logres(CHIP_MAC)
            mac_ls.append(CHIP_MAC)
            #StartUp 32K Xtal
            startUp = startUpXtal(touch_dac_val=touch_dac_val,oldBin=oldBin)
            startUp_ls.append(startUp[:-30])
            #Read Frequency 
            time.sleep(1)   
            freq=self.channel.req_com("rtc_clk_cal 2 128", timeout)
            freq_ls.append(freq)
            #Export Xtal 32K to IO2
            time.sleep(0.2)                
            # self.channel.req_com("TOUCH_PAD0_DEBUG_CFG 0 4 0",timeout)
            self.channel.req_com("TOUCH_PAD2_DEBUG_CFG 0 4 0",timeout)
            loginfo('Exported XTAL_32K CLK to IO2')
        logres(mac_ls)
        slpTestLog.write_value(mac_ls,startUp_ls)
        slpTestLog.flush_line()
        addDataToLog(chipNum_ls)
        addDataToLog(freq_ls)
        # Initial Sleep                     
        for chip_slt in chip_list:
            mu.mcu_slt(chip_slt)
            time.sleep(0.5) 
            goToSleep(opD=opD,slp_time=slp_time)
        addDataToLog(put2slp_ls)
        addDataToLog(slpCheck_ls)
        #Loop Test
        rpt = 1
        while True:
            logwarn('waiting...%rmins'%(slp_time+2))
            logwarn(time.localtime())
            time.sleep((slp_time+2)*60) #PYTHON wait for same sleep period and 2more minutes
            #prepare noReturn list
            noReturn_freq_ls = []
            noReturn_wk_ls   = []            
            wkFromSlp_ls     = ['WAKE UP NOW !!']        
            wk_ls            = ['WakeUp Cause_%d'%rpt]
            saveIt_ls        = ['Try to restart 32k']
            freq_ls          = ['Freq Read'] 
            put2slp_ls       = ['Go to bed for %dmins'%slp_time]        
            slpCheck_ls      = ['Check if sleeps']
            # Check Chips and put to sleep
            for chip_slt in chip_list:  
                #if chip_slt in error_ls:
                #    freq_ls.append('err')
                #choose coresponding MCU
                mu.mcu_slt(chip_slt)
                #wake up check
                time.sleep(0.2)
                tryToFix=wakeUpCheck(chip_slt)
                saveIt_ls.append(tryToFix)
                #Put chip to sleep
                time.sleep(0.2)
                goToSleep(opD=opD,slp_time=slp_time)
            if noReturn_freq_ls == [] and noReturn_wk_ls == []:
                print 'THIS CYCLE ALL GOOD'
            else:
                print 'Guys Not Wake Up Below'
                loginfo('FREQ NO RETURN CHIP:%s'%noReturn_freq_ls)
                loginfo('WAKUP NO RETURN CHIP:%s'%noReturn_wk_ls)
            addDataToLog(wkFromSlp_ls)
            addDataToLog(freq_ls)
            addDataToLog(wk_ls)
            addDataToLog(saveIt_ls)
            addDataToLog(put2slp_ls)
            addDataToLog(slpCheck_ls)
            rpt += 1
        return

    def regprint(self,touch_dac_val=1):
        mac_ls           = ['chip_mac']
        freq_ls          = ['Freq Read'] 
        startUp_ls       = ['StartUp Freq']
        regprintlog  = csvreport('/XTAL_32K/regprint')
        mac_ls.append(self.CHIP_MAC)
        #write data little function
        def addDataToLog(listOfData=[]):
            regprintlog.write_value(mac_ls,listOfData)
            regprintlog.flush_line()
            return
        #Crystal startUp function
        def startUpXtal(touch_dac_val = touch_dac_val): 
            self.channel.req_com("rtc_clk_32k_set 1 3 0",1)
            self.channel.req_com("rtc_clk_32k_ext_dac_set %d"%(touch_dac_val),1)
            self.channel.req_com("rtc_clk_32k_enable 1",1)
            time.sleep(1)
            returnVal = self.chip.rtc_clk.get_clk_calibration(2)
            return returnVal
        self.CHIP_MAC = self.chip.CHIP_ID.chip_mac()
        #StartUp 32K Xtal
        startUp = startUpXtal(touch_dac_val=touch_dac_val)
        startUp_ls.append(startUp)
        #Read Frequency            
        freq=self.channel.req_com("rtc_clk_cal 2 128", 1)
        freq_ls.append(freq)
        #Export Xtal 32K to IO2
        time.sleep(0.2)                
        # self.channel.req_com("TOUCH_PAD0_DEBUG_CFG 0 4 0",timeout)
        self.channel.req_com("TOUCH_PAD2_DEBUG_CFG 0 4 0",1)
        loginfo('Exported XTAL_32K CLK to IO2')
        regprintlog.write_value(mac_ls,startUp_ls)
        regprintlog.flush_line()
        addDataToLog(freq_ls)
        return 

    def scan_startup_MultiBoard(self, comNum, mcu_chl, chip_ls=range(28), touch_ls = range(8)):
        self.log1 = csvreport('/XTAL_32K/%s/MultiBoard/MultiBoard_32k_scan_startup_time' % time.strftime('%y_%m_%d'))
        self.log2 = csvreport('/XTAL_32K/%s/MultiBoard/MultiBoard_32k_freq' % time.strftime('%y_%m_%d'))        
        mcu  = MultiBoardControl(comNum, mcu_chl)
        for chip in chip_ls:  
            mcu.mcu_rst_module(chip)
            mcu.mcu_slt(chip)
            time.sleep(3)                  
            chipmac = self.chip.CHIP_ID.chip_mac()
            col_ls  = ['CHIP_NUM', 'CHIP_MAC']
            time_ls = ['chip_%d' % chip, chipmac]
            freq_ls = ['chip_%d' % chip, chipmac]
            for t in touch_ls:
                # raw_input('save_pic')
                mcu.mcu_rst_module(chip)
                mcu.mcu_slt(chip)
                time.sleep(3)                                   
                logwarn('touch%d test...' % t)
                Freq_0   = self.channel.req_com('rtc_clk_cal 2 128', 1)                
                try:
                    while int(Freq_0)!=0:
                        self.channel.req_com('rtc_clk_32k_enable 0', 1)
                        logres(Freq_0, 'Xtal Close Failed')
                        Freq_0 = self.channel.req_com('rtc_clk_cal 2 128', 1)                        
                except:                     
                    if Freq_0 == '':
                        logwarn('NO Freq') 
                else:
                    if int(Freq_0)==0:
                        logwarn('Xtal Close Success')
                self.chip.rtc_debug.TOUCH_PAD0(0,4,0)
                self.chip.gpio.rtc_gpio_out(7,1)
                time_str = self.channel.req_com("get_xtal_startup_time %d 1 3 0" % t, 10)
                times    = filter(str.isdigit, time_str) 
                print 'Delay: 10s..'
                time.sleep(10)
                Freq     = self.channel.req_com('rtc_clk_cal 2 128', 1)
                self.chip.gpio.rtc_gpio_out(7,0)
                self.channel.req_com('rtc_clk_32k_enable 0', 1)
                col_ls.append('touch_%d' % t)
                time_ls.append(times)
                freq_ls.append(Freq)
                loginfo('touch:%r, Freq_0:%r, costtime:%r, Freq:%r' % (t, Freq_0, time_str, Freq))
            self.log1.write_value(col_ls,time_ls)
            self.log2.write_value(col_ls,freq_ls)                                                
        self.log1.flush_line()
        self.log2.flush_line()
