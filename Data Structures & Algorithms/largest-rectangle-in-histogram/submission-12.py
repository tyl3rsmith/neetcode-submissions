class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        for i in range(len(heights)):
            leftMost = i
            while leftMost >= 0 and heights[leftMost] >= heights[i]:
                leftMost -= 1
            
            rightMost = i + 1
            while rightMost < len(heights) and heights[rightMost] >= heights[i]:
                rightMost += 1
            
            leftMost += 1

            currentArea = heights[i] * (rightMost - leftMost)
            maxArea = max(maxArea, currentArea)
        
        return maxArea


