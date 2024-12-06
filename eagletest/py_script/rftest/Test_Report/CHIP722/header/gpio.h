/* 
 * copyright (c) Espressif System 2010
 * 
 */
#ifndef GPIO_H_INCLUDED
#define GPIO_H_INCLUDED

#include <xtensa/hal.h>
#include <xtensa/config/core.h>
#include <xtensa/config/system.h>
#include "./diag_utils.h"
#include "ip_common.h"
#include "gpio_reg.h"
#include "rtc_io_reg.h"
#include "rtc_cntl_reg.h"
#include "io_mux_reg.h"
 
U32 gpio_pending_mask;
U32 gpio_pending_mask_high;

void
gpio_output_set(U32 set_mask,
        U32 clear_mask,
        U32 enable_mask,
        U32 disable_mask)
{

    WRITE_PERI_REG(GPIO_OUT_W1TS_REG, set_mask);
    WRITE_PERI_REG(GPIO_OUT_W1TC_REG, clear_mask);
    WRITE_PERI_REG(GPIO_ENABLE_W1TS_REG, enable_mask);
    WRITE_PERI_REG(GPIO_ENABLE_W1TC_REG, disable_mask);
}

void
gpio_output_set_high(U32 set_mask,
        U32 clear_mask,
        U32 enable_mask,
        U32 disable_mask)
{

    WRITE_PERI_REG(GPIO_OUT1_W1TS_REG, set_mask);
    WRITE_PERI_REG(GPIO_OUT1_W1TC_REG, clear_mask);
    WRITE_PERI_REG(GPIO_ENABLE1_W1TS_REG, enable_mask);
    WRITE_PERI_REG(GPIO_ENABLE1_W1TC_REG, disable_mask);
}


U32
gpio_input_get(void)
{
    U32 gpio_in;

    gpio_in = READ_PERI_REG(GPIO_IN_REG);
    return gpio_in;
}

U32
gpio_input_get_high(void)
{
    U32 gpio_in;

    gpio_in = READ_PERI_REG(GPIO_IN1_REG);
    return gpio_in;
}

U32
gpio_intr_pending(void)
{
    return gpio_pending_mask;
}

U32
gpio_intr_pending_high(void)
{
    return gpio_pending_mask_high;
}

/*
 * set gpio input to a signal
 * one gpio can input to several signals
 * If gpio == 0x30, cancel input to the signal, input 0 to signal
 * If gpio == 0x38, cancel input to the signal, input 1 to signal, for I2C pad
 */
void gpio_matrix_in(U32 gpio, U32 signal_idx, U32 inv)
{
    U32 addr = GPIO_FUNC0_IN_SEL_CFG_REG + (signal_idx * 4);
    U32 value = (gpio<< GPIO_FUNC0_IN_SEL_S);
    if(inv)
        value |= GPIO_FUNC0_IN_INV_SEL;
    if(gpio != 0x34)
        value |= GPIO_SIG0_IN_SEL;
    WRITE_PERI_REG(addr, value);

}

/*
 * set signal output to gpio
 * one signal can output to several gpios
 * If signal_idx == 0x100, cancel output put to the gpio
 */
#define INVALID_SIGNAL 0x100
#define GPIO_PIN_COUNT 46
void gpio_matrix_out(U32 gpio, U32 signal_idx, U32 out_inv, U32 oen_inv)
{
    U32 addr = GPIO_FUNC0_OUT_SEL_CFG_REG + (gpio * 4);
    U32 pin_reg;
    U32 value = signal_idx << GPIO_FUNC0_OUT_SEL_S;

    if (gpio >= GPIO_PIN_COUNT) {
        return;
    }

    if (gpio < 46) {
        pin_reg = (1 << gpio);
        WRITE_PERI_REG(GPIO_ENABLE_W1TS_REG, pin_reg);
    } else {
        pin_reg = (1 << (gpio - 46));
        WRITE_PERI_REG(GPIO_ENABLE1_W1TS_REG, pin_reg);
    }

    if(out_inv)
        value |= GPIO_FUNC0_OUT_INV_SEL;
    if(oen_inv)
        value |= GPIO_FUNC0_OEN_INV_SEL;
    WRITE_PERI_REG(addr, value);

}

