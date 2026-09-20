class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
            
        def dfs(i, target):
            if i == len(nums):
                return target == 0
            if target < 0:
                return False

            # dont include element
            choice1 = dfs(i + 1, target)
            # include the element
            choice2 = dfs(i + 1, target - nums[i])

            return choice1 or choice2
        
        return dfs(0, sum(nums) // 2)
        