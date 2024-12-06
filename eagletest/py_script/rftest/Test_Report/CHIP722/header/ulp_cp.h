#include "./rtc_mem_reg.h"

#define RTC_MEM_BASE	((RTC_SLOWMEM_BASE)+0x300)
#define RTC_MEM_DATA	(RTC_SLOWMEM_BASE)
#define SAR_WR_REG	1
#define SAR_RD_REG 	2
#define SAR_WR_I2C 	3
#define SAR_WAIT   	4
#define SAR_MEAS   	5
#define SAR_WR_MEM	6
#define SAR_ALU		7
#define SAR_BRANCH	8
#define SAR_EXIT	9
#define SAR_TSENS	10
#define SAR_END		11
#define SAR_RD_MEM	13

int sar_wr_reg(int addr, int high_bit, int low_bit, int data) {
	return (SAR_WR_REG << 28) | (high_bit << 23) | (low_bit << 18)
			| (data << 10) | addr;
}
int sar_rd_reg(int addr, int high_bit, int low_bit) {
	return (SAR_RD_REG << 28) | (high_bit << 23) | (low_bit << 18) | addr;
}
int sar_wr_i2c(int wr_en, int i2c_sel, int addr, int high_bit, int low_bit,
		int data) {
	return (SAR_WR_I2C << 28) | (wr_en << 27) | (i2c_sel << 22)
			| (high_bit << 19) | (low_bit << 16) | (data << 8) | addr;
}
int wait_delay(int delay) {
	return (SAR_WAIT << 28) | delay;
}
int meas_tsens(int meas_cyc, int delay, int dreg) {
	return (SAR_TSENS << 28) | (meas_cyc << 16) | (delay << 2) | dreg;
}
int sar_meas(int xpd_hall, int hall_phase, int sar_sel, int sar_mux, int dreg) {
	return (SAR_MEAS << 28) | (xpd_hall << 9) | (hall_phase << 8) | (sar_sel << 6) | (sar_mux << 2) | dreg;
}
int sar_wr_mem_set_offset(int offset) {
	return (SAR_WR_MEM << 28) | (1 << 26) | (offset << 10);
}
int sar_wr_mem_man(int offset, int write_way, int upper, int label, int sreg, int dreg) {
	return (SAR_WR_MEM << 28) | (1 << 27) | (offset << 10) | (write_way << 7) | (upper << 6) | (label << 4) | (sreg << 2) | dreg;
}
int sar_wr_mem(int write_way, int label, int sreg, int dreg) {
	return (SAR_WR_MEM << 28) | (1 << 25) | (write_way << 7) | (label << 4) | (sreg << 2) | dreg;
}
int sar_rd_mem(int rd_upper, int mem_offset, int sreg, int dreg) {
	return (SAR_RD_MEM << 28) | (rd_upper << 27) | (mem_offset << 10) | (sreg << 2) | dreg;
}
int alu_reg(int alu, int treg, int sreg, int dreg) {
	return (SAR_ALU << 28) |(0 << 26)| (alu << 21) | (treg << 4)| (sreg << 2) | dreg;
}
int alu_im(int imm, int alu, int sreg, int dreg) {
	return (SAR_ALU << 28) |(1 << 26)|(alu << 21)| (imm << 4) | (sreg << 2) | (dreg);
}
int stage_cnt_alu(int imm, int alu) {
	return (SAR_ALU << 28) |(2 << 26) |(alu << 21)| (imm << 4);
}
int jump(int jump_type, int jump_reg, int jmp_addr, int dreg) { // force branch
	return (SAR_BRANCH << 28) | (1 << 26) | (jump_type << 22) | (jump_reg << 21) | (jmp_addr << 2) | dreg;
}
int reg0_branch(int branch, int judge, int thres) {
	return (SAR_BRANCH << 28) | (0 << 26) | (branch << 18) | (judge << 16)
			| (thres);
}
int shatge_cnt_br(int branch, int judge, int combo, int thres) {
	return (SAR_BRANCH << 28) | (2 << 26) | (branch << 18) | (judge << 16) | (combo << 15)
			| (thres);
}
int cpu_wakeup(int wake) {
	return (SAR_EXIT << 28) | (0 << 26) | wake;
}
int meas_end() {
	return (SAR_END << 28);
}

#define R0 0
#define R1 1
#define R2 2
#define R3 3

#define WRITE_CMD(cmd) WRITE_PERI_REG(RTC_MEM_BASE + (pc++ << 2), cmd)

// Instructions for co-processor
// ALU
#define MOVI(reg_des, imm) 			WRITE_CMD(alu_im(imm, 4, 0, reg_des))
#define ADDI(reg_des, reg_src, imm)		WRITE_CMD(alu_im(imm, 0, reg_src, reg_des))
#define SUBI(reg_des, reg_src, imm)		WRITE_CMD(alu_im(imm, 1, reg_src, reg_des))
#define ANDI(reg_des, reg_src, imm)		WRITE_CMD(alu_im(imm, 2, reg_src, reg_des))
#define ORI(reg_des, reg_src, imm) 		WRITE_CMD(alu_im(imm, 3, reg_src, reg_des))
#define LSHI(reg_des, reg_src, imm)		WRITE_CMD(alu_im(imm, 5, reg_src, reg_des))
#define RSHI(reg_des, reg_src, imm) 		WRITE_CMD(alu_im(imm, 6, reg_src, reg_des))

