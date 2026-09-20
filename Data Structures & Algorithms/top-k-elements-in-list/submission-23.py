class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        freq = [[] for _ in range(len(nums) + 1)]
        for num in counts:
            freq[counts[num]].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            if len(res) == k:
                return res
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
                