class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create (position, speed) pairs
        pairs = [(p, s) for p, s in zip(position, speed)]

        # Sort by position in descending order
        pairs.sort(key=lambda x: x[0], reverse=True)

        fleets = 1
        prevTime = (target - pairs[0][0]) / pairs[0][1]

        for i in range(1, len(pairs)):
            timeToTarget = (target - pairs[i][0]) / pairs[i][1]

            if timeToTarget > prevTime:
                fleets += 1
                prevTime = timeToTarget
        
        return fleets

