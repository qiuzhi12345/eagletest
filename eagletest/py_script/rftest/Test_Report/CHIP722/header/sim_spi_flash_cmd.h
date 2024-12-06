/*************************************************************
 File name    : sim_spi_flash_cmd.h
 Author       : Wu Cheng`en
 Initial Date : 2018--5-15
 Description  : This file defined the universal function of spi
                cmd in usr mode and the default mode, the iomux
                or gmatrix setting, and spi clk frequency and so
                on.
Version       : 0.1
Revised Dtae  :
Status        : Pending
                It has been verified through VCS simulation.
*************************************************************/
#ifndef SIM_SPI_FLASH_CMD_H_INCLUDED
#define SIM_SPI_FLASH_CMD_H_INCLUDED

#include <xtensa/hal.h>
#include <xtensa/config/core.h>
#include <xtensa/config/system.h>
//#include "../include_new/diag_utils.h"
//
//#include "../include_new/extmem_reg.h"
//#include "../include_new/spi_reg.h"
//#include "../include_new/gpio.h"
//#include "../include_new/gpio_sig_map.h"
//#include "../include_new/dport_reg.h"
//#include "../include_new/sim_common.h"
//#include "../include_new/sim_spi_config.h"

#include "./diag_utils.h"
//
#include "./extmem_reg.h"
#include "./spi_reg.h"
//#include "./gpio.h"
//#include "./gpio_sig_map.h"
#include "./dport_reg.h"
#include "./sim_common.h"
#include "./sim_spi_config.h"

//#include "stdlib.h"
extern unsigned int dummy_delay;
unsigned int Rx_buffer[8];
//unsigned int Tx_buffer[16] = {0x313198a2,0x885a308d,0x3243f6a8,0x196a0b32,0xdc118597,0x02dc09fb,0x3925841d,0x78942314,
//                              0x03020100,0x13000504,0x15141312,0x03020100,0x885a308d,0x3243f6a8,0x196a0b32,0x456afcde};
unsigned int Tx_buffer[16] = {0x5aff00a5,0xa500ff5a,0xff00ff00,0x00ff00ff,0x5aff00a5,0xa500ff5a,0xff00ff00,0x00ff00ff,\
                              0x5aff00a5,0xa500ff5a,0xff00ff00,0x00ff00ff,0x5aff00a5,0xa500ff5a,0xff00ff00,0x00ff00ff};
void spi_io_pullup(unsigned int pullup){
    if(pullup){
        PIN_PULLUP_EN(PERIPHS_IO_MUX_SPICLK_U); //clk
        PIN_PULLUP_EN(PERIPHS_IO_MUX_SPID_U);   //data0
        PIN_PULLUP_EN(PERIPHS_IO_MUX_SPIQ_U);   //data1
        PIN_PULLUP_EN(PERIPHS_IO_MUX_SPIWP_U);  //data2
        PIN_PULLUP_EN(PERIPHS_IO_MUX_SPIHD_U);  //data3
        PIN_PULLUP_EN(PERIPHS_IO_MUX_SPICS0_U); //cs
    }else{
        PIN_PULLUP_DIS(PERIPHS_IO_MUX_SPICLK_U); //clk
        PIN_PULLUP_DIS(PERIPHS_IO_MUX_SPID_U  ); //data0
        PIN_PULLUP_DIS(PERIPHS_IO_MUX_SPIQ_U  ); //data1
        PIN_PULLUP_DIS(PERIPHS_IO_MUX_SPIWP_U ); //data2
        PIN_PULLUP_DIS(PERIPHS_IO_MUX_SPIHD_U ); //data3
        PIN_PULLUP_DIS(PERIPHS_IO_MUX_SPICS0_U); //cs   
    }
}
void spi_mtrx_pad(unsigned int pullup){
    spi_io_pullup(pullup);
//idx 30 is FUNC_SPICLK_GPIO30 in line 182 of ./include_new/io_mux_reg.h
//idx 0 is G0SPICLK_IN_IDX in line 1 of ./include_new/gpio_sig_map.h
    gpio_matrix_out(30,0,0,0); //clk, G0SPICLK_IN_IDX->FUNC_SPICLK_GPIO30
    gpio_matrix_out(31,1,0,0);  //Q, G0SPIQ_IN_IDX->FUNC_SPIQ_GPIO31
    gpio_matrix_out(32,2,0,0);  //D, G0SPID_IN_IDX-> FUNC_SPID_GPIO32
    gpio_matrix_out(27,3,0,0);  //HD, G0SPIHD_IN_IDX-> FUNC_SPIHD_GPIO27
    gpio_matrix_out(28,4,0,0); //WP, G0SPIWP_IN_IDX->FUNC_SPIWP_GPIO28
    gpio_matrix_out(29,5,0,0); //CMD / CS, G0SPICS0_IN_IDX-> FUNC_SPICS0_GPIO29

    gpio_matrix_in(31,1,0);
    gpio_matrix_in(32,2,0);
    gpio_matrix_in(27,3,0);
    gpio_matrix_in(28,4,0);

    gpio_pad_select_gpio(27);
    gpio_pad_select_gpio(28);
    gpio_pad_select_gpio(29);
    gpio_pad_select_gpio(30);
    gpio_pad_select_gpio(31);
    gpio_pad_select_gpio(32);
//The same as PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO32_U, 1);
//            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO32_U, FUNC_SPID_GPIO32);
//gpio_matrix_out, gpio_matrix_in, gpio_pad_select_gpio is in ./include_new/gpio.h
}

