# store freq in dis=ctionary

# method 1 # time complexity (T.C)=O(n), S.C=o(n)

# num=[5,6,7,7,1,9,11,1,1,5,1,1]
# freq_map=dict()
# for i in range(0,len(num)):
#     if num[i] in freq_map:
#         freq_map[num[i]]+=1
#     else:
#         freq_map[num[i]]=1
# print(freq_map)
# print(freq_map[1])



# Method 2 (T.C =O(1))
num=[5,6,7,7,1,9,11,1,1,5,1,1]
hash_map={}
n=len(num)
for i in range (0,n):
    hash_map[num[i]]=hash_map.get(num[i],0)+1
print(hash_map)