class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, total, sol):
            if total == target:
                res.append(sol[:])
                return
            
            # invalid, exit this path
            if i >= len(nums) or total > target:
                return

            # include in sum
            sol.append(nums[i])
            dfs(i, total + nums[i], sol)
            # backtrack
            sol.pop()

            # dont include in sum
            dfs(i + 1, total, sol) 
        
        dfs(0, 0, [])
        return res