void spi_iomux(unsigned int pullup){  //G0 SPI0/1
//    spi_io_pullup(pullup);
//    PIN_FUNC_SELECT(PERIPHS_IO_MUX_SPICLK_U,  FUNC_SPICLK_G0SPICLK );  //clk
//    PIN_FUNC_SELECT(PERIPHS_IO_MUX_SPID_U  ,  FUNC_SPID_G0SPID );      //data0
//    PIN_FUNC_SELECT(PERIPHS_IO_MUX_SPIQ_U  ,  FUNC_SPIQ_G0SPIQ );      //data1
//    PIN_FUNC_SELECT(PERIPHS_IO_MUX_SPIWP_U ,  FUNC_SPIWP_G0SPIWP);     //data2
//    PIN_FUNC_SELECT(PERIPHS_IO_MUX_SPIHD_U ,  FUNC_SPIHD_G0SPIHD);     //data3
//    PIN_FUNC_SELECT(PERIPHS_IO_MUX_SPICS0_U,  FUNC_SPICS0_G0SPICS0 );  //cs 
}

void spi_gpio_sync_sel(unsigned int val)
{
  SET_PERI_REG_MASK(GPIO_PIN21_REG, (val<<3 ) | val); // (REG_GPIO_BASE + 0xC8)
  SET_PERI_REG_MASK(GPIO_PIN22_REG, (val<<3 ) | val); // (REG_GPIO_BASE + 0xCC)
  SET_PERI_REG_MASK(GPIO_PIN23_REG, (val<<3 ) | val); // (REG_GPIO_BASE + 0xD0)
  SET_PERI_REG_MASK(GPIO_PIN24_REG, (val<<3 ) | val); // (REG_GPIO_BASE + 0xD4)
  SET_PERI_REG_MASK(GPIO_PIN25_REG, (val<<3 ) | val); // (REG_GPIO_BASE + 0xD8)
  SET_PERI_REG_MASK(GPIO_PIN27_REG, (val<<3 ) | val); // (REG_GPIO_BASE + 0xE0)
  SET_PERI_REG_MASK(GPIO_PIN28_REG, (val<<3 ) | val); // (REG_GPIO_BASE + 0xE4)
  SET_PERI_REG_MASK(GPIO_PIN29_REG, (val<<3 ) | val); // (REG_GPIO_BASE + 0xE8)
  SET_PERI_REG_MASK(GPIO_PIN30_REG, (val<<3 ) | val); // (REG_GPIO_BASE + 0xEC)
  SET_PERI_REG_MASK(GPIO_PIN31_REG, (val<<3 ) | val); // (REG_GPIO_BASE + 0xF0)
  SET_PERI_REG_MASK(GPIO_PIN32_REG, (val<<3 ) | val); // (REG_GPIO_BASE + 0xF4)
}

void spi2_io_pullup(unsigned int pullup){
    if(pullup){
        PIN_PULLUP_EN(PERIPHS_IO_MUX_GPIO36_U);  //clk
        PIN_PULLUP_EN(PERIPHS_IO_MUX_GPIO35_U);  //SIO[0],D
        PIN_PULLUP_EN(PERIPHS_IO_MUX_GPIO37_U);  //S//SIO[1],Q
        PIN_PULLUP_EN(PERIPHS_IO_MUX_GPIO38_U);
        PIN_PULLUP_EN(PERIPHS_IO_MUX_GPIO33_U);
        PIN_PULLUP_EN(PERIPHS_IO_MUX_GPIO34_U);  //cs 
    }else{
        PIN_PULLUP_DIS(PERIPHS_IO_MUX_GPIO36_U);  //clk
        PIN_PULLUP_DIS(PERIPHS_IO_MUX_GPIO35_U);  //SIO[0],D
        PIN_PULLUP_DIS(PERIPHS_IO_MUX_GPIO37_U);  //S//SIO[1],Q
        PIN_PULLUP_DIS(PERIPHS_IO_MUX_GPIO38_U);
        PIN_PULLUP_DIS(PERIPHS_IO_MUX_GPIO33_U);
        PIN_PULLUP_DIS(PERIPHS_IO_MUX_GPIO34_U);  //cs 
    }
}

