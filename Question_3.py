#Digit Frequency Score

 dic={}
count=0
n=str(n)
for i in n:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
for k,v in dic.items():
    m=int(k)*dic[k]
    count+=m
return count
