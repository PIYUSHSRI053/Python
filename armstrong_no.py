from math import *
def cntDigit(num):
    return int(log10(num)+1)

n=int(input("Enter: " ))
temp=m=n
cnt=cntDigit(m)
print (cnt)
total=0
while(n>0):
    r=n%10
    total=total+(r**cnt)
    n=n//10
if(total==temp):
    print("yes")
else:
    print("No")