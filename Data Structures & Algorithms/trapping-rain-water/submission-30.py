class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        maxL = [0] * len(height)
        maxL[0] = height[0]

        for i in range(1, len(height)):
            maxL[i] = max(maxL[i - 1], height[i])
        
        maxR = [0] * len(height)
        maxR[len(height) - 1] = height[len(height) - 1]

        for i in range(len(height) - 2, -1, -1):
            maxR[i] = max(maxR[i + 1], height[i])
        
        minArr = [min(maxL[i], maxR[i]) for i in range(len(height))]

        print(maxL)
        print(maxR)
        print(minArr)

        res = 0
        for i in range(len(height)):
            res += minArr[i] - height[i]
        
        return res