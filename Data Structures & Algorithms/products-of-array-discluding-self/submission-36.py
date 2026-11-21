class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_zeros = 0
        for num in nums:
            if num == 0:
                num_zeros += 1
        
        res = [0] * len(nums)

        if num_zeros == 0:
            total_product = 1
            for num in nums:
                total_product *= num
            
            for i in range(len(nums)):
                res[i] = total_product // nums[i]

        elif num_zeros == 1:
            total_product = 1
            for num in nums:
                if num == 0:
                    continue
                total_product *= num
            
            for i in range(len(nums)):
                if nums[i] == 0:
                    res[i] = total_product
        
        return res