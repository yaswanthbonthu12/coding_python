#Next Greater Element I

m=[]
for i in range(len(nums1)):
  for j in range(len(nums2)):
      if nums1[i]==nums2[j]:
          found=False
          s=nums2[j+1:]
          for h in range(len(s)):
              if nums2[j]<s[h]:
                  m.append(s[h])
                  found=True
                  break
          if not found:
              m.append(-1)
              
return m