void gpio_pad_select_gpio(U8 gpio_num)
{
    switch(gpio_num){
        case 0://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO0_U, 1);
            break;
        case 1://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO1_U, 1);
            break;
        case 2://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO2_U, 1);
            break;
        case 3://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO3_U, 1);
            break;
        case 4://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO4_U, 1);
            break;
        case 5://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO5_U, 1);
            break;
        case 6:
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO6_U, 1);
            break;
        case 7:
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO7_U, 1);
            break;
        case 8:
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO8_U, 1);
            break;
        case 9:
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO9_U, 1);
            break;
        case 10:
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO10_U, 1);
            break;
        case 11:
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO11_U, 1);
            break;
        case 12://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO12_U, 1);
            break;
        case 13://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO13_U, 1);
            break;
        case 14://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO14_U, 1);
            break;
        case 15://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_XTAL_32K_P_U, 1);
            break;
        case 16:
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_XTAL_32K_N_U, 1);
            break;
        case 17:
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_DAC_1_U, 1);
            break;
        case 18:
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_DAC_2_U, 1);
            break;
        case 19:
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO19_U, 1);
            break;
        case 20:
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO20_U, 1);
            break;
        case 21:
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO21_U, 1);
            break;
        case 26://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_SPICS1_U, 1);
            break;
        case 27://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_SPIHD_U, 1);
            break;
        case 28://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_SPIWP_U, 1);
            break;
        case 29://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_SPICS0_U, 1);
            break;
        case 30://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_SPICLK_U, 1);
            break;
        case 31://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_SPIQ_U, 1);
            break;
        case 32://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_SPID_U, 1);
            break;
        case 33://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO33_U, 1);
            break;
        case 34://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO34_U, 1);
            break;
        case 35://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO35_U, 1);
            break;
        case 36://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO36_U, 1);
            break;
        case 37://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO37_U, 1);
            break;
        case 38://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO38_U, 1);
            break;
        case 39://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_MTCK_U, 1);
            break;
        case 40://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_MTDO_U, 1);
            break;
        case 41://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_MTDI_U, 1);
            break;
        case 42://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_MTMS_U, 1);
            break;
        case 43://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_U0TXD_U, 1);
            break;
        case 44://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_U0RXD_U, 1);
            break;
        case 45://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO45_U, 1);
            break;
        case 46://
            PIN_FUNC_SELECT(PERIPHS_IO_MUX_GPIO46_U, 1);
            break;
        default:
            break;
    }

}

void gpio_pad_ie_set(U8 gpio_num)
{
    switch(gpio_num){
        case 0://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO0_U, FUN_IE);
            break;
        case 1://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO1_U, FUN_IE);
            break;
        case 2://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO2_U, FUN_IE);
            break;
        case 3://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO3_U, FUN_IE);
            break;
        case 4://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO4_U, FUN_IE);
            break;
        case 5://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO5_U, FUN_IE);
            break;
        case 6:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO6_U, FUN_IE);
            break;
        case 7:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO7_U, FUN_IE);
            break;
        case 8:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO8_U, FUN_IE);
            break;
        case 9:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO9_U, FUN_IE);
            break;
        case 10:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO10_U, FUN_IE);
            break;
        case 11:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO11_U, FUN_IE);
            break;
        case 12://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO12_U, FUN_IE);
            break;
        case 13://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO13_U, FUN_IE);
            break;
        case 14://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO14_U, FUN_IE);
            break;
        case 15://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_XTAL_32K_P_U, FUN_IE);
            break;
        case 16:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_XTAL_32K_N_U, FUN_IE);
            break;
        case 17:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_DAC_1_U, FUN_IE);
            break;
        case 18:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_DAC_2_U, FUN_IE);
            break;
        case 19:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO19_U, FUN_IE);
            break;
        case 20:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO20_U, FUN_IE);
            break;
        case 21:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO21_U, FUN_IE);
            break;
        case 26://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_SPICS1_U, FUN_IE);
            break;
        case 27://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_SPIHD_U, FUN_IE);
            break;
        case 28://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_SPIWP_U, FUN_IE);
            break;
        case 29://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_SPICS0_U, FUN_IE);
            break;
        case 30://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_SPICLK_U, FUN_IE);
            break;
        case 31://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_SPIQ_U, FUN_IE);
            break;
        case 32://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_SPID_U, FUN_IE);
            break;
        case 33://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO33_U, FUN_IE);
            break;
        case 34://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO34_U, FUN_IE);
            break;
        case 35://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO35_U, FUN_IE);
            break;
        case 36://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO36_U, FUN_IE);
            break;
        case 37://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO37_U, FUN_IE);
            break;
        case 38://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO38_U, FUN_IE);
            break;
        case 39://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_MTCK_U, FUN_IE);
            break;
        case 40://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_MTDO_U, FUN_IE);
            break;
        case 41://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_MTDI_U, FUN_IE);
            break;
        case 42://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_MTMS_U, FUN_IE);
            break;
        case 43://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_U0TXD_U, FUN_IE);
            break;
        case 44://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_U0RXD_U, FUN_IE);
            break;
        case 45://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO45_U, FUN_IE);
            break;
        case 46://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO46_U, FUN_IE);
            break;
        default:
            break;
    }
}

