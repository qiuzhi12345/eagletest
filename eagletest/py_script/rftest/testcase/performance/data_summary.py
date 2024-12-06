import time
import csv
import numpy as np
import pylab
import matplotlib.pyplot as plt
import serial
from rftest.rflib.utility import iofunc
from ordereddict import OrderedDict
import xlwt
import xlrd
import sys
import os
from rftest.rflib.csv_report import csvreport
import pandas as pd
import shutil
from rftest.rflib import rfglobal
##import xlsxwriter

#****************************************************#
#********** generate RF Test data table *************#
#****************************************************#

def gen_rf_file(rf_path, temperature=20):
    mac = wifi.read_mac()
    PATH = rf_path
    filetime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()));
    folder = 'RFTest_%s_%s_%s'%(mac,temperature,filetime[0:8])
    data_path = PATH+'%s'%(folder)+'/'
    if os.path.exists(data_path) == False:
        os.mkdir(data_path)
    init_file = data_path+'RFTest_INIT_%s_%s.log'%(mac,filetime)
    tx_file = data_path+'RFTest_TX_%s_%s.csv'%(mac,filetime)
    rx_sens_file = data_path+'RFTest_RXSens_%s_%s.csv'%(mac,filetime)
    rx_maxlevel_file = data_path+'RFTest_RXMaxLevel_%s_%s.csv'%(mac,filetime)
    rx_range_file = data_path+'RFTest_RXRange_%s_%s.csv'%(mac,filetime)
    rx_path = data_path+'RFTest_RX_%s_%s/'%(mac,filetime[0:8])
    if os.path.exists(rx_path) == False:
        os.mkdir(rx_path)

    return [init_file, tx_file, rx_sens_file, rx_maxlevel_file, rx_range_file, rx_path, data_path]

def get_test_title(instr, chan_m, ht40_m, rate_m):
    ostr = ''
    chan_o = ''
    rate_o = ''

    if instr == 'EVM':
        l_loop = 1
    else:
        l_loop = 1
    for l in range(l_loop):
        if instr == 'EVM':
            if l==0:
                instr_t = 'EVM'
            elif l==1:
                instr_t = 'EVM_STD'
            else:
                instr_t = 'EVM_MAX'
        for i in range(0, len(rate_m)):
            rate = rate_m[i]
            if instr == 'RX_Range':
                jr = 1
            else:
                jr = len(chan_m)
            for j in range(0, jr):

                if instr == 'RX_Range':
                    chan_i = i
                else:
                    chan_i = j
                chan = chan_m[chan_i]
                if instr == 'EVM':
                    ostr += instr_t+','
                else:
                    ostr += instr+','
                chan_o += 'CH%d_%d,'%(chan,ht40_m[chan_i])
                rate_o += '%s,'%rate

    return [ostr,chan_o,rate_o]

def gen_data_title(rf_setting_file):
    [cable_lose, unit_no, temperature, tx_channel, tx_ht40, tx_rate, rx_channel, rx_ht40, rx_rate, rxm_channel, rxm_ht40, rxm_rate, rxd_channel, rxd_ht40, rxd_rate, rxd_range] = get_rf_setting(rf_setting_file)

    [ostr_pwr,chan_pwr,rate_pwr] = get_test_title('POWER', tx_channel, tx_ht40, tx_rate)
    [ostr_evm,chan_evm,rate_evm] = get_test_title('EVM', tx_channel, tx_ht40, tx_rate)
    [ostr_freq,chan_freq,rate_freq] = get_test_title('FREQ_OFFSET', [tx_channel[0]], [tx_ht40[0]], [tx_rate[0]])
    [ostr_sens,chan_sens,rate_sens] = get_test_title('RX_Sens', rx_channel, rx_ht40, rx_rate)
    [ostr_range,chan_range,rate_range] = get_test_title('RX_Range', rxd_channel, rxd_ht40, rxd_rate)
    # tx data title
    title1 = ostr_pwr + ostr_evm + ostr_freq +'\n,'
    title2 = rate_pwr + rate_evm + rate_freq +'\n,'
    title3 = chan_pwr + chan_evm + chan_freq +'\n,'
    txd_title = 'MAC,'+title1+'MAC,'+title2+'MAC,'+title3

    # rx data title
    title1 = ostr_sens + ostr_range +'\n,'
    title2 = rate_sens + rate_range +'\n,'
    title3 = chan_sens + chan_range +'\n,'
    rxd_title = 'MAC,'+title1+'MAC,'+title2+'MAC,'+title3

    info = iofunc.csv2data(rf_setting_file, sheet='Test Info')
    test_info = ''
    for row in info:
        for tmp in row:
            test_info += '%s,'%tmp
        test_info += '\n,'

    return [txd_title, rxd_title, test_info]

