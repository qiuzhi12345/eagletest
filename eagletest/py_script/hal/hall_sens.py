class HALL_SENS(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel

    def config(self):
        '''
        :brief:
            config hall sensor to make hall sensor sample.
        :param:
            no param
        :return:
            no return
        '''
        return self.channel.req_com("hall_sens_config")

    def phase_inv(self):
        '''
        :brief:
            invert hall sensor phase.
        :param:
            no param
        :return:
            no return
        '''
        return self.channel.req_com("hall_sens_inv_phase")

    def close(self):
        '''
        :brief:
            close hall sensor to make it not work, mainly close xpd & phase.
        :param:
            no param
        :return:
            no return
        '''
        return self.channel.req_com("hall_sens_close")
