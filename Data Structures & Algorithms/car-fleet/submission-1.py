class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = [[p, s] for p, s in zip(position, speed)]
        position_speed.sort(reverse=True)

        stack = []
        for p, s in position_speed:
            time_to_dest = (target - p) / s
            stack.append(time_to_dest)
            if len(stack) < 2:
                continue
            
            if stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)

