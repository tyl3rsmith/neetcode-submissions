class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append([position[i], speed[i]])
        
        pairs = sorted(pairs, reverse=True)
        print(pairs)
        
        stack = []
        for p, s in pairs:
            time_to_dest = (target - p)/s

            if stack and time_to_dest <= stack[-1]:
                continue

            stack.append(time_to_dest)

            print(time_to_dest)
        
        return len(stack)
