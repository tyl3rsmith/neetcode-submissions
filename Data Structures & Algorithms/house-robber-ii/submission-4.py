class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robber(nums: List[int]) -> int:
            rob1, rob2 = 0, 0
            for n in nums:
                rob1, rob2 = rob2, max(n + rob1, rob2)
            
            return rob2
        
        return max(robber(nums[:len(nums) - 1]), robber(nums[1:]))

