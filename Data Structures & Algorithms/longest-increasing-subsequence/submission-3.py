class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        def dfs(i):
            LIS = 1
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    LIS = max(LIS, 1 + dfs(j))

            return LIS
        
        res = 0
        for i in range(n):
            res = max(res, dfs(i))
        
        return res