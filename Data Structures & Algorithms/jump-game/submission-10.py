class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def dfs(i):
            if i == len(nums) - 1:
                return True
            
            if nums[i] == 0:
                return False
            
            if i in memo:
                return memo[i]

            jump = min(i + nums[i], len(nums) - 1)

            for j in range(i + 1, jump + 1):
                if dfs(j):
                    memo[i] = True
                    return memo[i]
            
            memo[i] = False
            return memo[i]


        return dfs(0)