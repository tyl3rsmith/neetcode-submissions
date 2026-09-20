class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        left, middle = 0, 1
        result = list()
        maximum_right = len(nums) - 1
        while nums[left] <= 0 and middle < maximum_right:
            right = maximum_right
            while nums[left] + nums[middle] + nums[right] > 0 and right > middle:
                right -= 1
                maximum_right = right
            while middle < right:
                current_sum = nums[left] + nums[middle] + nums[right]
                if current_sum == 0:
                    result.append([nums[left], nums[middle], nums[right]])
                    middle += 1
                    right -= 1
                    while nums[middle] == nums[middle - 1] and middle < right :
                        middle += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    middle += 1
            left += 1
            while nums[left] == nums[left - 1] and left < middle:
                left += 1
            middle = left + 1

        return result