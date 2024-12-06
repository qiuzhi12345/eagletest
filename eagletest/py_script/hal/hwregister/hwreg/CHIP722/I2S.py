from hal.common import *
from hal.hwregister.hwreg.CHIP722.addr_base import *
class I2S(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.I2SCONF = I2SCONF(self.channel, self.chipv)
        self.I2SINT_RAW = I2SINT_RAW(self.channel, self.chipv)
        self.I2SINT_ST = I2SINT_ST(self.channel, self.chipv)
        self.I2SINT_ENA = I2SINT_ENA(self.channel, self.chipv)
        self.I2SINT_CLR = I2SINT_CLR(self.channel, self.chipv)
        self.I2STIMING = I2STIMING(self.channel, self.chipv)
        self.I2S_FIFO_CONF = I2S_FIFO_CONF(self.channel, self.chipv)
        self.I2SRXEOF_NUM = I2SRXEOF_NUM(self.channel, self.chipv)
        self.I2SCONF_SIGLE_DATA = I2SCONF_SIGLE_DATA(self.channel, self.chipv)
        self.I2SCONF_CHAN = I2SCONF_CHAN(self.channel, self.chipv)
        self.I2SOUT_LINK = I2SOUT_LINK(self.channel, self.chipv)
        self.I2SIN_LINK = I2SIN_LINK(self.channel, self.chipv)
        self.I2S_OUT_EOF_DES_ADDR = I2S_OUT_EOF_DES_ADDR(self.channel, self.chipv)
        self.I2S_IN_EOF_DES_ADDR = I2S_IN_EOF_DES_ADDR(self.channel, self.chipv)
        self.I2S_OUT_EOF_BFR_DES_ADDR = I2S_OUT_EOF_BFR_DES_ADDR(self.channel, self.chipv)
        self.I2S_AHB_TEST = I2S_AHB_TEST(self.channel, self.chipv)
        self.I2S_INLINK_DSCR = I2S_INLINK_DSCR(self.channel, self.chipv)
        self.I2S_INLINK_DSCR_BF0 = I2S_INLINK_DSCR_BF0(self.channel, self.chipv)
        self.I2S_INLINK_DSCR_BF1 = I2S_INLINK_DSCR_BF1(self.channel, self.chipv)
        self.I2S_OUTLINK_DSCR = I2S_OUTLINK_DSCR(self.channel, self.chipv)
        self.I2S_OUTLINK_DSCR_BF0 = I2S_OUTLINK_DSCR_BF0(self.channel, self.chipv)
        self.I2S_OUTLINK_DSCR_BF1 = I2S_OUTLINK_DSCR_BF1(self.channel, self.chipv)
        self.I2S_LC_CONF = I2S_LC_CONF(self.channel, self.chipv)
        self.I2S_OUTFIFO_PUSH = I2S_OUTFIFO_PUSH(self.channel, self.chipv)
        self.I2S_INFIFO_POP = I2S_INFIFO_POP(self.channel, self.chipv)
        self.I2S_LC_STATE0 = I2S_LC_STATE0(self.channel, self.chipv)
        self.I2S_LC_STATE1 = I2S_LC_STATE1(self.channel, self.chipv)
        self.I2S_LC_HUNG_CONF = I2S_LC_HUNG_CONF(self.channel, self.chipv)
        self.I2S_CVSD_CONF0 = I2S_CVSD_CONF0(self.channel, self.chipv)
        self.I2S_CVSD_CONF1 = I2S_CVSD_CONF1(self.channel, self.chipv)
        self.I2S_CVSD_CONF2 = I2S_CVSD_CONF2(self.channel, self.chipv)
        self.I2S_PLC_CONF0 = I2S_PLC_CONF0(self.channel, self.chipv)
        self.I2S_PLC_CONF1 = I2S_PLC_CONF1(self.channel, self.chipv)
        self.I2S_PLC_CONF2 = I2S_PLC_CONF2(self.channel, self.chipv)
        self.I2S_ESCO_CONF0 = I2S_ESCO_CONF0(self.channel, self.chipv)
        self.I2S_SCO_CONF0 = I2S_SCO_CONF0(self.channel, self.chipv)
        self.I2SCONF1 = I2SCONF1(self.channel, self.chipv)
        self.I2S_PD_CONF = I2S_PD_CONF(self.channel, self.chipv)
        self.I2SCONF2 = I2SCONF2(self.channel, self.chipv)
        self.I2S_CLKM_CONF = I2S_CLKM_CONF(self.channel, self.chipv)
        self.I2S_SAMPLE_RATE_CONF = I2S_SAMPLE_RATE_CONF(self.channel, self.chipv)
        self.I2S_PDM_CONF = I2S_PDM_CONF(self.channel, self.chipv)
        self.I2S_PDM_FREQ_CONF = I2S_PDM_FREQ_CONF(self.channel, self.chipv)
        self.I2S_STATE = I2S_STATE(self.channel, self.chipv)
        self.I2S_DATE = I2S_DATE(self.channel, self.chipv)
class I2SCONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x8
        self.__i2s_rx_reset_st_lsb = 29
        self.__i2s_rx_reset_st_msb = 29
        self.__reg_rx_big_endian_lsb = 28
        self.__reg_rx_big_endian_msb = 28
        self.__reg_tx_big_endian_lsb = 27
        self.__reg_tx_big_endian_msb = 27
        self.__pre_req_en_lsb = 26
        self.__pre_req_en_msb = 26
        self.__reg_rx_dma_equal_lsb = 25
        self.__reg_rx_dma_equal_msb = 25
        self.__reg_tx_dma_equal_lsb = 24
        self.__reg_tx_dma_equal_msb = 24
        self.__i2s_tx_reset_st_lsb = 23
        self.__i2s_tx_reset_st_msb = 23
        self.__i2s_rx_fifo_reset_st_lsb = 22
        self.__i2s_rx_fifo_reset_st_msb = 22
        self.__i2s_tx_fifo_reset_st_lsb = 21
        self.__i2s_tx_fifo_reset_st_msb = 21
        self.__reg_i2s_sig_loopback_lsb = 20
        self.__reg_i2s_sig_loopback_msb = 20
        self.__reg_rx_LSB_first_DMA_lsb = 19
        self.__reg_rx_LSB_first_DMA_msb = 19
        self.__reg_tx_LSB_first_DMA_lsb = 18
        self.__reg_tx_LSB_first_DMA_msb = 18
        self.__reg_rx_MSB_right_lsb = 17
        self.__reg_rx_MSB_right_msb = 17
        self.__reg_tx_MSB_right_lsb = 16
        self.__reg_tx_MSB_right_msb = 16
        self.__reg_i2s_rx_mono_lsb = 15
        self.__reg_i2s_rx_mono_msb = 15
        self.__reg_i2s_tx_mono_lsb = 14
        self.__reg_i2s_tx_mono_msb = 14
        self.__reg_i2s_rx_short_sync_lsb = 13
        self.__reg_i2s_rx_short_sync_msb = 13
        self.__reg_i2s_tx_short_sync_lsb = 12
        self.__reg_i2s_tx_short_sync_msb = 12
        self.__reg_rx_MSB_shift_lsb = 11
        self.__reg_rx_MSB_shift_msb = 11
        self.__reg_tx_MSB_shift_lsb = 10
        self.__reg_tx_MSB_shift_msb = 10
        self.__reg_rx_right_first_lsb = 9
        self.__reg_rx_right_first_msb = 9
        self.__reg_tx_right_first_lsb = 8
        self.__reg_tx_right_first_msb = 8
        self.__reg_rx_slave_mod_lsb = 7
        self.__reg_rx_slave_mod_msb = 7
        self.__reg_tx_slave_mod_lsb = 6
        self.__reg_tx_slave_mod_msb = 6
        self.__i2s_rx_start_lsb = 5
        self.__i2s_rx_start_msb = 5
        self.__i2s_tx_start_lsb = 4
        self.__i2s_tx_start_msb = 4
        self.__i2s_rx_fifo_reset_lsb = 3
        self.__i2s_rx_fifo_reset_msb = 3
        self.__i2s_tx_fifo_reset_lsb = 2
        self.__i2s_tx_fifo_reset_msb = 2
        self.__i2s_rx_reset_lsb = 1
        self.__i2s_rx_reset_msb = 1
        self.__i2s_tx_reset_lsb = 0
        self.__i2s_tx_reset_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_rx_reset_st(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_rx_reset_st_msb, self.__i2s_rx_reset_st_lsb)
    @i2s_rx_reset_st.setter
    def i2s_rx_reset_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_rx_reset_st_msb, self.__i2s_rx_reset_st_lsb, value)

    @property
    def reg_rx_big_endian(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_big_endian_msb, self.__reg_rx_big_endian_lsb)
    @reg_rx_big_endian.setter
    def reg_rx_big_endian(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_big_endian_msb, self.__reg_rx_big_endian_lsb, value)

    @property
    def reg_tx_big_endian(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_big_endian_msb, self.__reg_tx_big_endian_lsb)
    @reg_tx_big_endian.setter
    def reg_tx_big_endian(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_big_endian_msb, self.__reg_tx_big_endian_lsb, value)

    @property
    def pre_req_en(self):
        return self.__MEM.rdm(self.__addr, self.__pre_req_en_msb, self.__pre_req_en_lsb)
    @pre_req_en.setter
    def pre_req_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__pre_req_en_msb, self.__pre_req_en_lsb, value)

    @property
    def reg_rx_dma_equal(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_dma_equal_msb, self.__reg_rx_dma_equal_lsb)
    @reg_rx_dma_equal.setter
    def reg_rx_dma_equal(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_dma_equal_msb, self.__reg_rx_dma_equal_lsb, value)

    @property
    def reg_tx_dma_equal(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_dma_equal_msb, self.__reg_tx_dma_equal_lsb)
    @reg_tx_dma_equal.setter
    def reg_tx_dma_equal(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_dma_equal_msb, self.__reg_tx_dma_equal_lsb, value)

    @property
    def i2s_tx_reset_st(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_tx_reset_st_msb, self.__i2s_tx_reset_st_lsb)
    @i2s_tx_reset_st.setter
    def i2s_tx_reset_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_tx_reset_st_msb, self.__i2s_tx_reset_st_lsb, value)

    @property
    def i2s_rx_fifo_reset_st(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_rx_fifo_reset_st_msb, self.__i2s_rx_fifo_reset_st_lsb)
    @i2s_rx_fifo_reset_st.setter
    def i2s_rx_fifo_reset_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_rx_fifo_reset_st_msb, self.__i2s_rx_fifo_reset_st_lsb, value)

    @property
    def i2s_tx_fifo_reset_st(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_tx_fifo_reset_st_msb, self.__i2s_tx_fifo_reset_st_lsb)
    @i2s_tx_fifo_reset_st.setter
    def i2s_tx_fifo_reset_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_tx_fifo_reset_st_msb, self.__i2s_tx_fifo_reset_st_lsb, value)

    @property
    def reg_i2s_sig_loopback(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2s_sig_loopback_msb, self.__reg_i2s_sig_loopback_lsb)
    @reg_i2s_sig_loopback.setter
    def reg_i2s_sig_loopback(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2s_sig_loopback_msb, self.__reg_i2s_sig_loopback_lsb, value)

    @property
    def reg_rx_LSB_first_DMA(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_LSB_first_DMA_msb, self.__reg_rx_LSB_first_DMA_lsb)
    @reg_rx_LSB_first_DMA.setter
    def reg_rx_LSB_first_DMA(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_LSB_first_DMA_msb, self.__reg_rx_LSB_first_DMA_lsb, value)

    @property
    def reg_tx_LSB_first_DMA(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_LSB_first_DMA_msb, self.__reg_tx_LSB_first_DMA_lsb)
    @reg_tx_LSB_first_DMA.setter
    def reg_tx_LSB_first_DMA(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_LSB_first_DMA_msb, self.__reg_tx_LSB_first_DMA_lsb, value)

    @property
    def reg_rx_MSB_right(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_MSB_right_msb, self.__reg_rx_MSB_right_lsb)
    @reg_rx_MSB_right.setter
    def reg_rx_MSB_right(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_MSB_right_msb, self.__reg_rx_MSB_right_lsb, value)

    @property
    def reg_tx_MSB_right(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_MSB_right_msb, self.__reg_tx_MSB_right_lsb)
    @reg_tx_MSB_right.setter
    def reg_tx_MSB_right(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_MSB_right_msb, self.__reg_tx_MSB_right_lsb, value)

    @property
    def reg_i2s_rx_mono(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2s_rx_mono_msb, self.__reg_i2s_rx_mono_lsb)
    @reg_i2s_rx_mono.setter
    def reg_i2s_rx_mono(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2s_rx_mono_msb, self.__reg_i2s_rx_mono_lsb, value)

    @property
    def reg_i2s_tx_mono(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2s_tx_mono_msb, self.__reg_i2s_tx_mono_lsb)
    @reg_i2s_tx_mono.setter
    def reg_i2s_tx_mono(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2s_tx_mono_msb, self.__reg_i2s_tx_mono_lsb, value)

    @property
    def reg_i2s_rx_short_sync(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2s_rx_short_sync_msb, self.__reg_i2s_rx_short_sync_lsb)
    @reg_i2s_rx_short_sync.setter
    def reg_i2s_rx_short_sync(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2s_rx_short_sync_msb, self.__reg_i2s_rx_short_sync_lsb, value)

    @property
    def reg_i2s_tx_short_sync(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2s_tx_short_sync_msb, self.__reg_i2s_tx_short_sync_lsb)
    @reg_i2s_tx_short_sync.setter
    def reg_i2s_tx_short_sync(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2s_tx_short_sync_msb, self.__reg_i2s_tx_short_sync_lsb, value)

    @property
    def reg_rx_MSB_shift(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_MSB_shift_msb, self.__reg_rx_MSB_shift_lsb)
    @reg_rx_MSB_shift.setter
    def reg_rx_MSB_shift(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_MSB_shift_msb, self.__reg_rx_MSB_shift_lsb, value)

    @property
    def reg_tx_MSB_shift(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_MSB_shift_msb, self.__reg_tx_MSB_shift_lsb)
    @reg_tx_MSB_shift.setter
    def reg_tx_MSB_shift(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_MSB_shift_msb, self.__reg_tx_MSB_shift_lsb, value)

    @property
    def reg_rx_right_first(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_right_first_msb, self.__reg_rx_right_first_lsb)
    @reg_rx_right_first.setter
    def reg_rx_right_first(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_right_first_msb, self.__reg_rx_right_first_lsb, value)

    @property
    def reg_tx_right_first(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_right_first_msb, self.__reg_tx_right_first_lsb)
    @reg_tx_right_first.setter
    def reg_tx_right_first(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_right_first_msb, self.__reg_tx_right_first_lsb, value)

    @property
    def reg_rx_slave_mod(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_slave_mod_msb, self.__reg_rx_slave_mod_lsb)
    @reg_rx_slave_mod.setter
    def reg_rx_slave_mod(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_slave_mod_msb, self.__reg_rx_slave_mod_lsb, value)

    @property
    def reg_tx_slave_mod(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_slave_mod_msb, self.__reg_tx_slave_mod_lsb)
    @reg_tx_slave_mod.setter
    def reg_tx_slave_mod(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_slave_mod_msb, self.__reg_tx_slave_mod_lsb, value)

    @property
    def i2s_rx_start(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_rx_start_msb, self.__i2s_rx_start_lsb)
    @i2s_rx_start.setter
    def i2s_rx_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_rx_start_msb, self.__i2s_rx_start_lsb, value)

    @property
    def i2s_tx_start(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_tx_start_msb, self.__i2s_tx_start_lsb)
    @i2s_tx_start.setter
    def i2s_tx_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_tx_start_msb, self.__i2s_tx_start_lsb, value)

    @property
    def i2s_rx_fifo_reset(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_rx_fifo_reset_msb, self.__i2s_rx_fifo_reset_lsb)
    @i2s_rx_fifo_reset.setter
    def i2s_rx_fifo_reset(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_rx_fifo_reset_msb, self.__i2s_rx_fifo_reset_lsb, value)

    @property
    def i2s_tx_fifo_reset(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_tx_fifo_reset_msb, self.__i2s_tx_fifo_reset_lsb)
    @i2s_tx_fifo_reset.setter
    def i2s_tx_fifo_reset(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_tx_fifo_reset_msb, self.__i2s_tx_fifo_reset_lsb, value)

    @property
    def i2s_rx_reset(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_rx_reset_msb, self.__i2s_rx_reset_lsb)
    @i2s_rx_reset.setter
    def i2s_rx_reset(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_rx_reset_msb, self.__i2s_rx_reset_lsb, value)

    @property
    def i2s_tx_reset(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_tx_reset_msb, self.__i2s_tx_reset_lsb)
    @i2s_tx_reset.setter
    def i2s_tx_reset(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_tx_reset_msb, self.__i2s_tx_reset_lsb, value)
