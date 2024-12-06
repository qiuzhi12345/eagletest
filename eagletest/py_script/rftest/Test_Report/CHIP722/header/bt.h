#include <xtensa/hal.h>
#include <xtensa/config/core.h>
#include <xtensa/config/system.h>
#include "./diag_utils.h"
#include "./bt_le_reg.h"
#include "./ip_common.h"
#include "../../../submodule/WIFIMAC/sim/example/include_new/mac_pwr_reg.h"
#include "../../../submodule/WIFIMAC/sim/example/include_new/mac_sch_reg.h"
#include "./fe_reg.h"
#include "./fe2_reg.h"
#include "../../../submodule/7.2_WIFIBB/sim/example/include_new/agc_reg.h"
#include "./bb_tx_reg.h"
#include "./bt_reg.h"
#include "./bt_reg_v2.h"
#include "./i2c_mst_reg.h"
#include "./bt_mac_reg.h"
#include "./dport_reg.h"
#include "./rtc_cntl_reg.h"
#include "./gpio_reg.h"
#include "./sim_bus_addr.h"

//
#define LE_TXBUF_START      ADDR_DRAM0_SRAM_5+0xb100 
#define BT_TXBUF_START      ADDR_DRAM0_SRAM_5+0xb100

 //===========================================================================================================================================


// 0x3ffd0000-0x3ffdffff system

//*******0x3ffc0000-0x3ffcffff for RX
int bt_mac_tx_fillpacket()
{
  //WRITE_PERI_REG(BT_TXBUF_START, 0x33220017); // FHS
    WRITE_PERI_REG(BT_TXBUF_START, 0x3322002F); // HV1
    WRITE_PERI_REG(BT_TXBUF_START+4, 0x77665544); 
    WRITE_PERI_REG(BT_TXBUF_START+8, 0xbbAA9988); 
    WRITE_PERI_REG(BT_TXBUF_START+12, 0xffeeddcc); 
    WRITE_PERI_REG(BT_TXBUF_START+16, 0x00221100); 
    WRITE_PERI_REG(BT_TXBUF_START+20, 0x01010101); 
    WRITE_PERI_REG(BT_TXBUF_START+24, 0x01010101); 
    WRITE_PERI_REG(BT_TXBUF_START+28, 0x01010101); 
}

int le_tx_sim()
{
  // int enable
  SET_PERI_REG_MASK(INT_ENA_WDEVLE, WDEV_LETXEND_INT_ENA);
  SET_PERI_REG_BITS(WDEVLETX0_CONF0, WDEV_LETX0_LINK_ADDR, LE_TXBUF_START, WDEV_LETX0_LINK_ADDR_S);
  SET_PERI_REG_MASK(WDEVLETX0_CONF0, WDEV_LETX0_ENA);
  while((READ_PERI_REG(INT_ST_WDEVLE)&WDEV_LETXEND_INT_ENA) != WDEV_LETXEND_INT_ENA){}
  SET_PERI_REG_MASK(INT_CLR_WDEVLE, WDEV_LETXEND_INT_ENA);
  if (((READ_PERI_REG(WDEVLE_TXPMD))&WDEV_LETXEND_STATE) != 0x0){
    diag_fail("TX FAIL");
  }
}

int le_rx_sim()
{
  //
  SET_PERI_REG_MASK(INT_ENA_WDEVLE, WDEV_LERXEND_INT_ENA);
  SET_PERI_REG_MASK(WDEVLERX0_CONF, WDEV_LERX0_ENA);
  while((READ_PERI_REG(INT_ST_WDEVLE)&WDEV_LERXEND_INT_ENA) != WDEV_LERXEND_INT_ENA){}
  SET_PERI_REG_MASK(INT_CLR_WDEVLE, WDEV_LERXEND_INT_ENA);
  if (((READ_PERI_REG(WDEVLE_RXPMD))&WDEV_LERXEND_STATE) != 0x0){
    diag_fail("RX FAIL");
  }  
}


//#define BT_SIM_DEBUG

void set_tx_on_guard_time(void){
    *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_2_REG) =(460)|(200<<10)|((800-390-80)<<20);      // tx on cycles ahead | tx on cycles behind | guard
}

void set_tx_on_guard_time_new(void){
    *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_2_REG) =(460+80)|(200<<10)|((800-390-80)<<20);      // tx on cycles ahead | tx on cycles behind | guard
    SET_PERI_REG_BITS(BT_BITS_BT_TX_RAMP_REG,BT_BITS_TX_RAMPUP_DELAY,160,BT_BITS_TX_RAMPUP_DELAY_S);
}

void fill_tx_buffer_1m_1010(void){
   // fill 1m symbols
   //U32 packet_1m[]={0xAB7CC2D9,0x99F9A58F,0x2A0001c0,0x03f1c7fc,0x1bAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xA99F1000};
   U32 packet_1m[]={0x9b433ed5,0xf1a59f99,0x03800054,0x3FE38FC0,0xAAAAAAD8,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0x000099F1};
   int i;
   for(i=0;i<12;i++)*(volatile U32*)(REG_BT_BUFFER_BASE+4*i)=packet_1m[i];   
   // set 1m symbol length
   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_REG) =(0)|(4<<7)|(1<<15); // sadder | eadder(cancelled) |(lsb first)

   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_3_REG) =11*32+16;      //1m bit length

   }


void start_tx_1m(unsigned int freq_point){
   //start GFSK modulator
   *(volatile U32*)(BT_BITS_GFSK_MODULATOR_CTRL_REG) =1|(14<<2); // enable | modu ratio
   //start fhopper
   //*(volatile U32*)(TX_FHOPPER_CTRL) =1|(freq_point<<1); // enable | freq point n*500k

   //start buffer to GFSK
   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_REG) =(*(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_REG)&(~(1<<14)))|(1<<14); //
}
void start_tx_1m_new(void){
   SET_PERI_REG_MASK(BT_BITS_INT_CLR_BT_REG,BT_BITS_BT_TX_END_INT_CLR);
      //start GFSK modulator
   //*(volatile U32*)(BT_BITS_GFSK_MODULATOR_CTRL_REG) =1|(6<<2); // enable | modu ratio
   SET_PERI_REG_BITS(BT_BITS_GFSK_MODULATOR_CTRL_REG,BT_BITS_MODU_INDX,14,BT_BITS_MODU_INDX_S);
   //SET_PERI_REG_MASK(BT_BITS_GFSK_MODULATOR_CTRL_REG,BT_BITS_EN_GFSK_MODULATOR);

   //start DPSK modulator
   //*(volatile U32*)(BT_BITS_DPSK_MODULATOR_CTRL_REG) =(1)|((8*2)<<1)|((8*6)<<11); // enable | begin delay | end delay

      //start buffer to GFSK
   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_REG) =(*(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_REG)&(~(1<<14)))|(1<<14); //
}
void fill_tx_buffer_2m_1010(void){
   // fill 1m symbols
   U32 packet_1m[]={0x9b433ed5,0xf1a59f99,0x03800054,0x3FE38FC0,0xAAAAD83F};
   int i;
   for(i=0;i<5;i++)*(volatile U32*)(REG_BT_BUFFER_BASE+4*i)=packet_1m[i];   
   // set 1m symbol length
   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_REG) =(0)|(4<<7)|(1<<15); // sadder | eadder(cancelled) |(lsb first)

   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_3_REG) =4*32;      //1m bit length

   

   // fill 2m symbols
   //U32 packet_2m[]={0x1ddf5436,0x7AAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAA01B};
   U32 packet_2m[]={0xAAAA01B0,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0x00009847};
   for(i=0;i<15;i++)*(volatile U32*)(REG_BT_BUFFER_BASE+4*(i+5))=packet_2m[i];    
   // set 2m symbol length
   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_1_REG) =(5)|((5+14)<<7)|(0<<14)|(1<<22); // sadder | eadder 2m | eadder 3m | lsb first
 

}

void fill_tx_buffer_2m_prbs9(void){
   // fill 1m symbols
   U32 packet_1m[]={0x0F7C5CC8,
0x5CC8253B,
0x253B479F,
0x479F362A,
0x362A471B,
0x471B5713,
0x57131100,
0x11008461};
   int i;
   for(i=0;i<8;i++)*(volatile U32*)(REG_BT_BUFFER_BASE+4*i)=packet_1m[i];   
   // set 1m symbol length
   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_REG) =(0)|(4<<7)|(0<<15); // sadder | eadder(cancelled) |(lsb first)

   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_3_REG) =8*32;      //1m bit length

   

   // fill 2m symbols
   //U32 packet_2m[]={0x1ddf5436,0x7AAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAA01B};
   U32 packet_2m[]={0x0F7C5CC8,
0x5CC8253B,
0x253B479F,
0x479F362A,
0x362A471B,
0x471B5713,
0x57131100,
0x11008461,0x0};
   for(i=0;i<9;i++)*(volatile U32*)(REG_BT_BUFFER_BASE+4*(i+8))=packet_2m[i];    
   // set 2m symbol length
   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_1_REG) =(8)|((8+7)<<7)|(0<<14)|(0<<22); // sadder | eadder 2m | eadder 3m | lsb first
 

}


void fill_tx_buffer_2m_prbs15(void){
   // fill 1m symbols
   U32 packet_1m[]={0x0002000C,
0x002800F0,
0x02200CC0,
0x2A80FF02,
0x020C0C28,
0x28F0F222,
0x2CCCEAAA,
0x7FFD000E};
   int i;
   for(i=0;i<8;i++)*(volatile U32*)(REG_BT_BUFFER_BASE+4*i)=packet_1m[i];   
   // set 1m symbol length
   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_REG) =(0)|(4<<7)|(0<<15)|(1<<23); // sadder | eadder(cancelled) |(lsb first) | (init out DC)

   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_3_REG) =8*32;      //1m bit length

   

   // fill 2m symbols
   //U32 packet_2m[]={0x1ddf5436,0x7AAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAA01B};
   U32 packet_2m[]={0x0002000C,
0x002800F0,
0x02200CC0,
0x2A80FF02,
0x020C0C28,
0x28F0F222,
0x2CCCEAAA,
0x7FFD000E,0x0};
   for(i=0;i<9;i++)*(volatile U32*)(REG_BT_BUFFER_BASE+4*(i+8))=packet_2m[i];    
   // set 2m symbol length
   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_1_REG) =(8)|((8+7)<<7)|(0<<14)|(0<<22); // sadder | eadder 2m | eadder 3m | lsb first
 

}


void fill_tx_buffer_3m_1010(void){
   // fill 1m symbols
   U32 packet_1m[]={0x9b433ed5,0xf1a59f99,0x1C000054,0x07FC0E00,0xAAAAD83F};
   int i;
   for(i=0;i<5;i++)*(volatile U32*)(REG_BT_BUFFER_BASE+4*i)=packet_1m[i];   
   // set 1m symbol length
   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_REG) =(0)|(4<<7)|(1<<15); // sadder | eadder(cancelled) |(lsb first)

   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_3_REG) =4*32;      //1m bit length

   

   // fill 3m symbols
   U32 packet_3m[]={0xAAAA0298,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0x003DEEAA};
   for(i=0;i<22;i++)*(volatile U32*)(REG_BT_BUFFER_BASE+4*(i+5))=packet_3m[i];    
   // set 3m symbol length
   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_1_REG) =(5)|((0)<<7)|((5+21)<<14)|(1<<22); // sadder | eadder 2m | eadder 3m | lsb first
 

}

