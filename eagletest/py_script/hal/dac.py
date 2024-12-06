class DAC(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel

    def dac_out(self, dac_en, tone_en, dc_value, tone_scale, tone_step):
        '''
        :brief:
            dac configuration
        :param:
            - dac_en: 2 LSB bits with bit0 for DAC1 xpd control and bit1 for DAC2 xpd control
            - tone_en: 1 efficient bit, tone function enable signal. if 1, output sine wave; else output DC signal
            - dc_value: half-word efficient with bit[15:8] as DAC2 digital input for DC output and bit[7:0] as DAC1 digital input for DC output
            - tone_scale: scale control of tone amplitude
            - tone_step: step length of sine wave table, which could be used to control the tone frequency
        :return:
            no return
        '''
        return self.channel.req_com("dac_out %d %d 0x%x 0x%x 0x%x"%(dac_en, tone_en, dc_value, tone_scale, tone_step))

    def dc_out(self, pad, dc_value):
        '''
        :brief:
            dac dc mode configuration
        :param:
            - pad: can be set to 1 or 2, means dac1 and dac2.
            - dc_value: 8 bits, means input dc value of dac1 or dac2.
        :return:
            return dc_value
        '''
        return self.channel.req_com("dac_dc_out %d %d"%(pad, dc_value))

    def cw_out(self, pad, dc_offset = 0, fstep = 0x100, cw_scale = 0, phase_inv = 2):
        '''
        :brief:
            dac rtc ac mode configuration, output cosine waveform.
        :param:
            - pad: can be set to 1 or 2, means dac1 and dac2.
            - dc_offset: 8 bits, dc offset added to the waveform.
            - fstep: 16bits, used to adjust the cosine waveform frequency.
            - cw_scale: 2 bits, scale waveform, the amplitude of cosine waveform can be scaled down to 1, 1/2, 1/4 or 1/8 when set to 0, 1, 2, 3.
            - phase_inv: apply phase shift, 0, 90, 180, 270 degrees phase shift can be introduced when set 0, 1, 2, 3, normally need to set 2 or 3 to get cosine waveform.
        :return:
            return set parameters.
        '''
        return self.channel.req_com("dac_cw_out %d %d %d %d %d"%(pad, dc_offset, fstep, cw_scale, phase_inv))