class I2SINT_RAW(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0xc
        self.__i2s_out_total_eof_int_raw_lsb = 16
        self.__i2s_out_total_eof_int_raw_msb = 16
        self.__i2s_in_dscr_empty_int_raw_lsb = 15
        self.__i2s_in_dscr_empty_int_raw_msb = 15
        self.__i2s_out_dscr_err_int_raw_lsb = 14
        self.__i2s_out_dscr_err_int_raw_msb = 14
        self.__i2s_in_dscr_err_int_raw_lsb = 13
        self.__i2s_in_dscr_err_int_raw_msb = 13
        self.__i2s_out_eof_int_raw_lsb = 12
        self.__i2s_out_eof_int_raw_msb = 12
        self.__i2s_out_done_int_raw_lsb = 11
        self.__i2s_out_done_int_raw_msb = 11
        self.__i2s_in_err_eof_int_raw_lsb = 10
        self.__i2s_in_err_eof_int_raw_msb = 10
        self.__i2s_in_suc_eof_int_raw_lsb = 9
        self.__i2s_in_suc_eof_int_raw_msb = 9
        self.__i2s_in_done_int_raw_lsb = 8
        self.__i2s_in_done_int_raw_msb = 8
        self.__i2s_tx_hung_int_raw_lsb = 7
        self.__i2s_tx_hung_int_raw_msb = 7
        self.__i2s_rx_hung_int_raw_lsb = 6
        self.__i2s_rx_hung_int_raw_msb = 6
        self.__i2s_tx_rempty_int_raw_lsb = 5
        self.__i2s_tx_rempty_int_raw_msb = 5
        self.__i2s_tx_wfull_int_raw_lsb = 4
        self.__i2s_tx_wfull_int_raw_msb = 4
        self.__i2s_rx_rempty_int_raw_lsb = 3
        self.__i2s_rx_rempty_int_raw_msb = 3
        self.__i2s_rx_wfull_int_raw_lsb = 2
        self.__i2s_rx_wfull_int_raw_msb = 2
        self.__i2s_tx_put_data_int_raw_lsb = 1
        self.__i2s_tx_put_data_int_raw_msb = 1
        self.__i2s_rx_take_data_int_raw_lsb = 0
        self.__i2s_rx_take_data_int_raw_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_out_total_eof_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_out_total_eof_int_raw_msb, self.__i2s_out_total_eof_int_raw_lsb)
    @i2s_out_total_eof_int_raw.setter
    def i2s_out_total_eof_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_out_total_eof_int_raw_msb, self.__i2s_out_total_eof_int_raw_lsb, value)

    @property
    def i2s_in_dscr_empty_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_in_dscr_empty_int_raw_msb, self.__i2s_in_dscr_empty_int_raw_lsb)
    @i2s_in_dscr_empty_int_raw.setter
    def i2s_in_dscr_empty_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_in_dscr_empty_int_raw_msb, self.__i2s_in_dscr_empty_int_raw_lsb, value)

    @property
    def i2s_out_dscr_err_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_out_dscr_err_int_raw_msb, self.__i2s_out_dscr_err_int_raw_lsb)
    @i2s_out_dscr_err_int_raw.setter
    def i2s_out_dscr_err_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_out_dscr_err_int_raw_msb, self.__i2s_out_dscr_err_int_raw_lsb, value)

    @property
    def i2s_in_dscr_err_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_in_dscr_err_int_raw_msb, self.__i2s_in_dscr_err_int_raw_lsb)
    @i2s_in_dscr_err_int_raw.setter
    def i2s_in_dscr_err_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_in_dscr_err_int_raw_msb, self.__i2s_in_dscr_err_int_raw_lsb, value)

    @property
    def i2s_out_eof_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_out_eof_int_raw_msb, self.__i2s_out_eof_int_raw_lsb)
    @i2s_out_eof_int_raw.setter
    def i2s_out_eof_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_out_eof_int_raw_msb, self.__i2s_out_eof_int_raw_lsb, value)

    @property
    def i2s_out_done_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_out_done_int_raw_msb, self.__i2s_out_done_int_raw_lsb)
    @i2s_out_done_int_raw.setter
    def i2s_out_done_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_out_done_int_raw_msb, self.__i2s_out_done_int_raw_lsb, value)

    @property
    def i2s_in_err_eof_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_in_err_eof_int_raw_msb, self.__i2s_in_err_eof_int_raw_lsb)
    @i2s_in_err_eof_int_raw.setter
    def i2s_in_err_eof_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_in_err_eof_int_raw_msb, self.__i2s_in_err_eof_int_raw_lsb, value)

    @property
    def i2s_in_suc_eof_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_in_suc_eof_int_raw_msb, self.__i2s_in_suc_eof_int_raw_lsb)
    @i2s_in_suc_eof_int_raw.setter
    def i2s_in_suc_eof_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_in_suc_eof_int_raw_msb, self.__i2s_in_suc_eof_int_raw_lsb, value)

    @property
    def i2s_in_done_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_in_done_int_raw_msb, self.__i2s_in_done_int_raw_lsb)
    @i2s_in_done_int_raw.setter
    def i2s_in_done_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_in_done_int_raw_msb, self.__i2s_in_done_int_raw_lsb, value)

    @property
    def i2s_tx_hung_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_tx_hung_int_raw_msb, self.__i2s_tx_hung_int_raw_lsb)
    @i2s_tx_hung_int_raw.setter
    def i2s_tx_hung_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_tx_hung_int_raw_msb, self.__i2s_tx_hung_int_raw_lsb, value)

    @property
    def i2s_rx_hung_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_rx_hung_int_raw_msb, self.__i2s_rx_hung_int_raw_lsb)
    @i2s_rx_hung_int_raw.setter
    def i2s_rx_hung_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_rx_hung_int_raw_msb, self.__i2s_rx_hung_int_raw_lsb, value)

    @property
    def i2s_tx_rempty_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_tx_rempty_int_raw_msb, self.__i2s_tx_rempty_int_raw_lsb)
    @i2s_tx_rempty_int_raw.setter
    def i2s_tx_rempty_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_tx_rempty_int_raw_msb, self.__i2s_tx_rempty_int_raw_lsb, value)

    @property
    def i2s_tx_wfull_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_tx_wfull_int_raw_msb, self.__i2s_tx_wfull_int_raw_lsb)
    @i2s_tx_wfull_int_raw.setter
    def i2s_tx_wfull_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_tx_wfull_int_raw_msb, self.__i2s_tx_wfull_int_raw_lsb, value)

    @property
    def i2s_rx_rempty_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_rx_rempty_int_raw_msb, self.__i2s_rx_rempty_int_raw_lsb)
    @i2s_rx_rempty_int_raw.setter
    def i2s_rx_rempty_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_rx_rempty_int_raw_msb, self.__i2s_rx_rempty_int_raw_lsb, value)

    @property
    def i2s_rx_wfull_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_rx_wfull_int_raw_msb, self.__i2s_rx_wfull_int_raw_lsb)
    @i2s_rx_wfull_int_raw.setter
    def i2s_rx_wfull_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_rx_wfull_int_raw_msb, self.__i2s_rx_wfull_int_raw_lsb, value)

    @property
    def i2s_tx_put_data_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_tx_put_data_int_raw_msb, self.__i2s_tx_put_data_int_raw_lsb)
    @i2s_tx_put_data_int_raw.setter
    def i2s_tx_put_data_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_tx_put_data_int_raw_msb, self.__i2s_tx_put_data_int_raw_lsb, value)

    @property
    def i2s_rx_take_data_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_rx_take_data_int_raw_msb, self.__i2s_rx_take_data_int_raw_lsb)
    @i2s_rx_take_data_int_raw.setter
    def i2s_rx_take_data_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_rx_take_data_int_raw_msb, self.__i2s_rx_take_data_int_raw_lsb, value)
class I2SINT_ST(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x10
        self.__i2s_out_total_eof_int_st_lsb = 16
        self.__i2s_out_total_eof_int_st_msb = 16
        self.__i2s_in_dscr_empty_int_st_lsb = 15
        self.__i2s_in_dscr_empty_int_st_msb = 15
        self.__i2s_out_dscr_err_int_st_lsb = 14
        self.__i2s_out_dscr_err_int_st_msb = 14
        self.__i2s_in_dscr_err_int_st_lsb = 13
        self.__i2s_in_dscr_err_int_st_msb = 13
        self.__i2s_out_eof_int_st_lsb = 12
        self.__i2s_out_eof_int_st_msb = 12
        self.__i2s_out_done_int_st_lsb = 11
        self.__i2s_out_done_int_st_msb = 11
        self.__i2s_in_err_eof_int_st_lsb = 10
        self.__i2s_in_err_eof_int_st_msb = 10
        self.__i2s_in_suc_eof_int_st_lsb = 9
        self.__i2s_in_suc_eof_int_st_msb = 9
        self.__i2s_in_done_int_st_lsb = 8
        self.__i2s_in_done_int_st_msb = 8
        self.__i2s_tx_hung_int_st_lsb = 7
        self.__i2s_tx_hung_int_st_msb = 7
        self.__i2s_rx_hung_int_st_lsb = 6
        self.__i2s_rx_hung_int_st_msb = 6
        self.__i2s_tx_rempty_int_st_lsb = 5
        self.__i2s_tx_rempty_int_st_msb = 5
        self.__i2s_tx_wfull_int_st_lsb = 4
        self.__i2s_tx_wfull_int_st_msb = 4
        self.__i2s_rx_rempty_int_st_lsb = 3
        self.__i2s_rx_rempty_int_st_msb = 3
        self.__i2s_rx_wfull_int_st_lsb = 2
        self.__i2s_rx_wfull_int_st_msb = 2
        self.__i2s_tx_put_data_int_st_lsb = 1
        self.__i2s_tx_put_data_int_st_msb = 1
        self.__i2s_rx_take_data_int_st_lsb = 0
        self.__i2s_rx_take_data_int_st_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_out_total_eof_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_out_total_eof_int_st_msb, self.__i2s_out_total_eof_int_st_lsb)
    @i2s_out_total_eof_int_st.setter
    def i2s_out_total_eof_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_out_total_eof_int_st_msb, self.__i2s_out_total_eof_int_st_lsb, value)

    @property
    def i2s_in_dscr_empty_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_in_dscr_empty_int_st_msb, self.__i2s_in_dscr_empty_int_st_lsb)
    @i2s_in_dscr_empty_int_st.setter
    def i2s_in_dscr_empty_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_in_dscr_empty_int_st_msb, self.__i2s_in_dscr_empty_int_st_lsb, value)

    @property
    def i2s_out_dscr_err_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_out_dscr_err_int_st_msb, self.__i2s_out_dscr_err_int_st_lsb)
    @i2s_out_dscr_err_int_st.setter
    def i2s_out_dscr_err_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_out_dscr_err_int_st_msb, self.__i2s_out_dscr_err_int_st_lsb, value)

    @property
    def i2s_in_dscr_err_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_in_dscr_err_int_st_msb, self.__i2s_in_dscr_err_int_st_lsb)
    @i2s_in_dscr_err_int_st.setter
    def i2s_in_dscr_err_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_in_dscr_err_int_st_msb, self.__i2s_in_dscr_err_int_st_lsb, value)

    @property
    def i2s_out_eof_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_out_eof_int_st_msb, self.__i2s_out_eof_int_st_lsb)
    @i2s_out_eof_int_st.setter
    def i2s_out_eof_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_out_eof_int_st_msb, self.__i2s_out_eof_int_st_lsb, value)

    @property
    def i2s_out_done_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_out_done_int_st_msb, self.__i2s_out_done_int_st_lsb)
    @i2s_out_done_int_st.setter
    def i2s_out_done_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_out_done_int_st_msb, self.__i2s_out_done_int_st_lsb, value)

    @property
    def i2s_in_err_eof_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_in_err_eof_int_st_msb, self.__i2s_in_err_eof_int_st_lsb)
    @i2s_in_err_eof_int_st.setter
    def i2s_in_err_eof_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_in_err_eof_int_st_msb, self.__i2s_in_err_eof_int_st_lsb, value)

    @property
    def i2s_in_suc_eof_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_in_suc_eof_int_st_msb, self.__i2s_in_suc_eof_int_st_lsb)
    @i2s_in_suc_eof_int_st.setter
    def i2s_in_suc_eof_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_in_suc_eof_int_st_msb, self.__i2s_in_suc_eof_int_st_lsb, value)

    @property
    def i2s_in_done_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_in_done_int_st_msb, self.__i2s_in_done_int_st_lsb)
    @i2s_in_done_int_st.setter
    def i2s_in_done_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_in_done_int_st_msb, self.__i2s_in_done_int_st_lsb, value)

    @property
    def i2s_tx_hung_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_tx_hung_int_st_msb, self.__i2s_tx_hung_int_st_lsb)
    @i2s_tx_hung_int_st.setter
    def i2s_tx_hung_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_tx_hung_int_st_msb, self.__i2s_tx_hung_int_st_lsb, value)

    @property
    def i2s_rx_hung_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_rx_hung_int_st_msb, self.__i2s_rx_hung_int_st_lsb)
    @i2s_rx_hung_int_st.setter
    def i2s_rx_hung_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_rx_hung_int_st_msb, self.__i2s_rx_hung_int_st_lsb, value)

    @property
    def i2s_tx_rempty_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_tx_rempty_int_st_msb, self.__i2s_tx_rempty_int_st_lsb)
    @i2s_tx_rempty_int_st.setter
    def i2s_tx_rempty_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_tx_rempty_int_st_msb, self.__i2s_tx_rempty_int_st_lsb, value)

    @property
    def i2s_tx_wfull_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_tx_wfull_int_st_msb, self.__i2s_tx_wfull_int_st_lsb)
    @i2s_tx_wfull_int_st.setter
    def i2s_tx_wfull_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_tx_wfull_int_st_msb, self.__i2s_tx_wfull_int_st_lsb, value)

    @property
    def i2s_rx_rempty_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_rx_rempty_int_st_msb, self.__i2s_rx_rempty_int_st_lsb)
    @i2s_rx_rempty_int_st.setter
    def i2s_rx_rempty_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_rx_rempty_int_st_msb, self.__i2s_rx_rempty_int_st_lsb, value)

    @property
    def i2s_rx_wfull_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_rx_wfull_int_st_msb, self.__i2s_rx_wfull_int_st_lsb)
    @i2s_rx_wfull_int_st.setter
    def i2s_rx_wfull_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_rx_wfull_int_st_msb, self.__i2s_rx_wfull_int_st_lsb, value)

    @property
    def i2s_tx_put_data_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_tx_put_data_int_st_msb, self.__i2s_tx_put_data_int_st_lsb)
    @i2s_tx_put_data_int_st.setter
    def i2s_tx_put_data_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_tx_put_data_int_st_msb, self.__i2s_tx_put_data_int_st_lsb, value)

    @property
    def i2s_rx_take_data_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_rx_take_data_int_st_msb, self.__i2s_rx_take_data_int_st_lsb)
    @i2s_rx_take_data_int_st.setter
    def i2s_rx_take_data_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_rx_take_data_int_st_msb, self.__i2s_rx_take_data_int_st_lsb, value)