void fill_tx_buffer_3m_prbs9(void){
   // fill 1m symbols
   U32 packet_1m[]={0x0F7C5CC8,
0x5CC8253B,
0x253B479F,
0x479F362A,
0x362A471B,
0x471B5713,
0x57131100,
0x11008461,0x0};
   int i;
   for(i=0;i<8;i++)*(volatile U32*)(REG_BT_BUFFER_BASE+4*i)=packet_1m[i];   
   // set 1m symbol length
   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_REG) =(0)|(4<<7)|(0<<15); // sadder | eadder(cancelled) |(lsb first)

   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_3_REG) =8*32;      //1m bit length

   

   // fill 3m symbols
   //U32 packet_3m[]={0xAAAA0298,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0x003DEEAA};
   U32 packet_3m[]={0x0F7C5CC8,
0x5CC8253B,
0x253B479F,
0x479F362A,
0x362A471B,
0x471B5713,
0x57131100,
0x11008461,0x0};
   for(i=0;i<9;i++)*(volatile U32*)(REG_BT_BUFFER_BASE+4*(i+8))=packet_3m[i];    
   // set 3m symbol length
   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_1_REG) =(8)|((0)<<7)|((8+7)<<14)|(1<<22); // sadder | eadder 2m | eadder 3m | lsb first
 

}

void fill_tx_buffer_3m_prbs15(void){
   // fill 1m symbols
   U32 packet_1m[]={0x0002000C,
0x002800F0,
0x02200CC0,
0x2A80FF02,
0x020C0C28,
0x28F0F222,
0x2CCCEAAA,
0x7FFD000E,};
   int i;
   for(i=0;i<8;i++)*(volatile U32*)(REG_BT_BUFFER_BASE+4*i)=packet_1m[i];   
   // set 1m symbol length
   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_REG) =(0)|(4<<7)|(0<<15); // sadder | eadder(cancelled) |(lsb first)

   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_3_REG) =8*32;      //1m bit length

   

   // fill 3m symbols
   //U32 packet_3m[]={0xAAAA0298,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0xAAAAAAAA,0x003DEEAA};
   U32 packet_3m[]={0x0002000C,
0x002800F0,
0x02200CC0,
0x2A80FF02,
0x020C0C28,
0x28F0F222,
0x2CCCEAAA,
0x7FFD000E,0x0};
     
   for(i=0;i<9;i++)*(volatile U32*)(REG_BT_BUFFER_BASE+4*(i+8))=packet_3m[i];    
   // set 3m symbol length
   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_1_REG) =(8)|((0)<<7)|((8+7)<<14)|(0<<22); // sadder | eadder 2m | eadder 3m | lsb first
 

}

void start_tx_2m_3m(unsigned int freq_point){
   //start GFSK modulator
   *(volatile U32*)(BT_BITS_GFSK_MODULATOR_CTRL_REG) =1|(6<<2); // enable | modu ratio

   //start DPSK modulator
   *(volatile U32*)(BT_BITS_DPSK_MODULATOR_CTRL_REG) =(1)|((80*2)<<1)|((80*6)<<11); // enable | begin delay | end delay
   //start fhopper
   //*(volatile U32*)(TX_FHOPPER_CTRL) =1|(freq_point<<1); // enable | freq point n*500k

   //start buffer to GFSK
   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_REG) =(*(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_REG)&(~(1<<14)))|(1<<14); //
   //start buffer to DPSK
   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_1_REG) =(*(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_1_REG)&(~(1<<21)))|(1<<21); //
}

void start_tx_2m_3m_new(void){
      //start GFSK modulator
   *(volatile U32*)(BT_BITS_GFSK_MODULATOR_CTRL_REG) =1|(6<<2); // enable | modu ratio

   //start DPSK modulator
   *(volatile U32*)(BT_BITS_DPSK_MODULATOR_CTRL_REG) =(1)|((8*2)<<1)|((8*6)<<11); // enable | begin delay | end delay

      //start buffer to GFSK
   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_REG) =(*(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_REG)&(~(1<<14)))|(1<<14); //
   //start buffer to DPSK
   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_1_REG) =(*(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_1_REG)&(~(1<<21)))|(1<<21); //
}

void wait4tx_end(unsigned int data_rate){
   while((*(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_REG)&(1<<31))==0);
   if(data_rate>1){
      while((*(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_1_REG)&(1<<31))==0);
   }
   //stop buffer to GFSK
   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_REG) =(*(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_REG)&(~(1<<14)))|(0<<14); //
   //stop buffer to DPSK
   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_1_REG) =(*(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_1_REG)&(~(1<<21)))|(0<<21); //
}

void wait4tx_end_new(void){
   while((READ_PERI_REG(BT_BITS_INT_RAW_BT_REG)&(BT_BITS_BT_TX_END_INT_RAW))==0){}
   SET_PERI_REG_MASK(BT_BITS_INT_CLR_BT_REG,BT_BITS_BT_TX_END_INT_CLR);
    //stop buffer to GFSK
   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_REG) =(*(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_REG)&(~(1<<14)))|(0<<14); //
   //stop buffer to DPSK
   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_1_REG) =(*(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_1_REG)&(~(1<<21)))|(0<<21); //
}

void test_bt_rx_sim(int dumpfile_index)
{
  //begin rx test
  *(volatile U32*)(0x60000300)      = *(volatile U32*) (0x60000300) & 0xffffffef | (0x1<<4);  //set GPIO4 : reset ptr for dumping rx data in bench
  *(volatile U32*)(0x60000300)      = *(volatile U32*) (0x60000300) & 0xffffffd1 | (0x6<<1);  //set GPIO3~1 : to control rx data source
  *(volatile U32*)(0x60000300)      = *(volatile U32*) (0x60000300) & 0xffffffd1 | ((dumpfile_index & 0x7)<<1) | ((dumpfile_index & 0x8)<<2);  //set GPIO3~1 and GPIO5: to control rx data source
  *(volatile U32*)(0x60000300)      = *(volatile U32*) (0x60000300) & 0xffffffef | (0x0<<4);  //set GPIO4 : release ptr for dumping rx data in bench

  //*(volatile U32*)(BT_BITS_BT_RX_CTRL_REG) =(*(volatile U32*)(BT_BITS_BT_RX_CTRL_REG)&(~(1<<31)))|(1<<31); //


   delay_us(400);


  *(volatile U32*)(0x60000300)      = *(volatile U32*) (0x60000300) & 0xffffffef | (0x1<<4);  //set GPIO4 : reset ptr for dumping rx data in bench
}

void open_bt_rx_filters(unsigned int freq_point){
   int i;
 // input gfilter coeff
   
   U32 GFSK_LP24[] = {0x029992D6,
0x006C8876,
0x07CBE800,
0x07FBF7F6};
   U32 DPSK_LP40[] = {0x021936A7,
0x00AC966A,
0x07B3F410,
0x07AFCDE5,
0x000BF7F3,
0x00201207,
0x00000606};
      
   //for(i=4;i<7;i++){*(volatile U32*)(RX_GFILTER_A_COEFF + (4*i)) = 0;}   
   //for(i=0;i<4;i++){*(volatile U32*)(RX_GFILTER_A_COEFF + (4*i)) = GFSK_LP24[i];} 
   //for(i=0;i<7;i++){*(volatile U32*)(RX_GFILTER_B_COEFF + (4*i)) = DPSK_LP40[i];} 

   //RX mixer   
   //SET_PERI_REG_BITS(BT_BITS_RX_FHOPPER_CTRL_REG,BT_BITS_RX_HOPPE_N500K,(0x40-freq_point),BT_BITS_RX_HOPPE_N500K_S);

   //open rx filters
   //*(volatile U32*)(BT_BITS_BT_RX_CTRL_REG) = *(volatile U32*)(BT_BITS_BT_RX_CTRL_REG)|(1<<31); // RX_EN 
   //SET_PERI_REG_MASK(BT_BITS_RX_GFILTER_CTRL_REG,BT_BITS_FILTER_ENABLE);
   
   //rx power valid delay
   

   //demodulator tuning
   //SET_PERI_REG_BITS(BT_BITS_BT_RX_CFG_1_REG, 0x1f, 0x1a, 21); //3m sync thresh
   //SET_PERI_REG_BITS(BT_BITS_BT_RX_CFG_1_REG, 0x1f, 0x13, 11); //2m sync thresh

   //limit agc max gain
   SET_PERI_REG_BITS(AGCGAIN_CTRL_5_REG, AGC_MAX_GAIN_BT, 0x52, AGC_MAX_GAIN_BT_S); 

   //times of fine gain
   //SET_PERI_REG_BITS(AGCBT_CTRL1_REG, AGC_GAIN_TUNE_MIN_BT, 3, AGC_GAIN_TUNE_MIN_BT_S); 

   //DPO
   //SET_PERI_REG_MASK(BT_V2_BITS_RX_DEMOD_0_REG, BT_V2_BITS_DPO_DSAMP_EN);

   //wdt
CLEAR_PERI_REG_MASK(WDEVBBCCAHUNG_REG, WDEV_BBCCAHUNG_ENA);
//lyun   CLEAR_PERI_REG_MASK(WDEVBBTXHUNG_REG, WDEV_BBTXHUNG_ENA);
//lyun   CLEAR_PERI_REG_MASK(WDEVBBRXHUNG_REG, WDEV_BBRXHUNG_ENA);

//  SET_PERI_REG_BITS(BT_V2_BITS_RX_FILTER_CFG_REG, BT_V2_BITS_DPO_SHIFT_INIT, 4, BT_V2_BITS_DPO_SHIFT_INIT_S);
//  SET_PERI_REG_BITS(BT_V2_BITS_RX_FILTER_CFG_REG, BT_V2_BITS_DPO_SHIFT_SAMP, 4, BT_V2_BITS_DPO_SHIFT_SAMP_S);
//  SET_PERI_REG_BITS(BT_V2_BITS_RX_DEMOD_0_REG, BT_V2_BITS_LEN_SAMP, 4, BT_V2_BITS_LEN_SAMP_S);
//  SET_PERI_REG_BITS(BT_V2_BITS_RX_DEMOD_5_REG, BT_V2_BITS_LEN_INIT, 4, BT_V2_BITS_LEN_INIT_S);
//  SET_PERI_REG_BITS(BT_V2_BITS_RX_FILTER_CFG_REG, BT_V2_BITS_LEN_SHIFT, 0, BT_V2_BITS_LEN_SHIFT_S);
  SET_PERI_REG_BITS(BT_V2_BITS_RX_ACCESS_CORR_CFG_REG, BT_V2_BITS_CORR_THRESH_LE_1M, 3, BT_V2_BITS_CORR_THRESH_LE_1M_S);
  SET_PERI_REG_BITS(BT_V2_BITS_RX_ACCESS_CORR_CFG_REG, BT_V2_BITS_CORR_THRESH_LE_2M, 3, BT_V2_BITS_CORR_THRESH_LE_2M_S);
  SET_PERI_REG_BITS(BT_V2_BITS_RX_ACCESS_CORR_CFG_REG, BT_V2_BITS_CORR_THRESH_LE_CODED, 5, BT_V2_BITS_CORR_THRESH_LE_CODED_S);
  SET_PERI_REG_BITS(AGCBT_CTRL2_REG, AGC_PWR_RESTART_THR_BT, 15, AGC_PWR_RESTART_THR_BT_S);
  SET_PERI_REG_BITS(AGCBT_CTRL2_REG, AGC_PWR_DROP_THR_BT, 64-15, AGC_PWR_DROP_THR_BT_S);

  SET_PERI_REG_MASK(AGCBT_CTRL2_REG, AGC_PWR_FINE_RECORRECT_EN_LE|AGC_PWR_FINE_RECORRECT_EN_BT|AGC_PWR_FINE_RECORRECT_INF_BT);
  SET_PERI_REG_BITS(AGCBT_CTRL2_REG, AGC_PWR_FINE_RECORRECT_THR_BT, 15, AGC_PWR_FINE_RECORRECT_THR_BT_S);
   
   SET_PERI_REG_BITS(AGCBT_CTRL0_REG, AGC_BT_RXPWR_VAR_THR, 3,AGC_BT_RXPWR_VAR_THR_S);
   SET_PERI_REG_BITS(AGCBT_CTRL0_REG, AGC_BT_RSSI_THR, 256-110,AGC_BT_RSSI_THR_S);

   CLEAR_PERI_REG_MASK(AGCPWR_CTRL8_REG, AGC_ADCSAT_RSTA_EN_BT);   

  SET_PERI_REG_BITS(AGCPWR_CTRL27_REG, AGC_PWR_RESTART_THR_LE_CODED, 30, AGC_PWR_RESTART_THR_LE_CODED_S);
  SET_PERI_REG_BITS(AGCPWR_CTRL27_REG, AGC_PWR_DROP_THR_LE_CODED, 64-30, AGC_PWR_DROP_THR_LE_CODED_S);
  SET_PERI_REG_BITS(AGCPWR_CTRL27_REG, AGC_PWR_FINE_RECORRECT_THR_LE_CODED, 20, AGC_PWR_FINE_RECORRECT_THR_LE_CODED_S);
  SET_PERI_REG_BITS(AGCPWR_CTRL27_REG, AGC_LE_CODED_RXPWR_VAR_THR, 15,AGC_LE_CODED_RXPWR_VAR_THR_S);
  SET_PERI_REG_BITS(AGCPWR_CTRL27_REG, AGC_LE_CODED_RSSI_THR, 256-110,AGC_LE_CODED_RSSI_THR_S);

// rx target power
SET_PERI_REG_BITS(AGCBT_CTRL3_REG, AGC_PWR_FINE_1ST_LE, 512-44, AGC_PWR_FINE_1ST_LE_S);
SET_PERI_REG_BITS(AGCBT_CTRL4_REG, AGC_PWR_FINE_1ST_LE_LT, 512-44, AGC_PWR_FINE_1ST_LE_LT_S);
SET_PERI_REG_BITS(AGCBT_CTRL6_REG, AGC_PWR_FINE_1ST_LE_CODED, 512-44, AGC_PWR_FINE_1ST_LE_CODED_S);
SET_PERI_REG_BITS(AGCBT_CTRL6_REG, AGC_PWR_FINE_1ST_LE_CODED_LT, 512-44, AGC_PWR_FINE_1ST_LE_CODED_LT_S);


//SET_PERI_REG_MASK(BT_V2_BITS_RX_DEMOD_1_REG, BT_V2_BITS_GFILTER_SEL_2M);
SET_PERI_REG_MASK(BT_V2_BITS_RX_DEMOD_1_REG, BT_V2_BITS_GFILTER_SEL_1M);
}

