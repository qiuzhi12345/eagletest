#include <xtensa/hal.h>
#include <xtensa/config/core.h>
#include <xtensa/config/system.h>
#include "./diag_utils.h"

#include "./fe_reg.h"
#include "./fe2_reg.h"
//#include "./agc_reg.h"
//#include "./bb_tx_reg.h"
#include "./brx_reg.h"
#include "./bb_reg.h"
#include "./nrx_reg.h"
//#include "./mac_sch_reg.h"
//#include "./mac_sec_reg.h"
#include "../../../submodule/WIFIMAC/sim/example/include_new/mac_pwr_reg.h"
#include "./mux_common.c"
#include "./phy_fpga_v7_cal.c"
#include "./rtc_cntl_reg.h"
#include "./apb_ctrl_reg.h"
#include "dport_reg.h"
#include "./i2c_define.h"
#include "./../include_new/i2c_mst_reg.h"

#define BB_NOT_POST_SIM 1

void bb_printc(unsigned int seq_no,unsigned int rate,unsigned int rssi,unsigned int rx_success, unsigned int err)
{
   //*(volatile unsigned int*)(FE2_NOUSE_REG) = ((rssi << 16) | (rate<<8) | (seq_no<<1) | rx_success);
   printinfo("no= ", seq_no);
   printinfo("rate= ", rate);
   printinfo("rssi= ", rssi);
   printinfo("suc= ", rx_success);
   printinfo("err= ", err);
}

//*******************************************************************
//i2c test
//fe: REG_I2C_BASE + 0x04, 0x7c
#ifndef CHIP_ANA_MODE_SIM
unsigned int i2c_ana_rd(unsigned int host_addr, unsigned int mst_id, unsigned int addr, unsigned int byte_bit)
{
   unsigned int const mst_num = 0;
   unsigned int value;
   unsigned int* mst_ctrl_addr;
   mst_ctrl_addr = (unsigned int*) (host_addr + mst_num *4);
   value = (0<<24) | (0 << 16) | (addr <<8) | mst_id;
   *(volatile unsigned int*) mst_ctrl_addr = value;
   while(((*(volatile unsigned int*) mst_ctrl_addr ) & 0x2000000) != 0){};
   value = ((*(volatile unsigned int*) mst_ctrl_addr) >> 16) & 0xff & byte_bit;
   return value;
}


void i2c_ana_wr(unsigned int host_addr, unsigned int mst_id, unsigned int addr, unsigned int data, unsigned int byte_bit)
{
   unsigned int const mst_num = 0;
   unsigned int value;
   unsigned int* mst_ctrl_addr;
   unsigned int temp_data;

   value = i2c_ana_rd(host_addr, mst_id, addr, 0xff);
   temp_data = value & (~byte_bit) | data;

   mst_ctrl_addr = (unsigned int*) (host_addr + mst_num *4);
   value = (1<<24) | (temp_data << 16) | (addr <<8) | mst_id;
   *(volatile unsigned int*) mst_ctrl_addr = value;
   while(((*(volatile unsigned int*) mst_ctrl_addr ) & 0x2000000) != 0){};
}
#endif

void i2c_ana_check(unsigned int host_id, unsigned int mst_id, unsigned int addr, unsigned int data, unsigned int byte_bit)
{
  //init i2c
  //*(volatile unsigned int*)(REG_I2C_BASE + 0x48) = 0;
  int temp, host_addr;
  host_addr = REG_I2C_BASE + host_id*4;
  i2c_ana_wr(host_addr, mst_id, addr, data, byte_bit);
  temp=i2c_ana_rd(host_addr, mst_id, addr, byte_bit);
  if (temp != data) fail("Diag Failed\n");
}

unsigned int i2c_ana_rd_ana(unsigned int host_addr, unsigned int mst_id, unsigned int addr, unsigned int byte_bit)
{
   unsigned int value;
   //*(volatile U32*)(FE_HOST_FPGA) = *(volatile U32*)(FE_HOST_FPGA) & 0xfffffffe | 0x1;  //chip_ana_mode sel i2c enable
   value = i2c_ana_rd(host_addr, mst_id, addr, byte_bit);
   //*(volatile U32*)(FE_HOST_FPGA) = *(volatile U32*)(FE_HOST_FPGA) & 0xfffffffe | 0x0;  //chip_ana_mode sel i2c disable
   return value;

}

void i2c_ana_wr_ana(unsigned int host_addr, unsigned int mst_id, unsigned int addr, unsigned int data, unsigned int byte_bit)
{
   //*(volatile U32*)(FE_HOST_FPGA) = *(volatile U32*)(FE_HOST_FPGA) & 0xfffffffe | 0x1;  //chip_ana_mode sel i2c enable
   i2c_ana_wr(host_addr, mst_id, addr, data, byte_bit);
   //*(volatile U32*)(FE_HOST_FPGA) = *(volatile U32*)(FE_HOST_FPGA) & 0xfffffffe | 0x0;  //chip_ana_mode sel i2c disable}
}

void i2c_check_all()
{
    int i, i2c_host, i2c_block, addr1, addr2;
    int i2c_num = 12;

    i = ~((I2C_ULP_HOST<<11) | (I2C_BBPLL_HOST<<10) | (I2C_CKGEN_HOST<<9) | (I2C_ana_dig_HOST<<8) | (I2C_XTAL_HOST<<7) | (I2C_PLLA_HOST<<6) | (I2C_BIAS_HOST<<5) | (I2C_TXRF_HOST<<4) | (I2C_PLL_HOST<<3) | (I2C_BBTOP_HOST<<2) | (I2C_SDM_HOST<<1) | I2C_RFRX_HOST) & 0xfff;

    WRITE_PERI_REG(I2C_MST_ANA_CONF2_REG, (i<<4));

    for(i=0; i<i2c_num; i++){
        addr1 = 0; 
        addr2 = 1; 

        switch(i){
            case 0: i2c_host = I2C_RFRX_HOST;  i2c_block = I2C_RFRX_BLOCK;break;
            case 1: i2c_host = I2C_SDM_HOST;  i2c_block = I2C_SDM_BLOCK; break;
            case 2: i2c_host = I2C_BBTOP_HOST;  i2c_block = I2C_BBTOP_BLOCK; break;
            case 3: i2c_host = I2C_PLL_HOST;  i2c_block = I2C_PLL_BLOCK; break;
            case 4: i2c_host = I2C_TXRF_HOST;  i2c_block = I2C_TXRF_BLOCK; break;
            case 5: i2c_host = I2C_BIAS_HOST;  i2c_block = I2C_BIAS_BLOCK; break;
            case 6: i2c_host = I2C_PLLA_HOST;  i2c_block = I2C_PLLA_BLOCK; break;
            case 7: i2c_host = I2C_XTAL_HOST;  i2c_block = I2C_XTAL_BLOCK; break;
            case 8: i2c_host = I2C_ana_dig_HOST;  i2c_block = I2C_ana_dig_BLOCK; addr1 = 11; addr2 = 12; break;
            case 9: i2c_host = I2C_CKGEN_HOST;  i2c_block = I2C_CKGEN_BLOCK; break;
            case 10: i2c_host = I2C_BBPLL_HOST;  i2c_block = I2C_BBPLL_BLOCK; break;
            case 11: i2c_host = I2C_ULP_HOST;  i2c_block = I2C_ULP_BLOCK; break;
            default: i2c_host = I2C_BBPLL_HOST;  i2c_block = I2C_BBPLL_BLOCK; break;
        }
        
        i2c_ana_check(i2c_host, i2c_block, addr1, i*13+1, 0xff);
        i2c_ana_check(i2c_host, i2c_block, addr2, i*16+i+1, 0xff);
    }
}

//**********************************************************************
//pbus

//#define TXBB1 0
//#define TXBB2 1
#define RFRX1 0
#define BB 1
#define DCI 2
#define DCQ 3
#define RFTX1 4
#define RFTX2 5

#define EN1 1
#define EN2 2


void pbus_force_mode_v60(int pbus_force_en)
{
  *(volatile U32*)(FE_PUBS_CTRL0_REG) = (*(volatile U32*)(FE_PUBS_CTRL0_REG)) & 0xfffffffe | pbus_force_en;  //enter force mode
  //if(pbus_force_en){while(((*(volatile U32*)(FE_PUBS_CTRL3_REG)) & 0x40000000)==0){};  //wait untill enter force mode}
  if((pbus_force_en==0) && (*(volatile U32*)(APB_CTRL_WIFI_BB_CFG_REG)&0x2)){
     SET_PERI_REG_BITS(AGCPWR_CTRL7_REG, 1, 0, AGC_FAST_GAIN_SET_S); //fast_gain_set
     delay_us(2);
     SET_PERI_REG_BITS(AGCPWR_CTRL7_REG, 1, 1, AGC_FAST_GAIN_SET_S); //fast_gain_set
  }
}

void pbus_force_test_v60(int pbus_no, int bus_en, int config_data, int en_nodelay, int data_ext, int data_ext_num)
{
//  *(volatile U32*)(FE_PUBS_CTRL0_REG) = (*(volatile U32*)(FE_PUBS_CTRL0_REG)) & 0xfffffffe | 0x1;  //enter force mode
  *(volatile U32*)(FE_PUBS_CTRL0_REG) = (*(volatile U32*)(FE_PUBS_CTRL0_REG)) & 0x0fffffff | (data_ext_num<<30) | (data_ext<<29) | (en_nodelay<<28);  //pbus_data_ext_num, pbus_data_extent, pbus_en_delay
  *(volatile U32*)(FE_PUBS_CTRL0_REG) = (*(volatile U32*)(FE_PUBS_CTRL0_REG)) & 0xfffe0001 | (bus_en<<15) | (config_data<<6) | (pbus_no<<2) | (0x1<<1);  //pbus_en, pbus_data, pbus_sel, new_config_flag
  while((*(volatile U32*)(FE_PUBS_CTRL3_REG)) & 0x80000000){};  //wait untill force config done
  *(volatile U32*)(FE_PUBS_CTRL0_REG) = (*(volatile U32*)(FE_PUBS_CTRL0_REG)) & 0xfffffffd | (0x0<<1);  //clear new_config_flag
//  *(volatile U32*)(FE_PUBS_CTRL0_REG) = (*(volatile U32*)(FE_PUBS_CTRL0_REG)) & 0xfffffffe | 0x0;  //leave force mode
}

U32 pbus_rd_v60(int pbus_no, int bus_en)
{
   U32 pbus_rd_index;
   const U32 pbus_start_index[8] = {0,2,4,5,7,9,11,12};

   pbus_rd_index=pbus_start_index[pbus_no] + ((bus_en==4)? 2 : (bus_en-1));

   return (((*(volatile U32*)(FE_PUBS_RD0_REG + (pbus_rd_index/3*4)))>>((pbus_rd_index==12)? 0 : (18-(pbus_rd_index%3)*9))) & 0x1ff);
}

U32 pbus_rd_addr(int pbus_no, int bus_en){
   switch(pbus_no){
      case RFRX1:return FE_PUBS_RD1_REG;
      case BB: if(bus_en==1) return FE_PUBS_RD1_REG;
               else return FE_PUBS_RD2_REG;
      case DCI:return FE_PUBS_RD2_REG;
      case DCQ:return FE_PUBS_RD3_REG;
      case RFTX1:return FE_PUBS_RD3_REG;
      case RFTX2:return FE_PUBS_RD4_REG;
   }


}


