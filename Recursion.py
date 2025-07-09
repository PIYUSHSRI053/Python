# print piyush 4 time
def piyush(n):
    if(n==0):
        return
    else:
        print("Piyush")
    piyush(n-1)
piyush(4) 

# tc=O(n+1)=O(n)
# sc=O(n+1)=O(n)