#include <xtensa/hal.h>
#include <xtensa/config/core.h>
#include <xtensa/config/system.h>

//scl low period config
void scl_lp_config(unsigned int addr,unsigned int value)
{
  *(volatile U32*)(addr)=value;  
}

void ctr_config(unsigned int addr,unsigned int value)
{
  *(volatile U32*)(addr+4)=value;
//(rx_lsb_first|tx_lsb_first|trans_start|ms_mode|master_rw|ack|scl_force_out|sda_force_out)  
}
//txfifo cnt 
unsigned int txfifo_cnt(unsigned int addr)
{
  unsigned int temp;
  temp=((*(volatile U32*)(addr+4*2))>>16)&0xff;
  return temp;
}

//timeout protect
void timeout_config(unsigned int addr,unsigned int value)
{
  *(volatile U32*)(addr+4*3)=value;
}
//slave addr config when used as a slave
void slave_addr_config(unsigned int addr,unsigned int value)
{
  *(volatile U32*)(addr+4*4)=value;//(addr_10bit_en[31]|slave_addr_reg[14:0])
}
//fifo config
void fifo_config(unsigned int addr, unsigned int value)
{
  *(volatile U32*)(addr+4*6)=value;
//(rx_tout_thrhd[19:16]|rx_tout_en[14]|tx_fifo_rst[13]|rx_fifo_rst[12]|txfifo_empty_thrhd[10:4]|rxfifo_full_thrhd[3:0]])
}
//fifo write data
void fifo_wr(unsigned int addr,unsigned int value)
{
  *(volatile U32*)(addr+4*7)=value;
}
//fifo read data
unsigned int fifo_rd(unsigned int addr)
{
   unsigned int temp;
   temp=(*(volatile U32*)(addr+4*7));
   return temp;
}
//read i2c interrupt
unsigned int i2c_int_raw(unsigned int addr)
{
 unsigned int temp;
 temp=(*(volatile U32*)(addr+4*8));
 return temp;
 //(time_out_int_raw|trans_complete_int_raw|master_trans_comp_int_raw|arbitration_lost_int_raw|slave_trans_comp_int_raw|rxfifo_tout_int_raw|rxfifo_ovf_int_raw|txfifo_empty_int_raw|rxfifo_full_int_raw)
}
//i2c int clr
void i2c_int_clr(unsigned int addr, unsigned int value)
{
  *(volatile U32*)(addr+4*9)=value;
}
//i2c int enable
void i2c_int_en(unsigned int addr,unsigned int value)
{
  *(volatile U32*)(addr+4*10)=value;
}
//i2c sda duty
void i2c_sda_config(unsigned int addr,unsigned int value)
{
  *(volatile U32*)(addr+4*12)=value;
}
//scl high period
void scl_hp_config(unsigned int addr, unsigned int value)
{
  *(volatile U32*)(addr+4*14)=value;
}
//scl start period
void scl_startp_config(unsigned int addr, unsigned int value)
{
  *(volatile U32*)(addr+4*16)=value;
}
//scl stop period
void scl_stopp_config(unsigned int addr, unsigned int value)
{
  *(volatile U32*)(addr+4*17)=value;
}
//i2c command config
int i2c_cmd(unsigned int addr, unsigned int number,unsigned int op_code, unsigned int ack_value, unsigned int ack_exp,unsigned int ack_check_en,unsigned int byte_num)
{
  *(volatile U32*)(addr+4*18+4*number)=((op_code<<11)|(ack_value<<10)|(ack_exp<<9)|(ack_check_en<<8)|byte_num);
//(op_code[13:11]|ack_value[10]|ack_exp[9]|ack_check_en[8]|byte_num[7:0])
//op_code 0 rstart
//        1 write
//        2 read
//        3 stop
    return ((op_code<<11)|(ack_value<<10)|(ack_exp<<9)|(ack_check_en<<8)|byte_num);
}
//i2c command done
void i2c_cmd_done(unsigned int addr, unsigned int number)
{
  while(((*(volatile U32*)(addr+4*18+4*number))&0x80000000)==0);
}

//*************************************************
// case1 master(1 transfer) send n payload to slave
//*************************************************
void mws_7bit(unsigned int master_addr,unsigned int slave_addr1,unsigned int s7bit_addr,unsigned int payload_num)
{
   print_debug("[case1]start",payload_num);
   unsigned int master_tx_array[128];
   unsigned int slave1_rx_array[128];
   i2c_cmd(master_addr,0,1,0,0,1,(payload_num+1));//cmd0 write  send payload_num  datas
   i2c_cmd(master_addr,1,3,0,0,1,7);//cmd1 stop 
   ctr_config(slave_addr1,0x20);//slave mode
   slave_addr_config(slave_addr1,s7bit_addr);
   fifo_wr(master_addr,(s7bit_addr<<1));//the first byte master send
   int i=0;
   for(i=0;i<payload_num;i++)
   {
     unsigned int data_value;
     while((((*(volatile U32*)(master_addr+4*2))>>16)&0xff)==128);//check master's txfifo full
     data_value=rand()%255;
     fifo_wr(master_addr,data_value);
     master_tx_array[i]=data_value;
   }
   ctr_config(master_addr,0x30);
  //slave receive datas and store datas in slave_rx_array
  for(i=0;i<payload_num;i++)
  {
     while((((*(volatile U32*)(slave_addr1+4*2))>>8)&0x1f)==0);
     slave1_rx_array[i]=fifo_rd(slave_addr1);
  }
  while(((*(volatile U32*)(master_addr+4*8))&0x00000040)==0);//check tran_comp_int_raw bit
  i2c_int_clr(master_addr,0x40);//clear int
  i2c_cmd_done(master_addr,0);
  i2c_cmd_done(master_addr,1);
 //check master_tx_array==?slave_rx_array
 for(i=0;i<payload_num;i++)
 {
  if(master_tx_array[i]!=slave1_rx_array[i])
  {
   print_debug("[case1]master send to slave",payload_num);
   fail("master sends data error");
  }
 }
   print_debug("[case1]end",payload_num);
}



