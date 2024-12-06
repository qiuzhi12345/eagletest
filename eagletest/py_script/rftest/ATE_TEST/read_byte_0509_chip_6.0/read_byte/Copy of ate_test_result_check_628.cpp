

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


S8 ate_RX_GAIN_CHECK_LOW_hdb[14] = { 15, -28, 14, -6, -6, -4,  6, -4, -4, -4, -4, -4, -4, -4};
S8 ate_RX_GAIN_CHECK_HIGH_hdb[14] = {25, -17, 24,  6,  6,  4, 16,  4,  4,  4,  4,  4,  4,  4};

S8 ate_TX_PWCTRL_ATTEN_LOW_qdb[6] = {-14, -8, 9, 15, 25, 33}; //{-6, -4, 0, 4, 8, 12};
S8 ate_TX_PWCTRL_ATTEN_HIGH_qdb[6] = {20, 26, 35, 41, 51, 59}; //{14, 16, 20, 24, 28, 32};

S8 ate_RX_SWITCH_GAIN_HIGH_db[3] = {6, -4, 8};
S8 ate_RX_SWITCH_GAIN_LOW_db[3] = {-2, -11, 1};

#define ate_RX_NOISEFLOOR_HIGH -380
#define ate_RX_NOISEFLOOR_LOW  -396

#define ate_TX_PWCTRL_CHAN_OFFSET_HIGH_qdb  10
#define ate_TX_PWCTRL_CHAN_OFFSET_LOW_qdb  -10

#define ate_TXIQ_GAIN_HIGH  10
#define ate_TXIQ_GAIN_LOW  -10
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

#define ate_FREQ_OFFSET_HIGH_ppm  10
#define ate_FREQ_OFFSET_LOW_ppm  -20

#define ate_RX_PATH_SNR_HIGH_db  5000
#define ate_RX_PATH_SNR_LOW_db  17

#define ate_RX_PATH_GAIN_HIGH_db  54
#define ate_RX_PATH_GAIN_LOW_db   43

#define ate_ADC_DAC_SNR_HIGH_db  5000
#define ate_ADC_DAC_SNR_LOW_db  35

#define ate_dco_sweep_test_ADC_STEP_HIGH 5
#define ate_dco_sweep_test_ADC_STEP_LOW 0

#define ate_dco_sweep_test_DCO_HIGH 400
#define ate_dco_sweep_test_DCO_LOW 110

#define ate_BBRX2_RXIQ_HIGH  3
#define ate_BBRX2_RXIQ_LOW  -3

#define ate_TXBB_TXIQ_HIGH  5
#define ate_TXBB_TXIQ_LOW  -5

#define ate_VDD33_HIGH  3600
#define ate_VDD33_LOW  3200 

#define ate_temp_code_HIGH  120
#define ate_temp_code_LOW  0

#define ate_TXCAP_TMX2G_CCT_LOAD_HIGH  15
#define ate_TXCAP_TMX2G_CCT_LOAD_LOW  0

#define ate_TXCAP_PA2G_CCT_STG1_HIGH  12
#define ate_TXCAP_PA2G_CCT_STG1_LOW  0

#define ate_TXCAP_PA2G_CCT_STG2_HIGH  6
#define ate_TXCAP_PA2G_CCT_STG2_LOW  0

#define ate_rc_cal_dout_HIGH 60 
#define ate_rc_cal_dout_LOW 3

#define ate_RTC_freq_170khz_HIGH 185
#define ate_RTC_freq_170khz_LOW 140

#define ate_RTC_freq_70khz_HIGH 80
#define ate_RTC_freq_70khz_LOW 60

#define ate_rssi_HIGH  55
#define ate_rssi_LOW  50

#define ate_rx_suc_num_max_HIGH 10
#define ate_rx_suc_num_max_LOW  7

#define ate_rx_suc_num_sum_HIGH 40
#define ate_rx_suc_num_sum_LOW  18

