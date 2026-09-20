class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force

        product, zero_count = 1, 0

        for num in nums:
            if num != 0:
                product *= num
            else:
                zero_count += 1
        
        if zero_count > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)

        for i in range(len(nums)):
            if zero_count == 1:
                if nums[i] != 0:
                    res[i] = 0
                else:
                    res[i] = product
            else: # zero_count == 0
                res[i] = product // nums[i]
        return res





        