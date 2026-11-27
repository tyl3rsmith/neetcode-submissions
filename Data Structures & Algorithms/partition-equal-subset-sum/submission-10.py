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

        dp = [False] * (target + 1)
        nextDP = [False] * (target + 1)
        dp[0] = True
        nextDP[0] = True

        for i in range(len(nums)):
            for j in range(1, target + 1):
                if j - nums[i] >= 0:
                    nextDP[j] = dp[j] or dp[j - nums[i]]
                else:
                    nextDP[j] = dp[j]
            
            dp, nextDP = nextDP, dp
        
        return dp[target]

