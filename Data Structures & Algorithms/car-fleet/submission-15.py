class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for p, s in zip(position, speed):
            pairs.append((p, s))
        
        pairs.sort(key = lambda p: p[0], reverse = True)
        carStack = []
        
        for p, s in pairs:
            time_to_dest = (target - p) / s
            carStack.append(time_to_dest)

            if len(carStack) >= 2:
                if carStack[-1] <= carStack[-2]:
                    carStack.pop()
        
        return len(carStack)