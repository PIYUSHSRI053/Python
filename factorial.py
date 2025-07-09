def fect(n):
    if (n==0):
        return 1
    return n*fect(n-1)

a=int (input("Enter a positive no."))
print(fect(a)) 