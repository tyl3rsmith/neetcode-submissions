class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # count frequencies
        counts = {} # num -> freq
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        minHeap = []
        # build minHeap
        for num in counts:
            minHeap.append((counts[num], num))
        
        heapq.heapify(minHeap)
        
        # heap should be size k, then it will contain the top k elements after we pop the smallest at the top
        times_to_pop = len(minHeap) - k
        for _ in range(times_to_pop):
            heapq.heappop(minHeap)

        # heap of size k contains the top k elements now
        res = []
        for elem in minHeap:
            res.append(elem[1])
        
        return res