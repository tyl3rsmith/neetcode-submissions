class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        def dfs(subset, i):
            if (i == n):
                res.append(subset[:])
                return
            
            # include nums[i] in subset every single num is valid in this path even duplicates
            subset.append(nums[i])
            dfs(subset, i + 1)
            subset.pop()

            # dont include first skip duplicates in list
            while (i + 1 < n and nums[i] == nums[i + 1]):
                i += 1
            
            dfs(subset, i + 1)

        dfs([], 0)
        return res