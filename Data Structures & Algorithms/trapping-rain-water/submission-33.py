class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]

        res = 0
        while l < r:
            if maxL < maxR: # left ptr is our bottleneck wall
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else: # right ptr is our bottleneck wall
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        
        return res
            

