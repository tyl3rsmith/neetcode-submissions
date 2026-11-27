class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = sum(nums)

        if n % 2:
            return False

        target = n // 2
        memo = {}

        def dfs(i, target):
            if i >= len(nums):
                return target == 0
            
            if target < 0:
                return False
            
            if (i, target) in memo:
                return memo[(i, target)]
            
            # include in our sum
            choice1 = dfs(i + 1, target - nums[i])

            # skip and dont include in our sum
            choice2 = dfs(i + 1, target)

            memo[(i, target)] = choice1 or choice2
            return memo[(i, target)]

        return dfs(0, target)  