class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums)
        suff = [1] * len(nums)
        res = [0] * len(nums) 

        product = 1
        for i in range(1, len(nums)):
            product *= nums[i-1]
            pref[i] = product
        
        product = 1
        for i in range(len(nums) - 2, -1, -1):
            product *= nums[i+1]
            suff[i] = product

        print(pref)
        print(suff)
        
        res = [0] * len(nums)
        for i in range(len(pref)):
            res[i] = pref[i] * suff[i]

        return res
