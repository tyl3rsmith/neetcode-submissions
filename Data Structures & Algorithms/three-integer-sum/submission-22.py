class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        [-4, -1, -1, 0, 1, 2]
        for i in range(n - 2):
            # find all triplets starting with nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue # skip past duplicates

            l, r = i + 1, n - 1

            while l < r:
                target = -nums[i]
                current = nums[l] + nums[r]

                if current == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # skip duplicates
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1


                elif current > target:
                    r -= 1
                else:
                    l += 1
        
        return res


