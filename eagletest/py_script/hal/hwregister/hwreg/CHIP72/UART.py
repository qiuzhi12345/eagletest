from hal.common import *
from hal.hwregister.hwreg.CHIP72.addr_base import *
class UART(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.UART_FIFO = UART_FIFO(self.channel, self.chipv)
        self.UART_INT_RAW = UART_INT_RAW(self.channel, self.chipv)
        self.UART_INT_ST = UART_INT_ST(self.channel, self.chipv)
        self.UART_INT_ENA = UART_INT_ENA(self.channel, self.chipv)
        self.UART_INT_CLR = UART_INT_CLR(self.channel, self.chipv)
        self.UART_CLKDIV = UART_CLKDIV(self.channel, self.chipv)
        self.UART_AUTOBAUD = UART_AUTOBAUD(self.channel, self.chipv)
        self.UART_STATUS = UART_STATUS(self.channel, self.chipv)
        self.UART_CONF0 = UART_CONF0(self.channel, self.chipv)
        self.UART_CONF1 = UART_CONF1(self.channel, self.chipv)
        self.UART_LOWPULSE = UART_LOWPULSE(self.channel, self.chipv)
        self.UART_HIGHPULSE = UART_HIGHPULSE(self.channel, self.chipv)
        self.UART_RXD_CNT = UART_RXD_CNT(self.channel, self.chipv)
        self.UART_FLOW_CONF = UART_FLOW_CONF(self.channel, self.chipv)
        self.UART_SLEEP_CONF = UART_SLEEP_CONF(self.channel, self.chipv)
        self.UART_SWFC_CONF = UART_SWFC_CONF(self.channel, self.chipv)
        self.UART_IDLE_CONF = UART_IDLE_CONF(self.channel, self.chipv)
        self.UART_RS485_CONF = UART_RS485_CONF(self.channel, self.chipv)
        self.UART_AT_CMD_PRECNT = UART_AT_CMD_PRECNT(self.channel, self.chipv)
        self.UART_AT_CMD_POSTCNT = UART_AT_CMD_POSTCNT(self.channel, self.chipv)
        self.UART_AT_CMD_GAPTOUT = UART_AT_CMD_GAPTOUT(self.channel, self.chipv)
        self.UART_AT_CMD_CHAR = UART_AT_CMD_CHAR(self.channel, self.chipv)
        self.UART_MEM_CONF = UART_MEM_CONF(self.channel, self.chipv)
        self.UART_MEM_TX_STATUS = UART_MEM_TX_STATUS(self.channel, self.chipv)
        self.UART_MEM_RX_STATUS = UART_MEM_RX_STATUS(self.channel, self.chipv)
        self.UART_MEM_CNT_STATUS = UART_MEM_CNT_STATUS(self.channel, self.chipv)
        self.UART_POSPULSE = UART_POSPULSE(self.channel, self.chipv)
        self.UART_NEGPULSE = UART_NEGPULSE(self.channel, self.chipv)
        self.UART_DATE = UART_DATE(self.channel, self.chipv)
        self.UART_ID = UART_ID(self.channel, self.chipv)
class UART_FIFO(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x0
        self.__rxfifo_rd_byte_lsb = 0
        self.__rxfifo_rd_byte_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxfifo_rd_byte(self):
        return self.__MEM.rdm(self.__addr, self.__rxfifo_rd_byte_msb, self.__rxfifo_rd_byte_lsb)
    @rxfifo_rd_byte.setter
    def rxfifo_rd_byte(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxfifo_rd_byte_msb, self.__rxfifo_rd_byte_lsb, value)
class UART_INT_RAW(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x4
        self.__at_cmd_char_det_int_raw_lsb = 18
        self.__at_cmd_char_det_int_raw_msb = 18
        self.__rs485_clash_int_raw_lsb = 17
        self.__rs485_clash_int_raw_msb = 17
        self.__rs485_frm_err_int_raw_lsb = 16
        self.__rs485_frm_err_int_raw_msb = 16
        self.__rs485_parity_err_int_raw_lsb = 15
        self.__rs485_parity_err_int_raw_msb = 15
        self.__tx_done_int_raw_lsb = 14
        self.__tx_done_int_raw_msb = 14
        self.__tx_brk_idle_done_int_raw_lsb = 13
        self.__tx_brk_idle_done_int_raw_msb = 13
        self.__tx_brk_done_int_raw_lsb = 12
        self.__tx_brk_done_int_raw_msb = 12
        self.__glitch_det_int_raw_lsb = 11
        self.__glitch_det_int_raw_msb = 11
        self.__sw_xoff_int_raw_lsb = 10
        self.__sw_xoff_int_raw_msb = 10
        self.__sw_xon_int_raw_lsb = 9
        self.__sw_xon_int_raw_msb = 9
        self.__rxfifo_tout_int_raw_lsb = 8
        self.__rxfifo_tout_int_raw_msb = 8
        self.__brk_det_int_raw_lsb = 7
        self.__brk_det_int_raw_msb = 7
        self.__cts_chg_int_raw_lsb = 6
        self.__cts_chg_int_raw_msb = 6
        self.__dsr_chg_int_raw_lsb = 5
        self.__dsr_chg_int_raw_msb = 5
        self.__rxfifo_ovf_int_raw_lsb = 4
        self.__rxfifo_ovf_int_raw_msb = 4
        self.__frm_err_int_raw_lsb = 3
        self.__frm_err_int_raw_msb = 3
        self.__parity_err_int_raw_lsb = 2
        self.__parity_err_int_raw_msb = 2
        self.__txfifo_empty_int_raw_lsb = 1
        self.__txfifo_empty_int_raw_msb = 1
        self.__rxfifo_full_int_raw_lsb = 0
        self.__rxfifo_full_int_raw_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def at_cmd_char_det_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__at_cmd_char_det_int_raw_msb, self.__at_cmd_char_det_int_raw_lsb)
    @at_cmd_char_det_int_raw.setter
    def at_cmd_char_det_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__at_cmd_char_det_int_raw_msb, self.__at_cmd_char_det_int_raw_lsb, value)

    @property
    def rs485_clash_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rs485_clash_int_raw_msb, self.__rs485_clash_int_raw_lsb)
    @rs485_clash_int_raw.setter
    def rs485_clash_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rs485_clash_int_raw_msb, self.__rs485_clash_int_raw_lsb, value)

    @property
    def rs485_frm_err_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rs485_frm_err_int_raw_msb, self.__rs485_frm_err_int_raw_lsb)
    @rs485_frm_err_int_raw.setter
    def rs485_frm_err_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rs485_frm_err_int_raw_msb, self.__rs485_frm_err_int_raw_lsb, value)

    @property
    def rs485_parity_err_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rs485_parity_err_int_raw_msb, self.__rs485_parity_err_int_raw_lsb)
    @rs485_parity_err_int_raw.setter
    def rs485_parity_err_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rs485_parity_err_int_raw_msb, self.__rs485_parity_err_int_raw_lsb, value)

    @property
    def tx_done_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__tx_done_int_raw_msb, self.__tx_done_int_raw_lsb)
    @tx_done_int_raw.setter
    def tx_done_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__tx_done_int_raw_msb, self.__tx_done_int_raw_lsb, value)

    @property
    def tx_brk_idle_done_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__tx_brk_idle_done_int_raw_msb, self.__tx_brk_idle_done_int_raw_lsb)
    @tx_brk_idle_done_int_raw.setter
    def tx_brk_idle_done_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__tx_brk_idle_done_int_raw_msb, self.__tx_brk_idle_done_int_raw_lsb, value)

    @property
    def tx_brk_done_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__tx_brk_done_int_raw_msb, self.__tx_brk_done_int_raw_lsb)
    @tx_brk_done_int_raw.setter
    def tx_brk_done_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__tx_brk_done_int_raw_msb, self.__tx_brk_done_int_raw_lsb, value)

    @property
    def glitch_det_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__glitch_det_int_raw_msb, self.__glitch_det_int_raw_lsb)
    @glitch_det_int_raw.setter
    def glitch_det_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__glitch_det_int_raw_msb, self.__glitch_det_int_raw_lsb, value)

    @property
    def sw_xoff_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__sw_xoff_int_raw_msb, self.__sw_xoff_int_raw_lsb)
    @sw_xoff_int_raw.setter
    def sw_xoff_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__sw_xoff_int_raw_msb, self.__sw_xoff_int_raw_lsb, value)

    @property
    def sw_xon_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__sw_xon_int_raw_msb, self.__sw_xon_int_raw_lsb)
    @sw_xon_int_raw.setter
    def sw_xon_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__sw_xon_int_raw_msb, self.__sw_xon_int_raw_lsb, value)

    @property
    def rxfifo_tout_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rxfifo_tout_int_raw_msb, self.__rxfifo_tout_int_raw_lsb)
    @rxfifo_tout_int_raw.setter
    def rxfifo_tout_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxfifo_tout_int_raw_msb, self.__rxfifo_tout_int_raw_lsb, value)

    @property
    def brk_det_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__brk_det_int_raw_msb, self.__brk_det_int_raw_lsb)
    @brk_det_int_raw.setter
    def brk_det_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__brk_det_int_raw_msb, self.__brk_det_int_raw_lsb, value)

    @property
    def cts_chg_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__cts_chg_int_raw_msb, self.__cts_chg_int_raw_lsb)
    @cts_chg_int_raw.setter
    def cts_chg_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__cts_chg_int_raw_msb, self.__cts_chg_int_raw_lsb, value)

    @property
    def dsr_chg_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__dsr_chg_int_raw_msb, self.__dsr_chg_int_raw_lsb)
    @dsr_chg_int_raw.setter
    def dsr_chg_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__dsr_chg_int_raw_msb, self.__dsr_chg_int_raw_lsb, value)

    @property
    def rxfifo_ovf_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rxfifo_ovf_int_raw_msb, self.__rxfifo_ovf_int_raw_lsb)
    @rxfifo_ovf_int_raw.setter
    def rxfifo_ovf_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxfifo_ovf_int_raw_msb, self.__rxfifo_ovf_int_raw_lsb, value)

    @property
    def frm_err_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__frm_err_int_raw_msb, self.__frm_err_int_raw_lsb)
    @frm_err_int_raw.setter
    def frm_err_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__frm_err_int_raw_msb, self.__frm_err_int_raw_lsb, value)

    @property
    def parity_err_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__parity_err_int_raw_msb, self.__parity_err_int_raw_lsb)
    @parity_err_int_raw.setter
    def parity_err_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__parity_err_int_raw_msb, self.__parity_err_int_raw_lsb, value)

    @property
    def txfifo_empty_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__txfifo_empty_int_raw_msb, self.__txfifo_empty_int_raw_lsb)
    @txfifo_empty_int_raw.setter
    def txfifo_empty_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__txfifo_empty_int_raw_msb, self.__txfifo_empty_int_raw_lsb, value)

    @property
    def rxfifo_full_int_raw(self):
        return self.__MEM.rdm(self.__addr, self.__rxfifo_full_int_raw_msb, self.__rxfifo_full_int_raw_lsb)
    @rxfifo_full_int_raw.setter
    def rxfifo_full_int_raw(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxfifo_full_int_raw_msb, self.__rxfifo_full_int_raw_lsb, value)
