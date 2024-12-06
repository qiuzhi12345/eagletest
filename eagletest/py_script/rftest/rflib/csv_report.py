# -- coding: utf-8 --
import os
import time
import unicodecsv as ucsv

class csvreport(object):
    '''
    用于生成 CSV 格式 的 表格
    '''

    def __init__(self, csvname, title, no_time=0):
        '''
        :csvname:
              input csv name is path+name
        :title:
                it may be string ['str1, str2, str3, ...\n']
        :output CSV name is csvname+localtime.csv
        '''
        logtime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))
        if no_time==1:
            logtime = logtime[0:8]

        self.filename = '%s_%s.csv'%(csvname, logtime)
##        self.filename = './rftest/rfdata/test_phase_case/test_phase_case_CHIP722_A_20190507.csv'

        if os.path.isfile(self.filename) == False:
            self.wf = open(self.filename, 'w')
            self.wf.write(title)
        else:
            self.wf = open(self.filename, 'a')
        self.wf.close()

    def get_type(self, data, float_num=2):
        if type(data) == int:
            ostr = str(data)+','
        elif type(data) == str:
            ostr = data+','
        else:
            if float_num==2:
                ostr = '%2.2f,'%data
            else:
                ostr = '%2.6f,'%data
        return ostr

    def write_data(self, data_list, float_num=2):
        '''
        csv write data line
        :data_list:
            it may be string and int type, like ['str', 'str', int, int, ...]
        '''
        self.wf = open(self.filename, 'ab+')
        w = ucsv.writer(self.wf, encoding='gbk')
        wstr = ''
        for data in data_list:
##            print data
##            print type(data)
            if type(data) == list:
                for dl in data:
                    wstr += self.get_type(dl,float_num)
            else:
                wstr += self.get_type(data, float_num)

        wstr += '\n'
        w.writerow(data_list)
        # self.wf.write(wstr)
        self.wf.close()

    def write_string(self, string):
        '''
        csv write data line
        :string:
        '''
        self.wf = open(self.filename, 'a')
        self.wf.write(string)
        self.wf.close()

    def close(self):
        '''
        释放 csv 文件
        '''
        self.wf.close()

