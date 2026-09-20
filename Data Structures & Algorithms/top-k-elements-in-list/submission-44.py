class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        element_count = [[counts[num], num] for num in counts]
        element_count.sort(reverse=True)

        for i in range(len(element_count) - k):
            element_count.pop()
        
        return [num[1] for num in element_count]


