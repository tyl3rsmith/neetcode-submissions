class Solution {
    public int climb(int i, int n, int[] memo) {
        if (i == n) {
            return 1;
        }
        if (i > n) {
            return 0;
        }

        if (memo[i] != -1) {
            return memo[i];
        }

        memo[i] = climb(i + 1, n, memo) + climb(i + 2, n, memo);
        return memo[i];
    }

    public int climbStairs(int n) {
        int[] memo = new int[n];

        for (int i = 0; i < n; i++) {
            memo[i] = -1;
        }

        return climb(0, n, memo);
    }
}