void bt_tx_if_init(unsigned int guard,unsigned int tx_on_ahead, unsigned int tx_on_behind, unsigned init_tx_DC){
      SET_PERI_REG_BITS(BT_BITS_BT_TX_IF_REG, BT_BITS_BT_TX_GUARD, guard, BT_BITS_BT_TX_GUARD_S);
      SET_PERI_REG_BITS(BT_BITS_BT_TX_IF_REG, BT_BITS_BT_TX_ON_AHEAD, tx_on_ahead, BT_BITS_BT_TX_ON_AHEAD_S);
      SET_PERI_REG_BITS(BT_BITS_BT_TX_IF_REG, BT_BITS_BT_TX_ON_BEHIND, tx_on_behind, BT_BITS_BT_TX_ON_BEHIND_S);
      SET_PERI_REG_MASK(BT_BITS_BT_TX_IF_REG, BT_BITS_BT_TX_INTERFACE_EN);
      if(init_tx_DC)SET_PERI_REG_MASK(BT_BITS_BT_TX_IF_REG,BT_BITS_BT_TX_INIT_DC);
}

void bt_tx_8m_enable(unsigned hoppe_n500k){
   //start GFSK modulator

   //start DPSK modulator
   *(volatile U32*)(BT_BITS_DPSK_MODULATOR_CTRL_REG) =(1)|((8*2)<<1)|((8*6)<<11); // enable | begin delay | end delay

   SET_PERI_REG_BITS(BT_BITS_BT_TX_RAMP_REG,BT_BITS_TX_RAMPUP_DELAY,160,BT_BITS_TX_RAMPUP_DELAY_S);

   SET_PERI_REG_BITS(BT_BITS_BT_TX_8M_REG,BT_BITS_HOPPE_N500K,hoppe_n500k,BT_BITS_HOPPE_N500K_S);
   SET_PERI_REG_MASK(BT_BITS_BT_TX_8M_REG,BT_BITS_BT_TX_8M_EN);
}
void bt_tx_8m_disable(void){
   CLEAR_PERI_REG_MASK(BT_BITS_BT_TX_8M_REG,BT_BITS_BT_TX_8M_EN);
}

void bt_tx_LE_en(u32 enable){
   if(enable==1){
      SET_PERI_REG_MASK(BT_BITS_GFSK_MODULATOR_CTRL_REG,BT_BITS_LE_EN);
      SET_PERI_REG_MASK(BT_BITS_BT_BUFFER2TX_CTRL_REG,BT_BITS_INIT_TX_DC);
   }
   else CLEAR_PERI_REG_MASK(BT_BITS_GFSK_MODULATOR_CTRL_REG,BT_BITS_LE_EN);
}

/// Bluetooth ///
/// LMP PDU number
#define LMP_test_activate 56
#define LMP_test_control 57
#define LMP_detach 7
#define LMP_accepted 3
#define LMP_not_accepted 4

/// LMP_test_control contents position in payload including payload header?
#define LMP_PIP_test_scenario 2
#define LMP_PIP_hopping_mode 3
#define LMP_PIP_TX_frequency 4
#define LMP_PIP_RX_frequency 5
#define LMP_PIP_power_control_mode 6
#define LMP_PIP_poll_period 7
#define LMP_PIP_packet_type 8
#define LMP_PIP_length_of_test_data 9

/// test scenarios
#define LMP_TS_pause_test_mode 0
#define LMP_TS_ttest_0 1
#define LMP_TS_ttest_1 2
#define LMP_TS_ttest_1010 3
#define LMP_TS_ttest_prbs 4
#define LMP_TS_lbtest_ACL 5
#define LMP_TS_lbtest_SCO 6
#define LMP_TS_lbtest_ACL_nw 7
#define LMP_TS_lbtest_SCO_nw 8
#define LMP_TS_ttest_11110000 9
#define LMP_TS_exit_test_mode 255

/// hopping mode
#define LMP_HM_single_freq 0
#define LMP_HM_normal_hop 1

/// power control mode
#define LMP_PCM_fixed 0
#define LMP_PCM_adaptive 1


// Packet Type Structure
typedef struct{
   unsigned int type_code;
   unsigned int link_type;
   unsigned int payload_header_length;
   unsigned int payload_length;
   unsigned int payload1_header_length;
}packet_struct;

packet_struct packet_NULL,packet_POLL,packet_FHS,packet_DM1,packet_DH1,packet_2DH1,packet_HV1,packet_HV2,packet_HV3,packet_DV,packet_EV3,packet_EV4,packet_EV5,packet_2EV3,packet_3EV3,packet_2EV5,
               packet_3EV5,packet_AUX1,packet_DM3,packet_DH3,packet_DM5,packet_DH5,packet_3DH1,packet_2DH3,packet_3DH3,packet_2DH5,packet_3DH5,packet_error_type;
void init_NALL_packet_struct(){
   packet_NULL.type_code=0;
   packet_NULL.link_type=1;
   packet_NULL.payload_header_length=0;
   packet_NULL.payload_length=0;
	packet_NULL.payload1_header_length=0;
}

void init_POLL_packet_struct(){
   packet_POLL.type_code=1;
   packet_POLL.link_type=1;
   packet_POLL.payload_header_length=0;
   packet_POLL.payload_length=0;
	packet_POLL.payload1_header_length=0;
};

void init_FHS_packet_struct(){
   packet_FHS.type_code=2;
   packet_FHS.link_type=1;
   packet_FHS.payload_header_length=0;
   packet_FHS.payload_length=18;
	packet_FHS.payload1_header_length=0;
};

void init_error_type_packet_struct(){
   packet_error_type.type_code=15;
   packet_error_type.link_type=1;
   packet_error_type.payload_header_length=1;
   packet_error_type.payload_length=17;
	packet_error_type.payload1_header_length=0;
}
void init_DM1_packet_struct(){
   packet_DM1.type_code=3;
   packet_DM1.link_type=1;
   packet_DM1.payload_header_length=1;
   packet_DM1.payload_length=17;
	packet_DM1.payload1_header_length=0;
};

void init_DH1_packet_struct(){
   packet_DH1.type_code=4;
   packet_DH1.link_type=4;
   packet_DH1.payload_header_length=1;
   packet_DH1.payload_length=27;
	packet_DH1.payload1_header_length=0;
};

void init_2DH1_packet_struct(){
   packet_2DH1.type_code=4;
   packet_2DH1.link_type=5;
   packet_2DH1.payload_header_length=2;
   packet_2DH1.payload_length=54;
	packet_2DH1.payload1_header_length=0;
};

void init_HV1_packet_struct(){
   packet_HV1.type_code=5;
   packet_HV1.link_type=1;
   packet_HV1.payload_header_length=0;
   packet_HV1.payload_length=10;
	packet_HV1.payload1_header_length=0;
};

void init_HV2_packet_struct(){
   packet_HV2.type_code=6;
   packet_HV2.link_type=1;
   packet_HV2.payload_header_length=0;
   packet_HV2.payload_length=20;
	packet_HV2.payload1_header_length=0;
};

void init_HV3_packet_struct(){
   packet_HV3.type_code=7;
   packet_HV3.link_type=1;
   packet_HV3.payload_header_length=0;
   packet_HV3.payload_length=30;
	packet_HV3.payload1_header_length=0;
};


void init_DV_packet_struct(){
   packet_DV.type_code=8;
   packet_DV.link_type=1;
   packet_DV.payload_header_length=0;
   packet_DV.payload_length=19;
	packet_DV.payload1_header_length=1;
};

void init_EV3_packet_struct(){
   packet_EV3.type_code=7;
   packet_EV3.link_type=2;
   packet_EV3.payload_header_length=0;
   packet_EV3.payload_length=30;
	packet_EV3.payload1_header_length=0;
};

void init_EV4_packet_struct(){
   packet_EV4.type_code=12;
   packet_EV4.link_type=2;
   packet_EV4.payload_header_length=0;
   packet_EV4.payload_length=120;
   packet_EV4.payload_length=30;
	packet_EV4.payload1_header_length=0;
};

void init_EV5_packet_struct(){
   packet_EV5.type_code=13;
   packet_EV5.link_type=2;
   packet_EV5.payload_header_length=0;
   packet_EV5.payload_length=180;
   packet_EV5.payload_length=30;
	packet_EV5.payload1_header_length=0;
};

void init_2EV3_packet_struct(){
   packet_2EV3.type_code=6;
   packet_2EV3.link_type=3;
   packet_2EV3.payload_header_length=0;
   //packet_2EV3.payload_length=60;
   packet_2EV3.payload_length=30;
	packet_2EV3.payload1_header_length=0;
};

void init_3EV3_packet_struct(){
   packet_3EV3.type_code=7;
   packet_3EV3.link_type=3;
   packet_3EV3.payload_header_length=0;
   //packet_3EV3.payload_length=90;
   packet_3EV3.payload_length=30;
	packet_3EV3.payload1_header_length=0;
};

void init_2EV5_packet_struct(){
   packet_2EV5.type_code=12;
   packet_2EV5.link_type=3;
   packet_2EV5.payload_header_length=0;
   //packet_2EV5.payload_length=360;
   packet_2EV5.payload_length=30;
	packet_2EV5.payload1_header_length=0;
};

