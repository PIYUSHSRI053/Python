#prestore value into datastucture like list/dictionary/sets and the fetching it..

'''Question: conditions
1) 1<n[i]<=10
2) n can have 10^8 elements
3) m can have 10^8 elements
4) no. of element of in m element in n'''

n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]

# method 1
# tc=o(n^2)


# for num in m:
#     cnt=0
#     for x in n:
#         if(x==num):
#             cnt+=1
#     print(cnt)


#  Method 2
# hash_list=[0]*11
# for num in n:
#     hash_list[num]+=1
# for i in m:
#     if (i<1 or i > 10):
#         print(0)
#     else:
#         print(hash_list[i])
# tc=o(n+m) sc=o(11)

# method 3 
freq_dict={}
for num in range (1,len(n)):
    freq_dict[n[num]]=freq_dict.get(n[num],0)+1
for i in m:
   print(i,"=", freq_dict.get(i,0),  end=" , ")