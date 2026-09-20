class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # LIS: prev index is j, current index i
        n = len(nums)
        memo = [[False] * (n + 1) for _ in range(n)] # rows: i, cols: j inc by 1 since j can be negative
        def dfs(i, j):
            # base case: at the end no sequence LIS is len 0
            if i == n:
                return 0
            
            if memo[i][j + 1]:
                return memo[i][j + 1]

            # decision 1: skip current digit
            LIS = dfs(i + 1, j)

            # decision 2: take the current digit if valid
            # its the first digit i.e. j == -1
            # or the prev is smaller than this digit
            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i))
            
            memo[i][j + 1] = LIS
            return LIS
        return dfs(0, -1)