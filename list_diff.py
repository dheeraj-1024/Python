l=[1,2,3,4,15]
r=[1,2,5,4,1,2]
def diff(l,r):
 m=[]
 for i in l:
  for j in range(len(r)):
   if i==r[j]:
    break
   if j==len(r)-1:
    m+=[i]
 return m
print(diff(r,l)+diff(l,r))
