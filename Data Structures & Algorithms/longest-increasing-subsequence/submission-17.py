class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * (n + 1) for _ in range(n)]

        def dfs(i, j): # LIS at I coming from J
            if i >= n:
                return 0

            if memo[i][j + 1] != -1:
                return memo[i][j + 1]
            
            # dont include in LIS
            LIS = dfs(i + 1, j)

            # include in LIS
            if j == -1 or nums[i] > nums[j]:
                LIS = max(LIS, 1 + dfs(i + 1, i))
            
            memo[i][j + 1] = LIS
            return LIS

        
        return dfs(0, -1)