class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        
        for i in range(n):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            low, high = i + 1, n - 1
            while low < high:
                curr_sum = nums[i] + nums[low] + nums[high]
                if curr_sum > 0:
                    high -= 1
                elif curr_sum < 0:
                    low += 1
                else:
                    ans.append([nums[i], nums[low], nums[high]])
                    
                    low += 1
                    high -= 1

                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1

        return ans