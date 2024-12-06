#!/usr/bin/env python
#test function for chip_v4.0

import csv
import re
import sys
import numpy as np
import mfunc as mf
from pylab import *
from iofunc import *
import copy

rcParams['legend.loc'] = 'best'

class fig:
    ID = ''
    labelx = ''
    labely = ''
    X = []
    Y = []
    legends = []
    subtitle = []
    pdf=''

def dict2fig(D, xkey = [], ykey = [], legends=[], xylabel=[], subtitle=[], pdf=''):
    """ select X, Y from dict """
    F = fig()
    V = np.array(D.values())
    F.X = np.transpose(V[mf.index(D.keys(), xkey), :])
    F.Y = np.transpose(V[mf.index(D.keys(), ykey), :])
#     print F.X
#     print F.Y
    F.X = reshape(F.X, (size(F.X, 0), size(F.X, 1), 1), order='F')
    F.Y = reshape(F.Y, (size(F.Y, 0), size(F.Y, 1), 1), order='F')
    if legends:
        F.legends = legends
    else:
        F.legends = ykey
    F.subtitle = subtitle
##    if xfunc not in (None, ''):
##        X = F.X
##        F.X = eval(xfunc)
    if xylabel:
        [F.labelx, F.labely] = xylabel
    else:
        [F.labelx, F.labely] = [xkey[0], ykey[0]]

    F.pdf = pdf
    return F
    

def mplot(F, nfig=0):
    if isinstance(F, list):
        for i in range(len(F)):
            figure(nfig+i)
            mplot(F[i])
    else:
        clf()
                
        [M, N, P] = [size(F.Y, 0), size(F.Y, 1), size(F.Y, 2)]
        k = int(sqrt(P))
        if P > k*k:
            k = k + 1
        l = int(floor(P)/k)
        if mod(P, k) !=0:
            l = l+1
    ##    print k, l
        symbols = ['b-o', 'r-x', 'k-d', 'm-s', 'c-*', 'g-v', 'y-+', \
                   'b-x', 'r-d', 'k-s', 'm-*', 'c-v', 'g-+', 'y-o', \
                   'b-d', 'r-s', 'k-*', 'm-v', 'c-+', 'g-o', 'y-x', \
                   'b-s', 'r-*', 'k-v', 'm-+', 'c-o', 'g-x', 'y-d', \
                   'b-*', 'r-v', 'k-+', 'm-o', 'c-x', 'g-d', 'y-s', \
                   'b-v', 'r-+', 'k-o', 'm-x', 'c-d', 'g-s', 'y-*', \
                   'b-+', 'r-o', 'k-x', 'm-d', 'c-s', 'g-*', 'y-v', \
                   'b:o', 'r:x', 'k:d', 'm:s', 'c:*', 'g:v', 'y:+', \
                   'b:x', 'r:d', 'k:s', 'm:*', 'c:v', 'g:+', 'y:o', \
                   'b:d', 'r:s', 'k:*', 'm:v', 'c:+', 'g:o', 'y:x', \
                   'b:s', 'r:*', 'k:v', 'm:+', 'c:o', 'g:x', 'y:d', \
                   'b:*', 'r:v', 'k:+', 'm:o', 'c:x', 'g:d', 'y:s', \
                   'b:v', 'r:+', 'k:o', 'm:x', 'c:d', 'g:s', 'y:*', \
                   'b:+', 'r:o', 'k:x', 'm:d', 'c:s', 'g:*', 'y:v']
        for p in range(P):
            plotstr = 'plot('
            legends = []
            subplot(100*l+10*k+p+1)
            for n in range(0, N):
                plotstr = '%sF.X[:, %d, p], F.Y[:, %d, p], symbols[%d],'%(plotstr, n, n, n)

            plotstr = re.sub(',\)', ')', plotstr+')')
    ##        print plotstr
            eval(plotstr)
            if p == 0:
                legend(F.legends, loc=0)
            
            xlabel(F.labelx)
            ylabel(F.labely)
            grid(True)
            if F.subtitle[0]:
                title(F.subtitle[p])
        if F.pdf:
            d = os.path.dirname(F.pdf)
            if not os.path.exists(d):
                os.makedirs(d)
            savefig(F.pdf)
##            savefig(re.sub('\.pdf', '.emf', F.pdf))
    ##    show()

def figprocess(F, Type):
    if Type == 'fig2subfig':
        G = copy.copy(F[0])
        X = []; Y = []; subtitle = [];
        for f in F:
            subtitle.append(f.subtitle[0])
            X.append(f.X)
            Y.append(f.Y)
        G.X = np.dstack(X)
        G.Y = np.dstack(Y)
        G.subtitle = subtitle
        return G
    elif Type == 'mline2X':
        dim = [size(F.X, 1), size(F.X, 0), size(F.X, 2)]
        F.X = np.reshape(F.X, dim, order = 'F')
        F.Y = np.reshape(F.Y, dim, order = 'F')

        legends = np.array(map(lambda x:x.split('='), F.legends))
        for p in range(dim[2]):
            for n in range(dim[1]):
                F.X[:, n, p] = map(float, legends[:, 1])
##        print legends
        F.legends, F.labelx = [F.labelx], legends[0,0]
