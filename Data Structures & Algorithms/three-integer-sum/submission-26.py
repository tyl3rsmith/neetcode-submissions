class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)):
            complement = -nums[i]

            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] == complement:
                    res.add(tuple([nums[i], nums[l], nums[r]]))
                    # found a valid triplet search for more
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < complement:
                    l += 1
                else:
                    r -= 1

        return [list(x) for x in res]