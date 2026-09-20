class Solution:
    def trap(self, height: List[int]) -> int:
        # min of max left height and max right height - current height

        if not height:
            return 0

        res = 0
        for i in range(len(height)):
            leftMax = rightMax = 0

            for j in range(0, i):
                leftMax = max(leftMax, height[j])
            
            for j in range(i + 1, len(height)):
                rightMax = max(rightMax, height[j])
            
            res += max(min(leftMax, rightMax) - height[i], 0)
        
        return res