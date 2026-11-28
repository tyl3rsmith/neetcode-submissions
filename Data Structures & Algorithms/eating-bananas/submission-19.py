class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            eat_rate = l + (r - l) // 2

            j = 0
            time_taken = 0
            while j < len(piles):
                time_taken += math.ceil(piles[j] / eat_rate)

                if time_taken > h:
                    break

                j += 1
            
            if time_taken <= h and j == len(piles):
                res = eat_rate
                r = eat_rate - 1
            else:
                l = eat_rate + 1
                
        return res