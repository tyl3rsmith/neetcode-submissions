class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # verify that a solution exists
        if sum(cost) > sum(gas):
            return -1
        
        # if we get here a solution exists
        # we are guaranteed its unique
        totalGas = 0
        res = 0

        for i in range(len(gas)):
            totalGas += gas[i]
            totalGas -= cost[i]

            # greedy: if it dips below 0 it doesnt work
            # try next position and reset total 
            if totalGas < 0:
                totalGas = 0
                res = i + 1
        
        return res