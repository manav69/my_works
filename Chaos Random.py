import turtle as t
import random
import numpy as np
ar1=np.linspace(0,50,100000)
ar2=np.linspace(0,50,200000)
ar3=np.linspace(0,50,300000)
ar4=np.linspace(0,50,400000)
ar5=np.linspace(0,50,500000)

#an=[90,85,80,75]
an=np.linspace(-90,90,180)
#an=[90]
arr=np.linspace(0,1,1000)
a=[1,2,3,4,5,6,7,8]
while True:
    ar = random.choice([ar1, ar2, ar3, ar4, ar5])
    c=random.choice(a)
    s = random.choice(ar)
    ss = random.choice(arr)
    if c==1:
        t.forward(s- s * ss)
        t.right(random.choice(an))
    elif c==2:
        t.back(s - s * ss)
        t.left(random.choice(an))
    elif c==3:
        t.forward(s - s * ss)
        t.left(random.choice(an))
    elif c==4:
        t.back(s - s * ss)
        t.right(random.choice(an))
    elif c==5:
        t.forward(s * ss - s)
        t.right(random.choice(an))
    elif c==6:
        t.back(s * ss - s)
        t.right(random.choice(an))
    elif c==7:
        t.forward(s * ss - s)
        t.left(random.choice(an))
    else:
        t.back(s * ss - s)
        t.left(random.choice(an))
















t.done()