U32 pbus_rd_shift(int pbus_no, int bus_en){
   switch(pbus_no){
      case RFRX1:return 9;
      case BB: if(bus_en==1) return 0;
               else return 18;
      case DCI:if(bus_en==1) return 9;
               else return 0;
      case DCQ:if(bus_en==1) return 18;
               else return 9;
      case RFTX1:if(bus_en==1) return 0;
      case RFTX2:if(bus_en==1) return 0;
   }
}

U32 pbus_rd_v80(int pbus_no, int bus_en){
   U32 addr=pbus_rd_addr(pbus_no,bus_en);
   U32 shift=pbus_rd_shift(pbus_no,bus_en);
   return ((*(volatile U32*)(addr))&(0x1ff<<shift))>>shift;
}

void pbus_force_check(int pbus_no, int bus_en, int config_data, int en_nodelay, int data_ext, int data_ext_num)
{
   U32 temp;
   pbus_force_test_v60(pbus_no, bus_en, config_data, en_nodelay, data_ext, data_ext_num);
   temp = pbus_rd_v80(pbus_no, bus_en);
   if(temp!=config_data){fail("Diag Failed\n");}
}

void pbus_force_rx()
{
   pbus_force_test_v60(BB, EN1, 0x18b, 1, 1, 2);
   pbus_force_test_v60(RFRX1, EN1, 0x184, 1, 1, 2);
   pbus_force_test_v60(RFTX1, EN1, 0x0, 1, 1, 2);
}


//*******************************************************************
//bb

unsigned int pow_usr(unsigned int x, unsigned int y)
{
   unsigned int i, result=1;
   if(y>0)
   {
     for(i=0;i<y;i++)result = result*x;
   }
   return result;
}

unsigned int rx_gain_calc(unsigned int gain_index)
{
  unsigned int gain;
  unsigned int const GAIN_STEP = 6;

  if(gain_index<(GAIN_STEP*3)){gain= ((gain_index/GAIN_STEP)<<13) + (gain_index%GAIN_STEP);}
  else if(gain_index<(GAIN_STEP*3+GAIN_STEP*7)){gain= (3<<13) + ((gain_index-3*GAIN_STEP)/GAIN_STEP<<10) + ((gain_index-3*GAIN_STEP)%GAIN_STEP);}
  else if(gain_index<(GAIN_STEP*3+GAIN_STEP*7+GAIN_STEP*1)){gain= (3<<13) + (7<<10) + (0<<3) + ((gain_index-3*GAIN_STEP-7*GAIN_STEP)%GAIN_STEP);}
  else if(gain_index<(GAIN_STEP*3+GAIN_STEP*7+GAIN_STEP*7)){gain= (3<<13) + (7<<10) + ((pow_usr(2,((gain_index-3*GAIN_STEP-7*GAIN_STEP)/GAIN_STEP))-1)<<3) + ((gain_index-3*GAIN_STEP-7*GAIN_STEP)%GAIN_STEP);}
  else if(gain_index<(GAIN_STEP*3+GAIN_STEP*7+GAIN_STEP*7+5)){gain= (3<<13) + (7<<10) + (0x7f<<3) + ((gain_index-3*GAIN_STEP-7*GAIN_STEP-7*GAIN_STEP)%GAIN_STEP);}
  else{gain= (3<<13) + (7<<10) + (0x7f<<3) + 5;}

  return gain;
}

void set_rx_gain_simu_v52(unsigned int gain_num)
{
  unsigned int i,j;
  unsigned int agc_gain_table[128];
  
  unsigned int agc_bt_gain_offset =  GET_PERI_REG_BITS(AGCBT_CTRL3_REG,AGC_BT_GAIN_OFFSET,AGC_BT_GAIN_OFFSET_S);

  for(i=0; i<gain_num; i++)
  {
     agc_gain_table[i] = rx_gain_calc(i);
  }

  for(j=0;j<2;j++)
  {
     //0~127
     //write high 32 bit word
     //*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG) = (*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG)) & 0xffffff00 | 0x0f;  //wbe
     for(i=0; i<gain_num; i++)
     {
       *(volatile U32*)(FE2_FE_AGCMEM_CTRL2_REG) = (agc_gain_table[i]<<17) + (0x101<<8) + (0x0fe>>1);
       *(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG) = (*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG)) & 0xfffe0000 | (0x1<<16) | ((i+j*agc_bt_gain_offset)<<8) | 0x0f;  //we, waddr, wbe
       //*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG) = (*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG)) & 0xfffeffff | (0x1<<16);  //wen
     }
     //write low 32 bit word
     //*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG) = (*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG)) & 0xffffff00 | 0xf0;  //wbe
     for(i=0; i<gain_num; i++)
     {
       *(volatile U32*)(FE2_FE_AGCMEM_CTRL2_REG) = (0x102<<22) + (0x0fc<<13);
       *(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG) = (*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG)) & 0xfffe0000 | (0x1<<16) | ((i+j*agc_bt_gain_offset)<<8) | 0xf0;  //we, waddr, wbe
       //*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG) = (*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG)) & 0xfffeffff | (0x1<<16);  //wen
     }
  }
}

void set_rx_dcmem_simu_v60()
{
  unsigned int i;
  unsigned int agc_dc_table[128];

  for(i=0; i<128; i++)
  {
    agc_dc_table[i] = i;
  }

  //0~127
  for(i=0; i<128; i++)
  {
    *(volatile U32*)(AGCMEM_CTRL2_REG) = agc_dc_table[i];
    *(volatile U32*)(AGCMEM_CTRL1_REG) = (*(volatile U32*)(AGCMEM_CTRL1_REG)) & 0xfff300ff | (0x1<<19) | (0x0<<18) | (i<<8);  //force, wen, addr
    *(volatile U32*)(AGCMEM_CTRL1_REG) = (*(volatile U32*)(AGCMEM_CTRL1_REG)) & 0xfff3ffff | (0x0<<19) | (0x1<<18);  //force, wen
  }
}

#define INDEX_RFRX_PBUS   0
#define INDEX_BB_PBUS     1
#define INDEX_DCOI_PBUS   2
#define INDEX_DCOQ_PBUS   3
#define INDEX_TXRF1_PBUS  4
#define INDEX_TXRF2_PBUS  5
#define INDEX_EVENT_FLAG  15

#define EVENT_TX_GAIN_1   0
#define EVENT_TX_GAIN_2   1
#define EVENT_TX_GAIN_3   2
#define EVENT_TX_GAIN_4   3
#define EVENT_TX_GAIN_5   4

#define PBUS_EN1          1
#define PBUS_EN2          2

#define PBUS_RXON_NUM     2
#define PBUS_RXOFF_NUM    2
#define PBUS_TXON_NUM     6
#define PBUS_TXOFF_NUM    2
#define PBUS_PAON_NUM     2
#define PBUS_PAOFF_NUM    1

