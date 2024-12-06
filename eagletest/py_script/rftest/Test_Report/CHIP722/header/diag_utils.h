/* 
 * Customer ID=7011; Build=0x2b6f6; Copyright (c) 2009 by Tensilica Inc.  ALL RIGHTS RESERVED.
 * These coded instructions, statements, and computer programs are the
 * copyrighted works and confidential proprietary information of
 * Tensilica Inc.  They may be adapted and modified by bona fide
 * purchasers for internal use, but neither the original nor any
 * adapted or modified version may be disclosed or distributed to
 * third parties in any manner, medium, or form, in whole or in part,
 * without the prior written consent of Tensilica Inc.
 *
 * This software and its derivatives are to be executed solely on
 * products incorporating a Tensilica processor.
 */

#include <xtensa/hal.h>
#if !defined (DIAG_UTILS_H_INCLUDED)
#define DIAG_UTILS_H_INCLUDED
// If you change this define, you must also change the plusarg "+DVMagicExit" 
// sent to the simulator
#define MAGIC_DIAG_EXIT XSHAL_SIMIO_BYPASS_VADDR
#endif
#define PRINT_LINE printline(__FILE__,__FUNCTION__,__LINE__)
#define CHECK_LINE(value,ref) checkline(value,ref,__FUNCTION__, __FILE__,__LINE__)

int strlen (const char *str);

// Exit status
int set_diag_status(int stat);

// Place-holder routines
int diag_pass();
int diag_fail();

int pass(const char *msg);
int fail(const char *msg);

int Check (unsigned int address, unsigned int value, unsigned int mask);
int CheckU8 (unsigned char* AddressPtr, unsigned int value, unsigned int mask);

void printline(const char *file_name,const char *func_name,unsigned int line);
void checkline(unsigned int value,unsigned int ref,const char *file_name,const char *func_name,unsigned int line);

void err_print(const char * info_msg);
void printinfo(const char * info_msg,unsigned int value);
void ets_print(const char * info_msg,unsigned int value);

#define BIT(x) (0x1 << (x))

//#define CHIP_ANA_MODE_SIM

