class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # approach 3:
        # only valid sequence starts are those where nums - 1 is not present

        numSet = set(nums)
        res = 0

        for start in nums:
            if start - 1 not in numSet:
                length = 0
                while (start + length) in numSet:
                    length += 1
                
                res = max(res, length)
        
        return res

            
