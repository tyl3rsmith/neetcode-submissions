class Solution {
    public int climb(int i, int[] cost) {
        int n = cost.length;

        if (i >= cost.length) {
            return 0;
        }
        return cost[i] + Math.min(climb(i + 1, cost), climb(i + 2, cost));

    }
    public int minCostClimbingStairs(int[] cost) {
        return Math.min(climb(0, cost), climb(1, cost));
    }
}
