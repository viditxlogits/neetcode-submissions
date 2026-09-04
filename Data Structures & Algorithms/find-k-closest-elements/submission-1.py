class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        result = []
        L = 0 
        R = len(arr)-1
        while L < R and not(R-L+1 == k) :
            if abs(arr[L] - x) < abs(arr[R] - x):
                R-=1 
            elif abs(arr[L] - x) == abs(arr[R] - x):
                R -=1
            else:
                L+=1
        for i in range(L,R+1):
            result.append(arr[i])
        return result