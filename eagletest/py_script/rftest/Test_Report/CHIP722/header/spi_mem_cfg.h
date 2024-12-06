#include "./gpio_reg.h"
#include "./io_mux_reg.h"

#define REG_BIT_READ(addr,s)    ( *(volatile unsigned int *)(addr) >> (s) )
#define APB_IO_MUX_ADDR_PRE     ( REG_IO_MUX_BASE )
//#define LINE1
//#define CLK80
#define READ 1 
#define WREN 2 
#define WRDI 3 
#define RDID 4 
#define RDSR 5 
#define WRSR 6 
#define PP   7 
#define SE   8 
#define BE   9 
#define CE   10 
#define DP   11 
#define RES  12 
#define HPM  13 
#define USR  14 
void WaitFlashPEDone(unsigned int spi_no);
unsigned int sim_spi_rdst_0(unsigned int spi_no);
unsigned int sim_spi_rdst_1(unsigned int spi_no);

void SpiMEMStart(unsigned int spi_no,unsigned mode)
{
    unsigned int sus, busy;
    switch(mode){
        case READ: WRITE_PERI_REG(SPI_MEM_CMD_REG(spi_no),SPI_MEM_FLASH_READ); break;
        case WREN: WRITE_PERI_REG(SPI_MEM_CMD_REG(spi_no),SPI_MEM_FLASH_WREN); break;
        case WRDI: WRITE_PERI_REG(SPI_MEM_CMD_REG(spi_no),SPI_MEM_FLASH_WRDI); break;
        case RDID: WRITE_PERI_REG(SPI_MEM_CMD_REG(spi_no),SPI_MEM_FLASH_RDID); break;
        case RDSR: WRITE_PERI_REG(SPI_MEM_CMD_REG(spi_no),SPI_MEM_FLASH_RDSR); break;
        case WRSR: WRITE_PERI_REG(SPI_MEM_CMD_REG(spi_no),SPI_MEM_FLASH_WRSR); break;
        case PP  : WRITE_PERI_REG(SPI_MEM_CMD_REG(spi_no),SPI_MEM_FLASH_PP  ); break;
        case SE  : WRITE_PERI_REG(SPI_MEM_CMD_REG(spi_no),SPI_MEM_FLASH_SE  ); break;
        case BE  : WRITE_PERI_REG(SPI_MEM_CMD_REG(spi_no),SPI_MEM_FLASH_BE  ); break;
        case CE  : WRITE_PERI_REG(SPI_MEM_CMD_REG(spi_no),SPI_MEM_FLASH_CE  ); break;
        case DP  : WRITE_PERI_REG(SPI_MEM_CMD_REG(spi_no),SPI_MEM_FLASH_DP  ); break;
        case RES : WRITE_PERI_REG(SPI_MEM_CMD_REG(spi_no),SPI_MEM_FLASH_RES ); break;
        case HPM : WRITE_PERI_REG(SPI_MEM_CMD_REG(spi_no),SPI_MEM_FLASH_HPM ); break;
        case USR : WRITE_PERI_REG(SPI_MEM_CMD_REG(spi_no),SPI_MEM_USR       ); break;
        default: fail(0);break;
    }
    while((READ_PERI_REG(SPI_MEM_CMD_REG(spi_no))!=0) || 
          (READ_PERI_REG(SPI_MEM_SUS_STATUS_REG(spi_no))!=0)) {
	WaitFlashPEDone(spi_no); //atom operation
    }
}

void spi_flash_wren(unsigned int spi_no)
{
    SpiMEMStart(spi_no,WREN);
    int sta_0 = sim_spi_rdst_0(spi_no);
    if(sta_0&0x2 !=0x2 ) fail("FAIL\n");
}

void spi_flash_be(unsigned int spi_no ,unsigned int addr)
{
//    WaitFlashPEDone(spi_no);
    spi_flash_wren(spi_no);
    SET_PERI_REG_BITS( SPI_MEM_ADDR_REG(spi_no),0xffffffff,addr,0);// usr_addr_value
    SpiMEMStart(spi_no,BE);
}

void spi_flash_se(unsigned int spi_no,unsigned int addr)
{
//    WaitFlashPEDone(spi_no);
    spi_flash_wren(spi_no);
    SET_PERI_REG_BITS(SPI_MEM_FLASH_WAITI_CTRL_REG(1),0x1,0x1,SPI_MEM_WAITI_EN_S); // enable hardware wait flash idle. 
    SET_PERI_REG_BITS(SPI_MEM_ADDR_REG(spi_no),0xffffffff,addr,0); // usr_addr_value
    SpiMEMStart(spi_no,SE);
}

void spi_flash_per(unsigned int spi_no)
{
    WRITE_PERI_REG(SPI_MEM_FLASH_SUS_CMD_REG(spi_no),SPI_MEM_FLASH_PER);
    while(READ_PERI_REG(SPI_MEM_FLASH_SUS_CMD_REG(spi_no)));
}

void spi_flash_wrdi(unsigned int spi_no)
{
    SpiMEMStart(spi_no,WRDI);
}

unsigned int sim_spi_rdst_0(unsigned int spi_no) {
    unsigned int val = 0;
    
    WRITE_PERI_REG(SPI_MEM_CMD_REG(spi_no),SPI_MEM_FLASH_RDSR);
    while(READ_PERI_REG(SPI_MEM_CMD_REG(spi_no)));

    val = GET_PERI_REG_BITS(SPI_MEM_RD_STATUS_REG(spi_no),SPI_MEM_STATUS,SPI_MEM_STATUS_S);
    return val;
}
unsigned int sim_spi_rdst_1(unsigned int spi_no) {
    unsigned int val = 0;
    unsigned int reg_bak1;
    unsigned int reg_bak2;
    unsigned int reg_bak3;
    unsigned int reg_bak4;
    unsigned int reg_bak5;
    reg_bak1 = READ_PERI_REG(SPI_MEM_W0_REG(spi_no));
    reg_bak2 = READ_PERI_REG(SPI_MEM_USER_REG(spi_no));
    reg_bak3 = READ_PERI_REG(SPI_MEM_USER2_REG(spi_no));
    reg_bak4 = READ_PERI_REG(SPI_MEM_MISO_DLEN_REG(spi_no));
    reg_bak5 = READ_PERI_REG(SPI_MEM_CTRL_REG(spi_no));

    WRITE_PERI_REG(SPI_MEM_CTRL_REG(spi_no),0);
    WRITE_PERI_REG(SPI_MEM_USER_REG(spi_no),0);
    WRITE_PERI_REG(SPI_MEM_W0_REG(spi_no),0);
    
    SET_PERI_REG_MASK(SPI_MEM_CTRL_REG(spi_no),SPI_MEM_WP_REG|SPI_MEM_D_POL|SPI_MEM_Q_POL);
/*******************************************/
    SET_PERI_REG_MASK(SPI_MEM_USER_REG(spi_no),SPI_MEM_USR_COMMAND|SPI_MEM_USR_MISO|SPI_MEM_CS_SETUP);//////////////////////////////
    WRITE_PERI_REG(SPI_MEM_MISO_DLEN_REG(spi_no),0x7);
    SET_PERI_REG_BITS(SPI_MEM_USER2_REG(spi_no),SPI_MEM_USR_COMMAND_BITLEN,0x7,SPI_MEM_USR_COMMAND_BITLEN_S); 
    SET_PERI_REG_BITS(SPI_MEM_USER2_REG(spi_no),SPI_MEM_USR_COMMAND_VALUE,0x35,SPI_MEM_USR_COMMAND_VALUE_S); 

    WRITE_PERI_REG(SPI_MEM_CMD_REG(spi_no),SPI_MEM_USR);
    while(READ_PERI_REG(SPI_MEM_CMD_REG(spi_no)));

    val = GET_PERI_REG_BITS(SPI_MEM_W0_REG(spi_no),SPI_MEM_BUF0,SPI_MEM_BUF0_S);

    WRITE_PERI_REG(SPI_MEM_W0_REG(spi_no),reg_bak1);
    WRITE_PERI_REG(SPI_MEM_USER_REG(spi_no),reg_bak2);
    WRITE_PERI_REG(SPI_MEM_USER2_REG(spi_no),reg_bak3);
    WRITE_PERI_REG(SPI_MEM_MISO_DLEN_REG(spi_no),reg_bak4);
    WRITE_PERI_REG(SPI_MEM_CTRL_REG(spi_no),reg_bak5);
    return val;
}

