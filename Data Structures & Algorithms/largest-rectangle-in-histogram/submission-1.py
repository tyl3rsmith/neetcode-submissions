class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0

        for i in range(n):
            # brute force: fix a height and keep extending right and left
            # while its in bounds
            height = heights[i]

            rightMost = i + 1
            # keep moving right until
            # you hit the end or find a smaller height
            while rightMost < n and heights[rightMost] >= height:
                rightMost += 1
            
            leftMost = i
            # keep moving left until
            # we reach the first bar or find a smaller height
            while leftMost >= 0 and heights[leftMost] >= height:
                leftMost -= 1
            
            # Both loops stop one step too far
            # (past the rectangle boundary).

            rightMost -= 1
            leftMost += 1

            # rightMost and leftMost are inclusive indexes add 1
            # so we get the number of bars
            maxArea = max(maxArea, (rightMost - leftMost + 1) * height)
        
        return maxArea