class I2SINT_ENA(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x14
        self.__i2s_out_total_eof_int_ena_lsb = 16
        self.__i2s_out_total_eof_int_ena_msb = 16
        self.__i2s_in_dscr_empty_int_ena_lsb = 15
        self.__i2s_in_dscr_empty_int_ena_msb = 15
        self.__i2s_out_dscr_err_int_ena_lsb = 14
        self.__i2s_out_dscr_err_int_ena_msb = 14
        self.__i2s_in_dscr_err_int_ena_lsb = 13
        self.__i2s_in_dscr_err_int_ena_msb = 13
        self.__i2s_out_eof_int_ena_lsb = 12
        self.__i2s_out_eof_int_ena_msb = 12
        self.__i2s_out_done_int_ena_lsb = 11
        self.__i2s_out_done_int_ena_msb = 11
        self.__i2s_in_err_eof_int_ena_lsb = 10
        self.__i2s_in_err_eof_int_ena_msb = 10
        self.__i2s_in_suc_eof_int_ena_lsb = 9
        self.__i2s_in_suc_eof_int_ena_msb = 9
        self.__i2s_in_done_int_ena_lsb = 8
        self.__i2s_in_done_int_ena_msb = 8
        self.__i2s_tx_hung_int_ena_lsb = 7
        self.__i2s_tx_hung_int_ena_msb = 7
        self.__i2s_rx_hung_int_ena_lsb = 6
        self.__i2s_rx_hung_int_ena_msb = 6
        self.__i2s_tx_rempty_int_ena_lsb = 5
        self.__i2s_tx_rempty_int_ena_msb = 5
        self.__i2s_tx_wfull_int_ena_lsb = 4
        self.__i2s_tx_wfull_int_ena_msb = 4
        self.__i2s_rx_rempty_int_ena_lsb = 3
        self.__i2s_rx_rempty_int_ena_msb = 3
        self.__i2s_rx_wfull_int_ena_lsb = 2
        self.__i2s_rx_wfull_int_ena_msb = 2
        self.__i2s_tx_put_data_int_ena_lsb = 1
        self.__i2s_tx_put_data_int_ena_msb = 1
        self.__i2s_rx_take_data_int_ena_lsb = 0
        self.__i2s_rx_take_data_int_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_out_total_eof_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_out_total_eof_int_ena_msb, self.__i2s_out_total_eof_int_ena_lsb)
    @i2s_out_total_eof_int_ena.setter
    def i2s_out_total_eof_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_out_total_eof_int_ena_msb, self.__i2s_out_total_eof_int_ena_lsb, value)

    @property
    def i2s_in_dscr_empty_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_in_dscr_empty_int_ena_msb, self.__i2s_in_dscr_empty_int_ena_lsb)
    @i2s_in_dscr_empty_int_ena.setter
    def i2s_in_dscr_empty_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_in_dscr_empty_int_ena_msb, self.__i2s_in_dscr_empty_int_ena_lsb, value)

    @property
    def i2s_out_dscr_err_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_out_dscr_err_int_ena_msb, self.__i2s_out_dscr_err_int_ena_lsb)
    @i2s_out_dscr_err_int_ena.setter
    def i2s_out_dscr_err_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_out_dscr_err_int_ena_msb, self.__i2s_out_dscr_err_int_ena_lsb, value)

    @property
    def i2s_in_dscr_err_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_in_dscr_err_int_ena_msb, self.__i2s_in_dscr_err_int_ena_lsb)
    @i2s_in_dscr_err_int_ena.setter
    def i2s_in_dscr_err_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_in_dscr_err_int_ena_msb, self.__i2s_in_dscr_err_int_ena_lsb, value)

    @property
    def i2s_out_eof_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_out_eof_int_ena_msb, self.__i2s_out_eof_int_ena_lsb)
    @i2s_out_eof_int_ena.setter
    def i2s_out_eof_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_out_eof_int_ena_msb, self.__i2s_out_eof_int_ena_lsb, value)

    @property
    def i2s_out_done_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_out_done_int_ena_msb, self.__i2s_out_done_int_ena_lsb)
    @i2s_out_done_int_ena.setter
    def i2s_out_done_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_out_done_int_ena_msb, self.__i2s_out_done_int_ena_lsb, value)

    @property
    def i2s_in_err_eof_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_in_err_eof_int_ena_msb, self.__i2s_in_err_eof_int_ena_lsb)
    @i2s_in_err_eof_int_ena.setter
    def i2s_in_err_eof_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_in_err_eof_int_ena_msb, self.__i2s_in_err_eof_int_ena_lsb, value)

    @property
    def i2s_in_suc_eof_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_in_suc_eof_int_ena_msb, self.__i2s_in_suc_eof_int_ena_lsb)
    @i2s_in_suc_eof_int_ena.setter
    def i2s_in_suc_eof_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_in_suc_eof_int_ena_msb, self.__i2s_in_suc_eof_int_ena_lsb, value)

    @property
    def i2s_in_done_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_in_done_int_ena_msb, self.__i2s_in_done_int_ena_lsb)
    @i2s_in_done_int_ena.setter
    def i2s_in_done_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_in_done_int_ena_msb, self.__i2s_in_done_int_ena_lsb, value)

    @property
    def i2s_tx_hung_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_tx_hung_int_ena_msb, self.__i2s_tx_hung_int_ena_lsb)
    @i2s_tx_hung_int_ena.setter
    def i2s_tx_hung_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_tx_hung_int_ena_msb, self.__i2s_tx_hung_int_ena_lsb, value)

    @property
    def i2s_rx_hung_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_rx_hung_int_ena_msb, self.__i2s_rx_hung_int_ena_lsb)
    @i2s_rx_hung_int_ena.setter
    def i2s_rx_hung_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_rx_hung_int_ena_msb, self.__i2s_rx_hung_int_ena_lsb, value)

    @property
    def i2s_tx_rempty_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_tx_rempty_int_ena_msb, self.__i2s_tx_rempty_int_ena_lsb)
    @i2s_tx_rempty_int_ena.setter
    def i2s_tx_rempty_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_tx_rempty_int_ena_msb, self.__i2s_tx_rempty_int_ena_lsb, value)

    @property
    def i2s_tx_wfull_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_tx_wfull_int_ena_msb, self.__i2s_tx_wfull_int_ena_lsb)
    @i2s_tx_wfull_int_ena.setter
    def i2s_tx_wfull_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_tx_wfull_int_ena_msb, self.__i2s_tx_wfull_int_ena_lsb, value)

    @property
    def i2s_rx_rempty_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_rx_rempty_int_ena_msb, self.__i2s_rx_rempty_int_ena_lsb)
    @i2s_rx_rempty_int_ena.setter
    def i2s_rx_rempty_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_rx_rempty_int_ena_msb, self.__i2s_rx_rempty_int_ena_lsb, value)

    @property
    def i2s_rx_wfull_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_rx_wfull_int_ena_msb, self.__i2s_rx_wfull_int_ena_lsb)
    @i2s_rx_wfull_int_ena.setter
    def i2s_rx_wfull_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_rx_wfull_int_ena_msb, self.__i2s_rx_wfull_int_ena_lsb, value)

    @property
    def i2s_tx_put_data_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_tx_put_data_int_ena_msb, self.__i2s_tx_put_data_int_ena_lsb)
    @i2s_tx_put_data_int_ena.setter
    def i2s_tx_put_data_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_tx_put_data_int_ena_msb, self.__i2s_tx_put_data_int_ena_lsb, value)

    @property
    def i2s_rx_take_data_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_rx_take_data_int_ena_msb, self.__i2s_rx_take_data_int_ena_lsb)
    @i2s_rx_take_data_int_ena.setter
    def i2s_rx_take_data_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_rx_take_data_int_ena_msb, self.__i2s_rx_take_data_int_ena_lsb, value)
class I2SINT_CLR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x18
        self.__i2s_out_total_eof_int_clr_lsb = 16
        self.__i2s_out_total_eof_int_clr_msb = 16
        self.__i2s_in_dscr_empty_int_clr_lsb = 15
        self.__i2s_in_dscr_empty_int_clr_msb = 15
        self.__i2s_out_dscr_err_int_clr_lsb = 14
        self.__i2s_out_dscr_err_int_clr_msb = 14
        self.__i2s_in_dscr_err_int_clr_lsb = 13
        self.__i2s_in_dscr_err_int_clr_msb = 13
        self.__i2s_out_eof_int_clr_lsb = 12
        self.__i2s_out_eof_int_clr_msb = 12
        self.__i2s_out_done_int_clr_lsb = 11
        self.__i2s_out_done_int_clr_msb = 11
        self.__i2s_in_err_eof_int_clr_lsb = 10
        self.__i2s_in_err_eof_int_clr_msb = 10
        self.__i2s_in_suc_eof_int_clr_lsb = 9
        self.__i2s_in_suc_eof_int_clr_msb = 9
        self.__i2s_in_done_int_clr_lsb = 8
        self.__i2s_in_done_int_clr_msb = 8
        self.__i2s_tx_hung_int_clr_lsb = 7
        self.__i2s_tx_hung_int_clr_msb = 7
        self.__i2s_rx_hung_int_clr_lsb = 6
        self.__i2s_rx_hung_int_clr_msb = 6
        self.__i2s_tx_rempty_int_clr_lsb = 5
        self.__i2s_tx_rempty_int_clr_msb = 5
        self.__i2s_tx_wfull_int_clr_lsb = 4
        self.__i2s_tx_wfull_int_clr_msb = 4
        self.__i2s_rx_rempty_int_clr_lsb = 3
        self.__i2s_rx_rempty_int_clr_msb = 3
        self.__i2s_rx_wfull_int_clr_lsb = 2
        self.__i2s_rx_wfull_int_clr_msb = 2
        self.__i2s_put_data_int_clr_lsb = 1
        self.__i2s_put_data_int_clr_msb = 1
        self.__i2s_take_data_int_clr_lsb = 0
        self.__i2s_take_data_int_clr_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_out_total_eof_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_out_total_eof_int_clr_msb, self.__i2s_out_total_eof_int_clr_lsb)
    @i2s_out_total_eof_int_clr.setter
    def i2s_out_total_eof_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_out_total_eof_int_clr_msb, self.__i2s_out_total_eof_int_clr_lsb, value)

    @property
    def i2s_in_dscr_empty_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_in_dscr_empty_int_clr_msb, self.__i2s_in_dscr_empty_int_clr_lsb)
    @i2s_in_dscr_empty_int_clr.setter
    def i2s_in_dscr_empty_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_in_dscr_empty_int_clr_msb, self.__i2s_in_dscr_empty_int_clr_lsb, value)

    @property
    def i2s_out_dscr_err_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_out_dscr_err_int_clr_msb, self.__i2s_out_dscr_err_int_clr_lsb)
    @i2s_out_dscr_err_int_clr.setter
    def i2s_out_dscr_err_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_out_dscr_err_int_clr_msb, self.__i2s_out_dscr_err_int_clr_lsb, value)

    @property
    def i2s_in_dscr_err_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_in_dscr_err_int_clr_msb, self.__i2s_in_dscr_err_int_clr_lsb)
    @i2s_in_dscr_err_int_clr.setter
    def i2s_in_dscr_err_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_in_dscr_err_int_clr_msb, self.__i2s_in_dscr_err_int_clr_lsb, value)

    @property
    def i2s_out_eof_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_out_eof_int_clr_msb, self.__i2s_out_eof_int_clr_lsb)
    @i2s_out_eof_int_clr.setter
    def i2s_out_eof_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_out_eof_int_clr_msb, self.__i2s_out_eof_int_clr_lsb, value)

    @property
    def i2s_out_done_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_out_done_int_clr_msb, self.__i2s_out_done_int_clr_lsb)
    @i2s_out_done_int_clr.setter
    def i2s_out_done_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_out_done_int_clr_msb, self.__i2s_out_done_int_clr_lsb, value)

    @property
    def i2s_in_err_eof_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_in_err_eof_int_clr_msb, self.__i2s_in_err_eof_int_clr_lsb)
    @i2s_in_err_eof_int_clr.setter
    def i2s_in_err_eof_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_in_err_eof_int_clr_msb, self.__i2s_in_err_eof_int_clr_lsb, value)

    @property
    def i2s_in_suc_eof_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_in_suc_eof_int_clr_msb, self.__i2s_in_suc_eof_int_clr_lsb)
    @i2s_in_suc_eof_int_clr.setter
    def i2s_in_suc_eof_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_in_suc_eof_int_clr_msb, self.__i2s_in_suc_eof_int_clr_lsb, value)

    @property
    def i2s_in_done_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_in_done_int_clr_msb, self.__i2s_in_done_int_clr_lsb)
    @i2s_in_done_int_clr.setter
    def i2s_in_done_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_in_done_int_clr_msb, self.__i2s_in_done_int_clr_lsb, value)

    @property
    def i2s_tx_hung_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_tx_hung_int_clr_msb, self.__i2s_tx_hung_int_clr_lsb)
    @i2s_tx_hung_int_clr.setter
    def i2s_tx_hung_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_tx_hung_int_clr_msb, self.__i2s_tx_hung_int_clr_lsb, value)

    @property
    def i2s_rx_hung_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_rx_hung_int_clr_msb, self.__i2s_rx_hung_int_clr_lsb)
    @i2s_rx_hung_int_clr.setter
    def i2s_rx_hung_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_rx_hung_int_clr_msb, self.__i2s_rx_hung_int_clr_lsb, value)

    @property
    def i2s_tx_rempty_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_tx_rempty_int_clr_msb, self.__i2s_tx_rempty_int_clr_lsb)
    @i2s_tx_rempty_int_clr.setter
    def i2s_tx_rempty_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_tx_rempty_int_clr_msb, self.__i2s_tx_rempty_int_clr_lsb, value)

    @property
    def i2s_tx_wfull_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_tx_wfull_int_clr_msb, self.__i2s_tx_wfull_int_clr_lsb)
    @i2s_tx_wfull_int_clr.setter
    def i2s_tx_wfull_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_tx_wfull_int_clr_msb, self.__i2s_tx_wfull_int_clr_lsb, value)

    @property
    def i2s_rx_rempty_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_rx_rempty_int_clr_msb, self.__i2s_rx_rempty_int_clr_lsb)
    @i2s_rx_rempty_int_clr.setter
    def i2s_rx_rempty_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_rx_rempty_int_clr_msb, self.__i2s_rx_rempty_int_clr_lsb, value)

    @property
    def i2s_rx_wfull_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_rx_wfull_int_clr_msb, self.__i2s_rx_wfull_int_clr_lsb)
    @i2s_rx_wfull_int_clr.setter
    def i2s_rx_wfull_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_rx_wfull_int_clr_msb, self.__i2s_rx_wfull_int_clr_lsb, value)

    @property
    def i2s_put_data_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_put_data_int_clr_msb, self.__i2s_put_data_int_clr_lsb)
    @i2s_put_data_int_clr.setter
    def i2s_put_data_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_put_data_int_clr_msb, self.__i2s_put_data_int_clr_lsb, value)

    @property
    def i2s_take_data_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_take_data_int_clr_msb, self.__i2s_take_data_int_clr_lsb)
    @i2s_take_data_int_clr.setter
    def i2s_take_data_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_take_data_int_clr_msb, self.__i2s_take_data_int_clr_lsb, value)