def get_test_file(data_path):
    _dir=os.path.abspath(data_path)
    tlist=os.listdir(_dir)
    dir_path = []
    mac_list = []
    for flist in tlist:
        dpath = data_path+flist
        if os.path.isdir(dpath)==True:
            dir_path.append(dpath)
            flist_s = flist.split('_')
            mac_list.append(flist_s[1])
    print mac_list
    log_file = []
    tx_file = []
    rx_sens_file = []
    rx_range_file = []
    rx_dir = []

    for fpath in dir_path:
        _dir=os.path.abspath(fpath)
        tlist=os.listdir(_dir)
        for file_t in tlist:
            f1 = file_t.split('_')
            file_path = fpath+'/'+file_t
            if f1[1] == 'TX':
                tx_file.append(file_path)
            elif f1[1] == 'INIT':
                log_file.append(file_path)
            elif f1[1] == 'RXSens':
                rx_sens_file.append(file_path)
            elif f1[1] == 'RXRange':
                rx_range_file.append(file_path)
            elif f1[1] == 'RX':
                rx_dir.append(file_path)
    return [mac_list,log_file,tx_file,rx_sens_file,rx_range_file,rx_dir]

def get_data_color(data, thres_low, thres_high):
    if data<= thres_high and data >= thres_low:
        return 0   #color_index=1 is black
    else:
        print '%f,%f,%f'%(data, thres_low, thres_high)
        return 2   #color_index=2 is red

def get_tx_data(mac_list, tx_file, threshold_dict):
    color_list = ''
    out_str = ''
    for i in range(len(mac_list)):
        tfile = tx_file[i]
        mac = mac_list[i]
        data_str = ''
        tx_data = iofunc.csv2data(tfile)
        power = ''
        evm = ''
        freq_off = ''
        power_color = ''
        evm_color = ''
        freq_color = ''
        for j in range(1, len(tx_data)):
            row = tx_data[j]
            rate = row[2]
            power += row[3]+','
            evm += row[4]+','
            if j==1:
                freq_off += row[7]+','
                freq_color += '0,'
            power_color += '%d,'%get_data_color(float(row[3]), float(threshold_dict[rate][0])-1.5, float(threshold_dict[rate][0])+1.5)
            evm_color += '%d,'%get_data_color(float(row[4]), -40, float(threshold_dict[rate][1]))
        out_str += mac+','+power+evm+freq_off+'\n,'
        color_list += '0,'+power_color+evm_color+freq_color+'\n,'
    return [out_str, color_list]

def get_tx_gain(mac_list, log_file):
    out_str = 'mac, pa_gain, ana_gain, backoff, , , , bb_gain,\n,'
    for i in range(len(mac_list)):
        tfile = log_file[i]
        mac = mac_list[i]
        data_str = ''
        f=open(tfile,'r')
        text=f.readlines()
        for line in text:
            line=line.replace(';',',').replace('=',',').replace('\n','').replace('\r','').replace(' ','').replace(':',',')
            line = line.split(',')
            if line[0] == 'cal_rf_ana_gain':
                data_str += line[2]+','+line[4]+','
            elif line[0] == 'TX_POWER_BACKOFF':
                for i in range(1, len(line)):
                    if line[i] != '':
                        data_str += line[i]+','
            elif line[0] == 'TX_PWRCTRL_ATTEN':
                for i in range(1, len(line)):
                    if line[i] != '':
                        data_str += line[i]+','
        out_str += mac+','+data_str+'\n,'
    return out_str

