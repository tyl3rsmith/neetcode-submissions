class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) + 1

        while l < r:
            k = l + (r - l) // 2

            time_taken = 0
            for p in piles:
                time_taken += math.ceil(p / k)
                if time_taken > h:
                    break
            
            if time_taken > h: # rate k is too small increase
                l = k + 1
            else: # rate k is good but try to minimize to lower bound
                r = k
        
        # l should point at the lower bound k
        return l



        