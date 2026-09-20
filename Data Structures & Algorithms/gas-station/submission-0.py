class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        # brute force try every position
        for i in range(n):
            tank = gas[i] - cost[i]

            # we cant reach the next station starting here
            # try a different starting point
            if tank < 0:
                continue
            
            # if we are here we can reach the next station
            j = (i + 1) % n
            while j != i:
                # fill up and pay the cost
                tank += gas[j]
                tank -= cost[j]
                
                # make sure we have enough gas to travel to next station
                # if not we need to try a different start
                if tank < 0:
                    break

                # travel to next station
                j += 1
                j %= n
            
            # we are able to circle around back to the starting station
            # this is our result
            if j == i:
                return i
        
        return -1