#use the graphical approach to obtain an estimate of the root of f(m)=0

import matplotlib.pyplot as plt
from numpy import *

cd=0.25; g=9.81; v=36; t=4
mp=linspace(50, 200)
fp=sqrt(g*mp/cd)*tanh(sqrt(g*cd/mp)*t)-v

plt.plot(mp, fp)
plt.grid(True)
plt.show()
