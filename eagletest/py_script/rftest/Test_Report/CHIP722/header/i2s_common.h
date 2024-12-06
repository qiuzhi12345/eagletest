#include <xtensa/hal.h>
#include <xtensa/config/core.h>
#include <xtensa/config/system.h>
#include "../diag_utils.h"
//#include "i2s_reg.h"

#define MSB_right 0x1
#define MSB_left 0x0
#define right_first 0x1
#define left_first 0x0
void apb_wr(unsigned int addr, unsigned int value)
{
   *(volatile unsigned int*)(addr) = value;
}
#if 0
void i2s_test(int num, int case_num,int len,int trans_slave,int MSB_shift,int MSB_mode,
              int first_mode,int i2s_mono,int tx_chan_mod,int rx_chan_mod,int tx_fifo_mod,int rx_fifo_mod,int bit_mode,int i2s_short_sync){
  int take_int;
  int* reg_addr;
  int data_num;
  int delta;
  int a;
  int i;
  int bit_mode_msb;
  int bit_mode_lsb;
  delta=251;

  //*************************
  //i2s test begin:
  //*************************
/*******************************************************************************************************************/

  //trans master/slave
  SET_PERI_REG_BITS(I2SCONF_REG(num), 0x1, trans_slave,  I2S_TX_SLAVE_MOD_S);
  SET_PERI_REG_BITS(I2SCONF_REG(num), 0x1, ~trans_slave,  I2S_RX_SLAVE_MOD_S);

 
  //right_first
  SET_PERI_REG_BITS(I2SCONF_REG(num), 0x1,  first_mode,  I2S_TX_RIGHT_FIRST_S);
  SET_PERI_REG_BITS(I2SCONF_REG(num), 0x1,  first_mode,  I2S_RX_RIGHT_FIRST_S);

  //MSB right
  SET_PERI_REG_BITS(I2SCONF_REG(num), 0x1,  MSB_mode,  I2S_TX_MSB_RIGHT_S);
  SET_PERI_REG_BITS(I2SCONF_REG(num), 0x1,  MSB_mode,  I2S_RX_MSB_RIGHT_S);

  //MSB_shift
  SET_PERI_REG_BITS(I2SCONF_REG(num), 0x1,  MSB_shift,  I2S_TX_MSB_SHIFT_S);
  SET_PERI_REG_BITS(I2SCONF_REG(num), 0x1,  MSB_shift,  I2S_RX_MSB_SHIFT_S);

  //i2s_mono_en
  SET_PERI_REG_BITS( I2SCONF_REG(num),0x1,i2s_mono,I2S_TX_MONO_S);
  SET_PERI_REG_BITS( I2SCONF_REG(num),0x1,i2s_mono,I2S_RX_MONO_S);

  //i2s_short_sync
  SET_PERI_REG_BITS( I2SCONF_REG(num),0x1,i2s_short_sync,I2S_TX_SHORT_SYNC_S);
  SET_PERI_REG_BITS( I2SCONF_REG(num),0x1,i2s_short_sync,I2S_RX_SHORT_SYNC_S);
  
  //TX APB data mod
  SET_PERI_REG_BITS(I2S_FIFO_CONF_REG(num), I2S_TX_FIFO_MOD, tx_fifo_mod, I2S_TX_FIFO_MOD_S);
  SET_PERI_REG_BITS(I2S_FIFO_CONF_REG(num), I2S_RX_FIFO_MOD, rx_fifo_mod, I2S_RX_FIFO_MOD_S);
  
  //TX chan mod
  SET_PERI_REG_BITS(I2SCONF_CHAN_REG(num), I2S_TX_CHAN_MOD, tx_chan_mod, I2S_TX_CHAN_MOD_S);
  SET_PERI_REG_BITS(I2SCONF_CHAN_REG(num), I2S_RX_CHAN_MOD, rx_chan_mod, I2S_RX_CHAN_MOD_S);
  
  //bit_mode
  SET_PERI_REG_BITS(I2S_SAMPLE_RATE_CONF_REG(num), I2S_TX_BITS_MOD, bit_mode, I2S_TX_BITS_MOD_S);
  SET_PERI_REG_BITS(I2S_SAMPLE_RATE_CONF_REG(num), I2S_RX_BITS_MOD, bit_mode, I2S_RX_BITS_MOD_S);


/******************************************************************************************************************************/

  //test APB
  //clear int
  *(volatile U32*)(I2SINT_CLR_REG(num)) = *(volatile U32*)(I2SINT_CLR_REG(num)) & 0xffffffc0 | 0x3f;
  *(volatile U32*)(I2SINT_CLR_REG(num)) = *(volatile U32*)(I2SINT_CLR_REG(num)) & 0xffffffc0;

  //enable int
  *(volatile U32*)(I2SINT_ENA_REG(num)) = *(volatile U32*)(I2SINT_ENA_REG(num)) & 0xffffffc0 | 0x3f;
  
  //reset
  *(volatile U32*)(I2SCONF_REG(num))=  *(volatile U32*)(I2SCONF_REG(num)) & 0xfffffff0;
  *(volatile U32*)(I2SCONF_REG(num))=  *(volatile U32*)(I2SCONF_REG(num)) & 0xfffffff0 | (0xf);
  *(volatile U32*)(I2SCONF_REG(num))=  *(volatile U32*)(I2SCONF_REG(num)) & 0xfffffff0;
  SET_PERI_REG_BITS(I2SCONF2_REG(num),0x1,0x0,I2S_CAM_SYNC_FIFO_RESET_S);
  SET_PERI_REG_BITS(I2SCONF2_REG(num),0x1,0x1,I2S_CAM_SYNC_FIFO_RESET_S);
  SET_PERI_REG_BITS(I2SCONF2_REG(num),0x1,0x0,I2S_CAM_SYNC_FIFO_RESET_S);

 // SET_PERI_REG_BITS(REG_I2S_BASE,0xffffffff,0x1,0);
 // SET_PERI_REG_BITS(REG_I2S_BASE,0xffffffff,0x2,0);
 // SET_PERI_REG_BITS(REG_I2S_BASE,0xffffffff,0x3,0);
 // SET_PERI_REG_BITS(REG_I2S_BASE,0xffffffff,0x4,0);
  while (GET_PERI_REG_BITS(I2S_STATE_REG(num), 0x1, I2S_TX_FIFO_RESET_BACK_S)) {
  }

  //start
  if(trans_slave){
       SET_PERI_REG_BITS( I2SCONF_REG(num),0x1,0x1,I2S_TX_START_S);
       SET_PERI_REG_BITS( I2SCONF_REG(num),0x1,0x1,I2S_RX_START_S);
  }else{
       SET_PERI_REG_BITS( I2SCONF_REG(num),0x1,0x1,I2S_RX_START_S);
       SET_PERI_REG_BITS( I2SCONF_REG(num),0x1,0x1,I2S_TX_START_S);
  } 
  int offset = 0;
  while (1) {
     if (*(volatile U32*)(I2SINT_RAW_REG(num)) & 0x200) { //wait tx eof
       *(volatile U32*)(I2SINT_CLR_REG(num)) = 0x200;     //clear tx eof
         //start_end
       SET_PERI_REG_BITS( I2SCONF_REG(num),0x1,0x0,I2S_TX_START_S);
       SET_PERI_REG_BITS( I2SCONF_REG(num),0x1,0x0,I2S_RX_START_S);

       int loop_num;
       printinfo("case_num = \n", case_num);
         /*  
       for(loop_num = 0; loop_num < len; loop_num++) {
         printinfo("expect_h = ",(*(volatile U32*)(0x3ffb3000+loop_num*0x4))>>16);
         printinfo("expect_l = \n",(*(volatile U32*)(0x3ffb3000+loop_num*0x4)));
         printinfo("infact_h = ",  (*(volatile U32*)(0x3ffb1000+loop_num*0x4+ offset))>>16);
         printinfo("infact_l = \n",  *(volatile U32*)(0x3ffb1000+loop_num*0x4+ offset));
         if (*(volatile U32*)(0x3fff1000+(loop_num)*0x4 + offset) != ((tmp3<<24)+(tmp2<<16)+(tmp1<<8)+tmp0)) {
           *(volatile U32*)(REG_I2S_BASE + 0xf4) = loop_num;
           *(volatile U32*)(REG_I2S_BASE + 0xf8) = *(volatile U32*)(0x3fff1000+loop_num*0x4+ offset);           
           fail("Diag Failed\n");
           break;
         }
       }*/
       break;
     }  
  }


  //i2s test end!
  //*************************
}
#endif

