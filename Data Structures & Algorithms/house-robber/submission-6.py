class Solution:
    def rob(self, nums: List[int]) -> int:
        # base case:
            # at house 0 max rob is the money in house 0
            # from house 0 to house 1 max rob is the max between those houses

        # sub problem:
            # the max we can rob from house 0 to house i
            # eventually want to return the last index

        # recurrence
            # from house 2 onwards we want the max we can rob
                # either we can rob house 2 and get the max we can rob 2 houses before house 2
                # or we can not rob house 2 and get the max we can rob 1 house before house 2

        n = len(nums)

        if n == 0:
            return 0
        elif n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return dp[n-1]



