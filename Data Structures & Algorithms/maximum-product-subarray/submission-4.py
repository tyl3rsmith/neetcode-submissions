class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_max = cur_min = 1

        for num in nums:
            temp = num * cur_max
            cur_max = max(num * cur_max, num * cur_min, num)
            cur_min = min(temp, num * cur_min, num)
            res = max(res, cur_max)
        
        return res