unsigned int rx_buffer[256];
unsigned int tx_buffer[256];
//void i2s_clk_install(unsigned int freq_sample)
void i2s_clk_install( unsigned int i2s_no )
{
    if(i2s_no == 0){
        SET_PERI_REG_BITS(SYSTEM_PERIP_CLK_EN0_REG,0x1,0x1,4); //enable i2s0 clk
    } else {
        SET_PERI_REG_BITS(SYSTEM_PERIP_CLK_EN0_REG,0x1,0x1,21); //enable i2s1 clk
    }
    SET_PERI_REG_BITS(I2S_CLKM_CONF_REG(i2s_no),I2S_CLK_SEL,2,I2S_CLK_SEL_S);
    SET_PERI_REG_BITS(I2S_CLKM_CONF_REG(i2s_no),I2S_CLKM_DIV_A,0,I2S_CLKM_DIV_A_S);
    SET_PERI_REG_BITS(I2S_CLKM_CONF_REG(i2s_no),I2S_CLKM_DIV_B,0,I2S_CLKM_DIV_B_S);
    SET_PERI_REG_BITS(I2S_CLKM_CONF_REG(i2s_no),I2S_CLKM_DIV_NUM,4, I2S_CLKM_DIV_NUM_S);
    SET_PERI_REG_BITS(I2S_SAMPLE_RATE_CONF_REG(i2s_no),I2S_RX_BCK_DIV_NUM,4,I2S_RX_BCK_DIV_NUM_S);
    SET_PERI_REG_BITS(I2S_SAMPLE_RATE_CONF_REG(i2s_no),I2S_TX_BCK_DIV_NUM,4,I2S_TX_BCK_DIV_NUM_S);
}
void i2s_rx_init(unsigned int i2s_no, unsigned int bit_mode, unsigned int channel_mode)
{
    SET_PERI_REG_BITS(I2S_SAMPLE_RATE_CONF_REG(i2s_no), I2S_RX_BITS_MOD, bit_mode, I2S_RX_BITS_MOD_S);
    SET_PERI_REG_BITS(I2SCONF_REG(i2s_no), 0x1, ~channel_mode, I2S_RX_DMA_EQUAL_S); // enable camera mode
}