##        print F.legends
##        print F.labelx
##        print F.ID
        return F
    elif Type == 'mline2subfig':
        dim = [size(F.X, 0), size(F.X, 2), size(F.X, 1)]
        F.X = np.reshape(F.X, dim, order = 'F')
        F.Y = np.reshape(F.Y, dim, order = 'F')

        F.legends, F.subtitle = F.subtitle, F.legends
#         print F.legends
#         print F.subtitle
##        print F.ID
        return F
    elif Type == 'merge':
        G = copy.copy(F[0])
        X = []; Y = []; legends = [];
        for f in F:
            print f.legends, f.ID, mf.strcat(f.ID+'-', f.legends)
            if f.ID and (f.ID !=f.legends[0]):
                legends.extend(mf.strcat(f.ID+'-', f.legends))
            else:
                legends.extend(f.legends)
            X.append(f.X)
            Y.append(f.Y)
##        print legends
        G.X = np.hstack(X)
        G.Y = np.hstack(Y)
        G.legends = reshape(legends, -1)
##        print size(F[0].X, 0), size(F[0].X, 1), size(F[0].X, 2)
##        print size(G.X, 0), size(G.X, 1), size(G.X, 2)
        return G
    else:
        return F

def csv2fig(csvfile, data_format = 'ATE', xvar=None, xfunc=None, 
            yvar=None, yfunc=None, xyfunc=None, sweptvar='', 
            sweptval='', plotmap='', ID=None, pdf=None, ycellfunc=None, ylabel='', xlabel=''):
    """ csv2data load csv file to data

    set comment='#%' (default = '') to filter out lines start with #%   """

    [sweptvar, sweptval, plotmap] = map(mf.str2cellstr, [sweptvar, sweptval, plotmap])
    D = csv2data(csvfile, data_format=data_format)
    D = zip(*D)
    d = {''   :[]}
    for i in range(0, len(D)):
        row = D[i]
        d[D[i][0]] = D[i][1:]
    k = d.keys().index(xvar)

    if ycellfunc:
        d[yvar] = [eval(ycellfunc) for x in d[yvar]]
        
    F = fig()
    F.labelx = xvar
    if xlabel:
        F.labelx = xlabel

    if ylabel:
        F.labely = ylabel
    else:
        F.labely = yvar

#     print d.keys()
    F = data_reshape(F, d, xvar, yvar, 
                     sweptvar, sweptval, plotmap)
#     print F.Y
    if xfunc not in (None, ''):
        X = F.X
        F.X = eval(xfunc)
    if yfunc not in (None, ''):
        Y = F.Y
#         print F.Y
        
        F.Y = eval(yfunc)
    if xyfunc not in (None, ''):
        F = eval(xyfunc)
    if pdf not in (None, ''):
        F.pdf = pdf

    F.subtitle = [ID]
    F.ID = ID
    
    return F


def data_reshape(F, dic, xvar, yvar, 
                 sweptvar=None, sweptval=None, plotmap=None):
    """ data_reshape convert 1-D data to m-D figure data   """
    dim = []; swept = {''   :[]}
#     print dic
    for item in sweptvar:
        dim.append(len(unique(dic[item])))
    if len(dim) == 2:
        dim.append(1)
    F.X = np.array(mf.str2num(dic[xvar]))
    F.Y = np.array(mf.str2num(dic[yvar]))
#     print F.Y
    F.X = np.reshape(F.X, dim, order='F')
    F.Y = np.reshape(F.Y, dim, order='F')
    for i in range(len(sweptvar)):
        swept[sweptvar[i]] = [mf.str2num(mf.unique_no_sort(dic[sweptvar[i]])), \
                              mf.str2num(mf.unique_no_sort(dic[sweptvar[i]]))]
    if sweptval != ['']:
        for item in sweptval:
            [var, val] = item.split('=')
##            print val
            swept[var][1] = eval(val)
    for i in range(len(sweptvar)):
        idx = [':', ':', ':']
        var = sweptvar[i]
        if swept[var][0] != swept[var][1]:
            idx[i] = mf.index(swept[var][0], swept[var][1])
            F.X = eval("F.X[%s, %s, %s]"%(idx[0], idx[1], idx[2]))
            F.Y = eval("F.Y[%s, %s, %s]"%(idx[0], idx[1], idx[2]))
##            print idx        
        if i == 1:
            F.legends = mf.strcat(var+'=', map(str, swept[var][1]))
        elif i == 2:
            F.subtitle = mf.strcat(var+'=', map(str, swept[var][1]))
   
    return F
    
def xinterp(F, xval):
    """ xinterpolation to certain xvalues """
    G = copy.copy(F);
    [M, N, P] = [size(F.Y, 0), size(F.Y, 1), size(F.Y, 2)]
    G.X = np.array(ones([size(xval), N, P]))
    G.Y = np.array(ones([size(xval), N, P]))
    for p in range(P):
        for n in range(N):
            G.X[:, n, p] = xval
            G.Y[:, n, p] = interp(xval, F.X[:, n, p], F.Y[:, n, p])
    return G
    
def calibrate(F, Type):
    """ xinterpolation to certain xvalues """
    if Type == 'SA':
        SA = data2num(csv2data('../common/datalist/datalist_SA.csv', comment='#'))
        SA = np.array(SA[1:])
        [N, P] = [size(F.X, 1), size(F.X, 2)]
        for p in range(P):
            for n in range(N):
                F.Y[:, n, p] += interp(F.X[:, n, p], SA[:, 0], SA[:, 1])
                  
    return F
    
