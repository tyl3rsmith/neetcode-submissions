class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []

        for i in range(len(position)):
            pairs.append([position[i], speed[i]])

        pairs = sorted(pairs)[::-1]

        stack = []
        for i in range(len(pairs)):
            curr_position, curr_speed = pairs[i][0], pairs[i][1]
            time_to_dest = (target - curr_position) / curr_speed
            stack.append(time_to_dest)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)



        