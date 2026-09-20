class Solution:
    def rob(self, nums: List[int]) -> int:
        # base case: last two spots give 0 in profit
        # [1, 1, 3, 3, rob1, rob2]
        rob1, rob2 = 0, 0

        for i in range(len(nums) - 1, -1, -1):
            rob1, rob2 = max(nums[i] + rob2, rob1), rob1
        
        return rob1