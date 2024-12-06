

#ifndef CONVERT_EN
    #include "../csiclib/csicAppLib.h"
#endif // !CONVERT_EN


#include  <iomanip>
#include  <iostream> 
#include  <fstream>
#include  <stdlib.h>


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

#ifdef CONVERT_EN
    extern const char* log_name;
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

    #include "esp8089_ate_test_check.h"
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
typedef char * Charstar;
typedef void * Voidstar;
typedef void ** Voidstarstar;
typedef ShortInt  S16;
typedef signed int S32;
typedef SDL_Octet  U8;
typedef signed char S8;
typedef UnsignedShortInt  U16;
typedef UnsignedLongInt  U32;

////////////////////////////////
#ifndef CONVERT_EN
    #define ate_check_print 1    // ATE can modify
#else
    #define ate_check_print 1
#endif
////////////////////////////////


//S8 ate_RX_GAIN_CHECK_LOW_hdb[14] = { 15, -28, 14, -6, -6, -4,  6, -4, -4, -4, -4, -4, -4, -4};
//S8 ate_RX_GAIN_CHECK_HIGH_hdb[14] = {25, -17, 24,  6,  6,  4, 16,  4,  4,  4,  4,  4,  4,  4};
S8 ate_RX_GAIN_CHECK_LOW_hdb[14] = { 16, -25, 15, -4, -6, -4,  5, -2, -2, -2, -2, -2, -2, -2};
S8 ate_RX_GAIN_CHECK_HIGH_hdb[14] = {24, -17, 20,  1,  0,  1, 14,  2,  2,  2,  2,  2,  2,  2};

S8 ate_TX_PWCTRL_ATTEN_LOW_qdb[6] = {-6, 2, 10, 15, 20, 30}; //{-6, -4, 0, 4, 8, 12};
S8 ate_TX_PWCTRL_ATTEN_HIGH_qdb[6] = {26, 30, 38, 47, 53, 63}; //{14, 16, 20, 24, 28, 32};

S8 ate_RX_SWITCH_GAIN_HIGH_db[3] = { 5,  -6, 6};//{6, -4, 8};
S8 ate_RX_SWITCH_GAIN_LOW_db[3] =  { 1,  -9, 3};//{-2, -11, 1};

#define ate_RX_NOISEFLOOR_HIGH -370
#define ate_RX_NOISEFLOOR_LOW  -390

#define ate_TX_PWCTRL_CHAN_OFFSET_HIGH_qdb  10
#define ate_TX_PWCTRL_CHAN_OFFSET_LOW_qdb  -10

#define ate_TXIQ_GAIN_HIGH  12
#define ate_TXIQ_GAIN_LOW  -12
#define ate_TXIQ_PHASE_HIGH  25
#define ate_TXIQ_PHASE_LOW  -25

#define ate_RXIQ_GAIN_HIGH  13
#define ate_RXIQ_GAIN_LOW  -13
#define ate_RXIQ_PHASE_HIGH  27
#define ate_RXIQ_PHASE_LOW  -27

#define ate_TXDC_HIGH 124
#define ate_TXDC_LOW  3

#define ate_RXDC_HIGH  384
#define ate_RXDC_LOW  128

#define ate_FREQ_OFFSET_HIGH_ppm 30
#define ate_FREQ_OFFSET_LOW_ppm  -10

#define ate_RX_PATH_SNR_HIGH_db  5000
#define ate_RX_PATH_SNR_LOW_db  25

#define ate_RX_PATH_GAIN_HIGH_db  48
#define ate_RX_PATH_GAIN_LOW_db   40

#define ate_ADC_DAC_SNR_HIGH_db  5000
#define ate_ADC_DAC_SNR_LOW_db  34

#define ate_dco_sweep_test_ADC_STEP_HIGH 5
#define ate_dco_sweep_test_ADC_STEP_LOW 0

#define ate_BBRX2_RXIQ_HIGH  3
#define ate_BBRX2_RXIQ_LOW  -3

#define ate_TXBB_TXIQ_HIGH  6
#define ate_TXBB_TXIQ_LOW  -6

#define ate_VDD33_HIGH  3600
#define ate_VDD33_LOW  3200 

#define ate_TXCAP_TMX2G_CCT_LOAD_HIGH  15
#define ate_TXCAP_TMX2G_CCT_LOAD_LOW  0

#define ate_TXCAP_PA2G_CCT_STG1_HIGH  12
#define ate_TXCAP_PA2G_CCT_STG1_LOW  0

#define ate_TXCAP_PA2G_CCT_STG2_HIGH  6
#define ate_TXCAP_PA2G_CCT_STG2_LOW  0

#define ate_rc_cal_dout_HIGH 60 
#define ate_rc_cal_dout_LOW 3

#define ate_RTC_freq_170khz_HIGH 210
#define ate_RTC_freq_170khz_LOW 140

#define ate_RTC_freq_70khz_HIGH 90
#define ate_RTC_freq_70khz_LOW 60

#define FB_RX_NUM_HIGH 16
#define FB_RX_NUM_LOW 15

#define FB_RX_NUM_SUM_HIGH 96
#define FB_RX_NUM_SUM_LOW 64

#define DUT_RX_LOST_HIGH 2
#define DUT_RX_LOST_LOW 0

#define FB_RXRSSI_HIGH 48
#define FB_RXRSSI_LOW 41

#define DUT_RXRSSI_HIGH 60
#define DUT_RXRSSI_LOW 52

#define RXIQ_REMAIN_DB_HIGH  -30
#define RXIQ_REMAIN_DB_LOW  -200

#define RXIQ_COVER_FAIL_NUM_HIGH 0
#define RXIQ_COVER_FAIL_NUM_LOW  0

#define RXIQ_5M_SUB_HIGH 10
#define RXIQ_5M_SUB_LOW -8

//define check ITEM
#define TX_PWCTRL_ATTEN_ITEM  0
#define TXIQ_ITEM 1
#define RXIQ_ITEM 2
#define TXDC_ITEM 3
#define RXDC_ITEM 4
#define RX_GAIN_CHECK_ITEM 5
#define RX_NOISEFLOOR_ITEM 6
#define ADC_DAC_SNR_ITEM 7
#define FREQ_OFFSET_ITEM 8
#define RX_PATH_SNR_ITEM 9
#define RXIQ_REMAIN_ITEM 10
#define SDIO_PAD_ITEM 11
#define TX_PWCTRL_CHAN_OFFSET_ITEM 12
#define TXIQ_Convergence_ITEM 13
#define RXIQ_Convergence_ITEM 14
#define BBRX2_RXIQ_ITEM 15
#define TXBB_TXIQ_ITEM 16
#define RX_PATH_GAIN_ITEM 17
#define ADC_STEP_ITEM 18
#define RXIQ_COVER_FAIL_NUM_ITEM 19
#define RX_SWITCH_GAIN_ITEM 20
#define VDD33_ITEM 21
#define RXIQ_5M_SUB_ITEM 22
#define TXCAP_ITEM 23
#define RC_CAL_ITEM 24
#define ROM_BIST_ITEM 25
#define FB_RX_NUM_ITEM 26
#define FB_RX_NUM_SUM_ITEM 27
#define DUT_RX_LOST_ITEM 28
#define CHIP_ID_CRC_ITEM 29

#define DCO_HIGH_LOW_ITEM 12
#define FB_RXRSSI_ITEM 13
#define DUT_RXRSSI_ITEM 14
#define IO_TEST_ITEM 30
#define RTC_FREQ_ITEM 31

// check functions
U32 ate_check_result = 0;
void check_ate_data(int data_in, int data_low, int data_high, U8 check_item)
{
    if ((data_in < data_low) || (data_in > data_high)){
        ate_check_result = ate_check_result | (1<<check_item);
    }
}


