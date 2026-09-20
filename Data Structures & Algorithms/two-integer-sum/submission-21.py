class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = {}

        for i in range(n):
            diff = target - nums[i]

            if diff in seen:
                return [seen[diff], i]
            
            seen[nums[i]] = i
        return -1