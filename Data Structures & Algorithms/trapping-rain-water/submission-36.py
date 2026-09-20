class Solution:
    def trap(self, height: List[int]) -> int:
        # prefix and suffix arrays
        # min(maxLeftHeight, maxRightHeight) - height[i]

        leftMax = [height[0]] * len(height)
        for i in range(1, len(height)):
            leftMax[i] = max(height[i], leftMax[i - 1])

        rightMax = [height[-1]] * len(height)
        for i in range(len(height) - 2, -1, -1):
            rightMax[i] = max(height[i], rightMax[i + 1])

        res = 0
        for i in range(len(height)):
            res += min(leftMax[i], rightMax[i]) - height[i]
        
        return res
        
