
#ifdef MAC_COMMON

#else

#define MAC_COMMON

#include <xtensa/hal.h>
#include <xtensa/config/core.h>
#include <xtensa/config/system.h>
#include "./common.h"
#include "./soc_base.h"
#include "./bus.h"
#include "./diag_utils.h"

#include "./mac_reg.h"
#include "./fe_reg.h"
#include "./brx_reg.h"
#include "./bt_mac_reg.h"
#include "./bt_le_reg.h"
#include "./sensitive_reg.h"
#include "./apb_ctrl_reg.h"
#define  R1ML      0x0
#define  R2ML      0x1
#define  R5P5ML    0x2
#define  R11ML     0x3
#define  R1MS      0x4
#define  R2MS      0x5
#define  R5P5MS    0x6
#define  R11MS     0x7
#define  LROCT     0x10
#define  LRQUT     0x11
#define  LRHLF     0x12
#define  LRQUTQ    0x15
#define  LRHLFQ    0x16
#define  LR1MQ     0x17
#define  LRQUTR    0x19
#define  LRHLFR    0x1A
#define  R6M       0xB
#define  R9M       0xF
#define  R12M      0xA
#define  R18M      0xE
#define  R24M      0x9
#define  R36M      0xD
#define  R48M      0x8
#define  R54M      0xC
#define  MCS0      0x100
#define  MCS1      0x101
#define  MCS2      0x102
#define  MCS3      0x103
#define  MCS4      0x104
#define  MCS5      0x105
#define  MCS6      0x106
#define  MCS7      0x107
#define  MCS32     0x120
#define  VHT_MCS0      0x200
#define  VHT_MCS1      0x201
#define  VHT_MCS2      0x202
#define  VHT_MCS3      0x203
#define  VHT_MCS4      0x204
#define  VHT_MCS5      0x205
#define  VHT_MCS6      0x206
#define  VHT_MCS7      0x207
#define  SHORTGI   0x2
#define  NORMALGI  0x0
#define  SHORTGI_LDPC    0x3
#define  NORMALGI_LDPC   0x1
#define  CBW20 0x0
#define  CBW40 0x1

#define RXBUFFER_BASE 0x3ffbc000
#define RXBLOCK_NUM         0x20
#define RXBUF_START         RXBUFFER_BASE
#define RXBUF_BLOCK_SIZE    0x400
#define RXBUF_SIZE          0x8000
#define RXBUF_LK_START      RXBUFFER_BASE + 0x8000 
#define RXBUF_LK_SIZE       RXBUF_SIZE/RXBUF_BLOCK_SIZE*12 //0x180
//
//
#define TXBUF_APLK_START       RXBUFFER_BASE+0xb100
#define TXBUF_APSTART          RXBUFFER_BASE+0xc0fc

#define TXBUF_LK_START       RXBUFFER_BASE+0xb000
#define TXBUF_START          RXBUFFER_BASE+0xc102//+0x1c100

#define RXEST_BUF_START     RXBUFFER_BASE + 0xb100


//#ifndef CHIP_ANA_MODE_SIM
//    #define RX_CTRL_ADDR  FE_NOUSE_REG
//#else
    #define RX_CTRL_ADDR  WDEVPWRDATE_REG   //BRXDATE_REG  //for CHIP_ANA_MODE_SIM sim
//#endif

void txend_delay_us(unsigned int n_us)
{
  unsigned int i = n_us * CPU_SPEED;  //cpu instruction speed: 8M/s
  while(GET_PERI_REG_MASK(WDEV_INT_ST_MAC_REG, WDEV_TXEND_INT_ENA) == 0){}
  SET_PERI_REG_MASK(WDEV_INT_CLR_MAC_REG, WDEV_TXEND_INT_ENA );
  while(i--){};
}


