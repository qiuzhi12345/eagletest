from hal.common import *
from hal.hwregister.hwi2c.CHIP722.addr_base import *
class CKGEN(object):
    def __init__(self, channel, chipv = "CHIP722"):
        self.chipv = chipv
        self.channel = channel
        self.__I2C = I2C(self.channel, self.chipv)
        self.__base = CKGEN_BASE
        self.__hostid = CKGEN_HOSTID
        self.__sel_rx_lsb = 0
        self.__sel_rx_msb = 0
        self.__sel_rx_addr = 0x0
        self.__sel_tx_lsb = 1
        self.__sel_tx_msb = 1
        self.__sel_tx_addr = 0x0
        self.__force_pd_rx_lsb = 2
        self.__force_pd_rx_msb = 2
        self.__force_pd_rx_addr = 0x0
        self.__force_pd_tx_lsb = 3
        self.__force_pd_tx_msb = 3
        self.__force_pd_tx_addr = 0x0
        self.__sel_plan_b_lsb = 4
        self.__sel_plan_b_msb = 4
        self.__sel_plan_b_addr = 0x0
        self.__xpd_ckgen_lsb = 5
        self.__xpd_ckgen_msb = 5
        self.__xpd_ckgen_addr = 0x0
        self.__xpd_ckgen_buf_lsb = 6
        self.__xpd_ckgen_buf_msb = 6
        self.__xpd_ckgen_buf_addr = 0x0
        self.__ent_ckgen_pkdet_lsb = 7
        self.__ent_ckgen_pkdet_msb = 7
        self.__ent_ckgen_pkdet_addr = 0x0
        self.__dres_pp2g_lsb = 0
        self.__dres_pp2g_msb = 3
        self.__dres_pp2g_addr = 0x1
        self.__dres_pp4g_lsb = 4
        self.__dres_pp4g_msb = 7
        self.__dres_pp4g_addr = 0x1
        self.__dtest_ckgen_pkdet_lsb = 0
        self.__dtest_ckgen_pkdet_msb = 1
        self.__dtest_ckgen_pkdet_addr = 0x2
        self.__xpd_pkdet_pp4g_i_lsb = 2
        self.__xpd_pkdet_pp4g_i_msb = 2
        self.__xpd_pkdet_pp4g_i_addr = 0x2
        self.__xpd_pkdet_pp4g_q_lsb = 3
        self.__xpd_pkdet_pp4g_q_msb = 3
        self.__xpd_pkdet_pp4g_q_addr = 0x2
        self.__version_lsb = 4
        self.__version_msb = 7
        self.__version_addr = 0x2
        self.__fc_counts_en_7_0_lsb = 0
        self.__fc_counts_en_7_0_msb = 7
        self.__fc_counts_en_7_0_addr = 0x3
        self.__fc_counts_en_9_8_lsb = 0
        self.__fc_counts_en_9_8_msb = 1
        self.__fc_counts_en_9_8_addr = 0x4
        self.__fc_reset_n_lsb = 2
        self.__fc_reset_n_msb = 2
        self.__fc_reset_n_addr = 0x4
        self.__fc_start_lsb = 3
        self.__fc_start_msb = 3
        self.__fc_start_addr = 0x4
        self.__xpd_fc_lsb = 4
        self.__xpd_fc_msb = 4
        self.__xpd_fc_addr = 0x4
        self.__fc_cint_7_0_lsb = 0
        self.__fc_cint_7_0_msb = 7
        self.__fc_cint_7_0_addr = 0x5
        self.__fc_cint_13_8_lsb = 0
        self.__fc_cint_13_8_msb = 5
        self.__fc_cint_13_8_addr = 0x6
        self.__fc_cout_target_7_0_lsb = 0
        self.__fc_cout_target_7_0_msb = 7
        self.__fc_cout_target_7_0_addr = 0x7
        self.__fc_cout_target_13_8_lsb = 0
        self.__fc_cout_target_13_8_msb = 5
        self.__fc_cout_target_13_8_addr = 0x8

    def reg_addr_rd(self,reg_addr):
        return self.__I2C.i2c_rd(self.__base , self.__hostid ,reg_addr)
    def reg_addr_wr(self,reg_addr,value):
        return self.__I2C.i2c_wr(self.__base , self.__hostid ,reg_addr,value)

    @property
    def sel_rx(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sel_rx_addr, self.__sel_rx_msb, self.__sel_rx_lsb)
    @sel_rx.setter
    def sel_rx(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sel_rx_addr, self.__sel_rx_msb, self.__sel_rx_lsb, value)

    @property
    def sel_tx(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sel_tx_addr, self.__sel_tx_msb, self.__sel_tx_lsb)
    @sel_tx.setter
    def sel_tx(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sel_tx_addr, self.__sel_tx_msb, self.__sel_tx_lsb, value)

    @property
    def force_pd_rx(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__force_pd_rx_addr, self.__force_pd_rx_msb, self.__force_pd_rx_lsb)
    @force_pd_rx.setter
    def force_pd_rx(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__force_pd_rx_addr, self.__force_pd_rx_msb, self.__force_pd_rx_lsb, value)

    @property
    def force_pd_tx(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__force_pd_tx_addr, self.__force_pd_tx_msb, self.__force_pd_tx_lsb)
    @force_pd_tx.setter
    def force_pd_tx(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__force_pd_tx_addr, self.__force_pd_tx_msb, self.__force_pd_tx_lsb, value)

    @property
    def sel_plan_b(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__sel_plan_b_addr, self.__sel_plan_b_msb, self.__sel_plan_b_lsb)
    @sel_plan_b.setter
    def sel_plan_b(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__sel_plan_b_addr, self.__sel_plan_b_msb, self.__sel_plan_b_lsb, value)

    @property
    def xpd_ckgen(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_ckgen_addr, self.__xpd_ckgen_msb, self.__xpd_ckgen_lsb)
    @xpd_ckgen.setter
    def xpd_ckgen(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_ckgen_addr, self.__xpd_ckgen_msb, self.__xpd_ckgen_lsb, value)

    @property
    def xpd_ckgen_buf(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_ckgen_buf_addr, self.__xpd_ckgen_buf_msb, self.__xpd_ckgen_buf_lsb)
    @xpd_ckgen_buf.setter
    def xpd_ckgen_buf(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_ckgen_buf_addr, self.__xpd_ckgen_buf_msb, self.__xpd_ckgen_buf_lsb, value)

    @property
    def ent_ckgen_pkdet(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__ent_ckgen_pkdet_addr, self.__ent_ckgen_pkdet_msb, self.__ent_ckgen_pkdet_lsb)
    @ent_ckgen_pkdet.setter
    def ent_ckgen_pkdet(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__ent_ckgen_pkdet_addr, self.__ent_ckgen_pkdet_msb, self.__ent_ckgen_pkdet_lsb, value)

    @property
    def dres_pp2g(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dres_pp2g_addr, self.__dres_pp2g_msb, self.__dres_pp2g_lsb)
    @dres_pp2g.setter
    def dres_pp2g(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dres_pp2g_addr, self.__dres_pp2g_msb, self.__dres_pp2g_lsb, value)

    @property
    def dres_pp4g(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dres_pp4g_addr, self.__dres_pp4g_msb, self.__dres_pp4g_lsb)
    @dres_pp4g.setter
    def dres_pp4g(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dres_pp4g_addr, self.__dres_pp4g_msb, self.__dres_pp4g_lsb, value)

    @property
    def dtest_ckgen_pkdet(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__dtest_ckgen_pkdet_addr, self.__dtest_ckgen_pkdet_msb, self.__dtest_ckgen_pkdet_lsb)
    @dtest_ckgen_pkdet.setter
    def dtest_ckgen_pkdet(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__dtest_ckgen_pkdet_addr, self.__dtest_ckgen_pkdet_msb, self.__dtest_ckgen_pkdet_lsb, value)

    @property
    def xpd_pkdet_pp4g_i(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_pkdet_pp4g_i_addr, self.__xpd_pkdet_pp4g_i_msb, self.__xpd_pkdet_pp4g_i_lsb)
    @xpd_pkdet_pp4g_i.setter
    def xpd_pkdet_pp4g_i(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_pkdet_pp4g_i_addr, self.__xpd_pkdet_pp4g_i_msb, self.__xpd_pkdet_pp4g_i_lsb, value)

    @property
    def xpd_pkdet_pp4g_q(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_pkdet_pp4g_q_addr, self.__xpd_pkdet_pp4g_q_msb, self.__xpd_pkdet_pp4g_q_lsb)
    @xpd_pkdet_pp4g_q.setter
    def xpd_pkdet_pp4g_q(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_pkdet_pp4g_q_addr, self.__xpd_pkdet_pp4g_q_msb, self.__xpd_pkdet_pp4g_q_lsb, value)

    @property
    def version(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__version_addr, self.__version_msb, self.__version_lsb)
    @version.setter
    def version(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__version_addr, self.__version_msb, self.__version_lsb, value)

    @property
    def fc_counts_en_7_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__fc_counts_en_7_0_addr, self.__fc_counts_en_7_0_msb, self.__fc_counts_en_7_0_lsb)
    @fc_counts_en_7_0.setter
    def fc_counts_en_7_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__fc_counts_en_7_0_addr, self.__fc_counts_en_7_0_msb, self.__fc_counts_en_7_0_lsb, value)

    @property
    def fc_counts_en_9_8(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__fc_counts_en_9_8_addr, self.__fc_counts_en_9_8_msb, self.__fc_counts_en_9_8_lsb)
    @fc_counts_en_9_8.setter
    def fc_counts_en_9_8(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__fc_counts_en_9_8_addr, self.__fc_counts_en_9_8_msb, self.__fc_counts_en_9_8_lsb, value)

    @property
    def fc_reset_n(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__fc_reset_n_addr, self.__fc_reset_n_msb, self.__fc_reset_n_lsb)
    @fc_reset_n.setter
    def fc_reset_n(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__fc_reset_n_addr, self.__fc_reset_n_msb, self.__fc_reset_n_lsb, value)

    @property
    def fc_start(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__fc_start_addr, self.__fc_start_msb, self.__fc_start_lsb)
    @fc_start.setter
    def fc_start(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__fc_start_addr, self.__fc_start_msb, self.__fc_start_lsb, value)

    @property
    def xpd_fc(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__xpd_fc_addr, self.__xpd_fc_msb, self.__xpd_fc_lsb)
    @xpd_fc.setter
    def xpd_fc(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__xpd_fc_addr, self.__xpd_fc_msb, self.__xpd_fc_lsb, value)

    @property
    def fc_cint_7_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__fc_cint_7_0_addr, self.__fc_cint_7_0_msb, self.__fc_cint_7_0_lsb)
    @fc_cint_7_0.setter
    def fc_cint_7_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__fc_cint_7_0_addr, self.__fc_cint_7_0_msb, self.__fc_cint_7_0_lsb, value)

    @property
    def fc_cint_13_8(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__fc_cint_13_8_addr, self.__fc_cint_13_8_msb, self.__fc_cint_13_8_lsb)
    @fc_cint_13_8.setter
    def fc_cint_13_8(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__fc_cint_13_8_addr, self.__fc_cint_13_8_msb, self.__fc_cint_13_8_lsb, value)

    @property
    def fc_cout_target_7_0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__fc_cout_target_7_0_addr, self.__fc_cout_target_7_0_msb, self.__fc_cout_target_7_0_lsb)
    @fc_cout_target_7_0.setter
    def fc_cout_target_7_0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__fc_cout_target_7_0_addr, self.__fc_cout_target_7_0_msb, self.__fc_cout_target_7_0_lsb, value)

    @property
    def fc_cout_target_13_8(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__fc_cout_target_13_8_addr, self.__fc_cout_target_13_8_msb, self.__fc_cout_target_13_8_lsb)
    @fc_cout_target_13_8.setter
    def fc_cout_target_13_8(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__fc_cout_target_13_8_addr, self.__fc_cout_target_13_8_msb, self.__fc_cout_target_13_8_lsb, value)
