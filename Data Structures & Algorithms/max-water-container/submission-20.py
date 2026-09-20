class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force
        # check every combination of bars
        # compute the area and update maxArea
        res = 0
        l, r = 0, len(heights) - 1
        
        while l < r:
            res = max(res, min(heights[l], heights[r]) * (r - l))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res



