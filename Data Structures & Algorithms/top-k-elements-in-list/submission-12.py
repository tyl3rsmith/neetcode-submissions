class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        arr = []
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        
        for key in counts:
            arr.append([counts[key], key]) # [count, val]

        arr.sort()

        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res
