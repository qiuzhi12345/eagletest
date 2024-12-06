# -- coding: utf-8 --
import matplotlib.pyplot as plt, csv
import pandas as pd
import numpy as np

class draw_image(object):
    def __init__(self):
        pass
   
    def draw_xy_image(self, csv_file, xlabel=""):
        '''
        用于画类似adc pad在不同输入电压下输出不同data图，x轴为输入电压值，y轴为输出adc数值。
        input_dc    0.05  0.1    0.15   0.2   0.25    0.3    0.35    0.4    0.45    0.5     0.55    0.6     0.65
        2M            0    92    252    410    576    733    894    1059    1216    1376    1537    1700    1862
        80M           0    92    253    412    575    733    896    1060    1219    1377    1539    1700    1865
        wifiinit      0    117   277    437    602    763    924    1088    1247    1406    1570    1729    1894
        lightsleep    0    64    221    380    544    703    860    1028    1184    1346    1505    1669    1826
        deepsleep     0    59    220    384    545    702    864    1028    1187    1342    1503    1670    1827
        '''
        file_object = open(csv_file, 'rb')
        reader = csv.reader(file_object)
        head = reader.next()
        head_list = []
        for col_no, raw_head in enumerate(head):
            if not col_no:
                continue
            head_list.append(raw_head)
        for raw in reader:
            plt.plot(head_list, raw[1:], label = raw[0])
            plt.xlabel(xlabel)
            plt.legend(loc = 'upper left')
        plt.show()
    
    def draw_gaussian_image(self, csv_file, index_col, bins = 'auto', raw = 2):
        '''
        画高斯分布图，如温度分布，电流分布，固定输入电压的adc分布等。
        - csv_file: csv路径及名称；
        - index_col: 下面例子中的"index"；
        - bins: 100或1000等，根据需要调整；
        - raw: 画几张图，如下实例需要画３张图（regpd0_dbg0，　regpd1_dbg0，　regpd1_dbg7）。
        eg:
        index            1       2       3       4       5       6       7       8       9
        regpd0_dbg0    1672    1688    1653    1664    1673    1677    1656    1684    1661
        regpd1_dbg0    1679    1660    1649    1666    1674    1668    1674    1665    1690
        regpd1_dbg7    2282    2305    2281    2290    2272    2279    2272    2285    2291
        '''
        dt = pd.read_csv(csv_file, index_col= index_col)
        for i in range(raw):
            arr = np.array(dt[0+int(i) : 1+int(i)])
            mean = arr.sum() / float(arr.size)
            arr2 = (arr-mean)*(arr-mean)
            var = (arr2.sum() /arr.size)
            print mean , var
            dt[0+int(i) : 1+int(i)].T.hist(bins=bins, normed = False,label = 'mean:%.f var:%.4f' %(mean,var))
            plt.grid(True)
            plt.legend(loc='upper left')
            plt.show()

    def draw_gaussian_image_2(self, csv_file):
        '''
        画高斯分布图，比如常温下温度的分布等
        '''
        file_object = open(csv_file, 'rb')
        df = pd.read_csv(file_object)
        plt.ion()
        df.plot(kind = 'kde')