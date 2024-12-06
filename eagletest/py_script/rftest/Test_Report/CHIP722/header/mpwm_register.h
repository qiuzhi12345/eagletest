#ifndef _MCPWM_REG_H
#define _MCPWM_REG_H

#define MCPWM_PTCON           (MCPWM_REGISTER_BASE(0) + 0x00)  //PWM Time Base Control Register 
    /*
    PTEN 15 R/W 1'b0 
    PWM timer base enable, active high  
    
    Reserved 14~8 R 7''h0 
    Reserved 
    
    PTOPS 7~4 R/W 4'h0 
    PWM time base output postscale select bits  
        4'hf:  1:16 post scale 4'h1: 1:2 post scale 4'h0: 1:1 post scale  3~2 R 2''h0 Reserved 
    
    PTMOD 1~0 R/W 2'h0 
    PWM time base mode setting 2'h3 : PWM time base operates in a Continuous Up/Down mode with interrupts for double PWM updates   
        2'h2: PWM time base operates in a Continuous Up/Down Counting mode   
        2'h1:PWM time base operates in Single Event mode   
        2'h0: PWM time base operates in Free Running mode   
    */
    #define MCPWM_TIMER_BASE_EN        0x1        // 1:enable 0:disable
    #define MCPWM_TIMER_BASE_EN_M  (BIT(15))
    #define MCPWM_TIMER_BASE_EN_S      15
    #define MCPWM_TIMER_BASE_POST_SCALE   0xf   // 0x0:1:1  0x1:1:2 0xF:1:16
    #define MCPWM_TIMER_BASE_POST_SCALE_S  4
    #define MCPWM_TIMER_BASE_MODE        0x3 
    #define MCPWM_TIMER_BASE_MODE_S        0   

        //api
        //#define MCPWM_API_SET_TIMER_BASE_EN()   SET_PERI_REG_MASK(MCPWM_PTCON,MCPWM_TIMER_BASE_EN_M)
        //#define MCPWM_API_SET_TIMER_BASE_DIS()  CLEAR_PERI_REG_MASK(MCPWM_PTCON,MCPWM_TIMER_BASE_EN_M)
        #define MCPWM_API_GET_TIMER_BASE_EN()   GET_PERI_REG_BITS(MCPWM_PTCON,MCPWM_TIMER_BASE_EN,MCPWM_TIMER_BASE_EN_S)
        #define MCPWM_API_SET_TIMER_BASE_EN(val) SET_PERI_REG_BITS(MCPWM_PTCON,MCPWM_TIMER_BASE_EN,val,MCPWM_TIMER_BASE_EN_S);
        #define MCPWM_API_SET_TIMER_BASE_PSCALE(val)  SET_PERI_REG_BITS(MCPWM_PTCON,MCPWM_TIMER_BASE_POST_SCALE,val,MCPWM_TIMER_BASE_POST_SCALE_S)
        #define MCPWM_API_GET_TIMER_BASE_PSCALE()   GET_PERI_REG_BITS(MCPWM_PTCON,MCPWM_TIMER_BASE_POST_SCALE,MCPWM_TIMER_BASE_POST_SCALE_S)
        #define MCPWM_API_SET_TIMER_BASE_MODE(val)  SET_PERI_REG_BITS(MCPWM_PTCON,MCPWM_TIMER_BASE_MODE,val,MCPWM_TIMER_BASE_MODE_S)
        #define MCPWM_API_GET_TIMER_BASE_MODE()     GET_PERI_REG_BITS(MCPWM_PTCON,MCPWM_TIMER_BASE_MODE,MCPWM_TIMER_BASE_MODE_S)



#define MCPWM_PTMR            (MCPWM_REGISTER_BASE(0) + 0x04)  //PWM Time Base Register 
    /*
    PTDIR 15 R 1'b0 
    PWM Time Base Count Direction Status bit (read-only) 
        1'b1: PWM time base is counting down 
        1'b0: PWM time base is counting up 
    
    PTMR 14~0 R/W 15'h0 
    PWM Time Base Register Count Value bits 
    */
    #define MCPWM_TIMER_BASE_COUNT_DIR        0x1
	#define MCPWM_TIMER_BASE_COUNT_DIR_M  (BIT(15))
	#define MCPWM_TIMER_BASE_COUNT_DIR_S      15
    #define MCPWM_TIMER_BASE_COUNT_VAL   0x7FFF
    #define MCPWM_TIMER_BASE_COUNT_VAL_S   0

        //api
        #define MCPWM_API_GET_TIMER_BASE_CNT_DIR()   GET_PERI_REG_BITS(MCPWM_PTMR,MCPWM_TIMER_BASE_COUNT_DIR,MCPWM_TIMER_BASE_COUNT_DIR_S)
        #define MCPWM_API_SET_TIMER_BASE_CNT_VAL(val)  SET_PERI_REG_BITS(MCPWM_PTMR,MCPWM_TIMER_BASE_COUNT_VAL,val,MCPWM_TIMER_BASE_COUNT_VAL_S)
        #define MCPWM_API_GET_TIMER_BASE_CNT_VAL()   GET_PERI_REG_BITS( MCPWM_PTMR,MCPWM_TIMER_BASE_COUNT_VAL,MCPWM_TIMER_BASE_COUNT_VAL_S)



#define MCPWM_PTPER           (MCPWM_REGISTER_BASE(0) + 0x08)  //PWM Time Base Period Register 
    /*
    15 R 1'b0 Reserved 
    PTPER 14~0 R/W 15'hffff PWM Time Base Period Value bits 
    */
    #define MCPWM_TIMER_BASE_PERIOD_VAL      0x7FFF
    #define MCPWM_TIMER_BASE_PERIOD_VAL_S    0
	
        //api
        #define MCPWM_API_GET_TIMER_BASE_PERIOD_VAL()   GET_PERI_REG_BITS(MCPWM_PTPER,MCPWM_TIMER_BASE_PERIOD_VAL,MCPWM_TIMER_BASE_PERIOD_VAL_S)
        #define MCPWM_API_SET_TIMER_BASE_PERIOD_VAL(val)  SET_PERI_REG_BITS(MCPWM_PTPER,MCPWM_TIMER_BASE_PERIOD_VAL,val,MCPWM_TIMER_BASE_PERIOD_VAL_S)




#define MCPWM_SEVTCMP         (MCPWM_REGISTER_BASE(0) + 0x0C)  //Special Event Compare Register 
    /*
    SEVTDIR 15 R/W 1'b0 
    Special Event Trigger Time Base Direction bit 
        1'b1: A Special Event Trigger will occur when the PWM time base is counting down  
        1'b0 : A Special Event Trigger will occur when the PWM time base is counting up 
    
    SEVTCMP 14~0 R/W 15'h0 
    Special Event Compare Value bit   
    */
    #define MCPWM_TIMER_BASE_EVENT_TRIG_DIR     0x1
    #define MCPWM_TIMER_BASE_EVENT_TRIG_DIR_M  (BIT(15))
	#define MCPWM_TIMER_BASE_EVENT_TRIG_DIR_S    15
    #define MCPWM_TIMER_BASE_EVENT_CMP_CAL    0x7FFF
    #define MCPWM_TIMER_BASE_EVENT_CMP_CAL_S  0

        //api
        #define MCPWM_API_GET_TIMER_BASE_EVT_TRIG_DIR()  GET_PERI_REG_BITS(MCPWM_SEVTCMP,MCPWM_TIMER_BASE_EVENT_TRIG_DIR,MCPWM_TIMER_BASE_EVENT_TRIG_DIR_S)
        #define MCPWM_API_SET_TIMER_BASE_EVT_TRIG_DIR(val)  SET_PERI_REG_BITS(MCPWM_SEVTCMP,MCPWM_TIMER_BASE_EVENT_TRIG_DIR,val,MCPWM_TIMER_BASE_EVENT_TRIG_DIR_S)
        #define MCPWM_API_GET_TIMER_BASE_EVT_CMP_VAL()   GET_PERI_REG_BITS(MCPWM_SEVTCMP,MCPWM_TIMER_BASE_EVENT_CMP_CAL,MCPWM_TIMER_BASE_EVENT_CMP_CAL_S)
        #define MCPWM_API_SET_TIMER_BASE_EVT_CMP_VAL(val)  SET_PERI_REG_BITS(MCPWM_SEVTCMP,MCPWM_TIMER_BASE_EVENT_CMP_CAL,val,MCPWM_TIMER_BASE_EVENT_CMP_CAL_S)
        

	
#define MCPWM_PWMCON1         (MCPWM_REGISTER_BASE(0) + 0x10) //PWM Control Register 1 
    /*
    Reserved 15~12 R 0 
    Reserved 
    PMOD4 11 R/W 1'b0 PMW4 output mode 
    1'b1: independent mode 
    1'b0: complementary mode 
    PMOD3 10 R/W 1'b0 PMW3 output mode 
    1'b1: independent mode 
    1'b0: complementary mode 
    PMOD2 9 R/W 1'b0 PMW2 output mode 
    1'b1: independent mode 
    1'b0: complementary mode 
    PMOD1 8 R/W 1'b0 PMW1 output mode 
    1'b1: independent mode 
    1'b0: complementary mode 
    Reserved 7~0 R 8'h0 
    Reserved   
    */
    #define MCPWM_PWM4_OUTPUT_MODE_M  (BIT(11))
	#define MCPWM_PWM4_OUTPUT_MODE       0x1
	#define MCPWM_PWM4_OUTPUT_MODE_S     11
    #define MCPWM_PWM3_OUTPUT_MODE_M  (BIT(10))
	#define MCPWM_PWM3_OUTPUT_MODE       0x1
	#define MCPWM_PWM3_OUTPUT_MODE_S     10
    #define MCPWM_PWM2_OUTPUT_MODE_M  (BIT(9))
	#define MCPWM_PWM2_OUTPUT_MODE      0x1
	#define MCPWM_PWM2_OUTPUT_MODE_S     9
    #define MCPWM_PWM1_OUTPUT_MODE_M  (BIT(8))
	#define MCPWM_PWM1_OUTPUT_MODE      0x1
	#define MCPWM_PWM1_OUTPUT_MODE_S     8

        //api
        #define MCPWM_API_GET_PWM4_OUTPUT_MODE()  GET_PERI_REG_BITS(MCPWM_PWMCON1,MCPWM_PWM4_OUTPUT_MODE,MCPWM_PWM4_OUTPUT_MODE_S)
        #define MCPWM_API_SET_PWM4_OUTPUT_MODE(val) SET_PERI_REG_BITS(MCPWM_PWMCON1,MCPWM_PWM4_OUTPUT_MODE,val,MCPWM_PWM4_OUTPUT_MODE_S)
        #define MCPWM_API_GET_PWM3_OUTPUT_MODE()  GET_PERI_REG_BITS(MCPWM_PWMCON1,MCPWM_PWM3_OUTPUT_MODE,MCPWM_PWM3_OUTPUT_MODE_S)
        #define MCPWM_API_SET_PWM3_OUTPUT_MODE(val) SET_PERI_REG_BITS(MCPWM_PWMCON1,MCPWM_PWM3_OUTPUT_MODE,val,MCPWM_PWM3_OUTPUT_MODE_S)
        #define MCPWM_API_GET_PWM2_OUTPUT_MODE()  GET_PERI_REG_BITS(MCPWM_PWMCON1,MCPWM_PWM2_OUTPUT_MODE,MCPWM_PWM2_OUTPUT_MODE_S)
        #define MCPWM_API_SET_PWM2_OUTPUT_MODE(val) SET_PERI_REG_BITS(MCPWM_PWMCON1,MCPWM_PWM2_OUTPUT_MODE,val,MCPWM_PWM2_OUTPUT_MODE_S)
        #define MCPWM_API_GET_PWM1_OUTPUT_MODE()  GET_PERI_REG_BITS(MCPWM_PWMCON1,MCPWM_PWM1_OUTPUT_MODE,MCPWM_PWM1_OUTPUT_MODE_S)
        #define MCPWM_API_SET_PWM1_OUTPUT_MODE(val) SET_PERI_REG_BITS(MCPWM_PWMCON1,MCPWM_PWM1_OUTPUT_MODE,val,MCPWM_PWM1_OUTPUT_MODE_S)
        

#define MCPWM_PWMCON2         (MCPWM_REGISTER_BASE(0) + 0x14) //PWM Control Register 2 (PWMICAP)
    /*
    Reserved 15~12 R 0 
    Reserved 
    
    SEVOPS 11~8 R/W 4'h0 
    PWM Special Event Trigger Output Postscale Select 
    bits 1111 = 1:16 postscale  бн 0001 = 1:2 postscale  0000 = 1:1 postscale  
    Reserved 7~3 R 0 
    Reserved 
    
    IUE 2 R/W 1'b0 
    Immediate Update Enable bit  
    1'b1= Updates to the active PDCx(1,2,3,4 registers are immediate)  
    1'b0 = Updates to the active PxDCx(1,2,3,4 registers are synchronized to the PWM time base) 
    
    OSYNC 1 R/W 1'b0 
    Output Override Synchronization bit  
    1'b1= Output overrides via the OVDCON register are synchronized to the PWM time base  
    1'b0 = Output overrides via the OVDCON register occur on the next clk_pwm boundary 
    
    UDIS 0 R/W 1'b0 
    PWM Update Disable bit  
    1 = Updates from duty cycle and period buffer registers are disabled  
    0 = Updates from duty cycle and period buffer registers are enabled  
    */
    #define MCPWM_SPEC_EVT_TRIG_POST_SCALE    0xF
    #define MCPWM_SPEC_EVT_TRIG_POST_SCALE_S   8
    #define MCPWM_IMDT_UPDATE_EN_M              (BIT(2))
	#define MCPWM_IMDT_UPDATE_EN                0x1
	#define MCPWM_IMDT_UPDATE_EN_S              2
    #define MCPWM_OUTPUT_OVERRIDE_SYNC_M        (BIT(1))
	#define MCPWM_OUTPUT_OVERRIDE_SYNC           0x1
	#define MCPWM_OUTPUT_OVERRIDE_SYNC_S         1
    #define MCPWM_PWM_UPDATE_DISABLE_M          (BIT(0))
	#define MCPWM_PWM_UPDATE_DISABLE             0x1
	#define MCPWM_PWM_UPDATE_DISABLE_S           0

        //api
        #define MCPWM_API_GET_SPEC_EVT_TRIG_PSCALE()  GET_PERI_REG_BITS(MCPWM_PWMCON2,MCPWM_SPEC_EVT_TRIG_POST_SCALE,MCPWM_SPEC_EVT_TRIG_POST_SCALE_S)
        #define MCPWM_API_SET_SPEC_EVT_TRIG_PSCALE(val)  SET_PERI_REG_BITS(MCPWM_PWMCON2,MCPWM_SPEC_EVT_TRIG_POST_SCALE,val,MCPWM_SPEC_EVT_TRIG_POST_SCALE_S)
        #define MCPWM_API_GET_IMDT_UPDATE_EN()        GET_PERI_REG_BITS(MCPWM_PWMCON2,MCPWM_IMDT_UPDATE_EN,MCPWM_IMDT_UPDATE_EN_S)
        #define MCPWM_API_SET_IMDT_UPDATE_EN(val)     SET_PERI_REG_BITS(MCPWM_PWMCON2,MCPWM_IMDT_UPDATE_EN,val,MCPWM_IMDT_UPDATE_EN_S)
        #define MCPWM_API_GET_OUTPUT_OVRD_SYNC()      GET_PERI_REG_BITS(MCPWM_PWMCON2,MCPWM_OUTPUT_OVERRIDE_SYNC,MCPWM_OUTPUT_OVERRIDE_SYNC_S)
        #define MCPWM_API_SET_OUTPUT_OVRD_SYNC(val)   SET_PERI_REG_BITS(MCPWM_PWMCON2,MCPWM_OUTPUT_OVERRIDE_SYNC,val,MCPWM_OUTPUT_OVERRIDE_SYNC_S)
        #define MCPWM_API_GET_PWM_UPDATE_DISABLE()    GET_PERI_REG_BITS(MCPWM_PWMCON2,MCPWM_PWM_UPDATE_DISABLE,MCPWM_PWM_UPDATE_DISABLE_S)
        #define MCPWM_API_SET_PWM_UPDATE_DISABLE(val)  SET_PERI_REG_BITS(MCPWM_PWMCON2,MCPWM_PWM_UPDATE_DISABLE,val,MCPWM_PWM_UPDATE_DISABLE_S)
 



