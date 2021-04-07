import  matplotlib.pyplot as plt
import random
import numpy as np
plt.style.use('seaborn-whitegrid')

ar=np.linspace(-1,2,50000)
#arr=np.linspace(-3500,3500,50000)
#a=[1,2,3,4,5,6,7,8]
for r in range(1,10):
    plt.plot(r+ar,r+ar*0,'--r')
    plt.plot(0*ar+r,r+ar,'--r')
    plt.plot(r+ar,r+1+ar*0,'--r')
    plt.plot(0*ar+r+1,r+ar,'--r')
    #plt.plot(r+ar,(55*r+55*ar)**2)
    #plt.plot((55*r+55*ar)**2,r+ar)


plt.show()