#include <xtensa/hal.h>
#include <xtensa/config/core.h>
#include <xtensa/config/system.h>

#include "./../include_new/common.h"
#include "./../include_new/soc_base.h"
#include "./../include_new/bus.h"
#include "./../include_new/diag_utils.h"

#include "./../include_new/system_reg.h"
#include "./../include_new/apb_ctrl_reg.h"
#include "./../include_new/mac_register_new.h"
#include "./../include_new/interrupt_reg.h"

#define TXBUF_LK_START       ADDR_DRAM0_SRAM_5+0xb000
#define TXBUF_START          ADDR_DRAM0_SRAM_5+0xc102//+0x1c100

#define RXBLOCK_NUM         0x20
#define RXBUF_START         ADDR_DRAM0_SRAM_5
#define RXBUF_BLOCK_SIZE    0x400
#define RXBUF_SIZE          0x8000
#define RXBUF_LK_START      ADDR_DRAM0_SRAM_5 + 0x8000 
#define RXBUF_LK_SIZE       RXBUF_SIZE/RXBUF_BLOCK_SIZE*12 //0x180


#define RX_CTRL_ADDR  WDEVPWRDATE_REG

void txbuffer_init(){
  int i = 0;
  *(volatile U32*)(TXBUF_LK_START) = (0x1<<31) + (0x1<<30) + (0x0<<29) + (0x65<<12)  + (0x69<<0);
  *(volatile U32*)(TXBUF_LK_START+4) = TXBUF_START;
  *(volatile U32*)(TXBUF_LK_START+8) = 0;

  for (i=0; i<8; i++){
    SET_PERI_REG_BITS(WDEVTXQ_PLCP0_REG( i ) , WDEV_TXQ_LINK_ADDR, TXBUF_LK_START, WDEV_TXQ_LINK_ADDR_S);
    SET_PERI_REG_BITS(WDEVTXQ_PLCP1_REG( i ),  WDEV_TXQ_LENGTH, 0x65, WDEV_TXQ_LENGTH_S);
  }
}

void mac_soc_init()
{
  // init
  //SET_PERI_REG_MASK(APB_CTRL_WIFI_CLK_EN_REG, BIT(6));
  WRITE_PERI_REG( APB_CTRL_WIFI_CLK_EN_REG, 0xffffffff );
  SET_PERI_REG_MASK(WDEVTXQMEM_REG, WDEV_TXQMEM_CLEAR);
  while(((READ_PERI_REG(WDEVTXQMEM_REG))&WDEV_TXQMEM_READY) == 0){}
  WRITE_PERI_REG(WDEVDA0LO_REG, 0x03020100);
  WRITE_PERI_REG(WDEVDA0HI_REG, 0x0504);
  WRITE_PERI_REG(WDEVBSSID0_MASKLO_REG, 0xffffffff);
  WRITE_PERI_REG(WDEVBSSID0_MASKHI_REG, 0x1ffff);
  WRITE_PERI_REG(WDEVBSSID0LO_REG, 0x03020100);
  WRITE_PERI_REG(WDEVBSSID0HI_REG, 0x0504);
}


void mac_rx_start(int dumpfile_index)
{
  int input_sel;
  input_sel = (dumpfile_index>>0)&0xf;
  //begin rx test
  *(volatile U32*)(RX_CTRL_ADDR)      = *(volatile U32*) (RX_CTRL_ADDR) & 0xffffffef | (0x1<<4);  //set GPIO4 : reset ptr for dumping rx data in bench
  *(volatile U32*)(RX_CTRL_ADDR)      = *(volatile U32*) (RX_CTRL_ADDR) & 0xffffffd1 | (0x6<<1);  //set GPIO3~1 : to control rx data source
  *(volatile U32*)(RX_CTRL_ADDR)      = *(volatile U32*) (RX_CTRL_ADDR) & 0xffffffd1 | ((input_sel & 0x7)<<1) | (((input_sel>>3) & 0x1)<<5);  //set GPIO3~1 and GPIO5: to control rx data source
  *(volatile U32*)(RX_CTRL_ADDR)      = *(volatile U32*) (RX_CTRL_ADDR) & 0xffffffef | (0x0<<4);  //set GPIO4 : release ptr for dumping rx data in bench
}

void rxbuffer_init(){

  int i;
  int rxbuflkad[RXBLOCK_NUM];
  int rxbufad[RXBLOCK_NUM];

  rxbuflkad[0] = RXBUF_LK_START;
  for ( i=1; i<RXBLOCK_NUM; i++){
    rxbuflkad[i]= rxbuflkad[i-1]+12; 
  }
  rxbufad[0] = RXBUF_START; // 0x30000--0x36400
  for (i=1; i<RXBLOCK_NUM; i++){
    rxbufad[i] = rxbufad[i-1] + RXBUF_BLOCK_SIZE;//200 BUFFER SIZE
  }
  // init rxbuf dscr
  for (i=0; i<RXBLOCK_NUM ; i++){    
    WRITE_PERI_REG(rxbuflkad[i], (0x1<<31)+RXBUF_BLOCK_SIZE);//200 BUFFER SIZE
    WRITE_PERI_REG(rxbuflkad[i]+4, rxbufad[i]);
    WRITE_PERI_REG(rxbuflkad[i]+8, rxbuflkad[i+1]);
  }
  WRITE_PERI_REG(rxbuflkad[RXBLOCK_NUM-1]+8, rxbuflkad[0]);
  WRITE_PERI_REG(WDEVRXBASE_REG, rxbuflkad[0]);  //+0x2000 is for sw, so max rx length should <4096bytes
}