//**********************************************************
// case2 master restart to send payload to slave1 and slave2
//**********************************************************
void mws1rws2_bit7(unsigned int master_addr,unsigned int slave_addr1,unsigned int slave_addr2,unsigned int s7bit_addr1,unsigned int s7bit_addr2,unsigned int s1_payload_num0,unsigned int s2_payload_num0,unsigned int s1_payload_num1,unsigned int s2_payload_num1)
{
   print_debug("[case2]start",s1_payload_num0);
   print_debug("[case2]start",s2_payload_num0);
   print_debug("[case2]start",s1_payload_num1);
   print_debug("[case2]start",s2_payload_num1);
   unsigned int master_tx_array[128];
   unsigned int slave1_rx_array[128];
   unsigned int slave2_rx_array[128];
   i2c_cmd(master_addr,0,1,0,0,1,(s1_payload_num0+1));//cmd0 write s1_payload_num0 datas to slave1
   i2c_cmd(master_addr,1,0,0,0,1,7);//cmd1 restart 
   i2c_cmd(master_addr,2,1,0,0,1,(s2_payload_num0+1));//cmd2 write s2_payload_num0 datas to slave2
   i2c_cmd(master_addr,3,0,0,0,1,7);//cmd3 restart 
   i2c_cmd(master_addr,4,1,0,0,1,(s1_payload_num1+1));//cmd4 write s1_payload_num1 datas to slave1
   i2c_cmd(master_addr,5,0,0,0,1,7);//cmd5 restart 
   i2c_cmd(master_addr,6,1,0,0,1,(s2_payload_num1+1));//cmd6 write s2_payload_num1 datas to slave2
   i2c_cmd(master_addr,7,3,0,0,1,7);//cmd7 stop 
   ctr_config(slave_addr1,0x20);//config slave_addr1 and slave_addr2 in slave mode
   ctr_config(slave_addr2,0x20);
   slave_addr_config(slave_addr1,s7bit_addr1);
   slave_addr_config(slave_addr2,s7bit_addr2);
   fifo_wr(master_addr,(s7bit_addr1<<1));//first byte(slave_addr1+r/w)for slave1
   int i=0;
   for(i=0;i<(s1_payload_num0);i++)
   {
     unsigned int data_value;
     while((((*(volatile U32*)(master_addr+4*2))>>16)&0xff)==128);
     data_value=rand()%255;
     fifo_wr(master_addr,data_value);
     master_tx_array[i]=data_value;
   }
     while((((*(volatile U32*)(master_addr+4*2))>>16)&0xff)==128);
     fifo_wr(master_addr,(s7bit_addr2<<1));//first byte(slave_addr2+r/w) after restart for slave2
   for(i=s1_payload_num0;i<(s1_payload_num0+s2_payload_num0);i++)
   {
     unsigned int data_value;
     while((((*(volatile U32*)(master_addr+4*2))>>16)&0xff)==128);
     data_value=rand()%255;
     fifo_wr(master_addr,data_value);
     master_tx_array[i]=data_value;
   }
     while((((*(volatile U32*)(master_addr+4*2))>>16)&0xff)==128);
     fifo_wr(master_addr,(s7bit_addr1<<1));//first byte(slave_addr1+r/w) after restart for slave1
   for(i=(s1_payload_num0+s2_payload_num0);i<(s1_payload_num0+s2_payload_num0+s1_payload_num1);i++)
   {
     unsigned int data_value;
     while((((*(volatile U32*)(master_addr+4*2))>>16)&0xff)==128);
     data_value=rand()%255;
     fifo_wr(master_addr,data_value);
     master_tx_array[i]=data_value;
   }
     while((((*(volatile U32*)(master_addr+4*2))>>16)&0xff)==128);
     fifo_wr(master_addr,(s7bit_addr2<<1));//first byte(slave_addr2+r/w) after restart for slave2
   for(i=(s1_payload_num0+s2_payload_num0+s1_payload_num1);i<(s1_payload_num0+s2_payload_num0+s1_payload_num1+s2_payload_num1);i++)
   {
     unsigned int data_value;
     while((((*(volatile U32*)(master_addr+4*2))>>16)&0xff)==128);
     data_value=rand()%255;
     fifo_wr(master_addr,data_value);
     master_tx_array[i]=data_value;
   }
  ctr_config(master_addr,0x30);//master start transfer
  //slave1 and slave2 receive datas and store datas in slave1_rx_array
  i=0;
  int slave1_i=0;
  int slave2_i=0;
  while(i<(s1_payload_num0+s2_payload_num0+s1_payload_num1+s2_payload_num1))
  {
   if((((*(volatile U32*)(slave_addr1+4*2))>>8)&0x1f)!=0)
   {
     slave1_rx_array[slave1_i]=fifo_rd(slave_addr1);
     slave1_i++;
     i++;
   }
   if((((*(volatile U32*)(slave_addr2+4*2))>>8)&0x1f)!=0)
   {
     slave2_rx_array[slave2_i]=fifo_rd(slave_addr2);
     slave2_i++;
     i++;
   }
  }
  while(((*(volatile U32*)(master_addr+4*8))&0x00000040)==0);//check tran_comp_int_raw bit
  i2c_int_clr(master_addr,0x40);//clear int
  i2c_cmd_done(master_addr,0);
  i2c_cmd_done(master_addr,1);
  i2c_cmd_done(master_addr,2);
  i2c_cmd_done(master_addr,3);
  i2c_cmd_done(master_addr,4);
  i2c_cmd_done(master_addr,5);
  i2c_cmd_done(master_addr,6);
  i2c_cmd_done(master_addr,7);

  //check datas from master to slave1 and slave2
  for(i=0;i<s1_payload_num0;i++)
  {
    if(slave1_rx_array[i]!=master_tx_array[i])
    {
      print_debug("[case2]master write to slave1",s1_payload_num0);
      fail("slave1 receive data from master error");
    }
  }
  for(i=0;i<s2_payload_num0;i++)
  {
    if(slave2_rx_array[i]!=master_tx_array[s1_payload_num0+i])
    {
     print_debug("[case2]master write to slave2 after restart",s2_payload_num0);
     fail("slave2 receive data from master error");
    }
  }
  for(i=s1_payload_num0;i<(s1_payload_num0+s1_payload_num1);i++)
  {
    if(slave1_rx_array[i]!=master_tx_array[s2_payload_num0+i])
     {
       print_debug("[case2]master write to slave1 after restart ",s1_payload_num1);
       fail("slave1 receive data from master error");
     }
  }
  for(i=s2_payload_num0;i<(s2_payload_num1+s2_payload_num0);i++)
  {
    if(slave2_rx_array[i]!=master_tx_array[s1_payload_num0+s1_payload_num1+i])
    {
     print_debug("[case2]master write slave2 after restart",s2_payload_num1);
     fail("slave2 receive data from master error");
    }
  }
   print_debug("[case2]end",s2_payload_num1);
}