class UART_INT_ST(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x8
        self.__at_cmd_char_det_int_st_lsb = 18
        self.__at_cmd_char_det_int_st_msb = 18
        self.__rs485_clash_int_st_lsb = 17
        self.__rs485_clash_int_st_msb = 17
        self.__rs485_frm_err_int_st_lsb = 16
        self.__rs485_frm_err_int_st_msb = 16
        self.__rs485_parity_err_int_st_lsb = 15
        self.__rs485_parity_err_int_st_msb = 15
        self.__tx_done_int_st_lsb = 14
        self.__tx_done_int_st_msb = 14
        self.__tx_brk_idle_done_int_st_lsb = 13
        self.__tx_brk_idle_done_int_st_msb = 13
        self.__tx_brk_done_int_st_lsb = 12
        self.__tx_brk_done_int_st_msb = 12
        self.__glitch_det_int_st_lsb = 11
        self.__glitch_det_int_st_msb = 11
        self.__sw_xoff_int_st_lsb = 10
        self.__sw_xoff_int_st_msb = 10
        self.__sw_xon_int_st_lsb = 9
        self.__sw_xon_int_st_msb = 9
        self.__rxfifo_tout_int_st_lsb = 8
        self.__rxfifo_tout_int_st_msb = 8
        self.__brk_det_int_st_lsb = 7
        self.__brk_det_int_st_msb = 7
        self.__cts_chg_int_st_lsb = 6
        self.__cts_chg_int_st_msb = 6
        self.__dsr_chg_int_st_lsb = 5
        self.__dsr_chg_int_st_msb = 5
        self.__rxfifo_ovf_int_st_lsb = 4
        self.__rxfifo_ovf_int_st_msb = 4
        self.__frm_err_int_st_lsb = 3
        self.__frm_err_int_st_msb = 3
        self.__parity_err_int_st_lsb = 2
        self.__parity_err_int_st_msb = 2
        self.__txfifo_empty_int_st_lsb = 1
        self.__txfifo_empty_int_st_msb = 1
        self.__rxfifo_full_int_st_lsb = 0
        self.__rxfifo_full_int_st_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def at_cmd_char_det_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__at_cmd_char_det_int_st_msb, self.__at_cmd_char_det_int_st_lsb)
    @at_cmd_char_det_int_st.setter
    def at_cmd_char_det_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__at_cmd_char_det_int_st_msb, self.__at_cmd_char_det_int_st_lsb, value)

    @property
    def rs485_clash_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rs485_clash_int_st_msb, self.__rs485_clash_int_st_lsb)
    @rs485_clash_int_st.setter
    def rs485_clash_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rs485_clash_int_st_msb, self.__rs485_clash_int_st_lsb, value)

    @property
    def rs485_frm_err_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rs485_frm_err_int_st_msb, self.__rs485_frm_err_int_st_lsb)
    @rs485_frm_err_int_st.setter
    def rs485_frm_err_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rs485_frm_err_int_st_msb, self.__rs485_frm_err_int_st_lsb, value)

    @property
    def rs485_parity_err_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rs485_parity_err_int_st_msb, self.__rs485_parity_err_int_st_lsb)
    @rs485_parity_err_int_st.setter
    def rs485_parity_err_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rs485_parity_err_int_st_msb, self.__rs485_parity_err_int_st_lsb, value)

    @property
    def tx_done_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__tx_done_int_st_msb, self.__tx_done_int_st_lsb)
    @tx_done_int_st.setter
    def tx_done_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__tx_done_int_st_msb, self.__tx_done_int_st_lsb, value)

    @property
    def tx_brk_idle_done_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__tx_brk_idle_done_int_st_msb, self.__tx_brk_idle_done_int_st_lsb)
    @tx_brk_idle_done_int_st.setter
    def tx_brk_idle_done_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__tx_brk_idle_done_int_st_msb, self.__tx_brk_idle_done_int_st_lsb, value)

    @property
    def tx_brk_done_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__tx_brk_done_int_st_msb, self.__tx_brk_done_int_st_lsb)
    @tx_brk_done_int_st.setter
    def tx_brk_done_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__tx_brk_done_int_st_msb, self.__tx_brk_done_int_st_lsb, value)

    @property
    def glitch_det_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__glitch_det_int_st_msb, self.__glitch_det_int_st_lsb)
    @glitch_det_int_st.setter
    def glitch_det_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__glitch_det_int_st_msb, self.__glitch_det_int_st_lsb, value)

    @property
    def sw_xoff_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__sw_xoff_int_st_msb, self.__sw_xoff_int_st_lsb)
    @sw_xoff_int_st.setter
    def sw_xoff_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__sw_xoff_int_st_msb, self.__sw_xoff_int_st_lsb, value)

    @property
    def sw_xon_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__sw_xon_int_st_msb, self.__sw_xon_int_st_lsb)
    @sw_xon_int_st.setter
    def sw_xon_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__sw_xon_int_st_msb, self.__sw_xon_int_st_lsb, value)

    @property
    def rxfifo_tout_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rxfifo_tout_int_st_msb, self.__rxfifo_tout_int_st_lsb)
    @rxfifo_tout_int_st.setter
    def rxfifo_tout_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxfifo_tout_int_st_msb, self.__rxfifo_tout_int_st_lsb, value)

    @property
    def brk_det_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__brk_det_int_st_msb, self.__brk_det_int_st_lsb)
    @brk_det_int_st.setter
    def brk_det_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__brk_det_int_st_msb, self.__brk_det_int_st_lsb, value)

    @property
    def cts_chg_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__cts_chg_int_st_msb, self.__cts_chg_int_st_lsb)
    @cts_chg_int_st.setter
    def cts_chg_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__cts_chg_int_st_msb, self.__cts_chg_int_st_lsb, value)

    @property
    def dsr_chg_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__dsr_chg_int_st_msb, self.__dsr_chg_int_st_lsb)
    @dsr_chg_int_st.setter
    def dsr_chg_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__dsr_chg_int_st_msb, self.__dsr_chg_int_st_lsb, value)

    @property
    def rxfifo_ovf_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rxfifo_ovf_int_st_msb, self.__rxfifo_ovf_int_st_lsb)
    @rxfifo_ovf_int_st.setter
    def rxfifo_ovf_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxfifo_ovf_int_st_msb, self.__rxfifo_ovf_int_st_lsb, value)

    @property
    def frm_err_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__frm_err_int_st_msb, self.__frm_err_int_st_lsb)
    @frm_err_int_st.setter
    def frm_err_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__frm_err_int_st_msb, self.__frm_err_int_st_lsb, value)

    @property
    def parity_err_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__parity_err_int_st_msb, self.__parity_err_int_st_lsb)
    @parity_err_int_st.setter
    def parity_err_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__parity_err_int_st_msb, self.__parity_err_int_st_lsb, value)

    @property
    def txfifo_empty_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__txfifo_empty_int_st_msb, self.__txfifo_empty_int_st_lsb)
    @txfifo_empty_int_st.setter
    def txfifo_empty_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__txfifo_empty_int_st_msb, self.__txfifo_empty_int_st_lsb, value)

    @property
    def rxfifo_full_int_st(self):
        return self.__MEM.rdm(self.__addr, self.__rxfifo_full_int_st_msb, self.__rxfifo_full_int_st_lsb)
    @rxfifo_full_int_st.setter
    def rxfifo_full_int_st(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxfifo_full_int_st_msb, self.__rxfifo_full_int_st_lsb, value)
