class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # num -> freq

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 0
        
        min_heap = []

        for num in count:
            heapq.heappush(min_heap, (count[num], num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        res = []

        for i in range(k):
            res.append(heapq.heappop(min_heap)[1])
        
        return res