//********************************************
// case3 master send n(>128) payload to slave1
//********************************************
void mws_over_7bit(unsigned int master_addr,unsigned int slave_addr1,unsigned int s7bit_addr,unsigned int payload_num0)
{
   print_debug("[case3]start",payload_num0);
   unsigned int master_tx_array[150];
   unsigned int slave1_rx_array[150];
   i2c_cmd(master_addr,0,1,0,0,1,(payload_num0+1));//cmd0 write  send 130 datas slave1
   i2c_cmd(master_addr,1,3,0,0,1,7);//cmd1 stop 
   ctr_config(slave_addr1,0x20);
   slave_addr_config(slave_addr1,s7bit_addr);
   while((((*(volatile U32*)(master_addr+4*2))>>16)&0xff)==128);
   fifo_wr(master_addr,(s7bit_addr<<1));//first byte for slave1
   int i=0;
   for(i=0;i<127;i++)
   {
     unsigned int data_value;
     while((((*(volatile U32*)(master_addr+4*2))>>16)&0xff)==128);
     data_value=rand()%255;
     fifo_wr(master_addr,data_value);
     master_tx_array[i]=data_value;
   }
  
  ctr_config(master_addr,0x30);//start to transfer
  int slave1_i=0;
  //slave receive data
  while(slave1_i<payload_num0) 
  {
     unsigned int data_value;
     if((((*(volatile U32*)(slave_addr1+4*2))>>8)&0x1f)!=0)
     {
      slave1_rx_array[slave1_i]=fifo_rd(slave_addr1);
      slave1_i++;
     }
   if(((((*(volatile U32*)(master_addr+4*2))>>16)&0xff)<128)&&(i<130))
   {
     data_value=rand()%255;
     fifo_wr(master_addr,data_value);
     master_tx_array[i]=data_value;
     i++;
   }
  }
  while(((*(volatile U32*)(master_addr+4*8))&0x00000040)==0);//check tran_comp_int_raw bit
  i2c_int_clr(master_addr,0x40);//clear int
  i2c_cmd_done(master_addr,0);
  i2c_cmd_done(master_addr,1);
 //check data
  for(i=0;i<payload_num0;i++)
  {
    if(master_tx_array[i]!=slave1_rx_array[i])
    {
     print_debug("[case3]master write more than 128 bytes to slave",payload_num0);
     fail("error");
    }
  }
   print_debug("[case3]end",payload_num0);
}

//**********************************************
// case4 master write first --restart--then read 
//**********************************************
void mwrrs_7bit(unsigned int master_addr,unsigned int slave_addr1,unsigned int s7bit_addr,unsigned int s1_payload_num0, unsigned int s1_payload_num1)
{
   print_debug("[case4]start",s1_payload_num0);
   print_debug("[case4]start",s1_payload_num1);
   unsigned int master_tx_array[128];
   unsigned int master_rx_array[128];
   unsigned int slave1_tx_array[128];
   unsigned int slave1_rx_array[128];
    //prepare datas for master txfifo
   fifo_wr(master_addr,(s7bit_addr<<1));//first byte(slave_addr1+r/w)for slave1 write
   int i=0;
   for(i=0;i<(s1_payload_num0);i++)
   {
     unsigned int data_value;
     while((((*(volatile U32*)(master_addr+4*2))>>16)&0xff)==128);
     data_value=rand()%255;
     fifo_wr(master_addr,data_value);
     master_tx_array[i]=data_value;
   }
  //prepare datas for salve1 txfifo
   for(i=0;i<s1_payload_num1;i++)
   {
     unsigned int data_value;
     while((((*(volatile U32*)(slave_addr1+4*2))>>16)&0xff)==128);
     data_value=rand()%255;
     fifo_wr(slave_addr1,data_value);
     slave1_tx_array[i]=data_value;
   }
   fifo_wr(master_addr,((s7bit_addr<<1)|0x1));//first byte(slave_addr1+r/w)for slave1 read
 
   i2c_cmd(master_addr,0,1,0,0,1,(s1_payload_num0+1));//cmd0 write s1_payload_num0 datas to slave1
   i2c_cmd(master_addr,1,0,0,0,1,7);//cmd1 restart 
   i2c_cmd(master_addr,2,1,0,0,1,1);//cmd2 write 1 data to slave1
   if(s1_payload_num1==1)
   {
    i2c_cmd(master_addr,3,2,1,1,1,1);//cmd3 ack=1;
    i2c_cmd(master_addr,4,3,0,0,1,7);//cmd4 stop
   }
   else
   {
    i2c_cmd(master_addr,3,2,0,0,1,(s1_payload_num1-1));//cmd3 read s1_payload_num1 datas from slave1
    i2c_cmd(master_addr,4,2,1,1,1,1);//cmd4 ack=1;
    i2c_cmd(master_addr,5,3,0,0,1,7);//cmd5 stop
   }
   ctr_config(slave_addr1,0x20);//config slave_addr1 in slave mode 
   slave_addr_config(slave_addr1,s7bit_addr);
//   fifo_wr(master_addr,(s7bit_addr<<1));//first byte(slave_addr1+r/w)for slave1 write
//    //prepare datas for master txfifo
//   int i=0;
//   for(i=0;i<(s1_payload_num0);i++)
//   {
//     unsigned int data_value;
//     while((((*(volatile U32*)(master_addr+4*2))>>16)&0xff)==128);
//     data_value=rand()%255;
//     fifo_wr(master_addr,data_value);
//     master_tx_array[i]=data_value;
//   }
//  //prepare datas for salve1 txfifo
//   for(i=0;i<s1_payload_num1;i++)
//   {
//     unsigned int data_value;
//     while((((*(volatile U32*)(slave_addr1+4*2))>>16)&0xff)==128);
//     data_value=rand()%255;
//     fifo_wr(slave_addr1,data_value);
//     slave1_tx_array[i]=data_value;
//   }
//   fifo_wr(master_addr,((s7bit_addr<<1)|0x1));//first byte(slave_addr1+r/w)for slave1 read
  ctr_config(master_addr,0x30);//master start transfer
  //slave1  receive datas and store datas in slave1_rx_array
  int slave1_i=0;
  int master_i=0;
  //slave1 receive data from master
  while(slave1_i<s1_payload_num0)
  {
   if((((*(volatile U32*)(slave_addr1+4*2))>>8)&0x1f)!=0)
   {
     slave1_rx_array[slave1_i]=fifo_rd(slave_addr1);
     slave1_i++;
   }
  } 
 //master receive data from slave1
  while(master_i<s1_payload_num1)
  {
   if((((*(volatile U32*)(master_addr+4*2))>>8)&0x1f)!=0)
   {
     master_rx_array[master_i]=fifo_rd(master_addr);
     master_i++;
   }
  }
 
  while(((*(volatile U32*)(master_addr+4*8))&0x00000040)==0);//check tran_comp_int_raw bit
  i2c_int_clr(master_addr,0x40);//clear int
  i2c_cmd_done(master_addr,0);
  i2c_cmd_done(master_addr,1);
  i2c_cmd_done(master_addr,2);
  i2c_cmd_done(master_addr,3);
  i2c_cmd_done(master_addr,4);
  if(s1_payload_num1!=1)
  i2c_cmd_done(master_addr,5);
  //check datas from master to slave1 and slave2
  for(i=0;i<s1_payload_num0;i++)
  {
    if(slave1_rx_array[i]!=master_tx_array[i])
    {
      print_debug("[case4]master write restart read",s1_payload_num0);
      fail("slave1 receive data from master error");
    }
  }
  for(i=0;i<s1_payload_num1;i++)
  {
    if(slave1_tx_array[i]!=master_rx_array[i])
    {
      print_debug("[case4]master write restart read",s1_payload_num1);
      fail("slave1 send data to master error");
    }
  }
   print_debug("[case4]end",s1_payload_num1);
}