class UART_INT_ENA(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0xc
        self.__at_cmd_char_det_int_ena_lsb = 18
        self.__at_cmd_char_det_int_ena_msb = 18
        self.__rs485_clash_int_ena_lsb = 17
        self.__rs485_clash_int_ena_msb = 17
        self.__rs485_frm_err_int_ena_lsb = 16
        self.__rs485_frm_err_int_ena_msb = 16
        self.__rs485_parity_err_int_ena_lsb = 15
        self.__rs485_parity_err_int_ena_msb = 15
        self.__tx_done_int_ena_lsb = 14
        self.__tx_done_int_ena_msb = 14
        self.__tx_brk_idle_done_int_ena_lsb = 13
        self.__tx_brk_idle_done_int_ena_msb = 13
        self.__tx_brk_done_int_ena_lsb = 12
        self.__tx_brk_done_int_ena_msb = 12
        self.__glitch_det_int_ena_lsb = 11
        self.__glitch_det_int_ena_msb = 11
        self.__sw_xoff_int_ena_lsb = 10
        self.__sw_xoff_int_ena_msb = 10
        self.__sw_xon_int_ena_lsb = 9
        self.__sw_xon_int_ena_msb = 9
        self.__rxfifo_tout_int_ena_lsb = 8
        self.__rxfifo_tout_int_ena_msb = 8
        self.__brk_det_int_ena_lsb = 7
        self.__brk_det_int_ena_msb = 7
        self.__cts_chg_int_ena_lsb = 6
        self.__cts_chg_int_ena_msb = 6
        self.__dsr_chg_int_ena_lsb = 5
        self.__dsr_chg_int_ena_msb = 5
        self.__rxfifo_ovf_int_ena_lsb = 4
        self.__rxfifo_ovf_int_ena_msb = 4
        self.__frm_err_int_ena_lsb = 3
        self.__frm_err_int_ena_msb = 3
        self.__parity_err_int_ena_lsb = 2
        self.__parity_err_int_ena_msb = 2
        self.__txfifo_empty_int_ena_lsb = 1
        self.__txfifo_empty_int_ena_msb = 1
        self.__rxfifo_full_int_ena_lsb = 0
        self.__rxfifo_full_int_ena_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def at_cmd_char_det_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__at_cmd_char_det_int_ena_msb, self.__at_cmd_char_det_int_ena_lsb)
    @at_cmd_char_det_int_ena.setter
    def at_cmd_char_det_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__at_cmd_char_det_int_ena_msb, self.__at_cmd_char_det_int_ena_lsb, value)

    @property
    def rs485_clash_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rs485_clash_int_ena_msb, self.__rs485_clash_int_ena_lsb)
    @rs485_clash_int_ena.setter
    def rs485_clash_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rs485_clash_int_ena_msb, self.__rs485_clash_int_ena_lsb, value)

    @property
    def rs485_frm_err_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rs485_frm_err_int_ena_msb, self.__rs485_frm_err_int_ena_lsb)
    @rs485_frm_err_int_ena.setter
    def rs485_frm_err_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rs485_frm_err_int_ena_msb, self.__rs485_frm_err_int_ena_lsb, value)

    @property
    def rs485_parity_err_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rs485_parity_err_int_ena_msb, self.__rs485_parity_err_int_ena_lsb)
    @rs485_parity_err_int_ena.setter
    def rs485_parity_err_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rs485_parity_err_int_ena_msb, self.__rs485_parity_err_int_ena_lsb, value)

    @property
    def tx_done_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__tx_done_int_ena_msb, self.__tx_done_int_ena_lsb)
    @tx_done_int_ena.setter
    def tx_done_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__tx_done_int_ena_msb, self.__tx_done_int_ena_lsb, value)

    @property
    def tx_brk_idle_done_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__tx_brk_idle_done_int_ena_msb, self.__tx_brk_idle_done_int_ena_lsb)
    @tx_brk_idle_done_int_ena.setter
    def tx_brk_idle_done_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__tx_brk_idle_done_int_ena_msb, self.__tx_brk_idle_done_int_ena_lsb, value)

    @property
    def tx_brk_done_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__tx_brk_done_int_ena_msb, self.__tx_brk_done_int_ena_lsb)
    @tx_brk_done_int_ena.setter
    def tx_brk_done_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__tx_brk_done_int_ena_msb, self.__tx_brk_done_int_ena_lsb, value)

    @property
    def glitch_det_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__glitch_det_int_ena_msb, self.__glitch_det_int_ena_lsb)
    @glitch_det_int_ena.setter
    def glitch_det_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__glitch_det_int_ena_msb, self.__glitch_det_int_ena_lsb, value)

    @property
    def sw_xoff_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__sw_xoff_int_ena_msb, self.__sw_xoff_int_ena_lsb)
    @sw_xoff_int_ena.setter
    def sw_xoff_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__sw_xoff_int_ena_msb, self.__sw_xoff_int_ena_lsb, value)

    @property
    def sw_xon_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__sw_xon_int_ena_msb, self.__sw_xon_int_ena_lsb)
    @sw_xon_int_ena.setter
    def sw_xon_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__sw_xon_int_ena_msb, self.__sw_xon_int_ena_lsb, value)

    @property
    def rxfifo_tout_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rxfifo_tout_int_ena_msb, self.__rxfifo_tout_int_ena_lsb)
    @rxfifo_tout_int_ena.setter
    def rxfifo_tout_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxfifo_tout_int_ena_msb, self.__rxfifo_tout_int_ena_lsb, value)

    @property
    def brk_det_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__brk_det_int_ena_msb, self.__brk_det_int_ena_lsb)
    @brk_det_int_ena.setter
    def brk_det_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__brk_det_int_ena_msb, self.__brk_det_int_ena_lsb, value)

    @property
    def cts_chg_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__cts_chg_int_ena_msb, self.__cts_chg_int_ena_lsb)
    @cts_chg_int_ena.setter
    def cts_chg_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__cts_chg_int_ena_msb, self.__cts_chg_int_ena_lsb, value)

    @property
    def dsr_chg_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__dsr_chg_int_ena_msb, self.__dsr_chg_int_ena_lsb)
    @dsr_chg_int_ena.setter
    def dsr_chg_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__dsr_chg_int_ena_msb, self.__dsr_chg_int_ena_lsb, value)

    @property
    def rxfifo_ovf_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rxfifo_ovf_int_ena_msb, self.__rxfifo_ovf_int_ena_lsb)
    @rxfifo_ovf_int_ena.setter
    def rxfifo_ovf_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxfifo_ovf_int_ena_msb, self.__rxfifo_ovf_int_ena_lsb, value)

    @property
    def frm_err_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__frm_err_int_ena_msb, self.__frm_err_int_ena_lsb)
    @frm_err_int_ena.setter
    def frm_err_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__frm_err_int_ena_msb, self.__frm_err_int_ena_lsb, value)

    @property
    def parity_err_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__parity_err_int_ena_msb, self.__parity_err_int_ena_lsb)
    @parity_err_int_ena.setter
    def parity_err_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__parity_err_int_ena_msb, self.__parity_err_int_ena_lsb, value)

    @property
    def txfifo_empty_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__txfifo_empty_int_ena_msb, self.__txfifo_empty_int_ena_lsb)
    @txfifo_empty_int_ena.setter
    def txfifo_empty_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__txfifo_empty_int_ena_msb, self.__txfifo_empty_int_ena_lsb, value)

    @property
    def rxfifo_full_int_ena(self):
        return self.__MEM.rdm(self.__addr, self.__rxfifo_full_int_ena_msb, self.__rxfifo_full_int_ena_lsb)
    @rxfifo_full_int_ena.setter
    def rxfifo_full_int_ena(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxfifo_full_int_ena_msb, self.__rxfifo_full_int_ena_lsb, value)
