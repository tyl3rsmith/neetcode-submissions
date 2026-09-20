class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        product = 1
        zero_count = 0

        for num in nums:
            if num != 0:
                product *= num
            else:
                zero_count += 1
        
        if zero_count > 1:
            return [0] * len(nums)
        
        for i in range(len(nums)):
            if zero_count == 0:
                res[i] = product // nums[i]

            else: # if we have a zero then we need a new formula
                if nums[i] != 0: # means another element must be 0, so the product without nums[i] is 0
                    res[i] = 0
                else: # nums[i] is 0, so the product without nums[i] is the product of everything else
                    res[i] = product
        return res
        