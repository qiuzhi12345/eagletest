from hal.common import *
from hal.hwregister.hwreg.FPGA724_M1.addr_base import *
class MAC_TXQMEM(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.MACTXIMR2_PLCP1 = MACTXIMR2_PLCP1(self.channel, self.chipv)
        self.MACTXIMR2_PTI = MACTXIMR2_PTI(self.channel, self.chipv)
        self.MACTXIMR2_HTSIG = MACTXIMR2_HTSIG(self.channel, self.chipv)
        self.MACTXIMR2_VHTSIG1 = MACTXIMR2_VHTSIG1(self.channel, self.chipv)
        self.MACTXIMR2_VHTSIG2 = MACTXIMR2_VHTSIG2(self.channel, self.chipv)
        self.MACTXIMR2_HT80LEN = MACTXIMR2_HT80LEN(self.channel, self.chipv)
        self.MACTXIMR2_HT40LEN = MACTXIMR2_HT40LEN(self.channel, self.chipv)
        self.MACTXIMR2_HT20LEN = MACTXIMR2_HT20LEN(self.channel, self.chipv)
        self.MACTXIMR2_DUR = MACTXIMR2_DUR(self.channel, self.chipv)
        self.MACTXIMR2_DUR2 = MACTXIMR2_DUR2(self.channel, self.chipv)
        self.MACTXIMR2PMD = MACTXIMR2PMD(self.channel, self.chipv)
        self.MACTXIMR2BA_BMHI = MACTXIMR2BA_BMHI(self.channel, self.chipv)
        self.MACTXIMR2BA_BMLO = MACTXIMR2BA_BMLO(self.channel, self.chipv)
        self.MACTXIMR2BA_TAHI = MACTXIMR2BA_TAHI(self.channel, self.chipv)
        self.MACTXIMR2BA_TALO = MACTXIMR2BA_TALO(self.channel, self.chipv)
        self.MACTXIMR2BA_SSN = MACTXIMR2BA_SSN(self.channel, self.chipv)
        self.MACTXIMR2_TXSTART_US = MACTXIMR2_TXSTART_US(self.channel, self.chipv)
        self.MACTXIMR2_TXSTART_CYC = MACTXIMR2_TXSTART_CYC(self.channel, self.chipv)
        self.MACTXIMR2_TXRXACK_CYC = MACTXIMR2_TXRXACK_CYC(self.channel, self.chipv)
        self.MACTXIMR1_PLCP1 = MACTXIMR1_PLCP1(self.channel, self.chipv)
        self.MACTXIMR1_PTI = MACTXIMR1_PTI(self.channel, self.chipv)
        self.MACTXIMR1_HTSIG = MACTXIMR1_HTSIG(self.channel, self.chipv)
        self.MACTXIMR1_VHTSIG1 = MACTXIMR1_VHTSIG1(self.channel, self.chipv)
        self.MACTXIMR1_VHTSIG2 = MACTXIMR1_VHTSIG2(self.channel, self.chipv)
        self.MACTXIMR1_HT80LEN = MACTXIMR1_HT80LEN(self.channel, self.chipv)
        self.MACTXIMR1_HT40LEN = MACTXIMR1_HT40LEN(self.channel, self.chipv)
        self.MACTXIMR1_HT20LEN = MACTXIMR1_HT20LEN(self.channel, self.chipv)
        self.MACTXIMR1_DUR = MACTXIMR1_DUR(self.channel, self.chipv)
        self.MACTXIMR1_DUR2 = MACTXIMR1_DUR2(self.channel, self.chipv)
        self.MACTXIMR1PMD = MACTXIMR1PMD(self.channel, self.chipv)
        self.MACTXIMR1BA_BMHI = MACTXIMR1BA_BMHI(self.channel, self.chipv)
        self.MACTXIMR1BA_BMLO = MACTXIMR1BA_BMLO(self.channel, self.chipv)
        self.MACTXIMR1BA_TAHI = MACTXIMR1BA_TAHI(self.channel, self.chipv)
        self.MACTXIMR1BA_TALO = MACTXIMR1BA_TALO(self.channel, self.chipv)
        self.MACTXIMR1BA_SSN = MACTXIMR1BA_SSN(self.channel, self.chipv)
        self.MACTXIMR1_TXSTART_US = MACTXIMR1_TXSTART_US(self.channel, self.chipv)
        self.MACTXIMR1_TXSTART_CYC = MACTXIMR1_TXSTART_CYC(self.channel, self.chipv)
        self.MACTXIMR1_TXRXACK_CYC = MACTXIMR1_TXRXACK_CYC(self.channel, self.chipv)
        self.MACTXIMR0_PLCP1 = MACTXIMR0_PLCP1(self.channel, self.chipv)
        self.MACTXIMR0_PTI = MACTXIMR0_PTI(self.channel, self.chipv)
        self.MACTXIMR0_HTSIG = MACTXIMR0_HTSIG(self.channel, self.chipv)
        self.MACTXIMR0_VHTSIG1 = MACTXIMR0_VHTSIG1(self.channel, self.chipv)
        self.MACTXIMR0_VHTSIG2 = MACTXIMR0_VHTSIG2(self.channel, self.chipv)
        self.MACTXIMR0_HT80LEN = MACTXIMR0_HT80LEN(self.channel, self.chipv)
        self.MACTXIMR0_HT40LEN = MACTXIMR0_HT40LEN(self.channel, self.chipv)
        self.MACTXIMR0_HT20LEN = MACTXIMR0_HT20LEN(self.channel, self.chipv)
        self.MACTXIMR0_DUR = MACTXIMR0_DUR(self.channel, self.chipv)
        self.MACTXIMR0_DUR2 = MACTXIMR0_DUR2(self.channel, self.chipv)
        self.MACTXIMR0PMD = MACTXIMR0PMD(self.channel, self.chipv)
        self.MACTXIMR0BA_BMHI = MACTXIMR0BA_BMHI(self.channel, self.chipv)
        self.MACTXIMR0BA_BMLO = MACTXIMR0BA_BMLO(self.channel, self.chipv)
        self.MACTXIMR0BA_TAHI = MACTXIMR0BA_TAHI(self.channel, self.chipv)
        self.MACTXIMR0BA_TALO = MACTXIMR0BA_TALO(self.channel, self.chipv)
        self.MACTXIMR0BA_SSN = MACTXIMR0BA_SSN(self.channel, self.chipv)
        self.MACTXIMR0_TXSTART_US = MACTXIMR0_TXSTART_US(self.channel, self.chipv)
        self.MACTXIMR0_TXSTART_CYC = MACTXIMR0_TXSTART_CYC(self.channel, self.chipv)
        self.MACTXIMR0_TXRXACK_CYC = MACTXIMR0_TXRXACK_CYC(self.channel, self.chipv)
        self.MACTXQ7_PLCP1 = MACTXQ7_PLCP1(self.channel, self.chipv)
        self.MACTXQ7_PTI = MACTXQ7_PTI(self.channel, self.chipv)
        self.MACTXQ7_HTSIG = MACTXQ7_HTSIG(self.channel, self.chipv)
        self.MACTXQ7_VHTSIG1 = MACTXQ7_VHTSIG1(self.channel, self.chipv)
        self.MACTXQ7_VHTSIG2 = MACTXQ7_VHTSIG2(self.channel, self.chipv)
        self.MACTXQ7_HT80LEN = MACTXQ7_HT80LEN(self.channel, self.chipv)
        self.MACTXQ7_HT40LEN = MACTXQ7_HT40LEN(self.channel, self.chipv)
        self.MACTXQ7_HT20LEN = MACTXQ7_HT20LEN(self.channel, self.chipv)
        self.MACTXQ7_DUR = MACTXQ7_DUR(self.channel, self.chipv)
        self.MACTXQ7_DUR2 = MACTXQ7_DUR2(self.channel, self.chipv)
        self.MACTXQ7PMD = MACTXQ7PMD(self.channel, self.chipv)
        self.MACTXQ7BA_BMHI = MACTXQ7BA_BMHI(self.channel, self.chipv)
        self.MACTXQ7BA_BMLO = MACTXQ7BA_BMLO(self.channel, self.chipv)
        self.MACTXQ7BA_TAHI = MACTXQ7BA_TAHI(self.channel, self.chipv)
        self.MACTXQ7BA_TALO = MACTXQ7BA_TALO(self.channel, self.chipv)
        self.MACTXQ7BA_SSN = MACTXQ7BA_SSN(self.channel, self.chipv)
        self.MACTXQ7_TXSTART_US = MACTXQ7_TXSTART_US(self.channel, self.chipv)
        self.MACTXQ7_TXSTART_CYC = MACTXQ7_TXSTART_CYC(self.channel, self.chipv)
        self.MACTXQ7_TXRXACK_CYC = MACTXQ7_TXRXACK_CYC(self.channel, self.chipv)
        self.MACTXQ6_PLCP1 = MACTXQ6_PLCP1(self.channel, self.chipv)
        self.MACTXQ6_PTI = MACTXQ6_PTI(self.channel, self.chipv)
        self.MACTXQ6_HTSIG = MACTXQ6_HTSIG(self.channel, self.chipv)
        self.MACTXQ6_VHTSIG1 = MACTXQ6_VHTSIG1(self.channel, self.chipv)
        self.MACTXQ6_VHTSIG2 = MACTXQ6_VHTSIG2(self.channel, self.chipv)
        self.MACTXQ6_HT80LEN = MACTXQ6_HT80LEN(self.channel, self.chipv)
        self.MACTXQ6_HT40LEN = MACTXQ6_HT40LEN(self.channel, self.chipv)
        self.MACTXQ6_HT20LEN = MACTXQ6_HT20LEN(self.channel, self.chipv)
        self.MACTXQ6_DUR = MACTXQ6_DUR(self.channel, self.chipv)
        self.MACTXQ6_DUR2 = MACTXQ6_DUR2(self.channel, self.chipv)
        self.MACTXQ6PMD = MACTXQ6PMD(self.channel, self.chipv)
        self.MACTXQ6BA_BMHI = MACTXQ6BA_BMHI(self.channel, self.chipv)
        self.MACTXQ6BA_BMLO = MACTXQ6BA_BMLO(self.channel, self.chipv)
        self.MACTXQ6BA_TAHI = MACTXQ6BA_TAHI(self.channel, self.chipv)
        self.MACTXQ6BA_TALO = MACTXQ6BA_TALO(self.channel, self.chipv)
        self.MACTXQ6BA_SSN = MACTXQ6BA_SSN(self.channel, self.chipv)
        self.MACTXQ6_TXSTART_US = MACTXQ6_TXSTART_US(self.channel, self.chipv)
        self.MACTXQ6_TXSTART_CYC = MACTXQ6_TXSTART_CYC(self.channel, self.chipv)
        self.MACTXQ6_TXRXACK_CYC = MACTXQ6_TXRXACK_CYC(self.channel, self.chipv)
        self.MACTXQ5_PLCP1 = MACTXQ5_PLCP1(self.channel, self.chipv)
        self.MACTXQ5_PTI = MACTXQ5_PTI(self.channel, self.chipv)
        self.MACTXQ5_HTSIG = MACTXQ5_HTSIG(self.channel, self.chipv)
        self.MACTXQ5_VHTSIG1 = MACTXQ5_VHTSIG1(self.channel, self.chipv)
        self.MACTXQ5_VHTSIG2 = MACTXQ5_VHTSIG2(self.channel, self.chipv)
        self.MACTXQ5_HT80LEN = MACTXQ5_HT80LEN(self.channel, self.chipv)
        self.MACTXQ5_HT40LEN = MACTXQ5_HT40LEN(self.channel, self.chipv)
        self.MACTXQ5_HT20LEN = MACTXQ5_HT20LEN(self.channel, self.chipv)
        self.MACTXQ5_DUR = MACTXQ5_DUR(self.channel, self.chipv)
        self.MACTXQ5_DUR2 = MACTXQ5_DUR2(self.channel, self.chipv)
        self.MACTXQ5PMD = MACTXQ5PMD(self.channel, self.chipv)
        self.MACTXQ5BA_BMHI = MACTXQ5BA_BMHI(self.channel, self.chipv)
        self.MACTXQ5BA_BMLO = MACTXQ5BA_BMLO(self.channel, self.chipv)
        self.MACTXQ5BA_TAHI = MACTXQ5BA_TAHI(self.channel, self.chipv)
        self.MACTXQ5BA_TALO = MACTXQ5BA_TALO(self.channel, self.chipv)
        self.MACTXQ5BA_SSN = MACTXQ5BA_SSN(self.channel, self.chipv)
        self.MACTXQ5_TXSTART_US = MACTXQ5_TXSTART_US(self.channel, self.chipv)
        self.MACTXQ5_TXSTART_CYC = MACTXQ5_TXSTART_CYC(self.channel, self.chipv)
        self.MACTXQ5_TXRXACK_CYC = MACTXQ5_TXRXACK_CYC(self.channel, self.chipv)
        self.MACTXQ4_PLCP1 = MACTXQ4_PLCP1(self.channel, self.chipv)
        self.MACTXQ4_PTI = MACTXQ4_PTI(self.channel, self.chipv)
        self.MACTXQ4_HTSIG = MACTXQ4_HTSIG(self.channel, self.chipv)
        self.MACTXQ4_VHTSIG1 = MACTXQ4_VHTSIG1(self.channel, self.chipv)
        self.MACTXQ4_VHTSIG2 = MACTXQ4_VHTSIG2(self.channel, self.chipv)
        self.MACTXQ4_HT80LEN = MACTXQ4_HT80LEN(self.channel, self.chipv)
        self.MACTXQ4_HT40LEN = MACTXQ4_HT40LEN(self.channel, self.chipv)
        self.MACTXQ4_HT20LEN = MACTXQ4_HT20LEN(self.channel, self.chipv)
        self.MACTXQ4_DUR = MACTXQ4_DUR(self.channel, self.chipv)
        self.MACTXQ4_DUR2 = MACTXQ4_DUR2(self.channel, self.chipv)
        self.MACTXQ4PMD = MACTXQ4PMD(self.channel, self.chipv)
        self.MACTXQ4BA_BMHI = MACTXQ4BA_BMHI(self.channel, self.chipv)
        self.MACTXQ4BA_BMLO = MACTXQ4BA_BMLO(self.channel, self.chipv)
        self.MACTXQ4BA_TAHI = MACTXQ4BA_TAHI(self.channel, self.chipv)
        self.MACTXQ4BA_TALO = MACTXQ4BA_TALO(self.channel, self.chipv)
        self.MACTXQ4BA_SSN = MACTXQ4BA_SSN(self.channel, self.chipv)
        self.MACTXQ4_TXSTART_US = MACTXQ4_TXSTART_US(self.channel, self.chipv)
        self.MACTXQ4_TXSTART_CYC = MACTXQ4_TXSTART_CYC(self.channel, self.chipv)
        self.MACTXQ4_TXRXACK_CYC = MACTXQ4_TXRXACK_CYC(self.channel, self.chipv)
        self.MACTXQ3_PLCP1 = MACTXQ3_PLCP1(self.channel, self.chipv)
        self.MACTXQ3_PTI = MACTXQ3_PTI(self.channel, self.chipv)
        self.MACTXQ3_HTSIG = MACTXQ3_HTSIG(self.channel, self.chipv)
        self.MACTXQ3_VHTSIG1 = MACTXQ3_VHTSIG1(self.channel, self.chipv)
        self.MACTXQ3_VHTSIG2 = MACTXQ3_VHTSIG2(self.channel, self.chipv)
        self.MACTXQ3_HT80LEN = MACTXQ3_HT80LEN(self.channel, self.chipv)
        self.MACTXQ3_HT40LEN = MACTXQ3_HT40LEN(self.channel, self.chipv)
        self.MACTXQ3_HT20LEN = MACTXQ3_HT20LEN(self.channel, self.chipv)
        self.MACTXQ3_DUR = MACTXQ3_DUR(self.channel, self.chipv)
        self.MACTXQ3_DUR2 = MACTXQ3_DUR2(self.channel, self.chipv)
        self.MACTXQ3PMD = MACTXQ3PMD(self.channel, self.chipv)
        self.MACTXQ3BA_BMHI = MACTXQ3BA_BMHI(self.channel, self.chipv)
        self.MACTXQ3BA_BMLO = MACTXQ3BA_BMLO(self.channel, self.chipv)
        self.MACTXQ3BA_TAHI = MACTXQ3BA_TAHI(self.channel, self.chipv)
        self.MACTXQ3BA_TALO = MACTXQ3BA_TALO(self.channel, self.chipv)
        self.MACTXQ3BA_SSN = MACTXQ3BA_SSN(self.channel, self.chipv)
        self.MACTXQ3_TXSTART_US = MACTXQ3_TXSTART_US(self.channel, self.chipv)
        self.MACTXQ3_TXSTART_CYC = MACTXQ3_TXSTART_CYC(self.channel, self.chipv)
        self.MACTXQ3_TXRXACK_CYC = MACTXQ3_TXRXACK_CYC(self.channel, self.chipv)
        self.MACTXQ2_PLCP1 = MACTXQ2_PLCP1(self.channel, self.chipv)
        self.MACTXQ2_PTI = MACTXQ2_PTI(self.channel, self.chipv)
        self.MACTXQ2_HTSIG = MACTXQ2_HTSIG(self.channel, self.chipv)
        self.MACTXQ2_VHTSIG1 = MACTXQ2_VHTSIG1(self.channel, self.chipv)
        self.MACTXQ2_VHTSIG2 = MACTXQ2_VHTSIG2(self.channel, self.chipv)
        self.MACTXQ2_HT80LEN = MACTXQ2_HT80LEN(self.channel, self.chipv)
        self.MACTXQ2_HT40LEN = MACTXQ2_HT40LEN(self.channel, self.chipv)
        self.MACTXQ2_HT20LEN = MACTXQ2_HT20LEN(self.channel, self.chipv)
        self.MACTXQ2_DUR = MACTXQ2_DUR(self.channel, self.chipv)
        self.MACTXQ2_DUR2 = MACTXQ2_DUR2(self.channel, self.chipv)
        self.MACTXQ2PMD = MACTXQ2PMD(self.channel, self.chipv)
        self.MACTXQ2BA_BMHI = MACTXQ2BA_BMHI(self.channel, self.chipv)
        self.MACTXQ2BA_BMLO = MACTXQ2BA_BMLO(self.channel, self.chipv)
        self.MACTXQ2BA_TAHI = MACTXQ2BA_TAHI(self.channel, self.chipv)
        self.MACTXQ2BA_TALO = MACTXQ2BA_TALO(self.channel, self.chipv)
        self.MACTXQ2BA_SSN = MACTXQ2BA_SSN(self.channel, self.chipv)
        self.MACTXQ2_TXSTART_US = MACTXQ2_TXSTART_US(self.channel, self.chipv)
        self.MACTXQ2_TXSTART_CYC = MACTXQ2_TXSTART_CYC(self.channel, self.chipv)
        self.MACTXQ2_TXRXACK_CYC = MACTXQ2_TXRXACK_CYC(self.channel, self.chipv)
        self.MACTXQ1_PLCP1 = MACTXQ1_PLCP1(self.channel, self.chipv)
        self.MACTXQ1_PTI = MACTXQ1_PTI(self.channel, self.chipv)
        self.MACTXQ1_HTSIG = MACTXQ1_HTSIG(self.channel, self.chipv)
        self.MACTXQ1_VHTSIG1 = MACTXQ1_VHTSIG1(self.channel, self.chipv)
        self.MACTXQ1_VHTSIG2 = MACTXQ1_VHTSIG2(self.channel, self.chipv)
        self.MACTXQ1_HT80LEN = MACTXQ1_HT80LEN(self.channel, self.chipv)
        self.MACTXQ1_HT40LEN = MACTXQ1_HT40LEN(self.channel, self.chipv)
        self.MACTXQ1_HT20LEN = MACTXQ1_HT20LEN(self.channel, self.chipv)
        self.MACTXQ1_DUR = MACTXQ1_DUR(self.channel, self.chipv)
        self.MACTXQ1_DUR2 = MACTXQ1_DUR2(self.channel, self.chipv)
        self.MACTXQ1PMD = MACTXQ1PMD(self.channel, self.chipv)
        self.MACTXQ1BA_BMHI = MACTXQ1BA_BMHI(self.channel, self.chipv)
        self.MACTXQ1BA_BMLO = MACTXQ1BA_BMLO(self.channel, self.chipv)
        self.MACTXQ1BA_TAHI = MACTXQ1BA_TAHI(self.channel, self.chipv)
        self.MACTXQ1BA_TALO = MACTXQ1BA_TALO(self.channel, self.chipv)
        self.MACTXQ1BA_SSN = MACTXQ1BA_SSN(self.channel, self.chipv)
        self.MACTXQ1_TXSTART_US = MACTXQ1_TXSTART_US(self.channel, self.chipv)
        self.MACTXQ1_TXSTART_CYC = MACTXQ1_TXSTART_CYC(self.channel, self.chipv)
        self.MACTXQ1_TXRXACK_CYC = MACTXQ1_TXRXACK_CYC(self.channel, self.chipv)
        self.MACTXQ0_PLCP1 = MACTXQ0_PLCP1(self.channel, self.chipv)
        self.MACTXQ0_PTI = MACTXQ0_PTI(self.channel, self.chipv)
        self.MACTXQ0_HTSIG = MACTXQ0_HTSIG(self.channel, self.chipv)
        self.MACTXQ0_VHTSIG1 = MACTXQ0_VHTSIG1(self.channel, self.chipv)
        self.MACTXQ0_VHTSIG2 = MACTXQ0_VHTSIG2(self.channel, self.chipv)
        self.MACTXQ0_HT80LEN = MACTXQ0_HT80LEN(self.channel, self.chipv)
        self.MACTXQ0_HT40LEN = MACTXQ0_HT40LEN(self.channel, self.chipv)
        self.MACTXQ0_HT20LEN = MACTXQ0_HT20LEN(self.channel, self.chipv)
        self.MACTXQ0_DUR = MACTXQ0_DUR(self.channel, self.chipv)
        self.MACTXQ0_DUR2 = MACTXQ0_DUR2(self.channel, self.chipv)
        self.MACTXQ0PMD = MACTXQ0PMD(self.channel, self.chipv)
        self.MACTXQ0BA_BMHI = MACTXQ0BA_BMHI(self.channel, self.chipv)
        self.MACTXQ0BA_BMLO = MACTXQ0BA_BMLO(self.channel, self.chipv)
        self.MACTXQ0BA_TAHI = MACTXQ0BA_TAHI(self.channel, self.chipv)
        self.MACTXQ0BA_TALO = MACTXQ0BA_TALO(self.channel, self.chipv)
        self.MACTXQ0BA_SSN = MACTXQ0BA_SSN(self.channel, self.chipv)
        self.MACTXQ0_TXSTART_US = MACTXQ0_TXSTART_US(self.channel, self.chipv)
        self.MACTXQ0_TXSTART_CYC = MACTXQ0_TXSTART_CYC(self.channel, self.chipv)
        self.MACTXQ0_TXRXACK_CYC = MACTXQ0_TXRXACK_CYC(self.channel, self.chipv)
        self.MACTXOP0_Q15_PLCP0 = MACTXOP0_Q15_PLCP0(self.channel, self.chipv)
        self.MACTXOP0_Q14_PLCP0 = MACTXOP0_Q14_PLCP0(self.channel, self.chipv)
        self.MACTXOP0_Q13_PLCP0 = MACTXOP0_Q13_PLCP0(self.channel, self.chipv)
        self.MACTXOP0_Q12_PLCP0 = MACTXOP0_Q12_PLCP0(self.channel, self.chipv)
        self.MACTXOP0_Q11_PLCP0 = MACTXOP0_Q11_PLCP0(self.channel, self.chipv)
        self.MACTXOP0_Q10_PLCP0 = MACTXOP0_Q10_PLCP0(self.channel, self.chipv)
        self.MACTXOP0_Q9_PLCP0 = MACTXOP0_Q9_PLCP0(self.channel, self.chipv)
        self.MACTXOP0_Q8_PLCP0 = MACTXOP0_Q8_PLCP0(self.channel, self.chipv)
        self.MACTXOP0_Q7_PLCP0 = MACTXOP0_Q7_PLCP0(self.channel, self.chipv)
        self.MACTXOP0_Q6_PLCP0 = MACTXOP0_Q6_PLCP0(self.channel, self.chipv)
        self.MACTXOP0_Q5_PLCP0 = MACTXOP0_Q5_PLCP0(self.channel, self.chipv)
        self.MACTXOP0_Q4_PLCP0 = MACTXOP0_Q4_PLCP0(self.channel, self.chipv)
        self.MACTXOP0_Q3_PLCP0 = MACTXOP0_Q3_PLCP0(self.channel, self.chipv)
        self.MACTXOP0_Q2_PLCP0 = MACTXOP0_Q2_PLCP0(self.channel, self.chipv)
        self.MACTXOP0_Q1_PLCP0 = MACTXOP0_Q1_PLCP0(self.channel, self.chipv)
        self.MACTXOP1_Q15_PLCP0 = MACTXOP1_Q15_PLCP0(self.channel, self.chipv)
        self.MACTXOP1_Q14_PLCP0 = MACTXOP1_Q14_PLCP0(self.channel, self.chipv)
        self.MACTXOP1_Q13_PLCP0 = MACTXOP1_Q13_PLCP0(self.channel, self.chipv)
        self.MACTXOP1_Q12_PLCP0 = MACTXOP1_Q12_PLCP0(self.channel, self.chipv)
        self.MACTXOP1_Q11_PLCP0 = MACTXOP1_Q11_PLCP0(self.channel, self.chipv)
        self.MACTXOP1_Q10_PLCP0 = MACTXOP1_Q10_PLCP0(self.channel, self.chipv)
        self.MACTXOP1_Q9_PLCP0 = MACTXOP1_Q9_PLCP0(self.channel, self.chipv)
        self.MACTXOP1_Q8_PLCP0 = MACTXOP1_Q8_PLCP0(self.channel, self.chipv)
        self.MACTXOP1_Q7_PLCP0 = MACTXOP1_Q7_PLCP0(self.channel, self.chipv)
        self.MACTXOP1_Q6_PLCP0 = MACTXOP1_Q6_PLCP0(self.channel, self.chipv)
        self.MACTXOP1_Q5_PLCP0 = MACTXOP1_Q5_PLCP0(self.channel, self.chipv)
        self.MACTXOP1_Q4_PLCP0 = MACTXOP1_Q4_PLCP0(self.channel, self.chipv)
        self.MACTXOP1_Q3_PLCP0 = MACTXOP1_Q3_PLCP0(self.channel, self.chipv)
        self.MACTXOP1_Q2_PLCP0 = MACTXOP1_Q2_PLCP0(self.channel, self.chipv)
        self.MACTXOP1_Q1_PLCP0 = MACTXOP1_Q1_PLCP0(self.channel, self.chipv)
        self.MACTXOP2_Q15_PLCP0 = MACTXOP2_Q15_PLCP0(self.channel, self.chipv)
        self.MACTXOP2_Q14_PLCP0 = MACTXOP2_Q14_PLCP0(self.channel, self.chipv)
        self.MACTXOP2_Q13_PLCP0 = MACTXOP2_Q13_PLCP0(self.channel, self.chipv)
        self.MACTXOP2_Q12_PLCP0 = MACTXOP2_Q12_PLCP0(self.channel, self.chipv)
        self.MACTXOP2_Q11_PLCP0 = MACTXOP2_Q11_PLCP0(self.channel, self.chipv)
        self.MACTXOP2_Q10_PLCP0 = MACTXOP2_Q10_PLCP0(self.channel, self.chipv)
        self.MACTXOP2_Q9_PLCP0 = MACTXOP2_Q9_PLCP0(self.channel, self.chipv)
        self.MACTXOP2_Q8_PLCP0 = MACTXOP2_Q8_PLCP0(self.channel, self.chipv)
        self.MACTXOP2_Q7_PLCP0 = MACTXOP2_Q7_PLCP0(self.channel, self.chipv)
        self.MACTXOP2_Q6_PLCP0 = MACTXOP2_Q6_PLCP0(self.channel, self.chipv)
        self.MACTXOP2_Q5_PLCP0 = MACTXOP2_Q5_PLCP0(self.channel, self.chipv)
        self.MACTXOP2_Q4_PLCP0 = MACTXOP2_Q4_PLCP0(self.channel, self.chipv)
        self.MACTXOP2_Q3_PLCP0 = MACTXOP2_Q3_PLCP0(self.channel, self.chipv)
        self.MACTXOP2_Q2_PLCP0 = MACTXOP2_Q2_PLCP0(self.channel, self.chipv)
        self.MACTXOP2_Q1_PLCP0 = MACTXOP2_Q1_PLCP0(self.channel, self.chipv)
        self.MACTXMEMQDATE = MACTXMEMQDATE(self.channel, self.chipv)
class MACTXIMR2_PLCP1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x0
        self.__reg_tximr2_data_wbd_lsb = 31
        self.__reg_tximr2_data_wbd_msb = 31
        self.__reg_tximr2_rts_wbd_lsb = 30
        self.__reg_tximr2_rts_wbd_msb = 30
        self.__reg_tximr2_force_bw_lsb = 29
        self.__reg_tximr2_force_bw_msb = 29
        self.__reg_tximr2_nonhtdup_lsb = 27
        self.__reg_tximr2_nonhtdup_msb = 28
        self.__reg_tximr2_sigmode_lsb = 25
        self.__reg_tximr2_sigmode_msb = 26
        self.__reg_tximr2_kid_lsb = 17
        self.__reg_tximr2_kid_msb = 24
        self.__reg_tximr2_rate_lsb = 12
        self.__reg_tximr2_rate_msb = 16
        self.__reg_tximr2_length_lsb = 0
        self.__reg_tximr2_length_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr2_data_wbd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_data_wbd_msb, self.__reg_tximr2_data_wbd_lsb)
    @reg_tximr2_data_wbd.setter
    def reg_tximr2_data_wbd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_data_wbd_msb, self.__reg_tximr2_data_wbd_lsb, value)

    @property
    def reg_tximr2_rts_wbd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_rts_wbd_msb, self.__reg_tximr2_rts_wbd_lsb)
    @reg_tximr2_rts_wbd.setter
    def reg_tximr2_rts_wbd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_rts_wbd_msb, self.__reg_tximr2_rts_wbd_lsb, value)

    @property
    def reg_tximr2_force_bw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_force_bw_msb, self.__reg_tximr2_force_bw_lsb)
    @reg_tximr2_force_bw.setter
    def reg_tximr2_force_bw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_force_bw_msb, self.__reg_tximr2_force_bw_lsb, value)

    @property
    def reg_tximr2_nonhtdup(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_nonhtdup_msb, self.__reg_tximr2_nonhtdup_lsb)
    @reg_tximr2_nonhtdup.setter
    def reg_tximr2_nonhtdup(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_nonhtdup_msb, self.__reg_tximr2_nonhtdup_lsb, value)

    @property
    def reg_tximr2_sigmode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_sigmode_msb, self.__reg_tximr2_sigmode_lsb)
    @reg_tximr2_sigmode.setter
    def reg_tximr2_sigmode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_sigmode_msb, self.__reg_tximr2_sigmode_lsb, value)

    @property
    def reg_tximr2_kid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_kid_msb, self.__reg_tximr2_kid_lsb)
    @reg_tximr2_kid.setter
    def reg_tximr2_kid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_kid_msb, self.__reg_tximr2_kid_lsb, value)

    @property
    def reg_tximr2_rate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_rate_msb, self.__reg_tximr2_rate_lsb)
    @reg_tximr2_rate.setter
    def reg_tximr2_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_rate_msb, self.__reg_tximr2_rate_lsb, value)

    @property
    def reg_tximr2_length(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_length_msb, self.__reg_tximr2_length_lsb)
    @reg_tximr2_length.setter
    def reg_tximr2_length(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_length_msb, self.__reg_tximr2_length_lsb, value)
class MACTXIMR2_PTI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x4
        self.__reg_tximr2_pti_maintain_cnt_lsb = 20
        self.__reg_tximr2_pti_maintain_cnt_msb = 31
        self.__reg_tximr2_maintain_pti_lsb = 16
        self.__reg_tximr2_maintain_pti_msb = 19
        self.__reg_tximr2_rts_pti_lsb = 12
        self.__reg_tximr2_rts_pti_msb = 15
        self.__reg_tximr2_data_pti_lsb = 8
        self.__reg_tximr2_data_pti_msb = 11
        self.__reg_tximr2_ack_pti_lsb = 4
        self.__reg_tximr2_ack_pti_msb = 7
        self.__reg_tximr2_bssid_lsb = 0
        self.__reg_tximr2_bssid_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr2_pti_maintain_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_pti_maintain_cnt_msb, self.__reg_tximr2_pti_maintain_cnt_lsb)
    @reg_tximr2_pti_maintain_cnt.setter
    def reg_tximr2_pti_maintain_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_pti_maintain_cnt_msb, self.__reg_tximr2_pti_maintain_cnt_lsb, value)

    @property
    def reg_tximr2_maintain_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_maintain_pti_msb, self.__reg_tximr2_maintain_pti_lsb)
    @reg_tximr2_maintain_pti.setter
    def reg_tximr2_maintain_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_maintain_pti_msb, self.__reg_tximr2_maintain_pti_lsb, value)

    @property
    def reg_tximr2_rts_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_rts_pti_msb, self.__reg_tximr2_rts_pti_lsb)
    @reg_tximr2_rts_pti.setter
    def reg_tximr2_rts_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_rts_pti_msb, self.__reg_tximr2_rts_pti_lsb, value)

    @property
    def reg_tximr2_data_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_data_pti_msb, self.__reg_tximr2_data_pti_lsb)
    @reg_tximr2_data_pti.setter
    def reg_tximr2_data_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_data_pti_msb, self.__reg_tximr2_data_pti_lsb, value)

    @property
    def reg_tximr2_ack_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_ack_pti_msb, self.__reg_tximr2_ack_pti_lsb)
    @reg_tximr2_ack_pti.setter
    def reg_tximr2_ack_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_ack_pti_msb, self.__reg_tximr2_ack_pti_lsb, value)

    @property
    def reg_tximr2_bssid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_bssid_msb, self.__reg_tximr2_bssid_lsb)
    @reg_tximr2_bssid.setter
    def reg_tximr2_bssid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_bssid_msb, self.__reg_tximr2_bssid_lsb, value)
class MACTXIMR2_HTSIG(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x8
        self.__reg_tximr2_htsig_lsb = 0
        self.__reg_tximr2_htsig_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr2_htsig(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_htsig_msb, self.__reg_tximr2_htsig_lsb)
    @reg_tximr2_htsig.setter
    def reg_tximr2_htsig(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_htsig_msb, self.__reg_tximr2_htsig_lsb, value)
class MACTXIMR2_VHTSIG1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0xc
        self.__reg_tximr2_vhtsiga_lo_lsb = 0
        self.__reg_tximr2_vhtsiga_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr2_vhtsiga_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_vhtsiga_lo_msb, self.__reg_tximr2_vhtsiga_lo_lsb)
    @reg_tximr2_vhtsiga_lo.setter
    def reg_tximr2_vhtsiga_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_vhtsiga_lo_msb, self.__reg_tximr2_vhtsiga_lo_lsb, value)
class MACTXIMR2_VHTSIG2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x10
        self.__reg_tximr2_vhtsigb_lsb = 2
        self.__reg_tximr2_vhtsigb_msb = 24
        self.__reg_tximr2_vhtsiga_hi_lsb = 0
        self.__reg_tximr2_vhtsiga_hi_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr2_vhtsigb(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_vhtsigb_msb, self.__reg_tximr2_vhtsigb_lsb)
    @reg_tximr2_vhtsigb.setter
    def reg_tximr2_vhtsigb(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_vhtsigb_msb, self.__reg_tximr2_vhtsigb_lsb, value)

    @property
    def reg_tximr2_vhtsiga_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_vhtsiga_hi_msb, self.__reg_tximr2_vhtsiga_hi_lsb)
    @reg_tximr2_vhtsiga_hi.setter
    def reg_tximr2_vhtsiga_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_vhtsiga_hi_msb, self.__reg_tximr2_vhtsiga_hi_lsb, value)
class MACTXIMR2_HT80LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x14
        self.__reg_tximr2_ht80txop_num_lsb = 24
        self.__reg_tximr2_ht80txop_num_msb = 27
        self.__reg_tximr2_ht80eof_num_lsb = 22
        self.__reg_tximr2_ht80eof_num_msb = 23
        self.__reg_tximr2_ht80len_lsb = 0
        self.__reg_tximr2_ht80len_msb = 20
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr2_ht80txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_ht80txop_num_msb, self.__reg_tximr2_ht80txop_num_lsb)
    @reg_tximr2_ht80txop_num.setter
    def reg_tximr2_ht80txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_ht80txop_num_msb, self.__reg_tximr2_ht80txop_num_lsb, value)

    @property
    def reg_tximr2_ht80eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_ht80eof_num_msb, self.__reg_tximr2_ht80eof_num_lsb)
    @reg_tximr2_ht80eof_num.setter
    def reg_tximr2_ht80eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_ht80eof_num_msb, self.__reg_tximr2_ht80eof_num_lsb, value)

    @property
    def reg_tximr2_ht80len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_ht80len_msb, self.__reg_tximr2_ht80len_lsb)
    @reg_tximr2_ht80len.setter
    def reg_tximr2_ht80len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_ht80len_msb, self.__reg_tximr2_ht80len_lsb, value)
class MACTXIMR2_HT40LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x18
        self.__reg_tximr2_ht40txop_num_lsb = 24
        self.__reg_tximr2_ht40txop_num_msb = 27
        self.__reg_tximr2_ht40eof_num_lsb = 22
        self.__reg_tximr2_ht40eof_num_msb = 23
        self.__reg_tximr2_ht40len_lsb = 0
        self.__reg_tximr2_ht40len_msb = 18
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr2_ht40txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_ht40txop_num_msb, self.__reg_tximr2_ht40txop_num_lsb)
    @reg_tximr2_ht40txop_num.setter
    def reg_tximr2_ht40txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_ht40txop_num_msb, self.__reg_tximr2_ht40txop_num_lsb, value)

    @property
    def reg_tximr2_ht40eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_ht40eof_num_msb, self.__reg_tximr2_ht40eof_num_lsb)
    @reg_tximr2_ht40eof_num.setter
    def reg_tximr2_ht40eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_ht40eof_num_msb, self.__reg_tximr2_ht40eof_num_lsb, value)

    @property
    def reg_tximr2_ht40len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_ht40len_msb, self.__reg_tximr2_ht40len_lsb)
    @reg_tximr2_ht40len.setter
    def reg_tximr2_ht40len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_ht40len_msb, self.__reg_tximr2_ht40len_lsb, value)
class MACTXIMR2_HT20LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x1c
        self.__reg_tximr2_txop_sel_lsb = 28
        self.__reg_tximr2_txop_sel_msb = 29
        self.__reg_tximr2_20txop_num_lsb = 24
        self.__reg_tximr2_20txop_num_msb = 27
        self.__reg_tximr2_20eof_num_lsb = 22
        self.__reg_tximr2_20eof_num_msb = 23
        self.__reg_tximr2_rts_rate_lsb = 6
        self.__reg_tximr2_rts_rate_msb = 13
        self.__reg_tximr2_ant_force_lsb = 5
        self.__reg_tximr2_ant_force_msb = 5
        self.__reg_tximr2_ant_force_value_lsb = 4
        self.__reg_tximr2_ant_force_value_msb = 4
        self.__reg_tximr2_ant_force_last_lsb = 3
        self.__reg_tximr2_ant_force_last_msb = 3
        self.__reg_txrximr2_ant_force_lsb = 2
        self.__reg_txrximr2_ant_force_msb = 2
        self.__reg_txrximr2_ant_force_value_lsb = 1
        self.__reg_txrximr2_ant_force_value_msb = 1
        self.__reg_txrximr2_ant_force_last_lsb = 0
        self.__reg_txrximr2_ant_force_last_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr2_txop_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_txop_sel_msb, self.__reg_tximr2_txop_sel_lsb)
    @reg_tximr2_txop_sel.setter
    def reg_tximr2_txop_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_txop_sel_msb, self.__reg_tximr2_txop_sel_lsb, value)

    @property
    def reg_tximr2_20txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_20txop_num_msb, self.__reg_tximr2_20txop_num_lsb)
    @reg_tximr2_20txop_num.setter
    def reg_tximr2_20txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_20txop_num_msb, self.__reg_tximr2_20txop_num_lsb, value)

    @property
    def reg_tximr2_20eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_20eof_num_msb, self.__reg_tximr2_20eof_num_lsb)
    @reg_tximr2_20eof_num.setter
    def reg_tximr2_20eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_20eof_num_msb, self.__reg_tximr2_20eof_num_lsb, value)

    @property
    def reg_tximr2_rts_rate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_rts_rate_msb, self.__reg_tximr2_rts_rate_lsb)
    @reg_tximr2_rts_rate.setter
    def reg_tximr2_rts_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_rts_rate_msb, self.__reg_tximr2_rts_rate_lsb, value)

    @property
    def reg_tximr2_ant_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_ant_force_msb, self.__reg_tximr2_ant_force_lsb)
    @reg_tximr2_ant_force.setter
    def reg_tximr2_ant_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_ant_force_msb, self.__reg_tximr2_ant_force_lsb, value)

    @property
    def reg_tximr2_ant_force_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_ant_force_value_msb, self.__reg_tximr2_ant_force_value_lsb)
    @reg_tximr2_ant_force_value.setter
    def reg_tximr2_ant_force_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_ant_force_value_msb, self.__reg_tximr2_ant_force_value_lsb, value)

    @property
    def reg_tximr2_ant_force_last(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_ant_force_last_msb, self.__reg_tximr2_ant_force_last_lsb)
    @reg_tximr2_ant_force_last.setter
    def reg_tximr2_ant_force_last(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_ant_force_last_msb, self.__reg_tximr2_ant_force_last_lsb, value)

    @property
    def reg_txrximr2_ant_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrximr2_ant_force_msb, self.__reg_txrximr2_ant_force_lsb)
    @reg_txrximr2_ant_force.setter
    def reg_txrximr2_ant_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrximr2_ant_force_msb, self.__reg_txrximr2_ant_force_lsb, value)

    @property
    def reg_txrximr2_ant_force_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrximr2_ant_force_value_msb, self.__reg_txrximr2_ant_force_value_lsb)
    @reg_txrximr2_ant_force_value.setter
    def reg_txrximr2_ant_force_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrximr2_ant_force_value_msb, self.__reg_txrximr2_ant_force_value_lsb, value)

    @property
    def reg_txrximr2_ant_force_last(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrximr2_ant_force_last_msb, self.__reg_txrximr2_ant_force_last_lsb)
    @reg_txrximr2_ant_force_last.setter
    def reg_txrximr2_ant_force_last(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrximr2_ant_force_last_msb, self.__reg_txrximr2_ant_force_last_lsb, value)
class MACTXIMR2_DUR(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x20
        self.__reg_tximr2_20dur_lsb = 16
        self.__reg_tximr2_20dur_msb = 31
        self.__reg_tximr2_ht40dur_lsb = 0
        self.__reg_tximr2_ht40dur_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr2_20dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_20dur_msb, self.__reg_tximr2_20dur_lsb)
    @reg_tximr2_20dur.setter
    def reg_tximr2_20dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_20dur_msb, self.__reg_tximr2_20dur_lsb, value)

    @property
    def reg_tximr2_ht40dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_ht40dur_msb, self.__reg_tximr2_ht40dur_lsb)
    @reg_tximr2_ht40dur.setter
    def reg_tximr2_ht40dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_ht40dur_msb, self.__reg_tximr2_ht40dur_lsb, value)
class MACTXIMR2_DUR2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x24
        self.__reg_tximr2_hwseq_fgmd_lsb = 31
        self.__reg_tximr2_hwseq_fgmd_msb = 31
        self.__reg_tximr2_hwseq_qmfmd_lsb = 29
        self.__reg_tximr2_hwseq_qmfmd_msb = 29
        self.__reg_tximr2_hwseq_sel_lsb = 17
        self.__reg_tximr2_hwseq_sel_msb = 19
        self.__reg_tximr2_hwseq_update_lsb = 16
        self.__reg_tximr2_hwseq_update_msb = 16
        self.__reg_tximr2_ht80dur_lsb = 0
        self.__reg_tximr2_ht80dur_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr2_hwseq_fgmd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_hwseq_fgmd_msb, self.__reg_tximr2_hwseq_fgmd_lsb)
    @reg_tximr2_hwseq_fgmd.setter
    def reg_tximr2_hwseq_fgmd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_hwseq_fgmd_msb, self.__reg_tximr2_hwseq_fgmd_lsb, value)

    @property
    def reg_tximr2_hwseq_qmfmd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_hwseq_qmfmd_msb, self.__reg_tximr2_hwseq_qmfmd_lsb)
    @reg_tximr2_hwseq_qmfmd.setter
    def reg_tximr2_hwseq_qmfmd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_hwseq_qmfmd_msb, self.__reg_tximr2_hwseq_qmfmd_lsb, value)

    @property
    def reg_tximr2_hwseq_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_hwseq_sel_msb, self.__reg_tximr2_hwseq_sel_lsb)
    @reg_tximr2_hwseq_sel.setter
    def reg_tximr2_hwseq_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_hwseq_sel_msb, self.__reg_tximr2_hwseq_sel_lsb, value)

    @property
    def reg_tximr2_hwseq_update(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_hwseq_update_msb, self.__reg_tximr2_hwseq_update_lsb)
    @reg_tximr2_hwseq_update.setter
    def reg_tximr2_hwseq_update(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_hwseq_update_msb, self.__reg_tximr2_hwseq_update_lsb, value)
    @property
    def default_value(self):
        return 0x0

    @property
    def reg_tximr2_ht80dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr2_ht80dur_msb, self.__reg_tximr2_ht80dur_lsb)
    @reg_tximr2_ht80dur.setter
    def reg_tximr2_ht80dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr2_ht80dur_msb, self.__reg_tximr2_ht80dur_lsb, value)
class MACTXIMR2PMD(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x28
        self.__tximr2complete_num_lsb = 28
        self.__tximr2complete_num_msb = 31
        self.__tximr2_cbw_lsb = 25
        self.__tximr2_cbw_msb = 26
        self.__tximr2_rssi_lsb = 16
        self.__tximr2_rssi_msb = 23
        self.__tximr2complete_state_lsb = 12
        self.__tximr2complete_state_msb = 15
        self.__tximr2complete_st_match_lsb = 8
        self.__tximr2complete_st_match_msb = 11
        self.__tximr2complete_errcode_lsb = 0
        self.__tximr2complete_errcode_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr2complete_num(self):
        return self.__MEM.rdm(self.__addr, self.__tximr2complete_num_msb, self.__tximr2complete_num_lsb)
    @tximr2complete_num.setter
    def tximr2complete_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr2complete_num_msb, self.__tximr2complete_num_lsb, value)

    @property
    def tximr2_cbw(self):
        return self.__MEM.rdm(self.__addr, self.__tximr2_cbw_msb, self.__tximr2_cbw_lsb)
    @tximr2_cbw.setter
    def tximr2_cbw(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr2_cbw_msb, self.__tximr2_cbw_lsb, value)

    @property
    def tximr2_rssi(self):
        return self.__MEM.rdm(self.__addr, self.__tximr2_rssi_msb, self.__tximr2_rssi_lsb)
    @tximr2_rssi.setter
    def tximr2_rssi(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr2_rssi_msb, self.__tximr2_rssi_lsb, value)

    @property
    def tximr2complete_state(self):
        return self.__MEM.rdm(self.__addr, self.__tximr2complete_state_msb, self.__tximr2complete_state_lsb)
    @tximr2complete_state.setter
    def tximr2complete_state(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr2complete_state_msb, self.__tximr2complete_state_lsb, value)

    @property
    def tximr2complete_st_match(self):
        return self.__MEM.rdm(self.__addr, self.__tximr2complete_st_match_msb, self.__tximr2complete_st_match_lsb)
    @tximr2complete_st_match.setter
    def tximr2complete_st_match(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr2complete_st_match_msb, self.__tximr2complete_st_match_lsb, value)

    @property
    def tximr2complete_errcode(self):
        return self.__MEM.rdm(self.__addr, self.__tximr2complete_errcode_msb, self.__tximr2complete_errcode_lsb)
    @tximr2complete_errcode.setter
    def tximr2complete_errcode(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr2complete_errcode_msb, self.__tximr2complete_errcode_lsb, value)
class MACTXIMR2BA_BMHI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x2c
        self.__tximr2ba_bmhi_lsb = 0
        self.__tximr2ba_bmhi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr2ba_bmhi(self):
        return self.__MEM.rdm(self.__addr, self.__tximr2ba_bmhi_msb, self.__tximr2ba_bmhi_lsb)
    @tximr2ba_bmhi.setter
    def tximr2ba_bmhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr2ba_bmhi_msb, self.__tximr2ba_bmhi_lsb, value)
class MACTXIMR2BA_BMLO(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x30
        self.__tximr2ba_bmlo_lsb = 0
        self.__tximr2ba_bmlo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr2ba_bmlo(self):
        return self.__MEM.rdm(self.__addr, self.__tximr2ba_bmlo_msb, self.__tximr2ba_bmlo_lsb)
    @tximr2ba_bmlo.setter
    def tximr2ba_bmlo(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr2ba_bmlo_msb, self.__tximr2ba_bmlo_lsb, value)
class MACTXIMR2BA_TAHI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x34
        self.__tximr2ba_tahi_lsb = 0
        self.__tximr2ba_tahi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr2ba_tahi(self):
        return self.__MEM.rdm(self.__addr, self.__tximr2ba_tahi_msb, self.__tximr2ba_tahi_lsb)
    @tximr2ba_tahi.setter
    def tximr2ba_tahi(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr2ba_tahi_msb, self.__tximr2ba_tahi_lsb, value)
class MACTXIMR2BA_TALO(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x38
        self.__tximr2ba_talo_lsb = 0
        self.__tximr2ba_talo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr2ba_talo(self):
        return self.__MEM.rdm(self.__addr, self.__tximr2ba_talo_msb, self.__tximr2ba_talo_lsb)
    @tximr2ba_talo.setter
    def tximr2ba_talo(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr2ba_talo_msb, self.__tximr2ba_talo_lsb, value)
class MACTXIMR2BA_SSN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x3c
        self.__tximr2ba_tid_lsb = 12
        self.__tximr2ba_tid_msb = 15
        self.__tximr2ba_ssn_lsb = 0
        self.__tximr2ba_ssn_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr2ba_tid(self):
        return self.__MEM.rdm(self.__addr, self.__tximr2ba_tid_msb, self.__tximr2ba_tid_lsb)
    @tximr2ba_tid.setter
    def tximr2ba_tid(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr2ba_tid_msb, self.__tximr2ba_tid_lsb, value)

    @property
    def tximr2ba_ssn(self):
        return self.__MEM.rdm(self.__addr, self.__tximr2ba_ssn_msb, self.__tximr2ba_ssn_lsb)
    @tximr2ba_ssn.setter
    def tximr2ba_ssn(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr2ba_ssn_msb, self.__tximr2ba_ssn_lsb, value)
class MACTXIMR2_TXSTART_US(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x40
        self.__tximr2_txstart_us_lsb = 0
        self.__tximr2_txstart_us_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr2_txstart_us(self):
        return self.__MEM.rdm(self.__addr, self.__tximr2_txstart_us_msb, self.__tximr2_txstart_us_lsb)
    @tximr2_txstart_us.setter
    def tximr2_txstart_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr2_txstart_us_msb, self.__tximr2_txstart_us_lsb, value)
class MACTXIMR2_TXSTART_CYC(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x44
        self.__tximr2_txrxack_us_hi_lsb = 14
        self.__tximr2_txrxack_us_hi_msb = 31
        self.__tximr2_txstart_cycle_lsb = 0
        self.__tximr2_txstart_cycle_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr2_txrxack_us_hi(self):
        return self.__MEM.rdm(self.__addr, self.__tximr2_txrxack_us_hi_msb, self.__tximr2_txrxack_us_hi_lsb)
    @tximr2_txrxack_us_hi.setter
    def tximr2_txrxack_us_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr2_txrxack_us_hi_msb, self.__tximr2_txrxack_us_hi_lsb, value)

    @property
    def tximr2_txstart_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__tximr2_txstart_cycle_msb, self.__tximr2_txstart_cycle_lsb)
    @tximr2_txstart_cycle.setter
    def tximr2_txstart_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr2_txstart_cycle_msb, self.__tximr2_txstart_cycle_lsb, value)
class MACTXIMR2_TXRXACK_CYC(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x48
        self.__tximr2_txrxack_us_lsb = 18
        self.__tximr2_txrxack_us_msb = 31
        self.__tximr2_txrxack_cycdec_lsb = 7
        self.__tximr2_txrxack_cycdec_msb = 17
        self.__tximr2_txrxack_cycle_lsb = 0
        self.__tximr2_txrxack_cycle_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr2_txrxack_us(self):
        return self.__MEM.rdm(self.__addr, self.__tximr2_txrxack_us_msb, self.__tximr2_txrxack_us_lsb)
    @tximr2_txrxack_us.setter
    def tximr2_txrxack_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr2_txrxack_us_msb, self.__tximr2_txrxack_us_lsb, value)

    @property
    def tximr2_txrxack_cycdec(self):
        return self.__MEM.rdm(self.__addr, self.__tximr2_txrxack_cycdec_msb, self.__tximr2_txrxack_cycdec_lsb)
    @tximr2_txrxack_cycdec.setter
    def tximr2_txrxack_cycdec(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr2_txrxack_cycdec_msb, self.__tximr2_txrxack_cycdec_lsb, value)

    @property
    def tximr2_txrxack_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__tximr2_txrxack_cycle_msb, self.__tximr2_txrxack_cycle_lsb)
    @tximr2_txrxack_cycle.setter
    def tximr2_txrxack_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr2_txrxack_cycle_msb, self.__tximr2_txrxack_cycle_lsb, value)
class MACTXIMR1_PLCP1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x4c
        self.__reg_tximr1_data_wbd_lsb = 31
        self.__reg_tximr1_data_wbd_msb = 31
        self.__reg_tximr1_rts_wbd_lsb = 30
        self.__reg_tximr1_rts_wbd_msb = 30
        self.__reg_tximr1_force_bw_lsb = 29
        self.__reg_tximr1_force_bw_msb = 29
        self.__reg_tximr1_nonhtdup_lsb = 27
        self.__reg_tximr1_nonhtdup_msb = 28
        self.__reg_tximr1_sigmode_lsb = 25
        self.__reg_tximr1_sigmode_msb = 26
        self.__reg_tximr1_kid_lsb = 17
        self.__reg_tximr1_kid_msb = 24
        self.__reg_tximr1_rate_lsb = 12
        self.__reg_tximr1_rate_msb = 16
        self.__reg_tximr1_length_lsb = 0
        self.__reg_tximr1_length_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr1_data_wbd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_data_wbd_msb, self.__reg_tximr1_data_wbd_lsb)
    @reg_tximr1_data_wbd.setter
    def reg_tximr1_data_wbd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_data_wbd_msb, self.__reg_tximr1_data_wbd_lsb, value)

    @property
    def reg_tximr1_rts_wbd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_rts_wbd_msb, self.__reg_tximr1_rts_wbd_lsb)
    @reg_tximr1_rts_wbd.setter
    def reg_tximr1_rts_wbd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_rts_wbd_msb, self.__reg_tximr1_rts_wbd_lsb, value)

    @property
    def reg_tximr1_force_bw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_force_bw_msb, self.__reg_tximr1_force_bw_lsb)
    @reg_tximr1_force_bw.setter
    def reg_tximr1_force_bw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_force_bw_msb, self.__reg_tximr1_force_bw_lsb, value)

    @property
    def reg_tximr1_nonhtdup(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_nonhtdup_msb, self.__reg_tximr1_nonhtdup_lsb)
    @reg_tximr1_nonhtdup.setter
    def reg_tximr1_nonhtdup(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_nonhtdup_msb, self.__reg_tximr1_nonhtdup_lsb, value)

    @property
    def reg_tximr1_sigmode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_sigmode_msb, self.__reg_tximr1_sigmode_lsb)
    @reg_tximr1_sigmode.setter
    def reg_tximr1_sigmode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_sigmode_msb, self.__reg_tximr1_sigmode_lsb, value)

    @property
    def reg_tximr1_kid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_kid_msb, self.__reg_tximr1_kid_lsb)
    @reg_tximr1_kid.setter
    def reg_tximr1_kid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_kid_msb, self.__reg_tximr1_kid_lsb, value)

    @property
    def reg_tximr1_rate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_rate_msb, self.__reg_tximr1_rate_lsb)
    @reg_tximr1_rate.setter
    def reg_tximr1_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_rate_msb, self.__reg_tximr1_rate_lsb, value)

    @property
    def reg_tximr1_length(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_length_msb, self.__reg_tximr1_length_lsb)
    @reg_tximr1_length.setter
    def reg_tximr1_length(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_length_msb, self.__reg_tximr1_length_lsb, value)
class MACTXIMR1_PTI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x50
        self.__reg_tximr1_pti_maintain_cnt_lsb = 20
        self.__reg_tximr1_pti_maintain_cnt_msb = 31
        self.__reg_tximr1_maintain_pti_lsb = 16
        self.__reg_tximr1_maintain_pti_msb = 19
        self.__reg_tximr1_rts_pti_lsb = 12
        self.__reg_tximr1_rts_pti_msb = 15
        self.__reg_tximr1_data_pti_lsb = 8
        self.__reg_tximr1_data_pti_msb = 11
        self.__reg_tximr1_ack_pti_lsb = 4
        self.__reg_tximr1_ack_pti_msb = 7
        self.__reg_tximr1_bssid_lsb = 0
        self.__reg_tximr1_bssid_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr1_pti_maintain_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_pti_maintain_cnt_msb, self.__reg_tximr1_pti_maintain_cnt_lsb)
    @reg_tximr1_pti_maintain_cnt.setter
    def reg_tximr1_pti_maintain_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_pti_maintain_cnt_msb, self.__reg_tximr1_pti_maintain_cnt_lsb, value)

    @property
    def reg_tximr1_maintain_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_maintain_pti_msb, self.__reg_tximr1_maintain_pti_lsb)
    @reg_tximr1_maintain_pti.setter
    def reg_tximr1_maintain_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_maintain_pti_msb, self.__reg_tximr1_maintain_pti_lsb, value)

    @property
    def reg_tximr1_rts_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_rts_pti_msb, self.__reg_tximr1_rts_pti_lsb)
    @reg_tximr1_rts_pti.setter
    def reg_tximr1_rts_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_rts_pti_msb, self.__reg_tximr1_rts_pti_lsb, value)

    @property
    def reg_tximr1_data_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_data_pti_msb, self.__reg_tximr1_data_pti_lsb)
    @reg_tximr1_data_pti.setter
    def reg_tximr1_data_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_data_pti_msb, self.__reg_tximr1_data_pti_lsb, value)

    @property
    def reg_tximr1_ack_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_ack_pti_msb, self.__reg_tximr1_ack_pti_lsb)
    @reg_tximr1_ack_pti.setter
    def reg_tximr1_ack_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_ack_pti_msb, self.__reg_tximr1_ack_pti_lsb, value)

    @property
    def reg_tximr1_bssid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_bssid_msb, self.__reg_tximr1_bssid_lsb)
    @reg_tximr1_bssid.setter
    def reg_tximr1_bssid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_bssid_msb, self.__reg_tximr1_bssid_lsb, value)
class MACTXIMR1_HTSIG(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x54
        self.__reg_tximr1_htsig_lsb = 0
        self.__reg_tximr1_htsig_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr1_htsig(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_htsig_msb, self.__reg_tximr1_htsig_lsb)
    @reg_tximr1_htsig.setter
    def reg_tximr1_htsig(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_htsig_msb, self.__reg_tximr1_htsig_lsb, value)
class MACTXIMR1_VHTSIG1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x58
        self.__reg_tximr1_vhtsiga_lo_lsb = 0
        self.__reg_tximr1_vhtsiga_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr1_vhtsiga_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_vhtsiga_lo_msb, self.__reg_tximr1_vhtsiga_lo_lsb)
    @reg_tximr1_vhtsiga_lo.setter
    def reg_tximr1_vhtsiga_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_vhtsiga_lo_msb, self.__reg_tximr1_vhtsiga_lo_lsb, value)
class MACTXIMR1_VHTSIG2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x5c
        self.__reg_tximr1_vhtsigb_lsb = 2
        self.__reg_tximr1_vhtsigb_msb = 24
        self.__reg_tximr1_vhtsiga_hi_lsb = 0
        self.__reg_tximr1_vhtsiga_hi_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr1_vhtsigb(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_vhtsigb_msb, self.__reg_tximr1_vhtsigb_lsb)
    @reg_tximr1_vhtsigb.setter
    def reg_tximr1_vhtsigb(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_vhtsigb_msb, self.__reg_tximr1_vhtsigb_lsb, value)

    @property
    def reg_tximr1_vhtsiga_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_vhtsiga_hi_msb, self.__reg_tximr1_vhtsiga_hi_lsb)
    @reg_tximr1_vhtsiga_hi.setter
    def reg_tximr1_vhtsiga_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_vhtsiga_hi_msb, self.__reg_tximr1_vhtsiga_hi_lsb, value)
class MACTXIMR1_HT80LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x60
        self.__reg_tximr1_ht80txop_num_lsb = 24
        self.__reg_tximr1_ht80txop_num_msb = 27
        self.__reg_tximr1_ht80eof_num_lsb = 22
        self.__reg_tximr1_ht80eof_num_msb = 23
        self.__reg_tximr1_ht80len_lsb = 0
        self.__reg_tximr1_ht80len_msb = 20
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr1_ht80txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_ht80txop_num_msb, self.__reg_tximr1_ht80txop_num_lsb)
    @reg_tximr1_ht80txop_num.setter
    def reg_tximr1_ht80txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_ht80txop_num_msb, self.__reg_tximr1_ht80txop_num_lsb, value)

    @property
    def reg_tximr1_ht80eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_ht80eof_num_msb, self.__reg_tximr1_ht80eof_num_lsb)
    @reg_tximr1_ht80eof_num.setter
    def reg_tximr1_ht80eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_ht80eof_num_msb, self.__reg_tximr1_ht80eof_num_lsb, value)

    @property
    def reg_tximr1_ht80len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_ht80len_msb, self.__reg_tximr1_ht80len_lsb)
    @reg_tximr1_ht80len.setter
    def reg_tximr1_ht80len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_ht80len_msb, self.__reg_tximr1_ht80len_lsb, value)
class MACTXIMR1_HT40LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x64
        self.__reg_tximr1_ht40txop_num_lsb = 24
        self.__reg_tximr1_ht40txop_num_msb = 27
        self.__reg_tximr1_ht40eof_num_lsb = 22
        self.__reg_tximr1_ht40eof_num_msb = 23
        self.__reg_tximr1_ht40len_lsb = 0
        self.__reg_tximr1_ht40len_msb = 18
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr1_ht40txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_ht40txop_num_msb, self.__reg_tximr1_ht40txop_num_lsb)
    @reg_tximr1_ht40txop_num.setter
    def reg_tximr1_ht40txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_ht40txop_num_msb, self.__reg_tximr1_ht40txop_num_lsb, value)

    @property
    def reg_tximr1_ht40eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_ht40eof_num_msb, self.__reg_tximr1_ht40eof_num_lsb)
    @reg_tximr1_ht40eof_num.setter
    def reg_tximr1_ht40eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_ht40eof_num_msb, self.__reg_tximr1_ht40eof_num_lsb, value)

    @property
    def reg_tximr1_ht40len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_ht40len_msb, self.__reg_tximr1_ht40len_lsb)
    @reg_tximr1_ht40len.setter
    def reg_tximr1_ht40len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_ht40len_msb, self.__reg_tximr1_ht40len_lsb, value)
class MACTXIMR1_HT20LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x68
        self.__reg_tximr1_txop_sel_lsb = 28
        self.__reg_tximr1_txop_sel_msb = 29
        self.__reg_tximr1_20txop_num_lsb = 24
        self.__reg_tximr1_20txop_num_msb = 27
        self.__reg_tximr1_20eof_num_lsb = 22
        self.__reg_tximr1_20eof_num_msb = 23
        self.__reg_tximr1_rts_rate_lsb = 6
        self.__reg_tximr1_rts_rate_msb = 13
        self.__reg_tximr1_ant_force_lsb = 5
        self.__reg_tximr1_ant_force_msb = 5
        self.__reg_tximr1_ant_force_value_lsb = 4
        self.__reg_tximr1_ant_force_value_msb = 4
        self.__reg_tximr1_ant_force_last_lsb = 3
        self.__reg_tximr1_ant_force_last_msb = 3
        self.__reg_txrximr1_ant_force_lsb = 2
        self.__reg_txrximr1_ant_force_msb = 2
        self.__reg_txrximr1_ant_force_value_lsb = 1
        self.__reg_txrximr1_ant_force_value_msb = 1
        self.__reg_txrximr1_ant_force_last_lsb = 0
        self.__reg_txrximr1_ant_force_last_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr1_txop_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_txop_sel_msb, self.__reg_tximr1_txop_sel_lsb)
    @reg_tximr1_txop_sel.setter
    def reg_tximr1_txop_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_txop_sel_msb, self.__reg_tximr1_txop_sel_lsb, value)

    @property
    def reg_tximr1_20txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_20txop_num_msb, self.__reg_tximr1_20txop_num_lsb)
    @reg_tximr1_20txop_num.setter
    def reg_tximr1_20txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_20txop_num_msb, self.__reg_tximr1_20txop_num_lsb, value)

    @property
    def reg_tximr1_20eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_20eof_num_msb, self.__reg_tximr1_20eof_num_lsb)
    @reg_tximr1_20eof_num.setter
    def reg_tximr1_20eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_20eof_num_msb, self.__reg_tximr1_20eof_num_lsb, value)

    @property
    def reg_tximr1_rts_rate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_rts_rate_msb, self.__reg_tximr1_rts_rate_lsb)
    @reg_tximr1_rts_rate.setter
    def reg_tximr1_rts_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_rts_rate_msb, self.__reg_tximr1_rts_rate_lsb, value)

    @property
    def reg_tximr1_ant_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_ant_force_msb, self.__reg_tximr1_ant_force_lsb)
    @reg_tximr1_ant_force.setter
    def reg_tximr1_ant_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_ant_force_msb, self.__reg_tximr1_ant_force_lsb, value)

    @property
    def reg_tximr1_ant_force_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_ant_force_value_msb, self.__reg_tximr1_ant_force_value_lsb)
    @reg_tximr1_ant_force_value.setter
    def reg_tximr1_ant_force_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_ant_force_value_msb, self.__reg_tximr1_ant_force_value_lsb, value)

    @property
    def reg_tximr1_ant_force_last(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_ant_force_last_msb, self.__reg_tximr1_ant_force_last_lsb)
    @reg_tximr1_ant_force_last.setter
    def reg_tximr1_ant_force_last(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_ant_force_last_msb, self.__reg_tximr1_ant_force_last_lsb, value)

    @property
    def reg_txrximr1_ant_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrximr1_ant_force_msb, self.__reg_txrximr1_ant_force_lsb)
    @reg_txrximr1_ant_force.setter
    def reg_txrximr1_ant_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrximr1_ant_force_msb, self.__reg_txrximr1_ant_force_lsb, value)

    @property
    def reg_txrximr1_ant_force_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrximr1_ant_force_value_msb, self.__reg_txrximr1_ant_force_value_lsb)
    @reg_txrximr1_ant_force_value.setter
    def reg_txrximr1_ant_force_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrximr1_ant_force_value_msb, self.__reg_txrximr1_ant_force_value_lsb, value)

    @property
    def reg_txrximr1_ant_force_last(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrximr1_ant_force_last_msb, self.__reg_txrximr1_ant_force_last_lsb)
    @reg_txrximr1_ant_force_last.setter
    def reg_txrximr1_ant_force_last(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrximr1_ant_force_last_msb, self.__reg_txrximr1_ant_force_last_lsb, value)
class MACTXIMR1_DUR(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x6c
        self.__reg_tximr1_20dur_lsb = 16
        self.__reg_tximr1_20dur_msb = 31
        self.__reg_tximr1_ht40dur_lsb = 0
        self.__reg_tximr1_ht40dur_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr1_20dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_20dur_msb, self.__reg_tximr1_20dur_lsb)
    @reg_tximr1_20dur.setter
    def reg_tximr1_20dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_20dur_msb, self.__reg_tximr1_20dur_lsb, value)

    @property
    def reg_tximr1_ht40dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_ht40dur_msb, self.__reg_tximr1_ht40dur_lsb)
    @reg_tximr1_ht40dur.setter
    def reg_tximr1_ht40dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_ht40dur_msb, self.__reg_tximr1_ht40dur_lsb, value)
class MACTXIMR1_DUR2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x70
        self.__reg_tximr1_hwseq_fgmd_lsb = 31
        self.__reg_tximr1_hwseq_fgmd_msb = 31
        self.__reg_tximr1_hwseq_qmfmd_lsb = 29
        self.__reg_tximr1_hwseq_qmfmd_msb = 29
        self.__reg_tximr1_hwseq_sel_lsb = 17
        self.__reg_tximr1_hwseq_sel_msb = 19
        self.__reg_tximr1_hwseq_update_lsb = 16
        self.__reg_tximr1_hwseq_update_msb = 16
        self.__reg_tximr1_ht80dur_lsb = 0
        self.__reg_tximr1_ht80dur_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr1_hwseq_fgmd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_hwseq_fgmd_msb, self.__reg_tximr1_hwseq_fgmd_lsb)
    @reg_tximr1_hwseq_fgmd.setter
    def reg_tximr1_hwseq_fgmd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_hwseq_fgmd_msb, self.__reg_tximr1_hwseq_fgmd_lsb, value)

    @property
    def reg_tximr1_hwseq_qmfmd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_hwseq_qmfmd_msb, self.__reg_tximr1_hwseq_qmfmd_lsb)
    @reg_tximr1_hwseq_qmfmd.setter
    def reg_tximr1_hwseq_qmfmd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_hwseq_qmfmd_msb, self.__reg_tximr1_hwseq_qmfmd_lsb, value)

    @property
    def reg_tximr1_hwseq_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_hwseq_sel_msb, self.__reg_tximr1_hwseq_sel_lsb)
    @reg_tximr1_hwseq_sel.setter
    def reg_tximr1_hwseq_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_hwseq_sel_msb, self.__reg_tximr1_hwseq_sel_lsb, value)

    @property
    def reg_tximr1_hwseq_update(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_hwseq_update_msb, self.__reg_tximr1_hwseq_update_lsb)
    @reg_tximr1_hwseq_update.setter
    def reg_tximr1_hwseq_update(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_hwseq_update_msb, self.__reg_tximr1_hwseq_update_lsb, value)
    @property
    def default_value(self):
        return 0x0

    @property
    def reg_tximr1_ht80dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr1_ht80dur_msb, self.__reg_tximr1_ht80dur_lsb)
    @reg_tximr1_ht80dur.setter
    def reg_tximr1_ht80dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr1_ht80dur_msb, self.__reg_tximr1_ht80dur_lsb, value)
class MACTXIMR1PMD(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x74
        self.__tximr1complete_num_lsb = 28
        self.__tximr1complete_num_msb = 31
        self.__tximr1_cbw_lsb = 25
        self.__tximr1_cbw_msb = 26
        self.__tximr1_rssi_lsb = 16
        self.__tximr1_rssi_msb = 23
        self.__tximr1complete_state_lsb = 12
        self.__tximr1complete_state_msb = 15
        self.__tximr1complete_st_match_lsb = 8
        self.__tximr1complete_st_match_msb = 11
        self.__tximr1complete_errcode_lsb = 0
        self.__tximr1complete_errcode_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr1complete_num(self):
        return self.__MEM.rdm(self.__addr, self.__tximr1complete_num_msb, self.__tximr1complete_num_lsb)
    @tximr1complete_num.setter
    def tximr1complete_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr1complete_num_msb, self.__tximr1complete_num_lsb, value)

    @property
    def tximr1_cbw(self):
        return self.__MEM.rdm(self.__addr, self.__tximr1_cbw_msb, self.__tximr1_cbw_lsb)
    @tximr1_cbw.setter
    def tximr1_cbw(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr1_cbw_msb, self.__tximr1_cbw_lsb, value)

    @property
    def tximr1_rssi(self):
        return self.__MEM.rdm(self.__addr, self.__tximr1_rssi_msb, self.__tximr1_rssi_lsb)
    @tximr1_rssi.setter
    def tximr1_rssi(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr1_rssi_msb, self.__tximr1_rssi_lsb, value)

    @property
    def tximr1complete_state(self):
        return self.__MEM.rdm(self.__addr, self.__tximr1complete_state_msb, self.__tximr1complete_state_lsb)
    @tximr1complete_state.setter
    def tximr1complete_state(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr1complete_state_msb, self.__tximr1complete_state_lsb, value)

    @property
    def tximr1complete_st_match(self):
        return self.__MEM.rdm(self.__addr, self.__tximr1complete_st_match_msb, self.__tximr1complete_st_match_lsb)
    @tximr1complete_st_match.setter
    def tximr1complete_st_match(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr1complete_st_match_msb, self.__tximr1complete_st_match_lsb, value)

    @property
    def tximr1complete_errcode(self):
        return self.__MEM.rdm(self.__addr, self.__tximr1complete_errcode_msb, self.__tximr1complete_errcode_lsb)
    @tximr1complete_errcode.setter
    def tximr1complete_errcode(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr1complete_errcode_msb, self.__tximr1complete_errcode_lsb, value)
class MACTXIMR1BA_BMHI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x78
        self.__tximr1ba_bmhi_lsb = 0
        self.__tximr1ba_bmhi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr1ba_bmhi(self):
        return self.__MEM.rdm(self.__addr, self.__tximr1ba_bmhi_msb, self.__tximr1ba_bmhi_lsb)
    @tximr1ba_bmhi.setter
    def tximr1ba_bmhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr1ba_bmhi_msb, self.__tximr1ba_bmhi_lsb, value)
class MACTXIMR1BA_BMLO(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x7c
        self.__tximr1ba_bmlo_lsb = 0
        self.__tximr1ba_bmlo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr1ba_bmlo(self):
        return self.__MEM.rdm(self.__addr, self.__tximr1ba_bmlo_msb, self.__tximr1ba_bmlo_lsb)
    @tximr1ba_bmlo.setter
    def tximr1ba_bmlo(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr1ba_bmlo_msb, self.__tximr1ba_bmlo_lsb, value)
class MACTXIMR1BA_TAHI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x80
        self.__tximr1ba_tahi_lsb = 0
        self.__tximr1ba_tahi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr1ba_tahi(self):
        return self.__MEM.rdm(self.__addr, self.__tximr1ba_tahi_msb, self.__tximr1ba_tahi_lsb)
    @tximr1ba_tahi.setter
    def tximr1ba_tahi(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr1ba_tahi_msb, self.__tximr1ba_tahi_lsb, value)
class MACTXIMR1BA_TALO(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x84
        self.__tximr1ba_talo_lsb = 0
        self.__tximr1ba_talo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr1ba_talo(self):
        return self.__MEM.rdm(self.__addr, self.__tximr1ba_talo_msb, self.__tximr1ba_talo_lsb)
    @tximr1ba_talo.setter
    def tximr1ba_talo(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr1ba_talo_msb, self.__tximr1ba_talo_lsb, value)
class MACTXIMR1BA_SSN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x88
        self.__tximr1ba_tid_lsb = 12
        self.__tximr1ba_tid_msb = 15
        self.__tximr1ba_ssn_lsb = 0
        self.__tximr1ba_ssn_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr1ba_tid(self):
        return self.__MEM.rdm(self.__addr, self.__tximr1ba_tid_msb, self.__tximr1ba_tid_lsb)
    @tximr1ba_tid.setter
    def tximr1ba_tid(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr1ba_tid_msb, self.__tximr1ba_tid_lsb, value)

    @property
    def tximr1ba_ssn(self):
        return self.__MEM.rdm(self.__addr, self.__tximr1ba_ssn_msb, self.__tximr1ba_ssn_lsb)
    @tximr1ba_ssn.setter
    def tximr1ba_ssn(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr1ba_ssn_msb, self.__tximr1ba_ssn_lsb, value)
class MACTXIMR1_TXSTART_US(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x8c
        self.__tximr1_txstart_us_lsb = 0
        self.__tximr1_txstart_us_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr1_txstart_us(self):
        return self.__MEM.rdm(self.__addr, self.__tximr1_txstart_us_msb, self.__tximr1_txstart_us_lsb)
    @tximr1_txstart_us.setter
    def tximr1_txstart_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr1_txstart_us_msb, self.__tximr1_txstart_us_lsb, value)
class MACTXIMR1_TXSTART_CYC(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x90
        self.__tximr1_txrxack_us_hi_lsb = 14
        self.__tximr1_txrxack_us_hi_msb = 31
        self.__tximr1_txstart_cycle_lsb = 0
        self.__tximr1_txstart_cycle_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr1_txrxack_us_hi(self):
        return self.__MEM.rdm(self.__addr, self.__tximr1_txrxack_us_hi_msb, self.__tximr1_txrxack_us_hi_lsb)
    @tximr1_txrxack_us_hi.setter
    def tximr1_txrxack_us_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr1_txrxack_us_hi_msb, self.__tximr1_txrxack_us_hi_lsb, value)

    @property
    def tximr1_txstart_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__tximr1_txstart_cycle_msb, self.__tximr1_txstart_cycle_lsb)
    @tximr1_txstart_cycle.setter
    def tximr1_txstart_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr1_txstart_cycle_msb, self.__tximr1_txstart_cycle_lsb, value)
class MACTXIMR1_TXRXACK_CYC(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x94
        self.__tximr1_txrxack_us_lsb = 18
        self.__tximr1_txrxack_us_msb = 31
        self.__tximr1_txrxack_cycdec_lsb = 7
        self.__tximr1_txrxack_cycdec_msb = 17
        self.__tximr1_txrxack_cycle_lsb = 0
        self.__tximr1_txrxack_cycle_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr1_txrxack_us(self):
        return self.__MEM.rdm(self.__addr, self.__tximr1_txrxack_us_msb, self.__tximr1_txrxack_us_lsb)
    @tximr1_txrxack_us.setter
    def tximr1_txrxack_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr1_txrxack_us_msb, self.__tximr1_txrxack_us_lsb, value)

    @property
    def tximr1_txrxack_cycdec(self):
        return self.__MEM.rdm(self.__addr, self.__tximr1_txrxack_cycdec_msb, self.__tximr1_txrxack_cycdec_lsb)
    @tximr1_txrxack_cycdec.setter
    def tximr1_txrxack_cycdec(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr1_txrxack_cycdec_msb, self.__tximr1_txrxack_cycdec_lsb, value)

    @property
    def tximr1_txrxack_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__tximr1_txrxack_cycle_msb, self.__tximr1_txrxack_cycle_lsb)
    @tximr1_txrxack_cycle.setter
    def tximr1_txrxack_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr1_txrxack_cycle_msb, self.__tximr1_txrxack_cycle_lsb, value)
class MACTXIMR0_PLCP1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x98
        self.__reg_tximr0_data_wbd_lsb = 31
        self.__reg_tximr0_data_wbd_msb = 31
        self.__reg_tximr0_rts_wbd_lsb = 30
        self.__reg_tximr0_rts_wbd_msb = 30
        self.__reg_tximr0_force_bw_lsb = 29
        self.__reg_tximr0_force_bw_msb = 29
        self.__reg_tximr0_nonhtdup_lsb = 27
        self.__reg_tximr0_nonhtdup_msb = 28
        self.__reg_tximr0_sigmode_lsb = 25
        self.__reg_tximr0_sigmode_msb = 26
        self.__reg_tximr0_kid_lsb = 17
        self.__reg_tximr0_kid_msb = 24
        self.__reg_tximr0_rate_lsb = 12
        self.__reg_tximr0_rate_msb = 16
        self.__reg_tximr0_length_lsb = 0
        self.__reg_tximr0_length_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr0_data_wbd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_data_wbd_msb, self.__reg_tximr0_data_wbd_lsb)
    @reg_tximr0_data_wbd.setter
    def reg_tximr0_data_wbd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_data_wbd_msb, self.__reg_tximr0_data_wbd_lsb, value)

    @property
    def reg_tximr0_rts_wbd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_rts_wbd_msb, self.__reg_tximr0_rts_wbd_lsb)
    @reg_tximr0_rts_wbd.setter
    def reg_tximr0_rts_wbd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_rts_wbd_msb, self.__reg_tximr0_rts_wbd_lsb, value)

    @property
    def reg_tximr0_force_bw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_force_bw_msb, self.__reg_tximr0_force_bw_lsb)
    @reg_tximr0_force_bw.setter
    def reg_tximr0_force_bw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_force_bw_msb, self.__reg_tximr0_force_bw_lsb, value)

    @property
    def reg_tximr0_nonhtdup(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_nonhtdup_msb, self.__reg_tximr0_nonhtdup_lsb)
    @reg_tximr0_nonhtdup.setter
    def reg_tximr0_nonhtdup(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_nonhtdup_msb, self.__reg_tximr0_nonhtdup_lsb, value)

    @property
    def reg_tximr0_sigmode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_sigmode_msb, self.__reg_tximr0_sigmode_lsb)
    @reg_tximr0_sigmode.setter
    def reg_tximr0_sigmode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_sigmode_msb, self.__reg_tximr0_sigmode_lsb, value)

    @property
    def reg_tximr0_kid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_kid_msb, self.__reg_tximr0_kid_lsb)
    @reg_tximr0_kid.setter
    def reg_tximr0_kid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_kid_msb, self.__reg_tximr0_kid_lsb, value)

    @property
    def reg_tximr0_rate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_rate_msb, self.__reg_tximr0_rate_lsb)
    @reg_tximr0_rate.setter
    def reg_tximr0_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_rate_msb, self.__reg_tximr0_rate_lsb, value)

    @property
    def reg_tximr0_length(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_length_msb, self.__reg_tximr0_length_lsb)
    @reg_tximr0_length.setter
    def reg_tximr0_length(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_length_msb, self.__reg_tximr0_length_lsb, value)
class MACTXIMR0_PTI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x9c
        self.__reg_tximr0_pti_maintain_cnt_lsb = 20
        self.__reg_tximr0_pti_maintain_cnt_msb = 31
        self.__reg_tximr0_maintain_pti_lsb = 16
        self.__reg_tximr0_maintain_pti_msb = 19
        self.__reg_tximr0_rts_pti_lsb = 12
        self.__reg_tximr0_rts_pti_msb = 15
        self.__reg_tximr0_data_pti_lsb = 8
        self.__reg_tximr0_data_pti_msb = 11
        self.__reg_tximr0_ack_pti_lsb = 4
        self.__reg_tximr0_ack_pti_msb = 7
        self.__reg_tximr0_bssid_lsb = 0
        self.__reg_tximr0_bssid_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr0_pti_maintain_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_pti_maintain_cnt_msb, self.__reg_tximr0_pti_maintain_cnt_lsb)
    @reg_tximr0_pti_maintain_cnt.setter
    def reg_tximr0_pti_maintain_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_pti_maintain_cnt_msb, self.__reg_tximr0_pti_maintain_cnt_lsb, value)

    @property
    def reg_tximr0_maintain_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_maintain_pti_msb, self.__reg_tximr0_maintain_pti_lsb)
    @reg_tximr0_maintain_pti.setter
    def reg_tximr0_maintain_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_maintain_pti_msb, self.__reg_tximr0_maintain_pti_lsb, value)

    @property
    def reg_tximr0_rts_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_rts_pti_msb, self.__reg_tximr0_rts_pti_lsb)
    @reg_tximr0_rts_pti.setter
    def reg_tximr0_rts_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_rts_pti_msb, self.__reg_tximr0_rts_pti_lsb, value)

    @property
    def reg_tximr0_data_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_data_pti_msb, self.__reg_tximr0_data_pti_lsb)
    @reg_tximr0_data_pti.setter
    def reg_tximr0_data_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_data_pti_msb, self.__reg_tximr0_data_pti_lsb, value)

    @property
    def reg_tximr0_ack_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_ack_pti_msb, self.__reg_tximr0_ack_pti_lsb)
    @reg_tximr0_ack_pti.setter
    def reg_tximr0_ack_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_ack_pti_msb, self.__reg_tximr0_ack_pti_lsb, value)

    @property
    def reg_tximr0_bssid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_bssid_msb, self.__reg_tximr0_bssid_lsb)
    @reg_tximr0_bssid.setter
    def reg_tximr0_bssid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_bssid_msb, self.__reg_tximr0_bssid_lsb, value)
class MACTXIMR0_HTSIG(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0xa0
        self.__reg_tximr0_htsig_lsb = 0
        self.__reg_tximr0_htsig_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr0_htsig(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_htsig_msb, self.__reg_tximr0_htsig_lsb)
    @reg_tximr0_htsig.setter
    def reg_tximr0_htsig(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_htsig_msb, self.__reg_tximr0_htsig_lsb, value)
class MACTXIMR0_VHTSIG1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0xa4
        self.__reg_tximr0_vhtsiga_lo_lsb = 0
        self.__reg_tximr0_vhtsiga_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr0_vhtsiga_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_vhtsiga_lo_msb, self.__reg_tximr0_vhtsiga_lo_lsb)
    @reg_tximr0_vhtsiga_lo.setter
    def reg_tximr0_vhtsiga_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_vhtsiga_lo_msb, self.__reg_tximr0_vhtsiga_lo_lsb, value)
class MACTXIMR0_VHTSIG2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0xa8
        self.__reg_tximr0_vhtsigb_lsb = 2
        self.__reg_tximr0_vhtsigb_msb = 24
        self.__reg_tximr0_vhtsiga_hi_lsb = 0
        self.__reg_tximr0_vhtsiga_hi_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr0_vhtsigb(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_vhtsigb_msb, self.__reg_tximr0_vhtsigb_lsb)
    @reg_tximr0_vhtsigb.setter
    def reg_tximr0_vhtsigb(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_vhtsigb_msb, self.__reg_tximr0_vhtsigb_lsb, value)

    @property
    def reg_tximr0_vhtsiga_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_vhtsiga_hi_msb, self.__reg_tximr0_vhtsiga_hi_lsb)
    @reg_tximr0_vhtsiga_hi.setter
    def reg_tximr0_vhtsiga_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_vhtsiga_hi_msb, self.__reg_tximr0_vhtsiga_hi_lsb, value)
class MACTXIMR0_HT80LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0xac
        self.__reg_tximr0_ht80txop_num_lsb = 24
        self.__reg_tximr0_ht80txop_num_msb = 27
        self.__reg_tximr0_ht80eof_num_lsb = 22
        self.__reg_tximr0_ht80eof_num_msb = 23
        self.__reg_tximr0_ht80len_lsb = 0
        self.__reg_tximr0_ht80len_msb = 20
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr0_ht80txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_ht80txop_num_msb, self.__reg_tximr0_ht80txop_num_lsb)
    @reg_tximr0_ht80txop_num.setter
    def reg_tximr0_ht80txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_ht80txop_num_msb, self.__reg_tximr0_ht80txop_num_lsb, value)

    @property
    def reg_tximr0_ht80eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_ht80eof_num_msb, self.__reg_tximr0_ht80eof_num_lsb)
    @reg_tximr0_ht80eof_num.setter
    def reg_tximr0_ht80eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_ht80eof_num_msb, self.__reg_tximr0_ht80eof_num_lsb, value)

    @property
    def reg_tximr0_ht80len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_ht80len_msb, self.__reg_tximr0_ht80len_lsb)
    @reg_tximr0_ht80len.setter
    def reg_tximr0_ht80len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_ht80len_msb, self.__reg_tximr0_ht80len_lsb, value)
class MACTXIMR0_HT40LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0xb0
        self.__reg_tximr0_ht40txop_num_lsb = 24
        self.__reg_tximr0_ht40txop_num_msb = 27
        self.__reg_tximr0_ht40eof_num_lsb = 22
        self.__reg_tximr0_ht40eof_num_msb = 23
        self.__reg_tximr0_ht40len_lsb = 0
        self.__reg_tximr0_ht40len_msb = 18
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr0_ht40txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_ht40txop_num_msb, self.__reg_tximr0_ht40txop_num_lsb)
    @reg_tximr0_ht40txop_num.setter
    def reg_tximr0_ht40txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_ht40txop_num_msb, self.__reg_tximr0_ht40txop_num_lsb, value)

    @property
    def reg_tximr0_ht40eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_ht40eof_num_msb, self.__reg_tximr0_ht40eof_num_lsb)
    @reg_tximr0_ht40eof_num.setter
    def reg_tximr0_ht40eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_ht40eof_num_msb, self.__reg_tximr0_ht40eof_num_lsb, value)

    @property
    def reg_tximr0_ht40len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_ht40len_msb, self.__reg_tximr0_ht40len_lsb)
    @reg_tximr0_ht40len.setter
    def reg_tximr0_ht40len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_ht40len_msb, self.__reg_tximr0_ht40len_lsb, value)
class MACTXIMR0_HT20LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0xb4
        self.__reg_tximr0_txop_sel_lsb = 28
        self.__reg_tximr0_txop_sel_msb = 29
        self.__reg_tximr0_20txop_num_lsb = 24
        self.__reg_tximr0_20txop_num_msb = 27
        self.__reg_tximr0_20eof_num_lsb = 22
        self.__reg_tximr0_20eof_num_msb = 23
        self.__reg_tximr0_rts_rate_lsb = 6
        self.__reg_tximr0_rts_rate_msb = 13
        self.__reg_tximr0_ant_force_lsb = 5
        self.__reg_tximr0_ant_force_msb = 5
        self.__reg_tximr0_ant_force_value_lsb = 4
        self.__reg_tximr0_ant_force_value_msb = 4
        self.__reg_tximr0_ant_force_last_lsb = 3
        self.__reg_tximr0_ant_force_last_msb = 3
        self.__reg_txrximr0_ant_force_lsb = 2
        self.__reg_txrximr0_ant_force_msb = 2
        self.__reg_txrximr0_ant_force_value_lsb = 1
        self.__reg_txrximr0_ant_force_value_msb = 1
        self.__reg_txrximr0_ant_force_last_lsb = 0
        self.__reg_txrximr0_ant_force_last_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr0_txop_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_txop_sel_msb, self.__reg_tximr0_txop_sel_lsb)
    @reg_tximr0_txop_sel.setter
    def reg_tximr0_txop_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_txop_sel_msb, self.__reg_tximr0_txop_sel_lsb, value)

    @property
    def reg_tximr0_20txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_20txop_num_msb, self.__reg_tximr0_20txop_num_lsb)
    @reg_tximr0_20txop_num.setter
    def reg_tximr0_20txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_20txop_num_msb, self.__reg_tximr0_20txop_num_lsb, value)

    @property
    def reg_tximr0_20eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_20eof_num_msb, self.__reg_tximr0_20eof_num_lsb)
    @reg_tximr0_20eof_num.setter
    def reg_tximr0_20eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_20eof_num_msb, self.__reg_tximr0_20eof_num_lsb, value)

    @property
    def reg_tximr0_rts_rate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_rts_rate_msb, self.__reg_tximr0_rts_rate_lsb)
    @reg_tximr0_rts_rate.setter
    def reg_tximr0_rts_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_rts_rate_msb, self.__reg_tximr0_rts_rate_lsb, value)

    @property
    def reg_tximr0_ant_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_ant_force_msb, self.__reg_tximr0_ant_force_lsb)
    @reg_tximr0_ant_force.setter
    def reg_tximr0_ant_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_ant_force_msb, self.__reg_tximr0_ant_force_lsb, value)

    @property
    def reg_tximr0_ant_force_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_ant_force_value_msb, self.__reg_tximr0_ant_force_value_lsb)
    @reg_tximr0_ant_force_value.setter
    def reg_tximr0_ant_force_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_ant_force_value_msb, self.__reg_tximr0_ant_force_value_lsb, value)

    @property
    def reg_tximr0_ant_force_last(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_ant_force_last_msb, self.__reg_tximr0_ant_force_last_lsb)
    @reg_tximr0_ant_force_last.setter
    def reg_tximr0_ant_force_last(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_ant_force_last_msb, self.__reg_tximr0_ant_force_last_lsb, value)

    @property
    def reg_txrximr0_ant_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrximr0_ant_force_msb, self.__reg_txrximr0_ant_force_lsb)
    @reg_txrximr0_ant_force.setter
    def reg_txrximr0_ant_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrximr0_ant_force_msb, self.__reg_txrximr0_ant_force_lsb, value)

    @property
    def reg_txrximr0_ant_force_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrximr0_ant_force_value_msb, self.__reg_txrximr0_ant_force_value_lsb)
    @reg_txrximr0_ant_force_value.setter
    def reg_txrximr0_ant_force_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrximr0_ant_force_value_msb, self.__reg_txrximr0_ant_force_value_lsb, value)

    @property
    def reg_txrximr0_ant_force_last(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrximr0_ant_force_last_msb, self.__reg_txrximr0_ant_force_last_lsb)
    @reg_txrximr0_ant_force_last.setter
    def reg_txrximr0_ant_force_last(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrximr0_ant_force_last_msb, self.__reg_txrximr0_ant_force_last_lsb, value)
class MACTXIMR0_DUR(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0xb8
        self.__reg_tximr0_20dur_lsb = 16
        self.__reg_tximr0_20dur_msb = 31
        self.__reg_tximr0_ht40dur_lsb = 0
        self.__reg_tximr0_ht40dur_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr0_20dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_20dur_msb, self.__reg_tximr0_20dur_lsb)
    @reg_tximr0_20dur.setter
    def reg_tximr0_20dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_20dur_msb, self.__reg_tximr0_20dur_lsb, value)

    @property
    def reg_tximr0_ht40dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_ht40dur_msb, self.__reg_tximr0_ht40dur_lsb)
    @reg_tximr0_ht40dur.setter
    def reg_tximr0_ht40dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_ht40dur_msb, self.__reg_tximr0_ht40dur_lsb, value)
class MACTXIMR0_DUR2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0xbc
        self.__reg_tximr0_hwseq_fgmd_lsb = 31
        self.__reg_tximr0_hwseq_fgmd_msb = 31
        self.__reg_tximr0_hwseq_qmfmd_lsb = 29
        self.__reg_tximr0_hwseq_qmfmd_msb = 29
        self.__reg_tximr0_hwseq_sel_lsb = 17
        self.__reg_tximr0_hwseq_sel_msb = 19
        self.__reg_tximr0_hwseq_update_lsb = 16
        self.__reg_tximr0_hwseq_update_msb = 16
        self.__reg_tximr0_ht80dur_lsb = 0
        self.__reg_tximr0_ht80dur_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_tximr0_hwseq_fgmd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_hwseq_fgmd_msb, self.__reg_tximr0_hwseq_fgmd_lsb)
    @reg_tximr0_hwseq_fgmd.setter
    def reg_tximr0_hwseq_fgmd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_hwseq_fgmd_msb, self.__reg_tximr0_hwseq_fgmd_lsb, value)

    @property
    def reg_tximr0_hwseq_qmfmd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_hwseq_qmfmd_msb, self.__reg_tximr0_hwseq_qmfmd_lsb)
    @reg_tximr0_hwseq_qmfmd.setter
    def reg_tximr0_hwseq_qmfmd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_hwseq_qmfmd_msb, self.__reg_tximr0_hwseq_qmfmd_lsb, value)

    @property
    def reg_tximr0_hwseq_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_hwseq_sel_msb, self.__reg_tximr0_hwseq_sel_lsb)
    @reg_tximr0_hwseq_sel.setter
    def reg_tximr0_hwseq_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_hwseq_sel_msb, self.__reg_tximr0_hwseq_sel_lsb, value)

    @property
    def reg_tximr0_hwseq_update(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_hwseq_update_msb, self.__reg_tximr0_hwseq_update_lsb)
    @reg_tximr0_hwseq_update.setter
    def reg_tximr0_hwseq_update(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_hwseq_update_msb, self.__reg_tximr0_hwseq_update_lsb, value)
    @property
    def default_value(self):
        return 0x0

    @property
    def reg_tximr0_ht80dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_tximr0_ht80dur_msb, self.__reg_tximr0_ht80dur_lsb)
    @reg_tximr0_ht80dur.setter
    def reg_tximr0_ht80dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_tximr0_ht80dur_msb, self.__reg_tximr0_ht80dur_lsb, value)
class MACTXIMR0PMD(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0xc0
        self.__tximr0complete_num_lsb = 28
        self.__tximr0complete_num_msb = 31
        self.__tximr0_cbw_lsb = 25
        self.__tximr0_cbw_msb = 26
        self.__tximr0_rssi_lsb = 16
        self.__tximr0_rssi_msb = 23
        self.__tximr0complete_state_lsb = 12
        self.__tximr0complete_state_msb = 15
        self.__tximr0complete_st_match_lsb = 8
        self.__tximr0complete_st_match_msb = 11
        self.__tximr0complete_errcode_lsb = 0
        self.__tximr0complete_errcode_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr0complete_num(self):
        return self.__MEM.rdm(self.__addr, self.__tximr0complete_num_msb, self.__tximr0complete_num_lsb)
    @tximr0complete_num.setter
    def tximr0complete_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr0complete_num_msb, self.__tximr0complete_num_lsb, value)

    @property
    def tximr0_cbw(self):
        return self.__MEM.rdm(self.__addr, self.__tximr0_cbw_msb, self.__tximr0_cbw_lsb)
    @tximr0_cbw.setter
    def tximr0_cbw(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr0_cbw_msb, self.__tximr0_cbw_lsb, value)

    @property
    def tximr0_rssi(self):
        return self.__MEM.rdm(self.__addr, self.__tximr0_rssi_msb, self.__tximr0_rssi_lsb)
    @tximr0_rssi.setter
    def tximr0_rssi(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr0_rssi_msb, self.__tximr0_rssi_lsb, value)

    @property
    def tximr0complete_state(self):
        return self.__MEM.rdm(self.__addr, self.__tximr0complete_state_msb, self.__tximr0complete_state_lsb)
    @tximr0complete_state.setter
    def tximr0complete_state(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr0complete_state_msb, self.__tximr0complete_state_lsb, value)

    @property
    def tximr0complete_st_match(self):
        return self.__MEM.rdm(self.__addr, self.__tximr0complete_st_match_msb, self.__tximr0complete_st_match_lsb)
    @tximr0complete_st_match.setter
    def tximr0complete_st_match(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr0complete_st_match_msb, self.__tximr0complete_st_match_lsb, value)

    @property
    def tximr0complete_errcode(self):
        return self.__MEM.rdm(self.__addr, self.__tximr0complete_errcode_msb, self.__tximr0complete_errcode_lsb)
    @tximr0complete_errcode.setter
    def tximr0complete_errcode(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr0complete_errcode_msb, self.__tximr0complete_errcode_lsb, value)
class MACTXIMR0BA_BMHI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0xc4
        self.__tximr0ba_bmhi_lsb = 0
        self.__tximr0ba_bmhi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr0ba_bmhi(self):
        return self.__MEM.rdm(self.__addr, self.__tximr0ba_bmhi_msb, self.__tximr0ba_bmhi_lsb)
    @tximr0ba_bmhi.setter
    def tximr0ba_bmhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr0ba_bmhi_msb, self.__tximr0ba_bmhi_lsb, value)
class MACTXIMR0BA_BMLO(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0xc8
        self.__tximr0ba_bmlo_lsb = 0
        self.__tximr0ba_bmlo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr0ba_bmlo(self):
        return self.__MEM.rdm(self.__addr, self.__tximr0ba_bmlo_msb, self.__tximr0ba_bmlo_lsb)
    @tximr0ba_bmlo.setter
    def tximr0ba_bmlo(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr0ba_bmlo_msb, self.__tximr0ba_bmlo_lsb, value)
class MACTXIMR0BA_TAHI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0xcc
        self.__tximr0ba_tahi_lsb = 0
        self.__tximr0ba_tahi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr0ba_tahi(self):
        return self.__MEM.rdm(self.__addr, self.__tximr0ba_tahi_msb, self.__tximr0ba_tahi_lsb)
    @tximr0ba_tahi.setter
    def tximr0ba_tahi(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr0ba_tahi_msb, self.__tximr0ba_tahi_lsb, value)
class MACTXIMR0BA_TALO(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0xd0
        self.__tximr0ba_talo_lsb = 0
        self.__tximr0ba_talo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr0ba_talo(self):
        return self.__MEM.rdm(self.__addr, self.__tximr0ba_talo_msb, self.__tximr0ba_talo_lsb)
    @tximr0ba_talo.setter
    def tximr0ba_talo(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr0ba_talo_msb, self.__tximr0ba_talo_lsb, value)
class MACTXIMR0BA_SSN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0xd4
        self.__tximr0ba_tid_lsb = 12
        self.__tximr0ba_tid_msb = 15
        self.__tximr0ba_ssn_lsb = 0
        self.__tximr0ba_ssn_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr0ba_tid(self):
        return self.__MEM.rdm(self.__addr, self.__tximr0ba_tid_msb, self.__tximr0ba_tid_lsb)
    @tximr0ba_tid.setter
    def tximr0ba_tid(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr0ba_tid_msb, self.__tximr0ba_tid_lsb, value)

    @property
    def tximr0ba_ssn(self):
        return self.__MEM.rdm(self.__addr, self.__tximr0ba_ssn_msb, self.__tximr0ba_ssn_lsb)
    @tximr0ba_ssn.setter
    def tximr0ba_ssn(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr0ba_ssn_msb, self.__tximr0ba_ssn_lsb, value)
class MACTXIMR0_TXSTART_US(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0xd8
        self.__tximr0_txstart_us_lsb = 0
        self.__tximr0_txstart_us_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr0_txstart_us(self):
        return self.__MEM.rdm(self.__addr, self.__tximr0_txstart_us_msb, self.__tximr0_txstart_us_lsb)
    @tximr0_txstart_us.setter
    def tximr0_txstart_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr0_txstart_us_msb, self.__tximr0_txstart_us_lsb, value)
class MACTXIMR0_TXSTART_CYC(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0xdc
        self.__tximr0_txrxack_us_hi_lsb = 14
        self.__tximr0_txrxack_us_hi_msb = 31
        self.__tximr0_txstart_cycle_lsb = 0
        self.__tximr0_txstart_cycle_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr0_txrxack_us_hi(self):
        return self.__MEM.rdm(self.__addr, self.__tximr0_txrxack_us_hi_msb, self.__tximr0_txrxack_us_hi_lsb)
    @tximr0_txrxack_us_hi.setter
    def tximr0_txrxack_us_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr0_txrxack_us_hi_msb, self.__tximr0_txrxack_us_hi_lsb, value)

    @property
    def tximr0_txstart_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__tximr0_txstart_cycle_msb, self.__tximr0_txstart_cycle_lsb)
    @tximr0_txstart_cycle.setter
    def tximr0_txstart_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr0_txstart_cycle_msb, self.__tximr0_txstart_cycle_lsb, value)
class MACTXIMR0_TXRXACK_CYC(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0xe0
        self.__tximr0_txrxack_us_lsb = 18
        self.__tximr0_txrxack_us_msb = 31
        self.__tximr0_txrxack_cycdec_lsb = 7
        self.__tximr0_txrxack_cycdec_msb = 17
        self.__tximr0_txrxack_cycle_lsb = 0
        self.__tximr0_txrxack_cycle_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def tximr0_txrxack_us(self):
        return self.__MEM.rdm(self.__addr, self.__tximr0_txrxack_us_msb, self.__tximr0_txrxack_us_lsb)
    @tximr0_txrxack_us.setter
    def tximr0_txrxack_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr0_txrxack_us_msb, self.__tximr0_txrxack_us_lsb, value)

    @property
    def tximr0_txrxack_cycdec(self):
        return self.__MEM.rdm(self.__addr, self.__tximr0_txrxack_cycdec_msb, self.__tximr0_txrxack_cycdec_lsb)
    @tximr0_txrxack_cycdec.setter
    def tximr0_txrxack_cycdec(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr0_txrxack_cycdec_msb, self.__tximr0_txrxack_cycdec_lsb, value)

    @property
    def tximr0_txrxack_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__tximr0_txrxack_cycle_msb, self.__tximr0_txrxack_cycle_lsb)
    @tximr0_txrxack_cycle.setter
    def tximr0_txrxack_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__tximr0_txrxack_cycle_msb, self.__tximr0_txrxack_cycle_lsb, value)
class MACTXQ7_PLCP1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0xe4
        self.__reg_txq7_data_wbd_lsb = 31
        self.__reg_txq7_data_wbd_msb = 31
        self.__reg_txq7_rts_wbd_lsb = 30
        self.__reg_txq7_rts_wbd_msb = 30
        self.__reg_txq7_force_bw_lsb = 29
        self.__reg_txq7_force_bw_msb = 29
        self.__reg_txq7_nonhtdup_lsb = 27
        self.__reg_txq7_nonhtdup_msb = 28
        self.__reg_txq7_sigmode_lsb = 25
        self.__reg_txq7_sigmode_msb = 26
        self.__reg_txq7_kid_lsb = 17
        self.__reg_txq7_kid_msb = 24
        self.__reg_txq7_rate_lsb = 12
        self.__reg_txq7_rate_msb = 16
        self.__reg_txq7_length_lsb = 0
        self.__reg_txq7_length_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq7_data_wbd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_data_wbd_msb, self.__reg_txq7_data_wbd_lsb)
    @reg_txq7_data_wbd.setter
    def reg_txq7_data_wbd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_data_wbd_msb, self.__reg_txq7_data_wbd_lsb, value)

    @property
    def reg_txq7_rts_wbd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_rts_wbd_msb, self.__reg_txq7_rts_wbd_lsb)
    @reg_txq7_rts_wbd.setter
    def reg_txq7_rts_wbd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_rts_wbd_msb, self.__reg_txq7_rts_wbd_lsb, value)

    @property
    def reg_txq7_force_bw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_force_bw_msb, self.__reg_txq7_force_bw_lsb)
    @reg_txq7_force_bw.setter
    def reg_txq7_force_bw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_force_bw_msb, self.__reg_txq7_force_bw_lsb, value)

    @property
    def reg_txq7_nonhtdup(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_nonhtdup_msb, self.__reg_txq7_nonhtdup_lsb)
    @reg_txq7_nonhtdup.setter
    def reg_txq7_nonhtdup(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_nonhtdup_msb, self.__reg_txq7_nonhtdup_lsb, value)

    @property
    def reg_txq7_sigmode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_sigmode_msb, self.__reg_txq7_sigmode_lsb)
    @reg_txq7_sigmode.setter
    def reg_txq7_sigmode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_sigmode_msb, self.__reg_txq7_sigmode_lsb, value)

    @property
    def reg_txq7_kid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_kid_msb, self.__reg_txq7_kid_lsb)
    @reg_txq7_kid.setter
    def reg_txq7_kid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_kid_msb, self.__reg_txq7_kid_lsb, value)

    @property
    def reg_txq7_rate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_rate_msb, self.__reg_txq7_rate_lsb)
    @reg_txq7_rate.setter
    def reg_txq7_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_rate_msb, self.__reg_txq7_rate_lsb, value)

    @property
    def reg_txq7_length(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_length_msb, self.__reg_txq7_length_lsb)
    @reg_txq7_length.setter
    def reg_txq7_length(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_length_msb, self.__reg_txq7_length_lsb, value)
class MACTXQ7_PTI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0xe8
        self.__reg_txq7_pti_maintain_cnt_lsb = 20
        self.__reg_txq7_pti_maintain_cnt_msb = 31
        self.__reg_txq7_maintain_pti_lsb = 16
        self.__reg_txq7_maintain_pti_msb = 19
        self.__reg_txq7_rts_pti_lsb = 12
        self.__reg_txq7_rts_pti_msb = 15
        self.__reg_txq7_data_pti_lsb = 8
        self.__reg_txq7_data_pti_msb = 11
        self.__reg_txq7_ack_pti_lsb = 4
        self.__reg_txq7_ack_pti_msb = 7
        self.__reg_txq7_bssid_lsb = 0
        self.__reg_txq7_bssid_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq7_pti_maintain_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_pti_maintain_cnt_msb, self.__reg_txq7_pti_maintain_cnt_lsb)
    @reg_txq7_pti_maintain_cnt.setter
    def reg_txq7_pti_maintain_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_pti_maintain_cnt_msb, self.__reg_txq7_pti_maintain_cnt_lsb, value)

    @property
    def reg_txq7_maintain_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_maintain_pti_msb, self.__reg_txq7_maintain_pti_lsb)
    @reg_txq7_maintain_pti.setter
    def reg_txq7_maintain_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_maintain_pti_msb, self.__reg_txq7_maintain_pti_lsb, value)

    @property
    def reg_txq7_rts_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_rts_pti_msb, self.__reg_txq7_rts_pti_lsb)
    @reg_txq7_rts_pti.setter
    def reg_txq7_rts_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_rts_pti_msb, self.__reg_txq7_rts_pti_lsb, value)

    @property
    def reg_txq7_data_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_data_pti_msb, self.__reg_txq7_data_pti_lsb)
    @reg_txq7_data_pti.setter
    def reg_txq7_data_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_data_pti_msb, self.__reg_txq7_data_pti_lsb, value)

    @property
    def reg_txq7_ack_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_ack_pti_msb, self.__reg_txq7_ack_pti_lsb)
    @reg_txq7_ack_pti.setter
    def reg_txq7_ack_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_ack_pti_msb, self.__reg_txq7_ack_pti_lsb, value)

    @property
    def reg_txq7_bssid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_bssid_msb, self.__reg_txq7_bssid_lsb)
    @reg_txq7_bssid.setter
    def reg_txq7_bssid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_bssid_msb, self.__reg_txq7_bssid_lsb, value)
class MACTXQ7_HTSIG(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0xec
        self.__reg_txq7_htsig_lsb = 0
        self.__reg_txq7_htsig_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq7_htsig(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_htsig_msb, self.__reg_txq7_htsig_lsb)
    @reg_txq7_htsig.setter
    def reg_txq7_htsig(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_htsig_msb, self.__reg_txq7_htsig_lsb, value)
class MACTXQ7_VHTSIG1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0xf0
        self.__reg_txq7_vhtsiga_lo_lsb = 0
        self.__reg_txq7_vhtsiga_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq7_vhtsiga_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_vhtsiga_lo_msb, self.__reg_txq7_vhtsiga_lo_lsb)
    @reg_txq7_vhtsiga_lo.setter
    def reg_txq7_vhtsiga_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_vhtsiga_lo_msb, self.__reg_txq7_vhtsiga_lo_lsb, value)
class MACTXQ7_VHTSIG2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0xf4
        self.__reg_txq7_vhtsigb_lsb = 2
        self.__reg_txq7_vhtsigb_msb = 24
        self.__reg_txq7_vhtsiga_hi_lsb = 0
        self.__reg_txq7_vhtsiga_hi_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq7_vhtsigb(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_vhtsigb_msb, self.__reg_txq7_vhtsigb_lsb)
    @reg_txq7_vhtsigb.setter
    def reg_txq7_vhtsigb(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_vhtsigb_msb, self.__reg_txq7_vhtsigb_lsb, value)

    @property
    def reg_txq7_vhtsiga_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_vhtsiga_hi_msb, self.__reg_txq7_vhtsiga_hi_lsb)
    @reg_txq7_vhtsiga_hi.setter
    def reg_txq7_vhtsiga_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_vhtsiga_hi_msb, self.__reg_txq7_vhtsiga_hi_lsb, value)
class MACTXQ7_HT80LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0xf8
        self.__reg_txq7_ht80txop_num_lsb = 24
        self.__reg_txq7_ht80txop_num_msb = 27
        self.__reg_txq7_ht80eof_num_lsb = 22
        self.__reg_txq7_ht80eof_num_msb = 23
        self.__reg_txq7_ht80len_lsb = 0
        self.__reg_txq7_ht80len_msb = 20
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq7_ht80txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_ht80txop_num_msb, self.__reg_txq7_ht80txop_num_lsb)
    @reg_txq7_ht80txop_num.setter
    def reg_txq7_ht80txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_ht80txop_num_msb, self.__reg_txq7_ht80txop_num_lsb, value)

    @property
    def reg_txq7_ht80eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_ht80eof_num_msb, self.__reg_txq7_ht80eof_num_lsb)
    @reg_txq7_ht80eof_num.setter
    def reg_txq7_ht80eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_ht80eof_num_msb, self.__reg_txq7_ht80eof_num_lsb, value)

    @property
    def reg_txq7_ht80len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_ht80len_msb, self.__reg_txq7_ht80len_lsb)
    @reg_txq7_ht80len.setter
    def reg_txq7_ht80len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_ht80len_msb, self.__reg_txq7_ht80len_lsb, value)
class MACTXQ7_HT40LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0xfc
        self.__reg_txq7_ht40txop_num_lsb = 24
        self.__reg_txq7_ht40txop_num_msb = 27
        self.__reg_txq7_ht40eof_num_lsb = 22
        self.__reg_txq7_ht40eof_num_msb = 23
        self.__reg_txq7_ht40len_lsb = 0
        self.__reg_txq7_ht40len_msb = 18
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq7_ht40txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_ht40txop_num_msb, self.__reg_txq7_ht40txop_num_lsb)
    @reg_txq7_ht40txop_num.setter
    def reg_txq7_ht40txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_ht40txop_num_msb, self.__reg_txq7_ht40txop_num_lsb, value)

    @property
    def reg_txq7_ht40eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_ht40eof_num_msb, self.__reg_txq7_ht40eof_num_lsb)
    @reg_txq7_ht40eof_num.setter
    def reg_txq7_ht40eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_ht40eof_num_msb, self.__reg_txq7_ht40eof_num_lsb, value)

    @property
    def reg_txq7_ht40len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_ht40len_msb, self.__reg_txq7_ht40len_lsb)
    @reg_txq7_ht40len.setter
    def reg_txq7_ht40len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_ht40len_msb, self.__reg_txq7_ht40len_lsb, value)
class MACTXQ7_HT20LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x100
        self.__reg_txq7_txop_sel_lsb = 28
        self.__reg_txq7_txop_sel_msb = 29
        self.__reg_txq7_20txop_num_lsb = 24
        self.__reg_txq7_20txop_num_msb = 27
        self.__reg_txq7_20eof_num_lsb = 22
        self.__reg_txq7_20eof_num_msb = 23
        self.__reg_txq7_rts_rate_lsb = 6
        self.__reg_txq7_rts_rate_msb = 13
        self.__reg_txq7_ant_force_lsb = 5
        self.__reg_txq7_ant_force_msb = 5
        self.__reg_txq7_ant_force_value_lsb = 4
        self.__reg_txq7_ant_force_value_msb = 4
        self.__reg_txq7_ant_force_last_lsb = 3
        self.__reg_txq7_ant_force_last_msb = 3
        self.__reg_txrxq7_ant_force_lsb = 2
        self.__reg_txrxq7_ant_force_msb = 2
        self.__reg_txrxq7_ant_force_value_lsb = 1
        self.__reg_txrxq7_ant_force_value_msb = 1
        self.__reg_txrxq7_ant_force_last_lsb = 0
        self.__reg_txrxq7_ant_force_last_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq7_txop_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_txop_sel_msb, self.__reg_txq7_txop_sel_lsb)
    @reg_txq7_txop_sel.setter
    def reg_txq7_txop_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_txop_sel_msb, self.__reg_txq7_txop_sel_lsb, value)

    @property
    def reg_txq7_20txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_20txop_num_msb, self.__reg_txq7_20txop_num_lsb)
    @reg_txq7_20txop_num.setter
    def reg_txq7_20txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_20txop_num_msb, self.__reg_txq7_20txop_num_lsb, value)

    @property
    def reg_txq7_20eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_20eof_num_msb, self.__reg_txq7_20eof_num_lsb)
    @reg_txq7_20eof_num.setter
    def reg_txq7_20eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_20eof_num_msb, self.__reg_txq7_20eof_num_lsb, value)

    @property
    def reg_txq7_rts_rate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_rts_rate_msb, self.__reg_txq7_rts_rate_lsb)
    @reg_txq7_rts_rate.setter
    def reg_txq7_rts_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_rts_rate_msb, self.__reg_txq7_rts_rate_lsb, value)

    @property
    def reg_txq7_ant_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_ant_force_msb, self.__reg_txq7_ant_force_lsb)
    @reg_txq7_ant_force.setter
    def reg_txq7_ant_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_ant_force_msb, self.__reg_txq7_ant_force_lsb, value)

    @property
    def reg_txq7_ant_force_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_ant_force_value_msb, self.__reg_txq7_ant_force_value_lsb)
    @reg_txq7_ant_force_value.setter
    def reg_txq7_ant_force_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_ant_force_value_msb, self.__reg_txq7_ant_force_value_lsb, value)

    @property
    def reg_txq7_ant_force_last(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_ant_force_last_msb, self.__reg_txq7_ant_force_last_lsb)
    @reg_txq7_ant_force_last.setter
    def reg_txq7_ant_force_last(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_ant_force_last_msb, self.__reg_txq7_ant_force_last_lsb, value)

    @property
    def reg_txrxq7_ant_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrxq7_ant_force_msb, self.__reg_txrxq7_ant_force_lsb)
    @reg_txrxq7_ant_force.setter
    def reg_txrxq7_ant_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrxq7_ant_force_msb, self.__reg_txrxq7_ant_force_lsb, value)

    @property
    def reg_txrxq7_ant_force_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrxq7_ant_force_value_msb, self.__reg_txrxq7_ant_force_value_lsb)
    @reg_txrxq7_ant_force_value.setter
    def reg_txrxq7_ant_force_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrxq7_ant_force_value_msb, self.__reg_txrxq7_ant_force_value_lsb, value)

    @property
    def reg_txrxq7_ant_force_last(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrxq7_ant_force_last_msb, self.__reg_txrxq7_ant_force_last_lsb)
    @reg_txrxq7_ant_force_last.setter
    def reg_txrxq7_ant_force_last(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrxq7_ant_force_last_msb, self.__reg_txrxq7_ant_force_last_lsb, value)
class MACTXQ7_DUR(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x104
        self.__reg_txq7_20dur_lsb = 16
        self.__reg_txq7_20dur_msb = 31
        self.__reg_txq7_ht40dur_lsb = 0
        self.__reg_txq7_ht40dur_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq7_20dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_20dur_msb, self.__reg_txq7_20dur_lsb)
    @reg_txq7_20dur.setter
    def reg_txq7_20dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_20dur_msb, self.__reg_txq7_20dur_lsb, value)

    @property
    def reg_txq7_ht40dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_ht40dur_msb, self.__reg_txq7_ht40dur_lsb)
    @reg_txq7_ht40dur.setter
    def reg_txq7_ht40dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_ht40dur_msb, self.__reg_txq7_ht40dur_lsb, value)
class MACTXQ7_DUR2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x108
        self.__reg_txq7_hwseq_fgmd_lsb = 31
        self.__reg_txq7_hwseq_fgmd_msb = 31
        self.__reg_txq7_hwseq_qmfmd_lsb = 29
        self.__reg_txq7_hwseq_qmfmd_msb = 29
        self.__reg_txq7_hwseq_sel_lsb = 17
        self.__reg_txq7_hwseq_sel_msb = 19
        self.__reg_txq7_hwseq_update_lsb = 16
        self.__reg_txq7_hwseq_update_msb = 16
        self.__reg_txq7_ht80dur_lsb = 0
        self.__reg_txq7_ht80dur_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq7_hwseq_fgmd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_hwseq_fgmd_msb, self.__reg_txq7_hwseq_fgmd_lsb)
    @reg_txq7_hwseq_fgmd.setter
    def reg_txq7_hwseq_fgmd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_hwseq_fgmd_msb, self.__reg_txq7_hwseq_fgmd_lsb, value)

    @property
    def reg_txq7_hwseq_qmfmd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_hwseq_qmfmd_msb, self.__reg_txq7_hwseq_qmfmd_lsb)
    @reg_txq7_hwseq_qmfmd.setter
    def reg_txq7_hwseq_qmfmd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_hwseq_qmfmd_msb, self.__reg_txq7_hwseq_qmfmd_lsb, value)

    @property
    def reg_txq7_hwseq_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_hwseq_sel_msb, self.__reg_txq7_hwseq_sel_lsb)
    @reg_txq7_hwseq_sel.setter
    def reg_txq7_hwseq_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_hwseq_sel_msb, self.__reg_txq7_hwseq_sel_lsb, value)

    @property
    def reg_txq7_hwseq_update(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_hwseq_update_msb, self.__reg_txq7_hwseq_update_lsb)
    @reg_txq7_hwseq_update.setter
    def reg_txq7_hwseq_update(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_hwseq_update_msb, self.__reg_txq7_hwseq_update_lsb, value)
    @property
    def default_value(self):
        return 0x0

    @property
    def reg_txq7_ht80dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq7_ht80dur_msb, self.__reg_txq7_ht80dur_lsb)
    @reg_txq7_ht80dur.setter
    def reg_txq7_ht80dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq7_ht80dur_msb, self.__reg_txq7_ht80dur_lsb, value)
class MACTXQ7PMD(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x10c
        self.__txq7complete_num_lsb = 28
        self.__txq7complete_num_msb = 31
        self.__txq7_cbw_lsb = 25
        self.__txq7_cbw_msb = 26
        self.__txq7_rssi_lsb = 16
        self.__txq7_rssi_msb = 23
        self.__txq7complete_state_lsb = 12
        self.__txq7complete_state_msb = 15
        self.__txq7complete_st_match_lsb = 8
        self.__txq7complete_st_match_msb = 11
        self.__txq7complete_errcode_lsb = 0
        self.__txq7complete_errcode_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq7complete_num(self):
        return self.__MEM.rdm(self.__addr, self.__txq7complete_num_msb, self.__txq7complete_num_lsb)
    @txq7complete_num.setter
    def txq7complete_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq7complete_num_msb, self.__txq7complete_num_lsb, value)

    @property
    def txq7_cbw(self):
        return self.__MEM.rdm(self.__addr, self.__txq7_cbw_msb, self.__txq7_cbw_lsb)
    @txq7_cbw.setter
    def txq7_cbw(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq7_cbw_msb, self.__txq7_cbw_lsb, value)

    @property
    def txq7_rssi(self):
        return self.__MEM.rdm(self.__addr, self.__txq7_rssi_msb, self.__txq7_rssi_lsb)
    @txq7_rssi.setter
    def txq7_rssi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq7_rssi_msb, self.__txq7_rssi_lsb, value)

    @property
    def txq7complete_state(self):
        return self.__MEM.rdm(self.__addr, self.__txq7complete_state_msb, self.__txq7complete_state_lsb)
    @txq7complete_state.setter
    def txq7complete_state(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq7complete_state_msb, self.__txq7complete_state_lsb, value)

    @property
    def txq7complete_st_match(self):
        return self.__MEM.rdm(self.__addr, self.__txq7complete_st_match_msb, self.__txq7complete_st_match_lsb)
    @txq7complete_st_match.setter
    def txq7complete_st_match(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq7complete_st_match_msb, self.__txq7complete_st_match_lsb, value)

    @property
    def txq7complete_errcode(self):
        return self.__MEM.rdm(self.__addr, self.__txq7complete_errcode_msb, self.__txq7complete_errcode_lsb)
    @txq7complete_errcode.setter
    def txq7complete_errcode(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq7complete_errcode_msb, self.__txq7complete_errcode_lsb, value)
class MACTXQ7BA_BMHI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x110
        self.__txq7ba_bmhi_lsb = 0
        self.__txq7ba_bmhi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq7ba_bmhi(self):
        return self.__MEM.rdm(self.__addr, self.__txq7ba_bmhi_msb, self.__txq7ba_bmhi_lsb)
    @txq7ba_bmhi.setter
    def txq7ba_bmhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq7ba_bmhi_msb, self.__txq7ba_bmhi_lsb, value)
class MACTXQ7BA_BMLO(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x114
        self.__txq7ba_bmlo_lsb = 0
        self.__txq7ba_bmlo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq7ba_bmlo(self):
        return self.__MEM.rdm(self.__addr, self.__txq7ba_bmlo_msb, self.__txq7ba_bmlo_lsb)
    @txq7ba_bmlo.setter
    def txq7ba_bmlo(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq7ba_bmlo_msb, self.__txq7ba_bmlo_lsb, value)
class MACTXQ7BA_TAHI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x118
        self.__txq7ba_tahi_lsb = 0
        self.__txq7ba_tahi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq7ba_tahi(self):
        return self.__MEM.rdm(self.__addr, self.__txq7ba_tahi_msb, self.__txq7ba_tahi_lsb)
    @txq7ba_tahi.setter
    def txq7ba_tahi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq7ba_tahi_msb, self.__txq7ba_tahi_lsb, value)
class MACTXQ7BA_TALO(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x11c
        self.__txq7ba_talo_lsb = 0
        self.__txq7ba_talo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq7ba_talo(self):
        return self.__MEM.rdm(self.__addr, self.__txq7ba_talo_msb, self.__txq7ba_talo_lsb)
    @txq7ba_talo.setter
    def txq7ba_talo(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq7ba_talo_msb, self.__txq7ba_talo_lsb, value)
class MACTXQ7BA_SSN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x120
        self.__txq7ba_tid_lsb = 12
        self.__txq7ba_tid_msb = 15
        self.__txq7ba_ssn_lsb = 0
        self.__txq7ba_ssn_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq7ba_tid(self):
        return self.__MEM.rdm(self.__addr, self.__txq7ba_tid_msb, self.__txq7ba_tid_lsb)
    @txq7ba_tid.setter
    def txq7ba_tid(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq7ba_tid_msb, self.__txq7ba_tid_lsb, value)

    @property
    def txq7ba_ssn(self):
        return self.__MEM.rdm(self.__addr, self.__txq7ba_ssn_msb, self.__txq7ba_ssn_lsb)
    @txq7ba_ssn.setter
    def txq7ba_ssn(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq7ba_ssn_msb, self.__txq7ba_ssn_lsb, value)
class MACTXQ7_TXSTART_US(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x124
        self.__txq7_txstart_us_lsb = 0
        self.__txq7_txstart_us_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq7_txstart_us(self):
        return self.__MEM.rdm(self.__addr, self.__txq7_txstart_us_msb, self.__txq7_txstart_us_lsb)
    @txq7_txstart_us.setter
    def txq7_txstart_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq7_txstart_us_msb, self.__txq7_txstart_us_lsb, value)
class MACTXQ7_TXSTART_CYC(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x128
        self.__txq7_txrxack_us_hi_lsb = 14
        self.__txq7_txrxack_us_hi_msb = 31
        self.__txq7_txstart_cycle_lsb = 0
        self.__txq7_txstart_cycle_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq7_txrxack_us_hi(self):
        return self.__MEM.rdm(self.__addr, self.__txq7_txrxack_us_hi_msb, self.__txq7_txrxack_us_hi_lsb)
    @txq7_txrxack_us_hi.setter
    def txq7_txrxack_us_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq7_txrxack_us_hi_msb, self.__txq7_txrxack_us_hi_lsb, value)

    @property
    def txq7_txstart_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__txq7_txstart_cycle_msb, self.__txq7_txstart_cycle_lsb)
    @txq7_txstart_cycle.setter
    def txq7_txstart_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq7_txstart_cycle_msb, self.__txq7_txstart_cycle_lsb, value)
class MACTXQ7_TXRXACK_CYC(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x12c
        self.__txq7_txrxack_us_lsb = 18
        self.__txq7_txrxack_us_msb = 31
        self.__txq7_txrxack_cycdec_lsb = 7
        self.__txq7_txrxack_cycdec_msb = 17
        self.__txq7_txrxack_cycle_lsb = 0
        self.__txq7_txrxack_cycle_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq7_txrxack_us(self):
        return self.__MEM.rdm(self.__addr, self.__txq7_txrxack_us_msb, self.__txq7_txrxack_us_lsb)
    @txq7_txrxack_us.setter
    def txq7_txrxack_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq7_txrxack_us_msb, self.__txq7_txrxack_us_lsb, value)

    @property
    def txq7_txrxack_cycdec(self):
        return self.__MEM.rdm(self.__addr, self.__txq7_txrxack_cycdec_msb, self.__txq7_txrxack_cycdec_lsb)
    @txq7_txrxack_cycdec.setter
    def txq7_txrxack_cycdec(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq7_txrxack_cycdec_msb, self.__txq7_txrxack_cycdec_lsb, value)

    @property
    def txq7_txrxack_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__txq7_txrxack_cycle_msb, self.__txq7_txrxack_cycle_lsb)
    @txq7_txrxack_cycle.setter
    def txq7_txrxack_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq7_txrxack_cycle_msb, self.__txq7_txrxack_cycle_lsb, value)
class MACTXQ6_PLCP1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x130
        self.__reg_txq6_data_wbd_lsb = 31
        self.__reg_txq6_data_wbd_msb = 31
        self.__reg_txq6_rts_wbd_lsb = 30
        self.__reg_txq6_rts_wbd_msb = 30
        self.__reg_txq6_force_bw_lsb = 29
        self.__reg_txq6_force_bw_msb = 29
        self.__reg_txq6_nonhtdup_lsb = 27
        self.__reg_txq6_nonhtdup_msb = 28
        self.__reg_txq6_sigmode_lsb = 25
        self.__reg_txq6_sigmode_msb = 26
        self.__reg_txq6_kid_lsb = 17
        self.__reg_txq6_kid_msb = 24
        self.__reg_txq6_rate_lsb = 12
        self.__reg_txq6_rate_msb = 16
        self.__reg_txq6_length_lsb = 0
        self.__reg_txq6_length_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq6_data_wbd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_data_wbd_msb, self.__reg_txq6_data_wbd_lsb)
    @reg_txq6_data_wbd.setter
    def reg_txq6_data_wbd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_data_wbd_msb, self.__reg_txq6_data_wbd_lsb, value)

    @property
    def reg_txq6_rts_wbd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_rts_wbd_msb, self.__reg_txq6_rts_wbd_lsb)
    @reg_txq6_rts_wbd.setter
    def reg_txq6_rts_wbd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_rts_wbd_msb, self.__reg_txq6_rts_wbd_lsb, value)

    @property
    def reg_txq6_force_bw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_force_bw_msb, self.__reg_txq6_force_bw_lsb)
    @reg_txq6_force_bw.setter
    def reg_txq6_force_bw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_force_bw_msb, self.__reg_txq6_force_bw_lsb, value)

    @property
    def reg_txq6_nonhtdup(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_nonhtdup_msb, self.__reg_txq6_nonhtdup_lsb)
    @reg_txq6_nonhtdup.setter
    def reg_txq6_nonhtdup(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_nonhtdup_msb, self.__reg_txq6_nonhtdup_lsb, value)

    @property
    def reg_txq6_sigmode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_sigmode_msb, self.__reg_txq6_sigmode_lsb)
    @reg_txq6_sigmode.setter
    def reg_txq6_sigmode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_sigmode_msb, self.__reg_txq6_sigmode_lsb, value)

    @property
    def reg_txq6_kid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_kid_msb, self.__reg_txq6_kid_lsb)
    @reg_txq6_kid.setter
    def reg_txq6_kid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_kid_msb, self.__reg_txq6_kid_lsb, value)

    @property
    def reg_txq6_rate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_rate_msb, self.__reg_txq6_rate_lsb)
    @reg_txq6_rate.setter
    def reg_txq6_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_rate_msb, self.__reg_txq6_rate_lsb, value)

    @property
    def reg_txq6_length(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_length_msb, self.__reg_txq6_length_lsb)
    @reg_txq6_length.setter
    def reg_txq6_length(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_length_msb, self.__reg_txq6_length_lsb, value)
class MACTXQ6_PTI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x134
        self.__reg_txq6_pti_maintain_cnt_lsb = 20
        self.__reg_txq6_pti_maintain_cnt_msb = 31
        self.__reg_txq6_maintain_pti_lsb = 16
        self.__reg_txq6_maintain_pti_msb = 19
        self.__reg_txq6_rts_pti_lsb = 12
        self.__reg_txq6_rts_pti_msb = 15
        self.__reg_txq6_data_pti_lsb = 8
        self.__reg_txq6_data_pti_msb = 11
        self.__reg_txq6_ack_pti_lsb = 4
        self.__reg_txq6_ack_pti_msb = 7
        self.__reg_txq6_bssid_lsb = 0
        self.__reg_txq6_bssid_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq6_pti_maintain_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_pti_maintain_cnt_msb, self.__reg_txq6_pti_maintain_cnt_lsb)
    @reg_txq6_pti_maintain_cnt.setter
    def reg_txq6_pti_maintain_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_pti_maintain_cnt_msb, self.__reg_txq6_pti_maintain_cnt_lsb, value)

    @property
    def reg_txq6_maintain_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_maintain_pti_msb, self.__reg_txq6_maintain_pti_lsb)
    @reg_txq6_maintain_pti.setter
    def reg_txq6_maintain_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_maintain_pti_msb, self.__reg_txq6_maintain_pti_lsb, value)

    @property
    def reg_txq6_rts_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_rts_pti_msb, self.__reg_txq6_rts_pti_lsb)
    @reg_txq6_rts_pti.setter
    def reg_txq6_rts_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_rts_pti_msb, self.__reg_txq6_rts_pti_lsb, value)

    @property
    def reg_txq6_data_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_data_pti_msb, self.__reg_txq6_data_pti_lsb)
    @reg_txq6_data_pti.setter
    def reg_txq6_data_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_data_pti_msb, self.__reg_txq6_data_pti_lsb, value)

    @property
    def reg_txq6_ack_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_ack_pti_msb, self.__reg_txq6_ack_pti_lsb)
    @reg_txq6_ack_pti.setter
    def reg_txq6_ack_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_ack_pti_msb, self.__reg_txq6_ack_pti_lsb, value)

    @property
    def reg_txq6_bssid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_bssid_msb, self.__reg_txq6_bssid_lsb)
    @reg_txq6_bssid.setter
    def reg_txq6_bssid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_bssid_msb, self.__reg_txq6_bssid_lsb, value)
class MACTXQ6_HTSIG(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x138
        self.__reg_txq6_htsig_lsb = 0
        self.__reg_txq6_htsig_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq6_htsig(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_htsig_msb, self.__reg_txq6_htsig_lsb)
    @reg_txq6_htsig.setter
    def reg_txq6_htsig(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_htsig_msb, self.__reg_txq6_htsig_lsb, value)
class MACTXQ6_VHTSIG1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x13c
        self.__reg_txq6_vhtsiga_lo_lsb = 0
        self.__reg_txq6_vhtsiga_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq6_vhtsiga_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_vhtsiga_lo_msb, self.__reg_txq6_vhtsiga_lo_lsb)
    @reg_txq6_vhtsiga_lo.setter
    def reg_txq6_vhtsiga_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_vhtsiga_lo_msb, self.__reg_txq6_vhtsiga_lo_lsb, value)
class MACTXQ6_VHTSIG2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x140
        self.__reg_txq6_vhtsigb_lsb = 2
        self.__reg_txq6_vhtsigb_msb = 24
        self.__reg_txq6_vhtsiga_hi_lsb = 0
        self.__reg_txq6_vhtsiga_hi_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq6_vhtsigb(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_vhtsigb_msb, self.__reg_txq6_vhtsigb_lsb)
    @reg_txq6_vhtsigb.setter
    def reg_txq6_vhtsigb(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_vhtsigb_msb, self.__reg_txq6_vhtsigb_lsb, value)

    @property
    def reg_txq6_vhtsiga_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_vhtsiga_hi_msb, self.__reg_txq6_vhtsiga_hi_lsb)
    @reg_txq6_vhtsiga_hi.setter
    def reg_txq6_vhtsiga_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_vhtsiga_hi_msb, self.__reg_txq6_vhtsiga_hi_lsb, value)
class MACTXQ6_HT80LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x144
        self.__reg_txq6_ht80txop_num_lsb = 24
        self.__reg_txq6_ht80txop_num_msb = 27
        self.__reg_txq6_ht80eof_num_lsb = 22
        self.__reg_txq6_ht80eof_num_msb = 23
        self.__reg_txq6_ht80len_lsb = 0
        self.__reg_txq6_ht80len_msb = 20
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq6_ht80txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_ht80txop_num_msb, self.__reg_txq6_ht80txop_num_lsb)
    @reg_txq6_ht80txop_num.setter
    def reg_txq6_ht80txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_ht80txop_num_msb, self.__reg_txq6_ht80txop_num_lsb, value)

    @property
    def reg_txq6_ht80eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_ht80eof_num_msb, self.__reg_txq6_ht80eof_num_lsb)
    @reg_txq6_ht80eof_num.setter
    def reg_txq6_ht80eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_ht80eof_num_msb, self.__reg_txq6_ht80eof_num_lsb, value)

    @property
    def reg_txq6_ht80len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_ht80len_msb, self.__reg_txq6_ht80len_lsb)
    @reg_txq6_ht80len.setter
    def reg_txq6_ht80len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_ht80len_msb, self.__reg_txq6_ht80len_lsb, value)
class MACTXQ6_HT40LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x148
        self.__reg_txq6_ht40txop_num_lsb = 24
        self.__reg_txq6_ht40txop_num_msb = 27
        self.__reg_txq6_ht40eof_num_lsb = 22
        self.__reg_txq6_ht40eof_num_msb = 23
        self.__reg_txq6_ht40len_lsb = 0
        self.__reg_txq6_ht40len_msb = 18
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq6_ht40txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_ht40txop_num_msb, self.__reg_txq6_ht40txop_num_lsb)
    @reg_txq6_ht40txop_num.setter
    def reg_txq6_ht40txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_ht40txop_num_msb, self.__reg_txq6_ht40txop_num_lsb, value)

    @property
    def reg_txq6_ht40eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_ht40eof_num_msb, self.__reg_txq6_ht40eof_num_lsb)
    @reg_txq6_ht40eof_num.setter
    def reg_txq6_ht40eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_ht40eof_num_msb, self.__reg_txq6_ht40eof_num_lsb, value)

    @property
    def reg_txq6_ht40len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_ht40len_msb, self.__reg_txq6_ht40len_lsb)
    @reg_txq6_ht40len.setter
    def reg_txq6_ht40len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_ht40len_msb, self.__reg_txq6_ht40len_lsb, value)
class MACTXQ6_HT20LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x14c
        self.__reg_txq6_txop_sel_lsb = 28
        self.__reg_txq6_txop_sel_msb = 29
        self.__reg_txq6_20txop_num_lsb = 24
        self.__reg_txq6_20txop_num_msb = 27
        self.__reg_txq6_20eof_num_lsb = 22
        self.__reg_txq6_20eof_num_msb = 23
        self.__reg_txq6_rts_rate_lsb = 6
        self.__reg_txq6_rts_rate_msb = 13
        self.__reg_txq6_ant_force_lsb = 5
        self.__reg_txq6_ant_force_msb = 5
        self.__reg_txq6_ant_force_value_lsb = 4
        self.__reg_txq6_ant_force_value_msb = 4
        self.__reg_txq6_ant_force_last_lsb = 3
        self.__reg_txq6_ant_force_last_msb = 3
        self.__reg_txrxq6_ant_force_lsb = 2
        self.__reg_txrxq6_ant_force_msb = 2
        self.__reg_txrxq6_ant_force_value_lsb = 1
        self.__reg_txrxq6_ant_force_value_msb = 1
        self.__reg_txrxq6_ant_force_last_lsb = 0
        self.__reg_txrxq6_ant_force_last_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq6_txop_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_txop_sel_msb, self.__reg_txq6_txop_sel_lsb)
    @reg_txq6_txop_sel.setter
    def reg_txq6_txop_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_txop_sel_msb, self.__reg_txq6_txop_sel_lsb, value)

    @property
    def reg_txq6_20txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_20txop_num_msb, self.__reg_txq6_20txop_num_lsb)
    @reg_txq6_20txop_num.setter
    def reg_txq6_20txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_20txop_num_msb, self.__reg_txq6_20txop_num_lsb, value)

    @property
    def reg_txq6_20eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_20eof_num_msb, self.__reg_txq6_20eof_num_lsb)
    @reg_txq6_20eof_num.setter
    def reg_txq6_20eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_20eof_num_msb, self.__reg_txq6_20eof_num_lsb, value)

    @property
    def reg_txq6_rts_rate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_rts_rate_msb, self.__reg_txq6_rts_rate_lsb)
    @reg_txq6_rts_rate.setter
    def reg_txq6_rts_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_rts_rate_msb, self.__reg_txq6_rts_rate_lsb, value)

    @property
    def reg_txq6_ant_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_ant_force_msb, self.__reg_txq6_ant_force_lsb)
    @reg_txq6_ant_force.setter
    def reg_txq6_ant_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_ant_force_msb, self.__reg_txq6_ant_force_lsb, value)

    @property
    def reg_txq6_ant_force_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_ant_force_value_msb, self.__reg_txq6_ant_force_value_lsb)
    @reg_txq6_ant_force_value.setter
    def reg_txq6_ant_force_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_ant_force_value_msb, self.__reg_txq6_ant_force_value_lsb, value)

    @property
    def reg_txq6_ant_force_last(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_ant_force_last_msb, self.__reg_txq6_ant_force_last_lsb)
    @reg_txq6_ant_force_last.setter
    def reg_txq6_ant_force_last(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_ant_force_last_msb, self.__reg_txq6_ant_force_last_lsb, value)

    @property
    def reg_txrxq6_ant_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrxq6_ant_force_msb, self.__reg_txrxq6_ant_force_lsb)
    @reg_txrxq6_ant_force.setter
    def reg_txrxq6_ant_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrxq6_ant_force_msb, self.__reg_txrxq6_ant_force_lsb, value)

    @property
    def reg_txrxq6_ant_force_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrxq6_ant_force_value_msb, self.__reg_txrxq6_ant_force_value_lsb)
    @reg_txrxq6_ant_force_value.setter
    def reg_txrxq6_ant_force_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrxq6_ant_force_value_msb, self.__reg_txrxq6_ant_force_value_lsb, value)

    @property
    def reg_txrxq6_ant_force_last(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrxq6_ant_force_last_msb, self.__reg_txrxq6_ant_force_last_lsb)
    @reg_txrxq6_ant_force_last.setter
    def reg_txrxq6_ant_force_last(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrxq6_ant_force_last_msb, self.__reg_txrxq6_ant_force_last_lsb, value)
class MACTXQ6_DUR(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x150
        self.__reg_txq6_20dur_lsb = 16
        self.__reg_txq6_20dur_msb = 31
        self.__reg_txq6_ht40dur_lsb = 0
        self.__reg_txq6_ht40dur_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq6_20dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_20dur_msb, self.__reg_txq6_20dur_lsb)
    @reg_txq6_20dur.setter
    def reg_txq6_20dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_20dur_msb, self.__reg_txq6_20dur_lsb, value)

    @property
    def reg_txq6_ht40dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_ht40dur_msb, self.__reg_txq6_ht40dur_lsb)
    @reg_txq6_ht40dur.setter
    def reg_txq6_ht40dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_ht40dur_msb, self.__reg_txq6_ht40dur_lsb, value)
class MACTXQ6_DUR2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x154
        self.__reg_txq6_hwseq_fgmd_lsb = 31
        self.__reg_txq6_hwseq_fgmd_msb = 31
        self.__reg_txq6_hwseq_qmfmd_lsb = 29
        self.__reg_txq6_hwseq_qmfmd_msb = 29
        self.__reg_txq6_hwseq_sel_lsb = 17
        self.__reg_txq6_hwseq_sel_msb = 19
        self.__reg_txq6_hwseq_update_lsb = 16
        self.__reg_txq6_hwseq_update_msb = 16
        self.__reg_txq6_ht80dur_lsb = 0
        self.__reg_txq6_ht80dur_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq6_hwseq_fgmd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_hwseq_fgmd_msb, self.__reg_txq6_hwseq_fgmd_lsb)
    @reg_txq6_hwseq_fgmd.setter
    def reg_txq6_hwseq_fgmd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_hwseq_fgmd_msb, self.__reg_txq6_hwseq_fgmd_lsb, value)

    @property
    def reg_txq6_hwseq_qmfmd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_hwseq_qmfmd_msb, self.__reg_txq6_hwseq_qmfmd_lsb)
    @reg_txq6_hwseq_qmfmd.setter
    def reg_txq6_hwseq_qmfmd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_hwseq_qmfmd_msb, self.__reg_txq6_hwseq_qmfmd_lsb, value)

    @property
    def reg_txq6_hwseq_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_hwseq_sel_msb, self.__reg_txq6_hwseq_sel_lsb)
    @reg_txq6_hwseq_sel.setter
    def reg_txq6_hwseq_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_hwseq_sel_msb, self.__reg_txq6_hwseq_sel_lsb, value)

    @property
    def reg_txq6_hwseq_update(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_hwseq_update_msb, self.__reg_txq6_hwseq_update_lsb)
    @reg_txq6_hwseq_update.setter
    def reg_txq6_hwseq_update(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_hwseq_update_msb, self.__reg_txq6_hwseq_update_lsb, value)
    @property
    def default_value(self):
        return 0x0

    @property
    def reg_txq6_ht80dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq6_ht80dur_msb, self.__reg_txq6_ht80dur_lsb)
    @reg_txq6_ht80dur.setter
    def reg_txq6_ht80dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq6_ht80dur_msb, self.__reg_txq6_ht80dur_lsb, value)
class MACTXQ6PMD(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x158
        self.__txq6complete_num_lsb = 28
        self.__txq6complete_num_msb = 31
        self.__txq6_cbw_lsb = 25
        self.__txq6_cbw_msb = 26
        self.__txq6_rssi_lsb = 16
        self.__txq6_rssi_msb = 23
        self.__txq6complete_state_lsb = 12
        self.__txq6complete_state_msb = 15
        self.__txq6complete_st_match_lsb = 8
        self.__txq6complete_st_match_msb = 11
        self.__txq6complete_errcode_lsb = 0
        self.__txq6complete_errcode_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq6complete_num(self):
        return self.__MEM.rdm(self.__addr, self.__txq6complete_num_msb, self.__txq6complete_num_lsb)
    @txq6complete_num.setter
    def txq6complete_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq6complete_num_msb, self.__txq6complete_num_lsb, value)

    @property
    def txq6_cbw(self):
        return self.__MEM.rdm(self.__addr, self.__txq6_cbw_msb, self.__txq6_cbw_lsb)
    @txq6_cbw.setter
    def txq6_cbw(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq6_cbw_msb, self.__txq6_cbw_lsb, value)

    @property
    def txq6_rssi(self):
        return self.__MEM.rdm(self.__addr, self.__txq6_rssi_msb, self.__txq6_rssi_lsb)
    @txq6_rssi.setter
    def txq6_rssi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq6_rssi_msb, self.__txq6_rssi_lsb, value)

    @property
    def txq6complete_state(self):
        return self.__MEM.rdm(self.__addr, self.__txq6complete_state_msb, self.__txq6complete_state_lsb)
    @txq6complete_state.setter
    def txq6complete_state(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq6complete_state_msb, self.__txq6complete_state_lsb, value)

    @property
    def txq6complete_st_match(self):
        return self.__MEM.rdm(self.__addr, self.__txq6complete_st_match_msb, self.__txq6complete_st_match_lsb)
    @txq6complete_st_match.setter
    def txq6complete_st_match(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq6complete_st_match_msb, self.__txq6complete_st_match_lsb, value)

    @property
    def txq6complete_errcode(self):
        return self.__MEM.rdm(self.__addr, self.__txq6complete_errcode_msb, self.__txq6complete_errcode_lsb)
    @txq6complete_errcode.setter
    def txq6complete_errcode(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq6complete_errcode_msb, self.__txq6complete_errcode_lsb, value)
class MACTXQ6BA_BMHI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x15c
        self.__txq6ba_bmhi_lsb = 0
        self.__txq6ba_bmhi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq6ba_bmhi(self):
        return self.__MEM.rdm(self.__addr, self.__txq6ba_bmhi_msb, self.__txq6ba_bmhi_lsb)
    @txq6ba_bmhi.setter
    def txq6ba_bmhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq6ba_bmhi_msb, self.__txq6ba_bmhi_lsb, value)
class MACTXQ6BA_BMLO(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x160
        self.__txq6ba_bmlo_lsb = 0
        self.__txq6ba_bmlo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq6ba_bmlo(self):
        return self.__MEM.rdm(self.__addr, self.__txq6ba_bmlo_msb, self.__txq6ba_bmlo_lsb)
    @txq6ba_bmlo.setter
    def txq6ba_bmlo(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq6ba_bmlo_msb, self.__txq6ba_bmlo_lsb, value)
class MACTXQ6BA_TAHI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x164
        self.__txq6ba_tahi_lsb = 0
        self.__txq6ba_tahi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq6ba_tahi(self):
        return self.__MEM.rdm(self.__addr, self.__txq6ba_tahi_msb, self.__txq6ba_tahi_lsb)
    @txq6ba_tahi.setter
    def txq6ba_tahi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq6ba_tahi_msb, self.__txq6ba_tahi_lsb, value)
class MACTXQ6BA_TALO(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x168
        self.__txq6ba_talo_lsb = 0
        self.__txq6ba_talo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq6ba_talo(self):
        return self.__MEM.rdm(self.__addr, self.__txq6ba_talo_msb, self.__txq6ba_talo_lsb)
    @txq6ba_talo.setter
    def txq6ba_talo(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq6ba_talo_msb, self.__txq6ba_talo_lsb, value)
class MACTXQ6BA_SSN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x16c
        self.__txq6ba_tid_lsb = 12
        self.__txq6ba_tid_msb = 15
        self.__txq6ba_ssn_lsb = 0
        self.__txq6ba_ssn_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq6ba_tid(self):
        return self.__MEM.rdm(self.__addr, self.__txq6ba_tid_msb, self.__txq6ba_tid_lsb)
    @txq6ba_tid.setter
    def txq6ba_tid(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq6ba_tid_msb, self.__txq6ba_tid_lsb, value)

    @property
    def txq6ba_ssn(self):
        return self.__MEM.rdm(self.__addr, self.__txq6ba_ssn_msb, self.__txq6ba_ssn_lsb)
    @txq6ba_ssn.setter
    def txq6ba_ssn(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq6ba_ssn_msb, self.__txq6ba_ssn_lsb, value)
class MACTXQ6_TXSTART_US(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x170
        self.__txq6_txstart_us_lsb = 0
        self.__txq6_txstart_us_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq6_txstart_us(self):
        return self.__MEM.rdm(self.__addr, self.__txq6_txstart_us_msb, self.__txq6_txstart_us_lsb)
    @txq6_txstart_us.setter
    def txq6_txstart_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq6_txstart_us_msb, self.__txq6_txstart_us_lsb, value)
class MACTXQ6_TXSTART_CYC(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x174
        self.__txq6_txrxack_us_hi_lsb = 14
        self.__txq6_txrxack_us_hi_msb = 31
        self.__txq6_txstart_cycle_lsb = 0
        self.__txq6_txstart_cycle_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq6_txrxack_us_hi(self):
        return self.__MEM.rdm(self.__addr, self.__txq6_txrxack_us_hi_msb, self.__txq6_txrxack_us_hi_lsb)
    @txq6_txrxack_us_hi.setter
    def txq6_txrxack_us_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq6_txrxack_us_hi_msb, self.__txq6_txrxack_us_hi_lsb, value)

    @property
    def txq6_txstart_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__txq6_txstart_cycle_msb, self.__txq6_txstart_cycle_lsb)
    @txq6_txstart_cycle.setter
    def txq6_txstart_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq6_txstart_cycle_msb, self.__txq6_txstart_cycle_lsb, value)
class MACTXQ6_TXRXACK_CYC(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x178
        self.__txq6_txrxack_us_lsb = 18
        self.__txq6_txrxack_us_msb = 31
        self.__txq6_txrxack_cycdec_lsb = 7
        self.__txq6_txrxack_cycdec_msb = 17
        self.__txq6_txrxack_cycle_lsb = 0
        self.__txq6_txrxack_cycle_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq6_txrxack_us(self):
        return self.__MEM.rdm(self.__addr, self.__txq6_txrxack_us_msb, self.__txq6_txrxack_us_lsb)
    @txq6_txrxack_us.setter
    def txq6_txrxack_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq6_txrxack_us_msb, self.__txq6_txrxack_us_lsb, value)

    @property
    def txq6_txrxack_cycdec(self):
        return self.__MEM.rdm(self.__addr, self.__txq6_txrxack_cycdec_msb, self.__txq6_txrxack_cycdec_lsb)
    @txq6_txrxack_cycdec.setter
    def txq6_txrxack_cycdec(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq6_txrxack_cycdec_msb, self.__txq6_txrxack_cycdec_lsb, value)

    @property
    def txq6_txrxack_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__txq6_txrxack_cycle_msb, self.__txq6_txrxack_cycle_lsb)
    @txq6_txrxack_cycle.setter
    def txq6_txrxack_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq6_txrxack_cycle_msb, self.__txq6_txrxack_cycle_lsb, value)
class MACTXQ5_PLCP1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x17c
        self.__reg_txq5_data_wbd_lsb = 31
        self.__reg_txq5_data_wbd_msb = 31
        self.__reg_txq5_rts_wbd_lsb = 30
        self.__reg_txq5_rts_wbd_msb = 30
        self.__reg_txq5_force_bw_lsb = 29
        self.__reg_txq5_force_bw_msb = 29
        self.__reg_txq5_nonhtdup_lsb = 27
        self.__reg_txq5_nonhtdup_msb = 28
        self.__reg_txq5_sigmode_lsb = 25
        self.__reg_txq5_sigmode_msb = 26
        self.__reg_txq5_kid_lsb = 17
        self.__reg_txq5_kid_msb = 24
        self.__reg_txq5_rate_lsb = 12
        self.__reg_txq5_rate_msb = 16
        self.__reg_txq5_length_lsb = 0
        self.__reg_txq5_length_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq5_data_wbd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_data_wbd_msb, self.__reg_txq5_data_wbd_lsb)
    @reg_txq5_data_wbd.setter
    def reg_txq5_data_wbd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_data_wbd_msb, self.__reg_txq5_data_wbd_lsb, value)

    @property
    def reg_txq5_rts_wbd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_rts_wbd_msb, self.__reg_txq5_rts_wbd_lsb)
    @reg_txq5_rts_wbd.setter
    def reg_txq5_rts_wbd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_rts_wbd_msb, self.__reg_txq5_rts_wbd_lsb, value)

    @property
    def reg_txq5_force_bw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_force_bw_msb, self.__reg_txq5_force_bw_lsb)
    @reg_txq5_force_bw.setter
    def reg_txq5_force_bw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_force_bw_msb, self.__reg_txq5_force_bw_lsb, value)

    @property
    def reg_txq5_nonhtdup(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_nonhtdup_msb, self.__reg_txq5_nonhtdup_lsb)
    @reg_txq5_nonhtdup.setter
    def reg_txq5_nonhtdup(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_nonhtdup_msb, self.__reg_txq5_nonhtdup_lsb, value)

    @property
    def reg_txq5_sigmode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_sigmode_msb, self.__reg_txq5_sigmode_lsb)
    @reg_txq5_sigmode.setter
    def reg_txq5_sigmode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_sigmode_msb, self.__reg_txq5_sigmode_lsb, value)

    @property
    def reg_txq5_kid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_kid_msb, self.__reg_txq5_kid_lsb)
    @reg_txq5_kid.setter
    def reg_txq5_kid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_kid_msb, self.__reg_txq5_kid_lsb, value)

    @property
    def reg_txq5_rate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_rate_msb, self.__reg_txq5_rate_lsb)
    @reg_txq5_rate.setter
    def reg_txq5_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_rate_msb, self.__reg_txq5_rate_lsb, value)

    @property
    def reg_txq5_length(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_length_msb, self.__reg_txq5_length_lsb)
    @reg_txq5_length.setter
    def reg_txq5_length(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_length_msb, self.__reg_txq5_length_lsb, value)
class MACTXQ5_PTI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x180
        self.__reg_txq5_pti_maintain_cnt_lsb = 20
        self.__reg_txq5_pti_maintain_cnt_msb = 31
        self.__reg_txq5_maintain_pti_lsb = 16
        self.__reg_txq5_maintain_pti_msb = 19
        self.__reg_txq5_rts_pti_lsb = 12
        self.__reg_txq5_rts_pti_msb = 15
        self.__reg_txq5_data_pti_lsb = 8
        self.__reg_txq5_data_pti_msb = 11
        self.__reg_txq5_ack_pti_lsb = 4
        self.__reg_txq5_ack_pti_msb = 7
        self.__reg_txq5_bssid_lsb = 0
        self.__reg_txq5_bssid_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq5_pti_maintain_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_pti_maintain_cnt_msb, self.__reg_txq5_pti_maintain_cnt_lsb)
    @reg_txq5_pti_maintain_cnt.setter
    def reg_txq5_pti_maintain_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_pti_maintain_cnt_msb, self.__reg_txq5_pti_maintain_cnt_lsb, value)

    @property
    def reg_txq5_maintain_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_maintain_pti_msb, self.__reg_txq5_maintain_pti_lsb)
    @reg_txq5_maintain_pti.setter
    def reg_txq5_maintain_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_maintain_pti_msb, self.__reg_txq5_maintain_pti_lsb, value)

    @property
    def reg_txq5_rts_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_rts_pti_msb, self.__reg_txq5_rts_pti_lsb)
    @reg_txq5_rts_pti.setter
    def reg_txq5_rts_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_rts_pti_msb, self.__reg_txq5_rts_pti_lsb, value)

    @property
    def reg_txq5_data_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_data_pti_msb, self.__reg_txq5_data_pti_lsb)
    @reg_txq5_data_pti.setter
    def reg_txq5_data_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_data_pti_msb, self.__reg_txq5_data_pti_lsb, value)

    @property
    def reg_txq5_ack_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_ack_pti_msb, self.__reg_txq5_ack_pti_lsb)
    @reg_txq5_ack_pti.setter
    def reg_txq5_ack_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_ack_pti_msb, self.__reg_txq5_ack_pti_lsb, value)

    @property
    def reg_txq5_bssid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_bssid_msb, self.__reg_txq5_bssid_lsb)
    @reg_txq5_bssid.setter
    def reg_txq5_bssid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_bssid_msb, self.__reg_txq5_bssid_lsb, value)
class MACTXQ5_HTSIG(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x184
        self.__reg_txq5_htsig_lsb = 0
        self.__reg_txq5_htsig_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq5_htsig(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_htsig_msb, self.__reg_txq5_htsig_lsb)
    @reg_txq5_htsig.setter
    def reg_txq5_htsig(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_htsig_msb, self.__reg_txq5_htsig_lsb, value)
class MACTXQ5_VHTSIG1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x188
        self.__reg_txq5_vhtsiga_lo_lsb = 0
        self.__reg_txq5_vhtsiga_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq5_vhtsiga_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_vhtsiga_lo_msb, self.__reg_txq5_vhtsiga_lo_lsb)
    @reg_txq5_vhtsiga_lo.setter
    def reg_txq5_vhtsiga_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_vhtsiga_lo_msb, self.__reg_txq5_vhtsiga_lo_lsb, value)
class MACTXQ5_VHTSIG2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x18c
        self.__reg_txq5_vhtsigb_lsb = 2
        self.__reg_txq5_vhtsigb_msb = 24
        self.__reg_txq5_vhtsiga_hi_lsb = 0
        self.__reg_txq5_vhtsiga_hi_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq5_vhtsigb(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_vhtsigb_msb, self.__reg_txq5_vhtsigb_lsb)
    @reg_txq5_vhtsigb.setter
    def reg_txq5_vhtsigb(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_vhtsigb_msb, self.__reg_txq5_vhtsigb_lsb, value)

    @property
    def reg_txq5_vhtsiga_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_vhtsiga_hi_msb, self.__reg_txq5_vhtsiga_hi_lsb)
    @reg_txq5_vhtsiga_hi.setter
    def reg_txq5_vhtsiga_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_vhtsiga_hi_msb, self.__reg_txq5_vhtsiga_hi_lsb, value)
class MACTXQ5_HT80LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x190
        self.__reg_txq5_ht80txop_num_lsb = 24
        self.__reg_txq5_ht80txop_num_msb = 27
        self.__reg_txq5_ht80eof_num_lsb = 22
        self.__reg_txq5_ht80eof_num_msb = 23
        self.__reg_txq5_ht80len_lsb = 0
        self.__reg_txq5_ht80len_msb = 20
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq5_ht80txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_ht80txop_num_msb, self.__reg_txq5_ht80txop_num_lsb)
    @reg_txq5_ht80txop_num.setter
    def reg_txq5_ht80txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_ht80txop_num_msb, self.__reg_txq5_ht80txop_num_lsb, value)

    @property
    def reg_txq5_ht80eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_ht80eof_num_msb, self.__reg_txq5_ht80eof_num_lsb)
    @reg_txq5_ht80eof_num.setter
    def reg_txq5_ht80eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_ht80eof_num_msb, self.__reg_txq5_ht80eof_num_lsb, value)

    @property
    def reg_txq5_ht80len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_ht80len_msb, self.__reg_txq5_ht80len_lsb)
    @reg_txq5_ht80len.setter
    def reg_txq5_ht80len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_ht80len_msb, self.__reg_txq5_ht80len_lsb, value)
class MACTXQ5_HT40LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x194
        self.__reg_txq5_ht40txop_num_lsb = 24
        self.__reg_txq5_ht40txop_num_msb = 27
        self.__reg_txq5_ht40eof_num_lsb = 22
        self.__reg_txq5_ht40eof_num_msb = 23
        self.__reg_txq5_ht40len_lsb = 0
        self.__reg_txq5_ht40len_msb = 18
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq5_ht40txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_ht40txop_num_msb, self.__reg_txq5_ht40txop_num_lsb)
    @reg_txq5_ht40txop_num.setter
    def reg_txq5_ht40txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_ht40txop_num_msb, self.__reg_txq5_ht40txop_num_lsb, value)

    @property
    def reg_txq5_ht40eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_ht40eof_num_msb, self.__reg_txq5_ht40eof_num_lsb)
    @reg_txq5_ht40eof_num.setter
    def reg_txq5_ht40eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_ht40eof_num_msb, self.__reg_txq5_ht40eof_num_lsb, value)

    @property
    def reg_txq5_ht40len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_ht40len_msb, self.__reg_txq5_ht40len_lsb)
    @reg_txq5_ht40len.setter
    def reg_txq5_ht40len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_ht40len_msb, self.__reg_txq5_ht40len_lsb, value)
class MACTXQ5_HT20LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x198
        self.__reg_txq5_txop_sel_lsb = 28
        self.__reg_txq5_txop_sel_msb = 29
        self.__reg_txq5_20txop_num_lsb = 24
        self.__reg_txq5_20txop_num_msb = 27
        self.__reg_txq5_20eof_num_lsb = 22
        self.__reg_txq5_20eof_num_msb = 23
        self.__reg_txq5_rts_rate_lsb = 6
        self.__reg_txq5_rts_rate_msb = 13
        self.__reg_txq5_ant_force_lsb = 5
        self.__reg_txq5_ant_force_msb = 5
        self.__reg_txq5_ant_force_value_lsb = 4
        self.__reg_txq5_ant_force_value_msb = 4
        self.__reg_txq5_ant_force_last_lsb = 3
        self.__reg_txq5_ant_force_last_msb = 3
        self.__reg_txrxq5_ant_force_lsb = 2
        self.__reg_txrxq5_ant_force_msb = 2
        self.__reg_txrxq5_ant_force_value_lsb = 1
        self.__reg_txrxq5_ant_force_value_msb = 1
        self.__reg_txrxq5_ant_force_last_lsb = 0
        self.__reg_txrxq5_ant_force_last_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq5_txop_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_txop_sel_msb, self.__reg_txq5_txop_sel_lsb)
    @reg_txq5_txop_sel.setter
    def reg_txq5_txop_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_txop_sel_msb, self.__reg_txq5_txop_sel_lsb, value)

    @property
    def reg_txq5_20txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_20txop_num_msb, self.__reg_txq5_20txop_num_lsb)
    @reg_txq5_20txop_num.setter
    def reg_txq5_20txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_20txop_num_msb, self.__reg_txq5_20txop_num_lsb, value)

    @property
    def reg_txq5_20eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_20eof_num_msb, self.__reg_txq5_20eof_num_lsb)
    @reg_txq5_20eof_num.setter
    def reg_txq5_20eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_20eof_num_msb, self.__reg_txq5_20eof_num_lsb, value)

    @property
    def reg_txq5_rts_rate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_rts_rate_msb, self.__reg_txq5_rts_rate_lsb)
    @reg_txq5_rts_rate.setter
    def reg_txq5_rts_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_rts_rate_msb, self.__reg_txq5_rts_rate_lsb, value)

    @property
    def reg_txq5_ant_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_ant_force_msb, self.__reg_txq5_ant_force_lsb)
    @reg_txq5_ant_force.setter
    def reg_txq5_ant_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_ant_force_msb, self.__reg_txq5_ant_force_lsb, value)

    @property
    def reg_txq5_ant_force_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_ant_force_value_msb, self.__reg_txq5_ant_force_value_lsb)
    @reg_txq5_ant_force_value.setter
    def reg_txq5_ant_force_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_ant_force_value_msb, self.__reg_txq5_ant_force_value_lsb, value)

    @property
    def reg_txq5_ant_force_last(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_ant_force_last_msb, self.__reg_txq5_ant_force_last_lsb)
    @reg_txq5_ant_force_last.setter
    def reg_txq5_ant_force_last(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_ant_force_last_msb, self.__reg_txq5_ant_force_last_lsb, value)

    @property
    def reg_txrxq5_ant_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrxq5_ant_force_msb, self.__reg_txrxq5_ant_force_lsb)
    @reg_txrxq5_ant_force.setter
    def reg_txrxq5_ant_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrxq5_ant_force_msb, self.__reg_txrxq5_ant_force_lsb, value)

    @property
    def reg_txrxq5_ant_force_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrxq5_ant_force_value_msb, self.__reg_txrxq5_ant_force_value_lsb)
    @reg_txrxq5_ant_force_value.setter
    def reg_txrxq5_ant_force_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrxq5_ant_force_value_msb, self.__reg_txrxq5_ant_force_value_lsb, value)

    @property
    def reg_txrxq5_ant_force_last(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrxq5_ant_force_last_msb, self.__reg_txrxq5_ant_force_last_lsb)
    @reg_txrxq5_ant_force_last.setter
    def reg_txrxq5_ant_force_last(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrxq5_ant_force_last_msb, self.__reg_txrxq5_ant_force_last_lsb, value)
class MACTXQ5_DUR(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x19c
        self.__reg_txq5_20dur_lsb = 16
        self.__reg_txq5_20dur_msb = 31
        self.__reg_txq5_ht40dur_lsb = 0
        self.__reg_txq5_ht40dur_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq5_20dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_20dur_msb, self.__reg_txq5_20dur_lsb)
    @reg_txq5_20dur.setter
    def reg_txq5_20dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_20dur_msb, self.__reg_txq5_20dur_lsb, value)

    @property
    def reg_txq5_ht40dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_ht40dur_msb, self.__reg_txq5_ht40dur_lsb)
    @reg_txq5_ht40dur.setter
    def reg_txq5_ht40dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_ht40dur_msb, self.__reg_txq5_ht40dur_lsb, value)
class MACTXQ5_DUR2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x1a0
        self.__reg_txq5_hwseq_fgmd_lsb = 31
        self.__reg_txq5_hwseq_fgmd_msb = 31
        self.__reg_txq5_hwseq_qmfmd_lsb = 29
        self.__reg_txq5_hwseq_qmfmd_msb = 29
        self.__reg_txq5_hwseq_sel_lsb = 17
        self.__reg_txq5_hwseq_sel_msb = 19
        self.__reg_txq5_hwseq_update_lsb = 16
        self.__reg_txq5_hwseq_update_msb = 16
        self.__reg_txq5_ht80dur_lsb = 0
        self.__reg_txq5_ht80dur_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq5_hwseq_fgmd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_hwseq_fgmd_msb, self.__reg_txq5_hwseq_fgmd_lsb)
    @reg_txq5_hwseq_fgmd.setter
    def reg_txq5_hwseq_fgmd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_hwseq_fgmd_msb, self.__reg_txq5_hwseq_fgmd_lsb, value)

    @property
    def reg_txq5_hwseq_qmfmd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_hwseq_qmfmd_msb, self.__reg_txq5_hwseq_qmfmd_lsb)
    @reg_txq5_hwseq_qmfmd.setter
    def reg_txq5_hwseq_qmfmd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_hwseq_qmfmd_msb, self.__reg_txq5_hwseq_qmfmd_lsb, value)

    @property
    def reg_txq5_hwseq_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_hwseq_sel_msb, self.__reg_txq5_hwseq_sel_lsb)
    @reg_txq5_hwseq_sel.setter
    def reg_txq5_hwseq_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_hwseq_sel_msb, self.__reg_txq5_hwseq_sel_lsb, value)

    @property
    def reg_txq5_hwseq_update(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_hwseq_update_msb, self.__reg_txq5_hwseq_update_lsb)
    @reg_txq5_hwseq_update.setter
    def reg_txq5_hwseq_update(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_hwseq_update_msb, self.__reg_txq5_hwseq_update_lsb, value)
    @property
    def default_value(self):
        return 0x0

    @property
    def reg_txq5_ht80dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq5_ht80dur_msb, self.__reg_txq5_ht80dur_lsb)
    @reg_txq5_ht80dur.setter
    def reg_txq5_ht80dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq5_ht80dur_msb, self.__reg_txq5_ht80dur_lsb, value)
class MACTXQ5PMD(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x1a4
        self.__txq5complete_num_lsb = 28
        self.__txq5complete_num_msb = 31
        self.__txq5_cbw_lsb = 25
        self.__txq5_cbw_msb = 26
        self.__txq5_rssi_lsb = 16
        self.__txq5_rssi_msb = 23
        self.__txq5complete_state_lsb = 12
        self.__txq5complete_state_msb = 15
        self.__txq5complete_st_match_lsb = 8
        self.__txq5complete_st_match_msb = 11
        self.__txq5complete_errcode_lsb = 0
        self.__txq5complete_errcode_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq5complete_num(self):
        return self.__MEM.rdm(self.__addr, self.__txq5complete_num_msb, self.__txq5complete_num_lsb)
    @txq5complete_num.setter
    def txq5complete_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq5complete_num_msb, self.__txq5complete_num_lsb, value)

    @property
    def txq5_cbw(self):
        return self.__MEM.rdm(self.__addr, self.__txq5_cbw_msb, self.__txq5_cbw_lsb)
    @txq5_cbw.setter
    def txq5_cbw(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq5_cbw_msb, self.__txq5_cbw_lsb, value)

    @property
    def txq5_rssi(self):
        return self.__MEM.rdm(self.__addr, self.__txq5_rssi_msb, self.__txq5_rssi_lsb)
    @txq5_rssi.setter
    def txq5_rssi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq5_rssi_msb, self.__txq5_rssi_lsb, value)

    @property
    def txq5complete_state(self):
        return self.__MEM.rdm(self.__addr, self.__txq5complete_state_msb, self.__txq5complete_state_lsb)
    @txq5complete_state.setter
    def txq5complete_state(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq5complete_state_msb, self.__txq5complete_state_lsb, value)

    @property
    def txq5complete_st_match(self):
        return self.__MEM.rdm(self.__addr, self.__txq5complete_st_match_msb, self.__txq5complete_st_match_lsb)
    @txq5complete_st_match.setter
    def txq5complete_st_match(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq5complete_st_match_msb, self.__txq5complete_st_match_lsb, value)

    @property
    def txq5complete_errcode(self):
        return self.__MEM.rdm(self.__addr, self.__txq5complete_errcode_msb, self.__txq5complete_errcode_lsb)
    @txq5complete_errcode.setter
    def txq5complete_errcode(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq5complete_errcode_msb, self.__txq5complete_errcode_lsb, value)
class MACTXQ5BA_BMHI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x1a8
        self.__txq5ba_bmhi_lsb = 0
        self.__txq5ba_bmhi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq5ba_bmhi(self):
        return self.__MEM.rdm(self.__addr, self.__txq5ba_bmhi_msb, self.__txq5ba_bmhi_lsb)
    @txq5ba_bmhi.setter
    def txq5ba_bmhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq5ba_bmhi_msb, self.__txq5ba_bmhi_lsb, value)
class MACTXQ5BA_BMLO(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x1ac
        self.__txq5ba_bmlo_lsb = 0
        self.__txq5ba_bmlo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq5ba_bmlo(self):
        return self.__MEM.rdm(self.__addr, self.__txq5ba_bmlo_msb, self.__txq5ba_bmlo_lsb)
    @txq5ba_bmlo.setter
    def txq5ba_bmlo(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq5ba_bmlo_msb, self.__txq5ba_bmlo_lsb, value)
class MACTXQ5BA_TAHI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x1b0
        self.__txq5ba_tahi_lsb = 0
        self.__txq5ba_tahi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq5ba_tahi(self):
        return self.__MEM.rdm(self.__addr, self.__txq5ba_tahi_msb, self.__txq5ba_tahi_lsb)
    @txq5ba_tahi.setter
    def txq5ba_tahi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq5ba_tahi_msb, self.__txq5ba_tahi_lsb, value)
class MACTXQ5BA_TALO(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x1b4
        self.__txq5ba_talo_lsb = 0
        self.__txq5ba_talo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq5ba_talo(self):
        return self.__MEM.rdm(self.__addr, self.__txq5ba_talo_msb, self.__txq5ba_talo_lsb)
    @txq5ba_talo.setter
    def txq5ba_talo(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq5ba_talo_msb, self.__txq5ba_talo_lsb, value)
class MACTXQ5BA_SSN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x1b8
        self.__txq5ba_tid_lsb = 12
        self.__txq5ba_tid_msb = 15
        self.__txq5ba_ssn_lsb = 0
        self.__txq5ba_ssn_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq5ba_tid(self):
        return self.__MEM.rdm(self.__addr, self.__txq5ba_tid_msb, self.__txq5ba_tid_lsb)
    @txq5ba_tid.setter
    def txq5ba_tid(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq5ba_tid_msb, self.__txq5ba_tid_lsb, value)

    @property
    def txq5ba_ssn(self):
        return self.__MEM.rdm(self.__addr, self.__txq5ba_ssn_msb, self.__txq5ba_ssn_lsb)
    @txq5ba_ssn.setter
    def txq5ba_ssn(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq5ba_ssn_msb, self.__txq5ba_ssn_lsb, value)
class MACTXQ5_TXSTART_US(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x1bc
        self.__txq5_txstart_us_lsb = 0
        self.__txq5_txstart_us_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq5_txstart_us(self):
        return self.__MEM.rdm(self.__addr, self.__txq5_txstart_us_msb, self.__txq5_txstart_us_lsb)
    @txq5_txstart_us.setter
    def txq5_txstart_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq5_txstart_us_msb, self.__txq5_txstart_us_lsb, value)
class MACTXQ5_TXSTART_CYC(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x1c0
        self.__txq5_txrxack_us_hi_lsb = 14
        self.__txq5_txrxack_us_hi_msb = 31
        self.__txq5_txstart_cycle_lsb = 0
        self.__txq5_txstart_cycle_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq5_txrxack_us_hi(self):
        return self.__MEM.rdm(self.__addr, self.__txq5_txrxack_us_hi_msb, self.__txq5_txrxack_us_hi_lsb)
    @txq5_txrxack_us_hi.setter
    def txq5_txrxack_us_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq5_txrxack_us_hi_msb, self.__txq5_txrxack_us_hi_lsb, value)

    @property
    def txq5_txstart_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__txq5_txstart_cycle_msb, self.__txq5_txstart_cycle_lsb)
    @txq5_txstart_cycle.setter
    def txq5_txstart_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq5_txstart_cycle_msb, self.__txq5_txstart_cycle_lsb, value)
class MACTXQ5_TXRXACK_CYC(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x1c4
        self.__txq5_txrxack_us_lsb = 18
        self.__txq5_txrxack_us_msb = 31
        self.__txq5_txrxack_cycdec_lsb = 7
        self.__txq5_txrxack_cycdec_msb = 17
        self.__txq5_txrxack_cycle_lsb = 0
        self.__txq5_txrxack_cycle_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq5_txrxack_us(self):
        return self.__MEM.rdm(self.__addr, self.__txq5_txrxack_us_msb, self.__txq5_txrxack_us_lsb)
    @txq5_txrxack_us.setter
    def txq5_txrxack_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq5_txrxack_us_msb, self.__txq5_txrxack_us_lsb, value)

    @property
    def txq5_txrxack_cycdec(self):
        return self.__MEM.rdm(self.__addr, self.__txq5_txrxack_cycdec_msb, self.__txq5_txrxack_cycdec_lsb)
    @txq5_txrxack_cycdec.setter
    def txq5_txrxack_cycdec(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq5_txrxack_cycdec_msb, self.__txq5_txrxack_cycdec_lsb, value)

    @property
    def txq5_txrxack_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__txq5_txrxack_cycle_msb, self.__txq5_txrxack_cycle_lsb)
    @txq5_txrxack_cycle.setter
    def txq5_txrxack_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq5_txrxack_cycle_msb, self.__txq5_txrxack_cycle_lsb, value)
class MACTXQ4_PLCP1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x1c8
        self.__reg_txq4_data_wbd_lsb = 31
        self.__reg_txq4_data_wbd_msb = 31
        self.__reg_txq4_rts_wbd_lsb = 30
        self.__reg_txq4_rts_wbd_msb = 30
        self.__reg_txq4_force_bw_lsb = 29
        self.__reg_txq4_force_bw_msb = 29
        self.__reg_txq4_nonhtdup_lsb = 27
        self.__reg_txq4_nonhtdup_msb = 28
        self.__reg_txq4_sigmode_lsb = 25
        self.__reg_txq4_sigmode_msb = 26
        self.__reg_txq4_kid_lsb = 17
        self.__reg_txq4_kid_msb = 24
        self.__reg_txq4_rate_lsb = 12
        self.__reg_txq4_rate_msb = 16
        self.__reg_txq4_length_lsb = 0
        self.__reg_txq4_length_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq4_data_wbd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_data_wbd_msb, self.__reg_txq4_data_wbd_lsb)
    @reg_txq4_data_wbd.setter
    def reg_txq4_data_wbd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_data_wbd_msb, self.__reg_txq4_data_wbd_lsb, value)

    @property
    def reg_txq4_rts_wbd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_rts_wbd_msb, self.__reg_txq4_rts_wbd_lsb)
    @reg_txq4_rts_wbd.setter
    def reg_txq4_rts_wbd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_rts_wbd_msb, self.__reg_txq4_rts_wbd_lsb, value)

    @property
    def reg_txq4_force_bw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_force_bw_msb, self.__reg_txq4_force_bw_lsb)
    @reg_txq4_force_bw.setter
    def reg_txq4_force_bw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_force_bw_msb, self.__reg_txq4_force_bw_lsb, value)

    @property
    def reg_txq4_nonhtdup(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_nonhtdup_msb, self.__reg_txq4_nonhtdup_lsb)
    @reg_txq4_nonhtdup.setter
    def reg_txq4_nonhtdup(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_nonhtdup_msb, self.__reg_txq4_nonhtdup_lsb, value)

    @property
    def reg_txq4_sigmode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_sigmode_msb, self.__reg_txq4_sigmode_lsb)
    @reg_txq4_sigmode.setter
    def reg_txq4_sigmode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_sigmode_msb, self.__reg_txq4_sigmode_lsb, value)

    @property
    def reg_txq4_kid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_kid_msb, self.__reg_txq4_kid_lsb)
    @reg_txq4_kid.setter
    def reg_txq4_kid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_kid_msb, self.__reg_txq4_kid_lsb, value)

    @property
    def reg_txq4_rate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_rate_msb, self.__reg_txq4_rate_lsb)
    @reg_txq4_rate.setter
    def reg_txq4_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_rate_msb, self.__reg_txq4_rate_lsb, value)

    @property
    def reg_txq4_length(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_length_msb, self.__reg_txq4_length_lsb)
    @reg_txq4_length.setter
    def reg_txq4_length(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_length_msb, self.__reg_txq4_length_lsb, value)
class MACTXQ4_PTI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x1cc
        self.__reg_txq4_pti_maintain_cnt_lsb = 20
        self.__reg_txq4_pti_maintain_cnt_msb = 31
        self.__reg_txq4_maintain_pti_lsb = 16
        self.__reg_txq4_maintain_pti_msb = 19
        self.__reg_txq4_rts_pti_lsb = 12
        self.__reg_txq4_rts_pti_msb = 15
        self.__reg_txq4_data_pti_lsb = 8
        self.__reg_txq4_data_pti_msb = 11
        self.__reg_txq4_ack_pti_lsb = 4
        self.__reg_txq4_ack_pti_msb = 7
        self.__reg_txq4_bssid_lsb = 0
        self.__reg_txq4_bssid_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq4_pti_maintain_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_pti_maintain_cnt_msb, self.__reg_txq4_pti_maintain_cnt_lsb)
    @reg_txq4_pti_maintain_cnt.setter
    def reg_txq4_pti_maintain_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_pti_maintain_cnt_msb, self.__reg_txq4_pti_maintain_cnt_lsb, value)

    @property
    def reg_txq4_maintain_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_maintain_pti_msb, self.__reg_txq4_maintain_pti_lsb)
    @reg_txq4_maintain_pti.setter
    def reg_txq4_maintain_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_maintain_pti_msb, self.__reg_txq4_maintain_pti_lsb, value)

    @property
    def reg_txq4_rts_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_rts_pti_msb, self.__reg_txq4_rts_pti_lsb)
    @reg_txq4_rts_pti.setter
    def reg_txq4_rts_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_rts_pti_msb, self.__reg_txq4_rts_pti_lsb, value)

    @property
    def reg_txq4_data_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_data_pti_msb, self.__reg_txq4_data_pti_lsb)
    @reg_txq4_data_pti.setter
    def reg_txq4_data_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_data_pti_msb, self.__reg_txq4_data_pti_lsb, value)

    @property
    def reg_txq4_ack_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_ack_pti_msb, self.__reg_txq4_ack_pti_lsb)
    @reg_txq4_ack_pti.setter
    def reg_txq4_ack_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_ack_pti_msb, self.__reg_txq4_ack_pti_lsb, value)

    @property
    def reg_txq4_bssid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_bssid_msb, self.__reg_txq4_bssid_lsb)
    @reg_txq4_bssid.setter
    def reg_txq4_bssid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_bssid_msb, self.__reg_txq4_bssid_lsb, value)
class MACTXQ4_HTSIG(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x1d0
        self.__reg_txq4_htsig_lsb = 0
        self.__reg_txq4_htsig_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq4_htsig(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_htsig_msb, self.__reg_txq4_htsig_lsb)
    @reg_txq4_htsig.setter
    def reg_txq4_htsig(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_htsig_msb, self.__reg_txq4_htsig_lsb, value)
class MACTXQ4_VHTSIG1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x1d4
        self.__reg_txq4_vhtsiga_lo_lsb = 0
        self.__reg_txq4_vhtsiga_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq4_vhtsiga_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_vhtsiga_lo_msb, self.__reg_txq4_vhtsiga_lo_lsb)
    @reg_txq4_vhtsiga_lo.setter
    def reg_txq4_vhtsiga_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_vhtsiga_lo_msb, self.__reg_txq4_vhtsiga_lo_lsb, value)
class MACTXQ4_VHTSIG2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x1d8
        self.__reg_txq4_vhtsigb_lsb = 2
        self.__reg_txq4_vhtsigb_msb = 24
        self.__reg_txq4_vhtsiga_hi_lsb = 0
        self.__reg_txq4_vhtsiga_hi_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq4_vhtsigb(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_vhtsigb_msb, self.__reg_txq4_vhtsigb_lsb)
    @reg_txq4_vhtsigb.setter
    def reg_txq4_vhtsigb(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_vhtsigb_msb, self.__reg_txq4_vhtsigb_lsb, value)

    @property
    def reg_txq4_vhtsiga_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_vhtsiga_hi_msb, self.__reg_txq4_vhtsiga_hi_lsb)
    @reg_txq4_vhtsiga_hi.setter
    def reg_txq4_vhtsiga_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_vhtsiga_hi_msb, self.__reg_txq4_vhtsiga_hi_lsb, value)
class MACTXQ4_HT80LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x1dc
        self.__reg_txq4_ht80txop_num_lsb = 24
        self.__reg_txq4_ht80txop_num_msb = 27
        self.__reg_txq4_ht80eof_num_lsb = 22
        self.__reg_txq4_ht80eof_num_msb = 23
        self.__reg_txq4_ht80len_lsb = 0
        self.__reg_txq4_ht80len_msb = 20
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq4_ht80txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_ht80txop_num_msb, self.__reg_txq4_ht80txop_num_lsb)
    @reg_txq4_ht80txop_num.setter
    def reg_txq4_ht80txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_ht80txop_num_msb, self.__reg_txq4_ht80txop_num_lsb, value)

    @property
    def reg_txq4_ht80eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_ht80eof_num_msb, self.__reg_txq4_ht80eof_num_lsb)
    @reg_txq4_ht80eof_num.setter
    def reg_txq4_ht80eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_ht80eof_num_msb, self.__reg_txq4_ht80eof_num_lsb, value)

    @property
    def reg_txq4_ht80len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_ht80len_msb, self.__reg_txq4_ht80len_lsb)
    @reg_txq4_ht80len.setter
    def reg_txq4_ht80len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_ht80len_msb, self.__reg_txq4_ht80len_lsb, value)
class MACTXQ4_HT40LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x1e0
        self.__reg_txq4_ht40txop_num_lsb = 24
        self.__reg_txq4_ht40txop_num_msb = 27
        self.__reg_txq4_ht40eof_num_lsb = 22
        self.__reg_txq4_ht40eof_num_msb = 23
        self.__reg_txq4_ht40len_lsb = 0
        self.__reg_txq4_ht40len_msb = 18
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq4_ht40txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_ht40txop_num_msb, self.__reg_txq4_ht40txop_num_lsb)
    @reg_txq4_ht40txop_num.setter
    def reg_txq4_ht40txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_ht40txop_num_msb, self.__reg_txq4_ht40txop_num_lsb, value)

    @property
    def reg_txq4_ht40eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_ht40eof_num_msb, self.__reg_txq4_ht40eof_num_lsb)
    @reg_txq4_ht40eof_num.setter
    def reg_txq4_ht40eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_ht40eof_num_msb, self.__reg_txq4_ht40eof_num_lsb, value)

    @property
    def reg_txq4_ht40len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_ht40len_msb, self.__reg_txq4_ht40len_lsb)
    @reg_txq4_ht40len.setter
    def reg_txq4_ht40len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_ht40len_msb, self.__reg_txq4_ht40len_lsb, value)
class MACTXQ4_HT20LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x1e4
        self.__reg_txq4_txop_sel_lsb = 28
        self.__reg_txq4_txop_sel_msb = 29
        self.__reg_txq4_20txop_num_lsb = 24
        self.__reg_txq4_20txop_num_msb = 27
        self.__reg_txq4_20eof_num_lsb = 22
        self.__reg_txq4_20eof_num_msb = 23
        self.__reg_txq4_rts_rate_lsb = 6
        self.__reg_txq4_rts_rate_msb = 13
        self.__reg_txq4_ant_force_lsb = 5
        self.__reg_txq4_ant_force_msb = 5
        self.__reg_txq4_ant_force_value_lsb = 4
        self.__reg_txq4_ant_force_value_msb = 4
        self.__reg_txq4_ant_force_last_lsb = 3
        self.__reg_txq4_ant_force_last_msb = 3
        self.__reg_txrxq4_ant_force_lsb = 2
        self.__reg_txrxq4_ant_force_msb = 2
        self.__reg_txrxq4_ant_force_value_lsb = 1
        self.__reg_txrxq4_ant_force_value_msb = 1
        self.__reg_txrxq4_ant_force_last_lsb = 0
        self.__reg_txrxq4_ant_force_last_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq4_txop_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_txop_sel_msb, self.__reg_txq4_txop_sel_lsb)
    @reg_txq4_txop_sel.setter
    def reg_txq4_txop_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_txop_sel_msb, self.__reg_txq4_txop_sel_lsb, value)

    @property
    def reg_txq4_20txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_20txop_num_msb, self.__reg_txq4_20txop_num_lsb)
    @reg_txq4_20txop_num.setter
    def reg_txq4_20txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_20txop_num_msb, self.__reg_txq4_20txop_num_lsb, value)

    @property
    def reg_txq4_20eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_20eof_num_msb, self.__reg_txq4_20eof_num_lsb)
    @reg_txq4_20eof_num.setter
    def reg_txq4_20eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_20eof_num_msb, self.__reg_txq4_20eof_num_lsb, value)

    @property
    def reg_txq4_rts_rate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_rts_rate_msb, self.__reg_txq4_rts_rate_lsb)
    @reg_txq4_rts_rate.setter
    def reg_txq4_rts_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_rts_rate_msb, self.__reg_txq4_rts_rate_lsb, value)

    @property
    def reg_txq4_ant_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_ant_force_msb, self.__reg_txq4_ant_force_lsb)
    @reg_txq4_ant_force.setter
    def reg_txq4_ant_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_ant_force_msb, self.__reg_txq4_ant_force_lsb, value)

    @property
    def reg_txq4_ant_force_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_ant_force_value_msb, self.__reg_txq4_ant_force_value_lsb)
    @reg_txq4_ant_force_value.setter
    def reg_txq4_ant_force_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_ant_force_value_msb, self.__reg_txq4_ant_force_value_lsb, value)

    @property
    def reg_txq4_ant_force_last(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_ant_force_last_msb, self.__reg_txq4_ant_force_last_lsb)
    @reg_txq4_ant_force_last.setter
    def reg_txq4_ant_force_last(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_ant_force_last_msb, self.__reg_txq4_ant_force_last_lsb, value)

    @property
    def reg_txrxq4_ant_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrxq4_ant_force_msb, self.__reg_txrxq4_ant_force_lsb)
    @reg_txrxq4_ant_force.setter
    def reg_txrxq4_ant_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrxq4_ant_force_msb, self.__reg_txrxq4_ant_force_lsb, value)

    @property
    def reg_txrxq4_ant_force_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrxq4_ant_force_value_msb, self.__reg_txrxq4_ant_force_value_lsb)
    @reg_txrxq4_ant_force_value.setter
    def reg_txrxq4_ant_force_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrxq4_ant_force_value_msb, self.__reg_txrxq4_ant_force_value_lsb, value)

    @property
    def reg_txrxq4_ant_force_last(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrxq4_ant_force_last_msb, self.__reg_txrxq4_ant_force_last_lsb)
    @reg_txrxq4_ant_force_last.setter
    def reg_txrxq4_ant_force_last(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrxq4_ant_force_last_msb, self.__reg_txrxq4_ant_force_last_lsb, value)
class MACTXQ4_DUR(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x1e8
        self.__reg_txq4_20dur_lsb = 16
        self.__reg_txq4_20dur_msb = 31
        self.__reg_txq4_ht40dur_lsb = 0
        self.__reg_txq4_ht40dur_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq4_20dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_20dur_msb, self.__reg_txq4_20dur_lsb)
    @reg_txq4_20dur.setter
    def reg_txq4_20dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_20dur_msb, self.__reg_txq4_20dur_lsb, value)

    @property
    def reg_txq4_ht40dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_ht40dur_msb, self.__reg_txq4_ht40dur_lsb)
    @reg_txq4_ht40dur.setter
    def reg_txq4_ht40dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_ht40dur_msb, self.__reg_txq4_ht40dur_lsb, value)
class MACTXQ4_DUR2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x1ec
        self.__reg_txq4_hwseq_fgmd_lsb = 31
        self.__reg_txq4_hwseq_fgmd_msb = 31
        self.__reg_txq4_hwseq_qmfmd_lsb = 29
        self.__reg_txq4_hwseq_qmfmd_msb = 29
        self.__reg_txq4_hwseq_sel_lsb = 17
        self.__reg_txq4_hwseq_sel_msb = 19
        self.__reg_txq4_hwseq_update_lsb = 16
        self.__reg_txq4_hwseq_update_msb = 16
        self.__reg_txq4_ht80dur_lsb = 0
        self.__reg_txq4_ht80dur_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq4_hwseq_fgmd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_hwseq_fgmd_msb, self.__reg_txq4_hwseq_fgmd_lsb)
    @reg_txq4_hwseq_fgmd.setter
    def reg_txq4_hwseq_fgmd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_hwseq_fgmd_msb, self.__reg_txq4_hwseq_fgmd_lsb, value)

    @property
    def reg_txq4_hwseq_qmfmd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_hwseq_qmfmd_msb, self.__reg_txq4_hwseq_qmfmd_lsb)
    @reg_txq4_hwseq_qmfmd.setter
    def reg_txq4_hwseq_qmfmd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_hwseq_qmfmd_msb, self.__reg_txq4_hwseq_qmfmd_lsb, value)

    @property
    def reg_txq4_hwseq_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_hwseq_sel_msb, self.__reg_txq4_hwseq_sel_lsb)
    @reg_txq4_hwseq_sel.setter
    def reg_txq4_hwseq_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_hwseq_sel_msb, self.__reg_txq4_hwseq_sel_lsb, value)

    @property
    def reg_txq4_hwseq_update(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_hwseq_update_msb, self.__reg_txq4_hwseq_update_lsb)
    @reg_txq4_hwseq_update.setter
    def reg_txq4_hwseq_update(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_hwseq_update_msb, self.__reg_txq4_hwseq_update_lsb, value)
    @property
    def default_value(self):
        return 0x0

    @property
    def reg_txq4_ht80dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq4_ht80dur_msb, self.__reg_txq4_ht80dur_lsb)
    @reg_txq4_ht80dur.setter
    def reg_txq4_ht80dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq4_ht80dur_msb, self.__reg_txq4_ht80dur_lsb, value)
class MACTXQ4PMD(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x1f0
        self.__txq4complete_num_lsb = 28
        self.__txq4complete_num_msb = 31
        self.__txq4_cbw_lsb = 25
        self.__txq4_cbw_msb = 26
        self.__txq4_rssi_lsb = 16
        self.__txq4_rssi_msb = 23
        self.__txq4complete_state_lsb = 12
        self.__txq4complete_state_msb = 15
        self.__txq4complete_st_match_lsb = 8
        self.__txq4complete_st_match_msb = 11
        self.__txq4complete_errcode_lsb = 0
        self.__txq4complete_errcode_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq4complete_num(self):
        return self.__MEM.rdm(self.__addr, self.__txq4complete_num_msb, self.__txq4complete_num_lsb)
    @txq4complete_num.setter
    def txq4complete_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq4complete_num_msb, self.__txq4complete_num_lsb, value)

    @property
    def txq4_cbw(self):
        return self.__MEM.rdm(self.__addr, self.__txq4_cbw_msb, self.__txq4_cbw_lsb)
    @txq4_cbw.setter
    def txq4_cbw(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq4_cbw_msb, self.__txq4_cbw_lsb, value)

    @property
    def txq4_rssi(self):
        return self.__MEM.rdm(self.__addr, self.__txq4_rssi_msb, self.__txq4_rssi_lsb)
    @txq4_rssi.setter
    def txq4_rssi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq4_rssi_msb, self.__txq4_rssi_lsb, value)

    @property
    def txq4complete_state(self):
        return self.__MEM.rdm(self.__addr, self.__txq4complete_state_msb, self.__txq4complete_state_lsb)
    @txq4complete_state.setter
    def txq4complete_state(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq4complete_state_msb, self.__txq4complete_state_lsb, value)

    @property
    def txq4complete_st_match(self):
        return self.__MEM.rdm(self.__addr, self.__txq4complete_st_match_msb, self.__txq4complete_st_match_lsb)
    @txq4complete_st_match.setter
    def txq4complete_st_match(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq4complete_st_match_msb, self.__txq4complete_st_match_lsb, value)

    @property
    def txq4complete_errcode(self):
        return self.__MEM.rdm(self.__addr, self.__txq4complete_errcode_msb, self.__txq4complete_errcode_lsb)
    @txq4complete_errcode.setter
    def txq4complete_errcode(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq4complete_errcode_msb, self.__txq4complete_errcode_lsb, value)
class MACTXQ4BA_BMHI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x1f4
        self.__txq4ba_bmhi_lsb = 0
        self.__txq4ba_bmhi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq4ba_bmhi(self):
        return self.__MEM.rdm(self.__addr, self.__txq4ba_bmhi_msb, self.__txq4ba_bmhi_lsb)
    @txq4ba_bmhi.setter
    def txq4ba_bmhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq4ba_bmhi_msb, self.__txq4ba_bmhi_lsb, value)
class MACTXQ4BA_BMLO(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x1f8
        self.__txq4ba_bmlo_lsb = 0
        self.__txq4ba_bmlo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq4ba_bmlo(self):
        return self.__MEM.rdm(self.__addr, self.__txq4ba_bmlo_msb, self.__txq4ba_bmlo_lsb)
    @txq4ba_bmlo.setter
    def txq4ba_bmlo(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq4ba_bmlo_msb, self.__txq4ba_bmlo_lsb, value)
class MACTXQ4BA_TAHI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x1fc
        self.__txq4ba_tahi_lsb = 0
        self.__txq4ba_tahi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq4ba_tahi(self):
        return self.__MEM.rdm(self.__addr, self.__txq4ba_tahi_msb, self.__txq4ba_tahi_lsb)
    @txq4ba_tahi.setter
    def txq4ba_tahi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq4ba_tahi_msb, self.__txq4ba_tahi_lsb, value)
class MACTXQ4BA_TALO(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x200
        self.__txq4ba_talo_lsb = 0
        self.__txq4ba_talo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq4ba_talo(self):
        return self.__MEM.rdm(self.__addr, self.__txq4ba_talo_msb, self.__txq4ba_talo_lsb)
    @txq4ba_talo.setter
    def txq4ba_talo(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq4ba_talo_msb, self.__txq4ba_talo_lsb, value)
class MACTXQ4BA_SSN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x204
        self.__txq4ba_tid_lsb = 12
        self.__txq4ba_tid_msb = 15
        self.__txq4ba_ssn_lsb = 0
        self.__txq4ba_ssn_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq4ba_tid(self):
        return self.__MEM.rdm(self.__addr, self.__txq4ba_tid_msb, self.__txq4ba_tid_lsb)
    @txq4ba_tid.setter
    def txq4ba_tid(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq4ba_tid_msb, self.__txq4ba_tid_lsb, value)

    @property
    def txq4ba_ssn(self):
        return self.__MEM.rdm(self.__addr, self.__txq4ba_ssn_msb, self.__txq4ba_ssn_lsb)
    @txq4ba_ssn.setter
    def txq4ba_ssn(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq4ba_ssn_msb, self.__txq4ba_ssn_lsb, value)
class MACTXQ4_TXSTART_US(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x208
        self.__txq4_txstart_us_lsb = 0
        self.__txq4_txstart_us_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq4_txstart_us(self):
        return self.__MEM.rdm(self.__addr, self.__txq4_txstart_us_msb, self.__txq4_txstart_us_lsb)
    @txq4_txstart_us.setter
    def txq4_txstart_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq4_txstart_us_msb, self.__txq4_txstart_us_lsb, value)
class MACTXQ4_TXSTART_CYC(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x20c
        self.__txq4_txrxack_us_hi_lsb = 14
        self.__txq4_txrxack_us_hi_msb = 31
        self.__txq4_txstart_cycle_lsb = 0
        self.__txq4_txstart_cycle_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq4_txrxack_us_hi(self):
        return self.__MEM.rdm(self.__addr, self.__txq4_txrxack_us_hi_msb, self.__txq4_txrxack_us_hi_lsb)
    @txq4_txrxack_us_hi.setter
    def txq4_txrxack_us_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq4_txrxack_us_hi_msb, self.__txq4_txrxack_us_hi_lsb, value)

    @property
    def txq4_txstart_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__txq4_txstart_cycle_msb, self.__txq4_txstart_cycle_lsb)
    @txq4_txstart_cycle.setter
    def txq4_txstart_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq4_txstart_cycle_msb, self.__txq4_txstart_cycle_lsb, value)
class MACTXQ4_TXRXACK_CYC(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x210
        self.__txq4_txrxack_us_lsb = 18
        self.__txq4_txrxack_us_msb = 31
        self.__txq4_txrxack_cycdec_lsb = 7
        self.__txq4_txrxack_cycdec_msb = 17
        self.__txq4_txrxack_cycle_lsb = 0
        self.__txq4_txrxack_cycle_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq4_txrxack_us(self):
        return self.__MEM.rdm(self.__addr, self.__txq4_txrxack_us_msb, self.__txq4_txrxack_us_lsb)
    @txq4_txrxack_us.setter
    def txq4_txrxack_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq4_txrxack_us_msb, self.__txq4_txrxack_us_lsb, value)

    @property
    def txq4_txrxack_cycdec(self):
        return self.__MEM.rdm(self.__addr, self.__txq4_txrxack_cycdec_msb, self.__txq4_txrxack_cycdec_lsb)
    @txq4_txrxack_cycdec.setter
    def txq4_txrxack_cycdec(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq4_txrxack_cycdec_msb, self.__txq4_txrxack_cycdec_lsb, value)

    @property
    def txq4_txrxack_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__txq4_txrxack_cycle_msb, self.__txq4_txrxack_cycle_lsb)
    @txq4_txrxack_cycle.setter
    def txq4_txrxack_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq4_txrxack_cycle_msb, self.__txq4_txrxack_cycle_lsb, value)
class MACTXQ3_PLCP1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x214
        self.__reg_txq3_data_wbd_lsb = 31
        self.__reg_txq3_data_wbd_msb = 31
        self.__reg_txq3_rts_wbd_lsb = 30
        self.__reg_txq3_rts_wbd_msb = 30
        self.__reg_txq3_force_bw_lsb = 29
        self.__reg_txq3_force_bw_msb = 29
        self.__reg_txq3_nonhtdup_lsb = 27
        self.__reg_txq3_nonhtdup_msb = 28
        self.__reg_txq3_sigmode_lsb = 25
        self.__reg_txq3_sigmode_msb = 26
        self.__reg_txq3_kid_lsb = 17
        self.__reg_txq3_kid_msb = 24
        self.__reg_txq3_rate_lsb = 12
        self.__reg_txq3_rate_msb = 16
        self.__reg_txq3_length_lsb = 0
        self.__reg_txq3_length_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq3_data_wbd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_data_wbd_msb, self.__reg_txq3_data_wbd_lsb)
    @reg_txq3_data_wbd.setter
    def reg_txq3_data_wbd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_data_wbd_msb, self.__reg_txq3_data_wbd_lsb, value)

    @property
    def reg_txq3_rts_wbd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_rts_wbd_msb, self.__reg_txq3_rts_wbd_lsb)
    @reg_txq3_rts_wbd.setter
    def reg_txq3_rts_wbd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_rts_wbd_msb, self.__reg_txq3_rts_wbd_lsb, value)

    @property
    def reg_txq3_force_bw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_force_bw_msb, self.__reg_txq3_force_bw_lsb)
    @reg_txq3_force_bw.setter
    def reg_txq3_force_bw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_force_bw_msb, self.__reg_txq3_force_bw_lsb, value)

    @property
    def reg_txq3_nonhtdup(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_nonhtdup_msb, self.__reg_txq3_nonhtdup_lsb)
    @reg_txq3_nonhtdup.setter
    def reg_txq3_nonhtdup(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_nonhtdup_msb, self.__reg_txq3_nonhtdup_lsb, value)

    @property
    def reg_txq3_sigmode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_sigmode_msb, self.__reg_txq3_sigmode_lsb)
    @reg_txq3_sigmode.setter
    def reg_txq3_sigmode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_sigmode_msb, self.__reg_txq3_sigmode_lsb, value)

    @property
    def reg_txq3_kid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_kid_msb, self.__reg_txq3_kid_lsb)
    @reg_txq3_kid.setter
    def reg_txq3_kid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_kid_msb, self.__reg_txq3_kid_lsb, value)

    @property
    def reg_txq3_rate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_rate_msb, self.__reg_txq3_rate_lsb)
    @reg_txq3_rate.setter
    def reg_txq3_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_rate_msb, self.__reg_txq3_rate_lsb, value)

    @property
    def reg_txq3_length(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_length_msb, self.__reg_txq3_length_lsb)
    @reg_txq3_length.setter
    def reg_txq3_length(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_length_msb, self.__reg_txq3_length_lsb, value)
class MACTXQ3_PTI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x218
        self.__reg_txq3_pti_maintain_cnt_lsb = 20
        self.__reg_txq3_pti_maintain_cnt_msb = 31
        self.__reg_txq3_maintain_pti_lsb = 16
        self.__reg_txq3_maintain_pti_msb = 19
        self.__reg_txq3_rts_pti_lsb = 12
        self.__reg_txq3_rts_pti_msb = 15
        self.__reg_txq3_data_pti_lsb = 8
        self.__reg_txq3_data_pti_msb = 11
        self.__reg_txq3_ack_pti_lsb = 4
        self.__reg_txq3_ack_pti_msb = 7
        self.__reg_txq3_bssid_lsb = 0
        self.__reg_txq3_bssid_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq3_pti_maintain_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_pti_maintain_cnt_msb, self.__reg_txq3_pti_maintain_cnt_lsb)
    @reg_txq3_pti_maintain_cnt.setter
    def reg_txq3_pti_maintain_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_pti_maintain_cnt_msb, self.__reg_txq3_pti_maintain_cnt_lsb, value)

    @property
    def reg_txq3_maintain_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_maintain_pti_msb, self.__reg_txq3_maintain_pti_lsb)
    @reg_txq3_maintain_pti.setter
    def reg_txq3_maintain_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_maintain_pti_msb, self.__reg_txq3_maintain_pti_lsb, value)

    @property
    def reg_txq3_rts_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_rts_pti_msb, self.__reg_txq3_rts_pti_lsb)
    @reg_txq3_rts_pti.setter
    def reg_txq3_rts_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_rts_pti_msb, self.__reg_txq3_rts_pti_lsb, value)

    @property
    def reg_txq3_data_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_data_pti_msb, self.__reg_txq3_data_pti_lsb)
    @reg_txq3_data_pti.setter
    def reg_txq3_data_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_data_pti_msb, self.__reg_txq3_data_pti_lsb, value)

    @property
    def reg_txq3_ack_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_ack_pti_msb, self.__reg_txq3_ack_pti_lsb)
    @reg_txq3_ack_pti.setter
    def reg_txq3_ack_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_ack_pti_msb, self.__reg_txq3_ack_pti_lsb, value)

    @property
    def reg_txq3_bssid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_bssid_msb, self.__reg_txq3_bssid_lsb)
    @reg_txq3_bssid.setter
    def reg_txq3_bssid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_bssid_msb, self.__reg_txq3_bssid_lsb, value)
class MACTXQ3_HTSIG(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x21c
        self.__reg_txq3_htsig_lsb = 0
        self.__reg_txq3_htsig_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq3_htsig(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_htsig_msb, self.__reg_txq3_htsig_lsb)
    @reg_txq3_htsig.setter
    def reg_txq3_htsig(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_htsig_msb, self.__reg_txq3_htsig_lsb, value)
class MACTXQ3_VHTSIG1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x220
        self.__reg_txq3_vhtsiga_lo_lsb = 0
        self.__reg_txq3_vhtsiga_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq3_vhtsiga_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_vhtsiga_lo_msb, self.__reg_txq3_vhtsiga_lo_lsb)
    @reg_txq3_vhtsiga_lo.setter
    def reg_txq3_vhtsiga_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_vhtsiga_lo_msb, self.__reg_txq3_vhtsiga_lo_lsb, value)
class MACTXQ3_VHTSIG2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x224
        self.__reg_txq3_vhtsigb_lsb = 2
        self.__reg_txq3_vhtsigb_msb = 24
        self.__reg_txq3_vhtsiga_hi_lsb = 0
        self.__reg_txq3_vhtsiga_hi_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq3_vhtsigb(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_vhtsigb_msb, self.__reg_txq3_vhtsigb_lsb)
    @reg_txq3_vhtsigb.setter
    def reg_txq3_vhtsigb(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_vhtsigb_msb, self.__reg_txq3_vhtsigb_lsb, value)

    @property
    def reg_txq3_vhtsiga_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_vhtsiga_hi_msb, self.__reg_txq3_vhtsiga_hi_lsb)
    @reg_txq3_vhtsiga_hi.setter
    def reg_txq3_vhtsiga_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_vhtsiga_hi_msb, self.__reg_txq3_vhtsiga_hi_lsb, value)
class MACTXQ3_HT80LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x228
        self.__reg_txq3_ht80txop_num_lsb = 24
        self.__reg_txq3_ht80txop_num_msb = 27
        self.__reg_txq3_ht80eof_num_lsb = 22
        self.__reg_txq3_ht80eof_num_msb = 23
        self.__reg_txq3_ht80len_lsb = 0
        self.__reg_txq3_ht80len_msb = 20
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq3_ht80txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_ht80txop_num_msb, self.__reg_txq3_ht80txop_num_lsb)
    @reg_txq3_ht80txop_num.setter
    def reg_txq3_ht80txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_ht80txop_num_msb, self.__reg_txq3_ht80txop_num_lsb, value)

    @property
    def reg_txq3_ht80eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_ht80eof_num_msb, self.__reg_txq3_ht80eof_num_lsb)
    @reg_txq3_ht80eof_num.setter
    def reg_txq3_ht80eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_ht80eof_num_msb, self.__reg_txq3_ht80eof_num_lsb, value)

    @property
    def reg_txq3_ht80len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_ht80len_msb, self.__reg_txq3_ht80len_lsb)
    @reg_txq3_ht80len.setter
    def reg_txq3_ht80len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_ht80len_msb, self.__reg_txq3_ht80len_lsb, value)
class MACTXQ3_HT40LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x22c
        self.__reg_txq3_ht40txop_num_lsb = 24
        self.__reg_txq3_ht40txop_num_msb = 27
        self.__reg_txq3_ht40eof_num_lsb = 22
        self.__reg_txq3_ht40eof_num_msb = 23
        self.__reg_txq3_ht40len_lsb = 0
        self.__reg_txq3_ht40len_msb = 18
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq3_ht40txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_ht40txop_num_msb, self.__reg_txq3_ht40txop_num_lsb)
    @reg_txq3_ht40txop_num.setter
    def reg_txq3_ht40txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_ht40txop_num_msb, self.__reg_txq3_ht40txop_num_lsb, value)

    @property
    def reg_txq3_ht40eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_ht40eof_num_msb, self.__reg_txq3_ht40eof_num_lsb)
    @reg_txq3_ht40eof_num.setter
    def reg_txq3_ht40eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_ht40eof_num_msb, self.__reg_txq3_ht40eof_num_lsb, value)

    @property
    def reg_txq3_ht40len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_ht40len_msb, self.__reg_txq3_ht40len_lsb)
    @reg_txq3_ht40len.setter
    def reg_txq3_ht40len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_ht40len_msb, self.__reg_txq3_ht40len_lsb, value)
class MACTXQ3_HT20LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x230
        self.__reg_txq3_txop_sel_lsb = 28
        self.__reg_txq3_txop_sel_msb = 29
        self.__reg_txq3_20txop_num_lsb = 24
        self.__reg_txq3_20txop_num_msb = 27
        self.__reg_txq3_20eof_num_lsb = 22
        self.__reg_txq3_20eof_num_msb = 23
        self.__reg_txq3_rts_rate_lsb = 6
        self.__reg_txq3_rts_rate_msb = 13
        self.__reg_txq3_ant_force_lsb = 5
        self.__reg_txq3_ant_force_msb = 5
        self.__reg_txq3_ant_force_value_lsb = 4
        self.__reg_txq3_ant_force_value_msb = 4
        self.__reg_txq3_ant_force_last_lsb = 3
        self.__reg_txq3_ant_force_last_msb = 3
        self.__reg_txrxq3_ant_force_lsb = 2
        self.__reg_txrxq3_ant_force_msb = 2
        self.__reg_txrxq3_ant_force_value_lsb = 1
        self.__reg_txrxq3_ant_force_value_msb = 1
        self.__reg_txrxq3_ant_force_last_lsb = 0
        self.__reg_txrxq3_ant_force_last_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq3_txop_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_txop_sel_msb, self.__reg_txq3_txop_sel_lsb)
    @reg_txq3_txop_sel.setter
    def reg_txq3_txop_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_txop_sel_msb, self.__reg_txq3_txop_sel_lsb, value)

    @property
    def reg_txq3_20txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_20txop_num_msb, self.__reg_txq3_20txop_num_lsb)
    @reg_txq3_20txop_num.setter
    def reg_txq3_20txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_20txop_num_msb, self.__reg_txq3_20txop_num_lsb, value)

    @property
    def reg_txq3_20eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_20eof_num_msb, self.__reg_txq3_20eof_num_lsb)
    @reg_txq3_20eof_num.setter
    def reg_txq3_20eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_20eof_num_msb, self.__reg_txq3_20eof_num_lsb, value)

    @property
    def reg_txq3_rts_rate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_rts_rate_msb, self.__reg_txq3_rts_rate_lsb)
    @reg_txq3_rts_rate.setter
    def reg_txq3_rts_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_rts_rate_msb, self.__reg_txq3_rts_rate_lsb, value)

    @property
    def reg_txq3_ant_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_ant_force_msb, self.__reg_txq3_ant_force_lsb)
    @reg_txq3_ant_force.setter
    def reg_txq3_ant_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_ant_force_msb, self.__reg_txq3_ant_force_lsb, value)

    @property
    def reg_txq3_ant_force_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_ant_force_value_msb, self.__reg_txq3_ant_force_value_lsb)
    @reg_txq3_ant_force_value.setter
    def reg_txq3_ant_force_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_ant_force_value_msb, self.__reg_txq3_ant_force_value_lsb, value)

    @property
    def reg_txq3_ant_force_last(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_ant_force_last_msb, self.__reg_txq3_ant_force_last_lsb)
    @reg_txq3_ant_force_last.setter
    def reg_txq3_ant_force_last(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_ant_force_last_msb, self.__reg_txq3_ant_force_last_lsb, value)

    @property
    def reg_txrxq3_ant_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrxq3_ant_force_msb, self.__reg_txrxq3_ant_force_lsb)
    @reg_txrxq3_ant_force.setter
    def reg_txrxq3_ant_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrxq3_ant_force_msb, self.__reg_txrxq3_ant_force_lsb, value)

    @property
    def reg_txrxq3_ant_force_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrxq3_ant_force_value_msb, self.__reg_txrxq3_ant_force_value_lsb)
    @reg_txrxq3_ant_force_value.setter
    def reg_txrxq3_ant_force_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrxq3_ant_force_value_msb, self.__reg_txrxq3_ant_force_value_lsb, value)

    @property
    def reg_txrxq3_ant_force_last(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrxq3_ant_force_last_msb, self.__reg_txrxq3_ant_force_last_lsb)
    @reg_txrxq3_ant_force_last.setter
    def reg_txrxq3_ant_force_last(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrxq3_ant_force_last_msb, self.__reg_txrxq3_ant_force_last_lsb, value)
class MACTXQ3_DUR(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x234
        self.__reg_txq3_20dur_lsb = 16
        self.__reg_txq3_20dur_msb = 31
        self.__reg_txq3_ht40dur_lsb = 0
        self.__reg_txq3_ht40dur_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq3_20dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_20dur_msb, self.__reg_txq3_20dur_lsb)
    @reg_txq3_20dur.setter
    def reg_txq3_20dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_20dur_msb, self.__reg_txq3_20dur_lsb, value)

    @property
    def reg_txq3_ht40dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_ht40dur_msb, self.__reg_txq3_ht40dur_lsb)
    @reg_txq3_ht40dur.setter
    def reg_txq3_ht40dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_ht40dur_msb, self.__reg_txq3_ht40dur_lsb, value)
class MACTXQ3_DUR2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x238
        self.__reg_txq3_hwseq_fgmd_lsb = 31
        self.__reg_txq3_hwseq_fgmd_msb = 31
        self.__reg_txq3_hwseq_qmfmd_lsb = 29
        self.__reg_txq3_hwseq_qmfmd_msb = 29
        self.__reg_txq3_hwseq_sel_lsb = 17
        self.__reg_txq3_hwseq_sel_msb = 19
        self.__reg_txq3_hwseq_update_lsb = 16
        self.__reg_txq3_hwseq_update_msb = 16
        self.__reg_txq3_ht80dur_lsb = 0
        self.__reg_txq3_ht80dur_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq3_hwseq_fgmd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_hwseq_fgmd_msb, self.__reg_txq3_hwseq_fgmd_lsb)
    @reg_txq3_hwseq_fgmd.setter
    def reg_txq3_hwseq_fgmd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_hwseq_fgmd_msb, self.__reg_txq3_hwseq_fgmd_lsb, value)

    @property
    def reg_txq3_hwseq_qmfmd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_hwseq_qmfmd_msb, self.__reg_txq3_hwseq_qmfmd_lsb)
    @reg_txq3_hwseq_qmfmd.setter
    def reg_txq3_hwseq_qmfmd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_hwseq_qmfmd_msb, self.__reg_txq3_hwseq_qmfmd_lsb, value)

    @property
    def reg_txq3_hwseq_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_hwseq_sel_msb, self.__reg_txq3_hwseq_sel_lsb)
    @reg_txq3_hwseq_sel.setter
    def reg_txq3_hwseq_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_hwseq_sel_msb, self.__reg_txq3_hwseq_sel_lsb, value)

    @property
    def reg_txq3_hwseq_update(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_hwseq_update_msb, self.__reg_txq3_hwseq_update_lsb)
    @reg_txq3_hwseq_update.setter
    def reg_txq3_hwseq_update(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_hwseq_update_msb, self.__reg_txq3_hwseq_update_lsb, value)
    @property
    def default_value(self):
        return 0x0

    @property
    def reg_txq3_ht80dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq3_ht80dur_msb, self.__reg_txq3_ht80dur_lsb)
    @reg_txq3_ht80dur.setter
    def reg_txq3_ht80dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq3_ht80dur_msb, self.__reg_txq3_ht80dur_lsb, value)
class MACTXQ3PMD(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x23c
        self.__txq3complete_num_lsb = 28
        self.__txq3complete_num_msb = 31
        self.__txq3_cbw_lsb = 25
        self.__txq3_cbw_msb = 26
        self.__txq3_rssi_lsb = 16
        self.__txq3_rssi_msb = 23
        self.__txq3complete_state_lsb = 12
        self.__txq3complete_state_msb = 15
        self.__txq3complete_st_match_lsb = 8
        self.__txq3complete_st_match_msb = 11
        self.__txq3complete_errcode_lsb = 0
        self.__txq3complete_errcode_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq3complete_num(self):
        return self.__MEM.rdm(self.__addr, self.__txq3complete_num_msb, self.__txq3complete_num_lsb)
    @txq3complete_num.setter
    def txq3complete_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq3complete_num_msb, self.__txq3complete_num_lsb, value)

    @property
    def txq3_cbw(self):
        return self.__MEM.rdm(self.__addr, self.__txq3_cbw_msb, self.__txq3_cbw_lsb)
    @txq3_cbw.setter
    def txq3_cbw(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq3_cbw_msb, self.__txq3_cbw_lsb, value)

    @property
    def txq3_rssi(self):
        return self.__MEM.rdm(self.__addr, self.__txq3_rssi_msb, self.__txq3_rssi_lsb)
    @txq3_rssi.setter
    def txq3_rssi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq3_rssi_msb, self.__txq3_rssi_lsb, value)

    @property
    def txq3complete_state(self):
        return self.__MEM.rdm(self.__addr, self.__txq3complete_state_msb, self.__txq3complete_state_lsb)
    @txq3complete_state.setter
    def txq3complete_state(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq3complete_state_msb, self.__txq3complete_state_lsb, value)

    @property
    def txq3complete_st_match(self):
        return self.__MEM.rdm(self.__addr, self.__txq3complete_st_match_msb, self.__txq3complete_st_match_lsb)
    @txq3complete_st_match.setter
    def txq3complete_st_match(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq3complete_st_match_msb, self.__txq3complete_st_match_lsb, value)

    @property
    def txq3complete_errcode(self):
        return self.__MEM.rdm(self.__addr, self.__txq3complete_errcode_msb, self.__txq3complete_errcode_lsb)
    @txq3complete_errcode.setter
    def txq3complete_errcode(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq3complete_errcode_msb, self.__txq3complete_errcode_lsb, value)
class MACTXQ3BA_BMHI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x240
        self.__txq3ba_bmhi_lsb = 0
        self.__txq3ba_bmhi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq3ba_bmhi(self):
        return self.__MEM.rdm(self.__addr, self.__txq3ba_bmhi_msb, self.__txq3ba_bmhi_lsb)
    @txq3ba_bmhi.setter
    def txq3ba_bmhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq3ba_bmhi_msb, self.__txq3ba_bmhi_lsb, value)
class MACTXQ3BA_BMLO(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x244
        self.__txq3ba_bmlo_lsb = 0
        self.__txq3ba_bmlo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq3ba_bmlo(self):
        return self.__MEM.rdm(self.__addr, self.__txq3ba_bmlo_msb, self.__txq3ba_bmlo_lsb)
    @txq3ba_bmlo.setter
    def txq3ba_bmlo(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq3ba_bmlo_msb, self.__txq3ba_bmlo_lsb, value)
class MACTXQ3BA_TAHI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x248
        self.__txq3ba_tahi_lsb = 0
        self.__txq3ba_tahi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq3ba_tahi(self):
        return self.__MEM.rdm(self.__addr, self.__txq3ba_tahi_msb, self.__txq3ba_tahi_lsb)
    @txq3ba_tahi.setter
    def txq3ba_tahi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq3ba_tahi_msb, self.__txq3ba_tahi_lsb, value)
class MACTXQ3BA_TALO(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x24c
        self.__txq3ba_talo_lsb = 0
        self.__txq3ba_talo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq3ba_talo(self):
        return self.__MEM.rdm(self.__addr, self.__txq3ba_talo_msb, self.__txq3ba_talo_lsb)
    @txq3ba_talo.setter
    def txq3ba_talo(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq3ba_talo_msb, self.__txq3ba_talo_lsb, value)
class MACTXQ3BA_SSN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x250
        self.__txq3ba_tid_lsb = 12
        self.__txq3ba_tid_msb = 15
        self.__txq3ba_ssn_lsb = 0
        self.__txq3ba_ssn_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq3ba_tid(self):
        return self.__MEM.rdm(self.__addr, self.__txq3ba_tid_msb, self.__txq3ba_tid_lsb)
    @txq3ba_tid.setter
    def txq3ba_tid(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq3ba_tid_msb, self.__txq3ba_tid_lsb, value)

    @property
    def txq3ba_ssn(self):
        return self.__MEM.rdm(self.__addr, self.__txq3ba_ssn_msb, self.__txq3ba_ssn_lsb)
    @txq3ba_ssn.setter
    def txq3ba_ssn(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq3ba_ssn_msb, self.__txq3ba_ssn_lsb, value)
class MACTXQ3_TXSTART_US(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x254
        self.__txq3_txstart_us_lsb = 0
        self.__txq3_txstart_us_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq3_txstart_us(self):
        return self.__MEM.rdm(self.__addr, self.__txq3_txstart_us_msb, self.__txq3_txstart_us_lsb)
    @txq3_txstart_us.setter
    def txq3_txstart_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq3_txstart_us_msb, self.__txq3_txstart_us_lsb, value)
class MACTXQ3_TXSTART_CYC(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x258
        self.__txq3_txrxack_us_hi_lsb = 14
        self.__txq3_txrxack_us_hi_msb = 31
        self.__txq3_txstart_cycle_lsb = 0
        self.__txq3_txstart_cycle_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq3_txrxack_us_hi(self):
        return self.__MEM.rdm(self.__addr, self.__txq3_txrxack_us_hi_msb, self.__txq3_txrxack_us_hi_lsb)
    @txq3_txrxack_us_hi.setter
    def txq3_txrxack_us_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq3_txrxack_us_hi_msb, self.__txq3_txrxack_us_hi_lsb, value)

    @property
    def txq3_txstart_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__txq3_txstart_cycle_msb, self.__txq3_txstart_cycle_lsb)
    @txq3_txstart_cycle.setter
    def txq3_txstart_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq3_txstart_cycle_msb, self.__txq3_txstart_cycle_lsb, value)
class MACTXQ3_TXRXACK_CYC(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x25c
        self.__txq3_txrxack_us_lsb = 18
        self.__txq3_txrxack_us_msb = 31
        self.__txq3_txrxack_cycdec_lsb = 7
        self.__txq3_txrxack_cycdec_msb = 17
        self.__txq3_txrxack_cycle_lsb = 0
        self.__txq3_txrxack_cycle_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq3_txrxack_us(self):
        return self.__MEM.rdm(self.__addr, self.__txq3_txrxack_us_msb, self.__txq3_txrxack_us_lsb)
    @txq3_txrxack_us.setter
    def txq3_txrxack_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq3_txrxack_us_msb, self.__txq3_txrxack_us_lsb, value)

    @property
    def txq3_txrxack_cycdec(self):
        return self.__MEM.rdm(self.__addr, self.__txq3_txrxack_cycdec_msb, self.__txq3_txrxack_cycdec_lsb)
    @txq3_txrxack_cycdec.setter
    def txq3_txrxack_cycdec(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq3_txrxack_cycdec_msb, self.__txq3_txrxack_cycdec_lsb, value)

    @property
    def txq3_txrxack_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__txq3_txrxack_cycle_msb, self.__txq3_txrxack_cycle_lsb)
    @txq3_txrxack_cycle.setter
    def txq3_txrxack_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq3_txrxack_cycle_msb, self.__txq3_txrxack_cycle_lsb, value)
class MACTXQ2_PLCP1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x260
        self.__reg_txq2_data_wbd_lsb = 31
        self.__reg_txq2_data_wbd_msb = 31
        self.__reg_txq2_rts_wbd_lsb = 30
        self.__reg_txq2_rts_wbd_msb = 30
        self.__reg_txq2_force_bw_lsb = 29
        self.__reg_txq2_force_bw_msb = 29
        self.__reg_txq2_nonhtdup_lsb = 27
        self.__reg_txq2_nonhtdup_msb = 28
        self.__reg_txq2_sigmode_lsb = 25
        self.__reg_txq2_sigmode_msb = 26
        self.__reg_txq2_kid_lsb = 17
        self.__reg_txq2_kid_msb = 24
        self.__reg_txq2_rate_lsb = 12
        self.__reg_txq2_rate_msb = 16
        self.__reg_txq2_length_lsb = 0
        self.__reg_txq2_length_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq2_data_wbd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_data_wbd_msb, self.__reg_txq2_data_wbd_lsb)
    @reg_txq2_data_wbd.setter
    def reg_txq2_data_wbd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_data_wbd_msb, self.__reg_txq2_data_wbd_lsb, value)

    @property
    def reg_txq2_rts_wbd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_rts_wbd_msb, self.__reg_txq2_rts_wbd_lsb)
    @reg_txq2_rts_wbd.setter
    def reg_txq2_rts_wbd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_rts_wbd_msb, self.__reg_txq2_rts_wbd_lsb, value)

    @property
    def reg_txq2_force_bw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_force_bw_msb, self.__reg_txq2_force_bw_lsb)
    @reg_txq2_force_bw.setter
    def reg_txq2_force_bw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_force_bw_msb, self.__reg_txq2_force_bw_lsb, value)

    @property
    def reg_txq2_nonhtdup(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_nonhtdup_msb, self.__reg_txq2_nonhtdup_lsb)
    @reg_txq2_nonhtdup.setter
    def reg_txq2_nonhtdup(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_nonhtdup_msb, self.__reg_txq2_nonhtdup_lsb, value)

    @property
    def reg_txq2_sigmode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_sigmode_msb, self.__reg_txq2_sigmode_lsb)
    @reg_txq2_sigmode.setter
    def reg_txq2_sigmode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_sigmode_msb, self.__reg_txq2_sigmode_lsb, value)

    @property
    def reg_txq2_kid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_kid_msb, self.__reg_txq2_kid_lsb)
    @reg_txq2_kid.setter
    def reg_txq2_kid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_kid_msb, self.__reg_txq2_kid_lsb, value)

    @property
    def reg_txq2_rate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_rate_msb, self.__reg_txq2_rate_lsb)
    @reg_txq2_rate.setter
    def reg_txq2_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_rate_msb, self.__reg_txq2_rate_lsb, value)

    @property
    def reg_txq2_length(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_length_msb, self.__reg_txq2_length_lsb)
    @reg_txq2_length.setter
    def reg_txq2_length(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_length_msb, self.__reg_txq2_length_lsb, value)
class MACTXQ2_PTI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x264
        self.__reg_txq2_pti_maintain_cnt_lsb = 20
        self.__reg_txq2_pti_maintain_cnt_msb = 31
        self.__reg_txq2_maintain_pti_lsb = 16
        self.__reg_txq2_maintain_pti_msb = 19
        self.__reg_txq2_rts_pti_lsb = 12
        self.__reg_txq2_rts_pti_msb = 15
        self.__reg_txq2_data_pti_lsb = 8
        self.__reg_txq2_data_pti_msb = 11
        self.__reg_txq2_ack_pti_lsb = 4
        self.__reg_txq2_ack_pti_msb = 7
        self.__reg_txq2_bssid_lsb = 0
        self.__reg_txq2_bssid_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq2_pti_maintain_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_pti_maintain_cnt_msb, self.__reg_txq2_pti_maintain_cnt_lsb)
    @reg_txq2_pti_maintain_cnt.setter
    def reg_txq2_pti_maintain_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_pti_maintain_cnt_msb, self.__reg_txq2_pti_maintain_cnt_lsb, value)

    @property
    def reg_txq2_maintain_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_maintain_pti_msb, self.__reg_txq2_maintain_pti_lsb)
    @reg_txq2_maintain_pti.setter
    def reg_txq2_maintain_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_maintain_pti_msb, self.__reg_txq2_maintain_pti_lsb, value)

    @property
    def reg_txq2_rts_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_rts_pti_msb, self.__reg_txq2_rts_pti_lsb)
    @reg_txq2_rts_pti.setter
    def reg_txq2_rts_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_rts_pti_msb, self.__reg_txq2_rts_pti_lsb, value)

    @property
    def reg_txq2_data_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_data_pti_msb, self.__reg_txq2_data_pti_lsb)
    @reg_txq2_data_pti.setter
    def reg_txq2_data_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_data_pti_msb, self.__reg_txq2_data_pti_lsb, value)

    @property
    def reg_txq2_ack_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_ack_pti_msb, self.__reg_txq2_ack_pti_lsb)
    @reg_txq2_ack_pti.setter
    def reg_txq2_ack_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_ack_pti_msb, self.__reg_txq2_ack_pti_lsb, value)

    @property
    def reg_txq2_bssid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_bssid_msb, self.__reg_txq2_bssid_lsb)
    @reg_txq2_bssid.setter
    def reg_txq2_bssid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_bssid_msb, self.__reg_txq2_bssid_lsb, value)
class MACTXQ2_HTSIG(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x268
        self.__reg_txq2_htsig_lsb = 0
        self.__reg_txq2_htsig_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq2_htsig(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_htsig_msb, self.__reg_txq2_htsig_lsb)
    @reg_txq2_htsig.setter
    def reg_txq2_htsig(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_htsig_msb, self.__reg_txq2_htsig_lsb, value)
class MACTXQ2_VHTSIG1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x26c
        self.__reg_txq2_vhtsiga_lo_lsb = 0
        self.__reg_txq2_vhtsiga_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq2_vhtsiga_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_vhtsiga_lo_msb, self.__reg_txq2_vhtsiga_lo_lsb)
    @reg_txq2_vhtsiga_lo.setter
    def reg_txq2_vhtsiga_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_vhtsiga_lo_msb, self.__reg_txq2_vhtsiga_lo_lsb, value)
class MACTXQ2_VHTSIG2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x270
        self.__reg_txq2_vhtsigb_lsb = 2
        self.__reg_txq2_vhtsigb_msb = 24
        self.__reg_txq2_vhtsiga_hi_lsb = 0
        self.__reg_txq2_vhtsiga_hi_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq2_vhtsigb(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_vhtsigb_msb, self.__reg_txq2_vhtsigb_lsb)
    @reg_txq2_vhtsigb.setter
    def reg_txq2_vhtsigb(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_vhtsigb_msb, self.__reg_txq2_vhtsigb_lsb, value)

    @property
    def reg_txq2_vhtsiga_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_vhtsiga_hi_msb, self.__reg_txq2_vhtsiga_hi_lsb)
    @reg_txq2_vhtsiga_hi.setter
    def reg_txq2_vhtsiga_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_vhtsiga_hi_msb, self.__reg_txq2_vhtsiga_hi_lsb, value)
class MACTXQ2_HT80LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x274
        self.__reg_txq2_ht80txop_num_lsb = 24
        self.__reg_txq2_ht80txop_num_msb = 27
        self.__reg_txq2_ht80eof_num_lsb = 22
        self.__reg_txq2_ht80eof_num_msb = 23
        self.__reg_txq2_ht80len_lsb = 0
        self.__reg_txq2_ht80len_msb = 20
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq2_ht80txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_ht80txop_num_msb, self.__reg_txq2_ht80txop_num_lsb)
    @reg_txq2_ht80txop_num.setter
    def reg_txq2_ht80txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_ht80txop_num_msb, self.__reg_txq2_ht80txop_num_lsb, value)

    @property
    def reg_txq2_ht80eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_ht80eof_num_msb, self.__reg_txq2_ht80eof_num_lsb)
    @reg_txq2_ht80eof_num.setter
    def reg_txq2_ht80eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_ht80eof_num_msb, self.__reg_txq2_ht80eof_num_lsb, value)

    @property
    def reg_txq2_ht80len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_ht80len_msb, self.__reg_txq2_ht80len_lsb)
    @reg_txq2_ht80len.setter
    def reg_txq2_ht80len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_ht80len_msb, self.__reg_txq2_ht80len_lsb, value)
class MACTXQ2_HT40LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x278
        self.__reg_txq2_ht40txop_num_lsb = 24
        self.__reg_txq2_ht40txop_num_msb = 27
        self.__reg_txq2_ht40eof_num_lsb = 22
        self.__reg_txq2_ht40eof_num_msb = 23
        self.__reg_txq2_ht40len_lsb = 0
        self.__reg_txq2_ht40len_msb = 18
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq2_ht40txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_ht40txop_num_msb, self.__reg_txq2_ht40txop_num_lsb)
    @reg_txq2_ht40txop_num.setter
    def reg_txq2_ht40txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_ht40txop_num_msb, self.__reg_txq2_ht40txop_num_lsb, value)

    @property
    def reg_txq2_ht40eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_ht40eof_num_msb, self.__reg_txq2_ht40eof_num_lsb)
    @reg_txq2_ht40eof_num.setter
    def reg_txq2_ht40eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_ht40eof_num_msb, self.__reg_txq2_ht40eof_num_lsb, value)

    @property
    def reg_txq2_ht40len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_ht40len_msb, self.__reg_txq2_ht40len_lsb)
    @reg_txq2_ht40len.setter
    def reg_txq2_ht40len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_ht40len_msb, self.__reg_txq2_ht40len_lsb, value)
class MACTXQ2_HT20LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x27c
        self.__reg_txq2_txop_sel_lsb = 28
        self.__reg_txq2_txop_sel_msb = 29
        self.__reg_txq2_20txop_num_lsb = 24
        self.__reg_txq2_20txop_num_msb = 27
        self.__reg_txq2_20eof_num_lsb = 22
        self.__reg_txq2_20eof_num_msb = 23
        self.__reg_txq2_rts_rate_lsb = 6
        self.__reg_txq2_rts_rate_msb = 13
        self.__reg_txq2_ant_force_lsb = 5
        self.__reg_txq2_ant_force_msb = 5
        self.__reg_txq2_ant_force_value_lsb = 4
        self.__reg_txq2_ant_force_value_msb = 4
        self.__reg_txq2_ant_force_last_lsb = 3
        self.__reg_txq2_ant_force_last_msb = 3
        self.__reg_txrxq2_ant_force_lsb = 2
        self.__reg_txrxq2_ant_force_msb = 2
        self.__reg_txrxq2_ant_force_value_lsb = 1
        self.__reg_txrxq2_ant_force_value_msb = 1
        self.__reg_txrxq2_ant_force_last_lsb = 0
        self.__reg_txrxq2_ant_force_last_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq2_txop_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_txop_sel_msb, self.__reg_txq2_txop_sel_lsb)
    @reg_txq2_txop_sel.setter
    def reg_txq2_txop_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_txop_sel_msb, self.__reg_txq2_txop_sel_lsb, value)

    @property
    def reg_txq2_20txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_20txop_num_msb, self.__reg_txq2_20txop_num_lsb)
    @reg_txq2_20txop_num.setter
    def reg_txq2_20txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_20txop_num_msb, self.__reg_txq2_20txop_num_lsb, value)

    @property
    def reg_txq2_20eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_20eof_num_msb, self.__reg_txq2_20eof_num_lsb)
    @reg_txq2_20eof_num.setter
    def reg_txq2_20eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_20eof_num_msb, self.__reg_txq2_20eof_num_lsb, value)

    @property
    def reg_txq2_rts_rate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_rts_rate_msb, self.__reg_txq2_rts_rate_lsb)
    @reg_txq2_rts_rate.setter
    def reg_txq2_rts_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_rts_rate_msb, self.__reg_txq2_rts_rate_lsb, value)

    @property
    def reg_txq2_ant_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_ant_force_msb, self.__reg_txq2_ant_force_lsb)
    @reg_txq2_ant_force.setter
    def reg_txq2_ant_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_ant_force_msb, self.__reg_txq2_ant_force_lsb, value)

    @property
    def reg_txq2_ant_force_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_ant_force_value_msb, self.__reg_txq2_ant_force_value_lsb)
    @reg_txq2_ant_force_value.setter
    def reg_txq2_ant_force_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_ant_force_value_msb, self.__reg_txq2_ant_force_value_lsb, value)

    @property
    def reg_txq2_ant_force_last(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_ant_force_last_msb, self.__reg_txq2_ant_force_last_lsb)
    @reg_txq2_ant_force_last.setter
    def reg_txq2_ant_force_last(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_ant_force_last_msb, self.__reg_txq2_ant_force_last_lsb, value)

    @property
    def reg_txrxq2_ant_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrxq2_ant_force_msb, self.__reg_txrxq2_ant_force_lsb)
    @reg_txrxq2_ant_force.setter
    def reg_txrxq2_ant_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrxq2_ant_force_msb, self.__reg_txrxq2_ant_force_lsb, value)

    @property
    def reg_txrxq2_ant_force_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrxq2_ant_force_value_msb, self.__reg_txrxq2_ant_force_value_lsb)
    @reg_txrxq2_ant_force_value.setter
    def reg_txrxq2_ant_force_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrxq2_ant_force_value_msb, self.__reg_txrxq2_ant_force_value_lsb, value)

    @property
    def reg_txrxq2_ant_force_last(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrxq2_ant_force_last_msb, self.__reg_txrxq2_ant_force_last_lsb)
    @reg_txrxq2_ant_force_last.setter
    def reg_txrxq2_ant_force_last(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrxq2_ant_force_last_msb, self.__reg_txrxq2_ant_force_last_lsb, value)
class MACTXQ2_DUR(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x280
        self.__reg_txq2_20dur_lsb = 16
        self.__reg_txq2_20dur_msb = 31
        self.__reg_txq2_ht40dur_lsb = 0
        self.__reg_txq2_ht40dur_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq2_20dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_20dur_msb, self.__reg_txq2_20dur_lsb)
    @reg_txq2_20dur.setter
    def reg_txq2_20dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_20dur_msb, self.__reg_txq2_20dur_lsb, value)

    @property
    def reg_txq2_ht40dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_ht40dur_msb, self.__reg_txq2_ht40dur_lsb)
    @reg_txq2_ht40dur.setter
    def reg_txq2_ht40dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_ht40dur_msb, self.__reg_txq2_ht40dur_lsb, value)
class MACTXQ2_DUR2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x284
        self.__reg_txq2_hwseq_fgmd_lsb = 31
        self.__reg_txq2_hwseq_fgmd_msb = 31
        self.__reg_txq2_hwseq_qmfmd_lsb = 29
        self.__reg_txq2_hwseq_qmfmd_msb = 29
        self.__reg_txq2_hwseq_sel_lsb = 17
        self.__reg_txq2_hwseq_sel_msb = 19
        self.__reg_txq2_hwseq_update_lsb = 16
        self.__reg_txq2_hwseq_update_msb = 16
        self.__reg_txq2_ht80dur_lsb = 0
        self.__reg_txq2_ht80dur_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq2_hwseq_fgmd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_hwseq_fgmd_msb, self.__reg_txq2_hwseq_fgmd_lsb)
    @reg_txq2_hwseq_fgmd.setter
    def reg_txq2_hwseq_fgmd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_hwseq_fgmd_msb, self.__reg_txq2_hwseq_fgmd_lsb, value)

    @property
    def reg_txq2_hwseq_qmfmd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_hwseq_qmfmd_msb, self.__reg_txq2_hwseq_qmfmd_lsb)
    @reg_txq2_hwseq_qmfmd.setter
    def reg_txq2_hwseq_qmfmd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_hwseq_qmfmd_msb, self.__reg_txq2_hwseq_qmfmd_lsb, value)

    @property
    def reg_txq2_hwseq_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_hwseq_sel_msb, self.__reg_txq2_hwseq_sel_lsb)
    @reg_txq2_hwseq_sel.setter
    def reg_txq2_hwseq_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_hwseq_sel_msb, self.__reg_txq2_hwseq_sel_lsb, value)

    @property
    def reg_txq2_hwseq_update(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_hwseq_update_msb, self.__reg_txq2_hwseq_update_lsb)
    @reg_txq2_hwseq_update.setter
    def reg_txq2_hwseq_update(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_hwseq_update_msb, self.__reg_txq2_hwseq_update_lsb, value)
    @property
    def default_value(self):
        return 0x0

    @property
    def reg_txq2_ht80dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq2_ht80dur_msb, self.__reg_txq2_ht80dur_lsb)
    @reg_txq2_ht80dur.setter
    def reg_txq2_ht80dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq2_ht80dur_msb, self.__reg_txq2_ht80dur_lsb, value)
class MACTXQ2PMD(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x288
        self.__txq2complete_num_lsb = 28
        self.__txq2complete_num_msb = 31
        self.__txq2_cbw_lsb = 25
        self.__txq2_cbw_msb = 26
        self.__txq2_rssi_lsb = 16
        self.__txq2_rssi_msb = 23
        self.__txq2complete_state_lsb = 12
        self.__txq2complete_state_msb = 15
        self.__txq2complete_st_match_lsb = 8
        self.__txq2complete_st_match_msb = 11
        self.__txq2complete_errcode_lsb = 0
        self.__txq2complete_errcode_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq2complete_num(self):
        return self.__MEM.rdm(self.__addr, self.__txq2complete_num_msb, self.__txq2complete_num_lsb)
    @txq2complete_num.setter
    def txq2complete_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq2complete_num_msb, self.__txq2complete_num_lsb, value)

    @property
    def txq2_cbw(self):
        return self.__MEM.rdm(self.__addr, self.__txq2_cbw_msb, self.__txq2_cbw_lsb)
    @txq2_cbw.setter
    def txq2_cbw(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq2_cbw_msb, self.__txq2_cbw_lsb, value)

    @property
    def txq2_rssi(self):
        return self.__MEM.rdm(self.__addr, self.__txq2_rssi_msb, self.__txq2_rssi_lsb)
    @txq2_rssi.setter
    def txq2_rssi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq2_rssi_msb, self.__txq2_rssi_lsb, value)

    @property
    def txq2complete_state(self):
        return self.__MEM.rdm(self.__addr, self.__txq2complete_state_msb, self.__txq2complete_state_lsb)
    @txq2complete_state.setter
    def txq2complete_state(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq2complete_state_msb, self.__txq2complete_state_lsb, value)

    @property
    def txq2complete_st_match(self):
        return self.__MEM.rdm(self.__addr, self.__txq2complete_st_match_msb, self.__txq2complete_st_match_lsb)
    @txq2complete_st_match.setter
    def txq2complete_st_match(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq2complete_st_match_msb, self.__txq2complete_st_match_lsb, value)

    @property
    def txq2complete_errcode(self):
        return self.__MEM.rdm(self.__addr, self.__txq2complete_errcode_msb, self.__txq2complete_errcode_lsb)
    @txq2complete_errcode.setter
    def txq2complete_errcode(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq2complete_errcode_msb, self.__txq2complete_errcode_lsb, value)
class MACTXQ2BA_BMHI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x28c
        self.__txq2ba_bmhi_lsb = 0
        self.__txq2ba_bmhi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq2ba_bmhi(self):
        return self.__MEM.rdm(self.__addr, self.__txq2ba_bmhi_msb, self.__txq2ba_bmhi_lsb)
    @txq2ba_bmhi.setter
    def txq2ba_bmhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq2ba_bmhi_msb, self.__txq2ba_bmhi_lsb, value)
class MACTXQ2BA_BMLO(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x290
        self.__txq2ba_bmlo_lsb = 0
        self.__txq2ba_bmlo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq2ba_bmlo(self):
        return self.__MEM.rdm(self.__addr, self.__txq2ba_bmlo_msb, self.__txq2ba_bmlo_lsb)
    @txq2ba_bmlo.setter
    def txq2ba_bmlo(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq2ba_bmlo_msb, self.__txq2ba_bmlo_lsb, value)
class MACTXQ2BA_TAHI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x294
        self.__txq2ba_tahi_lsb = 0
        self.__txq2ba_tahi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq2ba_tahi(self):
        return self.__MEM.rdm(self.__addr, self.__txq2ba_tahi_msb, self.__txq2ba_tahi_lsb)
    @txq2ba_tahi.setter
    def txq2ba_tahi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq2ba_tahi_msb, self.__txq2ba_tahi_lsb, value)
class MACTXQ2BA_TALO(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x298
        self.__txq2ba_talo_lsb = 0
        self.__txq2ba_talo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq2ba_talo(self):
        return self.__MEM.rdm(self.__addr, self.__txq2ba_talo_msb, self.__txq2ba_talo_lsb)
    @txq2ba_talo.setter
    def txq2ba_talo(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq2ba_talo_msb, self.__txq2ba_talo_lsb, value)
class MACTXQ2BA_SSN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x29c
        self.__txq2ba_tid_lsb = 12
        self.__txq2ba_tid_msb = 15
        self.__txq2ba_ssn_lsb = 0
        self.__txq2ba_ssn_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq2ba_tid(self):
        return self.__MEM.rdm(self.__addr, self.__txq2ba_tid_msb, self.__txq2ba_tid_lsb)
    @txq2ba_tid.setter
    def txq2ba_tid(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq2ba_tid_msb, self.__txq2ba_tid_lsb, value)

    @property
    def txq2ba_ssn(self):
        return self.__MEM.rdm(self.__addr, self.__txq2ba_ssn_msb, self.__txq2ba_ssn_lsb)
    @txq2ba_ssn.setter
    def txq2ba_ssn(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq2ba_ssn_msb, self.__txq2ba_ssn_lsb, value)
class MACTXQ2_TXSTART_US(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x2a0
        self.__txq2_txstart_us_lsb = 0
        self.__txq2_txstart_us_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq2_txstart_us(self):
        return self.__MEM.rdm(self.__addr, self.__txq2_txstart_us_msb, self.__txq2_txstart_us_lsb)
    @txq2_txstart_us.setter
    def txq2_txstart_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq2_txstart_us_msb, self.__txq2_txstart_us_lsb, value)
class MACTXQ2_TXSTART_CYC(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x2a4
        self.__txq2_txrxack_us_hi_lsb = 14
        self.__txq2_txrxack_us_hi_msb = 31
        self.__txq2_txstart_cycle_lsb = 0
        self.__txq2_txstart_cycle_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq2_txrxack_us_hi(self):
        return self.__MEM.rdm(self.__addr, self.__txq2_txrxack_us_hi_msb, self.__txq2_txrxack_us_hi_lsb)
    @txq2_txrxack_us_hi.setter
    def txq2_txrxack_us_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq2_txrxack_us_hi_msb, self.__txq2_txrxack_us_hi_lsb, value)

    @property
    def txq2_txstart_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__txq2_txstart_cycle_msb, self.__txq2_txstart_cycle_lsb)
    @txq2_txstart_cycle.setter
    def txq2_txstart_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq2_txstart_cycle_msb, self.__txq2_txstart_cycle_lsb, value)
class MACTXQ2_TXRXACK_CYC(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x2a8
        self.__txq2_txrxack_us_lsb = 18
        self.__txq2_txrxack_us_msb = 31
        self.__txq2_txrxack_cycdec_lsb = 7
        self.__txq2_txrxack_cycdec_msb = 17
        self.__txq2_txrxack_cycle_lsb = 0
        self.__txq2_txrxack_cycle_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq2_txrxack_us(self):
        return self.__MEM.rdm(self.__addr, self.__txq2_txrxack_us_msb, self.__txq2_txrxack_us_lsb)
    @txq2_txrxack_us.setter
    def txq2_txrxack_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq2_txrxack_us_msb, self.__txq2_txrxack_us_lsb, value)

    @property
    def txq2_txrxack_cycdec(self):
        return self.__MEM.rdm(self.__addr, self.__txq2_txrxack_cycdec_msb, self.__txq2_txrxack_cycdec_lsb)
    @txq2_txrxack_cycdec.setter
    def txq2_txrxack_cycdec(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq2_txrxack_cycdec_msb, self.__txq2_txrxack_cycdec_lsb, value)

    @property
    def txq2_txrxack_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__txq2_txrxack_cycle_msb, self.__txq2_txrxack_cycle_lsb)
    @txq2_txrxack_cycle.setter
    def txq2_txrxack_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq2_txrxack_cycle_msb, self.__txq2_txrxack_cycle_lsb, value)
class MACTXQ1_PLCP1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x2ac
        self.__reg_txq1_data_wbd_lsb = 31
        self.__reg_txq1_data_wbd_msb = 31
        self.__reg_txq1_rts_wbd_lsb = 30
        self.__reg_txq1_rts_wbd_msb = 30
        self.__reg_txq1_force_bw_lsb = 29
        self.__reg_txq1_force_bw_msb = 29
        self.__reg_txq1_nonhtdup_lsb = 27
        self.__reg_txq1_nonhtdup_msb = 28
        self.__reg_txq1_sigmode_lsb = 25
        self.__reg_txq1_sigmode_msb = 26
        self.__reg_txq1_kid_lsb = 17
        self.__reg_txq1_kid_msb = 24
        self.__reg_txq1_rate_lsb = 12
        self.__reg_txq1_rate_msb = 16
        self.__reg_txq1_length_lsb = 0
        self.__reg_txq1_length_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq1_data_wbd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_data_wbd_msb, self.__reg_txq1_data_wbd_lsb)
    @reg_txq1_data_wbd.setter
    def reg_txq1_data_wbd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_data_wbd_msb, self.__reg_txq1_data_wbd_lsb, value)

    @property
    def reg_txq1_rts_wbd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_rts_wbd_msb, self.__reg_txq1_rts_wbd_lsb)
    @reg_txq1_rts_wbd.setter
    def reg_txq1_rts_wbd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_rts_wbd_msb, self.__reg_txq1_rts_wbd_lsb, value)

    @property
    def reg_txq1_force_bw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_force_bw_msb, self.__reg_txq1_force_bw_lsb)
    @reg_txq1_force_bw.setter
    def reg_txq1_force_bw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_force_bw_msb, self.__reg_txq1_force_bw_lsb, value)

    @property
    def reg_txq1_nonhtdup(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_nonhtdup_msb, self.__reg_txq1_nonhtdup_lsb)
    @reg_txq1_nonhtdup.setter
    def reg_txq1_nonhtdup(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_nonhtdup_msb, self.__reg_txq1_nonhtdup_lsb, value)

    @property
    def reg_txq1_sigmode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_sigmode_msb, self.__reg_txq1_sigmode_lsb)
    @reg_txq1_sigmode.setter
    def reg_txq1_sigmode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_sigmode_msb, self.__reg_txq1_sigmode_lsb, value)

    @property
    def reg_txq1_kid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_kid_msb, self.__reg_txq1_kid_lsb)
    @reg_txq1_kid.setter
    def reg_txq1_kid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_kid_msb, self.__reg_txq1_kid_lsb, value)

    @property
    def reg_txq1_rate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_rate_msb, self.__reg_txq1_rate_lsb)
    @reg_txq1_rate.setter
    def reg_txq1_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_rate_msb, self.__reg_txq1_rate_lsb, value)

    @property
    def reg_txq1_length(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_length_msb, self.__reg_txq1_length_lsb)
    @reg_txq1_length.setter
    def reg_txq1_length(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_length_msb, self.__reg_txq1_length_lsb, value)
class MACTXQ1_PTI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x2b0
        self.__reg_txq1_pti_maintain_cnt_lsb = 20
        self.__reg_txq1_pti_maintain_cnt_msb = 31
        self.__reg_txq1_maintain_pti_lsb = 16
        self.__reg_txq1_maintain_pti_msb = 19
        self.__reg_txq1_rts_pti_lsb = 12
        self.__reg_txq1_rts_pti_msb = 15
        self.__reg_txq1_data_pti_lsb = 8
        self.__reg_txq1_data_pti_msb = 11
        self.__reg_txq1_ack_pti_lsb = 4
        self.__reg_txq1_ack_pti_msb = 7
        self.__reg_txq1_bssid_lsb = 0
        self.__reg_txq1_bssid_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq1_pti_maintain_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_pti_maintain_cnt_msb, self.__reg_txq1_pti_maintain_cnt_lsb)
    @reg_txq1_pti_maintain_cnt.setter
    def reg_txq1_pti_maintain_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_pti_maintain_cnt_msb, self.__reg_txq1_pti_maintain_cnt_lsb, value)

    @property
    def reg_txq1_maintain_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_maintain_pti_msb, self.__reg_txq1_maintain_pti_lsb)
    @reg_txq1_maintain_pti.setter
    def reg_txq1_maintain_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_maintain_pti_msb, self.__reg_txq1_maintain_pti_lsb, value)

    @property
    def reg_txq1_rts_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_rts_pti_msb, self.__reg_txq1_rts_pti_lsb)
    @reg_txq1_rts_pti.setter
    def reg_txq1_rts_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_rts_pti_msb, self.__reg_txq1_rts_pti_lsb, value)

    @property
    def reg_txq1_data_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_data_pti_msb, self.__reg_txq1_data_pti_lsb)
    @reg_txq1_data_pti.setter
    def reg_txq1_data_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_data_pti_msb, self.__reg_txq1_data_pti_lsb, value)

    @property
    def reg_txq1_ack_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_ack_pti_msb, self.__reg_txq1_ack_pti_lsb)
    @reg_txq1_ack_pti.setter
    def reg_txq1_ack_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_ack_pti_msb, self.__reg_txq1_ack_pti_lsb, value)

    @property
    def reg_txq1_bssid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_bssid_msb, self.__reg_txq1_bssid_lsb)
    @reg_txq1_bssid.setter
    def reg_txq1_bssid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_bssid_msb, self.__reg_txq1_bssid_lsb, value)
class MACTXQ1_HTSIG(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x2b4
        self.__reg_txq1_htsig_lsb = 0
        self.__reg_txq1_htsig_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq1_htsig(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_htsig_msb, self.__reg_txq1_htsig_lsb)
    @reg_txq1_htsig.setter
    def reg_txq1_htsig(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_htsig_msb, self.__reg_txq1_htsig_lsb, value)
class MACTXQ1_VHTSIG1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x2b8
        self.__reg_txq1_vhtsiga_lo_lsb = 0
        self.__reg_txq1_vhtsiga_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq1_vhtsiga_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_vhtsiga_lo_msb, self.__reg_txq1_vhtsiga_lo_lsb)
    @reg_txq1_vhtsiga_lo.setter
    def reg_txq1_vhtsiga_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_vhtsiga_lo_msb, self.__reg_txq1_vhtsiga_lo_lsb, value)
class MACTXQ1_VHTSIG2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x2bc
        self.__reg_txq1_vhtsigb_lsb = 2
        self.__reg_txq1_vhtsigb_msb = 24
        self.__reg_txq1_vhtsiga_hi_lsb = 0
        self.__reg_txq1_vhtsiga_hi_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq1_vhtsigb(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_vhtsigb_msb, self.__reg_txq1_vhtsigb_lsb)
    @reg_txq1_vhtsigb.setter
    def reg_txq1_vhtsigb(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_vhtsigb_msb, self.__reg_txq1_vhtsigb_lsb, value)

    @property
    def reg_txq1_vhtsiga_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_vhtsiga_hi_msb, self.__reg_txq1_vhtsiga_hi_lsb)
    @reg_txq1_vhtsiga_hi.setter
    def reg_txq1_vhtsiga_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_vhtsiga_hi_msb, self.__reg_txq1_vhtsiga_hi_lsb, value)
class MACTXQ1_HT80LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x2c0
        self.__reg_txq1_ht80txop_num_lsb = 24
        self.__reg_txq1_ht80txop_num_msb = 27
        self.__reg_txq1_ht80eof_num_lsb = 22
        self.__reg_txq1_ht80eof_num_msb = 23
        self.__reg_txq1_ht80len_lsb = 0
        self.__reg_txq1_ht80len_msb = 20
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq1_ht80txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_ht80txop_num_msb, self.__reg_txq1_ht80txop_num_lsb)
    @reg_txq1_ht80txop_num.setter
    def reg_txq1_ht80txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_ht80txop_num_msb, self.__reg_txq1_ht80txop_num_lsb, value)

    @property
    def reg_txq1_ht80eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_ht80eof_num_msb, self.__reg_txq1_ht80eof_num_lsb)
    @reg_txq1_ht80eof_num.setter
    def reg_txq1_ht80eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_ht80eof_num_msb, self.__reg_txq1_ht80eof_num_lsb, value)

    @property
    def reg_txq1_ht80len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_ht80len_msb, self.__reg_txq1_ht80len_lsb)
    @reg_txq1_ht80len.setter
    def reg_txq1_ht80len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_ht80len_msb, self.__reg_txq1_ht80len_lsb, value)
class MACTXQ1_HT40LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x2c4
        self.__reg_txq1_ht40txop_num_lsb = 24
        self.__reg_txq1_ht40txop_num_msb = 27
        self.__reg_txq1_ht40eof_num_lsb = 22
        self.__reg_txq1_ht40eof_num_msb = 23
        self.__reg_txq1_ht40len_lsb = 0
        self.__reg_txq1_ht40len_msb = 18
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq1_ht40txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_ht40txop_num_msb, self.__reg_txq1_ht40txop_num_lsb)
    @reg_txq1_ht40txop_num.setter
    def reg_txq1_ht40txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_ht40txop_num_msb, self.__reg_txq1_ht40txop_num_lsb, value)

    @property
    def reg_txq1_ht40eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_ht40eof_num_msb, self.__reg_txq1_ht40eof_num_lsb)
    @reg_txq1_ht40eof_num.setter
    def reg_txq1_ht40eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_ht40eof_num_msb, self.__reg_txq1_ht40eof_num_lsb, value)

    @property
    def reg_txq1_ht40len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_ht40len_msb, self.__reg_txq1_ht40len_lsb)
    @reg_txq1_ht40len.setter
    def reg_txq1_ht40len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_ht40len_msb, self.__reg_txq1_ht40len_lsb, value)
class MACTXQ1_HT20LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x2c8
        self.__reg_txq1_txop_sel_lsb = 28
        self.__reg_txq1_txop_sel_msb = 29
        self.__reg_txq1_20txop_num_lsb = 24
        self.__reg_txq1_20txop_num_msb = 27
        self.__reg_txq1_20eof_num_lsb = 22
        self.__reg_txq1_20eof_num_msb = 23
        self.__reg_txq1_rts_rate_lsb = 6
        self.__reg_txq1_rts_rate_msb = 13
        self.__reg_txq1_ant_force_lsb = 5
        self.__reg_txq1_ant_force_msb = 5
        self.__reg_txq1_ant_force_value_lsb = 4
        self.__reg_txq1_ant_force_value_msb = 4
        self.__reg_txq1_ant_force_last_lsb = 3
        self.__reg_txq1_ant_force_last_msb = 3
        self.__reg_txrxq1_ant_force_lsb = 2
        self.__reg_txrxq1_ant_force_msb = 2
        self.__reg_txrxq1_ant_force_value_lsb = 1
        self.__reg_txrxq1_ant_force_value_msb = 1
        self.__reg_txrxq1_ant_force_last_lsb = 0
        self.__reg_txrxq1_ant_force_last_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq1_txop_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_txop_sel_msb, self.__reg_txq1_txop_sel_lsb)
    @reg_txq1_txop_sel.setter
    def reg_txq1_txop_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_txop_sel_msb, self.__reg_txq1_txop_sel_lsb, value)

    @property
    def reg_txq1_20txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_20txop_num_msb, self.__reg_txq1_20txop_num_lsb)
    @reg_txq1_20txop_num.setter
    def reg_txq1_20txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_20txop_num_msb, self.__reg_txq1_20txop_num_lsb, value)

    @property
    def reg_txq1_20eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_20eof_num_msb, self.__reg_txq1_20eof_num_lsb)
    @reg_txq1_20eof_num.setter
    def reg_txq1_20eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_20eof_num_msb, self.__reg_txq1_20eof_num_lsb, value)

    @property
    def reg_txq1_rts_rate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_rts_rate_msb, self.__reg_txq1_rts_rate_lsb)
    @reg_txq1_rts_rate.setter
    def reg_txq1_rts_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_rts_rate_msb, self.__reg_txq1_rts_rate_lsb, value)

    @property
    def reg_txq1_ant_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_ant_force_msb, self.__reg_txq1_ant_force_lsb)
    @reg_txq1_ant_force.setter
    def reg_txq1_ant_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_ant_force_msb, self.__reg_txq1_ant_force_lsb, value)

    @property
    def reg_txq1_ant_force_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_ant_force_value_msb, self.__reg_txq1_ant_force_value_lsb)
    @reg_txq1_ant_force_value.setter
    def reg_txq1_ant_force_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_ant_force_value_msb, self.__reg_txq1_ant_force_value_lsb, value)

    @property
    def reg_txq1_ant_force_last(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_ant_force_last_msb, self.__reg_txq1_ant_force_last_lsb)
    @reg_txq1_ant_force_last.setter
    def reg_txq1_ant_force_last(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_ant_force_last_msb, self.__reg_txq1_ant_force_last_lsb, value)

    @property
    def reg_txrxq1_ant_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrxq1_ant_force_msb, self.__reg_txrxq1_ant_force_lsb)
    @reg_txrxq1_ant_force.setter
    def reg_txrxq1_ant_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrxq1_ant_force_msb, self.__reg_txrxq1_ant_force_lsb, value)

    @property
    def reg_txrxq1_ant_force_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrxq1_ant_force_value_msb, self.__reg_txrxq1_ant_force_value_lsb)
    @reg_txrxq1_ant_force_value.setter
    def reg_txrxq1_ant_force_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrxq1_ant_force_value_msb, self.__reg_txrxq1_ant_force_value_lsb, value)

    @property
    def reg_txrxq1_ant_force_last(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrxq1_ant_force_last_msb, self.__reg_txrxq1_ant_force_last_lsb)
    @reg_txrxq1_ant_force_last.setter
    def reg_txrxq1_ant_force_last(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrxq1_ant_force_last_msb, self.__reg_txrxq1_ant_force_last_lsb, value)
class MACTXQ1_DUR(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x2cc
        self.__reg_txq1_20dur_lsb = 16
        self.__reg_txq1_20dur_msb = 31
        self.__reg_txq1_ht40dur_lsb = 0
        self.__reg_txq1_ht40dur_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq1_20dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_20dur_msb, self.__reg_txq1_20dur_lsb)
    @reg_txq1_20dur.setter
    def reg_txq1_20dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_20dur_msb, self.__reg_txq1_20dur_lsb, value)

    @property
    def reg_txq1_ht40dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_ht40dur_msb, self.__reg_txq1_ht40dur_lsb)
    @reg_txq1_ht40dur.setter
    def reg_txq1_ht40dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_ht40dur_msb, self.__reg_txq1_ht40dur_lsb, value)
class MACTXQ1_DUR2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x2d0
        self.__reg_txq1_hwseq_fgmd_lsb = 31
        self.__reg_txq1_hwseq_fgmd_msb = 31
        self.__reg_txq1_hwseq_qmfmd_lsb = 29
        self.__reg_txq1_hwseq_qmfmd_msb = 29
        self.__reg_txq1_hwseq_sel_lsb = 17
        self.__reg_txq1_hwseq_sel_msb = 19
        self.__reg_txq1_hwseq_update_lsb = 16
        self.__reg_txq1_hwseq_update_msb = 16
        self.__reg_txq1_ht80dur_lsb = 0
        self.__reg_txq1_ht80dur_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq1_hwseq_fgmd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_hwseq_fgmd_msb, self.__reg_txq1_hwseq_fgmd_lsb)
    @reg_txq1_hwseq_fgmd.setter
    def reg_txq1_hwseq_fgmd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_hwseq_fgmd_msb, self.__reg_txq1_hwseq_fgmd_lsb, value)

    @property
    def reg_txq1_hwseq_qmfmd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_hwseq_qmfmd_msb, self.__reg_txq1_hwseq_qmfmd_lsb)
    @reg_txq1_hwseq_qmfmd.setter
    def reg_txq1_hwseq_qmfmd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_hwseq_qmfmd_msb, self.__reg_txq1_hwseq_qmfmd_lsb, value)

    @property
    def reg_txq1_hwseq_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_hwseq_sel_msb, self.__reg_txq1_hwseq_sel_lsb)
    @reg_txq1_hwseq_sel.setter
    def reg_txq1_hwseq_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_hwseq_sel_msb, self.__reg_txq1_hwseq_sel_lsb, value)

    @property
    def reg_txq1_hwseq_update(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_hwseq_update_msb, self.__reg_txq1_hwseq_update_lsb)
    @reg_txq1_hwseq_update.setter
    def reg_txq1_hwseq_update(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_hwseq_update_msb, self.__reg_txq1_hwseq_update_lsb, value)
    @property
    def default_value(self):
        return 0x0

    @property
    def reg_txq1_ht80dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq1_ht80dur_msb, self.__reg_txq1_ht80dur_lsb)
    @reg_txq1_ht80dur.setter
    def reg_txq1_ht80dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq1_ht80dur_msb, self.__reg_txq1_ht80dur_lsb, value)
class MACTXQ1PMD(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x2d4
        self.__txq1complete_num_lsb = 28
        self.__txq1complete_num_msb = 31
        self.__txq1_cbw_lsb = 25
        self.__txq1_cbw_msb = 26
        self.__txq1_rssi_lsb = 16
        self.__txq1_rssi_msb = 23
        self.__txq1complete_state_lsb = 12
        self.__txq1complete_state_msb = 15
        self.__txq1complete_st_match_lsb = 8
        self.__txq1complete_st_match_msb = 11
        self.__txq1complete_errcode_lsb = 0
        self.__txq1complete_errcode_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq1complete_num(self):
        return self.__MEM.rdm(self.__addr, self.__txq1complete_num_msb, self.__txq1complete_num_lsb)
    @txq1complete_num.setter
    def txq1complete_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq1complete_num_msb, self.__txq1complete_num_lsb, value)

    @property
    def txq1_cbw(self):
        return self.__MEM.rdm(self.__addr, self.__txq1_cbw_msb, self.__txq1_cbw_lsb)
    @txq1_cbw.setter
    def txq1_cbw(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq1_cbw_msb, self.__txq1_cbw_lsb, value)

    @property
    def txq1_rssi(self):
        return self.__MEM.rdm(self.__addr, self.__txq1_rssi_msb, self.__txq1_rssi_lsb)
    @txq1_rssi.setter
    def txq1_rssi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq1_rssi_msb, self.__txq1_rssi_lsb, value)

    @property
    def txq1complete_state(self):
        return self.__MEM.rdm(self.__addr, self.__txq1complete_state_msb, self.__txq1complete_state_lsb)
    @txq1complete_state.setter
    def txq1complete_state(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq1complete_state_msb, self.__txq1complete_state_lsb, value)

    @property
    def txq1complete_st_match(self):
        return self.__MEM.rdm(self.__addr, self.__txq1complete_st_match_msb, self.__txq1complete_st_match_lsb)
    @txq1complete_st_match.setter
    def txq1complete_st_match(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq1complete_st_match_msb, self.__txq1complete_st_match_lsb, value)

    @property
    def txq1complete_errcode(self):
        return self.__MEM.rdm(self.__addr, self.__txq1complete_errcode_msb, self.__txq1complete_errcode_lsb)
    @txq1complete_errcode.setter
    def txq1complete_errcode(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq1complete_errcode_msb, self.__txq1complete_errcode_lsb, value)
class MACTXQ1BA_BMHI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x2d8
        self.__txq1ba_bmhi_lsb = 0
        self.__txq1ba_bmhi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq1ba_bmhi(self):
        return self.__MEM.rdm(self.__addr, self.__txq1ba_bmhi_msb, self.__txq1ba_bmhi_lsb)
    @txq1ba_bmhi.setter
    def txq1ba_bmhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq1ba_bmhi_msb, self.__txq1ba_bmhi_lsb, value)
class MACTXQ1BA_BMLO(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x2dc
        self.__txq1ba_bmlo_lsb = 0
        self.__txq1ba_bmlo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq1ba_bmlo(self):
        return self.__MEM.rdm(self.__addr, self.__txq1ba_bmlo_msb, self.__txq1ba_bmlo_lsb)
    @txq1ba_bmlo.setter
    def txq1ba_bmlo(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq1ba_bmlo_msb, self.__txq1ba_bmlo_lsb, value)
class MACTXQ1BA_TAHI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x2e0
        self.__txq1ba_tahi_lsb = 0
        self.__txq1ba_tahi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq1ba_tahi(self):
        return self.__MEM.rdm(self.__addr, self.__txq1ba_tahi_msb, self.__txq1ba_tahi_lsb)
    @txq1ba_tahi.setter
    def txq1ba_tahi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq1ba_tahi_msb, self.__txq1ba_tahi_lsb, value)
class MACTXQ1BA_TALO(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x2e4
        self.__txq1ba_talo_lsb = 0
        self.__txq1ba_talo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq1ba_talo(self):
        return self.__MEM.rdm(self.__addr, self.__txq1ba_talo_msb, self.__txq1ba_talo_lsb)
    @txq1ba_talo.setter
    def txq1ba_talo(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq1ba_talo_msb, self.__txq1ba_talo_lsb, value)
class MACTXQ1BA_SSN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x2e8
        self.__txq1ba_tid_lsb = 12
        self.__txq1ba_tid_msb = 15
        self.__txq1ba_ssn_lsb = 0
        self.__txq1ba_ssn_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq1ba_tid(self):
        return self.__MEM.rdm(self.__addr, self.__txq1ba_tid_msb, self.__txq1ba_tid_lsb)
    @txq1ba_tid.setter
    def txq1ba_tid(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq1ba_tid_msb, self.__txq1ba_tid_lsb, value)

    @property
    def txq1ba_ssn(self):
        return self.__MEM.rdm(self.__addr, self.__txq1ba_ssn_msb, self.__txq1ba_ssn_lsb)
    @txq1ba_ssn.setter
    def txq1ba_ssn(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq1ba_ssn_msb, self.__txq1ba_ssn_lsb, value)
class MACTXQ1_TXSTART_US(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x2ec
        self.__txq1_txstart_us_lsb = 0
        self.__txq1_txstart_us_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq1_txstart_us(self):
        return self.__MEM.rdm(self.__addr, self.__txq1_txstart_us_msb, self.__txq1_txstart_us_lsb)
    @txq1_txstart_us.setter
    def txq1_txstart_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq1_txstart_us_msb, self.__txq1_txstart_us_lsb, value)
class MACTXQ1_TXSTART_CYC(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x2f0
        self.__txq1_txrxack_us_hi_lsb = 14
        self.__txq1_txrxack_us_hi_msb = 31
        self.__txq1_txstart_cycle_lsb = 0
        self.__txq1_txstart_cycle_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq1_txrxack_us_hi(self):
        return self.__MEM.rdm(self.__addr, self.__txq1_txrxack_us_hi_msb, self.__txq1_txrxack_us_hi_lsb)
    @txq1_txrxack_us_hi.setter
    def txq1_txrxack_us_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq1_txrxack_us_hi_msb, self.__txq1_txrxack_us_hi_lsb, value)

    @property
    def txq1_txstart_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__txq1_txstart_cycle_msb, self.__txq1_txstart_cycle_lsb)
    @txq1_txstart_cycle.setter
    def txq1_txstart_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq1_txstart_cycle_msb, self.__txq1_txstart_cycle_lsb, value)
class MACTXQ1_TXRXACK_CYC(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x2f4
        self.__txq1_txrxack_us_lsb = 18
        self.__txq1_txrxack_us_msb = 31
        self.__txq1_txrxack_cycdec_lsb = 7
        self.__txq1_txrxack_cycdec_msb = 17
        self.__txq1_txrxack_cycle_lsb = 0
        self.__txq1_txrxack_cycle_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq1_txrxack_us(self):
        return self.__MEM.rdm(self.__addr, self.__txq1_txrxack_us_msb, self.__txq1_txrxack_us_lsb)
    @txq1_txrxack_us.setter
    def txq1_txrxack_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq1_txrxack_us_msb, self.__txq1_txrxack_us_lsb, value)

    @property
    def txq1_txrxack_cycdec(self):
        return self.__MEM.rdm(self.__addr, self.__txq1_txrxack_cycdec_msb, self.__txq1_txrxack_cycdec_lsb)
    @txq1_txrxack_cycdec.setter
    def txq1_txrxack_cycdec(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq1_txrxack_cycdec_msb, self.__txq1_txrxack_cycdec_lsb, value)

    @property
    def txq1_txrxack_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__txq1_txrxack_cycle_msb, self.__txq1_txrxack_cycle_lsb)
    @txq1_txrxack_cycle.setter
    def txq1_txrxack_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq1_txrxack_cycle_msb, self.__txq1_txrxack_cycle_lsb, value)
class MACTXQ0_PLCP1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x2f8
        self.__reg_txq0_data_wbd_lsb = 31
        self.__reg_txq0_data_wbd_msb = 31
        self.__reg_txq0_rts_wbd_lsb = 30
        self.__reg_txq0_rts_wbd_msb = 30
        self.__reg_txq0_force_bw_lsb = 29
        self.__reg_txq0_force_bw_msb = 29
        self.__reg_txq0_nonhtdup_lsb = 27
        self.__reg_txq0_nonhtdup_msb = 28
        self.__reg_txq0_sigmode_lsb = 25
        self.__reg_txq0_sigmode_msb = 26
        self.__reg_txq0_kid_lsb = 17
        self.__reg_txq0_kid_msb = 24
        self.__reg_txq0_rate_lsb = 12
        self.__reg_txq0_rate_msb = 16
        self.__reg_txq0_length_lsb = 0
        self.__reg_txq0_length_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq0_data_wbd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_data_wbd_msb, self.__reg_txq0_data_wbd_lsb)
    @reg_txq0_data_wbd.setter
    def reg_txq0_data_wbd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_data_wbd_msb, self.__reg_txq0_data_wbd_lsb, value)

    @property
    def reg_txq0_rts_wbd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_rts_wbd_msb, self.__reg_txq0_rts_wbd_lsb)
    @reg_txq0_rts_wbd.setter
    def reg_txq0_rts_wbd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_rts_wbd_msb, self.__reg_txq0_rts_wbd_lsb, value)

    @property
    def reg_txq0_force_bw(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_force_bw_msb, self.__reg_txq0_force_bw_lsb)
    @reg_txq0_force_bw.setter
    def reg_txq0_force_bw(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_force_bw_msb, self.__reg_txq0_force_bw_lsb, value)

    @property
    def reg_txq0_nonhtdup(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_nonhtdup_msb, self.__reg_txq0_nonhtdup_lsb)
    @reg_txq0_nonhtdup.setter
    def reg_txq0_nonhtdup(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_nonhtdup_msb, self.__reg_txq0_nonhtdup_lsb, value)

    @property
    def reg_txq0_sigmode(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_sigmode_msb, self.__reg_txq0_sigmode_lsb)
    @reg_txq0_sigmode.setter
    def reg_txq0_sigmode(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_sigmode_msb, self.__reg_txq0_sigmode_lsb, value)

    @property
    def reg_txq0_kid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_kid_msb, self.__reg_txq0_kid_lsb)
    @reg_txq0_kid.setter
    def reg_txq0_kid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_kid_msb, self.__reg_txq0_kid_lsb, value)

    @property
    def reg_txq0_rate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_rate_msb, self.__reg_txq0_rate_lsb)
    @reg_txq0_rate.setter
    def reg_txq0_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_rate_msb, self.__reg_txq0_rate_lsb, value)

    @property
    def reg_txq0_length(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_length_msb, self.__reg_txq0_length_lsb)
    @reg_txq0_length.setter
    def reg_txq0_length(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_length_msb, self.__reg_txq0_length_lsb, value)
class MACTXQ0_PTI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x2fc
        self.__reg_txq0_pti_maintain_cnt_lsb = 20
        self.__reg_txq0_pti_maintain_cnt_msb = 31
        self.__reg_txq0_maintain_pti_lsb = 16
        self.__reg_txq0_maintain_pti_msb = 19
        self.__reg_txq0_rts_pti_lsb = 12
        self.__reg_txq0_rts_pti_msb = 15
        self.__reg_txq0_data_pti_lsb = 8
        self.__reg_txq0_data_pti_msb = 11
        self.__reg_txq0_ack_pti_lsb = 4
        self.__reg_txq0_ack_pti_msb = 7
        self.__reg_txq0_bssid_lsb = 0
        self.__reg_txq0_bssid_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq0_pti_maintain_cnt(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_pti_maintain_cnt_msb, self.__reg_txq0_pti_maintain_cnt_lsb)
    @reg_txq0_pti_maintain_cnt.setter
    def reg_txq0_pti_maintain_cnt(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_pti_maintain_cnt_msb, self.__reg_txq0_pti_maintain_cnt_lsb, value)

    @property
    def reg_txq0_maintain_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_maintain_pti_msb, self.__reg_txq0_maintain_pti_lsb)
    @reg_txq0_maintain_pti.setter
    def reg_txq0_maintain_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_maintain_pti_msb, self.__reg_txq0_maintain_pti_lsb, value)

    @property
    def reg_txq0_rts_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_rts_pti_msb, self.__reg_txq0_rts_pti_lsb)
    @reg_txq0_rts_pti.setter
    def reg_txq0_rts_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_rts_pti_msb, self.__reg_txq0_rts_pti_lsb, value)

    @property
    def reg_txq0_data_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_data_pti_msb, self.__reg_txq0_data_pti_lsb)
    @reg_txq0_data_pti.setter
    def reg_txq0_data_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_data_pti_msb, self.__reg_txq0_data_pti_lsb, value)

    @property
    def reg_txq0_ack_pti(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_ack_pti_msb, self.__reg_txq0_ack_pti_lsb)
    @reg_txq0_ack_pti.setter
    def reg_txq0_ack_pti(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_ack_pti_msb, self.__reg_txq0_ack_pti_lsb, value)

    @property
    def reg_txq0_bssid(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_bssid_msb, self.__reg_txq0_bssid_lsb)
    @reg_txq0_bssid.setter
    def reg_txq0_bssid(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_bssid_msb, self.__reg_txq0_bssid_lsb, value)
class MACTXQ0_HTSIG(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x300
        self.__reg_txq0_htsig_lsb = 0
        self.__reg_txq0_htsig_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq0_htsig(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_htsig_msb, self.__reg_txq0_htsig_lsb)
    @reg_txq0_htsig.setter
    def reg_txq0_htsig(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_htsig_msb, self.__reg_txq0_htsig_lsb, value)
class MACTXQ0_VHTSIG1(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x304
        self.__reg_txq0_vhtsiga_lo_lsb = 0
        self.__reg_txq0_vhtsiga_lo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq0_vhtsiga_lo(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_vhtsiga_lo_msb, self.__reg_txq0_vhtsiga_lo_lsb)
    @reg_txq0_vhtsiga_lo.setter
    def reg_txq0_vhtsiga_lo(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_vhtsiga_lo_msb, self.__reg_txq0_vhtsiga_lo_lsb, value)
class MACTXQ0_VHTSIG2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x308
        self.__reg_txq0_vhtsigb_lsb = 2
        self.__reg_txq0_vhtsigb_msb = 24
        self.__reg_txq0_vhtsiga_hi_lsb = 0
        self.__reg_txq0_vhtsiga_hi_msb = 1
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq0_vhtsigb(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_vhtsigb_msb, self.__reg_txq0_vhtsigb_lsb)
    @reg_txq0_vhtsigb.setter
    def reg_txq0_vhtsigb(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_vhtsigb_msb, self.__reg_txq0_vhtsigb_lsb, value)

    @property
    def reg_txq0_vhtsiga_hi(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_vhtsiga_hi_msb, self.__reg_txq0_vhtsiga_hi_lsb)
    @reg_txq0_vhtsiga_hi.setter
    def reg_txq0_vhtsiga_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_vhtsiga_hi_msb, self.__reg_txq0_vhtsiga_hi_lsb, value)
class MACTXQ0_HT80LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x30c
        self.__reg_txq0_ht80txop_num_lsb = 24
        self.__reg_txq0_ht80txop_num_msb = 27
        self.__reg_txq0_ht80eof_num_lsb = 22
        self.__reg_txq0_ht80eof_num_msb = 23
        self.__reg_txq0_ht80len_lsb = 0
        self.__reg_txq0_ht80len_msb = 20
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq0_ht80txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_ht80txop_num_msb, self.__reg_txq0_ht80txop_num_lsb)
    @reg_txq0_ht80txop_num.setter
    def reg_txq0_ht80txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_ht80txop_num_msb, self.__reg_txq0_ht80txop_num_lsb, value)

    @property
    def reg_txq0_ht80eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_ht80eof_num_msb, self.__reg_txq0_ht80eof_num_lsb)
    @reg_txq0_ht80eof_num.setter
    def reg_txq0_ht80eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_ht80eof_num_msb, self.__reg_txq0_ht80eof_num_lsb, value)

    @property
    def reg_txq0_ht80len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_ht80len_msb, self.__reg_txq0_ht80len_lsb)
    @reg_txq0_ht80len.setter
    def reg_txq0_ht80len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_ht80len_msb, self.__reg_txq0_ht80len_lsb, value)
class MACTXQ0_HT40LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x310
        self.__reg_txq0_ht40txop_num_lsb = 24
        self.__reg_txq0_ht40txop_num_msb = 27
        self.__reg_txq0_ht40eof_num_lsb = 22
        self.__reg_txq0_ht40eof_num_msb = 23
        self.__reg_txq0_ht40len_lsb = 0
        self.__reg_txq0_ht40len_msb = 18
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq0_ht40txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_ht40txop_num_msb, self.__reg_txq0_ht40txop_num_lsb)
    @reg_txq0_ht40txop_num.setter
    def reg_txq0_ht40txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_ht40txop_num_msb, self.__reg_txq0_ht40txop_num_lsb, value)

    @property
    def reg_txq0_ht40eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_ht40eof_num_msb, self.__reg_txq0_ht40eof_num_lsb)
    @reg_txq0_ht40eof_num.setter
    def reg_txq0_ht40eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_ht40eof_num_msb, self.__reg_txq0_ht40eof_num_lsb, value)

    @property
    def reg_txq0_ht40len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_ht40len_msb, self.__reg_txq0_ht40len_lsb)
    @reg_txq0_ht40len.setter
    def reg_txq0_ht40len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_ht40len_msb, self.__reg_txq0_ht40len_lsb, value)
class MACTXQ0_HT20LEN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x314
        self.__reg_txq0_txop_sel_lsb = 28
        self.__reg_txq0_txop_sel_msb = 29
        self.__reg_txq0_20txop_num_lsb = 24
        self.__reg_txq0_20txop_num_msb = 27
        self.__reg_txq0_20eof_num_lsb = 22
        self.__reg_txq0_20eof_num_msb = 23
        self.__reg_txq0_rts_rate_lsb = 6
        self.__reg_txq0_rts_rate_msb = 13
        self.__reg_txq0_ant_force_lsb = 5
        self.__reg_txq0_ant_force_msb = 5
        self.__reg_txq0_ant_force_value_lsb = 4
        self.__reg_txq0_ant_force_value_msb = 4
        self.__reg_txq0_ant_force_last_lsb = 3
        self.__reg_txq0_ant_force_last_msb = 3
        self.__reg_txrxq0_ant_force_lsb = 2
        self.__reg_txrxq0_ant_force_msb = 2
        self.__reg_txrxq0_ant_force_value_lsb = 1
        self.__reg_txrxq0_ant_force_value_msb = 1
        self.__reg_txrxq0_ant_force_last_lsb = 0
        self.__reg_txrxq0_ant_force_last_msb = 0
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq0_txop_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_txop_sel_msb, self.__reg_txq0_txop_sel_lsb)
    @reg_txq0_txop_sel.setter
    def reg_txq0_txop_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_txop_sel_msb, self.__reg_txq0_txop_sel_lsb, value)

    @property
    def reg_txq0_20txop_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_20txop_num_msb, self.__reg_txq0_20txop_num_lsb)
    @reg_txq0_20txop_num.setter
    def reg_txq0_20txop_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_20txop_num_msb, self.__reg_txq0_20txop_num_lsb, value)

    @property
    def reg_txq0_20eof_num(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_20eof_num_msb, self.__reg_txq0_20eof_num_lsb)
    @reg_txq0_20eof_num.setter
    def reg_txq0_20eof_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_20eof_num_msb, self.__reg_txq0_20eof_num_lsb, value)

    @property
    def reg_txq0_rts_rate(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_rts_rate_msb, self.__reg_txq0_rts_rate_lsb)
    @reg_txq0_rts_rate.setter
    def reg_txq0_rts_rate(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_rts_rate_msb, self.__reg_txq0_rts_rate_lsb, value)

    @property
    def reg_txq0_ant_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_ant_force_msb, self.__reg_txq0_ant_force_lsb)
    @reg_txq0_ant_force.setter
    def reg_txq0_ant_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_ant_force_msb, self.__reg_txq0_ant_force_lsb, value)

    @property
    def reg_txq0_ant_force_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_ant_force_value_msb, self.__reg_txq0_ant_force_value_lsb)
    @reg_txq0_ant_force_value.setter
    def reg_txq0_ant_force_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_ant_force_value_msb, self.__reg_txq0_ant_force_value_lsb, value)

    @property
    def reg_txq0_ant_force_last(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_ant_force_last_msb, self.__reg_txq0_ant_force_last_lsb)
    @reg_txq0_ant_force_last.setter
    def reg_txq0_ant_force_last(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_ant_force_last_msb, self.__reg_txq0_ant_force_last_lsb, value)

    @property
    def reg_txrxq0_ant_force(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrxq0_ant_force_msb, self.__reg_txrxq0_ant_force_lsb)
    @reg_txrxq0_ant_force.setter
    def reg_txrxq0_ant_force(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrxq0_ant_force_msb, self.__reg_txrxq0_ant_force_lsb, value)

    @property
    def reg_txrxq0_ant_force_value(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrxq0_ant_force_value_msb, self.__reg_txrxq0_ant_force_value_lsb)
    @reg_txrxq0_ant_force_value.setter
    def reg_txrxq0_ant_force_value(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrxq0_ant_force_value_msb, self.__reg_txrxq0_ant_force_value_lsb, value)

    @property
    def reg_txrxq0_ant_force_last(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txrxq0_ant_force_last_msb, self.__reg_txrxq0_ant_force_last_lsb)
    @reg_txrxq0_ant_force_last.setter
    def reg_txrxq0_ant_force_last(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txrxq0_ant_force_last_msb, self.__reg_txrxq0_ant_force_last_lsb, value)
class MACTXQ0_DUR(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x318
        self.__reg_txq0_20dur_lsb = 16
        self.__reg_txq0_20dur_msb = 31
        self.__reg_txq0_ht40dur_lsb = 0
        self.__reg_txq0_ht40dur_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq0_20dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_20dur_msb, self.__reg_txq0_20dur_lsb)
    @reg_txq0_20dur.setter
    def reg_txq0_20dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_20dur_msb, self.__reg_txq0_20dur_lsb, value)

    @property
    def reg_txq0_ht40dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_ht40dur_msb, self.__reg_txq0_ht40dur_lsb)
    @reg_txq0_ht40dur.setter
    def reg_txq0_ht40dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_ht40dur_msb, self.__reg_txq0_ht40dur_lsb, value)
class MACTXQ0_DUR2(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x31c
        self.__reg_txq0_hwseq_fgmd_lsb = 31
        self.__reg_txq0_hwseq_fgmd_msb = 31
        self.__reg_txq0_hwseq_qmfmd_lsb = 29
        self.__reg_txq0_hwseq_qmfmd_msb = 29
        self.__reg_txq0_hwseq_sel_lsb = 17
        self.__reg_txq0_hwseq_sel_msb = 19
        self.__reg_txq0_hwseq_update_lsb = 16
        self.__reg_txq0_hwseq_update_msb = 16
        self.__reg_txq0_ht80dur_lsb = 0
        self.__reg_txq0_ht80dur_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txq0_hwseq_fgmd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_hwseq_fgmd_msb, self.__reg_txq0_hwseq_fgmd_lsb)
    @reg_txq0_hwseq_fgmd.setter
    def reg_txq0_hwseq_fgmd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_hwseq_fgmd_msb, self.__reg_txq0_hwseq_fgmd_lsb, value)

    @property
    def reg_txq0_hwseq_qmfmd(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_hwseq_qmfmd_msb, self.__reg_txq0_hwseq_qmfmd_lsb)
    @reg_txq0_hwseq_qmfmd.setter
    def reg_txq0_hwseq_qmfmd(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_hwseq_qmfmd_msb, self.__reg_txq0_hwseq_qmfmd_lsb, value)

    @property
    def reg_txq0_hwseq_sel(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_hwseq_sel_msb, self.__reg_txq0_hwseq_sel_lsb)
    @reg_txq0_hwseq_sel.setter
    def reg_txq0_hwseq_sel(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_hwseq_sel_msb, self.__reg_txq0_hwseq_sel_lsb, value)

    @property
    def reg_txq0_hwseq_update(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_hwseq_update_msb, self.__reg_txq0_hwseq_update_lsb)
    @reg_txq0_hwseq_update.setter
    def reg_txq0_hwseq_update(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_hwseq_update_msb, self.__reg_txq0_hwseq_update_lsb, value)
    @property
    def default_value(self):
        return 0x0

    @property
    def reg_txq0_ht80dur(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txq0_ht80dur_msb, self.__reg_txq0_ht80dur_lsb)
    @reg_txq0_ht80dur.setter
    def reg_txq0_ht80dur(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txq0_ht80dur_msb, self.__reg_txq0_ht80dur_lsb, value)
class MACTXQ0PMD(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x320
        self.__txq0complete_num_lsb = 28
        self.__txq0complete_num_msb = 31
        self.__txq0_cbw_lsb = 25
        self.__txq0_cbw_msb = 26
        self.__txq0_rssi_lsb = 16
        self.__txq0_rssi_msb = 23
        self.__txq0complete_state_lsb = 12
        self.__txq0complete_state_msb = 15
        self.__txq0complete_st_match_lsb = 8
        self.__txq0complete_st_match_msb = 11
        self.__txq0complete_errcode_lsb = 0
        self.__txq0complete_errcode_msb = 7
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq0complete_num(self):
        return self.__MEM.rdm(self.__addr, self.__txq0complete_num_msb, self.__txq0complete_num_lsb)
    @txq0complete_num.setter
    def txq0complete_num(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq0complete_num_msb, self.__txq0complete_num_lsb, value)

    @property
    def txq0_cbw(self):
        return self.__MEM.rdm(self.__addr, self.__txq0_cbw_msb, self.__txq0_cbw_lsb)
    @txq0_cbw.setter
    def txq0_cbw(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq0_cbw_msb, self.__txq0_cbw_lsb, value)

    @property
    def txq0_rssi(self):
        return self.__MEM.rdm(self.__addr, self.__txq0_rssi_msb, self.__txq0_rssi_lsb)
    @txq0_rssi.setter
    def txq0_rssi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq0_rssi_msb, self.__txq0_rssi_lsb, value)

    @property
    def txq0complete_state(self):
        return self.__MEM.rdm(self.__addr, self.__txq0complete_state_msb, self.__txq0complete_state_lsb)
    @txq0complete_state.setter
    def txq0complete_state(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq0complete_state_msb, self.__txq0complete_state_lsb, value)

    @property
    def txq0complete_st_match(self):
        return self.__MEM.rdm(self.__addr, self.__txq0complete_st_match_msb, self.__txq0complete_st_match_lsb)
    @txq0complete_st_match.setter
    def txq0complete_st_match(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq0complete_st_match_msb, self.__txq0complete_st_match_lsb, value)

    @property
    def txq0complete_errcode(self):
        return self.__MEM.rdm(self.__addr, self.__txq0complete_errcode_msb, self.__txq0complete_errcode_lsb)
    @txq0complete_errcode.setter
    def txq0complete_errcode(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq0complete_errcode_msb, self.__txq0complete_errcode_lsb, value)
class MACTXQ0BA_BMHI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x324
        self.__txq0ba_bmhi_lsb = 0
        self.__txq0ba_bmhi_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq0ba_bmhi(self):
        return self.__MEM.rdm(self.__addr, self.__txq0ba_bmhi_msb, self.__txq0ba_bmhi_lsb)
    @txq0ba_bmhi.setter
    def txq0ba_bmhi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq0ba_bmhi_msb, self.__txq0ba_bmhi_lsb, value)
class MACTXQ0BA_BMLO(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x328
        self.__txq0ba_bmlo_lsb = 0
        self.__txq0ba_bmlo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq0ba_bmlo(self):
        return self.__MEM.rdm(self.__addr, self.__txq0ba_bmlo_msb, self.__txq0ba_bmlo_lsb)
    @txq0ba_bmlo.setter
    def txq0ba_bmlo(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq0ba_bmlo_msb, self.__txq0ba_bmlo_lsb, value)
class MACTXQ0BA_TAHI(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x32c
        self.__txq0ba_tahi_lsb = 0
        self.__txq0ba_tahi_msb = 15
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq0ba_tahi(self):
        return self.__MEM.rdm(self.__addr, self.__txq0ba_tahi_msb, self.__txq0ba_tahi_lsb)
    @txq0ba_tahi.setter
    def txq0ba_tahi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq0ba_tahi_msb, self.__txq0ba_tahi_lsb, value)
class MACTXQ0BA_TALO(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x330
        self.__txq0ba_talo_lsb = 0
        self.__txq0ba_talo_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq0ba_talo(self):
        return self.__MEM.rdm(self.__addr, self.__txq0ba_talo_msb, self.__txq0ba_talo_lsb)
    @txq0ba_talo.setter
    def txq0ba_talo(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq0ba_talo_msb, self.__txq0ba_talo_lsb, value)
class MACTXQ0BA_SSN(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x334
        self.__txq0ba_tid_lsb = 12
        self.__txq0ba_tid_msb = 15
        self.__txq0ba_ssn_lsb = 0
        self.__txq0ba_ssn_msb = 11
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq0ba_tid(self):
        return self.__MEM.rdm(self.__addr, self.__txq0ba_tid_msb, self.__txq0ba_tid_lsb)
    @txq0ba_tid.setter
    def txq0ba_tid(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq0ba_tid_msb, self.__txq0ba_tid_lsb, value)

    @property
    def txq0ba_ssn(self):
        return self.__MEM.rdm(self.__addr, self.__txq0ba_ssn_msb, self.__txq0ba_ssn_lsb)
    @txq0ba_ssn.setter
    def txq0ba_ssn(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq0ba_ssn_msb, self.__txq0ba_ssn_lsb, value)
class MACTXQ0_TXSTART_US(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x338
        self.__txq0_txstart_us_lsb = 0
        self.__txq0_txstart_us_msb = 31
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq0_txstart_us(self):
        return self.__MEM.rdm(self.__addr, self.__txq0_txstart_us_msb, self.__txq0_txstart_us_lsb)
    @txq0_txstart_us.setter
    def txq0_txstart_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq0_txstart_us_msb, self.__txq0_txstart_us_lsb, value)
class MACTXQ0_TXSTART_CYC(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x33c
        self.__txq0_txrxack_us_hi_lsb = 14
        self.__txq0_txrxack_us_hi_msb = 31
        self.__txq0_txstart_cycle_lsb = 0
        self.__txq0_txstart_cycle_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq0_txrxack_us_hi(self):
        return self.__MEM.rdm(self.__addr, self.__txq0_txrxack_us_hi_msb, self.__txq0_txrxack_us_hi_lsb)
    @txq0_txrxack_us_hi.setter
    def txq0_txrxack_us_hi(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq0_txrxack_us_hi_msb, self.__txq0_txrxack_us_hi_lsb, value)

    @property
    def txq0_txstart_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__txq0_txstart_cycle_msb, self.__txq0_txstart_cycle_lsb)
    @txq0_txstart_cycle.setter
    def txq0_txstart_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq0_txstart_cycle_msb, self.__txq0_txstart_cycle_lsb, value)
class MACTXQ0_TXRXACK_CYC(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x340
        self.__txq0_txrxack_us_lsb = 18
        self.__txq0_txrxack_us_msb = 31
        self.__txq0_txrxack_cycdec_lsb = 7
        self.__txq0_txrxack_cycdec_msb = 17
        self.__txq0_txrxack_cycle_lsb = 0
        self.__txq0_txrxack_cycle_msb = 6
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def txq0_txrxack_us(self):
        return self.__MEM.rdm(self.__addr, self.__txq0_txrxack_us_msb, self.__txq0_txrxack_us_lsb)
    @txq0_txrxack_us.setter
    def txq0_txrxack_us(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq0_txrxack_us_msb, self.__txq0_txrxack_us_lsb, value)

    @property
    def txq0_txrxack_cycdec(self):
        return self.__MEM.rdm(self.__addr, self.__txq0_txrxack_cycdec_msb, self.__txq0_txrxack_cycdec_lsb)
    @txq0_txrxack_cycdec.setter
    def txq0_txrxack_cycdec(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq0_txrxack_cycdec_msb, self.__txq0_txrxack_cycdec_lsb, value)

    @property
    def txq0_txrxack_cycle(self):
        return self.__MEM.rdm(self.__addr, self.__txq0_txrxack_cycle_msb, self.__txq0_txrxack_cycle_lsb)
    @txq0_txrxack_cycle.setter
    def txq0_txrxack_cycle(self, value):
        return self.__MEM.wrm(self.__addr, self.__txq0_txrxack_cycle_msb, self.__txq0_txrxack_cycle_lsb, value)
class MACTXOP0_Q15_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x344
        self.__reg_txop0_q15_len_lsb = 20
        self.__reg_txop0_q15_len_msb = 31
        self.__reg_txop0_q15_link_addr_lsb = 0
        self.__reg_txop0_q15_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop0_q15_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q15_len_msb, self.__reg_txop0_q15_len_lsb)
    @reg_txop0_q15_len.setter
    def reg_txop0_q15_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q15_len_msb, self.__reg_txop0_q15_len_lsb, value)

    @property
    def reg_txop0_q15_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q15_link_addr_msb, self.__reg_txop0_q15_link_addr_lsb)
    @reg_txop0_q15_link_addr.setter
    def reg_txop0_q15_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q15_link_addr_msb, self.__reg_txop0_q15_link_addr_lsb, value)
class MACTXOP0_Q14_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x348
        self.__reg_txop0_q14_len_lsb = 20
        self.__reg_txop0_q14_len_msb = 31
        self.__reg_txop0_q14_link_addr_lsb = 0
        self.__reg_txop0_q14_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop0_q14_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q14_len_msb, self.__reg_txop0_q14_len_lsb)
    @reg_txop0_q14_len.setter
    def reg_txop0_q14_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q14_len_msb, self.__reg_txop0_q14_len_lsb, value)

    @property
    def reg_txop0_q14_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q14_link_addr_msb, self.__reg_txop0_q14_link_addr_lsb)
    @reg_txop0_q14_link_addr.setter
    def reg_txop0_q14_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q14_link_addr_msb, self.__reg_txop0_q14_link_addr_lsb, value)
class MACTXOP0_Q13_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x34c
        self.__reg_txop0_q13_len_lsb = 20
        self.__reg_txop0_q13_len_msb = 31
        self.__reg_txop0_q13_link_addr_lsb = 0
        self.__reg_txop0_q13_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop0_q13_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q13_len_msb, self.__reg_txop0_q13_len_lsb)
    @reg_txop0_q13_len.setter
    def reg_txop0_q13_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q13_len_msb, self.__reg_txop0_q13_len_lsb, value)

    @property
    def reg_txop0_q13_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q13_link_addr_msb, self.__reg_txop0_q13_link_addr_lsb)
    @reg_txop0_q13_link_addr.setter
    def reg_txop0_q13_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q13_link_addr_msb, self.__reg_txop0_q13_link_addr_lsb, value)
class MACTXOP0_Q12_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x350
        self.__reg_txop0_q12_len_lsb = 20
        self.__reg_txop0_q12_len_msb = 31
        self.__reg_txop0_q12_link_addr_lsb = 0
        self.__reg_txop0_q12_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop0_q12_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q12_len_msb, self.__reg_txop0_q12_len_lsb)
    @reg_txop0_q12_len.setter
    def reg_txop0_q12_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q12_len_msb, self.__reg_txop0_q12_len_lsb, value)

    @property
    def reg_txop0_q12_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q12_link_addr_msb, self.__reg_txop0_q12_link_addr_lsb)
    @reg_txop0_q12_link_addr.setter
    def reg_txop0_q12_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q12_link_addr_msb, self.__reg_txop0_q12_link_addr_lsb, value)
class MACTXOP0_Q11_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x354
        self.__reg_txop0_q11_len_lsb = 20
        self.__reg_txop0_q11_len_msb = 31
        self.__reg_txop0_q11_link_addr_lsb = 0
        self.__reg_txop0_q11_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop0_q11_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q11_len_msb, self.__reg_txop0_q11_len_lsb)
    @reg_txop0_q11_len.setter
    def reg_txop0_q11_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q11_len_msb, self.__reg_txop0_q11_len_lsb, value)

    @property
    def reg_txop0_q11_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q11_link_addr_msb, self.__reg_txop0_q11_link_addr_lsb)
    @reg_txop0_q11_link_addr.setter
    def reg_txop0_q11_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q11_link_addr_msb, self.__reg_txop0_q11_link_addr_lsb, value)
class MACTXOP0_Q10_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x358
        self.__reg_txop0_q10_len_lsb = 20
        self.__reg_txop0_q10_len_msb = 31
        self.__reg_txop0_q10_link_addr_lsb = 0
        self.__reg_txop0_q10_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop0_q10_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q10_len_msb, self.__reg_txop0_q10_len_lsb)
    @reg_txop0_q10_len.setter
    def reg_txop0_q10_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q10_len_msb, self.__reg_txop0_q10_len_lsb, value)

    @property
    def reg_txop0_q10_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q10_link_addr_msb, self.__reg_txop0_q10_link_addr_lsb)
    @reg_txop0_q10_link_addr.setter
    def reg_txop0_q10_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q10_link_addr_msb, self.__reg_txop0_q10_link_addr_lsb, value)
class MACTXOP0_Q9_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x35c
        self.__reg_txop0_q9_len_lsb = 20
        self.__reg_txop0_q9_len_msb = 31
        self.__reg_txop0_q9_link_addr_lsb = 0
        self.__reg_txop0_q9_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop0_q9_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q9_len_msb, self.__reg_txop0_q9_len_lsb)
    @reg_txop0_q9_len.setter
    def reg_txop0_q9_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q9_len_msb, self.__reg_txop0_q9_len_lsb, value)

    @property
    def reg_txop0_q9_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q9_link_addr_msb, self.__reg_txop0_q9_link_addr_lsb)
    @reg_txop0_q9_link_addr.setter
    def reg_txop0_q9_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q9_link_addr_msb, self.__reg_txop0_q9_link_addr_lsb, value)
class MACTXOP0_Q8_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x360
        self.__reg_txop0_q8_len_lsb = 20
        self.__reg_txop0_q8_len_msb = 31
        self.__reg_txop0_q8_link_addr_lsb = 0
        self.__reg_txop0_q8_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop0_q8_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q8_len_msb, self.__reg_txop0_q8_len_lsb)
    @reg_txop0_q8_len.setter
    def reg_txop0_q8_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q8_len_msb, self.__reg_txop0_q8_len_lsb, value)

    @property
    def reg_txop0_q8_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q8_link_addr_msb, self.__reg_txop0_q8_link_addr_lsb)
    @reg_txop0_q8_link_addr.setter
    def reg_txop0_q8_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q8_link_addr_msb, self.__reg_txop0_q8_link_addr_lsb, value)
class MACTXOP0_Q7_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x364
        self.__reg_txop0_q7_len_lsb = 20
        self.__reg_txop0_q7_len_msb = 31
        self.__reg_txop0_q7_link_addr_lsb = 0
        self.__reg_txop0_q7_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop0_q7_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q7_len_msb, self.__reg_txop0_q7_len_lsb)
    @reg_txop0_q7_len.setter
    def reg_txop0_q7_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q7_len_msb, self.__reg_txop0_q7_len_lsb, value)

    @property
    def reg_txop0_q7_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q7_link_addr_msb, self.__reg_txop0_q7_link_addr_lsb)
    @reg_txop0_q7_link_addr.setter
    def reg_txop0_q7_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q7_link_addr_msb, self.__reg_txop0_q7_link_addr_lsb, value)
class MACTXOP0_Q6_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x368
        self.__reg_txop0_q6_len_lsb = 20
        self.__reg_txop0_q6_len_msb = 31
        self.__reg_txop0_q6_link_addr_lsb = 0
        self.__reg_txop0_q6_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop0_q6_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q6_len_msb, self.__reg_txop0_q6_len_lsb)
    @reg_txop0_q6_len.setter
    def reg_txop0_q6_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q6_len_msb, self.__reg_txop0_q6_len_lsb, value)

    @property
    def reg_txop0_q6_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q6_link_addr_msb, self.__reg_txop0_q6_link_addr_lsb)
    @reg_txop0_q6_link_addr.setter
    def reg_txop0_q6_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q6_link_addr_msb, self.__reg_txop0_q6_link_addr_lsb, value)
class MACTXOP0_Q5_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x36c
        self.__reg_txop0_q5_len_lsb = 20
        self.__reg_txop0_q5_len_msb = 31
        self.__reg_txop0_q5_link_addr_lsb = 0
        self.__reg_txop0_q5_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop0_q5_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q5_len_msb, self.__reg_txop0_q5_len_lsb)
    @reg_txop0_q5_len.setter
    def reg_txop0_q5_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q5_len_msb, self.__reg_txop0_q5_len_lsb, value)

    @property
    def reg_txop0_q5_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q5_link_addr_msb, self.__reg_txop0_q5_link_addr_lsb)
    @reg_txop0_q5_link_addr.setter
    def reg_txop0_q5_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q5_link_addr_msb, self.__reg_txop0_q5_link_addr_lsb, value)
class MACTXOP0_Q4_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x370
        self.__reg_txop0_q4_len_lsb = 20
        self.__reg_txop0_q4_len_msb = 31
        self.__reg_txop0_q4_link_addr_lsb = 0
        self.__reg_txop0_q4_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop0_q4_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q4_len_msb, self.__reg_txop0_q4_len_lsb)
    @reg_txop0_q4_len.setter
    def reg_txop0_q4_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q4_len_msb, self.__reg_txop0_q4_len_lsb, value)

    @property
    def reg_txop0_q4_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q4_link_addr_msb, self.__reg_txop0_q4_link_addr_lsb)
    @reg_txop0_q4_link_addr.setter
    def reg_txop0_q4_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q4_link_addr_msb, self.__reg_txop0_q4_link_addr_lsb, value)
class MACTXOP0_Q3_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x374
        self.__reg_txop0_q3_len_lsb = 20
        self.__reg_txop0_q3_len_msb = 31
        self.__reg_txop0_q3_link_addr_lsb = 0
        self.__reg_txop0_q3_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop0_q3_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q3_len_msb, self.__reg_txop0_q3_len_lsb)
    @reg_txop0_q3_len.setter
    def reg_txop0_q3_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q3_len_msb, self.__reg_txop0_q3_len_lsb, value)

    @property
    def reg_txop0_q3_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q3_link_addr_msb, self.__reg_txop0_q3_link_addr_lsb)
    @reg_txop0_q3_link_addr.setter
    def reg_txop0_q3_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q3_link_addr_msb, self.__reg_txop0_q3_link_addr_lsb, value)
class MACTXOP0_Q2_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x378
        self.__reg_txop0_q2_len_lsb = 20
        self.__reg_txop0_q2_len_msb = 31
        self.__reg_txop0_q2_link_addr_lsb = 0
        self.__reg_txop0_q2_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop0_q2_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q2_len_msb, self.__reg_txop0_q2_len_lsb)
    @reg_txop0_q2_len.setter
    def reg_txop0_q2_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q2_len_msb, self.__reg_txop0_q2_len_lsb, value)

    @property
    def reg_txop0_q2_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q2_link_addr_msb, self.__reg_txop0_q2_link_addr_lsb)
    @reg_txop0_q2_link_addr.setter
    def reg_txop0_q2_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q2_link_addr_msb, self.__reg_txop0_q2_link_addr_lsb, value)
class MACTXOP0_Q1_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x37c
        self.__reg_txop0_q1_len_lsb = 20
        self.__reg_txop0_q1_len_msb = 31
        self.__reg_txop0_q1_link_addr_lsb = 0
        self.__reg_txop0_q1_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop0_q1_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q1_len_msb, self.__reg_txop0_q1_len_lsb)
    @reg_txop0_q1_len.setter
    def reg_txop0_q1_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q1_len_msb, self.__reg_txop0_q1_len_lsb, value)

    @property
    def reg_txop0_q1_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop0_q1_link_addr_msb, self.__reg_txop0_q1_link_addr_lsb)
    @reg_txop0_q1_link_addr.setter
    def reg_txop0_q1_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop0_q1_link_addr_msb, self.__reg_txop0_q1_link_addr_lsb, value)
class MACTXOP1_Q15_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x380
        self.__reg_txop1_q15_len_lsb = 20
        self.__reg_txop1_q15_len_msb = 31
        self.__reg_txop1_q15_link_addr_lsb = 0
        self.__reg_txop1_q15_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop1_q15_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q15_len_msb, self.__reg_txop1_q15_len_lsb)
    @reg_txop1_q15_len.setter
    def reg_txop1_q15_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q15_len_msb, self.__reg_txop1_q15_len_lsb, value)

    @property
    def reg_txop1_q15_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q15_link_addr_msb, self.__reg_txop1_q15_link_addr_lsb)
    @reg_txop1_q15_link_addr.setter
    def reg_txop1_q15_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q15_link_addr_msb, self.__reg_txop1_q15_link_addr_lsb, value)
class MACTXOP1_Q14_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x384
        self.__reg_txop1_q14_len_lsb = 20
        self.__reg_txop1_q14_len_msb = 31
        self.__reg_txop1_q14_link_addr_lsb = 0
        self.__reg_txop1_q14_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop1_q14_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q14_len_msb, self.__reg_txop1_q14_len_lsb)
    @reg_txop1_q14_len.setter
    def reg_txop1_q14_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q14_len_msb, self.__reg_txop1_q14_len_lsb, value)

    @property
    def reg_txop1_q14_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q14_link_addr_msb, self.__reg_txop1_q14_link_addr_lsb)
    @reg_txop1_q14_link_addr.setter
    def reg_txop1_q14_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q14_link_addr_msb, self.__reg_txop1_q14_link_addr_lsb, value)
class MACTXOP1_Q13_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x388
        self.__reg_txop1_q13_len_lsb = 20
        self.__reg_txop1_q13_len_msb = 31
        self.__reg_txop1_q13_link_addr_lsb = 0
        self.__reg_txop1_q13_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop1_q13_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q13_len_msb, self.__reg_txop1_q13_len_lsb)
    @reg_txop1_q13_len.setter
    def reg_txop1_q13_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q13_len_msb, self.__reg_txop1_q13_len_lsb, value)

    @property
    def reg_txop1_q13_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q13_link_addr_msb, self.__reg_txop1_q13_link_addr_lsb)
    @reg_txop1_q13_link_addr.setter
    def reg_txop1_q13_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q13_link_addr_msb, self.__reg_txop1_q13_link_addr_lsb, value)
class MACTXOP1_Q12_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x38c
        self.__reg_txop1_q12_len_lsb = 20
        self.__reg_txop1_q12_len_msb = 31
        self.__reg_txop1_q12_link_addr_lsb = 0
        self.__reg_txop1_q12_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop1_q12_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q12_len_msb, self.__reg_txop1_q12_len_lsb)
    @reg_txop1_q12_len.setter
    def reg_txop1_q12_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q12_len_msb, self.__reg_txop1_q12_len_lsb, value)

    @property
    def reg_txop1_q12_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q12_link_addr_msb, self.__reg_txop1_q12_link_addr_lsb)
    @reg_txop1_q12_link_addr.setter
    def reg_txop1_q12_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q12_link_addr_msb, self.__reg_txop1_q12_link_addr_lsb, value)
class MACTXOP1_Q11_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x390
        self.__reg_txop1_q11_len_lsb = 20
        self.__reg_txop1_q11_len_msb = 31
        self.__reg_txop1_q11_link_addr_lsb = 0
        self.__reg_txop1_q11_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop1_q11_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q11_len_msb, self.__reg_txop1_q11_len_lsb)
    @reg_txop1_q11_len.setter
    def reg_txop1_q11_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q11_len_msb, self.__reg_txop1_q11_len_lsb, value)

    @property
    def reg_txop1_q11_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q11_link_addr_msb, self.__reg_txop1_q11_link_addr_lsb)
    @reg_txop1_q11_link_addr.setter
    def reg_txop1_q11_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q11_link_addr_msb, self.__reg_txop1_q11_link_addr_lsb, value)
class MACTXOP1_Q10_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x394
        self.__reg_txop1_q10_len_lsb = 20
        self.__reg_txop1_q10_len_msb = 31
        self.__reg_txop1_q10_link_addr_lsb = 0
        self.__reg_txop1_q10_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop1_q10_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q10_len_msb, self.__reg_txop1_q10_len_lsb)
    @reg_txop1_q10_len.setter
    def reg_txop1_q10_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q10_len_msb, self.__reg_txop1_q10_len_lsb, value)

    @property
    def reg_txop1_q10_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q10_link_addr_msb, self.__reg_txop1_q10_link_addr_lsb)
    @reg_txop1_q10_link_addr.setter
    def reg_txop1_q10_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q10_link_addr_msb, self.__reg_txop1_q10_link_addr_lsb, value)
class MACTXOP1_Q9_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x398
        self.__reg_txop1_q9_len_lsb = 20
        self.__reg_txop1_q9_len_msb = 31
        self.__reg_txop1_q9_link_addr_lsb = 0
        self.__reg_txop1_q9_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop1_q9_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q9_len_msb, self.__reg_txop1_q9_len_lsb)
    @reg_txop1_q9_len.setter
    def reg_txop1_q9_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q9_len_msb, self.__reg_txop1_q9_len_lsb, value)

    @property
    def reg_txop1_q9_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q9_link_addr_msb, self.__reg_txop1_q9_link_addr_lsb)
    @reg_txop1_q9_link_addr.setter
    def reg_txop1_q9_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q9_link_addr_msb, self.__reg_txop1_q9_link_addr_lsb, value)
class MACTXOP1_Q8_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x39c
        self.__reg_txop1_q8_len_lsb = 20
        self.__reg_txop1_q8_len_msb = 31
        self.__reg_txop1_q8_link_addr_lsb = 0
        self.__reg_txop1_q8_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop1_q8_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q8_len_msb, self.__reg_txop1_q8_len_lsb)
    @reg_txop1_q8_len.setter
    def reg_txop1_q8_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q8_len_msb, self.__reg_txop1_q8_len_lsb, value)

    @property
    def reg_txop1_q8_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q8_link_addr_msb, self.__reg_txop1_q8_link_addr_lsb)
    @reg_txop1_q8_link_addr.setter
    def reg_txop1_q8_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q8_link_addr_msb, self.__reg_txop1_q8_link_addr_lsb, value)
class MACTXOP1_Q7_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x3a0
        self.__reg_txop1_q7_len_lsb = 20
        self.__reg_txop1_q7_len_msb = 31
        self.__reg_txop1_q7_link_addr_lsb = 0
        self.__reg_txop1_q7_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop1_q7_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q7_len_msb, self.__reg_txop1_q7_len_lsb)
    @reg_txop1_q7_len.setter
    def reg_txop1_q7_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q7_len_msb, self.__reg_txop1_q7_len_lsb, value)

    @property
    def reg_txop1_q7_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q7_link_addr_msb, self.__reg_txop1_q7_link_addr_lsb)
    @reg_txop1_q7_link_addr.setter
    def reg_txop1_q7_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q7_link_addr_msb, self.__reg_txop1_q7_link_addr_lsb, value)
class MACTXOP1_Q6_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x3a4
        self.__reg_txop1_q6_len_lsb = 20
        self.__reg_txop1_q6_len_msb = 31
        self.__reg_txop1_q6_link_addr_lsb = 0
        self.__reg_txop1_q6_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop1_q6_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q6_len_msb, self.__reg_txop1_q6_len_lsb)
    @reg_txop1_q6_len.setter
    def reg_txop1_q6_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q6_len_msb, self.__reg_txop1_q6_len_lsb, value)

    @property
    def reg_txop1_q6_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q6_link_addr_msb, self.__reg_txop1_q6_link_addr_lsb)
    @reg_txop1_q6_link_addr.setter
    def reg_txop1_q6_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q6_link_addr_msb, self.__reg_txop1_q6_link_addr_lsb, value)
class MACTXOP1_Q5_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x3a8
        self.__reg_txop1_q5_len_lsb = 20
        self.__reg_txop1_q5_len_msb = 31
        self.__reg_txop1_q5_link_addr_lsb = 0
        self.__reg_txop1_q5_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop1_q5_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q5_len_msb, self.__reg_txop1_q5_len_lsb)
    @reg_txop1_q5_len.setter
    def reg_txop1_q5_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q5_len_msb, self.__reg_txop1_q5_len_lsb, value)

    @property
    def reg_txop1_q5_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q5_link_addr_msb, self.__reg_txop1_q5_link_addr_lsb)
    @reg_txop1_q5_link_addr.setter
    def reg_txop1_q5_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q5_link_addr_msb, self.__reg_txop1_q5_link_addr_lsb, value)
class MACTXOP1_Q4_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x3ac
        self.__reg_txop1_q4_len_lsb = 20
        self.__reg_txop1_q4_len_msb = 31
        self.__reg_txop1_q4_link_addr_lsb = 0
        self.__reg_txop1_q4_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop1_q4_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q4_len_msb, self.__reg_txop1_q4_len_lsb)
    @reg_txop1_q4_len.setter
    def reg_txop1_q4_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q4_len_msb, self.__reg_txop1_q4_len_lsb, value)

    @property
    def reg_txop1_q4_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q4_link_addr_msb, self.__reg_txop1_q4_link_addr_lsb)
    @reg_txop1_q4_link_addr.setter
    def reg_txop1_q4_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q4_link_addr_msb, self.__reg_txop1_q4_link_addr_lsb, value)
class MACTXOP1_Q3_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x3b0
        self.__reg_txop1_q3_len_lsb = 20
        self.__reg_txop1_q3_len_msb = 31
        self.__reg_txop1_q3_link_addr_lsb = 0
        self.__reg_txop1_q3_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop1_q3_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q3_len_msb, self.__reg_txop1_q3_len_lsb)
    @reg_txop1_q3_len.setter
    def reg_txop1_q3_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q3_len_msb, self.__reg_txop1_q3_len_lsb, value)

    @property
    def reg_txop1_q3_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q3_link_addr_msb, self.__reg_txop1_q3_link_addr_lsb)
    @reg_txop1_q3_link_addr.setter
    def reg_txop1_q3_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q3_link_addr_msb, self.__reg_txop1_q3_link_addr_lsb, value)
class MACTXOP1_Q2_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x3b4
        self.__reg_txop1_q2_len_lsb = 20
        self.__reg_txop1_q2_len_msb = 31
        self.__reg_txop1_q2_link_addr_lsb = 0
        self.__reg_txop1_q2_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop1_q2_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q2_len_msb, self.__reg_txop1_q2_len_lsb)
    @reg_txop1_q2_len.setter
    def reg_txop1_q2_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q2_len_msb, self.__reg_txop1_q2_len_lsb, value)

    @property
    def reg_txop1_q2_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q2_link_addr_msb, self.__reg_txop1_q2_link_addr_lsb)
    @reg_txop1_q2_link_addr.setter
    def reg_txop1_q2_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q2_link_addr_msb, self.__reg_txop1_q2_link_addr_lsb, value)
class MACTXOP1_Q1_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x3b8
        self.__reg_txop1_q1_len_lsb = 20
        self.__reg_txop1_q1_len_msb = 31
        self.__reg_txop1_q1_link_addr_lsb = 0
        self.__reg_txop1_q1_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop1_q1_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q1_len_msb, self.__reg_txop1_q1_len_lsb)
    @reg_txop1_q1_len.setter
    def reg_txop1_q1_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q1_len_msb, self.__reg_txop1_q1_len_lsb, value)

    @property
    def reg_txop1_q1_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop1_q1_link_addr_msb, self.__reg_txop1_q1_link_addr_lsb)
    @reg_txop1_q1_link_addr.setter
    def reg_txop1_q1_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop1_q1_link_addr_msb, self.__reg_txop1_q1_link_addr_lsb, value)
class MACTXOP2_Q15_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x3bc
        self.__reg_txop2_q15_len_lsb = 20
        self.__reg_txop2_q15_len_msb = 31
        self.__reg_txop2_q15_link_addr_lsb = 0
        self.__reg_txop2_q15_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop2_q15_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q15_len_msb, self.__reg_txop2_q15_len_lsb)
    @reg_txop2_q15_len.setter
    def reg_txop2_q15_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q15_len_msb, self.__reg_txop2_q15_len_lsb, value)

    @property
    def reg_txop2_q15_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q15_link_addr_msb, self.__reg_txop2_q15_link_addr_lsb)
    @reg_txop2_q15_link_addr.setter
    def reg_txop2_q15_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q15_link_addr_msb, self.__reg_txop2_q15_link_addr_lsb, value)
class MACTXOP2_Q14_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x3c0
        self.__reg_txop2_q14_len_lsb = 20
        self.__reg_txop2_q14_len_msb = 31
        self.__reg_txop2_q14_link_addr_lsb = 0
        self.__reg_txop2_q14_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop2_q14_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q14_len_msb, self.__reg_txop2_q14_len_lsb)
    @reg_txop2_q14_len.setter
    def reg_txop2_q14_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q14_len_msb, self.__reg_txop2_q14_len_lsb, value)

    @property
    def reg_txop2_q14_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q14_link_addr_msb, self.__reg_txop2_q14_link_addr_lsb)
    @reg_txop2_q14_link_addr.setter
    def reg_txop2_q14_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q14_link_addr_msb, self.__reg_txop2_q14_link_addr_lsb, value)
class MACTXOP2_Q13_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x3c4
        self.__reg_txop2_q13_len_lsb = 20
        self.__reg_txop2_q13_len_msb = 31
        self.__reg_txop2_q13_link_addr_lsb = 0
        self.__reg_txop2_q13_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop2_q13_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q13_len_msb, self.__reg_txop2_q13_len_lsb)
    @reg_txop2_q13_len.setter
    def reg_txop2_q13_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q13_len_msb, self.__reg_txop2_q13_len_lsb, value)

    @property
    def reg_txop2_q13_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q13_link_addr_msb, self.__reg_txop2_q13_link_addr_lsb)
    @reg_txop2_q13_link_addr.setter
    def reg_txop2_q13_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q13_link_addr_msb, self.__reg_txop2_q13_link_addr_lsb, value)
class MACTXOP2_Q12_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x3c8
        self.__reg_txop2_q12_len_lsb = 20
        self.__reg_txop2_q12_len_msb = 31
        self.__reg_txop2_q12_link_addr_lsb = 0
        self.__reg_txop2_q12_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop2_q12_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q12_len_msb, self.__reg_txop2_q12_len_lsb)
    @reg_txop2_q12_len.setter
    def reg_txop2_q12_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q12_len_msb, self.__reg_txop2_q12_len_lsb, value)

    @property
    def reg_txop2_q12_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q12_link_addr_msb, self.__reg_txop2_q12_link_addr_lsb)
    @reg_txop2_q12_link_addr.setter
    def reg_txop2_q12_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q12_link_addr_msb, self.__reg_txop2_q12_link_addr_lsb, value)
class MACTXOP2_Q11_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x3cc
        self.__reg_txop2_q11_len_lsb = 20
        self.__reg_txop2_q11_len_msb = 31
        self.__reg_txop2_q11_link_addr_lsb = 0
        self.__reg_txop2_q11_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop2_q11_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q11_len_msb, self.__reg_txop2_q11_len_lsb)
    @reg_txop2_q11_len.setter
    def reg_txop2_q11_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q11_len_msb, self.__reg_txop2_q11_len_lsb, value)

    @property
    def reg_txop2_q11_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q11_link_addr_msb, self.__reg_txop2_q11_link_addr_lsb)
    @reg_txop2_q11_link_addr.setter
    def reg_txop2_q11_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q11_link_addr_msb, self.__reg_txop2_q11_link_addr_lsb, value)
class MACTXOP2_Q10_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x3d0
        self.__reg_txop2_q10_len_lsb = 20
        self.__reg_txop2_q10_len_msb = 31
        self.__reg_txop2_q10_link_addr_lsb = 0
        self.__reg_txop2_q10_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop2_q10_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q10_len_msb, self.__reg_txop2_q10_len_lsb)
    @reg_txop2_q10_len.setter
    def reg_txop2_q10_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q10_len_msb, self.__reg_txop2_q10_len_lsb, value)

    @property
    def reg_txop2_q10_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q10_link_addr_msb, self.__reg_txop2_q10_link_addr_lsb)
    @reg_txop2_q10_link_addr.setter
    def reg_txop2_q10_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q10_link_addr_msb, self.__reg_txop2_q10_link_addr_lsb, value)
class MACTXOP2_Q9_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x3d4
        self.__reg_txop2_q9_len_lsb = 20
        self.__reg_txop2_q9_len_msb = 31
        self.__reg_txop2_q9_link_addr_lsb = 0
        self.__reg_txop2_q9_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop2_q9_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q9_len_msb, self.__reg_txop2_q9_len_lsb)
    @reg_txop2_q9_len.setter
    def reg_txop2_q9_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q9_len_msb, self.__reg_txop2_q9_len_lsb, value)

    @property
    def reg_txop2_q9_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q9_link_addr_msb, self.__reg_txop2_q9_link_addr_lsb)
    @reg_txop2_q9_link_addr.setter
    def reg_txop2_q9_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q9_link_addr_msb, self.__reg_txop2_q9_link_addr_lsb, value)
class MACTXOP2_Q8_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x3d8
        self.__reg_txop2_q8_len_lsb = 20
        self.__reg_txop2_q8_len_msb = 31
        self.__reg_txop2_q8_link_addr_lsb = 0
        self.__reg_txop2_q8_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop2_q8_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q8_len_msb, self.__reg_txop2_q8_len_lsb)
    @reg_txop2_q8_len.setter
    def reg_txop2_q8_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q8_len_msb, self.__reg_txop2_q8_len_lsb, value)

    @property
    def reg_txop2_q8_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q8_link_addr_msb, self.__reg_txop2_q8_link_addr_lsb)
    @reg_txop2_q8_link_addr.setter
    def reg_txop2_q8_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q8_link_addr_msb, self.__reg_txop2_q8_link_addr_lsb, value)
class MACTXOP2_Q7_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x3dc
        self.__reg_txop2_q7_len_lsb = 20
        self.__reg_txop2_q7_len_msb = 31
        self.__reg_txop2_q7_link_addr_lsb = 0
        self.__reg_txop2_q7_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop2_q7_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q7_len_msb, self.__reg_txop2_q7_len_lsb)
    @reg_txop2_q7_len.setter
    def reg_txop2_q7_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q7_len_msb, self.__reg_txop2_q7_len_lsb, value)

    @property
    def reg_txop2_q7_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q7_link_addr_msb, self.__reg_txop2_q7_link_addr_lsb)
    @reg_txop2_q7_link_addr.setter
    def reg_txop2_q7_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q7_link_addr_msb, self.__reg_txop2_q7_link_addr_lsb, value)
class MACTXOP2_Q6_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x3e0
        self.__reg_txop2_q6_len_lsb = 20
        self.__reg_txop2_q6_len_msb = 31
        self.__reg_txop2_q6_link_addr_lsb = 0
        self.__reg_txop2_q6_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop2_q6_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q6_len_msb, self.__reg_txop2_q6_len_lsb)
    @reg_txop2_q6_len.setter
    def reg_txop2_q6_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q6_len_msb, self.__reg_txop2_q6_len_lsb, value)

    @property
    def reg_txop2_q6_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q6_link_addr_msb, self.__reg_txop2_q6_link_addr_lsb)
    @reg_txop2_q6_link_addr.setter
    def reg_txop2_q6_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q6_link_addr_msb, self.__reg_txop2_q6_link_addr_lsb, value)
class MACTXOP2_Q5_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x3e4
        self.__reg_txop2_q5_len_lsb = 20
        self.__reg_txop2_q5_len_msb = 31
        self.__reg_txop2_q5_link_addr_lsb = 0
        self.__reg_txop2_q5_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop2_q5_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q5_len_msb, self.__reg_txop2_q5_len_lsb)
    @reg_txop2_q5_len.setter
    def reg_txop2_q5_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q5_len_msb, self.__reg_txop2_q5_len_lsb, value)

    @property
    def reg_txop2_q5_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q5_link_addr_msb, self.__reg_txop2_q5_link_addr_lsb)
    @reg_txop2_q5_link_addr.setter
    def reg_txop2_q5_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q5_link_addr_msb, self.__reg_txop2_q5_link_addr_lsb, value)
class MACTXOP2_Q4_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x3e8
        self.__reg_txop2_q4_len_lsb = 20
        self.__reg_txop2_q4_len_msb = 31
        self.__reg_txop2_q4_link_addr_lsb = 0
        self.__reg_txop2_q4_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop2_q4_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q4_len_msb, self.__reg_txop2_q4_len_lsb)
    @reg_txop2_q4_len.setter
    def reg_txop2_q4_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q4_len_msb, self.__reg_txop2_q4_len_lsb, value)

    @property
    def reg_txop2_q4_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q4_link_addr_msb, self.__reg_txop2_q4_link_addr_lsb)
    @reg_txop2_q4_link_addr.setter
    def reg_txop2_q4_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q4_link_addr_msb, self.__reg_txop2_q4_link_addr_lsb, value)
class MACTXOP2_Q3_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x3ec
        self.__reg_txop2_q3_len_lsb = 20
        self.__reg_txop2_q3_len_msb = 31
        self.__reg_txop2_q3_link_addr_lsb = 0
        self.__reg_txop2_q3_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop2_q3_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q3_len_msb, self.__reg_txop2_q3_len_lsb)
    @reg_txop2_q3_len.setter
    def reg_txop2_q3_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q3_len_msb, self.__reg_txop2_q3_len_lsb, value)

    @property
    def reg_txop2_q3_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q3_link_addr_msb, self.__reg_txop2_q3_link_addr_lsb)
    @reg_txop2_q3_link_addr.setter
    def reg_txop2_q3_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q3_link_addr_msb, self.__reg_txop2_q3_link_addr_lsb, value)
class MACTXOP2_Q2_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x3f0
        self.__reg_txop2_q2_len_lsb = 20
        self.__reg_txop2_q2_len_msb = 31
        self.__reg_txop2_q2_link_addr_lsb = 0
        self.__reg_txop2_q2_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop2_q2_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q2_len_msb, self.__reg_txop2_q2_len_lsb)
    @reg_txop2_q2_len.setter
    def reg_txop2_q2_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q2_len_msb, self.__reg_txop2_q2_len_lsb, value)

    @property
    def reg_txop2_q2_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q2_link_addr_msb, self.__reg_txop2_q2_link_addr_lsb)
    @reg_txop2_q2_link_addr.setter
    def reg_txop2_q2_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q2_link_addr_msb, self.__reg_txop2_q2_link_addr_lsb, value)
class MACTXOP2_Q1_PLCP0(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x3f4
        self.__reg_txop2_q1_len_lsb = 20
        self.__reg_txop2_q1_len_msb = 31
        self.__reg_txop2_q1_link_addr_lsb = 0
        self.__reg_txop2_q1_link_addr_msb = 19
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_txop2_q1_len(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q1_len_msb, self.__reg_txop2_q1_len_lsb)
    @reg_txop2_q1_len.setter
    def reg_txop2_q1_len(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q1_len_msb, self.__reg_txop2_q1_len_lsb, value)

    @property
    def reg_txop2_q1_link_addr(self):
        return self.__MEM.rdm(self.__addr, self.__reg_txop2_q1_link_addr_msb, self.__reg_txop2_q1_link_addr_lsb)
    @reg_txop2_q1_link_addr.setter
    def reg_txop2_q1_link_addr(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_txop2_q1_link_addr_msb, self.__reg_txop2_q1_link_addr_lsb, value)
class MACTXMEMQDATE(object):
    def __init__(self, channel, chipv = "FPGA724_M1"):
        self.chipv = chipv
        self.channel = channel
        self.__MEM = MEM(self.channel, self.chipv)
        self.__addr = MAC_TXQMEM_BASE + 0x3f8
        self.__reg_mactxmemq_date_lsb = 0
        self.__reg_mactxmemq_date_msb = 27
    @property
    def reg(self):
        return self.__MEM.rdm(self.__addr, 31, 0)
    @reg.setter
    def reg(self, value):
        return self.__MEM.wrm(self.__addr, 31, 0, value)

    @property
    def reg_mactxmemq_date(self):
        return self.__MEM.rdm(self.__addr, self.__reg_mactxmemq_date_msb, self.__reg_mactxmemq_date_lsb)
    @reg_mactxmemq_date.setter
    def reg_mactxmemq_date(self, value):
        return self.__MEM.wrm(self.__addr, self.__reg_mactxmemq_date_msb, self.__reg_mactxmemq_date_lsb, value)
    @property
    def default_value(self):
        return 0x1904291
