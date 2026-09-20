class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                return nums[l]

            m = l + (r - l) // 2
            res = min(res, nums[m])

            # left sorted portion
            if nums[m] >= nums[r]:
                l = m + 1
            else: # right sorted portion min is in here
                r = m
                res = min(res, nums[m])
        
        return res
