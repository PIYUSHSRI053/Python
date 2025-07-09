def func(n,sum):
    if(n==0):
        print(sum)
        return
    else:
        sum=sum+n
        n=n-1
    func(n,sum)

n=10    
sum=0
func(n,sum)

