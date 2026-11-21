class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        best = 0
        nums.sort()

        i = 0
        curr = nums[i]
        streak = 0
        while i < len(nums):
            if curr != nums[i]: # need to reset since the consecutive sequence ended
                streak = 0
                curr = nums[i]

            while i < len(nums) and curr == nums[i]: # skip duplicates and advance pointer
                i += 1
            
            curr += 1
            streak += 1
            best = max(best, streak)
        
        return best