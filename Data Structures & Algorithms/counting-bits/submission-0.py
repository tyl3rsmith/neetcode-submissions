class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n + 1):
            num_of_ones = 0
            while num:
                num_of_ones += 1
                num &= num - 1
            res.append(num_of_ones)
        
        return res
        