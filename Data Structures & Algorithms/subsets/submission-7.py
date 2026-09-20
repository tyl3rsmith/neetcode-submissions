class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, sol):
            if i == len(nums):
                res.append(sol[:])
                return
            
            # dont include
            backtrack(i + 1, sol)
            
            # include
            sol.append(nums[i])
            backtrack(i + 1, sol)
            sol.pop()
        
        backtrack(0, [])
        return res
        