void spi3_io_pullup(unsigned int pullup){
    if(pullup){
        PIN_PULLUP_EN(PERIPHS_IO_MUX_GPIO12_U);  //clk
        PIN_PULLUP_EN(PERIPHS_IO_MUX_GPIO11_U);  //SIO[0],D
        PIN_PULLUP_EN(PERIPHS_IO_MUX_GPIO13_U);  //S//SIO[1],Q
    //  PIN_PULLUP_EN(PERIPHS_IO_MUX_GPIO14_U);
        PIN_PULLUP_EN(PERIPHS_IO_MUX_GPIO9_U);
        PIN_PULLUP_EN(PERIPHS_IO_MUX_GPIO10_U);  //cs 
    }else{
        PIN_PULLUP_DIS(PERIPHS_IO_MUX_GPIO12_U);  //clk
        PIN_PULLUP_DIS(PERIPHS_IO_MUX_GPIO11_U);  //SIO[0],D
        PIN_PULLUP_DIS(PERIPHS_IO_MUX_GPIO13_U);  //S//SIO[1],Q
    //  PIN_PULLUP_DIS(PERIPHS_IO_MUX_GPIO14_U);
        PIN_PULLUP_DIS(PERIPHS_IO_MUX_GPIO9_U);
        PIN_PULLUP_DIS(PERIPHS_IO_MUX_GPIO10_U);  //cs 
    }
}

void spi2_iomux(unsigned int pullup){  // SPI2
    spi2_io_pullup(pullup);
    PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO36_U,  FUNC_GPIO36_FSPICLK);  //clk
    PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO35_U,  FUNC_GPIO35_FSPID  );  //SIO[0],D
    PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO37_U,  FUNC_GPIO37_FSPIQ  );  //S//SIO[1],Q
    PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO38_U,  FUNC_GPIO38_FSPIWP );
    PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO33_U,  FUNC_GPIO33_FSPIHD );
    PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO34_U,  FUNC_GPIO34_FSPICS0);  //cs 

    SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO33_U,FUN_IE);
    SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO35_U,FUN_IE);
    SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO37_U,FUN_IE);
    SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO38_U,FUN_IE);
}

void spi3_iomux(unsigned int pullup){  // SPI3
//    spi3_io_pullup(pullup);
//    PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO12_U,  FUNC_GPIO12_VSPICLK);  //clk
//    PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO11_U,  FUNC_GPIO11_VSPID  );  //SIO[0],D
//    PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO13_U,  FUNC_GPIO13_VSPIQ  );  //S//SIO[1],Q
////  PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO14_U,  FUNC_GPIO14_VSPIWP );
//    PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO9_U,   FUNC_GPIO9_VSPIHD );
//    PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO10_U,  FUNC_GPIO10_VSPICS0);  //cs 
}

void spi2_gpio_sync_sel(unsigned int val)
{
  SET_PERI_REG_MASK(GPIO_PIN36_REG, (val<<3 ) | val); // HSPICLK 
  SET_PERI_REG_MASK(GPIO_PIN35_REG, (val<<3 ) | val); // HSPID  
  SET_PERI_REG_MASK(GPIO_PIN37_REG, (val<<3 ) | val); // HSPIQ  
//SET_PERI_REG_MASK(GPIO_PIN38_REG, (val<<3 ) | val); // HSPIWP 
  SET_PERI_REG_MASK(GPIO_PIN33_REG, (val<<3 ) | val); // HSPIHD 
  SET_PERI_REG_MASK(GPIO_PIN34_REG, (val<<3 ) | val); // HSPICS0
}

void spi3_gpio_sync_sel(unsigned int val)
{
  SET_PERI_REG_MASK(GPIO_PIN12_REG, (val<<3 ) | val); // VSPICLK 
  SET_PERI_REG_MASK(GPIO_PIN11_REG, (val<<3 ) | val); // VSPID  
  SET_PERI_REG_MASK(GPIO_PIN13_REG, (val<<3 ) | val); // VSPIQ  
//SET_PERI_REG_MASK(GPIO_PIN14_REG, (val<<3 ) | val); // VSPIWP 
  SET_PERI_REG_MASK(GPIO_PIN9_REG , (val<<3 ) | val); // VSPIHD 
  SET_PERI_REG_MASK(GPIO_PIN10_REG, (val<<3 ) | val); // VSPICS0
}

