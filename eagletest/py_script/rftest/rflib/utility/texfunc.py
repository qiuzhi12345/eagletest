#!/usr/bin/env python
#test function for chip_v4.0

import csv, re, os, xlrd, xlwt, time, copy
import numpy as np
import mfunc

def latexobj(F):
    """Create LaTeX scripts
    
    Keyword arguments:
    
    * F -- a dict or dict array with fields like "caption", "label", "data", ...etc

    Remarks:
    
    * If F is a vector, function is applied to each element of F
    * Two kind of objects are supported:
    
        * figure -- "figure" object that links the graphic file 
        * deluxetable -- "deluxtable" object by czwanglib.download.texTable.Table
    
    See Also: rfplot.printLatex
    
    """
    
    if isinstance(F, (list, tuple)):
        [latexobj(x) for x in F]
        return
    
    if F['object'].lower()=='figure':
        C = [[r'\begin{figure}[htbp]'], 
             [r'\centering'], 
             [r'\includegraphx{%s}{%s}'%(F['fileName'], F['width'])],
             [r'\caption{%s}'%F['caption']],
             [r'\label{fig:%s}'%F['label']],
             [r'\end{figure}'],
             []]
        return C
        
    elif F['object'].lower()=='deluxetable':
        import czwanglib.download.texTable.Table as Table
        texfile = '%s/Table_%s.tex'%(F['dir_tex'], F['runset'])
        print 'printing to %s ...'%texfile
        fout = open(texfile,'w')
#         print F
        t = Table.Table(len(F['data'][0]), justs=F['align'], caption=F['caption'], label="tab:%s"%F['label'])
        t.add_header_row(F['data'][0])
        D = mfunc.transpose(F['data'][1:])
        for i in range(len(D)):
            D[i] = [re.sub(r'\|', r'$|$', x) for x in D[i] ]
#         print D
        t.add_data(D, sigfigs=2)
        t.print_table(fout)
        fout.close()        

    
