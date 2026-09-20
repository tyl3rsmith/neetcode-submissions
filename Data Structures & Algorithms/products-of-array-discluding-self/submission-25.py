class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # division approach

        prod, zeros = 1, 0
        for num in nums:
            if num != 0:
                prod *= num
            else:
                zeros += 1
        
        if zeros > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)

        for i in range(len(nums)):
            if zeros:
                res[i] = 0 if nums[i] else prod
            else:
                res[i] = prod // nums[i]
        
        return res