void spi_oct_flash_mtrx_pad(unsigned int pullup){
//    if(pullup){
//        PIN_PULLUP_EN(PERIPHS_IO_MUX_SPICLK_U); //clk
//        PIN_PULLUP_EN(PERIPHS_IO_MUX_SPID_U);   //data0
//        PIN_PULLUP_EN(PERIPHS_IO_MUX_SPIQ_U);   //data1
//        PIN_PULLUP_EN(PERIPHS_IO_MUX_SPIWP_U);  //data2
//        PIN_PULLUP_EN(PERIPHS_IO_MUX_SPIHD_U);  //data3
//        PIN_PULLUP_EN(PERIPHS_IO_MUX_SPICS0_U); //cs
//        PIN_PULLUP_EN(PERIPHS_IO_MUX_GPIO21_U);
//        PIN_PULLUP_EN(PERIPHS_IO_MUX_GPIO22_U);
//        PIN_PULLUP_EN(PERIPHS_IO_MUX_GPIO23_U);
//        PIN_PULLUP_EN(PERIPHS_IO_MUX_GPIO24_U);
//        PIN_PULLUP_EN(PERIPHS_IO_MUX_GPIO25_U);
//    }else{
//        PIN_PULLUP_DIS(PERIPHS_IO_MUX_SPICLK_U); //clk
//        PIN_PULLUP_DIS(PERIPHS_IO_MUX_SPID_U  ); //data0
//        PIN_PULLUP_DIS(PERIPHS_IO_MUX_SPIQ_U  ); //data1
//        PIN_PULLUP_DIS(PERIPHS_IO_MUX_SPIWP_U ); //data2
//        PIN_PULLUP_DIS(PERIPHS_IO_MUX_SPIHD_U ); //data3
//        PIN_PULLUP_DIS(PERIPHS_IO_MUX_SPICS0_U); //cs   
//        PIN_PULLUP_DIS(PERIPHS_IO_MUX_GPIO21_U);
//        PIN_PULLUP_DIS(PERIPHS_IO_MUX_GPIO22_U);
//        PIN_PULLUP_DIS(PERIPHS_IO_MUX_GPIO23_U);
//        PIN_PULLUP_DIS(PERIPHS_IO_MUX_GPIO24_U);
//        PIN_PULLUP_DIS(PERIPHS_IO_MUX_GPIO25_U);
//    }
//    gpio_matrix_out(30,0,0,0);    //clk,      GPIO30 <- FUNC0   <- G0SPICLK_OUT_IDX
//    gpio_matrix_out(31,1,0,0);    //SIO[1] Q, GPIO31 <- FUNC1   <- G0SPIQ_OUT_IDX
//    gpio_matrix_out(32,2,0,0);    //SIO[0] D, GPIO32 <- FUNC2   <- G0SPID_OUT_IDX
//    gpio_matrix_out(27,3,0,0);    //SIO[3] HD,GPIO27 <- FUNC3   <- G0SPIHD_OUT_IDX
//    gpio_matrix_out(28,4,0,0);    //SIO[2] WP,GPIO28 <- FUNC4   <- G0SPIWP_OUT_IDX
//    gpio_matrix_out(29,5,0,0);    //CMD/CS0   GPIO29 <- FUNC5   <- G0SPICS0_OUT_IDX
//    gpio_matrix_out(21,128,0,0);  //SIO[4],   GPIO21 <- FUNC128 <- G0SPIIO4_OUT_IDX
//    gpio_matrix_out(22,129,0,0);  //SIO[5],   GPIO22 <- FUNC129 <- G0SPIIO5_OUT_IDX
//    gpio_matrix_out(23,130,0,0);  //SIO[6],   GPIO23 <- FUNC130 <- G0SPIIO6_OUT_IDX
//    gpio_matrix_out(24,131,0,0);  //SIO[7],   GPIO24 <- FUNC131 <- G0SPIIO7_OUT_IDX
//    gpio_matrix_out(25,132,0,0);  //DQS,      GPIO25 <- FUNC132 <- G0SPIDQS_OUT_IDX
//
//    gpio_matrix_in(31,  1,0);     //SIO[1], Q,  GPIO31 -> FUNC1   -> G0SPIQ_IN_IDX
//    gpio_matrix_in(32,  2,0);     //SIO[0], D,  GPIO32 -> FUNC2   -> G0SPID_IN_IDX
//    gpio_matrix_in(27,  3,0);     //SIO[3], HD, GPIO27 -> FUNC3   -> G0SPIHD_IN_IDX
//    gpio_matrix_in(28,  4,0);     //SIO[2], WP, GPIO28 -> FUNC4   -> G0SPIWP_IN_IDX
//    gpio_matrix_in(21,128,0);     //SIO[4],     GPIO21 -> FUNC128 -> G0SPIIO4_IN_IDX
//    gpio_matrix_in(22,129,0);     //SIO[5],     GPIO22 -> FUNC129 -> G0SPIIO5_IN_IDX
//    gpio_matrix_in(23,130,0);     //SIO[6],     GPIO23 -> FUNC130 -> G0SPIIO6_IN_IDX
//    gpio_matrix_in(24,131,0);     //SIO[7],     GPIO24 -> FUNC131 -> G0SPIIO7_IN_IDX
//    gpio_matrix_in(25,132,0);     //DQS,        GPIO25 -> FUNC132 -> G0SPIDQS_IN_IDX
//                                        
//    gpio_pad_select_gpio(21); //pad GPIO5 -> GPIO5(In io_mux.v)
//    gpio_pad_select_gpio(22);
//    gpio_pad_select_gpio(23);
//    gpio_pad_select_gpio(24);
//    gpio_pad_select_gpio(25);
//    gpio_pad_select_gpio(27);
//    gpio_pad_select_gpio(28);
//    gpio_pad_select_gpio(29);
//    gpio_pad_select_gpio(30);
//    gpio_pad_select_gpio(31);
//    gpio_pad_select_gpio(32);
}