void set_pbus_mem()
{
  unsigned int i;
  unsigned int index_start, index_end;
  unsigned int pbus_table[256];

  //data format: event_flag/pbus_id[3:0], pbus_en[1:0], pbus_data[8:0], pbus_data_we[8:0]
  unsigned int const table_rxon[PBUS_RXON_NUM] =   {((INDEX_RFRX_PBUS<<20)|(PBUS_EN1<<18)|(0x184<<9)|0x185),
                                                    ((INDEX_BB_PBUS<<20)|(PBUS_EN1<<18)|(0x89<<9)|0x1ff)};
  unsigned int const table_rxoff[PBUS_RXOFF_NUM] = {((INDEX_RFRX_PBUS<<20)|(PBUS_EN1<<18)|(0x4<<9)|0x185),
                                                    ((INDEX_BB_PBUS<<20)|(PBUS_EN1<<18)|(0x8<<9)|0x1ff)};
  unsigned int const table_txon[PBUS_TXON_NUM] =   {((INDEX_RFRX_PBUS<<20)|(PBUS_EN1<<18)|(0x1<<9)|0x1),
                                                    ((INDEX_BB_PBUS<<20)|(PBUS_EN1<<18)|(0x178<<9)|0x1ff),
                                                    ((INDEX_EVENT_FLAG<<20)|(EVENT_TX_GAIN_1<<16)),  //txbb_gain
                                                    ((INDEX_EVENT_FLAG<<20)|(EVENT_TX_GAIN_2<<16)),  //txbb_dc_1
                                                    ((INDEX_EVENT_FLAG<<20)|(EVENT_TX_GAIN_3<<16)),  //txbb_dc_2
                                                    ((INDEX_EVENT_FLAG<<20)|(EVENT_TX_GAIN_5<<16))};  //txbb_dc_2
  unsigned int const table_txoff[PBUS_TXOFF_NUM] = {((INDEX_RFRX_PBUS<<20)|(PBUS_EN1<<18)|(0x0<<9)|0x1),
                                                    ((INDEX_BB_PBUS<<20)|(PBUS_EN1<<18)|(0x08<<9)|0x1ff)};
  unsigned int const table_paon[PBUS_PAON_NUM] =   {((INDEX_TXRF1_PBUS<<20)|(PBUS_EN1<<18)|(0x7f<<9)|0x7f),
                                                    ((INDEX_EVENT_FLAG<<20)|(EVENT_TX_GAIN_4<<16))};  //rftx_gain
  unsigned int const table_paoff[PBUS_PAOFF_NUM] = {((INDEX_TXRF1_PBUS<<20)|(PBUS_EN1<<18)|(0x0<<9)|0x7f)};

  unsigned int const table_rxon_bt[PBUS_RXON_NUM] =   {((INDEX_RFRX_PBUS<<20)|(PBUS_EN1<<18)|(0x184<<9)|0x185),
                                                    ((INDEX_BB_PBUS<<20)|(PBUS_EN1<<18)|(0x08b<<9)|0x1ff)};
  unsigned int const table_rxoff_bt[PBUS_RXOFF_NUM] = {((INDEX_RFRX_PBUS<<20)|(PBUS_EN1<<18)|(0x4<<9)|0x185),
                                                    ((INDEX_BB_PBUS<<20)|(PBUS_EN1<<18)|(0xa<<9)|0x1ff)};
  unsigned int const table_txon_bt[PBUS_TXON_NUM] =   {((INDEX_RFRX_PBUS<<20)|(PBUS_EN1<<18)|(0x1<<9)|0x1),
                                                    ((INDEX_BB_PBUS<<20)|(PBUS_EN1<<18)|(0x17a<<9)|0x1ff),
                                                    ((INDEX_EVENT_FLAG<<20)|(EVENT_TX_GAIN_1<<16)),  //txbb_gain
                                                    ((INDEX_EVENT_FLAG<<20)|(EVENT_TX_GAIN_2<<16)),  //txbb_dc_1
                                                    ((INDEX_EVENT_FLAG<<20)|(EVENT_TX_GAIN_3<<16))};  //txbb_dc_2
  unsigned int const table_txoff_bt[PBUS_TXOFF_NUM] = {((INDEX_RFRX_PBUS<<20)|(PBUS_EN1<<18)|(0x0<<9)|0x1),
                                                    ((INDEX_BB_PBUS<<20)|(PBUS_EN1<<18)|(0x00a<<9)|0x1ff)};
  //******************************************************************************************************************************************
  //default

  for(i=0; i<256; i++)
  {
    pbus_table[i] = 0;
  }

  //rxon
  index_start = ((*(volatile U32*)(FE_PUBS_CFG0_REG))>>0) & 0xff;
  index_end = index_start + PBUS_RXON_NUM - 1;
  *(volatile U32*)(FE_PUBS_CFG0_REG) = (*(volatile U32*)(FE_PUBS_CFG0_REG)) & 0xffff00ff | (index_end<<8);
  for(i=0; i<PBUS_RXON_NUM; i++)
  {
    pbus_table[index_start+i] = table_rxon[i];
  }
  //rxoff
  index_start = ((*(volatile U32*)(FE_PUBS_CFG0_REG))>>16) & 0xff;
  index_end = index_start + PBUS_RXOFF_NUM - 1;
  *(volatile U32*)(FE_PUBS_CFG0_REG) = (*(volatile U32*)(FE_PUBS_CFG0_REG)) & 0x00ffffff | (index_end<<24);
  for(i=0; i<PBUS_RXOFF_NUM; i++)
  {
    pbus_table[index_start+i] = table_rxoff[i];
  }
  //txon
  index_start = ((*(volatile U32*)(FE_PUBS_CFG1_REG))>>0) & 0xff;
  index_end = index_start + PBUS_TXON_NUM - 1;
  *(volatile U32*)(FE_PUBS_CFG1_REG) = (*(volatile U32*)(FE_PUBS_CFG1_REG)) & 0xffff00ff | (index_end<<8);
  for(i=0; i<PBUS_TXON_NUM; i++)
  {
    pbus_table[index_start+i] = table_txon[i];
  }
  //txoff
  index_start = ((*(volatile U32*)(FE_PUBS_CFG1_REG))>>16) & 0xff;
  index_end = index_start + PBUS_TXOFF_NUM - 1;
  *(volatile U32*)(FE_PUBS_CFG1_REG) = (*(volatile U32*)(FE_PUBS_CFG1_REG)) & 0x00ffffff | (index_end<<24);
  for(i=0; i<PBUS_TXOFF_NUM; i++)
  {
    pbus_table[index_start+i] = table_txoff[i];
  }
  //paon
  index_start = ((*(volatile U32*)(FE_PUBS_CFG2_REG))>>0) & 0xff;
  index_end = index_start + PBUS_PAON_NUM - 1;
  *(volatile U32*)(FE_PUBS_CFG2_REG) = (*(volatile U32*)(FE_PUBS_CFG2_REG)) & 0xffff00ff | (index_end<<8);
  for(i=0; i<PBUS_PAON_NUM; i++)
  {
    pbus_table[index_start+i] = table_paon[i];
  }
  //paoff
  index_start = ((*(volatile U32*)(FE_PUBS_CFG2_REG))>>16) & 0xff;
  index_end = index_start + PBUS_PAOFF_NUM - 1;
  *(volatile U32*)(FE_PUBS_CFG2_REG) = (*(volatile U32*)(FE_PUBS_CFG2_REG)) & 0x00ffffff | (index_end<<24);
  for(i=0; i<PBUS_PAOFF_NUM; i++)
  {
    pbus_table[index_start+i] = table_paoff[i];
  }
   
  //*********************************************************************************************************************************
//#if BB_NOT_POST_SIM
  //bt

  //rxon
  index_start = ((*(volatile U32*)(FE_PUBS_CFG3_REG))>>0) & 0xff;
  index_end = index_start + PBUS_RXON_NUM - 1;
  *(volatile U32*)(FE_PUBS_CFG3_REG) = (*(volatile U32*)(FE_PUBS_CFG3_REG)) & 0xffff00ff | (index_end<<8);
  for(i=0; i<PBUS_RXON_NUM; i++)
  {
    pbus_table[index_start+i] = table_rxon_bt[i];
  }
  //rxoff
  index_start = ((*(volatile U32*)(FE_PUBS_CFG3_REG))>>16) & 0xff;
  index_end = index_start + PBUS_RXOFF_NUM - 1;
  *(volatile U32*)(FE_PUBS_CFG3_REG) = (*(volatile U32*)(FE_PUBS_CFG3_REG)) & 0x00ffffff | (index_end<<24);
  for(i=0; i<PBUS_RXOFF_NUM; i++)
  {
    pbus_table[index_start+i] = table_rxoff_bt[i];
  }
  //txon
  index_start = ((*(volatile U32*)(FE_PUBS_CFG4_REG))>>0) & 0xff;
  index_end = index_start + PBUS_TXON_NUM - 1;
  *(volatile U32*)(FE_PUBS_CFG4_REG) = (*(volatile U32*)(FE_PUBS_CFG4_REG)) & 0xffff00ff | (index_end<<8);
  for(i=0; i<PBUS_TXON_NUM; i++)
  {
    pbus_table[index_start+i] = table_txon_bt[i];
  }
  //txoff
  index_start = ((*(volatile U32*)(FE_PUBS_CFG4_REG))>>16) & 0xff;
  index_end = index_start + PBUS_TXOFF_NUM - 1;
  *(volatile U32*)(FE_PUBS_CFG4_REG) = (*(volatile U32*)(FE_PUBS_CFG4_REG)) & 0x00ffffff | (index_end<<24);
  for(i=0; i<PBUS_TXOFF_NUM; i++)
  {
    pbus_table[index_start+i] = table_txoff_bt[i];
  }
  //paon
  index_start = ((*(volatile U32*)(FE_PUBS_CFG5_REG))>>0) & 0xff;
  index_end = index_start + PBUS_PAON_NUM - 1;
  *(volatile U32*)(FE_PUBS_CFG5_REG) = (*(volatile U32*)(FE_PUBS_CFG5_REG)) & 0xffff00ff | (index_end<<8);
  for(i=0; i<PBUS_PAON_NUM; i++)
  {
    pbus_table[index_start+i] = table_paon[i];
  }
  //paoff
  index_start = ((*(volatile U32*)(FE_PUBS_CFG5_REG))>>16) & 0xff;
  index_end = index_start + PBUS_PAOFF_NUM - 1;
  *(volatile U32*)(FE_PUBS_CFG5_REG) = (*(volatile U32*)(FE_PUBS_CFG5_REG)) & 0x00ffffff | (index_end<<24);
  for(i=0; i<PBUS_PAOFF_NUM; i++)
  {
    pbus_table[index_start+i] = table_paoff[i];
  }
  //******************************************************************************************************************************
  //0~256 ---> 0~72
  for(i=0; i<72; i++)
  {
    *(volatile U32*)(FE2_FE_AGCMEM_CTRL2_REG) = pbus_table[i];
    *(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG) = (*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG)) & 0xfffd00ff | (0x1<<17) | (i<<8);  //we, waddr
    //*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG) = (*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG)) & 0xfffdffff | (0x1<<17);  //wen
    #if 0
    printinfo("no= ", i);
    printinfo("high= ", ((pbus_table[i]>>16)&0xffff));
    printinfo("low= \n", (pbus_table[i]&0xffff));
    #endif
  }
//#endif
}

void set_tx_gain(unsigned int gain_num)
{
  unsigned int i, addr_start;
  unsigned int tx_gain_table[32];

  //force value is 0

  addr_start = ((*(volatile U32*)(FE_TX_GAIN_CTRL_REG))>>10) & 0xff;
  //write high 32 bit word
  //*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG) = (*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG)) & 0xffffff00 | 0x0f;  //wbe
  *(volatile U32*)(FE2_FE_AGCMEM_CTRL2_REG) = 0;
  *(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG) = (*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG)) & 0xfffe0000 | (0x1<<16) | ((addr_start+i)<<8) | 0x0f;  //we, waddr, wbe
  //*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG) = (*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG)) & 0xfffeffff | (0x1<<16);  //wen
  //write low 32 bit word
  //*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG) = (*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG)) & 0xffffff00 | 0xf0;  //wbe
  *(volatile U32*)(FE2_FE_AGCMEM_CTRL2_REG) = 0;
  *(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG) = (*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG)) & 0xfffe0000 | (0x1<<16) | ((addr_start+i)<<8) | 0xf0;  //we, waddr, wbe
  //*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG) = (*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG)) & 0xfffeffff | (0x1<<16);  //wen

  //work mode value is random

  addr_start = ((*(volatile U32*)(FE_TX_GAIN_CTRL_REG))>>18) & 0xff;

  for(i=0; i<gain_num; i++)
  {
    tx_gain_table[i] = i;
  }

  //0~127
  //write high 32 bit word
  //*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG) = (*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG)) & 0xffffff00 | 0x0f;  //wbe
  for(i=0; i<gain_num; i++)
  {
    *(volatile U32*)(FE2_FE_AGCMEM_CTRL2_REG) = (((*(volatile U32*)(WDEVTIME_REG))&0xf)<<12) + (((*(volatile U32*)(WDEVTIME_REG))&0xf)<<3);
    *(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG) = (*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG)) & 0xfffe0000 | (0x1<<16) | ((addr_start+i)<<8) | 0x0f;  //we, waddr, wbe
    //*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG) = (*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG)) & 0xfffeffff | (0x1<<16);  //wen
  }
  //write low 32 bit word
  //*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG) = (*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG)) & 0xffffff00 | 0xf0;  //wbe
  for(i=0; i<gain_num; i++)
  {
    *(volatile U32*)(FE2_FE_AGCMEM_CTRL2_REG) = (((*(volatile U32*)(WDEVTIME_REG))&0xf)<<26) + (((*(volatile U32*)(WDEVTIME_REG))&0xf)<<17) + ((tx_gain_table[i]+1)<<10) + tx_gain_table[i];
    *(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG) = (*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG)) & 0xfffe0000 | (0x1<<16) | ((addr_start+i)<<8) | 0xf0;  //we, waddr, wbe
    //*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG) = (*(volatile U32*)(FE2_FE_AGCMEM_CTRL1_REG)) & 0xfffeffff | (0x1<<16);  //wen
  }
}

//tmp config, only for sim
//txfilt bw sel: 11n: 2; 11g: 1; 11b: 0
void set_tx_rate_map()
{
    int i;
    int data;
    for(i=0; i<3; i++)
    {
        data = (i<<28) | (i<<24) | (i<<20) | (i<<16) | (i<<12) | (i<<8) | (i<<4) | (i<<0);
        *(volatile U32*)(FE2_FE_TX_GAIN_MAP_0_REG + (i*4+0)*4) = data;
        *(volatile U32*)(FE2_FE_TX_GAIN_MAP_0_REG + (i*4+1)*4) = data;
        *(volatile U32*)(FE2_FE_TX_GAIN_MAP_0_REG + (i*4+2)*4) = data;
        *(volatile U32*)(FE2_FE_TX_GAIN_MAP_0_REG + (i*4+3)*4) = data;
    }
    *(volatile U32*)(FE_TXFILT_BAND_CTRL_1_REG) = 0x34;
}