//******************************************
// case5 master receive n payload from slave
//******************************************
void mrs_7bit(unsigned int master_addr,unsigned int slave_addr1,unsigned int s7bit_addr,unsigned int payload_num0)
{
   print_debug("[case5]start",payload_num0);
   unsigned int master_rx_array[128];
   unsigned int slave1_tx_array[128];
   int i=0;
   if(payload_num0==1)
   {
    i2c_cmd(master_addr,0,1,0,0,1,1);//cmd0 write 1 data to slave1
    i2c_cmd(master_addr,1,2,1,1,1,1);//cmd1 ack 
    i2c_cmd(master_addr,2,3,0,0,1,payload_num0);//cmd2 stop
   }
   else
   {
    i2c_cmd(master_addr,0,1,0,0,1,1);//cmd0 write 1 data to slave1
    i2c_cmd(master_addr,1,2,0,0,1,(payload_num0-1));//cmd1 read n datas from slave
    i2c_cmd(master_addr,2,2,1,1,1,1);//cmd2 ack 
    i2c_cmd(master_addr,3,3,0,0,1,payload_num0);//cmd3 stop
   }
   fifo_wr(master_addr,((s7bit_addr<<1)|(0x1)));//slave_addr=1,read
   //prepare datas for slave tx_fifo
   for(i=0;i<(payload_num0);i++)
   {
     unsigned int data_value;
     while((((*(volatile U32*)(slave_addr1+4*2))>>16)&0xff)==128);
     data_value=rand()%255;
     fifo_wr(slave_addr1,data_value);
     slave1_tx_array[i]=data_value;
   }
   ctr_config(slave_addr1,0x20);//0xa0
   slave_addr_config(slave_addr1,s7bit_addr);
   ctr_config(master_addr,0x30);//0xb0
 //master receive data from slave
 int master_i=0;
  while(master_i<payload_num0)
  {
   if((((*(volatile U32*)(master_addr+4*2))>>8)&0x1f)!=0)
   {
     master_rx_array[master_i]=fifo_rd(master_addr);
     master_i++;
   } 
  }    
  while(((*(volatile U32*)(master_addr+4*8))&0x00000040)==0);//check tran_comp_int_raw bit
  i2c_int_clr(master_addr,0x40);//clear int
  i2c_cmd_done(master_addr,0);
  i2c_cmd_done(master_addr,1);
  i2c_cmd_done(master_addr,2);
  if(payload_num0!=1)
  i2c_cmd_done(master_addr,3);
  // check data
  for(i=0;i<payload_num0;i++)
  {
    if(slave1_tx_array[i]!=master_rx_array[i])
    {
      print_debug("[case5]master read from slave",payload_num0);
      fail("slave1 send data to master error");
    }
  }
   print_debug("[case5]end",payload_num0);
}

//************************************************
// case6 master send  n payload to slave addr10bit
//***********************************************
void mws_10bit(unsigned int master_addr, unsigned int slave_addr1,unsigned int byte0_addr2,unsigned int byte1_addr,unsigned int payload_num0)
{
   print_debug("[case6]start",payload_num0);
   unsigned int master_tx_array[128];
   unsigned int slave1_rx_array[128];
   unsigned int s10bit_addr;
   unsigned int faddr_byte;
   int i=0;
   faddr_byte=(0x78|byte0_addr2);
   s10bit_addr=((1<<31)|(byte1_addr<<7)|faddr_byte);
   slave_addr_config(slave_addr1,s10bit_addr);//byte1_addr(0000001)+11110**(**is byte0_addr2)
   i2c_cmd(master_addr,0,1,0,0,1,(payload_num0+2));//cmd0 write n datas to slave
   i2c_cmd(master_addr,1,3,0,0,1,payload_num0);//cmd1 stop
   fifo_wr(master_addr,(faddr_byte<<1));//slave_addr1 first byte=11110**,write
   fifo_wr(master_addr,byte1_addr);//slave_addr1 second byte=0x01
   //prepare datas for master_tx_fifo
   for(i=0;i<(payload_num0);i++)//payload_num0 shouldn't be bigger than 126
   {
     unsigned int data_value;
     while((((*(volatile U32*)(master_addr+4*2))>>16)&0xff)==128);
     data_value=rand()%255;
     fifo_wr(master_addr,data_value);
     master_tx_array[i]=data_value;
   }
   ctr_config(slave_addr1,0x20);//
   ctr_config(master_addr,0x30);//
  //slave receive data from master 
  int slave_i=0;
  while(slave_i<payload_num0)
  {
   if((((*(volatile U32*)(slave_addr1+4*2))>>8)&0x1f)!=0)
   {
     slave1_rx_array[slave_i]=fifo_rd(slave_addr1);
     slave_i++;
   } 
  }    
  while(((*(volatile U32*)(master_addr+4*8))&0x00000040)==0);//check tran_comp_int_raw bit
  i2c_int_clr(master_addr,0x40);//clear int
  i2c_cmd_done(master_addr,0);
  i2c_cmd_done(master_addr,1);
  //check data
  for(i=0;i<payload_num0;i++)
  {
    if(slave1_rx_array[i]!=master_tx_array[i])
    {
     print_debug("[case6]master write to slave10bit",payload_num0);
     fail("slave1 send data to master error");
    }
  }
   print_debug("[case6]end",payload_num0);
}

