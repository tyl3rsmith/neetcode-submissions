class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                currArea = (j - i) * min(heights[i], heights[j])
                res = max(res, currArea)

        return res