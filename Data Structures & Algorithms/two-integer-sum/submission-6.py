class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {} # val -> index

        for i in range(len(nums)):
            table[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in table and table[complement] != i:
                return [i, table[complement]]
                                                                                                                