#define MCPWM_DTCON1          (MCPWM_REGISTER_BASE(0) + 0x18) //Dead Time Control Register 1 
    /*
    DTBPS 15~14 R/W 2'h0 
    Dead Time Unit B Prescale Select bits  
    2'b11 = Clock period for Dead Time Unit B is 8 clk_pwm 
    2'b10 = Clock period for Dead Time Unit B is 4 clk_pwm 
    2'b01 = Clock period for Dead Time Unit B is 2 clk_pwm 
    2'b00 = Clock period for Dead Time Unit B is 1 clk_pwm 
    DTB 13~8 R/W 6'h0 
    Unsigned 6-bit Dead Time Value bits for Dead Time Unit B 
    DTAPS 7~6 R/W 2'h0 
    Dead Time Unit A Prescale Select bits  
    2'b11 = Clock period for Dead Time Unit B is 8 clk_pwm 
    2'b10 = Clock period for Dead Time Unit B is 4 clk_pwm 
    2'b01 = Clock period for Dead Time Unit B is 2 clk_pwm 
    2'b00 = Clock period for Dead Time Unit B is 1 clk_pwm 
    DTA 5~0 R/W 6'h0 
    Unsigned 6-bit Dead Time Value bits for Dead Time Unit A  
    */
    #define MCPWM_DEAD_TIME_UNITB_PRESCALE_SEL       0x3
    #define MCPWM_DEAD_TIME_UNITB_PRESCALE_SEL_S     14
    #define MCPWM_DEAD_TIME_UNITB_VAL                0x3f
    #define MCPWM_DEAD_TIME_UNITB_VAL_S              8
    #define MCPWM_DEAD_TIME_UNITA_PRESCALE_SEL       0x3
    #define MCPWM_DEAD_TIME_UNITA_PRESCALE_SEL_S     6
    #define MCPWM_DEAD_TIME_UNITA_VAL                0x3f
    #define MCPWM_DEAD_TIME_UNITA_VAL_S              0
        //api
        #define MCPWM_API_GET_DEAD_TIME_UB_PRESCALE_SEL()   GET_PERI_REG_BITS(MCPWM_DTCON1,MCPWM_DEAD_TIME_UNITB_PRESCALE_SEL,MCPWM_DEAD_TIME_UNITB_PRESCALE_SEL_S)
        #define MCPWM_API_SET_DEAD_TIME_UB_PRESCALE_SEL(val)  SET_PERI_REG_BITS(MCPWM_DTCON1,MCPWM_DEAD_TIME_UNITB_PRESCALE_SEL,val,MCPWM_DEAD_TIME_UNITB_PRESCALE_SEL_S)
        #define MCPWM_API_GET_DEAD_TIME_UB_VAL()            GET_PERI_REG_BITS(MCPWM_DTCON1,MCPWM_DEAD_TIME_UNITB_VAL,MCPWM_DEAD_TIME_UNITB_VAL_S)
        #define MCPWM_API_SET_DEAD_TIME_UB_VAL(val)         SET_PERI_REG_BITS(MCPWM_DTCON1,MCPWM_DEAD_TIME_UNITB_VAL,val,MCPWM_DEAD_TIME_UNITB_VAL_S)
        #define MCPWM_API_GET_DEAD_TIME_UA_PRESCALE_SEL()   GET_PERI_REG_BITS(MCPWM_DTCON1,MCPWM_DEAD_TIME_UNITA_PRESCALE_SEL,MCPWM_DEAD_TIME_UNITA_PRESCALE_SEL_S)
        #define MCPWM_API_SET_DEAD_TIME_UA_PRESCALE_SEL(val) SET_PERI_REG_BITS(MCPWM_DTCON1,MCPWM_DEAD_TIME_UNITA_PRESCALE_SEL,val,MCPWM_DEAD_TIME_UNITA_PRESCALE_SEL_S)
        #define MCPWM_API_GET_DEAD_TIME_UA_VAL()            GET_PERI_REG_BITS(MCPWM_DTCON1,MCPWM_DEAD_TIME_UNITA_VAL,MCPWM_DEAD_TIME_UNITA_VAL_S)
        #define MCPWM_API_SET_DEAD_TIME_UA_VAL(val)         SET_PERI_REG_BITS(MCPWM_DTCON1,MCPWM_DEAD_TIME_UNITA_VAL,val,MCPWM_DEAD_TIME_UNITA_VAL_S)


#define MCPWM_DTCON2          (MCPWM_REGISTER_BASE(0) + 0x1C) //Dead Time Control Register 2 
    /*
    DTS4A 7 R/W 1'b0 
    Dead Time Select bit for PWM4 Signal Going Active  
    1 = Dead time provided from Unit B  
    0 = Dead time provided from Unit A 
    DTS4I 6 R/W 1'b0 
    Dead Time Select bit for PWM4 Signal Going Inactive  
    1 = Dead time provided from Unit B  
    0 = Dead time provided from Unit A 
    DTS3A 5 R/W 1'b0 
    Dead Time Select bit for PWM3 Signal Going Active  
    1 = Dead time provided from Unit B  
    0 = Dead time provided from Unit A 
    DTS3I 4 R/W 1'b0 
    Dead Time Select bit for PWM3 Signal Going Inactive  
    1 = Dead time provided from Unit B  
    0 = Dead time provided from Unit A 
    DTS2A 3 R/W 1'b0 
    Dead Time Select bit for PWM2 Signal Going Active  
    1 = Dead time provided from Unit B  
    0 = Dead time provided from Unit A 
    DTS2I 2 R/W 1'b0 
    Dead Time Select bit for PWM2 Signal Going Inactive  
    1 = Dead time provided from Unit B  
    0 = Dead time provided from Unit A 
    DTS1A 1 R/W 1'b0 
    Dead Time Select bit for PWM1 Signal Going Active  
    1 = Dead time provided from Unit B  
    0 = Dead time provided from Unit A 
    DTS1I 0 R/W 1'b0 
    Dead Time Select bit for PWM1 Signal Going Inactive  
    1 = Dead time provided from Unit B  
    0 = Dead time provided from Unit A 
    */
    #define MCPWM_PWM4_SIG_ACTIVE_SEL_M  (BIT(7))
    #define MCPWM_PWM4_SIG_ACTIVE_SEL   0x1
    #define MCPWM_PWM4_SIG_ACTIVE_SEL_S    7
    #define MCPWM_PWM4_SIG_INACTIVE_SEL_M  (BIT(6))
    #define MCPWM_PWM4_SIG_INACTIVE_SEL   0x1
    #define MCPWM_PWM4_SIG_INACTIVE_SEL_S    6
    
    #define MCPWM_PWM3_SIG_ACTIVE_SEL_M  (BIT(5))
    #define MCPWM_PWM3_SIG_ACTIVE_SEL   0x1
    #define MCPWM_PWM3_SIG_ACTIVE_SEL_S    5
    #define MCPWM_PWM3_SIG_INACTIVE_SEL_M  (BIT(4))
    #define MCPWM_PWM3_SIG_INACTIVE_SEL   0x1
    #define MCPWM_PWM3_SIG_INACTIVE_SEL_S    4
    
    #define MCPWM_PWM2_SIG_ACTIVE_SEL_M  (BIT(3))
    #define MCPWM_PWM2_SIG_ACTIVE_SEL   0x1
    #define MCPWM_PWM2_SIG_ACTIVE_SEL_S    3
    #define MCPWM_PWM2_SIG_INACTIVE_SEL_M  (BIT(2))
    #define MCPWM_PWM2_SIG_INACTIVE_SEL   0x1
    #define MCPWM_PWM2_SIG_INACTIVE_SEL_S    2
    
    #define MCPWM_PWM1_SIG_ACTIVE_SEL_M  (BIT(1))
    #define MCPWM_PWM1_SIG_ACTIVE_SEL   0x1
    #define MCPWM_PWM1_SIG_ACTIVE_SEL_S    1
    #define MCPWM_PWM1_SIG_INACTIVE_SEL_M  (BIT(0))
    #define MCPWM_PWM1_SIG_INACTIVE_SEL   0x1
    #define MCPWM_PWM1_SIG_INACTIVE_SEL_S    0
        //api
        #define MCPWM_API_GET_PWM4_SIG_ACT_SEL()   GET_PERI_REG_BITS(MCPWM_DTCON2,MCPWM_PWM4_SIG_ACTIVE_SEL,MCPWM_PWM4_SIG_ACTIVE_SEL_S)
        #define MCPWM_API_SET_PWM4_SIG_ACT_SEL(val) SET_PERI_REG_BITS(MCPWM_DTCON2,MCPWM_PWM4_SIG_ACTIVE_SEL,val,MCPWM_PWM4_SIG_ACTIVE_SEL_S)
        #define MCPWM_API_GET_PWM4_SIG_INACT_SEL() GET_PERI_REG_BITS(MCPWM_DTCON2,MCPWM_PWM4_SIG_INACTIVE_SEL,MCPWM_PWM4_SIG_INACTIVE_SEL_S)
        #define MCPWM_API_SET_PWM4_SIG_INACT_SEL(val) SET_PERI_REG_BITS(MCPWM_DTCON2,MCPWM_PWM4_SIG_INACTIVE_SEL,val,MCPWM_PWM4_SIG_INACTIVE_SEL_S)
        #define MCPWM_API_GET_PWM3_SIG_ACT_SEL()   GET_PERI_REG_BITS(MCPWM_DTCON2,MCPWM_PWM3_SIG_ACTIVE_SEL,MCPWM_PWM3_SIG_ACTIVE_SEL_S)
        #define MCPWM_API_SET_PWM3_SIG_ACT_SEL(val) SET_PERI_REG_BITS(MCPWM_DTCON2,MCPWM_PWM3_SIG_ACTIVE_SEL,val,MCPWM_PWM3_SIG_ACTIVE_SEL_S)
        #define MCPWM_API_GET_PWM3_SIG_INACT_SEL() GET_PERI_REG_BITS(MCPWM_DTCON2,MCPWM_PWM3_SIG_INACTIVE_SEL,MCPWM_PWM3_SIG_INACTIVE_SEL_S)
        #define MCPWM_API_SET_PWM3_SIG_INACT_SEL(val) SET_PERI_REG_BITS(MCPWM_DTCON2,MCPWM_PWM3_SIG_INACTIVE_SEL,val,MCPWM_PWM3_SIG_INACTIVE_SEL_S)
        #define MCPWM_API_GET_PWM2_SIG_ACT_SEL()   GET_PERI_REG_BITS(MCPWM_DTCON2,MCPWM_PWM2_SIG_ACTIVE_SEL,MCPWM_PWM2_SIG_ACTIVE_SEL_S)
        #define MCPWM_API_SET_PWM2_SIG_ACT_SEL(val) SET_PERI_REG_BITS(MCPWM_DTCON2,MCPWM_PWM2_SIG_ACTIVE_SEL,val,MCPWM_PWM2_SIG_ACTIVE_SEL_S)
        #define MCPWM_API_GET_PWM2_SIG_INACT_SEL() GET_PERI_REG_BITS(MCPWM_DTCON2,MCPWM_PWM2_SIG_INACTIVE_SEL,MCPWM_PWM2_SIG_INACTIVE_SEL_S)
        #define MCPWM_API_SET_PWM2_SIG_INACT_SEL(val) SET_PERI_REG_BITS(MCPWM_DTCON2,MCPWM_PWM2_SIG_INACTIVE_SEL,val,MCPWM_PWM2_SIG_INACTIVE_SEL_S)
        #define MCPWM_API_GET_PWM1_SIG_ACT_SEL()   GET_PERI_REG_BITS(MCPWM_DTCON2,MCPWM_PWM1_SIG_ACTIVE_SEL,MCPWM_PWM1_SIG_ACTIVE_SEL_S)
        #define MCPWM_API_SET_PWM1_SIG_ACT_SEL(val) SET_PERI_REG_BITS(MCPWM_DTCON2,MCPWM_PWM1_SIG_ACTIVE_SEL,val,MCPWM_PWM1_SIG_ACTIVE_SEL_S)
        #define MCPWM_API_GET_PWM1_SIG_INACT_SEL() GET_PERI_REG_BITS(MCPWM_DTCON2,MCPWM_PWM1_SIG_INACTIVE_SEL,MCPWM_PWM1_SIG_INACTIVE_SEL_S)
        #define MCPWM_API_SET_PWM1_SIG_INACT_SEL(val) SET_PERI_REG_BITS(MCPWM_DTCON2,MCPWM_PWM1_SIG_INACTIVE_SEL,val,MCPWM_PWM1_SIG_INACTIVE_SEL_S)