class I2STIMING(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x1c
        self.__reg_tx_bck_in_inv_lsb = 24
        self.__reg_tx_bck_in_inv_msb = 24
        self.__reg_data_enable_delay_lsb = 22
        self.__reg_data_enable_delay_msb = 23
        self.__reg_rx_dsync_sw_lsb = 21
        self.__reg_rx_dsync_sw_msb = 21
        self.__reg_tx_dsync_sw_lsb = 20
        self.__reg_tx_dsync_sw_msb = 20
        self.__reg_rx_bck_out_delay_lsb = 18
        self.__reg_rx_bck_out_delay_msb = 19
        self.__reg_rx_ws_out_delay_lsb = 16
        self.__reg_rx_ws_out_delay_msb = 17
        self.__reg_tx_sd_out_delay_lsb = 14
        self.__reg_tx_sd_out_delay_msb = 15
        self.__reg_tx_ws_out_delay_lsb = 12
        self.__reg_tx_ws_out_delay_msb = 13
        self.__reg_tx_bck_out_delay_lsb = 10
        self.__reg_tx_bck_out_delay_msb = 11
        self.__reg_rx_sd_in_delay_lsb = 8
        self.__reg_rx_sd_in_delay_msb = 9
        self.__reg_rx_ws_in_delay_lsb = 6
        self.__reg_rx_ws_in_delay_msb = 7
        self.__reg_rx_bck_in_delay_lsb = 4
        self.__reg_rx_bck_in_delay_msb = 5
        self.__reg_tx_ws_in_delay_lsb = 2
        self.__reg_tx_ws_in_delay_msb = 3
        self.__reg_tx_bck_in_delay_lsb = 0
        self.__reg_tx_bck_in_delay_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_bck_in_inv(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_bck_in_inv_msb, self.__reg_tx_bck_in_inv_lsb)
    @reg_tx_bck_in_inv.setter
    def reg_tx_bck_in_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_bck_in_inv_msb, self.__reg_tx_bck_in_inv_lsb, value)

    @property
    def reg_data_enable_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_data_enable_delay_msb, self.__reg_data_enable_delay_lsb)
    @reg_data_enable_delay.setter
    def reg_data_enable_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_data_enable_delay_msb, self.__reg_data_enable_delay_lsb, value)

    @property
    def reg_rx_dsync_sw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_dsync_sw_msb, self.__reg_rx_dsync_sw_lsb)
    @reg_rx_dsync_sw.setter
    def reg_rx_dsync_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_dsync_sw_msb, self.__reg_rx_dsync_sw_lsb, value)

    @property
    def reg_tx_dsync_sw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_dsync_sw_msb, self.__reg_tx_dsync_sw_lsb)
    @reg_tx_dsync_sw.setter
    def reg_tx_dsync_sw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_dsync_sw_msb, self.__reg_tx_dsync_sw_lsb, value)

    @property
    def reg_rx_bck_out_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_bck_out_delay_msb, self.__reg_rx_bck_out_delay_lsb)
    @reg_rx_bck_out_delay.setter
    def reg_rx_bck_out_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_bck_out_delay_msb, self.__reg_rx_bck_out_delay_lsb, value)

    @property
    def reg_rx_ws_out_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_ws_out_delay_msb, self.__reg_rx_ws_out_delay_lsb)
    @reg_rx_ws_out_delay.setter
    def reg_rx_ws_out_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_ws_out_delay_msb, self.__reg_rx_ws_out_delay_lsb, value)

    @property
    def reg_tx_sd_out_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_sd_out_delay_msb, self.__reg_tx_sd_out_delay_lsb)
    @reg_tx_sd_out_delay.setter
    def reg_tx_sd_out_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_sd_out_delay_msb, self.__reg_tx_sd_out_delay_lsb, value)

    @property
    def reg_tx_ws_out_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_ws_out_delay_msb, self.__reg_tx_ws_out_delay_lsb)
    @reg_tx_ws_out_delay.setter
    def reg_tx_ws_out_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_ws_out_delay_msb, self.__reg_tx_ws_out_delay_lsb, value)

    @property
    def reg_tx_bck_out_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_bck_out_delay_msb, self.__reg_tx_bck_out_delay_lsb)
    @reg_tx_bck_out_delay.setter
    def reg_tx_bck_out_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_bck_out_delay_msb, self.__reg_tx_bck_out_delay_lsb, value)

    @property
    def reg_rx_sd_in_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_sd_in_delay_msb, self.__reg_rx_sd_in_delay_lsb)
    @reg_rx_sd_in_delay.setter
    def reg_rx_sd_in_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_sd_in_delay_msb, self.__reg_rx_sd_in_delay_lsb, value)

    @property
    def reg_rx_ws_in_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_ws_in_delay_msb, self.__reg_rx_ws_in_delay_lsb)
    @reg_rx_ws_in_delay.setter
    def reg_rx_ws_in_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_ws_in_delay_msb, self.__reg_rx_ws_in_delay_lsb, value)

    @property
    def reg_rx_bck_in_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_bck_in_delay_msb, self.__reg_rx_bck_in_delay_lsb)
    @reg_rx_bck_in_delay.setter
    def reg_rx_bck_in_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_bck_in_delay_msb, self.__reg_rx_bck_in_delay_lsb, value)

    @property
    def reg_tx_ws_in_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_ws_in_delay_msb, self.__reg_tx_ws_in_delay_lsb)
    @reg_tx_ws_in_delay.setter
    def reg_tx_ws_in_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_ws_in_delay_msb, self.__reg_tx_ws_in_delay_lsb, value)

    @property
    def reg_tx_bck_in_delay(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_bck_in_delay_msb, self.__reg_tx_bck_in_delay_lsb)
    @reg_tx_bck_in_delay.setter
    def reg_tx_bck_in_delay(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_bck_in_delay_msb, self.__reg_tx_bck_in_delay_lsb, value)
class I2S_FIFO_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x20
        self.__reg_i2s_tx_24msb_en_lsb = 23
        self.__reg_i2s_tx_24msb_en_msb = 23
        self.__reg_i2s_rx_24msb_en_lsb = 22
        self.__reg_i2s_rx_24msb_en_msb = 22
        self.__reg_i2s_rx_fifo_sync_lsb = 21
        self.__reg_i2s_rx_fifo_sync_msb = 21
        self.__reg_i2s_rx_fifo_mod_force_en_lsb = 20
        self.__reg_i2s_rx_fifo_mod_force_en_msb = 20
        self.__reg_i2s_tx_fifo_mod_force_en_lsb = 19
        self.__reg_i2s_tx_fifo_mod_force_en_msb = 19
        self.__reg_i2s_rx_fifo_mod_lsb = 16
        self.__reg_i2s_rx_fifo_mod_msb = 18
        self.__reg_i2s_tx_fifo_mod_lsb = 13
        self.__reg_i2s_tx_fifo_mod_msb = 15
        self.__reg_i2s_dscr_en_lsb = 12
        self.__reg_i2s_dscr_en_msb = 12
        self.__reg_i2s_tx_data_num_lsb = 6
        self.__reg_i2s_tx_data_num_msb = 11
        self.__reg_i2s_rx_data_num_lsb = 0
        self.__reg_i2s_rx_data_num_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_i2s_tx_24msb_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2s_tx_24msb_en_msb, self.__reg_i2s_tx_24msb_en_lsb)
    @reg_i2s_tx_24msb_en.setter
    def reg_i2s_tx_24msb_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2s_tx_24msb_en_msb, self.__reg_i2s_tx_24msb_en_lsb, value)

    @property
    def reg_i2s_rx_24msb_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2s_rx_24msb_en_msb, self.__reg_i2s_rx_24msb_en_lsb)
    @reg_i2s_rx_24msb_en.setter
    def reg_i2s_rx_24msb_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2s_rx_24msb_en_msb, self.__reg_i2s_rx_24msb_en_lsb, value)

    @property
    def reg_i2s_rx_fifo_sync(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2s_rx_fifo_sync_msb, self.__reg_i2s_rx_fifo_sync_lsb)
    @reg_i2s_rx_fifo_sync.setter
    def reg_i2s_rx_fifo_sync(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2s_rx_fifo_sync_msb, self.__reg_i2s_rx_fifo_sync_lsb, value)

    @property
    def reg_i2s_rx_fifo_mod_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2s_rx_fifo_mod_force_en_msb, self.__reg_i2s_rx_fifo_mod_force_en_lsb)
    @reg_i2s_rx_fifo_mod_force_en.setter
    def reg_i2s_rx_fifo_mod_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2s_rx_fifo_mod_force_en_msb, self.__reg_i2s_rx_fifo_mod_force_en_lsb, value)

    @property
    def reg_i2s_tx_fifo_mod_force_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2s_tx_fifo_mod_force_en_msb, self.__reg_i2s_tx_fifo_mod_force_en_lsb)
    @reg_i2s_tx_fifo_mod_force_en.setter
    def reg_i2s_tx_fifo_mod_force_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2s_tx_fifo_mod_force_en_msb, self.__reg_i2s_tx_fifo_mod_force_en_lsb, value)

    @property
    def reg_i2s_rx_fifo_mod(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2s_rx_fifo_mod_msb, self.__reg_i2s_rx_fifo_mod_lsb)
    @reg_i2s_rx_fifo_mod.setter
    def reg_i2s_rx_fifo_mod(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2s_rx_fifo_mod_msb, self.__reg_i2s_rx_fifo_mod_lsb, value)

    @property
    def reg_i2s_tx_fifo_mod(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2s_tx_fifo_mod_msb, self.__reg_i2s_tx_fifo_mod_lsb)
    @reg_i2s_tx_fifo_mod.setter
    def reg_i2s_tx_fifo_mod(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2s_tx_fifo_mod_msb, self.__reg_i2s_tx_fifo_mod_lsb, value)

    @property
    def reg_i2s_dscr_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2s_dscr_en_msb, self.__reg_i2s_dscr_en_lsb)
    @reg_i2s_dscr_en.setter
    def reg_i2s_dscr_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2s_dscr_en_msb, self.__reg_i2s_dscr_en_lsb, value)

    @property
    def reg_i2s_tx_data_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2s_tx_data_num_msb, self.__reg_i2s_tx_data_num_lsb)
    @reg_i2s_tx_data_num.setter
    def reg_i2s_tx_data_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2s_tx_data_num_msb, self.__reg_i2s_tx_data_num_lsb, value)

    @property
    def reg_i2s_rx_data_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2s_rx_data_num_msb, self.__reg_i2s_rx_data_num_lsb)
    @reg_i2s_rx_data_num.setter
    def reg_i2s_rx_data_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2s_rx_data_num_msb, self.__reg_i2s_rx_data_num_lsb, value)
class I2SRXEOF_NUM(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x24
        self.__reg_i2s_rx_eof_num_lsb = 0
        self.__reg_i2s_rx_eof_num_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_i2s_rx_eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2s_rx_eof_num_msb, self.__reg_i2s_rx_eof_num_lsb)
    @reg_i2s_rx_eof_num.setter
    def reg_i2s_rx_eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2s_rx_eof_num_msb, self.__reg_i2s_rx_eof_num_lsb, value)
