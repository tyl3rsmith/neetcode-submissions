class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(val, sol, i):
            if val == 0:
                res.append(sol[:])
                return
            
            if i >= len(nums):
                return

            if val - nums[i] >= 0:
                sol.append(nums[i])
                dfs(val - nums[i], sol, i)
                sol.pop()
            
            dfs(val, sol, i + 1)
        
        dfs(target, [], 0)
        return res

