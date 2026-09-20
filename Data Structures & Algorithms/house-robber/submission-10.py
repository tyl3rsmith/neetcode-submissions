class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * (len(nums) + 1)
        
        def dfs(i):
            # if we go out of bounds we get 0
            if i >= len(nums):
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            # either rob the curr house or skip
            memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return memo[i]

        return dfs(0)