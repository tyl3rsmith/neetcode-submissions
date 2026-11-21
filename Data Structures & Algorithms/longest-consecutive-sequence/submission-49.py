class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        best = 0

        for num in nums:
            
            if num - 1 not in numSet:
                curr = num
                streak = 0

                while curr in numSet:
                    streak += 1
                    curr += 1
                
                best = max(best, streak)
    
        return best