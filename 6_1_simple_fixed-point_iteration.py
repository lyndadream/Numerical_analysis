#fixed-point iteration:
#  f(x)=0 → x=g(x)
#  x[i+1]=g(x[i])
#use simple fixed-point iteration to locate the root of f(x)=e**(-x)-x
#starting with an initial guess of x[0]=0
from numpy import *
from pandas import *

i=arange(11)
x=zeros(11)
ea=[' ']
et=zeros(11)
et_et=[' ']
true_value=0.56714329
    
for n in i:
    if n==0:
        et[n]=100
    else:
        x[n]=e**(-x[n-1])
        ea.append(abs((x[n]-x[n-1])/x[n])*100)
        et[n]=abs((true_value-x[n])/true_value)*100
        et_et.append(et[n]/et[n-1])
data={'i':i, 'xi':x, '|ea|,%':ea, '|et|,%':et, '|et|i/|et|i-1':et_et}
df=DataFrame(data)
print(df)