void spi_oct_flash_iomux(void){ 
//    PIN_FUNC_SELECT(PERIPHS_IO_MUX_SPICLK_U,  FUNC_SPICLK_G0SPICLK );  //clk
//    PIN_FUNC_SELECT(PERIPHS_IO_MUX_SPID_U  ,  FUNC_SPID_G0SPID );      //data0
//    PIN_FUNC_SELECT(PERIPHS_IO_MUX_SPIQ_U  ,  FUNC_SPIQ_G0SPIQ );      //data1
//    PIN_FUNC_SELECT(PERIPHS_IO_MUX_SPIWP_U ,  FUNC_SPIWP_G0SPIWP);     //data2
//    PIN_FUNC_SELECT(PERIPHS_IO_MUX_SPIHD_U ,  FUNC_SPIHD_G0SPIHD);     //data3
//    PIN_FUNC_SELECT(PERIPHS_IO_MUX_SPICS0_U,  FUNC_SPICS0_G0SPICS0 );  //cs   
//
//    PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO21_U,  FUNC_GPIO21_G0SPIIO4); //pad_gpio21->SPIIO4_out
//    PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO22_U,  FUNC_GPIO22_G0SPIIO5); //pad_gpio22->SPIIO5_out
//    PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO23_U,  FUNC_GPIO23_G0SPIIO6); //pad_gpio23->SPIIO6_out
//    PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO24_U,  FUNC_GPIO24_G0SPIIO7); //pad_gpio24->SPIIO7_out
//    PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO25_U,  FUNC_GPIO25_G0SPIDQS); //pad_gpio25->SPIDS_out
}

void switch_clk(U32 mode){
   SET_PERI_REG_BITS(APB_CTRL_SYSCLK_CONF_REG,APB_CTRL_SOC_CLK_SEL,0x0,APB_CTRL_SOC_CLK_SEL_S); 
   
   switch(mode){
       case 80 :WRITE_PERI_REG( DPORT_CPU_PER_CONF_REG, (1<<2) | 0 );//80MHz
                delay_us(1);
                break;
       case 160:WRITE_PERI_REG( DPORT_CPU_PER_CONF_REG, (1<<2) | 1 );//160MHz
                delay_us(1);
                break;
       case 240:WRITE_PERI_REG( DPORT_CPU_PER_CONF_REG, (1<<2) | 2 );//240MHz
                delay_us(1);
                break;
       default: fail(0);
                break;
   }
   
   SET_PERI_REG_BITS(APB_CTRL_SYSCLK_CONF_REG,APB_CTRL_SOC_CLK_SEL,0x1,APB_CTRL_SOC_CLK_SEL_S);
   delay_us(10);
}

