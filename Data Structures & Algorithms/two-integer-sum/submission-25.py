class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for i in range(len(nums)):
            if target - nums[i] in prev:
                return [prev[target - nums[i]], i]
            else:
                prev[nums[i]] = i

