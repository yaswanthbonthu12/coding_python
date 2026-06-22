#How Many Numbers Are Smaller Than the Current Number

m=[]
 for i in range(len(nums)):
     count=0
     for j in range(len(nums)):
         if nums[i]>nums[j] and i!=j:
             count+=1
     m.append(count)
 return m
