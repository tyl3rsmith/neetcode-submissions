class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        res = 0
        for i in range(len(height)):
            maxL = maxR = height[i]

            for j in range(0, i):
                maxL = max(maxL, height[j])
            
            for j in range(i + 1, len(height)):
                maxR = max(maxR, height[j])
            
            res += min(maxL, maxR) - height[i]
        
        return res
