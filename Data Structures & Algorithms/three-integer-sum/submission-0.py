class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            L = i+1 
            R = len(nums)-1
            while L< R:
                sol = nums[L] + nums[R]
                if  sol == target:
                    result.append([nums[i],nums[L],nums[R]])
                    L+=1
                    while L < R and nums[L] == nums[L-1]:
                        L +=1
                elif sol > target:
                    R-=1
                else :
                    L+=1 
        return result