#define MCPWM_FLTACON   (MCPWM_REGISTER_BASE(0) + 0x20) //Fault A Control Register 
    /*
    FAOV4H 15 R/W 1'b0 
    Fault Input A PWM Override Value bits 
    1'b1: PWM output pin is driven Active on an external fault input event 
    1'b0: PWM output pin is driven Inactive on an external fault input event 
    FAOV4L 14 R/W 1'b0 
    Fault Input A PWM Override Value bits 
    1'b1: PWM output pin is driven Active on an external fault input event 
    1'b0: PWM output pin is driven Inactive on an external fault input event 
    FAOV3H 13 R/W 1'b0 
    Fault Input A PWM Override Value bits 
    1'b1: PWM output pin is driven Active on an external fault input event 
    1'b0: PWM output pin is driven Inactive on an external fault input event 
    FAOV3L 12 R/W 1'b0 
    Fault Input A PWM Override Value bits 
    1'b1: PWM output pin is driven Active on an external fault input event 
    1'b0: PWM output pin is driven Inactive on an external fault input event 
    FAOV2H 11 R/W 1'b0 
    Fault Input A PWM Override Value bits 
    1'b1: PWM output pin is driven Active on an external fault input event 
    1'b0: PWM output pin is driven Inactive on an external fault input event 
    FAOV2L 10 R/W 1'b0 
    Fault Input A PWM Override Value bits 
    1'b1: PWM output pin is driven Active on an external fault input event 
    1'b0: PWM output pin is driven Inactive on an external fault input event 
    FAOV1H 9 R/W 1'b0 
    Fault Input A PWM Override Value bits 
    1'b1: PWM output pin is driven Active on an external fault input event 
    1'b0: PWM output pin is driven Inactive on an external fault input event 
    FAOV1L 8 R/W 1'b0 
    Fault Input A PWM Override Value bits 
    1'b1: PWM output pin is driven Active on an external fault input event 
    1'b0: PWM output pin is driven Inactive on an external fault input event 
    FLTAM 7 R/W 1'b0 
    Fault A Mode bit 
    1'b1: Fault A input pin functions in Cycle-by-Cycle mode 
    1'b0: Fault A input pin latches all control pins to the programmed states in FLTACON[5:8] 
    Reserved 6~4 R 3'h0 
    Reserved 
    FAEN4 3 R/W 1'b0 
    Fault Input A Enable bit 
    1'b1: PWM4H/PWM4L pair output is controlled by FLTA pin 
    1'b0: PWM4H/PWM4L pair output is not ontrolled by FLTA pin 
    FAEN3 2 R/W 1'b0 
    Fault Input A Enable bit 
    1'b1: PWM3H/PWM3L pair output is controlled by FLTA pin 
    1'b0: PWM3H/PWM3L pair output is not ontrolled by FLTA pin 
    FAEN2 1 R/W 1'b0 
    Fault Input A Enable bit 
    1'b1: PWM2H/PWM2L pair output is controlled by FLTA pin 
    1'b0: PWM2H/PWM2L pair output is not ontrolled by FLTA pin 
    FAEN1 0 R/W 1'b0 
    Fault Input A Enable bit 
    1'b1: PWM1H/PWM1L pair output is controlled by FLTA pin 
    1'b0: PWM4H/PWM4L pair output is not ontrolled by FLTA pin  
    */
    #define MCPWM_FAULTA_OVRD_PWM4H_VAL_M   (BIT(15))
    #define MCPWM_FAULTA_OVRD_PWM4H_VAL      0x1
    #define MCPWM_FAULTA_OVRD_PWM4H_VAL_S     15
    #define MCPWM_FAULTA_OVRD_PWM4L_VAL_M   (BIT(14))
    #define MCPWM_FAULTA_OVRD_PWM4L_VAL      0x1
    #define MCPWM_FAULTA_OVRD_PWM4L_VAL_S     14
    
    #define MCPWM_FAULTA_OVRD_PWM3H_VAL_M   (BIT(13))
    #define MCPWM_FAULTA_OVRD_PWM3H_VAL      0x1
    #define MCPWM_FAULTA_OVRD_PWM3H_VAL_S     13
    #define MCPWM_FAULTA_OVRD_PWM3L_VAL_M   (BIT(12))
    #define MCPWM_FAULTA_OVRD_PWM3L_VAL      0x1
    #define MCPWM_FAULTA_OVRD_PWM3L_VAL_S     12
    
    #define MCPWM_FAULTA_OVRD_PWM2H_VAL_M   (BIT(11))
    #define MCPWM_FAULTA_OVRD_PWM2H_VAL      0x1
    #define MCPWM_FAULTA_OVRD_PWM2H_VAL_S     11
    #define MCPWM_FAULTA_OVRD_PWM2L_VAL_M   (BIT(10))
    #define MCPWM_FAULTA_OVRD_PWM2L_VAL      0x1
    #define MCPWM_FAULTA_OVRD_PWM2L_VAL_S     10
    
    #define MCPWM_FAULTA_OVRD_PWM1H_VAL_M   (BIT(9))
    #define MCPWM_FAULTA_OVRD_PWM1H_VAL      0x1
    #define MCPWM_FAULTA_OVRD_PWM1H_VAL_S     9
    #define MCPWM_FAULTA_OVRD_PWM1L_VAL_M   (BIT(8))
    #define MCPWM_FAULTA_OVRD_PWM1L_VAL      0x1
    #define MCPWM_FAULTA_OVRD_PWM1L_VAL_S     8
    
    #define MCPWM_FAULTA_MODE_M             (BIT(7))
    #define MCPWM_FAULTA_MODE              0x1
    #define MCPWM_FAULTA_MODE_S               7
    
    #define MCPWM_FAULTA_OVRD_PWM4_EN_M     (BIT(3))  
	#define MCPWM_FAULTA_OVRD_PWM4_EN        0x1
	#define MCPWM_FAULTA_OVRD_PWM4_EN_S        3
    #define MCPWM_FAULTA_OVRD_PWM3_EN_M     (BIT(2))   
	#define MCPWM_FAULTA_OVRD_PWM3_EN        0x1
	#define MCPWM_FAULTA_OVRD_PWM3_EN_S        2
    #define MCPWM_FAULTA_OVRD_PWM2_EN_M     (BIT(1))
	#define MCPWM_FAULTA_OVRD_PWM2_EN        0x1
	#define MCPWM_FAULTA_OVRD_PWM2_EN_S        1
    #define MCPWM_FAULTA_OVRD_PWM1_EN_M     (BIT(0))   
	#define MCPWM_FAULTA_OVRD_PWM1_EN          0x1
    #define MCPWM_FAULTA_OVRD_PWM1_EN_S          0   
        //api
        #define MCPWM_API_GET_FAULTA_OVRD_PWM4H_VAL()   GET_PERI_REG_BITS(MCPWM_FLTACON,MCPWM_FAULTA_OVRD_PWM4H_VAL,MCPWM_FAULTA_OVRD_PWM4H_VAL_S)
        #define MCPWM_API_SET_FAULTA_OVRD_PWM4H_VAL(val)  SET_PERI_REG_BITS(MCPWM_FLTACON,MCPWM_FAULTA_OVRD_PWM4H_VAL,val,MCPWM_FAULTA_OVRD_PWM4H_VAL_S)
        #define MCPWM_API_GET_FAULTA_OVRD_PWM4L_VAL()   GET_PERI_REG_BITS(MCPWM_FLTACON,MCPWM_FAULTA_OVRD_PWM4L_VAL,MCPWM_FAULTA_OVRD_PWM4L_VAL_S)
        #define MCPWM_API_SET_FAULTA_OVRD_PWM4L_VAL(val)  SET_PERI_REG_BITS(MCPWM_FLTACON,MCPWM_FAULTA_OVRD_PWM4L_VAL,val,MCPWM_FAULTA_OVRD_PWM4L_VAL_S)
        #define MCPWM_API_GET_FAULTA_OVRD_PWM3H_VAL()   GET_PERI_REG_BITS(MCPWM_FLTACON,MCPWM_FAULTA_OVRD_PWM3H_VAL,MCPWM_FAULTA_OVRD_PWM3H_VAL_S)
        #define MCPWM_API_SET_FAULTA_OVRD_PWM3H_VAL(val)  SET_PERI_REG_BITS(MCPWM_FLTACON,MCPWM_FAULTA_OVRD_PWM3H_VAL,val,MCPWM_FAULTA_OVRD_PWM3H_VAL_S)
        #define MCPWM_API_GET_FAULTA_OVRD_PWM3L_VAL()   GET_PERI_REG_BITS(MCPWM_FLTACON,MCPWM_FAULTA_OVRD_PWM3L_VAL,MCPWM_FAULTA_OVRD_PWM3L_VAL_S)
        #define MCPWM_API_SET_FAULTA_OVRD_PWM3L_VAL(val)  SET_PERI_REG_BITS(MCPWM_FLTACON,MCPWM_FAULTA_OVRD_PWM3L_VAL,val,MCPWM_FAULTA_OVRD_PWM3L_VAL_S)
        #define MCPWM_API_GET_FAULTA_OVRD_PWM2H_VAL()   GET_PERI_REG_BITS(MCPWM_FLTACON,MCPWM_FAULTA_OVRD_PWM2H_VAL,MCPWM_FAULTA_OVRD_PWM2H_VAL_S)
        #define MCPWM_API_SET_FAULTA_OVRD_PWM2H_VAL(val)  SET_PERI_REG_BITS(MCPWM_FLTACON,MCPWM_FAULTA_OVRD_PWM2H_VAL,val,MCPWM_FAULTA_OVRD_PWM2H_VAL_S)
        #define MCPWM_API_GET_FAULTA_OVRD_PWM2L_VAL()   GET_PERI_REG_BITS(MCPWM_FLTACON,MCPWM_FAULTA_OVRD_PWM2L_VAL,MCPWM_FAULTA_OVRD_PWM2L_VAL_S)
        #define MCPWM_API_SET_FAULTA_OVRD_PWM2L_VAL(val)  SET_PERI_REG_BITS(MCPWM_FLTACON,MCPWM_FAULTA_OVRD_PWM2L_VAL,val,MCPWM_FAULTA_OVRD_PWM2L_VAL_S)
        #define MCPWM_API_GET_FAULTA_OVRD_PWM1H_VAL()   GET_PERI_REG_BITS(MCPWM_FLTACON,MCPWM_FAULTA_OVRD_PWM1H_VAL,MCPWM_FAULTA_OVRD_PWM1H_VAL_S)
        #define MCPWM_API_SET_FAULTA_OVRD_PWM1H_VAL(val)  SET_PERI_REG_BITS(MCPWM_FLTACON,MCPWM_FAULTA_OVRD_PWM1H_VAL,val,MCPWM_FAULTA_OVRD_PWM1H_VAL_S)
        #define MCPWM_API_GET_FAULTA_OVRD_PWM1L_VAL()   GET_PERI_REG_BITS(MCPWM_FLTACON,MCPWM_FAULTA_OVRD_PWM1L_VAL,MCPWM_FAULTA_OVRD_PWM1L_VAL_S)
        #define MCPWM_API_SET_FAULTA_OVRD_PWM1L_VAL(val)  SET_PERI_REG_BITS(MCPWM_FLTACON,MCPWM_FAULTA_OVRD_PWM1L_VAL,val,MCPWM_FAULTA_OVRD_PWM1L_VAL_S)
        #define MCPWM_API_GET_FAULTA_MODE()       GET_PERI_REG_BITS(MCPWM_FLTACON,MCPWM_FAULTA_MODE,MCPWM_FAULTA_MODE_S)
        #define MCPWM_API_SET_FAULTA_MODE(val)    SET_PERI_REG_BITS(MCPWM_FLTACON,MCPWM_FAULTA_MODE,val,MCPWM_FAULTA_MODE_S)
        #define MCPWM_API_GET_FAULTA_OVRD_PWM4_EN()  GET_PERI_REG_BITS(MCPWM_FLTACON,MCPWM_FAULTA_OVRD_PWM4_EN,MCPWM_FAULTA_OVRD_PWM4_EN_S)
        #define MCPWM_API_SET_FAULTA_OVRD_PWM4_EN(val)  SET_PERI_REG_BITS(MCPWM_FLTACON,MCPWM_FAULTA_OVRD_PWM4_EN,val,MCPWM_FAULTA_OVRD_PWM4_EN_S)
        #define MCPWM_API_GET_FAULTA_OVRD_PWM3_EN()  GET_PERI_REG_BITS(MCPWM_FLTACON,MCPWM_FAULTA_OVRD_PWM3_EN,MCPWM_FAULTA_OVRD_PWM3_EN_S)
        #define MCPWM_API_SET_FAULTA_OVRD_PWM3_EN(val)  SET_PERI_REG_BITS(MCPWM_FLTACON,MCPWM_FAULTA_OVRD_PWM3_EN,val,MCPWM_FAULTA_OVRD_PWM3_EN_S)
        #define MCPWM_API_GET_FAULTA_OVRD_PWM2_EN()  GET_PERI_REG_BITS(MCPWM_FLTACON,MCPWM_FAULTA_OVRD_PWM2_EN,MCPWM_FAULTA_OVRD_PWM2_EN_S)
        #define MCPWM_API_SET_FAULTA_OVRD_PWM2_EN(val)  SET_PERI_REG_BITS(MCPWM_FLTACON,MCPWM_FAULTA_OVRD_PWM2_EN,val,MCPWM_FAULTA_OVRD_PWM2_EN_S)
        #define MCPWM_API_GET_FAULTA_OVRD_PWM1_EN()  GET_PERI_REG_BITS(MCPWM_FLTACON,MCPWM_FAULTA_OVRD_PWM1_EN,MCPWM_FAULTA_OVRD_PWM1_EN_S)
        #define MCPWM_API_SET_FAULTA_OVRD_PWM1_EN(val)  SET_PERI_REG_BITS(MCPWM_FLTACON,MCPWM_FAULTA_OVRD_PWM1_EN,val,MCPWM_FAULTA_OVRD_PWM1_EN_S)



	

