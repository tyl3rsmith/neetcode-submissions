class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i in range(len(nums)):
            A.append([nums[i], i])

        A.sort()
        
        i, j = 0, len(nums) - 1
        while i < j:
            curr = A[i][0] + A[j][0]
            if curr == target:
                return [min(A[i][1], A[j][1]),
                        max(A[i][1], A[j][1])]
            elif curr > target:
                j -= 1
            else:
                i += 1
        
        