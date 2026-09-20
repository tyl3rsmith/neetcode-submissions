class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create (position, speed) pairs
        pairs = [(p, s) for p, s in zip(position, speed)]

        # sort by descending position
        pairs.sort(key=lambda x: x[0], reverse=True)

        fleets = 1
        prevCar = (target - pairs[0][0]) / pairs[0][1]

        for i in range(1, len(pairs)):
            curCar = (target - pairs[i][0]) / pairs[i][1]

            if curCar > prevCar:
                fleets += 1
                prevCar = curCar
        
        return fleets
