class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # approach 1: sorting
        if not nums:
            return 0
        
        nums.sort()

        i = 0
        res = 0

        current, streak = nums[0], 0
        while i < len(nums):
            # streak ended need to reset and start a new streak starting at nums[i]
            if nums[i] != current:
                current = nums[i]
                streak = 0

            # skip duplicates
            while i < len(nums) and nums[i] == current:
                i += 1
            
            streak += 1
            current += 1

            res = max(res, streak)
        
        return res

