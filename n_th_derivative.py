import numpy as np
import matplotlib.pyplot as plt
import math

x=np.array([i/100 for i in range(-1000,1001)])
y=np.array([math.exp(i) for i in x])

def diff_n(x,y,n=1):                   # when plotting remember to remove n elements from x, x[n:]
    u=[(y[i+1]-y[i])/(x[1]-x[0]) for i in range(len(y)-1)]
    if n==1:
        return u
    return diff_n(x,u,n-1)

plt.plot(x,y)
plt.plot(x[6:],diff_n(x,y,6))
plt.show()
