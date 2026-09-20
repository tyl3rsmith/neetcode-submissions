class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l = i + 1
            r = len(numbers) - 1

            need = target - numbers[i]

            while l <= r:
                m = (r + l) // 2

                if numbers[m] == need:
                    return [i + 1, m + 1]
                elif numbers[m] > need:
                    r = m - 1
                else:
                    l = m + 1
                
        