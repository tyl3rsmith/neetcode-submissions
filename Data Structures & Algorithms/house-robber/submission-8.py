class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        
        rob1, rob2 = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            rob1, rob2 = rob2, max(nums[i] + rob1, rob2)
        
        return rob2