from numpy import *
from pandas import *
import matplotlib.pyplot as plt

def diffex(ff, df, x, n):
    H=[]; D=[]; E=[]
    step = 1.0
    dftrue = df(x)
    for i in arange(0,n+1):
        h=step/10**i
        H.append(h)
        D.append((ff(x+h)-ff(x-h))/(2*h))
        E.append(abs(dftrue-D[i]))
    
    res=DataFrame({'step size':H, 'finite difference':D, 'true error':E})
    print(res)
    plt.plot(H, E)
    plt.title('Plot of Error Versus Step Size')
    plt.xlabel('Step Size')
    plt.ylabel('Error')
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