void test_rifs(int package_num_div2)
{
  int i;

  *(volatile U32*)(AGCFSM_CTRL1_REG) = *(volatile U32*)(AGCFSM_CTRL1_REG) & 0xfffbffff | (0x1<<18);  //rifs_mode

  *(volatile U32*)(REG_GPIO_BASE+ 0x00)      = *(volatile U32*) (REG_GPIO_BASE+ 0x00) & 0xffffffd1 | (0x6<<1);  //set GPIO3~1 : to control rx data source
  *(volatile U32*)(REG_GPIO_BASE+ 0x00)      = *(volatile U32*) (REG_GPIO_BASE+ 0x00) & 0xffffffd1 | (0x7<<1);  //set GPIO3~1 and GPIO5: to control rx data source

  for(i=0;i<package_num_div2;i++)
  {
    //begin rx test
    *(volatile U32*)(REG_GPIO_BASE+ 0x00) = 0x1e;  //reset GPIO4, init dumping rx data in bench
    *(volatile U32*)(REG_GPIO_BASE+ 0x00) = 0xe;  //release GPIO4, begin dump-out

    *(volatile U32*)(AGCFSM_CTRL3_REG) = (*(volatile U32*)(AGCFSM_CTRL3_REG)) & 0xffff7fff | (0x1<<15);  //clr_rx_end_td
    *(volatile U32*)(AGCFSM_CTRL3_REG) = (*(volatile U32*)(AGCFSM_CTRL3_REG)) & 0xffff7fff | (0x0<<15);  //clr_rx_end_td
  
    while(((*(volatile U32*)(AGCRD2_REG)) & 0x4000000 ) == 0){};

    //begin rx test
    *(volatile U32*)(REG_GPIO_BASE+ 0x00) = 0x1e;  //reset GPIO4, init dumping rx data in bench
    *(volatile U32*)(REG_GPIO_BASE+ 0x00) = 0xe;  //release GPIO4, begin dump-out

    *(volatile U32*)(AGCFSM_CTRL3_REG) = (*(volatile U32*)(AGCFSM_CTRL3_REG)) & 0xffff7fff | (0x1<<15);  //clr_rx_end_td
    *(volatile U32*)(AGCFSM_CTRL3_REG) = (*(volatile U32*)(AGCFSM_CTRL3_REG)) & 0xffff7fff | (0x0<<15);  //clr_rx_end_td
  
    while(((*(volatile U32*)(AGCRD2_REG)) & 0x4000000 ) == 0){};
  }

  *(volatile U32*)(AGCFSM_CTRL1_REG) = *(volatile U32*)(AGCFSM_CTRL1_REG) & 0xfffbffff | (0x0<<18);  //rifs_mode
}

void rx_gain_force(int force_en, int force_value)
{
  *(volatile U32*)(AGCPWR_CTRL7_REG) = *(volatile U32*)(AGCPWR_CTRL7_REG) & 0x007fffff | ((force_value & 0xff)<<24) | ((force_en & 0x1)<<23);
}

//*********************************************************************************************************
/*
void set_rx_gain_simu_gate(unsigned int gain_num)
{
  unsigned int i;
  unsigned int agc_gain_table_gate[128];

  for(i=0; i<gain_num; i++)
  {
    agc_gain_table_gate[i] = rx_gain_calc(i);
  }

  *(volatile U32*)(0x60009a68) = (*(volatile U32*)(0x60009a68)) & 0xfffffe00 | (0x0f<<1) | 0x0;
  for(i=0; i<gain_num; i++){*(volatile U32*)(0x60009e00+i*4) = ((agc_gain_table_gate[i]<<17) + (0x100<<8) + (0x100>>1));}
  *(volatile U32*)(0x60009a68) = (*(volatile U32*)(0x60009a68)) & 0xfffffe00 | (0xf0<<1) | 0x0;
  for(i=0; i<gain_num; i++){*(volatile U32*)(0x60009e00+i*4) = ((0x100<<22) + (0x100<<13));}
}

void bb_init_gate()
{
  *(volatile U32*)(WDEVOPTIONS_REG) = *(volatile U32*)(WDEVOPTIONS_REG) & 0xfffffff7 | (0x0<<3);
  *(volatile U32*)(APB_CTRL_WIFI_BB_CFG_REG) = *(volatile U32*) (APB_CTRL_WIFI_BB_CFG_REG) & 0xfffffffd | (0x1<<1);
  *(volatile U32*)(APB_CTRL_WIFI_BB_CFG_REG) = *(volatile U32*) (APB_CTRL_WIFI_BB_CFG_REG) & 0xfffffffe | (0x0<<0);
  *(volatile U32*)(APB_CTRL_WIFI_BB_CFG_REG) = *(volatile U32*) (APB_CTRL_WIFI_BB_CFG_REG) & 0xfffffffe | (0x1<<0);
  *(volatile U32*)(APB_CTRL_WIFI_BB_CFG_REG) = *(volatile U32*) (APB_CTRL_WIFI_BB_CFG_REG) & 0xfffffffe | (0x0<<0);
  *(volatile U32*)(APB_CTRL_WIFI_BB_CFG_REG) = *(volatile U32*) (APB_CTRL_WIFI_BB_CFG_REG) & 0xfffffffd | (0x0<<1);
  *(volatile U32*)(APB_CTRL_WIFI_BB_CFG_REG) = *(volatile U32*) (APB_CTRL_WIFI_BB_CFG_REG) & 0xfffffffd | (0x1<<1);
  *(volatile U32*)(APB_CTRL_WIFI_BB_CFG_REG) = *(volatile U32*) (APB_CTRL_WIFI_BB_CFG_REG) & 0xfffffffe | (0x0<<0);
  *(volatile U32*)(APB_CTRL_WIFI_BB_CFG_REG) = *(volatile U32*) (APB_CTRL_WIFI_BB_CFG_REG) & 0xfffffffe | (0x1<<0);
  *(volatile U32*)(APB_CTRL_WIFI_BB_CFG_REG) = *(volatile U32*) (APB_CTRL_WIFI_BB_CFG_REG) & 0xfffffffe | (0x0<<0);
  *(volatile U32*)(APB_CTRL_WIFI_BB_CFG_REG) = *(volatile U32*) (APB_CTRL_WIFI_BB_CFG_REG) & 0xfffffffd | (0x0<<1);
  *(volatile U32*)(0x60009838) = (*(volatile U32*)(0x60009838)) & 0xfff00fff | ((0xd0+0x20)<<12);
  set_rx_gain_simu_gate(110);
  *(volatile U32*)(FE_GEN_CTRL_REG) = (*(volatile U32*)(FE_GEN_CTRL_REG)) & 0xffffff5f | (1<<5) | (1<<7);  //tx/rx_timing
  *(volatile U32*)(FE_GEN_CTRL_REG) = (*(volatile U32*)(FE_GEN_CTRL_REG)) & 0xffffffef | (0<<4);
  *(volatile U32*)(0x60009d68) = (*(volatile U32*)(0x60009d68)) & 0xfffc03ff | (11<<10);
  //i2c_ana_wr(REG_I2C_BASE + 0x00, 0x77, 18, 0, 0xff);
  SET_PERI_REG_BITS(FE2_SCALE_CTRL_REG, FE2_RX_SCALE, 0, FE2_RX_SCALE_S);
  *(volatile U32*)(0x60009b50) = (*(volatile U32*)(0x60009b50)) & 0x7fffffff | (0x1<<31);
  *(volatile U32*)(0x60009d18) = (*(volatile U32*)(0x60009d18)) & 0x0 | (0x190<<0);
  *(volatile U32*)(0x600098ec) = (*(volatile U32*)(0x600098ec)) & 0xfc00ffff | (0x190<<16);
  *(volatile U32*)(0x60009988) = (*(volatile U32*)(0x60009988)) & 0xfbffffff | (0x0<<26);
  *(volatile U32*)(0x60009b50) = (*(volatile U32*)(0x60009b50)) & 0xffffff00 | (0xe0<<0);
  *(volatile U32*)(0x60009b50) = (*(volatile U32*)(0x60009b50)) & 0xf00fffff | (0xd5<<20);
  *(volatile U32*)(0x60009b68) = (*(volatile U32*)(0x60009b68)) & 0xfffe001f | (15<<11) | (16<<5);
  *(volatile U32*)(0x60009a64) = (*(volatile U32*)(0x60009a64)) & 0xffffffc1 | (8<<1);
  *(volatile U32*)(0x60009a40) = (*(volatile U32*)(0x60009a40)) & 0xffffff00 | (0xc9<<0);
  *(volatile U32*)(APB_CTRL_WIFI_BB_CFG_REG) = *(volatile U32*) (APB_CTRL_WIFI_BB_CFG_REG) & 0xfffffffd | (0x1<<1);
  delay_us(40);
  *(volatile U32*)(0x60009b64) = *(volatile U32*) (0x60009b64) & 0xfffffe00 | (0x140<<0);
  *(volatile U32*)(0x60009b60) = (*(volatile U32*)(0x60009b60)) & 0xfffd7ffd | (0x0<<17) | (0x0<<15) | (0x1<<1);
  *(volatile U32*)(0x60009838) = (*(volatile U32*)(0x60009838)) & 0xfff00fff | (0xd0<<12);  //rx_rssi
}
*/
//*********************************************************************************************************

//tx_clk_en
void set_txclk_en(unsigned int txclk_en)
{
   unsigned int value;

   //value = i2c_ana_rd_ana(REG_I2C_BASE + 0x00, 0x77, 28, 0xff);
   //i2c_ana_wr_ana(REG_I2C_BASE + 0x00, 0x77, 28, (value&0xbf|(txclk_en<<6)), 0xff);
   SET_PERI_REG_MASK(FE2_IQ_MIS_CTRL_REG, FE2_TX_CLK_FORCE_EN);

   value = i2c_ana_rd_ana(REG_I2C_BASE + 0x04, 0x7c, 21, 0xff);
   i2c_ana_wr_ana(REG_I2C_BASE + 0x04, 0x7c, 21, (value&0xfe|(txclk_en<<0)), 0xff);
}

// test tx tone
void start_tx_tone(int tone1_en, float freq_1_mhz, int tone1_atten, int tone2_en, float freq_2_mhz, int tone2_atten, int tone3_en, float freq_3_mhz, int tone3_atten)
{
  unsigned int reg_freq_1;
  unsigned int reg_freq_2;
  unsigned int reg_freq_3;  
  reg_freq_1 = (int)(freq_1_mhz * 1000 * 64/5000) & 0x3ff;
  reg_freq_2 = (int)(freq_2_mhz * 1000 * 64/5000) & 0x3ff;
  reg_freq_3 = (int)(freq_3_mhz * 1000 * 64/5000) & 0x3ff; 
  int dis_phase = 0;

  set_txclk_en(1);

  pbus_force_mode_v60(1);
  pbus_force_test_v60(RFTX1, EN1, 0x7f, 0, 0, 0);
  pbus_force_test_v60(BB, EN1, 0x7c, 0, 0, 0);
  pbus_force_test_v60(RFRX1, EN1, 0x05, 0, 0, 0);
  pbus_force_mode_v60(0);

  *(volatile U32*)(FE_TX_TEST_CTRL_0_REG) = (*(volatile U32*)(FE_TX_TEST_CTRL_0_REG)) & 0xf0000000 | (0x0<<24) | (0x0<<22) | (dis_phase<<21) | (0x0<<19) | (tone1_en<<18) | (tone1_atten<<10) | reg_freq_1;  //inv[3:0], phase_cfg[1:0], dis_phase, iq_sel[1:0], tone_en, atten, freq
  *(volatile U32*)(FE_TX_TEST_CTRL_1_REG) = (*(volatile U32*)(FE_TX_TEST_CTRL_1_REG)) & 0xf0000000 | (0x0<<24) | (0x0<<22) | (dis_phase<<21) | (0x0<<19) | (tone2_en<<18) | (tone2_atten<<10) | reg_freq_2;  //inv[3:0], phase_cfg[1:0], dis_phase, iq_sel[1:0], tone_en, atten, freq
  *(volatile U32*)(FE_TX_TEST_CTRL_3_REG) = (*(volatile U32*)(FE_TX_TEST_CTRL_3_REG)) & 0xf0000000 | (0x0<<24) | (0x0<<22) | (dis_phase<<21) | (0x0<<19) | (tone3_en<<18) | (tone3_atten<<10) | reg_freq_3;  //inv[3:0], phase_cfg[1:0], dis_phase, iq_sel[1:0], tone_en, atten, freq  
}