#define MCPWM_FLTBCON         (MCPWM_REGISTER_BASE(0) + 0x24) //Fault B Control Register 
    /*
    FBOV4H 15 R/W 1'b0 
    Fault Input B PWM Override Value bits 
    1'b1: PWM output pin is driven Active on an external fault input event 
    1'b0: PWM output pin is driven Inactive on an external fault input event 
    FBOV4L 14 R/W 1'b0 
    Fault Input B PWM Override Value bits 
    1'b1: PWM output pin is driven Active on an external fault input event 
    1'b0: PWM output pin is driven Inactive on an external fault input event 
    FBOV3H 13 R/W 1'b0 
    Fault Input B PWM Override Value bits 
    1'b1: PWM output pin is driven Active on an external fault input event 
    1'b0: PWM output pin is driven Inactive on an external fault input event 
    FBOV3L 12 R/W 1'b0 
    Fault Input B PWM Override Value bits 
    1'b1: PWM output pin is driven Active on an external fault input event 
    1'b0: PWM output pin is driven Inactive on an external fault input event 
    FBOV2H 11 R/W 1'b0 
    Fault Input B PWM Override Value bits 
    1'b1: PWM output pin is driven Active on an external fault input event 
    1'b0: PWM output pin is driven Inactive on an external fault input event 
    FBOV2L 10 R/W 1'b0 
    Fault Input B PWM Override Value bits 
    1'b1: PWM output pin is driven Active on an external fault input event 
    1'b0: PWM output pin is driven Inactive on an external fault input event 
    FBOV1H 9 R/W 1'b0 
    Fault Input B PWM Override Value bits 
    1'b1: PWM output pin is driven Active on an external fault input event 
    1'b0: PWM output pin is driven Inactive on an external fault input event 
    FBOV1L 8 R/W 1'b0 
    Fault Input B PWM Override Value bits 
    1'b1: PWM output pin is driven Active on an external fault input event 
    1'b0: PWM output pin is driven Inactive on an external fault input event 
    FLTBM 7 R/W 1'b0 
    Fault B Mode bit 
    1'b1: Fault B input pin functions in Cycle-by-Cycle mode 
    1'b0: Fault B input pin latches all control pins to the programmed states in FLTBCON[5:8] 
    Reserved 6~4 R 3'h0 
    Reserved 
    FBEN4 3 R/W 1'b0 
    Fault Input B Enable bit 
    1'b1: PWM4H/PWM4L pair output is controlled by FLTB pin 
    1'b0: PWM4H/PWM4L pair output is not controlled by FLTB pin 
    FBEN3 2 R/W 1'b0 
    Fault Input B Enable bit 
    1'b1: PWM3H/PWM3L pair output is controlled by FLTB pin 
    1'b0: PWM3H/PWM3L pair output is not controlled by FLTB pin 
    FBEN2 1 R/W 1'b0 
    Fault Input AB enable bit 
    1'b1: PWM2H/PWM2L pair output is controlled by FLTB pin 
    1'b0: PWM2H/PWM2L pair output is not controlled by FLTB pin 
    FBEN1 0 R/W 1'b0 
    Fault Input B Enable bit 
    1'b1: PWM1H/PWM1L pair output is controlled by FLTB pin 
    1'b0: PWM4H/PWM4L pair output is not controlled by FLTB pin  
    */
    #define MCPWM_FAULTB_OVRD_PWM4H_VAL_M   (BIT(15))
    #define MCPWM_FAULTB_OVRD_PWM4H_VAL	   0x1
    #define MCPWM_FAULTB_OVRD_PWM4H_VAL_S	  15
    #define MCPWM_FAULTB_OVRD_PWM4L_VAL_M   (BIT(14))
    #define MCPWM_FAULTB_OVRD_PWM4L_VAL	   0x1
    #define MCPWM_FAULTB_OVRD_PWM4L_VAL_S	  14
        
    #define MCPWM_FAULTB_OVRD_PWM3H_VAL_M   (BIT(13))
    #define MCPWM_FAULTB_OVRD_PWM3H_VAL	   0x1
    #define MCPWM_FAULTB_OVRD_PWM3H_VAL_S	  13
    #define MCPWM_FAULTB_OVRD_PWM3L_VAL_M   (BIT(12))
    #define MCPWM_FAULTB_OVRD_PWM3L_VAL	   0x1
    #define MCPWM_FAULTB_OVRD_PWM3L_VAL_S	  12
        
    #define MCPWM_FAULTB_OVRD_PWM2H_VAL_M   (BIT(11))
    #define MCPWM_FAULTB_OVRD_PWM2H_VAL	   0x1
    #define MCPWM_FAULTB_OVRD_PWM2H_VAL_S	  11
    #define MCPWM_FAULTB_OVRD_PWM2L_VAL_M   (BIT(10))
    #define MCPWM_FAULTB_OVRD_PWM2L_VAL	   0x1
    #define MCPWM_FAULTB_OVRD_PWM2L_VAL_S	  10
        
    #define MCPWM_FAULTB_OVRD_PWM1H_VAL_M   (BIT(9))
    #define MCPWM_FAULTB_OVRD_PWM1H_VAL	   0x1
    #define MCPWM_FAULTB_OVRD_PWM1H_VAL_S	  9
    #define MCPWM_FAULTB_OVRD_PWM1L_VAL_M   (BIT(8))
    #define MCPWM_FAULTB_OVRD_PWM1L_VAL	   0x1
    #define MCPWM_FAULTB_OVRD_PWM1L_VAL_S	  8
        
    #define MCPWM_FAULTB_MODE_M			  (BIT(7))
    #define MCPWM_FAULTB_MODE 			 0x1
    #define MCPWM_FAULTB_MODE_S 			  7
        
    #define MCPWM_FAULTB_OVRD_PWM4_EN_M	  (BIT(3))	
	#define MCPWM_FAULTB_OVRD_PWM4_EN        0x1
	#define MCPWM_FAULTB_OVRD_PWM4_EN_S        3
    #define MCPWM_FAULTB_OVRD_PWM3_EN_M	  (BIT(2))	
	#define MCPWM_FAULTB_OVRD_PWM3_EN        0x1
	#define MCPWM_FAULTB_OVRD_PWM3_EN_S        2
    #define MCPWM_FAULTB_OVRD_PWM2_EN_M	  (BIT(1))
	#define MCPWM_FAULTB_OVRD_PWM2_EN        0x1
	#define MCPWM_FAULTB_OVRD_PWM2_EN_S        1
    #define MCPWM_FAULTB_OVRD_PWM1_EN_M	  (BIT(0))
	#define MCPWM_FAULTB_OVRD_PWM1_EN        0x1
	#define MCPWM_FAULTB_OVRD_PWM1_EN_S        0
        //api
        #define MCPWM_API_GET_FAULTB_OVRD_PWM4H_VAL()     GET_PERI_REG_BITS(MCPWM_FLTBCON,MCPWM_FAULTB_OVRD_PWM4H_VAL,MCPWM_FAULTB_OVRD_PWM4H_VAL_S)
        #define MCPWM_API_SET_FAULTB_OVRD_PWM4H_VAL(val)  SET_PERI_REG_BITS(MCPWM_FLTBCON,MCPWM_FAULTB_OVRD_PWM4H_VAL,val,MCPWM_FAULTB_OVRD_PWM4H_VAL_S)
        #define MCPWM_API_GET_FAULTB_OVRD_PWM4L_VAL()     GET_PERI_REG_BITS(MCPWM_FLTBCON,MCPWM_FAULTB_OVRD_PWM4L_VAL,MCPWM_FAULTB_OVRD_PWM4L_VAL_S)
        #define MCPWM_API_SET_FAULTB_OVRD_PWM4L_VAL(val)  SET_PERI_REG_BITS(MCPWM_FLTBCON,MCPWM_FAULTB_OVRD_PWM4L_VAL,val,MCPWM_FAULTB_OVRD_PWM4L_VAL_S)
        #define MCPWM_API_GET_FAULTB_OVRD_PWM3H_VAL()     GET_PERI_REG_BITS(MCPWM_FLTBCON,MCPWM_FAULTB_OVRD_PWM3H_VAL,MCPWM_FAULTB_OVRD_PWM3H_VAL_S)
        #define MCPWM_API_SET_FAULTB_OVRD_PWM3H_VAL(val)  SET_PERI_REG_BITS(MCPWM_FLTBCON,MCPWM_FAULTB_OVRD_PWM3H_VAL,val,MCPWM_FAULTB_OVRD_PWM3H_VAL_S)
        #define MCPWM_API_GET_FAULTB_OVRD_PWM3L_VAL()     GET_PERI_REG_BITS(MCPWM_FLTBCON,MCPWM_FAULTB_OVRD_PWM3L_VAL,MCPWM_FAULTB_OVRD_PWM3L_VAL_S)
        #define MCPWM_API_SET_FAULTB_OVRD_PWM3L_VAL(val)  SET_PERI_REG_BITS(MCPWM_FLTBCON,MCPWM_FAULTB_OVRD_PWM3L_VAL,val,MCPWM_FAULTB_OVRD_PWM3L_VAL_S)
        #define MCPWM_API_GET_FAULTB_OVRD_PWM2H_VAL()     GET_PERI_REG_BITS(MCPWM_FLTBCON,MCPWM_FAULTB_OVRD_PWM2H_VAL,MCPWM_FAULTB_OVRD_PWM2H_VAL_S)
        #define MCPWM_API_SET_FAULTB_OVRD_PWM2H_VAL(val)  SET_PERI_REG_BITS(MCPWM_FLTBCON,MCPWM_FAULTB_OVRD_PWM2H_VAL,val,MCPWM_FAULTB_OVRD_PWM2H_VAL_S)
        #define MCPWM_API_GET_FAULTB_OVRD_PWM2L_VAL()     GET_PERI_REG_BITS(MCPWM_FLTBCON,MCPWM_FAULTB_OVRD_PWM2L_VAL,MCPWM_FAULTB_OVRD_PWM2L_VAL_S)
        #define MCPWM_API_SET_FAULTB_OVRD_PWM2L_VAL(val)  SET_PERI_REG_BITS(MCPWM_FLTBCON,MCPWM_FAULTB_OVRD_PWM2L_VAL,val,MCPWM_FAULTB_OVRD_PWM2L_VAL_S)
        #define MCPWM_API_GET_FAULTB_OVRD_PWM1H_VAL()     GET_PERI_REG_BITS(MCPWM_FLTBCON,MCPWM_FAULTB_OVRD_PWM1H_VAL,MCPWM_FAULTB_OVRD_PWM1H_VAL_S)
        #define MCPWM_API_SET_FAULTB_OVRD_PWM1H_VAL(val)  SET_PERI_REG_BITS(MCPWM_FLTBCON,MCPWM_FAULTB_OVRD_PWM1H_VAL,val,MCPWM_FAULTB_OVRD_PWM1H_VAL_S)
        #define MCPWM_API_GET_FAULTB_OVRD_PWM1L_VAL()     GET_PERI_REG_BITS(MCPWM_FLTBCON,MCPWM_FAULTB_OVRD_PWM1L_VAL,MCPWM_FAULTB_OVRD_PWM1L_VAL_S)
        #define MCPWM_API_SET_FAULTB_OVRD_PWM1L_VAL(val)  SET_PERI_REG_BITS(MCPWM_FLTBCON,MCPWM_FAULTB_OVRD_PWM1L_VAL,val,MCPWM_FAULTB_OVRD_PWM1L_VAL_S)
        #define MCPWM_API_GET_FAULTB_MODE()               GET_PERI_REG_BITS(MCPWM_FLTBCON,MCPWM_FAULTB_MODE,MCPWM_FAULTB_MODE_S)
        #define MCPWM_API_SET_FAULTB_MODE(val)            SET_PERI_REG_BITS(MCPWM_FLTBCON,MCPWM_FAULTB_MODE,val,MCPWM_FAULTB_MODE_S)
        
        #define MCPWM_API_GET_FAULTB_OVRD_PWM4_EN()       GET_PERI_REG_BITS(MCPWM_FLTBCON,MCPWM_FAULTB_OVRD_PWM4_EN,MCPWM_FAULTB_OVRD_PWM4_EN_S)
        #define MCPWM_API_SET_FAULTB_OVRD_PWM4_EN(val)    SET_PERI_REG_BITS(MCPWM_FLTBCON,MCPWM_FAULTB_OVRD_PWM4_EN,val,MCPWM_FAULTB_OVRD_PWM4_EN_S)
        #define MCPWM_API_GET_FAULTB_OVRD_PWM3_EN()       GET_PERI_REG_BITS(MCPWM_FLTBCON,MCPWM_FAULTB_OVRD_PWM3_EN,MCPWM_FAULTB_OVRD_PWM3_EN_S)
        #define MCPWM_API_SET_FAULTB_OVRD_PWM3_EN(val)    SET_PERI_REG_BITS(MCPWM_FLTBCON,MCPWM_FAULTB_OVRD_PWM3_EN,val,MCPWM_FAULTB_OVRD_PWM3_EN_S)
        #define MCPWM_API_GET_FAULTB_OVRD_PWM2_EN()       GET_PERI_REG_BITS(MCPWM_FLTBCON,MCPWM_FAULTB_OVRD_PWM2_EN,MCPWM_FAULTB_OVRD_PWM2_EN_S)
        #define MCPWM_API_SET_FAULTB_OVRD_PWM2_EN(val)    SET_PERI_REG_BITS(MCPWM_FLTBCON,MCPWM_FAULTB_OVRD_PWM2_EN,val,MCPWM_FAULTB_OVRD_PWM2_EN_S)
        #define MCPWM_API_GET_FAULTB_OVRD_PWM1_EN()       GET_PERI_REG_BITS(MCPWM_FLTBCON,MCPWM_FAULTB_OVRD_PWM1_EN,MCPWM_FAULTB_OVRD_PWM1_EN_S)
        #define MCPWM_API_SET_FAULTB_OVRD_PWM1_EN(val)    SET_PERI_REG_BITS(MCPWM_FLTBCON,MCPWM_FAULTB_OVRD_PWM1_EN,val,MCPWM_FAULTB_OVRD_PWM1_EN_S)


