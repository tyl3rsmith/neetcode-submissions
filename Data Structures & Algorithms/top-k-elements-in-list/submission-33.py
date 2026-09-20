class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqList = [[] for _ in range(len(nums) + 1)]
        freqMap = {} # num -> freq

        for num in nums:
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1
        
        for num in freqMap:
            freqList[freqMap[num]].append(num)
        
        res = []
        for i in range(len(nums), -1, -1):
            for num in freqList[i]:
                if len(res) == k:
                    return res
                res.append(num)
        
        return res
                
