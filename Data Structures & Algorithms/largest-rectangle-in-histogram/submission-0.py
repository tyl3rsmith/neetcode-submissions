class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
            start = i

            # we can't extend the height at the top of the stack
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, (i - index) * height)

                # this height is greater than the current height
                # we can extend the current start index back
                start = index
            
            stack.append((start, h))
        
        # there may be some entries left in the stack
        # they were extended all the way to the end
        for i, h in stack:
            maxArea = max(maxArea, (len(heights) - i) * h)
        

        return maxArea

        