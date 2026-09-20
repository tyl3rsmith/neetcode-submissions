class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        for i in range(len(heights)):
            l = i - 1
            r = i + 1
            width = 1

            while l >= 0 and heights[l] >= heights[i]:
                width += 1
                l -= 1
            
            while r < len(heights) and heights[r] >= heights[i]:
                width += 1
                r += 1
            
            currentArea = width * heights[i]
            maxArea = max(maxArea, currentArea)
        
        return maxArea