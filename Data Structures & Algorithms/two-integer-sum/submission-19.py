class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = {} # num -> index

        for i in range(n):
            complement = target - nums[i]

            if complement in seen:
                return [seen[complement], i]
                
            seen[nums[i]] = i
        
        return -1


