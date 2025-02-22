nums = [2,34,3,23,7,349,48,298,9]


for i in range(len(nums)):
    found = False
    for j in range(len(nums)-(i+1)):
        if nums[j]<nums[j+1]:
            nums[j],nums[j+1] = nums[j+1], nums[j]
            found = True
    
    if not found: break

    print(nums)
