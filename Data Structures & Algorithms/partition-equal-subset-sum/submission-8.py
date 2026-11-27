class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #   0 1 2 3 4 5 # target
        # 0 T F F F F F
        # 1 T T F F F F
        # 2 T T T F F F
        # 3 T T T T F F
        # 4 T T T T T T
        # coins available

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)

        dp = [[False] * (target + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True
        
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if i < n and j - nums[i] >= 0:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        # print(dp)
        return dp[n][target]

        [True, False, False, False, False, False]
        [True, True, False, False, False, False]
        [True, True, True, True, False, False]
        [True, True, True, True, True, True]
        [False, True, True, True, True, True]

        [True, False, False, False, False, False]
        [True, True, False, False, False, False]
        [True, True, True, True, False, False]
        [True, True, True, True, True, True]
        [False, True, True, True, True, True]