void gpio_pad_ie_clear(U8 gpio_num)
{
    switch(gpio_num){
        case 0://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO0_U, FUN_IE);
            break;
        case 1://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO1_U, FUN_IE);
            break;
        case 2://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO2_U, FUN_IE);
            break;
        case 3://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO3_U, FUN_IE);
            break;
        case 4://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO4_U, FUN_IE);
            break;
        case 5://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO5_U, FUN_IE);
            break;
        case 6:
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO6_U, FUN_IE);
            break;
        case 7:
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO7_U, FUN_IE);
            break;
        case 8:
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO8_U, FUN_IE);
            break;
        case 9:
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO9_U, FUN_IE);
            break;
        case 10:
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO10_U, FUN_IE);
            break;
        case 11:
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO11_U, FUN_IE);
            break;
        case 12://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO12_U, FUN_IE);
            break;
        case 13://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO13_U, FUN_IE);
            break;
        case 14://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO14_U, FUN_IE);
            break;
        case 15://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_XTAL_32K_P_U, FUN_IE);
            break;
        case 16:
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_XTAL_32K_N_U, FUN_IE);
            break;
        case 17:
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_DAC_1_U, FUN_IE);
            break;
        case 18:
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_DAC_2_U, FUN_IE);
            break;
        case 19:
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO19_U, FUN_IE);
            break;
        case 20:
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO20_U, FUN_IE);
            break;
        case 21:
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO21_U, FUN_IE);
            break;
        case 26://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_SPICS1_U, FUN_IE);
            break;
        case 27://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_SPIHD_U, FUN_IE);
            break;
        case 28://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_SPIWP_U, FUN_IE);
            break;
        case 29://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_SPICS0_U, FUN_IE);
            break;
        case 30://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_SPICLK_U, FUN_IE);
            break;
        case 31://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_SPIQ_U, FUN_IE);
            break;
        case 32://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_SPID_U, FUN_IE);
            break;
        case 33://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO33_U, FUN_IE);
            break;
        case 34://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO34_U, FUN_IE);
            break;
        case 35://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO35_U, FUN_IE);
            break;
        case 36://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO36_U, FUN_IE);
            break;
        case 37://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO37_U, FUN_IE);
            break;
        case 38://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO38_U, FUN_IE);
            break;
        case 39://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_MTCK_U, FUN_IE);
            break;
        case 40://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_MTDO_U, FUN_IE);
            break;
        case 41://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_MTDI_U, FUN_IE);
            break;
        case 42://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_MTMS_U, FUN_IE);
            break;
        case 43://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_U0TXD_U, FUN_IE);
            break;
        case 44://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_U0RXD_U, FUN_IE);
            break;
        case 45://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO45_U, FUN_IE);
            break;
        case 46://
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO46_U, FUN_IE);
            break;
        default:
            break;
    }
}


