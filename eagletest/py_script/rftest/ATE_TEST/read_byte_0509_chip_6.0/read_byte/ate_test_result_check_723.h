
#ifndef CONVERT_EN
#include "../csiclib/csicAppLib.h"
#endif // !CONVERT_EN

#include <iomanip>
#include <iostream>
#include <fstream>
#include <stdlib.h>

extern double DVDD_testV_1[2];
extern double VDD_RTC_testV_1[2];
extern double DVDD_testV_2[2];
extern double VDD_RTC_testV_2[2];
extern double LightSleep_IDD_VBAT[2];
extern double LightSleep_IDD_DVDD_IO[2];
extern double Chip_PD_IDD_VBAT[2];
extern double Chip_PD_IDD_DVDD_IO[2];
extern double DynamicIDD_VBAT[2];
extern double DynamicIDD_DVDD_IO[2];

extern int Product_B13;
extern int Product_B12;
extern int is_xm;
extern int burn_flag[8];
const int adc_flag = 0;
const int Non_240M_flag = 1; // to be fixed, should be used with caution;
const int PVT_6_DIG_flag = 2;
const int PVT_VOL_Level_flag = 3;

#ifdef CONVERT_EN
extern const char *log_name;
#endif

#include <time.h>

#include "math.h"
#include "stdlib.h"
#include "stdio.h"
#include "string.h"
#include "time.h"
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#ifndef CONVERT_EN
#include "Tester.h"
#include "CscDmdApi.h"
#include "CErrorException.h"
#include "CscDmd.h"
#include "CSCMultiWaveApiAll.h"

#include "esp32_ate_test_check.h"
#else
using namespace std;
#include "iostream"
#endif

typedef unsigned char SDL_Octet;
typedef short int ShortInt;
typedef long int LongInt;
typedef unsigned short UnsignedShortInt;
typedef unsigned UnsignedInt;
typedef unsigned long UnsignedLongInt;
typedef char *Charstar;
typedef void *Voidstar;
typedef void **Voidstarstar;
typedef ShortInt S16;
typedef signed int S32;
typedef SDL_Octet U8;
typedef signed char S8;
typedef UnsignedShortInt U16;
typedef UnsignedLongInt U32;

const unsigned char xm_crc_table[256] = {
    0,
    213,
    127,
    170,
    254,
    43,
    129,
    84,
    41,
    252,
    86,
    131,
    215,
    2,
    168,
    125,
    82,
    135,
    45,
    248,
    172,
    121,
    211,
    6,
    123,
    174,
    4,
    209,
    133,
    80,
    250,
    47,
    164,
    113,
    219,
    14,
    90,
    143,
    37,
    240,
    141,
    88,
    242,
    39,
    115,
    166,
    12,
    217,
    246,
    35,
    137,
    92,
    8,
    221,
    119,
    162,
    223,
    10,
    160,
    117,
    33,
    244,
    94,
    139,
    157,
    72,
    226,
    55,
    99,
    182,
    28,
    201,
    180,
    97,
    203,
    30,
    74,
    159,
    53,
    224,
    207,
    26,
    176,
    101,
    49,
    228,
    78,
    155,
    230,
    51,
    153,
    76,
    24,
    205,
    103,
    178,
    57,
    236,
    70,
    147,
    199,
    18,
    184,
    109,
    16,
    197,
    111,
    186,
    238,
    59,
    145,
    68,
    107,
    190,
    20,
    193,
    149,
    64,
    234,
    63,
    66,
    151,
    61,
    232,
    188,
    105,
    195,
    22,
    239,
    58,
    144,
    69,
    17,
    196,
    110,
    187,
    198,
    19,
    185,
    108,
    56,
    237,
    71,
    146,
    189,
    104,
    194,
    23,
    67,
    150,
    60,
    233,
    148,
    65,
    235,
    62,
    106,
    191,
    21,
    192,
    75,
    158,
    52,
    225,
    181,
    96,
    202,
    31,
    98,
    183,
    29,
    200,
    156,
    73,
    227,
    54,
    25,
    204,
    102,
    179,
    231,
    50,
    152,
    77,
    48,
    229,
    79,
    154,
    206,
    27,
    177,
    100,
    114,
    167,
    13,
    216,
    140,
    89,
    243,
    38,
    91,
    142,
    36,
    241,
    165,
    112,
    218,
    15,
    32,
    245,
    95,
    138,
    222,
    11,
    161,
    116,
    9,
    220,
    118,
    163,
    247,
    34,
    136,
    93,
    214,
    3,
    169,
    124,
    40,
    253,
    87,
    130,
    255,
    42,
    128,
    85,
    1,
    212,
    126,
    171,
    132,
    81,
    251,
    46,
    122,
    175,
    5,
    208,
    173,
    120,
    210,
    7,
    83,
    134,
    44,
    249};
unsigned char func_xm_crc8(const unsigned char table[256], unsigned char *pdata, size_t nbytes, unsigned char crc)
{
    /* loop over the buffer data */
    while (nbytes-- > 0)
    {
        crc = table[(crc ^ *pdata++) & 0xff];
    }

    return crc;
}

////////////////////////////////
#ifndef CONVERT_EN
#define ate_check_print 1 // ATE can modify
#else
#define ate_check_print 1
#endif
////////////////////////////////

//S8 ate_RX_GAIN_CHECK_LOW_hdb[14] = { 15, -28, 14, -6, -6, -4,  6, -4, -4, -4, -4, -4, -4, -4};
//S8 ate_RX_GAIN_CHECK_HIGH_hdb[14] = {25, -17, 24,  6,  6,  4, 16,  4,  4,  4,  4,  4,  4,  4};
//S8 ate_RX_GAIN_CHECK_LOW_hdb[14] = { 16, -25, 15, -4, -6, -4,  5, -2, -2, -2, -2, -2, -2, -2};
//S8 ate_RX_GAIN_CHECK_HIGH_hdb[14] = {24, -17, 20,  1,  0,  1, 14,  2,  2,  2,  2,  2,  2,  2};

S8 ate_RX_GAIN_CHECK_LOW_hdb[8] = {-6, -1, 3, -6, -7, -7, -6, -6};
S8 ate_RX_GAIN_CHECK_HIGH_hdb[8] = {6, 9, 14, 6, 5, 5, 6, 6};

S8 ate_TX_PWCTRL_ATTEN_LOW_qdb[6] = {-6, 2, 10, 15, 20, 30};   //{-6, -4, 0, 4, 8, 12};  //disable
S8 ate_TX_PWCTRL_ATTEN_HIGH_qdb[6] = {26, 30, 38, 47, 53, 63}; //{14, 16, 20, 24, 28, 32};

S8 ate_RX_SWITCH_GAIN_HIGH_db[3] = {0, 11, 1}; //{6, -4, 8};
S8 ate_RX_SWITCH_GAIN_LOW_db[3] = {-6, 5, -5}; //{-2, -11, 1};

#define ate_RX_NOISEFLOOR_HIGH -365
#define ate_RX_NOISEFLOOR_LOW -390

#define ate_TX_PWCTRL_BACKOFF_HIGH 4
#define ate_TX_PWCTRL_BACKOFF_LOW 0

#define ate_BT_TXIQ_GAIN_HIGH 12
#define ate_BT_TXIQ_GAIN_LOW -12
#define ate_BT_TXIQ_PHASE_HIGH 25
#define ate_BT_TXIQ_PHASE_LOW -25

#define ate_TXIQ_GAIN_HIGH 12
#define ate_TXIQ_GAIN_LOW -12
#define ate_TXIQ_PHASE_HIGH 25
#define ate_TXIQ_PHASE_LOW -25

#define ate_RXIQ_GAIN_HIGH 13
#define ate_RXIQ_GAIN_LOW -13
#define ate_RXIQ_PHASE_HIGH 27
#define ate_RXIQ_PHASE_LOW -27

#define ate_TXDC_HIGH 384
#define ate_TXDC_LOW 128

#define ate_RXDC_HIGH 384
#define ate_RXDC_LOW 128

#define ate_BT_RXDC_HIGH 384
#define ate_BT_RXDC_LOW 128

#define ate_BT_TXDC_HIGH 384
#define ate_BT_TXDC_LOW 128

#define ate_FREQ_OFFSET_HIGH_ppm 20
#define ate_FREQ_OFFSET_LOW_ppm -20

#define ate_RX_PATH_SNR_HIGH_db 5000
#define ate_RX_PATH_SNR_LOW_db 25

#define ate_HT40_RX_PATH_SNR_HIGH_db 5000
#define ate_HT40_RX_PATH_SNR_LOW_db 25

#define ate_BT_RX_PATH_SNR_HIGH_db 5000
#define ate_BT_RX_PATH_SNR_LOW_db 25

#define ate_RX_PATH_GAIN_HIGH_db 44
#define ate_RX_PATH_GAIN_LOW_db 24

