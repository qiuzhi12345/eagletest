from enum import Enum

class RATE_TAB(Enum):
    LG_1ML            = 0x0
    LG_2ML            = 0x1
    LG_5_5ML          = 0x2
    LG_11ML           = 0x3
    LG_2MS            = 0x5
    LG_5_5MS          = 0x6
    LG_11MS           = 0x7
    LG_6M             = 0xb
    LG_9M             = 0xf
    LG_12M            = 0xa
    LG_18M            = 0xe
    LG_24M            = 0x9
    LG_36M            = 0xd
    LG_48M            = 0x8
    LG_54M            = 0xc
    # LR_1_8BPSKVM      = 0x10
    # LR_1_4BPSKVM      = 0x11
    # LR_1_2BPSKVM      = 0x12
    # LR_1_4QPSKVM      = 0x15
    # LR_1_2QPSKVM      = 0x16
    # LR_1QPSKVM        = 0x17
    # LR_1_4BPSKM       = 0x19
    # LR_1_2BPSKM       = 0x1a
    HT_MCS0           = 0x20
    HT_MCS1           = 0x21
    HT_MCS2           = 0x22
    HT_MCS3           = 0x23
    HT_MCS4           = 0x24
    HT_MCS5           = 0x25
    HT_MCS6           = 0x26
    HT_MCS7           = 0x27 

RATE_DATA = {
    'LG_1ML'            : 1000000,
    'LG_2ML'            : 2000000,
    'LG_5_5ML'          : 5500000,
    'LG_11ML'           : 11000000,
    'LG_2MS'            : 2000000,
    'LG_5_5MS'          : 5500000,
    'LG_11MS'           : 11000000,
    'LG_6M'             : 6000000,
    'LG_9M'             : 9000000,
    'LG_12M'            : 12000000,
    'LG_18M'            : 18000000,
    'LG_24M'            : 24000000,
    'LG_36M'            : 36000000,
    'LG_48M'            : 48000000,
    'LG_54M'            : 54000000,
    'HT_MCS0'           : 7200000,
    'HT_MCS1'           : 14400000,
    'HT_MCS2'           : 21700000,
    'HT_MCS3'           : 28900000,
    'HT_MCS4'           : 43300000,
    'HT_MCS5'           : 37800000,
    'HT_MCS6'           : 65000000,
    'HT_MCS7'           : 72200000 
}
