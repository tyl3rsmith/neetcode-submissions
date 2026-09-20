class Solution:
    def house_robber(self, nums) -> int:
        n = len(nums)
        if n == 0:
            return 0
            
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        
        return dp[n - 1]

    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.house_robber(nums[1:]), self.house_robber(nums[:-1]))
        