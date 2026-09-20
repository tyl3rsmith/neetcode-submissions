class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap to track the largest stones
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)

        while len(maxHeap) > 1:
            # since its a max heap a >= b
            a, b = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)
            
            if a == b: # both stones destoryed
                continue
            else: # we know a > b
                heapq.heappush(maxHeap, -(a - b))
        
        if len(maxHeap) == 0:
            return 0
        else:
            return -maxHeap[-1]

        
        
        