#define MCPWM_OVDCON          (MCPWM_REGISTER_BASE(0) + 0x28) //Override Control Register 
    /*
    POVD4H 15 R/W 1'b1 PWM4H output override control 
    POVD4L 14 R/W 1'b1 PWM4L output override control 
    POVD3H 13 R/W 1'b1 PWM3H output override control 
    POVD3L 12 R/W 1'b1 PWM3L output override control 
    POVD2H 11 R/W 1'b1 PWM2H output override control 
    POVD2L 10 R/W 1'b1 PWM2L output override control 
    POVD1H 9 R/W 1'b1 PWM1H output override control 
    POVD1L 8 R/W 1'b1 PWM1L output override control 
    POUT4H 7 R/W 0 PWM4H override value 
    POUT4L 6 R/W 0 PWM4L override value 
    POUT3H 5 R/W 0 PWM3H override value 
    POUT3L 4 R/W 0 PWM3L override value 
    POUT2H 3 R/W 0 PWM2H override value 
    POUT2L 2 R/W 0 PWM2L override value 
    POUT1H 1 R/W 0 PWM1H override value 
    POUT1L 0 R/W 0 PWM1L override value  
    Note: 
    POVD4H-POVD4L: PWM output override enable           
    1'b1: the PWM output is controlled by PWM controller         
    1'b0:  the PWM output is override by the programmed POUTxH/L  
    POUT4H-POUT4L: PWM output override value         
    1'b1: force the PWM output to be valid         
    1'b0: force the PWM output to be invalid 
    */
    #define MCPWM_OVRD_CTRL_PWM4H_M     (BIT(15))
    #define MCPWM_OVRD_CTRL_PWM4H     0x1
    #define MCPWM_OVRD_CTRL_PWM4H_S      15
    #define MCPWM_OVRD_CTRL_PWM4L_M     (BIT(14))
    #define MCPWM_OVRD_CTRL_PWM4L     0x1
    #define MCPWM_OVRD_CTRL_PWM4L_S      14
    #define MCPWM_OVRD_CTRL_PWM3H_M     (BIT(13))
    #define MCPWM_OVRD_CTRL_PWM3H     0x1
    #define MCPWM_OVRD_CTRL_PWM3H_S      13
    #define MCPWM_OVRD_CTRL_PWM3L_M     (BIT(12))
    #define MCPWM_OVRD_CTRL_PWM3L     0x1
    #define MCPWM_OVRD_CTRL_PWM3L_S      12
    #define MCPWM_OVRD_CTRL_PWM2H_M     (BIT(11))
    #define MCPWM_OVRD_CTRL_PWM2H     0x1
    #define MCPWM_OVRD_CTRL_PWM2H_S      11
    #define MCPWM_OVRD_CTRL_PWM2L_M     (BIT(10))
    #define MCPWM_OVRD_CTRL_PWM2L     0x1
    #define MCPWM_OVRD_CTRL_PWM2L_S      10
    #define MCPWM_OVRD_CTRL_PWM1H_M     (BIT(9))
    #define MCPWM_OVRD_CTRL_PWM1H     0x1
    #define MCPWM_OVRD_CTRL_PWM1H_S      9
    #define MCPWM_OVRD_CTRL_PWM1L_M     (BIT(8))
    #define MCPWM_OVRD_CTRL_PWM1L     0x1
    #define MCPWM_OVRD_CTRL_PWM1L_S      8
    #define MCPWM_OVRD_VALUE_POUT4H_M    (BIT(7))
	#define MCPWM_OVRD_VALUE_POUT4H         0x1
	#define MCPWM_OVRD_VALUE_POUT4H_S       7
    #define MCPWM_OVRD_VALUE_POUT4L_M    (BIT(6))
	#define MCPWM_OVRD_VALUE_POUT4L         0x1
	#define MCPWM_OVRD_VALUE_POUT4L_S       6
	#define MCPWM_OVRD_VALUE_POUT3H        0x1
    #define MCPWM_OVRD_VALUE_POUT3H_M    (BIT(5))
	#define MCPWM_OVRD_VALUE_POUT3H_S       5
	#define MCPWM_OVRD_VALUE_POUT3L        0x1
    #define MCPWM_OVRD_VALUE_POUT3L_M    (BIT(4))
	#define MCPWM_OVRD_VALUE_POUT3L_S       4
	#define MCPWM_OVRD_VALUE_POUT2H         0x1
    #define MCPWM_OVRD_VALUE_POUT2H_M    (BIT(3))
	#define MCPWM_OVRD_VALUE_POUT2H_S       3
	#define MCPWM_OVRD_VALUE_POUT2L          0x1
    #define MCPWM_OVRD_VALUE_POUT2L_M    (BIT(2))
	#define MCPWM_OVRD_VALUE_POUT2L_S       2
	#define MCPWM_OVRD_VALUE_POUT1H         0x1
    #define MCPWM_OVRD_VALUE_POUT1H_M    (BIT(1))
	#define MCPWM_OVRD_VALUE_POUT1H_S       1
	#define MCPWM_OVRD_VALUE_POUT1L         0x1
    #define MCPWM_OVRD_VALUE_POUT1L_M    (BIT(0))
	#define MCPWM_OVRD_VALUE_POUT1L_S       0
        //api
        #define MCPWM_API_GET_OVRD_CTRL_PWM4H()       GET_PERI_REG_BITS(MCPWM_OVDCON,MCPWM_OVRD_CTRL_PWM4H,MCPWM_OVRD_CTRL_PWM4H_S)
        #define MCPWM_API_SET_OVRD_CTRL_PWM4H(val)    SET_PERI_REG_BITS( MCPWM_OVDCON,MCPWM_OVRD_CTRL_PWM4H,val,MCPWM_OVRD_CTRL_PWM4H_S)
        #define MCPWM_API_GET_OVRD_CTRL_PWM4L()       GET_PERI_REG_BITS(MCPWM_OVDCON,MCPWM_OVRD_CTRL_PWM4L,MCPWM_OVRD_CTRL_PWM4L_S)
        #define MCPWM_API_SET_OVRD_CTRL_PWM4L(val)    SET_PERI_REG_BITS( MCPWM_OVDCON,MCPWM_OVRD_CTRL_PWM4L,val,MCPWM_OVRD_CTRL_PWM4L_S)
        #define MCPWM_API_GET_OVRD_CTRL_PWM3H()       GET_PERI_REG_BITS(MCPWM_OVDCON,MCPWM_OVRD_CTRL_PWM3H,MCPWM_OVRD_CTRL_PWM3H_S)
        #define MCPWM_API_SET_OVRD_CTRL_PWM3H(val)    SET_PERI_REG_BITS( MCPWM_OVDCON,MCPWM_OVRD_CTRL_PWM3H,val,MCPWM_OVRD_CTRL_PWM3H_S)
        #define MCPWM_API_GET_OVRD_CTRL_PWM3L()       GET_PERI_REG_BITS(MCPWM_OVDCON,MCPWM_OVRD_CTRL_PWM3L,MCPWM_OVRD_CTRL_PWM3L_S)
        #define MCPWM_API_SET_OVRD_CTRL_PWM3L(val)    SET_PERI_REG_BITS( MCPWM_OVDCON,MCPWM_OVRD_CTRL_PWM3L,val,MCPWM_OVRD_CTRL_PWM3L_S)
        #define MCPWM_API_GET_OVRD_CTRL_PWM2H()       GET_PERI_REG_BITS(MCPWM_OVDCON,MCPWM_OVRD_CTRL_PWM2H,MCPWM_OVRD_CTRL_PWM2H_S)
        #define MCPWM_API_SET_OVRD_CTRL_PWM2H(val)    SET_PERI_REG_BITS( MCPWM_OVDCON,MCPWM_OVRD_CTRL_PWM2H,val,MCPWM_OVRD_CTRL_PWM2H_S)
        #define MCPWM_API_GET_OVRD_CTRL_PWM2L()       GET_PERI_REG_BITS(MCPWM_OVDCON,MCPWM_OVRD_CTRL_PWM2L,MCPWM_OVRD_CTRL_PWM2L_S)
        #define MCPWM_API_SET_OVRD_CTRL_PWM2L(val)    SET_PERI_REG_BITS( MCPWM_OVDCON,MCPWM_OVRD_CTRL_PWM2L,val,MCPWM_OVRD_CTRL_PWM2L_S)
        #define MCPWM_API_GET_OVRD_CTRL_PWM1H()       GET_PERI_REG_BITS(MCPWM_OVDCON,MCPWM_OVRD_CTRL_PWM1H,MCPWM_OVRD_CTRL_PWM1H_S)
        #define MCPWM_API_SET_OVRD_CTRL_PWM1H(val)    SET_PERI_REG_BITS( MCPWM_OVDCON,MCPWM_OVRD_CTRL_PWM1H,val,MCPWM_OVRD_CTRL_PWM1H_S)
        #define MCPWM_API_GET_OVRD_CTRL_PWM1L()       GET_PERI_REG_BITS(MCPWM_OVDCON,MCPWM_OVRD_CTRL_PWM1L,MCPWM_OVRD_CTRL_PWM1L_S)
        #define MCPWM_API_SET_OVRD_CTRL_PWM1L(val)    SET_PERI_REG_BITS( MCPWM_OVDCON,MCPWM_OVRD_CTRL_PWM1L,val,MCPWM_OVRD_CTRL_PWM1L_S)
        #define MCPWM_API_GET_OVRD_VAL_POUT4H()       GET_PERI_REG_BITS(MCPWM_OVDCON,MCPWM_OVRD_VALUE_POUT4H,MCPWM_OVRD_VALUE_POUT4H_S)
        #define MCPWM_API_SET_OVRD_VAL_POUT4H(val)    SET_PERI_REG_BITS( MCPWM_OVDCON,MCPWM_OVRD_VALUE_POUT4H,val,MCPWM_OVRD_VALUE_POUT4H_S)
        #define MCPWM_API_GET_OVRD_VAL_POUT4L()       GET_PERI_REG_BITS(MCPWM_OVDCON,MCPWM_OVRD_VALUE_POUT4L,MCPWM_OVRD_VALUE_POUT4L_S)
        #define MCPWM_API_SET_OVRD_VAL_POUT4L(val)    SET_PERI_REG_BITS( MCPWM_OVDCON,MCPWM_OVRD_VALUE_POUT4L,val,MCPWM_OVRD_VALUE_POUT4L_S)
        #define MCPWM_API_GET_OVRD_VAL_POUT3H()       GET_PERI_REG_BITS(MCPWM_OVDCON,MCPWM_OVRD_VALUE_POUT3H,MCPWM_OVRD_VALUE_POUT3H_S)
        #define MCPWM_API_SET_OVRD_VAL_POUT3H(val)    SET_PERI_REG_BITS( MCPWM_OVDCON,MCPWM_OVRD_VALUE_POUT3H,val,MCPWM_OVRD_VALUE_POUT3H_S)
        #define MCPWM_API_GET_OVRD_VAL_POUT3L()       GET_PERI_REG_BITS(MCPWM_OVDCON,MCPWM_OVRD_VALUE_POUT3L,MCPWM_OVRD_VALUE_POUT3L_S)
        #define MCPWM_API_SET_OVRD_VAL_POUT3L(val)    SET_PERI_REG_BITS( MCPWM_OVDCON,MCPWM_OVRD_VALUE_POUT3L,val,MCPWM_OVRD_VALUE_POUT3L_S)
        #define MCPWM_API_GET_OVRD_VAL_POUT2H()       GET_PERI_REG_BITS(MCPWM_OVDCON,MCPWM_OVRD_VALUE_POUT2H,MCPWM_OVRD_VALUE_POUT2H_S)
        #define MCPWM_API_SET_OVRD_VAL_POUT2H(val)    SET_PERI_REG_BITS( MCPWM_OVDCON,MCPWM_OVRD_VALUE_POUT2H,val,MCPWM_OVRD_VALUE_POUT2H_S)
        #define MCPWM_API_GET_OVRD_VAL_POUT2L()       GET_PERI_REG_BITS(MCPWM_OVDCON,MCPWM_OVRD_VALUE_POUT2L,MCPWM_OVRD_VALUE_POUT2L_S)
        #define MCPWM_API_SET_OVRD_VAL_POUT2L(val)    SET_PERI_REG_BITS( MCPWM_OVDCON,MCPWM_OVRD_VALUE_POUT2L,val,MCPWM_OVRD_VALUE_POUT2L_S)
        #define MCPWM_API_GET_OVRD_VAL_POUT1H()       GET_PERI_REG_BITS(MCPWM_OVDCON,MCPWM_OVRD_VALUE_POUT1H,MCPWM_OVRD_VALUE_POUT1H_S)
        #define MCPWM_API_SET_OVRD_VAL_POUT1H(val)    SET_PERI_REG_BITS( MCPWM_OVDCON,MCPWM_OVRD_VALUE_POUT1H,val,MCPWM_OVRD_VALUE_POUT1H_S)
        #define MCPWM_API_GET_OVRD_VAL_POUT1L()       GET_PERI_REG_BITS(MCPWM_OVDCON,MCPWM_OVRD_VALUE_POUT1L,MCPWM_OVRD_VALUE_POUT1L_S)
        #define MCPWM_API_SET_OVRD_VAL_POUT1L(val)    SET_PERI_REG_BITS( MCPWM_OVDCON,MCPWM_OVRD_VALUE_POUT1L,val,MCPWM_OVRD_VALUE_POUT1L_S)
        




#define MCPWM_PDC1            (MCPWM_REGISTER_BASE(0) + 0x2C) //PWM Duty Cycle Register 1 
    /*
    PDC1 15~0 R/W 16'h0 
    PWM1 output duty cycle  
    Note: PDC1[0]: the PWM output resolution          
    1'b1: clk_pwm /2 resolution         
    1'b0:  clk_pwm/2 resolution  
    */
    #define MCPWM_PWM1_OUTPUT_DUTY_CYCLE   0xffff
    #define MCPWM_PWM1_OUTPUT_DUTY_CYCLE_S      0
        //api
        #define MCPWM_API_GET_PWM1_OUTPUT_DUTY_CYCLE()     GET_PERI_REG_BITS(MCPWM_PDC1,MCPWM_PWM1_OUTPUT_DUTY_CYCLE,MCPWM_PWM1_OUTPUT_DUTY_CYCLE_S)
        #define MCPWM_API_SET_PWM1_OUTPUT_DUTY_CYCLE(val)  SET_PERI_REG_BITS( MCPWM_PDC1,MCPWM_PWM1_OUTPUT_DUTY_CYCLE,val,MCPWM_PWM1_OUTPUT_DUTY_CYCLE_S)


#define MCPWM_PDC2            (MCPWM_REGISTER_BASE(0) + 0x30) //PWM Duty Cycle Register 2 
    /*
    PDC2 15~0 R/W 16'h0 
    PWM2 output duty cycle  
    Note: PDC2[0]: the PWM output resolution          
    1'b1: clk_pwm /2 resolution         
    1'b0:  clk_pwm/2 resolution 
    */
    #define MCPWM_PWM2_OUTPUT_DUTY_CYCLE   0xffff
    #define MCPWM_PWM2_OUTPUT_DUTY_CYCLE_S		0
        //api
        #define MCPWM_API_GET_PWM2_OUTPUT_DUTY_CYCLE()     GET_PERI_REG_BITS(MCPWM_PDC2,MCPWM_PWM2_OUTPUT_DUTY_CYCLE,MCPWM_PWM2_OUTPUT_DUTY_CYCLE_S)
        #define MCPWM_API_SET_PWM2_OUTPUT_DUTY_CYCLE(val)  SET_PERI_REG_BITS( MCPWM_PDC2,MCPWM_PWM2_OUTPUT_DUTY_CYCLE,val,MCPWM_PWM2_OUTPUT_DUTY_CYCLE_S)


