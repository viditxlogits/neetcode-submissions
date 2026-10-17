class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        res = 0 
        l = 0 
        maxf = 0 
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0) # using dict to store 
            maxf = max(maxf,count[s[r]]) #         counts of letters
            while (r-l+1) - maxf > k : # to validate the win if not then 
                count[s[l]] -= 1  # remove the first element and move
                l +=1

            res = max(res,r-l+1)

        return res