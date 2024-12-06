#ifndef SIM_SPI_CONFIG_H_INCLUDED
#define SIM_SPI_CONFIG_H_INCLUDED

#include "./gpio.h"
#include "./gpio_reg.h"
#include "./io_mux_reg.h"
#include "./gpio_sig_map.h"
#include "./system_reg.h"

#define REG_BIT_READ(addr,s)    ( *(volatile unsigned int *)(addr) >> (s) )
#define APB_IO_MUX_ADDR_PRE     ( REG_IO_MUX_BASE )

unsigned int dummy_delay = 0;
void sim_mtrx(unsigned int mode ){
//    WRITE_PERI_REG(GPIO_ENABLE_REG,0x3f0000);                    //gpio16,17,18,19,20,21 enable 
//    if(mode == 0){
//        SET_PERI_REG_BITS(APB_IO_MUX_ADDR_PRE+0x4C,0x1,0x1,8);
//        WRITE_PERI_REG(GPIO_FUNC16_OUT_SEL_CFG_REG,0);               //CLK(GPIO16)
//    }else if(mode ==1){//
//        SET_PERI_REG_BITS(APB_IO_MUX_ADDR_PRE+0x60,0x7,0x1,12);  // pad clk(SD_CLK)
//    }
//
//    SET_PERI_REG_BITS(APB_IO_MUX_ADDR_PRE+0x50,0x1,0x1,8);
//    WRITE_PERI_REG(GPIO_FUNC17_OUT_SEL_CFG_REG,1);               //Q
//    SET_PERI_REG_BITS(GPIO_FUNC1_IN_SEL_CFG_REG,0xff,128+17,0);
//
//    SET_PERI_REG_BITS(APB_IO_MUX_ADDR_PRE+0x70,0x1,0x1,8);   //
//    WRITE_PERI_REG(GPIO_FUNC18_OUT_SEL_CFG_REG,2);               //D
//    SET_PERI_REG_BITS(GPIO_FUNC2_IN_SEL_CFG_REG,0xff,128+18,0);
//
//    SET_PERI_REG_BITS(APB_IO_MUX_ADDR_PRE+0x74,0x1,0x1,8);   // 
//    WRITE_PERI_REG(GPIO_FUNC19_OUT_SEL_CFG_REG,3);               //HD
//    SET_PERI_REG_BITS(GPIO_FUNC3_IN_SEL_CFG_REG,0xff,128+19,0);
//
//    SET_PERI_REG_BITS(APB_IO_MUX_ADDR_PRE+0x74,0x1,0x1,8);   //
//    WRITE_PERI_REG(GPIO_FUNC20_OUT_SEL_CFG_REG,4);               //wp
//    SET_PERI_REG_BITS(GPIO_FUNC4_IN_SEL_CFG_REG,0xff,128+20,0);
//
//    SET_PERI_REG_BITS(APB_IO_MUX_ADDR_PRE+0x74,0x1,0x1,8);   //
//    WRITE_PERI_REG(GPIO_FUNC21_OUT_SEL_CFG_REG,5);               // CS
}

void sim_spi_pad_init(unsigned int spi_no,unsigned int mst_mode) {
    if(spi_no == 0 | spi_no == 1){
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
    else if(spi_no == 2){
	PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO34_U,FUNC_GPIO34_FSPICS0);// pad cs(CMD)
	PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO36_U,FUNC_GPIO36_FSPICLK);// pad clk(CLK)
	PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO35_U,FUNC_GPIO35_FSPID);  // pad data1(d)
	PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO37_U,FUNC_GPIO37_FSPIQ);  // pad data0(q)
	PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO38_U,FUNC_GPIO38_FSPIWP); // pad WP(data3)
	PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO33_U,FUNC_GPIO33_FSPIHD); // pad HD(data2)     
      if (mst_mode) {
        SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO35_U,FUN_IE);
        SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO37_U,FUN_IE);
        SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO38_U,FUN_IE);
        SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO33_U,FUN_IE);
        SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO34_U,FUN_IE);
        SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO36_U,FUN_IE);
      }else {
        SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO35_U,FUN_IE);
        CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO37_U,FUN_IE);

        SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO38_U,FUN_IE);
        SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO33_U,FUN_IE);
        SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO34_U,FUN_IE);
        SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO36_U,FUN_IE);
      }
    }
    else if(spi_no == 3){
      if (mst_mode) {
          gpio_matrix_out(12,SPI3_CLK_OUT_MUX_IDX, 0,0); //clk, 
          gpio_matrix_out(11,SPI3_D_OUT_IDX,       0,0);  //D, 
          gpio_matrix_out(10,SPI3_CS0_OUT_IDX,     0,0); //CMD / CS, 
          gpio_matrix_in(13,SPI3_Q_IN_IDX,   0);  //Q, 

          gpio_pad_select_gpio(10);
          gpio_pad_select_gpio(11);
          gpio_pad_ie_set(11);    // for sio simulation.
          gpio_pad_select_gpio(12);
          gpio_pad_select_gpio(13);
          gpio_pad_ie_set(13);  
      }else {
          gpio_matrix_out(13,SPI3_Q_OUT_IDX,       0,0);  //Q, 
          gpio_matrix_in(12,SPI3_CLK_IN_IDX, 0); //clk, 
          gpio_matrix_in(11,SPI3_D_IN_IDX,   0);  //D, 
          gpio_matrix_in(10,SPI3_CS0_IN_IDX, 0); //CMD / CS, 

          gpio_pad_ie_set(10);
          gpio_pad_select_gpio(10);
          gpio_pad_select_gpio(11);
          gpio_pad_ie_set(11);
          gpio_pad_select_gpio(12);
          gpio_pad_ie_set(12);
          gpio_pad_select_gpio(13);
      }
         // gpio_matrix_out(12,SPI3_CLK_OUT_MUX_IDX, 0,0); //clk, 
         // gpio_matrix_out(13,SPI3_Q_OUT_IDX,       0,0);  //Q, 
         // gpio_matrix_out(11,SPI3_D_OUT_IDX,       0,0);  //D, 
         // gpio_matrix_out(10,SPI3_CS0_OUT_IDX,     0,0); //CMD / CS, 

         // gpio_matrix_in(12,SPI3_CLK_IN_IDX, 0); //clk, 
         // gpio_matrix_in(13,SPI3_Q_IN_IDX,   0);  //Q, 
         // gpio_matrix_in(11,SPI3_D_IN_IDX,   0);  //D, 
         // gpio_matrix_in(10,SPI3_CS0_IN_IDX, 0); //CMD / CS, 

         // gpio_pad_ie_set(10);
         // gpio_pad_select_gpio(10);
         // gpio_pad_select_gpio(11);
         // gpio_pad_ie_set(11);
         // gpio_pad_select_gpio(12);
         // gpio_pad_ie_set(12);
         // gpio_pad_select_gpio(13);
         // gpio_pad_ie_set(13);
    }
}

