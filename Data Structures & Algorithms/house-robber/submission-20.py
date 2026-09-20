class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        rob1 = max(nums[n - 1], nums[n - 2])
        rob2 = nums[n - 1]

        for i in range(n - 3, -1, -1):
            rob1, rob2 = max(nums[i] + rob2, rob1), rob1
        
        return rob1
        