class UART_INT_CLR(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x10
        self.__at_cmd_char_det_int_clr_lsb = 18
        self.__at_cmd_char_det_int_clr_msb = 18
        self.__rs485_clash_int_clr_lsb = 17
        self.__rs485_clash_int_clr_msb = 17
        self.__rs485_frm_err_int_clr_lsb = 16
        self.__rs485_frm_err_int_clr_msb = 16
        self.__rs485_parity_err_int_clr_lsb = 15
        self.__rs485_parity_err_int_clr_msb = 15
        self.__tx_done_int_clr_lsb = 14
        self.__tx_done_int_clr_msb = 14
        self.__tx_brk_idle_done_int_clr_lsb = 13
        self.__tx_brk_idle_done_int_clr_msb = 13
        self.__tx_brk_done_int_clr_lsb = 12
        self.__tx_brk_done_int_clr_msb = 12
        self.__glitch_det_int_clr_lsb = 11
        self.__glitch_det_int_clr_msb = 11
        self.__sw_xoff_int_clr_lsb = 10
        self.__sw_xoff_int_clr_msb = 10
        self.__sw_xon_int_clr_lsb = 9
        self.__sw_xon_int_clr_msb = 9
        self.__rxfifo_tout_int_clr_lsb = 8
        self.__rxfifo_tout_int_clr_msb = 8
        self.__brk_det_int_clr_lsb = 7
        self.__brk_det_int_clr_msb = 7
        self.__cts_chg_int_clr_lsb = 6
        self.__cts_chg_int_clr_msb = 6
        self.__dsr_chg_int_clr_lsb = 5
        self.__dsr_chg_int_clr_msb = 5
        self.__rxfifo_ovf_int_clr_lsb = 4
        self.__rxfifo_ovf_int_clr_msb = 4
        self.__frm_err_int_clr_lsb = 3
        self.__frm_err_int_clr_msb = 3
        self.__parity_err_int_clr_lsb = 2
        self.__parity_err_int_clr_msb = 2
        self.__txfifo_empty_int_clr_lsb = 1
        self.__txfifo_empty_int_clr_msb = 1
        self.__rxfifo_full_int_clr_lsb = 0
        self.__rxfifo_full_int_clr_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def at_cmd_char_det_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__at_cmd_char_det_int_clr_msb, self.__at_cmd_char_det_int_clr_lsb)
    @at_cmd_char_det_int_clr.setter
    def at_cmd_char_det_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__at_cmd_char_det_int_clr_msb, self.__at_cmd_char_det_int_clr_lsb, value)

    @property
    def rs485_clash_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rs485_clash_int_clr_msb, self.__rs485_clash_int_clr_lsb)
    @rs485_clash_int_clr.setter
    def rs485_clash_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rs485_clash_int_clr_msb, self.__rs485_clash_int_clr_lsb, value)

    @property
    def rs485_frm_err_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rs485_frm_err_int_clr_msb, self.__rs485_frm_err_int_clr_lsb)
    @rs485_frm_err_int_clr.setter
    def rs485_frm_err_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rs485_frm_err_int_clr_msb, self.__rs485_frm_err_int_clr_lsb, value)

    @property
    def rs485_parity_err_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rs485_parity_err_int_clr_msb, self.__rs485_parity_err_int_clr_lsb)
    @rs485_parity_err_int_clr.setter
    def rs485_parity_err_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rs485_parity_err_int_clr_msb, self.__rs485_parity_err_int_clr_lsb, value)

    @property
    def tx_done_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__tx_done_int_clr_msb, self.__tx_done_int_clr_lsb)
    @tx_done_int_clr.setter
    def tx_done_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__tx_done_int_clr_msb, self.__tx_done_int_clr_lsb, value)

    @property
    def tx_brk_idle_done_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__tx_brk_idle_done_int_clr_msb, self.__tx_brk_idle_done_int_clr_lsb)
    @tx_brk_idle_done_int_clr.setter
    def tx_brk_idle_done_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__tx_brk_idle_done_int_clr_msb, self.__tx_brk_idle_done_int_clr_lsb, value)

    @property
    def tx_brk_done_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__tx_brk_done_int_clr_msb, self.__tx_brk_done_int_clr_lsb)
    @tx_brk_done_int_clr.setter
    def tx_brk_done_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__tx_brk_done_int_clr_msb, self.__tx_brk_done_int_clr_lsb, value)

    @property
    def glitch_det_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__glitch_det_int_clr_msb, self.__glitch_det_int_clr_lsb)
    @glitch_det_int_clr.setter
    def glitch_det_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__glitch_det_int_clr_msb, self.__glitch_det_int_clr_lsb, value)

    @property
    def sw_xoff_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__sw_xoff_int_clr_msb, self.__sw_xoff_int_clr_lsb)
    @sw_xoff_int_clr.setter
    def sw_xoff_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__sw_xoff_int_clr_msb, self.__sw_xoff_int_clr_lsb, value)

    @property
    def sw_xon_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__sw_xon_int_clr_msb, self.__sw_xon_int_clr_lsb)
    @sw_xon_int_clr.setter
    def sw_xon_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__sw_xon_int_clr_msb, self.__sw_xon_int_clr_lsb, value)

    @property
    def rxfifo_tout_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rxfifo_tout_int_clr_msb, self.__rxfifo_tout_int_clr_lsb)
    @rxfifo_tout_int_clr.setter
    def rxfifo_tout_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxfifo_tout_int_clr_msb, self.__rxfifo_tout_int_clr_lsb, value)

    @property
    def brk_det_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__brk_det_int_clr_msb, self.__brk_det_int_clr_lsb)
    @brk_det_int_clr.setter
    def brk_det_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__brk_det_int_clr_msb, self.__brk_det_int_clr_lsb, value)

    @property
    def cts_chg_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__cts_chg_int_clr_msb, self.__cts_chg_int_clr_lsb)
    @cts_chg_int_clr.setter
    def cts_chg_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__cts_chg_int_clr_msb, self.__cts_chg_int_clr_lsb, value)

    @property
    def dsr_chg_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__dsr_chg_int_clr_msb, self.__dsr_chg_int_clr_lsb)
    @dsr_chg_int_clr.setter
    def dsr_chg_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__dsr_chg_int_clr_msb, self.__dsr_chg_int_clr_lsb, value)

    @property
    def rxfifo_ovf_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rxfifo_ovf_int_clr_msb, self.__rxfifo_ovf_int_clr_lsb)
    @rxfifo_ovf_int_clr.setter
    def rxfifo_ovf_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxfifo_ovf_int_clr_msb, self.__rxfifo_ovf_int_clr_lsb, value)

    @property
    def frm_err_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__frm_err_int_clr_msb, self.__frm_err_int_clr_lsb)
    @frm_err_int_clr.setter
    def frm_err_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__frm_err_int_clr_msb, self.__frm_err_int_clr_lsb, value)

    @property
    def parity_err_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__parity_err_int_clr_msb, self.__parity_err_int_clr_lsb)
    @parity_err_int_clr.setter
    def parity_err_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__parity_err_int_clr_msb, self.__parity_err_int_clr_lsb, value)

    @property
    def txfifo_empty_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__txfifo_empty_int_clr_msb, self.__txfifo_empty_int_clr_lsb)
    @txfifo_empty_int_clr.setter
    def txfifo_empty_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__txfifo_empty_int_clr_msb, self.__txfifo_empty_int_clr_lsb, value)

    @property
    def rxfifo_full_int_clr(self):
        return self.__MEM.rdm(self.__addr, self.__rxfifo_full_int_clr_msb, self.__rxfifo_full_int_clr_lsb)
    @rxfifo_full_int_clr.setter
    def rxfifo_full_int_clr(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxfifo_full_int_clr_msb, self.__rxfifo_full_int_clr_lsb, value)
