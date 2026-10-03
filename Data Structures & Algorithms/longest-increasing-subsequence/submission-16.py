class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dfs(i, j): # LIS at I coming from J
            if i >= n:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]
            
            # dont include in LIS
            LIS = dfs(i + 1, j)

            # include in LIS
            if j == -1 or nums[i] > nums[j]:
                LIS = max(LIS, 1 + dfs(i + 1, i))
            
            memo[(i, j)] = LIS
            return LIS

        
        return dfs(0, -1)