void sim_spi234_pad_init(unsigned int spi_no,unsigned int mst_mode)
{
    gpio_pad_pullup(10);
    if(spi_no == 2){
	PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO34_U,FUNC_GPIO34_FSPICS0);// pad cs(CMD)
	PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO36_U,FUNC_GPIO36_FSPICLK);// pad clk(CLK)
	PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO35_U,FUNC_GPIO35_FSPID);  // pad data1(d)
	PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO37_U,FUNC_GPIO37_FSPIQ);  // pad data0(q)
	PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO38_U,FUNC_GPIO38_FSPIWP); // pad WP(data3)
	PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO33_U,FUNC_GPIO33_FSPIHD); // pad HD(data2)     

        SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO34_U, FUN_PU);
        CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO34_U, FUN_PD);

        if (mst_mode) {
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO37_U,FUN_IE);
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO38_U,FUN_IE);
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO33_U,FUN_IE);
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO35_U,FUN_IE);

            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO34_U,FUN_IE);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO36_U,FUN_IE);
        }else {
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO35_U,FUN_IE);
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO37_U,FUN_IE);
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO38_U,FUN_IE);
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO33_U,FUN_IE);
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO34_U,FUN_IE);
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO36_U,FUN_IE);
      }
    } else if(spi_no == 3){
        if (mst_mode) {
            gpio_matrix_out(12,SPI3_CLK_OUT_MUX_IDX, 0,0); //clk, 
            gpio_matrix_out(10,SPI3_CS0_OUT_IDX,     0,0); //CMD / CS, 
            gpio_matrix_out(11,SPI3_D_OUT_IDX,       0,0);  //D, 
          //  gpio_matrix_in(11,SPI3_D_IN_IDX,           0);  //D, for sio simulation 
            gpio_matrix_in(13,SPI3_Q_IN_IDX,           0);  //Q, 

            gpio_pad_select_gpio(10);
            gpio_pad_select_gpio(11);
          //  gpio_pad_ie_set(11);    // for sio simulation.
            gpio_pad_select_gpio(12);
            gpio_pad_select_gpio(13);
            gpio_pad_ie_set(13);

	    gpio_matrix_out(13, SPI3_Q_OUT_IDX, 0,0);   //reset GM
            gpio_matrix_in(12,  SPI3_CLK_IN_IDX, 0);   //reset GM
            gpio_matrix_in(11,  SPI3_D_IN_IDX, 0);   //reset GM
            gpio_matrix_in(10,  SPI3_CS0_IN_IDX, 0);   //reset GM
	    gpio_pad_pullup(10);
	    gpio_pad_pullup(11);
	    gpio_pad_pullup(12);
	    gpio_pad_pullup(13);
        }else {
            gpio_matrix_out(13,SPI3_Q_OUT_IDX,       0,0);  //Q, 
          //  gpio_matrix_out(11,SPI3_D_OUT_IDX,       0,0);  //D, for sio simulation
            gpio_matrix_in(12,SPI3_CLK_IN_IDX, 0); //clk, 
            gpio_matrix_in(11,SPI3_D_IN_IDX,   0);  //D, 
            gpio_matrix_in(10,SPI3_CS0_IN_IDX, 0); //CMD / CS, 

            gpio_pad_select_gpio(10);
            gpio_pad_ie_set(10);
            gpio_pad_select_gpio(11);
           // gpio_pad_ie_set(11);        //for sio simulation
            gpio_pad_select_gpio(12);
            gpio_pad_ie_set(12);
            gpio_pad_select_gpio(13);

	    gpio_matrix_in(13,  SPI3_Q_IN_IDX, 0);   //reset GM
            gpio_matrix_out(12, SPI3_CLK_OUT_MUX_IDX, 0, 0);   //reset GM
            gpio_matrix_out(11, SPI3_D_OUT_IDX, 0, 0);   //reset GM
            gpio_matrix_out(10, SPI3_CS0_OUT_IDX, 0, 0);   //reset GM	    
        }
    } else if(spi_no == 4){
        SET_PERI_REG_MASK(SYSTEM_SPI_SHARED_DMA_SEL_REG,SYSTEM_SPI_SHARED_DMA_SEL);//spi4 uses dma
        if (mst_mode) {
            gpio_matrix_out(12,SPI4_CLK_OUT_MUX_IDX, 0,0); //clk, 
            gpio_matrix_out(11,SPI4_D_OUT_IDX,       0,0);  //D, 
            gpio_matrix_out(10,SPI4_CS0_OUT_IDX,     0,0); //CMD / CS, 
           // gpio_matrix_in (11,SPI4_D_IN_IDX,        0);  //D, for sio simulation
            gpio_matrix_in (13,SPI4_Q_IN_IDX,        0);  //Q, input 

            gpio_pad_select_gpio(10);
            gpio_pad_select_gpio(11);
           // gpio_pad_ie_set(11);    // for sio simulation.
            gpio_pad_select_gpio(12);
            gpio_pad_select_gpio(13);
            gpio_pad_ie_set(13);

            gpio_matrix_out(13, SPI4_Q_OUT_IDX,      0,0);   //reset GM
            gpio_matrix_in(12,  SPI4_CLK_IN_IDX, 0);   //reset GM
            gpio_matrix_in(11,  SPI4_D_IN_IDX,       0);   //reset GM
            gpio_matrix_in(10,  SPI4_CS0_IN_IDX,     0);   //reset GM
        }else {
            gpio_matrix_out(13,SPI4_Q_OUT_IDX,  0,0);  //Q, output 
            //gpio_matrix_out(11,SPI4_D_OUT_IDX,  0,0);  //D,for sio simulation  
            gpio_matrix_in (12,SPI4_CLK_IN_IDX, 0); //clk, 
            gpio_matrix_in (11,SPI4_D_IN_IDX,   0);  //D, 
            gpio_matrix_in (10,SPI4_CS0_IN_IDX, 0); //CMD / CS, 

            gpio_pad_select_gpio(10);
            gpio_pad_ie_set(10);//ie: set GPIO input enable; oe: set GPIO output enable.
            gpio_pad_select_gpio(11);
           // gpio_pad_ie_set(11);
            gpio_pad_select_gpio(12);
            gpio_pad_ie_set(12);
            gpio_pad_select_gpio(13);

	    gpio_matrix_in(13,  SPI4_Q_IN_IDX     , 0);   //reset GM
            gpio_matrix_out(12, SPI4_CLK_OUT_MUX_IDX, 0, 0);   //reset GM
            gpio_matrix_out(11, SPI4_D_OUT_IDX      , 0, 0);   //reset GM
            gpio_matrix_out(10, SPI4_CS0_OUT_IDX    , 0, 0);   //reset GM
	    
        }
   }
}

