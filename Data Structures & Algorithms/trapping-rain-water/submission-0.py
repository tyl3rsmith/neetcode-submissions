class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        leftMax = [0] * n
        leftMax[0] = 0

        curr_max = 0
        for i in range(1, n):
            curr_max = max(curr_max, height[i - 1])
            leftMax[i] = curr_max
        
        rightMax = [0] * n
        rightMax[-1] = 0

        curr_max = 0
        for i in range(n - 2, -1, -1):
            curr_max = max(curr_max, height[i + 1])
            rightMax[i] = curr_max
        

        minLeftRight = [0] * n

        for i in range(n):
            minLeftRight[i] = min(leftMax[i], rightMax[i])
        
        res = 0
        for i in range(n):
            res += max(minLeftRight[i] - height[i], 0)
        
        return res


        print(leftMax)
        print(rightMax)
        print(minLeftRight)
            
            

        