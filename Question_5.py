# Smallest Pair With Different Frequencies

result=[]
dic={}
for i in nums:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

small=min(dic)
for i in sorted(dic):
    if i>small and dic[i]!=dic[small]:
        return [small,i]
        break
return [-1,-1]