void sim_spi34_pad_init(unsigned int spi_no,unsigned int mst_mode)
{
    gpio_pad_pullup(10);
    gpio_pad_pullup(34);

    if(spi_no == 3){
        if (mst_mode) {
            gpio_matrix_out(36,SPI3_CLK_OUT_MUX_IDX, 0,0); //clk, 
            gpio_matrix_out(34,SPI3_CS0_OUT_IDX,     0,0); //CMD / CS, 
            gpio_matrix_out(35,SPI3_D_OUT_IDX,       0,0);  //D, 
          //  gpio_matrix_in(35,SPI3_D_IN_IDX,           0);  //D, for sio simulation 
            gpio_matrix_in(37,SPI3_Q_IN_IDX,           0);  //Q, 

            gpio_pad_select_gpio(34);
            gpio_pad_select_gpio(35);
          //  gpio_pad_ie_set(35);    // for sio simulation.
            gpio_pad_select_gpio(36);
            gpio_pad_select_gpio(37);
            gpio_pad_ie_set(37);

	    gpio_matrix_out(37, SPI3_Q_OUT_IDX, 0,0);   //reset GM
            gpio_matrix_in(36,  SPI3_CLK_IN_IDX, 0);   //reset GM
            gpio_matrix_in(35,  SPI3_D_IN_IDX, 0);   //reset GM
            gpio_matrix_in(34,  SPI3_CS0_IN_IDX, 0);   //reset GM
        }else {
            gpio_matrix_out(37,SPI3_Q_OUT_IDX,       0,0);  //Q, 
          //  gpio_matrix_out(35,SPI3_D_OUT_IDX,       0,0);  //D, for sio simulation
            gpio_matrix_in(36,SPI3_CLK_IN_IDX, 0); //clk, 
            gpio_matrix_in(35,SPI3_D_IN_IDX,   0);  //D, 
            gpio_matrix_in(34,SPI3_CS0_IN_IDX, 0); //CMD / CS, 

            gpio_pad_select_gpio(34);
            gpio_pad_ie_set(34);
            gpio_pad_select_gpio(35);
           // gpio_pad_ie_set(35);        //for sio simulation
            gpio_pad_select_gpio(36);
            gpio_pad_ie_set(36);
            gpio_pad_select_gpio(37);

	    gpio_matrix_in(37,  SPI3_Q_IN_IDX, 0);   //reset GM
            gpio_matrix_out(36, SPI3_CLK_OUT_MUX_IDX, 0, 0);   //reset GM
            gpio_matrix_out(35, SPI3_D_OUT_IDX, 0, 0);   //reset GM
            gpio_matrix_out(34, SPI3_CS0_OUT_IDX, 0, 0);   //reset GM	    	    
        }
    } else if(spi_no == 4){
        SET_PERI_REG_MASK(SYSTEM_SPI_SHARED_DMA_SEL_REG,SYSTEM_SPI_SHARED_DMA_SEL);//spi4 uses dma
        if (mst_mode) {
            gpio_matrix_out(12,SPI4_CLK_OUT_MUX_IDX, 0,0); //clk, 
            gpio_matrix_out(11,SPI4_D_OUT_IDX,       0,0);  //D, 
            gpio_matrix_out(10,SPI4_CS0_OUT_IDX,     0,0); //CMD / CS, 
           // gpio_matrix_in (11,SPI4_D_IN_IDX,        0);  //D, for sio simulation
            gpio_matrix_in (13,SPI4_Q_IN_IDX,        0);  //Q, input 

            gpio_pad_select_gpio(10);
            gpio_pad_select_gpio(11);
           // gpio_pad_ie_set(11);    // for sio simulation.
            gpio_pad_select_gpio(12);
            gpio_pad_select_gpio(13);
            gpio_pad_ie_set(13);

            gpio_matrix_out(13, SPI4_Q_OUT_IDX,      0,0);   //reset GM
            gpio_matrix_in(12,  SPI4_CLK_IN_IDX, 0);   //reset GM
            gpio_matrix_in(11,  SPI4_D_IN_IDX,       0);   //reset GM
            gpio_matrix_in(10,  SPI4_CS0_IN_IDX,     0);   //reset GM

        }else {
            gpio_matrix_out(13,SPI4_Q_OUT_IDX,  0,0);  //Q, output 
            //gpio_matrix_out(11,SPI4_D_OUT_IDX,  0,0);  //D,for sio simulation  
            gpio_matrix_in (12,SPI4_CLK_IN_IDX, 0); //clk, 
            gpio_matrix_in (11,SPI4_D_IN_IDX,   0);  //D, 
            gpio_matrix_in (10,SPI4_CS0_IN_IDX, 0); //CMD / CS, 

            gpio_pad_select_gpio(10);
            gpio_pad_ie_set(10);//ie: set GPIO input enable; oe: set GPIO output enable.
            gpio_pad_select_gpio(11);
           // gpio_pad_ie_set(11);
            gpio_pad_select_gpio(12);
            gpio_pad_ie_set(12);
            gpio_pad_select_gpio(13);

	    gpio_matrix_in(13,  SPI4_Q_IN_IDX     , 0);   //reset GM
            gpio_matrix_out(12, SPI4_CLK_OUT_MUX_IDX, 0, 0);   //reset GM
            gpio_matrix_out(11, SPI4_D_OUT_IDX      , 0, 0);   //reset GM
            gpio_matrix_out(10, SPI4_CS0_OUT_IDX    , 0, 0);   //reset GM
        }
   }
}

