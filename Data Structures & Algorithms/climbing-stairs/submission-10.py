class Solution:
    def climbStairs(self, n: int) -> int:
        # n: number of steps to reach the top
        # can take 1 or 2 steps at a time
        # want number of distinct ways to reach the top

        cache = [-1] * n
        # [-1, -1]

        def climb(i):
            if i == n:
                return 1
            elif i > n:
                return 0

            if cache[i] != -1:
                return cache[i]
            else:
                cache[i] = climb(i + 1) + climb(i + 2)
                return cache[i]

        return climb(0)

