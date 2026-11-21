class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        # find all triplets summing to 0 starting with nums[i]
        for i in range(len(nums)):
            # we can stop looking in this case since subsequent values are all positive
            # it will impossible to get a sum of 0 with all positive numbers
            if nums[i] > 0:
                break

            # we already found all triplets starting with nums[i]
            # skip to avoid duplicate solutions
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]

                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    # try to find more inner solutions
                    l += 1
                    r -= 1

                    # skip inner duplicates on the left
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                    # skip inner duplicates on the right
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                    
        return res