class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        temps = [] # pair: (temp, index)
        # maintain a stack
        # if stack is not decreasing then we found the res

        for i in range(len(temperatures)):
            while temps and temperatures[i] > temps[-1][0]:
                temp, index = temps.pop()
                result[index] = i - index

            temps.append((temperatures[i], i))
            print(temps)
        
        return result


        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break
        
        return result


        