
import os, sys
import pandas as pd
import numpy as np
import re

def py_relace(bfname="tester.tester('iqv',",afname="tester.tester(",fname_path='./'):
    fnamelist=gci(fname_path)
    print fnamelist
    for fname in fnamelist:
        print fname
        with open(fname,'rt') as f:
####            all_fid2_str = ""
            line_new=""

            for line in f:
                print line
                line=line.replace(bfname,afname)
                line_new=line_new+line

        with open(fname,"w") as f:
            f.write(line_new)
##            f.write(_str)

##            f.close()
##            line=line.replace(bfname[k],afname[k])
##            all_fid2_str = all_fid2_str +line
##    pyfid = open(os.path.split(fname)[0] + "/"+os.path.split(fname)[1].encode("utf-8"), 'w')
##    loginfo(pyfid)
##    pyfid.write(all_fid2_str)
##    pyfid.close()


def gci(filepath):
    filelist=[]
    files=os.listdir(filepath)
    print files
    for fi in files:
        fi_d=os.path.join(filepath,fi)
        if os.path.isdir(fi_d):
            gci(fi_d)

        else:
            fi_name=os.path.join(filepath,fi_d)
            if os.path.splitext(fi_name)[1]==".py":
                filelist.append(fi_name)
    return filelist

replace_dir={
"self.wificommon." : "self.wifi.",
"self.wifitx." : "self.wifi.",
"self.wifirx." : "self.wifi.",
"COMMON,WIFITX,WIFIRX" : "WIFILIB",
"self.wificommon = COMMON" : "self.wifi = WIFILIB",
"self.wificm_api." : "self.wifiapi.",
"self.wifitx_api." : "self.wifiapi.",
"self.wifirx_api." : "self.wifiapi.",
"WIFICM_API,WIFITX_API,WIFIRX_API" : "WIFIAPI",
"self.bttx." : "self.bt.",
"self.btrx." : "self.bt."
}

if __name__=="__main__":
    _path="d:/chip/eagletest/py_script/rftest/testcase/rf_debug"
##    py_relace(bfname="tester.tester('iqv',",afname="tester.tester(",fname_path=_path)
##    py_relace(bfname="baselib.instrument.iqv",afname="baselib.instrument.tester_serv",fname_path=_path)
    for bfname in replace_dir:
        afname=replace_dir[bfname]
        py_relace(bfname,afname,fname_path=_path)
##    py_relace(bfname="from rftest.rflib.common import WiFi",afname="from rftest.rflib.wifi_common import COMMON,WiFiTX,WiFiRX",fname_path=_path)
##    py_relace(bfname="self.adcdump = ADC_DUMP(self.channel,self.chipv)",afname="self.adcdump = DUMP(self.channel,self.chipv)",fname_path=_path)
##    py_relace(bfname="self.wifi.rfchsel",afname="self.wificommon.rfchsel",fname_path=_path)
##    py_relace(bfname="self.wifi = WiFi(self.channel,self.chipv)",afname="self.wificommon = COMMON(self.channel,self.chipv)\n"+"        self.wifitx = WiFiTX(self.channel,self.chipv)\n"+"        self.wifirx = WiFiRX(self.channel,self.chipv)",fname_path=_path)

