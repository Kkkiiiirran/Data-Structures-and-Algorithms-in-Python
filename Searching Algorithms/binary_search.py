nums = [1,2,3,4,5,6,7,8]
target = 10

i,j = 0,len(nums)-1

while i<=j:
    mid = (i+j)//2
    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid]<target:
        i=mid+1
    else:
        j=mid-1
else:
    print(-1)