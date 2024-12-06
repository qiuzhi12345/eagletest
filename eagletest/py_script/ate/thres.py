#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
import sys, os
import time
from baselib.loglib.log_lib import *
from scipy import stats
from pathlib import Path
# pvt0: (2) 1.0V
# pvt1: (3) 1.05V
# pvt2: (4) 1.1V
# pvt3: (7) 1.25V

# pwc_dig1: 1.1V
# pwc_dig2: 1.05V
# pwc_rtc : 1.1V

# channel  : 1500
# atten0 lo: 500
# atten0 hi: 800
# atten1 lo: 500
# atten1 hi: 1000
# atten2 lo: 500
# atten2 hi: 1400
# atten3 lo: 500
# atten3 hi: 2000

class thres(object):
    """
    ATE data Analyze
    """
    def __init__(self, df):
        super(thres, self).__init__()
        self._df = df
        self.__clear_df()
        self._use_extern = False
        self._extern_thres = pd.DataFrame()
        self._output_thres = pd.DataFrame(columns=['min', 'mean', 'max', 'fail_l', 'fail_h', 'fail_percent', 'thres_lo', 'thres_hi', 'thres_width', 'thres_width_hi', 'thres_width_lo', "accuracy"])
        self._select_co = []
        self._all_co = self._df.columns[0:]
        self.LOGPATH = "./log/"  
        self.Color_tab=['b','g','r','c','m','y','k']

    @staticmethod
    def data_catch2merge(path, sheet, column = []):
        '''
        load all xls-files in path and merge them

        :path:
            path of xls data
        :sheet:
            sheet name of target data
        :column: 
            array_type, consists of original names of data items to deal with, such as
            ["LightSleep_0_IDD_ANA","LightSleep_0_IDD_IO","LS_Wakeup_0_IDD_ANA","LS_Wakeup_0_IDD_IO","LightSleep_1_IDD_ANA","LightSleep_1_IDD_IO",/
            "LS_Wakeup_1_IDD_ANA","LS_Wakeup_1_IDD_IO","DeepSleep_IDD_ANA","DeepSleep_IDD_IO","DS_WakeUp_IDD_ANA","DS_WakeUp_IDD_IO"]
        '''
        df_temp = pd.DataFrame()
        df = pd.DataFrame(columns=column, data=[])
        pa=Path(path)
        for fil in list(pa.glob("**/*.xlsx")):
            logdebug("find [%d] %s"%(os.path.getsize("%s"%fil), fil))
            if column!=[]:
                try:
                    df_temp=pd.read_excel("%s"%fil, sheetname=sheet)
                except:
                    logerror("!!sheet %s doesn't exist!!"%sheet)
                    continue
                hunt_flg=0
                for sub_co in column:
                    for df_co in df_temp.columns:
                        if df_co.find(sub_co)!=-1:
                            df_temp=df_temp.rename(columns={df_co:sub_co})
                            #loginfo("found %s!"%sub_co)
                            hunt_flg=1
                            break
                    if not hunt_flg:
                        logerror("!!failed to find %s!!"%sub_co)
                        break
                if hunt_flg:
                    df = pd.concat([df, df_temp], join='inner')
                    df = df.dropna(axis=0, how='any')
        df.to_csv(path + 'data_merge_%s.csv'%time.asctime())
        return df

    @staticmethod
    def concat_pd(path, sheet):
        '''
        load all xls-files in path

        :path:
            path of xls data
        '''
        df = pd.DataFrame()
        for fil in os.listdir(path):
            if fil[-4:] == ".xls" or fil[-5:] == ".xlsx":
                logdebug("find [%d] %s"%(os.path.getsize(path + fil), fil))
                df = pd.concat([df, pd.read_excel(path + fil, sheetname=sheet)])
        return df

    def __clear_df(self):
        new_item = []
        for item in self._df.columns:
            if item.find(":") != -1:
                new_item.append(item.split(':')[1])
            else:
                new_item.append(item)

        self._df.columns = new_item
    def __calc(self, lo, hi, data):
        fail_h_cnt = len(data[data>hi])
        fail_l_cnt = len(data[data<lo])
        per = (fail_l_cnt+fail_h_cnt)*100/float(len(data))
        return fail_l_cnt, fail_h_cnt, per

    def get_extern_thres_value(self, file_name = "./baselib/ate/thres_value.csv"):
        '''
        Use extern thres

        :file_name:
            file of extern thres
        '''
        self._extern_thres = pd.read_csv(file_name, index_col=0)
        self._use_extern = True

    def report_csv(self, file_name = "thres_report.csv"):
        '''
        write thres report to csv file
        '''
        self._output_thres.to_csv(self.LOGPATH + file_name)

    def report_plot(self):
        plt.ion()
        plt.figure("%s"%(time.asctime()))
        for index,column in enumerate(self._select_co):
            data = self._df[column].dropna(axis=0, how='all')
            loginfo("%s %s"%(stats.mode(data)[0],stats.mode(data)[1]))
            data.plot(kind='kde')
            #data_length=re.search("[\d]",stats.mode(data)[1])
            plt.vlines(self._output_thres.loc[column]["thres_lo"], 0, 400, colors = self.Color_tab[index], linestyles = "dashed")
            plt.vlines(self._output_thres.loc[column]["thres_hi"], 0, 400, colors = self.Color_tab[index], linestyles = "dashed")
            plt.grid()
            plt.legend()

    def report_log(self):
        '''
        print thres report
        '''
        loginfo("%30s, %9s, %9s, %9s, %9s, %9s,  %9s, %9s, %9s, %9s, %9s, %9s, %9s"%('item', 'min', 'mean', 'max', 'fail_l', 'fail_h', 'fail_percent', 'thres_lo', 'thres_hi', 'thres_width', 'thres_width_hi', 'thres_width_lo', "accuracy"))
        for index in self._output_thres.index:
            stri = "%30s"%index
            for col in self._output_thres.columns:
                stri = stri + "%9s "%(str(self._output_thres.loc[index][col]))
            loginfo(stri)

    def do_thres(self, column = [],  full_match = False):
        '''
        do Analyze thres.

        :column: 
            if no column, it will calc the whole item
        :full_match:
            close approximate string matching
        '''
        self._output_thres.drop(self._output_thres.index, inplace=True)

        # get seleted co
        if column != []:
            if not full_match:
                for sub_co in column:
                    for df_co in self._all_co:
                        if df_co.find(sub_co) != -1:
                            if df_co not in self._select_co:
                                if self._use_extern and df_co not in self._extern_thres.index:
                                    logerror("df_co not in extern_thres")
                                    return -1
                                else:
                                    self._select_co.append(df_co)

            else:
                self._select_co = column
        else:
            if self._use_extern:
                self._select_co = self._extern_thres.index
            else:
                self._select_co = self._all_co


        print 222,self._select_co
        # start anly
        for index,column in enumerate(self._select_co):
            data = self._df[column]
            if self._use_extern:         
                if column in self._select_co:
                    thres = [self._extern_thres.loc[column]["thres_lo"], self._extern_thres.loc[column]["thres_hi"]]
                else:
                    continue
            else:           
                data.mean()
                thres = [data.mean()-data.std()*3.3, data.mean()+data.std()*3.3]
            fail_l_cnt, fail_h_cnt, per = self.__calc(thres[0] , thres[1], data)
            try:
                self._output_thres.loc[column] = [data.min(), data.mean(), data.max(), fail_l_cnt, fail_h_cnt, per, thres[0], thres[1], thres[1]-thres[0], thres[1]-data.mean(), data.mean()-thres[0], (thres[1]-thres[0])/2./3500.]
            except:
                logerror("error")
                logerror(str(data))
                return -1

        