void sim_spi_clk_config(unsigned int spi_no,unsigned int pre_div,unsigned int div){
    unsigned int temp;
    if(div>1){
        temp = ((div-1)<<SPI_CLKCNT_N_S)|
               (((div>>1)-1)<<SPI_CLKCNT_H_S)|
               ((div-1)<<SPI_CLKCNT_L_S); 
        temp |= (pre_div<<SPI_CLKDIV_PRE_S);
    }else{
        temp = (0x1<<SPI_CLK_EQU_SYSCLK_S);
    }
    WRITE_PERI_REG(SPI_CLOCK_REG(spi_no),temp);
}

void sim_spi_write_init(unsigned int spi_no,unsigned int mode) {
    if(mode==0) { //master
        SET_PERI_REG_BITS(SPI_SLAVE_REG(spi_no),0x1,mode,SPI_SLAVE_MODE_S); // master mode
    
        SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x0,SPI_CS_HOLD_S);      // cs_hold
        SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x1,SPI_CS_SETUP_S);     // cs_setup
    
        SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x1,SPI_USR_MOSI_S);     // usr_dout
        SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x0,SPI_USR_MISO_S);     // usr_din
        SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x0,SPI_USR_DUMMY_S);    // usr_dummy
        SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x1,SPI_USR_ADDR_S);     // usr_addr
    
        SET_PERI_REG_BITS(SPI_CTRL2_REG(spi_no),0x7,0x0,SPI_CS_DELAY_NUM_S);            //CS delay num
    
        SET_PERI_REG_BITS(SPI_USER1_REG(spi_no),0xff,0x0,SPI_USR_DUMMY_CYCLELEN_S);     // usr_dummy_cyclelen
        SET_PERI_REG_BITS(SPI_USER1_REG(spi_no),0x3f,0x17,SPI_USR_ADDR_BITLEN_S);   // usr_addr_bitlen
    
        SET_PERI_REG_BITS(SPI_MISO_DLEN_REG(spi_no),SPI_USR_MISO_DBITLEN,0xff,SPI_USR_MISO_DBITLEN_S);  // usr_din_bitlen
        SET_PERI_REG_BITS(SPI_MOSI_DLEN_REG(spi_no),SPI_USR_MOSI_DBITLEN,0xff,SPI_USR_MOSI_DBITLEN_S);  // usr_dout_bitlen
    
        SET_PERI_REG_BITS(SPI_USER2_REG(spi_no),SPI_USR_COMMAND_BITLEN,0x7,SPI_USR_COMMAND_BITLEN_S);   // usr_command_bitlen
        SET_PERI_REG_BITS(SPI_USER2_REG(spi_no),SPI_USR_COMMAND_VALUE,0x2,SPI_USR_COMMAND_VALUE_S);     // usr_command_value
    }else {//slave
        SET_PERI_REG_BITS(SPI_SLAVE_REG(spi_no),0x1,0x1,SPI_SLAVE_MODE_S);          // slave mode(should be configured firstly)
        SET_PERI_REG_BITS(SPI_CLOCK_REG(spi_no),0x3f,0x0,SPI_CLKCNT_H_S);           // clkcnt_H
        SET_PERI_REG_BITS(SPI_CLOCK_REG(spi_no),0x3f,0x0,SPI_CLKCNT_L_S);           // clkcnt_L
    
        SET_PERI_REG_BITS(SPI_CTRL2_REG(spi_no),0x7,0x0,SPI_CS_DELAY_NUM_S);        //CS delay num
           
        SET_PERI_REG_BITS(SPI_CMD_REG(spi_no),0x1,0x1,SPI_USR_S);                   // spi_usr 
    
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_USR_MOSI_S);             // usr_dout
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x1,SPI_USR_MISO_S);             // usr_din
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_USR_DUMMY_S);            // usr_dummy
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x1,SPI_USR_ADDR_S);             // usr_addr
    
      //  SET_PERI_REG_BITS(SPI_SLAVE1_REG(spi_no),0x3f,0x17,SPI_SLV_RD_ADDR_BITLEN_S); //slv_rd_addr_bitlen                  
      //  SET_PERI_REG_BITS(SPI_SLAVE1_REG(spi_no),0x3f,0x17,SPI_SLV_WR_ADDR_BITLEN_S); //slv_wr_addr_bitlen
    }
}

