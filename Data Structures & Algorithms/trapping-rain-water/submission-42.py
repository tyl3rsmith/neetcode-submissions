class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0] * len(height)

        for i in range(1, len(height)):
            leftMax[i] = max(height[i - 1], leftMax[i - 1])
        
        rightMax = [0] * len(height)
        rightMax[-1] = height[-1]

        for i in range(len(height) - 2, -1, -1):
            rightMax[i] = max(height[i + 1], rightMax[i + 1])

        water = 0
        for i in range(len(height)):
            # trapped water = min(maxL, maxR) - curr height
            water += max(0, min(leftMax[i], rightMax[i]) - height[i])
        return water