def get_rx_data(mac_list, rx_sens_file, rx_range_file, threshold_dict):
    out_str = ''
    color_list = ''
    for i in range(len(mac_list)):
        sens_file = rx_sens_file[i]
        range_file = rx_range_file[i]
        mac = mac_list[i]

        sens_data = iofunc.csv2data(sens_file)
        rxsens = ''
        sens_color = ''
        for j in range(1, len(sens_data)):
            row = sens_data[j]
            rate = row[2]
            rxsens += row[3]+','
            sens_color += '%d,'%get_data_color(float(row[3]), -102, float(threshold_dict[rate][2]))

        range_data = iofunc.csv2data(range_file)
        rxrange = ''
        range_color = ''
        for j in range(1, len(range_data)):
            row = range_data[j]
            rate = row[2]
            rxrange += row[5]+','
            range_color += '%d,'%get_data_color(float(row[5]), float(threshold_dict[rate][3]), 100)
        out_str += mac+','+rxsens+rxrange+'\n,'
        color_list += '0,'+sens_color+range_color+'\n,'
    return [out_str, color_list]

def set_color(color):
    style = xlwt.XFStyle()
    style.font.colour_index = color
    style.alignment.horz = 0x02   #HORZ_CENTER
    return style

def data_xlswrite(data, data_color, sheetw, col_in):
     data = data.split(',')
     if data_color != '':
        data_color = data_color.split(',')
     row = 0
     col = col_in
     for i in range(0, len(data)):
        if data[i] == '\n':
            row = 0
            col += 1
        elif data[i] != '':
            if data_color == '':
                color = 0
            else:
                if data_color[i] == '':
                    color =  0
                else:
                    color = int(data_color[i])
            sheetw.write(col, row, data[i], set_color(color))
            row += 1
     return col

def gen_data_table(rf_setting_file = '../Auto_RFTest/RFTest_Setting.xlsx', data_path = '../Auto_RFTest/RFTest_data/RFTest_data_20180525/'):
    filetime = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()));
    data_xls_file = data_path+'RFTest_Report_%s.xls'%(filetime)

    [txd_title, rxd_title, test_info] = gen_data_title(rf_setting_file)

    threshold_dict = iofunc.csv2dict(rf_setting_file, sheet='Threshold')

    [mac_list,log_file,tx_file,rx_sens_file,rx_range_file,rx_dir] = get_test_file(data_path)

    [tx_data, tx_color] = get_tx_data(mac_list, tx_file, threshold_dict)

    tx_gain_data = get_tx_gain(mac_list, log_file)

    [rx_data, rx_color] = get_rx_data(mac_list, rx_sens_file, rx_range_file, threshold_dict)

    wb = xlwt.Workbook()

    info_sheet = wb.add_sheet('Test Info')
    col_out = data_xlswrite(test_info, '', info_sheet, 0)

    tx_sheet = wb.add_sheet('TX_DATA')
    col_out = data_xlswrite(txd_title, '', tx_sheet, 0)
    col_out = data_xlswrite(tx_data, tx_color, tx_sheet, col_out)

    rx_sheet = wb.add_sheet('RX_DATA')
    col_out = data_xlswrite(rxd_title, '', rx_sheet, 0)
    col_out = data_xlswrite(rx_data, rx_color, rx_sheet, col_out)

    txg_sheet = wb.add_sheet('TX_GAIN')
    col_out = data_xlswrite(tx_gain_data, '', txg_sheet, 0)

    wb.save(data_xls_file)


def get_folder_file(source=''):
    _dir=os.path.abspath(source)
    tlist=os.listdir(_dir)
    all_file = []
    for i in range (len(tlist)):
        tname = tlist[i]
        fpath = source+'/'+tname
        all_file.append(fpath)
    all_file = sorted(all_file, key=lambda x: os.path.getmtime(os.path.join(_dir,x))) # sorted by time
    return all_file

def get_all_file(source=''):
    all_file = []
    sub_folder = get_folder_file(source)
    print sub_folder
    print '1'
    for folder in sub_folder:
        file_list = get_folder_file(folder)
        print file_list
        print '2'
        for f_list in file_list:
            if os.path.isdir(f_list):
                sub_list = get_folder_file(f_list)
                print sub_list
                print '3'
                for f1_list in sub_list:
                    if os.path.isdir(f1_list):
                        sub1_list = get_folder_file(f1_list)
                        print sub1_list
                        for f2_list in sub1_list:
                            if f2_list[-3:] == "log" or f2_list[-3:] == "csv":
                                all_file.append(f2_list)
                    else:
                        if f1_list[-3:] == "log" or f1_list[-3:] == "csv":
                            all_file.append(f1_list)
            else:
                if f_list[-3:] == "log" or f_list[-3:] == "csv":
                    all_file.append(f_list)
    print all_file
    return all_file