void mac_init()
{

  // =====rxbuffer init
  int i;
  int rxbuflkad[RXBLOCK_NUM];
  int rxbufad[RXBLOCK_NUM];
  int read_data;
  


  // digital clk to pll
  //delay_us(20);
  WRITE_PERI_REG( APB_CTRL_WIFI_CLK_EN_REG, 0xffffffff );
  SET_PERI_REG_BITS(APB_CTRL_SYSCLK_CONF_REG, APB_CTRL_SOC_CLK_SEL, 1, APB_CTRL_SOC_CLK_SEL_S);
  SET_PERI_REG_MASK(WDEVTXQMEM_REG, WDEV_TXQMEM_CLEAR);
  if(0){
  	SET_PERI_REG_BITS(WDEVTXIMR2_DUR_REG+16,0xffffffff,0x5a5a5a5a,0);
  	SET_PERI_REG_BITS(WDEVTXIMR2BA_TAHI_REG,0xffffffff,0x12345678,0);
  	read_data = READ_PERI_REG(WDEVTXIMR2_DUR_REG+16);

  	if(read_data != 0x5a5a5a5a){
  	       fail("fail"); 
  	}
  	SET_PERI_REG_BITS(WDEVTXIMR1BA_SSN_REG,0xffffffff,1,0);
  	SET_PERI_REG_BITS(WDEVTXIMR1PMD_REG,0xffffffff,0xa5a5a5a5,0);
  	read_data  = READ_PERI_REG(WDEVTXIMR1PMD_REG);
  	if(read_data != 0xa5a5a5a5){
  	       fail("fail"); 
  	}

  	SET_PERI_REG_BITS(WDEVTXIMR2_DUR_REG,0xffffffff,0x12345678,0);
  	read_data=READ_PERI_REG(WDEVTXIMR2BA_TAHI_REG);
  	if(read_data != 0x12345678){
  	       fail("fail"); 
  	}

  	for(i=0;i<61;i++){
  	        read_data=READ_PERI_REG(0x3ff21000+i*4);
  	        if(0x3ff21000+i*4 == WDEVTXIMR2_DUR_REG+16){
  			if(read_data != 0x5a5a5a5a){
  			       fail("fail"); 
  			}
  	        }else if(0x3ff21000+i*4 == WDEVTXIMR2BA_TAHI_REG){
  			if(read_data != 0x12345678){
  			       fail("fail"); 
  			}
  	        }else if(0x3ff21000+i*4 == WDEVTXIMR1BA_SSN_REG){
  			if(read_data != 0x1){
  			       fail("fail"); 
  			}
  	        }else if(0x3ff21000+i*4 == WDEVTXIMR1PMD_REG){
  			if(read_data != 0xa5a5a5a5){
  			       fail("fail"); 
  			}
  	        }else if(0x3ff21000+i*4 == WDEVTXIMR2_DUR_REG ){
  			if(read_data != 0x12345678){
  			       fail("fail"); 
  			}
  	        }else if(read_data != (0x50000+i)){
  	       	fail("fail"); 
  	        }
  	}
  }

  while(((READ_PERI_REG(WDEVTXQMEM_REG))&WDEV_TXQMEM_READY) == 0){
    WRITE_PERI_REG(WDEVTXIMR2_HT40LEN_REG, 0xd);
    WRITE_PERI_REG(WDEVTXIMR2_HT40LEN_REG, 0xe);
    READ_PERI_REG(WDEVTXIMR2_HT40LEN_REG);
    READ_PERI_REG(WDEVTXIMR2_HT40LEN_REG);
    
  }

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
  WRITE_PERI_REG(WDEVRXMODE_REG, 0x80000000);
  WRITE_PERI_REG(WDEVRXESTBASE_REG, RXEST_BUF_START);
  WRITE_PERI_REG(WDEVRXBUF_CONF_REG, 0x3000000c);
  WRITE_PERI_REG(WDEVRXMODE_REG, 0x80000000);
  WRITE_PERI_REG(WDEV_INT_ENA_MAC_REG, 0xf);
  WRITE_PERI_REG(WDEVDA0LO_REG, 0x03020100);
  WRITE_PERI_REG(WDEVDA0HI_REG, 0x0504);
  //SET_PERI_REG_MASK(WDEVRXOPTION_REG, WDEV_RXSUBAMPDU_LEN_HEAD);
  //mpdu discripter  
                                                        //eof     sub_sof   buffer_length  buffer_size 
  *(volatile U32*)(TXBUF_LK_START) = (0x1<<31) + (0x1<<30) + (0x0<<29) + (0x68<<12)  + (0x69<<0);
  *(volatile U32*)(TXBUF_LK_START+4) = TXBUF_START;
  *(volatile U32*)(TXBUF_LK_START+8) = TXBUF_LK_START+12;
  
  //ampdu discripter0
                                                        //eof     sub_sof   buffer_length  buffer_size 
  *(volatile U32*)(TXBUF_APLK_START) = (0x1<<31) + (0x0<<30) + (0x1<<29) + (0x69<<12)  + (0x69<<0);
  *(volatile U32*)(TXBUF_APLK_START+4) = TXBUF_APSTART;
  *(volatile U32*)(TXBUF_APLK_START+8) = TXBUF_APLK_START+16;

  //ampdu discripter1
                                                       //eof     sub_sof   buffer_length  buffer_size 
  *(volatile U32*)(TXBUF_APLK_START+16) = (0x1<<31) + (0x1<<30) + (0x1<<29) + (0x69<<12)  + (0x69<<0);
  *(volatile U32*)(TXBUF_APLK_START+20) = TXBUF_APSTART;
  *(volatile U32*)(TXBUF_APLK_START+24) = TXBUF_APLK_START+28;



  
  //////////////////////////////////////////////////
  // TX queue configure  imr
  //////////////////////////////////////////////////
  //int WDEVTXIMR_CONF[4]  = {WDEVTXIMR0_CONF_REG, WDEVTXIMR1_CONF_REG, WDEVTXIMR2_CONF_REG};
  int WDEVTXIMR_PLCP0[3] =  {WDEVTXIMR0_PLCP0_REG, WDEVTXIMR1_PLCP0_REG, WDEVTXIMR2_PLCP0_REG};
  int WDEVTXIMR_PLCP1[3] =  {WDEVTXIMR0_PLCP1_REG, WDEVTXIMR1_PLCP1_REG, WDEVTXIMR2_PLCP1_REG};
   
  for (i=0;i<=2;i++){
    //WRITE_PERI_REG(WDEVTXIMR_CONF[i], 0x00000000); // aifs = 0x4, backoff = 0x013
    WRITE_PERI_REG(WDEVTXIMR_PLCP0[i] , (TXBUF_LK_START&WDEV_TXQ6_LINK_ADDR   )); // txrate = 1.5Mbps, txlen = 069
    WRITE_PERI_REG(WDEVTXIMR_PLCP1[i] , (0x00002068                      )); // txrate = 1.5Mbps, txlen = 069

  }


  //////////////////////////////////////////////////
  // TX queue configure  Q
  //////////////////////////////////////////////////
  int WDEVTXQ_CONF[8]  = {WDEVTXQ0_CONF_REG, WDEVTXQ1_CONF_REG, WDEVTXQ2_CONF_REG, WDEVTXQ3_CONF_REG, WDEVTXQ4_CONF_REG, WDEVTXQ5_CONF_REG, WDEVTXQ6_CONF_REG, WDEVTXQ7_CONF_REG};
  int WDEVTXQ_PLCP0[8] =  {WDEVTXQ0_PLCP0_REG, WDEVTXQ1_PLCP0_REG, WDEVTXQ2_PLCP0_REG, WDEVTXQ3_PLCP0_REG, WDEVTXQ4_PLCP0_REG, WDEVTXQ5_PLCP0_REG, WDEVTXQ6_PLCP0_REG, WDEVTXQ7_PLCP0_REG};
  int WDEVTXQ_PLCP1[8] =  {WDEVTXQ0_PLCP1_REG, WDEVTXQ1_PLCP1_REG, WDEVTXQ2_PLCP1_REG, WDEVTXQ3_PLCP1_REG, WDEVTXQ4_PLCP1_REG, WDEVTXQ5_PLCP1_REG, WDEVTXQ6_PLCP1_REG, WDEVTXQ7_PLCP1_REG};
  int WDEVTXQ_VHTSIG1[8] =  {WDEVTXQ0_VHTSIG1_REG, WDEVTXQ1_VHTSIG1_REG, WDEVTXQ2_VHTSIG1_REG, WDEVTXQ3_VHTSIG1_REG, WDEVTXQ4_VHTSIG1_REG, WDEVTXQ5_VHTSIG1_REG, WDEVTXQ6_VHTSIG1_REG, WDEVTXQ7_VHTSIG1_REG};
  int WDEVTXQ_VHTSIG2[8] =  {WDEVTXQ0_VHTSIG2_REG, WDEVTXQ1_VHTSIG2_REG, WDEVTXQ2_VHTSIG2_REG, WDEVTXQ3_VHTSIG2_REG, WDEVTXQ4_VHTSIG2_REG, WDEVTXQ5_VHTSIG2_REG, WDEVTXQ6_VHTSIG2_REG, WDEVTXQ7_VHTSIG2_REG};
  int WDEVTXQ_HTSIG[8] =  {WDEVTXQ0_HTSIG_REG, WDEVTXQ1_HTSIG_REG, WDEVTXQ2_HTSIG_REG, WDEVTXQ3_HTSIG_REG, WDEVTXQ4_HTSIG_REG, WDEVTXQ5_HTSIG_REG, WDEVTXQ6_HTSIG_REG, WDEVTXQ7_HTSIG_REG};
  int WDEVTXOP1_Q_PLCP0[16] = {WDEVTXOP1_Q1_PLCP0_REG, WDEVTXOP1_Q1_PLCP0_REG, WDEVTXOP1_Q2_PLCP0_REG, WDEVTXOP1_Q3_PLCP0_REG, WDEVTXOP1_Q4_PLCP0_REG, WDEVTXOP1_Q5_PLCP0_REG, WDEVTXOP1_Q6_PLCP0_REG, WDEVTXOP1_Q7_PLCP0_REG, WDEVTXOP1_Q8_PLCP0_REG, WDEVTXOP1_Q9_PLCP0_REG, WDEVTXOP1_Q10_PLCP0_REG, WDEVTXOP1_Q11_PLCP0_REG, WDEVTXOP1_Q12_PLCP0_REG, WDEVTXOP1_Q13_PLCP0_REG, WDEVTXOP1_Q14_PLCP0_REG, WDEVTXOP1_Q15_PLCP0_REG};
  
  for (i=0;i<=3;i++){ // leagcy
    WRITE_PERI_REG(WDEVTXQ_CONF[i], 0x00000000); // aifs = 0x4, backoff = 0x013
    WRITE_PERI_REG(WDEVTXQ_PLCP0[i] , (TXBUF_LK_START&WDEV_TXQ6_LINK_ADDR                      )); // txrate = 11Mbps, txlen = 05d ,rts=1,ack=1
    WRITE_PERI_REG(WDEVTXQ_PLCP1[i] , (0x00009068                      )); // txrate = 11Mbps, txlen = 05d ,rts=1,ack=1
  }
  for (i=4;i<=5;i++){ // HT
    WRITE_PERI_REG(WDEVTXQ_CONF[i], 0x00000000); // aifs = 0x4, backoff = 0x013
    WRITE_PERI_REG(WDEVTXQ_PLCP0[i] , (TXBUF_APLK_START&WDEV_TXQ6_LINK_ADDR                      )); // txrate = 11Mbps, txlen = 0xd9 ,rts=1,ack=1
    WRITE_PERI_REG(WDEVTXQ_PLCP1[i] , (0x0200b069                      )); 
    WRITE_PERI_REG(WDEVTXQ_HTSIG[i] , (0x0800d980                      ));
  }





  for (i=6;i<=7;i++){ // VHT
    WRITE_PERI_REG(WDEVTXQ_CONF[i], 0x00000000); // aifs = 0x4, backoff = 0x013
    WRITE_PERI_REG(WDEVTXQ_PLCP0[i] , (TXBUF_LK_START&WDEV_TXQ6_LINK_ADDR                      )); // txrate = 11Mbps, txlen = 0xd9 ,rts=1,ack=1    
    SET_PERI_REG_BITS(WDEVTXQ_PLCP1[i], WDEV_TXQ0_SIGMODE, 3, WDEV_TXQ0_SIGMODE_S);
    WRITE_PERI_REG(WDEVTXQ_VHTSIG1[i], 0);
    WRITE_PERI_REG(WDEVTXQ_VHTSIG2[i], (0x68>>2)<<2); // len = 0x68
  }

  for (i=1;i<=15;i++){
    WRITE_PERI_REG(WDEVTXOP1_Q_PLCP0[i], (TXBUF_LK_START&WDEV_TXOP1_Q12_LINK_ADDR)|(0x65<<WDEV_TXOP1_Q12_LEN_S));
  }

  
  // mac watch dog
  WRITE_PERI_REG(WDEVHUNGRECOVER_REG, 0x8FFF8FFF);
  WRITE_PERI_REG(WDEVRX_DUMP0_LIM_REG,0xFFFF0000);


}