void spi_clk_config(unsigned int spi_no,unsigned int pre_div,unsigned int div){
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


//void spi_flash_line_mode(unsigned int spi_no, unsigned int mode){
////    while((SPI_EXT2_REG(0) & 0x7) != 0);
//    //SET_PERI_REG_BITS(SPI_CACHE_FCTRL_REG(0),0x1,0x0,SPI_CACHE_REQ_EN_S);   // ahb_spi_req_en
//    if(mode == 0){//slow mode, line1
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FAST_RD_MODE_S);  // fast_read_en
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FADDR_QUAD_S);    // faddr_quad
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FADDR_DUAL_S);    // faddr_dual    
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_QUAD_S);    // fread_qout
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_DUAL_S);    // fread_dout
//    }else if(mode == 1){//fast mode, line1
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x1,SPI_FAST_RD_MODE_S);  // fast_read_en
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_QIO_S);    // fread_qio
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_DIO_S);    // fread_dio    
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_QUAD_S);   // fread_qout
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_DUAL_S);   // fread_dout
//    }else if(mode == 2){//fast mode, line2(dout)
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x1,SPI_FAST_RD_MODE_S);  // fast_read_en
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_QIO_S);    // fread_qio   
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_DIO_S);    // fread_dio   
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_QUAD_S);   // fread_qout  
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x1,SPI_FREAD_DUAL_S);   // fread_dout
//    }else if(mode == 3){//fast mode, line2(dio)
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x1,SPI_FAST_RD_MODE_S);  // fast_read_en
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_QIO_S);    // fread_qio   
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x1,SPI_FREAD_DIO_S);    // fread_dio   
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_QUAD_S);        // fread_qout  
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_DUAL_S);   // fread_dout
//    }else if(mode == 4){//fast mode lin4(qout)
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x1,SPI_FAST_RD_MODE_S);       // fast_read_en
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_QIO_S);    // fread_qio   
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_DIO_S);    // fread_dio   
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x1,SPI_FREAD_QUAD_S);        // fread_qout  
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_DUAL_S);   // fread_dout
//    }else if(mode == 5){//fast mode lin4(qio)
//       // SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x1,SPI_FAST_RD_MODE_S);       // fast_read_en
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x1,SPI_FREAD_QIO_S);    // fread_qio   
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_DIO_S);    // fread_dio   
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_QUAD_S);        // fread_qout  
//        SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_DUAL_S);   // fread_dout
//   // }else if(mode == 6){//fast mode line 8 (STR oct)
//   //    // SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FAST_RD_MODE_S);       // fast_read_en
//   //     SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_QIO_S);    // fread_qio   
//   //     SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_DIO_S);    // fread_dio   
//   //     SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_QUAD_S);        // fread_qout  
//   //     SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_DUAL_S);   // fread_dout
//   //   //  SET_PERI_REG_BITS(SPI_CACHE_FCTRL_REG(spi_no),0x1,0x1,SPI_CACHE_FLASH_USR_CMD_S); // ahb_usr_command
//   //     SET_PERI_REG_MASK(SPI_CTRL_REG(spi_no),SPI_FCMD_OCT|SPI_FADDR_OCT|SPI_FDIN_OCT);
//   // }else if(mode == 7){//fast mode line 8 (DTR oct)
//   //    // SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FAST_RD_MODE_S);       // fast_read_en
//   //     SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_QIO_S);    // fread_qio   
//   //     SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_DIO_S);    // fread_dio   
//   //     SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_QUAD_S);        // fread_qout  
//   //     SET_PERI_REG_BITS(SPI_CTRL_REG(spi_no),0x1,0x0,SPI_FREAD_DUAL_S);   // fread_dout
//   //    // SET_PERI_REG_BITS(SPI_CACHE_FCTRL_REG(spi_no),0x1,0x1,SPI_CACHE_FLASH_USR_CMD_S); // ahb_usr_command
//   //     SET_PERI_REG_MASK(SPI_CTRL_REG(spi_no),SPI_FCMD_OCT|SPI_FADDR_OCT|SPI_FDIN_OCT|SPI_MODE);
//    }
//}


void spi_wait_idle (unsigned int spi_no, unsigned int line_mode, unsigned int opi_mode)
{
  unsigned int sta_reg_val[2]={1, 1}, mode_val = 0;
  if (line_mode == 8) {   //QPI mode
     mode_val = 8;
  }

  while (1) {
    if (opi_mode == 0) {          //SPI or QPI
        spi_flash_usr_cmd( 0x05, 0x8,  0 , 0, 0, sta_reg_val , 8, 2, spi_no,mode_val);//RDSR
    } else if (opi_mode == 1) {   //STR OPI
        spi_flash_usr_cmd( 0xFA05, 0x10,  0 , 32, 4, sta_reg_val , 8, 2, spi_no,line_mode);//RDSR
    } else if (opi_mode == 2) {   //DTR OPI
        spi_flash_usr_cmd( 0xFA05, 0x10,  0 , 32, 8, sta_reg_val , 8, 2, spi_no,line_mode);//RDSR
    }
    if ((sta_reg_val[0] & 1) != 1) {
       break; // wait WIP =0
    }
  }
}

