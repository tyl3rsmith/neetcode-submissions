class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # num -> freq
        freq = [[] for i in range(len(nums) + 1)] # freq -> num

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        for num in count:
            freq[count[num]].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                if len(res) == k:
                    return res
                res.append(num)
        
        return res