void sim_spi_read_init(unsigned int spi_no,unsigned int mode) {
    if(mode==0) { //master
        SET_PERI_REG_BITS(SPI_SLAVE_REG(spi_no),0x1,mode,SPI_SLAVE_MODE_S);         // master mode
        SET_PERI_REG_BITS(SPI_CLOCK_REG(spi_no),0x1,0x0,SPI_CLK_EQU_SYSCLK_S);      // clkdiv_0
    
        SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x0,SPI_CS_HOLD_S);          // cs_hold
        SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x1,SPI_CS_SETUP_S);         // cs_setup
    
        SET_PERI_REG_BITS(SPI_CTRL2_REG(spi_no),0x7,0x0,SPI_CS_DELAY_NUM_S);            //CS delay num
    
        SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x0,SPI_USR_MOSI_S);         // usr_dout
        SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x1,SPI_USR_MISO_S);         // usr_din
        SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x0,SPI_USR_DUMMY_S);        // usr_dummy
        SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x1,SPI_USR_ADDR_S);         // usr_addr
    
        SET_PERI_REG_BITS(SPI_USER1_REG(spi_no),0xff,0x3,SPI_USR_DUMMY_CYCLELEN_S);     // usr_dummy_cyclelen
        SET_PERI_REG_BITS(SPI_USER1_REG(spi_no),0x3f,0x17,SPI_USR_ADDR_BITLEN_S);   // usr_addr_bitlen
    
        SET_PERI_REG_BITS(SPI_MISO_DLEN_REG(spi_no),SPI_USR_MISO_DBITLEN,0xff,SPI_USR_MISO_DBITLEN_S);  // usr_din_bitlen
        SET_PERI_REG_BITS(SPI_MOSI_DLEN_REG(spi_no),SPI_USR_MOSI_DBITLEN,0xff,SPI_USR_MOSI_DBITLEN_S);  // usr_dout_bitlen
    
    
        SET_PERI_REG_BITS(SPI_USER2_REG(spi_no),SPI_USR_COMMAND_BITLEN,0x7,SPI_USR_COMMAND_BITLEN_S);   // usr_command_bitlen
        SET_PERI_REG_BITS(SPI_USER2_REG(spi_no),SPI_USR_COMMAND_VALUE,0x3,SPI_USR_COMMAND_VALUE_S);     // usr_command_value
    }else {//slave
        SET_PERI_REG_BITS(SPI_SLAVE_REG(spi_no),0x1,0x1,SPI_SLAVE_MODE_S);          // slave mode(should be configured firstly)
    
        SET_PERI_REG_BITS(SPI_CLOCK_REG(spi_no),0x3f,0x0,SPI_CLKCNT_H_S);           //clkcnt_H
        SET_PERI_REG_BITS(SPI_CLOCK_REG(spi_no),0x3f,0x0,SPI_CLKCNT_L_S);           //clkcnt_L
    
        SET_PERI_REG_BITS(SPI_CTRL2_REG(spi_no),0x7,0x0,SPI_CS_DELAY_NUM_S);                    //CS delay num
    
        SET_PERI_REG_BITS(SPI_CMD_REG(spi_no),0x1,0x1,SPI_USR_S);                   // spi_usr 
    
        SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x1,SPI_USR_MOSI_S);             // usr_dout
        SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x0,SPI_USR_MISO_S);             // usr_din
        SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x0,SPI_USR_DUMMY_S);            // usr_dummy
        SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x1,SPI_USR_ADDR_S);             // usr_addr
    
       // SET_PERI_REG_BITS(SPI_SLAVE1_REG(spi_no),0x3f,0x17,SPI_SLV_RD_ADDR_BITLEN_S);           //slv1,slv_rd_addr_bitlen                  
       // SET_PERI_REG_BITS(SPI_SLAVE1_REG(spi_no),0x3f,0x17,SPI_SLV_WR_ADDR_BITLEN_S);           //slv_wr_addr_bitlen
    }
}

void sim_spi_read_flash_init(unsigned int spi_no) {
//flash config
    SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x0,27);             // usr_dout
    SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x1,28);             // usr_din
    SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x1,29);             // usr_dummy
    SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x1,30);             // usr_addr

    SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x1,SPI_FREAD_QUAD_S);        
    SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x1,SPI_FADDR_QUAD_S);        

    SET_PERI_REG_BITS(SPI_USER1_REG(spi_no),0xff,0x3,SPI_USR_DUMMY_CYCLELEN_S);     // usr_dummy_cyclelen
    SET_PERI_REG_BITS(SPI_USER1_REG(spi_no),0x3f,0x17,SPI_USR_ADDR_BITLEN_S);       // addr_bitlen

//  SET_PERI_REG_BITS(SPI_MOSI_DLEN_REG(spi_no),0xffffff,0xFF,0);       // usr_dout_bitlen
    SET_PERI_REG_BITS(SPI_MISO_DLEN_REG(spi_no),0xffffff,0xFF,0);       // usr_din_bitlen

    SET_PERI_REG_BITS(SPI_USER2_REG(spi_no),0xffffffff,0x700000EB,0);   // usr_command_bitlen, usr_command_value
}

void sim_spi_write_flash_init(unsigned int spi_no) {
//flash config
//  sim_spi_wrst_qe(spi_no);

    SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x1,SPI_FREAD_QUAD_S);        
    SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x1,SPI_FADDR_QUAD_S); 
    SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x1,27);             // usr_dout
    SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x0,28);             // usr_din
    SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x0,29);             // usr_dummy
    SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x1,30);             // usr_addr

    SET_PERI_REG_BITS(SPI_USER1_REG(spi_no),0xff,0x5,0);            // usr_dummy_cyclelen
    SET_PERI_REG_BITS(SPI_USER1_REG(spi_no),0x3f,0x17,26);              // addr_bitlen

    SET_PERI_REG_BITS(SPI_MOSI_DLEN_REG(spi_no),0xffffff,0x3F,0);       // usr_dout_bitlen
    SET_PERI_REG_BITS(SPI_MISO_DLEN_REG(spi_no),0xffffff,0x3F,0);       // usr_din_bitlen

    SET_PERI_REG_BITS(SPI_USER2_REG(spi_no),0xffffffff,0x700000eb,0);           // usr_command_bitlen, usr_command_value
}


void sim_spi_master_read_init(unsigned int spi_no) {
    SET_PERI_REG_BITS(SPI_SLAVE_REG(spi_no),0x1,0x0,30);            // master mode
    SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x1,3);          // cs_hold
    SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x1,4);          // cs_setup
    sim_spi_pad_init(spi_no,1);
//flash config
    sim_spi_read_flash_init(spi_no);
}

void sim_spi_master_write_init(unsigned int spi_no) {
    SET_PERI_REG_BITS(SPI_SLAVE_REG(spi_no),0x1,0x0,30);            // master mode

    SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x1,3);          // cs_hold
    SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x1,4);          // cs_setup
    sim_spi_pad_init(spi_no,1);
//flash config
    sim_spi_write_flash_init(spi_no);
}
unsigned int sim_spi_master_read(unsigned int spi_no, unsigned int addr ) {
    unsigned int temp;
    SET_PERI_REG_BITS(SPI_ADDR_REG(spi_no),0xffffffff,addr,0);  // usr_addr_value
    temp = READ_PERI_REG(addr);

    return  temp;
}

