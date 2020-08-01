#memo:
"""
from sympy import *
x=Symbol("x")
res=diff(x**2, x)
"""
#use the Newton-Raphson methon to estimate the root of func
#input:
#  func=name of function
#  dfunc=name of derivative of function
#  xr=initial guess
#  es=desired relative error (default=0.0001%)
#  maxit=maximum allowable iterations (default=50)
#  *args=additional papameters used by function
#output:
#  root=real root
#  ea=approximate relative error (%)
#  itera=number of iterations
from numpy import *
def newtraph(func, dfunc, xr, es=0.0001, maxit=50, *args):
    itera=0
    while(1):
        xrold=xr
        xr=xr-func(xr)/dfunc(xr)
        itera=itera+1
        if xr !=0:
            ea=abs((xr-xrold)/xr)*100
        if ea<=es or itera>=maxit:
            break
    root=xr
    return root, ea, itera
