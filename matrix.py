import numpy as np
m1=np.array([[1,2,3],[4,5,6]])
m2=np.array([[1,2,3],[4,5,6],[7,8,9]])
ans=np.dot(m1,m2)
print("The multiplication of two matrix is:")
print(ans)

user_input=input("Enter a row to be search in Matrix 2(comma-sepreated eg-1,2,3)")
sr=np.array([int(x.strip())for x in user_input.split(',')])
found=any(np.array_equal(row,sr)for row in m2)
if found:
    print("yes")
else:
    print ("no")