void init_3EV5_packet_struct(){
   packet_3EV5.type_code=13;
   packet_3EV5.link_type=3;
   packet_3EV5.payload_header_length=0;
   //packet_3EV5.payload_length=540;
   packet_3EV5.payload_length=30;
	packet_3EV5.payload1_header_length=0;
};

void init_AUX1_packet_struct(){
   packet_AUX1.type_code=9;
   packet_AUX1.link_type=4;
   packet_AUX1.payload_header_length=1;
   packet_AUX1.payload_length=29;
	packet_AUX1.payload1_header_length=0;
};

void init_DM3_packet_struct(){
   packet_DM3.type_code=10;
   packet_DM3.link_type=4;
   packet_DM3.payload_header_length=2;
   packet_DM3.payload_length=121;
	packet_DM3.payload1_header_length=0;
};

void init_DH3_packet_struct(){
   packet_DH3.type_code=11;
   packet_DH3.link_type=4;
   packet_DH3.payload_header_length=2;
   packet_DH3.payload_length=183;
	packet_DH3.payload1_header_length=0;
};

void init_DM5_packet_struct(){
   packet_DM5.type_code=14;
   packet_DM5.link_type=4;
   packet_DM5.payload_header_length=2;
   packet_DM5.payload_length=224;
	packet_DM5.payload1_header_length=0;
};

void init_DH5_packet_struct(){
   packet_DH5.type_code=15;
   packet_DH5.link_type=4;
   packet_DH5.payload_header_length=2;
   packet_DH5.payload_length=339;
	packet_DH5.payload1_header_length=0;
};

void init_3DH1_packet_struct(){
   packet_3DH1.type_code=8;
   packet_3DH1.link_type=5;
   packet_3DH1.payload_header_length=2;
   packet_3DH1.payload_length=83;
	packet_3DH1.payload1_header_length=0;
};

void init_2DH3_packet_struct(){
   packet_2DH3.type_code=10;
   packet_2DH3.link_type=5;
   packet_2DH3.payload_header_length=2;
   packet_2DH3.payload_length=367;
	packet_2DH3.payload1_header_length=0;
};

void init_3DH3_packet_struct(){
   packet_3DH3.type_code=11;
   packet_3DH3.link_type=5;
   packet_3DH3.payload_header_length=2;
   packet_3DH3.payload_length=552;
	packet_3DH3.payload1_header_length=0;
};

void init_2DH5_packet_struct(){
   packet_2DH5.type_code=14;
   packet_2DH5.link_type=5;
   packet_2DH5.payload_header_length=2;
   packet_2DH5.payload_length=679;
	packet_2DH5.payload1_header_length=0;
};

void init_3DH5_packet_struct(){
   packet_3DH5.type_code=15;
   packet_3DH5.link_type=5;
   packet_3DH5.payload_header_length=2;
   packet_3DH5.payload_length=1021;
	packet_3DH5.payload1_header_length=0;
};

void init_packet_struct(){
   init_NALL_packet_struct();
   init_POLL_packet_struct();
   init_FHS_packet_struct();
   init_DM1_packet_struct();
   init_DH1_packet_struct();
   init_2DH1_packet_struct();
   init_HV1_packet_struct();
   init_HV2_packet_struct();
   init_HV3_packet_struct();
   init_DV_packet_struct();
   init_EV3_packet_struct();
   init_EV4_packet_struct();
   init_EV5_packet_struct();
   init_2EV3_packet_struct();
   init_3EV3_packet_struct();
   init_2EV5_packet_struct();
   init_3EV5_packet_struct();
   init_AUX1_packet_struct();
   init_DM3_packet_struct();
   init_DH3_packet_struct();
   init_DM5_packet_struct();
   init_DH5_packet_struct();
   init_3DH1_packet_struct();
   init_2DH3_packet_struct();
   init_3DH3_packet_struct();
   init_2DH5_packet_struct();
   init_3DH5_packet_struct();
   init_error_type_packet_struct();
}


u32 WDEVBTTX_CONF0(u32 device_sel){
   switch(device_sel){
      case 0: return WDEVBTTX0_CONF0;
      case 1: return WDEVBTTX0_CONF0;
      default: return WDEVBTTX0_CONF0;
      
   }
}

u32 WDEVBTTX_CONF1(u32 device_sel){
   switch(device_sel){
      case 0: return WDEVBTTX0_CONF1;
      case 1: return WDEVBTTX0_CONF1;
      default: return WDEVBTTX0_CONF1;
      
   }
}

u32 WDEVBTTX_HEAD(u32 device_sel){
   switch(device_sel){
      case 0: return WDEVBTTX0_HEAD;
      case 1: return WDEVBTTX0_HEAD;
      default: return WDEVBTTX0_HEAD;
      
   }
}

u32 WDEVBTRX_CONF(u32 device_sel){
   switch(device_sel){
      case 0: return WDEVBTRX0_CONF;
      case 1: return WDEVBTRX0_CONF;
      default: return WDEVBTRX0_CONF;
      
   }
}

void bt_mac_iqview_debug(u32 GIAC_en){
  WRITE_PERI_REG(WDEVBT_CLK_DEBUG, 0xFFFFFFFC);
  SET_PERI_REG_MASK(WDEVBT_DEBUG_MODE, WDEV_BTCLK_DEBUG_ENA);
  CLEAR_PERI_REG_MASK(WDEVBT_CODE_OPTION, WDEV_BTTX_AUTO_FRAMING);
   if(GIAC_en=1){
      SET_PERI_REG_BITS(WDEVBT_ULAP_DEBUG,WDEV_BT_LAP_DEBUG,0x9e8b33,WDEV_BT_LAP_DEBUG_S);
      SET_PERI_REG_BITS(WDEVBT_ULAP_DEBUG,WDEV_BT_UAP_DEBUG,0x00,WDEV_BT_UAP_DEBUG_S);  
   }
   else{
      SET_PERI_REG_BITS(WDEVBT_ULAP_DEBUG,WDEV_BT_LAP_DEBUG,0xC6967E,WDEV_BT_LAP_DEBUG_S);
      SET_PERI_REG_BITS(WDEVBT_ULAP_DEBUG,WDEV_BT_UAP_DEBUG,0x6B,WDEV_BT_UAP_DEBUG_S);
   }
   SET_PERI_REG_MASK(WDEVBT_DEBUG_MODE,WDEV_BTULAP_DEBUG_ENA);
   SET_PERI_REG_MASK(WDEVBT_CODE_OPTION,WDEV_BTRX_FORCE_NOWHITE);
   SET_PERI_REG_MASK(WDEVBT_CODE_OPTION,WDEV_BTTX_FORCE_NOWHITE);
}


int bt_tx_sim_debug()
{
  // int enable
  SET_PERI_REG_MASK(INT_ENA_WDEVBT, WDEV_BTTXEND_INT_ENA);
  
  //WRITE_PERI_REG(WDEVBTTX0_CONF1, 20); // FHS
  //WRITE_PERI_REG(WDEVBTTX0_CONF1, 12); // HV1
  //SET_PERI_REG_BITS(WDEVBTTX0_CONF0, WDEV_BTTX0_TYPE, 0x1, WDEV_BTTX0_TYPE_S);
  SET_PERI_REG_BITS(WDEVBTTX0_CONF0, WDEV_BTTX0_LINK_ADDR, BT_TXBUF_START, WDEV_BTTX0_LINK_ADDR_S);
  SET_PERI_REG_MASK(WDEVBT_DEBUG_MODE, WDEV_BTTX_VALID_DEBUG);
  //CLEAR_PERI_REG_MASK(WDEVBT_DEBUG_MODE, WDEV_BTTX_VALID_DEBUG);
  while((READ_PERI_REG(INT_ST_WDEVBT)&WDEV_BTTXEND_INT_ENA) != WDEV_BTTXEND_INT_ENA){}
  SET_PERI_REG_MASK(INT_CLR_WDEVBT, WDEV_BTTXEND_INT_ENA);
  if (((READ_PERI_REG(WDEVBT_TXPMD))&WDEV_BTTXEND_STATE) != 0x0){
    diag_fail("TX FAIL");
  }
}

int bt_rx_sim_debug()
{

   // clear rx buffer
   u32 i;
   for(i=0;i<258;i++)WRITE_PERI_REG((READ_PERI_REG(WDEVBT_RXBASE))+(i*4),0);
  //
  SET_PERI_REG_MASK(INT_ENA_WDEVBT, WDEV_BTRXEND_INT_ENA);

  //SET_PERI_REG_BITS(WDEVBTRX0_CONF, WDEV_BTRX0_TYPE, 0x1, WDEV_BTTX0_TYPE_S);
   SET_PERI_REG_MASK(WDEVBT_DEBUG_MODE, WDEV_BTRX_VALID_DEBUG);

   delay_us(20);
   test_bt_rx_sim(7+(1<<16));  //void test_rx_sim(int dumpfile_index)


  //CLEAR_PERI_REG_MASK(WDEVBT_DEBUG_MODE, WDEV_BTRX_VALID_DEBUG);
  while((READ_PERI_REG(INT_ST_WDEVBT)&WDEV_BTRXEND_INT_ENA) != WDEV_BTRXEND_INT_ENA){}
  SET_PERI_REG_MASK(INT_CLR_WDEVBT, WDEV_BTRXEND_INT_ENA);
  if (((READ_PERI_REG(WDEVBT_RXPMD))&WDEV_BTRXEND_STATE) != 0x0){
    diag_fail("RX FAIL");
  }
  
}

int bt_tx_sim_con(packet_struct packet, u32 device_sel)
{
      SET_PERI_REG_MASK(INT_CLR_WDEVBT, WDEV_BTTXEND_INT_ENA);  
      bt_test_mode_fill_tx_payload(packet.payload_header_length+2, packet.payload_length, LMP_TS_ttest_prbs, 0,device_sel);
      bt_mac_set_tx_bytelength(BT_TXBUF_START,packet.payload_header_length,packet.payload1_header_length,packet.payload_length,device_sel);
      bt_mac_set_tx_type_code(BT_TXBUF_START, packet.type_code,device_sel);
      bt_mac_set_tx_link_type(packet.link_type,device_sel);
      bt_mac_set_rx_link_type(packet.link_type,device_sel);

  // int enable
  SET_PERI_REG_MASK(INT_ENA_WDEVBT, WDEV_BTTXEND_INT_ENA);


  SET_PERI_REG_BITS(WDEVBTTX_CONF0(device_sel), WDEV_BTTX0_LINK_ADDR, BT_TXBUF_START, WDEV_BTTX0_LINK_ADDR_S);

  SET_PERI_REG_MASK(WDEVBTTX_CONF0(device_sel), WDEV_BTTX0SLOT_VALID); //  set as early as possible to use the nearest next TX slot
  SET_PERI_REG_MASK(WDEVBTTX_CONF0(device_sel), WDEV_BTTX0SLOT_ENA); //  set as early as possible to use the nearest next TX slot
  while((READ_PERI_REG(INT_ST_WDEVBT)&WDEV_BTTXEND_INT_ENA) != WDEV_BTTXEND_INT_ENA){}
  SET_PERI_REG_MASK(INT_CLR_WDEVBT, WDEV_BTTXEND_INT_ENA);
  if (((READ_PERI_REG(WDEVBT_TXPMD))&WDEV_BTTXEND_STATE) != 0x0){
    diag_fail("TX FAIL");
  }
}

