class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return
            
            # choice 1: include nums[i]
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()

            # choice 2: dont include nums[i]
            dfs(i + 1, subset)
        
        dfs(0, [])
        return res