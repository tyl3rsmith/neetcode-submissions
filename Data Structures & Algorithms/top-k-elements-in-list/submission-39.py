class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        minHeap = []
        for num in counts:
            heapq.heappush(minHeap, (counts[num], num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return [elem[1] for elem in minHeap]
        