int bt_tx_sim_con_2(packet_struct packet, u32 device_sel)
{
      SET_PERI_REG_MASK(INT_CLR_WDEVBT, WDEV_BTTXEND_INT_ENA);  
      bt_test_mode_fill_tx_payload(packet.payload_header_length+2, packet.payload_length, LMP_TS_ttest_prbs, 0,device_sel);
      bt_mac_set_tx_bytelength(BT_TXBUF_START,packet.payload_header_length,packet.payload1_header_length,packet.payload_length,device_sel);
      bt_mac_set_tx_type_code(BT_TXBUF_START, packet.type_code,device_sel);
      bt_mac_set_tx_link_type(packet.link_type,device_sel);
      bt_mac_set_rx_link_type(packet.link_type,device_sel);

  // int enable
  SET_PERI_REG_MASK(INT_ENA_WDEVBT, WDEV_BTTXEND_INT_ENA);


  SET_PERI_REG_BITS(WDEVBTTX_CONF0(device_sel), WDEV_BTTX0_LINK_ADDR, BT_TXBUF_START, WDEV_BTTX0_LINK_ADDR_S);

  SET_PERI_REG_MASK(WDEVBTTX_CONF0(device_sel), WDEV_BTTX0SLOT_VALID); //  set as early as possible to use the nearest next TX slot
  SET_PERI_REG_MASK(WDEVBTTX_CONF0(device_sel), WDEV_BTTX0SLOT_ENA); //  set as early as possible to use the nearest next TX slot
  while((READ_PERI_REG(INT_ST_WDEVBT)&WDEV_BTTXEND_INT_ENA) != WDEV_BTTXEND_INT_ENA){}
  SET_PERI_REG_MASK(INT_CLR_WDEVBT, WDEV_BTTXEND_INT_ENA);
  return ((READ_PERI_REG(WDEVBT_TXPMD))&WDEV_BTTXEND_STATE);
}


void bt_tx_bitstream(u32 len){
   u32 i,shift;
   for(i=0; i<1000; i++){
      shift = i%32;
      WRITE_PERI_REG(BT_TXBUF_START+(4*i), (0xffffffff<<shift));
   }
   SET_PERI_REG_BITS(WDEVBTTX0_CONF0, WDEV_BTTX0_LINK_ADDR, BT_TXBUF_START, WDEV_BTTX0_LINK_ADDR_S);
   SET_PERI_REG_BITS(WDEVBTTX_HEAD(0),0x3ff,len,3+WDEV_BTTX0_PAYLOAD_HEAD_S);
   SET_PERI_REG_BITS(WDEVBTTX0_CONF1, WDEV_BTTX0_LEN, len, WDEV_BTTX0_LEN_S);
   SET_PERI_REG_MASK(WDEVBT_DEBUG_MODE, WDEV_BTTX_BITSTREAM|WDEV_BTTX_VALID_DEBUG);
   

  while((READ_PERI_REG(INT_RAW_WDEVBT)&WDEV_BTTXEND_INT_ENA) != WDEV_BTTXEND_INT_ENA){}
  SET_PERI_REG_MASK(INT_CLR_WDEVBT, WDEV_BTTXEND_INT_ENA);
  printinfo("tx bitstream end!\n",len); 
}

int bt_rx_sim_con(u32 link_type,u32 device_sel)
{
      bt_mac_set_rx_link_type(link_type,device_sel);
      SET_PERI_REG_MASK(INT_CLR_WDEVBT, WDEV_BTRXEND_INT_ENA);
      SET_PERI_REG_MASK(WDEVBTRX_CONF(device_sel), WDEV_BTRX0SLOT_ENA);
   // clear rx buffer
   u32 i;
   for(i=0;i<258;i++)WRITE_PERI_REG((READ_PERI_REG(WDEVBT_RXBASE))+(i*4),0);
  //
  SET_PERI_REG_MASK(INT_ENA_WDEVBT, WDEV_BTRXEND_INT_ENA);

  while((READ_PERI_REG(INT_ST_WDEVBT)&WDEV_BTRXEND_INT_ENA) != WDEV_BTRXEND_INT_ENA){}
  SET_PERI_REG_MASK(INT_CLR_WDEVBT, WDEV_BTRXEND_INT_ENA);
  return ((READ_PERI_REG(WDEVBT_RXPMD))&WDEV_BTRXEND_STATE);

  
}


int bt_rx_sim_con_2(u32 device_sel)
{
      //bt_mac_set_rx_link_type(link_type,device_sel);
      SET_PERI_REG_MASK(INT_CLR_WDEVBT, WDEV_BTRXEND_INT_ENA);
      SET_PERI_REG_MASK(WDEVBTRX_CONF(device_sel), WDEV_BTRX0SLOT_ENA);
   // clear rx buffer
   u32 i;
   for(i=0;i<258;i++)WRITE_PERI_REG((READ_PERI_REG(WDEVBT_RXBASE))+(i*4),0);
  //
  SET_PERI_REG_MASK(INT_ENA_WDEVBT, WDEV_BTRXEND_INT_ENA);

  while((READ_PERI_REG(INT_ST_WDEVBT)&WDEV_BTRXEND_INT_ENA) != WDEV_BTRXEND_INT_ENA){}
  SET_PERI_REG_MASK(INT_CLR_WDEVBT, WDEV_BTRXEND_INT_ENA);
  if (((READ_PERI_REG(WDEVBT_RXPMD))&WDEV_BTRXEND_STATE) != 0x0){
    return 1;
  }else {
    return 0;
   }
  
}

void bt_mac_set_tx_bytelength(unsigned int tx_buf_addr,int pheader_length,int pheader1_length,int payloadlength, u32 device_sel){
   
   if(pheader_length==0){
      WRITE_PERI_REG(WDEVBTTX_CONF1(device_sel), payloadlength);
      SET_PERI_REG_BITS(WDEVBTSCO_CONF,WDEV_BTTXESCO_LEN, payloadlength,WDEV_BTTXESCO_LEN_S);
      SET_PERI_REG_BITS(WDEVBTSCO_CONF,WDEV_BTRXESCO_LEN, payloadlength,WDEV_BTRXESCO_LEN_S);
   }else if(pheader_length==1){
      WRITE_PERI_REG(WDEVBTTX_CONF1(device_sel), payloadlength);
      SET_PERI_REG_BITS(WDEVBTTX_HEAD(device_sel),0x1f,payloadlength,3+WDEV_BTTX0_PAYLOAD_HEAD_S);
   }else if(pheader_length==2){
      WRITE_PERI_REG(WDEVBTTX_CONF1(device_sel), payloadlength);
      SET_PERI_REG_BITS(WDEVBTTX_HEAD(device_sel),0x3ff,payloadlength,3+WDEV_BTTX0_PAYLOAD_HEAD_S);
   }
   if(pheader1_length!=0)SET_PERI_REG_BITS(WDEVBTTX_HEAD(device_sel),0x1f,payloadlength-10,3+WDEV_BTTX0_PAYLOAD_HEAD_S);
   
}

void bt_mac_set_tx_lt_addr(unsigned int tx_buf_addr, unsigned int lt_addr, u32 device_sel){
   SET_PERI_REG_BITS(WDEVBTTX_HEAD(device_sel),0x7,lt_addr,WDEV_BTTX0_PACKET_HEAD_S);

}

void bt_mac_set_tx_type_code(unsigned int tx_buf_addr, unsigned int type_code, u32 device_sel){
   SET_PERI_REG_BITS(WDEVBTTX_HEAD(device_sel),0xf,type_code,3+WDEV_BTTX0_PACKET_HEAD_S);

}

void bt_mac_set_tx_link_type(unsigned int link_type, u32 device_sel){
   SET_PERI_REG_BITS(WDEVBTTX_CONF0(device_sel), WDEV_BTTX0_TYPE, link_type, WDEV_BTTX0_TYPE_S);
}

void bt_mac_set_rx_link_type(unsigned int link_type, u32 device_sel){
   SET_PERI_REG_BITS(WDEVBTRX_CONF(device_sel), WDEV_BTRX0_TYPE, link_type, WDEV_BTRX0_TYPE_S);
}


int bt_mac_loopback_df(u32 device_sel){
   u32 tx_length= READ_PERI_REG(WDEVBTTX_CONF1(device_sel));
   u32 rx_length= READ_PERI_REG(READ_PERI_REG(WDEVBT_RXBASE))&0x7ff;
#ifdef BT_SIM_DEBUG
   bt_sim_debug(1, tx_length, rx_length,0,0);
#endif
   if(tx_length!=rx_length){
      printinfo("txlen\n",tx_length);
      printinfo("rxlen\n",rx_length);
      printinfo("length mismatch\n",0);
      fail("DIAG FAIL!\n");
   }
   int i;
   u32 tx_data,rx_data,mem_offset,shift;
   for(i=0;i<tx_length;i=i+1){
      mem_offset=i/4;
      shift=i%4;
      tx_data=READ_PERI_REG(BT_TXBUF_START+(mem_offset*4))&((0xff)<<(8*shift));
      rx_data=READ_PERI_REG(READ_PERI_REG(WDEVBT_RXBASE)+((mem_offset+4)*4))&((0xff)<<(8*shift));
#ifdef BT_SIM_DEBUG
      bt_sim_debug(2, mem_offset, shift,tx_data>>(shift*8),rx_data>>(shift*8));

#else
     printinfo("tx data\n",tx_data);
     printinfo("rx data\n",rx_data); 
     if(tx_data!=rx_data)fail("DIAG FAIL!\n");
#endif
   }
}

int bt_mac_loopback_master(packet_struct packet, u32 loopback){
      bt_test_mode_fill_tx_payload(packet.payload_header_length+2, packet.payload_length, LMP_TS_ttest_11110000, 0,0);
      bt_mac_set_tx_bytelength(BT_TXBUF_START,packet.payload_header_length,packet.payload1_header_length,packet.payload_length,0);
      bt_mac_set_tx_type_code(BT_TXBUF_START, packet.type_code,0);
      bt_mac_set_tx_link_type(packet.link_type,0);
      bt_mac_set_rx_link_type(packet.link_type,0);
      bt_tx_sim_debug();
      delay_us(10);
      if(loopback==1){
         bt_rx_sim_debug();
         delay_us(10);
         bt_mac_loopback_df(0);
      }
}

int bt_mac_loopback_slave(packet_struct packet){
      bt_mac_set_tx_link_type(packet.link_type,0);
      bt_mac_set_rx_link_type(packet.link_type,0);
      u32 rx_length= READ_PERI_REG(READ_PERI_REG(WDEVBT_RXBASE))&0x7ff;   
      WRITE_PERI_REG(WDEVBTTX0_CONF1, rx_length);
      SET_PERI_REG_BITS(WDEVBTSCO_CONF,WDEV_BTRXESCO_LEN, 30, WDEV_BTRXESCO_LEN_S); 
      
      bt_test_mode_fill_tx_payload(packet.payload_header_length+2, packet.payload_length, LMP_TS_ttest_1010, 1,0);
      /*
      rx_length=(rx_length/4)+1;
      u32 i;      
      for(i=0;i<rx_length;i++){
         WRITE_PERI_REG(BT_TXBUF_START+(i*4),READ_PERI_REG(READ_PERI_REG(WDEVBT_RXBASE)+((i+2)*4)));
      }
      */
      bt_tx_sim_debug();
      delay_us(10);
      bt_rx_sim_debug();
      delay_us(10);
      bt_mac_loopback_df(0);
}

int bt_con_loopback_master(packet_struct packet, u32 loopback, u32 slave_sel){
      u32 state=0, retry=0;
      bt_tx_sim_con_2(packet,slave_sel);
      if(loopback==1){
         state=bt_rx_sim_con(packet.link_type,slave_sel);
         while(state!=0){
            if(state==0x47)return;
            if(retry>=2)fail("DIAG FAIL!\n");
            state=bt_rx_sim_con(packet.link_type,slave_sel);
            retry++;
         }
         bt_mac_loopback_df(slave_sel);
      }
}

