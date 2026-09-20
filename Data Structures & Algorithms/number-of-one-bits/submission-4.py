class Solution:
    def hammingWeight(self, n: int) -> int:
        
        res = 0
        i = 1
        while n:
            print(i)
            i += 1
            res += 1
            n &= n - 1

        return res
        
        