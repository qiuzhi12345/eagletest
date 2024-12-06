# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import csv
import glob

def getlmt(data_array):
    if min(data_array)>=0:
       hlmt=max(data_array)*1.3;
       llmt=min(data_array)*0.9;
    elif max(data_array)>=0:
       hlmt=max(data_array)*1.3;
       llmt=min(data_array)*1.3;
    else:
       hlmt=max(data_array)*0.9;
       llmt=min(data_array)*1.1;
    return [llmt,hlmt];

def plot_curve(xdata,ydata,label='Y',xlabel='sample',ylabel='amplitude',title='example',subplot_en=0,subplot_row=3,subplot_col=3,index=0,plot_save=0,logdir='subplot',filename=''):
    data_num=len(ydata);
    #x = np.linspace(0,data_num,data_num);
    x = np.array(xdata);
    y = np.array(ydata);
    plt.ion()
    if subplot_en==1:
       sub_index = index%(subplot_row*subplot_col);
       subplot_new = (sub_index==1);
       subplot_id = subplot_row*100 + subplot_col*10 + sub_index;

       if plot_save==1:
          index_start = (index-1)/(subplot_row*subplot_col)*(subplot_row*subplot_col)+1;
          save_name = './log/'+logdir+'/band_scan_'+str(index_start)+'_'+str(index);

       if subplot_new==1:
          plt.figure(figsize=(8,8));

       plt.subplot(subplot_id);
       title = title+str(index)
    else:
       plt.figure(figsize=(8,8));

    plt.plot(x,y,label="$%s$"%label,color="blue",linewidth=2);
    #plt.plot(x,z,"b--",label="$cos(x^2)$")
    plt.xlabel("%s"%xlabel);
    plt.ylabel("%s"%ylabel);
    plt.title("%s"%title);

    lmt=getlmt(y);
    plt.ylim(lmt[0],lmt[1]);
    plt.legend();
    plt.grid()
    if plot_save==1:
        figname =filename[0:-4]+'_fft.png'
        plt.savefig(figname)
    # plt.show()

def plot_scatter(xdata,ydata,label='I/Q map',xlabel='I',ylabel='Q',title='Constellation'):
    data_num=len(ydata);
    x = np.array(xdata);
    y = np.array(ydata);

    plt.figure(figsize=(8,8));
    #plt.plot(x,y,label="$Constellation$",color="red",linewidth=2);
    plt.plot(x,y,"b*",label="$%s$"%label);
    plt.xlabel("%s"%xlabel);
    plt.ylabel("%s"%ylabel);
    plt.title("%s"%title);

    ylmt=getlmt(y);
    xlmt=getlmt(x);
    plt.ylim(ylmt[0],ylmt[1]);
    plt.xlim(xlmt[0],xlmt[1]);
    plt.legend();
    plt.show();

#result is list include all lines offset from header by lnoffset parameters
#lnofffset is count from 0,colummn_offset is too
def filefind(path,pattern):
    filelst=[];
    try:
        for doc in glob.glob('%s/%s'%(path,pattern)):
            filelst.append(doc);
    except:
        print 'fail to find file';
    return filelst;

def get_csv_line(filename,lnoffset):
    result=[];
    try:
       f=file(filename);
    except:
       print 'fail to find file';
       return result;
    reader=csv.reader(f);
    i=0;
    for line in reader:
        if i==lnoffset:
           result=line;
        i=i+1;

    f.close();
    return result;

def get_csv_vect(filename,lnoffset,column_offset,mode='data'):
    '''get one column from csv file,mode=data or str'''
    result=[];
    try:
       f=file(filename);
    except:
       print 'fail to find file';
       return result;

    reader=csv.reader(f);
    i=0;
    for line in reader:
        if i>=lnoffset:
           try:
              if column_offset+1>len(line):
                 print 'column offset out of range';
                 f.close();
                 return result;
              data=line[column_offset];
              if mode=='data':
                 result.append(float(data));
              else:
                 result.append(data);
           except:
              print 'data in line %d is not digital!'%i;
              f.close();
              return result;
        i=i+1;
    f.close();
    return result;

#fft calculate
def fft_calc(real_data,image_data):
    # cv_data=[real_data[i]+image_data[i]*1j for i in range(0,len(real_data))];
    cv_data = [(real_data[i]-512) + (image_data[i]-512) * 1j for i in range(0, len(real_data))];
    ll=len(cv_data);
    c_data= np.array(cv_data);

    # print np.blackman(ll)
    # print c_data*np.blackman(ll)
    abs_filterdata=abs(np.fft.fft(c_data*np.blackman(ll)))**2;
    # abs_filterdata = abs(np.fft.fft(c_data )) ** 2;

    pwr_fig=((abs(np.fft.fft(c_data))**2).sum())/(abs_filterdata.sum());

    f_data= pwr_fig*abs_filterdata/(ll**2); #0.3043

    # f_data = abs(np.fft.fft(c_data))
    return f_data;

