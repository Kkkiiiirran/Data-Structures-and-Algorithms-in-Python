nums = [1,2,3,4,5,6,7,8]
target = 10
for i in range(len(nums)):
    if nums[i]==target:
        print(i)
        break
else:
    print(-1)

