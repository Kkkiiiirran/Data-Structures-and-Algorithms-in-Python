nums = [2,34,3,23,7,349,48,298,9]
for i in range(len(nums)):
    j = i
    while j>0 and nums[j-1] > nums[j]:
        nums[j], nums[j-1] = nums[j-1], nums[j]
        j-=1 
print(nums)

