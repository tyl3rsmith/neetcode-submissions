class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(nums)

        for i in range(len(nums)):
            complement = -nums[i]

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] == complement:
                    res.append([nums[i], nums[l], nums[r]])
                    # found a valid triplet search for more

                    l += 1
                    r -= 1

                    # avoid duplicates
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif nums[l] + nums[r] < complement:
                    l += 1
                else:
                    r -= 1

        return res