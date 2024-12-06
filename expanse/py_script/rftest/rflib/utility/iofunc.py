#!/usr/bin/env python
#test function for chip_v4.0

import csv, re, os, xlrd, xlwt, time, copy
import numpy as np
import mfunc
from ordereddict import OrderedDict

def dirlist(pathstr='.', file_exp='\w+\.\w+', path_exp=''):
    """Return a list of all filenames that matches a pattern in a dir (include subdirs)"""
    l = []
    for dirpath, dirnames, filenames in os.walk(pathstr):
        for filename in [f for f in filenames if re.match(file_exp, f)]:
            if not path_exp or re.findall(path_exp, dirpath):
                l.append(os.path.join(dirpath, filename))
    return l
        
def mvfile(fullFile, Type ='mdate'):
    """ move filename.ext to filename_mdate.ext     """
    fileName, ext = os.path.splitext(fullFile)
    if Type == 'mdate':
        fileTime= time.strftime('%Y%m%d_%H%M%S', time.localtime(os.path.getmtime(fullFile)))
##        print fullFile, '%s_%s%s'%(fileName, fileTime, ext)
        os.rename(fullFile, '%s_%s%s'%(fileName, fileTime, ext))


def xls2list(xlsfile, sheet='', loc=[0,0], Nrow=0, Ncol=0):
    def cell2int(cell):
        """Convert Excel integer into Python integer."""
        value = cell.value
        if cell.ctype in (2,3) and int(cell.value) == cell.value:
            value = int(cell.value)
        return value
        
    if re.search('\w+\.xls.*$', xlsfile) and sheet:
        rb = xlrd.open_workbook(xlsfile)
        shxrange = range(rb.nsheets)
        try:
            sh = rb.sheet_by_name(sheet)
        except:
            print "no sheet in %s named %s" %(xlsfile, sheet)
            return None
        nrows = sh.nrows
        ncols = sh.ncols

        row_list = []
        if Nrow:
            Nrow += loc[0]
        else:
            Nrow = nrows
            
        if Ncol:
            Ncol += loc[1]
        else:
            Ncol = ncols
            
        for m in range(loc[0], Nrow):
            row_data = []
            for n in range(loc[1], Ncol):
#                 print sh.cell(m, n)
                row_data.append(str(cell2int(sh.cell(m, n))))
            row_list.append(row_data)
        return row_list

# def xlswrite(D, xlsfile, sheetName='', loc=[0,0]):
#     """ create/update an excel file  """
#     if os.path.exists(xlsfile):     # xls file exists
#         from xlutils.copy import copy
#         rb = xlrd.open_workbook(xlsfile,formatting_info=True)
#         wb = copy(rb)
#         sheet_names = map(str, rb.sheet_names())
#         if sheetName in sheet_names:    # new sheet name
#             ws = wb.get_sheet(sheet_names.index(sheetName))
#         else:
#             ws = wb.add_sheet(sheetName)
#     else:           # new xls file
#         wb = xlwt.Workbook()
#         ws = wb.add_sheet(sheetName)
# 
#     plain = xlwt.easyxf('')
#     if isinstance(D, list):
#         for m in range(len(D)):
#             for n in range(len(D[m])):
#                 setOutCell(ws, loc[0]+m, loc[1]+n, D[m][n])
# #                 ws.write(loc[0]+m, loc[1]+n,D[m][n])
#     elif isinstance(D, np.ndarray):
#         for m in range(np.size(D, 0)):
#             for n in range(np.size(D, 1)):
#                 setOutCell(ws, loc[0]+m, loc[1]+n, D[m, n])
# #                 ws.write(loc[0]+m, loc[1]+n,D[m,n])
# 
#     wb.save(xlsfile)
    
def xlswrite(D, xlsfile, sheetName='Sheet1', loc=[0,0], 
             pathstr=os.getcwd(), cond_format={}, formula={}, autofit={}):
    """ create/update an excel file  """
    
    import win32com.client as win32
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    xlsfile = os.path.join(pathstr, xlsfile)
    print xlsfile

    try:
        wb = excel.Workbooks.Open(xlsfile)
    except:
        wb = excel.Workbooks.Add()
        wb.SaveAs(xlsfile)
    wb.Worksheets(sheetName).Activate()
    ws = wb.Worksheets(sheetName)

    if D:
        if not isinstance(D, tuple):
            D = (D, )
            loc = (loc,)
        for i in range(len(D)):
            if isinstance(D[i], np.ndarray):
                D[i] = D[i].tolist()
            range_data = xlsloc(loc[i])+':'+xlsloc([loc[i][0]+len(D[i])-1, loc[i][1]+len(D[i][0])-1])
            ws.Range(range_data).Value = D[i]
