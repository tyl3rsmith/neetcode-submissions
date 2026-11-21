class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        # prefix products
        # pref[i] = left product excluding i
        pref = [1] * len(nums)
        for i in range(1, len(nums)):
            pref[i] = pref[i - 1] * nums[i - 1]

        # suffix products
        # suff[i] = right product excluding i
        suff = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            res[i] = pref[i] * suff[i]
        
        return res