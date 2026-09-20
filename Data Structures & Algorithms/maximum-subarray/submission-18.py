class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]

        for i in range(len(nums)):
            currSum = 0

            for j in range(i, len(nums)):
                currSum += nums[j]
        
                best = max(best, currSum)
        
        return best