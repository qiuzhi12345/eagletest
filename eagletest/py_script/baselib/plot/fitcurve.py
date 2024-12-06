import numpy as np
from scipy.optimize import leastsq
import pylab as pl

def sinfunc(x, p):
    """
    data fit function: A*sin(2*pi*k*x + theta)
    """
    A, k, theta = p
    return A*np.sin(2*np.pi*k*x+theta)

def sinresiduals(p, y, x):
    """
    difference between test data y and fitting func(x,p), p is wanted fitting figures
    """
    return y - sinfunc(x, p)


def sinfit(xdata,ydata,p0,show_fig=1):
    """
    fit sin curve A*sin(2*pi*k*x+theta),get p=[A,k,theta]
    y is test data,p0 is initial params of p
    """
    x = np.array(xdata);
    y = np.array(ydata);

    # call leastsq to fit data
    # residuals for calculating remained error
    # p0 is initial param
    # args is test data
    plsq = leastsq(sinresiduals, p0, args=(y, x))
    
    if show_fig==1:
       pl.plot(x, y, label="test data")
       pl.plot(x, sinfunc(x, plsq[0]), label="fit curve")
       pl.legend()
       pl.show()

    print "fitting params", plsq[0] # fitting params
    return plsq[0]

def linefunc(x, p):
    """
    data fit function: k*x+b
    """
    k,b = p
    return k*x+b

def lineresiduals(p, y, x):
    """
    difference between test data y and fitting func(x,p), p is wanted fitting figures
    """
    return y - linefunc(x, p)


def linefit(xdata,ydata,show_figure=0,p0=[1,0]):
    """
    fit line k*x+b,get p=[k,b]
    y is test data,p0 is initial params of p
    """
    x = np.array(xdata);
    y = np.array(ydata);

    # call leastsq to fit data
    # residuals for calculating remained error
    # p0 is initial param
    # args is test data
    plsq = leastsq(lineresiduals, p0, args=(y, x))
    
    if show_figure!=0:
       pl.plot(x, y, label="test data")
       pl.plot(x, linefunc(x, plsq[0]), label="fit curve")
       pl.legend()
       pl.show()

    print "fitting params", plsq[0] # fitting params
    return plsq[0]
