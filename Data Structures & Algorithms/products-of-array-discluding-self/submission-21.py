class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # division approach
        n = len(nums)

        prod = 1 # product of entire array
        for num in nums:
            if num == 0:
                continue
            prod *= num

        num_zeros = 0
        for num in nums:
            if num == 0:
                num_zeros += 1
        
        res = [0] * n
        if num_zeros >= 2: # two or more zeros every position will be 0
            return res
        
        elif num_zeros == 1: # every position besides the spot with a 0 is 0

            for i in range(n):
                if nums[i] != 0:
                    res[i] = 0
                else:
                    res[i] = prod
            
            return res
        
        else: # no zeros present can safely do prod // nums[i]
            for i in range(n):
                res[i] = prod // nums[i]
            
            return res
            

