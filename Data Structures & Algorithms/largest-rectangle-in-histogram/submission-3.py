class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (left most index, height)
        maxArea = 0

        for i, h in enumerate(heights):
            start_height = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                curr_area = (i - index) * height
                maxArea = max(maxArea, curr_area)
                start_height = index

            stack.append((start_height, h))
        
        for i, h in stack:
            curr_area = (len(heights) - i) * h
            maxArea = max(maxArea, curr_area)
        
        return maxArea

