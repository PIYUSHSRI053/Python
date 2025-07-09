# print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
# m = input("Input the name(Capital Only) of Month: ")
# if m == "February":
#     print("No. of days: 28/29 days")
# elif m in ("April", "June", "September", "November"):
#     print("No. of days: 30 days")  
# elif m in ("January", "March", "May", "July", "August", "October", "December"):
#     print("No. of days: 31 days")  
# else:
#     print("Wrong month name")  


# l=[]
# n=int (input("Enter the length of the list: "))
# for i in range(n):  
#     l.append(input("Enter the Element of list: "))
# nl=l[::-1]
# if(nl==l):
#     print("Palindrome Or True")
# else:
    # print("not Palindrome Or False")


# d = {}
# n = int(input("How many items do you want to add: "))
# for i in range(n):
#     key = input("Enter key: ")
#     value = float(input("Enter value (number): "))   
#     d[key] = value  
# print("Final dictionary:", d)
# total = sum(d.values())
# print("The sum Of all the value is: ",total)

print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
m = input("Input the name (Capital Only) of Month: ")
print("No. of days:", "28/29 days" if m == "February" else "30 days" if m in ("April", "June", "September", "November") else "31 days" if m in ("January", "March", "May", "July", "August", "October", "December") else "Wrong month name")

