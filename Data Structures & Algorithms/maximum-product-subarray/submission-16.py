class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #                      ┌── start new: x
        #              │
        #              ├── extend minimum: x × currMin
        # possibilities
        #              │
        #              └── extend maximum: x × currMax


        currMin = currMax = 1
        res = nums[0]

        for n in nums:
            
            currMin, currMax = min(n, currMin * n, currMax * n), max(n, currMax * n, currMin * n)
            res = max(res, currMax)
        
        return res