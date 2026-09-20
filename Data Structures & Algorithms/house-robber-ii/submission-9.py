class Solution:
    def helper(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for i in range(len(nums)):
            rob1, rob2 = max(nums[i] + rob2, rob1), rob1
        
        return rob1

    def rob(self, nums) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