class UART_CLKDIV(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x14
        self.__uart_clkdiv_frag_lsb = 20
        self.__uart_clkdiv_frag_msb = 23
        self.__uart_clkdiv_lsb = 0
        self.__uart_clkdiv_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def uart_clkdiv_frag(self):
        return self.__MEM.rdm(self.__addr, self.__uart_clkdiv_frag_msb, self.__uart_clkdiv_frag_lsb)
    @uart_clkdiv_frag.setter
    def uart_clkdiv_frag(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_clkdiv_frag_msb, self.__uart_clkdiv_frag_lsb, value)

    @property
    def uart_clkdiv(self):
        return self.__MEM.rdm(self.__addr, self.__uart_clkdiv_msb, self.__uart_clkdiv_lsb)
    @uart_clkdiv.setter
    def uart_clkdiv(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_clkdiv_msb, self.__uart_clkdiv_lsb, value)
class UART_AUTOBAUD(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x18
        self.__glitch_filt_lsb = 8
        self.__glitch_filt_msb = 15
        self.__autobaud_en_lsb = 0
        self.__autobaud_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def glitch_filt(self):
        return self.__MEM.rdm(self.__addr, self.__glitch_filt_msb, self.__glitch_filt_lsb)
    @glitch_filt.setter
    def glitch_filt(self, value):
        return self.__MEM.wrm(self.__addr, self.__glitch_filt_msb, self.__glitch_filt_lsb, value)

    @property
    def autobaud_en(self):
        return self.__MEM.rdm(self.__addr, self.__autobaud_en_msb, self.__autobaud_en_lsb)
    @autobaud_en.setter
    def autobaud_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__autobaud_en_msb, self.__autobaud_en_lsb, value)
class UART_STATUS(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x1c
        self.__txd_lsb = 31
        self.__txd_msb = 31
        self.__rtsn_lsb = 30
        self.__rtsn_msb = 30
        self.__dtrn_lsb = 29
        self.__dtrn_msb = 29
        self.__st_utx_out_lsb = 24
        self.__st_utx_out_msb = 27
        self.__txfifo_cnt_lsb = 16
        self.__txfifo_cnt_msb = 23
        self.__rxd_lsb = 15
        self.__rxd_msb = 15
        self.__ctsn_lsb = 14
        self.__ctsn_msb = 14
        self.__dsrn_lsb = 13
        self.__dsrn_msb = 13
        self.__st_urx_out_lsb = 8
        self.__st_urx_out_msb = 11
        self.__rxfifo_cnt_lsb = 0
        self.__rxfifo_cnt_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txd(self):
        return self.__MEM.rdm(self.__addr, self.__txd_msb, self.__txd_lsb)
    @txd.setter
    def txd(self, value):
        return self.__MEM.wrm(self.__addr, self.__txd_msb, self.__txd_lsb, value)

    @property
    def rtsn(self):
        return self.__MEM.rdm(self.__addr, self.__rtsn_msb, self.__rtsn_lsb)
    @rtsn.setter
    def rtsn(self, value):
        return self.__MEM.wrm(self.__addr, self.__rtsn_msb, self.__rtsn_lsb, value)

    @property
    def dtrn(self):
        return self.__MEM.rdm(self.__addr, self.__dtrn_msb, self.__dtrn_lsb)
    @dtrn.setter
    def dtrn(self, value):
        return self.__MEM.wrm(self.__addr, self.__dtrn_msb, self.__dtrn_lsb, value)

    @property
    def st_utx_out(self):
        return self.__MEM.rdm(self.__addr, self.__st_utx_out_msb, self.__st_utx_out_lsb)
    @st_utx_out.setter
    def st_utx_out(self, value):
        return self.__MEM.wrm(self.__addr, self.__st_utx_out_msb, self.__st_utx_out_lsb, value)

    @property
    def txfifo_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__txfifo_cnt_msb, self.__txfifo_cnt_lsb)
    @txfifo_cnt.setter
    def txfifo_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__txfifo_cnt_msb, self.__txfifo_cnt_lsb, value)

    @property
    def rxd(self):
        return self.__MEM.rdm(self.__addr, self.__rxd_msb, self.__rxd_lsb)
    @rxd.setter
    def rxd(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxd_msb, self.__rxd_lsb, value)

    @property
    def ctsn(self):
        return self.__MEM.rdm(self.__addr, self.__ctsn_msb, self.__ctsn_lsb)
    @ctsn.setter
    def ctsn(self, value):
        return self.__MEM.wrm(self.__addr, self.__ctsn_msb, self.__ctsn_lsb, value)

    @property
    def dsrn(self):
        return self.__MEM.rdm(self.__addr, self.__dsrn_msb, self.__dsrn_lsb)
    @dsrn.setter
    def dsrn(self, value):
        return self.__MEM.wrm(self.__addr, self.__dsrn_msb, self.__dsrn_lsb, value)

    @property
    def st_urx_out(self):
        return self.__MEM.rdm(self.__addr, self.__st_urx_out_msb, self.__st_urx_out_lsb)
    @st_urx_out.setter
    def st_urx_out(self, value):
        return self.__MEM.wrm(self.__addr, self.__st_urx_out_msb, self.__st_urx_out_lsb, value)

    @property
    def rxfifo_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rxfifo_cnt_msb, self.__rxfifo_cnt_lsb)
    @rxfifo_cnt.setter
    def rxfifo_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxfifo_cnt_msb, self.__rxfifo_cnt_lsb, value)
class UART_CONF0(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x20
        self.__uart_tick_ref_always_on_lsb = 27
        self.__uart_tick_ref_always_on_msb = 27
        self.__uart_err_wr_mask_lsb = 26
        self.__uart_err_wr_mask_msb = 26
        self.__reg_clk_en_lsb = 25
        self.__reg_clk_en_msb = 25
        self.__uart_dtr_inv_lsb = 24
        self.__uart_dtr_inv_msb = 24
        self.__uart_rts_inv_lsb = 23
        self.__uart_rts_inv_msb = 23
        self.__uart_txd_inv_lsb = 22
        self.__uart_txd_inv_msb = 22
        self.__uart_dsr_inv_lsb = 21
        self.__uart_dsr_inv_msb = 21
        self.__uart_cts_inv_lsb = 20
        self.__uart_cts_inv_msb = 20
        self.__uart_rxd_inv_lsb = 19
        self.__uart_rxd_inv_msb = 19
        self.__txfifo_rst_lsb = 18
        self.__txfifo_rst_msb = 18
        self.__rxfifo_rst_lsb = 17
        self.__rxfifo_rst_msb = 17
        self.__irda_en_lsb = 16
        self.__irda_en_msb = 16
        self.__tx_flow_en_lsb = 15
        self.__tx_flow_en_msb = 15
        self.__uart_loopback_lsb = 14
        self.__uart_loopback_msb = 14
        self.__irda_rx_inv_lsb = 13
        self.__irda_rx_inv_msb = 13
        self.__irda_tx_inv_lsb = 12
        self.__irda_tx_inv_msb = 12
        self.__irda_wctl_lsb = 11
        self.__irda_wctl_msb = 11
        self.__irda_tx_en_lsb = 10
        self.__irda_tx_en_msb = 10
        self.__irda_dplx_lsb = 9
        self.__irda_dplx_msb = 9
        self.__txd_brk_lsb = 8
        self.__txd_brk_msb = 8
        self.__sw_dtr_lsb = 7
        self.__sw_dtr_msb = 7
        self.__sw_rts_lsb = 6
        self.__sw_rts_msb = 6
        self.__stop_bit_num_lsb = 4
        self.__stop_bit_num_msb = 5
        self.__bit_num_lsb = 2
        self.__bit_num_msb = 3
        self.__parity_en_lsb = 1
        self.__parity_en_msb = 1
        self.__parity_lsb = 0
        self.__parity_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def uart_tick_ref_always_on(self):
        return self.__MEM.rdm(self.__addr, self.__uart_tick_ref_always_on_msb, self.__uart_tick_ref_always_on_lsb)
    @uart_tick_ref_always_on.setter
    def uart_tick_ref_always_on(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_tick_ref_always_on_msb, self.__uart_tick_ref_always_on_lsb, value)

    @property
    def uart_err_wr_mask(self):
        return self.__MEM.rdm(self.__addr, self.__uart_err_wr_mask_msb, self.__uart_err_wr_mask_lsb)
    @uart_err_wr_mask.setter
    def uart_err_wr_mask(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_err_wr_mask_msb, self.__uart_err_wr_mask_lsb, value)

    @property
    def reg_clk_en(self):
        return self.__MEM.rdm(self.__addr, self.__reg_clk_en_msb, self.__reg_clk_en_lsb)
    @reg_clk_en.setter
    def reg_clk_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_clk_en_msb, self.__reg_clk_en_lsb, value)

    @property
    def uart_dtr_inv(self):
        return self.__MEM.rdm(self.__addr, self.__uart_dtr_inv_msb, self.__uart_dtr_inv_lsb)
    @uart_dtr_inv.setter
    def uart_dtr_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_dtr_inv_msb, self.__uart_dtr_inv_lsb, value)

    @property
    def uart_rts_inv(self):
        return self.__MEM.rdm(self.__addr, self.__uart_rts_inv_msb, self.__uart_rts_inv_lsb)
    @uart_rts_inv.setter
    def uart_rts_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_rts_inv_msb, self.__uart_rts_inv_lsb, value)

    @property
    def uart_txd_inv(self):
        return self.__MEM.rdm(self.__addr, self.__uart_txd_inv_msb, self.__uart_txd_inv_lsb)
    @uart_txd_inv.setter
    def uart_txd_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_txd_inv_msb, self.__uart_txd_inv_lsb, value)

    @property
    def uart_dsr_inv(self):
        return self.__MEM.rdm(self.__addr, self.__uart_dsr_inv_msb, self.__uart_dsr_inv_lsb)
    @uart_dsr_inv.setter
    def uart_dsr_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_dsr_inv_msb, self.__uart_dsr_inv_lsb, value)

    @property
    def uart_cts_inv(self):
        return self.__MEM.rdm(self.__addr, self.__uart_cts_inv_msb, self.__uart_cts_inv_lsb)
    @uart_cts_inv.setter
    def uart_cts_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_cts_inv_msb, self.__uart_cts_inv_lsb, value)

    @property
    def uart_rxd_inv(self):
        return self.__MEM.rdm(self.__addr, self.__uart_rxd_inv_msb, self.__uart_rxd_inv_lsb)
    @uart_rxd_inv.setter
    def uart_rxd_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_rxd_inv_msb, self.__uart_rxd_inv_lsb, value)

    @property
    def txfifo_rst(self):
        return self.__MEM.rdm(self.__addr, self.__txfifo_rst_msb, self.__txfifo_rst_lsb)
    @txfifo_rst.setter
    def txfifo_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__txfifo_rst_msb, self.__txfifo_rst_lsb, value)

    @property
    def rxfifo_rst(self):
        return self.__MEM.rdm(self.__addr, self.__rxfifo_rst_msb, self.__rxfifo_rst_lsb)
    @rxfifo_rst.setter
    def rxfifo_rst(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxfifo_rst_msb, self.__rxfifo_rst_lsb, value)

    @property
    def irda_en(self):
        return self.__MEM.rdm(self.__addr, self.__irda_en_msb, self.__irda_en_lsb)
    @irda_en.setter
    def irda_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__irda_en_msb, self.__irda_en_lsb, value)

    @property
    def tx_flow_en(self):
        return self.__MEM.rdm(self.__addr, self.__tx_flow_en_msb, self.__tx_flow_en_lsb)
    @tx_flow_en.setter
    def tx_flow_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__tx_flow_en_msb, self.__tx_flow_en_lsb, value)

    @property
    def uart_loopback(self):
        return self.__MEM.rdm(self.__addr, self.__uart_loopback_msb, self.__uart_loopback_lsb)
    @uart_loopback.setter
    def uart_loopback(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_loopback_msb, self.__uart_loopback_lsb, value)

    @property
    def irda_rx_inv(self):
        return self.__MEM.rdm(self.__addr, self.__irda_rx_inv_msb, self.__irda_rx_inv_lsb)
    @irda_rx_inv.setter
    def irda_rx_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__irda_rx_inv_msb, self.__irda_rx_inv_lsb, value)

    @property
    def irda_tx_inv(self):
        return self.__MEM.rdm(self.__addr, self.__irda_tx_inv_msb, self.__irda_tx_inv_lsb)
    @irda_tx_inv.setter
    def irda_tx_inv(self, value):
        return self.__MEM.wrm(self.__addr, self.__irda_tx_inv_msb, self.__irda_tx_inv_lsb, value)

    @property
    def irda_wctl(self):
        return self.__MEM.rdm(self.__addr, self.__irda_wctl_msb, self.__irda_wctl_lsb)
    @irda_wctl.setter
    def irda_wctl(self, value):
        return self.__MEM.wrm(self.__addr, self.__irda_wctl_msb, self.__irda_wctl_lsb, value)

    @property
    def irda_tx_en(self):
        return self.__MEM.rdm(self.__addr, self.__irda_tx_en_msb, self.__irda_tx_en_lsb)
    @irda_tx_en.setter
    def irda_tx_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__irda_tx_en_msb, self.__irda_tx_en_lsb, value)

    @property
    def irda_dplx(self):
        return self.__MEM.rdm(self.__addr, self.__irda_dplx_msb, self.__irda_dplx_lsb)
    @irda_dplx.setter
    def irda_dplx(self, value):
        return self.__MEM.wrm(self.__addr, self.__irda_dplx_msb, self.__irda_dplx_lsb, value)

    @property
    def txd_brk(self):
        return self.__MEM.rdm(self.__addr, self.__txd_brk_msb, self.__txd_brk_lsb)
    @txd_brk.setter
    def txd_brk(self, value):
        return self.__MEM.wrm(self.__addr, self.__txd_brk_msb, self.__txd_brk_lsb, value)

    @property
    def sw_dtr(self):
        return self.__MEM.rdm(self.__addr, self.__sw_dtr_msb, self.__sw_dtr_lsb)
    @sw_dtr.setter
    def sw_dtr(self, value):
        return self.__MEM.wrm(self.__addr, self.__sw_dtr_msb, self.__sw_dtr_lsb, value)

    @property
    def sw_rts(self):
        return self.__MEM.rdm(self.__addr, self.__sw_rts_msb, self.__sw_rts_lsb)
    @sw_rts.setter
    def sw_rts(self, value):
        return self.__MEM.wrm(self.__addr, self.__sw_rts_msb, self.__sw_rts_lsb, value)

    @property
    def stop_bit_num(self):
        return self.__MEM.rdm(self.__addr, self.__stop_bit_num_msb, self.__stop_bit_num_lsb)
    @stop_bit_num.setter
    def stop_bit_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__stop_bit_num_msb, self.__stop_bit_num_lsb, value)

    @property
    def bit_num(self):
        return self.__MEM.rdm(self.__addr, self.__bit_num_msb, self.__bit_num_lsb)
    @bit_num.setter
    def bit_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__bit_num_msb, self.__bit_num_lsb, value)

    @property
    def parity_en(self):
        return self.__MEM.rdm(self.__addr, self.__parity_en_msb, self.__parity_en_lsb)
    @parity_en.setter
    def parity_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__parity_en_msb, self.__parity_en_lsb, value)

    @property
    def parity(self):
        return self.__MEM.rdm(self.__addr, self.__parity_msb, self.__parity_lsb)
    @parity.setter
    def parity(self, value):
        return self.__MEM.wrm(self.__addr, self.__parity_msb, self.__parity_lsb, value)
