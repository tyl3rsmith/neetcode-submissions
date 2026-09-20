class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prev = {}
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in prev:
                return [prev[complement], i + 1]
            prev[numbers[i]] = i + 1
        