class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        rob1, rob2 = 0, 0

        for i in range(n):
            rob1, rob2 = rob2, max(nums[i] + rob1, rob2)
        
        return rob2