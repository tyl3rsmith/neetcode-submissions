class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [-1] * len(nums)
        def dfs(i):
            # base case: we reach the end
            if i == len(nums) - 1:
                return True

            if memo[i] != -1:
                return memo[i] == 1

            # how far can we jump from this position
            jumpDist = min(i + nums[i], len(nums) - 1)

            # decision: try every jump
            for j in range(i + 1, jumpDist + 1):
                if dfs(j):
                    memo[i] = 1
                    return True
            
            # no valid jumps to the end if we got here we were stuck
            memo[i] = 0
            return False # invalid path
        
        return dfs(0)
