class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # division approach
        n = len(nums)

        prod = 1 # product of entire array
        num_zeros = 0 # zero count

        for num in nums:
            if num == 0:
                num_zeros += 1
            else:
                prod *= num

        if num_zeros >= 2: # two or more zeros every position will be 0
            return [0] * n
        
        res = [0] * n

        for i in range(n):
            if num_zeros: res[i] = 0 if nums[i] else prod
            else: res[i] = prod // nums[i]
        
        return res
