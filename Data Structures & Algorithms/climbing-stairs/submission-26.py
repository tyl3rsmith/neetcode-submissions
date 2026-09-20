class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n

        climb_1, climb_2 = 1, 2

        for i in range(3, n + 1):
            climb_1, climb_2 = climb_2, climb_1 + climb_2
        
        return climb_2