//*****************************************************
// case7 master receive  n payload from slave1 addr10bit
//******************************************************
void mrs_10bit(unsigned int master_addr, unsigned int slave_addr1,unsigned int byte0_addr2,unsigned int byte1_addr,unsigned int payload_num0)
{
   print_debug("[case7]start",payload_num0);
   unsigned int master_rx_array[128];
   unsigned int slave1_tx_array[128];
   unsigned int s10bit_addr;
   unsigned int faddr_byte;
   int i=0;
   faddr_byte=(0x78|byte0_addr2);
   s10bit_addr=((1<<31)|(byte1_addr<<7)|faddr_byte);
   slave_addr_config(slave_addr1,s10bit_addr);//byte1_addr(0000001)+11110**(**is byte0_addr2)
   if(payload_num0==1)
   {
    i2c_cmd(master_addr,0,1,0,0,1,2);//cmd0 write 2 data to slave1
    i2c_cmd(master_addr,1,2,1,1,1,1);//cmd1 ack 1
    i2c_cmd(master_addr,2,3,0,0,1,payload_num0);//cmd2 stop
   }
   else
   {
    i2c_cmd(master_addr,0,1,0,0,1,2);//cmd0 write 2 data to slave1
    i2c_cmd(master_addr,1,2,0,0,1,(payload_num0-1));//cmd1 read n datas from slave1
    i2c_cmd(master_addr,2,2,1,1,1,1);//cmd2 ack 1
    i2c_cmd(master_addr,3,3,0,0,1,payload_num0);//cmd3 stop
   }
   fifo_wr(master_addr,((faddr_byte<<1)|0x1));//slave_addr1 first byte=11110**,read
   fifo_wr(master_addr,byte1_addr);//slave_addr1 second byte=0x01
   //prepare datas for slave_tx_fifo
   for(i=0;i<(payload_num0);i++)
   {
     unsigned int data_value;
     while((((*(volatile U32*)(slave_addr1+4*2))>>16)&0xff)==128);
     data_value=rand()%255;
     fifo_wr(slave_addr1,data_value);
     slave1_tx_array[i]=data_value;
   }
   ctr_config(slave_addr1,0x20);//
   ctr_config(master_addr,0x30);//
  //master receive data from master 
  int master_i=0;
  while(master_i<payload_num0)
  {
   if((((*(volatile U32*)(master_addr+4*2))>>8)&0x1f)!=0)
   {
     master_rx_array[master_i]=fifo_rd(master_addr);
     master_i++;
   } 
  }    
  while(((*(volatile U32*)(master_addr+4*8))&0x00000040)==0);//check tran_comp_int_raw bit
  i2c_int_clr(master_addr,0x40);//clear int
  i2c_cmd_done(master_addr,0);
  i2c_cmd_done(master_addr,1);
  i2c_cmd_done(master_addr,2);
  if(payload_num0!=1)
  i2c_cmd_done(master_addr,3);
  // check data
  for(i=0;i<payload_num0;i++)
  {
   if(slave1_tx_array[i]!=master_rx_array[i])
   {
     print_debug("[case7]master read slave10bit",payload_num0);
     fail("slave1 send data to master error");
   }
  }
   print_debug("[case7]end",payload_num0);
}