#define ate_HT40_RX_PATH_GAIN_HIGH_db 44
#define ate_HT40_RX_PATH_GAIN_LOW_db 24

#define ate_BT_RX_PATH_GAIN_HIGH_db 161
#define ate_BT_RX_PATH_GAIN_LOW_db 141

#define ate_ADC_DAC_SNR_HIGH_db 5000
//#define ate_ADC_DAC_SNR_LOW_db  34  //note: 161129 tar
#define ate_ADC_DAC_SNR_LOW_db 33

#define ate_dco_sweep_test_ADC_STEP_HIGH 6
#define ate_dco_sweep_test_ADC_STEP_LOW 0

#define ate_RXBB_RXIQ_HIGH 3
#define ate_RXBB_RXIQ_LOW -3

#define ate_TXBB_TXIQ_HIGH 6
#define ate_TXBB_TXIQ_LOW -6

#define ate_VDD33_HIGH 3600
#define ate_VDD33_LOW 3000

#define ate_TSEN_HIGH 256
#define ate_TSEN_LOW 0

#define ate_TXCAP_TMX2G_CCT_LOAD_HIGH 15
#define ate_TXCAP_TMX2G_CCT_LOAD_LOW 0

#define ate_TXCAP_PA2G_CCT_STG1_HIGH 14
#define ate_TXCAP_PA2G_CCT_STG1_LOW 0

#define ate_TXCAP_PA2G_CCT_STG2_HIGH 6
#define ate_TXCAP_PA2G_CCT_STG2_LOW 0

#define ate_rc_cal_dout_HIGH 60
#define ate_rc_cal_dout_LOW 3

#define ate_RTC_freq_170khz_HIGH 210 //disable
#define ate_RTC_freq_170khz_LOW 140

#define ate_RTC_freq_70khz_HIGH 90 //disable
#define ate_RTC_freq_70khz_LOW 60

#define FB_RX_NUM_HIGH 16
#define FB_RX_NUM_LOW 15

#define FB_RX_NUM_SUM_HIGH 128 //96
#define FB_RX_NUM_SUM_LOW 112  //80

#define DUT_RX_LOST_HIGH 4
#define DUT_RX_LOST_LOW 0

#define FB_RXRSSI_HIGH -48
#define FB_RXRSSI_LOW -57

#define DUT_RXRSSI_HIGH -48
#define DUT_RXRSSI_LOW -57

#define RXIQ_REMAIN_DB_HIGH -30
#define RXIQ_REMAIN_DB_LOW -200

#define RXIQ_COVER_FAIL_NUM_HIGH 0 //disable
#define RXIQ_COVER_FAIL_NUM_LOW 0

#define RXIQ_5M_SUB_HIGH 10 //disable
#define RXIQ_5M_SUB_LOW -8

#define BT_TXRX_NUM_HIGH 10000
#define BT_TXRX_NUM_LOW 90 //all 100 NUM

#define BT_DUT_RSSI_HIGH -45
#define BT_DUT_RSSI_LOW -55

#define BT_FB_RSSI_HIGH -45
#define BT_FB_RSSI_LOW -55

#define RXDC_REMAIN_PWR_THR 45 //only check when pwr<45
#define RXDC_REMAIN_HIGH 64
#define RXDC_REMAIN_LOW -64

//define check ITEM
#define TX_PWCTRL_ATTEN_ITEM 0
#define TXIQ_ITEM 1
#define RXIQ_ITEM 2
#define TXDC_ITEM 3
#define RXDC_ITEM 4
#define RX_GAIN_CHECK_ITEM 5
#define RX_NOISEFLOOR_ITEM 6
#define ADC_DAC_SNR_ITEM 7
#define FREQ_OFFSET_ITEM 8
#define RX_PATH_SNR_ITEM 9
#define BT_RX_PATH_SNR_ITEM 10
#define BT_RX_PATH_GAIN_ITEM 11
#define TX_PWCTRL_BACKOFF_ITEM 12
#define BT_TXIQ_ITEM 13
#define BT_TXDC_ITEM 14
#define RXBB_RXIQ_ITEM 15
#define TXBB_TXIQ_ITEM 16
#define RX_PATH_GAIN_ITEM 17
#define ADC_STEP_ITEM 18
#define HT40_RX_PATH_GAIN_ITEM 19
#define RX_SWITCH_GAIN_ITEM 20
#define VDD33_ITEM 21
#define HT40_RX_PATH_SNR_ITEM 22
#define TXCAP_ITEM 23
#define RC_CAL_ITEM 24
#define RXDC_REMAIN_ITEM 25
#define TSEN_ITEM 26
#define FB_RX_NUM_SUM_ITEM 27
#define DUT_RX_LOST_ITEM 28
#define CHIP_ID_CRC_ITEM 29
#define FB_RXRSSI_ITEM 30
#define DUT_RXRSSI_ITEM 31
#define BT_TXRX_NUM_ITEM 32
#define BT_DUT_RSSI_ITEM 33
#define BT_FB_RSSI_ITEM 34
#define RXIQ_REMAIN_ITEM 35
#define FB_RX_NUM_ITEM 36


