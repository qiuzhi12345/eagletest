from hal.common import *
from hal.hwregister.hwreg.CHIP72.addr_base import *
class GPIO(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.GPIO_BT_SELECT = GPIO_BT_SELECT(self.channel, self.chipv)
        self.GPIO_OUT = GPIO_OUT(self.channel, self.chipv)
        self.GPIO_OUT_W1TS = GPIO_OUT_W1TS(self.channel, self.chipv)
        self.GPIO_OUT_W1TC = GPIO_OUT_W1TC(self.channel, self.chipv)
        self.GPIO_OUT1 = GPIO_OUT1(self.channel, self.chipv)
        self.GPIO_OUT1_W1TS = GPIO_OUT1_W1TS(self.channel, self.chipv)
        self.GPIO_OUT1_W1TC = GPIO_OUT1_W1TC(self.channel, self.chipv)
        self.GPIO_SDIO_SELECT = GPIO_SDIO_SELECT(self.channel, self.chipv)
        self.GPIO_ENABLE = GPIO_ENABLE(self.channel, self.chipv)
        self.GPIO_ENABLE_W1TS = GPIO_ENABLE_W1TS(self.channel, self.chipv)
        self.GPIO_ENABLE_W1TC = GPIO_ENABLE_W1TC(self.channel, self.chipv)
        self.GPIO_ENABLE1 = GPIO_ENABLE1(self.channel, self.chipv)
        self.GPIO_ENABLE1_W1TS = GPIO_ENABLE1_W1TS(self.channel, self.chipv)
        self.GPIO_ENABLE1_W1TC = GPIO_ENABLE1_W1TC(self.channel, self.chipv)
        self.GPIO_STRAP = GPIO_STRAP(self.channel, self.chipv)
        self.GPIO_IN = GPIO_IN(self.channel, self.chipv)
        self.GPIO_IN1 = GPIO_IN1(self.channel, self.chipv)
        self.GPIO_STATUS = GPIO_STATUS(self.channel, self.chipv)
        self.GPIO_STATUS_W1TS = GPIO_STATUS_W1TS(self.channel, self.chipv)
        self.GPIO_STATUS_W1TC = GPIO_STATUS_W1TC(self.channel, self.chipv)
        self.GPIO_STATUS1 = GPIO_STATUS1(self.channel, self.chipv)
        self.GPIO_STATUS1_W1TS = GPIO_STATUS1_W1TS(self.channel, self.chipv)
        self.GPIO_STATUS1_W1TC = GPIO_STATUS1_W1TC(self.channel, self.chipv)
        self.GPIO_ACPU_INT = GPIO_ACPU_INT(self.channel, self.chipv)
        self.GPIO_ACPU_NMI_INT = GPIO_ACPU_NMI_INT(self.channel, self.chipv)
        self.GPIO_PCPU_INT = GPIO_PCPU_INT(self.channel, self.chipv)
        self.GPIO_PCPU_NMI_INT = GPIO_PCPU_NMI_INT(self.channel, self.chipv)
        self.GPIO_CPUSDIO_INT = GPIO_CPUSDIO_INT(self.channel, self.chipv)
        self.GPIO_ACPU_INT1 = GPIO_ACPU_INT1(self.channel, self.chipv)
        self.GPIO_ACPU_NMI_INT1 = GPIO_ACPU_NMI_INT1(self.channel, self.chipv)
        self.GPIO_PCPU_INT1 = GPIO_PCPU_INT1(self.channel, self.chipv)
        self.GPIO_PCPU_NMI_INT1 = GPIO_PCPU_NMI_INT1(self.channel, self.chipv)
        self.GPIO_CPUSDIO_INT1 = GPIO_CPUSDIO_INT1(self.channel, self.chipv)
        self.GPIO_PIN0 = GPIO_PIN0(self.channel, self.chipv)
        self.GPIO_PIN1 = GPIO_PIN1(self.channel, self.chipv)
        self.GPIO_PIN2 = GPIO_PIN2(self.channel, self.chipv)
        self.GPIO_PIN3 = GPIO_PIN3(self.channel, self.chipv)
        self.GPIO_PIN4 = GPIO_PIN4(self.channel, self.chipv)
        self.GPIO_PIN5 = GPIO_PIN5(self.channel, self.chipv)
        self.GPIO_PIN6 = GPIO_PIN6(self.channel, self.chipv)
        self.GPIO_PIN7 = GPIO_PIN7(self.channel, self.chipv)
        self.GPIO_PIN8 = GPIO_PIN8(self.channel, self.chipv)
        self.GPIO_PIN9 = GPIO_PIN9(self.channel, self.chipv)
        self.GPIO_PIN10 = GPIO_PIN10(self.channel, self.chipv)
        self.GPIO_PIN11 = GPIO_PIN11(self.channel, self.chipv)
        self.GPIO_PIN12 = GPIO_PIN12(self.channel, self.chipv)
        self.GPIO_PIN13 = GPIO_PIN13(self.channel, self.chipv)
        self.GPIO_PIN14 = GPIO_PIN14(self.channel, self.chipv)
        self.GPIO_PIN15 = GPIO_PIN15(self.channel, self.chipv)
        self.GPIO_PIN16 = GPIO_PIN16(self.channel, self.chipv)
        self.GPIO_PIN17 = GPIO_PIN17(self.channel, self.chipv)
        self.GPIO_PIN18 = GPIO_PIN18(self.channel, self.chipv)
        self.GPIO_PIN19 = GPIO_PIN19(self.channel, self.chipv)
        self.GPIO_PIN20 = GPIO_PIN20(self.channel, self.chipv)
        self.GPIO_PIN21 = GPIO_PIN21(self.channel, self.chipv)
        self.GPIO_PIN22 = GPIO_PIN22(self.channel, self.chipv)
        self.GPIO_PIN23 = GPIO_PIN23(self.channel, self.chipv)
        self.GPIO_PIN24 = GPIO_PIN24(self.channel, self.chipv)
        self.GPIO_PIN25 = GPIO_PIN25(self.channel, self.chipv)
        self.GPIO_PIN26 = GPIO_PIN26(self.channel, self.chipv)
        self.GPIO_PIN27 = GPIO_PIN27(self.channel, self.chipv)
        self.GPIO_PIN28 = GPIO_PIN28(self.channel, self.chipv)
        self.GPIO_PIN29 = GPIO_PIN29(self.channel, self.chipv)
        self.GPIO_PIN30 = GPIO_PIN30(self.channel, self.chipv)
        self.GPIO_PIN31 = GPIO_PIN31(self.channel, self.chipv)
        self.GPIO_PIN32 = GPIO_PIN32(self.channel, self.chipv)
        self.GPIO_PIN33 = GPIO_PIN33(self.channel, self.chipv)
        self.GPIO_PIN34 = GPIO_PIN34(self.channel, self.chipv)
        self.GPIO_PIN35 = GPIO_PIN35(self.channel, self.chipv)
        self.GPIO_PIN36 = GPIO_PIN36(self.channel, self.chipv)
        self.GPIO_PIN37 = GPIO_PIN37(self.channel, self.chipv)
        self.GPIO_PIN38 = GPIO_PIN38(self.channel, self.chipv)
        self.GPIO_PIN39 = GPIO_PIN39(self.channel, self.chipv)
        self.cali_conf = cali_conf(self.channel, self.chipv)
        self.cali_data = cali_data(self.channel, self.chipv)
        self.GPIO_FUNC0_IN_SEL_CFG = GPIO_FUNC0_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC1_IN_SEL_CFG = GPIO_FUNC1_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC2_IN_SEL_CFG = GPIO_FUNC2_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC3_IN_SEL_CFG = GPIO_FUNC3_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC4_IN_SEL_CFG = GPIO_FUNC4_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC5_IN_SEL_CFG = GPIO_FUNC5_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC6_IN_SEL_CFG = GPIO_FUNC6_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC7_IN_SEL_CFG = GPIO_FUNC7_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC8_IN_SEL_CFG = GPIO_FUNC8_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC9_IN_SEL_CFG = GPIO_FUNC9_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC10_IN_SEL_CFG = GPIO_FUNC10_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC11_IN_SEL_CFG = GPIO_FUNC11_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC12_IN_SEL_CFG = GPIO_FUNC12_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC13_IN_SEL_CFG = GPIO_FUNC13_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC14_IN_SEL_CFG = GPIO_FUNC14_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC15_IN_SEL_CFG = GPIO_FUNC15_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC16_IN_SEL_CFG = GPIO_FUNC16_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC17_IN_SEL_CFG = GPIO_FUNC17_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC18_IN_SEL_CFG = GPIO_FUNC18_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC19_IN_SEL_CFG = GPIO_FUNC19_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC20_IN_SEL_CFG = GPIO_FUNC20_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC21_IN_SEL_CFG = GPIO_FUNC21_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC22_IN_SEL_CFG = GPIO_FUNC22_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC23_IN_SEL_CFG = GPIO_FUNC23_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC24_IN_SEL_CFG = GPIO_FUNC24_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC25_IN_SEL_CFG = GPIO_FUNC25_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC26_IN_SEL_CFG = GPIO_FUNC26_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC27_IN_SEL_CFG = GPIO_FUNC27_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC28_IN_SEL_CFG = GPIO_FUNC28_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC29_IN_SEL_CFG = GPIO_FUNC29_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC30_IN_SEL_CFG = GPIO_FUNC30_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC31_IN_SEL_CFG = GPIO_FUNC31_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC32_IN_SEL_CFG = GPIO_FUNC32_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC33_IN_SEL_CFG = GPIO_FUNC33_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC34_IN_SEL_CFG = GPIO_FUNC34_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC35_IN_SEL_CFG = GPIO_FUNC35_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC36_IN_SEL_CFG = GPIO_FUNC36_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC37_IN_SEL_CFG = GPIO_FUNC37_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC38_IN_SEL_CFG = GPIO_FUNC38_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC39_IN_SEL_CFG = GPIO_FUNC39_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC40_IN_SEL_CFG = GPIO_FUNC40_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC41_IN_SEL_CFG = GPIO_FUNC41_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC42_IN_SEL_CFG = GPIO_FUNC42_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC43_IN_SEL_CFG = GPIO_FUNC43_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC44_IN_SEL_CFG = GPIO_FUNC44_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC45_IN_SEL_CFG = GPIO_FUNC45_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC46_IN_SEL_CFG = GPIO_FUNC46_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC47_IN_SEL_CFG = GPIO_FUNC47_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC48_IN_SEL_CFG = GPIO_FUNC48_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC49_IN_SEL_CFG = GPIO_FUNC49_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC50_IN_SEL_CFG = GPIO_FUNC50_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC51_IN_SEL_CFG = GPIO_FUNC51_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC52_IN_SEL_CFG = GPIO_FUNC52_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC53_IN_SEL_CFG = GPIO_FUNC53_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC54_IN_SEL_CFG = GPIO_FUNC54_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC55_IN_SEL_CFG = GPIO_FUNC55_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC56_IN_SEL_CFG = GPIO_FUNC56_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC57_IN_SEL_CFG = GPIO_FUNC57_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC58_IN_SEL_CFG = GPIO_FUNC58_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC59_IN_SEL_CFG = GPIO_FUNC59_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC60_IN_SEL_CFG = GPIO_FUNC60_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC61_IN_SEL_CFG = GPIO_FUNC61_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC62_IN_SEL_CFG = GPIO_FUNC62_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC63_IN_SEL_CFG = GPIO_FUNC63_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC64_IN_SEL_CFG = GPIO_FUNC64_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC65_IN_SEL_CFG = GPIO_FUNC65_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC66_IN_SEL_CFG = GPIO_FUNC66_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC67_IN_SEL_CFG = GPIO_FUNC67_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC68_IN_SEL_CFG = GPIO_FUNC68_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC69_IN_SEL_CFG = GPIO_FUNC69_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC70_IN_SEL_CFG = GPIO_FUNC70_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC71_IN_SEL_CFG = GPIO_FUNC71_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC72_IN_SEL_CFG = GPIO_FUNC72_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC73_IN_SEL_CFG = GPIO_FUNC73_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC74_IN_SEL_CFG = GPIO_FUNC74_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC75_IN_SEL_CFG = GPIO_FUNC75_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC76_IN_SEL_CFG = GPIO_FUNC76_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC77_IN_SEL_CFG = GPIO_FUNC77_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC78_IN_SEL_CFG = GPIO_FUNC78_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC79_IN_SEL_CFG = GPIO_FUNC79_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC80_IN_SEL_CFG = GPIO_FUNC80_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC81_IN_SEL_CFG = GPIO_FUNC81_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC82_IN_SEL_CFG = GPIO_FUNC82_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC83_IN_SEL_CFG = GPIO_FUNC83_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC84_IN_SEL_CFG = GPIO_FUNC84_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC85_IN_SEL_CFG = GPIO_FUNC85_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC86_IN_SEL_CFG = GPIO_FUNC86_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC87_IN_SEL_CFG = GPIO_FUNC87_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC88_IN_SEL_CFG = GPIO_FUNC88_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC89_IN_SEL_CFG = GPIO_FUNC89_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC90_IN_SEL_CFG = GPIO_FUNC90_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC91_IN_SEL_CFG = GPIO_FUNC91_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC92_IN_SEL_CFG = GPIO_FUNC92_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC93_IN_SEL_CFG = GPIO_FUNC93_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC94_IN_SEL_CFG = GPIO_FUNC94_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC95_IN_SEL_CFG = GPIO_FUNC95_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC96_IN_SEL_CFG = GPIO_FUNC96_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC97_IN_SEL_CFG = GPIO_FUNC97_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC98_IN_SEL_CFG = GPIO_FUNC98_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC99_IN_SEL_CFG = GPIO_FUNC99_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC100_IN_SEL_CFG = GPIO_FUNC100_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC101_IN_SEL_CFG = GPIO_FUNC101_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC102_IN_SEL_CFG = GPIO_FUNC102_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC103_IN_SEL_CFG = GPIO_FUNC103_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC104_IN_SEL_CFG = GPIO_FUNC104_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC105_IN_SEL_CFG = GPIO_FUNC105_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC106_IN_SEL_CFG = GPIO_FUNC106_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC107_IN_SEL_CFG = GPIO_FUNC107_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC108_IN_SEL_CFG = GPIO_FUNC108_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC109_IN_SEL_CFG = GPIO_FUNC109_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC110_IN_SEL_CFG = GPIO_FUNC110_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC111_IN_SEL_CFG = GPIO_FUNC111_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC112_IN_SEL_CFG = GPIO_FUNC112_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC113_IN_SEL_CFG = GPIO_FUNC113_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC114_IN_SEL_CFG = GPIO_FUNC114_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC115_IN_SEL_CFG = GPIO_FUNC115_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC116_IN_SEL_CFG = GPIO_FUNC116_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC117_IN_SEL_CFG = GPIO_FUNC117_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC118_IN_SEL_CFG = GPIO_FUNC118_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC119_IN_SEL_CFG = GPIO_FUNC119_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC120_IN_SEL_CFG = GPIO_FUNC120_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC121_IN_SEL_CFG = GPIO_FUNC121_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC122_IN_SEL_CFG = GPIO_FUNC122_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC123_IN_SEL_CFG = GPIO_FUNC123_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC124_IN_SEL_CFG = GPIO_FUNC124_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC125_IN_SEL_CFG = GPIO_FUNC125_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC126_IN_SEL_CFG = GPIO_FUNC126_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC127_IN_SEL_CFG = GPIO_FUNC127_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC128_IN_SEL_CFG = GPIO_FUNC128_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC129_IN_SEL_CFG = GPIO_FUNC129_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC130_IN_SEL_CFG = GPIO_FUNC130_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC131_IN_SEL_CFG = GPIO_FUNC131_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC132_IN_SEL_CFG = GPIO_FUNC132_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC133_IN_SEL_CFG = GPIO_FUNC133_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC134_IN_SEL_CFG = GPIO_FUNC134_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC135_IN_SEL_CFG = GPIO_FUNC135_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC136_IN_SEL_CFG = GPIO_FUNC136_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC137_IN_SEL_CFG = GPIO_FUNC137_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC138_IN_SEL_CFG = GPIO_FUNC138_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC139_IN_SEL_CFG = GPIO_FUNC139_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC140_IN_SEL_CFG = GPIO_FUNC140_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC141_IN_SEL_CFG = GPIO_FUNC141_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC142_IN_SEL_CFG = GPIO_FUNC142_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC143_IN_SEL_CFG = GPIO_FUNC143_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC144_IN_SEL_CFG = GPIO_FUNC144_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC145_IN_SEL_CFG = GPIO_FUNC145_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC146_IN_SEL_CFG = GPIO_FUNC146_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC147_IN_SEL_CFG = GPIO_FUNC147_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC148_IN_SEL_CFG = GPIO_FUNC148_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC149_IN_SEL_CFG = GPIO_FUNC149_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC150_IN_SEL_CFG = GPIO_FUNC150_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC151_IN_SEL_CFG = GPIO_FUNC151_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC152_IN_SEL_CFG = GPIO_FUNC152_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC153_IN_SEL_CFG = GPIO_FUNC153_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC154_IN_SEL_CFG = GPIO_FUNC154_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC155_IN_SEL_CFG = GPIO_FUNC155_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC156_IN_SEL_CFG = GPIO_FUNC156_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC157_IN_SEL_CFG = GPIO_FUNC157_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC158_IN_SEL_CFG = GPIO_FUNC158_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC159_IN_SEL_CFG = GPIO_FUNC159_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC160_IN_SEL_CFG = GPIO_FUNC160_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC161_IN_SEL_CFG = GPIO_FUNC161_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC162_IN_SEL_CFG = GPIO_FUNC162_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC163_IN_SEL_CFG = GPIO_FUNC163_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC164_IN_SEL_CFG = GPIO_FUNC164_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC165_IN_SEL_CFG = GPIO_FUNC165_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC166_IN_SEL_CFG = GPIO_FUNC166_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC167_IN_SEL_CFG = GPIO_FUNC167_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC168_IN_SEL_CFG = GPIO_FUNC168_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC169_IN_SEL_CFG = GPIO_FUNC169_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC170_IN_SEL_CFG = GPIO_FUNC170_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC171_IN_SEL_CFG = GPIO_FUNC171_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC172_IN_SEL_CFG = GPIO_FUNC172_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC173_IN_SEL_CFG = GPIO_FUNC173_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC174_IN_SEL_CFG = GPIO_FUNC174_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC175_IN_SEL_CFG = GPIO_FUNC175_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC176_IN_SEL_CFG = GPIO_FUNC176_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC177_IN_SEL_CFG = GPIO_FUNC177_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC178_IN_SEL_CFG = GPIO_FUNC178_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC179_IN_SEL_CFG = GPIO_FUNC179_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC180_IN_SEL_CFG = GPIO_FUNC180_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC181_IN_SEL_CFG = GPIO_FUNC181_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC182_IN_SEL_CFG = GPIO_FUNC182_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC183_IN_SEL_CFG = GPIO_FUNC183_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC184_IN_SEL_CFG = GPIO_FUNC184_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC185_IN_SEL_CFG = GPIO_FUNC185_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC186_IN_SEL_CFG = GPIO_FUNC186_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC187_IN_SEL_CFG = GPIO_FUNC187_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC188_IN_SEL_CFG = GPIO_FUNC188_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC189_IN_SEL_CFG = GPIO_FUNC189_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC190_IN_SEL_CFG = GPIO_FUNC190_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC191_IN_SEL_CFG = GPIO_FUNC191_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC192_IN_SEL_CFG = GPIO_FUNC192_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC193_IN_SEL_CFG = GPIO_FUNC193_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC194_IN_SEL_CFG = GPIO_FUNC194_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC195_IN_SEL_CFG = GPIO_FUNC195_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC196_IN_SEL_CFG = GPIO_FUNC196_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC197_IN_SEL_CFG = GPIO_FUNC197_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC198_IN_SEL_CFG = GPIO_FUNC198_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC199_IN_SEL_CFG = GPIO_FUNC199_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC200_IN_SEL_CFG = GPIO_FUNC200_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC201_IN_SEL_CFG = GPIO_FUNC201_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC202_IN_SEL_CFG = GPIO_FUNC202_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC203_IN_SEL_CFG = GPIO_FUNC203_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC204_IN_SEL_CFG = GPIO_FUNC204_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC205_IN_SEL_CFG = GPIO_FUNC205_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC206_IN_SEL_CFG = GPIO_FUNC206_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC207_IN_SEL_CFG = GPIO_FUNC207_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC208_IN_SEL_CFG = GPIO_FUNC208_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC209_IN_SEL_CFG = GPIO_FUNC209_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC210_IN_SEL_CFG = GPIO_FUNC210_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC211_IN_SEL_CFG = GPIO_FUNC211_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC212_IN_SEL_CFG = GPIO_FUNC212_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC213_IN_SEL_CFG = GPIO_FUNC213_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC214_IN_SEL_CFG = GPIO_FUNC214_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC215_IN_SEL_CFG = GPIO_FUNC215_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC216_IN_SEL_CFG = GPIO_FUNC216_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC217_IN_SEL_CFG = GPIO_FUNC217_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC218_IN_SEL_CFG = GPIO_FUNC218_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC219_IN_SEL_CFG = GPIO_FUNC219_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC220_IN_SEL_CFG = GPIO_FUNC220_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC221_IN_SEL_CFG = GPIO_FUNC221_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC222_IN_SEL_CFG = GPIO_FUNC222_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC223_IN_SEL_CFG = GPIO_FUNC223_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC224_IN_SEL_CFG = GPIO_FUNC224_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC225_IN_SEL_CFG = GPIO_FUNC225_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC226_IN_SEL_CFG = GPIO_FUNC226_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC227_IN_SEL_CFG = GPIO_FUNC227_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC228_IN_SEL_CFG = GPIO_FUNC228_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC229_IN_SEL_CFG = GPIO_FUNC229_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC230_IN_SEL_CFG = GPIO_FUNC230_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC231_IN_SEL_CFG = GPIO_FUNC231_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC232_IN_SEL_CFG = GPIO_FUNC232_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC233_IN_SEL_CFG = GPIO_FUNC233_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC234_IN_SEL_CFG = GPIO_FUNC234_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC235_IN_SEL_CFG = GPIO_FUNC235_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC236_IN_SEL_CFG = GPIO_FUNC236_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC237_IN_SEL_CFG = GPIO_FUNC237_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC238_IN_SEL_CFG = GPIO_FUNC238_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC239_IN_SEL_CFG = GPIO_FUNC239_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC240_IN_SEL_CFG = GPIO_FUNC240_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC241_IN_SEL_CFG = GPIO_FUNC241_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC242_IN_SEL_CFG = GPIO_FUNC242_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC243_IN_SEL_CFG = GPIO_FUNC243_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC244_IN_SEL_CFG = GPIO_FUNC244_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC245_IN_SEL_CFG = GPIO_FUNC245_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC246_IN_SEL_CFG = GPIO_FUNC246_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC247_IN_SEL_CFG = GPIO_FUNC247_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC248_IN_SEL_CFG = GPIO_FUNC248_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC249_IN_SEL_CFG = GPIO_FUNC249_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC250_IN_SEL_CFG = GPIO_FUNC250_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC251_IN_SEL_CFG = GPIO_FUNC251_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC252_IN_SEL_CFG = GPIO_FUNC252_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC253_IN_SEL_CFG = GPIO_FUNC253_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC254_IN_SEL_CFG = GPIO_FUNC254_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC255_IN_SEL_CFG = GPIO_FUNC255_IN_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC0_OUT_SEL_CFG = GPIO_FUNC0_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC1_OUT_SEL_CFG = GPIO_FUNC1_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC2_OUT_SEL_CFG = GPIO_FUNC2_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC3_OUT_SEL_CFG = GPIO_FUNC3_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC4_OUT_SEL_CFG = GPIO_FUNC4_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC5_OUT_SEL_CFG = GPIO_FUNC5_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC6_OUT_SEL_CFG = GPIO_FUNC6_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC7_OUT_SEL_CFG = GPIO_FUNC7_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC8_OUT_SEL_CFG = GPIO_FUNC8_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC9_OUT_SEL_CFG = GPIO_FUNC9_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC10_OUT_SEL_CFG = GPIO_FUNC10_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC11_OUT_SEL_CFG = GPIO_FUNC11_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC12_OUT_SEL_CFG = GPIO_FUNC12_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC13_OUT_SEL_CFG = GPIO_FUNC13_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC14_OUT_SEL_CFG = GPIO_FUNC14_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC15_OUT_SEL_CFG = GPIO_FUNC15_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC16_OUT_SEL_CFG = GPIO_FUNC16_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC17_OUT_SEL_CFG = GPIO_FUNC17_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC18_OUT_SEL_CFG = GPIO_FUNC18_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC19_OUT_SEL_CFG = GPIO_FUNC19_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC20_OUT_SEL_CFG = GPIO_FUNC20_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC21_OUT_SEL_CFG = GPIO_FUNC21_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC22_OUT_SEL_CFG = GPIO_FUNC22_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC23_OUT_SEL_CFG = GPIO_FUNC23_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC24_OUT_SEL_CFG = GPIO_FUNC24_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC25_OUT_SEL_CFG = GPIO_FUNC25_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC26_OUT_SEL_CFG = GPIO_FUNC26_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC27_OUT_SEL_CFG = GPIO_FUNC27_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC28_OUT_SEL_CFG = GPIO_FUNC28_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC29_OUT_SEL_CFG = GPIO_FUNC29_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC30_OUT_SEL_CFG = GPIO_FUNC30_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC31_OUT_SEL_CFG = GPIO_FUNC31_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC32_OUT_SEL_CFG = GPIO_FUNC32_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC33_OUT_SEL_CFG = GPIO_FUNC33_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC34_OUT_SEL_CFG = GPIO_FUNC34_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC35_OUT_SEL_CFG = GPIO_FUNC35_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC36_OUT_SEL_CFG = GPIO_FUNC36_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC37_OUT_SEL_CFG = GPIO_FUNC37_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC38_OUT_SEL_CFG = GPIO_FUNC38_OUT_SEL_CFG(self.channel, self.chipv)
        self.GPIO_FUNC39_OUT_SEL_CFG = GPIO_FUNC39_OUT_SEL_CFG(self.channel, self.chipv)
class GPIO_BT_SELECT(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x0
        self.__GPIO_BT_SEL_lsb = 0
        self.__GPIO_BT_SEL_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_BT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_BT_SEL_msb, self.__GPIO_BT_SEL_lsb)
    @GPIO_BT_SEL.setter
    def GPIO_BT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_BT_SEL_msb, self.__GPIO_BT_SEL_lsb, value)
class GPIO_OUT(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x4
        self.__GPIO_OUT_DATA_lsb = 0
        self.__GPIO_OUT_DATA_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_OUT_DATA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_OUT_DATA_msb, self.__GPIO_OUT_DATA_lsb)
    @GPIO_OUT_DATA.setter
    def GPIO_OUT_DATA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_OUT_DATA_msb, self.__GPIO_OUT_DATA_lsb, value)
class GPIO_OUT_W1TS(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x8
        self.__GPIO_OUT_DATA_lsb = 0
        self.__GPIO_OUT_DATA_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_OUT_DATA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_OUT_DATA_msb, self.__GPIO_OUT_DATA_lsb)
    @GPIO_OUT_DATA.setter
    def GPIO_OUT_DATA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_OUT_DATA_msb, self.__GPIO_OUT_DATA_lsb, value)
class GPIO_OUT_W1TC(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0xc
        self.__GPIO_OUT_DATA_lsb = 0
        self.__GPIO_OUT_DATA_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_OUT_DATA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_OUT_DATA_msb, self.__GPIO_OUT_DATA_lsb)
    @GPIO_OUT_DATA.setter
    def GPIO_OUT_DATA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_OUT_DATA_msb, self.__GPIO_OUT_DATA_lsb, value)
class GPIO_OUT1(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x10
        self.__GPIO_OUT_DATA_lsb = 32
        self.__GPIO_OUT_DATA_msb = 39
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_OUT_DATA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_OUT_DATA_msb, self.__GPIO_OUT_DATA_lsb)
    @GPIO_OUT_DATA.setter
    def GPIO_OUT_DATA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_OUT_DATA_msb, self.__GPIO_OUT_DATA_lsb, value)
class GPIO_OUT1_W1TS(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x14
        self.__GPIO_OUT_DATA_lsb = 32
        self.__GPIO_OUT_DATA_msb = 39
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_OUT_DATA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_OUT_DATA_msb, self.__GPIO_OUT_DATA_lsb)
    @GPIO_OUT_DATA.setter
    def GPIO_OUT_DATA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_OUT_DATA_msb, self.__GPIO_OUT_DATA_lsb, value)
class GPIO_OUT1_W1TC(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x18
        self.__GPIO_OUT_DATA_lsb = 32
        self.__GPIO_OUT_DATA_msb = 39
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_OUT_DATA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_OUT_DATA_msb, self.__GPIO_OUT_DATA_lsb)
    @GPIO_OUT_DATA.setter
    def GPIO_OUT_DATA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_OUT_DATA_msb, self.__GPIO_OUT_DATA_lsb, value)
class GPIO_SDIO_SELECT(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x1c
        self.__GPIO_SDIO_SEL_lsb = 0
        self.__GPIO_SDIO_SEL_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SDIO_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SDIO_SEL_msb, self.__GPIO_SDIO_SEL_lsb)
    @GPIO_SDIO_SEL.setter
    def GPIO_SDIO_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SDIO_SEL_msb, self.__GPIO_SDIO_SEL_lsb, value)
class GPIO_ENABLE(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x20
        self.__GPIO_ENABLE_DATA_lsb = 0
        self.__GPIO_ENABLE_DATA_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_ENABLE_DATA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_ENABLE_DATA_msb, self.__GPIO_ENABLE_DATA_lsb)
    @GPIO_ENABLE_DATA.setter
    def GPIO_ENABLE_DATA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_ENABLE_DATA_msb, self.__GPIO_ENABLE_DATA_lsb, value)
class GPIO_ENABLE_W1TS(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x24
        self.__GPIO_ENABLE_DATA_lsb = 0
        self.__GPIO_ENABLE_DATA_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_ENABLE_DATA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_ENABLE_DATA_msb, self.__GPIO_ENABLE_DATA_lsb)
    @GPIO_ENABLE_DATA.setter
    def GPIO_ENABLE_DATA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_ENABLE_DATA_msb, self.__GPIO_ENABLE_DATA_lsb, value)
class GPIO_ENABLE_W1TC(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x28
        self.__GPIO_ENABLE_DATA_lsb = 0
        self.__GPIO_ENABLE_DATA_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_ENABLE_DATA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_ENABLE_DATA_msb, self.__GPIO_ENABLE_DATA_lsb)
    @GPIO_ENABLE_DATA.setter
    def GPIO_ENABLE_DATA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_ENABLE_DATA_msb, self.__GPIO_ENABLE_DATA_lsb, value)
class GPIO_ENABLE1(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x2c
        self.__GPIO_ENABLE_DATA_lsb = 32
        self.__GPIO_ENABLE_DATA_msb = 39
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_ENABLE_DATA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_ENABLE_DATA_msb, self.__GPIO_ENABLE_DATA_lsb)
    @GPIO_ENABLE_DATA.setter
    def GPIO_ENABLE_DATA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_ENABLE_DATA_msb, self.__GPIO_ENABLE_DATA_lsb, value)
class GPIO_ENABLE1_W1TS(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x30
        self.__GPIO_ENABLE_DATA_lsb = 32
        self.__GPIO_ENABLE_DATA_msb = 39
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_ENABLE_DATA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_ENABLE_DATA_msb, self.__GPIO_ENABLE_DATA_lsb)
    @GPIO_ENABLE_DATA.setter
    def GPIO_ENABLE_DATA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_ENABLE_DATA_msb, self.__GPIO_ENABLE_DATA_lsb, value)
class GPIO_ENABLE1_W1TC(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x34
        self.__GPIO_ENABLE_DATA_lsb = 32
        self.__GPIO_ENABLE_DATA_msb = 39
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_ENABLE_DATA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_ENABLE_DATA_msb, self.__GPIO_ENABLE_DATA_lsb)
    @GPIO_ENABLE_DATA.setter
    def GPIO_ENABLE_DATA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_ENABLE_DATA_msb, self.__GPIO_ENABLE_DATA_lsb, value)
class GPIO_STRAP(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x38
        self.__GPIO_STRAPPING_lsb = 0
        self.__GPIO_STRAPPING_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_STRAPPING(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_STRAPPING_msb, self.__GPIO_STRAPPING_lsb)
    @GPIO_STRAPPING.setter
    def GPIO_STRAPPING(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_STRAPPING_msb, self.__GPIO_STRAPPING_lsb, value)
class GPIO_IN(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x3c
        self.__GPIO_IN_DATA_next_lsb = 0
        self.__GPIO_IN_DATA_next_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_IN_DATA_next(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_IN_DATA_next_msb, self.__GPIO_IN_DATA_next_lsb)
    @GPIO_IN_DATA_next.setter
    def GPIO_IN_DATA_next(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_IN_DATA_next_msb, self.__GPIO_IN_DATA_next_lsb, value)
class GPIO_IN1(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x40
        self.__GPIO_IN_DATA_next_lsb = 32
        self.__GPIO_IN_DATA_next_msb = 39
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_IN_DATA_next(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_IN_DATA_next_msb, self.__GPIO_IN_DATA_next_lsb)
    @GPIO_IN_DATA_next.setter
    def GPIO_IN_DATA_next(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_IN_DATA_next_msb, self.__GPIO_IN_DATA_next_lsb, value)
class GPIO_STATUS(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x44
        self.__GPIO_STATUS_INTERRUPT_lsb = 0
        self.__GPIO_STATUS_INTERRUPT_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_STATUS_INTERRUPT(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_STATUS_INTERRUPT_msb, self.__GPIO_STATUS_INTERRUPT_lsb)
    @GPIO_STATUS_INTERRUPT.setter
    def GPIO_STATUS_INTERRUPT(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_STATUS_INTERRUPT_msb, self.__GPIO_STATUS_INTERRUPT_lsb, value)
class GPIO_STATUS_W1TS(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x48
        self.__GPIO_STATUS_INTERRUPT_lsb = 0
        self.__GPIO_STATUS_INTERRUPT_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_STATUS_INTERRUPT(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_STATUS_INTERRUPT_msb, self.__GPIO_STATUS_INTERRUPT_lsb)
    @GPIO_STATUS_INTERRUPT.setter
    def GPIO_STATUS_INTERRUPT(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_STATUS_INTERRUPT_msb, self.__GPIO_STATUS_INTERRUPT_lsb, value)
class GPIO_STATUS_W1TC(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x4c
        self.__GPIO_STATUS_INTERRUPT_lsb = 0
        self.__GPIO_STATUS_INTERRUPT_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_STATUS_INTERRUPT(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_STATUS_INTERRUPT_msb, self.__GPIO_STATUS_INTERRUPT_lsb)
    @GPIO_STATUS_INTERRUPT.setter
    def GPIO_STATUS_INTERRUPT(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_STATUS_INTERRUPT_msb, self.__GPIO_STATUS_INTERRUPT_lsb, value)
class GPIO_STATUS1(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x50
        self.__GPIO_STATUS_INTERRUPT_lsb = 32
        self.__GPIO_STATUS_INTERRUPT_msb = 39
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_STATUS_INTERRUPT(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_STATUS_INTERRUPT_msb, self.__GPIO_STATUS_INTERRUPT_lsb)
    @GPIO_STATUS_INTERRUPT.setter
    def GPIO_STATUS_INTERRUPT(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_STATUS_INTERRUPT_msb, self.__GPIO_STATUS_INTERRUPT_lsb, value)
class GPIO_STATUS1_W1TS(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x54
        self.__GPIO_STATUS_INTERRUPT_lsb = 32
        self.__GPIO_STATUS_INTERRUPT_msb = 39
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_STATUS_INTERRUPT(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_STATUS_INTERRUPT_msb, self.__GPIO_STATUS_INTERRUPT_lsb)
    @GPIO_STATUS_INTERRUPT.setter
    def GPIO_STATUS_INTERRUPT(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_STATUS_INTERRUPT_msb, self.__GPIO_STATUS_INTERRUPT_lsb, value)
class GPIO_STATUS1_W1TC(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x58
        self.__GPIO_STATUS_INTERRUPT_lsb = 32
        self.__GPIO_STATUS_INTERRUPT_msb = 39
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_STATUS_INTERRUPT(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_STATUS_INTERRUPT_msb, self.__GPIO_STATUS_INTERRUPT_lsb)
    @GPIO_STATUS_INTERRUPT.setter
    def GPIO_STATUS_INTERRUPT(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_STATUS_INTERRUPT_msb, self.__GPIO_STATUS_INTERRUPT_lsb, value)
class GPIO_ACPU_INT(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x60
        self.__GPIO_APPCPU_INT_lsb = 0
        self.__GPIO_APPCPU_INT_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_APPCPU_INT(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_APPCPU_INT_msb, self.__GPIO_APPCPU_INT_lsb)
    @GPIO_APPCPU_INT.setter
    def GPIO_APPCPU_INT(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_APPCPU_INT_msb, self.__GPIO_APPCPU_INT_lsb, value)
class GPIO_ACPU_NMI_INT(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x64
        self.__GPIO_APPCPU_NMI_INT_lsb = 0
        self.__GPIO_APPCPU_NMI_INT_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_APPCPU_NMI_INT(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_APPCPU_NMI_INT_msb, self.__GPIO_APPCPU_NMI_INT_lsb)
    @GPIO_APPCPU_NMI_INT.setter
    def GPIO_APPCPU_NMI_INT(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_APPCPU_NMI_INT_msb, self.__GPIO_APPCPU_NMI_INT_lsb, value)
class GPIO_PCPU_INT(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x68
        self.__GPIO_PROCPU_INT_lsb = 0
        self.__GPIO_PROCPU_INT_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PROCPU_INT(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PROCPU_INT_msb, self.__GPIO_PROCPU_INT_lsb)
    @GPIO_PROCPU_INT.setter
    def GPIO_PROCPU_INT(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PROCPU_INT_msb, self.__GPIO_PROCPU_INT_lsb, value)
class GPIO_PCPU_NMI_INT(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x6c
        self.__GPIO_PROCPU_NMI_INT_lsb = 0
        self.__GPIO_PROCPU_NMI_INT_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PROCPU_NMI_INT(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PROCPU_NMI_INT_msb, self.__GPIO_PROCPU_NMI_INT_lsb)
    @GPIO_PROCPU_NMI_INT.setter
    def GPIO_PROCPU_NMI_INT(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PROCPU_NMI_INT_msb, self.__GPIO_PROCPU_NMI_INT_lsb, value)
class GPIO_CPUSDIO_INT(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x70
        self.__GPIO_SDIO_INT_lsb = 0
        self.__GPIO_SDIO_INT_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SDIO_INT(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SDIO_INT_msb, self.__GPIO_SDIO_INT_lsb)
    @GPIO_SDIO_INT.setter
    def GPIO_SDIO_INT(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SDIO_INT_msb, self.__GPIO_SDIO_INT_lsb, value)
class GPIO_ACPU_INT1(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x74
        self.__GPIO_APPCPU_INT_lsb = 32
        self.__GPIO_APPCPU_INT_msb = 39
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_APPCPU_INT(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_APPCPU_INT_msb, self.__GPIO_APPCPU_INT_lsb)
    @GPIO_APPCPU_INT.setter
    def GPIO_APPCPU_INT(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_APPCPU_INT_msb, self.__GPIO_APPCPU_INT_lsb, value)
class GPIO_ACPU_NMI_INT1(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x78
        self.__GPIO_APPCPU_NMI_INT_lsb = 32
        self.__GPIO_APPCPU_NMI_INT_msb = 39
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_APPCPU_NMI_INT(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_APPCPU_NMI_INT_msb, self.__GPIO_APPCPU_NMI_INT_lsb)
    @GPIO_APPCPU_NMI_INT.setter
    def GPIO_APPCPU_NMI_INT(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_APPCPU_NMI_INT_msb, self.__GPIO_APPCPU_NMI_INT_lsb, value)
class GPIO_PCPU_INT1(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x7c
        self.__GPIO_PROCPU_INT_lsb = 32
        self.__GPIO_PROCPU_INT_msb = 39
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PROCPU_INT(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PROCPU_INT_msb, self.__GPIO_PROCPU_INT_lsb)
    @GPIO_PROCPU_INT.setter
    def GPIO_PROCPU_INT(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PROCPU_INT_msb, self.__GPIO_PROCPU_INT_lsb, value)
class GPIO_PCPU_NMI_INT1(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x80
        self.__GPIO_PROCPU_NMI_INT_lsb = 32
        self.__GPIO_PROCPU_NMI_INT_msb = 39
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PROCPU_NMI_INT(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PROCPU_NMI_INT_msb, self.__GPIO_PROCPU_NMI_INT_lsb)
    @GPIO_PROCPU_NMI_INT.setter
    def GPIO_PROCPU_NMI_INT(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PROCPU_NMI_INT_msb, self.__GPIO_PROCPU_NMI_INT_lsb, value)
class GPIO_CPUSDIO_INT1(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x84
        self.__GPIO_SDIO_INT_lsb = 32
        self.__GPIO_SDIO_INT_msb = 39
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SDIO_INT(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SDIO_INT_msb, self.__GPIO_SDIO_INT_lsb)
    @GPIO_SDIO_INT.setter
    def GPIO_SDIO_INT(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SDIO_INT_msb, self.__GPIO_SDIO_INT_lsb, value)
class GPIO_PIN0(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x88
        self.__GPIO_PIN0_INT_ENA_lsb = 13
        self.__GPIO_PIN0_INT_ENA_msb = 17
        self.__GPIO_PIN0_CONFIG_lsb = 11
        self.__GPIO_PIN0_CONFIG_msb = 12
        self.__GPIO_PIN0_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN0_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN0_INT_TYPE_lsb = 7
        self.__GPIO_PIN0_INT_TYPE_msb = 9
        self.__GPIO_PIN0_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN0_PAD_DRIVER_msb = 2
        self.__GPIO_PIN0_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN0_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN0_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN0_INT_ENA_msb, self.__GPIO_PIN0_INT_ENA_lsb)
    @GPIO_PIN0_INT_ENA.setter
    def GPIO_PIN0_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN0_INT_ENA_msb, self.__GPIO_PIN0_INT_ENA_lsb, value)

    @property
    def GPIO_PIN0_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN0_CONFIG_msb, self.__GPIO_PIN0_CONFIG_lsb)
    @GPIO_PIN0_CONFIG.setter
    def GPIO_PIN0_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN0_CONFIG_msb, self.__GPIO_PIN0_CONFIG_lsb, value)

    @property
    def GPIO_PIN0_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN0_WAKEUP_ENABLE_msb, self.__GPIO_PIN0_WAKEUP_ENABLE_lsb)
    @GPIO_PIN0_WAKEUP_ENABLE.setter
    def GPIO_PIN0_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN0_WAKEUP_ENABLE_msb, self.__GPIO_PIN0_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN0_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN0_INT_TYPE_msb, self.__GPIO_PIN0_INT_TYPE_lsb)
    @GPIO_PIN0_INT_TYPE.setter
    def GPIO_PIN0_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN0_INT_TYPE_msb, self.__GPIO_PIN0_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN0_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN0_PAD_DRIVER_msb, self.__GPIO_PIN0_PAD_DRIVER_lsb)
    @GPIO_PIN0_PAD_DRIVER.setter
    def GPIO_PIN0_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN0_PAD_DRIVER_msb, self.__GPIO_PIN0_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN0_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN0_SYNC_BYPASS_msb, self.__GPIO_PIN0_SYNC_BYPASS_lsb)
    @GPIO_PIN0_SYNC_BYPASS.setter
    def GPIO_PIN0_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN0_SYNC_BYPASS_msb, self.__GPIO_PIN0_SYNC_BYPASS_lsb, value)
class GPIO_PIN1(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x8c
        self.__GPIO_PIN1_INT_ENA_lsb = 13
        self.__GPIO_PIN1_INT_ENA_msb = 17
        self.__GPIO_PIN1_CONFIG_lsb = 11
        self.__GPIO_PIN1_CONFIG_msb = 12
        self.__GPIO_PIN1_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN1_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN1_INT_TYPE_lsb = 7
        self.__GPIO_PIN1_INT_TYPE_msb = 9
        self.__GPIO_PIN1_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN1_PAD_DRIVER_msb = 2
        self.__GPIO_PIN1_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN1_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN1_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN1_INT_ENA_msb, self.__GPIO_PIN1_INT_ENA_lsb)
    @GPIO_PIN1_INT_ENA.setter
    def GPIO_PIN1_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN1_INT_ENA_msb, self.__GPIO_PIN1_INT_ENA_lsb, value)

    @property
    def GPIO_PIN1_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN1_CONFIG_msb, self.__GPIO_PIN1_CONFIG_lsb)
    @GPIO_PIN1_CONFIG.setter
    def GPIO_PIN1_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN1_CONFIG_msb, self.__GPIO_PIN1_CONFIG_lsb, value)

    @property
    def GPIO_PIN1_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN1_WAKEUP_ENABLE_msb, self.__GPIO_PIN1_WAKEUP_ENABLE_lsb)
    @GPIO_PIN1_WAKEUP_ENABLE.setter
    def GPIO_PIN1_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN1_WAKEUP_ENABLE_msb, self.__GPIO_PIN1_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN1_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN1_INT_TYPE_msb, self.__GPIO_PIN1_INT_TYPE_lsb)
    @GPIO_PIN1_INT_TYPE.setter
    def GPIO_PIN1_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN1_INT_TYPE_msb, self.__GPIO_PIN1_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN1_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN1_PAD_DRIVER_msb, self.__GPIO_PIN1_PAD_DRIVER_lsb)
    @GPIO_PIN1_PAD_DRIVER.setter
    def GPIO_PIN1_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN1_PAD_DRIVER_msb, self.__GPIO_PIN1_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN1_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN1_SYNC_BYPASS_msb, self.__GPIO_PIN1_SYNC_BYPASS_lsb)
    @GPIO_PIN1_SYNC_BYPASS.setter
    def GPIO_PIN1_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN1_SYNC_BYPASS_msb, self.__GPIO_PIN1_SYNC_BYPASS_lsb, value)
class GPIO_PIN2(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x90
        self.__GPIO_PIN2_INT_ENA_lsb = 13
        self.__GPIO_PIN2_INT_ENA_msb = 17
        self.__GPIO_PIN2_CONFIG_lsb = 11
        self.__GPIO_PIN2_CONFIG_msb = 12
        self.__GPIO_PIN2_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN2_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN2_INT_TYPE_lsb = 7
        self.__GPIO_PIN2_INT_TYPE_msb = 9
        self.__GPIO_PIN2_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN2_PAD_DRIVER_msb = 2
        self.__GPIO_PIN2_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN2_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN2_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN2_INT_ENA_msb, self.__GPIO_PIN2_INT_ENA_lsb)
    @GPIO_PIN2_INT_ENA.setter
    def GPIO_PIN2_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN2_INT_ENA_msb, self.__GPIO_PIN2_INT_ENA_lsb, value)

    @property
    def GPIO_PIN2_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN2_CONFIG_msb, self.__GPIO_PIN2_CONFIG_lsb)
    @GPIO_PIN2_CONFIG.setter
    def GPIO_PIN2_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN2_CONFIG_msb, self.__GPIO_PIN2_CONFIG_lsb, value)

    @property
    def GPIO_PIN2_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN2_WAKEUP_ENABLE_msb, self.__GPIO_PIN2_WAKEUP_ENABLE_lsb)
    @GPIO_PIN2_WAKEUP_ENABLE.setter
    def GPIO_PIN2_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN2_WAKEUP_ENABLE_msb, self.__GPIO_PIN2_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN2_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN2_INT_TYPE_msb, self.__GPIO_PIN2_INT_TYPE_lsb)
    @GPIO_PIN2_INT_TYPE.setter
    def GPIO_PIN2_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN2_INT_TYPE_msb, self.__GPIO_PIN2_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN2_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN2_PAD_DRIVER_msb, self.__GPIO_PIN2_PAD_DRIVER_lsb)
    @GPIO_PIN2_PAD_DRIVER.setter
    def GPIO_PIN2_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN2_PAD_DRIVER_msb, self.__GPIO_PIN2_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN2_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN2_SYNC_BYPASS_msb, self.__GPIO_PIN2_SYNC_BYPASS_lsb)
    @GPIO_PIN2_SYNC_BYPASS.setter
    def GPIO_PIN2_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN2_SYNC_BYPASS_msb, self.__GPIO_PIN2_SYNC_BYPASS_lsb, value)
class GPIO_PIN3(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x94
        self.__GPIO_PIN3_INT_ENA_lsb = 13
        self.__GPIO_PIN3_INT_ENA_msb = 17
        self.__GPIO_PIN3_CONFIG_lsb = 11
        self.__GPIO_PIN3_CONFIG_msb = 12
        self.__GPIO_PIN3_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN3_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN3_INT_TYPE_lsb = 7
        self.__GPIO_PIN3_INT_TYPE_msb = 9
        self.__GPIO_PIN3_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN3_PAD_DRIVER_msb = 2
        self.__GPIO_PIN3_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN3_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN3_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN3_INT_ENA_msb, self.__GPIO_PIN3_INT_ENA_lsb)
    @GPIO_PIN3_INT_ENA.setter
    def GPIO_PIN3_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN3_INT_ENA_msb, self.__GPIO_PIN3_INT_ENA_lsb, value)

    @property
    def GPIO_PIN3_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN3_CONFIG_msb, self.__GPIO_PIN3_CONFIG_lsb)
    @GPIO_PIN3_CONFIG.setter
    def GPIO_PIN3_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN3_CONFIG_msb, self.__GPIO_PIN3_CONFIG_lsb, value)

    @property
    def GPIO_PIN3_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN3_WAKEUP_ENABLE_msb, self.__GPIO_PIN3_WAKEUP_ENABLE_lsb)
    @GPIO_PIN3_WAKEUP_ENABLE.setter
    def GPIO_PIN3_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN3_WAKEUP_ENABLE_msb, self.__GPIO_PIN3_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN3_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN3_INT_TYPE_msb, self.__GPIO_PIN3_INT_TYPE_lsb)
    @GPIO_PIN3_INT_TYPE.setter
    def GPIO_PIN3_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN3_INT_TYPE_msb, self.__GPIO_PIN3_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN3_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN3_PAD_DRIVER_msb, self.__GPIO_PIN3_PAD_DRIVER_lsb)
    @GPIO_PIN3_PAD_DRIVER.setter
    def GPIO_PIN3_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN3_PAD_DRIVER_msb, self.__GPIO_PIN3_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN3_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN3_SYNC_BYPASS_msb, self.__GPIO_PIN3_SYNC_BYPASS_lsb)
    @GPIO_PIN3_SYNC_BYPASS.setter
    def GPIO_PIN3_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN3_SYNC_BYPASS_msb, self.__GPIO_PIN3_SYNC_BYPASS_lsb, value)
class GPIO_PIN4(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x98
        self.__GPIO_PIN4_INT_ENA_lsb = 13
        self.__GPIO_PIN4_INT_ENA_msb = 17
        self.__GPIO_PIN4_CONFIG_lsb = 11
        self.__GPIO_PIN4_CONFIG_msb = 12
        self.__GPIO_PIN4_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN4_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN4_INT_TYPE_lsb = 7
        self.__GPIO_PIN4_INT_TYPE_msb = 9
        self.__GPIO_PIN4_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN4_PAD_DRIVER_msb = 2
        self.__GPIO_PIN4_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN4_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN4_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN4_INT_ENA_msb, self.__GPIO_PIN4_INT_ENA_lsb)
    @GPIO_PIN4_INT_ENA.setter
    def GPIO_PIN4_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN4_INT_ENA_msb, self.__GPIO_PIN4_INT_ENA_lsb, value)

    @property
    def GPIO_PIN4_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN4_CONFIG_msb, self.__GPIO_PIN4_CONFIG_lsb)
    @GPIO_PIN4_CONFIG.setter
    def GPIO_PIN4_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN4_CONFIG_msb, self.__GPIO_PIN4_CONFIG_lsb, value)

    @property
    def GPIO_PIN4_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN4_WAKEUP_ENABLE_msb, self.__GPIO_PIN4_WAKEUP_ENABLE_lsb)
    @GPIO_PIN4_WAKEUP_ENABLE.setter
    def GPIO_PIN4_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN4_WAKEUP_ENABLE_msb, self.__GPIO_PIN4_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN4_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN4_INT_TYPE_msb, self.__GPIO_PIN4_INT_TYPE_lsb)
    @GPIO_PIN4_INT_TYPE.setter
    def GPIO_PIN4_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN4_INT_TYPE_msb, self.__GPIO_PIN4_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN4_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN4_PAD_DRIVER_msb, self.__GPIO_PIN4_PAD_DRIVER_lsb)
    @GPIO_PIN4_PAD_DRIVER.setter
    def GPIO_PIN4_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN4_PAD_DRIVER_msb, self.__GPIO_PIN4_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN4_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN4_SYNC_BYPASS_msb, self.__GPIO_PIN4_SYNC_BYPASS_lsb)
    @GPIO_PIN4_SYNC_BYPASS.setter
    def GPIO_PIN4_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN4_SYNC_BYPASS_msb, self.__GPIO_PIN4_SYNC_BYPASS_lsb, value)
class GPIO_PIN5(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x9c
        self.__GPIO_PIN5_INT_ENA_lsb = 13
        self.__GPIO_PIN5_INT_ENA_msb = 17
        self.__GPIO_PIN5_CONFIG_lsb = 11
        self.__GPIO_PIN5_CONFIG_msb = 12
        self.__GPIO_PIN5_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN5_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN5_INT_TYPE_lsb = 7
        self.__GPIO_PIN5_INT_TYPE_msb = 9
        self.__GPIO_PIN5_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN5_PAD_DRIVER_msb = 2
        self.__GPIO_PIN5_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN5_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN5_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN5_INT_ENA_msb, self.__GPIO_PIN5_INT_ENA_lsb)
    @GPIO_PIN5_INT_ENA.setter
    def GPIO_PIN5_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN5_INT_ENA_msb, self.__GPIO_PIN5_INT_ENA_lsb, value)

    @property
    def GPIO_PIN5_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN5_CONFIG_msb, self.__GPIO_PIN5_CONFIG_lsb)
    @GPIO_PIN5_CONFIG.setter
    def GPIO_PIN5_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN5_CONFIG_msb, self.__GPIO_PIN5_CONFIG_lsb, value)

    @property
    def GPIO_PIN5_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN5_WAKEUP_ENABLE_msb, self.__GPIO_PIN5_WAKEUP_ENABLE_lsb)
    @GPIO_PIN5_WAKEUP_ENABLE.setter
    def GPIO_PIN5_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN5_WAKEUP_ENABLE_msb, self.__GPIO_PIN5_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN5_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN5_INT_TYPE_msb, self.__GPIO_PIN5_INT_TYPE_lsb)
    @GPIO_PIN5_INT_TYPE.setter
    def GPIO_PIN5_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN5_INT_TYPE_msb, self.__GPIO_PIN5_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN5_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN5_PAD_DRIVER_msb, self.__GPIO_PIN5_PAD_DRIVER_lsb)
    @GPIO_PIN5_PAD_DRIVER.setter
    def GPIO_PIN5_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN5_PAD_DRIVER_msb, self.__GPIO_PIN5_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN5_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN5_SYNC_BYPASS_msb, self.__GPIO_PIN5_SYNC_BYPASS_lsb)
    @GPIO_PIN5_SYNC_BYPASS.setter
    def GPIO_PIN5_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN5_SYNC_BYPASS_msb, self.__GPIO_PIN5_SYNC_BYPASS_lsb, value)
class GPIO_PIN6(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0xa0
        self.__GPIO_PIN6_INT_ENA_lsb = 13
        self.__GPIO_PIN6_INT_ENA_msb = 17
        self.__GPIO_PIN6_CONFIG_lsb = 11
        self.__GPIO_PIN6_CONFIG_msb = 12
        self.__GPIO_PIN6_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN6_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN6_INT_TYPE_lsb = 7
        self.__GPIO_PIN6_INT_TYPE_msb = 9
        self.__GPIO_PIN6_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN6_PAD_DRIVER_msb = 2
        self.__GPIO_PIN6_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN6_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN6_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN6_INT_ENA_msb, self.__GPIO_PIN6_INT_ENA_lsb)
    @GPIO_PIN6_INT_ENA.setter
    def GPIO_PIN6_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN6_INT_ENA_msb, self.__GPIO_PIN6_INT_ENA_lsb, value)

    @property
    def GPIO_PIN6_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN6_CONFIG_msb, self.__GPIO_PIN6_CONFIG_lsb)
    @GPIO_PIN6_CONFIG.setter
    def GPIO_PIN6_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN6_CONFIG_msb, self.__GPIO_PIN6_CONFIG_lsb, value)

    @property
    def GPIO_PIN6_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN6_WAKEUP_ENABLE_msb, self.__GPIO_PIN6_WAKEUP_ENABLE_lsb)
    @GPIO_PIN6_WAKEUP_ENABLE.setter
    def GPIO_PIN6_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN6_WAKEUP_ENABLE_msb, self.__GPIO_PIN6_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN6_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN6_INT_TYPE_msb, self.__GPIO_PIN6_INT_TYPE_lsb)
    @GPIO_PIN6_INT_TYPE.setter
    def GPIO_PIN6_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN6_INT_TYPE_msb, self.__GPIO_PIN6_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN6_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN6_PAD_DRIVER_msb, self.__GPIO_PIN6_PAD_DRIVER_lsb)
    @GPIO_PIN6_PAD_DRIVER.setter
    def GPIO_PIN6_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN6_PAD_DRIVER_msb, self.__GPIO_PIN6_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN6_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN6_SYNC_BYPASS_msb, self.__GPIO_PIN6_SYNC_BYPASS_lsb)
    @GPIO_PIN6_SYNC_BYPASS.setter
    def GPIO_PIN6_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN6_SYNC_BYPASS_msb, self.__GPIO_PIN6_SYNC_BYPASS_lsb, value)
class GPIO_PIN7(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0xa4
        self.__GPIO_PIN7_INT_ENA_lsb = 13
        self.__GPIO_PIN7_INT_ENA_msb = 17
        self.__GPIO_PIN7_CONFIG_lsb = 11
        self.__GPIO_PIN7_CONFIG_msb = 12
        self.__GPIO_PIN7_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN7_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN7_INT_TYPE_lsb = 7
        self.__GPIO_PIN7_INT_TYPE_msb = 9
        self.__GPIO_PIN7_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN7_PAD_DRIVER_msb = 2
        self.__GPIO_PIN7_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN7_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN7_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN7_INT_ENA_msb, self.__GPIO_PIN7_INT_ENA_lsb)
    @GPIO_PIN7_INT_ENA.setter
    def GPIO_PIN7_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN7_INT_ENA_msb, self.__GPIO_PIN7_INT_ENA_lsb, value)

    @property
    def GPIO_PIN7_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN7_CONFIG_msb, self.__GPIO_PIN7_CONFIG_lsb)
    @GPIO_PIN7_CONFIG.setter
    def GPIO_PIN7_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN7_CONFIG_msb, self.__GPIO_PIN7_CONFIG_lsb, value)

    @property
    def GPIO_PIN7_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN7_WAKEUP_ENABLE_msb, self.__GPIO_PIN7_WAKEUP_ENABLE_lsb)
    @GPIO_PIN7_WAKEUP_ENABLE.setter
    def GPIO_PIN7_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN7_WAKEUP_ENABLE_msb, self.__GPIO_PIN7_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN7_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN7_INT_TYPE_msb, self.__GPIO_PIN7_INT_TYPE_lsb)
    @GPIO_PIN7_INT_TYPE.setter
    def GPIO_PIN7_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN7_INT_TYPE_msb, self.__GPIO_PIN7_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN7_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN7_PAD_DRIVER_msb, self.__GPIO_PIN7_PAD_DRIVER_lsb)
    @GPIO_PIN7_PAD_DRIVER.setter
    def GPIO_PIN7_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN7_PAD_DRIVER_msb, self.__GPIO_PIN7_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN7_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN7_SYNC_BYPASS_msb, self.__GPIO_PIN7_SYNC_BYPASS_lsb)
    @GPIO_PIN7_SYNC_BYPASS.setter
    def GPIO_PIN7_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN7_SYNC_BYPASS_msb, self.__GPIO_PIN7_SYNC_BYPASS_lsb, value)
class GPIO_PIN8(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0xa8
        self.__GPIO_PIN8_INT_ENA_lsb = 13
        self.__GPIO_PIN8_INT_ENA_msb = 17
        self.__GPIO_PIN8_CONFIG_lsb = 11
        self.__GPIO_PIN8_CONFIG_msb = 12
        self.__GPIO_PIN8_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN8_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN8_INT_TYPE_lsb = 7
        self.__GPIO_PIN8_INT_TYPE_msb = 9
        self.__GPIO_PIN8_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN8_PAD_DRIVER_msb = 2
        self.__GPIO_PIN8_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN8_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN8_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN8_INT_ENA_msb, self.__GPIO_PIN8_INT_ENA_lsb)
    @GPIO_PIN8_INT_ENA.setter
    def GPIO_PIN8_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN8_INT_ENA_msb, self.__GPIO_PIN8_INT_ENA_lsb, value)

    @property
    def GPIO_PIN8_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN8_CONFIG_msb, self.__GPIO_PIN8_CONFIG_lsb)
    @GPIO_PIN8_CONFIG.setter
    def GPIO_PIN8_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN8_CONFIG_msb, self.__GPIO_PIN8_CONFIG_lsb, value)

    @property
    def GPIO_PIN8_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN8_WAKEUP_ENABLE_msb, self.__GPIO_PIN8_WAKEUP_ENABLE_lsb)
    @GPIO_PIN8_WAKEUP_ENABLE.setter
    def GPIO_PIN8_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN8_WAKEUP_ENABLE_msb, self.__GPIO_PIN8_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN8_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN8_INT_TYPE_msb, self.__GPIO_PIN8_INT_TYPE_lsb)
    @GPIO_PIN8_INT_TYPE.setter
    def GPIO_PIN8_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN8_INT_TYPE_msb, self.__GPIO_PIN8_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN8_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN8_PAD_DRIVER_msb, self.__GPIO_PIN8_PAD_DRIVER_lsb)
    @GPIO_PIN8_PAD_DRIVER.setter
    def GPIO_PIN8_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN8_PAD_DRIVER_msb, self.__GPIO_PIN8_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN8_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN8_SYNC_BYPASS_msb, self.__GPIO_PIN8_SYNC_BYPASS_lsb)
    @GPIO_PIN8_SYNC_BYPASS.setter
    def GPIO_PIN8_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN8_SYNC_BYPASS_msb, self.__GPIO_PIN8_SYNC_BYPASS_lsb, value)
class GPIO_PIN9(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0xac
        self.__GPIO_PIN9_INT_ENA_lsb = 13
        self.__GPIO_PIN9_INT_ENA_msb = 17
        self.__GPIO_PIN9_CONFIG_lsb = 11
        self.__GPIO_PIN9_CONFIG_msb = 12
        self.__GPIO_PIN9_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN9_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN9_INT_TYPE_lsb = 7
        self.__GPIO_PIN9_INT_TYPE_msb = 9
        self.__GPIO_PIN9_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN9_PAD_DRIVER_msb = 2
        self.__GPIO_PIN9_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN9_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN9_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN9_INT_ENA_msb, self.__GPIO_PIN9_INT_ENA_lsb)
    @GPIO_PIN9_INT_ENA.setter
    def GPIO_PIN9_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN9_INT_ENA_msb, self.__GPIO_PIN9_INT_ENA_lsb, value)

    @property
    def GPIO_PIN9_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN9_CONFIG_msb, self.__GPIO_PIN9_CONFIG_lsb)
    @GPIO_PIN9_CONFIG.setter
    def GPIO_PIN9_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN9_CONFIG_msb, self.__GPIO_PIN9_CONFIG_lsb, value)

    @property
    def GPIO_PIN9_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN9_WAKEUP_ENABLE_msb, self.__GPIO_PIN9_WAKEUP_ENABLE_lsb)
    @GPIO_PIN9_WAKEUP_ENABLE.setter
    def GPIO_PIN9_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN9_WAKEUP_ENABLE_msb, self.__GPIO_PIN9_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN9_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN9_INT_TYPE_msb, self.__GPIO_PIN9_INT_TYPE_lsb)
    @GPIO_PIN9_INT_TYPE.setter
    def GPIO_PIN9_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN9_INT_TYPE_msb, self.__GPIO_PIN9_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN9_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN9_PAD_DRIVER_msb, self.__GPIO_PIN9_PAD_DRIVER_lsb)
    @GPIO_PIN9_PAD_DRIVER.setter
    def GPIO_PIN9_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN9_PAD_DRIVER_msb, self.__GPIO_PIN9_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN9_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN9_SYNC_BYPASS_msb, self.__GPIO_PIN9_SYNC_BYPASS_lsb)
    @GPIO_PIN9_SYNC_BYPASS.setter
    def GPIO_PIN9_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN9_SYNC_BYPASS_msb, self.__GPIO_PIN9_SYNC_BYPASS_lsb, value)
class GPIO_PIN10(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0xb0
        self.__GPIO_PIN10_INT_ENA_lsb = 13
        self.__GPIO_PIN10_INT_ENA_msb = 17
        self.__GPIO_PIN10_CONFIG_lsb = 11
        self.__GPIO_PIN10_CONFIG_msb = 12
        self.__GPIO_PIN10_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN10_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN10_INT_TYPE_lsb = 7
        self.__GPIO_PIN10_INT_TYPE_msb = 9
        self.__GPIO_PIN10_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN10_PAD_DRIVER_msb = 2
        self.__GPIO_PIN10_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN10_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN10_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN10_INT_ENA_msb, self.__GPIO_PIN10_INT_ENA_lsb)
    @GPIO_PIN10_INT_ENA.setter
    def GPIO_PIN10_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN10_INT_ENA_msb, self.__GPIO_PIN10_INT_ENA_lsb, value)

    @property
    def GPIO_PIN10_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN10_CONFIG_msb, self.__GPIO_PIN10_CONFIG_lsb)
    @GPIO_PIN10_CONFIG.setter
    def GPIO_PIN10_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN10_CONFIG_msb, self.__GPIO_PIN10_CONFIG_lsb, value)

    @property
    def GPIO_PIN10_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN10_WAKEUP_ENABLE_msb, self.__GPIO_PIN10_WAKEUP_ENABLE_lsb)
    @GPIO_PIN10_WAKEUP_ENABLE.setter
    def GPIO_PIN10_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN10_WAKEUP_ENABLE_msb, self.__GPIO_PIN10_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN10_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN10_INT_TYPE_msb, self.__GPIO_PIN10_INT_TYPE_lsb)
    @GPIO_PIN10_INT_TYPE.setter
    def GPIO_PIN10_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN10_INT_TYPE_msb, self.__GPIO_PIN10_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN10_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN10_PAD_DRIVER_msb, self.__GPIO_PIN10_PAD_DRIVER_lsb)
    @GPIO_PIN10_PAD_DRIVER.setter
    def GPIO_PIN10_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN10_PAD_DRIVER_msb, self.__GPIO_PIN10_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN10_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN10_SYNC_BYPASS_msb, self.__GPIO_PIN10_SYNC_BYPASS_lsb)
    @GPIO_PIN10_SYNC_BYPASS.setter
    def GPIO_PIN10_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN10_SYNC_BYPASS_msb, self.__GPIO_PIN10_SYNC_BYPASS_lsb, value)
class GPIO_PIN11(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0xb4
        self.__GPIO_PIN11_INT_ENA_lsb = 13
        self.__GPIO_PIN11_INT_ENA_msb = 17
        self.__GPIO_PIN11_CONFIG_lsb = 11
        self.__GPIO_PIN11_CONFIG_msb = 12
        self.__GPIO_PIN11_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN11_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN11_INT_TYPE_lsb = 7
        self.__GPIO_PIN11_INT_TYPE_msb = 9
        self.__GPIO_PIN11_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN11_PAD_DRIVER_msb = 2
        self.__GPIO_PIN11_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN11_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN11_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN11_INT_ENA_msb, self.__GPIO_PIN11_INT_ENA_lsb)
    @GPIO_PIN11_INT_ENA.setter
    def GPIO_PIN11_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN11_INT_ENA_msb, self.__GPIO_PIN11_INT_ENA_lsb, value)

    @property
    def GPIO_PIN11_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN11_CONFIG_msb, self.__GPIO_PIN11_CONFIG_lsb)
    @GPIO_PIN11_CONFIG.setter
    def GPIO_PIN11_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN11_CONFIG_msb, self.__GPIO_PIN11_CONFIG_lsb, value)

    @property
    def GPIO_PIN11_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN11_WAKEUP_ENABLE_msb, self.__GPIO_PIN11_WAKEUP_ENABLE_lsb)
    @GPIO_PIN11_WAKEUP_ENABLE.setter
    def GPIO_PIN11_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN11_WAKEUP_ENABLE_msb, self.__GPIO_PIN11_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN11_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN11_INT_TYPE_msb, self.__GPIO_PIN11_INT_TYPE_lsb)
    @GPIO_PIN11_INT_TYPE.setter
    def GPIO_PIN11_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN11_INT_TYPE_msb, self.__GPIO_PIN11_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN11_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN11_PAD_DRIVER_msb, self.__GPIO_PIN11_PAD_DRIVER_lsb)
    @GPIO_PIN11_PAD_DRIVER.setter
    def GPIO_PIN11_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN11_PAD_DRIVER_msb, self.__GPIO_PIN11_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN11_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN11_SYNC_BYPASS_msb, self.__GPIO_PIN11_SYNC_BYPASS_lsb)
    @GPIO_PIN11_SYNC_BYPASS.setter
    def GPIO_PIN11_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN11_SYNC_BYPASS_msb, self.__GPIO_PIN11_SYNC_BYPASS_lsb, value)
class GPIO_PIN12(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0xb8
        self.__GPIO_PIN12_INT_ENA_lsb = 13
        self.__GPIO_PIN12_INT_ENA_msb = 17
        self.__GPIO_PIN12_CONFIG_lsb = 11
        self.__GPIO_PIN12_CONFIG_msb = 12
        self.__GPIO_PIN12_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN12_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN12_INT_TYPE_lsb = 7
        self.__GPIO_PIN12_INT_TYPE_msb = 9
        self.__GPIO_PIN12_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN12_PAD_DRIVER_msb = 2
        self.__GPIO_PIN12_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN12_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN12_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN12_INT_ENA_msb, self.__GPIO_PIN12_INT_ENA_lsb)
    @GPIO_PIN12_INT_ENA.setter
    def GPIO_PIN12_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN12_INT_ENA_msb, self.__GPIO_PIN12_INT_ENA_lsb, value)

    @property
    def GPIO_PIN12_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN12_CONFIG_msb, self.__GPIO_PIN12_CONFIG_lsb)
    @GPIO_PIN12_CONFIG.setter
    def GPIO_PIN12_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN12_CONFIG_msb, self.__GPIO_PIN12_CONFIG_lsb, value)

    @property
    def GPIO_PIN12_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN12_WAKEUP_ENABLE_msb, self.__GPIO_PIN12_WAKEUP_ENABLE_lsb)
    @GPIO_PIN12_WAKEUP_ENABLE.setter
    def GPIO_PIN12_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN12_WAKEUP_ENABLE_msb, self.__GPIO_PIN12_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN12_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN12_INT_TYPE_msb, self.__GPIO_PIN12_INT_TYPE_lsb)
    @GPIO_PIN12_INT_TYPE.setter
    def GPIO_PIN12_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN12_INT_TYPE_msb, self.__GPIO_PIN12_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN12_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN12_PAD_DRIVER_msb, self.__GPIO_PIN12_PAD_DRIVER_lsb)
    @GPIO_PIN12_PAD_DRIVER.setter
    def GPIO_PIN12_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN12_PAD_DRIVER_msb, self.__GPIO_PIN12_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN12_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN12_SYNC_BYPASS_msb, self.__GPIO_PIN12_SYNC_BYPASS_lsb)
    @GPIO_PIN12_SYNC_BYPASS.setter
    def GPIO_PIN12_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN12_SYNC_BYPASS_msb, self.__GPIO_PIN12_SYNC_BYPASS_lsb, value)
class GPIO_PIN13(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0xbc
        self.__GPIO_PIN13_INT_ENA_lsb = 13
        self.__GPIO_PIN13_INT_ENA_msb = 17
        self.__GPIO_PIN13_CONFIG_lsb = 11
        self.__GPIO_PIN13_CONFIG_msb = 12
        self.__GPIO_PIN13_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN13_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN13_INT_TYPE_lsb = 7
        self.__GPIO_PIN13_INT_TYPE_msb = 9
        self.__GPIO_PIN13_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN13_PAD_DRIVER_msb = 2
        self.__GPIO_PIN13_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN13_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN13_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN13_INT_ENA_msb, self.__GPIO_PIN13_INT_ENA_lsb)
    @GPIO_PIN13_INT_ENA.setter
    def GPIO_PIN13_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN13_INT_ENA_msb, self.__GPIO_PIN13_INT_ENA_lsb, value)

    @property
    def GPIO_PIN13_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN13_CONFIG_msb, self.__GPIO_PIN13_CONFIG_lsb)
    @GPIO_PIN13_CONFIG.setter
    def GPIO_PIN13_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN13_CONFIG_msb, self.__GPIO_PIN13_CONFIG_lsb, value)

    @property
    def GPIO_PIN13_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN13_WAKEUP_ENABLE_msb, self.__GPIO_PIN13_WAKEUP_ENABLE_lsb)
    @GPIO_PIN13_WAKEUP_ENABLE.setter
    def GPIO_PIN13_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN13_WAKEUP_ENABLE_msb, self.__GPIO_PIN13_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN13_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN13_INT_TYPE_msb, self.__GPIO_PIN13_INT_TYPE_lsb)
    @GPIO_PIN13_INT_TYPE.setter
    def GPIO_PIN13_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN13_INT_TYPE_msb, self.__GPIO_PIN13_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN13_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN13_PAD_DRIVER_msb, self.__GPIO_PIN13_PAD_DRIVER_lsb)
    @GPIO_PIN13_PAD_DRIVER.setter
    def GPIO_PIN13_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN13_PAD_DRIVER_msb, self.__GPIO_PIN13_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN13_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN13_SYNC_BYPASS_msb, self.__GPIO_PIN13_SYNC_BYPASS_lsb)
    @GPIO_PIN13_SYNC_BYPASS.setter
    def GPIO_PIN13_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN13_SYNC_BYPASS_msb, self.__GPIO_PIN13_SYNC_BYPASS_lsb, value)
class GPIO_PIN14(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0xc0
        self.__GPIO_PIN14_INT_ENA_lsb = 13
        self.__GPIO_PIN14_INT_ENA_msb = 17
        self.__GPIO_PIN14_CONFIG_lsb = 11
        self.__GPIO_PIN14_CONFIG_msb = 12
        self.__GPIO_PIN14_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN14_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN14_INT_TYPE_lsb = 7
        self.__GPIO_PIN14_INT_TYPE_msb = 9
        self.__GPIO_PIN14_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN14_PAD_DRIVER_msb = 2
        self.__GPIO_PIN14_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN14_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN14_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN14_INT_ENA_msb, self.__GPIO_PIN14_INT_ENA_lsb)
    @GPIO_PIN14_INT_ENA.setter
    def GPIO_PIN14_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN14_INT_ENA_msb, self.__GPIO_PIN14_INT_ENA_lsb, value)

    @property
    def GPIO_PIN14_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN14_CONFIG_msb, self.__GPIO_PIN14_CONFIG_lsb)
    @GPIO_PIN14_CONFIG.setter
    def GPIO_PIN14_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN14_CONFIG_msb, self.__GPIO_PIN14_CONFIG_lsb, value)

    @property
    def GPIO_PIN14_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN14_WAKEUP_ENABLE_msb, self.__GPIO_PIN14_WAKEUP_ENABLE_lsb)
    @GPIO_PIN14_WAKEUP_ENABLE.setter
    def GPIO_PIN14_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN14_WAKEUP_ENABLE_msb, self.__GPIO_PIN14_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN14_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN14_INT_TYPE_msb, self.__GPIO_PIN14_INT_TYPE_lsb)
    @GPIO_PIN14_INT_TYPE.setter
    def GPIO_PIN14_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN14_INT_TYPE_msb, self.__GPIO_PIN14_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN14_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN14_PAD_DRIVER_msb, self.__GPIO_PIN14_PAD_DRIVER_lsb)
    @GPIO_PIN14_PAD_DRIVER.setter
    def GPIO_PIN14_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN14_PAD_DRIVER_msb, self.__GPIO_PIN14_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN14_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN14_SYNC_BYPASS_msb, self.__GPIO_PIN14_SYNC_BYPASS_lsb)
    @GPIO_PIN14_SYNC_BYPASS.setter
    def GPIO_PIN14_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN14_SYNC_BYPASS_msb, self.__GPIO_PIN14_SYNC_BYPASS_lsb, value)
class GPIO_PIN15(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0xc4
        self.__GPIO_PIN15_INT_ENA_lsb = 13
        self.__GPIO_PIN15_INT_ENA_msb = 17
        self.__GPIO_PIN15_CONFIG_lsb = 11
        self.__GPIO_PIN15_CONFIG_msb = 12
        self.__GPIO_PIN15_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN15_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN15_INT_TYPE_lsb = 7
        self.__GPIO_PIN15_INT_TYPE_msb = 9
        self.__GPIO_PIN15_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN15_PAD_DRIVER_msb = 2
        self.__GPIO_PIN15_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN15_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN15_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN15_INT_ENA_msb, self.__GPIO_PIN15_INT_ENA_lsb)
    @GPIO_PIN15_INT_ENA.setter
    def GPIO_PIN15_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN15_INT_ENA_msb, self.__GPIO_PIN15_INT_ENA_lsb, value)

    @property
    def GPIO_PIN15_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN15_CONFIG_msb, self.__GPIO_PIN15_CONFIG_lsb)
    @GPIO_PIN15_CONFIG.setter
    def GPIO_PIN15_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN15_CONFIG_msb, self.__GPIO_PIN15_CONFIG_lsb, value)

    @property
    def GPIO_PIN15_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN15_WAKEUP_ENABLE_msb, self.__GPIO_PIN15_WAKEUP_ENABLE_lsb)
    @GPIO_PIN15_WAKEUP_ENABLE.setter
    def GPIO_PIN15_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN15_WAKEUP_ENABLE_msb, self.__GPIO_PIN15_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN15_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN15_INT_TYPE_msb, self.__GPIO_PIN15_INT_TYPE_lsb)
    @GPIO_PIN15_INT_TYPE.setter
    def GPIO_PIN15_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN15_INT_TYPE_msb, self.__GPIO_PIN15_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN15_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN15_PAD_DRIVER_msb, self.__GPIO_PIN15_PAD_DRIVER_lsb)
    @GPIO_PIN15_PAD_DRIVER.setter
    def GPIO_PIN15_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN15_PAD_DRIVER_msb, self.__GPIO_PIN15_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN15_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN15_SYNC_BYPASS_msb, self.__GPIO_PIN15_SYNC_BYPASS_lsb)
    @GPIO_PIN15_SYNC_BYPASS.setter
    def GPIO_PIN15_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN15_SYNC_BYPASS_msb, self.__GPIO_PIN15_SYNC_BYPASS_lsb, value)
class GPIO_PIN16(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0xc8
        self.__GPIO_PIN16_INT_ENA_lsb = 13
        self.__GPIO_PIN16_INT_ENA_msb = 17
        self.__GPIO_PIN16_CONFIG_lsb = 11
        self.__GPIO_PIN16_CONFIG_msb = 12
        self.__GPIO_PIN16_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN16_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN16_INT_TYPE_lsb = 7
        self.__GPIO_PIN16_INT_TYPE_msb = 9
        self.__GPIO_PIN16_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN16_PAD_DRIVER_msb = 2
        self.__GPIO_PIN16_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN16_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN16_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN16_INT_ENA_msb, self.__GPIO_PIN16_INT_ENA_lsb)
    @GPIO_PIN16_INT_ENA.setter
    def GPIO_PIN16_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN16_INT_ENA_msb, self.__GPIO_PIN16_INT_ENA_lsb, value)

    @property
    def GPIO_PIN16_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN16_CONFIG_msb, self.__GPIO_PIN16_CONFIG_lsb)
    @GPIO_PIN16_CONFIG.setter
    def GPIO_PIN16_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN16_CONFIG_msb, self.__GPIO_PIN16_CONFIG_lsb, value)

    @property
    def GPIO_PIN16_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN16_WAKEUP_ENABLE_msb, self.__GPIO_PIN16_WAKEUP_ENABLE_lsb)
    @GPIO_PIN16_WAKEUP_ENABLE.setter
    def GPIO_PIN16_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN16_WAKEUP_ENABLE_msb, self.__GPIO_PIN16_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN16_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN16_INT_TYPE_msb, self.__GPIO_PIN16_INT_TYPE_lsb)
    @GPIO_PIN16_INT_TYPE.setter
    def GPIO_PIN16_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN16_INT_TYPE_msb, self.__GPIO_PIN16_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN16_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN16_PAD_DRIVER_msb, self.__GPIO_PIN16_PAD_DRIVER_lsb)
    @GPIO_PIN16_PAD_DRIVER.setter
    def GPIO_PIN16_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN16_PAD_DRIVER_msb, self.__GPIO_PIN16_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN16_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN16_SYNC_BYPASS_msb, self.__GPIO_PIN16_SYNC_BYPASS_lsb)
    @GPIO_PIN16_SYNC_BYPASS.setter
    def GPIO_PIN16_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN16_SYNC_BYPASS_msb, self.__GPIO_PIN16_SYNC_BYPASS_lsb, value)
class GPIO_PIN17(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0xcc
        self.__GPIO_PIN17_INT_ENA_lsb = 13
        self.__GPIO_PIN17_INT_ENA_msb = 17
        self.__GPIO_PIN17_CONFIG_lsb = 11
        self.__GPIO_PIN17_CONFIG_msb = 12
        self.__GPIO_PIN17_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN17_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN17_INT_TYPE_lsb = 7
        self.__GPIO_PIN17_INT_TYPE_msb = 9
        self.__GPIO_PIN17_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN17_PAD_DRIVER_msb = 2
        self.__GPIO_PIN17_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN17_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN17_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN17_INT_ENA_msb, self.__GPIO_PIN17_INT_ENA_lsb)
    @GPIO_PIN17_INT_ENA.setter
    def GPIO_PIN17_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN17_INT_ENA_msb, self.__GPIO_PIN17_INT_ENA_lsb, value)

    @property
    def GPIO_PIN17_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN17_CONFIG_msb, self.__GPIO_PIN17_CONFIG_lsb)
    @GPIO_PIN17_CONFIG.setter
    def GPIO_PIN17_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN17_CONFIG_msb, self.__GPIO_PIN17_CONFIG_lsb, value)

    @property
    def GPIO_PIN17_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN17_WAKEUP_ENABLE_msb, self.__GPIO_PIN17_WAKEUP_ENABLE_lsb)
    @GPIO_PIN17_WAKEUP_ENABLE.setter
    def GPIO_PIN17_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN17_WAKEUP_ENABLE_msb, self.__GPIO_PIN17_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN17_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN17_INT_TYPE_msb, self.__GPIO_PIN17_INT_TYPE_lsb)
    @GPIO_PIN17_INT_TYPE.setter
    def GPIO_PIN17_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN17_INT_TYPE_msb, self.__GPIO_PIN17_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN17_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN17_PAD_DRIVER_msb, self.__GPIO_PIN17_PAD_DRIVER_lsb)
    @GPIO_PIN17_PAD_DRIVER.setter
    def GPIO_PIN17_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN17_PAD_DRIVER_msb, self.__GPIO_PIN17_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN17_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN17_SYNC_BYPASS_msb, self.__GPIO_PIN17_SYNC_BYPASS_lsb)
    @GPIO_PIN17_SYNC_BYPASS.setter
    def GPIO_PIN17_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN17_SYNC_BYPASS_msb, self.__GPIO_PIN17_SYNC_BYPASS_lsb, value)
class GPIO_PIN18(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0xd0
        self.__GPIO_PIN18_INT_ENA_lsb = 13
        self.__GPIO_PIN18_INT_ENA_msb = 17
        self.__GPIO_PIN18_CONFIG_lsb = 11
        self.__GPIO_PIN18_CONFIG_msb = 12
        self.__GPIO_PIN18_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN18_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN18_INT_TYPE_lsb = 7
        self.__GPIO_PIN18_INT_TYPE_msb = 9
        self.__GPIO_PIN18_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN18_PAD_DRIVER_msb = 2
        self.__GPIO_PIN18_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN18_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN18_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN18_INT_ENA_msb, self.__GPIO_PIN18_INT_ENA_lsb)
    @GPIO_PIN18_INT_ENA.setter
    def GPIO_PIN18_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN18_INT_ENA_msb, self.__GPIO_PIN18_INT_ENA_lsb, value)

    @property
    def GPIO_PIN18_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN18_CONFIG_msb, self.__GPIO_PIN18_CONFIG_lsb)
    @GPIO_PIN18_CONFIG.setter
    def GPIO_PIN18_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN18_CONFIG_msb, self.__GPIO_PIN18_CONFIG_lsb, value)

    @property
    def GPIO_PIN18_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN18_WAKEUP_ENABLE_msb, self.__GPIO_PIN18_WAKEUP_ENABLE_lsb)
    @GPIO_PIN18_WAKEUP_ENABLE.setter
    def GPIO_PIN18_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN18_WAKEUP_ENABLE_msb, self.__GPIO_PIN18_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN18_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN18_INT_TYPE_msb, self.__GPIO_PIN18_INT_TYPE_lsb)
    @GPIO_PIN18_INT_TYPE.setter
    def GPIO_PIN18_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN18_INT_TYPE_msb, self.__GPIO_PIN18_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN18_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN18_PAD_DRIVER_msb, self.__GPIO_PIN18_PAD_DRIVER_lsb)
    @GPIO_PIN18_PAD_DRIVER.setter
    def GPIO_PIN18_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN18_PAD_DRIVER_msb, self.__GPIO_PIN18_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN18_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN18_SYNC_BYPASS_msb, self.__GPIO_PIN18_SYNC_BYPASS_lsb)
    @GPIO_PIN18_SYNC_BYPASS.setter
    def GPIO_PIN18_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN18_SYNC_BYPASS_msb, self.__GPIO_PIN18_SYNC_BYPASS_lsb, value)
class GPIO_PIN19(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0xd4
        self.__GPIO_PIN19_INT_ENA_lsb = 13
        self.__GPIO_PIN19_INT_ENA_msb = 17
        self.__GPIO_PIN19_CONFIG_lsb = 11
        self.__GPIO_PIN19_CONFIG_msb = 12
        self.__GPIO_PIN19_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN19_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN19_INT_TYPE_lsb = 7
        self.__GPIO_PIN19_INT_TYPE_msb = 9
        self.__GPIO_PIN19_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN19_PAD_DRIVER_msb = 2
        self.__GPIO_PIN19_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN19_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN19_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN19_INT_ENA_msb, self.__GPIO_PIN19_INT_ENA_lsb)
    @GPIO_PIN19_INT_ENA.setter
    def GPIO_PIN19_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN19_INT_ENA_msb, self.__GPIO_PIN19_INT_ENA_lsb, value)

    @property
    def GPIO_PIN19_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN19_CONFIG_msb, self.__GPIO_PIN19_CONFIG_lsb)
    @GPIO_PIN19_CONFIG.setter
    def GPIO_PIN19_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN19_CONFIG_msb, self.__GPIO_PIN19_CONFIG_lsb, value)

    @property
    def GPIO_PIN19_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN19_WAKEUP_ENABLE_msb, self.__GPIO_PIN19_WAKEUP_ENABLE_lsb)
    @GPIO_PIN19_WAKEUP_ENABLE.setter
    def GPIO_PIN19_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN19_WAKEUP_ENABLE_msb, self.__GPIO_PIN19_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN19_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN19_INT_TYPE_msb, self.__GPIO_PIN19_INT_TYPE_lsb)
    @GPIO_PIN19_INT_TYPE.setter
    def GPIO_PIN19_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN19_INT_TYPE_msb, self.__GPIO_PIN19_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN19_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN19_PAD_DRIVER_msb, self.__GPIO_PIN19_PAD_DRIVER_lsb)
    @GPIO_PIN19_PAD_DRIVER.setter
    def GPIO_PIN19_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN19_PAD_DRIVER_msb, self.__GPIO_PIN19_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN19_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN19_SYNC_BYPASS_msb, self.__GPIO_PIN19_SYNC_BYPASS_lsb)
    @GPIO_PIN19_SYNC_BYPASS.setter
    def GPIO_PIN19_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN19_SYNC_BYPASS_msb, self.__GPIO_PIN19_SYNC_BYPASS_lsb, value)
class GPIO_PIN20(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0xd8
        self.__GPIO_PIN20_INT_ENA_lsb = 13
        self.__GPIO_PIN20_INT_ENA_msb = 17
        self.__GPIO_PIN20_CONFIG_lsb = 11
        self.__GPIO_PIN20_CONFIG_msb = 12
        self.__GPIO_PIN20_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN20_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN20_INT_TYPE_lsb = 7
        self.__GPIO_PIN20_INT_TYPE_msb = 9
        self.__GPIO_PIN20_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN20_PAD_DRIVER_msb = 2
        self.__GPIO_PIN20_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN20_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN20_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN20_INT_ENA_msb, self.__GPIO_PIN20_INT_ENA_lsb)
    @GPIO_PIN20_INT_ENA.setter
    def GPIO_PIN20_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN20_INT_ENA_msb, self.__GPIO_PIN20_INT_ENA_lsb, value)

    @property
    def GPIO_PIN20_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN20_CONFIG_msb, self.__GPIO_PIN20_CONFIG_lsb)
    @GPIO_PIN20_CONFIG.setter
    def GPIO_PIN20_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN20_CONFIG_msb, self.__GPIO_PIN20_CONFIG_lsb, value)

    @property
    def GPIO_PIN20_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN20_WAKEUP_ENABLE_msb, self.__GPIO_PIN20_WAKEUP_ENABLE_lsb)
    @GPIO_PIN20_WAKEUP_ENABLE.setter
    def GPIO_PIN20_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN20_WAKEUP_ENABLE_msb, self.__GPIO_PIN20_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN20_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN20_INT_TYPE_msb, self.__GPIO_PIN20_INT_TYPE_lsb)
    @GPIO_PIN20_INT_TYPE.setter
    def GPIO_PIN20_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN20_INT_TYPE_msb, self.__GPIO_PIN20_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN20_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN20_PAD_DRIVER_msb, self.__GPIO_PIN20_PAD_DRIVER_lsb)
    @GPIO_PIN20_PAD_DRIVER.setter
    def GPIO_PIN20_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN20_PAD_DRIVER_msb, self.__GPIO_PIN20_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN20_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN20_SYNC_BYPASS_msb, self.__GPIO_PIN20_SYNC_BYPASS_lsb)
    @GPIO_PIN20_SYNC_BYPASS.setter
    def GPIO_PIN20_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN20_SYNC_BYPASS_msb, self.__GPIO_PIN20_SYNC_BYPASS_lsb, value)
class GPIO_PIN21(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0xdc
        self.__GPIO_PIN21_INT_ENA_lsb = 13
        self.__GPIO_PIN21_INT_ENA_msb = 17
        self.__GPIO_PIN21_CONFIG_lsb = 11
        self.__GPIO_PIN21_CONFIG_msb = 12
        self.__GPIO_PIN21_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN21_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN21_INT_TYPE_lsb = 7
        self.__GPIO_PIN21_INT_TYPE_msb = 9
        self.__GPIO_PIN21_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN21_PAD_DRIVER_msb = 2
        self.__GPIO_PIN21_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN21_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN21_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN21_INT_ENA_msb, self.__GPIO_PIN21_INT_ENA_lsb)
    @GPIO_PIN21_INT_ENA.setter
    def GPIO_PIN21_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN21_INT_ENA_msb, self.__GPIO_PIN21_INT_ENA_lsb, value)

    @property
    def GPIO_PIN21_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN21_CONFIG_msb, self.__GPIO_PIN21_CONFIG_lsb)
    @GPIO_PIN21_CONFIG.setter
    def GPIO_PIN21_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN21_CONFIG_msb, self.__GPIO_PIN21_CONFIG_lsb, value)

    @property
    def GPIO_PIN21_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN21_WAKEUP_ENABLE_msb, self.__GPIO_PIN21_WAKEUP_ENABLE_lsb)
    @GPIO_PIN21_WAKEUP_ENABLE.setter
    def GPIO_PIN21_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN21_WAKEUP_ENABLE_msb, self.__GPIO_PIN21_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN21_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN21_INT_TYPE_msb, self.__GPIO_PIN21_INT_TYPE_lsb)
    @GPIO_PIN21_INT_TYPE.setter
    def GPIO_PIN21_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN21_INT_TYPE_msb, self.__GPIO_PIN21_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN21_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN21_PAD_DRIVER_msb, self.__GPIO_PIN21_PAD_DRIVER_lsb)
    @GPIO_PIN21_PAD_DRIVER.setter
    def GPIO_PIN21_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN21_PAD_DRIVER_msb, self.__GPIO_PIN21_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN21_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN21_SYNC_BYPASS_msb, self.__GPIO_PIN21_SYNC_BYPASS_lsb)
    @GPIO_PIN21_SYNC_BYPASS.setter
    def GPIO_PIN21_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN21_SYNC_BYPASS_msb, self.__GPIO_PIN21_SYNC_BYPASS_lsb, value)
class GPIO_PIN22(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0xe0
        self.__GPIO_PIN22_INT_ENA_lsb = 13
        self.__GPIO_PIN22_INT_ENA_msb = 17
        self.__GPIO_PIN22_CONFIG_lsb = 11
        self.__GPIO_PIN22_CONFIG_msb = 12
        self.__GPIO_PIN22_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN22_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN22_INT_TYPE_lsb = 7
        self.__GPIO_PIN22_INT_TYPE_msb = 9
        self.__GPIO_PIN22_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN22_PAD_DRIVER_msb = 2
        self.__GPIO_PIN22_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN22_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN22_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN22_INT_ENA_msb, self.__GPIO_PIN22_INT_ENA_lsb)
    @GPIO_PIN22_INT_ENA.setter
    def GPIO_PIN22_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN22_INT_ENA_msb, self.__GPIO_PIN22_INT_ENA_lsb, value)

    @property
    def GPIO_PIN22_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN22_CONFIG_msb, self.__GPIO_PIN22_CONFIG_lsb)
    @GPIO_PIN22_CONFIG.setter
    def GPIO_PIN22_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN22_CONFIG_msb, self.__GPIO_PIN22_CONFIG_lsb, value)

    @property
    def GPIO_PIN22_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN22_WAKEUP_ENABLE_msb, self.__GPIO_PIN22_WAKEUP_ENABLE_lsb)
    @GPIO_PIN22_WAKEUP_ENABLE.setter
    def GPIO_PIN22_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN22_WAKEUP_ENABLE_msb, self.__GPIO_PIN22_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN22_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN22_INT_TYPE_msb, self.__GPIO_PIN22_INT_TYPE_lsb)
    @GPIO_PIN22_INT_TYPE.setter
    def GPIO_PIN22_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN22_INT_TYPE_msb, self.__GPIO_PIN22_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN22_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN22_PAD_DRIVER_msb, self.__GPIO_PIN22_PAD_DRIVER_lsb)
    @GPIO_PIN22_PAD_DRIVER.setter
    def GPIO_PIN22_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN22_PAD_DRIVER_msb, self.__GPIO_PIN22_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN22_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN22_SYNC_BYPASS_msb, self.__GPIO_PIN22_SYNC_BYPASS_lsb)
    @GPIO_PIN22_SYNC_BYPASS.setter
    def GPIO_PIN22_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN22_SYNC_BYPASS_msb, self.__GPIO_PIN22_SYNC_BYPASS_lsb, value)
class GPIO_PIN23(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0xe4
        self.__GPIO_PIN23_INT_ENA_lsb = 13
        self.__GPIO_PIN23_INT_ENA_msb = 17
        self.__GPIO_PIN23_CONFIG_lsb = 11
        self.__GPIO_PIN23_CONFIG_msb = 12
        self.__GPIO_PIN23_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN23_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN23_INT_TYPE_lsb = 7
        self.__GPIO_PIN23_INT_TYPE_msb = 9
        self.__GPIO_PIN23_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN23_PAD_DRIVER_msb = 2
        self.__GPIO_PIN23_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN23_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN23_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN23_INT_ENA_msb, self.__GPIO_PIN23_INT_ENA_lsb)
    @GPIO_PIN23_INT_ENA.setter
    def GPIO_PIN23_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN23_INT_ENA_msb, self.__GPIO_PIN23_INT_ENA_lsb, value)

    @property
    def GPIO_PIN23_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN23_CONFIG_msb, self.__GPIO_PIN23_CONFIG_lsb)
    @GPIO_PIN23_CONFIG.setter
    def GPIO_PIN23_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN23_CONFIG_msb, self.__GPIO_PIN23_CONFIG_lsb, value)

    @property
    def GPIO_PIN23_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN23_WAKEUP_ENABLE_msb, self.__GPIO_PIN23_WAKEUP_ENABLE_lsb)
    @GPIO_PIN23_WAKEUP_ENABLE.setter
    def GPIO_PIN23_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN23_WAKEUP_ENABLE_msb, self.__GPIO_PIN23_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN23_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN23_INT_TYPE_msb, self.__GPIO_PIN23_INT_TYPE_lsb)
    @GPIO_PIN23_INT_TYPE.setter
    def GPIO_PIN23_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN23_INT_TYPE_msb, self.__GPIO_PIN23_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN23_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN23_PAD_DRIVER_msb, self.__GPIO_PIN23_PAD_DRIVER_lsb)
    @GPIO_PIN23_PAD_DRIVER.setter
    def GPIO_PIN23_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN23_PAD_DRIVER_msb, self.__GPIO_PIN23_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN23_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN23_SYNC_BYPASS_msb, self.__GPIO_PIN23_SYNC_BYPASS_lsb)
    @GPIO_PIN23_SYNC_BYPASS.setter
    def GPIO_PIN23_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN23_SYNC_BYPASS_msb, self.__GPIO_PIN23_SYNC_BYPASS_lsb, value)
class GPIO_PIN24(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0xe8
        self.__GPIO_PIN24_INT_ENA_lsb = 13
        self.__GPIO_PIN24_INT_ENA_msb = 17
        self.__GPIO_PIN24_CONFIG_lsb = 11
        self.__GPIO_PIN24_CONFIG_msb = 12
        self.__GPIO_PIN24_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN24_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN24_INT_TYPE_lsb = 7
        self.__GPIO_PIN24_INT_TYPE_msb = 9
        self.__GPIO_PIN24_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN24_PAD_DRIVER_msb = 2
        self.__GPIO_PIN24_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN24_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN24_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN24_INT_ENA_msb, self.__GPIO_PIN24_INT_ENA_lsb)
    @GPIO_PIN24_INT_ENA.setter
    def GPIO_PIN24_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN24_INT_ENA_msb, self.__GPIO_PIN24_INT_ENA_lsb, value)

    @property
    def GPIO_PIN24_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN24_CONFIG_msb, self.__GPIO_PIN24_CONFIG_lsb)
    @GPIO_PIN24_CONFIG.setter
    def GPIO_PIN24_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN24_CONFIG_msb, self.__GPIO_PIN24_CONFIG_lsb, value)

    @property
    def GPIO_PIN24_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN24_WAKEUP_ENABLE_msb, self.__GPIO_PIN24_WAKEUP_ENABLE_lsb)
    @GPIO_PIN24_WAKEUP_ENABLE.setter
    def GPIO_PIN24_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN24_WAKEUP_ENABLE_msb, self.__GPIO_PIN24_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN24_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN24_INT_TYPE_msb, self.__GPIO_PIN24_INT_TYPE_lsb)
    @GPIO_PIN24_INT_TYPE.setter
    def GPIO_PIN24_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN24_INT_TYPE_msb, self.__GPIO_PIN24_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN24_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN24_PAD_DRIVER_msb, self.__GPIO_PIN24_PAD_DRIVER_lsb)
    @GPIO_PIN24_PAD_DRIVER.setter
    def GPIO_PIN24_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN24_PAD_DRIVER_msb, self.__GPIO_PIN24_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN24_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN24_SYNC_BYPASS_msb, self.__GPIO_PIN24_SYNC_BYPASS_lsb)
    @GPIO_PIN24_SYNC_BYPASS.setter
    def GPIO_PIN24_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN24_SYNC_BYPASS_msb, self.__GPIO_PIN24_SYNC_BYPASS_lsb, value)
class GPIO_PIN25(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0xec
        self.__GPIO_PIN25_INT_ENA_lsb = 13
        self.__GPIO_PIN25_INT_ENA_msb = 17
        self.__GPIO_PIN25_CONFIG_lsb = 11
        self.__GPIO_PIN25_CONFIG_msb = 12
        self.__GPIO_PIN25_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN25_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN25_INT_TYPE_lsb = 7
        self.__GPIO_PIN25_INT_TYPE_msb = 9
        self.__GPIO_PIN25_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN25_PAD_DRIVER_msb = 2
        self.__GPIO_PIN25_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN25_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN25_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN25_INT_ENA_msb, self.__GPIO_PIN25_INT_ENA_lsb)
    @GPIO_PIN25_INT_ENA.setter
    def GPIO_PIN25_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN25_INT_ENA_msb, self.__GPIO_PIN25_INT_ENA_lsb, value)

    @property
    def GPIO_PIN25_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN25_CONFIG_msb, self.__GPIO_PIN25_CONFIG_lsb)
    @GPIO_PIN25_CONFIG.setter
    def GPIO_PIN25_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN25_CONFIG_msb, self.__GPIO_PIN25_CONFIG_lsb, value)

    @property
    def GPIO_PIN25_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN25_WAKEUP_ENABLE_msb, self.__GPIO_PIN25_WAKEUP_ENABLE_lsb)
    @GPIO_PIN25_WAKEUP_ENABLE.setter
    def GPIO_PIN25_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN25_WAKEUP_ENABLE_msb, self.__GPIO_PIN25_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN25_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN25_INT_TYPE_msb, self.__GPIO_PIN25_INT_TYPE_lsb)
    @GPIO_PIN25_INT_TYPE.setter
    def GPIO_PIN25_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN25_INT_TYPE_msb, self.__GPIO_PIN25_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN25_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN25_PAD_DRIVER_msb, self.__GPIO_PIN25_PAD_DRIVER_lsb)
    @GPIO_PIN25_PAD_DRIVER.setter
    def GPIO_PIN25_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN25_PAD_DRIVER_msb, self.__GPIO_PIN25_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN25_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN25_SYNC_BYPASS_msb, self.__GPIO_PIN25_SYNC_BYPASS_lsb)
    @GPIO_PIN25_SYNC_BYPASS.setter
    def GPIO_PIN25_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN25_SYNC_BYPASS_msb, self.__GPIO_PIN25_SYNC_BYPASS_lsb, value)
class GPIO_PIN26(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0xf0
        self.__GPIO_PIN26_INT_ENA_lsb = 13
        self.__GPIO_PIN26_INT_ENA_msb = 17
        self.__GPIO_PIN26_CONFIG_lsb = 11
        self.__GPIO_PIN26_CONFIG_msb = 12
        self.__GPIO_PIN26_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN26_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN26_INT_TYPE_lsb = 7
        self.__GPIO_PIN26_INT_TYPE_msb = 9
        self.__GPIO_PIN26_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN26_PAD_DRIVER_msb = 2
        self.__GPIO_PIN26_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN26_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN26_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN26_INT_ENA_msb, self.__GPIO_PIN26_INT_ENA_lsb)
    @GPIO_PIN26_INT_ENA.setter
    def GPIO_PIN26_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN26_INT_ENA_msb, self.__GPIO_PIN26_INT_ENA_lsb, value)

    @property
    def GPIO_PIN26_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN26_CONFIG_msb, self.__GPIO_PIN26_CONFIG_lsb)
    @GPIO_PIN26_CONFIG.setter
    def GPIO_PIN26_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN26_CONFIG_msb, self.__GPIO_PIN26_CONFIG_lsb, value)

    @property
    def GPIO_PIN26_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN26_WAKEUP_ENABLE_msb, self.__GPIO_PIN26_WAKEUP_ENABLE_lsb)
    @GPIO_PIN26_WAKEUP_ENABLE.setter
    def GPIO_PIN26_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN26_WAKEUP_ENABLE_msb, self.__GPIO_PIN26_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN26_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN26_INT_TYPE_msb, self.__GPIO_PIN26_INT_TYPE_lsb)
    @GPIO_PIN26_INT_TYPE.setter
    def GPIO_PIN26_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN26_INT_TYPE_msb, self.__GPIO_PIN26_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN26_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN26_PAD_DRIVER_msb, self.__GPIO_PIN26_PAD_DRIVER_lsb)
    @GPIO_PIN26_PAD_DRIVER.setter
    def GPIO_PIN26_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN26_PAD_DRIVER_msb, self.__GPIO_PIN26_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN26_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN26_SYNC_BYPASS_msb, self.__GPIO_PIN26_SYNC_BYPASS_lsb)
    @GPIO_PIN26_SYNC_BYPASS.setter
    def GPIO_PIN26_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN26_SYNC_BYPASS_msb, self.__GPIO_PIN26_SYNC_BYPASS_lsb, value)
class GPIO_PIN27(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0xf4
        self.__GPIO_PIN27_INT_ENA_lsb = 13
        self.__GPIO_PIN27_INT_ENA_msb = 17
        self.__GPIO_PIN27_CONFIG_lsb = 11
        self.__GPIO_PIN27_CONFIG_msb = 12
        self.__GPIO_PIN27_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN27_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN27_INT_TYPE_lsb = 7
        self.__GPIO_PIN27_INT_TYPE_msb = 9
        self.__GPIO_PIN27_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN27_PAD_DRIVER_msb = 2
        self.__GPIO_PIN27_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN27_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN27_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN27_INT_ENA_msb, self.__GPIO_PIN27_INT_ENA_lsb)
    @GPIO_PIN27_INT_ENA.setter
    def GPIO_PIN27_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN27_INT_ENA_msb, self.__GPIO_PIN27_INT_ENA_lsb, value)

    @property
    def GPIO_PIN27_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN27_CONFIG_msb, self.__GPIO_PIN27_CONFIG_lsb)
    @GPIO_PIN27_CONFIG.setter
    def GPIO_PIN27_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN27_CONFIG_msb, self.__GPIO_PIN27_CONFIG_lsb, value)

    @property
    def GPIO_PIN27_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN27_WAKEUP_ENABLE_msb, self.__GPIO_PIN27_WAKEUP_ENABLE_lsb)
    @GPIO_PIN27_WAKEUP_ENABLE.setter
    def GPIO_PIN27_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN27_WAKEUP_ENABLE_msb, self.__GPIO_PIN27_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN27_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN27_INT_TYPE_msb, self.__GPIO_PIN27_INT_TYPE_lsb)
    @GPIO_PIN27_INT_TYPE.setter
    def GPIO_PIN27_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN27_INT_TYPE_msb, self.__GPIO_PIN27_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN27_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN27_PAD_DRIVER_msb, self.__GPIO_PIN27_PAD_DRIVER_lsb)
    @GPIO_PIN27_PAD_DRIVER.setter
    def GPIO_PIN27_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN27_PAD_DRIVER_msb, self.__GPIO_PIN27_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN27_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN27_SYNC_BYPASS_msb, self.__GPIO_PIN27_SYNC_BYPASS_lsb)
    @GPIO_PIN27_SYNC_BYPASS.setter
    def GPIO_PIN27_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN27_SYNC_BYPASS_msb, self.__GPIO_PIN27_SYNC_BYPASS_lsb, value)
class GPIO_PIN28(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0xf8
        self.__GPIO_PIN28_INT_ENA_lsb = 13
        self.__GPIO_PIN28_INT_ENA_msb = 17
        self.__GPIO_PIN28_CONFIG_lsb = 11
        self.__GPIO_PIN28_CONFIG_msb = 12
        self.__GPIO_PIN28_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN28_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN28_INT_TYPE_lsb = 7
        self.__GPIO_PIN28_INT_TYPE_msb = 9
        self.__GPIO_PIN28_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN28_PAD_DRIVER_msb = 2
        self.__GPIO_PIN28_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN28_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN28_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN28_INT_ENA_msb, self.__GPIO_PIN28_INT_ENA_lsb)
    @GPIO_PIN28_INT_ENA.setter
    def GPIO_PIN28_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN28_INT_ENA_msb, self.__GPIO_PIN28_INT_ENA_lsb, value)

    @property
    def GPIO_PIN28_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN28_CONFIG_msb, self.__GPIO_PIN28_CONFIG_lsb)
    @GPIO_PIN28_CONFIG.setter
    def GPIO_PIN28_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN28_CONFIG_msb, self.__GPIO_PIN28_CONFIG_lsb, value)

    @property
    def GPIO_PIN28_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN28_WAKEUP_ENABLE_msb, self.__GPIO_PIN28_WAKEUP_ENABLE_lsb)
    @GPIO_PIN28_WAKEUP_ENABLE.setter
    def GPIO_PIN28_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN28_WAKEUP_ENABLE_msb, self.__GPIO_PIN28_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN28_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN28_INT_TYPE_msb, self.__GPIO_PIN28_INT_TYPE_lsb)
    @GPIO_PIN28_INT_TYPE.setter
    def GPIO_PIN28_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN28_INT_TYPE_msb, self.__GPIO_PIN28_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN28_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN28_PAD_DRIVER_msb, self.__GPIO_PIN28_PAD_DRIVER_lsb)
    @GPIO_PIN28_PAD_DRIVER.setter
    def GPIO_PIN28_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN28_PAD_DRIVER_msb, self.__GPIO_PIN28_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN28_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN28_SYNC_BYPASS_msb, self.__GPIO_PIN28_SYNC_BYPASS_lsb)
    @GPIO_PIN28_SYNC_BYPASS.setter
    def GPIO_PIN28_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN28_SYNC_BYPASS_msb, self.__GPIO_PIN28_SYNC_BYPASS_lsb, value)
class GPIO_PIN29(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0xfc
        self.__GPIO_PIN29_INT_ENA_lsb = 13
        self.__GPIO_PIN29_INT_ENA_msb = 17
        self.__GPIO_PIN29_CONFIG_lsb = 11
        self.__GPIO_PIN29_CONFIG_msb = 12
        self.__GPIO_PIN29_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN29_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN29_INT_TYPE_lsb = 7
        self.__GPIO_PIN29_INT_TYPE_msb = 9
        self.__GPIO_PIN29_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN29_PAD_DRIVER_msb = 2
        self.__GPIO_PIN29_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN29_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN29_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN29_INT_ENA_msb, self.__GPIO_PIN29_INT_ENA_lsb)
    @GPIO_PIN29_INT_ENA.setter
    def GPIO_PIN29_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN29_INT_ENA_msb, self.__GPIO_PIN29_INT_ENA_lsb, value)

    @property
    def GPIO_PIN29_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN29_CONFIG_msb, self.__GPIO_PIN29_CONFIG_lsb)
    @GPIO_PIN29_CONFIG.setter
    def GPIO_PIN29_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN29_CONFIG_msb, self.__GPIO_PIN29_CONFIG_lsb, value)

    @property
    def GPIO_PIN29_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN29_WAKEUP_ENABLE_msb, self.__GPIO_PIN29_WAKEUP_ENABLE_lsb)
    @GPIO_PIN29_WAKEUP_ENABLE.setter
    def GPIO_PIN29_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN29_WAKEUP_ENABLE_msb, self.__GPIO_PIN29_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN29_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN29_INT_TYPE_msb, self.__GPIO_PIN29_INT_TYPE_lsb)
    @GPIO_PIN29_INT_TYPE.setter
    def GPIO_PIN29_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN29_INT_TYPE_msb, self.__GPIO_PIN29_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN29_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN29_PAD_DRIVER_msb, self.__GPIO_PIN29_PAD_DRIVER_lsb)
    @GPIO_PIN29_PAD_DRIVER.setter
    def GPIO_PIN29_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN29_PAD_DRIVER_msb, self.__GPIO_PIN29_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN29_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN29_SYNC_BYPASS_msb, self.__GPIO_PIN29_SYNC_BYPASS_lsb)
    @GPIO_PIN29_SYNC_BYPASS.setter
    def GPIO_PIN29_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN29_SYNC_BYPASS_msb, self.__GPIO_PIN29_SYNC_BYPASS_lsb, value)
class GPIO_PIN30(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x100
        self.__GPIO_PIN30_INT_ENA_lsb = 13
        self.__GPIO_PIN30_INT_ENA_msb = 17
        self.__GPIO_PIN30_CONFIG_lsb = 11
        self.__GPIO_PIN30_CONFIG_msb = 12
        self.__GPIO_PIN30_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN30_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN30_INT_TYPE_lsb = 7
        self.__GPIO_PIN30_INT_TYPE_msb = 9
        self.__GPIO_PIN30_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN30_PAD_DRIVER_msb = 2
        self.__GPIO_PIN30_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN30_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN30_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN30_INT_ENA_msb, self.__GPIO_PIN30_INT_ENA_lsb)
    @GPIO_PIN30_INT_ENA.setter
    def GPIO_PIN30_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN30_INT_ENA_msb, self.__GPIO_PIN30_INT_ENA_lsb, value)

    @property
    def GPIO_PIN30_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN30_CONFIG_msb, self.__GPIO_PIN30_CONFIG_lsb)
    @GPIO_PIN30_CONFIG.setter
    def GPIO_PIN30_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN30_CONFIG_msb, self.__GPIO_PIN30_CONFIG_lsb, value)

    @property
    def GPIO_PIN30_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN30_WAKEUP_ENABLE_msb, self.__GPIO_PIN30_WAKEUP_ENABLE_lsb)
    @GPIO_PIN30_WAKEUP_ENABLE.setter
    def GPIO_PIN30_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN30_WAKEUP_ENABLE_msb, self.__GPIO_PIN30_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN30_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN30_INT_TYPE_msb, self.__GPIO_PIN30_INT_TYPE_lsb)
    @GPIO_PIN30_INT_TYPE.setter
    def GPIO_PIN30_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN30_INT_TYPE_msb, self.__GPIO_PIN30_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN30_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN30_PAD_DRIVER_msb, self.__GPIO_PIN30_PAD_DRIVER_lsb)
    @GPIO_PIN30_PAD_DRIVER.setter
    def GPIO_PIN30_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN30_PAD_DRIVER_msb, self.__GPIO_PIN30_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN30_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN30_SYNC_BYPASS_msb, self.__GPIO_PIN30_SYNC_BYPASS_lsb)
    @GPIO_PIN30_SYNC_BYPASS.setter
    def GPIO_PIN30_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN30_SYNC_BYPASS_msb, self.__GPIO_PIN30_SYNC_BYPASS_lsb, value)
class GPIO_PIN31(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x104
        self.__GPIO_PIN31_INT_ENA_lsb = 13
        self.__GPIO_PIN31_INT_ENA_msb = 17
        self.__GPIO_PIN31_CONFIG_lsb = 11
        self.__GPIO_PIN31_CONFIG_msb = 12
        self.__GPIO_PIN31_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN31_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN31_INT_TYPE_lsb = 7
        self.__GPIO_PIN31_INT_TYPE_msb = 9
        self.__GPIO_PIN31_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN31_PAD_DRIVER_msb = 2
        self.__GPIO_PIN31_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN31_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN31_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN31_INT_ENA_msb, self.__GPIO_PIN31_INT_ENA_lsb)
    @GPIO_PIN31_INT_ENA.setter
    def GPIO_PIN31_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN31_INT_ENA_msb, self.__GPIO_PIN31_INT_ENA_lsb, value)

    @property
    def GPIO_PIN31_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN31_CONFIG_msb, self.__GPIO_PIN31_CONFIG_lsb)
    @GPIO_PIN31_CONFIG.setter
    def GPIO_PIN31_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN31_CONFIG_msb, self.__GPIO_PIN31_CONFIG_lsb, value)

    @property
    def GPIO_PIN31_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN31_WAKEUP_ENABLE_msb, self.__GPIO_PIN31_WAKEUP_ENABLE_lsb)
    @GPIO_PIN31_WAKEUP_ENABLE.setter
    def GPIO_PIN31_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN31_WAKEUP_ENABLE_msb, self.__GPIO_PIN31_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN31_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN31_INT_TYPE_msb, self.__GPIO_PIN31_INT_TYPE_lsb)
    @GPIO_PIN31_INT_TYPE.setter
    def GPIO_PIN31_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN31_INT_TYPE_msb, self.__GPIO_PIN31_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN31_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN31_PAD_DRIVER_msb, self.__GPIO_PIN31_PAD_DRIVER_lsb)
    @GPIO_PIN31_PAD_DRIVER.setter
    def GPIO_PIN31_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN31_PAD_DRIVER_msb, self.__GPIO_PIN31_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN31_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN31_SYNC_BYPASS_msb, self.__GPIO_PIN31_SYNC_BYPASS_lsb)
    @GPIO_PIN31_SYNC_BYPASS.setter
    def GPIO_PIN31_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN31_SYNC_BYPASS_msb, self.__GPIO_PIN31_SYNC_BYPASS_lsb, value)
class GPIO_PIN32(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x108
        self.__GPIO_PIN32_INT_ENA_lsb = 13
        self.__GPIO_PIN32_INT_ENA_msb = 17
        self.__GPIO_PIN32_CONFIG_lsb = 11
        self.__GPIO_PIN32_CONFIG_msb = 12
        self.__GPIO_PIN32_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN32_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN32_INT_TYPE_lsb = 7
        self.__GPIO_PIN32_INT_TYPE_msb = 9
        self.__GPIO_PIN32_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN32_PAD_DRIVER_msb = 2
        self.__GPIO_PIN32_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN32_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN32_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN32_INT_ENA_msb, self.__GPIO_PIN32_INT_ENA_lsb)
    @GPIO_PIN32_INT_ENA.setter
    def GPIO_PIN32_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN32_INT_ENA_msb, self.__GPIO_PIN32_INT_ENA_lsb, value)

    @property
    def GPIO_PIN32_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN32_CONFIG_msb, self.__GPIO_PIN32_CONFIG_lsb)
    @GPIO_PIN32_CONFIG.setter
    def GPIO_PIN32_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN32_CONFIG_msb, self.__GPIO_PIN32_CONFIG_lsb, value)

    @property
    def GPIO_PIN32_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN32_WAKEUP_ENABLE_msb, self.__GPIO_PIN32_WAKEUP_ENABLE_lsb)
    @GPIO_PIN32_WAKEUP_ENABLE.setter
    def GPIO_PIN32_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN32_WAKEUP_ENABLE_msb, self.__GPIO_PIN32_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN32_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN32_INT_TYPE_msb, self.__GPIO_PIN32_INT_TYPE_lsb)
    @GPIO_PIN32_INT_TYPE.setter
    def GPIO_PIN32_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN32_INT_TYPE_msb, self.__GPIO_PIN32_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN32_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN32_PAD_DRIVER_msb, self.__GPIO_PIN32_PAD_DRIVER_lsb)
    @GPIO_PIN32_PAD_DRIVER.setter
    def GPIO_PIN32_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN32_PAD_DRIVER_msb, self.__GPIO_PIN32_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN32_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN32_SYNC_BYPASS_msb, self.__GPIO_PIN32_SYNC_BYPASS_lsb)
    @GPIO_PIN32_SYNC_BYPASS.setter
    def GPIO_PIN32_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN32_SYNC_BYPASS_msb, self.__GPIO_PIN32_SYNC_BYPASS_lsb, value)
class GPIO_PIN33(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x10c
        self.__GPIO_PIN33_INT_ENA_lsb = 13
        self.__GPIO_PIN33_INT_ENA_msb = 17
        self.__GPIO_PIN33_CONFIG_lsb = 11
        self.__GPIO_PIN33_CONFIG_msb = 12
        self.__GPIO_PIN33_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN33_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN33_INT_TYPE_lsb = 7
        self.__GPIO_PIN33_INT_TYPE_msb = 9
        self.__GPIO_PIN33_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN33_PAD_DRIVER_msb = 2
        self.__GPIO_PIN33_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN33_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN33_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN33_INT_ENA_msb, self.__GPIO_PIN33_INT_ENA_lsb)
    @GPIO_PIN33_INT_ENA.setter
    def GPIO_PIN33_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN33_INT_ENA_msb, self.__GPIO_PIN33_INT_ENA_lsb, value)

    @property
    def GPIO_PIN33_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN33_CONFIG_msb, self.__GPIO_PIN33_CONFIG_lsb)
    @GPIO_PIN33_CONFIG.setter
    def GPIO_PIN33_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN33_CONFIG_msb, self.__GPIO_PIN33_CONFIG_lsb, value)

    @property
    def GPIO_PIN33_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN33_WAKEUP_ENABLE_msb, self.__GPIO_PIN33_WAKEUP_ENABLE_lsb)
    @GPIO_PIN33_WAKEUP_ENABLE.setter
    def GPIO_PIN33_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN33_WAKEUP_ENABLE_msb, self.__GPIO_PIN33_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN33_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN33_INT_TYPE_msb, self.__GPIO_PIN33_INT_TYPE_lsb)
    @GPIO_PIN33_INT_TYPE.setter
    def GPIO_PIN33_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN33_INT_TYPE_msb, self.__GPIO_PIN33_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN33_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN33_PAD_DRIVER_msb, self.__GPIO_PIN33_PAD_DRIVER_lsb)
    @GPIO_PIN33_PAD_DRIVER.setter
    def GPIO_PIN33_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN33_PAD_DRIVER_msb, self.__GPIO_PIN33_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN33_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN33_SYNC_BYPASS_msb, self.__GPIO_PIN33_SYNC_BYPASS_lsb)
    @GPIO_PIN33_SYNC_BYPASS.setter
    def GPIO_PIN33_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN33_SYNC_BYPASS_msb, self.__GPIO_PIN33_SYNC_BYPASS_lsb, value)
class GPIO_PIN34(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x110
        self.__GPIO_PIN34_INT_ENA_lsb = 13
        self.__GPIO_PIN34_INT_ENA_msb = 17
        self.__GPIO_PIN34_CONFIG_lsb = 11
        self.__GPIO_PIN34_CONFIG_msb = 12
        self.__GPIO_PIN34_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN34_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN34_INT_TYPE_lsb = 7
        self.__GPIO_PIN34_INT_TYPE_msb = 9
        self.__GPIO_PIN34_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN34_PAD_DRIVER_msb = 2
        self.__GPIO_PIN34_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN34_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN34_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN34_INT_ENA_msb, self.__GPIO_PIN34_INT_ENA_lsb)
    @GPIO_PIN34_INT_ENA.setter
    def GPIO_PIN34_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN34_INT_ENA_msb, self.__GPIO_PIN34_INT_ENA_lsb, value)

    @property
    def GPIO_PIN34_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN34_CONFIG_msb, self.__GPIO_PIN34_CONFIG_lsb)
    @GPIO_PIN34_CONFIG.setter
    def GPIO_PIN34_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN34_CONFIG_msb, self.__GPIO_PIN34_CONFIG_lsb, value)

    @property
    def GPIO_PIN34_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN34_WAKEUP_ENABLE_msb, self.__GPIO_PIN34_WAKEUP_ENABLE_lsb)
    @GPIO_PIN34_WAKEUP_ENABLE.setter
    def GPIO_PIN34_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN34_WAKEUP_ENABLE_msb, self.__GPIO_PIN34_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN34_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN34_INT_TYPE_msb, self.__GPIO_PIN34_INT_TYPE_lsb)
    @GPIO_PIN34_INT_TYPE.setter
    def GPIO_PIN34_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN34_INT_TYPE_msb, self.__GPIO_PIN34_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN34_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN34_PAD_DRIVER_msb, self.__GPIO_PIN34_PAD_DRIVER_lsb)
    @GPIO_PIN34_PAD_DRIVER.setter
    def GPIO_PIN34_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN34_PAD_DRIVER_msb, self.__GPIO_PIN34_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN34_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN34_SYNC_BYPASS_msb, self.__GPIO_PIN34_SYNC_BYPASS_lsb)
    @GPIO_PIN34_SYNC_BYPASS.setter
    def GPIO_PIN34_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN34_SYNC_BYPASS_msb, self.__GPIO_PIN34_SYNC_BYPASS_lsb, value)
class GPIO_PIN35(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x114
        self.__GPIO_PIN35_INT_ENA_lsb = 13
        self.__GPIO_PIN35_INT_ENA_msb = 17
        self.__GPIO_PIN35_CONFIG_lsb = 11
        self.__GPIO_PIN35_CONFIG_msb = 12
        self.__GPIO_PIN35_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN35_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN35_INT_TYPE_lsb = 7
        self.__GPIO_PIN35_INT_TYPE_msb = 9
        self.__GPIO_PIN35_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN35_PAD_DRIVER_msb = 2
        self.__GPIO_PIN35_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN35_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN35_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN35_INT_ENA_msb, self.__GPIO_PIN35_INT_ENA_lsb)
    @GPIO_PIN35_INT_ENA.setter
    def GPIO_PIN35_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN35_INT_ENA_msb, self.__GPIO_PIN35_INT_ENA_lsb, value)

    @property
    def GPIO_PIN35_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN35_CONFIG_msb, self.__GPIO_PIN35_CONFIG_lsb)
    @GPIO_PIN35_CONFIG.setter
    def GPIO_PIN35_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN35_CONFIG_msb, self.__GPIO_PIN35_CONFIG_lsb, value)

    @property
    def GPIO_PIN35_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN35_WAKEUP_ENABLE_msb, self.__GPIO_PIN35_WAKEUP_ENABLE_lsb)
    @GPIO_PIN35_WAKEUP_ENABLE.setter
    def GPIO_PIN35_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN35_WAKEUP_ENABLE_msb, self.__GPIO_PIN35_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN35_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN35_INT_TYPE_msb, self.__GPIO_PIN35_INT_TYPE_lsb)
    @GPIO_PIN35_INT_TYPE.setter
    def GPIO_PIN35_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN35_INT_TYPE_msb, self.__GPIO_PIN35_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN35_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN35_PAD_DRIVER_msb, self.__GPIO_PIN35_PAD_DRIVER_lsb)
    @GPIO_PIN35_PAD_DRIVER.setter
    def GPIO_PIN35_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN35_PAD_DRIVER_msb, self.__GPIO_PIN35_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN35_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN35_SYNC_BYPASS_msb, self.__GPIO_PIN35_SYNC_BYPASS_lsb)
    @GPIO_PIN35_SYNC_BYPASS.setter
    def GPIO_PIN35_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN35_SYNC_BYPASS_msb, self.__GPIO_PIN35_SYNC_BYPASS_lsb, value)
class GPIO_PIN36(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x118
        self.__GPIO_PIN36_INT_ENA_lsb = 13
        self.__GPIO_PIN36_INT_ENA_msb = 17
        self.__GPIO_PIN36_CONFIG_lsb = 11
        self.__GPIO_PIN36_CONFIG_msb = 12
        self.__GPIO_PIN36_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN36_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN36_INT_TYPE_lsb = 7
        self.__GPIO_PIN36_INT_TYPE_msb = 9
        self.__GPIO_PIN36_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN36_PAD_DRIVER_msb = 2
        self.__GPIO_PIN36_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN36_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN36_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN36_INT_ENA_msb, self.__GPIO_PIN36_INT_ENA_lsb)
    @GPIO_PIN36_INT_ENA.setter
    def GPIO_PIN36_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN36_INT_ENA_msb, self.__GPIO_PIN36_INT_ENA_lsb, value)

    @property
    def GPIO_PIN36_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN36_CONFIG_msb, self.__GPIO_PIN36_CONFIG_lsb)
    @GPIO_PIN36_CONFIG.setter
    def GPIO_PIN36_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN36_CONFIG_msb, self.__GPIO_PIN36_CONFIG_lsb, value)

    @property
    def GPIO_PIN36_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN36_WAKEUP_ENABLE_msb, self.__GPIO_PIN36_WAKEUP_ENABLE_lsb)
    @GPIO_PIN36_WAKEUP_ENABLE.setter
    def GPIO_PIN36_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN36_WAKEUP_ENABLE_msb, self.__GPIO_PIN36_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN36_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN36_INT_TYPE_msb, self.__GPIO_PIN36_INT_TYPE_lsb)
    @GPIO_PIN36_INT_TYPE.setter
    def GPIO_PIN36_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN36_INT_TYPE_msb, self.__GPIO_PIN36_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN36_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN36_PAD_DRIVER_msb, self.__GPIO_PIN36_PAD_DRIVER_lsb)
    @GPIO_PIN36_PAD_DRIVER.setter
    def GPIO_PIN36_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN36_PAD_DRIVER_msb, self.__GPIO_PIN36_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN36_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN36_SYNC_BYPASS_msb, self.__GPIO_PIN36_SYNC_BYPASS_lsb)
    @GPIO_PIN36_SYNC_BYPASS.setter
    def GPIO_PIN36_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN36_SYNC_BYPASS_msb, self.__GPIO_PIN36_SYNC_BYPASS_lsb, value)
class GPIO_PIN37(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x11c
        self.__GPIO_PIN37_INT_ENA_lsb = 13
        self.__GPIO_PIN37_INT_ENA_msb = 17
        self.__GPIO_PIN37_CONFIG_lsb = 11
        self.__GPIO_PIN37_CONFIG_msb = 12
        self.__GPIO_PIN37_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN37_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN37_INT_TYPE_lsb = 7
        self.__GPIO_PIN37_INT_TYPE_msb = 9
        self.__GPIO_PIN37_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN37_PAD_DRIVER_msb = 2
        self.__GPIO_PIN37_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN37_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN37_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN37_INT_ENA_msb, self.__GPIO_PIN37_INT_ENA_lsb)
    @GPIO_PIN37_INT_ENA.setter
    def GPIO_PIN37_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN37_INT_ENA_msb, self.__GPIO_PIN37_INT_ENA_lsb, value)

    @property
    def GPIO_PIN37_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN37_CONFIG_msb, self.__GPIO_PIN37_CONFIG_lsb)
    @GPIO_PIN37_CONFIG.setter
    def GPIO_PIN37_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN37_CONFIG_msb, self.__GPIO_PIN37_CONFIG_lsb, value)

    @property
    def GPIO_PIN37_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN37_WAKEUP_ENABLE_msb, self.__GPIO_PIN37_WAKEUP_ENABLE_lsb)
    @GPIO_PIN37_WAKEUP_ENABLE.setter
    def GPIO_PIN37_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN37_WAKEUP_ENABLE_msb, self.__GPIO_PIN37_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN37_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN37_INT_TYPE_msb, self.__GPIO_PIN37_INT_TYPE_lsb)
    @GPIO_PIN37_INT_TYPE.setter
    def GPIO_PIN37_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN37_INT_TYPE_msb, self.__GPIO_PIN37_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN37_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN37_PAD_DRIVER_msb, self.__GPIO_PIN37_PAD_DRIVER_lsb)
    @GPIO_PIN37_PAD_DRIVER.setter
    def GPIO_PIN37_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN37_PAD_DRIVER_msb, self.__GPIO_PIN37_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN37_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN37_SYNC_BYPASS_msb, self.__GPIO_PIN37_SYNC_BYPASS_lsb)
    @GPIO_PIN37_SYNC_BYPASS.setter
    def GPIO_PIN37_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN37_SYNC_BYPASS_msb, self.__GPIO_PIN37_SYNC_BYPASS_lsb, value)
class GPIO_PIN38(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x120
        self.__GPIO_PIN38_INT_ENA_lsb = 13
        self.__GPIO_PIN38_INT_ENA_msb = 17
        self.__GPIO_PIN38_CONFIG_lsb = 11
        self.__GPIO_PIN38_CONFIG_msb = 12
        self.__GPIO_PIN38_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN38_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN38_INT_TYPE_lsb = 7
        self.__GPIO_PIN38_INT_TYPE_msb = 9
        self.__GPIO_PIN38_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN38_PAD_DRIVER_msb = 2
        self.__GPIO_PIN38_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN38_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN38_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN38_INT_ENA_msb, self.__GPIO_PIN38_INT_ENA_lsb)
    @GPIO_PIN38_INT_ENA.setter
    def GPIO_PIN38_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN38_INT_ENA_msb, self.__GPIO_PIN38_INT_ENA_lsb, value)

    @property
    def GPIO_PIN38_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN38_CONFIG_msb, self.__GPIO_PIN38_CONFIG_lsb)
    @GPIO_PIN38_CONFIG.setter
    def GPIO_PIN38_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN38_CONFIG_msb, self.__GPIO_PIN38_CONFIG_lsb, value)

    @property
    def GPIO_PIN38_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN38_WAKEUP_ENABLE_msb, self.__GPIO_PIN38_WAKEUP_ENABLE_lsb)
    @GPIO_PIN38_WAKEUP_ENABLE.setter
    def GPIO_PIN38_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN38_WAKEUP_ENABLE_msb, self.__GPIO_PIN38_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN38_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN38_INT_TYPE_msb, self.__GPIO_PIN38_INT_TYPE_lsb)
    @GPIO_PIN38_INT_TYPE.setter
    def GPIO_PIN38_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN38_INT_TYPE_msb, self.__GPIO_PIN38_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN38_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN38_PAD_DRIVER_msb, self.__GPIO_PIN38_PAD_DRIVER_lsb)
    @GPIO_PIN38_PAD_DRIVER.setter
    def GPIO_PIN38_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN38_PAD_DRIVER_msb, self.__GPIO_PIN38_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN38_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN38_SYNC_BYPASS_msb, self.__GPIO_PIN38_SYNC_BYPASS_lsb)
    @GPIO_PIN38_SYNC_BYPASS.setter
    def GPIO_PIN38_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN38_SYNC_BYPASS_msb, self.__GPIO_PIN38_SYNC_BYPASS_lsb, value)
class GPIO_PIN39(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x124
        self.__GPIO_PIN39_INT_ENA_lsb = 13
        self.__GPIO_PIN39_INT_ENA_msb = 17
        self.__GPIO_PIN39_CONFIG_lsb = 11
        self.__GPIO_PIN39_CONFIG_msb = 12
        self.__GPIO_PIN39_WAKEUP_ENABLE_lsb = 10
        self.__GPIO_PIN39_WAKEUP_ENABLE_msb = 10
        self.__GPIO_PIN39_INT_TYPE_lsb = 7
        self.__GPIO_PIN39_INT_TYPE_msb = 9
        self.__GPIO_PIN39_PAD_DRIVER_lsb = 2
        self.__GPIO_PIN39_PAD_DRIVER_msb = 2
        self.__GPIO_PIN39_SYNC_BYPASS_lsb = 0
        self.__GPIO_PIN39_SYNC_BYPASS_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_PIN39_INT_ENA(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN39_INT_ENA_msb, self.__GPIO_PIN39_INT_ENA_lsb)
    @GPIO_PIN39_INT_ENA.setter
    def GPIO_PIN39_INT_ENA(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN39_INT_ENA_msb, self.__GPIO_PIN39_INT_ENA_lsb, value)

    @property
    def GPIO_PIN39_CONFIG(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN39_CONFIG_msb, self.__GPIO_PIN39_CONFIG_lsb)
    @GPIO_PIN39_CONFIG.setter
    def GPIO_PIN39_CONFIG(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN39_CONFIG_msb, self.__GPIO_PIN39_CONFIG_lsb, value)

    @property
    def GPIO_PIN39_WAKEUP_ENABLE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN39_WAKEUP_ENABLE_msb, self.__GPIO_PIN39_WAKEUP_ENABLE_lsb)
    @GPIO_PIN39_WAKEUP_ENABLE.setter
    def GPIO_PIN39_WAKEUP_ENABLE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN39_WAKEUP_ENABLE_msb, self.__GPIO_PIN39_WAKEUP_ENABLE_lsb, value)

    @property
    def GPIO_PIN39_INT_TYPE(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN39_INT_TYPE_msb, self.__GPIO_PIN39_INT_TYPE_lsb)
    @GPIO_PIN39_INT_TYPE.setter
    def GPIO_PIN39_INT_TYPE(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN39_INT_TYPE_msb, self.__GPIO_PIN39_INT_TYPE_lsb, value)

    @property
    def GPIO_PIN39_PAD_DRIVER(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN39_PAD_DRIVER_msb, self.__GPIO_PIN39_PAD_DRIVER_lsb)
    @GPIO_PIN39_PAD_DRIVER.setter
    def GPIO_PIN39_PAD_DRIVER(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN39_PAD_DRIVER_msb, self.__GPIO_PIN39_PAD_DRIVER_lsb, value)

    @property
    def GPIO_PIN39_SYNC_BYPASS(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_PIN39_SYNC_BYPASS_msb, self.__GPIO_PIN39_SYNC_BYPASS_lsb)
    @GPIO_PIN39_SYNC_BYPASS.setter
    def GPIO_PIN39_SYNC_BYPASS(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_PIN39_SYNC_BYPASS_msb, self.__GPIO_PIN39_SYNC_BYPASS_lsb, value)
class cali_conf(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x128
        self.__cali_start_lsb = 31
        self.__cali_start_msb = 31
        self.__cali_rtc_max_lsb = 0
        self.__cali_rtc_max_msb = 9
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def cali_start(self):
        return self.__MEM.rdm(self.__addr, self.__cali_start_msb, self.__cali_start_lsb)
    @cali_start.setter
    def cali_start(self, value):
        return self.__MEM.wrm(self.__addr, self.__cali_start_msb, self.__cali_start_lsb, value)

    @property
    def cali_rtc_max(self):
        return self.__MEM.rdm(self.__addr, self.__cali_rtc_max_msb, self.__cali_rtc_max_lsb)
    @cali_rtc_max.setter
    def cali_rtc_max(self, value):
        return self.__MEM.wrm(self.__addr, self.__cali_rtc_max_msb, self.__cali_rtc_max_lsb, value)
class cali_data(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x12c
        self.__cali_rdy_sync2_lsb = 31
        self.__cali_rdy_sync2_msb = 31
        self.__cali_rdy_real_lsb = 30
        self.__cali_rdy_real_msb = 30
        self.__cali_value_sync2_lsb = 0
        self.__cali_value_sync2_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def cali_rdy_sync2(self):
        return self.__MEM.rdm(self.__addr, self.__cali_rdy_sync2_msb, self.__cali_rdy_sync2_lsb)
    @cali_rdy_sync2.setter
    def cali_rdy_sync2(self, value):
        return self.__MEM.wrm(self.__addr, self.__cali_rdy_sync2_msb, self.__cali_rdy_sync2_lsb, value)

    @property
    def cali_rdy_real(self):
        return self.__MEM.rdm(self.__addr, self.__cali_rdy_real_msb, self.__cali_rdy_real_lsb)
    @cali_rdy_real.setter
    def cali_rdy_real(self, value):
        return self.__MEM.wrm(self.__addr, self.__cali_rdy_real_msb, self.__cali_rdy_real_lsb, value)

    @property
    def cali_value_sync2(self):
        return self.__MEM.rdm(self.__addr, self.__cali_value_sync2_msb, self.__cali_value_sync2_lsb)
    @cali_value_sync2.setter
    def cali_value_sync2(self, value):
        return self.__MEM.wrm(self.__addr, self.__cali_value_sync2_msb, self.__cali_value_sync2_lsb, value)
class GPIO_FUNC0_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x130
        self.__GPIO_SIG0_IN_SEL_lsb = 7
        self.__GPIO_SIG0_IN_SEL_msb = 7
        self.__GPIO_FUNC0_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC0_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC0_IN_SEL_lsb = 0
        self.__GPIO_FUNC0_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG0_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG0_IN_SEL_msb, self.__GPIO_SIG0_IN_SEL_lsb)
    @GPIO_SIG0_IN_SEL.setter
    def GPIO_SIG0_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG0_IN_SEL_msb, self.__GPIO_SIG0_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC0_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC0_IN_INV_SEL_msb, self.__GPIO_FUNC0_IN_INV_SEL_lsb)
    @GPIO_FUNC0_IN_INV_SEL.setter
    def GPIO_FUNC0_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC0_IN_INV_SEL_msb, self.__GPIO_FUNC0_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC0_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC0_IN_SEL_msb, self.__GPIO_FUNC0_IN_SEL_lsb)
    @GPIO_FUNC0_IN_SEL.setter
    def GPIO_FUNC0_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC0_IN_SEL_msb, self.__GPIO_FUNC0_IN_SEL_lsb, value)
class GPIO_FUNC1_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x134
        self.__GPIO_SIG1_IN_SEL_lsb = 7
        self.__GPIO_SIG1_IN_SEL_msb = 7
        self.__GPIO_FUNC1_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC1_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC1_IN_SEL_lsb = 0
        self.__GPIO_FUNC1_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG1_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG1_IN_SEL_msb, self.__GPIO_SIG1_IN_SEL_lsb)
    @GPIO_SIG1_IN_SEL.setter
    def GPIO_SIG1_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG1_IN_SEL_msb, self.__GPIO_SIG1_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC1_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC1_IN_INV_SEL_msb, self.__GPIO_FUNC1_IN_INV_SEL_lsb)
    @GPIO_FUNC1_IN_INV_SEL.setter
    def GPIO_FUNC1_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC1_IN_INV_SEL_msb, self.__GPIO_FUNC1_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC1_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC1_IN_SEL_msb, self.__GPIO_FUNC1_IN_SEL_lsb)
    @GPIO_FUNC1_IN_SEL.setter
    def GPIO_FUNC1_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC1_IN_SEL_msb, self.__GPIO_FUNC1_IN_SEL_lsb, value)
class GPIO_FUNC2_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x138
        self.__GPIO_SIG2_IN_SEL_lsb = 7
        self.__GPIO_SIG2_IN_SEL_msb = 7
        self.__GPIO_FUNC2_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC2_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC2_IN_SEL_lsb = 0
        self.__GPIO_FUNC2_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG2_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG2_IN_SEL_msb, self.__GPIO_SIG2_IN_SEL_lsb)
    @GPIO_SIG2_IN_SEL.setter
    def GPIO_SIG2_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG2_IN_SEL_msb, self.__GPIO_SIG2_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC2_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC2_IN_INV_SEL_msb, self.__GPIO_FUNC2_IN_INV_SEL_lsb)
    @GPIO_FUNC2_IN_INV_SEL.setter
    def GPIO_FUNC2_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC2_IN_INV_SEL_msb, self.__GPIO_FUNC2_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC2_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC2_IN_SEL_msb, self.__GPIO_FUNC2_IN_SEL_lsb)
    @GPIO_FUNC2_IN_SEL.setter
    def GPIO_FUNC2_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC2_IN_SEL_msb, self.__GPIO_FUNC2_IN_SEL_lsb, value)
class GPIO_FUNC3_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x13c
        self.__GPIO_SIG3_IN_SEL_lsb = 7
        self.__GPIO_SIG3_IN_SEL_msb = 7
        self.__GPIO_FUNC3_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC3_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC3_IN_SEL_lsb = 0
        self.__GPIO_FUNC3_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG3_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG3_IN_SEL_msb, self.__GPIO_SIG3_IN_SEL_lsb)
    @GPIO_SIG3_IN_SEL.setter
    def GPIO_SIG3_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG3_IN_SEL_msb, self.__GPIO_SIG3_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC3_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC3_IN_INV_SEL_msb, self.__GPIO_FUNC3_IN_INV_SEL_lsb)
    @GPIO_FUNC3_IN_INV_SEL.setter
    def GPIO_FUNC3_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC3_IN_INV_SEL_msb, self.__GPIO_FUNC3_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC3_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC3_IN_SEL_msb, self.__GPIO_FUNC3_IN_SEL_lsb)
    @GPIO_FUNC3_IN_SEL.setter
    def GPIO_FUNC3_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC3_IN_SEL_msb, self.__GPIO_FUNC3_IN_SEL_lsb, value)
class GPIO_FUNC4_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x140
        self.__GPIO_SIG4_IN_SEL_lsb = 7
        self.__GPIO_SIG4_IN_SEL_msb = 7
        self.__GPIO_FUNC4_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC4_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC4_IN_SEL_lsb = 0
        self.__GPIO_FUNC4_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG4_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG4_IN_SEL_msb, self.__GPIO_SIG4_IN_SEL_lsb)
    @GPIO_SIG4_IN_SEL.setter
    def GPIO_SIG4_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG4_IN_SEL_msb, self.__GPIO_SIG4_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC4_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC4_IN_INV_SEL_msb, self.__GPIO_FUNC4_IN_INV_SEL_lsb)
    @GPIO_FUNC4_IN_INV_SEL.setter
    def GPIO_FUNC4_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC4_IN_INV_SEL_msb, self.__GPIO_FUNC4_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC4_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC4_IN_SEL_msb, self.__GPIO_FUNC4_IN_SEL_lsb)
    @GPIO_FUNC4_IN_SEL.setter
    def GPIO_FUNC4_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC4_IN_SEL_msb, self.__GPIO_FUNC4_IN_SEL_lsb, value)
class GPIO_FUNC5_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x144
        self.__GPIO_SIG5_IN_SEL_lsb = 7
        self.__GPIO_SIG5_IN_SEL_msb = 7
        self.__GPIO_FUNC5_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC5_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC5_IN_SEL_lsb = 0
        self.__GPIO_FUNC5_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG5_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG5_IN_SEL_msb, self.__GPIO_SIG5_IN_SEL_lsb)
    @GPIO_SIG5_IN_SEL.setter
    def GPIO_SIG5_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG5_IN_SEL_msb, self.__GPIO_SIG5_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC5_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC5_IN_INV_SEL_msb, self.__GPIO_FUNC5_IN_INV_SEL_lsb)
    @GPIO_FUNC5_IN_INV_SEL.setter
    def GPIO_FUNC5_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC5_IN_INV_SEL_msb, self.__GPIO_FUNC5_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC5_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC5_IN_SEL_msb, self.__GPIO_FUNC5_IN_SEL_lsb)
    @GPIO_FUNC5_IN_SEL.setter
    def GPIO_FUNC5_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC5_IN_SEL_msb, self.__GPIO_FUNC5_IN_SEL_lsb, value)
class GPIO_FUNC6_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x148
        self.__GPIO_SIG6_IN_SEL_lsb = 7
        self.__GPIO_SIG6_IN_SEL_msb = 7
        self.__GPIO_FUNC6_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC6_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC6_IN_SEL_lsb = 0
        self.__GPIO_FUNC6_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG6_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG6_IN_SEL_msb, self.__GPIO_SIG6_IN_SEL_lsb)
    @GPIO_SIG6_IN_SEL.setter
    def GPIO_SIG6_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG6_IN_SEL_msb, self.__GPIO_SIG6_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC6_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC6_IN_INV_SEL_msb, self.__GPIO_FUNC6_IN_INV_SEL_lsb)
    @GPIO_FUNC6_IN_INV_SEL.setter
    def GPIO_FUNC6_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC6_IN_INV_SEL_msb, self.__GPIO_FUNC6_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC6_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC6_IN_SEL_msb, self.__GPIO_FUNC6_IN_SEL_lsb)
    @GPIO_FUNC6_IN_SEL.setter
    def GPIO_FUNC6_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC6_IN_SEL_msb, self.__GPIO_FUNC6_IN_SEL_lsb, value)
class GPIO_FUNC7_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x14c
        self.__GPIO_SIG7_IN_SEL_lsb = 7
        self.__GPIO_SIG7_IN_SEL_msb = 7
        self.__GPIO_FUNC7_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC7_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC7_IN_SEL_lsb = 0
        self.__GPIO_FUNC7_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG7_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG7_IN_SEL_msb, self.__GPIO_SIG7_IN_SEL_lsb)
    @GPIO_SIG7_IN_SEL.setter
    def GPIO_SIG7_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG7_IN_SEL_msb, self.__GPIO_SIG7_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC7_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC7_IN_INV_SEL_msb, self.__GPIO_FUNC7_IN_INV_SEL_lsb)
    @GPIO_FUNC7_IN_INV_SEL.setter
    def GPIO_FUNC7_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC7_IN_INV_SEL_msb, self.__GPIO_FUNC7_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC7_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC7_IN_SEL_msb, self.__GPIO_FUNC7_IN_SEL_lsb)
    @GPIO_FUNC7_IN_SEL.setter
    def GPIO_FUNC7_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC7_IN_SEL_msb, self.__GPIO_FUNC7_IN_SEL_lsb, value)
class GPIO_FUNC8_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x150
        self.__GPIO_SIG8_IN_SEL_lsb = 7
        self.__GPIO_SIG8_IN_SEL_msb = 7
        self.__GPIO_FUNC8_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC8_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC8_IN_SEL_lsb = 0
        self.__GPIO_FUNC8_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG8_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG8_IN_SEL_msb, self.__GPIO_SIG8_IN_SEL_lsb)
    @GPIO_SIG8_IN_SEL.setter
    def GPIO_SIG8_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG8_IN_SEL_msb, self.__GPIO_SIG8_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC8_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC8_IN_INV_SEL_msb, self.__GPIO_FUNC8_IN_INV_SEL_lsb)
    @GPIO_FUNC8_IN_INV_SEL.setter
    def GPIO_FUNC8_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC8_IN_INV_SEL_msb, self.__GPIO_FUNC8_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC8_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC8_IN_SEL_msb, self.__GPIO_FUNC8_IN_SEL_lsb)
    @GPIO_FUNC8_IN_SEL.setter
    def GPIO_FUNC8_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC8_IN_SEL_msb, self.__GPIO_FUNC8_IN_SEL_lsb, value)
class GPIO_FUNC9_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x154
        self.__GPIO_SIG9_IN_SEL_lsb = 7
        self.__GPIO_SIG9_IN_SEL_msb = 7
        self.__GPIO_FUNC9_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC9_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC9_IN_SEL_lsb = 0
        self.__GPIO_FUNC9_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG9_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG9_IN_SEL_msb, self.__GPIO_SIG9_IN_SEL_lsb)
    @GPIO_SIG9_IN_SEL.setter
    def GPIO_SIG9_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG9_IN_SEL_msb, self.__GPIO_SIG9_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC9_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC9_IN_INV_SEL_msb, self.__GPIO_FUNC9_IN_INV_SEL_lsb)
    @GPIO_FUNC9_IN_INV_SEL.setter
    def GPIO_FUNC9_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC9_IN_INV_SEL_msb, self.__GPIO_FUNC9_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC9_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC9_IN_SEL_msb, self.__GPIO_FUNC9_IN_SEL_lsb)
    @GPIO_FUNC9_IN_SEL.setter
    def GPIO_FUNC9_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC9_IN_SEL_msb, self.__GPIO_FUNC9_IN_SEL_lsb, value)
class GPIO_FUNC10_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x158
        self.__GPIO_SIG10_IN_SEL_lsb = 7
        self.__GPIO_SIG10_IN_SEL_msb = 7
        self.__GPIO_FUNC10_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC10_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC10_IN_SEL_lsb = 0
        self.__GPIO_FUNC10_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG10_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG10_IN_SEL_msb, self.__GPIO_SIG10_IN_SEL_lsb)
    @GPIO_SIG10_IN_SEL.setter
    def GPIO_SIG10_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG10_IN_SEL_msb, self.__GPIO_SIG10_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC10_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC10_IN_INV_SEL_msb, self.__GPIO_FUNC10_IN_INV_SEL_lsb)
    @GPIO_FUNC10_IN_INV_SEL.setter
    def GPIO_FUNC10_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC10_IN_INV_SEL_msb, self.__GPIO_FUNC10_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC10_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC10_IN_SEL_msb, self.__GPIO_FUNC10_IN_SEL_lsb)
    @GPIO_FUNC10_IN_SEL.setter
    def GPIO_FUNC10_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC10_IN_SEL_msb, self.__GPIO_FUNC10_IN_SEL_lsb, value)
class GPIO_FUNC11_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x15c
        self.__GPIO_SIG11_IN_SEL_lsb = 7
        self.__GPIO_SIG11_IN_SEL_msb = 7
        self.__GPIO_FUNC11_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC11_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC11_IN_SEL_lsb = 0
        self.__GPIO_FUNC11_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG11_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG11_IN_SEL_msb, self.__GPIO_SIG11_IN_SEL_lsb)
    @GPIO_SIG11_IN_SEL.setter
    def GPIO_SIG11_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG11_IN_SEL_msb, self.__GPIO_SIG11_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC11_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC11_IN_INV_SEL_msb, self.__GPIO_FUNC11_IN_INV_SEL_lsb)
    @GPIO_FUNC11_IN_INV_SEL.setter
    def GPIO_FUNC11_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC11_IN_INV_SEL_msb, self.__GPIO_FUNC11_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC11_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC11_IN_SEL_msb, self.__GPIO_FUNC11_IN_SEL_lsb)
    @GPIO_FUNC11_IN_SEL.setter
    def GPIO_FUNC11_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC11_IN_SEL_msb, self.__GPIO_FUNC11_IN_SEL_lsb, value)
class GPIO_FUNC12_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x160
        self.__GPIO_SIG12_IN_SEL_lsb = 7
        self.__GPIO_SIG12_IN_SEL_msb = 7
        self.__GPIO_FUNC12_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC12_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC12_IN_SEL_lsb = 0
        self.__GPIO_FUNC12_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG12_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG12_IN_SEL_msb, self.__GPIO_SIG12_IN_SEL_lsb)
    @GPIO_SIG12_IN_SEL.setter
    def GPIO_SIG12_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG12_IN_SEL_msb, self.__GPIO_SIG12_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC12_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC12_IN_INV_SEL_msb, self.__GPIO_FUNC12_IN_INV_SEL_lsb)
    @GPIO_FUNC12_IN_INV_SEL.setter
    def GPIO_FUNC12_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC12_IN_INV_SEL_msb, self.__GPIO_FUNC12_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC12_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC12_IN_SEL_msb, self.__GPIO_FUNC12_IN_SEL_lsb)
    @GPIO_FUNC12_IN_SEL.setter
    def GPIO_FUNC12_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC12_IN_SEL_msb, self.__GPIO_FUNC12_IN_SEL_lsb, value)
class GPIO_FUNC13_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x164
        self.__GPIO_SIG13_IN_SEL_lsb = 7
        self.__GPIO_SIG13_IN_SEL_msb = 7
        self.__GPIO_FUNC13_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC13_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC13_IN_SEL_lsb = 0
        self.__GPIO_FUNC13_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG13_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG13_IN_SEL_msb, self.__GPIO_SIG13_IN_SEL_lsb)
    @GPIO_SIG13_IN_SEL.setter
    def GPIO_SIG13_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG13_IN_SEL_msb, self.__GPIO_SIG13_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC13_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC13_IN_INV_SEL_msb, self.__GPIO_FUNC13_IN_INV_SEL_lsb)
    @GPIO_FUNC13_IN_INV_SEL.setter
    def GPIO_FUNC13_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC13_IN_INV_SEL_msb, self.__GPIO_FUNC13_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC13_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC13_IN_SEL_msb, self.__GPIO_FUNC13_IN_SEL_lsb)
    @GPIO_FUNC13_IN_SEL.setter
    def GPIO_FUNC13_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC13_IN_SEL_msb, self.__GPIO_FUNC13_IN_SEL_lsb, value)
class GPIO_FUNC14_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x168
        self.__GPIO_SIG14_IN_SEL_lsb = 7
        self.__GPIO_SIG14_IN_SEL_msb = 7
        self.__GPIO_FUNC14_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC14_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC14_IN_SEL_lsb = 0
        self.__GPIO_FUNC14_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG14_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG14_IN_SEL_msb, self.__GPIO_SIG14_IN_SEL_lsb)
    @GPIO_SIG14_IN_SEL.setter
    def GPIO_SIG14_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG14_IN_SEL_msb, self.__GPIO_SIG14_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC14_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC14_IN_INV_SEL_msb, self.__GPIO_FUNC14_IN_INV_SEL_lsb)
    @GPIO_FUNC14_IN_INV_SEL.setter
    def GPIO_FUNC14_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC14_IN_INV_SEL_msb, self.__GPIO_FUNC14_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC14_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC14_IN_SEL_msb, self.__GPIO_FUNC14_IN_SEL_lsb)
    @GPIO_FUNC14_IN_SEL.setter
    def GPIO_FUNC14_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC14_IN_SEL_msb, self.__GPIO_FUNC14_IN_SEL_lsb, value)
class GPIO_FUNC15_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x16c
        self.__GPIO_SIG15_IN_SEL_lsb = 7
        self.__GPIO_SIG15_IN_SEL_msb = 7
        self.__GPIO_FUNC15_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC15_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC15_IN_SEL_lsb = 0
        self.__GPIO_FUNC15_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG15_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG15_IN_SEL_msb, self.__GPIO_SIG15_IN_SEL_lsb)
    @GPIO_SIG15_IN_SEL.setter
    def GPIO_SIG15_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG15_IN_SEL_msb, self.__GPIO_SIG15_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC15_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC15_IN_INV_SEL_msb, self.__GPIO_FUNC15_IN_INV_SEL_lsb)
    @GPIO_FUNC15_IN_INV_SEL.setter
    def GPIO_FUNC15_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC15_IN_INV_SEL_msb, self.__GPIO_FUNC15_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC15_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC15_IN_SEL_msb, self.__GPIO_FUNC15_IN_SEL_lsb)
    @GPIO_FUNC15_IN_SEL.setter
    def GPIO_FUNC15_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC15_IN_SEL_msb, self.__GPIO_FUNC15_IN_SEL_lsb, value)
class GPIO_FUNC16_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x170
        self.__GPIO_SIG16_IN_SEL_lsb = 7
        self.__GPIO_SIG16_IN_SEL_msb = 7
        self.__GPIO_FUNC16_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC16_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC16_IN_SEL_lsb = 0
        self.__GPIO_FUNC16_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG16_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG16_IN_SEL_msb, self.__GPIO_SIG16_IN_SEL_lsb)
    @GPIO_SIG16_IN_SEL.setter
    def GPIO_SIG16_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG16_IN_SEL_msb, self.__GPIO_SIG16_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC16_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC16_IN_INV_SEL_msb, self.__GPIO_FUNC16_IN_INV_SEL_lsb)
    @GPIO_FUNC16_IN_INV_SEL.setter
    def GPIO_FUNC16_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC16_IN_INV_SEL_msb, self.__GPIO_FUNC16_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC16_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC16_IN_SEL_msb, self.__GPIO_FUNC16_IN_SEL_lsb)
    @GPIO_FUNC16_IN_SEL.setter
    def GPIO_FUNC16_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC16_IN_SEL_msb, self.__GPIO_FUNC16_IN_SEL_lsb, value)
class GPIO_FUNC17_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x174
        self.__GPIO_SIG17_IN_SEL_lsb = 7
        self.__GPIO_SIG17_IN_SEL_msb = 7
        self.__GPIO_FUNC17_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC17_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC17_IN_SEL_lsb = 0
        self.__GPIO_FUNC17_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG17_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG17_IN_SEL_msb, self.__GPIO_SIG17_IN_SEL_lsb)
    @GPIO_SIG17_IN_SEL.setter
    def GPIO_SIG17_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG17_IN_SEL_msb, self.__GPIO_SIG17_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC17_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC17_IN_INV_SEL_msb, self.__GPIO_FUNC17_IN_INV_SEL_lsb)
    @GPIO_FUNC17_IN_INV_SEL.setter
    def GPIO_FUNC17_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC17_IN_INV_SEL_msb, self.__GPIO_FUNC17_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC17_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC17_IN_SEL_msb, self.__GPIO_FUNC17_IN_SEL_lsb)
    @GPIO_FUNC17_IN_SEL.setter
    def GPIO_FUNC17_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC17_IN_SEL_msb, self.__GPIO_FUNC17_IN_SEL_lsb, value)
class GPIO_FUNC18_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x178
        self.__GPIO_SIG18_IN_SEL_lsb = 7
        self.__GPIO_SIG18_IN_SEL_msb = 7
        self.__GPIO_FUNC18_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC18_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC18_IN_SEL_lsb = 0
        self.__GPIO_FUNC18_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG18_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG18_IN_SEL_msb, self.__GPIO_SIG18_IN_SEL_lsb)
    @GPIO_SIG18_IN_SEL.setter
    def GPIO_SIG18_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG18_IN_SEL_msb, self.__GPIO_SIG18_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC18_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC18_IN_INV_SEL_msb, self.__GPIO_FUNC18_IN_INV_SEL_lsb)
    @GPIO_FUNC18_IN_INV_SEL.setter
    def GPIO_FUNC18_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC18_IN_INV_SEL_msb, self.__GPIO_FUNC18_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC18_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC18_IN_SEL_msb, self.__GPIO_FUNC18_IN_SEL_lsb)
    @GPIO_FUNC18_IN_SEL.setter
    def GPIO_FUNC18_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC18_IN_SEL_msb, self.__GPIO_FUNC18_IN_SEL_lsb, value)
class GPIO_FUNC19_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x17c
        self.__GPIO_SIG19_IN_SEL_lsb = 7
        self.__GPIO_SIG19_IN_SEL_msb = 7
        self.__GPIO_FUNC19_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC19_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC19_IN_SEL_lsb = 0
        self.__GPIO_FUNC19_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG19_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG19_IN_SEL_msb, self.__GPIO_SIG19_IN_SEL_lsb)
    @GPIO_SIG19_IN_SEL.setter
    def GPIO_SIG19_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG19_IN_SEL_msb, self.__GPIO_SIG19_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC19_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC19_IN_INV_SEL_msb, self.__GPIO_FUNC19_IN_INV_SEL_lsb)
    @GPIO_FUNC19_IN_INV_SEL.setter
    def GPIO_FUNC19_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC19_IN_INV_SEL_msb, self.__GPIO_FUNC19_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC19_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC19_IN_SEL_msb, self.__GPIO_FUNC19_IN_SEL_lsb)
    @GPIO_FUNC19_IN_SEL.setter
    def GPIO_FUNC19_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC19_IN_SEL_msb, self.__GPIO_FUNC19_IN_SEL_lsb, value)
class GPIO_FUNC20_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x180
        self.__GPIO_SIG20_IN_SEL_lsb = 7
        self.__GPIO_SIG20_IN_SEL_msb = 7
        self.__GPIO_FUNC20_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC20_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC20_IN_SEL_lsb = 0
        self.__GPIO_FUNC20_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG20_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG20_IN_SEL_msb, self.__GPIO_SIG20_IN_SEL_lsb)
    @GPIO_SIG20_IN_SEL.setter
    def GPIO_SIG20_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG20_IN_SEL_msb, self.__GPIO_SIG20_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC20_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC20_IN_INV_SEL_msb, self.__GPIO_FUNC20_IN_INV_SEL_lsb)
    @GPIO_FUNC20_IN_INV_SEL.setter
    def GPIO_FUNC20_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC20_IN_INV_SEL_msb, self.__GPIO_FUNC20_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC20_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC20_IN_SEL_msb, self.__GPIO_FUNC20_IN_SEL_lsb)
    @GPIO_FUNC20_IN_SEL.setter
    def GPIO_FUNC20_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC20_IN_SEL_msb, self.__GPIO_FUNC20_IN_SEL_lsb, value)
class GPIO_FUNC21_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x184
        self.__GPIO_SIG21_IN_SEL_lsb = 7
        self.__GPIO_SIG21_IN_SEL_msb = 7
        self.__GPIO_FUNC21_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC21_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC21_IN_SEL_lsb = 0
        self.__GPIO_FUNC21_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG21_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG21_IN_SEL_msb, self.__GPIO_SIG21_IN_SEL_lsb)
    @GPIO_SIG21_IN_SEL.setter
    def GPIO_SIG21_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG21_IN_SEL_msb, self.__GPIO_SIG21_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC21_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC21_IN_INV_SEL_msb, self.__GPIO_FUNC21_IN_INV_SEL_lsb)
    @GPIO_FUNC21_IN_INV_SEL.setter
    def GPIO_FUNC21_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC21_IN_INV_SEL_msb, self.__GPIO_FUNC21_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC21_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC21_IN_SEL_msb, self.__GPIO_FUNC21_IN_SEL_lsb)
    @GPIO_FUNC21_IN_SEL.setter
    def GPIO_FUNC21_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC21_IN_SEL_msb, self.__GPIO_FUNC21_IN_SEL_lsb, value)
class GPIO_FUNC22_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x188
        self.__GPIO_SIG22_IN_SEL_lsb = 7
        self.__GPIO_SIG22_IN_SEL_msb = 7
        self.__GPIO_FUNC22_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC22_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC22_IN_SEL_lsb = 0
        self.__GPIO_FUNC22_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG22_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG22_IN_SEL_msb, self.__GPIO_SIG22_IN_SEL_lsb)
    @GPIO_SIG22_IN_SEL.setter
    def GPIO_SIG22_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG22_IN_SEL_msb, self.__GPIO_SIG22_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC22_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC22_IN_INV_SEL_msb, self.__GPIO_FUNC22_IN_INV_SEL_lsb)
    @GPIO_FUNC22_IN_INV_SEL.setter
    def GPIO_FUNC22_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC22_IN_INV_SEL_msb, self.__GPIO_FUNC22_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC22_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC22_IN_SEL_msb, self.__GPIO_FUNC22_IN_SEL_lsb)
    @GPIO_FUNC22_IN_SEL.setter
    def GPIO_FUNC22_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC22_IN_SEL_msb, self.__GPIO_FUNC22_IN_SEL_lsb, value)
class GPIO_FUNC23_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x18c
        self.__GPIO_SIG23_IN_SEL_lsb = 7
        self.__GPIO_SIG23_IN_SEL_msb = 7
        self.__GPIO_FUNC23_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC23_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC23_IN_SEL_lsb = 0
        self.__GPIO_FUNC23_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG23_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG23_IN_SEL_msb, self.__GPIO_SIG23_IN_SEL_lsb)
    @GPIO_SIG23_IN_SEL.setter
    def GPIO_SIG23_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG23_IN_SEL_msb, self.__GPIO_SIG23_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC23_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC23_IN_INV_SEL_msb, self.__GPIO_FUNC23_IN_INV_SEL_lsb)
    @GPIO_FUNC23_IN_INV_SEL.setter
    def GPIO_FUNC23_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC23_IN_INV_SEL_msb, self.__GPIO_FUNC23_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC23_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC23_IN_SEL_msb, self.__GPIO_FUNC23_IN_SEL_lsb)
    @GPIO_FUNC23_IN_SEL.setter
    def GPIO_FUNC23_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC23_IN_SEL_msb, self.__GPIO_FUNC23_IN_SEL_lsb, value)
class GPIO_FUNC24_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x190
        self.__GPIO_SIG24_IN_SEL_lsb = 7
        self.__GPIO_SIG24_IN_SEL_msb = 7
        self.__GPIO_FUNC24_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC24_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC24_IN_SEL_lsb = 0
        self.__GPIO_FUNC24_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG24_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG24_IN_SEL_msb, self.__GPIO_SIG24_IN_SEL_lsb)
    @GPIO_SIG24_IN_SEL.setter
    def GPIO_SIG24_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG24_IN_SEL_msb, self.__GPIO_SIG24_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC24_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC24_IN_INV_SEL_msb, self.__GPIO_FUNC24_IN_INV_SEL_lsb)
    @GPIO_FUNC24_IN_INV_SEL.setter
    def GPIO_FUNC24_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC24_IN_INV_SEL_msb, self.__GPIO_FUNC24_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC24_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC24_IN_SEL_msb, self.__GPIO_FUNC24_IN_SEL_lsb)
    @GPIO_FUNC24_IN_SEL.setter
    def GPIO_FUNC24_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC24_IN_SEL_msb, self.__GPIO_FUNC24_IN_SEL_lsb, value)
class GPIO_FUNC25_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x194
        self.__GPIO_SIG25_IN_SEL_lsb = 7
        self.__GPIO_SIG25_IN_SEL_msb = 7
        self.__GPIO_FUNC25_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC25_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC25_IN_SEL_lsb = 0
        self.__GPIO_FUNC25_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG25_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG25_IN_SEL_msb, self.__GPIO_SIG25_IN_SEL_lsb)
    @GPIO_SIG25_IN_SEL.setter
    def GPIO_SIG25_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG25_IN_SEL_msb, self.__GPIO_SIG25_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC25_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC25_IN_INV_SEL_msb, self.__GPIO_FUNC25_IN_INV_SEL_lsb)
    @GPIO_FUNC25_IN_INV_SEL.setter
    def GPIO_FUNC25_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC25_IN_INV_SEL_msb, self.__GPIO_FUNC25_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC25_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC25_IN_SEL_msb, self.__GPIO_FUNC25_IN_SEL_lsb)
    @GPIO_FUNC25_IN_SEL.setter
    def GPIO_FUNC25_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC25_IN_SEL_msb, self.__GPIO_FUNC25_IN_SEL_lsb, value)
class GPIO_FUNC26_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x198
        self.__GPIO_SIG26_IN_SEL_lsb = 7
        self.__GPIO_SIG26_IN_SEL_msb = 7
        self.__GPIO_FUNC26_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC26_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC26_IN_SEL_lsb = 0
        self.__GPIO_FUNC26_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG26_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG26_IN_SEL_msb, self.__GPIO_SIG26_IN_SEL_lsb)
    @GPIO_SIG26_IN_SEL.setter
    def GPIO_SIG26_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG26_IN_SEL_msb, self.__GPIO_SIG26_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC26_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC26_IN_INV_SEL_msb, self.__GPIO_FUNC26_IN_INV_SEL_lsb)
    @GPIO_FUNC26_IN_INV_SEL.setter
    def GPIO_FUNC26_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC26_IN_INV_SEL_msb, self.__GPIO_FUNC26_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC26_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC26_IN_SEL_msb, self.__GPIO_FUNC26_IN_SEL_lsb)
    @GPIO_FUNC26_IN_SEL.setter
    def GPIO_FUNC26_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC26_IN_SEL_msb, self.__GPIO_FUNC26_IN_SEL_lsb, value)
class GPIO_FUNC27_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x19c
        self.__GPIO_SIG27_IN_SEL_lsb = 7
        self.__GPIO_SIG27_IN_SEL_msb = 7
        self.__GPIO_FUNC27_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC27_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC27_IN_SEL_lsb = 0
        self.__GPIO_FUNC27_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG27_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG27_IN_SEL_msb, self.__GPIO_SIG27_IN_SEL_lsb)
    @GPIO_SIG27_IN_SEL.setter
    def GPIO_SIG27_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG27_IN_SEL_msb, self.__GPIO_SIG27_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC27_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC27_IN_INV_SEL_msb, self.__GPIO_FUNC27_IN_INV_SEL_lsb)
    @GPIO_FUNC27_IN_INV_SEL.setter
    def GPIO_FUNC27_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC27_IN_INV_SEL_msb, self.__GPIO_FUNC27_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC27_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC27_IN_SEL_msb, self.__GPIO_FUNC27_IN_SEL_lsb)
    @GPIO_FUNC27_IN_SEL.setter
    def GPIO_FUNC27_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC27_IN_SEL_msb, self.__GPIO_FUNC27_IN_SEL_lsb, value)
class GPIO_FUNC28_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x1a0
        self.__GPIO_SIG28_IN_SEL_lsb = 7
        self.__GPIO_SIG28_IN_SEL_msb = 7
        self.__GPIO_FUNC28_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC28_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC28_IN_SEL_lsb = 0
        self.__GPIO_FUNC28_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG28_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG28_IN_SEL_msb, self.__GPIO_SIG28_IN_SEL_lsb)
    @GPIO_SIG28_IN_SEL.setter
    def GPIO_SIG28_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG28_IN_SEL_msb, self.__GPIO_SIG28_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC28_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC28_IN_INV_SEL_msb, self.__GPIO_FUNC28_IN_INV_SEL_lsb)
    @GPIO_FUNC28_IN_INV_SEL.setter
    def GPIO_FUNC28_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC28_IN_INV_SEL_msb, self.__GPIO_FUNC28_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC28_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC28_IN_SEL_msb, self.__GPIO_FUNC28_IN_SEL_lsb)
    @GPIO_FUNC28_IN_SEL.setter
    def GPIO_FUNC28_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC28_IN_SEL_msb, self.__GPIO_FUNC28_IN_SEL_lsb, value)
class GPIO_FUNC29_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x1a4
        self.__GPIO_SIG29_IN_SEL_lsb = 7
        self.__GPIO_SIG29_IN_SEL_msb = 7
        self.__GPIO_FUNC29_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC29_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC29_IN_SEL_lsb = 0
        self.__GPIO_FUNC29_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG29_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG29_IN_SEL_msb, self.__GPIO_SIG29_IN_SEL_lsb)
    @GPIO_SIG29_IN_SEL.setter
    def GPIO_SIG29_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG29_IN_SEL_msb, self.__GPIO_SIG29_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC29_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC29_IN_INV_SEL_msb, self.__GPIO_FUNC29_IN_INV_SEL_lsb)
    @GPIO_FUNC29_IN_INV_SEL.setter
    def GPIO_FUNC29_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC29_IN_INV_SEL_msb, self.__GPIO_FUNC29_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC29_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC29_IN_SEL_msb, self.__GPIO_FUNC29_IN_SEL_lsb)
    @GPIO_FUNC29_IN_SEL.setter
    def GPIO_FUNC29_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC29_IN_SEL_msb, self.__GPIO_FUNC29_IN_SEL_lsb, value)
class GPIO_FUNC30_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x1a8
        self.__GPIO_SIG30_IN_SEL_lsb = 7
        self.__GPIO_SIG30_IN_SEL_msb = 7
        self.__GPIO_FUNC30_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC30_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC30_IN_SEL_lsb = 0
        self.__GPIO_FUNC30_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG30_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG30_IN_SEL_msb, self.__GPIO_SIG30_IN_SEL_lsb)
    @GPIO_SIG30_IN_SEL.setter
    def GPIO_SIG30_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG30_IN_SEL_msb, self.__GPIO_SIG30_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC30_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC30_IN_INV_SEL_msb, self.__GPIO_FUNC30_IN_INV_SEL_lsb)
    @GPIO_FUNC30_IN_INV_SEL.setter
    def GPIO_FUNC30_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC30_IN_INV_SEL_msb, self.__GPIO_FUNC30_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC30_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC30_IN_SEL_msb, self.__GPIO_FUNC30_IN_SEL_lsb)
    @GPIO_FUNC30_IN_SEL.setter
    def GPIO_FUNC30_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC30_IN_SEL_msb, self.__GPIO_FUNC30_IN_SEL_lsb, value)
class GPIO_FUNC31_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x1ac
        self.__GPIO_SIG31_IN_SEL_lsb = 7
        self.__GPIO_SIG31_IN_SEL_msb = 7
        self.__GPIO_FUNC31_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC31_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC31_IN_SEL_lsb = 0
        self.__GPIO_FUNC31_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG31_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG31_IN_SEL_msb, self.__GPIO_SIG31_IN_SEL_lsb)
    @GPIO_SIG31_IN_SEL.setter
    def GPIO_SIG31_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG31_IN_SEL_msb, self.__GPIO_SIG31_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC31_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC31_IN_INV_SEL_msb, self.__GPIO_FUNC31_IN_INV_SEL_lsb)
    @GPIO_FUNC31_IN_INV_SEL.setter
    def GPIO_FUNC31_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC31_IN_INV_SEL_msb, self.__GPIO_FUNC31_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC31_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC31_IN_SEL_msb, self.__GPIO_FUNC31_IN_SEL_lsb)
    @GPIO_FUNC31_IN_SEL.setter
    def GPIO_FUNC31_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC31_IN_SEL_msb, self.__GPIO_FUNC31_IN_SEL_lsb, value)
class GPIO_FUNC32_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x1b0
        self.__GPIO_SIG32_IN_SEL_lsb = 7
        self.__GPIO_SIG32_IN_SEL_msb = 7
        self.__GPIO_FUNC32_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC32_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC32_IN_SEL_lsb = 0
        self.__GPIO_FUNC32_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG32_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG32_IN_SEL_msb, self.__GPIO_SIG32_IN_SEL_lsb)
    @GPIO_SIG32_IN_SEL.setter
    def GPIO_SIG32_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG32_IN_SEL_msb, self.__GPIO_SIG32_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC32_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC32_IN_INV_SEL_msb, self.__GPIO_FUNC32_IN_INV_SEL_lsb)
    @GPIO_FUNC32_IN_INV_SEL.setter
    def GPIO_FUNC32_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC32_IN_INV_SEL_msb, self.__GPIO_FUNC32_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC32_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC32_IN_SEL_msb, self.__GPIO_FUNC32_IN_SEL_lsb)
    @GPIO_FUNC32_IN_SEL.setter
    def GPIO_FUNC32_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC32_IN_SEL_msb, self.__GPIO_FUNC32_IN_SEL_lsb, value)
class GPIO_FUNC33_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x1b4
        self.__GPIO_SIG33_IN_SEL_lsb = 7
        self.__GPIO_SIG33_IN_SEL_msb = 7
        self.__GPIO_FUNC33_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC33_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC33_IN_SEL_lsb = 0
        self.__GPIO_FUNC33_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG33_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG33_IN_SEL_msb, self.__GPIO_SIG33_IN_SEL_lsb)
    @GPIO_SIG33_IN_SEL.setter
    def GPIO_SIG33_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG33_IN_SEL_msb, self.__GPIO_SIG33_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC33_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC33_IN_INV_SEL_msb, self.__GPIO_FUNC33_IN_INV_SEL_lsb)
    @GPIO_FUNC33_IN_INV_SEL.setter
    def GPIO_FUNC33_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC33_IN_INV_SEL_msb, self.__GPIO_FUNC33_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC33_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC33_IN_SEL_msb, self.__GPIO_FUNC33_IN_SEL_lsb)
    @GPIO_FUNC33_IN_SEL.setter
    def GPIO_FUNC33_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC33_IN_SEL_msb, self.__GPIO_FUNC33_IN_SEL_lsb, value)
class GPIO_FUNC34_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x1b8
        self.__GPIO_SIG34_IN_SEL_lsb = 7
        self.__GPIO_SIG34_IN_SEL_msb = 7
        self.__GPIO_FUNC34_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC34_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC34_IN_SEL_lsb = 0
        self.__GPIO_FUNC34_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG34_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG34_IN_SEL_msb, self.__GPIO_SIG34_IN_SEL_lsb)
    @GPIO_SIG34_IN_SEL.setter
    def GPIO_SIG34_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG34_IN_SEL_msb, self.__GPIO_SIG34_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC34_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC34_IN_INV_SEL_msb, self.__GPIO_FUNC34_IN_INV_SEL_lsb)
    @GPIO_FUNC34_IN_INV_SEL.setter
    def GPIO_FUNC34_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC34_IN_INV_SEL_msb, self.__GPIO_FUNC34_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC34_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC34_IN_SEL_msb, self.__GPIO_FUNC34_IN_SEL_lsb)
    @GPIO_FUNC34_IN_SEL.setter
    def GPIO_FUNC34_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC34_IN_SEL_msb, self.__GPIO_FUNC34_IN_SEL_lsb, value)
class GPIO_FUNC35_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x1bc
        self.__GPIO_SIG35_IN_SEL_lsb = 7
        self.__GPIO_SIG35_IN_SEL_msb = 7
        self.__GPIO_FUNC35_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC35_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC35_IN_SEL_lsb = 0
        self.__GPIO_FUNC35_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG35_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG35_IN_SEL_msb, self.__GPIO_SIG35_IN_SEL_lsb)
    @GPIO_SIG35_IN_SEL.setter
    def GPIO_SIG35_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG35_IN_SEL_msb, self.__GPIO_SIG35_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC35_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC35_IN_INV_SEL_msb, self.__GPIO_FUNC35_IN_INV_SEL_lsb)
    @GPIO_FUNC35_IN_INV_SEL.setter
    def GPIO_FUNC35_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC35_IN_INV_SEL_msb, self.__GPIO_FUNC35_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC35_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC35_IN_SEL_msb, self.__GPIO_FUNC35_IN_SEL_lsb)
    @GPIO_FUNC35_IN_SEL.setter
    def GPIO_FUNC35_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC35_IN_SEL_msb, self.__GPIO_FUNC35_IN_SEL_lsb, value)
class GPIO_FUNC36_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x1c0
        self.__GPIO_SIG36_IN_SEL_lsb = 7
        self.__GPIO_SIG36_IN_SEL_msb = 7
        self.__GPIO_FUNC36_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC36_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC36_IN_SEL_lsb = 0
        self.__GPIO_FUNC36_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG36_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG36_IN_SEL_msb, self.__GPIO_SIG36_IN_SEL_lsb)
    @GPIO_SIG36_IN_SEL.setter
    def GPIO_SIG36_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG36_IN_SEL_msb, self.__GPIO_SIG36_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC36_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC36_IN_INV_SEL_msb, self.__GPIO_FUNC36_IN_INV_SEL_lsb)
    @GPIO_FUNC36_IN_INV_SEL.setter
    def GPIO_FUNC36_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC36_IN_INV_SEL_msb, self.__GPIO_FUNC36_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC36_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC36_IN_SEL_msb, self.__GPIO_FUNC36_IN_SEL_lsb)
    @GPIO_FUNC36_IN_SEL.setter
    def GPIO_FUNC36_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC36_IN_SEL_msb, self.__GPIO_FUNC36_IN_SEL_lsb, value)
class GPIO_FUNC37_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x1c4
        self.__GPIO_SIG37_IN_SEL_lsb = 7
        self.__GPIO_SIG37_IN_SEL_msb = 7
        self.__GPIO_FUNC37_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC37_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC37_IN_SEL_lsb = 0
        self.__GPIO_FUNC37_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG37_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG37_IN_SEL_msb, self.__GPIO_SIG37_IN_SEL_lsb)
    @GPIO_SIG37_IN_SEL.setter
    def GPIO_SIG37_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG37_IN_SEL_msb, self.__GPIO_SIG37_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC37_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC37_IN_INV_SEL_msb, self.__GPIO_FUNC37_IN_INV_SEL_lsb)
    @GPIO_FUNC37_IN_INV_SEL.setter
    def GPIO_FUNC37_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC37_IN_INV_SEL_msb, self.__GPIO_FUNC37_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC37_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC37_IN_SEL_msb, self.__GPIO_FUNC37_IN_SEL_lsb)
    @GPIO_FUNC37_IN_SEL.setter
    def GPIO_FUNC37_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC37_IN_SEL_msb, self.__GPIO_FUNC37_IN_SEL_lsb, value)
class GPIO_FUNC38_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x1c8
        self.__GPIO_SIG38_IN_SEL_lsb = 7
        self.__GPIO_SIG38_IN_SEL_msb = 7
        self.__GPIO_FUNC38_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC38_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC38_IN_SEL_lsb = 0
        self.__GPIO_FUNC38_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG38_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG38_IN_SEL_msb, self.__GPIO_SIG38_IN_SEL_lsb)
    @GPIO_SIG38_IN_SEL.setter
    def GPIO_SIG38_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG38_IN_SEL_msb, self.__GPIO_SIG38_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC38_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC38_IN_INV_SEL_msb, self.__GPIO_FUNC38_IN_INV_SEL_lsb)
    @GPIO_FUNC38_IN_INV_SEL.setter
    def GPIO_FUNC38_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC38_IN_INV_SEL_msb, self.__GPIO_FUNC38_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC38_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC38_IN_SEL_msb, self.__GPIO_FUNC38_IN_SEL_lsb)
    @GPIO_FUNC38_IN_SEL.setter
    def GPIO_FUNC38_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC38_IN_SEL_msb, self.__GPIO_FUNC38_IN_SEL_lsb, value)
class GPIO_FUNC39_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x1cc
        self.__GPIO_SIG39_IN_SEL_lsb = 7
        self.__GPIO_SIG39_IN_SEL_msb = 7
        self.__GPIO_FUNC39_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC39_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC39_IN_SEL_lsb = 0
        self.__GPIO_FUNC39_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG39_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG39_IN_SEL_msb, self.__GPIO_SIG39_IN_SEL_lsb)
    @GPIO_SIG39_IN_SEL.setter
    def GPIO_SIG39_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG39_IN_SEL_msb, self.__GPIO_SIG39_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC39_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC39_IN_INV_SEL_msb, self.__GPIO_FUNC39_IN_INV_SEL_lsb)
    @GPIO_FUNC39_IN_INV_SEL.setter
    def GPIO_FUNC39_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC39_IN_INV_SEL_msb, self.__GPIO_FUNC39_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC39_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC39_IN_SEL_msb, self.__GPIO_FUNC39_IN_SEL_lsb)
    @GPIO_FUNC39_IN_SEL.setter
    def GPIO_FUNC39_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC39_IN_SEL_msb, self.__GPIO_FUNC39_IN_SEL_lsb, value)
class GPIO_FUNC40_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x1d0
        self.__GPIO_SIG40_IN_SEL_lsb = 7
        self.__GPIO_SIG40_IN_SEL_msb = 7
        self.__GPIO_FUNC40_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC40_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC40_IN_SEL_lsb = 0
        self.__GPIO_FUNC40_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG40_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG40_IN_SEL_msb, self.__GPIO_SIG40_IN_SEL_lsb)
    @GPIO_SIG40_IN_SEL.setter
    def GPIO_SIG40_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG40_IN_SEL_msb, self.__GPIO_SIG40_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC40_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC40_IN_INV_SEL_msb, self.__GPIO_FUNC40_IN_INV_SEL_lsb)
    @GPIO_FUNC40_IN_INV_SEL.setter
    def GPIO_FUNC40_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC40_IN_INV_SEL_msb, self.__GPIO_FUNC40_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC40_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC40_IN_SEL_msb, self.__GPIO_FUNC40_IN_SEL_lsb)
    @GPIO_FUNC40_IN_SEL.setter
    def GPIO_FUNC40_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC40_IN_SEL_msb, self.__GPIO_FUNC40_IN_SEL_lsb, value)
class GPIO_FUNC41_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x1d4
        self.__GPIO_SIG41_IN_SEL_lsb = 7
        self.__GPIO_SIG41_IN_SEL_msb = 7
        self.__GPIO_FUNC41_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC41_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC41_IN_SEL_lsb = 0
        self.__GPIO_FUNC41_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG41_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG41_IN_SEL_msb, self.__GPIO_SIG41_IN_SEL_lsb)
    @GPIO_SIG41_IN_SEL.setter
    def GPIO_SIG41_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG41_IN_SEL_msb, self.__GPIO_SIG41_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC41_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC41_IN_INV_SEL_msb, self.__GPIO_FUNC41_IN_INV_SEL_lsb)
    @GPIO_FUNC41_IN_INV_SEL.setter
    def GPIO_FUNC41_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC41_IN_INV_SEL_msb, self.__GPIO_FUNC41_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC41_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC41_IN_SEL_msb, self.__GPIO_FUNC41_IN_SEL_lsb)
    @GPIO_FUNC41_IN_SEL.setter
    def GPIO_FUNC41_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC41_IN_SEL_msb, self.__GPIO_FUNC41_IN_SEL_lsb, value)
class GPIO_FUNC42_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x1d8
        self.__GPIO_SIG42_IN_SEL_lsb = 7
        self.__GPIO_SIG42_IN_SEL_msb = 7
        self.__GPIO_FUNC42_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC42_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC42_IN_SEL_lsb = 0
        self.__GPIO_FUNC42_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG42_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG42_IN_SEL_msb, self.__GPIO_SIG42_IN_SEL_lsb)
    @GPIO_SIG42_IN_SEL.setter
    def GPIO_SIG42_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG42_IN_SEL_msb, self.__GPIO_SIG42_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC42_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC42_IN_INV_SEL_msb, self.__GPIO_FUNC42_IN_INV_SEL_lsb)
    @GPIO_FUNC42_IN_INV_SEL.setter
    def GPIO_FUNC42_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC42_IN_INV_SEL_msb, self.__GPIO_FUNC42_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC42_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC42_IN_SEL_msb, self.__GPIO_FUNC42_IN_SEL_lsb)
    @GPIO_FUNC42_IN_SEL.setter
    def GPIO_FUNC42_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC42_IN_SEL_msb, self.__GPIO_FUNC42_IN_SEL_lsb, value)
class GPIO_FUNC43_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x1dc
        self.__GPIO_SIG43_IN_SEL_lsb = 7
        self.__GPIO_SIG43_IN_SEL_msb = 7
        self.__GPIO_FUNC43_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC43_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC43_IN_SEL_lsb = 0
        self.__GPIO_FUNC43_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG43_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG43_IN_SEL_msb, self.__GPIO_SIG43_IN_SEL_lsb)
    @GPIO_SIG43_IN_SEL.setter
    def GPIO_SIG43_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG43_IN_SEL_msb, self.__GPIO_SIG43_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC43_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC43_IN_INV_SEL_msb, self.__GPIO_FUNC43_IN_INV_SEL_lsb)
    @GPIO_FUNC43_IN_INV_SEL.setter
    def GPIO_FUNC43_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC43_IN_INV_SEL_msb, self.__GPIO_FUNC43_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC43_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC43_IN_SEL_msb, self.__GPIO_FUNC43_IN_SEL_lsb)
    @GPIO_FUNC43_IN_SEL.setter
    def GPIO_FUNC43_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC43_IN_SEL_msb, self.__GPIO_FUNC43_IN_SEL_lsb, value)
class GPIO_FUNC44_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x1e0
        self.__GPIO_SIG44_IN_SEL_lsb = 7
        self.__GPIO_SIG44_IN_SEL_msb = 7
        self.__GPIO_FUNC44_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC44_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC44_IN_SEL_lsb = 0
        self.__GPIO_FUNC44_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG44_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG44_IN_SEL_msb, self.__GPIO_SIG44_IN_SEL_lsb)
    @GPIO_SIG44_IN_SEL.setter
    def GPIO_SIG44_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG44_IN_SEL_msb, self.__GPIO_SIG44_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC44_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC44_IN_INV_SEL_msb, self.__GPIO_FUNC44_IN_INV_SEL_lsb)
    @GPIO_FUNC44_IN_INV_SEL.setter
    def GPIO_FUNC44_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC44_IN_INV_SEL_msb, self.__GPIO_FUNC44_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC44_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC44_IN_SEL_msb, self.__GPIO_FUNC44_IN_SEL_lsb)
    @GPIO_FUNC44_IN_SEL.setter
    def GPIO_FUNC44_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC44_IN_SEL_msb, self.__GPIO_FUNC44_IN_SEL_lsb, value)
class GPIO_FUNC45_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x1e4
        self.__GPIO_SIG45_IN_SEL_lsb = 7
        self.__GPIO_SIG45_IN_SEL_msb = 7
        self.__GPIO_FUNC45_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC45_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC45_IN_SEL_lsb = 0
        self.__GPIO_FUNC45_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG45_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG45_IN_SEL_msb, self.__GPIO_SIG45_IN_SEL_lsb)
    @GPIO_SIG45_IN_SEL.setter
    def GPIO_SIG45_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG45_IN_SEL_msb, self.__GPIO_SIG45_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC45_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC45_IN_INV_SEL_msb, self.__GPIO_FUNC45_IN_INV_SEL_lsb)
    @GPIO_FUNC45_IN_INV_SEL.setter
    def GPIO_FUNC45_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC45_IN_INV_SEL_msb, self.__GPIO_FUNC45_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC45_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC45_IN_SEL_msb, self.__GPIO_FUNC45_IN_SEL_lsb)
    @GPIO_FUNC45_IN_SEL.setter
    def GPIO_FUNC45_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC45_IN_SEL_msb, self.__GPIO_FUNC45_IN_SEL_lsb, value)
class GPIO_FUNC46_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x1e8
        self.__GPIO_SIG46_IN_SEL_lsb = 7
        self.__GPIO_SIG46_IN_SEL_msb = 7
        self.__GPIO_FUNC46_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC46_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC46_IN_SEL_lsb = 0
        self.__GPIO_FUNC46_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG46_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG46_IN_SEL_msb, self.__GPIO_SIG46_IN_SEL_lsb)
    @GPIO_SIG46_IN_SEL.setter
    def GPIO_SIG46_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG46_IN_SEL_msb, self.__GPIO_SIG46_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC46_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC46_IN_INV_SEL_msb, self.__GPIO_FUNC46_IN_INV_SEL_lsb)
    @GPIO_FUNC46_IN_INV_SEL.setter
    def GPIO_FUNC46_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC46_IN_INV_SEL_msb, self.__GPIO_FUNC46_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC46_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC46_IN_SEL_msb, self.__GPIO_FUNC46_IN_SEL_lsb)
    @GPIO_FUNC46_IN_SEL.setter
    def GPIO_FUNC46_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC46_IN_SEL_msb, self.__GPIO_FUNC46_IN_SEL_lsb, value)
class GPIO_FUNC47_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x1ec
        self.__GPIO_SIG47_IN_SEL_lsb = 7
        self.__GPIO_SIG47_IN_SEL_msb = 7
        self.__GPIO_FUNC47_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC47_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC47_IN_SEL_lsb = 0
        self.__GPIO_FUNC47_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG47_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG47_IN_SEL_msb, self.__GPIO_SIG47_IN_SEL_lsb)
    @GPIO_SIG47_IN_SEL.setter
    def GPIO_SIG47_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG47_IN_SEL_msb, self.__GPIO_SIG47_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC47_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC47_IN_INV_SEL_msb, self.__GPIO_FUNC47_IN_INV_SEL_lsb)
    @GPIO_FUNC47_IN_INV_SEL.setter
    def GPIO_FUNC47_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC47_IN_INV_SEL_msb, self.__GPIO_FUNC47_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC47_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC47_IN_SEL_msb, self.__GPIO_FUNC47_IN_SEL_lsb)
    @GPIO_FUNC47_IN_SEL.setter
    def GPIO_FUNC47_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC47_IN_SEL_msb, self.__GPIO_FUNC47_IN_SEL_lsb, value)
class GPIO_FUNC48_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x1f0
        self.__GPIO_SIG48_IN_SEL_lsb = 7
        self.__GPIO_SIG48_IN_SEL_msb = 7
        self.__GPIO_FUNC48_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC48_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC48_IN_SEL_lsb = 0
        self.__GPIO_FUNC48_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG48_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG48_IN_SEL_msb, self.__GPIO_SIG48_IN_SEL_lsb)
    @GPIO_SIG48_IN_SEL.setter
    def GPIO_SIG48_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG48_IN_SEL_msb, self.__GPIO_SIG48_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC48_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC48_IN_INV_SEL_msb, self.__GPIO_FUNC48_IN_INV_SEL_lsb)
    @GPIO_FUNC48_IN_INV_SEL.setter
    def GPIO_FUNC48_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC48_IN_INV_SEL_msb, self.__GPIO_FUNC48_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC48_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC48_IN_SEL_msb, self.__GPIO_FUNC48_IN_SEL_lsb)
    @GPIO_FUNC48_IN_SEL.setter
    def GPIO_FUNC48_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC48_IN_SEL_msb, self.__GPIO_FUNC48_IN_SEL_lsb, value)
class GPIO_FUNC49_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x1f4
        self.__GPIO_SIG49_IN_SEL_lsb = 7
        self.__GPIO_SIG49_IN_SEL_msb = 7
        self.__GPIO_FUNC49_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC49_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC49_IN_SEL_lsb = 0
        self.__GPIO_FUNC49_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG49_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG49_IN_SEL_msb, self.__GPIO_SIG49_IN_SEL_lsb)
    @GPIO_SIG49_IN_SEL.setter
    def GPIO_SIG49_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG49_IN_SEL_msb, self.__GPIO_SIG49_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC49_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC49_IN_INV_SEL_msb, self.__GPIO_FUNC49_IN_INV_SEL_lsb)
    @GPIO_FUNC49_IN_INV_SEL.setter
    def GPIO_FUNC49_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC49_IN_INV_SEL_msb, self.__GPIO_FUNC49_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC49_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC49_IN_SEL_msb, self.__GPIO_FUNC49_IN_SEL_lsb)
    @GPIO_FUNC49_IN_SEL.setter
    def GPIO_FUNC49_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC49_IN_SEL_msb, self.__GPIO_FUNC49_IN_SEL_lsb, value)
class GPIO_FUNC50_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x1f8
        self.__GPIO_SIG50_IN_SEL_lsb = 7
        self.__GPIO_SIG50_IN_SEL_msb = 7
        self.__GPIO_FUNC50_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC50_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC50_IN_SEL_lsb = 0
        self.__GPIO_FUNC50_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG50_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG50_IN_SEL_msb, self.__GPIO_SIG50_IN_SEL_lsb)
    @GPIO_SIG50_IN_SEL.setter
    def GPIO_SIG50_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG50_IN_SEL_msb, self.__GPIO_SIG50_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC50_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC50_IN_INV_SEL_msb, self.__GPIO_FUNC50_IN_INV_SEL_lsb)
    @GPIO_FUNC50_IN_INV_SEL.setter
    def GPIO_FUNC50_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC50_IN_INV_SEL_msb, self.__GPIO_FUNC50_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC50_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC50_IN_SEL_msb, self.__GPIO_FUNC50_IN_SEL_lsb)
    @GPIO_FUNC50_IN_SEL.setter
    def GPIO_FUNC50_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC50_IN_SEL_msb, self.__GPIO_FUNC50_IN_SEL_lsb, value)
class GPIO_FUNC51_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x1fc
        self.__GPIO_SIG51_IN_SEL_lsb = 7
        self.__GPIO_SIG51_IN_SEL_msb = 7
        self.__GPIO_FUNC51_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC51_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC51_IN_SEL_lsb = 0
        self.__GPIO_FUNC51_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG51_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG51_IN_SEL_msb, self.__GPIO_SIG51_IN_SEL_lsb)
    @GPIO_SIG51_IN_SEL.setter
    def GPIO_SIG51_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG51_IN_SEL_msb, self.__GPIO_SIG51_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC51_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC51_IN_INV_SEL_msb, self.__GPIO_FUNC51_IN_INV_SEL_lsb)
    @GPIO_FUNC51_IN_INV_SEL.setter
    def GPIO_FUNC51_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC51_IN_INV_SEL_msb, self.__GPIO_FUNC51_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC51_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC51_IN_SEL_msb, self.__GPIO_FUNC51_IN_SEL_lsb)
    @GPIO_FUNC51_IN_SEL.setter
    def GPIO_FUNC51_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC51_IN_SEL_msb, self.__GPIO_FUNC51_IN_SEL_lsb, value)
class GPIO_FUNC52_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x200
        self.__GPIO_SIG52_IN_SEL_lsb = 7
        self.__GPIO_SIG52_IN_SEL_msb = 7
        self.__GPIO_FUNC52_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC52_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC52_IN_SEL_lsb = 0
        self.__GPIO_FUNC52_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG52_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG52_IN_SEL_msb, self.__GPIO_SIG52_IN_SEL_lsb)
    @GPIO_SIG52_IN_SEL.setter
    def GPIO_SIG52_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG52_IN_SEL_msb, self.__GPIO_SIG52_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC52_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC52_IN_INV_SEL_msb, self.__GPIO_FUNC52_IN_INV_SEL_lsb)
    @GPIO_FUNC52_IN_INV_SEL.setter
    def GPIO_FUNC52_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC52_IN_INV_SEL_msb, self.__GPIO_FUNC52_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC52_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC52_IN_SEL_msb, self.__GPIO_FUNC52_IN_SEL_lsb)
    @GPIO_FUNC52_IN_SEL.setter
    def GPIO_FUNC52_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC52_IN_SEL_msb, self.__GPIO_FUNC52_IN_SEL_lsb, value)
class GPIO_FUNC53_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x204
        self.__GPIO_SIG53_IN_SEL_lsb = 7
        self.__GPIO_SIG53_IN_SEL_msb = 7
        self.__GPIO_FUNC53_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC53_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC53_IN_SEL_lsb = 0
        self.__GPIO_FUNC53_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG53_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG53_IN_SEL_msb, self.__GPIO_SIG53_IN_SEL_lsb)
    @GPIO_SIG53_IN_SEL.setter
    def GPIO_SIG53_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG53_IN_SEL_msb, self.__GPIO_SIG53_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC53_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC53_IN_INV_SEL_msb, self.__GPIO_FUNC53_IN_INV_SEL_lsb)
    @GPIO_FUNC53_IN_INV_SEL.setter
    def GPIO_FUNC53_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC53_IN_INV_SEL_msb, self.__GPIO_FUNC53_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC53_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC53_IN_SEL_msb, self.__GPIO_FUNC53_IN_SEL_lsb)
    @GPIO_FUNC53_IN_SEL.setter
    def GPIO_FUNC53_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC53_IN_SEL_msb, self.__GPIO_FUNC53_IN_SEL_lsb, value)
class GPIO_FUNC54_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x208
        self.__GPIO_SIG54_IN_SEL_lsb = 7
        self.__GPIO_SIG54_IN_SEL_msb = 7
        self.__GPIO_FUNC54_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC54_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC54_IN_SEL_lsb = 0
        self.__GPIO_FUNC54_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG54_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG54_IN_SEL_msb, self.__GPIO_SIG54_IN_SEL_lsb)
    @GPIO_SIG54_IN_SEL.setter
    def GPIO_SIG54_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG54_IN_SEL_msb, self.__GPIO_SIG54_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC54_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC54_IN_INV_SEL_msb, self.__GPIO_FUNC54_IN_INV_SEL_lsb)
    @GPIO_FUNC54_IN_INV_SEL.setter
    def GPIO_FUNC54_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC54_IN_INV_SEL_msb, self.__GPIO_FUNC54_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC54_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC54_IN_SEL_msb, self.__GPIO_FUNC54_IN_SEL_lsb)
    @GPIO_FUNC54_IN_SEL.setter
    def GPIO_FUNC54_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC54_IN_SEL_msb, self.__GPIO_FUNC54_IN_SEL_lsb, value)
class GPIO_FUNC55_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x20c
        self.__GPIO_SIG55_IN_SEL_lsb = 7
        self.__GPIO_SIG55_IN_SEL_msb = 7
        self.__GPIO_FUNC55_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC55_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC55_IN_SEL_lsb = 0
        self.__GPIO_FUNC55_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG55_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG55_IN_SEL_msb, self.__GPIO_SIG55_IN_SEL_lsb)
    @GPIO_SIG55_IN_SEL.setter
    def GPIO_SIG55_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG55_IN_SEL_msb, self.__GPIO_SIG55_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC55_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC55_IN_INV_SEL_msb, self.__GPIO_FUNC55_IN_INV_SEL_lsb)
    @GPIO_FUNC55_IN_INV_SEL.setter
    def GPIO_FUNC55_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC55_IN_INV_SEL_msb, self.__GPIO_FUNC55_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC55_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC55_IN_SEL_msb, self.__GPIO_FUNC55_IN_SEL_lsb)
    @GPIO_FUNC55_IN_SEL.setter
    def GPIO_FUNC55_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC55_IN_SEL_msb, self.__GPIO_FUNC55_IN_SEL_lsb, value)
class GPIO_FUNC56_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x210
        self.__GPIO_SIG56_IN_SEL_lsb = 7
        self.__GPIO_SIG56_IN_SEL_msb = 7
        self.__GPIO_FUNC56_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC56_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC56_IN_SEL_lsb = 0
        self.__GPIO_FUNC56_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG56_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG56_IN_SEL_msb, self.__GPIO_SIG56_IN_SEL_lsb)
    @GPIO_SIG56_IN_SEL.setter
    def GPIO_SIG56_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG56_IN_SEL_msb, self.__GPIO_SIG56_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC56_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC56_IN_INV_SEL_msb, self.__GPIO_FUNC56_IN_INV_SEL_lsb)
    @GPIO_FUNC56_IN_INV_SEL.setter
    def GPIO_FUNC56_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC56_IN_INV_SEL_msb, self.__GPIO_FUNC56_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC56_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC56_IN_SEL_msb, self.__GPIO_FUNC56_IN_SEL_lsb)
    @GPIO_FUNC56_IN_SEL.setter
    def GPIO_FUNC56_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC56_IN_SEL_msb, self.__GPIO_FUNC56_IN_SEL_lsb, value)
class GPIO_FUNC57_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x214
        self.__GPIO_SIG57_IN_SEL_lsb = 7
        self.__GPIO_SIG57_IN_SEL_msb = 7
        self.__GPIO_FUNC57_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC57_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC57_IN_SEL_lsb = 0
        self.__GPIO_FUNC57_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG57_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG57_IN_SEL_msb, self.__GPIO_SIG57_IN_SEL_lsb)
    @GPIO_SIG57_IN_SEL.setter
    def GPIO_SIG57_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG57_IN_SEL_msb, self.__GPIO_SIG57_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC57_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC57_IN_INV_SEL_msb, self.__GPIO_FUNC57_IN_INV_SEL_lsb)
    @GPIO_FUNC57_IN_INV_SEL.setter
    def GPIO_FUNC57_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC57_IN_INV_SEL_msb, self.__GPIO_FUNC57_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC57_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC57_IN_SEL_msb, self.__GPIO_FUNC57_IN_SEL_lsb)
    @GPIO_FUNC57_IN_SEL.setter
    def GPIO_FUNC57_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC57_IN_SEL_msb, self.__GPIO_FUNC57_IN_SEL_lsb, value)
class GPIO_FUNC58_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x218
        self.__GPIO_SIG58_IN_SEL_lsb = 7
        self.__GPIO_SIG58_IN_SEL_msb = 7
        self.__GPIO_FUNC58_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC58_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC58_IN_SEL_lsb = 0
        self.__GPIO_FUNC58_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG58_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG58_IN_SEL_msb, self.__GPIO_SIG58_IN_SEL_lsb)
    @GPIO_SIG58_IN_SEL.setter
    def GPIO_SIG58_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG58_IN_SEL_msb, self.__GPIO_SIG58_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC58_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC58_IN_INV_SEL_msb, self.__GPIO_FUNC58_IN_INV_SEL_lsb)
    @GPIO_FUNC58_IN_INV_SEL.setter
    def GPIO_FUNC58_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC58_IN_INV_SEL_msb, self.__GPIO_FUNC58_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC58_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC58_IN_SEL_msb, self.__GPIO_FUNC58_IN_SEL_lsb)
    @GPIO_FUNC58_IN_SEL.setter
    def GPIO_FUNC58_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC58_IN_SEL_msb, self.__GPIO_FUNC58_IN_SEL_lsb, value)
class GPIO_FUNC59_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x21c
        self.__GPIO_SIG59_IN_SEL_lsb = 7
        self.__GPIO_SIG59_IN_SEL_msb = 7
        self.__GPIO_FUNC59_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC59_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC59_IN_SEL_lsb = 0
        self.__GPIO_FUNC59_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG59_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG59_IN_SEL_msb, self.__GPIO_SIG59_IN_SEL_lsb)
    @GPIO_SIG59_IN_SEL.setter
    def GPIO_SIG59_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG59_IN_SEL_msb, self.__GPIO_SIG59_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC59_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC59_IN_INV_SEL_msb, self.__GPIO_FUNC59_IN_INV_SEL_lsb)
    @GPIO_FUNC59_IN_INV_SEL.setter
    def GPIO_FUNC59_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC59_IN_INV_SEL_msb, self.__GPIO_FUNC59_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC59_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC59_IN_SEL_msb, self.__GPIO_FUNC59_IN_SEL_lsb)
    @GPIO_FUNC59_IN_SEL.setter
    def GPIO_FUNC59_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC59_IN_SEL_msb, self.__GPIO_FUNC59_IN_SEL_lsb, value)
class GPIO_FUNC60_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x220
        self.__GPIO_SIG60_IN_SEL_lsb = 7
        self.__GPIO_SIG60_IN_SEL_msb = 7
        self.__GPIO_FUNC60_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC60_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC60_IN_SEL_lsb = 0
        self.__GPIO_FUNC60_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG60_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG60_IN_SEL_msb, self.__GPIO_SIG60_IN_SEL_lsb)
    @GPIO_SIG60_IN_SEL.setter
    def GPIO_SIG60_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG60_IN_SEL_msb, self.__GPIO_SIG60_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC60_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC60_IN_INV_SEL_msb, self.__GPIO_FUNC60_IN_INV_SEL_lsb)
    @GPIO_FUNC60_IN_INV_SEL.setter
    def GPIO_FUNC60_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC60_IN_INV_SEL_msb, self.__GPIO_FUNC60_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC60_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC60_IN_SEL_msb, self.__GPIO_FUNC60_IN_SEL_lsb)
    @GPIO_FUNC60_IN_SEL.setter
    def GPIO_FUNC60_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC60_IN_SEL_msb, self.__GPIO_FUNC60_IN_SEL_lsb, value)
class GPIO_FUNC61_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x224
        self.__GPIO_SIG61_IN_SEL_lsb = 7
        self.__GPIO_SIG61_IN_SEL_msb = 7
        self.__GPIO_FUNC61_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC61_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC61_IN_SEL_lsb = 0
        self.__GPIO_FUNC61_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG61_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG61_IN_SEL_msb, self.__GPIO_SIG61_IN_SEL_lsb)
    @GPIO_SIG61_IN_SEL.setter
    def GPIO_SIG61_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG61_IN_SEL_msb, self.__GPIO_SIG61_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC61_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC61_IN_INV_SEL_msb, self.__GPIO_FUNC61_IN_INV_SEL_lsb)
    @GPIO_FUNC61_IN_INV_SEL.setter
    def GPIO_FUNC61_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC61_IN_INV_SEL_msb, self.__GPIO_FUNC61_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC61_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC61_IN_SEL_msb, self.__GPIO_FUNC61_IN_SEL_lsb)
    @GPIO_FUNC61_IN_SEL.setter
    def GPIO_FUNC61_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC61_IN_SEL_msb, self.__GPIO_FUNC61_IN_SEL_lsb, value)
class GPIO_FUNC62_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x228
        self.__GPIO_SIG62_IN_SEL_lsb = 7
        self.__GPIO_SIG62_IN_SEL_msb = 7
        self.__GPIO_FUNC62_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC62_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC62_IN_SEL_lsb = 0
        self.__GPIO_FUNC62_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG62_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG62_IN_SEL_msb, self.__GPIO_SIG62_IN_SEL_lsb)
    @GPIO_SIG62_IN_SEL.setter
    def GPIO_SIG62_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG62_IN_SEL_msb, self.__GPIO_SIG62_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC62_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC62_IN_INV_SEL_msb, self.__GPIO_FUNC62_IN_INV_SEL_lsb)
    @GPIO_FUNC62_IN_INV_SEL.setter
    def GPIO_FUNC62_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC62_IN_INV_SEL_msb, self.__GPIO_FUNC62_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC62_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC62_IN_SEL_msb, self.__GPIO_FUNC62_IN_SEL_lsb)
    @GPIO_FUNC62_IN_SEL.setter
    def GPIO_FUNC62_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC62_IN_SEL_msb, self.__GPIO_FUNC62_IN_SEL_lsb, value)
class GPIO_FUNC63_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x22c
        self.__GPIO_SIG63_IN_SEL_lsb = 7
        self.__GPIO_SIG63_IN_SEL_msb = 7
        self.__GPIO_FUNC63_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC63_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC63_IN_SEL_lsb = 0
        self.__GPIO_FUNC63_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG63_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG63_IN_SEL_msb, self.__GPIO_SIG63_IN_SEL_lsb)
    @GPIO_SIG63_IN_SEL.setter
    def GPIO_SIG63_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG63_IN_SEL_msb, self.__GPIO_SIG63_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC63_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC63_IN_INV_SEL_msb, self.__GPIO_FUNC63_IN_INV_SEL_lsb)
    @GPIO_FUNC63_IN_INV_SEL.setter
    def GPIO_FUNC63_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC63_IN_INV_SEL_msb, self.__GPIO_FUNC63_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC63_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC63_IN_SEL_msb, self.__GPIO_FUNC63_IN_SEL_lsb)
    @GPIO_FUNC63_IN_SEL.setter
    def GPIO_FUNC63_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC63_IN_SEL_msb, self.__GPIO_FUNC63_IN_SEL_lsb, value)
class GPIO_FUNC64_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x230
        self.__GPIO_SIG64_IN_SEL_lsb = 7
        self.__GPIO_SIG64_IN_SEL_msb = 7
        self.__GPIO_FUNC64_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC64_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC64_IN_SEL_lsb = 0
        self.__GPIO_FUNC64_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG64_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG64_IN_SEL_msb, self.__GPIO_SIG64_IN_SEL_lsb)
    @GPIO_SIG64_IN_SEL.setter
    def GPIO_SIG64_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG64_IN_SEL_msb, self.__GPIO_SIG64_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC64_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC64_IN_INV_SEL_msb, self.__GPIO_FUNC64_IN_INV_SEL_lsb)
    @GPIO_FUNC64_IN_INV_SEL.setter
    def GPIO_FUNC64_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC64_IN_INV_SEL_msb, self.__GPIO_FUNC64_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC64_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC64_IN_SEL_msb, self.__GPIO_FUNC64_IN_SEL_lsb)
    @GPIO_FUNC64_IN_SEL.setter
    def GPIO_FUNC64_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC64_IN_SEL_msb, self.__GPIO_FUNC64_IN_SEL_lsb, value)
class GPIO_FUNC65_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x234
        self.__GPIO_SIG65_IN_SEL_lsb = 7
        self.__GPIO_SIG65_IN_SEL_msb = 7
        self.__GPIO_FUNC65_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC65_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC65_IN_SEL_lsb = 0
        self.__GPIO_FUNC65_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG65_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG65_IN_SEL_msb, self.__GPIO_SIG65_IN_SEL_lsb)
    @GPIO_SIG65_IN_SEL.setter
    def GPIO_SIG65_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG65_IN_SEL_msb, self.__GPIO_SIG65_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC65_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC65_IN_INV_SEL_msb, self.__GPIO_FUNC65_IN_INV_SEL_lsb)
    @GPIO_FUNC65_IN_INV_SEL.setter
    def GPIO_FUNC65_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC65_IN_INV_SEL_msb, self.__GPIO_FUNC65_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC65_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC65_IN_SEL_msb, self.__GPIO_FUNC65_IN_SEL_lsb)
    @GPIO_FUNC65_IN_SEL.setter
    def GPIO_FUNC65_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC65_IN_SEL_msb, self.__GPIO_FUNC65_IN_SEL_lsb, value)
class GPIO_FUNC66_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x238
        self.__GPIO_SIG66_IN_SEL_lsb = 7
        self.__GPIO_SIG66_IN_SEL_msb = 7
        self.__GPIO_FUNC66_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC66_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC66_IN_SEL_lsb = 0
        self.__GPIO_FUNC66_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG66_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG66_IN_SEL_msb, self.__GPIO_SIG66_IN_SEL_lsb)
    @GPIO_SIG66_IN_SEL.setter
    def GPIO_SIG66_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG66_IN_SEL_msb, self.__GPIO_SIG66_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC66_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC66_IN_INV_SEL_msb, self.__GPIO_FUNC66_IN_INV_SEL_lsb)
    @GPIO_FUNC66_IN_INV_SEL.setter
    def GPIO_FUNC66_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC66_IN_INV_SEL_msb, self.__GPIO_FUNC66_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC66_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC66_IN_SEL_msb, self.__GPIO_FUNC66_IN_SEL_lsb)
    @GPIO_FUNC66_IN_SEL.setter
    def GPIO_FUNC66_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC66_IN_SEL_msb, self.__GPIO_FUNC66_IN_SEL_lsb, value)
class GPIO_FUNC67_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x23c
        self.__GPIO_SIG67_IN_SEL_lsb = 7
        self.__GPIO_SIG67_IN_SEL_msb = 7
        self.__GPIO_FUNC67_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC67_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC67_IN_SEL_lsb = 0
        self.__GPIO_FUNC67_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG67_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG67_IN_SEL_msb, self.__GPIO_SIG67_IN_SEL_lsb)
    @GPIO_SIG67_IN_SEL.setter
    def GPIO_SIG67_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG67_IN_SEL_msb, self.__GPIO_SIG67_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC67_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC67_IN_INV_SEL_msb, self.__GPIO_FUNC67_IN_INV_SEL_lsb)
    @GPIO_FUNC67_IN_INV_SEL.setter
    def GPIO_FUNC67_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC67_IN_INV_SEL_msb, self.__GPIO_FUNC67_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC67_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC67_IN_SEL_msb, self.__GPIO_FUNC67_IN_SEL_lsb)
    @GPIO_FUNC67_IN_SEL.setter
    def GPIO_FUNC67_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC67_IN_SEL_msb, self.__GPIO_FUNC67_IN_SEL_lsb, value)
class GPIO_FUNC68_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x240
        self.__GPIO_SIG68_IN_SEL_lsb = 7
        self.__GPIO_SIG68_IN_SEL_msb = 7
        self.__GPIO_FUNC68_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC68_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC68_IN_SEL_lsb = 0
        self.__GPIO_FUNC68_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG68_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG68_IN_SEL_msb, self.__GPIO_SIG68_IN_SEL_lsb)
    @GPIO_SIG68_IN_SEL.setter
    def GPIO_SIG68_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG68_IN_SEL_msb, self.__GPIO_SIG68_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC68_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC68_IN_INV_SEL_msb, self.__GPIO_FUNC68_IN_INV_SEL_lsb)
    @GPIO_FUNC68_IN_INV_SEL.setter
    def GPIO_FUNC68_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC68_IN_INV_SEL_msb, self.__GPIO_FUNC68_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC68_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC68_IN_SEL_msb, self.__GPIO_FUNC68_IN_SEL_lsb)
    @GPIO_FUNC68_IN_SEL.setter
    def GPIO_FUNC68_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC68_IN_SEL_msb, self.__GPIO_FUNC68_IN_SEL_lsb, value)
class GPIO_FUNC69_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x244
        self.__GPIO_SIG69_IN_SEL_lsb = 7
        self.__GPIO_SIG69_IN_SEL_msb = 7
        self.__GPIO_FUNC69_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC69_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC69_IN_SEL_lsb = 0
        self.__GPIO_FUNC69_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG69_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG69_IN_SEL_msb, self.__GPIO_SIG69_IN_SEL_lsb)
    @GPIO_SIG69_IN_SEL.setter
    def GPIO_SIG69_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG69_IN_SEL_msb, self.__GPIO_SIG69_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC69_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC69_IN_INV_SEL_msb, self.__GPIO_FUNC69_IN_INV_SEL_lsb)
    @GPIO_FUNC69_IN_INV_SEL.setter
    def GPIO_FUNC69_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC69_IN_INV_SEL_msb, self.__GPIO_FUNC69_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC69_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC69_IN_SEL_msb, self.__GPIO_FUNC69_IN_SEL_lsb)
    @GPIO_FUNC69_IN_SEL.setter
    def GPIO_FUNC69_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC69_IN_SEL_msb, self.__GPIO_FUNC69_IN_SEL_lsb, value)
class GPIO_FUNC70_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x248
        self.__GPIO_SIG70_IN_SEL_lsb = 7
        self.__GPIO_SIG70_IN_SEL_msb = 7
        self.__GPIO_FUNC70_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC70_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC70_IN_SEL_lsb = 0
        self.__GPIO_FUNC70_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG70_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG70_IN_SEL_msb, self.__GPIO_SIG70_IN_SEL_lsb)
    @GPIO_SIG70_IN_SEL.setter
    def GPIO_SIG70_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG70_IN_SEL_msb, self.__GPIO_SIG70_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC70_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC70_IN_INV_SEL_msb, self.__GPIO_FUNC70_IN_INV_SEL_lsb)
    @GPIO_FUNC70_IN_INV_SEL.setter
    def GPIO_FUNC70_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC70_IN_INV_SEL_msb, self.__GPIO_FUNC70_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC70_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC70_IN_SEL_msb, self.__GPIO_FUNC70_IN_SEL_lsb)
    @GPIO_FUNC70_IN_SEL.setter
    def GPIO_FUNC70_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC70_IN_SEL_msb, self.__GPIO_FUNC70_IN_SEL_lsb, value)
class GPIO_FUNC71_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x24c
        self.__GPIO_SIG71_IN_SEL_lsb = 7
        self.__GPIO_SIG71_IN_SEL_msb = 7
        self.__GPIO_FUNC71_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC71_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC71_IN_SEL_lsb = 0
        self.__GPIO_FUNC71_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG71_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG71_IN_SEL_msb, self.__GPIO_SIG71_IN_SEL_lsb)
    @GPIO_SIG71_IN_SEL.setter
    def GPIO_SIG71_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG71_IN_SEL_msb, self.__GPIO_SIG71_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC71_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC71_IN_INV_SEL_msb, self.__GPIO_FUNC71_IN_INV_SEL_lsb)
    @GPIO_FUNC71_IN_INV_SEL.setter
    def GPIO_FUNC71_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC71_IN_INV_SEL_msb, self.__GPIO_FUNC71_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC71_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC71_IN_SEL_msb, self.__GPIO_FUNC71_IN_SEL_lsb)
    @GPIO_FUNC71_IN_SEL.setter
    def GPIO_FUNC71_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC71_IN_SEL_msb, self.__GPIO_FUNC71_IN_SEL_lsb, value)
class GPIO_FUNC72_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x250
        self.__GPIO_SIG72_IN_SEL_lsb = 7
        self.__GPIO_SIG72_IN_SEL_msb = 7
        self.__GPIO_FUNC72_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC72_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC72_IN_SEL_lsb = 0
        self.__GPIO_FUNC72_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG72_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG72_IN_SEL_msb, self.__GPIO_SIG72_IN_SEL_lsb)
    @GPIO_SIG72_IN_SEL.setter
    def GPIO_SIG72_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG72_IN_SEL_msb, self.__GPIO_SIG72_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC72_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC72_IN_INV_SEL_msb, self.__GPIO_FUNC72_IN_INV_SEL_lsb)
    @GPIO_FUNC72_IN_INV_SEL.setter
    def GPIO_FUNC72_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC72_IN_INV_SEL_msb, self.__GPIO_FUNC72_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC72_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC72_IN_SEL_msb, self.__GPIO_FUNC72_IN_SEL_lsb)
    @GPIO_FUNC72_IN_SEL.setter
    def GPIO_FUNC72_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC72_IN_SEL_msb, self.__GPIO_FUNC72_IN_SEL_lsb, value)
class GPIO_FUNC73_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x254
        self.__GPIO_SIG73_IN_SEL_lsb = 7
        self.__GPIO_SIG73_IN_SEL_msb = 7
        self.__GPIO_FUNC73_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC73_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC73_IN_SEL_lsb = 0
        self.__GPIO_FUNC73_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG73_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG73_IN_SEL_msb, self.__GPIO_SIG73_IN_SEL_lsb)
    @GPIO_SIG73_IN_SEL.setter
    def GPIO_SIG73_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG73_IN_SEL_msb, self.__GPIO_SIG73_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC73_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC73_IN_INV_SEL_msb, self.__GPIO_FUNC73_IN_INV_SEL_lsb)
    @GPIO_FUNC73_IN_INV_SEL.setter
    def GPIO_FUNC73_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC73_IN_INV_SEL_msb, self.__GPIO_FUNC73_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC73_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC73_IN_SEL_msb, self.__GPIO_FUNC73_IN_SEL_lsb)
    @GPIO_FUNC73_IN_SEL.setter
    def GPIO_FUNC73_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC73_IN_SEL_msb, self.__GPIO_FUNC73_IN_SEL_lsb, value)
class GPIO_FUNC74_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x258
        self.__GPIO_SIG74_IN_SEL_lsb = 7
        self.__GPIO_SIG74_IN_SEL_msb = 7
        self.__GPIO_FUNC74_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC74_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC74_IN_SEL_lsb = 0
        self.__GPIO_FUNC74_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG74_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG74_IN_SEL_msb, self.__GPIO_SIG74_IN_SEL_lsb)
    @GPIO_SIG74_IN_SEL.setter
    def GPIO_SIG74_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG74_IN_SEL_msb, self.__GPIO_SIG74_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC74_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC74_IN_INV_SEL_msb, self.__GPIO_FUNC74_IN_INV_SEL_lsb)
    @GPIO_FUNC74_IN_INV_SEL.setter
    def GPIO_FUNC74_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC74_IN_INV_SEL_msb, self.__GPIO_FUNC74_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC74_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC74_IN_SEL_msb, self.__GPIO_FUNC74_IN_SEL_lsb)
    @GPIO_FUNC74_IN_SEL.setter
    def GPIO_FUNC74_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC74_IN_SEL_msb, self.__GPIO_FUNC74_IN_SEL_lsb, value)
class GPIO_FUNC75_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x25c
        self.__GPIO_SIG75_IN_SEL_lsb = 7
        self.__GPIO_SIG75_IN_SEL_msb = 7
        self.__GPIO_FUNC75_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC75_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC75_IN_SEL_lsb = 0
        self.__GPIO_FUNC75_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG75_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG75_IN_SEL_msb, self.__GPIO_SIG75_IN_SEL_lsb)
    @GPIO_SIG75_IN_SEL.setter
    def GPIO_SIG75_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG75_IN_SEL_msb, self.__GPIO_SIG75_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC75_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC75_IN_INV_SEL_msb, self.__GPIO_FUNC75_IN_INV_SEL_lsb)
    @GPIO_FUNC75_IN_INV_SEL.setter
    def GPIO_FUNC75_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC75_IN_INV_SEL_msb, self.__GPIO_FUNC75_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC75_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC75_IN_SEL_msb, self.__GPIO_FUNC75_IN_SEL_lsb)
    @GPIO_FUNC75_IN_SEL.setter
    def GPIO_FUNC75_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC75_IN_SEL_msb, self.__GPIO_FUNC75_IN_SEL_lsb, value)
class GPIO_FUNC76_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x260
        self.__GPIO_SIG76_IN_SEL_lsb = 7
        self.__GPIO_SIG76_IN_SEL_msb = 7
        self.__GPIO_FUNC76_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC76_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC76_IN_SEL_lsb = 0
        self.__GPIO_FUNC76_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG76_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG76_IN_SEL_msb, self.__GPIO_SIG76_IN_SEL_lsb)
    @GPIO_SIG76_IN_SEL.setter
    def GPIO_SIG76_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG76_IN_SEL_msb, self.__GPIO_SIG76_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC76_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC76_IN_INV_SEL_msb, self.__GPIO_FUNC76_IN_INV_SEL_lsb)
    @GPIO_FUNC76_IN_INV_SEL.setter
    def GPIO_FUNC76_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC76_IN_INV_SEL_msb, self.__GPIO_FUNC76_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC76_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC76_IN_SEL_msb, self.__GPIO_FUNC76_IN_SEL_lsb)
    @GPIO_FUNC76_IN_SEL.setter
    def GPIO_FUNC76_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC76_IN_SEL_msb, self.__GPIO_FUNC76_IN_SEL_lsb, value)
class GPIO_FUNC77_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x264
        self.__GPIO_SIG77_IN_SEL_lsb = 7
        self.__GPIO_SIG77_IN_SEL_msb = 7
        self.__GPIO_FUNC77_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC77_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC77_IN_SEL_lsb = 0
        self.__GPIO_FUNC77_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG77_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG77_IN_SEL_msb, self.__GPIO_SIG77_IN_SEL_lsb)
    @GPIO_SIG77_IN_SEL.setter
    def GPIO_SIG77_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG77_IN_SEL_msb, self.__GPIO_SIG77_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC77_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC77_IN_INV_SEL_msb, self.__GPIO_FUNC77_IN_INV_SEL_lsb)
    @GPIO_FUNC77_IN_INV_SEL.setter
    def GPIO_FUNC77_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC77_IN_INV_SEL_msb, self.__GPIO_FUNC77_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC77_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC77_IN_SEL_msb, self.__GPIO_FUNC77_IN_SEL_lsb)
    @GPIO_FUNC77_IN_SEL.setter
    def GPIO_FUNC77_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC77_IN_SEL_msb, self.__GPIO_FUNC77_IN_SEL_lsb, value)
class GPIO_FUNC78_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x268
        self.__GPIO_SIG78_IN_SEL_lsb = 7
        self.__GPIO_SIG78_IN_SEL_msb = 7
        self.__GPIO_FUNC78_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC78_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC78_IN_SEL_lsb = 0
        self.__GPIO_FUNC78_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG78_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG78_IN_SEL_msb, self.__GPIO_SIG78_IN_SEL_lsb)
    @GPIO_SIG78_IN_SEL.setter
    def GPIO_SIG78_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG78_IN_SEL_msb, self.__GPIO_SIG78_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC78_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC78_IN_INV_SEL_msb, self.__GPIO_FUNC78_IN_INV_SEL_lsb)
    @GPIO_FUNC78_IN_INV_SEL.setter
    def GPIO_FUNC78_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC78_IN_INV_SEL_msb, self.__GPIO_FUNC78_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC78_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC78_IN_SEL_msb, self.__GPIO_FUNC78_IN_SEL_lsb)
    @GPIO_FUNC78_IN_SEL.setter
    def GPIO_FUNC78_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC78_IN_SEL_msb, self.__GPIO_FUNC78_IN_SEL_lsb, value)
class GPIO_FUNC79_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x26c
        self.__GPIO_SIG79_IN_SEL_lsb = 7
        self.__GPIO_SIG79_IN_SEL_msb = 7
        self.__GPIO_FUNC79_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC79_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC79_IN_SEL_lsb = 0
        self.__GPIO_FUNC79_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG79_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG79_IN_SEL_msb, self.__GPIO_SIG79_IN_SEL_lsb)
    @GPIO_SIG79_IN_SEL.setter
    def GPIO_SIG79_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG79_IN_SEL_msb, self.__GPIO_SIG79_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC79_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC79_IN_INV_SEL_msb, self.__GPIO_FUNC79_IN_INV_SEL_lsb)
    @GPIO_FUNC79_IN_INV_SEL.setter
    def GPIO_FUNC79_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC79_IN_INV_SEL_msb, self.__GPIO_FUNC79_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC79_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC79_IN_SEL_msb, self.__GPIO_FUNC79_IN_SEL_lsb)
    @GPIO_FUNC79_IN_SEL.setter
    def GPIO_FUNC79_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC79_IN_SEL_msb, self.__GPIO_FUNC79_IN_SEL_lsb, value)
class GPIO_FUNC80_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x270
        self.__GPIO_SIG80_IN_SEL_lsb = 7
        self.__GPIO_SIG80_IN_SEL_msb = 7
        self.__GPIO_FUNC80_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC80_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC80_IN_SEL_lsb = 0
        self.__GPIO_FUNC80_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG80_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG80_IN_SEL_msb, self.__GPIO_SIG80_IN_SEL_lsb)
    @GPIO_SIG80_IN_SEL.setter
    def GPIO_SIG80_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG80_IN_SEL_msb, self.__GPIO_SIG80_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC80_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC80_IN_INV_SEL_msb, self.__GPIO_FUNC80_IN_INV_SEL_lsb)
    @GPIO_FUNC80_IN_INV_SEL.setter
    def GPIO_FUNC80_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC80_IN_INV_SEL_msb, self.__GPIO_FUNC80_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC80_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC80_IN_SEL_msb, self.__GPIO_FUNC80_IN_SEL_lsb)
    @GPIO_FUNC80_IN_SEL.setter
    def GPIO_FUNC80_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC80_IN_SEL_msb, self.__GPIO_FUNC80_IN_SEL_lsb, value)
class GPIO_FUNC81_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x274
        self.__GPIO_SIG81_IN_SEL_lsb = 7
        self.__GPIO_SIG81_IN_SEL_msb = 7
        self.__GPIO_FUNC81_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC81_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC81_IN_SEL_lsb = 0
        self.__GPIO_FUNC81_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG81_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG81_IN_SEL_msb, self.__GPIO_SIG81_IN_SEL_lsb)
    @GPIO_SIG81_IN_SEL.setter
    def GPIO_SIG81_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG81_IN_SEL_msb, self.__GPIO_SIG81_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC81_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC81_IN_INV_SEL_msb, self.__GPIO_FUNC81_IN_INV_SEL_lsb)
    @GPIO_FUNC81_IN_INV_SEL.setter
    def GPIO_FUNC81_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC81_IN_INV_SEL_msb, self.__GPIO_FUNC81_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC81_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC81_IN_SEL_msb, self.__GPIO_FUNC81_IN_SEL_lsb)
    @GPIO_FUNC81_IN_SEL.setter
    def GPIO_FUNC81_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC81_IN_SEL_msb, self.__GPIO_FUNC81_IN_SEL_lsb, value)
class GPIO_FUNC82_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x278
        self.__GPIO_SIG82_IN_SEL_lsb = 7
        self.__GPIO_SIG82_IN_SEL_msb = 7
        self.__GPIO_FUNC82_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC82_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC82_IN_SEL_lsb = 0
        self.__GPIO_FUNC82_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG82_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG82_IN_SEL_msb, self.__GPIO_SIG82_IN_SEL_lsb)
    @GPIO_SIG82_IN_SEL.setter
    def GPIO_SIG82_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG82_IN_SEL_msb, self.__GPIO_SIG82_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC82_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC82_IN_INV_SEL_msb, self.__GPIO_FUNC82_IN_INV_SEL_lsb)
    @GPIO_FUNC82_IN_INV_SEL.setter
    def GPIO_FUNC82_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC82_IN_INV_SEL_msb, self.__GPIO_FUNC82_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC82_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC82_IN_SEL_msb, self.__GPIO_FUNC82_IN_SEL_lsb)
    @GPIO_FUNC82_IN_SEL.setter
    def GPIO_FUNC82_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC82_IN_SEL_msb, self.__GPIO_FUNC82_IN_SEL_lsb, value)
class GPIO_FUNC83_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x27c
        self.__GPIO_SIG83_IN_SEL_lsb = 7
        self.__GPIO_SIG83_IN_SEL_msb = 7
        self.__GPIO_FUNC83_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC83_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC83_IN_SEL_lsb = 0
        self.__GPIO_FUNC83_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG83_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG83_IN_SEL_msb, self.__GPIO_SIG83_IN_SEL_lsb)
    @GPIO_SIG83_IN_SEL.setter
    def GPIO_SIG83_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG83_IN_SEL_msb, self.__GPIO_SIG83_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC83_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC83_IN_INV_SEL_msb, self.__GPIO_FUNC83_IN_INV_SEL_lsb)
    @GPIO_FUNC83_IN_INV_SEL.setter
    def GPIO_FUNC83_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC83_IN_INV_SEL_msb, self.__GPIO_FUNC83_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC83_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC83_IN_SEL_msb, self.__GPIO_FUNC83_IN_SEL_lsb)
    @GPIO_FUNC83_IN_SEL.setter
    def GPIO_FUNC83_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC83_IN_SEL_msb, self.__GPIO_FUNC83_IN_SEL_lsb, value)
class GPIO_FUNC84_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x280
        self.__GPIO_SIG84_IN_SEL_lsb = 7
        self.__GPIO_SIG84_IN_SEL_msb = 7
        self.__GPIO_FUNC84_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC84_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC84_IN_SEL_lsb = 0
        self.__GPIO_FUNC84_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG84_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG84_IN_SEL_msb, self.__GPIO_SIG84_IN_SEL_lsb)
    @GPIO_SIG84_IN_SEL.setter
    def GPIO_SIG84_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG84_IN_SEL_msb, self.__GPIO_SIG84_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC84_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC84_IN_INV_SEL_msb, self.__GPIO_FUNC84_IN_INV_SEL_lsb)
    @GPIO_FUNC84_IN_INV_SEL.setter
    def GPIO_FUNC84_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC84_IN_INV_SEL_msb, self.__GPIO_FUNC84_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC84_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC84_IN_SEL_msb, self.__GPIO_FUNC84_IN_SEL_lsb)
    @GPIO_FUNC84_IN_SEL.setter
    def GPIO_FUNC84_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC84_IN_SEL_msb, self.__GPIO_FUNC84_IN_SEL_lsb, value)
class GPIO_FUNC85_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x284
        self.__GPIO_SIG85_IN_SEL_lsb = 7
        self.__GPIO_SIG85_IN_SEL_msb = 7
        self.__GPIO_FUNC85_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC85_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC85_IN_SEL_lsb = 0
        self.__GPIO_FUNC85_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG85_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG85_IN_SEL_msb, self.__GPIO_SIG85_IN_SEL_lsb)
    @GPIO_SIG85_IN_SEL.setter
    def GPIO_SIG85_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG85_IN_SEL_msb, self.__GPIO_SIG85_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC85_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC85_IN_INV_SEL_msb, self.__GPIO_FUNC85_IN_INV_SEL_lsb)
    @GPIO_FUNC85_IN_INV_SEL.setter
    def GPIO_FUNC85_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC85_IN_INV_SEL_msb, self.__GPIO_FUNC85_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC85_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC85_IN_SEL_msb, self.__GPIO_FUNC85_IN_SEL_lsb)
    @GPIO_FUNC85_IN_SEL.setter
    def GPIO_FUNC85_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC85_IN_SEL_msb, self.__GPIO_FUNC85_IN_SEL_lsb, value)
class GPIO_FUNC86_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x288
        self.__GPIO_SIG86_IN_SEL_lsb = 7
        self.__GPIO_SIG86_IN_SEL_msb = 7
        self.__GPIO_FUNC86_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC86_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC86_IN_SEL_lsb = 0
        self.__GPIO_FUNC86_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG86_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG86_IN_SEL_msb, self.__GPIO_SIG86_IN_SEL_lsb)
    @GPIO_SIG86_IN_SEL.setter
    def GPIO_SIG86_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG86_IN_SEL_msb, self.__GPIO_SIG86_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC86_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC86_IN_INV_SEL_msb, self.__GPIO_FUNC86_IN_INV_SEL_lsb)
    @GPIO_FUNC86_IN_INV_SEL.setter
    def GPIO_FUNC86_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC86_IN_INV_SEL_msb, self.__GPIO_FUNC86_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC86_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC86_IN_SEL_msb, self.__GPIO_FUNC86_IN_SEL_lsb)
    @GPIO_FUNC86_IN_SEL.setter
    def GPIO_FUNC86_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC86_IN_SEL_msb, self.__GPIO_FUNC86_IN_SEL_lsb, value)
class GPIO_FUNC87_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x28c
        self.__GPIO_SIG87_IN_SEL_lsb = 7
        self.__GPIO_SIG87_IN_SEL_msb = 7
        self.__GPIO_FUNC87_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC87_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC87_IN_SEL_lsb = 0
        self.__GPIO_FUNC87_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG87_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG87_IN_SEL_msb, self.__GPIO_SIG87_IN_SEL_lsb)
    @GPIO_SIG87_IN_SEL.setter
    def GPIO_SIG87_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG87_IN_SEL_msb, self.__GPIO_SIG87_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC87_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC87_IN_INV_SEL_msb, self.__GPIO_FUNC87_IN_INV_SEL_lsb)
    @GPIO_FUNC87_IN_INV_SEL.setter
    def GPIO_FUNC87_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC87_IN_INV_SEL_msb, self.__GPIO_FUNC87_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC87_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC87_IN_SEL_msb, self.__GPIO_FUNC87_IN_SEL_lsb)
    @GPIO_FUNC87_IN_SEL.setter
    def GPIO_FUNC87_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC87_IN_SEL_msb, self.__GPIO_FUNC87_IN_SEL_lsb, value)
class GPIO_FUNC88_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x290
        self.__GPIO_SIG88_IN_SEL_lsb = 7
        self.__GPIO_SIG88_IN_SEL_msb = 7
        self.__GPIO_FUNC88_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC88_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC88_IN_SEL_lsb = 0
        self.__GPIO_FUNC88_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG88_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG88_IN_SEL_msb, self.__GPIO_SIG88_IN_SEL_lsb)
    @GPIO_SIG88_IN_SEL.setter
    def GPIO_SIG88_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG88_IN_SEL_msb, self.__GPIO_SIG88_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC88_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC88_IN_INV_SEL_msb, self.__GPIO_FUNC88_IN_INV_SEL_lsb)
    @GPIO_FUNC88_IN_INV_SEL.setter
    def GPIO_FUNC88_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC88_IN_INV_SEL_msb, self.__GPIO_FUNC88_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC88_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC88_IN_SEL_msb, self.__GPIO_FUNC88_IN_SEL_lsb)
    @GPIO_FUNC88_IN_SEL.setter
    def GPIO_FUNC88_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC88_IN_SEL_msb, self.__GPIO_FUNC88_IN_SEL_lsb, value)
class GPIO_FUNC89_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x294
        self.__GPIO_SIG89_IN_SEL_lsb = 7
        self.__GPIO_SIG89_IN_SEL_msb = 7
        self.__GPIO_FUNC89_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC89_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC89_IN_SEL_lsb = 0
        self.__GPIO_FUNC89_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG89_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG89_IN_SEL_msb, self.__GPIO_SIG89_IN_SEL_lsb)
    @GPIO_SIG89_IN_SEL.setter
    def GPIO_SIG89_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG89_IN_SEL_msb, self.__GPIO_SIG89_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC89_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC89_IN_INV_SEL_msb, self.__GPIO_FUNC89_IN_INV_SEL_lsb)
    @GPIO_FUNC89_IN_INV_SEL.setter
    def GPIO_FUNC89_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC89_IN_INV_SEL_msb, self.__GPIO_FUNC89_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC89_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC89_IN_SEL_msb, self.__GPIO_FUNC89_IN_SEL_lsb)
    @GPIO_FUNC89_IN_SEL.setter
    def GPIO_FUNC89_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC89_IN_SEL_msb, self.__GPIO_FUNC89_IN_SEL_lsb, value)
class GPIO_FUNC90_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x298
        self.__GPIO_SIG90_IN_SEL_lsb = 7
        self.__GPIO_SIG90_IN_SEL_msb = 7
        self.__GPIO_FUNC90_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC90_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC90_IN_SEL_lsb = 0
        self.__GPIO_FUNC90_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG90_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG90_IN_SEL_msb, self.__GPIO_SIG90_IN_SEL_lsb)
    @GPIO_SIG90_IN_SEL.setter
    def GPIO_SIG90_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG90_IN_SEL_msb, self.__GPIO_SIG90_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC90_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC90_IN_INV_SEL_msb, self.__GPIO_FUNC90_IN_INV_SEL_lsb)
    @GPIO_FUNC90_IN_INV_SEL.setter
    def GPIO_FUNC90_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC90_IN_INV_SEL_msb, self.__GPIO_FUNC90_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC90_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC90_IN_SEL_msb, self.__GPIO_FUNC90_IN_SEL_lsb)
    @GPIO_FUNC90_IN_SEL.setter
    def GPIO_FUNC90_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC90_IN_SEL_msb, self.__GPIO_FUNC90_IN_SEL_lsb, value)
class GPIO_FUNC91_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x29c
        self.__GPIO_SIG91_IN_SEL_lsb = 7
        self.__GPIO_SIG91_IN_SEL_msb = 7
        self.__GPIO_FUNC91_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC91_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC91_IN_SEL_lsb = 0
        self.__GPIO_FUNC91_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG91_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG91_IN_SEL_msb, self.__GPIO_SIG91_IN_SEL_lsb)
    @GPIO_SIG91_IN_SEL.setter
    def GPIO_SIG91_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG91_IN_SEL_msb, self.__GPIO_SIG91_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC91_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC91_IN_INV_SEL_msb, self.__GPIO_FUNC91_IN_INV_SEL_lsb)
    @GPIO_FUNC91_IN_INV_SEL.setter
    def GPIO_FUNC91_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC91_IN_INV_SEL_msb, self.__GPIO_FUNC91_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC91_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC91_IN_SEL_msb, self.__GPIO_FUNC91_IN_SEL_lsb)
    @GPIO_FUNC91_IN_SEL.setter
    def GPIO_FUNC91_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC91_IN_SEL_msb, self.__GPIO_FUNC91_IN_SEL_lsb, value)
class GPIO_FUNC92_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x2a0
        self.__GPIO_SIG92_IN_SEL_lsb = 7
        self.__GPIO_SIG92_IN_SEL_msb = 7
        self.__GPIO_FUNC92_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC92_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC92_IN_SEL_lsb = 0
        self.__GPIO_FUNC92_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG92_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG92_IN_SEL_msb, self.__GPIO_SIG92_IN_SEL_lsb)
    @GPIO_SIG92_IN_SEL.setter
    def GPIO_SIG92_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG92_IN_SEL_msb, self.__GPIO_SIG92_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC92_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC92_IN_INV_SEL_msb, self.__GPIO_FUNC92_IN_INV_SEL_lsb)
    @GPIO_FUNC92_IN_INV_SEL.setter
    def GPIO_FUNC92_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC92_IN_INV_SEL_msb, self.__GPIO_FUNC92_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC92_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC92_IN_SEL_msb, self.__GPIO_FUNC92_IN_SEL_lsb)
    @GPIO_FUNC92_IN_SEL.setter
    def GPIO_FUNC92_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC92_IN_SEL_msb, self.__GPIO_FUNC92_IN_SEL_lsb, value)
class GPIO_FUNC93_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x2a4
        self.__GPIO_SIG93_IN_SEL_lsb = 7
        self.__GPIO_SIG93_IN_SEL_msb = 7
        self.__GPIO_FUNC93_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC93_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC93_IN_SEL_lsb = 0
        self.__GPIO_FUNC93_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG93_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG93_IN_SEL_msb, self.__GPIO_SIG93_IN_SEL_lsb)
    @GPIO_SIG93_IN_SEL.setter
    def GPIO_SIG93_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG93_IN_SEL_msb, self.__GPIO_SIG93_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC93_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC93_IN_INV_SEL_msb, self.__GPIO_FUNC93_IN_INV_SEL_lsb)
    @GPIO_FUNC93_IN_INV_SEL.setter
    def GPIO_FUNC93_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC93_IN_INV_SEL_msb, self.__GPIO_FUNC93_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC93_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC93_IN_SEL_msb, self.__GPIO_FUNC93_IN_SEL_lsb)
    @GPIO_FUNC93_IN_SEL.setter
    def GPIO_FUNC93_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC93_IN_SEL_msb, self.__GPIO_FUNC93_IN_SEL_lsb, value)
class GPIO_FUNC94_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x2a8
        self.__GPIO_SIG94_IN_SEL_lsb = 7
        self.__GPIO_SIG94_IN_SEL_msb = 7
        self.__GPIO_FUNC94_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC94_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC94_IN_SEL_lsb = 0
        self.__GPIO_FUNC94_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG94_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG94_IN_SEL_msb, self.__GPIO_SIG94_IN_SEL_lsb)
    @GPIO_SIG94_IN_SEL.setter
    def GPIO_SIG94_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG94_IN_SEL_msb, self.__GPIO_SIG94_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC94_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC94_IN_INV_SEL_msb, self.__GPIO_FUNC94_IN_INV_SEL_lsb)
    @GPIO_FUNC94_IN_INV_SEL.setter
    def GPIO_FUNC94_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC94_IN_INV_SEL_msb, self.__GPIO_FUNC94_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC94_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC94_IN_SEL_msb, self.__GPIO_FUNC94_IN_SEL_lsb)
    @GPIO_FUNC94_IN_SEL.setter
    def GPIO_FUNC94_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC94_IN_SEL_msb, self.__GPIO_FUNC94_IN_SEL_lsb, value)
class GPIO_FUNC95_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x2ac
        self.__GPIO_SIG95_IN_SEL_lsb = 7
        self.__GPIO_SIG95_IN_SEL_msb = 7
        self.__GPIO_FUNC95_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC95_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC95_IN_SEL_lsb = 0
        self.__GPIO_FUNC95_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG95_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG95_IN_SEL_msb, self.__GPIO_SIG95_IN_SEL_lsb)
    @GPIO_SIG95_IN_SEL.setter
    def GPIO_SIG95_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG95_IN_SEL_msb, self.__GPIO_SIG95_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC95_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC95_IN_INV_SEL_msb, self.__GPIO_FUNC95_IN_INV_SEL_lsb)
    @GPIO_FUNC95_IN_INV_SEL.setter
    def GPIO_FUNC95_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC95_IN_INV_SEL_msb, self.__GPIO_FUNC95_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC95_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC95_IN_SEL_msb, self.__GPIO_FUNC95_IN_SEL_lsb)
    @GPIO_FUNC95_IN_SEL.setter
    def GPIO_FUNC95_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC95_IN_SEL_msb, self.__GPIO_FUNC95_IN_SEL_lsb, value)
class GPIO_FUNC96_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x2b0
        self.__GPIO_SIG96_IN_SEL_lsb = 7
        self.__GPIO_SIG96_IN_SEL_msb = 7
        self.__GPIO_FUNC96_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC96_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC96_IN_SEL_lsb = 0
        self.__GPIO_FUNC96_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG96_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG96_IN_SEL_msb, self.__GPIO_SIG96_IN_SEL_lsb)
    @GPIO_SIG96_IN_SEL.setter
    def GPIO_SIG96_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG96_IN_SEL_msb, self.__GPIO_SIG96_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC96_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC96_IN_INV_SEL_msb, self.__GPIO_FUNC96_IN_INV_SEL_lsb)
    @GPIO_FUNC96_IN_INV_SEL.setter
    def GPIO_FUNC96_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC96_IN_INV_SEL_msb, self.__GPIO_FUNC96_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC96_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC96_IN_SEL_msb, self.__GPIO_FUNC96_IN_SEL_lsb)
    @GPIO_FUNC96_IN_SEL.setter
    def GPIO_FUNC96_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC96_IN_SEL_msb, self.__GPIO_FUNC96_IN_SEL_lsb, value)
class GPIO_FUNC97_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x2b4
        self.__GPIO_SIG97_IN_SEL_lsb = 7
        self.__GPIO_SIG97_IN_SEL_msb = 7
        self.__GPIO_FUNC97_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC97_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC97_IN_SEL_lsb = 0
        self.__GPIO_FUNC97_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG97_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG97_IN_SEL_msb, self.__GPIO_SIG97_IN_SEL_lsb)
    @GPIO_SIG97_IN_SEL.setter
    def GPIO_SIG97_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG97_IN_SEL_msb, self.__GPIO_SIG97_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC97_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC97_IN_INV_SEL_msb, self.__GPIO_FUNC97_IN_INV_SEL_lsb)
    @GPIO_FUNC97_IN_INV_SEL.setter
    def GPIO_FUNC97_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC97_IN_INV_SEL_msb, self.__GPIO_FUNC97_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC97_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC97_IN_SEL_msb, self.__GPIO_FUNC97_IN_SEL_lsb)
    @GPIO_FUNC97_IN_SEL.setter
    def GPIO_FUNC97_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC97_IN_SEL_msb, self.__GPIO_FUNC97_IN_SEL_lsb, value)
class GPIO_FUNC98_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x2b8
        self.__GPIO_SIG98_IN_SEL_lsb = 7
        self.__GPIO_SIG98_IN_SEL_msb = 7
        self.__GPIO_FUNC98_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC98_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC98_IN_SEL_lsb = 0
        self.__GPIO_FUNC98_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG98_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG98_IN_SEL_msb, self.__GPIO_SIG98_IN_SEL_lsb)
    @GPIO_SIG98_IN_SEL.setter
    def GPIO_SIG98_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG98_IN_SEL_msb, self.__GPIO_SIG98_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC98_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC98_IN_INV_SEL_msb, self.__GPIO_FUNC98_IN_INV_SEL_lsb)
    @GPIO_FUNC98_IN_INV_SEL.setter
    def GPIO_FUNC98_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC98_IN_INV_SEL_msb, self.__GPIO_FUNC98_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC98_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC98_IN_SEL_msb, self.__GPIO_FUNC98_IN_SEL_lsb)
    @GPIO_FUNC98_IN_SEL.setter
    def GPIO_FUNC98_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC98_IN_SEL_msb, self.__GPIO_FUNC98_IN_SEL_lsb, value)
class GPIO_FUNC99_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x2bc
        self.__GPIO_SIG99_IN_SEL_lsb = 7
        self.__GPIO_SIG99_IN_SEL_msb = 7
        self.__GPIO_FUNC99_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC99_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC99_IN_SEL_lsb = 0
        self.__GPIO_FUNC99_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG99_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG99_IN_SEL_msb, self.__GPIO_SIG99_IN_SEL_lsb)
    @GPIO_SIG99_IN_SEL.setter
    def GPIO_SIG99_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG99_IN_SEL_msb, self.__GPIO_SIG99_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC99_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC99_IN_INV_SEL_msb, self.__GPIO_FUNC99_IN_INV_SEL_lsb)
    @GPIO_FUNC99_IN_INV_SEL.setter
    def GPIO_FUNC99_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC99_IN_INV_SEL_msb, self.__GPIO_FUNC99_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC99_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC99_IN_SEL_msb, self.__GPIO_FUNC99_IN_SEL_lsb)
    @GPIO_FUNC99_IN_SEL.setter
    def GPIO_FUNC99_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC99_IN_SEL_msb, self.__GPIO_FUNC99_IN_SEL_lsb, value)
class GPIO_FUNC100_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x2c0
        self.__GPIO_SIG100_IN_SEL_lsb = 7
        self.__GPIO_SIG100_IN_SEL_msb = 7
        self.__GPIO_FUNC100_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC100_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC100_IN_SEL_lsb = 0
        self.__GPIO_FUNC100_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG100_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG100_IN_SEL_msb, self.__GPIO_SIG100_IN_SEL_lsb)
    @GPIO_SIG100_IN_SEL.setter
    def GPIO_SIG100_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG100_IN_SEL_msb, self.__GPIO_SIG100_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC100_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC100_IN_INV_SEL_msb, self.__GPIO_FUNC100_IN_INV_SEL_lsb)
    @GPIO_FUNC100_IN_INV_SEL.setter
    def GPIO_FUNC100_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC100_IN_INV_SEL_msb, self.__GPIO_FUNC100_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC100_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC100_IN_SEL_msb, self.__GPIO_FUNC100_IN_SEL_lsb)
    @GPIO_FUNC100_IN_SEL.setter
    def GPIO_FUNC100_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC100_IN_SEL_msb, self.__GPIO_FUNC100_IN_SEL_lsb, value)
class GPIO_FUNC101_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x2c4
        self.__GPIO_SIG101_IN_SEL_lsb = 7
        self.__GPIO_SIG101_IN_SEL_msb = 7
        self.__GPIO_FUNC101_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC101_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC101_IN_SEL_lsb = 0
        self.__GPIO_FUNC101_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG101_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG101_IN_SEL_msb, self.__GPIO_SIG101_IN_SEL_lsb)
    @GPIO_SIG101_IN_SEL.setter
    def GPIO_SIG101_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG101_IN_SEL_msb, self.__GPIO_SIG101_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC101_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC101_IN_INV_SEL_msb, self.__GPIO_FUNC101_IN_INV_SEL_lsb)
    @GPIO_FUNC101_IN_INV_SEL.setter
    def GPIO_FUNC101_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC101_IN_INV_SEL_msb, self.__GPIO_FUNC101_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC101_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC101_IN_SEL_msb, self.__GPIO_FUNC101_IN_SEL_lsb)
    @GPIO_FUNC101_IN_SEL.setter
    def GPIO_FUNC101_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC101_IN_SEL_msb, self.__GPIO_FUNC101_IN_SEL_lsb, value)
class GPIO_FUNC102_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x2c8
        self.__GPIO_SIG102_IN_SEL_lsb = 7
        self.__GPIO_SIG102_IN_SEL_msb = 7
        self.__GPIO_FUNC102_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC102_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC102_IN_SEL_lsb = 0
        self.__GPIO_FUNC102_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG102_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG102_IN_SEL_msb, self.__GPIO_SIG102_IN_SEL_lsb)
    @GPIO_SIG102_IN_SEL.setter
    def GPIO_SIG102_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG102_IN_SEL_msb, self.__GPIO_SIG102_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC102_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC102_IN_INV_SEL_msb, self.__GPIO_FUNC102_IN_INV_SEL_lsb)
    @GPIO_FUNC102_IN_INV_SEL.setter
    def GPIO_FUNC102_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC102_IN_INV_SEL_msb, self.__GPIO_FUNC102_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC102_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC102_IN_SEL_msb, self.__GPIO_FUNC102_IN_SEL_lsb)
    @GPIO_FUNC102_IN_SEL.setter
    def GPIO_FUNC102_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC102_IN_SEL_msb, self.__GPIO_FUNC102_IN_SEL_lsb, value)
class GPIO_FUNC103_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x2cc
        self.__GPIO_SIG103_IN_SEL_lsb = 7
        self.__GPIO_SIG103_IN_SEL_msb = 7
        self.__GPIO_FUNC103_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC103_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC103_IN_SEL_lsb = 0
        self.__GPIO_FUNC103_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG103_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG103_IN_SEL_msb, self.__GPIO_SIG103_IN_SEL_lsb)
    @GPIO_SIG103_IN_SEL.setter
    def GPIO_SIG103_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG103_IN_SEL_msb, self.__GPIO_SIG103_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC103_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC103_IN_INV_SEL_msb, self.__GPIO_FUNC103_IN_INV_SEL_lsb)
    @GPIO_FUNC103_IN_INV_SEL.setter
    def GPIO_FUNC103_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC103_IN_INV_SEL_msb, self.__GPIO_FUNC103_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC103_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC103_IN_SEL_msb, self.__GPIO_FUNC103_IN_SEL_lsb)
    @GPIO_FUNC103_IN_SEL.setter
    def GPIO_FUNC103_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC103_IN_SEL_msb, self.__GPIO_FUNC103_IN_SEL_lsb, value)
class GPIO_FUNC104_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x2d0
        self.__GPIO_SIG104_IN_SEL_lsb = 7
        self.__GPIO_SIG104_IN_SEL_msb = 7
        self.__GPIO_FUNC104_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC104_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC104_IN_SEL_lsb = 0
        self.__GPIO_FUNC104_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG104_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG104_IN_SEL_msb, self.__GPIO_SIG104_IN_SEL_lsb)
    @GPIO_SIG104_IN_SEL.setter
    def GPIO_SIG104_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG104_IN_SEL_msb, self.__GPIO_SIG104_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC104_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC104_IN_INV_SEL_msb, self.__GPIO_FUNC104_IN_INV_SEL_lsb)
    @GPIO_FUNC104_IN_INV_SEL.setter
    def GPIO_FUNC104_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC104_IN_INV_SEL_msb, self.__GPIO_FUNC104_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC104_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC104_IN_SEL_msb, self.__GPIO_FUNC104_IN_SEL_lsb)
    @GPIO_FUNC104_IN_SEL.setter
    def GPIO_FUNC104_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC104_IN_SEL_msb, self.__GPIO_FUNC104_IN_SEL_lsb, value)
class GPIO_FUNC105_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x2d4
        self.__GPIO_SIG105_IN_SEL_lsb = 7
        self.__GPIO_SIG105_IN_SEL_msb = 7
        self.__GPIO_FUNC105_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC105_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC105_IN_SEL_lsb = 0
        self.__GPIO_FUNC105_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG105_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG105_IN_SEL_msb, self.__GPIO_SIG105_IN_SEL_lsb)
    @GPIO_SIG105_IN_SEL.setter
    def GPIO_SIG105_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG105_IN_SEL_msb, self.__GPIO_SIG105_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC105_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC105_IN_INV_SEL_msb, self.__GPIO_FUNC105_IN_INV_SEL_lsb)
    @GPIO_FUNC105_IN_INV_SEL.setter
    def GPIO_FUNC105_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC105_IN_INV_SEL_msb, self.__GPIO_FUNC105_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC105_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC105_IN_SEL_msb, self.__GPIO_FUNC105_IN_SEL_lsb)
    @GPIO_FUNC105_IN_SEL.setter
    def GPIO_FUNC105_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC105_IN_SEL_msb, self.__GPIO_FUNC105_IN_SEL_lsb, value)
class GPIO_FUNC106_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x2d8
        self.__GPIO_SIG106_IN_SEL_lsb = 7
        self.__GPIO_SIG106_IN_SEL_msb = 7
        self.__GPIO_FUNC106_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC106_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC106_IN_SEL_lsb = 0
        self.__GPIO_FUNC106_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG106_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG106_IN_SEL_msb, self.__GPIO_SIG106_IN_SEL_lsb)
    @GPIO_SIG106_IN_SEL.setter
    def GPIO_SIG106_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG106_IN_SEL_msb, self.__GPIO_SIG106_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC106_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC106_IN_INV_SEL_msb, self.__GPIO_FUNC106_IN_INV_SEL_lsb)
    @GPIO_FUNC106_IN_INV_SEL.setter
    def GPIO_FUNC106_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC106_IN_INV_SEL_msb, self.__GPIO_FUNC106_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC106_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC106_IN_SEL_msb, self.__GPIO_FUNC106_IN_SEL_lsb)
    @GPIO_FUNC106_IN_SEL.setter
    def GPIO_FUNC106_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC106_IN_SEL_msb, self.__GPIO_FUNC106_IN_SEL_lsb, value)
class GPIO_FUNC107_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x2dc
        self.__GPIO_SIG107_IN_SEL_lsb = 7
        self.__GPIO_SIG107_IN_SEL_msb = 7
        self.__GPIO_FUNC107_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC107_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC107_IN_SEL_lsb = 0
        self.__GPIO_FUNC107_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG107_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG107_IN_SEL_msb, self.__GPIO_SIG107_IN_SEL_lsb)
    @GPIO_SIG107_IN_SEL.setter
    def GPIO_SIG107_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG107_IN_SEL_msb, self.__GPIO_SIG107_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC107_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC107_IN_INV_SEL_msb, self.__GPIO_FUNC107_IN_INV_SEL_lsb)
    @GPIO_FUNC107_IN_INV_SEL.setter
    def GPIO_FUNC107_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC107_IN_INV_SEL_msb, self.__GPIO_FUNC107_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC107_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC107_IN_SEL_msb, self.__GPIO_FUNC107_IN_SEL_lsb)
    @GPIO_FUNC107_IN_SEL.setter
    def GPIO_FUNC107_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC107_IN_SEL_msb, self.__GPIO_FUNC107_IN_SEL_lsb, value)
class GPIO_FUNC108_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x2e0
        self.__GPIO_SIG108_IN_SEL_lsb = 7
        self.__GPIO_SIG108_IN_SEL_msb = 7
        self.__GPIO_FUNC108_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC108_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC108_IN_SEL_lsb = 0
        self.__GPIO_FUNC108_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG108_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG108_IN_SEL_msb, self.__GPIO_SIG108_IN_SEL_lsb)
    @GPIO_SIG108_IN_SEL.setter
    def GPIO_SIG108_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG108_IN_SEL_msb, self.__GPIO_SIG108_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC108_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC108_IN_INV_SEL_msb, self.__GPIO_FUNC108_IN_INV_SEL_lsb)
    @GPIO_FUNC108_IN_INV_SEL.setter
    def GPIO_FUNC108_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC108_IN_INV_SEL_msb, self.__GPIO_FUNC108_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC108_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC108_IN_SEL_msb, self.__GPIO_FUNC108_IN_SEL_lsb)
    @GPIO_FUNC108_IN_SEL.setter
    def GPIO_FUNC108_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC108_IN_SEL_msb, self.__GPIO_FUNC108_IN_SEL_lsb, value)
class GPIO_FUNC109_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x2e4
        self.__GPIO_SIG109_IN_SEL_lsb = 7
        self.__GPIO_SIG109_IN_SEL_msb = 7
        self.__GPIO_FUNC109_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC109_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC109_IN_SEL_lsb = 0
        self.__GPIO_FUNC109_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG109_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG109_IN_SEL_msb, self.__GPIO_SIG109_IN_SEL_lsb)
    @GPIO_SIG109_IN_SEL.setter
    def GPIO_SIG109_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG109_IN_SEL_msb, self.__GPIO_SIG109_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC109_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC109_IN_INV_SEL_msb, self.__GPIO_FUNC109_IN_INV_SEL_lsb)
    @GPIO_FUNC109_IN_INV_SEL.setter
    def GPIO_FUNC109_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC109_IN_INV_SEL_msb, self.__GPIO_FUNC109_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC109_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC109_IN_SEL_msb, self.__GPIO_FUNC109_IN_SEL_lsb)
    @GPIO_FUNC109_IN_SEL.setter
    def GPIO_FUNC109_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC109_IN_SEL_msb, self.__GPIO_FUNC109_IN_SEL_lsb, value)
class GPIO_FUNC110_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x2e8
        self.__GPIO_SIG110_IN_SEL_lsb = 7
        self.__GPIO_SIG110_IN_SEL_msb = 7
        self.__GPIO_FUNC110_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC110_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC110_IN_SEL_lsb = 0
        self.__GPIO_FUNC110_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG110_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG110_IN_SEL_msb, self.__GPIO_SIG110_IN_SEL_lsb)
    @GPIO_SIG110_IN_SEL.setter
    def GPIO_SIG110_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG110_IN_SEL_msb, self.__GPIO_SIG110_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC110_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC110_IN_INV_SEL_msb, self.__GPIO_FUNC110_IN_INV_SEL_lsb)
    @GPIO_FUNC110_IN_INV_SEL.setter
    def GPIO_FUNC110_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC110_IN_INV_SEL_msb, self.__GPIO_FUNC110_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC110_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC110_IN_SEL_msb, self.__GPIO_FUNC110_IN_SEL_lsb)
    @GPIO_FUNC110_IN_SEL.setter
    def GPIO_FUNC110_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC110_IN_SEL_msb, self.__GPIO_FUNC110_IN_SEL_lsb, value)
class GPIO_FUNC111_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x2ec
        self.__GPIO_SIG111_IN_SEL_lsb = 7
        self.__GPIO_SIG111_IN_SEL_msb = 7
        self.__GPIO_FUNC111_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC111_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC111_IN_SEL_lsb = 0
        self.__GPIO_FUNC111_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG111_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG111_IN_SEL_msb, self.__GPIO_SIG111_IN_SEL_lsb)
    @GPIO_SIG111_IN_SEL.setter
    def GPIO_SIG111_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG111_IN_SEL_msb, self.__GPIO_SIG111_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC111_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC111_IN_INV_SEL_msb, self.__GPIO_FUNC111_IN_INV_SEL_lsb)
    @GPIO_FUNC111_IN_INV_SEL.setter
    def GPIO_FUNC111_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC111_IN_INV_SEL_msb, self.__GPIO_FUNC111_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC111_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC111_IN_SEL_msb, self.__GPIO_FUNC111_IN_SEL_lsb)
    @GPIO_FUNC111_IN_SEL.setter
    def GPIO_FUNC111_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC111_IN_SEL_msb, self.__GPIO_FUNC111_IN_SEL_lsb, value)
class GPIO_FUNC112_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x2f0
        self.__GPIO_SIG112_IN_SEL_lsb = 7
        self.__GPIO_SIG112_IN_SEL_msb = 7
        self.__GPIO_FUNC112_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC112_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC112_IN_SEL_lsb = 0
        self.__GPIO_FUNC112_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG112_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG112_IN_SEL_msb, self.__GPIO_SIG112_IN_SEL_lsb)
    @GPIO_SIG112_IN_SEL.setter
    def GPIO_SIG112_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG112_IN_SEL_msb, self.__GPIO_SIG112_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC112_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC112_IN_INV_SEL_msb, self.__GPIO_FUNC112_IN_INV_SEL_lsb)
    @GPIO_FUNC112_IN_INV_SEL.setter
    def GPIO_FUNC112_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC112_IN_INV_SEL_msb, self.__GPIO_FUNC112_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC112_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC112_IN_SEL_msb, self.__GPIO_FUNC112_IN_SEL_lsb)
    @GPIO_FUNC112_IN_SEL.setter
    def GPIO_FUNC112_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC112_IN_SEL_msb, self.__GPIO_FUNC112_IN_SEL_lsb, value)
class GPIO_FUNC113_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x2f4
        self.__GPIO_SIG113_IN_SEL_lsb = 7
        self.__GPIO_SIG113_IN_SEL_msb = 7
        self.__GPIO_FUNC113_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC113_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC113_IN_SEL_lsb = 0
        self.__GPIO_FUNC113_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG113_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG113_IN_SEL_msb, self.__GPIO_SIG113_IN_SEL_lsb)
    @GPIO_SIG113_IN_SEL.setter
    def GPIO_SIG113_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG113_IN_SEL_msb, self.__GPIO_SIG113_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC113_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC113_IN_INV_SEL_msb, self.__GPIO_FUNC113_IN_INV_SEL_lsb)
    @GPIO_FUNC113_IN_INV_SEL.setter
    def GPIO_FUNC113_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC113_IN_INV_SEL_msb, self.__GPIO_FUNC113_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC113_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC113_IN_SEL_msb, self.__GPIO_FUNC113_IN_SEL_lsb)
    @GPIO_FUNC113_IN_SEL.setter
    def GPIO_FUNC113_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC113_IN_SEL_msb, self.__GPIO_FUNC113_IN_SEL_lsb, value)
class GPIO_FUNC114_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x2f8
        self.__GPIO_SIG114_IN_SEL_lsb = 7
        self.__GPIO_SIG114_IN_SEL_msb = 7
        self.__GPIO_FUNC114_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC114_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC114_IN_SEL_lsb = 0
        self.__GPIO_FUNC114_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG114_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG114_IN_SEL_msb, self.__GPIO_SIG114_IN_SEL_lsb)
    @GPIO_SIG114_IN_SEL.setter
    def GPIO_SIG114_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG114_IN_SEL_msb, self.__GPIO_SIG114_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC114_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC114_IN_INV_SEL_msb, self.__GPIO_FUNC114_IN_INV_SEL_lsb)
    @GPIO_FUNC114_IN_INV_SEL.setter
    def GPIO_FUNC114_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC114_IN_INV_SEL_msb, self.__GPIO_FUNC114_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC114_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC114_IN_SEL_msb, self.__GPIO_FUNC114_IN_SEL_lsb)
    @GPIO_FUNC114_IN_SEL.setter
    def GPIO_FUNC114_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC114_IN_SEL_msb, self.__GPIO_FUNC114_IN_SEL_lsb, value)
class GPIO_FUNC115_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x2fc
        self.__GPIO_SIG115_IN_SEL_lsb = 7
        self.__GPIO_SIG115_IN_SEL_msb = 7
        self.__GPIO_FUNC115_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC115_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC115_IN_SEL_lsb = 0
        self.__GPIO_FUNC115_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG115_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG115_IN_SEL_msb, self.__GPIO_SIG115_IN_SEL_lsb)
    @GPIO_SIG115_IN_SEL.setter
    def GPIO_SIG115_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG115_IN_SEL_msb, self.__GPIO_SIG115_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC115_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC115_IN_INV_SEL_msb, self.__GPIO_FUNC115_IN_INV_SEL_lsb)
    @GPIO_FUNC115_IN_INV_SEL.setter
    def GPIO_FUNC115_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC115_IN_INV_SEL_msb, self.__GPIO_FUNC115_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC115_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC115_IN_SEL_msb, self.__GPIO_FUNC115_IN_SEL_lsb)
    @GPIO_FUNC115_IN_SEL.setter
    def GPIO_FUNC115_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC115_IN_SEL_msb, self.__GPIO_FUNC115_IN_SEL_lsb, value)
class GPIO_FUNC116_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x300
        self.__GPIO_SIG116_IN_SEL_lsb = 7
        self.__GPIO_SIG116_IN_SEL_msb = 7
        self.__GPIO_FUNC116_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC116_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC116_IN_SEL_lsb = 0
        self.__GPIO_FUNC116_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG116_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG116_IN_SEL_msb, self.__GPIO_SIG116_IN_SEL_lsb)
    @GPIO_SIG116_IN_SEL.setter
    def GPIO_SIG116_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG116_IN_SEL_msb, self.__GPIO_SIG116_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC116_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC116_IN_INV_SEL_msb, self.__GPIO_FUNC116_IN_INV_SEL_lsb)
    @GPIO_FUNC116_IN_INV_SEL.setter
    def GPIO_FUNC116_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC116_IN_INV_SEL_msb, self.__GPIO_FUNC116_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC116_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC116_IN_SEL_msb, self.__GPIO_FUNC116_IN_SEL_lsb)
    @GPIO_FUNC116_IN_SEL.setter
    def GPIO_FUNC116_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC116_IN_SEL_msb, self.__GPIO_FUNC116_IN_SEL_lsb, value)
class GPIO_FUNC117_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x304
        self.__GPIO_SIG117_IN_SEL_lsb = 7
        self.__GPIO_SIG117_IN_SEL_msb = 7
        self.__GPIO_FUNC117_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC117_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC117_IN_SEL_lsb = 0
        self.__GPIO_FUNC117_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG117_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG117_IN_SEL_msb, self.__GPIO_SIG117_IN_SEL_lsb)
    @GPIO_SIG117_IN_SEL.setter
    def GPIO_SIG117_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG117_IN_SEL_msb, self.__GPIO_SIG117_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC117_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC117_IN_INV_SEL_msb, self.__GPIO_FUNC117_IN_INV_SEL_lsb)
    @GPIO_FUNC117_IN_INV_SEL.setter
    def GPIO_FUNC117_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC117_IN_INV_SEL_msb, self.__GPIO_FUNC117_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC117_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC117_IN_SEL_msb, self.__GPIO_FUNC117_IN_SEL_lsb)
    @GPIO_FUNC117_IN_SEL.setter
    def GPIO_FUNC117_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC117_IN_SEL_msb, self.__GPIO_FUNC117_IN_SEL_lsb, value)
class GPIO_FUNC118_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x308
        self.__GPIO_SIG118_IN_SEL_lsb = 7
        self.__GPIO_SIG118_IN_SEL_msb = 7
        self.__GPIO_FUNC118_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC118_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC118_IN_SEL_lsb = 0
        self.__GPIO_FUNC118_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG118_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG118_IN_SEL_msb, self.__GPIO_SIG118_IN_SEL_lsb)
    @GPIO_SIG118_IN_SEL.setter
    def GPIO_SIG118_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG118_IN_SEL_msb, self.__GPIO_SIG118_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC118_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC118_IN_INV_SEL_msb, self.__GPIO_FUNC118_IN_INV_SEL_lsb)
    @GPIO_FUNC118_IN_INV_SEL.setter
    def GPIO_FUNC118_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC118_IN_INV_SEL_msb, self.__GPIO_FUNC118_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC118_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC118_IN_SEL_msb, self.__GPIO_FUNC118_IN_SEL_lsb)
    @GPIO_FUNC118_IN_SEL.setter
    def GPIO_FUNC118_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC118_IN_SEL_msb, self.__GPIO_FUNC118_IN_SEL_lsb, value)
class GPIO_FUNC119_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x30c
        self.__GPIO_SIG119_IN_SEL_lsb = 7
        self.__GPIO_SIG119_IN_SEL_msb = 7
        self.__GPIO_FUNC119_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC119_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC119_IN_SEL_lsb = 0
        self.__GPIO_FUNC119_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG119_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG119_IN_SEL_msb, self.__GPIO_SIG119_IN_SEL_lsb)
    @GPIO_SIG119_IN_SEL.setter
    def GPIO_SIG119_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG119_IN_SEL_msb, self.__GPIO_SIG119_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC119_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC119_IN_INV_SEL_msb, self.__GPIO_FUNC119_IN_INV_SEL_lsb)
    @GPIO_FUNC119_IN_INV_SEL.setter
    def GPIO_FUNC119_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC119_IN_INV_SEL_msb, self.__GPIO_FUNC119_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC119_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC119_IN_SEL_msb, self.__GPIO_FUNC119_IN_SEL_lsb)
    @GPIO_FUNC119_IN_SEL.setter
    def GPIO_FUNC119_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC119_IN_SEL_msb, self.__GPIO_FUNC119_IN_SEL_lsb, value)
class GPIO_FUNC120_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x310
        self.__GPIO_SIG120_IN_SEL_lsb = 7
        self.__GPIO_SIG120_IN_SEL_msb = 7
        self.__GPIO_FUNC120_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC120_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC120_IN_SEL_lsb = 0
        self.__GPIO_FUNC120_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG120_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG120_IN_SEL_msb, self.__GPIO_SIG120_IN_SEL_lsb)
    @GPIO_SIG120_IN_SEL.setter
    def GPIO_SIG120_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG120_IN_SEL_msb, self.__GPIO_SIG120_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC120_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC120_IN_INV_SEL_msb, self.__GPIO_FUNC120_IN_INV_SEL_lsb)
    @GPIO_FUNC120_IN_INV_SEL.setter
    def GPIO_FUNC120_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC120_IN_INV_SEL_msb, self.__GPIO_FUNC120_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC120_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC120_IN_SEL_msb, self.__GPIO_FUNC120_IN_SEL_lsb)
    @GPIO_FUNC120_IN_SEL.setter
    def GPIO_FUNC120_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC120_IN_SEL_msb, self.__GPIO_FUNC120_IN_SEL_lsb, value)
class GPIO_FUNC121_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x314
        self.__GPIO_SIG121_IN_SEL_lsb = 7
        self.__GPIO_SIG121_IN_SEL_msb = 7
        self.__GPIO_FUNC121_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC121_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC121_IN_SEL_lsb = 0
        self.__GPIO_FUNC121_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG121_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG121_IN_SEL_msb, self.__GPIO_SIG121_IN_SEL_lsb)
    @GPIO_SIG121_IN_SEL.setter
    def GPIO_SIG121_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG121_IN_SEL_msb, self.__GPIO_SIG121_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC121_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC121_IN_INV_SEL_msb, self.__GPIO_FUNC121_IN_INV_SEL_lsb)
    @GPIO_FUNC121_IN_INV_SEL.setter
    def GPIO_FUNC121_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC121_IN_INV_SEL_msb, self.__GPIO_FUNC121_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC121_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC121_IN_SEL_msb, self.__GPIO_FUNC121_IN_SEL_lsb)
    @GPIO_FUNC121_IN_SEL.setter
    def GPIO_FUNC121_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC121_IN_SEL_msb, self.__GPIO_FUNC121_IN_SEL_lsb, value)
class GPIO_FUNC122_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x318
        self.__GPIO_SIG122_IN_SEL_lsb = 7
        self.__GPIO_SIG122_IN_SEL_msb = 7
        self.__GPIO_FUNC122_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC122_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC122_IN_SEL_lsb = 0
        self.__GPIO_FUNC122_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG122_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG122_IN_SEL_msb, self.__GPIO_SIG122_IN_SEL_lsb)
    @GPIO_SIG122_IN_SEL.setter
    def GPIO_SIG122_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG122_IN_SEL_msb, self.__GPIO_SIG122_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC122_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC122_IN_INV_SEL_msb, self.__GPIO_FUNC122_IN_INV_SEL_lsb)
    @GPIO_FUNC122_IN_INV_SEL.setter
    def GPIO_FUNC122_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC122_IN_INV_SEL_msb, self.__GPIO_FUNC122_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC122_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC122_IN_SEL_msb, self.__GPIO_FUNC122_IN_SEL_lsb)
    @GPIO_FUNC122_IN_SEL.setter
    def GPIO_FUNC122_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC122_IN_SEL_msb, self.__GPIO_FUNC122_IN_SEL_lsb, value)
class GPIO_FUNC123_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x31c
        self.__GPIO_SIG123_IN_SEL_lsb = 7
        self.__GPIO_SIG123_IN_SEL_msb = 7
        self.__GPIO_FUNC123_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC123_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC123_IN_SEL_lsb = 0
        self.__GPIO_FUNC123_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG123_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG123_IN_SEL_msb, self.__GPIO_SIG123_IN_SEL_lsb)
    @GPIO_SIG123_IN_SEL.setter
    def GPIO_SIG123_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG123_IN_SEL_msb, self.__GPIO_SIG123_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC123_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC123_IN_INV_SEL_msb, self.__GPIO_FUNC123_IN_INV_SEL_lsb)
    @GPIO_FUNC123_IN_INV_SEL.setter
    def GPIO_FUNC123_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC123_IN_INV_SEL_msb, self.__GPIO_FUNC123_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC123_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC123_IN_SEL_msb, self.__GPIO_FUNC123_IN_SEL_lsb)
    @GPIO_FUNC123_IN_SEL.setter
    def GPIO_FUNC123_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC123_IN_SEL_msb, self.__GPIO_FUNC123_IN_SEL_lsb, value)
class GPIO_FUNC124_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x320
        self.__GPIO_SIG124_IN_SEL_lsb = 7
        self.__GPIO_SIG124_IN_SEL_msb = 7
        self.__GPIO_FUNC124_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC124_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC124_IN_SEL_lsb = 0
        self.__GPIO_FUNC124_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG124_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG124_IN_SEL_msb, self.__GPIO_SIG124_IN_SEL_lsb)
    @GPIO_SIG124_IN_SEL.setter
    def GPIO_SIG124_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG124_IN_SEL_msb, self.__GPIO_SIG124_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC124_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC124_IN_INV_SEL_msb, self.__GPIO_FUNC124_IN_INV_SEL_lsb)
    @GPIO_FUNC124_IN_INV_SEL.setter
    def GPIO_FUNC124_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC124_IN_INV_SEL_msb, self.__GPIO_FUNC124_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC124_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC124_IN_SEL_msb, self.__GPIO_FUNC124_IN_SEL_lsb)
    @GPIO_FUNC124_IN_SEL.setter
    def GPIO_FUNC124_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC124_IN_SEL_msb, self.__GPIO_FUNC124_IN_SEL_lsb, value)
class GPIO_FUNC125_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x324
        self.__GPIO_SIG125_IN_SEL_lsb = 7
        self.__GPIO_SIG125_IN_SEL_msb = 7
        self.__GPIO_FUNC125_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC125_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC125_IN_SEL_lsb = 0
        self.__GPIO_FUNC125_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG125_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG125_IN_SEL_msb, self.__GPIO_SIG125_IN_SEL_lsb)
    @GPIO_SIG125_IN_SEL.setter
    def GPIO_SIG125_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG125_IN_SEL_msb, self.__GPIO_SIG125_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC125_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC125_IN_INV_SEL_msb, self.__GPIO_FUNC125_IN_INV_SEL_lsb)
    @GPIO_FUNC125_IN_INV_SEL.setter
    def GPIO_FUNC125_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC125_IN_INV_SEL_msb, self.__GPIO_FUNC125_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC125_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC125_IN_SEL_msb, self.__GPIO_FUNC125_IN_SEL_lsb)
    @GPIO_FUNC125_IN_SEL.setter
    def GPIO_FUNC125_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC125_IN_SEL_msb, self.__GPIO_FUNC125_IN_SEL_lsb, value)
class GPIO_FUNC126_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x328
        self.__GPIO_SIG126_IN_SEL_lsb = 7
        self.__GPIO_SIG126_IN_SEL_msb = 7
        self.__GPIO_FUNC126_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC126_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC126_IN_SEL_lsb = 0
        self.__GPIO_FUNC126_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG126_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG126_IN_SEL_msb, self.__GPIO_SIG126_IN_SEL_lsb)
    @GPIO_SIG126_IN_SEL.setter
    def GPIO_SIG126_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG126_IN_SEL_msb, self.__GPIO_SIG126_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC126_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC126_IN_INV_SEL_msb, self.__GPIO_FUNC126_IN_INV_SEL_lsb)
    @GPIO_FUNC126_IN_INV_SEL.setter
    def GPIO_FUNC126_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC126_IN_INV_SEL_msb, self.__GPIO_FUNC126_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC126_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC126_IN_SEL_msb, self.__GPIO_FUNC126_IN_SEL_lsb)
    @GPIO_FUNC126_IN_SEL.setter
    def GPIO_FUNC126_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC126_IN_SEL_msb, self.__GPIO_FUNC126_IN_SEL_lsb, value)
class GPIO_FUNC127_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x32c
        self.__GPIO_SIG127_IN_SEL_lsb = 7
        self.__GPIO_SIG127_IN_SEL_msb = 7
        self.__GPIO_FUNC127_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC127_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC127_IN_SEL_lsb = 0
        self.__GPIO_FUNC127_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG127_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG127_IN_SEL_msb, self.__GPIO_SIG127_IN_SEL_lsb)
    @GPIO_SIG127_IN_SEL.setter
    def GPIO_SIG127_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG127_IN_SEL_msb, self.__GPIO_SIG127_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC127_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC127_IN_INV_SEL_msb, self.__GPIO_FUNC127_IN_INV_SEL_lsb)
    @GPIO_FUNC127_IN_INV_SEL.setter
    def GPIO_FUNC127_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC127_IN_INV_SEL_msb, self.__GPIO_FUNC127_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC127_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC127_IN_SEL_msb, self.__GPIO_FUNC127_IN_SEL_lsb)
    @GPIO_FUNC127_IN_SEL.setter
    def GPIO_FUNC127_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC127_IN_SEL_msb, self.__GPIO_FUNC127_IN_SEL_lsb, value)
class GPIO_FUNC128_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x330
        self.__GPIO_SIG128_IN_SEL_lsb = 7
        self.__GPIO_SIG128_IN_SEL_msb = 7
        self.__GPIO_FUNC128_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC128_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC128_IN_SEL_lsb = 0
        self.__GPIO_FUNC128_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG128_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG128_IN_SEL_msb, self.__GPIO_SIG128_IN_SEL_lsb)
    @GPIO_SIG128_IN_SEL.setter
    def GPIO_SIG128_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG128_IN_SEL_msb, self.__GPIO_SIG128_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC128_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC128_IN_INV_SEL_msb, self.__GPIO_FUNC128_IN_INV_SEL_lsb)
    @GPIO_FUNC128_IN_INV_SEL.setter
    def GPIO_FUNC128_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC128_IN_INV_SEL_msb, self.__GPIO_FUNC128_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC128_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC128_IN_SEL_msb, self.__GPIO_FUNC128_IN_SEL_lsb)
    @GPIO_FUNC128_IN_SEL.setter
    def GPIO_FUNC128_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC128_IN_SEL_msb, self.__GPIO_FUNC128_IN_SEL_lsb, value)
class GPIO_FUNC129_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x334
        self.__GPIO_SIG129_IN_SEL_lsb = 7
        self.__GPIO_SIG129_IN_SEL_msb = 7
        self.__GPIO_FUNC129_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC129_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC129_IN_SEL_lsb = 0
        self.__GPIO_FUNC129_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG129_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG129_IN_SEL_msb, self.__GPIO_SIG129_IN_SEL_lsb)
    @GPIO_SIG129_IN_SEL.setter
    def GPIO_SIG129_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG129_IN_SEL_msb, self.__GPIO_SIG129_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC129_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC129_IN_INV_SEL_msb, self.__GPIO_FUNC129_IN_INV_SEL_lsb)
    @GPIO_FUNC129_IN_INV_SEL.setter
    def GPIO_FUNC129_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC129_IN_INV_SEL_msb, self.__GPIO_FUNC129_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC129_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC129_IN_SEL_msb, self.__GPIO_FUNC129_IN_SEL_lsb)
    @GPIO_FUNC129_IN_SEL.setter
    def GPIO_FUNC129_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC129_IN_SEL_msb, self.__GPIO_FUNC129_IN_SEL_lsb, value)
class GPIO_FUNC130_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x338
        self.__GPIO_SIG130_IN_SEL_lsb = 7
        self.__GPIO_SIG130_IN_SEL_msb = 7
        self.__GPIO_FUNC130_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC130_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC130_IN_SEL_lsb = 0
        self.__GPIO_FUNC130_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG130_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG130_IN_SEL_msb, self.__GPIO_SIG130_IN_SEL_lsb)
    @GPIO_SIG130_IN_SEL.setter
    def GPIO_SIG130_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG130_IN_SEL_msb, self.__GPIO_SIG130_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC130_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC130_IN_INV_SEL_msb, self.__GPIO_FUNC130_IN_INV_SEL_lsb)
    @GPIO_FUNC130_IN_INV_SEL.setter
    def GPIO_FUNC130_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC130_IN_INV_SEL_msb, self.__GPIO_FUNC130_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC130_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC130_IN_SEL_msb, self.__GPIO_FUNC130_IN_SEL_lsb)
    @GPIO_FUNC130_IN_SEL.setter
    def GPIO_FUNC130_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC130_IN_SEL_msb, self.__GPIO_FUNC130_IN_SEL_lsb, value)
class GPIO_FUNC131_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x33c
        self.__GPIO_SIG131_IN_SEL_lsb = 7
        self.__GPIO_SIG131_IN_SEL_msb = 7
        self.__GPIO_FUNC131_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC131_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC131_IN_SEL_lsb = 0
        self.__GPIO_FUNC131_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG131_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG131_IN_SEL_msb, self.__GPIO_SIG131_IN_SEL_lsb)
    @GPIO_SIG131_IN_SEL.setter
    def GPIO_SIG131_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG131_IN_SEL_msb, self.__GPIO_SIG131_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC131_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC131_IN_INV_SEL_msb, self.__GPIO_FUNC131_IN_INV_SEL_lsb)
    @GPIO_FUNC131_IN_INV_SEL.setter
    def GPIO_FUNC131_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC131_IN_INV_SEL_msb, self.__GPIO_FUNC131_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC131_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC131_IN_SEL_msb, self.__GPIO_FUNC131_IN_SEL_lsb)
    @GPIO_FUNC131_IN_SEL.setter
    def GPIO_FUNC131_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC131_IN_SEL_msb, self.__GPIO_FUNC131_IN_SEL_lsb, value)
class GPIO_FUNC132_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x340
        self.__GPIO_SIG132_IN_SEL_lsb = 7
        self.__GPIO_SIG132_IN_SEL_msb = 7
        self.__GPIO_FUNC132_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC132_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC132_IN_SEL_lsb = 0
        self.__GPIO_FUNC132_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG132_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG132_IN_SEL_msb, self.__GPIO_SIG132_IN_SEL_lsb)
    @GPIO_SIG132_IN_SEL.setter
    def GPIO_SIG132_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG132_IN_SEL_msb, self.__GPIO_SIG132_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC132_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC132_IN_INV_SEL_msb, self.__GPIO_FUNC132_IN_INV_SEL_lsb)
    @GPIO_FUNC132_IN_INV_SEL.setter
    def GPIO_FUNC132_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC132_IN_INV_SEL_msb, self.__GPIO_FUNC132_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC132_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC132_IN_SEL_msb, self.__GPIO_FUNC132_IN_SEL_lsb)
    @GPIO_FUNC132_IN_SEL.setter
    def GPIO_FUNC132_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC132_IN_SEL_msb, self.__GPIO_FUNC132_IN_SEL_lsb, value)
class GPIO_FUNC133_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x344
        self.__GPIO_SIG133_IN_SEL_lsb = 7
        self.__GPIO_SIG133_IN_SEL_msb = 7
        self.__GPIO_FUNC133_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC133_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC133_IN_SEL_lsb = 0
        self.__GPIO_FUNC133_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG133_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG133_IN_SEL_msb, self.__GPIO_SIG133_IN_SEL_lsb)
    @GPIO_SIG133_IN_SEL.setter
    def GPIO_SIG133_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG133_IN_SEL_msb, self.__GPIO_SIG133_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC133_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC133_IN_INV_SEL_msb, self.__GPIO_FUNC133_IN_INV_SEL_lsb)
    @GPIO_FUNC133_IN_INV_SEL.setter
    def GPIO_FUNC133_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC133_IN_INV_SEL_msb, self.__GPIO_FUNC133_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC133_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC133_IN_SEL_msb, self.__GPIO_FUNC133_IN_SEL_lsb)
    @GPIO_FUNC133_IN_SEL.setter
    def GPIO_FUNC133_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC133_IN_SEL_msb, self.__GPIO_FUNC133_IN_SEL_lsb, value)
class GPIO_FUNC134_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x348
        self.__GPIO_SIG134_IN_SEL_lsb = 7
        self.__GPIO_SIG134_IN_SEL_msb = 7
        self.__GPIO_FUNC134_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC134_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC134_IN_SEL_lsb = 0
        self.__GPIO_FUNC134_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG134_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG134_IN_SEL_msb, self.__GPIO_SIG134_IN_SEL_lsb)
    @GPIO_SIG134_IN_SEL.setter
    def GPIO_SIG134_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG134_IN_SEL_msb, self.__GPIO_SIG134_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC134_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC134_IN_INV_SEL_msb, self.__GPIO_FUNC134_IN_INV_SEL_lsb)
    @GPIO_FUNC134_IN_INV_SEL.setter
    def GPIO_FUNC134_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC134_IN_INV_SEL_msb, self.__GPIO_FUNC134_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC134_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC134_IN_SEL_msb, self.__GPIO_FUNC134_IN_SEL_lsb)
    @GPIO_FUNC134_IN_SEL.setter
    def GPIO_FUNC134_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC134_IN_SEL_msb, self.__GPIO_FUNC134_IN_SEL_lsb, value)
class GPIO_FUNC135_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x34c
        self.__GPIO_SIG135_IN_SEL_lsb = 7
        self.__GPIO_SIG135_IN_SEL_msb = 7
        self.__GPIO_FUNC135_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC135_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC135_IN_SEL_lsb = 0
        self.__GPIO_FUNC135_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG135_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG135_IN_SEL_msb, self.__GPIO_SIG135_IN_SEL_lsb)
    @GPIO_SIG135_IN_SEL.setter
    def GPIO_SIG135_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG135_IN_SEL_msb, self.__GPIO_SIG135_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC135_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC135_IN_INV_SEL_msb, self.__GPIO_FUNC135_IN_INV_SEL_lsb)
    @GPIO_FUNC135_IN_INV_SEL.setter
    def GPIO_FUNC135_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC135_IN_INV_SEL_msb, self.__GPIO_FUNC135_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC135_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC135_IN_SEL_msb, self.__GPIO_FUNC135_IN_SEL_lsb)
    @GPIO_FUNC135_IN_SEL.setter
    def GPIO_FUNC135_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC135_IN_SEL_msb, self.__GPIO_FUNC135_IN_SEL_lsb, value)
class GPIO_FUNC136_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x350
        self.__GPIO_SIG136_IN_SEL_lsb = 7
        self.__GPIO_SIG136_IN_SEL_msb = 7
        self.__GPIO_FUNC136_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC136_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC136_IN_SEL_lsb = 0
        self.__GPIO_FUNC136_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG136_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG136_IN_SEL_msb, self.__GPIO_SIG136_IN_SEL_lsb)
    @GPIO_SIG136_IN_SEL.setter
    def GPIO_SIG136_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG136_IN_SEL_msb, self.__GPIO_SIG136_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC136_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC136_IN_INV_SEL_msb, self.__GPIO_FUNC136_IN_INV_SEL_lsb)
    @GPIO_FUNC136_IN_INV_SEL.setter
    def GPIO_FUNC136_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC136_IN_INV_SEL_msb, self.__GPIO_FUNC136_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC136_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC136_IN_SEL_msb, self.__GPIO_FUNC136_IN_SEL_lsb)
    @GPIO_FUNC136_IN_SEL.setter
    def GPIO_FUNC136_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC136_IN_SEL_msb, self.__GPIO_FUNC136_IN_SEL_lsb, value)
class GPIO_FUNC137_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x354
        self.__GPIO_SIG137_IN_SEL_lsb = 7
        self.__GPIO_SIG137_IN_SEL_msb = 7
        self.__GPIO_FUNC137_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC137_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC137_IN_SEL_lsb = 0
        self.__GPIO_FUNC137_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG137_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG137_IN_SEL_msb, self.__GPIO_SIG137_IN_SEL_lsb)
    @GPIO_SIG137_IN_SEL.setter
    def GPIO_SIG137_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG137_IN_SEL_msb, self.__GPIO_SIG137_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC137_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC137_IN_INV_SEL_msb, self.__GPIO_FUNC137_IN_INV_SEL_lsb)
    @GPIO_FUNC137_IN_INV_SEL.setter
    def GPIO_FUNC137_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC137_IN_INV_SEL_msb, self.__GPIO_FUNC137_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC137_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC137_IN_SEL_msb, self.__GPIO_FUNC137_IN_SEL_lsb)
    @GPIO_FUNC137_IN_SEL.setter
    def GPIO_FUNC137_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC137_IN_SEL_msb, self.__GPIO_FUNC137_IN_SEL_lsb, value)
class GPIO_FUNC138_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x358
        self.__GPIO_SIG138_IN_SEL_lsb = 7
        self.__GPIO_SIG138_IN_SEL_msb = 7
        self.__GPIO_FUNC138_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC138_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC138_IN_SEL_lsb = 0
        self.__GPIO_FUNC138_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG138_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG138_IN_SEL_msb, self.__GPIO_SIG138_IN_SEL_lsb)
    @GPIO_SIG138_IN_SEL.setter
    def GPIO_SIG138_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG138_IN_SEL_msb, self.__GPIO_SIG138_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC138_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC138_IN_INV_SEL_msb, self.__GPIO_FUNC138_IN_INV_SEL_lsb)
    @GPIO_FUNC138_IN_INV_SEL.setter
    def GPIO_FUNC138_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC138_IN_INV_SEL_msb, self.__GPIO_FUNC138_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC138_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC138_IN_SEL_msb, self.__GPIO_FUNC138_IN_SEL_lsb)
    @GPIO_FUNC138_IN_SEL.setter
    def GPIO_FUNC138_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC138_IN_SEL_msb, self.__GPIO_FUNC138_IN_SEL_lsb, value)
class GPIO_FUNC139_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x35c
        self.__GPIO_SIG139_IN_SEL_lsb = 7
        self.__GPIO_SIG139_IN_SEL_msb = 7
        self.__GPIO_FUNC139_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC139_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC139_IN_SEL_lsb = 0
        self.__GPIO_FUNC139_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG139_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG139_IN_SEL_msb, self.__GPIO_SIG139_IN_SEL_lsb)
    @GPIO_SIG139_IN_SEL.setter
    def GPIO_SIG139_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG139_IN_SEL_msb, self.__GPIO_SIG139_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC139_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC139_IN_INV_SEL_msb, self.__GPIO_FUNC139_IN_INV_SEL_lsb)
    @GPIO_FUNC139_IN_INV_SEL.setter
    def GPIO_FUNC139_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC139_IN_INV_SEL_msb, self.__GPIO_FUNC139_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC139_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC139_IN_SEL_msb, self.__GPIO_FUNC139_IN_SEL_lsb)
    @GPIO_FUNC139_IN_SEL.setter
    def GPIO_FUNC139_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC139_IN_SEL_msb, self.__GPIO_FUNC139_IN_SEL_lsb, value)
class GPIO_FUNC140_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x360
        self.__GPIO_SIG140_IN_SEL_lsb = 7
        self.__GPIO_SIG140_IN_SEL_msb = 7
        self.__GPIO_FUNC140_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC140_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC140_IN_SEL_lsb = 0
        self.__GPIO_FUNC140_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG140_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG140_IN_SEL_msb, self.__GPIO_SIG140_IN_SEL_lsb)
    @GPIO_SIG140_IN_SEL.setter
    def GPIO_SIG140_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG140_IN_SEL_msb, self.__GPIO_SIG140_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC140_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC140_IN_INV_SEL_msb, self.__GPIO_FUNC140_IN_INV_SEL_lsb)
    @GPIO_FUNC140_IN_INV_SEL.setter
    def GPIO_FUNC140_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC140_IN_INV_SEL_msb, self.__GPIO_FUNC140_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC140_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC140_IN_SEL_msb, self.__GPIO_FUNC140_IN_SEL_lsb)
    @GPIO_FUNC140_IN_SEL.setter
    def GPIO_FUNC140_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC140_IN_SEL_msb, self.__GPIO_FUNC140_IN_SEL_lsb, value)
class GPIO_FUNC141_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x364
        self.__GPIO_SIG141_IN_SEL_lsb = 7
        self.__GPIO_SIG141_IN_SEL_msb = 7
        self.__GPIO_FUNC141_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC141_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC141_IN_SEL_lsb = 0
        self.__GPIO_FUNC141_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG141_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG141_IN_SEL_msb, self.__GPIO_SIG141_IN_SEL_lsb)
    @GPIO_SIG141_IN_SEL.setter
    def GPIO_SIG141_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG141_IN_SEL_msb, self.__GPIO_SIG141_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC141_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC141_IN_INV_SEL_msb, self.__GPIO_FUNC141_IN_INV_SEL_lsb)
    @GPIO_FUNC141_IN_INV_SEL.setter
    def GPIO_FUNC141_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC141_IN_INV_SEL_msb, self.__GPIO_FUNC141_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC141_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC141_IN_SEL_msb, self.__GPIO_FUNC141_IN_SEL_lsb)
    @GPIO_FUNC141_IN_SEL.setter
    def GPIO_FUNC141_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC141_IN_SEL_msb, self.__GPIO_FUNC141_IN_SEL_lsb, value)
class GPIO_FUNC142_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x368
        self.__GPIO_SIG142_IN_SEL_lsb = 7
        self.__GPIO_SIG142_IN_SEL_msb = 7
        self.__GPIO_FUNC142_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC142_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC142_IN_SEL_lsb = 0
        self.__GPIO_FUNC142_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG142_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG142_IN_SEL_msb, self.__GPIO_SIG142_IN_SEL_lsb)
    @GPIO_SIG142_IN_SEL.setter
    def GPIO_SIG142_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG142_IN_SEL_msb, self.__GPIO_SIG142_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC142_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC142_IN_INV_SEL_msb, self.__GPIO_FUNC142_IN_INV_SEL_lsb)
    @GPIO_FUNC142_IN_INV_SEL.setter
    def GPIO_FUNC142_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC142_IN_INV_SEL_msb, self.__GPIO_FUNC142_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC142_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC142_IN_SEL_msb, self.__GPIO_FUNC142_IN_SEL_lsb)
    @GPIO_FUNC142_IN_SEL.setter
    def GPIO_FUNC142_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC142_IN_SEL_msb, self.__GPIO_FUNC142_IN_SEL_lsb, value)
class GPIO_FUNC143_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x36c
        self.__GPIO_SIG143_IN_SEL_lsb = 7
        self.__GPIO_SIG143_IN_SEL_msb = 7
        self.__GPIO_FUNC143_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC143_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC143_IN_SEL_lsb = 0
        self.__GPIO_FUNC143_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG143_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG143_IN_SEL_msb, self.__GPIO_SIG143_IN_SEL_lsb)
    @GPIO_SIG143_IN_SEL.setter
    def GPIO_SIG143_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG143_IN_SEL_msb, self.__GPIO_SIG143_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC143_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC143_IN_INV_SEL_msb, self.__GPIO_FUNC143_IN_INV_SEL_lsb)
    @GPIO_FUNC143_IN_INV_SEL.setter
    def GPIO_FUNC143_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC143_IN_INV_SEL_msb, self.__GPIO_FUNC143_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC143_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC143_IN_SEL_msb, self.__GPIO_FUNC143_IN_SEL_lsb)
    @GPIO_FUNC143_IN_SEL.setter
    def GPIO_FUNC143_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC143_IN_SEL_msb, self.__GPIO_FUNC143_IN_SEL_lsb, value)
class GPIO_FUNC144_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x370
        self.__GPIO_SIG144_IN_SEL_lsb = 7
        self.__GPIO_SIG144_IN_SEL_msb = 7
        self.__GPIO_FUNC144_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC144_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC144_IN_SEL_lsb = 0
        self.__GPIO_FUNC144_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG144_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG144_IN_SEL_msb, self.__GPIO_SIG144_IN_SEL_lsb)
    @GPIO_SIG144_IN_SEL.setter
    def GPIO_SIG144_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG144_IN_SEL_msb, self.__GPIO_SIG144_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC144_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC144_IN_INV_SEL_msb, self.__GPIO_FUNC144_IN_INV_SEL_lsb)
    @GPIO_FUNC144_IN_INV_SEL.setter
    def GPIO_FUNC144_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC144_IN_INV_SEL_msb, self.__GPIO_FUNC144_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC144_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC144_IN_SEL_msb, self.__GPIO_FUNC144_IN_SEL_lsb)
    @GPIO_FUNC144_IN_SEL.setter
    def GPIO_FUNC144_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC144_IN_SEL_msb, self.__GPIO_FUNC144_IN_SEL_lsb, value)
class GPIO_FUNC145_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x374
        self.__GPIO_SIG145_IN_SEL_lsb = 7
        self.__GPIO_SIG145_IN_SEL_msb = 7
        self.__GPIO_FUNC145_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC145_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC145_IN_SEL_lsb = 0
        self.__GPIO_FUNC145_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG145_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG145_IN_SEL_msb, self.__GPIO_SIG145_IN_SEL_lsb)
    @GPIO_SIG145_IN_SEL.setter
    def GPIO_SIG145_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG145_IN_SEL_msb, self.__GPIO_SIG145_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC145_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC145_IN_INV_SEL_msb, self.__GPIO_FUNC145_IN_INV_SEL_lsb)
    @GPIO_FUNC145_IN_INV_SEL.setter
    def GPIO_FUNC145_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC145_IN_INV_SEL_msb, self.__GPIO_FUNC145_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC145_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC145_IN_SEL_msb, self.__GPIO_FUNC145_IN_SEL_lsb)
    @GPIO_FUNC145_IN_SEL.setter
    def GPIO_FUNC145_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC145_IN_SEL_msb, self.__GPIO_FUNC145_IN_SEL_lsb, value)
class GPIO_FUNC146_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x378
        self.__GPIO_SIG146_IN_SEL_lsb = 7
        self.__GPIO_SIG146_IN_SEL_msb = 7
        self.__GPIO_FUNC146_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC146_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC146_IN_SEL_lsb = 0
        self.__GPIO_FUNC146_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG146_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG146_IN_SEL_msb, self.__GPIO_SIG146_IN_SEL_lsb)
    @GPIO_SIG146_IN_SEL.setter
    def GPIO_SIG146_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG146_IN_SEL_msb, self.__GPIO_SIG146_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC146_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC146_IN_INV_SEL_msb, self.__GPIO_FUNC146_IN_INV_SEL_lsb)
    @GPIO_FUNC146_IN_INV_SEL.setter
    def GPIO_FUNC146_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC146_IN_INV_SEL_msb, self.__GPIO_FUNC146_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC146_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC146_IN_SEL_msb, self.__GPIO_FUNC146_IN_SEL_lsb)
    @GPIO_FUNC146_IN_SEL.setter
    def GPIO_FUNC146_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC146_IN_SEL_msb, self.__GPIO_FUNC146_IN_SEL_lsb, value)
class GPIO_FUNC147_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x37c
        self.__GPIO_SIG147_IN_SEL_lsb = 7
        self.__GPIO_SIG147_IN_SEL_msb = 7
        self.__GPIO_FUNC147_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC147_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC147_IN_SEL_lsb = 0
        self.__GPIO_FUNC147_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG147_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG147_IN_SEL_msb, self.__GPIO_SIG147_IN_SEL_lsb)
    @GPIO_SIG147_IN_SEL.setter
    def GPIO_SIG147_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG147_IN_SEL_msb, self.__GPIO_SIG147_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC147_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC147_IN_INV_SEL_msb, self.__GPIO_FUNC147_IN_INV_SEL_lsb)
    @GPIO_FUNC147_IN_INV_SEL.setter
    def GPIO_FUNC147_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC147_IN_INV_SEL_msb, self.__GPIO_FUNC147_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC147_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC147_IN_SEL_msb, self.__GPIO_FUNC147_IN_SEL_lsb)
    @GPIO_FUNC147_IN_SEL.setter
    def GPIO_FUNC147_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC147_IN_SEL_msb, self.__GPIO_FUNC147_IN_SEL_lsb, value)
class GPIO_FUNC148_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x380
        self.__GPIO_SIG148_IN_SEL_lsb = 7
        self.__GPIO_SIG148_IN_SEL_msb = 7
        self.__GPIO_FUNC148_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC148_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC148_IN_SEL_lsb = 0
        self.__GPIO_FUNC148_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG148_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG148_IN_SEL_msb, self.__GPIO_SIG148_IN_SEL_lsb)
    @GPIO_SIG148_IN_SEL.setter
    def GPIO_SIG148_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG148_IN_SEL_msb, self.__GPIO_SIG148_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC148_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC148_IN_INV_SEL_msb, self.__GPIO_FUNC148_IN_INV_SEL_lsb)
    @GPIO_FUNC148_IN_INV_SEL.setter
    def GPIO_FUNC148_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC148_IN_INV_SEL_msb, self.__GPIO_FUNC148_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC148_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC148_IN_SEL_msb, self.__GPIO_FUNC148_IN_SEL_lsb)
    @GPIO_FUNC148_IN_SEL.setter
    def GPIO_FUNC148_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC148_IN_SEL_msb, self.__GPIO_FUNC148_IN_SEL_lsb, value)
class GPIO_FUNC149_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x384
        self.__GPIO_SIG149_IN_SEL_lsb = 7
        self.__GPIO_SIG149_IN_SEL_msb = 7
        self.__GPIO_FUNC149_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC149_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC149_IN_SEL_lsb = 0
        self.__GPIO_FUNC149_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG149_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG149_IN_SEL_msb, self.__GPIO_SIG149_IN_SEL_lsb)
    @GPIO_SIG149_IN_SEL.setter
    def GPIO_SIG149_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG149_IN_SEL_msb, self.__GPIO_SIG149_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC149_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC149_IN_INV_SEL_msb, self.__GPIO_FUNC149_IN_INV_SEL_lsb)
    @GPIO_FUNC149_IN_INV_SEL.setter
    def GPIO_FUNC149_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC149_IN_INV_SEL_msb, self.__GPIO_FUNC149_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC149_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC149_IN_SEL_msb, self.__GPIO_FUNC149_IN_SEL_lsb)
    @GPIO_FUNC149_IN_SEL.setter
    def GPIO_FUNC149_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC149_IN_SEL_msb, self.__GPIO_FUNC149_IN_SEL_lsb, value)
class GPIO_FUNC150_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x388
        self.__GPIO_SIG150_IN_SEL_lsb = 7
        self.__GPIO_SIG150_IN_SEL_msb = 7
        self.__GPIO_FUNC150_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC150_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC150_IN_SEL_lsb = 0
        self.__GPIO_FUNC150_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG150_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG150_IN_SEL_msb, self.__GPIO_SIG150_IN_SEL_lsb)
    @GPIO_SIG150_IN_SEL.setter
    def GPIO_SIG150_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG150_IN_SEL_msb, self.__GPIO_SIG150_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC150_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC150_IN_INV_SEL_msb, self.__GPIO_FUNC150_IN_INV_SEL_lsb)
    @GPIO_FUNC150_IN_INV_SEL.setter
    def GPIO_FUNC150_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC150_IN_INV_SEL_msb, self.__GPIO_FUNC150_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC150_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC150_IN_SEL_msb, self.__GPIO_FUNC150_IN_SEL_lsb)
    @GPIO_FUNC150_IN_SEL.setter
    def GPIO_FUNC150_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC150_IN_SEL_msb, self.__GPIO_FUNC150_IN_SEL_lsb, value)
class GPIO_FUNC151_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x38c
        self.__GPIO_SIG151_IN_SEL_lsb = 7
        self.__GPIO_SIG151_IN_SEL_msb = 7
        self.__GPIO_FUNC151_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC151_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC151_IN_SEL_lsb = 0
        self.__GPIO_FUNC151_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG151_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG151_IN_SEL_msb, self.__GPIO_SIG151_IN_SEL_lsb)
    @GPIO_SIG151_IN_SEL.setter
    def GPIO_SIG151_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG151_IN_SEL_msb, self.__GPIO_SIG151_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC151_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC151_IN_INV_SEL_msb, self.__GPIO_FUNC151_IN_INV_SEL_lsb)
    @GPIO_FUNC151_IN_INV_SEL.setter
    def GPIO_FUNC151_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC151_IN_INV_SEL_msb, self.__GPIO_FUNC151_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC151_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC151_IN_SEL_msb, self.__GPIO_FUNC151_IN_SEL_lsb)
    @GPIO_FUNC151_IN_SEL.setter
    def GPIO_FUNC151_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC151_IN_SEL_msb, self.__GPIO_FUNC151_IN_SEL_lsb, value)
class GPIO_FUNC152_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x390
        self.__GPIO_SIG152_IN_SEL_lsb = 7
        self.__GPIO_SIG152_IN_SEL_msb = 7
        self.__GPIO_FUNC152_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC152_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC152_IN_SEL_lsb = 0
        self.__GPIO_FUNC152_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG152_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG152_IN_SEL_msb, self.__GPIO_SIG152_IN_SEL_lsb)
    @GPIO_SIG152_IN_SEL.setter
    def GPIO_SIG152_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG152_IN_SEL_msb, self.__GPIO_SIG152_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC152_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC152_IN_INV_SEL_msb, self.__GPIO_FUNC152_IN_INV_SEL_lsb)
    @GPIO_FUNC152_IN_INV_SEL.setter
    def GPIO_FUNC152_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC152_IN_INV_SEL_msb, self.__GPIO_FUNC152_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC152_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC152_IN_SEL_msb, self.__GPIO_FUNC152_IN_SEL_lsb)
    @GPIO_FUNC152_IN_SEL.setter
    def GPIO_FUNC152_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC152_IN_SEL_msb, self.__GPIO_FUNC152_IN_SEL_lsb, value)
class GPIO_FUNC153_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x394
        self.__GPIO_SIG153_IN_SEL_lsb = 7
        self.__GPIO_SIG153_IN_SEL_msb = 7
        self.__GPIO_FUNC153_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC153_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC153_IN_SEL_lsb = 0
        self.__GPIO_FUNC153_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG153_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG153_IN_SEL_msb, self.__GPIO_SIG153_IN_SEL_lsb)
    @GPIO_SIG153_IN_SEL.setter
    def GPIO_SIG153_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG153_IN_SEL_msb, self.__GPIO_SIG153_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC153_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC153_IN_INV_SEL_msb, self.__GPIO_FUNC153_IN_INV_SEL_lsb)
    @GPIO_FUNC153_IN_INV_SEL.setter
    def GPIO_FUNC153_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC153_IN_INV_SEL_msb, self.__GPIO_FUNC153_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC153_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC153_IN_SEL_msb, self.__GPIO_FUNC153_IN_SEL_lsb)
    @GPIO_FUNC153_IN_SEL.setter
    def GPIO_FUNC153_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC153_IN_SEL_msb, self.__GPIO_FUNC153_IN_SEL_lsb, value)
class GPIO_FUNC154_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x398
        self.__GPIO_SIG154_IN_SEL_lsb = 7
        self.__GPIO_SIG154_IN_SEL_msb = 7
        self.__GPIO_FUNC154_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC154_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC154_IN_SEL_lsb = 0
        self.__GPIO_FUNC154_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG154_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG154_IN_SEL_msb, self.__GPIO_SIG154_IN_SEL_lsb)
    @GPIO_SIG154_IN_SEL.setter
    def GPIO_SIG154_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG154_IN_SEL_msb, self.__GPIO_SIG154_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC154_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC154_IN_INV_SEL_msb, self.__GPIO_FUNC154_IN_INV_SEL_lsb)
    @GPIO_FUNC154_IN_INV_SEL.setter
    def GPIO_FUNC154_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC154_IN_INV_SEL_msb, self.__GPIO_FUNC154_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC154_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC154_IN_SEL_msb, self.__GPIO_FUNC154_IN_SEL_lsb)
    @GPIO_FUNC154_IN_SEL.setter
    def GPIO_FUNC154_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC154_IN_SEL_msb, self.__GPIO_FUNC154_IN_SEL_lsb, value)
class GPIO_FUNC155_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x39c
        self.__GPIO_SIG155_IN_SEL_lsb = 7
        self.__GPIO_SIG155_IN_SEL_msb = 7
        self.__GPIO_FUNC155_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC155_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC155_IN_SEL_lsb = 0
        self.__GPIO_FUNC155_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG155_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG155_IN_SEL_msb, self.__GPIO_SIG155_IN_SEL_lsb)
    @GPIO_SIG155_IN_SEL.setter
    def GPIO_SIG155_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG155_IN_SEL_msb, self.__GPIO_SIG155_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC155_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC155_IN_INV_SEL_msb, self.__GPIO_FUNC155_IN_INV_SEL_lsb)
    @GPIO_FUNC155_IN_INV_SEL.setter
    def GPIO_FUNC155_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC155_IN_INV_SEL_msb, self.__GPIO_FUNC155_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC155_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC155_IN_SEL_msb, self.__GPIO_FUNC155_IN_SEL_lsb)
    @GPIO_FUNC155_IN_SEL.setter
    def GPIO_FUNC155_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC155_IN_SEL_msb, self.__GPIO_FUNC155_IN_SEL_lsb, value)
class GPIO_FUNC156_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x3a0
        self.__GPIO_SIG156_IN_SEL_lsb = 7
        self.__GPIO_SIG156_IN_SEL_msb = 7
        self.__GPIO_FUNC156_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC156_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC156_IN_SEL_lsb = 0
        self.__GPIO_FUNC156_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG156_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG156_IN_SEL_msb, self.__GPIO_SIG156_IN_SEL_lsb)
    @GPIO_SIG156_IN_SEL.setter
    def GPIO_SIG156_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG156_IN_SEL_msb, self.__GPIO_SIG156_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC156_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC156_IN_INV_SEL_msb, self.__GPIO_FUNC156_IN_INV_SEL_lsb)
    @GPIO_FUNC156_IN_INV_SEL.setter
    def GPIO_FUNC156_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC156_IN_INV_SEL_msb, self.__GPIO_FUNC156_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC156_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC156_IN_SEL_msb, self.__GPIO_FUNC156_IN_SEL_lsb)
    @GPIO_FUNC156_IN_SEL.setter
    def GPIO_FUNC156_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC156_IN_SEL_msb, self.__GPIO_FUNC156_IN_SEL_lsb, value)
class GPIO_FUNC157_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x3a4
        self.__GPIO_SIG157_IN_SEL_lsb = 7
        self.__GPIO_SIG157_IN_SEL_msb = 7
        self.__GPIO_FUNC157_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC157_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC157_IN_SEL_lsb = 0
        self.__GPIO_FUNC157_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG157_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG157_IN_SEL_msb, self.__GPIO_SIG157_IN_SEL_lsb)
    @GPIO_SIG157_IN_SEL.setter
    def GPIO_SIG157_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG157_IN_SEL_msb, self.__GPIO_SIG157_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC157_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC157_IN_INV_SEL_msb, self.__GPIO_FUNC157_IN_INV_SEL_lsb)
    @GPIO_FUNC157_IN_INV_SEL.setter
    def GPIO_FUNC157_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC157_IN_INV_SEL_msb, self.__GPIO_FUNC157_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC157_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC157_IN_SEL_msb, self.__GPIO_FUNC157_IN_SEL_lsb)
    @GPIO_FUNC157_IN_SEL.setter
    def GPIO_FUNC157_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC157_IN_SEL_msb, self.__GPIO_FUNC157_IN_SEL_lsb, value)
class GPIO_FUNC158_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x3a8
        self.__GPIO_SIG158_IN_SEL_lsb = 7
        self.__GPIO_SIG158_IN_SEL_msb = 7
        self.__GPIO_FUNC158_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC158_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC158_IN_SEL_lsb = 0
        self.__GPIO_FUNC158_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG158_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG158_IN_SEL_msb, self.__GPIO_SIG158_IN_SEL_lsb)
    @GPIO_SIG158_IN_SEL.setter
    def GPIO_SIG158_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG158_IN_SEL_msb, self.__GPIO_SIG158_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC158_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC158_IN_INV_SEL_msb, self.__GPIO_FUNC158_IN_INV_SEL_lsb)
    @GPIO_FUNC158_IN_INV_SEL.setter
    def GPIO_FUNC158_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC158_IN_INV_SEL_msb, self.__GPIO_FUNC158_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC158_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC158_IN_SEL_msb, self.__GPIO_FUNC158_IN_SEL_lsb)
    @GPIO_FUNC158_IN_SEL.setter
    def GPIO_FUNC158_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC158_IN_SEL_msb, self.__GPIO_FUNC158_IN_SEL_lsb, value)
class GPIO_FUNC159_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x3ac
        self.__GPIO_SIG159_IN_SEL_lsb = 7
        self.__GPIO_SIG159_IN_SEL_msb = 7
        self.__GPIO_FUNC159_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC159_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC159_IN_SEL_lsb = 0
        self.__GPIO_FUNC159_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG159_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG159_IN_SEL_msb, self.__GPIO_SIG159_IN_SEL_lsb)
    @GPIO_SIG159_IN_SEL.setter
    def GPIO_SIG159_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG159_IN_SEL_msb, self.__GPIO_SIG159_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC159_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC159_IN_INV_SEL_msb, self.__GPIO_FUNC159_IN_INV_SEL_lsb)
    @GPIO_FUNC159_IN_INV_SEL.setter
    def GPIO_FUNC159_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC159_IN_INV_SEL_msb, self.__GPIO_FUNC159_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC159_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC159_IN_SEL_msb, self.__GPIO_FUNC159_IN_SEL_lsb)
    @GPIO_FUNC159_IN_SEL.setter
    def GPIO_FUNC159_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC159_IN_SEL_msb, self.__GPIO_FUNC159_IN_SEL_lsb, value)
class GPIO_FUNC160_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x3b0
        self.__GPIO_SIG160_IN_SEL_lsb = 7
        self.__GPIO_SIG160_IN_SEL_msb = 7
        self.__GPIO_FUNC160_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC160_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC160_IN_SEL_lsb = 0
        self.__GPIO_FUNC160_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG160_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG160_IN_SEL_msb, self.__GPIO_SIG160_IN_SEL_lsb)
    @GPIO_SIG160_IN_SEL.setter
    def GPIO_SIG160_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG160_IN_SEL_msb, self.__GPIO_SIG160_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC160_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC160_IN_INV_SEL_msb, self.__GPIO_FUNC160_IN_INV_SEL_lsb)
    @GPIO_FUNC160_IN_INV_SEL.setter
    def GPIO_FUNC160_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC160_IN_INV_SEL_msb, self.__GPIO_FUNC160_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC160_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC160_IN_SEL_msb, self.__GPIO_FUNC160_IN_SEL_lsb)
    @GPIO_FUNC160_IN_SEL.setter
    def GPIO_FUNC160_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC160_IN_SEL_msb, self.__GPIO_FUNC160_IN_SEL_lsb, value)
class GPIO_FUNC161_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x3b4
        self.__GPIO_SIG161_IN_SEL_lsb = 7
        self.__GPIO_SIG161_IN_SEL_msb = 7
        self.__GPIO_FUNC161_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC161_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC161_IN_SEL_lsb = 0
        self.__GPIO_FUNC161_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG161_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG161_IN_SEL_msb, self.__GPIO_SIG161_IN_SEL_lsb)
    @GPIO_SIG161_IN_SEL.setter
    def GPIO_SIG161_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG161_IN_SEL_msb, self.__GPIO_SIG161_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC161_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC161_IN_INV_SEL_msb, self.__GPIO_FUNC161_IN_INV_SEL_lsb)
    @GPIO_FUNC161_IN_INV_SEL.setter
    def GPIO_FUNC161_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC161_IN_INV_SEL_msb, self.__GPIO_FUNC161_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC161_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC161_IN_SEL_msb, self.__GPIO_FUNC161_IN_SEL_lsb)
    @GPIO_FUNC161_IN_SEL.setter
    def GPIO_FUNC161_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC161_IN_SEL_msb, self.__GPIO_FUNC161_IN_SEL_lsb, value)
class GPIO_FUNC162_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x3b8
        self.__GPIO_SIG162_IN_SEL_lsb = 7
        self.__GPIO_SIG162_IN_SEL_msb = 7
        self.__GPIO_FUNC162_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC162_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC162_IN_SEL_lsb = 0
        self.__GPIO_FUNC162_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG162_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG162_IN_SEL_msb, self.__GPIO_SIG162_IN_SEL_lsb)
    @GPIO_SIG162_IN_SEL.setter
    def GPIO_SIG162_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG162_IN_SEL_msb, self.__GPIO_SIG162_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC162_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC162_IN_INV_SEL_msb, self.__GPIO_FUNC162_IN_INV_SEL_lsb)
    @GPIO_FUNC162_IN_INV_SEL.setter
    def GPIO_FUNC162_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC162_IN_INV_SEL_msb, self.__GPIO_FUNC162_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC162_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC162_IN_SEL_msb, self.__GPIO_FUNC162_IN_SEL_lsb)
    @GPIO_FUNC162_IN_SEL.setter
    def GPIO_FUNC162_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC162_IN_SEL_msb, self.__GPIO_FUNC162_IN_SEL_lsb, value)
class GPIO_FUNC163_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x3bc
        self.__GPIO_SIG163_IN_SEL_lsb = 7
        self.__GPIO_SIG163_IN_SEL_msb = 7
        self.__GPIO_FUNC163_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC163_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC163_IN_SEL_lsb = 0
        self.__GPIO_FUNC163_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG163_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG163_IN_SEL_msb, self.__GPIO_SIG163_IN_SEL_lsb)
    @GPIO_SIG163_IN_SEL.setter
    def GPIO_SIG163_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG163_IN_SEL_msb, self.__GPIO_SIG163_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC163_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC163_IN_INV_SEL_msb, self.__GPIO_FUNC163_IN_INV_SEL_lsb)
    @GPIO_FUNC163_IN_INV_SEL.setter
    def GPIO_FUNC163_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC163_IN_INV_SEL_msb, self.__GPIO_FUNC163_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC163_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC163_IN_SEL_msb, self.__GPIO_FUNC163_IN_SEL_lsb)
    @GPIO_FUNC163_IN_SEL.setter
    def GPIO_FUNC163_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC163_IN_SEL_msb, self.__GPIO_FUNC163_IN_SEL_lsb, value)
class GPIO_FUNC164_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x3c0
        self.__GPIO_SIG164_IN_SEL_lsb = 7
        self.__GPIO_SIG164_IN_SEL_msb = 7
        self.__GPIO_FUNC164_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC164_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC164_IN_SEL_lsb = 0
        self.__GPIO_FUNC164_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG164_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG164_IN_SEL_msb, self.__GPIO_SIG164_IN_SEL_lsb)
    @GPIO_SIG164_IN_SEL.setter
    def GPIO_SIG164_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG164_IN_SEL_msb, self.__GPIO_SIG164_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC164_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC164_IN_INV_SEL_msb, self.__GPIO_FUNC164_IN_INV_SEL_lsb)
    @GPIO_FUNC164_IN_INV_SEL.setter
    def GPIO_FUNC164_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC164_IN_INV_SEL_msb, self.__GPIO_FUNC164_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC164_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC164_IN_SEL_msb, self.__GPIO_FUNC164_IN_SEL_lsb)
    @GPIO_FUNC164_IN_SEL.setter
    def GPIO_FUNC164_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC164_IN_SEL_msb, self.__GPIO_FUNC164_IN_SEL_lsb, value)
class GPIO_FUNC165_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x3c4
        self.__GPIO_SIG165_IN_SEL_lsb = 7
        self.__GPIO_SIG165_IN_SEL_msb = 7
        self.__GPIO_FUNC165_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC165_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC165_IN_SEL_lsb = 0
        self.__GPIO_FUNC165_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG165_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG165_IN_SEL_msb, self.__GPIO_SIG165_IN_SEL_lsb)
    @GPIO_SIG165_IN_SEL.setter
    def GPIO_SIG165_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG165_IN_SEL_msb, self.__GPIO_SIG165_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC165_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC165_IN_INV_SEL_msb, self.__GPIO_FUNC165_IN_INV_SEL_lsb)
    @GPIO_FUNC165_IN_INV_SEL.setter
    def GPIO_FUNC165_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC165_IN_INV_SEL_msb, self.__GPIO_FUNC165_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC165_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC165_IN_SEL_msb, self.__GPIO_FUNC165_IN_SEL_lsb)
    @GPIO_FUNC165_IN_SEL.setter
    def GPIO_FUNC165_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC165_IN_SEL_msb, self.__GPIO_FUNC165_IN_SEL_lsb, value)
class GPIO_FUNC166_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x3c8
        self.__GPIO_SIG166_IN_SEL_lsb = 7
        self.__GPIO_SIG166_IN_SEL_msb = 7
        self.__GPIO_FUNC166_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC166_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC166_IN_SEL_lsb = 0
        self.__GPIO_FUNC166_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG166_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG166_IN_SEL_msb, self.__GPIO_SIG166_IN_SEL_lsb)
    @GPIO_SIG166_IN_SEL.setter
    def GPIO_SIG166_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG166_IN_SEL_msb, self.__GPIO_SIG166_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC166_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC166_IN_INV_SEL_msb, self.__GPIO_FUNC166_IN_INV_SEL_lsb)
    @GPIO_FUNC166_IN_INV_SEL.setter
    def GPIO_FUNC166_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC166_IN_INV_SEL_msb, self.__GPIO_FUNC166_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC166_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC166_IN_SEL_msb, self.__GPIO_FUNC166_IN_SEL_lsb)
    @GPIO_FUNC166_IN_SEL.setter
    def GPIO_FUNC166_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC166_IN_SEL_msb, self.__GPIO_FUNC166_IN_SEL_lsb, value)
class GPIO_FUNC167_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x3cc
        self.__GPIO_SIG167_IN_SEL_lsb = 7
        self.__GPIO_SIG167_IN_SEL_msb = 7
        self.__GPIO_FUNC167_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC167_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC167_IN_SEL_lsb = 0
        self.__GPIO_FUNC167_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG167_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG167_IN_SEL_msb, self.__GPIO_SIG167_IN_SEL_lsb)
    @GPIO_SIG167_IN_SEL.setter
    def GPIO_SIG167_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG167_IN_SEL_msb, self.__GPIO_SIG167_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC167_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC167_IN_INV_SEL_msb, self.__GPIO_FUNC167_IN_INV_SEL_lsb)
    @GPIO_FUNC167_IN_INV_SEL.setter
    def GPIO_FUNC167_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC167_IN_INV_SEL_msb, self.__GPIO_FUNC167_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC167_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC167_IN_SEL_msb, self.__GPIO_FUNC167_IN_SEL_lsb)
    @GPIO_FUNC167_IN_SEL.setter
    def GPIO_FUNC167_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC167_IN_SEL_msb, self.__GPIO_FUNC167_IN_SEL_lsb, value)
class GPIO_FUNC168_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x3d0
        self.__GPIO_SIG168_IN_SEL_lsb = 7
        self.__GPIO_SIG168_IN_SEL_msb = 7
        self.__GPIO_FUNC168_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC168_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC168_IN_SEL_lsb = 0
        self.__GPIO_FUNC168_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG168_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG168_IN_SEL_msb, self.__GPIO_SIG168_IN_SEL_lsb)
    @GPIO_SIG168_IN_SEL.setter
    def GPIO_SIG168_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG168_IN_SEL_msb, self.__GPIO_SIG168_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC168_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC168_IN_INV_SEL_msb, self.__GPIO_FUNC168_IN_INV_SEL_lsb)
    @GPIO_FUNC168_IN_INV_SEL.setter
    def GPIO_FUNC168_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC168_IN_INV_SEL_msb, self.__GPIO_FUNC168_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC168_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC168_IN_SEL_msb, self.__GPIO_FUNC168_IN_SEL_lsb)
    @GPIO_FUNC168_IN_SEL.setter
    def GPIO_FUNC168_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC168_IN_SEL_msb, self.__GPIO_FUNC168_IN_SEL_lsb, value)
class GPIO_FUNC169_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x3d4
        self.__GPIO_SIG169_IN_SEL_lsb = 7
        self.__GPIO_SIG169_IN_SEL_msb = 7
        self.__GPIO_FUNC169_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC169_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC169_IN_SEL_lsb = 0
        self.__GPIO_FUNC169_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG169_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG169_IN_SEL_msb, self.__GPIO_SIG169_IN_SEL_lsb)
    @GPIO_SIG169_IN_SEL.setter
    def GPIO_SIG169_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG169_IN_SEL_msb, self.__GPIO_SIG169_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC169_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC169_IN_INV_SEL_msb, self.__GPIO_FUNC169_IN_INV_SEL_lsb)
    @GPIO_FUNC169_IN_INV_SEL.setter
    def GPIO_FUNC169_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC169_IN_INV_SEL_msb, self.__GPIO_FUNC169_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC169_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC169_IN_SEL_msb, self.__GPIO_FUNC169_IN_SEL_lsb)
    @GPIO_FUNC169_IN_SEL.setter
    def GPIO_FUNC169_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC169_IN_SEL_msb, self.__GPIO_FUNC169_IN_SEL_lsb, value)
class GPIO_FUNC170_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x3d8
        self.__GPIO_SIG170_IN_SEL_lsb = 7
        self.__GPIO_SIG170_IN_SEL_msb = 7
        self.__GPIO_FUNC170_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC170_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC170_IN_SEL_lsb = 0
        self.__GPIO_FUNC170_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG170_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG170_IN_SEL_msb, self.__GPIO_SIG170_IN_SEL_lsb)
    @GPIO_SIG170_IN_SEL.setter
    def GPIO_SIG170_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG170_IN_SEL_msb, self.__GPIO_SIG170_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC170_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC170_IN_INV_SEL_msb, self.__GPIO_FUNC170_IN_INV_SEL_lsb)
    @GPIO_FUNC170_IN_INV_SEL.setter
    def GPIO_FUNC170_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC170_IN_INV_SEL_msb, self.__GPIO_FUNC170_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC170_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC170_IN_SEL_msb, self.__GPIO_FUNC170_IN_SEL_lsb)
    @GPIO_FUNC170_IN_SEL.setter
    def GPIO_FUNC170_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC170_IN_SEL_msb, self.__GPIO_FUNC170_IN_SEL_lsb, value)
class GPIO_FUNC171_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x3dc
        self.__GPIO_SIG171_IN_SEL_lsb = 7
        self.__GPIO_SIG171_IN_SEL_msb = 7
        self.__GPIO_FUNC171_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC171_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC171_IN_SEL_lsb = 0
        self.__GPIO_FUNC171_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG171_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG171_IN_SEL_msb, self.__GPIO_SIG171_IN_SEL_lsb)
    @GPIO_SIG171_IN_SEL.setter
    def GPIO_SIG171_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG171_IN_SEL_msb, self.__GPIO_SIG171_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC171_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC171_IN_INV_SEL_msb, self.__GPIO_FUNC171_IN_INV_SEL_lsb)
    @GPIO_FUNC171_IN_INV_SEL.setter
    def GPIO_FUNC171_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC171_IN_INV_SEL_msb, self.__GPIO_FUNC171_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC171_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC171_IN_SEL_msb, self.__GPIO_FUNC171_IN_SEL_lsb)
    @GPIO_FUNC171_IN_SEL.setter
    def GPIO_FUNC171_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC171_IN_SEL_msb, self.__GPIO_FUNC171_IN_SEL_lsb, value)
class GPIO_FUNC172_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x3e0
        self.__GPIO_SIG172_IN_SEL_lsb = 7
        self.__GPIO_SIG172_IN_SEL_msb = 7
        self.__GPIO_FUNC172_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC172_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC172_IN_SEL_lsb = 0
        self.__GPIO_FUNC172_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG172_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG172_IN_SEL_msb, self.__GPIO_SIG172_IN_SEL_lsb)
    @GPIO_SIG172_IN_SEL.setter
    def GPIO_SIG172_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG172_IN_SEL_msb, self.__GPIO_SIG172_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC172_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC172_IN_INV_SEL_msb, self.__GPIO_FUNC172_IN_INV_SEL_lsb)
    @GPIO_FUNC172_IN_INV_SEL.setter
    def GPIO_FUNC172_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC172_IN_INV_SEL_msb, self.__GPIO_FUNC172_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC172_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC172_IN_SEL_msb, self.__GPIO_FUNC172_IN_SEL_lsb)
    @GPIO_FUNC172_IN_SEL.setter
    def GPIO_FUNC172_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC172_IN_SEL_msb, self.__GPIO_FUNC172_IN_SEL_lsb, value)
class GPIO_FUNC173_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x3e4
        self.__GPIO_SIG173_IN_SEL_lsb = 7
        self.__GPIO_SIG173_IN_SEL_msb = 7
        self.__GPIO_FUNC173_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC173_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC173_IN_SEL_lsb = 0
        self.__GPIO_FUNC173_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG173_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG173_IN_SEL_msb, self.__GPIO_SIG173_IN_SEL_lsb)
    @GPIO_SIG173_IN_SEL.setter
    def GPIO_SIG173_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG173_IN_SEL_msb, self.__GPIO_SIG173_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC173_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC173_IN_INV_SEL_msb, self.__GPIO_FUNC173_IN_INV_SEL_lsb)
    @GPIO_FUNC173_IN_INV_SEL.setter
    def GPIO_FUNC173_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC173_IN_INV_SEL_msb, self.__GPIO_FUNC173_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC173_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC173_IN_SEL_msb, self.__GPIO_FUNC173_IN_SEL_lsb)
    @GPIO_FUNC173_IN_SEL.setter
    def GPIO_FUNC173_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC173_IN_SEL_msb, self.__GPIO_FUNC173_IN_SEL_lsb, value)
class GPIO_FUNC174_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x3e8
        self.__GPIO_SIG174_IN_SEL_lsb = 7
        self.__GPIO_SIG174_IN_SEL_msb = 7
        self.__GPIO_FUNC174_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC174_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC174_IN_SEL_lsb = 0
        self.__GPIO_FUNC174_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG174_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG174_IN_SEL_msb, self.__GPIO_SIG174_IN_SEL_lsb)
    @GPIO_SIG174_IN_SEL.setter
    def GPIO_SIG174_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG174_IN_SEL_msb, self.__GPIO_SIG174_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC174_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC174_IN_INV_SEL_msb, self.__GPIO_FUNC174_IN_INV_SEL_lsb)
    @GPIO_FUNC174_IN_INV_SEL.setter
    def GPIO_FUNC174_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC174_IN_INV_SEL_msb, self.__GPIO_FUNC174_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC174_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC174_IN_SEL_msb, self.__GPIO_FUNC174_IN_SEL_lsb)
    @GPIO_FUNC174_IN_SEL.setter
    def GPIO_FUNC174_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC174_IN_SEL_msb, self.__GPIO_FUNC174_IN_SEL_lsb, value)
class GPIO_FUNC175_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x3ec
        self.__GPIO_SIG175_IN_SEL_lsb = 7
        self.__GPIO_SIG175_IN_SEL_msb = 7
        self.__GPIO_FUNC175_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC175_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC175_IN_SEL_lsb = 0
        self.__GPIO_FUNC175_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG175_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG175_IN_SEL_msb, self.__GPIO_SIG175_IN_SEL_lsb)
    @GPIO_SIG175_IN_SEL.setter
    def GPIO_SIG175_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG175_IN_SEL_msb, self.__GPIO_SIG175_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC175_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC175_IN_INV_SEL_msb, self.__GPIO_FUNC175_IN_INV_SEL_lsb)
    @GPIO_FUNC175_IN_INV_SEL.setter
    def GPIO_FUNC175_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC175_IN_INV_SEL_msb, self.__GPIO_FUNC175_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC175_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC175_IN_SEL_msb, self.__GPIO_FUNC175_IN_SEL_lsb)
    @GPIO_FUNC175_IN_SEL.setter
    def GPIO_FUNC175_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC175_IN_SEL_msb, self.__GPIO_FUNC175_IN_SEL_lsb, value)
class GPIO_FUNC176_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x3f0
        self.__GPIO_SIG176_IN_SEL_lsb = 7
        self.__GPIO_SIG176_IN_SEL_msb = 7
        self.__GPIO_FUNC176_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC176_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC176_IN_SEL_lsb = 0
        self.__GPIO_FUNC176_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG176_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG176_IN_SEL_msb, self.__GPIO_SIG176_IN_SEL_lsb)
    @GPIO_SIG176_IN_SEL.setter
    def GPIO_SIG176_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG176_IN_SEL_msb, self.__GPIO_SIG176_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC176_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC176_IN_INV_SEL_msb, self.__GPIO_FUNC176_IN_INV_SEL_lsb)
    @GPIO_FUNC176_IN_INV_SEL.setter
    def GPIO_FUNC176_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC176_IN_INV_SEL_msb, self.__GPIO_FUNC176_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC176_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC176_IN_SEL_msb, self.__GPIO_FUNC176_IN_SEL_lsb)
    @GPIO_FUNC176_IN_SEL.setter
    def GPIO_FUNC176_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC176_IN_SEL_msb, self.__GPIO_FUNC176_IN_SEL_lsb, value)
class GPIO_FUNC177_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x3f4
        self.__GPIO_SIG177_IN_SEL_lsb = 7
        self.__GPIO_SIG177_IN_SEL_msb = 7
        self.__GPIO_FUNC177_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC177_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC177_IN_SEL_lsb = 0
        self.__GPIO_FUNC177_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG177_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG177_IN_SEL_msb, self.__GPIO_SIG177_IN_SEL_lsb)
    @GPIO_SIG177_IN_SEL.setter
    def GPIO_SIG177_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG177_IN_SEL_msb, self.__GPIO_SIG177_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC177_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC177_IN_INV_SEL_msb, self.__GPIO_FUNC177_IN_INV_SEL_lsb)
    @GPIO_FUNC177_IN_INV_SEL.setter
    def GPIO_FUNC177_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC177_IN_INV_SEL_msb, self.__GPIO_FUNC177_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC177_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC177_IN_SEL_msb, self.__GPIO_FUNC177_IN_SEL_lsb)
    @GPIO_FUNC177_IN_SEL.setter
    def GPIO_FUNC177_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC177_IN_SEL_msb, self.__GPIO_FUNC177_IN_SEL_lsb, value)
class GPIO_FUNC178_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x3f8
        self.__GPIO_SIG178_IN_SEL_lsb = 7
        self.__GPIO_SIG178_IN_SEL_msb = 7
        self.__GPIO_FUNC178_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC178_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC178_IN_SEL_lsb = 0
        self.__GPIO_FUNC178_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG178_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG178_IN_SEL_msb, self.__GPIO_SIG178_IN_SEL_lsb)
    @GPIO_SIG178_IN_SEL.setter
    def GPIO_SIG178_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG178_IN_SEL_msb, self.__GPIO_SIG178_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC178_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC178_IN_INV_SEL_msb, self.__GPIO_FUNC178_IN_INV_SEL_lsb)
    @GPIO_FUNC178_IN_INV_SEL.setter
    def GPIO_FUNC178_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC178_IN_INV_SEL_msb, self.__GPIO_FUNC178_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC178_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC178_IN_SEL_msb, self.__GPIO_FUNC178_IN_SEL_lsb)
    @GPIO_FUNC178_IN_SEL.setter
    def GPIO_FUNC178_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC178_IN_SEL_msb, self.__GPIO_FUNC178_IN_SEL_lsb, value)
class GPIO_FUNC179_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x3fc
        self.__GPIO_SIG179_IN_SEL_lsb = 7
        self.__GPIO_SIG179_IN_SEL_msb = 7
        self.__GPIO_FUNC179_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC179_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC179_IN_SEL_lsb = 0
        self.__GPIO_FUNC179_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG179_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG179_IN_SEL_msb, self.__GPIO_SIG179_IN_SEL_lsb)
    @GPIO_SIG179_IN_SEL.setter
    def GPIO_SIG179_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG179_IN_SEL_msb, self.__GPIO_SIG179_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC179_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC179_IN_INV_SEL_msb, self.__GPIO_FUNC179_IN_INV_SEL_lsb)
    @GPIO_FUNC179_IN_INV_SEL.setter
    def GPIO_FUNC179_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC179_IN_INV_SEL_msb, self.__GPIO_FUNC179_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC179_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC179_IN_SEL_msb, self.__GPIO_FUNC179_IN_SEL_lsb)
    @GPIO_FUNC179_IN_SEL.setter
    def GPIO_FUNC179_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC179_IN_SEL_msb, self.__GPIO_FUNC179_IN_SEL_lsb, value)
class GPIO_FUNC180_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x400
        self.__GPIO_SIG180_IN_SEL_lsb = 7
        self.__GPIO_SIG180_IN_SEL_msb = 7
        self.__GPIO_FUNC180_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC180_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC180_IN_SEL_lsb = 0
        self.__GPIO_FUNC180_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG180_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG180_IN_SEL_msb, self.__GPIO_SIG180_IN_SEL_lsb)
    @GPIO_SIG180_IN_SEL.setter
    def GPIO_SIG180_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG180_IN_SEL_msb, self.__GPIO_SIG180_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC180_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC180_IN_INV_SEL_msb, self.__GPIO_FUNC180_IN_INV_SEL_lsb)
    @GPIO_FUNC180_IN_INV_SEL.setter
    def GPIO_FUNC180_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC180_IN_INV_SEL_msb, self.__GPIO_FUNC180_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC180_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC180_IN_SEL_msb, self.__GPIO_FUNC180_IN_SEL_lsb)
    @GPIO_FUNC180_IN_SEL.setter
    def GPIO_FUNC180_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC180_IN_SEL_msb, self.__GPIO_FUNC180_IN_SEL_lsb, value)
class GPIO_FUNC181_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x404
        self.__GPIO_SIG181_IN_SEL_lsb = 7
        self.__GPIO_SIG181_IN_SEL_msb = 7
        self.__GPIO_FUNC181_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC181_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC181_IN_SEL_lsb = 0
        self.__GPIO_FUNC181_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG181_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG181_IN_SEL_msb, self.__GPIO_SIG181_IN_SEL_lsb)
    @GPIO_SIG181_IN_SEL.setter
    def GPIO_SIG181_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG181_IN_SEL_msb, self.__GPIO_SIG181_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC181_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC181_IN_INV_SEL_msb, self.__GPIO_FUNC181_IN_INV_SEL_lsb)
    @GPIO_FUNC181_IN_INV_SEL.setter
    def GPIO_FUNC181_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC181_IN_INV_SEL_msb, self.__GPIO_FUNC181_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC181_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC181_IN_SEL_msb, self.__GPIO_FUNC181_IN_SEL_lsb)
    @GPIO_FUNC181_IN_SEL.setter
    def GPIO_FUNC181_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC181_IN_SEL_msb, self.__GPIO_FUNC181_IN_SEL_lsb, value)
class GPIO_FUNC182_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x408
        self.__GPIO_SIG182_IN_SEL_lsb = 7
        self.__GPIO_SIG182_IN_SEL_msb = 7
        self.__GPIO_FUNC182_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC182_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC182_IN_SEL_lsb = 0
        self.__GPIO_FUNC182_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG182_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG182_IN_SEL_msb, self.__GPIO_SIG182_IN_SEL_lsb)
    @GPIO_SIG182_IN_SEL.setter
    def GPIO_SIG182_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG182_IN_SEL_msb, self.__GPIO_SIG182_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC182_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC182_IN_INV_SEL_msb, self.__GPIO_FUNC182_IN_INV_SEL_lsb)
    @GPIO_FUNC182_IN_INV_SEL.setter
    def GPIO_FUNC182_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC182_IN_INV_SEL_msb, self.__GPIO_FUNC182_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC182_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC182_IN_SEL_msb, self.__GPIO_FUNC182_IN_SEL_lsb)
    @GPIO_FUNC182_IN_SEL.setter
    def GPIO_FUNC182_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC182_IN_SEL_msb, self.__GPIO_FUNC182_IN_SEL_lsb, value)
class GPIO_FUNC183_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x40c
        self.__GPIO_SIG183_IN_SEL_lsb = 7
        self.__GPIO_SIG183_IN_SEL_msb = 7
        self.__GPIO_FUNC183_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC183_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC183_IN_SEL_lsb = 0
        self.__GPIO_FUNC183_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG183_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG183_IN_SEL_msb, self.__GPIO_SIG183_IN_SEL_lsb)
    @GPIO_SIG183_IN_SEL.setter
    def GPIO_SIG183_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG183_IN_SEL_msb, self.__GPIO_SIG183_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC183_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC183_IN_INV_SEL_msb, self.__GPIO_FUNC183_IN_INV_SEL_lsb)
    @GPIO_FUNC183_IN_INV_SEL.setter
    def GPIO_FUNC183_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC183_IN_INV_SEL_msb, self.__GPIO_FUNC183_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC183_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC183_IN_SEL_msb, self.__GPIO_FUNC183_IN_SEL_lsb)
    @GPIO_FUNC183_IN_SEL.setter
    def GPIO_FUNC183_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC183_IN_SEL_msb, self.__GPIO_FUNC183_IN_SEL_lsb, value)
class GPIO_FUNC184_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x410
        self.__GPIO_SIG184_IN_SEL_lsb = 7
        self.__GPIO_SIG184_IN_SEL_msb = 7
        self.__GPIO_FUNC184_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC184_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC184_IN_SEL_lsb = 0
        self.__GPIO_FUNC184_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG184_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG184_IN_SEL_msb, self.__GPIO_SIG184_IN_SEL_lsb)
    @GPIO_SIG184_IN_SEL.setter
    def GPIO_SIG184_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG184_IN_SEL_msb, self.__GPIO_SIG184_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC184_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC184_IN_INV_SEL_msb, self.__GPIO_FUNC184_IN_INV_SEL_lsb)
    @GPIO_FUNC184_IN_INV_SEL.setter
    def GPIO_FUNC184_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC184_IN_INV_SEL_msb, self.__GPIO_FUNC184_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC184_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC184_IN_SEL_msb, self.__GPIO_FUNC184_IN_SEL_lsb)
    @GPIO_FUNC184_IN_SEL.setter
    def GPIO_FUNC184_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC184_IN_SEL_msb, self.__GPIO_FUNC184_IN_SEL_lsb, value)
class GPIO_FUNC185_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x414
        self.__GPIO_SIG185_IN_SEL_lsb = 7
        self.__GPIO_SIG185_IN_SEL_msb = 7
        self.__GPIO_FUNC185_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC185_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC185_IN_SEL_lsb = 0
        self.__GPIO_FUNC185_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG185_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG185_IN_SEL_msb, self.__GPIO_SIG185_IN_SEL_lsb)
    @GPIO_SIG185_IN_SEL.setter
    def GPIO_SIG185_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG185_IN_SEL_msb, self.__GPIO_SIG185_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC185_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC185_IN_INV_SEL_msb, self.__GPIO_FUNC185_IN_INV_SEL_lsb)
    @GPIO_FUNC185_IN_INV_SEL.setter
    def GPIO_FUNC185_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC185_IN_INV_SEL_msb, self.__GPIO_FUNC185_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC185_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC185_IN_SEL_msb, self.__GPIO_FUNC185_IN_SEL_lsb)
    @GPIO_FUNC185_IN_SEL.setter
    def GPIO_FUNC185_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC185_IN_SEL_msb, self.__GPIO_FUNC185_IN_SEL_lsb, value)
class GPIO_FUNC186_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x418
        self.__GPIO_SIG186_IN_SEL_lsb = 7
        self.__GPIO_SIG186_IN_SEL_msb = 7
        self.__GPIO_FUNC186_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC186_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC186_IN_SEL_lsb = 0
        self.__GPIO_FUNC186_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG186_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG186_IN_SEL_msb, self.__GPIO_SIG186_IN_SEL_lsb)
    @GPIO_SIG186_IN_SEL.setter
    def GPIO_SIG186_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG186_IN_SEL_msb, self.__GPIO_SIG186_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC186_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC186_IN_INV_SEL_msb, self.__GPIO_FUNC186_IN_INV_SEL_lsb)
    @GPIO_FUNC186_IN_INV_SEL.setter
    def GPIO_FUNC186_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC186_IN_INV_SEL_msb, self.__GPIO_FUNC186_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC186_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC186_IN_SEL_msb, self.__GPIO_FUNC186_IN_SEL_lsb)
    @GPIO_FUNC186_IN_SEL.setter
    def GPIO_FUNC186_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC186_IN_SEL_msb, self.__GPIO_FUNC186_IN_SEL_lsb, value)
class GPIO_FUNC187_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x41c
        self.__GPIO_SIG187_IN_SEL_lsb = 7
        self.__GPIO_SIG187_IN_SEL_msb = 7
        self.__GPIO_FUNC187_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC187_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC187_IN_SEL_lsb = 0
        self.__GPIO_FUNC187_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG187_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG187_IN_SEL_msb, self.__GPIO_SIG187_IN_SEL_lsb)
    @GPIO_SIG187_IN_SEL.setter
    def GPIO_SIG187_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG187_IN_SEL_msb, self.__GPIO_SIG187_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC187_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC187_IN_INV_SEL_msb, self.__GPIO_FUNC187_IN_INV_SEL_lsb)
    @GPIO_FUNC187_IN_INV_SEL.setter
    def GPIO_FUNC187_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC187_IN_INV_SEL_msb, self.__GPIO_FUNC187_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC187_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC187_IN_SEL_msb, self.__GPIO_FUNC187_IN_SEL_lsb)
    @GPIO_FUNC187_IN_SEL.setter
    def GPIO_FUNC187_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC187_IN_SEL_msb, self.__GPIO_FUNC187_IN_SEL_lsb, value)
class GPIO_FUNC188_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x420
        self.__GPIO_SIG188_IN_SEL_lsb = 7
        self.__GPIO_SIG188_IN_SEL_msb = 7
        self.__GPIO_FUNC188_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC188_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC188_IN_SEL_lsb = 0
        self.__GPIO_FUNC188_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG188_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG188_IN_SEL_msb, self.__GPIO_SIG188_IN_SEL_lsb)
    @GPIO_SIG188_IN_SEL.setter
    def GPIO_SIG188_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG188_IN_SEL_msb, self.__GPIO_SIG188_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC188_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC188_IN_INV_SEL_msb, self.__GPIO_FUNC188_IN_INV_SEL_lsb)
    @GPIO_FUNC188_IN_INV_SEL.setter
    def GPIO_FUNC188_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC188_IN_INV_SEL_msb, self.__GPIO_FUNC188_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC188_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC188_IN_SEL_msb, self.__GPIO_FUNC188_IN_SEL_lsb)
    @GPIO_FUNC188_IN_SEL.setter
    def GPIO_FUNC188_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC188_IN_SEL_msb, self.__GPIO_FUNC188_IN_SEL_lsb, value)
class GPIO_FUNC189_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x424
        self.__GPIO_SIG189_IN_SEL_lsb = 7
        self.__GPIO_SIG189_IN_SEL_msb = 7
        self.__GPIO_FUNC189_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC189_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC189_IN_SEL_lsb = 0
        self.__GPIO_FUNC189_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG189_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG189_IN_SEL_msb, self.__GPIO_SIG189_IN_SEL_lsb)
    @GPIO_SIG189_IN_SEL.setter
    def GPIO_SIG189_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG189_IN_SEL_msb, self.__GPIO_SIG189_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC189_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC189_IN_INV_SEL_msb, self.__GPIO_FUNC189_IN_INV_SEL_lsb)
    @GPIO_FUNC189_IN_INV_SEL.setter
    def GPIO_FUNC189_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC189_IN_INV_SEL_msb, self.__GPIO_FUNC189_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC189_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC189_IN_SEL_msb, self.__GPIO_FUNC189_IN_SEL_lsb)
    @GPIO_FUNC189_IN_SEL.setter
    def GPIO_FUNC189_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC189_IN_SEL_msb, self.__GPIO_FUNC189_IN_SEL_lsb, value)
class GPIO_FUNC190_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x428
        self.__GPIO_SIG190_IN_SEL_lsb = 7
        self.__GPIO_SIG190_IN_SEL_msb = 7
        self.__GPIO_FUNC190_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC190_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC190_IN_SEL_lsb = 0
        self.__GPIO_FUNC190_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG190_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG190_IN_SEL_msb, self.__GPIO_SIG190_IN_SEL_lsb)
    @GPIO_SIG190_IN_SEL.setter
    def GPIO_SIG190_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG190_IN_SEL_msb, self.__GPIO_SIG190_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC190_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC190_IN_INV_SEL_msb, self.__GPIO_FUNC190_IN_INV_SEL_lsb)
    @GPIO_FUNC190_IN_INV_SEL.setter
    def GPIO_FUNC190_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC190_IN_INV_SEL_msb, self.__GPIO_FUNC190_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC190_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC190_IN_SEL_msb, self.__GPIO_FUNC190_IN_SEL_lsb)
    @GPIO_FUNC190_IN_SEL.setter
    def GPIO_FUNC190_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC190_IN_SEL_msb, self.__GPIO_FUNC190_IN_SEL_lsb, value)
class GPIO_FUNC191_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x42c
        self.__GPIO_SIG191_IN_SEL_lsb = 7
        self.__GPIO_SIG191_IN_SEL_msb = 7
        self.__GPIO_FUNC191_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC191_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC191_IN_SEL_lsb = 0
        self.__GPIO_FUNC191_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG191_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG191_IN_SEL_msb, self.__GPIO_SIG191_IN_SEL_lsb)
    @GPIO_SIG191_IN_SEL.setter
    def GPIO_SIG191_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG191_IN_SEL_msb, self.__GPIO_SIG191_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC191_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC191_IN_INV_SEL_msb, self.__GPIO_FUNC191_IN_INV_SEL_lsb)
    @GPIO_FUNC191_IN_INV_SEL.setter
    def GPIO_FUNC191_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC191_IN_INV_SEL_msb, self.__GPIO_FUNC191_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC191_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC191_IN_SEL_msb, self.__GPIO_FUNC191_IN_SEL_lsb)
    @GPIO_FUNC191_IN_SEL.setter
    def GPIO_FUNC191_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC191_IN_SEL_msb, self.__GPIO_FUNC191_IN_SEL_lsb, value)
class GPIO_FUNC192_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x430
        self.__GPIO_SIG192_IN_SEL_lsb = 7
        self.__GPIO_SIG192_IN_SEL_msb = 7
        self.__GPIO_FUNC192_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC192_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC192_IN_SEL_lsb = 0
        self.__GPIO_FUNC192_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG192_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG192_IN_SEL_msb, self.__GPIO_SIG192_IN_SEL_lsb)
    @GPIO_SIG192_IN_SEL.setter
    def GPIO_SIG192_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG192_IN_SEL_msb, self.__GPIO_SIG192_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC192_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC192_IN_INV_SEL_msb, self.__GPIO_FUNC192_IN_INV_SEL_lsb)
    @GPIO_FUNC192_IN_INV_SEL.setter
    def GPIO_FUNC192_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC192_IN_INV_SEL_msb, self.__GPIO_FUNC192_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC192_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC192_IN_SEL_msb, self.__GPIO_FUNC192_IN_SEL_lsb)
    @GPIO_FUNC192_IN_SEL.setter
    def GPIO_FUNC192_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC192_IN_SEL_msb, self.__GPIO_FUNC192_IN_SEL_lsb, value)
class GPIO_FUNC193_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x434
        self.__GPIO_SIG193_IN_SEL_lsb = 7
        self.__GPIO_SIG193_IN_SEL_msb = 7
        self.__GPIO_FUNC193_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC193_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC193_IN_SEL_lsb = 0
        self.__GPIO_FUNC193_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG193_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG193_IN_SEL_msb, self.__GPIO_SIG193_IN_SEL_lsb)
    @GPIO_SIG193_IN_SEL.setter
    def GPIO_SIG193_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG193_IN_SEL_msb, self.__GPIO_SIG193_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC193_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC193_IN_INV_SEL_msb, self.__GPIO_FUNC193_IN_INV_SEL_lsb)
    @GPIO_FUNC193_IN_INV_SEL.setter
    def GPIO_FUNC193_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC193_IN_INV_SEL_msb, self.__GPIO_FUNC193_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC193_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC193_IN_SEL_msb, self.__GPIO_FUNC193_IN_SEL_lsb)
    @GPIO_FUNC193_IN_SEL.setter
    def GPIO_FUNC193_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC193_IN_SEL_msb, self.__GPIO_FUNC193_IN_SEL_lsb, value)
class GPIO_FUNC194_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x438
        self.__GPIO_SIG194_IN_SEL_lsb = 7
        self.__GPIO_SIG194_IN_SEL_msb = 7
        self.__GPIO_FUNC194_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC194_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC194_IN_SEL_lsb = 0
        self.__GPIO_FUNC194_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG194_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG194_IN_SEL_msb, self.__GPIO_SIG194_IN_SEL_lsb)
    @GPIO_SIG194_IN_SEL.setter
    def GPIO_SIG194_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG194_IN_SEL_msb, self.__GPIO_SIG194_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC194_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC194_IN_INV_SEL_msb, self.__GPIO_FUNC194_IN_INV_SEL_lsb)
    @GPIO_FUNC194_IN_INV_SEL.setter
    def GPIO_FUNC194_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC194_IN_INV_SEL_msb, self.__GPIO_FUNC194_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC194_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC194_IN_SEL_msb, self.__GPIO_FUNC194_IN_SEL_lsb)
    @GPIO_FUNC194_IN_SEL.setter
    def GPIO_FUNC194_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC194_IN_SEL_msb, self.__GPIO_FUNC194_IN_SEL_lsb, value)
class GPIO_FUNC195_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x43c
        self.__GPIO_SIG195_IN_SEL_lsb = 7
        self.__GPIO_SIG195_IN_SEL_msb = 7
        self.__GPIO_FUNC195_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC195_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC195_IN_SEL_lsb = 0
        self.__GPIO_FUNC195_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG195_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG195_IN_SEL_msb, self.__GPIO_SIG195_IN_SEL_lsb)
    @GPIO_SIG195_IN_SEL.setter
    def GPIO_SIG195_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG195_IN_SEL_msb, self.__GPIO_SIG195_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC195_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC195_IN_INV_SEL_msb, self.__GPIO_FUNC195_IN_INV_SEL_lsb)
    @GPIO_FUNC195_IN_INV_SEL.setter
    def GPIO_FUNC195_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC195_IN_INV_SEL_msb, self.__GPIO_FUNC195_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC195_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC195_IN_SEL_msb, self.__GPIO_FUNC195_IN_SEL_lsb)
    @GPIO_FUNC195_IN_SEL.setter
    def GPIO_FUNC195_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC195_IN_SEL_msb, self.__GPIO_FUNC195_IN_SEL_lsb, value)
class GPIO_FUNC196_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x440
        self.__GPIO_SIG196_IN_SEL_lsb = 7
        self.__GPIO_SIG196_IN_SEL_msb = 7
        self.__GPIO_FUNC196_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC196_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC196_IN_SEL_lsb = 0
        self.__GPIO_FUNC196_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG196_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG196_IN_SEL_msb, self.__GPIO_SIG196_IN_SEL_lsb)
    @GPIO_SIG196_IN_SEL.setter
    def GPIO_SIG196_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG196_IN_SEL_msb, self.__GPIO_SIG196_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC196_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC196_IN_INV_SEL_msb, self.__GPIO_FUNC196_IN_INV_SEL_lsb)
    @GPIO_FUNC196_IN_INV_SEL.setter
    def GPIO_FUNC196_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC196_IN_INV_SEL_msb, self.__GPIO_FUNC196_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC196_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC196_IN_SEL_msb, self.__GPIO_FUNC196_IN_SEL_lsb)
    @GPIO_FUNC196_IN_SEL.setter
    def GPIO_FUNC196_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC196_IN_SEL_msb, self.__GPIO_FUNC196_IN_SEL_lsb, value)
class GPIO_FUNC197_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x444
        self.__GPIO_SIG197_IN_SEL_lsb = 7
        self.__GPIO_SIG197_IN_SEL_msb = 7
        self.__GPIO_FUNC197_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC197_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC197_IN_SEL_lsb = 0
        self.__GPIO_FUNC197_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG197_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG197_IN_SEL_msb, self.__GPIO_SIG197_IN_SEL_lsb)
    @GPIO_SIG197_IN_SEL.setter
    def GPIO_SIG197_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG197_IN_SEL_msb, self.__GPIO_SIG197_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC197_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC197_IN_INV_SEL_msb, self.__GPIO_FUNC197_IN_INV_SEL_lsb)
    @GPIO_FUNC197_IN_INV_SEL.setter
    def GPIO_FUNC197_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC197_IN_INV_SEL_msb, self.__GPIO_FUNC197_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC197_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC197_IN_SEL_msb, self.__GPIO_FUNC197_IN_SEL_lsb)
    @GPIO_FUNC197_IN_SEL.setter
    def GPIO_FUNC197_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC197_IN_SEL_msb, self.__GPIO_FUNC197_IN_SEL_lsb, value)
class GPIO_FUNC198_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x448
        self.__GPIO_SIG198_IN_SEL_lsb = 7
        self.__GPIO_SIG198_IN_SEL_msb = 7
        self.__GPIO_FUNC198_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC198_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC198_IN_SEL_lsb = 0
        self.__GPIO_FUNC198_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG198_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG198_IN_SEL_msb, self.__GPIO_SIG198_IN_SEL_lsb)
    @GPIO_SIG198_IN_SEL.setter
    def GPIO_SIG198_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG198_IN_SEL_msb, self.__GPIO_SIG198_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC198_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC198_IN_INV_SEL_msb, self.__GPIO_FUNC198_IN_INV_SEL_lsb)
    @GPIO_FUNC198_IN_INV_SEL.setter
    def GPIO_FUNC198_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC198_IN_INV_SEL_msb, self.__GPIO_FUNC198_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC198_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC198_IN_SEL_msb, self.__GPIO_FUNC198_IN_SEL_lsb)
    @GPIO_FUNC198_IN_SEL.setter
    def GPIO_FUNC198_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC198_IN_SEL_msb, self.__GPIO_FUNC198_IN_SEL_lsb, value)
class GPIO_FUNC199_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x44c
        self.__GPIO_SIG199_IN_SEL_lsb = 7
        self.__GPIO_SIG199_IN_SEL_msb = 7
        self.__GPIO_FUNC199_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC199_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC199_IN_SEL_lsb = 0
        self.__GPIO_FUNC199_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG199_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG199_IN_SEL_msb, self.__GPIO_SIG199_IN_SEL_lsb)
    @GPIO_SIG199_IN_SEL.setter
    def GPIO_SIG199_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG199_IN_SEL_msb, self.__GPIO_SIG199_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC199_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC199_IN_INV_SEL_msb, self.__GPIO_FUNC199_IN_INV_SEL_lsb)
    @GPIO_FUNC199_IN_INV_SEL.setter
    def GPIO_FUNC199_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC199_IN_INV_SEL_msb, self.__GPIO_FUNC199_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC199_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC199_IN_SEL_msb, self.__GPIO_FUNC199_IN_SEL_lsb)
    @GPIO_FUNC199_IN_SEL.setter
    def GPIO_FUNC199_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC199_IN_SEL_msb, self.__GPIO_FUNC199_IN_SEL_lsb, value)
class GPIO_FUNC200_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x450
        self.__GPIO_SIG200_IN_SEL_lsb = 7
        self.__GPIO_SIG200_IN_SEL_msb = 7
        self.__GPIO_FUNC200_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC200_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC200_IN_SEL_lsb = 0
        self.__GPIO_FUNC200_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG200_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG200_IN_SEL_msb, self.__GPIO_SIG200_IN_SEL_lsb)
    @GPIO_SIG200_IN_SEL.setter
    def GPIO_SIG200_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG200_IN_SEL_msb, self.__GPIO_SIG200_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC200_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC200_IN_INV_SEL_msb, self.__GPIO_FUNC200_IN_INV_SEL_lsb)
    @GPIO_FUNC200_IN_INV_SEL.setter
    def GPIO_FUNC200_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC200_IN_INV_SEL_msb, self.__GPIO_FUNC200_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC200_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC200_IN_SEL_msb, self.__GPIO_FUNC200_IN_SEL_lsb)
    @GPIO_FUNC200_IN_SEL.setter
    def GPIO_FUNC200_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC200_IN_SEL_msb, self.__GPIO_FUNC200_IN_SEL_lsb, value)
class GPIO_FUNC201_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x454
        self.__GPIO_SIG201_IN_SEL_lsb = 7
        self.__GPIO_SIG201_IN_SEL_msb = 7
        self.__GPIO_FUNC201_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC201_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC201_IN_SEL_lsb = 0
        self.__GPIO_FUNC201_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG201_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG201_IN_SEL_msb, self.__GPIO_SIG201_IN_SEL_lsb)
    @GPIO_SIG201_IN_SEL.setter
    def GPIO_SIG201_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG201_IN_SEL_msb, self.__GPIO_SIG201_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC201_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC201_IN_INV_SEL_msb, self.__GPIO_FUNC201_IN_INV_SEL_lsb)
    @GPIO_FUNC201_IN_INV_SEL.setter
    def GPIO_FUNC201_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC201_IN_INV_SEL_msb, self.__GPIO_FUNC201_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC201_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC201_IN_SEL_msb, self.__GPIO_FUNC201_IN_SEL_lsb)
    @GPIO_FUNC201_IN_SEL.setter
    def GPIO_FUNC201_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC201_IN_SEL_msb, self.__GPIO_FUNC201_IN_SEL_lsb, value)
class GPIO_FUNC202_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x458
        self.__GPIO_SIG202_IN_SEL_lsb = 7
        self.__GPIO_SIG202_IN_SEL_msb = 7
        self.__GPIO_FUNC202_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC202_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC202_IN_SEL_lsb = 0
        self.__GPIO_FUNC202_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG202_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG202_IN_SEL_msb, self.__GPIO_SIG202_IN_SEL_lsb)
    @GPIO_SIG202_IN_SEL.setter
    def GPIO_SIG202_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG202_IN_SEL_msb, self.__GPIO_SIG202_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC202_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC202_IN_INV_SEL_msb, self.__GPIO_FUNC202_IN_INV_SEL_lsb)
    @GPIO_FUNC202_IN_INV_SEL.setter
    def GPIO_FUNC202_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC202_IN_INV_SEL_msb, self.__GPIO_FUNC202_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC202_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC202_IN_SEL_msb, self.__GPIO_FUNC202_IN_SEL_lsb)
    @GPIO_FUNC202_IN_SEL.setter
    def GPIO_FUNC202_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC202_IN_SEL_msb, self.__GPIO_FUNC202_IN_SEL_lsb, value)
class GPIO_FUNC203_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x45c
        self.__GPIO_SIG203_IN_SEL_lsb = 7
        self.__GPIO_SIG203_IN_SEL_msb = 7
        self.__GPIO_FUNC203_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC203_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC203_IN_SEL_lsb = 0
        self.__GPIO_FUNC203_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG203_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG203_IN_SEL_msb, self.__GPIO_SIG203_IN_SEL_lsb)
    @GPIO_SIG203_IN_SEL.setter
    def GPIO_SIG203_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG203_IN_SEL_msb, self.__GPIO_SIG203_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC203_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC203_IN_INV_SEL_msb, self.__GPIO_FUNC203_IN_INV_SEL_lsb)
    @GPIO_FUNC203_IN_INV_SEL.setter
    def GPIO_FUNC203_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC203_IN_INV_SEL_msb, self.__GPIO_FUNC203_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC203_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC203_IN_SEL_msb, self.__GPIO_FUNC203_IN_SEL_lsb)
    @GPIO_FUNC203_IN_SEL.setter
    def GPIO_FUNC203_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC203_IN_SEL_msb, self.__GPIO_FUNC203_IN_SEL_lsb, value)
class GPIO_FUNC204_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x460
        self.__GPIO_SIG204_IN_SEL_lsb = 7
        self.__GPIO_SIG204_IN_SEL_msb = 7
        self.__GPIO_FUNC204_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC204_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC204_IN_SEL_lsb = 0
        self.__GPIO_FUNC204_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG204_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG204_IN_SEL_msb, self.__GPIO_SIG204_IN_SEL_lsb)
    @GPIO_SIG204_IN_SEL.setter
    def GPIO_SIG204_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG204_IN_SEL_msb, self.__GPIO_SIG204_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC204_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC204_IN_INV_SEL_msb, self.__GPIO_FUNC204_IN_INV_SEL_lsb)
    @GPIO_FUNC204_IN_INV_SEL.setter
    def GPIO_FUNC204_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC204_IN_INV_SEL_msb, self.__GPIO_FUNC204_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC204_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC204_IN_SEL_msb, self.__GPIO_FUNC204_IN_SEL_lsb)
    @GPIO_FUNC204_IN_SEL.setter
    def GPIO_FUNC204_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC204_IN_SEL_msb, self.__GPIO_FUNC204_IN_SEL_lsb, value)
class GPIO_FUNC205_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x464
        self.__GPIO_SIG205_IN_SEL_lsb = 7
        self.__GPIO_SIG205_IN_SEL_msb = 7
        self.__GPIO_FUNC205_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC205_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC205_IN_SEL_lsb = 0
        self.__GPIO_FUNC205_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG205_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG205_IN_SEL_msb, self.__GPIO_SIG205_IN_SEL_lsb)
    @GPIO_SIG205_IN_SEL.setter
    def GPIO_SIG205_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG205_IN_SEL_msb, self.__GPIO_SIG205_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC205_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC205_IN_INV_SEL_msb, self.__GPIO_FUNC205_IN_INV_SEL_lsb)
    @GPIO_FUNC205_IN_INV_SEL.setter
    def GPIO_FUNC205_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC205_IN_INV_SEL_msb, self.__GPIO_FUNC205_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC205_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC205_IN_SEL_msb, self.__GPIO_FUNC205_IN_SEL_lsb)
    @GPIO_FUNC205_IN_SEL.setter
    def GPIO_FUNC205_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC205_IN_SEL_msb, self.__GPIO_FUNC205_IN_SEL_lsb, value)
class GPIO_FUNC206_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x468
        self.__GPIO_SIG206_IN_SEL_lsb = 7
        self.__GPIO_SIG206_IN_SEL_msb = 7
        self.__GPIO_FUNC206_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC206_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC206_IN_SEL_lsb = 0
        self.__GPIO_FUNC206_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG206_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG206_IN_SEL_msb, self.__GPIO_SIG206_IN_SEL_lsb)
    @GPIO_SIG206_IN_SEL.setter
    def GPIO_SIG206_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG206_IN_SEL_msb, self.__GPIO_SIG206_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC206_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC206_IN_INV_SEL_msb, self.__GPIO_FUNC206_IN_INV_SEL_lsb)
    @GPIO_FUNC206_IN_INV_SEL.setter
    def GPIO_FUNC206_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC206_IN_INV_SEL_msb, self.__GPIO_FUNC206_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC206_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC206_IN_SEL_msb, self.__GPIO_FUNC206_IN_SEL_lsb)
    @GPIO_FUNC206_IN_SEL.setter
    def GPIO_FUNC206_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC206_IN_SEL_msb, self.__GPIO_FUNC206_IN_SEL_lsb, value)
class GPIO_FUNC207_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x46c
        self.__GPIO_SIG207_IN_SEL_lsb = 7
        self.__GPIO_SIG207_IN_SEL_msb = 7
        self.__GPIO_FUNC207_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC207_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC207_IN_SEL_lsb = 0
        self.__GPIO_FUNC207_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG207_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG207_IN_SEL_msb, self.__GPIO_SIG207_IN_SEL_lsb)
    @GPIO_SIG207_IN_SEL.setter
    def GPIO_SIG207_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG207_IN_SEL_msb, self.__GPIO_SIG207_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC207_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC207_IN_INV_SEL_msb, self.__GPIO_FUNC207_IN_INV_SEL_lsb)
    @GPIO_FUNC207_IN_INV_SEL.setter
    def GPIO_FUNC207_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC207_IN_INV_SEL_msb, self.__GPIO_FUNC207_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC207_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC207_IN_SEL_msb, self.__GPIO_FUNC207_IN_SEL_lsb)
    @GPIO_FUNC207_IN_SEL.setter
    def GPIO_FUNC207_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC207_IN_SEL_msb, self.__GPIO_FUNC207_IN_SEL_lsb, value)
class GPIO_FUNC208_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x470
        self.__GPIO_SIG208_IN_SEL_lsb = 7
        self.__GPIO_SIG208_IN_SEL_msb = 7
        self.__GPIO_FUNC208_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC208_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC208_IN_SEL_lsb = 0
        self.__GPIO_FUNC208_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG208_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG208_IN_SEL_msb, self.__GPIO_SIG208_IN_SEL_lsb)
    @GPIO_SIG208_IN_SEL.setter
    def GPIO_SIG208_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG208_IN_SEL_msb, self.__GPIO_SIG208_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC208_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC208_IN_INV_SEL_msb, self.__GPIO_FUNC208_IN_INV_SEL_lsb)
    @GPIO_FUNC208_IN_INV_SEL.setter
    def GPIO_FUNC208_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC208_IN_INV_SEL_msb, self.__GPIO_FUNC208_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC208_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC208_IN_SEL_msb, self.__GPIO_FUNC208_IN_SEL_lsb)
    @GPIO_FUNC208_IN_SEL.setter
    def GPIO_FUNC208_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC208_IN_SEL_msb, self.__GPIO_FUNC208_IN_SEL_lsb, value)
class GPIO_FUNC209_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x474
        self.__GPIO_SIG209_IN_SEL_lsb = 7
        self.__GPIO_SIG209_IN_SEL_msb = 7
        self.__GPIO_FUNC209_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC209_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC209_IN_SEL_lsb = 0
        self.__GPIO_FUNC209_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG209_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG209_IN_SEL_msb, self.__GPIO_SIG209_IN_SEL_lsb)
    @GPIO_SIG209_IN_SEL.setter
    def GPIO_SIG209_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG209_IN_SEL_msb, self.__GPIO_SIG209_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC209_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC209_IN_INV_SEL_msb, self.__GPIO_FUNC209_IN_INV_SEL_lsb)
    @GPIO_FUNC209_IN_INV_SEL.setter
    def GPIO_FUNC209_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC209_IN_INV_SEL_msb, self.__GPIO_FUNC209_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC209_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC209_IN_SEL_msb, self.__GPIO_FUNC209_IN_SEL_lsb)
    @GPIO_FUNC209_IN_SEL.setter
    def GPIO_FUNC209_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC209_IN_SEL_msb, self.__GPIO_FUNC209_IN_SEL_lsb, value)
class GPIO_FUNC210_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x478
        self.__GPIO_SIG210_IN_SEL_lsb = 7
        self.__GPIO_SIG210_IN_SEL_msb = 7
        self.__GPIO_FUNC210_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC210_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC210_IN_SEL_lsb = 0
        self.__GPIO_FUNC210_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG210_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG210_IN_SEL_msb, self.__GPIO_SIG210_IN_SEL_lsb)
    @GPIO_SIG210_IN_SEL.setter
    def GPIO_SIG210_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG210_IN_SEL_msb, self.__GPIO_SIG210_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC210_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC210_IN_INV_SEL_msb, self.__GPIO_FUNC210_IN_INV_SEL_lsb)
    @GPIO_FUNC210_IN_INV_SEL.setter
    def GPIO_FUNC210_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC210_IN_INV_SEL_msb, self.__GPIO_FUNC210_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC210_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC210_IN_SEL_msb, self.__GPIO_FUNC210_IN_SEL_lsb)
    @GPIO_FUNC210_IN_SEL.setter
    def GPIO_FUNC210_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC210_IN_SEL_msb, self.__GPIO_FUNC210_IN_SEL_lsb, value)
class GPIO_FUNC211_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x47c
        self.__GPIO_SIG211_IN_SEL_lsb = 7
        self.__GPIO_SIG211_IN_SEL_msb = 7
        self.__GPIO_FUNC211_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC211_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC211_IN_SEL_lsb = 0
        self.__GPIO_FUNC211_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG211_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG211_IN_SEL_msb, self.__GPIO_SIG211_IN_SEL_lsb)
    @GPIO_SIG211_IN_SEL.setter
    def GPIO_SIG211_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG211_IN_SEL_msb, self.__GPIO_SIG211_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC211_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC211_IN_INV_SEL_msb, self.__GPIO_FUNC211_IN_INV_SEL_lsb)
    @GPIO_FUNC211_IN_INV_SEL.setter
    def GPIO_FUNC211_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC211_IN_INV_SEL_msb, self.__GPIO_FUNC211_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC211_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC211_IN_SEL_msb, self.__GPIO_FUNC211_IN_SEL_lsb)
    @GPIO_FUNC211_IN_SEL.setter
    def GPIO_FUNC211_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC211_IN_SEL_msb, self.__GPIO_FUNC211_IN_SEL_lsb, value)
class GPIO_FUNC212_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x480
        self.__GPIO_SIG212_IN_SEL_lsb = 7
        self.__GPIO_SIG212_IN_SEL_msb = 7
        self.__GPIO_FUNC212_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC212_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC212_IN_SEL_lsb = 0
        self.__GPIO_FUNC212_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG212_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG212_IN_SEL_msb, self.__GPIO_SIG212_IN_SEL_lsb)
    @GPIO_SIG212_IN_SEL.setter
    def GPIO_SIG212_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG212_IN_SEL_msb, self.__GPIO_SIG212_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC212_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC212_IN_INV_SEL_msb, self.__GPIO_FUNC212_IN_INV_SEL_lsb)
    @GPIO_FUNC212_IN_INV_SEL.setter
    def GPIO_FUNC212_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC212_IN_INV_SEL_msb, self.__GPIO_FUNC212_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC212_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC212_IN_SEL_msb, self.__GPIO_FUNC212_IN_SEL_lsb)
    @GPIO_FUNC212_IN_SEL.setter
    def GPIO_FUNC212_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC212_IN_SEL_msb, self.__GPIO_FUNC212_IN_SEL_lsb, value)
class GPIO_FUNC213_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x484
        self.__GPIO_SIG213_IN_SEL_lsb = 7
        self.__GPIO_SIG213_IN_SEL_msb = 7
        self.__GPIO_FUNC213_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC213_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC213_IN_SEL_lsb = 0
        self.__GPIO_FUNC213_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG213_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG213_IN_SEL_msb, self.__GPIO_SIG213_IN_SEL_lsb)
    @GPIO_SIG213_IN_SEL.setter
    def GPIO_SIG213_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG213_IN_SEL_msb, self.__GPIO_SIG213_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC213_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC213_IN_INV_SEL_msb, self.__GPIO_FUNC213_IN_INV_SEL_lsb)
    @GPIO_FUNC213_IN_INV_SEL.setter
    def GPIO_FUNC213_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC213_IN_INV_SEL_msb, self.__GPIO_FUNC213_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC213_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC213_IN_SEL_msb, self.__GPIO_FUNC213_IN_SEL_lsb)
    @GPIO_FUNC213_IN_SEL.setter
    def GPIO_FUNC213_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC213_IN_SEL_msb, self.__GPIO_FUNC213_IN_SEL_lsb, value)
class GPIO_FUNC214_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x488
        self.__GPIO_SIG214_IN_SEL_lsb = 7
        self.__GPIO_SIG214_IN_SEL_msb = 7
        self.__GPIO_FUNC214_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC214_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC214_IN_SEL_lsb = 0
        self.__GPIO_FUNC214_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG214_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG214_IN_SEL_msb, self.__GPIO_SIG214_IN_SEL_lsb)
    @GPIO_SIG214_IN_SEL.setter
    def GPIO_SIG214_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG214_IN_SEL_msb, self.__GPIO_SIG214_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC214_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC214_IN_INV_SEL_msb, self.__GPIO_FUNC214_IN_INV_SEL_lsb)
    @GPIO_FUNC214_IN_INV_SEL.setter
    def GPIO_FUNC214_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC214_IN_INV_SEL_msb, self.__GPIO_FUNC214_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC214_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC214_IN_SEL_msb, self.__GPIO_FUNC214_IN_SEL_lsb)
    @GPIO_FUNC214_IN_SEL.setter
    def GPIO_FUNC214_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC214_IN_SEL_msb, self.__GPIO_FUNC214_IN_SEL_lsb, value)
class GPIO_FUNC215_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x48c
        self.__GPIO_SIG215_IN_SEL_lsb = 7
        self.__GPIO_SIG215_IN_SEL_msb = 7
        self.__GPIO_FUNC215_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC215_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC215_IN_SEL_lsb = 0
        self.__GPIO_FUNC215_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG215_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG215_IN_SEL_msb, self.__GPIO_SIG215_IN_SEL_lsb)
    @GPIO_SIG215_IN_SEL.setter
    def GPIO_SIG215_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG215_IN_SEL_msb, self.__GPIO_SIG215_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC215_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC215_IN_INV_SEL_msb, self.__GPIO_FUNC215_IN_INV_SEL_lsb)
    @GPIO_FUNC215_IN_INV_SEL.setter
    def GPIO_FUNC215_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC215_IN_INV_SEL_msb, self.__GPIO_FUNC215_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC215_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC215_IN_SEL_msb, self.__GPIO_FUNC215_IN_SEL_lsb)
    @GPIO_FUNC215_IN_SEL.setter
    def GPIO_FUNC215_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC215_IN_SEL_msb, self.__GPIO_FUNC215_IN_SEL_lsb, value)
class GPIO_FUNC216_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x490
        self.__GPIO_SIG216_IN_SEL_lsb = 7
        self.__GPIO_SIG216_IN_SEL_msb = 7
        self.__GPIO_FUNC216_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC216_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC216_IN_SEL_lsb = 0
        self.__GPIO_FUNC216_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG216_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG216_IN_SEL_msb, self.__GPIO_SIG216_IN_SEL_lsb)
    @GPIO_SIG216_IN_SEL.setter
    def GPIO_SIG216_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG216_IN_SEL_msb, self.__GPIO_SIG216_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC216_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC216_IN_INV_SEL_msb, self.__GPIO_FUNC216_IN_INV_SEL_lsb)
    @GPIO_FUNC216_IN_INV_SEL.setter
    def GPIO_FUNC216_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC216_IN_INV_SEL_msb, self.__GPIO_FUNC216_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC216_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC216_IN_SEL_msb, self.__GPIO_FUNC216_IN_SEL_lsb)
    @GPIO_FUNC216_IN_SEL.setter
    def GPIO_FUNC216_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC216_IN_SEL_msb, self.__GPIO_FUNC216_IN_SEL_lsb, value)
class GPIO_FUNC217_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x494
        self.__GPIO_SIG217_IN_SEL_lsb = 7
        self.__GPIO_SIG217_IN_SEL_msb = 7
        self.__GPIO_FUNC217_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC217_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC217_IN_SEL_lsb = 0
        self.__GPIO_FUNC217_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG217_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG217_IN_SEL_msb, self.__GPIO_SIG217_IN_SEL_lsb)
    @GPIO_SIG217_IN_SEL.setter
    def GPIO_SIG217_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG217_IN_SEL_msb, self.__GPIO_SIG217_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC217_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC217_IN_INV_SEL_msb, self.__GPIO_FUNC217_IN_INV_SEL_lsb)
    @GPIO_FUNC217_IN_INV_SEL.setter
    def GPIO_FUNC217_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC217_IN_INV_SEL_msb, self.__GPIO_FUNC217_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC217_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC217_IN_SEL_msb, self.__GPIO_FUNC217_IN_SEL_lsb)
    @GPIO_FUNC217_IN_SEL.setter
    def GPIO_FUNC217_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC217_IN_SEL_msb, self.__GPIO_FUNC217_IN_SEL_lsb, value)
class GPIO_FUNC218_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x498
        self.__GPIO_SIG218_IN_SEL_lsb = 7
        self.__GPIO_SIG218_IN_SEL_msb = 7
        self.__GPIO_FUNC218_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC218_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC218_IN_SEL_lsb = 0
        self.__GPIO_FUNC218_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG218_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG218_IN_SEL_msb, self.__GPIO_SIG218_IN_SEL_lsb)
    @GPIO_SIG218_IN_SEL.setter
    def GPIO_SIG218_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG218_IN_SEL_msb, self.__GPIO_SIG218_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC218_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC218_IN_INV_SEL_msb, self.__GPIO_FUNC218_IN_INV_SEL_lsb)
    @GPIO_FUNC218_IN_INV_SEL.setter
    def GPIO_FUNC218_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC218_IN_INV_SEL_msb, self.__GPIO_FUNC218_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC218_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC218_IN_SEL_msb, self.__GPIO_FUNC218_IN_SEL_lsb)
    @GPIO_FUNC218_IN_SEL.setter
    def GPIO_FUNC218_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC218_IN_SEL_msb, self.__GPIO_FUNC218_IN_SEL_lsb, value)
class GPIO_FUNC219_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x49c
        self.__GPIO_SIG219_IN_SEL_lsb = 7
        self.__GPIO_SIG219_IN_SEL_msb = 7
        self.__GPIO_FUNC219_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC219_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC219_IN_SEL_lsb = 0
        self.__GPIO_FUNC219_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG219_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG219_IN_SEL_msb, self.__GPIO_SIG219_IN_SEL_lsb)
    @GPIO_SIG219_IN_SEL.setter
    def GPIO_SIG219_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG219_IN_SEL_msb, self.__GPIO_SIG219_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC219_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC219_IN_INV_SEL_msb, self.__GPIO_FUNC219_IN_INV_SEL_lsb)
    @GPIO_FUNC219_IN_INV_SEL.setter
    def GPIO_FUNC219_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC219_IN_INV_SEL_msb, self.__GPIO_FUNC219_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC219_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC219_IN_SEL_msb, self.__GPIO_FUNC219_IN_SEL_lsb)
    @GPIO_FUNC219_IN_SEL.setter
    def GPIO_FUNC219_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC219_IN_SEL_msb, self.__GPIO_FUNC219_IN_SEL_lsb, value)
class GPIO_FUNC220_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x4a0
        self.__GPIO_SIG220_IN_SEL_lsb = 7
        self.__GPIO_SIG220_IN_SEL_msb = 7
        self.__GPIO_FUNC220_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC220_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC220_IN_SEL_lsb = 0
        self.__GPIO_FUNC220_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG220_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG220_IN_SEL_msb, self.__GPIO_SIG220_IN_SEL_lsb)
    @GPIO_SIG220_IN_SEL.setter
    def GPIO_SIG220_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG220_IN_SEL_msb, self.__GPIO_SIG220_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC220_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC220_IN_INV_SEL_msb, self.__GPIO_FUNC220_IN_INV_SEL_lsb)
    @GPIO_FUNC220_IN_INV_SEL.setter
    def GPIO_FUNC220_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC220_IN_INV_SEL_msb, self.__GPIO_FUNC220_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC220_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC220_IN_SEL_msb, self.__GPIO_FUNC220_IN_SEL_lsb)
    @GPIO_FUNC220_IN_SEL.setter
    def GPIO_FUNC220_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC220_IN_SEL_msb, self.__GPIO_FUNC220_IN_SEL_lsb, value)
class GPIO_FUNC221_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x4a4
        self.__GPIO_SIG221_IN_SEL_lsb = 7
        self.__GPIO_SIG221_IN_SEL_msb = 7
        self.__GPIO_FUNC221_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC221_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC221_IN_SEL_lsb = 0
        self.__GPIO_FUNC221_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG221_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG221_IN_SEL_msb, self.__GPIO_SIG221_IN_SEL_lsb)
    @GPIO_SIG221_IN_SEL.setter
    def GPIO_SIG221_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG221_IN_SEL_msb, self.__GPIO_SIG221_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC221_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC221_IN_INV_SEL_msb, self.__GPIO_FUNC221_IN_INV_SEL_lsb)
    @GPIO_FUNC221_IN_INV_SEL.setter
    def GPIO_FUNC221_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC221_IN_INV_SEL_msb, self.__GPIO_FUNC221_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC221_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC221_IN_SEL_msb, self.__GPIO_FUNC221_IN_SEL_lsb)
    @GPIO_FUNC221_IN_SEL.setter
    def GPIO_FUNC221_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC221_IN_SEL_msb, self.__GPIO_FUNC221_IN_SEL_lsb, value)
class GPIO_FUNC222_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x4a8
        self.__GPIO_SIG222_IN_SEL_lsb = 7
        self.__GPIO_SIG222_IN_SEL_msb = 7
        self.__GPIO_FUNC222_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC222_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC222_IN_SEL_lsb = 0
        self.__GPIO_FUNC222_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG222_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG222_IN_SEL_msb, self.__GPIO_SIG222_IN_SEL_lsb)
    @GPIO_SIG222_IN_SEL.setter
    def GPIO_SIG222_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG222_IN_SEL_msb, self.__GPIO_SIG222_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC222_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC222_IN_INV_SEL_msb, self.__GPIO_FUNC222_IN_INV_SEL_lsb)
    @GPIO_FUNC222_IN_INV_SEL.setter
    def GPIO_FUNC222_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC222_IN_INV_SEL_msb, self.__GPIO_FUNC222_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC222_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC222_IN_SEL_msb, self.__GPIO_FUNC222_IN_SEL_lsb)
    @GPIO_FUNC222_IN_SEL.setter
    def GPIO_FUNC222_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC222_IN_SEL_msb, self.__GPIO_FUNC222_IN_SEL_lsb, value)
class GPIO_FUNC223_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x4ac
        self.__GPIO_SIG223_IN_SEL_lsb = 7
        self.__GPIO_SIG223_IN_SEL_msb = 7
        self.__GPIO_FUNC223_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC223_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC223_IN_SEL_lsb = 0
        self.__GPIO_FUNC223_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG223_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG223_IN_SEL_msb, self.__GPIO_SIG223_IN_SEL_lsb)
    @GPIO_SIG223_IN_SEL.setter
    def GPIO_SIG223_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG223_IN_SEL_msb, self.__GPIO_SIG223_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC223_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC223_IN_INV_SEL_msb, self.__GPIO_FUNC223_IN_INV_SEL_lsb)
    @GPIO_FUNC223_IN_INV_SEL.setter
    def GPIO_FUNC223_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC223_IN_INV_SEL_msb, self.__GPIO_FUNC223_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC223_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC223_IN_SEL_msb, self.__GPIO_FUNC223_IN_SEL_lsb)
    @GPIO_FUNC223_IN_SEL.setter
    def GPIO_FUNC223_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC223_IN_SEL_msb, self.__GPIO_FUNC223_IN_SEL_lsb, value)
class GPIO_FUNC224_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x4b0
        self.__GPIO_SIG224_IN_SEL_lsb = 7
        self.__GPIO_SIG224_IN_SEL_msb = 7
        self.__GPIO_FUNC224_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC224_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC224_IN_SEL_lsb = 0
        self.__GPIO_FUNC224_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG224_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG224_IN_SEL_msb, self.__GPIO_SIG224_IN_SEL_lsb)
    @GPIO_SIG224_IN_SEL.setter
    def GPIO_SIG224_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG224_IN_SEL_msb, self.__GPIO_SIG224_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC224_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC224_IN_INV_SEL_msb, self.__GPIO_FUNC224_IN_INV_SEL_lsb)
    @GPIO_FUNC224_IN_INV_SEL.setter
    def GPIO_FUNC224_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC224_IN_INV_SEL_msb, self.__GPIO_FUNC224_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC224_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC224_IN_SEL_msb, self.__GPIO_FUNC224_IN_SEL_lsb)
    @GPIO_FUNC224_IN_SEL.setter
    def GPIO_FUNC224_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC224_IN_SEL_msb, self.__GPIO_FUNC224_IN_SEL_lsb, value)
class GPIO_FUNC225_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x4b4
        self.__GPIO_SIG225_IN_SEL_lsb = 7
        self.__GPIO_SIG225_IN_SEL_msb = 7
        self.__GPIO_FUNC225_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC225_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC225_IN_SEL_lsb = 0
        self.__GPIO_FUNC225_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG225_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG225_IN_SEL_msb, self.__GPIO_SIG225_IN_SEL_lsb)
    @GPIO_SIG225_IN_SEL.setter
    def GPIO_SIG225_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG225_IN_SEL_msb, self.__GPIO_SIG225_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC225_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC225_IN_INV_SEL_msb, self.__GPIO_FUNC225_IN_INV_SEL_lsb)
    @GPIO_FUNC225_IN_INV_SEL.setter
    def GPIO_FUNC225_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC225_IN_INV_SEL_msb, self.__GPIO_FUNC225_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC225_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC225_IN_SEL_msb, self.__GPIO_FUNC225_IN_SEL_lsb)
    @GPIO_FUNC225_IN_SEL.setter
    def GPIO_FUNC225_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC225_IN_SEL_msb, self.__GPIO_FUNC225_IN_SEL_lsb, value)
class GPIO_FUNC226_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x4b8
        self.__GPIO_SIG226_IN_SEL_lsb = 7
        self.__GPIO_SIG226_IN_SEL_msb = 7
        self.__GPIO_FUNC226_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC226_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC226_IN_SEL_lsb = 0
        self.__GPIO_FUNC226_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG226_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG226_IN_SEL_msb, self.__GPIO_SIG226_IN_SEL_lsb)
    @GPIO_SIG226_IN_SEL.setter
    def GPIO_SIG226_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG226_IN_SEL_msb, self.__GPIO_SIG226_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC226_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC226_IN_INV_SEL_msb, self.__GPIO_FUNC226_IN_INV_SEL_lsb)
    @GPIO_FUNC226_IN_INV_SEL.setter
    def GPIO_FUNC226_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC226_IN_INV_SEL_msb, self.__GPIO_FUNC226_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC226_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC226_IN_SEL_msb, self.__GPIO_FUNC226_IN_SEL_lsb)
    @GPIO_FUNC226_IN_SEL.setter
    def GPIO_FUNC226_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC226_IN_SEL_msb, self.__GPIO_FUNC226_IN_SEL_lsb, value)
class GPIO_FUNC227_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x4bc
        self.__GPIO_SIG227_IN_SEL_lsb = 7
        self.__GPIO_SIG227_IN_SEL_msb = 7
        self.__GPIO_FUNC227_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC227_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC227_IN_SEL_lsb = 0
        self.__GPIO_FUNC227_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG227_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG227_IN_SEL_msb, self.__GPIO_SIG227_IN_SEL_lsb)
    @GPIO_SIG227_IN_SEL.setter
    def GPIO_SIG227_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG227_IN_SEL_msb, self.__GPIO_SIG227_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC227_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC227_IN_INV_SEL_msb, self.__GPIO_FUNC227_IN_INV_SEL_lsb)
    @GPIO_FUNC227_IN_INV_SEL.setter
    def GPIO_FUNC227_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC227_IN_INV_SEL_msb, self.__GPIO_FUNC227_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC227_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC227_IN_SEL_msb, self.__GPIO_FUNC227_IN_SEL_lsb)
    @GPIO_FUNC227_IN_SEL.setter
    def GPIO_FUNC227_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC227_IN_SEL_msb, self.__GPIO_FUNC227_IN_SEL_lsb, value)
class GPIO_FUNC228_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x4c0
        self.__GPIO_SIG228_IN_SEL_lsb = 7
        self.__GPIO_SIG228_IN_SEL_msb = 7
        self.__GPIO_FUNC228_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC228_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC228_IN_SEL_lsb = 0
        self.__GPIO_FUNC228_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG228_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG228_IN_SEL_msb, self.__GPIO_SIG228_IN_SEL_lsb)
    @GPIO_SIG228_IN_SEL.setter
    def GPIO_SIG228_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG228_IN_SEL_msb, self.__GPIO_SIG228_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC228_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC228_IN_INV_SEL_msb, self.__GPIO_FUNC228_IN_INV_SEL_lsb)
    @GPIO_FUNC228_IN_INV_SEL.setter
    def GPIO_FUNC228_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC228_IN_INV_SEL_msb, self.__GPIO_FUNC228_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC228_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC228_IN_SEL_msb, self.__GPIO_FUNC228_IN_SEL_lsb)
    @GPIO_FUNC228_IN_SEL.setter
    def GPIO_FUNC228_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC228_IN_SEL_msb, self.__GPIO_FUNC228_IN_SEL_lsb, value)
class GPIO_FUNC229_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x4c4
        self.__GPIO_SIG229_IN_SEL_lsb = 7
        self.__GPIO_SIG229_IN_SEL_msb = 7
        self.__GPIO_FUNC229_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC229_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC229_IN_SEL_lsb = 0
        self.__GPIO_FUNC229_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG229_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG229_IN_SEL_msb, self.__GPIO_SIG229_IN_SEL_lsb)
    @GPIO_SIG229_IN_SEL.setter
    def GPIO_SIG229_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG229_IN_SEL_msb, self.__GPIO_SIG229_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC229_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC229_IN_INV_SEL_msb, self.__GPIO_FUNC229_IN_INV_SEL_lsb)
    @GPIO_FUNC229_IN_INV_SEL.setter
    def GPIO_FUNC229_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC229_IN_INV_SEL_msb, self.__GPIO_FUNC229_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC229_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC229_IN_SEL_msb, self.__GPIO_FUNC229_IN_SEL_lsb)
    @GPIO_FUNC229_IN_SEL.setter
    def GPIO_FUNC229_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC229_IN_SEL_msb, self.__GPIO_FUNC229_IN_SEL_lsb, value)
class GPIO_FUNC230_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x4c8
        self.__GPIO_SIG230_IN_SEL_lsb = 7
        self.__GPIO_SIG230_IN_SEL_msb = 7
        self.__GPIO_FUNC230_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC230_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC230_IN_SEL_lsb = 0
        self.__GPIO_FUNC230_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG230_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG230_IN_SEL_msb, self.__GPIO_SIG230_IN_SEL_lsb)
    @GPIO_SIG230_IN_SEL.setter
    def GPIO_SIG230_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG230_IN_SEL_msb, self.__GPIO_SIG230_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC230_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC230_IN_INV_SEL_msb, self.__GPIO_FUNC230_IN_INV_SEL_lsb)
    @GPIO_FUNC230_IN_INV_SEL.setter
    def GPIO_FUNC230_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC230_IN_INV_SEL_msb, self.__GPIO_FUNC230_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC230_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC230_IN_SEL_msb, self.__GPIO_FUNC230_IN_SEL_lsb)
    @GPIO_FUNC230_IN_SEL.setter
    def GPIO_FUNC230_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC230_IN_SEL_msb, self.__GPIO_FUNC230_IN_SEL_lsb, value)
class GPIO_FUNC231_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x4cc
        self.__GPIO_SIG231_IN_SEL_lsb = 7
        self.__GPIO_SIG231_IN_SEL_msb = 7
        self.__GPIO_FUNC231_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC231_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC231_IN_SEL_lsb = 0
        self.__GPIO_FUNC231_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG231_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG231_IN_SEL_msb, self.__GPIO_SIG231_IN_SEL_lsb)
    @GPIO_SIG231_IN_SEL.setter
    def GPIO_SIG231_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG231_IN_SEL_msb, self.__GPIO_SIG231_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC231_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC231_IN_INV_SEL_msb, self.__GPIO_FUNC231_IN_INV_SEL_lsb)
    @GPIO_FUNC231_IN_INV_SEL.setter
    def GPIO_FUNC231_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC231_IN_INV_SEL_msb, self.__GPIO_FUNC231_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC231_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC231_IN_SEL_msb, self.__GPIO_FUNC231_IN_SEL_lsb)
    @GPIO_FUNC231_IN_SEL.setter
    def GPIO_FUNC231_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC231_IN_SEL_msb, self.__GPIO_FUNC231_IN_SEL_lsb, value)
class GPIO_FUNC232_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x4d0
        self.__GPIO_SIG232_IN_SEL_lsb = 7
        self.__GPIO_SIG232_IN_SEL_msb = 7
        self.__GPIO_FUNC232_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC232_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC232_IN_SEL_lsb = 0
        self.__GPIO_FUNC232_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG232_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG232_IN_SEL_msb, self.__GPIO_SIG232_IN_SEL_lsb)
    @GPIO_SIG232_IN_SEL.setter
    def GPIO_SIG232_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG232_IN_SEL_msb, self.__GPIO_SIG232_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC232_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC232_IN_INV_SEL_msb, self.__GPIO_FUNC232_IN_INV_SEL_lsb)
    @GPIO_FUNC232_IN_INV_SEL.setter
    def GPIO_FUNC232_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC232_IN_INV_SEL_msb, self.__GPIO_FUNC232_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC232_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC232_IN_SEL_msb, self.__GPIO_FUNC232_IN_SEL_lsb)
    @GPIO_FUNC232_IN_SEL.setter
    def GPIO_FUNC232_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC232_IN_SEL_msb, self.__GPIO_FUNC232_IN_SEL_lsb, value)
class GPIO_FUNC233_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x4d4
        self.__GPIO_SIG233_IN_SEL_lsb = 7
        self.__GPIO_SIG233_IN_SEL_msb = 7
        self.__GPIO_FUNC233_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC233_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC233_IN_SEL_lsb = 0
        self.__GPIO_FUNC233_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG233_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG233_IN_SEL_msb, self.__GPIO_SIG233_IN_SEL_lsb)
    @GPIO_SIG233_IN_SEL.setter
    def GPIO_SIG233_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG233_IN_SEL_msb, self.__GPIO_SIG233_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC233_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC233_IN_INV_SEL_msb, self.__GPIO_FUNC233_IN_INV_SEL_lsb)
    @GPIO_FUNC233_IN_INV_SEL.setter
    def GPIO_FUNC233_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC233_IN_INV_SEL_msb, self.__GPIO_FUNC233_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC233_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC233_IN_SEL_msb, self.__GPIO_FUNC233_IN_SEL_lsb)
    @GPIO_FUNC233_IN_SEL.setter
    def GPIO_FUNC233_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC233_IN_SEL_msb, self.__GPIO_FUNC233_IN_SEL_lsb, value)
class GPIO_FUNC234_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x4d8
        self.__GPIO_SIG234_IN_SEL_lsb = 7
        self.__GPIO_SIG234_IN_SEL_msb = 7
        self.__GPIO_FUNC234_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC234_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC234_IN_SEL_lsb = 0
        self.__GPIO_FUNC234_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG234_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG234_IN_SEL_msb, self.__GPIO_SIG234_IN_SEL_lsb)
    @GPIO_SIG234_IN_SEL.setter
    def GPIO_SIG234_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG234_IN_SEL_msb, self.__GPIO_SIG234_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC234_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC234_IN_INV_SEL_msb, self.__GPIO_FUNC234_IN_INV_SEL_lsb)
    @GPIO_FUNC234_IN_INV_SEL.setter
    def GPIO_FUNC234_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC234_IN_INV_SEL_msb, self.__GPIO_FUNC234_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC234_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC234_IN_SEL_msb, self.__GPIO_FUNC234_IN_SEL_lsb)
    @GPIO_FUNC234_IN_SEL.setter
    def GPIO_FUNC234_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC234_IN_SEL_msb, self.__GPIO_FUNC234_IN_SEL_lsb, value)
class GPIO_FUNC235_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x4dc
        self.__GPIO_SIG235_IN_SEL_lsb = 7
        self.__GPIO_SIG235_IN_SEL_msb = 7
        self.__GPIO_FUNC235_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC235_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC235_IN_SEL_lsb = 0
        self.__GPIO_FUNC235_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG235_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG235_IN_SEL_msb, self.__GPIO_SIG235_IN_SEL_lsb)
    @GPIO_SIG235_IN_SEL.setter
    def GPIO_SIG235_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG235_IN_SEL_msb, self.__GPIO_SIG235_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC235_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC235_IN_INV_SEL_msb, self.__GPIO_FUNC235_IN_INV_SEL_lsb)
    @GPIO_FUNC235_IN_INV_SEL.setter
    def GPIO_FUNC235_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC235_IN_INV_SEL_msb, self.__GPIO_FUNC235_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC235_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC235_IN_SEL_msb, self.__GPIO_FUNC235_IN_SEL_lsb)
    @GPIO_FUNC235_IN_SEL.setter
    def GPIO_FUNC235_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC235_IN_SEL_msb, self.__GPIO_FUNC235_IN_SEL_lsb, value)
class GPIO_FUNC236_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x4e0
        self.__GPIO_SIG236_IN_SEL_lsb = 7
        self.__GPIO_SIG236_IN_SEL_msb = 7
        self.__GPIO_FUNC236_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC236_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC236_IN_SEL_lsb = 0
        self.__GPIO_FUNC236_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG236_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG236_IN_SEL_msb, self.__GPIO_SIG236_IN_SEL_lsb)
    @GPIO_SIG236_IN_SEL.setter
    def GPIO_SIG236_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG236_IN_SEL_msb, self.__GPIO_SIG236_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC236_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC236_IN_INV_SEL_msb, self.__GPIO_FUNC236_IN_INV_SEL_lsb)
    @GPIO_FUNC236_IN_INV_SEL.setter
    def GPIO_FUNC236_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC236_IN_INV_SEL_msb, self.__GPIO_FUNC236_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC236_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC236_IN_SEL_msb, self.__GPIO_FUNC236_IN_SEL_lsb)
    @GPIO_FUNC236_IN_SEL.setter
    def GPIO_FUNC236_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC236_IN_SEL_msb, self.__GPIO_FUNC236_IN_SEL_lsb, value)
class GPIO_FUNC237_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x4e4
        self.__GPIO_SIG237_IN_SEL_lsb = 7
        self.__GPIO_SIG237_IN_SEL_msb = 7
        self.__GPIO_FUNC237_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC237_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC237_IN_SEL_lsb = 0
        self.__GPIO_FUNC237_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG237_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG237_IN_SEL_msb, self.__GPIO_SIG237_IN_SEL_lsb)
    @GPIO_SIG237_IN_SEL.setter
    def GPIO_SIG237_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG237_IN_SEL_msb, self.__GPIO_SIG237_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC237_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC237_IN_INV_SEL_msb, self.__GPIO_FUNC237_IN_INV_SEL_lsb)
    @GPIO_FUNC237_IN_INV_SEL.setter
    def GPIO_FUNC237_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC237_IN_INV_SEL_msb, self.__GPIO_FUNC237_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC237_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC237_IN_SEL_msb, self.__GPIO_FUNC237_IN_SEL_lsb)
    @GPIO_FUNC237_IN_SEL.setter
    def GPIO_FUNC237_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC237_IN_SEL_msb, self.__GPIO_FUNC237_IN_SEL_lsb, value)
class GPIO_FUNC238_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x4e8
        self.__GPIO_SIG238_IN_SEL_lsb = 7
        self.__GPIO_SIG238_IN_SEL_msb = 7
        self.__GPIO_FUNC238_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC238_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC238_IN_SEL_lsb = 0
        self.__GPIO_FUNC238_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG238_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG238_IN_SEL_msb, self.__GPIO_SIG238_IN_SEL_lsb)
    @GPIO_SIG238_IN_SEL.setter
    def GPIO_SIG238_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG238_IN_SEL_msb, self.__GPIO_SIG238_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC238_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC238_IN_INV_SEL_msb, self.__GPIO_FUNC238_IN_INV_SEL_lsb)
    @GPIO_FUNC238_IN_INV_SEL.setter
    def GPIO_FUNC238_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC238_IN_INV_SEL_msb, self.__GPIO_FUNC238_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC238_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC238_IN_SEL_msb, self.__GPIO_FUNC238_IN_SEL_lsb)
    @GPIO_FUNC238_IN_SEL.setter
    def GPIO_FUNC238_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC238_IN_SEL_msb, self.__GPIO_FUNC238_IN_SEL_lsb, value)
class GPIO_FUNC239_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x4ec
        self.__GPIO_SIG239_IN_SEL_lsb = 7
        self.__GPIO_SIG239_IN_SEL_msb = 7
        self.__GPIO_FUNC239_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC239_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC239_IN_SEL_lsb = 0
        self.__GPIO_FUNC239_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG239_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG239_IN_SEL_msb, self.__GPIO_SIG239_IN_SEL_lsb)
    @GPIO_SIG239_IN_SEL.setter
    def GPIO_SIG239_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG239_IN_SEL_msb, self.__GPIO_SIG239_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC239_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC239_IN_INV_SEL_msb, self.__GPIO_FUNC239_IN_INV_SEL_lsb)
    @GPIO_FUNC239_IN_INV_SEL.setter
    def GPIO_FUNC239_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC239_IN_INV_SEL_msb, self.__GPIO_FUNC239_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC239_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC239_IN_SEL_msb, self.__GPIO_FUNC239_IN_SEL_lsb)
    @GPIO_FUNC239_IN_SEL.setter
    def GPIO_FUNC239_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC239_IN_SEL_msb, self.__GPIO_FUNC239_IN_SEL_lsb, value)
class GPIO_FUNC240_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x4f0
        self.__GPIO_SIG240_IN_SEL_lsb = 7
        self.__GPIO_SIG240_IN_SEL_msb = 7
        self.__GPIO_FUNC240_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC240_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC240_IN_SEL_lsb = 0
        self.__GPIO_FUNC240_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG240_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG240_IN_SEL_msb, self.__GPIO_SIG240_IN_SEL_lsb)
    @GPIO_SIG240_IN_SEL.setter
    def GPIO_SIG240_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG240_IN_SEL_msb, self.__GPIO_SIG240_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC240_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC240_IN_INV_SEL_msb, self.__GPIO_FUNC240_IN_INV_SEL_lsb)
    @GPIO_FUNC240_IN_INV_SEL.setter
    def GPIO_FUNC240_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC240_IN_INV_SEL_msb, self.__GPIO_FUNC240_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC240_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC240_IN_SEL_msb, self.__GPIO_FUNC240_IN_SEL_lsb)
    @GPIO_FUNC240_IN_SEL.setter
    def GPIO_FUNC240_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC240_IN_SEL_msb, self.__GPIO_FUNC240_IN_SEL_lsb, value)
class GPIO_FUNC241_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x4f4
        self.__GPIO_SIG241_IN_SEL_lsb = 7
        self.__GPIO_SIG241_IN_SEL_msb = 7
        self.__GPIO_FUNC241_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC241_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC241_IN_SEL_lsb = 0
        self.__GPIO_FUNC241_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG241_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG241_IN_SEL_msb, self.__GPIO_SIG241_IN_SEL_lsb)
    @GPIO_SIG241_IN_SEL.setter
    def GPIO_SIG241_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG241_IN_SEL_msb, self.__GPIO_SIG241_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC241_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC241_IN_INV_SEL_msb, self.__GPIO_FUNC241_IN_INV_SEL_lsb)
    @GPIO_FUNC241_IN_INV_SEL.setter
    def GPIO_FUNC241_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC241_IN_INV_SEL_msb, self.__GPIO_FUNC241_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC241_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC241_IN_SEL_msb, self.__GPIO_FUNC241_IN_SEL_lsb)
    @GPIO_FUNC241_IN_SEL.setter
    def GPIO_FUNC241_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC241_IN_SEL_msb, self.__GPIO_FUNC241_IN_SEL_lsb, value)
class GPIO_FUNC242_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x4f8
        self.__GPIO_SIG242_IN_SEL_lsb = 7
        self.__GPIO_SIG242_IN_SEL_msb = 7
        self.__GPIO_FUNC242_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC242_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC242_IN_SEL_lsb = 0
        self.__GPIO_FUNC242_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG242_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG242_IN_SEL_msb, self.__GPIO_SIG242_IN_SEL_lsb)
    @GPIO_SIG242_IN_SEL.setter
    def GPIO_SIG242_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG242_IN_SEL_msb, self.__GPIO_SIG242_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC242_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC242_IN_INV_SEL_msb, self.__GPIO_FUNC242_IN_INV_SEL_lsb)
    @GPIO_FUNC242_IN_INV_SEL.setter
    def GPIO_FUNC242_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC242_IN_INV_SEL_msb, self.__GPIO_FUNC242_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC242_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC242_IN_SEL_msb, self.__GPIO_FUNC242_IN_SEL_lsb)
    @GPIO_FUNC242_IN_SEL.setter
    def GPIO_FUNC242_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC242_IN_SEL_msb, self.__GPIO_FUNC242_IN_SEL_lsb, value)
class GPIO_FUNC243_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x4fc
        self.__GPIO_SIG243_IN_SEL_lsb = 7
        self.__GPIO_SIG243_IN_SEL_msb = 7
        self.__GPIO_FUNC243_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC243_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC243_IN_SEL_lsb = 0
        self.__GPIO_FUNC243_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG243_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG243_IN_SEL_msb, self.__GPIO_SIG243_IN_SEL_lsb)
    @GPIO_SIG243_IN_SEL.setter
    def GPIO_SIG243_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG243_IN_SEL_msb, self.__GPIO_SIG243_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC243_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC243_IN_INV_SEL_msb, self.__GPIO_FUNC243_IN_INV_SEL_lsb)
    @GPIO_FUNC243_IN_INV_SEL.setter
    def GPIO_FUNC243_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC243_IN_INV_SEL_msb, self.__GPIO_FUNC243_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC243_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC243_IN_SEL_msb, self.__GPIO_FUNC243_IN_SEL_lsb)
    @GPIO_FUNC243_IN_SEL.setter
    def GPIO_FUNC243_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC243_IN_SEL_msb, self.__GPIO_FUNC243_IN_SEL_lsb, value)
class GPIO_FUNC244_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x500
        self.__GPIO_SIG244_IN_SEL_lsb = 7
        self.__GPIO_SIG244_IN_SEL_msb = 7
        self.__GPIO_FUNC244_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC244_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC244_IN_SEL_lsb = 0
        self.__GPIO_FUNC244_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG244_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG244_IN_SEL_msb, self.__GPIO_SIG244_IN_SEL_lsb)
    @GPIO_SIG244_IN_SEL.setter
    def GPIO_SIG244_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG244_IN_SEL_msb, self.__GPIO_SIG244_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC244_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC244_IN_INV_SEL_msb, self.__GPIO_FUNC244_IN_INV_SEL_lsb)
    @GPIO_FUNC244_IN_INV_SEL.setter
    def GPIO_FUNC244_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC244_IN_INV_SEL_msb, self.__GPIO_FUNC244_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC244_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC244_IN_SEL_msb, self.__GPIO_FUNC244_IN_SEL_lsb)
    @GPIO_FUNC244_IN_SEL.setter
    def GPIO_FUNC244_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC244_IN_SEL_msb, self.__GPIO_FUNC244_IN_SEL_lsb, value)
class GPIO_FUNC245_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x504
        self.__GPIO_SIG245_IN_SEL_lsb = 7
        self.__GPIO_SIG245_IN_SEL_msb = 7
        self.__GPIO_FUNC245_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC245_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC245_IN_SEL_lsb = 0
        self.__GPIO_FUNC245_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG245_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG245_IN_SEL_msb, self.__GPIO_SIG245_IN_SEL_lsb)
    @GPIO_SIG245_IN_SEL.setter
    def GPIO_SIG245_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG245_IN_SEL_msb, self.__GPIO_SIG245_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC245_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC245_IN_INV_SEL_msb, self.__GPIO_FUNC245_IN_INV_SEL_lsb)
    @GPIO_FUNC245_IN_INV_SEL.setter
    def GPIO_FUNC245_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC245_IN_INV_SEL_msb, self.__GPIO_FUNC245_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC245_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC245_IN_SEL_msb, self.__GPIO_FUNC245_IN_SEL_lsb)
    @GPIO_FUNC245_IN_SEL.setter
    def GPIO_FUNC245_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC245_IN_SEL_msb, self.__GPIO_FUNC245_IN_SEL_lsb, value)
class GPIO_FUNC246_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x508
        self.__GPIO_SIG246_IN_SEL_lsb = 7
        self.__GPIO_SIG246_IN_SEL_msb = 7
        self.__GPIO_FUNC246_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC246_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC246_IN_SEL_lsb = 0
        self.__GPIO_FUNC246_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG246_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG246_IN_SEL_msb, self.__GPIO_SIG246_IN_SEL_lsb)
    @GPIO_SIG246_IN_SEL.setter
    def GPIO_SIG246_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG246_IN_SEL_msb, self.__GPIO_SIG246_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC246_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC246_IN_INV_SEL_msb, self.__GPIO_FUNC246_IN_INV_SEL_lsb)
    @GPIO_FUNC246_IN_INV_SEL.setter
    def GPIO_FUNC246_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC246_IN_INV_SEL_msb, self.__GPIO_FUNC246_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC246_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC246_IN_SEL_msb, self.__GPIO_FUNC246_IN_SEL_lsb)
    @GPIO_FUNC246_IN_SEL.setter
    def GPIO_FUNC246_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC246_IN_SEL_msb, self.__GPIO_FUNC246_IN_SEL_lsb, value)
class GPIO_FUNC247_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x50c
        self.__GPIO_SIG247_IN_SEL_lsb = 7
        self.__GPIO_SIG247_IN_SEL_msb = 7
        self.__GPIO_FUNC247_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC247_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC247_IN_SEL_lsb = 0
        self.__GPIO_FUNC247_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG247_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG247_IN_SEL_msb, self.__GPIO_SIG247_IN_SEL_lsb)
    @GPIO_SIG247_IN_SEL.setter
    def GPIO_SIG247_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG247_IN_SEL_msb, self.__GPIO_SIG247_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC247_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC247_IN_INV_SEL_msb, self.__GPIO_FUNC247_IN_INV_SEL_lsb)
    @GPIO_FUNC247_IN_INV_SEL.setter
    def GPIO_FUNC247_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC247_IN_INV_SEL_msb, self.__GPIO_FUNC247_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC247_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC247_IN_SEL_msb, self.__GPIO_FUNC247_IN_SEL_lsb)
    @GPIO_FUNC247_IN_SEL.setter
    def GPIO_FUNC247_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC247_IN_SEL_msb, self.__GPIO_FUNC247_IN_SEL_lsb, value)
class GPIO_FUNC248_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x510
        self.__GPIO_SIG248_IN_SEL_lsb = 7
        self.__GPIO_SIG248_IN_SEL_msb = 7
        self.__GPIO_FUNC248_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC248_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC248_IN_SEL_lsb = 0
        self.__GPIO_FUNC248_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG248_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG248_IN_SEL_msb, self.__GPIO_SIG248_IN_SEL_lsb)
    @GPIO_SIG248_IN_SEL.setter
    def GPIO_SIG248_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG248_IN_SEL_msb, self.__GPIO_SIG248_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC248_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC248_IN_INV_SEL_msb, self.__GPIO_FUNC248_IN_INV_SEL_lsb)
    @GPIO_FUNC248_IN_INV_SEL.setter
    def GPIO_FUNC248_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC248_IN_INV_SEL_msb, self.__GPIO_FUNC248_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC248_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC248_IN_SEL_msb, self.__GPIO_FUNC248_IN_SEL_lsb)
    @GPIO_FUNC248_IN_SEL.setter
    def GPIO_FUNC248_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC248_IN_SEL_msb, self.__GPIO_FUNC248_IN_SEL_lsb, value)
class GPIO_FUNC249_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x514
        self.__GPIO_SIG249_IN_SEL_lsb = 7
        self.__GPIO_SIG249_IN_SEL_msb = 7
        self.__GPIO_FUNC249_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC249_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC249_IN_SEL_lsb = 0
        self.__GPIO_FUNC249_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG249_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG249_IN_SEL_msb, self.__GPIO_SIG249_IN_SEL_lsb)
    @GPIO_SIG249_IN_SEL.setter
    def GPIO_SIG249_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG249_IN_SEL_msb, self.__GPIO_SIG249_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC249_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC249_IN_INV_SEL_msb, self.__GPIO_FUNC249_IN_INV_SEL_lsb)
    @GPIO_FUNC249_IN_INV_SEL.setter
    def GPIO_FUNC249_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC249_IN_INV_SEL_msb, self.__GPIO_FUNC249_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC249_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC249_IN_SEL_msb, self.__GPIO_FUNC249_IN_SEL_lsb)
    @GPIO_FUNC249_IN_SEL.setter
    def GPIO_FUNC249_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC249_IN_SEL_msb, self.__GPIO_FUNC249_IN_SEL_lsb, value)
class GPIO_FUNC250_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x518
        self.__GPIO_SIG250_IN_SEL_lsb = 7
        self.__GPIO_SIG250_IN_SEL_msb = 7
        self.__GPIO_FUNC250_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC250_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC250_IN_SEL_lsb = 0
        self.__GPIO_FUNC250_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG250_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG250_IN_SEL_msb, self.__GPIO_SIG250_IN_SEL_lsb)
    @GPIO_SIG250_IN_SEL.setter
    def GPIO_SIG250_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG250_IN_SEL_msb, self.__GPIO_SIG250_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC250_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC250_IN_INV_SEL_msb, self.__GPIO_FUNC250_IN_INV_SEL_lsb)
    @GPIO_FUNC250_IN_INV_SEL.setter
    def GPIO_FUNC250_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC250_IN_INV_SEL_msb, self.__GPIO_FUNC250_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC250_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC250_IN_SEL_msb, self.__GPIO_FUNC250_IN_SEL_lsb)
    @GPIO_FUNC250_IN_SEL.setter
    def GPIO_FUNC250_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC250_IN_SEL_msb, self.__GPIO_FUNC250_IN_SEL_lsb, value)
class GPIO_FUNC251_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x51c
        self.__GPIO_SIG251_IN_SEL_lsb = 7
        self.__GPIO_SIG251_IN_SEL_msb = 7
        self.__GPIO_FUNC251_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC251_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC251_IN_SEL_lsb = 0
        self.__GPIO_FUNC251_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG251_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG251_IN_SEL_msb, self.__GPIO_SIG251_IN_SEL_lsb)
    @GPIO_SIG251_IN_SEL.setter
    def GPIO_SIG251_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG251_IN_SEL_msb, self.__GPIO_SIG251_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC251_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC251_IN_INV_SEL_msb, self.__GPIO_FUNC251_IN_INV_SEL_lsb)
    @GPIO_FUNC251_IN_INV_SEL.setter
    def GPIO_FUNC251_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC251_IN_INV_SEL_msb, self.__GPIO_FUNC251_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC251_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC251_IN_SEL_msb, self.__GPIO_FUNC251_IN_SEL_lsb)
    @GPIO_FUNC251_IN_SEL.setter
    def GPIO_FUNC251_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC251_IN_SEL_msb, self.__GPIO_FUNC251_IN_SEL_lsb, value)
class GPIO_FUNC252_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x520
        self.__GPIO_SIG252_IN_SEL_lsb = 7
        self.__GPIO_SIG252_IN_SEL_msb = 7
        self.__GPIO_FUNC252_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC252_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC252_IN_SEL_lsb = 0
        self.__GPIO_FUNC252_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG252_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG252_IN_SEL_msb, self.__GPIO_SIG252_IN_SEL_lsb)
    @GPIO_SIG252_IN_SEL.setter
    def GPIO_SIG252_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG252_IN_SEL_msb, self.__GPIO_SIG252_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC252_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC252_IN_INV_SEL_msb, self.__GPIO_FUNC252_IN_INV_SEL_lsb)
    @GPIO_FUNC252_IN_INV_SEL.setter
    def GPIO_FUNC252_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC252_IN_INV_SEL_msb, self.__GPIO_FUNC252_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC252_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC252_IN_SEL_msb, self.__GPIO_FUNC252_IN_SEL_lsb)
    @GPIO_FUNC252_IN_SEL.setter
    def GPIO_FUNC252_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC252_IN_SEL_msb, self.__GPIO_FUNC252_IN_SEL_lsb, value)
class GPIO_FUNC253_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x524
        self.__GPIO_SIG253_IN_SEL_lsb = 7
        self.__GPIO_SIG253_IN_SEL_msb = 7
        self.__GPIO_FUNC253_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC253_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC253_IN_SEL_lsb = 0
        self.__GPIO_FUNC253_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG253_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG253_IN_SEL_msb, self.__GPIO_SIG253_IN_SEL_lsb)
    @GPIO_SIG253_IN_SEL.setter
    def GPIO_SIG253_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG253_IN_SEL_msb, self.__GPIO_SIG253_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC253_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC253_IN_INV_SEL_msb, self.__GPIO_FUNC253_IN_INV_SEL_lsb)
    @GPIO_FUNC253_IN_INV_SEL.setter
    def GPIO_FUNC253_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC253_IN_INV_SEL_msb, self.__GPIO_FUNC253_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC253_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC253_IN_SEL_msb, self.__GPIO_FUNC253_IN_SEL_lsb)
    @GPIO_FUNC253_IN_SEL.setter
    def GPIO_FUNC253_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC253_IN_SEL_msb, self.__GPIO_FUNC253_IN_SEL_lsb, value)
class GPIO_FUNC254_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x528
        self.__GPIO_SIG254_IN_SEL_lsb = 7
        self.__GPIO_SIG254_IN_SEL_msb = 7
        self.__GPIO_FUNC254_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC254_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC254_IN_SEL_lsb = 0
        self.__GPIO_FUNC254_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG254_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG254_IN_SEL_msb, self.__GPIO_SIG254_IN_SEL_lsb)
    @GPIO_SIG254_IN_SEL.setter
    def GPIO_SIG254_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG254_IN_SEL_msb, self.__GPIO_SIG254_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC254_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC254_IN_INV_SEL_msb, self.__GPIO_FUNC254_IN_INV_SEL_lsb)
    @GPIO_FUNC254_IN_INV_SEL.setter
    def GPIO_FUNC254_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC254_IN_INV_SEL_msb, self.__GPIO_FUNC254_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC254_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC254_IN_SEL_msb, self.__GPIO_FUNC254_IN_SEL_lsb)
    @GPIO_FUNC254_IN_SEL.setter
    def GPIO_FUNC254_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC254_IN_SEL_msb, self.__GPIO_FUNC254_IN_SEL_lsb, value)
class GPIO_FUNC255_IN_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x52c
        self.__GPIO_SIG255_IN_SEL_lsb = 7
        self.__GPIO_SIG255_IN_SEL_msb = 7
        self.__GPIO_FUNC255_IN_INV_SEL_lsb = 6
        self.__GPIO_FUNC255_IN_INV_SEL_msb = 6
        self.__GPIO_FUNC255_IN_SEL_lsb = 0
        self.__GPIO_FUNC255_IN_SEL_msb = 5
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_SIG255_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_SIG255_IN_SEL_msb, self.__GPIO_SIG255_IN_SEL_lsb)
    @GPIO_SIG255_IN_SEL.setter
    def GPIO_SIG255_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_SIG255_IN_SEL_msb, self.__GPIO_SIG255_IN_SEL_lsb, value)

    @property
    def GPIO_FUNC255_IN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC255_IN_INV_SEL_msb, self.__GPIO_FUNC255_IN_INV_SEL_lsb)
    @GPIO_FUNC255_IN_INV_SEL.setter
    def GPIO_FUNC255_IN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC255_IN_INV_SEL_msb, self.__GPIO_FUNC255_IN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC255_IN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC255_IN_SEL_msb, self.__GPIO_FUNC255_IN_SEL_lsb)
    @GPIO_FUNC255_IN_SEL.setter
    def GPIO_FUNC255_IN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC255_IN_SEL_msb, self.__GPIO_FUNC255_IN_SEL_lsb, value)
class GPIO_FUNC0_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x530
        self.__GPIO_FUNC0_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC0_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC0_OEN_SEL_lsb = 10
        self.__GPIO_FUNC0_OEN_SEL_msb = 10
        self.__GPIO_FUNC0_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC0_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC0_OUT_SEL_lsb = 0
        self.__GPIO_FUNC0_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC0_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC0_OEN_INV_SEL_msb, self.__GPIO_FUNC0_OEN_INV_SEL_lsb)
    @GPIO_FUNC0_OEN_INV_SEL.setter
    def GPIO_FUNC0_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC0_OEN_INV_SEL_msb, self.__GPIO_FUNC0_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC0_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC0_OEN_SEL_msb, self.__GPIO_FUNC0_OEN_SEL_lsb)
    @GPIO_FUNC0_OEN_SEL.setter
    def GPIO_FUNC0_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC0_OEN_SEL_msb, self.__GPIO_FUNC0_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC0_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC0_OUT_INV_SEL_msb, self.__GPIO_FUNC0_OUT_INV_SEL_lsb)
    @GPIO_FUNC0_OUT_INV_SEL.setter
    def GPIO_FUNC0_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC0_OUT_INV_SEL_msb, self.__GPIO_FUNC0_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC0_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC0_OUT_SEL_msb, self.__GPIO_FUNC0_OUT_SEL_lsb)
    @GPIO_FUNC0_OUT_SEL.setter
    def GPIO_FUNC0_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC0_OUT_SEL_msb, self.__GPIO_FUNC0_OUT_SEL_lsb, value)
class GPIO_FUNC1_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x534
        self.__GPIO_FUNC1_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC1_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC1_OEN_SEL_lsb = 10
        self.__GPIO_FUNC1_OEN_SEL_msb = 10
        self.__GPIO_FUNC1_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC1_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC1_OUT_SEL_lsb = 0
        self.__GPIO_FUNC1_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC1_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC1_OEN_INV_SEL_msb, self.__GPIO_FUNC1_OEN_INV_SEL_lsb)
    @GPIO_FUNC1_OEN_INV_SEL.setter
    def GPIO_FUNC1_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC1_OEN_INV_SEL_msb, self.__GPIO_FUNC1_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC1_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC1_OEN_SEL_msb, self.__GPIO_FUNC1_OEN_SEL_lsb)
    @GPIO_FUNC1_OEN_SEL.setter
    def GPIO_FUNC1_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC1_OEN_SEL_msb, self.__GPIO_FUNC1_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC1_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC1_OUT_INV_SEL_msb, self.__GPIO_FUNC1_OUT_INV_SEL_lsb)
    @GPIO_FUNC1_OUT_INV_SEL.setter
    def GPIO_FUNC1_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC1_OUT_INV_SEL_msb, self.__GPIO_FUNC1_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC1_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC1_OUT_SEL_msb, self.__GPIO_FUNC1_OUT_SEL_lsb)
    @GPIO_FUNC1_OUT_SEL.setter
    def GPIO_FUNC1_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC1_OUT_SEL_msb, self.__GPIO_FUNC1_OUT_SEL_lsb, value)
class GPIO_FUNC2_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x538
        self.__GPIO_FUNC2_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC2_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC2_OEN_SEL_lsb = 10
        self.__GPIO_FUNC2_OEN_SEL_msb = 10
        self.__GPIO_FUNC2_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC2_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC2_OUT_SEL_lsb = 0
        self.__GPIO_FUNC2_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC2_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC2_OEN_INV_SEL_msb, self.__GPIO_FUNC2_OEN_INV_SEL_lsb)
    @GPIO_FUNC2_OEN_INV_SEL.setter
    def GPIO_FUNC2_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC2_OEN_INV_SEL_msb, self.__GPIO_FUNC2_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC2_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC2_OEN_SEL_msb, self.__GPIO_FUNC2_OEN_SEL_lsb)
    @GPIO_FUNC2_OEN_SEL.setter
    def GPIO_FUNC2_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC2_OEN_SEL_msb, self.__GPIO_FUNC2_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC2_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC2_OUT_INV_SEL_msb, self.__GPIO_FUNC2_OUT_INV_SEL_lsb)
    @GPIO_FUNC2_OUT_INV_SEL.setter
    def GPIO_FUNC2_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC2_OUT_INV_SEL_msb, self.__GPIO_FUNC2_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC2_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC2_OUT_SEL_msb, self.__GPIO_FUNC2_OUT_SEL_lsb)
    @GPIO_FUNC2_OUT_SEL.setter
    def GPIO_FUNC2_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC2_OUT_SEL_msb, self.__GPIO_FUNC2_OUT_SEL_lsb, value)
class GPIO_FUNC3_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x53c
        self.__GPIO_FUNC3_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC3_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC3_OEN_SEL_lsb = 10
        self.__GPIO_FUNC3_OEN_SEL_msb = 10
        self.__GPIO_FUNC3_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC3_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC3_OUT_SEL_lsb = 0
        self.__GPIO_FUNC3_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC3_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC3_OEN_INV_SEL_msb, self.__GPIO_FUNC3_OEN_INV_SEL_lsb)
    @GPIO_FUNC3_OEN_INV_SEL.setter
    def GPIO_FUNC3_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC3_OEN_INV_SEL_msb, self.__GPIO_FUNC3_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC3_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC3_OEN_SEL_msb, self.__GPIO_FUNC3_OEN_SEL_lsb)
    @GPIO_FUNC3_OEN_SEL.setter
    def GPIO_FUNC3_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC3_OEN_SEL_msb, self.__GPIO_FUNC3_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC3_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC3_OUT_INV_SEL_msb, self.__GPIO_FUNC3_OUT_INV_SEL_lsb)
    @GPIO_FUNC3_OUT_INV_SEL.setter
    def GPIO_FUNC3_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC3_OUT_INV_SEL_msb, self.__GPIO_FUNC3_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC3_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC3_OUT_SEL_msb, self.__GPIO_FUNC3_OUT_SEL_lsb)
    @GPIO_FUNC3_OUT_SEL.setter
    def GPIO_FUNC3_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC3_OUT_SEL_msb, self.__GPIO_FUNC3_OUT_SEL_lsb, value)
class GPIO_FUNC4_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x540
        self.__GPIO_FUNC4_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC4_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC4_OEN_SEL_lsb = 10
        self.__GPIO_FUNC4_OEN_SEL_msb = 10
        self.__GPIO_FUNC4_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC4_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC4_OUT_SEL_lsb = 0
        self.__GPIO_FUNC4_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC4_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC4_OEN_INV_SEL_msb, self.__GPIO_FUNC4_OEN_INV_SEL_lsb)
    @GPIO_FUNC4_OEN_INV_SEL.setter
    def GPIO_FUNC4_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC4_OEN_INV_SEL_msb, self.__GPIO_FUNC4_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC4_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC4_OEN_SEL_msb, self.__GPIO_FUNC4_OEN_SEL_lsb)
    @GPIO_FUNC4_OEN_SEL.setter
    def GPIO_FUNC4_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC4_OEN_SEL_msb, self.__GPIO_FUNC4_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC4_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC4_OUT_INV_SEL_msb, self.__GPIO_FUNC4_OUT_INV_SEL_lsb)
    @GPIO_FUNC4_OUT_INV_SEL.setter
    def GPIO_FUNC4_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC4_OUT_INV_SEL_msb, self.__GPIO_FUNC4_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC4_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC4_OUT_SEL_msb, self.__GPIO_FUNC4_OUT_SEL_lsb)
    @GPIO_FUNC4_OUT_SEL.setter
    def GPIO_FUNC4_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC4_OUT_SEL_msb, self.__GPIO_FUNC4_OUT_SEL_lsb, value)
class GPIO_FUNC5_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x544
        self.__GPIO_FUNC5_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC5_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC5_OEN_SEL_lsb = 10
        self.__GPIO_FUNC5_OEN_SEL_msb = 10
        self.__GPIO_FUNC5_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC5_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC5_OUT_SEL_lsb = 0
        self.__GPIO_FUNC5_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC5_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC5_OEN_INV_SEL_msb, self.__GPIO_FUNC5_OEN_INV_SEL_lsb)
    @GPIO_FUNC5_OEN_INV_SEL.setter
    def GPIO_FUNC5_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC5_OEN_INV_SEL_msb, self.__GPIO_FUNC5_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC5_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC5_OEN_SEL_msb, self.__GPIO_FUNC5_OEN_SEL_lsb)
    @GPIO_FUNC5_OEN_SEL.setter
    def GPIO_FUNC5_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC5_OEN_SEL_msb, self.__GPIO_FUNC5_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC5_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC5_OUT_INV_SEL_msb, self.__GPIO_FUNC5_OUT_INV_SEL_lsb)
    @GPIO_FUNC5_OUT_INV_SEL.setter
    def GPIO_FUNC5_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC5_OUT_INV_SEL_msb, self.__GPIO_FUNC5_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC5_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC5_OUT_SEL_msb, self.__GPIO_FUNC5_OUT_SEL_lsb)
    @GPIO_FUNC5_OUT_SEL.setter
    def GPIO_FUNC5_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC5_OUT_SEL_msb, self.__GPIO_FUNC5_OUT_SEL_lsb, value)
class GPIO_FUNC6_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x548
        self.__GPIO_FUNC6_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC6_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC6_OEN_SEL_lsb = 10
        self.__GPIO_FUNC6_OEN_SEL_msb = 10
        self.__GPIO_FUNC6_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC6_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC6_OUT_SEL_lsb = 0
        self.__GPIO_FUNC6_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC6_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC6_OEN_INV_SEL_msb, self.__GPIO_FUNC6_OEN_INV_SEL_lsb)
    @GPIO_FUNC6_OEN_INV_SEL.setter
    def GPIO_FUNC6_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC6_OEN_INV_SEL_msb, self.__GPIO_FUNC6_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC6_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC6_OEN_SEL_msb, self.__GPIO_FUNC6_OEN_SEL_lsb)
    @GPIO_FUNC6_OEN_SEL.setter
    def GPIO_FUNC6_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC6_OEN_SEL_msb, self.__GPIO_FUNC6_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC6_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC6_OUT_INV_SEL_msb, self.__GPIO_FUNC6_OUT_INV_SEL_lsb)
    @GPIO_FUNC6_OUT_INV_SEL.setter
    def GPIO_FUNC6_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC6_OUT_INV_SEL_msb, self.__GPIO_FUNC6_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC6_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC6_OUT_SEL_msb, self.__GPIO_FUNC6_OUT_SEL_lsb)
    @GPIO_FUNC6_OUT_SEL.setter
    def GPIO_FUNC6_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC6_OUT_SEL_msb, self.__GPIO_FUNC6_OUT_SEL_lsb, value)
class GPIO_FUNC7_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x54c
        self.__GPIO_FUNC7_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC7_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC7_OEN_SEL_lsb = 10
        self.__GPIO_FUNC7_OEN_SEL_msb = 10
        self.__GPIO_FUNC7_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC7_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC7_OUT_SEL_lsb = 0
        self.__GPIO_FUNC7_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC7_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC7_OEN_INV_SEL_msb, self.__GPIO_FUNC7_OEN_INV_SEL_lsb)
    @GPIO_FUNC7_OEN_INV_SEL.setter
    def GPIO_FUNC7_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC7_OEN_INV_SEL_msb, self.__GPIO_FUNC7_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC7_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC7_OEN_SEL_msb, self.__GPIO_FUNC7_OEN_SEL_lsb)
    @GPIO_FUNC7_OEN_SEL.setter
    def GPIO_FUNC7_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC7_OEN_SEL_msb, self.__GPIO_FUNC7_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC7_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC7_OUT_INV_SEL_msb, self.__GPIO_FUNC7_OUT_INV_SEL_lsb)
    @GPIO_FUNC7_OUT_INV_SEL.setter
    def GPIO_FUNC7_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC7_OUT_INV_SEL_msb, self.__GPIO_FUNC7_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC7_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC7_OUT_SEL_msb, self.__GPIO_FUNC7_OUT_SEL_lsb)
    @GPIO_FUNC7_OUT_SEL.setter
    def GPIO_FUNC7_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC7_OUT_SEL_msb, self.__GPIO_FUNC7_OUT_SEL_lsb, value)
class GPIO_FUNC8_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x550
        self.__GPIO_FUNC8_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC8_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC8_OEN_SEL_lsb = 10
        self.__GPIO_FUNC8_OEN_SEL_msb = 10
        self.__GPIO_FUNC8_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC8_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC8_OUT_SEL_lsb = 0
        self.__GPIO_FUNC8_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC8_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC8_OEN_INV_SEL_msb, self.__GPIO_FUNC8_OEN_INV_SEL_lsb)
    @GPIO_FUNC8_OEN_INV_SEL.setter
    def GPIO_FUNC8_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC8_OEN_INV_SEL_msb, self.__GPIO_FUNC8_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC8_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC8_OEN_SEL_msb, self.__GPIO_FUNC8_OEN_SEL_lsb)
    @GPIO_FUNC8_OEN_SEL.setter
    def GPIO_FUNC8_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC8_OEN_SEL_msb, self.__GPIO_FUNC8_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC8_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC8_OUT_INV_SEL_msb, self.__GPIO_FUNC8_OUT_INV_SEL_lsb)
    @GPIO_FUNC8_OUT_INV_SEL.setter
    def GPIO_FUNC8_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC8_OUT_INV_SEL_msb, self.__GPIO_FUNC8_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC8_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC8_OUT_SEL_msb, self.__GPIO_FUNC8_OUT_SEL_lsb)
    @GPIO_FUNC8_OUT_SEL.setter
    def GPIO_FUNC8_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC8_OUT_SEL_msb, self.__GPIO_FUNC8_OUT_SEL_lsb, value)
class GPIO_FUNC9_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x554
        self.__GPIO_FUNC9_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC9_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC9_OEN_SEL_lsb = 10
        self.__GPIO_FUNC9_OEN_SEL_msb = 10
        self.__GPIO_FUNC9_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC9_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC9_OUT_SEL_lsb = 0
        self.__GPIO_FUNC9_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC9_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC9_OEN_INV_SEL_msb, self.__GPIO_FUNC9_OEN_INV_SEL_lsb)
    @GPIO_FUNC9_OEN_INV_SEL.setter
    def GPIO_FUNC9_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC9_OEN_INV_SEL_msb, self.__GPIO_FUNC9_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC9_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC9_OEN_SEL_msb, self.__GPIO_FUNC9_OEN_SEL_lsb)
    @GPIO_FUNC9_OEN_SEL.setter
    def GPIO_FUNC9_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC9_OEN_SEL_msb, self.__GPIO_FUNC9_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC9_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC9_OUT_INV_SEL_msb, self.__GPIO_FUNC9_OUT_INV_SEL_lsb)
    @GPIO_FUNC9_OUT_INV_SEL.setter
    def GPIO_FUNC9_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC9_OUT_INV_SEL_msb, self.__GPIO_FUNC9_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC9_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC9_OUT_SEL_msb, self.__GPIO_FUNC9_OUT_SEL_lsb)
    @GPIO_FUNC9_OUT_SEL.setter
    def GPIO_FUNC9_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC9_OUT_SEL_msb, self.__GPIO_FUNC9_OUT_SEL_lsb, value)
class GPIO_FUNC10_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x558
        self.__GPIO_FUNC10_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC10_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC10_OEN_SEL_lsb = 10
        self.__GPIO_FUNC10_OEN_SEL_msb = 10
        self.__GPIO_FUNC10_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC10_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC10_OUT_SEL_lsb = 0
        self.__GPIO_FUNC10_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC10_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC10_OEN_INV_SEL_msb, self.__GPIO_FUNC10_OEN_INV_SEL_lsb)
    @GPIO_FUNC10_OEN_INV_SEL.setter
    def GPIO_FUNC10_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC10_OEN_INV_SEL_msb, self.__GPIO_FUNC10_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC10_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC10_OEN_SEL_msb, self.__GPIO_FUNC10_OEN_SEL_lsb)
    @GPIO_FUNC10_OEN_SEL.setter
    def GPIO_FUNC10_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC10_OEN_SEL_msb, self.__GPIO_FUNC10_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC10_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC10_OUT_INV_SEL_msb, self.__GPIO_FUNC10_OUT_INV_SEL_lsb)
    @GPIO_FUNC10_OUT_INV_SEL.setter
    def GPIO_FUNC10_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC10_OUT_INV_SEL_msb, self.__GPIO_FUNC10_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC10_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC10_OUT_SEL_msb, self.__GPIO_FUNC10_OUT_SEL_lsb)
    @GPIO_FUNC10_OUT_SEL.setter
    def GPIO_FUNC10_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC10_OUT_SEL_msb, self.__GPIO_FUNC10_OUT_SEL_lsb, value)
class GPIO_FUNC11_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x55c
        self.__GPIO_FUNC11_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC11_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC11_OEN_SEL_lsb = 10
        self.__GPIO_FUNC11_OEN_SEL_msb = 10
        self.__GPIO_FUNC11_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC11_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC11_OUT_SEL_lsb = 0
        self.__GPIO_FUNC11_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC11_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC11_OEN_INV_SEL_msb, self.__GPIO_FUNC11_OEN_INV_SEL_lsb)
    @GPIO_FUNC11_OEN_INV_SEL.setter
    def GPIO_FUNC11_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC11_OEN_INV_SEL_msb, self.__GPIO_FUNC11_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC11_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC11_OEN_SEL_msb, self.__GPIO_FUNC11_OEN_SEL_lsb)
    @GPIO_FUNC11_OEN_SEL.setter
    def GPIO_FUNC11_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC11_OEN_SEL_msb, self.__GPIO_FUNC11_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC11_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC11_OUT_INV_SEL_msb, self.__GPIO_FUNC11_OUT_INV_SEL_lsb)
    @GPIO_FUNC11_OUT_INV_SEL.setter
    def GPIO_FUNC11_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC11_OUT_INV_SEL_msb, self.__GPIO_FUNC11_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC11_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC11_OUT_SEL_msb, self.__GPIO_FUNC11_OUT_SEL_lsb)
    @GPIO_FUNC11_OUT_SEL.setter
    def GPIO_FUNC11_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC11_OUT_SEL_msb, self.__GPIO_FUNC11_OUT_SEL_lsb, value)
class GPIO_FUNC12_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x560
        self.__GPIO_FUNC12_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC12_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC12_OEN_SEL_lsb = 10
        self.__GPIO_FUNC12_OEN_SEL_msb = 10
        self.__GPIO_FUNC12_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC12_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC12_OUT_SEL_lsb = 0
        self.__GPIO_FUNC12_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC12_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC12_OEN_INV_SEL_msb, self.__GPIO_FUNC12_OEN_INV_SEL_lsb)
    @GPIO_FUNC12_OEN_INV_SEL.setter
    def GPIO_FUNC12_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC12_OEN_INV_SEL_msb, self.__GPIO_FUNC12_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC12_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC12_OEN_SEL_msb, self.__GPIO_FUNC12_OEN_SEL_lsb)
    @GPIO_FUNC12_OEN_SEL.setter
    def GPIO_FUNC12_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC12_OEN_SEL_msb, self.__GPIO_FUNC12_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC12_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC12_OUT_INV_SEL_msb, self.__GPIO_FUNC12_OUT_INV_SEL_lsb)
    @GPIO_FUNC12_OUT_INV_SEL.setter
    def GPIO_FUNC12_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC12_OUT_INV_SEL_msb, self.__GPIO_FUNC12_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC12_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC12_OUT_SEL_msb, self.__GPIO_FUNC12_OUT_SEL_lsb)
    @GPIO_FUNC12_OUT_SEL.setter
    def GPIO_FUNC12_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC12_OUT_SEL_msb, self.__GPIO_FUNC12_OUT_SEL_lsb, value)
class GPIO_FUNC13_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x564
        self.__GPIO_FUNC13_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC13_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC13_OEN_SEL_lsb = 10
        self.__GPIO_FUNC13_OEN_SEL_msb = 10
        self.__GPIO_FUNC13_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC13_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC13_OUT_SEL_lsb = 0
        self.__GPIO_FUNC13_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC13_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC13_OEN_INV_SEL_msb, self.__GPIO_FUNC13_OEN_INV_SEL_lsb)
    @GPIO_FUNC13_OEN_INV_SEL.setter
    def GPIO_FUNC13_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC13_OEN_INV_SEL_msb, self.__GPIO_FUNC13_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC13_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC13_OEN_SEL_msb, self.__GPIO_FUNC13_OEN_SEL_lsb)
    @GPIO_FUNC13_OEN_SEL.setter
    def GPIO_FUNC13_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC13_OEN_SEL_msb, self.__GPIO_FUNC13_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC13_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC13_OUT_INV_SEL_msb, self.__GPIO_FUNC13_OUT_INV_SEL_lsb)
    @GPIO_FUNC13_OUT_INV_SEL.setter
    def GPIO_FUNC13_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC13_OUT_INV_SEL_msb, self.__GPIO_FUNC13_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC13_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC13_OUT_SEL_msb, self.__GPIO_FUNC13_OUT_SEL_lsb)
    @GPIO_FUNC13_OUT_SEL.setter
    def GPIO_FUNC13_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC13_OUT_SEL_msb, self.__GPIO_FUNC13_OUT_SEL_lsb, value)
class GPIO_FUNC14_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x568
        self.__GPIO_FUNC14_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC14_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC14_OEN_SEL_lsb = 10
        self.__GPIO_FUNC14_OEN_SEL_msb = 10
        self.__GPIO_FUNC14_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC14_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC14_OUT_SEL_lsb = 0
        self.__GPIO_FUNC14_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC14_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC14_OEN_INV_SEL_msb, self.__GPIO_FUNC14_OEN_INV_SEL_lsb)
    @GPIO_FUNC14_OEN_INV_SEL.setter
    def GPIO_FUNC14_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC14_OEN_INV_SEL_msb, self.__GPIO_FUNC14_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC14_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC14_OEN_SEL_msb, self.__GPIO_FUNC14_OEN_SEL_lsb)
    @GPIO_FUNC14_OEN_SEL.setter
    def GPIO_FUNC14_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC14_OEN_SEL_msb, self.__GPIO_FUNC14_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC14_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC14_OUT_INV_SEL_msb, self.__GPIO_FUNC14_OUT_INV_SEL_lsb)
    @GPIO_FUNC14_OUT_INV_SEL.setter
    def GPIO_FUNC14_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC14_OUT_INV_SEL_msb, self.__GPIO_FUNC14_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC14_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC14_OUT_SEL_msb, self.__GPIO_FUNC14_OUT_SEL_lsb)
    @GPIO_FUNC14_OUT_SEL.setter
    def GPIO_FUNC14_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC14_OUT_SEL_msb, self.__GPIO_FUNC14_OUT_SEL_lsb, value)
class GPIO_FUNC15_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x56c
        self.__GPIO_FUNC15_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC15_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC15_OEN_SEL_lsb = 10
        self.__GPIO_FUNC15_OEN_SEL_msb = 10
        self.__GPIO_FUNC15_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC15_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC15_OUT_SEL_lsb = 0
        self.__GPIO_FUNC15_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC15_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC15_OEN_INV_SEL_msb, self.__GPIO_FUNC15_OEN_INV_SEL_lsb)
    @GPIO_FUNC15_OEN_INV_SEL.setter
    def GPIO_FUNC15_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC15_OEN_INV_SEL_msb, self.__GPIO_FUNC15_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC15_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC15_OEN_SEL_msb, self.__GPIO_FUNC15_OEN_SEL_lsb)
    @GPIO_FUNC15_OEN_SEL.setter
    def GPIO_FUNC15_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC15_OEN_SEL_msb, self.__GPIO_FUNC15_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC15_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC15_OUT_INV_SEL_msb, self.__GPIO_FUNC15_OUT_INV_SEL_lsb)
    @GPIO_FUNC15_OUT_INV_SEL.setter
    def GPIO_FUNC15_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC15_OUT_INV_SEL_msb, self.__GPIO_FUNC15_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC15_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC15_OUT_SEL_msb, self.__GPIO_FUNC15_OUT_SEL_lsb)
    @GPIO_FUNC15_OUT_SEL.setter
    def GPIO_FUNC15_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC15_OUT_SEL_msb, self.__GPIO_FUNC15_OUT_SEL_lsb, value)
class GPIO_FUNC16_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x570
        self.__GPIO_FUNC16_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC16_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC16_OEN_SEL_lsb = 10
        self.__GPIO_FUNC16_OEN_SEL_msb = 10
        self.__GPIO_FUNC16_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC16_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC16_OUT_SEL_lsb = 0
        self.__GPIO_FUNC16_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC16_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC16_OEN_INV_SEL_msb, self.__GPIO_FUNC16_OEN_INV_SEL_lsb)
    @GPIO_FUNC16_OEN_INV_SEL.setter
    def GPIO_FUNC16_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC16_OEN_INV_SEL_msb, self.__GPIO_FUNC16_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC16_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC16_OEN_SEL_msb, self.__GPIO_FUNC16_OEN_SEL_lsb)
    @GPIO_FUNC16_OEN_SEL.setter
    def GPIO_FUNC16_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC16_OEN_SEL_msb, self.__GPIO_FUNC16_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC16_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC16_OUT_INV_SEL_msb, self.__GPIO_FUNC16_OUT_INV_SEL_lsb)
    @GPIO_FUNC16_OUT_INV_SEL.setter
    def GPIO_FUNC16_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC16_OUT_INV_SEL_msb, self.__GPIO_FUNC16_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC16_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC16_OUT_SEL_msb, self.__GPIO_FUNC16_OUT_SEL_lsb)
    @GPIO_FUNC16_OUT_SEL.setter
    def GPIO_FUNC16_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC16_OUT_SEL_msb, self.__GPIO_FUNC16_OUT_SEL_lsb, value)
class GPIO_FUNC17_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x574
        self.__GPIO_FUNC17_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC17_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC17_OEN_SEL_lsb = 10
        self.__GPIO_FUNC17_OEN_SEL_msb = 10
        self.__GPIO_FUNC17_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC17_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC17_OUT_SEL_lsb = 0
        self.__GPIO_FUNC17_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC17_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC17_OEN_INV_SEL_msb, self.__GPIO_FUNC17_OEN_INV_SEL_lsb)
    @GPIO_FUNC17_OEN_INV_SEL.setter
    def GPIO_FUNC17_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC17_OEN_INV_SEL_msb, self.__GPIO_FUNC17_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC17_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC17_OEN_SEL_msb, self.__GPIO_FUNC17_OEN_SEL_lsb)
    @GPIO_FUNC17_OEN_SEL.setter
    def GPIO_FUNC17_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC17_OEN_SEL_msb, self.__GPIO_FUNC17_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC17_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC17_OUT_INV_SEL_msb, self.__GPIO_FUNC17_OUT_INV_SEL_lsb)
    @GPIO_FUNC17_OUT_INV_SEL.setter
    def GPIO_FUNC17_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC17_OUT_INV_SEL_msb, self.__GPIO_FUNC17_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC17_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC17_OUT_SEL_msb, self.__GPIO_FUNC17_OUT_SEL_lsb)
    @GPIO_FUNC17_OUT_SEL.setter
    def GPIO_FUNC17_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC17_OUT_SEL_msb, self.__GPIO_FUNC17_OUT_SEL_lsb, value)
class GPIO_FUNC18_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x578
        self.__GPIO_FUNC18_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC18_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC18_OEN_SEL_lsb = 10
        self.__GPIO_FUNC18_OEN_SEL_msb = 10
        self.__GPIO_FUNC18_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC18_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC18_OUT_SEL_lsb = 0
        self.__GPIO_FUNC18_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC18_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC18_OEN_INV_SEL_msb, self.__GPIO_FUNC18_OEN_INV_SEL_lsb)
    @GPIO_FUNC18_OEN_INV_SEL.setter
    def GPIO_FUNC18_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC18_OEN_INV_SEL_msb, self.__GPIO_FUNC18_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC18_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC18_OEN_SEL_msb, self.__GPIO_FUNC18_OEN_SEL_lsb)
    @GPIO_FUNC18_OEN_SEL.setter
    def GPIO_FUNC18_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC18_OEN_SEL_msb, self.__GPIO_FUNC18_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC18_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC18_OUT_INV_SEL_msb, self.__GPIO_FUNC18_OUT_INV_SEL_lsb)
    @GPIO_FUNC18_OUT_INV_SEL.setter
    def GPIO_FUNC18_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC18_OUT_INV_SEL_msb, self.__GPIO_FUNC18_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC18_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC18_OUT_SEL_msb, self.__GPIO_FUNC18_OUT_SEL_lsb)
    @GPIO_FUNC18_OUT_SEL.setter
    def GPIO_FUNC18_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC18_OUT_SEL_msb, self.__GPIO_FUNC18_OUT_SEL_lsb, value)
class GPIO_FUNC19_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x57c
        self.__GPIO_FUNC19_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC19_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC19_OEN_SEL_lsb = 10
        self.__GPIO_FUNC19_OEN_SEL_msb = 10
        self.__GPIO_FUNC19_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC19_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC19_OUT_SEL_lsb = 0
        self.__GPIO_FUNC19_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC19_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC19_OEN_INV_SEL_msb, self.__GPIO_FUNC19_OEN_INV_SEL_lsb)
    @GPIO_FUNC19_OEN_INV_SEL.setter
    def GPIO_FUNC19_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC19_OEN_INV_SEL_msb, self.__GPIO_FUNC19_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC19_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC19_OEN_SEL_msb, self.__GPIO_FUNC19_OEN_SEL_lsb)
    @GPIO_FUNC19_OEN_SEL.setter
    def GPIO_FUNC19_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC19_OEN_SEL_msb, self.__GPIO_FUNC19_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC19_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC19_OUT_INV_SEL_msb, self.__GPIO_FUNC19_OUT_INV_SEL_lsb)
    @GPIO_FUNC19_OUT_INV_SEL.setter
    def GPIO_FUNC19_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC19_OUT_INV_SEL_msb, self.__GPIO_FUNC19_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC19_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC19_OUT_SEL_msb, self.__GPIO_FUNC19_OUT_SEL_lsb)
    @GPIO_FUNC19_OUT_SEL.setter
    def GPIO_FUNC19_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC19_OUT_SEL_msb, self.__GPIO_FUNC19_OUT_SEL_lsb, value)
class GPIO_FUNC20_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x580
        self.__GPIO_FUNC20_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC20_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC20_OEN_SEL_lsb = 10
        self.__GPIO_FUNC20_OEN_SEL_msb = 10
        self.__GPIO_FUNC20_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC20_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC20_OUT_SEL_lsb = 0
        self.__GPIO_FUNC20_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC20_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC20_OEN_INV_SEL_msb, self.__GPIO_FUNC20_OEN_INV_SEL_lsb)
    @GPIO_FUNC20_OEN_INV_SEL.setter
    def GPIO_FUNC20_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC20_OEN_INV_SEL_msb, self.__GPIO_FUNC20_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC20_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC20_OEN_SEL_msb, self.__GPIO_FUNC20_OEN_SEL_lsb)
    @GPIO_FUNC20_OEN_SEL.setter
    def GPIO_FUNC20_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC20_OEN_SEL_msb, self.__GPIO_FUNC20_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC20_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC20_OUT_INV_SEL_msb, self.__GPIO_FUNC20_OUT_INV_SEL_lsb)
    @GPIO_FUNC20_OUT_INV_SEL.setter
    def GPIO_FUNC20_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC20_OUT_INV_SEL_msb, self.__GPIO_FUNC20_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC20_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC20_OUT_SEL_msb, self.__GPIO_FUNC20_OUT_SEL_lsb)
    @GPIO_FUNC20_OUT_SEL.setter
    def GPIO_FUNC20_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC20_OUT_SEL_msb, self.__GPIO_FUNC20_OUT_SEL_lsb, value)
class GPIO_FUNC21_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x584
        self.__GPIO_FUNC21_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC21_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC21_OEN_SEL_lsb = 10
        self.__GPIO_FUNC21_OEN_SEL_msb = 10
        self.__GPIO_FUNC21_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC21_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC21_OUT_SEL_lsb = 0
        self.__GPIO_FUNC21_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC21_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC21_OEN_INV_SEL_msb, self.__GPIO_FUNC21_OEN_INV_SEL_lsb)
    @GPIO_FUNC21_OEN_INV_SEL.setter
    def GPIO_FUNC21_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC21_OEN_INV_SEL_msb, self.__GPIO_FUNC21_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC21_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC21_OEN_SEL_msb, self.__GPIO_FUNC21_OEN_SEL_lsb)
    @GPIO_FUNC21_OEN_SEL.setter
    def GPIO_FUNC21_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC21_OEN_SEL_msb, self.__GPIO_FUNC21_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC21_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC21_OUT_INV_SEL_msb, self.__GPIO_FUNC21_OUT_INV_SEL_lsb)
    @GPIO_FUNC21_OUT_INV_SEL.setter
    def GPIO_FUNC21_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC21_OUT_INV_SEL_msb, self.__GPIO_FUNC21_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC21_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC21_OUT_SEL_msb, self.__GPIO_FUNC21_OUT_SEL_lsb)
    @GPIO_FUNC21_OUT_SEL.setter
    def GPIO_FUNC21_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC21_OUT_SEL_msb, self.__GPIO_FUNC21_OUT_SEL_lsb, value)
class GPIO_FUNC22_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x588
        self.__GPIO_FUNC22_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC22_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC22_OEN_SEL_lsb = 10
        self.__GPIO_FUNC22_OEN_SEL_msb = 10
        self.__GPIO_FUNC22_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC22_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC22_OUT_SEL_lsb = 0
        self.__GPIO_FUNC22_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC22_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC22_OEN_INV_SEL_msb, self.__GPIO_FUNC22_OEN_INV_SEL_lsb)
    @GPIO_FUNC22_OEN_INV_SEL.setter
    def GPIO_FUNC22_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC22_OEN_INV_SEL_msb, self.__GPIO_FUNC22_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC22_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC22_OEN_SEL_msb, self.__GPIO_FUNC22_OEN_SEL_lsb)
    @GPIO_FUNC22_OEN_SEL.setter
    def GPIO_FUNC22_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC22_OEN_SEL_msb, self.__GPIO_FUNC22_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC22_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC22_OUT_INV_SEL_msb, self.__GPIO_FUNC22_OUT_INV_SEL_lsb)
    @GPIO_FUNC22_OUT_INV_SEL.setter
    def GPIO_FUNC22_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC22_OUT_INV_SEL_msb, self.__GPIO_FUNC22_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC22_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC22_OUT_SEL_msb, self.__GPIO_FUNC22_OUT_SEL_lsb)
    @GPIO_FUNC22_OUT_SEL.setter
    def GPIO_FUNC22_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC22_OUT_SEL_msb, self.__GPIO_FUNC22_OUT_SEL_lsb, value)
class GPIO_FUNC23_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x58c
        self.__GPIO_FUNC23_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC23_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC23_OEN_SEL_lsb = 10
        self.__GPIO_FUNC23_OEN_SEL_msb = 10
        self.__GPIO_FUNC23_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC23_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC23_OUT_SEL_lsb = 0
        self.__GPIO_FUNC23_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC23_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC23_OEN_INV_SEL_msb, self.__GPIO_FUNC23_OEN_INV_SEL_lsb)
    @GPIO_FUNC23_OEN_INV_SEL.setter
    def GPIO_FUNC23_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC23_OEN_INV_SEL_msb, self.__GPIO_FUNC23_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC23_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC23_OEN_SEL_msb, self.__GPIO_FUNC23_OEN_SEL_lsb)
    @GPIO_FUNC23_OEN_SEL.setter
    def GPIO_FUNC23_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC23_OEN_SEL_msb, self.__GPIO_FUNC23_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC23_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC23_OUT_INV_SEL_msb, self.__GPIO_FUNC23_OUT_INV_SEL_lsb)
    @GPIO_FUNC23_OUT_INV_SEL.setter
    def GPIO_FUNC23_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC23_OUT_INV_SEL_msb, self.__GPIO_FUNC23_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC23_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC23_OUT_SEL_msb, self.__GPIO_FUNC23_OUT_SEL_lsb)
    @GPIO_FUNC23_OUT_SEL.setter
    def GPIO_FUNC23_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC23_OUT_SEL_msb, self.__GPIO_FUNC23_OUT_SEL_lsb, value)
class GPIO_FUNC24_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x590
        self.__GPIO_FUNC24_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC24_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC24_OEN_SEL_lsb = 10
        self.__GPIO_FUNC24_OEN_SEL_msb = 10
        self.__GPIO_FUNC24_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC24_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC24_OUT_SEL_lsb = 0
        self.__GPIO_FUNC24_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC24_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC24_OEN_INV_SEL_msb, self.__GPIO_FUNC24_OEN_INV_SEL_lsb)
    @GPIO_FUNC24_OEN_INV_SEL.setter
    def GPIO_FUNC24_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC24_OEN_INV_SEL_msb, self.__GPIO_FUNC24_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC24_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC24_OEN_SEL_msb, self.__GPIO_FUNC24_OEN_SEL_lsb)
    @GPIO_FUNC24_OEN_SEL.setter
    def GPIO_FUNC24_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC24_OEN_SEL_msb, self.__GPIO_FUNC24_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC24_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC24_OUT_INV_SEL_msb, self.__GPIO_FUNC24_OUT_INV_SEL_lsb)
    @GPIO_FUNC24_OUT_INV_SEL.setter
    def GPIO_FUNC24_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC24_OUT_INV_SEL_msb, self.__GPIO_FUNC24_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC24_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC24_OUT_SEL_msb, self.__GPIO_FUNC24_OUT_SEL_lsb)
    @GPIO_FUNC24_OUT_SEL.setter
    def GPIO_FUNC24_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC24_OUT_SEL_msb, self.__GPIO_FUNC24_OUT_SEL_lsb, value)
class GPIO_FUNC25_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x594
        self.__GPIO_FUNC25_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC25_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC25_OEN_SEL_lsb = 10
        self.__GPIO_FUNC25_OEN_SEL_msb = 10
        self.__GPIO_FUNC25_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC25_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC25_OUT_SEL_lsb = 0
        self.__GPIO_FUNC25_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC25_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC25_OEN_INV_SEL_msb, self.__GPIO_FUNC25_OEN_INV_SEL_lsb)
    @GPIO_FUNC25_OEN_INV_SEL.setter
    def GPIO_FUNC25_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC25_OEN_INV_SEL_msb, self.__GPIO_FUNC25_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC25_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC25_OEN_SEL_msb, self.__GPIO_FUNC25_OEN_SEL_lsb)
    @GPIO_FUNC25_OEN_SEL.setter
    def GPIO_FUNC25_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC25_OEN_SEL_msb, self.__GPIO_FUNC25_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC25_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC25_OUT_INV_SEL_msb, self.__GPIO_FUNC25_OUT_INV_SEL_lsb)
    @GPIO_FUNC25_OUT_INV_SEL.setter
    def GPIO_FUNC25_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC25_OUT_INV_SEL_msb, self.__GPIO_FUNC25_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC25_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC25_OUT_SEL_msb, self.__GPIO_FUNC25_OUT_SEL_lsb)
    @GPIO_FUNC25_OUT_SEL.setter
    def GPIO_FUNC25_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC25_OUT_SEL_msb, self.__GPIO_FUNC25_OUT_SEL_lsb, value)
class GPIO_FUNC26_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x598
        self.__GPIO_FUNC26_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC26_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC26_OEN_SEL_lsb = 10
        self.__GPIO_FUNC26_OEN_SEL_msb = 10
        self.__GPIO_FUNC26_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC26_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC26_OUT_SEL_lsb = 0
        self.__GPIO_FUNC26_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC26_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC26_OEN_INV_SEL_msb, self.__GPIO_FUNC26_OEN_INV_SEL_lsb)
    @GPIO_FUNC26_OEN_INV_SEL.setter
    def GPIO_FUNC26_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC26_OEN_INV_SEL_msb, self.__GPIO_FUNC26_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC26_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC26_OEN_SEL_msb, self.__GPIO_FUNC26_OEN_SEL_lsb)
    @GPIO_FUNC26_OEN_SEL.setter
    def GPIO_FUNC26_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC26_OEN_SEL_msb, self.__GPIO_FUNC26_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC26_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC26_OUT_INV_SEL_msb, self.__GPIO_FUNC26_OUT_INV_SEL_lsb)
    @GPIO_FUNC26_OUT_INV_SEL.setter
    def GPIO_FUNC26_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC26_OUT_INV_SEL_msb, self.__GPIO_FUNC26_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC26_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC26_OUT_SEL_msb, self.__GPIO_FUNC26_OUT_SEL_lsb)
    @GPIO_FUNC26_OUT_SEL.setter
    def GPIO_FUNC26_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC26_OUT_SEL_msb, self.__GPIO_FUNC26_OUT_SEL_lsb, value)
class GPIO_FUNC27_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x59c
        self.__GPIO_FUNC27_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC27_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC27_OEN_SEL_lsb = 10
        self.__GPIO_FUNC27_OEN_SEL_msb = 10
        self.__GPIO_FUNC27_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC27_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC27_OUT_SEL_lsb = 0
        self.__GPIO_FUNC27_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC27_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC27_OEN_INV_SEL_msb, self.__GPIO_FUNC27_OEN_INV_SEL_lsb)
    @GPIO_FUNC27_OEN_INV_SEL.setter
    def GPIO_FUNC27_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC27_OEN_INV_SEL_msb, self.__GPIO_FUNC27_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC27_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC27_OEN_SEL_msb, self.__GPIO_FUNC27_OEN_SEL_lsb)
    @GPIO_FUNC27_OEN_SEL.setter
    def GPIO_FUNC27_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC27_OEN_SEL_msb, self.__GPIO_FUNC27_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC27_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC27_OUT_INV_SEL_msb, self.__GPIO_FUNC27_OUT_INV_SEL_lsb)
    @GPIO_FUNC27_OUT_INV_SEL.setter
    def GPIO_FUNC27_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC27_OUT_INV_SEL_msb, self.__GPIO_FUNC27_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC27_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC27_OUT_SEL_msb, self.__GPIO_FUNC27_OUT_SEL_lsb)
    @GPIO_FUNC27_OUT_SEL.setter
    def GPIO_FUNC27_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC27_OUT_SEL_msb, self.__GPIO_FUNC27_OUT_SEL_lsb, value)
class GPIO_FUNC28_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x5a0
        self.__GPIO_FUNC28_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC28_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC28_OEN_SEL_lsb = 10
        self.__GPIO_FUNC28_OEN_SEL_msb = 10
        self.__GPIO_FUNC28_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC28_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC28_OUT_SEL_lsb = 0
        self.__GPIO_FUNC28_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC28_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC28_OEN_INV_SEL_msb, self.__GPIO_FUNC28_OEN_INV_SEL_lsb)
    @GPIO_FUNC28_OEN_INV_SEL.setter
    def GPIO_FUNC28_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC28_OEN_INV_SEL_msb, self.__GPIO_FUNC28_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC28_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC28_OEN_SEL_msb, self.__GPIO_FUNC28_OEN_SEL_lsb)
    @GPIO_FUNC28_OEN_SEL.setter
    def GPIO_FUNC28_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC28_OEN_SEL_msb, self.__GPIO_FUNC28_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC28_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC28_OUT_INV_SEL_msb, self.__GPIO_FUNC28_OUT_INV_SEL_lsb)
    @GPIO_FUNC28_OUT_INV_SEL.setter
    def GPIO_FUNC28_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC28_OUT_INV_SEL_msb, self.__GPIO_FUNC28_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC28_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC28_OUT_SEL_msb, self.__GPIO_FUNC28_OUT_SEL_lsb)
    @GPIO_FUNC28_OUT_SEL.setter
    def GPIO_FUNC28_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC28_OUT_SEL_msb, self.__GPIO_FUNC28_OUT_SEL_lsb, value)
class GPIO_FUNC29_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x5a4
        self.__GPIO_FUNC29_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC29_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC29_OEN_SEL_lsb = 10
        self.__GPIO_FUNC29_OEN_SEL_msb = 10
        self.__GPIO_FUNC29_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC29_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC29_OUT_SEL_lsb = 0
        self.__GPIO_FUNC29_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC29_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC29_OEN_INV_SEL_msb, self.__GPIO_FUNC29_OEN_INV_SEL_lsb)
    @GPIO_FUNC29_OEN_INV_SEL.setter
    def GPIO_FUNC29_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC29_OEN_INV_SEL_msb, self.__GPIO_FUNC29_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC29_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC29_OEN_SEL_msb, self.__GPIO_FUNC29_OEN_SEL_lsb)
    @GPIO_FUNC29_OEN_SEL.setter
    def GPIO_FUNC29_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC29_OEN_SEL_msb, self.__GPIO_FUNC29_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC29_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC29_OUT_INV_SEL_msb, self.__GPIO_FUNC29_OUT_INV_SEL_lsb)
    @GPIO_FUNC29_OUT_INV_SEL.setter
    def GPIO_FUNC29_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC29_OUT_INV_SEL_msb, self.__GPIO_FUNC29_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC29_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC29_OUT_SEL_msb, self.__GPIO_FUNC29_OUT_SEL_lsb)
    @GPIO_FUNC29_OUT_SEL.setter
    def GPIO_FUNC29_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC29_OUT_SEL_msb, self.__GPIO_FUNC29_OUT_SEL_lsb, value)
class GPIO_FUNC30_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x5a8
        self.__GPIO_FUNC30_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC30_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC30_OEN_SEL_lsb = 10
        self.__GPIO_FUNC30_OEN_SEL_msb = 10
        self.__GPIO_FUNC30_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC30_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC30_OUT_SEL_lsb = 0
        self.__GPIO_FUNC30_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC30_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC30_OEN_INV_SEL_msb, self.__GPIO_FUNC30_OEN_INV_SEL_lsb)
    @GPIO_FUNC30_OEN_INV_SEL.setter
    def GPIO_FUNC30_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC30_OEN_INV_SEL_msb, self.__GPIO_FUNC30_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC30_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC30_OEN_SEL_msb, self.__GPIO_FUNC30_OEN_SEL_lsb)
    @GPIO_FUNC30_OEN_SEL.setter
    def GPIO_FUNC30_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC30_OEN_SEL_msb, self.__GPIO_FUNC30_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC30_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC30_OUT_INV_SEL_msb, self.__GPIO_FUNC30_OUT_INV_SEL_lsb)
    @GPIO_FUNC30_OUT_INV_SEL.setter
    def GPIO_FUNC30_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC30_OUT_INV_SEL_msb, self.__GPIO_FUNC30_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC30_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC30_OUT_SEL_msb, self.__GPIO_FUNC30_OUT_SEL_lsb)
    @GPIO_FUNC30_OUT_SEL.setter
    def GPIO_FUNC30_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC30_OUT_SEL_msb, self.__GPIO_FUNC30_OUT_SEL_lsb, value)
class GPIO_FUNC31_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x5ac
        self.__GPIO_FUNC31_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC31_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC31_OEN_SEL_lsb = 10
        self.__GPIO_FUNC31_OEN_SEL_msb = 10
        self.__GPIO_FUNC31_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC31_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC31_OUT_SEL_lsb = 0
        self.__GPIO_FUNC31_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC31_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC31_OEN_INV_SEL_msb, self.__GPIO_FUNC31_OEN_INV_SEL_lsb)
    @GPIO_FUNC31_OEN_INV_SEL.setter
    def GPIO_FUNC31_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC31_OEN_INV_SEL_msb, self.__GPIO_FUNC31_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC31_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC31_OEN_SEL_msb, self.__GPIO_FUNC31_OEN_SEL_lsb)
    @GPIO_FUNC31_OEN_SEL.setter
    def GPIO_FUNC31_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC31_OEN_SEL_msb, self.__GPIO_FUNC31_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC31_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC31_OUT_INV_SEL_msb, self.__GPIO_FUNC31_OUT_INV_SEL_lsb)
    @GPIO_FUNC31_OUT_INV_SEL.setter
    def GPIO_FUNC31_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC31_OUT_INV_SEL_msb, self.__GPIO_FUNC31_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC31_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC31_OUT_SEL_msb, self.__GPIO_FUNC31_OUT_SEL_lsb)
    @GPIO_FUNC31_OUT_SEL.setter
    def GPIO_FUNC31_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC31_OUT_SEL_msb, self.__GPIO_FUNC31_OUT_SEL_lsb, value)
class GPIO_FUNC32_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x5b0
        self.__GPIO_FUNC32_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC32_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC32_OEN_SEL_lsb = 10
        self.__GPIO_FUNC32_OEN_SEL_msb = 10
        self.__GPIO_FUNC32_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC32_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC32_OUT_SEL_lsb = 0
        self.__GPIO_FUNC32_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC32_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC32_OEN_INV_SEL_msb, self.__GPIO_FUNC32_OEN_INV_SEL_lsb)
    @GPIO_FUNC32_OEN_INV_SEL.setter
    def GPIO_FUNC32_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC32_OEN_INV_SEL_msb, self.__GPIO_FUNC32_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC32_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC32_OEN_SEL_msb, self.__GPIO_FUNC32_OEN_SEL_lsb)
    @GPIO_FUNC32_OEN_SEL.setter
    def GPIO_FUNC32_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC32_OEN_SEL_msb, self.__GPIO_FUNC32_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC32_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC32_OUT_INV_SEL_msb, self.__GPIO_FUNC32_OUT_INV_SEL_lsb)
    @GPIO_FUNC32_OUT_INV_SEL.setter
    def GPIO_FUNC32_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC32_OUT_INV_SEL_msb, self.__GPIO_FUNC32_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC32_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC32_OUT_SEL_msb, self.__GPIO_FUNC32_OUT_SEL_lsb)
    @GPIO_FUNC32_OUT_SEL.setter
    def GPIO_FUNC32_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC32_OUT_SEL_msb, self.__GPIO_FUNC32_OUT_SEL_lsb, value)
class GPIO_FUNC33_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x5b4
        self.__GPIO_FUNC33_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC33_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC33_OEN_SEL_lsb = 10
        self.__GPIO_FUNC33_OEN_SEL_msb = 10
        self.__GPIO_FUNC33_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC33_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC33_OUT_SEL_lsb = 0
        self.__GPIO_FUNC33_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC33_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC33_OEN_INV_SEL_msb, self.__GPIO_FUNC33_OEN_INV_SEL_lsb)
    @GPIO_FUNC33_OEN_INV_SEL.setter
    def GPIO_FUNC33_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC33_OEN_INV_SEL_msb, self.__GPIO_FUNC33_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC33_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC33_OEN_SEL_msb, self.__GPIO_FUNC33_OEN_SEL_lsb)
    @GPIO_FUNC33_OEN_SEL.setter
    def GPIO_FUNC33_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC33_OEN_SEL_msb, self.__GPIO_FUNC33_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC33_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC33_OUT_INV_SEL_msb, self.__GPIO_FUNC33_OUT_INV_SEL_lsb)
    @GPIO_FUNC33_OUT_INV_SEL.setter
    def GPIO_FUNC33_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC33_OUT_INV_SEL_msb, self.__GPIO_FUNC33_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC33_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC33_OUT_SEL_msb, self.__GPIO_FUNC33_OUT_SEL_lsb)
    @GPIO_FUNC33_OUT_SEL.setter
    def GPIO_FUNC33_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC33_OUT_SEL_msb, self.__GPIO_FUNC33_OUT_SEL_lsb, value)
class GPIO_FUNC34_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x5b8
        self.__GPIO_FUNC34_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC34_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC34_OEN_SEL_lsb = 10
        self.__GPIO_FUNC34_OEN_SEL_msb = 10
        self.__GPIO_FUNC34_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC34_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC34_OUT_SEL_lsb = 0
        self.__GPIO_FUNC34_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC34_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC34_OEN_INV_SEL_msb, self.__GPIO_FUNC34_OEN_INV_SEL_lsb)
    @GPIO_FUNC34_OEN_INV_SEL.setter
    def GPIO_FUNC34_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC34_OEN_INV_SEL_msb, self.__GPIO_FUNC34_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC34_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC34_OEN_SEL_msb, self.__GPIO_FUNC34_OEN_SEL_lsb)
    @GPIO_FUNC34_OEN_SEL.setter
    def GPIO_FUNC34_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC34_OEN_SEL_msb, self.__GPIO_FUNC34_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC34_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC34_OUT_INV_SEL_msb, self.__GPIO_FUNC34_OUT_INV_SEL_lsb)
    @GPIO_FUNC34_OUT_INV_SEL.setter
    def GPIO_FUNC34_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC34_OUT_INV_SEL_msb, self.__GPIO_FUNC34_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC34_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC34_OUT_SEL_msb, self.__GPIO_FUNC34_OUT_SEL_lsb)
    @GPIO_FUNC34_OUT_SEL.setter
    def GPIO_FUNC34_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC34_OUT_SEL_msb, self.__GPIO_FUNC34_OUT_SEL_lsb, value)
class GPIO_FUNC35_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x5bc
        self.__GPIO_FUNC35_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC35_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC35_OEN_SEL_lsb = 10
        self.__GPIO_FUNC35_OEN_SEL_msb = 10
        self.__GPIO_FUNC35_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC35_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC35_OUT_SEL_lsb = 0
        self.__GPIO_FUNC35_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC35_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC35_OEN_INV_SEL_msb, self.__GPIO_FUNC35_OEN_INV_SEL_lsb)
    @GPIO_FUNC35_OEN_INV_SEL.setter
    def GPIO_FUNC35_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC35_OEN_INV_SEL_msb, self.__GPIO_FUNC35_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC35_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC35_OEN_SEL_msb, self.__GPIO_FUNC35_OEN_SEL_lsb)
    @GPIO_FUNC35_OEN_SEL.setter
    def GPIO_FUNC35_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC35_OEN_SEL_msb, self.__GPIO_FUNC35_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC35_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC35_OUT_INV_SEL_msb, self.__GPIO_FUNC35_OUT_INV_SEL_lsb)
    @GPIO_FUNC35_OUT_INV_SEL.setter
    def GPIO_FUNC35_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC35_OUT_INV_SEL_msb, self.__GPIO_FUNC35_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC35_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC35_OUT_SEL_msb, self.__GPIO_FUNC35_OUT_SEL_lsb)
    @GPIO_FUNC35_OUT_SEL.setter
    def GPIO_FUNC35_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC35_OUT_SEL_msb, self.__GPIO_FUNC35_OUT_SEL_lsb, value)
class GPIO_FUNC36_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x5c0
        self.__GPIO_FUNC36_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC36_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC36_OEN_SEL_lsb = 10
        self.__GPIO_FUNC36_OEN_SEL_msb = 10
        self.__GPIO_FUNC36_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC36_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC36_OUT_SEL_lsb = 0
        self.__GPIO_FUNC36_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC36_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC36_OEN_INV_SEL_msb, self.__GPIO_FUNC36_OEN_INV_SEL_lsb)
    @GPIO_FUNC36_OEN_INV_SEL.setter
    def GPIO_FUNC36_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC36_OEN_INV_SEL_msb, self.__GPIO_FUNC36_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC36_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC36_OEN_SEL_msb, self.__GPIO_FUNC36_OEN_SEL_lsb)
    @GPIO_FUNC36_OEN_SEL.setter
    def GPIO_FUNC36_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC36_OEN_SEL_msb, self.__GPIO_FUNC36_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC36_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC36_OUT_INV_SEL_msb, self.__GPIO_FUNC36_OUT_INV_SEL_lsb)
    @GPIO_FUNC36_OUT_INV_SEL.setter
    def GPIO_FUNC36_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC36_OUT_INV_SEL_msb, self.__GPIO_FUNC36_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC36_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC36_OUT_SEL_msb, self.__GPIO_FUNC36_OUT_SEL_lsb)
    @GPIO_FUNC36_OUT_SEL.setter
    def GPIO_FUNC36_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC36_OUT_SEL_msb, self.__GPIO_FUNC36_OUT_SEL_lsb, value)
class GPIO_FUNC37_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x5c4
        self.__GPIO_FUNC37_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC37_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC37_OEN_SEL_lsb = 10
        self.__GPIO_FUNC37_OEN_SEL_msb = 10
        self.__GPIO_FUNC37_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC37_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC37_OUT_SEL_lsb = 0
        self.__GPIO_FUNC37_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC37_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC37_OEN_INV_SEL_msb, self.__GPIO_FUNC37_OEN_INV_SEL_lsb)
    @GPIO_FUNC37_OEN_INV_SEL.setter
    def GPIO_FUNC37_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC37_OEN_INV_SEL_msb, self.__GPIO_FUNC37_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC37_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC37_OEN_SEL_msb, self.__GPIO_FUNC37_OEN_SEL_lsb)
    @GPIO_FUNC37_OEN_SEL.setter
    def GPIO_FUNC37_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC37_OEN_SEL_msb, self.__GPIO_FUNC37_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC37_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC37_OUT_INV_SEL_msb, self.__GPIO_FUNC37_OUT_INV_SEL_lsb)
    @GPIO_FUNC37_OUT_INV_SEL.setter
    def GPIO_FUNC37_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC37_OUT_INV_SEL_msb, self.__GPIO_FUNC37_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC37_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC37_OUT_SEL_msb, self.__GPIO_FUNC37_OUT_SEL_lsb)
    @GPIO_FUNC37_OUT_SEL.setter
    def GPIO_FUNC37_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC37_OUT_SEL_msb, self.__GPIO_FUNC37_OUT_SEL_lsb, value)
class GPIO_FUNC38_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x5c8
        self.__GPIO_FUNC38_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC38_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC38_OEN_SEL_lsb = 10
        self.__GPIO_FUNC38_OEN_SEL_msb = 10
        self.__GPIO_FUNC38_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC38_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC38_OUT_SEL_lsb = 0
        self.__GPIO_FUNC38_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC38_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC38_OEN_INV_SEL_msb, self.__GPIO_FUNC38_OEN_INV_SEL_lsb)
    @GPIO_FUNC38_OEN_INV_SEL.setter
    def GPIO_FUNC38_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC38_OEN_INV_SEL_msb, self.__GPIO_FUNC38_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC38_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC38_OEN_SEL_msb, self.__GPIO_FUNC38_OEN_SEL_lsb)
    @GPIO_FUNC38_OEN_SEL.setter
    def GPIO_FUNC38_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC38_OEN_SEL_msb, self.__GPIO_FUNC38_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC38_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC38_OUT_INV_SEL_msb, self.__GPIO_FUNC38_OUT_INV_SEL_lsb)
    @GPIO_FUNC38_OUT_INV_SEL.setter
    def GPIO_FUNC38_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC38_OUT_INV_SEL_msb, self.__GPIO_FUNC38_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC38_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC38_OUT_SEL_msb, self.__GPIO_FUNC38_OUT_SEL_lsb)
    @GPIO_FUNC38_OUT_SEL.setter
    def GPIO_FUNC38_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC38_OUT_SEL_msb, self.__GPIO_FUNC38_OUT_SEL_lsb, value)
class GPIO_FUNC39_OUT_SEL_CFG(object):
    def __init__(self, channel, chipv = "CHIP72"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = GPIO_BASE + 0x5cc
        self.__GPIO_FUNC39_OEN_INV_SEL_lsb = 11
        self.__GPIO_FUNC39_OEN_INV_SEL_msb = 11
        self.__GPIO_FUNC39_OEN_SEL_lsb = 10
        self.__GPIO_FUNC39_OEN_SEL_msb = 10
        self.__GPIO_FUNC39_OUT_INV_SEL_lsb = 9
        self.__GPIO_FUNC39_OUT_INV_SEL_msb = 9
        self.__GPIO_FUNC39_OUT_SEL_lsb = 0
        self.__GPIO_FUNC39_OUT_SEL_msb = 8
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def GPIO_FUNC39_OEN_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC39_OEN_INV_SEL_msb, self.__GPIO_FUNC39_OEN_INV_SEL_lsb)
    @GPIO_FUNC39_OEN_INV_SEL.setter
    def GPIO_FUNC39_OEN_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC39_OEN_INV_SEL_msb, self.__GPIO_FUNC39_OEN_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC39_OEN_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC39_OEN_SEL_msb, self.__GPIO_FUNC39_OEN_SEL_lsb)
    @GPIO_FUNC39_OEN_SEL.setter
    def GPIO_FUNC39_OEN_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC39_OEN_SEL_msb, self.__GPIO_FUNC39_OEN_SEL_lsb, value)

    @property
    def GPIO_FUNC39_OUT_INV_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC39_OUT_INV_SEL_msb, self.__GPIO_FUNC39_OUT_INV_SEL_lsb)
    @GPIO_FUNC39_OUT_INV_SEL.setter
    def GPIO_FUNC39_OUT_INV_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC39_OUT_INV_SEL_msb, self.__GPIO_FUNC39_OUT_INV_SEL_lsb, value)

    @property
    def GPIO_FUNC39_OUT_SEL(self):
        return self.__MEM.rdm(self.__addr, self.__GPIO_FUNC39_OUT_SEL_msb, self.__GPIO_FUNC39_OUT_SEL_lsb)
    @GPIO_FUNC39_OUT_SEL.setter
    def GPIO_FUNC39_OUT_SEL(self, value):
        return self.__MEM.wrm(self.__addr, self.__GPIO_FUNC39_OUT_SEL_msb, self.__GPIO_FUNC39_OUT_SEL_lsb, value)
