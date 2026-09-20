class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)

            if heights[l] < heights[r]: # l is the bottleneck
                l += 1
            elif heights[l] > heights[r]: # r is the bottleneck
                r -= 1
            else: # equal heights both bottlenecks
                l += 1
                r -= 1
        return res
