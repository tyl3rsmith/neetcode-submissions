class Solution:
    def permute(self, nums: List[int],) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []
        used = [False] * n

        def backtrack():
            if len(sol) == n:
                res.append(sol[:])
                return
            
            for i in range(n):
                if not used[i]:
                    sol.append(nums[i])
                    used[i] = True
                    backtrack()
                    used[i] = False
                    sol.pop()
        backtrack()
        return res

        