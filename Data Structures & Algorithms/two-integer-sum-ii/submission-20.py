class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # optimized II
        # since its sorted use 2 ptrs 
        
        l, r = 0, len(numbers) - 1

        while l < r:
            current_sum = numbers[l] + numbers[r]

            if current_sum < target: # need to inc search range values
                l += 1
            elif current_sum > target: # need to dec search range values
                r -= 1
            else:
                return [l + 1, r + 1]


        
