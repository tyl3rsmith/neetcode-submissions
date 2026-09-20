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
            minHeap.append((counts[num], num))
        
        heapq.heapify(minHeap)
        
        print(minHeap)
        times_to_pop = len(minHeap) - k
        print(times_to_pop)
        for _ in range(times_to_pop):
            heapq.heappop(minHeap)
        
        print(minHeap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        
        return res
        