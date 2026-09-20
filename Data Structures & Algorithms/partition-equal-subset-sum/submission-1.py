class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # partitioned into two subsets so that the sum of both subsets is equal
        # total sum // 2 needs to be the sum of the subsets
        # if the total sum is odd it's impossible to have 2 subsets with an equal sum
        if sum(nums) % 2:
            return False

        # memo[i][target] is our cache
        memo = [[-1] * ((sum(nums) // 2) + 1) for _ in range(len(nums) + 1)]

        def dfs(i, target):
            if i == len(nums):
                return target == 0
            if target < 0:
                return False
            
            if memo[i][target] != -1:
                return memo[i][target] == 1

            # dont include element
            choice1 = dfs(i + 1, target)
            # include the element
            choice2 = dfs(i + 1, target - nums[i])

            memo[i][target] = 1 if choice1 or choice2 else 0
            return choice1 or choice2
        
        return dfs(0, sum(nums) // 2)
        