class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        seen = 0

        start = 0
        end = len(nums)

        while start < end:
            if nums[start] == val:
                nums.pop(start)
                end -= 1
                seen += 1
            else:
                start += 1
    

        return len(nums)
        