class Solution:
    def canJump(self, nums: List[int]) -> bool:

        def dfs(i):
            if i == len(nums) - 1:
                return True
            
            if nums[i] == 0:
                return False

            jump = min(i + nums[i], len(nums) - 1)

            for j in range(i + 1, jump + 1):
                if dfs(j):
                    return True
            
            return False


        return dfs(0)