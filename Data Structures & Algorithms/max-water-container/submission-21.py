class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Use two pointers at the outer bounds to maximize the initial width.
        # Calculate the area using the shorter of the two heights.
        # Move the pointer with the shorter height since it limits the area.
        res = 0
        l, r = 0, len(heights) - 1
        
        while l < r:
            res = max(res, min(heights[l], heights[r]) * (r - l))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res