void sim_spi_read(unsigned int spi_no , unsigned int addr , unsigned int len) {
    SET_PERI_REG_BITS(SPI_ADDR_REG(spi_no),SPI_USR_ADDR_VALUE,(addr|(len<<24)),SPI_USR_ADDR_VALUE_S);   // usr_addr_value
    SET_PERI_REG_BITS(SPI_CMD_REG(spi_no),0x1,0x1,SPI_USR_S);              // reg_usr
    while(( REG_BIT_READ(SPI_SLAVE_REG(spi_no),SPI_USR_S) ) & 1 );
}

void sim_spi_write(unsigned int spi_no , unsigned int addr, unsigned int data ,unsigned int len) {
    SET_PERI_REG_BITS(SPI_ADDR_REG(spi_no),SPI_USR_ADDR_VALUE,(addr|(len<<24)),SPI_USR_ADDR_VALUE_S);   // usr_addr_value
    SET_PERI_REG_BITS(SPI_W0_REG(spi_no),SPI_BUF0,data,SPI_BUF0_S);                // reg_buf[0]
    SET_PERI_REG_BITS(SPI_CMD_REG(spi_no),0x1,0x1,SPI_USR_S);              // reg_usr
    while( 1 ) {                               // trans_done
        if( ( REG_BIT_READ(SPI_SLAVE_REG(spi_no),SPI_TRANS_DONE_S) ) & 1 ) {
            SET_PERI_REG_BITS(SPI_SLAVE_REG(spi_no),0x1,0x0,SPI_TRANS_DONE_S);
            break;
        }
    }
}

void sim_spi_encrypt_init(unsigned int spi_no) {
    sim_spi_clk_config(spi_no,0,4);//20Mhz
    SET_PERI_REG_BITS(SPI_SLAVE_REG(spi_no),0x1,0x0,SPI_SLAVE_MODE_S);      // master mode

    SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x0,SPI_CS_HOLD_S);          // cs_hold
    SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x1,SPI_CS_SETUP_S);         // cs_setup

    SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x1,SPI_USR_MOSI_S);         // usr_dout
    SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x0,SPI_USR_MISO_S);         // usr_din
    SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x0,SPI_USR_DUMMY_S);        // usr_dummy
    SET_PERI_REG_BITS(SPI_USER_REG(spi_no),0x1,0x1,SPI_USR_ADDR_S);         // usr_addr

    SET_PERI_REG_BITS(SPI_USER1_REG(spi_no),0xff,0x0,SPI_USR_DUMMY_CYCLELEN_S);     // usr_dummy_cyclelen
    SET_PERI_REG_BITS(SPI_USER1_REG(spi_no),0x3f,0x17,SPI_USR_ADDR_BITLEN_S);   // usr_addr_bitlen

    SET_PERI_REG_BITS(SPI_MISO_DLEN_REG(spi_no),SPI_USR_MISO_DBITLEN,0xff,SPI_USR_MISO_DBITLEN_S);  // usr_din_bitlen
    SET_PERI_REG_BITS(SPI_MOSI_DLEN_REG(spi_no),SPI_USR_MOSI_DBITLEN,0xff,SPI_USR_MOSI_DBITLEN_S);  // usr_dout_bitlen

    SET_PERI_REG_BITS(SPI_USER2_REG(spi_no),SPI_USR_COMMAND_BITLEN,0x7,SPI_USR_COMMAND_BITLEN_S);   // usr_command_bitlen
    SET_PERI_REG_BITS(SPI_USER2_REG(spi_no),SPI_USR_COMMAND_VALUE,0x2,SPI_USR_COMMAND_VALUE_S);     // usr_command_value
}

void pick_up_hspi_flash(unsigned int loop){
    unsigned int i,j;
    unsigned int trans_done;
    unsigned int last_flag;
    unsigned int read_data;
    last_flag =0;
    trans_done =0;
    for(i=0;i<loop;i++){
        printinfo("loop is \n",last_flag);
        sim_spi_read(2,0x00000000+i*4*8,8*4);//addr
        for(j=0;j<8;j++){
            read_data = READ_PERI_REG(REG_SPI_BASE(2)+0x40+j*4);
            WRITE_PERI_REG(0x40040000+i*8*4+j*4,read_data);//write the data to iram
        }
    }
}

void pick_up_flash(unsigned int loop){
    unsigned int i,j;
    unsigned int trans_done;
    unsigned int last_flag;
    unsigned int read_data;
    last_flag =0;
    trans_done =0;
    for(i=0;i<loop;i++){
        printinfo("loop is \n",last_flag);
        sim_spi_read(3,0x00000000+i*4*8,8*4);//addr
        for(j=0;j<8;j++){
            read_data = READ_PERI_REG(REG_SPI_BASE(3)+0x40+j*4);
            WRITE_PERI_REG(0x40040000+i*8*4+j*4,read_data);//write the data to iram
        }
    }
}

