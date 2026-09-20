class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # optimized I
        # use a hashmap as a lookup for target - numbers[i]
        
        prev = {}
        for i in range(len(numbers)):
            if target - numbers[i] in prev:
                return [prev[target - numbers[i]], i + 1]
            
            prev[numbers[i]] = i + 1


        
