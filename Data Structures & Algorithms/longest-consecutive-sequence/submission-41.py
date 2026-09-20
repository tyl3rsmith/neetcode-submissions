class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for num in numSet:
            curr, length = num, 0

            while curr in numSet:
                length += 1
                curr += 1   
            
            res = max(res, length)
        
        return res
            