#     ws.Range('N2:BR80').Select()
#     wb.SaveAs(xlsfile)
#     ws.Range(range_data).Select()
    if formula:
        [xls_formula(win32, excel, ws, x) for x in formula]
    if cond_format:
        [xls_cond_format(win32, excel, ws, x) for x in cond_format]
    if autofit:
        print "autofitting the width of column %s..."%autofit['range']
        ws.Columns(autofit['range']).Select()
        ws.Columns(autofit['range']).EntireColumn.AutoFit()

    
    wb.SaveAs(xlsfile)
#     excel.Quit()

def xlsloc(loc=[0,0]): 
    """Convert XY location in excel format. [0,0]->A1"""
    if isinstance(loc, list):
        if isinstance(loc[0], list):
            loc=[xlsloc(x) for x in loc]
            loc = ':'.join(loc)
        else:
            ncol = loc[1]
            loc_y = ''
            while ncol//26:
    #             print chr(ncol%26+97)
                loc_y = chr(ncol%26+97).upper() + loc_y
                ncol = ncol//26-1
            loc_y = chr(ncol%26+97).upper() + loc_y
            loc = '%s%d'%(loc_y, loc[0]+1)
    else:       # analyze column
        ncol = loc
        loc_y = ''
        while ncol//26:
            loc_y = chr(ncol%26+97).upper() + loc_y
            ncol = ncol//26-1
        loc = chr(ncol%26+97).upper() + loc_y
    return loc
            
def xls_cond_format(win32, excel, ws, cond_format):
    """Create "conditional Format" by equations."""
    ws.Range(cond_format['range']).Select()
    excel.Selection.FormatConditions.Delete()   # delete existing cond format
    excel.Selection.FormatConditions.Add(Type=win32.constants.xlExpression, Formula1=cond_format['formula'])
    excel.Selection.FormatConditions(excel.Selection.FormatConditions.Count).SetFirstPriority()
    x = excel.Selection.FormatConditions(1).Interior
    x.PatternColorIndex = win32.constants.xlAutomatic
    x.Color = cond_format['color']
    x.TintAndShade = 0

def xls_formula(win32, excel, ws, formula):
    """Create "conditional Format" by equations."""
    range = formula['range'].split(':')
#     print range
#     print formula['formula']
    if 'formula_array' in formula and formula['formula_array']:
        ws.Range(range[0]).FormulaArray = formula['formula']
    else:
        ws.Range(range[0]).Formula = formula['formula']
    ws.Range("%s:%s"%(range[0], range[0])).Select()
    if range[1] != range[0]:
        excel.Selection.AutoFill(ws.Range(formula['range']), win32.constants.xlFillDefault)
   

def _getOutCell(outSheet, colIndex, rowIndex):
    """ HACK: Extract the internal xlwt cell representation. """
    row = outSheet._Worksheet__rows.get(rowIndex)
    if not row: return None

    cell = row._Row__cells.get(colIndex)
    return cell

def setOutCell(outSheet, row, col, value):
    """ Change cell value without changing formatting. """
    # HACK to retain cell style.
    previousCell = _getOutCell(outSheet, col, row)
    # END HACK, PART I

    outSheet.write(row, col, value)

    # HACK, PART II
    if previousCell:
        newCell = _getOutCell(outSheet, col, row)
        if newCell:
            newCell.xf_idx = previousCell.xf_idx
    # END HACK



def getchoice(L, key='', key_exp='', prompt='Choice list', scalar=False, midx=[], xchoices='?', outvar='choice'):
    """ select a choice from a list  """
## -------------------- Multiple Key ------------------------------
    if isinstance(key, list):
        D = copy.copy(L)
        res = []
        midx = range(len(D[key[0]]))
        for i in range(len(key)):
            res.append(getchoice(D, key[i], prompt=prompt[i],
                            scalar=scalar[i], midx=midx, xchoices=xchoices))
            L = D[key[i]]
            idx = [j for j in range(len(L)) if L[j]==res[i]]
            midx = list(set(midx) & set(idx))
        return res
## -------------------- Single Key ------------------------------
    if isinstance(L, dict):
        D = L
        L = L[key]
    if midx:
        L = [L[i] for i in midx]
    L = [L[i] for i in range(len(L)) if L[i]]   # remove empty cells
    L = np.unique(L)
    if key_exp and mfunc.indexreg(L, key_exp):
        L = L[mfunc.indexreg(L, key_exp)] 
    
    if xchoices == '*':
        res = L
    elif xchoices == '?':
        d = dict()
        idx = range(ord('0'), ord('9'))
        idx.extend(range(ord('a'), ord('z')))
        idx.extend(range(ord('A'), ord('Z')))
        idx = map(chr, idx)
    ##    print idx
        print "----------- %s ----------"%prompt
        for i in range(min(len(L), len(idx))):
            d[idx[i]] = L[i]
            print '\t%s: %s'%(idx[i], L[i])
        choices = raw_input("Enter your choice [0-%s]: "%(idx[i]))
        if not choices:
            print "warning: no choice is made...."
            res = []
        elif choices == '*':
            res = d.values()
        else:
            res = [d[x] for x in choices]
    if outvar == 'dict_vector':
        k = []
        [k.extend(mfunc.indexreg(D[key], '^%s$'%x)) for x in res]