class I2SCONF_SIGLE_DATA(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x28
        self.__reg_i2s_sigle_data_lsb = 0
        self.__reg_i2s_sigle_data_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_i2s_sigle_data(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2s_sigle_data_msb, self.__reg_i2s_sigle_data_lsb)
    @reg_i2s_sigle_data.setter
    def reg_i2s_sigle_data(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2s_sigle_data_msb, self.__reg_i2s_sigle_data_lsb, value)
class I2SCONF_CHAN(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x2c
        self.__reg_rx_chan_mod_lsb = 3
        self.__reg_rx_chan_mod_msb = 4
        self.__reg_tx_chan_mod_lsb = 0
        self.__reg_tx_chan_mod_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rx_chan_mod(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_chan_mod_msb, self.__reg_rx_chan_mod_lsb)
    @reg_rx_chan_mod.setter
    def reg_rx_chan_mod(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_chan_mod_msb, self.__reg_rx_chan_mod_lsb, value)

    @property
    def reg_tx_chan_mod(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_chan_mod_msb, self.__reg_tx_chan_mod_lsb)
    @reg_tx_chan_mod.setter
    def reg_tx_chan_mod(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_chan_mod_msb, self.__reg_tx_chan_mod_lsb, value)
class I2SOUT_LINK(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x30
        self.__outlink_park_lsb = 31
        self.__outlink_park_msb = 31
        self.__i2s_outlink_restart_lsb = 30
        self.__i2s_outlink_restart_msb = 30
        self.__i2s_outlink_start_lsb = 29
        self.__i2s_outlink_start_msb = 29
        self.__i2s_outlink_stop_lsb = 28
        self.__i2s_outlink_stop_msb = 28
        self.__i2s_outlink_addr_lsb = 0
        self.__i2s_outlink_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def outlink_park(self):
        return self.__MEM.rdm(self.__addr, self.__outlink_park_msb, self.__outlink_park_lsb)
    @outlink_park.setter
    def outlink_park(self, value):
        return self.__MEM.wrm(self.__addr, self.__outlink_park_msb, self.__outlink_park_lsb, value)

    @property
    def i2s_outlink_restart(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_outlink_restart_msb, self.__i2s_outlink_restart_lsb)
    @i2s_outlink_restart.setter
    def i2s_outlink_restart(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_outlink_restart_msb, self.__i2s_outlink_restart_lsb, value)

    @property
    def i2s_outlink_start(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_outlink_start_msb, self.__i2s_outlink_start_lsb)
    @i2s_outlink_start.setter
    def i2s_outlink_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_outlink_start_msb, self.__i2s_outlink_start_lsb, value)

    @property
    def i2s_outlink_stop(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_outlink_stop_msb, self.__i2s_outlink_stop_lsb)
    @i2s_outlink_stop.setter
    def i2s_outlink_stop(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_outlink_stop_msb, self.__i2s_outlink_stop_lsb, value)

    @property
    def i2s_outlink_addr(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_outlink_addr_msb, self.__i2s_outlink_addr_lsb)
    @i2s_outlink_addr.setter
    def i2s_outlink_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_outlink_addr_msb, self.__i2s_outlink_addr_lsb, value)
class I2SIN_LINK(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x34
        self.__inlink_park_lsb = 31
        self.__inlink_park_msb = 31
        self.__i2s_inlink_restart_lsb = 30
        self.__i2s_inlink_restart_msb = 30
        self.__i2s_inlink_start_lsb = 29
        self.__i2s_inlink_start_msb = 29
        self.__i2s_inlink_stop_lsb = 28
        self.__i2s_inlink_stop_msb = 28
        self.__i2s_inlink_addr_lsb = 0
        self.__i2s_inlink_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def inlink_park(self):
        return self.__MEM.rdm(self.__addr, self.__inlink_park_msb, self.__inlink_park_lsb)
    @inlink_park.setter
    def inlink_park(self, value):
        return self.__MEM.wrm(self.__addr, self.__inlink_park_msb, self.__inlink_park_lsb, value)

    @property
    def i2s_inlink_restart(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_inlink_restart_msb, self.__i2s_inlink_restart_lsb)
    @i2s_inlink_restart.setter
    def i2s_inlink_restart(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_inlink_restart_msb, self.__i2s_inlink_restart_lsb, value)

    @property
    def i2s_inlink_start(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_inlink_start_msb, self.__i2s_inlink_start_lsb)
    @i2s_inlink_start.setter
    def i2s_inlink_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_inlink_start_msb, self.__i2s_inlink_start_lsb, value)

    @property
    def i2s_inlink_stop(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_inlink_stop_msb, self.__i2s_inlink_stop_lsb)
    @i2s_inlink_stop.setter
    def i2s_inlink_stop(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_inlink_stop_msb, self.__i2s_inlink_stop_lsb, value)

    @property
    def i2s_inlink_addr(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_inlink_addr_msb, self.__i2s_inlink_addr_lsb)
    @i2s_inlink_addr.setter
    def i2s_inlink_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_inlink_addr_msb, self.__i2s_inlink_addr_lsb, value)
class I2S_OUT_EOF_DES_ADDR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x38
        self.__i2s_out_eof_des_addr_lsb = 0
        self.__i2s_out_eof_des_addr_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_out_eof_des_addr(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_out_eof_des_addr_msb, self.__i2s_out_eof_des_addr_lsb)
    @i2s_out_eof_des_addr.setter
    def i2s_out_eof_des_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_out_eof_des_addr_msb, self.__i2s_out_eof_des_addr_lsb, value)
class I2S_IN_EOF_DES_ADDR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x3c
        self.__i2s_in_suc_eof_des_addr_lsb = 0
        self.__i2s_in_suc_eof_des_addr_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_in_suc_eof_des_addr(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_in_suc_eof_des_addr_msb, self.__i2s_in_suc_eof_des_addr_lsb)
    @i2s_in_suc_eof_des_addr.setter
    def i2s_in_suc_eof_des_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_in_suc_eof_des_addr_msb, self.__i2s_in_suc_eof_des_addr_lsb, value)
class I2S_OUT_EOF_BFR_DES_ADDR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x40
        self.__i2s_out_eof_bfr_des_addr_lsb = 0
        self.__i2s_out_eof_bfr_des_addr_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_out_eof_bfr_des_addr(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_out_eof_bfr_des_addr_msb, self.__i2s_out_eof_bfr_des_addr_lsb)
    @i2s_out_eof_bfr_des_addr.setter
    def i2s_out_eof_bfr_des_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_out_eof_bfr_des_addr_msb, self.__i2s_out_eof_bfr_des_addr_lsb, value)
class I2S_AHB_TEST(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x44
        self.__i2s_ahb_testaddr_lsb = 4
        self.__i2s_ahb_testaddr_msb = 5
        self.__i2s_ahb_testmode_lsb = 0
        self.__i2s_ahb_testmode_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_ahb_testaddr(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_ahb_testaddr_msb, self.__i2s_ahb_testaddr_lsb)
    @i2s_ahb_testaddr.setter
    def i2s_ahb_testaddr(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_ahb_testaddr_msb, self.__i2s_ahb_testaddr_lsb, value)

    @property
    def i2s_ahb_testmode(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_ahb_testmode_msb, self.__i2s_ahb_testmode_lsb)
    @i2s_ahb_testmode.setter
    def i2s_ahb_testmode(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_ahb_testmode_msb, self.__i2s_ahb_testmode_lsb, value)
class I2S_INLINK_DSCR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x48
        self.__i2s_inlink_dscr_lsb = 0
        self.__i2s_inlink_dscr_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_inlink_dscr(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_inlink_dscr_msb, self.__i2s_inlink_dscr_lsb)
    @i2s_inlink_dscr.setter
    def i2s_inlink_dscr(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_inlink_dscr_msb, self.__i2s_inlink_dscr_lsb, value)
class I2S_INLINK_DSCR_BF0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x4c
        self.__i2s_inlink_dscr_bf0_lsb = 0
        self.__i2s_inlink_dscr_bf0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_inlink_dscr_bf0(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_inlink_dscr_bf0_msb, self.__i2s_inlink_dscr_bf0_lsb)
    @i2s_inlink_dscr_bf0.setter
    def i2s_inlink_dscr_bf0(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_inlink_dscr_bf0_msb, self.__i2s_inlink_dscr_bf0_lsb, value)
class I2S_INLINK_DSCR_BF1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x50
        self.__i2s_inlink_dscr_bf1_lsb = 0
        self.__i2s_inlink_dscr_bf1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_inlink_dscr_bf1(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_inlink_dscr_bf1_msb, self.__i2s_inlink_dscr_bf1_lsb)
    @i2s_inlink_dscr_bf1.setter
    def i2s_inlink_dscr_bf1(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_inlink_dscr_bf1_msb, self.__i2s_inlink_dscr_bf1_lsb, value)
class I2S_OUTLINK_DSCR(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x54
        self.__i2s_outlink_dscr_lsb = 0
        self.__i2s_outlink_dscr_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_outlink_dscr(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_outlink_dscr_msb, self.__i2s_outlink_dscr_lsb)
    @i2s_outlink_dscr.setter
    def i2s_outlink_dscr(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_outlink_dscr_msb, self.__i2s_outlink_dscr_lsb, value)
class I2S_OUTLINK_DSCR_BF0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x58
        self.__i2s_outlink_dscr_bf0_lsb = 0
        self.__i2s_outlink_dscr_bf0_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_outlink_dscr_bf0(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_outlink_dscr_bf0_msb, self.__i2s_outlink_dscr_bf0_lsb)
    @i2s_outlink_dscr_bf0.setter
    def i2s_outlink_dscr_bf0(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_outlink_dscr_bf0_msb, self.__i2s_outlink_dscr_bf0_lsb, value)
class I2S_OUTLINK_DSCR_BF1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x5c
        self.__i2s_outlink_dscr_bf1_lsb = 0
        self.__i2s_outlink_dscr_bf1_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_outlink_dscr_bf1(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_outlink_dscr_bf1_msb, self.__i2s_outlink_dscr_bf1_lsb)
    @i2s_outlink_dscr_bf1.setter
    def i2s_outlink_dscr_bf1(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_outlink_dscr_bf1_msb, self.__i2s_outlink_dscr_bf1_lsb, value)
class I2S_LC_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x60
        self.__i2s_mem_trans_en_lsb = 13
        self.__i2s_mem_trans_en_msb = 13
        self.__i2s_check_owner_lsb = 12
        self.__i2s_check_owner_msb = 12
        self.__i2s_out_data_burst_en_lsb = 11
        self.__i2s_out_data_burst_en_msb = 11
        self.__i2s_indscr_burst_en_lsb = 10
        self.__i2s_indscr_burst_en_msb = 10
        self.__i2s_outdscr_burst_en_lsb = 9
        self.__i2s_outdscr_burst_en_msb = 9
        self.__i2s_out_eof_mode_lsb = 8
        self.__i2s_out_eof_mode_msb = 8
        self.__i2s_out_no_restart_clr_lsb = 7
        self.__i2s_out_no_restart_clr_msb = 7
        self.__i2s_out_auto_wrback_lsb = 6
        self.__i2s_out_auto_wrback_msb = 6
        self.__i2s_in_loop_test_lsb = 5
        self.__i2s_in_loop_test_msb = 5
        self.__i2s_out_loop_test_lsb = 4
        self.__i2s_out_loop_test_msb = 4
        self.__i2s_ahbm_rst_lsb = 3
        self.__i2s_ahbm_rst_msb = 3
        self.__i2s_ahbm_fifo_rst_lsb = 2
        self.__i2s_ahbm_fifo_rst_msb = 2
        self.__i2s_out_rst_lsb = 1
        self.__i2s_out_rst_msb = 1
        self.__i2s_in_rst_lsb = 0
        self.__i2s_in_rst_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_mem_trans_en(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_mem_trans_en_msb, self.__i2s_mem_trans_en_lsb)
    @i2s_mem_trans_en.setter
    def i2s_mem_trans_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_mem_trans_en_msb, self.__i2s_mem_trans_en_lsb, value)

    @property
    def i2s_check_owner(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_check_owner_msb, self.__i2s_check_owner_lsb)
    @i2s_check_owner.setter
    def i2s_check_owner(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_check_owner_msb, self.__i2s_check_owner_lsb, value)

    @property
    def i2s_out_data_burst_en(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_out_data_burst_en_msb, self.__i2s_out_data_burst_en_lsb)
    @i2s_out_data_burst_en.setter
    def i2s_out_data_burst_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_out_data_burst_en_msb, self.__i2s_out_data_burst_en_lsb, value)

    @property
    def i2s_indscr_burst_en(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_indscr_burst_en_msb, self.__i2s_indscr_burst_en_lsb)
    @i2s_indscr_burst_en.setter
    def i2s_indscr_burst_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_indscr_burst_en_msb, self.__i2s_indscr_burst_en_lsb, value)

    @property
    def i2s_outdscr_burst_en(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_outdscr_burst_en_msb, self.__i2s_outdscr_burst_en_lsb)
    @i2s_outdscr_burst_en.setter
    def i2s_outdscr_burst_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_outdscr_burst_en_msb, self.__i2s_outdscr_burst_en_lsb, value)

    @property
    def i2s_out_eof_mode(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_out_eof_mode_msb, self.__i2s_out_eof_mode_lsb)
    @i2s_out_eof_mode.setter
    def i2s_out_eof_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_out_eof_mode_msb, self.__i2s_out_eof_mode_lsb, value)

    @property
    def i2s_out_no_restart_clr(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_out_no_restart_clr_msb, self.__i2s_out_no_restart_clr_lsb)
    @i2s_out_no_restart_clr.setter
    def i2s_out_no_restart_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_out_no_restart_clr_msb, self.__i2s_out_no_restart_clr_lsb, value)

    @property
    def i2s_out_auto_wrback(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_out_auto_wrback_msb, self.__i2s_out_auto_wrback_lsb)
    @i2s_out_auto_wrback.setter
    def i2s_out_auto_wrback(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_out_auto_wrback_msb, self.__i2s_out_auto_wrback_lsb, value)

    @property
    def i2s_in_loop_test(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_in_loop_test_msb, self.__i2s_in_loop_test_lsb)
    @i2s_in_loop_test.setter
    def i2s_in_loop_test(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_in_loop_test_msb, self.__i2s_in_loop_test_lsb, value)

    @property
    def i2s_out_loop_test(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_out_loop_test_msb, self.__i2s_out_loop_test_lsb)
    @i2s_out_loop_test.setter
    def i2s_out_loop_test(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_out_loop_test_msb, self.__i2s_out_loop_test_lsb, value)

    @property
    def i2s_ahbm_rst(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_ahbm_rst_msb, self.__i2s_ahbm_rst_lsb)
    @i2s_ahbm_rst.setter
    def i2s_ahbm_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_ahbm_rst_msb, self.__i2s_ahbm_rst_lsb, value)

    @property
    def i2s_ahbm_fifo_rst(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_ahbm_fifo_rst_msb, self.__i2s_ahbm_fifo_rst_lsb)
    @i2s_ahbm_fifo_rst.setter
    def i2s_ahbm_fifo_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_ahbm_fifo_rst_msb, self.__i2s_ahbm_fifo_rst_lsb, value)

    @property
    def i2s_out_rst(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_out_rst_msb, self.__i2s_out_rst_lsb)
    @i2s_out_rst.setter
    def i2s_out_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_out_rst_msb, self.__i2s_out_rst_lsb, value)

    @property
    def i2s_in_rst(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_in_rst_msb, self.__i2s_in_rst_lsb)
    @i2s_in_rst.setter
    def i2s_in_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_in_rst_msb, self.__i2s_in_rst_lsb, value)
