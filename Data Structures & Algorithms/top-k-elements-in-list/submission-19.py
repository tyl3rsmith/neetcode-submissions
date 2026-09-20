class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # num, count
        res = []
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        max_elem = nums[0]
        for _ in range(k):
            for num in count:
                if count[num] > count[max_elem]:
                    max_elem = num
            res.append(max_elem)
            count[max_elem] = 0
        
        return res