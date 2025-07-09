n="azyxyyzaaaa"
m=["d","a","y","x"]

# method 1
# tc=o(n^2)


# for ch in m:
#     cnt=0
#     ascii_value=ord(ch)
#     for x in n:
#         if(x==ch):
#             cnt+=1
#     print(cnt)


#  Method 2
hash_list=[0]*26
for ch in n:
    ascii_value=ord(ch)
    index=ascii_value-97
    hash_list[index]+=1
for ch in m:
    ascii_value2=ord(ch)
    i=ascii_value2-97
    if (i<0 or i > 26):
        print(0)
    else:
        print(hash_list[i])
# # tc=o(n+m) sc=o(11)

# # method 3 
# freq_dict={}
# for ch in range (1,len(n)):
#     freq_dict[n[ch]]=freq_dict.get(n[ch],0)+1
# for i in m:
#    print(i,"=", freq_dict.get(i,0),  end=" , ")