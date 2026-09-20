class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        # base case if i == n: len of LIS is 0
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        # row: i -> n + 1 rows since base case ends at index n
        # col: j -> n + 1 rows since j can be -1
        # dp[i][j + 1] len of LIS ending at i with prev j

        for i in range(n - 1, -1, -1):
            for j in range(i - 1, -2, -1):
                # dont include nums[i]
                LIS = dp[i + 1][j + 1]

                # include nums[i]
                if j == -1 or nums[j] < nums[i]:
                    LIS = max(LIS, 1 + dp[i + 1][i + 1])
                
                dp[i][j + 1] = LIS
        
        return dp[0][0]