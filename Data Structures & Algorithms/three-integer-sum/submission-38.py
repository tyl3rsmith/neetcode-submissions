class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort() # sort so we can skip duplicates

        # [-4, -1, -1, 0, 1, 2]

        # optimization fix pointer i

        # doing a 2 ptr search on the rest of the list
        # two sum sorted where target = -nums[i]

        # all triplets starting with nums[i]
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            target = -nums[i]
            
            # we found all triplets starting with nums[i] so skip to avoid duplicates
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])

                    # check for more solutions
                    l += 1
                    r -= 1

                    # we want unqiue solutions so we skip duplicates
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1 

                    while l < r and nums[r + 1] == nums[r]:
                        r -= 1

        return result