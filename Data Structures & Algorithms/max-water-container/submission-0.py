class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0 
        R = len(heights)-1
        vol_max = 0 
        while L < R:
            col = min(heights[L],heights[R])
            vol = col * (R-L) 
            vol_max = max(vol,vol_max)
            if heights[L] < heights[R]:
                L +=1
            else:
                R-=1
        return vol_max