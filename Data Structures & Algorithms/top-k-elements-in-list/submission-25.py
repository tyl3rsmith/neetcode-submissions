class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        res = []

        while k > 0:
            curr_max = 0
            max_elem = 0
            for num in counts:
                if counts[num] > curr_max:
                    curr_max = counts[num]
                    max_elem = num
            
            res.append(max_elem)
            del counts[max_elem]
            
            k -= 1
        
        return res