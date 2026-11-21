class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        # one bucket for each possible count 0, 1, ..., len(nums)
        # place items into respective bucket based on their count
        # iterate in order of highest count buckets first and add them to our res

        buckets = [[] for _ in range(len(nums) + 1)]
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        for num in counts:
            buckets[counts[num]].append(num)

        res = []
        for i in range(len(nums), -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
