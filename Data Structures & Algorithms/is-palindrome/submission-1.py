class Solution:
    def isPalindrome(self, s: str) -> bool:
        ref = []
        for i in s.lower() :
            if i.isalnum():
                ref.append(i)
        l = 0 
        r = len(ref)-1 
        while l < r :
            if ref[l] != ref[r]:
                return False
            l +=1
            r -= 1
        return True
            