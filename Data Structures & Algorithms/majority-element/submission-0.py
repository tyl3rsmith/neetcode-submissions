class Solution:
    def majorityElement(self, nums):
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        temp_max = 0
        majority_element = -1
        for num in counts:
            if counts[num] > temp_max:
                majority_element = num
                temp_max = counts[num]
        
        return majority_element


