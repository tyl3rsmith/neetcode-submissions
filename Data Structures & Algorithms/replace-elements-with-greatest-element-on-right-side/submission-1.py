class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n == 1:
            return [-1]
        
        res = [0] * n
        res[-1], res[-2] = -1, arr[-1]

        currMax = max(arr[-1], arr[-2])
        for i in range(n - 3, -1, -1):
            res[i] = currMax
            currMax = max(currMax, arr[i])
        
        return res

        