//define check enable
#define ate_RX_GAIN_CHECK_check_en 1
#define ate_TX_PWCTRL_ATTEN_check_en 1
#define ate_TX_PWCTRL_CHAN_OFFSET_check_en 1
#define ate_RX_NOISEFLOOR_check_en 1
#define ate_TXIQ_GAIN_check_en 1
#define ate_TXIQ_PHASE_check_en 1
#define ate_RXIQ_GAIN_check_en 1
#define ate_RXIQ_PHASE_check_en 1
#define ate_TXDC_check_en 1
#define ate_RXDC_check_en 1
#define ate_FREQ_OFFSET_check_en 1
#define ate_RX_PATH_SNR_check_en 1
#define ate_RX_PATH_GAIN_check_en 1
#define ate_ADC_DAC_SNR_check_en 1
#define ate_dco_sweep_test_ADC_STEP_check_en 1
#define ate_dco_sweep_test_DCO_check_en 0
#define ate_RX_SWITCH_GAIN_check_en 1
#define ate_BBRX2_RXIQ_check_en 1
#define ate_TXBB_TXIQ_check_en 1
#define ate_VDD33_check_en 1
#define ate_temp_code_check_en 0
#define ate_TXCAP_TMX2G_CCT_LOAD_check_en 1
#define ate_TXCAP_PA2G_CCT_STG1_check_en 1
#define ate_TXCAP_PA2G_CCT_STG2_check_en 1
#define ate_rc_cal_dout_check_en 1
#define ate_RTC_freq_170khz_check_en 1
#define ate_RTC_freq_70khz_check_en 1

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
    S8 *TXBB_TXDC_i; 
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
    U8 *wifi_init_time;
    U32 wifi_init_time_t;

    U16 addr_offset[] = {1, 5, 6, 8, 9, 11, 14, 23, 32, 41, 50, 92, 98, 104, 110, 113, 116, 119, 125, 139, 140, 141, 146, 151, 156, 161, 191, 221, 
                        251, 401, 405, 406, 407, 409, 412, 416, 417, 427, 437, 442, 447, 452, 455, 459, 467, 468, 470, 471, 486, 501, 502, 508, 509, 510, 281, 311, 335, 356};

    U32 result_mask = 
                            (ate_TX_PWCTRL_ATTEN_check_en << 0) | 
                            (ate_TXIQ_GAIN_check_en << 1) | 
                            (ate_TXIQ_PHASE_check_en << 2) | 
                            (ate_RXIQ_GAIN_check_en << 3) | 
                            (ate_RXIQ_PHASE_check_en << 4) | 
                            (ate_TXDC_check_en << 5) | (ate_TXDC_check_en << 6) | 
                            (ate_RXDC_check_en << 7) | (ate_RXDC_check_en << 8) | (ate_RXDC_check_en << 9) | (ate_RXDC_check_en << 10) | 
                            (ate_RX_GAIN_CHECK_check_en << 11) | 
                            (ate_RX_NOISEFLOOR_check_en << 12) | 
                            (ate_ADC_DAC_SNR_check_en << 13) | 
                            (ate_FREQ_OFFSET_check_en << 14) | 
                            (ate_RX_PATH_SNR_check_en << 15) | 
                            (1 << 16) |
                            (ate_TX_PWCTRL_CHAN_OFFSET_check_en << 17) | 
                            (ate_RTC_freq_170khz_check_en << 18) |
                            (ate_RTC_freq_70khz_check_en << 19) |
                            (ate_BBRX2_RXIQ_check_en << 20) | 
                            (ate_TXBB_TXIQ_check_en << 21) |
                            (ate_RX_PATH_GAIN_check_en << 22) | 
                            (ate_dco_sweep_test_ADC_STEP_check_en << 23) |  
                            (ate_dco_sweep_test_ADC_STEP_check_en << 24) | 
                            (ate_dco_sweep_test_DCO_check_en << 25) | 
                            (ate_RX_SWITCH_GAIN_check_en << 26) |
                            (ate_VDD33_check_en << 27) | 
                            (ate_temp_code_check_en << 28) |  
                            (ate_TXCAP_TMX2G_CCT_LOAD_check_en << 29) | 
                            (ate_TXCAP_PA2G_CCT_STG1_check_en << 29) |
                            (ate_TXCAP_PA2G_CCT_STG2_check_en << 29) |
                            (ate_rc_cal_dout_check_en << 30) |
                            (1 << 31);


    ate_check_result = 0;

    CHIP_ID = (U8*)data_in + addr_offset[0] - 1;
    CHIP_VERSION = (U8*)data_in + addr_offset[1] - 1;
    VDD33 = (U8*)data_in + addr_offset[2] - 1;
    temp_code = (U8*)data_in + addr_offset[3] - 1;
    offset = (U8*)data_in + addr_offset[4] - 1;
    cal_rf_ana_gain = (U8*)data_in + addr_offset[5] - 1;
    TXBB_TXIQ_gain = (S8*)data_in + addr_offset[6] - 1;
    TXBB_TXIQ_phase = (S8*)data_in + addr_offset[7] - 1;
    TXBB_TXDC_i = (S8*)data_in + addr_offset[8] - 1;
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
    wifi_init_time = (U8*)data_in + addr_offset[57] - 1;

