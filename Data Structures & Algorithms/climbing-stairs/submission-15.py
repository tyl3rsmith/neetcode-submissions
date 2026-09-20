class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        # two is ways to get to the nth stair
        # one is ways to get from the n-1th stair to the nth stair

        # to compute ways to get from the n - 2th stairs to the n stair we would do:
            # ways to get to the n th stair from the n - 1th stair (1 step)
            # ways to get to the n th stair from the nth stair (2 steps)
            # i.e. one + two

        for i in range(n - 1):
            one, two = one + two, one

        return one
