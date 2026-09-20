class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in counts:
            buckets[counts[num]].append(num)
        
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for elem in buckets[i]:
                if len(res) == k:
                    break
                res.append(elem)

        return res