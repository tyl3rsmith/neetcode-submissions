class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                prev_temp, prev_ind = stack.pop()
                res[prev_ind] = index - prev_ind

            stack.append([temp, index])
        
        return res
        