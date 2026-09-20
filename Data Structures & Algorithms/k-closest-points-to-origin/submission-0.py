class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for p in points:
            distance = math.sqrt((p[0] ** 2) + (p[1] ** 2))
            heapq.heappush(maxHeap, (-distance, p))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        return [x[1] for x in maxHeap]