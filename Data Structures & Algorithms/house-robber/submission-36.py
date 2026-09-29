class Solution:
    def rob(self, nums: List[int]) -> int:
        # choice 1: rob house[i]
        # choice 2: get max we can rob skipping house[i]

        n = len(nums)
        memo = {}
        def dfs(i):
            if i >= n:
                return 0
            
            if i in memo:
                return memo[i]

            
            choice1 = nums[i] + dfs(i + 2)
            choice2 = dfs(i + 1)

            memo[i] = max(choice1, choice2)
            return memo[i]
        
        return dfs(0)