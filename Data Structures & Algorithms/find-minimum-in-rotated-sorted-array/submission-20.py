class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            # we got to a fully sorted portion minimum is the left
            if nums[l] < nums[r]:
                res = nums[l]
                break

            m = l + (r - l) // 2
            res = min(res, nums[m])

            # if we are in left sorted portion look right
            if nums[m] >= nums[l]:
                l = m + 1
            # if we are in the right sorted portion try to shrink left to find better res
            else:
                r = m
        
        return res