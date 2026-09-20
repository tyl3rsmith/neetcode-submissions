class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in num_map:
                return [num_map[diff], i]
            else:
                num_map[nums[i]] = i
