class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        element_count_heap = [[counts[num], num] for num in counts]
        heapq.heapify(element_count_heap)

        for _ in range(len(element_count_heap) - k):
            heapq.heappop(element_count_heap)

        return [num[1] for num in element_count_heap]


