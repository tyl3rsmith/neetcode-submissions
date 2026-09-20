class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        res = 0

        for num in nums:

            streak = 0
            current = num

            while current in store:
                streak += 1
                current += 1
            
            res = max(res, streak)
        
        return res