class UART_CONF1(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x24
        self.__rx_tout_en_lsb = 31
        self.__rx_tout_en_msb = 31
        self.__rx_tout_thrhd_lsb = 24
        self.__rx_tout_thrhd_msb = 30
        self.__rx_flow_en_lsb = 23
        self.__rx_flow_en_msb = 23
        self.__rx_flow_thrhd_lsb = 16
        self.__rx_flow_thrhd_msb = 22
        self.__txfifo_empty_thrhd_lsb = 8
        self.__txfifo_empty_thrhd_msb = 14
        self.__rxfifo_full_thrhd_lsb = 0
        self.__rxfifo_full_thrhd_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rx_tout_en(self):
        return self.__MEM.rdm(self.__addr, self.__rx_tout_en_msb, self.__rx_tout_en_lsb)
    @rx_tout_en.setter
    def rx_tout_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_tout_en_msb, self.__rx_tout_en_lsb, value)

    @property
    def rx_tout_thrhd(self):
        return self.__MEM.rdm(self.__addr, self.__rx_tout_thrhd_msb, self.__rx_tout_thrhd_lsb)
    @rx_tout_thrhd.setter
    def rx_tout_thrhd(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_tout_thrhd_msb, self.__rx_tout_thrhd_lsb, value)

    @property
    def rx_flow_en(self):
        return self.__MEM.rdm(self.__addr, self.__rx_flow_en_msb, self.__rx_flow_en_lsb)
    @rx_flow_en.setter
    def rx_flow_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_flow_en_msb, self.__rx_flow_en_lsb, value)

    @property
    def rx_flow_thrhd(self):
        return self.__MEM.rdm(self.__addr, self.__rx_flow_thrhd_msb, self.__rx_flow_thrhd_lsb)
    @rx_flow_thrhd.setter
    def rx_flow_thrhd(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_flow_thrhd_msb, self.__rx_flow_thrhd_lsb, value)

    @property
    def txfifo_empty_thrhd(self):
        return self.__MEM.rdm(self.__addr, self.__txfifo_empty_thrhd_msb, self.__txfifo_empty_thrhd_lsb)
    @txfifo_empty_thrhd.setter
    def txfifo_empty_thrhd(self, value):
        return self.__MEM.wrm(self.__addr, self.__txfifo_empty_thrhd_msb, self.__txfifo_empty_thrhd_lsb, value)

    @property
    def rxfifo_full_thrhd(self):
        return self.__MEM.rdm(self.__addr, self.__rxfifo_full_thrhd_msb, self.__rxfifo_full_thrhd_lsb)
    @rxfifo_full_thrhd.setter
    def rxfifo_full_thrhd(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxfifo_full_thrhd_msb, self.__rxfifo_full_thrhd_lsb, value)
class UART_LOWPULSE(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x28
        self.__lowpulse_min_cnt_lsb = 0
        self.__lowpulse_min_cnt_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def lowpulse_min_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__lowpulse_min_cnt_msb, self.__lowpulse_min_cnt_lsb)
    @lowpulse_min_cnt.setter
    def lowpulse_min_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__lowpulse_min_cnt_msb, self.__lowpulse_min_cnt_lsb, value)
class UART_HIGHPULSE(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x2c
        self.__highpulse_min_cnt_lsb = 0
        self.__highpulse_min_cnt_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def highpulse_min_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__highpulse_min_cnt_msb, self.__highpulse_min_cnt_lsb)
    @highpulse_min_cnt.setter
    def highpulse_min_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__highpulse_min_cnt_msb, self.__highpulse_min_cnt_lsb, value)
class UART_RXD_CNT(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x30
        self.__rxd_edge_cnt_lsb = 0
        self.__rxd_edge_cnt_msb = 9
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rxd_edge_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rxd_edge_cnt_msb, self.__rxd_edge_cnt_lsb)
    @rxd_edge_cnt.setter
    def rxd_edge_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rxd_edge_cnt_msb, self.__rxd_edge_cnt_lsb, value)
