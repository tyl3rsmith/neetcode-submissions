class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force
        n = len(heights)
        res = 0

        for i in range(n):
            for j in range(i + 1, n):
                currentArea = min(heights[i], heights[j]) * (j - i)
                res = max(res, currentArea)
        
        return res

        