def delete_file(source=''):
    _dir=os.path.abspath(source)
    tlist=os.listdir(_dir)
    all_file = []
    for i in range (len(tlist)):
        tname = tlist[i]
        f_file = source+'/'+tname
        if f_file[-3:] == "csv":
            os.remove(f_file)

def get_init_print_data(result):
    init_dict = rfglobal.init_print_dict
    result1 = result.replace(';',',').replace('=',',').replace('\n',',').replace('\r','').replace(' ','').replace(':',',')
    result2 = result1.split(',')

    data_result = []
    title = ''
    index = 0
    flag = 0
    abandon = 0
    for item in result2:

        if item=='RX_NOISEFLOOR' and flag==1:
            abandon = 1
        else:
            abandon = 0

        if (item in init_dict) and abandon==0:
            data_m = init_dict[item]
##                    loginfo(item,flag,abandon)
##                    loginfo(result2[index:index+6])
            for k in range(len(data_m)):
                shift = data_m[k]
                data_result.append(result2[index+shift+1])
                title += '%s_%d,'%(item, k)
        index += 1

        if item=='RX_NOISEFLOOR':
            flag = 1
##                    loginfo(item,flag,abandon)
    title += '\n'
    return[data_result, title]

def init_print_data():
    source = 'D:/chip/eagletest/py_script/rftest/rfdata/init_print_20191017/'
    file_path = source+'result_csv/'
    if os.path.exists(file_path) == False:
        os.mkdir(file_path)
    else:
        delete_file(file_path)

    all_file = get_all_file(source)
    print all_file
    gen_file = file_path+'init_print_data'

    flie_i = 0
    for file_r in all_file:
        fr=open(file_r,'r')
        text=fr.readlines()
        result = ''
        for line in text:
            result += line
        [data_result, title] = get_init_print_data(result)

        if file_i == 0:
            csvreport1 = csvreport(gen_file, title)
        csvreport1.write_data(data_result)
        flie_i += 1
        fr.close()

def csv_col_data(csv_data, coln):
    col_data = []
    for row in csv_data:
        col_data.append(row[coln])
    return col_data


def test_data_summary():

##    data_type = 'RXGain_force'
##    data_type = 'fix_gain_rate_sweep'
##    data_type = 'RXGain_table'
##    data_type = 'fix_signal_Interference_sweep'
    data_type = 'rxiq_rx_range'

    if data_type == 'RXSens':
        source = 'D:/chip/eagletest/py_script/rftest/rfdata/RXSens_summary/'
        data_path = source+'sens_data/'
        gen_file = 'sens_data_summary_chan14'
        col_title=[1]
        copy_col=[3]
        title_index=[1]
    elif data_type == 'RXGain_force':
        source = 'D:/chip/eagletest/py_script/rftest/rfdata/sweep_rxgain_force_20191017/'
        data_path = source
        gen_file = 'rxgain_data_summary'
        col_title=[0,1]
        copy_col=[4,5,8,9]
        title_index=[5,6]
    elif data_type == 'RXGain_table':
        source = 'D:/chip/eagletest/py_script/rftest/rfdata/sweep_rx_table_20191017/'
        data_path = source
        gen_file = 'rxgain_table_summary'
        col_title=[0,1,2,3]
        copy_col=[6,7,8,9,10]
        title_index=[4,5]
    elif data_type == 'fix_gain_rate_sweep':
        source = 'D:/mystuff/B2/TX/'
        data_path = source
        gen_file = 'tx_data_power'
        col_title=[0,1,2,3,4]
        copy_col=[5]
        title_index=[5,6]

    elif data_type == 'fix_signal_Interference_sweep':
        source = 'D:/chip/eagletest/py_script/rftest/rfdata/Interference_test/ESP32_0x30aea467691c_20191216/bt_2437/'
        data_path = source
        gen_file = 'Interference_summary'
        col_title=[0,1,2]
        copy_col=[3,4,5,6]
        title_index=[8]

    elif data_type == 'rxiq_rx_range':
        source = 'D:/chip/eagletest/py_script/rftest/rfdata/rxiq_rxrange/rxiq_amp_3/'
        data_path = source
        gen_file = 'rxiq_rx_range_summary'
        col_title=[0,1]
        copy_col=[2]
        title_index=[6]

    file_path = source+'result_csv/'
    if os.path.exists(file_path) == False:
        os.mkdir(file_path)
    else:
        delete_file(file_path)

    all_file =  get_all_file(data_path)

    csvreport1 = csvreport(file_path+gen_file, '')

    data_result = []
    C = open(all_file[0],'r')
    csv_data = list(csv.reader(C))
    for i in col_title:
        data_result.append(csv_col_data(csv_data, i))

    chipn = 0
    for file_r in all_file:
