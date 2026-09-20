class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def dfs(i, started):
            # base case
            if i == len(nums):
                # if we reach the end but the subarray doesnt exist its invalid
                return 0 if started else -1e6

            # currently in a subarray
            if started:
                # two options end or continue the subarray
                return max(0, nums[i] + dfs(i + 1, True))
            
            # not in a subarray
            # can either skip this index or start a new subarray
            return max(dfs(i + 1, False), nums[i] + dfs(i + 1, True))
        
        return dfs(0, False)