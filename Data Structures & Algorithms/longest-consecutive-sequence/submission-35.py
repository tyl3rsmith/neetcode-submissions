class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()

        i = 0
        res = 0
        current = nums[0]
        streak = 0

        while i < len(nums):
            # reset streak, try new one
            if current != nums[i]:
                streak = 0
                current = nums[i]

            # skip duplicates
            while i < len(nums) and nums[i] == current:
                i += 1
        

            streak += 1
            current += 1
            res = max(res, streak)
        
        return res