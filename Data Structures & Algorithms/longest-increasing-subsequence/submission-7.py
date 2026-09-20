class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # LIS: prev index is j, current index i
        n = len(nums)
        def dfs(i, j):
            # base case: at the end no sequence LIS is len 0
            if i == n:
                return 0
            
            # decision 1: skip current digit
            LIS = dfs(i + 1, j)

            # decision 2: take the current digit if valid
            # its the first digit i.e. j == -1
            # or the prev is smaller than this digit
            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i))
            
            return LIS
        return dfs(0, -1)