void sim_spi_wrst_qe(unsigned int spi_no) {
    unsigned int sta_0 = 0;
    unsigned int sta_1 = 0;
    unsigned int sta   = 0;
    unsigned int reg_bak1;
    unsigned int reg_bak2;
    unsigned int reg_bak3;
    unsigned int reg_bak4;
    unsigned int reg_bak5;

//  WaitFlashPEDone(spi_no);
    spi_flash_wren(spi_no);

    reg_bak1 = READ_PERI_REG(SPI_MEM_W0_REG(spi_no));
    reg_bak2 = READ_PERI_REG(SPI_MEM_USER_REG(spi_no));
    reg_bak3 = READ_PERI_REG(SPI_MEM_USER2_REG(spi_no));
    reg_bak4 = READ_PERI_REG(SPI_MEM_MISO_DLEN_REG(spi_no));
    reg_bak5 = READ_PERI_REG(SPI_MEM_CTRL_REG(spi_no));

    WRITE_PERI_REG(SPI_MEM_CTRL_REG(spi_no),0);
    WRITE_PERI_REG(SPI_MEM_USER_REG(spi_no),0);

    SET_PERI_REG_MASK(SPI_MEM_CTRL_REG(spi_no),SPI_MEM_WP_REG|SPI_MEM_D_POL|SPI_MEM_Q_POL);
/*******************************************/
    SET_PERI_REG_MASK(SPI_MEM_USER_REG(spi_no),SPI_MEM_USR_MISO|SPI_MEM_CS_SETUP);//////////////////////////////
    SET_PERI_REG_BITS(SPI_MEM_MISO_DLEN_REG(spi_no),SPI_MEM_USR_MISO_DBITLEN,0x7,SPI_MEM_USR_MISO_DBITLEN_S);       // usr_din_bitlen
    sta_0 = sim_spi_rdst_0(spi_no);
    sta_1 = sim_spi_rdst_1(spi_no);
    sta = sta_0 | ((sta_1 | 0x2) <<8);  
    SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(spi_no),0x1,0x1,SPI_MEM_WRSR_2B_S);      // wrsr_2b 
    SET_PERI_REG_BITS(SPI_MEM_RD_STATUS_REG(spi_no),0xFFFFFFFF,sta,SPI_MEM_STATUS_S);       //sta

    SpiMEMStart(spi_no,WRSR);
    sim_spi_wait_flash_idle(spi_no);
    WRITE_PERI_REG(SPI_MEM_W0_REG(spi_no),reg_bak1);
    WRITE_PERI_REG(SPI_MEM_USER_REG(spi_no),reg_bak2);
    WRITE_PERI_REG(SPI_MEM_USER2_REG(spi_no),reg_bak3);
    WRITE_PERI_REG(SPI_MEM_MISO_DLEN_REG(spi_no),reg_bak4);
    WRITE_PERI_REG(SPI_MEM_CTRL_REG(spi_no),reg_bak5);
}

void sim_spi_wrst_qe1(unsigned int spi_no) {
    unsigned int sta   = 0;
    unsigned int reg_bak1;
    unsigned int reg_bak2;
    unsigned int reg_bak3;
    unsigned int reg_bak4;
    unsigned int reg_bak5;

//    WaitFlashPEDone(spi_no);
    spi_flash_wren(spi_no);

    reg_bak1 = READ_PERI_REG(SPI_MEM_W0_REG(spi_no));
    reg_bak2 = READ_PERI_REG(SPI_MEM_USER_REG(spi_no));
    reg_bak3 = READ_PERI_REG(SPI_MEM_USER2_REG(spi_no));
    reg_bak4 = READ_PERI_REG(SPI_MEM_MISO_DLEN_REG(spi_no));
    reg_bak5 = READ_PERI_REG(SPI_MEM_CTRL_REG(spi_no));

    WRITE_PERI_REG(SPI_MEM_CTRL_REG(spi_no),0);
    WRITE_PERI_REG(SPI_MEM_USER_REG(spi_no),0);

    SET_PERI_REG_MASK(SPI_MEM_CTRL_REG(spi_no),SPI_MEM_WP_REG|SPI_MEM_D_POL|SPI_MEM_Q_POL);
/*******************************************/
    sta = sim_spi_rdst_1(spi_no);
    sta = (sta | 0x2);  
//////////////////////////////////////////
    WRITE_PERI_REG(SPI_MEM_W0_REG(spi_no),sta);
    SET_PERI_REG_MASK(SPI_MEM_USER_REG(spi_no),SPI_MEM_USR_COMMAND|SPI_MEM_USR_MOSI|SPI_MEM_CS_SETUP);//////////////////////////////
    WRITE_PERI_REG(SPI_MEM_MOSI_DLEN_REG(spi_no),0x7);
    SET_PERI_REG_BITS(SPI_MEM_USER2_REG(spi_no),SPI_MEM_USR_COMMAND_BITLEN,0x7,SPI_MEM_USR_COMMAND_BITLEN_S); 
    SET_PERI_REG_BITS(SPI_MEM_USER2_REG(spi_no),SPI_MEM_USR_COMMAND_VALUE,0x31,SPI_MEM_USR_COMMAND_VALUE_S); 

    WRITE_PERI_REG(SPI_MEM_CMD_REG(spi_no),SPI_MEM_USR);
    while(READ_PERI_REG(SPI_MEM_CMD_REG(spi_no)));

    WRITE_PERI_REG(SPI_MEM_W0_REG(spi_no),reg_bak1);
    WRITE_PERI_REG(SPI_MEM_USER_REG(spi_no),reg_bak2);
    WRITE_PERI_REG(SPI_MEM_USER2_REG(spi_no),reg_bak3);
    WRITE_PERI_REG(SPI_MEM_MISO_DLEN_REG(spi_no),reg_bak4);
    WRITE_PERI_REG(SPI_MEM_CTRL_REG(spi_no),reg_bak5);

}