void mac_interrupt_enable(void * interrupt_handler)
{
  SET_PERI_REG_BITS(INTERRUPT_PRO_MAC_INTR_MAP_REG, INTERRUPT_PRO_MAC_INTR_MAP, 10, INTERRUPT_PRO_MAC_INTR_MAP_S);
  SET_PERI_REG_BITS(INTERRUPT_PRO_PWR_INTR_MAP_REG, INTERRUPT_PRO_PWR_INTR_MAP, 10, INTERRUPT_PRO_PWR_INTR_MAP_S);
  
  _xtos_set_interrupt_handler_arg(10, interrupt_handler, 0);
  _xtos_ints_on(1 <<10);
}

void mac_interrupt_disable()
{
  _xtos_ints_off(1 << 10);
}


//==========================
#define AUTO_IDLE  0
#define TXRTS_START  1
#define TXRTS_END  2
#define RXCTS_START  3
#define RXCTS_END  4
#define TXDATA_START  5
#define TXDATA_END  6
#define RXACK_START  7
#define RXACK_END  8
#define AUTO_DONE  9


u32 auto_state= AUTO_IDLE;


void auto_isr_init()
{
  SET_PERI_REG_MASK(INT_ENA_WDEV_REG, WDEV_TXSTART_INT|WDEV_TXEND_INT|WDEV_RXEND_INT|WDEV_RXSTART_INT|WDEV_TXCOMPLETE_INT);
}
void auto_isr_deinit()
{
  CLEAR_PERI_REG_MASK(INT_ENA_WDEV_REG, WDEV_TXSTART_INT|WDEV_TXEND_INT|WDEV_RXEND_INT|WDEV_RXSTART_INT|WDEV_TXCOMPLETE_INT);
}
void auto_fsm_reset(){
  auto_state= AUTO_IDLE;
  WRITE_PERI_REG(WDEVSIM_FINISH_REG, 0x0);
}
void auto_isr()
{
  u32 int_st = READ_PERI_REG(INT_ST_WDEV_REG);
  WRITE_PERI_REG(INT_CLR_WDEV_REG, int_st);    
  SET_PERI_REG_MASK(WDEVSIM_FINISH_REG, BIT(31));
  if (int_st & WDEV_RXEND_INT){
    SET_PERI_REG_MASK(RX_CTRL_ADDR, BIT(4));
  }

  // FSM
  if (auto_state == AUTO_IDLE){
    if (int_st & WDEV_TXSTART_RTS_INT){
      auto_state = TXRTS_START;
      SET_PERI_REG_BITS(WDEVSIM_FINISH_REG, 0xff, auto_state, 0);
      //ets_print("*%d\n", auto_state);
    } 
  }
  
  if (auto_state == TXRTS_START){
    if (int_st & WDEV_TXEND_INT){
      auto_state = TXRTS_END;
      SET_PERI_REG_BITS(WDEVSIM_FINISH_REG, 0xff, auto_state, 0);
      //ets_print("*%d\n", auto_state);
    }
  }
  
  if (auto_state == TXRTS_END){
    if (int_st & WDEV_RXSTART_INT){
      auto_state = RXCTS_START;
      SET_PERI_REG_BITS(WDEVSIM_FINISH_REG, 0xff, auto_state, 0);
      //ets_print("*%d\n", auto_state);
    }
  }
  
  if (auto_state == RXCTS_START){
    if (int_st & WDEV_RXEND_INT){
      auto_state = RXCTS_END;
      SET_PERI_REG_BITS(WDEVSIM_FINISH_REG, 0xff, auto_state, 0);
      //ets_print("*%d\n", auto_state);
    }
  }
  
  if (auto_state == RXCTS_END){
    if (int_st & WDEV_TXSTART_DATA_INT){
      auto_state = TXDATA_START;
      SET_PERI_REG_BITS(WDEVSIM_FINISH_REG, 0xff, auto_state, 0);
      //ets_print("*%d\n", auto_state);
    }
  }
  
  if (auto_state == TXDATA_START){
    if (int_st & WDEV_TXEND_INT){
      auto_state = TXDATA_END;
      SET_PERI_REG_BITS(WDEVSIM_FINISH_REG, 0xff, auto_state, 0);
      //ets_print("*%d\n", auto_state);
    }
  }
  
  if (auto_state == TXDATA_END){
    if (int_st & WDEV_RXSTART_INT){
      auto_state = RXACK_START;
      SET_PERI_REG_BITS(WDEVSIM_FINISH_REG, 0xff, auto_state, 0);
      //ets_print("*%d\n", auto_state);
    }
  }
  
  if (auto_state == RXACK_START){
    if (int_st & WDEV_RXEND_INT){
      auto_state = RXACK_END;
      SET_PERI_REG_BITS(WDEVSIM_FINISH_REG, 0xff, auto_state, 0);
      //ets_print("*%d\n", auto_state);
    }
  }

  if (int_st & WDEV_TXCOMPLETE_INT ){
    auto_state = AUTO_DONE;
    SET_PERI_REG_BITS(WDEVSIM_FINISH_REG, 0xff, auto_state, 0);
    //ets_print("*%d\n", auto_state);
  }

  CLEAR_PERI_REG_MASK(WDEVSIM_FINISH_REG, BIT(31));
}

void rx_cts()
{
  delay_us(16);
  mac_rx_start(7);  
}

void rx_ack()
{
  delay_us(16);
  mac_rx_start(6);  

}

void rx_data()
{
  delay_us(16);
  mac_rx_start(1);  
}
