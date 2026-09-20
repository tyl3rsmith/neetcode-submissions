class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        print(nums)

        # start finding triplets starting with nums[i]
        for i in range(len(nums)):

            # skip duplicate ones we already computed all triplets starting with nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # two sum 2ptr to find the other two
            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]

                if threeSum < 0: # need to inc sum
                    l += 1
                elif threeSum > 0: # need to dec sum
                    r -= 1
                else: # found a valid triplet
                    res.append([nums[i], nums[l], nums[r]])

                    # search for more valid solns
                    l += 1
                    r -= 1

                    # skip duplicates
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                    # skip duplicates
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res

            
