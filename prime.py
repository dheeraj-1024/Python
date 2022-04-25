i=100000
for j in range(2,i):
 for k in range(2,j):
  if j%k==0:
   break
  if k==j-1:
   print(j)
