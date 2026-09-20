class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, curr):
            if i == len(nums):
                return curr == target
            
            if (i, curr) in memo:
                return memo[(i, curr)]

            # choice 1: add nums[i]
            choice1 = dfs(i + 1, curr + nums[i])

            # choice 2: subtract nums[i]
            choice2 = dfs(i + 1, curr - nums[i])

            memo[(i, curr)] = choice1 + choice2
            return memo[(i, curr)]
        
        return dfs(0, 0)