nums = [1,2,3,3,4,4,6,7,8]
x = 5

i,j= 0,len(nums)-1
ans = 0
while i<=j:
    mid = (i+j)//2
    if nums[mid]<=x:
        ans = nums[i]
        i=mid+1
    else:
        j=mid-1
print(ans)