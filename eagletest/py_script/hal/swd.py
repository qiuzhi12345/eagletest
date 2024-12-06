# -- coding: utf-8 --
class SWD(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        
    def swd_init(self, auto_feed = 1, swd_sig_width = 300):
        '''
        :brief: set swd param to make swd work.
        :param:
            - auto_feed: 喂狗模式选择
             - 1： RTC_SWD自动喂狗；
             - 0： 软件喂狗。
            - swd_sig_width: 超时计数器接收的喂狗信号和清空复位标记信号的宽度，10bit。
        :return: no return
        '''
        return self.channel.req_com("swd_init %d %d"%(auto_feed, swd_sig_width))
    
    def swd_stop(self):
        '''
        :brief: swd停止工作
        :param: no param
        :return: no return
        '''
        return self.channel.req_com("swd_stop")

    def swd_lock(self):
        '''
        :brief: 开启swd写保护。
        :param: no param
        :return: no return
        '''
        return self.channel.req_com("swd_lock")

    def swd_unlock(self):
        '''
        :brief: 解锁swd。
        :param: no param
        :return: no return
        '''
        return self.channel.req_com("swd_unlock")

    def swd_feed(self):
        '''
        :brief: feed swd
        :param:  no param
        :return:  no return
        '''
        return self.channel.req_com("swd_feed")
    
    def get_swd_feed_int(self):
        '''
        :brief: 超时计数器达到3时，发出的中断信号，一旦喂狗，该信号会自动清除。
        :param:  no param
        :return:  no return
        '''
        return self.channel.req_com("get_swd_feed_int")
    
    def get_swd_reset_flag(self):
        '''
        :brief: 超时计数器超时，发出的复位标记信号。
        :param:  no param
        :return:  no return
        '''
        return self.channel.req_com("get_swd_rst_flag")  
    
    def clr_swd_reset_flag(self):
        '''
        :brief: 清除复位标记信号。
        :param:  no param
        :return:  no return
        '''
        return self.channel.req_com("clr_swd_rst_flag")    

    def swd_int_enable(self, enable):
        '''
        :brief: enable or disable swd interrupt
        :param:
            enable:
                - 0: disable;
                - 1: enable
        :return: no return
        ''' 
        return self.channel.req_com("swd_int_enable %d"%(enable))
    
    def swd_int_raw_sts(self):
        '''
        :brief: swd interrupt raw status
        :param: no param
        :return:  raw status value
        ''' 
        return self.channel.req_com("swd_int_raw")
    
    def swd_int_sts(self):
        '''
        :brief: swd interrupt status
        :param: no param
        :return:  status value
        ''' 
        return self.channel.req_com("swd_int_sts")

    def swd_int_clr(self):
        '''
        :brief:  clear swd interrupt
        :param:  no param
        :return: no return
        ''' 
        return self.channel.req_com("swd_int_clr")


