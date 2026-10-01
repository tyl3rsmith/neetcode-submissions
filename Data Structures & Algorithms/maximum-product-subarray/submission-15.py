class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]

        currMin = currMax = 1

        for n in nums:

            temp = currMin

            currMin = min(
                n, # prev elements were all positive
                n * currMin, # n is positive
                n * currMax, # n is negative
            )
            
            currMax = max(
                n, # prev elements were all negative
                n * temp, # n is negative
                n * currMax, # n is positive
            )

            res = max(res, currMax)
        
        return res

