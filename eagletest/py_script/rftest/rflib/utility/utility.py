#!/usr/bin/env python
#test function for chip_v4.0

import csv, re, os, xlrd, xlwt, time, copy, glob
import numpy as np
#import mfunc
import thread, threading

def playMp3(dirMp3='.'):
    """ play Mp3 songs in a directory """

    e = threading.Event()
    def wait_for_input():
        raw_input('press any key and Enter to stop')
        e.set()

    fileList = glob.glob("%s/*.mp3"%dirMp3)
    if fileList:
        thread.start_new_thread(wait_for_input, tuple())
        for mp3file in fileList:
            T0 = time.clock()
            print "-"*10+" Playing '%s'"%mp3file
            mp3 = mp3play.load(mp3file)
            mp3.play()
            while (time.clock() - T0) < mp3.seconds():
                time.sleep(1)
                if e.isSet():
                    mp3.stop()
                    return
            mp3.stop()
        
    else:
        print "No mp3 files were found!"

##def sort_dict(d):
##    y = dict()
##    keys = np.sort(d.keys())
##    print keys
##    for key in keys:
##        print key
##        y[key] = d[key]
##    print "---------y=", y
##    return y
        
