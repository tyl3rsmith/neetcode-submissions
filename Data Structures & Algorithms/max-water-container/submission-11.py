class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 2 ptr approach
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            currentArea = min(heights[l], heights[r]) * (r - l)
            res = max(res, currentArea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res
   