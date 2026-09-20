class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        freqList = []
        for num in counts:
            freqList.append([counts[num], num])
        
        freqList.sort()
        print(freqList)

        res = []
        for _ in range(k):
            res.append(freqList.pop()[1])
        
        return res
        

        