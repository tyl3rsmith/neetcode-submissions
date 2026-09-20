class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for num in nums:
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1
        
        minHeap = []

        for num in freqMap:
            minHeap.append((freqMap[num], num))
        
        heapq.heapify(minHeap)

        n = len(minHeap)
        while n > k:
            heapq.heappop(minHeap)
            n -= 1


        res = []
        for num in minHeap:
            res.append(num[1])
        
        return res