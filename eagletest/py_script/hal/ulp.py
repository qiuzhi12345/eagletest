# -- coding: utf-8 --
class ULP(object):
    def __init__(self, channel, chipv = "ESP32"):
        self.chipv = chipv
        self.channel = channel

    def init(self):
        '''
        :brief:
            init ulp
        :param:
            no param
        :return:
            no return
        '''
        return self.channel.req_com("ulp_init")

    def start(self, mode):
        '''
        :brief:
            start ulp
        :param:
            mode: non 0 means ulp start by ulp timer;
                - 0: Top mode;
                - 1: set register(ulp_slp_timer_en) to trig ulp timer;
                - 2: rtc_gpio connected to high or low or other mode to trig ulp timer(begin from CHIP722)
        :return:
            no return
        '''
        return self.channel.req_com("ulp_start %d"%(mode))
    
    def movi(self, Rdst, imm_value):
        '''
        :brief:
            move imm_value to Rdst
        :param:
            - rdst: it can be R0, R1, R2, R3;
            - imm_value: immediate value
        :return:
            no return
        '''
        return self.channel.req_com("MOVI %d %d"%(Rdst, imm_value))
    
    def addi(self, Rdst, Rsrc, imm_value):
        '''
        :brief:
            value in Rsrc add imm_value, then restore in Rdst
        :param:
            - Rdst: destination register, it can be R0, R1, R2, R3;
            - Rsrc: original register, it can be RO, R1, R2, R3;
            - imm_value: immediate value
        :return:
            no return
        '''
        return self.channel.req_com("ADDI %d %d %d"%(Rdst, Rsrc, imm_value))

    def subi(self, Rdst, Rsrc, imm_value):
        '''
        :brief:
            value in Rsrc subtract imm_value, then restore in Rdst
        :param:
            - Rdst: destination register, it can be R0, R1, R2, R3;
            - Rsrc: original register, it can be RO, R1, R2, R3;
            - imm_value: immediate value
        :return: - no return
        '''
        return self.channel.req_com("SUBI %d %d %d"%(Rdst, Rsrc, imm_value))

    def andi(self, Rdst, Rsrc, imm_value):
        '''
        :brief:
            value in Rsrc logical and imm_value, then restore in Rdst
        :param:
            - Rdst: destination register, it can be R0, R1, R2, R3;
            - Rsrc: original register, it can be RO, R1, R2, R3;
            - imm_value: immediate value
        :return:
            no return
        '''
        return self.channel.req_com("ANDI %d %d %d"%(Rdst, Rsrc, imm_value))

    def ori(self, Rdst, Rsrc, imm_value):
        '''
        :brief:
            value in Rsrc logical or imm_value, then restore in Rdst
        :param:
            - Rdst: destination register, it can be R0, R1, R2, R3;
            - Rsrc: original register, it can be RO, R1, R2, R3;
            - imm_value: immediate value
        :return:
            no return
        '''
        return self.channel.req_com("ORI %d %d %d"%(Rdst, Rsrc, imm_value))

    def lshi(self, Rdst, Rsrc, imm_value):
        '''
        :brief:
            value in Rsrc logical move left for imm_value bits, then restore in Rdst
        :param:
            - Rdst: destination register, it can be R0, R1, R2, R3;
            - Rsrc: original register, it can be RO, R1, R2, R3;
            - imm_value: immediate value
        :return:
            no return
        '''
        return self.channel.req_com("LSHI %d %d %d"%(Rdst, Rsrc, imm_value))

    def rshi(self, Rdst, Rsrc, imm_value):
        '''
        :brief:
            value in Rsrc logical move to right imm_value, then restore in Rdst
        :param:
            - Rdst: destination register, it can be R0, R1, R2, R3;
            - Rsrc: original register, it can be RO, R1, R2, R3;
            - imm_value: immediate value
        :return:
            no return
        '''
        return self.channel.req_com("RSHI %d %d %d"%(Rdst, Rsrc, imm_value))

    def movr(self, Rdst, Rsrc):
        '''
        :brief:
            move value in Rsrc to Rdst
        :param:
            - Rdst: destination register, it can be R0, R1, R2, R3;
            - Rsrc: original register, it can be RO, R1, R2, R3;
        :return:
            no return
        '''
        return self.channel.req_com("MOVR %d %d"%(Rdst, Rsrc))

    def addr(self, Rdst, Rsrc, Rtar):
        '''
        :brief:
            value in Rsrc add value in Rtar, then restore in Rdst
        :param:
            - Rdst: destination register, it can be R0, R1, R2, R3;
            - Rsrc: original register, it can be RO, R1, R2, R3;
            - Rtar: it can be RO, R1, R2, R3, whose value will be added to Rsrc ;
        :return:
            no return
        '''
        return self.channel.req_com("ADDR %d %d %d"%(Rdst, Rsrc, Rtar))

    def subr(self, Rdst, Rsrc, Rtar):
        '''
        :brief:
            value in Rsrc subtract value in Rtar, then restore in Rdst
        :param:
            - Rdst: destination register, it canimm_value be R0, R1, R2, R3;
            - Rsrc: original register, it can be RO, R1, R2, R3;
            - Rtar: it can be RO, R1, R2, R3, whose value will be subtracted to Rsrc ;
        :return:
            no return
        '''
        return self.channel.req_com("SUBR %d %d %d"%(Rdst, Rsrc, Rtar))

    def andr(self, Rdst, Rsrc, Rtar):
        '''
        :brief:
            value in Rsrc and value in Rtar, then restore in Rdst
        :param:
            - Rdst: destination register, it can be R0, R1, R2, R3;
            - Rsrc: original register, it can be RO, R1, R2, R3;
            - Rtar: it can be RO, R1, R2, R3, whose value will and with Rsrc ;
        :return:
            no return
        '''
        return self.channel.req_com("ANDR %d %d %d"%(Rdst, Rsrc, Rtar))

    def orr(self, Rdst, Rsrc, Rtar):
        '''
        :brief:
            value in Rsrc or value in Rtar, then restore in Rdst
        :param:
            - Rdst: destination register, it can be R0, R1, R2, R3;
            - Rsrc: original register, it can be RO, R1, R2, R3;
            - Rtar: it can be RO, R1, R2, R3, whose value will or with Rsrc ;
        :return:
            no return
        '''
        return self.channel.req_com("ORR %d %d %d"%(Rdst, Rsrc, Rtar))

    def lshr(self, Rdst, Rsrc, Rtar):
        '''
        :brief:
            value in Rsrc logical move left for value in Rtar bits, then restore in Rdst
        :param:
            - Rdst: destination register, it can be R0, R1, R2, R3;
            - Rsrc: original register, it can be RO, R1, R2, R3;
            - Rtar: it can be RO, R1, R2, R3 ;
        :return:
            no return
        '''
        return self.channel.req_com("LSHR %d %d %d"%(Rdst, Rsrc, Rtar))

    def rshr(self, Rdst, Rsrc, Rtar):
        '''
        :brief:
            value in Rsrc logical move right for value in Rtar bits, then restore in Rdst
        :param:
            - Rdst: destination register, it can be R0, R1, R2, R3;
            - Rsrc: original register, it can be RO, R1, R2, R3;
            - Rtar: it can be RO, R1, R2, R3 ;
        :return:
            no return
        '''
        return self.channel.req_com("RSHR %d %d %d"%(Rdst, Rsrc, Rtar))

    def rsts(self):
        '''
        :brief:
            reset stage count register
        :param:
            no param
        :return:
            no return
        '''
        return self.channel.req_com("RSTS")

    def adds(self, imm_value):
        '''
        :brief:
            increase stage count register for imm_value
        :param:
            imm_value: value will be added to stage count register
        :return:
            no return
        '''
        return self.channel.req_com("ADDS %d"%(imm_value))

    def subs(self, imm_value):
        '''
        :brief:
            decrease stage count register for imm_value
        :param:
            imm_value: value will be subtract by stage count register
        :return:
            no return
        '''
        return self.channel.req_com("SUBS %d"%(imm_value))

    def bls(self, thres, step):
        '''
        :brief:
            - if value in stage count register is lower than thres, jump step[6:0] steps forward or backward which depends step[7];
            - if step[7] is 1, backward jump, otherwise forward jump.
        :param:
            - thres: which stage count register compare to;
            - step: pc jump counts.
        :return:
            no return
        '''
        return self.channel.req_com("BLS %d %d"%(thres, step))

    def bes(self, thres, step):
        '''
        :brief:
            - if value in stage count register is equal with thres, jump step[6:0] steps forward or backward which depends step[7];
            - if step[7] is 1, backward jump, otherwise forward jump.
        :param:
            - thres: which stage count register compare to;
            - step: pc jump counts.
        :return:
            no return
        '''
        return self.channel.req_com("BES %d %d"%(thres, step))

    def bhs(self, thres, step):
        '''
        :brief:
            - if value in stage count register is higher than thres, jump step[6:0] steps forward or backward which depends step[7];
            - if step[7] is 1, backward jump, otherwise forward jump.
        :param:
            - thres: which stage count register compare to;
            - step: pc jump counts.
        :return:
            no return
        '''
        return self.channel.req_com("BHS %d %d"%(thres, step))

    def bles(self, thres, step):
        '''
        :brief:
            - if value in stage count register is lower than thres or equal to thres, jump step[6:0] steps forward or backward which depends step[7];
            - if step[7] is 1, backward jump, otherwise forward jump.
            - add from CHIP722.
        :param:
            - thres: which stage count register compare to;
            - step: pc jump counts.
        :return:
            no return
        '''
        return self.channel.req_com("BLES %d %d"%(thres, step))

    def bhes(self, thres, step):
        '''
        :brief:
            - if value in stage count register is higher than thres or equal to thres, jump step[6:0] steps forward or backward which depends step[7];
            - if step[7] is 1, backward jump, otherwise forward jump, add from CHIP722.
        :param:
            - thres: which stage count register compare to;
            - step: pc jump counts.
        :return:
            no return
        '''
        return self.channel.req_com("BHES %d %d"%(thres, step))

    def jmpi(self, ImmAddr):
        '''
        :brief:
            jump to the address contained in ImmAddr
        :param:
            ImmAddr: address to jump
        :return:
            no return
        '''
        return self.channel.req_com("JMPI %d"%(ImmAddr))

    def jmpr(self, Rdst):
        '''
        :brief:
            jump to the address contained in Rdst
        :param:
            Rdst: register containing address
        :return:
            no return
        '''
        return self.channel.req_com("JMPR %d"%(Rdst))

    def jzi(self, ImmAddr):
        '''
        :brief:
            jump to the address contained in ImmAddr only if the last ALU operation has set the zero flag
        :param:
            ImmAddr: address to jump
        :return:
            no return
        '''
        return self.channel.req_com("JZI %d"%(ImmAddr))

    def jzr(self, Rdst):
        '''
        :brief:
            jump to the address contained in Rdst only if the last ALU operation has set the zero flag
        :param:
            Rdst: address to jump
        :return:
            no return
        '''
        return self.channel.req_com("JZR %d"%(Rdst))

    def joi(self, ImmAddr):
        '''
        :brief:
            jump to the address contained in ImmAddr only if the last ALU operation has set the overflow flag
        :param:
            ImmAddr: address to jump
        :return:
            no return
        '''
        return self.channel.req_com("JOI %d"%(ImmAddr))

    def jor(self, Rdst):
        '''
        :brief:
            jump to the address contained in Rdst only if the last ALU operation has set the overflow flag
        :param:
            Rdst: address to jump
        :return:
            no return
        '''
        return self.channel.req_com("JOR %d"%(Rdst))

    def stm(self, Rsrc, Rdst, offset):
        '''
        :brief:
            - store the 16-bit value to Rsrc in the lower half-word of memory with address Rdst+Offset;
            - Mem[Rdst + Offset]{31:0} = {PC[10:0], 5’b0, Rsrc[15:0]}.
        :param:
            - Rsrc: Register R[0-3], 16-bit value to store;
            - Rdst: Register R[0-3], address of the destination, expressed in 31-bit words;
            - offset: 10-bit signed value, offset expressed in 32-bit words.
        :return:
            no return
        '''
        return self.channel.req_com("STM %d %d %d"%(Rsrc, Rdst, offset))

    def ldm(self, Rdst, Rsrc, offset):
        '''
        :brief:
            read value from memory to register, Rdst[15:0] = Mem[Rsrc+Offset][15:0]
        :param:
            - Rdst: Register R[0-3], address of destination memory, expressed in 32-bit words;
            - Rsrc: Register R[0-3];
            - offset: 10-bit signed value, offset expressed in 32-bit words.
        :return:
            no return
        '''
        return self.channel.req_com("LDM %d %d %d"%(Rdst, Rsrc, offset))

    def ldmu(self, Rdst, Rsrc, offset):
        '''
        :brief:
            read value from memory to register, Rdst[15:0] = Mem[Rsrc+Offset][31:16], add from CHIP722
        :param:
            - Rdst: Register R[0-3], address of destination memory, expressed in 32-bit words;
            - Rsrc: Register R[0-3];
            - offset: 10-bit signed value, offset expressed in 32-bit words.
        :return:
            no return
        '''
        return self.channel.req_com("LDMU %d %d %d"%(Rdst, Rsrc, offset))

    def ldr(self, addr, high, low):
        '''
        :brief:
            store REG[addr][high:low] to R0
        :param:
            - addr: register address;
            - high: high bit;
            - low: low bit;
        :return:
            no return
        '''
        return self.channel.req_com("LDR %d %d %d"%(addr, high, low))

    def blr(self, thres, step):
        '''
        :brief:
            - if value in R0 is lower than thres, jump step[6:0] steps forward or backward which depends step[7].
            - if step[7] is 1, backward jump, otherwise forward jump.
        :param: thres: which R0 compare to;
               step: pc jump counts.
        :return: - no return
        '''
        return self.channel.req_com("BLR %d %d"%(thres, step))

    def bhr(self, thres, step):
        '''
        :brief:
            - in other chips except CHIP722, if value in R0 is higher than thres or equal to thres, jump step[6:0] steps forward or backward which depends step[7].
            - in CHIP722: if value in R0 is higher than thres, jump step[6:0] steps forward or backward which depends step[7].
            - if step[7] is 1, backward jump, otherwise forward jump.
        :param:
            - thres: which R0 compare to;
            - step: pc jump counts.
        :return:
            no return
        '''
        return self.channel.req_com("BHR %d %d"%(thres, step))

    def ber(self, thres, step):
        '''
        :brief:
            - if value in R0 is equal to thres, jump step[6:0] steps forward or backward which depends step[7].
            - if step[7] is 1, backward jump, otherwise forward jump.
            - add from CHIP722
        :param:
            - thres: which R0 compare to;
            - step: pc jump counts.
        :return:
            no return
        '''
        return self.channel.req_com("BER %d %d"%(thres, step))

    def str(self, addr, high, low, data):
        '''
        :brief:
            write data to REG[addr][high:low]
        :param:
            - addr: register address;
            - high: high bit;
            - low: low bit;
            - data: data value to write to
        :return:
            no return
        '''
        return self.channel.req_com("STR %d %d %d %d"%(addr, high, low, data))

    def wakeup(self):
        '''
        :brief:
            ulp wakeup cpu from deep sleep
        :param:
            no param;
        :return:
            no return
        '''
        return self.channel.req_com("ulp_wakeup")

    def delay(self, delay_cycle):
        '''
        :brief:
            ulp delay
        :param:
            delay_delay: delay cycle;
        :return:
            no return
        '''
        return self.channel.req_com("ulp_delay %d"%(delay_cycle))

    def meas_adc0(self, reg, channel):
        '''
        :brief:
            measure adc0
        :param:
            - reg: register to store adc data
            - channel: which to measure
        :return:
            no return
        '''
        return self.channel.req_com("meas_adc0 %d %d"%(reg, channel))

    def meas_adc1(self, reg, channel):
        '''
        :brief:
            measure adc1
        :param:
            - reg: register to store adc data
            - channel: which to measure
        :return:
            no return
        '''
        return self.channel.req_com("meas_adc1 %d %d"%(reg, channel))

    def tsens(self, reg, wait_cycle):
        '''
        :brief:
            measure temperature
        :param:
            - reg: register to store tmp value
            - wait_cycle: cycles between two tmp samples.
        :return:
            no return
        '''
        return self.channel.req_com("TSENS %d %d"%(reg, wait_cycle))

    def end(self):
        '''Rdst, Rsrc
        :brief:
            end ulp
        :param:
            no param
        :return:
            no return
        '''
        return self.channel.req_com("ulp_end")

    def sleep(self, wakeup_reg = 0):
        '''
        :brief:
            select register which restore sleep time, default select register 0.
        :param:
            wakeup_reg: can set [0~4], register which stored sleep cycle;
        :return:
            no return
        '''
        return self.channel.req_com("SLEEP %d"%(wakeup_reg))

    def set_ulp_slp_time(self, cycle):
        '''
        :brief:
            set sleep cycle
        :param:
            cycle: sleep cycle, 32 bit;
        :return:
            no return
        '''
        return self.channel.req_com("set_reg0_cycle %d"%(cycle))

    def set_offset(self, offset):
        '''
        :brief:
            - 设置起始地址偏移，与stw和stc一起使用, add from CHIP722.
        :param:
            - offset: STW、STC的基地址偏移, 11bits
        :return:
            no return
        '''
        return self.channel.req_com("SET_OFFSET %d"%(offset))

    def stw(self, Rsrc, Rdst):
        '''
        :brief:
            - WORD操作指令，地址偏移+1;
            - Mem[Rsrc1 + cur_offset]{31:0} = {PC[10:0], 5’d0,Rdst[15:0]};
            - cur_offset = cur_offset + 1
            - add from CHIP722.
        :param:
            - Rsrc: original register, it can be RO, R1, R2, R3;
            - Rdst: destination register, it can be R0, R1, R2, R3;
        :return:
            no return
        '''
        return self.channel.req_com("STW %d %d"%(Rsrc, Rdst))

    def stc(self, Rsrc, Rdst):
        '''
        :brief:
            - STC为半字操作(第一次写当前地址的低16bit，第二次写当前地址的高16bit)，每执行两次，地址偏移+1。注意：使用STC时，必须写完一个字，即一次burst操作的指令必须是偶数个;先写低16bit，再写高16bit.
            - Mem [ Rsrc1 + cur_offset ]{15:0} = {Rdst[15:0]}  (STC1）;
            - Mem [ Rsrc1 + cur_offset ]{31:16} = {Rdst[15:0]}（STC2）;
            - cur_offset = cur_offset + 1
            - add from CHIP722.
        :param:
            - Rsrc: original register, it can be RO, R1, R2, R3;
            - Rdst: destination register, it can be R0, R1, R2, R3;
        :return:
            no return
        '''
        return self.channel.req_com("STC %d %d"%(Rsrc, Rdst))

    def stm32u(self, Rsrc, Rdst, offset):
        '''
        :brief:
            store the 16-bit value to Rsrc in the higher half-word of memory with address Rdst+Offset;
            - Mem[Rdst + Offset][31:16] = Rsrc[15:0]
            - add from CHIP722.
        :param:
            - Rsrc: Register R[0-3], 16-bit value to store;
            - Rdst: Register R[0-3], address of the destination, expressed in 31-bit words;
            - offset: 11-bit signed value, offset expressed in 32-bit words.
        :return:
            no return
        '''
        return self.channel.req_com("STM32U %d %d %d"%(Rsrc, Rdst, offset))

    def stm32l(self, Rsrc, Rdst, offset):
        '''
        :brief:
            store the 16-bit value to Rsrc in the lower half-word of memory with address Rdst+Offset;
            - Mem[Rdst + Offset][15:0] = Rsrc[15:0];
            - add from CHIP722.
        :param:
            - Rsrc: Register R[0-3], 16-bit value to store;
            - Rdst: Register R[0-3], address of the destination, expressed in 31-bit words;
            - offset: 11-bit signed value, offset expressed in 32-bit words.
        :return:
            no return
        '''
        return self.channel.req_com("STM32L %d %d %d"%(Rsrc, Rdst, offset))

    def stmlbu(self, data_label, Rsrc, Rdst, offset):
        '''
        :brief:
            - Mem[Rdst + offset]{31:16} = {data_label[1:0]，Rsrc[13:0]}
            - add from CHIP722.
        :param:
            - data_label: 2bits, store value
            - Rsrc: Register R[0-3], 16-bit value to store;
            - Rdst: Register R[0-3], address of the destination, expressed in 31-bit words;
            - offset: 11-bit signed value, offset expressed in 32-bit words.
        :return:
            no return
        '''
        return self.channel.req_com("STMLBU %d %d %d %d"%(data_label, Rsrc, Rdst, offset))

    def stmlbl(self, data_label, Rsrc, Rdst, offset):
        '''
        :brief:
            - Mem[Rdst + offset]{15:0} = {data_label[1:0]，Rsrc[13:0]}
            - add from CHIP722.
        :param:
            - data_label: 2bits, store value
            - Rsrc: Register R[0-3], 16-bit value to store;
            - Rdst: Register R[0-3], address of the destination, expressed in 31-bit words;
            - offset: 11-bit signed value, offset expressed in 32-bit words.
        :return:
            no return
        '''
        return self.channel.req_com("STMLBL %d %d %d %d"%(data_label, Rsrc, Rdst, offset))
