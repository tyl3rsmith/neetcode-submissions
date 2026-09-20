class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        arr = []
        for i in range(n):
            arr.append([nums[i], i])
        arr.sort()

        l, r = 0, n - 1

        while l < r:
            if arr[l][0] + arr[r][0] == target:
                return [min(arr[l][1], arr[r][1]), max(arr[l][1], arr[r][1])]
            elif arr[l][0] + arr[r][0] < target:
                l += 1
            else:
                r -= 1
        
        return -1