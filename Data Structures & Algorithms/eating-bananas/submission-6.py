class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed, max_speed = 1, max(piles)
        res = max_speed

        while min_speed <= max_speed:
            curr_speed = min_speed + ((max_speed - min_speed) // 2)

            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / curr_speed)
            
            if total_time <= h:
                res = curr_speed
                max_speed = curr_speed - 1
            else:
                min_speed = curr_speed + 1
        
        return res