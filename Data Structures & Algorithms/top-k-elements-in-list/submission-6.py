class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort approach
        # map the freq of each value to the index and for the values keep a list
        # of the values with that freq
        # we know the # of indices is prop to the size of the array, the most number of freq for a value would be 6 times
        # start at the end of the array as the most freq are at the right

        buckets = [[] for i in range(len(nums) + 1)]
        res = []
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        for key in freq:
            buckets[freq[key]].append(key)
        

        for j in range(len(buckets) - 1, -1, -1):
            if buckets[j] != []:
                for val in buckets[j]:
                    if len(res) >= k:
                        break
                    else:
                        res.append(val)
        
        return res
        