void fill_tx_packet(int *packet, int packet_len)
{
  int j;
  U32 init_addr;
  init_addr = TXBUF_START;
  for (j=0; j< packet_len; j=j+1) {
    *(volatile U32*)(init_addr + j*4)=(packet[4*j+3]<<24) + (packet[4*j+2]<<16) + (packet[4*j+1]<<8) + packet[4*j];
  }  

  *(volatile U32*)(TXBUF_LK_START) = (0x1<<31) + (0x1<<30) + (0x0<<29) + (packet_len<<12)  + ((packet_len+4)<<0);
}

void tx_queue_init(void)
{
  //--------------------------------------------
  //-- memory Initialisation
  //--------------------------------------------
  long long    packet[0x68] = {0x08,0x01,0x5a,0xa5,0x00,0x01,0x02,0x03,0x04,0x05,0x10,0x11,0x12,0x13,0x14,0x15,
                               0x00,0x01,0x02,0x03,0x04,0x05,0x00,0x00,0x04,0x05,0x06,0x07,0x08,0x09,0x0a,0x0b,
			       0x0c,0x0d,0x0e,0x0f,0x10,0x11,0x12,0x13,0x14,0x15,0x16,0x17,0x18,0x19,0x1a,0x1b,
			       0x1c,0x1d,0x1e,0x1f,0x20,0x21,0x22,0x23,0x24,0x25,0x26,0x27,0x28,0x29,0x30,0x31,
			       0x32,0x33,0x34,0x35,0x36,0x37,0x38,0x39,0x3a,0x3b,0x3c,0x3d,0x3e,0x3f,0x40,0x41,
			       0x42,0x43,0x44,0x45,0x46,0x47,0x48,0x49,0x4a,0x4b,0x4c,0x4d,0x4e,0x4f,0x50,0x51,
			       0x52,0x53,0x54,0x55,0x56}; 

  int j;
  U32 init_addr;
  init_addr = TXBUF_START;

  for (j=0; j< 0x1a; j=j+1) {
    *(volatile U8*)(init_addr + j) = packet[j];
    //*(volatile U32*)(init_addr + j*4)=(packet[4*j+3]<<24) + (packet[4*j+2]<<16) + (packet[4*j+1]<<8) + packet[4*j];
  }  

  for (j=0;j<0x80;j=j+1) {
    *(volatile U32*)(init_addr + 0x068 + j*4)= j* 0x01010101;
  }

  *(volatile U32*)(TXBUF_APSTART)= (0x1<<12) + 0x65;
}

