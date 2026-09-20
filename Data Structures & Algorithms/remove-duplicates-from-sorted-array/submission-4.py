class Solution:
    def removeDuplicates(self, nums) -> int:
        num_unique = 1
        
        start = 1
        end = len(nums)
        
        while start < end:
            if nums[start] != nums[start - 1]:
                num_unique += 1
                start += 1
            else:
                nums.pop(start)
                end -= 1
        return len(nums)