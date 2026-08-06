from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print()
        c1 = Counter(s)
        c2 = Counter(t)
        # if c1 == c2:
        #     return True 
        # else:
        #     return False
        if len(s) != len(t):
            return False
        else:
            for ch in c1:
                if c1[ch] != c2[ch]:
                    return False
            return True
        