void stop_tx_tone(int tone_no)
{
  switch(tone_no){
     case 1: 
        *(volatile U32*)(FE_TX_TEST_CTRL_0_REG) = (*(volatile U32*)(FE_TX_TEST_CTRL_0_REG)) & 0xfffbffff | (0x0<<18);  //tone_en_1
	break;
     case 2: 
        *(volatile U32*)(FE_TX_TEST_CTRL_1_REG) = (*(volatile U32*)(FE_TX_TEST_CTRL_1_REG)) & 0xfffbffff | (0x0<<18);  //tone_en_2
	break;
     case 3: 
        *(volatile U32*)(FE_TX_TEST_CTRL_3_REG) = (*(volatile U32*)(FE_TX_TEST_CTRL_3_REG)) & 0xfffbffff | (0x0<<18);  //tone_en_2
	break;
     default: 
//        *(volatile U32*)(BB_ADC_PARALLEL_CONTROL) = (*(volatile U32*)(BB_ADC_PARALLEL_CONTROL)) & 0xffffdfff | (0x1<<13);  //release dacon
        *(volatile U32*)(FE_TX_TEST_CTRL_3_REG) = (*(volatile U32*)(FE_TX_TEST_CTRL_3_REG)) & 0xfffbffff | (0x0<<18);  //tone_en
        *(volatile U32*)(FE_TX_TEST_CTRL_1_REG) = (*(volatile U32*)(FE_TX_TEST_CTRL_1_REG)) & 0xfffbffff | (0x0<<18);  //tone_en
        *(volatile U32*)(FE_TX_TEST_CTRL_0_REG) = (*(volatile U32*)(FE_TX_TEST_CTRL_0_REG)) & 0xfffbffff | (0x0<<18);  //tone_en
        set_txclk_en(0);
        pbus_force_mode_v60(1);
        pbus_force_test_v60(RFTX1, EN1, 0x0, 0, 0, 0);
        pbus_force_test_v60(BB, EN1, 0x188, 0, 0, 0);
        pbus_force_test_v60(RFRX1, EN1, 0x184, 0, 0, 0);
        pbus_force_mode_v60(0);
     break;
  }
}

void iq_est(int freq, int atten, int length, int loop)  //calculate: (length+1)*(loop+1)
{
  int result0, result1, result2, result3, result4, result2_1, result2_2, result2_3, result2_4;

  start_tx_tone(1, freq, atten, 0, freq, atten, 0, freq, atten);  //void start_tx_tone(int tone1_en, float freq_1_mhz, int tone1_atten, int tone2_en, float freq_2_mhz, int tone2_atten, int tone3_en, float freq_3_mhz, int tone3_atten)

  delay_us(50);

  *(volatile U32*)(FE_PUBS_CTRL3_REG) = (*(volatile U32*)(FE_PUBS_CTRL3_REG)) & 0xfffc3fff | (0xf<<14);  //force tx/rx_on
  *(volatile U32*)(FE2_TX_DC_CTRL_REG) = (*(volatile U32*)(FE2_TX_DC_CTRL_REG)) & ~FE2_LOOP_BACK_EN | (0x1<<FE2_LOOP_BACK_EN_S);  //ana_inf loopback

  *(volatile U32*)(FE_IQ_EST_CTRL_00_REG) = (*(volatile U32*)(FE_IQ_EST_CTRL_00_REG)) & 0xfffffffe | 0x1;  //clk_en
  *(volatile U32*)(FE_IQ_LOOP_CTRL_REG) = (*(volatile U32*)(FE_IQ_LOOP_CTRL_REG)) & 0xffffff00 | loop;  //loop_num
  *(volatile U32*)(FE_IQ_EST_CTRL_00_REG) = (*(volatile U32*)(FE_IQ_EST_CTRL_00_REG)) & 0xfffe0001 | (length<<2) | (0x1<<1);  //length, est_en
  while(((*(volatile U32*)(FE_IQ_LOOP_CTRL_REG)) & FE_IQ_EST_DONE)==0){};  //wait untill iq est done
  //read result
  result0 = (*(volatile U32*)(FE_IQ_LOOP_CTRL_REG));
  result1 = (*(volatile U32*)(FE_IQ_RESULT1_REG));
  result2 = (*(volatile U32*)(FE_IQ_RESULT2_REG));
  result3 = (*(volatile U32*)(FE_IQ_RESULT3_REG));
  result4 = (*(volatile U32*)(FE_IQ_RESULT4_REG));
  *(volatile U32*)(FE_IQ_EST_CTRL_00_REG) = (*(volatile U32*)(FE_IQ_EST_CTRL_00_REG)) & 0xfffffffd | (0x0<<1);  //est_en=0
  *(volatile U32*)(FE_IQ_EST_CTRL_00_REG) = (*(volatile U32*)(FE_IQ_EST_CTRL_00_REG)) & 0xfffffffe | 0x0;  //clk_en=0

  *(volatile U32*)(FE_PUBS_CTRL3_REG) = (*(volatile U32*)(FE_PUBS_CTRL3_REG)) & 0xfffc3fff | (0x0<<14);  //force tx/rx_on
  *(volatile U32*)(FE2_TX_DC_CTRL_REG) = (*(volatile U32*)(FE2_TX_DC_CTRL_REG)) & ~FE2_LOOP_BACK_EN | (0x0<<FE2_LOOP_BACK_EN_S);  //en ana_inf loopback

  stop_tx_tone(0);  //void stop_tx_tone(int tone_no)

}

// int dump_from_adc()
// {
//   mac_write(REG_PROAPB_CTRL_BASE + 0x24, 0x00000004);
//   mac_write(WDEVADCDUMP0_REG, 0x8000ffff);
//   mac_write(WDEVADCDUMP0_REG, 0x80007fff);
//   mac_write(WDEVADCDUMP0_REG, 0x0);
// }

//*********************************************************************************************************
//set_tx_interp_en(1, 1000000, (1000000+200), 250, 250)
void set_tx_interp_en(unsigned int tx_interp_en, unsigned int freq_rf, unsigned int freq_dig, int tx_delay, int dac_delay)
{
   if(tx_interp_en == 0){
       tx_delay = 0;
       dac_delay = 0;
       SET_PERI_REG_MASK(FE2_TX_DC_CTRL_REG, FE2_TX_INTERP_BYPASS);
   }else{
       SET_PERI_REG_BITS(FE2_FREQ_CTRL1_REG, FE2_FREQ_RF_A, freq_rf, FE2_FREQ_RF_A_S);
       SET_PERI_REG_BITS(FE2_FREQ_CTRL2_REG, FE2_FREQ_DIG_B, freq_dig, FE2_FREQ_DIG_B_S);
       CLEAR_PERI_REG_MASK(FE2_TX_DC_CTRL_REG, FE2_TX_INTERP_BYPASS);
   }
   SET_PERI_REG_BITS(FE2_TX_INTERP_CTRL_REG, FE2_TX_INTERP_DELAY, tx_delay, FE2_TX_INTERP_DELAY_S); 
   SET_PERI_REG_BITS(BB_FSM_CTRL_REG, BB_TX_WAIT_DELAY, dac_delay, BB_TX_WAIT_DELAY_S); //dac_on_delay
}

void dpd_set_en(int bypass, int index, int mult, int shift)
{
    SET_PERI_REG_BITS(FE2_DPD_CFG1_REG, FE2_DPD_INTERP_MULT, mult, FE2_DPD_INTERP_MULT_S);
    SET_PERI_REG_BITS(FE2_DPD_CFG1_REG, FE2_DPD_INTERP_SHIFT, shift, FE2_DPD_INTERP_SHIFT_S);
    SET_PERI_REG_BITS(FE2_DPD_CFG1_REG, FE2_DPD_INDEX1, index, FE2_DPD_INDEX1_S);
    //SET_PERI_REG_BITS(FE2_DPD_CFG1_REG, FE2_DPD_GAIN_SAT, 512, FE2_DPD_GAIN_SAT_S);
    SET_PERI_REG_BITS(FE2_TX_MASK_CTRL_REG, 1, bypass, FE2_DPD_BYPASS_S);
}

// write dpd table
//void dpd_table_wr(void)
//{
//    int i, data, rd_data, addr;
//    data = 10;
//    for(i=0; i<256; i++){
//        addr = i;
//        data = i;
//        SET_PERI_REG_BITS(FE2_FREQ_CTRL1_REG, FE2_DPD_TAB_Q, data, FE2_DPD_TAB_Q_S);
//        SET_PERI_REG_BITS(FE2_FREQ_CTRL2_REG, FE2_DPD_TAB_I, data, FE2_DPD_TAB_I_S);
//        SET_PERI_REG_BITS(FE2_TX_MASK_CTRL_REG, FE2_DPD_TAB_ADDR, addr, FE2_DPD_TAB_ADDR_S);
//        SET_PERI_REG_MASK(FE2_TX_MASK_CTRL_REG, FE2_DPD_TAB_WR);
//        CLEAR_PERI_REG_MASK(FE2_TX_MASK_CTRL_REG, FE2_DPD_TAB_WR);
//    }
//    for(i=0; i<10; i++){
//        addr = i;
//        data = (i<<12) + i;
//        SET_PERI_REG_BITS(FE2_TX_MASK_CTRL_REG, FE2_DPD_TAB_ADDR, addr, FE2_DPD_TAB_ADDR_S);
//        SET_PERI_REG_MASK(FE2_TX_MASK_CTRL_REG, FE2_DPD_TAB_RD);
//        CLEAR_PERI_REG_MASK(FE2_TX_MASK_CTRL_REG, FE2_DPD_TAB_RD);
//        rd_data = GET_PERI_REG_BITS(FE2_DPD_MEM_DATA, FE2_DPD_MEM_READ, FE2_DPD_MEM_READ_S);
//        if (rd_data != data) fail("Diag Failed\n");
//    }
//}

//*********************************************************************************************************
// analog interface HT20 SYS_CLK no gating mode
void ana_inf_ht20_no_gating_mode()
{
}

// analog interface HT20 SYS_CLK gating mode
void ana_inf_ht20_gating_mode(unsigned int freq_rf, unsigned int freq_dig)
{
}

// analog interface dump mode
void ana_inf_dump_mode()
{
}

// analog interface dump mode
void ana_inf_ht40_mode()
{
}
void adc_mode(int adc_160m){
   SET_PERI_REG_BITS(FE2_FE_RX_SCALE_REG, 0x1, adc_160m, FE2_FE_RX_IN_160M_S);
   SET_PERI_REG_BITS(FE2_FE_RX_SCALE_REG, 0x1, ~adc_160m, FE2_FE_RX_IN_80M_S);
   //SET_PERI_REG_BITS(FE2_TX_TONE_CTRL_REG,0x1,adc_160m,FE2_ADC_160M_DSP_S);
   //SET_PERI_REG_BITS(FE_GEN_CTRL_REG,0x1,~adc_160m,FE_ADC_80M_DSP_S);
}
void bb_bss_bw_40_en(int bb_ht_2040)
{
   SET_PERI_REG_BITS(APB_CTRL_WIFI_BB_CFG_REG, 0x3, bb_ht_2040, 2);
}

