# -- coding: utf-8 --
class X32K_WDT(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel

    def wdt_init(self, factor_value = 0x22222333):
        '''
        :brief: set 32k wdt to make it work, default set backup 32k enable, restart 32k enable, return 32k enable.
        :param:
            factor_value: 分频因子，在xtal 32k挂死时由150k按factor_value分频成32k作为备用32k，算法如下：
            设rtc_clk的频率为f_rtc_clk(单位为khz),8个分频因子为x0,x1,x2,x3,x4,x5,x6,x7。S = x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7。
            所以x0~x7只需要满足两个条件即可：
            S =  f_rtc_clk * (4/32)；
            M + 1 >= xn >= M；（ 0 <= n <= 7,xn 为整数 ）
            其中：M = 取整(f_rtc_clk / 32 / 2) , S取整数（四舍五入）。
            例如： rtc_clk的时钟频率为163khz，则f_rtc_clk = 163， S = 20 ，M = 2 ，所以满足条件的{x0,x1,x2,x3,x4,x5,x6,x7} = {2,3,2,3,2,3,2,3}, fvalue = 0x23232323
            假如150k真实频率为150k，则f_rtc_clk = 150 ，S = 18， M = 2，有6个2, 2个3，满足条件的{x0,x1,x2,x3,x4,x5,x6,x7} = {2,2,2,2,2,2,3,3}, fvalue = 0x22222233
        :return:
            no return
        '''
        return self.channel.req_com("x32k_wdt_init %d"%(factor_value))

    def wdt_config(self, timeout_thres = 0x5, stable_thres = 0xf, restart_time = 0x200, return_time = 0xf):
        '''
        :brief: set x32k wdt param.
        :param:
            - timeout_thres: 超过该阈值未检测到x32k时钟上升沿，则认为x32k有问题, 最大值为0xfe；
            - stable_thres： 重启后的x32k时钟周期小于该阈值则认为x32k时钟稳定；
            - restart_time： x32k重启时间，最大值0xfffe；
            - return_time： x32k_wdt将时钟从backup_32k切回x32k的等待时间。
        :return:
            no return
        '''
        return self.channel.req_com("x32k_wdt_config %d %d %d %d"%(timeout_thres, stable_thres, restart_time, return_time))

    def x32k_poweron_bysoftware(self, is_software = True):
        '''
        :brief: x32k上下电默认是状态机控制的，也可以选择软件配置。
        :param:
            - is_software: True为软件控制， False为状态机控制；
        :return:
            no return
        '''
        return self.channel.req_com("x32k_poweron_bysoftware %d"%(is_software))

    def wdt_enable(self, enable = 1):
        '''
        :brief: 32k wdt enable or disable
        :param:
            enable: enable x32k wdt or not;
        :return:
            no return
        '''
        return self.channel.req_com("x32k_wdt_enable %d"%(enable))
    
    def wdt_reset_enable(self, enable = 1):
        '''
        :brief: 32k wdt复位使能
        :param:
            enable: enable x32k or not.
        :return:
            no return
        '''
        return self.channel.req_com("x32k_wdt_reset_enable %d"%(enable))
    
    def x32k_backup_enable(self, enable):
        '''
        :brief: 备用32k时钟使能。
        :param:
            enable: enable backup 32k or not.
        :return:
            no return
        '''
        return self.channel.req_com("x32k_auto_backup_enable %d"%(enable))

    def x32k_restart_enable(self, enable):
        '''
        :brief: 32k挂死时，自动重启32k时钟使能.
        :param:
            enable: enable x32k restart or not.
        :return:
            no return
        '''
        return self.channel.req_com("x32k_auto_restart_enable %d"%(enable))
    
    def x32k_reture_enable(self, enable):
        '''
        :brief: 32k挂死时，x32k时钟返回使能，时钟由backup 32k切回xtal 32k.
        :param:
            enable: enable x32k return or not.
        :return:
            no return
        '''
        return self.channel.req_com("x32k_auto_return_enable %d"%(enable))

    def wdt_int_enable(self, enable):
        '''
        :brief:
            xtal 32k时钟停振时，x32k wdt将发起中断。
        :param:
            enable:
                - 0: disable;
                - 1: enable
        :return:
            no return
        ''' 
        return self.channel.req_com("x32k_dead_int_enable %d"%(enable))
    
    def wdt_int_raw_sts(self):
        '''
        :brief:
            wdt interrupt raw status
        :param:
            no param
        :return:
            raw status value
        ''' 
        return self.channel.req_com("x32k_dead_int_raw")
    
    def wdt_int_sts(self):
        '''
        :brief:
            wdt interrupt status
        :param:
            no param
        :return:
            status value
        ''' 
        return self.channel.req_com("x32k_dead_int_sts")

    def wdt_int_clr(self):
        '''
        :brief:
            clear wdt interrupt
        :param:
            no param
        :return:
            no return
        ''' 
        return self.channel.req_com("x32k_dead_int_clr")