class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product *= num
        
        if zero_count >= 2:
            return [0] * len(nums)

        res = [0] * len(nums)

        for i in range(len(nums)):
            if zero_count == 1:
                if nums[i] == 0:
                    res[i] = product
                else:
                    res[i] = 0
            else:
                res[i] = product // nums[i]
        
        return res