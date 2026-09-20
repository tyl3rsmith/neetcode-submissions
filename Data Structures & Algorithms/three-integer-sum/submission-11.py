class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        h = {} # num : index
        n = len(nums)
        s = set()

        for i in range(n):
            h[nums[i]] = i
        
        for i in range(n):
            for j in range(i+1, n):
                target = -nums[i] - nums[j]

                if target in h and h[target] != i and h[target] != j:
                    s.add(tuple(sorted([nums[i], nums[j], target])))
        
        return [list(i) for i in s]
