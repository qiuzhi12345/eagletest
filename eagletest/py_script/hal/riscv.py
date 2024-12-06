from hal.common import MEM

class RISCV(object):
    def __init__(self,channel,chipv="AUTO"):
        self.channel = channel
        self.chipv = chipv
        self.mem_wr = MEM(self.channel,self.chipv)
        self.riscv_mem_base = 0x50000000
        
    def mem_load(self):
        with open("./dist/pxp/riscv_code.dat","r") as code_file:
            riscv_content = code_file.read()
            line_list = riscv_content.split("\n")
        row_count = 0
        for line in line_list:
            if(row_count < 2048):
                self.mem_wr.wr(self.riscv_mem_base + (row_count << 2), int('0b'+line, 2))
                row_count += 1
                #print line
            else:
                print "ERROR!!! Code_Size > 8k\n"