class UART_FLOW_CONF(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x34
        self.__uart_send_xoff_lsb = 5
        self.__uart_send_xoff_msb = 5
        self.__uart_send_xon_lsb = 4
        self.__uart_send_xon_msb = 4
        self.__uart_force_xoff_lsb = 3
        self.__uart_force_xoff_msb = 3
        self.__uart_force_xon_lsb = 2
        self.__uart_force_xon_msb = 2
        self.__uart_xonoff_del_lsb = 1
        self.__uart_xonoff_del_msb = 1
        self.__uart_sw_flow_con_en_lsb = 0
        self.__uart_sw_flow_con_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def uart_send_xoff(self):
        return self.__MEM.rdm(self.__addr, self.__uart_send_xoff_msb, self.__uart_send_xoff_lsb)
    @uart_send_xoff.setter
    def uart_send_xoff(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_send_xoff_msb, self.__uart_send_xoff_lsb, value)

    @property
    def uart_send_xon(self):
        return self.__MEM.rdm(self.__addr, self.__uart_send_xon_msb, self.__uart_send_xon_lsb)
    @uart_send_xon.setter
    def uart_send_xon(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_send_xon_msb, self.__uart_send_xon_lsb, value)

    @property
    def uart_force_xoff(self):
        return self.__MEM.rdm(self.__addr, self.__uart_force_xoff_msb, self.__uart_force_xoff_lsb)
    @uart_force_xoff.setter
    def uart_force_xoff(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_force_xoff_msb, self.__uart_force_xoff_lsb, value)

    @property
    def uart_force_xon(self):
        return self.__MEM.rdm(self.__addr, self.__uart_force_xon_msb, self.__uart_force_xon_lsb)
    @uart_force_xon.setter
    def uart_force_xon(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_force_xon_msb, self.__uart_force_xon_lsb, value)

    @property
    def uart_xonoff_del(self):
        return self.__MEM.rdm(self.__addr, self.__uart_xonoff_del_msb, self.__uart_xonoff_del_lsb)
    @uart_xonoff_del.setter
    def uart_xonoff_del(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_xonoff_del_msb, self.__uart_xonoff_del_lsb, value)

    @property
    def uart_sw_flow_con_en(self):
        return self.__MEM.rdm(self.__addr, self.__uart_sw_flow_con_en_msb, self.__uart_sw_flow_con_en_lsb)
    @uart_sw_flow_con_en.setter
    def uart_sw_flow_con_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_sw_flow_con_en_msb, self.__uart_sw_flow_con_en_lsb, value)
class UART_SLEEP_CONF(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x38
        self.__uart_active_threshold_lsb = 0
        self.__uart_active_threshold_msb = 9
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def uart_active_threshold(self):
        return self.__MEM.rdm(self.__addr, self.__uart_active_threshold_msb, self.__uart_active_threshold_lsb)
    @uart_active_threshold.setter
    def uart_active_threshold(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_active_threshold_msb, self.__uart_active_threshold_lsb, value)
class UART_SWFC_CONF(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x3c
        self.__uart_xoff_char_lsb = 24
        self.__uart_xoff_char_msb = 31
        self.__uart_xon_char_lsb = 16
        self.__uart_xon_char_msb = 23
        self.__uart_xoff_threshold_lsb = 8
        self.__uart_xoff_threshold_msb = 15
        self.__uart_xon_threshold_lsb = 0
        self.__uart_xon_threshold_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def uart_xoff_char(self):
        return self.__MEM.rdm(self.__addr, self.__uart_xoff_char_msb, self.__uart_xoff_char_lsb)
    @uart_xoff_char.setter
    def uart_xoff_char(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_xoff_char_msb, self.__uart_xoff_char_lsb, value)

    @property
    def uart_xon_char(self):
        return self.__MEM.rdm(self.__addr, self.__uart_xon_char_msb, self.__uart_xon_char_lsb)
    @uart_xon_char.setter
    def uart_xon_char(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_xon_char_msb, self.__uart_xon_char_lsb, value)

    @property
    def uart_xoff_threshold(self):
        return self.__MEM.rdm(self.__addr, self.__uart_xoff_threshold_msb, self.__uart_xoff_threshold_lsb)
    @uart_xoff_threshold.setter
    def uart_xoff_threshold(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_xoff_threshold_msb, self.__uart_xoff_threshold_lsb, value)

    @property
    def uart_xon_threshold(self):
        return self.__MEM.rdm(self.__addr, self.__uart_xon_threshold_msb, self.__uart_xon_threshold_lsb)
    @uart_xon_threshold.setter
    def uart_xon_threshold(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_xon_threshold_msb, self.__uart_xon_threshold_lsb, value)
class UART_IDLE_CONF(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x40
        self.__uart_tx_brk_num_lsb = 20
        self.__uart_tx_brk_num_msb = 27
        self.__uart_tx_idle_num_lsb = 10
        self.__uart_tx_idle_num_msb = 19
        self.__rx_idle_thrhd_lsb = 0
        self.__rx_idle_thrhd_msb = 9
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def uart_tx_brk_num(self):
        return self.__MEM.rdm(self.__addr, self.__uart_tx_brk_num_msb, self.__uart_tx_brk_num_lsb)
    @uart_tx_brk_num.setter
    def uart_tx_brk_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_tx_brk_num_msb, self.__uart_tx_brk_num_lsb, value)

    @property
    def uart_tx_idle_num(self):
        return self.__MEM.rdm(self.__addr, self.__uart_tx_idle_num_msb, self.__uart_tx_idle_num_lsb)
    @uart_tx_idle_num.setter
    def uart_tx_idle_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_tx_idle_num_msb, self.__uart_tx_idle_num_lsb, value)

    @property
    def rx_idle_thrhd(self):
        return self.__MEM.rdm(self.__addr, self.__rx_idle_thrhd_msb, self.__rx_idle_thrhd_lsb)
    @rx_idle_thrhd.setter
    def rx_idle_thrhd(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_idle_thrhd_msb, self.__rx_idle_thrhd_lsb, value)
class UART_RS485_CONF(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x44
        self.__rs485_tx_dly_num_lsb = 6
        self.__rs485_tx_dly_num_msb = 9
        self.__rs485_rx_dly_num_lsb = 5
        self.__rs485_rx_dly_num_msb = 5
        self.__rs485rxby_tx_en_lsb = 4
        self.__rs485rxby_tx_en_msb = 4
        self.__rs485tx_rx_en_lsb = 3
        self.__rs485tx_rx_en_msb = 3
        self.__dl1_en_lsb = 2
        self.__dl1_en_msb = 2
        self.__dl0_en_lsb = 1
        self.__dl0_en_msb = 1
        self.__rs485_en_lsb = 0
        self.__rs485_en_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rs485_tx_dly_num(self):
        return self.__MEM.rdm(self.__addr, self.__rs485_tx_dly_num_msb, self.__rs485_tx_dly_num_lsb)
    @rs485_tx_dly_num.setter
    def rs485_tx_dly_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__rs485_tx_dly_num_msb, self.__rs485_tx_dly_num_lsb, value)

    @property
    def rs485_rx_dly_num(self):
        return self.__MEM.rdm(self.__addr, self.__rs485_rx_dly_num_msb, self.__rs485_rx_dly_num_lsb)
    @rs485_rx_dly_num.setter
    def rs485_rx_dly_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__rs485_rx_dly_num_msb, self.__rs485_rx_dly_num_lsb, value)

    @property
    def rs485rxby_tx_en(self):
        return self.__MEM.rdm(self.__addr, self.__rs485rxby_tx_en_msb, self.__rs485rxby_tx_en_lsb)
    @rs485rxby_tx_en.setter
    def rs485rxby_tx_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__rs485rxby_tx_en_msb, self.__rs485rxby_tx_en_lsb, value)

    @property
    def rs485tx_rx_en(self):
        return self.__MEM.rdm(self.__addr, self.__rs485tx_rx_en_msb, self.__rs485tx_rx_en_lsb)
    @rs485tx_rx_en.setter
    def rs485tx_rx_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__rs485tx_rx_en_msb, self.__rs485tx_rx_en_lsb, value)

    @property
    def dl1_en(self):
        return self.__MEM.rdm(self.__addr, self.__dl1_en_msb, self.__dl1_en_lsb)
    @dl1_en.setter
    def dl1_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__dl1_en_msb, self.__dl1_en_lsb, value)

    @property
    def dl0_en(self):
        return self.__MEM.rdm(self.__addr, self.__dl0_en_msb, self.__dl0_en_lsb)
    @dl0_en.setter
    def dl0_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__dl0_en_msb, self.__dl0_en_lsb, value)

    @property
    def rs485_en(self):
        return self.__MEM.rdm(self.__addr, self.__rs485_en_msb, self.__rs485_en_lsb)
    @rs485_en.setter
    def rs485_en(self, value):
        return self.__MEM.wrm(self.__addr, self.__rs485_en_msb, self.__rs485_en_lsb, value)
class UART_AT_CMD_PRECNT(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x48
        self.__pre_idle_num_lsb = 0
        self.__pre_idle_num_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def pre_idle_num(self):
        return self.__MEM.rdm(self.__addr, self.__pre_idle_num_msb, self.__pre_idle_num_lsb)
    @pre_idle_num.setter
    def pre_idle_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__pre_idle_num_msb, self.__pre_idle_num_lsb, value)