void test_tx_sim(int *queue_index )
{

  SET_PERI_REG_MASK(WDEV_INT_CLR_MAC_REG, WDEV_TXEND_INT_ENA);
  if (queue_index[8] == 0) {
   if (queue_index[0])  SET_PERI_REG_MASK(WDEVTXIMR0_PLCP0_REG, WDEV_TXIMR0_ENA|WDEV_TXIMR0_VALID);
   if (queue_index[1])  SET_PERI_REG_MASK(WDEVTXIMR1_PLCP0_REG, WDEV_TXIMR1_ENA|WDEV_TXIMR1_VALID);
   if (queue_index[2])  SET_PERI_REG_MASK(WDEVTXIMR2_PLCP0_REG, WDEV_TXIMR2_ENA|WDEV_TXIMR2_VALID);
  }
  
  if (queue_index[8] == 1) {
    if (queue_index[0]) SET_PERI_REG_MASK(WDEVTXQ0_PLCP0_REG, WDEV_TXQ0_ENA|WDEV_TXQ0_VALID);
    if (queue_index[1]) SET_PERI_REG_MASK(WDEVTXQ1_PLCP0_REG, WDEV_TXQ1_ENA|WDEV_TXQ1_VALID);
    if (queue_index[2]) SET_PERI_REG_MASK(WDEVTXQ2_PLCP0_REG, WDEV_TXQ2_ENA|WDEV_TXQ2_VALID);
    if (queue_index[3]) SET_PERI_REG_MASK(WDEVTXQ3_PLCP0_REG, WDEV_TXQ3_ENA|WDEV_TXQ3_VALID);
    if (queue_index[4]) SET_PERI_REG_MASK(WDEVTXQ4_PLCP0_REG, WDEV_TXQ4_ENA|WDEV_TXQ4_VALID);
    if (queue_index[5]) SET_PERI_REG_MASK(WDEVTXQ5_PLCP0_REG, WDEV_TXQ5_ENA|WDEV_TXQ5_VALID);
    if (queue_index[6]) SET_PERI_REG_MASK(WDEVTXQ6_PLCP0_REG, WDEV_TXQ6_ENA|WDEV_TXQ6_VALID);
    if (queue_index[7]) SET_PERI_REG_MASK(WDEVTXQ7_PLCP0_REG, WDEV_TXQ7_ENA|WDEV_TXQ7_VALID);
  }

#if 0  //test bt stop bb
  delay_us(30);
  *(volatile U32*)(WDEVGPO_REG)      = *(volatile U32*) (WDEVGPO_REG) & 0xfffdffff | (0x1<<17);  //mac_stop_bb
  *(volatile U32*)(WDEVGPO_REG)      = *(volatile U32*) (WDEVGPO_REG) & 0xfffdffff | (0x0<<17);  //mac_stop_bb
#endif
#if 0  //test mac reset bb
  delay_us(30);
  *(volatile U32*)(WDEVGPO_REG)      = *(volatile U32*) (WDEVGPO_REG) & 0xfffffffe | (0x1<<0);  //mac_rst_bb
  *(volatile U32*)(WDEVGPO_REG)      = *(volatile U32*) (WDEVGPO_REG) & 0xfffffffe | (0x0<<0);  //mac_rst_bb
#endif
  
  while(GET_PERI_REG_MASK(WDEV_INT_ST_MAC_REG, WDEV_TXEND_INT_ENA) == 0){
  }; 
  Check ((WDEVTXPMD_REG), 0x00000000, WDEV_TXEND_STATE);
  SET_PERI_REG_MASK(WDEV_INT_CLR_MAC_REG, WDEV_TXEND_INT_ENA);
/*   printinfo("WDEVTXENA_ST_REG:\n", READ_PERI_REG(WDEVTXENA_ST_REG)); */
/*   if (queue_index[8] == 0) { */
/*     if (queue_index[0] == 1) CHECK_LINE(READ_PERI_REG(WDEVTXENA_ST_REG)&WDEV_TXIMR0_ENA_ST, WDEV_TXIMR0_ENA_ST); */
/*     if (queue_index[1] == 1) CHECK_LINE(READ_PERI_REG(WDEVTXENA_ST_REG)&WDEV_TXIMR1_ENA_ST, WDEV_TXIMR1_ENA_ST); */
/*     if (queue_index[2] == 1) CHECK_LINE(READ_PERI_REG(WDEVTXENA_ST_REG)&WDEV_TXIMR2_ENA_ST, WDEV_TXIMR2_ENA_ST); */
/*   } */
/*   else if (queue_index[8] == 1){ */
/*     if (queue_index[0] == 1) CHECK_LINE(READ_PERI_REG(WDEVTXENA_ST_REG)&WDEV_TXQ0_ENA_ST, WDEV_TXQ0_ENA_ST); */
/*     if (queue_index[1] == 1) CHECK_LINE(READ_PERI_REG(WDEVTXENA_ST_REG)&WDEV_TXQ1_ENA_ST, WDEV_TXQ1_ENA_ST); */
/*     if (queue_index[2] == 1) CHECK_LINE(READ_PERI_REG(WDEVTXENA_ST_REG)&WDEV_TXQ2_ENA_ST, WDEV_TXQ2_ENA_ST); */
/*     if (queue_index[3] == 1) CHECK_LINE(READ_PERI_REG(WDEVTXENA_ST_REG)&WDEV_TXQ3_ENA_ST, WDEV_TXQ3_ENA_ST); */
/*     if (queue_index[4] == 1) CHECK_LINE(READ_PERI_REG(WDEVTXENA_ST_REG)&WDEV_TXQ4_ENA_ST, WDEV_TXQ4_ENA_ST); */
/*     if (queue_index[5] == 1) CHECK_LINE(READ_PERI_REG(WDEVTXENA_ST_REG)&WDEV_TXQ5_ENA_ST, WDEV_TXQ5_ENA_ST); */
/*     if (queue_index[6] == 1) CHECK_LINE(READ_PERI_REG(WDEVTXENA_ST_REG)&WDEV_TXQ6_ENA_ST, WDEV_TXQ6_ENA_ST); */
/*     if (queue_index[7] == 1) CHECK_LINE(READ_PERI_REG(WDEVTXENA_ST_REG)&WDEV_TXQ7_ENA_ST, WDEV_TXQ7_ENA_ST); */
/*   } */
  WRITE_PERI_REG(WDEVTXENA_ST_CLR_REG, READ_PERI_REG(WDEVTXENA_ST_REG));
  queue_index[0] = 0;
  queue_index[1] = 0;
  queue_index[2] = 0;
  queue_index[3] = 0;
  queue_index[4] = 0;
  queue_index[5] = 0;
  queue_index[6] = 0;
  queue_index[7] = 0;
  queue_index[8] = 0;
}

