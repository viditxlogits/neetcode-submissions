from collections import Counter 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        for value in counts.values():
            if value > 1 :
                return True
        return False