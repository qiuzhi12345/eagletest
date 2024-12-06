class EXT_DAC(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel

    def spi_inf_cfg(self, spi_no=2, clk_div):
        '''
        :brief:
            spi interface configuration of ESP chip for control of external DAC device (DAC80004)
        :param:
            - spi_no: select spi port
            - clk_div : division value of spi clk from apb clock (80M), e.g. 10-->spi_clk=8M
        :return:
            no return
        '''
        return self.channel.req_com("spi_inf_cfg %d %d"%(spi_no, clk_div))

    def esp_rd_spidev(self, spi_no=2, rd_cmd, cs_dly):
        '''
        :breif:
            read register value of the slave device
        :param:
            -spi_no: select spi port
            -rd_cmd: command number of dac80004, 4 bits in accordance with command bits
            -cs_dly: cycle values of hold_time and setup_time, with high half-byte for the former and low half-byte for the latter
        :return:
            return the value of accessed register
        '''
        return self.channel.req_com("esp_rd_spidev %d %d %d"%(spi_no, rd_cmd, cs_dly))

    def esp_wr_spidev(self, spi_no=2, value, cs_dly):
        '''
        :breif:
            write value into register of the slave device
        :param:
            -spi_no: select spi port
            -value : 32-bit, value to write into the slave device
                    - bit[31:29]: don't care
                    - bit28     : R/W (1->R, 0->W)
                    - bit[27:24]: command bits
                    - bit[23:20]: channel address bits
                    - bit[19:0] : control bits for other functions
            -cs_dly: cycle values of hold_time and setup_time, with high half-byte for the former and low half-byte for the latter
        :return:
            return the value of accessed register
        '''
        return self.channel.req_com("esp_wr_spidev %d 0x%x %d"%(spi_no, value, cs_dly))
