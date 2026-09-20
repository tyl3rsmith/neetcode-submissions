class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {} # (index, curr) -> # ways
        def backtrack(i, curr):
            if i == len(nums):
                if curr == target:
                    return 1
                else:
                    return 0
            
            if (i, curr) in memo:
                return memo[(i, curr)]
            
            # add nums[i]
            choice1 = backtrack(i + 1, curr + nums[i])

            # subtract nums[i]
            choice2 = backtrack(i + 1, curr - nums[i])

            memo[(i, curr)] = choice1 + choice2
            return memo[(i, curr)]
        
        return backtrack(0, 0)
            