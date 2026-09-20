class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # dp[i][j+1] = length of LIS starting at index i,
        # with the previous number included at index j.
        for i in range(n - 1, -1, -1):
            for j in range(i - 1, -2, -1):
                # choice 1: skip i
                # If we don’t include nums[i], LIS starting at i
                # is the same as starting at i+1 with the same j.
                LIS = dp[i + 1][j + 1]

                # choice 2: include i
                if j == -1 or nums[j] < nums[i]:
                    LIS = max(LIS, 1 + dp[i + 1][i + 1])
                
                dp[i][j + 1] = LIS

        return dp[0][0]