void spi_flash_line_mode(unsigned int spi_no, unsigned int mode){
//    while((SPI_EXT2_REG(0) & 0x7) != 0);
    //SET_PERI_REG_BITS(SPI_CACHE_FCTRL_REG(0),0x1,0x0,SPI_CACHE_REQ_EN_S);   // ahb_spi_req_en
    if(mode == 0){//slow mode, line1           03H
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FAST_RD_MODE_S);  // fast_read_en
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FADDR_QUAD_S);    // faddr_quad
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FADDR_DUAL_S);    // faddr_dual    
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_QUAD_S);    // fread_qout
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_DUAL_S);    // fread_dout
    }else if(mode == 1){//fast mode, line1     0BH
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x1,SPI_FAST_RD_MODE_S);  // fast_read_en
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FADDR_QUAD_S);    // faddr_quad
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FADDR_DUAL_S);    // faddr_dual  
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_QUAD_S);    // fread_qout
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_DUAL_S);    // fread_dout
    }else if(mode == 2){//fast mode, line2(dout) 3BH
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x1,SPI_FAST_RD_MODE_S);  // fast_read_en
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FADDR_QUAD_S);    // faddr_quad
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FADDR_DUAL_S);    // faddr_dual  
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_QUAD_S);    // fread_qout  
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x1,SPI_FREAD_DUAL_S);    // fread_dout
    }else if(mode == 3){//fast mode, line2(dio)  BBH
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x1,SPI_FAST_RD_MODE_S);  // fast_read_en
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FADDR_QUAD_S);    // faddr_quad
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x1,SPI_FADDR_DUAL_S);    // faddr_dual   
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_QUAD_S);    // fread_qout  
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x1,SPI_FREAD_DUAL_S);    // fread_dout
    }else if(mode == 4){//fast mode lin4(qout)   6BH
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x1,SPI_FAST_RD_MODE_S);  // fast_read_en
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FADDR_QUAD_S);    // faddr_quad
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FADDR_DUAL_S);    // faddr_dual  
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x1,SPI_FREAD_QUAD_S);    // fread_qout  
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_DUAL_S);    // fread_dout
    }else if(mode == 5){//fast mode lin4(qio)    EBH
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x1,SPI_FAST_RD_MODE_S);  // fast_read_en
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x1,SPI_FADDR_QUAD_S);    // faddr_quad
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FADDR_DUAL_S);    // faddr_dual    
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x1,SPI_FREAD_QUAD_S);    // fread_qout  
        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_DUAL_S);    // fread_dout
   // }else if(mode == 6){//fast mode line 8 (STR oct)
   //    // SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FAST_RD_MODE_S);       // fast_read_en
   //     SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_QIO_S);    // fread_qio   
   //     SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_DIO_S);    // fread_dio   
   //     SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_QUAD_S);        // fread_qout  
   //     SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_DUAL_S);   // fread_dout
   //   //  SET_PERI_REG_BITS(SPI_CACHE_FCTRL_REG(spi_no),0x1,0x1,SPI_CACHE_FLASH_USR_CMD_S); // ahb_usr_command
   //     SET_PERI_REG_MASK(SPI_CTRL_REG(spi_no),SPI_FCMD_OCT|SPI_FADDR_OCT|SPI_FDIN_OCT);
   // }else if(mode == 7){//fast mode line 8 (DTR oct)
   //    // SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FAST_RD_MODE_S);       // fast_read_en
   //     SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_QIO_S);    // fread_qio   
   //     SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_DIO_S);    // fread_dio   
   //     SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_QUAD_S);        // fread_qout  
   //     SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_DUAL_S);   // fread_dout
   //    // SET_PERI_REG_BITS(SPI_CACHE_FCTRL_REG(spi_no),0x1,0x1,SPI_CACHE_FLASH_USR_CMD_S); // ahb_usr_command
   //     SET_PERI_REG_MASK(SPI_CTRL_REG(spi_no),SPI_FCMD_OCT|SPI_FADDR_OCT|SPI_FDIN_OCT|SPI_MODE);
    }
}

