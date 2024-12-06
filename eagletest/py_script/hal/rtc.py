class RTC(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel
        
    def rtc_reset_cause(self):
        '''
        :brief:
            get rtc reset reason
        :param:
            no parem
        :return:
            return reset reason
        ''' 
        return self.channel.req_com("rtc_reset_cause")
