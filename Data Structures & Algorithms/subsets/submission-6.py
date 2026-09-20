class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            for i in range(len(res)):
                subset = res[i][:]
                subset.append(num)
                res.append(subset)
            
        
        return res 