class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j in range(n) and temperatures[i] >= temperatures[j]: # havent found a warmer day
                if res[j] == 0: # no warmer days ahead
                    j = n
                    break
                else:
                    j += res[j]
            
            if j < n:
                res[i] = j - i
        
        return res