//===========================================
// wrap_mode;0: disable
//           1: 16 bytes
//           2: 32 bytes
//           3: 64 bytes
//===========================================
void sim_spi_set_wrap(unsigned int spi_no,unsigned int wrap_mode ) {
    unsigned int mode   = 0;
    unsigned int reg_bak0;
    unsigned int reg_bak1;
    unsigned int reg_bak2;
    unsigned int reg_bak3;
    unsigned int reg_bak4;
    unsigned int reg_bak5;

    spi_flash_wren(spi_no);

    reg_bak0 = READ_PERI_REG(SPI_MEM_USER1_REG(spi_no));
    reg_bak1 = READ_PERI_REG(SPI_MEM_W0_REG(spi_no));
    reg_bak2 = READ_PERI_REG(SPI_MEM_USER_REG(spi_no));
    reg_bak3 = READ_PERI_REG(SPI_MEM_USER2_REG(spi_no));
    reg_bak4 = READ_PERI_REG(SPI_MEM_MISO_DLEN_REG(spi_no));
    reg_bak5 = READ_PERI_REG(SPI_MEM_CTRL_REG(spi_no));

    WRITE_PERI_REG(SPI_MEM_CTRL_REG(spi_no),0);
    WRITE_PERI_REG(SPI_MEM_USER_REG(spi_no),0);

    SET_PERI_REG_MASK(SPI_MEM_CTRL_REG(spi_no),SPI_MEM_WP_REG|SPI_MEM_D_POL|SPI_MEM_Q_POL);
    switch( wrap_mode ) {
        case 1: mode = 2; break;
        case 2: mode = 4; break;
        case 3: mode = 6; break;
        default: mode = 0xf;    
    }
    mode = (mode&0xf)<<4;  
//////////////////////////////////////////
    WRITE_PERI_REG(SPI_MEM_W0_REG(spi_no),mode);
    SET_PERI_REG_MASK(SPI_MEM_USER_REG(spi_no),SPI_MEM_USR_COMMAND|SPI_MEM_FWRITE_QIO|SPI_MEM_USR_DUMMY|SPI_MEM_USR_MOSI|SPI_MEM_CS_SETUP);//////////////////////////////
    SET_PERI_REG_BITS(SPI_MEM_USER1_REG(spi_no),SPI_MEM_USR_DUMMY_CYCLELEN,0x5,SPI_MEM_USR_DUMMY_CYCLELEN_S); // usr_dummy_cyclelen
    WRITE_PERI_REG(SPI_MEM_MOSI_DLEN_REG(spi_no),0x7);
    SET_PERI_REG_BITS(SPI_MEM_USER2_REG(spi_no),SPI_MEM_USR_COMMAND_BITLEN,0x7,SPI_MEM_USR_COMMAND_BITLEN_S); 
    SET_PERI_REG_BITS(SPI_MEM_USER2_REG(spi_no),SPI_MEM_USR_COMMAND_VALUE,0x77,SPI_MEM_USR_COMMAND_VALUE_S); 

    WRITE_PERI_REG(SPI_MEM_CMD_REG(spi_no),SPI_MEM_USR);
    while(READ_PERI_REG(SPI_MEM_CMD_REG(spi_no)));

    WRITE_PERI_REG(SPI_MEM_USER1_REG(spi_no),reg_bak0);
    WRITE_PERI_REG(SPI_MEM_W0_REG(spi_no),reg_bak1);
    WRITE_PERI_REG(SPI_MEM_USER_REG(spi_no),reg_bak2);
    WRITE_PERI_REG(SPI_MEM_USER2_REG(spi_no),reg_bak3);
    WRITE_PERI_REG(SPI_MEM_MISO_DLEN_REG(spi_no),reg_bak4);
    WRITE_PERI_REG(SPI_MEM_CTRL_REG(spi_no),reg_bak5);
}

//===========================================
// wrap_mode;0: disable
//           1: 16 bytes
//           2: 32 bytes
//           3: 64 bytes
//===========================================
void sim_spi_set_swrap(unsigned int spi_no,unsigned int cmd,unsigned int wrap_mode ) {
    unsigned int reg_bak0;
    unsigned int reg_bak1;
    unsigned int reg_bak2;
    unsigned int reg_bak3;
    unsigned int reg_bak4;
    unsigned int reg_bak5;

    reg_bak0 = READ_PERI_REG(SPI_MEM_USER1_REG(spi_no));
    reg_bak1 = READ_PERI_REG(SPI_MEM_W0_REG(spi_no));
    reg_bak2 = READ_PERI_REG(SPI_MEM_USER_REG(spi_no));
    reg_bak3 = READ_PERI_REG(SPI_MEM_USER2_REG(spi_no));
    reg_bak4 = READ_PERI_REG(SPI_MEM_MISO_DLEN_REG(spi_no));
    reg_bak5 = READ_PERI_REG(SPI_MEM_CTRL_REG(spi_no));

    WRITE_PERI_REG(SPI_MEM_CTRL_REG(spi_no),0);
    WRITE_PERI_REG(SPI_MEM_USER_REG(spi_no),0);

    SET_PERI_REG_MASK(SPI_MEM_CTRL_REG(spi_no),SPI_MEM_WP_REG|SPI_MEM_D_POL|SPI_MEM_Q_POL|SPI_MEM_FCMD_QUAD);
//////////////////////////////////////////
    WRITE_PERI_REG(SPI_MEM_W0_REG(spi_no),wrap_mode);
    SET_PERI_REG_MASK(SPI_MEM_USER_REG(spi_no),SPI_MEM_USR_COMMAND|SPI_MEM_FWRITE_QIO|SPI_MEM_USR_MOSI|SPI_MEM_CS_SETUP);//////////////////////////////
    SET_PERI_REG_BITS(SPI_MEM_USER1_REG(spi_no),SPI_MEM_USR_DUMMY_CYCLELEN,0x5,SPI_MEM_USR_DUMMY_CYCLELEN_S); // usr_dummy_cyclelen
    WRITE_PERI_REG(SPI_MEM_MOSI_DLEN_REG(spi_no),0x7);
    SET_PERI_REG_BITS(SPI_MEM_USER2_REG(spi_no),SPI_MEM_USR_COMMAND_BITLEN,0x7,SPI_MEM_USR_COMMAND_BITLEN_S); 
    SET_PERI_REG_BITS(SPI_MEM_USER2_REG(spi_no),SPI_MEM_USR_COMMAND_VALUE,cmd,SPI_MEM_USR_COMMAND_VALUE_S); 

    WRITE_PERI_REG(SPI_MEM_CMD_REG(spi_no),SPI_MEM_USR);
    while(READ_PERI_REG(SPI_MEM_CMD_REG(spi_no)));

    WRITE_PERI_REG(SPI_MEM_USER1_REG(spi_no),reg_bak0);
    WRITE_PERI_REG(SPI_MEM_W0_REG(spi_no),reg_bak1);
    WRITE_PERI_REG(SPI_MEM_USER_REG(spi_no),reg_bak2);
    WRITE_PERI_REG(SPI_MEM_USER2_REG(spi_no),reg_bak3);
    WRITE_PERI_REG(SPI_MEM_MISO_DLEN_REG(spi_no),reg_bak4);
    WRITE_PERI_REG(SPI_MEM_CTRL_REG(spi_no),reg_bak5);
}