void clear_txerrstate()
{
  *(volatile U32*)(WDEVTXSTATE_REG) = 0x0;
}
void sim_check()
{
  *(volatile U32*)(WDEVSIM_FINISH_REG) = 0x1;
}
void test_tx_sim_bb(int queue_index)
{
  *(volatile U32*)(WDEVTXQ0_PLCP0_REG) = *(volatile U32*)(WDEVTXQ0_PLCP0_REG) & 0x3fffffff | (0x3 << 30);
  while(((*(volatile U32*)(WDEV_INT_ST_MAC_REG)) & WDEV_TXEND_INT_ENA) == 0){};
  Check ((WDEVTXPMD_REG), 0x00000000, 0xFF0000);
  *(volatile U32*)(WDEV_INT_CLR_MAC_REG) = 0x3;
}

void key_cache_wr(unsigned int *key_word,int entry_num){
  int i;
  unsigned int key_cache_addr;
  unsigned int key_data;
  for (i=0;i<10;i++) {
    key_cache_addr = REG_WDEV_BASE + 0x1400 + entry_num*0x28 + i;
    key_data = key_word[i];
    WRITE_PERI_REG(key_cache_addr,key_data);
  }
}

void key_cache_init(){
  int i;
  unsigned int wapi_key[10] = {0x03020100,0x700504,0xccddeeff,0x8899aabb,0x44556677,0x00112233,0xcddeeff0,0x899aabbc,0x45566778,0x01122334};
  
  for (i=0;i<25;i++){
    key_cache_wr(wapi_key,i);
  }

  WRITE_PERI_REG(WDEVSEC_CONF3_REG,0xFFFFFFFF);                  //key cache entry valid ind
}


void rx_sim_dumpfile_enable()
{
  *(volatile U32*)(0x60000870)      = *(volatile U32*) (0x60000870) & 0xffffffcf | (0x0<<4);  //set io_mux to enable GPIO0 out
  *(volatile U32*)(0x60000870)      = *(volatile U32*) (0x60000874) & 0xffffffcf | (0x0<<4);  //set io_mux to enable GPIO1 out
  *(volatile U32*)(0x60000870)      = *(volatile U32*) (0x60000878) & 0xffffffcf | (0x0<<4);  //set io_mux to enable GPIO2 out
  *(volatile U32*)(0x60000870)      = *(volatile U32*) (0x6000087c) & 0xffffffcf | (0x0<<4);  //set io_mux to enable GPIO3 out
  *(volatile U32*)(0x60000870)      = *(volatile U32*) (0x60000880) & 0xffffffcf | (0x0<<4);  //set io_mux to enable GPIO4 out
  *(volatile U32*)(0x60000870)      = *(volatile U32*) (0x60000884) & 0xffffffcf | (0x0<<4);  //set io_mux to enable GPIO5 out
  *(volatile U32*)(0x60000300)      = *(volatile U32*) (0x60000300) & 0xfffffffe | (0x1);     //set GPIO0 : enable dump rx data in bench
  *(volatile U32*)(0x60000300)      = *(volatile U32*) (0x60000300) & 0xffffffef | (0x1<<4);  //set GPIO4 : reset ptr for dumping rx data in bench
}

void test_rx_start(int dumpfile_index)
{
  int input_sel;
  input_sel = (dumpfile_index>>0)&0xf;
  //begin rx test
    
  *(volatile U32*)(RX_CTRL_ADDR)      = *(volatile U32*) (RX_CTRL_ADDR) & 0xffffffef | (0x1<<4);  //set GPIO4 : reset ptr for dumping rx data in bench
  *(volatile U32*)(RX_CTRL_ADDR)      = *(volatile U32*) (RX_CTRL_ADDR) & 0xffffffd1 | (0x6<<1);  //set GPIO3~1 : to control rx data source
  *(volatile U32*)(RX_CTRL_ADDR)      = *(volatile U32*) (RX_CTRL_ADDR) & 0xffffffd1 | ((input_sel & 0x7)<<1) | (((input_sel>>3) & 0x1)<<5);  //set GPIO3~1 and GPIO5: to control rx data source
  *(volatile U32*)(RX_CTRL_ADDR)      = *(volatile U32*) (RX_CTRL_ADDR) & 0xffffffef | (0x0<<4);  //set GPIO4 : release ptr for dumping rx data in bench

}
unsigned int test_rx_end()
{
  while(GET_PERI_REG_MASK(WDEV_INT_ST_MAC_REG, WDEV_RXEND_INT_ENA) != WDEV_RXEND_INT_ENA){}
  SET_PERI_REG_MASK(WDEV_INT_CLR_MAC_REG, WDEV_RXEND_INT_ENA);
  return GET_PERI_REG_BITS(WDEVRXPMD_REG, WDEV_RXEND_STATE, WDEV_RXEND_STATE_S);
}