void gpio_pad_pullup(U8 gpio_num)
{
    switch(gpio_num){
        case 0://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO0_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO0_U, FUN_PD);
            break;
        case 1://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO1_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO1_U, FUN_PD);
            break;
        case 2://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO2_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO2_U, FUN_PD);
            break;
        case 3://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO3_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO3_U, FUN_PD);
            break;
        case 4://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO4_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO4_U, FUN_PD);
            break;
        case 5://bit8
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO5_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO5_U, FUN_PD);
            break;
        case 6:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO6_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO6_U, FUN_PD);
            break;
        case 7:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO7_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO7_U, FUN_PD);
            break;
        case 8:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO8_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO8_U, FUN_PD);
            break;
        case 9:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO9_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO9_U, FUN_PD);
            break;
        case 10:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO10_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO10_U, FUN_PD);
            break;
        case 11:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO11_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO11_U, FUN_PD);
            break;
        case 12://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO12_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO12_U, FUN_PD);
            break;
        case 13://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO13_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO13_U, FUN_PD);
            break;
        case 14://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO14_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO14_U, FUN_PD);
            break;
        case 15://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_XTAL_32K_P_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_XTAL_32K_P_U, FUN_PD);
            break;
        case 16:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_XTAL_32K_N_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_XTAL_32K_N_U, FUN_PD);
            break;
        case 17:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_DAC_1_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_DAC_1_U, FUN_PD);
            break;
        case 18:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_DAC_2_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_DAC_2_U, FUN_PD);
            break;
        case 19:
            break;
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO19_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO19_U, FUN_PD);
        case 20:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO20_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO20_U, FUN_PD);
            break;
        case 21:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO21_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO21_U, FUN_PD);
            break;
        case 26://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_SPICS1_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_SPICS1_U, FUN_PD);
            break;
        case 27://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_SPIHD_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_SPIHD_U, FUN_PD);
            break;
        case 28://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_SPIWP_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_SPIWP_U, FUN_PD);
            break;
        case 29://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_SPICS0_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_SPICS0_U, FUN_PD);
            break;
        case 30://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_SPICLK_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_SPICLK_U, FUN_PD);
            break;
        case 31://
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_SPIQ_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_SPIQ_U, FUN_PD);
            break;
        case 32:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_SPID_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_SPID_U, FUN_PD);
            break;
        case 33:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO33_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO33_U, FUN_PD);
            break;
        case 34:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO34_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO34_U, FUN_PD);
            break;
        case 35:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO35_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO35_U, FUN_PD);
            break;
        case 36:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO36_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO36_U, FUN_PD);
            break;
        case 37:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO37_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO37_U, FUN_PD);
            break;
        case 38:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO38_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO38_U, FUN_PD);
            break;
        case 39:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_MTCK_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_MTCK_U, FUN_PD);
            break;
        case 40:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_MTDO_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_MTDO_U, FUN_PD);
            break;
        case 41:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_MTDI_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_MTDI_U, FUN_PD);
            break;
        case 42:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_MTMS_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_MTMS_U, FUN_PD);
            break;
        case 43:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_U0TXD_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_U0TXD_U, FUN_PD);
            break;
        case 44:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_U0RXD_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_U0RXD_U, FUN_PD);
            break;
        case 45:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO45_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO45_U, FUN_PD);
            break;
        case 46:
            SET_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO46_U, FUN_PU);
            CLEAR_PERI_REG_MASK(PERIPHS_IO_MUX_GPIO46_U, FUN_PD);
            break;
        default:
            break;
    }

}

