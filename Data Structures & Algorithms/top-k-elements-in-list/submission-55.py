class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the occurrence of each element
        # place into a max heap, pop k times

        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        heap = [(-counts[num], num) for num in counts]
        heapq.heapify(heap)
        
        res = []
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res
