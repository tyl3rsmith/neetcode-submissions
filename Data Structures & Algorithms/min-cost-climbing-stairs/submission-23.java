class Solution {
    public int climb(int i, int[] cost, int[] memo) {
        int n = cost.length;

        if (i >= cost.length) {
            return 0;
        }

        if (memo[i] != -1) {
            return memo[i];
        }
        memo[i] = cost[i] + Math.min(climb(i + 1, cost, memo), climb(i + 2, cost, memo));
        return memo[i];

    }
    public int minCostClimbingStairs(int[] cost) {
        int[] memo = new int[cost.length];
        for (int i = 0; i < cost.length; i++) {
            memo[i] = -1;
        }

        return Math.min(climb(0, cost, memo), climb(1, cost, memo));
    }
}
