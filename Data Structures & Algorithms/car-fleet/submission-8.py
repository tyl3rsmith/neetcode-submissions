class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []

        for i in range(len(position)):
            pairs.append([position[i], speed[i]])
        
        stack = []
        for p, s in sorted(pairs)[::-1]:
            time_to_dest = (target - p) / s
            
            if (stack and time_to_dest <= stack[-1]):
                continue
            
            stack.append(time_to_dest)
        
        return len(stack)

        