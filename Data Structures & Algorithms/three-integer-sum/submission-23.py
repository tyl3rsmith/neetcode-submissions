class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        print(nums)

        res = []
        for i in range(n - 2):
            # finding all threeSums starting with nums[i]
            if i > 0 and nums[i] == nums[i - 1]: # skip duplicates
                continue

            l, r = i + 1, n - 1
            
            while l < r:
                target = -nums[i]
                current = nums[l] + nums[r]

                if current < target:
                    l += 1
                elif current > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]]) # found a soln
                    l += 1 # shift ptrs to find new soln
                    r -= 1

                    # skip duplicate solns
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        
        return res
