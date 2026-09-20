class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def dfs(i, j): # i: start of LIS, j: last included in LIS
            if i == len(nums):
                return 0
            
            # dont include in LIS
            LIS = dfs(i + 1, j)

            # include in LIS
            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i))

            return LIS
            
        return dfs(0, -1)