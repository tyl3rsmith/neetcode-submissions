class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # i: current index in nums
        # started: currently inside a sub array or not started one yet
        memo = {}
        def dfs(i, started):
            if i == len(nums):
                # only return 0 if we are in a sub array otherwise an empty subarray has an invalid sum
                return 0 if started else -1e6
            
            if (i, started) in memo:
                return memo[(i, started)]
            
            if started:
                # case 1: inside a subarray, either end or continue
                memo[(i, started)] = max(0, nums[i] + dfs(i + 1, True))
                return memo[(i, started)]

            # case 2: not inside a subarray, either skip or start
            memo[(i, started)] = max(dfs(i + 1, False), nums[i] + dfs(i + 1, True))
            return memo[(i, started)]
        
        return dfs(0, False)

