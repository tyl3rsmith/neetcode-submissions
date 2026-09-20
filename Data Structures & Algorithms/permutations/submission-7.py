class Solution:
    def permute(self, nums: List[int],) -> List[List[int]]:
        res, sol = [], []
        used = set()

        def backtrack():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for i in range(len(nums)):
                if i not in used:
                    sol.append(nums[i])
                    used.add(i)
                    backtrack()
                    sol.pop()
                    used.remove(i)

        backtrack()
        return res
                    
        