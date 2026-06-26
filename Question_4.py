#Find Words That Can Be Formed by Characters

dic={}

for i in chars:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1

r=0
for k in words:
    temp=dic.copy()
    valid=True
    
    for i in k:
        if i in temp and temp[i]>0:
            temp[i]-=1
        else:
            valid=False
            break
    if valid:
        r+=len(k)
print(r)
