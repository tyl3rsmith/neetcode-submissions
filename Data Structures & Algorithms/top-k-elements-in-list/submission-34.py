class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        minHeap = [] # least freq element at the top
        for num in counts:
            minHeap.append((counts[num], num))
        
        heapq.heapify(minHeap)

        # for it to be the top k elements the heap needs to be popped until its size k
        times_to_pop = len(minHeap) - k

        for _ in range(times_to_pop):
            heapq.heappop(minHeap)
        
        res = []
        for element in minHeap:
            res.append(element[1])
        
        return res