/*
void bt_sim_debug(u32 a, u32 b, u32 c, u32 d, u32 e){
   SET_PERI_REG_BITS(RX_GFILTER_A_COEFF_5,BT_BITS_RX_GFILTER_A_COEFF_15,a,BT_BITS_RX_GFILTER_A_COEFF_15_S);
   SET_PERI_REG_BITS(RX_GFILTER_A_COEFF_5,BT_BITS_RX_GFILTER_A_COEFF_16,b,BT_BITS_RX_GFILTER_A_COEFF_16_S);
   SET_PERI_REG_BITS(RX_GFILTER_A_COEFF_5,BT_BITS_RX_GFILTER_A_COEFF_17,c,BT_BITS_RX_GFILTER_A_COEFF_17_S);
   SET_PERI_REG_BITS(RX_GFILTER_A_COEFF_6,BT_BITS_RX_GFILTER_A_COEFF_18,d,BT_BITS_RX_GFILTER_A_COEFF_18_S);
   SET_PERI_REG_BITS(RX_GFILTER_A_COEFF_6,BT_BITS_RX_GFILTER_A_COEFF_19,e,BT_BITS_RX_GFILTER_A_COEFF_19_S);
}
*/
//// LMP test mode ////
u8 PRBS9[1024];

u32 bt_test_mode_get_rx_payload_byte(u32 byte_position){ //start from 1
   byte_position = byte_position-1;
   u32 word_offset=byte_position/4;
   u32 byte_offset=byte_position%4;
   u32 byte=((READ_PERI_REG((READ_PERI_REG(WDEVBT_RXBASE))+((word_offset)*4)))>>(byte_offset*8))&0xff;
   return byte;
}


u32 bt_test_mode_get_tx_payload_byte(u32 data_type, u32 loopback, u32 byte_offset, u32 word_offset, u32 byte_cnt, u32 rx_addr_base){
   u32 content,indx_PRBS9;
   if(loopback==1){
      content=((READ_PERI_REG(rx_addr_base+((4+word_offset)*4)))>>(byte_offset*8))&0xff;
      
   }
   else {
      switch(data_type){
         case LMP_TS_ttest_0:
         content=0;
         break;
         case LMP_TS_ttest_1:
         content=0xff;
         break;
         case LMP_TS_ttest_1010:
         content=0xaa;
         break;
         case LMP_TS_ttest_prbs:
         //content=PRBS9[byte_cnt];
         content=((byte_offset+word_offset)*5)^0xaa;
         break;         
         case LMP_TS_ttest_11110000:
         content=0xf0;
         break;
      }
   }
      return content;
}


void bt_test_mode_fill_tx_payload(u32 lheader, u32 lpayload, u32 data_type, u32 loopback,u32 device_sel){ // not support DV packet, lheader = length of header + length of payload header
   u32 byte_offset=0,word_offset=0,i,content;
   u32 tx_addr_base=BT_TXBUF_START, rx_addr_base=READ_PERI_REG(WDEVBT_RXBASE);
   for(i=0;i<lpayload;i++){
      if(byte_offset==4){
         byte_offset=0;
         word_offset=word_offset+1;
      }
      content = bt_test_mode_get_tx_payload_byte(data_type, loopback, byte_offset, word_offset, i, rx_addr_base);
      SET_PERI_REG_BITS(tx_addr_base+(word_offset*4),0xff,content,(byte_offset*8));
      byte_offset++;
   }
   if(loopback==1){
        u32 lheader=(READ_PERI_REG(rx_addr_base+(2*4))&0xffff);
         u32 header=(READ_PERI_REG(rx_addr_base+(2*4))&0xffc00000)>>22;
         SET_PERI_REG_BITS(WDEVBTTX_HEAD(device_sel),WDEV_BTTX0_PACKET_HEAD,header,WDEV_BTTX0_PACKET_HEAD_S);
         SET_PERI_REG_BITS(WDEVBTTX_HEAD(device_sel),WDEV_BTTX0_PAYLOAD_HEAD,lheader,WDEV_BTTX0_PAYLOAD_HEAD_S);

   }
}

/// LE
#define ACCESS_ADDR_ADV 0x8e89bed6

void le_fill_tx_buffer_1010(void){
   u32 i;
   SET_PERI_REG_MASK(BT_BITS_BT_BUFFER_CTRL_REG,BT_BITS_BUFFER_CTRL_APB_MODE);
   for(i=0;i<256;i++)WRITE_PERI_REG(REG_BT_BUFFER_BASE+(4*i),0); //clear buffer

   // fill 1m symbols
   le_fill_tx_access_addr(ACCESS_ADDR_ADV);
   le_fill_tx_header(20<<3);
  
   for(i=0;i<20;i++)le_fill_tx_payload(i,0xaa);
   CLEAR_PERI_REG_MASK(BT_BITS_BT_BUFFER_CTRL_REG,BT_BITS_BUFFER_CTRL_APB_MODE);
   // set 1m symbol length
   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_REG) = (READ_PERI_REG(BT_BITS_BT_BUFFER2TX_CTRL_REG)&(~0x7fffff)) | (0)|(4<<7)|(1<<15); // sadder | eadder(cancelled) |(lsb first)

   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_3_REG) =8+32+16+(20*8);      //1m bit length

   }

void le_fill_tx_buffer_num(void){
   u32 i;
   SET_PERI_REG_MASK(BT_BITS_BT_BUFFER_CTRL_REG,BT_BITS_BUFFER_CTRL_APB_MODE);
   for(i=0;i<256;i++)WRITE_PERI_REG(REG_BT_BUFFER_BASE+(4*i),0); //clear buffer

   // fill 1m symbols
   le_fill_tx_access_addr(ACCESS_ADDR_ADV);
   le_fill_tx_header(20<<3);
  
   for(i=0;i<20;i++)le_fill_tx_payload(i,(i&0xf)|((i&0xf)<<4));
   CLEAR_PERI_REG_MASK(BT_BITS_BT_BUFFER_CTRL_REG,BT_BITS_BUFFER_CTRL_APB_MODE);
   // set 1m symbol length
   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_REG) =(READ_PERI_REG(BT_BITS_BT_BUFFER2TX_CTRL_REG)&(~0x7fffff)) | (0)|(4<<7)|(1<<15); // sadder | eadder(cancelled) |(lsb first)

   *(volatile U32*)(BT_BITS_BT_BUFFER2TX_CTRL_3_REG) =8+32+16+(20*8);      //1m bit length

   }

void le_fill_tx_access_addr(u32 access_addr){
   if((access_addr&1)==1)SET_PERI_REG_BITS(REG_BT_BUFFER_BASE,0xff,0x55,0);
   else SET_PERI_REG_BITS(REG_BT_BUFFER_BASE,0xff,0xaa,0);
   SET_PERI_REG_BITS(REG_BT_BUFFER_BASE,0xffffff,access_addr,8);
   SET_PERI_REG_BITS(REG_BT_BUFFER_BASE+4,0xff,access_addr>>24,0);
}
void le_fill_tx_header(u32 header){
   SET_PERI_REG_BITS(REG_BT_BUFFER_BASE+4,0xffff,header,8);
}

void le_fill_tx_payload(u32 byte_cnt,u32 data){
   u32 word_offset,byte_offset,byte;
   byte=byte_cnt+7;
   word_offset=byte/4;
   byte_offset=byte%4;
   SET_PERI_REG_BITS(REG_BT_BUFFER_BASE+(4*word_offset),0xff,data,8*byte_offset);
}

// LE with lc
void le_lc_fill_tx_attributes(u32 len,u32 type, u32 crypt){
   u32 mask=0x1f;
   if(type==1){
      mask=0x3f;
      SET_PERI_REG_MASK(WDEVLETX0_CONF0,WDEV_LETX0_TYPE);
      SET_PERI_REG_BITS(WDEVLETX0_HEAD,mask,len,8);
   }else{
      CLEAR_PERI_REG_MASK(WDEVLETX0_CONF0,WDEV_LETX0_TYPE);
      SET_PERI_REG_BITS(WDEVLETX0_HEAD,mask,len,8);
   }

   SET_PERI_REG_BITS(WDEVLETX0_CONF0,WDEV_LETX0_LINK_ADDR,BT_TXBUF_START,WDEV_LETX0_LINK_ADDR_S);
   SET_PERI_REG_BITS(WDEVLETX0_CONF0,WDEV_LETX0_LEN,len,WDEV_LETX0_LEN_S);
   if(crypt==1)SET_PERI_REG_MASK(WDEVLETX0_CONF0,WDEV_LETX0_CRYPT);
   else CLEAR_PERI_REG_MASK(WDEVLETX0_CONF0,WDEV_LETX0_CRYPT);
}

void le_lc_tx_start(){
   SET_PERI_REG_MASK(INT_CLR_WDEVLE,WDEV_LETXEND_INT_CLR);
   while(GET_PERI_REG_MASK(INT_RAW_WDEVLE,WDEV_LETXEND_INT_RAW)==WDEV_LETXEND_INT_RAW);
   SET_PERI_REG_MASK(WDEVLETX0_CONF0,WDEV_LETX0_ENA);
}

u32 le_lc_wait4tx(){
   while(GET_PERI_REG_MASK(INT_RAW_WDEVLE,WDEV_LETXEND_INT_RAW)!=WDEV_LETXEND_INT_RAW){}
   return GET_PERI_REG_BITS(WDEVLE_TXPMD,WDEV_LETXEND_STATE,WDEV_LETXEND_STATE_S);
}

void le_lc_fill_rx_attributes(u32 type, u32 crypt){
  if(type==1){
      SET_PERI_REG_MASK(WDEVLERX0_CONF,WDEV_LERX0_TYPE);
  }else{
      CLEAR_PERI_REG_MASK(WDEVLERX0_CONF,WDEV_LERX0_TYPE);
  }
   if(crypt==1)SET_PERI_REG_MASK(WDEVLERX0_CONF,WDEV_LERX0_CRYPT);
   else CLEAR_PERI_REG_MASK(WDEVLERX0_CONF,WDEV_LERX0_CRYPT);

}

void le_lc_rx_start(){
   SET_PERI_REG_MASK(INT_CLR_WDEVLE,WDEV_LERXEND_INT_CLR);
   while(GET_PERI_REG_MASK(INT_RAW_WDEVLE,WDEV_LERXEND_INT_RAW)==WDEV_LERXEND_INT_RAW);
   SET_PERI_REG_MASK(WDEVLERX0_CONF,WDEV_LERX0_ENA);
}

u32 le_lc_wait4rx(){
   while(GET_PERI_REG_MASK(INT_RAW_WDEVLE,WDEV_LERXEND_INT_RAW)!=WDEV_LERXEND_INT_RAW){}
   return GET_PERI_REG_BITS(WDEVLE_RXPMD,WDEV_LERXEND_STATE,WDEV_LERXEND_STATE_S);
}

int le_mac_loopback_df(void){
   u32 tx_length= GET_PERI_REG_BITS(WDEVLETX0_CONF0,WDEV_LETX0_LEN,WDEV_LETX0_LEN_S);
   u32 rx_length= (READ_PERI_REG(READ_PERI_REG(WDEVLE_RXBASE))&(0x3f<<8))>>8;

   printinfo("tx length\n",tx_length);
   printinfo("rx length\n",rx_length);

   int i;
   u32 tx_data,rx_data,mem_offset,shift;
   for(i=0;i<tx_length;i=i+1){
      mem_offset=i/4;
      shift=i%4;
      tx_data=READ_PERI_REG(BT_TXBUF_START+(mem_offset*4))&((0xff)<<(8*shift));
      rx_data=READ_PERI_REG(READ_PERI_REG(WDEVLE_RXBASE)+((mem_offset+2)*4))&((0xff)<<(8*shift));
      printinfo("tx data\n",tx_data>>(8*shift));
      printinfo("rx data\n",rx_data>>(8*shift));
#ifdef BT_SIM_DEBUG
      bt_sim_debug(2, mem_offset, shift,tx_data>>(shift*8),rx_data>>(shift*8));
      printinfo("tx data\n",tx_data>>(8*shift));
      printinfo("rx data\n",rx_data>>(8*shift));
#else
     if(tx_data!=rx_data)fail("DIAG FAIL!\n");
#endif
   }
}






