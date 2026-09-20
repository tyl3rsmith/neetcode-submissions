class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i in range(len(heights)):
            start = i
            while (stack and stack[-1][0] > heights[i]):
                height, index = stack.pop()
                res = max(res, height * (i - index))
                start = index
            stack.append([heights[i], start])
        
        while stack:
            height, index = stack.pop()
            res = max(res, height * (len(heights) - index))
        
        return res