void spi_wren (unsigned int spi_no, unsigned int line_mode, unsigned int opi_mode)
{
  unsigned int sta_reg_val[2]={0, 0}, mode_val = 0;
  if (line_mode == 8) {   //QPI mode
     mode_val = 8;
  }
  if (opi_mode == 0) {          //SPI or QPI
      spi_flash_usr_cmd( 0x06, 0x8,  0 , 0, 0, 0 , 0, 0, spi_no,mode_val);//WREN
  } else if (opi_mode == 1) {   //STR OPI
      spi_flash_usr_cmd( 0xF906, 0x10,  0 , 0, 0, 0 , 0, 0, spi_no,line_mode);//WRDIS
  } else if (opi_mode == 2) {   //DTR OPI
      spi_flash_usr_cmd( 0xF906, 0x10,  0 , 0, 0, 0 , 0, 0, spi_no,line_mode);//WREN
  }

  spi_wait_idle(spi_no, line_mode, 0);
  while (1) {
    if (opi_mode == 0) {          //SPI
        spi_flash_usr_cmd( 0x05, 0x8,  0, 0, 0, sta_reg_val , 8, 2, spi_no,mode_val);//RDSR
    } else if (opi_mode == 1) {   //STR OPI
        spi_flash_usr_cmd( 0xFA05, 0x10,  0, 32, 4, sta_reg_val , 8, 2, spi_no,line_mode);//RDSR
    } else if (opi_mode == 2) {   //DTR OPI
        spi_flash_usr_cmd( 0xFA05, 0x10,  0, 32, 8, sta_reg_val , 8, 2, spi_no,line_mode);//RDSR
    }
    if (sta_reg_val[0] & 2) {
       break; // wait WEL =1
    }
  }
}

void spi_flash_qe (unsigned int spi_no)  // 0x31 wrties 1 byte to set QE 1
{
    unsigned int rdata[2], sta_reg_val[2]={0, 0};
    spi_wren(spi_no, 0, 0);
    spi_flash_usr_cmd( 0x35, 0x8,  0 , 0, 0, sta_reg_val , 8, 2, spi_no,0);//RDSR
    sta_reg_val[0] = (sta_reg_val[0] | 2);
    spi_flash_usr_cmd( 0x31, 0x8,  0 , 0, 0,  sta_reg_val, 8, 1, spi_no,0);//WRSR
    spi_wait_idle(spi_no, 0, 0);
}

void spi_flash_qe1 (unsigned int spi_no) //0x01 writes 2 bytes to set QE 1
{
    unsigned int rdata[2]={0, 0}, sta_reg_val[2]={0, 0};
    spi_wren(spi_no, 0, 0);
    spi_flash_usr_cmd( 0x05, 0x8,  0 , 0, 0, sta_reg_val , 8, 2, spi_no,0);//RDSR, SR[7:0]
    rdata[0] = sta_reg_val[0];

    spi_flash_usr_cmd( 0x35, 0x8,  0 , 0, 0, sta_reg_val , 8, 2, spi_no,0);//RDSR, SR[15:8]
    sta_reg_val[0] = (sta_reg_val[0] | 2);
    rdata[0] = rdata[0] | (sta_reg_val[0] << 8);
    spi_flash_usr_cmd( 0x01, 0x8,  0 , 0, 0,  rdata, 16, 1, spi_no,0);//WRSR
    spi_wait_idle(spi_no, 0, 0);
}

void spi_flash_qpi_en(unsigned int spi_no)
{
    static unsigned int rdata[2];
  //  spi_wren(spi_no, 0, 0);
  //  sim_spi_wrst_qe1(spi_no);
  //  spi_wait_idle(spi_no, 0, 0);
    spi_flash_qe (spi_no);
    spi_flash_usr_cmd( 0x38, 0x8,  0 , 0, 0, rdata, 0, 0, spi_no,0);  //
}

unsigned int spi_mst_usr_cmd(unsigned int cmd,  unsigned int cmd_bitlen, unsigned int cmd_dual, unsigned int cmd_quad, 
                             unsigned int addr, unsigned int addr_bitlen,unsigned int addr_dual,unsigned int addr_quad,
			     unsigned int dummy_cyclen, unsigned int *data,unsigned int data_bitlen, unsigned int mode,
			     unsigned int din_dual,unsigned int din_quad, unsigned int dout_dual, unsigned int dout_quad,
		      	     unsigned int spi_no) 
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
 SET_PERI_REG_MASK(SPI_CTRL_REG(spi_no), SPI_WR_BIT_ORDER | SPI_RD_BIT_ORDER);
 unsigned int tmp_len =0, remain_word_num =0;
 tmp_len = data_bitlen >> 3;
 remain_word_num = ((tmp_len & 3) == 0) ? (tmp_len >> 2) :( (tmp_len >> 2) + 1);
 SET_PERI_REG_MASK(SPI_CTRL_REG(spi_no), SPI_FAST_RD_MODE);
