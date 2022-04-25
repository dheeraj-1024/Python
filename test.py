import numpy as np
import random as r
l=10
list=[[r.randint(1,10) for j in range(l)] for i in range(l)]
a=np.asarray(list)

def min(a,b,c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    else:
        return c

def deletion(a):
    row=np.shape(a)[0]
    col=np.shape(a)[1]
    minima = np.min(a[0,1:col-1])
    for j in range(1,col-1):
        if a[0][j]==minima:
            julia=j
            path=[j]
    k=julia
    for i in range(1,row):
        if 0<k<col-1:
            m=min(a[i][k-1],a[i][k],a[i][k+1])
            if a[i][k]==m:
                path+=[col*i+k]
                k=k
            elif a[i][k-1]==m:
                path+=[col*i+(k-1)]
                k=k-1
            elif a[i][k+1]==m:
                path+=[col*i+(k+1)]
                k=k+1
        elif k==0:
            if a[i][k]>a[i][k+1]:
                path+=[col*i+(k+1)]
                k=k+1
            else:
                path+=[col*i+(k)]
                k=k
        elif k==col-1:
            if a[i][k]>a[i][k-1]:
                path+=[col*i+(k-1)]
                k=k-1
            else:
                path+=[col*i+k]
                k=k
    b=np.delete(a,path)
    b=np.reshape(b,(row,col-1))
    return(b)

for i in range(5):
    a=deletion(a)
print(a)