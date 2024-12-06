from baselib.test_channel.com import COM as com
from baselib.loglib.log_lib import *
from baselib.loglib.log_csv import *
from maclib.mac_common import *
from hal.common import CHIP_INFO
from hal.rtc_sleep import *
from hal.rtc_timer import *
from hal.rtc_clock import *
import time
import random
import pandas as pd
import matplotlib.pyplot as plt
import re

class WIFIMAC_TC_FUNC(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.mac = mac_common(self.channel, self.chipv)
        self.wifimac = self.mac.wifimac



    def tc_tx2ap(self,
                        rate = RATE_TAB['LG_6M'].value, 
                        sgi = 0,
                        cwb = 0,
                        length= 100,
                        burst_num = 10,
                        rfchannel=6,
                        rfmode = 0,
                        ap_addr = 0x8098f02cb71c):

        self.mac.mac_txrx_init(rfchannel, rfmode)
        self.mac.mac_txrx_init(rfchannel, rfmode)

        self.mac.wifimac.mac_txpacket_rand()
        txlink = self.mac.set_tx_packet(ap_addr, rate, sgi, cwb, length)
        txpmd = self.mac.wifimac.mac_tx_start(burst_num, 1)
        tx_suc_cnt = self.mac.wifimac.get_tx_cnt(1)
        loginfo("tx suc:", tx_suc_cnt, "/", burst_num)

    def tc_rxtx_dump(self, inst_channel,
                        csi = True,
                        rate = RATE_TAB['LG_6M'].value, 
                        sgi = 0,
                        cwb = 0,
                        length= 100,
                        burst_num = 10,
                        rfchannel=6,
                        rfmode = 0,
                        show_buf = True,
                        role = 0):
        self.inst_channel = inst_channel
        inst_chipv = CHIP_INFO(inst_channel).get_chipv()
        if role == 0:
            tx_inst = mac_common(inst_channel, inst_chipv)
            rx_inst = self.mac
            rx_channel = self.channel
            rx_chipv = self.chipv
        else:
            tx_inst = self.mac
            rx_inst = mac_common(inst_channel, inst_chipv)
            rx_channel = inst_channel
            rx_chipv = inst_chipv

        rx_inst.mac_txrx_init(rfchannel, rfmode)
        rx_inst.CSI(csi)
        dut_mac = rx_inst.set_rx_conf()

        tx_inst.mac_txrx_init(rfchannel, rfmode)

        tx_inst.wifimac.mac_txpacket_rand()
        tx_inst.set_tx_packet(dut_mac, rate.value, sgi, cwb, length)
        loginfo(dut_mac, rate, sgi, cwb, length)
        txpmd = tx_inst.wifimac.mac_tx_start(burst_num, 1)
        tx_suc_cnt = tx_inst.wifimac.get_tx_cnt(1)
        rx_suc_cnt = rx_inst.wifimac.get_rx_cnt(1)
        loginfo("tx st:", tx_suc_cnt, burst_num)
        loginfo("rx st:", rx_suc_cnt, burst_num)
       # rx_inst.dbg.dbg_rxstatus()
        if rx_suc_cnt != 0:
            with get_rxpacket(rx_channel, rx_chipv) as rxbase:
                rxlink = RxLinkDscr(rx_channel, rx_chipv, rxbase)
                rxctrl = RXCTRL(rx_channel, rx_chipv, rxlink.buf_ptr)
                rxhead = MACHEAD(rx_channel, rx_chipv, rxlink.buf_ptr + rxctrl.struct_size + rxctrl.rx_channel_estimate_len)
                loginfo("=== sig: %d rate:0x%x mcs: %d cwb: 0x%x len:%d csi_len: %d fc: 0x%x"%(rxctrl.sig_mode, rxctrl.rate, rxctrl.MCS, rxctrl.CWB,rxctrl.dump_len, rxctrl.rx_channel_estimate_len, rxhead.fc))
                if show_buf:
                    rx_inst.dbg.dbg_showrxbuffer()

    def tc_tc_rxtx_plot(self, fname):
        res = re.search("rxtest\_b(\d*)\_rfch(\d*)\_rfmd(\d*)\_r(\d*)", fname)
        if res:
            burst_num = res.group(1)
            rfchannel = res.group(2)
            rfmode = res.group(3)
            role = res.group(4)

        df = pd.read_csv(fname)
        if role == "0":
            fgname = "b=%s rfm=%s rfc=%s DUT-RX"%(burst_num, rfmode, rfchannel)
        else:
            fgname = "b=%s rfm=%s rfc=%s DUT-TX"%(burst_num, rfmode, rfchannel)
        plt.ion()
        df_rx = df["rx_suc_cnt"]/df["burst_num"]
        df_tx = df["tx_suc_cnt"]/df["rx_suc_cnt"]
        plt.figure(fgname)
        plt.subplot(221)
        plt.title("RX")
        df_rx.plot.line()
        plt.subplot(222)
        plt.title("TX")
        df_tx.plot.line()
        plt.subplot(223)
        plt.title("RX")
        df_rx.plot.kde()
        plt.subplot(224)
        plt.title("TX")
        df_tx.plot.kde()


    def tc_rxtx_test(self, inst_channel, burst_num = 100, rfchannel = 13, rfmode = 0, role = 0):
        inst_chipv = CHIP_INFO(inst_channel).get_chipv()
        if role == 0:
            tx_inst = mac_common(inst_channel, inst_chipv)
            rx_inst = self.mac
            rx_channel = self.channel
            rx_chipv = self.chipv
        else:
            tx_inst = self.mac
            rx_inst = mac_common(inst_channel, inst_chipv)
            rx_channel = inst_channel
            rx_chipv = inst_chipv

        rx_inst.mac_txrx_init(rfchannel, rfmode)
        rx_mac = rx_inst.set_rx_conf(0)
        tx_inst.mac_txrx_init(rfchannel, rfmode)
        cnt = 0
        length_list = range(26, 1600)
        length_list.reverse()

        with csvreport("mac/rxtest_b%d_rfch%d_rfmd%d_r%d"%(burst_num, rfchannel, rfmode, role)) as rpt:
            for length in length_list:
                for rate in RATE_TAB:
                    if rate.name[:3] == "HT_":
                        if rfmode > 0:
                            cwb_list = [0,1]
                        else:
                            sgi_list = [0]
                    else:
                        cwb_list = [0]
                        sgi_list = [0]
                    for cwb in cwb_list:
                        for sgi in sgi_list:
                            # length = random.randint(40, 1900) 
                            tx_inst.set_tx_packet(rx_mac, rate.value, sgi, cwb, length)
                            loginfo(rx_mac, rate, sgi, cwb, length)
                            cnt = cnt + 1
                            txpmd = tx_inst.wifimac.mac_tx_start(burst_num, 1)
                            tx_inst.wifimac.mac_txpacket_rand()
                            tx_suc_cnt = tx_inst.wifimac.get_tx_cnt(1)
                            rx_suc_cnt = rx_inst.wifimac.get_rx_cnt(1)
                            rpt.write_value(["time", "num", "burst_num", "tx_suc_cnt", "rx_suc_cnt", "txrate", "txcwb", "tx_sgi", "tx_len"], 
                                            [time.asctime(), cnt, burst_num, tx_suc_cnt, rx_suc_cnt, rate.name, cwb, sgi, length])
                            loginfo("%d: %d/%d/%d"%(cnt, tx_suc_cnt, rx_suc_cnt, burst_num))
                            if rx_suc_cnt != 0:
                                with get_rxpacket(rx_channel, rx_chipv) as rxbase:
                                    rxlink = RxLinkDscr(rx_channel, rx_chipv, rxbase)
                                    rxctrl = RXCTRL(rx_channel, rx_chipv, rxlink.buf_ptr)
                                    rxhead = MACHEAD(rx_channel, rx_chipv, rxlink.buf_ptr + rxctrl.struct_size + rxctrl.rx_channel_estimate_len)
                                    loginfo("=== sig: %d rate:0x%x mcs: %d cwb: 0x%x len:%d csi_len: %d fc: 0x%x"%(rxctrl.sig_mode, rxctrl.rate, rxctrl.MCS, rxctrl.CWB,rxctrl.dump_len, rxctrl.rx_channel_estimate_len, rxhead.fc))
                                    rpt.write_value(["rx_sig", "rx_rate", "rx_mcs", "rx_cwb", "rx_len", "rx_csi_len", "rx_fc"], 
                                                    [rxctrl.sig_mode, rxctrl.rate, rxctrl.MCS, rxctrl.CWB, rxctrl.dump_len, rxctrl.rx_channel_estimate_len, rxhead.fc])


    def tc_rxtx_stable_test(self, inst_channel, loop_time=4):
        for loop in range(0, loop_time):
            for rfmode in (0,1):
                if rfmode == 0:
                    rfch_lst = [1,11]
                else:
                    rfch_lst = [3,8]
                for rfch in rfch_lst:
                    for role in (0,1):
                        self.tc_rxtx_test(inst_channel, 100, rfch, rfmode, role)


    def tc_txrxstop_test(self, inst_channel, burst_num1=2000, burst_num2=100, rfchannel = 13, rfmode = 0, role = 0):
        inst_chipv = CHIP_INFO(inst_channel).get_chipv()
        if role == 0:
            tx_inst = mac_common(inst_channel, inst_chipv)
            rx_inst = self.mac
            rx_channel = self.channel
            rx_chipv = self.chipv
        else:
            tx_inst = self.mac
            rx_inst = mac_common(inst_channel, inst_chipv)
            rx_channel = inst_channel
            rx_chipv = inst_chipv

        rx_inst.mac_txrx_init(rfchannel, rfmode)
        rx_mac = rx_inst.set_rx_conf(0)
        tx_inst.mac_txrx_init(rfchannel, rfmode)
        stop_tx_suc_cnt=[]
        stop_pmd_list=[]
        stop_cannot_stop=[]
        tx_suc_cnt_list=[]
        pmd_list=[]

        for ll in range(0,1000):
            stop_tx_suc_cnt=[]
            stop_pmd_list=[]
            stop_cannot_stop=[]
            tx_suc_cnt_list=[]
            pmd_list=[]
            for rate in RATE_TAB:
                sgi=0
                cwb=0
                length=500
                cts=0
                rts=1
                ack=1
                txop=0
                tx_inst.set_tx_packet(rx_mac, rate.value, sgi, cwb, length)
                tx_inst.tx_q_conf(cts,  rts, ack, txop)
                loginfo(rx_mac, rate, sgi, cwb, length, cts,  rts, ack, txop)
                tx_inst.wifimac.mac_txpacket_rand()
                txpmd = tx_inst.wifimac.mac_tx_start(burst_num1, 0)
                cannot_stop=0
                for loopnum in range(0,2000):
                    stop_hold_ms = random.randint(8,10)
                    txing=tx_inst.wifimac.mac_qstop(0x7ff)
                    if txing==1 :
                        logerror("cannot_stop in ",rate)
                        cannot_stop=cannot_stop+1
                    time.sleep(stop_hold_ms/1000)
                    tx_inst.wifimac.mac_qstop_cancel(0x7ff)
                    unstop_hold_ms= random.randint(3,6)
                    time.sleep(unstop_hold_ms/1000)
                
                time_out=0
                while tx_inst.wifimac.mac_tx_finish_check() == 1 :
                    time.sleep(1)
                    time_out = time_out + 1
                    if time_out > 95:
                        logerror("time will out","rate is", rate, "has sent", tx_inst.wifimac.get_tx_send_cnt(0))
                        if time_out > 100:
                            logerror("time out!")
                            return


                tx_suc_cnt = tx_inst.wifimac.get_tx_cnt(1)
                rx_suc_cnt = rx_inst.wifimac.get_rx_cnt(1)
                pmd_info   = tx_inst.wifimac.mac_tx_pmd_read(1)
                
                stop_pmd_list.append(pmd_info)
                stop_tx_suc_cnt.append(tx_suc_cnt)   
                stop_cannot_stop.append(cannot_stop)
                loginfo("rx_suc_cnt",rx_suc_cnt);
                if rx_suc_cnt == 0 :
                    logerror("rx_suc_cnt is zero, something wrong!")
                #loginfo("tx suc:", tx_suc_cnt, "tx int num", tx_int_cnt, "tx sent", burst_num1, "cannot stop", cannot_stop)
                
                '''
                    
                    tx without any stop

                '''
                ## init tx package again
                tx_inst.set_tx_packet(rx_mac, rate.value, sgi, cwb, length)
                txpmd = tx_inst.wifimac.mac_tx_start(burst_num2, 1)
      
                tx_suc_cnt = tx_inst.wifimac.get_tx_cnt(1)
                rx_suc_cnt = rx_inst.wifimac.get_rx_cnt(1) 
                pmd_info   = tx_inst.wifimac.mac_tx_pmd_read(1)      

                pmd_list.append(pmd_info)
                tx_suc_cnt_list.append(tx_suc_cnt)        

            for i in range(0,len(stop_tx_suc_cnt)):
                loginfo("tx suc:", stop_tx_suc_cnt[i], "/", burst_num1, "cannot stop", stop_cannot_stop[i],"pmd_info",stop_pmd_list[i])
                loginfo("tx suc:", tx_suc_cnt_list[i], "/", burst_num2,"pmd_info",pmd_list[i])



    def tc_txrx_mutiq_stop_test(self, inst_channel, burst_num1=2000, burst_num2=100, rfchannel = 13, rfmode = 0, role = 0, bkrandom = 0, noinit=0):
        inst_chipv = CHIP_INFO(inst_channel).get_chipv()
        if role == 0:
            tx_inst = mac_common(inst_channel, inst_chipv)
            rx_inst = self.mac
            rx_channel = self.channel
            rx_chipv = self.chipv
        else:
            tx_inst = self.mac
            rx_inst = mac_common(inst_channel, inst_chipv)
            rx_channel = inst_channel
            rx_chipv = inst_chipv

        if noinit == 0 :
            rx_inst.mac_txrx_init(rfchannel, rfmode)
            rx_mac = rx_inst.set_rx_conf(0)
            tx_inst.mac_txrx_init(rfchannel, rfmode,0xff)
        else:
            rx_mac = int(CHIP_ID(rx_channel, rx_chipv).chip_mac(), 16)

        stop_tx_suc_cnt=[]
        stop_pmd_list=[]
        stop_cannot_stop=[]
        tx_suc_cnt_list=[]
        pmd_list=[]
        rx_inst.wifimac.time0_tar_set(0,10)
        rx_inst.wifimac.time0_tar_set(1,20)
        with csvreport("mac/mutiqstop_b%d_rfch%d_rfmd%d_r%d"%(burst_num1, rfchannel, rfmode, role)) as rpt:
            for ll in range(0,200):
                stop_tx_suc_cnt=[]
                stop_pmd_list=[]
                stop_cannot_stop=[]
                tx_suc_cnt_list=[]
                pmd_list=[]
                for rate in RATE_TAB:
                    sgi=0
                    cwb=0
                    length=500
                    cts=0
                    rts=1
                    ack=1
                    aifs=3
                    txop=0
                    for qnum in range(0,8):
                        tx_inst.set_tx_packet(rx_mac, rate.value, sgi, cwb, length,qnum)
                        if bkrandom == 1:
                            tx_inst.tx_q_conf(cts,  rts, ack, txop,aifs, qnum,0xffff)
                        else:
                            tx_inst.tx_q_conf(cts,  rts, ack, txop,aifs, qnum, qnum*20+10)

                    loginfo(rx_mac, rate, sgi, cwb, length, cts,  rts, ack, txop)

                    tx_inst.wifimac.mac_txpacket_rand()
                    tx_inst.wifimac.mac_tx_mutiq_start(q0_loop = burst_num1,q1_loop = burst_num1,q2_loop = burst_num1,q3_loop = burst_num1,q4_loop = burst_num1,q5_loop = burst_num1,q6_loop = burst_num1,q7_loop = burst_num1,qmap = 0xff)
                    cannot_stop=0
                    for loopnum in range(0,2500):
                        stop_hold_ms = random.randint(8,10)
                        txing=tx_inst.wifimac.mac_qstop(0x7ff)
                        if txing==1 :
                            logerror("cannot_stop in ",rate)
                            cannot_stop=cannot_stop+1
                        time.sleep(stop_hold_ms/1000)
                        tx_inst.wifimac.mac_qstop_cancel(0x7ff)
                        unstop_hold_ms= random.randint(3,6)
                        time.sleep(unstop_hold_ms/1000)
                    
                    time_out=0
                    tx_send_cnt_buf1 = tx_inst.wifimac.get_tx_send_cnt(0)                
                    while tx_inst.wifimac.mac_tx_finish_check() == 1 :
                        time.sleep(1)
                        tx_send_cnt_buf2 = tx_inst.wifimac.get_tx_send_cnt(0)
                        if tx_send_cnt_buf2 > tx_send_cnt_buf1 :
                            tx_send_cnt_buf1 = tx_send_cnt_buf2
                            continue
                        else:
                            time_out = time_out + 1
                            if time_out > 95:
                                logerror("time will out","rate is", rate, "has sent", tx_inst.wifimac.get_tx_send_cnt(0))
                                if time_out > 100:
                                    logerror("time out in step 1!")
                                   # return

                    tx_suc_cnt = []
                    for q_cnt in range(0,8):
                        tx_suc_cnt.append(tx_inst.wifimac.get_tx_cnt(1,q_cnt))
                    
                    rx_suc_cnt = rx_inst.wifimac.get_rx_cnt(1)
                    pmd_info   = tx_inst.wifimac.mac_tx_pmd_read(1)
                    
                    stop_pmd_list.append(pmd_info)
                    stop_tx_suc_cnt.append(tx_suc_cnt)   
                    stop_cannot_stop.append(cannot_stop)
                    rpt.write_value(["time", "round", "pmd_info_stop", "tx_suc_cnt_stop", "cannot_stop","rx_suc_cnt_stop", "txrate", "txcwb", "tx_sgi", "tx_len"],
                                    [time.asctime(), ll, pmd_info, tx_suc_cnt, cannot_stop,rx_suc_cnt, rate.name, cwb, sgi, length])

                    loginfo("rx_suc_cnt",rx_suc_cnt);
                    if rx_suc_cnt == 0 :
                        logerror("rx_suc_cnt is zero in step1, something wrong!")
                        #return
                  
                    #loginfo("tx suc:", tx_suc_cnt, "tx int num", tx_int_cnt, "tx sent", burst_num1, "cannot stop", cannot_stop)
                    
                    '''
                        
                        tx without any stop

                    '''

                    ###set tx buffer again
                    for qnum in range(0,8):
                        tx_inst.set_tx_packet(rx_mac, rate.value, sgi, cwb, length,qnum)

                    tx_inst.wifimac.mac_tx_mutiq_start(q0_loop = burst_num2,q1_loop = burst_num2,q2_loop = burst_num2,q3_loop = burst_num2,q4_loop = burst_num2,q5_loop = burst_num2,q6_loop = burst_num2,q7_loop = burst_num2,qmap = 0xff)
                    
                    time_out=0
                    while tx_inst.wifimac.mac_tx_finish_check() == 1 :
                        time.sleep(1)
                        time_out = time_out + 1
                        if time_out > 95:
                            logerror("time will out","rate is", rate, "has sent", tx_inst.wifimac.get_tx_send_cnt(0))
                            if time_out > 100:
                                logerror("time out in step2!")
                                #return

                    tx_suc_cnt = []
                    for q_cnt in range(0,8):
                        tx_suc_cnt.append(tx_inst.wifimac.get_tx_cnt(1,q_cnt))
                        tx_inst.wifimac.mac_tx_col_read(1,q_cnt)
                  
                    rx_suc_cnt = rx_inst.wifimac.get_rx_cnt(1) 
                    pmd_info   = tx_inst.wifimac.mac_tx_pmd_read(1)      
                    if rx_suc_cnt == 0 :
                        logerror("rx_suc_cnt is zero in step2, something wrong! pmd is",pmd_info)
                        #return

                    pmd_list.append(pmd_info)
                    tx_suc_cnt_list.append(tx_suc_cnt)    

                    rpt.write_value(["pmd_info_without_stop", "tx_suc_cnt_without_stop", "rx_suc_cnt_without_stop"],
                                    [pmd_info, tx_suc_cnt,rx_suc_cnt])

                for i in range(0,len(stop_tx_suc_cnt)):
                    loginfo("tx suc:", stop_tx_suc_cnt[i], "/", burst_num1, "cannot stop", stop_cannot_stop[i],"pmd_info",stop_pmd_list[i])
                    loginfo("tx suc:", tx_suc_cnt_list[i], "/", burst_num2,"pmd_info",pmd_list[i])


    def tc_txrxbuffer_test(self, inst_channel, burst_num=2000, rfchannel = 13, rfmode = 0, role = 0):
        inst_chipv = CHIP_INFO(inst_channel).get_chipv()
        if role == 0:
            tx_inst = mac_common(inst_channel, inst_chipv)
            rx_inst = self.mac
            rx_channel = self.channel
            rx_chipv = self.chipv
        else:
            tx_inst = self.mac
            rx_inst = mac_common(inst_channel, inst_chipv)
            rx_channel = inst_channel
            rx_chipv = inst_chipv


        rx_inst.mac_txrx_init(rfchannel, rfmode)
        rx_mac = rx_inst.set_rx_conf(0)
        tx_inst.mac_txrx_init(rfchannel, rfmode)
        tx_suc_cnt_list=[]
        pmd_list=[]
        last_full_cnt=0
        rx_dbg = mac_dbg(rx_channel, rx_chipv)
        with csvreport("mac/rx_buffer_reload_b%d_rfch%d_rfmd%d_r%d"%(burst_num, rfchannel, rfmode, role)) as rpt:
            for ll in range(0,5000):
                tx_suc_cnt_list=[]
                pmd_list=[]
                for rate in RATE_TAB:
                    sgi=0
                    cwb=0
                    length=500
                    cts=0
                    rts=1
                    ack=1
                    txop=0
                    
                    '''
                        set time0 alarm range
                    '''
                    min_us=length*8*1000000/RATE_DATA[rate.name]
                    max_us=rx_inst.wifimac.get_total_buffer_num(0)*2*min_us

                    rx_inst.wifimac.time0_tar_set(0,min_us)
                    rx_inst.wifimac.time0_tar_set(1,max_us)

                    tx_inst.set_tx_packet(rx_mac, rate.value, sgi, cwb, length)
                    tx_inst.tx_q_conf(cts,  rts, ack, txop)
                    loginfo(rx_mac, rate, sgi, cwb, length, cts,  rts, ack, txop, min_us,max_us)
                    tx_inst.wifimac.mac_txpacket_rand()

                    txpmd = tx_inst.wifimac.mac_tx_start(burst_num, 1)
                
                    tx_suc_cnt = tx_inst.wifimac.get_tx_cnt(1)
                    rx_suc_cnt = rx_inst.wifimac.get_rx_cnt(1) 
                    pmd_info   = tx_inst.wifimac.mac_tx_pmd_read(1)      

                    ovfl_cnt=rx_dbg.hwreg.MAC_RX.MACRX_BUF_FULLCNT.reg-last_full_cnt
                    loginfo("rx_suc_cnt",rx_suc_cnt,"overfull",ovfl_cnt)
                    
                    rpt.write_value(["time", "round", "overfull","pmd_info", "tx_suc_cnt", "rx_suc_cnt", "txrate", "txcwb", "tx_sgi", "tx_len"],
                                    [time.asctime(), ll, ovfl_cnt,pmd_info, tx_suc_cnt,rx_suc_cnt, rate.name, cwb, sgi, length])

                    last_full_cnt=rx_dbg.hwreg.MAC_RX.MACRX_BUF_FULLCNT.reg

                    if rx_suc_cnt == 0 :
                        logerror("rx_suc_cnt is zero, something wrong!")
                        rx_dbg.dbg_rxstatus()
                        #return

                    pmd_list.append(pmd_info)
                    tx_suc_cnt_list.append(tx_suc_cnt)        

                for i in range(0,len(tx_suc_cnt_list)):
                    loginfo("tx suc:", tx_suc_cnt_list[i], "/", burst_num,"pmd_info",pmd_list[i])

                time.sleep(1)



    def tc_txrx_ampdu(self, inst_channel, burst_num=2000, rfchannel = 13, rfmode = 0, role = 0):
        inst_chipv = CHIP_INFO(inst_channel).get_chipv()
        if role == 0:
            tx_inst = mac_common(inst_channel, inst_chipv)
            tx_mem = MEM(inst_channel, inst_chipv)
            tx_chip_mac = int(CHIP_ID(inst_channel, inst_chipv).chip_mac(), 16)
            tx_dbg = mac_dbg(inst_channel, inst_chipv)          
            rx_inst = self.mac
            rx_channel = self.channel
            rx_chipv = self.chipv
        else:
            tx_inst = self.mac
            tx_mem = MEM(self.channel, self.chipv)
            tx_chip_mac = int(CHIP_ID(self.channel, self.chipv).chip_mac(), 16)
            tx_dbg = mac_dbg(self.channel, self.chipv)
            rx_inst = mac_common(inst_channel, inst_chipv)
            rx_channel = inst_channel
            rx_chipv = inst_chipv

        rx_inst.mac_txrx_init(rfchannel, rfmode)
        rx_mac = rx_inst.set_rx_conf(0)
        tx_inst.mac_txrx_init(rfchannel, rfmode)
        tx_inst.set_rx_conf(0)

        rx_dbg = mac_dbg(rx_channel, rx_chipv)        
        rx_dbg.hwreg.MAC_RX.MACRXBA0_WINCONF.reg_rxba0_winlen=5
        rx_dbg.hwreg.MAC_RX.MACRXBA0_TAHI.reg = (tx_chip_mac>>32)
        rx_dbg.hwreg.MAC_RX.MACRXBA0_TALO.reg = (tx_chip_mac&0xffffffff)
        rx_dbg.hwreg.MAC_RX.MACRXBA0_CONF.reg_rxba0_ena=1
        rx_dbg.hwreg.MAC_RX.MACRXBA0_CONF.reg_rxba0_imr=1
        rx_dbg.hwreg.MAC_RX.MACRXBA0_WINCONF.reg_rxba0_winstart = 0

        rx_dbg.hwreg.MAC_RX.MACRXOPTION.reg_rxsampdu_int_size =1

        tx_suc_cnt_list=[]
        pmd_list=[]
        last_full_cnt=0
        rx_inst.wifimac.time0_tar_set(0,10)
        rx_inst.wifimac.time0_tar_set(1,15)
        tx_inst.wifimac.time0_tar_set(0,8)
        tx_inst.wifimac.time0_tar_set(1,10)
        # set ba level
        tx_inst.wifimac.set_ba_level(5,3,2,0)
        for ll in range(0,5000):
            tx_suc_cnt_list=[]
            pmd_list=[]
            for rate in [RATE_TAB['HT_MCS0'].value,RATE_TAB['HT_MCS1'].value,RATE_TAB['HT_MCS2'].value,RATE_TAB['HT_MCS3'].value,RATE_TAB['HT_MCS4'].value]:
                sgi=0
                cwb=0
                length=500
                cts=0
                rts=1
                ack=2
                txop=0
                ampdu=1
                qsel=0
                delim_num=4
                rx_dbg.hwreg.MAC_RX.MACRXBA0_WINCONF.reg_rxba0_winlen=5
                rx_dbg.hwreg.MAC_RX.MACRXBA0_WINCONF.reg_rxba0_winstart = 0
                tx_inst.set_tx_packet(rx_mac, rate.value, sgi, cwb, length,qsel,1,0,ampdu,delim_num);
                tx_inst.set_tx_packet(rx_mac, rate.value, sgi, cwb, length,qsel,0,0,ampdu,delim_num);
                tx_inst.set_tx_packet(rx_mac, rate.value, sgi, cwb, length,qsel,0,0,ampdu,delim_num);
                tx_inst.set_tx_packet(rx_mac, rate.value, sgi, cwb, length,qsel,0,0,ampdu,delim_num);
                tx_inst.set_tx_packet(rx_mac, rate.value, sgi, cwb, length,qsel,0,1,ampdu,delim_num);
                      
                tx_inst.tx_q_conf(cts,  rts, ack, txop)

                loginfo(rx_mac, rate, sgi, cwb, length, cts,  rts, ack, txop)
                tx_inst.wifimac.mac_txpacket_rand()

                txpmd = tx_inst.wifimac.mac_tx_start(burst_num, 1)
            
                tx_suc_cnt = tx_inst.wifimac.get_tx_cnt(1)
                rx_suc_cnt = rx_inst.wifimac.get_rx_cnt(1) 
                pmd_info   = tx_inst.wifimac.mac_tx_pmd_read(1)      
                ba_num     = tx_inst.wifimac.get_ba_num(1)
                loginfo("rx_suc_cnt",rx_suc_cnt,"overfull",rx_dbg.hwreg.MAC_RX.MACRX_BUF_FULLCNT.reg-last_full_cnt)
                loginfo("ba_num",ba_num)

                last_full_cnt=rx_dbg.hwreg.MAC_RX.MACRX_BUF_FULLCNT.reg
                if rx_suc_cnt == 0 :
                    logerror("rx_suc_cnt is zero, something wrong!")
                    rx_dbg.dbg_rxstatus()
                    return

                pmd_list.append(pmd_info)
                tx_suc_cnt_list.append(tx_suc_cnt)        

            for i in range(0,len(tx_suc_cnt_list)):
                loginfo("tx suc:", tx_suc_cnt_list[i], "/", burst_num,"pmd_info",pmd_list[i])

            time.sleep(1)

    def tc_mac_pti_test(self,out_pti=1):
        
        tx_inst = self.mac
        tx_mem = MEM(self.channel, self.chipv)
        tx_chip_mac = int(CHIP_ID(self.channel, self.chipv).chip_mac(), 16)
        tx_dbg = mac_dbg(self.channel, self.chipv)
        tx_inst.mac_txrx_init(13, 0)

        tx_dbg.hwreg.MAC_PWR.MACRWBT_COEX_TIMER0_CONF0.reg_coex_timer0_pti=10
        tx_dbg.hwreg.MAC_PWR.MACRWBT_COEX_TIMER0_CONF0.reg_coex_timer0_ena=1
        tx_dbg.hwreg.MAC_PWR.MACRWBT_COEX_TIMER0_CONF0.reg_coex_timer0_fh=1

        tx_dbg.hwreg.MAC_PWR.MACCO_EXTERN_CONF0.reg_extern_out0_pti=1
        tx_dbg.hwreg.MAC_PWR.MACCO_EXTERN_CONF0.reg_extern_out1_pti=2
        tx_dbg.hwreg.MAC_PWR.MACCO_EXTERN_CONF0.reg_extern_out2_pti=13
        tx_dbg.hwreg.MAC_PWR.MACCO_EXTERN_CONF0.reg_extern_out3_pti=14

        tx_dbg.hwreg.MAC_PWR.MACCO_EXTERN_CONF0.reg_extern_in0_pti=1
        tx_dbg.hwreg.MAC_PWR.MACCO_EXTERN_CONF0.reg_extern_in1_pti=2
        tx_dbg.hwreg.MAC_PWR.MACCO_EXTERN_CONF0.reg_extern_in2_pti=11
        tx_dbg.hwreg.MAC_PWR.MACCO_EXTERN_CONF0.reg_extern_in3_pti=12

        if out_pti == 0:
            tx_dbg.hwreg.MAC_PWR.MACRWBT_COEX_GPIO_SEL.reg_gpio_wlan_active_sel= 7
        else:
            tx_dbg.hwreg.MAC_PWR.MACRWBT_COEX_GPIO_SEL.reg_gpio_wlan_active_sel= 0




class WIFISLEEP_TC_FUNC(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        self.clk_source = 0
        self.hwreg = HWREG(self.channel, self.chipv)
        self.mem = MEM(self.channel, self.chipv)
        self.rtc_clk = RTC_CLK(self.channel, self.chipv)
        self.rtc_sleep = RTC_SLEEP(self.channel, self.chipv)
        self.rtc_timer = RTC_TIMER(self.channel, self.chipv)
        chip = mac_common(self.channel, self.chipv)

    def get_tsf(self):
        self.hwreg.MAC_PWR.MACTSF_TIME_FZ.reg_tsf0time_fz = 1
        cur = self.hwreg.MAC_PWR.MACTSF0_TIME_LO.reg + (self.hwreg.MAC_PWR.MACTSF0_TIME_HI.reg << 32)
        self.hwreg.MAC_PWR.MACTSF_TIME_FZ.reg_tsf0time_fz = 0
        return cur        

    def tsf_wakeup_set(self, sleep_time = 1000000):
        cur = self.get_tsf()
        tar = cur + sleep_time
        self.hwreg.MAC_PWR.MACTSF0_TIMER_LO.reg = tar & 0xffffffff
        self.hwreg.MAC_PWR.MACTSF0_TIMER_HI.reg = tar >> 32
        self.hwreg.MAC_PWR.MACTSF0TIMER_ENA.reg_tsf0timer_wakeup_ena = 1
        self.hwreg.MAC_PWR.MACTSF0TIMER_ENA.reg_tsf0timer_ena = 1
        return tar
    # def set_lp_clk(self):
    #     chip.hals.MEM.wr(0x3f4c0054, 0x1001001)
    #     chip.hals.MEM.wr(0x3f4c0050, 0)


    def sel_lp_clk(self, clk_source = 0):
        self.clk_source = clk_source
        if self.clk_source == 0:
            self.mem.wr(0x3f4c0054, 0x1001001)
            self.mem.wr(0x3f4c0050, 0)
        elif self.clk_source == 1:
            self.hwreg.RTC_CNTL.RTC_CLK_CONF.reg_dig_clk8m_en = 1
            self.mem.wr(0x3f4c0054, 0x2001001)
            self.mem.wr(0x3f4c0050, 255)

        # calibration
        cali = (int(self.rtc_clk.get_clk_calibration(self.clk_source))>>7)
        self.cali_value_s = cali/4096.
        loginfo("cali value:", cali, self.cali_value_s)
        self.hwreg.MAC_PWR.MACRTC_CALISW.reg_calisw_value = cali


    def tc_Lsleep_tsf(self, sleep_time):
        RES = 1
        # clock TBTT wakeup
        self.hwreg.MAC_PWR.MACSLEEP0_CONF.reg_wakeup0_ena = 0
        self.sel_lp_clk(0)
        self.hwreg.MAC_PWR.MACTSF0_ACTIVE.reg_tsf0_active_clr = 1
        self.hwreg.MAC_PWR.INT_CLR_MACPWR.tsf0_reach_int_clr = 1
        # time.sleep(sleep_time + 1)
        cur0 = self.get_tsf()/1000000.
        loginfo("cur0:", cur0)
        self.tsf_wakeup_set(sleep_time*1000000)
        loginfo("active:", self.hwreg.MAC_PWR.MACTSF0_ACTIVE.tsf0_active_st)
        loginfo("goto sleep...")
        self.rtc_sleep.sleep(0,0x20,0,1) 
        cur1 = self.get_tsf()/1000000.
        loginfo("wakeup...")
        loginfo("cur1:", cur1)
        loginfo("reg_tsf0timer_ena:", self.hwreg.MAC_PWR.MACTSF0TIMER_ENA.reg_tsf0timer_ena)
        loginfo("active:", self.hwreg.MAC_PWR.MACTSF0_ACTIVE.tsf0_active_st)
        
        time.sleep(1)
        if self.hwreg.MAC_PWR.INT_RAW_MACPWR.tsf0_reach_int_raw: # check ini
            self.hwreg.MAC_PWR.INT_CLR_MACPWR.tsf0_reach_int_clr = 1
        else:
            logwarn("no interrrput")
            RES = 0

        if self.hwreg.MAC_PWR.MACTSF0_ACTIVE.tsf0_active_st:
            self.hwreg.MAC_PWR.MACTSF0_ACTIVE.reg_tsf0_active_clr = 1
            if self.hwreg.MAC_PWR.MACTSF0_ACTIVE.tsf0_active_st:
                logwarn("active clear fail")
                RES = 0
        else:
            RES = 0
            logwarn("no active")

        if abs(cur1-cur0 - sleep_time) > 0.2:
            RES = 0
            logwarn("time tsf time error:", cur1-cur0, "cur1:", cur1, "cur0:", cur0)
        logresck(RES)


    def tc_Lsleep_tbtt(self, TBTT = 1000):
        self.sel_lp_clk(0)
        self.hwreg.MAC_PWR.MACSLEEP0_CONF.reg_wakeup0_ena = 1
        self.hwreg.MAC_PWR.MACBEAINTER0.reg_tbtt0 = TBTT
        cur_last = self.get_tsf()/1000000.
        while True:
            cur0 = self.get_tsf()/1000000.
            loginfo("delta:", cur0-cur_last, "cur:", cur0)
            self.rtc_timer.update_time()
            rtc_time0 = self.rtc_timer.get_time_low()
            loginfo("rtc_time:", rtc_time0)
            if abs(cur0-cur_last - TBTT*1024/1000000.) > 0.2:
                logwarn("wakeup interval:", cur0-cur_last, "TBTT:", TBTT*1024/1000000.)
            cur_last = cur0
            self.rtc_sleep.sleep(0,0x20,0,1) 
            self.rtc_timer.update_time()
            rtc_time1 = self.rtc_timer.get_time_low()
            loginfo("rtc_time_delta:", int(rtc_time1)-int(rtc_time0), self.cali_value_s*(int(rtc_time1)-int(rtc_time0))/1000000.)
            if self.hwreg.MAC_PWR.MACTSF0_ACTIVE.tsf0_active_st:
                self.hwreg.MAC_PWR.MACTSF0_ACTIVE.reg_tsf0_active_clr = 1
                if self.hwreg.MAC_PWR.MACTSF0_ACTIVE.tsf0_active_st:
                    logwarn("active clear fail")