class UART_AT_CMD_POSTCNT(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x4c
        self.__post_idle_num_lsb = 0
        self.__post_idle_num_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def post_idle_num(self):
        return self.__MEM.rdm(self.__addr, self.__post_idle_num_msb, self.__post_idle_num_lsb)
    @post_idle_num.setter
    def post_idle_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__post_idle_num_msb, self.__post_idle_num_lsb, value)
class UART_AT_CMD_GAPTOUT(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x50
        self.__rx_gap_tout_lsb = 0
        self.__rx_gap_tout_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def rx_gap_tout(self):
        return self.__MEM.rdm(self.__addr, self.__rx_gap_tout_msb, self.__rx_gap_tout_lsb)
    @rx_gap_tout.setter
    def rx_gap_tout(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_gap_tout_msb, self.__rx_gap_tout_lsb, value)
class UART_AT_CMD_CHAR(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x54
        self.__char_num_lsb = 8
        self.__char_num_msb = 15
        self.__at_cmd_char_lsb = 0
        self.__at_cmd_char_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def char_num(self):
        return self.__MEM.rdm(self.__addr, self.__char_num_msb, self.__char_num_lsb)
    @char_num.setter
    def char_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__char_num_msb, self.__char_num_lsb, value)

    @property
    def at_cmd_char(self):
        return self.__MEM.rdm(self.__addr, self.__at_cmd_char_msb, self.__at_cmd_char_lsb)
    @at_cmd_char.setter
    def at_cmd_char(self, value):
        return self.__MEM.wrm(self.__addr, self.__at_cmd_char_msb, self.__at_cmd_char_lsb, value)
class UART_MEM_CONF(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x58
        self.__tx_mem_empty_thrhd_lsb = 28
        self.__tx_mem_empty_thrhd_msb = 30
        self.__rx_mem_full_thrhd_lsb = 25
        self.__rx_mem_full_thrhd_msb = 27
        self.__uart_xoff_threshold_h2_lsb = 23
        self.__uart_xoff_threshold_h2_msb = 24
        self.__uart_xon_threshold_h2_lsb = 21
        self.__uart_xon_threshold_h2_msb = 22
        self.__rx_tout_thrhd_h3_lsb = 18
        self.__rx_tout_thrhd_h3_msb = 20
        self.__rx_flow_thrhd_h3_lsb = 15
        self.__rx_flow_thrhd_h3_msb = 17
        self.__reg_tx_size_lsb = 7
        self.__reg_tx_size_msb = 10
        self.__reg_rx_size_lsb = 3
        self.__reg_rx_size_msb = 6
        self.__reg_mem_pd_lsb = 0
        self.__reg_mem_pd_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tx_mem_empty_thrhd(self):
        return self.__MEM.rdm(self.__addr, self.__tx_mem_empty_thrhd_msb, self.__tx_mem_empty_thrhd_lsb)
    @tx_mem_empty_thrhd.setter
    def tx_mem_empty_thrhd(self, value):
        return self.__MEM.wrm(self.__addr, self.__tx_mem_empty_thrhd_msb, self.__tx_mem_empty_thrhd_lsb, value)

    @property
    def rx_mem_full_thrhd(self):
        return self.__MEM.rdm(self.__addr, self.__rx_mem_full_thrhd_msb, self.__rx_mem_full_thrhd_lsb)
    @rx_mem_full_thrhd.setter
    def rx_mem_full_thrhd(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_mem_full_thrhd_msb, self.__rx_mem_full_thrhd_lsb, value)

    @property
    def uart_xoff_threshold_h2(self):
        return self.__MEM.rdm(self.__addr, self.__uart_xoff_threshold_h2_msb, self.__uart_xoff_threshold_h2_lsb)
    @uart_xoff_threshold_h2.setter
    def uart_xoff_threshold_h2(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_xoff_threshold_h2_msb, self.__uart_xoff_threshold_h2_lsb, value)

    @property
    def uart_xon_threshold_h2(self):
        return self.__MEM.rdm(self.__addr, self.__uart_xon_threshold_h2_msb, self.__uart_xon_threshold_h2_lsb)
    @uart_xon_threshold_h2.setter
    def uart_xon_threshold_h2(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_xon_threshold_h2_msb, self.__uart_xon_threshold_h2_lsb, value)

    @property
    def rx_tout_thrhd_h3(self):
        return self.__MEM.rdm(self.__addr, self.__rx_tout_thrhd_h3_msb, self.__rx_tout_thrhd_h3_lsb)
    @rx_tout_thrhd_h3.setter
    def rx_tout_thrhd_h3(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_tout_thrhd_h3_msb, self.__rx_tout_thrhd_h3_lsb, value)

    @property
    def rx_flow_thrhd_h3(self):
        return self.__MEM.rdm(self.__addr, self.__rx_flow_thrhd_h3_msb, self.__rx_flow_thrhd_h3_lsb)
    @rx_flow_thrhd_h3.setter
    def rx_flow_thrhd_h3(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_flow_thrhd_h3_msb, self.__rx_flow_thrhd_h3_lsb, value)

    @property
    def reg_tx_size(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tx_size_msb, self.__reg_tx_size_lsb)
    @reg_tx_size.setter
    def reg_tx_size(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tx_size_msb, self.__reg_tx_size_lsb, value)

    @property
    def reg_rx_size(self):
        return self.__MEM.rdm(self.__addr, self.__reg_rx_size_msb, self.__reg_rx_size_lsb)
    @reg_rx_size.setter
    def reg_rx_size(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_rx_size_msb, self.__reg_rx_size_lsb, value)

    @property
    def reg_mem_pd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mem_pd_msb, self.__reg_mem_pd_lsb)
    @reg_mem_pd.setter
    def reg_mem_pd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mem_pd_msb, self.__reg_mem_pd_lsb, value)
class UART_MEM_TX_STATUS(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x5c
        self.__mem_tx_status_lsb = 0
        self.__mem_tx_status_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def mem_tx_status(self):
        return self.__MEM.rdm(self.__addr, self.__mem_tx_status_msb, self.__mem_tx_status_lsb)
    @mem_tx_status.setter
    def mem_tx_status(self, value):
        return self.__MEM.wrm(self.__addr, self.__mem_tx_status_msb, self.__mem_tx_status_lsb, value)
class UART_MEM_RX_STATUS(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x60
        self.__mem_rx_status_lsb = 0
        self.__mem_rx_status_msb = 23
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def mem_rx_status(self):
        return self.__MEM.rdm(self.__addr, self.__mem_rx_status_msb, self.__mem_rx_status_lsb)
    @mem_rx_status.setter
    def mem_rx_status(self, value):
        return self.__MEM.wrm(self.__addr, self.__mem_rx_status_msb, self.__mem_rx_status_lsb, value)
class UART_MEM_CNT_STATUS(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x64
        self.__tx_mem_cnt_lsb = 3
        self.__tx_mem_cnt_msb = 5
        self.__rx_mem_cnt_lsb = 0
        self.__rx_mem_cnt_msb = 2
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tx_mem_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__tx_mem_cnt_msb, self.__tx_mem_cnt_lsb)
    @tx_mem_cnt.setter
    def tx_mem_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__tx_mem_cnt_msb, self.__tx_mem_cnt_lsb, value)

    @property
    def rx_mem_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__rx_mem_cnt_msb, self.__rx_mem_cnt_lsb)
    @rx_mem_cnt.setter
    def rx_mem_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__rx_mem_cnt_msb, self.__rx_mem_cnt_lsb, value)
class UART_POSPULSE(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x68
        self.__posedge_min_cnt_lsb = 0
        self.__posedge_min_cnt_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def posedge_min_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__posedge_min_cnt_msb, self.__posedge_min_cnt_lsb)
    @posedge_min_cnt.setter
    def posedge_min_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__posedge_min_cnt_msb, self.__posedge_min_cnt_lsb, value)
class UART_NEGPULSE(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x6c
        self.__negedge_min_cnt_lsb = 0
        self.__negedge_min_cnt_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def negedge_min_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__negedge_min_cnt_msb, self.__negedge_min_cnt_lsb)
    @negedge_min_cnt.setter
    def negedge_min_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__negedge_min_cnt_msb, self.__negedge_min_cnt_lsb, value)
class UART_DATE(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x78
        self.__uart_date_lsb = 0
        self.__uart_date_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def uart_date(self):
        return self.__MEM.rdm(self.__addr, self.__uart_date_msb, self.__uart_date_lsb)
    @uart_date.setter
    def uart_date(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_date_msb, self.__uart_date_lsb, value)
    @property
    def default_value(self):
        return 0x15122500 
class UART_ID(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = UART_BASE + 0x7c
        self.__uart_id_lsb = 0
        self.__uart_id_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def uart_id(self):
        return self.__MEM.rdm(self.__addr, self.__uart_id_msb, self.__uart_id_lsb)
    @uart_id.setter
    def uart_id(self, value):
        return self.__MEM.wrm(self.__addr, self.__uart_id_msb, self.__uart_id_lsb, value)
