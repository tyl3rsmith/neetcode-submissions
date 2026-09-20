class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []

        for i, n in enumerate(nums):
            arr.append([n, i])
        
        arr.sort()
        print(arr)
        i = 0
        j = len(nums) - 1

        while i < j:
            curr = arr[i][0] + arr[j][0]
            if curr == target:
                return [min(arr[i][1], arr[j][1]), max(arr[i][1], arr[j][1])]
            elif curr < target:
                i += 1
            elif curr > target:
                j -= 1
        

        
                                                                                                                