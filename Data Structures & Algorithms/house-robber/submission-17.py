class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        memo = [-1] * n
        def dfs(i):
            if i >= n:
                return 0

            # two choices
            # rob the current house (nums[i] + dfs(i+2))
            # skip this house (dfs(i + 1))

            if memo[i] != -1:
                return memo[i]

            memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return memo[i]
        
        
        return dfs(0)

        