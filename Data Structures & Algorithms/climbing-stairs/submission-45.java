class Solution {
    public int climb(int i, int n) {
        if (i == n) {
            return 1;
        }
        if (i > n) {
            return 0;
        }

        return climb(i + 1, n) + climb(i + 2, n);
    }

    public int climbStairs(int n) {
        return climb(0, n);
    }
}
