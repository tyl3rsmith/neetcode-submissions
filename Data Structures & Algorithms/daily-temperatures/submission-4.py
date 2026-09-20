class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        for i in range(len(temperatures)):
            j = i + 1
            num_temp = 1
            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    break
                j += 1
                num_temp += 1
            temperatures[i] = 0 if j == len(temperatures) else num_temp
        
        return temperatures

