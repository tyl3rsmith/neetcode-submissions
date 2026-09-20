class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_max = cur_min = 1

        for n in nums:
            temp = n * cur_max # the line after may change cur_max
            # 2 cases:
            # start a new sub array: n
            # extend the subarray: multiply n with min and max since n could be negative
            cur_max = max(n, n * cur_max, n * cur_min)
            cur_min = min(n, temp, n * cur_min)
            res = max(res, cur_max)
        
        return res