##        print file_r
        file_name = file_r.split('/')
        title_name = file_name[-1][0:-4].split('_')
        title_append = ''
        for tn in title_index:
            title_append += title_name[tn]+'_'

        title_append +='%s_'%chipn

        C = open(file_r,'r')
        csv_data = list(csv.reader(C))
        for i in copy_col:
            col_data = csv_col_data(csv_data, i)
            col_data[0] = title_append + col_data[0]
            data_result.append(col_data)

        chipn += 1


    for i in range(0,len(data_result[0])):
        col_data = []
        for data in data_result:
            col_data.append(data[i])
        csvreport1.write_data(col_data)


filePath = 'D:/chip/eagletest/py_script/rftest/rfdata/rxiq_rxrange/rxiq_rxrange_summary'
newPath = 'D:/chip/eagletest/py_script/rftest/rfdata/rxiq_rxrange/rxiq_amp_3/rxiq_rxrange_summary/'

def createDir(newPath=newPath):
    isExists=os.path.exists(newPath)
    if not isExists:
        os.makedirs(newPath)
        print newPath, "make dir ok"
    else:
        print newPath, "dir exists"

def copyFile(filePath=filePath,newPath=newPath):
    fileNames =os.listdir(filePath)
    print fileNames
    for file in fileNames:
        newDir = filePath + '/'+file
        if os.path.isfile(newDir):
            print newDir
            shutil.copy(newDir,newPath)
        else:
            copyFile(newDir,newPath)


def draw_line_Chart():

    csv_file= 'D:/mystuff/B2/TX/tx_data_power_20190827_203016'
    csv = pd.read_csv(csv_file +'.csv')
    csv.to_excel(csv_file+'.xlsx',sheet_name='data')

    data = xlrd.open_workbook(r'D:/mystuff/B2/TX/tx_data_power_20190827_203016.xlsx')
    table=data.sheets()[0]
    nrows=table.nrows
    ncols=table.ncols
    print[nrows,ncols]

# ---CSV to chart-----#f
##    csv_file =(open('D:/mystuff/B2/TX/tx_data_power_20190827_203016.csv'))
##    lines = csv_file.readlines()
##    csv_file.close()
    raw_data=[]

##    for line in lines:
##        raw_data.append(line.split(','))
##    ncols=len(raw_data[0])
##    nrows=len(raw_data)
##    print[nrows,ncols]

    for i in range(4,ncols):
        raw_data.append(table.col_values(i))
##
    workbook = xlsxwriter.Workbook('D:/mystuff/B2/TX/tx_data_power_chart.xlsx')
    worksheet = workbook.add_worksheet()
##
    for i, line in enumerate(raw_data):
        for j ,col in enumerate(line):
           worksheet.write(j,i,col)

    chart = workbook.add_chart({'type':'line'})
    chart.set_title({'name':'Power'})
    chart.set_x_axis({'name':['Sheet1',0,0]})
    chart.set_y_axis({'name':'Power(dBm)',
                        'min':12,
                        'max':22,})

    for j in range (2,ncols-4):
##
        chart.add_series({
        'name':['Sheet1',0,j],
        'categories':['Sheet1',1,0,nrows,0], ## x_axis range
        'values':['Sheet1',1,j,nrows-1,j],## data range
        })

    worksheet.insert_chart(nrows+1,0,chart)
    workbook.close()






















