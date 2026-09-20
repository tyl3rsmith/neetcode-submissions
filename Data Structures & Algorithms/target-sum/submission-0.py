class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def backtrack(i, curr):
            if i == len(nums):
                if curr == target:
                    return 1
                else:
                    return 0
            
            # add nums[i]
            choice1 = backtrack(i + 1, curr + nums[i])

            # subtract nums[i]
            choice2 = backtrack(i + 1, curr - nums[i])

            return choice1 + choice2
        
        return backtrack(0, 0)
            