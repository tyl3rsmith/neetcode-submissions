class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # sliding window approach
        # remove negative prefix sum
        res = nums[0]
        curSum = 0

        for n in nums:
            # greedy optimization, reset sum / window if we have a negative prefix
            if curSum < 0:
                curSum = 0
            
            curSum += n
            res = max(res, curSum)

        return res