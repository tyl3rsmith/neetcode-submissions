class Solution {
public:

    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();

        int dp1 = cost[n - 2];
        int dp2 = cost[n - 1];

        for (int i = n - 3; i >= 0; i--) {
            int temp = dp1;
            dp1 = cost[i] + min(dp1, dp2);
            dp2 = temp;
        }

        return min(dp1, dp2);
    }
};
