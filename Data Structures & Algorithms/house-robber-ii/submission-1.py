class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        def house_robber_1(nums: List[int]) -> int:
            rob1, rob2 = 0, 0

            for num in nums:
                rob1, rob2 = rob2, max(num + rob1, rob2)
            
            return rob2
        
        return max(house_robber_1(nums[0:len(nums) - 1]), house_robber_1(nums[1:len(nums)]))
