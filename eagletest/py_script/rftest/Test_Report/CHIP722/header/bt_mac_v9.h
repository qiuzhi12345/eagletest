inline void write_initial ()
{
 //DI Radio Initialization Start
printinfo ("start initialization \n",0);
//#----------------------------------------------------------------------------
//# Init EM radio table
//#----------------------------------------------------------------------------
WRITE_PERI_REG(0x3ffc0100,0x06040200);
WRITE_PERI_REG(0x3ffc0104,0x0e0c0a08);
WRITE_PERI_REG(0x3ffc0108,0x16141210);
WRITE_PERI_REG(0x3ffc010c,0x1e1c1a18);
WRITE_PERI_REG(0x3ffc0110,0x26242220);
WRITE_PERI_REG(0x3ffc0114,0x2e2c2a28);
WRITE_PERI_REG(0x3ffc0118,0x36343230);
WRITE_PERI_REG(0x3ffc011c,0x3e3c3a38);
WRITE_PERI_REG(0x3ffc0120,0x46444240);
WRITE_PERI_REG(0x3ffc0124,0x4e4c4a48);
WRITE_PERI_REG(0x3ffc0128,0x07050301);
WRITE_PERI_REG(0x3ffc012c,0x0f0d0b09);
WRITE_PERI_REG(0x3ffc0130,0x17151311);
WRITE_PERI_REG(0x3ffc0134,0x1f1d1b19);
WRITE_PERI_REG(0x3ffc0138,0x27252321);
WRITE_PERI_REG(0x3ffc013c,0x2f2d2b29);
WRITE_PERI_REG(0x3ffc0140,0x37353331);
WRITE_PERI_REG(0x3ffc0144,0x3f3d3b39);
WRITE_PERI_REG(0x3ffc0148,0x47454341);
WRITE_PERI_REG(0x3ffc014c,0x004d4b49);

//----------------------------------------------------------------------------
//  ExtRC RF Settings
// ----------------------------------------------------------------------------
mac_write (0x60031070,0x00000000);
mac_write (0x60031074,0x00001020);

mac_write (0x60031478,0x04070100);
mac_write (0x6003147C,0x39003900);
mac_write (0x6003148C,0x00310231);
mac_write (0x60031490,0x00000201);

mac_write (0x60031878,0xC8C00100);
mac_write (0x6003187C,0xE400E400);
//mac_write (0x60031880,0x00600261);		//change startcounter from 30 to 60 for 1mbps
mac_write (0x60031880,0x00300231);
mac_write (0x60031890,0x00000201);
mac_write (0x60031884,0x00310231);
//mac_write (0x60031884,0x00610261);		//change startcounter from 31 to 61 for 2mbps
mac_write (0x60031894,0x00000101);
// ----------------------------------------------------------------------------
// # EDR control register 
// ----------------------------------------------------------------------------
mac_write (0x60031428,0x1A000512);
printinfo ("initialzation done \n",0);
//DI Radio Initialization Done
//
//#----------------------------------------------------------------------------
//# Init Prefetch Time and Prefetch Abort Time APFM
//#----------------------------------------------------------------------------
//# BT_PREFETCHABORT_TIME_US 200 us
//# BT_PREFETCH_TIME_US 160 us
//BT_WR_RG 000000E0 01900140
mac_write (0x600314e0,0x01900140);
//# BLE_PREFETCHABORT_TIME_US 160 us
//# BLE_PREFETCH_TIME_US 120 us
//LE_WR_RG 000000E0 014000F0
mac_write (0x600318e0,0x014000F0);


// ----------------------------------------------------------------------------
//Encryption working space @ [0x160 - 0x16F]
// ----------------------------------------------------------------------------
WRITE_PERI_REG(0x3ffc0160,0x00000000);
WRITE_PERI_REG(0x3ffc0164,0x00000000);
WRITE_PERI_REG(0x3ffc0168,0x00000000);
WRITE_PERI_REG(0x3ffc016c,0x00000000);


}
