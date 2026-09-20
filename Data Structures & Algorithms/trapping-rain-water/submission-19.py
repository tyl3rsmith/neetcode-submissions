class Solution:
    def trap(self, height: List[int]) -> int:
        # min of max left height and max right height - current height

        maxLeft = [0] * len(height)
        for i in range(1, len(maxLeft)):
            maxLeft[i] = max(maxLeft[i - 1], height[i - 1])
        
        maxRight = [0] * len(height)
        for i in range(len(maxRight) - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i + 1])
        
        print(maxLeft)
        print(maxRight)

        res = 0
        for i in range(len(height)):
            res += max(min(maxLeft[i], maxRight[i]) - height[i], 0)
        
        return res