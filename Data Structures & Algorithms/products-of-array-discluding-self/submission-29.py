class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        total_product = 1
        for num in nums:
            if num == 0:
                zero_cnt += 1
            else:
                total_product *= num
        
        if zero_cnt >= 2:
            return [0] * len(nums)
        elif zero_cnt == 1:
            res = []
            for i in range(len(nums)):
                if nums[i] != 0:
                    res.append(0)
                else:
                    res.append(total_product)
            return res
        else:
            res = []
            for num in nums:
                res.append(total_product // num)
            return res