void clk_force_on_vit(int force_on)
{   //clk_force_on_vit
   SET_PERI_REG_BITS(NRXVIT_REG, 0x1, force_on, 0);
}

void bb_rx_ht20_cen_bcov_en(int rx_ht20_cen_bcov_en)
{
     SET_PERI_REG_BITS(BB_CTRL0_REG, 0x1, rx_ht20_cen_bcov_en, 6);
}

/* void bb_tx_ht20_cen(int tx_ht20_cen_en) */
/* { */
/*      SET_PERI_REG_BITS(WDEVOPTIONS_REG, 0x1, tx_ht20_cen_en, 27); */
/* } */

void spur_reg_write()
{  
    int tone_coef_1, tone_coef_1_abs;
    int sc_index_b;  //subcarrier base(coef*(80m/1024/8))/(20m/64)
    int sc_pos;  //unit: 1/4 subcarrier from base
    int sc_coeff_b, sc_coeff_r, sc_coeff_l;  //mask-coeff of subcarrier base and right/left
    int addr_offset_b, addr_offset_r, addr_offset_l;  //reg-addr of subcarrier base and right/left
    int bit_offset_b, bit_offset_r, bit_offset_l;  //bit-offset in reg of subcarrier base and right/left

    sc_coeff_l = 0;  //default

    //tone_shift_max_1 = ((READ_PERI_REG(BB_TONE_CTRL_1_REG) & 0x70000000) >> 28); //reg_tone_shift_max_1_fft[30:28]
    tone_coef_1  = ((READ_PERI_REG(BB_TONE_CTRL_1_REG)>>13) & 0x1)? (READ_PERI_REG(BB_TONE_CTRL_1_REG) & 0x1fff) : 0; //reg_tone_est_coef_1 [12:0]
    if((tone_coef_1>>12)&0x1){
        tone_coef_1 = tone_coef_1 - 8192;
        tone_coef_1_abs = -tone_coef_1;
    }else{
        tone_coef_1_abs = tone_coef_1;
    }

    sc_index_b = tone_coef_1_abs/32;
    sc_pos     = (tone_coef_1_abs%32)/4;
    if(tone_coef_1<0){
        sc_index_b = -sc_index_b - 1;
        sc_pos     = 7 - sc_pos;
    }else if(tone_coef_1==0){
        sc_pos     = 64;
    }

    //close 2 sub-carrier at most
    switch(sc_pos){
        case 0: sc_coeff_b = 2; sc_coeff_r = 0; break;
        case 1: sc_coeff_b = 2; sc_coeff_r = 0; break;
        case 2: sc_coeff_b = 2; sc_coeff_r = 1; break;
        case 3: sc_coeff_b = 1; sc_coeff_r = 1; break;
        case 4: sc_coeff_b = 1; sc_coeff_r = 1; break;
        case 5: sc_coeff_b = 1; sc_coeff_r = 2; break;
        case 6: sc_coeff_b = 0; sc_coeff_r = 2; break;
        case 7: sc_coeff_b = 0; sc_coeff_r = 2; break;
        default: sc_coeff_b = 0; sc_coeff_r = 0; break;
    }
    
    //test for mcs0
    //sc_coeff_b = 3; sc_coeff_r = 3; sc_coeff_l = 3;

    *(volatile U32*)(NRXSPURV0_REG) = 0;  //15~0
    *(volatile U32*)(NRXSPURV1_REG) = 0;  //31~16
    *(volatile U32*)(NRXSPURV2_REG) = 0;  //47~32
    *(volatile U32*)(NRXSPURV3_REG) = 0;  //63~48
    *(volatile U32*)(NRXSPURV4_REG) = 0;  //-49~-64
    *(volatile U32*)(NRXSPURV5_REG) = 0;  //-33~-48
    *(volatile U32*)(NRXSPURV6_REG) = 0;  //-17~-32
    *(volatile U32*)(NRXSPURV7_REG) = 0;  //-1~-16

    if(tone_coef_1<0){
        addr_offset_b = (sc_index_b+64)/16 + 4;
        addr_offset_r = (sc_index_b+1+64)/16 + 4;
        addr_offset_l = (sc_index_b-1+64)/16 + 4;
        bit_offset_b = ((64+sc_index_b)%16) * 2;
        bit_offset_r = ((64+sc_index_b+1)%16) * 2;
        bit_offset_l = ((64+sc_index_b-1)%16) * 2;
    }else{
        addr_offset_b = sc_index_b/16;
        addr_offset_r = (sc_index_b+1)/16;
        addr_offset_l = (sc_index_b-1)/16;
        bit_offset_b = (sc_index_b%16) * 2;
        bit_offset_r = ((sc_index_b+1)%16) * 2;
        bit_offset_l = ((sc_index_b-1)%16) * 2;
    }

    *(volatile U32*)(NRXSPURV0_REG + addr_offset_b*4) = *(volatile U32*)(NRXSPURV0_REG + addr_offset_b*4) & ~(3<< bit_offset_b) | (sc_coeff_b << bit_offset_b);
    *(volatile U32*)(NRXSPURV0_REG + addr_offset_r*4) = *(volatile U32*)(NRXSPURV0_REG + addr_offset_r*4) & ~(3<< bit_offset_r) | (sc_coeff_r << bit_offset_r);
    *(volatile U32*)(NRXSPURV0_REG + addr_offset_l*4) = *(volatile U32*)(NRXSPURV0_REG + addr_offset_l*4) & ~(3<< bit_offset_l) | (sc_coeff_l << bit_offset_l);

    printinfo("coeff  = ", tone_coef_1);
    printinfo("index  = ", sc_index_b);
    printinfo("sc_pos = ", sc_pos);
    printinfo("addr_b = ", addr_offset_b);
    printinfo("addr_r = ", addr_offset_r);
    printinfo("bit_b  = ", bit_offset_b);
    printinfo("bit_r  = ", bit_offset_r);

}
int spur_cal(int freq,int BW_h, int spur_freq_cfg,int spur_freq_cfg_div)
{
//freq :2432 2437 2442 2447
//BW_h: 10
//spur_freq_cfg:40
//spur_freq_cfg_div:1
    int data1,data2,data3;
    int fspur;
    if((spur_freq_cfg_div!=0)&&(spur_freq_cfg!=0)){
        data1 = freq*spur_freq_cfg_div/spur_freq_cfg;
        data2 = freq*10 - spur_freq_cfg*data1*10/spur_freq_cfg_div;
        data3 = spur_freq_cfg*(data1+1)*10/spur_freq_cfg_div - freq*10;
        printinfo("data2 = ", data2);
        printinfo("data3  = \n", data3);        

        if(data2<(BW_h*10)){
            fspur = -data2;//unit:0.1M
        }else if(data3<(BW_h*10)){
            fspur = data3;
        }else{
            fspur = 0;
        }
    }else{
        fspur = 0;
    }
//    fspur_coef = fspur*1024/100;
    printinfo("fspur  = \n", fspur);  
    return fspur;
}

