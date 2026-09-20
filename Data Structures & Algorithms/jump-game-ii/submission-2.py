class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[-1] = 0

        for i in range(n - 2, -1, -1):
            jumpDist = min(n - 1, i + nums[i])

            for j in range(i + 1, jumpDist + 1):
                dp[i] = min(dp[i], 1 + dp[j])
        
        return dp[0]
        