//*********************************
//case8 10bit read--restart--write
//********************************
void mrrw_10bit(unsigned int master_addr,unsigned int slave_addr1,unsigned int byte0_addr2,unsigned int byte1_addr,unsigned int payload_num0,unsigned int payload_num1)
{
   print_debug("[case8]start",payload_num0);
   print_debug("[case8]start",payload_num1);
   unsigned int master_rx_array[128];
   unsigned int master_tx_array[128];
   unsigned int slave1_tx_array[128];
   unsigned int slave1_rx_array[128];
   unsigned int s10bit_addr;
   unsigned int faddr_byte;
   int i=0;
   faddr_byte=(0x78|byte0_addr2);
   s10bit_addr=((1<<31)|(byte1_addr<<7)|faddr_byte);
   slave_addr_config(slave_addr1,s10bit_addr);//byte1_addr(0000001)+11110**(**is byte0_addr2)
   i2c_cmd(master_addr,0,1,0,0,1,2);//cmd0 write 2 data to slave1
   if(payload_num0==1)
   {
    i2c_cmd(master_addr,1,2,1,1,1,1);//cmd1 ack 1
    i2c_cmd(master_addr,2,0,0,0,1,1);//cmd2 restart
    i2c_cmd(master_addr,3,1,0,0,1,(payload_num1+2));//cmd3 write m datas to slave1 
    i2c_cmd(master_addr,4,3,0,0,1,payload_num1);//cmd4 stop
 
   }
   else
   {
    i2c_cmd(master_addr,1,2,0,0,1,(payload_num0-1));//cmd1 read n datas from slave1
    i2c_cmd(master_addr,2,2,1,1,1,1);//cmd2 ack 1
    i2c_cmd(master_addr,3,0,0,0,1,1);//cmd3 restart
    i2c_cmd(master_addr,4,1,0,0,1,(payload_num1+2));//cmd4 write m datas to slave1 
    i2c_cmd(master_addr,5,3,0,0,1,payload_num1);//cmd5 stop
   }
   fifo_wr(master_addr,((faddr_byte<<1)|0x1));//slave_addr1 first byte=11110**,read
   fifo_wr(master_addr,byte1_addr);//slave_addr1 second byte=0x01
   //prepare datas for slave_tx_fifo
   for(i=0;i<(payload_num0);i++)
   {
     unsigned int data_value;
     while((((*(volatile U32*)(slave_addr1+4*2))>>16)&0xff)==128);
     data_value=rand()%255;
     fifo_wr(slave_addr1,data_value);
     slave1_tx_array[i]=data_value;
   }
   fifo_wr(master_addr,(faddr_byte<<1));//slave_addr1 first byte=11110**,write
   fifo_wr(master_addr,byte1_addr);//slave_addr1 second byte=0x01
   //prepare datas for master_tx_fifo
   for(i=0;i<(payload_num1);i++)
   {
     unsigned int data_value;
     while((((*(volatile U32*)(master_addr+4*2))>>16)&0xff)==128);
     data_value=rand()%255;
     fifo_wr(master_addr,data_value);
     master_tx_array[i]=data_value;
   }
 
   ctr_config(slave_addr1,0x20);//
   ctr_config(master_addr,0x30);//
  //master receive data from master 
  int master_i=0;
  while(master_i<payload_num0)
  {
   if((((*(volatile U32*)(master_addr+4*2))>>8)&0x1f)!=0)
   {
     master_rx_array[master_i]=fifo_rd(master_addr);
     master_i++;
   } 
  }    
  //slave1 receive data
  int slave_i=0;
  while(slave_i<payload_num1)
  {
   if((((*(volatile U32*)(slave_addr1+4*2))>>8)&0x1f)!=0)
   {
     slave1_rx_array[slave_i]=fifo_rd(slave_addr1);
     slave_i++;
   } 
  }    
 
  while(((*(volatile U32*)(master_addr+4*8))&0x00000040)==0);//check tran_comp_int_raw bit
  i2c_int_clr(master_addr,0x40);//clear int
  i2c_cmd_done(master_addr,0);
  i2c_cmd_done(master_addr,1);
  i2c_cmd_done(master_addr,2);
  i2c_cmd_done(master_addr,3);
  i2c_cmd_done(master_addr,4);
  if(payload_num0!=1)
  i2c_cmd_done(master_addr,5);
  // check data
  for(i=0;i<payload_num0;i++)
  {
   if(slave1_tx_array[i]!=master_rx_array[i])
   {
     print_debug("[case8]master read restart write:read",payload_num0);
     fail("slave1 send data to master error");
   }
  }
  for(i=0;i<payload_num1;i++)
  {
   if(slave1_rx_array[i]!=master_tx_array[i])
   {
     print_debug("[case8]master read restart write:write",payload_num1);
     fail("slave1 receive data from master error");
   }
  }
   print_debug("[case8]end",payload_num1);
}

//********************************************************
//case9  master write slave without providing enough datas
//********************************************************
void mws_less_7bit(unsigned int master_addr,unsigned int slave_addr1,unsigned int s7bit_addr,unsigned int payload_num)
{
   print_debug("[case9]start",payload_num);
   unsigned int master_tx_array[128];
   unsigned int slave1_rx_array[128];
   i2c_cmd(master_addr,0,1,0,0,1,(payload_num+1));//cmd0 write  send payload_num  datas
   i2c_cmd(master_addr,1,3,0,0,1,7);//cmd1 stop 
   ctr_config(slave_addr1,0x20);//slave mode
   slave_addr_config(slave_addr1,s7bit_addr);
   fifo_wr(master_addr,(s7bit_addr<<1));//the first byte master send
   int i=0;
   //provide payload_num-2 datas for master txfifo
   for(i=0;i<(payload_num-2);i++)
   {
     unsigned int data_value;
     while((((*(volatile U32*)(master_addr+4*2))>>16)&0xff)==128);//check master's txfifo full
     data_value=rand()%255;
     fifo_wr(master_addr,data_value);
     master_tx_array[i]=data_value;
   }
   ctr_config(master_addr,0x30);
  //slave receive datas and store datas in slave_rx_array
  for(i=0;i<(payload_num-2);i++)
  {
     while((((*(volatile U32*)(slave_addr1+4*2))>>8)&0x1f)==0);
     slave1_rx_array[i]=fifo_rd(slave_addr1);
  }
  while(((*(volatile U32*)(master_addr+4*8))&0x00000040)==0);//check tran_comp_int_raw bit
  i2c_int_clr(master_addr,0x40);//clear tran_comp_int
  //i2c_cmd_done(master_addr,0);//cmd0=0,cmd1=0
  //i2c_cmd_done(master_addr,1);
 //check master_tx_array==?slave_rx_array
 for(i=0;i<(payload_num-2);i++)
 {
  if(master_tx_array[i]!=slave1_rx_array[i])
  {
   print_debug("[case9]master send 2 dates less than",payload_num);
   fail("master sends data error");
  }
 }
   print_debug("[case9]end",payload_num);
}
//************************************************************************************************
//case10  master write slave, slave receive data when rx_fifo_cnt is rx_full_thrhd(rx_fifo_int_raw)
//if slave doesn't read data from rx_fifo,then master will stop writing datas to slave 
//*************************************************************************************************
void mws_rxstop_7bit(unsigned int master_addr,unsigned int slave_addr1,unsigned int s7bit_addr,unsigned int payload_num,unsigned int rx_full_thrhd)
{
   print_debug("[case10]start",payload_num);
   unsigned int master_tx_array[128];
   unsigned int slave1_rx_array[128];
   i2c_cmd(master_addr,0,1,0,0,1,(payload_num+1));//cmd0 write  send payload_num  datas
   i2c_cmd(master_addr,1,3,0,0,1,7);//cmd1 stop 
   ctr_config(slave_addr1,0x20);//slave mode
   slave_addr_config(slave_addr1,s7bit_addr);
   fifo_config(slave_addr1,rx_full_thrhd);//rx_fifo_full_thrhd=0xf,default=0xb
   fifo_wr(master_addr,(s7bit_addr<<1));//the first byte master send
   int i=0;
   //provide payload_num datas for master txfifo
   for(i=0;i<(payload_num);i++)
   {
     unsigned int data_value;
     while((((*(volatile U32*)(master_addr+4*2))>>16)&0xff)==128);//check master's txfifo full
     data_value=rand()%255;
     fifo_wr(master_addr,data_value);
     master_tx_array[i]=data_value;
   }
   ctr_config(master_addr,0x30);
   int slave_i=0;
   for(i=0;i<payload_num;)
   {
     if(((*(volatile U32*)(slave_addr1+4*8))&0x00000001)==1)//check rxfifo_full_int_raw bit
     //slave receive datas and store datas in slave_rx_array
    { 
      while((((*(volatile U32*)(slave_addr1+4*2))>>8)&0x1f)!=0)//check rxfifo_cnt bit
      {
       slave1_rx_array[i]=fifo_rd(slave_addr1);
       i++;
      }
     i2c_int_clr(slave_addr1,1);//clear int
    }
    if((((*(volatile U32*)(master_addr+4*8))&0x00000040)!=0)&&(((*(volatile U32*)(slave_addr1+4*8))&0x00000001)==0))// tran_comp_int_raw=1&&rxfifo_full_int_raw!=1
   // if((((*(volatile U32*)(master_addr+4*8))&0x00000040)!=0))// tran_comp_int_raw=1&&rxfifo_full_int_raw!=1
   {
      while((((*(volatile U32*)(slave_addr1+4*2))>>8)&0x1f)!=0)//check rxfifo_cnt bit
      {
       slave1_rx_array[i]=fifo_rd(slave_addr1);
       i++;
      }
     i2c_int_clr(master_addr,0x40);//clear tran_comp_int_raw
   }
  }
  i2c_cmd_done(master_addr,0);
  i2c_cmd_done(master_addr,1);
//check master_tx_array==?slave_rx_array
 for(i=0;i<(payload_num);i++)
 {
  if(master_tx_array[i]!=slave1_rx_array[i])
  {
   print_debug("[case10]master send slave",payload_num);
   fail("master sends data error");
  }
 }
   print_debug("[case10]end",payload_num);
}

