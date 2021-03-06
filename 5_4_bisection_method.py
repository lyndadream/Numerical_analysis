#use bisection method to find the root of func
#example:
#  fm=lambda m,cd,t,v:sqrt(9.81*m/cd)*tanh(sqrt(9.81*cd/m)*t)-v
#  a=bisect(fm,40,200,0.0001,50,0.25,4,36)
#input:
#  func = name of function
#  xl, xu = lower and upper guesses
#  es = desired relative error (default = 0.0001%)
#  maxit = maximum allowable iterations (default = 50)
#  *args = additional parameters used by func
#output:
#  root = real root
#  fx = function value at root
#  ea = approximate relative error (%)
#  itera = number of iterations
from numpy import *
def bisect(func, xl, xu, es=0.0001, maxit=50, *args):
    test=func(xl, *args)*func(xu, *args)
    if test > 0: return None
    itera=0; xr=xl; ea=100
    while(1):
        xrold=xr
        xr=(xl+xu)/2
        itera=itera+1
        if xr !=0:
            ea=abs((xr-xrold)/xr)*100
        test=func(xl, *args)*func(xr, *args)
        if test<0:
            xu=xr
        elif test>0:
            xl=xr
        else:
            ea=0
        if ea<=es or itera>=maxit:
            break
    root=xr; fx=func(xr, *args)
    res=[root, fx, ea, itera]
    return res
