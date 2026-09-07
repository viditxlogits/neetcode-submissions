class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % len(nums)
        def reverse(l:int,r:int) -> None:
            while l < r:
                nums[l],nums[r] = nums[r],nums[l]
                l,r = l+1,r-1
        reverse(0,n-1) # reverse the whole list
        reverse(0,k-1) # first k elements back to original
        reverse(k,n-1) # last set also reversed coming to original state
        