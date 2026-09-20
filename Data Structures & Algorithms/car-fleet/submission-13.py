class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append([position[i], speed[i]])
        
        pairs = sorted(pairs, reverse=True) # no car can pass one ahead of it
        
        stack = []
        for p, s in pairs:
            time_to_dest = (target - p) / s
            stack.append(time_to_dest)

            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