class I2S_OUTFIFO_PUSH(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x64
        self.__i2s_outfifo_push_lsb = 16
        self.__i2s_outfifo_push_msb = 16
        self.__i2s_outfifo_wdata_lsb = 0
        self.__i2s_outfifo_wdata_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_outfifo_push(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_outfifo_push_msb, self.__i2s_outfifo_push_lsb)
    @i2s_outfifo_push.setter
    def i2s_outfifo_push(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_outfifo_push_msb, self.__i2s_outfifo_push_lsb, value)

    @property
    def i2s_outfifo_wdata(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_outfifo_wdata_msb, self.__i2s_outfifo_wdata_lsb)
    @i2s_outfifo_wdata.setter
    def i2s_outfifo_wdata(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_outfifo_wdata_msb, self.__i2s_outfifo_wdata_lsb, value)
class I2S_INFIFO_POP(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x68
        self.__i2s_infifo_pop_lsb = 16
        self.__i2s_infifo_pop_msb = 16
        self.__i2s_infifo_rdata_lsb = 0
        self.__i2s_infifo_rdata_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_infifo_pop(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_infifo_pop_msb, self.__i2s_infifo_pop_lsb)
    @i2s_infifo_pop.setter
    def i2s_infifo_pop(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_infifo_pop_msb, self.__i2s_infifo_pop_lsb, value)

    @property
    def i2s_infifo_rdata(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_infifo_rdata_msb, self.__i2s_infifo_rdata_lsb)
    @i2s_infifo_rdata.setter
    def i2s_infifo_rdata(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_infifo_rdata_msb, self.__i2s_infifo_rdata_lsb, value)
class I2S_LC_STATE0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x6c
        self.__out_empty_lsb = 31
        self.__out_empty_msb = 31
        self.__out_full_lsb = 30
        self.__out_full_msb = 30
        self.__outfifo_cnt_lsb = 23
        self.__outfifo_cnt_msb = 29
        self.__out_state_lsb = 20
        self.__out_state_msb = 22
        self.__out_dscr_state_lsb = 18
        self.__out_dscr_state_msb = 19
        self.__outlink_dscr_addr_lsb = 0
        self.__outlink_dscr_addr_msb = 17
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def out_empty(self):
        return self.__MEM.rdm(self.__addr, self.__out_empty_msb, self.__out_empty_lsb)
    @out_empty.setter
    def out_empty(self, value):
        return self.__MEM.wrm(self.__addr, self.__out_empty_msb, self.__out_empty_lsb, value)

    @property
    def out_full(self):
        return self.__MEM.rdm(self.__addr, self.__out_full_msb, self.__out_full_lsb)
    @out_full.setter
    def out_full(self, value):
        return self.__MEM.wrm(self.__addr, self.__out_full_msb, self.__out_full_lsb, value)

    @property
    def outfifo_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__outfifo_cnt_msb, self.__outfifo_cnt_lsb)
    @outfifo_cnt.setter
    def outfifo_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__outfifo_cnt_msb, self.__outfifo_cnt_lsb, value)

    @property
    def out_state(self):
        return self.__MEM.rdm(self.__addr, self.__out_state_msb, self.__out_state_lsb)
    @out_state.setter
    def out_state(self, value):
        return self.__MEM.wrm(self.__addr, self.__out_state_msb, self.__out_state_lsb, value)

    @property
    def out_dscr_state(self):
        return self.__MEM.rdm(self.__addr, self.__out_dscr_state_msb, self.__out_dscr_state_lsb)
    @out_dscr_state.setter
    def out_dscr_state(self, value):
        return self.__MEM.wrm(self.__addr, self.__out_dscr_state_msb, self.__out_dscr_state_lsb, value)

    @property
    def outlink_dscr_addr(self):
        return self.__MEM.rdm(self.__addr, self.__outlink_dscr_addr_msb, self.__outlink_dscr_addr_lsb)
    @outlink_dscr_addr.setter
    def outlink_dscr_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__outlink_dscr_addr_msb, self.__outlink_dscr_addr_lsb, value)
class I2S_LC_STATE1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x70
        self.__in_empty_lsb = 31
        self.__in_empty_msb = 31
        self.__in_full_lsb = 30
        self.__in_full_msb = 30
        self.__infifo_cnt_debug_lsb = 23
        self.__infifo_cnt_debug_msb = 29
        self.__in_state_lsb = 20
        self.__in_state_msb = 22
        self.__in_dscr_state_lsb = 18
        self.__in_dscr_state_msb = 19
        self.__inlink_dscr_addr_lsb = 0
        self.__inlink_dscr_addr_msb = 17
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def in_empty(self):
        return self.__MEM.rdm(self.__addr, self.__in_empty_msb, self.__in_empty_lsb)
    @in_empty.setter
    def in_empty(self, value):
        return self.__MEM.wrm(self.__addr, self.__in_empty_msb, self.__in_empty_lsb, value)

    @property
    def in_full(self):
        return self.__MEM.rdm(self.__addr, self.__in_full_msb, self.__in_full_lsb)
    @in_full.setter
    def in_full(self, value):
        return self.__MEM.wrm(self.__addr, self.__in_full_msb, self.__in_full_lsb, value)

    @property
    def infifo_cnt_debug(self):
        return self.__MEM.rdm(self.__addr, self.__infifo_cnt_debug_msb, self.__infifo_cnt_debug_lsb)
    @infifo_cnt_debug.setter
    def infifo_cnt_debug(self, value):
        return self.__MEM.wrm(self.__addr, self.__infifo_cnt_debug_msb, self.__infifo_cnt_debug_lsb, value)

    @property
    def in_state(self):
        return self.__MEM.rdm(self.__addr, self.__in_state_msb, self.__in_state_lsb)
    @in_state.setter
    def in_state(self, value):
        return self.__MEM.wrm(self.__addr, self.__in_state_msb, self.__in_state_lsb, value)

    @property
    def in_dscr_state(self):
        return self.__MEM.rdm(self.__addr, self.__in_dscr_state_msb, self.__in_dscr_state_lsb)
    @in_dscr_state.setter
    def in_dscr_state(self, value):
        return self.__MEM.wrm(self.__addr, self.__in_dscr_state_msb, self.__in_dscr_state_lsb, value)

    @property
    def inlink_dscr_addr(self):
        return self.__MEM.rdm(self.__addr, self.__inlink_dscr_addr_msb, self.__inlink_dscr_addr_lsb)
    @inlink_dscr_addr.setter
    def inlink_dscr_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__inlink_dscr_addr_msb, self.__inlink_dscr_addr_lsb, value)
class I2S_LC_HUNG_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x74
        self.__i2s_lc_fifo_timeout_ena_lsb = 11
        self.__i2s_lc_fifo_timeout_ena_msb = 11
        self.__i2s_lc_fifo_timeout_shift_lsb = 8
        self.__i2s_lc_fifo_timeout_shift_msb = 10
        self.__i2s_lc_fifo_timeout_lsb = 0
        self.__i2s_lc_fifo_timeout_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_lc_fifo_timeout_ena(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_lc_fifo_timeout_ena_msb, self.__i2s_lc_fifo_timeout_ena_lsb)
    @i2s_lc_fifo_timeout_ena.setter
    def i2s_lc_fifo_timeout_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_lc_fifo_timeout_ena_msb, self.__i2s_lc_fifo_timeout_ena_lsb, value)

    @property
    def i2s_lc_fifo_timeout_shift(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_lc_fifo_timeout_shift_msb, self.__i2s_lc_fifo_timeout_shift_lsb)
    @i2s_lc_fifo_timeout_shift.setter
    def i2s_lc_fifo_timeout_shift(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_lc_fifo_timeout_shift_msb, self.__i2s_lc_fifo_timeout_shift_lsb, value)

    @property
    def i2s_lc_fifo_timeout(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_lc_fifo_timeout_msb, self.__i2s_lc_fifo_timeout_lsb)
    @i2s_lc_fifo_timeout.setter
    def i2s_lc_fifo_timeout(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_lc_fifo_timeout_msb, self.__i2s_lc_fifo_timeout_lsb, value)
class I2S_CVSD_CONF0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x80
        self.__i2s_cvsd_reg_y_min_lsb = 16
        self.__i2s_cvsd_reg_y_min_msb = 31
        self.__i2s_cvsd_reg_y_max_lsb = 0
        self.__i2s_cvsd_reg_y_max_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_cvsd_reg_y_min(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_cvsd_reg_y_min_msb, self.__i2s_cvsd_reg_y_min_lsb)
    @i2s_cvsd_reg_y_min.setter
    def i2s_cvsd_reg_y_min(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_cvsd_reg_y_min_msb, self.__i2s_cvsd_reg_y_min_lsb, value)

    @property
    def i2s_cvsd_reg_y_max(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_cvsd_reg_y_max_msb, self.__i2s_cvsd_reg_y_max_lsb)
    @i2s_cvsd_reg_y_max.setter
    def i2s_cvsd_reg_y_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_cvsd_reg_y_max_msb, self.__i2s_cvsd_reg_y_max_lsb, value)
class I2S_CVSD_CONF1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x84
        self.__i2s_cvsd_reg_sigma_min_lsb = 16
        self.__i2s_cvsd_reg_sigma_min_msb = 31
        self.__i2s_cvsd_reg_sigma_max_lsb = 0
        self.__i2s_cvsd_reg_sigma_max_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_cvsd_reg_sigma_min(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_cvsd_reg_sigma_min_msb, self.__i2s_cvsd_reg_sigma_min_lsb)
    @i2s_cvsd_reg_sigma_min.setter
    def i2s_cvsd_reg_sigma_min(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_cvsd_reg_sigma_min_msb, self.__i2s_cvsd_reg_sigma_min_lsb, value)

    @property
    def i2s_cvsd_reg_sigma_max(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_cvsd_reg_sigma_max_msb, self.__i2s_cvsd_reg_sigma_max_lsb)
    @i2s_cvsd_reg_sigma_max.setter
    def i2s_cvsd_reg_sigma_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_cvsd_reg_sigma_max_msb, self.__i2s_cvsd_reg_sigma_max_lsb, value)
class I2S_CVSD_CONF2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x88
        self.__i2s_cvsd_reg_h_lsb = 16
        self.__i2s_cvsd_reg_h_msb = 18
        self.__i2s_cvsd_reg_beta_lsb = 6
        self.__i2s_cvsd_reg_beta_msb = 15
        self.__i2s_cvsd_reg_J_lsb = 3
        self.__i2s_cvsd_reg_J_msb = 5
        self.__i2s_cvsd_reg_K_lsb = 0
        self.__i2s_cvsd_reg_K_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_cvsd_reg_h(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_cvsd_reg_h_msb, self.__i2s_cvsd_reg_h_lsb)
    @i2s_cvsd_reg_h.setter
    def i2s_cvsd_reg_h(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_cvsd_reg_h_msb, self.__i2s_cvsd_reg_h_lsb, value)

    @property
    def i2s_cvsd_reg_beta(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_cvsd_reg_beta_msb, self.__i2s_cvsd_reg_beta_lsb)
    @i2s_cvsd_reg_beta.setter
    def i2s_cvsd_reg_beta(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_cvsd_reg_beta_msb, self.__i2s_cvsd_reg_beta_lsb, value)

    @property
    def i2s_cvsd_reg_J(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_cvsd_reg_J_msb, self.__i2s_cvsd_reg_J_lsb)
    @i2s_cvsd_reg_J.setter
    def i2s_cvsd_reg_J(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_cvsd_reg_J_msb, self.__i2s_cvsd_reg_J_lsb, value)

    @property
    def i2s_cvsd_reg_K(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_cvsd_reg_K_msb, self.__i2s_cvsd_reg_K_lsb)
    @i2s_cvsd_reg_K.setter
    def i2s_cvsd_reg_K(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_cvsd_reg_K_msb, self.__i2s_cvsd_reg_K_lsb, value)
class I2S_PLC_CONF0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x8c
        self.__i2s_N_min_err_lsb = 25
        self.__i2s_N_min_err_msb = 27
        self.__i2s_pack_len_8k_lsb = 20
        self.__i2s_pack_len_8k_msb = 24
        self.__i2s_max_slide_sample_lsb = 12
        self.__i2s_max_slide_sample_msb = 19
        self.__i2s_shift_rate_lsb = 9
        self.__i2s_shift_rate_msb = 11
        self.__i2s_N_err_seg_lsb = 6
        self.__i2s_N_err_seg_msb = 8
        self.__i2s_good_pack_max_lsb = 0
        self.__i2s_good_pack_max_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_N_min_err(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_N_min_err_msb, self.__i2s_N_min_err_lsb)
    @i2s_N_min_err.setter
    def i2s_N_min_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_N_min_err_msb, self.__i2s_N_min_err_lsb, value)

    @property
    def i2s_pack_len_8k(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_pack_len_8k_msb, self.__i2s_pack_len_8k_lsb)
    @i2s_pack_len_8k.setter
    def i2s_pack_len_8k(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_pack_len_8k_msb, self.__i2s_pack_len_8k_lsb, value)

    @property
    def i2s_max_slide_sample(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_max_slide_sample_msb, self.__i2s_max_slide_sample_lsb)
    @i2s_max_slide_sample.setter
    def i2s_max_slide_sample(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_max_slide_sample_msb, self.__i2s_max_slide_sample_lsb, value)

    @property
    def i2s_shift_rate(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_shift_rate_msb, self.__i2s_shift_rate_lsb)
    @i2s_shift_rate.setter
    def i2s_shift_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_shift_rate_msb, self.__i2s_shift_rate_lsb, value)

    @property
    def i2s_N_err_seg(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_N_err_seg_msb, self.__i2s_N_err_seg_lsb)
    @i2s_N_err_seg.setter
    def i2s_N_err_seg(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_N_err_seg_msb, self.__i2s_N_err_seg_lsb, value)

    @property
    def i2s_good_pack_max(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_good_pack_max_msb, self.__i2s_good_pack_max_lsb)
    @i2s_good_pack_max.setter
    def i2s_good_pack_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_good_pack_max_msb, self.__i2s_good_pack_max_lsb, value)
class I2S_PLC_CONF1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x90
        self.__i2s_slide_win_len_lsb = 24
        self.__i2s_slide_win_len_msb = 31
        self.__i2s_bad_ola_win2_para_lsb = 16
        self.__i2s_bad_ola_win2_para_msb = 23
        self.__i2s_bad_ola_win2_para_shift_lsb = 12
        self.__i2s_bad_ola_win2_para_shift_msb = 15
        self.__i2s_bad_cef_atten_para_shift_lsb = 8
        self.__i2s_bad_cef_atten_para_shift_msb = 11
        self.__i2s_bad_cef_atten_para_lsb = 0
        self.__i2s_bad_cef_atten_para_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_slide_win_len(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_slide_win_len_msb, self.__i2s_slide_win_len_lsb)
    @i2s_slide_win_len.setter
    def i2s_slide_win_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_slide_win_len_msb, self.__i2s_slide_win_len_lsb, value)

    @property
    def i2s_bad_ola_win2_para(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_bad_ola_win2_para_msb, self.__i2s_bad_ola_win2_para_lsb)
    @i2s_bad_ola_win2_para.setter
    def i2s_bad_ola_win2_para(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_bad_ola_win2_para_msb, self.__i2s_bad_ola_win2_para_lsb, value)

    @property
    def i2s_bad_ola_win2_para_shift(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_bad_ola_win2_para_shift_msb, self.__i2s_bad_ola_win2_para_shift_lsb)
    @i2s_bad_ola_win2_para_shift.setter
    def i2s_bad_ola_win2_para_shift(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_bad_ola_win2_para_shift_msb, self.__i2s_bad_ola_win2_para_shift_lsb, value)

    @property
    def i2s_bad_cef_atten_para_shift(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_bad_cef_atten_para_shift_msb, self.__i2s_bad_cef_atten_para_shift_lsb)
    @i2s_bad_cef_atten_para_shift.setter
    def i2s_bad_cef_atten_para_shift(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_bad_cef_atten_para_shift_msb, self.__i2s_bad_cef_atten_para_shift_lsb, value)

    @property
    def i2s_bad_cef_atten_para(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_bad_cef_atten_para_msb, self.__i2s_bad_cef_atten_para_lsb)
    @i2s_bad_cef_atten_para.setter
    def i2s_bad_cef_atten_para(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_bad_cef_atten_para_msb, self.__i2s_bad_cef_atten_para_lsb, value)