#         print k, res, D[key]
        for key in D:
            D[key] = D[key][k]
        res = mfunc.tovector(D)
    

    if scalar:
        if len(res) > 1:
            print "Warning: multiple choices, only 1st choice is kept!"
        res = res[0]
    return res


def regexpfile(infile, regexp):
    """ return certain regexp in a text file """
    fid = open(infile, 'rU');
    C = [line for line in fid]
    fid.close()
    x = dict()
    x['nline'] = []
    x['match'] = []
    for i in range(len(C)):
        if re.search(regexp, C[i]):
            x['match'].append(re.match(regexp, C[i]))
            x['nline'].append(i)

    return x

def cleancsv(fid, data_format = 'ATE'):
    C = [line for line in fid]
    if data_format == 'ATE':
        nheader = 3
        xls = './automation/piccolo/plot_list.xlsx'
        del C[0:nheader+1]
        # header mapping
        hmap = mfunc.transpose(csv2data(xls, 'map', comment='#'))
##        print C[0]
        C[0] = mapstr(C[0], hmap[0], hmap[1])
##        print C[0]
        C[1:] = mapstr(C[1:], ['"', r'-1.#J'], ['', 'None'])
#         print C
    else:
        pass
    return C

def mapstr(C, exp_old, exp_new):
    def f(x):
        return mapstr(x, exp_old, exp_new)
    if isinstance(C, (list, tuple)):
        C = map(f, C)

    elif isinstance(C, str):
        for i in range(len(exp_old)):
            C = re.sub(exp_old[i], exp_new[i], C)
    return C


def csv2data(csvfile, sheet='', comment='', 
             nheader=0, data_format=None, strxpand='', nidx_fillchar=None):
    """ csv2data load csv file to data

    set comment='#%' (default='') to filter out lines start with #%   """

    if re.search(r'.*\.csv$', csvfile):
        infile = open(csvfile, 'rU');
        C = cleancsv(infile, data_format)
        csv_in = list(csv.reader(C));
        infile.close()
    elif re.search('\w+\.xls.*$', csvfile) and sheet:
        csv_in = xls2list(csvfile, sheet)

    D = []
    for row in csv_in:
        if row==[] or row[0]=='' or (not row[0][0] in comment):
            D.append(row)
    if nheader > 0:
        del D[0:nheader]

##    print strxpand
    if strxpand:    # expand a certain column
        E = []
        k = D[0].index(strxpand)
        for i in range(len(D)):
            v = D[i][k].split(' ')
            for j in range(len(v)):
                x = copy.copy(D[i])
                x[k] = v[j]
##                print x
                E.append(x)
        D = E
    
    if nidx_fillchar != None:
        for m in range(len(D)):
            if D[m][nidx_fillchar]=='' and m>0:
                D[m][nidx_fillchar] = D[m-1][nidx_fillchar]

    return D

def data2filter(C, condition):
    ''' filter specific column, 1st row of data is header row. e.g.   '''

    [header, val] = condition
    D = [C[0]]
##    print C[0]
##    print header
    k = C[0].index(header)
    for row in C:
        if row[k] == val:
            D.append(row)
    return D

def data2num(C, dim = 2):
    ''' convert any numeric row/col to numbers  '''
    D = C
    if dim == 1:
        for i in range(len(D)):
            D[i][1:] = mfunc.str2num(D[i][1:])
    elif dim == 2:
        D = mfunc.transpose(data2num(mfunc.transpose(D), dim = 1))
    return D


def data2csv(csvfile, data, header = '', axis = 1, mode='wb'):
    """ data2csv write data to csv file
    if data is tuple, arrange them in columns

    set header=['#block', 'net', ...] (default = '') to include header line   """
    print "--- printing to '%s' ... "%csvfile
    outfile = open(csvfile, mode);
    csv_out = csv.writer(outfile)
    if header:
        csv_out.writerow(header)
    if isinstance(data, tuple):
        data = map(np.array, data)
        data = np.concatenate(data, axis = axis)
##        print data
    for i in range(0, len(data)):
        csv_out.writerow(data[i])

    outfile.close()
    return data

