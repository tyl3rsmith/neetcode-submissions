class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort algorithm
        # index = count
        # val = num

        buckets = [[] for _ in range(len(nums) + 1)]
        freq = {} # key: num, val: count
        res = []
        
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        for num in freq:
            buckets[freq[num]].append(num)
   
        for i in range(len(buckets) - 1, -1, -1):
            if not buckets[i]:
                continue
            else:
                if len(res) < k:
                    for val in buckets[i]:
                        if len(res) == k:
                            break
                        else:
                            res.append(val)
        
        return res
                



