class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for num in nums:
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1
        
        res = []
        for _ in range(k):
            currMaxFreq = 0
            maxElem = 0
            for num in freqMap:
                if freqMap[num] > currMaxFreq:
                    currMaxFreq = freqMap[num]
                    maxElem = num
            
            res.append(maxElem)
            del freqMap[maxElem]
        
        return res