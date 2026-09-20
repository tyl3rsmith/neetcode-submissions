class Solution:
    def hammingWeight(self, n: int) -> int:
        
        res = 0
        for i in range(32):
            bit_mask = 1 << i
            if bit_mask & n:
                res += 1
        
        return res
        
        