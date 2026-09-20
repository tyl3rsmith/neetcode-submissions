class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dfs(i, j):
            # i: current index we're considering
            # j: index of the previous element included

            # base case: no more numbers to consider LIS is len 0
            if i == len(nums):
                return 0
            
            # we dont include i, j stays the same
            LIS = dfs(i + 1, j)
            
            # we include i if its valid
            # valid if there's no prev num: j == -1 or
            # the prev num is smaller than the curr num
            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i)) # include

            return LIS
        
        return dfs(0, -1)