#ifndef CONVERT_EN
char printf_buf[100240];
char line[512];
#define PHY_PRINT(fmt, arg...)         \
    do                                 \
    {                                  \
        memset(line, 0, sizeof(line)); \
        sprintf(line, fmt, ##arg);     \
        strcat(printf_buf, line);      \
    } while (0);
#else
char printf_buf[100240];
char temp_buf[10240];
char line[512];
#define PHY_PRINT(str, ...)              \
    do                                   \
    {                                    \
        memset(line, 0, sizeof(line));   \
        sprintf(line, str, __VA_ARGS__); \
        strcat_s(printf_buf, line);      \
    } while (0);
//#define  PHY_PRINT(str,...) printf(str,__VA_ARGS__);
#endif

#pragma pack(1)
struct ATE_PRINT_DATA_TO_MEM
{
    U32 CHIP_ID[2];
    U16 VDD33;
    U8 temp_code;
    S8 vdd33_offset;
    U8 filter_dcap_wifi[4];
    U8 filter_dcap_bt[2];
    S16 noise_array[3];
    U16 cal_rf_ana_gain[2];
    U8 para_txcap[12]; //4*3
    S16 target_power_chan_backoff[4];
    S8 tx_pwctrl_atten[24]; //POWER_CTRL_NUM*4
    S8 wifi_txiq_gain[2];
    S8 wifi_txiq_phase[2];
    U16 txdc_table[20]; //TXDC_TABLE_SIZE*4
    U16 bt_bb_gain;
    S8 bt_txiq_gain[3];
    S8 bt_txiq_phase[3];
    U16 bt_txdc_table[12]; //3*4
    U8 bt_pa_gain[10];     //BT_TX_GAIN_SIZE
    S8 bt_dig_atten[10];   //BT_TX_GAIN_SIZE
    S8 wifi_rxiq_gain[4];
    S8 wifi_rxiq_phase[4];
    U16 rxdc_rfrx_bt[2];   //RXRF_DC_NUM_BT*2      S2 change
    U16 rxdc_rfrx_wifi[26]; //(RXRF_DC_NUM_WIFI + RXRFBB_DC_NUM_WIFI*RXRF_DC_CHAN_NUM_WIFI)*2    S2 change
    U16 rxdc_rxbb_wifi[12]; //RXBB_DC_NUM_WIFI*2 
    U16 rxdc_chan_wifi[56];     //S2 change
    S16 dco_sweep_test_ADC_STEP[4];
    U16 dco_sweep_test_DCO[4];
    S8 wifi_txbb_txiq_gain[16];  //TXBB_TXIQ_NUM
    S8 wifi_txbb_txiq_phase[16]; //TXBB_TXIQ_NUM
    S8 rxbb_rxiq_gain[24];       //RXBB_RXIQ_NUM
    S8 rxbb_rxiq_phase[24];      //RXBB_RXIQ_NUM
    S8 rx_gain_check_step[24];   //3*8
    S16 ADC_DAC_SNR;
    U16 adc_dac_snr_2tone_gain;
    S32 adc_dac_snr_2tone_total_pwr;
    U32 freq_offset_cal_total_pwr[3];
    U8 freq_offset_cal_bb_gain[3];
    U8 RX_PATH_GAIN[3];
    U8 rc_dout;
    U8 remain_0;
    S16 RX_PATH_SNR[3];
    S16 RXIQ_REMAIN_DB[3];
    S16 FREQ_OFFSET_ppm[3];
    S16 FREQ_OFFSET_khz[3];
    U8 rx_switch_gain_check_bbgain[5];
    U8 TX_POCKET_SITE_NUM;
    S16 rx_switch_gain_check_total_pwr_db[5];
    S16 rx_switch_gain_check_sig_pwr_db[5];
    S16 rx_switch_gain_check_sw_g[5];
    S16 RX_SWITCH_GAIN[3];
    S16 RX_PARA_CAL_TONE[7];
    S16 RX_PARA_CAL[21]; //7*3
    U8 TX_POCKET_REQ_TIMES[2];
    S8 TX_POCKET_TEST_rssi[16];
    U8 TX_POCKET_TEST_num[16];
    U8 txp_result[4];
    S16 TX_POCKET_freq_offset[4];
    U32 TX_POCKET_STATE[8];
    U32 txreq_start_time;
    S8 rxdc_est[84]; //7*4*2
    U32 efuse_data[84];   //S2 change
    U32 svn_log;
    S32 ate_test_time[2];
    U32 bt_txrx_num[6];
    S8 bt_dut_rssi[3];
    S8 bt_fb_rssi[3];
    S8 remain_1[2];
    U32 check_result;
} __packed;

struct ATE_PRINT_DATA_TO_MEM ate_check_data;
/*
unsigned char calcrc_bytes_32(unsigned char *p, unsigned char len);
U32 chip_crc_cmp_32(unsigned char *p, U8 chip_crc, int byte_num)
{
    unsigned char crc = calcrc_bytes_32(p, byte_num);

    if ((unsigned char)chip_crc == crc)
    {
        PHY_PRINT("\nchip_crc_cmp_32 passed with crc_read %x vs crc_exp %x,\n", chip_crc, crc);
        return 0;
    }
    else
    {
        PHY_PRINT("\nchip_crc_cmp_32 failed with crc_read %x vs crc_exp %x,\n", chip_crc, crc);
        return 1;
    }
}
*/
// check functions
U32 ate_check_result[2] = {0, 0};
void check_ate_data(int data_in, int data_low, int data_high, U8 check_item)
{
    if ((data_in < data_low) || (data_in > data_high))
    {
        if (check_item < 32)
        {
            ate_check_result[0] = ate_check_result[0] | (1 << check_item);
        }
        else
        {
            ate_check_result[1] = ate_check_result[1] | (1 << (check_item - 32));
        }

        //  PHY_PRINT("\ncheck_ate_fail, data_in:%d,data_low:%d,data_high:%d,check_item:%d\n", data_in, data_low, data_high, check_item);
    }
    else
    {
        //  PHY_PRINT("\ncheck_ate_pass, data_in:%d,data_low:%d,data_high:%d,check_item:%d\n", data_in, data_low, data_high, check_item);
    }
}

unsigned char ate_check(unsigned char *data_in, int sitenum)
{
    int i, j;
    U32 CHIP_ID_l;
    U32 CHIP_ID_h;
    int cpp_version = 181009;
    U32 result_mask[2] = {0xffffffff, 0xffffffff};
    ate_check_result[0] = 0;
    ate_check_result[1] = 0;
    //#if ate_check_print
    memset(printf_buf, 0, sizeof(printf_buf));
    //#endif
    U32 *start_addr, *end_addr, length_m, length;
    start_addr = &ate_check_data.CHIP_ID[0];
    end_addr = &ate_check_data.check_result;
    length_m = sizeof(struct ATE_PRINT_DATA_TO_MEM) / 4;
    PHY_PRINT("\ndata_length=%d, %d\n", length_m, sizeof(struct ATE_PRINT_DATA_TO_MEM));

    for (i = 0; i < length_m; i++)
    {
        (*start_addr) = (data_in[i * 4 + 3] << 24) + (data_in[i * 4 + 2] << 16) + (data_in[i * 4 + 1] << 8) + (data_in[i * 4 + 0]);
        //PHY_PRINT("%d: start_addr=0x%x, 0x%x\n", i, start_addr, *start_addr);
        start_addr += 1;
    }

    //efuse check
    unsigned char *efuse_pt;
    unsigned char *pt_temp;
    unsigned char crc_result;
    efuse_pt = (unsigned char *)&ate_check_data.efuse_data;

    // reserve bits check
    for (int i = 0; i < 4; i++)
    {
        pt_temp = efuse_pt + i;
        check_ate_data(*pt_temp & 0xffffffff, 0, 0, CHIP_ID_CRC_ITEM);
    }
/*
    for (int i = 11; i < 16; i++)
    {
        pt_temp = efuse_pt + i;

        if (i == 13)
        {
            check_ate_data(*pt_temp & 0xffffffff, Product_B13, Product_B13, CHIP_ID_CRC_ITEM);
        }
        else if (i == 12)
        {
            check_ate_data(*pt_temp & 0xffffffff, Product_B12, Product_B12, CHIP_ID_CRC_ITEM);
        }
        else
        {
            check_ate_data(*pt_temp & 0xffffffff, 0, 0, CHIP_ID_CRC_ITEM);
        }
    } 

    for (int i = 17; i < 92; i++)
    {
        pt_temp = efuse_pt + i;

        if (i == 17)
        {
            check_ate_data(*pt_temp & 0xff, 0x01, 0x1f, CHIP_ID_CRC_ITEM);
        }
        else if (i == 24)
        {
            check_ate_data(*pt_temp & 0xffffffff, 0x04 + is_xm * 1, 0x04 + is_xm * 1, CHIP_ID_CRC_ITEM);
        }
        else if (i == 23)
        {
            // VOL DIG 6 calibrate value;
            check_ate_data(*pt_temp & 0xffffffff, 0x1 * burn_flag[PVT_6_DIG_flag], 0xf * burn_flag[PVT_6_DIG_flag], CHIP_ID_CRC_ITEM);
        }
        else if (i == 22)
        {
            // VOL DIG 6 calibrate value;
            check_ate_data(*pt_temp & 0xffffffff, 0, burn_flag[PVT_VOL_Level_flag] * 0x80, CHIP_ID_CRC_ITEM);
        }
        else
        {
            check_ate_data(*pt_temp & 0xffffffff, 0, 0, CHIP_ID_CRC_ITEM);
        }
    }

    if (is_xm == 0)
    {
        for (int i = 92; i < 124; i++)
        {
            pt_temp = efuse_pt + i;
            check_ate_data(*pt_temp & 0xffffffff, 0, 0, CHIP_ID_CRC_ITEM);
        }

        //    //check ck8m
        //    pt_temp=efuse_pt+16;
        //    check_ate_data( *pt_temp&0xffffffff, 30, 36, CHIP_ID_CRC_ITEM);
        //check crc
        crc_result = chip_crc_cmp_32(efuse_pt + 4, *(efuse_pt + 10), 6);
        check_ate_data(crc_result, 0, 0, CHIP_ID_CRC_ITEM);
    }
    else
    {
        unsigned char *func_otp_read = new unsigned char[30];

        for (int i = 0; i < 6; i++)
        {
            func_otp_read[5 - i] = *(efuse_pt + 4 + i);
        }

        for (int i = 6; i < 30; i++)
        {
            func_otp_read[i] = *(efuse_pt + 86 + i);
        }

        for (int i = 0; i < 30; i++)
        {
            //printf("func_otp_read[%d]=%x\n",i,func_otp_read[i]);
        }

        unsigned char func_crc8_xm_exp = 0;
        unsigned char crc_cmp_rslt = 1;
        func_crc8_xm_exp = func_xm_crc8(xm_crc_table, func_otp_read, 30, 0);

        if (*(efuse_pt + 10) != func_crc8_xm_exp)
        {
            printf("func efuse crc error! func_crc_read value=%x func_crc_exp=%x\n", *(efuse_pt + 10), func_crc8_xm_exp);
        }

        crc_cmp_rslt = *(efuse_pt + 10) - func_crc8_xm_exp; // burned unit check crc only
        check_ate_data(crc_cmp_rslt & 0xffffffff, 0, 0, CHIP_ID_CRC_ITEM);

        if (ate_check_result[0] & (1 << 29))
        {
            cout << "chip id crc failed from item crc_cmp_rslt with value :" << int(crc_cmp_rslt) << endl;
        }

        if (func_otp_read != NULL)
        {
            delete[] func_otp_read;
        }
    } */

    if (ate_check_print)
    {
        PHY_PRINT("SVN_LOG=%d\n", ate_check_data.svn_log);
    }

    if (ate_check_print)
    {
        PHY_PRINT("cpp_version=%d\n", cpp_version);
    }

    if (ate_check_print)
    {
        PHY_PRINT("CHIP_ID=0x%x, 0x%x\n", ate_check_data.CHIP_ID[1], ate_check_data.CHIP_ID[0]);
    }

    if (ate_check_print)
    {
        PHY_PRINT("VDD33=%d, temp_code=%d, vdd33_offset=%d\n", ate_check_data.VDD33, ate_check_data.temp_code, ate_check_data.vdd33_offset);
    }

    check_ate_data(ate_check_data.VDD33, ate_VDD33_LOW, ate_VDD33_HIGH, VDD33_ITEM);
    check_ate_data(ate_check_data.temp_code, ate_TSEN_LOW, ate_TSEN_HIGH, TSEN_ITEM);

    if (ate_check_print)
        PHY_PRINT("rc_dout=%d, wifi:%d, %d, %d, %d, bt:%d, %d\n", ate_check_data.rc_dout,
                  ate_check_data.filter_dcap_wifi[0], ate_check_data.filter_dcap_wifi[1], ate_check_data.filter_dcap_wifi[2], ate_check_data.filter_dcap_wifi[3],
                  ate_check_data.filter_dcap_bt[0], ate_check_data.filter_dcap_bt[1]);

    check_ate_data(ate_check_data.rc_dout, ate_rc_cal_dout_LOW, ate_rc_cal_dout_HIGH, RC_CAL_ITEM);

    if (ate_check_print)
    {
        PHY_PRINT("rf_gain=0x%x, ana_gain=0x%x\n", ate_check_data.cal_rf_ana_gain[0], ate_check_data.cal_rf_ana_gain[1]);
    }

    S16 noisefloor_min = 0;

    for (i = 0; i < 3; i++)
    {
        if (ate_check_print)
        {
            PHY_PRINT("RX_NOISEFLOOR, %d\n", ate_check_data.noise_array[i]);
        }

        if (noisefloor_min > ate_check_data.noise_array[i])
        {
            noisefloor_min = ate_check_data.noise_array[i];
        }
    }

    check_ate_data(noisefloor_min, ate_RX_NOISEFLOOR_LOW, ate_RX_NOISEFLOOR_HIGH, RX_NOISEFLOOR_ITEM);

    if (ate_check_print)
    {
        PHY_PRINT("TXCAP_TMX2G_CCT_LOAD, ");
    }

    for (i = 0; i < 4; i++)
    {
        if (ate_check_print)
        {
            PHY_PRINT("%d, ", ate_check_data.para_txcap[i * 3]);
        }

        check_ate_data(ate_check_data.para_txcap[i * 3], ate_TXCAP_TMX2G_CCT_LOAD_LOW, ate_TXCAP_TMX2G_CCT_LOAD_HIGH, TXCAP_ITEM);
    }

    if (ate_check_print)
    {
        PHY_PRINT("\n");
    }

    if (ate_check_print)
    {
        PHY_PRINT("TXCAP_PA2G_CCT_STG1, ");
    }

    for (i = 0; i < 4; i++)
    {
        if (ate_check_print)
        {
            PHY_PRINT("%d, ", ate_check_data.para_txcap[i * 3 + 1]);
        }

        check_ate_data(ate_check_data.para_txcap[i * 3 + 1], ate_TXCAP_PA2G_CCT_STG1_LOW, ate_TXCAP_PA2G_CCT_STG1_HIGH, TXCAP_ITEM);
    }

    if (ate_check_print)
    {
        PHY_PRINT("\n");
    }

    if (ate_check_print)
    {
        PHY_PRINT("TXCAP_PA2G_CCT_STG2, ");
    }

    for (i = 0; i < 4; i++)
    {
        if (ate_check_print)
        {
            PHY_PRINT("%d, ", ate_check_data.para_txcap[i * 3 + 2]);
        }

        check_ate_data(ate_check_data.para_txcap[i * 3 + 2], ate_TXCAP_PA2G_CCT_STG2_LOW, ate_TXCAP_PA2G_CCT_STG2_HIGH, TXCAP_ITEM);
    }

    if (ate_check_print)
    {
        PHY_PRINT("\n");
    }

    if (ate_check_print)
    {
        PHY_PRINT("TX_POWER_BACKOFF, ");
    }

    for (i = 0; i < 4; i++)
    {
        if (ate_check_print)
        {
            PHY_PRINT("%d, ", ate_check_data.target_power_chan_backoff[i]);
        }

        check_ate_data(ate_check_data.target_power_chan_backoff[i], ate_TX_PWCTRL_BACKOFF_LOW, ate_TX_PWCTRL_BACKOFF_HIGH, TX_PWCTRL_BACKOFF_ITEM);
    }

    if (ate_check_print)
    {
        PHY_PRINT("\n");
    }

    if (ate_check_print)
    {
        PHY_PRINT("TX_PWRCTRL_ATTEN, ");
    }

    for (i = 0; i < 24; i++)
    {
        if (ate_check_print)
        {
            PHY_PRINT("%d, ", ate_check_data.tx_pwctrl_atten[i]);
        }

        //if(i%6==5)check_ate_data(ate_check_data.tx_pwctrl_atten[i], ate_TX_PWCTRL_ATTEN_LOW_qdb[i%6], ate_TX_PWCTRL_ATTEN_HIGH_qdb[i%6], TX_PWCTRL_ATTEN_ITEM);
    }

    if (ate_check_print)
    {
        PHY_PRINT("\n");
    }

    if (ate_check_print)
    {
        PHY_PRINT("TXIQ, %d, %d; %d, %d\n", ate_check_data.wifi_txiq_gain[0], ate_check_data.wifi_txiq_phase[0], ate_check_data.wifi_txiq_gain[1], ate_check_data.wifi_txiq_phase[1]);
    }

    for (i = 0; i < 2; i++)
    {
        check_ate_data(ate_check_data.wifi_txiq_gain[i], ate_TXIQ_GAIN_LOW, ate_TXIQ_GAIN_HIGH, TXIQ_ITEM);
    }

    for (i = 0; i < 2; i++)
    {
        check_ate_data(ate_check_data.wifi_txiq_phase[i], ate_TXIQ_PHASE_LOW, ate_TXIQ_PHASE_HIGH, TXIQ_ITEM);
    }

    if (ate_check_print)
    {
        PHY_PRINT("TXDC, ");
    }

    for (i = 0; i < 5; i++)
    {
        if (ate_check_print)
        {
            PHY_PRINT("%d, %d, %d, %d; ", ate_check_data.txdc_table[i * 4], ate_check_data.txdc_table[i * 4 + 1], ate_check_data.txdc_table[i * 4 + 2], ate_check_data.txdc_table[i * 4 + 3]);
        }

        for (j = 0; j < 4; j++)
        {
            check_ate_data(ate_check_data.txdc_table[i * 4 + j], ate_TXDC_LOW, ate_TXDC_HIGH, TXDC_ITEM);
        }
    }

    if (ate_check_print)
    {
        PHY_PRINT("\n");
    }

    if (ate_check_print)
    {
        PHY_PRINT("BT_PA_GAIN, ");
    }

    for (i = 0; i < 10; i++)
    {
        if (ate_check_print)
        {
            PHY_PRINT("0x%x, ", ate_check_data.bt_pa_gain[i]);
        }
    }

    if (ate_check_print)
    {
        PHY_PRINT("\n");
    }

    if (ate_check_print)
    {
        PHY_PRINT("BT_DIG_ATTEN, ");
    }

    for (i = 0; i < 10; i++)
    {
        if (ate_check_print)
        {
            PHY_PRINT("%d, ", ate_check_data.bt_dig_atten[i]);
        }
    }

    if (ate_check_print)
    {
        PHY_PRINT("\n");
    }

    if (ate_check_print)
    {
        PHY_PRINT("BT_TX_BB, 0x%x\n", ate_check_data.bt_bb_gain);
    }

    if (ate_check_print)
    {
        PHY_PRINT("BT_TXIQ, ");
    }

    for (i = 0; i < 3; i++)
    {
        if (ate_check_print)
        {
            PHY_PRINT("%d, %d; ", ate_check_data.bt_txiq_gain[i], ate_check_data.bt_txiq_phase[i]);
        }

//s2 no bt
        // check_ate_data(ate_check_data.bt_txiq_gain[i], ate_BT_TXIQ_GAIN_LOW, ate_BT_TXIQ_GAIN_HIGH, BT_TXIQ_ITEM);
        // check_ate_data(ate_check_data.bt_txiq_phase[i], ate_BT_TXIQ_PHASE_LOW, ate_BT_TXIQ_PHASE_HIGH, BT_TXIQ_ITEM);
    }

    if (ate_check_print)
    {
        PHY_PRINT("\n");
    }

    if (ate_check_print)
    {
        PHY_PRINT("BT_TXDC, ");
    }

    for (i = 0; i < 12; i++)
    {
        if (ate_check_print)
        {
            PHY_PRINT("%d,", ate_check_data.bt_txdc_table[i]);
        }
//s2 no bt
        // check_ate_data(ate_check_data.bt_txdc_table[i], ate_BT_TXDC_LOW, ate_BT_TXDC_HIGH, BT_TXDC_ITEM);
    }

    if (ate_check_print)
    {
        PHY_PRINT("\n");
    }

    if (ate_check_print)
    {
        PHY_PRINT("RXIQ, ");
    }

    for (i = 0; i < 4; i++)
    {
        if (ate_check_print)
        {
            PHY_PRINT("%d, %d; ", ate_check_data.wifi_rxiq_gain[i], ate_check_data.wifi_rxiq_phase[i]);
        }

        check_ate_data(ate_check_data.wifi_rxiq_gain[i], ate_RXIQ_GAIN_LOW, ate_RXIQ_GAIN_HIGH, RXIQ_ITEM);
        check_ate_data(ate_check_data.wifi_rxiq_phase[i], ate_RXIQ_PHASE_LOW, ate_RXIQ_PHASE_HIGH, RXIQ_ITEM);
    }

    if (ate_check_print)
    {
        PHY_PRINT("\n");
    }

    if (ate_check_print)
    {
        PHY_PRINT("RXDC_RFRX_BT, ");
    }

    for (i = 0; i < 2; i++)      //S2 change
    {
        if (ate_check_print)
        {
            PHY_PRINT("%d, ", ate_check_data.rxdc_rfrx_bt[i]);
        }

        //check_ate_data(ate_check_data.rxdc_rfrx_bt[i], ate_BT_RXDC_LOW, ate_BT_RXDC_HIGH, RXDC_ITEM);    //S2 change
    }

    if (ate_check_print)
    {
        PHY_PRINT("\n");
    }

    if (ate_check_print)
    {
        PHY_PRINT("RXDC_RFRX_WIFI, ");
    }

    for (i = 0; i < 26; i++)     //S2 change
    {
        if (ate_check_print)
        {
            PHY_PRINT("%d, ", ate_check_data.rxdc_rfrx_wifi[i]);
        }

        check_ate_data(ate_check_data.rxdc_rfrx_wifi[i], ate_RXDC_LOW, ate_RXDC_HIGH, RXDC_ITEM);
    }

       if (ate_check_print)
    {
        PHY_PRINT("\n");
    }

    if (ate_check_print)
    {
        PHY_PRINT("RXDC_CHAN_WIFI, ");
    } 

    for (i = 0; i < 56; i++)     //S2 change
    {
        if (ate_check_print)                        //S2 change
        {
            PHY_PRINT("%d, ", ate_check_data.rxdc_chan_wifi[i]);                    //S2 change
        }

        check_ate_data(ate_check_data.rxdc_chan_wifi[i], ate_RXDC_LOW, ate_RXDC_HIGH, RXDC_ITEM);  //S2 change
    }




    if (ate_check_print)
    {
        PHY_PRINT("\n");
    }

    if (ate_check_print)
    {
        PHY_PRINT("RXDC_RXBB_WIFI, ");
    }

    for (i = 0; i < 12; i++)
    {
        if (ate_check_print)
        {
            PHY_PRINT("%d, ", ate_check_data.rxdc_rxbb_wifi[i]);
        }

        check_ate_data(ate_check_data.rxdc_rxbb_wifi[i], ate_RXDC_LOW, ate_RXDC_HIGH, RXDC_ITEM);
    }

    if (ate_check_print)
    {
        PHY_PRINT("\n");
    }

    if (ate_check_print)
    {
        PHY_PRINT("dco_sweep_test_ADC_STEP, %d, %d; %d, %d\n",
                  ate_check_data.dco_sweep_test_ADC_STEP[0], ate_check_data.dco_sweep_test_ADC_STEP[1],
                  ate_check_data.dco_sweep_test_ADC_STEP[2], ate_check_data.dco_sweep_test_ADC_STEP[3]);
    }

    check_ate_data(ate_check_data.dco_sweep_test_ADC_STEP[0], ate_dco_sweep_test_ADC_STEP_LOW, ate_dco_sweep_test_ADC_STEP_HIGH, ADC_STEP_ITEM);
    check_ate_data(ate_check_data.dco_sweep_test_ADC_STEP[1], ate_dco_sweep_test_ADC_STEP_LOW, ate_dco_sweep_test_ADC_STEP_HIGH, ADC_STEP_ITEM);
    check_ate_data(ate_check_data.dco_sweep_test_ADC_STEP[2], ate_dco_sweep_test_ADC_STEP_LOW, ate_dco_sweep_test_ADC_STEP_HIGH, ADC_STEP_ITEM);
    check_ate_data(ate_check_data.dco_sweep_test_ADC_STEP[3], ate_dco_sweep_test_ADC_STEP_LOW, ate_dco_sweep_test_ADC_STEP_HIGH, ADC_STEP_ITEM);

    if (ate_check_print)
    {
        PHY_PRINT("dco_sweep_test_DCO, %d, %d; %d, %d\n",
                  ate_check_data.dco_sweep_test_DCO[0], ate_check_data.dco_sweep_test_DCO[1],
                  ate_check_data.dco_sweep_test_DCO[2], ate_check_data.dco_sweep_test_DCO[3]);
    }

    if (ate_check_print)
    {
        PHY_PRINT("TXBB_TXIQ, ");
    }

    for (i = 0; i < 16; i++)
    {
        if (ate_check_print)
        {
            PHY_PRINT("%d, %d; ", ate_check_data.wifi_txbb_txiq_gain[i], ate_check_data.wifi_txbb_txiq_phase[i]);
        }

        check_ate_data(ate_check_data.wifi_txbb_txiq_gain[i], ate_TXBB_TXIQ_LOW, ate_TXBB_TXIQ_HIGH, TXBB_TXIQ_ITEM);
        check_ate_data(ate_check_data.wifi_txbb_txiq_phase[i], ate_TXBB_TXIQ_LOW, ate_TXBB_TXIQ_HIGH, TXBB_TXIQ_ITEM);
    }

    if (ate_check_print)
    {
        PHY_PRINT("\n");
    }

    if (ate_check_print)
    {
        PHY_PRINT("RXBB_RXIQ, ");
    }

    for (i = 0; i < 24; i++)
    {
        if (ate_check_print)
        {
            PHY_PRINT("%d, %d; ", ate_check_data.rxbb_rxiq_gain[i], ate_check_data.rxbb_rxiq_phase[i]);
        }

        check_ate_data(ate_check_data.rxbb_rxiq_gain[i], ate_RXBB_RXIQ_LOW, ate_RXBB_RXIQ_HIGH, RXBB_RXIQ_ITEM);
        check_ate_data(ate_check_data.rxbb_rxiq_phase[i], ate_RXBB_RXIQ_LOW, ate_RXBB_RXIQ_HIGH, RXBB_RXIQ_ITEM);
    }

    if (ate_check_print)
    {
        PHY_PRINT("\n");
    }

    for (i = 0; i < 3; i++)
    {
        if (ate_check_print)
        {
            PHY_PRINT("RX_GAIN_CHECK_%d, ", i * 5 + 1);
        }

        for (j = 0; j < 8; j++)
        {
            if (ate_check_print)
            {
                PHY_PRINT("%d, ", ate_check_data.rx_gain_check_step[i * 8 + j]);
            }

            check_ate_data(ate_check_data.rx_gain_check_step[i * 8 + j], ate_RX_GAIN_CHECK_LOW_hdb[j], ate_RX_GAIN_CHECK_HIGH_hdb[j], RX_GAIN_CHECK_ITEM);
        }

        if (ate_check_print)
        {
            PHY_PRINT("\n");
        }
    }

    if (ate_check_print)
    {
        PHY_PRINT("adc_dac_snr_data, bb_index=%d, tot_pwr=%d, min_pwr=16384, max=65526\n", ate_check_data.adc_dac_snr_2tone_gain, ate_check_data.adc_dac_snr_2tone_total_pwr);
    }

    if (ate_check_print)
    {
        PHY_PRINT("ADC_DAC_SNR , %ddB\n", ate_check_data.ADC_DAC_SNR);
    }

    check_ate_data(ate_check_data.ADC_DAC_SNR, ate_ADC_DAC_SNR_LOW_db, ate_ADC_DAC_SNR_HIGH_db, ADC_DAC_SNR_ITEM);

    if (ate_check_print)
    {
        PHY_PRINT("freq_offset_cal_0: , bb_gain=%d, tot_pwr=%d, min_pwr=16384, max=65526\n", ate_check_data.freq_offset_cal_bb_gain[0], ate_check_data.freq_offset_cal_total_pwr[0]);
    }

    if (ate_check_print)
    {
        PHY_PRINT("FREQ_OFFSET_0 , %dppm, %dkhz\n", ate_check_data.FREQ_OFFSET_ppm[0], ate_check_data.FREQ_OFFSET_khz[0]);
    }

    if (ate_check_print)
    {
        PHY_PRINT("RXIQ_REMAIN_0 , %ddB\n", ate_check_data.RXIQ_REMAIN_DB[0]);
    }

    if (ate_check_print)
    {
        PHY_PRINT("RX_PATH_GAIN_0 , %d\n", ate_check_data.RX_PATH_GAIN[0]);
    }

    if (ate_check_print)
    {
        PHY_PRINT("RX_PATH_SNR_0 , %ddB\n", ate_check_data.RX_PATH_SNR[0]);
    }

    check_ate_data(ate_check_data.RX_PATH_GAIN[0], ate_RX_PATH_GAIN_LOW_db, ate_RX_PATH_GAIN_HIGH_db, RX_PATH_GAIN_ITEM);
    check_ate_data(ate_check_data.FREQ_OFFSET_ppm[0], ate_FREQ_OFFSET_LOW_ppm, ate_FREQ_OFFSET_HIGH_ppm, FREQ_OFFSET_ITEM);
    check_ate_data(ate_check_data.RX_PATH_SNR[0], ate_RX_PATH_SNR_LOW_db, ate_RX_PATH_SNR_HIGH_db, RX_PATH_SNR_ITEM);
    check_ate_data(ate_check_data.RXIQ_REMAIN_DB[0], RXIQ_REMAIN_DB_LOW, RXIQ_REMAIN_DB_HIGH, RXIQ_REMAIN_ITEM);

    if (ate_check_print)
    {
        PHY_PRINT("freq_offset_cal_1: , bb_gain=%d, tot_pwr=%d, min_pwr=16384, max=65526\n", ate_check_data.freq_offset_cal_bb_gain[1], ate_check_data.freq_offset_cal_total_pwr[1]);
    }

    if (ate_check_print)
    {
        PHY_PRINT("FREQ_OFFSET_1 , %dppm, %dkhz\n", ate_check_data.FREQ_OFFSET_ppm[1], ate_check_data.FREQ_OFFSET_khz[1]);
    }

    if (ate_check_print)
    {
        PHY_PRINT("RXIQ_REMAIN_1 , %ddB\n", ate_check_data.RXIQ_REMAIN_DB[1]);
    }

    if (ate_check_print)
    {
        PHY_PRINT("RX_PATH_GAIN_1 , %d\n", ate_check_data.RX_PATH_GAIN[1]);
    }

    if (ate_check_print)
    {
        PHY_PRINT("RX_PATH_SNR_1 , %ddB\n", ate_check_data.RX_PATH_SNR[1]);
    }
     //chip s2 no BT moudle
    // check_ate_data(ate_check_data.RX_PATH_GAIN[1], ate_BT_RX_PATH_GAIN_LOW_db, ate_BT_RX_PATH_GAIN_HIGH_db, BT_RX_PATH_GAIN_ITEM);
    // check_ate_data(ate_check_data.RX_PATH_SNR[1], ate_BT_RX_PATH_SNR_LOW_db, ate_BT_RX_PATH_SNR_HIGH_db, BT_RX_PATH_SNR_ITEM);

    if (ate_check_print)
    {
        PHY_PRINT("freq_offset_cal_2: , bb_gain=%d, tot_pwr=%d, min_pwr=16384, max=65526\n", ate_check_data.freq_offset_cal_bb_gain[2], ate_check_data.freq_offset_cal_total_pwr[2]);
    }

    if (ate_check_print)
    {
        PHY_PRINT("FREQ_OFFSET_2 , %dppm, %dkhz\n", ate_check_data.FREQ_OFFSET_ppm[2], ate_check_data.FREQ_OFFSET_khz[2]);
    }

    if (ate_check_print)
    {
        PHY_PRINT("RXIQ_REMAIN_2 , %ddB\n", ate_check_data.RXIQ_REMAIN_DB[2]);
    }

    if (ate_check_print)
    {
        PHY_PRINT("RX_PATH_GAIN_2 , %d\n", ate_check_data.RX_PATH_GAIN[2]);
    }

    if (ate_check_print)
    {
        PHY_PRINT("RX_PATH_SNR_2 , %ddB\n", ate_check_data.RX_PATH_SNR[2]);
    }

    check_ate_data(ate_check_data.RX_PATH_GAIN[2], ate_HT40_RX_PATH_GAIN_LOW_db, ate_HT40_RX_PATH_GAIN_HIGH_db, HT40_RX_PATH_GAIN_ITEM);
    check_ate_data(ate_check_data.RX_PATH_SNR[2], ate_HT40_RX_PATH_SNR_LOW_db, ate_HT40_RX_PATH_SNR_HIGH_db, HT40_RX_PATH_SNR_ITEM);
    check_ate_data(ate_check_data.RXIQ_REMAIN_DB[2], RXIQ_REMAIN_DB_LOW, RXIQ_REMAIN_DB_HIGH, RXIQ_REMAIN_ITEM);

    for (i = 0; i < 5; i++)
    {
        if (ate_check_print)
            PHY_PRINT("rx_switch_gain_data_%d, bbgain=%d, tot_pwr=%d, sig_pwr=%d, sw_g=%d\n", i, ate_check_data.rx_switch_gain_check_bbgain[i],
                      ate_check_data.rx_switch_gain_check_total_pwr_db[i], ate_check_data.rx_switch_gain_check_sig_pwr_db[i], ate_check_data.rx_switch_gain_check_sw_g[i]);
    }

    if (ate_check_print)
    {
        PHY_PRINT("RX_SWITCH_GAIN: %d, %d, %d\n", ate_check_data.RX_SWITCH_GAIN[0], ate_check_data.RX_SWITCH_GAIN[1], ate_check_data.RX_SWITCH_GAIN[2]);
    }

    check_ate_data(ate_check_data.RX_SWITCH_GAIN[0], ate_RX_SWITCH_GAIN_LOW_db[0], ate_RX_SWITCH_GAIN_HIGH_db[0], RX_SWITCH_GAIN_ITEM);
    check_ate_data(ate_check_data.RX_SWITCH_GAIN[1], ate_RX_SWITCH_GAIN_LOW_db[1], ate_RX_SWITCH_GAIN_HIGH_db[1], RX_SWITCH_GAIN_ITEM);
    check_ate_data(ate_check_data.RX_SWITCH_GAIN[2], ate_RX_SWITCH_GAIN_LOW_db[2], ate_RX_SWITCH_GAIN_HIGH_db[2], RX_SWITCH_GAIN_ITEM);

    if (ate_check_print)
        PHY_PRINT("rx_para_cal_tone, pll_cap=0x%x, lna_max=0x%x, vga_max=0x%x, max_pwr=%d, max_scale=%d, %d, %d\n", ate_check_data.RX_PARA_CAL_TONE[0],
                  ate_check_data.RX_PARA_CAL_TONE[1], ate_check_data.RX_PARA_CAL_TONE[2], ate_check_data.RX_PARA_CAL_TONE[3],
                  ate_check_data.RX_PARA_CAL_TONE[4], ate_check_data.RX_PARA_CAL_TONE[5], ate_check_data.RX_PARA_CAL_TONE[6]);

    for (i = 0; i < 3; i++)
    {
        if (ate_check_print)
            PHY_PRINT("rx_para_cal_%d, pll_cap=0x%x, lna_max=0x%x, vga_max=0x%x, max_pwr=%d, max_scale=%d, %d, %d\n", i * 5 + 1, ate_check_data.RX_PARA_CAL[i * 7],
                      ate_check_data.RX_PARA_CAL[i * 7 + 1], ate_check_data.RX_PARA_CAL[i * 7 + 2], ate_check_data.RX_PARA_CAL[i * 7 + 3],
                      ate_check_data.RX_PARA_CAL[i * 7 + 4], ate_check_data.RX_PARA_CAL[i * 7 + 5], ate_check_data.RX_PARA_CAL[i * 7 + 6]);
    }

    if (ate_check_print)
    {
        PHY_PRINT("WIFI_RXDC_REMAIN, ");
    }

    for (i = 0; i < 84; i++)
    {
        if (ate_check_print)
        {
            PHY_PRINT("%d, ", ate_check_data.rxdc_est[i]);
        }

        if (((i % 3) == 2) && (ate_check_data.rxdc_est[i] < RXDC_REMAIN_PWR_THR))
        {
            check_ate_data(ate_check_data.rxdc_est[i - 2], RXDC_REMAIN_LOW, RXDC_REMAIN_HIGH, RXDC_REMAIN_ITEM);
            check_ate_data(ate_check_data.rxdc_est[i - 1], RXDC_REMAIN_LOW, RXDC_REMAIN_HIGH, RXDC_REMAIN_ITEM);
        }
    }

    if (ate_check_print)
    {
        PHY_PRINT("\n");
    }

    if (ate_check_print)
    {
        PHY_PRINT("site_num, %d; req_suc, %d; req_times, %d; dut_txseq, %d\n", ate_check_data.TX_POCKET_SITE_NUM & 0xf, ate_check_data.TX_POCKET_SITE_NUM >> 7, ate_check_data.TX_POCKET_REQ_TIMES[0], ate_check_data.TX_POCKET_REQ_TIMES[1]);
    }

    if (ate_check_print)
    {
        PHY_PRINT("fb_rxrssi, ");
    }

    S8 max_fb_rssi = -127, max_dut_rssi = -127;
    noisefloor_min = noisefloor_min / 4 + 1;

    for (i = 0; i < 8; i++)
    {
        if (ate_check_data.svn_log == 221)
        {
            ate_check_data.TX_POCKET_TEST_rssi[0 + i * 2] -= (noisefloor_min + 96);
        }

        if (max_fb_rssi < ate_check_data.TX_POCKET_TEST_rssi[0 + i * 2])
        {
            max_fb_rssi = ate_check_data.TX_POCKET_TEST_rssi[0 + i * 2];
        }

        if (ate_check_print)
        {
            PHY_PRINT("%d, ", ate_check_data.TX_POCKET_TEST_rssi[0 + i * 2]);
        }
    }

    if (ate_check_print)
    {
        PHY_PRINT("\n");
    }

    if (ate_check_print)
    {
        PHY_PRINT("dut_rxrssi, ");
    }

    for (i = 0; i < 8; i++)
    {
        if (max_dut_rssi < ate_check_data.TX_POCKET_TEST_rssi[1 + i * 2])
        {
            max_dut_rssi = ate_check_data.TX_POCKET_TEST_rssi[1 + i * 2];
        }

        if (ate_check_print)
        {
            PHY_PRINT("%d, ", ate_check_data.TX_POCKET_TEST_rssi[1 + i * 2]);
        }
    }

    if (ate_check_print)
    {
        PHY_PRINT("\n");
    }

    if (ate_check_print)
    {
        PHY_PRINT("max_fb_rssi=%d, max_dut_rssi=%d\n", max_fb_rssi, max_dut_rssi);
    }

    check_ate_data(max_fb_rssi, FB_RXRSSI_LOW, FB_RXRSSI_HIGH, FB_RXRSSI_ITEM);
    check_ate_data(max_dut_rssi, DUT_RXRSSI_LOW, DUT_RXRSSI_HIGH, DUT_RXRSSI_ITEM);
    U8 fb_rx_num_sum = 0, dut_rx_num_sum = 0, dut_rx_lost = 0, fb_rx_num_max = 0;

    if (ate_check_print)
    {
        PHY_PRINT("fb_rx_num, ");
    }

    for (i = 0; i < 8; i++)
    {
        //fb_rx_num_sum += ate_check_data.TX_POCKET_TEST_num[0+i*2];
        if (ate_check_print)
        {
            PHY_PRINT("%d, ", ate_check_data.TX_POCKET_TEST_num[0 + i * 2]);
        }

        if (fb_rx_num_max < ate_check_data.TX_POCKET_TEST_num[0 + i * 2])
        {
            fb_rx_num_max = ate_check_data.TX_POCKET_TEST_num[0 + i * 2];
        }
    }

    if (ate_check_print)
    {
        PHY_PRINT("\n");
    }

    check_ate_data(fb_rx_num_max, FB_RX_NUM_LOW, FB_RX_NUM_HIGH, FB_RX_NUM_ITEM);

    //check_ate_data(fb_rx_num_sum, FB_RX_NUM_SUM_LOW, FB_RX_NUM_SUM_HIGH, FB_RX_NUM_SUM_ITEM);
    if (ate_check_print)
    {
        PHY_PRINT("dut_rx_num, ");
    }

    for (i = 0; i < 8; i++)
    {
        //dut_rx_num_sum += ate_check_data.TX_POCKET_TEST_num[1+i*2];
        if (ate_check_print)
        {
            PHY_PRINT("%d, ", ate_check_data.TX_POCKET_TEST_num[1 + i * 2]);
        }
    }

    if (ate_check_print)
    {
        PHY_PRINT("\n");
    }

    //dut_rx_lost = fb_rx_num_sum - dut_rx_num_sum;
    if (ate_check_print)
    {
        PHY_PRINT("txp_result, %d, %d, %d, %d\n", ate_check_data.txp_result[0], ate_check_data.txp_result[1], ate_check_data.txp_result[2], ate_check_data.txp_result[3]);
    }

    fb_rx_num_sum = ate_check_data.txp_result[0];
    dut_rx_num_sum = ate_check_data.txp_result[1];
    dut_rx_lost = ate_check_data.txp_result[3];
    check_ate_data(fb_rx_num_sum, FB_RX_NUM_SUM_LOW, FB_RX_NUM_SUM_HIGH, FB_RX_NUM_SUM_ITEM);
    check_ate_data(dut_rx_lost, DUT_RX_LOST_LOW, DUT_RX_LOST_HIGH, DUT_RX_LOST_ITEM);

    if (ate_check_print)
    {
        PHY_PRINT("freq_offset_rx, ");
    }

    for (i = 0; i < 4; i++)
    {
        if (ate_check_print)
        {
            PHY_PRINT("%d, ", ate_check_data.TX_POCKET_freq_offset[i]);
        }
    }

    if (ate_check_print)
    {
        PHY_PRINT("\n");
    }

    if (ate_check_print)
        PHY_PRINT("txp_state: 0x%08x%08x%08x%08x, 0x%08x%08x%08x%08x;\n", ate_check_data.TX_POCKET_STATE[3], ate_check_data.TX_POCKET_STATE[2], ate_check_data.TX_POCKET_STATE[1], ate_check_data.TX_POCKET_STATE[0],
        ate_check_data.TX_POCKET_STATE[7], ate_check_data.TX_POCKET_STATE[6], ate_check_data.TX_POCKET_STATE[5], ate_check_data.TX_POCKET_STATE[4]);

    //if (ate_check_print) PHY_PRINT("fb_rx_num_sum=%d, dut_rx_lost=%d\n", fb_rx_num_sum, dut_rx_lost);
    if (ate_check_print)
    {
        PHY_PRINT("txreq_start_time=%d\n", ate_check_data.txreq_start_time);
    }

    if (ate_check_print)
        PHY_PRINT("bt_txrx_num: dut_rx_num=%d, fb_rx_num=%d, ntx=%d, nslvtx=%d, nrxac=%d, nrxall=%d\n", ate_check_data.bt_txrx_num[0], ate_check_data.bt_txrx_num[1],
        ate_check_data.bt_txrx_num[2], ate_check_data.bt_txrx_num[3], ate_check_data.bt_txrx_num[4], ate_check_data.bt_txrx_num[5]);
//S2 NO BT
    // check_ate_data(ate_check_data.bt_txrx_num[0], BT_TXRX_NUM_LOW, BT_TXRX_NUM_HIGH, BT_TXRX_NUM_ITEM);
    // check_ate_data(ate_check_data.bt_txrx_num[1], BT_TXRX_NUM_LOW, BT_TXRX_NUM_HIGH, BT_TXRX_NUM_ITEM);

    if (ate_check_print)
    {
        PHY_PRINT("bt_dut_rssi: %d, %d, %d\n", ate_check_data.bt_dut_rssi[0], ate_check_data.bt_dut_rssi[1], ate_check_data.bt_dut_rssi[2]);
    }

    // check_ate_data(ate_check_data.bt_dut_rssi[0], BT_DUT_RSSI_LOW, BT_DUT_RSSI_HIGH, BT_DUT_RSSI_ITEM);

    if (ate_check_print)
    {
        PHY_PRINT("bt_fb_rssi: %d, %d, %d\n", ate_check_data.bt_fb_rssi[0], ate_check_data.bt_fb_rssi[1], ate_check_data.bt_fb_rssi[2]);
    }

    // check_ate_data(ate_check_data.bt_fb_rssi[0], BT_FB_RSSI_LOW, BT_FB_RSSI_HIGH, BT_FB_RSSI_ITEM);

    if (ate_check_print)
    {
        PHY_PRINT("efuse_data: ");
    }

    for (i = 0; i < 84; i++)
    {
        if (ate_check_print)
        {
            PHY_PRINT("0x%x, ", ate_check_data.efuse_data[i]);
        }
    }

    if (ate_check_print)
        PHY_PRINT("\n", ate_check_data.txreq_start_time)
    if (ate_check_print)
    {
        PHY_PRINT("ate_test_time: %d, %d\n", ate_check_data.ate_test_time[0], ate_check_data.ate_test_time[1]);
    }

    if (ate_check_print)
    {
        PHY_PRINT("check_result[0]=0x%x, check_result[1]=0x%x\n", ate_check_result[0], ate_check_result[1]);
    }

    //ate_check_result[0] = ate_check_result[0] & result_mask[0];
    U32 check_flag = 0;

    if (ate_check_print)
    {
        PHY_PRINT("\n\n--------------------------------------------------------\n");

        if ((ate_check_result[0] > 0) || (ate_check_result[1] > 0))
        {
            PHY_PRINT("---------------CHECK BOARD FAIL----------------\nBecause:");

            for (i = 0; i < 64; i++)
            {
                if (i < 32)
                {
                    check_flag = ate_check_result[0] & (1 << i);
                }
                else
                {
                    check_flag = ate_check_result[1] & (1 << (i - 32));
                }

                if (check_flag)
                {
                    switch (i)
                    {
                    case TX_PWCTRL_ATTEN_ITEM:
                        PHY_PRINT("TX_PWRCTRL_ATTEN FAIL, ");
                        break;

                    case TXIQ_ITEM:
                        PHY_PRINT("TXIQ FAIL, ");
                        break;

                    case RXIQ_ITEM:
                        PHY_PRINT("RXIQ FAIL, ");
                        break;

                    case TXDC_ITEM:
                        PHY_PRINT("TXDC FAIL, ");
                        break;
//S2 NO BT
                    // case BT_RX_PATH_SNR_ITEM:
                    //     PHY_PRINT("BT_RX_PATH_SNR FAIL, ");
                    //     break;

                    // case BT_RX_PATH_GAIN_ITEM:
                    //     PHY_PRINT("BT_RX_PATH_GAIN FAIL, ");
                    //     break;

                    case HT40_RX_PATH_SNR_ITEM:
                        PHY_PRINT("HT40_RX_PATH_SNR FAIL, ");
                        break;

                    case HT40_RX_PATH_GAIN_ITEM:
                        PHY_PRINT("HT40_RX_PATH_GAIN FAIL, ");
                        break;
//S2 NO BT
                    // case BT_TXIQ_ITEM:
                    //     PHY_PRINT("BT_TXIQ FAIL, ");
                    //     break;

                    // case BT_TXDC_ITEM:
                    //     PHY_PRINT("BT_TXDC FAIL, ");
                    //     break;

                    case RXDC_REMAIN_ITEM:
                        PHY_PRINT("RXDC_REMAIN FAIL, ");
                        break;

                    case RXDC_ITEM:
                        PHY_PRINT("RXDC FAIL, ");
                        break;

                    case RX_GAIN_CHECK_ITEM:
                        PHY_PRINT("RX_GAIN_CHECK FAIL, ");
                        break;

                    case RX_NOISEFLOOR_ITEM:
                        PHY_PRINT("RX_NOISEFLOOR FAIL, ");
                        break;

                    case ADC_DAC_SNR_ITEM:
                        PHY_PRINT("ADC_DAC_SNR FAIL, ");
                        break;

                    case FREQ_OFFSET_ITEM:
                        PHY_PRINT("FREQ_OFFSET FAIL, ");
                        break;

                    case RX_PATH_SNR_ITEM:
                        PHY_PRINT("RX_PATH_SNR FAIL, ");
                        break;

                    case TX_PWCTRL_BACKOFF_ITEM:
                        PHY_PRINT("TX_PWCTRL_BACKOFF FAIL, ");
                        break;

                    case FB_RXRSSI_ITEM:
                        PHY_PRINT("FB_RXRSSI FAIL, ");
                        break;

                    case DUT_RXRSSI_ITEM:
                        PHY_PRINT("DUT_RXRSSI FAIL, ");
                        break;

                    case RXBB_RXIQ_ITEM:
                        PHY_PRINT("RXBB_RXIQ FAIL, ");
                        break;

                    case TXBB_TXIQ_ITEM:
                        PHY_PRINT("TXBB_TXIQ FAIL, ");
                        break;

                    case RX_PATH_GAIN_ITEM:
                        PHY_PRINT("RX_PATH_GAIN FAIL, ");
                        break;

                    case ADC_STEP_ITEM:
                        PHY_PRINT("ADC_STEP FAIL, ");
                        break;

                    case RX_SWITCH_GAIN_ITEM:
                        PHY_PRINT("RX_SWITCH_GAIN FAIL, ");
                        break;

                    case VDD33_ITEM:
                        PHY_PRINT("VDD33 FAIL, ");
                        break;

                    case TXCAP_ITEM:
                        PHY_PRINT("TXCAP FAIL, ");
                        break;

                    case RC_CAL_ITEM:
                        PHY_PRINT("RC_CAL FAIL, ");
                        break;

                    case TSEN_ITEM:
                        PHY_PRINT("TSEN FAIL, ");
                        break;

                    case FB_RX_NUM_SUM_ITEM:
                        PHY_PRINT("FB_RX_NUM_SUM FAIL, ");
                        break;

                    case DUT_RX_LOST_ITEM:
                        PHY_PRINT("DUT_RX_LOST FAIL, ");
                        break;

                    case CHIP_ID_CRC_ITEM:
                        PHY_PRINT("CHIP_ID_CRC FAIL, ");
                        break;

                    case BT_TXRX_NUM_ITEM:
                        PHY_PRINT("BT_TXRX_NUM FAIL, ");
                        break;

                    case BT_DUT_RSSI_ITEM:
                        PHY_PRINT("BT_DUT_RSSI FAIL, ");
                        break;

                    case BT_FB_RSSI_ITEM:
                        PHY_PRINT("BT_FB_RSSI FAIL, ");
                        break;

                    case RXIQ_REMAIN_ITEM:
                        PHY_PRINT("RXIQ_REMAIN FAIL, ");
                        break;

                    case FB_RX_NUM_ITEM:
                        PHY_PRINT("FB_RX_NUM FAIL, ");
                        break;

                    default:
                        break;
                    }
                }
            }

            PHY_PRINT("\n");
        }
        else
        {
            PHY_PRINT("---------------CHECK BOARD PASS----------------\n");
        }

        PHY_PRINT("--------------------------------------------------------\n\n\n");
    }

#if ate_check_print
    PHY_PRINT("DVDD_testV1 = %f\n", DVDD_testV_1[sitenum]);
    PHY_PRINT("VDD_RTC_testV1 = %f\n", VDD_RTC_testV_1[sitenum]);
    PHY_PRINT("DVDD_testV2 = %f\n", DVDD_testV_2[sitenum]);
    PHY_PRINT("VDD_RTC_testV2 = %f\n", VDD_RTC_testV_2[sitenum]);
    PHY_PRINT("LightSleep_IDD_VBAT = %f\n", LightSleep_IDD_VBAT[sitenum]);
    PHY_PRINT("LightSleep_IDD_DVDD_IO = %f\n", LightSleep_IDD_DVDD_IO[sitenum]);
    PHY_PRINT("Chip_PD_IDD_VBAT = %f\n", Chip_PD_IDD_VBAT[sitenum]);
    PHY_PRINT("Chip_PD_IDD_DVDD_IO = %f\n", Chip_PD_IDD_DVDD_IO[sitenum]);
    PHY_PRINT("AnaWorkIDD_VBAT = %f\n", DynamicIDD_VBAT[sitenum]);
    PHY_PRINT("AnaWorkIDD_DVDD_IO = %f\n", DynamicIDD_DVDD_IO[sitenum]);
#endif
#ifndef CONVERT_EN
    U8 *din;
    din = (U8 *)data_in;

    for (i = 0; i < sizeof(struct ATE_PRINT_DATA_TO_MEM); i++)
    {
        PHY_PRINT("%02x\n", din[i]);
    }


#endif
#ifndef CONVERT_EN
    //   cscExec->Datalog()->printf("%s", printf_buf);
    char filename[68];
    char time[64];
    const time_t t = std::time(NULL);
    struct tm *current_time = localtime(&t);
    CHIP_ID_h = ((ate_check_data.CHIP_ID[1] & 0xffff) << 8) + (ate_check_data.CHIP_ID[0] >> 24);
    CHIP_ID_l = ate_check_data.CHIP_ID[0] & 0xffffff;
    //sprintf(filename, "./RF_Site%d_ft_chip_id_%d_%x_%x_%d%02d%02d_%02d%02d%02d.log",sitenum+1, cpp_version,CHIP_ID_h ,CHIP_ID_l, 1900 + current_time->tm_year, 1 + current_time->tm_mon,  current_time->tm_mday, current_time->tm_hour, current_time->tm_min, current_time->tm_sec);
    sprintf(filename, "/usr/local/home/prod/DATA_LOCAL/ESP_datalog/RF_Site%d_ft_chip_id_%d_%x_%x_%d%02d%02d_%02d%02d%02d.log", sitenum + 1, cpp_version, CHIP_ID_h, CHIP_ID_l, 1900 + current_time->tm_year, 1 + current_time->tm_mon, current_time->tm_mday, current_time->tm_hour, current_time->tm_min, current_time->tm_sec);
    ofstream outIDFile;
    outIDFile.open(filename, ios::out);

    if (!outIDFile)
    {
        cerr << "RF datalog File can't be opened\n";
        exit(1);
    }

    outIDFile << printf_buf << endl;
    outIDFile.close();
#else
    char filename[64];
    /*
       char time[64];
       const time_t t = std::time(NULL);
       struct tm* current_time = localtime(&t);
       */
    sprintf(filename, "./%s", log_name);
    ofstream outIDFile;
    outIDFile.open(filename, ios::out);

    if (!outIDFile)
    {
        cerr << "RF datalog File can't be opened\n";
        cin.get();
        cin.get();
        exit(1);
    }

    outIDFile << printf_buf << endl;
    outIDFile.close();
    //cout<<printf_buf<<endl;
    //cout<<log_name<<endl;
    /*
    printf_buf=NULL;
    temp_buf=NULL;
    line=NULL;
    filename='';
    */
#endif
    return ((ate_check_result[0] > 0) || (ate_check_result[1] > 0));
}