//*****************************************************************
//case11  master read slave,but slave doesn't have enough data in txfifo,then master will receive 0xff 
//*****************************************************************
void mrs_less_7bit(unsigned int master_addr,unsigned int slave_addr1,unsigned int s7bit_addr,unsigned int payload_num0)
{
   print_debug("[case11]start",payload_num0);
   unsigned int master_rx_array[128];
   unsigned int slave1_tx_array[128];
   int i=0;
   i2c_cmd(master_addr,0,1,0,0,1,1);//cmd0 write 1 data to slave1
   i2c_cmd(master_addr,1,2,0,0,1,(payload_num0-1));//cmd1 read n datas from slave
   i2c_cmd(master_addr,2,2,1,1,1,1);//cmd2 ack 
   i2c_cmd(master_addr,3,3,0,0,1,payload_num0);//cmd3 stop
   fifo_wr(master_addr,((s7bit_addr<<1)|(0x1)));//slave_addr=1,read
   //prepare datas for slave tx_fifo
   for(i=0;i<(payload_num0-2);i++)
   {
     unsigned int data_value;
     while((((*(volatile U32*)(slave_addr1+4*2))>>16)&0xff)==128);
     data_value=rand()%255;
     fifo_wr(slave_addr1,data_value);
     slave1_tx_array[i]=data_value;
   }
   ctr_config(slave_addr1,0x20);//
   slave_addr_config(slave_addr1,s7bit_addr);
   ctr_config(master_addr,0x30);//
 //master receive data from slave
  int master_i=0;
  while(master_i<(payload_num0))
  {
   if((((*(volatile U32*)(master_addr+4*2))>>8)&0x1f)!=0)
   {
     master_rx_array[master_i]=fifo_rd(master_addr);
     master_i++;
   } 
  }    
  while(((*(volatile U32*)(master_addr+4*8))&0x00000040)==0);//check tran_comp_int_raw bit
  i2c_int_clr(master_addr,0x40);//clear int
 // check data
  for(i=0;i<(payload_num0-2);i++)
  {
    if(slave1_tx_array[i]!=master_rx_array[i])
    {
      print_debug("[case11]master read slave",payload_num0);
      fail("slave1 send data to master error");
    }
  }
  i2c_cmd_done(master_addr,0);
  i2c_cmd_done(master_addr,1);
  i2c_cmd_done(master_addr,2);
  i2c_cmd_done(master_addr,3);
  print_debug("[case11]end",payload_num0);
}

