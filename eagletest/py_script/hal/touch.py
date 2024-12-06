class TOUCH(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel

    def touch_init(self, touch_no, dac = 7):
        '''
        :brief:
            touch init single pad
        :param:
            - touch_no: [0~9], which touch to init
            - dac: dac value, 3 bits
        :return:
            no return
        '''
        return self.channel.req_com("touch_single_init %d %d"%(touch_no, dac))

    def touch_read(self, touch_no):
        '''
        :brief:
            read touch out value
        :param:
            touch_no: [0~9], which touch to read
        :return:
            return touch out value
        '''
        return self.channel.req_com("touch_read %d"%(touch_no))

    def set_thres(self, touch_no, thres):
        '''
        :brief:
            set touch threshold
        :param:
            - touch_no: [0~9];
            - thres: threshold to set
        :return:
            no return
        '''
        return self.channel.req_com("set_thres %d %d"%(touch_no, thres))

    def get_thres(self, touch_no):
        '''
        :brief:
            get touch threshold value
        :param:
            touch_no: [0~9], get which threshold
        :return:
            return touch_no touch threshold
        '''
        return self.channel.req_com("get_thres %d"%(touch_no))

    def get_meas_en(self, touch_no):
        '''
        :brief:
            get meas_en register value, it means touch condition occur or not
        :param:
            touch_no: [0~9], get which meas_en
        :return:
            - return 1: touch valid;
            - return 0: touch invalid
        ''' 
        return self.channel.req_com("get_meas_en %d"%(touch_no))

    def touch_global_init(self, drefh = 3, drefl = 0, drange = 3, xpd_wait = 10, meas_delay = 0xffff):
        '''
        :brief:
            set global parameter for each touch
        :param:
            - drefh: touch sensor saw wave top voltage, 2 bits;
            - drefl: touch sensor saw wave bottom voltage, 2 bits;
            - drange: touch sensor saw wave voltage range, 2 bits;
            - xpd_wait: waiting time between touch_start and touch_xpd, 8 bits;
            - meas_delay: the measurement's duration(in 8MHZ cycles), 16 bits.
        :return:
            no return
        '''
        return self.channel.req_com("touch_global_init %d %d %d %d %d"%(drefh, drefl, drange, xpd_wait, meas_delay))

    def touch_clr_meas_en(self):
        '''
        :brief:
            clear meas_en value
        :param:
            no param
        :return:
            no return
        '''
        return self.channel.req_com("clr_meas_en")

    def get_int_raw_sts(self):
        '''
        :brief:
            get interrupt raw status
        :param:
            no param
        :return:
            return raw status
        '''
        return self.channel.req_com("get_touch_raw_sts")

    def get_int_sts(self):
        '''
        :brief:
            get interrupt status
        :param:
            no param
        :return:
            return status
        '''
        return self.channel.req_com("get_touch_sts")

    def enable_int(self, enable):
        '''
        :brief:
            enable touch interrupt
        :param:
            enable:
                - 1: enable interrupt;
                - 0: disable interrupt
        :return:
            no return
        '''
        return self.channel.req_com("enable_touch_int %d"%(enable))

    def clr_int(self):
        '''
        :brief:
            clear interrupt
        :param:
            no param
        :return:
            no return
        '''
        return self.channel.req_com("clr_touch_int")

    def enable_period_timer(self):
        '''
        :brief:
            enable touch period timer
        :param:
            no param
        :return:
            no return
        '''
        return self.channel.req_com("touch_period_enable")

    def disable_period_timer(self):
        '''
        :brief:
            disable touch sleep period timer
        :param:
            no param
        :return:
            no return
        '''
        return self.channel.req_com("touch_period_disable")

    def touch_debug(self, touch_no, tie_opt = 0):
        '''
        :brief:
            debug touch to get touch wave form by instrument. only for analog.
        :param:
            - touch_no: [0~9], which touch to read
            - tie_opt: default touch sensor tie option. 0: tie low; 1: tie high
        :return:
            no return
        '''
        return self.channel.req_com("touch_debug_open %d %d"%(touch_no, tie_opt))

    def touch_debug_close(self, touch_no):
        '''
        :brief:
            close touch debug function. only for analog.
        :param:
            touch_no: [0~9], which touch to read
        :return:
            no return
        '''
        return self.channel.req_com("touch_debug_close %d"%(touch_no))

