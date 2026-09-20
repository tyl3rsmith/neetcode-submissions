class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i, sol):
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in sol:
                    sol.append(nums[i])
                    backtrack(i + 1, sol)
                    sol.pop()
        
        backtrack(0, [])
        return res