def data2csv_test(csvfile, data, header = '', axis = 1, mode='wb'):
    outfile = open(csvfile, mode);
    csv_out = csv.writer(outfile)
    if header:
        csv_out.writerow(header)
    if isinstance(data, tuple):
        data = map(np.array, data)
        data = np.concatenate(data, axis = axis)
    #for i in range(0, len(data)):
    #    csv_out.writerow(data[i])
    csv_out.writerow(data)

    outfile.close()
    return data


def csv2dict(csvfile='', sheet='', nkey=1, idx_key=None, idx_val=None, 
             func_key=None, func_val=None, nidx_fillchar=None, conflict_key='overwrite',
             comment='#%', filter_col=None, str2num=False, axis=0, strxpand='', val_list=False):
    """ csv2dict convert a csv file into a dict with the first

    'nkey' column as the key 
    
    """

    def list2key(row, idx, iskey=False):
        """Convert list based on the idx"""
        if isinstance(idx, list):
            # convert to scalar if tuple/list has only one element
            if len(idx) == 1:
                val = row[idx[0]]
            else:
                val = [row[i] for i in idx]
                if iskey:
                    val = tuple(val)
        else:
            val = row[idx]
        return val
        
    nkey = int(float(nkey))     # convert string to int
    dict0 = OrderedDict()
    csv_in = csv2data(csvfile, sheet=sheet, comment=comment, strxpand=strxpand, nidx_fillchar=nidx_fillchar);
    
    if filter_col:
        csv_in = data2filter(csv_in, filter_col)
    if str2num:
        csv_in = data2num(csv_in, dim=2)
    
    N = len(csv_in[0])
    if not idx_key:
        idx_key = range(0, nkey)
    if not idx_val:
        idx_val = range(nkey, N)
        
    if axis == 0:
        for i, row in enumerate(csv_in):
            key = list2key(row, idx_key, iskey=True)
            val = list2key(row, idx_val)
                
            if func_key:
                key = func_key(key)
            if func_val:
                val = func_val(val)
            
            if key not in dict0 or conflict_key=='overwrite':
                dict0[key] = val
            else:
                if not isinstance(dict0[key], list):
                    dict0[key] = [dict0[key]]
                dict0[key].append(val) 
    elif axis == 1:         # BUG: not support idx_key and idx_val
        keys = csv_in[nkey-1]
        vals = np.array(csv_in[nkey:])
        for i in range(len(keys)):
            dict0[keys[i]] = vals[:, i]
    
    if val_list:
        for key in dict0:
            if not isinstance(dict0[key], list):
                dict0[key] = [dict0[key]]
    return dict0

def csv2define(csvfile, sheet, def_file, def_str):
    data = csv2data(csvfile, sheet, comment='#%')
    f = open(def_file, 'w')
    for i in range(0, len(data)):
        D = data[i]
        [addr,msb,lsb,ctrl_name] = [int(D[0]), int(D[1]), int(D[2]), D[3]]
        ctrl_name = re.sub(r'''\[[\d:]*\]''', '', ctrl_name)
        f.write('#define '+def_str+'_'+ctrl_name+'        '+str(addr)+'\n')
        f.write('#define '+def_str+'_'+ctrl_name+'_msb    '+str(msb)+'\n')
        f.write('#define '+def_str+'_'+ctrl_name+'_lsb    '+str(lsb)+'\n')
        f.write('\n')

def csv2regdict(xls, sheet, dict_type='addr'):
    """Extract an addr/ctrl dict from i2c table
    
    for example:
        dict_type = 'ctrl'
        output = {
            "TMX2G_CCT_LOAD"    	:[1,3,0,4],
            "TMX2G_RCT_LOAD"    	:[1,6,4,0],
            ...
        dict_type = 'addr'
        output = {
            1    	:10,
            2       :0,
            ...
    
    """
    regs = {}
    if sheet == 'txrf': sheet = 'rftx'    # name alias

    csv_in = csv2data(xls, sheet, comment='#%')
    for row in csv_in:
        [addr,msb,lsb] = [int(float(x)) for x in row[0:3]]
        [ctrl_name, rw, value] = row[3:6]
        if rw.lower() == 'r':
            value = 'b0'
        if dict_type == 'ctrl':
            value = int(value.replace('b',''), 2)
            ctrl_name = re.sub(r'''\[[\d:]*\]''', '', ctrl_name)
            regs[ctrl_name] = [addr, msb, lsb, value]
        elif dict_type == 'addr':
            if rw.lower() != 'r':
                value = list(value.replace('b',''))
                value.reverse()
                regs.setdefault(addr, ['0']*8)
                regs[addr][lsb:msb+1] = value
        else:
            print "error: '%s' is not a valid type"%dict_type
    if dict_type == 'addr':
        for addr in regs:
            regs[addr].reverse()
            regs[addr] = ''.join(regs[addr])  # convert to binary str
            regs[addr] = int(regs[addr], 2)
    return regs