void sim_spi_wait_flash_idle(unsigned int spi_no)
{
    unsigned int temp = 0;

    while(1){
        temp = sim_spi_rdst_0(spi_no);
        temp = ((temp & 0x1) >> 1);
        if(0 == temp)
            break;
    }
}

// wait program / erase  suspend done.
void WaitFlashPEDone(unsigned int spi_no)
{
    unsigned int sus = 0;
    unsigned int busy = 0;
    do{
        // it should be sent command to flash, 
        // because some level resetings donot lead to flash power-down,
        // while reseting entire digital core, which will lost all information about flash.
        sus = GET_PERI_REG_MASK(SPI_MEM_SUS_STATUS_REG(spi_no),SPI_MEM_FLASH_SUS);
        if( sus ){
            spi_flash_per(spi_no); // suspend resume
        } else {
            break;
        }
    }while(1);
}

void sim_spi_mem_pad_init(unsigned int spi_no) {
	PIN_FUNC_SELECT(PERIPHS_IO_MUX_SPICS0_U,FUNC_SPICS0_SPICS0);// pad cs(CMD)
	PIN_FUNC_SELECT(PERIPHS_IO_MUX_SPICLK_U,FUNC_SPICLK_SPICLK);// pad clk(CLK)
	PIN_FUNC_SELECT(PERIPHS_IO_MUX_SPID_U,FUNC_SPID_SPID);      // pad data1(d)
	PIN_FUNC_SELECT(PERIPHS_IO_MUX_SPIQ_U,FUNC_SPIQ_SPIQ);      // pad data0(q)
	PIN_FUNC_SELECT(PERIPHS_IO_MUX_SPIWP_U,FUNC_SPIWP_SPIWP);   // pad WP(data3)
	PIN_FUNC_SELECT(PERIPHS_IO_MUX_SPIHD_U,FUNC_SPIHD_SPIHD);   // pad HD(data2)
        SET_PERI_REG_MASK(PERIPHS_IO_MUX_SPID_U,FUN_IE);
        SET_PERI_REG_MASK(PERIPHS_IO_MUX_SPIQ_U,FUN_IE);
        SET_PERI_REG_MASK(PERIPHS_IO_MUX_SPIWP_U,FUN_IE);
        SET_PERI_REG_MASK(PERIPHS_IO_MUX_SPIHD_U,FUN_IE);
}

