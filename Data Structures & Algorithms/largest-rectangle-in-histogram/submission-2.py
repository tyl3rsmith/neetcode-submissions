class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0

        for i in range(n):
            current_height = heights[i]

            rightMost = i + 1
            while rightMost < n and heights[rightMost] >= current_height:
                rightMost += 1
            
            leftMost = i
            while leftMost >= 0 and heights[leftMost] >= current_height:
                leftMost -= 1
            
            # last iteration overshot the leftMost and rightMost calculation by 1
            rightMost -= 1
            leftMost += 1

            maxArea = max(maxArea, (rightMost - leftMost + 1) * current_height)
        
        return maxArea