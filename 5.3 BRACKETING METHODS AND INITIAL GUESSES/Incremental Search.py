#finds bracket of x that contain sign changes of a function on an interval
#input:
#  func=name of function
#  xmin, xmax=endpoints of interval
#  ns=number of subintervals (default=50)
#output:
#  xb[k][0] is the lower bound of the kth sign change
#  xb[k][1] is the upper bound of the kth sign change

#example
#f=lambda x: sin(10*x)+cos(3*x)
#incsearch(f, 3, 6, 100)

from numpy import *
def incsearch(func, xmin, xmax, ns=50):
    x=linspace(xmin, xmax, ns, endpoint=False)
    f=func(x)
    xbl=[]; xbu=[]
    for k in arange(0,ns-1):
        if sign(f[k]) != sign(f[k+1]):
            xbl.append(x[k])
            xbu.append(x[k+1])
    xb=hstack((array(xbl).reshape(len(xbl), 1), array(xbu).reshape(len(xbu),1)))
    if xb.any():
        print("number of brackets:",len(xbl))
    else:
        print("no brackets found, check interval or increase ns")