void spi_flash_mode_change(unsigned int spi_no, unsigned int mode){
    while((READ_PERI_REG(SPI_MEM_FSM_REG(0)) & 0x7) != 0);
    SET_PERI_REG_BITS(SPI_MEM_CACHE_FCTRL_REG(0),0x1,0x0,SPI_MEM_CACHE_REQ_EN_S);   // ahb_spi_req_en
    if(mode == 0){//slow mode, line1
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x0,SPI_MEM_FASTRD_MODE_S);  // fast_read_en
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x0,SPI_MEM_FREAD_QIO_S);    // fread_qio
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x0,SPI_MEM_FREAD_DIO_S);    // fread_dio    
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x0,SPI_MEM_FREAD_QUAD_S);   // fread_qout
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x0,SPI_MEM_FREAD_DUAL_S);   // fread_dout
        SET_PERI_REG_BITS(SPI_MEM_USER_REG(0),0x1,0x0,SPI_MEM_USR_DUMMY_S);    // usr_dummy
        SET_PERI_REG_BITS(SPI_MEM_USER1_REG(0),SPI_MEM_USR_ADDR_BITLEN,0x17,SPI_MEM_USR_ADDR_BITLEN_S);      // addr_bitlen
        SET_PERI_REG_BITS(SPI_MEM_USER2_REG(0),SPI_MEM_USR_COMMAND_VALUE,0x3,SPI_MEM_USR_COMMAND_VALUE_S);  // usr_command_value
    }else if(mode == 1){//fast mode, line1
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x1,SPI_MEM_FASTRD_MODE_S);  // fast_read_en
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x0,SPI_MEM_FREAD_QIO_S);    // fread_qio
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x0,SPI_MEM_FREAD_DIO_S);    // fread_dio    
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x0,SPI_MEM_FREAD_QUAD_S);   // fread_qout
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x0,SPI_MEM_FREAD_DUAL_S);   // fread_dout
        SET_PERI_REG_BITS(SPI_MEM_USER_REG(0),0x1,0x1,SPI_MEM_USR_DUMMY_S);    // usr_dummy
        SET_PERI_REG_BITS(SPI_MEM_USER1_REG(0),SPI_MEM_USR_ADDR_BITLEN,0x17,SPI_MEM_USR_ADDR_BITLEN_S);      // addr_bitlen
        SET_PERI_REG_BITS(SPI_MEM_USER1_REG(0),SPI_MEM_USR_DUMMY_CYCLELEN,0x7,SPI_MEM_USR_DUMMY_CYCLELEN_S); // usr_dummy_cyclelen
        SET_PERI_REG_BITS(SPI_MEM_USER2_REG(0),SPI_MEM_USR_COMMAND_VALUE,0x0B,SPI_MEM_USR_COMMAND_VALUE_S);  // usr_command_value
    }else if(mode == 2){//fast mode, line2(dout)
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x1,SPI_MEM_FASTRD_MODE_S);  // fast_read_en
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x0,SPI_MEM_FREAD_QIO_S);    // fread_qio   
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x0,SPI_MEM_FREAD_DIO_S);    // fread_dio   
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x0,SPI_MEM_FREAD_QUAD_S);   // fread_qout  
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x1,SPI_MEM_FREAD_DUAL_S);   // fread_dout
        SET_PERI_REG_BITS(SPI_MEM_USER_REG(0),0x1,0x1,SPI_MEM_USR_DUMMY_S);    // usr_dummy   
        SET_PERI_REG_BITS(SPI_MEM_USER1_REG(0),SPI_MEM_USR_ADDR_BITLEN,0x17,SPI_MEM_USR_ADDR_BITLEN_S);      // addr_bitlen
        SET_PERI_REG_BITS(SPI_MEM_USER1_REG(0),SPI_MEM_USR_DUMMY_CYCLELEN,0x7,SPI_MEM_USR_DUMMY_CYCLELEN_S); // usr_dummy_cyclelen
        SET_PERI_REG_BITS(SPI_MEM_USER2_REG(0),SPI_MEM_USR_COMMAND_VALUE,0x3B,SPI_MEM_USR_COMMAND_VALUE_S);  // usr_command_value
    }else if(mode == 3){//fast mode, line2(dio)
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x1,SPI_MEM_FASTRD_MODE_S);  // fast_read_en
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x0,SPI_MEM_FREAD_QIO_S);    // fread_qio   
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x1,SPI_MEM_FREAD_DIO_S);    // fread_dio   
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x0,SPI_MEM_FREAD_QUAD_S);        // fread_qout  
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x0,SPI_MEM_FREAD_DUAL_S);   // fread_dout
        SET_PERI_REG_BITS(SPI_MEM_USER_REG(0),0x1,0x1,SPI_MEM_USR_DUMMY_S);    // usr_dummy   
        SET_PERI_REG_BITS(SPI_MEM_USER1_REG(0),SPI_MEM_USR_ADDR_BITLEN,0x17,SPI_MEM_USR_ADDR_BITLEN_S);      // addr_bitlen
        SET_PERI_REG_BITS(SPI_MEM_USER1_REG(0),SPI_MEM_USR_DUMMY_CYCLELEN,0x3,SPI_MEM_USR_DUMMY_CYCLELEN_S); // usr_dummy_cyclelen
        SET_PERI_REG_BITS(SPI_MEM_USER2_REG(0),SPI_MEM_USR_COMMAND_VALUE,0xBB,SPI_MEM_USR_COMMAND_VALUE_S);  // usr_command_value
    }else if(mode == 4){//fast mode lin4(qout)
        sim_spi_wrst_qe(spi_no);
        sim_spi_wrst_qe1(spi_no);
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x1,SPI_MEM_FASTRD_MODE_S);       // fast_read_en
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x0,SPI_MEM_FREAD_QIO_S);    // fread_qio   
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x0,SPI_MEM_FREAD_DIO_S);    // fread_dio   
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x1,SPI_MEM_FREAD_QUAD_S);        // fread_qout  
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x0,SPI_MEM_FREAD_DUAL_S);   // fread_dout
        SET_PERI_REG_BITS(SPI_MEM_USER_REG(0),0x1,0x1,SPI_MEM_USR_DUMMY_S);    // usr_dummy   
        SET_PERI_REG_BITS(SPI_MEM_USER1_REG(0),SPI_MEM_USR_ADDR_BITLEN,0x17,SPI_MEM_USR_ADDR_BITLEN_S);      // addr_bitlen
        SET_PERI_REG_BITS(SPI_MEM_USER1_REG(0),SPI_MEM_USR_DUMMY_CYCLELEN,0x7,SPI_MEM_USR_DUMMY_CYCLELEN_S); // usr_dummy_cyclelen
        SET_PERI_REG_BITS(SPI_MEM_USER2_REG(0),SPI_MEM_USR_COMMAND_VALUE,0x6B,SPI_MEM_USR_COMMAND_VALUE_S);  // usr_command_value
    }else if(mode == 5){//fast mode lin4(qio)
        sim_spi_wrst_qe(spi_no);
        sim_spi_wrst_qe1(spi_no);
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x1,SPI_MEM_FASTRD_MODE_S);       // fast_read_en
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x1,SPI_MEM_FREAD_QIO_S);    // fread_qio   
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x0,SPI_MEM_FREAD_DIO_S);    // fread_dio   
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x0,SPI_MEM_FREAD_QUAD_S);        // fread_qout  
        SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x0,SPI_MEM_FREAD_DUAL_S);   // fread_dout
        SET_PERI_REG_BITS(SPI_MEM_USER_REG(0),0x1,0x1,SPI_MEM_USR_DUMMY_S);    // usr_dummy   
        SET_PERI_REG_BITS(SPI_MEM_RD_STATUS_REG(0),SPI_MEM_WB_MODE,0xF0,SPI_MEM_WB_MODE_S);//wb mode bit
        SET_PERI_REG_BITS(SPI_MEM_USER1_REG(0),SPI_MEM_USR_ADDR_BITLEN,0x1F,SPI_MEM_USR_ADDR_BITLEN_S);      // addr_bitlen
        SET_PERI_REG_BITS(SPI_MEM_USER1_REG(0),SPI_MEM_USR_DUMMY_CYCLELEN,0x3,SPI_MEM_USR_DUMMY_CYCLELEN_S); // usr_dummy_cyclelen
        SET_PERI_REG_BITS(SPI_MEM_USER2_REG(0),SPI_MEM_USR_COMMAND_VALUE,0xEB,SPI_MEM_USR_COMMAND_VALUE_S);  // usr_command_value
    }else if(mode == 6){
        //SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x0,SPI_MEM_FASTRD_MODE_S);       // fast_read_en
        //SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x0,SPI_MEM_FREAD_QIO_S);    // fread_qio   
        //SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x0,SPI_MEM_FREAD_DIO_S);    // fread_dio   
        //SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x0,SPI_MEM_FREAD_QUAD_S);        // fread_qout  
        //SET_PERI_REG_BITS(SPI_MEM_CTRL_REG(0),0x1,0x0,SPI_MEM_FREAD_DUAL_S);   // fread_dout
        //SET_PERI_REG_BITS(SPI_MEM_USER_REG(0),0x1,0x1,SPI_MEM_USR_DUMMY_S);    // usr_dummy  
        //SET_PERI_REG_BITS(SPI_MEM_USER1_REG(0),SPI_MEM_USR_ADDR_BITLEN,0x17,SPI_MEM_USR_ADDR_BITLEN_S);      // addr_bitlen
        //SET_PERI_REG_BITS(SPI_MEM_CACHE_FCTRL_REG(0),0x1,0x1,SPI_MEM_CACHE_FLASH_USR_CMD_S); // ahb_usr_command
	//SET_PERI_REG_MASK(SPI_MEM_CTRL_REG(0),SPI_MEM_FCMD_OCT|SPI_MEM_FADDR_OCT|SPI_MEM_FDIN_OCT);
        //SET_PERI_REG_BITS(SPI_MEM_USER1_REG(0),SPI_MEM_USR_DUMMY_CYCLELEN,0x7,SPI_MEM_USR_DUMMY_CYCLELEN_S); // usr_dummy_cyclelen
        //SET_PERI_REG_BITS(SPI_MEM_USER2_REG(0),SPI_MEM_USR_COMMAND_VALUE,0xBE,SPI_MEM_USR_COMMAND_VALUE_S);  // usr_command_value
	fail("xx\n");
    }
    SET_PERI_REG_BITS(SPI_MEM_CACHE_FCTRL_REG(0),0x1,0x1,SPI_MEM_CACHE_FLASH_USR_CMD_S); // ahb_usr_command
    SET_PERI_REG_BITS(SPI_MEM_CACHE_FCTRL_REG(0),0x1,0x1,SPI_MEM_CACHE_REQ_EN_S);                // ahb_spi_req_en
}