unsigned int test_rx_sim(int dumpfile_index)
{
  int temp,i;
  int input_sel, dur_time, check_disable, rx_pkg_num, delay_disable, init_rand_gain;
  int error_code, init_gain;
  unsigned int success = 0;
  unsigned int timeout = 0;

  input_sel = (dumpfile_index>>0)&0xf;
  dur_time = (dumpfile_index>>4)&0x7f;
  rx_pkg_num = (dumpfile_index>>12)&0xf; //actually total (rx_pkg_num+1)
  check_disable = (dumpfile_index>>16)&0x1;
  delay_disable = (dumpfile_index>>19)&0x1;
  error_code = (dumpfile_index>>20)&0xff;
  init_rand_gain = (dumpfile_index>>28)&0x1;

  init_gain = rand()%86;

  //set packet's duration time for timeout(unit: us)
  if(dur_time==0)dur_time=(1600*8+200);  //the most length of pocket is 1.6k
  else dur_time = dur_time*100;

  if(~delay_disable){delay_us(10);}

  //check if rx is already wrongly triggered
  if(((READ_PERI_REG(WDEV_INT_ST_MAC_REG)) & WDEV_RXSTART_INT_ENA) != 0){  //rx_start occur
     if(((READ_PERI_REG(WDEV_INT_ST_MAC_REG)) & WDEV_RXEND_INT_ENA) == 0){  //rx_end hasn't occur
        //mac force reset
	temp = (READ_PERI_REG(WDEVBBRXHUNG_REG));
	READ_PERI_REG(WDEVBBRXHUNG_REG) = (READ_PERI_REG(WDEVBBRXHUNG_REG)) & 0x7ffff000 | (0x1<<31) | 0x0;  //panic_reset_en, panic_timer
	while(((READ_PERI_REG(WDEV_INT_ST_MAC_REG)) & 0x4) == 0){};
	READ_PERI_REG(WDEVBBRXHUNG_REG) = temp;
     }
     //clear former rx int first(for sim)
     READ_PERI_REG(WDEV_INT_CLR_MAC_REG) = 0xc;
  }
  //begin rx test
  test_rx_start(input_sel);
  delay_us(66);
  SET_PERI_REG_MASK(WDEVRXMODE_REG, WDEV_RXBUFDSCR_RELOAD); 
  if(init_rand_gain){                   
      //READ_PERI_REG(AGCPWR_CTRL7_REG) = READ_PERI_REG(AGCPWR_CTRL7_REG) & 0x007fffff | (init_gain<<24) | (1<<23);  //force_gain */
      //READ_PERI_REG(AGCPWR_CTRL7_REG) = READ_PERI_REG(AGCPWR_CTRL7_REG) & 0xff7fffff | (0<<23);  //force_gain */
  }

  for(i=0;i<(rx_pkg_num+1);i++)
  {
     temp = READ_PERI_REG(WDEVTIME_REG);
     while(((READ_PERI_REG(WDEV_INT_ST_MAC_REG)) & WDEV_RXEND_INT_ENA ) == 0)
     {
        if((READ_PERI_REG(WDEVTIME_REG))-temp>dur_time){
           timeout = 1;
           if(check_disable==0){
              fail("Check Failed\n");
           }
           break;
        }
     };

     if(timeout==0){
        if(check_disable==0){
           Check ((WDEVRXPMD_REG), error_code, 0xff);
           //if not fail
           success = 1;
        }else if(((READ_PERI_REG(WDEVRXPMD_REG)) & 0xff ) == 0){
           success = 1;
        }
     }

     READ_PERI_REG(WDEV_INT_CLR_MAC_REG) = WDEV_RXSTART_INT_ENA|WDEV_RXEND_INT_ENA;

     //if(success)break;  //for rx restart sim end
  }

  READ_PERI_REG(RX_CTRL_ADDR)      = READ_PERI_REG (RX_CTRL_ADDR) & 0xffffffef | (0x1<<4);  //set GPIO4 : reset ptr for dumping rx data in bench

  return success;

}

void test_rxampdu_sim(int dumpfile_index)
{
  int temp;

  //check if rx is already wrongly triggered
  if(((READ_PERI_REG(WDEV_INT_ST_MAC_REG)) & 0x8) != 0){  //rx_start occur
     if(((READ_PERI_REG(WDEV_INT_ST_MAC_REG)) & 0x4) == 0){  //rx_end hasn't occur
        //mac force reset
	temp = (READ_PERI_REG(WDEVBBRXHUNG_REG));
	READ_PERI_REG(WDEVBBRXHUNG_REG) = (READ_PERI_REG(WDEVBBRXHUNG_REG)) & 0x7ffff000 | (0x1<<31) | 0x0;  //panic_reset_en, panic_timer
	while(((READ_PERI_REG(WDEV_INT_ST_MAC_REG)) & 0x4) == 0){};
	READ_PERI_REG(WDEVBBRXHUNG_REG) = temp;
     }
     //clear former rx int first(for sim)
     READ_PERI_REG(WDEV_INT_CLR_MAC_REG) = 0xc;
  }

  //begin rx tests
  test_rx_start(dumpfile_index&0xf);

  while(((READ_PERI_REG(WDEV_INT_ST_MAC_REG)) & 0x4 ) == 0){};
  // Check ((WDEVRXPMD_REG), 0x00000000, 0xff);
  READ_PERI_REG(WDEV_INT_CLR_MAC_REG) = 0xc;

  READ_PERI_REG(RX_CTRL_ADDR)      = READ_PERI_REG (RX_CTRL_ADDR) & 0xffffffef | (0x1<<4);  //set GPIO4 : reset ptr for dumping rx data in bench
}


/* int get_rx_sim_result(int dumpfile_index, int tx_queue_num, int check_en) */
/* { */
/*   int temp; */
/*   int rx_result; */
/*   int i = 0; */
/*   int timeout = 0; */
/*   int rate, length, rate_mbps, max_us; */

/*   //check if rx is already wrongly triggered */
/*   if(((READ_PERI_REG(WDEV_INT_ST_MAC_REG)) & 0x8) != 0){  //rx_start occur */
/*      if(((READ_PERI_REG(WDEV_INT_ST_MAC_REG)) & 0x4) == 0){  //rx_end hasn't occur */
/*         //mac force reset */
/* 	temp = (READ_PERI_REG(WDEVBBRXHUNG_REG)); */
/* 	READ_PERI_REG(WDEVBBRXHUNG_REG) = (READ_PERI_REG(WDEVBBRXHUNG_REG)) & 0x7ffff000 | (0x1<<31) | 0x0;  //panic_reset_en, panic_timer */
/* 	while(((READ_PERI_REG(WDEV_INT_ST_MAC_REG)) & 0x4) == 0){}; */
/* 	READ_PERI_REG(WDEVBBRXHUNG_REG) = temp; */
/*      } */
/*      //clear former rx int first(for sim) */
/*      READ_PERI_REG(WDEV_INT_CLR_MAC_REG) = 0xc; */
/*   } */

