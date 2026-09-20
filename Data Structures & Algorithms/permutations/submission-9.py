class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def backtrack(i, sol, used):
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    sol.append(nums[i])
                    used[i] = True
                    backtrack(i + 1, sol, used)
                    used[i] = False
                    sol.pop()
        
        backtrack(0, [], used)
        return res