//*****************************************************************
//case12  master read slave,master receive data based on rx_fifo_full_int_raw 
//*****************************************************************
void mrs_rxstop_7bit(unsigned int master_addr,unsigned int slave_addr1,unsigned int s7bit_addr,unsigned int payload_num0,unsigned int rx_full_thrhd)
{
   print_debug("[case12]start",payload_num0);
   unsigned int master_rx_array[128];
   unsigned int slave1_tx_array[128];
   fifo_config(master_addr,rx_full_thrhd);//rx_fifo_full_thrhd=0xf,default=0xb
   int i=0;
   if(payload_num0==1)
   {
    i2c_cmd(master_addr,0,1,0,0,1,1);//cmd0 write 1 data to slave1
    i2c_cmd(master_addr,1,2,1,1,1,1);//cmd1 ack 
    i2c_cmd(master_addr,2,3,0,0,1,payload_num0);//cmd2 stop
   }
   else
   {
    i2c_cmd(master_addr,0,1,0,0,1,1);//cmd0 write 1 data to slave1
    i2c_cmd(master_addr,1,2,0,0,1,(payload_num0-1));//cmd1 read n datas from slave
    i2c_cmd(master_addr,2,2,1,1,1,1);//cmd2 ack 
    i2c_cmd(master_addr,3,3,0,0,1,payload_num0);//cmd3 stop
   }
   fifo_wr(master_addr,((s7bit_addr<<1)|(0x1)));//slave_addr=1,read
   //prepare datas for slave tx_fifo
   for(i=0;i<(payload_num0);i++)
   {
     unsigned int data_value;
     while((((*(volatile U32*)(slave_addr1+4*2))>>16)&0xff)==128);
     data_value=rand()%255;
     fifo_wr(slave_addr1,data_value);
     slave1_tx_array[i]=data_value;
   }
   ctr_config(slave_addr1,0x20);//
   slave_addr_config(slave_addr1,s7bit_addr);
   ctr_config(master_addr,0x30);//
 //master receive data from slave
 int master_i=0;
  while(master_i<payload_num0)
  {
   if(((*(volatile U32*)(master_addr+4*8))&0x00000001)==1)//check rxfifo_full_int_raw bit
   {
     while((((*(volatile U32*)(master_addr+4*2))>>8)&0x1f)!=0)
     {
      master_rx_array[master_i]=fifo_rd(master_addr);
      master_i++;
     }
     i2c_int_clr(master_addr,1);//clear int
   }
   if((((*(volatile U32*)(master_addr+4*8))&0x00000040)!=0)&&(((*(volatile U32*)(master_addr+4*8))&0x00000001)==0))// tran_comp_int_raw=1&&rxfifo_full_int_raw!=1
   {
     while((((*(volatile U32*)(master_addr+4*2))>>8)&0x1f)!=0)
     {
      master_rx_array[master_i]=fifo_rd(master_addr);
      master_i++;
     }
     i2c_int_clr(master_addr,0x40);//clear int
   } 
 }    
  i2c_cmd_done(master_addr,0);
  i2c_cmd_done(master_addr,1);
  i2c_cmd_done(master_addr,2);
  if(payload_num0!=1)
  i2c_cmd_done(master_addr,3);
  // check data
  for(i=0;i<payload_num0;i++)
  {
    if(slave1_tx_array[i]!=master_rx_array[i])
    {
      print_debug("[case12]master read from slave",payload_num0);
      fail("slave1 send data to master error");
    }
  }
   print_debug("[case12]end",payload_num0);
//  while(((*(volatile U32*)(master_addr+4*8))&0x00000040)==0);//check tran_comp_int_raw bit
}



int main_i2c_ext (void)
{
   //u32 master_addr = 0x60013000;
   u32 master_addr = 0x60008c00;
   u32 slave_addr1 = 0x60008400;
   u32 slave_addr2 = 0x60023000;
   //master scl and sda config
   //scl_start_period>sda_duty_num>=13
   //scl_stop_period>scl_high_period
   scl_lp_config(master_addr,40);
   scl_hp_config(master_addr,40);
   i2c_sda_config(master_addr,14);
   scl_startp_config(master_addr,30);
   scl_stopp_config(master_addr,44);
   timeout_config(master_addr,200);

//master scl and sda config
//-----| 1+low_period  |------------------|
//     |---------------|   5+high_period  |------------
//
  /* scl_lp_config(master_addr,18);
   scl_hp_config(master_addr,20);
   i2c_sda_config(master_addr,8);
   scl_startp_config(master_addr,14);
   scl_stopp_config(master_addr,25);
   timeout_config(master_addr,200);*/


   timeout_config(slave_addr1,200);//must be configured as large as possible
   scl_lp_config(slave_addr1,40);
   scl_hp_config(slave_addr1,40);
   i2c_sda_config(slave_addr1,14);
   scl_startp_config(slave_addr1,30);
   scl_stopp_config(slave_addr1,44);//must be larger than scl_hp

   //timeout_config(slave_addr2,200);//must be configured as large as possible
   //scl_lp_config(slave_addr2,40);
   //scl_hp_config(slave_addr2,40);
   //i2c_sda_config(slave_addr2,14);
   //scl_startp_config(slave_addr2,30);
   //scl_stopp_config(slave_addr2,44);
//-----------------------------
// single cases(12 total)
//----------------------------
//  mrs_rxstop_7bit(master_addr,slave_addr1,1,36,15);
//  mrs_less_7bit(master_addr,slave_addr1,1,8);
//  mws_rxstop_7bit(master_addr,slave_addr1,1,86,15);
//  mws_less_7bit(master_addr,slave_addr1,1,8);
//  mrrw_10bit (master_addr,slave_addr1,0,1,9,8);
//  mws_7bit(master_addr,slave_addr1,1,8);
//  mws1rws2_bit7(master_addr,slave_addr1,slave_addr2,1,2,7,5,6,8);
//  mws_over_7bit(master_addr,slave_addr1,1,130);
//  mwrrs_7bit(master_addr,slave_addr1,1,7,7);
//  mrs_7bit(master_addr,slave_addr1,1,7);
//  mws_10bit(master_addr, slave_addr1,0,1,7);
//  mrs_10bit(master_addr, slave_addr1, 0, 1, 7);

//--------------------
// random test
//--------------------
  i2c_int_en(master_addr, 1<<7);

  int i;
  unsigned int temp0;
  unsigned int temp1;
  for(i=0;i<1;i++)
  {
    //temp0 = 3;
    //temp1 = 3;
    temp0=1+rand()%125;
    mws_rxstop_7bit(master_addr,slave_addr1,1,temp0,15);
    i2c_int_clr(master_addr, 1<<7);
 
    temp0=1+rand()%125;
    mrs_rxstop_7bit(master_addr,slave_addr1,1,temp0,15);
    i2c_int_clr(master_addr, 1<<7);

    temp0=1+rand()%125;
    temp1=1+rand()%125;
    mwrrs_7bit(master_addr,slave_addr1,1,temp0,temp1);
    i2c_int_clr(master_addr, 1<<7);

//pass("diag pass\n");


    temp0=1+rand()%125;
    temp1=1+rand()%125;
    mrrw_10bit (master_addr,slave_addr1,0,1,temp0,temp1);
    i2c_int_clr(master_addr, 1<<7);

    temp0=1+rand()%125;
    mws_7bit(master_addr,slave_addr1,1,temp0);//master write i datas to slave1
    i2c_int_clr(master_addr, 1<<7);

    temp0=1+rand()%125;
    mrs_7bit(master_addr,slave_addr1,1,temp0);//master read i datas from slave1
    i2c_int_clr(master_addr, 1<<7);

    temp0=1+rand()%125;
    mws_10bit(master_addr, slave_addr1,0,1,temp0);//master write i datas to slave1
    i2c_int_clr(master_addr, 1<<7);

    temp0=1+rand()%125;
    mrs_10bit(master_addr, slave_addr1, 0, 1, temp0);//master read i datas to slave1
  }

pass("diag pass\n");
}
