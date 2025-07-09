# aa = input("Enter the first string: ")
# # .replace(" ", "").lower()
# bb = input("Enter the second string: ")
# a=list(aa)
# b=list(bb)

# if sorted(a) == sorted(b):
#     print("Yes, it's an anagram.")
# else:
#     print("Not an anagram.")



# a=[]
# l=int(input("enter the length of list:"))
# for i in range (0,l):
#     print("enter",i+1,"element:")
#     b=int(input())
#     a.append(b)
# print (a)
# rl=[]
# for i in range (0,l):
#     if(a[i]%2==0):
#         rl.append("Even")
#     else:
#         rl.append("Odd")
# print (rl)

# Sebseq increasing order

# a=[]
# l=int(input("enter the length of list:"))
# for i in range (0,l):
#     print("enter",i+1,"element:")
#     b=int(input())
#     a.append(b)
# print (a)
# cnt=0
# main_cnt=0
# for i in range(0,l):
#         if(a[i]>a[i-1]):
#             cnt+=1
#         else:
#             main_cnt=max(main_cnt,cnt)
#             cnt=1
# main_cnt = max(main_cnt, cnt)
# print (main_cnt)


# mulltiplication using numppy
# import numpy as np

# A = np.array([[1, 2],
#               [3, 4]])

# B = np.array([[5, 6],
#               [7, 8]])

# result = np.dot(A, B)  # or A @ B in Python 3.5+
# print("Result of matrix multiplication:\n", result)



# Multiplication using for...
# A =([[1, 2],
#      [3, 4]])

# B =([[5, 6],
#     [7, 8]])
# # Perform multiplication
# result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
# for i in range(len(A)):  # rows of A
#     for j in range(len(B[0])):  # columns of B
#         for k in range(len(B)):  # rows of B or columns of A
#             result[i][j] += A[i][k] * B[k][j]
# print("Result of matrix multiplication:")
# for row in result:
#     print(row)

# def func(*function):
#     print("the studend",function[0])
# func("piyush","manoj","mayank","shammmm")

# x="Piyush"
# def func():
#     x="Mayank"
#     print (x)
# func()
# print(x)

# r=int(input("enter the no. of row"))
# c=int(input("enter the no. of column"))
# matrix=[]
# for u in range(r):
#     a=[]
#     for j in range (c):
#         a.append(int(input()))
#     matrix.append(a)
# for i in range(r):
#     for j in range(c):
#         print (matrix[i][j],end = "_")
#     print()



# def harno(number):
#     temp=number;
#     sum=0;
#     while(number>0):
#        t=number%10
#        sum+=t
#        number=number//10
#     if(temp%sum==0):
#         print("Yes")
#     else:
#         print ("no")
#     return

# number =20;
# harno(number)


# def binaryser(arr,l,r,x):
#     arr=sorted(arr)
#     if(l<=r):
#         mid=(l+r)//2
#         if(arr[mid]==x):
#             return mid
#         elif(arr[mid]>x):
#             binaryser(arr,l,mid-1,x)
#         elif(arr[mid]<x):
#             binaryser(arr,mid+1,r,x)
#         else:
#             return -1
#     else:
#         return -1

# arr=[10,230,2,1,32,44]
# x=100
# result=binaryser(arr,0,len(arr)-1,x)
# if(result!=-1):
#     print(f"The position of {x} is",result)
# else:
#     print (f"The {x} is not present")



# import numpy as np
# data_type=[("Name","S15"),("Class",int),("Height",float)]
# student_detail=[("a",7,17.2),("b",3,19.80),("C",6,19.22),("d",7,18.33)]
# a=np.array(student_detail ,data_type)
# print ("Orignal array:")
# print(a)
# print("sorted array")
# print(np.sort(a,order=('Class','Height')))



import numpy as np
arr=[]
n=int(input("Enter the no. of element in array"))
for i in range(0,n):
    print(f"Enter the {i+1} element",end=" ")
    a=int(input())
    arr.append(a)
b=np.array(arr)
print("Median is",np.median(b))
print("Mean is ",np.mean(b))
print("std is ",np.std(b))
print("var is",np.var(b))
