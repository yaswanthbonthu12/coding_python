arr=[1,1,2,2,2,3,3]
dic={}
for i in arr:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)
