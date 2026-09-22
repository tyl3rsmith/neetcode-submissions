class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(i, subset):
            if i == n:
                res.append(subset[:])
                return

            # skip nums[i]
            dfs(i + 1, subset)

            # include nums[i]
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()
        
        dfs(0, [])
        return res