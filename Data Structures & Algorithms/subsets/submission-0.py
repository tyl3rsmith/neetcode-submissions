class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def dfs(i):
            if i == n:
                res.append(sol[::])
                return
            
            # dont pick nums[i]
            dfs(i + 1)

            # pick nums[i]
            sol.append(nums[i])
            dfs(i + 1)

            # undo picking nums[i]
            sol.pop()


        dfs(0)
        return res