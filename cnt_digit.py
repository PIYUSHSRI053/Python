# a=int(input("Enter a no.: "))
# temp=a
# cnt=0
# while(a>0):
#     cnt+=1
#     a=a//10
# print(cnt)


from math import *
def cntDigit(num):
    return int (log10(num)+1)
a=int(input("Enter a no.: "))
print(cntDigit(a))
