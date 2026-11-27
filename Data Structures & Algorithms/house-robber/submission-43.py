class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            # rob the current house
            choice1 = nums[i] + dfs(i + 2)

            # skip the current house get the best we can get in the remainder
            choice2 = dfs(i + 1)

            memo[i] = max(choice1, choice2) 
            return memo[i]
        
        return dfs(0)