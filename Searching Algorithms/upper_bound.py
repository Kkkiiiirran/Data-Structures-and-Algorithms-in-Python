nums = [1,2,3,3,4,5,5,7,8]
x = 5
i,j = 0,len(nums)-1
ans =len(nums)
while i<=j:
    mid = (i+j)//2
    if nums[mid] >=x:
        ans = nums[i]
        j = mid-1
    else:
        i = mid+1

print(ans)
