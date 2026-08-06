class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ref = defaultdict(int)
        for i in nums:
            ref[i] += 1
            if ref[i] > len(nums)//2:
                return i