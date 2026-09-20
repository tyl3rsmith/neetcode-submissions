class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            # maxHeap so stone 1 >= stone2
            stone1, stone2 = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)

            if stone1 > stone2:
                heapq.heappush(maxHeap, -(stone1 - stone2))
            elif stone1 == stone2:
                continue
        
        if maxHeap:
            return -maxHeap[0]
        else:
            return 0
