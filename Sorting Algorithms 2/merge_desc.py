nums = [2,34,3,23,7,349,48,298,9]

def merge(nums, l, r, mid):
    i = l 
    j = mid+1
    ans = []
    while i<=mid and j<=r:
        if nums[i]>nums[j]:
            ans.append(nums[i])
            i+=1
        else:
            ans.append(nums[j])
            j+=1
    
    while i<=mid:
        ans.append(nums[i])
        i+=1 
    
    while j<=r:
        ans.append(nums[j])
        j+=1 
    
    for i in range(len(ans)):
        nums[l] = ans[i]
        l+=1 
    
def mergeSort(nums,i,j):
    if i>=j: return 
    mid = (i+j)//2
    mergeSort(nums,i,mid)
    mergeSort(nums,mid+1,j)
    merge(nums,i,j,mid)

mergeSort(nums,0,len(nums)-1)
print(nums)