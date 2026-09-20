class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]: # this is a sorted portion
                res = min(res, nums[l])
                break
            
            m = l + ((r - l) // 2)
            res = min(res, nums[m])

            if nums[m] >= nums[l]: # left sorted portion
                l = m + 1
            else: # right sorted portion
                r = m - 1
        
        return res

            
        