// rw bt cfg
//#define RF_SLACK 30
#define RF_SLACK 51
void rw_bt_init(){
   SET_PERI_REG_BITS(BT_V2_BITS_PHASE_GEN_CFG_REG, BT_V2_BITS_HIGH_SEL, 2, BT_V2_BITS_HIGH_SEL_S);
   SET_PERI_REG_BITS(BT_V2_BITS_PHASE_GEN_CFG_REG, BT_V2_BITS_LOW_SEL, 2, BT_V2_BITS_LOW_SEL_S);
   //SET_PERI_REG_BITS(BT_V2_BITS_PHASE_GEN_CFG_REG, BT_V2_BITS_HIGH_SEL_BB, 2, BT_V2_BITS_HIGH_SEL_BB_S);
   SET_PERI_REG_MASK(BT_V2_BITS_PHASE_GEN_CFG_REG, BT_V2_BITS_PHASE_EN);
   //SET_PERI_REG_MASK(BT_V2_BITS_PHASE_GEN_CFG_REG, BT_V2_BITS_PHASE_EN_BB);



   //rw setting
mac_write (0x60031070,0x00000000); 

//# Set DP Corr enable
//# Set RFSEL to 0x2
//`ifdef RW_DM_CORRELATOR_INST
//DM_WR_RG 00000074 00001020
//`endif
SET_PERI_REG_MASK(0x60031074, 0x00001020);
//`ifndef RW_DM_CORRELATOR_INST
//DM_WR_RG 00000074 00004020
//`endif


//# Set field count on sync value to 0x2
//# Set sync Error to 0x7
//BT_WR_RG 00000078 04070100
mac_write (0x60031478, 0x04070100);

//# Set Tx Path delay to 0x2
//# Set rx path delay to 0x2
//
//BT_WR_RG 00000090 00000201
mac_write (0x60031490, 0x00000202);

//rate config
mac_write (0x6003147C,0x39003900);

   SET_PERI_REG_BITS(0x6003148c, 0xff, 180-RF_SLACK, 16); //rxpwrupct
   SET_PERI_REG_BITS(0x6003148c, 0xff, 180-RF_SLACK, 0); //txpwrupct
   CLEAR_PERI_REG_MASK(0x60031474, BIT(22));//no dpcorr_en
   //SET_PERI_REG_BITS(0x60031428, 0x1ff, 400, 0); //rxgrd_timeout
   //SET_PERI_REG_BITS(0x60031428, 0x3f, 0x2a, 24); //nwinsize

   SET_PERI_REG_MASK(0x60031400, BIT(12)); //disable seqn error
   SET_PERI_REG_MASK(0x60031400, BIT(16)); //disable whitening
   SET_PERI_REG_BITS(0x600314e0, 0x3ff, 446, 16); // prefetch abort time
   SET_PERI_REG_BITS(0x600314e0, 0x1ff, 300, 0); // prefetch time

   //SET_PERI_REG_MASK(0x60031428, BIT(16)); //TX RATE switch instant
   SET_PERI_REG_BITS(0x60031428, 0x1ff, 20, 0); //rxgrd_timeout

   SET_PERI_REG_MASK(0x60031530, BIT(0)); //wifi coex en

   
}


#define LE_SLACK 30
void rw_le_init(){
   //WRITE_PERI_REG(BT_BITS_BT_RW_EM_BASE_REG, 0x3ffc0000);
   //SET_PERI_REG_MASK(BT_BITS_BT_MUX_CFG_REG, BT_BITS_BT_MUX_RW_EN);
   //SET_PERI_REG_BITS(BT_BITS_BT_RW_LE_CFG_REG, BT_BITS_RW_LE_TX_EN_DELAY, 128-LE_SLACK, BT_BITS_RW_LE_TX_EN_DELAY_S);
   //SET_PERI_REG_BITS(BT_BITS_BT_RW_LE_CFG_REG, BT_BITS_RW_LE_RX_EN_DELAY, 110-LE_SLACK, BT_BITS_RW_LE_RX_EN_DELAY_S);
   SET_PERI_REG_BITS(BT_V2_BITS_PHASE_GEN_CFG_REG, BT_V2_BITS_HIGH_SEL, 2, BT_V2_BITS_HIGH_SEL_S);
   SET_PERI_REG_BITS(BT_V2_BITS_PHASE_GEN_CFG_REG, BT_V2_BITS_LOW_SEL, 2, BT_V2_BITS_LOW_SEL_S);
   SET_PERI_REG_MASK(BT_V2_BITS_PHASE_GEN_CFG_REG, BT_V2_BITS_PHASE_EN);
   // above now move to LC reg
   SET_PERI_REG_BITS(0x600310f8,0x7,2,4);
   SET_PERI_REG_BITS(0x600310f8,0x7,2,8);
   SET_PERI_REG_MASK(0x600310f8,BIT(0));



   //rw setting
   CLEAR_PERI_REG_MASK(0x60031074, BIT(13));//no dpcorr_en
   
   //1m
   SET_PERI_REG_BITS(0x60031080, 0xff, 130-LE_SLACK, 0); //txpwrup
   SET_PERI_REG_BITS(0x60031080, 0xff, 130-LE_SLACK, 16); //rxpwrup
   SET_PERI_REG_BITS(0x60031080, 0xff, 256-10, 24); //rxsync poistion


   //2m
   SET_PERI_REG_BITS(0x60031084, 0xff, 130-LE_SLACK, 0); //txpwrup
   SET_PERI_REG_BITS(0x60031084, 0xff, 130-LE_SLACK, 16); //rxpwrup
   SET_PERI_REG_BITS(0x60031084, 0xff, 256-10, 24); //rxsync poistion

   //S8
    SET_PERI_REG_BITS(0x60031088, 0xff, 130-LE_SLACK, 0); //txpwrup
   SET_PERI_REG_BITS(0x60031088, 0xff, 130-LE_SLACK, 16); //rxpwrup  

   //S2
    SET_PERI_REG_BITS(0x6003108c, 0xff, 130-LE_SLACK, 0); //txpwrup
   SET_PERI_REG_BITS(0x6003108c, 0xff, 130-LE_SLACK, 16); //rxpwrup  
   

   SET_PERI_REG_BITS(0x60031000, 0xf, 0xf, 0); //rxwinszdef
   
   SET_PERI_REG_MASK(0x60031000, BIT(14)); //disable whitening

   SET_PERI_REG_BITS(0x600310e0, 0x3ff, 446, 16); // prefetch abort time
   SET_PERI_REG_BITS(0x600310e0, 0x1ff, 250, 0); //prefetch time
   
   SET_PERI_REG_MASK(0x60031150, BIT(0));//wifi coex en
   

//#----------------------------------------------------------------------------
//# ExtRC RF Settings
//#----------------------------------------------------------------------------
mac_write (0x60031070,0x00000000); 

//# Set DP Corr enable
//# Set RFSEL to 0x2
//`ifdef RW_DM_CORRELATOR_INST
//DM_WR_RG 00000074 00001020
//`endif
SET_PERI_REG_MASK(0x60031074, 0x00001020);
//`ifndef RW_DM_CORRELATOR_INST
//DM_WR_RG 00000074 00004020
//`endif


//# Set field count on sync value to 0x2
//# Set sync Error to 0x7
//BT_WR_RG 00000078 04070100
mac_write (0x60031478, 0x04070100);

//# Set Tx Path delay to 0x2
//# Set rx path delay to 0x2
//
//BT_WR_RG 00000090 00000201
mac_write (0x60031490, 0x00000202);

//# Set phymsk to support LR + 2Mbps
//LE_WR_RG 00000078 C8C00100
mac_write (0x60031078, 0xc8c00100);
   SET_PERI_REG_BITS(0x60031078,0x7, 4, 16); // corr err

//LE_WR_RG 00000094 00000101
mac_write (0x60031094, 0x00000101); //2m RX Path delay
//
//LE_WR_RG 00000098 0F020201
mac_write (0x60031098, 0x0f020201); //TX RX Path delay for S2/8

mac_write (0x6003109c, 0x0d000001); //TX RX Path delay for S2
//

//DI Radio Initialization Done
//printinfo("radio initialization done \n", 1);
//
//#----------------------------------------------------------------------------
//# Init Prefetch Time and Prefetch Abort Time APFM
//#----------------------------------------------------------------------------
//# BT_PREFETCHABORT_TIME_US 200 us
//# BT_PREFETCH_TIME_US 160 us
//BT_WR_RG 000000E0 01900140
//mac_write (0x600314e0, 0x01900140); //!!!!!!
//
//# BLE_PREFETCHABORT_TIME_US 160 us
//# BLE_PREFETCH_TIME_US 120 us
//LE_WR_RG 000000E0 014000F0
//mac_write (0x600310e0, 0x014000f0);//!!!!!!
//

//em slice
SET_PERI_REG_MASK(0x600312c4, BIT(0)); // EM base0 en
SET_PERI_REG_BITS(0x60031204, 0x3ffff, 0x30000 ,0); // EM base0
SET_PERI_REG_BITS(0x60031204, 0x3fff, 0x0 ,18); // EM base0 start
SET_PERI_REG_BITS(0x60031208, 0x3fff, 0x3fff ,18); // EM base1 start
   
}

void rw_32k_sel_8mdiv(){
   SET_PERI_REG_MASK(DPORT_BT_LPCK_DIV_FRAC_REG, DPORT_LPCLK_SEL_8M);
   SET_PERI_REG_MASK(RTC_CLK_CONF,RTC_CNTL_DIG_CLK8M_EN);
   SET_PERI_REG_BITS(DPORT_BT_LPCK_DIV_INT_REG, DPORT_BT_LPCK_DIV_NUM, 374, DPORT_BT_LPCK_DIV_NUM_S);
   SET_PERI_REG_BITS(DPORT_BT_LPCK_DIV_FRAC_REG, DPORT_BT_LPCK_DIV_A, 0, DPORT_BT_LPCK_DIV_A_S);
   SET_PERI_REG_BITS(DPORT_BT_LPCK_DIV_FRAC_REG, DPORT_BT_LPCK_DIV_B, 0, DPORT_BT_LPCK_DIV_B_S);
}

u32 rw_get_clkn(){
   SET_PERI_REG_MASK(0x6003101c,BIT(31));
   while(GET_PERI_REG_MASK(0x6003101c,BIT(31)));
   return GET_PERI_REG_BITS(0x6003101c, 0xfffffff, 0);
}

