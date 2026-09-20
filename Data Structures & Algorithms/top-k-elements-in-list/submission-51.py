class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
            
        arr = []
        for num in counts:
            arr.append([counts[num], num])
        
        arr.sort()

        res = []
        for i in range(len(arr) - 1, -1, -1):
            if len(res) == k:
                return res
            res.append(arr[i][1])
        
        return res