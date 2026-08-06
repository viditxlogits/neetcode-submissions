class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0] * 3
        for num in nums:
            bucket[num] +=1 
        index = 0 
        for i in range(len(bucket)):
            t = bucket[i]
            while t > 0 :
                nums[index] = i
                index += 1
                t-=1