#define MOVR(des, src)				WRITE_CMD(alu_reg(4, 0, src, des))
#define ADDR(des, src, tar)			WRITE_CMD(alu_reg(0, tar, src, des))
#define SUBR(des, src, tar)			WRITE_CMD(alu_reg(1, tar, src, des))
#define ANDR(des, src, tar)			WRITE_CMD(alu_reg(2, tar, src, des))
#define ORR(des, src, tar)			WRITE_CMD(alu_reg(3, tar, src, des))
#define LSHR(des, src, tar)			WRITE_CMD(alu_reg(5, tar, src, des))
#define RSHR(des, src, tar)			WRITE_CMD(alu_reg(6, tar, src, des))

#define RSTS					WRITE_CMD(stage_cnt_alu(2, 2))
#define ADDS(imm)				WRITE_CMD(stage_cnt_alu(imm, 0))
#define SUBS(imm)				WRITE_CMD(stage_cnt_alu(imm, 1))

// BRANCH
#define BLTS(thres, step)			WRITE_CMD(shatge_cnt_br(step, 0, 1, thres))
#define BGTS(thres, step)			WRITE_CMD(shatge_cnt_br(step, 1, 1, thres))
#define BEQS(thres, step)			WRITE_CMD(shatge_cnt_br(step, 2, 0, thres))
#define BLES(thres, step)			WRITE_CMD(shatge_cnt_br(step, 2, 1, thres))
#define BGES(thres, step)			WRITE_CMD(shatge_cnt_br(step, 3, 1, thres))
#define BLR(thres, step)			WRITE_CMD(reg0_branch(step, 0, thres))
#define BGR(thres, step)			WRITE_CMD(reg0_branch(step, 1, thres))
#define BER(thres, step)			WRITE_CMD(reg0_branch(step, 2, thres))

// new jump
// int jump(int jump_type, int jump_reg, int jmp_addr, int dreg)
#define JMPI(addr)				WRITE_CMD(jump(0, 0, addr, 0))
#define JMPR(dreg)				WRITE_CMD(jump(0, 1, 0, dreg))
// jump if zero
#define JZI(addr)				WRITE_CMD(jump(1, 0, addr, 0))
#define JZR(dreg)				WRITE_CMD(jump(1, 1, 0, dreg))
// jump if overflow
#define JOI(addr)				WRITE_CMD(jump(2, 0, addr, 0))
#define JOR(dreg)				WRITE_CMD(jump(2, 1, 0, dreg))

// RD/WR MEM
#define LDW(dreg, offset)			WRITE_CMD(sar_rd_mem(0, offset, 3, dreg))
#define LDWU(offset, sreg, dreg)		WRITE_CMD(sar_rd_mem(1, offset, sreg, dreg))
#define LDWL(offset, sreg, dreg)		WRITE_CMD(sar_rd_mem(0, offset, sreg, dreg))

// ST Word/ ST word compact
#define SET_OFFSET(offset)			WRITE_CMD(sar_wr_mem_set_offset(offset))
#define STW(dreg) 					WRITE_CMD(sar_wr_mem(0, 0, 3, dreg))	
#define STC(dreg) 					WRITE_CMD(sar_wr_mem(3, 0, 3, dreg))

// ST word manually
#define STM(offset, sreg, dreg)				WRITE_CMD(sar_wr_mem_man(offset, 0, 0, 0, sreg, dreg))
#define STM32U(offset, sreg, dreg)			WRITE_CMD(sar_wr_mem_man(offset, 3, 1, 0, sreg, dreg))
#define STM32L(offset, sreg, dreg)			WRITE_CMD(sar_wr_mem_man(offset, 3, 0, 0, sreg, dreg))
#define STMLBU(offset, label, sreg, dreg)	WRITE_CMD(sar_wr_mem_man(offset, 1, 0, label, sreg, dreg))
#define STMLBL(offset, label, sreg, dreg)	WRITE_CMD(sar_wr_mem_man(offset, 1, 0, label, sreg, dreg))

// RD/WR REG
#define LDR(addr, high, low)			WRITE_CMD(sar_rd_reg((addr&0xfff)>>2, high, low))
#define STR(addr, high, low, data)		WRITE_CMD(sar_wr_reg((addr&0xfff)>>2, high, low, data))

// I2C
#define RDI2C(addr, high, low)			WRITE_CMD(sar_wr_i2c(0, 0, addr, high, low, 0))
#define WRI2C(addr, high, low, data)		WRITE_CMD(sar_wr_i2c(1, 0, addr, high, low, data))
// MEAS
#define MEAS0(dreg, sar_mux)			WRITE_CMD(sar_meas(0, 0, 0, (sar_mux+1), dreg))
#define MEAS1(dreg, sar_mux)			WRITE_CMD(sar_meas(0, 0, 1, (sar_mux+1), dreg))
#define HALLP(dreg, phase)			WRITE_CMD(sar_meas(1, phase, 0, 1, dreg))
#define HALLN(dreg, phase)	 		WRITE_CMD(sar_meas(1, phase, 0, 4, dreg))

// DELAY
#define DELAY(cycle)				WRITE_CMD(wait_delay(cycle))

// wake up & sleep cycle
#define WAKEUP					WRITE_CMD(cpu_wakeup(1))

// TSENS
#define TSENS(dreg, delay)			WRITE_CMD(meas_tsens(0, delay, dreg))


// END
#define END					WRITE_CMD(meas_end())
