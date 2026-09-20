class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        
        while len(stones) > 1:
            # arr is sorted so stone1 >= stone2
            stone1, stone2 = stones.pop(), stones.pop()

            if stone1 == stone2:
                continue
            elif stone1 > stone2:
                stones.append(stone1 - stone2)
                stones.sort()
        
        if stones:
            return stones[0]
        else:
            return 0

