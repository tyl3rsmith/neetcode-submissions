class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        arr = []
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
    
        for key in freq:
            arr.append([freq[key], key]) # arr is [count, val]

        arr.sort()
        
        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res