void gpio_pad_unhold(U8 gpio_num)
{
    switch(gpio_num){
        case 0://
            CLEAR_PERI_REG_MASK(RTC_PAD_HOLD, RTC_CNTL_TOUCH_PAD0_HOLD);
            break;
        case 1://
            CLEAR_PERI_REG_MASK(RTC_PAD_HOLD, RTC_CNTL_TOUCH_PAD1_HOLD);
            break;
        case 2://TOUCH2
            CLEAR_PERI_REG_MASK(RTC_PAD_HOLD, RTC_CNTL_TOUCH_PAD2_HOLD);
            break;
        case 3://
            CLEAR_PERI_REG_MASK(RTC_PAD_HOLD, RTC_CNTL_TOUCH_PAD3_HOLD);
            break;
        case 4://
            CLEAR_PERI_REG_MASK(RTC_PAD_HOLD, RTC_CNTL_TOUCH_PAD4_HOLD);
            break;
        case 5://bit8
            CLEAR_PERI_REG_MASK(RTC_PAD_HOLD, RTC_CNTL_TOUCH_PAD5_HOLD);
            break;
        case 6:
            CLEAR_PERI_REG_MASK(RTC_PAD_HOLD, RTC_CNTL_TOUCH_PAD6_HOLD);
            break;
        case 7:
            CLEAR_PERI_REG_MASK(RTC_PAD_HOLD, RTC_CNTL_TOUCH_PAD7_HOLD);
            break;
        case 8:
            CLEAR_PERI_REG_MASK(RTC_PAD_HOLD, RTC_CNTL_TOUCH_PAD8_HOLD);
            break;
        case 9:
            CLEAR_PERI_REG_MASK(RTC_PAD_HOLD, RTC_CNTL_TOUCH_PAD9_HOLD);
            break;
        case 10:
            CLEAR_PERI_REG_MASK(RTC_PAD_HOLD, RTC_CNTL_TOUCH_PAD10_HOLD);
            break;
        case 11://
            CLEAR_PERI_REG_MASK(RTC_PAD_HOLD, RTC_CNTL_TOUCH_PAD11_HOLD);
            break;
        case 12://
            CLEAR_PERI_REG_MASK(RTC_PAD_HOLD, RTC_CNTL_TOUCH_PAD12_HOLD);
            break;
        case 13://
            CLEAR_PERI_REG_MASK(RTC_PAD_HOLD, RTC_CNTL_TOUCH_PAD13_HOLD);
            break;
        case 14://
            CLEAR_PERI_REG_MASK(RTC_PAD_HOLD, RTC_CNTL_TOUCH_PAD14_HOLD);
            break;
        case 15://
            CLEAR_PERI_REG_MASK(RTC_PAD_HOLD, RTC_CNTL_X32P_HOLD);
            break;
        case 16:
            CLEAR_PERI_REG_MASK(RTC_PAD_HOLD, RTC_CNTL_X32N_HOLD);
            break;
        case 17:
            CLEAR_PERI_REG_MASK(RTC_PAD_HOLD, RTC_CNTL_PDAC1_HOLD);
            break;
        case 18:
            CLEAR_PERI_REG_MASK(RTC_PAD_HOLD, RTC_CNTL_PDAC2_HOLD);
            break;
        case 19:
            CLEAR_PERI_REG_MASK(RTC_PAD_HOLD, RTC_CNTL_RTC_PAD19_HOLD);
            break;
        case 20:
            CLEAR_PERI_REG_MASK(RTC_PAD_HOLD, RTC_CNTL_RTC_PAD20_HOLD);
            break;
        case 21:
            CLEAR_PERI_REG_MASK(RTC_PAD_HOLD, RTC_CNTL_RTC_PAD21_HOLD);
            break;
        default:
            CLEAR_PERI_REG_MASK(DIG_PAD_HOLD, BIT(gpio_num - 22));
            break;
    }
}
#endif // GPIO_H_INCLUDED

#if 0
/*
 * API Note: We could use this gpio layer to manage per-pin ISRs and
 * DSRs rather than just allow a single ISR and DSR for all pins.
 * For the way that GPIO is used on this platform, this adds overhead
 * and is of minimal value.
 */

void gpio_intr_test(U32 intr_mask, void *arg)
{
        U32 value;
        value = GPIO_INPUT_GET(GPIO_ID_PIN(3));
		
	 if(value == 1)	
	 {     GPIO_OUTPUT_SET(GPIO_ID_PIN(1) , 1);
	 }
	 else
	 {     GPIO_OUTPUT_SET(GPIO_ID_PIN(1) , 0);
	 }
	 gpio_intr_ack(intr_mask);
}
#endif

#if 0
void
gpio_module_install(struct gpio_api *tbl)
{
    tbl->_gpio_init                     = _gpio_init;
    tbl->_gpio_output_set               = _gpio_output_set;
    tbl->_gpio_input_get                = _gpio_input_get;
    tbl->_gpio_register_set             = _gpio_register_set;
    tbl->_gpio_register_get             = _gpio_register_get;
    tbl->_gpio_intr_handler_register    = _gpio_intr_handler_register;
    tbl->_gpio_intr_pending             = _gpio_intr_pending;
    tbl->_gpio_intr_ack                 = _gpio_intr_ack;
}
#endif //0
