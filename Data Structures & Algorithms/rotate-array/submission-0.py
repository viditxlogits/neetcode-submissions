class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        move = len(nums)-k
        for i in range(move):
            nums.append(nums[i])
        del nums[:move]
        
        