void i2s_tx_init(unsigned int i2s_no, unsigned int bit_mode, unsigned int channel_mode)
{
    SET_PERI_REG_BITS(I2S_SAMPLE_RATE_CONF_REG(i2s_no), I2S_TX_BITS_MOD, bit_mode, I2S_TX_BITS_MOD_S);
    SET_PERI_REG_BITS(I2SCONF_REG(i2s_no), 0x1, ~channel_mode, I2S_TX_DMA_EQUAL_S); // enable camera mode
}

void i2s_interrupt_init(unsigned int i2s_no)
{
    //clear int
    SET_PERI_REG_MASK(I2SINT_CLR_REG(i2s_no),I2S_OUT_EOF_INT_CLR|I2S_OUT_DONE_INT_CLR|I2S_IN_SUC_EOF_INT_CLR|I2S_IN_DONE_INT_CLR);
    CLEAR_PERI_REG_MASK(I2SINT_CLR_REG(i2s_no),I2S_OUT_EOF_INT_CLR|I2S_OUT_DONE_INT_CLR|I2S_IN_SUC_EOF_INT_CLR|I2S_IN_DONE_INT_CLR);
    //enable int
    SET_PERI_REG_MASK(I2SINT_ENA_REG(i2s_no),I2S_OUT_EOF_INT_CLR|I2S_OUT_DONE_INT_CLR|I2S_IN_SUC_EOF_INT_CLR|I2S_IN_DONE_INT_CLR);
}

void i2s_reset(unsigned int i2s_no)
{
    CLEAR_PERI_REG_MASK(I2SCONF_REG(i2s_no),I2S_RX_FIFO_RESET|I2S_TX_FIFO_RESET|I2S_RX_RESET|I2S_TX_RESET);
    SET_PERI_REG_MASK(I2SCONF_REG(i2s_no),I2S_RX_FIFO_RESET|I2S_TX_FIFO_RESET|I2S_RX_RESET|I2S_TX_RESET);
    CLEAR_PERI_REG_MASK(I2SCONF_REG(i2s_no),I2S_RX_FIFO_RESET|I2S_TX_FIFO_RESET|I2S_RX_RESET|I2S_TX_RESET);
}
void i2s_dma_rx(unsigned int i2s_no,unsigned int byte_len, unsigned int bit_mode, unsigned int channel_mode)                                                   
{
    unsigned int flag;
    unsigned int link_start_addr;
    unsigned int value;
    pchain link;
    i2s_clk_install(i2s_no);
    SET_PERI_REG_BITS(I2SCONF2_REG(i2s_no), 0x1, 1, I2S_LCD_EN_S);
    i2s_rx_init(i2s_no,bit_mode,channel_mode);
    i2s_reset(i2s_no);
    WRITE_PERI_REG(I2SRXEOF_NUM_REG(i2s_no),byte_len);
    link = (pchain)malloc(sizeof(pchain));
    if(NULL == link){
        printinfo("link is NULL\n",0);
        fail("link is NULL\n");
    }
    // link initial
    link_init(link,rx_buffer,sizeof(rx_buffer));
    link_start_addr = (unsigned int)link;
    value = (1<<29)|(link_start_addr & 0xFFFFF);
    WRITE_PERI_REG(I2SIN_LINK_REG(i2s_no),value);//enable pop

    //reset
    SET_PERI_REG_BITS( I2SCONF_REG(i2s_no),0x1,0x1,I2S_RX_START_S);
    while( 1 ) {
        if (READ_PERI_REG(I2SINT_RAW_REG(i2s_no)) & 0x300) { //wait rx eof
            break;
        }
    }
}
