class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i in range(len(nums)):
            arr.append([nums[i], i]) # arr[i][j] = [val, index]

        arr.sort() # sorts by arr[i][0] i.e. the value

        i = 0
        j = len(nums) - 1

        while i < j:
            curr = arr[i][0] + arr[j][0]
            if curr == target:
                return [min(arr[i][1], arr[j][1]), max(arr[i][1], arr[j][1])] # indices corresponding to values that summed to target
            elif curr < target:
                i += 1
            else:
                j -= 1

        return arr
                                                                                                            