from hal.common import *
from hal.hwregister.hwi2c.CHIP724.addr_base import *
class RFTX(object):
    def __init__(self, channel, chipv = "CHIP724"):
        self.chipv = chipv
        self.channel = channel
        self.__I2C = I2C(self.channel, self.chipv)
        self.__base = RFTX_BASE
        self.__hostid = RFTX_HOSTID
        self.__TMX2G_CCT_LOAD_lsb = 0
        self.__TMX2G_CCT_LOAD_msb = 3
        self.__TMX2G_CCT_LOAD_addr = 0x1
        self.__TMX2G_RCT_LOAD_lsb = 4
        self.__TMX2G_RCT_LOAD_msb = 6
        self.__TMX2G_RCT_LOAD_addr = 0x1
        self.__PA2G_CCT_STG1_lsb = 0
        self.__PA2G_CCT_STG1_msb = 3
        self.__PA2G_CCT_STG1_addr = 0x2
        self.__PA2G_CCT_STG2_lsb = 4
        self.__PA2G_CCT_STG2_msb = 7
        self.__PA2G_CCT_STG2_addr = 0x2
        self.__PA2G_ICT_STG0_lsb = 0
        self.__PA2G_ICT_STG0_msb = 3
        self.__PA2G_ICT_STG0_addr = 0x3
        self.__PA2G_ICT_STG0_CGM_lsb = 4
        self.__PA2G_ICT_STG0_CGM_msb = 7
        self.__PA2G_ICT_STG0_CGM_addr = 0x3
        self.__PA2G_ICT_STG1_lsb = 0
        self.__PA2G_ICT_STG1_msb = 3
        self.__PA2G_ICT_STG1_addr = 0x4
        self.__PA2G_ICT_STG1_CGM_lsb = 4
        self.__PA2G_ICT_STG1_CGM_msb = 7
        self.__PA2G_ICT_STG1_CGM_addr = 0x4
        self.__PA2G_ICT_STG2_lsb = 0
        self.__PA2G_ICT_STG2_msb = 3
        self.__PA2G_ICT_STG2_addr = 0x5
        self.__PA2G_CCT2F_STG0_lsb = 4
        self.__PA2G_CCT2F_STG0_msb = 7
        self.__PA2G_CCT2F_STG0_addr = 0x5
        self.__PA2G_MCT_CLASSB_lsb = 0
        self.__PA2G_MCT_CLASSB_msb = 1
        self.__PA2G_MCT_CLASSB_addr = 0x6
        self.__PA2G_RCT_STG2_lsb = 3
        self.__PA2G_RCT_STG2_msb = 5
        self.__PA2G_RCT_STG2_addr = 0x6
        self.__PA2G_STG1_SEL_ICGM_lsb = 6
        self.__PA2G_STG1_SEL_ICGM_msb = 6
        self.__PA2G_STG1_SEL_ICGM_addr = 0x6
        self.__PA2G_STG1_SEL_ICGM_N_lsb = 7
        self.__PA2G_STG1_SEL_ICGM_N_msb = 7
        self.__PA2G_STG1_SEL_ICGM_N_addr = 0x6
        self.__PA2G_VCT_CSC_STG0_lsb = 0
        self.__PA2G_VCT_CSC_STG0_msb = 3
        self.__PA2G_VCT_CSC_STG0_addr = 0x7
        self.__PA2G_VCT_CSC_STG1_lsb = 4
        self.__PA2G_VCT_CSC_STG1_msb = 7
        self.__PA2G_VCT_CSC_STG1_addr = 0x7
        self.__PA2G_VCT_CSC_STG2_lsb = 0
        self.__PA2G_VCT_CSC_STG2_msb = 3
        self.__PA2G_VCT_CSC_STG2_addr = 0x8
        self.__PA2G_PKDET_EN_lsb = 4
        self.__PA2G_PKDET_EN_msb = 6
        self.__PA2G_PKDET_EN_addr = 0x8
        self.__TR_lsb = 0
        self.__TR_msb = 2
        self.__TR_addr = 0x9
        self.__TE_PA2G_lsb = 3
        self.__TE_PA2G_msb = 3
        self.__TE_PA2G_addr = 0x9
        self.__LB_EN_lsb = 4
        self.__LB_EN_msb = 4
        self.__LB_EN_addr = 0x9
        self.__LB_EN_IQ_lsb = 5
        self.__LB_EN_IQ_msb = 5
        self.__LB_EN_IQ_addr = 0x9
        self.__LB_GCT_lsb = 6
        self.__LB_GCT_msb = 6
        self.__LB_GCT_addr = 0x9
        self.__TE_PWDET_lsb = 7
        self.__TE_PWDET_msb = 7
        self.__TE_PWDET_addr = 0x9
        self.__PWDET_VTH_TUNE_lsb = 0
        self.__PWDET_VTH_TUNE_msb = 3
        self.__PWDET_VTH_TUNE_addr = 0xa
        self.__SPARE_TX_lsb = 0
        self.__SPARE_TX_msb = 7
        self.__SPARE_TX_addr = 0xb

    def reg_addr_rd(self,reg_addr):
        return self.__I2C.i2c_rd(self.__base , self.__hostid ,reg_addr)
    def reg_addr_wr(self,reg_addr,value):
        return self.__I2C.i2c_wr(self.__base , self.__hostid ,reg_addr,value)

    @property
    def TMX2G_CCT_LOAD(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__TMX2G_CCT_LOAD_addr, self.__TMX2G_CCT_LOAD_msb, self.__TMX2G_CCT_LOAD_lsb)
    @TMX2G_CCT_LOAD.setter
    def TMX2G_CCT_LOAD(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__TMX2G_CCT_LOAD_addr, self.__TMX2G_CCT_LOAD_msb, self.__TMX2G_CCT_LOAD_lsb, value)

    @property
    def TMX2G_RCT_LOAD(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__TMX2G_RCT_LOAD_addr, self.__TMX2G_RCT_LOAD_msb, self.__TMX2G_RCT_LOAD_lsb)
    @TMX2G_RCT_LOAD.setter
    def TMX2G_RCT_LOAD(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__TMX2G_RCT_LOAD_addr, self.__TMX2G_RCT_LOAD_msb, self.__TMX2G_RCT_LOAD_lsb, value)

    @property
    def PA2G_CCT_STG1(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__PA2G_CCT_STG1_addr, self.__PA2G_CCT_STG1_msb, self.__PA2G_CCT_STG1_lsb)
    @PA2G_CCT_STG1.setter
    def PA2G_CCT_STG1(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__PA2G_CCT_STG1_addr, self.__PA2G_CCT_STG1_msb, self.__PA2G_CCT_STG1_lsb, value)

    @property
    def PA2G_CCT_STG2(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__PA2G_CCT_STG2_addr, self.__PA2G_CCT_STG2_msb, self.__PA2G_CCT_STG2_lsb)
    @PA2G_CCT_STG2.setter
    def PA2G_CCT_STG2(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__PA2G_CCT_STG2_addr, self.__PA2G_CCT_STG2_msb, self.__PA2G_CCT_STG2_lsb, value)

    @property
    def PA2G_ICT_STG0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__PA2G_ICT_STG0_addr, self.__PA2G_ICT_STG0_msb, self.__PA2G_ICT_STG0_lsb)
    @PA2G_ICT_STG0.setter
    def PA2G_ICT_STG0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__PA2G_ICT_STG0_addr, self.__PA2G_ICT_STG0_msb, self.__PA2G_ICT_STG0_lsb, value)

    @property
    def PA2G_ICT_STG0_CGM(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__PA2G_ICT_STG0_CGM_addr, self.__PA2G_ICT_STG0_CGM_msb, self.__PA2G_ICT_STG0_CGM_lsb)
    @PA2G_ICT_STG0_CGM.setter
    def PA2G_ICT_STG0_CGM(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__PA2G_ICT_STG0_CGM_addr, self.__PA2G_ICT_STG0_CGM_msb, self.__PA2G_ICT_STG0_CGM_lsb, value)

    @property
    def PA2G_ICT_STG1(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__PA2G_ICT_STG1_addr, self.__PA2G_ICT_STG1_msb, self.__PA2G_ICT_STG1_lsb)
    @PA2G_ICT_STG1.setter
    def PA2G_ICT_STG1(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__PA2G_ICT_STG1_addr, self.__PA2G_ICT_STG1_msb, self.__PA2G_ICT_STG1_lsb, value)

    @property
    def PA2G_ICT_STG1_CGM(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__PA2G_ICT_STG1_CGM_addr, self.__PA2G_ICT_STG1_CGM_msb, self.__PA2G_ICT_STG1_CGM_lsb)
    @PA2G_ICT_STG1_CGM.setter
    def PA2G_ICT_STG1_CGM(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__PA2G_ICT_STG1_CGM_addr, self.__PA2G_ICT_STG1_CGM_msb, self.__PA2G_ICT_STG1_CGM_lsb, value)

    @property
    def PA2G_ICT_STG2(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__PA2G_ICT_STG2_addr, self.__PA2G_ICT_STG2_msb, self.__PA2G_ICT_STG2_lsb)
    @PA2G_ICT_STG2.setter
    def PA2G_ICT_STG2(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__PA2G_ICT_STG2_addr, self.__PA2G_ICT_STG2_msb, self.__PA2G_ICT_STG2_lsb, value)

    @property
    def PA2G_CCT2F_STG0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__PA2G_CCT2F_STG0_addr, self.__PA2G_CCT2F_STG0_msb, self.__PA2G_CCT2F_STG0_lsb)
    @PA2G_CCT2F_STG0.setter
    def PA2G_CCT2F_STG0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__PA2G_CCT2F_STG0_addr, self.__PA2G_CCT2F_STG0_msb, self.__PA2G_CCT2F_STG0_lsb, value)

    @property
    def PA2G_MCT_CLASSB(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__PA2G_MCT_CLASSB_addr, self.__PA2G_MCT_CLASSB_msb, self.__PA2G_MCT_CLASSB_lsb)
    @PA2G_MCT_CLASSB.setter
    def PA2G_MCT_CLASSB(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__PA2G_MCT_CLASSB_addr, self.__PA2G_MCT_CLASSB_msb, self.__PA2G_MCT_CLASSB_lsb, value)

    @property
    def PA2G_RCT_STG2(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__PA2G_RCT_STG2_addr, self.__PA2G_RCT_STG2_msb, self.__PA2G_RCT_STG2_lsb)
    @PA2G_RCT_STG2.setter
    def PA2G_RCT_STG2(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__PA2G_RCT_STG2_addr, self.__PA2G_RCT_STG2_msb, self.__PA2G_RCT_STG2_lsb, value)

    @property
    def PA2G_STG1_SEL_ICGM(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__PA2G_STG1_SEL_ICGM_addr, self.__PA2G_STG1_SEL_ICGM_msb, self.__PA2G_STG1_SEL_ICGM_lsb)
    @PA2G_STG1_SEL_ICGM.setter
    def PA2G_STG1_SEL_ICGM(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__PA2G_STG1_SEL_ICGM_addr, self.__PA2G_STG1_SEL_ICGM_msb, self.__PA2G_STG1_SEL_ICGM_lsb, value)

    @property
    def PA2G_STG1_SEL_ICGM_N(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__PA2G_STG1_SEL_ICGM_N_addr, self.__PA2G_STG1_SEL_ICGM_N_msb, self.__PA2G_STG1_SEL_ICGM_N_lsb)
    @PA2G_STG1_SEL_ICGM_N.setter
    def PA2G_STG1_SEL_ICGM_N(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__PA2G_STG1_SEL_ICGM_N_addr, self.__PA2G_STG1_SEL_ICGM_N_msb, self.__PA2G_STG1_SEL_ICGM_N_lsb, value)

    @property
    def PA2G_VCT_CSC_STG0(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__PA2G_VCT_CSC_STG0_addr, self.__PA2G_VCT_CSC_STG0_msb, self.__PA2G_VCT_CSC_STG0_lsb)
    @PA2G_VCT_CSC_STG0.setter
    def PA2G_VCT_CSC_STG0(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__PA2G_VCT_CSC_STG0_addr, self.__PA2G_VCT_CSC_STG0_msb, self.__PA2G_VCT_CSC_STG0_lsb, value)

    @property
    def PA2G_VCT_CSC_STG1(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__PA2G_VCT_CSC_STG1_addr, self.__PA2G_VCT_CSC_STG1_msb, self.__PA2G_VCT_CSC_STG1_lsb)
    @PA2G_VCT_CSC_STG1.setter
    def PA2G_VCT_CSC_STG1(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__PA2G_VCT_CSC_STG1_addr, self.__PA2G_VCT_CSC_STG1_msb, self.__PA2G_VCT_CSC_STG1_lsb, value)

    @property
    def PA2G_VCT_CSC_STG2(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__PA2G_VCT_CSC_STG2_addr, self.__PA2G_VCT_CSC_STG2_msb, self.__PA2G_VCT_CSC_STG2_lsb)
    @PA2G_VCT_CSC_STG2.setter
    def PA2G_VCT_CSC_STG2(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__PA2G_VCT_CSC_STG2_addr, self.__PA2G_VCT_CSC_STG2_msb, self.__PA2G_VCT_CSC_STG2_lsb, value)

    @property
    def PA2G_PKDET_EN(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__PA2G_PKDET_EN_addr, self.__PA2G_PKDET_EN_msb, self.__PA2G_PKDET_EN_lsb)
    @PA2G_PKDET_EN.setter
    def PA2G_PKDET_EN(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__PA2G_PKDET_EN_addr, self.__PA2G_PKDET_EN_msb, self.__PA2G_PKDET_EN_lsb, value)

    @property
    def TR(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__TR_addr, self.__TR_msb, self.__TR_lsb)
    @TR.setter
    def TR(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__TR_addr, self.__TR_msb, self.__TR_lsb, value)

    @property
    def TE_PA2G(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__TE_PA2G_addr, self.__TE_PA2G_msb, self.__TE_PA2G_lsb)
    @TE_PA2G.setter
    def TE_PA2G(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__TE_PA2G_addr, self.__TE_PA2G_msb, self.__TE_PA2G_lsb, value)

    @property
    def LB_EN(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__LB_EN_addr, self.__LB_EN_msb, self.__LB_EN_lsb)
    @LB_EN.setter
    def LB_EN(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__LB_EN_addr, self.__LB_EN_msb, self.__LB_EN_lsb, value)

    @property
    def LB_EN_IQ(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__LB_EN_IQ_addr, self.__LB_EN_IQ_msb, self.__LB_EN_IQ_lsb)
    @LB_EN_IQ.setter
    def LB_EN_IQ(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__LB_EN_IQ_addr, self.__LB_EN_IQ_msb, self.__LB_EN_IQ_lsb, value)

    @property
    def LB_GCT(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__LB_GCT_addr, self.__LB_GCT_msb, self.__LB_GCT_lsb)
    @LB_GCT.setter
    def LB_GCT(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__LB_GCT_addr, self.__LB_GCT_msb, self.__LB_GCT_lsb, value)

    @property
    def TE_PWDET(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__TE_PWDET_addr, self.__TE_PWDET_msb, self.__TE_PWDET_lsb)
    @TE_PWDET.setter
    def TE_PWDET(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__TE_PWDET_addr, self.__TE_PWDET_msb, self.__TE_PWDET_lsb, value)

    @property
    def PWDET_VTH_TUNE(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__PWDET_VTH_TUNE_addr, self.__PWDET_VTH_TUNE_msb, self.__PWDET_VTH_TUNE_lsb)
    @PWDET_VTH_TUNE.setter
    def PWDET_VTH_TUNE(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__PWDET_VTH_TUNE_addr, self.__PWDET_VTH_TUNE_msb, self.__PWDET_VTH_TUNE_lsb, value)

    @property
    def SPARE_TX(self):
        return self.__I2C.i2c_rdm(self.__base , self.__hostid ,self.__SPARE_TX_addr, self.__SPARE_TX_msb, self.__SPARE_TX_lsb)
    @SPARE_TX.setter
    def SPARE_TX(self, value):
        return self.__I2C.i2c_wrm(self.__base , self.__hostid ,self.__SPARE_TX_addr, self.__SPARE_TX_msb, self.__SPARE_TX_lsb, value)