unsigned int spi_flash_usr_cmd(unsigned int cmd,         unsigned int cmd_bitlen,   unsigned int addr, 
                               unsigned int addr_bitlen, unsigned int dummy_cyclen, unsigned int *data, 
                               unsigned int data_bitlen, unsigned int mode,         unsigned int spi_no, unsigned int line_mode) 
{
 unsigned int value_bak0 = READ_PERI_REG(SPI_USER_REG(spi_no));
 unsigned int value_bak1 = READ_PERI_REG(SPI_USER1_REG(spi_no));
 unsigned int value_bak2 = READ_PERI_REG(SPI_USER2_REG(spi_no));
 unsigned int value_bak3 = READ_PERI_REG(SPI_MISO_DLEN_REG(spi_no));
 unsigned int value_bak4 = READ_PERI_REG(SPI_MOSI_DLEN_REG(spi_no));
 unsigned int value_bak5 = READ_PERI_REG(SPI_CTRL_REG(spi_no));
 unsigned int value_bak6 = READ_PERI_REG(SPI_W0_REG(spi_no));           
 unsigned int value_bak7 = READ_PERI_REG(SPI_ADDR_REG(spi_no));
 WRITE_PERI_REG(SPI_USER_REG(spi_no), 0);
 WRITE_PERI_REG(SPI_USER1_REG(spi_no), 0);
 WRITE_PERI_REG(SPI_USER2_REG(spi_no), 0);
 WRITE_PERI_REG(SPI_MISO_DLEN_REG(spi_no), 0);
 WRITE_PERI_REG(SPI_MOSI_DLEN_REG(spi_no), 0);
 WRITE_PERI_REG(SPI_CTRL_REG(spi_no), 0);
 WRITE_PERI_REG(SPI_W0_REG(spi_no), 0);  
 WRITE_PERI_REG(SPI_ADDR_REG(spi_no), 0);

 SET_PERI_REG_MASK(SPI_CTRL_REG(spi_no), SPI_WP_REG);
 static unsigned int tmp_len =0, remain_word_num =0;
 tmp_len = data_bitlen >> 3;
 remain_word_num = ((tmp_len & 3) == 0) ? (tmp_len >> 2) :( (tmp_len >> 2) + 1);
 
 if (line_mode == 7)  {
     // SET_PERI_REG_MASK(SPI_CTRL_REG(spi_no),SPI_MODE);//DTR OPI, spi_ddr_mode-> spi_mode in spi_core.v
 } 

// CMD
 if (cmd_bitlen > 0 ) {
   SET_PERI_REG_BITS(SPI_USER2_REG(spi_no), SPI_USR_COMMAND_BITLEN, cmd_bitlen-1, SPI_USR_COMMAND_BITLEN_S);
   SET_PERI_REG_BITS(SPI_USER2_REG(spi_no), SPI_USR_COMMAND_VALUE, cmd, SPI_USR_COMMAND_VALUE_S); 
   SET_PERI_REG_MASK (SPI_USER_REG(spi_no), SPI_USR_COMMAND | SPI_CS_HOLD);
  // if ((line_mode == 6) || (line_mode == 7))  {  // OPI mode
  //      SET_PERI_REG_MASK(SPI_CTRL_REG(spi_no),SPI_FCMD_OCT);
  // } else if (line_mode == 8) {                  //QPI mode
  //      SET_PERI_REG_MASK(SPI_CTRL_REG(spi_no),SPI_FCMD_QUAD);
  // } else if (line_mode == 9) {                  //SDI mode
  //      SET_PERI_REG_MASK(SPI_CTRL_REG(spi_no),SPI_FCMD_DUAL);
  // }
}
 if ((cmd == 0x6) ||(cmd == 0x1) || (cmd == 0x31) || (cmd == 0x11) || (cmd == 0x01FE)) {  //SPI/OPI
     CLEAR_PERI_REG_MASK(SPI_USER_REG(spi_no), SPI_CS_HOLD);
 }   
//ADDR
 if (addr_bitlen > 0) { 
   SET_PERI_REG_MASK (SPI_USER_REG(spi_no),  SPI_USR_ADDR);
   //if(addr_bitlen == 31) {
   if(addr_bitlen > 24) {
         SET_PERI_REG_BITS(SPI_ADDR_REG(spi_no), SPI_USR_ADDR_VALUE, addr,   SPI_USR_ADDR_VALUE_S);
   }else {
         SET_PERI_REG_BITS(SPI_ADDR_REG(spi_no), SPI_USR_ADDR_VALUE, addr<<8, SPI_USR_ADDR_VALUE_S);
   }
   SET_PERI_REG_BITS(SPI_USER1_REG(spi_no), SPI_USR_ADDR_BITLEN, addr_bitlen-1, SPI_USR_ADDR_BITLEN_S); 
 //  if ((line_mode == 6) || (line_mode == 7))  {
 //       SET_PERI_REG_MASK(SPI_CTRL_REG(spi_no),SPI_FADDR_OCT);
 //  }
}//others: No ADDR
 
//DUMMY 
 if (dummy_cyclen > 0) {
   SET_PERI_REG_MASK(SPI_USER_REG(spi_no), SPI_USR_DUMMY);
   SET_PERI_REG_BITS(SPI_USER1_REG(spi_no), SPI_USR_DUMMY_CYCLELEN, dummy_cyclen-1, SPI_USR_DUMMY_CYCLELEN_S);
}

//DATA
 if (data_bitlen > 0) {
    if (mode ==1) { //Write DATA
     // if ((line_mode == 6) || (line_mode == 7)) {
     //   SET_PERI_REG_MASK(SPI_CTRL_REG(spi_no),SPI_FDOUT_OCT);        //OPI
     // }else if (line_mode == 8) {       //QPI mode, send addr in mosi domain when there is no data  out
     //   SET_PERI_REG_MASK(SPI_USER_REG(spi_no),SPI_FWRITE_QIO);
     // }else if (line_mode == 9) {       //SDI mode, send addr in mosi domain when there is no data  out
     //   SET_PERI_REG_MASK(SPI_USER_REG(spi_no),SPI_FWRITE_DIO);
     // }

      SET_PERI_REG_MASK (SPI_USER_REG(spi_no), SPI_USR_MOSI );
      WRITE_PERI_REG(SPI_MOSI_DLEN_REG(spi_no), data_bitlen-1);
      unsigned int j;
      if (remain_word_num > 16) {
         remain_word_num = 16;                                 // program at most 256 bytes for once
      }
      for (j =0; j< remain_word_num; j++) {                   // write data into W0-W15 according to data_bitlen
        WRITE_PERI_REG((SPI_W0_REG(spi_no) + j*4), *data++);
      }
    } else if (mode ==2) { //Read DATA
      SET_PERI_REG_MASK (SPI_USER_REG(spi_no),  SPI_USR_MISO );
      WRITE_PERI_REG(SPI_MISO_DLEN_REG(spi_no), data_bitlen-1);
      if (dummy_delay >0) {
          SET_PERI_REG_BITS(SPI_USER1_REG(spi_no),SPI_USR_DUMMY_CYCLELEN, 
                                                  dummy_delay +dummy_cyclen-1, SPI_USR_DUMMY_CYCLELEN_S);
          SET_PERI_REG_MASK(SPI_USER_REG(spi_no), SPI_USR_DUMMY);
      }
      if (line_mode <8) {  //0-7: line cmd; >8: other 
        spi_flash_line_mode(spi_no, line_mode);
    //  } else if (line_mode == 8) {       //QPI mode, send addr in miso domain when there is no data in 
    //    SET_PERI_REG_MASK(SPI_CTRL_REG(spi_no),SPI_FREAD_QIO);
    //  }else if (line_mode == 9) {       //SDI mode, send addr in miso domain when there is no data in 
    //    SET_PERI_REG_MASK(SPI_CTRL_REG(spi_no),SPI_FREAD_DIO);
      }
    }  
}
 WRITE_PERI_REG(SPI_CMD_REG(spi_no), SPI_USR);
 while (READ_PERI_REG(SPI_CMD_REG(spi_no)) & SPI_USR);

 static unsigned int i;
 if (mode ==2) {
    if (remain_word_num > 16){    // read data from W0-W15, so at most 16 words
      remain_word_num = 16;  
    }
     if (remain_word_num <2){ 
          *data = READ_PERI_REG(SPI_W0_REG(spi_no));
    }else{
       for (i =0; i< remain_word_num; i++) {    
          *data = READ_PERI_REG(SPI_W0_REG(spi_no) + i *4);
          *data++;
       }
   }
}
 WRITE_PERI_REG(SPI_USER_REG(spi_no),      value_bak0);  
// WRITE_PERI_REG(SPI_USER1_REG(spi_no),     value_bak1);
 WRITE_PERI_REG(SPI_USER2_REG(spi_no),     value_bak2);
 WRITE_PERI_REG(SPI_MISO_DLEN_REG(spi_no), value_bak3);
 WRITE_PERI_REG(SPI_MOSI_DLEN_REG(spi_no), value_bak4);
 WRITE_PERI_REG(SPI_CTRL_REG(spi_no),      value_bak5);
 WRITE_PERI_REG(SPI_W0_REG(spi_no),        value_bak6);
 WRITE_PERI_REG(SPI_ADDR_REG(spi_no),      value_bak7);
return 0;
}


#endif //SIM_SPI_CONFIG_H_INCLUDED
