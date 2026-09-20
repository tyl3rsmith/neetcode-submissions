class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0

        for i in range(n):
            height = heights[i]

            leftMost = i
            while leftMost >= 0 and heights[leftMost] >= height:
                leftMost -= 1

            rightMost = i + 1
            while rightMost < n and heights[rightMost] >= height:
                rightMost += 1
            
            # last iteration over shot the left and right most
            leftMost += 1
            rightMost -= 1

            maxArea = max(maxArea, height * (rightMost - leftMost + 1))
        
        return maxArea