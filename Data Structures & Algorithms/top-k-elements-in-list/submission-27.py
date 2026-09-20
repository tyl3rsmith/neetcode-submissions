class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
       
        arr = []
        for item in counts:
            arr.append([item, counts[item]])
        
        arr.sort(key = lambda x: x[1])
        
        res = []
        for _ in range(k):
            res.append(arr.pop()[0])
        
        return res
        