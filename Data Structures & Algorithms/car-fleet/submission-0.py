class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))

        pairs.sort(reverse=True)
        stack = []

        for p, s in pairs:
            distance_to_destination = target - p
            time_to_destination = distance_to_destination / s
            stack.append(time_to_destination)

            will_collide = False
            if len(stack) >= 2:
                will_collide = stack[-1] <= stack[-2]

            if will_collide:
                stack.pop()
        
        return len(stack)