#ifndef CONVERT_EN
    char printf_buf[10240];
    char line[512];
    #define PHY_PRINT(fmt, arg...)  do { \
    memset(line, 0, sizeof(line));\
        sprintf(line, fmt, ##arg);\
        strcat(printf_buf, line); \
    } while (0);
#else 
    char printf_buf[10240];
    char temp_buf[10240];
    char line[512];
    #define PHY_PRINT(str,...) do { \
    memset(line, 0, sizeof(line));\
        sprintf(line, str, __VA_ARGS__);\
        strcat_s(printf_buf, line); \
    } while (0);
//#define  PHY_PRINT(str,...) printf(str,__VA_ARGS__);
#endif


unsigned char ate_check(unsigned char *data_in,int sitenum)
{
    int i, j;
    U8 *CHIP_ID;
    U32 CHIP_ID_t;
    U8 *CHIP_VERSION;
    U8 *VDD33;
    U16 VDD33_t;
    U8 *temp_code;
    U8 *offset;
    S16 offset_t;
    U8 *cal_rf_ana_gain;
    S8 *TXBB_TXIQ_gain; 
    S8 *TXBB_TXIQ_phase;
    S8 *RX_PARA_CAL_TONE_DATA_1; 
    S8 *TXBB_TXDC_q; 
    S8 *RX_GAIN_CHECK;
    S8 *BBRX2_RXIQ_gain;
    S8 *BBRX2_RXIQ_phase;
    U8 *RX_NOISEFLOOR;  //S16
    S16 RX_NOISEFLOOR_t[3];
    U8 *TXCAP_TMX2G_CCT_LOAD;
    U8 *TXCAP_PA2G_CCT_STG1;
    U8 *TXCAP_PA2G_CCT_STG2;
    S8 *TX_PWRCTRL_ATTEN;
    S8 *TX_PWCTRL_CHAN_OFFSET;
    S8 *TXIQ_gain;
    S8 *TXIQ_phase;
    U8 *TXDC_i;
    U8 *TXDC_q;
    S8 *RXIQ_gain;
    S8 *RXIQ_phase;
    U8 *RXDC_c_i;
    U16 RXDC_c_i_t[30];
    U8 *RXDC_c_q;
    U16 RXDC_c_q_t[30];
    U8 *RXDC_f_i;
    U16 RXDC_f_i_t[30];
    U8 *RXDC_f_q;
    U16 RXDC_f_q_t[30];
    U8 *freq_offset_cal_total_pwr;
    S32 freq_offset_cal_total_pwr_t;
    U8 *freq_offset_cal_bb_gain;
    S8 *FREQ_OFFSET;
    U8 *RX_PATH_SNR;
    S16 RX_PATH_SNR_t;
    U8 *adc_dac_snr_2tone_gain;
    U8 *adc_dac_snr_2tone_total_pwr;
    S32 adc_dac_snr_2tone_total_pwr_t;
    U8 *ADC_DAC_SNR;
    U8 *rx_switch_gain_check_bbrx1;
    U16 rx_switch_gain_check_bbrx1_t[5];
    U8 *rx_switch_gain_check_bbrx2;
    U16 rx_switch_gain_check_bbrx2_t[5];
    U8 *rx_switch_gain_check_total_pwr_db;
    U8 *rx_switch_gain_check_sig_pwr_db;
    S8 *rx_switch_gain_check_sw_g;
    S8 *RX_SWITCH_GAIN;
    S8 *dco_sweep_test_ADC_STEP;
    U8 *dco_sweep_test_DCO;
    U16 dco_sweep_test_DCO_t[4];
    U8 *rx_path_gain;
    U8 *RX_NOISEFLOOR_14;
    S16 RX_NOISEFLOOR_14_t;
    U8 *rc_cal_dout;
    U8 *rx_gain_check_tot_pwr;
    U8 *rx_gain_check_sig_pwr;
    U8 *rxiq_tot_pwr;
    U8 *check_result;
    U32 check_result_t;
    U8 *RTC_freq_170khz;
    U8 *RTC_freq_70khz;
    U8 *svn_version;
    U16 svn_version_t;
    U8 *TX_POCKET_TEST;
    U8 *TX_POCKET_STATE;
    U32 TX_POCKET_STATE_t[6];
    U8 *RX_PARA_CAL;
    U8 *RX_PARA_CAL_TONE;
    U8 *wifi_init_time;
    U32 wifi_init_time_t;
    U8 *WIFI_INIT_ITEM;
    U32 WIFI_INIT_ITEM_t;
    S8 *RX_PARA_CAL_TONE_DATA_2;
    U8 *TX_POCKET_REQ_TIMES;
    U8 *rom_bist_result;
    U8 *io_test_result;
    S8 *rxiq_remain;
    S8 *RXIQ_FREQ_TEST;
    U8 *TX_POCKET_SITE_NUM;
    U8 *rxiq_compute_num;
    U8 *rxiq_cover_fail_num;

    U16 addr_offset[] = {1, 5, 6, 8, 9, 11, 14, 23, 32, 41, 50, 92, 98, 104, 110, 113, 116, 119, 125, 139, 140, 141, 146, 151, 156, 161, 191, 221, 
                         251, 401, 405, 406, 407, 409, 412, 416, 417, 427, 437, 442, 447, 452, 455, 459, 467, 468, 470, 471, 486, 501, 502, 508, 509, 
                         510, 281, 311, 335, 356, 363, 369, 373, 367, 387, 507, 388, 389, 393, 394, 398};

    U32 result_mask = 0xffffffff; 

    ate_check_result = 0;

    CHIP_ID = (U8*)data_in + addr_offset[0] - 1;
    CHIP_VERSION = (U8*)data_in + addr_offset[1] - 1;
    VDD33 = (U8*)data_in + addr_offset[2] - 1;
    temp_code = (U8*)data_in + addr_offset[3] - 1;
    offset = (U8*)data_in + addr_offset[4] - 1;
    cal_rf_ana_gain = (U8*)data_in + addr_offset[5] - 1;
    TXBB_TXIQ_gain = (S8*)data_in + addr_offset[6] - 1;
    TXBB_TXIQ_phase = (S8*)data_in + addr_offset[7] - 1;
    RX_PARA_CAL_TONE_DATA_1 = (S8*)data_in + addr_offset[8] - 1;
    TXBB_TXDC_q = (S8*)data_in + addr_offset[9] - 1;
    RX_GAIN_CHECK = (S8*)data_in + addr_offset[10] - 1;
    BBRX2_RXIQ_gain = (S8*)data_in + addr_offset[11] - 1;
    BBRX2_RXIQ_phase = (S8*)data_in + addr_offset[12] - 1;
    RX_NOISEFLOOR = (U8*)data_in + addr_offset[13] - 1;
    TXCAP_TMX2G_CCT_LOAD = (U8*)data_in + addr_offset[14] - 1;
    TXCAP_PA2G_CCT_STG1 = (U8*)data_in + addr_offset[15] - 1;
    TXCAP_PA2G_CCT_STG2 = (U8*)data_in + addr_offset[16] - 1;
    TX_PWRCTRL_ATTEN = (S8*)data_in + addr_offset[17] - 1;
    TX_PWCTRL_CHAN_OFFSET = (S8*)data_in + addr_offset[18] - 1;
    TXIQ_gain = (S8*)data_in + addr_offset[19] - 1;
    TXIQ_phase = (S8*)data_in + addr_offset[20] - 1;
    TXDC_i = (U8*)data_in + addr_offset[21] - 1;
    TXDC_q = (U8*)data_in + addr_offset[22] - 1;
    RXIQ_gain = (S8*)data_in + addr_offset[23] - 1;
    RXIQ_phase = (S8*)data_in + addr_offset[24] - 1;
    RXDC_c_i = (U8*)data_in + addr_offset[25] - 1;
    RXDC_c_q = (U8*)data_in + addr_offset[26] - 1;
    RXDC_f_i = (U8*)data_in + addr_offset[27] - 1;
    RXDC_f_q = (U8*)data_in + addr_offset[28] - 1;
    freq_offset_cal_total_pwr = (U8*)data_in + addr_offset[29] - 1;
    freq_offset_cal_bb_gain = (U8*)data_in + addr_offset[30] - 1;
    FREQ_OFFSET = (S8*)data_in + addr_offset[31] - 1;
    RX_PATH_SNR = (U8*)data_in + addr_offset[32] - 1;
    adc_dac_snr_2tone_gain = (U8*)data_in + addr_offset[33] - 1;
    adc_dac_snr_2tone_total_pwr = (U8*)data_in + addr_offset[34] - 1;
    ADC_DAC_SNR = (U8*)data_in + addr_offset[35] - 1;
    rx_switch_gain_check_bbrx1 = (U8*)data_in + addr_offset[36] - 1;
    rx_switch_gain_check_bbrx2 = (U8*)data_in + addr_offset[37] - 1;
    rx_switch_gain_check_total_pwr_db = (U8*)data_in + addr_offset[38] - 1;
    rx_switch_gain_check_sig_pwr_db = (U8*)data_in + addr_offset[39] - 1;
    rx_switch_gain_check_sw_g = (S8*)data_in + addr_offset[40] - 1;
    RX_SWITCH_GAIN = (S8*)data_in + addr_offset[41] - 1;
    dco_sweep_test_ADC_STEP = (S8*)data_in + addr_offset[42] - 1;
    dco_sweep_test_DCO = (U8*)data_in + addr_offset[43] - 1;
    rx_path_gain = (U8*)data_in + addr_offset[44] - 1;
    RX_NOISEFLOOR_14 = (U8*)data_in + addr_offset[45] - 1;
    rc_cal_dout = (U8*)data_in + addr_offset[46] - 1;
    rx_gain_check_tot_pwr = (U8*)data_in + addr_offset[47] - 1;
    rx_gain_check_sig_pwr = (U8*)data_in + addr_offset[48] - 1;  
    rxiq_tot_pwr = (U8*)data_in + addr_offset[49] - 1; 
    check_result = (U8*)data_in + addr_offset[50] - 1;
    RTC_freq_170khz = (U8*)data_in + addr_offset[51] - 1;
    RTC_freq_70khz = (U8*)data_in + addr_offset[52] - 1;
    svn_version = (U8*)data_in + addr_offset[53] - 1;
    TX_POCKET_TEST = (U8*)data_in + addr_offset[54] - 1;
    TX_POCKET_STATE = (U8*)data_in + addr_offset[55] - 1;
    RX_PARA_CAL = (U8*)data_in + addr_offset[56] - 1;
    RX_PARA_CAL_TONE = (U8*)data_in + addr_offset[57] - 1;
    wifi_init_time = (U8*)data_in + addr_offset[58] - 1;
    WIFI_INIT_ITEM = (U8*)data_in + addr_offset[59] - 1;
    RX_PARA_CAL_TONE_DATA_2 = (S8*)data_in + addr_offset[60] - 1; 
    TX_POCKET_REQ_TIMES = (U8*)data_in + addr_offset[61] - 1; 
    rom_bist_result = (U8*)data_in + addr_offset[62] - 1; 
    io_test_result = (U8*)data_in + addr_offset[63] - 1;
    rxiq_remain = (S8*)data_in + addr_offset[64] - 1;
    RXIQ_FREQ_TEST = (S8*)data_in + addr_offset[65] - 1;
    TX_POCKET_SITE_NUM = (U8*)data_in + addr_offset[66] - 1;
    rxiq_compute_num = (U8*)data_in + addr_offset[67] - 1;
    rxiq_cover_fail_num = (U8*)data_in + addr_offset[68] - 1;

//#if ate_check_print
    memset(printf_buf, 0, sizeof(printf_buf));
//#endif

    check_result_t = (check_result[3] << 8*3) | (check_result[2] << 8*2) | 
                     (check_result[1] << 8*1) | (check_result[0] << 8*0); 

    if (ate_check_print) PHY_PRINT("\nCHIP_VERSION: 0x%x\n", *CHIP_VERSION);
    CHIP_ID_t = (CHIP_ID[3] << 8*3) | (CHIP_ID[2] << 8*2) | (CHIP_ID[1] << 8*1) | (CHIP_ID[0] << 8*0);
    if (ate_check_print) PHY_PRINT("CHIP_ID: 0x%x\n", CHIP_ID_t);
    
    if (ate_check_print) PHY_PRINT("rc_cal_dout=%d\n", *rc_cal_dout);
    check_ate_data(*rc_cal_dout, ate_rc_cal_dout_LOW, ate_rc_cal_dout_HIGH, RC_CAL_ITEM);
    
    for(i=0; i<3; i++){
        if (ate_check_print) PHY_PRINT("rx_para_cal, ");
        for(j=0; j<7; j++){
            if (ate_check_print) PHY_PRINT("%d, ", RX_PARA_CAL[i*7+j]);
        }
        if (ate_check_print) PHY_PRINT("\n");
    }

    VDD33_t = (VDD33[1] << 8*1) | (VDD33[0] << 8*0);
    offset_t = (offset[1] << 8*1) | (offset[0] << 8*0);
    if (ate_check_print) PHY_PRINT("VDD33=%d, temp_code=%d, offset=%d\n", VDD33_t, *temp_code, offset_t);
    check_ate_data(VDD33_t, ate_VDD33_LOW, ate_VDD33_HIGH, VDD33_ITEM);

    if (ate_check_print) {
        PHY_PRINT("cal_rf_ana_gain, rf_gain=0x%x, ana_gain=0x%x, bb_atten=%d\n", 
                      cal_rf_ana_gain[0], cal_rf_ana_gain[1], cal_rf_ana_gain[2]);
    }
    
    if (ate_check_print) PHY_PRINT("TXBB_TXIQ, ");
    for(i=0; i<4; i++){
        if (ate_check_print) PHY_PRINT("%d, %d; ", TXBB_TXIQ_gain[i], TXBB_TXIQ_phase[i]);
        check_ate_data(TXBB_TXIQ_gain[i], ate_TXBB_TXIQ_LOW, ate_TXBB_TXIQ_HIGH, TXBB_TXIQ_ITEM);
        check_ate_data(TXBB_TXIQ_phase[i], ate_TXBB_TXIQ_LOW, ate_TXBB_TXIQ_HIGH, TXBB_TXIQ_ITEM);
    }
    if (ate_check_print) PHY_PRINT("\n");
        
    S8 *step;
    for(i=0; i<3; i++){
        step = &RX_GAIN_CHECK[i*14];
        if (ate_check_print) PHY_PRINT("RX_GAIN_CHECK, ");
        for(j=0; j<14; j++){
            if (ate_check_print) PHY_PRINT("%d, ", step[j]);
            check_ate_data(step[j], ate_RX_GAIN_CHECK_LOW_hdb[j], ate_RX_GAIN_CHECK_HIGH_hdb[j], RX_GAIN_CHECK_ITEM);
        }
        if (ate_check_print) PHY_PRINT("\n");
    }

    if (ate_check_print) {
        PHY_PRINT("rx_para_cal_tone, %d, 0x%x, 0x%x, %d, %d, %d, %d\n", RX_PARA_CAL_TONE[0], RX_PARA_CAL_TONE[1], RX_PARA_CAL_TONE[2], 
                   (S8)RX_PARA_CAL_TONE[3], RX_PARA_CAL_TONE[4], RX_PARA_CAL_TONE[5], RX_PARA_CAL_TONE[6]);

        PHY_PRINT("rx_para_cal_tone_sig_pwr_db_1, ");
        for(j=0; j<8; j++){
            PHY_PRINT("%d, ", RX_PARA_CAL_TONE_DATA_1[j]);
        }
        PHY_PRINT("\n");

        PHY_PRINT("rx_para_cal_tone_sig_pwr_db_2, ");
        for(j=0; j<8; j++){
            PHY_PRINT("%d, ", RX_PARA_CAL_TONE_DATA_1[j+8]);
        }
        PHY_PRINT("\n");

        PHY_PRINT("rx_para_cal_tone_sig_pwr_db_3, ");
        for(j=0; j<2; j++){
            PHY_PRINT("%d, ", RX_PARA_CAL_TONE_DATA_1[j+16]);
        }
        for(j=0; j<6; j++){
            PHY_PRINT("%d, ", RX_PARA_CAL_TONE_DATA_2[j+0]);
        }
        PHY_PRINT("\n");

        PHY_PRINT("rx_para_cal_tone_sig_pwr_db_4, ");
        for(j=0; j<8; j++){
            PHY_PRINT("%d, ", RX_PARA_CAL_TONE_DATA_2[j+6]);
        }
        PHY_PRINT("\n");
    }

    if (ate_check_print) PHY_PRINT("RX_GAIN_CHECK_POWER_hdb, ");
    for(i=0; i<15; i++){
        if (ate_check_print) PHY_PRINT("%d, %d; ", rx_gain_check_tot_pwr[i], rx_gain_check_sig_pwr[i]);
    }
    if (ate_check_print) PHY_PRINT("\n");

    if (ate_check_print) PHY_PRINT("BBRX2_RXIQ, ");
    for(i=0; i<6; i++){
        if (ate_check_print) PHY_PRINT("%d, %d; ", BBRX2_RXIQ_gain[i], BBRX2_RXIQ_phase[i]);
        check_ate_data(BBRX2_RXIQ_gain[i], ate_BBRX2_RXIQ_LOW, ate_BBRX2_RXIQ_HIGH, BBRX2_RXIQ_ITEM);
        check_ate_data(BBRX2_RXIQ_phase[i], ate_BBRX2_RXIQ_LOW, ate_BBRX2_RXIQ_HIGH, BBRX2_RXIQ_ITEM);
    }
    if (ate_check_print) PHY_PRINT("\n");
    
    int noisefloor_min;
    for(i=0; i<2; i++){
        RX_NOISEFLOOR_t[i] = (RX_NOISEFLOOR[i*2+1] << 8*1) | (RX_NOISEFLOOR[i*2+0] << 8*0);
        if (ate_check_print) PHY_PRINT("RX_NOISEFLOOR, %d\n", RX_NOISEFLOOR_t[i]);
    }
    if((RX_NOISEFLOOR_t[0]) < RX_NOISEFLOOR_t[1])
        noisefloor_min = RX_NOISEFLOOR_t[0];
    else
        noisefloor_min = RX_NOISEFLOOR_t[1];
    check_ate_data(noisefloor_min, ate_RX_NOISEFLOOR_LOW, ate_RX_NOISEFLOOR_HIGH, RX_NOISEFLOOR_ITEM);
    
    if (ate_check_print) PHY_PRINT("TXCAP_TMX2G_CCT_LOAD, ");
    for(i=0; i<3; i++){
        if (ate_check_print) PHY_PRINT("%d, ", TXCAP_TMX2G_CCT_LOAD[i]);
        check_ate_data(TXCAP_TMX2G_CCT_LOAD[i], ate_TXCAP_TMX2G_CCT_LOAD_LOW, ate_TXCAP_TMX2G_CCT_LOAD_HIGH, TXCAP_ITEM);
    }
    if (ate_check_print) PHY_PRINT("\n");
   
    if (ate_check_print) PHY_PRINT("TXCAP_PA2G_CCT_STG1, ");
    for(i=0; i<3; i++){
        if (ate_check_print) PHY_PRINT("%d, ", TXCAP_PA2G_CCT_STG1[i]);
        check_ate_data(TXCAP_PA2G_CCT_STG1[i], ate_TXCAP_PA2G_CCT_STG1_LOW, ate_TXCAP_PA2G_CCT_STG1_HIGH, TXCAP_ITEM);
    }
    if (ate_check_print) PHY_PRINT("\n");
   
    if (ate_check_print) PHY_PRINT("TXCAP_PA2G_CCT_STG2, ");
    for(i=0; i<3; i++){
        if (ate_check_print) PHY_PRINT("%d, ", TXCAP_PA2G_CCT_STG2[i]);
        check_ate_data(TXCAP_PA2G_CCT_STG2[i], ate_TXCAP_PA2G_CCT_STG2_LOW, ate_TXCAP_PA2G_CCT_STG2_HIGH, TXCAP_ITEM);
    }
    if (ate_check_print) PHY_PRINT("\n");
   
    if (ate_check_print) PHY_PRINT("TX_PWRCTRL_ATTEN, ");
    for(i=0; i<6; i++){
        if (ate_check_print) PHY_PRINT("%d, ", TX_PWRCTRL_ATTEN[i]);
        //check_ate_data(TX_PWRCTRL_ATTEN[i], ate_TX_PWCTRL_ATTEN_LOW_qdb[i], ate_TX_PWCTRL_ATTEN_HIGH_qdb[i], TX_PWCTRL_ATTEN_ITEM);
    }
    if (ate_check_print) PHY_PRINT("\n");
   
    if (ate_check_print) PHY_PRINT("TX_PWCTRL_CHAN_OFFSET, ");
    for(i=0; i<14; i++){
        if (ate_check_print) PHY_PRINT("%d, ", TX_PWCTRL_CHAN_OFFSET[i]);
        //check_ate_data(TX_PWCTRL_CHAN_OFFSET[i], ate_TX_PWCTRL_CHAN_OFFSET_LOW_qdb, ate_TX_PWCTRL_CHAN_OFFSET_HIGH_qdb, TX_PWCTRL_CHAN_OFFSET_ITEM);
    }
    if (ate_check_print) PHY_PRINT("\n");
    
    if((check_result_t >> TXIQ_Convergence_ITEM) & 0x1){
        if (*TXIQ_gain > 0) *TXIQ_gain = 16;
        else *TXIQ_gain = -16;
        if (*TXIQ_phase > 0) *TXIQ_phase = 32;
        else *TXIQ_phase = -32;
    }
    if (ate_check_print) PHY_PRINT("TXIQ, %d, %d\n", *TXIQ_gain, *TXIQ_phase);
    check_ate_data(*TXIQ_gain, ate_TXIQ_GAIN_LOW, ate_TXIQ_GAIN_HIGH, TXIQ_ITEM);
    check_ate_data(*TXIQ_phase, ate_TXIQ_PHASE_LOW, ate_TXIQ_PHASE_HIGH, TXIQ_ITEM);
    
    if (ate_check_print) PHY_PRINT("TXDC, ");
    for(i=0; i<4; i++){
        if (ate_check_print) PHY_PRINT("%d, %d; ", TXDC_i[i], TXDC_q[i]);
        check_ate_data(TXDC_i[i], ate_TXDC_LOW, ate_TXDC_HIGH, TXDC_ITEM);
        check_ate_data(TXDC_q[i], ate_TXDC_LOW, ate_TXDC_HIGH, TXDC_ITEM);
    }
    if (ate_check_print) PHY_PRINT("\n");

    if (ate_check_print) PHY_PRINT("RXIQ_TEST_-5M: %d, %d\n", RXIQ_FREQ_TEST[2], RXIQ_FREQ_TEST[3]); 
    if (ate_check_print) PHY_PRINT("RXIQ_TEST_5M: %d, %d\n", RXIQ_FREQ_TEST[0], RXIQ_FREQ_TEST[1]);
    check_ate_data(RXIQ_FREQ_TEST[2]-RXIQ_FREQ_TEST[0], RXIQ_5M_SUB_LOW, RXIQ_5M_SUB_HIGH, RXIQ_5M_SUB_ITEM);
    check_ate_data(RXIQ_FREQ_TEST[3]-RXIQ_FREQ_TEST[1], RXIQ_5M_SUB_LOW, RXIQ_5M_SUB_HIGH, RXIQ_5M_SUB_ITEM);

    if (ate_check_print) PHY_PRINT("RXIQ, ");
    for(i=0; i<5; i++){
        if (ate_check_print) PHY_PRINT("%d, %d; ", RXIQ_gain[i], RXIQ_phase[i]);
        check_ate_data(RXIQ_gain[i], ate_RXIQ_GAIN_LOW, ate_RXIQ_GAIN_HIGH, RXIQ_ITEM);
        check_ate_data(RXIQ_phase[i], ate_RXIQ_PHASE_LOW, ate_RXIQ_PHASE_HIGH, RXIQ_ITEM);
    }
    if (ate_check_print) PHY_PRINT("\n");

    if (ate_check_print) PHY_PRINT("RXIQ_tot_power, %ddB\n", *rxiq_tot_pwr);    
    
    U32 rxiq_compute_num_t;
    rxiq_compute_num_t = (rxiq_compute_num[3] << 8*3) | (rxiq_compute_num[2] << 8*2) | 
                                               (rxiq_compute_num[1] << 8*1) | (rxiq_compute_num[0] << 8*0);
    if (ate_check_print){ 
        PHY_PRINT("rxiq_cover_fail_num=%d\n", *rxiq_cover_fail_num);
        PHY_PRINT("rxiq_compute_num: ");
        for(i=0; i<13; i++){
            PHY_PRINT("%d,", (rxiq_compute_num_t>>(i*2))&0x3);
        }
        PHY_PRINT("\n");
    }
    check_ate_data(*rxiq_cover_fail_num, RXIQ_COVER_FAIL_NUM_LOW, RXIQ_COVER_FAIL_NUM_HIGH, RXIQ_COVER_FAIL_NUM_ITEM);
    
    if (ate_check_print) PHY_PRINT("RXDC, ");
    for(i=0; i<30; i++){
        RXDC_c_i_t[i] = RXDC_c_i[i] << 2;
        RXDC_c_q_t[i] = RXDC_c_q[i] << 2;
        RXDC_f_i_t[i] = RXDC_f_i[i] << 2;
        RXDC_f_q_t[i] = RXDC_f_q[i] << 2;
        check_ate_data(RXDC_c_i_t[i], ate_RXDC_LOW, ate_RXDC_HIGH, RXDC_ITEM);
        check_ate_data(RXDC_c_q_t[i], ate_RXDC_LOW, ate_RXDC_HIGH, RXDC_ITEM);
        check_ate_data(RXDC_f_i_t[i], ate_RXDC_LOW, ate_RXDC_HIGH, RXDC_ITEM);
        check_ate_data(RXDC_f_q_t[i], ate_RXDC_LOW, ate_RXDC_HIGH, RXDC_ITEM);
        if (ate_check_print) PHY_PRINT("%d, %d, %d, %d; ", RXDC_c_i_t[i], RXDC_c_q_t[i], RXDC_f_i_t[i], RXDC_f_q_t[i]);
    }
    if (ate_check_print) PHY_PRINT("\n");

    freq_offset_cal_total_pwr_t = (freq_offset_cal_total_pwr[3] << 8*3) | (freq_offset_cal_total_pwr[2] << 8*2) | 
                                               (freq_offset_cal_total_pwr[1] << 8*1) | (freq_offset_cal_total_pwr[0] << 8*0);
    if (ate_check_print) PHY_PRINT("freq_offset_cal, bb_gain=%d, total_pwr=%d\n", *freq_offset_cal_bb_gain, freq_offset_cal_total_pwr_t);
    if (ate_check_print) PHY_PRINT("RX_PATH_GAIN, %ddB\n", *rx_path_gain);
    check_ate_data(*rx_path_gain, ate_RX_PATH_GAIN_LOW_db, ate_RX_PATH_GAIN_HIGH_db, RX_PATH_GAIN_ITEM);
    
    check_ate_data(*FREQ_OFFSET, ate_FREQ_OFFSET_LOW_ppm, ate_FREQ_OFFSET_HIGH_ppm, FREQ_OFFSET_ITEM);
    if (ate_check_print) PHY_PRINT("FREQ_OFFSET, %dPPM\n", *FREQ_OFFSET);
    
    RX_PATH_SNR_t = (RX_PATH_SNR[1] << 8*1) | (RX_PATH_SNR[0] << 8*0);
    check_ate_data(RX_PATH_SNR_t, ate_RX_PATH_SNR_LOW_db, ate_RX_PATH_SNR_HIGH_db, RX_PATH_SNR_ITEM);
    
    if (ate_check_print) PHY_PRINT("RX_PATH_SNR, %ddB\n", RX_PATH_SNR_t);

    if (ate_check_print) PHY_PRINT("RXIQ_REMAIN, %ddB\n", *rxiq_remain);
    check_ate_data(*rxiq_remain, RXIQ_REMAIN_DB_LOW, RXIQ_REMAIN_DB_HIGH, RXIQ_REMAIN_ITEM);

    adc_dac_snr_2tone_total_pwr_t = (adc_dac_snr_2tone_total_pwr[3] << 8*3) | (adc_dac_snr_2tone_total_pwr[2] << 8*2) | 
                                    (adc_dac_snr_2tone_total_pwr[1] << 8*1) | (adc_dac_snr_2tone_total_pwr[0] << 8*0);
    
    if (ate_check_print) {
        PHY_PRINT("adc_dac_snr_2tone, bbrx1=0x%x, bbrx2=0x%x, tone_atten=%d: total_pwr=%d\n", 
                       adc_dac_snr_2tone_gain[0], adc_dac_snr_2tone_gain[1], 
                       adc_dac_snr_2tone_gain[2], adc_dac_snr_2tone_total_pwr_t);
    }
    
    check_ate_data(*ADC_DAC_SNR, ate_ADC_DAC_SNR_LOW_db, ate_ADC_DAC_SNR_HIGH_db, ADC_DAC_SNR_ITEM);
    if (ate_check_print) PHY_PRINT("ADC_DAC_SNR, %ddB\n", *ADC_DAC_SNR);

    if (ate_check_print) PHY_PRINT("rx_switch_gain_check: ");
    for (i=0; i<5; i++){
        rx_switch_gain_check_bbrx1_t[i] = (rx_switch_gain_check_bbrx1[i*2+1] << 8*1) | (rx_switch_gain_check_bbrx1[i*2+0] << 8*0);
        rx_switch_gain_check_bbrx2_t[i] = (rx_switch_gain_check_bbrx2[i*2+1] << 8*1) | (rx_switch_gain_check_bbrx2[i*2+0] << 8*0);
        if (ate_check_print) {
            PHY_PRINT("0x%x, ", rx_switch_gain_check_bbrx1_t[i]);
            PHY_PRINT("0x%x, ", rx_switch_gain_check_bbrx2_t[i]);
            PHY_PRINT("%d, ", rx_switch_gain_check_total_pwr_db[i]);
            PHY_PRINT("%d, ", rx_switch_gain_check_sig_pwr_db[i]);
            PHY_PRINT("%d; ", rx_switch_gain_check_sw_g[i]);
        }
    }
    if (ate_check_print) PHY_PRINT("\n");

    if (ate_check_print) PHY_PRINT("RX_SWITCH_GAIN: %d, %d, %d\n", RX_SWITCH_GAIN[0], RX_SWITCH_GAIN[1], RX_SWITCH_GAIN[2]);
    check_ate_data(RX_SWITCH_GAIN[0], ate_RX_SWITCH_GAIN_LOW_db[0], ate_RX_SWITCH_GAIN_HIGH_db[0], RX_SWITCH_GAIN_ITEM);
    check_ate_data(RX_SWITCH_GAIN[1], ate_RX_SWITCH_GAIN_LOW_db[1], ate_RX_SWITCH_GAIN_HIGH_db[1], RX_SWITCH_GAIN_ITEM);
    check_ate_data(RX_SWITCH_GAIN[2], ate_RX_SWITCH_GAIN_LOW_db[2], ate_RX_SWITCH_GAIN_HIGH_db[2], RX_SWITCH_GAIN_ITEM);

    if (ate_check_print) {
        PHY_PRINT("dco_sweep_test_ADC_STEP, %d, %d; %d, %d\n", 
            dco_sweep_test_ADC_STEP[0], dco_sweep_test_ADC_STEP[1], 
            dco_sweep_test_ADC_STEP[2], dco_sweep_test_ADC_STEP[3]);
    }
    check_ate_data(dco_sweep_test_ADC_STEP[0], ate_dco_sweep_test_ADC_STEP_LOW, ate_dco_sweep_test_ADC_STEP_HIGH, ADC_STEP_ITEM);
    check_ate_data(dco_sweep_test_ADC_STEP[1], ate_dco_sweep_test_ADC_STEP_LOW, ate_dco_sweep_test_ADC_STEP_HIGH, ADC_STEP_ITEM);
    check_ate_data(dco_sweep_test_ADC_STEP[2], ate_dco_sweep_test_ADC_STEP_LOW, ate_dco_sweep_test_ADC_STEP_HIGH, ADC_STEP_ITEM);
    check_ate_data(dco_sweep_test_ADC_STEP[3], ate_dco_sweep_test_ADC_STEP_LOW, ate_dco_sweep_test_ADC_STEP_HIGH, ADC_STEP_ITEM);
    
    for(i=0; i<4; i++){
        dco_sweep_test_DCO_t[i] = (dco_sweep_test_DCO[i*2+1] << 8*1) | (dco_sweep_test_DCO[i*2+0] << 8*0);
    }   
    
    if (ate_check_print) {
        PHY_PRINT("dco_sweep_test_DCO, %d, %d; %d, %d\n", 
            dco_sweep_test_DCO_t[0], dco_sweep_test_DCO_t[1], 
            dco_sweep_test_DCO_t[2], dco_sweep_test_DCO_t[3]);
    }
    check_ate_data(dco_sweep_test_DCO_t[0], dco_sweep_test_DCO_t[0], dco_sweep_test_DCO_t[1], DCO_HIGH_LOW_ITEM);
    check_ate_data(dco_sweep_test_DCO_t[2], dco_sweep_test_DCO_t[2], dco_sweep_test_DCO_t[3], DCO_HIGH_LOW_ITEM);

    if (ate_check_print) PHY_PRINT("rombist_rslt=%d\n", *rom_bist_result);
    check_ate_data(*rom_bist_result, 0, 0, ROM_BIST_ITEM);

    if (ate_check_print) PHY_PRINT("timeout_fail=%d, check_fail=%d, chip_id_crc_fail=%d\n",
            (TX_POCKET_TEST[25] >> 0) & 0x1, (TX_POCKET_TEST[25] >> 1) & 0x1, (TX_POCKET_TEST[25] >> 2) & 0x1);
    check_ate_data((TX_POCKET_TEST[25] >> 2) & 0x1, 0, 0, CHIP_ID_CRC_ITEM);

    check_ate_data(CHIP_ID_t==0, 0, 0, CHIP_ID_CRC_ITEM);

    if (ate_check_print) PHY_PRINT("txp_pwctrl_atten, %d\n", TX_POCKET_TEST[0]);

    if (ate_check_print) PHY_PRINT("site_num, %d; req_suc, %d; req_times, %d; dut_txseq, %d\n", (*TX_POCKET_SITE_NUM)&0xf, ((*TX_POCKET_SITE_NUM) >> 7)&1, TX_POCKET_REQ_TIMES[0], TX_POCKET_REQ_TIMES[1]);

    if (ate_check_print) PHY_PRINT("fb_rxrssi, ");
    for(i=0; i<6; i++){
        if (ate_check_print) PHY_PRINT("%d, ", TX_POCKET_TEST[1+i*2]);
    }
    if (ate_check_print) PHY_PRINT("\n");
    check_ate_data(TX_POCKET_TEST[1+5*2], FB_RXRSSI_LOW, FB_RXRSSI_HIGH, FB_RXRSSI_ITEM);

    if (ate_check_print) PHY_PRINT("dut_rxrssi, ");
    for(i=0; i<6; i++){
        if (ate_check_print) PHY_PRINT("%d, ", TX_POCKET_TEST[2+i*2]);
    }
    if (ate_check_print) PHY_PRINT("\n");
    check_ate_data(TX_POCKET_TEST[2+5*2], DUT_RXRSSI_LOW, DUT_RXRSSI_HIGH, DUT_RXRSSI_ITEM);

    U8 fb_rx_num_sum = 0, dut_rx_num_sum = 0, dut_rx_lost = 0, fb_rx_num_max = 0;
    if (ate_check_print) PHY_PRINT("fb_rx_num, ");
    for(i=0; i<6; i++){
        fb_rx_num_sum += TX_POCKET_TEST[13+i*2];
        if (ate_check_print) PHY_PRINT("%d, ", TX_POCKET_TEST[13+i*2]);
        if(fb_rx_num_max < TX_POCKET_TEST[13+i*2]) fb_rx_num_max = TX_POCKET_TEST[13+i*2];
    }
    if (ate_check_print) PHY_PRINT("\n");
    check_ate_data(fb_rx_num_max, FB_RX_NUM_LOW, FB_RX_NUM_HIGH, FB_RX_NUM_ITEM);
    check_ate_data(fb_rx_num_sum, FB_RX_NUM_SUM_LOW, FB_RX_NUM_SUM_HIGH, FB_RX_NUM_SUM_ITEM);

    if (ate_check_print) PHY_PRINT("dut_rx_num, ");
    for(i=0; i<6; i++){
        dut_rx_num_sum += TX_POCKET_TEST[14+i*2];
        if (ate_check_print) PHY_PRINT("%d, ", TX_POCKET_TEST[14+i*2]);
    }
    dut_rx_lost = fb_rx_num_sum - dut_rx_num_sum;
    check_ate_data(dut_rx_lost, DUT_RX_LOST_LOW, DUT_RX_LOST_HIGH, DUT_RX_LOST_ITEM);

    if (ate_check_print) PHY_PRINT("\n");
   
    for(i=0; i<6; i++){
        TX_POCKET_STATE_t[i] = (TX_POCKET_STATE[i*4+3] << 8*3) | (TX_POCKET_STATE[i*4+2] << 8*2) | (TX_POCKET_STATE[i*4+1] << 8*1) | (TX_POCKET_STATE[i*4+0] << 8*0);
    }
    if (ate_check_print) PHY_PRINT("txp_state: 0x%08x%08x%08x, 0x%08x%08x%08x;\n", TX_POCKET_STATE_t[2],TX_POCKET_STATE_t[1],TX_POCKET_STATE_t[0],
                                                                           TX_POCKET_STATE_t[5],TX_POCKET_STATE_t[4],TX_POCKET_STATE_t[3]);
    if (ate_check_print) PHY_PRINT("fb_rx_num_sum=%d, dut_rx_lost=%d\n", fb_rx_num_sum, dut_rx_lost);

    if (ate_check_print) PHY_PRINT("txreq_start_time=0x%x\n", (TX_POCKET_TEST[29] << 8*3) | (TX_POCKET_TEST[28] << 8*2) | 
                                                              (TX_POCKET_TEST[27] << 8*1) | (TX_POCKET_TEST[26] << 8*0));

    ate_check_result = ate_check_result & result_mask;
    if (ate_check_print) PHY_PRINT("check_result_t=0x%x, ate_check_result=0x%x\n", check_result_t, ate_check_result); 

    if (ate_check_print) PHY_PRINT("RTC_freq_170khz=%d\n", *RTC_freq_170khz);
    check_ate_data(*RTC_freq_170khz, ate_RTC_freq_170khz_LOW, ate_RTC_freq_170khz_HIGH, RTC_FREQ_ITEM);

    if (ate_check_print) PHY_PRINT("RTC_freq_70khz=%d\n", *RTC_freq_70khz);
    check_ate_data(*RTC_freq_70khz, ate_RTC_freq_70khz_LOW, ate_RTC_freq_70khz_HIGH, RTC_FREQ_ITEM);

    if (ate_check_print) PHY_PRINT("io_test_result=%d\n", (*io_test_result)&0x1);
    check_ate_data((*io_test_result)&0x1, 0, 0, IO_TEST_ITEM);

    wifi_init_time_t = (wifi_init_time[3] << 8*3) | (wifi_init_time[2] << 8*2) | 
                       (wifi_init_time[1] << 8*1) | (wifi_init_time[0] << 8*0); 
    if (ate_check_print) PHY_PRINT("wifi_init_time: %dus\n", wifi_init_time_t);

    WIFI_INIT_ITEM_t = (WIFI_INIT_ITEM[3] << 8*3) | (WIFI_INIT_ITEM[2] << 8*2) | 
                       (WIFI_INIT_ITEM[1] << 8*1) | (WIFI_INIT_ITEM[0] << 8*0); 
    if (ate_check_print) PHY_PRINT("WIFI_INIT_ITEM: 0x%x\n", WIFI_INIT_ITEM_t);

    svn_version_t = (svn_version[1] << 8*1) | (svn_version[0] << 8*0);
    if (ate_check_print) PHY_PRINT("SVN_Version: %d\n", svn_version_t); 

    if (ate_check_print) {
/*
        PHY_PRINT("\n\n--------------------------------------------------------\n");
        if (check_result_t > 0){
            PHY_PRINT("---------------CHECK BOARD FAIL----------------\nBecause:");
            for (i=0; i<32; i++){
                if (check_result_t & (1 << i)){
                    switch(i){
                        case TX_PWCTRL_ATTEN_ITEM: PHY_PRINT("TX_PWRCTRL_ATTEN FAIL, "); break;
                        case TXIQ_ITEM: PHY_PRINT("TXIQ FAIL, "); break;
                        case RXIQ_ITEM: PHY_PRINT("RXIQ FAIL, "); break;
                        case TXDC_ITEM: PHY_PRINT("TXDC FAIL, "); break;
                        case RXIQ_REMAIN_ITEM: PHY_PRINT("RXIQ_REMAIN FAIL, "); break;
                        case RXDC_ITEM: PHY_PRINT("RXDC FAIL, "); break;
                        case RX_GAIN_CHECK_ITEM: PHY_PRINT("RX_GAIN_CHECK FAIL, "); break;
                        case RX_NOISEFLOOR_ITEM: PHY_PRINT("RX_NOISEFLOOR FAIL, "); break;
                        case ADC_DAC_SNR_ITEM: PHY_PRINT("ADC_DAC_SNR FAIL, "); break;
                        case FREQ_OFFSET_ITEM: PHY_PRINT("FREQ_OFFSET FAIL, "); break;
                        case RX_PATH_SNR_ITEM: PHY_PRINT("RX_PATH_SNR FAIL, "); break;
                        case SDIO_PAD_ITEM: PHY_PRINT("SDIO_PAD FAIL, "); break;
                        case TX_PWCTRL_CHAN_OFFSET_ITEM: PHY_PRINT("TX_PWCTRL_CHAN_OFFSET FAIL, "); break;
                        case TXIQ_Convergence_ITEM: PHY_PRINT("TXIQ_Convergence FAIL, "); break;
                        case RXIQ_Convergence_ITEM: PHY_PRINT("RXIQ_Convergence FAIL, "); break;
                        case BBRX2_RXIQ_ITEM: PHY_PRINT("BBRX2_RXIQ FAIL, "); break;
                        case TXBB_TXIQ_ITEM: PHY_PRINT("TXBB_TXIQ FAIL, "); break;
                        case RX_PATH_GAIN_ITEM: PHY_PRINT("RX_PATH_GAIN FAIL, "); break;
                        case ADC_STEP_ITEM: PHY_PRINT("ADC_STEP FAIL, "); break;
                        case DCO_HIGH_LOW_ITEM: PHY_PRINT("DCO_HIGH_LOW FAIL, "); break;
                        case RX_SWITCH_GAIN_ITEM: PHY_PRINT("RX_SWITCH_GAIN FAIL, "); break;
                        case VDD33_ITEM: PHY_PRINT("VDD33 FAIL, "); break;
                        case temp_code_ITEM: PHY_PRINT("temp_code FAIL, "); break;
                        case TXCAP_ITEM: PHY_PRINT("TXCAP FAIL, "); break;
                        case RC_CAL_ITEM: PHY_PRINT("RC_CAL FAIL, "); break;
                        case ROM_BIST_ITEM: PHY_PRINT("ROM_BIST FAIL, "); break;
                        case CHIP_ID_CRC_ITEM: PHY_PRINT("CHIP_ID_CRC FAIL, "); break; 
                        default: break;
                    }
                }
            }            
            PHY_PRINT("\n");
        }else{
            PHY_PRINT("---------------CHECK BOARD PASS----------------\n");
        }
        PHY_PRINT("--------------------------------------------------------\n\n\n");   
*/
        PHY_PRINT("\n\n--------------------------------------------------------\n");
        if (ate_check_result > 0){
            PHY_PRINT("---------------CHECK BOARD FAIL----------------\nBecause:");
            for (i=0; i<32; i++){
                if (ate_check_result & (1 << i)){
                    switch(i){
                        case TX_PWCTRL_ATTEN_ITEM: PHY_PRINT("TX_PWRCTRL_ATTEN FAIL, "); break;
                        case TXIQ_ITEM: PHY_PRINT("TXIQ FAIL, "); break;
                        case RXIQ_ITEM: PHY_PRINT("RXIQ FAIL, "); break;
                        case TXDC_ITEM: PHY_PRINT("TXDC FAIL, "); break;
                        case RXIQ_REMAIN_ITEM: PHY_PRINT("RXIQ_REMAIN FAIL, "); break;
                        case RXDC_ITEM: PHY_PRINT("RXDC FAIL, "); break;
                        case RX_GAIN_CHECK_ITEM: PHY_PRINT("RX_GAIN_CHECK FAIL, "); break;
                        case RX_NOISEFLOOR_ITEM: PHY_PRINT("RX_NOISEFLOOR FAIL, "); break;
                        case ADC_DAC_SNR_ITEM: PHY_PRINT("ADC_DAC_SNR FAIL, "); break;
                        case FREQ_OFFSET_ITEM: PHY_PRINT("FREQ_OFFSET FAIL, "); break;
                        case RX_PATH_SNR_ITEM: PHY_PRINT("RX_PATH_SNR FAIL, "); break;
                        case SDIO_PAD_ITEM: PHY_PRINT("SDIO_PAD FAIL, "); break;
                        //case TX_PWCTRL_CHAN_OFFSET_ITEM: PHY_PRINT("TX_PWCTRL_CHAN_OFFSET FAIL, "); break;
                        case FB_RXRSSI_ITEM: PHY_PRINT("FB_RXRSSI FAIL, "); break;
                        case DUT_RXRSSI_ITEM: PHY_PRINT("DUT_RXRSSI FAIL, "); break;
                        case BBRX2_RXIQ_ITEM: PHY_PRINT("BBRX2_RXIQ FAIL, "); break;
                        case TXBB_TXIQ_ITEM: PHY_PRINT("TXBB_TXIQ FAIL, "); break;
                        case RX_PATH_GAIN_ITEM: PHY_PRINT("RX_PATH_GAIN FAIL, "); break;
                        case ADC_STEP_ITEM: PHY_PRINT("ADC_STEP FAIL, "); break;
                        case DCO_HIGH_LOW_ITEM: PHY_PRINT("DCO_HIGH_LOW FAIL, "); break;
                        case RXIQ_COVER_FAIL_NUM_ITEM: PHY_PRINT("rxiq_cover_fail_num FAIL, "); break;
                        case RX_SWITCH_GAIN_ITEM: PHY_PRINT("RX_SWITCH_GAIN FAIL, "); break;
                        case VDD33_ITEM: PHY_PRINT("VDD33 FAIL, "); break;
                        case RXIQ_5M_SUB_ITEM: PHY_PRINT("RXIQ_5M_SUB FAIL, "); break;
                        case TXCAP_ITEM: PHY_PRINT("TXCAP FAIL, "); break;
                        case RC_CAL_ITEM: PHY_PRINT("RC_CAL FAIL, "); break;
                        case ROM_BIST_ITEM: PHY_PRINT("ROM_BIST FAIL, "); break;
                        case FB_RX_NUM_ITEM: PHY_PRINT("FB_RX_NUM FAIL, "); break;
                        case FB_RX_NUM_SUM_ITEM: PHY_PRINT("FB_RX_NUM_SUM FAIL, "); break;
                        case DUT_RX_LOST_ITEM: PHY_PRINT("DUT_RX_LOST FAIL, "); break;
                        case CHIP_ID_CRC_ITEM: PHY_PRINT("CHIP_ID_CRC FAIL, "); break; 
                        case IO_TEST_ITEM: PHY_PRINT("IO_TEST FAIL, "); break;
                        case RTC_FREQ_ITEM: PHY_PRINT("RTC_FREQ FAIL, "); break;
                        default: break;
                    }
                }
            }    
            PHY_PRINT("\n");
        }else{
            PHY_PRINT("---------------CHECK BOARD PASS----------------\n");
        }
        PHY_PRINT("--------------------------------------------------------\n\n\n");           
    }

#if ate_check_print
    PHY_PRINT("DVDD_testV1 = %f\n",DVDD_testV_1[sitenum]);
    PHY_PRINT("VDD_RTC_testV1 = %f\n",VDD_RTC_testV_1[sitenum]);
    PHY_PRINT("DVDD_testV2 = %f\n",DVDD_testV_2[sitenum]);
    PHY_PRINT("VDD_RTC_testV2 = %f\n",VDD_RTC_testV_2[sitenum]);
    PHY_PRINT("LightSleep_IDD_VBAT = %f\n",LightSleep_IDD_VBAT[sitenum]);
    PHY_PRINT("LightSleep_IDD_DVDD_IO = %f\n",LightSleep_IDD_DVDD_IO[sitenum]);
    PHY_PRINT("Chip_PD_IDD_VBAT = %f\n",Chip_PD_IDD_VBAT[sitenum]);
    PHY_PRINT("Chip_PD_IDD_DVDD_IO = %f\n",Chip_PD_IDD_DVDD_IO[sitenum]);
    PHY_PRINT("AnaWorkIDD_VBAT = %f\n",DynamicIDD_VBAT[sitenum]);
    PHY_PRINT("AnaWorkIDD_DVDD_IO = %f\n",DynamicIDD_DVDD_IO[sitenum]);
#endif

#ifndef CONVERT_EN
    U8 *din;
    din = (U8*)data_in;
    for(i=0; i<512; i++){
        PHY_PRINT("%02x\n", din[i]);
    }

    PHY_PRINT("%f\n",DVDD_testV_1[sitenum]);
    PHY_PRINT("%f\n",VDD_RTC_testV_1[sitenum]);
    PHY_PRINT("%f\n",DVDD_testV_2[sitenum]);
    PHY_PRINT("%f\n",VDD_RTC_testV_2[sitenum]);
    PHY_PRINT("%f\n",LightSleep_IDD_VBAT[sitenum]);
    PHY_PRINT("%f\n",LightSleep_IDD_DVDD_IO[sitenum]);
    PHY_PRINT("%f\n",Chip_PD_IDD_VBAT[sitenum]);
    PHY_PRINT("%f\n",Chip_PD_IDD_DVDD_IO[sitenum]);
    PHY_PRINT("%f\n",DynamicIDD_VBAT[sitenum]);
    PHY_PRINT("%f\n",DynamicIDD_DVDD_IO[sitenum]);
#endif

#ifndef CONVERT_EN
//   cscExec->Datalog()->printf("%s", printf_buf);
    char filename[64];
    char time[64];
    const time_t t = std::time(NULL);
    struct tm* current_time = localtime(&t);

    //sprintf(filename, "../datalog/Site%d_chip_id_%x_%d%02d%02d_%02d%02d%02d.log", sitenum+1, CHIP_ID_t, 1900 + current_time->tm_year, 1 + current_time->tm_mon,  current_time->tm_mday, current_time->tm_hour, current_time->tm_min, current_time->tm_sec);
    //sprintf(filename, "/usr/local/home/test/datalog/124_chip_id/Site%d_chip_id_%x_%d%02d%02d_%02d%02d%02d.log",sitenum+1, CHIP_ID_t, 1900 + current_time->tm_year, 1 + current_time->tm_mon,  current_time->tm_mday, current_time->tm_hour, current_time->tm_min, current_time->tm_sec);
    sprintf(filename, "/usr/local/home/prod/PROD_DATA/ESP/datalog/Site%d_chip_id_%x_%d%02d%02d_%02d%02d%02d.log", sitenum+1, CHIP_ID_t, 1900 + current_time->tm_year, 1 + current_time->tm_mon,  current_time->tm_mday, current_time->tm_hour, current_time->tm_min, current_time->tm_sec);

    ofstream outIDFile;
    outIDFile.open(filename,ios::out);
    if(!outIDFile) {
        cerr<<"File can't be opened\n";
        exit(1);
    }
    outIDFile<<printf_buf<<endl;
    outIDFile.close();
#else
    char filename[64];
    /*
	   char time[64];
	   const time_t t = std::time(NULL);
	   struct tm* current_time = localtime(&t);
	   */

	   sprintf(filename, "./%s",log_name );

		ofstream outIDFile;
		outIDFile.open(filename,ios::out);
		if(!outIDFile) {
			cerr<<"File can't be opened\n";
			cin.get();cin.get();
			exit(1);
		}
		outIDFile<<printf_buf<<endl;
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


    return (ate_check_result > 0);

}