void coex_hard_init(){
  // wifi mac
   SET_PERI_REG_BITS(WDEVRWBT_COEX_WAIT1_REG, WDEV_WLAN_ANT_SEL_HEAD_WAIT, 0x10, WDEV_WLAN_ANT_SEL_HEAD_WAIT_S);
   SET_PERI_REG_BITS(WDEVRWBT_COEX_WAIT0_REG, WDEV_WLAN_ANT_SEL_TAIL_WAIT, 1600, WDEV_WLAN_ANT_SEL_TAIL_WAIT_S);
   SET_PERI_REG_BITS(WDEVRWBT_COEX_WAIT1_REG, WDEV_MAC_REFUSE_TIME, 0x10, WDEV_MAC_REFUSE_TIME_S);
   SET_PERI_REG_MASK(WDEVRWBT_COEX_CONF_REG, WDEV_RW_BT_COEX_EN);
   //SET_PERI_REG_BITS(WDEVRWBT_COEX_CONF, WDEV_RW_NBT_ACTIVE_BLE, 0x3, WDEV_RW_NBT_ACTIVE_BLE_S);
   // SET_PERI_REG_BITS(WDEVRWBT_COEX_CONF_REG, WDEV_RW_BT_ACTIVE_SEL, BIT(2), WDEV_RW_BT_ACTIVE_SEL_S);
   //SET_PERI_REG_BITS(WDEVRWBT_COEX_CONF, WDEV_RW_NBT_PRIO_BLE, 0x3, WDEV_RW_NBT_PRIO_BLE_S);
   SET_PERI_REG_BITS(WDEVRWBT_COEX_CONF_REG, WDEV_RW_BT_PRIO_SEL, BIT(0), WDEV_RW_BT_PRIO_SEL_S);
   
   SET_PERI_REG_BITS(WDEVRWBT_COEX_GPIO_SEL_REG,  WDEV_GPIO_BT_ACTIVE_SEL, 2, WDEV_GPIO_BT_ACTIVE_SEL_S); //GPIO force rw prio
   

   // rwbt open coex
   SET_PERI_REG_MASK(0x600310d0, BIT(0));// bt co-en
   SET_PERI_REG_MASK(0x600310d0, BIT(4)|BIT(5));// wlan tx block
   SET_PERI_REG_MASK(0x600310d0, BIT(6)|BIT(7));// wlan rx block
   READ_PERI_REG(0x600310d0);
   *(volatile U8*)(0x600310d1) = BIT(1);
   READ_PERI_REG(0x600310d0);
   *(volatile U16*)(0x600310d2) = BIT(0)|BIT(15);
   READ_PERI_REG(0x600310d0);
   *(volatile U16*)(0x600310d2);


}

void coex_hard_toggle(){
   if(GET_PERI_REG_MASK(GPIO_FUNC37_IN_SEL_CFG_REG, GPIO_FUNC37_IN_INV_SEL))CLEAR_PERI_REG_MASK(GPIO_FUNC37_IN_SEL_CFG_REG, GPIO_FUNC37_IN_INV_SEL);
   else SET_PERI_REG_MASK(GPIO_FUNC37_IN_SEL_CFG_REG, GPIO_FUNC37_IN_INV_SEL);
}

void coex_soft_init(){
  // wifi mac
   SET_PERI_REG_BITS(WDEVRWBT_COEX_WAIT1_REG, WDEV_WLAN_ANT_SEL_HEAD_WAIT, 0x10, WDEV_WLAN_ANT_SEL_HEAD_WAIT_S);
   SET_PERI_REG_BITS(WDEVRWBT_COEX_WAIT0_REG, WDEV_WLAN_ANT_SEL_TAIL_WAIT, 1600, WDEV_WLAN_ANT_SEL_TAIL_WAIT_S);
   SET_PERI_REG_BITS(WDEVRWBT_COEX_WAIT1_REG, WDEV_MAC_REFUSE_TIME, 0x10, WDEV_MAC_REFUSE_TIME_S);
   SET_PERI_REG_MASK(WDEVRWBT_COEX_CONF_REG, WDEV_RW_BT_COEX_EN);
   //SET_PERI_REG_BITS(WDEVRWBT_COEX_CONF, WDEV_RW_NBT_ACTIVE_BLE, 0x3, WDEV_RW_NBT_ACTIVE_BLE_S);
   // SET_PERI_REG_BITS(WDEVRWBT_COEX_CONF_REG, WDEV_RW_BT_ACTIVE_SEL, BIT(0), WDEV_RW_BT_ACTIVE_SEL_S);
   //SET_PERI_REG_BITS(WDEVRWBT_COEX_CONF, WDEV_RW_NBT_PRIO_BLE, 0x3, WDEV_RW_NBT_PRIO_BLE_S);
   SET_PERI_REG_BITS(WDEVRWBT_COEX_CONF_REG, WDEV_RW_BT_PRIO_SEL, BIT(0), WDEV_RW_BT_PRIO_SEL_S);
   
   SET_PERI_REG_BITS(WDEVRWBT_COEX_GPIO_SEL_REG,  WDEV_GPIO_BT_ACTIVE_SEL, 2, WDEV_GPIO_BT_ACTIVE_SEL_S); //GPIO force rw prio & active



}


void coex_soft_toggle(){

   if(GET_PERI_REG_MASK(GPIO_FUNC37_IN_SEL_CFG_REG, GPIO_FUNC37_IN_INV_SEL)){ //force wifi
      CLEAR_PERI_REG_MASK(GPIO_FUNC37_IN_SEL_CFG_REG, GPIO_FUNC37_IN_INV_SEL);
      SET_PERI_REG_BITS(AGCBT_CTRL1_REG, AGC_FORCE_BT_MODE, 2, AGC_FORCE_BT_MODE_S);
   }
   else{
      SET_PERI_REG_MASK(GPIO_FUNC37_IN_SEL_CFG_REG, GPIO_FUNC37_IN_INV_SEL);
      SET_PERI_REG_BITS(AGCBT_CTRL1_REG, AGC_FORCE_BT_MODE, 3, AGC_FORCE_BT_MODE_S);
   }
}

void force_bt_mode(){
   //force fe
   SET_PERI_REG_BITS(AGCBT_CTRL1_REG, AGC_FORCE_BT_MODE, 3, AGC_FORCE_BT_MODE_S);
   //force agc
   // SET_PERI_REG_BITS(WDEVRWBT_COEX_CONF_REG, WDEV_RW_BT_ACTIVE_SEL, BIT(0), WDEV_RW_BT_ACTIVE_SEL_S);
   SET_PERI_REG_BITS(WDEVRWBT_COEX_CONF_REG, WDEV_RW_BT_PRIO_SEL, BIT(0), WDEV_RW_BT_PRIO_SEL_S);   
   SET_PERI_REG_BITS(WDEVRWBT_COEX_WAIT1_REG, WDEV_WLAN_ANT_SEL_HEAD_WAIT, 0x10, WDEV_WLAN_ANT_SEL_HEAD_WAIT_S);
   SET_PERI_REG_BITS(WDEVRWBT_COEX_WAIT0_REG, WDEV_WLAN_ANT_SEL_TAIL_WAIT, 1600, WDEV_WLAN_ANT_SEL_TAIL_WAIT_S);
   SET_PERI_REG_BITS(WDEVRWBT_COEX_WAIT1_REG, WDEV_MAC_REFUSE_TIME, 0x10, WDEV_MAC_REFUSE_TIME_S);
 
   SET_PERI_REG_BITS(WDEVRWBT_COEX_GPIO_SEL_REG,  WDEV_GPIO_BT_ACTIVE_SEL, 2, WDEV_GPIO_BT_ACTIVE_SEL_S); //GPIO force BT 
   SET_PERI_REG_MASK(GPIO_FUNC37_IN_SEL_CFG_REG, GPIO_FUNC37_IN_INV_SEL);

}

void coex_pti_init(){
   //change bt mode off delay
   //SET_PERI_REG_BITS(BT_BITS_BT_BB2FE_REG, BT_BITS_BT_MODE_OFF_INIT, 245, BT_BITS_BT_MODE_OFF_INIT_S);

  // wifi mac
   SET_PERI_REG_BITS(WDEVRWBT_COEX_WAIT1_REG, WDEV_WLAN_ANT_SEL_HEAD_WAIT, 0x10, WDEV_WLAN_ANT_SEL_HEAD_WAIT_S);
   SET_PERI_REG_BITS(WDEVRWBT_COEX_WAIT0_REG, WDEV_WLAN_ANT_SEL_TAIL_WAIT, 1600, WDEV_WLAN_ANT_SEL_TAIL_WAIT_S);
   SET_PERI_REG_BITS(WDEVRWBT_COEX_WAIT1_REG, WDEV_MAC_REFUSE_TIME, 0x10, WDEV_MAC_REFUSE_TIME_S);
   //SET_PERI_REG_BITS(WDEVRWBT_COEX_CONF, WDEV_RW_NBT_ACTIVE_BLE, 0x3, WDEV_RW_NBT_ACTIVE_BLE_S);
   // SET_PERI_REG_BITS(WDEVRWBT_COEX_CONF_REG, WDEV_RW_BT_ACTIVE_SEL,BIT(2), WDEV_RW_BT_ACTIVE_SEL_S);
   //SET_PERI_REG_BITS(WDEVRWBT_COEX_CONF, WDEV_RW_NBT_PRIO_BLE, 0x3, WDEV_RW_NBT_PRIO_BLE_S);
   SET_PERI_REG_BITS(WDEVRWBT_COEX_CONF_REG, WDEV_RW_BT_PRIO_SEL, BIT(3)|BIT(2), WDEV_RW_BT_PRIO_SEL_S);
   SET_PERI_REG_BITS(WDEVRWBT_COEX_CONF_REG, WDEV_FREQ_HOP_TIMER, 60, WDEV_FREQ_HOP_TIMER_S);
   SET_PERI_REG_MASK(WDEVRWBT_COEX_CONF_REG, WDEV_RW_BT_COEX_EN);


   // rwbt open coex
   SET_PERI_REG_MASK(0x60031150, BIT(0));// bt co-en
   SET_PERI_REG_MASK(0x60031150, BIT(4)|BIT(5));// wlan tx block
   SET_PERI_REG_MASK(0x60031150, BIT(6)|BIT(7));// wlan rx block

   //le  open coex
   SET_PERI_REG_MASK(0x60031300, BIT(0));//wifi coex en
   SET_PERI_REG_BITS(0x60031300, 0xf, 0xf, 4);
   

   //open coex timer0 force for WIFI
   SET_PERI_REG_MASK(WDEVRWBT_COEX_TIMER0_CONF0_REG, WDEV_COEX_TIMER0_ENA|WDEV_COEX_TIMER0_FH);
   

   //WDEVBBCCAHUNG change larger
//lyun   CLEAR_PERI_REG_MASK(WDEVBBCCAHUNG_REG,  WDEV_BBCCAHUNG_ENA); 
 

   //lc ifs pti
   SET_PERI_REG_MASK(0x60031048,BIT(8));
   SET_PERI_REG_BITS(0x60031048,0xf,0xf,4);
   
   
}

void coex_pti_toggle(){
   //  if(GET_PERI_REG_BITS(WDEVRWBT_COEX_PTI_REG, WDEV_WLAN_DEFAULT_PTI, WDEV_WLAN_DEFAULT_PTI_S)){
   //     SET_PERI_REG_BITS(WDEVRWBT_COEX_PTI_REG, WDEV_WLAN_DEFAULT_PTI, 0x0, WDEV_WLAN_DEFAULT_PTI_S);
   //  }
   //  else SET_PERI_REG_BITS(WDEVRWBT_COEX_PTI_REG, WDEV_WLAN_DEFAULT_PTI, 0xf, WDEV_WLAN_DEFAULT_PTI_S);
}

void coex_timer_pti_toggle(){
   if(GET_PERI_REG_BITS(WDEVRWBT_COEX_TIMER0_CONF0_REG, WDEV_COEX_TIMER0_PTI, WDEV_COEX_TIMER0_PTI_S)){
      SET_PERI_REG_BITS(WDEVRWBT_COEX_TIMER0_CONF0_REG, WDEV_COEX_TIMER0_PTI, 0x0, WDEV_COEX_TIMER0_PTI_S);
   }
   else SET_PERI_REG_BITS(WDEVRWBT_COEX_TIMER0_CONF0_REG, WDEV_COEX_TIMER0_PTI, 0xf, WDEV_COEX_TIMER0_PTI_S);
}




void set_freq_init(){
   SET_PERI_REG_MASK(I2C_MST_SET_FREQ_CTRL0_REG, BIT(24));
   SET_PERI_REG_BITS(I2C_MST_SET_FREQ_CTRL0_REG, 0x1f, 8, 10);
   WRITE_PERI_REG(I2C_MST_SET_FREQ_I2C_DELAY_EN_REG, 0xffffffff);
   WRITE_PERI_REG(I2C_MST_SET_FREQ_I2C_DELAY_REG, 240);
   

}