#define MCPWM_PDC3            (MCPWM_REGISTER_BASE(0) + 0x34) //PWM Duty Cycle Register 3 
    /*
    PDC3 15~0 R/W 16'h0 
    PWM3 output duty cycle  
    Note: PDC3[0]: the PWM output resolution          
    1'b1: clk_pwm /2 resolution         
    1'b0:  clk_pwm/2 resolution  
    */
    #define MCPWM_PWM3_OUTPUT_DUTY_CYCLE   0xffff
    #define MCPWM_PWM3_OUTPUT_DUTY_CYCLE_S      0
        //api
        #define MCPWM_API_GET_PWM3_OUTPUT_DUTY_CYCLE()     GET_PERI_REG_BITS(MCPWM_PDC3,MCPWM_PWM3_OUTPUT_DUTY_CYCLE,MCPWM_PWM3_OUTPUT_DUTY_CYCLE_S)
        #define MCPWM_API_SET_PWM3_OUTPUT_DUTY_CYCLE(val)  SET_PERI_REG_BITS( MCPWM_PDC3,MCPWM_PWM3_OUTPUT_DUTY_CYCLE,val,MCPWM_PWM3_OUTPUT_DUTY_CYCLE_S)




#define MCPWM_PDC4            (MCPWM_REGISTER_BASE(0) + 0x38) //PWM Duty Cycle Register 4 
    /*
    PDC4 15~0 R/W 16'h0 
    PWM4 output duty cycle  
    Note: PDC4[0]: the PWM output resolution          
    1'b1: clk_pwm /2 resolution         
    1'b0:  clk_pwm/2 resolution  
    */
    #define MCPWM_PWM4_OUTPUT_DUTY_CYCLE   0xffff
    #define MCPWM_PWM4_OUTPUT_DUTY_CYCLE_S      0
        //api
        #define MCPWM_API_GET_PWM4_OUTPUT_DUTY_CYCLE()     GET_PERI_REG_BITS(MCPWM_PDC4,MCPWM_PWM4_OUTPUT_DUTY_CYCLE,MCPWM_PWM4_OUTPUT_DUTY_CYCLE_S)
        #define MCPWM_API_SET_PWM4_OUTPUT_DUTY_CYCLE(val)  SET_PERI_REG_BITS( MCPWM_PDC4,MCPWM_PWM4_OUTPUT_DUTY_CYCLE,val,MCPWM_PWM4_OUTPUT_DUTY_CYCLE_S)



#define MCPWM_POLAR           (MCPWM_REGISTER_BASE(0) + 0x3C) //PWM output polarity control Register 
    /*
    Reserved 15~8 R 8'h0 Reserved 
    POLAR 7~0 R/W 8'h0 
    PWM output polarity control 
    bit[7]:  PWM4H polarity 
    bit[6]:  PWM4L polarity 
    bit[5]:  PWM3H polarity 
    bit[4]:  PWM3L polarity 
    bit[3]:  PWM2H polarity 
    bit[2]:  PWM2L polarity 
    bit[1]:  PWM1H polarity 
    bit[0]:  PWM1L polarity  
    Note1: The POLAR[7:0] bit function is as the follows           
    1'b1: for PWM output low level is valid           
    1'b0: for PWM output high level is valid 
    Note2: be care for setting the polarity of the PWM output when working under complementary mode. 
    */
    #define MCPWM_PWM4_H_OUTPUT_POLARITY_M      (BIT(7))
	#define MCPWM_PWM4_H_OUTPUT_POLARITY           0x1
	#define MCPWM_PWM4_H_OUTPUT_POLARITY_S         7
    #define MCPWM_PWM4_L_OUTPUT_POLARITY_M      (BIT(6))
	#define MCPWM_PWM4_L_OUTPUT_POLARITY           0x1
	#define MCPWM_PWM4_L_OUTPUT_POLARITY_S         6
    #define MCPWM_PWM3_H_OUTPUT_POLARITY_M      (BIT(5))
	#define MCPWM_PWM3_H_OUTPUT_POLARITY          0x1
	#define MCPWM_PWM3_H_OUTPUT_POLARITY_S         5
    #define MCPWM_PWM3_L_OUTPUT_POLARITY_M      (BIT(4))
	#define MCPWM_PWM3_L_OUTPUT_POLARITY           0x1
	#define MCPWM_PWM3_L_OUTPUT_POLARITY_S         4
    #define MCPWM_PWM2_H_OUTPUT_POLARITY_M      (BIT(3))
	#define MCPWM_PWM2_H_OUTPUT_POLARITY           0x1
	#define MCPWM_PWM2_H_OUTPUT_POLARITY_S         3
    #define MCPWM_PWM2_L_OUTPUT_POLARITY_M      (BIT(2))
	#define MCPWM_PWM2_L_OUTPUT_POLARITY           0x1
	#define MCPWM_PWM2_L_OUTPUT_POLARITY_S         2
    #define MCPWM_PWM1_H_OUTPUT_POLARITY_M      (BIT(1))
	#define MCPWM_PWM1_H_OUTPUT_POLARITY           0x1
	#define MCPWM_PWM1_H_OUTPUT_POLARITY_S         1
    #define MCPWM_PWM1_L_OUTPUT_POLARITY_M      (BIT(0))
	#define MCPWM_PWM1_L_OUTPUT_POLARITY          0x1
	#define MCPWM_PWM1_L_OUTPUT_POLARITY_S         0
        //api
        #define MCPWM_API_GET_PWM4_H_OUTPUT_POLAR()         GET_PERI_REG_BITS(MCPWM_POLAR,MCPWM_PWM4_H_OUTPUT_POLARITY,MCPWM_PWM4_H_OUTPUT_POLARITY_S)
        #define MCPWM_API_SET_PWM4_H_OUTPUT_POLAR(val)      SET_PERI_REG_BITS( MCPWM_POLAR,MCPWM_PWM4_H_OUTPUT_POLARITY,val,MCPWM_PWM4_H_OUTPUT_POLARITY_S)
        #define MCPWM_API_GET_PWM4_L_OUTPUT_POLAR()         GET_PERI_REG_BITS(MCPWM_POLAR,MCPWM_PWM4_L_OUTPUT_POLARITY,MCPWM_PWM4_L_OUTPUT_POLARITY_S)
        #define MCPWM_API_SET_PWM4_L_OUTPUT_POLAR(val)      SET_PERI_REG_BITS( MCPWM_POLAR,MCPWM_PWM4_L_OUTPUT_POLARITY,val,MCPWM_PWM4_L_OUTPUT_POLARITY_S)
        #define MCPWM_API_GET_PWM3_H_OUTPUT_POLAR()         GET_PERI_REG_BITS(MCPWM_POLAR,MCPWM_PWM3_H_OUTPUT_POLARITY,MCPWM_PWM3_H_OUTPUT_POLARITY_S)
        #define MCPWM_API_SET_PWM3_H_OUTPUT_POLAR(val)      SET_PERI_REG_BITS( MCPWM_POLAR,MCPWM_PWM3_H_OUTPUT_POLARITY,val,MCPWM_PWM3_H_OUTPUT_POLARITY_S)
        #define MCPWM_API_GET_PWM3_L_OUTPUT_POLAR()         GET_PERI_REG_BITS(MCPWM_POLAR,MCPWM_PWM3_L_OUTPUT_POLARITY,MCPWM_PWM3_L_OUTPUT_POLARITY_S)
        #define MCPWM_API_SET_PWM3_L_OUTPUT_POLAR(val)      SET_PERI_REG_BITS( MCPWM_POLAR,MCPWM_PWM3_L_OUTPUT_POLARITY,val,MCPWM_PWM3_L_OUTPUT_POLARITY_S)
        #define MCPWM_API_GET_PWM2_H_OUTPUT_POLAR()         GET_PERI_REG_BITS(MCPWM_POLAR,MCPWM_PWM2_H_OUTPUT_POLARITY,MCPWM_PWM2_H_OUTPUT_POLARITY_S)
        #define MCPWM_API_SET_PWM2_H_OUTPUT_POLAR(val)      SET_PERI_REG_BITS( MCPWM_POLAR,MCPWM_PWM2_H_OUTPUT_POLARITY,val,MCPWM_PWM2_H_OUTPUT_POLARITY_S)
        #define MCPWM_API_GET_PWM2_L_OUTPUT_POLAR()         GET_PERI_REG_BITS(MCPWM_POLAR,MCPWM_PWM2_L_OUTPUT_POLARITY,MCPWM_PWM2_L_OUTPUT_POLARITY_S)
        #define MCPWM_API_SET_PWM2_L_OUTPUT_POLAR(val)      SET_PERI_REG_BITS( MCPWM_POLAR,MCPWM_PWM2_L_OUTPUT_POLARITY,val,MCPWM_PWM2_L_OUTPUT_POLARITY_S)
        #define MCPWM_API_GET_PWM1_H_OUTPUT_POLAR()         GET_PERI_REG_BITS(MCPWM_POLAR,MCPWM_PWM1_H_OUTPUT_POLARITY,MCPWM_PWM1_H_OUTPUT_POLARITY_S)
        #define MCPWM_API_SET_PWM1_H_OUTPUT_POLAR(val)      SET_PERI_REG_BITS( MCPWM_POLAR,MCPWM_PWM1_H_OUTPUT_POLARITY,val,MCPWM_PWM1_H_OUTPUT_POLARITY_S)
        #define MCPWM_API_GET_PWM1_L_OUTPUT_POLAR()         GET_PERI_REG_BITS(MCPWM_POLAR,MCPWM_PWM1_L_OUTPUT_POLARITY,MCPWM_PWM1_L_OUTPUT_POLARITY_S)
        #define MCPWM_API_SET_PWM1_L_OUTPUT_POLAR(val)      SET_PERI_REG_BITS( MCPWM_POLAR,MCPWM_PWM1_L_OUTPUT_POLARITY,val,MCPWM_PWM1_L_OUTPUT_POLARITY_S)




#define MCPWM_PTDIV           (MCPWM_REGISTER_BASE(0) + 0x40) //PWM clock divider Register 
    /*
    PTDIV 15~0 R/W 16'h0 
    PWM clock divider The clk_pwm is divided by APB PCLK  
    */
    #define MCPWM_PWM_CLK_DIV_VAL        0xffff
    #define MCPWM_PWM_CLK_DIV_VAL_S           0
        //api
        #define MCPWM_API_GET_PWM_CLK_DIV_VAL()        GET_PERI_REG_BITS(MCPWM_PTDIV,MCPWM_PWM_CLK_DIV_VAL,MCPWM_PWM_CLK_DIV_VAL_S)
        #define MCPWM_API_SET_PWM_CLK_DIV_VAL(val)     SET_PERI_REG_BITS( MCPWM_PTDIV,MCPWM_PWM_CLK_DIV_VAL,val,MCPWM_PWM_CLK_DIV_VAL_S)



#define MCPWM_PWM_INT_ENA     (MCPWM_REGISTER_BASE(0) + 0x44) //PWM INT enable Register 
    /*
    Reserved 15~7 R 8'h0 reserved 
    CAP3_INT_ENA 6 R/W 1'b0 Capture unit3 int enable 
    CAP2_INT_ENA 5 R/W 1'b0 Capture unit2 int enable 
    CAP1_INT_ENA 4 R/W 1'b0 Capture unit1 int enable 
    FLTB_INT_ENA 3 R/W 1'b0 Fault B int enable 
    FLTA_INT_ENA 2 R/W 1'b0 Fault A int enable 
    PWM_EVENT_INT_ENA 
    1 R/W 1'b0 Special event int enable 
    PTIMER_ INT_ENA 
    0 R/W 1'b0 PTIMER int enable 
    */
    #define MCPWM_CAP_3_INT_EN_M    (BIT(6))
	#define MCPWM_CAP_3_INT_EN         0x1
	#define MCPWM_CAP_3_INT_EN_S       6
    #define MCPWM_CAP_2_INT_EN_M    (BIT(5))
	#define MCPWM_CAP_2_INT_EN         0x1
	#define MCPWM_CAP_2_INT_EN_S       5
    #define MCPWM_CAP_1_INT_EN_M    (BIT(4))
	#define MCPWM_CAP_1_INT_EN        0x1
	#define MCPWM_CAP_1_INT_EN_S       4
    #define MCPWM_FLTB_INT_EN_M     (BIT(3))
	#define MCPWM_FLTB_INT_EN         0x1
	#define MCPWM_FLTB_INT_EN_S        3
    #define MCPWM_FLTA_INT_EN_M     (BIT(2))
	#define MCPWM_FLTA_INT_EN          0x1
	#define MCPWM_FLTA_INT_EN_S        2
    #define MCPWM_SPEC_EVNT_INT_EN_M (BIT(1))
	#define MCPWM_SPEC_EVNT_INT_EN      0x1
	#define MCPWM_SPEC_EVNT_INT_EN_S    1
    #define MCPWM_PTIMER_INT_EN_M    (BIT(0))
	#define MCPWM_PTIMER_INT_EN         0x1
	#define MCPWM_PTIMER_INT_EN_S       0
        //api
        #define MCPWM_API_GET_CAP_3_INT_EN()         GET_PERI_REG_BITS(MCPWM_PWM_INT_ENA,MCPWM_CAP_3_INT_EN,MCPWM_CAP_3_INT_EN_S)
        #define MCPWM_API_SET_CAP_3_INT_EN(val)      SET_PERI_REG_BITS( MCPWM_PWM_INT_ENA,MCPWM_CAP_3_INT_EN,val,MCPWM_CAP_3_INT_EN_S)
        #define MCPWM_API_GET_CAP_2_INT_EN()         GET_PERI_REG_BITS(MCPWM_PWM_INT_ENA,MCPWM_CAP_2_INT_EN,MCPWM_CAP_2_INT_EN_S)
        #define MCPWM_API_SET_CAP_2_INT_EN(val)      SET_PERI_REG_BITS( MCPWM_PWM_INT_ENA,MCPWM_CAP_2_INT_EN,val,MCPWM_CAP_2_INT_EN_S)
        #define MCPWM_API_GET_CAP_1_INT_EN()         GET_PERI_REG_BITS(MCPWM_PWM_INT_ENA,MCPWM_CAP_1_INT_EN,MCPWM_CAP_1_INT_EN_S)
        #define MCPWM_API_SET_CAP_1_INT_EN(val)      SET_PERI_REG_BITS( MCPWM_PWM_INT_ENA,MCPWM_CAP_1_INT_EN,val,MCPWM_CAP_1_INT_EN_S)
        #define MCPWM_API_GET_FLTB_INT_EN()          GET_PERI_REG_BITS(MCPWM_PWM_INT_ENA,MCPWM_FLTB_INT_EN,MCPWM_FLTB_INT_EN_S)
        #define MCPWM_API_SET_FLTB_INT_EN(val)       SET_PERI_REG_BITS( MCPWM_PWM_INT_ENA,MCPWM_FLTB_INT_EN,val,MCPWM_FLTB_INT_EN_S)
        #define MCPWM_API_GET_FLTA_INT_EN()          GET_PERI_REG_BITS(MCPWM_PWM_INT_ENA,MCPWM_FLTA_INT_EN,MCPWM_FLTA_INT_EN_S)
        #define MCPWM_API_SET_FLTA_INT_EN(val)       SET_PERI_REG_BITS( MCPWM_PWM_INT_ENA,MCPWM_FLTA_INT_EN,val,MCPWM_FLTA_INT_EN_S)
        #define MCPWM_API_GET_SPEC_EVT_INT_EN()      GET_PERI_REG_BITS(MCPWM_PWM_INT_ENA,MCPWM_SPEC_EVNT_INT_EN,MCPWM_SPEC_EVNT_INT_EN_S)
        #define MCPWM_API_SET_SPEC_EVT_INT_EN(val)   SET_PERI_REG_BITS( MCPWM_PWM_INT_ENA,MCPWM_SPEC_EVNT_INT_EN,val,MCPWM_SPEC_EVNT_INT_EN_S)
        #define MCPWM_API_GET_PTIMER_INT_EN()        GET_PERI_REG_BITS(MCPWM_PWM_INT_ENA,MCPWM_PTIMER_INT_EN,MCPWM_PTIMER_INT_EN_S)
        #define MCPWM_API_SET_PTIMER_INT_EN(val)     SET_PERI_REG_BITS( MCPWM_PWM_INT_ENA,MCPWM_PTIMER_INT_EN,val,MCPWM_PTIMER_INT_EN_S)





