from math import *
res=[]
num=int (input("enter the no.: "))
for i in range (1,int(sqrt(num)+1)):
    if num%i==0:
        res.append(i)
        if num//i!=i:
            res.append(num//i)
print (res)
print("AFTER SORT:")
res.sort()
print (res)