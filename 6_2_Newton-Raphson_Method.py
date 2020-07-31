#Newton-Raphson Method:
#  x[i+1]=x[i]-f(x[i])/f'(x[i])
#use the Newton-Raphson method to estimate the root of f(x)=e**(-x)-x
#employing an initial guess of x[0]=0

from numpy import *
from pandas import *

i=arange(5)
x=zeros(5)
et=zeros(5)
true_value=0.56714329
    
for n in i:
    if n==0:
        et[n]=100
    else:
        tmp=e**(-x[n-1])
        x[n]=x[n-1]-(tmp-x[n-1])/(-tmp-1)
        et[n]=abs((true_value-x[n])/true_value)*100

data={'i':i, 'xi':x, '|et|,%':et}
df=DataFrame(data)
print(df)
