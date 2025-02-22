nums = [2,34,3,23,7,349,48,298,9]

for i in range(len(nums)):
    found = False
    for j in range(1,len(nums)-i):
        if nums[j]<nums[j-1]:
            found = True
            nums[j], nums[j-1] = nums[j-1], nums[j]
    if not found:
        break
    print(nums)
