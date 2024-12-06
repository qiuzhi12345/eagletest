import re;
import time
import platform
import os, sys


from baselib.loglib.log_lib import *

####import baselib####
from baselib.test_channel.com import *
# from baselib.test_channel.sock import *
# from baselib.test_channel.server import *
from baselib.instrument.cmw_bt import *
from baselib.instrument.spa import *
from baselib.instrument.mxg import *
loginfo("load baselib module success")


from testcase.Init import *
from rftest.testcase.Init import *
loginfo("load rftest module success")


print("\n       ***********************************\n"
        "                   welcome                \n"
        "       ***********************************\n")


#### %load_ext autoreload   %autoreload 2