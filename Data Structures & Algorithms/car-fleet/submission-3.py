class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = [[p, s] for p, s in zip(position, speed)]
        position_speed.sort(reverse=True)

        print(position_speed)

        fleets = 1
        prevTime = (target - position_speed[0][0]) / position_speed[0][1]
        for i in range(1, len(position_speed)):
            curr_time = (target - position_speed[i][0]) / position_speed[i][1]

            if curr_time > prevTime:
                fleets += 1
                prevTime = curr_time
        
        return fleets