//#if ate_check_print
    memset(printf_buf, 0, sizeof(printf_buf));
//#endif

    check_result_t = (check_result[3] << 8*3) | (check_result[2] << 8*2) | 
                     (check_result[1] << 8*1) | (check_result[0] << 8*0); 

    if (ate_check_print) PHY_PRINT("\nCHIP_VERSION: 0x%x\n", *CHIP_VERSION);
    CHIP_ID_t = (CHIP_ID[3] << 8*3) | (CHIP_ID[2] << 8*2) | (CHIP_ID[1] << 8*1) | (CHIP_ID[0] << 8*0);
    if (ate_check_print) PHY_PRINT("CHIP_ID: 0x%x\n", CHIP_ID_t);
    
    if (ate_check_print) PHY_PRINT("rc_cal_dout=%d\n", *rc_cal_dout);
    check_ate_data(*rc_cal_dout, ate_rc_cal_dout_LOW, ate_rc_cal_dout_HIGH, 30);
    
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
    check_ate_data(VDD33_t, ate_VDD33_LOW, ate_VDD33_HIGH, 27);
    check_ate_data(*temp_code, ate_temp_code_LOW, ate_temp_code_HIGH, 28);

    if (ate_check_print) {
        PHY_PRINT("cal_rf_ana_gain, rf_gain=0x%x, ana_gain=0x%x, bb_atten=%d\n", 
                      cal_rf_ana_gain[0], cal_rf_ana_gain[1], cal_rf_ana_gain[2]);
    }
    
    if (ate_check_print) PHY_PRINT("TXBB_TXIQ, ");
    for(i=0; i<4; i++){
        if (ate_check_print) PHY_PRINT("%d, %d; ", TXBB_TXIQ_gain[i], TXBB_TXIQ_phase[i]);
        check_ate_data(TXBB_TXIQ_gain[i], ate_TXBB_TXIQ_LOW, ate_TXBB_TXIQ_HIGH, 21);
        check_ate_data(TXBB_TXIQ_phase[i], ate_TXBB_TXIQ_LOW, ate_TXBB_TXIQ_HIGH, 21);
    }
    if (ate_check_print) PHY_PRINT("\n");

    //if (ate_check_print) PHY_PRINT("TXBB_TXDC, ");
    //for(i=0; i<9; i++){
    //    if (ate_check_print) PHY_PRINT("%d, %d; ", TXBB_TXDC_i[i], TXBB_TXDC_q[i]);
    //}
    //if (ate_check_print) PHY_PRINT("\n");
        
    S8 *step;
    for(i=0; i<3; i++){
        step = &RX_GAIN_CHECK[i*14];
        if (ate_check_print) PHY_PRINT("RX_GAIN_CHECK, ");
        for(j=0; j<14; j++){
            if (ate_check_print) PHY_PRINT("%d, ", step[j]);
            check_ate_data(step[j], ate_RX_GAIN_CHECK_LOW_hdb[j], ate_RX_GAIN_CHECK_HIGH_hdb[j], 11);
        }
        if (ate_check_print) PHY_PRINT("\n");
    }

    if (ate_check_print) PHY_PRINT("RX_GAIN_CHECK_POWER_hdb, ");
    for(i=0; i<15; i++){
        if (ate_check_print) PHY_PRINT("%d, %d; ", rx_gain_check_tot_pwr[i], rx_gain_check_sig_pwr[i]);
    }
    if (ate_check_print) PHY_PRINT("\n");

    if (ate_check_print) PHY_PRINT("BBRX2_RXIQ, ");
    for(i=0; i<6; i++){
        if (ate_check_print) PHY_PRINT("%d, %d; ", BBRX2_RXIQ_gain[i], BBRX2_RXIQ_phase[i]);
        check_ate_data(BBRX2_RXIQ_gain[i], ate_BBRX2_RXIQ_LOW, ate_BBRX2_RXIQ_HIGH, 20);
        check_ate_data(BBRX2_RXIQ_phase[i], ate_BBRX2_RXIQ_LOW, ate_BBRX2_RXIQ_HIGH, 20);
    }
    if (ate_check_print) PHY_PRINT("\n");
    
    int noisefloor_min;
    for(i=0; i<2; i++){
        RX_NOISEFLOOR_t[i] = (RX_NOISEFLOOR[i*2+1] << 8*1) | (RX_NOISEFLOOR[i*2+0] << 8*0);
        if (ate_check_print) PHY_PRINT("RX_NOISEFLOOR, %d\n", RX_NOISEFLOOR_t[i]);
    }
    if((RX_NOISEFLOOR_t[0] + 20) < RX_NOISEFLOOR_t[1])
        noisefloor_min = RX_NOISEFLOOR_t[0] + 20;
    else
        noisefloor_min = RX_NOISEFLOOR_t[1];
    check_ate_data(noisefloor_min, ate_RX_NOISEFLOOR_LOW, ate_RX_NOISEFLOOR_HIGH, 12);
    
    if (ate_check_print) PHY_PRINT("TXCAP_TMX2G_CCT_LOAD, ");
    for(i=0; i<3; i++){
        if (ate_check_print) PHY_PRINT("%d, ", TXCAP_TMX2G_CCT_LOAD[i]);
        check_ate_data(TXCAP_TMX2G_CCT_LOAD[i], ate_TXCAP_TMX2G_CCT_LOAD_LOW, ate_TXCAP_TMX2G_CCT_LOAD_HIGH, 29);
    }
    if (ate_check_print) PHY_PRINT("\n");
   
    if (ate_check_print) PHY_PRINT("TXCAP_PA2G_CCT_STG1, ");
    for(i=0; i<3; i++){
        if (ate_check_print) PHY_PRINT("%d, ", TXCAP_PA2G_CCT_STG1[i]);
        check_ate_data(TXCAP_PA2G_CCT_STG1[i], ate_TXCAP_PA2G_CCT_STG1_LOW, ate_TXCAP_PA2G_CCT_STG1_HIGH, 29);
    }
    if (ate_check_print) PHY_PRINT("\n");
   
    if (ate_check_print) PHY_PRINT("TXCAP_PA2G_CCT_STG2, ");
    for(i=0; i<3; i++){
        if (ate_check_print) PHY_PRINT("%d, ", TXCAP_PA2G_CCT_STG2[i]);
        check_ate_data(TXCAP_PA2G_CCT_STG2[i], ate_TXCAP_PA2G_CCT_STG2_LOW, ate_TXCAP_PA2G_CCT_STG2_HIGH, 29);
    }
    if (ate_check_print) PHY_PRINT("\n");
   
    if (ate_check_print) PHY_PRINT("TX_PWRCTRL_ATTEN, ");
    for(i=0; i<6; i++){
        if (ate_check_print) PHY_PRINT("%d, ", TX_PWRCTRL_ATTEN[i]);
        check_ate_data(TX_PWRCTRL_ATTEN[i], ate_TX_PWCTRL_ATTEN_LOW_qdb[i], ate_TX_PWCTRL_ATTEN_HIGH_qdb[i], 0);
    }
    if (ate_check_print) PHY_PRINT("\n");
   
    if (ate_check_print) PHY_PRINT("TX_PWCTRL_CHAN_OFFSET, ");
    for(i=0; i<14; i++){
        if (ate_check_print) PHY_PRINT("%d, ", TX_PWCTRL_CHAN_OFFSET[i]);
        check_ate_data(TX_PWCTRL_CHAN_OFFSET[i], ate_TX_PWCTRL_CHAN_OFFSET_LOW_qdb, ate_TX_PWCTRL_CHAN_OFFSET_HIGH_qdb, 17);
    }
    if (ate_check_print) PHY_PRINT("\n");
    
    if((check_result_t >> 18) & 0x1){
        if (*TXIQ_gain > 0) *TXIQ_gain = 16;
        else *TXIQ_gain = -16;
        if (*TXIQ_phase > 0) *TXIQ_phase = 32;
        else *TXIQ_phase = -32
    }
    if (ate_check_print) PHY_PRINT("TXIQ, %d, %d\n", *TXIQ_gain, *TXIQ_phase);
    check_ate_data(*TXIQ_gain, ate_TXIQ_GAIN_LOW, ate_TXIQ_GAIN_HIGH, 1);
    check_ate_data(*TXIQ_phase, ate_TXIQ_PHASE_LOW, ate_TXIQ_PHASE_HIGH, 2);
    
    if (ate_check_print) PHY_PRINT("TXDC, ");
    for(i=0; i<4; i++){
        if (ate_check_print) PHY_PRINT("%d, %d; ", TXDC_i[i], TXDC_q[i]);
        check_ate_data(TXDC_i[i], ate_TXDC_LOW, ate_TXDC_HIGH, 5);
        check_ate_data(TXDC_q[i], ate_TXDC_LOW, ate_TXDC_HIGH, 6);
    }
    if (ate_check_print) PHY_PRINT("\n");
    
    if (ate_check_print) PHY_PRINT("RXIQ, ");
    for(i=0; i<5; i++){
        if((check_result_t >> 19) & 0x1){
        if (RXIQ_gain[i] > 0) RXIQ_gain[i] = 16;
        else RXIQ_gain[i] = -16;
        if (RXIQ_phase[i] > 0) RXIQ_phase[i] = 32;
        else RXIQ_phase[i] = -32
        }
        if (ate_check_print) PHY_PRINT("%d, %d; ", RXIQ_gain[i], RXIQ_phase[i]);
        check_ate_data(RXIQ_gain[i], ate_RXIQ_GAIN_LOW, ate_RXIQ_GAIN_HIGH, 3);
        check_ate_data(RXIQ_phase[i], ate_RXIQ_PHASE_LOW, ate_RXIQ_PHASE_HIGH, 4);
    }
    if (ate_check_print) PHY_PRINT("\n");

    if (ate_check_print) PHY_PRINT("RXIQ_tot_power, %ddB\n", *rxiq_tot_pwr);    

    if (ate_check_print) PHY_PRINT("RXDC, ");
    for(i=0; i<30; i++){
        RXDC_c_i_t[i] = (RXDC_c_i[i*2+1] << 8*1) | (RXDC_c_i[i*2+0] << 8*0);
        RXDC_c_q_t[i] = (RXDC_c_q[i*2+1] << 8*1) | (RXDC_c_q[i*2+0] << 8*0);
        RXDC_f_i_t[i] = (RXDC_f_i[i*2+1] << 8*1) | (RXDC_f_i[i*2+0] << 8*0);
        RXDC_f_q_t[i] = (RXDC_f_q[i*2+1] << 8*1) | (RXDC_f_q[i*2+0] << 8*0);
        check_ate_data(RXDC_c_i_t[i], ate_RXDC_LOW, ate_RXDC_HIGH, 7);
        check_ate_data(RXDC_c_q_t[i], ate_RXDC_LOW, ate_RXDC_HIGH, 8);
        check_ate_data(RXDC_f_i_t[i], ate_RXDC_LOW, ate_RXDC_HIGH, 9);
        check_ate_data(RXDC_f_q_t[i], ate_RXDC_LOW, ate_RXDC_HIGH, 10);
        if (ate_check_print) PHY_PRINT("%d, %d, %d, %d; ", RXDC_c_i_t[i], RXDC_c_q_t[i], RXDC_f_i_t[i], RXDC_f_q_t[i]);
    }
    if (ate_check_print) PHY_PRINT("\n");

    freq_offset_cal_total_pwr_t = (freq_offset_cal_total_pwr[3] << 8*3) | (freq_offset_cal_total_pwr[2] << 8*2) | 
                                               (freq_offset_cal_total_pwr[1] << 8*1) | (freq_offset_cal_total_pwr[0] << 8*0);
    if (ate_check_print) PHY_PRINT("freq_offset_cal, bb_gain=%d, total_pwr=%d\n", *freq_offset_cal_bb_gain, freq_offset_cal_total_pwr_t);
    if (ate_check_print) PHY_PRINT("RX_PATH_GAIN, %ddB\n", *rx_path_gain);
    check_ate_data(*rx_path_gain, ate_RX_PATH_GAIN_LOW_db, ate_RX_PATH_GAIN_HIGH_db, 22);
    
    check_ate_data(*FREQ_OFFSET, ate_FREQ_OFFSET_LOW_ppm, ate_FREQ_OFFSET_HIGH_ppm, 14);
    if (ate_check_print) PHY_PRINT("FREQ_OFFSET, %dPPM\n", *FREQ_OFFSET);
    
    RX_PATH_SNR_t = (RX_PATH_SNR[1] << 8*1) | (RX_PATH_SNR[0] << 8*0);
    check_ate_data(RX_PATH_SNR_t, ate_RX_PATH_SNR_LOW_db, ate_RX_PATH_SNR_HIGH_db, 15);
    
    if (ate_check_print) PHY_PRINT("RX_PATH_SNR, %ddB\n", RX_PATH_SNR_t);

    adc_dac_snr_2tone_total_pwr_t = (adc_dac_snr_2tone_total_pwr[3] << 8*3) | (adc_dac_snr_2tone_total_pwr[2] << 8*2) | 
                                    (adc_dac_snr_2tone_total_pwr[1] << 8*1) | (adc_dac_snr_2tone_total_pwr[0] << 8*0);
    
    if (ate_check_print) {
        PHY_PRINT("adc_dac_snr_2tone, bbrx1=0x%x, bbrx2=0x%x, tone_atten=%d: total_pwr=%d\n", 
                       adc_dac_snr_2tone_gain[0], adc_dac_snr_2tone_gain[1], 
                       adc_dac_snr_2tone_gain[2], adc_dac_snr_2tone_total_pwr_t);
    }
    
    check_ate_data(*ADC_DAC_SNR, ate_ADC_DAC_SNR_LOW_db, ate_ADC_DAC_SNR_HIGH_db, 13);
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
    check_ate_data(RX_SWITCH_GAIN[0], ate_RX_SWITCH_GAIN_LOW_db[0], ate_RX_SWITCH_GAIN_HIGH_db[0], 26);
    check_ate_data(RX_SWITCH_GAIN[1], ate_RX_SWITCH_GAIN_LOW_db[1], ate_RX_SWITCH_GAIN_HIGH_db[1], 26);
    check_ate_data(RX_SWITCH_GAIN[2], ate_RX_SWITCH_GAIN_LOW_db[2], ate_RX_SWITCH_GAIN_HIGH_db[2], 26);

    if (ate_check_print) {
        PHY_PRINT("dco_sweep_test_ADC_STEP, %d, %d; %d, %d\n", 
            dco_sweep_test_ADC_STEP[0], dco_sweep_test_ADC_STEP[1], 
            dco_sweep_test_ADC_STEP[2], dco_sweep_test_ADC_STEP[3]);
    }
    check_ate_data(dco_sweep_test_ADC_STEP[0], ate_dco_sweep_test_ADC_STEP_LOW, ate_dco_sweep_test_ADC_STEP_HIGH, 23);
    check_ate_data(dco_sweep_test_ADC_STEP[1], ate_dco_sweep_test_ADC_STEP_LOW, ate_dco_sweep_test_ADC_STEP_HIGH, 23);
    check_ate_data(dco_sweep_test_ADC_STEP[2], ate_dco_sweep_test_ADC_STEP_LOW, ate_dco_sweep_test_ADC_STEP_HIGH, 24);
    check_ate_data(dco_sweep_test_ADC_STEP[3], ate_dco_sweep_test_ADC_STEP_LOW, ate_dco_sweep_test_ADC_STEP_HIGH, 24);
    
    for(i=0; i<4; i++){
        dco_sweep_test_DCO_t[i] = (dco_sweep_test_DCO[i*2+1] << 8*1) | (dco_sweep_test_DCO[i*2+0] << 8*0);
        check_ate_data(dco_sweep_test_DCO_t[i], ate_dco_sweep_test_DCO_LOW, ate_dco_sweep_test_DCO_HIGH, 25);
    }   
    
    if (ate_check_print) {
        PHY_PRINT("dco_sweep_test_DCO, %d, %d; %d, %d\n", 
            dco_sweep_test_DCO_t[0], dco_sweep_test_DCO_t[1], 
            dco_sweep_test_DCO_t[2], dco_sweep_test_DCO_t[3]);
    }

    if (ate_check_print) PHY_PRINT("txp_pwctrl_atten, %d\n", TX_POCKET_TEST[0]);

    if (ate_check_print) PHY_PRINT("fb_rxrssi, ");
    for(i=0; i<6; i++){
        if (ate_check_print) PHY_PRINT("%d, ", TX_POCKET_TEST[1+i*2]);
    }
    if (ate_check_print) PHY_PRINT("\n")

    if (ate_check_print) PHY_PRINT("dut_rxrssi, ");
    for(i=0; i<6; i++){
        if (ate_check_print) PHY_PRINT("%d, ", TX_POCKET_TEST[2+i*2]);
    }
    if (ate_check_print) PHY_PRINT("\n")

    if (ate_check_print) PHY_PRINT("fb_rx_num, ");
    for(i=0; i<6; i++){
        if (ate_check_print) PHY_PRINT("%d, ", TX_POCKET_TEST[13+i*2]);
    }
    if (ate_check_print) PHY_PRINT("\n")

    if (ate_check_print) PHY_PRINT("dut_rx_num, ");
    for(i=0; i<6; i++){
        if (ate_check_print) PHY_PRINT("%d, ", TX_POCKET_TEST[14+i*2]);
    }
    if (ate_check_print) PHY_PRINT("\n")

    for(i=0; i<6; i++){
	TX_POCKET_STATE_t[i] = (TX_POCKET_STATE[i*2+3] << 8*3) | (TX_POCKET_STATE[i*2+2] << 8*2) | (TX_POCKET_STATE[i*2+1] << 8*1) | (TX_POCKET_STATE[i*2+0] << 8*0);
    }
    if (ate_check_print) PHY_PRINT("txp_state: 0x%08x%08x%08x, 0x%08x%08x%08x;\n", TX_POCKET_STATE_t[2],TX_POCKET_STATE_t[1],TX_POCKET_STATE_t[0],
		                                                                   TX_POCKET_STATE_t[5],TX_POCKET_STATE_t[4],TX_POCKET_STATE_t[3]);
    if (ate_check_print) PHY_PRINT("txreq_start_time=%d\n", (TX_POCKET_STATE[29] << 8*3) | (TX_POCKET_STATE[28] << 8*2) | 
                                                            (TX_POCKET_STATE[27] << 8*1) | (TX_POCKET_STATE[26] << 8*0));
    
    ate_check_result = ate_check_result & result_mask;
    if (ate_check_print) PHY_PRINT("check_result_t=0x%x, ate_check_result=0x%x\n", check_result_t, ate_check_result); 

    if (ate_check_print) PHY_PRINT("RTC_freq_170khz=%d\n", *RTC_freq_170khz);
    check_ate_data(*RTC_freq_170khz, ate_RTC_freq_170khz_LOW, ate_RTC_freq_170khz_HIGH, 18);

    if (ate_check_print) PHY_PRINT("RTC_freq_70khz=%d\n", *RTC_freq_70khz);
    check_ate_data(*RTC_freq_70khz, ate_RTC_freq_70khz_LOW, ate_RTC_freq_70khz_HIGH, 19);

    wifi_init_time_t = (wifi_init_time[3] << 8*3) | (wifi_init_time[2] << 8*2) | 
                       (wifi_init_time[1] << 8*1) | (wifi_init_time[0] << 8*0); 
    if (ate_check_print) PHY_PRINT("wifi_init_time: %dus\n", wifi_init_time_t);

    svn_version_t = (svn_version[1] << 8*1) | (svn_version[0] << 8*0);
    if (ate_check_print) PHY_PRINT("WIFI_Test SVN_Version: %d\n", svn_version_t); 

    if (ate_check_print) {
        PHY_PRINT("\n\n--------------------------------------------------------\n");
        if (check_result_t > 0){
            PHY_PRINT("---------------CHECK BOARD FAIL----------------\nBecause:");
            for (i=0; i<27; i++){
                if (check_result_t & (1 << i)){
                    switch(i){
                        case 0: PHY_PRINT("TX_PWRCTRL_ATTEN FAIL, "); break;
                        case 1: PHY_PRINT("TXIQ_GAIN FAIL, "); break;
                        case 2: PHY_PRINT("TXIQ_PHASE FAIL, "); break;
                        case 3: PHY_PRINT("RXIQ_GAIN FAIL, "); break;
                        case 4: PHY_PRINT("RXIQ_PHASE FAIL, "); break;
                        case 5: PHY_PRINT("TXDC_I FAIL, "); break;
                        case 6: PHY_PRINT("TXDC_Q FAIL, "); break;
                        case 7: PHY_PRINT("RXDC_C_I FAIL, "); break;
                        case 8: PHY_PRINT("RXDC_C_Q FAIL, "); break;
                        case 9: PHY_PRINT("RXDC_F_I FAIL, "); break;
                        case 10: PHY_PRINT("RXDC_F_Q FAIL, "); break;
                        case 11: PHY_PRINT("RX_GAIN_CHECK FAIL, "); break;
                        case 12: PHY_PRINT("RX_NOISEFLOOR FAIL, "); break;
                        case 13: PHY_PRINT("ADC_DAC_SNR FAIL, "); break;
                        case 14: PHY_PRINT("FREQ_OFFSET FAIL, "); break;
                        case 15: PHY_PRINT("RX_PATH_SNR FAIL, "); break;
                        case 16: PHY_PRINT("SDIO_PAD FAIL, "); break;
                        case 17: PHY_PRINT("TX_PWCTRL_CHAN_OFFSET FAIL, "); break;
                        case 18: PHY_PRINT("TXIQ_Convergence FAIL, "); break;
                        case 19: PHY_PRINT("RXIQ_Convergence FAIL, "); break;
                        case 20: PHY_PRINT("BBRX2_RXIQ FAIL, "); break;
                        case 21: PHY_PRINT("TXBB_TXIQ FAIL, "); break;
                        case 22: PHY_PRINT("RX_PATH_GAIN FAIL, "); break;
                        case 23: PHY_PRINT("ADC_STEP_I FAIL, "); break;
                        case 24: PHY_PRINT("ADC_STEP_Q FAIL, "); break;
                        case 25: PHY_PRINT("DCO_HIGH_LOW FAIL, "); break;
                        case 26: PHY_PRINT("RX_SWITCH_GAIN FAIL, "); break;
                    }
                }
            }            
            PHY_PRINT("\n");
        }else{
            PHY_PRINT("---------------CHECK BOARD PASS----------------\n");
        }
        PHY_PRINT("--------------------------------------------------------\n\n\n");   

        PHY_PRINT("\n\n--------------------------------------------------------\n");
        if (ate_check_result > 0){
            PHY_PRINT("---------------CHECK BOARD FAIL----------------\nBecause:");
            for (i=0; i<32; i++){
                if (ate_check_result & (1 << i)){
                    switch(i){
                        case 0: PHY_PRINT("TX_PWRCTRL_ATTEN FAIL, "); break;
                        case 1: PHY_PRINT("TXIQ_GAIN FAIL, "); break;
                        case 2: PHY_PRINT("TXIQ_PHASE FAIL, "); break;
                        case 3: PHY_PRINT("RXIQ_GAIN FAIL, "); break;
                        case 4: PHY_PRINT("RXIQ_PHASE FAIL, "); break;
                        case 5: PHY_PRINT("TXDC_I FAIL, "); break;
                        case 6: PHY_PRINT("TXDC_Q FAIL, "); break;
                        case 7: PHY_PRINT("RXDC_C_I FAIL, "); break;
                        case 8: PHY_PRINT("RXDC_C_Q FAIL, "); break;
                        case 9: PHY_PRINT("RXDC_F_I FAIL, "); break;
                        case 10: PHY_PRINT("RXDC_F_Q FAIL, "); break;
                        case 11: PHY_PRINT("RX_GAIN_CHECK FAIL, "); break;
                        case 12: PHY_PRINT("RX_NOISEFLOOR FAIL, "); break;
                        case 13: PHY_PRINT("ADC_DAC_SNR FAIL, "); break;
                        case 14: PHY_PRINT("FREQ_OFFSET FAIL, "); break;
                        case 15: PHY_PRINT("RX_PATH_SNR FAIL, "); break;
                        case 16: PHY_PRINT("rssi FAIL, "); break;
                        case 17: PHY_PRINT("TX_PWCTRL_CHAN_OFFSET FAIL, "); break;
                        case 18: PHY_PRINT("RTC_freq_170khz FAIL, "); break;
                        case 19: PHY_PRINT("RTC_freq_70khz FAIL, "); break;
                        case 20: PHY_PRINT("BBRX2_RXIQ FAIL, "); break;
                        case 21: PHY_PRINT("TXBB_TXIQ FAIL, "); break;
                        case 22: PHY_PRINT("RX_PATH_GAIN FAIL, "); break;
                        case 23: PHY_PRINT("ADC_STEP_I FAIL, "); break;
                        case 24: PHY_PRINT("ADC_STEP_Q FAIL, "); break;
                        case 25: PHY_PRINT("DCO_HIGH_LOW FAIL, "); break;
                        case 26: PHY_PRINT("RX_SWITCH_GAIN FAIL, "); break;
                        case 27: PHY_PRINT("VDD33 FAIL, "); break;
                        case 28: PHY_PRINT("temp_code FAIL, "); break;
                        case 29: PHY_PRINT("TXCAP FAIL, "); break;
                        case 30: PHY_PRINT("RC_CAL FAIL, "); break;
                        case 31: PHY_PRINT("rx_suc_num FAIL, "); break;
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
#else
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
    sprintf(filename, "/usr/local/home/test/datalog/124_chip_id/Site%d_chip_id_%x_%d%02d%02d_%02d%02d%02d.log",sitenum+1, CHIP_ID_t, 1900 + current_time->tm_year, 1 + current_time->tm_mon,  current_time->tm_mday, current_time->tm_hour, current_time->tm_min, current_time->tm_sec);

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
