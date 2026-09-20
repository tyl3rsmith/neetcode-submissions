class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []

        def backtrack(i):
            if (i >= len(nums)):
                res.append(sol[:])
                return

            # include
            sol.append(nums[i])
            backtrack(i + 1)

            # don't include
            sol.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return res