class I2S_PLC_CONF2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x94
        self.__i2s_reg_min_period_lsb = 2
        self.__i2s_reg_min_period_msb = 6
        self.__i2s_reg_cvsd_seg_mod_lsb = 0
        self.__i2s_reg_cvsd_seg_mod_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_reg_min_period(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_reg_min_period_msb, self.__i2s_reg_min_period_lsb)
    @i2s_reg_min_period.setter
    def i2s_reg_min_period(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_reg_min_period_msb, self.__i2s_reg_min_period_lsb, value)

    @property
    def i2s_reg_cvsd_seg_mod(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_reg_cvsd_seg_mod_msb, self.__i2s_reg_cvsd_seg_mod_lsb)
    @i2s_reg_cvsd_seg_mod.setter
    def i2s_reg_cvsd_seg_mod(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_reg_cvsd_seg_mod_msb, self.__i2s_reg_cvsd_seg_mod_lsb, value)
class I2S_ESCO_CONF0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x98
        self.__i2s_plc2dma_en_lsb = 12
        self.__i2s_plc2dma_en_msb = 12
        self.__i2s_plc_en_lsb = 11
        self.__i2s_plc_en_msb = 11
        self.__i2s_cvsd_dec_reset_lsb = 10
        self.__i2s_cvsd_dec_reset_msb = 10
        self.__i2s_cvsd_dec_start_lsb = 9
        self.__i2s_cvsd_dec_start_msb = 9
        self.__i2s_esco_cvsd_inf_en_lsb = 8
        self.__i2s_esco_cvsd_inf_en_msb = 8
        self.__i2s_esco_cvsd_pack_len_8k_lsb = 3
        self.__i2s_esco_cvsd_pack_len_8k_msb = 7
        self.__i2s_esco_cvsd_dec_pack_err_lsb = 2
        self.__i2s_esco_cvsd_dec_pack_err_msb = 2
        self.__i2s_esco_chan_mod_lsb = 1
        self.__i2s_esco_chan_mod_msb = 1
        self.__i2s_esco_en_lsb = 0
        self.__i2s_esco_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_plc2dma_en(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_plc2dma_en_msb, self.__i2s_plc2dma_en_lsb)
    @i2s_plc2dma_en.setter
    def i2s_plc2dma_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_plc2dma_en_msb, self.__i2s_plc2dma_en_lsb, value)

    @property
    def i2s_plc_en(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_plc_en_msb, self.__i2s_plc_en_lsb)
    @i2s_plc_en.setter
    def i2s_plc_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_plc_en_msb, self.__i2s_plc_en_lsb, value)

    @property
    def i2s_cvsd_dec_reset(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_cvsd_dec_reset_msb, self.__i2s_cvsd_dec_reset_lsb)
    @i2s_cvsd_dec_reset.setter
    def i2s_cvsd_dec_reset(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_cvsd_dec_reset_msb, self.__i2s_cvsd_dec_reset_lsb, value)

    @property
    def i2s_cvsd_dec_start(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_cvsd_dec_start_msb, self.__i2s_cvsd_dec_start_lsb)
    @i2s_cvsd_dec_start.setter
    def i2s_cvsd_dec_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_cvsd_dec_start_msb, self.__i2s_cvsd_dec_start_lsb, value)

    @property
    def i2s_esco_cvsd_inf_en(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_esco_cvsd_inf_en_msb, self.__i2s_esco_cvsd_inf_en_lsb)
    @i2s_esco_cvsd_inf_en.setter
    def i2s_esco_cvsd_inf_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_esco_cvsd_inf_en_msb, self.__i2s_esco_cvsd_inf_en_lsb, value)

    @property
    def i2s_esco_cvsd_pack_len_8k(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_esco_cvsd_pack_len_8k_msb, self.__i2s_esco_cvsd_pack_len_8k_lsb)
    @i2s_esco_cvsd_pack_len_8k.setter
    def i2s_esco_cvsd_pack_len_8k(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_esco_cvsd_pack_len_8k_msb, self.__i2s_esco_cvsd_pack_len_8k_lsb, value)

    @property
    def i2s_esco_cvsd_dec_pack_err(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_esco_cvsd_dec_pack_err_msb, self.__i2s_esco_cvsd_dec_pack_err_lsb)
    @i2s_esco_cvsd_dec_pack_err.setter
    def i2s_esco_cvsd_dec_pack_err(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_esco_cvsd_dec_pack_err_msb, self.__i2s_esco_cvsd_dec_pack_err_lsb, value)

    @property
    def i2s_esco_chan_mod(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_esco_chan_mod_msb, self.__i2s_esco_chan_mod_lsb)
    @i2s_esco_chan_mod.setter
    def i2s_esco_chan_mod(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_esco_chan_mod_msb, self.__i2s_esco_chan_mod_lsb, value)

    @property
    def i2s_esco_en(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_esco_en_msb, self.__i2s_esco_en_lsb)
    @i2s_esco_en.setter
    def i2s_esco_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_esco_en_msb, self.__i2s_esco_en_lsb, value)
class I2S_SCO_CONF0(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0x9c
        self.__i2s_cvsd_enc_reset_lsb = 3
        self.__i2s_cvsd_enc_reset_msb = 3
        self.__i2s_cvsd_enc_start_lsb = 2
        self.__i2s_cvsd_enc_start_msb = 2
        self.__reg_i2s_sco_no_i2s_en_lsb = 1
        self.__reg_i2s_sco_no_i2s_en_msb = 1
        self.__reg_i2s_sco_with_i2s_en_lsb = 0
        self.__reg_i2s_sco_with_i2s_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def i2s_cvsd_enc_reset(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_cvsd_enc_reset_msb, self.__i2s_cvsd_enc_reset_lsb)
    @i2s_cvsd_enc_reset.setter
    def i2s_cvsd_enc_reset(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_cvsd_enc_reset_msb, self.__i2s_cvsd_enc_reset_lsb, value)

    @property
    def i2s_cvsd_enc_start(self):
        return self.__MEM.rdm(self.__addr, self.__i2s_cvsd_enc_start_msb, self.__i2s_cvsd_enc_start_lsb)
    @i2s_cvsd_enc_start.setter
    def i2s_cvsd_enc_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__i2s_cvsd_enc_start_msb, self.__i2s_cvsd_enc_start_lsb, value)

    @property
    def reg_i2s_sco_no_i2s_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2s_sco_no_i2s_en_msb, self.__reg_i2s_sco_no_i2s_en_lsb)
    @reg_i2s_sco_no_i2s_en.setter
    def reg_i2s_sco_no_i2s_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2s_sco_no_i2s_en_msb, self.__reg_i2s_sco_no_i2s_en_lsb, value)

    @property
    def reg_i2s_sco_with_i2s_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2s_sco_with_i2s_en_msb, self.__reg_i2s_sco_with_i2s_en_lsb)
    @reg_i2s_sco_with_i2s_en.setter
    def reg_i2s_sco_with_i2s_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2s_sco_with_i2s_en_msb, self.__reg_i2s_sco_with_i2s_en_lsb, value)
class I2SCONF1(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0xa0
        self.__reg_i2s_tx_zeros_rm_en_lsb = 9
        self.__reg_i2s_tx_zeros_rm_en_msb = 9
        self.__reg_i2s_tx_stop_en_lsb = 8
        self.__reg_i2s_tx_stop_en_msb = 8
        self.__rx_pcm_bypass_lsb = 7
        self.__rx_pcm_bypass_msb = 7
        self.__rx_pcm_conf_lsb = 4
        self.__rx_pcm_conf_msb = 6
        self.__tx_pcm_bypass_lsb = 3
        self.__tx_pcm_bypass_msb = 3
        self.__tx_pcm_conf_lsb = 0
        self.__tx_pcm_conf_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_i2s_tx_zeros_rm_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2s_tx_zeros_rm_en_msb, self.__reg_i2s_tx_zeros_rm_en_lsb)
    @reg_i2s_tx_zeros_rm_en.setter
    def reg_i2s_tx_zeros_rm_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2s_tx_zeros_rm_en_msb, self.__reg_i2s_tx_zeros_rm_en_lsb, value)

    @property
    def reg_i2s_tx_stop_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2s_tx_stop_en_msb, self.__reg_i2s_tx_stop_en_lsb)
    @reg_i2s_tx_stop_en.setter
    def reg_i2s_tx_stop_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2s_tx_stop_en_msb, self.__reg_i2s_tx_stop_en_lsb, value)

    @property
    def rx_pcm_bypass(self):
        return self.__MEM.rdm(self.__addr, self.__rx_pcm_bypass_msb, self.__rx_pcm_bypass_lsb)
    @rx_pcm_bypass.setter
    def rx_pcm_bypass(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_pcm_bypass_msb, self.__rx_pcm_bypass_lsb, value)

    @property
    def rx_pcm_conf(self):
        return self.__MEM.rdm(self.__addr, self.__rx_pcm_conf_msb, self.__rx_pcm_conf_lsb)
    @rx_pcm_conf.setter
    def rx_pcm_conf(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_pcm_conf_msb, self.__rx_pcm_conf_lsb, value)

    @property
    def tx_pcm_bypass(self):
        return self.__MEM.rdm(self.__addr, self.__tx_pcm_bypass_msb, self.__tx_pcm_bypass_lsb)
    @tx_pcm_bypass.setter
    def tx_pcm_bypass(self, value):
        return self.__MEM.wrm(self.__addr, self.__tx_pcm_bypass_msb, self.__tx_pcm_bypass_lsb, value)

    @property
    def tx_pcm_conf(self):
        return self.__MEM.rdm(self.__addr, self.__tx_pcm_conf_msb, self.__tx_pcm_conf_lsb)
    @tx_pcm_conf.setter
    def tx_pcm_conf(self, value):
        return self.__MEM.wrm(self.__addr, self.__tx_pcm_conf_msb, self.__tx_pcm_conf_lsb, value)
class I2S_PD_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0xa4
        self.__reg_plc_mem_force_pu_lsb = 3
        self.__reg_plc_mem_force_pu_msb = 3
        self.__reg_plc_mem_force_pd_lsb = 2
        self.__reg_plc_mem_force_pd_msb = 2
        self.__reg_i2s_fifo_force_pu_lsb = 1
        self.__reg_i2s_fifo_force_pu_msb = 1
        self.__reg_i2s_fifo_force_pd_lsb = 0
        self.__reg_i2s_fifo_force_pd_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_plc_mem_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_plc_mem_force_pu_msb, self.__reg_plc_mem_force_pu_lsb)
    @reg_plc_mem_force_pu.setter
    def reg_plc_mem_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_plc_mem_force_pu_msb, self.__reg_plc_mem_force_pu_lsb, value)

    @property
    def reg_plc_mem_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_plc_mem_force_pd_msb, self.__reg_plc_mem_force_pd_lsb)
    @reg_plc_mem_force_pd.setter
    def reg_plc_mem_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_plc_mem_force_pd_msb, self.__reg_plc_mem_force_pd_lsb, value)

    @property
    def reg_i2s_fifo_force_pu(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2s_fifo_force_pu_msb, self.__reg_i2s_fifo_force_pu_lsb)
    @reg_i2s_fifo_force_pu.setter
    def reg_i2s_fifo_force_pu(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2s_fifo_force_pu_msb, self.__reg_i2s_fifo_force_pu_lsb, value)

    @property
    def reg_i2s_fifo_force_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2s_fifo_force_pd_msb, self.__reg_i2s_fifo_force_pd_lsb)
    @reg_i2s_fifo_force_pd.setter
    def reg_i2s_fifo_force_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2s_fifo_force_pd_msb, self.__reg_i2s_fifo_force_pd_lsb, value)
