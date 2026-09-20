class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create (position, speed) pairs
        pairs = [(p, s) for p, s in zip(position, speed)]

        # sort by descending position
        pairs.sort(key=lambda x: x[0], reverse=True)

        stack = []
        for p, s in pairs:
            time_to_dest = (target - p) / s
            stack.append(time_to_dest)

            # check if they form a fleet
            if len(stack) >= 2: 

                # car 2 reaches before car 1
                if stack[-1] <= stack[-2]:
                    # car 1 is the bottleneck slow car 2 down to car 1
                    stack.pop()
                
                # otherwise car 2 is after car 1 both are on the stack as seperate fleets

        return len(stack)
