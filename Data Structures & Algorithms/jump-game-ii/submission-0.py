class Solution:
    def jump(self, nums: List[int]) -> int:
        def dfs(i):
            if i == len(nums) - 1:
                return 0
            
            jumpDist = min(i + nums[i], len(nums) - 1)
            minJumps = float('inf')

            for j in range(i + 1, jumpDist + 1):
                minJumps = min(minJumps, 1 + dfs(j))
            
            return minJumps
        
        return dfs(0)

        