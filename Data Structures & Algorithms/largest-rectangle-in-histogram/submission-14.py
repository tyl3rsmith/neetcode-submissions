class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        for i, h in enumerate(heights):
            leftMost = i
            while leftMost >= 0 and heights[leftMost] >= h:
                leftMost -= 1
            
            rightMost = i
            while rightMost < len(heights) and heights[rightMost] >= h:
                rightMost += 1
            
            leftMost += 1
            

            maxArea = max(maxArea, h * (rightMost - leftMost))
        
        return maxArea


