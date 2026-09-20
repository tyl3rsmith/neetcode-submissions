class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for p, s in zip(position, speed):
            pairs.append((p, s))
        
        pairs.sort(key=lambda p: p[0], reverse=True)

        stack = []
        for p, s in pairs:
            time_to_dest = (target - p) / s
            stack.append(time_to_dest)

            if len(stack) >= 2:
                if stack[-1] <= stack[-2]:
                    stack.pop()
        
        return len(stack)