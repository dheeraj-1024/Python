"""Gives the powers of 2 in Binary Representation of given Decimal Number."""
# evolve : convert to OOP.

l=[]
def binary_power(x,power_limit=25):
 if x==1:
  return 1
 if x==0: 
  return 0
 for i in range(power_limit):
  if x-2**i<0:
   l.append(i-1)
   break
 binary_power(x-2**(i-1))
 return "completed conversion to binary !"

binary_power(100)             # ----------->  call the function
print(l)    		                # ----------->  l gives the list of powers of 2
