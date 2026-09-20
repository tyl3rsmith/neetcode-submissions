class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for num in nums:
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1
        
        groups = []

        for num in freqMap:
            groups.append((freqMap[num], num))
        
        groups.sort()

        res = []
        for _ in range(k):
            res.append(groups.pop()[1])
        
        return res