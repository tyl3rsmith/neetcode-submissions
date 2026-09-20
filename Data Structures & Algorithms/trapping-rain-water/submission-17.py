class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0

        left = [0] * len(height)
        right = [0] * len(height)

        for i in range(len(height)):
            l, r = i - 1, i + 1
            leftMax = rightMax = 0

            while l >= 0:
                leftMax = max(leftMax, height[l])
                l -= 1
            
            while r < len(height):
                rightMax = max(rightMax, height[r])
                r += 1
            
            left[i] = leftMax
            right[i] = rightMax
        
        
        for i in range(len(height)):
            area = max(min(left[i], right[i]) - height[i], 0)
            maxArea += area
        
        return maxArea


        
                

            