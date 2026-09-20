class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def dfs(i, j):
            if i == len(nums):
                return []  # return sequence instead of length
            
            # Option 1: skip current element
            skip = dfs(i + 1, j)
            
            # Option 2: include current element
            take = []
            if j == -1 or nums[j] < nums[i]:
                take = [nums[i]] + dfs(i + 1, i)

            # Return the longer sequence
            if len(take) > len(skip):
                return take
            else:
                return skip

        return len(dfs(0, -1))