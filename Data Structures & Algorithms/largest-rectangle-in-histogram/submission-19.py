class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # optimize with stack
        # maintain monotonically increasing stack of heights
        # if we get a new height less than the prev remove it and calculate those areas
        # at the end stack is all heights that could be extended to the end so calculate those areas

        stack = [] # (index, height)
        res = 0

        for i, h in enumerate(heights):
            start = i

            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                start = index
                res = max(res, height * (i - index))

            stack.append((start, h))
            # print(stack)
        
        for start, height in stack:
            res = max(res, height * (len(heights) - start))
        return res