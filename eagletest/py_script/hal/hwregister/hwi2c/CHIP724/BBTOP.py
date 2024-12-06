from hal.common import *
from hal.hwregister.hwi2c.CHIP724.addr_base import *
class BBTOP(object):
    def __init__(self, channel, chipv = "CHIP724"):
        self.chipv = chipv
        self.channel = channel
        self.__I2C = I2C(self.channel, self.chipv)
        self.__base = BBTOP_BASE
        self.__hostid = BBTOP_HOSTID
        self.__filter_dtest_lsb = 0
        self.__filter_dtest_msb = 1
        self.__filter_dtest_addr = 0x0
        self.__ent_filter_i_lsb = 2
        self.__ent_filter_i_msb = 2
        self.__ent_filter_i_addr = 0x0
        self.__ent_filter_q_lsb = 3
        self.__ent_filter_q_msb = 3
        self.__ent_filter_q_addr = 0x0
        self.__ent_filter_bias_i_lsb = 4
        self.__ent_filter_bias_i_msb = 4
        self.__ent_filter_bias_i_addr = 0x0
        self.__ent_filter_bias_q_lsb = 5
        self.__ent_filter_bias_q_msb = 5
        self.__ent_filter_bias_q_addr = 0x0
        self.__enlb_lsb = 6
        self.__enlb_msb = 6
        self.__enlb_addr = 0x0
        self.__tmx_lbd1_lsb = 0
        self.__tmx_lbd1_msb = 3
        self.__tmx_lbd1_addr = 0x1
        self.__tmx_lbd2_lsb = 4
        self.__tmx_lbd2_msb = 7
        self.__tmx_lbd2_addr = 0x1
        self.__tmx_dsw_bias_lsb = 0
        self.__tmx_dsw_bias_msb = 1
        self.__tmx_dsw_bias_addr = 0x2
        self.__tmx_dv2i_bias_lsb = 2
        self.__tmx_dv2i_bias_msb = 3
        self.__tmx_dv2i_bias_addr = 0x2
        self.__dac_ck_ph_inv_lsb = 4
        self.__dac_ck_ph_inv_msb = 4
        self.__dac_ck_ph_inv_addr = 0x2
        self.__filter_xpd_lat_lsb = 5
        self.__filter_xpd_lat_msb = 5
        self.__filter_xpd_lat_addr = 0x2
        self.__nc1_lsb = 6
        self.__nc1_msb = 7
        self.__nc1_addr = 0x2
        self.__filter_cmplx_ctrl_lsb = 0
        self.__filter_cmplx_ctrl_msb = 1
        self.__filter_cmplx_ctrl_addr = 0x3
        self.__encmplx_btrx_lsb = 2
        self.__encmplx_btrx_msb = 2
        self.__encmplx_btrx_addr = 0x3
        self.__encmplx_bttx_lsb = 3
        self.__encmplx_bttx_msb = 3
        self.__encmplx_bttx_addr = 0x3
        self.__nc2_lsb = 4
        self.__nc2_msb = 7
        self.__nc2_addr = 0x3
        self.__filter_wfrx0_dcap_lq_lsb = 0
        self.__filter_wfrx0_dcap_lq_msb = 5
        self.__filter_wfrx0_dcap_lq_addr = 0x4
        self.__filter_wfrx0_dcap_hq_lsb = 0
        self.__filter_wfrx0_dcap_hq_msb = 5
        self.__filter_wfrx0_dcap_hq_addr = 0x5
        self.__filter_wfrx1_dcap_lq_lsb = 0
        self.__filter_wfrx1_dcap_lq_msb = 5
        self.__filter_wfrx1_dcap_lq_addr = 0x6
        self.__filter_wfrx1_dcap_hq_lsb = 0
        self.__filter_wfrx1_dcap_hq_msb = 5
        self.__filter_wfrx1_dcap_hq_addr = 0x7
        self.__filter_wfrx2_dcap_lq_lsb = 0
        self.__filter_wfrx2_dcap_lq_msb = 5
        self.__filter_wfrx2_dcap_lq_addr = 0x8
        self.__filter_wfrx2_dcap_hq_lsb = 0
        self.__filter_wfrx2_dcap_hq_msb = 5
        self.__filter_wfrx2_dcap_hq_addr = 0x9
        self.__filter_wfrx3_dcap_lq_lsb = 0
        self.__filter_wfrx3_dcap_lq_msb = 5
        self.__filter_wfrx3_dcap_lq_addr = 0xa
        self.__filter_wfrx3_dcap_hq_lsb = 0
        self.__filter_wfrx3_dcap_hq_msb = 5
        self.__filter_wfrx3_dcap_hq_addr = 0xb
        self.__filter_wftx0_dcap_lq_lsb = 0
        self.__filter_wftx0_dcap_lq_msb = 5
        self.__filter_wftx0_dcap_lq_addr = 0xc
        self.__filter_wftx0_dcap_hq_lsb = 0
        self.__filter_wftx0_dcap_hq_msb = 5
        self.__filter_wftx0_dcap_hq_addr = 0xd
        self.__filter_wftx1_dcap_lq_lsb = 0
        self.__filter_wftx1_dcap_lq_msb = 5
        self.__filter_wftx1_dcap_lq_addr = 0xe
        self.__filter_wftx1_dcap_hq_lsb = 0
        self.__filter_wftx1_dcap_hq_msb = 5
        self.__filter_wftx1_dcap_hq_addr = 0xf
        self.__filter_wftx2_dcap_lq_lsb = 0
        self.__filter_wftx2_dcap_lq_msb = 5
        self.__filter_wftx2_dcap_lq_addr = 0x10
        self.__filter_wftx2_dcap_hq_lsb = 0
        self.__filter_wftx2_dcap_hq_msb = 5
        self.__filter_wftx2_dcap_hq_addr = 0x11
        self.__filter_wftx3_dcap_lq_lsb = 0
        self.__filter_wftx3_dcap_lq_msb = 5
        self.__filter_wftx3_dcap_lq_addr = 0x12
        self.__filter_wftx3_dcap_hq_lsb = 0
        self.__filter_wftx3_dcap_hq_msb = 5
        self.__filter_wftx3_dcap_hq_addr = 0x13
        self.__filter_btrx0_dcap_lq_lsb = 0
        self.__filter_btrx0_dcap_lq_msb = 5
        self.__filter_btrx0_dcap_lq_addr = 0x14
        self.__filter_btrx0_dcap_hq_lsb = 0
        self.__filter_btrx0_dcap_hq_msb = 5
        self.__filter_btrx0_dcap_hq_addr = 0x15
        self.__filter_btrx1_dcap_lq_lsb = 0
        self.__filter_btrx1_dcap_lq_msb = 5
        self.__filter_btrx1_dcap_lq_addr = 0x16
        self.__filter_btrx1_dcap_hq_lsb = 0
        self.__filter_btrx1_dcap_hq_msb = 5
        self.__filter_btrx1_dcap_hq_addr = 0x17
        self.__filter_btrx2_dcap_lq_lsb = 0
        self.__filter_btrx2_dcap_lq_msb = 5
        self.__filter_btrx2_dcap_lq_addr = 0x18
        self.__filter_btrx2_dcap_hq_lsb = 0
        self.__filter_btrx2_dcap_hq_msb = 5
        self.__filter_btrx2_dcap_hq_addr = 0x19
        self.__filter_btrx3_dcap_lq_lsb = 0
        self.__filter_btrx3_dcap_lq_msb = 5
        self.__filter_btrx3_dcap_lq_addr = 0x1a
        self.__filter_btrx3_dcap_hq_lsb = 0
        self.__filter_btrx3_dcap_hq_msb = 5
        self.__filter_btrx3_dcap_hq_addr = 0x1b
        self.__filter_bttx0_dcap_lq_lsb = 0
        self.__filter_bttx0_dcap_lq_msb = 5
        self.__filter_bttx0_dcap_lq_addr = 0x1c
        self.__filter_bttx0_dcap_hq_lsb = 0
        self.__filter_bttx0_dcap_hq_msb = 5
        self.__filter_bttx0_dcap_hq_addr = 0x1d
        self.__filter_bttx1_dcap_lq_lsb = 0
        self.__filter_bttx1_dcap_lq_msb = 5
        self.__filter_bttx1_dcap_lq_addr = 0x1e
        self.__filter_bttx1_dcap_hq_lsb = 0
        self.__filter_bttx1_dcap_hq_msb = 5
        self.__filter_bttx1_dcap_hq_addr = 0x1f
        self.__filter_bttx2_dcap_lq_lsb = 0
        self.__filter_bttx2_dcap_lq_msb = 5
        self.__filter_bttx2_dcap_lq_addr = 0x20
        self.__filter_bttx2_dcap_hq_lsb = 0
        self.__filter_bttx2_dcap_hq_msb = 5
        self.__filter_bttx2_dcap_hq_addr = 0x21
        self.__filter_bttx3_dcap_lq_lsb = 0
        self.__filter_bttx3_dcap_lq_msb = 5
        self.__filter_bttx3_dcap_lq_addr = 0x22
        self.__filter_bttx3_dcap_hq_lsb = 0
        self.__filter_bttx3_dcap_hq_msb = 5
        self.__filter_bttx3_dcap_hq_addr = 0x23
        self.__filter_wfrx0_dgdc_lsb = 0
        self.__filter_wfrx0_dgdc_msb = 0
        self.__filter_wfrx0_dgdc_addr = 0x24
        self.__filter_wfrx0_input_ld_lsb = 1
        self.__filter_wfrx0_input_ld_msb = 2
        self.__filter_wfrx0_input_ld_addr = 0x24
        self.__filter_wfrx0_bstb_lsb = 3
        self.__filter_wfrx0_bstb_msb = 4
        self.__filter_wfrx0_bstb_addr = 0x24
        self.__filter_wfrx0_dedge_lsb = 5
        self.__filter_wfrx0_dedge_msb = 7
        self.__filter_wfrx0_dedge_addr = 0x24
        self.__filter_wfrx1_dgdc_lsb = 0
        self.__filter_wfrx1_dgdc_msb = 0
        self.__filter_wfrx1_dgdc_addr = 0x25
        self.__filter_wfrx1_input_ld_lsb = 1
        self.__filter_wfrx1_input_ld_msb = 2
        self.__filter_wfrx1_input_ld_addr = 0x25
        self.__filter_wfrx1_bstb_lsb = 3
        self.__filter_wfrx1_bstb_msb = 4
        self.__filter_wfrx1_bstb_addr = 0x25
        self.__filter_wfrx1_dedge_lsb = 5
        self.__filter_wfrx1_dedge_msb = 7
        self.__filter_wfrx1_dedge_addr = 0x25
        self.__filter_wfrx2_dgdc_lsb = 0
        self.__filter_wfrx2_dgdc_msb = 0
        self.__filter_wfrx2_dgdc_addr = 0x26
        self.__filter_wfrx2_input_ld_lsb = 1
        self.__filter_wfrx2_input_ld_msb = 2
        self.__filter_wfrx2_input_ld_addr = 0x26
        self.__filter_wfrx2_bstb_lsb = 3
        self.__filter_wfrx2_bstb_msb = 4
        self.__filter_wfrx2_bstb_addr = 0x26
        self.__filter_wfrx2_dedge_lsb = 5
        self.__filter_wfrx2_dedge_msb = 7
        self.__filter_wfrx2_dedge_addr = 0x26
        self.__filter_wfrx3_dgdc_lsb = 0
        self.__filter_wfrx3_dgdc_msb = 0
        self.__filter_wfrx3_dgdc_addr = 0x27
        self.__filter_wfrx3_input_ld_lsb = 1
        self.__filter_wfrx3_input_ld_msb = 2
        self.__filter_wfrx3_input_ld_addr = 0x27
        self.__filter_wfrx3_bstb_lsb = 3
        self.__filter_wfrx3_bstb_msb = 4
        self.__filter_wfrx3_bstb_addr = 0x27
        self.__filter_wfrx3_dedge_lsb = 5
        self.__filter_wfrx3_dedge_msb = 7
        self.__filter_wfrx3_dedge_addr = 0x27
        self.__filter_wftx0_dgdc_lsb = 0
        self.__filter_wftx0_dgdc_msb = 0
        self.__filter_wftx0_dgdc_addr = 0x28
        self.__filter_wftx0_input_ld_lsb = 1
        self.__filter_wftx0_input_ld_msb = 2
        self.__filter_wftx0_input_ld_addr = 0x28
        self.__filter_wftx0_bstb_lsb = 3
        self.__filter_wftx0_bstb_msb = 4
        self.__filter_wftx0_bstb_addr = 0x28
        self.__filter_wftx0_dedge_lsb = 5
        self.__filter_wftx0_dedge_msb = 7
        self.__filter_wftx0_dedge_addr = 0x28
        self.__filter_wftx1_dgdc_lsb = 0
        self.__filter_wftx1_dgdc_msb = 0
        self.__filter_wftx1_dgdc_addr = 0x29
        self.__filter_wftx1_input_ld_lsb = 1
        self.__filter_wftx1_input_ld_msb = 2
        self.__filter_wftx1_input_ld_addr = 0x29
        self.__filter_wftx1_bstb_lsb = 3
        self.__filter_wftx1_bstb_msb = 4
        self.__filter_wftx1_bstb_addr = 0x29
        self.__filter_wftx1_dedge_lsb = 5
        self.__filter_wftx1_dedge_msb = 7
        self.__filter_wftx1_dedge_addr = 0x29
        self.__filter_wftx2_dgdc_lsb = 0
        self.__filter_wftx2_dgdc_msb = 0
        self.__filter_wftx2_dgdc_addr = 0x2a
        self.__filter_wftx2_input_ld_lsb = 1
        self.__filter_wftx2_input_ld_msb = 2
        self.__filter_wftx2_input_ld_addr = 0x2a
        self.__filter_wftx2_bstb_lsb = 3
        self.__filter_wftx2_bstb_msb = 4
        self.__filter_wftx2_bstb_addr = 0x2a
        self.__filter_wftx2_dedge_lsb = 5
        self.__filter_wftx2_dedge_msb = 7
        self.__filter_wftx2_dedge_addr = 0x2a
        self.__filter_wftx3_dgdc_lsb = 0
        self.__filter_wftx3_dgdc_msb = 0
        self.__filter_wftx3_dgdc_addr = 0x2b
        self.__filter_wftx3_input_ld_lsb = 1
        self.__filter_wftx3_input_ld_msb = 2
        self.__filter_wftx3_input_ld_addr = 0x2b
        self.__filter_wftx3_bstb_lsb = 3
        self.__filter_wftx3_bstb_msb = 4
        self.__filter_wftx3_bstb_addr = 0x2b
        self.__filter_wftx3_dedge_lsb = 5
        self.__filter_wftx3_dedge_msb = 7
        self.__filter_wftx3_dedge_addr = 0x2b
        self.__filter_btrx0_dgdc_lsb = 0
        self.__filter_btrx0_dgdc_msb = 0
        self.__filter_btrx0_dgdc_addr = 0x2c
        self.__filter_btrx0_input_ld_lsb = 1
        self.__filter_btrx0_input_ld_msb = 2
        self.__filter_btrx0_input_ld_addr = 0x2c
        self.__filter_btrx0_bstb_lsb = 3
        self.__filter_btrx0_bstb_msb = 4
        self.__filter_btrx0_bstb_addr = 0x2c
        self.__filter_btrx0_dedge_lsb = 5
        self.__filter_btrx0_dedge_msb = 7
        self.__filter_btrx0_dedge_addr = 0x2c
        self.__filter_btrx1_dgdc_lsb = 0
        self.__filter_btrx1_dgdc_msb = 0
        self.__filter_btrx1_dgdc_addr = 0x2d
        self.__filter_btrx1_input_ld_lsb = 1
        self.__filter_btrx1_input_ld_msb = 2
        self.__filter_btrx1_input_ld_addr = 0x2d
        self.__filter_btrx1_bstb_lsb = 3
        self.__filter_btrx1_bstb_msb = 4
        self.__filter_btrx1_bstb_addr = 0x2d
        self.__filter_btrx1_dedge_lsb = 5
        self.__filter_btrx1_dedge_msb = 7
        self.__filter_btrx1_dedge_addr = 0x2d
        self.__filter_btrx2_dgdc_lsb = 0
        self.__filter_btrx2_dgdc_msb = 0
        self.__filter_btrx2_dgdc_addr = 0x2e
        self.__filter_btrx2_input_ld_lsb = 1
        self.__filter_btrx2_input_ld_msb = 2
        self.__filter_btrx2_input_ld_addr = 0x2e
        self.__filter_btrx2_bstb_lsb = 3
        self.__filter_btrx2_bstb_msb = 4
        self.__filter_btrx2_bstb_addr = 0x2e
        self.__filter_btrx2_dedge_lsb = 5
        self.__filter_btrx2_dedge_msb = 7
        self.__filter_btrx2_dedge_addr = 0x2e
        self.__filter_btrx3_dgdc_lsb = 0
        self.__filter_btrx3_dgdc_msb = 0
        self.__filter_btrx3_dgdc_addr = 0x2f
        self.__filter_btrx3_input_ld_lsb = 1
        self.__filter_btrx3_input_ld_msb = 2
        self.__filter_btrx3_input_ld_addr = 0x2f
        self.__filter_btrx3_bstb_lsb = 3
        self.__filter_btrx3_bstb_msb = 4
        self.__filter_btrx3_bstb_addr = 0x2f
        self.__filter_btrx3_dedge_lsb = 5
        self.__filter_btrx3_dedge_msb = 7
        self.__filter_btrx3_dedge_addr = 0x2f
        self.__filter_bttx0_dgdc_lsb = 0
        self.__filter_bttx0_dgdc_msb = 0
        self.__filter_bttx0_dgdc_addr = 0x30
        self.__filter_bttx0_input_ld_lsb = 1
        self.__filter_bttx0_input_ld_msb = 2
        self.__filter_bttx0_input_ld_addr = 0x30
        self.__filter_bttx0_bstb_lsb = 3
        self.__filter_bttx0_bstb_msb = 4
        self.__filter_bttx0_bstb_addr = 0x30
        self.__filter_bttx0_dedge_lsb = 5
        self.__filter_bttx0_dedge_msb = 7
        self.__filter_bttx0_dedge_addr = 0x30
        self.__filter_bttx1_dgdc_lsb = 0
        self.__filter_bttx1_dgdc_msb = 0
        self.__filter_bttx1_dgdc_addr = 0x31
        self.__filter_bttx1_input_ld_lsb = 1
        self.__filter_bttx1_input_ld_msb = 2
        self.__filter_bttx1_input_ld_addr = 0x31
        self.__filter_bttx1_bstb_lsb = 3
        self.__filter_bttx1_bstb_msb = 4
        self.__filter_bttx1_bstb_addr = 0x31
        self.__filter_bttx1_dedge_lsb = 5
        self.__filter_bttx1_dedge_msb = 7
        self.__filter_bttx1_dedge_addr = 0x31
        self.__filter_bttx2_dgdc_lsb = 0
        self.__filter_bttx2_dgdc_msb = 0
        self.__filter_bttx2_dgdc_addr = 0x32
        self.__filter_bttx2_input_ld_lsb = 1
        self.__filter_bttx2_input_ld_msb = 2
        self.__filter_bttx2_input_ld_addr = 0x32
        self.__filter_bttx2_bstb_lsb = 3
        self.__filter_bttx2_bstb_msb = 4
        self.__filter_bttx2_bstb_addr = 0x32
        self.__filter_bttx2_dedge_lsb = 5
        self.__filter_bttx2_dedge_msb = 7
        self.__filter_bttx2_dedge_addr = 0x32
        self.__filter_bttx3_dgdc_lsb = 0
        self.__filter_bttx3_dgdc_msb = 0
        self.__filter_bttx3_dgdc_addr = 0x33
        self.__filter_bttx3_input_ld_lsb = 1
        self.__filter_bttx3_input_ld_msb = 2
        self.__filter_bttx3_input_ld_addr = 0x33
        self.__filter_bttx3_bstb_lsb = 3
        self.__filter_bttx3_bstb_msb = 4
        self.__filter_bttx3_bstb_addr = 0x33
        self.__filter_bttx3_dedge_lsb = 5
        self.__filter_bttx3_dedge_msb = 7
        self.__filter_bttx3_dedge_addr = 0x33
        self.__filter_wfrx0_dcc_lsb = 0
        self.__filter_wfrx0_dcc_msb = 1
        self.__filter_wfrx0_dcc_addr = 0x34
        self.__filter_wfrx1_dcc_lsb = 2
        self.__filter_wfrx1_dcc_msb = 3
        self.__filter_wfrx1_dcc_addr = 0x34
        self.__filter_wfrx2_dcc_lsb = 4
        self.__filter_wfrx2_dcc_msb = 5
        self.__filter_wfrx2_dcc_addr = 0x34
        self.__filter_wfrx3_dcc_lsb = 6
        self.__filter_wfrx3_dcc_msb = 7
        self.__filter_wfrx3_dcc_addr = 0x34
        self.__filter_wftx0_dcc_lsb = 0
        self.__filter_wftx0_dcc_msb = 1
        self.__filter_wftx0_dcc_addr = 0x35
        self.__filter_wftx1_dcc_lsb = 2
        self.__filter_wftx1_dcc_msb = 3
        self.__filter_wftx1_dcc_addr = 0x35
        self.__filter_wftx2_dcc_lsb = 4
        self.__filter_wftx2_dcc_msb = 5
        self.__filter_wftx2_dcc_addr = 0x35
        self.__filter_wftx3_dcc_lsb = 6
        self.__filter_wftx3_dcc_msb = 7
        self.__filter_wftx3_dcc_addr = 0x35
        self.__filter_btrx0_dcc_lsb = 0
        self.__filter_btrx0_dcc_msb = 1
        self.__filter_btrx0_dcc_addr = 0x36
        self.__filter_btrx1_dcc_lsb = 2
        self.__filter_btrx1_dcc_msb = 3
        self.__filter_btrx1_dcc_addr = 0x36
        self.__filter_btrx2_dcc_lsb = 4
        self.__filter_btrx2_dcc_msb = 5
        self.__filter_btrx2_dcc_addr = 0x36
        self.__filter_btrx3_dcc_lsb = 6
        self.__filter_btrx3_dcc_msb = 7
        self.__filter_btrx3_dcc_addr = 0x36
        self.__filter_bttx0_dcc_lsb = 0
        self.__filter_bttx0_dcc_msb = 1
        self.__filter_bttx0_dcc_addr = 0x37
        self.__filter_bttx1_dcc_lsb = 2
        self.__filter_bttx1_dcc_msb = 3
        self.__filter_bttx1_dcc_addr = 0x37
        self.__filter_bttx2_dcc_lsb = 4
        self.__filter_bttx2_dcc_msb = 5
        self.__filter_bttx2_dcc_addr = 0x37
        self.__filter_bttx3_dcc_lsb = 6
        self.__filter_bttx3_dcc_msb = 7
        self.__filter_bttx3_dcc_addr = 0x37

    def reg_addr_rd(self,reg_addr):
        return self.__I2C.i2c_rd(self.__base , self.__hostid ,reg_addr)
    def reg_addr_wr(self,reg_addr,value):
        return self.__I2C.i2c_wr(self.__base , self.__hostid ,reg_addr,value)

    @property
    def filter_dtest(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_dtest_addr, self.__filter_dtest_msb, self.__filter_dtest_lsb)
    @filter_dtest.setter
    def filter_dtest(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_dtest_addr, self.__filter_dtest_msb, self.__filter_dtest_lsb, value)

    @property
    def ent_filter_i(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_filter_i_addr, self.__ent_filter_i_msb, self.__ent_filter_i_lsb)
    @ent_filter_i.setter
    def ent_filter_i(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_filter_i_addr, self.__ent_filter_i_msb, self.__ent_filter_i_lsb, value)

    @property
    def ent_filter_q(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_filter_q_addr, self.__ent_filter_q_msb, self.__ent_filter_q_lsb)
    @ent_filter_q.setter
    def ent_filter_q(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_filter_q_addr, self.__ent_filter_q_msb, self.__ent_filter_q_lsb, value)

    @property
    def ent_filter_bias_i(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_filter_bias_i_addr, self.__ent_filter_bias_i_msb, self.__ent_filter_bias_i_lsb)
    @ent_filter_bias_i.setter
    def ent_filter_bias_i(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_filter_bias_i_addr, self.__ent_filter_bias_i_msb, self.__ent_filter_bias_i_lsb, value)

    @property
    def ent_filter_bias_q(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_filter_bias_q_addr, self.__ent_filter_bias_q_msb, self.__ent_filter_bias_q_lsb)
    @ent_filter_bias_q.setter
    def ent_filter_bias_q(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_filter_bias_q_addr, self.__ent_filter_bias_q_msb, self.__ent_filter_bias_q_lsb, value)

    @property
    def enlb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__enlb_addr, self.__enlb_msb, self.__enlb_lsb)
    @enlb.setter
    def enlb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__enlb_addr, self.__enlb_msb, self.__enlb_lsb, value)

    @property
    def tmx_lbd1(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tmx_lbd1_addr, self.__tmx_lbd1_msb, self.__tmx_lbd1_lsb)
    @tmx_lbd1.setter
    def tmx_lbd1(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tmx_lbd1_addr, self.__tmx_lbd1_msb, self.__tmx_lbd1_lsb, value)

    @property
    def tmx_lbd2(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tmx_lbd2_addr, self.__tmx_lbd2_msb, self.__tmx_lbd2_lsb)
    @tmx_lbd2.setter
    def tmx_lbd2(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tmx_lbd2_addr, self.__tmx_lbd2_msb, self.__tmx_lbd2_lsb, value)

    @property
    def tmx_dsw_bias(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tmx_dsw_bias_addr, self.__tmx_dsw_bias_msb, self.__tmx_dsw_bias_lsb)
    @tmx_dsw_bias.setter
    def tmx_dsw_bias(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tmx_dsw_bias_addr, self.__tmx_dsw_bias_msb, self.__tmx_dsw_bias_lsb, value)

    @property
    def tmx_dv2i_bias(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__tmx_dv2i_bias_addr, self.__tmx_dv2i_bias_msb, self.__tmx_dv2i_bias_lsb)
    @tmx_dv2i_bias.setter
    def tmx_dv2i_bias(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__tmx_dv2i_bias_addr, self.__tmx_dv2i_bias_msb, self.__tmx_dv2i_bias_lsb, value)

    @property
    def dac_ck_ph_inv(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dac_ck_ph_inv_addr, self.__dac_ck_ph_inv_msb, self.__dac_ck_ph_inv_lsb)
    @dac_ck_ph_inv.setter
    def dac_ck_ph_inv(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dac_ck_ph_inv_addr, self.__dac_ck_ph_inv_msb, self.__dac_ck_ph_inv_lsb, value)

    @property
    def filter_xpd_lat(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_xpd_lat_addr, self.__filter_xpd_lat_msb, self.__filter_xpd_lat_lsb)
    @filter_xpd_lat.setter
    def filter_xpd_lat(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_xpd_lat_addr, self.__filter_xpd_lat_msb, self.__filter_xpd_lat_lsb, value)

    @property
    def nc1(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__nc1_addr, self.__nc1_msb, self.__nc1_lsb)
    @nc1.setter
    def nc1(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__nc1_addr, self.__nc1_msb, self.__nc1_lsb, value)

    @property
    def filter_cmplx_ctrl(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_cmplx_ctrl_addr, self.__filter_cmplx_ctrl_msb, self.__filter_cmplx_ctrl_lsb)
    @filter_cmplx_ctrl.setter
    def filter_cmplx_ctrl(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_cmplx_ctrl_addr, self.__filter_cmplx_ctrl_msb, self.__filter_cmplx_ctrl_lsb, value)

    @property
    def encmplx_btrx(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__encmplx_btrx_addr, self.__encmplx_btrx_msb, self.__encmplx_btrx_lsb)
    @encmplx_btrx.setter
    def encmplx_btrx(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__encmplx_btrx_addr, self.__encmplx_btrx_msb, self.__encmplx_btrx_lsb, value)

    @property
    def encmplx_bttx(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__encmplx_bttx_addr, self.__encmplx_bttx_msb, self.__encmplx_bttx_lsb)
    @encmplx_bttx.setter
    def encmplx_bttx(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__encmplx_bttx_addr, self.__encmplx_bttx_msb, self.__encmplx_bttx_lsb, value)

    @property
    def nc2(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__nc2_addr, self.__nc2_msb, self.__nc2_lsb)
    @nc2.setter
    def nc2(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__nc2_addr, self.__nc2_msb, self.__nc2_lsb, value)

    @property
    def filter_wfrx0_dcap_lq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx0_dcap_lq_addr, self.__filter_wfrx0_dcap_lq_msb, self.__filter_wfrx0_dcap_lq_lsb)
    @filter_wfrx0_dcap_lq.setter
    def filter_wfrx0_dcap_lq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx0_dcap_lq_addr, self.__filter_wfrx0_dcap_lq_msb, self.__filter_wfrx0_dcap_lq_lsb, value)

    @property
    def filter_wfrx0_dcap_hq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx0_dcap_hq_addr, self.__filter_wfrx0_dcap_hq_msb, self.__filter_wfrx0_dcap_hq_lsb)
    @filter_wfrx0_dcap_hq.setter
    def filter_wfrx0_dcap_hq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx0_dcap_hq_addr, self.__filter_wfrx0_dcap_hq_msb, self.__filter_wfrx0_dcap_hq_lsb, value)

    @property
    def filter_wfrx1_dcap_lq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx1_dcap_lq_addr, self.__filter_wfrx1_dcap_lq_msb, self.__filter_wfrx1_dcap_lq_lsb)
    @filter_wfrx1_dcap_lq.setter
    def filter_wfrx1_dcap_lq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx1_dcap_lq_addr, self.__filter_wfrx1_dcap_lq_msb, self.__filter_wfrx1_dcap_lq_lsb, value)

    @property
    def filter_wfrx1_dcap_hq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx1_dcap_hq_addr, self.__filter_wfrx1_dcap_hq_msb, self.__filter_wfrx1_dcap_hq_lsb)
    @filter_wfrx1_dcap_hq.setter
    def filter_wfrx1_dcap_hq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx1_dcap_hq_addr, self.__filter_wfrx1_dcap_hq_msb, self.__filter_wfrx1_dcap_hq_lsb, value)

    @property
    def filter_wfrx2_dcap_lq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx2_dcap_lq_addr, self.__filter_wfrx2_dcap_lq_msb, self.__filter_wfrx2_dcap_lq_lsb)
    @filter_wfrx2_dcap_lq.setter
    def filter_wfrx2_dcap_lq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx2_dcap_lq_addr, self.__filter_wfrx2_dcap_lq_msb, self.__filter_wfrx2_dcap_lq_lsb, value)

    @property
    def filter_wfrx2_dcap_hq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx2_dcap_hq_addr, self.__filter_wfrx2_dcap_hq_msb, self.__filter_wfrx2_dcap_hq_lsb)
    @filter_wfrx2_dcap_hq.setter
    def filter_wfrx2_dcap_hq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx2_dcap_hq_addr, self.__filter_wfrx2_dcap_hq_msb, self.__filter_wfrx2_dcap_hq_lsb, value)

    @property
    def filter_wfrx3_dcap_lq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx3_dcap_lq_addr, self.__filter_wfrx3_dcap_lq_msb, self.__filter_wfrx3_dcap_lq_lsb)
    @filter_wfrx3_dcap_lq.setter
    def filter_wfrx3_dcap_lq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx3_dcap_lq_addr, self.__filter_wfrx3_dcap_lq_msb, self.__filter_wfrx3_dcap_lq_lsb, value)

    @property
    def filter_wfrx3_dcap_hq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx3_dcap_hq_addr, self.__filter_wfrx3_dcap_hq_msb, self.__filter_wfrx3_dcap_hq_lsb)
    @filter_wfrx3_dcap_hq.setter
    def filter_wfrx3_dcap_hq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx3_dcap_hq_addr, self.__filter_wfrx3_dcap_hq_msb, self.__filter_wfrx3_dcap_hq_lsb, value)

    @property
    def filter_wftx0_dcap_lq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx0_dcap_lq_addr, self.__filter_wftx0_dcap_lq_msb, self.__filter_wftx0_dcap_lq_lsb)
    @filter_wftx0_dcap_lq.setter
    def filter_wftx0_dcap_lq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx0_dcap_lq_addr, self.__filter_wftx0_dcap_lq_msb, self.__filter_wftx0_dcap_lq_lsb, value)

    @property
    def filter_wftx0_dcap_hq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx0_dcap_hq_addr, self.__filter_wftx0_dcap_hq_msb, self.__filter_wftx0_dcap_hq_lsb)
    @filter_wftx0_dcap_hq.setter
    def filter_wftx0_dcap_hq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx0_dcap_hq_addr, self.__filter_wftx0_dcap_hq_msb, self.__filter_wftx0_dcap_hq_lsb, value)

    @property
    def filter_wftx1_dcap_lq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx1_dcap_lq_addr, self.__filter_wftx1_dcap_lq_msb, self.__filter_wftx1_dcap_lq_lsb)
    @filter_wftx1_dcap_lq.setter
    def filter_wftx1_dcap_lq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx1_dcap_lq_addr, self.__filter_wftx1_dcap_lq_msb, self.__filter_wftx1_dcap_lq_lsb, value)

    @property
    def filter_wftx1_dcap_hq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx1_dcap_hq_addr, self.__filter_wftx1_dcap_hq_msb, self.__filter_wftx1_dcap_hq_lsb)
    @filter_wftx1_dcap_hq.setter
    def filter_wftx1_dcap_hq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx1_dcap_hq_addr, self.__filter_wftx1_dcap_hq_msb, self.__filter_wftx1_dcap_hq_lsb, value)

    @property
    def filter_wftx2_dcap_lq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx2_dcap_lq_addr, self.__filter_wftx2_dcap_lq_msb, self.__filter_wftx2_dcap_lq_lsb)
    @filter_wftx2_dcap_lq.setter
    def filter_wftx2_dcap_lq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx2_dcap_lq_addr, self.__filter_wftx2_dcap_lq_msb, self.__filter_wftx2_dcap_lq_lsb, value)

    @property
    def filter_wftx2_dcap_hq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx2_dcap_hq_addr, self.__filter_wftx2_dcap_hq_msb, self.__filter_wftx2_dcap_hq_lsb)
    @filter_wftx2_dcap_hq.setter
    def filter_wftx2_dcap_hq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx2_dcap_hq_addr, self.__filter_wftx2_dcap_hq_msb, self.__filter_wftx2_dcap_hq_lsb, value)

    @property
    def filter_wftx3_dcap_lq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx3_dcap_lq_addr, self.__filter_wftx3_dcap_lq_msb, self.__filter_wftx3_dcap_lq_lsb)
    @filter_wftx3_dcap_lq.setter
    def filter_wftx3_dcap_lq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx3_dcap_lq_addr, self.__filter_wftx3_dcap_lq_msb, self.__filter_wftx3_dcap_lq_lsb, value)

    @property
    def filter_wftx3_dcap_hq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx3_dcap_hq_addr, self.__filter_wftx3_dcap_hq_msb, self.__filter_wftx3_dcap_hq_lsb)
    @filter_wftx3_dcap_hq.setter
    def filter_wftx3_dcap_hq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx3_dcap_hq_addr, self.__filter_wftx3_dcap_hq_msb, self.__filter_wftx3_dcap_hq_lsb, value)

    @property
    def filter_btrx0_dcap_lq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx0_dcap_lq_addr, self.__filter_btrx0_dcap_lq_msb, self.__filter_btrx0_dcap_lq_lsb)
    @filter_btrx0_dcap_lq.setter
    def filter_btrx0_dcap_lq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx0_dcap_lq_addr, self.__filter_btrx0_dcap_lq_msb, self.__filter_btrx0_dcap_lq_lsb, value)

    @property
    def filter_btrx0_dcap_hq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx0_dcap_hq_addr, self.__filter_btrx0_dcap_hq_msb, self.__filter_btrx0_dcap_hq_lsb)
    @filter_btrx0_dcap_hq.setter
    def filter_btrx0_dcap_hq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx0_dcap_hq_addr, self.__filter_btrx0_dcap_hq_msb, self.__filter_btrx0_dcap_hq_lsb, value)

    @property
    def filter_btrx1_dcap_lq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx1_dcap_lq_addr, self.__filter_btrx1_dcap_lq_msb, self.__filter_btrx1_dcap_lq_lsb)
    @filter_btrx1_dcap_lq.setter
    def filter_btrx1_dcap_lq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx1_dcap_lq_addr, self.__filter_btrx1_dcap_lq_msb, self.__filter_btrx1_dcap_lq_lsb, value)

    @property
    def filter_btrx1_dcap_hq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx1_dcap_hq_addr, self.__filter_btrx1_dcap_hq_msb, self.__filter_btrx1_dcap_hq_lsb)
    @filter_btrx1_dcap_hq.setter
    def filter_btrx1_dcap_hq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx1_dcap_hq_addr, self.__filter_btrx1_dcap_hq_msb, self.__filter_btrx1_dcap_hq_lsb, value)

    @property
    def filter_btrx2_dcap_lq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx2_dcap_lq_addr, self.__filter_btrx2_dcap_lq_msb, self.__filter_btrx2_dcap_lq_lsb)
    @filter_btrx2_dcap_lq.setter
    def filter_btrx2_dcap_lq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx2_dcap_lq_addr, self.__filter_btrx2_dcap_lq_msb, self.__filter_btrx2_dcap_lq_lsb, value)

    @property
    def filter_btrx2_dcap_hq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx2_dcap_hq_addr, self.__filter_btrx2_dcap_hq_msb, self.__filter_btrx2_dcap_hq_lsb)
    @filter_btrx2_dcap_hq.setter
    def filter_btrx2_dcap_hq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx2_dcap_hq_addr, self.__filter_btrx2_dcap_hq_msb, self.__filter_btrx2_dcap_hq_lsb, value)

    @property
    def filter_btrx3_dcap_lq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx3_dcap_lq_addr, self.__filter_btrx3_dcap_lq_msb, self.__filter_btrx3_dcap_lq_lsb)
    @filter_btrx3_dcap_lq.setter
    def filter_btrx3_dcap_lq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx3_dcap_lq_addr, self.__filter_btrx3_dcap_lq_msb, self.__filter_btrx3_dcap_lq_lsb, value)

    @property
    def filter_btrx3_dcap_hq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx3_dcap_hq_addr, self.__filter_btrx3_dcap_hq_msb, self.__filter_btrx3_dcap_hq_lsb)
    @filter_btrx3_dcap_hq.setter
    def filter_btrx3_dcap_hq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx3_dcap_hq_addr, self.__filter_btrx3_dcap_hq_msb, self.__filter_btrx3_dcap_hq_lsb, value)

    @property
    def filter_bttx0_dcap_lq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx0_dcap_lq_addr, self.__filter_bttx0_dcap_lq_msb, self.__filter_bttx0_dcap_lq_lsb)
    @filter_bttx0_dcap_lq.setter
    def filter_bttx0_dcap_lq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx0_dcap_lq_addr, self.__filter_bttx0_dcap_lq_msb, self.__filter_bttx0_dcap_lq_lsb, value)

    @property
    def filter_bttx0_dcap_hq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx0_dcap_hq_addr, self.__filter_bttx0_dcap_hq_msb, self.__filter_bttx0_dcap_hq_lsb)
    @filter_bttx0_dcap_hq.setter
    def filter_bttx0_dcap_hq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx0_dcap_hq_addr, self.__filter_bttx0_dcap_hq_msb, self.__filter_bttx0_dcap_hq_lsb, value)

    @property
    def filter_bttx1_dcap_lq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx1_dcap_lq_addr, self.__filter_bttx1_dcap_lq_msb, self.__filter_bttx1_dcap_lq_lsb)
    @filter_bttx1_dcap_lq.setter
    def filter_bttx1_dcap_lq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx1_dcap_lq_addr, self.__filter_bttx1_dcap_lq_msb, self.__filter_bttx1_dcap_lq_lsb, value)

    @property
    def filter_bttx1_dcap_hq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx1_dcap_hq_addr, self.__filter_bttx1_dcap_hq_msb, self.__filter_bttx1_dcap_hq_lsb)
    @filter_bttx1_dcap_hq.setter
    def filter_bttx1_dcap_hq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx1_dcap_hq_addr, self.__filter_bttx1_dcap_hq_msb, self.__filter_bttx1_dcap_hq_lsb, value)

    @property
    def filter_bttx2_dcap_lq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx2_dcap_lq_addr, self.__filter_bttx2_dcap_lq_msb, self.__filter_bttx2_dcap_lq_lsb)
    @filter_bttx2_dcap_lq.setter
    def filter_bttx2_dcap_lq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx2_dcap_lq_addr, self.__filter_bttx2_dcap_lq_msb, self.__filter_bttx2_dcap_lq_lsb, value)

    @property
    def filter_bttx2_dcap_hq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx2_dcap_hq_addr, self.__filter_bttx2_dcap_hq_msb, self.__filter_bttx2_dcap_hq_lsb)
    @filter_bttx2_dcap_hq.setter
    def filter_bttx2_dcap_hq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx2_dcap_hq_addr, self.__filter_bttx2_dcap_hq_msb, self.__filter_bttx2_dcap_hq_lsb, value)

    @property
    def filter_bttx3_dcap_lq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx3_dcap_lq_addr, self.__filter_bttx3_dcap_lq_msb, self.__filter_bttx3_dcap_lq_lsb)
    @filter_bttx3_dcap_lq.setter
    def filter_bttx3_dcap_lq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx3_dcap_lq_addr, self.__filter_bttx3_dcap_lq_msb, self.__filter_bttx3_dcap_lq_lsb, value)

    @property
    def filter_bttx3_dcap_hq(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx3_dcap_hq_addr, self.__filter_bttx3_dcap_hq_msb, self.__filter_bttx3_dcap_hq_lsb)
    @filter_bttx3_dcap_hq.setter
    def filter_bttx3_dcap_hq(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx3_dcap_hq_addr, self.__filter_bttx3_dcap_hq_msb, self.__filter_bttx3_dcap_hq_lsb, value)

    @property
    def filter_wfrx0_dgdc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx0_dgdc_addr, self.__filter_wfrx0_dgdc_msb, self.__filter_wfrx0_dgdc_lsb)
    @filter_wfrx0_dgdc.setter
    def filter_wfrx0_dgdc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx0_dgdc_addr, self.__filter_wfrx0_dgdc_msb, self.__filter_wfrx0_dgdc_lsb, value)

    @property
    def filter_wfrx0_input_ld(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx0_input_ld_addr, self.__filter_wfrx0_input_ld_msb, self.__filter_wfrx0_input_ld_lsb)
    @filter_wfrx0_input_ld.setter
    def filter_wfrx0_input_ld(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx0_input_ld_addr, self.__filter_wfrx0_input_ld_msb, self.__filter_wfrx0_input_ld_lsb, value)

    @property
    def filter_wfrx0_bstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx0_bstb_addr, self.__filter_wfrx0_bstb_msb, self.__filter_wfrx0_bstb_lsb)
    @filter_wfrx0_bstb.setter
    def filter_wfrx0_bstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx0_bstb_addr, self.__filter_wfrx0_bstb_msb, self.__filter_wfrx0_bstb_lsb, value)

    @property
    def filter_wfrx0_dedge(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx0_dedge_addr, self.__filter_wfrx0_dedge_msb, self.__filter_wfrx0_dedge_lsb)
    @filter_wfrx0_dedge.setter
    def filter_wfrx0_dedge(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx0_dedge_addr, self.__filter_wfrx0_dedge_msb, self.__filter_wfrx0_dedge_lsb, value)

    @property
    def filter_wfrx1_dgdc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx1_dgdc_addr, self.__filter_wfrx1_dgdc_msb, self.__filter_wfrx1_dgdc_lsb)
    @filter_wfrx1_dgdc.setter
    def filter_wfrx1_dgdc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx1_dgdc_addr, self.__filter_wfrx1_dgdc_msb, self.__filter_wfrx1_dgdc_lsb, value)

    @property
    def filter_wfrx1_input_ld(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx1_input_ld_addr, self.__filter_wfrx1_input_ld_msb, self.__filter_wfrx1_input_ld_lsb)
    @filter_wfrx1_input_ld.setter
    def filter_wfrx1_input_ld(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx1_input_ld_addr, self.__filter_wfrx1_input_ld_msb, self.__filter_wfrx1_input_ld_lsb, value)

    @property
    def filter_wfrx1_bstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx1_bstb_addr, self.__filter_wfrx1_bstb_msb, self.__filter_wfrx1_bstb_lsb)
    @filter_wfrx1_bstb.setter
    def filter_wfrx1_bstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx1_bstb_addr, self.__filter_wfrx1_bstb_msb, self.__filter_wfrx1_bstb_lsb, value)

    @property
    def filter_wfrx1_dedge(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx1_dedge_addr, self.__filter_wfrx1_dedge_msb, self.__filter_wfrx1_dedge_lsb)
    @filter_wfrx1_dedge.setter
    def filter_wfrx1_dedge(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx1_dedge_addr, self.__filter_wfrx1_dedge_msb, self.__filter_wfrx1_dedge_lsb, value)

    @property
    def filter_wfrx2_dgdc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx2_dgdc_addr, self.__filter_wfrx2_dgdc_msb, self.__filter_wfrx2_dgdc_lsb)
    @filter_wfrx2_dgdc.setter
    def filter_wfrx2_dgdc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx2_dgdc_addr, self.__filter_wfrx2_dgdc_msb, self.__filter_wfrx2_dgdc_lsb, value)

    @property
    def filter_wfrx2_input_ld(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx2_input_ld_addr, self.__filter_wfrx2_input_ld_msb, self.__filter_wfrx2_input_ld_lsb)
    @filter_wfrx2_input_ld.setter
    def filter_wfrx2_input_ld(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx2_input_ld_addr, self.__filter_wfrx2_input_ld_msb, self.__filter_wfrx2_input_ld_lsb, value)

    @property
    def filter_wfrx2_bstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx2_bstb_addr, self.__filter_wfrx2_bstb_msb, self.__filter_wfrx2_bstb_lsb)
    @filter_wfrx2_bstb.setter
    def filter_wfrx2_bstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx2_bstb_addr, self.__filter_wfrx2_bstb_msb, self.__filter_wfrx2_bstb_lsb, value)

    @property
    def filter_wfrx2_dedge(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx2_dedge_addr, self.__filter_wfrx2_dedge_msb, self.__filter_wfrx2_dedge_lsb)
    @filter_wfrx2_dedge.setter
    def filter_wfrx2_dedge(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx2_dedge_addr, self.__filter_wfrx2_dedge_msb, self.__filter_wfrx2_dedge_lsb, value)

    @property
    def filter_wfrx3_dgdc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx3_dgdc_addr, self.__filter_wfrx3_dgdc_msb, self.__filter_wfrx3_dgdc_lsb)
    @filter_wfrx3_dgdc.setter
    def filter_wfrx3_dgdc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx3_dgdc_addr, self.__filter_wfrx3_dgdc_msb, self.__filter_wfrx3_dgdc_lsb, value)

    @property
    def filter_wfrx3_input_ld(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx3_input_ld_addr, self.__filter_wfrx3_input_ld_msb, self.__filter_wfrx3_input_ld_lsb)
    @filter_wfrx3_input_ld.setter
    def filter_wfrx3_input_ld(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx3_input_ld_addr, self.__filter_wfrx3_input_ld_msb, self.__filter_wfrx3_input_ld_lsb, value)

    @property
    def filter_wfrx3_bstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx3_bstb_addr, self.__filter_wfrx3_bstb_msb, self.__filter_wfrx3_bstb_lsb)
    @filter_wfrx3_bstb.setter
    def filter_wfrx3_bstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx3_bstb_addr, self.__filter_wfrx3_bstb_msb, self.__filter_wfrx3_bstb_lsb, value)

    @property
    def filter_wfrx3_dedge(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx3_dedge_addr, self.__filter_wfrx3_dedge_msb, self.__filter_wfrx3_dedge_lsb)
    @filter_wfrx3_dedge.setter
    def filter_wfrx3_dedge(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx3_dedge_addr, self.__filter_wfrx3_dedge_msb, self.__filter_wfrx3_dedge_lsb, value)

    @property
    def filter_wftx0_dgdc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx0_dgdc_addr, self.__filter_wftx0_dgdc_msb, self.__filter_wftx0_dgdc_lsb)
    @filter_wftx0_dgdc.setter
    def filter_wftx0_dgdc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx0_dgdc_addr, self.__filter_wftx0_dgdc_msb, self.__filter_wftx0_dgdc_lsb, value)

    @property
    def filter_wftx0_input_ld(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx0_input_ld_addr, self.__filter_wftx0_input_ld_msb, self.__filter_wftx0_input_ld_lsb)
    @filter_wftx0_input_ld.setter
    def filter_wftx0_input_ld(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx0_input_ld_addr, self.__filter_wftx0_input_ld_msb, self.__filter_wftx0_input_ld_lsb, value)

    @property
    def filter_wftx0_bstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx0_bstb_addr, self.__filter_wftx0_bstb_msb, self.__filter_wftx0_bstb_lsb)
    @filter_wftx0_bstb.setter
    def filter_wftx0_bstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx0_bstb_addr, self.__filter_wftx0_bstb_msb, self.__filter_wftx0_bstb_lsb, value)

    @property
    def filter_wftx0_dedge(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx0_dedge_addr, self.__filter_wftx0_dedge_msb, self.__filter_wftx0_dedge_lsb)
    @filter_wftx0_dedge.setter
    def filter_wftx0_dedge(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx0_dedge_addr, self.__filter_wftx0_dedge_msb, self.__filter_wftx0_dedge_lsb, value)

    @property
    def filter_wftx1_dgdc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx1_dgdc_addr, self.__filter_wftx1_dgdc_msb, self.__filter_wftx1_dgdc_lsb)
    @filter_wftx1_dgdc.setter
    def filter_wftx1_dgdc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx1_dgdc_addr, self.__filter_wftx1_dgdc_msb, self.__filter_wftx1_dgdc_lsb, value)

    @property
    def filter_wftx1_input_ld(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx1_input_ld_addr, self.__filter_wftx1_input_ld_msb, self.__filter_wftx1_input_ld_lsb)
    @filter_wftx1_input_ld.setter
    def filter_wftx1_input_ld(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx1_input_ld_addr, self.__filter_wftx1_input_ld_msb, self.__filter_wftx1_input_ld_lsb, value)

    @property
    def filter_wftx1_bstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx1_bstb_addr, self.__filter_wftx1_bstb_msb, self.__filter_wftx1_bstb_lsb)
    @filter_wftx1_bstb.setter
    def filter_wftx1_bstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx1_bstb_addr, self.__filter_wftx1_bstb_msb, self.__filter_wftx1_bstb_lsb, value)

    @property
    def filter_wftx1_dedge(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx1_dedge_addr, self.__filter_wftx1_dedge_msb, self.__filter_wftx1_dedge_lsb)
    @filter_wftx1_dedge.setter
    def filter_wftx1_dedge(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx1_dedge_addr, self.__filter_wftx1_dedge_msb, self.__filter_wftx1_dedge_lsb, value)

    @property
    def filter_wftx2_dgdc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx2_dgdc_addr, self.__filter_wftx2_dgdc_msb, self.__filter_wftx2_dgdc_lsb)
    @filter_wftx2_dgdc.setter
    def filter_wftx2_dgdc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx2_dgdc_addr, self.__filter_wftx2_dgdc_msb, self.__filter_wftx2_dgdc_lsb, value)

    @property
    def filter_wftx2_input_ld(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx2_input_ld_addr, self.__filter_wftx2_input_ld_msb, self.__filter_wftx2_input_ld_lsb)
    @filter_wftx2_input_ld.setter
    def filter_wftx2_input_ld(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx2_input_ld_addr, self.__filter_wftx2_input_ld_msb, self.__filter_wftx2_input_ld_lsb, value)

    @property
    def filter_wftx2_bstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx2_bstb_addr, self.__filter_wftx2_bstb_msb, self.__filter_wftx2_bstb_lsb)
    @filter_wftx2_bstb.setter
    def filter_wftx2_bstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx2_bstb_addr, self.__filter_wftx2_bstb_msb, self.__filter_wftx2_bstb_lsb, value)

    @property
    def filter_wftx2_dedge(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx2_dedge_addr, self.__filter_wftx2_dedge_msb, self.__filter_wftx2_dedge_lsb)
    @filter_wftx2_dedge.setter
    def filter_wftx2_dedge(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx2_dedge_addr, self.__filter_wftx2_dedge_msb, self.__filter_wftx2_dedge_lsb, value)

    @property
    def filter_wftx3_dgdc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx3_dgdc_addr, self.__filter_wftx3_dgdc_msb, self.__filter_wftx3_dgdc_lsb)
    @filter_wftx3_dgdc.setter
    def filter_wftx3_dgdc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx3_dgdc_addr, self.__filter_wftx3_dgdc_msb, self.__filter_wftx3_dgdc_lsb, value)

    @property
    def filter_wftx3_input_ld(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx3_input_ld_addr, self.__filter_wftx3_input_ld_msb, self.__filter_wftx3_input_ld_lsb)
    @filter_wftx3_input_ld.setter
    def filter_wftx3_input_ld(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx3_input_ld_addr, self.__filter_wftx3_input_ld_msb, self.__filter_wftx3_input_ld_lsb, value)

    @property
    def filter_wftx3_bstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx3_bstb_addr, self.__filter_wftx3_bstb_msb, self.__filter_wftx3_bstb_lsb)
    @filter_wftx3_bstb.setter
    def filter_wftx3_bstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx3_bstb_addr, self.__filter_wftx3_bstb_msb, self.__filter_wftx3_bstb_lsb, value)

    @property
    def filter_wftx3_dedge(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx3_dedge_addr, self.__filter_wftx3_dedge_msb, self.__filter_wftx3_dedge_lsb)
    @filter_wftx3_dedge.setter
    def filter_wftx3_dedge(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx3_dedge_addr, self.__filter_wftx3_dedge_msb, self.__filter_wftx3_dedge_lsb, value)

    @property
    def filter_btrx0_dgdc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx0_dgdc_addr, self.__filter_btrx0_dgdc_msb, self.__filter_btrx0_dgdc_lsb)
    @filter_btrx0_dgdc.setter
    def filter_btrx0_dgdc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx0_dgdc_addr, self.__filter_btrx0_dgdc_msb, self.__filter_btrx0_dgdc_lsb, value)

    @property
    def filter_btrx0_input_ld(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx0_input_ld_addr, self.__filter_btrx0_input_ld_msb, self.__filter_btrx0_input_ld_lsb)
    @filter_btrx0_input_ld.setter
    def filter_btrx0_input_ld(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx0_input_ld_addr, self.__filter_btrx0_input_ld_msb, self.__filter_btrx0_input_ld_lsb, value)

    @property
    def filter_btrx0_bstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx0_bstb_addr, self.__filter_btrx0_bstb_msb, self.__filter_btrx0_bstb_lsb)
    @filter_btrx0_bstb.setter
    def filter_btrx0_bstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx0_bstb_addr, self.__filter_btrx0_bstb_msb, self.__filter_btrx0_bstb_lsb, value)

    @property
    def filter_btrx0_dedge(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx0_dedge_addr, self.__filter_btrx0_dedge_msb, self.__filter_btrx0_dedge_lsb)
    @filter_btrx0_dedge.setter
    def filter_btrx0_dedge(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx0_dedge_addr, self.__filter_btrx0_dedge_msb, self.__filter_btrx0_dedge_lsb, value)

    @property
    def filter_btrx1_dgdc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx1_dgdc_addr, self.__filter_btrx1_dgdc_msb, self.__filter_btrx1_dgdc_lsb)
    @filter_btrx1_dgdc.setter
    def filter_btrx1_dgdc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx1_dgdc_addr, self.__filter_btrx1_dgdc_msb, self.__filter_btrx1_dgdc_lsb, value)

    @property
    def filter_btrx1_input_ld(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx1_input_ld_addr, self.__filter_btrx1_input_ld_msb, self.__filter_btrx1_input_ld_lsb)
    @filter_btrx1_input_ld.setter
    def filter_btrx1_input_ld(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx1_input_ld_addr, self.__filter_btrx1_input_ld_msb, self.__filter_btrx1_input_ld_lsb, value)

    @property
    def filter_btrx1_bstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx1_bstb_addr, self.__filter_btrx1_bstb_msb, self.__filter_btrx1_bstb_lsb)
    @filter_btrx1_bstb.setter
    def filter_btrx1_bstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx1_bstb_addr, self.__filter_btrx1_bstb_msb, self.__filter_btrx1_bstb_lsb, value)

    @property
    def filter_btrx1_dedge(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx1_dedge_addr, self.__filter_btrx1_dedge_msb, self.__filter_btrx1_dedge_lsb)
    @filter_btrx1_dedge.setter
    def filter_btrx1_dedge(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx1_dedge_addr, self.__filter_btrx1_dedge_msb, self.__filter_btrx1_dedge_lsb, value)

    @property
    def filter_btrx2_dgdc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx2_dgdc_addr, self.__filter_btrx2_dgdc_msb, self.__filter_btrx2_dgdc_lsb)
    @filter_btrx2_dgdc.setter
    def filter_btrx2_dgdc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx2_dgdc_addr, self.__filter_btrx2_dgdc_msb, self.__filter_btrx2_dgdc_lsb, value)

    @property
    def filter_btrx2_input_ld(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx2_input_ld_addr, self.__filter_btrx2_input_ld_msb, self.__filter_btrx2_input_ld_lsb)
    @filter_btrx2_input_ld.setter
    def filter_btrx2_input_ld(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx2_input_ld_addr, self.__filter_btrx2_input_ld_msb, self.__filter_btrx2_input_ld_lsb, value)

    @property
    def filter_btrx2_bstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx2_bstb_addr, self.__filter_btrx2_bstb_msb, self.__filter_btrx2_bstb_lsb)
    @filter_btrx2_bstb.setter
    def filter_btrx2_bstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx2_bstb_addr, self.__filter_btrx2_bstb_msb, self.__filter_btrx2_bstb_lsb, value)

    @property
    def filter_btrx2_dedge(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx2_dedge_addr, self.__filter_btrx2_dedge_msb, self.__filter_btrx2_dedge_lsb)
    @filter_btrx2_dedge.setter
    def filter_btrx2_dedge(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx2_dedge_addr, self.__filter_btrx2_dedge_msb, self.__filter_btrx2_dedge_lsb, value)

    @property
    def filter_btrx3_dgdc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx3_dgdc_addr, self.__filter_btrx3_dgdc_msb, self.__filter_btrx3_dgdc_lsb)
    @filter_btrx3_dgdc.setter
    def filter_btrx3_dgdc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx3_dgdc_addr, self.__filter_btrx3_dgdc_msb, self.__filter_btrx3_dgdc_lsb, value)

    @property
    def filter_btrx3_input_ld(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx3_input_ld_addr, self.__filter_btrx3_input_ld_msb, self.__filter_btrx3_input_ld_lsb)
    @filter_btrx3_input_ld.setter
    def filter_btrx3_input_ld(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx3_input_ld_addr, self.__filter_btrx3_input_ld_msb, self.__filter_btrx3_input_ld_lsb, value)

    @property
    def filter_btrx3_bstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx3_bstb_addr, self.__filter_btrx3_bstb_msb, self.__filter_btrx3_bstb_lsb)
    @filter_btrx3_bstb.setter
    def filter_btrx3_bstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx3_bstb_addr, self.__filter_btrx3_bstb_msb, self.__filter_btrx3_bstb_lsb, value)

    @property
    def filter_btrx3_dedge(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx3_dedge_addr, self.__filter_btrx3_dedge_msb, self.__filter_btrx3_dedge_lsb)
    @filter_btrx3_dedge.setter
    def filter_btrx3_dedge(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx3_dedge_addr, self.__filter_btrx3_dedge_msb, self.__filter_btrx3_dedge_lsb, value)

    @property
    def filter_bttx0_dgdc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx0_dgdc_addr, self.__filter_bttx0_dgdc_msb, self.__filter_bttx0_dgdc_lsb)
    @filter_bttx0_dgdc.setter
    def filter_bttx0_dgdc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx0_dgdc_addr, self.__filter_bttx0_dgdc_msb, self.__filter_bttx0_dgdc_lsb, value)

    @property
    def filter_bttx0_input_ld(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx0_input_ld_addr, self.__filter_bttx0_input_ld_msb, self.__filter_bttx0_input_ld_lsb)
    @filter_bttx0_input_ld.setter
    def filter_bttx0_input_ld(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx0_input_ld_addr, self.__filter_bttx0_input_ld_msb, self.__filter_bttx0_input_ld_lsb, value)

    @property
    def filter_bttx0_bstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx0_bstb_addr, self.__filter_bttx0_bstb_msb, self.__filter_bttx0_bstb_lsb)
    @filter_bttx0_bstb.setter
    def filter_bttx0_bstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx0_bstb_addr, self.__filter_bttx0_bstb_msb, self.__filter_bttx0_bstb_lsb, value)

    @property
    def filter_bttx0_dedge(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx0_dedge_addr, self.__filter_bttx0_dedge_msb, self.__filter_bttx0_dedge_lsb)
    @filter_bttx0_dedge.setter
    def filter_bttx0_dedge(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx0_dedge_addr, self.__filter_bttx0_dedge_msb, self.__filter_bttx0_dedge_lsb, value)

    @property
    def filter_bttx1_dgdc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx1_dgdc_addr, self.__filter_bttx1_dgdc_msb, self.__filter_bttx1_dgdc_lsb)
    @filter_bttx1_dgdc.setter
    def filter_bttx1_dgdc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx1_dgdc_addr, self.__filter_bttx1_dgdc_msb, self.__filter_bttx1_dgdc_lsb, value)

    @property
    def filter_bttx1_input_ld(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx1_input_ld_addr, self.__filter_bttx1_input_ld_msb, self.__filter_bttx1_input_ld_lsb)
    @filter_bttx1_input_ld.setter
    def filter_bttx1_input_ld(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx1_input_ld_addr, self.__filter_bttx1_input_ld_msb, self.__filter_bttx1_input_ld_lsb, value)

    @property
    def filter_bttx1_bstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx1_bstb_addr, self.__filter_bttx1_bstb_msb, self.__filter_bttx1_bstb_lsb)
    @filter_bttx1_bstb.setter
    def filter_bttx1_bstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx1_bstb_addr, self.__filter_bttx1_bstb_msb, self.__filter_bttx1_bstb_lsb, value)

    @property
    def filter_bttx1_dedge(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx1_dedge_addr, self.__filter_bttx1_dedge_msb, self.__filter_bttx1_dedge_lsb)
    @filter_bttx1_dedge.setter
    def filter_bttx1_dedge(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx1_dedge_addr, self.__filter_bttx1_dedge_msb, self.__filter_bttx1_dedge_lsb, value)

    @property
    def filter_bttx2_dgdc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx2_dgdc_addr, self.__filter_bttx2_dgdc_msb, self.__filter_bttx2_dgdc_lsb)
    @filter_bttx2_dgdc.setter
    def filter_bttx2_dgdc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx2_dgdc_addr, self.__filter_bttx2_dgdc_msb, self.__filter_bttx2_dgdc_lsb, value)

    @property
    def filter_bttx2_input_ld(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx2_input_ld_addr, self.__filter_bttx2_input_ld_msb, self.__filter_bttx2_input_ld_lsb)
    @filter_bttx2_input_ld.setter
    def filter_bttx2_input_ld(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx2_input_ld_addr, self.__filter_bttx2_input_ld_msb, self.__filter_bttx2_input_ld_lsb, value)

    @property
    def filter_bttx2_bstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx2_bstb_addr, self.__filter_bttx2_bstb_msb, self.__filter_bttx2_bstb_lsb)
    @filter_bttx2_bstb.setter
    def filter_bttx2_bstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx2_bstb_addr, self.__filter_bttx2_bstb_msb, self.__filter_bttx2_bstb_lsb, value)

    @property
    def filter_bttx2_dedge(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx2_dedge_addr, self.__filter_bttx2_dedge_msb, self.__filter_bttx2_dedge_lsb)
    @filter_bttx2_dedge.setter
    def filter_bttx2_dedge(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx2_dedge_addr, self.__filter_bttx2_dedge_msb, self.__filter_bttx2_dedge_lsb, value)

    @property
    def filter_bttx3_dgdc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx3_dgdc_addr, self.__filter_bttx3_dgdc_msb, self.__filter_bttx3_dgdc_lsb)
    @filter_bttx3_dgdc.setter
    def filter_bttx3_dgdc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx3_dgdc_addr, self.__filter_bttx3_dgdc_msb, self.__filter_bttx3_dgdc_lsb, value)

    @property
    def filter_bttx3_input_ld(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx3_input_ld_addr, self.__filter_bttx3_input_ld_msb, self.__filter_bttx3_input_ld_lsb)
    @filter_bttx3_input_ld.setter
    def filter_bttx3_input_ld(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx3_input_ld_addr, self.__filter_bttx3_input_ld_msb, self.__filter_bttx3_input_ld_lsb, value)

    @property
    def filter_bttx3_bstb(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx3_bstb_addr, self.__filter_bttx3_bstb_msb, self.__filter_bttx3_bstb_lsb)
    @filter_bttx3_bstb.setter
    def filter_bttx3_bstb(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx3_bstb_addr, self.__filter_bttx3_bstb_msb, self.__filter_bttx3_bstb_lsb, value)

    @property
    def filter_bttx3_dedge(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx3_dedge_addr, self.__filter_bttx3_dedge_msb, self.__filter_bttx3_dedge_lsb)
    @filter_bttx3_dedge.setter
    def filter_bttx3_dedge(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx3_dedge_addr, self.__filter_bttx3_dedge_msb, self.__filter_bttx3_dedge_lsb, value)

    @property
    def filter_wfrx0_dcc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx0_dcc_addr, self.__filter_wfrx0_dcc_msb, self.__filter_wfrx0_dcc_lsb)
    @filter_wfrx0_dcc.setter
    def filter_wfrx0_dcc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx0_dcc_addr, self.__filter_wfrx0_dcc_msb, self.__filter_wfrx0_dcc_lsb, value)

    @property
    def filter_wfrx1_dcc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx1_dcc_addr, self.__filter_wfrx1_dcc_msb, self.__filter_wfrx1_dcc_lsb)
    @filter_wfrx1_dcc.setter
    def filter_wfrx1_dcc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx1_dcc_addr, self.__filter_wfrx1_dcc_msb, self.__filter_wfrx1_dcc_lsb, value)

    @property
    def filter_wfrx2_dcc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx2_dcc_addr, self.__filter_wfrx2_dcc_msb, self.__filter_wfrx2_dcc_lsb)
    @filter_wfrx2_dcc.setter
    def filter_wfrx2_dcc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx2_dcc_addr, self.__filter_wfrx2_dcc_msb, self.__filter_wfrx2_dcc_lsb, value)

    @property
    def filter_wfrx3_dcc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wfrx3_dcc_addr, self.__filter_wfrx3_dcc_msb, self.__filter_wfrx3_dcc_lsb)
    @filter_wfrx3_dcc.setter
    def filter_wfrx3_dcc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wfrx3_dcc_addr, self.__filter_wfrx3_dcc_msb, self.__filter_wfrx3_dcc_lsb, value)

    @property
    def filter_wftx0_dcc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx0_dcc_addr, self.__filter_wftx0_dcc_msb, self.__filter_wftx0_dcc_lsb)
    @filter_wftx0_dcc.setter
    def filter_wftx0_dcc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx0_dcc_addr, self.__filter_wftx0_dcc_msb, self.__filter_wftx0_dcc_lsb, value)

    @property
    def filter_wftx1_dcc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx1_dcc_addr, self.__filter_wftx1_dcc_msb, self.__filter_wftx1_dcc_lsb)
    @filter_wftx1_dcc.setter
    def filter_wftx1_dcc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx1_dcc_addr, self.__filter_wftx1_dcc_msb, self.__filter_wftx1_dcc_lsb, value)

    @property
    def filter_wftx2_dcc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx2_dcc_addr, self.__filter_wftx2_dcc_msb, self.__filter_wftx2_dcc_lsb)
    @filter_wftx2_dcc.setter
    def filter_wftx2_dcc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx2_dcc_addr, self.__filter_wftx2_dcc_msb, self.__filter_wftx2_dcc_lsb, value)

    @property
    def filter_wftx3_dcc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_wftx3_dcc_addr, self.__filter_wftx3_dcc_msb, self.__filter_wftx3_dcc_lsb)
    @filter_wftx3_dcc.setter
    def filter_wftx3_dcc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_wftx3_dcc_addr, self.__filter_wftx3_dcc_msb, self.__filter_wftx3_dcc_lsb, value)

    @property
    def filter_btrx0_dcc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx0_dcc_addr, self.__filter_btrx0_dcc_msb, self.__filter_btrx0_dcc_lsb)
    @filter_btrx0_dcc.setter
    def filter_btrx0_dcc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx0_dcc_addr, self.__filter_btrx0_dcc_msb, self.__filter_btrx0_dcc_lsb, value)

    @property
    def filter_btrx1_dcc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx1_dcc_addr, self.__filter_btrx1_dcc_msb, self.__filter_btrx1_dcc_lsb)
    @filter_btrx1_dcc.setter
    def filter_btrx1_dcc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx1_dcc_addr, self.__filter_btrx1_dcc_msb, self.__filter_btrx1_dcc_lsb, value)

    @property
    def filter_btrx2_dcc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx2_dcc_addr, self.__filter_btrx2_dcc_msb, self.__filter_btrx2_dcc_lsb)
    @filter_btrx2_dcc.setter
    def filter_btrx2_dcc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx2_dcc_addr, self.__filter_btrx2_dcc_msb, self.__filter_btrx2_dcc_lsb, value)

    @property
    def filter_btrx3_dcc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_btrx3_dcc_addr, self.__filter_btrx3_dcc_msb, self.__filter_btrx3_dcc_lsb)
    @filter_btrx3_dcc.setter
    def filter_btrx3_dcc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_btrx3_dcc_addr, self.__filter_btrx3_dcc_msb, self.__filter_btrx3_dcc_lsb, value)

    @property
    def filter_bttx0_dcc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx0_dcc_addr, self.__filter_bttx0_dcc_msb, self.__filter_bttx0_dcc_lsb)
    @filter_bttx0_dcc.setter
    def filter_bttx0_dcc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx0_dcc_addr, self.__filter_bttx0_dcc_msb, self.__filter_bttx0_dcc_lsb, value)

    @property
    def filter_bttx1_dcc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx1_dcc_addr, self.__filter_bttx1_dcc_msb, self.__filter_bttx1_dcc_lsb)
    @filter_bttx1_dcc.setter
    def filter_bttx1_dcc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx1_dcc_addr, self.__filter_bttx1_dcc_msb, self.__filter_bttx1_dcc_lsb, value)

    @property
    def filter_bttx2_dcc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx2_dcc_addr, self.__filter_bttx2_dcc_msb, self.__filter_bttx2_dcc_lsb)
    @filter_bttx2_dcc.setter
    def filter_bttx2_dcc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx2_dcc_addr, self.__filter_bttx2_dcc_msb, self.__filter_bttx2_dcc_lsb, value)

    @property
    def filter_bttx3_dcc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__filter_bttx3_dcc_addr, self.__filter_bttx3_dcc_msb, self.__filter_bttx3_dcc_lsb)
    @filter_bttx3_dcc.setter
    def filter_bttx3_dcc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__filter_bttx3_dcc_addr, self.__filter_bttx3_dcc_msb, self.__filter_bttx3_dcc_lsb, value)