void sim_spi_cache_flash_init(unsigned mode) {
//flash config
    SET_PERI_REG_BITS(SPI_MEM_RD_STATUS_REG(0),0xff,0x0,SPI_MEM_WB_MODE_S);     // mode bit
    SET_PERI_REG_BITS(SPI_MEM_USER_REG(0),0x1,0x1,SPI_MEM_USR_ADDR_S);      // usr_addr
                                                                
    SET_PERI_REG_BITS(SPI_MEM_USER_REG(0),0x1,0x0,SPI_MEM_USR_MOSI_S);      // usr_dout
    SET_PERI_REG_BITS(SPI_MEM_USER_REG(0),0x1,0x1,SPI_MEM_USR_MISO_S);      // usr_din

    SET_PERI_REG_BITS(SPI_MEM_MOSI_DLEN_REG(0),SPI_MEM_USR_MOSI_DBITLEN,0xff,SPI_MEM_USR_MOSI_DBITLEN_S);// usr_dout_bitlen
    SET_PERI_REG_BITS(SPI_MEM_MISO_DLEN_REG(0),SPI_MEM_USR_MISO_DBITLEN,0xff,SPI_MEM_USR_MISO_DBITLEN_S);// usr_din_bitlen
    
    SET_PERI_REG_BITS(SPI_MEM_MISC_REG(1),0x1,0x0,SPI_MEM_CS0_DIS_S);         // cs0 enable
    SET_PERI_REG_BITS(SPI_MEM_MISC_REG(1),0x1,0x1,SPI_MEM_CS1_DIS_S);         // cs1 disable 
    spi_flash_mode_change(1,mode); 


    SET_PERI_REG_BITS(SPI_MEM_MISC_REG(0),0x1,0x0,SPI_MEM_CS0_DIS_S);     // cs0 enable
    SET_PERI_REG_BITS(SPI_MEM_MISC_REG(0),0x1,0x0,SPI_MEM_CS1_DIS_S);     // cs1 enable 
}

