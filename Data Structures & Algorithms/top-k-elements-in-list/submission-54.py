class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        res = []

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        while k > 0:
            maxCount = 0
            maxNum = None

            for num in counts:
                if counts[num] > maxCount:
                    maxNum = num
                    maxCount = counts[num]
            
            res.append(maxNum)
            del counts[maxNum]
            k -= 1
        
        return res