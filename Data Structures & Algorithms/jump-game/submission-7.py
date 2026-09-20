class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [-1] * len(nums)
        def dfs(i):
            if i == len(nums) - 1:
                return True

            if nums[i] == 0:
                return False
            
            if memo[i] != -1:
                return memo[i] == 1
            
            end = min(len(nums) - 1, i + nums[i])
            for j in range(i + 1, end + 1):
                if dfs(j):
                    memo[i] = 1
                    return True
            
            memo[i] = 0
            return False
        
        return dfs(0)
        