#define MCPWM_PWM_INT_RAW     (MCPWM_REGISTER_BASE(0) + 0x48) //PWM INT raw Register 
    /*
    Reserved 15~7 R 8'h0 reserved 
    CAP3_INT_ENA 6 R/W 1'b0 Capture unit3 int enable 
    CAP2_INT_ENA 5 R/W 1'b0 Capture unit2 int enable 
    CAP1_INT_RAW 4 R/W 1'b0 Capture unit1 int raw 
    FLTB_INT_RAW 3 R/W 1'b0 Fault B int raw 
    FLTA_INT_RAW 2 R/W 1'b0 Fault A int raw 
    PWM_EVENT INT_RAW 
    1 R/W 1'b0 Special event int raw 
    PTIMER_ INT_RAW 
    0 R/W 1'b0 PTIMER int raw 
    */
    #define MCPWM_CAP_3_INT_RAW_M	  (BIT(6))
	#define MCPWM_CAP_3_INT_RAW       0x1
	#define MCPWM_CAP_3_INT_RAW_S      6
    #define MCPWM_CAP_2_INT_RAW_M	  (BIT(5))
	#define MCPWM_CAP_2_INT_RAW       0x1
	#define MCPWM_CAP_2_INT_RAW_S      5
    #define MCPWM_CAP_1_INT_RAW_M   (BIT(4))
	#define MCPWM_CAP_1_INT_RAW        0x1
	#define MCPWM_CAP_1_INT_RAW_S      4
    #define MCPWM_FLTB_INT_RAW_M	  (BIT(3))
	#define MCPWM_FLTB_INT_RAW        0x1
	#define MCPWM_FLTB_INT_RAW_S       3
    #define MCPWM_FLTA_INT_RAW_M	  (BIT(2))
	#define MCPWM_FLTA_INT_RAW         0x1
	#define MCPWM_FLTA_INT_RAW_S       2
    #define MCPWM_SPEC_EVNT_INT_RAW_M (BIT(1))
	#define MCPWM_SPEC_EVNT_INT_RAW      0x1
	#define MCPWM_SPEC_EVNT_INT_RAW_S    1
    #define MCPWM_PTIMER_INT_RAW_M    (BIT(0))
	#define MCPWM_PTIMER_INT_RAW         0X1
    #define MCPWM_PTIMER_INT_RAW_S       0
        //api
        #define MCPWM_API_GET_CAP_3_INT_RAW()         GET_PERI_REG_BITS(MCPWM_PWM_INT_RAW,MCPWM_CAP_3_INT_RAW,MCPWM_CAP_3_INT_RAW_S)
        #define MCPWM_API_SET_CAP_3_INT_RAW(val)      SET_PERI_REG_BITS( MCPWM_PWM_INT_RAW,MCPWM_CAP_3_INT_RAW,val,MCPWM_CAP_3_INT_RAW_S)
        #define MCPWM_API_GET_CAP_2_INT_RAW()         GET_PERI_REG_BITS(MCPWM_PWM_INT_RAW,MCPWM_CAP_2_INT_RAW,MCPWM_CAP_2_INT_RAW_S)
        #define MCPWM_API_SET_CAP_2_INT_RAW(val)      SET_PERI_REG_BITS( MCPWM_PWM_INT_RAW,MCPWM_CAP_2_INT_RAW,val,MCPWM_CAP_2_INT_RAW_S)
        #define MCPWM_API_GET_CAP_1_INT_RAW()         GET_PERI_REG_BITS(MCPWM_PWM_INT_RAW,MCPWM_CAP_1_INT_RAW,MCPWM_CAP_1_INT_RAW_S)
        #define MCPWM_API_SET_CAP_1_INT_RAW(val)      SET_PERI_REG_BITS( MCPWM_PWM_INT_RAW,MCPWM_CAP_1_INT_RAW,val,MCPWM_CAP_1_INT_RAW_S)
        #define MCPWM_API_GET_FLTB_INT_RAW()          GET_PERI_REG_BITS(MCPWM_PWM_INT_RAW,MCPWM_FLTB_INT_RAW,MCPWM_FLTB_INT_RAW_S)
        #define MCPWM_API_SET_FLTB_INT_RAW(val)       SET_PERI_REG_BITS( MCPWM_PWM_INT_RAW,MCPWM_FLTB_INT_RAW,val,MCPWM_FLTB_INT_RAW_S)
        #define MCPWM_API_GET_FLTA_INT_RAW()          GET_PERI_REG_BITS(MCPWM_PWM_INT_RAW,MCPWM_FLTA_INT_RAW,MCPWM_FLTA_INT_RAW_S)
        #define MCPWM_API_SET_FLTA_INT_RAW(val)       SET_PERI_REG_BITS( MCPWM_PWM_INT_RAW,MCPWM_FLTA_INT_RAW,val,MCPWM_FLTA_INT_RAW_S)
        #define MCPWM_API_GET_SPEC_EVT_INT_RAW()      GET_PERI_REG_BITS(MCPWM_PWM_INT_RAW,MCPWM_SPEC_EVNT_INT_RAW,MCPWM_SPEC_EVNT_INT_RAW_S)
        #define MCPWM_API_SET_SPEC_EVT_INT_RAW(val)   SET_PERI_REG_BITS( MCPWM_PWM_INT_RAW,MCPWM_SPEC_EVNT_INT_RAW,val,MCPWM_SPEC_EVNT_INT_RAW_S)
        #define MCPWM_API_GET_PTIMER_INT_RAW()        GET_PERI_REG_BITS(MCPWM_PWM_INT_RAW,MCPWM_PTIMER_INT_RAW,MCPWM_PTIMER_INT_RAW_S)
        #define MCPWM_API_SET_PTIMER_INT_RAW(val)     SET_PERI_REG_BITS( MCPWM_PWM_INT_RAW,MCPWM_PTIMER_INT_RAW,val,MCPWM_PTIMER_INT_RAW_S)


#define MCPWM_PWM_INT_ST      (MCPWM_REGISTER_BASE(0) + 0x4C) //PWM INT state Register
    /*
    Reserved 15~7 R 8'h0 reserved 
    CAP3_INT_ST 6 R/W 1'b0 Capture unit3 int state 
    CAP2_INT_ST 5 R/W 1'b0 Capture unit2 int state 
    CAP1_INT_ST 4 R/W 1'b0 Capture unit1 int state 
    FLTB_INT_ST 3 R/W 1'b0 Fault B int state 
    FLTA_INT_ST 2 R/W 1'b0 Fault A int state 
    PWM_EVENT INT_ST 
    1 R/W 1'b0 Special event int state 
    PTIMER_ INT_ST 
    0 R/W 1'b0 PTIMER int state 
    */
    #define MCPWM_CAP_3_INT_ST_M   (BIT(6))
	#define MCPWM_CAP_3_INT_ST       0x1
	#define MCPWM_CAP_3_INT_ST_S      6
    #define MCPWM_CAP_2_INT_ST_M   (BIT(5))
	#define MCPWM_CAP_2_INT_ST       0x1
    #define MCPWM_CAP_2_INT_ST_S      5
	#define MCPWM_CAP_1_INT_ST_M   (BIT(4))
	#define MCPWM_CAP_1_INT_ST       0x1
    #define MCPWM_CAP_1_INT_ST_S      4
	#define MCPWM_FLTB_INT_ST_M	  (BIT(3))
	#define MCPWM_FLTB_INT_ST         0x1
    #define MCPWM_FLTB_INT_ST_S        3
	#define MCPWM_FLTA_INT_ST_M	  (BIT(2))
	#define MCPWM_FLTA_INT_ST         0x1
    #define MCPWM_FLTA_INT_ST_S        2
	#define MCPWM_SPEC_EVNT_INT_ST_M (BIT(1))
	#define MCPWM_SPEC_EVNT_INT_ST      0x1
    #define MCPWM_SPEC_EVNT_INT_ST_S    1
	#define MCPWM_PTIMER_INT_ST_M	(BIT(0))
	#define MCPWM_PTIMER_INT_ST      0x1
    #define MCPWM_PTIMER_INT_ST_S    0 
        //api
        #define MCPWM_API_GET_CAP_3_INT_ST()         GET_PERI_REG_BITS(MCPWM_PWM_INT_ST,MCPWM_CAP_3_INT_ST,MCPWM_CAP_3_INT_ST_S)
        #define MCPWM_API_SET_CAP_3_INT_ST(val)      SET_PERI_REG_BITS( MCPWM_PWM_INT_ST,MCPWM_CAP_3_INT_ST,val,MCPWM_CAP_3_INT_ST_S)
        #define MCPWM_API_GET_CAP_2_INT_ST()         GET_PERI_REG_BITS(MCPWM_PWM_INT_ST,MCPWM_CAP_2_INT_ST,MCPWM_CAP_2_INT_ST_S)
        #define MCPWM_API_SET_CAP_2_INT_ST(val)      SET_PERI_REG_BITS( MCPWM_PWM_INT_ST,MCPWM_CAP_2_INT_ST,val,MCPWM_CAP_2_INT_ST_S)
        #define MCPWM_API_GET_CAP_1_INT_ST()         GET_PERI_REG_BITS(MCPWM_PWM_INT_ST,MCPWM_CAP_1_INT_ST,MCPWM_CAP_1_INT_ST_S)
        #define MCPWM_API_SET_CAP_1_INT_ST(val)      SET_PERI_REG_BITS( MCPWM_PWM_INT_ST,MCPWM_CAP_1_INT_ST,val,MCPWM_CAP_1_INT_ST_S)
        #define MCPWM_API_GET_FLTB_INT_ST()          GET_PERI_REG_BITS(MCPWM_PWM_INT_ST,MCPWM_FLTB_INT_ST,MCPWM_FLTB_INT_ST_S)
        #define MCPWM_API_SET_FLTB_INT_ST(val)       SET_PERI_REG_BITS( MCPWM_PWM_INT_ST,MCPWM_FLTB_INT_ST,val,MCPWM_FLTB_INT_ST_S)
        #define MCPWM_API_GET_FLTA_INT_ST()          GET_PERI_REG_BITS(MCPWM_PWM_INT_ST,MCPWM_FLTA_INT_ST,MCPWM_FLTA_INT_ST_S)
        #define MCPWM_API_SET_FLTA_INT_ST(val)       SET_PERI_REG_BITS( MCPWM_PWM_INT_ST,MCPWM_FLTA_INT_ST,val,MCPWM_FLTA_INT_ST_S)
        #define MCPWM_API_GET_SPEC_EVT_INT_ST()      GET_PERI_REG_BITS(MCPWM_PWM_INT_ST,MCPWM_SPEC_EVNT_INT_ST,MCPWM_SPEC_EVNT_INT_ST_S)
        #define MCPWM_API_SET_SPEC_EVT_INT_ST(val)   SET_PERI_REG_BITS( MCPWM_PWM_INT_ST,MCPWM_SPEC_EVNT_INT_ST,val,MCPWM_SPEC_EVNT_INT_ST_S)
        #define MCPWM_API_GET_PTIMER_INT_ST()        GET_PERI_REG_BITS(MCPWM_PWM_INT_ST,MCPWM_PTIMER_INT_ST,MCPWM_PTIMER_INT_ST_S)
        #define MCPWM_API_SET_PTIMER_INT_ST(val)     SET_PERI_REG_BITS( MCPWM_PWM_INT_ST,MCPWM_PTIMER_INT_ST,val,MCPWM_PTIMER_INT_ST_S)
	


