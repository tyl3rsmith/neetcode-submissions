class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        rightMax, leftMax = [0] * n, [0] * n

        leftMax[0], rightMax[n - 1] = height[0], height[n - 1]

        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        for i in range(n):
            res += min(leftMax[i], rightMax[i]) - height[i]
        
        return res
        