/*   //begin rx test */
/*   READ_PERI_REG(RX_CTRL_ADDR)      = READ_PERI_REG (RX_CTRL_ADDR) & 0xffffffef | (0x1<<4);  //set GPIO4 : reset ptr for dumping rx data in bench */
/*   READ_PERI_REG(RX_CTRL_ADDR)      = READ_PERI_REG (RX_CTRL_ADDR) & 0xffffffd1 | (0x6<<1);  //set GPIO3~1 : to control rx data source */
/*   READ_PERI_REG(RX_CTRL_ADDR)      = READ_PERI_REG (RX_CTRL_ADDR) & 0xffffffef | (0x0<<4);  //set GPIO4 : release ptr for dumping rx data in bench */
/*   READ_PERI_REG(RX_CTRL_ADDR)      = READ_PERI_REG (RX_CTRL_ADDR) & 0xffffffd1 | ((dumpfile_index & 0x7)<<1) | ((dumpfile_index & 0x8)<<2);  //set GPIO3~1 : to control rx data source */

/*   //get frame's information for time calculation in tx-rx loop sim */
/*   if(tx_queue_num==1){temp = (READ_PERI_REG(WDEVTXQ0_PLCP0_REG));} */
/*   else if(tx_queue_num==2){temp = (READ_PERI_REG(WDEVTXIMR0_PLCP0_REG));} */
/*   rate = (temp>>16) & 0xf; */
/*   length = temp & 0xfff; */
/*   switch(rate){ */
/*      case 0: rate_mbps = 1; break; */
/*      case 1: rate_mbps = 2; break; */
/*      case 2: rate_mbps = 5; break; */
/*      case 3: rate_mbps = 11; break; */
/*      case 4: rate_mbps = 1; break; */
/*      case 5: rate_mbps = 2; break; */
/*      case 6: rate_mbps = 5; break; */
/*      case 7: rate_mbps = 11; break; */
/*      case 8: rate_mbps = 48; break; */
/*      case 9: rate_mbps = 24; break; */
/*      case 10: rate_mbps = 12; break; */
/*      case 11: rate_mbps = 6; break; */
/*      case 12: rate_mbps = 54; break; */
/*      case 13: rate_mbps = 36; break; */
/*      case 14: rate_mbps = 18; break; */
/*      case 15: rate_mbps = 9; break; */
/*      default: rate_mbps = 1; break; */
/*   } */
/*   max_us = length*8/rate_mbps + 300; */

/*   //wait rx_end or timeout */
/*   while(((READ_PERI_REG(WDEV_INT_ST_MAC_REG)) & 0x4) == 0)  //check rx end */
/*   { */
/*      i++; */
/*      if(dumpfile_index==7){if(i>max_us*2){timeout = 1;break;}}  //each read period is 0.55us(according psel of reg WDEV_INT_ST_MAC_REG) */
/*      //elsif(i>34000){timeout = 1;break;}  //2048bytes of 1Mbps is ok */
/*      else if(i>17000){timeout = 1;break;}  //1024bytes of 1Mbps is ok */
/*   } */

/*   if(timeout){rx_result = 0xffffffff;} */
/*   else{rx_result = *(volatile unsigned int*)(WDEVRXPMD_REG);} */

/*   if(check_en) */
/*   { */
/*      if(timeout){fail("Check Failed\n");} */
/*      else{Check ((WDEVRXPMD_REG), 0x00000000, 0xff);} */
/*   } */
/*   READ_PERI_REG(WDEV_INT_CLR_MAC_REG) = 0xc; */

/*   READ_PERI_REG(RX_CTRL_ADDR)      = READ_PERI_REG (RX_CTRL_ADDR) & 0xffffffef | (0x1<<4);  //set GPIO4 : reset ptr for dumping rx data in bench */

/*   return rx_result; */
/* } */

void mac_tx_sim(int rate,int length,int gi,int ht_bandwidth,int dup, int vht1, int vht2)
{

  //   rate = 'h0x , 11b/g
  //   rate = 'h1x , 11lr
  //   rate = 'h1xx , 11n
  //   rate = 'h200, vht
  // vhtSIGA = {vht2[1:0],vht1[31:0]};
  // vhtSIGB = vht2[24:2]
  //  length : Byte

   //discripter  
   int block_num;
   int i;
   int sig_mode;
   int legcy_rate;
   int legcy_len;
   block_num = (length-1)/0x200;
   for (i=0;i<block_num;i=i+1) {
                                                                     //eof     sub_sof   buffer_length  buffer_size 
     READ_PERI_REG(TXBUF_LK_START + 0x0 + i*0xC) = (0x1<<31) + (0x0<<30) + (0x0<<29) + (0x200<<12)  + 0x200;
     READ_PERI_REG(TXBUF_LK_START + 0x4 + i*0xC) = TXBUF_START;
     READ_PERI_REG(TXBUF_LK_START + 0x8 + i*0xC) = (TXBUF_LK_START + 0xC + i*0xc);
   }

     READ_PERI_REG(TXBUF_LK_START + 0x0 + block_num*0xC) = (0x1<<31) + (0x1<<30) + (0x0<<29) + (((length-1)%0x200 +1)<<12)  + (length%0x200);
     READ_PERI_REG(TXBUF_LK_START + 0x4 + block_num*0xC) = TXBUF_START;
     READ_PERI_REG(TXBUF_LK_START + 0x8 + block_num*0xC) = TXBUF_LK_START + 0xC;
 


  //mem initial
  tx_queue_init();

  //config q
  if (rate >= 0x200) {
    legcy_rate = 0xb;
    sig_mode = 0x3;
    legcy_len = 0x44;
  }
  else if (rate >= 0x100) { // 11n
    legcy_rate = 0xb;
    sig_mode = 0x1;
    legcy_len = 0x44;
  }
  else {              // 11b/g/lr
    legcy_rate = rate;
    sig_mode = 0x0;
    legcy_len = length;
  }
  SET_PERI_REG_BITS(WDEVTXQ0_CONF_REG, WDEV_TXQ6_AIFS, 0x0, WDEV_TXQ6_AIFS_S);// aifs,backoff
  SET_PERI_REG_BITS(WDEVTXQ0_CONF_REG, WDEV_TXQ6_BACKOFF, 0x0, WDEV_TXQ6_BACKOFF_S);// aifs,backoff
  //WRITE_PERI_REG(WDEVTXQ0_PLCP1_REG , (sig_mode<<24) + (legcy_rate<<12)+legcy_len); //sigmode,kid,rate,length
  SET_PERI_REG_BITS(WDEVTXQ0_PLCP1_REG, WDEV_TXQ0_SIGMODE , sig_mode, WDEV_TXQ0_SIGMODE_S);
  SET_PERI_REG_BITS(WDEVTXQ0_PLCP1_REG, WDEV_TXQ0_RATE ,legcy_rate , WDEV_TXQ0_RATE_S);
  SET_PERI_REG_BITS(WDEVTXQ0_PLCP1_REG, WDEV_TXQ0_LENGTH ,legcy_len , WDEV_TXQ0_LENGTH_S);
  WRITE_PERI_REG(WDEVTXQ0_HTSIG_REG , (gi<<30)+(length<<8)+(ht_bandwidth<<7)+(rate&0x7f));
  WRITE_PERI_REG(WDEVTXQ0_VHTSIG1_REG, vht1);
  WRITE_PERI_REG(WDEVTXQ0_VHTSIG2_REG, vht2);
  SET_PERI_REG_BITS(WDEVTXQ0_PLCP1_REG, WDEV_TXQ7_NONHTDUP, dup, WDEV_TXQ7_NONHTDUP_S); // 1: dup40M, 2: dup80M
  int tx_q_index[9] = {1,0,0,0,0,0,0,0,1};
  test_tx_sim(tx_q_index);
}


