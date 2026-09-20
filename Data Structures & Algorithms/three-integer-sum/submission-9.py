class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]: # avoid duplicates
                continue
            
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                curr_sum = nums[i] + nums[lo] + nums[hi]
                if curr_sum > 0:
                    hi -= 1
                elif curr_sum < 0:
                    lo += 1
                else:
                    ans.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1

                    while nums[lo] == nums[lo - 1] and lo < hi: # skip duplicates
                        lo += 1
                    while nums[hi] == nums[hi + 1] and lo < hi:
                        hi -= 1
        
        return ans

