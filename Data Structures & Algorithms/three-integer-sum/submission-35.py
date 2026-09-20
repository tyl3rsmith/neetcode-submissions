class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        print(nums)

        for i in range(len(nums)): # find all triplets starting with nums[i]
            if i > 0 and nums[i] == nums[i - 1]: # skip duplicates already found all triplets that start with nums[i]
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]]) # we found a soln need to look for more

                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]: # skip duplicates on left
                        l += 1
                    
                    while l < r and nums[r] == nums[r + 1]: # skip duplicates on right
                        r -= 1
                    
        
        return res