#define MCPWM_PWM_INT_CLR     (MCPWM_REGISTER_BASE(0) + 0x50) //PWM INT clear Register 
    /*
    Reserved 15~7 R 8'h0 reserved 
    CAP3_INT_CLR 6 W 1'b0 Write 1'b1 will clear capture unit3 int raw 
    CAP2_INT_CLR 5 W 1'b0 
    Write 1'b1 will clear capture unit2 int raw 
    CAP1_INT_CLR 4 W 1'b0 
    Write 1'b1 will clear capture unit1 int raw FLTB_INT_CLR 3 W 1'b0 Write 1'b1 will clear Fault B int raw 
    FLTA_INT_CLR 2 W 1'b0 Write 1'b1 will clear Fault A int raw 
    PWM_EVENT INT_CLR 
    1 W 1'b0 Write 1'b1 will clear Special event int raw 
    PTIMER_ INT_CLR 
    0 W 1'b0 Write 1'b1 will clear PTIMER int raw 
    */
    #define MCPWM_CAP_3_INT_CLR_M	 (BIT(6))
	#define MCPWM_CAP_3_INT_CLR      0x1
	#define MCPWM_CAP_3_INT_CLR_S     6
    #define MCPWM_CAP_2_INT_CLR_M	 (BIT(5))
	#define MCPWM_CAP_2_INT_CLR      0x1
    #define MCPWM_CAP_2_INT_CLR_S     5
	#define MCPWM_CAP_1_INT_CLR_M	 (BIT(4))
	#define MCPWM_CAP_1_INT_CLR       0x1
    #define MCPWM_CAP_1_INT_CLR_S     4
	#define MCPWM_FLTB_INT_CLR_M	  (BIT(3))
	#define MCPWM_FLTB_INT_CLR         0x1
    #define MCPWM_FLTB_INT_CLR_S       3
	#define MCPWM_FLTA_INT_CLR_M	  (BIT(2))
	#define MCPWM_FLTA_INT_CLR        0x1
    #define MCPWM_FLTA_INT_CLR_S       2
	#define MCPWM_SPEC_EVNT_INT_CLR_M (BIT(1))
	#define MCPWM_SPEC_EVNT_INT_CLR      0x1
    #define MCPWM_SPEC_EVNT_INT_CLR_S    1
	#define MCPWM_PTIMER_INT_CLR_M (BIT(0))
	#define MCPWM_PTIMER_INT_CLR     0x1
    #define MCPWM_PTIMER_INT_CLR_S    0

        //api
        #define MCPWM_API_SET_CAP_3_INT_CLR(val)      SET_PERI_REG_BITS( MCPWM_PWM_INT_CLR,MCPWM_CAP_3_INT_CLR,val,MCPWM_CAP_3_INT_CLR_S)
        #define MCPWM_API_SET_CAP_2_INT_CLR(val)      SET_PERI_REG_BITS( MCPWM_PWM_INT_CLR,MCPWM_CAP_2_INT_CLR,val,MCPWM_CAP_2_INT_CLR_S)
        #define MCPWM_API_SET_CAP_1_INT_CLR(val)      SET_PERI_REG_BITS( MCPWM_PWM_INT_CLR,MCPWM_CAP_1_INT_CLR,val,MCPWM_CAP_1_INT_CLR_S)
        #define MCPWM_API_SET_FLTB_INT_CLR(val)       SET_PERI_REG_BITS( MCPWM_PWM_INT_CLR,MCPWM_FLTB_INT_CLR,val,MCPWM_FLTB_INT_CLR_S)
        #define MCPWM_API_SET_FLTA_INT_CLR(val)       SET_PERI_REG_BITS( MCPWM_PWM_INT_CLR,MCPWM_FLTA_INT_CLR,val,MCPWM_FLTA_INT_CLR_S)
        #define MCPWM_API_SET_SPEC_EVT_INT_CLR(val)   SET_PERI_REG_BITS( MCPWM_PWM_INT_CLR,MCPWM_SPEC_EVNT_INT_CLR,val,MCPWM_SPEC_EVNT_INT_CLR_S)
        #define MCPWM_API_SET_PTIMER_INT_CLR(val)     SET_PERI_REG_BITS( MCPWM_PWM_INT_CLR,MCPWM_PTIMER_INT_CLR,val,MCPWM_PTIMER_INT_CLR_S)
		
		





#define MCPWM_CAP_MOD         (MCPWM_REGISTER_BASE(0) + 0x54) //Capture mode control Register 
    /*
    Reserved 15~6 R 8'h0 Reserved 
    CAP3_MOD 5~4 R/W 2'h0 
    Capture3 working mode 
    CAP2_MOD 3~2 R/W 2'h0 
    Capture1 working mode 
    CAP1_MOD 1~0 R/W 2'h0 Capture1 working mode  
    Note: CAPx_MOD(x=1,2,3) bit function is as the follows:         
    2'b00:  capture unit is disabled         
    2'b01:  capture input posedge detection         
    2'b10:  capture input negedge detection         
    2'b11:  capture input posedge and negedge detection  
    */
    #define MCPWM_CAP_ENA_M    (BIT(15))
    #define MCPWM_CAP_3_MODE   0x3
    #define MCPWM_CAP_3_MODE_S   4
    #define MCPWM_CAP_2_MODE   0x3
    #define MCPWM_CAP_2_MODE_S   2
    #define MCPWM_CAP_1_MODE   0x3
    #define MCPWM_CAP_1_MODE_S   0
        //api
        #define MCPWM_API_GET_CAP_3_MODE()        GET_PERI_REG_BITS(MCPWM_CAP_MOD,MCPWM_CAP_3_MODE,MCPWM_CAP_3_MODE_S)
        #define MCPWM_API_SET_CAP_3_MODE(val)     SET_PERI_REG_BITS( MCPWM_CAP_MOD,MCPWM_CAP_3_MODE,val,MCPWM_CAP_3_MODE_S)
        #define MCPWM_API_GET_CAP_2_MODE()        GET_PERI_REG_BITS(MCPWM_CAP_MOD,MCPWM_CAP_2_MODE,MCPWM_CAP_2_MODE_S)
        #define MCPWM_API_SET_CAP_2_MODE(val)     SET_PERI_REG_BITS( MCPWM_CAP_MOD,MCPWM_CAP_2_MODE,val,MCPWM_CAP_2_MODE_S)
        #define MCPWM_API_GET_CAP_1_MODE()        GET_PERI_REG_BITS(MCPWM_CAP_MOD,MCPWM_CAP_1_MODE,MCPWM_CAP_1_MODE_S)
        #define MCPWM_API_SET_CAP_1_MODE(val)     SET_PERI_REG_BITS( MCPWM_CAP_MOD,MCPWM_CAP_1_MODE,val,MCPWM_CAP_1_MODE_S)


#define MCPWM_CAP_ST          (MCPWM_REGISTER_BASE(0) + 0x58) //Capture state Register 
    /*
    Reserved 15~6 R 9'h00 Reserved 
    CAP3_ST 5~4 R/W 2'h0 
    Capture3 current state 
    CAP2_ST 3~2 R/W 2'h0 
    Capture1 current state 
    CAP1_ST 1~0 R/W 2'h0 Capture1 current state  
    Note: CAPx_ST(x=1,2,3) bits functions is as the follows:          
    2'b00: capture unit is idle          
    2'b01: capture detected the posedge of cap_in         
    2'b10:  capture detected the negedge of cap_in         
    2'b11:  reserved  
    */
    #define MCPWM_CAP_3_ST    0x3
    #define MCPWM_CAP_3_ST_S    4
    #define MCPWM_CAP_2_ST    0x3
    #define MCPWM_CAP_2_ST_S    2
    #define MCPWM_CAP_1_ST    0x3
    #define MCPWM_CAP_1_ST_S    0
        //api
        #define MCPWM_API_GET_CAP_3_ST()        GET_PERI_REG_BITS(MCPWM_CAP_ST,MCPWM_CAP_3_ST,MCPWM_CAP_3_ST_S)
        #define MCPWM_API_SET_CAP_3_ST(val)     SET_PERI_REG_BITS( MCPWM_CAP_ST,MCPWM_CAP_3_ST,val,MCPWM_CAP_3_ST_S)
        #define MCPWM_API_GET_CAP_2_ST()        GET_PERI_REG_BITS(MCPWM_CAP_ST,MCPWM_CAP_2_ST,MCPWM_CAP_2_ST_S)
        #define MCPWM_API_SET_CAP_2_ST(val)     SET_PERI_REG_BITS( MCPWM_CAP_ST,MCPWM_CAP_2_ST,val,MCPWM_CAP_2_ST_S)
        #define MCPWM_API_GET_CAP_1_ST()        GET_PERI_REG_BITS(MCPWM_CAP_ST,MCPWM_CAP_1_ST,MCPWM_CAP_1_ST_S)
        #define MCPWM_API_SET_CAP_1_ST(val)     SET_PERI_REG_BITS( MCPWM_CAP_ST,MCPWM_CAP_1_ST,val,MCPWM_CAP_1_ST_S)



#define MCPWM_CAP1_TIME       (MCPWM_REGISTER_BASE(0) + 0x5C) //Capture unit1 recorded time 
    /*
    Reserved 15 R 1'b0 Reserved 
    CAP1_TIME 14~0 R/W 15'h0 Capture unit1 recorded time 
    */
    #define MCPWM_CAP_1_REC_VAL     0x7fff
    #define MCPWM_CAP_1_REC_VAL_S        0
        //api
        #define MCPWM_API_GET_CAP_1_REC_VAL()     GET_PERI_REG_BITS(MCPWM_CAP1_TIME,MCPWM_CAP_1_REC_VAL,MCPWM_CAP_1_REC_VAL_S)
        #define MCPWM_API_SET_CAP_1_REC_VAL(val)  SET_PERI_REG_BITS( MCPWM_CAP1_TIME,MCPWM_CAP_1_REC_VAL,val,MCPWM_CAP_1_REC_VAL_S)


#define MCPWM_CAP2_TIME       (MCPWM_REGISTER_BASE(0) + 0x60) //Capture unit2 recorded time 
    /*
    Reserved 15 R 1'b0 Reserved 
    CAP2_TIME 14~0 R/W 15'h0 Capture unit2 recorded time 
    */
    #define MCPWM_CAP_2_REC_VAL     0x7fff
    #define MCPWM_CAP_2_REC_VAL_S        0
        //api
        #define MCPWM_API_GET_CAP_2_REC_VAL()     GET_PERI_REG_BITS(MCPWM_CAP2_TIME,MCPWM_CAP_2_REC_VAL,MCPWM_CAP_2_REC_VAL_S)
        #define MCPWM_API_SET_CAP_2_REC_VAL(val)  SET_PERI_REG_BITS( MCPWM_CAP2_TIME,MCPWM_CAP_2_REC_VAL,val,MCPWM_CAP_2_REC_VAL_S)



#define MCPWM_CAP3_TIME       (MCPWM_REGISTER_BASE(0) + 0x64) //Capture unit3 recorded time 
    /*
    Reserved 15 R 1'b0 Reserved 
    CAP3_TIME 14~0 R/W 15'h0 Capture unit3 recorded time 
    */
    #define MCPWM_CAP_3_REC_VAL     0x7fff
    #define MCPWM_CAP_3_REC_VAL_S        0
        //api
        #define MCPWM_API_GET_CAP_3_REC_VAL()     GET_PERI_REG_BITS(MCPWM_CAP3_TIME,MCPWM_CAP_3_REC_VAL,MCPWM_CAP_3_REC_VAL_S)
        #define MCPWM_API_SET_CAP_3_REC_VAL(val)  SET_PERI_REG_BITS( MCPWM_CAP3_TIME,MCPWM_CAP_3_REC_VAL,val,MCPWM_CAP_3_REC_VAL_S)
        
#define MCPWM_PWM_ST          (MCPWM_REGISTER_BASE(0) + 0x68) // PWM state register   
    /*
    Reserved 15~7 R 1'b0 Reserved 
    CAP3_IN 6 R 1'b0 Capture unit3 in state 
    CAP2_IN 5 R 1'b0 Capture unit2 in state 
    CAP1_IN 4 R 1'b0 Capture unit1 in state 
    FLTB 3 R 1'b0 Fault B in state 
    FLTA 2 R 1'b0 Fault A in state 
    PWM_EVENT 1 R 1'b0 Special event state 
    PTINT 0 R 1'b0 PTIMER int state 
    */
    #define MCPWM_CAP_3_IN_ST_M      (BIT(6))
    #define MCPWM_CAP_3_IN_ST       0x1
    #define MCPWM_CAP_3_IN_ST_S        6
    #define MCPWM_CAP_2_IN_ST_M      (BIT(5))
    #define MCPWM_CAP_2_IN_ST       0x1
    #define MCPWM_CAP_2_IN_ST_S        5
    #define MCPWM_CAP_1_IN_ST_M      (BIT(4))
    #define MCPWM_CAP_1_IN_ST       0x1
    #define MCPWM_CAP_1_IN_ST_S        4
    
    #define MCPWM_FLT_B_IN_ST_M       (BIT(3))
    #define MCPWM_FLT_B_IN_ST       0x1
    #define MCPWM_FLT_B_IN_ST_S        3
    #define MCPWM_FLT_A_IN_ST_M       (BIT(2))
    #define MCPWM_FLT_A_IN_ST       0x1
    #define MCPWM_FLT_A_IN_ST_S        2
    
    #define MCPWM_SPEC_EVNT_ST_M       (BIT(1))
    #define MCPWM_SPEC_EVNT_ST      0x1
    #define MCPWM_SPEC_EVNT_ST_S       1
    #define MCPWM_PWM_PTIMER_INT_ST_M   (BIT(0))
    #define MCPWM_PWM_PTIMER_IN_ST   0x1
    #define MCPWM_PWM_PTIMER_IN_ST_S    0
        //api
        #define MCPWM_API_GET_CAP3_IN_ST()         GET_PERI_REG_BITS(MCPWM_PWM_ST,MCPWM_CAP_3_IN_ST,MCPWM_CAP_3_IN_ST_S)
        #define MCPWM_API_GET_CAP2_IN_ST()         GET_PERI_REG_BITS(MCPWM_PWM_ST,MCPWM_CAP_2_IN_ST,MCPWM_CAP_2_IN_ST_S)
        #define MCPWM_API_GET_CAP1_IN_ST()         GET_PERI_REG_BITS(MCPWM_PWM_ST,MCPWM_CAP_1_IN_ST,MCPWM_CAP_1_IN_ST_S)
        #define MCPWM_API_GET_FLT_A_IN_ST()        GET_PERI_REG_BITS(MCPWM_PWM_ST,MCPWM_FLT_A_IN_ST,MCPWM_FLT_A_IN_ST_S)
        #define MCPWM_API_GET_FLT_B_IN_ST()        GET_PERI_REG_BITS(MCPWM_PWM_ST,MCPWM_FLT_B_IN_ST,MCPWM_FLT_B_IN_ST_S)
        #define MCPWM_API_GET_SPEC_EVT_ST()        GET_PERI_REG_BITS(MCPWM_PWM_ST,MCPWM_SPEC_EVNT_ST,MCPWM_SPEC_EVNT_ST_S)
        #define MCPWM_API_GET_PTIMER_IN_ST()      GET_PERI_REG_BITS(MCPWM_PWM_ST,MCPWM_PWM_PTIMER_IN_ST,MCPWM_PWM_PTIMER_IN_ST_S)


#endif

