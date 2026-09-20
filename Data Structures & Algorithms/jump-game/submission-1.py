class Solution:
    def canJump(self, nums: List[int]) -> bool:

        def dfs(i):
            # base case: we reach the end
            if i == len(nums) - 1:
                return True

            # how far can we jump from this position
            jumpDist = min(i + nums[i], len(nums) - 1)

            # decision: try every jump
            for j in range(i + 1, jumpDist + 1):
                if dfs(j):
                    return True
            
            # no valid jumps to the end if we got here we were stuck
            return False # invalid path
        
        return dfs(0)