void spi_sram_op(int spi_no, int cmd)
{
    unsigned int reg_bak0;
    unsigned int reg_bak1;
    unsigned int reg_bak2;
    unsigned int reg_bak3;
    unsigned int reg_bak4;
    unsigned int reg_bak5;

    reg_bak0 = READ_PERI_REG(SPI_MEM_USER1_REG(spi_no));
    reg_bak1 = READ_PERI_REG(SPI_MEM_W0_REG(spi_no));
    reg_bak2 = READ_PERI_REG(SPI_MEM_USER_REG(spi_no));
    reg_bak3 = READ_PERI_REG(SPI_MEM_USER2_REG(spi_no));
    reg_bak4 = READ_PERI_REG(SPI_MEM_MISO_DLEN_REG(spi_no));
    reg_bak5 = READ_PERI_REG(SPI_MEM_CTRL_REG(spi_no));

    WRITE_PERI_REG(SPI_MEM_CTRL_REG(spi_no),0);
    WRITE_PERI_REG(SPI_MEM_USER_REG(spi_no),0);

    SET_PERI_REG_MASK(SPI_MEM_CTRL_REG(spi_no),SPI_MEM_WP_REG|SPI_MEM_D_POL|SPI_MEM_Q_POL);
//////////////////////////////////////////
    SET_PERI_REG_MASK(SPI_MEM_USER_REG(spi_no),SPI_MEM_USR_COMMAND|SPI_MEM_CS_SETUP);//////////////////////////////
    SET_PERI_REG_BITS(SPI_MEM_USER2_REG(spi_no),SPI_MEM_USR_COMMAND_BITLEN,0x7,SPI_MEM_USR_COMMAND_BITLEN_S); 
    SET_PERI_REG_BITS(SPI_MEM_USER2_REG(spi_no),SPI_MEM_USR_COMMAND_VALUE,cmd,SPI_MEM_USR_COMMAND_VALUE_S); 

    WRITE_PERI_REG(SPI_MEM_CMD_REG(spi_no),SPI_MEM_USR);
    while(READ_PERI_REG(SPI_MEM_CMD_REG(spi_no)));

    WRITE_PERI_REG(SPI_MEM_USER1_REG(spi_no),reg_bak0);
    WRITE_PERI_REG(SPI_MEM_W0_REG(spi_no),reg_bak1);
    WRITE_PERI_REG(SPI_MEM_USER_REG(spi_no),reg_bak2);
    WRITE_PERI_REG(SPI_MEM_USER2_REG(spi_no),reg_bak3);
    WRITE_PERI_REG(SPI_MEM_MISO_DLEN_REG(spi_no),reg_bak4);
    WRITE_PERI_REG(SPI_MEM_CTRL_REG(spi_no),reg_bak5);
}
void spi_sram_rdid(int spi_no)
{
    unsigned int reg_bak0;
    unsigned int reg_bak1;
    unsigned int reg_bak2;
    unsigned int reg_bak3;
    unsigned int reg_bak4;
    unsigned int reg_bak5;

    reg_bak0 = READ_PERI_REG(SPI_MEM_USER1_REG(spi_no));
    reg_bak1 = READ_PERI_REG(SPI_MEM_W0_REG(spi_no));
    reg_bak2 = READ_PERI_REG(SPI_MEM_USER_REG(spi_no));
    reg_bak3 = READ_PERI_REG(SPI_MEM_USER2_REG(spi_no));
    reg_bak4 = READ_PERI_REG(SPI_MEM_MISO_DLEN_REG(spi_no));
    reg_bak5 = READ_PERI_REG(SPI_MEM_CTRL_REG(spi_no));

    WRITE_PERI_REG(SPI_MEM_CTRL_REG(spi_no),0);
    WRITE_PERI_REG(SPI_MEM_USER_REG(spi_no),0);

    WRITE_PERI_REG(SPI_MEM_MISO_DLEN_REG(spi_no),0xf);
    SET_PERI_REG_MASK(SPI_MEM_CTRL_REG(spi_no),SPI_MEM_WP_REG|SPI_MEM_D_POL|SPI_MEM_Q_POL);
//////////////////////////////////////////
    SET_PERI_REG_MASK(SPI_MEM_USER_REG(spi_no),SPI_MEM_USR_COMMAND|SPI_MEM_USR_ADDR|SPI_MEM_USR_MISO|SPI_MEM_CS_SETUP);//////////////////////////////
    SET_PERI_REG_BITS(SPI_MEM_USER1_REG(spi_no),SPI_MEM_USR_ADDR_BITLEN,0x17,SPI_MEM_USR_ADDR_BITLEN_S); 
    SET_PERI_REG_BITS(SPI_MEM_USER2_REG(spi_no),SPI_MEM_USR_COMMAND_BITLEN,0x7,SPI_MEM_USR_COMMAND_BITLEN_S); 
    SET_PERI_REG_BITS(SPI_MEM_USER2_REG(spi_no),SPI_MEM_USR_COMMAND_VALUE,0x9f,SPI_MEM_USR_COMMAND_VALUE_S); 

    WRITE_PERI_REG(SPI_MEM_CMD_REG(spi_no),SPI_MEM_USR);
    while(READ_PERI_REG(SPI_MEM_CMD_REG(spi_no)));

    //ets_print("sram id %x \n", READ_PERI_REG(SPI_MEM_W0_REG(spi_no))&0xffff);

    WRITE_PERI_REG(SPI_MEM_USER1_REG(spi_no),reg_bak0);
    WRITE_PERI_REG(SPI_MEM_W0_REG(spi_no),reg_bak1);
    WRITE_PERI_REG(SPI_MEM_USER_REG(spi_no),reg_bak2);
    WRITE_PERI_REG(SPI_MEM_USER2_REG(spi_no),reg_bak3);
    WRITE_PERI_REG(SPI_MEM_MISO_DLEN_REG(spi_no),reg_bak4);
    WRITE_PERI_REG(SPI_MEM_CTRL_REG(spi_no),reg_bak5);
}
void spi_sram_mode_change(unsigned int mode){
    if(mode !=3 ){
        spi_sram_op(1,0xff);
        SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),SPI_MEM_SRAM_ADDR_BITLEN,0x17,SPI_MEM_SRAM_ADDR_BITLEN_S);// sram dummy_bitlen
    }
    spi_sram_rdid(1);
    if(mode == 0){//line1
        SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),0x1,0x0,SPI_MEM_USR_RD_SRAM_DUMMY_S);          // sram_dummy
        SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),SPI_MEM_SRAM_RDUMMY_CYCLELEN,0x0,SPI_MEM_SRAM_RDUMMY_CYCLELEN_S);// sram dummy_bitlen
        SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),0x1,0x0,SPI_MEM_USR_SRAM_DIO_S);       // sram_iomode
        SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),0x1,0x0,SPI_MEM_USR_SRAM_QIO_S);       // sram_iomode
        SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),0x1,0x1,SPI_MEM_CACHE_SRAM_USR_WCMD_S);    // sram_usr_wcmd
        SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),0x1,0x1,SPI_MEM_CACHE_SRAM_USR_RCMD_S);    // sram_usr_rcmd
        SET_PERI_REG_BITS(SPI_MEM_SRAM_DRD_CMD_REG(0),SPI_MEM_CACHE_SRAM_USR_RD_CMD_BITLEN,0x7,SPI_MEM_CACHE_SRAM_USR_RD_CMD_BITLEN_S); // read cmd len
        SET_PERI_REG_BITS(SPI_MEM_SRAM_DRD_CMD_REG(0),SPI_MEM_CACHE_SRAM_USR_RD_CMD_VALUE,0x03,SPI_MEM_CACHE_SRAM_USR_RD_CMD_VALUE_S);  // read  cmd value
        SET_PERI_REG_BITS(SPI_MEM_SRAM_DWR_CMD_REG(0),SPI_MEM_CACHE_SRAM_USR_WR_CMD_BITLEN,0x7,SPI_MEM_CACHE_SRAM_USR_WR_CMD_BITLEN_S);     // write cmd len
        SET_PERI_REG_BITS(SPI_MEM_SRAM_DWR_CMD_REG(0),SPI_MEM_CACHE_SRAM_USR_WR_CMD_VALUE,0x02,SPI_MEM_CACHE_SRAM_USR_WR_CMD_VALUE_S);     // write cmd value
    }else if(mode == 1){//line2 (dio)
        spi_sram_op(1,0x3b);
        SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),0x1,0x1,SPI_MEM_USR_RD_SRAM_DUMMY_S);          // sram_dummy
        SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),SPI_MEM_SRAM_RDUMMY_CYCLELEN,0x3,SPI_MEM_SRAM_RDUMMY_CYCLELEN_S);// sram dummy_bitlen
        SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),0x1,0x1,SPI_MEM_USR_SRAM_DIO_S);       // sram_iomode
        SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),0x1,0x0,SPI_MEM_USR_SRAM_QIO_S);       // sram_iomode
        SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),0x1,0x1,SPI_MEM_CACHE_SRAM_USR_WCMD_S);    // sram_usr_wcmd
        SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),0x1,0x1,SPI_MEM_CACHE_SRAM_USR_RCMD_S);    // sram_usr_rcmd
        SET_PERI_REG_BITS(SPI_MEM_SRAM_DRD_CMD_REG(0),SPI_MEM_CACHE_SRAM_USR_RD_CMD_BITLEN,0x7,SPI_MEM_CACHE_SRAM_USR_RD_CMD_BITLEN_S); // read cmd len
        SET_PERI_REG_BITS(SPI_MEM_SRAM_DRD_CMD_REG(0),SPI_MEM_CACHE_SRAM_USR_RD_CMD_VALUE,0x03,SPI_MEM_CACHE_SRAM_USR_RD_CMD_VALUE_S);  // read  cmd value
        SET_PERI_REG_BITS(SPI_MEM_SRAM_DWR_CMD_REG(0),SPI_MEM_CACHE_SRAM_USR_WR_CMD_BITLEN,0x7,SPI_MEM_CACHE_SRAM_USR_WR_CMD_BITLEN_S);     // write cmd len
        SET_PERI_REG_BITS(SPI_MEM_SRAM_DWR_CMD_REG(0),SPI_MEM_CACHE_SRAM_USR_WR_CMD_VALUE,0x02,SPI_MEM_CACHE_SRAM_USR_WR_CMD_VALUE_S);     // write cmd value	
    }else if(mode == 2){//line4 (qio)
        spi_sram_op(1,0x35);
        SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),0x1,0x1,SPI_MEM_USR_RD_SRAM_DUMMY_S);  // sram_dummy
        SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),SPI_MEM_SRAM_RDUMMY_CYCLELEN,0x5,SPI_MEM_SRAM_RDUMMY_CYCLELEN_S);// sram dummy_bitlen
        SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),0x1,0x0,SPI_MEM_USR_SRAM_DIO_S);       // sram_iomode
        SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),0x1,0x1,SPI_MEM_USR_SRAM_QIO_S);       // sram_iomode
        SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),0x1,0x1,SPI_MEM_CACHE_SRAM_USR_WCMD_S);    // sram_usr_wcmd
        SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),0x1,0x1,SPI_MEM_CACHE_SRAM_USR_RCMD_S);    // sram_usr_rcmd
        SET_PERI_REG_BITS(SPI_MEM_SRAM_DRD_CMD_REG(0),SPI_MEM_CACHE_SRAM_USR_RD_CMD_BITLEN,0x7,SPI_MEM_CACHE_SRAM_USR_RD_CMD_BITLEN_S); // read cmd len
        SET_PERI_REG_BITS(SPI_MEM_SRAM_DRD_CMD_REG(0),SPI_MEM_CACHE_SRAM_USR_RD_CMD_VALUE,0xEB,SPI_MEM_CACHE_SRAM_USR_RD_CMD_VALUE_S);  // read  cmd value
        SET_PERI_REG_BITS(SPI_MEM_SRAM_DWR_CMD_REG(0),SPI_MEM_CACHE_SRAM_USR_WR_CMD_BITLEN,0x7,SPI_MEM_CACHE_SRAM_USR_WR_CMD_BITLEN_S);     // write cmd len
        SET_PERI_REG_BITS(SPI_MEM_SRAM_DWR_CMD_REG(0),SPI_MEM_CACHE_SRAM_USR_WR_CMD_VALUE,0x38,SPI_MEM_CACHE_SRAM_USR_WR_CMD_VALUE_S);     // write cmd value
    }else if(mode == 3){//line4 (oct)
        //SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),0x1,0x1,SPI_MEM_USR_RD_SRAM_DUMMY_S);  // sram_dummy
        //SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),SPI_MEM_SRAM_RDUMMY_CYCLELEN,0x7,SPI_MEM_SRAM_RDUMMY_CYCLELEN_S);// sram dummy_bitlen
        //SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),0x1,0x0,SPI_MEM_USR_SRAM_DIO_S);       // sram_iomode
        //SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),0x1,0x0,SPI_MEM_USR_SRAM_QIO_S);       // sram_iomode
        //SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),0x1,0x1,SPI_MEM_USR_SRAM_OCT_S);       // sram_iomode
        //SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),0x1,0x1,SPI_MEM_CACHE_SRAM_USR_WCMD_S);    // sram_usr_wcmd
        //SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),0x1,0x1,SPI_MEM_CACHE_SRAM_USR_RCMD_S);    // sram_usr_rcmd
        //SET_PERI_REG_BITS(SPI_MEM_SRAM_DRD_CMD_REG(0),SPI_MEM_CACHE_SRAM_USR_RD_CMD_BITLEN,0x7,SPI_MEM_CACHE_SRAM_USR_RD_CMD_BITLEN_S); // read cmd len
        //SET_PERI_REG_BITS(SPI_MEM_SRAM_DRD_CMD_REG(0),SPI_MEM_CACHE_SRAM_USR_RD_CMD_VALUE,0xBE,SPI_MEM_CACHE_SRAM_USR_RD_CMD_VALUE_S);  // read  cmd value
        //SET_PERI_REG_BITS(SPI_MEM_SRAM_DWR_CMD_REG(0),SPI_MEM_CACHE_SRAM_USR_WR_CMD_BITLEN,0x7,SPI_MEM_CACHE_SRAM_USR_WR_CMD_BITLEN_S);     // write cmd len
        //SET_PERI_REG_BITS(SPI_MEM_SRAM_DWR_CMD_REG(0),SPI_MEM_CACHE_SRAM_USR_WR_CMD_VALUE,0x32,SPI_MEM_CACHE_SRAM_USR_WR_CMD_VALUE_S);     // write cmd value
	fail("xx\n");
    }
}

