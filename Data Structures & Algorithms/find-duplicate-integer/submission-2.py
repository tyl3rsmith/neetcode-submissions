class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = [0] * len(nums)
        for num in nums:
            # we know 1 <= num <= n (n + 1 = len of arr)
            if seen[num]:
                return num
            seen[num] = 1
        
        return -1