void spur_reg_write_one_tone(tone_ctrl_reg,spur_reg0,spur_reg1,spur_reg8)
{  
    int tone_coef_1, tone_coef_1_abs;
    int sc_index_b;  //subcarrier base(coef*(80m/1024/8))/(20m/64)
    int sc_pos;  //unit: 1/4 subcarrier from base
    int sc_coeff_b, sc_coeff_r, sc_coeff_l, sc_coeff_r2, sc_coeff_l2;  //mask-coeff of subcarrier base and right/left
    int addr_offset_b, addr_offset_r, addr_offset_l;  //reg-addr of subcarrier base and right/left
    int bit_offset_b, bit_offset_r, bit_offset_l, bit_offset_r2, bit_offset_l2;  //bit-offset in reg of subcarrier base and right/left

    sc_coeff_l = 0;  //default
    sc_coeff_r = 0;  //default
    sc_coeff_r2 = 0; //default
    sc_coeff_l2 = 0; //default

    //tone_shift_max_1 = ((READ_PERI_REG(tone_ctrl_reg) & 0x70000000) >> 28); //reg_tone_shift_max_1_fft[30:28]
    tone_coef_1  = ((READ_PERI_REG(tone_ctrl_reg)>>13) & 0x1)? (READ_PERI_REG(tone_ctrl_reg) & 0x1fff) : 0; //reg_tone_est_coef_1 [12:0]
    if((tone_coef_1>>12)&0x1){
        tone_coef_1 = tone_coef_1 - 8192;
        tone_coef_1_abs = -tone_coef_1;
    }else{
        tone_coef_1_abs = tone_coef_1;
    }

    sc_index_b = (tone_coef_1_abs+16)/32;  //get the nearest integer
    sc_pos     = (tone_coef_1_abs - sc_index_b*32)/4;  //-4~+3
    if((tone_coef_1==0)||(sc_index_b>61)){
        sc_pos     = 64;  //not valid
    }else if(tone_coef_1<0){
        sc_index_b = -sc_index_b;
        sc_pos     = -sc_pos;
    }

    *(volatile U32*)(spur_reg0) = 0;  //tone1
    *(volatile U32*)(spur_reg1) = 0;  

    //mcs0 close 5 sub-carrier at most 
    switch(sc_pos){
        case -4:  sc_coeff_l2 = 2; sc_coeff_l = 3; sc_coeff_b = 3; sc_coeff_r = 2; sc_coeff_r2 = 0; break;
        case -3:  sc_coeff_l2 = 2; sc_coeff_l = 3; sc_coeff_b = 3; sc_coeff_r = 2; sc_coeff_r2 = 0; break;
        case -2:  sc_coeff_l2 = 2; sc_coeff_l = 3; sc_coeff_b = 3; sc_coeff_r = 2; sc_coeff_r2 = 0; break;
        case -1:  sc_coeff_l2 = 2; sc_coeff_l = 3; sc_coeff_b = 3; sc_coeff_r = 3; sc_coeff_r2 = 1; break;
        case  0:  sc_coeff_l2 = 2; sc_coeff_l = 3; sc_coeff_b = 3; sc_coeff_r = 3; sc_coeff_r2 = 2; break;
        case  1:  sc_coeff_l2 = 1; sc_coeff_l = 3; sc_coeff_b = 3; sc_coeff_r = 3; sc_coeff_r2 = 2; break;
        case  2:  sc_coeff_l2 = 0; sc_coeff_l = 2; sc_coeff_b = 3; sc_coeff_r = 3; sc_coeff_r2 = 2; break;
        case  3:  sc_coeff_l2 = 0; sc_coeff_l = 2; sc_coeff_b = 3; sc_coeff_r = 3; sc_coeff_r2 = 2; break;
        case  4:  sc_coeff_l2 = 0; sc_coeff_l = 2; sc_coeff_b = 3; sc_coeff_r = 3; sc_coeff_r2 = 2; break;
        default: sc_coeff_l2 = 0; sc_coeff_l = 0; sc_coeff_b = 0; sc_coeff_r = 0; sc_coeff_r2 = 0; break;
    }
    *(volatile U32*)(spur_reg0) = *(volatile U32*)(spur_reg0) & ~(0x3ff << 0 ) | (sc_coeff_l2 << 0) |  (sc_coeff_l << 2) | (sc_coeff_b << 4) | (sc_coeff_r << 6) | (sc_coeff_r2 << 8) ;
    //mcs1 close 5 sub-carrier at most 
    *(volatile U32*)(spur_reg0) = *(volatile U32*)(spur_reg0) & ~(0x3ff << 10 ) | (((sc_coeff_l2 << 0) |  (sc_coeff_l << 2) | (sc_coeff_b << 4) | (sc_coeff_r << 6) | (sc_coeff_r2 << 8)) << 10) ;

    //mcs2 close 5 sub-carrier at most 
    *(volatile U32*)(spur_reg0) = *(volatile U32*)(spur_reg0) & ~(0x3ff << 20 ) | (((sc_coeff_l2 << 0) |  (sc_coeff_l << 2) | (sc_coeff_b << 4) | (sc_coeff_r << 6) | (sc_coeff_r2 << 8)) << 20) ;

    //mcs3 close 3 sub-carrier at most
    switch(sc_pos){
        case -4:  sc_coeff_l = 3; sc_coeff_b = 3; sc_coeff_r = 0; break;
        case -3:  sc_coeff_l = 3; sc_coeff_b = 3; sc_coeff_r = 0; break;
        case -2:  sc_coeff_l = 2; sc_coeff_b = 3; sc_coeff_r = 1; break;
        case -1:  sc_coeff_l = 2; sc_coeff_b = 3; sc_coeff_r = 2; break;
        case  0:  sc_coeff_l = 2; sc_coeff_b = 3; sc_coeff_r = 2; break;
        case  1:  sc_coeff_l = 2; sc_coeff_b = 3; sc_coeff_r = 2; break;
        case  2:  sc_coeff_l = 1; sc_coeff_b = 3; sc_coeff_r = 2; break;
        case  3:  sc_coeff_l = 0; sc_coeff_b = 3; sc_coeff_r = 3; break;
        case  4:  sc_coeff_l = 0; sc_coeff_b = 3; sc_coeff_r = 3; break;
        default: sc_coeff_l = 0; sc_coeff_b = 0; sc_coeff_r = 0; break;
    }
    *(volatile U32*)(spur_reg1) = *(volatile U32*)(spur_reg1) & ~(0x3f << 0) | (((sc_coeff_l << 0) | (sc_coeff_b << 2) | (sc_coeff_r << 4) ) << 0);

    //mcs4 close 3 sub-carrier at most
    *(volatile U32*)(spur_reg1) = *(volatile U32*)(spur_reg1) & ~(0x3f << 6) | (((sc_coeff_l << 0) | (sc_coeff_b << 2) | (sc_coeff_r << 4) ) << 6);

    //mcs5 close 3 sub-carrier at most
    switch(sc_pos){
        case -4:  sc_coeff_l = 2; sc_coeff_b = 2; sc_coeff_r = 0; break;
        case -3:  sc_coeff_l = 2; sc_coeff_b = 2; sc_coeff_r = 0; break;
        case -2:  sc_coeff_l = 1; sc_coeff_b = 3; sc_coeff_r = 0; break;
        case -1:  sc_coeff_l = 1; sc_coeff_b = 3; sc_coeff_r = 1; break;
        case  0:  sc_coeff_l = 1; sc_coeff_b = 3; sc_coeff_r = 1; break;
        case  1:  sc_coeff_l = 1; sc_coeff_b = 3; sc_coeff_r = 2; break;
        case  2:  sc_coeff_l = 0; sc_coeff_b = 3; sc_coeff_r = 1; break;
        case  3:  sc_coeff_l = 0; sc_coeff_b = 2; sc_coeff_r = 2; break;
        case  4:  sc_coeff_l = 0; sc_coeff_b = 2; sc_coeff_r = 2; break;
        default: sc_coeff_l = 0; sc_coeff_b = 0; sc_coeff_r = 0; break;
    }
    *(volatile U32*)(spur_reg1) = *(volatile U32*)(spur_reg1) & ~(0x3f << 12) | (((sc_coeff_l << 0) | (sc_coeff_b << 2) | (sc_coeff_r << 4) ) << 12);

    //mcs6 close 2 sub-carrier at most
    switch(sc_pos){
        case -4:  sc_coeff_l = 1; sc_coeff_b = 1; sc_coeff_r = 0; break;
        case -3:  sc_coeff_l = 1; sc_coeff_b = 1; sc_coeff_r = 0; break;
        case -2:  sc_coeff_l = 1; sc_coeff_b = 2; sc_coeff_r = 0; break;
        case -1:  sc_coeff_l = 1; sc_coeff_b = 2; sc_coeff_r = 0; break;
        case  0:  sc_coeff_l = 1; sc_coeff_b = 2; sc_coeff_r = 1; break;
        case  1:  sc_coeff_l = 0; sc_coeff_b = 2; sc_coeff_r = 1; break;
        case  2:  sc_coeff_l = 0; sc_coeff_b = 2; sc_coeff_r = 1; break;
        case  3:  sc_coeff_l = 0; sc_coeff_b = 1; sc_coeff_r = 1; break;
        case  4:  sc_coeff_l = 0; sc_coeff_b = 1; sc_coeff_r = 1; break;
        default: sc_coeff_l = 0; sc_coeff_b = 0; sc_coeff_r = 0; break;
    }
    *(volatile U32*)(spur_reg1) = *(volatile U32*)(spur_reg1) & ~(0x3f << 18) | (((sc_coeff_l << 0) | (sc_coeff_b << 2) | (sc_coeff_r << 4) ) << 18);

    //mcs7 close 2 sub-carrier at most
    switch(sc_pos){
        case -4:  sc_coeff_l = 1; sc_coeff_b = 1; sc_coeff_r = 0; break;
        case -3:  sc_coeff_l = 1; sc_coeff_b = 1; sc_coeff_r = 0; break;
        case -2:  sc_coeff_l = 0; sc_coeff_b = 2; sc_coeff_r = 0; break;
        case -1:  sc_coeff_l = 0; sc_coeff_b = 2; sc_coeff_r = 0; break;
        case  0:  sc_coeff_l = 0; sc_coeff_b = 2; sc_coeff_r = 0; break;
        case  1:  sc_coeff_l = 0; sc_coeff_b = 2; sc_coeff_r = 0; break;
        case  2:  sc_coeff_l = 0; sc_coeff_b = 2; sc_coeff_r = 0; break;
        case  3:  sc_coeff_l = 0; sc_coeff_b = 1; sc_coeff_r = 1; break;
        case  4:  sc_coeff_l = 0; sc_coeff_b = 1; sc_coeff_r = 1; break;
        default: sc_coeff_l = 0; sc_coeff_b = 0; sc_coeff_r = 0; break;
    }
    *(volatile U32*)(spur_reg1) = *(volatile U32*)(spur_reg1) & ~(0x3f << 24) | (((sc_coeff_l << 0) | (sc_coeff_b << 2) | (sc_coeff_r << 4) ) << 24);

    //position
    *(volatile U32*)(spur_reg8) = *(volatile U32*)(spur_reg8) & ~(0x7f << 0) | (sc_index_b << 0);


    printinfo("coeff  = ", tone_coef_1);
    printinfo("index  = ", sc_index_b);
    printinfo("sc_pos = \n", sc_pos);
}

void tx_interp_test_en(int tx_interp_en)
{
   int ppm, rxppm, brx_ptr, freq_rf, freq_dig, nrx_ppm_force, brx_ppm_force, tx_delay, dac_on_wait;

   ppm = 200;
   if(ppm > 0){
       freq_rf  = 1000000+ppm;
       freq_dig = 1000000;
       tx_delay = 2;
       dac_on_wait = 250;
   }else{
       freq_rf  = 1000000;
       freq_dig = 1000000-ppm;
       tx_delay = 250;
       dac_on_wait = 250;
   }
   rxppm = -ppm;
   nrx_ppm_force = rxppm;  //2^21*4/3.2*10^-6=2.62144~=21/8
   brx_ppm_force = rxppm;

    if(rxppm < 0) brx_ptr = 61;
    else if(rxppm > 0) brx_ptr = 2;
    else brx_ptr = 32;

   if(tx_interp_en){
       SET_PERI_REG_BITS(NRXPILOTCONF2_REG, NRX_SLOPE_FIX, nrx_ppm_force, NRX_SLOPE_FIX_S);
       SET_PERI_REG_BITS(BRXTIM_PPM_COM_REG, BRX_TIM_PPM_CORRECT, brx_ppm_force, BRX_TIM_PPM_CORRECT_S);
       SET_PERI_REG_BITS(BRXTIM_PPM_COM_REG, BRX_TIM_CORRECT_PTR, brx_ptr, BRX_TIM_CORRECT_PTR_S);           
   }

}

void bb_wdg_test_en(int wdg_srch_en, int wdg_busy_en, int wdg_srch_thr, int wdg_busy_thr, int rst_en, int int_clr)
{
   *(volatile U32*)(BB_WDG_0_REG) = (wdg_busy_en<<BB_WDG_BUSY_CHK_S) |
                                (wdg_srch_en<<BB_WDG_SRCH_CHK_S) | 
                                (wdg_busy_thr<<BB_WDG_MAX_BUSY_S) | 
                                (wdg_srch_thr<<BB_WDG_MAX_SRCH_S);
   *(volatile U32*)(BB_WDG_1_REG) = (rst_en<<BB_WDG_RST_EN_S) |
                                (1<<BB_WDG_INT_EN_S) | 
                                (int_clr<<BB_WDG_CLR_S);
}

void ana_inf_init(int ht2040_mode)
{
  adc_mode(ht2040_mode);
  bb_bss_bw_40_en(ht2040_mode);//enable bb_ht_2040

  //for testbench's sim only
  SET_PERI_REG_BITS(FE2_FE_RX_SYN3_2_REG, 1, (ht2040_mode? 0 : 1), FE2_RX_480DET_ADC80_S);
}

