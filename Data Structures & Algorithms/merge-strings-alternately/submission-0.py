class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []
        w1 = len(word1)
        w2 = len(word2)
        L1 = w1 if w1 < w2 else w2
        i = 0 
        while i < L1:
            output.append(word1[i])
            output.append(word2[i])
            i+=1
        if w1 > w2:
            output.append(word1[L1:])
        else :
            output.append(word2[L1:])
        result = "".join(output)
        return result