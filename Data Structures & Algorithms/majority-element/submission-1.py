class Solution:
    def majorityElement(self, nums):
        counts = {}
        res = temp_max = 0

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

            if temp_max < counts[num]:
                temp_max = counts[num]
                res = num
        
        return res