// CMD
 if (cmd_bitlen > 0 ) {
   SET_PERI_REG_BITS(SPI_USER2_REG(spi_no), SPI_USR_COMMAND_BITLEN, cmd_bitlen-1, SPI_USR_COMMAND_BITLEN_S);
   SET_PERI_REG_BITS(SPI_USER2_REG(spi_no), SPI_USR_COMMAND_VALUE, cmd, SPI_USR_COMMAND_VALUE_S); 
   SET_PERI_REG_MASK (SPI_USER_REG(spi_no), SPI_USR_COMMAND | SPI_CS_HOLD);
}
 if (cmd_dual > 0) {
     SET_PERI_REG_MASK(SPI_CTRL_REG(spi_no), SPI_FCMD_DUAL);
 }else {
     CLEAR_PERI_REG_MASK(SPI_CTRL_REG(spi_no), SPI_FCMD_DUAL);
 }
 if (cmd_quad > 0) {
     SET_PERI_REG_MASK(SPI_CTRL_REG(spi_no), SPI_FCMD_QUAD);
 }else {
     CLEAR_PERI_REG_MASK(SPI_CTRL_REG(spi_no), SPI_FCMD_QUAD);
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

}//others: No ADDR
 if (addr_dual > 0) {
     SET_PERI_REG_MASK(SPI_CTRL_REG(spi_no), SPI_FADDR_DUAL);
 }else {
     CLEAR_PERI_REG_MASK(SPI_CTRL_REG(spi_no), SPI_FADDR_DUAL);
 }
 if (addr_quad > 0) {
     SET_PERI_REG_MASK(SPI_CTRL_REG(spi_no), SPI_FADDR_QUAD);
 }else {
     CLEAR_PERI_REG_MASK(SPI_CTRL_REG(spi_no), SPI_FADDR_QUAD);
 }  
//DUMMY 
 if (dummy_cyclen > 0) {
   SET_PERI_REG_MASK(SPI_USER_REG(spi_no), SPI_USR_DUMMY);
   SET_PERI_REG_BITS(SPI_USER1_REG(spi_no), SPI_USR_DUMMY_CYCLELEN, dummy_cyclen-1, SPI_USR_DUMMY_CYCLELEN_S);
}

//DATA
 if (data_bitlen > 0) {
    if (mode ==1) { //Write DATA
      if (dout_dual > 0) {
          SET_PERI_REG_MASK(SPI_USER_REG(spi_no), SPI_FWRITE_DUAL);
      }else {
          CLEAR_PERI_REG_MASK(SPI_USER_REG(spi_no), SPI_FWRITE_DUAL);
      }
      if (dout_quad > 0) {
          SET_PERI_REG_MASK(SPI_USER_REG(spi_no), SPI_FWRITE_QUAD);
      }else {
          CLEAR_PERI_REG_MASK(SPI_USER_REG(spi_no), SPI_FWRITE_QUAD);
      }  
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
      if (din_dual > 0) {
          SET_PERI_REG_MASK(SPI_CTRL_REG(spi_no), SPI_FREAD_DUAL);
      }else {
          CLEAR_PERI_REG_MASK(SPI_CTRL_REG(spi_no), SPI_FREAD_DUAL);
      }
      if (din_quad > 0) {
          SET_PERI_REG_MASK(SPI_CTRL_REG(spi_no), SPI_FREAD_QUAD);
      }else {
          CLEAR_PERI_REG_MASK(SPI_CTRL_REG(spi_no), SPI_FREAD_QUAD);
      }  
      SET_PERI_REG_MASK (SPI_USER_REG(spi_no),  SPI_USR_MISO );
      WRITE_PERI_REG(SPI_MISO_DLEN_REG(spi_no), data_bitlen-1);
      if (dummy_delay >0) {
          SET_PERI_REG_BITS(SPI_USER1_REG(spi_no),SPI_USR_DUMMY_CYCLELEN, 
                                                  dummy_delay +dummy_cyclen-1, SPI_USR_DUMMY_CYCLELEN_S);
          SET_PERI_REG_MASK(SPI_USER_REG(spi_no), SPI_USR_DUMMY);
      }
    }  
}
 WRITE_PERI_REG(SPI_CMD_REG(spi_no), SPI_USR);
 while (READ_PERI_REG(SPI_CMD_REG(spi_no)) & SPI_USR);

 unsigned int i;
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

#endif // SIM_SPI_FLASH_CMD_H_INCLUDED
