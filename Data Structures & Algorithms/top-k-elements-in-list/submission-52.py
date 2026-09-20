class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
            
        heap = [] # heapified by the counts min count always at the top
        for num in counts:
            heapq.heappush(heap, (counts[num], num))

            if len(heap) > k:
                heapq.heappop(heap) # if the size is bigger than k we pop the smallest
        
        # now the heap has the k largest elements
        res = []
        for count, num in heap:
            res.append(num)
        
        return res