class I2SCONF2(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0xa8
        self.__reg_i2si_v_sync_filter_thres_lsb = 11
        self.__reg_i2si_v_sync_filter_thres_msb = 13
        self.__reg_i2si_v_sync_filter_en_lsb = 10
        self.__reg_i2si_v_sync_filter_en_msb = 10
        self.__reg_cam_clk_loopback_lsb = 9
        self.__reg_cam_clk_loopback_msb = 9
        self.__reg_cam_sync_fifo_reset_lsb = 8
        self.__reg_cam_sync_fifo_reset_msb = 8
        self.__reg_inter_valid_en_lsb = 7
        self.__reg_inter_valid_en_msb = 7
        self.__reg_ext_adc_start_en_lsb = 6
        self.__reg_ext_adc_start_en_msb = 6
        self.__reg_lcd_en_lsb = 5
        self.__reg_lcd_en_msb = 5
        self.__reg_data_enable_lsb = 4
        self.__reg_data_enable_msb = 4
        self.__reg_data_enable_test_en_lsb = 3
        self.__reg_data_enable_test_en_msb = 3
        self.__reg_lcd_tx_sdx2_en_lsb = 2
        self.__reg_lcd_tx_sdx2_en_msb = 2
        self.__reg_lcd_tx_wrx2_en_lsb = 1
        self.__reg_lcd_tx_wrx2_en_msb = 1
        self.__reg_camera_en_lsb = 0
        self.__reg_camera_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_i2si_v_sync_filter_thres(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2si_v_sync_filter_thres_msb, self.__reg_i2si_v_sync_filter_thres_lsb)
    @reg_i2si_v_sync_filter_thres.setter
    def reg_i2si_v_sync_filter_thres(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2si_v_sync_filter_thres_msb, self.__reg_i2si_v_sync_filter_thres_lsb, value)

    @property
    def reg_i2si_v_sync_filter_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2si_v_sync_filter_en_msb, self.__reg_i2si_v_sync_filter_en_lsb)
    @reg_i2si_v_sync_filter_en.setter
    def reg_i2si_v_sync_filter_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2si_v_sync_filter_en_msb, self.__reg_i2si_v_sync_filter_en_lsb, value)

    @property
    def reg_cam_clk_loopback(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cam_clk_loopback_msb, self.__reg_cam_clk_loopback_lsb)
    @reg_cam_clk_loopback.setter
    def reg_cam_clk_loopback(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cam_clk_loopback_msb, self.__reg_cam_clk_loopback_lsb, value)

    @property
    def reg_cam_sync_fifo_reset(self):
        return self.__MEM.rdm(self.__addr, self.__reg_cam_sync_fifo_reset_msb, self.__reg_cam_sync_fifo_reset_lsb)
    @reg_cam_sync_fifo_reset.setter
    def reg_cam_sync_fifo_reset(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_cam_sync_fifo_reset_msb, self.__reg_cam_sync_fifo_reset_lsb, value)

    @property
    def reg_inter_valid_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_inter_valid_en_msb, self.__reg_inter_valid_en_lsb)
    @reg_inter_valid_en.setter
    def reg_inter_valid_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_inter_valid_en_msb, self.__reg_inter_valid_en_lsb, value)

    @property
    def reg_ext_adc_start_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_ext_adc_start_en_msb, self.__reg_ext_adc_start_en_lsb)
    @reg_ext_adc_start_en.setter
    def reg_ext_adc_start_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_ext_adc_start_en_msb, self.__reg_ext_adc_start_en_lsb, value)

    @property
    def reg_lcd_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lcd_en_msb, self.__reg_lcd_en_lsb)
    @reg_lcd_en.setter
    def reg_lcd_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lcd_en_msb, self.__reg_lcd_en_lsb, value)

    @property
    def reg_data_enable(self):
        return self.__MEM.rdm(self.__addr, self.__reg_data_enable_msb, self.__reg_data_enable_lsb)
    @reg_data_enable.setter
    def reg_data_enable(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_data_enable_msb, self.__reg_data_enable_lsb, value)

    @property
    def reg_data_enable_test_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_data_enable_test_en_msb, self.__reg_data_enable_test_en_lsb)
    @reg_data_enable_test_en.setter
    def reg_data_enable_test_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_data_enable_test_en_msb, self.__reg_data_enable_test_en_lsb, value)

    @property
    def reg_lcd_tx_sdx2_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lcd_tx_sdx2_en_msb, self.__reg_lcd_tx_sdx2_en_lsb)
    @reg_lcd_tx_sdx2_en.setter
    def reg_lcd_tx_sdx2_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lcd_tx_sdx2_en_msb, self.__reg_lcd_tx_sdx2_en_lsb, value)

    @property
    def reg_lcd_tx_wrx2_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_lcd_tx_wrx2_en_msb, self.__reg_lcd_tx_wrx2_en_lsb)
    @reg_lcd_tx_wrx2_en.setter
    def reg_lcd_tx_wrx2_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_lcd_tx_wrx2_en_msb, self.__reg_lcd_tx_wrx2_en_lsb, value)

    @property
    def reg_camera_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_camera_en_msb, self.__reg_camera_en_lsb)
    @reg_camera_en.setter
    def reg_camera_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_camera_en_msb, self.__reg_camera_en_lsb, value)
class I2S_CLKM_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0xac
        self.__reg_clk_sel_lsb = 21
        self.__reg_clk_sel_msb = 22
        self.__reg_clk_en_lsb = 20
        self.__reg_clk_en_msb = 20
        self.__reg_clkm_div_a_lsb = 14
        self.__reg_clkm_div_a_msb = 19
        self.__reg_clkm_div_b_lsb = 8
        self.__reg_clkm_div_b_msb = 13
        self.__reg_clkm_div_num_lsb = 0
        self.__reg_clkm_div_num_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_clk_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk_sel_msb, self.__reg_clk_sel_lsb)
    @reg_clk_sel.setter
    def reg_clk_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk_sel_msb, self.__reg_clk_sel_lsb, value)

    @property
    def reg_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk_en_msb, self.__reg_clk_en_lsb)
    @reg_clk_en.setter
    def reg_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk_en_msb, self.__reg_clk_en_lsb, value)

    @property
    def reg_clkm_div_a(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clkm_div_a_msb, self.__reg_clkm_div_a_lsb)
    @reg_clkm_div_a.setter
    def reg_clkm_div_a(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clkm_div_a_msb, self.__reg_clkm_div_a_lsb, value)

    @property
    def reg_clkm_div_b(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clkm_div_b_msb, self.__reg_clkm_div_b_lsb)
    @reg_clkm_div_b.setter
    def reg_clkm_div_b(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clkm_div_b_msb, self.__reg_clkm_div_b_lsb, value)

    @property
    def reg_clkm_div_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clkm_div_num_msb, self.__reg_clkm_div_num_lsb)
    @reg_clkm_div_num.setter
    def reg_clkm_div_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clkm_div_num_msb, self.__reg_clkm_div_num_lsb, value)
class I2S_SAMPLE_RATE_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0xb0
        self.__reg_rx_bits_mod_lsb = 18
        self.__reg_rx_bits_mod_msb = 23
        self.__reg_tx_bits_mod_lsb = 12
        self.__reg_tx_bits_mod_msb = 17
        self.__reg_rx_bck_div_num_lsb = 6
        self.__reg_rx_bck_div_num_msb = 11
        self.__reg_tx_bck_div_num_lsb = 0
        self.__reg_tx_bck_div_num_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rx_bits_mod(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_bits_mod_msb, self.__reg_rx_bits_mod_lsb)
    @reg_rx_bits_mod.setter
    def reg_rx_bits_mod(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_bits_mod_msb, self.__reg_rx_bits_mod_lsb, value)

    @property
    def reg_tx_bits_mod(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_bits_mod_msb, self.__reg_tx_bits_mod_lsb)
    @reg_tx_bits_mod.setter
    def reg_tx_bits_mod(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_bits_mod_msb, self.__reg_tx_bits_mod_lsb, value)

    @property
    def reg_rx_bck_div_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_bck_div_num_msb, self.__reg_rx_bck_div_num_lsb)
    @reg_rx_bck_div_num.setter
    def reg_rx_bck_div_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_bck_div_num_msb, self.__reg_rx_bck_div_num_lsb, value)

    @property
    def reg_tx_bck_div_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_bck_div_num_msb, self.__reg_tx_bck_div_num_lsb)
    @reg_tx_bck_div_num.setter
    def reg_tx_bck_div_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_bck_div_num_msb, self.__reg_tx_bck_div_num_lsb, value)
class I2S_PDM_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0xb4
        self.__reg_rx_pdm_way_mode_lsb = 30
        self.__reg_rx_pdm_way_mode_msb = 31
        self.__reg_tx_pdm_way_mode_lsb = 28
        self.__reg_tx_pdm_way_mode_msb = 29
        self.__reg_tx_pdm_chan_mod_lsb = 26
        self.__reg_tx_pdm_chan_mod_msb = 27
        self.__reg_tx_pdm_hp_bypass_lsb = 25
        self.__reg_tx_pdm_hp_bypass_msb = 25
        self.__reg_rx_pdm_sinc_dsr_16_en_lsb = 24
        self.__reg_rx_pdm_sinc_dsr_16_en_msb = 24
        self.__reg_tx_pdm_sigmadelta_in_shift_lsb = 22
        self.__reg_tx_pdm_sigmadelta_in_shift_msb = 23
        self.__reg_tx_pdm_sinc_in_shift_lsb = 20
        self.__reg_tx_pdm_sinc_in_shift_msb = 21
        self.__reg_tx_pdm_lp_in_shift_lsb = 18
        self.__reg_tx_pdm_lp_in_shift_msb = 19
        self.__reg_tx_pdm_hp_in_shift_lsb = 16
        self.__reg_tx_pdm_hp_in_shift_msb = 17
        self.__reg_tx_pdm_prescale_lsb = 8
        self.__reg_tx_pdm_prescale_msb = 15
        self.__reg_tx_pdm_sinc_osr2_lsb = 4
        self.__reg_tx_pdm_sinc_osr2_msb = 7
        self.__reg_pdm2pcm_conv_en_lsb = 3
        self.__reg_pdm2pcm_conv_en_msb = 3
        self.__reg_pcm2pdm_conv_en_lsb = 2
        self.__reg_pcm2pdm_conv_en_msb = 2
        self.__reg_rx_pdm_en_lsb = 1
        self.__reg_rx_pdm_en_msb = 1
        self.__reg_tx_pdm_en_lsb = 0
        self.__reg_tx_pdm_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_rx_pdm_way_mode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_pdm_way_mode_msb, self.__reg_rx_pdm_way_mode_lsb)
    @reg_rx_pdm_way_mode.setter
    def reg_rx_pdm_way_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_pdm_way_mode_msb, self.__reg_rx_pdm_way_mode_lsb, value)

    @property
    def reg_tx_pdm_way_mode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_pdm_way_mode_msb, self.__reg_tx_pdm_way_mode_lsb)
    @reg_tx_pdm_way_mode.setter
    def reg_tx_pdm_way_mode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_pdm_way_mode_msb, self.__reg_tx_pdm_way_mode_lsb, value)

    @property
    def reg_tx_pdm_chan_mod(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_pdm_chan_mod_msb, self.__reg_tx_pdm_chan_mod_lsb)
    @reg_tx_pdm_chan_mod.setter
    def reg_tx_pdm_chan_mod(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_pdm_chan_mod_msb, self.__reg_tx_pdm_chan_mod_lsb, value)

    @property
    def reg_tx_pdm_hp_bypass(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_pdm_hp_bypass_msb, self.__reg_tx_pdm_hp_bypass_lsb)
    @reg_tx_pdm_hp_bypass.setter
    def reg_tx_pdm_hp_bypass(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_pdm_hp_bypass_msb, self.__reg_tx_pdm_hp_bypass_lsb, value)

    @property
    def reg_rx_pdm_sinc_dsr_16_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_pdm_sinc_dsr_16_en_msb, self.__reg_rx_pdm_sinc_dsr_16_en_lsb)
    @reg_rx_pdm_sinc_dsr_16_en.setter
    def reg_rx_pdm_sinc_dsr_16_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_pdm_sinc_dsr_16_en_msb, self.__reg_rx_pdm_sinc_dsr_16_en_lsb, value)

    @property
    def reg_tx_pdm_sigmadelta_in_shift(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_pdm_sigmadelta_in_shift_msb, self.__reg_tx_pdm_sigmadelta_in_shift_lsb)
    @reg_tx_pdm_sigmadelta_in_shift.setter
    def reg_tx_pdm_sigmadelta_in_shift(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_pdm_sigmadelta_in_shift_msb, self.__reg_tx_pdm_sigmadelta_in_shift_lsb, value)

    @property
    def reg_tx_pdm_sinc_in_shift(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_pdm_sinc_in_shift_msb, self.__reg_tx_pdm_sinc_in_shift_lsb)
    @reg_tx_pdm_sinc_in_shift.setter
    def reg_tx_pdm_sinc_in_shift(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_pdm_sinc_in_shift_msb, self.__reg_tx_pdm_sinc_in_shift_lsb, value)

    @property
    def reg_tx_pdm_lp_in_shift(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_pdm_lp_in_shift_msb, self.__reg_tx_pdm_lp_in_shift_lsb)
    @reg_tx_pdm_lp_in_shift.setter
    def reg_tx_pdm_lp_in_shift(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_pdm_lp_in_shift_msb, self.__reg_tx_pdm_lp_in_shift_lsb, value)

    @property
    def reg_tx_pdm_hp_in_shift(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_pdm_hp_in_shift_msb, self.__reg_tx_pdm_hp_in_shift_lsb)
    @reg_tx_pdm_hp_in_shift.setter
    def reg_tx_pdm_hp_in_shift(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_pdm_hp_in_shift_msb, self.__reg_tx_pdm_hp_in_shift_lsb, value)

    @property
    def reg_tx_pdm_prescale(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_pdm_prescale_msb, self.__reg_tx_pdm_prescale_lsb)
    @reg_tx_pdm_prescale.setter
    def reg_tx_pdm_prescale(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_pdm_prescale_msb, self.__reg_tx_pdm_prescale_lsb, value)

    @property
    def reg_tx_pdm_sinc_osr2(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_pdm_sinc_osr2_msb, self.__reg_tx_pdm_sinc_osr2_lsb)
    @reg_tx_pdm_sinc_osr2.setter
    def reg_tx_pdm_sinc_osr2(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_pdm_sinc_osr2_msb, self.__reg_tx_pdm_sinc_osr2_lsb, value)

    @property
    def reg_pdm2pcm_conv_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pdm2pcm_conv_en_msb, self.__reg_pdm2pcm_conv_en_lsb)
    @reg_pdm2pcm_conv_en.setter
    def reg_pdm2pcm_conv_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pdm2pcm_conv_en_msb, self.__reg_pdm2pcm_conv_en_lsb, value)

    @property
    def reg_pcm2pdm_conv_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_pcm2pdm_conv_en_msb, self.__reg_pcm2pdm_conv_en_lsb)
    @reg_pcm2pdm_conv_en.setter
    def reg_pcm2pdm_conv_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_pcm2pdm_conv_en_msb, self.__reg_pcm2pdm_conv_en_lsb, value)

    @property
    def reg_rx_pdm_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_pdm_en_msb, self.__reg_rx_pdm_en_lsb)
    @reg_rx_pdm_en.setter
    def reg_rx_pdm_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_pdm_en_msb, self.__reg_rx_pdm_en_lsb, value)

    @property
    def reg_tx_pdm_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_pdm_en_msb, self.__reg_tx_pdm_en_lsb)
    @reg_tx_pdm_en.setter
    def reg_tx_pdm_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_pdm_en_msb, self.__reg_tx_pdm_en_lsb, value)
class I2S_PDM_FREQ_CONF(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0xb8
        self.__reg_tx_pdm_fp_lsb = 10
        self.__reg_tx_pdm_fp_msb = 19
        self.__reg_tx_pdm_fs_lsb = 0
        self.__reg_tx_pdm_fs_msb = 9
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tx_pdm_fp(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_pdm_fp_msb, self.__reg_tx_pdm_fp_lsb)
    @reg_tx_pdm_fp.setter
    def reg_tx_pdm_fp(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_pdm_fp_msb, self.__reg_tx_pdm_fp_lsb, value)

    @property
    def reg_tx_pdm_fs(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_pdm_fs_msb, self.__reg_tx_pdm_fs_lsb)
    @reg_tx_pdm_fs.setter
    def reg_tx_pdm_fs(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_pdm_fs_msb, self.__reg_tx_pdm_fs_lsb, value)
class I2S_STATE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0xbc
        self.__reg_i2s_tx_idle_lsb = 0
        self.__reg_i2s_tx_idle_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_i2s_tx_idle(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2s_tx_idle_msb, self.__reg_i2s_tx_idle_lsb)
    @reg_i2s_tx_idle.setter
    def reg_i2s_tx_idle(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2s_tx_idle_msb, self.__reg_i2s_tx_idle_lsb, value)
class I2S_DATE(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = I2S_BASE + 0xfc
        self.__reg_i2sdate_lsb = 0
        self.__reg_i2sdate_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_i2sdate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_i2sdate_msb, self.__reg_i2sdate_lsb)
    @reg_i2sdate.setter
    def reg_i2sdate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_i2sdate_msb, self.__reg_i2sdate_lsb, value)
    @property
    def default_value(self):
        return 0x18092900
