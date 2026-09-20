class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        res = []

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        max_elem = nums[0]

        for i in range(k):
            for key in counts:
                if counts[key] > counts[max_elem]:
                    max_elem = key
            res.append(max_elem)
            counts[max_elem] = 0

        return res
                
        
        
        