void sim_spi_cache_sram_init(unsigned mode) {
//sram config
    SET_PERI_REG_BITS(SPI_MEM_RD_STATUS_REG(0),0xff,0x0,SPI_MEM_WB_MODE_S);     // mode bit
    SET_PERI_REG_BITS(SPI_MEM_USER_REG(0),0x1,0x1,SPI_MEM_USR_ADDR_S);      // usr_addr
                                                                
    SET_PERI_REG_BITS(SPI_MEM_CACHE_SCTRL_REG(0),SPI_MEM_SRAM_ADDR_BITLEN,0x17,SPI_MEM_SRAM_ADDR_BITLEN_S);      // addr_bitlen

    SET_PERI_REG_BITS(SPI_MEM_MOSI_DLEN_REG(0),SPI_MEM_USR_MOSI_DBITLEN,0xff,SPI_MEM_USR_MOSI_DBITLEN_S);// usr_dout_bitlen
    SET_PERI_REG_BITS(SPI_MEM_MISO_DLEN_REG(0),SPI_MEM_USR_MISO_DBITLEN,0xff,SPI_MEM_USR_MISO_DBITLEN_S);// usr_din_bitlen

    SET_PERI_REG_BITS(SPI_MEM_SRAM_DRD_CMD_REG(0),SPI_MEM_CACHE_SRAM_USR_RD_CMD_BITLEN,0x7,SPI_MEM_CACHE_SRAM_USR_RD_CMD_BITLEN_S); // read cmd len
    SET_PERI_REG_BITS(SPI_MEM_SRAM_DRD_CMD_REG(0),SPI_MEM_CACHE_SRAM_USR_RD_CMD_VALUE,0x3,SPI_MEM_CACHE_SRAM_USR_RD_CMD_VALUE_S);  // read  cmd value
    SET_PERI_REG_BITS(SPI_MEM_SRAM_DWR_CMD_REG(0),SPI_MEM_CACHE_SRAM_USR_WR_CMD_BITLEN,0x7,SPI_MEM_CACHE_SRAM_USR_WR_CMD_BITLEN_S);     // write cmd len
    SET_PERI_REG_BITS(SPI_MEM_SRAM_DWR_CMD_REG(0),SPI_MEM_CACHE_SRAM_USR_WR_CMD_VALUE,0x2,SPI_MEM_CACHE_SRAM_USR_WR_CMD_VALUE_S);     // write cmd value
    SET_PERI_REG_BITS(SPI_MEM_MISC_REG(1),0x1,0x1,SPI_MEM_CS0_DIS_S);     // cs0 disable
    SET_PERI_REG_BITS(SPI_MEM_MISC_REG(1),0x1,0x0,SPI_MEM_CS1_DIS_S);     // cs1 enable 
    spi_sram_mode_change(mode);
    SET_PERI_REG_BITS(SPI_MEM_MISC_REG(1),0x1,0x0,SPI_MEM_CS0_DIS_S);     // cs0 disable
    SET_PERI_REG_BITS(SPI_MEM_MISC_REG(1),0x1,0x1,SPI_MEM_CS1_DIS_S);     // cs1 enable 

    SET_PERI_REG_BITS(SPI_MEM_MISC_REG(0),0x1,0x0,SPI_MEM_CS0_DIS_S);     // cs0 enable
    SET_PERI_REG_BITS(SPI_MEM_MISC_REG(0),0x1,0x0,SPI_MEM_CS1_DIS_S);     // cs1 enable 
}

void sim_spi_mem_clk_config(unsigned int spi_no,unsigned int pre_div,unsigned int div){
    unsigned int temp;
    if(div>1){
        temp = ((div-1)<<SPI_MEM_CLKCNT_N_S)|
               (((div>>1)-1)<<SPI_MEM_CLKCNT_H_S)|
               ((div-1)<<SPI_MEM_CLKCNT_L_S); 
    }else{
        temp = (0x1<<SPI_MEM_CLK_EQU_SYSCLK_S);
    }
    WRITE_PERI_REG(SPI_MEM_CLOCK_REG(spi_no),temp);
}

void sim_spi_mem_sclk_config(unsigned int spi_no,unsigned int pre_div,unsigned int div){
    unsigned int temp;
    if(div>1){
        temp = ((div-1)<<SPI_MEM_SCLKCNT_N_S)|
               (((div>>1)-1)<<SPI_MEM_SCLKCNT_H_S)|
               ((div-1)<<SPI_MEM_SCLKCNT_L_S); 
    }else{
        temp = (0x1<<SPI_MEM_SCLK_EQU_SYSCLK_S);
    }
    WRITE_PERI_REG(SPI_MEM_SRAM_CLK_REG(spi_no),temp);
}

void sim_spi_cache_init() {
    SET_PERI_REG_BITS(SPI_MEM_FLASH_WAITI_CTRL_REG(1),0x1,0x1,SPI_MEM_WAITI_EN_S); // enable hardware wait flash idle. 
    sim_spi_mem_pad_init(0);
    //config CS1 for SRAM
    PIN_FUNC_SELECT(PERIPHS_IO_MUX_SPICS1_U,FUNC_SPICS1_SPICS1);   // pad WP(data3)

    sim_spi_cache_flash_init(5);//flash config
    sim_spi_cache_sram_init(2);//sram config
    
    SET_PERI_REG_BITS(SPI_MEM_CACHE_FCTRL_REG(0),0x1,0x1,SPI_MEM_CACHE_REQ_EN_S); // ahb_spi_req_en
}
