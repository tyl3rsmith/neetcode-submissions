class Solution:
    def permute(self, nums: List[int],) -> List[List[int]]:
        res, sol = [], []
        used = [False] * len(nums)

        def backtrack(i):
            if (len(sol) == len(nums)):
                res.append(sol[:])
                return res
            
            for i in range(len(nums)):
                if not used[i]:
                    sol.append(nums[i])
                    used[i] = True
                    backtrack(i + 1)
                    sol.pop()
                    used[i] = False
        
        backtrack(0)
        return res
        
        