def fibo(a):
 i=0
 j=1
 l=[]
 for k in range(a):
  c=i
  i=j
  j=j+c
  l+=[j]
 return l
print(fibo(20))
