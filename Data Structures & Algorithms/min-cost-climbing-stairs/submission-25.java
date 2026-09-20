class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int[] dp = new int[cost.length];
        int dp2 = cost[cost.length - 1];
        int dp1 = cost[cost.length - 2];

        for (int i = cost.length - 3; i >= 0; i--) {
            int temp = dp1;
            dp1 = cost[i] + Math.min(dp1, dp2);
            dp2 = temp;
        }

        return Math.min(dp1, dp2);

    }
}
