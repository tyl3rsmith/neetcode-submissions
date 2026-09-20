class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob1(nums: List[int]) -> int:
            n = len(nums)
            rob1, rob2 = 0, 0

            for i in range(n):
                rob1, rob2 = rob2, max(nums[i] + rob1, rob2)
        
            return rob2
    
        return max(rob1(nums[1:]), rob1(nums[:len(nums) - 1]))
