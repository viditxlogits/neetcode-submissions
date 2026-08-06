class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return (mergesort(nums))
    
def mergesort(nums):
    if (len(nums) <= 1):
        return nums
    m = len(nums)//2
    left = mergesort(nums[:m])
    right = mergesort(nums[m:])

    return merge(left,right)

def merge(left,right):
    result = []
    i = j = 0 
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return (result)