void bb_init(int init_mode)
{
  
  int ana_mode = init_mode & 0x1;
  int re_init = (init_mode >> 1) & 0x1;
  int ht2040_mode = (init_mode >> 2) & 0x1;

  //SET_PERI_REG_BITS(RTC_CLK_CONF, APB_CTRL_SOC_CLK_SEL, 1, APB_CTRL_SOC_CLK_SEL_S);  //sel soc clk
  SET_PERI_REG_BITS(APB_CTRL_SYSCLK_CONF_REG, APB_CTRL_SOC_CLK_SEL, 1, APB_CTRL_SOC_CLK_SEL_S);  //sel soc clk: use pll

  SET_PERI_REG_BITS(APB_CTRL_SYSCLK_CONF_REG, (APB_CTRL_CLK_320M_EN>>APB_CTRL_CLK_320M_EN_S), 1, APB_CTRL_CLK_320M_EN_S);  //clk320m_en

  *(volatile U32*)(APB_CTRL_WIFI_BB_CFG_REG)= *(volatile U32*) (APB_CTRL_WIFI_BB_CFG_REG) & 0xfffffffd | (0x0<<1);  //enable bb
  SET_PERI_REG_BITS(FE2_FE_RX_SYN3_2_REG, 1, 1, FE2_RX_SYNC_DBG_CLR_S);  //clr debug cnt

  ana_inf_init(ht2040_mode);

  if(re_init==0){
#ifdef CHIP_ANA_MODE_SIM
     //slv_diag_dis(1);
     //mux_half_rate(0);
#endif
     //set_rx_dcmem_simu_v60();
   
     set_pbus_mem();
#if BB_NOT_POST_SIM
     set_rx_gain_simu_v52(96);//agcmem
#endif
     set_tx_gain(16);
     set_tx_rate_map();   
   
     //i2c_mst opt
     *(volatile U32*)(REG_I2C_BASE + 0x20) = (0x1<<7);
     *(volatile U32*)(REG_I2C_BASE + 0x24) = (0x1<<7);
     *(volatile U32*)(REG_I2C_BASE + 0x28) = (0x1<<7);
     *(volatile U32*)(REG_I2C_BASE + 0x2c) = (0x1<<7);
     *(volatile U32*)(REG_I2C_BASE + 0x30) = (0x1<<7);
   
   
     if(ana_mode)
     {
       //*(volatile U32*)(FE_HOST_FPGA) = *(volatile U32*)(FE_HOST_FPGA) & 0xfffffffe | 0x1;  //chip_ana_mode sel i2c enable
     }
     //i2c_ana_wr(REG_I2C_BASE + 0x00, 0x77, 18, 0, 0xff);  //rx scale
     SET_PERI_REG_BITS(FE2_SCALE_CTRL_REG, FE2_RX_SCALE, 0, FE2_RX_SCALE_S);
     //enable rx phase det
     //i2c_ana_wr(REG_I2C_BASE + 0x00, 0x77, 29, 0x1, 0x20);
     //i2c_ana_wr(REG_I2C_BASE + 0x00, 0x77, 29, 0x0, 0x20);
   
     if(ana_mode)
     {
       //*(volatile U32*)(FE_HOST_FPGA) = *(volatile U32*)(FE_HOST_FPGA) & 0xfffffffe | 0x0;  //chip_ana_mode sel i2c disable
     }
   
     //bug begin
     //*(volatile U32*)(AGCDC_CTRL2_REG) = (*(volatile U32*)(AGCDC_CTRL2_REG)) & 0xfffeffff | (0<<16);  //rx_dc_init_en
     //bug end
   
     //for analog-mode
     //*(volatile U32*)(AGCFSM_CTRL2_REG) = *(volatile U32*)(AGCFSM_CTRL2_REG) & 0xffffff80 | 0x2f;
   
     //change for agc_rx_filter
     //*(volatile U32*)(AGCPWR_CTRL3_REG) = (*(volatile U32*)(AGCPWR_CTRL3_REG)) & 0xfffffe00 | (0x1c4<<0);  //sat_thr
      
     //fs_vs_f_para(fs / f_rf * (1<<shift))
     //for 2437: 278229@ht40
     //for 2437: 275375@ht40
     //for 2462: 272579@ht40
     //for 2484: 270165@ht40
     //for 2494: 269081@ht40
     //for 2504: 268007@ht40
      SET_PERI_REG_BITS(NRXFREQPARA_REG, 0xffffff, 275375, 0x0);
      SET_PERI_REG_BITS(NRXFREQPARA_REG, 0xff, 23, 24);
   
     //*(volatile U32*)(AGCPWR_CTRL7_REG) = *(volatile U32*)(AGCPWR_CTRL7_REG) & 0xffffff00 | 0xfe;  //gain comp
   
     //rifs
     //*(volatile U32*)(AGCFSM_CTRL1_REG) = *(volatile U32*)(AGCFSM_CTRL1_REG) & 0xfffbffff | (0x1<<18);  //rifs_mode
   
     //*(volatile U32*)(AGCFSM_CTRL2_REG) = *(volatile U32*)(AGCFSM_CTRL2_REG) & 0xffffff80 | (0x28<<0);  //
   
     //force tx seed
     *(volatile U32*)(BBTXCONF_REG) = *(volatile U32*)(BBTXCONF_REG) & 0xffffff00 | (0x1<<7) | 0x10;  //force_en, seed
   
     //force rx ffo
     //*(volatile U32*)(NRXTDM1_REG) = *(volatile U32*)(NRXTDM1_REG) & 0xe0007fff | (0x0<<16) | (0x1<<15);  //ffo, force_en
   
     //set rx fte
     //*(volatile U32*)(NRXTE) = *(volatile U32*)(NRXTE) & 0xffffe03f | (0x15<<6);  //fte
   
     //rx scale(test)
     //*(volatile U32*)(NRXSCALE_REG) = *(volatile U32*)(NRXSCALE_REG) & 0xffffff83 | (0x2<<4) | (0x0<<2);  //mult, shr
     //for sim only
     //*(volatile U32*)(FE_PUBS_CFG5_REG) = *(volatile U32*)(FE_PUBS_CFG5_REG) & 0xffff00ff | (0x30<<8);//paon_t_bt
     //*(volatile U32*)(FE_PUBS_CFG6_REG) = *(volatile U32*)(FE_PUBS_CFG6_REG) & 0xffff00ff | (0x30<<8);//paon_t
   
     *(volatile U32*)(BBTXANALOG_CTRL1_REG) = (*(volatile U32*)(BBTXANALOG_CTRL1_REG)) & 0xfff00fff | (0xd0<<12);  //rx_rssi(signed, 8bit, unit:dbm)

  }

  //tone rm set(-4Mhz)
  //*(volatile U32*)(BB_TONE_CTRL_1_REG)      = *(volatile U32*) (BB_TONE_CTRL_1_REG) & 0xffffe000 | (0x198<<0);  //tone coef
  //spur_reg_write_one_tone(BB_TONE_CTRL_1_REG,NRXSPURV0_REG,NRXSPURV1_REG,NRXSPURV8_REG);
  *(volatile U32*)(BB_TONE_CTRL_1_REG)      = *(volatile U32*) (BB_TONE_CTRL_1_REG) & 0xffffe000 | (0x1e67<<0);  //tone coef
  spur_reg_write_one_tone(BB_TONE_CTRL_1_REG,NRXSPURV0_REG,NRXSPURV1_REG,NRXSPURV8_REG);  //coef_en's default value is 0, so this will write nothing

  *(volatile U32*)(APB_CTRL_WIFI_BB_CFG_REG)      = *(volatile U32*) (APB_CTRL_WIFI_BB_CFG_REG) & 0xfefffffd | (0x1<<28);  //for new BB
  *(volatile U32*)(APB_CTRL_WIFI_BB_CFG_REG)      = *(volatile U32*) (APB_CTRL_WIFI_BB_CFG_REG) & 0xfffffffd | (0x1<<1);  //enable bb
  *(volatile U32*)(APB_CTRL_WIFI_BB_CFG_REG)      = *(volatile U32*) (APB_CTRL_WIFI_BB_CFG_REG) & 0xfffffffd | (0x0<<1);  //enable bb
  *(volatile U32*)(APB_CTRL_WIFI_BB_CFG_REG)      = *(volatile U32*) (APB_CTRL_WIFI_BB_CFG_REG) & 0xfffffffd | (0x1<<1);  //enable bb
  *(volatile U32*)(APB_CTRL_WIFI_BB_CFG_REG)      = *(volatile U32*) (APB_CTRL_WIFI_BB_CFG_REG) & 0xfffffffd | (0x0<<1);  //enable bb
  *(volatile U32*)(APB_CTRL_WIFI_BB_CFG_REG)      = *(volatile U32*) (APB_CTRL_WIFI_BB_CFG_REG) & 0xfffffffd | (0x1<<1);  //enable bb
  SET_PERI_REG_BITS(FE2_FE_RX_SYN3_2_REG, 1, 0, FE2_RX_SYNC_DBG_CLR_S);  //clr debug cnt

  *(volatile U32*)(AGCPWR_CTRL7_REG) = *(volatile U32*)(AGCPWR_CTRL7_REG) & 0x007fffff | (34<<24) | (1<<23);  //force_gain
  *(volatile U32*)(AGCPWR_CTRL7_REG) = *(volatile U32*)(AGCPWR_CTRL7_REG) & 0x007fffff | (34<<24) | (0<<23);  //force_gain

  delay_us(40);
#if 0
  //do noise floor calibration
  *(volatile U32*)(AGCFSM_CTRL4_REG) = (*(volatile U32*)(AGCFSM_CTRL4_REG)) & 0xffffefff | (0x1<<12);  //dis_agc_corr
  *(volatile U32*)(AGCPWR_CTRL1_REG) = (*(volatile U32*)(AGCPWR_CTRL1_REG)) & 0xff7ffff8 | (0x1<<23) | 0x0;  //en, count
  while(((*(volatile U32*)(AGCRD1_REG))>>24) & 0x1){};  //in noise cal
  *(volatile U32*)(AGCPWR_CTRL1_REG) = (*(volatile U32*)(AGCPWR_CTRL1_REG)) & 0xff7fffff | (0x0<<23);  //en
  *(volatile U32*)(AGCFSM_CTRL4_REG) = (*(volatile U32*)(AGCFSM_CTRL4_REG)) & 0xffffefff | (0x0<<12);  //dis_agc_corr
#endif
  SET_PERI_REG_BITS(AGCPWR_CTRL1_REG,0x1,1,AGC_NOISE_HW_FORCE_S);

}

void set_ck_cpu(int freq)
{
    // *(volatile U32*)(APB_CTRL_SYSCLK_CONF_REG) = (*(volatile U32*)(APB_CTRL_SYSCLK_CONF_REG)) & ~(APB_CTRL_SOC_CLK_SEL << APB_CTRL_SOC_CLK_SEL_S) | (0 << APB_CTRL_SOC_CLK_SEL_S);  //switch to xtal
    // *(volatile U32*)(SYSTEM_CPU_PER_CONF_REG) = (*(volatile U32*)(SYSTEM_CPU_PER_CONF_REG)) & ~SYSTEM_PLL_FREQ_SEL | ((freq==480) << SYSTEM_PLL_FREQ_SEL_S);  //pll_sel_480m
    // *(volatile U32*)(APB_CTRL_SYSCLK_CONF_REG) = (*(volatile U32*)(APB_CTRL_SYSCLK_CONF_REG)) & ~(APB_CTRL_SOC_CLK_SEL << APB_CTRL_SOC_CLK_SEL_S) | (1 << APB_CTRL_SOC_CLK_SEL_S);  //switch to pll
    SET_PERI_REG_BITS(APB_CTRL_SYSCLK_CONF_REG, APB_CTRL_SOC_CLK_SEL, 0, APB_CTRL_SOC_CLK_SEL_S);  //switch to xtal
    SET_PERI_REG_BITS(DPORT_CPU_PER_CONF_REG, 1, (freq==480), DPORT_PLL_FREQ_SEL_S);  //pll_sel_480m
    SET_PERI_REG_BITS(APB_CTRL_SYSCLK_CONF_REG, APB_CTRL_SOC_CLK_SEL, 1, APB_CTRL_SOC_CLK_SEL_S);  //switch to pll
}

void set_rx_sync_clk(int rx_sync_clk_half_sel)
{
    SET_PERI_REG_BITS(FE2_IQ_MIS_CTRL_REG, 1, (rx_sync_clk_half_sel & 0x1), FE2_CLK_1_RX_SYNC_SEL_S);
    SET_PERI_REG_BITS(FE2_IQ_MIS_CTRL_REG, 1, (rx_sync_clk_half_sel & 0x1), FE2_CLK_2_RX_SYNC_SEL_S);
}