#fftdata is one array
def fft_plot(fftdata,sample_freq_mhz,center_freq_mhz,offset_db=0,subplot_en=0,subplot_row=3,subplot_col=3,index=0,plot_save=0,logdir='subplot',filename=''):
    ll=len(fftdata);
    x=center_freq_mhz+np.array(range(0,ll))*sample_freq_mhz*1.0/ll;
    xdata=[xi for xi in x];
    xdata_p=xdata[0:ll/2];
    xdata_n=[xi-sample_freq_mhz for xi in xdata[ll/2:]];

    y=10*np.log10(fftdata);
    ydata=[yi-offset_db for yi in y];
    ydata_p=ydata[0:ll/2];
    ydata_n=ydata[ll/2:];
    plot_curve(xdata_n+xdata_p,ydata_n+ydata_p,'FFT','Freq(MHz)','Amplitude(dB)','Spectrum',subplot_en,subplot_row,subplot_col,index,plot_save,logdir,filename);

#IQ time domain figure
def iqwave(filename,fig_type='iq', plot_save=0):
    real_data=get_csv_vect(filename,3,1);
    image_data=get_csv_vect(filename,3,2);
    data_num=len(real_data);
    if data_num==0:
       print 'fail to get IQ data';
       return;
    x = np.linspace(0,data_num,data_num);
    iwave = np.array(real_data);
    qwave = np.array(image_data);

    plt.figure(figsize=(16,8));
    plt.subplot(211);
    if fig_type=='iq':
       plt.plot(x,iwave,label="$I$",color="blue",linewidth=2);
       plt.xlabel("Samples");
       plt.ylabel("Amplitude");
       plt.title("I Wave");
    else:
       plt.plot(x,iwave,label="$Rssi$",color="blue",linewidth=2);
       plt.xlabel("Samples");
       plt.ylabel("Rssi");
       plt.title("IQ Amplitude");

    lmt=getlmt(iwave);
    plt.ylim(lmt[0],lmt[1]);
    plt.legend();

    plt.subplot(212);
    if fig_type=='iq':
       plt.plot(x,qwave,label="$Q$",color="blue",linewidth=2);
       plt.xlabel("Samples");
       plt.ylabel("Amplitude");
       plt.title("Q Wave");
    else:
       plt.plot(x,qwave,label="$Phase$",color="blue",linewidth=2);
       plt.xlabel("Samples");
       plt.ylabel("Phase");
       plt.title("IQ Phase");

    lmt=getlmt(qwave);
    plt.ylim(lmt[0],lmt[1]);
    plt.legend();
    if plot_save==1:
        figname =filename[0:-4]+'_iq.png'
        plt.savefig(figname)
    plt.show();


def get_txtone_amp(ifile='', qfile=''):
    real_data=get_csv_vect(ifile,1,1);
    image_data=get_csv_vect(qfile,1,1);

    iwave = np.array(real_data);
    qwave = np.array(image_data);

    length = len(iwave)

    power = []
    for i in range(0, length):
        power.append(iwave[i]**2+qwave[i]**2)
    sig_amp = np.sqrt(np.mean(power))
    print [sig_amp, length]
    return sig_amp


#IQ Constellation figure
def const_plot(filename):
    real_data=get_csv_vect(filename,3,1);
    image_data=get_csv_vect(filename,3,2);
    plot_scatter(real_data,image_data,label='I/Q map',xlabel='I',ylabel='Q',title='Constellation');

#fft onetime,not average
def fft_onetime(filename,sample_freq_mhz=44,center_freq_mhz=0):
    real_data=get_csv_vect(filename,3,1);
    image_data=get_csv_vect(filename,3,2);
    if real_data!=[] and image_data!=[]:
       fftdata=fft_calc(real_data,image_data);
       fft_plot(fftdata,sample_freq_mhz,center_freq_mhz);
    else:
       print 'fail to get data from file';

#fft average multi times
#path tail not include '/', correct way lik './log/testcase'
def fft_average(path,sample_freq_mhz=44,center_freq_mhz=0):
    filelst= filefind(path,'AdcDump*.csv');
    n=len(filelst);
    if n>0:
       for i,filename in enumerate(filelst):
           real_data=get_csv_vect(filename,3,1);
           image_data=get_csv_vect(filename,3,2);
           if i==0:
              fftdata=fft_calc(real_data,image_data);
           else:
              fftdata=fftdata+fft_calc(real_data,image_data);
    else:
       print 'fail to find file in specific path';
       return;
    fftdata=fftdata/n;
    fft_plot(fftdata,sample_freq_mhz,center_freq_mhz);

