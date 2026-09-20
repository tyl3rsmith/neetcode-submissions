class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height)
        maxArea = 0

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index

            stack.append((start, heights[i]))
        
        while stack:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (len(heights) - index))
        
        return maxArea