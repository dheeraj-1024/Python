from math import*
import matplotlib.pyplot as plt
import numpy as np
y=np.loadtxt("data.dat",usecols=1)
x=np.loadtxt("data.dat",usecols=0)
y1=[]
for i in x:
 y1+=[tan(i)]
t=np.array(y1)
plt.plot(x,y,'ko')
plt.plot(x,t,'go')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Y vs X")
plt.show()
