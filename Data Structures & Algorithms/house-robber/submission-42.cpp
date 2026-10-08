class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();

        if (n < 2) {
            return nums[0];
        }

        int dp2 = nums[0];
        int dp1 = max(nums[0], nums[1]);

        for (int i = 2; i < n; i++) {
            int temp = dp1;
            dp1 = max(nums[i] + dp2, dp1);
            dp2 = temp;
        }

        return dp1;
    }
};