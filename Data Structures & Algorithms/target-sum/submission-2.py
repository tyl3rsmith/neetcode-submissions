class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(i, curr):
            if i == len(nums):
                return curr == target

            # choice 1: add nums[i]
            choice1 = dfs(i + 1, curr + nums[i])

            # choice 2: subtract nums[i]
            choice2 = dfs(i + 1, curr - nums[i])

            return choice1 + choice2
        
        return dfs(0, 0)