class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        for i in range(n):
            num_days = 1
            j = i + 1
            while j < n:
                if temperatures[j] > temperatures[i]:
                    break
                j += 1
                num_days += 1
            temperatures[i] = 0 if j == n else num_days
        
        return temperatures
        