void test_dump()
{
   SET_PERI_REG_BITS( SENSITIVE_PMS_OCCUPY_1_REG, SENSITIVE_PMS_OCCUPY_MAC_DUMP, 0xf, SENSITIVE_PMS_OCCUPY_MAC_DUMP_S );
   SET_PERI_REG_BITS(WDEVOPTIONS_REG, WDEV_SCHCLK_EN, 1, WDEV_SCHCLK_EN_S);
   SET_PERI_REG_BITS(WDEVADCDUMP0_REG, WDEV_ADCDUMP_SIZE, 0x100, WDEV_ADCDUMP_SIZE_S);
   SET_PERI_REG_BITS(WDEVADCDUMP0_REG, 1, 1, WDEV_ADCDUMP_ENA_S);
   delay_us(50);
   SET_PERI_REG_BITS(WDEVADCDUMP0_REG, 1, 1, WDEV_ADCDUMP_START_S);
   delay_us(150);
   SET_PERI_REG_BITS(WDEVADCDUMP0_REG, 1, 0, WDEV_ADCDUMP_START_S);
   SET_PERI_REG_BITS(WDEVADCDUMP0_REG, 1, 0, WDEV_ADCDUMP_ENA_S);
}


/*
void rx_dump_sim(int chip_rx, int adc_mult, int package_num, int rx_period_us)
{
  int temp;
  int i=0, j=0;
  int dumpfile_index = 6;

  //adc
  if(chip_rx){
     READ_PERI_REG(apb_bb_offset + BB_ANALOG_CTRL3) = (READ_PERI_REG(apb_bb_offset + BB_ANALOG_CTRL3)) & 0xfffc0000 | (0x40<<10) | (0x1<<9) | (0x0<<6) | (adc_mult & 0x3f);  //zero point, c2dis, shl, mult(8b->9b)
  } else {
     READ_PERI_REG(apb_bb_offset + BB_ANALOG_CTRL3) = (READ_PERI_REG(apb_bb_offset + BB_ANALOG_CTRL3)) & 0xfffc0000 | (0x80<<10) | (0x1<<9) | (0x0<<6) | (adc_mult & 0x3f);  //zero point, c2dis, shl, mult(8b->9b)
  }

  //check if rx is already wrongly triggered
  if(((READ_PERI_REG(WDEV_INT_ST_MAC_REG)) & 0x8) != 0){  //rx_start occur
     if(((READ_PERI_REG(WDEV_INT_ST_MAC_REG)) & 0x4) == 0){  //rx_end hasn't occur
        //mac force reset
	temp = (READ_PERI_REG(WDEVBBRXHUNG_REG));
	READ_PERI_REG(WDEVBBRXHUNG_REG) = (READ_PERI_REG(WDEVBBRXHUNG_REG)) & 0x7ffff000 | (0x1<<31) | 0x0;  //panic_reset_en, panic_timer
	while(((READ_PERI_REG(WDEV_INT_ST_MAC_REG)) & 0x4) == 0){};
	READ_PERI_REG(WDEVBBRXHUNG_REG) = temp;
     }
     //clear former rx int first(for sim)
     READ_PERI_REG(WDEV_INT_CLR_MAC_REG) = 0xc;
  }

  //begin rx test
  READ_PERI_REG(RX_CTRL_ADDR)      = READ_PERI_REG (RX_CTRL_ADDR) & 0xffffffef | (0x1<<4);  //set GPIO4 : reset ptr for dumping rx data in bench
  READ_PERI_REG(RX_CTRL_ADDR)      = READ_PERI_REG (RX_CTRL_ADDR) & 0xfffffff1 | (0x6<<1);  //set GPIO3~1 : to control rx data source
  READ_PERI_REG(RX_CTRL_ADDR)      = READ_PERI_REG (RX_CTRL_ADDR) & 0xffffffef | (0x0<<4);  //set GPIO4 : release ptr for dumping rx data in bench
  READ_PERI_REG(RX_CTRL_ADDR)      = READ_PERI_REG (RX_CTRL_ADDR) & 0xfffffff1 | (0x6<<1);  //set GPIO3~1 : to control rx data source

  //wait rx_end or timeout
  for(i=0; i<package_num; i++) {
    while(((READ_PERI_REG(WDEV_INT_ST_MAC_REG)) & 0x4) == 0)  //check rx end
    {
       j++;
       if(j>rx_period_us*8){break;}
    }
    READ_PERI_REG(WDEV_INT_CLR_MAC_REG) = 0xc;
  }

  READ_PERI_REG(RX_CTRL_ADDR)      = READ_PERI_REG (RX_CTRL_ADDR) & 0xffffffef | (0x1<<4);  //set GPIO4 : reset ptr for dumping rx data in bench
}
*/


#endif




